Differentiating (6.4), one gets

$$
n r \cos \psi \mathrm { d } \psi + r \sin \psi \mathrm { d } n + n \sin \phi \mathrm { d } r = 0 ,
$$

or

$$
r n \cos \psi \left( \mathrm { d } \psi + \frac { \mathrm { d } r } { r } \tan \psi \right) = - r \sin \psi \mathrm { d } n ,
$$

which, with (6.5), gives

$$
\mathrm { d } z = - { \frac { \mathrm { d } n } { n } } \tan \psi .
$$

Another way of writing (6.4) is

$$
\tan \psi = \frac { r _ { 0 } n _ { 0 } \sin z _ { 0 } } { \left( r ^ { 2 } n ^ { 2 } - r _ { 0 } ^ { 2 } n _ { 0 } ^ { 2 } \sin ^ { 2 } z _ { 0 } \right) ^ { 1 / 2 } } ,
$$

and substituting it into Equation (6.7), one finally gets, after integration,

$$
R = r _ { 0 } n _ { 0 } \sin z _ { 0 } \int _ { 1 } ^ { n _ { 0 } } \frac { \mathrm { d } n } { n \left( r ^ { 2 } n ^ { 2 } - r _ { 0 } ^ { 2 } n _ { 0 } ^ { 2 } \sin ^ { 2 } z _ { 0 } \right) ^ { 1 / 2 } } ,
$$

which is an exact equation, but assumes that one knows the variation of $n$ with $r$ or $r = r ( n )$ . This is not directly available from observations, and one would need to use a model. So, in practice, what is useful is to reduce (6.8) to a simpler formulation and later consider some integrals as parameters to be determined.

# 6.1.3 The Laplace formula

Let us re-write (6.8) as

$$
R = \sin z _ { 0 } \int _ { 1 } ^ { n _ { 0 } } \frac { \mathrm { d } n } { n ( ( r n / r _ { 0 } n _ { 0 } ) ^ { 2 } - \sin ^ { 2 } z _ { 0 } ) ^ { 1 / 2 } } ,
$$

and introduce two small parameters. The first is the refractivity on the ground, $\alpha = n _ { 0 } - 1$ . Applying the Gladstone–Dale law, which states that for small densities the refractivity is proportional to the density of the gas, and calling $\rho$ the relative density with respect to the density on the ground, one has

$$
n - 1 = ( n _ { 0 } - 1 ) \rho = \alpha \rho .
$$

Setting $h$ , the height with respect to the ground, as

$$
r = r _ { 0 } + h ,
$$

one gets

$$
\begin{array} { l } { \displaystyle \left( \frac { n r } { n _ { 0 } r _ { 0 } } \right) ^ { 2 } = \left( \frac { 1 + \alpha \rho } { 1 + \alpha } \right) ^ { 2 } \left( 1 + \frac { h } { r _ { 0 } } \right) ^ { 2 } } \\ { = 1 + \displaystyle \frac { 2 h } { r _ { 0 } } + 2 \alpha \left( \rho - 1 \right) + \cdot \cdot \cdot } \\ { = 1 + 2 \eta } \end{array}
$$

in which $2 \eta$ stands for the increment to 1. With these parameters, one has

$$
R = \sin z _ { 0 } \int _ { 0 } ^ { 1 } \frac { \alpha \mathrm { d } \rho } { ( 1 + \alpha \rho ) \sqrt { 1 - \sin ^ { 2 } z _ { 0 } + 2 \eta } } ,
$$

or, after replacing $\cos ^ { 2 } z _ { 0 }$ by $1 / ( 1 + \tan ^ { 2 } z _ { 0 } )$ and developing $R$ with respect to small quantities $\alpha$ and $\eta$ , one obtains

$$
R = \alpha \tan z _ { 0 } \int _ { 0 } ^ { 1 } \left( 1 + \alpha \rho \right) \left( 1 - \eta \left( 1 + \tan ^ { 2 } z _ { 0 } \right) \right) \mathrm { d } \rho .
$$

Let us remark that

$$
\int _ { 0 } ^ { 1 } \eta \mathrm { d } \rho = \int _ { 0 } ^ { 1 } \frac { h } { r _ { 0 } } \mathrm { d } \rho + \alpha \int _ { 0 } ^ { 1 } \left( \rho - 1 \right) \mathrm { d } \rho .
$$

The first integral can be integrated in parts

$$
\int _ { 0 } ^ { 1 } \frac { h } { r _ { 0 } } \mathrm { d } \rho = \left[ \frac { h \rho } { r _ { 0 } } \right] _ { 0 } ^ { 1 } + \frac { 1 } { r _ { 0 } } \int _ { 0 } ^ { \infty } \rho \mathrm { d } h .
$$

Since $h = 0$ when $\rho = 1$ , the term within brackets is null. The second integral is the scale factor $L$ of the atmosphere. Let us now call $\beta = L / r _ { 0 } = p / \delta _ { 0 } r _ { 0 }$ , $p$ being the pressure and $\delta _ { 0 }$ the air density at the site. Then we obtain after some simplifications

$$
R = \alpha ( 1 - \beta ) \tan z _ { 0 } - \alpha \left( \beta - \frac { \alpha } { 2 } \right) \tan ^ { 3 } z _ { 0 } .
$$

This is the Laplace formula, usually written

$$
R = A \tan z _ { 0 } - B \tan ^ { 3 } z _ { 0 } ,
$$

where $A = \alpha ( 1 - \beta )$ and $B = \alpha ( \beta - \alpha / 2 )$ .

# 6.1.4 Dependence on physical parameters

A simple look at the meaning of $A$ and $B$ shows that they depend upon the density of the air at the site, that is on temperature and pressure. Furthermore the refractive indices depend on the wavelength. We shall examine how these parameters affect $R$ , as well as some other smaller effects. Several approaches have been followed, and the resulting refraction tables were published. The most complete were published by the Pulkovo Observatory (1985), and then discussed by Guseva (1987), who found that these tables closely correspond to the mean atmospheric structure under a variety of observational conditions, and significantly reduce systematic errors of refraction determinations. These were put in the form of analytical expressions with a few short tables by the Bureau des Longitudes (Simon et al., 1996), and the following discussion is based upon this last work (note, however, that misprints for $f ( z _ { 0 } )$ and $g ( z _ { 0 } )$ have been corrected here).

# 6.1.4.1 Temperature and pressure

The well-known Boyle’s law of perfect gases is only a first approximation to the variation of density, and consequently of $\alpha$ . One starts with the Laplace formula for normal conditions, that is:

- temperature $t \colon t _ { 0 } = 1 5 ^ { \circ } \mathrm { C }$ - pressure $p \colon p _ { 0 } = 1 0 1 3 2 5 \mathrm { P a }$ (pascals) - wavelength λ: $\lambda _ { 0 } = 0 . 5 9 0 \mathrm { n m }$ - partial water vapor pressure $f \colon f _ { 0 } = 0 \mathrm { P a }$ .

Then,

$$
\begin{array} { l } { \alpha _ { 0 } = 0 . 0 0 0 \ 2 7 7 \ 1 1 7 \ ( = 5 7 \mathrm { { } } _ { . } ^ { \prime \prime } 1 5 9 5 ) } \\ { \beta _ { 0 } = 0 . 0 0 1 3 0 3 7 } \end{array}
$$

and the Laplace formula is:

$$
R _ { 0 } = 6 0 _ { \cdot } ^ { \prime } 2 3 6 \tan z _ { 0 } - 0 \mathrm { : } 0 6 7 5 \tan ^ { 3 } z _ { 0 } .
$$

The corrected formulae for $R$ at temperature $t$ (in degrees Celsius) and pressure $p$ (in pascals) as deduced from the Pulkovo tables is

$$
R ( t , p ) = R _ { 0 } \frac { p } { p _ { 0 } } \frac { 1 . 0 5 5 2 1 2 6 } { 1 + 0 . 0 0 3 6 8 0 8 4 t } F G ,
$$

with

$$
\begin{array} { l } { F = [ 1 - 0 . 0 0 3 5 9 2 ( t - 1 5 ) - 0 . 0 0 0 0 0 5 5 ( t - 7 . 5 ) ^ { 2 } ] [ 1 + f ( z _ { 0 } ) ] , } \\ { G = [ 1 + 0 . 9 4 3 0 \times 1 0 ^ { - 5 } ( p - p _ { 0 } ) - 0 . 7 8 \times 1 0 ^ { - 1 0 } ( p - p _ { 0 } ) ^ { 2 } ] [ 1 + g ( z _ { 0 } ) ] , } \end{array}
$$

where the correcting factors depending upon the zenith distance $z _ { 0 }$ are tabulated in Table 6.1. They increase with $z _ { 0 }$ and remain close to 1, reaching a maximum respectively of 1.01 and 1.0013 for $z _ { 0 } = 7 0 ^ { \circ }$ .

Table 6.1. Correction factors as functions of zenith distance   

<table><tr><td>Z0</td><td>10-4 f(z)</td><td>10-4g(z)</td></tr><tr><td>0°</td><td>0</td><td>4</td></tr><tr><td>10°</td><td>0</td><td>4</td></tr><tr><td>20°</td><td>0</td><td>4</td></tr><tr><td>30°</td><td>0</td><td>5</td></tr><tr><td>35°</td><td>0</td><td>5</td></tr><tr><td>40°</td><td>2</td><td>5</td></tr><tr><td>45°</td><td>6</td><td>6</td></tr><tr><td>50°</td><td>12</td><td>6</td></tr><tr><td>55°</td><td>21</td><td>7</td></tr><tr><td>60°</td><td>34</td><td>8</td></tr><tr><td>65°</td><td>56</td><td>10</td></tr><tr><td>70°</td><td>97</td><td>13</td></tr></table>

# 6.1.4.2 Chromatic effects

The actual dependence of $n$ , and hence of $\alpha$ , is a rather complicated function of the inverse square of the wavelength. An approximate expression for the chromatic refraction at wavelength $\lambda$ in accordance with the Pulkovo tables is

$$
R ( t , p , \lambda ) = R ( t , p ) ( 0 . 9 8 2 8 2 + 0 . 0 0 5 9 8 1 / \lambda ^ { 2 } ) .
$$

However since, in general, the observations are made in a finite interval of wavelengths using a filter whose transparency is also a function of $\lambda$ , the above formula is sufficient when applied to the mean wavelength of the ensemble star-filter.

For this reason, it is often preferable to make two observations at two widely separated mean wavelengths. Let $z _ { 1 }$ and $z _ { 2 }$ be the two observed zenith distances for $\lambda = \lambda _ { 1 }$ and $\lambda _ { 2 }$ , and $C$ be the wavelength-dependent coefficient in the Laplace formula which takes the form

$$
R = A _ { 0 } \tan z + { \frac { C } { \lambda ^ { 2 } } } \tan z - B _ { 0 } \tan ^ { 3 } z ,
$$

so that the two observations give two equations

$$
\begin{array} { r l } & { z = z _ { 1 } + A _ { 0 } \tan z _ { 1 } + \frac { C \tan z _ { 1 } } { \lambda _ { 1 } ^ { 2 } } - B _ { 0 } \tan ^ { 3 } z _ { 1 } , } \\ & { z = z _ { 2 } + A _ { 0 } \tan z _ { 2 } + \frac { C \tan z _ { 2 } } { \lambda _ { 2 } ^ { 2 } } - B _ { 0 } \tan ^ { 3 } z _ { 2 } , } \end{array}
$$

with two unknowns $z$ and $C$ . It is, of course, assumed that the other terms of the Laplace formula are known, that is, determined, from measurements of temperature, pressure, etc.

# 6.1.4.3 Water vapor

The content of water vapor in air varies considerably with meteorological conditions and the proportion of water vapor defined by its partial pressure $f$ modifies $n$ and $\alpha$ . The Pulkovo refraction tables are well represented by the following correction to $R ( t , p , \lambda )$ :

$$
R ( t , p , \lambda , f ) = R ( t , p , \lambda ) ( 1 - 0 . 1 5 2 \times 1 0 ^ { - 5 } f - 0 . 5 5 \times 1 0 ^ { - 9 } f ^ { 2 } ) .
$$

# 6.1.4.4 Refraction at a finite distance

If the observed object, although outside the atmosphere, is close to the Earth, it is not possible to assume that the true direction is parallel to the asymptote of the light ray.

On Fig. 6.1, if the object is in $N$ the actual point from which the true zenith distance is given is $K$ . If the origin of the ray is not at infinity, there is an apparent parallactic displacement, so that in order to get the true direction, one has to correct the position of $\varOmega$ by $x = \varOmega K$ along the vertical.

In the triangle $O M K$ of Fig. 6.1, one has

$$
O K \sin z = r \sin \psi .
$$

Applying the invariant (6.4), one has

$$
n _ { 0 } r _ { 0 } \sin z _ { 0 } = n r \sin \psi .
$$

The combination of these two equations gives, assuming, in addition, that the source, $M$ , is outside the atmosphere so that $n = 1$ :

$$
O K = x + r _ { 0 } = \frac { n _ { 0 } r _ { 0 } \sin z _ { 0 } } { \sin z } .
$$

By construction, if $R$ is the refraction, one has, neglecting the third-order small quantities,

$$
\begin{array} { l } { { \sin z = \sin ( z _ { 0 } + R ) } } \\ { { \displaystyle \quad = \sin z _ { 0 } \left( 1 - \frac { R ^ { 2 } } { 2 } + R \cot z _ { 0 } \right) . } } \end{array}
$$

Then,

$$
\begin{array} { l } { \displaystyle \frac { x } { r _ { 0 } } = n _ { 0 } \left( 1 + \frac { R ^ { 2 } } { 2 } - R \cot z _ { 0 } \right) - 1 , } \\ { \displaystyle \frac { x } { r _ { 0 } } = n _ { 0 } \alpha _ { 0 } - n _ { 0 } R \cot z _ { 0 } + n _ { 0 } \frac { R ^ { 2 } } { 2 } . } \end{array}
$$

# 6.1.5 Accuracy of refraction formulae

The formulae given in Section 6.1.4 are, at best, good to a few milliarcseconds (mas) for small zenith distances. They degrade for larger values of $z _ { 0 }$ . One can estimate the errors to be of the order of 0.01 around $5 5 ^ { \circ }$ , and 0.05 for $z _ { 0 } = 7 0 ^ { \circ }$ . At lower altitudes, additional multiplicative coefficients are to be applied for chromatic and water vapor corrections. For $A$ and $B$ , special tables exist in the literature (Simon et al., 1996), and additional corrections must be introduced for latitude in order to take into account the non-sphericity of the Earth and of its atmosphere, as well as for the height of the observer – a purely geometrical effect due to the curvature of the Earth, independent of the effects of atmospheric pressure. The precision of these improved formulae is rather poor, and becomes worse for increasing zenith distances. The maximum uncertainty of the refraction occurs at the horizon where it reaches a fraction of a degree (see Section 13.3.3).

Even at small zenith distances the errors of refraction formulae, or tables, forbid sub-milliarcsecond astrometry. It is necessary to determine simultaneously the refraction using two or more color observations. But even then, the uncertainty in the actual mean wavelength of the observation, as well as the short period variations of refraction due to atmospheric turbulence, do not permit one to expect anything better than a few tenths of a mas. To obtain higher accuracies, one must get rid of refraction completely by observing from space.

# 6.1.6 Refraction in distance measurements

The speed of light in a gas is $c / n$ , where $n$ is the refractive index of the medium. Let us consider a distance between the ground (index 0) and a point, $P$ , determined using $c$ as the speed of light. The actual distance is smaller, and the difference is given by the integral

$$
\Delta D = \int _ { 0 } ^ { P } ( n ( s ) - 1 ) \mathrm { d } s ,
$$

taken along the ray path. Neglecting the curvature of the light and assuming that the atmosphere is composed of plane layers, if $h$ is the height of the layer, one has

$$
\mathrm { d } h = \mathrm { d } s \cos z ,
$$

and

$$
\Delta D = \frac { 1 } { \cos z } \int _ { 0 } ^ { A } \left( n ( h ) - 1 \right) \mathrm { d } h .
$$

Using the Gladstone–Dale law (formula (6.9)) and introducing the coefficients $\alpha$

and $\beta$ used in (6.10), or the scale factor of the atmosphere, one gets

$$
\Delta D = \frac { \alpha \beta r _ { 0 } } { \cos z } = \frac { \alpha L } { \cos z } .
$$

This has to be corrected for chromatic refraction and the particular effect of water vapor, as in the case of the optical refraction, using the same corrective terms for $\alpha$ and $\beta$ .

This theoretical approach is not ideal when high accuracy is sought. So, in practice, it is better to use an empirical formula deduced from the analysis of a large number of observations. The Marini and Murray (1973) formula, adopted by the IERS standards, is the following, expressed in meters:

$$
\Delta D = \frac { \phi ( \lambda ) } { \psi ( \phi , h ) } \times \frac { A + B } { \cos z + B / ( ( A + B ) ( \cos z + 0 . 0 1 ) ) } ,
$$

where

$$
\begin{array} { l } { A = 0 . 0 0 0 0 2 3 5 7 p + 0 . 0 0 0 0 0 1 4 1 f , } \\ { B = ( 1 . 0 8 4 \times 1 0 ^ { - 1 0 } ) p T K + \frac { ( 9 . 4 6 8 \times 1 0 ^ { - 1 2 } ) p ^ { 2 } } { T ( 3 - 1 / K ) } , } \end{array}
$$

where $T = t + 2 7 3 . 1 6$ is the absolute temperature, $p$ and $f$ are the pressure and the partial water vapor pressure expressed in pascals, $\lambda$ is the wavelength in micrometers, $h$ is the height in kilometers, and $\phi$ is the latitude of the observer. In addition,

$$
\begin{array} { c } { { K = 1 . 1 6 3 - 0 . 0 0 9 6 8 \cos 2 \phi - 0 . 0 0 0 0 4 T + 0 . 0 0 0 0 0 0 1 4 3 5 p , } } \\ { { \Phi ( \lambda ) = 0 . 9 6 5 0 + 0 . 0 1 6 4 / \lambda ^ { 2 } + 0 . 0 0 0 2 2 8 / \lambda ^ { 4 } , } } \\ { { \Psi ( \phi , h ) = 1 - 0 . 0 0 2 6 \cos 2 \phi - 0 . 0 0 0 3 1 h . } } \end{array}
$$

# 6.1.7 Refraction in radio waves

The refractive index in radio waves is very different, and a special formula, due to Smith and Weintraub (1953), is generally adopted,

$$
\alpha _ { \mathrm { R } } = \frac { 0 . 2 8 4 0 \times 1 0 ^ { - 8 } p } { 1 + 0 . 0 0 3 6 6 t } - \frac { 0 . 4 6 9 \times 1 0 ^ { - 9 } f } { 1 + 0 . 0 0 3 6 6 t } + \frac { 0 . 5 0 8 \times 1 0 ^ { - 7 } f } { \left( 1 + 0 . 0 0 3 6 6 t \right) ^ { 2 } } ,
$$

where the same notations and units as above are used. The refraction is

$$
R = \alpha _ { \mathrm { R } } \tan z _ { 0 } - 0 \sp { \prime } . 0 6 7 \tan \sp { 3 } z _ { 0 } .
$$

However, in general, the radio observations for astrometry (VLBI) reduce to time measurements, so that the main effect to take into account is the refraction in distance, which is dealt with in a way similar to that in Section 6.1.6.

In addition, radio waves undergo an important delay due to the ionosphere. The speed of the waves is

$$
V = c n = c { \sqrt { 1 - { \frac { \nu _ { \mathrm { p } } ^ { 2 } } { \nu ^ { 2 } } } } } ,
$$

where $\nu$ is the frequency of the wave and $\nu _ { \mathrm { p } }$ is the proper frequency of the plasma given, in hertz, by

$$
\nu _ { \mathrm { p } } = { \frac { N _ { \mathrm { e } } ^ { 2 } } { \varepsilon _ { 0 } m _ { \mathrm { e } } } } ,
$$

where $N$ is the electronic density of the plasma per cubic meter, $e$ and $m _ { \mathrm { e } }$ are the charge and the mass of the electron, respectively, and $\varepsilon _ { 0 }$ is the constant of permittivity of free space, (or electric constant) equal to

$8 . 8 5 4 1 8 7 8 1 7 \times 1 0 ^ { - 1 2 }$ farads per meter $( f / m )$

The distance correction, after introducing the various numerical values in the formula, is

$$
\Delta D _ { \mathrm { R } } = c \Delta t = 4 0 . 3 0 8 \frac { N } { \nu ^ { 2 } } .
$$

It is determined by making observations at two frequencies and solving the two equations (6.19) after eliminating $N$ .

Then if $\Delta D _ { \mathrm { R } } ^ { 0 }$ is the distance correction at the zenith, the actual effect of the ionospheric refraction is

$$
\Delta D _ { \mathrm { R } } = \frac { \Delta D _ { \mathrm { R } } ^ { 0 } } { \cos \left( \sin ^ { - 1 } \left( \frac { r _ { 0 } \sin z } { r _ { 0 } + h } \right) \right) } ,
$$

where $h$ is the mean height of the ionosphere. This formula takes into account the sphericity of the ionosphere, but assumes that the latter is homogeneous. A more detailed analysis can be found in Thomson et al., 1986.

# 6.2 Parallactic corrections

As a rule, observations made at different times from different locations should be referred to a single common system. For determining star positions, the preference is the celestial barycentric reference frame (Section 7.2). If the observed objects were at infinity, the translation from the observer to the barycenter of the Solar System would not affect their apparent direction. But this is not the case, since stars are at some finite distance. The result is that the motion of the observer produces an apparent displacement of the star with respect to the fixed reference system, called the parallactic displacement. The motion of the observer is conveniently split into three components.

![](images/764ead2f64c7161cec34d6ca18f01cc249d72e9c329744081a989e5a18db7343.jpg)  
Fig. 6.2. Parallactic correction of the star position.

- A linear uniform motion, representing the motion of the Solar System as a whole. It combines with analogous linear motions of stars in the Galaxy and will be considered in Section 11.3 dealing with proper motions and radial velocities.   
- The motion of the center of mass of the Earth around the barycenter. It is the combination of the motion of the barycenter of the Earth–Moon system about the barycenter of the Solar System, and of the motion of the center of mass of the Earth about the barycenter of the Earth–Moon system. The result is a yearly periodic displacement called annual parallax and a small monthly component. Actually, the yearly periodicity is only an approximation that is valid at the level of a milliarcsecond. It is not adequate at higher precisions, and the actual motion of the center of mass of the Earth must be used.   
- The motion of the observer around the center of mass of the Earth. If the observer is on the ground, the effect produced is called the diurnal parallax. The same phenomenon exists for a spacecraft, and one can speak of orbital parallax.

# 6.2.1 Correction for annual parallax

Let us assume that the barycentric spherical coordinates of the star $S$ are $\alpha$ and $\delta$ and that the distance of the star is $\rho$ (Fig. 6.2). The components of the three-dimensional vector BS are

$$
\left\{ \begin{array} { l l } { \rho \cos \delta \cos \alpha } \\ { \rho \cos \delta \sin \alpha } \\ { \quad \rho \sin \delta . } \end{array} \right.
$$

Let $E$ be the center of the Earth. The components $x , y , z$ of the vector BE are given by the ephemerides of the Earth’s motion and are functions of the time $t$ . The actual geocentric coordinates $\alpha _ { E }$ , $\delta _ { E }$ and the geocentric distance $\rho _ { E }$ are given, as a function of the barycentric coordinates and distance, $\alpha _ { B } , \delta _ { B }$ , and $\rho$ by

$$
\begin{array} { r l } & { \rho _ { E } \cos \delta _ { E } \cos \alpha _ { E } = \rho \cos \delta _ { B } \cos \alpha _ { B } - x , } \\ & { \rho _ { E } \cos \delta _ { E } \sin \alpha _ { E } = \rho \cos \delta _ { B } \sin \alpha _ { B } - y } \\ & { \rho _ { E } \sin \delta _ { E } = \rho \sin \delta _ { B } - z . } \end{array}
$$

The corrections $\Delta \alpha = \alpha _ { B } - \alpha _ { E }$ and $\Delta \delta = \delta _ { B } - \delta _ { E }$ to the barycentric positions are readily obtained if one neglects the second-order effects, an assumption that is justified because, for almost all stars, the ratio $B E / \rho$ is smaller than $1 0 ^ { - 6 }$ radians, the largest value, for Proxima Centauri, being $3 . 7 \times 1 0 ^ { - 6 }$ . One then may differentiate (6.20) and obtain the following formulae expressed in radians as functions of $\Delta \alpha , \Delta \delta$ , and $\Delta \rho = \rho - \rho _ { E }$ :

$$
\begin{array} { l } { \displaystyle \Delta \alpha \cos \delta = \frac { x } { \rho } \sin \alpha - \frac { y } { \rho } \cos \alpha , } \\ { \displaystyle \Delta \delta = \left( \frac { x } { \rho } \cos \alpha + \frac { y } { \rho } \sin \alpha \right) \sin \delta - \frac { z } { \rho } \cos \delta , } \end{array}
$$

and the variation of the distance of the star

$$
\Delta \rho = - x \cos \alpha \cos \delta - y \sin \alpha \cos \delta + z \sin \delta .
$$

It is to be noted that, although these formulae are valid to better than a microarcsecond, one cannot, as was classically done, replace the Earth’s orbit by a conventional ellipse. It is necessary to derive $x / \rho , y / \rho$ , and $z / \rho$ from precise barycentric ephemerides of the Earth’s center of mass, with a relative accuracy of $1 0 ^ { - 6 }$ , so as to avoid any erroneous effect.

# 6.2.2 Stellar parallax

Formulae (6.21) are expressed in radians, which is an inconvenient unit for astrometry in general, and especially for small angles. So, it is customary to express small angles in seconds of arc (and submultiples mas and $\mu \mathrm { a s }$ ). This leads to defining the stellar parallax $\varpi$ as the ratio $1 / \rho$ where $\rho$ is expressed in astronomical units, transformed into arcseconds,

$$
\varpi = k / \rho ,
$$

with $k = \pi / 6 4 8 0 0 0$ . It is also the angle in arcseconds with which one sees one astronomical unit from the star.

However, one generally expresses the distance $\rho$ in units of $6 4 8 0 0 0 / \pi =$ 206 264.81 astronomical units, a unit called parsec, then one has simply,

$$
\varpi = 1 / \rho ,
$$

The parsec is the distance corresponding to a parallax of $1 ^ { \prime \prime }$ , and is also equal to 3.261 5637 light-years. If, in a first approximation, we describe the motion of the Earth as an ellipse, with a semi-major axis equal to one astronomical unit, the apparent geocentric motion of the star around its barycentric position is an ellipse, whose semi-major axis is equal to its parallax.

Using the stellar parallax and the parsec, the formulae (6.21) are transformed into:

$$
\begin{array} { r } { \Delta \alpha \cos \delta = \varpi \left( x \sin \alpha - y \cos \alpha \right) , \qquad } \\ { \Delta \delta = \varpi \left[ ( x \cos \alpha + y \sin \alpha ) \sin \delta - z \cos \delta \right] , } \end{array}
$$

where the coordinates $, \ y , \ z$ of the Earth are expressed in astronomical units and the corrections to the position are in arcseconds.

Note. The interpretation of the parallax and the determination of its associated uncertainty in terms of the distance to the star is not straightforward. It will be discussed in Section 11.2.

# 6.2.3 Diurnal and orbital parallaxes

The diurnal parallax is the displacement of the geocentric position of the star S due to the vector GP where $P$ is the observer and $G$ is the geocenter. Let $\lambda$ , $\phi$ and $R$ be the geocentric coordinates of $P$ , and $T$ the sidereal time or the stellar angle (see Section 10.4.4). The components of GP are

$$
\begin{array} { l } { x ^ { \prime } = R \cos \phi \cos ( T + \lambda ) , } \\ { y ^ { \prime } = R \cos \phi \sin ( T + \lambda ) , } \\ { z ^ { \prime } = R \sin \phi . } \end{array}
$$

To compute the parallactic correction, it is sufficient to apply Equations (6.21), replacing $x , y , z$ by $x + x ^ { \prime } , y + y ^ { \prime } , z + z ^ { \prime }$ , or using only $x ^ { \prime } , y ^ { \prime } , z ^ { \prime }$ if only the diurnal parallax correction is needed.

If the observation is performed from a satellite, the geocentric coordinates of the satellite $x ^ { \prime } , y ^ { \prime } , z$ $z ^ { \prime }$ are obtained from the orbital ephemerides. In both cases, formulae (6.21) apply again, provided that the quantities $x ^ { \prime }$ , $y ^ { \prime } , z ^ { \prime }$ are respectively added to $x , y , z$ .

Generally, in the past, diurnal parallax corrections were not applied to the observations of stars. The effect, of the order of $R / \rho$ , is smaller than the effect of the stellar parallax by a factor equal to the ratio between the Earth’s radius and the astronomical unit $( 4 . 2 6 \times 1 0 ^ { - 5 } )$ ). Nevertheless, for a parallax equal to $0 ^ { \prime } 1$ , this represents a correction of $4 ~ \mu \mathrm { a s }$ . So it is not to be neglected for nearby stars. In the case of orbital parallax, which gives a larger correction (a factor of 6 for a geostationary satellite), the correction must be made, and was indeed performed in the reduction of Hipparcos data.

In the case of the Moon and the planets, the situation is different. It is important to get the position of the body at a well-determined time, and to take into account the fact that during the time the light traveled from the body to the observer, the Moon, or the planet, as well as the Earth and the observer moved. This will be presented in Section 6.3.6.

# 6.3 Aberration

Since the velocity of light is finite, the apparent direction to an object is affected by the motions of the object and of the observer. Let us first consider the case of very distant objects like stars. The correction for the motion of the observer is called stellar aberration. The motion of an observer on Earth can be divided into three parts: the diurnal rotation of the Earth, the orbital motion of the Earth about the barycenter of the Solar System, and the motion of the barycenter in space. Thus, stellar aberration is made up of the three components, which are referred to as diurnal, annual, and secular aberration. For a spacecraft in orbit around the Earth, the diurnal aberration is replaced by orbital aberration.

In the case of objects in the Solar System, the situation is different. One speaks of planetary aberration, but it is actually a different concept. In this case, aberration corresponds to the displacement of a planet between the moment the light was emitted and the time when it was received by the observer. Here, the light-time and the relative motions of the body and of the Earth can be accurately computed in order to determine the planetary aberration.

# 6.3.1 Secular aberration

The stars and barycenter of the Solar System can generally be considered to be in uniform rectilinear motion. The aberrational displacement due to the relative motion is equal to the proper motion of the star multiplied by the light-time, which results in a correction of the position of each star. These are seldom well known and, since the knowledge of the barycentric position of a star at the time of observation has no scientific interest, this displacement is in general ignored. However, one might wish to refer the stars to another reference frame than the barycentric. One may think of the local standard of rest, which is at rest with respect to close-by stars.

![](images/3f50521f3ceb2cdfafe0f6446e577534aa77b762833fc320a38b5fca07c6ab10.jpg)  
Fig. 6.3. Stellar aberration.

Then the secular aberration would be computed from the motion of the Sun with respect to it; the value is $1 9 . 5 \mathrm { k m / s }$ in the direction of the apex. The corresponding magnitude of the secular aberration is about 13 arcseconds. But the apex itself depends upon the classes and the population of stars used to determine it, so that the physical significance of the local standard of rest is questionable.

One may also wish to take a galactocentric reference frame. In that case, the Sun has a velocity of the order of $2 2 0 \mathrm { k m } / \mathrm { s }$ , leading to a secular aberration of $1 5 0 ^ { \prime \prime }$ . Let us, however, note that, for very accurate astrometry, the curvature of the orbit of the Sun may have to be taken into account. This part of the secular aberration is proportional to the square of time. In one year, assuming a period of the Sun’s galactic orbit of $P = 2 5 0 0 0 0 0 0 0$ years, the rotation of the instantaneous velocity vector is $2 \pi / P$ radians. This represents a change of the velocity vector of $5 . 5 \mathrm { m m / s }$ giving rise to a variation of the secular galactic aberration of about $4 \mu \mathrm { a s }$ . Stars in the vicinity of the Sun have similar motions around the center of the Galaxy, which cancel out most of this effect. But it remains to be considered for very distant stars and extragalactic objects. This aberration in proper motion may reach a fraction of a milliarcsecond close to the center of the galaxy, where stars have short revolution periods (Kovalevsky, 2003).

# 6.3.2 Stellar aberration

In general, the observer at $E$ is moving with a velocity $\mathbf { V }$ relative to the fixed frame. The apparent change in the geometric direction of the celestial object at $S$ , due to the orbital motion of the Earth about the barycenter, is called stellar aberration. In Fig. 6.3, $\mathbf { p }$ is a unit vector in the geometric direction $E S$ , i.e. in the direction of the body at time $t$ in a fixed frame. The velocity vector of the light is $- c \mathbf { p }$ in the same frame. At time $t$ the observer will see the body at $S ^ { \prime }$ , a direction defined by the vectorial sum of the two velocities. The unit vector of this direction is $ { \mathbf { p } } ^ { \prime }$ . Here, $( \mathbf { S } ^ { \prime } \mathbf { E } , \ \mathbf { V } ) = { \boldsymbol { \theta } } $ is the angle between the direction of motion and $\mathbf { p }$ in the stationary frame, and $S E S ^ { \prime } = \Delta \theta$ is the displacement due to aberration in the moving frame, which is always toward the direction of motion.

The classical Newtonian expression for the direction of the source as seen by the moving observer is obtained by vector addition of velocities as follows:

$$
\mathbf { p } ^ { \prime } = { \frac { \mathbf { p } + \mathbf { V } / c } { | \mathbf { p } + \mathbf { V } / c | . } }
$$

Taking the scalar part of the vector cross product of $\mathbf { p }$ with $\mathbf { p } ^ { \prime }$ , then

$$
\begin{array} { c } { \sin \Delta \theta = \displaystyle \frac { \left( V / c \right) \sin \theta } { \sqrt { \left( 1 + 2 ( V / c ) \cos \theta + ( V / c ) ^ { 2 } \right) } } } \\ { = \displaystyle \frac { V } { c } \sin \theta - \frac { 1 } { 2 } \bigg ( \displaystyle \frac { V } { c } \bigg ) ^ { 2 } \sin 2 \theta + \cdots , } \end{array}
$$

since $| { \bf p } \times { \bf p ^ { \prime } } | = \sin \Delta \theta$ , $| { \bf p } \times { \bf p } | = 0$ , and $\begin{array} { r } { | \mathbf { p } \times \mathbf { V } / c | = \frac { V } { c } \sin \theta } \end{array}$

The term of order $V / c$ is about 0.0001, which, expressed in arcseconds, is of the order of $2 0 ^ { \prime \prime }$ . Similarly, the term in $( V / c ) ^ { 2 }$ has a maximum value of about 0.001. The third-order terms are not significant, particularly because they are smaller than the effect of general relativity.

# 6.3.3 Aberration in relativity

In special relativity, the velocity of light is constant in the moving and stationary frame, and the Lorentz formula for the addition of velocities applies. This is also true in general relativity whose local kinematic properties are those of special relativity plus additional effects caused by the curvature of space-time. The latter effects are applied separately as light deflection (see Section 6.4).

Let us apply the velocity addition formula in special relativity (5.8). With the notations set above for the classical case, we have:

- the velocity of light in the geometric direction: $c \mathbf { p }$ , - the velocity of light in the apparent direction: $c \mathbf { p } ^ { \prime }$ , - the velocity of the observer: V.

Formula (5.8) becomes:

$$
c { \bf p } ^ { \prime } = \frac { c { \bf p } + \gamma { \bf V } + ( \gamma - 1 ) ( { \bf V } \cdot c { \bf p } ) { \bf V } / V ^ { 2 } } { \gamma ( 1 + c { \bf p } \cdot { \bf V } / c ^ { 2 } ) } ,
$$

with $\gamma = ( 1 - V ^ { 2 } / c ^ { 2 } ) ^ { - 1 / 2 }$ . Dividing by $c$ and dividing both terms of the fraction

by $\gamma$ , one obtains:

$$
\mathbf { p } ^ { \prime } = { \frac { \mathbf { p } { \boldsymbol { \gamma } } ^ { - 1 } + \mathbf { V } / c + ( 1 - { \boldsymbol { \gamma } } ^ { - 1 } ) ( \mathbf { V } \cdot \mathbf { p } ) \mathbf { V } / V ^ { 2 } } { 1 + \mathbf { p } \cdot \mathbf { V } / c } } .
$$

From the definition of $\gamma$ , it is easy to see that

$$
( 1 - \gamma ^ { - 1 } ) ( 1 + \gamma ^ { - 1 } ) = \mathbf { V } ^ { 2 } / c ^ { 2 } .
$$

Hence

$$
\begin{array} { l } { { \bf { p } } ^ { \prime } = \frac { \gamma ^ { - 1 } { \bf { p } } + ( { \bf { V } } / c ) + ( { \bf { p } } \cdot { \bf { V } } / c ) ( { \bf { V } } / c ) / ( 1 + \gamma ^ { - 1 } ) } { 1 + { \bf { p } } \cdot { \bf { V } } / c } } \\ { = \frac { \gamma ^ { - 1 } { \bf { p } } } { 1 + { \bf { p } } \cdot { \bf { V } } / c } + ( 1 + \gamma ^ { - 1 } ) { \bf { V } } / c . } \end{array}
$$

Again taking the modulus of the vector cross products of Equation (6.26) with $\mathbf { p }$ , then

$$
\begin{array} { l } { \sin \Delta \theta = \frac { ( V / c ) \sin \theta + 1 / 2 ( V / c ) ^ { 2 } \sin 2 \theta / ( 1 + \gamma ^ { - 1 } ) } { 1 + ( V / c ) \cos \theta } } \\ { = \displaystyle \frac { V } { c } \sin \theta - \frac { 1 } { 4 } \bigg ( \frac { V } { c } \bigg ) ^ { 2 } \sin 2 \theta + \frac { 1 } { 4 } \bigg ( \frac { V } { c } \bigg ) ^ { 3 } \sin 2 \theta \cos \theta + \cdot \cdot \cdot } \end{array}
$$

$$
\Delta \theta = { \frac { V } { c } } \sin \theta - { \frac { 1 } { 4 } } \left( { \frac { V } { c } } \right) ^ { 2 } \sin 2 \theta + { \frac { 1 } { 6 } } \left( { \frac { V } { c } } \right) ^ { 3 } \sin \theta ( 1 + 2 \sin ^ { 2 } \theta ) + \cdot \cdot \cdot .
$$

This shows that special-relativistic aberration and classical Newtonian aberration agree only up to the first order in $V / c$ (mas precision). The difference in the second order is $\frac { 1 } { 4 } \big ( \frac { V } { c } \big ) ^ { 2 } \sin { 2 \theta }$ , that can reach 0.5 mas. For this reason, it is recommended that relativistic aberration (Equations (6.26)–(6.28)) be systematically used, particularly when high precision is required.

# 6.3.4 Accurate computation of the annual aberration

In accordance with recommendations of the International Astronomical Union in 1952, the annual aberration is calculated beginning in 1960 from the actual motion of the Earth, referred to an inertial frame of reference and to the center of mass of the Solar System. The resulting aberrational displacement, $\Delta \theta$ , may be resolved into corrections to the directional coordinates by standard methods. Let us call ${ \dot { X } } , { \dot { Y } }$ , and $\dot { Z }$ the components of the Earth’s velocity, V, in equatorial rectangular axes, and $x = \dot { X } / c$ , $y = \dot { Y } / c$ and $z = \dot { Z } / c$ the components of the reduced velocity vector $\mathbf { v } = \mathbf { V } / c$ . The components of the unit vector u of the direction of the star are

$$
\begin{array} { r c l } { { } } & { { } } & { { u = \cos \delta \cos \alpha , } } \\ { { } } & { { } } & { { v = \cos \delta \sin \alpha , } } \\ { { } } & { { } } & { { w = \sin \delta . } } \end{array}
$$

The aberration displacement is a rotation of $\Delta \theta$ about the normal $\mathbf { N }$ to this plane:

$$
\mathbf { N } = \mathbf { u } \times \mathbf { v }
$$

whose components are:

$$
\begin{array} { c } { { L = z \cos \delta \sin \alpha - y \sin \delta , } } \\ { { { } } } \\ { { M = x \sin \delta - z \cos \delta \cos \alpha , } } \\ { { { } } } \\ { { N = y \cos \delta \cos \alpha - x \cos \delta \sin \alpha . } } \end{array}
$$

According to Equation (3.22), the components of the displaced (apparent) direction $ { \mathbf { u } } ^ { \prime }$ of the star are given by

$$
{ \bf u } ^ { \prime } = { \bf u } \cos \Delta \theta + ( { \bf N } \times { \bf u } ) \sin \Delta \theta .
$$

The components of $ { \mathbf { u } } ^ { \prime }$ are therefore:

$$
\begin{array} { l } { { x ^ { \prime } = \cos \delta ^ { \prime } \sin \alpha ^ { \prime } = \cos \delta \sin \alpha \cos \Delta \theta + \displaystyle \frac { V } { c } ( M \sin \delta - N \cos \delta \sin \alpha ) \sin \Delta \theta , } } \\ { { y ^ { \prime } = \cos \delta ^ { \prime } \cos \alpha ^ { \prime } = \cos \delta \sin \alpha \cos \Delta \theta + \displaystyle \frac { V } { c } ( N \cos \delta \cos \alpha - L \sin \delta ) \sin \Delta \theta , } } \\ { { z ^ { \prime } = \sin \delta ^ { \prime } = \sin \delta \cos \Delta \theta + \displaystyle \frac { V } { c } ( L \cos \delta \sin \alpha - M \cos \delta \cos \alpha ) \sin \Delta \theta . \qquad } } \end{array}
$$

From these expressions, one can derive the components $u ^ { \prime } , \ v ^ { \prime } , \ w ^ { \prime }$ of $ { \mathbf { u } } ^ { \prime }$ and consequently the displaced coordinates $\alpha ^ { \prime }$ and $\delta ^ { \prime }$ and the corrections to right ascension and declination, referred to the same coordinate system in the sense corrected place minus uncorrected place.

$$
\begin{array} { c } { { \Delta \alpha = \alpha ^ { \prime } - \alpha , } } \\ { { \Delta \delta = \delta ^ { \prime } - \delta . } } \end{array}
$$

# 6.3.5 Approximate formulae for annual aberration

These exact formulae are to be used when a full third order accuracy (to a $\mu \mathrm { a s }$ ), is needed. For uncertainties of the order of a mas, the following approximate

expressions (Seidelmann, 1992) are sufficient:

$$
\begin{array} { c } { { \displaystyle \Delta \alpha \cos \delta = - \frac { \dot { X } } { c } \sin \alpha + \frac { \dot { Y } } { c } \cos \alpha + \frac { 1 } { c ^ { 2 } } ( \dot { X } \sin \alpha - \dot { Y } \cos \alpha ) } } \\ { { \mathrm { } ~ } } \\ { { \mathrm { } ~ \times ( \dot { X } \cos \alpha + \dot { Y } \sin \alpha ) \sec \delta \mathrm { c } \delta + \cdots , } } \\ { { \mathrm { } ~ \Delta \delta = - \frac { \dot { X } } { c } \cos \alpha \sin \delta - \frac { \dot { Y } } { c } \sin \alpha \sin \delta + \frac { \dot { Z } } { c } \cos \delta } } \\ { { \mathrm { } ~ - \frac { 1 } { 2 c ^ { 2 } } ( \dot { X } \sin \alpha - \dot { Y } \cos \alpha ) ^ { 2 } \tan \delta } } \\ { { \mathrm { } ~ + \frac { 1 } { c ^ { 2 } } ( \dot { X } \cos \delta \cos \alpha + \dot { Y } \cos \delta \sin \alpha + \dot { Z } \sin \delta ) } } \\ { { \mathrm { } ~ \times ( \dot { X } \sin \delta \cos \alpha + \dot { Y } \sin \delta \sin \alpha - \dot { Z } \cos \delta ) + \cdots . } } \end{array}
$$

Also to first order in $V / c$ , we obtain the aberration in right ascension and declination due to the unperturbed elliptic component of the orbital motion of the Earth with respect to the Sun. It means, as earlier, the quantity to be added to the uncorrected place $\alpha , \delta$ in order to obtain the place corrected for aberration $\alpha ^ { \prime } { , } \delta ^ { \prime }$ is:

$$
\begin{array} { l } { { \alpha ^ { \prime } - \alpha = - \kappa \sec \delta ( ( \sin A + e \sin \pi ) \sin \alpha - \cos \epsilon ( \cos A + e \cos \pi ) \cos \alpha ) } } \\ { { \delta ^ { \prime } - \delta = - \kappa ( \sin A + e \sin \pi ) \cos \alpha \sin \delta } } \\ { { \qquad - \kappa \cos \epsilon ( \cos A + e \cos \pi ) ( \tan \epsilon \cos \delta - \sin \alpha \sin \delta ) , \qquad ( 6 . 3 2 ) } } \end{array}
$$

where $\varLambda$ is the longitude of the Sun, $e$ and $\boldsymbol { \Pi }$ are the eccentricity and longitude of perigee of the solar orbit, $\epsilon$ is the mean obliquity of the ecliptic, and $\kappa$ is the constant of aberration. The latter is the ratio of the mean orbital speed of the Earth to the speed of light, where perturbations and the motion of the Sun relative to the barycenter are neglected. It is equal to

$$
\kappa = n a / c \sqrt { 1 - e ^ { 2 } } ,
$$

where $c$ is the speed of light, $a$ is the mean distance of the Earth from the Sun, and $n$ is the mean motion of the Earth’s orbit.

Its value for the standard epoch J2000.0 is:

$$
\kappa = 2 0 _ { \cdot } ^ { \prime \prime } 4 9 5 5 2 .
$$

It was used as the multiplicative factor to analytical expressions of the annual aberration, the parameters being the elements of the Earth’s orbit around the Sun (see, for instance, Woolard and Clemence, 1966, p. 110). This is now obsolete. The aberration must be computed using the actual velocity of the observer with respect to the barycenter of the Solar System as provided by ephemerides. It is, however, convenient to handle separately the annual aberration due to the motion of the center of the Earth around the barycenter, $B$ , of the Solar System as presented above, and the diurnal aberration due to the motion of the observer as a consequence of the Earth’s rotation.

Note. The second term in each factor in Equation (6.32) depends explicitly on the eccentricity and represents the components of the displacement due to the departure of the elliptic orbital motion from a circle. The component of the aberration that depends on $e$ is known as elliptic aberration.

# 6.3.6 Diurnal and orbital aberration

The rotation of the Earth on its axis carries the observer toward the East with a velocity $\cos \phi ^ { \prime }$ , where $\omega$ is the equatorial angular velocity of the Earth (the standard value of $\omega$ is given in Appendix B; if $a$ is the equatorial radius, then $a \omega = 0 . 4 6 4 \mathrm { k m } / \mathrm { s }$ is the equatorial rotational velocity of the surface of the Earth), and $\rho$ and $\phi ^ { \prime }$ are the geocentric distance and latitude of the observer, respectively. The corresponding constant of diurnal aberration is

$$
{ \frac { a } { c } } \omega { \frac { \rho } { a } } \cos \phi ^ { \prime } = 0 ; 3 2 0 0 { \frac { \rho } { a } } \cos \phi ^ { \prime } .
$$

The aberrational displacement may be resolved into corrections in right ascension and declination:

$$
\begin{array} { l } { { \Delta \alpha = 0 ; 3 2 0 0 { \frac { \rho } { a } } \cos \phi ^ { \prime } \cos { H } \sec \delta , } } \\ { { \Delta \delta = 0 ; 3 2 0 0 { \frac { \rho } { a } } \cos \phi ^ { \prime } \sin { H } \sin \delta , } } \end{array}
$$

where $H$ is the hour angle. The effect is small but is of importance for accurate observations. For a star at transit, $h = 0 ^ { \circ }$ or $1 8 0 ^ { \circ }$ , so $\Delta \delta$ is zero, but

$$
\Delta \alpha = \pm 0 ! 3 2 0 0 { \frac { \rho } { a } } \cos \phi ^ { \prime } ,
$$

where the plus and minus signs are used for upper and lower transits, respectively;   
this may be regarded as a correction to the time of transit.

Alternatively, the effect may be computed in rectangular coordinates using the following expression for the geocentric velocity vector $\mathrm { d } \mathbf { r } / \mathrm { d } t$ of the observer with respect to the celestial equatorial reference frame of date

$$
\frac { \mathrm { d } \mathbf { r } } { \mathrm { d } t } = \left( \begin{array} { c } { - \omega \rho \cos \phi ^ { \prime } \sin ( \theta + \lambda ) } \\ { \omega \rho \cos \phi ^ { \prime } \cos ( \theta + \lambda ) } \\ { 0 } \end{array} \right)
$$

where $\theta$ is the Greenwich sidereal time, or stellar angle (see Section 10.4), and $\lambda$ is the longitude of the observer (East longitudes are positive).

The geocentric velocity vector of the observer is added to the barycentric velocity of the Earth’s center, to obtain the corresponding barycentric velocity vector of the observer. This procedure is valid insofar as the accuracy required permits the use of the Newtonian law of addition of velocities. At a microarcsecond accuracy, the addition of vectors should be performed in the barycentric reference frame and the Lorentz vector addition formulae (Section 5.2.3) should be applied.

In the case of observations that are performed from an artificial satellite, the diurnal aberration must be replaced by the orbital aberration. Since in general, there is no accurate analytical representation of the motion of the satellite and the velocity $\mathrm { d } \mathbf { r } / \mathrm { d } t$ is provided in interpolatable numerical form, the latter procedure is the only one possible.

If observations are performed from a space probe, the velocity vector $\mathbf { V }$ of the probe is given in barycentric coordinates. The procedure is then the same as the one described for annual aberration, $\mathbf { V }$ replacing the velocity of the center of mass of the Earth.

# 6.3.7 Planetary aberration

Planetary aberration is the displacement of the observed position of a celestial body produced by both the motion of the body and the motion of the Earth.

Let us denote the barycentric position of the Earth, $E$ , as a function of the barycentric time $t$ by $\mathbf { E _ { B } } ( t )$ , and the barycentric position of a planet, $P$ , by $\mathbf { P _ { B } } ( t )$ . If the observation of $P$ takes place at the time $t _ { 0 }$ , $P$ is seen at the place ${ \bf P _ { B } } ( t _ { 0 } - \tau )$ , where $\tau$ is the light-time, that is the time taken by the light to travel from $P$ to $E$ . The light-time, assuming a Newtonian space-time, is then given by

$$
\tau = | \mathbf { P _ { B } } ( t _ { 0 } - \tau ) - \mathbf { E _ { B } } ( t _ { 0 } ) | / c .
$$

This equation can be solved assuming that one has an ephemeris of the variation of $\mathbf { P _ { B } }$ with time. This is the case, except for newly discovered objects, for which an orbit must be first determined. It is then sufficient to assume that the first and second derivatives are known:

$$
\mathbf { P _ { B } } ( t _ { 0 } - \tau ) = \mathbf { P _ { B } } ( t _ { 0 } ) - \frac { \mathrm { d } ( \mathbf { P _ { B } } ) } { \mathrm { d } t } ( \tau ) + \frac { 1 } { 2 } \frac { \mathrm { d ^ { 2 } } ( \mathbf { P _ { B } } ) } { \mathrm { d } t ^ { 2 } } ( \tau ) ^ { 2 } .
$$

Equations (6.36) and (6.37) can be solved by successive approximations. The planetary aberration is the geocentric angle between two vectors:

$$
\begin{array} { r } { ( { \bf E _ { B } } ( t _ { 0 } ) { \bf P _ { B } } ( t _ { 0 } ) , ~ { \bf E _ { B } } ( t _ { 0 } ) { \bf P _ { B } } ( t _ { 0 } - \tau ) ) . } \end{array}
$$

![](images/8d43f3e96c88c99e2e512d87eef640825f8f54f8f16e607a7fc6707e720bad31.jpg)  
Fig. 6.4. Internal and external contacts for the transit of $P$ in front of $S$ .

This expression should be eventually corrected for light deflection and retardation described in the following sections, accounting for the actual relativistic space-time in the Solar System.

If ultimate accuracy is not required, one may assume, as in the Newtonian case, that the vector velocities of $E$ and $P$ can be added. The consequence would be that the aberration effects on the Earth and the planet can be computed independently and then added. This amounts to adding the correction for stellar aberration to the geometric position of the planet corrected for light-time. The error introduced in this simpler procedure can amount to a few milliarcseconds.

# 6.3.8 Differential planetary aberration

Aberration, because of its dependence on the relative motions and distances, sometimes has complex effects, where two or more bodies are involved, as, for instance, in eclipses, transits, and the phenomena of satellite systems; and on some past occasions, the determination of these effects has presented an intricate problem.

In a transit of a planet across the disk of the Sun, for example, the external contacts occur when the observer is on the conical surface that circumscribes the Sun and the planet and has its vertex between the Sun and the planet. The internal contacts occur when the observer is on the cone circumscribing the planet and the Sun (S) and has its vertex between the planet $( P )$ and the Earth (Fig. 6.4). The observed contacts are at the instants when the apparent positions of a point on the limb of the planet and a point on the limb of the Sun are the same; i.e. the ray of light from the Sun, that reaches the geometric position of the observer at the instant $T$ of contact, has grazed the planet on the way. Let $\tau _ { 2 }$ be the light-time between the limb of the Sun and the observer, and $\tau _ { 1 }$ the light-time between the limb of the Sun and the limb of the planet. This ray left the Sun at a previous time $T - \tau _ { 2 }$ and reached the planet at time $( T - \tau _ { 2 } ) + \tau _ { 1 }$ . The circumscribing cones are formed by the grazing rays; hence, the points on the Earth and the planet that lie in the same straight line on one of the cones at the instant of a contact, are the geometric position of the observer at the time $T$ , and the geometric position of the point on the planet at time $T - \tau _ { 2 } + \tau _ { 1 }$ . Therefore, in the formulas of the theory of transits, for any value of the time $T$ , all quantities depending on the time must be derived from the values of the barycentric coordinates $( r , l , b )$ of the planet at $T - \tau _ { 2 } + \tau _ { 1 }$ , and the barycentric coordinates $( \boldsymbol { r } ^ { \prime } , \boldsymbol { l } ^ { \prime } , \boldsymbol { b } ^ { \prime } )$ of the Earth at time $T$ .

Similarly, in comparing observed positions of objects in the Solar System with one another, or with reference stars, in order to determine the coordinates of a body, great care is required in correcting the observations for aberration, according to the means of observation used, and the method of comparison.

In eclipsing binary systems, an apparent variation of the period may be produced by the variation in light-time with the changing distance from the observer, owing to an orbital motion of the eclipsing pair resulting from a distant third component (see Section 12.6).

# 6.4 Relativistic light deflection

As shown in Section 5.4.2, the light travels in space on a path that depends on the distribution of masses. To describe it, it is sufficient to treat bodies in the Solar System as point masses.

# 6.4.1 The light path

Let us compute the path of light under the influence of a body of mass $M$ and in particular the Sun. It is described by the parametrized Equations (5.35). It was already shown that it follows a curve on a plane. So we shall study it in polar coordinates $( r , \lambda )$ centered at the point mass. Let us repeat the equations:

$$
\begin{array} { c } { { \left( \displaystyle \frac { \mathrm { d } r } { \mathrm { d } p } \right) ^ { 2 } = \left( 1 - \displaystyle \frac { 2 m ^ { 2 } } { r ^ { 2 } } \right) c ^ { 2 } k ^ { 2 } - \left( 1 - \displaystyle \frac { 2 m } { r } \right) \displaystyle \frac { h ^ { 2 } } { r ^ { 2 } } , } } \\ { { \displaystyle \frac { \mathrm { d } \lambda } { \mathrm { d } p } = \displaystyle \frac { h } { r ^ { 2 } } , } } \end{array}
$$

where $h$ and $k$ are the generalized angular momentum and energy integrals, and $m = G M / c ^ { 2 }$ . It is convenient to introduce a new variable $u = 1 / r$ and eliminate $\mathrm { d } p$ between the two equations, so that

$$
\left( { \frac { \mathrm { d } u } { \mathrm { d } \lambda } } \right) ^ { 2 } = \left( { \frac { \mathrm { d } u } { \mathrm { d } r } } { \frac { \mathrm { d } r } { \mathrm { d } p } } { \frac { \mathrm { d } p } { \mathrm { d } \lambda } } \right) ^ { 2 } = { \frac { 1 } { r ^ { 4 } } } { \bigg ( } { \frac { \mathrm { d } r } { \mathrm { d } p } } { \bigg ) } ^ { 2 } { \frac { r ^ { 4 } } { h ^ { 2 } } } = { \frac { 1 } { h ^ { 2 } } } { \bigg ( } { \frac { \mathrm { d } r } { \mathrm { d } p } } { \bigg ) } ^ { 2 } ,
$$

and, finally,

$$
\left( { \frac { \mathrm { d } u } { \mathrm { d } \lambda } } \right) ^ { 2 } = ( 1 - 2 m ^ { 2 } u ^ { 2 } ) { \frac { c ^ { 2 } k ^ { 2 } } { h ^ { 2 } } } - ( 1 - 2 m u ) u ^ { 2 } .
$$

It is important to evaluate the contribution of $2 m ^ { 2 } u ^ { 2 }$ to the first term. In the case of the Sun,

$$
\begin{array} { r } { G M = 1 . 3 2 7 1 2 4 \times 1 0 ^ { 2 0 } \mathrm { m } ^ { 3 } / \mathrm { s } ^ { 2 } , } \\ { c ^ { 2 } = 8 . 9 8 7 5 5 4 \times 1 0 ^ { 1 6 } \mathrm { m } ^ { 2 } / \mathrm { s } ^ { 2 } , } \end{array}
$$

hence, $m = 1 4 7 6 . 6 2 \mathrm { m }$ .

No star can be observed at a distance from the center of the Sun that is less than the Sun’s apparent radius, which is $R _ { \odot } = 1 / U _ { \odot } = 6 . 9 6 \times 1 0 ^ { 8 } \mathrm { m }$ . So, $m U _ { \odot } =$ $0 . 2 1 2 \times 1 0 ^ { - 5 }$ and $m ^ { 2 } u ^ { 2 } < 5 \times 1 0 ^ { - 1 2 }$ , and can be neglected with respect to 1. Hence, (6.41) reduces to

$$
\left( { \frac { \mathrm { d } u } { \mathrm { d } \lambda } } \right) ^ { 2 } = K ^ { 2 } - u ^ { 2 } + 2 m u ^ { 3 } ,
$$

where $K ^ { 2 }$ is a constant that is determined by the condition that, at the minimum distance $R$ of the light ray to the central mass, one has $\mathrm { d } u / \mathrm { d } \lambda = 0$ . Finally, setting $V = 1 / R$ ,

$$
K ^ { 2 } = 1 / R ^ { 2 } - 2 m / R ^ { 3 } = V ^ { 2 } - 2 m V ^ { 3 } .
$$

Ultimately, the equation of the light path is:

$$
\left( { \frac { \mathrm { d } u } { \mathrm { d } \lambda } } \right) ^ { 2 } = V ^ { 2 } - 2 m V ^ { 3 } - u ^ { 2 } + 2 m u ^ { 3 } .
$$

If $m = 0$ , the path is given by the reduced Equation (6.42):

$$
\left( { \frac { \mathrm { d } u } { \mathrm { d } \lambda } } \right) ^ { 2 } = V ^ { 2 } - u ^ { 2 } .
$$

Here, $\lambda$ is made to vary from 0 to $\pi$ when $r$ varies from $- \infty$ to $+ \infty$ . It is easy to verify that the solution of (6.43) is a straight line defined, in polar cordinates centered at the Sun by

$$
r = { \frac { R } { \sin \lambda } } .
$$

Now, with regard to the full Equation (6.42), let us consider that the solution is a perturbed solution of (6.43), and write

$$
R u = \sin \lambda + m F ( \lambda ) .
$$

Let us call $F ^ { \prime } ( \lambda )$ , the derivative with respect to $\lambda$ . Differentiating (6.44), one gets

$$
\frac { \mathrm { d } u } { \mathrm { d } \lambda } = \frac { \cos \lambda } { R } + \frac { m } { R } F ^ { \prime } ( \lambda ) ,
$$

and

$$
\left( { \frac { \mathrm { d } u } { \mathrm { d } \lambda } } \right) ^ { 2 } = { \frac { \cos ^ { 2 } \lambda } { R ^ { 2 } } } + { \frac { 2 m } { R ^ { 2 } } } F ^ { \prime } ( \lambda ) \cos \lambda .
$$

Let us now substitute the expression (6.44) into Equation (6.42) where we have replaced $V$ and $K ^ { 2 }$ by functions of $1 / R$ . One obtains, neglecting terms in $m ^ { 2 }$ ,

$$
\left( \frac { \mathrm { d } u } { \mathrm { d } \lambda } \right) ^ { 2 } = \left( \frac { 1 } { R ^ { 2 } } - \frac { 2 m } { R ^ { 3 } } \right) - \frac { \sin ^ { 2 } \lambda } { R ^ { 2 } } - \frac { 2 m } { R ^ { 2 } } \sin \lambda F ( \lambda ) + \frac { 2 m } { R ^ { 3 } } \sin ^ { 3 } \lambda .
$$

Equating the two expressions (6.45) and (6.46), one gets, after some simplifications,

$$
\frac { 2 m } { R ^ { 2 } } F ^ { \prime } ( \lambda ) \cos \lambda = - \frac { 2 m } { R ^ { 3 } } - \frac { 2 m } { R ^ { 2 } } \sin \lambda F ( \lambda ) + \frac { 2 m } { R ^ { 3 } } \sin ^ { 3 } \lambda .
$$

Finally, dividing by $2 m / R ^ { 2 } \cos \lambda$ , one obtains the differential equation giving $F ( \lambda )$

$$
{ \frac { \cos \lambda F ^ { \prime } ( \lambda ) + \sin \lambda F ( \lambda ) } { \cos ^ { 2 } \lambda } } = { \frac { \mathrm { d } } { \mathrm { d } \lambda } } \left( { \frac { F ( \lambda ) } { \cos \lambda } } \right) = { \frac { \sin ^ { 3 } \lambda - 1 } { R \cos ^ { 2 } \lambda } } .
$$

This equation is easily integrable, and the result is

$$
F ( \lambda ) = \frac { 1 } { R } ( 1 + \cos ^ { 2 } \lambda - \sin \lambda + C \cos \lambda ) ,
$$

where $C$ is the constant of integration to be determined. Inserting this result into Equation (6.44), one gets

$$
u = \frac { 1 } { r } = \frac { \sin \lambda } { R } \left( 1 - m / R \right) + \frac { m } { R ^ { 2 } } ( 1 + \cos ^ { 2 } \lambda + C \cos \lambda ) .
$$

The second part of the equation is small with respect to the first, so that one can put it as a factor, and develop the inverse of $u$ to the first order of $m$ :

$$
r = \frac { R } { ( 1 - m / R ) \sin \lambda } - m \left( \frac { 1 + C \cos \lambda + \cos ^ { 2 } \lambda } { \sin ^ { 2 } \lambda } \right) .
$$

Let us first remark, that the reference straight path is slightly shifted towards the Sun (Fig. 6.5). In order to determine the value of the constant of integration $C$ , let us note that we have assumed that the gravitational field of the Sun is isotropic. It results that the path is symmetrical with respect to the line of its closest approach to the Sun $\lambda = 9 0 ^ { \circ }$ ) so that $F ^ { \prime } ( \pi / 2 )$ must be zero. This sets $C = 0$ , and, in conclusion,

![](images/1bbf36a757ee3f5edec352e20ec389523fdf1217e9e67c1200d7872f0bc36fd8.jpg)  
Fig. 6.5. The light path $C _ { 1 } C _ { 2 }$ and its closest approach $H$ from the central mass $o$ at a distance $R$ . The apparent direction of a star $G$ before bending is along the asymptote $S _ { 1 }$ and after bending it is along the asymptote $S _ { 2 }$ , the deflection angle being $\varDelta$ . If the observer is in $A$ or $B$ , the directions of rays emitted by the star are respectively $S _ { A }$ and $S _ { B }$ , and the deflections are $\varDelta _ { A }$ and $\varDelta _ { B }$ .

the distance from the Sun is

$$
r = \frac { R } { ( 1 - m / R ) \sin \lambda } - m \left( \frac { 1 + \cos ^ { 2 } \lambda } { \sin ^ { 2 } \lambda } \right) .
$$

# 6.4.2 Deflection of light for a star

The curvature of the light path implies that the direction from which the light hits the observer is not the direction from which it was emitted. Let us first assume that the observer is at infinity. Then, the light path has two asymptotes (Fig. 6.5); one in the direction of the emitter, the other of the observer. They correspond to the values of $\lambda$ for which $1 / u  \infty$ . Following (4.48), this corresponds to

$$
\sin \lambda ( 1 + m ) + \frac { m } { R } ( 1 + \cos ^ { 2 } \lambda ) = 0 ,
$$

which, to the first order of $m$ , gives $\lambda = 2 m / R$ or $\pi - 2 m / R$ . The total deviation, returning to the definition of $m$ is therefore

$$
\Delta \lambda = { \frac { 4 G M } { R c ^ { 2 } } } .
$$

Taking the numerical values for $R _ { \odot }$ of the Sun given above, the total deflection for a Sun grazing ray is $ { \Delta _ { \odot } } = 0 . 8 4 8 6 \times 1 0 ^ { - 5 }$ rad, or $1 ^ { \prime \prime } 7 5$ .

Let us now assume that the observer, $A$ , is a point on the path defined by the angle $\lambda$ between the undisturbed direction and the direction of $A$ as seen from the Sun, $o$ (Fig. 6.5) used in the previous derivations. We do not give the derivation

![](images/b04d0cc063efd5e2faa2f00e794a934f4c163fb4cdafef57680f8d66f5692915.jpg)  
Fig. 6.6. Position of the unit vector $\mathbf { d }$ of the direction of the deviation in the Sun–Earth–star (OES) plane.

of the deflection, which is rather lengthy. It can be found in Will (1974) or Soffel (1989). The result is

$$
\begin{array} { l } { \displaystyle \varDelta _ { A } ( \lambda ) = \frac { 4 G M } { R c ^ { 2 } } \left( \frac { 1 - \cos \lambda } { 2 } \right) = \frac { 2 G M } { r c ^ { 2 } } \left( \frac { 1 - \cos \lambda } { \sin \lambda } \right) } \\ { \displaystyle = \frac { 2 G M } { r c ^ { 2 } } \left( \frac { \sin \lambda } { 1 + \cos \lambda } \right) = \frac { 2 G M } { r c ^ { 2 } } \tan \lambda / 2 , } \end{array}
$$

where $r$ is the distance of the observer to the Sun $( R = r \sin \lambda$ ).

However, $\lambda$ is not a directly observable quantity. It is preferable to use the angular elongation, $\psi$ , of the star from the Sun. To an accuracy of the order of the square of the deflection, one has $\psi = \pi - \lambda$ , and the deflection is

$$
\Delta _ { A } ( \psi ) = { \frac { 4 G M } { R c ^ { 2 } } } \left( { \frac { 1 + \cos \psi } { 2 } } \right) = { \frac { 2 G M } { r c ^ { 2 } } } \cot \psi / 2 .
$$

This deviation must now be expressed as variations of the coordinates $\alpha$ and $\delta$ of the star. In the Sun–Earth–star $( O E S )$ plane already considered, the unit vector, $\mathbf { d } = \mathbf { E } \mathbf { K }$ , of the deviation is perpendicular to ES in the direction of the half-plane including the Sun (Fig. 6.6). Let e and $\mathbf { p }$ be the unit vectors of OE and ES respectively. Finally, let $H$ be the point on $O E$ , such that the projection of $E H$ on $\mathbf { d }$ is $K$ . Then, one can see from the figure that

$$
\mathbf { d } = { \frac { - \mathbf { e } } { \sin \lambda } } + \mathbf { p } \cot \lambda .
$$

The angular components of the deviation are obtained by multiplying this expression

by the expression (6.50). One gets

$$
{ \boldsymbol { \mathbf { D } } } = { \frac { 2 G M } { r c ^ { 2 } } } { \frac { \sin \lambda } { 1 + \cos \lambda } } \left( { \frac { - \mathbf { e } } { \sin \lambda } } + \mathbf { p } \cot \lambda \right) = { \frac { 2 G M } { r c ^ { 2 } } } \left( { \frac { - \mathbf { e } + \mathbf { p } \cos \lambda } { 1 + \cos \lambda } } \right) .
$$

Note that the minus sign corresponds to the fact that the deflection is always in the direction of the Sun, while e is in the opposite direction. In computing the actual deflection on the sky, the contribution of the $\mathbf { p }$ component, directed towards the star, is zero. One is left with

$$
\mathbf { D } = { \frac { 2 G M } { r c ^ { 2 } } } { \frac { - \mathbf { e } } { 1 + \cos \lambda } } = { \frac { 2 G M } { r c ^ { 2 } } } { \frac { - \mathbf { e } } { 1 - \cos \psi } } ,
$$

where $\psi$ is the elongation of the star from the Sun $( \alpha _ { \odot } , \delta _ { \odot } )$ , given by

$$
\cos \psi = \sin \delta \sin \delta _ { \odot } + \cos \delta \cos \delta _ { \odot } \cos ( \alpha - \alpha _ { \odot } ) .
$$

The modified coordinates of the star are then (Seidelmann, 1992),

$$
\begin{array} { l } { \displaystyle \Delta \alpha = \frac { 2 G M } { r c ^ { 2 } } \frac { \cos \delta _ { \odot } \sin ( \alpha - \alpha _ { \odot } ) } { ( 1 - \cos \psi ) \cos \delta } } \\ { \displaystyle \Delta \delta = \frac { 2 G M } { r c ^ { 2 } } \frac { \sin \delta \cos \delta _ { \odot } \cos ( \alpha - \alpha _ { \odot } ) - \cos \delta \sin \delta _ { \odot } } { 1 - \cos \psi } . } \end{array}
$$

# 6.4.3 Deflection of light for planets

In the case of planets at a finite distance from the Earth, $\psi$ and $\lambda$ are no more equal, and Equations (6.50) and (6.51) are not equivalent. The formula representing the light deflection is (6.50), a function of $\lambda$ . Figure 6.7 shows the geometry in the triangle Sun–Earth–planet $( O E P )$ , the angles $\psi , \lambda$ and the third angle, $\zeta$ in $P$ . Let $K$ be the origin of the unit vector, $\mathbf { K O } = \mathbf { d }$ , of the direction of the deviation and $H$ the intersection of the parallel to $O P$ drawn from $K$ with $O E$ . One has

$$
\mathbf { d } = \mathbf { H } \mathbf { O } + \mathbf { K } \mathbf { H } .
$$

In the triangle $O H K$ , the angles can be expressed easily in $\lambda$ , $\psi$ , and $\zeta$ as shown in the figure. Let us apply the sine relations in this triangle:

$$
{ \frac { K H } { \cos \psi } } = { \frac { O H } { \cos \zeta } } = { \frac { O K } { \sin \lambda } } ,
$$

and, since $O K = 1$ , one has

$$
K H = { \frac { \cos \psi } { \sin \lambda } } \quad { \mathrm { a n d } } \quad O H = { \frac { \cos \zeta } { \sin \lambda } } .
$$

![](images/dae08c87c6acbc1476a65914b928ff13a5eb2098f98e7692ed1426583e500099.jpg)  
Fig. 6.7. Position of the unit vector $\mathbf { d }$ of the direction of the deviation in the Sun–Earth–planet (OEP) plane.

The lengths of the vectors in (6.55) being determined, the formula becomes

$$
\mathbf { d } = - { \frac { \mathbf { q } \cos \zeta + \mathbf { e } \cos \psi } { \sin \lambda } } .
$$

The angular components of the deviation are obtained by multiplying this expression by the magnitude of the deflection given by formula (6.50):

$$
{ \bf D } = - \frac { 2 G M } { r c ^ { 2 } } \left( \frac { \sin \lambda } { 1 + \cos \lambda } \right) \frac { { \bf q } \cos \zeta + { \bf e } \cos \psi } { \sin \lambda } = - \frac { 2 G M } { r c ^ { 2 } } \frac { { \bf q } \cos \zeta + { \bf e } \cos \psi } { 1 + \cos \lambda } .
$$

The determination of the modified coordinates is to be performed in the same manner as in the case of stars.

# 6.4.4 Gravitational deflection by stars or quasars

The light emitted by some distant star and grazing another celestial body is deviated in the manner described above, irrespective of whether it is a star or another massive object. If the emitting object moves with a constant proper motion, the apparent path as well as its luminosity are modified by the massive object. For this reason, the deflector is also called a gravitational lens. Let us first consider a point-like star, $S$ , exactly aligned with the deflector, $L$ , of mass $M$ , and the observer, $o$ . The light is deviated by the same amount in all directions, and the image of $S$ , as seen from $o$ , is a circle, called an Einstein circle or ring. To describe the path of a ray in a plane passing by $S , L$ , and $o$ , it is legitimate to represent the nonlinear part by a point, $H$ , since it is very short in comparison with distances between stars (upper part of Fig. 6.8). Let $R _ { 1 }$ and $R _ { 2 }$ be the distances $S L$ and $O L$ respectively, with $R = R _ { 1 } + R _ { 2 }$ . Let also $D = L H$ be the Einstein distance, that is the distance between $L$ and the ray emitted by $S$ and received by $o$ .

![](images/b9959befb791baada65a3ddc8c6cd560ac5c86fcb4dd0269795ba2066bc85322.jpg)  
Fig. 6.8. The deflection of the light emitted by $S$ by the lens $L$ . The upper part of the figure represents the situation when the observer $o$ is aligned with $L S$ . In the lower part of the figure, $S$ is shifted.

The angle $\varDelta$ between the rays is the total deviation given by (6.45). But it is also, in the triangle $O H S$ , the sum of the small angles $\alpha = D / R _ { 1 }$ and the $\beta = D / R _ { 2 }$ under which $L H$ is seen from $S$ and $o$ respectively:

$$
\varDelta = \frac { 4 G M } { c ^ { 2 } D } = \frac { D } { R _ { 1 } } + \frac { D } { R _ { 2 } } ,
$$

from which one obtains the distance $D$ ,

$$
D = \left( \frac { 4 G M } { c ^ { 2 } } \frac { R _ { 1 } R _ { 2 } } { R _ { 1 } + R _ { 2 } } \right) ^ { 1 / 2 } .
$$

The radius of the Einstein circle is, therefore,

$$
\beta = \frac { D } { R _ { 2 } } = \left( \frac { 4 G M } { c ^ { 2 } } \frac { R _ { 1 } } { R R _ { 2 } } \right) ^ { 1 / 2 } .
$$

Suppose now that $S$ is not aligned with $O L$ as shown in the lower part of Fig. 6.8. The light is deflected in $H$ . Let $I$ be the point on the deviated ray at the distance of $S$ from $o$ . Let $H ^ { \prime }$ be the intersection of $L H$ with $O S$ . The deflection angle $\varDelta$ is

$$
\varDelta = \frac { I S } { R _ { 1 } } .
$$

One sees on the figure that

$$
\frac { I S } { H H ^ { \prime } } = \frac { O P } { O L } = \frac { R } { R _ { 2 } } ,
$$

![](images/99acee10f32bfe437a5361f27835ea0b1c676325927061c0a6695e9d85b21200.jpg)  
Fig. 6.9. Gravitational arcs in the cluster of galaxies Abell 2218 (Hubble Space Telescope). Material created with support from AURA/STScI under NASA contract NAS5-26555.

so that, introducing this in expression (6.59) for $\varDelta$ , and setting $H H ^ { \prime } = D + D ^ { \prime }$ , where $D ^ { \prime } = L H ^ { \prime }$ , one gets

$$
{ \frac { 4 G M } { D c ^ { 2 } } } = ( D + D ^ { \prime } ) { \frac { R } { R _ { 1 } R _ { 2 } } } .
$$

This is a second-order equation in $D$ , which can be written as

$$
D ^ { 2 } + D D ^ { \prime } = { \frac { 4 G M } { c ^ { 2 } } } { \frac { R _ { 1 } R _ { 2 } } { R } } .
$$

The right-hand term is precisely the square of the Einstein distance (6.57). Expressed as a function of the Einstein radius $\beta$ , it becomes

$$
D ^ { 2 } + D D ^ { \prime } = \beta ^ { 2 } R _ { 2 } ^ { 2 } .
$$

There are two solutions, corresponding to each side of the deflector. As seen from the observer, calling $\gamma$ the angle between the directions of $L$ and $S$ as seen from $o$ , the angular directions $( \theta = D / R _ { 2 }$ ) from $L$ of the two images are given by

$$
\theta = 0 . 5 [ \gamma \pm ( \gamma ^ { 2 } + 4 \beta ^ { 2 } ) ^ { 1 / 2 } ] .
$$

Note that one of the images is inside the Einstein circle and the other is outside it.

If $S$ is not point-like, the shape is a more or less developed arc, a very common feature among clusters of galaxies (Fig. 6.9). If, in addition, $S$ is an extended source with an irregular shape, the gravitational lensing produces complicated bright structures. Now, assume that $S$ moves with an apparent proper motion, $\mu$ , with respect to $L$ and parallel to an $L x$ axis. Taking the origin of time at the moment of the closest approach at the distance $D$ along $L y$ (Fig. 6.8); the true positions of $S$ are represented by

$$
x = \mu t ; \qquad y = D .
$$

![](images/a5167d14098a4882fc0af7aaa7fc37748894cf00699214ebaa85ecfc8f254030.jpg)  
Fig. 6.10. Apparent paths $S ^ { \prime }$ and $S ^ { \prime \prime }$ of $S$ when passing close behind the object $L$ .

At some time $t$ , the two apparent positions $S ^ { \prime }$ and $S ^ { \prime \prime }$ of $S$ are given by (6.63) with the distance

$$
\gamma = L S = { \sqrt { D ^ { 2 } + \mu ^ { 2 } t ^ { 2 } } } = D \sec \psi ,
$$

along the $S L$ line. The shapes of the paths are drawn in Fig. 6.10. An analysis of the apparent motion of the outer component as a function of time shows that it is accelerated when it approaches the vicinity of $L$ , and decelerated when it leaves it. A rough estimate of the time necessary to observe these paths is given by the Einstein Time, $T _ { \mathrm { E } }$ , which is the time taken by $S$ to travel the radius of the Einstein circle, in years

$$
T _ { \mathrm { E } } = { \frac { 3 9 0 } { \mu } } { \frac { M R _ { \mathrm { 1 } } } { R R _ { \mathrm { 2 } } } } ,
$$

where $M$ is expressed in solar masses, the distances in kiloparsecs (kpc), and the proper motion $\mu$ in mas per year. With the same units, the radius of the Einstein circle $\beta$ , in mas, is given by

$$
\beta = 2 . 7 \frac { M R _ { 1 } } { R R _ { 2 } } .
$$

Example. Taking $R _ { 2 } = 1 \mathrm { k p c }$ , $R = 3 \mathrm { k p c }$ , a one solar mass lens, and a relative proper motion of $S$ with respect to $L$ equal to $2 0 \mathrm { k m } / \mathrm { s }$ , one has

$$
\beta = 1 . 8 \mathrm { m a s } ; \qquad T _ { \mathrm { E } } = 1 \mathrm { m o n t h } .
$$

This shows that, if the detection of gravitational lensing in stars is still difficult, it will be within easy reach for microarcsecond astrometry.

Another property of the gravitational lenses is the magnitudes of the images. The lensing preserves the surface brightness, so that the magnification $A$ is given, in a first approximation by the ratio of image to source areas:

$$
A = \left| { \frac { \gamma } { \theta } } { \frac { \mathrm { d } \gamma } { \mathrm { d } \theta } } \right| .
$$

Following Schneider et al. (1992), one has

$$
A _ { \pm } = \frac { u ^ { 2 } + 2 } { 2 u \sqrt { u ^ { 2 } + 4 } } \pm \frac 1 2 ,
$$

where $\pm$ corresponds to one or the other solution of (6.63) and $u = \gamma / \beta$ .

These characteristics of the disturbed proper motion of a star are used in attempts to recognize the presence of MACHOS (massive compact halo objects) that may exist in the outskirts of our Galaxy. They are also used very much in probing the distant Universe, particularly when there is a large magnification of the distant object. More detailed information can be found in Paszy´nski (1996) and Schneider et al. (1992).

# 6.5 Retardation of light

Deflection is not the only effect of the gravitational field on electro-magnetic radiation. Locally, measured with proper time, the speed of light is an invariant $( c )$ . But this is not the case if it is measured in coordinate time, which is a simple consequence of the gravitational time dilatation described by Equation (5.24). We shall consider here, as we did for light deflection, the gravitational effect of a central mass and neglect terms of order three or more in $1 / c$ . The light follows a geodesic defined by $\mathrm { d } s ^ { 2 } = 0$ . Introducing again $m = G M / c ^ { 2 }$ , we have

$$
\mathrm { d } s ^ { 2 } = - \mathrm { d } \tau ^ { 2 } = 0 = - \left( 1 - \frac { 2 m } { r } \right) c ^ { 2 } \mathrm { d } t ^ { 2 } + \left( 1 + \frac { 2 m } { r } \right) ( \mathrm { d } x ^ { 2 } + \mathrm { d } y ^ { 2 } + \mathrm { d } z ^ { 2 } ) .
$$

We neglect the effect of the light deflection on the retardation (it is a second-order effect), and assume a rectilinear path along the line $H E$ at the minimum distance $O H = R$ from the central object as shown in Fig. 6.6. The $\mathrm { d } s ^ { 2 }$ becomes

$$
0 = - \left( 1 - { \frac { 2 m } { r } } \right) c ^ { 2 } \mathrm { d } t ^ { 2 } + \left( 1 + { \frac { 2 m } { r } } \right) \mathrm { d } z ^ { 2 } ,
$$

from which one obtains the time of travel $t$ between points of abscissæ $z _ { 1 }$ and $z _ { 2 }$

$$
t = \frac { 1 } { c } \int _ { z _ { 1 } } ^ { z _ { 2 } } \sqrt { \frac { ( 1 + 2 m / r ) } { 1 - 2 m / r } } \mathrm { d } z .
$$

Developing this expression, neglecting terms in $m ^ { 2 }$ , and replacing $r$ by $\sqrt { R ^ { 2 } + z ^ { 2 } }$ , gives

$$
t = \frac { 1 } { c } ( z _ { 2 } - z _ { 1 } ) + \frac { 1 } { c } ( z _ { 2 } - z _ { 1 } ) \int _ { z _ { 1 } } ^ { z _ { 2 } } \frac { 2 m } { \sqrt { R ^ { 2 } + z ^ { 2 } } } \mathrm { d } z
$$

The first term represents the travel time with a velocity $c$ . What is left is the extratime delay $\Delta t$ . As in the case of the deflection, it is advisable to split the effect and compute it systematically from the point of closest approach corresponding to $z = 0$ . Returning to the initial notations and performing the integration, one gets:

$$
\Delta t ( 0 , z ) = \frac { 2 G M } { c ^ { 3 } } \ln \frac { | z | + \sqrt { z ^ { 2 } + R ^ { 2 } } } { R } .
$$

If now we assume that $R / z$ is small and can be neglected, this reduces to

$$
\Delta t ( 0 , z ) = \frac { 2 G M } { c ^ { 3 } } \ln \frac { 2 z } { R } .
$$

The total retardation between two points $z _ { 1 }$ and $z _ { 2 }$ is, according to the respective positions of these points and $H$ ,

$$
\Delta t ( z _ { 1 } , z _ { 2 } ) = \mid \Delta t ( 0 , z _ { 2 } ) \pm \Delta t ( 0 , z _ { 1 } ) \mid .
$$

To give an example, the additional delay between the limb of the Sun and the Earth is $5 9 . 7 \mu \mathrm { s }$ .

It is to be remarked, at this point, that formula (6.69) is coordinate dependent. It is important that the coordinate system be consistent with the one used to describe the light path. More details on the actual computation of delays can be found in McCarthy (2003), including the additional delays due to the bending of the light ray in space and at the arrival on the Earth. In particular, there is a delay correction $\Delta T$ to be introduced in the measurement of the return time in a laser ranging system. It amounts to

$$
\Delta T = \frac { 2 G M } { c ^ { 3 } } \ln \left( \frac { R _ { 1 } + R _ { 2 } + \rho } { | R _ { 1 } + R _ { 2 } - \rho | } \right) ,
$$

where $R _ { 1 }$ is the distance from the Earth’s center to the beginning of the light path, $R _ { 2 }$ is the distance from the satellite center to the end of the light path, and $\rho$ is the Euclidean distance between the beginning and the ending of the light path.

# 7 Extragalactic reference frame

In Section 1.4 we stated that astrometry must be developed within an extragalactic reference frame to microarcsecond accuracies. The objective of the present chapter is to provide the theoretical and practical background of this basic concept.

# 7.1 International Celestial Reference System (ICRS)

A reference system is the underlying theoretical concept for the construction of a reference frame. In an ideal kinematic reference system it is assumed that the Universe does not rotate. The theoretical background was presented in Section 5.4.1. The reference system requires the identification of a physical system and its characteristics, or parameters, which are determined from observations and that can be used to define the reference system. In 1991 the International Astronomical Union agreed, in principle, to change to a fundamental reference system based on distant extragalactic radio sources, in place of nearby bright optical stars (IAU, 1992; IAU, 1998; IAU, 2001). The distances of extragalactic radio sources are so large that motions of selected objects, and changes in their source structure, should not contribute to apparent temporal positional changes greater than a few microarcseconds. Thus, positions of these objects should be able to define a quasi-inertial reference frame that is purely kinematic. A Working Group was established to determine a catalog of sources to define this frame that is now called the ICRF. The XXIII-rd IAU General Assembly (IAU, 1998) adopted a resolution that:

(i) from 1 January 1998, the IAU celestial reference system shall be the International Celestial Reference System (ICRS) as defined by the International Earth Orientation Service (IERS) ( Arias et al., 1995),   
(ii) the International Celestial Reference Frame (ICRF) shall be the fundamental reference frame as constructed by the IAU Working Group on Reference Frames (Ma and Feissel, 1997),   
(iii) the Hipparcos Catalogue, with the exception of some problem stars (see Section 7.3) shall be the primary realization of the ICRF at optical wavelengths,   
(iv) the ICRF shall be maintained by the IERS, and   
(v) the ICRS shall have its origin at the barycenter of the Solar System, the directions of its axes are fixed with respect to the extragalactic sources and, for continuity with the past and with the FK5 system, aligned with the dynamical system of J2000.0 and the FK5 system of J2000.0, within the errors of the FK5 system.

Specifically, the origin of the right ascensions, the $x$ -axis of the ICRS celestial system, was defined in the initial realization (Arias et al., 1988) by adopting the mean right ascension of 23 radio sources from catalogs compiled by fixing the right ascension of the radio source 3C273B to the usual (Hazard et al., 1971) FK5 value $1 2 { \mathrm { h } } 2 9 { \mathrm { m } } 6 . 6 9 9 7 { \mathrm { s } }$ at J2000.0) (Kaplan et al., 1982). The definitions of the system and the reduction of observations are to be within the framework of general relativity (Chapters 5 and 6).

Actually, the IAU resolutions of the XXIV-th General Assembly introduced two space fixed systems: the Barycentric Celestial Reference System (BCRS) and the Geocentric Celestial Reference System (GCRS), which have been both defined in terms of the metric tensors given in Section 5.3.3 by Equation (5.22). The difference lies in the generalized potentials (Section 5.3.2) that are taken into account. The generalized Lorentz transformation between them, which contains the acceleration of the geocenter and the gravitational potential, is presented in Section 7.6. The ICRS is to be understood as defining the orientation of the axes of both these systems for each of the origins. These axes show no kinematical rotation between them, but they are related by a scale factor and have different time coordinates (TCB and TCG). For example, the metric of the BCRS with barycentric coordinates $( t$ and x) is

$$
\begin{array} { l } { { g _ { 0 0 } = - 1 + \displaystyle \frac { 2 w } { c ^ { 2 } } - \displaystyle \frac { 2 w ^ { 2 } } { c ^ { 4 } } , } } \\ { { \displaystyle g _ { i i } = 1 + \displaystyle \frac { 2 } { c ^ { 2 } } w , } } \\ { { \displaystyle g _ { 0 i } = - \displaystyle \frac { 4 } { c ^ { 3 } } w _ { i } , } } \end{array}
$$

with

$$
\begin{array} { l } { { \displaystyle w ( t , { \bf x } ) = G \sum \mathrm { d } ^ { 3 } x ^ { \prime } \frac { \sigma ( t , { \bf x } ^ { \prime } ) } { | { \bf x } - { \bf x } ^ { \prime } | } + \frac { G } { 2 c ^ { 2 } } \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } \sum \mathrm { d } ^ { 3 } x ^ { \prime } \sigma ( t , { \bf x } ^ { \prime } ) | { \bf x } - { \bf x } ^ { \prime } | } } \\ { { \displaystyle w _ { i } ( t , { \bf x } ) = G \sum \mathrm { d } ^ { 3 } x ^ { \prime } \frac { \sigma ^ { i } ( t , { \bf x } ^ { \prime } ) } { | { \bf x } - { \bf x } ^ { \prime } | } , } } \end{array}
$$

where $\sigma$ and $\sigma ^ { i }$ are the gravitational mass and current densities, respectively, $G$ is

the gravitational constant, $t$ is the TCB (see Section 5.5.2), and $\mathrm { d } ^ { 3 } \boldsymbol { x } ^ { \prime }$ is the element of volume.

A similar expression holds for the definition of the GCRS, the time being the TCG. For more details, see Soffel (2000).

# 7.2 International Celestial Reference Frame (ICRF)

The ICRF is the observed realization of the ICRS for practical applications. It can similarly be geocentric and barycentric. The coordinates of the radio sources are the same in both frames. Coordinates in this frame should be designated right ascension and declination without any further qualification, except for designating the epoch of observations for applying proper motions.

The ICRF is based on 212 defining sources distributed over the entire sky, but only $22 \%$ are in the Southern Hemisphere (Fig. 7.1). The positions, accurate to better than 1 mas, were based on a single solution of 1.6 million VLBI pairs of group delays and phase delay rates data obtained between August 1979 and July 1995. A Working Group selected a list of well-observed and well-behaved sources as the defining sources for this frame and a list of secondary sources (Ma et al., 1998; Johnston et al., 1995). The sources are from three lists:

(i) the most-compact and well-observed 212 defining sources, with a median uncertainty of individual positions of 0.4 mas;   
(ii) compact sources (294) whose positions are likely to improve when more observations are accumulated; and   
(iii) sources (102) less suited for astrometric purposes, but which provide ties for reference frames at other wavelengths.

These sources became the definition and representation of the International Celestial Reference Frame (ICRF). These sources have the advantages that they are very distant, so they have no apparent proper motion, and they have been observed over a long period of time by Very Long Baseline Interferometry (VLBI, see Section 2.4.2), so they have individual accuracies of better than 1 mas. A realization of the frame axes accuracy is estimated at 0.02 mas (Ma and Feissel, 1997). They have the disadvantage that they are optically faint and cannot be easily observed; the optical magnitudes of the defining sources range between 14th and 23rd magnitude, with the majority at 18–19 visual magnitude. So, other catalogs are necessary as realizations of the ICRS for the optical and other wavelengths.

Another disadvantage is that a number of the extragalactic radio sources display structures on spatial scales in the mas range. The spatial structure is usually more compact at higher frequencies. The sources are variable on time scales of weeks to years. An example is given in Fig. 7.2. In this particular instance, the source presents strong modifications of the structure that are not acceptable for astrometric observations. Actually, smaller changes are present in many sources, but generally they do not introduce errors of the order of the uncertainties of the observations. However, this will no longer be the case if observations reach 10 or $2 0 \mu \mathrm { a s }$ precision. So, owing to this variability of the structure of the sources, the positions must be measured over long periods of time, both to determine the ICRF and to maintain it in the future. Geodetic observational programs will be a source of observations in the future, as they have been in the past, but they concern only a limited number of sources. So, in addition, astrometric observations will be needed from VLBI antennas worldwide. Observations for source structure by the VLA or the VLBA will also be needed. Observations for source structure of sources south of $- 2 0 ^ { \circ }$ will be difficult due to the lack of radio telescopes. There are several causes of measurement uncertainties:

![](images/4112a74df547505e7090a3db85fead8257bb7c587548ab6fb856783fdcd13ea4.jpg)  
Fig. 7.1. Distribution (above) of the 212 defining sources of the ICRF and (below) distribution of all the 608 ICRF sources of the three lists (Ma et al., 1998).

![](images/6c91adee965a429d0a26d940a0719f8b15df9252e9e7c25e1a9de7ec8485d290.jpg)  
Fig. 7.2. Variation in the observed structure of the radio source 4C39.25. A new component (b) seems to have been ejected in 1980 (arrow) from the component (c) and to move towards the component (a) with a velocity of $0 . 1 6 \pm 0 . 0 2$ mas/year. The scale is 0.5 mas per interval of graduation (Shaffer and Marscher, 1987).

(i) the propagation of signals in the troposphere causes an error that varies as a function of elevation and azimuth (Section 6.1);   
(ii) the systematic and random portions of the elevation error that can be reduced by mapping functions;   
(iii) the gradients in azimuth cause a North–South asymmetry owing to the greater tropospheric thickness near the equator. This can cause errors of about 0.5 mas in declination.

There are also systematic errors introduced by the software used in the data reduction models for the large set of observational data. Comparisons of solutions in the past have shown discrepancies of about 5 mas. In addition, errors in station locations introduce errors in the source positions of 0.25 mas. The resulting formal uncertainties for ICRF sources are of the order of 0.4–1 mas. This is illustrated by Fig. 7.3, which shows the long history of consistent observations of two ICRF sources. Future observations, better modeling, and improvements in source structure knowledge should reduce these uncertainties. However, source structure and structural motion may set a limit on the precision attainable for the ICRF.

![](images/117fb854b0d81dbc0723fa27e96b34b03e61f265c146421108553726ba23d2b9.jpg)  
Fig. 7.3. Residuals of observations with respect to the IERS solution of one defining source $( 1 3 0 8 + 3 2 6 )$ and one candidate source $( 1 8 0 3 + 7 8 4 )$ (from Ma and Feissel, 1997).

# 7.3 Optical realizations of the ICRF

Previously the fundamental reference frame was based on optical observations of bright stars, primarily made with transit circle type instruments (Section 1.1), and compiled into fundamental catalogs, the most recent being the FK5 (Section 11.5.2). The accuracies of the observations were generally about $0 \% 3$ and of the catalogs were about $0 \% 1$ . Owing to variations in observational histories and accuracies in the Northern and Southern Hemispheres, there were systematic errors in the catalogs. Since these catalogs had been used for a long period, the ICRF was aligned with the FK5 to within the accuracy of the FK5.

The Hipparcos mission (1989–1993) established a global astrometric catalog independent of atmospheric effects and Earth orientation parameters. This catalog is described in Section 11.6.1. It contains 118 218 stars with typical precisions, for stars of magnitude brighter than 9, of 0.8–1 mas in position, proper motion and parallax. This catalog, in addition to being much more accurate than previous catalogs at optical wavelengths, is also not subject to systematic errors based on magnitude and declination zones. However, in contrast to the extragalactic sources, the Hipparcos Catalogue stars display proper motions. Thus, the accuracies of the Hipparcos positions are time dependent and degrade with time from the mean observational epoch of 1991.25. In resolution B1.2, the XXIV-th General Assembly of the IAU established the Hipparcos Catalogue as the optical realization of the ICRS after removing stars that are double, that have been insufficiently observed, or do not have linear proper motions. These are the stars marked as C, G, V, X, and O. This is now the optical realization of the reference frame (Urban et al., 2000b) and is now called International Hipparcos Reference Frame (IHRF).

Owing to the magnitude limit of the Hipparcos observations, the optical counterparts of the defining sources of the ICRF could not be observed directly. Link procedures were adopted to achieve two small rotations fixing the orientation of the Hipparcos Catalogue and removing any global rotation from the proper motions (Lindegren and Kovalevsky, 1995). This link was established using a variety of methods, including VLBI, MERLIN, and VLA observations of radio stars that are also optically bright Hipparcos stars. The most precise contribution was based on VLBI observations of 12 radio stars, which were tied directly to the ICRF. The five astrometric parameters of these stars were determined to better than mas precision (Lestrade et al., 1995). The weighted least-squares solution using all of the methods was able to adjust the Hipparcos Catalogue to the ICRF with uncertainties of 0.6 mas in position and 0.25 mas/year in proper motion at epoch 1991.25 (Kovalevsky et al., 1997).

The Hipparcos Catalogue is limited in the number of stars and the magnitude of stars. The Hipparcos satellite had a separate observational mode called Tycho, which observed many more stars in the same magnitude range as described in Section 11.6.2. Many further catalogs, based on the IHRF have extended the reference to many fainter stars. They are presented in Section 11.7.

# 7.4 Dynamical reference frame tie to the ICRF

Before the ICRS, reference frames were dynamical reference frames constructed assuming that the motions of bodies in the Solar System do not present accelerations that would be reflected in some rotation of the reference system. They were, therefore, based on observations of the planets (essentially inner planets) and the Moon. Lately a mixed stellar–dynamical reference frame was used for the FK5 catalog (Section 11.5.2), which was the official celestial reference frame until 1998. The dynamical reference frame and the FK5 reference frame were aligned as well as possible within their errors for the epoch J2000.0. This was done using the bright star reference frame, the adopted precession constant, and the dynamically determined equinox. In practice, since the ephemerides of the inner planets were based on radar observations and the ephemerides of the outer planets were based on optical observations, there was the possibility of discrepancies between the two systems. Actually, there is a difference between the dynamical equinox, determined from the ephemerides, and the origin, 0 hour right-ascension value, of the FK5 catalog. This difference is also time dependent and was a source of errors in the old system.

The ICRF is a fixed reference frame, and the numerical integration of the ephemerides in the ICRF is performed on a fixed reference frame. Thus, radar and laser ranging observations can be reduced on that frame. The advent of VLBI observations of spacecraft at planets and planetary satellites provides positions directly on the radio reference frame at accuracies of 1–3 mas. CCD observations of planets using the Hipparcos Catalogue give planet and satellite observations on the ICRF at accuracies of about 30 mas (Stone and Dahn, 1995). A joint analysis of VLBI and lunar laser ranging observations provides a tie between the JPL ephemerides and the IERS radio catalogs (Folkner et al., 1994). Thus, the present JPL ephemerides of the planets and the Moon use the ICRF reference frame (Standish et al., 1995).

# 7.5 Transformation between GCRS and BCRS

Since the origin of the geocentric system moves nonlinearly along a geodesic in the barycentric system, but has fixed directions with respect to extragalactic sources, there is a Coriolis-like effect from the relativistic theory of the transformation if referred to the BCRS. Thus, the theory of the transformations between reference frames (Section 5.3.4) must be applied (Brumberg and Groten, 2001). The principal effect is a secular effect, called geodesic precession, which is a rotation of 1.92 mas/year of the geocentric reference system with respect to the barycentric reference system.

The full theory can be found in Brumberg (1991a,b) who gives the following result in the general case of a weak gravitational field for the rotation of a system $B$ in another system $A$ :

$$
\varOmega _ { \mathrm { G } } = \frac { 3 } { 2 } \frac { \mathbf { v } \times U } { c ^ { 3 } } ,
$$

where $U$ is the gravitational potential at $A$ and $\mathbf { V }$ is the velocity of the origin of $A$ . If one assumes the framework of a Schwarzschild field, in which $U$ is a point mass

potential of the Sun (Section 5.3.3, Equation (5.26)), the formulation (Ohanian, 1980) reduces to

$$
\Omega _ { \mathrm { G } } = { \frac { 3 G M } { 2 r ^ { 3 } } } { \frac { \mathbf { r } \times \mathbf { v } } { c ^ { 2 } } } .
$$

Applied to the actual case of an elliptic orbit of the Earth with an eccentricity $e$ , a semi-major axis $a$ , and a mean motion $n$ , the mean value of this expression is (Murray, 1983),

$$
\Omega _ { \mathrm { G } } = \frac { 3 n ^ { 3 } a ^ { 2 } } { 2 r ^ { 3 } c ^ { 2 } \sqrt { ( 1 - e ^ { 2 } ) } } .
$$

The numerical value that is derived for the geodesic precession is

$$
\Omega _ { \mathrm { G } } = 0 . 7 0 1 9 1 9 4 \mathrm { p e r y e a r . }
$$

It is to be noted, that in the equation (7.4), $\mathbf { r }$ and v present periodic variations. They produce periodic changes in the angle of precession and constitute the geodesic nutation. Fukushima (1991) gives the following expression for the precession angle:

$$
\Delta \psi _ { \mathrm { G } } = - 0 \mathrm { { : } } 0 0 0 1 5 3 \sin l ^ { \prime } - 0 \mathrm { { : } } 0 0 0 0 0 2 \sin 2 l ^ { \prime } ,
$$

where $l ^ { \prime }$ is the mean anomaly of the Sun.

The transformation also includes a relation between the geocentric and the barycentric coordinate times (TCB and TCG). It is given by equation (5.39) in Section 5.5.2.

Let us finally mention that there is an equivalent to the geodesic precession in comparing the barycentric and the galactic reference systems. In this case the rate of rotation is of the order of 8.5 nanoarcseconds (nas) per year and is, therefore, negligible (Brumberg, 1991a,b).

# 7.6 ICRF stars at other epochs

The simplistic formulae for transforming a celestial position $( \alpha , \delta$ from epoch $T _ { 0 }$ in the BCRF) to an arbitrary epoch $T$ are:

$$
\begin{array} { c } { \alpha = \alpha _ { 0 } + ( T - T _ { 0 } ) \mu _ { \alpha } } \\ { \delta = \delta _ { 0 } + ( T - T _ { 0 } ) \mu _ { \delta } , } \end{array}
$$

where $\mu _ { \alpha }$ and $\mu _ { \delta }$ are the unreduced proper motion in $\alpha$ and $\delta$ as given in catalogs. This model describes a curved spiraling motion towards one of the poles, while real stars are expected to move along great circles. The difference with respect to a rigorous model is usually very small, but it may become significant near the celestial pole or over long time periods. Thus, while Equation (7.6) should not be used in general applications, it does provide a first-order approximation and an estimate of position uncertainties.

Note that in (7.6), the parallactic correction does not appear. We have assumed there that the transformation is performed in the BCRF. In the geocentric frame (GCRF), one must also correct for the parallax. This is what is done in the following sections. However, it must be kept in mind that, if the epoch transformation is done in the barycentric reference frame, one should omit from the equation the parallactic correction.

The rigorous transformation of parameters can be formulated based on a standard model of stellar motion. The standard model assumes a uniform space velocity for the object. Its path on the celestial sphere (as seen from the Solar System barycenter, without the displacement due to parallax) is an arc of a great arc circle. The angular velocity (proper motion) along this arc is variable, reaching a maximum when the object is closest to the Sun along its rectilinear path; the distance (parallax) and distance rate (radial velocity, $V _ { \mathrm { r } }$ ) change also with time. In a rigorous treatment, the variation of these six parameters must be considered. This is presented in Section 11.3, together with the corresponding uncertainty propagation.

# 7.7 Consequences of adoption of the ICRS and ICRF

What are the practical consequences of the adoption of the new ICRS and ICRF for the general practice of astronomy? For uses with accuracy requirements worse than 50 mas, the adoption of the ICRS has no significant effect. But for better precisions, there are a number of positive impacts on astronomy:

(i) the ICRS and ICRF are fixed for all epochs; however, the Earth’s equator still moves kinematically for observations from the surface of the Earth. The new procedures, which include a new precession–nutation model, the geodesic precession and nutation, and a new definition of intermediate axes are given in Chapters 8 and 10;   
(ii) there is no epoch attached to the ICRS, therefore, future improvements of the ICRF will not change the ICRS fiducial point or the direction of its axes;   
(iii) changes of stellar positions between two epochs are determined from proper motions referred to the ICRF;   
(iv) the determination of the directions of celestial objects in the ICRS must be consistent with the terrestrial coordinates in the ITRS (Chapter 9) by use of the IERS orientation parameters of universal time, polar motion, and precession–nutation expressions as given in Chapter 10.

# 7.8 Transformations to ecliptic and galactic coordinates

Let us establish the notations for these transformations. A direction is given by a unit vector, a, written as a column matrix (see Section 3.4). Three systems of coordinates will be considered:

(i) ICRS equatorial system $\mathbf { a } _ { 0 }$ : $( x , y , z )$ with the coordinates $\alpha$ and $\delta$ , proper motion components $\mu _ { \alpha }$ and $\mu _ { \delta }$ , and the parallax $\varpi$ ,   
(ii) ecliptic system $\mathbf { a } _ { k } \colon ( x _ { k } , y _ { k } , z _ { k } )$ with the corresponding paramaters $\lambda$ $, \beta \mu _ { \lambda } , \mu _ { \beta } , \varpi$ ,   
(iii) galactic system $\mathbf { a } _ { g } \colon ( x _ { g } , y _ { g } , z _ { g } )$ with the corresponding parameters $l$ and $b$ , $\mu _ { l }$ , $\mu _ { b } , \varpi$ .

Thus, the arbitrary direction u may be written in terms of equatorial, ecliptic, and galactic coordinates as

$$
\begin{array} { r l } & { \mathbf { u } = \left( \begin{array} { c } { x } \\ { y } \\ { z } \end{array} \right) = \left( \begin{array} { c } { \cos \delta \cos \alpha } \\ { \cos \delta \sin \alpha } \\ { \sin \delta } \end{array} \right) = \left( \begin{array} { c } { x _ { k } } \\ { y _ { k } } \\ { z _ { k } } \end{array} \right) = \left( \begin{array} { c } { \cos \beta \cos \lambda } \\ { \cos \beta \sin \lambda } \\ { \sin \beta } \end{array} \right) } \\ & { \quad = \left( \begin{array} { c } { x _ { g } } \\ { y _ { g } } \\ { z _ { g } } \end{array} \right) = \left( \begin{array} { c } { \cos b \cos l } \\ { \cos b \sin l } \\ { \sin b } \end{array} \right) . } \end{array}
$$

The transformation between equatorial and ecliptic systems is given by:

$$
\left( \begin{array} { l } { x _ { k } } \\ { y _ { k } } \\ { z _ { k } } \end{array} \right) = \mathcal A _ { k } \times \left( \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right) ,
$$

where, using $\varepsilon$ as the obliquity of the ecliptic,

$$
\begin{array} { r l } { \mathcal { A } _ { k } = \left( \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { \cos \varepsilon } & { \sin \varepsilon } \\ { 0 } & { - \sin \varepsilon } & { \cos \varepsilon } \end{array} \right) \times \left( \begin{array} { c } { x } \\ { y } \\ { z } \end{array} \right) ~ } & { { } } \\ { = \left( \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { + 0 . 9 1 7 4 8 2 1 3 1 5 } & { 0 . 3 9 7 7 7 6 9 9 5 8 } \\ { 0 } & { - 0 . 3 9 7 7 6 9 9 5 8 } & { 0 . 9 1 7 4 8 2 1 3 1 5 } \end{array} \right) , } \end{array}
$$

where $\varepsilon$ is the obliquity of the fixed ecliptic with its origin identical as the origin of the ICRS. The values in (7.8) correspond to $\varepsilon = 2 3 ^ { \circ } 2 6 ^ { \prime } 2 1 . 4 0 5 9$ , which is a value given by Fukushima (2001).

The transformation between equatorial and galactic systems is given by:

$$
\begin{array} { r } { \left( \begin{array} { c } { x _ { g } } \\ { y _ { g } } \\ { z _ { g } } \end{array} \right) = \mathcal A _ { g } \times \left( \begin{array} { c } { x } \\ { y } \\ { z } \end{array} \right) , } \end{array}
$$

where the matrix $\mathbf { A } _ { g }$ relates the galactic pole and the center of the ICRS system. This transformation is not standardized by an IAU definition. If we use the following values for the galactic pole in the ICRS system: $\alpha _ { g } = 1 9 2 . 8 5 9 4 8$ and $\delta _ { g } = + 2 7 \% 1 2 8 2 5$ , and define the origin of the galactic longitude by the galactic longitude of the ascending node of the galactic plane on the equator of the ICRS, given by $l _ { \Omega } = 3 2 . 9 3 1 9 2$ , then the transformation matrix may be computed to any desired accuracy. To 10 decimal places, it is:

$$
\mathcal { A } _ { g } = \left( \begin{array} { c c c } { - 0 . 0 5 4 8 7 5 5 6 0 4 } & { - 0 . 8 7 3 4 3 7 0 9 0 2 } & { - 0 . 4 8 3 8 3 5 0 1 5 5 } \\ { + 0 . 4 9 4 1 0 9 4 2 7 9 } & { - 0 . 4 4 4 8 2 9 6 3 0 0 } & { + 0 . 7 4 6 9 8 2 2 4 4 5 } \\ { - 0 . 8 6 7 6 6 6 1 4 9 0 } & { - 0 . 1 9 8 0 7 6 3 7 3 4 } & { + 0 . 4 5 5 9 8 3 7 7 6 2 } \end{array} \right) .
$$

The galactic coordinates given above are based on adopting coordinates of directions of the north galactic pole and galactic center based on physical features in the Galaxy with respect to the B1950 coordinate frame (Blaauw et al., 1960). The transformation to ICRS values was given by Murray (1989). The resulting change in the directions of the principal axes, compared to the definition by Murray, is at most 18 mas.

The ecliptic longitude and latitude are computed from:

$$
\binom { \cos \beta \cos \lambda } { \cos \beta \sin \lambda } = \mathcal { A } _ { k } \times \left( \begin{array} { c } { \cos \delta \cos \alpha } \\ { \cos \delta \sin \alpha } \\ { \sin \delta } \end{array} \right) ,
$$

and the galactic longitude and latitude from:

$$
\left( \begin{array} { c } { \cos b \cos l } \\ { \cos b \sin l } \\ { \sin b } \end{array} \right) = \mathcal { A } _ { g } \times \left( \begin{array} { c } { \cos \delta \cos \alpha } \\ { \cos \delta \sin \alpha } \\ { \sin \delta } \end{array} \right) .
$$

Now, let $\mathbf { p }$ and $\mathbf { q }$ be unit vectors in the ICRF perpendicular to $\mathbf { u }$ in the direction of the increasing $\alpha$ and $\delta$ , and similar definitions for $\mathbf { p } _ { k }$ and $\mathbf { q } _ { k }$ in the ecliptic axes, and $\mathbf { p } _ { g }$ and ${ \bf q } _ { g }$ , in the galactic axes. These vectors are parts of the normal p, q, r triads, where $\mathbf { p } = \mathbf { q } \times \mathbf { u }$ and $\mathbf { q } = \mathbf { u } \times \mathbf { p }$ . The variation in $\mathbf { u }$ due to small changes in the spherical coordinates can be written as:

$$
\Delta { \bf u } = \Delta \alpha ^ { * } { \bf p } + \Delta \delta { \bf q } = \Delta \lambda ^ { * } { \bf p } _ { k } + \Delta \beta { \bf q } _ { k } = \Delta l ^ { * } { \bf p } _ { g } + \Delta b { \bf q } _ { g } ,
$$

where

$$
\begin{array} { c } { { \Delta \alpha ^ { * } = \Delta \alpha \cos \delta , } } \\ { { \Delta \lambda ^ { * } = \Delta \lambda \cos \beta , } } \\ { { \Delta l ^ { * } = \Delta l \cos b . } } \end{array}
$$

Using the orthonormality of the tangent vectors, one may solve these equations and get:

$$
\begin{array} { r } { \Delta \lambda = ( \Delta \alpha ^ { * } \mathbf { p } + \Delta \delta \mathbf { q } ) \cdot \mathbf { p } _ { k } , } \\ { \Delta \beta = ( \Delta \alpha ^ { * } \mathbf { p } + \Delta \delta \mathbf { q } ) \cdot \mathbf { q } _ { k } , } \end{array}
$$

and

$$
\begin{array} { r } { \Delta l = ( \Delta \alpha ^ { * } { \bf p } + \Delta \delta { \bf q } ) \cdot { \bf p } _ { g } , } \\ { \Delta b = ( \Delta \alpha ^ { * } { \bf p } + \Delta \delta { \bf q } ) \cdot { \bf q } _ { g } . } \end{array}
$$

The above equations contain the partial derivatives of the ecliptic and galactic coordinates with respect to the equatorial coordinates. They are obtained as scalar products of the relevant tangential vectors expressed in any convenient coordinate system. This can be written in matrix notation as follows:

$$
\binom { \Delta \lambda ^ { * } } { \Delta \beta } = \left( \begin{array} { c c } { \mathbf { p } _ { k } ^ { ^ { \prime } } \cdot \mathbf { p } } & { \mathbf { p } _ { k } ^ { ^ { \prime } } \cdot \mathbf { q } } \\ { \mathbf { q } _ { k } ^ { ^ { \prime } } \cdot \mathbf { p } } & { \mathbf { q } _ { k } ^ { ^ { \prime } } \cdot \mathbf { q } } \end{array} \right) \times \left( \begin{array} { c } { \Delta \alpha ^ { * } } \\ { \Delta \delta } \end{array} \right) ,
$$

and

$$
\begin{array}{c} \binom { \Delta l ^ { * } } { \Delta b } = \binom { \mathbf { p } ^ { \prime } { } _ { g } \cdot \mathbf { p } } { \mathbf { q } ^ { \prime } { } _ { g } \cdot \mathbf { p } } \ \mathbf { p } _ { g } ^ { \prime } \cdot \mathbf { q }  \\ { \mathbf { q } _ { g } ^ { \prime } \cdot \mathbf { p } } & { \mathbf { q } _ { g } ^ { \prime } \cdot \mathbf { q } } \end{array} ) \times ( \begin{array} { c } { \Delta \alpha ^ { * } } \\ { \Delta \delta } \end{array} ) .
$$

Considering the proper motion components as the time derivatives of coordinates, their transformations are given by:

$$
\begin{array}{c} { \binom { \mu _ { \lambda ^ { * } } } { \mu _ { \beta } } } = { \binom { \mathbf { p ^ { \prime } } _ { k } \cdot \mathbf { p } } { \mathbf { q ^ { \prime } } _ { k } \cdot \mathbf { p } } } \ \mathbf { p ^ { \prime } } _ { k } \cdot \mathbf { q }  \end{array}  ) \times { \binom { \mu _ { \alpha ^ { * } } } { \mu _ { \delta } } } ,
$$

and

$$
\binom { \mu _ { l ^ { * } } } { \mu _ { b } } = \binom { \mathbf { p } _ { g } ^ { \prime } \cdot \mathbf { p } \quad \mathbf { p } _ { g } ^ { \prime } \cdot \mathbf { q } } { \mathbf { q } _ { g } ^ { \prime } \cdot \mathbf { p } \quad \mathbf { q } _ { g } ^ { \prime } \cdot \mathbf { q } } \times \binom { \mu _ { \alpha ^ { * } } } { \mu _ { \delta } } .
$$

The complete transformation of the equatorial position and proper motion into the ecliptic system is given by Equations (7.10), (7.13) and (7.15), the parallax is independent of the coordinate system. Taking the five astrometric parameters in the order $\alpha , \delta , \varpi$ , $\mu _ { \alpha }$ , and $\mu _ { \delta }$ , the Jacobian matrix for the transformation is:

$$
\mathcal { I } = \left( \begin{array} { c c c c c } { c } & { s } & { 0 } & { 0 } & { 0 } \\ { - s } & { c } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { c } & { s } \\ { 0 } & { 0 } & { 0 } & { - s } & { c } \end{array} \right) ,
$$

where $c = \mathbf { p } _ { k } ^ { \prime } \cdot \mathbf { p } = \mathbf { q } _ { k } ^ { \prime } \cdot \mathbf { q }$ , and $s = \mathbf { p } _ { k } ^ { \prime } \cdot \mathbf { q } = - \mathbf { q } _ { \ k } ^ { \prime } \cdot \mathbf { p }$ , so that the full equation is

given by

$$
\left( \begin{array} { c } { { \Delta \lambda ^ { * } } } \\ { { \Delta \beta ^ { * } } } \\ { { \varpi } } \\ { { \mu _ { \lambda ^ { * } } } } \\ { { \mu _ { \beta } } } \end{array} \right) = \left( \begin{array} { c c c c c } { { c } } & { { s } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { - s } } & { { c } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { c } } & { { s } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { - s } } & { { c } } \end{array} \right) \times \left( \begin{array} { c } { { \Delta \alpha ^ { * } } } \\ { { \Delta \delta ^ { * } } } \\ { { \varpi } } \\ { { \mu _ { \alpha ^ { * } } } } \\ { { \mu _ { \delta } } } \end{array} \right) .
$$

The transformation of the equatorial parameters into the galactic system is given by Equations (7.11), (7.14) and (7.16); the Jacobian matrix is given by (7.17), with $c = \mathbf { p } _ { g } ^ { \prime } \cdot \mathbf { p } = \mathbf { q } _ { g } ^ { \prime } \cdot \mathbf { q }$ , and $s = \mathbf { p } _ { g } ^ { \prime } \cdot \mathbf { q } = - \mathbf { q } _ { g } ^ { \prime } \cdot \mathbf { p }$ .

# 8 Dynamical reference frame

Until 1998 the reference frame was defined in terms of the Solar System and the dynamics induced by the motions of Solar System bodies and their shapes. The two reference planes were the equator of the Earth and the ecliptic, the mean plane of the Earth’s orbit. The intersection of these two planes, the equinox, was the fiducial point. Since both the equator and the ecliptic move owing to solar and lunar gravitational forces on the shape of the Earth and perturbations by the planets on the Earth’s motion, the equinox moves with time. Therefore, each dynamical reference frame had to be defined for a specific epoch and observations and predictions were transformed to and from standard epochs to the chosen times of observations.

We have presented, in Chapter 7, the new adopted International Celestial Reference System (ICRS) based on the extragalactic radio sources. Now, the fundamental reference frame is fixed for all times. The IAU introduced in 2000 two space fixed systems. The Barycentric Celestial Reference System (BCRS) and the Geocentric Celestial Reference System (GCRS) have been defined in terms of metric tensors and the generalized Lorentz transformation between them, which contains the acceleration of the geocenter and the gravitational potential. The ICRS is to be understood as defining the orientation of the axes of both these systems for each of the origins. The International Celestial Reference Frame, (ICRF), determined from VLBI observations is the realization of the ICRS and can similarly be geocentric and barycentric.

The fiducial point of the ICRS does not have to revolve as the equinox did. It was adopted to be aligned with the equinox of the FK5 and the dynamical equinox at J2000.0 within their errors. For the reference frame of date on the moving equator, there is the option for a fiducial point (Section 8.4). One option is to retain the equinox, which is moving along the equator. The other option, which has been recommended by the IAU, is the use of the Celestial Ephemeris Origin (CEO), which does not have any motion along the instantaneous equator.

However, the motions of the Solar System and its bodies have not changed. Thus, as they are applicable, these motions must be taken into account. Specifically, the kinematics of the Earth must be included for Earth based observations. Similarly, the dynamics and kinematics of other observational platforms must be included as appropriate. Information concerning the celestial mechanics explaining the Solar System dynamics can be found in Brouwer and Clemence (1961), Brumberg (1991a,b), Hagihara (1970–76), Kovalevsky (1967) and Murray and Dermott (1999).

# 8.1 Our Solar System

Our Solar System, as it is currently known, consists of the Sun; four terrestrial planets, Mercury, Venus, Earth, and Mars; four large gaseous planets, Jupiter, Saturn, Uranus, and Neptune; a distant small planet, Pluto; planetary satellites, one around the Earth, two around Mars, one around Pluto, and many around the gaseous planets; many minor planets, primarily in orbits between the terrestrial and gaseous planets, but with some crossing the orbits of the terrestrial planets and others among the gaseous planets; some minor planets have satellites in orbit around them; Kuiper belt objects beyond the orbit of Neptune; and comets, short-period comets that have been observed at more than one apparition, long-period comets that have not been observed before, and Oort cloud comets, which are beyond the Kuiper belt. There is also a large amount of material consisting of smaller particles in the Solar System, some in rings about the gaseous planets, and some which enters the Earth’s atmosphere daily, some observed as meteors, and much that is unobserved.

Each of the objects has gravitational effects on the motions of the other objects, proportional to their masses and inversely proportional to the squares of the distances between them. Some of these effects are negligible, depending upon the accuracy of the computations. Additionally, none of the objects is a homogeneous sphere, so the shapes of the bodies affect the motions of nearby objects and the kinematics of the bodies are affected by the gravitational forces due to other bodies on the irregular shapes. Some quantitative information concerning the orbits and the physical characteristics of the planets is given in the Appendix B.

# 8.2 Ephemerides

The motions of the Solar System objects can be represented as two-body motion with six Keplerian orbital elements, either by osculating or mean elements. More accurate ephemerides may be achieved by means of algebraic expressions that represent the perturbations due to the many additional bodies. These algebraic expressions are usually in terms of Fourier or Chebyshev series. The most accurate ephemerides are currently achieved by means of numerical integration of the equations of motion, which include all bodies that can have a significant effect on the motions. For the planets, the motions of all the planets are integrated simultaneously. The gravitational forces are computed considering the bodies to be point masses. Included in the equations of motion are the relativistic terms.

For each body $i$ , the point mass acceleration is written in the framework of general relativity in the book by Brumberg (1991a). However, it is generally not necessary to use the full relativistic procedures. It is simpler to use the limited PPN formulation as presented in section 5.3.6. The acceleration, including gravitational perturbations by minor planets, is given by Will (1974) as follows:

$$
\begin{array} { l } { { \displaystyle \frac { \mathrm { d } ^ { 2 } \mathbf { r } _ { i } } { \mathrm { d } t ^ { 2 } } = \sum _ { j \not = i } ^ { \infty } \frac { \mu _ { j } ( \mathbf { r } _ { j } - \mathbf { r } _ { i } ) } { r _ { i j } ^ { 3 } } \Biggl \{ 1 - 2 ( \beta + \gamma ) / c ^ { 2 } \sum _ { k \not = i } ^ { \infty } \frac { \mu _ { k } } { r _ { k i } } - ( 2 \beta - 1 ) / c ^ { 2 } \sum _ { k \not = j } ^ { \infty } \frac { \mu _ { k } } { r _ { j k } } } } \\ { ~ + \gamma ( v _ { i } / c ) ^ { 2 } + ( 1 + \gamma ) ( v _ { j } / c ) ^ { 2 } - 2 ( 1 + \gamma ) ( v _ { j } / c ) ^ { 2 } - 2 ( 1 + \gamma ) / c ^ { 2 } \frac { 2 \mathbf { r } _ { i } } { \mathrm { d } t } \cdot \frac { \mathrm { d } \mathbf { r } _ { j } } { \mathrm { d } t } }  \\ { { \displaystyle ~ - ( 3 / 2 c ^ { 2 } ) ( \mathbf { r } _ { i } - \mathbf { r } _ { j } ) ^ { 2 } ( \mathbf { r } _ { j } / \mathrm { d } t ) ^ { 2 } + 1 / 2 c ^ { 2 } ( \mathbf { r } _ { j } - \mathbf { r } _ { i } ) \frac { \mathrm { d } \mathbf { r } _ { j } } { \mathrm { d } t ^ { 2 } } \Biggr \} } } \\ { { \displaystyle ~ + c ^ { - 2 } \sum _ { j \not = i } ^ { \infty } \frac { \mu _ { j } } { r _ { i j } ^ { 3 } } \left\{ ( \mathbf { r } _ { i } - \mathbf { r } _ { j } ) \left[ ( 2 + 2 \gamma ) \frac { \mathrm { d } \mathbf { r } _ { i } } { \mathrm { d } t } - ( 1 + 2 \gamma ) \frac { \mathrm { d } \mathbf { r } _ { j } } { \mathrm { d } t } \right] \right\} \left( \frac { \mathrm { d } \mathbf { r } _ { i } } { \mathrm { d } t } - \frac { \mathrm { d } \mathbf { r } _ { j } } { \mathrm { d } t } \right) } } \\   \displaystyle ~ + ( 3 + 4 \gamma ) / 2 c ^ { 2 } \sum _ { j \not = i } ^ { \infty } \frac { \mu _ { j } } { r _ { i j } ^ { 3 } } \frac { \mathrm { d } ^ { 2 } \mathbf { r } _ { j } } { \mathrm { d } t ^ { 2 } } + \sum _ { m } \frac  \mu _  m  \end{array}
$$

Here, $\mathbf { r } _ { i }$ , $\mathrm { d } \mathbf { r } _ { i } / \mathrm { d } t$ and $\mathrm { d } ^ { 2 } \mathbf { r } _ { i } / \mathrm { d } t ^ { 2 }$ are the Solar System barycentric position, velocity, and acceleration vectors of body $i , \mu _ { j } = G m _ { j }$ , where $G$ is the gravitational constant and $m _ { j }$ is the mass of body $j ; \beta$ is the PPN parameter measuring the nonlinearity in superposition of gravity; $\gamma$ is the PPN parameter measuring space curvature produced by a unit rest mass (in general relativity, $\beta = \gamma = 1 ) ; v _ { j } = | \mathrm { d } \mathbf { r } _ { j } / \mathrm { d } t |$ ; $c$ is the velocity of light; and index $m$ jis for minor planets included in the integration.

In order to achieve full accuracy in the ephemerides, the effects of the body figures (i.e. the lack of symmetry to be represented by point masses), the tidal effects between the Earth and the Moon, and lunar libration effects must be included.

The numerically computed ephemerides must be fit to observational data for all the bodies on a single consistent reference system. The computation and fitting is an iterative process providing improved values of initial conditions, orbital elements, and masses, as appropriate. As a result, each ephemeris defines its own motion of the Earth and dynamical reference frame. The current ephemeris is Jet Propulsion Laboratory’s DE 405, which is described by Standish (1998) and is available from http://ssd.jpl.nasa.gov/eph info.html.

This will be replaced by a new ephemeris as necessary to maintain the accuracy required for the Solar System ephemerides for the navigation of space-probes.

# 8.3 Reference planes

There are several natural reference planes, which can be used to define a reference frame. There are reference planes that must be used for observational purposes, there are reference frames that are theoretically desirable, but not observational, and unfortunately most of the planes are in motion, and their accuracies are restricted by observational uncertainties.

The Earth, being our habitat and base for observations, becomes a natural basis for most reference frames. The equatorial plane is the most obvious and necessary reference plane, since the motions of all observatories are with respect to that plane. It can be determined from observational data either by determining the celestial pole or from diurnal motions of celestial sources. Unfortunately, the equatorial plane moves owing to gravitational forces by the Sun, Moon and planets on the bulge of the Earth, and owing to the dynamics of the many components of the interior, surface and exterior of the Earth. These motions are called precession, nutation and polar motion.

Another natural plane of reference is the orbital plane of the Earth. This is subject to perturbations caused by the planets and is changing continuously. The mean orbital plane of the Earth is called the ecliptic. As long as a general theory of Newcomb was used to determine the ephemeris of the Earth, the ecliptic was well defined by the mean elements. With a numerical integration for the ephemeris of the Earth, the time period used to define the mean orbit is arbitrary.

The equinox is defined as the intersection of the ecliptic and the mean equator of the Earth. In determining this intersection from numerically integrated ephemerides, a distinction must be made. The equator can be taken as the instantaneous plane or as a uniformly moving plane. The historical determination was made based on the uniformly moving plane, and that is the definition that has continued to be used. The difference is approximately a tenth of an arcsecond. For calendars, seasons, and holiday definitions the equinox is specified as the time when the Sun passes through either of the intersection points, i.e. when the apparent latitude of the Sun is $0 ^ { \circ }$ .

Another reference plane defined by the Solar System is the invariable, or Laplacian, plane. This is the plane normal to the axis of angular momentum and passing through the barycenter of the Solar System. This plane can be theoretically defined and specified, but it is not observable. It is somewhat dependent upon the completeness of the knowledge of the bodies of the system and their masses.

# 8.4 New definitions of a reference frame and fiducial point

To transform from the fixed International Celestial Reference Frame (ICRF) to that of date, the position of the moving equator and the location of an origin on that equator must be defined. The IAU has recommended a new system such that the origin of right ascensions on the true, or intermediate, celestial equator is no longer the equinox, but a point called the Celestial Ephemeris Origin (CEO), which does not depend on the position of the ecliptic. The true equatorial plane is determined from the precession–nutation model and its pole is called the Celestial Intermediate Pole (CIP). The resulting reference system is called the Celestial Intermediate Frame (Seidelmann and Kovalevsky, 2002). Note that these names are not consistent. It would have been more appropriate to call the origin on the equator Celestial Intermediate Origin (CIO), so that the word intermediate would be present in the names of all quantities defining this system. However, in this book, we shall stick to the official designation – CEO.

New precession–nutation models were adopted, designated by IAU 2000A and IAU 2000B, depending on the precision at the milliarcsecond levels. Based on the latest observational data, the IERS provides the most precise precession–nutation values, which are put in the same form as values derived from theoretical formulae. Precession and nutation models are applied together, thus eliminating the distinction between the mean and true equators. Owing to increased accuracies and frequency of observations of the Earth orientation, sub-daily polar motion and nutation periods can be determined. Thus, the separation of nutation and polar motion terms becomes arbitrary, and the choice was made to designate all terms with periods less than two days as polar motion.

In addition, the pole of the ICRF does not coincide with the mean pole of J2000.0, and there is a difference between the origin of the $x$ -axis in the ITRS and the equinox of J2000.0. These shifts have been included in the precession–nutation models. The numerical developments of the precession–nutation models, including the pole offsets, are changing with the availability of additional observations.

The Celestial Ephemeris Origin (CEO) is defined such that its motion on a fixed celestial sphere has no component along the equator. The position of the CEO on the equator is defined by an integral that involves only the path followed by the precession–nutation pole (CIP) since the reference epoch (Capitaine et al., 1986). For the details concerning the CIP and the CEO, see Sections 8.7 and 10.3.

The ICRS provides a fixed, epoch independent frame. For the moving reference frame of date, at least for an extended transitional period, there will be choices available. These may be described as the classical system, the improved classical system, and the new, or intermediate, system.

(i) The classical system is the system (since 1984) that uses the Celestial Ephemeris Pole (CEP) to define the equatorial plane, the Lieske et al. (1977) precession for the mean equator and equinox, the IAU 1980 Theory of Nutation (Seidelmann, 1982; Wahr, 1981) for the true positions, and the Aoki et al. (1982) expression to relate Greenwich Mean Sidereal Time (GMST) to UT1.

(ii) The improved classical system uses the CIP as determined by the IAU 2000 precession and nutation model to define the equatorial plane, the improved precession values to determine the mean equinox, the new nutation model for the true positions, and an improved expression to relate GMST to UT1.   
(iii) For the new, or intermediate, system, the true equatorial plane and its pole (CIP) are determined from the IAU2000 precession–nutation model as above, the CEO is determined by a formula based uniquely on observations of the CIP, and the rotation of the Earth is determined from the CEO as the stellar angle, or Earth rotation angle, which is linear with time. The stellar angle does not depend on precession or nutation. The equinox is no longer used.

The differences between the systems are that the equinox moves along the equator at about 50 arcseconds per year, while the CEO moves only about 20 milliarcseconds per century. The improved classical system with precession and nutation separated and the new system with the precession–nutation model should lead to the same results within the applied accuracy. The classical system will have a precession error of about 0.3 per century, nutation errors of a little more than 1 mas, and uncorrected offsets of the pole. In the classical systems precession terms appear in the formula between GMST and UT1, while nutation terms appear in the formula for Greenwich Apparent Sidereal Time, as the equation of the equinoxes. So there is crosstalk and resulting errors in those expressions. See Section 10.3 for the details.

In the following sections, precession and nutation will be described as necessary for both the classical, old and improved values, and the new systems. Chapter 10 gives Earth orientation details, including the stellar angle, CIP and CEO.

# 8.5 Generalities on precession and nutation

The motion of the equatorial plane is caused by the torque of the Sun, Moon and planets on the dynamical figure of the Earth. It has been traditionally divided into two parts. The first is the smooth long-period motion of the mean pole of the equator about the pole of the ecliptic with a period of about $2 5 ~ 8 0 0$ years, discovered by Hipparchus in the second century bc. This is a motion of the rotation axis of the Earth. This is the luni-solar precession. The other part, which comprises a large number of periodic oscillations of the rotation axis with small amplitudes, is the nutation. The most important nutation term, associated with the regression of the lunar orbit’s line of nodes, has an amplitude of about $9 . 0$ and a period of 18.6 years. It was discovered by Bradley in 1748. The methods of observation of precession and nutation are described in Section 10.2.

The motion of the ecliptic is the result of the gravitational effects of the planets on the Earth’s orbit and this makes a contribution to precession known as planetary precession. If the equator were fixed, this motion would cause a precession of the equinox of about $1 2 ^ { \prime \prime }$ per century and a decrease in the obliquity of the ecliptic of about $4 7 ^ { \prime \prime }$ per century. The combination of luni-solar and planetary precession is called general precession. The causes of precession and nutation are the same, only the periods are different. The new (IAU 2000) precession–nutation model removes the distinction. The new precession–nutation model has been adopted by the IAU and IAU 2000A is accurate to $0 . 2 \mathrm { \ m a s }$ , while IAU 2000B is accurate to 1 mas. This model replaces the old precession model based on a constant of precession and the IAU 1980 Theory of Nutation. The precession–nutation model is subject to corrections based on observational data. The real, non-rigid Earth dynamics are not currently fully understood. Thus, for the best accuracies it is recommended that numerical values determined and distributed by the IERS be used for precession– nutation.

The new precession–nutation model is documented in three papers: the new nutation series for non-rigid Earth and insights into the Earth’s interior is in Mathews et al. (2002); the Very Long Baseline Interferometry results are in Herring et al. (2002); and the effects of electro-magnetic coupling are in Buffett et al. (2002).

Until the year 2003, the officially adopted constant of general precession in longitude per Julian century at epoch J2000.0 was $p = 5 0 2 9 _ { \cdot } ^ { \prime \prime } 0 9 0 6$ . It was known to be incorrect by about $- 0 . 3 0$ per century. The IAU 1980 Theory of Nutation also needed improvement. For improved accuracy with the classical system and the equinox, the precession constant should be corrected to the value $p = 5 0 2 8 _ { \cdot } ^ { \prime \prime } 7 9 7$ per Julian century, and a nutation model without the precession terms should be used.

There are some additional changes of which astronomers should be aware. The pole of the ICRS does not coincide with the mean pole of J2000.0 and there is a difference between the origin of the $x$ -axis in the ICRS and the equinox of J2000.0. These shifts have been included in the precession–nutation models. The geodesic precession and nutation have been included in the precession–nutation model, although that is a very different effect that arises from the transformation between the geocentric and the barycentric coordinates, each with fixed directions (see Section 7.5). Free core nutation is not included in the precession–nutation model. Since new observational capabilities provide the possibility of determining motions of the pole with periods less than a day, the arbitrary choice has been made to include all such motions with periods less than two days in polar motion values.

# 8.6 Precession

The motion of the ecliptic is described using Fig. 8.1 with angles $\pi _ { A }$ and $\Pi _ { A }$ , where $\pi _ { A }$ is the angle between the mean ecliptic at a fixed epoch $t _ { 0 }$ and the mean ecliptic of date $t$ , and $\Pi _ { A }$ is the angular distance from the equinox $\gamma _ { 0 }$ at the fixed epoch to the ascending node where the ecliptic of date meets the fixed ecliptic of epoch. The expressions for $\pi _ { A }$ and $\Pi _ { A }$ are of the form

![](images/367e5cde4deaabc012481f9d6dd92663557bfbe4c45f9a2e8fb06bdab628c6e6.jpg)  
Fig. 8.1. The ecliptic and equator at epoch and date.

$$
\begin{array} { c } { { \sin \pi _ { A } \sin \Pi _ { A } = s t + s _ { 1 } t ^ { 2 } + s _ { 2 } t ^ { 3 } } } \\ { { \sin \pi _ { A } \cos \Pi _ { A } = c t + c _ { 1 } t ^ { 2 } + c _ { 2 } t ^ { 3 } , } } \end{array}
$$

where for continuity $\pi _ { A } > 0$ to $t > 0$ and $\pi _ { A } < 0$ to $t < 0$ . The precessional effect due to the motion of the ecliptic is the arc $P \gamma$ in Fig. 8.1 and is the accumulated planetary precession $\chi _ { A }$ . Its rate of change at epoch $t _ { 0 }$ is

$$
\chi = s \csc \epsilon _ { 0 } ,
$$

where $\epsilon _ { 0 }$ is the obliquity of the ecliptic at the epoch $t _ { 0 }$

The precessional constant, $P _ { 0 }$ , occurs in the dynamical equations of motion for the equator because of the torques produced by the Sun and Moon. The value of the constant is determined from observations, since it can not be accurately calculated from a theoretical dependency on geophysical and gravitational parameters. Lunisolar precession at epoch $t _ { 0 }$

$$
\psi = P _ { 0 } \cos \epsilon _ { 0 } - P _ { \mathrm { g } }
$$

is the rate of change in longitude $\psi _ { A }$ along the ecliptic due to the motion of the equator at epoch $t _ { 0 }$ , where $P _ { \mathrm { g } }$ is the geodesic precession, which is a relativistic effect amounting to $1 ^ { \prime \prime } 9 2$ per Julian century described in Section 7.5. The combined effect of planetary precession and luni-solar precession is called general precession in longitude. The accumulated general precession $p _ { A }$ in Fig. 8.1 is

$$
p _ { A } = \gamma R - \gamma _ { 0 } R .
$$

The rate of precession at epoch $t _ { 0 }$ is

$$
p _ { A } = \psi - \chi \cos \epsilon _ { 0 } = P _ { 0 } \cos \epsilon _ { 0 } - P _ { \mathrm { g } } - s \cos \epsilon _ { 0 } ,
$$

![](images/82c196f09ccd72875e13b32d24ae80b5cb22d55c25095236c71a5ed792977705.jpg)  
Fig. 8.2. The precession angles $\zeta _ { A }$ , $z _ { A }$ , and $\theta _ { A }$ . The ecliptic of fixed epoch $E _ { \mathrm { f } }$ meets the mean equator of the same epoch in $\gamma _ { 0 }$ . Similarly, $\gamma$ is the intersection of the mean equator and the ecliptic of epoch $E _ { \mathrm { p } }$ .

and $p$ may be resolved into general precession in right ascension, $m$ , and in declination $n$ , where

$$
\begin{array} { r } { m = \psi \cos \epsilon _ { 0 } - \chi = ( P _ { 0 } \cos \epsilon _ { 0 } - P _ { \mathrm { g } } ) \cos \epsilon _ { 0 } - s \cos \epsilon \epsilon _ { 0 } } \\ { n = \psi \sin \epsilon _ { 0 } = ( P _ { 0 } \cos \epsilon _ { 0 } - P _ { \mathrm { g } } ) \sin \epsilon _ { 0 } . } \end{array}
$$

$$
p = m \cos \epsilon _ { 0 } + n \sin \epsilon _ { 0 } .
$$

Precession may be formulated in several ways. The vector directions of the polar axis of the Earth and polar axis of the ecliptic may be expressed in terms of polynomials involving time arguments (Murray, 1983), which are then used to calculate the effects of precession. The following method developed from Newcomb, and adopted by the IAU (Lieske et al., 1977), is useful for practical applications.

The accumulated precession angles $\zeta _ { A } , z _ { A }$ and $\theta _ { A }$ , which are used to calculate the effect of precession on equatorial coordinates, are referred to a base epoch $E _ { 0 }$ and have time arguments that describe precession from an arbitrary fixed epoch $E _ { \mathrm { f } }$ to an epoch of date $E _ { \mathrm { p } }$ . The angles are shown on the surface of a sphere in Fig. 8.2. In the figure the pole of the equator at $E _ { \mathrm { f } }$ is point $P _ { 0 }$ . At the epoch $E _ { \mathrm { p } }$ , $P _ { 0 }$ has moved to $P$ . Imagine a right-handed set of three-dimensional, Cartesian coordinate axes with origin at the center of the sphere, $X$ -axis pointing to $\gamma _ { 0 }$ , where the equator and ecliptic meet (the equinox) at the fixed epoch $E _ { \mathrm { f } }$ . The $Y$ -axis is $9 0 ^ { \circ }$ away in an easterly direction along the equator, and the $Z$ -axis points toward the pole $P _ { 0 }$ . Initially, precession will move $P _ { 0 }$ toward $\gamma _ { 0 }$ , but the movement of the ecliptic will cause $P _ { 0 }$ to move in a slightly different direction.

A rotation of $- \zeta _ { A }$ about the $Z$ -axis makes $P _ { 0 } \gamma _ { 0 }$ pass through $P$ . This great circle meets the mean equator of epoch at right angles at point $\boldsymbol { Q }$ and the mean equator of date at right angles at $R$ . The $x$ -axis is now in the direction $\boldsymbol { Q }$ ; the $y$ -axis points toward the node $S$ , where the two equators cross.

A rotation of $+ \theta _ { A }$ equal to the angular separation of $P$ from $P _ { 0 }$ about the new $y$ -axis brings the mean equator of epoch to the mean equator of date. The $z$ -axis points to the pole of date $P$ , the $y$ -axis to the node $S$ , and the $x$ -axis now points toward $R$ in the plane of the equator of date.

Finally, a rotation of $- z _ { A }$ equal to the angle $\gamma P R$ about the $z$ -axis brings $R$ to $\gamma$ , so that the $x$ -axis points toward $\gamma$ , the equinox of date, and still lies in the plane of the mean equator of date.

The precession matrix $\mathcal { P }$ , made up of these rotations, precesses equatorial rectangular coordinates from an arbitrary fixed equinox and equator of epoch $E _ { \mathrm { f } }$ to one of date $E _ { \mathrm { p } }$ and is given by

$$
\mathcal { P } ( E _ { \mathrm { f } } , E _ { \mathrm { p } } ) = \mathcal { R } _ { 3 } ( - z _ { A } ) \mathcal { R } _ { 2 } ( - \theta _ { A } ) \mathcal { R } _ { 3 } ( - \zeta _ { A } ) .
$$

Rewriting Equation (8.8) in terms of spherical coordinates gives

$$
\mathcal { P } = \left( \begin{array} { c c c c } { \cos z _ { A } \cos \theta _ { A } \cos \zeta _ { A } } & { - \cos z _ { A } \cos \theta _ { A } \sin \zeta _ { A } } & { - \cos z _ { A } \sin \theta _ { A } } \\ { - \sin z _ { A } \sin \zeta _ { A } } & { - \sin z _ { A } \cos \zeta _ { A } } & { } \\ { \sin z _ { A } \cos \theta _ { A } \cos \zeta _ { A } } & { - \sin z _ { A } \cos \theta _ { A } \sin \zeta _ { A } } & { - \sin z _ { A } \sin \theta _ { A } } \\ { \cos z _ { A } \sin \zeta _ { A } } & { \cos z _ { A } \cos \zeta _ { A } } & { } \\ { \sin \theta _ { A } \cos \zeta _ { A } } & { \sin \theta _ { A } \sin \zeta _ { A } } & { \cos \theta _ { A } } \end{array} \right) .
$$

Having calculated the precession angles for the matrix $P$ , one can calculate the inverse matrix $\mathcal { P } ^ { - 1 }$ in various ways; for example,

$$
\begin{array} { r l } & { \mathcal { P } ^ { - 1 } = \mathcal { R } _ { 3 } ^ { - 1 } ( - \zeta _ { A } ) \times \mathcal { R } _ { 2 } ^ { - 1 } ( + \theta _ { A } ) \times \mathcal { R } _ { 3 } ^ { - 1 } ( - z _ { A } ) , } \\ & { \mathcal { P } ^ { - 1 } = \mathcal { R } _ { 3 } ^ { \top } ( - \zeta _ { A } ) \times \mathcal { R } _ { 2 } ^ { \top } ( + \theta _ { A } ) \times \mathcal { R } _ { 3 } ^ { \top } ( - z _ { A } ) , } \\ & { \mathcal { P } ^ { - 1 } = \mathcal { R } _ { 3 } ( \zeta _ { A } ) \times \mathcal { R } _ { 2 } ( - \theta _ { A } ) \times \mathcal { R } _ { 3 } ( z _ { A } ) , } \\ & { \mathcal { P } ^ { - 1 } = \mathcal { P } ( E _ { \mathrm { p } } , E _ { \mathrm { f } } ) , } \end{array}
$$

where use has been made of the property that the inverse of a rotation matrix is its transpose (i.e. it is orthogonal).

# 8.6.1 Precession angles and rates adopted by IAU (1976)

The basis for precession is taken directly from the discussion of Lieske et al. (1977) and modified by the small amount discussed in Lieske (1979). The following values are adopted constants at epoch J2000.0:

(i) general precession in longitude: $p = 5 0 2 9 _ { \cdot } ^ { \prime \prime } 0 9 6 6$ per Julian century, (ii) geodesic precession: $P _ { \mathrm { g } } = 1   { : } 9 2$ per Julian century, (iii) obliquity of the equinox: $\epsilon _ { 0 } = 2 3 ^ { \circ } 2 6 ^ { \prime } 2 1 ! { } ^ { \prime \prime } 4 4 8$ .

In addition numerical expressions are provided for a number of quantities used in computing precession in various cases. Let us give the more important:

$$
\begin{array} { c } { { \sin \pi _ { A } \sin \Pi _ { A } = ( 4 ^ { \prime \prime } 1 9 7 6 - 0 ^ { \prime } 7 5 2 5 0 T + 0 ^ { \prime \prime } 0 0 0 4 3 1 T ^ { 2 } ) t } } \\ { { + ( 0 ^ { \prime } 1 9 4 4 7 + 0 ^ { \prime } 0 0 0 6 9 7 T ) t ^ { 2 } - 0 ^ { \prime } 0 0 0 1 7 9 t ^ { 3 } } } \end{array}
$$

$$
1 \pi _ { A } \cos { \pi _ { A } } = ( - 4 6 ^ { \prime \prime } 8 1 5 0 - 0 \% 1 7 T + 0 \% 0 5 4 3 9 T ^ { 2 } ) t
$$

$$
+ ( - 4 6 \mathrm { { ^ { \prime } } 8 1 } 5 0 - 0 \mathrm { { ^ { \prime } } 0 0 1 } 1 7 T + 0 \mathrm { { ^ { \prime } } 0 0 5 } 4 3 9 T ^ { 2 } ) t
$$

$$
+ ( - 0 \sp { \prime } . 0 0 0 5 9 + 0 \sp { \prime \prime } . 0 0 5 4 3 9 T ) t \sp { 2 } + 0 \sp { \prime \prime } . 0 0 1 8 1 3 t \sp { 3 } .
$$

These equations give expressions for the accumulated precession angles as functions of time, where the base epoch of the equations is $E _ { 0 } = J 2 0 0 0 . 0$ or Julian day $J D ( E _ { 0 } ) = 2 4 5 1 5 4 5 . 0$ , and the time arguments are in units of Julian centuries, i.e.

$$
\begin{array} { c } { T = ( J D ( E _ { \mathrm { f } } ) - J D ( E _ { 0 } ) ) / 3 6 5 2 5 } \\ { t = ( J D ( E _ { \mathrm { D } } ) - J D ( E _ { \mathrm { f } } ) ) / 3 6 5 2 5 , } \end{array}
$$

where $E _ { \mathrm { f } }$ is a fixed epoch and $E _ { \mathrm { D } }$ is the epoch of date expressed in days. The

expressions at epoch $E _ { \mathrm { f } }$ for the rates per Julian century of general precession, in longitude $( p )$ , right ascension $( m )$ and declination $( n )$ , and the rate of rotation of the ecliptic, are

$$
\begin{array} { l } { \displaystyle { p = \frac { \mathrm { d } } { \mathrm { d } t } ( p _ { A } ) _ { \vert t = 0 } = 5 0 2 9 ^ { \prime } 0 9 6 6 + 2 ^ { \prime \prime } 2 2 2 2 6 T - 0 \sp { \prime } 0 0 0 0 0 4 2 T ^ { 2 } , } } \\ { \displaystyle { m = \frac { \mathrm { d } } { \mathrm { d } t } ( \zeta _ { A } + z _ { A } ) \vert _ { t = 0 } = 4 6 1 2 ^ { \prime \prime } 4 3 6 2 + 2 \sp { \prime \prime } 7 9 3 1 2 T - 0 \sp { \prime \prime } 0 0 0 2 7 8 T ^ { 2 } , } } \\ { \displaystyle { n = \frac { \mathrm { d } } { \mathrm { d } t } ( \theta _ { A } ) \vert _ { t = 0 } = 2 0 0 4 \sp { \prime \prime } 3 1 0 9 - 0 \sp { \prime \prime } 8 5 3 3 0 T - 0 \sp { \prime \prime } 0 0 0 2 1 7 T ^ { 2 } , } } \\ { \displaystyle { \pi = \frac { \mathrm { d } } { \mathrm { d } t } ( \pi _ { A } ) \vert _ { t = 0 } = 4 7 \sp { \prime } 0 0 2 9 - 0 \sp { \prime \prime } 0 6 6 0 3 T + 0 \sp { \prime } 0 0 0 5 9 8 T ^ { 2 } . } } \end{array}
$$

# 8.6.2 Improved values of precession angles and rates

Improved values of precession constants based on recent observational data and the methods of Lieske are derived by Hilton (2002) from the best estimate of the obliquity of the ecliptic (Fukushima, 2001), the IAU 2000A value of the precession and value of the change in the obliquity of the ecliptic with respect to the mean ecliptic of date, and the value of the motion of the mean ecliptic (Simon et al., 1994). The values are given for J2000.0.

and

$$
\zeta _ { A } = ( 2 3 0 6 \mathrm { ^ { \prime } / } 0 8 0 6 + \mathrm { 1 ^ { \prime \prime } / } 3 9 7 9 3 T - 0 \mathrm { ^ { \prime } / } 0 0 0 1 3 7 T ^ { 2 } ) t
$$

# 8.6.3 Rigorous reduction for precession

The most convenient method of rigorously precessing mean equatorial rectangular coordinates is to use the precession matrix $\mathcal { P }$ as follows:

$$
\mathbf { r } = \mathcal { P } \mathbf { r } _ { 0 }
$$

and

$$
\mathbf { r } _ { 0 } = \mathcal { P } ^ { - 1 } \mathbf { r } ,
$$

which transforms the position vector $\mathbf { r } _ { 0 }$ referred to the fixed epoch $E _ { \mathrm { f } } = t _ { 0 }$ to the position vector $\mathbf { r }$ referred to the epoch of date $E _ { \mathrm { D } } = t$ , and vice versa. The matrix $\mathcal { P }$ is evaluated using the precession angles $\zeta _ { A } , z _ { A }$ , and $\theta _ { A }$ ) in Equation (8.8) or (8.9) and the appropriate time arguments.

Equations (8.14) can be rewritten in terms of right ascension and declination $( \alpha , \delta )$ a s

$$
\begin{array} { c } { { \sin ( \alpha - z _ { A } ) \cos \delta = \sin ( \alpha _ { 0 } + \zeta _ { A } ) \cos \delta _ { 0 } , } } \\ { { \cos ( \alpha - z _ { A } ) \cos \delta = \cos ( \alpha _ { 0 } + \zeta _ { A } ) \cos \theta _ { A } \cos \delta _ { 0 } - \sin \theta _ { A } \sin \delta _ { 0 } } } \\ { { \sin \delta = \cos ( \alpha _ { 0 } + \zeta _ { A } ) \sin \theta _ { A } \cos \delta _ { 0 } + \cos \theta _ { A } \sin \delta _ { 0 } , } } \end{array}
$$

and the inverse is

$$
\begin{array} { r l } & { \sin ( \alpha _ { 0 } + \zeta _ { A } ) \cos \delta _ { 0 } = \sin ( \alpha - z _ { A } ) \cos \delta , } \\ & { \cos ( \alpha _ { 0 } + \zeta _ { A } ) \cos \delta _ { 0 } = \cos ( \alpha - z _ { A } ) \cos \theta _ { A } \cos \delta + \sin \theta _ { A } \sin \delta } \\ & { \qquad \sin \delta _ { 0 } = - \cos ( \alpha - z _ { A } ) \sin \theta _ { A } \cos \delta + \cos \theta _ { A } \sin \delta . } \end{array}
$$

# 8.7 Nutation

We present two theories of nutation. The IAU 1980 theory is associated with the classical reference system (Section 8.4). The IAU 2000 theory is to be used in the improved classical and the new systems.

# 8.7.1 IAU 1980 Theory of Nutation

The IAU 1980 Theory of Nutation was the officially adopted theory from 1984 until 2003. It is adequate to accuracies of 1 mas. The IAU 1980 Theory of Nutation (Seidelmann, 1982; Wahr, 1981) was based on a modification of a rigid Earth theory published by Kinoshita (1977) and on the geophysical model 1066A of Gilbert and Dziewonski (1975). It included the effects of a solid inner core and a liquid outer core and a distribution of elastic parameters inferred from a large set of seismological data values. The corresponding pole was called the Celestial Ephemeris Pole (CEP) and is the axis of figure of the mean surface of the Earth. The nutation matrix $\mathcal { N }$ is a function of the nutation in longitude, $\Delta \psi$ , and the nutation in obliquity, $\Delta \epsilon$ , as follows:

$$
\begin{array} { r } { \mathcal { N } = \mathcal { R } _ { 1 } ( - \epsilon _ { A } ) \times \mathcal { R } _ { 3 } ( \Delta \psi ) \times \mathcal { R } _ { 1 } ( \epsilon _ { A } + \Delta \epsilon ) . } \end{array}
$$

The currently observed differences to the IAU 1976 precession and the IAU 1980 Theory of Nutation $\ S \Delta \psi$ and $\delta \Delta \epsilon$ are given as dpsi and deps in the IERS Bulletins.

These are with respect to the conventional celestial pole positions defined by the models and reported as celestial pole offsets by the IERS. Using these offsets, the corrected nutation is given by

$$
\begin{array} { r } { \Delta \psi = \Delta \psi ( \mathrm { I A U } 1 9 8 0 ) + \delta \Delta \psi , } \\ { \Delta \epsilon = \Delta \epsilon ( \mathrm { I A U } 1 9 8 0 ) + \delta \Delta \epsilon . } \end{array}
$$

This is practically equivalent to replacing $\mathcal { N }$ by

$$
\mathcal { N } ^ { \prime } = \left( \begin{array} { c c c } { 1 } & { - \delta \Delta \psi \cos \epsilon _ { t } } & { - \delta \Delta \psi \sin \epsilon _ { t } } \\ { \delta \Delta \psi \cos \epsilon _ { t } } & { 1 } & { \delta \Delta \epsilon } \\ { \delta \Delta \psi \sin \epsilon _ { t } } & { \delta \Delta \epsilon } & { 1 } \end{array} \right) \times \mathcal { N } ,
$$

where $\epsilon _ { t } = \epsilon _ { A } + \Delta \epsilon$ and $\mathcal { N }$ represents the IAU 1980 Theory of Nutation.

# 8.7.2 The precession–nutation model IAU 2000A and IAU 2000B

The precession–nutation model IAU 2000A has been adopted by the IAU 2000 (Resolution B1.6) to replace the IAU 1976 Precession and the IAU 1980 Theory of Nutation described above. This model, developed by Mathews et al. (2002), is based on the solution of linearized dynamical equations of the wobble nutation problem and makes use of estimated values of seven of the parameters appearing in the theory, obtained from a least-squares fit of the theory to an up-to-date precession– nutation VLBI data set. The series of nutation relies on the Souchay et al. (1999) rigid Earth nutation series, rescaled by 1.000 012 249 to account for the change in the dynamical ellipticity of the Earth implied by the observed correction to the luni-solar precession of the equator. The non-rigid Earth transformation is the MHB2000 model of Mathews et al. (2002), which improves the IAU 1980 Theory of Nutation by taking into account the effect of mantle anelasticity, ocean tides, electro-magnetic couplings produced between the fluid outer core and the mantle as well as between the solid inner core and fluid outer core, and the consideration of the linear terms which have hitherto been ignored in this type of formulation.

The resulting nutation series includes 678 luni-solar terms and 687 planetary terms and provides the direction of the celestial pole in the GCRS with an accuracy of 0.2 mas. The series includes the geodesic nutation (Section 5.3.4). This inclusion means that when using the precession–nutation model, the resulting position of stars are in the BCRS. If one insisted in having them in GCRS, one should subtract it from the precession–nutation series.

On the other hand, the free core nutation (FCN) being a free motion that cannot be predicted rigorously, is not considered as being part of the IAU 2000A model.

The IAU 2000 series of nutation is associated with improved numerical values for the precession rate of the equator in longitude and obliquity:

$$
\begin{array} { r l } & { \hat { \delta } \psi _ { A } = ( - 0 ^ { \prime } 2 9 9 6 5 \pm 0 ^ { \prime } 0 0 0 4 ) / \mathrm { c e n t u r y } , } \\ & { \hat { \delta } \omega _ { A } = ( - 0 ^ { \prime } 0 2 5 2 4 \pm 0 ^ { \prime } 0 0 0 1 ) / \mathrm { c e n t u r y } , } \end{array}
$$

as well as with the following offset of the direction of the CIP at J2000.0 from the direction of the pole of the GCRS:

$$
\begin{array} { r } { \psi _ { 0 } = ( - 0 \mathrm { : } 0 1 6 6 1 7 \pm 0 \mathrm { : } 0 0 0 1 ) , } \\ { \eta _ { 0 } = ( - 0 \mathrm { : } 0 0 6 8 1 9 \pm 0 \mathrm { : } 0 0 0 0 1 ) . } \end{array}
$$

As recommended by IAU 2000 (Resolution B1.6), an abridged model, designated IAU 2000B, is available for those who need a model only at the 1 mas level. Such a model has been developed by McCarthy and Luzum (2003); it includes 80 lunisolar terms plus a planetary bias to account for the effect of the planetary terms in the time period under consideration. It provides the celestial pole motion with an accuracy that does not result in a difference greater than 1 mas with respect to that of the IAU 2000A model during the period 1995–2050.

The precession quantities $\psi _ { A } , \theta _ { A } , \epsilon _ { A }$ , and $\chi _ { A }$ are necessary for computing the coordinates $X$ and $Y$ of the CIP in the GCRS using the current nutation series. On the other hand, the precession quantities $\zeta _ { A } , \theta _ { A }$ , and $z _ { A }$ are necessary for computing the precession matrix using the procedure described in Section 8.6.1. The expressions are those given in (8.11), together with:

$$
\begin{array} { r l } & { \omega _ { A } = \epsilon _ { 0 } + 0 \mathrm { { ' } } 0 5 1 2 7 t ^ { 2 } - 0 \mathrm { { ' } } 0 0 7 7 2 6 t ^ { 3 } , } \\ & { \epsilon _ { A } = \epsilon _ { 0 } - 4 6 \mathrm { { ' } } 8 1 5 0 t - 0 \mathrm { { ' } } 0 0 0 5 9 t ^ { 2 } + 0 \mathrm { { ' } } 0 0 1 8 1 3 t ^ { 3 } . } \end{array}
$$

with $\epsilon _ { 0 } = 8 4 3 8 1 _ { \cdot } ^ { \prime \prime } 4 4 8$ .

To derive the position $( X , Y , Z )$ of the CIP, the following procedure can be applied.

The inclination, $\omega$ , of the true equator of date on the ecliptic of J2000.0 and the longitude, $\psi$ , on the ecliptic of J2000.0, of the node of the true equator of date, are computed from the precession quantities by:

$$
\begin{array} { l } { \omega = \omega _ { A } + \delta \psi \sin \epsilon _ { A } \sin \chi _ { A } + \delta \epsilon \cos \chi _ { A } , } \\ { \psi = \psi _ { A } + \frac { \delta \psi \sin \epsilon _ { A } \cos \chi _ { A } - \delta \epsilon \sin \chi _ { A } } { \sin \omega _ { A } } . } \end{array}
$$

From these, one computes the intermediate coordinates of the pole (Capitaine, 1990),

$$
\begin{array} { r l } & { \bar { X } = \sin \omega \sin \psi , } \\ & { \bar { Y } = - \sin \epsilon _ { 0 } \cos \omega + \cos \epsilon _ { 0 } \sin \omega \cos \psi , } \end{array}
$$

and, finally,

$$
\begin{array} { r } { X = \bar { X } + \xi _ { 0 } - \bar { Y } \mathrm { d } \alpha _ { 0 } , } \\ { Y = \bar { Y } + \eta _ { 0 } + \bar { X } \mathrm { d } \alpha _ { 0 } , } \end{array}
$$

where $\xi _ { 0 } = - 0 . 0 1 6 6 1 7$ and $\eta _ { 0 } = - 0 . 0 0 6 8 1 9$ are the celestial pole offsets at the epoch J2000.0 and $\mathrm { d } \alpha _ { 0 }$ is the right ascension of the mean equinox. It is a very small quantity, of the order of 0.2 mas (Chapront et al., 1999) and can therefore be neglected.

The IAU 2000 nutation model is given by series for nutation in longitude $\delta \psi$ and obliquity $\Delta \epsilon$ , referred to the mean equator and equinox of date, with $t$ measured in Julian centuries from epoch J2000.0:

$$
\begin{array} { r l } & { \Delta \psi = \displaystyle \sum _ { i = 1 } ^ { N } ( ( A _ { i } + A _ { i } ^ { \prime } t ) \sin ( \mathrm { a r g u m e n t } ) + ( A _ { i } ^ { \prime \prime } + A _ { i } ^ { \prime \prime } t ) \cos ( \mathrm { a r g u m e n t } ) ) , } \\ & { \Delta \epsilon = \displaystyle \sum _ { i = 1 } ^ { N } ( ( B _ { i } + B _ { i } ^ { \prime } t ) \sin ( \mathrm { a r g u m e n t } ) + ( B _ { i } ^ { \prime \prime } + B _ { i } ^ { \prime \prime } t ) \cos ( \mathrm { a r g u m e n t } ) ) . } \end{array}
$$

The IAU 2000A subroutine, provided by T. Herring, is available electronically on the USNO website at: ftp://maia.usno.navy.mil/conv2000/chapter5/IAU2000A.f.

It produces celestial pole offsets based on the MHB2000 model with the exception of the free core nutation (FCN). The software can also be used to model the expected FCN based on the most recent astronomical observations. The IAU 2000B subroutine is available at:

ftp://maia.usno.navy.mil/conv2000/chapter5/IAU2000B.f.

The complete matrix algorithms for transformation between the terrestrial reference frame (ITRF) and ICRF, including precession, nutation, polar motion, and Earth’s rotation, are given for the classical, the improved classical, and the new CEO-based systems, in Section 10.6.

# 9 Terrestrial coordinate systems

In contrast with celestial reference frames, which have existed since the time when catalogs of stars over the whole sky became available, a global reference system for the positions on the Earth did not exist until direct geodesic links could be performed between regions separated by oceans and, more generally, by geographically or politically impassable barriers. So there were a number of local, geodetic coordinate systems, called datums, to which the positions of terrestrial sites were referred. They were given under the form of parameters defining the shape and the size of a reference ellipsoid, as well as its orientation with respect to some conventional features such as a mean pole and a zero meridian. The ellipsoid parameters were determined to best fit the local geoid (equipotential surface corresponding to the mean ocean level), and attached to the Earth by conventional coordinates of an initial point.

# 9.1 Introduction

At the beginning of the space age, positional and, later, laser or Doppler observations of satellites were used to link the individual datums and to place them in a unique terrestrial coordinate system. However, locally, countries continued (and many still do) to use their own datums for surveying and legal objectives. But for scientific purposes, this was a much too complex system, and a global terrestrial reference system had to be developed. As a first step, it was agreed to orient the reference frame with respect to a conventional terrestrial pole and zero meridian as defined by the Bureau International de l’Heure, and to adopt a Geodetic Reference System (GRS), (IAG, 1980), based upon an Earth equatorial radius of $\mathrm { ~ a ~ } =$ $6 3 7 8 1 3 7 \mathrm { m }$ and a polar radius of $\mathrm { b } = 6 3 5 6 7 5 2 . 3 \mathrm { m }$ . These values were used to build an absolute (that is centered at the center of mass of the Earth) datum called the World Geodetic System (WGS 84) (see DMA, 1987). This datum is in wide use, particularly in the USA. In the most recent datum, called World Geodetic Datum

2000 (WGD 2000), the parameters of the reference ellipsoid including the permanent deformation due to the Earth’s tides (Section 9.7.2), are: $a = 6 3 7 8 1 3 6 . 6 0 2 \pm$ $0 . 0 5 3 \mathrm { m }$ and $b = 6 3 5 6 7 5 2 . 8 6 0 \pm 0 . 0 5 2 \mathrm { m }$ (Grafarend and Ardalan, 1999).

On the other hand, for actual use in astrometry, one needs very accurate positions of observing instruments with respect to the center of mass of the Earth. For this reason, as well as for many applications in geodesy and geophysics, global terrestrial reference systems and frames in rectangular coordinates are built in an analogous way to its celestial counterpart (Section 7.2). These goals are realized by a certain number of fiducial points on the surface of the Earth, which are difficult to interconnect. However, it is necessary to have a continuous reference frame all over our planet. The role of the geodetic systems is to provide a frame that is readily accessible (Section 9.3).

# 9.2 Terrestrial reference systems

As in the case of celestial reference systems, it is first necessary to specify how such a system must be defined. Evidently it should be based on positions of a certain number of points on the Earth’s crust, but, in contrast with the extragalactic sources, their positions in any terrestrial coordinate system are not fixed, because the various parts of the crust move with respect to each other as the result of global tectonics, and because the crust as a whole undergoes periodic (Earth tides, atmospheric or ocean loading, etc.) and secular (post-glacial rebound, orogenic upheavals) deformations. As a consequence, there are no a priori markers that could be considered as fiducial points driven only by the global motions of the Earth. Another condition was that the definition of the Conventional Terrestrial Reference System (CTRS) should be compatible with the IAU resolutions on reference systems (Section 7.1).

So, in 1991, the International Union for Geodesy and Geophysics (IUGG) approved these conditions (IUGG, 1992) and endorsed the resolutions on reference systems of the XXI-st General Assembly of the IAU. It declared that the reference system so defined will be considered as the CTRS, also known as the International Terrestrial Reference System (ITRS). In this resolution, the IUGG also stated that the five items defining the ITRS should be:

(i) CTRS to be defined from a geocentric non-rotating system by a spatial rotation leading to a quasi-Cartesian system,   
(ii) the geocentric non-rotating system to be identical to the Geocentric Reference System (GRS) as defined in the IAU resolutions,   
(iii) the coordinate time of the CTRS as well as the GRS to be the Geocentric Coordinate Time (TCG),   
(iv) the origin of the system to be the geocenter of the Earth’s masses including oceans and atmosphere, and

(v) the system to have no global residual rotation with respect to horizontal motions at the Earth’s surface.

These considerations implied the following characteristic for the International Terrestrial Reference System (ITRS) adopted by the IERS (International Earth Rotation Service), which is in charge of realizing the corresponding reference frames. They are the following (Boucher, 1990):

(i) the terrestrial reference system is to be geocentric, the center of mass being defined for the whole Earth, including oceans and atmosphere,   
(ii) its scale is that of a local Earth frame as meant by a relativistic theory of gravitation,   
(iii) its orientation is the one initially given by the Bureau International de l’Heure (BIH) in 1984.0, and   
(iv) its time evolution in orientation will follow no global net rotation or translation condition.

The materialization of the ITRS is by a terrestrial reference frame through a network of station reference points, or ground marks, specified by Cartesian equatorial coordinates. The prime meridian OXZ is the international meridian, also called Greenwich meridian and the $O Y$ axis is on the equator towards the east. It was decided that the permanent solid Earth tidal deformations be included in the coordinates, so that the adopted coordinates will differ from the instantaneous coordinates by only periodic terms. In addition, as a consequence of item (iii) above, in defining the $O Z$ direction of the frame, care was taken that it coincides with the reference axis that defines the polar motion (Section 10.4.1).

This materialization was realized by successive approximations. Actually, several such frames were constructed and published by the IERS under the names International Terrestrial Reference Frame XX (ITRF-XX) where XX is the year of the last data used. This work was started in 1984 by the BIH, which had constructed a terrestrial reference frame under the conditions specified above. When the IERS was created, it took over the job and published successive solutions of ITRFs. This process led, in 1999, to the publication of ITRF-97 (Boucher et al., 1999). It was later superceded by the ITRF-2000 (Altamimi et al., 2002). This frame is to be considered as the terrestrial counterpart of the ICRF described in Section 7.2.

# 9.3 The ITRF series

Similar to the construction of the ICRF, the ITRF is the result of a compilation of geocentric station positions, OP, and velocities, V, provided for a given epoch, $t$ , by individual terrestrial reference frames constructed using different observing techniques. These are VLBI (Section 2.4.2), GPS (Section 2.4.1), laser ranging on satellites (Section 2.4.3), and DORIS (see Cazenave et al., 1992). The connection to the center of mass is ensured by a dynamical analysis of observations of satellites by lasers and GPS. Whenever a station is equipped with different instruments, an accurate local geodetic survey provides their connection to a well defined fiducial point on the site.

# 9.3.1 Construction of the ITRF-97

The bases of the computation of the ITRF-97 were 19 independent catalogs of station positions and velocities derived from observations spanning up to 23 years by one, or the other, of the techniques mentioned above. Then, they are reduced to a common epoch (1997.0) and a shift of the origin, a rotation, and scale factor are applied to put them in the ITRS. This is actually a method that is very similar to what was done in constructing the ICRS (Section 7.1), with the additional complication that the positions of the stations are drifting. If there are several instruments (stations) at the same site, the station velocities are constrained to be the same, while their relative positions are constrained by the results of the local survey. The description and position of the fiducial point adopted in each site are given in the publication (Boucher et al., 1999).

Finally, the ITRF-97 contained the rectangular components in the ITRS of the positions at epoch 1997.0 and the velocities expressed in meters and meters per year together with their standard uncertainties of 550 stations located on 325 sites. The velocities are constrained by a model of tectonic plate motions (DeMets et al., 1994), described in Table 9.1. These motions are defined by the components $\Omega _ { X }$ , $\Omega _ { Y }$ , and $\Omega _ { Z }$ of the rotation vector $\pmb { \Omega }$ . The positions of the plates considered in this table are shown in Fig. 9.1.

# 9.3.2 The ITRF-2000

For the first time in the history of the ITRFs, this new realization of the International Terrestrial Reference System combines unconstrained Space Geodesy solutions that are free from any tectonic plate motion model. The only condition that is retained is to ensure consistency with the series of Earth rotation parameters that link terrestrial and celestial frames as determined by IERS (see Chapter 10). On the whole, 30 individual solutions for the terrestrial reference frame were used in the construction of the ITRF-2000. They include solutions derived from individual techniques computed by different teams, multitechnique derivations, and GPS densifications, also determined by different methods and groups.

The ITRF-2000 is geocentric. The effect of the geocenter motion (Section 9.9.1) is deduced from the determination of the geocenter as sensed by satellite ranging and GPS solutions, but was afterwards averaged over the period of the observations (1991–2000). The scale is a weighted mean of VLBI, satellite ranging and GPS solutions. However, it was corrected by 0.7 parts per billion to meet the requirements to be in TCG time frame instead of TT used in the analyses. The orientation is aligned to ITRF-97 using only 50 continuously observed sites located on rigid parts of tectonic plates. The station positions are reduced to epoch 1997.0. The definition of the system is estimated to be at the level of $1 \ \mathrm { m m }$ /year (Altamimi et al., 2002).

Table 9.1. Components of the Cartesian rotation vectors for the main plates in milliarcseconds per year   

<table><tr><td>Plate name</td><td>Ωx</td><td>Ωy</td><td>z</td></tr><tr><td>Africa</td><td>+0.184</td><td>-0.639</td><td>+0.809</td></tr><tr><td>Antartica</td><td>-0.169</td><td>-0.351</td><td>+0.764</td></tr><tr><td>Arabia</td><td>+1.379</td><td>-0.107</td><td>+1.394</td></tr><tr><td>Australia</td><td>+1.628</td><td>+1.057</td><td>+1.296</td></tr><tr><td>Caribbean</td><td>-0.037</td><td>-0.698</td><td>+0.326</td></tr><tr><td>Cocos</td><td>-2.150</td><td>-4.456</td><td>+2.253</td></tr><tr><td>Eurasia</td><td>-0.202</td><td>-0.494</td><td>+0.650</td></tr><tr><td>India</td><td>+1.376</td><td>+0.008</td><td>+1.401</td></tr><tr><td>Juan de Fuca</td><td>+1.072</td><td>+1.776</td><td>-1.200</td></tr><tr><td>Nazca</td><td>-0.316</td><td>-1.769</td><td>+1.982</td></tr><tr><td>North America</td><td>+0.053</td><td>-0.742</td><td>0.032</td></tr><tr><td>Pacific</td><td>-0.311</td><td>+0.998</td><td>-2.056</td></tr><tr><td>Philippine</td><td>+2.081</td><td>-1.477</td><td>-1.994</td></tr><tr><td>Rivera</td><td>-1.937</td><td>-6.386</td><td>+2.485</td></tr><tr><td>Scotia</td><td>-0.085</td><td>-0.549</td><td>-0.262</td></tr><tr><td>South America</td><td>-0.214</td><td>-0.312</td><td>-0.179</td></tr></table>

![](images/c560ff9b28a10eef5aca81d6f2cc3a12c56e252075f0b239274b11fece668bba.jpg)  
Fig. 9.1. The 16 plates with their boundaries whose motions are given in the NNR-Novelia model (DeMets et al., 1994). Several minor plates are not shown.

![](images/e8cd060d279834c0795bb0ee41896f8dd1942316194522b7eeb30ff2e4c01415.jpg)  
Fig. 9.2. ITRF-2000 sites. The shape of the spots indicates the number of stations on the site (Altamimi et al., 2002).

On the whole, positions and velocities are given for about 500 sites (see Fig. 9.2). The positions of about half of them are determined to better than $1 \ \mathrm { c m }$ , and the uncertainties of the velocities of about 100 sites are estimated to be equal to, or smaller than $1 \mathrm { m m }$ /year.

# 9.3.3 Position of a point in the ITRF

Let OP and $\mathbf { V }$ be the position and velocity of a station in the ITRF-2000, its coordinates at a time $t$ are given by:

$$
\begin{array} { r } { \mathbf { O P } ( t ) = \mathbf { O P } ( 1 9 9 7 . 0 ) + \mathbf { V } ( t - 1 9 9 7 . 0 ) . } \end{array}
$$

All the secular motions are included in $\mathbf { V }$ , while all periodic terms are subtracted from the observations using models and additional local measurements (effects of underground water, variations of the atmospheric loading, local discrepancies from the model, etc.). In the absence of better local measurements, models described in Section 9.7 have to be applied to raw observations before obtaining the coordinates in ITRF.

Note that it is not possible to obtain the coordinates of the position of a point on the Earth, which is not part of the ITRF references, by some kind of interpolation. If a rather limited precision is needed – and this is the case for all astronomical observations of objects outside the Solar System – it is sufficient to use geodetic coordinates as shown in the next section. But this is not the case for observations in the vicinity of the Earth, for instance lunar laser observations. Here, centimeter or even millimeter accuracies are required. Then, one must proceed in establishing geodetic links with ITRF stations using, for instance, simultaneous GPS observations. If this cannot be repeated and no velocity can be determined, as a default, a kinematic tectonic plate motion model must be used under the form of a global rotation $\varOmega$ . The IERS Conventions (2001) advise the use of the NNR-Novelia model (DeMets et al., 1994). Table 9.1 gives the rotation angles around the OX, OY, and $O Z$ axes in milliarcseconds per year, the same as for ITRF-97.

# 9.4 Geodetic coordinates

As indicated in Section 9.2, it is preferable to use geocentric Cartesian coordinates $X , Y , Z$ to define the position of a point $P$ on the Earth. However, when one needs to represent some parameter over the Earth, it is necessary to have a continuous reference. The solution is the geodetic coordinates defined with respect to a reference ellipsoid whose center is at the geocenter.

Let us consider the meridian plane of the point (Fig. 9.3) and draw the intersection ellipse defined by its equatorial radius $a$ and its flattening $f ,$ or its polar radius $b = a ( 1 - f )$ . Let $x$ and $z$ be the geocentric coordinates of $P$ in the plane

$$
\begin{array} { l } { x = \sqrt { X ^ { 2 } + Y ^ { 2 } } = r \cos \varPhi , } \\ { z = Z = r \sin \varPhi , } \end{array}
$$

where $r$ is the geocentric distance and $\phi$ is the geocentric latitude

$$
\phi = \tan ^ { - 1 } ( z / x ) .
$$

Let us now compute $x$ and $z$ by using the reference ellipsoid. We assume here that the equatorial plane of the ellipsoid is the XOY plane of the ITRF. If this is not the case, one should first rotate the ITRF in such a way that these planes coincide.

The geodetic latitude $\phi _ { \mathrm { g } }$ is the angle between the $O x$ axis and the normal $P Q$ to the ellipse as drawn from $P .$ The geodetic height is $h = P H$ along the normal, $H ( \xi , \zeta )$ , being its intersection with the ellipse.