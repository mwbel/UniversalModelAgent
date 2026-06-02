calculate the tangent plane coordinates as described in $\ S 9 . 5 . 1 . 1$ .Then,the apparent angular distance $s$ and position angle $P$ are computed from

$$
\begin{array} { c } { { s = \sqrt { ( X ^ { 2 } + Y ^ { 2 } ) } } } \\ { { \tan P = X / Y . } } \end{array}
$$

Times when $s$ reaches a maximum or minimum are singled out. The times when $s$ isa maximum are times of elongation,with eastern elongations being those for which $X$ is positive and the northern elongations being those for which $Y$ ispositive.The timeswhen $s$ is a minimum are times of conjunction.For a direct satellite,the conjunction following eastern elongation is inferior conjunction and the conjunction following northern elongation is superior conjunction.

Using the IAU numbering system,the phenomena listed in The Astronomical Almanac for satellites Mars I, I,Saturm Ito VII, Uranus I to V,andNeptuneIareall computedusing this method.In Taylor and Sinclair(2oo3) a comparison wasmade of this method with the traditional method as previously used to compute satellite phenomena.The new method was preferred sincethe times of phenomena wereconsidered better,as they refer to theactual orbit rather thanaprojection of an idealized circular orbit.

# 9.5.2.2 Approximate Apparent Distance and Position Angle

The method given in Taylor and Sinclair (2Oo3) is used to compute tables to calculate approximate apparent distance and position angle.It was shown in this paper that it gives similar results to the traditional method previously used to compute these tabular values.

Once all tmes of greatest eastern (or northern) elongation have been computed for a particular satellite,the times are compared to the time of opposition for that satellite's planet. The first eastern elongation time after opposition is chosen as the start time for computing the table of apparent distances and position angles for one satellite orbit.In the case of Mars, where opposition occurs every other year,in years when no opposition is expected the first eastern elongation time after either January1orDecember 31of the edition year ischosen forthecomputations.Thechoice of date depends onwhich yields the betterview of the satellites.

For the chosen orbit using the same time step fora satelite that was used previously in the traditional method, $X$ and $Y$ offsets as described in $\ S 9 . 5 . 1 . 1$ are computed. Equations 9.43 and 9.44 are then used to calculate the angular distance and position angle.Denoting $s _ { 0 }$ (in radians)and $\Delta _ { 0 }$ to be theangular distanceand current distance of the planet from the Earth respectively at these times and $^ { a }$ the semimajor axis of the satellite orbit,we can form the scaled distance

$$
F = \frac { s _ { 0 } \Delta _ { 0 } } { a } .
$$

A table of scaled distances for the chosen orbit can then be computed.

Aseparate table gives the multiplying factors,which are values of the quantity $a / \Delta$ throughout the year,at intervals as used in the traditional method.These values are multiplied by the conversion factor from radians to seconds of arc.

To compute the approximate apparent distance and position angle at any time $\tau$ in the year we find firstly the time interval from the last greatest eastern (or northern) elongation.Then, using this time interval as the time argument,extract from the table of scaled distances and position angles $F$ and $P$ $P$ will be the approximate position angle required.Enter with time argument $t$ the table giving the multiplying factorsand findthe value of $a / \Delta$ .Theapproximate apparent distance in seconds of arc will be

$$
s = \frac { F a } { \Delta } .
$$

# 9.6Satellite Data in The Astronomical Almanac and Notation

# 9.6.1 Presented Data

Datatablesforthesatellitesarefound inSectionFofTheAstronomical AlmanacandinThe Astronomical Almanac Online URL[1].Due to the recent proliferation of known satellites associated with the gas giant planets,a setof selection criteria has been established under which satellites will be included in the printed data tables in the TheAstronomical Almanac. These criteriaare the following:The visual magnitude of the satelite must not be fainter than 23.O and the satellite must be sanctioned by the IAU with a roman numeral and a name designation. Satellites that have yet to receive IAU approval are designated as works-inprogress and shallbe included at a later time should such approval be granted,provided their visual magnitudesare not fainter than 23.0.A more complete version of the tables,including satelliteswith visual magnitudes fainterthan23.O,is foundatTheAstronomicalAlmanac Online.

Positional data presentedfor the brighter satellites generally fall in two broadcategories— elongations or differential coordinates.Elongationsare typically given for satelites with orbits lessthan 9O days,and differential coordinates are provided for the longer period ones. Table9.2 summarizes the positional information in The Astronomical Almanac.

Computations requiring poles of rotation and prime meridian data utilize the latest published report from IAU/IAG Working Group on Cartographic Coordinatesand Rotational Elements (Archinal etal.2O11).SeeURL[2] foradditional details.

# 9.6.2 Notation

Many different notations have been used in the literature for the orbital elements of the satellites.The notations for the angular elements used in the balance of this chapter are described below.

For those satelites for which the orbit is referred directly to the ecliptic and equinox of B1950.0 or J2000.0 the notation is

$$
\begin{array} { r l } & { \lambda = \mathrm { m e a n ~ l o n g i t u d e } } \\ & { \varpi = \mathrm { l o n g i t u d e ~ o f ~ t h e ~ p e r i c e n t e r } } \\ & { \Omega = \mathrm { l o n g i t u d e ~ o f ~ t h e ~ a s c e n d i n g ~ n o d e } } \\ & { \quad i = \mathrm { i n c l i n a t i o n } . } \end{array}
$$

[able9.2 Summary of satelite positional data in The Astronomical Almanai   

<table><tr><td>Planet</td><td></td><td>Satellite</td><td>Elongations</td><td>Diff. Coordinates</td></tr><tr><td>Mars</td><td>I</td><td>Phobos</td><td>yes</td><td>no</td></tr><tr><td></td><td>ⅡI</td><td>Deimos</td><td>yes</td><td>no</td></tr><tr><td>Jupiter</td><td>I</td><td>Io</td><td>*</td><td>*</td></tr><tr><td></td><td>II</td><td>Europa</td><td>*</td><td>*</td></tr><tr><td></td><td>IⅢI</td><td>Ganymede</td><td>*</td><td>*</td></tr><tr><td></td><td>IV</td><td>Callisto</td><td>*</td><td>*</td></tr><tr><td></td><td>V</td><td>Amalthea</td><td>yes</td><td>no</td></tr><tr><td></td><td>VI</td><td>Himalia</td><td>no</td><td>yes</td></tr><tr><td></td><td>VII</td><td>Elara</td><td>no</td><td>yes</td></tr><tr><td></td><td>VIII</td><td>Pasiphae</td><td>no</td><td>yes</td></tr><tr><td></td><td>IX</td><td>Sinope</td><td>no</td><td>yes</td></tr><tr><td></td><td>X</td><td>Lysithea</td><td>no</td><td>yes</td></tr><tr><td></td><td>XI</td><td>Carme</td><td>no</td><td>yes</td></tr><tr><td></td><td>XII</td><td>Ananke</td><td>no</td><td>yes</td></tr><tr><td></td><td>XIII</td><td>Leda</td><td>no</td><td>yes</td></tr><tr><td>Saturn</td><td>I</td><td>Mimas</td><td>yes</td><td>no</td></tr><tr><td></td><td>II</td><td>Enceladus</td><td>yes</td><td>no</td></tr><tr><td></td><td>IⅢI</td><td>Tethys</td><td>yes</td><td>no</td></tr><tr><td></td><td>IV</td><td>Dione</td><td>yes</td><td>no</td></tr><tr><td></td><td>V</td><td>Rhea</td><td>yes</td><td>no</td></tr><tr><td></td><td>VI</td><td>Titan</td><td>yes</td><td>no</td></tr><tr><td></td><td>VII</td><td>Hyperion</td><td>yes</td><td>yes</td></tr><tr><td></td><td>VIII</td><td>Iapetus</td><td>yes</td><td>yes</td></tr><tr><td></td><td>IX</td><td>Phoebe</td><td>no</td><td>yes</td></tr><tr><td>Uranus</td><td>I</td><td>Ariel</td><td>yes</td><td>no</td></tr><tr><td></td><td>II</td><td>Umbriel</td><td>yes</td><td>no</td></tr><tr><td></td><td>IⅢI</td><td>Titania</td><td>yes</td><td>no</td></tr><tr><td></td><td>IV</td><td>Oberon</td><td>yes</td><td>no</td></tr><tr><td></td><td>V</td><td>Miranda</td><td>yes</td><td>no</td></tr><tr><td>Neptune</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>I II</td><td>Triton Nereid</td><td>yes no</td><td>no yes</td></tr><tr><td>Pluto</td><td>I</td><td>Charon</td><td>yes</td><td>no</td></tr></table>

Where an intermediate reference plane is used (usually the equatorial plane of the planet or theLaplacian plane) the notation used for the angular elements is

$$
\begin{array} { r l } & { L = \mathrm { m e a n ~ l o n g i t u d e } } \\ & { P = \mathrm { l o n g i t u d e ~ o f ~ t h e ~ p e r i c e n t e r } } \\ & { \theta = \mathrm { l o n g i t u d e ~ o f ~ t h e ~ a s c e n d i n g ~ n o d e } } \\ & { \gamma = \mathrm { i n c l i n a t i o n } . } \end{array}
$$

When the orbital elementsare referred to the Earth equator and equinox of B1950.O or J2000.O,the notation used for the angular elements is

$$
\begin{array} { c } { { l = \mathrm { m e a n ~ l o n g i t u d e } } } \\ { { \pi = \mathrm { l o n g i t u d e ~ o f ~ t h e ~ p e r i c e n t e r } } } \\ { { N = \mathrm { l o n g i t u d e ~ o f ~ t h e ~ a s c e n d i n g ~ n o d e } } } \\ { { J = \mathrm { i n c l i n a t i o n } . } } \end{array}
$$

The reason for using the ecliptic as the reference plane for the orbits is forconvenience rather than any good dynamical or observational reason.The planes of dynamical significance are the equatorial and orbital planes of the planet. The plane of observational significance is theEarth'sequatorial plane.Theorbital elementsof the planetsare,however,referred to the ecliptic,and so it was probablyaconvenient frame in which to calculate solar and planetary perturbations.

# 9.7 The Satelltes of Mars

Ephemerides of the greatest eastern elongationsare given for the satelites ofMars in The Astronomical Almanac.The ephemerides of the satellites are computed from elements given by Sinclair (1989).

Phobos

Deimos

$$
\begin{array} { r l } & { \gamma = 1 \Im ^ { 2 } 7 9 } \\ & { \theta = 2 4 0 ^ { \circ } 3 8 - 0 ^ { \circ } 0 1 8 0 1 d } \\ & { L = 2 8 ^ { \circ } 9 6 + n d - 0 . 2 7 \sin } \\ & { P = 1 1 1 ^ { \circ } 7 + 0 ^ { \circ } 0 1 7 9 8 d } \\ & { h = 1 9 6 ^ { \circ } 5 5 - 0 . 0 1 8 0 1 d } \\ & { N _ { a } = 4 6 ^ { \circ } 3 7 - 0 ^ { \circ } 0 0 1 4 y } \\ & { J _ { a } = 3 6 ^ { \circ } 6 2 + 0 ^ { \circ } 0 0 0 8 y } \end{array}
$$

where

$$
\begin{array} { l } { d = \mathrm { J D } - 2 4 4 1 2 6 6 . 5 } \\ { y = d / 3 6 5 . 2 5 . } \end{array}
$$

These elementsare referred to the fixed Laplacian planes of the satellites.The angular elementsare shown inFig.9.11.The orbital elements are defined as follows: the semimajor axis $a$ ; themeandailymotion $n$ ；theeccentricity $e$ ；theinclination $\gamma$ ; thelongitude of the ascending node, $\theta$ ,measured from the ascending node of the Laplacian plane on the Earth's equator along the Laplacian plane to the node of the orbit; $L$ ,the mean longitude reckoned from the vernal equinox along the Earth’s equator to the ascending node of theLaplacian plane,then along the Laplacian plane to the ascending node of the orbit,and then along the orbit to the mean position of the satellite; $P$ ,thelongitudeof thepericenter,measured in the same manner as $L$ from the vernal equinox to the pericenter; $N _ { a }$ ,the longitude of the ascending nodeof the Laplacian planereckonedfrom the vernal equinox along the Earth's equator; $J _ { a }$ ,the inclinationof theLaplacian plane to the Earth's equator; $h$ ,reckoned along theLaplacian plane from its ascending node on the orbital plane of Mars to the ascending node of the satellite orbit.

![](images/3d678073767c1ae4620d661200415d57d47e574f03b055a16b17ea73ee6db3b6.jpg)  
Figure9.11 Reference system for Phobos and Deimos. $D =$ position of satellite pericenter, $\theta = A C$ , $L = \mathcal { T } A + A B + B C + C D +$ mean anomaly, $P = \Upsilon A + A B +$ $B C + C D$ , $N _ { a } = \Upsilon A$ ,and $N = \Upsilon E$ .

Though the theories for the motion of the satellites contain several periodic terms,the only periodic perturbation of importance for Earth-based observations is $L = - 0 . 2 7 \sin h$ forDeimos.

$J$ and $N$ ,the inclination and ascending node of the satellite orbit on the Earth's equator can be found by considering the spherical triangle $A E C$ inFig.9.11.From spherical trigonometry we have

$$
\begin{array} { l } { \sin J \sin ( N - N _ { a } ) = \sin \gamma \sin \theta } \\ { \sin J \cos ( N - N _ { a } ) = \cos \gamma \sin J _ { a } + \sin \gamma \cos J _ { a } \cos \theta . } \end{array}
$$

Now find the arc length $E C$ of triangle $A E C$ from

$$
\begin{array} { l } { \sin J \sin E C = \sin J _ { a } \sin \theta } \\ { \sin J \cos E C = \cos J _ { a } \sin \gamma + \sin J _ { a } \cos \gamma \cos \theta . } \end{array}
$$

$u$ follows from

$$
u = E C + L - N _ { a } - \theta + ( f - M )
$$

where $( f - M )$ is the equationof center that is computed viaEq.9.1,where

$$
M = L - P .
$$

The computation of the tabulated values follows as described in $\ S 9 . 4 . 2$ .

# 9.8 The Satellites of Jupiter

# 9.8.1The Galilean Satellites

The ephemerides and phenomena of Satellites I-IV given in The Astronomical Almanac are based on the theory ofLieske(1977),with constants due to Arlot (1982).Lieske's theory is a revision of the theory by Sampson (1921).A shortened version ofLieske's theory is presented below,which will give the positions of the satellites to about $5 0 0 \mathrm { k m }$ .The constants used below are from Lieske (1987):

$$
\begin{array} { r l } & { | 0 ^ { 7 } \xi _ { 1 } = - 4 1 2 7 9 \cos ( 2 L _ { 1 } - 2 L _ { 2 } ) ; } \\ & { | 0 ^ { 7 } \nu _ { 1 } = - 5 5 9 6 \sin ( P _ { 3 } - P _ { 4 } ) - 2 1 9 8 \sin ( P _ { 1 } + P _ { 3 } - 2 \Pi _ { 1 } - 2 G ) } \\ & { \qquad + 1 3 2 1 \sin ( \phi _ { l } ) - 1 1 5 7 \sin ( L _ { 1 } - 2 L _ { 2 } + P _ { 4 } ) } \\ & { \qquad - 1 9 4 0 \sin ( L _ { 1 } - 2 L _ { 2 } + P _ { 3 } ) - 7 9 1 \sin ( L _ { 1 } - 2 L _ { 2 } + P _ { 2 } ) } \\ & { \qquad + 7 9 1 \sin ( L _ { 1 } - 2 L _ { 2 } - P _ { 2 } ) + 8 2 3 6 3 \sin ( 2 L _ { 1 } - 2 L _ { 2 } ) ; } \\ & { | 0 ^ { 7 } \xi _ { 1 } = + 7 0 3 8 \sin ( L _ { 1 } - \theta _ { 1 } ) + 1 8 3 5 \sin ( L _ { 1 } - \theta _ { 2 } ) ; } \\ & { | 0 ^ { 7 } \xi _ { 2 } = - 3 1 8 7 \cos ( L _ { 2 } - P _ { 3 } ) - 1 7 3 8 \cos ( L _ { 2 } - P _ { 4 } ) } \\ & { \qquad + 9 3 7 4 8 \cos ( L _ { 1 } - L _ { 2 } ) ; } \end{array}
$$

$$
\begin{array} { r l } & { { 1 0 ^ { 7 } } \nu _ { 2 } = - 1 1 5 8 \sin ( - 2 \Pi _ { \mathrm { J } } + 2 \Psi ) + 1 7 1 5 \sin ( - 2 \Pi _ { \mathrm { J } } + \theta _ { 3 } + \Psi - 2 G ) } \\ & { \qquad - 1 8 4 6 \sin ( G ) + 2 3 9 7 \sin ( P _ { 3 } - P _ { 4 } ) - 3 1 7 2 \sin ( \phi _ { l } ) } \\ & { \qquad - 1 9 9 3 \sin ( L _ { \mathrm { 2 } } - L _ { 3 } ) + 1 8 4 4 \sin ( L _ { \mathrm { 2 } } - P _ { 2 } ) } \\ & { \qquad + 6 3 9 4 \sin ( L _ { \mathrm { 2 } } - P _ { 3 } ) + 3 4 5 1 \sin ( L _ { \mathrm { 2 } } - P _ { 4 } ) } \\ & { \qquad + 4 1 5 9 \sin ( L _ { \mathrm { 1 } } - 2 L _ { 2 } + P _ { 4 } ) + 7 5 7 1 \sin ( L _ { \mathrm { 1 } } - 2 L _ { 2 } + P _ { 3 } ) } \\ & { \qquad - 1 4 9 1 \sin ( L _ { \mathrm { 1 } } - 2 L _ { 2 } + P _ { 2 } ) - 1 8 5 6 4 0 \sin ( L _ { \mathrm { 1 } } - L _ { 2 } ) } \\ & { \qquad - 8 0 3 \sin ( L _ { \mathrm { 1 } } - L _ { 3 } ) + 9 1 5 \sin ( 2 L _ { \mathrm { 1 } } - 2 L _ { 2 } ) ; } \end{array}
$$

$$
\begin{array} { r l r } & { } & { \delta } \\ & { } & { + 6 . 3 9 4 \sin ( L _ { 2 } - P _ { 3 } ) + 3 4 5 1 \sin ( L _ { 2 } - P _ { 4 } ) } \\ & { } & { + 4 1 5 9 \sin ( L _ { 1 } - 2 L _ { 2 } + P _ { 4 } ) + 7 5 7 1 \sin ( L _ { 1 } - } \\ & { } & { - 1 4 9 1 \sin ( L _ { 1 } - 2 L _ { 2 } + P _ { 2 } ) ) - 1 8 5 6 4 0 \sin ( L _ { 1 } } \\ & { } & { - 8 0 3 3 \sin ( L _ { 1 } - L _ { 3 } ) + 9 1 5 \sin ( 2 L _ { 1 } - 2 L _ { 2 } ) ; } \\ & { } & { 1 0 \widetilde { 7 } _ { \xi _ { 2 } } = 4 8 1 5 7 5 \sin ( L _ { 2 } - \theta _ { 2 } ) + 4 5 1 2 \sin ( L _ { 2 } - \theta _ { 3 } ) } \\ & { } & { - 3 2 8 6 \sin ( L _ { 2 } - \Psi _ { 3 } ) ; } \\ & { } & { 1 0 \widetilde { 7 } _ { \xi _ { 3 } } = - 1 4 6 1 0 \cos ( L _ { 3 } - P _ { 3 } ) - 1 7 5 8 \cos ( 2 L _ { 3 } - 2 L _ { 4 } ) } \\ & { } & { + 6 3 3 3 \cos ( L _ { 2 } - L _ { 3 } ) - 7 8 9 4 \sin ( L _ { 3 } - P _ { 4 } ) ; } \\ & { } & \\ { 1 0 ^ { 2 } \nu _ { 3 } = - 1 4 8 8 \sin ( - 2 \Pi _ { 1 } + 2 \Psi _ { 3 } ) + 4 1 1 \sin ( - \theta _ { 3 } + \Psi } \end{array}
$$

$$
\begin{array} { r l } { | 0 ^ { 7 } \nu _ { 3 } = - 1 4 8 8 \sin ( - 2 \Pi _ { J } + 2 \Psi ) + 4 1 1 \sin ( - \theta _ { 3 } + \Psi ) } \\ { \ } & { + 3 4 6 \sin ( - \theta _ { 4 } + \Psi ) - 2 3 3 8 \sin ( G ) } \\ { \ } & { + 6 5 5 \sin ( N _ { 3 } - P _ { 4 } ) + 5 2 3 \sin ( P _ { 1 } + P _ { 3 } - 2 \Pi _ { 1 } - 2 G ) } \\ { \ } & { + 3 1 4 \sin ( \phi _ { i } ) - 9 4 3 \sin ( L _ { 3 } - L _ { 4 } ) } \\ { \ } & { + 2 9 3 8 7 \sin ( L _ { 3 } - P _ { 3 } ) + 1 5 8 0 0 \sin ( L _ { 3 } - P _ { 4 } ) } \\ { \ } & { + 3 2 1 8 \sin ( 2 L _ { 3 } - 2 L _ { 4 } ) + 2 2 6 \sin ( 3 L _ { 3 } - 2 L _ { 4 } ) } \\ { \ } & { - 1 2 0 3 8 \sin ( L _ { 2 } - L _ { 3 } ) - 6 6 2 \sin ( L _ { 1 } - 2 L _ { 2 } + P _ { 4 } ) } \\ { \ } & { - 1 2 4 6 \sin ( L _ { 1 } - 2 L _ { 2 } + P _ { 3 } ) + 6 9 9 \sin ( L _ { 1 } - 2 L _ { 2 } + P _ { 2 } ) } \\ { \ } & { + 2 1 7 \sin ( L _ { 1 } - L _ { 3 } ) ; } \end{array}
$$

$$
\begin{array} { r } { { 1 0 ^ { 7 } } \zeta _ { 3 } = \mathrm { ~ - ~ } 2 7 9 3 \sin ( L _ { 3 } - \theta _ { 2 } ) + 3 2 3 8 7 \sin ( L _ { 3 } - \theta _ { 3 } ) } \\ { \mathrm { ~ } + 6 8 7 1 \sin ( I . \mathrm { ~ - ~ } \theta . ) - 1 6 8 7 6 \sin ( I . \mathrm { ~ - ~ } \Psi ) . } \end{array}
$$

$$
\begin{array} { r l } { \| 0 \| _ { \mathcal { H } _ { 4 } } ^ { 2 } = } & { 1 6 5 6 \cos ( L _ { 4 } - P _ { 3 } ) - 7 3 3 3 2 8 \cos ( \Omega _ { 4 } - P _ { 4 } ) } \\ & { + 1 8 2 \cos ( L _ { 4 } - \Pi _ { 1 } ) - 8 4 1 0 \cos ( L _ { 4 } + P _ { 4 } - 2 \Pi _ { 1 } - 2 \theta ) } \\ & { - 2 6 9 \cos ( 2 L _ { 4 } - 2 P _ { 4 } ) + 9 7 4 \cos ( \Omega _ { 3 } - L _ { 4 } ) \cdot } \\ & { - 2 6 9 \cos ( 2 L _ { 4 } - 2 P _ { 4 } ) + 9 3 0 \sin ( 2 L _ { 3 } - 2 L _ { 4 } ) \cdot } \\ { \| 0 \| _ { \mathcal { H } _ { 4 } } ^ { 2 } = } & { - 4 9 7 \sin ( - 2 P _ { 4 } + 2 \Psi ) + 3 0 9 \sin ( - 2 P _ { 4 } + \theta _ { 4 } + \Psi ) } \\ & { - 4 8 4 0 \sin ( - 2 \Pi _ { 1 } + 2 \Psi ) + 2 0 7 4 4 \sin ( - \theta _ { 4 } + \Psi ) } \\ & { - 5 6 0 5 \sin ( G ) - 2 0 4 3 \sin ( 2 G ) } \\ & { - 4 9 5 \sin ( 5 \theta ^ { \prime } - 2 G + \phi _ { 2 } ) + 2 3 4 \sin ( P _ { 4 } - \Pi _ { 1 } ) } \\ & { - 6 1 2 \sin ( 9 _ { 3 } - P _ { 4 } ) - 3 3 1 8 \sin ( \Omega _ { 4 } - P _ { 3 } ) } \\ & { + 1 4 6 7 3 \sin ( \Omega _ { 4 } - P _ { 4 } ) + 1 7 8 \sin ( L _ { 4 } - \Pi _ { 3 } - G ) } \\ & { - 3 6 3 \sin ( L _ { 4 } - \Pi _ { 3 } ) + 1 0 8 5 \sin ( L _ { 4 } + P _ { 4 } - 2 \Pi _ { 3 } - 2 G ) } \\ & { + 6 7 2 \sin ( 2 L _ { 4 } - 2 P _ { 4 } ) + 2 1 8 \sin ( 2 L _ { 4 } - 2 \Pi _ { 1 } - 2 G ) } \\ & { + 6 7 2 \sin ( 2 L _ { 4 } - 2 P _ { 4 } ) + 2 1 8 \sin ( 2 L _ { 4 } - 2 \Pi _ { 1 } - 2 G ) } \end{array}
$$

$$
\begin{array} { r l } & { \quad + 1 6 7 \sin ( 2 L _ { 4 } - \theta _ { 4 } - \Psi ) - 1 4 2 \sin ( 2 L _ { 4 } - 2 \Psi ) } \\ & { \quad + 1 4 8 \sin ( L _ { 3 } - 2 L _ { 4 } + P _ { 4 } ) - 3 9 0 \sin ( L _ { 3 } - L _ { 4 } ) } \\ & { \quad - 1 9 5 \sin ( 2 L _ { 3 } - 2 L _ { 4 } ) + 1 8 5 \sin ( 3 L _ { 3 } - 7 L _ { 4 } + 4 P _ { 4 } ) ; } \\ & { \quad 1 0 ^ { 7 } \zeta _ { 4 } = + 7 7 3 \sin ( L _ { 4 } - 2 \Pi _ { 5 } + \Psi - 2 G ) } \\ & { \quad \quad \quad - 5 0 7 5 \sin ( L _ { 4 } - \theta _ { 3 } ) + 4 4 3 0 0 \sin ( L _ { 4 } - \theta _ { 4 } ) } \end{array}
$$

where

$L _ { i }$ ， $P _ { i }$ ,and $\theta _ { i }$ are the mean longitude,proper periapse,and proper node of satellite $i$ . $\phi _ { l }$ is the libration phase angle; $\Pi _ { \mathrm { J } }$ is the longitude of perihelion of Jupiter; $\Psi$ is the longitude of the origin of the coordinates (Jupiter's pole); $G ^ { \prime }$ and $G$ are the mean anomalies of Saturn and Jupiter; $\phi _ { 2 }$ is the phase angle in solar $\left( A / R \right) ^ { 3 }$ withangle $5 G ^ { \prime } - 2 G$ .

To convert $\xi , \nu ,$ and $\zeta$ to rectangular coordinates $\bar { x }$ , $\bar { y }$ ，andzin the moving Jovian equatorial frame,Eqs.9.53and 9.54can beused.Satelite subscripts have been omitted for clarity.

$$
\begin{array} { l } { { \bar { x } = a ( 1 + \xi ) \cos ( L - \Psi + \nu ) } } \\ { { \bar { y } = a ( 1 + \xi ) \sin ( L - \Psi + \nu ) } } \\ { { \bar { z } = a \zeta . } } \end{array}
$$

The coefficients $^ { a }$ are

$$
\begin{array} { r l } & { a _ { 1 } = 0 . 0 0 2 8 1 9 3 4 7 \mathrm { ~ a u } } \\ & { a _ { 2 } = 0 . 0 0 4 4 8 5 8 7 2 \mathrm { ~ a u } } \\ & { a _ { 3 } = 0 . 0 0 7 1 5 5 3 5 2 \mathrm { ~ a u } } \\ & { a _ { 4 } = 0 . 0 1 2 5 8 5 4 3 6 \mathrm { ~ a u } . } \end{array}
$$

The formula for finding the coordinates in the Earth equatorial frame of 1950.0 is

$$
\mathbf { r } = \mathbf { R } _ { 1 } ( - \varepsilon ) \mathbf { R } _ { 3 } ( - \Omega ) \mathbf { R } _ { 1 } ( - J ) \mathbf { R } _ { 3 } ( - \Phi ) \mathbf { R } _ { 1 } ( - I ) \bar { \mathbf { r } }
$$

where

$$
\begin{array} { r l } & { \bar { \bf r } = ( \bar { x } , \bar { y } , \bar { z } ) ^ { \mathrm { T } } } \\ & { { \bf r } = ( x , y , z ) ^ { \mathrm { T } } } \\ & { \varepsilon = 2 3 ^ { \circ } 2 6 ^ { \prime } 4 4 ^ { \prime \prime } 8 4 } \\ & { \Omega = 9 9 \mathrm { e } 9 9 7 5 4 } \\ & { J = 1 3 0 6 9 1 } \\ & { \Phi = \Psi - \Omega } \\ & { I = 3 ^ { \circ } 1 0 4 0 1 . } \end{array}
$$

$\varepsilon$ is the obliquity of the ecliptic; $\Omega$ is the longitude of the ascending node of Jupiter; $J$ is the inclination of Jupiter's orbit to the ecliptic; $I$ is the inclination of Jupiter’s orbit to Jupiter's equator. The rotation matrices $\mathbf { R } _ { i }$ are defined in $\ S 9 . 1 . 5$ and described in Chapter 14.

Thedata tabulated in The Astronomical Almanac consist of:theapproximate times of superior geocentric conjunction; the times of the geocentric phenomena; and the approximate configurations,in graphical form,of the satellites relative to the disk of Jupiter.

The Terrestrial Time of each superior geocentric conjunction is given for each satellite to the nearest minute.The phenomena for which times are given are eclipses,occultations, transits,and shadow transits.The TT of the beginning and end of each phenomenon (disappearance and reappearance for eclipses and occultations,ingressand egress for transits and shadow transits) are given to the nearest minute for all phenomena that are observable. When Jupiter is in opposition,the shadow may be hidden by the disk and no eclipses can be observed.In general, eclipses may be observed on the western side of Jupiter before opposition and on the eastern side after opposition.Before opposition the disappearance only ofSatelite Iinto the shadow may be observed since itis occulted before it emerges from theshadow;after oppositiononly thereappearances from the shadowarevisible.The same is true in general of Satellite II,although occasionally both phenomena can be seen.In the case of Satellites II and IV,both phases of the eclipses are usually visible except near certain oppositions.Similarly the occultation disappearances and reappearances of a satellite cannot beobservedif,at the time concerned,thesatelliteiseclipsed.ForSatellitesIand $\mathrm { I I }$ there are,in general,cycles of six phenomena consisting of both phases of both transit and shadow transit,one phase of the eclipse,and the other phase of the occultation.

For SatelliteIV,none of the phenomena occur when the plane of the orbit of the satelliteessentially the same as that of Jupiter'sequator—is inclinedat more thanabout $2 ^ { \circ }$ to the line from Jupiter to the Earth (for occultations and transits) or to the Sun (for eclipses and shadow transits).

Owing to the finite disks of the satelites,the phenomena do not take place instantaneously —the timesreferto the center of thedisk.When the Earth isnear the satellites’orbital planes,one satelite may be eclipsed by the shadow of another,or may occult another. This so-called mutual event season happens about every six years for the Galilean satellites. Typically predictionsare made bycollaborators and printed in The Astronomical Almanac. Adescription of a method of prediction is given byLevin (1934).

The configurations of the four satellites relative to the disk of Jupiter are shown in The Astronomical Almanac in graphical form,on the pages facing the tabular ephemerides of the times of the eclipsesand other phenomena.These are generally provided by colleagues at Institut de Mecanique Celeste et de Calcul des Ephémérides (IMCCE)underalong-standing data exchangeagreement.

# 9.8.2 Jupiter's Fifth Satellite,Amalthea

The data given in The Astronomical Almanac consist of the Universal Timesof every 20th eastern elongation.The elongations are computed from the following circular orbital elements,referred to the equator of Jupiter,given by van Woerkom (1950):

$$
{ \begin{array} { r l } & { t _ { 0 } = 1 9 0 3 \operatorname { S e p t e m b e r } 1 . 5 \operatorname { U T } = \operatorname { I D } 2 4 1 6 3 5 9 . 0 ; } \\ & { a = 2 4 9 ^ { \prime } 5 5 ; } \\ & { \gamma = 2 4 ^ { \prime } 1 ; } \\ & { \theta = 8 2 ^ { \prime } 5 - 9 1 4 5 6 2 t ; } \\ & { n = 7 2 2 ^ { \prime } 6 3 1 7 5 / \operatorname { d a y } ; } \\ & { L _ { 0 } = 1 9 4 ^ { \prime } 9 8 ; } \\ & { \delta L _ { 0 } = - 0 . 9 1 1 3 - 0 . 5 0 0 7 6 t + 0 ^ { \prime } 0 0 0 3 5 t ^ { 2 } ; } \\ & { t = ( \operatorname { I D } - t _ { 0 } ) / 3 6 5 . 2 5 . } \end{array} }
$$

$a$ is the apparent semimajor axis at a distance of one astronomical unit; $\gamma$ ,the inclination to the equator of Jupiter; $\theta$ ,thelongitude of the ascending node; $n$ ,the mean motion per solar day; $L _ { 0 }$ ,the mean longitude at epoch $t _ { 0 }$ ;and $\delta L _ { 0 }$ ,the correction to mean longitude. $t - t _ { 0 }$ is reckoned in Julian years.The longitudes are measured in the plane of the equator of Jupiter, from the ascending node of the mean orbital plane of Jupiter on the plane of the equator of JupiterasshowninFig.9.12.Fromthese orbital elements:

$$
\begin{array} { r l } { \mathrm { s i d e r e a l p e r i o d } } & { 0 . 4 9 9 9 1 0 8 3 = 1 1 \mathrm { h } 9 9 7 8 6 0 } \\ { \mathrm { m e a n ~ s y n o d i c ~ p e r i o d } } & { 0 . 4 9 9 9 6 8 5 1 = 1 1 \mathrm { h } 9 9 9 2 4 4 . } \end{array}
$$

In determining these elements,van Woerkomadopted Souillart's elements of the equator ofJupiter,but for thecalculation of the elongationsin The Astronomical Almanac theright ascension and declination of Jupiter's pole of Davies et al. (1989) are used:

$$
\begin{array} { c } { { \alpha _ { 0 } = 2 6 8 . 0 5 - 0 . 0 0 9 T } } \\ { { \delta _ { 0 } = 6 4 . 4 9 + 0 . 0 0 3 T } } \end{array}
$$

where $\alpha _ { 0 }$ and $\delta _ { 0 }$ are referred to the equator and equinox of J2000.0

$$
T = ( \mathrm { J D } - 2 4 5 1 5 4 5 . 0 ) / 3 6 5 2 5 .
$$

![](images/e108e3064a60aec5b749fa4fe1c30b11a95bcb75000ca65afb9089d5dd0fcc8c.jpg)  
Figure9.12 Reference system for Amaltheaand Thebe. $\Delta = 1 8 0 ^ { \circ } - A B , \theta = 1 8 0 ^ { \circ } + B C$ , $\theta - \Delta = A C$ , $\psi = D C$ , $N = \Upsilon D$ ,and $\alpha _ { 0 } = \Upsilon A - 9 0 ^ { \circ }$

The right ascension, $N$ ,of the node of the orbit on the Earth’s equator;the inclination, $J$ ,of the orbit to the Earth'sequator;and the arc, $\psi$ ,along the orbit from the node on the Earth's equator to the node on Jupiter’s equator are given by

$$
\begin{array} { c } { { \sin J \sin ( N - \alpha _ { 0 } ) = + \cos \delta _ { 0 } \cos \gamma + \sin \delta _ { 0 } \sin \gamma \cos ( \theta - \Delta ) } } \\ { { \sin J \cos ( N - \alpha _ { 0 } ) = - \sin \gamma \sin ( \theta - \Delta ) } } \\ { { \cos J = + \sin \delta _ { 0 } \cos \gamma - \cos \delta _ { 0 } \sin \gamma \cos ( \theta - \Delta ) } } \\ { { \sin J \sin \psi = + \cos \delta _ { 0 } \sin ( \theta - \Delta ) } } \\ { { \sin J \cos \psi = + \sin \delta _ { 0 } \sin \gamma + \cos \delta _ { 0 } \cos \gamma \cos ( \theta - \Delta ) } } \end{array}
$$

in which $\theta - \Delta$ (the arc along Jupiter’s equator from its node on the Earth's equator to the node of the satellite's orbit) is given by

$$
{ \begin{array} { r l } & { \theta - \Delta = 2 1 9 \cdot 8 - 2 ^ { \mathrm { r } } . 5 4 0 5 7 4 8 7 ( t - t _ { 0 } ) ; \quad ( 2 ^ { \mathrm { r } } . 5 4 \cdot . . = \mathrm { r e v ~ p e r ~ y e a r } ) } \\ & { \qquad = 2 1 9 \cdot 8 - 2 ^ { \circ } . 5 0 4 0 5 7 3 7 d } \end{array} }
$$

where $^ d$ is the number of days from the epoch (JD 2416359.0).

The quantities $N$ , $J$ ,and $\psi$ are calculated from the preceding equations at $0 ^ { \mathrm { h } }$ at any date, and are then used to form $U$ ( $B$ and $P$ are notrequired) from Eqs.9.26.The orbital longitude, $u$ ,measured from the node on the Earth's equator, at $0 ^ { \mathrm { h } }$ on that date is derived from

$$
\begin{array} { c } { u = L _ { 0 } + n d - \theta + \psi + \delta L _ { 0 } } \\ { = \psi + 1 1 2 . 3 7 + 2 . 0 1 4 2 6 6 2 d . } \end{array}
$$

Then the times of the elongations on that date are

$$
\begin{array} { r l } { \mathrm { e a s t e r n \ e l o n g a t i o n } } & { 0 . 0 3 3 3 2 7 ( U + 9 0 ^ { \circ } - u ) + 0 . 1 3 8 6 1 \Delta } \\ { \mathrm { w e s t e r m \ e l o n g a t i o n } } & { 0 . 0 3 3 3 2 7 ( U + 2 7 0 ^ { \circ } - u ) + 0 . 1 3 8 6 1 \Delta } \end{array}
$$

in which $\Delta$ is the geocentric distance ofJupiter.The terms in $\Delta$ are the corrections for lighttime;for strict accuracy they should be interpolated to the times of geometric elongation which the first terms represent.

The calculation of elongation time need be made for onlya few of the ephemeris dates,the others being obtained by means of multiples of the period.For strict accuracy,the calculation should be repeated with the values of the quantities at the calculated times instead of at $0 ^ { \mathrm { h } }$ ; but for the tabular accuracy of $0 ^ { \mathrm { h } } 1$ ,this is unnecessary.

# 9.8.3 Jupiter's Sixth through Thirteenth Satellites

Differential right ascensions and declinations of Satelites VI-XIII are presented in The Astronomical Almanac.The coordinates are referred to the equator and equinox of J2000.0. They are computed with a variable-order,variable-step-size numerical integrator developed by Shampine and Gordon (1975). The equations of motion in $x$ , $y$ and $Z$ are:

$$
\begin{array} { c c l } { \displaystyle \frac { d ^ { 2 } x } { d t ^ { 2 } } = - \frac { M _ { 1 } x } { r _ { \mathrm { j s } } ^ { 3 } } \left[ 1 - \frac { 3 J _ { 2 } r _ { \mathrm { J } } ^ { 2 } } { 2 r _ { \mathrm { j s } } ^ { 2 } } ( 5 \mu ^ { 2 } - 1 ) \right] + \displaystyle \sum _ { i = 1 } ^ { 9 } M _ { i } \frac { x _ { i } - x } { r _ { \mathrm { j s } } ^ { 3 } } - \frac { x _ { i } } { r _ { \mathrm { i s } } ^ { 3 } } } \\ { \displaystyle \frac { d ^ { 2 } y } { d t ^ { 2 } } = - \frac { M _ { \mathrm { J } } y } { r _ { \mathrm { j s } } ^ { 3 } } \left[ 1 - \frac { 3 J _ { 2 } r _ { \mathrm { J } } ^ { 2 } } { 2 r _ { \mathrm { j s } } ^ { 2 } } ( 5 \mu ^ { 2 } - 1 ) \right] + \displaystyle \sum _ { i = 1 } ^ { 9 } M _ { i } \frac { y _ { i } - y } { r _ { \mathrm { j s } } ^ { 3 } } - \frac { y _ { i } } { r _ { \mathrm { i s } } ^ { 3 } } } \\ { \displaystyle \frac { d ^ { 2 } z } { d t ^ { 2 } } = - \frac { M _ { \mathrm { J } } z } { r _ { \mathrm { j s } } ^ { 3 } } \left[ 1 - \frac { 3 J _ { 2 } r _ { \mathrm { J } } ^ { 2 } } { 2 r _ { \mathrm { j s } } ^ { 2 } } ( 5 \mu ^ { 2 } - 3 ) \right] + \displaystyle \sum _ { i = 1 } ^ { 9 } M _ { i } \frac { z _ { i } - z } { r _ { \mathrm { j s } } ^ { 3 } } - \frac { z _ { i } } { r _ { \mathrm { i s } } ^ { 3 } } } \\ { \displaystyle \mu = \frac { z } { r } } \end{array}
$$

where the perturbing bodies are the Sun and planets. $M _ { \mathrm { J } }$ is the mass of Jupiter; the $M _ { i }$ 'sare the masses of the perturbing bodies; $r _ { \mathrm { { J } } }$ is the radius of Jupiter; $r _ { \mathrm { j s } }$ isJupiter-satellite distance; $x _ { i }$ , $y _ { i }$ ,and $z _ { i }$ are the rectangular components of the satellite-perturbing body distance; $r _ { \mathrm { i s } }$ is the satellite-perturbing body distance; $r _ { \mathrm { i j } }$ is the Jupiter-perturbing body distance.Planetary coordinates are taken from the DE4o5/LE4O5 (seeChapter 8).The reciprocal masses,in solar mass units,and the $J _ { 2 }$ for Jupiter used in integrations are as follows:

<table><tr><td>Sun</td><td>1.0</td><td>Mercury</td><td>6023600.0</td></tr><tr><td>Venus</td><td>408523.5</td><td>Earth</td><td>332946.038</td></tr><tr><td>Mars</td><td>3 098710.0</td><td>Jupiter</td><td>1047.35</td></tr><tr><td>Saturn</td><td>3498.0</td><td>Uranus</td><td>22960.0</td></tr><tr><td>Neptune</td><td>19314.0</td><td>Pluto</td><td>130000000.0</td></tr><tr><td>J ofJupiter</td><td>0.01475</td><td></td><td></td></tr></table>

The starting planetocentric coordinates and velocities from Rohde (199O) are given in Table 9.3.The differential coordinates are computed from Eqs.9.24.

Table 9.3 The starting planetocentric coordinates and velocities of some Jovian satellites (Rohde 1990).Epoch JD $2 4 4 7 8 9 0 . 5 = 1 9 8 9$ December 30   

<table><tr><td colspan="2">Satellite</td><td></td><td>r (au)</td><td>v (au/day)</td></tr><tr><td>VI</td><td>Himalia</td><td>X</td><td>-0.0394627736618</td><td>+0.0013683275790</td></tr><tr><td></td><td></td><td>y</td><td>-0.0722678670569</td><td>-0.0002593437765</td></tr><tr><td></td><td></td><td>Z</td><td>-0.0170810682702</td><td>-0.0010464833518</td></tr><tr><td>VII</td><td>Elara</td><td>X</td><td>-0.0619697457552</td><td>+0.0004392130964</td></tr><tr><td></td><td></td><td>y</td><td>-0.0044124460879</td><td>-0.0020946808809</td></tr><tr><td></td><td></td><td>Z</td><td>+0.0265446659756</td><td>-0.0003974001515</td></tr><tr><td>VIII</td><td>Pasiphae</td><td>X</td><td>-0.0474722144088</td><td>-0.0010182557362</td></tr><tr><td></td><td></td><td>y</td><td>-0.1000885430216</td><td>+0.0011925451174</td></tr><tr><td></td><td></td><td>Z</td><td>-0.0009486933348</td><td>+0.0009171895371</td></tr><tr><td>IX</td><td>Sinope</td><td>X</td><td>-0.0579232252532</td><td>+0.0011014867506</td></tr><tr><td></td><td></td><td>y</td><td>+0.1464131750776</td><td>+0.0002877970106</td></tr><tr><td></td><td></td><td>Z</td><td>+0.0885266909368</td><td>-0.0003615702389</td></tr><tr><td>X</td><td>Lysithea</td><td>X</td><td>+0.0683709404212</td><td>+0.0006111658968</td></tr><tr><td></td><td></td><td>y</td><td>-0.0114622412925</td><td>+0.0012863404782</td></tr><tr><td></td><td></td><td>Z</td><td>-0.0304090473403</td><td>+0.0013466750538</td></tr><tr><td>XI</td><td>Carme</td><td>X</td><td>-0.1221787634075</td><td>-0.0007075200606</td></tr><tr><td></td><td></td><td>y</td><td>-0.1048136497855</td><td>+0.0009285971336</td></tr><tr><td></td><td></td><td>Z</td><td>-0.0685824702747</td><td>+0.0001468741809</td></tr><tr><td>XII</td><td>Ananke</td><td>X</td><td>+0.1246479748900</td><td>-0.0006562509816</td></tr><tr><td></td><td></td><td>y</td><td>-0.0256709692336</td><td>-0.0013514562258</td></tr><tr><td></td><td></td><td>Z</td><td>-0.0203855454615</td><td>+0.0002939680931</td></tr><tr><td>XIII</td><td>Leda</td><td>X</td><td>+0.0356054434403</td><td>+0.0013645601641</td></tr><tr><td></td><td></td><td>y</td><td>-0.0810815597479</td><td>+0.0006286869081</td></tr><tr><td></td><td></td><td>Z</td><td>+0.0052592795262</td><td>+0.0005799993600</td></tr></table>

# 9.9 The Rings and Satellites of Saturn

# 9.9.1The Rings of Saturn

The rings of Saturn liein its equatorial plane.The inclination and ascending node of this plane on the Earth's equator are determined from the north pole of Saturn as defined by Davies et al.(1989).The outer,inner,and dusky rings in this publication correspond to the $A$ , $B$ ,and $C$ rings,respectively.The Cassni division lies between the inner and outer rings. The dimensions of the outer ring and the factors for calculating the relative dimensions of the rings are from Esposito et al.(1984).

The ephemeris of the rings contains the following quantities that determine the Saturnicentric positions of the Earth and Sunreferred to the plane of the rings,upon which the appearance of the rings depends:

$U =$ the geocentric longitude of Saturn,measured in the plane of the rings eastward from its ascending node on the mean equator of the Earth; the Saturnicentric longitude of theEarth,measured in the sameway,is $U + 1 8 0 ^ { \circ }$ .   
$B =$ theSaturnicentric latitude of the Earth referred to the plane of the rings,positive toward the north;when $B$ ispositive,the visible surface of the rings is the northern surface.   
$P =$ the geocentric position angle of the northern semiminor axis of the apparent ellipse of the rings,measured from the north toward the east.   
$U ^ { \prime } =$ the heliocentric longitude of Saturn,measuredinthe plane ofthe rings eastward from its ascending node on the ecliptic;the Saturnicentric longitude of the Sun,measured in the same way, is $U ^ { \prime } + 1 8 0 ^ { \circ }$ .   
$B ^ { \prime } =$ theSaturnicentric latitude ofthe Sun referred to the plane of the rings,positive toward the north;when $B ^ { \prime }$ ispositive,the northern surface of the rings is the illuminated surface.   
$P ^ { \prime } =$ the heliocentric position angle of the northern semiminor axis of the rings on the heliocentric celestial sphere,measured eastward from the circle of latitude through Saturn.

The right ascension and declination of the north pole of Saturn are according to Davies et al. (1989),

$$
\begin{array} { c } { { \alpha _ { \mathrm { S } } = 4 0 { } ^ { \circ } . 5 8 - 0 { } ^ { \circ } . 0 3 6 T } } \\ { { { } } } \\ { { \delta _ { \mathrm { S } } = 8 3 { } ^ { \circ } . 5 4 - 0 { } ^ { \circ } . 0 0 4 T } } \end{array}
$$

where $\alpha _ { \mathrm S }$ and $\delta _ { \mathrm { { S } } }$ arereferred to the equator and equinox of J2Ooo.O and（ $( T =$ $( \mathrm { J D } - 2 4 5 1 5 4 5 . 0 ) / 3 6 5 2 5 )$

Adding the variations due to precession, calculated by the formulae in $\ S 6 . 6 . 2$ ,givesthe elements referred to the ecliptic and mean equinox of date; from them,the inclination, $J$ ,to the mean equator of date and the right ascension, $N$ ,ofthe ascendingnode measured from the mean equinox of date are obtained from

$$
\begin{array} { c } { { J = 9 0 ^ { \circ } - \delta _ { 0 } } } \\ { { N = \alpha _ { 0 } + 9 0 ^ { \circ } . } } \end{array}
$$

The arc $\phi$ from the ascending node of the ring plane on the Earth's equator along the ring plane to its ascending node on the ecliptic is obtained from

$$
\sin N \cot \phi = \cot \varepsilon \sin J - \cos J \cos N
$$

where $\varepsilon$ is the mean obliquity of date.From the elements referred to the equator of the Earth, and from the geocentric equatorial coordinates of Saturn, the ephemeris of $U$ , $B$ ,and $P$ is calculated by Eqs.9.26.These quantitiesare defined with reference to the ring plane in the same way as with reference to the orbital plane of a satellite;but the effect of nutation must firstberemoved from the apparent right ascensionand declination of Saturn,to refer the position of the planet to the same equinox as the elements of the reference plane.

$U ^ { \prime }$ ， $B ^ { \prime }$ ,and $P ^ { \prime }$ may be obtained by formulae exactly analogous to Eqs.9.26 from the ecliptic elements of the plane of the rings and the heliocentric longitude, $l$ ,and latitude, $^ b$ ,of Saturn,referred to the mean equinox of date:

$$
\begin{array} { c } { { \cos B ^ { \prime } \sin P ^ { \prime } = - \sin i \cos ( l - \Omega ) } } \\ { { \cos B ^ { \prime } \cos P ^ { \prime } = + \cos i \cos b + \sin i \sin b \sin ( l - \Omega ) } } \\ { { \sin B ^ { \prime } = - \cos i \sin b + \sin i \cos b \sin ( l - \Omega ) } } \\ { { \cos B ^ { \prime } \sin U ^ { \prime } = + \sin i \sin b + \cos i \cos b \sin ( l - \Omega ) } } \end{array}
$$

The rings become invisible when

1.The ring-plane passes through the Sun,since neither side of the rings is then illuminated.   
2.The ring-plane passes between the Sun and the Earth,since the unilluminated side of the rings is facing the Earth.   
3.The ring-plane passes through the Earth,since the ringsare too thin to be visible edge on.

Twice during each revolution of Saturn around the Sun—near the times when the ringplane passes through the Sun—the Earth usually crosses the ring-plane three times,though occasionally it crosses only once.The last occasion on which only one passage of the Earth through the ring-plane occurred was in 1950.

# 9.9.2 The Satellites of Saturn

TheAstronomical Almanac presents times of greatest eastern elongation for Satellites I-V,times of elongations (eastern and western) and conjunctions for SatelitesVI-VIII,and differential rightascensionsand declinationsfor SatellitesVI-IX.

Eclipses,occultations,transits,and shadow-transits of the satellites occur duringa limited periodeach time the Earth passes through the plane of the rings.Methods for calculating these phenomena are described by Comrie (1934).See also Taylor(1951).

Ephemerides are not provided for SatelitesX-LII although orbital, physical,and photometricdata are listed foranumberof these satellites on pagesF2-F5of The Astronomical Almanacand forall of thesesatellitesatTheAstronomical Almanac Onlinewebsite.Janus wasdiscovered in1967.Epimetheus,Helene,Telesto,andCalypso satellites werediscovered byground-based observations during 198o.Atlas,Prometheus,and Pandora were discovered byVoyager.Many of the satellitesare co-orbital. Janus and Epimetheus follow horseshoe paths in a reference frame rotating at their mean orbital speed.Telesto and Calypso orbit at the $L _ { 4 }$ and $L _ { 5 }$ Lagrangian points of Tethys.Helene is near the $L _ { 4 }$ Lagrangian point of Dione. Pandora and Prometheus are the shepherd satellites of the F-ring.

9.9.2.1Mimas,Enceladus,Tethys,andDione The orbital theories for Mimas,Enceladus,Tethys,and Dione are based on Kozai (1957). The values of the elements for Mimas,Enceladus,Tethys,and Dione are from Taylor and

![](images/13c0a1702e8c24a0eec5e849f589a7ca84d03afde407cf19074b29cea3076e09.jpg)  
Figure9.13 Reference plane forMimas,Enceladus,Tethysand Dione. $\theta _ { 1 } =$ $\Upsilon B + B C$ , $P = \Upsilon B + B C + C D$ , $N = \Upsilon E$ ,and $L _ { 1 } = \Upsilon B + B C + C D + \mathrm { m e a n }$ anomaly. $\Omega _ { e }$ and $e _ { e }$ arethe ascending node and inclination of Saturn's equator relativeto theEarth'sequatorand equinoxofB1950.O,respectively.Valuesused are $\Omega _ { e } = 1 6 8 . 8 3 8 7$ and $i _ { e } = 2 8 . 0 6 5 3$ .

Shen (1988),with mean motion and secular rates for Mimas and Enceladus from Kozai and corresponding quantities for Tethysand Dione from Garcia (1972).The elements ofMimas, Enceladus,Tethys,and Dione are referred to the B1950.O equator of Saturn (see Fig.9.13). The only significant periodic perturbations on these satellites are the mutual perturbations of Mimas and Tethys,and those of Enceladus and Dione.In each case,they are caused bya close 2:1 commensurability of mean motions.These perturbations affect the longitude and are denoted by $\Delta L$ .

The orbital elements of Mimas are as follows:

$$
\begin{array} { r l } & { d = \mathbb { D } = 2 4 1 0 9 3 . 0 } \\ & { t = d / 3 6 5 . 2 5 } \\ & { T = \zeta . 0 6 1 6 ( ( \mathbb { D } - 2 4 3 3 2 8 2 . 4 2 3 ) / 3 6 5 . 2 5 ) + 1 9 5 0 . 0 - 1 8 6 6 . 0 6 } \\ & { a = 0 . 0 0 1 2 4 1 7 1 u } \\ & { n = 3 8 1 9 9 4 5 1 6 / 2 { \mathrm { d i a p } } } \\ & { e = 0 . 0 1 9 8 6 } \\ & { \gamma = 1 . 5 7 0 } \\ & { \theta _ { 1 } = 4 9 2 4 - 3 6 5 0 2 5 t } \\ & { L _ { 1 } = 1 2 8 8 5 3 9 + n d - 4 3 2 4 1 5 \sin T - 0 . 7 7 1 4 \sin 3 T } \\ & { \quad - 0 . 5 0 2 0 8 1 5 T } \\ & { P = 1 0 7 5 0 . 3 6 5 5 6 0 t } \end{array}
$$

where $a$ is the semimajor axis; $n$ the daily mean motion; $e$ the eccentricity; $\gamma$ the inclination of the orbital plane to Saturn's equator; $\theta _ { 1 }$ the longitude of the ascending node; $L _ { 1 }$ the mean longitude;and $P$ the longitude of the pericenter.

The orbital elements of Enceladus are given by:

$$
\begin{array} { r l } & { d = \tt I D - 2 4 1 1 0 9 3 . 0 } \\ & { t = d / 3 6 . 5 2 5 } \\ & { a = 0 . 0 0 1 5 8 9 3 5 \tt a u } \\ & { n = 2 6 2 7 3 1 9 0 5 2 / \tt d a y } \\ & { e = 0 . 0 0 5 3 2 } \\ & { \gamma = 0 . 0 3 6 } \\ & { \theta _ { 1 } = 1 4 5 ^ { \circ } - 1 5 2 7 7 t } \\ & { L _ { 1 } = 2 0 ^ { ( 0 . 1 5 5 + n \ d + 1 5 . 7 3 8 \sin { ( 5 9 ^ { \circ } 4 + 3 2 ^ { \circ } 7 3 t ) } } } \\ & { \quad \quad + 1 3 . 7 0 4 \sin { ( 1 1 9 9 2 + 9 3 ^ { \circ } 1 8 t ) } } \\ & { P = 3 1 2 7 7 + 1 2 3 ^ { \circ } 4 2 t } \end{array}
$$

where the variablesare defined in the same manner as for Mimas.

The orbital elements of Tethys are as follows:

$$
\begin{array} { r l } & { d = \mathbb { I D } - 2 4 1 0 9 3 , 0 } \\ & { t = d / 3 6 5 . 2 5 } \\ & { T = 5 . 0 6 1 6 \big ( ( \mathbb { I D } - 2 4 3 3 2 8 2 . 4 2 3 ) / 3 6 5 . 2 5 \big ) + 1 9 5 0 . 0 - 1 8 6 6 . 0 6 } \\ & { a = 0 . 0 0 1 9 7 0 6 9 . 0 } \\ & { n = 1 9 0 . 6 7 9 9 2 0 2 7 8 / \mathrm { d i y } } \\ & { e = 0 . 0 0 0 2 1 2 } \\ & { \gamma = \Gamma . 1 1 2 1 } \\ & { \theta _ { 1 } = 1 1 7 4 . 1 7 2 7 2 4 7 5 4 t } \\ & { L _ { 1 } = 2 8 4 . 9 9 8 2 + n d + 2 5 0 7 5 1 \sin T + 0 . 7 0 3 4 1 \sin 3 T } \\ & { \quad + 0 . 7 0 0 1 0 \sin 5 T } \\ & { P = 9 7 2 7 2 9 2 t } \end{array}
$$

where the variablesare defined in the same manner as for Mimas.

The orbital elements of Dione are given by:

$$
\begin{array} { r l } & { d = \tt I D - 2 4 1 1 0 9 3 . 0 } \\ & { t = d / 3 6 . 5 2 5 } \\ & { a = 0 . 0 0 2 5 2 4 1 3 \tt a u } \\ & { n = 1 3 1 5 5 3 4 9 2 0 0 2 6 / \tt d a y } \\ & { e = 0 . 0 0 1 7 1 5 } \\ & { \gamma = 0 . 0 5 0 8 9 } \\ & { \theta _ { 1 } = 2 2 8 ^ { - } - 3 0 . 5 6 1 9 7 t } \\ & { L _ { 1 } = 2 5 5 . 1 1 8 3 + n d - 0 . 7 8 8 \sin { ( 5 9 ^ { 2 } 4 + 3 2 ^ { 5 } 7 3 t ) } } \\ & { \quad - 0 . 7 7 5 \sin { ( 1 1 9 ^ { 2 } 5 2 + 9 3 ^ { 5 } 1 8 t ) } } \\ & { P = 1 7 3 6 6 + 3 0 ^ { 9 } 8 3 8 1 t } \end{array}
$$

where the variablesare defined in the same manneras forMimas.

Todetermine the times of greatest eastern elongation we must first find the orbital longitude, $\boldsymbol { u }$ ；the longitude of the ascending node $N$ of the orbit on the Earth's equator; and the inclination of the orbit to the Earth's equator, $J$ .From spherical trigonometry we have from triangle $B F C$ in Fig.9.13,

$$
\begin{array} { r l } & { \sin i \sin B F = \sin \gamma \sin ( \theta _ { 1 } - \Omega _ { \mathrm { e } } ) } \\ & { \sin i \cos B F = \cos \gamma \sin i _ { \mathrm { e } } + \sin \gamma \cos i _ { \mathrm { e } } \cos ( \theta _ { 1 } - \Omega _ { \mathrm { e } } ) } \end{array}
$$

which can be solved for $B F$ and $i$ .The arc length $F C$ and its quadrant can be found from the equations

$$
\begin{array} { l } { \sin i \sin F C = \sin ( \theta _ { 1 } - \Omega _ { \mathrm { e } } ) \sin i _ { \mathrm { e } } } \\ { \sin i \cos F C = \cos i _ { e } \sin \gamma + \sin i _ { \mathrm { e } } \cos \gamma \cos ( \theta _ { 1 } - \Omega _ { \mathrm { e } } ) . } \end{array}
$$

Similarly,from the triangle $\Upsilon _ { E F }$ we have

$$
\begin{array} { l } { \sin J \sin N = \sin i \sin ( \Omega _ { \mathrm { e } } + B F ) } \\ { \sin J \cos N = \cos i \sin \varepsilon + \sin i \cos \varepsilon \cos ( \Omega _ { \mathrm { e } } + B F ) } \end{array}
$$

which can be solved for $J$ and $N$ .Then the arc $E F$ and its quadrant can be found from

$$
\begin{array} { l } { \sin J \sin E F = \sin ( \Omega _ { \mathrm { e } } + B F ) \sin \varepsilon } \\ { \sin J \cos E F = \cos \varepsilon \sin i + \sin \varepsilon \cos i \cos ( \Omega _ { \mathrm { e } } + B F ) } \end{array}
$$

$u$ then follows from

$$
u = P - \theta _ { 1 } + E F + F C + \mathrm { t r u e \ a n o m a l y } .
$$

The tabulated orbital elements $\gamma , a$ ,and $e$ are listed above. The remaining elements must be computed. From the spherical triangle $\Upsilon A B$ in Fig. 9.13 we have

$$
\begin{array} { r l } & { \sin J _ { \mathrm { e } } \sin A B = \sin \varepsilon \sin \Omega _ { \mathrm { e } } } \\ & { \sin J _ { \mathrm { e } } \cos A B = \cos \varepsilon \sin i _ { \mathrm { e } } + \sin \varepsilon \cos i _ { \mathrm { e } } \cos \Omega _ { \mathrm { e } } } \end{array}
$$

which can be solved for $A B$ .

Then

$$
\begin{array} { c } { \theta = \theta _ { 1 } - \Omega _ { \mathrm { e } } + A B } \\ { \boldsymbol { L } = \boldsymbol { L } _ { 1 } - \Omega _ { \mathrm { e } } + A B } \\ { M = \boldsymbol { L } _ { 1 } - P . } \end{array}
$$

9.9.2.2Rhea,Titan, Hyperion,and lapetus

The orbital theories for Rhea and Titanare from Sinclair (1977).The orbital elements are from Taylor and Shen (1988) with the mean motions and secular rates used from Garcia (1972).The theory and orbital elements for Hyperion are from Taylor(1984).The theory for the motion of Iapetus is taken from Sinclair(1974) with some additional periodic terms from Harper et al.(1988).The orbital elements for Iapetus are from Taylor and Shen (1988).

Because of the oblateness of Saturn and solar perturbations,the orbit plane of Rhea precesses at aconstant inclination around the Laplacian plane of Rhea.Because we are using the eclipticas the reference plane,this motion around theLaplacian plane appears as periodic variations in $\lambda$ ， $\varpi$ , $\Omega$ ,and $i$ The osculating elements are given by:

$$
\gamma _ { 0 } = 0 . 3 3 0 5
$$

$$
\lambda = 3 5 9 . 4 7 2 7 + n d
$$

$$
i = i _ { \mathrm { e } } - 0 . 0 4 5 5
$$

where

$$
\begin{array} { r l } & { \pi = 3 0 5 ^ { \circ } + 1 0 ^ { \circ } 2 0 7 7 t } \\ & { \varpi _ { \mathrm { T } } = 2 7 6 ^ { \circ } . 4 9 + 0 ^ { \circ } . 5 2 1 9 ( \mathrm { J D } - 2 4 1 1 3 6 8 . 0 ) / 3 6 5 . 2 5 } \\ & { N _ { \mathrm { T } } = 4 4 ^ { \circ } . 5 - 0 ^ { \circ } . 5 2 1 9 ( \mathrm { J D } - 2 4 1 1 3 6 8 . 0 ) / 3 6 5 . 2 5 } \\ & { \kappa = 5 7 . 2 9 5 7 8 } \\ & { d = \mathrm { J D } - 2 4 1 1 0 9 3 . 0 } \\ & { t = d / 3 6 5 . 2 5 . } \end{array}
$$

Here $a$ is the semimajor axis; $n$ is the daily mean motion; $e$ is the eccentricity; $\varpi$ and $\lambda$ are thelongitude of pericenter and the mean longitude,respectively,reckoned from the vernal equinox along the ecliptic to the ascending node and thence along the orbit; $i$ and $\Omega$ are the inclination and ascending node of the orbit with respect to the ecliptic of 195o.0.The angular elements are shown in Fig. 9.14.

The coefficient 0.Ooio0 in the expressions for $e$ sin $\varpi$ and $e$ cos $\varpi$ isa forced eccentricity dueto Titan.Thealgebraic expression for thisisgiven in Sinclair(1977).The inclination and node of Rhea's Laplacian plane relative to the ecliptic (1950.0)are $i = i _ { \mathrm { e } } - 0 . 0 4 5 5$ and $\Omega = \Omega _ { \mathrm { e } } - 0 . 0 0 7 8$

There are a number of significant solar perturbations on Titan’s orbit and,as for Rhea, 入， $\Omega$ ，and $i$ areaffected by periodic variations due to the reference plane not being the Laplacian plane. The solar perturbations are functions of the mean elements of the apparent orbit of the Sun about Saturn. The solar elements needed are $\lambda _ { \mathrm { s } }$ ， $\Omega _ { \mathrm { s } }$ ,and $i _ { \mathrm { s } }$ (which are defined inFig.9.15),and $l _ { \mathrm { s } }$ ,the mean anomaly.Approximate values of $i$ , $\Omega$ ,and $\varpi$ are also needed,and these are denoted by $i _ { \mathrm { a } }$ , $\Omega _ { \mathrm { a } }$ ,and $\varpi _ { \mathrm { a } }$ These quantities are given by thefollowing expressions:

![](images/fd0b3ddc930801587dfdec02d3bf3655bb1db2824c637dddf2af74c20a8029dd.jpg)  
Figure9.14 Reference system for Rhea,Titan,Hyperion,Iapetus,andPhoebe. $\varpi = \cap { \cal F } + { \cal F } D$ and $\lambda = \Upsilon _ { F } + F D +$ mean anomaly.

![](images/2a9e72a5d3dd2d7a6495a68ad1cf9cf11ee0bcd6704a42f175e3bcb78cff1df6.jpg)  
Figure9.15 Angles needed to evaluate solar perturbations on Titan. $\Omega _ { \mathrm { a } } = \Upsilon D$ , $\theta = \Upsilon A + A B$ , $\varpi _ { \mathrm { a } } = \Upsilon D + D C$ ,and $\lambda _ { s } = \Upsilon { \cal A } + { \cal A } E$ .

$$
\begin{array} { r l } & { T = ( { \bf D } - 2 4 1 5 0 2 0 , 0 ) / 3 6 5 2 5 } \\ & { I _ { s } = 1 7 5 4 7 6 2 + 1 2 1 2 5 5 1 5 1 7 } \\ & { i _ { s } = 2 5 4 9 1 + 0 . 7 0 0 2 4 3 5 T } \\ & { \Omega _ { s } = 1 1 3 3 5 3 0 - 0 . 2 5 9 7 T } \\ & { \partial _ { s } = 1 1 3 3 5 6 3 - 0 . 2 5 9 7 1 3 6 T } \\ & { i _ { s } = 2 6 7 2 6 3 5 4 1 2 2 5 1 1 3 6 T } \\ & { t = ( { \bf D } - 2 4 1 1 3 6 8 , 0 ) / 3 6 5 2 2 5 } \\ & { \kappa = 5 7 2 9 5 7 8 } \\ & { \gamma _ { 0 } = 0 . 2 5 9 0 0 } \\ & { i _ { s } = i _ { s } - 0 . 5 6 2 6 0 4 + \kappa \sin \gamma _ { 0 } \cos ( 4 1 7 2 8 - 0 5 5 2 1 9 t ) } \\ & { \Omega _ { a } = \Omega _ { e } - 0 . 0 7 4 1 8 + \kappa \sin \gamma _ { 0 } \sin ( 4 1 7 2 8 - 0 ^ { 1 5 } 2 1 9 t ) / \sin i _ { e } } \\ & { \Omega _ { s } = 2 2 5 5 8 3 7 + 0 ^ { 1 5 } 2 1 9 t . } \end{array}
$$

The quantities $( i _ { \mathrm { e } } - 0 . 6 2 0 4 )$ and $( \Omega _ { \mathrm { e } } - 0 . 1 4 1 8 )$ define the inclination and node of the Laplacian planeof Titan.The auxiliary angles- $\theta , \Gamma , \Psi , g$ ,and $L _ { \mathrm { s } }$ —are given by:

$$
\begin{array} { c } { \cos \Gamma = \cos i _ { s } \cos i _ { \mathrm { a } } + \sin i _ { s } \sin i _ { \mathrm { a } } \cos ( \Omega _ { \mathrm { a } } - \Omega _ { s } ) } \\ { \sin \Gamma \sin \Psi = \sin i _ { s } \sin ( \Omega _ { \mathrm { a } } - \Omega _ { s } ) } \\ { \sin \Gamma \cos \Psi = \cos i _ { s } \sin i _ { \mathrm { a } } - \sin i _ { s } \cos i _ { \mathrm { a } } \cos ( \Omega _ { \mathrm { a } } - \Omega _ { s } ) } \\ { \sin \Gamma \sin ( \theta - \Omega _ { s } ) = \sin i _ { \mathrm { a } } \sin ( \Omega _ { \mathrm { a } } - \Omega _ { s } ) } \\ { \sin \Gamma \cos ( \theta - \Omega _ { s } ) = - \sin i _ { s } \cos i _ { \mathrm { a } } } \\ { + \cos i _ { s } \sin i _ { \mathrm { a } } \cos ( \Omega _ { \mathrm { a } } - \Omega _ { s } ) } \\ { L _ { s } = \lambda _ { s } - ( \theta - \Omega _ { s } ) - \Omega _ { s } } \\ { g = \varpi _ { s } - \Omega _ { \mathrm { a } } - \Psi . } \end{array}
$$

The osculating elements of Titan are given by:

$$
\begin{array} { r l } & { a = 0 . 0 0 8 1 6 7 6 5 8 \mathrm { a t } } \\ & { n = 2 2 5 7 6 9 7 3 8 5 / 2 \mathrm { a y } } \\ & { e = 0 . 0 2 8 8 1 5 - 0 . 0 0 0 1 8 4 \mathrm { c o s } 2 g + 0 . 0 0 0 0 7 3 \mathrm { c o s } 2 ( L _ { s } - g ) } \\ & { = m _ { \mathrm { a } } + \kappa [ 0 . 0 0 6 3 0 \mathrm { s } 0 . 2 g + 0 . 0 0 0 2 5 0 \mathrm { s } \mathrm { m } 2 ( L _ { s } - g ) ] } \\ & { \lambda = 2 6 5 3 1 2 1 + n d + \kappa [ \sin \gamma _ { 0 } \tan { \frac { 1 } { 2 } } i _ { \mathrm { c } } \sin ( 4 1 5 2 8 } \\ & { \quad - 0 . 5 2 1 9 \tau ) - 0 . 0 0 0 1 7 6 \mathrm { s } \mathrm { m } 1 . } \\ & { \quad \quad + 0 . 0 0 0 0 5 7 \sin ( 2 L _ { s } + \Psi ) ] } \\ & { i = i _ { \mathrm { a } } + 0 . 0 0 0 0 2 3 2 \kappa \cos ( 2 L _ { s } + \Psi ) } \\ & { \quad \quad - 0 . 0 0 0 5 0 3 \kappa \sin ( 2 L _ { s } + \Psi ) } \end{array}
$$

where $d = \mathrm { J D } - 2 4 1 1 3 6 8 . 0 ; t = d / 3 6 5 . 2 5$ and $\kappa = 5 7 . 2 9 5 7 8$

The algebraic expressions for the coefficients of these periodic terms are given in Sinclair (1977).

The osculating elements of Hyperion's orbit are given by:

$$
+ 0 . 0 0 0 1 3 \cos ( 3 1 ^ { \circ } . 9 + 6 1 ^ { \circ } . 7 5 2 4 T )
$$

$$
- 0 . 0 1 8 \sin ( 1 3 ^ { \circ } + 2 4 . 4 4 T ) ) / \sin ( i _ { \mathrm { e } } - 0 . 7 4 7 )
$$

$$
\lambda = 1 7 6 \% 7 4 8 1 + n d + 0 \% 5 1 5 0 7 \sin ( 1 0 5 \% 3 1 - 2 \% 3 9 2 T )
$$

$$
+ 0 \% 1 9 2 \sin ( \zeta - \tau ) - 0 \% 9 1 \sin \zeta + 0 \% 2 1 1 \sin ( \zeta + \tau )
$$

where

$$
\begin{array} { r l } & { d = \mathrm { J D } - 2 4 1 5 0 2 0 . 0 } \\ & { T = \mathrm { J D } - 2 4 3 3 2 8 2 . 4 2 3 4 5 9 0 5 ) / 3 6 5 . 2 4 2 2 + 5 0 . 0 } \\ & { \tau = 9 3 ^ { \circ } 1 3 + 0 ^ { \circ } . 5 6 2 0 3 9 d } \\ & { \zeta = 1 4 8 ^ { \circ } 7 2 - 1 9 . 1 8 4 T . } \end{array}
$$

Here again the elements are reckoned in the same way as for Rhea.

The orbital plane of Iapetus is inclined at about $8 ^ { \circ }$ to itsLaplacian plane,which is itself inclined at about $1 5 ^ { \circ }$ to the equatorial plane of Saturn,and $1 2 ^ { \circ }$ to the orbital plane of Saturn. Asaresult,the motion of the orbital plane of Iapetus is quite complicated,and is described by cubic polynomials in time for $i$ and $\Omega$ .The osculating elements are computed as follows:

$$
\begin{array} { r l } & { t = \mathrm { J D } - 2 4 0 9 7 8 6 . 0 } \\ & { t _ { \mathrm { c } } = t / 3 6 5 2 5 } \\ & { T = ( \mathrm { J D } - 2 4 1 5 0 2 0 . 0 ) / 3 6 5 2 5 . } \end{array}
$$

The elements computed from constant and secular terms are:

$$
\begin{array} { r l } & { a = 0 . 0 2 3 8 0 9 8 4 \mathrm { a u } } \\ & { n = 4 \% 5 3 7 9 5 7 1 1 / \mathrm { d a y } } \\ & { e = 0 . 0 2 8 8 1 8 4 + 0 . 0 0 0 5 7 5 t _ { \mathrm { c } } } \\ & { i = 1 8 \% 4 5 9 5 9 - 0 . 9 9 5 5 5 t _ { \mathrm { c } } - 0 . 0 7 2 0 t _ { \mathrm { c } } ^ { 2 } + 0 . 5 0 0 5 4 t _ { \mathrm { c } } ^ { 3 } } \\ & { \lambda = 7 6 . 5 1 9 8 5 4 + n t } \\ & { \varpi = 3 5 2 9 9 5 + 1 1 ^ { \circ } 6 5 t _ { \mathrm { c } } } \\ & { \Omega = 1 4 3 \% 1 2 9 4 - 3 \% 9 7 7 t _ { \mathrm { c } } + 0 . 5 1 1 6 t _ { \mathrm { c } } ^ { 2 } + 0 . 0 0 8 t _ { \mathrm { c } } ^ { 3 } . } \end{array}
$$

Theauxiliary angles needed to compute periodic terms are calculated as follows:

$$
{ \begin{array} { r l } & { \theta = 4 { \mathrm { s } } ^ { 2 } { \mathrm { 6 } } 7 - 0 { \mathrm { . 1 } } 9 5 T } \\ & { \Theta = 1 4 6 { \mathrm { s } } 8 1 9 - 3 { \mathrm { . 9 } } 1 8 T } \\ & { \lambda _ { \mathrm { s } } = 2 6 7 { \mathrm { . 2 } } 6 3 + 1 2 2 2 { \mathrm { . 1 } } 1 4 T } \\ & { w _ { \mathrm { s } } = 9 { \mathrm { 1 } } ^ { \circ } 7 9 6 + 0 { \mathrm { 5 } } 6 { \mathrm { 2 } } 7 } \\ & { \lambda _ { \mathrm { T } } = 2 6 { \mathrm { 1 } } ^ { \circ } 3 1 9 + 2 { \mathrm { 2 } } ^ { \circ } 5 7 6 9 7 4 ( { \mathrm { I D } } - 2 4 1 1 3 6 8 . 0 ) } \\ & { w _ { \mathrm { T } } = 2 7 7 { \mathrm { 1 } } 0 2 + 0 { \mathrm { . 0 } } 0 1 3 8 9 ( { \mathrm { J D } } - 2 4 1 1 3 6 8 . 0 ) } \\ & { \phi = 6 0 { \mathrm { . 4 } } 7 0 + 1 { \mathrm { 5 } } { \mathrm { 2 } } 1 } \\ & { \Phi = 2 0 { \mathrm { 5 } } ^ { \circ } 0 5 5 - 2 { \mathrm { 5 } } 0 1 T . } \end{array} }
$$

From these we compute the following:

$$
\begin{array} { c } { { l = \lambda - \varpi } } \\ { { l _ { s } = \lambda _ { s } - \varpi _ { s } } } \\ { { l _ { \Gamma } = \lambda _ { \mathrm { T } } - \varpi _ { \mathrm { T } } } } \\ { { g = \varpi - \Omega - \theta } } \\ { { g _ { s } = \varpi _ { s } - \Theta } } \\ { { g _ { \Gamma } = \varpi _ { \mathrm { T } } - \Phi } } \\ { { g _ { 1 } = \varpi - \Omega - \phi } } \end{array}
$$

Some of the expressions fr the perturbations involve $e$ and $i$ .For these the following expressions are used.

$$
\begin{array} { l } { { e = 0 . 0 2 8 8 1 8 4 + 0 . 0 0 0 5 7 5 t _ { \mathrm { c } } } } \\ { { { } } } \\ { { i = 1 8 { : } 4 5 9 5 9 - 0 . 9 5 5 5 t _ { \mathrm { c } } - 0 . 0 7 2 0 t _ { \mathrm { c } } ^ { 2 } + 0 { : } 0 0 5 4 t _ { \mathrm { c } } ^ { 3 } . } } \end{array}
$$

The following perturbations are to be added to the elements

$$
\begin{array} { r l } & { \Delta a = 1 0 ^ { - 5 } a [ 7 . 8 7 \cos ( 2 l + 2 g - 2 l _ { \mathrm { s } } - 2 g _ { \mathrm { s } } ) + 9 8 . 7 9 \cos ( l + g _ { \mathrm { l } } - l _ { \mathrm { T } } - g _ { \mathrm { T } } ) ] } \\ & { \Delta e = 1 0 ^ { - 5 } [ - 1 4 0 . 9 7 \cos ( g _ { \mathrm { l } } - g _ { \mathrm { T } } ) + 3 7 . 3 3 \cos ( 2 l _ { \mathrm { s } } + 2 g _ { \mathrm { s } } - 2 g ) } \\ & { \qquad + 1 1 . 8 0 \cos ( l + 2 g - 2 l _ { \mathrm { s } } - 2 g _ { \mathrm { s } } ) + 2 4 . 0 8 \cos { l } + 2 8 . 4 9 \cos ( 2 l + g _ { \mathrm { l } } - l _ { \mathrm { T } } - g _ { \mathrm { T } } ) } \\ & { \qquad + 6 1 . 9 0 \cos ( l _ { \mathrm { T } } + g _ { \mathrm { T } } - g _ { \mathrm { l } } ) + 0 . 4 9 6 \cos ( 3 l _ { \mathrm { s } } + 2 g _ { \mathrm { s } } - 2 g ) ] } \end{array}
$$

$$
+ 0 \% 0 0 5 8 \cos ( 3 l _ { \mathrm { s } } + 2 g _ { \mathrm { s } } ) - 0 \% 0 2 4 \cos ( l _ { \mathrm { s } } + 2 g _ { \mathrm { s } } )
$$

$$
\Delta \lambda = \mathrm { ~ - } 0 . 0 4 2 ~ 9 9 \sin ( l + g _ { \mathrm { l } } - l _ { \mathrm { T } } - g _ { \mathrm { T } } ) - 0 . 0 0 7 8 9 \sin ( 2 l + 2 g - 2 l _ { \mathrm { s } } - 2 g _ { \mathrm { s } } )
$$

$$
+ 0 \% 0 0 6 5 0 \sin ( 2 l _ { \mathrm { s } } + 2 g _ { \mathrm { s } } + \theta )
$$

$$
\begin{array} { r l } & { \Delta \varpi = [ 0 ^ { \mathrm { { g } } } 0 8 0 0 7 7 \sin ( g _ { \mathrm { I } } - g _ { \mathrm { T } } ) + 0 ^ { \mathrm { { c } } } 0 2 1 3 9 \sin ( 2 l _ { \mathrm { s } } + 2 g _ { \mathrm { s } } - 2 g ) } \\ & { \qquad - 0 ^ { \mathrm { { c } } } 0 0 6 7 6 \sin ( l + 2 g - 2 l _ { \mathrm { s } } - 2 g _ { \mathrm { s } } ) + 0 ^ { \mathrm { { c } } } 0 1 3 8 0 \sin l } \\ & { \qquad + 0 ^ { \mathrm { { c } } } 0 1 6 3 2 \sin ( 2 l + g _ { \mathrm { 1 } } - l _ { \mathrm { T } } - g _ { \mathrm { T } } ) + 0 ^ { \mathrm { { c } } } 0 3 5 4 7 \sin ( l _ { \mathrm { T } } + g _ { \mathrm { T } } - g _ { \mathrm { 1 } } ) } \\ & { \qquad + 0 ^ { \mathrm { { c } } } 0 0 0 2 8 \sin ( 3 l _ { \mathrm { s } } + 2 g _ { \mathrm { s } } - 2 g ) ] / e } \\ & { \Delta \Omega = [ 0 ^ { \mathrm { { g } } } 0 4 2 0 4 \sin ( 2 l _ { \mathrm { s } } + 2 g _ { \mathrm { s } } + \theta ) + 0 ^ { \mathrm { { c } } } 0 0 2 3 5 \sin ( l + g _ { \mathrm { 1 } } + l _ { \mathrm { T } } + g _ { \mathrm { T } } + \phi ) } \\ & { \qquad + 0 ^ { \mathrm { { c } } } 0 0 3 5 8 \sin ( l + g _ { \mathrm { 1 } } - l _ { \mathrm { T } } - g _ { \mathrm { T } } + \phi ) - 0 ^ { \mathrm { { c } } } 0 0 6 \sin 2 l _ { \mathrm { s } } } \\ & { \qquad + 0 ^ { \mathrm { { c } } } 0 0 0 3 \sin ( 4 l _ { \mathrm { s } } + 2 g _ { \mathrm { s } } ) + 0 ^ { \mathrm { { g } } } 0 2 8 \sin ( 3 l _ { \mathrm { s } } + 2 g _ { \mathrm { s } } ) } \\ & { \qquad - 0 ^ { \mathrm { { c } } } 0 0 1 2 \sin ( l _ { \mathrm { s } } + 2 g _ { \mathrm { s } } ) - 0 ^ { \mathrm { { g } } } 0 1 4 2 \sin l _ { \mathrm { s } } / \sin ( l _ { \mathrm { s } } + 2 g _ { \mathrm { s } } ) } \\ &  \qquad - 0 ^ { \mathrm { { c } } } 0 0 1 2 \sin ( { l _ { \mathrm { s } } } + 2 g _  \mathrm \end{array}
$$

To determine $J , u$ ,and $N$ ,we can use the spherical triangle $\Upsilon _ { E F }$ in Fig.9.14 to obtain

$$
\begin{array} { l } { \sin J \sin N = \sin i \sin \Omega } \\ { \sin J \cos N = \cos i \sin \varepsilon + \sin i \cos \varepsilon \cos \Omega } \end{array}
$$

which can be solved for $N$ and $J$ .The arc $\phi$ can be found from the equation

$$
\sin J \sin \phi = \sin \Omega \sin \varepsilon .
$$

$u$ then follows from

$$
u = \varpi - \Omega + \phi + \mathrm { t r u e \ a n o m a l y } .
$$

The tabulated orbital elements $a$ and $e$ were shown previously. The remaining elements are computed as follows.To calculate $\theta$ we first find the arc $A C$ inFig.9.13.From spherical trigonometry we have for the triangle $A E C$ ：

$$
\sin ( N - N _ { \mathrm { e } } ) \cot \theta = \cos ( N - N _ { \mathrm { e } } ) \cos J _ { \mathrm { e } } - \sin J _ { \mathrm { e } } \cot J
$$

which can be solved for $\theta$ . $M$ is given by

$$
\begin{array} { r } { M = \lambda - \varpi . } \end{array}
$$

$\gamma$ can be determined by the formula

$$
\sin \gamma \sin \theta = \sin { J } \sin ( N - N _ { \mathrm { e } } ) .
$$

$L$ is found by first finding the arc length $F C$ from

$$
\sin { F C } \sin { \gamma } = \sin ( \Omega - \Omega _ { \mathrm { e } } ) \sin i _ { \mathrm { e } } .
$$

$L$ is then given by

$$
L = \lambda - \Omega - F C + \theta .
$$

The differential coordinates ofHyperion and Iapetus are computed as follows:the rectangular coordinates $x$ and $y$ of the satellite in the orbital plane are found from Eqs.9.19.These coordinates are then transformed to the Earth equator and equinox by Eqs.9.2O and 9.21. The differential coordinates $\xi$ and $\eta$ are then computed through Eqs.9.24.

# 9.9.2.3 Phoebe

The orbital elements used inThe Astronomical Almanac are those determinedby Zadunaisky (1954).The ephemerides consist of differential right ascensions and declinations given at 2- day intervals.The elements are referred to the ecliptic and equinox of 1950.0.The values of the elements are as follows:

where

$$
\begin{array} { c } { t = \mathrm { J D } - 2 4 3 3 2 8 2 . 5 } \\ { T = t / 3 6 5 . 2 5 . } \end{array}
$$

$^ a$ is the semimajor axis; $\lambda$ ,the mean longitude measured from the equinox along the ecliptic to the ascending node then along the orbit; $e$ ,the eccentricity; $\varpi$ ,the longitude of the pericenter reckoned from the equinox along the ecliptic to the ascending node then along the orbit to the pericenter; $i$ ,the inclinationof the orbit totheecliptic;and $\Omega$ ,thelongitude of the ascending node of the orbit on the ecliptic reckoned from the equinox.

To compute the differential right ascension and declination, the $x$ and $y$ coordinates in the orbital plane are found using $\mathrm { E q 9 . 1 9 }$ ,where

$$
M = \lambda - \varpi .
$$

The coordinates are transformed to the Earth equator and equinox using Eqs.9.20 and 9.21. Finally, $\Delta \alpha$ and $\Delta \delta$ are computed from $\xi$ and $\eta$ using Eq. 9.24.

# 9.10 The Rings and Satellites of Uranus

Orbital elementsare given for the rings of Uranusas determined by Elliotetal.(1981). Times of greatest northern elongationsare given for Satellites Ithrough V;Ariel,Umbriel, Titania,Oberon,andMiranda.The orbital elementsof these satellitesare fromLaskarand Jacobson (1987).The theory is developed in elliptical elements.Leading secularand periodic perturbations in the elements are quoted below.

Miranda

$$
+ 0 . 0 2 5 4 7 2 1 7 \sin ( - 2 . 1 8 1 6 7 \times 1 0 ^ { - 4 } \times 2 \pi T + 1 . 3 2 )
$$

$$
- 0 . 0 0 3 0 8 8 3 1 \sin ( - 4 . 3 6 3 3 6 \times 1 0 ^ { - 4 } \times 2 \pi T + 2 . 6 4 )
$$

$$
+ 1 . 9 4 1 0 \times 1 0 ^ { - 4 } \exp { i ( 0 . 7 0 7 \times 2 \pi T + 6 . 0 5 ) }
$$

$$
\zeta = 0 . 0 3 7 8 7 1 7 1 \exp i ( - 1 . 5 4 4 4 9 \times 1 0 ^ { - 4 } \times 2 \pi T + 5 . 7 0 ) .
$$

Ariel

$$
m / M _ { \mathrm { U } } = 1 . 4 9 \times 1 0 ^ { - 5 }
$$

$$
- 1 . 8 6 0 5 0 \times 1 0 ^ { - 3 } \sin ( - 2 . 1 8 1 6 7 \times 1 0 ^ { - 4 } \times 2 \pi T + 1 . 3 2 )
$$

$$
+ 2 . 1 9 9 9 \times 1 0 ^ { - 4 } \sin ( - 4 . 3 6 3 3 6 \times 1 0 ^ { - 4 } \times 2 \pi T + 2 . 6 4 ) \mathrm { r a d i a n s }
$$

$$
z = 1 . 1 8 7 6 3 \times 1 0 ^ { - 3 } \exp i ( 4 . 7 2 7 8 2 4 \times 1 0 ^ { - 5 } \times 2 \pi T + 2 . 4 1 )
$$

$$
+ 8 . 6 1 5 9 \times 1 0 ^ { - 4 } \exp i ( 2 . 1 7 9 3 1 6 \times 1 0 ^ { - 5 } \times 2 \pi T + 2 . 0 7 )
$$

$$
\begin{array} { l } { { \zeta = 3 . 5 8 2 5 \times 1 0 ^ { - 4 } \exp { i ( - 4 . 7 8 2 4 7 4 \times 1 0 ^ { - 5 } \times 2 \pi T + 0 . 4 0 ) } } } \\ { { \qquad + 2 . 9 0 0 8 \times 1 0 ^ { - 4 } \exp { i ( - 2 . 1 5 6 6 2 8 \times 1 0 ^ { - 5 } \times 2 \pi T + 0 . 5 9 ) } . } } \end{array}
$$

Umbriel

$$
+ 3 . 0 9 1 7 \times 1 0 ^ { - 4 } \exp i ( 1 . 5 8 0 5 2 4 \times 1 0 ^ { - 5 } \times 2 \pi T + 0 . 7 4 )
$$

$$
+ 2 . 2 1 9 2 \times 1 0 ^ { - 4 } \exp i ( 2 . 9 3 6 3 0 6 8 \times 1 0 ^ { - 6 } \times 2 \pi T + 0 . 4 3 )
$$

$$
+ 5 . 4 9 2 3 \times 1 0 ^ { - 4 } \exp i ( - 0 . 0 1 1 5 7 \times 2 \pi T + 5 . 7 1 )
$$

$$
\zeta = 1 . 1 1 3 3 6 \times 1 0 ^ { - 3 } \exp { i ( - 2 . 1 5 6 6 2 8 \times 2 \pi T + 0 . 5 9 ) }
$$

$$
+ 3 . 5 0 1 4 \times 1 0 ^ { - 4 } \exp { i ( - 1 . 4 0 1 3 7 3 \times 1 0 ^ { - 5 } \times 2 \pi T + 1 . 7 5 ) } .
$$

Titania

$$
m / M _ { \mathrm { U } } = 3 . 9 7 \times 1 0 ^ { - 5 }
$$

$$
\begin{array} { l } { { z = 9 . 3 2 8 1 \times 1 0 ^ { - 4 } \exp i ( 1 . 5 8 0 5 2 4 \times 1 0 ^ { - 5 } \times 2 \pi T + 0 . 7 4 ) } } \\ { { \qquad + 1 . 1 2 0 8 9 \times 1 0 ^ { - 3 } \exp i ( 2 . 9 3 6 3 0 6 8 \times 1 0 ^ { - 6 } \times 2 \pi T + 0 . 4 3 ) } } \\ { { \qquad + 7 . 9 3 4 3 \times 1 0 ^ { - 4 } \exp i ( - 6 . 9 0 0 8 \times 1 0 ^ { - 3 } \times 2 \pi T + 1 . 8 2 ) } } \\ { { \qquad \zeta = 6 . 8 5 7 2 \times 1 0 ^ { - 4 } \exp i ( - 1 . 4 0 1 3 7 3 \times 1 0 ^ { - 5 } \times 2 \pi T + 1 . 7 5 ) } } \\ { { \qquad + 3 . 7 8 3 2 \times 1 0 ^ { - 4 } \exp i ( - 1 . 9 7 1 3 9 1 8 \times 1 0 ^ { - 6 } \times 2 \pi T + 4 . 2 1 ) . } } \end{array}
$$

Oberon

$$
\begin{array} { r l } & { M _ { \mathrm { U } } = 3 . 4 5 \times 1 0 ^ { - 5 } } \\ & { n = 0 . 4 6 6 5 8 0 5 4 \mathrm { r a d i a n s } / \mathrm { d a y } } \\ & { L = - 0 . 9 1 5 5 9 1 8 0 + 0 . 4 6 6 6 9 2 \ 1 2 T \ \mathrm { r a d i a n s } } \\ & { z = - 7 . 5 8 6 8 \times 1 0 ^ { - 4 } \exp { i ( 1 . 5 8 0 5 2 4 \times 1 0 ^ { - 5 } \times 2 \pi T + 0 . 7 4 ) } } \\ & { \qquad + 1 . 3 9 7 3 4 \times 1 0 ^ { - 3 } \exp { i ( 2 . 9 3 6 3 0 6 8 \times 1 0 ^ { - 6 } \times 2 \pi T + 0 . 4 3 ) } } \\ & { \qquad - 9 . 8 7 2 6 \times 1 0 ^ { - 4 } \exp { i ( - 6 . 9 0 0 8 \times 1 0 ^ { - 3 } \times 2 \pi T + 1 . 8 2 ) } } \\ & { \zeta = - 5 . 9 6 3 3 \times 1 0 ^ { - 4 } \exp { i ( - 1 . 4 0 1 3 7 3 \times 1 0 ^ { - 5 } \times 2 \pi T + 1 . 7 5 ) } } \\ & { \qquad + 4 . 5 1 6 9 \times 1 0 ^ { - 4 } \exp { i ( - 1 . 9 7 1 3 9 1 8 \times 1 0 ^ { - 6 } \times 2 \pi T + 4 . 2 1 ) } } \end{array}
$$

with $T = { \mathrm { J D } } - 2 4 4 4 2 3 9 . 5$ and $i = \sqrt { - 1 }$

Here $m / M _ { \mathrm { U } }$ is the ratio of the mass of the satellite to the mass of Uranus; $n$ is the daily mean motion; $L$ is the mean longitude measured from the ascending node of Uranus'equator on the Earth's equator to the ascending node of the satellite orbit on Uranus’equator along the orbit to the mean position of the satellite. $z$ and $\boldsymbol { \zeta }$ are converted to classical elements with the following formulae

$$
\begin{array} { l } { z = e \exp ( i P ) } \\ { \zeta = \sin \displaystyle \frac { \gamma } { 2 } \exp ( i \theta ) } \end{array}
$$

where $e$ is the eccentricity; $P$ is the longitude of the pericenter reckoned from the ascending node of Uranus’equator on the Earth's equator of 195o.0,along Uranus’equator to the ascending node of the orbit on Uranus'equator,and then along the orbit to the pericenter; $\gamma$ is the inclination of the orbital plane to Uranus'equator; $\theta$ is the longitude of the ascending node of the orbit on Uranus'equator measured from the ascending node of Uranus’equator on the Earth's equator.

Referred to the Earth's equator the motions of the satellites are direct.However,referred to the ecliptic they are retrograde,havingan angle of inclination of roughly $9 8 ^ { \circ } { }$ .Theorbital plane is inclined at suchalarge angle to the Earth'sequator that the semimajor axisof the apparent orbit usually lies nearly north and south. Consequently,the greatest elongations are designated as northern and southern elongations instead of eastern or western. Only when the Earth is near the plane through the celestial pole perpendicular to the orbital plane,as during

1986-1987,is the minor axis of the apparent orbit directed approximately north and south. Even then,the north pole of the orbital plane may lie to the south of the geocentric position of Uranus.The north pole of the orbital plane is that from which the satellites’motion appears to be counterclockwise.This pole corresponds to the physical ephemeris south pole of Uranus, which is defined as lying south of the invariable plane of the solar system.

During the course of one revolution of Uranus,the Earth passes twice through the plane perpendicularto the orbital plane when the apparent orbits of the satellites are almost circular; andlikewise,it passes twice through the orbital plane when the apparent orbits become straight lines.The Earth passed through the orbital plane from south to north in1966,and the sequence of geometric relations during the interval from then until 2o5O exemplifies the cycle during the 84-year period of Uranus.

1966-2008: Earth north of orbital plane; $B$ positive. Superior conjunction at position angle $P$   
1966-1986: Northern elongation at $P + 9 0 ^ { \circ }$ ,when $u - U = 9 0 ^ { \circ }$ .   
1986: Earth passed through plane perpendicular to orbital plane,at $U = 2 7 0 ^ { \circ }$ .   
1986-2008: Northern elongationat $P - 9 0 ^ { \circ }$ ,when $u - U = 2 7 0 ^ { \circ }$   
2008: Earth passed through orbital plane,north to south; $B = 0 ^ { \circ }$ .   
2008-2050: Earth south of orbital plane; $B$ negative. Superior conjunction at position angle $P + 1 8 0 ^ { \circ }$ .   
2008-2030: Northern elongation at $P - 9 0 ^ { \circ }$ ,when $u - U = 2 7 0 ^ { \circ }$ .   
2030: Earth passes through plane perpendicular to orbital plane,at $U = 9 0 ^ { \circ }$ .   
2030-2050: Northern elongation at $P + 9 0 ^ { \circ }$ ,when $u - U = 9 0 ^ { \circ }$ .

At the passage of the Earth through the plane perpendicular to the orbital plane,the position angle of the northern elongation changes by $1 8 0 ^ { \circ }$ ,because the more northerly and more southerly extremities of the major axisare interchanged.The angle $P$ is the position angle of the pole of the orbital plane that lies north of the celestial equator;but either the eastern or western extremity of the minor axis may be directed toward this pole,according to circumstances.Northern elongation may be to either the east or west of north.The elongations cannot be unambiguously designated as eastern and western.

To calculate the values of $J$ , $u$ ,and $N$ ,consider spherical triangle $A B D$ in Fig. 9.16. Spherical trigonometry givesus:

$$
\begin{array} { l } { \sin J \sin ( N - N _ { \mathrm { e } } ) = \sin \gamma \sin \theta } \\ { \sin J \cos ( N - N _ { \mathrm { e } } ) = \cos \gamma \sin J _ { \mathrm { e } } + \sin \gamma \cos J _ { \mathrm { e } } \cos \theta } \end{array}
$$

which can be solved for $J$ and $N$ .Thevalues of $N _ { \mathrm { e } }$ and $J _ { \mathrm { e } }$ ,thelongitude ofthe ascending node ofUranus’equator and its inclination to the Earth'sequator,are found from the coordinates of Uranus'south pole: $\alpha _ { 0 } = 7 7 . 4 3$ and $\delta _ { 0 } = + 1 5 \%$ (Davies et al. 1989):

$$
\begin{array} { r } { N _ { \mathrm { e } } = \alpha _ { 0 } + 9 0 ^ { \circ } } \\ { J _ { \mathrm { e } } = 9 0 ^ { \circ } - \delta _ { 0 } . } \end{array}
$$

![](images/efbf779351ae575abf3a97fc7e3c990ab9105f48b292de09bceb0db2f874acd4.jpg)  
Figure9.16 Reference system for the Uranian satellites. $N = \Upsilon D$ , $P = A B + B C$ ,and $L = A B + B C +$ mean anomaly.

Thearc length DBis found from

$$
\sin D B \sin \gamma = \sin ( N - N _ { \mathrm { e } } ) \sin J _ { \mathrm { e } } .
$$

Then

$$
u = L - \theta + D B + ( f - M )
$$

where $( f - M )$ is the equation of center which can be found from Eq.9.1,and

$$
M = L - P .
$$

Orbital,physical,and photometricdataare presentedonpagesF2-F5ofTheAstronomical Almanacfor7of the1O smallsatellites discoveredby Voyager.Dataforall10 satellitesare presentedat The Astronomical Almanac Online.The orbitsof thesesatellitesall lie inside the orbitofMiranda.Cordeliaand Opheliaareshepherd satellites for the $\varepsilon$ -ring.It hasalso beenproposed that Cordeliais the outer shepherd for the $\delta$ -ring,and thatOpheliaisthe outer shepherd of the $\gamma$ -ring.SinceVoyager,3moresatelliteshave beendiscoveredwithin the orbit of Miranda.A total of9 irregular satellites with orbital periods in the range 500- 3000 days,most of them in retrograde orbits,have also been discovered recently. Orbital, physical,and photometric data forthese12 satellitesarepresentedat The Astronomical Almanac Online.

# 9.11 The Satellites of Neptune

Ephemerides are given for the greatest eastern elongations of Triton,calculated from the orbital elements determinedby Harris (1984).Differential right ascensionsand declinations are given for Nereid from orbital elements computed by Jacobson (1990).

# 9.11.1 Triton

The orbit ofTriton is retrograde.Theorbit,as faras it has been determined from observations, iscircular.The orbital plane is defined with respect toa fixed reference plane.This reference plane is defined such that the projections of spin angular momentum of Neptune and the orbital angular momentum of Triton on the plane are equal and opposite.The pole of this fixed plane with respect to the Earth'sequator and equinox of J2Ooo.O are

$$
\begin{array} { r l } & { \alpha _ { \mathrm { p } } = 2 9 8 { \cdot } 7 2 + 2 { \cdot } 5 8 \sin N - 0 { \cdot } 0 4 \sin 2 N } \\ & { \delta _ { \mathrm { p } } = 4 2 { \cdot } 6 3 - 1 { \cdot } 9 0 \cos N + 0 { \cdot } 0 1 \cos 2 N } \\ & { N = 3 5 9 { \cdot } 2 8 + 5 4 { \cdot } 3 0 8 T } \\ & { T = ( \mathrm { J D } - 2 4 5 1 5 4 5 . 0 ) / 3 6 5 2 5 . } \end{array}
$$

The orbital elements of Triton referred to the fixed plane (see Fig.9.17)are

$$
\begin{array} { r l } & { t _ { 0 } = \mathrm { J D } 2 4 3 3 2 8 2 . 5 } \\ & { \begin{array} { r l } & { a = 4 8 8 ^ { \prime } 4 9 } \\ & { e = 0 } \\ & { n = 6 1 ^ { \circ } 2 5 8 8 5 3 2 / \mathrm { d a y } } \\ & { L _ { 0 } = 2 0 0 ^ { \circ } 9 1 3 } \end{array} } \\ & { \begin{array} { r l } & { \gamma = 1 5 8 ^ { \circ } 9 9 6 = 2 1 ^ { \circ } 0 0 4 \mathrm { ~ r e t r o g r a d e } } \\ & { \theta = 1 5 1 ^ { \circ } 4 0 1 + 0 ^ { \circ } 5 7 8 0 6 ( \mathrm { J D } - t _ { 0 } ) / 3 6 5 . 2 5 } \end{array} } \end{array}
$$

where $a$ is the greatest elongation at unit distance; $e$ is the eccentricity; $n$ is the daily mean motion; $L _ { 0 }$ is the mean longitude reckoned from the ascending node through the invariable plane at epoch; $\gamma$ is the inclination of the orbital plane to the invariable plane;and $\theta$ isthe angle from the intersection of invariable plane with the Earth's equatorial plane of 1950.0 to the ascending node of the orbit through the invariable plane.

Because the retrograde direction of the motion is represented by an orbital inclination greater than $9 0 ^ { \circ }$ ,theascendingnode of the orbit is the pointatwhich the satellite crosses the equator from south to north.The pole of the orbit from which the motion appears counterclockwise is the south pole,at position angle $P$ .Elongation isat position angle $P - 9 0 ^ { \circ }$ ,when $u - U = 2 7 0 ^ { \circ }$ .

Twice during the course of one revolution of Neptune,about 165 years,the Earth passes through the orbital plane of Triton,when the apparent orbit becomes a straight line.The Earth crossed the orbital plane from north to south near the end of 1952;for an interval during 1950-1954,Triton transited the disk of Neptune and was occulted by the disk during each revolution.Before1953, $B$ wasnegative,and inferior conjunctionwas on the southern arc of the apparent orbit at position angle $P$ .Since the passage through the orbital plane, $B$ has been positive,and inferior conjunction is on the northern arc at $P + 1 8 0 ^ { \circ }$ .TheEarthwill pass through the orbital plane again in 2035.

![](images/6341e9b5295f870f4c1454aa672484708f12c7b8f8829a1ab8c214289f8069ae.jpg)  
Figure9.17 Reference system for Triton. $N = \Upsilon C$

When the numerical value of $B$ reaches a maximumas the Earth passes through the plane perpendicular to the orbital plane,as in 1987,the minor axis of theapparent orbit lies exactly north and south,the major axis lies east and west,andthe position angle of the more northerly elongation changes by $1 8 0 ^ { \circ }$ .Before 1987,the western elongation was the more northerly; since then,the eastern elongation has been the more northerly.

The computation of $J , u$ ,and $N$ is as follows.From the spherical triangle in Fig.9.17 we have

$$
\begin{array} { l } { \sin J \sin ( N - N _ { \mathrm { e } } ) = \sin \gamma \sin \theta } \\ { \sin J \cos ( N - N _ { \mathrm { e } } ) = \cos \gamma \sin J _ { \mathrm { e } } + \sin \gamma \cos J _ { \mathrm { e } } \cos \theta } \end{array}
$$

which can be solved for $J$ and $N$ . $N _ { \mathrm { e } }$ and $J _ { \mathrm { e } }$ ,the longitude of the node and the inclination of the invariable plane to the Earth's equator,are found from

$$
\begin{array} { r } { N _ { \mathrm { e } } = \alpha _ { \mathrm { p } } + 9 0 ^ { \circ } } \\ { J _ { \mathrm { e } } = 9 0 ^ { \circ } - \delta _ { \mathrm { p } } } \end{array}
$$

where $\alpha _ { \mathrm { { p } } }$ and $\delta _ { \mathrm { p } }$ are,respectively,the right ascension and declination of Neptune's pole.The arc length $C B$ can be computed from

$$
\sin C B \sin \gamma = \sin ( N - N _ { \mathrm { e } } ) \sin J _ { \mathrm { e } } .
$$

$u$ follows from

$$
u = L _ { 0 } + C B + n ( \mathrm { J D } - t _ { 0 } )
$$

where JD is the Juliandate of interest.

# 9.11.2 Nereid

The orbit of Nereid is unique among the satelites in the solar system,because of its extreme eccentricity and the great difference in its inclination from that of Triton.Jacobson (1990)

![](images/09d2a2f83787aa6a0795f5568aa81e450e57361761924360e8fd8a3319f8df22.jpg)  
Figure9.18 Reference system for Nereid. $N = \Upsilon D$ and $P = A B + B C$

improved onthe previous orbitaltheory of Mignard(1981)byaccounting for the perturbations to Nereid's orbit due to Triton.The orbital elementsof Nereid referred to the mean orbital plane of Neptune are (see Fig. 9.18):

$$
\begin{array} { r l } & { \Omega = 3 1 5 ^ { \mathrm { o } } 9 9 5 8 9 2 8 - 3 ^ { \mathrm { o } } 6 5 0 2 7 2 5 6 2 T } \\ & { \gamma = 6 ^ { \mathrm { o } } 7 4 8 2 3 1 8 5 0 } \\ & { e = 0 . 7 5 0 8 7 6 2 9 1 } \\ & { \theta = 2 5 1 ^ { \mathrm { 0 } } 7 2 4 2 2 4 0 + 0 ^ { \mathrm { o } } 8 6 9 6 0 4 8 0 8 3 T } \\ & { a = 0 . 0 3 6 8 4 0 \mathrm { a u } } \\ & { n = 0 ^ { \mathrm { o } } 9 9 9 6 2 2 7 2 4 4 / \mathrm { d a y } } \\ & { M = 2 5 1 ^ { \mathrm { 0 } } 1 4 9 8 4 6 8 8 + 0 ^ { \mathrm { o } } 9 9 9 6 4 6 5 3 2 9 t - \theta } \end{array}
$$

where $\theta$ is the longitude of the node, $n$ is the mean daily motion, $M$ is the mean anomaly of date, $T$ isreckoned in Julian centuries,and $t$ isthenumber of days elapsed from JD 2433680.5. The inclination, $\gamma$ ,isreferred to Neptune's orbital plane.The longitude of the node is measured inNeptune'sorbital plane from its intersection with the 195o.O celestial equator. The orbit of Neptune is taken to have inclination, $J _ { e } = 2 2 . 3 1 3$ ,and longitude of ascending node, $N _ { e } = 3 . 5 2 2$ with respect to the 1950.0 celestial equator.

The differential right ascension and declination $x$ and $y$ coordinates in the orbital plane are computed from the Eqs.9.19.These coordinates are transformed to the orbital plane using

$$
{ \left[ \begin{array} { l } { x _ { 1 } } \\ { y _ { 1 } } \\ { z _ { 1 } } \end{array} \right] } = \mathbf { R } _ { 3 } ( - \theta ) \mathbf { R } _ { 1 } ( - \gamma ) \mathbf { R } _ { 3 } ( - P ) { \left[ \begin{array} { l } { x } \\ { y } \\ { 0 } \end{array} \right] }
$$

where $P = \theta - \Omega$ .Thesecoordinates are thentransformed tothe Earth equator and equinox of 1950.0 using

$$
\left[ \begin{array} { l } { x _ { 2 } } \\ { y _ { 2 } } \\ { z _ { 2 } } \end{array} \right] = \mathbf { R } _ { 3 } ( - N _ { \mathrm { e } } ) \mathbf { R } _ { 1 } ( - J _ { \mathrm { e } } ) \left[ \begin{array} { l } { x _ { 1 } } \\ { y _ { 1 } } \\ { z _ { 1 } } \end{array} \right] .
$$

The coordinates $x _ { 2 }$ , $y _ { 2 } , z _ { 2 }$ are then used to compute $\Delta \alpha$ and $\Delta \delta$ from $\xi$ and $\eta$ using Eq. 9.24.

# 9.12 The Satellites of Pluto

Timesof greatest northernelongationare presentedin The Astronomical Almanac forCharon; neither Hydra nor Nixare presented,as they fall outside of theselectioncriterion of being magnitude 23.Oor brighter.The orbital elements from which the Charon data are calculated aretaken from Tholen (1985).The elements,referred to the Earth'sequatorand equinox of 1950.0,are

$$
\begin{array} { l } { a = 0 . 0 0 0 1 2 7 8 8 \mathrm { a u } } \\ { \begin{array} { l } { n = 5 6 { } ^ { \circ } . 3 6 2 5 / \mathrm { d a y } } \\ { J = 9 4 9 . 3 } \end{array} } \\ { \begin{array} { l } { N = 2 2 3 9 . 7 } \\ { l _ { 0 } = 7 8 . 6 } \end{array} } \\ { \begin{array} { l } { t _ { 0 } = 2 . 4 4 5 0 0 0 . 5 } \end{array} } \end{array}
$$

where $a$ is the semimajor axis; $n$ ,the mean daily motion; $J$ ,theinclination of the orbital plane to the Earth equator of 1950.0; $N$ ,the longitude of the ascending node reckoned from the vernal equinox; $l _ { 0 }$ ,the mean longitude at epoch reckoned from the ascending node along the orbit; and $t _ { 0 }$ ,the date of epoch.

The orbit of Charon is retrograde.The pole of the orbit from which the motion appears counterclockwise is the south pole,at position angle $P$ .Elongation is at position angle $P - 9 0 ^ { \circ }$ ,when $u - U = 2 7 0 ^ { \circ }$ .

Twice during the course of one revolution of Pluto,about 248 years,the Earth passes through the orbitalplane of Charon,when the apparent orbit becomes a straight line.The Earth crossed the orbital plane three times during 1987-1988,the end result being acrossing from north to south.In the interval 1985-1990,Charon transited the disk of Plutoand was occulted by the disk during each revolution.Before 1987, $B$ was negative,and inferior conjunction was on the southern arc of the apparent orbit at position angle $P$ .Since the passage through the orbital plane, $B$ has been positive,and inferior conjunction is on the northern arc at $P + 1 8 0 ^ { \circ }$

When the numerical value of $B$ reaches a maximum as the Earth passes through the plane perpendicularto the orbital plane,as in 2O5o,the minor axis of the apparent orbit Iies exactly north and south,the major axis lies east and west,and the position angle of the more northerly elongation changes by $1 8 0 ^ { \circ }$ .Before 2O5O,the western elongation is the more northerly;after 2050,the eastern elongation will be the more northerly.

Since the orbit is referred to the Earth equatorand equinox of 1950.0, $J$ and $N$ are already known. $u$ isfound simply from

$$
u = l _ { 0 } + n ( \mathrm { J D } - t _ { 0 } )
$$

where JD is the Julian date of interest.

# Acknowledgments

Acknowledgments are due to Andrew Sinclair because much of this chapteris taken verbatim from Chapter 6 of the previous edition (Rohde and Sinclair 1992).

# REFERENCES

1.The Astronomical Almanac Online: http://asa.usno.navy.mil or http://asa.hmnao.com.   
2.IAU/IAG Working Group on Cartographic Coordinates and Rotational Elements: http://astrogeology.usgs.gov/Page/groups/name/IAU-WGCCRE.   
Archinal,B.A.,M.F.A'Hearn,E.Bowel,A.Conrad,G.J.Consolmagno,G.E.Hunt,R.Courtin, T.Fukushima,D.Hesteroffer,J.L.Hilton,G.A.Krasinsky,G.Neumann,J.Oberst,P.K. Seidelmann,P.Stooke,D.J.Tholen,P.C.Thomas,andI.P.Williams (2011).Report of theIAU Working GrouponCartographic Coordinates and Rotational Elements:2Oo9.Celestial Mechanics andDynamical Astronomy 109(2),101-135.   
Arlot,J.E. (1982).New Constants for Sampson-Lieske Theoryof the Galilean Satelites of Jupiter. Astronomyand Astrophysics107,305-310.   
Arlot,J.E.,J.Chapront,C.Ruatti,andD.T.Vu (1986).Compact ephemerides of the main satellites ofJupiter,Saturnand Uranus.AstronomyandAstrophysicsSupp.Series65(2),383-403.   
Brouwer,M.andG.M.Clemence (1961).Methods ofCelestial Mechanics.London: Academic Press.   
Chapront,J.andD.T.Vu(1984).A new compact representation of ephemerides-Application to the motion of Pluto,the sun and the Galilean satelites of Jupiter.Astronomy and Astrophysics 141, 131-143.   
Comrie,L.J.(1934).Phenomena of Saturn's Satelites.Memoirsofthe British Astronomical Association 30,97-106.   
Davies,M.E.,V.K.Abalakin,M.Bursa,G.E.Hunt,J.H.Lieske,B.Morando,R.H.Rapp,P.K. Seidelmann,A.T.Sinclair,andY.S.Tjuflin(1989).Reportofthe IAU/IAG/Cospar Working Group onCartographic Coordinates andRotational Elements ofthePlanets and Satellites:1988.Celestial Mechanics46,187-204.   
Elliot,J.L.,R.G.French,J.A.Frogel,J.H.Elias,D.J.Mink,andW.Liller(1981).OrbitsofNine UranianRings.AstronomicalJournal 86,444-455.   
Esposito,L.W.,J.N.Cuzzi,J.H.Holberg,E.A.Marouf,G.L.Tyler,andC.C.Porco(1984).Saturn's Rings:Structure,Dynamics,and Particle Properties.In T. Gerhels and M.S.Matthews (Eds.), Saturn,pp.463-545.Tucson,AZ:University of Arizona Press.   
Garcia,H.A.(1972).The Mass and Figure of Saturn by Photographic Astrometry of Its Satellites. Astronomical Journal 77,684-691.   
Harper,D.,D.B.Taylor,A.T.Sinclair,and S.Kaixian(1988).The Theory of the Motion of Iapetus. Astronomy and Astrophysics191,381-384.   
Harris,A.W.(1984).Physical Properties of Neptuneand Triton Inferred from the Orbit of Triton. In J.T.Bergstralh (Ed.),Uranusand Neptune,NASA ConferencePublication 233o,Washington, DC,pp.357-373.NASA.   
Hohenkerk,C.Y.,B.Yallop,C.A.Smith,andA.T.Sinclair(1992).CelestialReferenceSystems.In P.K.Seidelmann (Ed.),ExplanatorySupplement toTheAstronomicalAlmanac,Chapter 3,pp. 184-185.Mill Valley,CA:University ScienceBooks.   
Jacobson,R.A.(1990).The orbits of the satellites of Neptune.Astronomy and Astrophysics 231, 241-250.   
Kozai,Y.(1957).On the Astronomical Constants of Saturnian Satellites System. Annals of the Tokyo Observatory,Series25,73-106.   
Laskar,J.andR.A.Jacobson (1987).An Analytical Ephemeris of the Uranian Satelites.Astronomy andAstrophysics188,212-224.   
Levin,A.E.(1934).Mutual Eclipsesand OccultationsofJupiter'sSatelites.MemoirsoftheBritish Astronomical Association30,149-183.   
Lieske,J.H.(1977).TheoryofMotionof Jupiter'sGalilean Satellites.AstronomyandAstrophysics56, 333-352.   
Lieske,J.H.(1987).Galilean Satelite Evolution:Observational Evidence for Secular Changes in MeanMotions.Astronomyand Astrophysics176,146-158.   
Mignard,F.(1981).TheMeanElementsofNereid.AstronomicalJournal86,1728-1729.   
Rohde,J.R.(1990).Unpublished.   
Rohde,J.R.andA.T.Sinclair(1992).Orbital EphemeridesofRingsand Satelites.InP.K.Seidelmann (Ed.),Explanatoryuppementthestroomicalmanac,Chapter6,pp2581.illValley CA:University Science Books.   
Sampson,R.A.(1921).Theoryof theFour Great SatelitesofJupiter.MemoirsoftheRoyal Astronomical Society63,1-270.   
Shampine,L.F.andM.K.Gordon (1975).Computer SolutionsofOrdinary Differential Equations. San Francisco: W. H.Freeman and Company.   
Sinclair,A.T.(1974).A Theoryof theMotionofIapetus.MonthlyNoticesof theRoyal Astronomical Society 169,591-605.   
Sinclair,A.T.(1977).TheOrbitsof Tethys,Dione,Rhea,Titan andIapetus.Monthly Noticesof the RoyalAstronomicalSociety180,447-459.   
Sinclair,A.T.(1989).TheOrbits of the SatellitesofMarsDetermined from Earth-based andSpacecraft Observations.Astronomyand Astrophysics220,321-328.   
Taylor,D.B.(1984).A Comparison of the Theory of the Motion of Hyperion with Observations Made During1967-1982.Astronomy andAstrophysics141,151-158.   
Taylor,D.B.(1995).Compactephemeridesfordiffrentialtangentplanecoordinatesofplanetary satelites. Technical Note 68,HMNautical Almanac Office,UKHO,Taunton,UK.   
Taylor,D.B.and K.X.Shen (1988).Analysis of Astrometric Observations from 1967to 1983 of the MajorSatellites of Saturn.AstronomyandAstrophysics200,269-278.   
Taylor,D.B.and A.T.Sinclair (2Oo3).Approximate ephemerides and phenomena of natural satelites. Technical Note73,HMNautical Almanac Offce,UKHO,Taunton,UK.   
Taylor,S.W.(1951).On the Shadow ofSaturn on ItsRings.AstronomicalJournal55,229-230.   
Tholen,D.J.(1985).TheOrbit ofPluto's Satellite.AstronomicalJournal90,2353-2359.   
vanWoerkom,A.J.J.(1950).TheMotionofJupiter'sFifth Satelite,1892-1949.InAstronomical Papersof the American Ephemeris andNautical Almanac,Volume XIII.Washington,DC:U.S. Government Printing Office.   
Zadunaisky,P.E.(1954).ADetermination of New Elements of theOrbitof Phoebe,Ninth Satelite of Satum.AstronomicalJournal 59,1-6.

# Physical Ephemerides of Solar System Bodies

JAMESL.HILTON

# 10.1 Introduction

The physical ephemerides of solar system bodies give information on the appearance of the apparent disks of those objects.Physical ephemerides are used for making and reducing observations of the surface markings of an object,determining the exact center of an object's disk from observations of the limbs of the object,and estimating the object’s apparent brightness.

In general,the physical ephemeridescanbe broken into two groups:

1.information depending on the rotational elements and cartographic coordinates,and 2.the phase and apparent brightness of the object, which depend on the position of the Earth and Sun relative to the object and the object’s physical appearance.

Unless otherwise stated,all coordinates given in thischapter refer to the Barycentric Celestial Reference System (BCRS).The quantity $T$ is the time in Julian centuries of 36525 days from J2000.0,and $t$ is the time in days (86400 SI seconds) from J2000.0.All values tabulatedin The Astronomical Almanacare geocentricand have been corrected for the effects of aberration.

# 10.2Rotational Elements and Cartographic Coordinates

The cartographic coordinates of an object consist of the orientation of the north pole for aplanet or planetary satelliteor thepositive pole fora dwarf planet or other small solar system object1,and the position of the prime meridian of the object with respectto an inertial reference frame.Theseelementsare givenbythe threequantities: $\alpha , \delta$ ,and $W$ asa function of time,showninFig.10.1.

The angles $\alpha$ and δare the right ascension and declination of date of the planet’s north pole or dwarf planet’s positive pole.The International Astronomical Union (IAU) definition of the north pole of a planet (Archinal et al.2O1la) is the rotation axis that lies on the north side of the invariable plane of the solar system.The positive pole is pole around which the object rotates in a counterclockwise direction.The angles $\alpha$ andδ may vary slowly with time dueto the precession of the object about its polar axis.In the absence of other information, the axis of rotation is assumed to be normal to the mean orbital plane.This assumption is currently made for most of the satellites.

![](images/66ba1af5c5d1aad9a67b1d0b07c1c5df960a3592d211f31550fc178bc597efc2.jpg)  
Figure 10.1 The position of the north pole and prime meridian of a solar system body in Earth equatorial coordinates

The angle $W$ is measured along the object's equator,ina counterclockwise direction when viewed from the north pole foraplanet or positive pole foradwarf planet2,from the ascending node of the object's equator on the BCRS $( \ S 6 . 2 )$ to the point where the prime meridian of the object crosses its equator.The right ascension of the node, $\boldsymbol { Q }$ ,isat $6 ^ { \mathrm { h } } + \alpha$ ,and the inclination of the object'sequator to the Earth's equator is $9 0 ^ { \circ } - \delta$ .The object and its prime meridian are generally assumed to rotate uniformly;hence $W$ varieslinearlywith time.Ifacartographic position forthe prime meridianisassigned toan object,thatis,ifasuitable observable surface feature defines the position of the prime meridian, the expression for $W$ is chosen so that the ephemeris position follows the motion of the cartographic position.There may be errors in therotational elements of the object that willcause the cartographic position to drift away from the ephemeris position by asmall amount $\Delta W$ .The angle $\Delta W$ is measured positively counterclockwise from the ephemeris position of $W$ asviewed from above the north pole.For aprime meridian that has acartographic definition,the ephemeris definitionof $W$ may change as more accurate information on the motion of the cartographic prime meridianis obtained.

The IAU definition for the north pole requires the rotationabout that pole to be classified as either direct or retrograde.Direct rotation is counterclockwise as viewed from above the body'snorth pole,while retrograde rotation isclockwise.Fora body with direct rotation, Wincreases with time.For most of the satellites it is assumed that the rotation period is identical to the mean orbital period.For dwarf planets,the rotation is always direct; however, the obliquity of the pole may be greater than $9 0 ^ { \circ }$

The definitions forthe solar prime meridianand pole in $\ S 1 0 . 5$ are derived from Carrington (1863).The definitions for the prime meridian and pole of each of the planets,satelites,and minor planets for which the IAU has accepted acartographic coordinate system are found in Archinal etal.(2O1la);Archinal etal. (2O11b).The values for poles and prime meridians of the planetsand the dwarf planets (1) Ceres and (13434O) Pluto used in The Astronomical Almanac are in Table 10.1.In general,the expressions giving $\alpha _ { J 2 0 0 0 }$ , $\delta _ { J 2 0 0 0 }$ ,and $W$ should be accurateto one tenthof a degree.Two decimalplaces,however,are given to assure consistency when changing coordinate systems.The added zero digits to the rate values of $W$ arefor computational consistency andare not an indication of greater accuracy.Threesignificant digits beyond the decimal point are given in the expressions forMars,reflecting the greater confidence in its accuracy.

# 10.2.1Planetocentricand Planetographic Coordinate Systems

Both planetocentric and planetographic systems of coordinates are used in the study of the planetsand satellites.Both systemsare based on the same fundamental axis of rotation,but differ,as described below,in theirdefinitions of latitude,longitude,and range.Planetocentric coordinatesareused forgeneral purposesand are based onaright-handed systemof axes with its origin at the center of mass of the object.Planetographic coordinates are used for cartographic purposes and depend on the adoption of a reference surface,usually a spheroid, which approximates an equipotential surface of the object.The latitude and ranges for both of these coordinate systems are shown in Fig.10.2.

Theplanetographic reference surfaces for most of the planets are spheroids for which the equatorial radius, $a$ ,is larger than the polar radius, $^ b$ (Fig.10.2). Since the equipotential surface is usually a spheroid,the shape of the spheroid is related to that of a sphere by its geometric flattening, $f$ ,

$$
f = { \frac { a - b } { a } } .
$$

For some of the planets and most of the satellites the reference surface is a sphere.For some satellites,such asPhobos,Deimos,and Hyperion,the reference surface should be triaxial. However,triaxial ellipsoidswould make many computations more complicated,especially those related to map projections. Therefore,spherical or spheroidal reference surfaces are usuallyused in mapping programs.The polar axis for each reference surface is assumed tobe the mean axis of rotationas defined by the adopted rotational elements.For most of the planets thepresent accuracy of measurement does not reveal a deviation between the axis of rotation and the axis of figure.The equatorial radii and flattenings of the planets andPluto are found on pageE6 (E88 prior to 2oo5) of The Astronomical Almanac and in Table1O.2.The radii(spherical,spheroidal,or triaxial asapplicable)of the natural satellites of the planets,with minimum apparent magnitudes less than or equal to 23.0,are found on pagesF3andF5of The Astronomical Almanac and in Table10.3.A more complete list of satellites,including those with minimum apparent magnitudes greater than 23.Oand ones with provisional IAU designations,are given in The Astronomical Almanac Online at http://asa .usno.navy.mil or http://asa.hmnao.com.The equatorial diameters and geometric albedos of the dwarf planets,Ceres,Pluto,(136108)Haumea,(136199)Eris,and(136472)Makemake are found on page G3.

<table><tr><td></td><td>Table1o.1 The positionsof the polesand primemeridians of the planets </td></tr><tr><td colspan="2">Planet Parameter and Value</td></tr><tr><td>Mercury α0=281:0097-0:0328T</td><td></td></tr><tr><td>8=61:4143-0:0049T</td><td></td></tr><tr><td></td><td>W=329:5469+6:1385205t+0:009 938 22 sin M-0:00104581 sin</td></tr><tr><td></td><td>-0:00010280 sinM3-0:000 02364 sinM4-0:00000532 sinM</td></tr><tr><td colspan="2">Venus α =272:76</td></tr><tr><td>8= 67:16</td><td></td></tr><tr><td>W=160:20-14813688t</td><td></td></tr><tr><td>Earth α0=000-0:641T</td><td></td></tr><tr><td>80=90:00-0.557T</td><td></td></tr><tr><td></td><td>W=190:147+360:985 6235t</td></tr><tr><td>Mars α0=317:68143-01061T</td><td></td></tr><tr><td>80=52:88650-0:0609T</td><td></td></tr><tr><td>W=176:630+350:891982 26t</td><td></td></tr><tr><td></td><td>Jupiterα0= 268:056 595-0:006 499T+0:000117sinJ1+0:000938 sinJ2 +0:001432 sinJ3+0:000030 sinJ4+0002150 sinJ5</td></tr><tr><td></td><td>δ0=64:495303+0:002413T+0:000 050c0sJ1+0:000404cosJ2 +0:000 617cosJ3-0000013c0sJ4+0000926 cosJ5</td></tr><tr><td>W=284:95+870:5360000t</td><td></td></tr><tr><td colspan="2">Saturn α0=40589-0036T</td></tr><tr><td></td><td></td></tr><tr><td></td><td>80=83.537-0:004T</td></tr><tr><td>W=38:90+810:7939024t</td><td></td></tr><tr><td>Uranus αo = 257:311</td><td></td></tr><tr><td>80=-15:175</td><td></td></tr><tr><td></td><td>W=203:81-501:1600928t</td></tr><tr><td>Neptuneα0=299:36+0:70 sin N</td><td></td></tr><tr><td>δ0=43:46-051cos N</td><td></td></tr><tr><td></td><td>W=25318+536:3128492t-0:48 sinN</td></tr><tr><td>Ceres α=291</td><td></td></tr><tr><td>80=59</td><td></td></tr><tr><td></td><td>W=170:90+952:1532t</td></tr><tr><td>Pluto αo=132:993</td><td></td></tr><tr><td>80=-6163</td><td></td></tr><tr><td></td><td>W=302:695+56:362 5225t</td></tr><tr><td>The values for Mn,Jn,and Nare:</td><td></td></tr><tr><td>M=174:791086+4:092 335t</td><td></td></tr><tr><td></td><td>M=349:582171+8184670t</td></tr><tr><td></td><td>M3=164:373257+12:277 005 t</td></tr><tr><td></td><td>M4=339:164343+16:369 340t</td></tr><tr><td></td><td>M5=153:955429+20:461675 t</td></tr><tr><td>J1=99:360714+4850:4046T</td><td></td></tr><tr><td></td><td>J2= 175:895 369+1191:9605T</td></tr><tr><td>J3= 300:323162+262:5475T</td><td></td></tr><tr><td>J4=114:012 305+6070:2476T</td><td></td></tr><tr><td>J5=49:511251+643000 T</td><td></td></tr><tr><td>N=357:85+52:316T</td><td></td></tr></table>

![](images/5176d23ca69c22a6f8eecbe2d579ddaa5748453f54998d3c0b42f76a714f05b8.jpg)  
Figure10.2 Planetocentric and planetographic coordinates systems

Table 10.2 The equatorial radii and flattenings of the planets and Pluto   

<table><tr><td>Planet</td><td>Equatorial Radius (km)</td><td>Flattenning</td></tr><tr><td>Mercury</td><td>2439.7</td><td>0.0</td></tr><tr><td>Venus</td><td>6051.8</td><td>0.0</td></tr><tr><td>Earth</td><td>6378.14</td><td>0.003353 64</td></tr><tr><td>Marsa</td><td>3396.2</td><td>0.006 772</td></tr><tr><td></td><td></td><td>0.005000</td></tr><tr><td>Jupiter</td><td>71492.</td><td>0.064874</td></tr><tr><td>Saturn</td><td>60268.</td><td>0.097 962</td></tr><tr><td>Uranus</td><td>25559.</td><td>0.022 927</td></tr><tr><td>Neptune</td><td>24764.</td><td>0.017 081</td></tr><tr><td>Pluto</td><td>1195.</td><td>0.</td></tr></table>

aTwo flattening values are given forMars.The first value is determined using the north polar radius and the second using the south polar radius (Smith et al.1999).

Different methods were used to derive the values for the equatorial radii and geometric flatteningof the different planetsand satellites.Thus,they do not always refer to common definitions.Some radii are derived from star or spacecraft occultation measurement,some limb fitting,and some control-network computations.The spheroid for the Earth,for example,