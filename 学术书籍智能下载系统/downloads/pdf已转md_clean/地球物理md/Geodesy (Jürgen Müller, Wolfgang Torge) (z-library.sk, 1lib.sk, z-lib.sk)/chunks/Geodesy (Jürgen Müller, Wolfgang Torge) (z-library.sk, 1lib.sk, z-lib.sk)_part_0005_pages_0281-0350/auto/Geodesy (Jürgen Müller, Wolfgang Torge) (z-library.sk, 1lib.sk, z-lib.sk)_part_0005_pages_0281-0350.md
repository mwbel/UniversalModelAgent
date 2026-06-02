A fi rst-degree term in the spherical harmonic expansion would not affect the gravity anomaly, as the corresponding expansion (6.136) contains the factor $( I - 1 )$ . Hence, the ellipsoid may be positioned in the geocenter without changing the gravity fi eld: the gravimetric method yields “absolute” results.

Because of residual uncertainties in the determination of the mass and the potential, small differences between the values for the geoid and the ellipsoid may be admitted:

$$
\delta M = M - M _ { _ \mathrm { E } | | ^ { \prime } } \delta W = W _ { _ 0 } - U _ { _ 0 } .
$$

The spherical harmonic expansion of $T$ then must be extended by

$$
T _ { _ 0 } = { \frac { { G \delta M } } { R } } ,
$$

and Bruns’ formula must take $T _ { \phantom { } _ { 0 } }$ and the potential difference into account:

$$
N _ { \mathrm { 0 } } = \frac { G \delta M } { \gamma R } - \frac { \delta W } { \gamma } .
$$

For spherical approximation, the constant $N _ { \mathrm { 0 } }$ corresponds to a change in scale of the geoid.

The corresponding generalization of the spherical harmonic expansion of the gravity anomaly (6.137) provides another relation between the gravity fi eld and the “gravimetric datum”. Taking (6.101) into account, we obtain for the zero-degree term (6.19):

$$
\Delta g _ { 0 } = - \frac { T _ { 0 } } { R } + \frac { 2 } { R } \delta W = - \frac { G \delta M } { R ^ { 2 } } + \frac { 2 } { R } \delta W ,
$$

see Hofmann-Wellenhof and Moritz (2005, p. 113 ff.). If $N _ { \mathrm { o } }$ and $\Delta g _ { 0 }$ are determined by (geometric and gravimetric) measurements, (6.126) and (6.127) can be solved for $\delta M$ and $\delta W .$

The zero-degree undulation $N _ { \mathrm { o } }$ can be derived from a comparison of gravimetric geoid heights with geoid values derived from the differences of geometric heights referring either to the geoid or to the ellipsoid. The primary data sets to be used for the latter purpose are from satellite altimetry (oceans) and GPS leveling (continents), see Fig. 6.25, Jekeli (1998). The geoid height is obtained from these satellite techniques by the relation

$$
N _ { \mathrm { s a t } } = h _ { \mathrm { s a t } } - H ,
$$

![](images/4784e071dde5bcdca7594ba84e5b4d4ae5f6bbeae39e327ed4d4ca6e92634c45.jpg)  
Fig. 6.25: Gravimetric geoid and geodetic reference ellipsoid.

where $h _ { \mathrm { { s a t } } }$ stands for the ellipsoidal height of the altimeter or the GPS height, and $H$ is the height of the altimeter above the geoid (result of the altimeter measurements) or the orthometric height derived from leveling. The zero-degree term is then obtained by

$$
N _ { \mathrm { 0 } } = N _ { \mathrm { s a t } } - N _ { \mathrm { g r a v ^ { \prime } } }
$$

$N _ { \mathrm { g r a v } }$ is the geoid height from the gravimetric solution. The determination of  the other hand, is still handicapped by defi ciencies in the global gravity $\begin{array} { r } { \Delta g _ { \mathrm { 0 } } = 0 } \end{array}$ coverage. Another solution of this problem has been made possible by separating the determination of the geocentric gravitational constant GM. This quantity is known today with high accuracy from space probes and high-orbiting satellites, which allows the potential of the geoid to be determined from (6.126). Current values for the potential of the geoid and the semi-major axis of a best-fi tting ellipsoid are given in [4.3].

As we have seen, with the usual assumption of equality of mass and potential the gravimetric solution of the boundary-value problem delivers results which refer to a best-fi tting ellipsoid, where the equatorial radius (“scale”) remains unknown by $N _ { \mathrm { o } }$ . After the determination of $N _ { 0 ^ { \prime } }$ it could be used to derive the semi-major axis of the best-fi tting ellipsoid to which the gravimetric geoid heights refer (i.e. the ellipsoid is changed):

$$
a _ { \mathrm { g r a v } } = a _ { \mathrm { s a t } } + N _ { \mathrm { o } } .
$$

In practice, the adopted ellipsoid parameters are generally part of an international geodetic reference system, cf. [4.3], and consequently kept unchanged. In that case, the gravimetrically determined geoid heights have to be corrected in order to refer to the international reference ellipsoid (e.g., the GRS80 ellipsoid):

$$
N _ { \mathrm { r e f } } = N _ { \mathrm { s a t } } = N _ { \mathrm { g r a v } } + N _ { \mathrm { 0 } } .
$$

# 6.6 Global gravity fi eld modeling

Global gravity fi eld modeling is required for large-scale problems including the determination of satellite orbits, inertial navigation, and development of geophysical and geodynamic models. Especially the geoid is required for establishing a global vertical reference system and for deriving sea surface topography. Finally, global models provide the long-wavelength part of the gravity fi eld for local gravity fi eld approximation, cf. [6.7].

Global gravity models are based on spherical harmonic expansions, applicable on all kinds of residual gravity fi eld quantities [6.6.1]. The low and medium frequency part of these series expansions is derived from the analysis of satellite orbits, from satellite-tosatellite tracking and satellite gravity gradiometry [6.6.2]. High degree and order developments are achieved by combining these data with the results of terrestrial gravimetry and satellite altimetry [6.6.3].

# 6.6.1 Spherical harmonic expansion

Equations (6.3) to (6.5) provide the development of the disturbing potential $T$ into spherical harmonics. A gravity fi eld model thus is represented by the spherical harmonic coeffi cients. The functional relations between $T$ and other relevant gravity fi eld parameters, cf. [6.5.1], also allow spherical harmonic expansions for the height anomaly, the geoid height, the gravity disturbance, the gravity anomaly, and other residual gravity fi eld quantities. These expansions generally employ fully normalized spherical harmonics, cf. [3.3.2], and are valid in the Earth’s exterior space and on its surface.

By inserting (6.4) into Bruns’ theorem (6.96c), we obtain the spherical harmonic expansion for the height anomaly

$$
\zeta ( r ,                      \vartheta , \lambda ) = \frac { G M } { r \gamma } \sum _ { I = 2 } ^ { \infty } \left( \frac { a } { r } \right) ^ { I } \sum _ { m = 0 } ^ { I } ( \Delta \overline { { C } } _ { I m } \cos m \lambda + \Delta \overline { { S } } _ { I m } \sin m \lambda ) \overline { { P } } _ { I m } ( \cos \vartheta ) .
$$

Here, we have introduced the fully normalized spherical harmonics indicated by bars, cf. [3.3.2]. From (6.97b), a corresponding expansion follows for the geoid height, with $r = R$ (spherical approximation) and $\gamma = \gamma$ . By introducing (6.120) into (6.9), we may prove that simple (approximate) relation between the geoid height and the quasigeoid height (height anomaly above the ellipsoid):

$$
N ( r , \ \vartheta , \lambda ) = \zeta ( r , \ \vartheta , \lambda ) + \frac { \Delta g _ { _ B } } { \overline { { \gamma } } } H .
$$

The difference (which is also valid for the corresponding surfaces in outer space) depends on the Bouguer anomaly and on height. For the ocean surface $\left( H \approx 0 \right)$ ), this approximately leads to $N = \zeta$ .

Differentiation of (6.3) with respect to $r$ gives the spherical harmonic expansion (again in fully normalized harmonics) for the gravity disturbance (6.99):

$$
\delta g ( r , \ \vartheta , \ \lambda ) = - \frac { \partial T } { \partial r } = \frac { 1 } { r } \sum _ { I = 2 } ^ { \infty } ( I + 1 ) \Big ( \frac { a } { r } \Big ) ^ { I + 1 } T _ { I } ( \vartheta , \lambda ) .
$$

By introducing (6.5) we obtain the explicit formula

$$
\begin{array} { r l }   { \delta g ( r , \ \vartheta , \ \lambda ) = \frac { G M \sum _ { I = 2 } ^ { \infty } ( I + 1 ) ( \frac { a } { r } ) ^ { I } \sum _ { m = 0 } ^ { I } ( \Delta \overline { { C } } _ { I m } \cos m \lambda } } \\ & { \ + \Delta \overline { { S } } _ { I m } \sin m \lambda ) \ \overline { { P } } _ { I m } ( \cos \vartheta ) . } \end{array}
$$

Inserting (6.3) and (6.134a) into (6.101b) yields the expansion of the gravity anomaly

$$
\Delta g ( r , \ \vartheta , \lambda ) = \frac { 1 } { r } \sum _ { I = 2 } ^ { \infty } ( I - 1 ) \Big ( \frac { a } { r } \Big ) ^ { I + 1 } T _ { I } ( \vartheta , \lambda ) .
$$

Again substituting $T _ { \scriptscriptstyle I }$ from (6.5) gives the explicit solution

$$
\Delta g ( r , \ \vartheta , \ \lambda ) = \frac { \displaystyle { G M \sum _ { r ^ { 2 } } ( I - 1 ) \Big ( \frac { a } { r } \Big ) ^ { I } \sum _ { m = 0 } ^ { I } ( \Delta \overline { { C } } _ { I m } \cos m \lambda } } { \displaystyle { + \Delta \overline { { S } } _ { I m } \sin m \lambda ) \overline { { P } } _ { I m } ( \cos \vartheta ) . } }
$$

By comparing the abbreviated form

$$
\Delta g ( r , \ \vartheta , \ \lambda ) = \sum _ { I = 2 } ^ { \infty } \Bigl ( \frac { a } { r } \Bigr ) ^ { I + 1 } \Delta g _ { I } ( \vartheta , \lambda ) ,
$$

with (6.135a), we obtain the relation between the surface spherical-harmonics of $T$ and $\Delta g$

$$
\Delta g _ { I } ( \vartheta , \lambda ) = \frac { I - 1 } { r } T _ { I } ( \vartheta , \lambda ) .
$$

Corresponding developments for other residual gravity fi eld quantities as defl ections of the vertical or gravity gradient anomalies can be derived accordingly (e.g., Wenzel,

1985, p. 30 ff.; Wolf, 2007, p. 10 ff.). Due to the scarcity of terrestrial data of these types, these (global) expansions have been of limited relevance. This situation has changed with the availability of altimetry-derived vertical defl ections on the oceans (Watts et al., 1984), and of second-order derivatives of $T$ obtained from satellite gravity gradiometry (Rummel et al., 1993). These data sets now contribute signifi cantly to the development of high-resolution geopotential models, cf. [6.6.3], and justify a corresponding representation. Subsequently, we give some examples (spherical approximation).

The spherical harmonic expansions for the vertical defl ection components based on (6.98) read as follows:

$$
\begin{array} { l } { { \displaystyle \xi ( r , ~ \vartheta , ~ \lambda ) = \frac { G M \displaystyle \sum _ { r ^ { 2 } \gamma } ^ { \infty } ( \frac { a } { r } ) ^ { \prime } \sum _ { m = 0 } ^ { I } \bigl ( \Delta \overline { { C } } _ { l m } \cos m \lambda + \Delta \overline { { S } } _ { l m } \sin m \lambda \bigr ) \frac { d \overline { { P } } _ { l m } ( \cos \vartheta ) } { d \vartheta } , ~ ( 6 , \ldots , \ldots , M ) \displaystyle \sum _ { r ^ { 2 } \gamma \sin \vartheta } ^ { \perp } \bigl ( \frac { r } { r } \bigr ) ^ { \prime } \sum _ { m = 0 } ^ { I } \left( \frac { r } { r } \right) ^ { \prime } \sum _ { m = 0 } ^ { I } \left( \sin \lambda \overline { { C } } _ { l m } \sin m \lambda + m \Delta \overline { { S } } _ { l m } \cos m \lambda \right) \overline { { P } } _ { l m } ( \cos \vartheta ) , } } } \\ { { \displaystyle \eta ( r , ~ \vartheta , ~ \lambda ) = \frac { G M \displaystyle \sum _ { r ^ { 2 } \gamma \sin \vartheta } ^ { \infty } \sum _ { l = 2 } ^ { \infty } \bigl ( \frac { a } { r } \bigr ) ^ { I } \sum _ { m = 0 } ^ { I } \bigl ( - m \Delta \overline { { C } } _ { l m } \sin m \lambda + m \Delta \overline { { S } } _ { l m } \cos m \lambda \bigr ) \overline { { P } } _ { l m } ( \cos \vartheta ) . } } } \end{array}
$$

The second vertical derivative $T _ { _ { Z Z } } = \ T _ { _ { r r } }$ (with $Z$ outwards directed coordinate in the local level system) of the disturbing potential, being the most important component of the corresponding Eötvös tensor (3.68), is given by

$$
T _ { \pi } ( r , ~ \vartheta , ~ \lambda ) = \frac { G M } { r ^ { 3 } } \sum _ { I = 2 } ^ { \infty } ( I + 1 ) \left( I + 2 \right) \left( \frac { a } { r } \right) ^ { I } \sum _ { m = 0 } ^ { I } ( \Delta \overline { { C } } _ { I m } \mathrm { c o s } m \lambda + \Delta \overline { { S } } _ { I m } \mathrm { s i n } m \lambda ) \overline { { P } } _ { I m } ( \mathrm { c o s } \vartheta ) .
$$

Equations (6.132) to (6.138) permit the harmonic coeffi cients to be determined from “observations” (geoid heights, gravity anomalies, etc.), by least-squares adjustment, cf. [6.6.2].

The coeffi cients can also be determined by quadrature over the observations. Taking the orthogonality relations and the properties of the fully normalized harmonics into account, the inversion of (6.133) and (6.136) yields (Jekeli, 1998):

$$
{ \left\{ \Delta \overline { { C } } _ { I m } \right\} } = \frac { 1 } { 4 \pi G M } \int \int r \gamma \Bigl ( \frac { r } { a } \Bigr ) ^ { I } N \overline { { P } } _ { _ { I m } } ( \cos \Phi ) \Bigl \{ \cos { m \lambda } \atop \sin { m \lambda }  \Bigr \} d \sigma
$$

and

$$
\left\{ \Delta \overline { { C } } _ { I m } \right\} = \frac { 1 } { 4 \pi G M } \iint \frac { r ^ { 2 } } { I - 1 } \left( \frac { r } { a } \right) ^ { I } \Delta g \overline { { P } } _ { I m } ( \cos \vartheta ) \Big \{ \stackrel { \cos m \lambda } { \sin m \lambda } \Big \} d \sigma .
$$

The integration is extended over the unit sphere $\sigma .$ In contrast to least-squares adjustment, the quadrature approach only allows exploitation of one type of data for the determination of the harmonic coeffi cients.

Terrestrial gravity fi eld data sets (gravity anomalies, altimetric geoid heights) do not cover the Earth homogeneously, and they have a limited spatial resolution. Consequently, mean geoid heights and mean gravity anomalies over surface compartments are generally introduced in gravity fi eld modeling, where the surface blocks are bounded by meridians and parallels. The mean values are calculated according to

$$
\overline { { N } } = \frac { 1 } { \Delta \sigma } \underset { \Delta \sigma } { \iint } N d \sigma , \quad \Delta \overline { { g } } = \frac { 1 } { \Delta \sigma } \underset { \Delta \sigma } { \iint } \Delta g d \sigma .
$$

The block size $\Delta \sigma$ depends on the data distribution, cf. [6.6.3]. The maximum gravity ___ fi eld resolution which can be achieved is $\sqrt { \Delta \sigma }$ . This corresponds to a maximum degree of the spherical harmonic expansion $I _ { \mathrm { m a x } } = 1 8 0 ^ { \circ } /$ resolution°, cf. [3.3.3]. The introduction of mean values causes a local smoothing of the gravity fi eld, which also leads to smoothed harmonic coeffi cients. This fact has to be taken into account by damping factors (≤1), which depend on the degree and the dimension of the compartment (Katsambalos, 1979).

The truncation of the spherical harmonic expansion at $I _ { \mathrm { m a x } }$ produces an omission error due to the neglected part of the gravity fi eld. This “error” can be estimated from a degree variance model, as developed for gravity anomalies, see (6.27). Such models may be based on the covariance function of the gravity anomalies (6.25), but can also be calculated from Laplace’s surface harmonics $\Delta g _ { _ { I } } ( 6 . 2 6 )$ . In spherical approximation $r =$ $a = R )$ ), (6.138) gives

$$
\Delta g _ { I } ^ { \phantom { } } = \frac { G M } { R ^ { 2 } } ( I - 1 ) \sum _ { m = 0 } ^ { I } \bigl ( \Delta \overline { { { C } } } _ { I m } ^ { \phantom { } } \mathrm { c o s } m \lambda + \Delta \overline { { { S } } } _ { I m } ^ { \phantom { } } \mathrm { s i n } m \lambda \bigr ) \overline { { { P } } } _ { I m } ^ { \phantom { } } ( \mathrm { c o s } \vartheta ) .
$$

Inserting (6.141) into (6.26) and evaluating yields the anomaly degree variances as a function of the harmonic coeffi cients:

$$
\sigma _ { I } ^ { 2 } ( \Delta g ) = \left( \frac { G M } { R ^ { 2 } } \right) ^ { 2 } ( I - 1 ) ^ { 2 } \sum _ { m = 0 } ^ { I } \big ( \Delta \overline { { C } } _ { I m } ^ { 2 } + \Delta \overline { { S } } _ { I m } ^ { 2 } \big ) .
$$

The functional relations between the gravity fi eld parameters, cf. [6.5.1], also permit the calculation of degree variances for geoid heights, defl ections of the vertical, and higher-order derivatives (Tscherning and Rapp, 1974; Tscherning, 1976). As an example, with $\gamma = G M / r ^ { 2 } ,$ , a comparison between (6.132) and (6.136) gives the geoid degree variance

$$
\sigma _ { \scriptscriptstyle { I } } ^ { 2 } ( N ) = \left( \frac { R } { \gamma ( I - 1 ) } \right) ^ { 2 } \sigma _ { \scriptscriptstyle { I } } ^ { 2 } ( \Delta g ) .
$$

Based on the anomaly degree variance model developed by Tscherning and Rapp (1974), the omission error for geoid heights, gravity anomalies, and defl ections of the vertical can be estimated on a global scale, Fig. 6.26. For present-day satellite-only solutions (series truncation. e.g., at degree 200), this “error” amounts to about $0 . 4 {  { \mathrm { m } } } ,$ , $3 0 0 \mu \mathrm { m } \dot { \mathrm { s } } ^ { - 2 } ,$ and $4 ^ { \prime \prime }$ . A recent development to degree 2160, cf. [6.6.2], is characterized by a geoid omission “error” of only $2 \ldots 3 \mathsf { c m } _ { }$ , while the gravity anomalies and the vertical defl ections still have omission parts of about $1 0 0 \mu \mathrm { m } \bar { \mathrm { s } } ^ { - 2 }$ and $2 ^ { \prime \prime }$ . An expansion to $I = 1 0 \ 0 0 0$ (representing a spatial resolution of about $2 \ \mathrm { k m } )$ ) would reduce these errors to less than $1 \ \mathrm { m m }$ , and $1 5 ~ { \mu \mathrm { m s } } ^ { - 2 }$ and $0 . 2 ^ { \prime \prime } ,$ respectively.

An early and (at least for the lower spectral part) still useful estimate of the power spectrum of the Earth’s gravitational fi eld based on a global set of gravity anomalies was given by Kaula (1966), with $\sigma _ { _ { I } } ^ { 2 } = \sum _ { m = 0 } ^ { I } \bigl ( \Delta \overline { { C } } _ { _ { I m } } ^ { 2 } + \Delta \overline { { S } } _ { _ { I m } } ^ { 2 } \bigr ) \approx \frac { 1 6 0 \times 1 0 ^ { - 1 2 } } { I ^ { 3 } }$ and the average value per degree $\sigma ( \Delta \overline { { C } } _ { I m ^ { \prime } } \Delta \overline { { S } } _ { I m } )$ $= \sigma _ { \scriptscriptstyle { I } } / \sqrt { 2 I + 1 } \approx \pm 1 0 ^ { - 5 } / I ^ { 2 }$ . By summing up the geoid degree variances of the terms omitted at a spherical harmonic development until $I _ { \mathrm { m a x ^ { \prime } } }$ Kaula obtained $\pm 6 4 / I _ { \mathrm { m a x } } \mathrm { ~ m ~ }$ as a rough global estimate for the geoid omission error.

![](images/dfde75fe84ed765ad3eadc28b54ec1786ce6eeefb0e6b2ea4e22df549c31850e.jpg)  
Fig. 6.26: Omission error for geoid heights (height anomalies), vertical defl ections, and gravity anomalies (anomaly degree variance model Tscherning and Rapp, 1974).

# 6.6.2 “Satellite-only” gravity fi eld models

Low-degree gravity fi eld models are required for precise satellite orbit calculation, as needed for positioning, and for long-wave geoid representation necessary, e.g., for modeling sea surface topography, cf. [3.4.2]. Furthermore, these models provide an essential support for high-resolution geoid modeling, cf. [6.6.3], [6.7.1]. The models are based on satellite tracking from ground stations, on satellite-to-satellite tracking, and on satellite gravity gradiometry. These observations can be analyzed with respect to the deviations of the true orbit from a precalculated reference orbit, cf. [5.2.2], where the corresponding models include a spherical harmonic development of the gravitational potential: “Satellite-only” models. In some cases, these models have been utilized for the precise orbit determination of a specifi c satellite, by especially taking into account observations to that satellite (“tailored” models).

The basic equation for the estimation of gravity fi eld parameters from satellite observations is given by (6.33a), which connects the positions of the ground station and the satellite through the observations. With known station coordinates, the satellite orbit remains the unknown quantity, where the Keplerian orbit elements are changed with time through the “perturbing” gravitational potential (5.35); here we neglect other “disturbing” forces. As the potential is modeled by a spherical harmonic expansion, the harmonic coeffi cients enter as unknowns into the observation equations of satellite geodesy, cf. [6.2.1].

Classical gravity fi eld estimation is based on the infl uence of the gravitational fi eld on the satellite orbit, where we may distinguish between secular (linear), long-periodic (few days to months), and short-periodic (periods less than one day or one satellite revolution) perturbations (Kaula, 1966; Schneider, 1992, 1993, 1996; Seeber, 2003). After transformation of the spherical coordinates of the harmonic expansion (3.89) into the Keplerian elements, we obtain the relationship between the orbital perturbations and the harmonic coeffi cients by forming the derivatives of the perturbing potential with respect to the elements, and inserting them into (5.35).

Determination of the secular and long-periodic perturbations requires the integration over long arcs (several days). Here, short-periodic perturbations with periods of one or several revolutions are already eliminated. Furthermore, the infl uence of the tracking station coordinates becomes smaller with longer integration intervals. For the low-degree zonal coeffi cients, the integration over one satellite revolution yields the following variations for the orbital elements of main interest (Heiskanen and Moritz, 1967, p. 347 ff.):

$$
\begin{array}{c} \begin{array} { r l } & { \Delta \varOmega = - 3 \pi ( \frac { a _ { e } } { \overline { { p } } } ) ^ { 2 } \cos i J _ { 2 } + \ldots } \\ & { \Delta \omega = 6 \pi ( \frac { a _ { e } } { \overline { { p } } } ) ^ { 2 } ( 1 - \frac { 5 } { 4 } \sin ^ { 2 } i ) J _ { 2 } + \ldots } \\ & { \Delta e = - 3 \pi ( 1 - e ^ { 2 } ) ( \frac { a _ { e } } { \overline { { p } } } ) ^ { 3 } ( 1 - \frac { 5 } { 4 } \sin ^ { 2 } i ) \sin i \cos \omega J _ { 3 } + \ldots } \\ & { \Delta i = 3 \pi e ( \frac { a _ { e } } { \overline { { p } } } ) ^ { 3 } ( 1 - \frac { 5 } { 4 } \sin ^ { 2 } i ) \cos i \cos \omega J _ { 3 } + \ldots } \end{array} ) ,  \end{array}
$$

with $\overline { { { p } } } = a ^ { \left( 1 \mathrm { ~ - ~ } e ^ { 2 } \right) }$ and $a _ { e }$ semi-major axis of the Earth ellipsoid.

$J _ { 2 }$ and higher even-zonal-coeffi cients cause secular perturbations in $\varOmega$ and $\omega .$ For $i < 9 0 ^ { \circ } ,$ $\varOmega$ decreases in time (westward regression of the nodal line). The change in $\omega$ corresponds to a rotation of the orbital ellipse in the orbital plane (Fig. 5.5). This rotation produces longperiodic perturbations in the quantities $e$ and $i ,$ as they depend on $\omega .$ The even zonals thus can be determined primarily from the perturbations in $\varOmega$ and $\omega ,$ while the odd zonals are obtained from $\boldsymbol { j }$ and e. If the perturbations are added to the orbital elements of the initial epoch, one obtains the orbital elements at a specifi c epoch as a function of the zonal harmonics. As mentioned earlier, the coeffi cients depend particularly on the inclination but also on the semi-major axis and the eccentricity.

The tesseral harmonics are responsible for small-amplitude (a few $1 0 0 \mathrm { ~ m } )$ shortperiodic perturbations, especially in the elements $i , \ \varOmega ,$ w. They can be determined from dense observation sequences over short arcs. Several tesseral terms of higher degree and order can be also determined by resonance effects, arising after days to weeks. These effects occur if the ratio of the mean angular velocity of the satellite to the rotational velocity of the Earth is an integer number, which produces an enhancement of perturbation in a repeat orbit.

In order to resolve the gravitational fi eld to a certain degree, satellites in different altitudes and with different inclinations are required at this classical strategy, in addition to a good global distribution of the tracking stations and a suffi ciently long observation time. The attenuation of the gravity fi eld with height and the decrease of the harmonic coeffi cients at higher degrees, together with defi ciencies in the geometry of the satellite orbits and the ground stations, limits the resolution of “satellite-only” models based only on ground-based measurements. Using several decades of tracking data, a certain limit at gravitational fi eld modeling was reached around the year 2000, with spherical harmonic expansions until degree and order 70 to 90, where the relative uncertainty of the coeffi cients reached around $1 0 0 \%$ already at degree 30 to 40.

Dedicated satellite gravity fi eld missions with low Earth orbiters (some $1 0 0 ~ \mathrm { k m }$ altitude) and “in-situ” sensors (satellite-to-satellite tracking, gravity gradiometry) have led to a signifi cant change of this classical strategy, cf. [5.2.8], Rummel (1979), Reigber et al. (2005). Range, range rate and gradient measurements now enter into the corresponding observation equations for the determination of higher degree and order spherical harmonic coeffi cients, and tracking data from Earth or from other satellites mainly serve for improving the long-wave part of the gravitational fi eld. Corresponding models have been calculated until degree and order 200 and higher, and agree well until degree and order 120 to 150 (Förste et al., 2009).

While limitations in computational facilities previously forced zonal, tesseral and resonant terms to be computed separately, the harmonic coeffi cients can now be rigorously determined from all available observations by a least-squares adjustment (for instance by adding the normal equations of different data sets evaluated separately). With present knowledge of the tracking station coordinates, the satellites’ orbits, the Earth’s rotation parameters, as well as the tidal effects, the corresponding parameters generally can be introduced as known quantities into the adjustment, and variations of the low-degree coeffi cients with time may be included (Reigber, 1989; Bouman, 1997). Weighting of different data sets and modeling of systematic effects still poses a special problem for these complex adjustments (this is also valid for the “combined” models to be discussed in [6.6.3]). As the accuracy estimates generally are too optimistic, the calculated standard deviations are often “scaled”, i.e., enlarged (Lerch et al., 1991).

With respect to the accuracy of gravity models (this is valid for any kind of mathematical representation and also for the “combined” solutions!) we have to distinguish between the commission and the omission error. The commission error stems from the errors of the data which propagate through the modeling process (e.g., a least-squares adjustment) into the results. The limited spatial resolution of the data and the model derived from them, on the other hand, results in an omission error which can be estimated by corresponding models, cf. [6.6.1]. The accuracy (commission error) achieved at the most recent gravity fi eld models (degree and order 200 and higher) is about 0.1 to $_ { 0 . 2 \mathrm { ~ m ~ } }$ (geoid) and 20 to $3 0 ~ { \mu \mathrm { m } } { \varsigma } ^ { - 2 }$ (gravity anomalies), and an accuracy increase to $2 \mathrm { \ c m }$ resp. $1 0 \mu \mathrm { m } s ^ { - 2 }$ or better is expected as result of the complete GOCE mission (e.g., Ihde et al., 2010).

The fi rst gravity fi eld information from space came from Sputnik I (1957), with the dynamic form factor $J _ { 2 }$ (polar fl attening); and from Vanguard I (1958), with the coeffi cient $J _ { 3 }$ (unequal fl attening at the north and south pole), O’Keefe et al. (1959). The Smithsonian Astrophysical Observatory (SAO) Standard Earth I provided a model complete to degree and order 8 (Lundquist and Veis, 1966). At the end of the twentieth century, ground-based “satellite-only” models employed several million records of tracking data. Laser distance and microwave range and range-rate measurements formed the bulk of the data, but optical directions also were included and assisted in stabilizing the solutions. Finally, observations to more than 30 satellites were generally used, with altitudes varying between 800 and $2 0 ~ 0 0 0 ~ \mathrm { k m }$ and inclinations between $4 0 ^ { \circ }$ and $1 1 0 ^ { \circ }$ . Among the last solutions of this type we have the NASA Goddard Space Flight Center (GSFC) Earth model GEM T3 (Lerch et al., 1994), the joint (GSFC, University of Texas, Ohio State University, CNES France) gravity model JGM-2S, complete to degree and order 70 (Nerem et al., 1994), and the JGM-3 model (70,70, including DORIS and GPS tracking, Tapley et al., 1996), which was developed primarily for the TOPEX/POSEIDON mission, as well as the GRIM5-S1 (99,95) model (Geoforschungszentrum Potsdam and Groupe de Recherches de Géodésie Spatiale, Toulouse, Gruber et al., 2000).

Among the “satellite-only” gravity models derived during the past ten years from “in situ” (satellite-to-satellite tracking and gravity gradiometry) and tracking data, we have the GRACEbased solutions ITG-GRACE (180,180; Institut für Geodäsie und Geoinformation, Universität Bonn, Mayer-Gürr et al. 2010), GGM (180,180; Center for Space Research, University of Texas, Tapley et al., 2007), JEM01-RL03B (120,120; NASA/JPL, Pasadena), EIGEN – European Improved Gravity model of the Earth by New techniques – (150,150; GRACE and LAGEOS data, GRGS Toulouse and GFZ Potsdam, Reigber et al., 2005; Förste et al., 2008; Flechtner et al., 2010b). Large-scale gravity fi eld variations with time have been found from monthly and weekly GRACE solutions, developed until degree 120 resp. 30 (Cheng and Tapley, 2004), cf. [8.3.5]. The evaluation of the fi rst months of GOCE gravity gradiometry and tracking data led to GOCE-only models up to degree and order 240 (Pail et al., 2011), and to combined solutions with GRACE data, where GRACE dominates until degree and order 100, and GOCE signifi cantly contributes from about 150,150 (Pail et al., 2010b), cf. [5.2.8].

# 6.6.3 Combined (high resolution) gravity fi eld models

“Satellite-only” models can be improved (with respect to spatial resolution and accuracy) by combining them with satellite altimetry and surface gravity (Rapp, 1998). These data are generally available as mean values for compartments (blocks) formed by the grid of geographical coordinates, and ranging, e.g., from $5 ^ { \prime } \times 5 ^ { \prime }$ to $1 ^ { \circ } \times 1 ^ { \circ }$ dimensions. Again, the spherical harmonic expansion is employed for modeling, where degree and order of the development now depend on the spatial resolution of the altimetric and gravimetric data. A combination solution thus contains the following “observations”: the harmonic coeffi cients of a “satellite-only” model with the full error covariance matrix, mean free-air anomalies from terrestrial gravimetry on land and sea, and mean geoid heights derived from satellite altimetry, both with an appropriate error model. The corresponding observation equations (i.e., the relation of gravity anomalies and geoid heights to the spherical harmonic coeffi cients) are given by (6.136) and (6.133), where the reduction of sea surface topography from the altimeter measurements is presupposed. Some solutions also use gravity anomalies instead of altimetric geoid heights, with a transformation based either on an integral formula, cf. [6.7.1], or on least-squares collocation, cf. [6.8].

Point free-air gravity anomalies (or mean gravity anomalies for some countries) are collected and kept at a few global gravity data bases (U.S. National Geospatial-Intelligence Agency (NGA), Bureau Gravimetrique International, Toulouse, France), see Fig. 6.27. The accuracy of point anomalies derived from land, sea and airborne gravimetry varies between 5 and $5 0 \mu \mathrm { m } \mathrm { s } ^ { - 2 } ,$ , cf. [5.4.4]. In order to avoid long-wave systematic errors in gravity fi eld modeling, the anomalies have to refer to the same gravity (IGSN71), horizontal (ITRF, GRS80) and vertical reference systems, where the global vertical datum poses a special problem, cf. [3.4.3], Heck (1990). Mean anomalies can be derived, e.g., by least-squares prediction, where Bouguer anomalies may be used as intermediate gravity fi eld quantities, cf. [6.5.3]. On the continents, mean gravity anomalies are now available for most regions, but with different spatial resolution (from $1 ^ { \prime } \times 1 ^ { \prime }$ to $3 0 ^ { \prime } \times 3 0 ^ { \prime }$ ) and accuracy (varying between about 20 and $2 0 0 ~ { \mu \mathrm { m s } } ^ { - 2 }$ ). Larger gaps still exist in parts of South America, Africa, Asia and especially in Antarctica, and will be fi lled by airborne gravimetry, cf. [5.4.4]. The oceans, on the other hand, are only sparely covered by sea gravimetry tracks of rather heterogeneous accuracy, and this situation will in future change only slowly, see [4.4] and Fig. 6.27, Kenyon (1998). As a consequence, high-resolution gravity fi eld data for the oceans are now generally derived from satellite altimetry, which covers the oceans more homogeneously (see below).

![](images/78f32e03c6114d17c4e2f89e52cb422268f6374a6b6acd369aa4d35c4f8ff583.jpg)  
Fig. 6.27: Global distribution of terrestrial gravity data, courtesy S. Bonvalot, Bureau Gravimétrique International.

More than three decades of satellite altimetry have provided a large amount of distance measurements between the altimeter satellites and the sea surface, cf. [5.2.7]. With proper reduction of sea surface topography (oceanographic model), accurate orbit determination (tracking), altimeter calibration and adjustment of the track crossover discrepancies, mean altimetric geoid heights have been derived for the ocean areas. Data sets of high accuracy and resolution (e.g. $2 ^ { \prime } \times 2 ^ { \prime }$ or $5 ^ { \prime } \times 5 ^ { \prime }$ ) are available especially from the GEOSAT and ERS-1 geodetic missions (Sandwell and Smith, 2009), which cover the oceans between $\pm 7 2 ^ { \circ }$ and $8 2 ^ { \circ }$ latitude, respectively, with an equatorial track spacing of 4 and $8 ~ \mathrm { k m }$ . After reducing the dynamic ocean topography from the altimetric ground data, along-track differentiation provides defl ections of the vertical. Double differentiation delivers gravity gradients, which can be used for the evaluation of the GOCE mission results, cf. [5.2.8]. Mean altimetric gravity anomalies can be calculated by inversion from the mean geoid heights, cf. [6.7.1]. Recent solutions exploit retracked satellite altimetry and the results of more recent altimetry missions, and provides the global marine gravity fi eld with $1 ^ { \prime } \times 1 ^ { \prime }$ spatial resolution and an average accuracy of 20 to $5 0 ~ \mu \mathrm { m } \mathrm { s } ^ { - 2 }$ (Andersen et al., 2010).

By combining the mean anomalies from surface gravimetry and altimetry, only a few percent of the Earth’s surface remain uncovered. These gaps can be fi lled either by isostatic anomalies calculated from a topographic-isostatic model (Pavlis and Rapp, 1990), or just bridged by the satellite-only model.

High-degree geopotential models are calculated either by least-squares adjustment or by quadrature methods (Rapp, 1998).

A least-squares adjustment, in principle, would utilize all available data in order to determine the full set of potential coeffi cients (130 321 coeffi cients at $I , m = 3 6 0 , 3 6 0 ;$ ： 3.67 million coeffi cients at 2160,2160), together with the error variance/covariance matrix. As computational limitations still prevent a rigorous adjustment of these quantities, alternative solutions have been developed. At these strategies, for instance, a complete data coverage on a grid and homogeneous and uncorrelated errors are presupposed for the high-resolution data sets. Special arrangements of the normal equation matrix (block-diagonal technique) then allow an effi cient computation by iterative procedures (Wenzel, 1985; Pavlis et al., 1996). Subsequently, the normal equations of these data sets are added to the normal equations of the satellite-only model.

The quadrature approach employs the integration over the gravity anomalies according to (6.139b). As a global and homogeneous data set is required at this strategy, altimetric geoid heights have to be transformed into gravity anomalies (see above) and data gaps have to be fi lled by interpolation or model values. After the calculation of the harmonic coeffi cients from the gravity anomalies, they are again combined by adjustment with the coeffi cients of a satellite-only gravity model (e.g., Rapp and Pavlis, 1990).

Early spherical harmonic expansions based on terrestrial gravity data are due to Jeffreys (1941–1943), Zhongolovich (1952), and Uotila (1962). Sparse data coverage limited these expansions to the low-degree harmonics. Kaula (1959) introduced a constraint from satellite orbit analysis in order to develop a 8,8 geoid model. Among the geopotential models, developed before the advent of dedicated gravity fi eld satellite missions are the Ohio State University (OSU) model OSU91 (combination of the satellite-only GEM-T2 (36,36) model with $1 ^ { \circ } \times 1 ^ { \circ }$ and $3 0 ^ { \circ } \times 3 0 ^ { \circ }$ gravity anomalies from surface gravimetry and altimetry, quadrature method, Rapp et al., 1991), and the Geoforschungszentrum Potsdam (GFZ) model GFZ96 (combination of the GRIM-4 (60,60/ 72,72) models with terrestrial anomalies and ERS-1 geoid heights, least-squares iteration, Gruber et al., 1997), both complete to degree and order 360. A 1800,1800 model GPM98 was developed by Wenzel (1999) by combining EGM96 with $5 ^ { \prime } \times 5 ^ { \prime }$ mean gravity anomalies available for about $7 5 \%$ of the Earth’s surface. The inclusion of GRACE and also GOCE data signifi cantly improves the quality of combined gravitational models. We mention the GGM02C (200, 200) model (Tapley et al., 2005) as a combination of a GRACE-only model with EGM96 (see below), and the EIGEN-5C (360, 360) model, as a combination of the satellite-only model EIGEN-5S with $0 . 5 ^ { \circ } \times 0 . 5 ^ { \circ }$ gravimetry and altimetry surface data (Förste et al., 2008). The EIGEN-6C (1420,1420) model combines LAGEOS-, GRACE- and GOCE-data (EIGEN-6S, 240,240) and gravity anomalies from altimetry (oceans) and the EGM2008 model (land), the solution includes time variable (drift, annual and semiannual) spherical harmonic coeffi cients up to degree and order 50 (Förste et al., 2011).

Tab. 6.1 presents the low degree and order harmonic coeffi cients and a selection of higher degree values as derived from the recent combination solution EGM2008 (see below). The anomaly degree variances approximately follow Kaula’s rule, with relative errors reaching about $5 0 \%$ around degree 700, and $1 0 0 \%$ around degree 1800 (Arabelos and Tscherning, 2010).

Extended sets of satellite tracking data, terrestrial gravity anomalies and ocean-wide satellite altimetry have been utilized in the NASA/GSFC and NIMA joint geopotential (360,360) model EGM96 (Lemoine et al., 1998). Up to degree and order 359, the model parameters have been derived from a block-diagonal least-squares adjustment, and the degree 360 coeffi cients were calculated by quadrature. Geoid accuracy estimates are between $_ { 0 . 5 \mathrm { ~ m ~ } }$ for the oceans and $1 \textrm { m }$ for land areas. The NGA (U.S.A. National Geospatial-Intelligence Agency) Earth Gravitational Model EGM2008 (Pavlis et al., 2008) is based upon the ITG-GRACE03S gravitational model (180,180) and a global gravity anomaly database of $5 ^ { \prime } \times 5 ^ { \prime }$ resolution. The anomalies have been derived from terrestrial gravity measurements on land $1 6 \%$ still not covered with high quality data) and satellite altimetry on the oceans, where a dynamic ocean topography model (degree and order 180) is also provided. EGM2008 is complete to degree and order 2159 (spherical harmonic coeffi cients given for the “zerotide” and the “tide-free” system, cf. [3.4.1]), which corresponds to a $5 ^ { \prime }$ spatial resolution. The “scaling” parameters have the numerical values $G M = 3 9 8 ~ 6 0 0 . 4 4 1 5 \times 1 0 ^ { 9 } ~ \mathsf { m } ^ { 3 } \mathsf { s } ^ { - 2 }$ and $a = 6 \ 3 7 8 \ 1 \ : 3 6 . 3 \ \mathrm { m } ,$ , and a version related to WGS84 is also available, cf. [5.2.5]. The quality of the $5 ^ { \prime } \times 5 ^ { \prime }$ geoid solution has been estimated by error propagation and by independent comparisons (GPS/leveling, astronomic defl ections of the vertical), Förste et al. (2009). The accuracy obtained varies especially between land and ocean areas and amounts to about $0 . 1 \textrm { m }$ (geoid) resp. $1 ^ { \prime \prime } . . . 2 ^ { \prime \prime }$ (defl ection of the vertical) for the continents, and $0 . 0 6 \mathrm { ~ m ~ }$ resp. $0 . 4 ^ { \prime \prime }$ for the oceans. The omission error for the geoid is a few cm globally, but may reach up to $0 . 1 \textrm { m }$ in mountainous areas (Jekeli et al., 2009).

Tab. 6.1. Samples of fully normalized spherical harmonic coeffi cients $( \times 1 0 ^ { 6 } )$ , EGM2008 Global Gravitational Model (Pavlis et al., 2008)   

<table><tr><td>1</td><td>m</td><td>Cm</td><td>Sm</td></tr><tr><td>2</td><td>0</td><td>-484.169 317</td><td></td></tr><tr><td>2</td><td>1</td><td>-0.000 207</td><td>0.001 384</td></tr><tr><td>2</td><td>2</td><td>2.439 384</td><td>-1.400 274</td></tr><tr><td>3</td><td>0</td><td>0.957 161</td><td></td></tr><tr><td>3</td><td>1</td><td>2.030 462</td><td>0.248 200</td></tr><tr><td>3</td><td>2</td><td>0.904 788</td><td>-0.619 005</td></tr><tr><td>3</td><td>3</td><td>0.721 322</td><td>1.414 349</td></tr><tr><td>4</td><td>0</td><td>0.539 966</td><td></td></tr><tr><td>4</td><td>1</td><td>-0.536157</td><td>-0.473 567</td></tr><tr><td>4</td><td>2</td><td>0.350 502</td><td>0.662 480</td></tr><tr><td>4</td><td>3</td><td>0.990 857</td><td>-0.200 957</td></tr><tr><td>4</td><td>4</td><td>-0.188 520</td><td>0.308 804</td></tr><tr><td>10</td><td>0</td><td>0.053330</td><td></td></tr><tr><td>20</td><td>0</td><td>0.021 559</td><td></td></tr><tr><td>50</td><td>0</td><td>-0.004 844</td><td></td></tr><tr><td>100</td><td>0</td><td>0.002 355</td><td></td></tr><tr><td>200</td><td>0</td><td>-0.000 161</td><td></td></tr><tr><td>500</td><td>0</td><td>-0.000 029</td><td></td></tr><tr><td>1000</td><td>0</td><td>-0.000 007</td><td></td></tr><tr><td>1500</td><td>0</td><td>0.000 001</td><td></td></tr><tr><td>2000</td><td>0</td><td>0.000 001</td><td></td></tr></table>

The long-wave structures of the free-air anomalies and the geoid, as derived from a recent geopotential model, are shown in Figs. 6.28 and 6.29. The free-air anomalies vary rather irregularly about zero, but a correlation with extended mountain chains (Cordilleras, Himalaya) can be recognized. The principal features of the geoid include the maxima near New Guinea $( + 8 0 ~ \mathrm { m } )$ , in the North Atlantic, the southwestern Indian Ocean, and in the Andes, as well as the minima at Sri Lanka $( - 1 0 5 \mathrm { ~ m } )$ ), in Antarctica, to the west of California, and near Puerto Rico.

![](images/aed6c4170a5200e4fd3ca7c481d25f9351170824d9546a263585cf4af6e68b3a.jpg)  
Fig. 6.28: EGM2008 gravity anomalies (Pavlis et al., 2008), (http://Earth-info.nga.mil/GandG/ wgs84/gravitymod/egm2008/ ).

![](images/33fc74524b389e5945d7cd29cadd31b7b5377005d1cad7a5899729f61004ae18.jpg)  
Fig. 6.29: EGM2008 geoid heights, contour line interval $1 0 \mathrm { m }$ (Pavlis et al., 2008), (http://Earthinfo.nga.mil/GandG/wgs84/gravitymod/egm2008/ ).

# 6.7 Local gravity fi eld modeling

Local gravity fi eld modeling is especially useful for the determination of geoid/quasigeoid heights or defl ections of the vertical, with high accuracy and spatial resolution, as for instance needed for the reduction of GPS heights, cf. [6.4.3]. This strategy presupposes the availability of high resolution gravity fi eld data in and around the area concerned. The spherical harmonic development of the gravity fi eld, described in [6.6], was and is (not yet) capable of delivering such a local solution. Integral formulas, on the other hand, allow a pointwise calculation of gravity fi eld quantities for the area under investigation, and thus provide the possibility of an arbitrarily high gravity fi eld resolution which depends only on data coverage and quality (Sansò and Rummel, 1997).

Utilizing gravity anomalies as the primary data set, classical solutions aim at the determination of geoid heights and defl ections of the vertical [6.7.1]. Reduction to the geoid is avoided in the calculation of the corresponding surface quantities, where the quasigeoid plays a special role [6.7.2]. Once the gravity fi eld is known on the geoid or on the physical surface of the Earth, upward continuation provides gravity fi eld quantities in space [6.7.3]. Astronomically determined defl ections of the vertical furnish differences of geoid or quasigeoid heights and may locally support or substitute gravimetric solutions [6.7.4].

An alternative approach to the integral formulas is least-squares collocation which will be discussed in [6.8].

# 6.7.1 Gravimetric geoid heights and defl ections of the vertical: integral formulas

The series expansion (6.4) for the disturbing potential $T$ can also be represented by a surface integral. By inserting (6.138) into (6.3), this expansion reads

$$
T ( r , \ \vartheta , \ \lambda ) = \sum _ { I = 2 } ^ { \infty } \frac { r } { I - 1 } \left( \frac { a } { r } \right) ^ { I + 1 } \Delta g _ { I } ^ { \ } ( \vartheta , \lambda ) .
$$

As known from potential theory, the surface spherical harmonics $\Delta g _ { I }$ can be derived by inversion of (6.137), as a surface integral of the gravity anomalies over the unit sphere $\sigma$ :

$$
\Delta g _ { I } = \frac { 2 I + 1 } { 4 \pi } \int \limits _ { \sigma } \int \limits _ { \sigma } \Delta g P _ { I } \left( \cos \psi \right) d \sigma ,
$$

where $P _ { \mathrm { \ell } } ( \cos \psi )$ are the Legendre polynomials. Inserting into (6.145) yields the disturbing potential on the geoid in spherical approximation $r = R = a .$ )

$$
T ( \vartheta , \lambda ) = \frac { R } { 4 \pi } \int \int S ( \psi ) \Delta g d \sigma ,
$$

where the integral kernel (Stokes’ function)

$$
S ( \psi ) = \sum _ { I = 2 } ^ { \infty } \frac { 2 I + 1 } { I - 1 } P _ { _ I } ( \cos \psi )
$$

can be expressed in closed form:

$$
S ( \psi ) = \frac { 1 } { \sin \frac { \psi } { 2 } } + 1 - 5 \cos \psi - 6 \sin \frac { \psi } { 2 } - 3 \cos \psi | \mathrm { n } \left( \mathrm { s i n } \frac { \psi } { 2 } + \mathrm { s i n } ^ { 2 } \frac { \psi } { 2 } \right) .
$$

This integral formula has been derived by Stokes (1849); it is called Stokes’ formula.

By inserting (6.147) into Bruns’ theorem (6.97b), we obtain the geoid height

$$
N = \frac { R } { 4 \pi \gamma _ { m } } \iiint _ { \sigma } S ( \psi ) \ \Delta g d \sigma ,
$$

wherea solut $\gamma _ { { } _ { m } }$ is a mean gravity value over the Earth. Stokes’ formula can also be derived as n of the integral equation (6.93), if applied to the geoid. If a geoid accuracy of the cm-order of magnitude is required, ellipsoidal corrections have to be applied to (6.149), Sünkel (1997). We also remember the conditions of mass and potential equality between the geoid and the reference ellipsoid, inherent in Stokes’ formula, cf. (6.126).

Stokes’ function $S ( \psi )$ acts as a weighting function on the gravity anomalies. It depends on the spherical distance $\psi$ between the point of computation and the surface element $d \sigma$ with the gravity anomaly Δg. $S ( \psi )$ decreases with $\psi$ until a fi rst zero value at $\psi = 3 9 ^ { \circ } ,$ , and then oscillates with large values and another zero value at $1 1 7 ^ { \circ }$ until $\psi = 1 8 0 ^ { \circ }$ (Fig. 6.30). The neighborhood of the computation point requires particular attention, as $S ( \psi )$ becomes infi nite at $\psi = 0 ^ { \circ }$ . The contribution of the innermost zone around the point of computation can be estimated in planar approximation (e.g., with a radius $s _ { i } = 5 ~ \mathrm { k m } )$ , by expanding $\Delta g$ in a Taylor series and performing integration term by term. To a fi rst approximation, the effect of the inner zone on the geoid height depends on the gravity anomaly in the computation point:

$$
N _ { _ i } = \frac { S _ { i } } { \gamma _ { _ m } } \Delta g _ { _ P } + \ldots .
$$

The components of the defl ection of the vertical are obtained by differentiating the disturbing potential $T$ in north-south and east-west direction (6.98). This can be realized by expressing $\psi$ in (6.147) in spherical coordinates of the computation point and the source point, the corresponding formulas of spherical trigonometry are taken from the spherical polar triangle, see Fig. 2.14. After differentiation with respect to latitude and longitude and subsequent resubstitution of $\psi$ we obtain

$$
\left\{ \begin{array} { l } { \displaystyle \xi } \\  \displaystyle \eta \right\} _ { \mathrm { 0 } } = \frac { 1 } { 4 \pi \gamma _ { m } } \iint \frac { d S ( \psi ) } { d \psi } \Delta g \Bigl \{ \cos \alpha \Bigr \} d \sigma , \end{array}
$$

![](images/a2af2365a841d73c6cf85be05cead9729849528b6c67ab71b1b4a2682d8903f2.jpg)  
Fig. 6.30: Original and modifi ed Stokes’ function, modifi cation according to (6.163).

where $\alpha$ is the azimuth of the great circle from the computation point to the source point. Equation (6.151) was derived by Vening-Meinesz (1928). The Vening-Meinesz function

$$
\begin{array} { l } { \displaystyle \frac { d S } { d \psi } = - \frac { \cos \left( \frac { \psi } { 2 } \right) } { 2 \sin ^ { 2 } \left( \frac { \psi } { 2 } \right) } + 8 \sin \psi - 6 \cos \left( \frac { \psi } { 2 } \right) - 3 \frac { 1 - \sin \left( \frac { \psi } { 2 } \right) } { \sin \psi } } \\ { \displaystyle \qquad + ~ 3 \sin \psi \ln \left[ \sin \left( \frac { \psi } { 2 } \right) + \sin ^ { 2 } \left( \frac { \psi } { 2 } \right) \right] . } \end{array}
$$

is infi nite at $\psi = 0 ^ { \circ }$ and then decreases rapidly, attaining only small values after $\psi = 5 0 ^ { \circ }$ to $6 0 ^ { \circ }$ (Fig. 6.31). The contribution of the innermost zone depends primarily on the horizontal gradient of the gravity anomalies:

$$
\left\{ \begin{array} { l } { \boldsymbol { \xi } } \\ { \boldsymbol { \eta } } \end{array} \right\} _ { i } = - \frac { \mathsf { s _ { i } } } { 2 \gamma _ { \mathrm { m } } } \left\{ \begin{array} { l } { \partial ( \Delta g ) / \partial x } \\ { \partial ( \Delta g ) / \partial \gamma } \end{array} \right\} _ { P } + \\ldots .
$$

Stokes’ and Vening-Meinesz’ formulas allow a pointwise calculation of the geoid height and the defl ection of the vertical, by integrating the gravity anomalies given on the surface of the geoid, cf. [6.5.3]. The properties of Stokes’ function require high resolution gravity data all over the Earth, while the effect of remote zones is small in the calculation of vertical defl ections and can be estimated by low-degree global gravity fi eld models. The inner zone may contribute some cm to the geoid height, this is well accounted for at gravity station distances of 1 to $5 ~ \mathrm { k m } ,$ , depending mainly on the roughness of topography. The effect of the inner zone on the defl ection of the vertical can reach several arcsec, especially in the mountains. A dense gravity survey and/or the calculation of the effect of topography is needed in order to achieve an accuracy better than 1 arcsec.

In practice, the integrals (6.149) and (6.151) are solved by a summation of fi nite surface elements. For this purpose, either a set of gridded point anomalies is formed from the observed data, using e.g., least-squares prediction or spline interpolation, or mean values over surface blocks delineated by meridians and parallels are calculated, cf. [6.6.3]. The latter case also requires the integration of the Stokes’ or Vening-Meinesz’ function over the block. After gridding, a very effi cient solution is obtained in the spectral domain using Fast Fourier Transform (FFT) techniques. The convolution required in (6.149) and (6.151) then becomes a simple multiplication, and the results are easily retransformed to the space domain by the inverse FFT (Schwarz et al., 1990; Haagmans et al., 1993).

![](images/2b2c4554106a68aa05cfec5e6c32f74762a140553103b4359a35393edda36da7.jpg)  
Fig. 6.31: Vening-Meinesz function.

As discussed in [6.6.3], satellite altimetry provides a high resolution data set of geoid heights for the oceans, which now signifi cantly contributes to gravity fi eld modeling. Computation strategies either directly use the altimetrically derived geoid heights or transform them into gravity anomalies. The transformation procedure is based on least-squares collocation, cf. [6.8.2], or on a surface integral over the geoid heights.

The surface integral for calculating gravity anomalies from geoid heights respectively from the disturbing potential is obtained by the inversion of Stokes’ formula (6.149). Here we remember again that we restrict these developments to the boundary case of the Earth’s surface, with a spherical approximation $\left( r = R \right) $ ; the extension to space will be discussed in [6.7.3]. We start from the spherical harmonic expansion of (6.137) and the relation between the surface spherical harmonics of $\Delta g$ and $T ( 6 . 1 3 8 )$ , and take the surface integral for the calculation of surface spherical harmonics into account:

$$
T _ { \scriptscriptstyle I } = { \frac { 2 I + 1 } { 4 \pi } } \int \int _ { \sigma } T ( \vartheta , \lambda ) { \cal P } _ { \scriptscriptstyle I } ( \cos \psi ) d \sigma
$$

(see the corresponding equation (6.146) for gravity anomalies). We thus obtain a fi rst version of the inverse Stokes’ formula (Molodenskii et al., 1962, p. 50):

$$
\Delta g ( \vartheta , \lambda ) = \frac { 1 } { 4 \pi R } \int \displaylimits _ { \sigma } ^ { } \int \displaylimits _ { \sigma } ^ { } ( \vartheta ) T ( \vartheta ^ { \prime } , \lambda ^ { \prime } ) d \sigma ,
$$

with the (only distance dependent) kernel function:

$$
\hat { Z } ( \psi ) = \sum _ { I = 0 } ^ { \infty } ( I - 1 ) \left( 2 I + 1 \right) P _ { I } ( \cos \psi ) .
$$

For numerical calculations (6.155) generally is transformed into (Jekeli, 2009, p. 25 ff.):

$$
\Delta g ( \vartheta , \lambda ) = - \frac { T ( \vartheta , \lambda ) } { R } + \frac { 1 } { 4 \pi R } \iint _ { \sigma } \left( T ( \vartheta ^ { \prime } , \lambda ^ { \prime } ) - T ( \vartheta , \lambda ) \right) Z ( \psi ) d \sigma .
$$

The inverse Stokes’ function now can be expressed also in a simple closed form:

$$
Z ( \psi ) = \sum _ { I = 1 } ^ { \infty } I \left( 2 I + 1 \right) P _ { I } ( \cos \psi ) = - \frac { 1 } { 4 \sin ^ { 3 } \frac { \psi } { 2 } } .
$$

The effect of the inner zone again has to be considered separately. It depends on the vertical gradient of the gravity anomaly (Lelgemann, 1976):

$$
\Delta g _ { i } = \frac { s _ { i } } { 4 } \Bigg \lvert \frac { \partial ( \Delta g ) } { \partial r } \Bigg \rvert _ { P } ,
$$

where $S _ { j }$ is the radius of the inner zone. Due to the properties of the integral kernel, the infl uence of the more remote zones on $\Delta \mathrm { g }$ decreases rapidly. Hence, in contrast to Stokes’s integral, the integration of the inverse Stokes’ integral can be restricted to a radius of a few degrees.

Satellite-based positioning (GNSS), provides ellipsoidal heights for points on the Earth’s surface in a continuously increasing manner. This allows to calculate the gravity disturbance $\delta g$ as an “observed” residual gravity fi eld quantity, cf. [6.1.2], and to solve the gravimetric boundary value problem on a geometrically known boundary surface, cf. [6.5.1], (Hotine, 1969, p. 317 ff.; Koch and Pope, 1972). Exploiting the small difference between $\Delta g$ and $\delta { \boldsymbol { g } } ,$ see (6.134), (6.135), we obtain Hotine’s formula for the calculation of geoid heights from gravity disturbances (Hofmann-Wellenhof and Moritz, 2005, p. 115 ff.):

$$
N = \frac { R } { 4 \pi \gamma _ { m } } \iint _ { \sigma } H ( \psi ) \delta g d \sigma
$$

with the Hotine function

$$
H ( \psi ) = \sum _ { I = 0 } ^ { \infty } \frac { 2 I + 1 } { I + 1 } P _ { I } \left( \cos \psi \right) = \frac { 1 } { \sin \frac { \psi } { 2 } } - \ln \left( 1 + \frac { 1 } { \sin \frac { \psi } { 2 } } \right) .
$$

In the future, a corresponding strategy may obtain greater relevance for gravity fi eld modeling.

Purely gravimetric or gravimetric/altimetric calculations of geoid heights and defl ections of the vertical suffer from the data gaps at the polar caps, in some continental areas, and at coastal zones. They are also hampered by long-wave systematic data errors and by inhomogeneous spatial resolution and accuracy of the gravity data. As global geopotential models today provide the long-wave part of the gravity fi eld with high accuracy, cf. [6.6.3], and gravity anomalies with station distances down to 1 to $5 \mathrm { k m }$ are available in many regions, combined solutions based on integral formulas have been developed for local solutions covering the area well surveyed by terrestrial gravimetry. In addition, data smoothing techniques are employed on the gravity anomalies, considering the gravimetric terrain effect which can be calculated from digital terrain models, cf. [6.5.2].

Combination solutions apply the remove-restore technique (Forsberg and Tscherning, 1981; Denker et al., 1986), which includes the following steps:

• Reduction of the gravity anomalies $\Delta g$ by the anomaly part of the global model $\Delta g _ { { \scriptscriptstyle M } } ^ { { \mathrm { ~ ~ } } }$ (long wavelengths). Smoothing of the anomalies by some kind of terrain reduction $\Delta g _ { r }$ (short wavelengths), see below. Gridding of the residual gravity anomalies $\Delta g _ { \mathrm { r e s } } = \Delta g - \Delta g _ { \scriptscriptstyle M } - \Delta g _ { \scriptscriptstyle T } .$ (6.160)   
Application of Stokes’ formula (6.149) on the residual gravity anomalies, resulting in residual geoid heights $N _ { _ { \mathrm { r e s } } }$ . Restoration of the effects of the global model and the terrain to the residual geoid heights:

$$
N = N _ { \mathrm { r e s } } + N _ { \scriptscriptstyle M } + N _ { \scriptscriptstyle T } .
$$

The remove-restore technique can also be applied on the defl ections of the vertical or any other gravity fi eld quantity. It is used successfully also with least-squares collocation.

Since the residual gravity anomalies neither contain the long nor the short-wave parts of the gravity fi eld, they are considerably smaller and smoother than the original data, and they possess (approximately) homogeneity and isotropy properties, cf. [6.1.3]. With global spherical harmonic models of high degree and order, the integration area can be restricted to the region with dense data coverage and a narrow edge zone (spherical distance of a few degrees) around it. As only a small radius of integration is required at this remove-restore technique, a planar approximation of Stokes’ formula is permitted. Stokes’ function then reduces to

$$
S ( \psi ) \approx \frac { 1 } { \sin \left( \frac { \psi } { 2 } \right) } \approx \frac { 2 } { \psi } \approx 2 \frac { R } { I _ { \mathrm { 0 } } } ,
$$

with $I _ { { _ 0 } } = \sqrt { ( x - x _ { _ p } ) ^ { 2 } + { _ 0 } y - y _ { _ p } ) ^ { 2 } }$ and $x _ { p ^ { \prime } } \ y _ { p }$ plane coordinates of the computation point. The spherical surface element is replaced by the planar element

$$
d S = R ^ { 2 } d \sigma .
$$

Inserting (6.162a) and (6.162b) into (6.149) yields Stokes’ formula in planar approximation

$$
N = \frac { 1 } { 2 \pi \gamma _ { _ { m } } } \iint _ { S } ^ { \Delta g } d S ,
$$

which is very convenient to evaluate by FFT techniques.

Different strategies can be pursued for the application of terrain reductions (Forsberg and Tscherning, 1997).

When Helmert’s condensation method is employed, terrain-corrected Bouguer anomalies may be fi rst used for gridding, cf. [6.5.3]. After restoring the Bouguer plate term (“condensation”), Faye anomalies reduced by the effect of the global model serve for the calculation of residual geoid heights.

With the residual terrain correction, only the high-frequency part of topography is taken into account in the remove-restore process, as the long-wave part has been subtracted already with the global model (Forsberg and Tscherning, 1981). It is calculated from a residual terrain model (RTM) which refers to a reference topography, as provided by a global topographic model (spherical harmonic expansion of the same degree and order as the geopotential model), or the moving average over mean heights of, e.g., $1 5 ^ { \prime } \times 1 5 ^ { \prime }$ or $3 0 ^ { \prime } \times$ $3 0 ^ { \prime }$ blocks, Fig. 6.32. The result of this procedure is a balanced set of positive and negative anomalies, where the prism method is used generally for the calculation, cf. [6.5.2].

![](images/1dfad7634f1408a45c9863849c37af6af9fffa2c383d8dacc168a94b124a5558.jpg)  
Fig. 6.32: Bouguer plate with terrain correction and residual terrain correction.

If applied to Stokes’ formula, the remove-restore technique implies that the complete spectrum of the geoid heights is computed from the gravity anomalies in the integration area, substituted by the values of the global model only outside this region. In the case of long-wave discrepancies between the terrestrial gravity data and the global model, this leads to a distortion of the long wavelengths of the geoid. This problem is avoided by leastsquares spectral combination (Sjöberg, 1979; Wenzel, 1982). Here, the long-wavelengths spectral components of the global model and of the gravity anomalies are combined within the area of integration, using least-squares adjustment with spectral weights

$$
W _ { I } = \frac { \sigma _ { I } ^ { 2 } \left( \varepsilon _ { M } \right) } { \sigma _ { I } ^ { 2 } \left( \varepsilon _ { M } \right) + \sigma _ { I } ^ { 2 } \left( \varepsilon \Delta g \right) } .
$$

The error degree variances $\sigma _ { \mathfrak { r } _ { 1 } } ^ { 2 } ( \varepsilon _ { \ M } )$ of the potential coeffi cients of the global model are estimated in analogy to (6.143), and the error degree variances of the terrestrial anomalies $\sigma _ { . . } ^ { 2 } ( \varepsilon _ { _ { \Delta g } } )$ are derived from an error covariance function, in analogy to (6.25). Stokes’ function (6.148a) is extended now by the spectral weights to form an optimum integral kernel

$$
W ( \psi ) = \sum _ { I = 2 } ^ { \infty } \frac { 2 I + 1 } { I - 1 } W _ { I } P _ { I } ( \cos \psi ) .
$$

This function is no longer infi nite at $\psi = 0 ^ { \circ } ,$ , and it converges to zero more rapidly than the original Stokes’ function, see Fig. 6.30.

Early gravimetric geoid calculations with Stokes’ formula are due to Hirvonen (1934) and Tanni (1948). Based on isostatic anomalies, the “Columbus Geoid” was calculated at the Ohio State University (Heiskanen, 1957). A combination of a low-degree satellite model (Goddard GEM-6, degree and order 16) with $1 ^ { \circ } \times 1 ^ { \circ }$ free-air anomalies (integration radius $1 0 ^ { \circ } )$ ) was presented by Marsh and Vincent (1974). Among the recent regional solutions is the $1 ^ { \prime } \times 1 ^ { \prime }$ -gravimetric geoid model USGG2009 for the United States of America and its territories (Fig. 6.33), following the previous $2 ^ { \prime } \times 2 ^ { \prime }$ -geoid, which utilized the EGM96 model and Faye anomalies (Smith and Roman, 2001). USGG2009 is based on a $1 ^ { \prime } \times 1 ^ { \prime }$ -grid of free-anomalies, altimetry-derived anomalies, the SRTM $3 ^ { \prime }$ digital elevation model for topographic reductions, and the global geopotential model EGM2008 as a reference model, cf. [6.6.3]. The surface gravity data have been reduced by the long-wavelength part (global model) and the effect of topography (residual terrain model), and then transferred to the ellipsoid by harmonic downward continuation. A modified Stokes’ kernel was applied for the integration of the residual anomalies, which retained all signal below degree 120 from EGM2008. USGG2009 refers to the NAD83 ellipsoid, cf. [7.1], and is centered in the ITRF reference frame. Presently it is the best approximation of mean sea level, with an accuracy of about $5 ~ \textrm { c m }$ (Roman et al., 2009). Least-squares spectral combination has been also applied in the calculation of a European quasigeoid, which will be discussed in [6.7.2].

![](images/cacbaebd30c02c76a7eb10022587bec021c61ebbfda4faab08fb9bbfa52fd76f.jpg)  
Fig. 6.33: Gravimetric Geoid USGG2009 of the U.S.A., contour line interval $5 \textrm { m }$ , courtesy National Geodetic Survey/NOAA (http://www.ngs.noaa.gov/GEOID/USGG2009/ ).

# 6.7.2 Gravimetric height anomalies and surface defl ections of the vertical

The geodetic boundary-value problem for the physical surface of the Earth has been formulated by $M . S$ Molodensky, through the integral equation (6.92), Molodenskii et al. (1962). By introducing the telluroid $\Sigma$ as an approximation to the Earth’s surface, an integral equation for the disturbing potential was obtained (6.93). In contrast to the derivative ∂T/∂n [ $\acute { n }$ is the normal to the level surface, which entered into the fundamental relation (6.101)], the derivative $\partial T / \partial n _ { _ \Sigma } ( n _ { _ \Sigma }$ normal to the telluroid) is now required. It not only depends on the gravity anomaly but also on the defl ection of the vertical and the inclination of the terrain. Evaluating $\partial T / \partial n _ { _ { \Sigma } }$ from (6.101) and inserting into (6.93) yields a linear integral equation of the second kind for $T$ (Heiskanen and Moritz, 1967, p. 299 ff.)

$$
\begin{array} { l } { \displaystyle { T - \frac { 1 } { 2 \pi } \int \int _ { \Sigma } \left( \frac { \partial } { \partial n _ { \Sigma } } \left( \frac { 1 } { I } \right) - \frac { 1 } { \gamma } \ \frac { \partial \gamma } { \partial h } \frac { \cos \beta } { I } \right) T d \Sigma } } \\ { \displaystyle { = \frac { 1 } { 2 \pi } \int \int _ { \Sigma } \int _ { I } \left( \Delta g - \gamma \left( \xi \tan \beta _ { _ x } + \eta \tan \beta _ { _ y } \right) \cos \beta d \Sigma \right) } , } \end{array}
$$

with $\beta _ { _ { x ^ { \prime } } } \beta _ { _ { y } }$ being the angles of terrain inclination in NS and EW-direction, $\beta$ the angle of maximum inclination, and $\xi , \eta$ the vertical defl ection components; $I$ is the distance between the source point and the computation point. We remember that $\Delta g$ represents the free-air anomaly defi ned on the Earth’s surface according to Molodensky (6.15).

A simpler integral equation can be derived by expressing $T$ as the potential of an infi - nitely thin surface layer condensed on the telluroid. With the surface density $\mu$ (6.114), the law of gravitation (3.10) yields

$$
T = G \int \displaylimits _ { \Sigma } ^ { \mu } \frac { \mu } { I } d \Sigma .
$$

As the potential of a surface layer is harmonic outside the surface, Laplace’s equation is fulfi lled, and we may introduce (6.165) and its normal derivative into the boundary condition (6.101). This strategy again results in a linear integral equation which now only depends on $\Delta g$ and on the terrain inclination. It can be solved by successive approximation, leading to a series expansion for $T .$ In spherical approximation ( $\sigma$ unit sphere, $R$ Earth’s radius), and limiting the series to its fi rst two terms, the disturbing potential then is given by (Moritz, 1971):

$$
T = { \frac { R } { 4 \pi } } \int _ { \sigma } \int S ( \psi ) \big ( \Delta g + G _ { \scriptscriptstyle 1 } + \ldots \big ) d \sigma = T _ { \scriptscriptstyle 0 } + T _ { \scriptscriptstyle 1 } + \ldots
$$

With Bruns’ formula (6.96), the corresponding development for the height anomaly $\zeta$ is obtained:

$$
\zeta = \frac { R } { 4 \pi \gamma } \int \limits _ { \sigma } ^ { \infty } [ \int S ( \psi ) ( \Delta g + G _ { 1 } + \ldots ) d \sigma = \zeta _ { 0 } + \zeta _ { 1 } + \ldots .
$$

With $\mathsf { S } ( \psi )$ being Stokes’ function (6.148), the main term in (6.166a,b) corresponds to Stokes’ formula now applied to the surface gravity anomalies (6.14). The fi rst correction term, in close approximation, is given by

$$
G _ { \scriptscriptstyle 1 } = \frac { R ^ { \scriptscriptstyle 2 } } { 2 \pi } \displaystyle \iint _ { \sigma } ^ { } \displaystyle \frac { H ^ { \scriptscriptstyle N } - H _ { \scriptscriptstyle P } ^ { \scriptscriptstyle N } } { I _ { \scriptscriptstyle 0 } ^ { \scriptscriptstyle 3 } } \Delta g d \sigma , \quad I _ { \scriptscriptstyle 0 } = 2 R \sin \frac { \psi } { 2 } .
$$

It depends on the terrain inclination $H ^ { N }$ normal height) and on the gravity anomalies. Assuming a linear correlation of the gravity anomalies with height, $G _ { \mathfrak { r } }$ can be approximated by the gravimetric terrain correction (6.113), Sideris (1990). Hence, Faye anomalies, cf. [6.5.3], are well suited for the computation of height anomalies.

Since the integral kernel in (6.166c) decreases rapidly with increasing spherical distance $\psi ,$ the integration can be restricted to a limited area. Higher-order terms in $( 6 . 1 6 6 \mathrm { a } / \mathrm { b } )$ contain the tangent of the terrain inclination and can be neglected generally. In order to ensure convergence of Molodensky’s series expansion, extreme inclinations and singularities (steep slopes) need to be removed by some smoothing procedure. The Molodensky correction terms reach the dm-order of magnitude in the high mountains and remain at the cm-order in the lowlands. If the remove-restore technique, cf. [6.7.1], is applied, the corrections reduce by about one-order of magnitude and the series convergence is signifi cantly improved (Denker and Tziavos, 1999). Molodensky’s problem has been thoroughly investigated by Moritz (1971) and others, and the existence and uniqueness of the solution was proved by Hörmander (1976) and Sansò (1988).

A very effi cient method for calculating the height anomaly is provided by the “gradient solution”, which is particularly well suited for FFT techniques (Moritz, 1980; Forsberg and Tscherning, 1997).

Here, the surface gravity anomalies are fi rst reduced to sea level (geoid or quasigeoid), by analytical downward continuation. Then Stokes’ integral is applied, leading to height anomalies on sea level. Subsequent upward continuation of the sea level height anomaly fi nally gives the surface height anomaly:

$$
\zeta = \frac { R } { 4 \pi \gamma } \iint _ { \sigma } \left( \Delta g - \frac { \partial ( \Delta g ) } { \partial H ^ { N } } H ^ { N } \right) S ( \psi ) d \sigma + \frac { \partial \zeta } { \partial H ^ { N } } H ^ { N } .
$$

Poisson’s integral provides the radial derivative of $\Delta g$ (Hofmann-Wellenhof and Moritz, 2005, p. 32 ff.):

$$
\frac { \partial ( \Delta g ) } { \partial H ^ { N } } = \frac { R ^ { 2 } } { 2 \pi } \int \int _ { \sigma } ^ { \Delta g - \Delta g _ { P } } d \sigma ,
$$

and the vertical gradient of $\zeta$ results from (6.96) and (6.101):

$$
\frac { \partial \zeta } { \partial H ^ { N } } = \frac { \partial } { \partial H ^ { N } } \left( \frac { T } { \gamma } \right) = \frac { 1 } { \gamma } \Bigg ( \frac { \partial T } { \partial H ^ { N } } - \frac { 1 } { \gamma } \frac { \partial \gamma } { \partial H ^ { N } } T \Bigg ) = - \frac { \Delta g } { \gamma } .
$$

If the surface anomalies are reduced to the level of the computation point $P ,$ $H ^ { N }$ in (6.167a) has to be substituted by ${ \cal H } ^ { N } - { \cal H } _ { P } ^ { N }$ . The last term in (6.167a) then vanishes, as $H$ outside the integral means $H _ { { P ^ { \prime } } } ^ { N }$ and (6.167a) simplifi es to

$$
\zeta = \frac { R } { 4 \pi \gamma } \iint _ { \sigma } \left( \Delta g - \frac { \partial ( \Delta g ) } { \partial H ^ { N } } \left( H ^ { N } - H _ { P } ^ { N } \right) \right) S ( \psi ) d \sigma .
$$

The anomalies are now reduced from ground level to the level of the calculation point, which means that reference levels are changing with the points of calculation.

The surface defl ection of the vertical (see Molodensky’s defi nition in [6.1.2]) is derived from (6.166b) by differentiation according to (6.98):

$$
 \left\{ \begin{array} { l } { \displaystyle \xi ^ { N } \right\} } = { \frac { 1 } { 4 \pi \gamma } } \int \int _ { \sigma } \left( \Delta g + G _ { 1 } + \ldots \right) { \frac { d S ( \psi ) } { d \psi } } \left\{ \begin{array} { l } { \displaystyle \cos \alpha } \\ { \displaystyle \sin \alpha } \end{array} \right\} d \sigma - { \frac { \Delta g } { \gamma } } { \left\{ \begin{array} { l } { \displaystyle \tan \beta _ { x } } \\ { \displaystyle \tan \beta _ { \gamma } } \end{array} \right\} } . \end{array}
$$

The principal term in (6.168) is Vening-Meinesz’ formula (6.151), and the Molodensky correction terms again take the effect of the terrain into account. Another version of (6.168) is obtained by differentiation of (6.167d), Hofmann-Wellenhof and Moritz (2005, p. 314 ff.).

Molodensky’s problem is characterized by the fact that no assumptions on the density distribution within the Earth are necessary, in contrast to the geoid determination using Stokes’ formula. By the relation (6.9) between the geoid and the quasigeoid, a simple method is available to derive geoid heights from height anomalies by adding a correction term which depends on the Bouguer anomaly and the height. Data reductions onto the geoid and calculations of indirect effects are avoided by this strategy, and density hypotheses enter only through the Bouguer anomaly (Flury and Rummel, 2009). On a large scale, the Bouguer anomalies are negative on the continents, cf. [8.2.4], hence the quasigeoid generally is above the geoid. The differences between the geoid and the quasigeoid are of the cm- to dm-order of magnitude in fl at and hilly regions but may reach one meter and more in the mountains. Defl ections of the vertical defi ned on the ground and on the geoid may differ by a few arcsec in mountainous areas.

One example for a regional quasigeoid determination is the European Gravimetric Quasigeoid EGG07 (Denker et al. 2009). It is based on a high-resolution data set of point and mean gravity anomalies derived from land, sea and airborne gravimetry, and on satellite altimetry in the marine areas (Fig. 6.34). The remove-restore technique was applied using the EIGEN-GL04C (360,360) model from GFZ geopotential model (based on CHAMP, GRACE and terrestrial data), and terrain reductions according to the residual terrain model technique. A $3 ^ { \prime \prime } \times 3 ^ { \prime \prime }$ (partly $1 ^ { \prime \prime } \times 1 ^ { \prime \prime } )$ digital elevation model delivered the terrain information, and a moving average fi lter over $3 0 ^ { \prime }$ $\times 4 5 ^ { \prime }$ blocks provided the reference topography. Gridded $1 ^ { \prime } \times 1 ^ { \prime }$ residual gravity anomalies were transformed to height anomalies by least-squares spectral combination, cf. [6.7.1]. The main part of EGG07 (Fig. 6.35) stems from the global model, but the contributions from terrestrial gravity data and topography still amount to $\pm 0 . 4 \mathrm { ~ m ~ }$ (maximum $4 ~ \mathsf { m }$ and $\pm 0 . 0 3 \mathrm { ~ m ~ }$ (maximum $0 . 8 \mathrm { ~ m ~ }$ ), respectively. The accuracy of the $1 ^ { \prime } \times 1 ^ { \prime }$ EGG07 quasigeoid model has been evaluated by comparisons with GPS/leveling control points, which indicate an accuracy potential in the order of 0.03 to $0 . 0 5 ~ \mathrm { m }$ at continental scales and 0.01 to $0 . 0 2 \mathrm { ~ m ~ }$ over distances up to a few $1 0 0 ~ \mathrm { k m }$ , if high quality and high resolution input data are available in the area of interest. The EGG2008 solution follows the same philosophy, by combining an improved gravity anomaly data set with the global EGM2008 model, cf. [6.6.3]. This reduces the contribution from terrestrial gravity data to about $\pm 0 . 2 \mathrm { ~ m ~ }$ (maximum $2 . 4 \ : \mathrm { m } )$ , and further approaches the $^ { \prime \prime } { \mathrm { C } } { \sf m } ^ { \prime \prime }$ accuracy at local geoid/quasigeoid modeling (Denker, 2012).

![](images/e5f4281d2862aeafde4a5fe1bec1ccf61c79bb8c0975902ffb580ea45e0a7419.jpg)  
Fig. 6.34: Distribution of land, marine and airborne gravity data used for the European quasigeoid EGG07 (Denker et al., 2009).

![](images/fda9b14689c7c8ccfc894ab5bbf9e8c3f3653a56547a7b5b2e52668d7b87d6e8.jpg)  
Fig. 6.35: European gravimetric quasigeoid EGG07, contour line interval $5 \textrm { m }$ (Denker et al., 2009).

Quasigeoid modeling for other parts of the world follow similar strategies, and partly also include GPS/leveling control points.

# 6.7.3 The external gravity fi eld

The gravity fi eld outside the Earth is of interest for the orbit determination of satellites, and for the evaluation and exploitation of gravity fi eld related data obtained by satellite and airborne methods. Corresponding modeling is based on the fact that the gravitational potential is a harmonic function in the exterior space, cf. [3.1.3]. This includes the upward or downward continuation of gravity fi eld quantities from or towards the Earth’s surface, either globally or locally.

Global modeling employs the spherical harmonic expansion of the disturbing potential (spherical approximation), see (6.3) to (6.4)

$$
T ( r , \ \vartheta , \ \psi ) = \sum _ { I = 2 } ^ { \infty } \biggl ( \frac { R } { r } \biggr ) ^ { I + 1 } T _ { _ I } ( \vartheta , \lambda )
$$

and the corresponding expansions for the height anomaly (6.132), the gravity disturbance (6.134) and the gravity anomaly (6.135), the defl ection of the vertical (6.137), the vertical gradient (6.138), and other residual gravity fi eld quantities, where the $T _ { \cal ( } \vartheta , \lambda )$ represent the surface spherical harmonics of $T .$ These expansions converge outside a sphere enclosing the Earth, cf. [3.3.2]. The spherical harmonic expansions clearly reveal the attenuation of the gravity fi eld with altitude, being proportional to $1 / r$ for the disturbing potential, to $1 / r ^ { 2 }$ for the gravity anomaly (gravity disturbance) and defl ection of the vertical, and to $1 / r ^ { 3 }$ for the gravity gradient.

Some examples for gravity fi eld attenuation with height are given in Fig. 6.36. Calculated from the Earth Gravitational Model EGM2008, cf. [6.6.3], the structures of the height anomaly (equal to the quasigeoid at height zero), the gravity anomaly, and the vertical gravity gradient are shown for the height $h = 0$ and $h = 3 5 0 ~ { \mathrm { k m } } .$ , the different behavior of the residual gravity fi eld quantities can be easily recognized.

![](images/a8ba69610459a2d96068d31e46506d681daf5cf75c955e45db74e2feabc36309.jpg)  
Fig. 6.36: Height anomaly, gravity anomaly and vertical gravity gradient at height $h = 0$ km and $h = 3 5 0 ~ \mathrm { k m }$ , from the Earth Gravitational Model EGM2008 (Pavlis et al., 2008); IfE, Leibniz Universität Hannover.

Another example for the small gravity fi eld signal at satellite altitude is given in Fig. 6.37. It shows the near radial component of the gravitational gradient tensor, as measured over two months by the GOCE satellite above the central Andes.

With continuously improving global gravity fi eld data sets, cf. [6.6.3], spherical harmonic developments are of relevance for the majority of gravity fi eld computations in space. More local problems as occurring for instance at airborne gravimetry, on the other hand, requires gravity fi eld modeling which additionally utilizes local gravity data of high resolution and accuracy. The corresponding solutions are provided again by integral formulas.

Dealing with functions harmonic in space and given on the sphere as boundary surface (spherical approximation), the problem of upward continuation corresponds to the fi rst boundary-value problem (Dirichlet problem) of potential theory. The solution is given by Poisson’s integral which for the disturbing potential reads as (Hofmann-Wellenhof and Moritz, 2005, p. 247 ff.)

$$
T _ { _ P } = \frac { R ( r ^ { 2 } - R ^ { 2 } ) } { 4 \pi } { \int \int \frac { T } { \sigma } d \sigma } .
$$

With respect to the free-air anomaly $\Delta g ,$ according to (6.135) the function

$$
r \Delta g = \sum _ { I = 2 } ^ { \infty } ( I - 1 ) \left( { \frac { a } { r } } \right) ^ { I + 1 } T _ { _ I } ( \vartheta , \lambda )
$$

is harmonic in space. This leads to the integral

$$
\Delta g _ { P } = \frac { R ^ { 2 } \left( r ^ { 2 } - R ^ { 2 } \right) } { 4 \pi r } \int \int _ { \sigma } ^ { \Delta g } d \sigma
$$

![](images/8192e70ee69103e1409e1acf97eca0ef78647caf640f0f67fa2cb117af29ff55.jpg)  
Fig. 6.37: Measured GOCE gravitational gradients $T _ { _ { Z Z } }$ (gradiometer reference frame) over the central Andes (October to December 2010), band-pass fi ltered to the gradiometer measurement bandwidth $( 0 . 0 0 5 { - } 0 . 1 \ \mathsf { H z } )$ corresponding to a spatial resolution of about 750 to $4 0 ~ \mathrm { k m }$ , level 1b data provided by ESA; IfE, Leibniz Universität Hannover.

for the calculation of gravity anomalies in space from boundary values, where $\Delta g _ { P }$ refers to the point $P$ in space and $\Delta g$ are the surface anomalies on the spherical boundary surface. The integral kernel decreases rapidly with distance, which allows restriction of the integration area on a limited zone around the computation point.

We now insert (6.171b) into (6.101b) which now represents a differential equation in space, and remove the spherical harmonics of degree zero and one. This leads to a spatial extension of the geoid related Stokes’ formula (6.147) for the disturbing potential, which was derived by Pizetti:

where

$$
\begin{array} { l } { \displaystyle { T ( r , ~ \vartheta , ~ \lambda ) = \frac { R } { 4 \pi } \iint S ( r , \psi ) \Delta g d \sigma , } } \\ { \displaystyle { S ( r , \psi ) = \frac { 2 R } { I } + \frac { R } { r } - \frac { 3 R I } { r ^ { 2 } } - \frac { R ^ { 2 } } { r ^ { 2 } } \cos \psi \left( 5 + 3 ~ | \mathrm { n } \frac { r - R \cos \psi + I } { 2 r } \right) } , } \end{array}
$$

with

$$
\begin{array} { r } { I = \sqrt { r ^ { 2 } + R ^ { 2 } - 2 R r \cos \psi } , } \end{array}
$$

is the extended Stokes’ function.

Bruns’ theorem fi nally gives the separation between the geopotential surface $W = W _ { p }$ and the spheropotential surface $U = U _ { _ Q } = W _ { _ P }$ (height anomaly in space):

$$
\zeta ( r , \ \vartheta , \ \lambda ) = \frac { R } { 4 \pi \gamma } \int \displaylimits _ { \sigma } \int \displaylimits _ { \sigma } \Delta g d \sigma .
$$

Corresponding spatial extensions can be derived for all other integral formulas such as the inverse Stokes’ integral, Hotine’s formula for gravity disturbance, and Vening-Meinesz formulae for the defl ection of the vertical.

# 6.7.4 Astrogeodetic geoid and quasigeoid determination

Geoid and quasigeoid height differences can be obtained from defl ections of the vertical, determined according to (6.57), (6.58) from astronomic and geodetic latitudes and longitudes resp. azimuths.

In astronomic leveling, the defl ections of the vertical are integrated along the path, either on the geoid or on the Earth’s surface (Fig. 6.38). On the geoid, we have

$$
d N = - \varepsilon _ { _ 0 } d s ,
$$

where $\varepsilon _ { \scriptscriptstyle 0 }$ is the vertical defl ection component in the azimuth direction of the path (6.18), reduced to the geoid according to Pizetti’s defi nition, cf. [6.1.2]. Integration between $P _ { \uparrow }$ and $P _ { _ 2 }$ yields the geoid height difference

$$
\Delta N _ { _ { 1 , 2 } } = N _ { _ { 2 } } - N _ { _ { 1 } } = - \int _ { 1 } ^ { 2 } \varepsilon _ { _ 0 } d s .
$$

The negative sign follows from the sign conventions for the geoid height (6.8) and the defl ection of the vertical (6.17).

The geoid defl ection of the vertical, required in (6.174), is obtained by reducing the observed astronomic latitude and longitude onto the geoid:

$$
\Phi _ { _ 0 } = \Phi + \delta \Phi , \Lambda _ { _ 0 } = \Lambda + \delta \Lambda ,
$$

![](images/401fd75947a3fd1283fb259663d884894a1f428254eaa151b215ab3b94f04b08.jpg)  
Fig. 6.38: Astronomic leveling.

where $\Phi _ { \phantom { } _ { 0 } }$ and $\Lambda _ { \phantom { } _ { 0 } }$ are the astronomic coordinates on the geoid (Fig. 6.39). The reductions follow from the integration of the plumb line curvature $\kappa _ { x ^ { \prime } } \kappa _ { y } ( 3 . 7 4 )$ between the Earth’s surface and the geoid:

$$
\delta \Phi = - \int \displaylimits _ { 0 } ^ { H } \kappa _ { x } \ : d H , \quad \delta \Lambda \mathrm { c o s } \Phi = - \int \displaylimits _ { 0 } ^ { H } \kappa _ { y } \ : d H ,
$$

with $H$ being the orthometric height. Inserting (3.67) and (3.70) yields

$$
\delta \Phi = - \int \displaylimits _ { 0 } ^ { H } \frac { \partial g } { \partial x } d H , \quad \delta \Lambda \cos \Phi = - \int \displaylimits _ { 0 } ^ { H } \frac { \partial g } { \partial y } d H ,
$$

$R$ mean radius of the Earth. With (6.17), the NS and EW components of the vertical defl ection are given by

$$
\xi _ { \ L _ { 0 } } = \xi + \delta \Phi , \quad \eta _ { \ L _ { 0 } } = \eta + \mathrm { c o s } \Phi \delta \Lambda ,
$$

![](images/3e36a0cb473404765bd7f9beb30fbc78f779eff67211ad5f744d33375cc73db3.jpg)  
Fig. 6.39: Plumb line curvature in the meridian plane.

and the azimuthal component reads

$$
\begin{array} { r } { \pmb { \mathcal { E } } _ { 0 } = \pmb { \mathcal {xi } } _ { 0 } \cos \alpha + \eta _ { \mathrm { 0 } } \sin \alpha . } \end{array}
$$

In order to evaluate (6.176), the gravity and the horizontal gravity gradient along the plumb line are required. Digital terrain models allow estimation of these quantities with an accuracy between $0 . 1 { ^ { \prime \prime } }$ and $1 ^ { \prime \prime } ,$ but errors may be larger in high mountains. The angle of plumb line curvature itself attains values of a few $0 . 1 ^ { \prime \prime }$ in the lowlands and may reach $1 0 ^ { \prime \prime }$ and more at high mountain stations.

Instead of integrating the defl ections of the vertical on the geoid, the surface vertical defl ections (defi nitions from Helmert or from Molodensky) may be used. The azimuthal component of Helmert’s defl ections of the vertical is given by

$$
\varepsilon = \varepsilon _ { \scriptscriptstyle 0 } - \delta \varepsilon ,
$$

where the components of $\delta \varepsilon$ are obtained from (6.176b). Inserting into (6.174b) yields the geoid height difference

$$
\Delta N _ { 1 , 2 } = N _ { 2 } - N _ { 1 } = - \int ^ { 2 } \varepsilon d s - \int _ { 1 } ^ { 2 } \delta \varepsilon d s .
$$

As seen from Fig. 6.38, the second term on the righthand side equals the orthometric height reduction $E$ which is well known from geometric leveling (6.81b): the angle of plumb line curvature is the horizontal derivative of $E .$ We thus have

$$
\Delta N _ { _ { 1 , 2 } } ^ { _ { 1 , 2 } } = - \int _ { 1 } ^ { 2 } \varepsilon d s - E _ { _ { 1 , 2 } } .
$$

For height anomalies, the difference follows from the differential (Moritz, 1983)

$$
d \zeta = \frac { d \zeta } { d s } d s + \frac { d \zeta } { d h } d h .
$$

The fi rst term describes the effect of Molodensky’s vertical defl ection. The second term enters because the physical surface of the Earth is not a level surface. Using (6.167c) and integration along the path yields Molodensky’s astronomic leveling of height anomalies

$$
\Delta \zeta _ { _ { 1 , 2 } } = \zeta _ { _ { 2 } } - \zeta _ { _ { 1 } } = - \int _ { 1 } ^ { 2 } \varepsilon ^ { N } d s - \int _ { 1 } ^ { 2 } \frac { \Delta g } { \gamma } d h ,
$$

where $\Delta g$ refers to the Earth’s surface.

The relation between geoid and quasigeoid height differences follows from (6.9) and (6.81):

$$
\begin{array} { r } { \Delta \zeta _ { 1 , 2 } = \Delta N _ { 1 , 2 } + E _ { 1 , 2 } - E _ { 1 , 2 } ^ { N } } \end{array}
$$

or when taking (6.179b) into account

$$
\begin{array} { l } { \displaystyle \Delta \zeta _ { 1 , 2 } = - \int _ { 1 } ^ { 2 } \varepsilon d s - E _ { 1 , 2 } ^ { N } , } \end{array}
$$

where $E _ { \scriptscriptstyle { 1 , 2 } } ^ { \scriptscriptstyle { N } }$ is the normal height reduction (6.81c).

The small correction terms in (6.179), (6.181), and (6.182) can be calculated easily from surface gravity and a digital terrain model. Therefore, the integration of surface vertical defl ections is of advantage even for geoid computations, as the tedious reductions onto the geoid required in (6.174) are not necessary.

The line integrals of astronomic leveling presuppose that the defl ections of the vertical are given continuously along the path. In reality, vertical defl ections generally are available only at larger distances (several $1 0 \mathrm { k m }$ or more), which is due to the time-consuming astronomic observations. Station distances of a few km or even less are restricted to special engineering or research surveys (see below). This poses the problem of interpolation between the vertical defl ection points (in the following, we do not distinguish between the vertical defl ections on the geoid and on the Earth’s surface!). Interpolation can be carried out by purely mathematical methods or supported by additional information on the gravity fi eld behavior.

In the simplest case of mathematical interpolation, a linear change of the defl ections of the vertical between the stations $P _ { \mathrm { \uparrow } }$ and $P _ { _ 2 }$ is assumed. The integration then yields

$$
\Delta N _ { _ { 1 , 2 } } = - \frac { \varepsilon _ { _ 1 } + \varepsilon _ { _ 2 } } { 2 } s ,
$$

where $s$ is the distance between $P _ { \uparrow }$ and $P _ { _ 2 }$ .

The linear interpolation model is adequate in fl at areas and where the distances between the vertical defl ection points are not too large (a few $\mathsf { k m } ^ { \prime }$ ). An area with suffi cient control point coverage then can be evaluated either by forming triangles and adjusting the geoid height misclosures or by a surface polynomial approximation to the geoid (Vanicˇek and Merry, 1973). The polynomial coeffi cients are determined from the corresponding series expansions of the vertical defl ection components, which result from (6.98) and Bruns’ formula

$$
\xi = - \frac { 1 } { R } \frac { \partial N } { \partial \varphi } , \quad \eta = - \frac { 1 } { R \cos \varphi } \frac { \partial N } { \partial \lambda } ,
$$

where the condition of integrability of a potential fi eld, cf. [3.1.5], must be fulfi lled:

$$
\frac { \partial \xi } { \cos \varphi \partial \lambda } = \frac { \partial \eta } { \partial \varphi . }
$$

Least-squares prediction, cf. [6.1.3], offers another effi cient interpolation method (Heitz, 1969), while least-squares collocation, cf. [6.8.2], even allows direct estimation of geoid heights from the vertical defl ections, thus providing an alternative to the integral formulas.

Additional gravity fi eld information between the vertical defl ection points can be supplied by terrain models, gravity anomalies, and zenith angles, and used for interpolation.

A digital terrain model (possibly also taking density variations into account) can be used to calculate the effect of topography on the defl ections of the vertical. For more extended calculation areas, the effect of isostatically compensating masses should also be considered, cf. [6.5.2]. By subtracting the corresponding contribution from the observations, the vertical defl ection fi eld is smoothed, and mathematical interpolation methods are made easier. The interpolated residual defl ections of the vertical are then augmented by the effects of topography and isostasy, leading to a densifi ed network of vertical defl ection points. This remove-restore method has proved to be effi cient especially in mountainous areas (Hirt and Flury, 2008).

If a dense fi eld of gravity stations around the vertical defl ection points is available, it can be utilized for a gravimetric interpolation. Here, gravimetric defl ections of the vertical are computed according to (6.151) by integrating the gravity anomalies over a limited area (e.g., three times the distance between the vertical defl ection points). This gravimetric part is then removed from the observations, in addition a systematic difference between the astrogeodetic and the gravimetric vertical defl ections has to be taken into account (different reference systems, effect of the zones neglected in the calculation of the gravimetric vertical defl ections). The residual defl ections of the vertical thus obtained are smooth and easy to interpolate. This method has been extended to astrogravimetric leveling, with a gravimetric “correction” to quasigeoid differences obtained from linear interpolation of surface defl ections of the vertical (Molodenski et al., 1962). This gravimetric interpolation allows calculation of geoid or quasigeoid height differences with cm to dm accuracy, even at larger spacing of the vertical defl ection points.

Reciprocal zenith angles deliver differences of the vertical defl ection components $\varepsilon$ in the line of sight. According to (6.85), the observed zenith angles $Z$ and the ellipsoidal quantities $\zeta$ are related by (Fig. 6.20)

$$
\zeta _ { 1 } = z _ { 1 } + \varepsilon _ { 1 } , \quad \zeta _ { 2 } = z _ { 2 } + \varepsilon _ { 2 } .
$$

Inserting into (6.87), and taking sign conventions into account, yields

$$
\pmb { \varepsilon } _ { { } _ { 2 } } - \pmb { \varepsilon } _ { { } _ { 1 } } = Z _ { { } _ { 1 } } + Z _ { { } _ { 2 } } - \frac { S } { R } - \pi ,
$$

where $S$ is the spherical distance between $P _ { \uparrow }$ and $P _ { 2 }$ . Starting at a vertical defl ection point, these differences can be used for the interpolation of defl ections of the vertical. The method has found some application in mountainous areas, where an interpolation accuracy of about 1 arcsec has been achieved.

The advantage of the astrogeodetic method of geoid or quasigeoid determination consists in its independence from data outside the area of calculation, in contrast to the gravimetric method where a global coverage with gravity data is needed. In addition, the demands on the accuracy of the point heights are less stringent as with the formation of gravity anomalies. On the other hand, the establishment of a vertical defl ection point requires substantially more time than a gravity measurement. A station spacing of 10 to $2 0 \mathrm { k m }$ is available only in few regions, and even distances of up to 30 to $5 0 ~ \mathrm { k m }$ are limited to well-surveyed countries. Large parts of the continents are covered only sparely, with concentration on profi les along fi rst-order triangulation chains, cf. [7.1.1]. Under these conditions, the accuracy of astronomic leveling mainly depends on the quality of interpolation, where an accuracy of a few cm to $0 . 1 \textrm { m }$ over some $1 0 0 ~ \mathrm { k m }$ can be achieved in densely surveyed areas. With station distances of a few km, and by applying remove-restore techniques with respect to topographic-isostatic effects (see above), the accuracy can be increased to 0.01 to $0 . 0 2 \mathrm { ~ m ~ }$ over several $1 0 0 ~ \mathrm { k m }$ . Sub-millimeter/ km precision can be obtained at dedicated geoid profi les with station distances of 50 to $1 0 0 ~ \mathrm { m } ,$ , employing transportable zenith cameras (Hirt and Seeber, 2007), cf. [5.3.1].

The superior effi ciency of gravimetric methods has greatly reduced the application of astronomic leveling. It is now only occasionally applied at areas or profi les which are not well covered by gravity measurements as in the mountains where gravity stations are typically concentrated along the roads. More important is the method’s capability to independently control gravimetric geoid/quasigeoid solutions, and to high-resolution local gravity fi eld determination as required at sophisticated engineering projects.

Astronomic leveling was introduced by Helmert (1884) and fi rst applied in the Harz mountains, Germany. From the 1950s to the 1970s, astrogeodetic geoid determinations were carried out in a number of countries, using astronomic observations on the fi rst-order triangulation points (Heitz, 1969). Defl ections of the vertical, and the resulting geoid, referred to the national geodetic datum and served for the reduction of horizontal angles and chord distances onto the national reference ellipsoid, cf. [6.3.2], [7.1]. Large-scale solutions included the “Bomford” geoid for Europe (Levallois and Monge, 1978) and the continent-wide geoid determination by Fischer et al. (1968), with an average accuracy of a few meters. High precision astrogeodetic geoid models have been developed in Switzerland and Austria, based on a densifi ed net of vertical defl ection points and high-resolution digital terrain models, and employing remove-restore techniques (e.g., Marti, 1997). Profi les of $5 0 0 ~ \mathrm { k m }$ length and with station distances of a few km have been established in Germany for the control of gravimetric geoid models. Based on astrogeodetic measurements with a transportable zenith camera system and a digital terrain model for applying the removerestore technique, an agreement of a few cm was generally obtained between the astrogeodetic and the gravimetric solutions (Voigt et al., 2009). For parts of continental Europe, a corresponding comparison between astrogeodetic data and gravimetric defl ections of the vertical derived from EGM2008 showed an agreement of about $3 ^ { \prime \prime } ,$ , which reduced to about $1 ^ { \prime \prime }$ after taking the omission error of the global model into account (Hirt et al., 2010).

# 6.8 Least-squares collocation

The strategy of combining observation equations for all relevant data and using leastsquares adjustment for the determination of geometric and gravimetric parameters has been already shortly discussed at the beginning of this chapter. Through least-squares collocation, a stochastic model for gravity fi eld estimation is added, which leads to a very general method of combination.

In the most general form of least-squares collocation with parameters (Moritz, 1980, p. 111 ff.), this method combines the calculation of station coordinates and other deterministic unknowns (harmonic coeffi cients, Earth ellipsoid and Earth orientation parameters, calibration and drift coeffi cients, etc.) with the estimation of residual gravity fi eld quantities at unsurveyed points, utilizing all kind of (geometric and physical) observables (Krarup, 1969; Moritz, 1973). By extending the (linear) observation equation for least-squares (parameter) adjustment by a gravity fi eld signal part, the general form of the observation equation reads

$$
\mathbf { l } = \mathbf { A x } + \mathbf { s } + \mathbf { n } ,
$$

where l is the linearized vector of observations. It is composed of the deterministic part Ax and two stochastic parts s and n. x represents the parameter vector and A the design matrix containing the differential relations between observations and parameters. The signal vector s contains the residual gravity fi eld quantities at any point, either observed or to be predicted; it is more formally handled as a random quantity. The signal vector may include, in contrast to least-squares prediction, cf. [6.1.3], any kind of gravity fi eld quantities such as residual harmonic coeffi cients, geoid or quasigeoid heights, gravity anomalies, defl ections of the vertical, gravity gradient components, etc. The noise vector n represents the errors of the measurements, and is random originally. Each of the stochastic quantities is supposed to have a mean value of zero. The statistical behavior of these two parts is described by the covariance matrix C of the gravity fi eld signals, on the one hand, and the covariance matrix D of the observational noise, on the other, where mutual independence of signal and noise is assumed.

As easily recognized, least-squares collocation with parameters is an overdetermined problem with respect to the parameters (the number of observations exceeds the number of parameters) and an underdetermined problem with respect to the gravity fi eld signal (more signals have to be predicted than have been observed). It is solved by applying a least-squares minimum condition on the weighted quadratic sum of the signal and the noise part, thus combining least-squares adjustment with least-squares prediction already discussed in [6.1.3], Moritz (1980). Following well-known rules of adjustment theory, the solution for the parameter vector is given by

$$
\mathbf { x } = \big ( \mathbf { A } ^ { \intercal } \overline { { \mathbf { C } } } ^ { - 1 } \mathbf { A } \big ) ^ { - 1 } \mathbf { A } ^ { \intercal } \overline { { \mathbf { C } } } ^ { - 1 } \mathbf { I } ,
$$

with $\overline { { \mathbf { C } } } = \mathbf { C } + \mathbf { D }$ . The component of the signal vector predicted in an unsurveyed point $P$ results in

$$
\hat { S } _ { P } = \mathbf { C } _ { P } ^ { \top } \overline { { \mathbf { C } } } ^ { - 1 } \mathbf { \Gamma } ( \mathbf { l } - \mathbf { A x } ) ,
$$

where the covariance vectors and matrices are explained in [6.1.3], but may now include heterogeneous signals. Following the arguments given in [6.2.1] for the combined adjustment, the least-squares parameter adjustment generally is separated from detailed gravity fi eld estimation. This leads to “pure” least-squares collocation, as an extension of least-squares prediction, cf. [6.1.3].

At least-squares collocation, applied to gravity fi eld estimation, the elements of the signal covariance matrix C are required, describing the correlation between heterogeneous residual gravity fi eld quantities. Since all these quantities belong to the same gravity fi eld, the covariances have to be derived from a (harmonic) basic covariance function through covariance propagation. The covariance function of the disturbing potential $T$ is selected for this purpose, as all residual gravity fi eld quantities are related to $T$ in a simple manner. This covariance function is defi ned in analogy to the covariance function of the gravity anomalies (6.21). It is considered to be the mean value of the products of $T$ in the points $P$ and $P ^ { \prime }$ for a constant spherical distance $\psi ,$ where again we assume homogeneity and isotropy. The function is then given by:

$$
K ( \psi ) = \mathrm { c o v } _ { \psi } ( T ) = M \{ T T ^ { \prime } \} _ { \psi } .
$$

Covariance propagation is well known from the theory of errors and is applied here to gravity fi eld signals. As demonstrated by (6.96) to (6.101), all residual gravity fi eld quantities (either observed or to be predicted) can be expressed as a linear functional of $T$ . For an observation $I _ { \phantom { } _ { i } }$ we thus have

$$
I _ { \mathrm { { } } i } = { L _ { \mathrm { { } } _ { i } } ^ { P ^ { \prime } } } T ( P ^ { \prime } ) ,
$$

where $L _ { _ i }$ is the functional to be applied to the disturbing potential $T$ in order to transform it into the gravity fi eld quantity wanted. The covariance between $T$ and $I _ { \phantom { } _ { i } }$ is obtained by applying $L _ { _ i }$ on the covariance function $K ( \psi ) = K ( P , P ^ { \prime } ) ,$ , which can be expressed as a function of the spatial coordinates of $P$ and $P ^ { \prime }$ :

$$
C _ { P i } = M \{  T I _ { i } \} = L _ { i } ^ { P ^ { \prime } } K ( \psi ) .
$$

For different types of observations at $P$ and $P ^ { \prime }$ , the covariance results from a subsequent application of the functionals $L$ valid for the transformation of $T$ into the respective observation:

$$
C _ { i j } = M \left\{ I _ { i } I _ { j } \right\} = L _ { i } ^ { P } L _ { j } ^ { P ^ { \prime } } K ( \psi ) .
$$

The same rules have to be followed if heterogeneous signals shall be estimated.

The statistical description of the Earth’s gravity fi eld required for least squares collocation is available by anomaly degree variance models, cf. [6.1.3]. The relation of these models to the basic covariance function introduced above can be derived by applying the mean value operator (6.190) on the spherical harmonic expansion of the disturbing potential (6.4). This yields the spatial covariance function of $T _ { : }$

$$
K ( \psi ) = \sum _ { I = 2 } ^ { \infty } \sigma _ { _ { I } } ^ { 2 } \left( T \right) \left( \frac { R ^ { 2 } } { r r ^ { \prime } } \right) ^ { I + 1 } P _ { _ { I } } \left( \cos \psi \right) ,
$$

where the potential degree variances are defi ned in analogy to (6.26):

$$
\sigma _ { { } _ { I } } ^ { 2 } ( T ) = M \{ { \cal T } _ { { } _ { I } } ^ { 2 } \} .
$$

Taking Bruns’ formula $N = \ T / \gamma$ into account, equation (6.143) provides the relation between the degree variances of the disturbing potential and the gravity anomalies:

$$
\sigma _ { { \scriptscriptstyle I } } ^ { 2 } ( T ) = \bigg ( \frac { R } { { \cal I } - 1 } \bigg ) ^ { 2 } \sigma _ { { \scriptscriptstyle I } } ^ { 2 } \big ( \Delta g \big ) .
$$

Inserting (6.195) into (6.194a) fi nally yields

$$
K ( \psi ) = R ^ { 2 } \sum _ { I = 2 } ^ { \infty } \frac { 1 } { ( I - 1 ) ^ { 2 } } \sigma _ { I } ^ { 2 } \left( \Delta g \right) \left( \frac { R ^ { 2 } } { r r ^ { \prime } } \right) ^ { I + 1 } P _ { I } ( \cos \psi ) ,
$$

which enables the calculation of the basic covariance function from an anomaly degree variance model. For local applications, the covariance function has to be fi t to the gravity fi eld structure in the area of calculation, cf. [6.1.3].

The advantage of least-squares collocation is the fl exibility in estimating any kind of gravity fi eld quantity from different types of gravity fi eld observations, at surveyed and unsurveyed points. The data can be processed as discrete values and need not be continuous, as required for the application of integral formulas, cf. [6.7]. Neither gridding of the data nor reduction to some reference level is required. For homogeneous and continuously distributed data, least-squares collocation transforms into the integral formulas of physical geodesy (Moritz, 1976). On the other hand, the amount of data that can be handled remains limited by computing facilities, as equation systems have to be solved for the inversion of $\bar { \mathbf { C } }$ having a dimension equal to the number of observations. Applications have therefore been restricted to limited areas and data sets. By introducing some restrictions on the data, computing time can be reduced and larger data sets evaluated (Sünkel, 1986a; Bottoni and Barzaghi, 1993; Sansò and Tscherning, 2003).

Least-squares collocation is applied especially for local and regional geoid determination (Tscherning and Forsberg, 1986; Denker, 1988), but also for the estimation of gravity anomalies from altimetric geoid heights and for downward continuation problems. Remove-restore techniques are used generally, cf. [6.7.1], which reduces the data collection area. One example for the application of least-squares collocation is the geoid of Austria, determined from vertical defl ections and gravity anomalies after reducing a global and a topographic-isostatic gravity model (accuracy of a few cm), Kühtreiber (2002). The upward continuation of second derivatives of the disturbing potential from the ground, for GOCE data calibration and validation represents another example of least-squares application (Wolf and Denker, 2005).

# 7 Geodetic and Gravimetric Networks

Geodetic and gravimetric networks consist of monumented control points that provide the reference frames for positioning and gravity-fi eld determination. In the sequel, we concentrate on regional networks which are established nation- or continent-wide. They serve as the basis for all kind of surveying and navigation, as well as for geo- information systems including topographic and thematic map series, and for the investigation of recent geodynamics. Regional networks are increasingly derived from or integrated into global reference frames established and maintained by international conventions, cf. [2.4], [5.4.3]. Local networks are established, e.g., for engineering and exploration projects, real estate surveys and crustal movement investigations. They generally follow similar rules as regional networks at design, measurement, and evaluation, adapted to the specifi c demands and peculiarities of the respective problem.

Until recently, horizontal and vertical control networks have been established separately, following the classical treatment of (horizontal) positioning and heighting. These networks still are the basis of national geodetic reference systems, and they even have been partly combined to continent-wide systems [7.1], [7.2]. Since some decades, geodetic space methods allow the establishment of three-dimensional (3D) networks orientated with respect to a geocentric reference system. Today, these methods are characterized by very effi cient procedures and homogeneous results of high accuracy, and consequently they are superseding the classical control networks. Strong endeavors are made now to integrate these networks into the 3D frame which also requires the inclusion of a geoid model [7.3]. Gravity networks serve the different needs of geodesy and geophysics, with the reference provided either by a global gravity standardization net or by absolute gravimetry; they are now also tied to the 3D geodetic reference frame [7.4].

If reobserved after a certain time span, geodetic and gravimetric networks can be utilized for the detection and investigation of medium- and long-term temporal variations of position and gravity. With progress in data acquisition and evaluation, continuously operating networks are established increasingly, which also allow the measurement of short-term variations. World-wide networks meanwhile monitor global changes and the variations of the Earth rotation routinely, cf. [2.4.2], while regional and local networks concentrate on the investigation of areas affected by recent geodynamic activities, cf. [8.3.4], [8.3.5].

The establishment of geodetic networks is treated in textbooks on geodesy and geodetic surveying, e.g., Bomford (1980); Moffi tt and Bossler (1997); Anderson and Mikhail (1998); Kahmen (2006), and Hofmann-Wellenhof et al. (2008) with respect to GNSS; for gravity networks see, e.g., Torge (1989).

# 7.1 Horizontal control networks

National horizontal control networks were established from the eighteenth century until the 1980s, where the networks’ design, observation, and computation methods changed with the available techniques. Computations were carried out on a conventional reference ellipsoid fi tted to the survey area. Since the 1960s, spatial geodetic methods have allowed orientation of the classical networks with respect to the global geocentric reference system, and control of scale and systematic distortions. In the following, we describe the design of these networks, the measurement and computation techniques applied, the accuracy achieved, and the orientation with respect to the Earth’s body (geodetic datum). Having served (and serving) as a basis for many applications in surveying and mapping, they are still of relevance and now in a state of transition to the global 3D reference frame, cf. [7.3].

Horizontal control networks have been realized by trigonometric (triangulation) points, which in principle should be distributed evenly over the country. One distinguishes between different orders of trigonometric points, from fi rst-order or primary ( station separation 30 to $6 0 ~ \mathrm { k m } )$ ) to second-order (about $1 0 ~ \mathrm { k m } )$ to fourth- or even fi fth-order (down to 1 to $2 \ \mathrm { k m } \cdot$ ) stations, where the state of the networks’ coverage strongly depends on the development of the respective region or country. The maximum distance between fi rst-order points was determined by terrestrial measurement methods, which required intervisibility between the network stations. Consequently, fi rst- and partly also secondorder stations were established on the top of hills and mountains; observation towers (wooden or steel constructions with heights of $3 0 ~ \mathsf { m }$ and more) were erected especially in fl at areas. The stations have been permanently marked by underground and surface monuments (stone plates, stone or concrete pillars, bolts in hard bedrock). Eccentric marks have been set up in order to aid in the recovery and verifi cation of the center mark.

Classical horizontal control networks have been observed by the methods of triangulation, trilateration, and traversing.

In triangulation, all angles of the triangles formed by the trigonometric points are observed with a theodolite (Fig. 7.1). The instrument is set up on the observation pillar or tower; at large distances the targets are made visible by light signals. Either directions (successive observation of all target points) or angles (separate measurement of the two directions comprising one angle) are observed in several sets (i.e., in both positions of the telescope), distributed over the horizontal circle of the theodolite. The scale of a triangulation network is obtained from the length of at least one triangulation side, either derived from a short baseline through a baseline extension net or measured directly by a distance meter. Astronomic observations provide the orientation of the network, where an astronomic azimuth (Laplace azimuth) is needed for the horizontal orientation, see below.

![](images/1ae0a84eddddf7fd4692169fe75d38ac3cbba19873883b9f2bf07e6d9660448e.jpg)  
Fig. 7.1: Triangulation with baseline extension net and Laplace azimuth (principle).

![](images/17788417048e3f09296ec51a7019f164de85e147064c13a6cf01f8d1b8f5463d.jpg)  
Fig. 7.2: Trilateration with Laplace azimuth (principle).

Trilateration employs electromagnetic distance meters in order to measure the lengths of all triangle sides of a network, including diagonals (Fig. 7.2). Again, at least one Laplace azimuth is needed for the orientation of the net. Electromagnetic distance measurements put less demands on the stability of observation towers as compared to angular measurements, and the use of microwaves makes the method more independent from weather conditions.

Traverses combine distance and angular measurements, where the traverse stations are arranged along a profi le between already existing control points. The traverse stations may be either transformed into the national reference system by means of the control points, or immediately calculated in that system if astronomic (Laplace azimuth) or terrestrial orientation is available, Fig. 7.3 gives some examples. Traversing represents a very effective and fl exible method for establishing horizontal control, with no more need to establish stations on hilltops. It has been employed primarily for the densifi cation of higher-order networks.

![](images/d8126042544c04e4ef0c3a5532b9ce797cf36d1f040393ac29b2cb9ca7300454.jpg)  
Fig. 7.3: Traverse connecting two control points (principle): a) without additional orientation, b) with orientation by Laplace azimuths, c) with orientation by directions to control points.

Horizontal control networks have also be formed by combining the methods of triangulation, trilateration, and traversing. Such networks are very stable in design, and allow establishment of fi rst- and second-order control simultaneously. Optimization methods have been developed for the design and survey of trigonometric networks. Starting from the demands on accuracy and reliability, these methods provide information on the optimum point confi guration and the distribution of the measurements in the network given the limitations of available equipment and the maximum allowable cost of the survey (Grafarend and Sansò, 1985).

Triangulation as part of a national geodetic survey started in France (1733–1750: Carte géométrique de la France, under the direction of Cassini de Thury) and in Great Britain (since about 1780 triangulation by the Ordnance Survey, under $W .$ Roy and others). It continued to be the method for establishing horizontal control networks in the nineteenth and twentieth century until the introduction of electromagnetic distance measurements. Triangulation often started with chains (in many cases established along meridians and parallels) composed of triangles or quadrilaterals with diagonals tied together every few $1 0 0 ~ \mathrm { k m }$ . The meshes of this framework then were fi lled by fi rst- or second-order areal triangulation. The triangulations of Bavaria (1808–1828, J.G. Soldner) and of Prussia (since 1875, O. Schreiber) brought signifi cant improvements in measurement and calculation techniques, which also infl uenced other national geodetic surveys. Large-scale networks (chains and fi lling nets) were developed in the U.S.A. (starting in the 1830s and connected with the names of F. R. Hassler and (later) J.F. Hayford, W. Bowie and many others) and in the former Soviet Union (since the 1930s, T.N. Krassovski). Trilateration was applied from the 1950s to the 1970s for strengthening, extending, and densifying triangulation networks. Airborne microwave methods were employed for the rapid survey of regions with diffi cult access and for bridging water areas (a few meters to $^ { 1 0 \mathrm { ~ m ~ } }$ accuracy over some $1 0 0 ~ \mathrm { k m } ,$ . Traversing has been used mainly for network densifi cation since the 1960s, but fi rst-order geodimeter traverses also strengthened continental networks (U.S.A.) or even established them (Australia). From the 1960s to the 1980s, satellite methods were utilized to control the quality of horizontal control networks and especially to determine the orientation and the scale of the ellipsoidal systems with respect to the global geocentric system, see below.

First- and some second-order horizontal control networks have been calculated on a reference ellipsoid within the system of ellipsoidal coordinates, cf. [4.1]. Lower-order networks are primarily calculated in planar Cartesian coordinates, after conformal mapping of the ellipsoid onto the plane (Maling, 1973; Kuntz, 1990; Grafarend and Krumm, 2006). The network calculation started with the reduction of the observed horizontal angles/directions and spatial distances to the ellipsoid, where the gravity-fi eld-related reductions (defl ections of the vertical, geoid height) were not considered during earlier surveys, cf. [6.3.2]. The adjustment was carried out either by the method of conditions or by variation of the coordinates, with redundancy resulting from triangle misclosures, diagonals in trilateration quadrilaterals, and additional baselines and Laplace azimuths. The coordinates’ transfer from an initial point (see below) was based on the solutions of the direct resp. inverse problem on the ellipsoid, cf. [6.3.3]. Among the defi ciencies of this classical “development method” are the neglecting of the defl ections of the vertical, the inadequate reduction of distances on the ellipsoid, and especially the step by step calculation of larger networks, with junction constraints when connecting a new network section to an existing one. This led to long-wavelength network distortions of different type, with regionally varying errors in scale $1 0 ^ { - 5 }$ and more) and orientation (a few arcsec). Coordinate errors with respect to the initial point increased from a few decimeters over about $1 0 0 ~ \mathrm { k m }$ to about $1 \textrm { m }$ over several $1 0 0 ~ \mathrm { k m }$ and reached $_ { 1 0 \textrm { m } }$ and more at the edges of extended continent-wide networks.

The geodetic datum of a horizontal control network comprises the parameters of the reference ellipsoid and of the network’s orientation with respect to the Earth’s body, cf. [6.3.3]. Conventional ellipsoids, as computed by the adjustment of several arc measurements, were introduced during earlier geodetic surveys, cf. [1.3.3]. Some horizontal networks refer to locally best-fi tting ellipsoids, as derived from a minimum condition on the observed vertical defl ections, using the equations (6.51):

$$
\sum ( \xi ^ { 2 } + \eta ^ { 2 } ) = \operatorname * { m i n } .
$$

Tab. 7.1 gives the parameters of some reference ellipsoids that have been used for national geodetic surveys (Strasser, 1957; NIMA, 2000).

The ellipsoids of Airy (applied in Great Britain), Everest (India, etc.), Bessel (Germany, Austria, Japan, etc.), Clarke 1866 (U.S.A., Canada, etc.), and Clarke 1880 (France, etc.) are based on the adjustment of arc measurements distributed over the continents. The Hayford ellipsoid fi ts best to the vertical defl ection (topographic-isostatically reduced) fi eld in the U.S.A., it has been introduced in a number of countries. The Krassovski ellipsoid resulted from a fi t to the Russian triangulations, with additional data from western Europe and the U.S.A. The ellipsoids of the Geodetic Reference Systems GRS67 (Australia, etc.) and GRS80 represent recent global approximations to the geoid, cf. [4.3].

The orientation of the ellipsoid was realized by defi ning the ellipsoidal coordinates of a fundamental (initial) point, also called network origin, and by conditions for the parallelism of the axes of the ellipsoidal and the global geocentric system, cf. [6.3.3].

In earlier surveys, the coordinates of the fundamental point were fi xed by postulating equality between observed astronomic latitude, longitude, and orthometric height and the corresponding ellipsoidal quantities. This is identical to setting the defl ection of the vertical and the geoid height of the fundamental point to zero:

$$
\xi _ { { \scriptscriptstyle F } } = 0 , \quad \eta _ { { \scriptscriptstyle F } } = 0 , \quad N _ { { \scriptscriptstyle F } } = 0 .
$$

Tab. 7.1. Parameters of reference ellipsoids (rounded values), NIMA (2000)   

<table><tr><td>Name, Year</td><td>Semi-major axis a (m)</td><td>Reciprocal flattening 1/f</td></tr><tr><td>Airy, 1830</td><td>6 377 563</td><td>299.3</td></tr><tr><td>Everest,1830</td><td>6 377 276</td><td>300.8</td></tr><tr><td>Bessel, 1841</td><td>6 377 397</td><td>299.15</td></tr><tr><td>Clarke, 1866</td><td>6378 206</td><td>294.98</td></tr><tr><td>Clarke, 1880</td><td>6 378 249</td><td>293.47</td></tr><tr><td>Hayford, 1909</td><td>6378 388</td><td>297.0</td></tr><tr><td>= Int.Ell.1924</td><td></td><td></td></tr><tr><td>Krassovski, 1940</td><td>6 378 245</td><td>298.3</td></tr><tr><td>GRS67</td><td>6 378 160</td><td>298.247</td></tr><tr><td>GRS80</td><td>6 378 137</td><td>298.257</td></tr></table>

This strategy provides a good approximation of the ellipsoid to the geoid close to the origin, but may lead to larger deviations at more remote areas (Fig. 7.4). If a suffi cient number of vertical defl ection points were available and well distributed over the area of calculation, the minimum condition (7.1) was used. It permits the determination of the defl ection of the vertical in the fundamental point and at extended networks also the parameters of a best-fi tting ellipsoid. This procedure led to an optimum fi tting over the whole area, and kept the defl ections of the vertical small. In many cases, the geoid height of the origin point was defi ned indirectly by reducing the baselines onto the geoid and treating them as ellipsoidal quantities (Fig. 7.5). The minimum condition for the geoid heights

$$
\sum N ^ { 2 } = \operatorname* { m i n } .
$$

was seldom applied using relative geoid heights calculated from astronomic leveling, cf. [6.7.4], and utilizing the last equation of (6.51).

The parallelism of the axes of the ellipsoidal and the geocentric system was achieved by the condition equations (6.57) and (6.58) for the defl ection of the vertical and the azimuth (Laplace equation). In extended networks, several base lines and Laplace stations often were established at distances of a few $1 0 0 ~ \mathrm { k m }$ in order to control the error propagation through the network with respect to scale and orientation (effects of lateral refraction). More recently, the ellipsoid parameters of a geodetic reference system have been introduced, cf. [4.3], and the ellipsoid has been optimally fi tted to the geoid, Fig. 7.6. Tab. 7.2 lists the ellipsoids and the origin points used for some geodetic datums (NIMA, 2000).

![](images/b49d32786783a93b96026bb2f9aa25f2d83083991bfc7e1eb532efb24280989a.jpg)  
Fig. 7.4: Locally best fi tting “conventional” ellipsoid.

![](images/6034e909df56c9fa35dd459100e6d55f298be3afc593ec15eb5251afb08e07c1.jpg)  
Fig. 7.5: Regionally best fi tting ellipsoid.

![](images/5d727e223f56d10b64239352a087c8897875bf12960fee8f64a394ce333bd205.jpg)  
Fig. 7.6: Mean Earth ellipsoid.

Tab. 7.2. Reference ellipsoids and origin points of some geodetic datums   

<table><tr><td rowspan="2">Geodetic datum</td><td rowspan="2">Reference ellipsoid</td><td rowspan="2">Name of origin</td><td colspan="2">Origin</td></tr><tr><td>Latit.</td><td>Longit.</td></tr><tr><td>Australian Geodetic 1984 (AGD84)</td><td>GRS67</td><td>Johnston</td><td>-25°57&#x27;</td><td>133°13&#x27;</td></tr><tr><td>Deutsches Hauptdreiecksnetz (DHDN),Germany</td><td>Bessel 1841</td><td>Rauenberg/Berlin</td><td>52°27&#x27;</td><td>13°22&#x27;</td></tr><tr><td>European Datum 1950 (ED50)</td><td>Intern.Ellipsoid 1924</td><td>Potsdam, Helmertturm</td><td>52°23&#x27;</td><td>13°04&#x27;</td></tr><tr><td>Indian</td><td>Everest 1830</td><td>Kalianpur</td><td>24°07&#x27;</td><td>77°39&#x27;</td></tr><tr><td>North American 1927 (NAD27)</td><td>Clarke 1866</td><td>Meades Ranch, Kansas</td><td>39°13&#x27;</td><td>261°27&#x27;</td></tr><tr><td>North American 1983 (NAD83)</td><td>GRS80</td><td>Geocentric</td><td></td><td></td></tr><tr><td>Ordnance Survey of Great Britain 1936 (OSG36)</td><td>Airy 1830</td><td>Herstmonceux</td><td>50°52&#x27;</td><td>0°21&#x27;</td></tr><tr><td>Pulkovo 1942, former Soviet Union</td><td>Krassovski 1940</td><td>Pulkovo</td><td>59°46&#x27;</td><td>30°20&#x27;</td></tr><tr><td>South American 1969 (SAD69)</td><td>GRS67</td><td>Chua,Brazil</td><td>-19°46&#x27;</td><td>311°54&#x27;</td></tr></table>

The following description of the triangulation networks established in North America and Europe illustrates the development of regional horizontal control systems, and the primary triangulation of Germany serves as an example for a local solution.

The horizontal control network of the U.S.A. was constructed by triangulation chains with mesh sizes of about $5 0 0 ~ \mathrm { k m }$ . Nodal nets with baselines and Laplace azimuths were established at the junctions of the chains and treated as constraints in the adjustment, and areal networks later fi lled the meshes. A conventional ellipsoid (Clarke, 1866) was introduced, with the orientation obtained from the minimum condition for vertical defl ections (7.1): North American Datum 1927 (NAD27), see Tab. 7.2. This system has been replaced by the North American Datum of 1983 (NAD83), implemented as legal datum in 1986. NAD83(1986) combines the horizontal control networks of the U.S.A., Canada, Greenland, Mexico, and Central America by a rigorous adjustment (Schwarz and Wade, 1990), Fig. 7.7. The observations include terrestrial data (horizontal directions, azimuths, distances), Doppler stations (for large-scale control and reference to the geocenter), and VLBI baselines (for scale and orientation). The adjustment (about 1.8 million observations and $3 0 0 ~ 0 0 0$ points) was performed by Helmert-blocking (Wolf, 1978) and utilized a height-constrained 3D procedure, cf. [6.2] (Vincenty, 1982). The two-dimensional results refer to the Geodetic Reference System 1980, with a geocentric position accurate to about $2 \textrm { m }$ . The relative station uncertainty is a few cm to a few dm for distances between 10 and $3 0 0 ~ \mathrm { k m }$ (Snay, 1990). NAD83 (1986) has been superimposed by GPS positioning since the end of the 1980s, and local readjustments of GPS and terrestrial data led to numerous state and regional High Precision Geodetic Networks (HPGNs), in addition to a continuously operating GPS network. This led to a recomputation as a 3D network, and a new realization of the horizontal datum within the National Spatial Reference System: NAD83 (NSRS2007), cf. [7.3].

![](images/ec1860249f90e870ec6686029f077037ce1753c78736e8941a76ba30c1cf4160.jpg)  
Fig. 7.7: Horizontal control network of the U.S.A. (NAD83), with fi rst- and second-order triangulation, and traverses, courtesy National Geodetic Survey, National Ocean Service, NOAA.

Since the 1950s, attempts have been made in Europe to unify the national triangulation networks, where the political separation forced to separate solutions for western and eastern European countries. In western Europe, a unifi ed European triangulation network (RETrig) was developed, which started from a central European network formed by selected triangulation chains and later was augmented by blocks in the southwest, southeast, and north (Whitten, 1952): European Datum 1950 (ED50), see Tab. 7.2. The International Ellipsoid 1924 served as the reference surface and was orientated by the minimum condition (7.1), which provided vertical defl ection components $( \xi = 3 . 3 6 ^ { \prime \prime }$ , $\eta \ : = \ : 1 . 7 8 ^ { \prime \prime } )$ for the origin Potsdam, Helmert-Turm. The baselines, reduced to the geoid, indirectly provided the geoid height ( $N = 0 . 4 ~ \mathrm { m } )$ at the origin. A rigorous readjustment of all fi rst-order triangulation nets was carried out later, including electromagnetic distance measurements, VLBI, satellite laser ranging, and Doppler observations: European datum 1987 (ED87), Poder and Hornik (1989). Orientation was adopted from ED50, but parallelism of the axes and scale could be improved. While ED50 was introduced in several countries, and served as the NATO military system until the 1990s, no practical application was found for ED87. Extensive retriangulations took place in eastern Europe since the 1950s. They were connected to the horizontal control network of the former Soviet Union, which was based on extended triangulation chains. Calculations were performed on the Krassovski (1940) ellipsoid, with parameters and orientation derived from the minimum condition for vertical defl ections (7.1), and the geoid height set to zero at the origin Pulkovo: Pulkovo Datum 1942 ( Izotov, 1959). Reductions to the ellipsoid became possible by observed and gravimetrically interpolated defl ections of the vertical and quasigeoid heights from astrogravimetric leveling, cf. [6.7.4]. A readjustment of the Russian triangulation chains together with the fi rst- and second-order networks of the eastern European countries delivered the last realization of this unifi ed astrogeodetic “System $4 2 ^ { \prime \prime }$ in 1983. Since the end of the 1980s, a new European Terrestrial Reference System (ETRS) has been defi ned, and realized through geodetic space techniques, cf. [7.3].

The primary triangulation net of Germany, developed since the $1 8 7 0 s ,$ is an example of a local horizontal control network. The northwestern part, between the rivers Elbe and Main, was covered by triangulation chains and densifi cation nets between 1870 and 1895 as part of the geodetic survey of Prussia. A conventional ellipsoid (Bessel, 1841) was introduced for the calculation and orientated by the condition (7.2) at the origin Rauenberg/Berlin, whereby the geoid height was fi xed indirectly through the reduction of fi ve baselines, one of them located near Berlin. The Laplace azimuth from Rauenberg to Berlin, Marienkirche provided the network’s orientation on the ellipsoid. After the network adjustment, the ellipsoidal coordinates were calculated according to the development method. The eastern parts of Prussia and the triangulations of the southern German states were later tied to this “Schreiber’s block” utilizing common points at the networks’ margins: Deutsches Hauptdreiecksnetz (DHDN), see Tab. 7.2. In western Germany, the DHDN has been locally improved since the 1950s by additional horizontal directions and electromagnetic distance measurements, without changing the original datum. While the relative accuracy over some 10 to $1 0 0 ~ \mathrm { k m }$ is at the dm order of magnitude, distortions up to $1 \textrm { m }$ have been found between different parts of the network. In eastern Germany, a complete retriangulation was carried out after 1950 and calculated within the common adjustment of the eastern European triangulations (see above): Staatliches Trigonometrisches Netz 1942/1983 (STN42/83), Ihde und Lindstrot (1995). The DHDN90 thus consists of three blocks observed over a time span of more than 100 years with different orientation (Schmidt, 1995), Fig. 7.8. The sites of this classical fi rst-order triangulation generally are included into the national geodetic base net being established by means of GNSS methods. The densifi cation networks, on the other hand, probably will be maintained only partially within the frame of state-wide horizontal control, cf. [7.3].

Satellite positioning was employed early to control the quality of horizontal-control networks given in a local or regional datum, and to determine the datum transformation parameters with respect to the geocentric system, Ashkenazi et al. (1988). Equations (6.47) were used to calculate translation, rotation, and scale factor, using identical stations coordinated in the global system (especially in the WGS84) and in the local or regional geodetic datum (after proper transformation from geodetic to Cartesian coordinates). Tab. 7.3 provides mean values for translation, rotation, and scale factor for some geodetic datums, with reference to a geocentric system.

Translations are at the order of magnitude of the defl ections of the vertical. They are larger when conventional ellipsoids have been used and decrease with best-fi tting ellipsoids. The rotation angles mirror the accuracy of the astronomic observations and are usually not signifi cant. While the scale errors for older networks reach $1 0 ^ { - 5 }$ and more, they attain only $1 0 ^ { - 6 }$ and less in recent systems, characterizing the progress in length determination. The results strongly depend on the number and distribution of the identical points. Due to network distortions, datum-shift values for a limited area may differ signifi cantly from the mean values of a national reference system given above, e.g., by 10 to $2 0 \mathrm { m }$ and more for the translation parameters, and $1 0 ^ { - 6 }$ and more for the scale factor. As an example, a scale difference of nearly $3 \times 1 0 ^ { - 6 }$ has been found between the central and the southern part of DHDN/Germany. If a 3-parameter solution (translation only) is carried out, the translation values of older networks may experience considerable changes.

![](images/c1297ee0e338a49d2d178ec9de66ac5ded35b76c88ec31995f973fa805ea7057.jpg)  
Fig. 7.8: Primary triangulation net of Germany (DHDN90), courtesy Bundesamt für Kartographie und Geodäsie (BKG), Frankfurt a.M., Germany.

Tab. 7.3. Translation, rotation, and scale factors (mean values) for some geodetic datums with reference to the geocentric system (DMA, 1987; NIMA, 2000), for DHDN and Pulkovo 1942 from Ihde and Lindstrot (1995)   

<table><tr><td rowspan="3">Geodetic Datum (see Tab. 7.2)</td><td colspan="8">7-Parameter-Transformation</td><td colspan="3">3-Parameter-Transf.</td></tr><tr><td colspan="2">Translation (m)</td><td colspan="2"></td><td colspan="2">Rotation (arcsec)</td><td colspan="2">Scale factor</td><td colspan="3">Translation (m) only</td></tr><tr><td>X。</td><td>Y</td><td>Z</td><td>8</td><td>8</td><td>8</td><td></td><td>m × 106</td><td>X</td><td>Y</td><td>Z</td></tr><tr><td>AGD84</td><td>-127</td><td>-50</td><td>153</td><td>0.0</td><td></td><td>0.0 -0.1</td><td></td><td>1.2</td><td>-134</td><td>-48</td><td>149</td></tr><tr><td>DHDN</td><td>582</td><td>105</td><td>414</td><td>-1.0</td><td></td><td>-0.4</td><td>3.1</td><td>8.3</td><td></td><td></td><td></td></tr><tr><td>ED50</td><td>-102</td><td>-102</td><td>-129</td><td>0.4</td><td></td><td>-0.2</td><td>0.4</td><td>2.5</td><td>-87</td><td>-98</td><td>-121</td></tr><tr><td>Indian</td><td>227</td><td>803</td><td>274</td><td>-0.4</td><td></td><td>-0.6</td><td>-0.4</td><td>6.6</td><td>295</td><td>736</td><td>257</td></tr><tr><td>NAD27</td><td>-4</td><td>166</td><td>183</td><td>-0.3</td><td></td><td>0.3</td><td>-0.1</td><td>0.4</td><td>-8</td><td>160</td><td>176</td></tr><tr><td>OSG36</td><td>446</td><td>-99</td><td>544</td><td>-0.9</td><td>-0.3</td><td></td><td>-0.4</td><td>-20.9</td><td>375</td><td>-111</td><td>431</td></tr><tr><td>Pulkovo 42</td><td>24</td><td>-123</td><td>-94</td><td>0.0</td><td></td><td>0.2</td><td>0.1</td><td>1.1</td><td>28</td><td>-130</td><td>-95</td></tr><tr><td>SAD69</td><td>-56</td><td>-3</td><td>-38</td><td>0.1</td><td></td><td>-0.6</td><td>-0.2</td><td>-0.6</td><td>-57</td><td>1</td><td>-41</td></tr></table>

Remark: Pulkovo42 7-Parameter-Transformation values are valid for eastern Germany, while 3-Parameter-Transformation values are valid for Russia.

The transformation from a local/regional geodetic datum to the geocentric system can be done either by a complete readjustment including spatial observations (example: NAD83) or by transformation, the latter method being less laborious. Again, the transformation equations (6.47) are used, introducing either mean datum-shift parameters or (better) parameter values modeled as a function of position, e.g., as low-order polynomials. Corresponding parameter values or models are provided by the responsible agencies (e.g., by BKG Frankfurt a.M. for the transformation from the European national systems to ETRS89: http://www.crs-geo.eu), or they can be calculated together with the changes of coordinates. Residual differences between the two sets of coordinates may be determined also by refi ned transformation methods, e.g., by least-squares prediction, cf. also [7.3].

Of special interest is the datum transformation of ellipsoidal (geodetic) coordinates, which includes the transition from a conventional or best-fi tting ellipsoid to a geocentric one. From (6.49) we obtain the corresponding changes which occur in the ellipsoidal latitude, longitude, and height. Restricting ourselves to a spherical approximation and neglecting the (small) rotations and change of scale, we get (ellipsoidal formulas are given by DMA, 1987 and Ehlert, 1991):

$$
\begin{array} { r l } & { a \Delta \varphi = - \sin \varphi \cos \lambda X _ { 0 } - \sin \varphi \sin \lambda Y _ { 0 } + \cos \varphi Z _ { 0 } + a \mathrm { s i n } 2 \varphi \Delta f } \\ & { a \mathrm { c o s } \varphi \Delta \lambda = - \mathrm { s i n } \lambda X _ { 0 } + \mathrm { c o s } \lambda Y _ { 0 } } \\ & { \Delta h = \mathrm { c o s } \varphi \mathrm { c o s } \lambda X _ { 0 } + \mathrm { c o s } \varphi \mathrm { s i n } \lambda Y _ { 0 } + \mathrm { s i n } \varphi Z _ { 0 } - \Delta a + a \mathrm { s i n } ^ { 2 } \varphi \Delta f } \end{array} \biggr ] .
$$

Here, the sign of the translation vector

$$
\mathbf { X } _ { _ { 0 } } = { \left| \begin{array} { l } { X _ { _ { 0 } } } \\ { Y _ { _ { 0 } } } \\ { Z _ { _ { 0 } } } \end{array} \right| } = { \left| \begin{array} { l l } { X - { \overline { { X } } } } \\ { Y - { \overline { { Y } } } } \\ { Z - { \overline { { Z } } } } \end{array} \right| }
$$

has been changed (reduction!). All differences are formed in the sense “geocentric – local system”, resulting in the transformation

$$
\begin{array} { l } { \varphi = \overline { { \varphi } } + \Delta \varphi , \quad \lambda = \overline { { \lambda } } + \Delta \lambda , \quad h = \overline { { h } } + \Delta h \mathrm { a n d } } \\ { a = \overline { { a } } + \Delta a , \quad f = \overline { { f } } + \Delta f . } \end{array}
$$

Again, the changes in $\varphi , \lambda , h$ can be modeled and demonstrated in contour charts, provided a suffi ciently large number of identical points have been used. The accuracy of these transformations depends on the area under investigation and the number of points available in both systems. A few $\mathsf { m }$ accuracy has been achieved for continent-wide geodetic systems, and residuals of a few cm may be obtained at well surveyed local networks.

# 7.2 Vertical control networks

Traditionally, national vertical control networks have been established separately from horizontal control nets. This is due to the demand that heights have to be defi ned with respect to the gravity fi eld and a corresponding reference surface (e.g., geoid, quasigeoid) rather than to the ellipsoidal system used for horizontal positioning.

Vertical control networks are surveyed by geometric (also spirit or differential) leveling and occasionally also by hydrostatic leveling, cf. [5.5.4], the control points being designated as bench marks. According to the leveling procedure and the accuracy achieved, national geodetic surveys distinguish between different orders of leveling. First-order leveling is carried out in closed loops (loop circumferences of some $1 0 0 \mathrm { k m } )$ ) following the rules for precise leveling. An accuracy of $0 . 5 \dots 1 \ \mathrm { m m } \sqrt { s } \left( \mathrm { k m } \right)$ is achieved at double-run leveling (s is the length of the leveled line), but systematic effects may lead to error accumulation over long distances. The loops are composed of leveling lines connecting the nodal points of the network (Fig. 7.9). The lines, in turn, are formed by leveling runs that connect neighboring benchmarks (average spacing 0.5 to $2 ~ \mathrm { k m }$ and more). The fi rst-order leveling network generally is densifi ed by second to fourth-order leveling, with diminishing demands on accuracy.

![](images/e4599991fb1e833cee738f8c1a47861207038e4c7916b81be16b1c23c0a6392d.jpg)  
Fig. 7.9: Leveling network (principle).

Leveling lines generally follow main roads, railway lines, and waterways. The bench marks consist of bolts in buildings, bedrock, or on concrete posts. Long pipes have been set up in alluvial regions. Underground monuments are established in geologically stable areas in order to control the network stability with respect to variations with time. First-order networks should be reobserved at time intervals of some 10 years, as regional and local height changes can reach one mm/year and more, especially in areas which experience vertical crustal movements of tectonic, isostatic or man-made origin, cf. [8.3.4].

Prior to the adjustment of a leveling network, the observed raw height differences have to be transformed either to geopotential differences or to differences of normal or orthometric heights by taking surface gravity into account, cf. [6.4.1]. The adjustment then utilizes the loop misclosure condition of zero and is carried out either by the method of condition equations or, preferably, by the method of parameter variation.

First-order leveling networks were established in many countries between the 1860s and the 1950s when surface gravity along the leveling lines was not known. Hence, gravity reductions were either neglected completely or actual gravity was approximated by normal gravity, leading to normal or spheroidal orthometric heights. These path-dependent heights may differ from normal or orthometric heights by some mm (fl at terrain) to some dm (mountains). Today, surface gravity along the leveling lines is generally available by measurement or prediction, and can be taken into account.

The vertical datum of a national height system generally is defi ned by mean sea level (MSL) as derived from tide gauge records. The zero height surface running through the defi ning MSL depends on the choice of the height system, and is either a level surface close to the geoid (orthometric heights) or the quasigeoid (normal heights). In future, high-resolution geoid or quasigeoid models may also serve for the defi nition of the vertical datum, again being realized through the heights of fundamental bench marks. If based on MSL from different tide gauges, national height systems may differ by some dm to one m and more, between each other and from the geoid as a global reference surface. This is due to the effect of sea surface topography, which additionally causes network distortions if the vertical datum is constrained to MSL of more than one tide gauge, cf. [3.4.3].

Estimates of the differences between the vertical datum of different height systems are available from satellite positioning and global geoid models and from continent-wide leveling connected to tide gauges (Rapp, 1995b). For instance, the zero height surface of the North American Vertical Datum of 1988 is about $_ { 0 . 5 \mathrm { ~ m ~ } }$ below MSL at Amsterdam. In Europe, the national vertical datums have been derived from MSL records in the Mediterranean Sea, the North Sea, and the Baltic Sea. Taking the mean sea level in Amsterdam (used, e.g., in the Netherlands, in Germany, and in the European leveling net) as reference, MSL in Kronstadt (near St. Petersburg, Russia) is about $1 5 \ \mathrm { c m }$ higher, and zero-height surfaces derived from tide gauge records along the Mediterranean Sea are about 0.4 to $_ { 0 . 5 \textrm { m } }$ lower (Sacher et al., 1999).

We now shortly describe the development of the North American and the European leveling networks, as well as the German height system, being examples for classical regional and local vertical control nets.

![](images/b13bc59cc85f967df8f9afd4a92261112c69b542f076e5a982cb594334ce6875.jpg)  
Fig. 7.10: NAVD 88 leveling network, from Zilkoski et al. (1995).

Geodetic leveling in the United States began in the middle of the nineteenth century, and a fi rst network adjustment was performed in 1900. The adjustment of more than 100 000 kilometers of geometric leveling from the U.S.A. and from Canada provided the National Geodetic Vertical Datum of 1929 (NGVD29). Being constrained to the MSL of 26 tide gauges, network distortions of $5 0 \mathrm { c m }$ and more thus have been introduced into the results. After replacing destroyed bench marks and extensive re-leveling, a new adjustment of the leveling data of the U.S.A., Canada and Mexico was started in the 1970s, and resulted in the North American Vertical Datum of 1988 (NAVD88). The adjustment included more than 700 000 bench marks and was carried out in geopotential numbers, employing the Helmert-blocking technique. Heights are given as orthometric heights according to Helmert, see (6.84), and refer to MSL of now only one primary bench mark (Father Point, Rimouski, Quebec, Canada), Zilkoski et al. (1995). A national height modernization program is underway which will utilize an up-to-date regional gravitational geoid model, on the one hand, and a geoid model fi tted to GNSS/NAVD88 control points, on the other, for defi ning a vertical datum suitable for GNSS techniques.

The United European Leveling Net (UELN) has been formed by fi rst-order leveling lines of the European countries. Several re-adjustments have been carried out since 1954, with continuous quality improvement and network extension, the latest one being UELN95/98 (Fig. 7.11). The adjustments are performed in geopotential numbers, and normal heights are derived. The average accuracy of the leveling is about $1 . 1 \ \mathrm { m m } \ \sqrt { s } \ \mathrm { ( k m }$ ), and the standard deviations related to the datum point Amsterdam remain less than $_ { 0 . 1 \mathrm { ~ m ~ } }$ . The vertical datum is taken from MSL of the North Sea as determined in the period 1940 to 1958 at Amsterdam (Normal Amsterdamsch Peil NAP of 1950). The UELN is connected to a large number of tide gauges, which permits determination of sea surface topography around Europe, in addition to the datum differences between national vertical reference systems (see above). UELN represents the basis of the European Vertical Reference System (EVRS), which by combination with GNSS heights is embedded in the spatial reference system ETRS, cf. [7.3], Ihde et al.

![](images/80a530901c841ed82d4fe463fc3a557702bb58062ce38b9731f5bc3017ee5830.jpg)  
Fig. 7.11: United European Leveling Net (status 2008), courtesy BKG, Frankfurt a.M., Germany.

(2002). The latest realization of this integrated system is the reference frame EVRF2007, calculated in the zero-tide system. The datum of the UELN has been kept as good as possible by introducing the previous heights of 13 “datum points”, assumed to be not affected by temporal variations. Leveling data from the northern European land uplift area have been reduced to epoch 2000. In future, UELN will be extended to a kinematic height system by including vertical point velocities (Sacher et al., 2008).

First-order leveling in Germany started state-wide around 1865 and fi nally led to a national height system calculated from the raw leveling data, with the leveling of Prussia as the core network. The vertical datum was derived by connection to the Amsterdam normal tide gauge, representing mean high tide for the period 1683/1684 (Waalewijn, 1986). The zero height surface (Normal-Null, N.N.) was fi xed by a standard bench mark, established $3 7 . 0 0 0 \mathrm { ~ m ~ }$ above N.N. at the former Berlin observatory and since 1912 by a set of underground marks. Complete re-surveys were carried out from 1912 to 1960 and from 1980 to 1985 (only western Germany). These networks were adjusted as normal-orthometric heights: Deutsches Haupthöhennetz (DHHN). In eastern Germany, re-leveling was performed in the 1970s and adjusted as normal heights within the frame of the eastern European height system, where the vertical datum was taken from MSL at the tide gauge in Kronstadt near St. Petersburg: Höhennull (HN). Due to the different defi nitions of the vertical datum and the height system, systematic height differences between 8 and $1 6 ~ \mathrm { c m }$ were later found at the former boundary between western and eastern Germany. After 1990, a re-adjustment of the complete national network (loop diameter 30 to 80 km, more than 50 000 bench marks with mutual distance between 0.5 and $1 . 5 \mathrm { k m } )$ was carried out in geopotential numbers. The vertical datum is defi ned now by the geopotential number of the UELN86 nodal point Wallenhorst and thus refers to MSL at Amsterdam (see above): DHHN92, Fig. 7.12. Normal heights have been introduced as offi cial heights, referring to the quasigeoid as reference surface: Normalhöhennull (NHN), Weber (1995). Recent modernization includes re-survey of most leveling lines and connection to existing GNSS-networks and absolute gravity stations, a dedicated DHHN-GNSS network comprising about 250 stations was established at the beginning of the twenty-fi rst century.

Leveling networks are characterized by high accuracy, but systematic errors may accumulate over large distances. A severe handicap of classical leveling networks is the signifi cant loss of benchmarks with time due to human activities, and the manifold height changes occurring at local and regional scales. Due to the timeconsuming measurement procedure, repetition or restoration surveys are feasible only after longer time intervals, which leads to a rapid network decay. A more rapid establishment of vertical control networks has been achieved occasionally by trigonometric leveling, cf. [6.4.2], and a drastic change is now taking place by GNSS heighting in connection with high-resolution geoid or quasigeoid models, cf. [6.4.3]. In this way, vertical control networks are integrated in, and gradually substituted by 3D reference systems, cf. [7.3]. The time-consuming spirit leveling required for the establishment and maintenance of the classical vertical control networks may become mostly superfl uous. On the other hand, geometric leveling will maintain its importance over shorter distances, and especially in areas of recent crustal movements, such as regions of land subsidence and zones of Earthquake or volcanic activity, cf. [8.3.4].

![](images/32c258f8a157816c0f957250deab41aa23dc8a441c9d5574e935d5c74938544f.jpg)  
Fig. 7.12: Primary leveling network of Germany (DHHN92), courtesy BKG, Frankfurt a.M., Germany.

# 7.3 Three-dimensional networks

Starting in the end of the 1980s, GNSS techniques have more and more entered into geodesy and are now primarily used at all scales for positioning and navigation, cf. [5.2.5]. This has led to a drastic change at the establishment and maintenance of geodetic control networks which are now defi nitely $3 D$ and based on satellites as system carriers.

Nowadays, the global geodetic reference is well established and provided by the International Terrestrial Reference Frame (ITRF) being the realization of the International Terrestrial Reference System. The ITRF stations are given with their 3D geocentric coordinates (cm-accuracy) for a certain reference epoch, and with corresponding horizontal velocities, cf. [2.4.2]. The International GNSS Service (IGS) provides a powerful contribution to the ITRF and serves for densifying this global reference frame, cf. [5.2.5]. A multitude of GNSS surveys has already densifi ed or will in future densify this global reference frame, superseding the classical control networks. This process happens at local, regional or continent-wide dimensions, and has triggered a new defi nition and realization of national and supra-national geodetic reference systems, and strategies for integrating the existing control nets.

Immediately following the development of geodetic GPS and other GNSS methods, continent-wide (supra-national) and national 3D networks were established. Although a more or less homogeneous station-coverage is generally the goal, the distances between the observation sites in reality vary considerably. The station distribution depends, among others, on topography and on the state of economic development, and station distances consequently range from a few ten to some $1 0 0 ~ \mathrm { k m }$ and more. At least three stations per country have been often selected as a reference for further densifi cation and for the transformation of existing control networks, cf. [7.1]. The station sites are selected according to the requirements of GNSS observations (no visibility obstructions between $5 ^ { \circ }$ to $1 5 ^ { \circ }$ and $9 0 ^ { \circ }$ elevation, absence of multipath effects, no radio wave interference), cf. [5.2.5]. Generally the stations are monumented by concrete pillars, providing a forced centering for the GNSS antenna and a height reference mark. Eccentric marks are established in order to locally control horizontal position and height, and underground monuments are benefi cial for the long-term preservation of the network. Existing fi rst- and second-order control points may be used if they fulfi ll the GNSS requirements, otherwise the GNSS stations should be connected to the existing control networks by local surveys.

Although the strategies for establishing and maintaining these GNSS based reference networks differ, the following directions clearly can be identifi ed:

establishment of a large-scale (continent-wide, national) fundamental threedimensional network by GNSS campaigns, with proper system defi nition and connection to the International Terrestrial Reference Frame, . installation of a network of permanent GNSS stations,

• densifi cation of the fundamental network by GNSS methods, transformation of existing classical horizontal control network into the threedimensional system, connection of the 3D-reference system to the vertical control and gravity reference systems.

Dedicated GNSS campaigns are carried out for the determination of the 3D-coordinates of the network stations, employing relative positioning, cf. [5.2.5]. This strategy requires the inclusion of at least one reference station with coordinates given in the ITRF, but generally all ITRF and IGS stations (or control stations of a continent-wide reference system) in the survey region are introduced as reference (“fi ducial”) stations. Depending on the number of stations and available GNSS receivers (two-frequency geodetic type), either all stations are observed simultaneously or the network is divided into blocks that are observed sequentially (Fig.7.13). All observations made simultaneously during a given time interval are called a “session” (Snay, 1986). The duration of one session is between 8 and $2 4 \ \mathrm { h } ,$ , which permits determination of the ambiguity unknowns and a simultaneous solution for the station coordinates and tropospheric correction para meters (“multi-station” adjustment). The results of one session are highly correlated. Consequently, two or more sessions are generally carried out, leading to a total observation time of some days to one week. A “multi-session” adjustment then combines the results of several sessions. Optimization methods have been developed and may be employed for network planning and survey (Dare and Saleh, 2000).

By referencing the network to IGS stations and applying the IGS precise orbital data, the effect of reference station and orbital errors on the station coordinates is only at the few mm level. When different type GNSS receivers are employed in one campaign, corrections have to be applied for antenna phase-center differences. In addition, phasecenter variations have to be taken into account by calibration (Seeber et al., 1998). Longer observation periods increase the accuracy of the results, due to the changing satellite geometry and the reduction of residual tropospheric, multipath, and antenna effects. This is especially valid for the height component, where small satellite elevations improve the geometry of the solution but introduce larger tropospheric errors. Accuracies of $1 \mathrm { { \ c m } }$ and better are achieved now for the adjusted horizontal coordinates of fundamental network stations, and heights can be determined with an accuracy of 1 to $2 \mathrm { \ c m }$ .

![](images/68b3f3b0e609c608d95b0e5eb9313dbcd67c9df3ae72fb0bb059e6839f0417e9.jpg)  
Fig. 7.13: GNSS network constructed from individual blocks (principle).

Following the ITRF strategy, reference epochs are defi ned for the fi nal station coordinates of the fundamental networks, which may differ from the epoch of the ITRF stations introduced and from the time of the observation campaign. Consequently, reductions have to be applied which take the station velocities between the different epochs into account.

Permanent GNSS networks have increasingly been established since the 1990s at regional and local scales. They consist of “active” GNSS stations, equipped with geodetic GNSS receivers that continuously track all visible GNSS satellites with a high data rate (e.g., 1 s). Station distances vary considerably, ranging from about $1 0 0 ~ \mathrm { k m }$ to a few $1 0 0 ~ \mathrm { k m }$ at continent-wide networks, and 30 to $1 0 0 ~ \mathrm { k m }$ and more at national systems. Undisturbed visibility to the satellites is achieved by installing the antennas several m to $^ { 1 0 \mathrm { ~ m ~ } }$ above the ground on concrete pillars, steel grid masts, etc., or on the top of buildings. Permanent networks represent a continuous realization of the underlying supra-national or national geodetic reference system, thus serving for maintenance and for control of variations with time due to recent crustal movements. They represent a reference for all types of GNSS surveys carried out within the permanent network area, by making available the raw GNSS tracking data (code and carrier phase measurements) for the “reference” station of a “baseline”, Fig. 7.14. More sophisticated “Satellite Positioning Services” exploit the known geometry of the stations’ array to determine the ambiguities and to calculate baseline corrections for ionospheric, tropospheric, and orbit effects. Together with the station coordinates this allows the application of differential GNSS methods with a single receiver ( Wanninger, 2000). Real-time positioning with “baselines” is possible with cm-accuracy, and post-processing with long observation series may achieve a few mm precision, see below and [5.2.5], [6.2.1].

After the establishment of a national 3D geodetic reference frame, relative GNSSpositioning can be employed also for network densifi cation. While the fundamental network may be constructed with station distances of several $1 0 ~ \mathrm { k m }$ (corresponding to the fi rst-order trigonometric points), densifi cation nets with distances down to $1 0 ~ \mathrm { k m }$ (former second-order triangulation) may be useful for larger countries. The relative mode again requires two or more receivers and the connection to reference stations. If a network of permanent GNSS stations as realization of the national reference frame is available (telemetry data transfer to the users), differential GNSS methods can be applied. For short (few to $1 0 \ \mathrm { k m } ,$ ) baselines, a relative cm-accuracy can be achieved in quasi real-time after proper ambiguity solution. For longer baselines, the results are degraded by the distance-dependent errors of GNSS, and have to be improved by the corrections provided by the permanent network’s positioning service.

![](images/a4fba5a979c83753713bf6caa96ed12d7fb5581955bbd45c091eee45e0e40855.jpg)  
Fig. 7.14: GNSS network constructed from baselines to permanent GNSS stations (principle).

With Precise Point Positioning (PPP), an alternative to the relative method of DGNSS has been developed and could also be used for the establishment of geodetic 3D control networks (Zumberge et al., 1997; Ebner and Featherstone, 2008). This absolute method evaluates undifferenced dual-frequency pseudorange and carrier phase observations obtained with only one receiver, along with IGS precise orbits and satellite clock corrections in one mathematical model, for estimating station coordinates, tropospheric zenith path delays, receiver clock corrections, and ambiguities (Kouba and Héroux, 2001). Network adjustments (post-processing) of extended observation series (up to $2 4 \ \mathrm { h }$ ) deliver cm-accuracy for position, and clock corrections at the 0.1 ns level. The method can be extended by taking current corrections into account derived from a regional or local RTK (real-time kinematic) network. This strategy allows an immediate determination of carrier phase ambiguities, and delivers quasi-real-time cm-accuracy (Wübbena et al., 2005).

By connecting the 3D GNSS network to fi rst- and second-order trigonometric points, the existing classical horizontal control networks can be transformed into the threedimensional reference frame. A minimum of three identical points with coordinates given in both systems is required for a 7-parameter transformation, which may suffi ce for homogeneous networks of high precision, cf. [7.1]. Additional GNSS control points are needed if the classical networks contain larger distortions; the selection of these points depends on the network peculiarities, and usually more sophisticated transformation models will be necessary, including polynomial, least-squares, or spline approximation (Moritz, 1978). In this way, the local cm-accuracy of classical networks can be kept, and the effect of the network distortions can be reduced to the order of a few cm to dm over distances of some 10 to $1 0 0 ~ \mathrm { k m }$ . After the completion of the transformation to a 3D reference frame, the classical horizontal networks of lower order generally will no longer be maintained.

Space-geodetic and especially GNSS methods also give reason for a change with respect to the defi nition and realization of vertical reference systems. This is due to the fact that space-based techniques allow the determination of ellipsoidal heights with an accuracy comparable with the accuracy of spirit leveling, at least at distances larger than a few ten kilometers, cf. [6.4.3]. By combining with high-resolution global or local geoid/quasigeoid models, cf. [6.6], [6.7], another method for determining gravity-fi eld related heights thus is available. This forces the incorporation of the classical vertical control networks into the 3D reference frame. By including fi rst-order leveling benchmarks and tide gauges in the 3D network, the differences between the ellipsoidal heights and the heights of the national height system can be determined at selected points, i.e., the geoid or quasigeoid heights. These GNSS/leveling control points allow the national height system to be fi tted to a regional geoid or quasigeoid model, and they can be used to derive gravity-fi eld related heights (orthometric heights, normal heights) for all threedimensional reference stations. The vertical datum may be even defi ned by a global or regional geoid/quasigeoid model, with corresponding reductions of the heights given in the classical height system. The vertical control points now are an integrated part of the 3D reference frame, evenly distributed over the respective continent or nation and not restricted to the leveling lines. With increasing accuracy of the geoid-resp. quasigeoid-“reduction” of GNSS heights, the application of geometric leveling will be reduced to more local problems where mm-accuracy is required, cf. [7.2].

Finally, there is a tendency to also measure absolute gravity on the primary stations of a 3D reference frame. This will lead to fundamental geodetic control networks, providing 3D geodetic coordinates, gravity potential (and related height) and gravity for a certain epoch, and (as far as possible) corresponding long-term variations with time.

Some examples for the transition from the classical geodetic control networks to reference frames embedded in the global 3D system are given in the following, with the continent-wide reference systems introduced in the U.S.A., in South and Central America, and in Europe, and with the spatial reference frame established in Germany.

Since the 1980s, GPS-based methods rapidly entered into surveying and navigation in the U.S.A. Numerous adjustments of new GPS and existing terrestrial data led to a number of state High Precision Geodetic Networks (HPGN’s), with a local accuracy of around $5 \ \mathrm { c m } ,$ , but consistency problems across state lines. In addition, a Continuously Operating Reference Station (CORS) network was established in the mid-1990s by NGS, which is now operating with about 1600 stations in the U.S.A., its territories and a few foreign countries, Fig. 7.15. Based on the contributions of over 200 different institutions, CORS provides GNSS data consisting of carrier phase and code range measurements in support of 3D positioning, and allows a few cm-accuracy. These drastic changes triggered the establishment of a National Spatial Reference System (NSRS), superimposing or integrating the previous horizontal and vertical survey control. Consequently, a re-adjustment of horizontal positions and ellipsoidal heights for GPS stations in the contiguous United States was carried out, holding the CORS coordinates fi xed (ITRF geocentric datum!) and including only GPS measurements. ITRF- and NAD83-related coordinates NAD83(NSRS) have been produced, where the latter experienced changes of 0.2 to $1 \textrm { m }$ relative to NAD83(1986), Pearson (2011).

![](images/e48451f688144c0c4bde7f9bff347c1343868d76205dfc8a73ebc0e602da7351.jpg)  
Fig. 7.15: CORS station equipped with a Trimple Zephyr Geodetic Antenna, El Paso, TX, U.S.A., courtesy NGS (http://www.ngs.noaa.gov/CORS ).

In South America, a continent-wide densifi cation of the ITRF started in 1995, and was later extended to Central and North America: Sistema de Referencia Geocéntrico para las Américas (SIRGAS). The system has been fi rst realized through two measuring campaigns (1995, 2000), where simultaneous GPS observations over 10 days were carried out on some 60 resp. 200 stations well distributed over the sub-continent and the whole hemisphere, respectively; positions were calculated in ITRF2000 (Drewes et al., 2005). Since 2000, the continuously operating network (SIRGAS-CON) represents a third realization of this system, which is well connected to the global IGS net (Fig. 7.16.). It provides weekly solutions for the station positions and multi-annual solutions which contain linear station velocities, cf. [8.3.4]. SIRGAS also serves as a basis for the national reference frames recently established through GPS measurements, and for the transformation of the classical horizontal control networks in South America (generally given in the South American Datum 1969) into the global reference system (Sanchez and Brunini, 2009). A dedicated SIRGAS GPS campaign was carried out in 2000 which included leveling benchmarks and tide gauges, in order to derive a unifi ed height system for South America. This system shall be defi ned by a geoid potential value (national vertical datums now deviate by $_ { 0 . 5 \textrm { m } }$ and more from a common MSL) and realized by the geopotential numbers of the control points, based on SIRGAS ellipsoidal heights and a geoid model, as well as on readjustments of the existing national height networks (Sanchez, 2007).

![](images/4814d882f74e116109c4129b9a8c9855e2eae3fec952a25e02393435b072125f.jpg)  
Fig. 7.16: Reference frame SIRGAS-CON, station distribution (status 2010), courtesy DGFI München.

A European Reference Frame (EUREF) has been built up since the end of the 1980s, as realization of the European Terrestrial Reference System 1989 (ETRS89). This system is defi ned through the coordinates (1989.0) of the ITRF89 stations located on the “stable” (i.e., moving with the same plate velocity) part of the European tectonic plate, which allows the frame to remain unchanged over a longer time interval. ETRS was fi rst realized through the European Terrestrial Reference Frame 1989 (ETRF89), and continuously extended over the continent. The station positions were determined by successive GPS campaigns that included ITRF and IGS stations and generally included several countries. With ETRF2000 the network now covers nearly all of Europe, with station distances between 100 and $5 0 0 ~ \mathrm { k m }$ or more. Of special relevance is the EUREF Permanent Network (EPN) comprising more than 200 stations with continuously observing dual-frequency GPS and GPS/GLONASS receivers (Fig. 7.17). Providing hourly data, EPN contributes to IGS and densifi es it (Torres et al., 2009).

A European Unifi ed Vertical Network (EUVN) is under construction, and integrated into EUREF. The network now comprises about 200 stations determined since 1997 by dedicated GPS campaigns using one-week observation time. It includes EUREF sites, nodal points of the European leveling net UELN, tide gauges, and a number of permanent GNSS stations, with 3D coordinates, geopotential numbers and normal heights. EUVN thus will serve (at a few-cm accuracy level) to unify the different European height systems, and provide fi ducial points in order to fi t the European quasigeoid, cf. [6.4.3], to a unifi ed European height system. By extension to a kinematic height system, EUVN shall be used for monitoring large-scale vertical crustal movements and sea level changes (Kenyeres et al., 2000).

![](images/7f9edc83c2952a53cade50f15460a5b1f9a2260e2e57d4c2b4647906eef0aaab.jpg)  
Fig. 7.17: EUREF Permanent Network tracking stations (status 2012), courtesy C. Bruyninx EPN Central Bureau, Observatoire Royal de Belgique (http://www.epncb.oma.be/_trackingnetwork/ ).

In Germany, a 3D network related to ITRF and EUREF stations was established in 1991: Deutsches Referenznetz 1991 (DREF91). The network stations are mostly co-located with fi rstor second-order trigonometric points. The integration of DREF into the European reference frame is realized through the German Geodetic Reference Net (GREF), being part of the European GNSS Permanent Net and of IGS. Operated by BKG, it contains about 30 permanent stations, with an accuracy of $5 \mathrm { \ m m }$ in position and $1 0 ~ \mathrm { m m }$ in height, Fig. 7.18. The Satellite Positioning Service (SAPOS) of the State Survey Agencies breaks this DREF/GREF reference frame down to the state level. SAPOS is based on about 260 GPS reference stations (average distance $5 0 ~ \mathrm { k m }$ , accuracy $1 ~ \mathrm { c m } ^ { \prime }$ ), well distributed over the German states (Hankemeier et al., 1998), Fig. 7.19, Fig. 7.20. It serves for differential GNSS positioning by providing range corrections for real-time code or carrier phase measurements (meter- resp. cm-accuracy), and raw observation data for post-processing (sub-cm accuracy).

With respect to further network densifi cation and connection to existing control nets, the German state survey agencies went different ways. This led to a strategy for the development of a unifi ed geodetic spatial reference in Germany (AdV, 2006). According to this planning, the spatial reference shall consist of the geodetic base net and the SAPOS reference stations both defi ned in ETRS89, the fi rst-order vertical control points given in DHHN92, cf. [7.2], and the gravity control points given in DHSN96, cf. [7.4]. The base net stations shall have a maximum distance of $3 0 ~ \mathrm { k m }$ which corresponds to the average distance of the classical fi rstorder triangulation points, and well marked with respect to horizontal position and height. They shall be determined by geodetic satellite methods, precise leveling, and gravity measurements, with accuracy demands corresponding to the requirements for GREF, DHHN92, and DHSN96. Lower-order trigonometric control networks will be under the responsibility of the state survey administrations, and generally maintained only at a reduced level.

![](images/e30b55bcea4708dbd0be5b463f4508a30f1b60488a8df6c59ebb8eb6af4966bd.jpg)  
Fig. 7.18: German Geodetic Reference Net GREF (status 2009), courtesy BKG, Frankfurt a.M., Germany.

![](images/aa7a79a3f04f98f3237ff75302c051334442a575c4faccc798792fb0a525a0b3.jpg)  
Fig. 7.19: Satellite Positioning Service (SAPOS) of the German State Survey Administration (status 2011), courtesy Landesbetrieb Geoinformation und Vermessung Hamburg (http://www.hamburg. de/sapos).

![](images/473bcc47df36191ec46455a1734bfb1a05073f255e6015bd5173ee8fe4816e23.jpg)  
Fig. 7.20: SAPOS permanent GNSS station, courtesy Landesbetrieb Geoinformation und Vermessung Hamburg (http://www.hamburg.de/sapos).

# 7.4 Gravity networks

Gravity networks provide the frame for gravimetric surveys on global, regional, or local scales. They consist of gravity stations where gravity has been determined by absolute or relative methods. On a global scale, the gravity standard has been realized by the International Gravity Standardization Net 1971 (IGSN71), but absolute gravimeters now allow an independent realization, cf. [5.4.3].

National gravimetric surveys are based on a primary or base network, which in most cases is densifi ed by lower-order nets. The gravity base network stations should be evenly distributed over the area, with station distances varying between a few $1 0 ~ \mathrm { k m }$ to a few $1 0 0 ~ \mathrm { k m }$ depending on the size of the country. The station sites should be (as far as possible) stable with respect to geological, hydrological, and microseismic conditions. They should be permanently marked, and co-location with geodetic base-stations is advisable. Eccenter sites may serve for securing the center station and for controlling local height and mass changes. Horizontal position and height of the gravity stations should be determined with m- and mm- to cm-accuracy, respectively. Subsequent gravimetric densifi cation networks generally are co-located with horizontal and vertical control nets.

Absolute gravimeters generally are employed nowadays for the establishment of gravity base networks, partly in combination with relative gravity meters. Densifi cation networks are observed primarily with relative instruments, cf. [5.4.1], [5.4.2]. Relative gravimeters need to be calibrated, and repeated measurements are necessary in order to determine the instrumental drift. The use of several instruments reduces residual systematic effects. Relative gravimetry requires at least one absolute station in order to derive the gravity $^ { \prime \prime } \mathrm { d a t u m ^ { \prime \prime } }$ , and a calibration line for the control and improvement of the calibration factor. The establishment of gravity networks for geophysical and geodynamic investigations follows the same rules, but the distribution of the gravity stations is then determined by the geological structures or the geodynamic processes to be investigated, cf. [8.3.5]. The accuracy of primary gravity networks, established by absolute gravimeters or by a combination of absolute and relative gravimetry, is about $0 . 0 5 ~ \mu \mathrm { m } s ^ { - 2 }$ to $0 . 1 \ \mu \mathrm { m } \ s ^ { \dot { - } 2 } ,$ ; densifi cation networks may be accurate to 0.1… $0 . 5 \ \mu \mathrm { m } \ s ^ { - 2 }$ .

Gravity measurements on national scale started in the second half of the nineteenth century, triggered by growing demands from geodesy and geophysics. In the twentieth century, exploration geophysics and physical geodesy (geoid determination) became strong drivers for denser gravity fi eld surveying, based on accurate and reliable gravity reference networks. These demands led in many countries to the establishment of gravity base networks, which continuously improved through progress in technology.

In the U.S.A., the Coast and Geodetic Survey and its successor, the National Geodetic Survey (NGS), carried out numerous gravity surveys during the second half of the twentieth century, generally within the frame of dedicated programs (statewide surveys, surveys along leveling lines, gravimeter calibration lines, etc.). A country-wide gravity network was established in 1976/1979 by LaCoste and Romberg gravimeters and constrained to the absolute standard. A running NGS absolute gravity program (jointly with NIMA Geospatial Sciences Division) is covering the country with a multitude of absolute gravity measurements (comprising now several hundred absolute gravity sites), serving as national gravity reference network and for the studies of vertical crustal movements, among others (Peter et al., 1989). In Canada, the primary control points of the Canadian Gravity Standardization Net will be replaced by the Canadian Absolute Gravity Array sites, co-located with GNSS reference sites (Fig. 7.21). Following previous repeated absolute gravity observations, regular resurveys of the array stations will contribute to the investigation of sea-level rise, post-glacial rebound, and tectonic deformation, cf. [8.3.5].

![](images/decf3a5036840318a5534d152a98198a17e08b5aa55f826f746c306d984deee1.jpg)  
Fig. 7.21: Canadian Absolute Gravity Array and Base Network (status 2010), courtesy National Resources Canada Geodetic Survey Division (http://www.geod.nrcan.gc.ca/edu/gravi_e.php).

![](images/57339b492d99d534989d8bf3ad211dc45c3eaa67dde972ecc63e2890c9f910c8.jpg)  
Fig. 7.22: Primary gravity net (red circles) of Germany (DHSN96), with German gravity base net (DSGN94) stations (blue circles), courtesy BKG, Frankfurt a.M., Germany.

In Germany, gravity base networks and densifying networks were established since the $1 9 3 0 s ,$ employing relative pendulum instruments and gravity meters, and tied to the Potsdam absolute gravity value. Absolute gravimetry was introduced in 1976/1977 in order to establish a combined absolute/relative base network in western Germany which was extended to eastern Germany and completely re-measured in 1994/1995: Deutsches Schweregrundnetz 1994 (DSGN94). The network consists of 30 stations (one center and at least two eccentric points) that were observed with an absolute gravimeter FG5. Repeated observations and relative ties (several gravimeters of type LaCoste and Romberg and Scintrex) served for investigations of accuracy $( 0 . 0 5 ~ \mu \mathrm { m } \ : s ^ { - 2 } )$ and reliability (Torge et al., 1999). A fi rst-order densifi cation net (average station distance $3 0 ~ \mathrm { k m } )$ was observed with several relative gravimeters (1978–1982, 1994), Fig. 7.22. Further densifi cation down to a few km has been realized or is in progress.

# 8 Structure and Dynamics of the Earth

As discussed in the previous chapters, geodesy covers the determination of the Earth’s fi gure, its external gravity fi eld, and its orientation in space, which results in timedependent models for the geometry, the gravity fi eld and the orientation of the Earth, see also [1]. As a part of the geosciences (geophysics including oceanography, hydrology and meteorology, geology, petrology, mineralogy, geochemistry and others), geodesy thus provides direct information or boundary conditions for the development of static and dynamic geophysical Earth models. These models, in turn, deliver signifi cant information for the planning of geodetic networks and space missions, and for proper reduction of observations.

Global geophysical Earth models are mainly based on a radial structure of physical properties, and presuppose hydrostatic equilibrium [8.1]. These assumptions are not valid for the upper (and partly also for deeper) layers of the Earth, where geodynamic processes play an important role [8.2]. The contributions of geodesy to research in geodynamics are demonstrated by examples from Earth rotation variations, sea level changes, recent crustal movements, and temporal gravity changes [8.3].

From the extensive geophysical literature, we mention the classical work of Jeffreys (1970) and the textbooks by Fowler (2005) and Lowrie (2007). The interrelations between geodesy and geophysics have been treated early in Heiskanen and Vening-Meinesz (1958), see also Lambeck (1988) and Moritz (1990). For the state of geophysical data collection and parameter estimation, we refer to Ahrens (1995) and Groten (2004).

# 8.1 The geophysical Earth model

Various observations show that the Earth does not posses a homogeneous structure:

The mass $M$ of the Earth as derived from the geocentric gravitational constant $G M ,$ cf. [4.3], and the constant of gravitation $G ,$ cf. [2.1], amounts to $M = 5 . 9 7 3$ $\times 1 0 ^ { 2 4 }$ kg. With the volume of the Earth ellipsoid $1 0 8 3 \times 1 0 ^ { 1 8 } \mathrm { m } ^ { 3 } .$ , we obtain the mean density

$$
\rho _ { { \mathrm { m } } } = 5 . 5 1 5 \times 1 0 ^ { 3 } { \mathrm { k g } } { \mathrm { m } } ^ { - 3 } .
$$

As the density of the Earth’s crust only amounts to $2 . 7 . . . 2 . 9 \times 1 0 ^ { 3 } \mathrm { k g } \mathrm { m } ^ { - 3 } ,$ density must increase toward the interior of the Earth.

• Astronomic and geodetic observations of the lunisolar precession, cf. [2.3.2], deliver the dynamic (mechanical) ellipticity (Fukushima, 2003):

$$
H = \frac { C - \overline { { A } } } { C } = 3 . 2 7 3 8 \times 1 0 ^ { - 3 } , \quad \overline { { A } } = \frac { 1 } { 2 } ( A + B ) .
$$

A, $B ,$ and $C$ are the equatorial and polar moments of inertia of the Earth, cf. [3.3.4]. With the dynamical form factor provided by satellite geodesy, cf. [4.3],

$$
J _ { _ { 2 } } = { \frac { C - { \overline { { A } } } } { a ^ { 2 } M } } = 1 0 8 2 . 6 3 \times 1 0 ^ { - 6 } ,
$$

we obtain the moment of inertia with respect to the rotational axis

$$
C = 0 . 3 3 0 7 0 1 a ^ { 2 } M .
$$

If the Earth were a homogeneous sphere, we would have $C = 0 . 4 \ a ^ { 2 } \ M .$ This again indicates a density increase with depth.

• Seismology shows that the Earth has a shell-like structure, with the shell boundaries being defi ned by discontinuities of the seismic waves velocities.

With the velocities of the seismic waves being known, and under the assumption of hydrostatic equilibrium, density, gravity, and pressure inside a spherically layered Earth model can be calculated as a function of the radial distance from the Earth’s center of mass. Here, the assumption of hydrostatic pressure in the Earth’s interior is justifi ed by the fact that the Earth originally existed in a liquid state. In that case, the pressure depends only on the weight of the masses lying above, and it increases toward the center of the Earth.

Seismology determines the velocities of the primary (compression) and the secondary (shear) seismic waves, $V _ { p }$ and $V _ { s }$ . From these velocities the seismic parameter

$$
\varPhi = \frac { K } { \rho } = { v _ { p } ^ { 2 } - \frac { 4 } { 3 } v _ { s } ^ { 2 } }
$$

is derived, where $K$ is the bulk modulus (compressibility) and $\rho$ is density. $K$ is defi ned as the ratio between the hydrostatic pressure and the dilation experienced by a body under this pressure. The relationship between changes of pressure $p$ and density is given by

$$
d \rho = { \frac { 1 } { \phi } } d p .
$$

Under hydrostatic equilibrium, the increase of pressure with depth depends on the weight of the additional vertical mass column. With the radial distance $r ,$ the fundamental hydrostatic equation reads

$$
d p = - g ( r ) \rho ( r ) d r ,
$$

where the minus indicates that pressure decreases with increasing radius. Finally, from (8.4) and (8.5) we obtain the relation between height and density changes (Adams-Williamson equation):

$$
\frac { d \rho } { d r } = - \frac { g ( r ) \dot { \rho ( r ) } } { \phi ( r ) } .
$$

According to (3.52), the radial change of the gravity potential $W$ is given by

$$
d W = - g ( r ) d r .
$$

Inserting (8.7) into (8.5) yields

$$
d p = \rho ( r ) d W .
$$

Hence, the surfaces of equal pressure (isobaric surfaces) coincide with equipotential surfaces and, after (8.4), also with surfaces of equal density.

Starting from density and gravity values on the Earth’s surface, density, pressure and gravity inside the Earth can be calculated iteratively, using (8.3), (8.4) and (3.22), (3.23). Here, we use the total mass and the polar moment of inertia as boundary conditions. Corresponding spherically symmetric Earth models based on seismic data consist of several layers characterized by chemical and physical properties (composition, pressure, temperature), and are based primarily on the results of seismology (seismic travel times from body waves and surface waves, free oscillation frequencies). The velocities, or the velocity gradients, of the seismic waves change abruptly at the boundaries of the layers (discontinuity surfaces or zones), as does density (Fig. 8.1). Inside one layer, density increases smoothly and reaches about $1 3 ~ 0 0 0 ~ \mathrm { k g } \mathrm { m } ^ { - 3 }$ at the Earth’s center. Gravity remains nearly constant within the Earth’s mantle and decreases almost linearly to zero in the core. Pressure increases continuously with depth. The Earth models developed by Bullen (1975) and the Preliminary Earth Model (PREM) from Dziewonski and Anderson (1981) have gained special importance.

The layered structure of the Earth is shown in (Fig. 8.2). The Earth’s crust (average thickness over the continents and the oceans is about $2 4 \mathrm { k m } )$ is the uppermost layer and is characterized by a complex structure. It is separated from the upper mantle by the Mohorovicˇic´ discontinuity. Lateral density variations are pronounced in the crust, but are found also in the upper mantle, cf. [8.2.1]. The crust and the uppermost part of the mantle (also called the lid of the low-velocity layer beneath it) behave approximately rigidly, they are part of plate tectonic motions, cf. [8.2.3]. The lower mantle starts at a depth of 650 to $6 7 0 \mathrm { k m }$ and is separated from the core at $2 8 9 0 \mathrm { k m }$ depth, through the Wiechert-Gutenberg discontinuity. The liquid outer core extends to $5 1 5 0 { \mathrm { k m } } ,$ , followed by the solid inner core.

The density distribution of these Earth models can also be tested by comparing its elasticity parameters with the results obtained from the observation of natural oscillations and (to a limited extent) Earth tides, cf. [8.3.6]. The free oscillations especially provide an important constraint on the models.

More refi ned models have to take the deviations from spherical symmetry into account, as well as departures from hydrostatic equilibrium. These deviations are clearly indicated by the odd zonal and the tesseral harmonic coeffi cients of the gravity potential, cf. [3.3.4], and by other geophysical observations. We remember that the seconddegree harmonic coeffi cients in the gravity fi eld reveal the main deviations of the Earth’s fi gure from a sphere, i.e., the polar and the equatorial ellipticity, cf. [3.3.4]. The latter one is signifi cantly smaller than the fl attening at the poles, as demonstrated by the two nearly equal equatorial moments of inertia $A = 0 . 3 2 9 6 1 5 a ^ { 2 } M$ and $B = 0 . 3 2 9 6 2 2 a ^ { 2 } M ,$ where the larger principal axis of inertia is directed to about $1 5 ^ { \circ } \mathrm { W }$ longitude. Refi ned geophysical Earth models that take the ellipsoidal form and the rotation of the Earth into account may use the level ellipsoid as a good approximation for the external boundary surface, cf. [4.2.1].

![](images/8cd1d8538ad1fc1f94b59dd4e193b0570c277939b5778314989d55fb48a82bed.jpg)  
Fig. 8.1: Density $\rho \left( 1 0 ^ { 3 } \mathrm { k g } / \mathrm { m } ^ { 3 } \right) .$ , gravity $g ( \boldsymbol { \mathsf { m } } / \boldsymbol { \mathsf { s } } ^ { 2 } ) .$ , and pressure $p$ with $( 1 0 ^ { 1 1 } \mathrm { P a } )$ inside a spherically symmetric Earth model (PREM), after Dziewonski and Anderson (1981).

![](images/e25bb29fd517189322d1560ee7600e7d5cf6d70e41a0b415d9152c8f637a38bc.jpg)  
Fig. 8.2: Spherical Earth model (PREM), with homogeneous shells separated by discontinuity zones (D.), not to scale, after Dziewonski and Anderson (1981).

A global deviation from hydrostatic equilibrium is indicated by the fl attening of a rotating spheroidal body in equilibrium, composed of density layers that are approximately ellipsoidal. A differential equation derived by Clairaut (1743) provides the fl attening of a corresponding layer as a function of its radius. The solution relates the dynamic ellipticity $H = 1 / 3 0 5 . 4 5$ with the hydrostatic fl attening $f _ { _ h }$ and the geodetic parameter $m \left( 4 . 5 0 \right)$ :

$$
H = { \frac { f _ { h } - { \frac { 1 } { 2 } } m } { 1 - { \frac { 2 } { 5 } } { \sqrt { \frac { 5 m } { 2 f _ { h } } } } - 1 } } \cdotp
$$

Inserting the observed values for $H$ and $m$ results in hydrostatic fl attening values around 1/299.8, which differ signifi cantly from the value 1/298.25 derived directly from satellite orbit analyses, cf. [4.3], Denis et al. (1997).

The deviation of the observed from the hydrostatic value may be attributed to a “fossil” fl attening of the lower mantle, which developed when the Earth’s rotational velocity was larger and which is not compensated yet. The still incomplete recovery of the ancient ice loads at the polar caps may be another explanation.

# 8.2 The upper layers of the Earth

Large deviations from the spherically symmetric Earth model are found in the Earth’s crust and upper mantle [8.2.1]. Topographic mass excesses (mountains) and defi ciencies (oceans) are, to a large part, compensated by the underlying masses, which leads to isostatic equilibrium [8.2.2]. The theory of plate tectonics introduces (nearly) rigid lithospheric plates that move against each other, causing crustal deformations, especially at the plate boundaries [8.2.3]. Since the gravity fi eld refl ects the distribution of the terrestrial masses, it provides an essential constraint in the development of crust and mantle models [8.2.4].

# 8.2.1 Structure of the Earth’s crust and upper mantle

The heterogeneous structure of the uppermost layers of the Earth is recognized by the distribution and composition of the topographic masses. There is a pronounced difference between the mean elevation of the continents (about $0 . 5 ~ \mathrm { k m } ^ { \prime }$ ) and the mean depth of the oceans (about $4 . 5 \mathrm { k m }$ ). Ocean depths increase with growing distance from the ocean ridges (mean depth around $2 . 5 \ \mathrm { k m }$ ) due to thermal cooling and contraction of the oceanic lithosphere with sea-fl oor spreading, cf. [8.2.3]. Consequently, the age of the oceanic crust is 200 million years, at most, while the continental crust dates back about 4 billion years (Cazenave, 1995).

The crust is composed of a variety of sedimentary, igneous (effusive and intrusive), and metamorphic rocks. Density changes occur primarily between different types of rock, but larger density variations are also found within the same rock material, especially in sediments. Density estimates are based on surface rock samples, borehole probes, and the relationship between density and seismic wave velocities (Mueller, 1974). The mantle has been investigated mainly by seismic methods, and three-dimensional models are now available from seismic tomography. Large-scale lateral variations of the P- and S-wave velocities are found here, correlated with zones of density and temperature anomalies (Dziewonski and Woodhouse, 1987).

The structure of the Earth’s crust and upper mantle may be briefl y described as follows (Fig. 8.3):

Sediment layers with highly varying thickness are found in the uppermost stratum in large parts of the crust. Seismic wave velocities and rock densities (average value $2 4 0 0 ~ \mathrm { k g } \mathrm { m } ^ { - 3 }$ for consolidated sandstone) vary considerably in this zone. In continental areas, the next lower layer of the upper crust consists mainly of acidic rocks such as granite (mean density $2 7 0 0 ~ \mathrm { k g } \mathrm { m } ^ { - 3 } ,$ ); primary wave velocities vary between 5.9 and $6 . 3 \ \mathsf { k m } \mathsf { s } ^ { - 1 }$ . The lower crust is composed of basic rocks such as basalt and gabbro (mean density $2 9 0 0 ~ \mathrm { k g } \mathrm { m } ^ { - 3 } ,$ .

![](images/4029dfc3b083295c4b660a791be4775fdd37d88e2dfac29708d8275c7879dd11.jpg)  
Fig. 8.3: Structure of the Earth’s crust with rock densities $( \mathrm { k g / m ^ { 3 } } )$ and velocities of seismic primary waves.

Wave velocities exceed $6 . 5 ~ \mathsf { k m } \mathsf { s } ^ { - 1 }$ and gradually increase to more than $7 ~ \mathrm { k m } \varsigma ^ { - 1 }$ . The boundary between the upper and the lower crust (Conrad discontinuity) is marked only in some parts of the continents, at depths of 10 to $2 0 ~ \mathrm { k m }$ . Beneath the oceans, consolidated sediments and basalt lava fl ows are found in the upper part of the crust above a basaltic layer of 6 to $7 \mathrm { k m }$ thickness (Tanimoto, 1995).

A sharp (over a few km) change in seismic velocity $( \mathsf { v } _ { p } > 7 . 8 \ \mathsf { k m } \mathsf { s } _ { 2 } ^ { - 1 } )$ ) is found at an average depth of $3 5 ~ \mathrm { k m }$ on the continents and $1 0 ~ \mathrm { k m }$ on the oceans. This Mohorovicˇic´ discontinuity (Moho) defi nes the boundary between crust and mantle. Ultrabasic rocks (peridotite, with olivine as the main mineral constituent) are assumed to be located below the Moho, with a density of 3300 to $3 4 0 0 ~ \mathrm { k g } \mathrm { m } ^ { - 3 }$ . The depth of the Moho is closely related to topography. On the continents, it may be less than $2 0 ~ \mathrm { k m }$ (e.g., at the Afar hotspot), reaching about 30 to $4 0 ~ \mathrm { k m }$ at old shields and platforms. Cenozoic mountain belts (Alps, Rocky Mountains, Himalaya) are characterized by a crustal thickness of 60 to $8 0 ~ \mathrm { k m }$ . Beneath the oceans, the crustal thickness is more constant. An extremely thin crust of a few kilometers is found at slow spreading and fracture zones, while a thick crust of about $2 0 ~ \mathrm { k m }$ may appear where hotspots (mantle plumes) are located under ridge axes, as in southern Iceland. These variations of crustal thickness are mainly due to isostasy and plate tectonics, cf. [8.2.2], [8.2.3].

Three-dimensional models of the crust are based on seismic and non-seismic data. They contain information on the subsurface spatial distribution and density of ice and water, soft and hard sediments, and the upper, middle and lower crust. The global CRUST 2.0 model (U.S. Geological Survey) provides a horizontal resolution of $2 ^ { \circ } \times 2 ^ { \circ }$ ; the accuracy of the sediment and crustal thickness is estimated to $1 ~ \mathrm { k m }$ and $5 \mathrm { k m }$ , respectively (Mooney et al., 1998; Tenzer et al., 2009). More detailed crustal models are available for several parts of the world, e.g., for Europe (EuCRUST-07: $1 5 ^ { \prime } \times 1 5 ^ { \prime }$ grid, sediments and two layers of the crystalline crust), Tesauro et al. (2008).

# 8.2.2 Isostasy

When considering the topographic masses and ocean waters as deviations from hydrostatic equilibrium, the removal of topography and the fi lling of the oceans should create an equilibrium fi gure, with a gravity fi eld approximately coinciding with the normal gravity fi eld, cf. [4.2.2]. However, from the systematic behavior of the residual gravity fi eld quantities, it follows that the visible mass excesses and defi ciencies are, to a large part, compensated by a corresponding mass distribution in the interior of the Earth (Heiskanen and Vening-Meinesz, 1958; Watts, 2001).

Already during the arc measurement in Peru, cf. [1.3.2], Bouguer discovered that the defl ections of the vertical as computed from the masses of the mountains were larger than the observed values. In the nineteenth century, the Survey of India (G. Everest) revealed signifi cant differences between observed and calculated defl ections of the vertical caused by the Himalaya Mountains, the computed values being several times larger than the observed ones. This observation was the basis for the theory of isostasy and the isostatic models developed by Airy and Pratt (see below).

The large-scale behavior of the Bouguer anomalies, cf. [6.5.3], is another indication for the compensation of the visible mass anomalies. In mountainous areas, the Bouguer anomalies are generally negative, reaching values as low as $- 2 0 0 0 ~ { \mu \mathrm { m } } s ^ { - 2 } ,$ while positive values (up to $4 0 0 0 \ \mu \mathrm { m } \ s ^ { - 2 } )$ are common over the oceans. A correlation with the mean height or depth (mean value calculated over a dimension of several $1 0 0 ~ \mathrm { k m } )$ can be demonstrated and in many parts of the world approximated by a regression of $- 1 0 0 0 ~ { \mu \mathrm { m } } ~ { \mathsf { s } } ^ { - 2 } / 1 0 0 0 ~ \mathrm { m }$ height, and $+ 1 0 0 0 ~ \mu \mathrm { m } { \sf s } ^ { - 2 } /$ $1 0 0 0 \mathrm { ~ m ~ }$ depth. Finally, the geoid heights produced alone by the topographic masses would reach values of up to about $\pm 5 0 0 \mathrm { ~ m ~ }$ (Helmert, 1884), whereas the observed values hardly exceed $1 0 0 ~ \mathrm { { m } }$ .

The model of isostasy is used to explain these observations. It postulates that the topographic masses (excess masses on the continents, defi cit masses on the oceans) are compensated in such a way that hydrostatic pressure equilibrium is achieved at a certain depth of compensation. The compensation depends on the quantity of the topographic load and may be achieved by different mechanisms. Loads of several $1 0 \mathrm { k m }$ to about $1 0 0 ~ \mathrm { k m }$ horizontal dimensions are supported by the strength of the lithosphere and not isostatically compensated, while larger loads generally lead to an elastic fl exure of the lithosphere and corresponding compensation. Therefore, large-scale topographic features of several $1 0 0 ~ \mathrm { k m }$ dimension and more are generally in isostatic equilibrium.

Incomplete isostatic compensation is found in the areas of strong pleistocene glaciation (North America and Fennoscandia), at structures of plate tectonics, and in some mountain areas. In the fi rst case, the melting of the ice masses (between about 20 000 and 10 000 years B.C.) after the Pleistocene has caused an isostatic imbalance, which is still compensated by postglacial rebound (glacial isostatic adjustment). The resulting sea level changes, land uplift rates and gravity variations are observed using different terrestrial and space techniques, and provide information on the viscosity of the Earth’s mantle, cf. [8.3.3]−[8.3.5]. Isostatic mass transports also happen at tectonic plate boundaries as characterized by ocean ridges, deep-sea trenches, and continental collision zones (mountain building), which consequently are not in a perfect state of equilibrium, cf. [8.2.3]. Mountains may also become overcompensated by large erosion, and as a consequence a vertical uplift will occur.

The classical isostasy models of Airy and Pratt are based on the assumption that isostatic compensation takes place locally in vertical columns only. Utilizing the hydrostatic equation (8.5), the condition of isostasy then reads (with $g = { \mathrm { c o n s t . } }$ )

$$
\displaystyle \int _ { H + T } ^ { H } \rho d z = \mathrm { c o n s t . } ,
$$