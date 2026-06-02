![](images/32bdca8f933b0cbbf6eb5a03cb4d86c8bb7e53733f0a1e347b87a95cf0db7e84.jpg)  
Fig. 9.3. Geodetic latitude $\phi _ { \mathrm { g } }$ and geodetic height $h$ of a point $P$ .

Noting that the equation of the ellipse is

$$
\frac { \xi ^ { 2 } } { a ^ { 2 } } + \frac { \zeta ^ { 2 } } { a ^ { 2 } ( 1 - f ) ^ { 2 } } = 1 ,
$$

one gets by differentiation the slope $\phi _ { \mathrm { g } }$ of the normal

$$
\tan \phi _ { \mathrm { g } } = - \frac { \mathrm { d } \xi } { \mathrm { d } \zeta } = \frac { \zeta } { \xi ( 1 - f ) ^ { 2 } } .
$$

The rectangular coordinates of $P$ are

$$
\begin{array} { c } { { x = \xi + h \cos \phi _ { \mathrm { g } } , } } \\ { { { } } } \\ { { z = \zeta + h \sin \phi _ { \mathrm { g } } . } } \end{array}
$$

Equations (9.2) and (9.3) can be used to get $\xi$ and $\zeta$ as functions of $a$ and $\phi _ { g }$ , so that one finally gets:

$$
\begin{array} { l } { \xi = \frac { a } { \sqrt { 1 + ( 1 - f ) ^ { 2 } \tan ^ { 2 } \phi _ { g } } } , } \\ { \zeta = \frac { a \tan \phi _ { g } ( 1 - f ) ^ { 2 } } { \sqrt { 1 + ( 1 - f ) ^ { 2 } \tan ^ { 2 } \phi _ { g } } } , } \end{array}
$$

which, with the expression (9.3), gives the final expressions which are usually written using an intermediate function $C$ :

$$
\begin{array} { l } { C = [ \cos ^ { 2 } \phi _ { \mathrm { g } } + ( 1 - f ) ^ { 2 } \sin ^ { 2 } \phi _ { \mathrm { g } } ] ^ { - 1 / 2 } , } \\ { x = r \cos \phi = a ( C + h / a ) \cos \phi _ { \mathrm { g } } , } \\ { z = r \sin \phi = a ( C ( 1 - f ) ^ { 2 } + h / a ) \sin \phi _ { \mathrm { g } } . } \end{array}
$$

These equations link geodetic and geocentric coordinates, assuming that they have the same coordinate axes. To determine $\phi$ and $h$ , several methods exist and can be found, for instance, in Borkowski (1989) or in Fukushima (1999). Let us note, that, neglecting the deflection of the vertical that will be introduced in Section 9.7.2, we have assumed that the longitudes are the same in both systems.

# 9.5 Physical geodesy

Up to now, we have presented a purely geometrical approach to the description of the Earth. This approach particularly suits space geodesy. However, neither the geocenter, the axes of ITRS, nor the reference ellipsoid are readily available on an observing site, particularly on an astronomical observatory. The ground-based instruments, like transit instruments, or astrolabes (see Section 1.1) refer to the local vertical. The first available coordinate system (Section 3.8) is the horizontal system defined by the azimuth and zenith distance. The vertical direction is defined by a physical property of the Earth, its gravity field. In many respects, there is a tight relationship between the geometrical and the dynamic description of the Earth which is, by nature, in the area of classical geodesy.

# 9.5.1 Earth’s gravitational field

On the surface of the Earth, gravity is actually the result of the gravitational acceleration produced by the planet Earth as a whole, the centrifugal acceleration due to the rotation of the Earth, and several additional components due to the attraction by the Moon and the Sun (tidal accelerations), as well as to the particular mass distribution in the environment, giving rise to gravity anomalies.

The theory of the gravitational field of the Earth is based upon the classical potential theory that provides the tools to compute the gravitational potential outside the Earth. Let $G$ be the constant of gravitation, and $\rho ( \xi , \eta , \zeta )$ the density of a point $Q$ with coordinates $\xi , \eta , \zeta$ . According to Newton’s law, each element $\boldsymbol { Q }$ produces on an external point $P ,$ with coordinates $x , y , z ,$ an attractive force

$$
{ \bf d F } = - G _ { \rho } ( \xi , \eta , \zeta ) { \bf d } \xi { \bf d } \eta { \bf d } \zeta \frac { { \bf Q } { \bf P } } { { \cal Q } P ^ { 3 } } ,
$$

whose three components are the partial derivatives of the potential

$$
\mathrm { d } U = G \frac { \rho ( \xi , \eta , \zeta ) \mathrm { d } \xi \mathrm { d } \eta \mathrm { d } \zeta } { \sqrt { ( x - \xi ) ^ { 2 } + ( y - \eta ) ^ { 2 } + ( z - \zeta ) ^ { 2 } } } .
$$

Integrating it over the whole volume of the Earth, one obtains the Earth’s full gravitational potential $U$ . There is no finite expression for $U _ { i }$ , and the integration is possible only for points outside a sphere, which includes all elements of the Earth, so that the denominator of (9.6) does not vanish. Under this assumption, at a point $P$ defined by its spherical coordinates, $r , \phi$ $\phi , \lambda$ , in a terrestrial reference system centered at the geocenter, the potential $U$ is, as a rule, written as a development in spherical harmonics with the following notations:

$$
\begin{array} { l } { { \displaystyle { \cal U } = \frac { G M } { r } \Biggl [ 1 - \sum _ { k = 2 } ^ { \infty } \left( \frac { a } { r } \right) ^ { k } J _ { k } P _ { k } ( \sin \phi ) + \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { \infty } \left( \frac { a } { r } \right) ^ { n } ( C _ { n m } \cos m \lambda } } \\ { { \displaystyle ~ + S _ { n m } \sin m \lambda ) P _ { n m } \cos \phi \Biggr ] } , } \end{array}
$$

where the following conditions hold.

(i) $G M$ is the geocentric gravitational constant whose conventional best value is

$$
G M = ( 3 . 9 8 6 0 0 4 4 1 8 \pm 8 ) \times 1 0 ^ { 5 } \mathrm { m ^ { 3 } / s ^ { 2 } } .
$$

(ii) $a$ is a scaling constant, conventionally taken as equal to the equatorial radius of the Geodetic Reference System: $a = 6 3 7 8 1 3 6 . 6 \mathrm { m }$ (see Section 9.1).

(iii) $P _ { k }$ are Legendre polynomials and $P _ { n m }$ are Legendre functions of the first kind that are of degree $n$ and order m. They may or may not be normalized; the normalization coefficient being, or not, put into the coefficients $J _ { n }$ , $C _ { n m }$ and $S _ { n m }$ .

(iv) $J _ { k }$ are called the zonal harmonics, and $C _ { n m }$ , $S _ { n m }$ are the tesseral harmonics.

# Remarks.

- By construction, since the center of mass is at the origin of coordinates, $J _ { 1 } =$ $C _ { 1 1 } = S _ { 1 1 } = 0$ .   
- The values of $C _ { 2 1 }$ and $S _ { 2 1 }$ depend on the shift between the polar axis of ITRF and the axis of rotation of the Earth (see Section 10.4.1).   
- The coefficient $J _ { 2 }$ is called the dynamical form factor of the Earth and is connected to its mean flattening. A conventional value has been adopted by both the IUGG and the GRS:

$$
J _ { 2 } = 0 . 0 0 1 0 8 2 6 3 9 5 .
$$

This actually varies with time, essentially because of the post-glacial rebound and the melting of Antarctic ice (Section 9.9.2).

The values of the zonal and tesseral harmonics are determined by space geodesy methods, that essentially model gravitational and other forces acting on the motions of artificial satellites, which are observed by various techniques (Doppler, laser ranging, altimetry, etc.). The coefficients of the models – such as Equation (9.7) for the gravitational effects – are determined to minimize the observing residuals (see, for instance, Zarrouati, 1997). A review of various integration methods is to be found in Kinoshita and Kozai (1989). The results are given in the form of lists of values of the spherical harmonics, and constitute Earth potential models. Three series of such models exist and they are periodically improved by adding new data. These are:

- the GEM series (Goddard Earth Models) constructed at NASA, Goddard Space Flight Center,   
- the JGM models (University of Texas, Austin), and   
- the GRIM series (GRGS – Institute of Munich) developed jointly by CNES (Toulouse) and DGFI (Munich).

The models differ in their details, but are roughly of the same quality. The maximum order and degree now reach about 70, representing some 10 000 coefficients in (9.7). The accuracy with which they represent the motion of a satellite depends upon the satellite. For most of the distant satellites, the uncertainty in the representation is in the range of one to a few centimeters.

# 9.5.2 Gravity on the surface of the Earth

It is not legitimate to extrapolate directly formula (9.7) toward the Earth and derive the potential at the level of the Earth’s surface. It has to be done stepwise, by removing the effects of the atmosphere and surrounding ground effects. This is currently being done, and one obtains the potential at any point in the vicinity of the Earth. The differences with the coefficients of the gravitational Earth models are small, and the form of Equation (9.7) can be kept, provided that the centrifugal potential

$$
V = \frac { 1 } { 2 } \omega _ { 0 } ^ { 2 } ( X ^ { 2 } + Y ^ { 2 } ) ,
$$

where $\omega _ { 0 }$ is the angular velocity of the Earth, is added.

There is a particular equipotential surface that is of great importance for geodesy. It is the geoid, a surface from which the heights are evaluated. In the past, it was defined as the shape of the equipotential surface that best fits the mean surface of the oceans. It represented the shape the Earth would have, if it were entirely covered with oceans at rest. This definition is too imprecise for the needs of very accurate geodesy and terrestrial time definition (Section 5.5.1). It is now defined as the surface on which the geopotential is

$$
U _ { \mathrm { G } } = 6 2 6 3 6 8 5 6 \mathrm { m } ^ { 2 } / \mathrm { s } ^ { 2 } .
$$

As an illustration, we present in Fig. 9.4 the heights of the geoid with respect to the GRS ellipsoid. At the global level of this figure, all the models are alike, and differ only in detailed local features. The large-scale deformations that can reach $\pm 1 0 0 \mathrm { m }$ are not correlated with surface relief, and actually result from large mass anomalies deep in the mantle. Over the oceans, very detailed maps of the geoid are now obtained with satellite radar altimetry (Topex-Poseidon, Jason, or ERS missions). Individual height measurements with respect to the ITRF are obtained with uncertainties of the order of a few centimeters. As a result, the ocean geoid is now mapped with a resolution of $5 0 { \mathrm { - } } 1 0 0 \ \mathrm { k m }$ , and a height uncertainty of $2 { - } 5 \ \mathrm { c m }$ . The small structures observed are highly correlated with the sea-floor topography. These observations also give a refined view of the oceanographic contributions to the heights of the oceans, owing to tides, currents, and associated eddies, winds, atmospheric pressure, and water density.

![](images/0b2bdad63fa7d5a656b54054e96189fb59337ec7cb6fa448df257a1e63aece06.jpg)  
Fig. 9.4. Map of the largest features of the geoid as derived from one of the versions of the GRIM4 model and referred to the GRS ellipsoid. The approximate heights, in meters, of the main features are indicated. The heavy line corresponds to zero height.

At this point, it is necessary to stress the practical importance of the geoid. It is the surface to which all geographic heights are referred. The extension of the system of heights is made by geodetic leveling calibrated on tidal gauges. Lately, gravimetric methods replaced leveling. On the ground, the main origin of gravity data is gravimetry. Various campaigns have covered the major part of the continental crust. The results are assembled and discussed by the Bureau Gravim´etrique International (BGI) at Toulouse and transformed into geoid height maps as well as surface gravity data files. These corrections are to be applied to get the gravity at the reference ellipsoid: the free air correction for topography to take into account the crust in the environment, and the isostasic correction to compensate for the effect of the weight of the relief on the reaction of the mantle on the crust. These corrections, and the way to obtain the direction of the vertical on the ellipsoid, are part of physical geodesy, a classical science described in text books on ground-based geodesy (see, for instance, Moritz, 1980).

![](images/abb6495016a21d2567bea5c80188fb2588a9be1789b4ffc9afdc380bddda54b7.jpg)  
Fig. 9.5. General definition of the longitude $( \lambda )$ and the latitude $( \phi )$ of a point $M$

# 9.6 Coordinates of a point on the Earth

In Section 9.4 we introduced two types of terrestrial coordinates. However, the principal parameter that is required for classical ground-based astrometry is the direction, in the terrestrial reference frame, of the vertical at the observatory site. This involves a third type of coordinates. So, let us take up again the definition of angular coordinates on the Earth.

The position of a point $M$ is defined by two spherical coordinates: its latitude and its longitude (Fig. 9.5). The general definition of latitude is

$$
9 0 ^ { \circ } - ( \mathbf { M P } , \mathbf { M z } ) ,
$$

where MP is the direction of the pole and Mz the direction of a particular vertical. The angle $( \mathbf { M P } , \mathbf { M z } )$ is the colatitude. The other coordinate is the longitude, defined as the angle, reckoned eastward between the plane of the origin meridian and the plane $P M z .$ . Although in the past, the opposite sign convention was sometimes adopted, we shall use this convention: the East is positive, so the longitudes in Asia are positive; in America they are negative.

Because of the different approaches to the vertical as described in the preceding sections, there are three different types of coordinate, each of them having a specific use in describing the positions of points on the Earth’s surface. Two of them have been already defined in Section 9.4.

- The geocentric coordinates. Let XYZ be the rectangular coordinates of $M$ in the ITRF. The latitude and the longitude are respectively defined by

$$
\begin{array} { l } { { \phi = \tan ^ { - 1 } ( Z / \sqrt { X ^ { 2 } + Y ^ { 2 } } ) , } } \\ { { \varLambda = \tan ^ { - 1 } ( Y / X ) \quad \mathrm { f o r } \quad X > 0 , \mathrm { a n d } } } \\ { { \varLambda = 1 8 0 ^ { \circ } + \tan ^ { - 1 } ( Y / X ) \quad \mathrm { f o r } \quad X < 0 . } } \end{array}
$$

- The geodetic coordinates. They are defined with respect to the reference ellipsoid. The geodetic latitude is the angle $\phi _ { \mathrm { g } }$ between the equatorial plane and the normal to the reference ellipsoid, defined in Section 9.4 and illustrated by Fig. 9.3. We assume, as it is generally the case, that the equator of this ellipsoid is the $X O Y$ plane of the ITRF. Then, the geodetic longitude, $\lambda _ { \mathrm { g } }$ , is equal to $\varLambda$ .

Let us now introduce a third type of coordinate. The vertical is defined as the direction perpendicular to the local potential surface or, in other words, the direction of the gravity acceleration. The corresponding coordinates are called astronomical coordinates, or geographic coordinates. The vertical, which defines them does not coincide with the direction of the normal to the reference ellipsoid, whose direction is given by Equation (9.2), nor is it the direction OP in Fig. 9.3. The astronomical latitude, $\phi$ , is the angle between the physical vertical and the equatorial plane, which is perpendicular to the direction of the celestial pole (Fig. 9.6). The astronomical longitude, $\lambda$ , is the angle between the origin meridian and the (PZ, z) plane.

The angle between the direction of the vertical and the normal to the reference ellipsoid is the deflection of the vertical, which has a North–South component, $\xi$ , and an East–West component, $\eta$ . If we assume – and this point will be discussed in Chapter $1 0 -$ that the celestial pole is the celestial intermediate pole, defined as the extension on the celestial sphere of the $O Z$ axis of the ITRF, then by definition of the North–South component of the deflection of the vertical, one has

$$
\phi = \phi _ { \mathrm { g } } + \xi .
$$

Here, $\phi$ is the latitude actually measured by astronomical instruments such as meridian circles or astrolabes, after correction for polar motion with respect to the celestial intermediate pole (Section 10.4.2). Similarly, the East–West deflection of the vertical modifies the longitude, $\lambda _ { g }$ , which is shifted by an angle corresponding to the East–West vertical deflection, $\eta$ ,

$$
\lambda = \lambda _ { \mathrm { g } } - \eta / \cos { \phi } .
$$

![](images/37a9e7680147e7a24a8f798b3ed31adf6e9385e59cbdd4cc81f8f525d40110d3.jpg)  
Fig. 9.6. Astronomical and geodetic coordinates and the deflection of the vertical $( \xi , \eta )$ . $z$ is the physical vertical and $z _ { \mathrm { g } }$ is the normal to the ellipsoid.

This formula defines the sign of $\eta$ . Applying these corrections to the computable normal to the reference ellipsoid, one gets the components of the on-site vertical direction in the terrestrial reference frame (see Section 9.7.2).

We have mentioned that the geodetic system of terrestrial coordinates is very much used for various purposes. The geodetic coordinates are those that appear on maps. But the astronomical coordinates are necessarily present in local astronomical observations, which are referred to the physical vertical and the local meridian, defined as the vertical plane containing the direction of the celestial pole.

# 9.7 Topocentric astronomical coordinates

In what follows, we shall assume that all corrections to observations, in particular for astronomical refraction, are made, and assume that celestial directions are those from which the light arrives when reaching the vicinity of the Earth. Two topocentric coordinate systems, already presented in Section 3.10.3, are used.

The horizontal system of celestial coordinates, also called the alt-azimuth system, is based on the direction of the zenith, $Z ,$ and the horizontal plane, perpendicular to the local vertical. The origin on this plane is its northern intersection with the meridian plane. In Fig. 9.7, the position of a point, $M$ , on the celestial sphere is defined by two angles. One is the zenith distance

$$
z = ( O Z , O M )
$$

or the altitude $h = 9 0 ^ { \circ } - z$ .

![](images/15ca48ca8745d6a0197ab71fbdc30a167036f1af5dcdc5d2e188d14bad7e14f1.jpg)  
Fig. 9.7. The alt-azimuth topocentric coordinates $A , z$ , or $h$ , and associated angles in the celestial sphere.

The other angle is the azimuth, $A$ , of the half vertical plane ZOM with the northern half meridian reckoned clockwise (towards East). Actually there are several other conventions used, such as counterclockwise (direct) reckoning, and/or with an origin at the southern point of the meridian. In this book, we use the most generally accepted definition given above (Fig. 9.7).

The other commonly used topocentric coordinate system is the local equatorial system (see Fig. 9.8) which, like the celestial reference system, is defined by the direction of the pole and the intermediate equator as defined by its pole, the Celestial Intermediate Pole (CIP, see Section 10.4.2). The two coordinates are the intermediate declination $\delta _ { \mathrm { i } }$ , defined as in the celestial system, and the local hour angle $H$ , reckoned westward from the meridian plane. It is related to the right ascension by the equation

$$
H = T _ { \mathrm { l } } - \alpha _ { \mathrm { i } } ,
$$

where $T _ { \mathrm { l } }$ used to be the local sidereal time, which was defined as the hour angle of the equinox, or $\gamma$ point. Now, with the definition of the Celestial Ephemeris Origin (CEO, see Section 10.3.1) as the origin of the right ascensions in the intermediate celestial reference system $( \alpha _ { \mathrm { i } } )$ , $T _ { \mathrm { l } }$ is the local stellar angle (see Section 10.4.4), and the corresponding declination is the intermediate declination $\delta _ { \mathrm { i } }$ . One

![](images/d17cbf48d1f5389df888bb1be4c3b571f71bcaf803b18049491f73fbf1e27edd.jpg)  
Fig. 9.8. The equatorial $H$ , δ, topocentric coordinates; $\phi$ is the astronomical latitude of the observer.

has also

$$
H = T + \lambda - \alpha _ { \mathrm { i } } ,
$$

where $\lambda$ is the longitude, and $T$ was the Greenwich sidereal time of the prime meridian of the ITRF and now is the stellar angle of the same meridian.

With the exception of the declination δ, the three other coordinates, $z , A$ and $H$ vary with time because of the rotation of the Earth. In addition, together with $\delta$ , they may be biased by the possible deflection $\xi , \eta$ of the vertical and its time variations due, for instance, to underground hydrology.

As the first step to comparisons between observations made from different locations, it is necessary to transform them into coordinates as seen from a common reference point, chosen to be the geocenter. This is done in two or three steps depending upon the system in which the observations are performed. They are described in the following sub-sections.

# 9.7.1 Transformation from horizontal to equatorial coordinates

This transformation corresponds, as seen on Fig. 9.8, to a rotation around the West– East axis by the angle $( O Z , O P )$ ) equal to $9 0 ^ { \circ } - \phi$ , where $\phi$ is the astronomical latitude (Section 9.6). In the right-handed, local horizontal rectangular coordinates $O ( x y z )$ , the components of a unit vector $\mathbf { V }$ are

$$
\mathbf { V } \left\{ { \begin{array} { c } { - \sin z \cos A , } \\ { \sin z \sin A , } \\ { \cos z . } \end{array} } \right.
$$

In the equatorial local system, one has

$$
\mathbf { V } ^ { \prime } \left\{ \begin{array} { c } { \cos \delta \cos H , } \\ { - \cos \delta \sin H , } \\ { \sin \delta . } \end{array} \right.
$$

One obtains $\mathbf { V } ^ { \prime }$ by applying to $\mathbf { V }$ the rotation $\mathcal { R } _ { y } ( \phi - 9 0 ^ { \circ } )$ , or the following direct relations

$$
\left. \begin{array} { c } { { \cos \delta \cos { H } = \cos \phi \cos z - \sin \phi \sin z \cos { A } , } } \\ { { \cos \delta \sin { H } = - \sin z \sin A , } } \\ { { \sin \delta } } \end{array} \right\}
$$

From this, one gets unambiguously $\delta$ and $H .$ . The inverse relation can readily be obtained by a similar method:

$$
\left. \begin{array} { c } { { \sin z \cos A = \cos \phi \sin \delta - \sin \phi \cos \delta \cos \cal H , } } \\ { { \sin z \sin A = - \cos \delta \sin \cal H , } } \\ { { \cos z } } \end{array} \right\}
$$

# 9.7.2 Correction for the deflection of the vertical

Because of the local deflection of the vertical, the direct transformation from the local equatorial system to the geocentric system is not possible. It is necessary first to align the local coordinate axes with the geodetic coordinates. From Equations (9.10) and (9.11), the correction is equivalent to a change in latitude such that

$$
\phi _ { \mathrm { g } } = \phi - \xi .
$$

The rotation of $\eta / \cos \phi$ in longitude is equivalent to a change in the hour angle, so that the new value is

$$
H _ { \mathrm { g } } = H + \eta / \cos { \phi } .
$$

The actual values of the deflection of the vertical can be computed from the regional gravity anomalies by formulae derived by Vening Meinesz (see Heiskanen and Moritz, 1967). It can also be determined by comparing the geodetic latitude and longitude, as deduced from observations of the site position by GPS, which gives the geocentric coordinates, and the astronomical coordinates as deduced from observations of stars with known positions in the celestial reference frame, for instance using transit instruments. This method is also advantageous because it can be repeated, and time-dependent deflections of the vertical, owing for instance to modifications of the level of underground water, can be monitored.

# 9.7.3 Computation of the geocentric coordinates

The transformation from the geodetic to geocentric coordinates is straightforward as far as directions are concerned. The longitude is unchanged $( \varLambda = \lambda _ { \mathrm { g } }$ ) and the geocentric latitude, $\varPhi$ , can be obtained from formulae (9.5). The problem is more complicated for the observations of bodies in the Solar System, for which the shift from topocentric to geocentric coordinates changes significantly with the directions in which they appear. The correction for this is the diurnal parallax. For the Moon, and even more so for artificial satellites, it is a major change in coordinates, which has to be computed with a very high accuracy.

We suppose that the geocentric coordinates of the observer, OP, are known, for instance from GPS observations. If the topocentric coordinates of the object PS were also known, the solution would be straightforward through applying the vectorial addition

$$
\mathbf { O S } = \mathbf { O P } + \mathbf { P S } .
$$

This is not generally the case. The distance from the observing site to the observed body is not known, and one is led to use the geocentric distance as found in ephemerides. Note also that this concerns the position of the object at the time at which the light was emitted, and not the actual position the body may have reached at the time of the observation. The additional correction for this effect is the correction for light-time (Section 6.3.7).

Let $\rho ^ { \prime }$ , $H ^ { \prime }$ , $\delta ^ { \prime }$ be the spherical topocentric coordinates of the object, and $\rho , H , \delta ^ { \prime }$ , its geocentric coordinates. Since we have already corrected for the deflection of the vertical, $H ^ { \prime }$ and $H$ are reckoned from the same meridian plane. The geocentric coordinates of $P$ with the meridian plane as the ZOX plane are $r , 0 , \phi$ . In these geocentric rectangular coordinates, the components of the three vectors of Equation (9.15) are

$$
\mathbf { P S } \left\{ \begin{array} { c } { \rho ^ { \prime } \cos \delta ^ { \prime } \cos H ^ { \prime } , } \\ { - \rho ^ { \prime } \cos \delta ^ { \prime } \sin H ^ { \prime } , } \\ { \rho ^ { \prime } \sin \delta ^ { \prime } , } \end{array} \right. \qquad \mathbf { O S } \left\{ \begin{array} { c } { \rho \cos \delta \cos H , } \\ { - \rho \cos \delta \sin H , } \\ { \rho \sin \delta , } \end{array} \right. \qquad \mathbf { O P } \left\{ \begin{array} { c } { r \cos \phi , } \\ { 0 , } \\ { r \sin \phi , } \end{array} \right.
$$

where $\delta ^ { \prime }$ and $H ^ { \prime }$ are observed and $\rho$ is taken from the ephemerides. Equation (9.14) becomes

$$
\left\{ \begin{array} { l l } { \rho \cos \delta \cos H = \rho ^ { \prime } \cos \delta ^ { \prime } \cos H ^ { \prime } + r \cos \phi , } \\ { \rho \cos \delta \sin H = \rho ^ { \prime } \cos \delta ^ { \prime } \sin H ^ { \prime } , } \\ { \rho \sin \delta \quad = \rho ^ { \prime } \sin \delta ^ { \prime } + r \sin \phi . } \end{array} \right\}
$$

The solution is straightforward. In a first step, one computes $\rho ^ { \prime }$ which is given,

adding the squares of the three equations, by

$$
\rho ^ { \prime 2 } + 2 \rho ^ { \prime } ( r \cos \varPhi \cos \delta ^ { \prime } \cos H ^ { \prime } + r \sin \varPhi \sin \delta ^ { \prime } ) + r ^ { 2 } - \rho ^ { 2 } = 0
$$

taking the positive solution. Then, replacing $\rho ^ { \prime }$ by the value just computed, one can solve (9.16) for $\delta$ and $H _ { ; }$ , and obtain the geocentric alt-azimuth coordinates as well as the topocentric distance, assuming, of course, that the ephemerides for $\rho$ are correct. One may remark that the $Z$ component does not depend on $H .$ . It is the fixed part of the diurnal parallax, while the $X$ and $Y$ components are functions of time with the rotation of the Earth. This latter part is the diurnal parallax proper.

# 9.8 Time variations

The position of an apparently fixed point on the surface of the Earth is actually not stable. Several crustal motions occur that modify, at a level of a few millimeters to a few decimeters, the geocentric coordinates of the site, and it is necessary, depending upon the accuracy expected, to take them into account. The most important are the Earth tides, but many other smaller effects due to ocean and atmospheric loading, and polar tides are to be considered. Secular effects due to tectonic motions and post glacial rebound are generally taken into account in the ITRF.

# 9.8.1 The tidal potential

Since the Earth has finite dimensions and is not spherical, the gravitational forces exerted by an external body, such as the Moon or the Sun, are different at the center of mass of the Earth than at some other point on the planet, in particular on its surface. Let us consider, in a first approximation, a spherical Earth, centered at $o$ , and the Moon, the center of mass, $M$ , of which produces an attractive acceleration on a point $P$ on the surface of the Earth equal to

$$
\mathbf { f } = G m ^ { \prime } { \frac { \mathbf { P } \mathbf { M } } { P M ^ { 3 } } } ,
$$

where $m ^ { \prime }$ is the mass of the Moon (see Fig. 9.9) and $G$ is the gravitational constant. In the system of reference centered at the center of mass of the Earth, $o$ , the acceleration $A$ is equal to the effect of the gravitational interaction between the Earth and the Moon, assuming that their masses are concentrated at $o$ and $M$

$$
\mathbf { A } = G m ^ { \prime } { \frac { \mathbf { O } \mathbf { M } } { O M ^ { 3 } } } .
$$

Hence, the apparent force, produced by the perturbing action of $M$ on a unit mass

![](images/e6d057138c280220027129fdb98d48ae49addecc14868ffdd45c53c3ab37e578.jpg)  
Fig. 9.9. Attraction of the Moon on $P$ and its components $\Delta g$ and $\Delta f$ .

(which is, evidently, equal to the acceleration) is, in this reference system,

$$
\mathbf { F } = \mathbf { f } - \mathbf { A } = G m ^ { \prime } \left[ { \frac { \mathbf { P M } } { P M ^ { 3 } } } - { \frac { \mathbf { O M } } { O M ^ { 3 } } } \right] .
$$

It is called the tidal force. Now, both forces are conservative and their field can be written in terms of the gradient of a potential, the tidal potential,

$$
W = G m ^ { \prime } \left( \frac { 1 } { P M } - \frac { { \bf O P } \cdot { \bf O M } } { O M ^ { 3 } } \right) .
$$

Let us express $W$ by introducing the geocentric zenith distance $z$ of $M$ (we assume as a first approximation that OP is the vertical of $P$ ). Let us call $O P = a$ , $P M = r ^ { \prime }$ and $O M = r$ Then one has

$$
\frac { 1 } { r ^ { \prime } } = \frac { 1 } { r } \left( 1 - \frac { 2 a } { r } + \frac { a ^ { 2 } } { r ^ { 2 } } \right) ^ { 1 / 2 } ,
$$

or

$$
{ \frac { 1 } { r ^ { \prime } } } = { \frac { 1 } { r } } + { \frac { a } { r ^ { 2 } } } \cos z + { \frac { 1 } { r } } \sum _ { n = 2 } ^ { \infty } \left( { \frac { a ^ { 2 } } { r ^ { 2 } } } \right) P _ { n } ( \cos z ) ,
$$

where the functions $P _ { n }$ are the Legendre polynomials already introduced in Section 9.5.1. The additional term in (9.17) is precisely $- a \cos z / r ^ { 2 }$ , so that the expression of $W$ is:

$$
W = { \frac { G m ^ { \prime } } { r } } \sum _ { n = 2 } ^ { \infty } \left( { \frac { a } { r } } \right) ^ { 2 } P _ { n } ( \cos z ) = \sum _ { n = 2 } ^ { \infty } W _ { n } .
$$

The tidal acceleration can be split into its components along the vertical and along the horizontal plane of $P .$

Along the vertical, this acceleration corresponds to a variation of the local gravity

$$
\Delta \mathbf { g } = - G m ^ { \prime } \frac { \partial W } { \partial a } .
$$

In the vertical plane containing the Moon, the horizontal force is

$$
\Delta \mathbf { f } = - \frac { \partial W } { a \partial z } .
$$

The horizontal acceleration modifies the direction of the vertical; the tides produce an angular deflection $\Delta \mathbf { v }$ of the vertical, in the direction of the vertical plane containing the Moon, and whose value is

$$
\Delta { \bf v } = \frac { - 1 } { g } \frac { \partial W } { a \partial z } .
$$

In practice, in computing $W ,$ one will add the effects due to the Moon and the Sun. Let us note that the variation of the local gravity also modifies the shape of the geoid. The deformation of the geoid due to $W -$ which is time dependent because of the rotation of the Earth – is called the static oceanic, or geoidal, tide. The radial shift at the point $P$ is

$$
\Delta h = { \frac { W } { g } } = { \frac { G m ^ { \prime } } { g r } } \sum _ { n = 2 } ^ { \infty } \left( { \frac { a } { 2 } } \right) ^ { 2 } P _ { n } ( \cos z ) .
$$

It is generally accepted that for the computation of tides, the second and third harmonics of W represent the actual displacements to a few millimeters. The amplitude of $\Delta h$ may be as large as $8 0 \mathrm { c m }$ , while the angular deviation of the vertical around its mean value can reach 25 mas.

Let us now take into account the fundamental feature in the theory of tides, the rotation of the Earth which causes the plane OPM to move around $O P .$ For this, let us express W in the equatorial geocentric coordinates $\alpha , \delta$ of the Moon, $M .$ . The components of OP and OM are, respectively,

$$
\mathbf O \mathbf P \left\{ \begin{array} { l l } { a \cos \phi } \\ { \quad 0 } \\ { a \sin \phi } \end{array} \right. \quad \mathbf O \mathbf M \left\{ \begin{array} { l l } { r \cos \delta \cos H } \\ { r \cos \delta \sin H } \\ { r \sin \delta } \end{array} \right.
$$

from which, one gets,

$$
\cos z = \sin \phi \sin \delta + \cos \phi \cos \delta \cos ( T + \lambda - \alpha ) ,
$$

where $T$ is the Greenwich sidereal time, or the stellar angle, and $\lambda$ is the longitude of $P .$ The second-order term of W includes two terms, $i = 1$ for the Moon and $i = 2$ for the Sun:

$$
W _ { 2 } ^ { i } = \frac { G m ^ { \prime } a ^ { 2 } } { r ^ { 3 } } \left( \frac { 3 \cos ^ { 2 } z - 1 } { 2 } \right) ,
$$

which become, after some calculations,

$$
\begin{array} { l } { { { \displaystyle W _ { 2 } ^ { i } = \frac { G m ^ { \prime } a ^ { 2 } } { r ^ { 3 } } [ ( \frac { 3 } { 2 } \sin ^ { 2 } \varPhi \sin ^ { 2 } \delta + \frac { 3 } { 4 } \cos ^ { 2 } \varPhi \cos ^ { 2 } \delta - \frac { 1 } { 2 } )  } } } \\ { { { \displaystyle \qquad + 3 \sin \varPhi \cos \varPhi \sin \delta \cos \delta \cos ( T + \lambda - \alpha ) \qquad } } } \\ { { { \displaystyle \qquad + \frac { 3 } { 4 } \cos ^ { 2 } \varPhi \cos ^ { 2 } \delta \cos 2 ( T + \lambda - \alpha ) ] } . } } \end{array}
$$

Similarly, ${ W } _ { 3 } ^ { i }$ can be developed in sin $k ( T + \lambda - \alpha )$ with $1 \leq k \leq 3$ .

The quantities $\delta$ and $\lambda$ must be obtained from the theories of the motions of the Moon and of the Earth. For the Moon the various expressions of $\delta$ and $\alpha$ are expressed as functions of four trigonometric time arguments (Brouwer and Clemence, 1961).

(i) $l \colon$ mean anomaly of the Moon, (ii) $g$ : longitude of the lunar perigee, (iii) $h$ : longitude of the node of the Moon’s orbit, (iv) $l ^ { \prime }$ : longitude of the Sun.

For the solar tides, $l ^ { \prime }$ is the only significant argument. After the substitution of these expressions into (9.21), one obtains general, multi-argument, trigonometric series in $T , l , g , h$ , and $l ^ { \prime }$ from which significant terms are identified and kept for computing the tides. These terms can be arranged into several classes.

- Terms including $2 T$ correspond to semi-diurnal tidal waves.   
- Terms including $T$ correspond to diurnal tidal waves. There are also small third diurnal terms in $3 T .$ .   
- Monthly and semi-monthly effects are produced by terms which include no $T$ term, but respectively $l$ and 2l terms.   
- Long periodic terms are essentially semi-annual and annual, arising from terms in $l ^ { \prime }$ and $2 l ^ { \prime }$ .   
- Very long period terms are functions only of $g$ and $h$ , while secular terms give a constant tide, which is included in the shape of the geoid and in the coordinates provided by the ITRF. They are not to be considered in the theory.

# 9.8.2 Solid Earth tides

If the Earth were a perfectly rigid body, the above description would be sufficient. This is not the case and, under the influence of the tidal force field, the Earth is globally deformed. It reacts essentially like an elastic body, so that the deformation is proportional to the amplitude of the forces. The actual response is governed by Love and Shida numbers.

- The Love number $h$ represents the ratio of the height of the Earth tide to the height of the corresponding static geoidal tide at the surface.   
- The Love number $k$ represents the ratio of the additional potential produced by this deformation to the deforming potential.   
- The Shida number $l$ represents the ratio between the horizontal displacement of the crust and that of the corresponding static geoidal tide at the surface.

Before the advent of very accurate astrometry and satellite geodesy, these numbers were considered as unique, and the deflection of the vertical was given by its two components for a point with coordinates $\phi$ and $\lambda$ (Melchior, 1966):

- along the meridian, towards North

$$
v _ { N } = - \frac { l } { g } \frac { \partial W _ { 2 } } { \partial \phi } ,
$$

- along the East–West direction towards West

$$
v _ { W } = \frac { l } { g \cos \phi } \frac { \partial W _ { 2 } } { \partial \lambda } .
$$

Similarly, the vertical component of the tide was limited to

$$
\Delta h = ( 1 + k ) \frac { W _ { 2 } } { g } .
$$

With respect to the instantaneous position of the geoid affected by the geoidal tide, the vertical component was

$$
\Delta h ^ { \prime } = ( 1 + k - h ) \frac { W _ { 2 } } { g } ,
$$

where only the second-order part $W _ { 2 }$ of the development of $W$ was kept. The values adopted for these numbers were (Derr, 1969):

$$
h = 0 . 6 1 5 , \quad k = 0 . 0 8 5 , \quad l = 0 . 3 0 3 .
$$

Now that an accuracy of $1 \mathrm { m m }$ is desired, a much more sophisticated representation is necessary, and there are as many numbers as there are periods in the time series representing the tidal potential. In addition, they depend on station latitude $\phi$ (Wahr, 1981). This dependence is a consequence of the ellipticity, the rotation of the Earth, and the resonance with the nearly diurnal free wobble in the Earth’s rotation. For long periods, the mantle anelasticity is to be taken into account and leads to corrections to the elastic Love, or Shida, numbers.

It is outside the scope of this book to present the details of the computation of the effects of the Earth tides on the displacement of a station. They are described in IERS (2003).

# 9.8.3 Polar tides

In writing the expression (9.8) for the Earth centrifugal potential, it was assumed that the angular velocity $\vec { \Omega }$ was a vector supported by the $O Z$ axis. Because of polar motion (Section 10.4.1), this is not true and the actual potential is

$$
V = { \frac { 1 } { 2 } } ( r ^ { 2 } | \vec { \Omega } | ^ { 2 } - ( r \cdot \vec { \Omega } ) ^ { 2 } ) ,
$$

where the components of $\vec { \Omega }$ are set to be

$$
\vec { \Omega } \left\{ \begin{array} { c } { \omega _ { 0 } m _ { 1 } , } \\ { \omega _ { 0 } m _ { 2 } , } \\ { \omega _ { 0 } ( 1 + m _ { 3 } ) , } \end{array} \right.
$$

where the parameters $m _ { 1 }$ and $m _ { 2 }$ describe polar motion with respect to the mean pole adopted for the ITRF, and $m _ { 3 } - { \bf a }$ negligible quantity – is a variation of the rotation ratio $\omega _ { 0 }$ . The formulation for the displacement of a site is given in Wahr (1985) and, calling $S _ { r }$ the upward radial, $S _ { \phi }$ the meridian southward, and $S _ { \lambda }$ the eastward displacements, and using the mean values (quite sufficient here) of the Love and Shida numbers, one gets in millimeters as functions of $\Delta V$ , the effect on $V$ of $m _ { 1 }$ and $m _ { 2 }$ :

$$
\begin{array} { l } { { S _ { r } = \displaystyle \frac { h } { g } \Delta V = - 6 . 6 \times 1 0 ^ { 6 } ( m _ { 1 } \cos \lambda + m _ { 2 } \sin \lambda ) \sin 2 \varPhi } } \\ { { S _ { \phi } = \displaystyle \frac { l } { g } \frac { \partial \Delta V } { \partial \phi } = - 1 . 9 \times 1 0 ^ { 6 } ( m _ { 1 } \cos \lambda + m _ { 2 } \sin \lambda ) \cos 2 \varPhi } } \\ { { S _ { \lambda } = \displaystyle \frac { 1 } { g \sin \phi } \frac { \partial \Delta V } { \partial \lambda } = 1 . 9 \times 1 0 ^ { 6 } ( m _ { 1 } \sin \lambda - m _ { 2 } \cos \lambda ) \cos 2 \varPhi . } } \end{array}
$$

Despite the apparently large coefficients $m _ { 1 }$ and $m _ { 2 }$ being expressed in radians, the values are smaller than $1 ^ { \prime \prime }$ , the maximum radial displacement is of the order of 25 mm and the maximum horizontal displacement is around $7 ~ \mathrm { m m }$ . There is also a variation of the gravity with a maximum of $1 5 \mu \mathrm { G a l }$ ,

$$
\delta \mathbf { g } = - 3 . 9 \times 1 0 ^ { 6 } ( m _ { 1 } \cos \lambda + m _ { 2 } \sin \lambda ) \sin 2 \phi .
$$

# 9.8.4 Ocean loading

We have not yet described the ocean tides. They are produced by the same tidal potential (Equation (9.19)) as the Earth tides. The effect on a given point of the ocean is, however, much more complicated to compute, because the variety of local limiting conditions, such as the depth and floor topography of the seas, and the shape of the coastlines, induce a very complex response of the oceans to the tidal potential. Models based upon tidal gauges and satellite altimetry observations compute the phase with respect to the lunar, or solar hour angle, and the amplitude of various components of the tidal potential. Since they have different periods, the actual tidal heights are time dependent. Figure 9.10 gives, as an example of the complexity, a map of the amplitudes produced by the $M _ { 2 }$ semi-diurnal wave, the main wave produced by the lunar attraction and having a period of $1 2  { \mathrm { h } } 2 5  { \mathrm { m i n } }$ .

![](images/e9369424addc29b9b720b9593a964b7951259a2724f20fd6a5e5d646c410b2e5.jpg)  
Fig. 9.10. Amplitudes of the $M _ { 2 }$ tidal wave and the phases with an interval of $3 0 ^ { \circ }$ referred to the passage of the Moon through the local meridian. The amplitude is proportional to the levels of grey, and varies from 10 to $1 8 0 \mathrm { c m }$ . (From Le Provost et al., 1994, Spectroscopy of the world ocean tides from a fluid element hydrodynamic model, $J .$ Geophys. Res., 99, 24 777–24 797. Copyright 1994 American Geophysical Union. Reproduced by permission of American Geophysical Union.)

The variations of the height of the water surface with respect to the mean ocean surface produce a direct effect, owing to the gravitational attraction of the raised water, or a negative effect, owing to the lowered surface of the oceans. There is a second effect, a loading effect, because the changing surface exerts a time-variable load on the solid Earth below the ocean bottom, and deforms the elastic Earth all around. In addition, this deformation produces a variation of the gravitational attraction, called the indirect effect of tidal water.

In order to compute the sum of these effects, it is necessary to introduce the sea tide potential, $W _ { \mathrm { w } }$ , produced by the additional or missing water layers with respect to the mean surface of the oceans (that is, in practice, the geoid). In order to compute $W _ { \mathrm { w } }$ , one can integrate the tidal water effect through the whole Earth, or within some limited area, $S$ , of the ocean close to the point, $A$ , of coordinates $\phi _ { A } , \lambda _ { A }$ , for which the deformation is being computed:

$$
W _ { \mathrm { w } } ( \phi _ { \mathrm { A } } , \lambda _ { \mathrm { A } } ) = - G a ^ { 2 } \int \int _ { S } \frac { Z ( \phi , \lambda ) } { \rho ( \phi _ { A } , \lambda _ { A } , \phi , \lambda ) } \frac { \mathrm { d } \phi \mathrm { d } \lambda } { \cos \phi } ,
$$

where $a$ is the radius of the Earth, $Z$ is the height (positive or negative) of the tide at the point $P ( \phi , \lambda )$ , $\rho$ is the distance $P A$ , and where it is assumed that the density of water is unity. This potential may be used, as already done in Section 9.8.2, to compute the effect on the position of A. More details on these computations will be found in Vaniˇcek and Krakiwsky (1982). To facilitate computations, it is possible to develop $W _ { \mathrm { w } }$ in a spherical harmonic series. However, when determining the actual effects on A, one has to know load numbers, similar to Love and Shida numbers, which express the proportionality between the potential and the deformation. They are functions of the local rheological structure of the crust and should be determined for each site from the observed ocean loading effect. Theoretical values were computed by Goad (1980). The amplitudes and phases of the vertical motions are tabulated for each tidal wave in the Explanatory Supplement to the Astronomical Almanac (Seidelmann, 1992). The amplitudes are generally smaller than $1 0 ~ \mathrm { m m }$ , but the effects of all tidal waves must be summed up, taking into account at each instant, the values of phases.

# 9.8.5 Atmospheric loading

The atmosphere exerts a variable load on the Earth’s surface, depending linearly on the pressure. But, because of the Earth’s elasticity, one has to consider the total load over a large surface, typically $2 0 0 0 \mathrm { k m }$ in diameter. The effect can be modeled by different empirical formulae, the simplest being a linear function of the pressure, $p _ { A }$ , on the site, $A$ , and a mean pressure, $\bar { p }$ , in the surrounding region. Second-order polynomial representations have also been proposed. However, one has to rely only on the pressure actually measured at $A$ . So, in practice, a linear function of $p _ { A }$ is used. The slope depends upon the relationship that may exist between the local pressure and the mean pressure $\bar { p }$ as a mean throughout a year or a season as well as on the load numbers. So the atmospheric load effect must be investigated at each site, and this was done in particular for some VLBI and GPS sites, in which observations are continuously performed.

The most accurate results were obtained for 11 VLBI sites (van Dam and Herring, 1994). The slope, expressed in millimeters per hectopascal, is generally of the order of $- 0 . 3$ to $- 0 . 5$ for height variations. Following theoretical calculations by van Dam and Wahr (1987), the peak-to-peak displacement may frequently be of the order of $2 0 { - } 2 5 ~ \mathrm { m m }$ , with accompanying gravity perturbations of $4 . 6 ~ \mu \mathrm { G a l }$ . There are also horizontal motions that are of the order of one third of the vertical displacements.

In conclusion, as in the case of ocean loading, the atmospheric loading effects must be calibrated at each site, whenever observing precisions call for a knowledge of the position of the instrument to better than $2 \mathrm { c m }$ .

![](images/b1270156ac555d63002e8526a4ab443186e4672a5e50ccfe2443ae3b88159abc.jpg)  
Fig. 9.11. Annual geocenter motion from space geodesy results (dashed curve) and a geophysical model including the main loading effects. (Reproduced with permission from Bouill´e et al., 2000, Geophys. J. Int., 143, 71–80.)

# 9.9 Dynamical consequences

The different local effects described in the previous section, when integrated over the Earth, modify the global distribution of matter in our planet and consequently its gravitational field. This surface mass redistribution is secular, owing to plate tectonics, post-glacial rebound, or melting of ice sheets. It also presents shorter, but not necessarily periodic, cycles produced by atmospheric or oceanic mass transfers. These changes in mass distribution produce changes in the Earth’s gravitational potential (9.7). The result is perceptible by space geodesy techniques, insofar as the lowest-degree harmonics are concerned.

![](images/35eb1f802f4ec6ebdd93637818e9f2af08e7bed76646a994fb692d0d54811836.jpg)  
Fig. 9.12. Variations of $J _ { 2 }$ and $J _ { 3 }$ during 10 years from the observations of the satellites Starlette and LAGEOS1. (Adapted from Cheng and Tapley, 1999, Seasonal variations of low degree zonal harmonics of the Earth’s gravity field from satellite laser ranging observations, $J .$ Geophys. Res., 104, 2661–2681. Copyright 1999 American Geophysical Union. Reproduced by permission of American Geophysical Union.)

# 9.9.1 Motion of the geocenter

The appearance of first-order harmonics in the residuals of the determination of an Earth potential model is an indication that the reference system is not centered at the geocenter. The actual coordinates of the center of mass of the Earth are (Heiskanen and Moritz, 1967):

$$
x _ { \mathrm { g } } = a C _ { 1 , 1 } , \quad y _ { \mathrm { g } } = a S _ { 1 , 1 } , \quad z _ { \mathrm { g } } = a J _ { 1 } .
$$

The most important periodic effects are annual variations due to atmospheric and ocean loading and the variations of soil and underground water. The amplitude is of the order of a couple of millimeters and, as Fig. 9.11 shows, the geophysical model represents the measured effect within the uncertainties of the space geodesy determinations.

Actually, the spectrum of time variations of the first-order harmonics is quite complex, sensitive to shorter, and sometimes random, modifications of the atmospheric and hydrologic environments. It is, therefore, not possible to give a clear picture of these variations; it is to be compared with similar features in the motion of the polar motion (Section 10.4.1). It seems however, that annual, and smaller semi-annual motions of the geocenter are now well assessed (Chen et al., 2000).

# 9.9.2 Variations of the Earth potential

Similarly, and for the same reasons, other lower terms of the geopotential undergo periodic variations. Such changes are now detected in the zonal harmonics $J _ { 2 } , J _ { 3 }$ , $J _ { 4 }$ , $J _ { 5 }$ , $J _ { 6 }$ , and $J _ { 8 }$ (Cheng and Tapley, 1999). They are of the order of a few units in $1 0 ^ { - 1 0 }$ . The best-determined variations concern $J _ { 2 }$ and $J _ { 3 }$ as shown in Fig. 9.12.

Secular variations of some zonal harmonics have been detected. They are due to the consequences of the deglaciation of the late Pleistocene glacial cycle, and the resulting post-glacial rebound (Mitrovica and Peltier, 1993), together with the present ice melting (James and Ivins, 1997). The values found for the time derivatives are (Cheng et al., 1997):

$$
\begin{array} { r } { \dot { J } _ { 2 } = ( - 2 . 7 \pm 0 . 4 ) \times 1 0 ^ { - 1 1 } / \mathrm { y e a r } , \quad \dot { J } _ { 3 } = ( 1 . 3 \pm 0 . 5 ) \times 1 0 ^ { - 1 1 } / \mathrm { y e a r } , } \\ { \dot { J } _ { 4 } = ( - 1 . 4 \pm 1 . 0 ) \times 1 0 ^ { - 1 1 } / \mathrm { y e a r } , \quad \dot { J } _ { 5 } = ( 2 . 1 \pm 0 . 6 ) \times 1 0 ^ { - 1 1 } / \mathrm { y e a r } . } \end{array}
$$

# 10

Earth orientation

Without any internal or external forces acting on it, the Earth would rotate at a uniform rate around its center of mass and around an axis inclined by $2 3 ^ { \circ } 2 6 ^ { \prime }$ with respect to the ecliptic pole. The mean rotation period is $2 3 ^ { \mathrm { h } } 5 6 ^ { \mathrm { m } } 4 _ { \cdot } ^ { \mathrm { s } } 1 0$ . In reality, the Earth is composed of non-rigid parts in an oblate spheroidal shape and it is not isolated in space. These conditions produce variations in the rotation speed and in the direction of its axis. They will be described in the next section.

# 10.1 Earth orientation presentation

The orientation of the Earth in space is a complex combination of several types of motions. The axis of rotation moves with respect to the celestial reference frame. This is the precession–nutation already studied in Chapter 8. But this axis also moves with respect to the Earth’s crust as represented by the ITRF. This is the polar motion. Finally, the Earth rotates at a variable rate about this axis. In this chapter, we study the last two effects, but in association with precession–nutation for a global description of the Earth orientation.

# 10.1.1 General description and history

The diurnal rotation axis is perpendicular to the equatorial plane, but the equatorial plane moves as described in Sections 8.5–8.7. It is not regular, and the variations in the rotation of the Earth were detected in the 1800s from the observed motion of the Moon, but they were not confirmed until correlations in the variations of the motions of the Moon and Mercury were established. De Sitter (1927), Stoyko (1937), and Spencer Jones (1939) discovered the secular deceleration and seasonal variations of the Earth’s rotation rate. The variations in the Earth’s rotation rate are now known to be of three types: secular, irregular, and periodic. The secular variation of the rotational speed is the approximately linear increase in the length-of-day (LOD), primarily because of tidal friction. This effect causes a slowing of the Earth’s rotational speed with a lengthening of the day by about 0.0005–0.0035 s per century. The irregular changes appear to be random, but may be correlated with physical processes within the Earth. These changes cause variations in the LOD by as much as 0.01 s over the past 200 years and consist of the so-called decade fluctuations with periods of 5–10 years and short interval variations. The higherfrequency variations are related to the changes in the total angular momentum of the atmosphere, oceans, ice caps, and interior of the Earth. Periodic variations are the result of repeatable physical processes, such as tides in the solid Earth due to the Sun and Moon. These produce variations in the LOD as large as 0.0005 s with periods of 1 year, $1 / 2$ year, 27.55 days, 13.66 days, etc. Also, season changes in the global weather patterns will cause similar amplitude changes with annual and semi-annual periods. Finally, very-short-period (in particular diurnal and sub-daily) variations in the speed of rotation of the solid Earth are produced by an exchange of angular momentum between the atmosphere and the crust.

In addition to the variable Earth rotation, there is also polar motion. This is the motion of the Earth’s axis of rotation with respect to the surface of the Earth. In 1765, Euler predicted that, if the axis of rotation is not coincident with the principal axis of inertia, the rotation axis would have a motion with respect to the Earth-fixed reference frame. In 1891, Chandler discovered the motion of geographical latitudes of astronomical observatories from observational data. However, the period is 433 days, while Euler predicted 305 days owing to the Earth’s ellipticity. The difference is the result of the non-rigidity of the Earth. A second motion follows an approximately elliptical path with an annual period and is caused by the redistribution of the atmospheric and ice masses during the year. There also exist short period components sensitive to the global meteorological situation, and, in particular, to jet streams and high-altitude winds.

Polar motion is distinct from precession and nutation, which are motions of the axis of rotation with respect to the stars, or the International Celestial Reference Frame (ICRF), and can almost entirely be developed theoretically (see Section 8.7). This is not the case for the rotation of the Earth and polar motion, which must be determined from observations. From the 1890s until 1988, a regular program of optical observations, using zenith tubes and astrolabes, was conducted by the International Polar Motion Service (IPMS) and the Bureau International de l’Heure (BIH) to determine polar motion and the Earth’s rotation. In the 1980s an IAU Working Group investigated methods of achieving greater accuracy by means of Very Long Baseline Interferometry (VLBI), lunar laser ranging, and other techniques. This led to the regular use of VLBI, and the progressive suppression of optical observations for Earth orientation parameter determination. Now, the use of Global Positioning System (GPS) measurements has made available almost continuous determinations of Earth Orientation Parameters (EOP). Thus, short-term (sub-daily) variations of both Earth rotation and polar motion can now be investigated. Since the GPS is a system around the Earth with orbits determined from Earth observations, it is not tied to an independent reference frame, and VLBI observations are still necessary.

This extension of techniques, and the necessity to merge the different results into a single solution, led to the establishment in 1988 of the International Earth Rotation Service (IERS) with broad responsibility for Earth orientation parameters. The IERS is organized into a central bureau, now in Germany, and various functional centers. Technical Notes are published as needed, including periodic editions of the IERS Conventions, which specify constants, reference frames, and methods to be used for Earth orientation. More information is available at http://www.iers.org.

# 10.1.2 Dynamical causes

The dynamical causes of Earth orientation changes can be classified as astronomical and geophysical. Most of them are common with those causing the precession and nutation (Section 8.5), but some are specific to the Earth’s rotation and polar motion. The astronomical causes are tidal torques due to gravitational attractions of celestial bodies on the Earth. The geophysical causes are mass displacements in the Earth’s layers (solid core, fluid core, mantle, oceans, and atmosphere), mechanical (gravitation, pressure, and viscosity), and electro-magnetic interactions between the Earth’s layers.

It has been established that conservation of angular momentum is preserved, but it is the angular momentum of the complete Earth–Moon system. In the Earth’s case the angular momentum is divided between the Earth’s crust, the atmosphere, the oceans, the mantle, and the fluid and solid cores. So the observed variations of the Earth’s surface are caused by redistributions of the angular momentum with the other components (see Section 9.8). The correlations have been well established, but to date the variations are not predictable to meaningful levels of accuracy. There are also observed seasonal short- and long-term variations.

The Moon raises tides (Section 9.8.1) in the ocean, and tidal friction carries the maximum tide ahead of the line joining the center of the Earth and Moon. The resulting couple diminishes the speed of rotation of the Earth and this reacts on the Moon to increase its angular momentum. The sum of the angular momentum on the Earth and the orbital momentum of the Moon remains constant to the extent that one neglects the very small contribution due to solar torques. This produces an increase in the size of the orbit of the Moon, and a reduction of the angular speed of the Earth. Let us note at this point that tidal friction is distinct from changes in the moments of inertia caused by tides.

# 10.1.3 Geophysical causes

Geophysical effects introduce complications into the astronomical forcing motions of Earth orientation. Gravitational and centrifugal forcing cause deformations and moment of inertia changes. These are responsible for modifications of nutation amplitudes and variations of the Earth’s rotation, at periods the same as nutations and with amplitudes up to $1 \mathrm { m s }$ . These effects are scaled by the elasticity factors of the mantle, the Love and Shida numbers (Section 9.8.2). The elastic deformations of centrifugal origin cause the modification of the period from Euler’s theoretical to Chandler’s observed value.

The fluid core has a clockwise, nearly diurnal wobble with respect to the crust, because the inertia axes do not coincide. The effect on the mantle is a motion independent of rotation, called free core nutation, with a period dependent on the flattening of the core–mantle boundary. In a celestial frame, the free nutation would appear as a clockwise oscillation. The present model of precession–nutation (IAU 2000 precession–nutation model, see Section 8.6), takes into account the rigid solution and non-rigid effects, but not the free core nutation which has to be derived from the observations. The underlying theories agree with observations at the sub-milliarcsecond level.

The displacement of masses inside the Earth’s superficial layer, triggered by thermal, tidal, and electro-magnetic influences, have long-period effects on the Earth’s rotation. Variations in the centrifugal forces due to wobble of the rotation axis cause a change in water height in the oceans, called “pole tide”. This changes the period of the Chandler wobble.

Decade-long fluctuations of the length-of-day (LOD) might be caused by the superficial layers, such as the El Ni˜no cycle, in the atmosphere and ocean, and coupling between the core and mantle. The secular change in the LOD is attributed to tidal friction, which transfers the Earth’s angular momentum to the lunar orbit.

An observed secular motion of the pole with respect to the crust of about 0.3 per century toward $8 0 ^ { \circ }$ West is attributed to the slow viscous mass redistribution (post-glacial rebound) associated with the ice cap melting after the termination of the Pleistocene glaciation 20 000 to 15 000 years ago.

While qualitative, if not quantitative, explanations exist for the variations in the Earth’s orientation due to geophysical effects, there remains an unexplained aspect to the Chandler motion of the pole. The theory is that, in the absence of any external torque, the rotation axis turns around the axis of figure in the terrestrial frame. However, the Earth is not a perfect elastic body, so this motion should be dissipated in thermal energy. No damping of the Chandler motion has been observed. Thus, there must be one or several excitation mechanisms, which have not been identified.

Earth’s rotation plays an important role in physical theories. While an extragalactic reference frame is very close to being inertial (see Chapter 7), the rotating crust is non-inertial. Non-inertial frames, undergoing acceleration with respect to the inertial frame, are subject to centrifugal and Coriolis effects. The consequence is that the Earth has an equatorial bulge and lower gravity at the equator than at the poles. Historically, this has been confirmed by geodetic measurements and latitude dependent pendulum recordings in the eighteenth century. Also, the Foucault pendulum, designed in 1851, exhibits the rotation of the oscillation plane from the Coriolis effect due to the Earth’s rotation.

There are many reciprocal influences between the Earth’s rotation and the behavior of various components of the Earth, in particular the atmosphere and the oceans. For a complete description of geophysical causes and consequences of the Earth’s rotation, see Lambeck (1980).

# 10.2 Observation of the Earth’s rotation

The methods and accuracy of observations of Earth rotation, polar motion, precession, and nutation have changed. With the availability of VLBI observations, the Earth orientation parameters and precession–nutation can now be determined much more accurately. The optical observations were limited to accuracies of about 200 mas and reference frame accuracies of about 30 mas. VLBI observations are close to milliarcsecond accuracies and the frame can be determined to $0 . 0 2 0 \mathrm { { m a s } }$ . Thus, the accuracies of precession–nutation and Earth orientation parameters have improved accordingly. The present daily EOP determinations are of the order of $0 . 2 \mathrm { m a s }$ , or $1 \mathrm { c m }$ , accuracy. In addition, the observations can be related directly to a pseudo-inertial reference frame. The observational techniques are summarized in the following sections.

# 10.2.1 Classical techniques

The variations in the rotation of the Earth and the position of the pole have been monitored since the latter part of the nineteenth century. Observations by photographic and visual zenith tubes, astrolabes, lunar occultations, eclipses, and transits of stars and Solar System observations have been used. Many studies over the years have been complicated by their dependence on the position and motion of the Moon and whether there has been a change in the acceleration of the Moon’s mean motion and any change in the rate of Ephemeris Time based on the Moon’s motion. These astronomical observations indicate that the Moon’s mean motion is constant. Results of these studies are given by Stephenson and Morrison (1984), McCarthy and Babcock (1986), and Stephenson and Lieske (1988). A review of optical observations for solutions of Earth orientation parameters was done by Vondrak and Ron (2000). But recently, using lunar laser ranging data, Chapront et al. (2002) have detected the tidal acceleration of the lunar longitude and found it equal to $r = - 2 5 . 8 5 8 \pm 0 . 7 0 0 3$ per century squared. Historical summaries of length of day and polar motion determinations are given in the Explanatory Supplement (Seidelmann, 1992).

# 10.2.2 Very Long Baseline Interferometry (VLBI)

The availability of VLBI observations (see Section 2.4.2) provides much more accurate observations that are tied to an extragalactic reference frame, which has no apparent motion. Thus, this source of observations became the preferred method for determination of Earth orientation parameters. VLBI has disadvantages in that there is a time lag due to the transportation of the observational tapes from the observation site to a correlator and the correlation time. Thus, there is a delay in the availability and currency of the observations. In addition, VLBI is an expensive observational technique.

# 10.2.3 Laser ranging

The installation of corner cube reflectors on the Moon and on artificial satellites provided targets for laser ranging from sites on Earth (see Section 2.4.3 and Kovalevsky, 2002). Although lunar laser ranging measurements are few in number, they have the advantage of being available immediately without the delay required to correlate the VLBI observations. Satellite ranging observations can be used to determine the motions of satellites, motions of the observing sites, and Earth orientation parameters. The observations are complicated by the multitude of parameters that are required in the solution, but can provide very accurate distance measurements between the observatory and the reflector. The quantity of such observations has never been sufficient to allow the technique to be a primary source for Earth orientation parameters, but the observations can be very timely.

# 10.2.4 Global Positioning System (GPS)

The availability of the Global Positioning System (GPS) for navigation and timing provided a powerful geological observational tool (see Section 2.4.1). Observations can be made continuously from many sites for very little cost. The observations from well-determined sites are combined for determinations of geodetic datums and plate motions. They have the disadvantage that they are not independent of the Earth, since, as with satellite ranging, the observations link the surface of the Earth to satellites in motion around the Earth. For Earth rotation they have the further complication that a part of the variable Earth rotation that is being sought is coplanar with a variable solar radiation pressure that is affecting the motions of the satellites. However, a method has been developed using models for the motion of the nodes of the orbits (Kammeyer, 2000). Therefore, from GPS observations variations in rotation and polar motion over short time periods of minutes can be measured and are precise to $\pm 2 0 \mu \mathrm { s } / \mathrm { d a y }$ . This has provided a powerful new tool in the investigations of very-short-period components of polar motion, nutation, and Earth rotation. However, GPS observations are tied to a reference frame that is not inertial, so VLBI observations are still necessary with respect to the ICRF. Details concerning GPS observations can be found in Kovalevsky (2002) and Hofmann-Wallenhof et al. (1992).

# 10.3 Celestial and terrestrial moving frames

To describe the rotation of the Earth, one needs to specify the rotation axis and the rotation angle of a reference system linked to the solid Earth with respect to some celestial reference. However, a direct link between the terrestrial reference frame (now the ITRF) and the celestial reference frame (now the ICRF) that would be described by a single transformation matrix, $\mathcal { M }$ , would involve too many parameters and a variety of different physical causes, only some of which can be modeled. So, an intermediate moving reference frame is introduced and the transformation is made in two steps.

First, the correction for polar motion and the Earth’s rotation proper, described by a matrix $\mathcal { R } ^ { \star }$ transforms ITRS into the Intermediate Reference System as defined in Section 8.4. Then, a precession–nutation matrix $\mathcal { P } N$ (Section 8.7) transforms the intermediate system into the celestial reference system. One has,

$$
\mathcal { M } = \mathcal { P } N \times \mathcal { R } ^ { \star } .
$$

Traditionally the equinox, the intersection of the ecliptic and moving mean equatorial plane, has been used as the fiducial point for measurements along both the equator and the ecliptic. With the transition from the dynamical system to the kinematic system a new fiducial point was desired. A number of possibilities were considered as origins on the moving equator. These included the intersections of the fixed ecliptic, with the zero-line meridian of the International Celestial Reference System (ICRS), and with the instantaneous prime meridian, the node on the celestial reference great circle, and the so-called non-rotating origin (Kovalevsky and McCarthy, 1998).

It is desirable, in defining the origin for the Earth’s rotation on the moving equator, to eliminate the spurious rotation due to the motion of the equator with respect to the ICRS due to precession and nutation. In considering each of the various geometrical definitions, the instantaneous motion of the considered origin becomes added to the Earth’s angular rotation. This led to the choice of an origin defined by the kinematical property of having no instantaneous rotation about the Geocentric Celestial Reference System (GCRS) axis of rotation. This means that the instantaneous movement of the CEO is always at right angles to the instantaneous equator.

This is the so-called non-rotating origin introduced by Guinot (1979). It is designated as the Celestial Ephemeris Origin (CEO) with respect to the GCRS. Similarly, it was necessary to define a Terrestrial Ephemeris Origin (TEO), which designates the terrestrial non-rotating origin in the International Terrestrial Reference System (ITRS) (Seidelmann and Kovalevsky, 2002).

In this approach to the description of the rotation of the Earth in the ICRS, one also has to define the Intermediate Reference Frame. Its pole, the Celestial Intermediate Pole (CIP), is no longer defined by a physical property or a model, but it is just a conventional intermediate pole for the transformation between the geocentric ICRS (GCRS) and the ITRS. The CIP separates the motion of the ITRS pole into a celestial part including the long-period precession–nutation motion with periods greater than two days in the GCRS, and the terrestrial part including the long-period, daily and sub-daily components of the polar motion. This terrestrial part contains also the variations corresponding to the prograde diurnal and semidiurnal nutations as well as the daily and sub-daily tidal variations in polar motion. The motion of the CIP in the GCRS is determined from the IAU 2000A model for precession and forced nutation for periods greater than two days, plus the celestial pole offsets as estimated from observations. The motion of the CIP in the ITRS is determined from Earth orientation observations and takes into account the modeled high-frequency variations in both the GCRS and ITRS.

# 10.3.1 Celestial Ephemeris Origin

For the concept of the Celestial Ephemeris Origin (CEO), consider a rigid body represented by a celestial sphere, with fixed ICRS reference Cartesian axes $O X Y Z$ and $\scriptstyle \sum _ { 0 }$ , the origin of the equator of the ICRS (intersection of $O X$ with the celestial sphere), as in Fig. 10.1. Let $P$ represent the pole of the intermediate system at time $t$ , defining the Cartesian coordinates $O \xi \eta \zeta$ , such that $O \xi$ is along $O P$ and $\sigma$ is the point on the equator of $P$ where $O \xi$ pierces the sphere. The condition is imposed that for any infinitesimal displacement of $P$ there is no rotation around $O \xi$ . Then $\sigma$ would be the non-rotating origin, that is the CEO on the moving equator of $P$ .

Let, similarly, $P _ { 0 }$ be the pole of the intermediate system at time $t _ { 0 }$ and the corresponding $\mathrm { C E O } \left( \sigma _ { 0 } \right)$ . The motion of point $P$ between dates $t _ { 0 }$ and $t$ is determined by evaluating the quantity $s$

$$
s = [ \sigma N ] - [ \Sigma _ { 0 } N ] - ( [ \sigma _ { 0 } N _ { 0 } ] - [ \Sigma _ { 0 } N _ { 0 } ] ) ,
$$

where quantities in brackets are arcs measured on oriented great circles shown in Fig. 10.1; $N _ { 0 }$ and $N$ are the ascending nodes of the equators at $t _ { 0 }$ and $t$ on the equator of the ICRS. Then $s$ is given by

$$
s = - \int _ { t _ { 0 } } ^ { t } \frac { X \dot { Y } - Y \dot { X } } { 1 + Z } \mathrm { d } t - ( [ \sigma _ { 0 } N _ { 0 } ] - [ \Sigma _ { 0 } N _ { 0 } ] ) ,
$$

![](images/db3011a0d924ca0a7ff42f268bbd1ddcb20f8d630ccc75dd6c7b039fab515acf.jpg)  
Fig. 10.1. Definition of the non-rotating origin $( \sigma )$ ) on ICRF with motion of the pole $P$ from $t _ { 0 }$ to $t$ .

where the dot denotes the time derivative. In polar coordinates, if $D$ is the angle (OZ, OP) and $E$ is the angle of the plane OZP with respect to the principal plane OXZ, the equation is

$$
s = \int _ { t _ { 0 } } ^ { t } ( \cos D - 1 ) \dot { E } \mathrm { d } t - ( [ \sigma _ { 0 } N _ { 0 } ] - [ \Sigma _ { 0 } N _ { 0 } ] ) .
$$

The convention is adopted that $t _ { 0 }$ corresponds to the epoch when the true (or intermediate) equator coincided with the equator of the ITRF (J2000.0). Then, $[ \sigma _ { 0 } N _ { 0 } ] = [ \Sigma _ { 0 } N _ { 0 } ]$ and is the constant $s ( t _ { 0 } )$ in the integral. Then,

$$
s = \int _ { t _ { 0 } } ^ { t } ( \cos D - 1 ) \dot { E } \mathrm { d } t .
$$

For the period 1975–2025, the development of $s ( t )$ including all terms exceeding $0 . 5 \mu \mathrm { a s }$ is, in $\mu \mathrm { a s }$ (Capitaine et al., 2002):

$$
\begin{array} { l } { { \displaystyle s ( t ) = - \frac { X Y } { 2 } + 2 0 0 4 + 3 8 1 2 t - 1 2 1 t ^ { 2 } - 7 2 5 7 4 t ^ { 3 } } } \\ { { \displaystyle ~ + \sum _ { k } C _ { k } \sin \alpha _ { k } + 2 t \sin \varOmega + 4 t \sin 2 \varOmega } } \\ { { \displaystyle ~ + 7 4 4 t ^ { 2 } \sin \varOmega + 5 7 t ^ { 2 } \sin 2 L } } \\ { { \displaystyle ~ + 1 0 t ^ { 2 } \sin 2 L ^ { \prime } - 9 t ^ { 2 } \sin 2 \varOmega , } } \end{array}
$$

where $t$ is expressed in centuries since J2000.0 $( t _ { 0 } = 0$ ) and where $\alpha _ { k }$ and $C _ { k }$ are given in Table 10.1. To extend the development for the periods 1900–1975 and

Table 10.1. Additional terms in $s ( t )$ and $\Delta s ( t )$ for Equations (10.5) and (10.6) in $\mu a s$ units (Capitaine et al., 2002)   

<table><tr><td>αk</td><td>Ck</td><td>di</td><td>Di</td></tr><tr><td>Ω</td><td>-2641</td><td>l&#x27;</td><td>-6</td></tr><tr><td>2</td><td>-63</td><td>l&#x27;+2L</td><td>+2</td></tr><tr><td>Ω+2L</td><td>-12</td><td>l</td><td>-3</td></tr><tr><td>$Ω-2L</td><td>+11</td><td>2L&#x27;+Ω</td><td>+2</td></tr><tr><td>2L</td><td>+5</td><td>l+2L&#x27;</td><td>+1</td></tr><tr><td>$+2L&#x27;</td><td>-2</td><td></td><td></td></tr><tr><td>$-2L&#x27;</td><td>+2</td><td></td><td></td></tr><tr><td>3</td><td>+2</td><td></td><td></td></tr><tr><td>l&#x27;+Ω</td><td>+1</td><td></td><td></td></tr><tr><td>l&#x27;-</td><td>+1</td><td></td><td></td></tr></table>

2025–2100 for terms exceeding $0 . 5 \mu \mathrm { a s }$ , add in $\mu \mathrm { a s }$ :

$$
\Delta s ( t ) = + 2 8 t ^ { 4 } + 1 5 t ^ { 5 } - 2 2 t ^ { 3 } \cos \varOmega - t ^ { 3 } \cos 2 L + \sum _ { i } D _ { i } t ^ { 2 } \sin \alpha _ { i } ,
$$

where $\alpha _ { i }$ and $D _ { i }$ are given in Table 10.1. In this table and in Equations (10.5) and (10.6), the notations, referred to the ICRF axes and the corresponding fixed ecliptic are:

$\varOmega$ : mean longitude of the node of the lunar orbit,   
$L$ : mean longitude of the Sun,   
$L ^ { \prime }$ : mean longitude of the Moon,   
l: mean anomaly of the Sun $( l = L - \varpi )$ ) where $\varpi$ is the mean longitude of the Sun’s perigee,   
$l ^ { \prime }$ : mean anomaly of the Moon $( l ^ { \prime } = L ^ { \prime } - \varpi ^ { \prime } )$ , $\varpi ^ { \prime }$ being the mean longitude of the Moon’s perigee.

At present, the uncertainty of these expressions is smaller than $1 \ \mu \mathrm { a s }$ and is insensitive to expected modifications of the nutation–precession theory to about this level. A maximum error of $3 ~ \mu \mathrm { a s }$ could be reached in 2100 (Capitaine et al., 2000).

# 10.3.2 Terrestrial Ephemeris Origin

For Earth orientation, the concept of the non-rotating origin must be applied to both the CRS and the TRS. The definitions are quite similar.

![](images/24730b51d846ac1b754cf620200a54b5b8041837ca4c6ebcb41856ce554a38dd.jpg)  
Fig. 10.2. Definition of the non-rotating origin (NRO) on ITRF with motion of the pole $P ^ { \prime }$ from $t _ { 0 }$ to $t$ .

Let us call $M$ the ascending node of the instantaneous equator corresponding to the terrestrial pole $P ^ { \prime }$ on the ITRF equator (Fig. 10.2). The non-rotating origin $\varpi$ on the instantaneous equator is derived from the origin $\varPi _ { 0 }$ of the terrestrial longitudes by the evaluation of $s ^ { \prime }$ , with similar conventions as for $s$ concerning the subscript 0 corresponding to $t = 0$ , one has:

$$
s ^ { \prime } = [ \varpi M ] - [ \Pi _ { 0 } M ] - \left( [ \varpi _ { 0 } M _ { 0 } ] - [ \Pi _ { 0 } M _ { 0 } ] \right) .
$$

If $u ( t )$ and $v ( t )$ are the geocentric angles of the components $x$ and $y$ of the position of $P ^ { \prime }$ in the ITRS, then,

$$
s ^ { \prime } = - \int _ { t _ { 0 } } ^ { t } \frac { u \dot { v } - v \dot { u } } { 2 } \mathrm { d } t - ( [ \varpi _ { 0 } M _ { 0 } ] - [ \Pi _ { 0 } M _ { 0 } ] ) .
$$

Here, because of the very small magnitude of the polar displacements, the third component of $\mathbf { O P } ^ { \prime }$ may be taken as equal to 1 to better than $1 \ \mu \mathrm { a s }$ in several centuries (Capitaine et al., 2000). Now, adopting the convention that $\varpi _ { 0 }$ is on the ITRF equator at $t = 0$ , the second part of the equation is cancelled by the constant part $s _ { 0 } ^ { \prime }$ of the integral. Then, if $F$ and $g$ are the polar coordinates of $P ^ { \prime }$ , one obtains the final expression analogous to (10.4):

$$
s ^ { \prime } = \int _ { t _ { 0 } } ^ { t } ( \cos g - 1 ) \dot { F } \mathrm { d } t .
$$

This is a very small correction that must however be taken into account when microarcsecond accuracies are sought. The quantities $F$ and $g$ are provided by the IERS.

# 10.4 Description of the Earth’s orientation

The matrix $\mathcal { R } ^ { \star }$ entering in (10.1) includes two components. One is the polar motion, which represents the displacement of the axis of rotation with respect to the surface of the Earth realized by the ITRF (Section 10.4.1). Let us call the corresponding rotation matrix, $\mathcal { W }$ . The other component describes, using the matrix, $\mathcal { R }$ , the Earth’s rotation with respect to some celestial meridian (or a fiducial point on the equator). This rotation is described by the sidereal time (Section 10.4.3) in the old equinox– equator system and by the stellar angle (Section 10.4.4) in the new system. So, one has,

$$
\mathcal { R } ^ { \star } = \mathcal { R } ( t ) \times \mathcal { W } ( t ) .
$$

# 10.4.1 Polar motion

In the past, the terms nutation and polar motion were defined as the forced and free motions of the reference pole. However, these separations were not completely clear. The forced solution accounts for the external forces, i.e. gravitational forces due to the Sun, Moon, and planets. The free solution is the solution of the differential equations that results from setting the external forces to zero. For a rigid Earth this results in the Eulerian free motion, which is a component of polar motion with annual periods in the terrestrial frame. For a non-rigid Earth the period is lengthened to about 14 months, and is called the Chandler component of polar motion. Thus, the forced, annual, polar motion due to climate and motions resulting from geophysical strains and meteorological effects might logically be included in nutation, but are included in polar motion, because these effects cannot be calculated as accurately as the external forcing effects. In addition, with the Global Positioning System (GPS) observations being made on an almost continuous basis, short period effects are detectable. Now, with the definition of the intermediate reference frame, an arbitrary separation has been introduced that anything with a period shorter than two days is considered as polar motion.

For an Earth with a fluid core there exists a second free solution, the nearly diurnal free polar motion, also called the nearly diurnal, free wobble, or free core nutation. This is not in the nutation series and the observed values are provided by the IERS.

The pole and zero meridian of the International Terrestrial Reference Frame (ITRF, see Section 9.3) are defined implicitly by the ITRF coordinates for instruments used to determine the Earth orientation parameters. Polar motion is specified in terms of two small angles, $x$ and $y$ , which correspond to the coordinates of the Celestial Intermediate Pole (CIP) with respect to the ITRF pole, and are measured along the meridians at longitudes $0 ^ { \circ }$ and $2 7 0 ^ { \circ }$ $9 0 ^ { \circ }$ west). If we take also into account the shift $s ^ { \prime }$ from the zero meridian to the Terrestrial Ephemeris Origin (10.9),

then the polar motion matrix is

$$
\begin{array} { r } { \mathcal { W } ( t ) = \mathcal { R } _ { 3 } ( - s ^ { \prime } ) \times \mathcal { R } _ { 1 } ( - y ) \times \mathcal { R } _ { 2 } ( x ) . } \end{array}
$$

The values for polar motion are given by the IERS and are available at its web site.

# 10.4.2 Rotation of the Earth around the CIP axis

The Earth rotates about its axis and at the same time moves in its orbit around the Sun. Thus, while the Earth rotates with respect to an inertial frame, or the ICRF, it moves in its orbit so that additional rotation with respect to the Sun must be included. As said in the introduction of this section, there are two methods to express the angle of rotation with respect to some celestial meridian taken as origin. Both provide the parameter for the time-dependent matrix $\mathcal { R } ( t )$ as a function of time.

(i) The celestial reference fiducial point is the true equinox, $\gamma$ , on the instantaneous equator. The parameter is the sidereal time (Section 10.4.3).   
(ii) The celestial fiducial point is the Celestial Ephemeris Origin (CEO). The corresponding parameter is the stellar angle (Section 10.4.4).

# 10.4.3 Sidereal time

Historically, sidereal time was the hour angle of the catalog equinox, and was subject to the motion of the equinox due to precession and nutation (see Section 8.5).

The local hour angle of the equinox is the local sidereal time $( \tau _ { \mathrm { L } } )$ and increases by $3 6 0 ^ { \circ }$ or $^ { 2 4 \mathrm { ~ h ~ } }$ in a sidereal day. It is to be remarked that, strictly speaking, the sidereal time is an angle, not a time. The local hour angle of an object $( H _ { \mathrm { L } } )$ equals the local sidereal time minus the right ascension, $\alpha$ , of the object.

$$
\begin{array} { r } { H _ { \mathrm { L } } = \tau _ { \mathrm { L } } - \alpha . } \end{array}
$$

The local sidereal time is equal to the right ascension of the local meridian, and is determined by the techniques described in Section 10.2. Local sidereal time $( \tau _ { \mathrm { L } } )$ i s calculated from sidereal time on the International Meridian $\scriptstyle \tau = \mathrm { G S T } =$ Greenwich sidereal time), when the geographic longitude $\lambda$ (eastward) is known; thus

$$
\tau _ { \mathrm { L } } = \tau + \lambda .
$$

One must distinguish the sidereal time proper, which contains periodic as well as secular terms of the precession–nutation, from a mean sidereal time, which is an expression in which only secular terms are present. Finally, the matrix $\mathcal { R } ( t )$ representing the rotation as measured from the equinox $\gamma$ at a time $t$ is

$$
\begin{array} { r } { \mathcal { R } ( t ) = \mathcal { R } _ { 3 } ( - \tau ) . } \end{array}
$$

![](images/f8b006174ef92adf982771dc1c91c704323eb96dbfcbe2be389c2a425a2fbf83.jpg)  
Fig. 10.3. Definition of the stellar angle.

# 10.4.4 Stellar angle

In the CEO based system the equivalent of sidereal time is the hour angle of the Celestial Ephemeris Origin (CEO), and hence is subject only to the motions of that origin. It is called the stellar angle or Earth rotation angle, and is noted $\theta$ . The stellar angle in Fig. 10.3 is defined by the angle measured along the equator of the Celestial Intermediate Pole (CIP) between the Terrestrial Ephemeris Origin (TEO) and the CEO, positively in the retrograde direction. The main property of the CEO, being a non-rotating origin, ensures that the derivative $\dot { \theta }$ is strictly equal to the instantaneous angular velocity $\omega$ of the Earth around the CIP. Thus, $\theta$ represents rigorously the sidereal rotation of the Earth around its axis, and the matrix $\mathcal { R } ( t )$ a t a time $t$ is given by

$$
\begin{array} { r } { \mathcal { R } ( t ) = \mathcal { R } _ { 3 } ( - \theta ) . } \end{array}
$$

The numerical relation between $t$ and $\theta$ is given by Equation (10.20) in the next section.

There is also a relation that links the Greenwich sidereal time $\tau$ and the stellar angle $\theta$ . Capitaine and Gontier (1993) gave an analytical expression as a function of the nutation referred to the ecliptic of epoch and of precession. Inserting numerical values given by the IAU 2000 precession–nutation theory, one obtains (Capitaine et al., 2002),

$$
\begin{array} { l } { { \tau = \theta + 4 6 1 2 ^ { \prime \prime } 1 5 7 4 8 2 t + 1 ^ { \prime \prime } 3 9 6 6 7 8 4 1 t ^ { 2 } - 0 \% 0 0 0 9 3 4 4 t ^ { 3 } } } \\ { { \nonumber } } \\ { { \displaystyle ~ + 0 { : } 0 0 0 0 1 8 8 t ^ { 4 } + \Delta \psi \cos \epsilon _ { A } - \sum C _ { k } \sin \alpha _ { k } - 0 { : } 0 0 2 0 1 2 , } } \end{array}
$$

where the quantities $C _ { k }$ and $\alpha _ { k }$ are given by Table 10.1, $\Delta \psi$ is the nutation in longitude referred to the mean equator and equinox of date provided by the IAU 2000 nutation–precession series, and the obliquity of the ecliptic $\epsilon _ { A }$ is given by

$$
\epsilon _ { A } = 8 4 3 8 1 ^ { \prime \prime } 4 4 8 - 4 4 ^ { \prime \prime } 8 1 5 0 T - 0 \sp { \prime } 0 0 0 5 9 T \sp { 2 } + 0 \sp { \prime } 0 0 1 8 1 3 T \sp { 3 } ,
$$

where $T$ is in Julian centuries since 2000 January $1 , 1 2 \mathrm { U T } 1$ .

# 10.5 Universal Time

The rotation of the Earth with respect to the Sun is called Universal Time. Thus, the natural unit is the day. The definition of the day has naturally been based on the rotation of the Earth with respect to the Sun. Owing to the orbital motion of the Earth around the Sun in about 365 days, the Earth must rotate about four minutes longer to be in the same angular position with respect to the Sun than to be in the same angular position with respect to the stars. Actually, there is a relation between Universal Time and either the sidereal time or the stellar angle.

# 10.5.1 Solar time

The time defined in terms of the Sun is the solar time. The local apparent solar time (LAT) is related to the local hour angle of the Sun, $H _ { \odot }$ but is, by definition, 12 hours larger. Now, using (10.12), one gets

$$
\mathrm { L A T } = \mathrm { L S T } - \alpha _ { \odot } - 1 2 \mathrm { h o u r s } ,
$$

where LST is the local sidereal time and $\alpha _ { \odot }$ is the right ascension of the Sun.

Owing to the eccentricity of the Earth’s orbit about the Sun and its inclination with respect to the equator, the right ascension of the Sun does not vary uniformly with time. To define a more uniform time scale, the concept has been introduced of a point $U$ , called mean Sun, that moves along the celestial equator at a uniform rate and whose right ascension is $\alpha _ { U }$ . This is the Universal Time (UT), defined in terms of Greenwich sidereal time $( \tau )$ by an expression of the form

$$
\mathrm { U T } = \tau - \alpha _ { \mathrm { U } } - 1 2 \mathrm { h o u r s } ,
$$

where the coefficients in the expression of the right ascension of the mean Sun, $\mathrm { R A } ( U )$ , can be chosen so that UT may be regarded as mean solar time on the International (Greenwich) meridian.

The variation in the apparent motion of the Sun introduces a difference between local mean time (LMT) and the local apparent solar time (LAT) known as the equation of time. This is the difference between the time given by a sundial and the time given by a clock for a given location.

$$
\mathrm { L A T } = H _ { \odot } + 1 2 \mathrm { h o u r s } = \mathrm { L M T } + \mathrm { e q u a t i o n o f } \mathrm { t i m e } ,
$$

where $H _ { \odot }$ is the local hour angle of the Sun. The principal contributions to the equation of time arise from the eccentricity of the Earth’s motion around the Sun and the inclination of the plane of the ecliptic to the plane of the equator. The equation of time varies through the year in a smoothly periodic manner by up to 16 minutes (see Fig. 10.4). This is also the reason why in June and December, when the longest and shortest periods of sunlight occur, the times of sunrise and sunset do not reach their extreme values on the shortest and longest days.

![](images/6e3575298d4a626c4b51fea418477ac3ac335d3f2e927e894eeffd1c93c15f12.jpg)  
Fig. 10.4. Variation in the equation of time through the year.

# 10.5.2 Universal Time

As just mentioned, Universal Time conforms closely to the mean diurnal motion of the Sun. The apparent diurnal motion of the Sun involves both the non-uniform diurnal rotation of the Earth and the motion of the Earth in its orbit around the Sun. Universal Time is related to sidereal time or the stellar angle by means of a numerical formula. It can be derived at any instant from observations of the diurnal motion of stars or radio sources. The uncorrected, observed, rotational time scale, which is dependent on the place of observation, is designated UT0. When this is corrected for the shift in longitude of the observing station caused by polar motion, it is designated UT1. This is influenced by the variable rotation of the Earth and is the usual version of Universal Time.

Thus, UT1 is proportional to the angle of rotation of the Earth in space, around the true position of the rotation axis. The rate of UT1 is chosen so that the day of

UT1 is close to the mean duration of the solar day, and the phase of UT1 is chosen so that $1 2 ^ { \mathrm { h } }$ UT1 corresponds approximately to the instant when the Sun crosses the international meridian. In practice UT1 is determined from observations of sources defining the extragalactic reference frame (ICRF) and thus varies with the true rotation of the Earth.

Since January 1, 1984, Greenwich mean sidereal time (GMST) has been related to UT1 by the equation (Aoki et al., 1982):

$$
\begin{array} { r } { \mathrm { G M S T ~ f o r ~ 0 h ~ U T 1 } = 2 4 1 1 0 ^ { 5 } 5 4 8 4 1 + 8 6 4 0 1 8 4 ` 8 1 2 8 6 6 T _ { \mathrm { u } } ^ { \prime } } \\ { + 0 { \mathrm { : } } 0 9 3 1 0 4 { T _ { \mathrm { u } } ^ { \prime } } ^ { 2 } - 6 { \mathrm { : } } 2 \times 1 0 ^ { - 6 } { T _ { \mathrm { u } } ^ { \prime } } ^ { 3 } , \quad } \end{array}
$$

where $T _ { \mathrm { u } } ^ { \prime }$ is expressed in Julian centuries, $\mathrm { \Delta } T _ { \mathrm { u } } ^ { \prime } = d _ { \mathrm { u } } / 3 6 5 2 5$ , $d _ { \mathrm { u } }$ being the number of days of Universal Time elapsed since JD 2 451 545.0 UT1 (2000 January 1, 12h UT1 ) taking on values of $\pm 0 . 5 , \pm 1 . 5 , \pm 2 . 5 , \pm 3 . 5 , . . . .$

Let us note that the IAU 2000 precession–nutation series uses a different precession rate and an offset in obliquity. This produces a change in GMST, which can be written in microseconds, as:

$$
\mathrm { d } G M S T = ( - 1 8 3 3 0 . 2 6 6 T _ { \mathrm { u } } ^ { \prime } + 7 . 8 7 T _ { \mathrm { u } } ^ { \prime 2 } + 1 . 2 7 T _ { \mathrm { u } } ^ { \prime 4 } ) \mu \mathrm { s } .
$$

Now, with the introduction of the new intermediate reference system, UT1 is linearly proportional to the stellar angle (or Earth rotation angle). The definition of UT1 by its relationship with mean sidereal time is replaced by a similar definition as a function of the stellar angle. It is proportional to the angle $\theta$ defined in Section (10.4.4) as the angle between the TEO and the CEO. Thus, the definition of UT1 is such that the time derivative of UT1 is proportional to $\omega$ .

The numerical relationship between the stellar angle and UT1 has been derived (Capitaine et al., 2000) to be consistent with the conventional relationship between GMST and UT1. This provides the definition of UT1 for the ICRF. To an accuracy of $1 ~ \mu \mathrm { a s }$ , the relationship is

$$
\theta ( T _ { \mathrm { u } } ) = 2 \pi ( 0 . 7 7 9 0 5 7 2 7 3 2 6 4 0 + 1 . 0 0 2 7 3 7 8 1 1 9 1 1 3 5 4 4 8 T _ { \mathrm { u } } ) ,
$$

where $\theta$ is expressed in radians, and $T _ { \mathrm { u } }$ in days:

$$
T _ { \mathrm { u } } = ( \mathrm { J u l i a n ~ U T 1 ~ d a t e } - 2 4 5 1 5 4 5 . 0 ) .
$$

One can also express $\theta$ in seconds, that is in units analogous to those used for GMST in Equation (10.19):

$$
\theta _ { \mathrm { s } } ( T _ { \mathrm { u } } ) = ( 6 7 3 1 0 ^ { \mathrm { s } } . 5 4 8 4 1 0 0 1 + 8 6 6 3 6 ^ { \mathrm { s } } . 5 4 6 9 4 9 1 4 1 0 2 7 0 8 6 T _ { \mathrm { u } } ) .
$$

This linear expression shows that, as implied by its definition, and in contrast with GMST, the stellar angle for 0h UT1 is a constant.

# 10.5.3 Universal time scale

The variable rotation of the Earth being the basis for the UT1 time scale, the difference between UT1 and the uniform time scale TAI (Section 5.5.1) increases while the Earth rotation is slowing down, thus leading to the introduction of leap seconds into a uniform time scale also based on TAI, called UTC (Coordinated Universal Time). UTC is the basis for all civil timekeeping. The introduction of a leap second is decided by the IERS, when the difference, UT1−UTC, tends to be larger than 0.s 9, and the introduction takes place as a sixty-first second in the last minute of June or December.

The length of the SI second, in terms of the cesium atom, was determined in the mid 1950s from observations of the motion of the Moon with respect to the new cesium atomic time standard. The lunar orbit was related to the solar ephemeris of Newcomb that was developed in 1898. That ephemeris was based on observations of the Sun from the nineteenth century. The mean epoch of the observations was about 1850. From this ephemeris the second of Ephemeris Time had been defined, and it was to that ephemeris second that the cesium frequency was related. So, the SI second was really defined in terms of the second of time appropriate to the rotation of the Earth in 1850. Thus, a century and a half of Earth slowing is reflected in the difference between the current rate of rotation of the Earth and the current rate of the uniform time. This difference is expected to continue to increase and require more frequent leap seconds.

There is also the complication that modern electronic navigation and communication systems are based on the Uniform Time system, and they are not capable of accepting leap seconds. A system like the GPS navigation system cannot have a step in its time scale at critical times, such as when an aircraft is in final approach for a landing. This combination of more frequent leap seconds in the future and systems that cannot tolerate leap seconds has led to the initiation of studies of alternative means of relating a variable rotating Earth and a uniform, accurate time scale.

# 10.6 ITRF to ICRF transformations

The Earth rotation parameters define the coordinate transformation from a terrestrial reference (ITRF) frame (coordinates $x$ , $y , \ z )$ to a celestial reference (ICRF) frame (coordinates $X$ , Y, Z); taking into account the two components of $\mathcal { R } ^ { \star }$ defined by (10.10) and the transformation from the intermediate system to ICRS as described in Chapter 8, and which can be represented by the precession–nutation matrix $\mathcal { P } N ( t )$ . The latter is the product of the precession matrix $\mathcal { P }$ given by Equation (8.8) by the nutation matrix $\mathcal { N }$ or $\mathcal { N } ^ { \prime }$ given by Equations (8.18) or (8.20) respectively.

The overall transformation is generally written in the following form:

$$
\binom { X } { Y } = \mathcal { P } N ( t ) \times \mathcal { R } ( t ) \times \mathcal { W } ( t ) \times \binom { x } { y } ,
$$

where the fundamental components $\mathcal { P } N ( t ) , \mathcal { R } ( t ) , \mathcal { W } ( t )$ are the transformation matrices arising from the motion of the celestial pole in the CRS owing to precession and nutation, from the rotation of the Earth around the same pole, and from polar motion, respectively.

The $\mathcal { P } N ( t )$ matrix is the product of the $\mathcal { P } \times \mathcal { N }$ of the precession matrix $\mathcal { P }$ given by (8.8) by the nutation matrix $\mathcal { N }$ given by (8.19).

# 10.6.1 Classical and improved classical systems

The difference between these two systems lies only in the choice of different precession–nutation theories and poles (CEP, see Section 8.6.1, or CIP, see Section 8.4). The transformation algorithms are the same, so that the two cases are presented together.

In Equation (10.11), the matrix $\mathcal { W } ( t )$ is determined by the two components of the polar motion in terms of two small angles, $x$ and $y$ , which correspond to the coordinates of the celestial pole with respect to the terrestrial pole. The first matrix $\mathcal { R } _ { 3 } ( s ^ { \prime } )$ is not introduced in this case.

$$
\mathcal { W } ( t ) = \mathcal { R } _ { 1 } ( y ) \times \mathcal { R } _ { 2 } ( x ) .
$$

The matrix $\mathcal { R } ( t )$ is, similarly,

$$
\mathcal { R } ( t ) = \mathcal { R } _ { 3 } ( - \tau )
$$

In these equations, the axis of the rotation is defined by the conventions of Section 3.4.1. The quantity $\tau$ is the Greenwich sidereal time at date $t$ and is obtained in three steps.

(i) Take the relationship between Greenwich mean sidereal time (GMST) and Universal Time UT1 as given by Equation (10.21), possibly corrected by (10.22)   
(ii) Interpolate for any time of the day, and obtain $\mathrm { G M S T } ( t )$ . One must use the ratio $r$ of universal to sidereal time with the same notations as in (10.21): r = 1.002 727 909 350 795 + 5.9006 × 10−11T u − 5.9 × 10−15T u2 .   
(iii) Add the accumulated precession and nutation in right ascension as given by Aoki and Kinoshita (1983): $\tau = \mathrm { G M S T } + \Delta \psi \cos \epsilon _ { A } + 0 \sp { \prime } 0 0 2 6 4 \sin \varOmega + 0 \sp { \prime \prime } 0 0 0 0 6 3 \sin 2 \varOmega .$ (10.27)

Here, $\Delta \psi$ is the nutation in longitude and $\epsilon _ { A }$ is the obliquity of the ecliptic given by (10.17).

Thus, the angle $\tau$ refers to the ecliptic of date and includes Earth rotation, accumulated precession and nutation along the equator, crossed terms between precession and nutation, and crossed nutation terms (Capitaine and Gontier, 1993). The secular term in the GMST and UT1 relationship mixes UT1 and Barycentric Coordinate Time (TCB).

The third matrix of (10.24) $\mathcal { P } N ( t )$ is described above.

The above procedure conforms to the position and motion of the equinox specified in the IAU 1976 System of Astronomical Constants, the 1980 IAU Theory of Nutation, and the positions and proper motions of stars in the FK5 catalog. Improved values for constants in the above expressions may be available in the future.

# 10.6.2 CEO-based system

The ICRS eliminates any possible global rotation and any link to the orbital motion of the Earth. So in the new system the Earth Orientation Parameters (EOP) are based on the intermediary system defined by the CIP and the CEO. We have seen, in Chapter 8, that the position of the CIP is presented under the form of series for nutation in longitude $\Delta \psi$ and obliquity $\Delta \epsilon$ . The derivation of the position $( X , ~ Y , ~ Z )$ of the CIP, using the IAU 2000 precession–nutation series is described in Section 8.7.2.

The coordinate transformation from the ITRS to the ICRS at date $t$ is given by (10.24). The matrix $\mathcal { W } ( t )$ is given by (10.11) and the matrix $\mathcal { R } ( t )$ is given by (10.15). The precession–nutation matrix, $\mathcal { P } N ( t )$ , can be obtained in the following manner. Using the notations of Section 10.3.1, one has

$$
\begin{array} { l } { { X = \sin D \cos E , } } \\ { { \nonumber } } \\ { { Y = \sin D \sin E . } } \end{array}
$$

Let us call

$$
a = \frac { 1 } { ( 1 + \cos D ) } ,
$$

which can also be written with sufficient accuracy as

$$
a = \frac { 1 } { 2 } + \frac { 1 } { 8 } ( X ^ { 2 } + Y ^ { 2 } ) .
$$

Under these conditions, one has

$$
\mathcal { P } N ( t ) = \mathcal { R } _ { 3 } ( - E ) \times \mathcal { R } _ { 2 } ( - D ) \times \mathcal { R } _ { 3 } ( E ) \times \mathcal { R } _ { 3 } ( s ) .
$$

The notation $\mathcal { R } _ { i }$ follows the notations of Section 3.4.1. One may note, that $\mathcal { P } N ( t )$ can also be given in an equivalent form directly from $X$ and $Y$ as:

$$
\mathcal { P } N ( t ) = \left( \begin{array} { c c c } { 1 - a X ^ { 2 } } & { - a X Y } & { X } \\ { - a X Y } & { 1 - a Y ^ { 2 } } & { Y } \\ { - X } & { - Y } & { 1 - a ( X ^ { 2 } + Y ^ { 2 } ) } \end{array} \right) \cdot \mathcal { R } _ { 3 } ( s ) .
$$

# 10.7 Other effects

The accurate determination of the Earth orientation parameters requires the consideration of a number of forces and effects. In order to achieve consistent results, the IERS has established conventions that should be used for all data reduction procedures. These conventions are revised periodically and published as an IERS Technical Note by the IERS Central Bureau. Items that need to be considered in the different data reduction procedures include the geopotential model, site displacement due to ocean and atmospheric loading and solid Earth tides, tidal variations in the Earth’s rotation, the tropospheric model, atmospheric angular momentum, ocean currents, and plate tectonics.

# 11

Stars

The main objective of stellar astrometry is to determine the positions of stars in space at some epoch and to describe their displacements in time. The instruments used for observations, and how the positions are determined, are given in Kovalevsky (2002). The reference frames have been discussed in Chapters 7–10 of the present book. The observational reduction procedures and corrections for apparent displacements were described in Chapter 6.

Star positions are not an objective per se. What is of interest are the motions and distances of celestial bodies. The first are the proper motions that describe the apparent displacements due to the actual motion of stars with respect to the barycenter of the Solar System. As we have already seen in Chapter 6, in order to transfer Earth-based observations to a barycentric position, one has to correct for annual parallax. However, the value of the parallax coefficient has a major importance in astronomy, because it is the basic source of distances in the Universe. This is why the determination of distances is discussed in detail in this chapter. By adding radial velocity to a combination of proper motion and distance, one obtains the space motion of a star. In addition, a section on magnitudes and spectra is given, not only because they provide important information to be used together with astrometric parameters, but also because they enter in the reduction of astrometric observations.

The last sections of this chapter give an overview of the most important astrometric star catalogs and their accuracies, with an emphasis on the Hipparcos Catalogue, which brought a dramatic change in the accuracies and triggered the compilation of a large number of star catalogs.

# 11.1 Star positions

Traditionally, the position of a star at some time $t$ is given by two spherical coordinates. The most generally used system of coordinates is the equatorial system, so

that the position on the celestial sphere is given by:

- the right ascension $\alpha$ - the declination δ

as already defined in Section 3.8. The unit vector of the direction of the star in this system is:

$$
{ \bf S } = \left( \begin{array} { c } { { \cos \delta \cos \alpha } } \\ { { \cos \delta \sin \alpha } } \\ { { \sin \delta } } \end{array} \right) .
$$

However, two other systems of coordinates are sometimes used: ecliptic coordinates and galactic coordinates (Section 7.8).

# 11.1.1 Proper motion

The proper motion is the time derivative of the coordinates of a star at an epoch $t _ { 0 }$ , typically the epoch of the catalogue. The proper motion in equatorial coordinates is composed of two quantities:

- the proper motion in right ascension $\mu _ { \alpha } = ( \mathrm { d } \alpha / \mathrm { d } t ) _ { t = t _ { 0 } }$ , - the proper motion in declination $\mu _ { \delta } = ( \mathrm { d } \delta / \mathrm { d } t ) _ { t = t _ { 0 } }$ .

While $\mu _ { \delta }$ corresponds to an actual angle on the sky, $\mu _ { \alpha }$ is reckoned on the equator, so that the actual angular component along the local small circle is $\mu _ { \alpha } \cos \delta$ . For consistency reasons, we shall assume that $\mu _ { \delta }$ and $\mu _ { \alpha }$ are both expressed in arcseconds. This means that if $\mu _ { \alpha }$ is given in seconds of time, it must be multiplied by 15 to give arcseconds.

The proper motion is a vector on the tangent plane to the celestial sphere at the position $\alpha _ { 0 } , \delta _ { 0 }$ of the star at time $t$ (see Section 3.9.1). Its modulus is

$$
\mu = \sqrt { \mu _ { \alpha } ^ { 2 } \mathrm { c o s } ^ { 2 } \delta + \mu _ { \delta } ^ { 2 } }
$$

and its position angle $\phi$ reckoned from the North, Eastward from $0 ^ { \circ }$ to $3 6 0 ^ { \circ }$ is given by

$$
\begin{array} { r } { \mu _ { \alpha } \cos \delta = \mu \sin \phi } \\ { \mu _ { \delta } = \mu \cos \phi . } \end{array}
$$

Another way of describing this is to introduce the normal orthogonal vector triad at epoch $( \mathbf { p _ { 0 } } , \mathbf { q _ { 0 } } , \mathbf { r _ { 0 } } )$ such that

$$
\begin{array} { r } { \mathbf p _ { 0 } = \left( \begin{array} { c } { - \sin \alpha _ { 0 } } \\ { \cos \alpha _ { 0 } } \\ { 0 } \end{array} \right) ; \quad \mathbf q _ { 0 } = \left( \begin{array} { c } { - \sin \delta _ { 0 } \cos \alpha _ { 0 } } \\ { - \sin \delta _ { 0 } \sin \alpha _ { 0 } } \\ { \cos \delta _ { 0 } } \end{array} \right) , } \end{array}
$$

and $\mathbf { r _ { 0 } }$ is directed outwards from the celestial sphere. Then, the proper motion vector, $\mathbf { V }$ , is

$$
{ \bf V } = { \bf p _ { 0 } } \mu _ { \alpha } \cos \delta + { \bf q _ { 0 } } \mu _ { \delta } .
$$

We shall make use of this standard space triad (Section 3.9.3), and regard it as a fixed set of coordinate axes, strictly and completely defined by $\alpha _ { 0 }$ and $\delta _ { 0 }$ and, in particular, we shall consider that it is not affected by the observational uncertainty of $\alpha _ { 0 }$ and $\delta _ { 0 }$ .

# 11.2 Distance of stars

Stars are not infinitely distant. This is revealed by the annual parallax already defined and studied in Section 6.2. By definition, the annual parallax $\varpi$ expressed in parsecs is related to the distance $\rho$ by

$$
\rho = { \frac { 1 } { \varpi } }
$$

where $\varpi$ is expressed in arcseconds. Let us assume that the parallax was found to be $\varpi _ { 0 }$ with a standard uncertainty $\sigma$ , and that its probability density function (pdf) is normal (formula (4.12))

$$
f ( \varpi ) = \frac { 1 } { \sqrt { 2 \pi } \sigma } \exp \left[ \frac { - ( \varpi - \varpi _ { 0 } ) ^ { 2 } } { 2 \sigma ^ { 2 } } \right] .
$$

Let $\rho _ { 0 }$ be the corresponding value of the distance $\stackrel { \prime } { \rho } _ { 0 } = 1 / \varpi _ { 0 }$ ). The pdf of $\rho$ is no longer Gaussian in $\rho - \rho _ { 0 }$ , and in some cases is so different that the treatment of uncertainties must take this fact into account. Noting that

$$
\varpi - \varpi _ { 0 } = \frac { 1 } { \rho } - \frac { 1 } { \rho _ { 0 } } = \frac { \rho _ { 0 } - \rho } { \rho \rho _ { 0 } }
$$

and

$$
\mathrm { d } \varpi = - \frac { \mathrm { d } \rho } { \rho ^ { 2 } } ,
$$

the transformed pdf for $\rho$ is

$$
g ( \rho ) = \frac { 1 } { \sqrt { 2 \pi } \sigma \rho ^ { 2 } } \exp \left[ \frac { - ( \rho - \rho _ { 0 } ) ^ { 2 } } { 2 \sigma ^ { 2 } \rho ^ { 2 } \rho _ { 0 } ^ { 2 } } \right] .
$$

Another way of considering this distribution is to express it as a function of a relative shift, $x$ , in distance

$$
x = \frac { \rho - \rho _ { 0 } } { \rho _ { 0 } } ,
$$

![](images/170e384a793ee6e2f8dd7490a95c71ea80276eca6d60796e4bf9042ed60aa442.jpg)  
Fig. 11.1. Example of the pdf of the distance corresponding to an observed parallax $\varpi _ { 0 } = 1 / \rho _ { 0 }$ with an r.m.s. equal to $\sigma$ . In this example $\alpha = \rho _ { 0 } \sigma = 0 . 2$ . The other line presents, for the same value of $x$ , the pdf resulting from the assumptions of Lutz and Kelker (1973).

or $\rho = \rho _ { 0 } ( 1 + x )$ . Then formula (11.3) becomes, setting $\alpha = \rho _ { 0 } \sigma$ ,

$$
G ( x ) = \frac { 1 } { \sqrt { 2 \pi } \alpha ( 1 + x ) ^ { 2 } } \exp \left[ \frac { - x ^ { 2 } } { 2 \alpha ^ { 2 } ( 1 + x ) ^ { 2 } } \right] .
$$

The structure of $G ( x )$ depends only on the product of $\alpha = \rho _ { 0 } \sigma$ , or better, the ratio $\alpha = \sigma / \varpi _ { 0 }$ of the r.m.s. of the observed parallax to its value given by this observation. The function is not Gaussian as shown in Fig. 11.1. In particular, the maximum is shifted towards negative $x$ , meaning that the value $1 / \varpi _ { 0 }$ is somewhat over-estimated. Actually, the curve has one maximum and one minimum, given by the following expression, obtained by setting $\mathrm { d } G / \mathrm { d } x = 0$ ,

$$
x ^ { 2 } + \left( 2 + \frac { 1 } { 2 \alpha ^ { 2 } } \right) x + 1 = 0 .
$$

Figure 11.2 gives the value of the positive root as a function of $\alpha$ . It can be seen that the bias is negligible for values of $\alpha < 0 . 1$ , which, in the case of Hipparcos data $( \sigma = 1$ mas) corresponds to stars closer than 100 parsecs.

![](images/b8b8f9bd8e4f86b34b4830e2d633e0c332aa9d3e3e4b718eb6696c43ea7df80b.jpg)  
Fig. 11.2. Values of the maximums of the pdf resulting from classical statistical reasoning and those derived with the assumptions of Lutz and Kelker (1973).

Another approach was proposed by Lutz and Kelker (1973), and widely used in the literature. These authors assume that the stars are uniformly distributed in space. Then, the number of stars at distances between $\rho$ and $\rho + \mathrm { d } \rho$ is

$$
N ( \rho ) \mathrm { d } \rho = 4 \pi \rho ^ { 2 } \mathrm { d } \rho ,
$$

or, in terms of parallaxes,

$$
N ( \varpi ) \mathrm { d } \varpi = 4 \pi { \frac { \mathrm { d } \rho } { \varpi ^ { 4 } } } .
$$

As a consequence, (11.3) becomes

$$
F ^ { * } ( \varpi ) = \frac { \sqrt { 8 \pi } } { \sigma \varpi ^ { 4 } } \exp \left[ \frac { - ( \varpi - \varpi _ { 0 } ) ^ { 2 } } { 2 \sigma ^ { 2 } } \right] ,
$$

or

$$
G ^ { * } ( \rho ) = \frac { \sqrt { 8 \pi } \rho ^ { 2 } } { \sigma } \exp \left[ \frac { - ( \rho - \rho _ { 0 } ) ^ { 2 } } { 2 \sigma ^ { 2 } \rho ^ { 2 } \rho _ { 0 } ^ { 2 } } \right] .
$$

One can again use $x$ as the new variable and it is found that the maximum of the distribution is given by the smallest root of

$$
x ^ { 2 } + \left( 2 - \frac { 1 } { 2 \alpha ^ { 2 } } \right) x + 1 = 0 .
$$

An example of the Lutz and Kelker distribution is given in Fig. 11.1, and the value of the maximum as a function of $\alpha$ is given in Fig. 11.2. In this case, the value $\rho _ { 0 } = 1 / \varpi _ { 0 }$ appears to be an under-estimation of the parallax. Again the bias is negligible for small values of $\alpha$ .

It is necessary to point out, that, in this second approach, the parallax is no longer a result of an observation, but rather a new random variable with an a priori distribution law. It is to be used, assuming that the distribution is realistic, only in the case where the parallax is used as one of the parameters to search for some common feature, for example the absolute magnitude of a set of stars having the same spectral or photometric features, as was the case in the original paper by Lutz and Kelker (1973).

Another consequence of the special pdf for distances is that truncating a sample using the observed parallaxes necessarily induces a systematic error. The truncation must be performed using an independent parameter, for instance the apparent magnitude, but not the absolute magnitude determined from the value of the distance. Some pernicious effects of doing so are described in Luri and Arenou (1997).

In conclusion, whenever the distances are used as a parameter related to a given star, as in the case of kinematics or dynamics of the Galaxy, the function to be used is the one given by $g ( \rho )$ , and no Lutz and Kelker correction should be applied. However, this brings up another difficulty.

# 11.2.1 Uncertainties in distance determination

An essential feature of the functions $g ( \rho )$ or $G ( x )$ described in the previous section is that their integral from $- \infty$ to $+ \infty$ does not converge, so that they cannot be considered as being actual probability distributions around the observed value of the parallax. In particular, the second-order moments cannot be computed, because the integrals also do not converge. Therefore, it is necessary to transform $g ( \rho )$ or $G ( x )$ in such a way that the new function has all the properties of a pdf, and choose among the infinity of solutions those that best fit these functions in some given intervals of $\rho$ and $x$ , that have the largest probabilities of including the true values. If, in addition, this new pdf is Gaussian, it would have the advantage of giving an estimate of the uncertainty, a well-defined maximum that could be chosen as the best value of the distance, and provide the means of pursuing the calculation of any quantity that is a function of the distance, together with its uncertainty. This would be the case, for instance, of absolute magnitudes, transverse velocities expressed in kilometers per second, etc.

A simplistic approach to the problem of assigning an r.m.s. to the distance is to consider the two values of $\rho$ ,

$$
\rho _ { 1 } = \frac { 1 } { \varpi _ { 0 } + \sigma } ; \quad \rho _ { 2 } = \frac { 1 } { \varpi _ { 0 } - \sigma } ,
$$

and declare that the probability to have $\rho _ { 1 } < \rho < \rho _ { 2 }$ is the same as to have $\varpi _ { 0 } -$ $\sigma < \varpi < \varpi _ { 0 } + \sigma$ . This leads one to declare that $\sigma _ { \rho } = ( \rho _ { 2 } - \rho _ { 1 } ) / 2 .$ . This is actually an acceptable approximation for the condition that $\sigma$ is small with respect to $\varpi _ { 0 }$ . But this is not the case if $\alpha$ is large. For instance, if one has $\varpi _ { 0 } = 4 \pm 2$ mas, $\rho _ { 1 } =$ 167 pc and $\rho _ { 2 } = 5 0 0 \mathrm { p c }$ , while $\rho _ { 0 } = 2 5 0 \mathrm { p c }$ , the interval $\rho _ { 1 } - \rho _ { 2 }$ is not centered at $\rho _ { 0 }$ , and adopting $\sigma _ { \rho }$ as given above, one gets $8 3 < \rho < 4 1 6 \mathrm { p c }$ , which is nonsense. For smaller $\varpi _ { 0 }$ , one may be in a position to consider $\rho = \infty$ as probable.

Before going further, let us remark that if $\alpha$ is large, there remains, statistically speaking, a large probability for negative values of the distance. This is of course physically not acceptable, but for statistical consistency, one must take them into account. For this reason, in the Hipparcos Catalogue, some parallaxes are given that have been found negative and not replaced by zero. A possible approach is to filter out smoothly the lowest values of parallaxes by assigning them a weight that approaches zero gradually with $\varpi$ . Two techniques to do so are proposed by Smith and Eichhorn (1996). The simpler one realizes this weighting by the following functions:

$$
w ( \varpi , \sigma ) = \exp \left( - \eta \frac { \sigma ^ { 2 } } { \rho ^ { 2 } } \right) ,
$$

where $\eta$ is a free parameter that determines the width of the excised region around $\varpi = 0$ . This renders the function $g ( \rho )$ integrable and, provided that an adequate scaling is applied, it is transformed into a bona fide pdf. The major disadvantage is the presence of an adjustable parameter, whose value directly influences the value of the second moment. So, these weighting methods should be applied with great care, only for large $\alpha$ and when there is no additional external model, which can constrain the limits of acceptable distances such as, for instance, the Lutz and Kelker assumption on the distribution of stars or a distribution of absolute magnitudes (Smith, 1987).

The approach announced in the beginning of this section consists first of cutting $g ( \rho )$ at places beyond which the probability becomes practically negligible. The fit to a Gaussian pdf is realized within an interval of distances defined by

$$
A = \frac { 1 } { \varpi _ { 0 } + k \sigma } \leq \rho \leq \frac { 1 } { \varpi _ { 0 } - k \sigma } = B ,
$$

where $k$ is a number between 2 (probability to be outside the interval equal to 0.0455) and 3 (probability 0.0027), and $\varpi _ { 0 }$ is the observed value of the parallax. Evidently, this approach is possible only if $\varpi _ { 0 } / \sigma$ , which is $1 / \alpha$ , is not too large, namely that $k \ll \varpi _ { 0 } / \sigma = 1 / \alpha$ . But in many studies, one does not consider remote stars for which the distance is too badly determined. This is the case of all local kinematic or astrophysical studies.

Let us consider the function $G ( x )$ as given by equation (11.5), and define

$$
G ^ { \prime } ( x ) = \frac { G _ { 0 } } { \sqrt { 2 \pi } \alpha ( 1 + x ) ^ { 2 } } \exp \left[ \frac { - x ^ { 2 } } { 2 \alpha ^ { 2 } ( 1 + x ^ { 2 } ) } \right] ,
$$

where $G _ { 0 } = \sqrt { 2 \pi } \alpha$ is chosen in such a way that $G ^ { \prime } ( 0 ) = 1$ and let us represent it by

$$
F ( x ) = \frac { G _ { 0 } } { \sqrt { 2 \pi } s } \exp \left[ \frac { - ( x - x _ { \mathrm { m } } ) ^ { 2 } } { 2 s ^ { 2 } } \right] ,
$$

where $s$ is the new r.m.s. and $x _ { \mathrm { m } }$ the maximum of the function. The determination of these two parameters is made by minimizing

$$
I _ { A } = \int _ { a } ^ { 0 } ( G ( x ) - F ( x ) ) \mathrm { d } x ,
$$

and

$$
I _ { B } = \int _ { 0 } ^ { b } \left( G ( x ) - F ( x ) \right) \mathrm { d } x ,
$$

where $a$ and $b$ are the values of $x$ corresponding to A and B:

$$
a = \frac { A - \rho _ { 0 } } { \rho _ { 0 } } ; ~ b = \frac { B - \rho _ { 0 } } { \rho _ { 0 } } ,
$$

with the additional condition that $I _ { A } = I _ { B }$ . Since $G ^ { \prime } ( x )$ is a one-parameter function, the resulting values of $s$ and $x _ { \mathrm { m } }$ are functions only of $\alpha$ , so that they can be determined in advance. Figure 11.3 illustrates this fit in the case of $\alpha = 0 . 2$ . In Fig. 11.4, the values of $m _ { 0 }$ and $s$ are given as a function of $\alpha$ .

# 11.3 Space motions

The positions of stars are not fixed. After correcting the apparent positions for various parallaxes, what remains is their motion with respect to the barycenter of the Solar System. This motion is divided into two components.

(i) The motion perpendicular to the line of sight is the proper motion (Section 11.1.1) expressed in arcseconds either per century or per year. We shall assume in what follows that they are yearly proper motions expressed in arcseconds per year.   
(ii) The motion along the line of sight is the radial velocity. Obtained from measurements of the Doppler shift of spectral lines, it is expressed in kilometers per second. We must, however, ascertain that the observations are corrected for the motions of the Earth and reduced to the value at the barycenter of the Solar System.

![](images/28c812cac2e9336241c6e34ad740b406121f1399a0bacf0e1679d5988674a01a.jpg)  
Fig. 11.3. Representation of $G ^ { \prime } ( x )$ by a Gaussian pdf $F ( x )$ for $\alpha = 0 . 2$ . The limits correspond to $k = 2 . 5$ (probability to be outside the interval is $1 . 3 \%$ ). Arrows show the values of $x$ corresponding to the maximums of distributions. In this computation, the shaded areas almost cancel out. The integrated weighted probability of this area is $3 . 3 \%$ .

![](images/a9a8eceeac886c52b9a0f5cbb76a5e0e7f6bb236a8a6afcacb181d5369c42fac.jpg)  
Fig. 11.4. Plot of the r.m.s. $\sigma$ in $x$ as a function of $\alpha$ for the best-fit Gaussian, computed assuming $k = 2 . 5$ .

# 11.3.1 Radial velocities

Let us consider a source moving with respect to an observer with a velocity $v$ whose direction has an angle $\theta$ with the direction source–observer, and emits a wavelength $\lambda _ { 0 }$ . The apparent wavelength as perceived by the observer is

$$
\lambda = \lambda _ { 0 } \Bigl ( 1 - \frac { v } { c } \cos \theta \Bigr ) ,
$$

where $c$ is the speed of light. If the source recedes from the observer, $\cos \theta < 0$ and $\lambda > \lambda _ { 0 }$ and the light seems redder. If it approaches the observer, cos $\theta > 0$ and $\lambda < \lambda _ { 0 }$ , the light seems to be bluer. This is the classical Doppler effect.

Remark. The atom is a small clock, which in its proper reference system has a period $T _ { 0 }$ . Following the general relativity theory, in a reference frame with respect to which it moves, with a velocity $v$ , the period is (Section 5.2.5):

$$
T = T _ { 0 } / { \sqrt { 1 - v ^ { 2 } / c ^ { 2 } } } .
$$

This modifies the actual wavelength, so that the modified formula for Doppler effect is

$$
\lambda = \lambda _ { 0 } \left( 1 - \frac { v } { c } \cos \theta \right) / \sqrt { 1 - v ^ { 2 } / c ^ { 2 } } .
$$

For stars in the Galaxy, $v < 5 0 0 \mathrm { k m / s }$ , the correcting relativistic factor is negligible, taking into account that star’s radial velocities are observed with a precision at the best of $0 . 1 \mathrm { k m } / \mathrm { s }$ . The Doppler shift, which is measured by comparing the stellar spectrum with the spectrum of a fixed emitter, is

$$
\Delta \lambda = \lambda - \lambda _ { 0 } = \lambda _ { 0 } \left( { \frac { V _ { \mathrm { r } } ^ { \prime \prime } } { c } } \right) ,
$$

where $V _ { \mathrm { r } } ^ { \prime \prime } = - v \cos { \theta }$ is called the radial velocity,

$$
V _ { \mathrm { r } } ^ { \prime \prime } = \frac { c \Delta \lambda } { \lambda _ { 0 } } ,
$$

chosen to be positive when the star is receding from the observer along the $\mathbf { r _ { 0 } }$ axis.

The observed radial velocity $V _ { \mathrm { r } } ^ { \prime \prime }$ is topocentric. One has to transform it into the barycentric system of coordinates by subtracting the projection on the direction of the object, of the observer’s velocity around the axis of rotation of the Earth, $ { \mathbf { u } } ^ { \prime }$ , and of the velocity of the geocenter with respect to the barycenter of the Solar System, $\mathbf { u }$ .

In equatorial coordinates, the components of the radial velocity vector, $\mathbf { V } _ { \mathrm { r } } ^ { \prime \prime }$ , are

$$
\mathbf { V } _ { \mathrm { r } } ^ { \prime \prime } \left\{ \begin{array} { l l } { V _ { \mathrm { r } } ^ { \prime \prime } \cos \delta \ \cos \alpha } \\ { V _ { \mathrm { r } } ^ { \prime \prime } \cos \delta \ \sin \alpha } \\ { \quad \quad \quad V _ { \mathrm { r } } ^ { \prime \prime } \sin \delta . } \end{array} \right.
$$

The velocity $ { \mathbf { u } } ^ { \prime }$ of the observer on the Earth is perpendicular to the local meridian. Its equatorial components are

$$
{ \bf u } ^ { \prime } \left\{ \begin{array} { c } { r \omega \sin T _ { \mathrm { l } } } \\ { - r \omega \cos T _ { \mathrm { l } } } \\ { 0 , } \end{array} \right.
$$

where $r$ is the distance, in kilometers, from the observer to the axis of rotation of the Earth, $\omega$ the rate of rotation of the Earth expressed in radians per second $( \omega = 0 . 0 0 0 0 7 2 5 2 3 4 8 9 )$ and $T _ { \mathrm { l } }$ the local sidereal time.

The velocity $\mathbf { u }$ of the geocenter with respect to the barycenter of the Solar System is derived from the ephemerides of the Earth’s motion. For instance in the JPL series of Development Ephemerides, the current one in 2002 is DE 405, which gives the rectangular coordinates in the ICRS from which the time derivatives may be computed in kilometers per second.

The actual barycentric radial velocity vector is, therefore,

$$
\mathbf { V } _ { \mathrm { r } } = ( \mathbf { V } _ { \mathrm { r } } ^ { \prime \prime } - \mathbf { u } ^ { \prime } - \mathbf { u } ) ,
$$

and the barycentric radial velocity is

$$
V _ { \mathrm { r } } = \mathbf { V } _ { \mathrm { r } } \cdot \mathbf { S } ,
$$

where $\mathbf { S }$ is the unit vector of the barycentric direction of the star.

# 11.3.2 Motions in space

Both proper motions and radial velocities are expressed in different units. To obtain the three components of the motion in space, one has to write the proper motion in kilometers per second. To do this, it is necessary to know the distance $\rho$ of the star. However, in what follows, we shall use $\varpi = 1 / \rho$ , whether or not the corrections for $\rho$ presented in Section 11.2 are made.

The annual proper motion, $\mu$ , can be readily expressed in astronomical units per year. From the actual definition of the parallax, it is $\mu / \varpi$ . In order to express it in kilometers per second, one has to divide it by the number of seconds in a Julian year:

$$
s = 0 . 3 1 5 5 7 6 \times 1 0 ^ { 7 } ,
$$

and to multiply it by the number of kilometers in an astronomical unit:

$$
a = 0 . 1 4 9 5 9 7 8 7 \times 1 0 ^ { 9 } .
$$

So, the transverse velocity (in $\mathrm { k m } / \mathrm { s }$ ) is:

$$
V _ { \mathrm { T } } = 4 . 7 4 0 4 7 { \frac { \mu } { \varpi } } = A { \frac { \mu } { \varpi } } .
$$

Often, it is sufficient to take $A = 4 . 7 4$ . Other values are sometimes given in the literature, because the usage was to consider the tropical rather than the Julian year. The correct value to use is $A = 4 . 7 4 0 4 7$ .

The standard expression for the space velocity is:

$$
{ \bf V } = A \frac { \mu _ { \alpha } } { \varpi } \cos \delta { \bf p } _ { 0 } + A \frac { \mu _ { \delta } } { \varpi } { \bf q } _ { 0 } + V _ { \mathrm { r } } { \bf r } _ { 0 } .
$$

However, a more accurate formula must be used in some occasions. This is obtained, if one no longer neglects the light-time effect described in Section 6.5, by dividing the preceding expression by $k = 1 - V _ { \mathrm { r } } / c$ . So, that the actual formula is:

$$
{ \bf V } = \frac { 1 } { k } \left( A \frac { \mu _ { \alpha } } { \varpi } \cos \delta { \bf p } _ { 0 } + A \frac { \mu _ { \delta } } { \varpi } { \bf q } _ { 0 } + V _ { \mathrm { r } } { \bf r } _ { 0 } \right) .
$$

For most of the cases in galactic astronomy, with the exception of close highvelocity stars, one may neglect the factor $k$ , but it is an important correction for large radial velocities, for instance for extragalactic objects.

# 11.3.3 Variability of proper motions

In their motions in the Galaxy, stars undergo gravitational forces that may modify their velocities, so that their proper motions and radial velocities vary with time. There is no general theory, and the effect is to be studied case by case from a dynamical point of view. However, there is a class of objects where neglecting this effect may lead to serious errors.

To assume that the space motion of a star is linear means that the center of mass of the system represented by the star coincides with the star. This is often not the case, many stars are double or multiple systems and each component moves around a common barycenter, which is the point that has a linear motion in space, while the apparent proper motion of each component is curved. To detect such variations in proper motion is one of the methods used to detect so-called astrometric binaries. This problem will be described in Section 12.4. It is necessary to have this possibility in mind when dealing with proper motions and radial velocities, and be cautious that the apparent motion may be a combination of the space motion of the stellar system and the orbital motion of the observed star.

Another case is the secular or perspective acceleration, which is a purely geometric effect due to the variation of the proper motion of an approaching or receding object. Let $V$ be the space velocity and $\theta$ its angle with the direction of the star, whose distance is $\rho _ { 0 }$ (Fig. 11.5). The modulus $\mu$ of the proper motion is

$$
\mu = \frac { V \sin \theta } { \rho } .
$$

Taking its derivative with respect to time, one gets

$$
{ \frac { { \mathrm { d } } \mu } { { \mathrm { d } } t } } = - { \frac { V } { \rho ^ { 2 } } } \sin \theta { \frac { { \mathrm { d } } \rho } { { \mathrm { d } } t } } + { \frac { V } { \rho } } \cos \theta { \frac { { \mathrm { d } } \theta } { { \mathrm { d } } t } } .
$$

![](images/bf23233434de3d3ecce02c1d05214dc594a0f3ce0458b711896260ecf7f97183.jpg)  
Fig. 11.5. Definition of the angle $\theta$ and its variation $\mathrm { d } \theta$ when the star moved by $\mu$ .

From the triangle $O S P$ in Fig. 11.5, one can see that $\mathrm { d } \theta / \mathrm { d } t = - \mu$ , and $V \cos \theta =$ $V _ { \mathrm { r } } = \mathrm { d } \rho / \mathrm { d } t$ . One has therefore

$$
\frac { \mathrm { d } \mu } { \mathrm { d } t } = - \frac { \mu } { \rho } \frac { \mathrm { d } \rho } { \mathrm { d } t } - \frac { \mu } { \rho } V _ { \mathrm { r } } = - \frac { 2 \mu } { \rho } V _ { \mathrm { r } } ,
$$

or, if $\mu$ is expressed in arcseconds per year, $\varpi$ in arcseconds, $V _ { \mathrm { r } }$ in kilometers per second,

$$
{ \frac { \mathrm { d } \mu } { \mathrm { d } t } } = - 0 . 0 0 0 0 0 0 2 0 5 \mu \varpi V _ { \mathrm { r } } .
$$

This correction is significant only for nearby stars with high radial velocities.

# 11.3.4 Epoch transformation

Independent of the physical importance of proper motions and space velocities in the kinematic and dynamic studies of the Galaxy and other star systems, formula (11.11) is the basis of the computation of star positions at some epoch $T$ , different from the basic epoch $T _ { 0 }$ at which positions and proper motions are given. If one assumes that the parameters are uncorrelated, one has, putting $t = T - T _ { 0 }$ ,

$$
\begin{array} { r } { \alpha = \alpha _ { 0 } + t \mu _ { \alpha _ { 0 } } } \\ { \delta = \delta _ { 0 } + t \mu _ { \delta _ { 0 } } . } \end{array}
$$

However, this is an approximate solution. Let us make a rigorous treatment of the problem. At the time $t _ { 0 }$ , the barycentric direction of the star $S$ is $\bf u _ { 0 } = \bf r _ { 0 }$ and the radius vector is

$$
\mathbf { B S } = \mathbf { b } ( 0 ) = \mathbf { r _ { 0 } } { \frac { A } { \varpi _ { 0 } } } .
$$

The proper motion vector is:

$$
\begin{array} { r } { { \bf M _ { 0 } } = { \bf p _ { 0 } } \mu _ { \alpha } ^ { \star } + { \bf q _ { 0 } } \mu _ { \delta } , } \end{array}
$$

where we have assumed again, that the proper motion components are in arcseconds per year, and introduced the simplified notations

$$
\begin{array} { c } { { \alpha ^ { \star } = \alpha \cos \delta , } } \\ { { \mu _ { \alpha } { } ^ { \star } = \mu _ { \alpha } \cos \delta . } } \end{array}
$$

The space velocity $\mathbf { V }$ , which is assumed not to vary with time, is given by (11.11) in which we neglect the coefficient $k$

$$
{ \bf V } = { \bf p } _ { 0 } \frac { A } { \varpi _ { 0 } } \mu _ { \alpha ^ { \star } } + { \bf q } _ { 0 } \frac { A } { \varpi _ { 0 } } \mu _ { \delta } + { \bf r } _ { 0 } V _ { \mathrm { r } } ,
$$

that we write somewhat differently in order to have $A / \varpi$ as a factor. Putting

$$
\zeta _ { 0 } = V _ { \mathrm { r } } \frac { \varpi _ { 0 } } { A } ,
$$

one gets

$$
\mathbf { V } = { \frac { A } { \varpi _ { 0 } } } ( \mathbf { p } \mathbf { 0 } \mu _ { \alpha ^ { \star } } + \mathbf { q } \mathbf { 0 } \mu _ { \delta } + \mathbf { r } \mathbf { 0 } \zeta _ { 0 } ) .
$$

At time $t = T - T _ { 0 }$ , the radius vector is

$$
\mathbf { b } ( t ) = \mathbf { b } ( 0 ) + \mathbf { V } t .
$$

The unit vector at time $t$ is

$$
{ \bf u } _ { 0 } ( t ) = \left( { \bf r } _ { 0 } ( 1 + \zeta _ { 0 } t ) + { \bf M } _ { 0 } t \right) f ,
$$

where $f$ is a normalizing factor equal to

$$
f = \left| { \bf b } ( 0 ) \right| / \left| { \bf b } ( t ) \right| .
$$

Recalling that

$$
\vert \mathbf { b } ( 0 ) \vert = \left. \mathbf { r _ { 0 } } { \frac { A } { \varpi _ { 0 } } } \right. = { \frac { A } { \varpi _ { 0 } } } ,
$$

and

$$
\vert \mathbf { b } ( t ) \vert ^ { 2 } = \vert \mathbf { b } ( 0 ) \vert ^ { 2 } + 2 \mathbf { b } ( 0 ) \cdot \left( { \frac { A } { \varpi _ { 0 } } } \mathbf { M } _ { 0 } + \mathbf { r } _ { 0 } \zeta _ { 0 } \right) t + \left( { \frac { A } { \varpi _ { 0 } } } \mathbf { M } _ { 0 } + \mathbf { r } _ { 0 } \zeta _ { 0 } \right) ^ { 2 } t ^ { 2 } ,
$$

one obtains:

$$
f = \frac { 1 } { \sqrt { 1 + 2 \zeta _ { 0 } t + \left( M _ { 0 } ^ { 2 } + \zeta _ { 0 } ^ { 2 } \right) t ^ { 2 } } } ,
$$

and, after differentiation,

$$
\frac { \mathrm { d } f } { \mathrm { d } t } = - f ^ { 3 } \left( \zeta _ { 0 } + \left( M _ { 0 } ^ { 2 } + \zeta _ { 0 } \right) \right) t .
$$

Then, we can determine the new parallax

$$
\varpi ( t ) = \varpi _ { 0 } f .
$$

Differentiating (11.15), one gets the proper motion vector at time $t$ . After reduction, one simplifies the expression and gets

$$
\mathbf { M _ { 0 } } ( t ) = \left( \mathbf { M _ { 0 } } ( 1 + \zeta _ { 0 } t ) - \mathbf { r _ { 0 } } M _ { 0 } ^ { 2 } t \right) f ^ { 3 } .
$$

Finally, the sixth parameter $\zeta _ { 0 }$ becomes

$$
\zeta _ { 0 } ( t ) = V _ { \mathrm { r } } ( t ) \frac { \varpi ( t ) } { A } = \frac { \mathrm { d } \left( b ( t ) \right) } { \mathrm { d } t } f \frac { \varpi _ { 0 } } { A } .
$$

The derivative of $b ( t )$ is readily obtained knowing that $f ^ { 2 } = { \bf b } ( 0 ) ^ { 2 } / { \bf b } ( t ) ^ { 2 } .$ So finally, one has

$$
\begin{array} { r } { \varsigma ( t ) = \left[ \zeta _ { 0 } + \big ( M _ { 0 } ^ { 2 } + \zeta _ { 0 } ^ { 2 } \big ) t \right] f ^ { 3 } . } \end{array}
$$

Formulae (11.15), (11.17) and (11.18) describe fully the transformation from the parameters at time $T _ { 0 } , ( \alpha _ { 0 } ^ { \star } , \ \delta _ { 0 } , \ \varpi$ $\varpi _ { 0 }$ , $\mu _ { \alpha _ { 0 } \star }$ , $\mu _ { \delta _ { 0 } }$ , $V _ { r _ { 0 } , }$ ), and their value at time $T _ { 0 } + t$ , $( \alpha ^ { \star } ( t ) , \ \delta ( t )$ , $\varpi$ , $\mu _ { \alpha ^ { \star } } ( t )$ , $\mu _ { \delta } ( t )$ , $V _ { \mathrm { r } } ( t ) )$ . This transformation is reversible and the same formulae may be used backwards by replacing $t$ by $- t$ . Needless to say, this transformation includes the effect of secular acceleration.

Let us remark, however, that the origin of the proper motion vector $\mathbf { M _ { 0 } } ( t )$ is ${ \bf { u } } _ { \bf { 0 } } ( t )$ , and it is, therefore, necessary to consider the local propagated triad $\mathbf { p } ( t ) , \mathbf { q } ( t ) , \mathbf { r } ( t )$ , where $\mathbf { r } ( t )$ is the unit vector of ${ \bf b } ( t )$ so that one has:

$$
\mathbf { M } ( t ) = \mu _ { \alpha ^ { \star } } ( t ) \mathbf { p } ( t ) + \mu _ { \delta } ( t ) \mathbf { q } ( t ) .
$$

# 11.3.5 Uncertainty propagation

The above transformation of astrometric parameters from time $T _ { 0 }$ to time $T _ { 0 } + t$ is only part of the expected results. It is also necessary to determine r.m.s. uncertainties for these parameters, and also to see how correlations develop with time. Let us first consider the simplistic approach with formula (11.13), namely assuming correlation only between a coordinate and the corresponding component of the proper motion,

$$
\begin{array} { r } { \alpha ^ { \star } ( t ) = \alpha _ { 0 } ^ { \star } + t \mu _ { \alpha _ { 0 } ^ { \star } } , } \\ { \delta ( t ) = \delta _ { 0 } + t \mu _ { \delta 0 } . } \end{array}
$$

The derivation of uncertainties at time $t$ is given in the example of Section 4.2.

$$
\begin{array} { r l } & { \sigma _ { \alpha ^ { \star } } ^ { 2 } ( t ) = \big [ \sigma _ { \alpha ^ { \star } } ^ { 2 } + 2 t \rho _ { \mu _ { \alpha ^ { \star } } } \sigma _ { \alpha ^ { \star } } \sigma _ { \mu _ { \alpha ^ { \star } } } + t ^ { 2 } \sigma _ { \mu _ { \alpha ^ { \star } } } \big ] _ { 0 } , } \\ & { \sigma _ { \delta } ^ { 2 } ( t ) = \big [ \sigma _ { \delta } ^ { 2 } + 2 t \rho _ { \mu _ { \delta } } \sigma _ { \delta } \sigma _ { \mu _ { \delta } } + t ^ { 2 } \sigma _ { \mu _ { \delta } } ^ { 2 } \big ] _ { 0 } . } \end{array}
$$

This result can also be obtained using the generalized transformation of Section 4.2.3.

With the above stated assumption concerning the correlations, the variance– covariance matrix at time $T _ { 0 }$ is

$$
\mathcal { C } = \left( \begin{array} { c c c c } { \sigma _ { \alpha ^ { \star } } ^ { 2 } } & { 0 } & { \sigma _ { \alpha ^ { \star } } \sigma _ { \mu _ { \alpha ^ { \star } } } \rho _ { \alpha ^ { \star } } \rho _ { \mu _ { \alpha ^ { \star } } } } & { 0 } \\ { 0 } & { \sigma _ { \delta } ^ { 2 } } & { 0 } & { \sigma _ { \delta } \sigma _ { \mu _ { \delta } } \rho _ { \delta \mu _ { \delta } } } \\ { \sigma _ { \alpha ^ { \star } } \sigma _ { \mu _ { \alpha ^ { \star } } } \rho _ { \alpha ^ { \star } } \rho _ { \mu _ { \alpha ^ { \star } } } } & { 0 } & { \sigma _ { \mu _ { \alpha ^ { \star } } } ^ { 2 } } & { 0 } \\ { 0 } & { \sigma _ { \delta } \sigma _ { \mu _ { \delta } } \rho _ { \delta \mu _ { \delta } } } & { 0 } & { \sigma _ { \mu _ { \delta } } ^ { 2 } } \end{array} \right) .
$$

The Jacobian $\mathcal { I }$ of the transformation is

$$
\mathcal { I } = \left( \begin{array} { c c c c } { 1 } & { 0 } & { t } & { 0 } \\ { 0 } & { 1 } & { 0 } & { t } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right) ,
$$

and if one computes $\begin{array} { r } { \mathcal { S } = \mathcal { I C } \mathcal { I } ^ { \top } } \end{array}$ , one obtains the new $\sigma _ { \alpha ^ { \star } } ^ { 2 } ( t )$ and $\sigma _ { \delta } ^ { 2 } ( t )$ as given by (11.19), and the two new correlation coefficients:

$$
\begin{array} { r } { \rho _ { \alpha ^ { \star } \mu _ { \alpha ^ { \star } } } ( t ) = \frac { \sigma _ { \alpha ^ { \star } } \sigma _ { \mu _ { \alpha ^ { \star } } } \rho _ { \alpha ^ { \star } \mu _ { \alpha } ^ { \star } } + \sigma _ { \alpha ^ { \star } } ^ { 2 } t } { \sigma _ { \alpha ^ { \star } } ( t ) \sigma _ { \mu _ { \alpha } ^ { \star } } } , } \\ { \rho _ { \delta \mu _ { \delta } } ( t ) = \frac { \sigma _ { \delta } \sigma _ { \mu _ { \delta } } \rho _ { \delta \mu _ { \delta } } + \sigma _ { \mu \delta } ^ { 2 } t } { \sigma _ { \delta } ( t ) \sigma _ { \mu _ { \delta } } } . } \end{array}
$$

The other correlation coefficients remain null and the r.m.s. uncertainties in $\mu _ { \alpha ^ { \star } }$ and $\mu _ { \delta }$ are not changed.

For the most general case of the complete transformation of the six parameters as presented in Section 11.3.4, one must take the more-general $6 \times 6$ variance– covariance matrix. The $6 \times 6$ terms of the Jacobian can be found in ESA (1997, Section 1.5.5).

# 11.4 Magnitudes

Although photometry is not an astrometric technique, the apparent intensity of a celestial source is a major parameter in assessing the quality of the astrometric observations and of the results that can be derived. For instance, it is evident that the precision with which a star position may be observed depends directly on its brightness. The fainter the celestial objects appear to be, the more difficult it is to set a micrometer on its image, or to measure it on a photographic plate or on a CCD. At some level of faintness, the object is no longer observable even if its image is exposed for some time on the detector. Alternatively, bright objects in the field of view saturate the detector, and cannot be measured as accurately as well-exposed images on CCDs. To take this fact into account in the astrometric reduction procedure, it is necessary to quantify the photometric properties of the source. It is therefore useful that the bases of this quantification be presented here.

# 11.4.1 Luminous intensity and flux

The intensity of a source characterizes the energy that is emitted by the source in a unit of time. It is generally frequency dependent, and one defines a specific intensity, $I _ { \lambda }$ , at a wavelength $\lambda$ , or a frequency, $\nu = c / \lambda$ , expressed in hertz. The flux is expressed in $\mathrm { W } / ( \mathrm { m } ^ { 2 } \mathrm { H z } \mathrm { s r } )$ . In general, what is useful is the integral of $I _ { \nu }$ over the medium and the instrumental filters. Let $T ( \lambda )$ be the transmission, that is the proportion of light that is recorded by the instrument. The transmitted intensity is

$$
I _ { T } = \int _ { 0 } ^ { \infty } T \left( \lambda \right) I _ { \lambda } d _ { \lambda } .
$$

What is actually observed is an energy collected by a detector. This is measured by the flux density, or flux which is the power of the radiation per unit area, expressed in $\mathbb { W } / ( \mathrm { m } ^ { 2 } \mathrm { H z } )$ , or $\mathrm { W } / \mathrm { m } ^ { 2 }$ , if it is a global transmitted flux density. It is a very small quantity, and in radio astronomy, it is expressed in janskys (1 jansky $=$ $1 0 ^ { - 2 6 } \mathrm { W / ( m ^ { 2 } H z ) } ;$ ).

The energy collected by a receiver per second, or flux, is the power going through some surface and is expressed in watts.

# 11.4.2 Apparent magnitudes

In astronomical photometry, the flux observations are not absolute. The expression of flux in watts is not easily measured, and it is the ratio of fluxes, which is generally determined. This leads to the definition of magnitude scales, which all refer to some standard stars used to define a magnitude equal to zero. If $F _ { 0 }$ is the flux recorded for this reference, and $F$ is the flux recorded for another star in the same experimental conditions, one defines the magnitude $m$ of the second star as

$$
m = - 2 . 5 \log { \frac { F } { F _ { 0 } } } ,
$$

where the logarithm is the decimal logarithm. The difference of magnitudes between two stars $S _ { 1 }$ and $S _ { 2 }$ whose fluxes are respectively $F _ { 1 }$ and $F _ { 2 }$ is

$$
m _ { 1 } - m _ { 2 } = \Delta m = - 2 . 5 \log { \frac { F _ { 1 } } { F _ { 2 } } } .
$$

A good approximation, although it is not exact, is that a difference of 5 magnitudes corresponds a ratio of fluxes equal to $( 2 . 5 ) ^ { 5 } \simeq 1 0 0$ .

![](images/5fcf1b58927621743905816edef16f9180805a7fce4b2dfe6ca276e89f45daac.jpg)  
Fig. 11.6. Sensitivity curves for the $U B V$ Johnson system, the $R$ and $I$ bands, and the wide-band Hipparcos system $H i p$ . The medium wavelengths are respectively 0.365, 0.44, 0.55, 0.70, and $0 . 9 0 \mu \mathrm { m }$ (Zombeck, 1990).

# 11.4.3 Magnitude scales

The flux measured depends on the instrument and on the type of receivers. This could lead to great inconsistencies in magnitudes determined by different instruments, using different filters. For this reason, there is a general consensus in defining magnitude systems or scales, with reference filters that are used to reproduce the transmissions required by the definition. Figure 11.6 shows the sensitivity curves of the most popular system called $U B V$ ( $U =$ ultraviolet, $B = { \mathrm { b l u e } }$ , $V =$ visual). It is defined by a certain number of standard stars which set the origin $( \mathrm { m a g } = 0 $ ) and the scale. Another wide-band photometric scale was derived from the photometric observations by Hipparcos (see also Fig. 11.6), while the million stars of the Tycho Catalogue have magnitudes given in scales that are very close to $B$ and $V$ . Another photometric scale was commonly used in photographic astronomy and is called photographic magnitudes $m _ { \mathrm { p g } }$ . It used to correspond to the response of early photographic plates. It is close to the blue Johnson filter, and the two scales are related by

$$
m _ { \mathrm { p g } } = B - 0 . 1 1 .
$$

One should also mention the $I$ (infrared scale), which is becoming increasingly useful in astrometry, and another important photometric system defined for the SLOAN Digital Sky Survey (SDSS). The photometric system consists of five filters whose characteristics are given in Table 11.1. Most of the astrometric instruments, as well as the atmospheric refraction, are sensitive to the spectral distribution of energy. As a consequence, the image of the star is spread along a small spectrum.

Table 11.1. Wavelengths of the SLOAN photometric survey   

<table><tr><td>Filter name</td><td>Central wavelength</td><td>Wavelength width</td></tr><tr><td>ú&#x27;gr&#x27;i</td><td>350</td><td>60</td></tr><tr><td></td><td>480</td><td>140</td></tr><tr><td></td><td>625</td><td>140</td></tr><tr><td></td><td>770</td><td>150</td></tr><tr><td>Z</td><td>910</td><td>120</td></tr></table>

Depending on the color of the star, the position of its centroid is shifted. An indicator of this shift, to be corrected for astrometric purposes, is the color index $c$ defined as

$$
c = B - V .
$$

For instruments that are sensitive to the red part of the spectrum, one uses also the color index $V - I$ rather than $B - V$ .

# 11.4.4 Absolute magnitudes

The magnitudes defined in the preceding section are apparent magnitudes, that is the apparent luminosity as seen from the Earth after corrections for the absorption by the atmosphere and the instrument, so as to reproduce the sensitivity required by the definition of the chosen scale. But this does not give any information on the actual luminosity of the star. To do this, an absolute magnitude is defined as the magnitude the star would have if it were at a distance of $1 0 \mathrm { p c }$ . Since the apparent luminosity decreases as the inverse square of the distance, the absolute magnitude $M$ is defined as

$$
m - M = 5 \mathrm { l o g } \rho - 5 = - 5 ( 1 + \mathrm { l o g } \varpi ) .
$$

The quantity $m - M$ is called the distance modulus. It is necessary to specify in which photometric system the absolute magnitude is reckoned $( M _ { V } , M _ { B }$ , etc.).

Actually, the important astrophysical quantity is the total energy flux emitted by the star. It is not directly obtained by observation, and the corrections (for instance to $M _ { V }$ ) imply modeling of the star as a function of its effective temperature, gravity, spectrum, etc., and correcting for interstellar extinction. The results are bolometric magnitudes which are not currently used in astrometry, although they are the correct parameters to be used in analyzing the mass–luminosity relationship and in discussing physical properties of stars.

# 11.4.5 Stellar spectral types

Often, in astrometric star catalogs, the color is not provided and, instead, there is an indication of their spectral type. Although various spectral types are defined by criteria in terms of the presence, or absence, of some spectral lines, their determination is partly a matter of interpretation, especially when one is led to consider a composite spectrum of two stars in a close binary system. It is not, therefore, a parameter as well quantified as a color index.

Let us recall the definition of the main spectral classes, designated by a letter followed by a number between 0 and 9, representing an evolution of the characteristics within a class. A small letter may follow indicating certain peculiarities of the spectral lines (emission lines, sharp or nebulous lines, etc.). The most frequent classes are as follows.

- O: Hot blue stars with strong helium HeII absorption lines and a strong ultraviolet continuum. Temperatures are above $3 0 0 0 0 \mathrm { K }$ .   
- B: Hot blue stars with HeI absorption lines and hydrogen appearing in the latest sub-classes (B5–B9). Temperatures range between 12 000 and $3 0 0 0 0 \mathrm { K }$ .   
- A: White stars with very strong hydrogen lines, and CaII lines appearing in the latest sub-classes. Temperatures are between 7500 and $1 2 0 0 0 \mathrm { K }$ .   
- F: White or yellowish stars with strong CaII lines, hydrogen lines are weaker, and other ionized metallic lines appear in the latest sub-classes. Temperatures range between 6000 and $7 5 0 0 \mathrm { K }$ .   
- G: In these yellow stars, the CaII lines are still strong, and many iron and other metallic ionized and neutral lines appear, while hydrogen lines become weak. Temperatures range between 5300 and $6 0 0 0 \mathrm { K }$ . The Sun is a G2 star.   
- K: Orange and reddish stars, with a large quantity of neutral metallic lines. Some CH and CN molecular bands are appearing. Temperatures are between 4000 and $5 3 0 0 \mathrm { K }$ .   
- M: Very red stars, with many molecular bands. Temperatures may be as low as 2500 K.

In addition, some special classes have been defined among very hot stars (Q, P, W), cold stars (S, R and N depending upon the presence of some molecules), and, at the extreme edge, brown dwarfs, which are visible essentially in the infrared.

There is another important classification derived from the spectra and from the knowledge of the absolute magnitudes, the luminosity class.

- I: Supergiants - II: Bright giants - III: Giants - IV: Sub-giants - V: Main sequence - VI: Sub-dwarfs - VII: White dwarfs.

Table 11.2. The relation between $B { - } V$ and the main spectral types   

<table><tr><td>Spectrum</td><td>B-V</td><td>Spectrum</td><td>B-V</td></tr><tr><td></td><td></td><td></td><td>0.60</td></tr><tr><td>05</td><td>-0.32</td><td>G0 G2</td><td>0.64</td></tr><tr><td>09</td><td>-0.31</td><td></td><td></td></tr><tr><td>BO</td><td>-0.30 -0.24</td><td>G5</td><td>0.68</td></tr><tr><td>B2</td><td></td><td>G8</td><td>0.72</td></tr><tr><td>B5</td><td>-0.16 -0.09</td><td>K0</td><td>0.81</td></tr><tr><td>B8</td><td></td><td>K2</td><td>0.92</td></tr><tr><td>A0</td><td>0.00</td><td>K3</td><td>0.98</td></tr><tr><td>A2</td><td>0.06</td><td>K5</td><td>1.15</td></tr><tr><td>A5</td><td>0.15</td><td>K7</td><td>1.30</td></tr><tr><td>A7</td><td>0.20</td><td>M0</td><td>1.41</td></tr><tr><td>FO</td><td>0.33</td><td>M1</td><td>1.48</td></tr><tr><td>F2</td><td>0.38</td><td>M3</td><td>1.55</td></tr><tr><td>F5</td><td>0.45</td><td>M5</td><td>1.61</td></tr><tr><td>F8</td><td>0.53</td><td>M8</td><td>2.00</td></tr></table>

The theory of stellar evolution shows how stars may move from one luminosity class to another depending upon their age, mass, metal content, etc. The mainsequence stars correspond to a stable situation, while the star is burning hydrogen in its core. The first four categories correspond to stars that have hotter cores, and are burning helium, or heavier elements like carbon or oxygen. They have a much larger atmosphere and are brighter than main sequence stars. Sub-dwarfs are metal-poor stars, and white dwarfs are in a degenerate state at the end of stars’ lives.

Generally, the spectral classes are not used as such in the reduction of astrometric observations or in determining the chromatic part of the refraction. One assumes that the star is a main-sequence star, and we give, in Table 11.2 the relation between $B { - } V$ and the main spectral types. This table may be interpolated, but one must have in mind that important biases may be introduced if the luminosity class is not V, especially for K, G, and F type stars, as shown in Fig. 11.7, and, even more so, in the case of composite spectra of double stars.

But this is not sufficient for very accurate astrometry. In the case of the measurements of centroids of images of stars on CCDs, the spectra are necessary to characterize the differences in point spread functions of the stars, and determine accurate relative positions of different types of stars.

# 11.5 Pre-Hipparcos star catalogs

In our presentation of star catalogs, a special emphasis is given to the Hipparcos Catalogue, because it is the basis of the realization of the celestial reference system in optical wavelengths and was the driving force in the adoption of the International Celestial Reference System (ICRS, see Section 7.1).

![](images/a2b775ba843ed8581316a5848b5524301c68261d294c392048b6416cf55a7c9b.jpg)  
Fig. 11.7. Correspondence between the color index $B { - } V$ and the absolute magnitude $M _ { V }$ , the spectral type and the luminosity class. (From Zombeck, M. V., 1990, Handbook of Space Astronomy and Astrophysics, 2nd Edn, p. 65. Reprinted with the permission of Cambridge University Press.)

The common characteristic of star catalogs before Hipparcos is that they gave positions and proper motions in the dynamic reference frame, which meant that they had to be referred to the equinox and the equator as defined by the dynamical frame. Generally a star catalog contains the position (right ascension and declination) in a specified reference system reduced at a common date, called epoch. When a catalog is built from many years of observations, it also contains the proper motions. But it generally does not include parallaxes or photometric data which are presented in specific catalogs.

Depending upon the way they are obtained, one may distinguish between observational catalogs, fundamental catalogs, and reference catalogs, even if in some cases catalogs may have some characteristics of two of these classes.

# 11.5.1 Observational catalogs

These contain the results of the observations by a given instrument during a certain interval of time. They may simply be a list of observed positions, but they are often published after some reduction, which transforms the observed positions into a set of coordinates in a specified reference system for the epoch of the observations. Two possibilities exist.

(i) Relative catalogs. Among the observed stars, there is a certain proportion of stars whose positions are taken from a catalog that is already given in the specified reference system, like a fundamental or a reference catalog. The positions of these reference stars are used to determine the instrumental parameters, like the plate constants in photographic or CCD astrometry, or the constants of a transit instrument (collimation, inclination, decentering, etc.). Correcting the raw observations of the other stars with the values found for these parameters, usually for a limited area of the sky, provides their coordinates in the system of the reference stars.   
(ii) Absolute catalogs. In these catalogs, the reduction to the reference system is made using observations of the Sun, planets, or minor planets, which allow us, by using a theory of their apparent motion in the reference system, to link the observed star positions to the equinox, the origin of the right ascensions, and to the equator, for the origin of declinations. Fundamental azimuth is also required. Actually, there were only a few meridian circles in the world that were able to observe the Sun, the planets, and stars, so that there were only a small number of absolute catalogs, which were the basis of the construction of a reference frame.

The construction of an observational absolute catalog is a lengthy and complex procedure. A detailed description may be found in chapter 17 of Woolard and Clemence (1966). The notion of absolute catalogs based upon the observation of the Sun has become obsolete with the new definition of the celestial reference system, ICRS, so we do not insist on this aspect of observational astrometry.

This is not the case of relative catalogs, which will now be the normal way to publish star-position observations. The methods are described in detail in Chapter 14. There is a very large number (several hundreds, possibly one thousand) of such catalogs built since the beginning of the nineteenth century. Each transit or meridian instrument in usage produced such a catalog, or list of observations, every few years. Many of them are quoted in Eichhorn (1974) who also gives references to existing lists of star catalogs prior to this date. Another source is the general index to the FK3, FK4 and FK5 catalogs.

# 11.5.2 Fundamental catalogs

A fundamental catalog is a catalog compiled from a large number of instrumental catalogs, in particular from all available absolute catalogs, to define the frame, and to build an ensemble of stellar positions and proper motions in the current reference system. It becomes the reference frame consistent, not only with the definition of the system (see Chapter 8), but also with the values of the fundamental astronomical constants that are adopted at that time (constants of precession, nutation, aberration, etc.). Again it is very complicated and lengthy work that was undertaken only rarely (every 20 years or so), and used to take about ten years of a team’s work. Since it has now become essentially a historical interest, we refer the reader to chapter 18 of Woolard and Clemence (1966). Two series of fundamental catalogs were built during the twentieth century by German and American astronomical institutes respectively.

The German series of fundamental catalogs was started in the nineteenth century by Auwers, who compiled the Fundamental Catalog for the Zone Observations for the Astronomisches Gesellschaft and included 539 Northern and 83 Southern stars. It was followed by the Neuer Fundamental Katalog (NFK, by J. Peters, 1907) in the beginning of the twentieth century and then by the FK3 (Kopff, 1937), the FK4 (Fricke et al., 1963) and finally the FK5 (Fricke et al., 1988). The FK4 was the last catalog based uniquely on a dynamical reference system (see Chapter 8). The system of right ascensions was based upon 45 absolute catalogs and the same constant of precession as FK3 (Gliese, 1963). It included 1535 stars. Later, a list of supplementary stars was added, the FK4 supplement. The basic FK5 catalog includes the FK4 stars, and was derived as a correction to the FK4 based upon 85 absolute and 90 observational catalogs. An FK5 extension, including 3117 stars, added differentially to the system, was later issued (Fricke et al., 1991). The FK5 system was obtained by applying a correction to the FK4 equinox (Fricke, 1982), the IAU expressions for general precession (Lieske et al., 1977), and a discussion of the galactic rotation effect on the proper motions. The consequence of this particular novelty is that, although referred to a dynamical system, the FK5 is not strictly based upon motions of the Sun and planets, and is, therefore, a mixed stellar–dynamical reference frame, a choice fully justified by the announced objective to stick as well as possible to the observations, among which the observations of the Sun and the planets were the weakest part.

The American series of fundamental catalogs was mostly compiled at the US Naval Observatory. It originated with the Catalogue of Fundamental Stars published by S. Newcomb in 1899, which contained the positions of 1257 stars for the years 1875.0 and 1900.0, without distinguishing proper motions from the effect of the luni-solar precession. The reference system was purely dynamical, based upon Newcomb’s theories of the motions in the Solar System. There was no direct connection between this catalog and its successors: the Preliminary General Catalogue (PGC) compiled by L. Boss in 1910 and the General Catalogue (GC) due to B. Boss et al. (1937), which comprised 33 342 star positions and proper motions. The latter were not very good, with uncertainties of the order of 20 mas/year. One of the reasons was that, for many of the stars, few earlier observations were available and thus, the accuracy of the catalog quickly degraded. For this reason, a less ambitious project based upon many newer observations, was undertaken and Morgan (1952) produced the N30 catalogue of 5268 stars from 60 observational and absolute catalogs. The reference system $\mathbf { N } =$ Normal System) was based on observations of the Sun, Moon and Planets for the position of the equinox and the equator. The catalog gives positions for the epoch 1950.0 and proper motions obtained generally using normal N30 positions and older GC positions. The N30 catalog is much more accurate than the GC, but the mean uncertainty of proper motions is of the order of 3–7 mas/year, still larger than the FK3, where there was a smaller number of stars, but each of them with a longer history of observations in both absolute and relative catalogs. This, together with the continuity of the FK series, led the IAU to adopt the latter as the basic reference for astrometric observations. A very detailed description of the principles on which all these fundamental catalogs (except FK5) were built can be found in Eichhorn (1974).

# 11.5.3 Positional reference catalogs

Fundamental catalogs provide the positions of only a few stars, and there is a need to have the coordinates of as many stars as possible with an acceptable precision. This need was recognized around 1880 and a worldwide project, called Carte du Ciel, was organized with the cooperation of 20 observatories equipped with two refractive telescopes mounted on a single tube.

The reference stars were obtained by observations with meridian circles. The photographs covered fields of $2 . 2 \times 2 . 2$ with corner to center overlapping each surrounding plate. Most of the sky was covered in 35 years, except a few missing zones that were re-observed later. The series of the plates, reproduced on paper, represent as such the so-called Carte du Ciel and are a record of the sky to about magnitude 14–15. In conjunction with the Carte du Ciel, the Astrographic Catalogue plates were taken. These sought to reach 11 th magnitude and the $x - y$ plate measurements were published. The measurements of the plates concerned on the average 200 stars. So, the coordinates of about 1.5 million stars were computed with an actual accuracy of the order of $1 ^ { \prime \prime }$ to $2 ^ { \prime \prime }$ . This accuracy was primarily the result of the accuracy of reference stars and the resulting plate constants. New measurements of plates and their reductions have been undertaken in several places; better computing facilities and measuring machines, together with better coordinates of reference stars derived from modern catalogs, have provided better first epoch coordinates for subsequent proper motion determinations (Sections 11.5.5 and 11.6.2).