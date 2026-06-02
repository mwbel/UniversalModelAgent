where $r$ istheheliocentric distance expressedinunitsof the solar radiusand $\beta$ is the solar latitude.The values for the constants, $A$ , $^ { a }$ ,and $b$ areincluded in Table 8.5.When near conjunction the major uncertainties of ranging observations are due to uncertainty in $N _ { \mathrm { e } }$ ,a numberwhich is highly time-dependent.Since thedelayis frequency dependent,the total delaymay be calibrated using dual-frequency ranging；otherwise,the parameters in the preceding formula must represent some sort of mean values.

For some ranging,measurements were taken in two separate frequencies,so that one can remove the effect entirely since it is frequency-dependent and may therefore be solved-for.

# 8.7.7Time Delay for the Troposphere

The delay from the Earth's troposphere for radio frequencies is discussed by Chao (1970). For each leg, it is

$$
\Delta \tau _ { t r o p o } = 7 \mathrm { n s e c } / ( \cos z + 0 . 0 0 1 4 / ( 0 . 0 4 5 + \cot z ) )
$$

where $Z$ is the zenith distance at the antenna.

# 8.7.8 Modeling the Surface of Mercury

For radar observations,the point of reflection on the surface of Mercury was approximated bya triaxial ellipsoid.Following Anderson et al.(1996),a set of fully normalized Legendre functions to the second degree was adjusted to fit the surface:

$$
\begin{array} { l } { { R _ { 0 } = + c _ { 1 0 } \sqrt { 3 } \sin \phi + ( c _ { 1 1 } \cos \lambda + s _ { 1 1 } \sin \lambda ) \sqrt { 3 } \cos \phi + c _ { 2 0 } \displaystyle \frac { \sqrt { 5 } } { 2 } ( 3 \sin ^ { 2 } \phi - 1 ) } } \\ { { \mathrm { } + ( c _ { 2 1 } \cos \lambda + s _ { 2 1 } \sin \lambda ) \sqrt { 1 5 } \sin \phi \cos \phi + ( c _ { 2 2 } \cos 2 \lambda + s _ { 2 2 } \sin 2 \lambda ) \displaystyle \frac { \sqrt { 1 5 } } { 2 } \cos ^ { 2 } \phi } } \end{array}
$$

where $\lambda$ is the longitude and $\phi$ is the latitude of the echo point on the surface.The least-squares adjustment forDE405 yielded:

$$
\begin{array} { r l r l r l } & { R _ { 0 } \equiv 2 , 4 3 9 , 7 6 0 ~ \mathrm { m } } & & { c _ { 1 0 } = + 9 2 0 \pm 5 2 3 ~ \mathrm { m } } & & { c _ { 1 1 } = + 1 8 6 \pm 3 8 ~ \mathrm { m } } & & { s _ { 1 1 } = - 2 4 5 \pm 3 8 ~ \mathrm { m } } \\ & { c _ { 2 1 } = + 7 9 \pm 1 5 7 ~ \mathrm { m } } & & { s _ { 2 1 } = + 7 4 4 \pm 1 6 6 ~ } & & { c _ { 2 2 } = + 2 9 2 \pm 3 2 ~ \mathrm { m } } & & { s _ { 2 2 } = + 3 4 5 \pm 3 4 ~ \mathrm { m } } \end{array}
$$

Since the latitude, $\phi$ ,of the radar echopoint on Mercuryisalwayswithin12 degrees of the equator, $c _ { 2 0 }$ is highlycorrelated $( \gg 0 . 9 9 )$ with $R _ { 0 }$ and was therefore omitted from the solution.Forthe other parameters,they serve merely as a smoothing function for determining theMercury ephemeris.For more definitive values in regard to the shape of Mercury,see Anderson et al. (1996).

# 8.7.9 Modeling the Surface of Venus

The surface of Venus was modeled using a topographical map fit to measurements from the Pioneer Venus Orbiter spacecraft (Pettengill etal.198O).Themap isreferenced to a sphere whose radius was determined to be $6 0 5 2 . 2 6 \pm 0 . 0 3 \mathrm { k m }$ in the least-squares adjustment.With such modeling,the radar residuals of Venus are reduced from over $2 \mathrm { k m }$ to less than $1 \ \mathrm { k m }$

# 8.7.10 Modeling the Surface of Mars-Closure Points

The severe topography on the surface of Mars shows variations of many kilometers.These introduce scatter into the observations which is not entirely random,thus presenting the dangerofsystematic errors.

Therefore,the radar ranging to Mars was used only in the closure point mode.Closure points are pairs of days during which the observed points on the surface ofMars are nearly identical with respect to their longitudes and latitudes on Mars.Since the same topographical features are observed during each of the two days,the uncertainty introduced by the topography may be eliminated by subtracting the residuals of one day from the corresponding ones of the other day.The remaining difference is then due to only the ephemeris drift between the two days.The closure points for Mars have apriori uncertainties of about $1 0 0 \mathrm { m }$ orless when the points are within O.2 degrees of each other on the martian surface.

# 8.7.11 Viking Lander Computations

The range data from the Viking Landers on the surface of Mars were reduced using the formulae given above with the reflection point on the planet's surface being represented by thelocation of thelanderon Mars.Forthis,one needs the Martian coordinates ofthe landers as well as a set of angles used to expressthe orientation of Mars within the ephemeris reference frame.The position of the lander, expressed inthe frame of the ephemeris,is given by

$$
\mathbf { r } = \mathbf { r } _ { x } ( - \varepsilon ) \mathbf { r } _ { z } ( - \Omega ) \mathbf { r } _ { x } ( - I ) \mathbf { r } _ { z } ( - \Omega _ { q } ^ { \prime } ) \mathbf { r } _ { x } ( - I _ { q } ^ { \prime } ) \mathbf { r } _ { z } ( - V ^ { \prime } ) \mathbf { r } _ { 0 }
$$

where $\varepsilon$ is the obliquity of the ecliptic; $\Omega$ and $I$ are the node and inclination of the mean Martian orbit upon the (J20oo.O) ecliptic; $\Omega _ { q }$ and $I _ { q }$ are the mean node and inclination of the Martian equator upon the mean orbit; $V$ isthe longitude of the Martian prime meridian measured along the equator from the intersection of the orbit;and $\mathbf { r } _ { 0 }$ ,theMarsfixedcoordinates of the lander,and where

$$
\Omega _ { q } ^ { \prime } = \Omega _ { q } - \Delta \psi , \qquad I _ { q } ^ { \prime } = I _ { q } + \Delta \varepsilon \quad \mathrm { a n d } \quad V ^ { \prime } = V + \Delta \psi \cos I _ { q } ^ { \prime }
$$

where $\Delta \psi$ and $\Delta \varepsilon$ express the nutation of Mars,computedfrom the formulation ofLyttleton, Cain,and Liu (1979).The Mars-fixed coordinates of the lander are computed from the cylindrical coordinates,

$$
\mathbf { r } _ { 0 } ^ { T } = [ u \cos \lambda , u \sin \lambda , v ] ^ { T } .
$$

The values for the parameters used in the reductions are given in $\ S \ 8 . 8$ .The values for $\varepsilon$ ， $\Omega$ ,and $I$ were adopted: those for $\Omega _ { q }$ , $I _ { q }$ ,and $V$ ,as well as the coordinates of the landers, were estimated in the least-squares adjustments.For a more extensive treatment including parameter values,see Folkner et al.(1998).

# 8.8 Initial Conditions and Constants of DE405/LE405

The starting conditions for DE405/LE405 were the result of two successive least-squares adjustments.The first adjustment was a solution for all of the relevant parameters whose valueswere best determined from the ephemeris data.Then,some of the parameters were rounded off(at a negligible level) for the sake of appearance and ease of use.These rounded values were then forced as known constants into the second solution which produced aminor adjustment to the other parameters.

This chapter gives the numerical values of all of the parameters that were used in the final integration of DE405/LE405.The starting epoch was Julian Ephemeris Date2440400.5 (June28,1969)—chosenasbeing the last $" 0 4 0 0 "$ datebefore thestartof theLunarLaser Ranging observations.Table 8.2 gives the cartesian coordinates of the heliocentric planets, the solar system barycentric Sun and the geocentric Moon.The orientation parameters of the Moon are given in Table8.3,the dynamical constants (those in the equations of motion) are presented in Table8.4,anumberof parameters used inthe reduction ofthe observational data (but not in the equations of motion) are shown in Table 8.5,and Table 8.6 gives the radii and taxonomic classes of the 297 non-Big3asteroidsused inDE405.

Table8.2 Initial conditions at JED $\mathrm { ( T _ { e p h } ) }$ 2440400.5 (June 28,1969).J2000.0equatorial coordinates and velocities of the heliocentric planet-system barycenters,the solar system barycentric Sun,and the geocentric Moon [au,au/day].   

<table><tr><td>Mercury</td><td>0.3572602064472754D+00</td><td>-0.9154904243051842D-01</td><td>-0.8598103998694038D-01</td></tr><tr><td rowspan="2">Venus</td><td>0.3367845662193786D-02</td><td>0.2488934284224929D-01</td><td>0.1294407158679597D-01</td></tr><tr><td>0.6082494331856041D+00</td><td>-0.3491324431959006D+00</td><td>-0.1955443457854069D+00</td></tr><tr><td rowspan="2">EMBary</td><td>0.1095242010990884D-01</td><td>0.1561250673986247D-01</td><td>0.6328876451746666D-02</td></tr><tr><td>0.1160149091391665D+00</td><td>-0.9266055536403853D+00</td><td>-0.4018062776069881D+00</td></tr><tr><td rowspan="2">Mars</td><td>0.1681162005220229D-01</td><td>0.1743131687982032D-02</td><td>0.7559737671361461D-03</td></tr><tr><td>-0.1146885824390927D+00</td><td>-0.1328366530833488D+01</td><td>-0.6061551894193808D+00</td></tr><tr><td rowspan="2">Jupiter</td><td>0.1448200480794475D-01</td><td>0.2372854923607114D-03</td><td>-0.2837498361023970D-03</td></tr><tr><td>-0.5384209406992146D+01</td><td>-0.8312476561610838D+00</td><td>-0.2250947570335499D+00</td></tr><tr><td rowspan="2">Saturn</td><td>0.1092363291218498D-02</td><td>-0.6523294191192267D-02</td><td>-0.2823012267219439D-02</td></tr><tr><td>0.7889889933822818D+01</td><td>0.4595710726926013D+01</td><td>0.1558431516725090D+01</td></tr><tr><td rowspan="2">Uranus</td><td>-0.3217203491093664D-02</td><td>0.4330632233555692D-02</td><td>0.1926417463799453D-02</td></tr><tr><td>-0.1826990081497826D+02</td><td>-0.1162711580219047D+01</td><td>-0.2503695407425549D+00</td></tr><tr><td rowspan="2">Neptune</td><td>0.2215401656274106D-03</td><td>-0.3767653558246162D-02</td><td>-0.1653243804922394D-02</td></tr><tr><td>-0.1605954509192446D+02</td><td>-0.2394294829087950D+02</td><td>-0.9400422780354008D+01</td></tr><tr><td rowspan="2">Pluto</td><td>0.2643122791576562D-02</td><td>-0.1503492080758795D-02</td><td>-0.6812710048723478D-03</td></tr><tr><td>-0.3048782211215555D+02</td><td>-0.8732454301967293D+00</td><td>0.8911296984184755D+01</td></tr><tr><td rowspan="2">Moon</td><td>0.3225621959332332D-03</td><td>-0.3148747927551605D-02</td><td>-0.1080177931593696D-02</td></tr><tr><td>-0.8081773279114842D-03</td><td>-0.1994630001620399D-02</td><td>-0.1087262660838102D-02</td></tr><tr><td rowspan="2"></td><td>0.6010848166591298D-03</td><td>-0.1674454606151515D-03</td><td>-0.8556214497398617D-04</td></tr><tr><td>0.4502508156233894D-02</td><td>0.7670747009323788D-03</td><td>0.2660568051770271D-03</td></tr><tr><td rowspan="2">Sun</td><td>-0.3517482096451887D-06</td><td>0.5177625399584830D-05</td><td>0.2229101854391665D-05</td></tr><tr><td></td><td></td><td></td></tr></table>

[able8.3J2OoOangular coordinates of the lunar physicallibrations[rad,rad/day   

<table><tr><td>ΦM,0M，ψM</td><td>0.00512995970515812456</td><td>0.38239065587686011507</td><td>1.29414222411027863099</td></tr><tr><td>@xM，ωyM，ωzM</td><td>0.00004524704499022800</td><td>-0.00000223092763198743</td><td>0.22994485870136698411</td></tr></table>

「able 8.4 Dynamical constants used in the integration of DE405/LE405   

<table><tr><td colspan="3">Defining Constants,Scale Factor</td></tr><tr><td>k2</td><td>0.017202098952</td><td>Gauss’(gravitational) constant</td></tr><tr><td>c</td><td>299792.458[km/sec]</td><td>speed of light</td></tr><tr><td>au</td><td>149597870.691 [km/au]</td><td>scale factor</td></tr><tr><td colspan="3">Planetary Masses</td></tr><tr><td>GMs/GM1</td><td>6023600.</td><td>mass-1 for Mercury</td></tr><tr><td>GMs/GM2</td><td>408523.71</td><td>mass-1 for Venus</td></tr><tr><td>GMs/GMB</td><td>328900.5614</td><td>mass-1 for EM-Bary</td></tr><tr><td>GM5/GM4</td><td>3098708.</td><td>mass-1 for Mars</td></tr><tr><td>GM5/GM5</td><td>1047.3486</td><td>mass-1 for Jupiter</td></tr><tr><td>GMs/GM6</td><td>3497.898</td><td>mass-1 for Satum</td></tr><tr><td>GMs/GM7</td><td>22902.98</td><td>mass-l for Uranus</td></tr><tr><td>GM5/GMg</td><td>19412.24</td><td>mass-1 for Neptune</td></tr><tr><td>GM5/GM9</td><td>135200000.</td><td>mass-l for Pluto</td></tr><tr><td>GMe/GMm</td><td>81.30056</td><td>Earth-Moon mass ratio</td></tr><tr><td colspan="3">AsteroidMassesandDensities</td></tr><tr><td>mCeres</td><td>4.7 ×10-10 GMs</td><td>Mass of Ceres</td></tr><tr><td>m pallas</td><td>1.0 ×10-10 GMs</td><td>Mass of Pallas</td></tr><tr><td>mVesta</td><td>1.3×10-10 GMs</td><td>Mass of Vesta</td></tr><tr><td>pc</td><td>1.8</td><td>MeandensityofC-type asteroids</td></tr><tr><td>ps</td><td>2.4</td><td>Meandensity of S-type asteroids</td></tr><tr><td>PM</td><td>5.0</td><td>Meandensity ofM-typeasteroids</td></tr><tr><td colspan="3">Relativity,G,J(Sun)</td></tr><tr><td>β</td><td>1.0</td><td>PPN parameter</td></tr><tr><td>y</td><td>1.0</td><td>PPN parameter</td></tr><tr><td>G</td><td>0.0</td><td>rate of change of the gravitational constant</td></tr><tr><td>Js</td><td>2×10-7</td><td>dynamical form-factoroftheSun</td></tr><tr><td colspan="3">Earth Parameters</td></tr><tr><td>Re</td><td>6378.137[km]</td><td>radius of the Earth</td></tr><tr><td>J2e</td><td>0.001082626</td><td>Zonal harmonics of the Earth</td></tr><tr><td>J3e</td><td>-0.000002533</td><td></td></tr><tr><td>J4e</td><td>-0.000001616</td><td></td></tr><tr><td>k2e0</td><td>0.34</td><td>potential Love number for zonal Earth tides</td></tr><tr><td>k2e1</td><td>0.30</td><td>fordiurnal Earth tides</td></tr><tr><td>k2e2</td><td>0.30</td><td>for semidiurnal Earth tides</td></tr><tr><td>Te0</td><td>0.0</td><td>time-lagfor thezonal Earth tides</td></tr><tr><td>Te1</td><td>0.01290895939 [days]</td><td>for diurnal Earth tides</td></tr><tr><td>Te2</td><td>0.00694178558 [days]</td><td>for semidiurnal Earth tides</td></tr><tr><td>Φx</td><td>0.0</td><td>X-axisrotationat J2000.0</td></tr><tr><td>Φy</td><td>0.0</td><td>Y-axisrotationatJ2000.0</td></tr><tr><td>dΦx/dt</td><td>0.000244["/yr]</td><td>negative obliquity rate correction:-△</td></tr><tr><td>dΦy/dt</td><td>-0.001193["/yr]</td><td>precession correction:+△p sinε</td></tr><tr><td colspan="3">Moon Parameters</td></tr><tr><td>Rm</td><td>1738.0[km]</td><td>radiusoftheMoon</td></tr><tr><td>βL</td><td>0.0006316121</td><td>lunarmoment parameters</td></tr><tr><td>YL</td><td>0.0002278583</td><td></td></tr><tr><td>k2m</td><td>0.0299221167</td><td>potential love number of theMoon</td></tr><tr><td>Tm</td><td>0.1667165558[days]</td><td>time-lagfor the lunarsolid-body tide</td></tr><tr><td>J2ma a</td><td>0.000204312007</td><td>input zonal harmonics of the Moon</td></tr><tr><td>J3m</td><td>0.000008785470</td><td></td></tr><tr><td>J4m</td><td>-0.000000145383</td><td></td></tr><tr><td>C3,1m</td><td>0.000030803810</td><td>input tesseral harmonics of the Moon</td></tr><tr><td>C3,2m</td><td>0.000004879807</td><td></td></tr><tr><td>C3,3m</td><td>0.000001770176</td><td></td></tr><tr><td>S3,1m</td><td>0.000004259329</td><td></td></tr><tr><td>S3,2m</td><td>0.000001695516</td><td></td></tr><tr><td>S3,3m</td><td>-0.000000270970</td><td></td></tr><tr><td>C4,1m</td><td>-0.000007177801</td><td></td></tr><tr><td>C4,2m</td><td>-0.000001439518</td><td></td></tr><tr><td>C4,3m</td><td>-0.000000085479</td><td></td></tr><tr><td>C4,4m</td><td>-0.000000154904</td><td></td></tr><tr><td>S4,1m</td><td>0.000002947434</td><td></td></tr><tr><td>S4,2m</td><td>-0.000002884372</td><td></td></tr><tr><td>S4,3m</td><td>-0.000000788967</td><td></td></tr><tr><td>S4,4m</td><td>0.000000056404</td><td></td></tr></table>

ä Note,as described in $\ S \ 8 . 3$ ,the values used for $J _ { 2 m }$ ， $C _ { 2 , 2 m }$ , $C _ { 2 , m }$ , $S _ { 2 , 1 m }$ ,and $S _ { 2 , 2 m }$ arecomputed from the (time-varying) lunar moment-of-inertia tensor.The $J _ { 2 m }$ listed here is input; the rigid value,used in the force and torque equations,is derived from this input value and from the potential Love number, $k _ { 2 m }$ .The rigid value of $C _ { 2 , 2 m }$ is computed from $J _ { 2 m } ,$ $\beta _ { L }$ ,and $\gamma _ { L }$

[able8.5 Auxiliary constants used in the observational reductions for DE405/LE40.   

<table><tr><td colspan="2">MarsOrientation Parameters</td><td></td></tr><tr><td>£</td><td>23.4392811[]</td><td>Meanobliquityoftheecliptic</td></tr><tr><td>ε</td><td>0.0[%/day]</td><td></td></tr><tr><td>Ω</td><td>49.6167[]</td><td>Node of Mars’mean orbit upon ecliptic</td></tr><tr><td>Ω</td><td>0.0[%day]</td><td></td></tr><tr><td>1</td><td>1.85137[]</td><td>Inclination ofMars’mean orbit upon ecliptic</td></tr><tr><td>i</td><td>0.0[day]</td><td></td></tr><tr><td></td><td>35.4371[°]</td><td>NodeofMars’equatoruponMars’orbit</td></tr><tr><td>q</td><td>-5.76×10-6[°%day]</td><td></td></tr><tr><td>L</td><td>25.1886[°]</td><td>Inclination ofMars’equator upon Mars’orbit</td></tr><tr><td>iq</td><td>-0.1094×10-6[%day]</td><td></td></tr><tr><td>V</td><td>1.3361259[]</td><td>Longitude ofMars’primemeridian</td></tr><tr><td>V</td><td>350.89198512444[/day]</td><td></td></tr><tr><td colspan="3">Viking Spacecraft Coordinates</td></tr><tr><td>λ1</td><td>311.82160[]</td><td>longitudeofVikingLander#1</td></tr><tr><td>u1</td><td>3136.520 [km]</td><td>axial distance</td></tr><tr><td>U1</td><td>1284.469[km]</td><td>z-height</td></tr><tr><td>λ1</td><td>134.05322[]</td><td>longitudeofVikingLander#2</td></tr><tr><td>u1</td><td>2277.366[km]</td><td>axial distance</td></tr><tr><td>U1</td><td>2500.054[km]</td><td>z-height</td></tr><tr><td colspan="3">SolarCorona Parameters (see Eq.8.24)</td></tr><tr><td>A</td><td>1.06×108[cm-3]</td><td></td></tr><tr><td>a</td><td>4.89×10[cm-3]</td><td></td></tr><tr><td>b</td><td>3.91×105[cm-3]</td><td></td></tr></table>

Table8.6 The297 non-Big 3individual asteroids used in the integrationof DE405.The taxonomic class and the radius in kmare given.   

<table><tr><td>0010</td><td>Hygiea</td><td>C</td><td>214.5</td><td>0109</td><td>Felicitas</td><td>C</td><td>45.8</td><td>0238</td><td>Hypatia</td><td>C</td><td>78.0</td></tr><tr><td>0013</td><td>Egeria</td><td>C</td><td>107.5</td><td>0111</td><td>Ate</td><td>C</td><td>69.5</td><td>0240</td><td>Vanadis</td><td>C</td><td>54.0</td></tr><tr><td>0019</td><td>Fortuna</td><td>C</td><td>100.0</td><td>0112</td><td>Iphigenia</td><td>C</td><td>37.8</td><td>0241</td><td>Germania</td><td>C</td><td>84.5</td></tr><tr><td>0024</td><td>Themis</td><td>C</td><td>99.0</td><td>0114</td><td>Kassandra</td><td>C</td><td>51.5</td><td>0247</td><td>Eukrate</td><td>C</td><td>68.5</td></tr><tr><td>0031</td><td>Euphrosyne</td><td>C</td><td>124.0</td><td>0117</td><td>Lomia</td><td>C</td><td>77.0</td><td>0259</td><td>Aletheia</td><td>C</td><td>92.5</td></tr><tr><td>0034</td><td>Circe</td><td>C</td><td>59.0</td><td>0120</td><td>Lachesis</td><td>C</td><td>89.0</td><td>0266</td><td>Aline</td><td>C</td><td>56.5</td></tr><tr><td>0035</td><td>Leukothea</td><td>C</td><td>54.0</td><td>0121</td><td>Hermione</td><td>C</td><td>108.5</td><td>0268</td><td>Adorea</td><td>C</td><td>71.0</td></tr><tr><td>0036</td><td>Atalante</td><td>C</td><td>54.5</td><td>0127</td><td>Johanna</td><td>C</td><td>61.0</td><td>0275</td><td>Sapientia</td><td>C</td><td>57.5</td></tr><tr><td>0038</td><td>Leda</td><td>C</td><td>60.0</td><td>0128</td><td>Nemesis</td><td>C</td><td>97.0</td><td>0276</td><td>Adelheid</td><td>C</td><td>63.5</td></tr><tr><td>0041</td><td>Daphne</td><td>C</td><td>91.0</td><td>0130</td><td>Elektra</td><td>C</td><td>94.5</td><td>0283</td><td>Emma</td><td>C</td><td>75.0</td></tr><tr><td>0045</td><td>Eugenia</td><td>C</td><td>107.0</td><td>0134</td><td>Sophrosyne</td><td>C</td><td>53.5</td><td>0303</td><td>Josephina</td><td>C</td><td>51.5</td></tr><tr><td>0046</td><td>Hestia</td><td>C</td><td>65.5</td><td>0137</td><td>Meliboea</td><td>C</td><td>75.0</td><td>0304</td><td>Olga</td><td>C</td><td>34.2</td></tr><tr><td>0047</td><td>Aglaja</td><td>C</td><td>68.5</td><td>0139</td><td>Juewa</td><td>C</td><td>81.0</td><td>0308</td><td>Polyxo</td><td>C</td><td>74.0</td></tr><tr><td>0048</td><td>Doris</td><td>C</td><td>112.5</td><td>0140</td><td>Siwa</td><td>C</td><td>57.0</td><td>0313</td><td>Chaldaea</td><td>C</td><td>50.5</td></tr><tr><td>0049</td><td>Pales</td><td>C</td><td>77.0</td><td>0141</td><td>Lumen</td><td>C</td><td>67.5</td><td>0324</td><td>Bamberga</td><td>C</td><td>114.0</td></tr><tr><td>0050</td><td>Virginia</td><td>C</td><td>44.0</td><td>0143</td><td>Adria</td><td>C</td><td>46.4</td><td>0326</td><td>Tamara</td><td>C</td><td>50.0</td></tr><tr><td>0051</td><td>Nemausa</td><td>C</td><td>76.5</td><td>0144</td><td>Vibilia</td><td>C</td><td>73.0</td><td>0329</td><td>Svea</td><td>C</td><td>40.2</td></tr><tr><td>0052</td><td>Europa</td><td>C</td><td>156.0</td><td>0145</td><td>Adeona</td><td>C</td><td>77.5</td><td>0334</td><td>Chicago</td><td>C</td><td>85.0</td></tr><tr><td>0053</td><td>Kalypso</td><td>C</td><td>59.5</td><td>0146</td><td>Lucina</td><td>C</td><td>68.5</td><td>0335</td><td>Roberta</td><td>C</td><td>46.8</td></tr><tr><td>0054</td><td>Alexandra</td><td>C</td><td>85.5</td><td>0147</td><td>Protogeneia</td><td>C</td><td>68.5</td><td>0336</td><td>Lacadiera</td><td>C</td><td>36.0</td></tr><tr><td>0056</td><td>Melete</td><td>C</td><td>58.5</td><td>0150</td><td>Nuwa</td><td>C</td><td>78.5</td><td>0344</td><td>Desiderata</td><td>C</td><td>69.0</td></tr><tr><td>0058</td><td>Concordia</td><td>C</td><td>48.9</td><td>0154</td><td>Bertha</td><td>C</td><td>96.0</td><td>0345</td><td>Tercidina</td><td>C</td><td>50.0</td></tr><tr><td>0059</td><td>Elpis</td><td>C</td><td>86.5</td><td>0156</td><td>Xanthippe</td><td>C</td><td>63.0</td><td>0350</td><td>Ornamenta</td><td>C</td><td></td></tr><tr><td>0062</td><td>Erato</td><td>C</td><td>49.6</td><td>0159</td><td>Aemilia</td><td>C</td><td>65.5</td><td>0356</td><td>Liguria</td><td>C</td><td>61.5</td></tr><tr><td>0065</td><td>Cybele</td><td>C</td><td>120.0</td><td>0160</td><td>Una</td><td>C</td><td>42.5</td><td>0357</td><td>Ninina</td><td>C</td><td>67.5</td></tr><tr><td>0070</td><td>Panopaea</td><td>C</td><td>63.5</td><td>0162</td><td>Laurentia</td><td>C</td><td>52.5</td><td>0358</td><td>Apollonia</td><td>C</td><td>55.0 45.9</td></tr><tr><td>0072</td><td>Feronia</td><td>C</td><td>44.6</td><td>0163</td><td>Erigone</td><td>C</td><td>38.2</td><td>0360</td><td>Carlova</td><td>C</td><td></td></tr><tr><td>0074</td><td>Galatea</td><td>C</td><td>61.5</td><td>0164</td><td>Eva</td><td>C</td><td>55.0</td><td>0362</td><td>Havnia</td><td>C</td><td>60.5</td></tr><tr><td>0076</td><td>Freia</td><td>C</td><td>95.0</td><td>0165</td><td>Loreley</td><td>C</td><td>80.0</td><td>0363</td><td>Padua</td><td>C</td><td>49.0</td></tr><tr><td>0078</td><td>Diana</td><td>C</td><td>62.5</td><td>0168</td><td>Sibylla</td><td>C</td><td>77.0</td><td>0365</td><td>Corduba</td><td></td><td>48.5</td></tr><tr><td>0081</td><td>Terpsichore</td><td>C</td><td>62.0</td><td>0171</td><td></td><td>C</td><td>60.5</td><td>0366</td><td>Vincentina</td><td>C</td><td>55.0</td></tr><tr><td>0083</td><td>Beatrix</td><td>C</td><td>42.1</td><td></td><td>Ophelia Ino</td><td></td><td></td><td>0372</td><td>Palma</td><td>C</td><td>49.0</td></tr><tr><td>0084</td><td>Klio</td><td>C</td><td></td><td>0173 0175</td><td></td><td>C</td><td>79.5</td><td>0373</td><td>Melusina</td><td>C</td><td>97.5</td></tr><tr><td></td><td>Io</td><td>C</td><td>41.5 78.5</td><td>0176</td><td>Andromache</td><td>C C</td><td>53.5</td><td>0375</td><td>Ursula</td><td>C</td><td>49.8</td></tr><tr><td>0085</td><td>Semele</td><td>C</td><td>63.5</td><td>0185</td><td>Iduna</td><td>C</td><td>62.5 82.5</td><td>0377</td><td>Campania</td><td>C C</td><td>108.0 47.2</td></tr><tr><td>0086 0087</td><td>Sylvia</td><td>C</td><td>135.5</td><td>0187</td><td>Eunike Lamberta</td><td>C</td></tr><tr><td>0431</td><td>Nephele</td><td>C</td><td>48.9</td><td>0751</td><td>Faina</td><td>C</td><td>57.5</td><td>0071</td><td>Niobe</td><td>S</td><td>43.6</td></tr><tr><td>0442</td><td>Eichsfeldia</td><td>C</td><td>33.8</td><td>0762</td><td>Pulcova</td><td>C</td><td>71.0</td><td>0080</td><td>Sappho</td><td></td><td>40.9</td></tr><tr><td>0444</td><td>Gyptis</td><td>C</td><td>85.0</td><td>0769</td><td>Tatjana</td><td>C</td><td>51.0</td><td>0089</td><td>Julia</td><td></td><td>79.5</td></tr><tr><td>0449</td><td>Hamburga</td><td>C</td><td>44.3</td><td>0772</td><td>Tanete</td><td>C</td><td>61.5</td><td>0103</td><td>Hera</td><td></td><td>47.6</td></tr><tr><td>0451</td><td>Patientia</td><td>C</td><td>115.0</td><td>0773</td><td>Irmintraud</td><td>C</td><td>49.5</td><td>0115</td><td>Thyra</td><td></td><td>41.8</td></tr><tr><td>0454</td><td>Mathesis</td><td>C</td><td>42.2</td><td>0776</td><td>Berbericia</td><td>C</td><td>88.5</td><td>0124</td><td>Alkeste</td><td>S S</td><td>39.8</td></tr><tr><td>0455</td><td>Bruchsalia</td><td>C</td><td>43.8</td><td>0780</td><td>Armenia</td><td>C</td><td>48.5</td><td>0148</td><td>Gallia</td><td>S</td><td>52.0</td></tr><tr><td>0466</td><td>Tisiphone</td><td>C</td><td>60.5</td><td>0788</td><td>Hohensteina</td><td>C</td><td>54.5</td><td>0181</td><td>Eucharis</td><td>S</td><td>53.5</td></tr><tr><td>0469</td><td>Argentina</td><td>C</td><td>64.5</td><td>0790</td><td>Pretoria</td><td>C</td><td>88.0</td><td>0192</td><td>Nausikaa</td><td>S</td><td>53.5</td></tr><tr><td>0476</td><td>Hedwig</td><td>C</td><td>60.5</td><td>0791</td><td>Ani</td><td>C</td><td>53.5</td><td>0196</td><td>Philomela</td><td>S</td><td>73.0</td></tr><tr><td>0481</td><td>Emita</td><td>C</td><td>58.0</td><td>0804</td><td>Hispania</td><td>C</td><td>80.5</td><td>0221</td><td>Eos</td><td>S</td><td>55.0</td></tr><tr><td>0488</td><td>Kreusa</td><td>C</td><td>79.0</td><td>0814</td><td>Tauris</td><td>C</td><td>58.0</td><td>0230</td><td>Athamantis</td><td>S</td><td>57.5</td></tr><tr><td>0489</td><td>Comacina</td><td>C</td><td>72.0</td><td>0895</td><td>Helio</td><td>C</td><td>73.5</td><td>0236</td><td>Honoria</td><td>S</td><td>45.2</td></tr><tr><td>0490</td><td>Veritas</td><td>C</td><td>60.5</td><td>0909</td><td>Ulla</td><td>C</td><td>60.0</td><td>0287</td><td>Nephthys</td><td>S</td><td>35.0</td></tr><tr><td>0491</td><td>Carina</td><td>C</td><td>50.5</td><td>0914</td><td>Palisana</td><td>C</td><td>39.5</td><td>0328</td><td>Gudrun</td><td>S</td><td>23.5</td></tr><tr><td>0498</td><td>Tokio</td><td>C</td><td>42.4</td><td>1015</td><td>Christa</td><td>C</td><td>50.5</td><td>0346</td><td>Hermentaria</td><td>S</td><td>55.0</td></tr><tr><td>0505</td><td>Cava</td><td>C</td><td>57.5</td><td>1021</td><td>Flammario</td><td>C</td><td>51.5</td><td>0349</td><td>Dembowska</td><td>S</td><td>71.5</td></tr><tr><td>0506</td><td>Marion</td><td>C</td><td>54.5</td><td>1093</td><td>Freda</td><td>C</td><td>60.0</td><td>0354</td><td>Eleonora</td><td>S</td><td>81.0</td></tr><tr><td>0508</td><td>Princetonia</td><td>C</td><td>73.5</td><td>1467</td><td>Mashona</td><td>C</td><td>56.0</td><td>0385</td><td>IImatar</td><td>S</td><td>47.0</td></tr><tr><td>0511</td><td>Davida</td><td>C</td><td>168.5</td><td>0003</td><td>Juno</td><td>S</td><td>133.5</td><td>0387</td><td>Aquitania</td><td>S</td><td>53.0</td></tr><tr><td>0514</td><td>Armida</td><td>C</td><td>55.0</td><td>0005</td><td>Astraea</td><td>S</td><td>62.5</td><td>0389</td><td>Industria</td><td>S</td><td>40.8</td></tr><tr><td>0521</td><td>Brixia</td><td>C</td><td>60.5</td><td>0006</td><td>Hebe</td><td>S</td><td>96.0</td><td>0416</td><td>Vaticana</td><td>S</td><td>44.8</td></tr><tr><td>0535</td><td>Montague</td><td>C</td><td>38.5</td><td>0007</td><td>Iris</td><td>S</td><td>101.5</td><td>0433</td><td>Eros</td><td>S</td><td>10.0</td></tr><tr><td>0536</td><td>Merapi</td><td>C</td><td>79.0</td><td>0008</td><td>Flora</td><td>S</td><td>70.5</td><td>0471</td><td>Papagena</td><td>S</td><td>67.5</td></tr><tr><td>0545</td><td>Messalina</td><td>C</td><td>57.5</td><td>0009</td><td>Metis</td><td>S</td><td>85.0</td><td>0532</td><td>Herculina</td><td>S</td><td>112.5</td></tr><tr><td>0554</td><td>Peraga</td><td>C</td><td>49.2</td><td>0011</td><td>Parthenope</td><td>S</td><td>81.0</td><td>0674</td><td>Rachele</td><td>S</td><td>50.5</td></tr><tr><td>0566</td><td>Stereoskopia</td><td>C</td><td>87.5</td><td>0012</td><td>Victoria</td><td>S</td><td>58.5</td><td>0980</td><td>Anacostia</td><td>S</td><td>44.5</td></tr><tr><td>0568</td><td>Cheruskia</td><td>C</td><td>44.9</td><td>0014</td><td>Irene</td><td>S</td><td>83.5</td><td>1036</td><td>Ganymed</td><td>S</td><td>20.5</td></tr><tr><td>0595</td><td>Polyxena</td><td>C</td><td>57.0</td><td>0015</td><td>Eunomia</td><td>S</td><td>136.0</td><td>0016</td><td>Psyche</td><td>M</td><td>132.0</td></tr><tr><td>0596</td><td>Scheila</td><td>C</td><td>58.5</td><td>0017</td><td>Thetis</td><td>S</td><td>46.6</td><td>0021</td><td>Lutetia</td><td>M</td><td>49.8</td></tr><tr><td>0602</td><td>Marianna</td><td>C</td><td>65.0</td><td>0018</td><td>Melpomene</td><td>S</td><td>74.0</td><td>0022</td><td>Kalliope</td><td>M</td><td>93.5</td></tr><tr><td>0618</td><td>Elfriede</td><td>C</td><td>62.0</td><td>0020</td><td>Massalia</td><td>S</td><td>75.5</td><td>0069</td><td>Hesperia</td><td>M</td><td>71.5</td></tr><tr><td>0626</td><td>Notburga</td><td>C</td><td>52.0</td><td>0023</td><td>Thalia</td><td>S</td><td>55.5</td><td>0075</td><td>Eurydike</td><td>M</td><td>29.1</td></tr><tr><td>0635</td><td>Vundtia</td><td>C</td><td>50.0</td><td>0025</td><td>Phocaea</td><td>s</td><td>39.1</td><td>0077</td><td>Frigga</td><td>M</td><td>35.5</td></tr><tr><td>0654</td><td>Zelinda</td><td>C</td><td>66.0</td><td>0026</td><td>Proserpina</td><td>S</td><td>49.4</td><td>0092</td><td>Undina</td><td>M</td><td>66.0</td></tr><tr><td>0663</td><td>Gerlinde</td><td>C</td><td>52.0</td><td>0027</td><td>Euterpe</td><td colspan="6">S</td></tr></table>

# 8.8.1 Asteroids

The initial conditions forall 3Oo asteroids came froma file maintained by the Solar System Dynamics Group at JPL.The radii from the same file were used to compute the masses of each of the 297 non-Big3 individual asteroids fromtheformula, $G M = 6 . 2 7 \times 1 0 ^ { - 2 2 } { \mathrm { R } } ^ { 3 } \rho _ { k }$ ， where R is the radius of the asteroid in kilometers and where $\rho _ { k }$ is the density of the $\mathrm { k } ^ { t h }$ taxonomic class of asteroids (S,C,orM),given in Table 8.6.

# 8.9Positional Errors of the Planetary and Lunar Ephemerides

Estimates of ephemeris errors are based upon a numberof factors,including the accuracies of the observational data,the stability to various parameter and data combinations tested in the least-squaresadjustments,the observed abilities to predict positions into the future,knowledge of the uncertainties associated with various relevant factors,etc.However,one may get amore definitive assessment comparing two ephemerides,assuming that the differences are due mainly to the older ephemeris,the newer one having benefitted from refined modeling and enhanced data sets.

This section first discusses the accuracies of the ephemerides,showing how the different data types contribute to the various ephemeris parameters;it then presents comparisons of DE200 and ofDE405with a recent ephemeris,DE409.

# 8.9.1 Inner Four Planets: Ephemerides from Ranging and VLBl

The ephemerides of the fourinnermost planets along with the Moon and the Sun are all wellknown with respect to each other(intra-planet distances and angles)because of the accurate ranging observations towhich the ephemeridesare adjusted.Furthermore,the mean motion ofthis whole inner-body system isalso well-determined by fiting to the ranging observations.For explanations of this latter fact,seeWilliams and Standish (1989) or Standish and Williams (1990).

The orientation of the inner planet system is provided by VLBI observations of the Magellan Spacecraftorbiting Venus and the Phobos Spacecrafton its approach to Mars.These observations link the spacecraft to the ICRF(International Celestial Reference System),and thus the planet to the ICRF,given that the planetocentric spacecraft orbit is sufficiently well-determined.Anadditional frame-tie (Folkner etal.1993）was determined using the well-establishedEarth-basedpositionsoftheVLBIantennae,linkedtotheLLR(lunar laser ranging) telescopes by means of ground surveys. The positions of these telescopes, in turn,are connected to the Moon’sorbit using theLLR data,and since the Moon’s orbit is sensitive to the positionof the strongly perturbing Sun,it is tied to the heliocentric Earth orbit.

Radar ranging observations have inherent accuracies of less than 1OO meters,though the unmodeled uncertainties introduced by the surface topographies area few hundred meters and more.Spacecraft orbits,on the other hand, have shown accuracies of 1O meters or less. The VLBI observations have uncertainties of a few milliarcseconds;with about 2O of them, the uncertainty of the orientation of the whole inner planet ephemeris system of DE405 is

$0 _ { \cdot } ^ { \prime \prime } 0 0 1 { - } 0 _ { \cdot } ^ { \prime \prime } 0 0 2$ which is the equivalent of a kilometer or soat the typical distances between the inner planets.

Thus,during the present decade or so,relative distances between two of the inner-solarsystem bodies are accurate to 1OO-2Oo meters; relative angles between the inner bodies (e.g., Earth-Sun-planet angle)are accurateto less than $0 ^ { \prime \prime } 0 0 1$ .The orientation is accurate to $0 . ^ { \prime \prime } 0 0 1 -$ $0 ^ { \prime \prime } 0 0 2$ Away from the present epoch of accurate ranging and VLBI,the accuracies deteriorate due to the uncertainties in the mean motions caused by the perturbative effects of the asteroids.

# 8.9.2Uncertainties from Asteroid Perturbations

The massesof the asteroidsare not well-known,and therefore it has not been possible to model their perturbations with fullaccuracy.Williams(1984) estimated that due to the asteroids,the mean motions of the inner planets have uncertainties on the order of $0 . ^ { \prime \prime } 0 2$ century—acouple of kilometers per decade.

# 8.9.3Outer Planets: Reliance on the Classical Optical Observations

In contrast to those of the inner planets,the ephemerides of the outer planets rely almost entirely upon optical observations in which systematic errors over the past have been at the level of $0 \% 1$ orso.As a result, the outer planet ephemerides are much less accurate than those of the planets observed with ranging.Modern CCD measurements now show single (presumably random) observation measurement errors of about $0 . 1$ so that present-day planeof-sky positions (directions) are determined to a few hundredths of an arcsecond.For times away from the present,the accuracy deteriorates significantly,especially with the outermost planets.

# 8.9.4 Planetary Positional Errors in the Almanacs,1984-2002

Acomparison between DE200,created before 1980,and DE409,created in 2003,shows differences which must,for the most part, be attributed to the errors in DE2OO;thus,these differences give good estimates of the errors in the positions of The Astronomical Almanac for the years,1984-20o2.Plots of the differencesare given in Figs.8.1 through 8.10.

# 8.9.5 Planetary Position Uncertainties in 2003

One can also compare DE405with DE409.Importantly,this more recent ephemeris includes both ranging and VLBI measurements of the MGS (1999-) and the Odyssey (2002-) spacecraft in orbit aroundMars(Konopliv 2002,2003;Border 2002,2003),and also the continuing CCD measurements of the outer planets and their satellites (Stone 1998; Stone and Harris 2OoO).As such,DE409 is believed to be more accurate thanDE4O5,and the differences certainly represent the sizes of the uncertainties in DE4O5,if not estimates of theactual errors themselves.The differences,DE4O5-DE409,are shown in Figs.8.11 through 8.20.

![](images/99d8ddbcad8fc67d09d13ba82aa04264482fdd07cfa253b62edc240f6ca6c745.jpg)  
Figures8.1-8.5 Differences in right ascension,declination and distance between DE2oo-DE409

![](images/fbee1ec6071e013809562939a2339ba9da3207174e39d7096e7d0eee8472fa4a.jpg)  
Figures 8.6-8.10 Differences in right ascension,declination and distance between DE20o-DE409

![](images/bf8a840bd2bb36ba00b3dc2e27a4747e056b20688eead38881ce35896593406c.jpg)  
Figures8.11-8.15 Differences in right ascension,declination and distance between DE405-DE409

![](images/b1368a9e9df1b49e702ccbeaeaf9533f9c473188c3291891931d87f7db16883d.jpg)  
Figures 8.16-8.20 Differences in right ascension,declination and distance between DE405-DE409

It may be immediately noticed thatthe laterdifferences,DE405-DE4O9,are significantly smaller than those of DE2oo-DE4O5.As the observational data accumulate,the convergence of the ephemerides becomes a good indicator of the inherent errors and uncertainties.

The comparisons of both DE200 and DE405 with DE409 are discussed in further detail in Standish (2004).

# 8.10Keplerian Elements for Approximate Positions of the Major Planets

Lower accuracy formulae for planetary positions have a number of important applications when one doesn't need the full accuracy of an integrated ephemeris.They are often used in observation scheduling,telescope pointing,and prediction of certain phenomena as well as in the planning and design of spacecraft missions.

Approximate positions of the nine major planets may be found by using Keplerian formulae with their associated elements and rates.Such elements are not intended to represent anysort of mean;theyare simply theresult of beingadjustedfora best fit.As such,it must be noted that the elements are not valid outside the given time-interval over which they were fit.

The elements are given in Table 8.7or in Tables 8.8 and 8.9,depending upon the timeinterval overwhich they were fitand within which they are to be used.

Formulae for using them are given in $\ S 8 . 1 0 . 1$

Table8.7Keplerian elements and their rates,with respect to the meanecliptic and equinox of J2000.0, valid for the time-interval A.D.180O-A.D.2050   

<table><tr><td></td><td>a [au,au/cy]</td><td>e [rad,rad/cy]</td><td>1 [deg,deg/cy]</td><td>L [deg,deg/cy]</td><td>T [deg,deg/cy]</td><td>Ω [deg,deg/cy]</td></tr><tr><td>Mercury</td><td>0.38709927</td><td>0.20563593</td><td>7.00497902</td><td>252.25032350</td><td>77.45779628</td><td>48.33076593</td></tr><tr><td></td><td>0.00000037</td><td>0.00001906</td><td>-0.00594749</td><td>149472.67411175</td><td>0.16047689</td><td>-0.12534081</td></tr><tr><td>Venus</td><td>0.72333566</td><td>0.00677672</td><td>3.39467605</td><td>181.97909950</td><td>131.60246718</td><td>76.67984255</td></tr><tr><td></td><td>0.00000390</td><td>0.00004107</td><td>-0.00078890</td><td>58517.81538729</td><td>0.00268329</td><td>-0.27769418</td></tr><tr><td>EM Bary</td><td>1.00000261</td><td>0.01671123</td><td>-0.00001531</td><td>100.46457166</td><td>102.93768193</td><td>0.0</td></tr><tr><td></td><td>0.00000562</td><td>-0.00004392</td><td>-0.01294668</td><td>35999.37244981</td><td>0.32327364</td><td>0.0</td></tr><tr><td>Mars</td><td>1.52371034</td><td>0.09339410</td><td>1.84969142</td><td>-4.55343205</td><td>-23.94362959</td><td>49.55953891</td></tr><tr><td></td><td>0.00001847</td><td>0.00007882</td><td>-0.00813131</td><td>19140.30268499</td><td>0.44441088</td><td>-0.29257343</td></tr><tr><td>Jupiter</td><td>5.20288700</td><td>0.04838624</td><td>1.30439695</td><td>34.39644051</td><td>14.72847983</td><td>100.47390909</td></tr><tr><td></td><td>-0.00011607</td><td>-0.00013253</td><td>-0.00183714</td><td>3034.74612775</td><td>0.21252668</td><td>0.20469106</td></tr><tr><td>Saturn</td><td>9.53667594</td><td>0.05386179</td><td>2.48599187</td><td>49.95424423</td><td>92.59887831</td><td>113.66242448</td></tr><tr><td></td><td>-0.00125060</td><td>-0.00050991</td><td>0.00193609</td><td>1222.49362201</td><td>-0.41897216</td><td>-0.28867794</td></tr><tr><td>Uranus</td><td>19.18916464</td><td>0.04725744</td><td>0.77263783</td><td>313.23810451</td><td>170.95427630</td><td>74.01692503</td></tr><tr><td></td><td>-0.00196176</td><td>-0.00004397</td><td>-0.00242939</td><td>428.48202785</td><td>0.40805281</td><td>0.04240589</td></tr><tr><td>Neptune</td><td>30.06992276</td><td>0.00859048</td><td>1.77004347</td><td>-55.12002969</td><td>44.96476227</td><td>131.78422574</td></tr><tr><td></td><td>0.00026291</td><td>0.00005105</td><td>0.00035372</td><td>218.45945325</td><td>-0.32241464</td><td>-0.00508664</td></tr><tr><td>Pluto</td><td>39.48211675</td><td>0.24882730</td><td>17.14001206</td><td>238.92903833</td><td>224.06891629</td><td>110.30393684</td></tr><tr><td></td><td>-0.00031596</td><td>0.00005170</td><td>0.00004818</td><td>145.20780515</td><td>-0.04062942</td><td>-0.01183482</td></tr></table>

Table 8.8 Keplerian elements and their rates,with respectto the mean ecliptic and equinox of J2000.0, valid for the time-interval 30OO B.C.-A.D.3Ooo.Further,the computation of $M$ forJupiter through Pluto must be augmented by the additional terms described in Eq.8.3O and given in Table 8.9.   

<table><tr><td></td><td>a [au,au/cy]</td><td>e [rad,rad/cy]</td><td>1 [deg,deg/cy]</td><td>L [deg,deg/cy]</td><td>T [deg,deg/cy]</td><td>[deg,deg/cy]</td></tr><tr><td>Mercury</td><td>0.38709843</td><td>0.20563661</td><td>7.00559432</td><td>252.25166724</td><td>77.45771895</td><td>48.33961819</td></tr><tr><td></td><td>0.00000000</td><td>0.00002123</td><td>-0.00590158</td><td>149472.67486623</td><td>0.15940013</td><td>-0.12214182</td></tr><tr><td>Venus</td><td>0.72332102</td><td>0.00676399</td><td>3.39777545</td><td>181.97970850</td><td>131.76755713</td><td>76.67261496</td></tr><tr><td></td><td>-0.00000026</td><td>-0.00005107</td><td>0.00043494</td><td>58517.81560260</td><td>0.05679648</td><td>-0.27274174</td></tr><tr><td>EMBary</td><td>1.00000018</td><td>0.01673163</td><td>-0.00054346</td><td>100.46691572</td><td>102.93005885</td><td>-5.11260389</td></tr><tr><td></td><td>-0.00000003</td><td>-0.00003661</td><td>-0.01337178</td><td>35999.37306329</td><td>0.31795260</td><td>-0.24123856</td></tr><tr><td>Mars</td><td>1.52371243</td><td>0.09336511</td><td>1.85181869</td><td>-4.56813164</td><td>-23.91744784</td><td>49.71320984</td></tr><tr><td></td><td>0.00000097</td><td>0.00009149</td><td>-0.00724757</td><td>19140.29934243</td><td>0.45223625</td><td>-0.26852431</td></tr><tr><td>Jupiter</td><td>5.20248019</td><td>0.04853590</td><td>1.29861416</td><td>34.33479152</td><td>14.27495244</td><td>100.29282654</td></tr><tr><td></td><td>-0.00002864</td><td>0.00018026</td><td>-0.00322699</td><td>3034.90371757</td><td>0.18199196</td><td>0.13024619</td></tr><tr><td>Saturn</td><td>9.54149883</td><td>0.05550825</td><td>2.49424102</td><td>50.07571329</td><td>92.86136063</td><td>113.63998702</td></tr><tr><td></td><td>-0.00003065</td><td>-0.00032044</td><td>0.00451969</td><td>1222.11494724</td><td>0.54179478</td><td></td></tr><tr><td>Uranus</td><td>19.18797948</td><td>0.04685740</td><td>0.77298127</td><td>314.20276625</td><td></td><td>-0.25015002 73.96250215</td></tr><tr><td></td><td>-0.00020455</td><td>-0.00001550</td><td>-0.00180155</td><td></td><td>172.43404441</td><td></td></tr><tr><td>Neptune</td><td></td><td>0.00895439</td><td>1.77005520</td><td>428.49512595</td><td>0.09266985</td><td>0.05739699</td></tr><tr><td></td><td>30.06952752 0.00006447</td><td>0.00000818</td><td>0.00022400</td><td>304.22289287 218.46515314</td><td>46.68158724</td><td>131.78635853</td></tr><tr><td>Pluto</td><td>39.48686035</td><td>0.24885238</td><td>17.14104260</td><td>238.96535011</td><td>0.01009938 224.09702598</td><td>-0.00606302 110.30167986</td></tr><tr><td></td><td>0.00449751</td><td>0.00006016</td><td>0.00000501</td><td>145.18042903</td><td>-0.00968827</td><td>-0.00809981</td></tr></table>

Table 8.9 Additional terms which must be added to the computation of $M$ for Jupiter through Pluto,300O B.C.toA.D.3000,as described inEq.8.30   

<table><tr><td></td><td>b</td><td>C</td><td>S</td><td>f</td></tr><tr><td>Jupiter</td><td>-0.00012452</td><td>0.06064060</td><td>-0.35635438</td><td>38.35125000</td></tr><tr><td>Saturn</td><td>0.00025899</td><td>-0.13434469</td><td>0.87320147</td><td>38.35125000</td></tr><tr><td>Uranus</td><td>0.00058331</td><td>-0.97731848</td><td>0.17689245</td><td>7.67025000</td></tr><tr><td>Neptune</td><td>-0.00041348</td><td>0.68346318</td><td>-0.10162547</td><td>7.67025000</td></tr><tr><td>Pluto</td><td>-0.01262724</td><td></td><td></td><td></td></tr></table>

# 8.10.1Formulae for Using the Keplerian Elements

Keplerian elements given in the Tables 8.7-8.9 are $a _ { o }$ a semimajor axis [au,au/century] $e _ { o } , \dot { e }$ eccentricity[radians,radians/century] $I _ { o } , \dot { I }$ inclination[degrees,degrees/century] $L _ { o } , \dot { L }$ mean longitude [degrees,degrees/century] $\varpi _ { o }$ ， $\dot { \varpi }$ longitude of perihelion [degrees,degrees/century] ${ \boldsymbol { \varpi } } = { \boldsymbol { \omega } } + { \boldsymbol { \Omega } } ,$ $\Omega _ { o }$ , $\dot { \Omega }$ longitudeoftheascendingnode[degrees,degrseur]

InordertoaineoiatesofoeofteaetativenJulianEpmisate $\mathrm { T _ { e p h } }$

1.Compute the value of each of that planet’s six elements: $a = a _ { o } + \dot { a } \mathrm { T }$ ,etc.,whereT, the number of centuries past J2000.0,is $\mathrm { T } { = } ( \mathrm { T } _ { \mathrm { e p h } } { - } 2 4 5 1 5 4 5 . 0 ) / 3 6 5 2 5$ .

2.Compute the argument of perihelion, $\omega$ ,and the mean anomaly, $M$

$$
\omega = \varpi - \Omega \quad ; \quad M = L - \varpi + b \Gamma ^ { 2 } + c \cos ( f \mathrm { T } ) + s \sin ( f \mathrm { T } )
$$

where the last three terms must be added to $M$ for Jupiter through Pluto when using the formulaefor 300O B.C.to A.D.3000.

3.Modulus the mean anomaly so that $- 1 8 0 ^ { \circ } \leq M \leq + 1 8 0 ^ { \circ }$ and then obtain the eccentric anomaly, $E$ ,from the solution of Kepler's equation (see $\ S 8 . 1 0 . 2 $ ：

$$
M = E - e ^ { * } \sin E
$$

where $e ^ { * } = 1 8 0 / \pi \times e = 5 7 . 2 9 5 7 8 e$

4.Compute the planet's heliocentric coordinates in its orbital plane, $\mathbf { r } ^ { \prime }$ ,with the $x ^ { \prime }$ -axis aligned from the focus to the perihelion:

$$
x ^ { \prime } = a ( \cos E - e ) \quad ; \quad y ^ { \prime } = a { \sqrt { 1 - e ^ { 2 } } } \ \sin E \quad ; \quad z ^ { \prime } = 0 .
$$

5.Compute the coordinates, $\mathbf { r } _ { e c l }$ ,in the J2Ooo.O ecliptic plane,with the x-axisaligned toward the equinox:

$$
\mathbf { r } _ { e c l } = \mathcal { M } \mathbf { r } ^ { \prime } \equiv \mathcal { R } _ { z } ( - \Omega ) \mathcal { R } _ { x } ( - I ) \mathcal { R } _ { z } ( - \omega ) \mathbf { r } ^ { \prime }
$$

so that

$$
\begin{array} { l l r c l } { x _ { e c l } = } & { \left( \cos \omega \cos \Omega - \sin \omega \sin \Omega \cos I \right) } & { x ^ { \prime } } & { + \left( - \sin \omega \cos \Omega - \cos \omega \sin \Omega \cos I \right) } & { y ^ { \prime } } \\ { y _ { e c l } = } & { \left( \cos \omega \sin \Omega + \sin \omega \cos \Omega \cos I \right) } & { x ^ { \prime } } & { + \left( - \sin \omega \sin \Omega + \cos \omega \cos \Omega \cos I \right) } & { y ^ { \prime } } \\ { z _ { e c l } = } & { \left( \sin \omega \sin I \right) } & { x ^ { \prime } } & { + \left( \cos \omega \sin I \right) } & { y ^ { \prime } } \end{array}
$$

6.If desiredineeuatoalodatesi“IF,ae", $\mathbf { r _ { e q } }$

$$
\begin{array} { r c l r c l } { { x _ { e q } } } & { { = } } & { { x _ { e c l } } } & { { } } & { { } } & { { } } \\ { { y _ { e q } } } & { { = } } & { { } } & { { + \ \cos \varepsilon } } & { { y _ { e c l } \ } } & { { - \ \sin \varepsilon \quad z _ { e c l } } } \\ { { z _ { e q } } } & { { = } } & { { } } & { { + \ \sin \varepsilon } } & { { y _ { e c l } } } & { { + \ \cos \varepsilon } } & { { z _ { e c l } } } \end{array}
$$

where the obliquity at J2000.0 is $\varepsilon = 2 3 . 4 3 9 2 8$

8.10.2Solution of Kepler's Equation, $M = E - e$ sin $E$

Given the mean anomaly, $M$ ,and the eccentricity, $e$ ,both in radians,start with

$$
E _ { 0 } = M + e \sin M
$$

and iterate the following three equations,with $n = 0 , 1 , 2 , . . . ,$ until $| \Delta E | \le t o l$ ：

$$
\Delta M = M - ( E _ { n } - e \sin E _ { n } ) ; \Delta E = \Delta M / ( 1 - e \cos E _ { n } ) ; E _ { n + 1 } = E _ { n } + \Delta E .
$$

For the approximate formulae in this present context, $t o l = 1 0 ^ { - 7 }$ radians is sufficient.

Table 8.10 Approximate errors in right ascension,α,declination,δ,and distance, $\rho$ ,fromthe Keplerian formulation of $\ S 8 . 1 0 . 3$   

<table><tr><td></td><td colspan="3">1800-2050</td><td colspan="3">3000 B.C.to A.D.3000</td></tr><tr><td></td><td>α[]</td><td>8[]</td><td>ρ[1000 km]</td><td>α[]</td><td>8[]</td><td>ρ [1000 km]</td></tr><tr><td>Mercury</td><td>15</td><td>1</td><td>1</td><td>20</td><td>15</td><td>1</td></tr><tr><td>Venus</td><td>20</td><td>1</td><td>4</td><td>40</td><td>30</td><td>8</td></tr><tr><td>EM Bary</td><td>20</td><td>8</td><td>6</td><td>40</td><td>15</td><td>15</td></tr><tr><td>Mars</td><td>40</td><td>2</td><td>25</td><td>100</td><td>40</td><td>30</td></tr><tr><td>Jupiter</td><td>400</td><td>10</td><td>600</td><td>600</td><td>100</td><td>1000</td></tr><tr><td>Saturn</td><td>600</td><td>25</td><td>1500</td><td>1000</td><td>100</td><td>4000</td></tr><tr><td>Uranus</td><td>50</td><td>2</td><td>1000</td><td>2000</td><td>30</td><td>8000</td></tr><tr><td>Neptune</td><td>10</td><td>1</td><td>200</td><td>400</td><td>15</td><td>4000</td></tr><tr><td>Pluto</td><td>5</td><td>2</td><td>300</td><td>400</td><td>100</td><td>2500</td></tr></table>

# 8.10.3 Approximate Accuracies of the Keplerian Formulae

Table 8.1O gives the accuracies that one can expect from the Keplerian formulation given in this section.

# 8.11The Availabilityof Ephemerides

Thefundamental ephemerides usedin The Astronomical Almanac since 1984,DE2Oo (1984- 2002)and DE405(2003-),are both available ona CD-ROM from the publisher,Willmann-Bell, see URL[3].The package allows a professional user to obtain the rectangular coordinates of the Sun,Moon,and nine major planets by means of a simple subroutine written in standard Fortran:

Willmann-Bell,Inc. POBox 35025 Richmond,VA 23235 804-320-7016 804-272-5920 (Fax)

Theephemeridesarealso availableas described in URL[4];see linkswithin that website.Also described there are references to other packagesand toolkits for the use of the ephemerides,as well as to the software being available in other programminglanguages.

TheREADME on URL[4] also containsa few modificationsto the software from the CD-ROM.However,it should be easier for the userto retrieve the software from the website, evenwhenusing the data files from the CD-ROM.

One mayalso use the interactivewebsite,Horizons,URL[5],which uses theJPL ephemerides,giving positional data (in2O11) for over 7O astronomical quantities for the8 planets and Pluto,more than 17O natural satellites and over 5oo ooO asteroids and comets;Horizons uses the full precision of the JPL ephemerides.

There are certainly other sources of ephemerides,though not alluseDE2OO or DE405, thefundamental ephemerides ofThe Astronomical Almanac.Further,there doexistanumber of packages which provide less accurate positions for the solar system bodies.

A description of a number of options may be found at URL[6].

# Acknowledgements

The research described in this chapter was carried out at the Jet Propulsion Laboratory, California Institute of Technology,under a contract with the National Aeronauticsand Space Administration. Government sponsorship is acknowledged.

# REFERENCES

1.Observational Data Used for Ephemeris Production: http://ssd.jpl.nasa.gov/plan-eph-data/index.html.   
2.IERS Conventions 2Oo3 (Technical Note 32): http://www.usno.navy.mil/USNO/earth-orientation/eo-info/general/conv2003/.   
3.Commercially Available JPLPlanetary and Lunar Ephemerides: http://www.willbell.com/software/jpl.htm.   
4.JPL Ephemerides Export Information: http://iau-comm4.jpl.nasa.gov/README.   
5.JPL Horizons System: http://ssd.jpl.nasa.gov/?horizons.   
6.Ephemerides via IAU Commission 4: http://iaucom4.org/ephemerides.html.   
Anderson,J.D.,R.F.Jurgens,E.L.Lau,andM.A.Slade(1996).Shape and Orientationof Mercury fromRadarRangingData.Icarusl24,690-697.   
Berge,G.L.,D.O.Muhleman,andR.P.Linfield (1988). Very Large Array Observationsof Uranus at 2.0 cm. Astronomical Journal 96,388-395.   
Border,J.S.(2002,2003).Private communications.   
Brown,E.W.(1919).Tablesof the Motionof theMoon.NewHaven,CT:Yale UniversityPress.   
Chao,C.C.(1970).A Preliminary Estimation of Tropospheric Influence on the Range and Range Rate DataDuring the Closest Approach of theMM71Mars Mission.Technical Memo 391-129,Jet Propulsion Laboratory.   
Clemence,G.M.(1954).Perturbations of the Five OuterPlanets by theFour Inner Ones.In Astronomical Papersof theAmerican EphemerisandNautical Almanac,VolumeXII,partV. Washington,DC:U.S. Government Printing Office.   
Clemence,G.M.,J.G.Porter,andD.H.Sadler(1952).Aberrationin theLunarEphemeris. Astronomical Journal57,46-47.   
Debarbat,S.andB.Guinot (197O).La Methodedes Hauteurs Egales enAstronomie.Paris:Gordon& Breach.   
Eckert,W.,D.Brouwer,and G.M. Clemence (1951).Coordinates of the Five Outer Planets 1953- 2060.In Astronomical Papers of the American Ephemeris and Nautical Almanac,Volume XI. Washington,DC: U.S. Government Printing Office.   
Eckert,W.J.,R.Jones,andH.K.Clark(1954).ImprovedLunar Ephemeris1952-1959.Washington, D.C.:U.S.Naval Observatory,Nautical AlmanacOffice.   
Eckert,W.J.,T.C.VanFlandern,andG.A.Wilkins (1969).ANote on the Evaluationof theLatitude of theMoon.MonthlyNotices oftheRoyalAstronomical Society146,473-478.   
Eckert,W.J.,M.J.Walker,andD.D.Eckert (1966).Transformation of the LunarCoordinatesand OrbitalParameters.Astronomical Journal7l,314-332.   
Eckhardt,D.H.(1981).Theory of thelibrationof theMoon.Moon and thePlanets25,3-49.   
Estabrook,FB.(1971a).Private communications.   
Estabrook,FB. (1971b).Derivation of Relativistic Lagrangian for n-Body Equations containing Relativity Parameters $\beta$ and $\gamma$ .IOM14 June 1971,JetPropulsionLaboratory. Section 328.   
Folkner,W.F.,C.FYoder,D.N.Yuan,E.M.Standish,andR.A.Preston (1998).Interior Structure andSeasonal MassRedistributionof Mars fromRadio Tracking ofMars Pathfinder.Science278, 1749-1752.   
Folkner,W.M.,P.Charlot,M.H.Finger,J.G.Williams,O.J.Sovers,X.X.Newhall,andE.M.Standish (1993).Determinationof the extragalactic frame tie from joint analysis of radio interferometric andlunar laser rangingmeasurements.Astronomyand Astrophysics287,279-289.   
Fricke,W.(1971).A Rediscussion of Newcomb's Determination of Precession.Astronomy and Astrophysics13,298-308.   
Fricke,W.(1982).Determinationof the Equinoxand Equator of theFK5.Astronomy and Astrophysics107,L13-L16.   
Fricke,W.andA.Kopff(1963).Fourth Fundamental Catalogue(FK4).Heidelberg:Astronomisches Rechen-Institut.Veroffentlichungen #10.   
Konopliv,A.S.(2002,2003).Private communications.   
Krogh,F.T.(1972).Lecture Notes in Mathematics,362.New York: Springer-Verlag.p.22.   
Lieske,J.H.,T.Lederle,W.Fricke,andB.Morando (1977).Expressions for the Precession Quantities Based upon the IAU (1976) System of Astronomical Constants.Astronomy and Astrophysics 58, 1-16.   
Lyttleton,R.A.,D.L.Cain,andA.S.Liu (1979).NutationofMars.JPLPublication 79-85,Jet Propulsion Laboratory.   
Ma,C.,E.F.Arias,T.M.Eubanks,A.L.Fey,A.-M.Gontier,C.S.Jacobs,O.J.Sovers,B.A. Archinal,andP.Charlot(1998).The International Celestial ReferenceFrameasRealizedby Very LongBaselineInterferometry.AstronomicalJournal1l6,516-546.   
Morrison,L.V.(1996).Private communications.   
Moyer,T.D.(1971).MathematicalFormulation of the Double-Precision Orbit Determination Program (DPODP).Technical Report 32-1527,JetPropulsionLaboratory.   
Moyer,T.D.(2Oo0).Formulationfor Observed and Computed Values of Deep SpaceNetwork Data Types forNavigation.JPLPublication OO-7,JetPropulsionLaboratory.   
Muhleman,D.O.and J.D.Anderson (1981). SolarWind Electron Densities from Viking Dual-FrequencyRadio Measurements.Astrophysical Journal 247,1093-1101.   
Muhleman,D.O.,G.L.Berge,andD.Jones (1988).VLA Observations of Neptune and the Mass of Triton. Informal report, CalTech.   
Muhleman,D.O.,G.L.Berge,andD.J.Rudy (1986).Precise VLA Positions andFlux-Density MeasurementsoftheJupiterSystem.AstronomicalJournal92,1428-1435.   
Muhleman,D.O.,G.L.Berge,D.J.Rudy,A.E.NiellR.P.Linfield,andE.M.Standish (1985). PrecisePosition MeasurementsofJupiter,Saturnand Uranus Systemswith the Very LargeArray CelestialMechanics37,329-337.   
Newcomb,S.(1898a).Tables of the Heliocentric Motion of Mars.In Astronomical Papers of theAmerican EphemerisandNautical Almanac,VolumeVI,partIV.Washington,DC:U.S. Government Printing Office.   
Newcomb,S. (1898b).Tables of the Heliocentric Motion of Mercury.In Astronomical Papers of theAmericanEphemerisandNauticalAlmanac,VolumeVI,partII.Washington,DC:U.S. Government Printing Office.   
Newcomb,S.(1898c).Tables of the Heliocentric Motion of Venus.In Astronomical Papersof theAmerican EphemerisandNautical Almanac,VolumeVI,partII.Washington,DC:U.S. Government Printing Office.   
Newcomb,S.(1898d).TablesoftheMotionofthe Earthonits AxisandAround theSun.InAstronomical Papersof theAmericanEphemerisandNauticalAlmanac,VolumeVI,partI.Washington,DC: U.S.Government Printing Office.   
Newhall,X.X.,E.M.Standish,andJ.G.Williams (1983).DE102:anumerically integrated ephemeris oftheMoonand planets spanningforty-fourcenturies.AstronomyandAstrophysicsl25,150-167.   
Newhall,X.X.and J. G.Willams (1997).Estimation of the Lunar Physical Librations.Celestial MechanicsandDynamical Astronomy66,21-30.   
Nicholson,P.D.(1992).Privatecommunications.   
Pettengill,G.H.,E.Eliason,P.G.Ford, G.B.Loriot,H.Masursky,andG.E.McGill(198O).Pioneer VenusRadarResults:Altimetry and SurfaceProperties.Journal ofGeophysical Research 85,A13, 8261-8270.   
Ross,F.E.(1917).New Elements of Mars.In Astronomical Papersof theAmerican Ephemeris and Nautical Almanac,VolumeIX,partII.Washington,DC: U.S.GovernmentPrintingOffce.   
Schwan,H.(1983).AMethod for theDeterminationofa SystemofPositionsandProper Motions of Starswithan Applicationto theWashington6Inch TCObservations.Heidelberg:Astronomisches Rechen-Institut. Veroffentlichungen #30.   
Shapiro,I.I.(1964).Fourth Test of General Relativity.Physical Review Letters13,789.   
Standish,E.M.(1982).Orientationof theJPLEphemerides,DE200/LE200,to theDynamicalEquinox ofJ2000.Astronomyand Astrophysics114,297-302.   
Standish,E.M.(199O).The observational basis for JPL's DE2OO,the planetary ephemerides of the Astronomical Almanac.AstronomyandAstrophysics233,252-271.   
Standish,E.M.(1998).TimeScales intheJPLandCfAEphemerides.Astronomy and Astrophysics336, 381-384.   
Standish,E.M.(2oo4).Anapproximation to the errors inthe planetary ephemerides ofthe Astronomical Almanac.Astronomy and Astrophysics417,1165-1171.   
Standish,E.M.,X.X.Newhall,J.G.Williams,andD.K.Yoemans (1992).Orbital Ephemerides of the Sun,Moon,andPlanets.InP.K.Seidelmann (Ed.),ExplanatorySupplementtoTheAstronomical Almanac,Chapter5,pp.279-323.Mill Valley,CA:University Science Books.   
Standish,E.M.and J. G.Williams (199O).Dynamical Reference Frames in the Planetaryand Earth-MoonSystems.InJ.H.LieskeandV.K.Abalakin (Eds.),Inertial Coordinate Systemon theSky, Dordrecht,pp.173-181.Kluwer.   
Stone,R.C.(1998).CCD Positions for the Outer Planets in 1996-97 Determined in the Extragalactic ReferenceFrame.Astronomical Journal1l6,1461-1469.   
Stone,R.C.andF.H.Harris (2OO0).CCDPositions Determined in the International Celestial Reference Frame(ICRF) forthe OuterPlanetsand Manyof theirSatelitesin1995-99.Astronomical Journal119,1985-1998.   
Will,C.M.(1974).Thetheoretical toolsof experimental gravitation.InB.Bertoti (Ed.),Experimental Gravitation,New York.Academic Press.Proceedingsof the International School of Physics "Enrico Fermi";course 56.   
Williams,J.G.(1984).DeterminingAsteroidMasses fromPerturbationsonMars.Icarus57,1-13.   
Williams,J.G.(1994).Contributionsto the Earth's obliquity rate,precession,and nutation. AstronomicalJournal108,711-724.   
Willams,J.G.,D.H.Boggs,C.FYoder,J.T.Ratcliff,andJ.O.Dickey(2OO1).Lunarrotational dissipationinsolidbodyandmoltencore.JournalofGeophysicalResearch106El1,27933-27968.   
Willams,J.G.andE.M.Standish (1989).DynamicalReferenceFramesin thePlanetary and Earth-MoonSystems.InJ.Kovalevsky,I.I.Mueller,andB.Kolaczek (Eds.),ReferenceFrames, Dordrecht.Kluwer.   
Yoder,C.F.(1979).Effects of the Spin-Spin Interaction and the Inelastic Tidal Deformation on the LunarPhysicalLibrations.InP.E.NacozyandS.Ferraz-Mello (Eds.),Natural and Artificial SatelliteMotion,University of TexasPress.Austin.

# Planetary Satellites and Rings

JAMESR.ROHDEANDMARKSTOLLBERG

# 9.1 Introduction

Theephemerides of most satellites in The Astronomical Almanacarecalculated fromaset ofanalytical expressions,termed a theory,for the motion of the satellite in an orbit that is basically anellipse,but subject to variousperturbing forces,such as the oblateness of the planetand the attractions of other satellites and the Sun.The orbits of the outer satellites of Jupiter are highly perturbed and representations by theories are not sufficiently accurate.In these cases numerical integrations of the equations of motion of the satellites are used.

The objective of this chapteris to describe the theory ofthe motion of each ofthe principal satellites in enough detail for search and identification purposes.In many cases,a description of the complete theory that can be used for the precise analysis of observations is given,but in caseswhere the theories contain large numbers of periodic terms,only an outline of the theoryis given,togetherwith references towhere the complete theory can be found.

There has been a recent proliferation of known satellites associated with the gas giant planets.A set of criteria has been developed for which satellites are included in The Astronomical Almanac;see $\ S 9 . 6$ fordetails.A more complete listing of the satellites is given in The Astronomical Almanac Online at URL[1].

# 9.2 Orbital Elements and Perturbations

# 9.2.1 Orbital Elements

In this section we use a fairly common notation to define the osculating elements,formulae,and transformations.The orientation of the orbital plane relative to a reference plane and origin are describedby three elements,which are showninFigs.9.1and9.2.These elementsare

$$
\begin{array} { r l } & { \omega = \mathrm { a r g u m e n t o f t h e } \mathrm { p e r i c e n t e r } } \\ & { \Omega = \mathrm { l o n g i t u d e o f t h e a s c e n d i n g n o d e } } \\ & { \ i = \mathrm { i n c l i n a t i o n } . } \end{array}
$$

In addition,the size and shape of the orbit are described by the semimajor axis $^ { a }$ and eccentricity $e$ .The position of the satellite along the orbit,measured from the pericenter,is describedbythemeananomaly $M$ or the true anomaly $f$ .Thedifference $f - M$ isknown

![](images/dda30d8ed5f0ad12336a5d75065609ab2d079d68b7044f3f3e86bd19aaad2add.jpg)  
Figure9.1 The orbital elements used to describe the orbital plane relative to a reference plane and an origin of longitude $o$

![](images/316524cce07e501b38fe5b2df50f9664500e4aaacba203773b68e96c4de38b57.jpg)  
Figure9.2 An equivalent form of the orbital elements.The end-on view of a great circle onthecelestial sphere isrepresented asa straight line.Triangles formed by such lines are spherical triangles,and the formulae of spherical trigonometry apply.

as the equation of center.The equation of center can be approximated to sufficient accuracy for the satellites by

$$
f - M = \left( 2 e - \frac { 1 } { 4 } e ^ { 3 } \right) \sin M + \frac { 5 } { 4 } e ^ { 2 } \sin 2 M + \frac { 1 3 } { 1 2 } e ^ { 3 } \sin 3 M .
$$

For many satellites the pericenteris ill-defined since $e$ is small,or the nodeis ill-defined since $i$ is small In the former case it is usual to use the quantity $\lambda$ ,rather than $M$ ,and in the latter case the quantity $\omega$ ,ratherthan $\omega$ ,where

$$
\begin{array} { r l r l } & { \lambda = M + \omega + \Omega } & & { \mathrm { ( t h e ~ m e a n ~ l o n g i t u d e ) } } \\ & { \varpi = \omega + \Omega } & & { \mathrm { ( t h e ~ l o n g i t u d e ~ o f ~ p e r i c e n t e r ) } . } \end{array}
$$

# 9.2.2 Secular Perturbations of the Orbit

If the orbit were unperturbed,then all the elements would remain constant except the mean anomaly $M$ ，which would increase at a constant rate $n$ ,the mean motion of the satellite. Fora perturbed orbit the same elliptical model can be used,but the orbital elements,now called osculating elements,are functions of time,typically of the form of aconstant plus periodic terms.In addition,the angular elements can have a linear (or secular） variation with time.The form of the expressions for the osculating elements depends on the reference plane chosen.The oblateness of the planet causes the pole of the orbital plane to precess around the pole of the planet,and solar perturbations cause it to precess around the pole of the planet's orbit.Perturbations by other satellites cause precession around the poles of their orbital planes,but usually this effect is smaller than the other two effects.Because the satelites’orbital polesare usuallyclose to the poleofthe planet,their effectisprimarilyan addition tothe oblatenesseffect.The Laplacianplaneis the reference planeabout whose axis the satellite's orbit precesses as aresult of these two major effects.The axis of the Laplacian plane is coplanar with and between the polar and orbital axes of the planet.Hence,the node of the orbit regresses around a plane that lies between the equatorial and orbital planes of the planet,and has acommon line of intersection with the planes.The orbit maintains aconstant inclination to the Laplacian plane (apart from other,usually smaller perturbing effects).The Laplacian plane isalso knownasthe invariable plane through the planet.

The location of the Laplacian plane is shown in Fig.9.3.It divides the angle between the equatorial and orbital planes into parts $i _ { 1 }$ and $i _ { 2 }$ ,where

$$
2 n ^ { 2 } J _ { 2 } r _ { 0 } ^ { 2 } \sin 2 i _ { 2 } = a ^ { 2 } n ^ { \prime 2 } ( 1 - e ^ { \prime 2 } ) ^ { - 1 / 2 } \sin 2 i _ { 1 }
$$

where $J _ { 2 }$ is the oblateness coefficient of the planet; $r _ { 0 }$ is the equatorial radius of the planet; $n ^ { \prime }$ is the orbital mean motion of the planet; $e ^ { \prime }$ is the orbital eccentricity of the planet;and $n$ is the mean motion of the satellite.

Apart from small short-period perturbations,the motion of the satellite's orbit relative to theLaplacian plane is such that

$$
\begin{array} { l } { { \gamma = \mathrm { c o n s t a n t } } } \\ { { \theta = \theta _ { 0 } - K \left( t - t _ { 0 } \right) } } \end{array}
$$

where $\gamma$ is the inclination of the satellite's orbit to the Laplacian plane,and $\theta$ is the arc reckoned from the intersection ofthe planet'sequatorialand orbitalplanes along theLaplacian plane to the node of the satellite's orbit on the Laplacian plane.However,it is usually more convenient to takea plane other than the Laplacian planeas the reference plane,as it eases the calculation of perturbations by other objects,and also eases the transformation of the calculated position to a reference frame based on the Earth's equator (which is needed for comparison with observations).If,for example,the orbital plane of the planet in Fig.9.3 is takenas the reference plane,then the osculating inclination and longitude of the node will be the angles $i$ and $\Omega$ .The formulae of spherical trigonometry give

$$
\begin{array} { r l } & { \sin i \sin ( \Omega - \Omega _ { 1 } ) = \sin \gamma \sin \theta } \\ & { \sin i \cos ( \Omega - \Omega _ { 1 } ) = \cos \gamma \sin i _ { 1 } + \sin \gamma \cos i _ { 1 } \cos \theta } \end{array}
$$

![](images/c0614c29eefcacbfbe26ecd328d5c1bd7d42970bf0dbf766c3367fbc4a75679c.jpg)  
Figure9.3 The Laplacian plane

where $i _ { 1 }$ , $\Omega _ { 1 }$ are the inclination and longitude of the node of the Laplacian plane relative to the adopted reference plane;and $\gamma$ and $\theta$ are defined above.In most cases $\gamma$ is small, and so $( \Omega - \Omega _ { 1 } )$ is small as well.Thus,the following approximate formulae are obtained:

$$
\begin{array} { l } { i = i _ { 1 } + \gamma \cos \theta } \\ { \Omega = \Omega _ { 1 } + \gamma \sin \theta / \sin i . } \end{array}
$$

Hence,the use of a reference plane other than the Laplacian plane introduces a periodic oscillation into the osculating inclination and longitude of the node.Note that $i _ { 1 }$ and $\Omega _ { 1 }$ are quantities whose values are determined by the physical properties of the system.The arbitrary constants associated with the inclination and node are the quantities $\gamma$ and the phase of $\theta$ .This choice of reference plane also introduces a periodic variation,equal to theangular difference $\phi + \Omega - \Omega _ { 1 } - \theta$ ,into the longitude of the pericenter and the mean longitude.This periodic variation is given approximately by

$$
\Delta \varpi , \Delta \lambda = \gamma \tan { \frac { 1 } { 2 } } i _ { 1 } \sin \theta .
$$

For most satellites the oblateness effect on the orbital plane is much larger than the solar perturbations,and so the Laplacian plane is very close to theequatorial plane.Fora more distantsatellite,such as Iapetus,the effectsare comparable,so the Laplacian plane lies about midway between the equatorial and orbital planes.For the Moon,the solar perturbations dominate,and theLaplacian plane virtually coincides with the Earth'smean orbital plane— the ecliptic.

The oblateness,solar,and otherperturbations also cause secularvariations ofthe longitude of pericenter (in most cases the pericenter advances around the orbit) and of the mean longitude of the satellite,so that the mean motion in longitude is different from(generally greater than)thevalue derived from Kepler'slaw foranunperturbed orbit.Itis this overall rate of motion that is quotedas the satellite’smean motion,and itis thusan observed mean motion. Hence, when using the mean motion to determine the mass of the planet from Kepler's law,one must allow for the part of it due to secular perturbations.

It is usefulto note in this context that the semimajor axis ofthe orbit is affected ina similar way.The various perturbing forces cause perturbations of the eccentricity and the longitude of the pericenter of the form

$$
\begin{array} { r } { \Delta e = A \cos M } \\ { e \Delta \varpi = A \sin M . } \end{array}
$$

The effect of these terms on the true longitude is zero to first-order.The perturbation of the distance $r$ arising from $\Delta e$ and $\Delta \varpi$ is obtained from

$$
r = a ( 1 - e \cos M )
$$

with $M = \lambda - \varpi$

Differentiating Eq.9.9,we have

$$
\begin{array} { c } { { \Delta r = - a \cos M \Delta e - a e \sin M \Delta \varpi } } \\ { { { } } } \\ { { = - a A . } } \end{array}
$$

It is the normal practice to ignore these terms in $e$ and $\varpi$ ,and to determine thevalue of the semimajor axis from observations that willabsorb the constant term.This must be allowed for when computing the mass of the planet from Kepler's law.

# 9.2.3Perturbations due to Commensurabilities

There are many instances of pairs of satellites with mean motions, $n$ and $n ^ { \prime }$ ,havinga relationship of the form

$$
p n \simeq q n ^ { \prime }
$$

where $p$ and $q$ are two small integers.Such a situation is called a commensurability of meanmotionsor,more simply,an orbital resonance,because it causes increased mutual perturbations.This resonance effect is caused by a repeated geometric relationship of the positions of the two satelites (their longitudes) relative to a particular point in their orbits. This point isusually the pericenter of one of the satellites,but forMimas-Tethys it is the midpoint of their nodes on the equator of Saturn.We shall take as an example the case where the commensurability is

$$
2 n ^ { \prime } - n - \dot { \varpi } \simeq 0 .
$$

The prime refers to the outer satellite,and $\dot { \varpi }$ is the secular rate of change of the longitude of the pericenter of the inner satelite,caused by the oblateness ofthe planet,other perturbations, and by the resonance itself.As aresult the angular argument

$$
\theta = 2 \lambda ^ { \prime } - \lambda - \varpi
$$

variesvery slowly.If $\theta$ eitherincreases or decreases continually,then the motion is termed circulation,because the position ofconjunctions of the satelites circulates around their orbits, and in this case the mutual perturbations are not particularly large.In many cases,however,

theaverage rate of change of $\theta$ is zero,and the value of $\theta$ oscillates about either $0 ^ { \circ }$ or $1 8 0 ^ { \circ }$ , depending on the type of commensurability.This type of motion is termed libration.In this example,the libration is about $0 ^ { \circ }$ ,and we can write $\theta$ as

$$
\theta = ( \lambda - \varpi ) - 2 ( \lambda - \lambda ^ { \prime } ) = 0 ^ { \circ } + \mathrm { o s c i l l a t i o n } .
$$

Ata conjunction of the satellites, $\lambda - \lambda ^ { \prime } = 0$ ,and so $\lambda - \varpi$ will be close to zero also,and hence all conjunctions occur near the pericenter of the inner satellite orbit.As might be expected, this particular type of resonance has a significant perturbing effect on the longitudes of the two satellites,and on the longitude of pericenterand eccentricity of the inner satellite.If thelibration amplitude is small,then the libration can be represented adequately by a single periodic term; e.g.,

$$
\theta = 0 ^ { \circ } + B \sin ( \beta t + \varepsilon ) .
$$

Iftheamplitudeis large,e.g.,forthe Titan-Hyperionand Mimas-Tethysresonances,then aFourier series is needed to represent the libration.The amplitude $B$ and phase $\varepsilon$ ofthe libration are the arbitrary constants associated with $e$ and $\varpi$ .The libration frequency $\beta$ is afunction of the masses of the satellites,the closeness of the commensurability,and the libration amplitude,if itis large.

The principal effects of this resonance on the orbit are to cause perturbations of the longitudes of the satelites with the period of the libration,and to cause a forced component of the eccentricity,whose magnitude depends on the mass of the perturbing satelite and the closeness of the commensurability.This forced component is usually the largest component of the eccentricity.

The commensurabilities that are of most significance in the satellite systems are listed in Table 9.1.In addition many of the features of the rings of Saturn are associated with commensurabilities with satellites.Some ofthe smallsatellites of Saturnarein1:1commensurabilities with the major satellites.These commensurabilities cause the small satellites to follow or precede the majorsatellites by $6 0 ^ { \circ }$ in theirorbits.The2:1commensurabilitiesamong theGalilean satellites Io,Europa,and Ganymede are closely associated with the Laplace commensurabilitythat affectsall three satelltes;as a result,the long-term mean value of $( n _ { 1 } - 3 n _ { 2 } + 2 n _ { 3 } )$ is exactly zero,and the angular argument $( \lambda _ { 1 } - 3 \lambda _ { 2 } + 2 \lambda _ { 3 } )$ has a mean value of $1 8 0 ^ { \circ }$ ,and oscillates about this value with amplitude $0 \% 0 6 6$ and period 2070 days.

# 9.2.4Long-Period Perturbations by Other Satellites

The pericenters and nodes of satelite orbits move slowly compared with the orbital speed, and so the relative motion of the pericenters or nodes of a pair of satellites is slow,and significant perturbations can arise from the arguments $\varpi - \varpi ^ { \prime }$ or $\Omega - \Omega ^ { \prime }$ In the planetary systemthese are called secular perturbations,butthey arein factof very long period-25,000 years and longer.Inthe satellite systems the periods are much shorter,and the perturbations areusually represented by periodic terms.The magnitude of this effect depends on the mass of the perturbing satellite and the size of its eccentricity or inclination.Hence,for example, in the Saturn system only the effects of Titan are significant.Its effect on the osculating eccentricity $e$ and longitude of pericenter $\varpi$ of Rhea are of the form

Table 9.1 Principal commensurabilities among satellites   

<table><tr><td>Argumenta</td><td>Satellites</td><td>Libration Amplitudeb</td></tr><tr><td>2x-λ-の</td><td>Enceladus-Dione</td><td>15</td></tr><tr><td>1</td><td>Io-Europa</td><td>1</td></tr><tr><td>&quot;</td><td>Europa-Ganymede</td><td>3°</td></tr><tr><td>2λ-λ-の&#x27;</td><td>Enceladus-Dione</td><td>C</td></tr><tr><td>1</td><td>Io-Europa</td><td>3</td></tr><tr><td>1</td><td>Europa-Ganymede</td><td>C</td></tr><tr><td>4x&#x27;-2λ-2-2&#x27;</td><td>Mimas-Tethys</td><td>97°</td></tr><tr><td>4λ-3λ-の&#x27;</td><td>Titan-Hyperion</td><td>36°</td></tr><tr><td>2λ&quot;-3λ&#x27;+λ</td><td>Io-Europa-Ganymede</td><td>0.07</td></tr><tr><td>2λ&quot;-3λ&#x27;+λ</td><td>Miranda-Ariel-Umbriel</td><td>C</td></tr></table>

äA prime refers to the outer satellite of a pair or to the middle satelliteof a triplet. Double-primes refer to the outer satelite of triple commensurabilities. b Circulation motion is denoted by C.

$$
\begin{array} { r } { e \cos \varpi = e _ { \mathrm { p } } \cos \varpi _ { \mathrm { p } } + e _ { \mathrm { f } } \cos \varpi _ { \mathrm { T } } } \\ { e \sin \varpi = e _ { \mathrm { p } } \sin \varpi _ { \mathrm { p } } + e _ { \mathrm { f } } \sin \varpi _ { \mathrm { T } } } \end{array}
$$

where $\varpi _ { \mathrm { T } }$ isthe longitude of the pericenter of Titan, $e _ { \mathrm { f } }$ isa forced component of the eccentricity caused by its resonance with Titan,and $e _ { \mathrm { p } } , \varpi _ { \mathrm { p } }$ are the proper eccentricity and longitude of pericenter of Rhea,so that $e _ { \mathrm { p } }$ and the phase of $\varpi _ { \mathrm { p } }$ are arbitrary constants,and the rate of $\varpi _ { \mathrm { p } }$ is due principally to the oblateness of Saturn.

This effect is particularly noticeable forRhea,as the forced eccentricity $e _ { \mathrm { f } }$ is much larger than the proper eccentricity $e _ { \mathrm { p } } .$ In this particularcase $\varpi _ { \mathrm { T } }$ is the proper longitude of pericenter of Titan, and $e _ { \mathrm { f } }$ is related to the proper eccentricity and mass of Titan.

Inthe satellite systems ofJupiterand Saturn there are several satellitesof large mass compared to that of the other satellites,and so theyare liable to cause sizable forced eccentricities or inclinations oneach other’sorbits.These forced componentscan themselves cause significant forced components on other satellites,and the resulting terms can have frequencies quite different from the natural frequencies of the system due to the oblateness, etc.To compute these perturbations the eigenvalue theory used for the secular perturbation theory of the planets must beused (see Brouwer and Clemence 1961).

# 9.3Planetocentric Rectangular Coordinates

The theory of the motion of a satellite gives expressions for the osculating elements as functions of time.In many cases it is more convenient to represent the position of a satellite inits orbit in rectangular coordinates rather than osculating elements.Let the osculating elements of the satellite be $a , e , i , \lambda , \varpi$ ,and $\Omega$ .Then,

1.calculate the mean anomaly $M$ from

$$
M = \lambda - \varpi .
$$

2.Determine the eccentric anomaly $E$ from Kepler's equation

$$
E - e \sin E = M .
$$

3.Calculate the coordinates $x , y$ in the orbital plane (where the $x$ -axisis toward the pericenter) from

$$
\begin{array} { l } { x = a ( \cos E - e ) } \\ { \qquad \quad } \\ { y = a ( 1 - e ^ { 2 } ) ^ { 1 / 2 } \sin E . } \end{array}
$$

Methods for solving Kepler's equation can be found in standard celestial mechanics texts.

4.Next calculate the coordinates $x _ { 1 }$ ， $y _ { 1 }$ ， $z _ { 1 }$ relative to the reference plane and $x$ -axis directionused foraparticular satelite.If,as inFig.9.1,the orbit is related directly to thereference plane by the orbital elements,then $x _ { 1 }$ , $y _ { 1 }$ , $z _ { 1 }$ are given by

$$
\left[ \begin{array} { l } { x _ { 1 } } \\ { y _ { 1 } } \\ { z _ { 1 } } \end{array} \right] = \mathbf { R } _ { 3 } ( - \Omega ) \mathbf { R } _ { 1 } ( - i ) \mathbf { R } _ { 3 } ( - \omega ) \left[ \begin{array} { l } { x } \\ { y } \\ { 0 } \end{array} \right]
$$

where $\omega = \varpi - \Omega$ ,and ${ \bf R } _ { i } ( a )$ for $i = 1$ ,2,3 isa rotation through anangle $^ a$ about the current $x$ -， $y \cdot$ ,or $Z$ -axisrespectively (see $\ S \ 1 4 . 4$ for expressions for these rotation matrices).This particular transformation is given explicitly as

$$
\begin{array} { r l } & { x _ { 1 } = ( x \cos \omega - y \sin \omega ) \cos \Omega - ( x \sin \omega + y \cos \omega ) \sin \Omega \cos i } \\ & { y _ { 1 } = ( x \cos \omega - y \sin \omega ) \sin \Omega + ( x \sin \omega + y \cos \omega ) \cos \Omega \cos i } \\ & { z _ { 1 } = ( x \sin \omega + y \cos \omega ) \sin i . } \end{array}
$$

A more complicated case is shown inFig.9.4,where the orbit is referred toan intermediate plane (e.g.,the equator of the planet) which is itself referred to the reference plane and $x$ -axis direction. The coordinates $x _ { 1 }$ $y _ { 1 } , z _ { 1 }$ are given by

$$
\left[ \begin{array} { l } { x _ { 1 } } \\ { y _ { 1 } } \\ { z _ { 1 } } \end{array} \right] = \mathbf { R } _ { 3 } ( - \Omega _ { \mathrm { e } } ) \mathbf { R } _ { 1 } ( - i _ { \mathrm { e } } ) \mathbf { R } _ { 3 } ( - N + \Omega _ { \mathrm { e } } ) \mathbf { R } _ { 1 } ( - \gamma ) \mathbf { R } _ { 3 } ( - \omega ) \left[ \begin{array} { l } { x } \\ { y } \\ { 0 } \end{array} \right]
$$

where $i _ { \mathrm { e } }$ and $\Omega _ { \mathrm { e } }$ are the inclination and node of the intermediate plane,and $\gamma$ and $N$ are the inclination and node of the orbital plane,as shown in Fig.9.4.

If the coordinates $x _ { 1 }$ , $y _ { 1 } , z _ { 1 }$ are referred to the ecliptic and equinox of B1950.0,then the coordinates $x _ { 2 }$ , $y _ { 2 }$ , $z _ { 2 }$ of the satellite relative to the center of mass of the planet,in the frame of theEarth's equator and equinox ofB1950.0,are

$$
\left[ \begin{array} { l } { x _ { 2 } } \\ { y _ { 2 } } \\ { z _ { 2 } } \end{array} \right] = \mathbf { R } _ { 1 } ( - \varepsilon ) \left[ \begin{array} { l } { x _ { 1 } } \\ { y _ { 1 } } \\ { z _ { 1 } } \end{array} \right]
$$

where $\varepsilon = 2 3 ^ { \circ } . 4 4 5 7 8 7 8 7$ is the obliquity of the ecliptic at B1950.0.

If the coordinates must be referred to the equator and equinox of some epoch other than B1950.0 (e.g.,“of date”or of J2ooo.O),then precession should be applied to $x _ { 2 } , y _ { 2 } , z _ { 2 }$ .The precession matrix from B1950.0 to J2000.0 is given in $\ S \ 3 . 5 9 1$ of Hohenkerk et al.(1992).

![](images/e8258ea0c8bf83ef6622eb6458db6cef19c6f557134aafb7a032aa2929d9b89d.jpg)  
Figure9.4 Thesatellite orbit referred toanintermediate plane,where $P$ is the pericenter of the satellite orbit and $N = \Omega _ { e } + A B$

![](images/630fd5438979b14f51e36ebf521e73d0760bfb06350af2f5d93ef9580f552951.jpg)  
Figure9.5 Coordinates of the satelliterelative to the planet: $p =$ position angle, $s =$ angular distance, $\xi = \Delta \alpha$ cosδ,and $\eta = \Delta \delta$ . $\Delta \alpha =$ differencein right ascension (satellite minus planet), $\Delta \delta =$ difference in declination (satellite minus planet), and $\delta =$ declination of planet.

We now consider the apparent position of the satelite as seen by an observeron the Earth. Let $\xi = \Delta \alpha$ cos $\delta$ and $\eta = \Delta \delta$ be the differential coordinates of the satellitein right ascension and declination respectively (see Fig.9.5).The differences are in the sense satellite minus center of planet.Then,to first order,

$$
\begin{array} { l } { { \xi = ( y _ { 2 } \cos \alpha - x _ { 2 } \sin \alpha ) / r } } \\ { { \eta = ( z _ { 2 } \cos \delta - x _ { 2 } \sin \delta \cos \alpha - y _ { 2 } \sin \delta \sin \alpha ) / r } } \end{array}
$$

where $\alpha$ and $\delta$ are the right ascension and declination of the planet; $r$ is the distance of the planet from the Earth,in the same units as $x _ { 2 }$ , $y _ { 2 } , z _ { 2 }$ (usually au);and $\xi$ and $\eta$ are in radians.

The position angle $p$ and angular distance $s$ of the satellite relative to the planet are given by

$$
\begin{array} { l } { \tan p = \xi / \eta } \\ { s = ( \xi ^ { 2 } + \eta ^ { 2 } ) ^ { 1 / 2 } . } \end{array}
$$

# 9.4Traditional Method

# 9.4.1 The Apparent Orbit

The apparent orbit of a satellite on the geocentric celestial sphere is an ellipse that is the orthogonal projection,in the direction of the line of sight,of the actual orbit in space.In a circularorbit,the orbital diameterthat isperpendicular to the line of sightis projected into the major axis of the apparent ellipse.At its extremities,the satellite is at its greatest elongations from the primary.In planning observations of sateliteswith short-period orbits,times of greatest elongations are more useful than differential coordinates.

Attimes of greatest elongation the satelite and planet center areseparatedby an apparent angular distance $a / \Delta$ ,where $^ { a }$ is the apparent semimajor axis in arcsecondsat a distance of one astronomical unit and $\Delta$ is the geocentric distance of the primary.The orbital diameter that liesin the plane formed by the line of sight andthe normalto the orbitalplane,projects into the minor axis.Atthe further extremity ofthis diameter,the satelite is insuperior geocentric conjunction with theprimary,and at the nearer extremity it is at inferior conjunction.The ratio of the semiminor axis to the semimajor axis is the absolute value of sin $B$ ,where $B$ is the angle between the line of sight and the plane of the orbit.

On the planetocentric celestial sphere of the primary,the path of the satellite is agreat circle,and the positions of the satelite on the planetocentric sphere at any time are obtained from the orbital elements.To represent these positions,the same coordinate systems are adopted as those defined on the geocentric celestial sphere by the equator and the ecliptic. Because of the mathematically infinite radius of the celestial sphere,these reference circles areinidentically the same positions on the planetocentric sphere as on the geocentric sphere. The Earth on the planetocentric sphere is diametrically opposite the geocentric position of the planet,and,therefore,at right ascension $\alpha \pm 1 8 0 ^ { \circ }$ and declination $- \delta$ ,where $\alpha$ and $\delta$ are the geocentric coordinates of the planet.

Referred to the celestial equator,the position of the great circle that the satellite describes on the planetocentric sphere is represented by its inclination $( J )$ and the right ascension $( N _ { \cdot }$ ) of its ascending node,or by the right ascension $( N - 9 0 ^ { \circ } )$ and declination $( 9 0 ^ { \circ } - J )$ of the pole of the orbit.The major axis of the apparent elliptic orbit that the satelite describes on the geocentric sphere is parallel to the plane of this great circle.

InFig.9.6 the following angles are indicated:

$P$ :The position angle of the minor axis of theapparent orbit,measured from North.The axis selected is the one pointing toward the pole of the orbit relative to which the satellite motion is direct.

![](images/f599742d4fbcc4b1cd59443240db9f9e48b7a3060c09f1b09e02f4c0845361f5.jpg)  
Figure9.6 Planetocentric celestial sphere.The Earth has right ascension, $1 8 0 ^ { \circ } + \alpha$ ,and declination, $- \delta .$ $\Upsilon _ { x } = 1 8 0 ^ { \circ } + \alpha$ and $x ^ { \prime } x = 1 8 0 ^ { \circ } + \alpha - ( N - 9 0 ^ { \circ } ) = \alpha - N - 9 0 ^ { \circ }$

$B$ :theplanetocentric latitude of the Earth relative to the orbital plane of the satellite; positive toward the pole of the orbit for which motion is direct. $U$ :the geocentric longitude of the planet measured around the orbit of the satellite,from the ascending node on the Earth's equator. Hence,the planetocentric longitude of the Earth,measured from the same point, is $U - 1 8 0 ^ { \circ }$ .

From spherical triangle $Q R E$ shown in Fig.9.7 we obtain

$$
\begin{array} { c } { \cos B \sin U = + \cos J \cos \delta \sin ( \alpha - N ) + \sin J \sin \delta } \\ { \cos B \cos U = + \cos \delta \cos ( \alpha - N ) } \\ { \sin B = + \sin J \cos \delta \sin ( \alpha - N ) - \cos J \sin \delta } \\ { \cos B \sin P = - \sin J \cos ( \alpha - N ) } \\ { \cos B \cos P = + \sin J \sin \delta \sin ( \alpha - N ) + \cos J \cos \delta . } \end{array}
$$

The position of the satellite is described by $u$ ——theplanetocentric longitude of the satellite measured in the same way as $U$ —and $\sigma$ —theplanetocentric angular displacement of the satellite from theanti-Earth direction; $\sigma$ takes the value $0 ^ { \circ }$ to $1 8 0 ^ { \circ }$ ,and has thevalue $1 8 0 ^ { \circ }$ whenthesatelliteliesbetweentheplanetand theEarth.

![](images/fc55f6d807faf77089c7940f80539057dc4f80292af8347f56cfb2bcab553e08.jpg)  
Figure9.7 Spherical triangleused to compute $U$ , $B$ ,and $P$

![](images/54e75cbb6e6c6c2bebb67afa03a4ee3870d12773a6ef555cd11d575c7110f552.jpg)  
Figure9.8 Spherical triangle used to compute $\sigma$ and $p - P$

From spherical triangle $E T S$ shown in Fig.9.8 we obtain

$$
\begin{array} { c } { \sin \sigma \sin ( p - P ) = \sin ( u - U ) } \\ { \sin \sigma \cos ( p - P ) = \sin B \cos ( u - U ) } \\ { \cos \sigma = \cos B \cos ( u - U ) . } \end{array}
$$

Let $r$ be the distance of the satellite from the planet, $\Delta$ be the distance of the planet from the Earth, $\Delta _ { \mathrm { s } }$ be the distance of the satellite from the Earth,and $s$ be the geocentric distance of the satellite from the planet. $r$ , $\Delta$ ,and $\Delta _ { \mathrm { s } }$ are measured in units of length, and $\mathbf { \Delta } _ { \mathbf { { \mathcal { S } } } }$ ismeasured in units of arc.

Then,from the plane triangle formed by the Earth, the planet,and the satellite,

$$
\begin{array} { l } { \Delta _ { \mathrm { s } } \sin s = r \sin \sigma } \\ { \Delta _ { \mathrm { s } } \cos s = r \cos \sigma + \Delta . } \end{array}
$$

![](images/1adcf3aebdb0195efdcc933ab477dd972fbc2e1eea7f72d00b3fbb1625fefb69.jpg)  
Figure9.9 Apparent orbit of asatelliteof the primary $P$ as projected onthe geocentric sphere.This figure shows the situation when the Earth is north of the orbital plane of the satellite.

With sufficient accuracy we may write:

$$
s = \frac { r } { \Delta \sin 1 ^ { \prime \prime } } \sin \sigma = \frac { a } { \Delta } \sin \sigma
$$

where $a$ is the apparent semimajor axis in arcseconds at a distance of one astronomical unit. Rigorous formulae for $p$ and $s$ in terms of the differential coordinates of the satellite,and also in terms of the planetocentric coordinates,are given later.

At greatest elongation, $u - U = \pm 9 0 ^ { \circ }$ , $\sigma = 9 0 ^ { \circ }$ ,and $s = a / \Delta$ where the position angle $p = P \pm 9 0 ^ { \circ }$ .At the extremities of the minor axis of the apparent orbit,the satellite is at inferior or superior conjunction; $u - U$ is $0 ^ { \circ }$ or $1 8 0 ^ { \circ }$ , $\sigma = B$ ,and theposition angle is $P$ or $P + 1 8 0 ^ { \circ }$ .Evidently,when theEarthisnorth of theorbital plane,the satellite isat inferior conjunction at the southern extremity of the minor axis,and is at superior conjunction at the northern extremity (see Fig. 9.9); $B$ is then positiveif the motion is direct,negative if retrograde.When the Earth is south of the orbital plane,superior conjunction is at the southern extremity of theminor axis,and $B$ isnegative in direct motion,positivein retrograde motion. Irrespective,therefore,of whether the motion is direct or retrograde,the position angle at superior conjunction,when $B$ is positive, is $p = P$ ;when $B$ is negative, it is $p = P + 1 8 0 ^ { \circ }$

Theapparent orbit becomes increasingly eliptical as the Earth approaches the orbital plane,and reduces toa straight line when the Earth isin this plane.As the Earth passes through the plane and $B$ changes sign,each superior and inferior conjunction occurs at the opposite extremity of the minor axis from that at which it previously took place.Similarly, when the Earthisin the plane that isperpendicularto the orbital planeand contains the celestial pole,the minor axis is exactly in the north-south direction,and the majoraxis is exactly east-west.As the Earth passes through this plane,the extremity of the major axis that formerly was the more northerly becomes the more southerly.

Only when $J$ is not too greatly different from $0 ^ { \circ }$ or $1 8 0 ^ { \circ }$ is the direction of the minor axis necessarily nearly enough north and south for the elongations to be strictlyand unambiguously described as eastern and western.When $J$ is in the neighborhood of $9 0 ^ { \circ }$ ,asin the case of the satellites of Uranus and Pluto,the direction of the minor axis on the celestial sphere rangesfrom north-south to east-west.Thisintroduces confusion in the terminology for the elongations,but in general they are more appropriately regarded as northern and southern than as eastern and western.

In the ephemerides for finding the apparent distance $s$ and position angle $p$ ,the factor sin $o$ giving the ratio of $s$ to the apparent distance at greatest elongation is denoted by $F$ ,and therefore the apparent distance of the satellite from the primary is given by

$$
s = F a / \Delta .
$$

With $P _ { 0 }$ denoting an arbitrary fixed integral number of degrees near the value of $P$ at opposition, the value of $p$ at any time is expressed in the form $p _ { 1 } + p _ { 2 }$ $p _ { 1 }$ is the sum of the approximate position angle at elongation and the amount of motion in position angle since elongation. ,depending on the date,denotes the correction $P - P _ { 0 }$ .Incalculating $F$ and $P _ { 2 }$   
$p _ { 1 }$ ,the value of the eccentricity of the apparent orbit at opposition is used; consequently, in the values of $s$ and $p$ thatare derived from them,the effect of the variation ofthe eccentricity of the apparent orbit is neglected.

Many of the values described in this sectionare tabulated and presented on The Astronomical AlmanacOnline.

# 9.4.2 Calculating Tabulated Values

Theapparent positions of the satelitesarerepresented by their positions relative to the primary,expressed eitherby the apparent angular distance and position angle,or by the differential spherical (or rectangular） coordinates in right ascension and declination. The tabularvalues are corrected forlight-time,and are directly comparable with observationsat thetabular times.It is usuallysufficiently accurate to use the light-time from the planet to the Earth.The timescale of the theories of the satellitesis TDB.The timescale of the ephemerides inTheAstronomical AlmanacisusuallyUT.Thevalueof $\Delta T$ ,where

$$
\Delta T = \mathrm { T T } - \mathrm { U T } , \quad \mathrm { a n d T T \approx \mathrm { T D B } }
$$

is approximated at the time of production of the book and used in the computations.

# 9.4.2.1Times of Greatest Elongation

The method for calculating the inclination,orbital longitude,and longitude of the ascending node with respect to the Earth's equator, $J , u$ ,and $N$ ,respectively,can vary fromsatellite to satellite.The descriptions for these calculationsare contained in $\ S 9 . 7$ through $\ S 9 . 1 2$ .Given that $J , u$ ,and $N$ have been computed for $0 ^ { \mathrm { h } }$ on a given date,and that the right ascension and declination of the primary, $\alpha$ and $\delta$ ,areknown, $U , B$ ,and $P$ are calculated from Eqs.9.26.

The angle to the nearest elongation is given by

$$
d u = 9 0 ^ { \circ } - ( u - U ) .
$$

The time for the satellite to transit this angle is

$$
d t = d u / n .
$$

If $_ { d t }$ is greater than one day, $J , u$ and $N$ ,and then $U , B$ ,and $P$ are redetermined for $0 ^ { \mathrm { h } }$ on the next day. A new $d t$ is then computed.The light-time correction $0 ^ { \mathrm { h } } . 1 3 8 6 1 \Delta$ is then applied to give the time of elongation. $\Delta$ is the Earth-planet distance.

# 9.4.2.2 Apparent Distance and Position Angle

Given $J$ ， $u$ ,and $N$ on the date of opposition, $P$ is determined from Eqs.9.26. $P _ { 0 }$ isthe integral part of $P$ .Now from $J , u$ ,and $N$ at $0 ^ { \mathrm { h } }$ on any date, $U$ , $B$ and $P$ are computed from Eqs. 9.26. $p - P$ and sin $\sigma = F$ are found from Eqs. 9.27. $p _ { 1 }$ is the sum of $p - P$ and $P _ { 0 }$ · $p _ { 2 }$ is the difference $P - P _ { 0 }$ ,where $P$ is the value for $0 ^ { \mathrm { h } }$ on the date in question, not the value at opposition.The determination of $a / \Delta$ is astraightforward computation from the semimajor axis, $^ a$ ,andtheEarth-planetdistance, $\Delta$ .

# 9.4.2.3 Differential Coordinates

Tofirst order,the differential right ascension and declination in the sense satellite minus planet are

$$
\begin{array} { l } { \Delta \alpha = s \sin p \sec ( \delta + \Delta \delta ) } \\ { \Delta \delta = s \cos p } \end{array}
$$

where $\mathbf { \Delta } _ { \mathbf { { \boldsymbol { \mathscr { S } } } } }$ is calculated fromEq.99and $p = p _ { 1 } + p _ { 2 }$

# 9.5 Modern Method

# 9.5.1 The Apparent Orbit

# 9.5.1.1Diferential Tangent Plane Coordinates

For the computation of satellite positions it is necessary to have available either a set of subroutines that evaluate satelite positions from their orbital elements and perturbations atany specified time,oruse themixed function data（ $\langle \ S 9 . 5 . 1 . 2 \rangle$ .The satellite positions $( x _ { 2 } , y _ { 2 } , z _ { 2 } )$ fromEq.9.23 are precessed to the equator and equinox of J2ooo.0,which is moreconvenient formodern observations.Let $\alpha$ and $\delta$ bethe rightascensionand declination of the planet.Then the differential coordinates $X$ , $Y$ of the satellite relative to the planet, referred to axes lying in the tangent plane (see Fig.9.10) are

$$
\begin{array} { l } { X = k ( y _ { 2 } \cos \alpha - x _ { 2 } \sin \alpha ) } \\ { Y = k ( z _ { 2 } \cos \delta - x _ { 2 } \cos \alpha \sin \delta - y _ { 2 } \sin \alpha \sin \delta ) } \end{array}
$$

where

$$
k = \Delta / ( \Delta + z _ { 2 } \sin \delta + y _ { 2 } \cos \delta \sin \alpha + x _ { 2 } \cos \delta \cos \alpha )
$$

![](images/dae3eaab042001dea62fbf41fd53e82af16f5ac40dc6b11b29ee8caca922f88f.jpg)  
Figure9.10 Apparent orbit of the satellte projected onto the tangent plane, and the coordinate system used

and $\Delta$ is the current distance of the planet from the Earth. $X$ and $Y$ will be in astronomical units but can be converted to angular quantities (arcseconds)asseen from the Earth by multiplying by $3 6 0 0 \times 1 8 0 / ( \pi \times \Delta )$ These are the $X$ and $Y$ referred to in the following discussion.

# 9.5.1.2 Mixed Functions Approximation

Thevariations of the tangent plane coordinates are quasi-periodic in character.Using a novel approach formulated by Chapront and Vu(1984),these coordinates can be represented compactly by a mixture of periodic and secular functions (mixed functions).For satelite ephemerides represented by these mixed functions astronomers require to compute the observables $\Delta \alpha \cos \delta$ and $\Delta \delta$ where $\Delta \alpha$ and $\Delta \delta$ are the differences in right ascension and declination of the satellite from the planet respectively. Since $\Delta \alpha$ and $\Delta \delta$ are small, to the first order in small quantities

$$
\begin{array} { r } { \Delta \alpha \cos \delta = X } \\ { \Delta \delta = Y } \end{array}
$$

and to the second order

$$
\Delta \alpha \cos \delta = X + \sin 1 ^ { \prime \prime } X Y \tan \delta
$$

$$
\Delta \delta = Y - \sin 1 ^ { \prime \prime } { \frac { X ^ { 2 } } { 2 } } \tan \delta .
$$

The formulae correct to the second order are needed for satelites with large elongation,such as Iapetus.

This approach to represent satellite ephemerides has been used by Arlot et al.(1986).The satellite ephemerides for the major satellites of Mars,Jupiter,Saturn,and Uranus produced atThe Institut de Mécanique Celeste etde Calcul des Ephémérides (IMCCE)use this form. Taylor (1995) has followed the same approach producing ephemerides of the eight major satellites of Saturn using the mixed functions approximation but with different original theories.This work was later extended to produce ephemerides for the major satellites of Mars,Jupiter,Uranus,and TritonofNeptune'ssystem.These ephemerides have been used in the computation of phenomena and approximate ephemerides,following the methods described in $\ S \ 9 . 5 . 2 . 1$ and $\ S \ 9 . 5 . 2 . 2$ respectively.In producing the mixed functions the complete satelite theories were used.The mixed functions approximation allows a satellite ephemeris toberepresented compactlywhile still retaining theprecision of theoriginal theory.Itis particularly suited to fast-moving satellites where the chosen interval for fitting can be equal to several orbital periods.

Briefly,thismethod represents the differential tangent plane coordinatesbya linear combination ofasetofbasis functions to modelthequasi-periodiccharacterof thecoordinates onachosen time interval mapped to the interval[-1,1]byalinear transformationof the time. From fitting the mixed functions approximation of the coordinate to the coordinate over this chosen time interval using the quadratic mean and seeking the minimum of it,one obtains the coefficients of the basis functions.In fact,the interval for the fitting was taken slightly longerthan the original chosen interval,asa maximum errorat the ends of the interval isa common feature of the fitting process.

If we let $f ( t )$ be a coordinate,then for achosen interval,one can representthis by

$$
\begin{array} { c } { f ( t ) \simeq a _ { 0 } + a _ { 1 } t + b _ { 1 } \sin ( \nu t + \phi _ { 1 } ) + b _ { 2 } \sin ( 2 \nu t + \phi _ { 2 } ) } \\ { + b _ { 3 } t \sin ( \nu t + \phi _ { 3 } ) + b _ { 4 } t ^ { 2 } \sin ( \nu t + \phi _ { 4 } ) } \end{array}
$$

where $a _ { 0 }$ , $a _ { 1 } ; b _ { i }$ ， $i = 1 , \ldots , 4 ; \phi _ { i }$ ， $i = 1 , \ldots , 4$ are functions of the solved-for coefficients, interval size,and amount the limits of the original interval for fitting was extended. $\nu$ is the main frequency of the motion of the satellite.

Taylor(1995),and the extension of this work to other satellite systems,used the same fitting parameters,namely thelength of interval to fit overand number of coefficients solved for,asare used inthe ephemerides producedat IMCCE.ForTriton,the formas givenabove was used (i.e.,no coefficients in the fiting process were taken as zero) and the intervals for which the mixed functions were valid was 66 days.Forall satelltes,the production of a mixed function ephemeris for the time interval over which the approximation is valid,theabsolute differences from the original coordinatesareabout $0 \% 1$ orless.

# 9.5.2 Calculating Tabulated Values

# 9.5.2.1Times of Elongation and Conjunction

Thephenomena for the satelites are computed using the method described in Taylor and Sinclair (2Oo3),except for theGalilean satellites where a different scheme is used.This is due to the fact that their orbits are always seen virtually edge-on from the Earth;see $\ S 9 . 8 . 1$ .

The timesof elongationand conjunctionare tabulatedinTheAstronomical Almanactoa precision of O.1 hour.The simple method of computing these times is to start at the beginning of the required year and take a time step of O.1 hour throughout the whole year.At each step