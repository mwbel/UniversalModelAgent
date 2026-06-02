barycentre and itscoordinates referred to the ICRS,can be succinctly represented as

$$
\mathbf { u } _ { 4 } ( t ^ { \prime } ) = \mathbf { R } _ { 3 } ( - \beta ) \mathcal { R } _ { \Sigma } f [ g [ \mathbf { u } _ { \mathrm { B } } ( t - \tau ) - \mathbf { E } _ { \mathrm { B } } ( t ) ] ]
$$

where

<table><tr><td>t</td><td>istheepoch ofobservation,inthe TT timescale;</td></tr><tr><td>t</td><td>istheepoch ofobservation, in the TDB timescale;</td></tr><tr><td>T</td><td>isthelight-travel time fromtheplanet to theEarth,in theTDB</td></tr><tr><td>uB(t-τ)</td><td>timescale,for light arrivingat the epoch of observation t; is the barycentric position of the planet at epoch t-τ,</td></tr><tr><td>EB(t)</td><td>referred totheICRS; is the barycentric position of the Earth at the epoch of observation t, referredtotheICRS;</td></tr><tr><td>g[...]</td><td>is the function representing the gravitational deflection of light;</td></tr><tr><td>f[...]</td><td>is the function representing the aberration of light;</td></tr><tr><td>R</td><td>isthe transformation from the GCRS to the ofdate system that includes</td></tr><tr><td></td><td>frame bias,precession and nutation,and,where the origin of right ascension is the GCRS origin (Σ) on the true equator of date (see Fig.7.1);</td></tr><tr><td>R(-β)</td><td>isthe rotation about the CIP that positions the origin of right ascension and determinesthe paradigmchosen.Earth rotation (GASTorERA asappropriate)may be included givingcoordinatesreferred to the</td></tr><tr><td>u4(t&#x27;)</td><td>Terrestrial IntermediateReference System; is the apparent or intermediate geocentric place of the planet at the</td></tr></table>

This expression is schematic;the fullfunctional forms of $f$ and $g$ ,theelementsof $\mathcal { R } _ { \Sigma }$ ,the choice of $\beta$ and,thus,the paradigmas well as other auxiliary calculations are not indicated.

A detailed description of the algorithmdivided into numbered steps follows.Inplaces it is divided into two columns.The firstcolumn gives the traditional Equinox-based method where right ascension is measured from the equinox (true or mean as required)and thus GHA must beformed using Greenwich Sidereal Time,apparent (GAST)or mean (GMST),respectively. The second column gives the CIO-based method, which is theIAU recommended paradigm, where right ascension is measured from the CIO,and ERA must be used to calculate GHA.

1.Given an instant for which the position of the planet is required,obtain the dynamical time (TDB) to use with the ephemeris.If the position is required at a given Universal Time (UT1),or the hour angle is required,then obtain a value for $\Delta T$ ,which may have to be predicted.   
2.Calculate the geocentric rectangular coordinates of the planet from barycentric ephemerides of the planet and the Earth at coordinate time argument TDB,allowing for light-time calculated from heliocentric coordinates.

3.Calculate the geocentric direction of the planetbyallowing for light-deflection due to solar gravitation.

4.Calculate the proper direction of the planet by applying the correction for the Earth's orbital velocity about the barycentre (i.e.,annual aberration).The resulting position is in the GCRS.

# Equinox Method

# CIO Method

5.Rotate from the GCRS to the system definedby the true equator and equinox of date by applying rotations for frame bias,precession and nutation.

6. Convert to spherical coordinates,giving thegeocentricapparent right ascension and declination with respect to the true equinox and equator of date.

5 RotatefromtheGCRS to theCelestial Intermediate Reference System using the $( \mathcal { X } , \mathcal { Y } )$ of the CIP,and the CIO locator $s$ toapplyframe biasand precession-nutation.   
6 Convert to spherical coordinates,giving the geocentric intermediate right ascension and declination with respect to the CIO and equator of date.   
7 Calculate theEarth Rotation Angleand form the Greenwich Hour Angle for the given UT1.

7. Calculate Greenwich Apparent Sidereal Time and form the Greenwich Hour Angle for the given UT1.

Alternatively,if rightascension isnot required,combine Steps5nd7.

\*5. Apply frame bias,precession,nutation and Greenwich Apparent Sidereal Time to convert from the GCRS to the Terrestrial Intermediate Reference System;with origin of longitude at the TIO on the equator of date.

Rotate,using $\mathcal { X }$ , $y$ , $s$ and $\theta$ toapply frame bias, precession-nutation and Earthrotation,from the GCRS to the Terrestrial IntermediateReference System;with origin of longitude at the TIO on equator of date.

\*6. Convert to spherical coordinates,giving the Greenwich Hour Angle $( H )$ and declination (δ) with respect to the Terrestrial Intermediate Reference System(TIO and equator of date).

Note: In Steps 7and Steps $^ { * 5 }$ the effects of polar motion (see $\colon \ S \ 7 . 2 . 6 . 2$ and Chapter 6) have been ignored;they are the very small difference between the ITRS zero meridian and the TIO,and the position of the CIP within the ITRS.

# 7.4.1.1Relevant Time Arguments

Ascertain the instant,date and time,and timescale at which the position is required.From this time obtain the terrestrial time(TT)and the barycentric dynamical time (TDB).If the positionwilleventually be referred to theEarth,i.e.,via the TIOand hourangle,thenaUT1 timewill be required.

Step1.1.Express the instant (epoch) of observation $t ^ { \prime }$ asaTT Julian date.The terrestrial time is related to UT1 via the following relationship

$$
t ^ { \prime } = \mathrm { J D } + \mathrm { U T } 1 / 2 4 + { \Delta T } / { 8 6 4 0 0 }
$$

Where JD is the Julian date at $0 ^ { \mathrm { h } } \mathrm { T T }$ on the day,UT1 is time in hours,and $\Delta T = \mathrm { T A I } +$ 32184-UT1.UT1isaffectedbyunpredictable irregularities intheEarth's rotation,but itis

always within $0 . 9$ of UTC,the lattr defining civil time and broadcast worldwide according to international convention.These issues are discussed in detail in Chapter 3.

Step 1.2. Compute $T ^ { \prime }$ ,the number of Julian centuries in the TT timescale from J2Oo0.0 TT (JD 245 1545.0 TT).

$$
T ^ { \prime } = ( t ^ { \prime } - 2 4 5 1 5 4 5 . 0 ) / 3 6 5 2 5 .
$$

Step1.3.Compute the difference (in seconds) between the TT and TDB timescales,or equivalently $\mathrm { T _ { e p h } }$ of the JPL DE405/LE405 ephemeris,from

$$
\mathrm { T D B } - \mathrm { T T } = 0 . 0 0 1 6 5 7 \sin g + 0 . 0 0 0 0 2 2 \sin ( L - L _ { J } )
$$

and

$$
\begin{array} { r } { g = 3 5 7 \mathrm { ^ { \circ } . 5 3 } + 3 . 5 9 9 9 0 5 \times 1 0 ^ { 4 } T ^ { \prime } } \\ { L - L _ { J } = 2 4 6 \mathrm { ^ { \circ } . 1 1 } + 3 . 2 9 6 4 4 7 \times 1 0 ^ { 4 } T ^ { \prime } } \end{array}
$$

where $g$ isthemean anomaly of the Earth in itsorbitaround the Sun,and $L - L _ { J }$ is the difference in the mean ecliptic longitudes of the Sun and Jupiter (Simon et al.1994).Strictly the time argument in equations for $g$ and $L - L _ { J }$ should be TDB.Theabove formula for $\mathrm { T D B - T T }$ is accurate to about $\pm 3 0 \mu \mathrm { s }$ over the period 1980 to 2050,when compared to theFairhead and Bretagnon (199O) model adopted by IAU-SOFA (URL[3]).The difference between TDB and $\mathrm { T T }$ isoftenignored,since the two timescales differ by no more than 2 milliseconds.See Moyer(1981) for a complete discussion.

Next form the TDB,or equivalently the $\mathrm { T _ { e p h } }$ ,Julian date and fraction from

$$
t = t ^ { \prime } + ( \mathrm { T D B } - \mathrm { T T } ) / 8 6 4 0 0
$$

and

$$
T = ( t - 2 4 5 1 5 4 5 . 0 ) / 3 6 5 2 5 .
$$

The algorithm given above is much more precise than is required for the computation of apparent or intermediate places of most solar system bodiesand stars.For all solar system bodies,except the Moon and close approaching comets and asteroids,the approximation $t = t ^ { \prime }$ will lead to errors that may approach $0 . ^ { \prime \prime } 0 0 1$ in very unfavorable circumstances.For stellar places set $t = t ^ { \prime }$ with negligible error.

# 7.4.1.2 Ephemeris Data for Earth,Sunand Planet

Obtain the appropriate ephemeris data for time $t$ and at the light-time $t - \tau$

Astandard ephemeris for the major bodies in the solar system is the Jet Propulsion Laboratory(JPL)ephemeris designatedDE405/LE405(Standish1998a)the reference system of which is the ICRS (see Chapter 8).The positions of the Sun,Moon and planets given in The Astronomical Almanac and several other international almanacs are now obtained from this ephemeris.Aset of analytical planetary theories fited to DE2oo has been developed by Bretagnon(1982).IAUCommission4website(URL[4])lists various sources ofephemerides.

Step 2.1.Extract from the appropriate ephemeris,for the time $t$ ,the barycentric position of the planet, ${ \bf u } _ { \mathrm { B } } ( t )$ ,the barycentric position and velocity of the Earth, ${ \bf E } _ { \mathrm { B } } ( t )$ and $\dot { \mathbf { E } } _ { \mathrm { B } } ( t )$ ,and the barycentric position of the Sun, ${ \bf S } _ { \mathrm { B } } ( t )$ ,all referred to the ICRS.All position vectors are assumed to be inau and velocity vectors inau/day.

The barycentric position of the Earth is used to form the geocentric position of the body (see $\ S \ 7 . 4 . 1 . 3 )$ ;the barycentric velocity of the Earth is used in theaberration computation (see $\ S \ 7 . 4 . 1 . 5 )$ ；and the heliocentric position of the Earth is used in the computation of the relativistic gravitational deflection of light (see $\ S \ 7 . 4 . 1 . 4$ ).Values of the componentsof the vectors $\mathbf { E } _ { \mathrm { B } }$ , $\dot { \bf E } _ { \mathrm { B } }$ and $- \mathbf { E } _ { \mathrm { H } }$ at1-day intervalsare tabulatedin TheAstronomical Almanac.

Step 2.2.Calculate the heliocentric position of the Earth.

$$
\mathbf { E } _ { \mathrm { H } } ( t ) = \mathbf { E } _ { \mathrm { B } } ( t ) - \mathbf { S } _ { \mathrm { B } } ( t ) .
$$

Note that the barycentric position of the Earth is that of the centre of mass of the Earth and not that of the Earth-Moon barycentre.

7.4.1.3Geometric Positionof Planet,Accounting for Light-Time

Step 2.3.Compute the geometric distance between Earth and planet,i.e.,compute $^ d$ ,the geometric distance between the positions of the centres of mass of the planet and the Earth at time $t$ ,inau,from

$$
\begin{array} { r } { d = | \mathbf { u } _ { \mathrm { B } } ( t ) - \mathbf { E } _ { \mathrm { B } } ( t ) | . } \end{array}
$$

Thegeometric distance is the quantity tabulated in The Astronomical Almanacas the“true distance”of solar system bodies.Using $d$ compute $\tau$ ,afirst approximation to the light-travel time between the planet and the Earth

$$
\tau = d / c
$$

where $c$ is the speed of light expressed in au/day; its precise value may be computed from

$$
c = 8 6 4 0 0 / \tau _ { A } = 8 6 4 0 0 / 4 9 9 . 0 0 4 7 8 3 8 0 6 1
$$

where $\tau _ { A }$ is the light-time for unit distance (1 au).The value given is that specified by the JPL DE405/LE405 ephemeris where the units are compatible with TDB.

Step 2.4.Extract from the ephemeris,for the time $t - \tau$ ,the barycentric position of the planet and the Sun, ${ \bf u } _ { \mathrm { B } } ( t - \tau )$ and $\mathbf { S } _ { \mathrm { B } } ( t - \tau )$ ,respectively.

Step 2.5. Calculate $\mathbf { U }$ and $\mathbf { Q }$ approximations to the geocentric and heliocentric position of the centre of mass of the planet,respectively,at the epoch of observation $t$ ,from

$$
\begin{array} { r l } & { \mathbf { U } = \mathbf { u } _ { \mathrm { B } } ( t - \tau ) - \mathbf { E } _ { \mathrm { B } } ( t ) } \\ & { \mathbf { Q } = \mathbf { u } _ { \mathrm { B } } ( t - \tau ) - \mathbf { S } _ { \mathrm { B } } ( t - \tau ) . } \end{array}
$$

Step 2.6. Nextcompute $\tau ^ { \prime }$ ,abetterapproximationto the light-traveltime between the planet and the Earth from

$$
c \tau ^ { \prime } = U + ( 2 \mu / c ^ { 2 } ) \ln { \frac { E + U + Q } { E - U + Q } }
$$

where $\tau ^ { \prime }$ includes the effect of gravitational retardation due to the Sun. $U = | \mathbf { U } |$ , $E = | \mathbf { E } _ { \mathrm { H } } |$ $Q = | \mathbf { Q } |$ .The heliocentric gravitational constant $\mu$ and the velocity of light $c$ may be rewritten as

$$
{ \begin{array} { r l } & { \mu / c ^ { 2 } = k ^ { 2 } \tau _ { A } ^ { 2 } / 8 6 4 0 0 ^ { 2 } } \\ & { \qquad = 0 . 0 1 7 2 0 2 0 9 8 9 5 ^ { 2 } \times ( 4 9 9 . 0 0 4 7 8 3 8 0 6 1 / 8 6 4 0 0 ) ^ { 2 } } \\ & { \qquad = 9 . 8 7 0 6 \times 1 0 ^ { - 9 } } \end{array} }
$$

where $k$ is the Gaussian gravitational constant and $\tau _ { A }$ is the light-time for unit distance (Eq.7.107 in Step 2.3) where DE405/LE405 and TDB compatible values are given.

Compare $\tau ^ { \prime }$ with $\tau$ ;if they are identical within some smalltolerance continue to Step 2.7. If they are not,then replace the value of $\tau$ with the value of $\tau ^ { \prime }$ and repeat Step 2.4 through Step 2.6 until the light-time converges to within the tolerance permitted.Since the speed of bodies in the solar system is small compared to the speed of light,this process converges rapidly.

The tolerance permitted depends on the precision desired in the final coordinates and the apparent angular speed of the body as viewed from Earth.The most rapidly moving objects in the sky are the Moon (angular rate $\approx 0 . 7 5$ per second),Mercury (angular rateat inferior conjunction $0 { : } ^ { \prime \prime } 0 5$ per second),and the Sun (angular rate $0 . { } ^ { \prime \prime } 0 4$ per second).However, occasionally an Earth-crossing asteroid or comet may exceed these rates for short periods of time. Fora computational precision of one milliarcsecond,therefore,the light-time convergence tolerance must be $0 \mathrm { { s } } 0 0 2 = 2 \times 1 0 ^ { - 8 }$ days orless;we suggest $1 \times 1 0 ^ { - 8 }$ days.For the Moon, TheAstronomical Almanac uses the convergence criteriathatthe change in time between two iterations must not cause the distance $d$ to change by more than $1 \times 1 0 ^ { - 1 0 }$ au.

Kaplan et al.(1989) ignores the second term in Eq 7.110,(order1 micro-arcsecond), whichis due to the relativistic delay caused by the Sun's gravitational feld.

Step 2.7. Once $\tau$ has converged,form the geocentricand heliocentric positions of the body at time $t - \tau$ ,respectively from

$$
\begin{array} { l } { \mathbf { U } = \mathbf { u } _ { \mathrm { B } } ( t - \tau ) - \mathbf { E } _ { \mathrm { B } } ( t ) } \\ { \mathrm { a n d } ~ \mathbf { Q } = \mathbf { u } _ { \mathrm { B } } ( t - \tau ) - \mathbf { S } _ { \mathrm { B } } ( t - \tau ) . } \end{array}
$$

7.4.1.4Relativistic Deflection of Light

Calculate light-deflection due to solar gravitation.A detailed explanation on light-deflection is given in $\ S 7 . 2 . 4$

Step 3.1.First form the following unit vectors and dimensionless scalar quantities

$$
\begin{array} { l r } { \mathbf { u } = \mathbf { U } / | \mathbf { U } | \qquad \mathbf { q } = \mathbf { Q } / | \mathbf { Q } | \qquad \mathbf { e } = \mathbf { E } _ { \mathrm { H } } / | \mathbf { E } _ { \mathrm { H } } | } \\ { g _ { 1 } = { \frac { 2 \mu } { c ^ { 2 } E } } \qquad g _ { 2 } = 1 + ( \mathbf { q } \cdot \mathbf { e } ) } \end{array}
$$

where the constants $\mu$ and $c$ are given in Step 2.6Eq.7.111,and $\mathbf { E } _ { \mathrm { H } }$ is given in Step 2.2 Eq.7.104.

Step 3.2.The deflected position of the body relative to the geocentric inertial frame that is instantaneously stationary in the space time reference frame of the solar system is then

$$
\mathbf { u } _ { 1 } = | \mathbf { U } | \left( \mathbf { u } + \frac { g _ { 1 } } { g _ { 2 } } \left[ ( \mathbf { u } \cdot \mathbf { q } ) \mathbf { e } - ( \mathbf { e } \cdot \mathbf { u } ) \mathbf { q } \right] \right) .
$$

The vector ${ \bf u } _ { 1 } / | \mathbf { U } |$ is a unit vector to order $\mu / c ^ { 2 }$

For the Sun or bodies lying behind the Sun on the Sun-Earth line,the light-deflection can be considered zero,so that $\mathbf { u } _ { 1 } = \mathbf { U }$

# 7.4.1.5 Aberration of Light

Calculate the proper directionof the planet by applying the correction for the Earth'sorbital velocity about the barycentre.A detailed explanation on aberration is given in $\ S 7 . 2 . 3 . 2$ .

Step 4.1.Form the following quantities

$$
\begin{array} { c } { { \bf u = u _ { \mathrm { 1 } } / | { \bf u } _ { \mathrm { 1 } } | \qquad { \bf V } = \dot { \bf E } _ { \mathrm { B } } ( t ) / c } } \\ { { \beta ^ { - 1 } = \sqrt { 1 - V ^ { 2 } } \qquad f _ { \mathrm { 1 } } = ( { \bf u } \cdot { \bf V } ) \qquad f _ { \mathrm { 2 } } = 1 + f _ { \mathrm { 1 } } / ( 1 + \beta ^ { - 1 } ) } } \end{array}
$$

where the velocity $( \mathbf { V } )$ is expressed in units of the velocity of light and is equal to the Earth's velocity in the barycentric frame.

Step 4.2.The aberrated position of the body in the geocentric inertial frame that is moving with instantaneous velocity $( \mathbf { V } )$ of the Earth relative to the natural frame is then given by the vector

$$
\mathbf { u } _ { 2 } = ( \beta ^ { - 1 } \mathbf { u } _ { 1 } + f _ { 2 } | \mathbf { u } _ { 1 } | \mathbf { V } ) / ( 1 + f _ { 1 } ) .
$$

The above algorithm includes relativistic terms (Murray 1981) (see $\ S 7 . 2 . 3 . 2 )$ ,whichare of the order1 milliarcsecond.Therefore,for many applications the much simpler classical formula maybeused

$$
\mathbf { u } _ { 2 } = \mathbf { u } _ { 1 } + | \mathbf { u } _ { 1 } | \mathbf { V } .
$$

# 7.4.1.6 Transformation to "Of Date"Positions

Rotate the resulting coordinate system,the GCRS,to the coordinate system of date by including the effects of frame bias,precession and nutation.These effects,and the various algorithms by which the matrices may be calculated are given in $\ S 7 . 2 . 5$ and described indetail in Chapter6.The combined bias-precesson-nutation matrices, $\mathbf { M }$ and C,for equinox-based andCIO-basedparadigms,respectively,aretabulateddailyat $0 ^ { \mathrm { h } } \mathrm { T T }$ inTheAstronomical Almanac and must be interpolated to the epoch of observation.

Equinox Method

CIO Method

Step 5.

The apparent position vector ${ \bf u } _ { 3 }$ is given by

The intermediate position vector $\mathbf { u } _ { 3 }$ is given by

$$
\begin{array} { c } { { \mathbf { u } _ { 3 } = { \mathbf { R } } _ { 3 } ( - s + E _ { o } ) \ \mathcal { R } _ { \Sigma } \ \mathbf { u } _ { 2 } } } \\ { { { } } } \\ { { { } = { \mathbf { M } } \ \mathbf { u } _ { 2 } = { \mathbf { N P B } } \ \mathbf { u } _ { 2 } } } \end{array}
$$

$$
\begin{array} { c } { \mathbf { u } _ { 3 } = \mathbf { R } _ { 3 } ( - s ) \ \mathbf { \mathcal { R } } _ { \Sigma } \mathbf { u } _ { 2 } } \\ { \mathbf { \qquad } = \mathbf { C } \mathbf { u } _ { 2 } } \end{array}
$$

where $\mathbf { M }$ is given in $\ S 7 . 2 . 5 . 1$ .

where $\mathbf { C }$ is given in $\ S 7 . 2 . 5 . 2$

Step 6.Convert to spherical coordinates; apparent rightascensionand declination $\alpha _ { e }$ ， $\delta$ using:

Convert to spherical coordinates; intermediaterightascensionand declination $\alpha _ { i }$ , $\delta$ using:

$$
\begin{array} { c } { { \alpha _ { e } = \tan ^ { - 1 } \displaystyle \frac { \eta } { \xi } } } \\ { { \delta = \tan ^ { - 1 } \displaystyle \frac { \zeta } { \sqrt { \xi ^ { 2 } + \eta ^ { 2 } } } } } \end{array}
$$

$$
\begin{array} { c } { { \alpha _ { i } = \displaystyle \tan ^ { - 1 } \frac { \eta } { \xi } } } \\ { { \delta = \displaystyle \tan ^ { - 1 } \frac { \xi } { \sqrt { \xi ^ { 2 } + \eta ^ { 2 } } } } } \end{array}
$$

where ${ \bf u } _ { 3 } = ( \xi , \eta , \zeta )$ .The quadrant of $\alpha _ { e } , \ \alpha _ { i }$ is determined by the signs of $\xi$ and $\eta$

# 7.4.1.7 Position Relative to the Earth

Relate the celestial position to the TIO so that hour angle may be calculated.

Step 7.Calculate GAST for the required UT1 and then form

Calculate the ERA $\left( \theta \right)$ for the required UT1 and then form

$$
H = \mathrm { G A S T } - \alpha _ { e } .
$$

$$
H = \theta - \alpha _ { i } .
$$

Note: $H$ is usually given in arc measure,while GAST and right ascension are given in units of time.

Note: $H$ and $\theta$ are usually given in arcmeasure,while right ascension is given in units of time.

Alternatively combining Steps5and7before forming sphericalcoordinates

# Step ${ \mathfrak { s } } ^ { * }$

The position $\mathbf { \Pi } ( \mathbf { u } _ { 4 } )$ relative to the Terrestrial IntermediateReference System is given by

The position $\mathbf { \Pi } ( \mathbf { u } _ { 4 } )$ relative to the Terrestrial IntermediateReference System is given by

$$
\begin{array} { r } { \mathbf { u } _ { 4 } = \mathbf { R } _ { 3 } ( \mathrm { G A S T } - s + E _ { o } ) \mathcal { R } _ { \Sigma } \mathbf { u } _ { 2 } } \\ { = \mathbf { R } _ { 3 } ( \mathrm { G A S T } ) \mathbf { M } \mathbf { u } _ { 2 } } \end{array}
$$

$$
\begin{array} { r } { \mathbf { u } _ { 4 } = \mathbf { R } _ { 3 } ( \theta - s ) \mathbf { \mathcal { R } } _ { \Sigma } \mathbf { u } _ { 2 } } \\ { = \mathbf { R } _ { 3 } ( \theta ) \mathbf { C } \mathbf { u } _ { 2 } \quad \mathrm { ( ) } } \end{array}
$$

where $\mathbf { M }$ is given in $\ S 7 . 2 . 5 . 1$ and $\ S \ 7 . 2 . 6 . 1$ .

where $\mathbf { c }$ is given in $\ S 7 . 2 . 5 . 2$ and $\ S \ 7 . 2 . 6 . 1$ .

Step ${ \mathfrak { 6 } } ^ { * }$ ，Convert to spherical coordinates Greenwich Hour Angle $( H )$ and declination $\delta$ using:

$$
H = \tan ^ { - 1 } \frac { - \eta } { \xi } , \qquad \delta = \tan ^ { - 1 } \frac { \xi } { \sqrt { \xi ^ { 2 } + \eta ^ { 2 } } }
$$

where ${ \bf u } _ { 4 } = ( \xi , \eta , \zeta )$ ,and $H$ is measured from the TIO meridian positive to the west,and thequadrantisdetermined bythesignsof $\xi$ and $- \eta$ .

# 7.4.2Apparent and Intermediate Place Algorithm for Stars

The algorithm used to compute the apparent or intermediate place of a star or star-like object at the instant of observation $t ^ { \prime }$ ,given its right ascension,declination and proper motion,and other data (as available) at some catalogue or reference epoch $t _ { 0 }$ with respect to the ICRS, may be succinctly represented as:

$$
\mathbf { u } _ { 4 } ( t ^ { \prime } ) = \mathbf { R } _ { 3 } ( - \beta ) \mathcal { R } _ { \Sigma } f [ g [ \mathbf { u } _ { \mathrm { B } } ( t _ { 0 } ) + ( t - t _ { 0 } ) \dot { \mathbf { u } } _ { \mathrm { B } } ( t _ { 0 } ) - \mathbf { E } _ { \mathrm { B } } ( t ) ] ]
$$

where

$t ^ { \prime }$ isthe epoch of observation,in the TT timescale;   
$t$ istheepoch of observation, in the TDB timescale;   
$t _ { 0 }$ isthereference epoch of the catalogue,in the TDB timescale;   
${ \bf u } _ { \mathrm { B } } ( t _ { 0 } )$ is the catalog place of the star at the reference epoch $t _ { 0 }$ ,represented asa3-dimensional position vector inau; origin,solar system barycentre,and coordinatesreferred to theICRS;   
$\dot { { \bf u } } _ { \mathrm { B } } ( t _ { 0 } )$ is the space motion vector (in au/day) of the star at the reference epoch $t _ { 0 }$ ,obtained from the catalog proper motions,parallax and radial velocity;   
$\mathbf { E _ { \mathrm { B } } }$ isthe barycentric position of the Earth at the epoch of observation $t$ ,referred to the ICRS;   
$g [ \ldots ]$ is the function representing the gravitational deflection of light;   
$f [ . . . ]$ is the function representing the aberration of light;   
$\mathcal { R } _ { \Sigma }$ isthe transformation from the GCRS to the“of date”system that includes frame bias, precessionand nutation,and,where the origin of right ascensionis the GCRSorigin $\Sigma$ ) on the true equator of date(seeFig.7.1);   
${ \bf R } _ { 3 } ( - \beta )$ is the rotation about the CIP that positions the origin of right ascension and determines theparadigmchosen.Earth rotation(GASTorERAasappropriate)maybe included giving coordinates referred to the Terrestrial IntermediateReference System;   
${ \bf u } _ { 4 } ( t ^ { \prime } )$ istheapparent or intermediate geocentricplace of the starat the epoch of observation $t ^ { \prime }$ represented asa 3-dimensional position vector $( \xi , \eta , \zeta )$

The above expression is similar toEq.7.98 for planets.Most of the algorithm is identical. The main modifications to the planetary reduction in the stellar case are:

(a) the distinction between TDB and TT is not significant;   
(b)the more complex motion of a planet compared to that of a star. In $\ S ~ 7 . 4 . 1 . 2$ and $\ S \ 7 . 4 . 1 . 3$ wehad to obtain the position of the planet from an ephemerisand deal with the light-time problem explicitly;in this section we will assume uniform rectilinear motion for the star and neglect variations in light-time as the star moves,although this is discussed in $\ S 7 . 2 . 1$   
(c)the relativity term for light-deflection is modified to the asymptotic case where the star is assumed to be at infinity.

If the catalogue position of the star is not with respect to the ICRS,and the accuracy of the data warrants it,then transform it to the ICRS.See Chapter 4 for theFK5 to ICRS,and other conversions.

The steps in the stellar reduction are as follows:

# 7.4.2.1Relevant Time Arguments

Step 1.Follow Steps 1.1 through 1.3 in $\ S \ 7 . 4 . 1 . 1$ ,orset $\mathrm { T D B } = \mathrm { T T }$ ,i.e.,set $t = t ^ { \prime }$ as appropriate.

7.4.2.2EphemerisDataforEarth,SunandStar Obtain at time $t$ the appropriate ephemeris data.

Step2.1.Extract fromaplanetaryephemeris,forthe time $t$ ,the barycentric position and velocity of the Earth, ${ \bf E } _ { \mathrm { B } } ( t )$ and $\dot { \mathbf { E } } _ { \mathrm { B } } ( t )$ and the barycentric position of the Sun, ${ \bf S } _ { \mathrm { B } } ( t )$ ,all referred to the ICRS.All position vectors are assumed to be in au and velocity vectors in au/day.

Step 2.2.Calculate the heliocentric position of the Earth ( $\mathbf { E } _ { \mathrm { H } } )$ from

$$
\mathbf { E } _ { \mathrm { H } } ( t ) = \mathbf { E } _ { \mathrm { B } } ( t ) - \mathbf { S } _ { \mathrm { B } } ( t ) .
$$

Forapparent places of stars accurate toafew milliarcseconds it is necessary only to obtain the Earth and Sun's position components to three significant digits and the Earth's velocity components to five significant digits.Itis,therefore,feasible to construct relatively compact closed-form algorithmswhich provide the required data (Stumpff 198ob).The NOVAS software (Kaplan etal.2OO9;URL[2]) of theNautical Almanac Office of USNO contains routines that evaluates the barycentric position and velocity of the Earth,without using external files.Similarly,the IAU-SOFAroutine EPVoO (URL[3]) usesasimplified solution from the VSOP planetary theory by Moisson and Bretagnon (2Oo1) to evaluate the Earth's barycentric and heliocentric positions and velocities.However,for the highest precision,or when the apparent places of planets are being computed,more complex algorithms or external files are required.

Step 2.3.For the selected star extract from the given catalogue its position (α,δ),at some reference epoch $t _ { 0 }$ ,together with $\mu _ { \alpha }$ and $\mu _ { \delta }$ ,the corresponding proper motion components, as well as the parallax $\pi$ and radial velocity $\dot { r }$ in $\mathrm { k m } / \mathrm { s }$ .Forthisparticularalgorithm,it is assumed that the reference system of the catalogue is the ICRS,if not,then the catalogue datamust be transformed to the ICRS.

Step 2.4.Form the barycentric position vector, ${ \bf u } _ { \mathrm { B } } ( t _ { 0 } )$ (in au),and space motion vector, $\dot { \bf u } _ { \mathrm { B } } ( t _ { 0 } )$ (au/day). In particular use Eq.7.2O to form ${ \bf u } _ { \mathrm { B } } ( t _ { 0 } )$ and either of Eqs.7.22 or 7.24 to calculate the space motion vector $\dot { \bf u } _ { \mathrm { B } } ( t _ { 0 } )$ depending on the form and units of the proper motions.Detailed information on space motion is discussed in $\ S 7 . 2 . 1$ .

Step 2.5.Compute the barycentric position of the star,at the epoch of observation $( t$ ,by adding the distance moved during the interval of time between the catalog epoch $\left( t _ { 0 } \right)$ and the epoch of observation

$$
\begin{array} { r } { { \bf u } _ { \mathrm { B } } ( t ) = { \bf u } _ { \mathrm { B } } ( t _ { 0 } ) + \left( t - t _ { 0 } \right) \dot { \bf u } _ { \mathrm { B } } ( t _ { 0 } ) . } \end{array}
$$

The assumption is made here and in The Astronomical Almanac that there is no explicit correction for light-time in these stellar computations,however this is discussed in $\ S 7 . 2 . 1$

# 7.4.2.3 Geocentric Position of the Star

Step 2.6.Calculate U,the geocentric vector of the star at the required epoch,from

$$
\mathbf { U } = \mathbf { u } _ { \mathrm { B } } ( t ) - \pi \mathbf { \Gamma } \mathbf { E } _ { \mathrm { B } } ( t ) .
$$

# 7.4.2.4Relativistic Deflection of Light

Calculate light-deflection due to solar gravitation.Adetailed explanation on light-deflection is given in $\ S 7 . 2 . 4$

Step 3.First form the heliocentric position of the star

$$
{ \bf Q } = { \bf u } _ { \mathrm { B } } ( t ) - { \bf S } _ { \mathrm { B } } ( t )
$$

which is then used in $\ S \ 7 . 4 . 1 . 4$ Steps 3.1 and 3.2 to obtain the star's geocentric position, corrected forlight-deflection $\mathbf { u } _ { 1 }$

Note that Step 3.2 may be simplified (see $\ S 7 . 2 . 4$ ,Eq.7.65)by substituting $\mathbf q = \mathbf u$ as stars represent the asymptotic case.

# 7.4.2.5Aberration of Light

Follow Steps 4 for aberration of light in $\ S \ 7 . 4 . 1 . 5$ .

# 7.4.2.6The"Of Date"Positions

Follow the Steps in $\ S 7 . 4 . 1 . 6$ or $\ S 7 . 4 . 1 . 7$ as required.

# 7.4.3Topocentric Place Algorithm

The topocentric place of a star or planet refers to its apparent direction as it would actually be observed from some place on Earth,neglecting atmospheric refraction.The apparent and intermediateplaces,developed in $\ S ~ 7 . 4 . 1$ and $\ S \ 7 . 4 . 2$ ,canbethought of as theposition ofan object for a fictitious observer locatedat the centre of a transparent non-refracting Earth.The only difference between these places and a topocentric place is due to the slightly different position and velocity of an observer on the Earth's surface compared with those of thefictitious observer at the Earth's centre.The change in direction of the observed body due tothedifference of position,is referred toas geocentric parallax (or diurnal parallax),and is significant only for objects in the solar system.It is typicallya few arcseconds for most solar system bodies,but reaches about $1 ^ { \circ }$ for the Moon.The change in direction due to the difference in velocity,(due to the rotationof the Earth) is referred toas diurnal aberration, andisindependent of thedistance of the observed body,and itisalways less than $0 ^ { \prime \prime } 3 2$

Atmospheric refraction also affects the apparent direction of celestial objects.In fact, refraction at all wavelengths is orders of magnitude larger than either geocentric parallax or diurnal aberration.Refraction is discussed in $\ S \ 7 . 2 . 7$ ,andas it isusuallyconsidered a correction to observations rather than an effect to be taken into account when computing a topocentricplace,it isnot considered here.

The simplest way of computing a topocentric place is to compute an apparent or intermediate place using the position and velocity vectors of the observer rather than the centre of mass of the Earth.That is,modifythe barycentric vectors ${ \bf E } _ { \mathrm { B } } ( t )$ and $\dot { \mathbf { E } } _ { \mathrm { B } } ( t )$ byadding the positionand velocityof the observer relative to the centre of the Earth,ensuring that the latteris transformed to the reference systemof the former,see Steps5and 6 in $\ S 7 . 4 . 3 . 4$ and $\ S 7 . 4 . 3 . 5$ ,respectively.This procedure is equally applicable to stars and solarsystem objects. The development that follows requires quantities related to precession and nutation that, in thecomputation of geocentric apparent or intermediate places,are not needed before Step 5 in $\ S \ 7 . 4 . 1 . 6$ .These quantities should be computed,used here,and saved for later use; they are specifically noted as they arise.

# 7.4.3.1 Universal Timeof the Observation

Step1.Determine the Universal Time of observation,specifically,the epoch of observation in the UT1 timescale.UT1is affected by unpredictable irregularities in the Earth's rotation, butisalwayswithin O9 of UTC,the latter defining civil timeand broadcast worldwide according to international convention. The difference $\Delta \mathrm { U T } = \mathrm { U T 1 } - \mathrm { U T C }$ is determined and distributedby the IERS (URL[5]).The predicted value of $\Delta \mathrm { U T }$ to within O:1(denoted DUT1) is also coded into UTC broadcasts (see $\ S 3 . 2 . 2$ , $\ S \ 3 . 5 . 1$ ,and $\ S \ 3 . 1 0 . 1 $

# 7.4.3.2 Terrestrial Coordinatesof the Observer

There are three commonly used ways of expressing terrestrial (i.e.,Earth-fixed) coordinates:

1．geocentric equatorial rectangular coordinates, $x$ ,y,z;   
2.geocentric longitude,latitude and distance,λ, $\phi ^ { \prime } , \rho$ ;   
3.geodetic longitude,latitude and height,λ, $\phi , h$ .

Geodetic coordinates are referred to a reference spheroid (an ellipse of revolution),which isnormally geocentric,and is defined by itsequatorial radius $( a )$ and flattening $( f )$ .For example,those of the 2010 Conventions (IERS 2010) are

$$
a = 6 3 7 8 1 3 6 . 6 \mathrm { m } \quad \mathrm { a n d } \quad f = 1 / 2 9 8 . 2 5 6 4 2 .
$$

The geodetic and geocentric longitudes of a point are the same.The following relationships hold between the geocentric and geodetic (geographic) coordinates:

$$
\mathbf { r } = { \left[ \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right] } = { \left[ \begin{array} { l } { \rho \cos \phi ^ { \prime } \cos \lambda } \\ { \rho \cos \phi ^ { \prime } \sin \lambda } \\ { \rho \sin \phi ^ { \prime } } \end{array} \right] } = { \left[ \begin{array} { l } { ( a C + h ) \cos \phi \cos \lambda } \\ { ( a C + h ) \cos \phi \sin \lambda } \\ { ( a S + h ) \sin \phi } \end{array} \right] }
$$

where $a$ is the equatorial radius of the spheroid and $C$ and $S$ areauxiliary functions that depend on the geodetic latitude and the flattening $f$ of the reference spheroid(see Eqs.7.130). It follows from the properties of the ellipse that

$$
C = ( \cos ^ { 2 } \phi + ( 1 - f ) ^ { 2 } \sin ^ { 2 } \phi ) ^ { - 1 / 2 } \qquad S = ( 1 - f ) ^ { 2 } C .
$$

Geocentric coordinates may be calculated directly from geodetic coordinates and conversely.It is easier to use an iterative procedure for the inverse calculation (see Chapter 5, $\ S 5 . 2 . 4 )$ .Series expansions,which contain terms up to $f ^ { 3 }$ ,for $S$ , $C$ , $\rho$ and $\phi - \phi ^ { \prime }$ are:

$$
\begin{array} { r l } & { S = 1 - \displaystyle \frac { 3 } { 2 } f + \frac { 5 } { 1 6 } f ^ { 2 } + \frac { 3 } { 3 2 } f ^ { 3 } - \bigl ( \frac { 1 } { 2 } f - \frac { 1 } { 2 } f ^ { 2 } - \frac { 5 } { 6 4 } f ^ { 3 } \bigr ) \cos 2 \phi } \\ & { \qquad + \bigl ( \frac { 3 } { 1 6 } f ^ { 2 } - \frac { 3 } { 3 2 } f ^ { 3 } \bigr ) \cos 4 \phi - \frac { 5 } { 6 4 } f ^ { 3 } \cos 6 \phi } \\ & { C = 1 + \displaystyle \frac { 1 } { 2 } f + \frac { 5 } { 1 6 } f ^ { 2 } + \frac { 7 } { 3 2 } f ^ { 3 } - \bigl ( \frac { 1 } { 2 } f + \frac { 1 } { 2 } f ^ { 2 } + \frac { 2 7 } { 6 4 } f ^ { 3 } \bigr ) \cos 2 \phi } \\ & { \qquad + \bigl ( \frac { 3 } { 1 6 } f ^ { 2 } + \frac { 9 } { 3 2 } f ^ { 3 } \bigr ) \cos 4 \phi - \frac { 5 } { 6 4 } f ^ { 3 } \cos 6 \phi } \end{array}
$$

$$
\begin{array} { c } { { \rho = 1 - \displaystyle \frac 1 2 f + \frac 5 { 1 6 } f ^ { 2 } + \frac 5 { 3 2 } f ^ { 3 } + \big ( \frac 1 2 f - \frac { 1 3 } { 6 4 } f ^ { 3 } \big ) \cos 2 \phi } } \\ { { \mathrm { } } } \\ { { - \big ( \frac 5 { 1 6 } f ^ { 2 } + \frac 5 { 3 2 } f ^ { 3 } \big ) \cos 4 \phi + \frac { 1 3 } { 6 4 } f ^ { 3 } \cos 6 \phi } } \\ { { \phi - \phi ^ { \prime } = \big ( f + \frac 1 2 f ^ { 2 } \big ) \sin 2 \phi - \big ( \frac 1 2 f ^ { 2 } + \frac 1 2 f ^ { 3 } \big ) \sin 4 \phi + \frac 1 3 f ^ { 3 } \sin 6 \phi . } } \end{array}
$$

The expressions for $\rho$ and $\phi - \phi ^ { \prime }$ are for points on the spheroid( $h = 0$ ),andthe latterquantity is sometimes known as the“reduction in latitude”or“the angleof the vertical”,and it is of order $1 0 ^ { \prime }$ in mid-latitudes.To a first approximation when $h$ is small, the geocentric radius is increased by $h / a$ and the angle of the vertical is unchanged.The height $h$ refers toa height above the reference spheroid and differs from the height above mean sea level (i.e.,above the geoid)by the“undulation of the geoid’at thepoint.

Step 2.Obtain $\mathbf { r }$ (in meters)the position vector of the observerin an Earth-fixed, geocentric, right-handed coordinate system,with the $x y$ -plane the Earth'sequator,the $x z$ -plane the ITRS meridian,and the $Z$ -axispointed towardsthe north terrestrial pole.In termsof theobserver's geodetic latitude $\phi$ ,longitude $\lambda$ (eastlongitudespositive）and height $h$ above the Earth's reference ellipsoid,[for most purposes the height above mean sea level (the regional geoid) can be used], $\mathbf { r }$ isgivenbyEq.7.131 and the latestvalues for $a$ and $f$ may be found in SectionKof The Astronomical Almanac.

# 7.4.3.3 Geocentric Position and Velocity of the Observer

Step 3.Compute the geocentric position and velocity of the observer,with respect to the celestial of date reference system,in meters,and meters/second,respectively,from

$$
\begin{array} { r l } & { \mathbf { g } ( t ) = \mathbf { R } _ { 3 } ( - \beta ) \mathbf { W } ^ { - 1 } \mathbf { r } } \\ & { \qquad = \mathbf { R } _ { 3 } ( - \beta ) \mathbf { R } _ { 3 } ( - s ^ { \prime } ) \mathbf { R } _ { 2 } ( x _ { p } ) \mathbf { R } _ { 1 } ( y _ { p } ) \mathbf { r } } \\ & { \dot { \mathbf { g } } ( t ) = \dot { \beta } \hat { \mathbf { k } } \wedge \mathbf { g } ( t ) } \\ & { \qquad = \dot { \beta } \left[ \begin{array} { c c c } { - \sin \beta } & { - \cos \beta } & { 0 } \\ { \cos \beta } & { - \sin \beta } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] \mathbf { W } ^ { - 1 } \mathbf { r } . } \end{array}
$$

Polar motion $( \mathbf { W } ^ { - 1 }$ ，see $\ S \ 7 . 2 . 6 . 2 )$ involving $( x _ { p } , y _ { p } )$ the coordinates of the CIP in the ITRS,and $s ^ { \prime }$ the TIO locator (see Chapter6),transforms from the ITRSto the Terrestrial IntermediateReference System.Note that here the transformation starts from the TRS,as in theIERS Conventions.The rotation $\mathbf { R } _ { 3 } ( - \beta )$ rotatesthe Terrestrial Intermediate Reference Systemabout theCIP to the celestial system.The choice of $\beta$ determines thecelestial system and the paradigm;for equinox-based positions set $\beta = \mathrm { G A S T }$ ；forCIO-based positionsset $\beta = \theta$ ,theEarthRotationAngle.This choice willdetermine choicesin Step 5below,and the origin ofright ascension will either be the true equinox or the CIO,respectively.GASTand $\theta$ (theERA),are determinedat the time of observationandare giveninChapter6 (see $\ S 6 . 8 . 4$ and $\ S 6 . 8 . 5 _ { \times }$ ).Note,thatERAandGASTare basicallyfunctionsofUT1,while precessionand nutation are not.

Strictly speaking in the velocity equation (Eq.7.139) $\dot { \beta }$ will be either GAST or $\dot { \theta }$ , respectively,depending on the choice of paradigm.However, the difference between the rates in the two paradigms is very small,and noting that the velocity of the observer on the surface of the Earth is then added to the velocity of the Earth (see Step 6, $\ S 7 . 4 . 3 . 5 )$ aspartof theaberration correction,it is sufficient to replace $\dot { \beta }$ with the standard value of the nominal meanangular velocity of theEarth $\omega = 7 . 2 9 2 1 1 5 \times 1 0 ^ { - 5 }$ radians/second.Theunit vector $\hat { \mathbf { k } }$ points towards the north CIP of date.

Polar motion,which affects the components of the observer's geocentric position vector at the 10-meter $( 0 ^ { \prime \prime } 3 )$ level,andmaybeneglectedif desiredbyreplacing ${ \bf R } _ { 1 } ( y _ { p } )$ and ${ \bf R } _ { 2 } ( x _ { p } )$ byunit matrices.The drift of the TIO within theITRS is less than 5O microarcseconds after a century (see $\ S \ 7 . 2 . 6 . 2 )$ ,which isinsignificant,thus ${ \bf R } _ { 3 } ( - s ^ { \prime } )$ mayalso be replaced by a unit matrix.Neglecting polar motion affects the computed topocentric place of the Moon byseveral milliarcseconds,with amuch smallereffect,inverselyproportional to distance, forother bodies.If effectsat this level are important,correctionsarealso required to refer theregional geoid (the coordinate system for the observer's geodetic latitude,longitude and height)to the Earth'sreference ellipsoid.In forming the velocity of the observera standard value forthe rotationrate of the Earth has beenused,and the smalleffects due tothe variation inrate from this value and due to the change of the polar motion components have been ignored.

More information on the computation of an observer's geocentric coordinates are given in Section Kof The Astronomical Almanac,Mueller(1969),Taff (1981),as well asChapter5.

Step 4.Convert the geocentric position and velocity vectors to units ofau and au/day,respectively,by multiplying ${ \bf g } ( t )$ by $1 / A$ and $\dot { { \bf g } } ( t )$ by $8 6 4 0 0 / A$ ,where $A = 1 . 4 9 5 9 7 8 7 0 6 9 1 \times 1 0 ^ { 1 1 }$ is the number of metres in1auand is the value from the JPLDE405/LE405 ephemeris.

Transform the vectors ${ \bf g } ( t )$ and ${ \dot { \bf g } } ( t )$ from the of date system to the ICRS,which is a spacefixed coordinate system and the coordinate system in which the position and velocity of the Earth are expressed.

Step 5.

$$
\begin{array} { r l r l r l } { \mathbf { E } \mathbf { \Psi } _ { } \mathbf { f } ^ { \mathsf { c u r f a c e \cdot \ t a s e \cdot t r a t e : } } \mathbf { g } ( t ) } & { \qquad } & { \mathbf { 5 . } } & { \qquad } & { \mathbf { G } ( t ) = \mathbf { C } ^ { - 1 } \mathbf { g } ( t ) } \\ { \mathbf { G } ( t ) = \mathbf { M } ^ { - 1 } \mathbf { g } ( t ) } & { \qquad } & { \mathbf { 5 . } } & { \qquad } & { \mathbf { G } ( t ) = \mathbf { C } ^ { - 1 } \mathbf { g } ( t ) } \\ { \dot { \mathbf { G } } ( t ) = \mathbf { M } ^ { - 1 } \dot { \mathbf { g } } ( t ) } & { \qquad } & { \dot { \mathbf { G } } ( t ) = \mathbf { C } ^ { - 1 } \dot { \mathbf { g } } ( t ) } \end{array}
$$

where the inverse $\mathbf { M } ^ { - 1 } = \mathbf { M } ^ { \mathrm { T } }$ the transpose of $\mathbf { M }$ (see $\ S 7 . 2 . 5 . 1$ )

where the inverse $\mathbf { C } ^ { - 1 } = \mathbf { C } ^ { \mathrm { { T } } }$ the transpose of $\mathbf { c }$ (see $\ S 7 . 2 . 5 . 2$ ).

The most eficient procedure would be to evaluate the elements of the matrixat this point and save them forlateruse in Step5of $\ S 7 . 4 . 1 . 6$ ,noting that here the inversematrixisused.

Strictly,the frame bias,precession,and nutation matrices definea transformation between aspace-fixed systemand a slowly rotating system.The slow rotation is thechanging orientation of the Earth's axis due to external torques that the precessionand nutation theories describe.Therefore,the conversion of the observers velocity given in Eq.7.141 is missing aCoriolis term.However,the equivalent linear velocity of this rotation is of order $1 0 ^ { - 5 }$ m/second foran observer on the surface of the Earth,comparable to the tracking velocity of large telescopesand completely negligible.

# 7.4.3.5Barycentric Position and Velocity of the Observer

Step 6.Calculate the barycentric position and velocity of the observer $\mathbf { O } _ { \mathrm { B } } ( t )$ and $\dot { \mathbf { O } } _ { \mathrm { B } } ( t )$ ,by adding the geocentric position and velocity of the observer, $\mathbf { G } ( t )$ and $\dot { \mathbf { G } } ( t )$ ,obtained above, to the barycentric position and velocity of the Earth ${ \bf E } _ { \mathrm { B } } ( t )$ and $\dot { \mathbf { E } } _ { \mathrm { B } } ( t )$ obtained in Step 2.1 of $\ S 7 . 4 . 1 . 2$ ,thus

$$
\begin{array} { r } { \mathbf { O } _ { \mathrm { B } } = \mathbf { E } _ { \mathrm { B } } ( t ) + \mathbf { G } ( t ) } \\ { \dot { \mathbf { O } } _ { \mathrm { B } } = \dot { \mathbf { E } } _ { \mathrm { B } } ( t ) + \dot { \mathbf { G } } ( t ) . } \end{array}
$$

Then redefine the vectors ${ \bf E } _ { \mathrm { B } } ( t )$ and $\dot { \mathbf { E } } _ { \mathrm { B } } ( t )$ to be identical to $\mathbf { O } _ { \mathrm { B } } ( t )$ and $\dot { \bf O } _ { \mathrm { B } }$ .

# 7.4.3.6 Topocentric Place

Step 7.Continuing at Step 2.1 in $\ S 7 . 4 . 1 . 2$ ,the other steps follow as before,except that the transformation matrix (see Step 5 above) from the GCRS need not be re-computed in the steps in $\ S \ 7 . 4 . 1 . 6$ .

The right ascension $\alpha$ and declination δobtained at Step6 represent the topocentric place of the object at the epoch of observation.The topocentric hour angle of the object may be calculatedby replacingSteps5and6by Steps $5 ^ { * }$ and $6 ^ { * }$ .Alternatively see $\ S 7 . 1 . 3 . 2$ ,where hourangle is given in terms of right ascension.

In many cases the above procedure may be simplified but most care is needed for objects in the inner solar system when the highest precision is required.For objects beyond the inner solar system,to milliarcsecond precision, when using the equinox method nutation may be ignored throughout.Thatis,mean sidereal time can be used instead of apparent sidereal time (the equation of the equinoxes can be considered zero) and nutation may be neglected. Additionally,the difference between UT1and UTC timescalescan be ignored.However, these simplifications may not resultin any real computational saving.The nutation parameters would have to be calculated anyway inalater step.Furthermore,these simplifications affect the computed sidereal time at the $1 ^ { s }$ level,and will therefore cause errorsin the computed topocentric hourangleof thismagnitude.Therefore,inmanycases,carryingout the full procedure,and saving the values of the relevant nutation and time variables for later use, may be the most prudent course.

# 7.4.4Summary of the Algorithms

The development of the apparent and intermediate place algorithms using matrix/vector notation is rigorous and allows the planet and star algorithms to use those parts which are common to both.It also allows users to tailor their program to their own needs,as well as the testing of alternative,or simplified,algorithms for special purposes.

In this unified approach for planets and stars,position vectors have been used throughout. Many other algorithms use unit vectors (see The Astronomical Almanac).There are penalties either way,and if the proceduresare carefully implemented the results will be identical.

Themethod given here involvesa series of steps.However,if the observation time remains the same,quantities such as the time arguments,the ephemeris data for the Earth, the precession and nutation matrices can be saved and re-used.For example,when there arealarge numberof“ofdate”places to be computed,it ismore efficient to compute the places of all bodies at a given observing epoch before moving to a new observing epoch.The major computational burden in the algorithm involvestheretrieval of datafromthe planetary ephemerisin $\ S 7 . 4 . 1 . 2$ Steps2.1 through 2.6 and the evaluation of the two nutation angles $\Delta \psi$ and $\Delta \epsilon$ orequivalently the $( { \mathcal { X } } , { \mathcal { Y } } )$ coordinates ofthe CIP,that areinvolved in thecalculation of the transformation from the GCRS to “of date"position see, $\ S 7 . 4 . 1 . 6$ , $\ S 7 . 2 . 5 $ and Chapter6.

If computational time becomes critical (such as within telescope control systems or in micro-computer implementations),the method of obtaining the ephemeris and nutation data mustbe considered.Self-contained algorithms can often be simplified by truncating small terms from the series,ifhigh precision in the final place is not required.Consideration should also be given to pre-computing therequired data for fixed intervals and storing the data in an external file which can be efficiently accessed and interpolated.Planetary ephemeris data arefrequently distributed in this form anyway.Pre-computing and storing the elementsof thecombined bias-precession-nutation matrix $\mathbf { M }$ or $\mathbf { C }$ (see $\ S \ 7 . 2 . 5$ ）isalso feasible.The convenience of self-contained algorithms must be weighed against the number ofcalculations required,the accuracy of the algorithm,and the accuracy needed for the final result.

# 7.4.5Approximate Algorithms

This section summarizes mean places and the method of Day Numbers.Together these techniques were auseful procedure for calculating apparent places of stars accurately $( \pm 0 . ^ { \prime \prime } 0 1 )$ where most of the information was pre-computed.First,however,we give an algorithm for calculating the intermediate place,accurate to about $\pm 1 ^ { \prime \prime }$ over a century and the resulting altitudeandazimuth.

# 7.4.5.1 Approximate ClO-based Method

The following is an approximate procedure based on the CIO method for calculating the intermediate position of astar fora specified UT1 instant.During the process the intermediate right ascension and declination $( \alpha _ { i } , \delta _ { i } )$ ,the GHA,LHA,and the altitude andazimuth $( a , A _ { Z } )$ areall calculated.The procedure given isaccurate to about $\pm 1 ^ { \prime \prime }$ between1925and2100, however,between 1900 and 1925 the errors may reach $1 ^ { \prime \prime } 7$ due to the approximation of the Earth'svelocity.This analysis assumed that the ERA was calculated accurately.

Strictly,all the parameters,except the ERA $\mathbf { \Pi } ^ { ( \theta ) }$ ,should be evaluated for the equivalent $\mathrm { T T } \left( \mathrm { U T 1 } + \Delta \mathrm { T } \right)$ instant.

Step 1.Given the observer's position $( \lambda , \phi )$ and a givenUT1 instant,(i.e.,aspecifieddate and UT1 time),calculate the UT1Julian dateand fraction (JD).Also form the intervals $D _ { \mathrm { U } }$ in daysand $T$ in Julian centuries,respectively,from $\mathrm { J 2 0 0 0 . 0 = 2 4 5 1 5 4 5 . 0 U T 1 }$ .

$$
D _ { \mathrm { U } } { = } \mathrm { J D } { - } 2 4 5 1 5 4 5 . 0 \quad { \mathrm { a n d } } \quad T { = } D _ { \mathrm { U } } / 3 6 5 2 5 . 
$$

Step 2.Evaluate the position (q) and space motion $\mathbf { \Pi } ^ { ( \mathbf { m } ) }$ vectors of the star with respect to the ICRS (see $\ S 7 . 2 . 1$ ,Eqs.7.20 and 7.22 or 7.24).

Step 3.Apply space motion and ignore parallax to give the approximate geocentric position of the star at the epoch of date,

$$
\mathbf { p } = \mathbf { q } + T \mathbf { m } .
$$

Step 4.Apply aberration and precession-nutation,resulting in an of date position

$$
\mathbf { r } = \mathbf { V } + \mathbf { C } ( { \boldsymbol { \chi } } , { \boldsymbol { \ y } } , s ) \mathbf { p }
$$

where $\mathbf { V } = ( V _ { x } , V _ { y } , V _ { z } )$ inau/day is the approximate barycentric velocity of the Earth (see Eqs.7.44). The more accurate the approximation of $\mathbf { V }$ the better the result. The precessionnutation matrix $\mathbf { C }$ isapproximated byignoring the tiny rotation $s$ ,and simplifyingEq 7.75. Expanding the matrix equation gives

$$
\left[ { \begin{array} { c } { x _ { i } } \\ { y _ { i } } \\ { z _ { i } } \end{array} } \right] = { \frac { 1 } { c } } { \left[ \begin{array} { l } { + 0 . 0 1 7 2 \sin L } \\ { - 0 . 0 1 5 8 \cos L } \\ { - 0 . 0 0 6 8 \cos L } \end{array} \right] } + \left[ { \begin{array} { c c c } { 1 - \chi ^ { 2 } / 2 } & { 0 } & { - \chi } \\ { 0 } & { 1 } & { - \mathcal { V } } \\ { \chi } & { \mathcal { V } } & { 1 - \chi ^ { 2 } / 2 } \end{array} } \right] { \left[ \begin{array} { l } { p _ { x } } \\ { p _ { y } } \\ { p _ { z } } \end{array} \right] } .
$$

Thus,first calculate the following quantities

$$
\begin{array} { r l } & { L = 2 8 0 { \% } 5 + 3 6 0 0 0 { \% } 8 \bar { T } } \\ & { \Omega = 1 2 5 . 0 - 1 9 3 4 { \cdot } 1 \bar { T } } \\ & { \mathcal { X } = + 2 0 0 4 { \% } T - 0 { \% } { \it 4 } 3 T ^ { 2 } - 6 { \% } 8 4 \sin \Omega - 0 . 5 2 \sin 2 L } \\ & { \mathcal { Y } = - 0 { \it 4 } ^ { \prime \prime } 0 3 T - 2 2 { \it 4 } 1 T ^ { 2 } + 9 { \it 4 } ^ { \prime \prime } 2 1 \cos \Omega + 0 . 5 7 \cos 2 L . } \end{array}
$$

These simple formulae for $\mathcal { X }$ and $_ { \mathcal { V } }$ are accurate to $\pm 0 . 6$ between 1900 and 2100,thus keeping this part of the approximation well below the target accuracy of $1 ^ { \prime \prime }$ .Theecliptic longitude of the Sun, $L$ ,isused in both the position of the CIP and approximating the barycentric velocity of the Earth.The speed of light is given by $c = 1 7 3 . 1 4 \mathrm { a u } / \mathrm { d }$ .

Multiplying out the matrix and rewriting in terms of coordinates,the position of the star with respect to the Celestial Intermediate Reference System is given by

$$
\begin{array} { l } { x _ { i } = V _ { x } + p _ { x } ( 1 - \mathcal { X } ^ { 2 } / 2 ) - p _ { z } \mathcal { X } } \\ { y _ { i } = V _ { y } + p _ { y } - p _ { z } \mathcal { V } } \\ { z _ { i } = V _ { z } + p _ { x } \mathcal { X } + p _ { y } \mathcal { V } + p _ { z } ( 1 - \mathcal { X } ^ { 2 } / 2 ) } \end{array}
$$

where $\mathcal { X }$ and $y$ must beexpressed inradians.Use Eq.7.2 replacing $( \xi , \eta , \zeta )$ with $( x _ { i } , y _ { i } , z _ { i } )$ to give $( \alpha _ { i } , \delta )$ the approximate intermediate place.

Step 5.Next transform to the observers local system,by rotations of $\theta + \lambda$ about the CIP, followedbyarotation of $9 0 ^ { \circ } - \phi$ aboutthe $y$ -axis inthe planeof the observer's localmeridian, giving

$$
\begin{array} { l } { x = - [ x _ { i } \cos ( \theta + \lambda ) + y _ { i } \sin ( \theta + \lambda ) ] \sin \phi + z _ { i } \cos \phi } \\ { y = - x _ { i } \sin ( \theta + \lambda ) + y _ { i } \cos ( \theta + \lambda ) } \\ { z = + [ x _ { i } \cos ( \theta + \lambda ) + y _ { i } \sin ( \theta + \lambda ) ] \cos \phi + z _ { i } \sin \phi } \end{array}
$$

where the Earth Rotation Angleis given by

$$
\begin{array} { r l } & { \theta = 2 \pi ( 0 . 7 7 9 0 5 7 2 7 3 2 6 4 0 + 1 . 0 0 2 7 3 7 8 1 1 9 1 1 3 5 4 4 8 D _ { \mathrm { U } } ) \mathrm { r a d i a n s } } \\ & { \quad = 3 6 0 ^ { \circ } ( 0 . 7 7 9 0 5 7 2 7 3 2 6 4 0 + 0 . 0 0 2 7 3 7 8 1 1 9 1 1 3 5 4 4 8 D _ { \mathrm { U } } + D _ { \mathrm { U } } \mathrm { m o d } 1 ) . } \end{array}
$$

$D _ { \mathrm { U } } \mathrm { m o d } 1$ isthe fraction of the UT1 day remainingafter removing all the whole days.At this stage the quantities $\mathrm { G H A } = \theta - \alpha _ { i }$ and $\operatorname { L H A } = \theta - \alpha _ { i } + \lambda$ ,may also be formed (see $\ S 7 . 1 . 3 . 2 $ .It should be noted that there are no approximations in this or the next step.

Step 6.Finally convert from $x$ , $y$ , $Z$ coordinates to altitude $( a )$ and azimuth $( A _ { z } )$

$$
a = \tan ^ { - 1 } { \frac { z } { \sqrt { ( x ^ { 2 } + y ^ { 2 } ) } } } \quad { \mathrm { a n d } } \quad A _ { z } = \tan ^ { - 1 } { \frac { y } { x } }
$$

where azimuth is measured from north through east in the plane of the horizon and altitude is measured perpendicular to the horizon (see $\ S 7 . 1 . 3 . 4 $ .To approximate the topocentricaltitude (to about O.1) add the parallax in altitude (see $\ S 7 . 2 . 2 . 2 $ and refraction (see $\ S 7 . 2 . 7 . 3$ ).

# 7.4.5.2 Mean Places

Mean places are a concept that is particularly used for positions of starsand other objects outside the solar system.The mean place represents the direction of the object as it would hypothetically be observed from the solar system barycentre at the specified date.The coordinate system must be specified;positions could be referred to a standard coordinate system(ICRS,J2000.0,etc.) or one“of date".

Section Hof TheAstronomicalAlmanac includes listsof the mean places of different types of stars and stellar objects.These are barycentric positions that are tabulated with respect to the mean equinox of the middle of the year, e.g.,J2o13.5.To calculate such amean place at agiven date,take the ICRS (barycentric) catalogue position (r) (as found in most star catalogues),apply space motion (see $\ S 7 . 2 . 1$ and Eq.7.25) from the epoch of the catalogue position $\mathbf { \rho } ( t )$ to the required date $( t _ { 1 } )$ and then transform from the ICRS to the mean equinox of date (PB), thus

$$
\mathbf { r } _ { 2 } = \mathbf { P } \mathbf { B } \left( \mathbf { r } + \left( t _ { 1 } - t \right) \dot { \mathbf { r } } \right)
$$

An apparent place (see $\ S 7 . 4 . 2 )$ with nutation ignored,i.e.,place with respectto the mean equinox of date,is useful when calculating hour angles since the lengthy calculation of nutation angles is not required.Hour angles are discussed in $\ S ~ 7 . 1 . 3 . 2$ .This concept does not apply to theIAU recommended Celestial Intermediate Reference System which may be referred to as the equator and CIO of date.

# 7.4.5.3 Methods Using Day Numbers

Historically there are two Day Numbers techniques,Besselian Day Numbers and Independent Day Numbers.These techniques are described in the $\ S \ 3 . 3 4$ of the previous edition of the Explanatory Supplement (Hohenkerk etal.1992)and the Besselian Day Numbers were last tabulatedinTheAstronomical Almanacfor2003.

Insummary,the apparent (equinox) rightascension and declination $( \alpha _ { 1 } , \delta _ { 1 } )$ ,ofastarat an epoch $t + \tau$ ,which includes the effects of precession,nutation,annual aberration,proper motion,annual parallax,and includes the second-order day numbers( $J$ and $J ^ { \prime }$ )，maybe calculated either using theBesselian Day Numbers $A , B , C , D , E$ ,and star constants,from

$$
\begin{array} { l } { { \alpha _ { 1 } = \alpha + A a + B b + C c + D d + E + J \tan ^ { 2 } \delta + \tau \mu _ { \alpha } + \pi ( d X - c Y ) } } \\ { { \delta _ { 1 } = \delta + A a ^ { \prime } + B b ^ { \prime } + C c ^ { \prime } + D d ^ { \prime } + J ^ { \prime } \tan \delta + \tau \mu _ { \delta } + \pi ( d ^ { \prime } X - c ^ { \prime } Y ) } } \end{array}
$$

or using the Independent Day Numbers $f , g , G , h , H$ ,from

$$
\begin{array} { l } { { \alpha _ { 1 } = \alpha + f + g \sin { ( G + \alpha ) } \tan \delta + h \sin { ( H + \alpha ) } \sec \delta + J \tan ^ { 2 } \delta } } \\ { { \qquad + \tau \mu _ { \alpha } + \pi ( d X - c Y ) } } \\ { { \delta _ { 1 } = \delta + g \cos { ( G + \alpha ) } + h \cos { ( H + \alpha ) } \sin \delta + i \cos { \delta } + J ^ { \prime } \tan { \delta } } } \\ { { \qquad + \tau \mu _ { \delta } + \pi ( d ^ { \prime } X - c ^ { \prime } Y ) } } \end{array}
$$

where $\alpha$ , $\delta$ aretheright ascension and declination of the star for the mean equinox and epoch of $t$ ,and $\mu _ { \alpha }$ and $\mu _ { \delta }$ are the annual proper motions in right ascension and declination, respectively and $\pi$ is the parallax. $X$ and $Y$ are the barycentric coordinates of the Earth.For stars,the corrections for the deflection of light was not included.

Acknowledgements.Acknowledgements are due to the original authors and others as much of the material in this chapter—particular on the effects space motion,parallax,aberration, light deflectionand refraction-is taken from Chapter 3of the previous edition (Hohenkerk etal.1992)which was collaborative effort between the Nautical Almanac Offices of the U.S. andUK.

# REFERENCES

1.The Astronomical Almanac Online: http://asa.usno.navy.mil orhtp://asa.hmnao.com.   
2.Naval Observatory Vector Astrometry Software (NOVAS): http://aa.usno.navy.mil/software/novas/novas_info.php.   
3.IAU Standards of Fundamental Astronomy (SOFA) Software Collction: http://www.iausofa.org/.   
4.IAU Commission4(Ephemerides): http://www.iaucom4.org/.   
5.International Earth Rotationand Reference Systems Service: http://www.iers.org/.   
6.IAUResolutionsAdopted bythe General Assemblies: http://www.iau.org/administration/resolutions/general_assemblies/.   
Abalakin,V.K.(1985).RefractionTablesofPulkovo Observatory(5th ed.).Leningrad:Academy of Sciences of theUSSR.NaukaPublishingHouse.   
Auer,L.H.and E.M.Standish (1979).Astronomical Refraction:Computational Method for All Zenith Angles.Technical note,Yale University Astronomy Department,NewHaven,CT.   
Auer,L.H.andE.M.Standish(2oo0).Astronomical Refraction:ComputationalMethod forAllZenith Angles.Astronomical Journal 119,2472-2474.   
Capitaine,N.andP.T.Wallace(2Oo6).High PrecisionMethods forLocating theCelestial Intermediate Poleand Origin.Astronomy and Astrophysics450,855-872.   
Dyson,F.W.,A.S.Eddington,andC.Davidson (192O).ADeterminationof theDeflectionofLight bythe Sun’s Gravitational Field,from Observations Madeat the Total Eclipse of May 29,1919. RoyalSocietyofLondonPhilosophicalTransactionsSeriesA220,291-333.   
Einstein,A.(1956).The Meaning of Relativity(5th ed.).Princeton andLondon:Princeton University Press.   
Fairhead,L.andP.Bretagnon (199O).Ananalytical formulafor the time transformation TD-TT. Astronomyand Astrophysics229,240-247.   
Fomalont,E.B.andR.A.Sramek (1975).A confirmation of Einstein's general theory of relativity by measuring the bendingof microwaveradiation inthe gravitational fieldof the Sun.Astrophysical Journal199,749-755.   
Hilton,J.L.,N.Capitaine,J.Chapront,J.M.Ferrandiz,A.Fienga,T.Fukushima,J.Getino,P.Mathews, J.-L.Simon,M.Soffel,J.Vondrak,P.Wallace,andJ.Williams (2Oo6).Report of the Intemational Astronomical Union DivisionIWorking GrouponPrecessonand the Ecliptic.Celestial Mechanics and Dynamical Astronomy94,351-367.   
Hohenkerk,C.Y.andA.T.Sinclair(1985).Thecomputation ofangular atmospheric refractionatlarge zenithangles.Technical Note 63,HMNautical AlmanacOffice,Greenwich.   
Hohenkerk,C.Y.,B.Yallop,C.A.Smith,andA.T.Sinclair(1992).Celestial Reference Systems.In P.K.Seidelmann (Ed.),Explanatory Supplement to TheAstronomicalAlmanac,Chapter3,pp. 95-198.Mill Valley,CA: University Science Books.   
IAU(20o1).InH.Rickman (Ed.),Transactionsof the International Astronomical Union,Volume XXIVB,San Francisco.Astronomical Society of the Pacific.Proc.24th General Assembly, Manchester,2000.   
IAU (2008).InK.A.vander Hucht (Ed.),Transactionsof the International Astronomical Union, Volume XXVIB,Cambridge.Cambridge University Press.Proc.26th General Assembly,Prague, 2006.   
IERS (2O10).Conventions (2O10). Technical Note 36,International Earth Rotation and Reference SystemsService,Frankfurt am Main.Verlagdes Bundesamts fir Kartographieund Geodäsie, G.Petit and B.Luzum (Eds.).   
Kaplan, G.H.(2Oo5).The IAU Resolutions on Astronomical Reference Systems,Time Scales,and EarthRotationModels.Circular179,U.S.Naval Observatory,Washington,DC.   
Kaplan,G.H.,J.A.Bangert,J.L.Bartlett,W.K.Puatua,andA.K.B.Monet(2OO9).User'sGuide to NOVAS 3.0.Circular180,U.S.Naval Observatory,Washington,DC.   
Kaplan,G.H.,J.A.Hughes,P.K.Seidelmann,C.A.Smith,andB.D.Yallop (1989).Mean and apparent place computations in the new IAU system.II.Apparent, topocentric,and astrometric placesof planetsand stars.AstronomicalJournal97,1197-1210.   
Moisson,X.andP.Bretagnon (2Oo1).Analytical Planetary solutionVSOP2000.Celestial Mechanics andDynamical Astronomy80,205-213.   
Murray,C.A.(1981).Relativisticastrometry.Monthly Noticesofthe RoyalAstronomical Society195, 639-648.   
Murray,C.A.(1985).Vectorial Astrometry (5th ed.).Bristol:Hilger.   
NauticalAlmanacOfficesofUKandUSA(1983).TheAstronomicalAlmanacfortheYear1984. Washington&London: US Government Printing Office& HM Stationery Office.   
Pulkova Obs.(1956).Refraction tables of Pulkova Observatory (4th ed.).Moscow andLeningrad: Academy of Sciences Press.   
Saastamoinen,J. (1972).Introduction to practical computation of astronomical refraction.Buletinof Geodesy 106,383-397.   
Seidelmann,P.K.(Ed.)(1992).Explanatory Supplementto TheAstronomicalAlmanac.Mill Valley, CA:University Science Books.   
Shapiro,I.I.(1967).New method for the detectionof light deflection by solar gravity.Science 157, 806-808.   
Simon,J.L.,P.Bretagnon,J.Chapront,M.Chapront-Touze,G.Francou,andJ.Laskar(1994). Numerical expressons for precession formulae and mean elements for the Moon and planets. Astronomy and Astrophysics 282,663-683.   
Standish,E.M.(1998a).JPLPlanetary andLunar Ephemerides,DE405/LE405.IOM312.F-98-048, Jet Propulsion Laboratory.   
Standish,E.M.(1998b).Time scales in JPL and CfA ephemerides.Astronomy andAstrophysics336, 381-384.   
Stumpff,P.(1979).The rigorous treatment of stellar aberration and doppler shift,and the barycentric motion of the Earth.Astronomy and Astrophysics 78,229-238.   
Stumpff,P.(198Oa). On the relationship between classical and relativistic theory of stellar aberration. Astronomyand Astrophysics84,257-259.   
Stumpff,P.(198ob).Two self-consistent Fortran subroutines forthe computationof the Earth's motion. AstronomyandAstrophysicsSupplementSeries4l,1-8.   
Stumpff,P.(1985).Rigorous treatment of the heliocentric motion of stars.Astronomy and Astrophysics144,232-240.   
Taff,L.G.(1981).Computational Spherical Astronomy.New York:Wiley.   
Wallace,P.T.and N.Capitaine (2Oo6).Precession-nutation procedures consistent with IAU 2006 resolutions.AstronomyandAstrophysics 459,981-985.   
Yallop,B.D.(1983).TheAstronomical Almanac for the Year1984.Washington&London:US Government Printing Office&HMStationery Office.Pages B16-B41.

# FURTHER READING

Atkinson,R.d.(1972).Modem Aberration for Observations of any Date.Astronomical Journal 77, 512-517.   
Capitaine,N.,J.Chapront,S.Lambert,andP.T.Wallace (2Oo3).Expressionsfor thecelestial intermediate pole and celestial ephemeris originconsistent with the IAU 2oooA precession-nutation model.AstronomyandAstrophysics400,1145-1154.   
Capitaine,N.and A.Gontier (1993).Accurate procedure for deriving UTI atasubmilliarcsecond accuracy from Greenwich Sidereal Timeor fromthe stellarangle.Astronomy and Astrophysics 275, 645-650.   
Capitaine,N.,B.Guinot,andD.D.McCarthy(2OoO).Definitionofthe Celestial Ephemeris Origin and ofUT1in the InternationalCelestialReferenceFrame.AstronomyandAstrophysics355,398-405.   
Capitaine,N.,P.T.Wallace,andJ.Chapront (2OO3).Expressions for IAU2Ooo Precession Quantities (IAU2006 P03 model).Astronomy and Astrophysics 412,567-586.   
Capitaine,N.,P.T.Wallace,andJ.Chapront (2005).Improvement of the IAU20oO precession model. AstronomyandAstrophysics432,355-367.   
Capitaine,N.,P.T.Wallace,andD.D.McCarthy (2003).Expressions to Implement theIAU2000 DefinitionofUT1.Astronomyand Astrophysics406,1135-1149.   
Chapront,J.,M.Chapront-Touzé,andG.Francou (2Oo2).Anewdetermination oflunarorbital parameters,precession constantand tidal acceleration fromLLR measurements.Astronomyand Astrophysics387,700-709.   
Chauvenet,W.(196O).AManualofsphericalandpracticalastronomy-Vol.l:Spherical astronomy; Vol.2:Theory anduseofastronomical instruments.Methodof least squares (revisedand corr.,5th ed.).New York:DoverPublication.   
Duncombe,R.L.,W.Fricke,P.K.Seidelmann,and G.A.Wilkins (1977).Joint report of the working groups of the IAU Commission 4on precession, planetary ephemerides,unitsand time-scales.In E.A.MullerandA.Jappel(Eds.),TransactionsoftheInternationalAstronomicalUnion,Volume XVIB,Dordrecht,pp.56.Reidel.Proc.16th General Assembly,Grenoble,1976.   
Duncombe,R.L.,P.K.Seidelmann,and T.C.van Flandern (1975).Celestial reference systems derivable from solar system dynamics.InB.Kolaczek and G.Weiffenbach (Eds.),IAU Colloq.26: OnReferenceCoordinate Systemsfor Earth Dynamics,pp.223-233.   
Eichelberger,W.S.(19o4).Reduction tables for transit circle observations.In Publications of the UnitedStatesNavalObservatory,2ndSeries,Volume4,part4,appendix2.Washington:US Government Printing Office.   
Emerson,B.(1973).Amethod ofcalculating apparent places of stars.Royal Greenwich Observatory Bulletin178,299-300.   
Garfinkel,B.(1944).Aninvestigationinthe theoryofastronomicalrefraction.AstronomicalJournal50, 169-179.   
Garfinkel,B.(1967).Astronomical refraction in apolytropic atmosphere.Astronomical Journal 72, 235-254.   
Green,R.M. (1985).SphericalAstronomy (5thed.).CambridgeandNewYork:Cambridge University Press.   
Harzer,P.(1924a).Berechnung der AblenkungderLichtstrahlen in der Atmosphäre der Erde auf rein meteorologisch-physikalischer Grundlage.Publikationder Sternwartein Kiel (13).   
Harzer,P.(1924b).Gebrauchstabellen zur Berechnung der Ablenkungen derLichtstrahlen in der AtmosphärederErde fuirdie Beobachtungenam grossen KielerMeridiankreise.Publikationder Sternwarte in Kiel (14).   
IERS(20O4).Conventions (2Oo3).Technical Note32,International Earth Rotation Service,Frankfurt amMain.Verlag desBundesamts fir Kartographieund Geodasie,D.D.McCarthy and G.Petit (Eds.).   
Kaplan,G.H.(1981).The IAU resolutionson astronomicalconstants,time scales,and the fundamental referenceframe.Circular163,U.S.NavalObservatory,Washington,DC.   
Kovalevsky,J.andP.K.Seidelmann (2Oo4).FundamentalsofAstrometry.CambridgeandNew York: Cambridge University Press.   
Lederle,T.and H.Schwan (1984).Procedure for computing the apparent places of fundamental stars (APFS) from1984 onwards.Astronomyand Astrophysics134,1-6.   
Mathews,P.M.,T.A.Herring,and B.A.Buffet (20o2).Modeling of nutationand precession New nutation seriesfor nonrigid Earthand insights into theEarth'sinterior.Journal ofGeophysical Research 107,2068-2093.   
Moyer,T.D.(1981).Transformation from proper time on earth to coordinate time insolar system barycentric space-time frameof reference.I.II.Celestial Mechanics 23,33-56.   
Nautical Almanac Officesof UKand USA (1961).Explanatory Supplement to The Astronomical EphemerisandTheAmericanEphemerisandNauticalAlmanac.London:HerMajesty'sStationery Office. Reprinted 1974.   
Porter,J.G.andD.H.Sadler (1953).The accurate calculation of apparent places of stars.Monthly NoticesoftheRoyalAstronomical Society113,455-467.   
Smart,W.M.(1944).Text-book in Spherical Astronomy.Cambridge:Cambridge University Press.   
Standish,E.M.(1982).Orientationof the JPL ephemerides,DE200/LE200,to the dynamical equinox of J2000.Astronomy and Astrophysicsl14,297-302.   
Stumpff,P.(1986).Relativistic and perspective effects in proper motions and radial velocities of stars. InJ.KovaleskyandV.A.Brumberg(Eds.),RelativityinCelestialMechanicsandAstronomy,IAU Symposium114,pp.193-198.Dordrecht: Reidel.   
Willis,J.E.(1941).Adeterminationof astronomical refraction from physical data.Transactions of the American Geophysical Union,324.   
Woolard,E.W.andG.M.Clemence (1981).Spherical Astronomy.New York &London:Academic Press.

# Orbital Ephemerides of the Sun, Moon,and Planets

E.MYLESSTANDISH&JAMESG.WILLIAMS

# 8.1 Fundamental Ephemerides

The fundamental planetary and lunar ephemerides of The Astronomical Almanac,starting in the year 2003,are DE405/LE405of Caltech's JetPropulsion Laboratory (JPL).They replace JPL'sDE2OO which have been used in thealmanac since 1984.Previous to 1984,the fundamental ephemerides were based upon analytical theories;these are described in $\ S 8 . 2$ DE405/LE4o5 result from a least-squares adjustment of a previously existing ephemeris to avariety of observational data (measurements),followed byanumerical integrationof the dynamical equations of motion which describe the gravitational physics of the solar system. These fundamental ephemerides are the bases for computing the planetary and lunar positions and other related phenomena thatare listed in the almanac.

For the final (integration) phase of the ephemeris creation process,there are three main ingredients,each ofwhich constitutesamajorphase itself:

·the equations of motion describing the gravitational physics which govern the dynamical motions of the bodies,   
·a method for integrating the equations of motion,and   
·the initial conditions and dynamical constants;i.e.,the starting positions and velocities of the bodiesat some initial epoch alongwith the values for various constants which affect the motion (e.g.,planetary masses).

Itis mainly the accuracy of the third component,the initial conditions and dynamical constants,which determines the accuracy of modern-day ephemerides,since the other two components (the physicsand the integrationmethod) are both believed to be sufficiently complete and accurate.The values of the initial conditions and constants are determined by the least-squares adjustment of them to the observational data (measurements),and the accuracy of this adjustment,and thus of the ephemerides themselves,depends primarily uponthe distribution,variety,and accuracy of the observational data.Thiscrucial part of the ephemeris creation process is given in $\ S 8 . 5$

It is assumed that the equations of motion accurately describe the basic physics which governthe motion of the major bodies of the solar system-atleastto the presently observable accuracy.For themotion of theMoon,the fittingof the lunarephemeristo the lunar laser ranging observations isused to estimate the constants involved andto help distinguish various models of the lunar interior,Earth-raised tides,etc.The equations of motion are given in $\ S 8 . 3$

Numerical integration of the equations of motion is the only known method capable of computing fundamental ephemerides at an accuracy which is comparable to that of the modern-day observations;analytical theories have not beenable to attain such high accuracy. The computerprogram which was used to integrate the equations of motion for DE405/LE405 has been demonstrated to be sufficiently accurate (Newhall,Standish,and Williams1983).

The reference frame for the ephemerides is the International Celestial Reference Frame (ICRF:Ma et al.1998).The advantages for using the frame are many;they are discussed in $\ S \ S . 6$

Theindependent variable of the equations of motion,and,thus,of the fundamental ephemerides themselves,may be termed, $\mathrm { ^ { * } T _ { e p h } } ^ { \mathrm { } } ,$ . It isafully rigorous relativisticcoordinate time,implicitly defined by the equations of motion themselves. $\mathrm { T _ { e p h } }$ may be considered similar to previously-defined“ET”or to“TDB”,since their average rates are the same,even though thereare basic differences in thedefinitions.The time recently defined by the IAU, “TCB",ismathematicallyquivalentto $\mathrm { T _ { e p h } }$ ; TCB and $\mathrm { T _ { e p h } }$ difer by only a constant rate. (Fora discussion,see Standish (1998)).

Thischapter describes the previous ephemerides used in The Astronomical Almanac $( \ S \ 8 . 2 )$ ;presents the equations of motion used in computing the present ephemeris,DE405 $( \ S \ 8 . 3 )$ ；givessome detail about the numerical integrationprogram $( \ S \ 8 . 4 )$ ;describes the observationaldatatowhichDE4O5wasadjusted $( \ S \ 8 . 5 )$ ;discusses thereference frame of theephemerides $( \ S 8 . 6 )$ ;givessome of the formulae used in reducing theobservational data (8.7); presents the values of the initial conditions and constants of DE4o5(g8.8);estimates the accuracy ofthe ephemerides(S 8.9); gives sets of Keplerian elements useful forproducing approximate planetarycoordinates (S 8.10); and shows the sources where DE405/LE405 may be found on CDrom and over the internet $( \ S 8 . 1 1 )$

# 8.2Previous Ephemerides Used in TheAstronomical Almanac

# 8.2.1Ephemerides Priorto 1984

Before1984,theephemeridesfor the Sun,Mercury，Venus,andMarswere basedon the theories and tables of Newcomb (1898a,b,c,d). Computerized evaluations of the tables were used from 1960 through 1980.From 1981 to 1983,the ephemerideswere based on the evaluations of the theories themselves.The ephemerides of the Sun were derived from the algorithm given byS.Newcombin TablesoftheSun(Newcomb1898d).Newcomb's theories oftheinnerplanets(1895-1898) served as the basis for the heliocentric ephemeridesof Mercury,Venus,and Mars.In the case ofMars,the corrections derived byF.E.Ross (1917) were applied.

Ephemeridesof the outerplanets,Jupiter,Saturn,Uranus,Neptune,andPluto,were computed from the heliocentric rectangular coordinates obtained by numerical integration (Eckert,Brouwer,and Clemence 1951).Although perturbations by the inner planets (Clemence 1954)were included in the printed geocentric ephemerides of the outer planets,they were omitted from the printed heliocentric ephemerides and orbital elements.

Thelunar ephemeris,designated by the serial number $j = 2$ ，wascalculated directly fromE.W.Brown'salgorithm insteadof from his TablesofMotionoftheMoon (1919). Thiswas specified in the Improved Lunar Ephemeris (Eckert,Jones,and Clark1954).

Toobtaina strictly gravitational ephemeris expressed in themeasure of time defined by Newcomb's Tables of the Sun,the fundamental arguments of Brown's tableswere amended by removing the empirical termandby applying to the Moon's mean longitude the correction, $- 8 . 7 7 2 - 2 6 . 7 4 T - 1 1 . 7 2 2 T ^ { 2 }$ ,where $T$ is measured in Julian centuries from 190o January 0.5(JED 2415020.0.In addition,this ephemeriswas based on the IAU(1964) System ofAstronomical Constants,and was further improved in its precision by transformation corrections (Eckert,Walker,andEckert1966,Eckert,VanFlandern,and Wilkins1969).The expressions for the mean longitude of the Moon and its perigee were adjusted to remove the implicit partial correction for aberration (Clemence,Porter,and Sadler1952).

# 8.2.2 Ephemerides from 1984through 2002

During theyears1984-2003,the JPL ephemerides,DE200/LE200,were the basesof the ephemerides in The Astronomical Almanac.The equations of motion were essentially those used in JPL'sDE1O2(Newhall,Standish,and William1983); they are also described in the previous Explanatory Supplement (Standish etal.1992).The observations to which these ephemerides were fitis documented in Standish(199O).The reference frame of DE2OO is the mean equator and dynamical equinox of J2ooo.O,as determined and described in Standish (1982).

# 8.2.3Ephemerides Starting in 2003

Startingin2Oo3,the fundamental planetaryand lunar ephemerides of TheAstronomical AlmanacareDE4o5/LE4o5,referenced,asnotedabove,tothe InternationalCelestialReference Frame (ICRF).The remainder of thischapter describes the creation ofDE405.

# 8.3Equations of Motion

Equations of motion describe the forces upon the planets,Sun and Moon which affect their motionsand the torques upon the Moon which affect its orientation.It is believed that the equationsdescribed here are correct and complete tothelevel of accuracy ofthe observational data.I.e.,given the accuracy of the observations,there is nothing to suggest that other forces ordifferent forces are presentinthe solar system.The uncertainties existing inthe planets'and Moon's motions are certainly explainable,considering the uncertaintiesin the observations and in the fitted initial conditions and dynamical constants.

The major elements of this section were developed at JPL over the past few decades.Just the formulae are given here;also included are references to their descriptions,previously published by those responsible for their development.

The equations of motion used for the creation of DE4O5/LE405 included contributions from: (a) point-massinteractions among theMoon,planets,and Sun; (b) general relativity (isotropic,parametrized post-Newtonian);(c)Newtonian perturbations of selected asteroids; (d)action upon the figure of the Earth from the Moon and Sun; (e)action upon the figure of the Moon from the Earth and Sun;(f) physical libration of the Moon,modeled asa solid body with tidal and rotational distortion,including both elastic and dissipational effects,(g) the effect upon the Moon's motion caused by tides raised upon the Earth by the Moon and Sun, and (h)the perturbations of 3Oo asteroids upon the motions of Mars,the Earth,and the Moon.

# 8.3.1 Point-Mass Interactions

The principal gravitational force on the nine planets,the Sun,and the Moon is modeled by considering those bodies to be point masses in the isotropic,parametrized post-Newtonian (PPN) $n$ -bodymetric (Will1974).The $n$ -body equationswerederivedbyEstabrook(1971b) from the variation of a time-independent Lagrangian action integral formulated ina nonrotating solar-system-barycentric Cartesian coordinate frame.Also included are Newtonian gravitational perturbations from 3Oo asteroids,chosen because they have the most pronounced effecton the Earth-Marsrange overthe time span coveredby the accurate spacecraft ranging observations.

For each body $i$ ,the point-mass acceleration is given by

$$
\begin{array} { r l } & { \hat { \mathbf { t } } _ { j _ { p o t r a m s } } = \displaystyle { \sum _ { j \neq i } \frac { \mu _ { j } ( \mathbf { r } _ { j } - \mathbf { r } _ { i } ) } { r _ { i j } ^ { 3 } } } \left\{ 1 - \frac { 2 ( \beta + \gamma ) } { c ^ { 2 } } \sum _ { k \neq j } \frac { \mu _ { k } } { r _ { i k } } - \frac { 2 \beta - 1 } { c ^ { 2 } } \sum _ { k \neq j } \frac { \mu _ { k } } { r _ { j k } } \right. } \\ & { \qquad + \left. \gamma \left( \frac { \eta _ { k } } { c } \right) ^ { 2 } + ( 1 + \gamma ) \left( \frac { v _ { j } } { c } \right) ^ { 2 } - \frac { 2 ( 1 + \gamma ) } { c ^ { 2 } } \hat { \mathbf { t } } _ { i } \cdot \hat { \mathbf { t } } _ { j } } \\ & { - \frac { 3 } { 2 c ^ { 2 } } \left[ \frac { ( \mathbf { r } _ { i } - \mathbf { r } _ { j } ) \cdot \hat { \mathbf { t } } _ { j } } { r _ { i j } } \right] ^ { 2 } + \frac { 1 } { 2 c ^ { 2 } } ( \mathbf { r } _ { j } - \mathbf { r } _ { i } ) \cdot \tilde { \mathbf { t } } _ { j } \right\} } \\ & { \qquad + \frac { 1 } { c ^ { 2 } } \displaystyle { \sum _ { j \neq i } \frac { \mu _ { j } ( \mathbf { r } _ { i } - \mathbf { r } _ { j } ) } { r _ { i j } ^ { 3 } } } \left\{ ( \mathbf { r } _ { i } - \mathbf { r } _ { j } ) \cdot [ ( 2 + 2 \gamma ) \hat { \mathbf { t } } _ { i } - ( 1 + 2 \gamma ) \mathbf { \hat { t } } _ { j } ] ( \hat { \mathbf { t } } _ { i } - \hat { \mathbf { t } } _ { j } ) \right. } \\ & { \qquad \left. + \frac { ( 3 + 4 \gamma ) } { 2 c ^ { 2 } } \displaystyle { \sum _ { j \neq i } \frac { \mu _ { j } \tilde { \mathbf { r } } _ { j } } { r _ { i j } } } + \sum _ { n = 1 } ^ { 3 } \frac { \mu _ { n } ( \mathbf { r } _ { n } - \mathbf { r } _ { i } ) } { r _ { n i } ^ { 3 } } + \sum _ { \ell , n = 1 } ^ { 5 } \mathbf { F } \right. } \end{array}
$$

where $\mathbf { r } _ { i }$ ， $\dot { \mathbf { r } } _ { i }$ ,and $\ddot { \mathbf { r } _ { i } }$ are the solar-system-barycentric position,velocity,and acceleration vectors of body $i ; \mu _ { j } = G m _ { j }$ ，where $G$ is the gravitational constant and $m _ { j }$ is the mass of body $j$ $; r _ { i j } = | \mathbf { r } _ { j } - \mathbf { r } _ { i } | ;$ $\beta$ is the PPN parameter measuring the nonlinearity in superposition of gravity; $\gamma$ is the PPN parameter measuring space curvature produced by unit rest mass (in this integration,as in general relativity, $\beta = \gamma = 1 )$ ； $v _ { i } = | \dot { \mathbf { r } } _ { i } |$ ;and $c$ is the velocity of light.

The quantity $\ddot { \mathbf { r } _ { j } }$ appearing in two terms on the right-hand side of Eq.8.1 denotes the barycentric acceleration of each body $j$ due to Newtonian effects of the remaining bodies and the asteroids.Thus,the right-hand side of the equationis dependent upon the left-hand side,and so,rigorously,the computation should be iterated.However,use of Newtonian accelerations for these terms is sufficiently accurate.

In the next-to-last term on the right-hand side of Eq.8.1,quantities employing the index $m$ refer to the“Big3”asteroids,Ceres,Pallas,and Vesta.The last termrepresents forces upon the Earth,Moon,and Mars,only,from 297 other asteroids,grouped according to three taxonomic classes (C,S,M).The asteroid forces were computed in the following way:

·The orbitsof the Big3asteroidswere integrated under the forces of themselves, the nine planets,the Sun,and the Moon,using initial conditions from the dastcom filemaintained by JPL'sSolar SystemDynamics Group.These orbitswere fitwith Chebychev polynomials and used in the succeeding integration of the 297 non-Big 3 asteroids.For the eventual integration ofDE4O5,periodic mean orbitswere used for theBig 3asteroidswhich had been fit to their integrated orbits.

·The 297 individual orbits were integrated under the gravitational forces of the Sun, planets,and the Big 3asteroids.At each step,the force vectors of these non-Big 3 asteroids upon the Earth,Moon and Mars were computed,summed,and stored in 3 temporary files,one for the sums of the $2 1 8 \mathrm { { C } }$ -classasteroids,oneforthe sums ofthe 58 S-type asteroids,and one for the sums of the $^ { 2 1 \mathrm { ~ M ~ } }$ -type asteroids.Also stored in the same temporary files were the contributions from these non-Big 3asteroids to the solarsystem'scenter of mass.The vectors from these temporary fileswere fitwith Chebychev polynomialsand stored in a final file to be used inthe main planetary and lunar integration.

·The radii, masses,and taxonomic classes of the 297 asteroids used in DE405/LE405 are listed in $\ S \ 8 . 8$ .

# 8.3.2Solar System Barycenter

In the $n$ -bodymetric,all dynamical quantitiesare expressed with respect toacenter of mass whose definition is modified from the usual Newtonian formulation.The solar system barycenter is given by Estabrook(1971a) as

$$
\sum _ { i } \mu _ { i } ^ { * } \mathbf { r } _ { i } = 0
$$

where

$$
\mu _ { i } ^ { * } = \mu _ { i } \left\{ 1 + \frac { 1 } { 2 c ^ { 2 } } v _ { i } ^ { 2 } - \frac { 1 } { 2 c ^ { 2 } } \sum _ { j \neq i } \frac { \mu _ { j } } { r _ { i j } } \right\}
$$

and where $\mu _ { i }$ is the gravitational constant times the mass of the $i ^ { \mathrm { { t h } } }$ body; $v _ { i }$ is the barycentric speed of the $i ^ { \mathrm { t h } }$ body.

During the process of numerical integration the equations of motion for only the Moon and planetswere actually evaluated and integrated.The barycentric positionand velocity of the Sun were obtained from the equations of the barycenter.It should be noted that each of the two barycenter equations depends upon the other,requiring an iteration during the evaluation of the solar position and velocity.

# 8.3.3 Figure Effects

Long-term accuracy of the integrated lunar orbit requires the inclusion of the figures of the Earth,Moon,and Sun in the mathematical model.In DE4O5 the gravitational effects due to figures include:

1.The force of attraction between the zonal harmonics (through fourth degree) of the Earth andthepoint-mass Moon,Sun,Venus,andJuiter;   
2.the force of atraction between the zonal harmonics (through fourth degree) and the second- through fourth-degree tesseral harmonics of the Moon and the point-mass Earth,Sun,Venus,andJupiter;

3.The dynamical form-factorof the Sun( $[ J _ { 2 } )$ .

The contribution to the inertial acceleration of an extended bodyarising from the interaction of its own figure with an external point mass is expressed in the $\xi \eta \zeta$ coordinate system, where the $\xi$ -axis is directed outward from the extended body to thepoint mass；the $\xi \zeta$ - plane contains the figure (rotational) pole of the extended body,and the $\eta$ -axis completes the right-handed system.

In that system (see,e.g.,Moyer 1971),

$$
\begin{array} { r l r }   { [ \begin{array} { c } { \vec { \xi } } \\ { \vec { \eta } } \\ { \vec { \zeta } } \end{array} ] = - \frac { \mu } { r ^ { 2 } } \{ \begin{array} { l l } { n _ { 1 } } \\ { \sum _ { n = 2 } ^ { n } J _ { n } ( \frac { \mathcal { R } } { r } ) ^ { n } [ \begin{array} { c } { ( n + 1 ) P _ { n } ( \sin \phi ) } \\ { 0 } \\ { - \cos \phi P _ { n } ^ { \prime } ( \sin \phi ) } \end{array} ]  } } \\ & { } & {  + \sum _ { n = 2 } ^ { n _ { 2 } } ( \frac { \mathcal { R } } { r } ) ^ { n } \sum _ { m = 1 } ^ { n } [ \begin{array} { c } { - ( n + 1 ) P _ { n } ^ { m } ( \sin \phi ) [ + C _ { n m } \cos m \lambda + S _ { n m } \sin m \lambda ] } \\ { m \sec \phi P _ { n } ^ { m } ( \sin \phi ) [ - C _ { n m } \sin m \lambda + S _ { n m } \cos m \lambda ] } \\ { \cos \phi P _ { n } ^ { m \prime } ( \sin \phi ) [ + C _ { n m } \cos m \lambda + S _ { n m } \sin m \lambda ] } \end{array} ] \} } \end{array} \end{array}
$$

where $\mu$ is the gravitational constant $G$ times the mass of the point body; $r$ is the centerof-mass separation between the two bodies; $n _ { 1 }$ and $n _ { 2 }$ are the maximum degrees of the zonal and tesseral expansions,respectively; $P _ { n } ( \sin \phi )$ istheLegendrepolynomial of degree $n$ $P _ { n } ^ { m } ( \sin \phi )$ is the associated Legendre function of degree $n$ and order $m$ ； $J _ { n }$ is the zonal harmonic for the extended body; $C _ { n m }$ , $S _ { n m }$ are thetesseral harmonics for the extended body; $_ { \mathcal { R } }$ is the equatorial radius of the extended body; $\phi$ is the latitude of the point mass relative to the body-fixed coordinate systemin which the harmonics are expressed;and $\lambda$ is the east longitude of the point mass in the same body-fixed coordinate system.

The primes denote differentiation with respect to the argument sin $\phi$ .Theaccelerations are transformed into the solar-system-barycentric Cartesian system by application of the appropriate rotation matrix.

Theinteraction between the figure of anextended body anda point mass also induces an inertial acceleration of the point mass.If $\ddot { \mathbf { r } } _ { f i g }$ denotes the acceleration given in Eq.8.3 when expressed in solar-system-barycentric coordinates,then the corresponding acceleration of the point mass, $\ddot { \mathbf { r } } _ { p m }$ ,is

$$
\ddot { \mathbf { r } } _ { p m } = - \frac { m _ { f i g } } { m _ { p m } } \ddot { \mathbf { r } } _ { f i g }
$$

where $m _ { f i g }$ and $m _ { p m }$ are the masses of the extended body and point mass,respectively.

The orientation of the Earth includes precession,obliquity change (Lieske et al.1977), and18.6-year nutation. The correction for precession, $d \Phi _ { Y } / d t$ ,was setto $0 ^ { \prime \prime } 1 1 9 3 /$ cy $\Delta p =$ $- 0 . 3 / \mathrm { c y } )$ ,and the obliquity rate correction, $d \Phi _ { X } / d t$ ,was taken from (Williams 1994).In addition,offsets to the Earth'sorientationat J2000.0, $\Phi _ { X }$ and $\Phi _ { Y }$ ,were determined through thestrength of the lunar laser rangingdata.Thevalues forallfour parameters are given in Table 8.4.

# 8.3.4 Lunar Gravity Coefficients

For the Moon, the $2 ^ { \mathrm { n d } }$ degree gravity field is time-varying,and the harmonic gravity coefficients are computed from the moment-of-inertia tensor,where the time dependence has been accounted for. For near principal axis alignment, the $1 ^ { \mathrm { s t } }$ order relations for the coefficients

are given by

$$
\begin{array} { l } { J _ { 2 } ^ { m } ( t ) = \frac { I _ { 3 3 } ( t ) - \frac { 1 } { 2 } [ I _ { 1 1 } ( t ) + I _ { 2 2 } ( t ) ] } { m { \mathcal R } ^ { 2 } } } \\ { C _ { 2 2 } ^ { m } ( t ) = \frac { I _ { 2 2 } ( t ) - I _ { 1 1 } ( t ) } { 4 m { \mathcal R } ^ { 2 } } } \\ { C _ { 2 1 } ( t ) = - I _ { 1 3 } ( t ) / m { \mathcal R } ^ { 2 } } \\ { S _ { 2 1 } ( t ) = - I _ { 3 2 } ( t ) / m { \mathcal R } ^ { 2 } } \\ { S _ { 2 2 } ( t ) = - I _ { 2 1 } ( t ) / 2 m { \mathcal R } ^ { 2 } } \end{array}
$$

where the $I _ { i j }$ are the components of the moment-of-inertia tensor,to be described later; $m$ is the lunar mass and $_ { \mathcal { R } }$ ,thelunar radius.

# 8.3.5Lunar Physical Libration:Coordinates

The orientation of the Moonis given by aset of Euler angles, $\phi , \theta$ ,and $\psi$ ,which relate the Moon-centered,rotating lunar system to the reference frame of the ephemerides (nominally, theICRF).The elastic Moon is distortedby tides and rotation,butthe mean principal axes are well-defined.This Moon-centered mean-principal-axis frameis herecalled the selenographic frame.The angles are $\phi$ ,theangle from the $x$ -axis of the ephemeris reference framealong the $x y$ -plane to the intersection of the lunar equator; $\theta$ ,the inclination of the lunar equator upon the $x y$ -plane;and $\psi$ ,the longitude from that intersection along the lunar equatorto the prime meridian.

Instead of integrating the second derivatives of the Euler angles,their first derivatives are expressed in terms of the selenocentric,body-fixed angular velocity vector, $\omega$ ：

$$
\begin{array} { r l } & { \dot { \phi } = ( \omega _ { x } \sin \psi + \omega _ { y } \cos \psi ) / \sin \theta } \\ & { \dot { \theta } = \omega _ { x } \cos \psi - \omega _ { y } \sin \psi } \\ & { \dot { \psi } = \omega _ { z } - \dot { \phi } \cos \theta . } \end{array}
$$

The first derivatives of the Euler angles and the first derivatives of $\omega$ areintegrated,asseen in the following subsection.

# 8.3.6Physical Libration Differential Equations

The moment of inertia tensor, $\mathbf { I }$ ,has a rigid-body contribution plus two variable contributions due to tidal and rotational distortions.The distortions are functions of the lunar position and rotational velocities,computed at time, $t - \tau _ { m }$ ,where $\tau _ { m }$ isa time-lag of about 4 hours in DE405,as determined from the fitsto the lunar laser rangingdata.The time delay allows for dissipation when flexing the Moon (Williams et al.2001).

The angular momentum vector can be expressed in inertial or body-fixed coordinates; it is the product of the moment of inertia tensor(given in $\ S 8 . 3 . 7 )$ and the angular velocity vector: $\mathbf { L } = \mathbf { I } \ \omega$ .The time derivative of the angular momentum vector is equal to the torque.In an inertial coordinate system: ${ \bf N } = d { \bf L } / d t$ ,but inarotating system,

$$
\mathbf { N } = { \frac { d } { d t } } ( \mathbf { I } { \boldsymbol { \omega } } ) + { \boldsymbol { \omega } } \times \mathbf { I } { \boldsymbol { \omega } }
$$

where the second term on the right side puts the time derivative into the body-fixed system.

The complete equation of motion forthe lunar librations is then given by

$$
\dot { \boldsymbol { \omega } } = \mathbf { I } ^ { - 1 } \{ \Sigma _ { i } \mathbf { N } _ { f i g - p m } \mathbf { \Omega } + \mathbf { N } _ { f i g - f i g } \mathbf { \Omega } - \dot { \textbf { I } } \boldsymbol { \omega }  - \boldsymbol { \omega } \times \mathbf { I } \boldsymbol { \omega } \}
$$

where the torques have been separated into the sums of the torques upon the lunar figure from external point masses, $i$ ,and from theEarth'sextended figure.These are discussed later in the section.

# 8.3.7 The Moment of Inertia Tensor

The three parts of the moment of inertia tensor represent the rigid body,the tidal distortion, andthe spin distortion,where the latter two include both elasticity and dissipation.The bodyfixed selenographic reference frame uses the rigid body principal axes.In this frame,the tensoris

$$
{ \begin{array} { r l } & { \mathbf { I } = { \left[ \begin{array} { l l l } { A } & { 0 } & { 0 } \\ { 0 } & { B } & { 0 } \\ { 0 } & { 0 } & { C } \end{array} \right] } } \\ & { \quad - { \frac { k _ { 2 n } m _ { e } R _ { m } ^ { 5 } } { r ^ { 5 } } } { \left[ \begin{array} { l l l l } { x ^ { 2 } - { \frac { 1 } { 3 } } r ^ { 2 } } & { x y } & { x z } \\ { } & { x y } & { y ^ { 2 } - { \frac { 1 } { 3 } } r ^ { 2 } } & { y z } \\ { } & { x z } & { y z } & { z ^ { 2 } - { \frac { 1 } { 3 } } r ^ { 2 } } \end{array} \right] } } \\ & { \quad + { \frac { k _ { 2 n } R _ { m } ^ { 5 } } { 3 G } } { \left[ \begin{array} { l l l l } { \omega _ { x } ^ { 2 } - { \frac { 1 } { 3 } } ( \omega ^ { 2 } - n ^ { 2 } ) } & { \omega _ { x } \omega _ { y } } & { \omega _ { x } \omega _ { z } } \\ { } & { \omega _ { x } \omega _ { y } } & { \omega _ { y } ^ { 2 } - { \frac { 1 } { 3 } } ( \omega ^ { 2 } - n ^ { 2 } ) } & { \omega _ { y } \omega _ { z } } \\ { } & { \omega _ { x } \omega _ { z } } & { \omega _ { y } \omega _ { z } } & { \omega _ { z } ^ { 2 } - { \frac { 1 } { 3 } } ( \omega ^ { 2 } + 2 n ^ { 2 } ) } \end{array} \right] } } \end{array} }
$$

where the coordinates and rotational velocities, $\mathbf { r }$ and $\omega$ ,areevaluatedat time $t - \tau _ { m }$ ,and where $k _ { 2 m }$ is the lunar potential Love number; $m _ { e }$ is the mass of the Earth; $R _ { m }$ is the equatorial radius of the Moon; $r$ is the Earth-Moon distance; $x$ , $y$ , $z$ are the components of the Earth-Moonvectoraligned with the rigid body principal axes; $\omega _ { x }$ , $\omega _ { y }$ , $\omega _ { z }$ are the components of $\omega$ in the selenographic system;and $n$ isthe average lunar mean motion.

# 8.3.8Time Derivative of the Inertia Tensor

$$
\begin{array} { r l } & { \mathbf { f } = \frac { 5 k _ { 2 n } m _ { e } R _ { n } ^ { 5 } } { r ^ { 7 } } \cdot \hat { \mathbf { r } } [ \begin{array} { l l l } { x ^ { 2 } - \frac { 1 } { 3 } r ^ { 2 } } & { x y } & { x z } \\ { x y } & { y ^ { 2 } - \frac { 1 } { 3 } r ^ { 2 } } & { y z } \\ { x z } & { y z } & { z ^ { 2 } - \frac { 1 } { 3 } r ^ { 2 } } \end{array} ] } \\ & { \quad - \frac { k _ { 2 n } m _ { e } R _ { n } ^ { 5 } } { r ^ { 5 } } [ \begin{array} { l l l } { 2 ( x \dot { x } - \frac { 1 } { 3 } \mathbf { r } \cdot \mathbf { t } ) } & { x \dot { y } + \dot { x } y } & { x \dot { z } + \dot { x } z } \\ { x \dot { y } + \dot { x } y } & { 2 ( y \dot { y } - \frac { 1 } { 3 } \mathbf { r } \cdot \mathbf { t } ) } & { y \dot { z } + \dot { y } z } \\ { x \dot { z } + \dot { x } z } & { y \dot { z } + \dot { y } z } & { 2 ( z \dot { z } - \frac { 1 } { 3 } \mathbf { r } \cdot \mathbf { t } ) } \end{array} ] } \\ &  \quad + \frac { k _ { 2 n } R _ { m } ^ { 5 } } { 3 G } [ \begin{array} { l l l } { 2 ( \omega _ { x } \dot { \omega } _ { x } - \frac { 1 } { 3 } \omega \cdot \dot { \omega } ) } & { \omega _ { x } \dot { \omega } _ { y } + \dot { \omega } _ { x } \omega _ { y } } & { \omega _ { x } \dot { \omega } _ { z } + \dot { \omega } _ { x } \omega _ { z } } \\ { \omega _ { x } \dot { \omega } _ { y } + \omega _ { x } \omega _ { y } } & { 2 ( \omega _ { y } \dot { \omega } _ { y } - \frac { 1 } { 3 } \omega \cdot \dot { \omega } ) } & { \omega _ { y } \dot { \omega } _ { z } + \dot { \omega } _ { y } \omega _ { z } } \\ { \omega _ { x } \dot { \omega } _ { z } + \dot { \omega } _ { x } \omega _ { z } } & { \omega _ { y } \dot { \omega } _ { z } + \dot { \omega } _ { y } \omega _ { z } } &  2 ( \omega _ { z } \dot { \omega } _ { z } - \frac { 1 } { 3 } \end{array} \end{array}
$$

# 8.3.9Principal Moments

The rigid-body principal moments are $A$ ， $B$ ,and $c$ ,with the $c$ axis aligned toward the pole.

$$
\begin{array} { r l } & { A = \cfrac { 2 ( 1 - \beta _ { L } \gamma _ { L } ) } { ( 2 \beta _ { L } - \gamma _ { L } + \beta _ { L } \gamma _ { L } ) } M _ { m } \mathcal { R } _ { m } ^ { 2 } J _ { 2 } ^ { \mathrm { r i g i d } } } \\ & { B = \cfrac { 2 ( 1 + \gamma _ { L } ) } { ( 2 \beta _ { L } - \gamma _ { L } + \beta _ { L } \gamma _ { L } ) } M _ { m } \mathcal { R } _ { m } ^ { 2 } J _ { 2 } ^ { \mathrm { r i g i d } } } \\ & { C = \cfrac { 2 ( 1 + \beta _ { L } ) } { ( 2 \beta _ { L } - \gamma _ { L } + \beta _ { L } \gamma _ { L } ) } M _ { m } \mathcal { R } _ { m } ^ { 2 } J _ { 2 } ^ { \mathrm { r i g i d } } } \end{array}
$$

$\beta _ { L }$ $\gamma _ { L }$ $\beta _ { L } = ( C - A ) / B$ $\gamma _ { L } = ( B - A ) / C$ $a _ { m }$ $\begin{array} { r } { J _ { 2 } ^ { \mathrm { r i g i d } } = J _ { 2 } ^ { \mathrm { i n p u t } } + k _ { 2 m } \frac { M _ { e } } { M _ { m } } \left( \frac { \mathcal { R } _ { m } } { a _ { m } } \right) ^ { 3 } } \end{array}$ $J _ { 2 } ^ { \mathrm { i n p u t } }$ doesnotep $J _ { 2 } ^ { \mathrm { i n p u t } } , \beta _ { L } , \gamma _ { L } , \mu _ { m }$ the $3 ^ { r d }$ degree harmonics, $k _ { 2 m }$ ,and $\tau _ { m }$ are quantities which are solved for in the least-squares data fits and then input into the integration program; $\mathcal { R } _ { m }$ and the $4 ^ { t h }$ degree harmonics are input, but not solvedforA,B,Candid arederived from the preceding relations.For furtherdiscussion, see Newhall and Williams (1997).

# 8.3.10 Figure-Point Mass Torques upon the Moon

Froma single point-mass (body）acting upon the figure of the Moon,the lunar torque is given by

$$
{ \bf N } _ { f i g - p m } = M _ { m } { \bf r } _ { p m } \times \ddot { \bf r } _ { f i g }
$$

where $\mathbf { r } _ { p m }$ is the selenocentric position of the point mass and $\ddot { \mathbf { r } } _ { f i g }$ is the inertial acceleration due to the point-mass.Torques are computed for the figure of the Moon interacting with the Earth,Sun,Venus,andJupiter.

# 8.3.11Figure-Figure Torque upon the Moon

Yoder(1979) and Eckhardt (1981) showed that figure-figure torques are important for the Moon.Three significant terms of the torque upon the figure of the Moon from the Earth's figure( ${ \cal J } _ { 2 e } )$ are

$$
\begin{array} { l } { { \displaystyle { \bf N } _ { f i g - f i g } = \frac { 1 5 \mu _ { e } \mathcal { R } _ { e } ^ { 2 } J _ { 2 e } } { 2 r _ { e } ^ { 5 } } \left\{ ( 1 - 7 \sin ^ { 2 } \phi ) [ \hat { \bf r } _ { e } \times { \hat { \bf I } } \hat { \bf r } _ { e } ] \right. } \ ~ } \\ { { \displaystyle ~ + \left. 2 \sin \phi [ \hat { \bf r } _ { e } \times { \hat { \bf I } } \hat { \bf P } _ { e } + \hat { \bf P } _ { e } \times { \hat { \bf I } } \hat { \bf r } _ { e } ] \right. } \ ~ } \\  { \displaystyle ~ \left. - \frac { 2 } { 5 } [ \hat { \bf P } _ { e } \times { \hat { \bf I } } \hat { \bf P } _ { e } ] \right\} } \end{array}
$$

where $\hat { \mathbf { P } } _ { \mathrm { e } }$ is the direction vector of the Earth's pole and $\hat { \mathbf { r } } _ { \mathbf { e } }$ is the direction vector of the Earth fromtheMoon,both expressed in the selenographicreference frame; $\mathbf { I }$ is the lunar moment of inertia tensor; $\mathcal { R } _ { e }$ is the equatorial radius of the Earth in au’s;and for this equation, $\phi$ is defined by sin $\phi = \hat { \mathbf { r } } _ { \mathrm { e } } \cdot \hat { \mathbf { P } } _ { \mathrm { e } }$ .Figure-figure acceleration of the lunar orbit is not considered.

# 8.3.12 Acceleration of the Moon from Earth Tides

The tides raised upon the Earth by the Sun and Moon affect,in turn,the motion of the Moon. For this,let

$$
G ~ = ~ \mathrm { \ g r a v i t a t i o n a l { \ c o n s t a n t } }
$$

for the distorted body (in thiscase,the Earth),

M mass   
R = radius   
θ sidereal rotation rate   
k2j = frequency dependent Love numbers $j = 0$ ,1, $2 \Rightarrow$ slow zonal,diurnal,smidurl tides)   
τj=freqcyependenttiedelays（j=0,1,ooal,al,sidalidal dissipation)

for the perturbed body(in this case,the Moon),

$$
\begin{array} { l c l } { { m } } & { { = } } & { { \mathrm { m a s s } } } \\ { { { \bf r } } } & { { = } } & { { \mathrm { p o s i t i o n } ( \mathrm { c e n t e r e d o n } \mathrm { m a s s } { \bf M } ) } } \end{array}
$$

for thetide-raising body (in this case,the Moonand Sun),

$$
\begin{array} { l c l } { { m ^ { \prime } } } & { { = } } & { { \mathrm { m a s s } } } \\ { { { \bf r } ^ { \prime } } } & { { = } } & { { \mathrm { p o s i t i o n } ( \mathrm { c e n t e r e d o n } \mathrm { m a s s } { \bf M } ) } } \end{array}
$$

For each frequency band,back-date the position of the tide-raising body by the timedelay, $\tau _ { j }$ ,and rotate that vector,aboutthe distorted body'srotational pole,through the lag angle, $\dot { \theta } \tau _ { j }$ ,giving

$$
\mathbf { r } _ { j } ^ { * } = \mathcal { R } _ { 3 } ( \dot { \theta } \tau _ { j } ) \mathbf { r } ^ { \prime } ( t - \tau _ { j } ) .
$$

For the acceleration of the perturbed body with respect to the distorted body (Moon with respect to Earth),break $\mathbf { r }$ and $\mathbf { r } ^ { * }$ into equatorial and polar components (with respect to the distorted body): $\mathbf { r } = \pmb { \rho } + \mathbf { z }$ and $\mathbf { r } ^ { * } = \rho ^ { * } + \mathbf { z } ^ { * }$ .

$$
\begin{array} { r } { \ddot { \mathbf { r } } ( \mathrm { t i d e } ) = \displaystyle \frac { 3 } { 2 } \frac { G m ^ { \prime } ( 1 + \frac { m } { M } ) \mathcal { R } ^ { 5 } } { r ^ { 5 } } \left. \frac { k _ { 2 0 } } { r _ { 0 } ^ { 5 5 } } \left( [ 2 z _ { 0 } ^ { * 2 } \mathbf { z } + \rho _ { 0 } ^ { * 2 } \rho ] - \frac { 5 [ ( z z _ { 0 } ^ { * } ) ^ { 2 } + \frac { 1 } { 2 } ( \rho \rho _ { 0 } ^ { * } ) ^ { 2 } ] \mathbf { r } } { r ^ { 2 } } + r _ { 0 } ^ { * 2 } \mathbf { r } \right) \right. } \\ { \left. + \frac { k _ { 2 1 } } { r _ { 1 } ^ { * 5 } } \left( 2 [ ( \rho \cdot \rho _ { 1 } ^ { * } ) \mathbf { z } _ { 1 } ^ { * } + z z _ { 1 } ^ { * } \rho _ { 1 } ^ { * } ] - \frac { 1 0 z z _ { 1 } ^ { * } ( \rho \cdot \rho _ { 1 } ^ { * } ) \mathbf { r } } { r ^ { 2 } } \right) \right. \qquad \left. ( 8 . 1 3 \mathrm { e } ) \right. } \\ { \left. + \frac { k _ { 2 2 } } { r _ { 2 } ^ { * 5 } } \left( [ 2 ( \rho \cdot \rho _ { 2 } ^ { * } ) \rho _ { 2 } ^ { * } - \rho _ { 2 } ^ { * 2 } \rho ] - \frac { 5 [ ( \rho \cdot \rho _ { 2 } ^ { * } ) ^ { 2 } - \frac { 1 } { 2 } ( \rho \rho _ { 2 } ^ { * } ) ^ { 2 } ] \mathbf { r } } { r ^ { 2 } } \right) \right. } \end{array}
$$

Note that $\rho \rho _ { i } ^ { * } = | \rho | | \rho _ { i } ^ { * } |$ ;it isnot $\boldsymbol { \rho } \cdot \boldsymbol { \rho } _ { i } ^ { * }$ .The acceleration from both Sun- and Moon-raised tides is computed.Tidesraised on the Earth by the Moon do not influence themutual barycentric motion,and the effectof Sun-raised tides onthe barycentric motion isnot considered.The tidal acceleration due to tidal dissipation is implicit in the above acceleration. The explicit conversion of the three Love numbers and time delays to tidal $\dot { n }$ requires a separate theory.

# 8.4 The Numerical Integration of DE405/LE405

The numerical integration of Eqs.8.1,8.6,and 8.8 was carried out using a variable-step-size, variable-order Adams method (Krogh 1972).The actual order of the 33 equations at any instantis determined bya specified error bound and by the behaviorof backward differences ofaccelerations.

Ithas proved numerically more suitable to integrate the lunar ephemeris relative to the Earth rather than to the solar systembarycenter.The solar-system-barycentric Earth and Moon states arereplaced by the quantities $\mathbf { r _ { e m } }$ and $\mathbf { r _ { B } }$ ,givenby

$$
{ \bf r _ { e m } } = { \bf r _ { m } } - { \bf r _ { e } }
$$

and

$$
\mathbf { r _ { B } } = { \frac { \mu _ { e } \mathbf { r _ { e } } + \mu _ { m } \mathbf { r _ { m } } } { \mu _ { e } + \mu _ { m } } }
$$

where the subscripts $e$ and $m$ denote the Earth and Moon,respectively.Note that $\mathbf { r _ { e m } }$ is the difference of solar-system-barycentric vectors and is distinguished from a geocentric vector bytherelativistic transformation from thebarycenterto geocenter.(Thevector $\mathbf { r _ { B } }$ can be interpreted as representing the coordinates ofthe NewtonianEarth-Moon barycenterrelative to the solar system barycenter.It has no physical significance and does not appear in force calculations;itis solelyavehicle for improving thenumerical behaviorof the differential equations.)

# 8.4.1Estimated Integration Error

The method of error control used in the integration puts a limit on the absolute value of the estimated error in velocity of each equationat the end of every integration step.Step size andintegration orders were adjusted on the basis of estimated error.The limits selected for DE405 were $2 \times 1 0 ^ { - 1 7 }$ au/day in each component of the equations of motion for the planets and Moon, and $2 \times 1 0 ^ { - 1 5 }$ rad $\mathrm { d } ^ { - 1 }$ for each component of the libration equations.

Integrations prior to DE4o5 were performed ona Univac mainframe computer in double precision,witha 6O-bit mantissa;DE4O5was integrated on a VAX Alpha in quadruple precision.In all cases,the integration error has been significantly less than the estimated error resulting from the uncertainties in the adjustment of the initial conditions and constants tothe observational data.These latter errorsare discussed later in $\ S \ 8 . 9$ .

# 8.4.2 Adopted Constants

The integration requires the input of numerical values for a number of parameters. Some of these parameters,such as the initial positionsand velocitiesof the planetsandMoon,result from the least-squares fits and are different in each fit.Other parameters,such as some of the masses and the Earth's zonal harmonics,come from outside sources and are only rarely changed for these present purposes.Some parameters,such as the massof the Earth-Moon system,canbederived fromthe data,butforconvenience are changedonly whenstatistically significant improvements can be made over the standard values.The lists of initial conditions and constants are given in $\ S \ 8 . 8$

The list of the initial conditions and dynamical constants used in the integration of the equations of motion used for the creation of DE4O5 is given in $\ S \ 8 . 8$ .Also given in $\ S \ : 8 . 8$ is a list of constants used in the reduction of the observational data which were determined in the least-squares solution.

# 8.5 Observational Data Fitby the Planetary andLunar Ephemerides

Increating modern ephemerides,the majority of the effort is directed toward the setof observational data(measurements)to which the ephemeridesare fitand to the fiting process itself.This section describes the observational data used in the creation of DE4o5/LE405. These observational data and their references are available over the internet at URL[1].

Table 8.1 presents the different types of observational data fit byDE4O5,along with the time-span,thebodiesobserved,thecoordinates measured,the inherent accuracy,and the number of observations.These different sets of observations are discussed briefly here,with some of the unique features of their reductions presented in $\ S 8 . 7$ .References to the data can be found at URL[1].

# 8.5.1 Optical Data

Classical ephemerides over the past centuries have been based entirely upon optical observations:almost exclusively,meridian circle transit timings.With the advent of planetary radar, spacecraft missions,VLBI,etc.,the situation for the four inner planets has changed dramatically.

All of the optical observations for the Sun,Mercury,Venus,andMars were omitted from theleast-squares adjustment leading to DE4O5.The newer and more accurate data types determine these orbits far more accurately (by orders of magnitude)than do the optical data. Since relatively large systematic errors are known to remain in the optical observations,even afterthe many corrections described in Standish (199O),and since at that time there was a large uncertainty connected with theframe-tie between theFK5and ICRFreferenceframes, inclusionof the optical observations for the inner planets could have been detrimental fortheir ephemerides.Thus,the initial conditions for the inner four planets were adjusted to ranging data primarily,with the VLBI observations serving to orient the whole inner planetary system onto the ICRF.

For Jupiter,the initial conditions were fit to a number of different types of observations, not all of which seemed to be fully consistent with each other. Since that time,however, subsequent analyses of the Jupiter ephemeris,using more recent measurements from the Galileo spacecraft,indicate that the errors are no larger than about $1 5 0 \mathrm { k m } ( 0 \ddagger 0 5 )$

For the outermost four planets,the optical observations are effectively the only observations and are expected to remain so for a number of years.

# 8.5.2Meridian Transits

Transit observations are differential in nature—the planetary observations undergo the same processing as those of the observed stars,both being related to the standard catalog of the epoch.The observations are published as geocentric apparent right ascensions and declinations,taken at the time of meridian passage.For comparison,then,one obtains a computed position from the ephemerides by iterating to find the time at which the local apparent hour angle of the planet is zero.The formulation for computing apparent places is essentially identical to that described in Chapter 7.

# 8.5.3Photographic and CCD Astrometry

Photographic and CCDastrometric observations are handled inthe same way.The observations based upon the 195O reference frame(those of Pluto) were transformed onto the J2000.0 frame using the precession and equinox corrections of Fricke (1971,1982).Those based upon the (J2oo0.O)FK5 were then transformed onto the ICRF using preliminary corrections supplied by Morrison (1996).

# 8.5.4 Occultation Timings

The timings were supplied in normal point form-corrections to the specific ephemeris used in the reductions.The reductions were made by those modeling the Uranian rings and the Neptunian disk and transmitted to the authorby Nicholson (1992).

# 8.5.5 Astrolabe

Astrolabe observations are effectively timings of an object when its apparent altitude above the horizon attains a certain pre-determined value.These observations are described in Debarbat and Guinot (1970).

# 8.5.6Radiometric Emission Measurements

Theradiometric emission fromthe Jovianand Saturnian satellitesand from the disks of Uranus and Neptune were measured differentially against the then-existing radio reference catalogue,a precursor to the IERS (International Earth Rotation and Reference system Service)Radio Catalogue,which is itself the precursor of the ICRF.The observations were takenattheVeryLargeArray(VLA) inSoccoro,NewMexico byMuhlemanetal.(1985), Muhleman,Berge,andRudy (1986) Muhleman,Berge,and Jones (1988)and byBerge, Muhleman,and Linfield (1988).They are presented in normal point form- corrections to the specific ephemeris used in the reductions.

# 8.5.7 Ranging Data

Arange measurement is the actual round-trip time of the electromagnetic signal from when itleaves the transmitter until the time it arrives at thereceiver.The signal is returned froma spacecraft transponderorfromaplanet,having bounced off of a spot on the surface where the normal to the surface points toward the Earth.The timing is done at the antennaeby atomic clocks in what maybe considered UTC.

Theranging observations reflected from the surface ofMercury,Venus,orMars,are accurate toalevelof about1OO meters.However,for ephemerispurposes,variations in the topography of a planet'ssurface introducea noise-like uncertainty.This enters directly into the process of deducing the distance from the spot on the surface to the center of mass of the planet.Methods to reduce these uncertainties are described in $\ S 8 . 7$ .

Table8.1 Observational data fit by DE405.The columns contain the observatory/source,the time coverage,thebodiesmeasured,thecomponentsmeasured,theaprioriuncertaintiesofameasurement, the number of observationsand the group totals.   

<table><tr><td colspan="7"></td></tr><tr><td>Observatory</td><td>years</td><td>bodies</td><td>coords.</td><td>apriori sigmas</td><td>#</td><td>group totals</td></tr><tr><td colspan="7">OpticalMeridian Transits</td></tr><tr><td>Washington</td><td>1911-1994</td><td>Sun,...,Nep</td><td>r.a.,dec.</td><td>1:'0/0'5</td><td>14242</td><td></td></tr><tr><td>Herstmonceux</td><td>1957-1982</td><td>Sun,...,Nep</td><td>r.a.,dec.</td><td>1"0/0"5</td><td>2851</td><td>17093</td></tr><tr><td colspan="7">PhotoelectricMeridian Transits</td></tr><tr><td>La Palma</td><td>1984-1993</td><td>Mar,...,Plu</td><td>r.a.,dec.</td><td>0.25</td><td>6410</td><td></td></tr><tr><td>Bordeaux</td><td>1985-1996</td><td>Sat,Ura,Nep</td><td>r.a.,dec.</td><td>025</td><td>854</td><td></td></tr><tr><td>Tokyo</td><td>1986-1988</td><td>Mar,...,Nep</td><td>r.a.,dec.</td><td>05</td><td>498</td><td></td></tr><tr><td>Flagstaff- USNO</td><td>1995</td><td>Plu</td><td>r.a.,dec.</td><td>01</td><td>20</td><td>7782</td></tr><tr><td colspan="7">Photographic Astrometry of Pluto</td></tr><tr><td>(Pre-disc)</td><td>1914-1927</td><td>Pluto</td><td>r.a.,dec.</td><td>0.'5</td><td>28</td><td></td></tr><tr><td>Lowell</td><td>1930-1951</td><td></td><td></td><td></td><td>620</td><td></td></tr><tr><td>Yerkes-McD</td><td>1930-1953</td><td></td><td></td><td></td><td>310</td><td></td></tr><tr><td>(Nrml pts.)</td><td>1930-1958</td><td></td><td></td><td></td><td>66</td><td></td></tr><tr><td>MacDonald</td><td>1949-1953</td><td></td><td></td><td></td><td>56</td><td></td></tr><tr><td>Yerkes</td><td>1962-1963</td><td></td><td></td><td></td><td>42</td><td></td></tr><tr><td>Palomar</td><td>1963-1965</td><td></td><td></td><td></td><td>8</td><td></td></tr><tr><td>Dyer</td><td>1964-1981</td><td></td><td></td><td></td><td>44</td><td></td></tr><tr><td>Bordeaux</td><td>1967</td><td></td><td></td><td></td><td>24</td><td></td></tr><tr><td>Asiago</td><td>1969-1978</td><td></td><td></td><td></td><td>350</td><td></td></tr><tr><td>Torino</td><td>1973-1982</td><td></td><td></td><td></td><td>74</td><td></td></tr><tr><td>Copenhagen</td><td>1975-1978</td><td></td><td></td><td></td><td>150</td><td></td></tr><tr><td>Flagstaff</td><td>1980-1994</td><td></td><td></td><td></td><td>16</td><td></td></tr><tr><td>Lick</td><td>1980-1985</td><td></td><td></td><td></td><td>56</td><td></td></tr><tr><td>La Silla</td><td>1988-1989</td><td></td><td></td><td></td><td>58</td><td>1902</td></tr><tr><td colspan="7">CCDAstrometry of Uranus,Neptune and Pluto</td></tr><tr><td>Flagstaff-USNO</td><td>1995-1996</td><td>Ura,Nep</td><td>r.a., dec.</td><td>0"20</td><td>313</td><td></td></tr><tr><td>Flagstaff -USNO</td><td>1995-1996</td><td>Plu</td><td>r.a.,dec.</td><td>0"20</td><td>63</td><td></td></tr><tr><td>Bordeaux</td><td>1995-1996</td><td>Plu</td><td>r.a., dec.</td><td>0"20</td><td>13</td><td>389</td></tr><tr><td colspan="7">Occultation Timings</td></tr><tr><td>Uranus rings</td><td>1977-1983</td><td>Ura</td><td>r.a.,dec.</td><td>014</td><td>14</td><td></td></tr><tr><td>Neptune disk</td><td>1968-1985</td><td>Nep</td><td>r.a.,dec.</td><td>027</td><td>18</td><td>32</td></tr><tr><td colspan="7">Astrolabe</td></tr><tr><td>Quito</td><td>1969</td><td>Sat</td><td>r.a.,dec.</td><td>0.'3-1!'6</td><td>1</td><td></td></tr><tr><td>Algiers</td><td>1969-1973</td><td>Mar,Sat</td><td></td><td></td><td>48</td><td></td></tr><tr><td>San Fernando</td><td>1970-1978</td><td>Mar,Jup,Sat</td><td></td><td></td><td>338</td><td></td></tr><tr><td>Besangon</td><td>1971-1973</td><td>Sat</td><td></td><td></td><td>44</td><td></td></tr><tr><td>Paris</td><td>1971-1978</td><td>Mar,Sat</td><td></td><td></td><td>146</td><td></td></tr><tr><td>OCA</td><td>1972-1981</td><td>Mar,Jup,Sat</td><td></td><td></td><td>202</td><td></td></tr><tr><td>Santiago</td><td>1975-1985</td><td>Ura</td><td></td><td></td><td>284</td><td>1063</td></tr><tr><td>Observatory</td><td>years</td><td>bodies</td><td>coords.</td><td>apriori sigmas</td><td>#</td><td>group totals</td></tr><tr><td colspan="7">RadarRanging</td></tr><tr><td>Arecibo</td><td>1967-1982</td><td>Mer,Ven</td><td>range</td><td>10km</td><td>284</td><td></td></tr><tr><td>Haystack</td><td>1966-1971</td><td>Mer,Ven</td><td></td><td>1.5</td><td>188</td><td></td></tr><tr><td>Goldstone13</td><td>1964-1970</td><td>Ven</td><td></td><td>1.5</td><td>9</td><td></td></tr><tr><td>Gldstn 13-14</td><td>1970-1977</td><td>Mer,Ven</td><td></td><td>1.5</td><td>23</td><td></td></tr><tr><td>Goldstone14</td><td>1970-1993</td><td>Mer,Ven</td><td></td><td>1.5</td><td>376</td><td>880</td></tr><tr><td colspan="7">MarsRadar-Ranging Closure Points</td></tr><tr><td>Goldstone14</td><td>1971-1993</td><td>Mars</td><td>diff. range</td><td>1.5</td><td>65</td><td>65</td></tr><tr><td colspan="7">Radio Astrometry of Thermal Emission</td></tr><tr><td>VLA</td><td>1987</td><td>Jup,...,Nepr.a.,dec.</td><td></td><td>0'03-0"1</td><td>10</td><td>10</td></tr><tr><td colspan="7">Spacecraft Measurements</td></tr><tr><td>Mariner9</td><td>1971-1972</td><td>Mars</td><td>range</td><td>35-120m</td><td>629</td><td></td></tr><tr><td>Pioneer 10</td><td>1973</td><td>Jupiter</td><td>range</td><td>3km</td><td>1</td><td></td></tr><tr><td>Pioneer 11</td><td>1974</td><td></td><td></td><td>12 km</td><td>1</td><td></td></tr><tr><td>Viking Lander</td><td>1976-1980</td><td>Mars</td><td>range</td><td>7m</td><td>1018</td><td></td></tr><tr><td></td><td>1980-1981</td><td></td><td></td><td>12m</td><td>264</td><td></td></tr><tr><td>Voyager1OD</td><td>1979</td><td>Jupiter</td><td>r.a.,dec.</td><td>0'01,0.05</td><td>2</td><td></td></tr><tr><td></td><td></td><td></td><td>range</td><td>3km</td><td>1</td><td></td></tr><tr><td>Voyager 2 OD</td><td>1979</td><td></td><td>range</td><td>3km</td><td>1</td><td></td></tr><tr><td>Phobos OD</td><td>1989</td><td>Mars</td><td>range</td><td>0.5km</td><td>1</td><td></td></tr><tr><td>Phobos VLBI</td><td>1989</td><td>Mars</td><td>r.a., dec.</td><td>0.'01-0"1</td><td>2</td><td></td></tr><tr><td>Ulysses VLBI&amp;OD</td><td>1992</td><td>Jupiter</td><td>r.a.,dec.</td><td>0'003,0"006</td><td>2</td><td></td></tr><tr><td></td><td></td><td></td><td>range</td><td>3km</td><td>1</td><td></td></tr><tr><td>Magellan VLBI</td><td>1990-1994</td><td>Venus</td><td>r.a.,dec.</td><td>0.003-0'01</td><td>18</td><td></td></tr><tr><td>Galileo OD</td><td>1995</td><td>Jupiter</td><td>r.a.,dec.</td><td>0.'05,0."2</td><td>2</td><td></td></tr><tr><td></td><td></td><td></td><td>range</td><td>20km</td><td>1</td><td>1956</td></tr><tr><td colspan="7">Frame-TieDetermination</td></tr><tr><td>ICRF frame-tie</td><td>1988</td><td>Earth</td><td>h</td><td>0"003</td><td>6</td><td>6</td></tr><tr><td>Lunar Laser Ranging</td><td></td><td>Moon</td><td>range</td><td>2-30cm</td><td>11218</td><td>11218</td></tr><tr><td colspan="7"></td></tr><tr><td>Nominal Values</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td></tr><tr><td>Total</td><td></td><td></td><td></td><td></td><td></td><td>42410</td></tr></table>

Ranging observations to spacecraft can be accurate to a level of onlyacouple of meters, though these observations are also affected by a number of factors,including the delay of thesignal through the solar corona,delays in the electronic circuitry,and uncertainties in the spacecraft’s position—either from orbital uncertainties or from a lander's position on a planet’srotating surface.

In any case,the computations of all ranging measurements are very similar. The formulation is given in $\ S 8 . 7$

# 8.5.8 Orbiter Range Points

Orbiterrange points are received in the formof normal points,a representation of modified distance measurements.The original round-trip range and Dopplermeasurements are reduced usingtheJPL OrbitDeterminationProgram(Moyer1971).This reductionisanadjustment for all relevant parameters,except for those of the planetary ephemeris,including the spacecraft orbit,the planet’s mass and gravity field,etc.As such,the resultant range residualsrepresent derived corrections to the nominal planetary ephemeris usedin the reduction.These residuals arethen added to the geometric (instantaneous Earth-planet) range inorder to givea pseudo “observed”range point.

References for the sources of the normal points are given in the website URL[1].

# 8.5.9 Lander Range Data

Lander range data are two-way ranging measurements taken of landed spacecraft on the surface of aplanet.These dataare reduced using the formulae given in $\ S 8 . 7$ with the reflection point on theplanet’ssurface being representedby the locationof thelander on theplanet. For this,one needs the surface coordinates of the landers and the orientation of the planet in order to orient the lander into the ephemeris reference frame.

# 8.5.10 VLBI Data

VLBI measurements of a spacecraft with respect to background sources from aradio source catalogue may be combined with the planetocentric spacecraft trajectory in order to yield a positional determination of the planet with respect to the reference frame of the radio source catalogue.For DE4O5,there were two such points from the Phobos spacecraft nearing its encounter with Mars and18 from the Magellan spacecraft in its orbit around Venus.Venus is relatively free from the asteroid perturbations that introduce uncertainties into the ephemeris ofMars,so that its ephemeris can be more accurately projected in time.Therefore,the Venus orbit,(which connects Venus into the inner planetary system),inconjunction with the VLBIobservations of Venus,is important in orienting the inner planet system onto the radio frame.

# 8.5.11Lunar Laser Range Data

The Lunar LaserRange (LLR)dataconsist of time-of-flight measurements of the laser pulses from McDonald Observatory,Haleakala,orL'Observatoire de la Cote d'Azur(OCA) to any one of four retroreflectors on the Moon and back again.The retroreflectors are at the Apollo

11,14,and15landing sitesand on theLunokhod2 vehicle.In the solutions forDE4O5,there were11218 range points,distributed from1969 to 1996.

The LLR data are deposited in the National Space Science Data Center and the International Laser Ranging Service.During the least-squares fit the ranges have been weighted according to the instrumental errors that accompany each point.The simple post-fit rms residual in one-way range was about $3 0 \mathrm { c m }$ in 1970 and improved to about $3 \mathrm { c m }$ throughout the 1990's.

# 8.6The Orientation of DE405/LE405

Inthepast,the 195O-based ephemerides of JPL have been aligned onto the (1950) FK4 reference frame (Fricke and Kopf1963).Starting with DE2O0,the ephemerides were aligned onto their own mean equator and dynamical equinox of J2ooo.O (see Standish 1982).

The JPL planetary and lunar ephemerides starting with DE4Oo have been aligned onto the International Celestial ReferenceFrame (ICRF)—formerly,the IERS frame.This choice of the ICRF is advantageous for a number of reasons:

1.The ICRF is now the standard reference frame in astronomy.   
2.The timing and polar motion data used for the orientation of the Earth,distributed by theIERS,arenowreferred to theICRF.   
3.The ephemerides are now fittoa numberof VLBI observationswhich were referenced to the ICRF.Among all of the ephemeris observations which are explicitly given in a celestial reference system,these ICRF-based onesare themost accurate.   
4.The ICRFis stable;itis accessible；it will not show any net rotationwhen the coordinates are improved in the future.

# 8.6.1Adjustment of DE405 onto the ICRF Reference Frame

DE405 was adjusted to fit the ICRF-based VLBI observations of the Magellan Spacecraft orbiting Venus (18 points,1990-94)and of the Phobos Spacecraft as it approached Mars (2 points,1989) as described inthe previous section.These data servetoalign the ephemerides automatically onto the ICRF during the least-squaresadjustment.The inherent accuracy of each of these datapoints is about 3-1O milliarcseconds.

Ephemerides of the outer planets rely almost entirely upon optical observations.These were initially referenced to various stellar catalogues,then transformed onto the FK4 using the formulae of Schwan (1983),then onto the FK5 system by applying the equinox offset and motion parameters of Fricke(1982),and finally onto the ICRF using a tentative set of transformation tables supplied by Morrison (1996).

# 8.7Various Formulae Used in the Reduction of the Observational Data

In the course of reducing various types of observations,coming from many different sources, itis necessary to applyanumber of modeling formulae and corrections to the initially received measurements.This section presents some of the details.

# 8.7.1 Phase Corrections

For the planetary disk observations,the planet is usually not fully illuminated and therefore shows a crescent or gibbous disk.For the outer planets where the phase angle, $i$ ,isalways small,the following formula,chosensimply fromempirical considerations,wasapplied to the published transit observations:

$$
\begin{array} { r } { \left| \begin{array} { l } { \Delta \alpha } \\ { \Delta \delta } \end{array} \right| = \left| \begin{array} { l } { \sin \Theta } \\ { \cos \Theta } \end{array} \right| B _ { k } \sin 2 i } \end{array}
$$

where $i$ is the angle between the Earth and the Sun as seen from the planet; $\Theta$ is the position angle of the mid-point ofthe illuminated edge,measured clockwise from north.Phase corrections were of prime importance for the inner planets when their optical observations were included in earlier ephemerides.For the outer planets,the phase corrections for only Jupiter are of much significance.

# 8.7.2 Corrections to Precession and Equinox Drift

The optical residuals in right ascension and declination were reduced using the 1976 IAU (Fricke 1971,1982) values for precessionand equinox drift.More recent estimates for precession had indicated a further correction to the IAU value of $\Delta p = - 0 . 7 3 / \mathrm { c y }$ Also,any existing secular-like trends,such as equinox drift,were modeled by the quantity, $\Delta k$ ,using the standard formulae,

$$
\begin{array} { l } { \Delta \alpha = ( \Delta k + \Delta n \sin \alpha \tan \delta ) T _ { 2 0 0 0 } } \\ { \Delta \delta = ( \Delta n \cos \alpha ) T _ { 2 0 0 0 } } \end{array}
$$

where $T _ { 2 0 0 0 }$ is the time in centuries past J2000.0, $\Delta n = \Delta p$ sin $\varepsilon$ ,and $\varepsilon$ is the obliquity.

In DE405,the value of $\Delta p$ was set to $- 0 . { } ^ { \prime \prime } 3 / \mathrm { c y }$ ；thatfor $\Delta k$ was determined to be $- 0 . 7 0 6 2 / \mathrm { c y }$ in the solution.

# 8.7.3 Computation of Ranges

Arange measurement is the actual round-trip time of the electromagnetic signal from when it leaves the transmitter untilthe time it arrives at the receiver.The timing is doneby the (UTC) clockat theantenna;thus,the observationis essentially the $U T C$ times of transmission and of reception.

For an observation received at the time $t _ { R }$ (expressed in units of $\mathrm { T _ { e p h } }$ ,the time which is the independent variable of the equations of motion),the round-trip light-time is given by the difference $U T C ( t _ { R } ) - U T C ( t _ { R } - \tau _ { d } - \tau _ { u } )$ ,where

$$
\tau _ { u } = \vert \mathbf { r _ { B } } ( t _ { R } - \tau _ { d } ) - \mathbf { r _ { A } } ( t _ { R } - \tau _ { d } - \tau _ { u } ) \vert / c + \Delta \tau _ { u } [ r e l ] + \Delta \tau _ { u } [ c o r ] + \Delta \tau _ { u } [ t r o p o ]
$$

and

$$
\tau _ { d } = \vert \mathbf { r } _ { \mathrm { A } } ( t _ { R } ) - \mathbf { r } _ { \mathrm { B } } ( t _ { R } - \tau _ { d } ) \vert / c + \Delta \tau _ { d } [ r e l ] + \Delta \tau _ { d } [ c o r ] + \Delta \tau _ { d } [ t r o p o ]
$$

and where $\tau _ { u }$ and $\tau _ { d }$ are the light-times (in $\mathrm { T _ { e p h } }$ units）of the upleg and the downleg, respectively; $\mathbf { r } _ { \mathrm { A } }$ is the solar-system-barycentric position of the antenna on the Earth's surface;

$\mathbf { r _ { B } }$ isthe solar-system-barycentric position ofthe bouncepoint,eitheraresponding spacecraft or the reflection point on the planet's surface; $c$ is the velocity of light;and the three $\Delta \tau _ { \mathrm { ~ s ~ } } ^ { \prime }$ are the corrections to the light-times due to relativity,the electron content of the solar corona, and the Earth's troposphere,respectively.The two formulae are each solved iteratively,first for $\tau _ { d }$ then for $\tau _ { u }$

# 8.7.4 Antenna Location

The location of the antenna is computed in a straightforward manner using the proper formulae (precession,nutation,UT1,and polar motion) with which one orients the Earth,and inparticular the observing station,onto the ICRF,the reference frame ofthe ephemerides.The formulation was the same as that given by the IERS standards document of 2Oo3 (URL[2]). though the geological driftsof the stationswere being omitted during the time of DE405's creation.

# 8.7.5Time Delay for Relativity

The time-delay due to relativity,given by Shapiro (1964),is obtainedby integrating along the signal path over the value of the potential.For each leg of the signal path,the delay is given by the formula

$$
\Delta \tau _ { r e l } = \frac { ( 1 + \gamma ) G M } { c ^ { 3 } } \ln { \left| \frac { e + p + q } { e + p - q } \right| }
$$

where $\gamma$ is the PPN parameter of general relativity and where $e$ , $p$ ,and $q$ are the heliocentric distance of the Earth,the heliocentric distance of the planet,and the geocentric distance of the planet,respectively.These distances are evaluated at $t - \tau _ { d }$ for the planet, at $t - \tau _ { d } - \tau _ { u }$ for the Earth during the upleg,and at $t$ forthe Earth during the downleg.This formula has been augmented since the creation of DE405 (see Moyer (2Ooo)) in order to allow for the increased length of the signal path due to the path'sbending.Further,it is now necessary to apply this correction for not only the Sun's potential but also for that of Jupiter,since the latteralters Earth-Mars rangingby a meter or so.

# 8.7.6Time Delay for the Solar Corona

The delay from the solar corona (see Muhleman and Anderson 1981) is obtained by integrating along the signal path from point $P _ { 1 }$ to point $P _ { 2 }$ over the density of ionized electrons, $N _ { \mathrm { e } }$ $( \mathrm { c m } ^ { - 3 } )$ ，

$$
\Delta \tau _ { c o r } = \frac { 4 0 . 3 } { c f ^ { 2 } } \int _ { P _ { 1 } } ^ { P _ { 2 } } N _ { \mathrm { e } } d s
$$

where $c$ is the speed of light (cm/sec), $f$ is the frequency ( $\mathbf { H } \mathbf { z }$ ),and $\mathbf { J }$ is the linear distance (cm).The density is given by

$$
N _ { \mathrm { e } } = { \frac { A } { r ^ { 6 } } } + { \frac { a b / { \sqrt { a ^ { 2 } \sin ^ { 2 } \beta + b ^ { 2 } \cos ^ { 2 } \beta } } } { r ^ { 2 } } }
$$