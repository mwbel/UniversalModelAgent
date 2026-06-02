Table 9.2: Delays (in millimeters) corresponding to the first to fourth higher order ionospheric delay terms (in columns) for a representative subset of typical frequencies used in radio astronomy and geodesy: the values are based on typical values of $| B _ { 0 } \cos \theta _ { 0 } | \sim 1 0 ^ { 4 } ~ \mathrm { n T }$ , $\theta _ { 0 } = \pi / 4$ , $N _ { 0 } = 1 0 ^ { 1 2 } \mathrm { m ^ { - 3 } }$ and $S = 3 \times 1 0 ^ { 1 8 } \mathrm { m ^ { - 2 } }$ (the values that can be typically neglected –those lower than 1 mm– can be clearly identified by a negative exponent).   

<table><tr><td>f/MHz</td><td>Technique</td><td></td><td></td><td></td><td>δp1,p,1 / mm δp1,p,2 / mm δp1,p,3 / mm δp1,p,4 / mm</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>150</td><td>NIMS</td><td>-5.3 · 106</td><td>-9.9·103</td><td></td><td>-4.8.103</td><td>-1.8· 101</td></tr><tr><td>400</td><td>NIMS /DORIS</td><td>-7.5 . 105</td><td>-5.2· 10²</td><td></td><td>-9.4· 101</td><td>-1.3·10-1</td></tr><tr><td>1228</td><td>GPS (L2)</td><td>-8.0·104</td><td>-1.8· 101</td><td></td><td>−1.1 · 100</td><td>-5.0·10-4</td></tr><tr><td>1575</td><td>GPS (L1)</td><td>-4.8·104</td><td>-8.5.100</td><td></td><td>-3.9 ·10-1</td><td>-1.4· 10-4</td></tr><tr><td>2000</td><td>DORIS</td><td>-3.0 · 104</td><td>-4.2· 100</td><td></td><td>-1.5·10-1</td><td>-4.2:10-5</td></tr><tr><td>2300</td><td>Low VLBI f.</td><td>-2.3· 104</td><td>-2.8·100</td><td></td><td>-8.8·10-2</td><td>-2.2·10-5</td></tr><tr><td>8400</td><td>High VLBI f.</td><td>−1.7 · 103</td><td>-5.7·10-2</td><td></td><td>-4.9·10-4</td><td>-3.3·10-8</td></tr><tr><td>12000</td><td>Time trans.low Ku f.</td><td>-8.3.102</td><td>-1.9 · 10-2</td><td></td><td>−1.1 · 10-4</td><td>-5.2 . 10-9</td></tr><tr><td>14000</td><td>Time trans.high Ku f.</td><td>-6.1·10²</td><td>−1.2 · 10-2</td><td></td><td>-6.2:10-5</td><td>-2.5.10-9</td></tr></table>

particular Jakowski et al. (1994) derived by ray tracing a simple expression for GPS in which, with the above introduced notation, the coefficient of the $f ^ { - 4 }$ term approximating the bending effect is:

$$
\Delta s _ { 3 } \simeq 2 . 4 9 5 \times 1 0 ^ { 8 } [ ( 1 - 0 . 8 5 9 2 \cos ^ { 2 } E ] ^ { - 1 / 2 } - 1 ] \cdot \hat { S } ^ { 2 }
$$

where $\mathrm { E }$ is the spherical elevation, i.e. the complement of the zenith angle with respect to the geocenter direction and where the units are not in SI system: the STEC $\hat { S }$ in TECU $= 1 0 ^ { 1 6 } \mathrm { m } ^ { - 3 }$ , the elevation $E$ in degrees and the factor $\Delta { s } _ { 3 }$ in $\mathrm { m m } { \cdot } ( \mathrm { M H z } ) ^ { 4 }$ . This expression is a particular approximation for GPS of the general results obtained for different frequencies. Details of the typical dependences for other frequencies can be seen in Figure 9.1 for different levels of electron content (8, 40 and 100 TECU) and different elevations (10, 25 and 50 degrees).

Recently Hoque and Jakowski (2008) proposed an update for this expresion taking into account the dependency not only on the STEC but also on the vertical distribution of electron content (by considering the F2 layer scale and maximum ionization heights, see Equation (23) in the given reference). But we retain Equation (9.37) for this document because, as the authors recognize in the same paper, these parameters are not easily available in the practice.

As the ray bending depends on the carrier frequency, an additional effect on the ionospheric correction appears when two different carriers are used, because the STEC differs on the two paths. However, following Hoque and Jakowski (2008) Equation (31), this effect is small (mm level at low elevation).

# Effects on code pseudorange data

The corresponding effect can be computed for the code pseudorange measurements, by using the well known relationship between phase and code refractive indices, $n _ { p }$ and $n _ { c }$ respectively, relating the phase velocity with the group (code) velocity, see for instance Davies (1990) page 13:

$$
n _ { c } = n _ { p } + f { \frac { d n _ { p } } { d f } }
$$

A similar relationship holds for the code and carrier phase ionospheric delays, $\delta \rho _ { I , c }$ and $\delta \rho _ { I , p }$ , after introducing Equation (9.38) in Equation (9.14):

$$
\delta \rho _ { I , c } = \delta \rho _ { I , p } + f \frac { d } { d f } \delta \rho _ { I , p }
$$

Applying Equation (9.39) to Equation (9.20), the ionospheric effect on code ionospheric delay, up to third order term, is:

$$
\delta \rho _ { I , c } = \frac { s _ { 1 } } { f ^ { 2 } } + 2 \frac { s _ { 2 } } { f ^ { 3 } } + 3 \frac { s _ { 3 } } { f ^ { 4 } }
$$

![](images/02af0500ed6ec808b267d4f0da04cf26a2910a175725293e8e7d1660173d6da5.jpg)  
Figure 9.1: Results of ray-tracing calculations concerning the dependency of the excess path length from the frequency of the propagation radio wave. At frequencies below $6 0 0 ~ \mathrm { M H z }$ the calculations correspond to a satellite height $h _ { s } = 1 0 0 0 \mathrm { k m }$ (NIMS/NNSS, DORIS) whereas above $6 0 0 ~ \mathrm { M H z }$ the calculations correspond to a satellite height $h _ { s } = 2 0 0 0 0 \mathrm { k m }$ (GPS, GLONASS) [Figure kindly provided by Dr. Norbert Jakowski, see Jakowski et al. (1994)]

It can be seen from this relationship, taking into account Equations (9.21), (9.22) and (9.23), that the ionospheric delay on the code pseudorange is positive, associated to a decrease of the EM signal group velocity in the transionospheric propagation.

# 9.4.2 Correcting the ionospheric effects on code and phase

The most efficient way of correcting the ionospheric effects is by combining simultaneous measurements in $k$ different frequencies, which allows to cancel the ionospheric effects up to order $k - 1$ , taking into account Equations (9.20) and (9.40) for carrier phase and code, respectively. A well know example is the case of the actual GPS system with two frequencies, which allows to cancel out the first order ionospheric effect by the so called ionospheric-free combination of observables (see below). And in the future, with Galileo and modernized GPS systems (broadcasting at three frequencies), the full correction can be extended to second order ionospheric terms too.

# Correcting the ionospheric term for single frequency users

If the user is only able to gather measurements at a single frequency $f$ , then his main problem is to correct as much as possible (or at least mitigate) the first order ionospheric terms in phase and code measurements, $\delta \rho _ { I , p , 1 }$ (9.20) and $\delta \rho _ { I , c , 1 }$ (9.40), which account for more than $9 9 . 9 \%$ of the total ionospheric delays, as we have shown above. Following (9.21) the first order ionospheric terms are only dependent on the Slant Total Electron Content R \~rR\~r Nedl and the signal frequency:

$$
\left. \begin{array} { l } { \delta \rho _ { I , p , 1 } = - 4 0 . 3 0 9 \frac { S } { f ^ { 2 } } } \\ { \delta \rho _ { I , c , 1 } = + 4 0 . 3 0 9 \frac { S } { f ^ { 2 } } } \end{array} \right\}
$$

Taking into account this expression, the single frequency users with available phase and code measurements at frequency $f _ { a }$ , and not interested on precise positioning, can use as main observable the so called Graphic combination $\begin{array} { r } { G _ { a } = \frac { 1 } { 2 } \left( \rho _ { c } ^ { a } + \rho _ { p } ^ { a } \right) } \end{array}$ . In this way the I1 ionospheric delay is completely removed at the price of having an observable with the half part of the code thermal and multipath noise, maintaining as additional unknown the carrier phase ambiguity for each continuous arc of phase data. However the graphic combination can be convenient for real-time users with relatively low requirements of accuracy, in conditions of maximum solar activity and/or low latitude and daylight time or strong ionospheric storms scenarios.

On the other hand, there are different available external sources for the STEC $S$ , which allow to directly correct the single frequency observables. Many of them provide the vertically integrated ionospheric free electron density, the so called Vertical Total Electron Content (VTEC), globally or at least at regional scale.

From the VTEC values ( $V$ ) corresponding to the observation time, the STEC $S$ can be estimated thanks to a factor approximating the conversion from the vertical to the slant Total Electron Content: the so called ionospheric mapping function, $M$ , by $S = M \cdot V$ .

Typically a thin shell spherical layer model, at a fixed effective ionospheric height $h$ , is applied:

$$
M = { \frac { 1 } { \sqrt { 1 - { \frac { r ^ { 2 } \cos ^ { 2 } E } { ( r + h ) ^ { 2 } } } } } }
$$

where $r$ and $E$ are the geocentric distance and ray spherical elevation taken from the user receiver. In the case of IGS the adopted effective height is $h = 4 5 0 k m$ . This approximation can introduce significant errors as well, of $5 \%$ or more, specially when the 3D nature of the electron density distribution $N _ { e }$ has a larger impact on the integrated (total electron content) values: at low elevation or low latitude observations, see for instance Hern´andez-Pajares et al. (2005). Other better approximations are possible, as Modified Single Mapping Function (Hugentobler et al. 2002), variable effective height, see Komjathy and Langley (1996) and Hern´andez-Pajares et al. (2005) or multilayer tomographic model, see for instance Hern´andez-Pajares et al. (2002).

Some common sources of electron content are:

• Global VTEC maps, such as those computed by the International GNSS Service (IGS) $< ^ { 5 } >$ from a global network of dual-frequency receivers. The user can compute its STEC, $S$ , from interpolating the VTEC maps and applying the corresponding mapping function given by Equation (9.42) with $h = 4 5 0 k m$ in IGS IONEX format, see Schaer et al. (1998). The IGS VTEC maps have typically errors of 10 to $2 0 \%$ , see for instance Hern´andez-Pajares (2004) and Or´us et al. (2002).   
• Predicted VTEC models such as those used by GNSS: Klobuchar model broadcasted in GPS navigation message, or NeQuick $< ^ { 6 } >$ for the future Galileo system. They can show average errors up to $5 0 \%$ (up to 30% at low latitude, see for instance Or´us et al. (2002) or Arag´on et al. (2004). Moreover predicted Global VTEC maps are available from IGS center CODE server $< ^ { 7 } >$ .   
• Regional VTEC models, which provide better accuracy by means of a better temporal and spatial resolution, thanks to the availability of dense networks of permanent receivers (e.g. for Japan, Europe or USA).   
Empirical standard models of the Ionosphere, based on all available data sources, such as the International Reference Ionosphere (IRI, Bilitza 1990) available at $< ^ { 8 } >$ or PIM (Daniell et al. 1995) available at $< ^ { 9 } >$ . If they

are adjusted to the actual conditions by means of one or several parameters, such as the Sun Spot Number (Bilitza et al. 1999), these empirical models can provide at least similar performance than predicted VTEC models for GNSS. Otherwise the performance can be poor, depending on the region and time.

Correcting the ionospheric term for dual frequency users In case the user is able to gather two simultaneous measurements at two frequencies, $f _ { a }$ and $f _ { b }$ , the situation is much better, because the first order term can be cancelled, elliminating more than $9 9 . 9 \%$ of the total ionospheric delay. The first-order-ionospheric-free combination $\rho _ { p } ^ { ( 1 ) }$ is defined by the weight factors $f _ { a } ^ { 2 }$ and $- f _ { b } ^ { 2 }$ as

$$
\rho _ { p } ^ { ( 1 ) } ( a , b ) = \frac { f _ { a } ^ { 2 } \rho _ { p } ^ { ( a ) } - f _ { b } ^ { 2 } \rho _ { p } ^ { ( b ) } } { f _ { a } ^ { 2 } - f _ { b } ^ { 2 } } .
$$

If the measurements at the two frequencies are not exactly simultaneous, with a time offset small enough to consider that the electron content does not vary between the two measurements, the linear combination can still be applied but it is necessary to account for the time offset10.

dependencies, for carrier phase and code ( The first-order-ionospheric-free combination leads to the following new ionospheric $\overline { { \delta \rho _ { I , p } ^ { ( 1 ) } } }$ and $\delta \rho _ { I , c } ^ { ( 1 ) }$ respectively), after considering Equations (9.20) and (9.40):

$$
\delta \rho _ { I , p } ^ { ( 1 ) } = \frac { f _ { a } ^ { 2 } \delta \rho _ { I , p } ^ { ( a ) } - f _ { b } ^ { 2 } \delta \rho _ { I , p } ^ { ( b ) } } { f _ { a } ^ { 2 } - f _ { b } ^ { 2 } } = \frac { s _ { 2 } } { f _ { a } f _ { b } ( f _ { a } + f _ { b } ) } + \frac { s _ { 3 } } { f _ { a } ^ { 2 } f _ { b } ^ { 2 } }
$$

$$
\delta \rho _ { I , c } ^ { ( 1 ) } = \frac { f _ { a } ^ { 2 } \delta \rho _ { I , c } ^ { ( a ) } - f _ { b } ^ { 2 } \delta \rho _ { I , c } ^ { ( b ) } } { f _ { a } ^ { 2 } - f _ { b } ^ { 2 } } = - \frac { 2 s _ { 2 } } { f _ { a } f _ { b } \big ( f _ { a } + f _ { b } \big ) } - \frac { 3 s _ { 3 } } { f _ { a } ^ { 2 } f _ { b } ^ { 2 } }
$$

where $s _ { 2 }$ and $s _ { 3 }$ depend on electron density $N _ { e }$ and magnetic field $\vec { B }$ , according to expressions (9.22) and (9.29). The following approximations can be done to facilitate the computations:

$$
s _ { 2 } = 1 . 1 2 8 4 \times 1 0 ^ { 1 2 } \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } B \cos \theta d l \simeq 1 . 1 2 8 4 \times 1 0 ^ { 1 2 } B _ { p } \cos \theta _ { p } \cdot S
$$

where $\boldsymbol { B } _ { p }$ and $\theta _ { p }$ are the magnetic field modulus and projecting angle with respect to the propagation direction, at an effective pierce point $p$ , and $S$ is the integrated electron density, or STEC $S$ . This approximation is used by Kedar et al. (2003) and Petrie et al. (2010), and in other references cited above.

For this equation, a source of magnetic field is needed, which should be more realistic than the dipolar one, such as the International Magnetic Reference Field (IMRF) available at ${ < } ^ { 1 1 } >$ or the Comprehensive Model 12 available at ${ < } ^ { 1 3 } >$ , to reduce errors of up to more than $6 0 \%$ in certain regions, see a discussion in Hern´andez-Pajares et al. (2007). Both models are provided as Fortran routines: the IMRF model is provided with a short description of the arguments as the subroutine igrf10syn in the file igrf10.f at ${ < } ^ { 1 1 } >$ . The Comprehensive Model CM4 is provided with a complete description of the arguments as cm4field.f at ${ < } ^ { 1 3 } >$ .

The third order coefficient can be approximated in terms of the maximum electron density along the ray path $N _ { m }$ :

$$
s _ { 3 } \simeq 8 1 2 \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } ^ { 2 } d l \simeq 8 1 2 \eta N _ { m } S
$$

We may take $\eta \simeq 0 . 6 6$ and $N _ { m }$ can be expressed as function of the slab thickness $H$ (which can be modelled as function on the latitude and local time) and the VTEC $V$ , see more details in Fritsche et al. (2005) and references therein.

These expressions typically lead for GPS to values ofthe second order ionospheric correction: for instance $\delta \bar { \rho } _ { I , p } ^ { ( 1 ) } \simeq 2 $ centimeters for cm for a given $S \simeq 3 0 0 \mathrm { \ T E C U = 3 \times 1 0 ^ { 1 8 } \ m ^ { - 3 } }$ magnetic field projection of $B \cos \theta \simeq 3 \times 1 0 ^ { 4 } n T$ .

Moreover the geometric path excess produced by the ray curvature (or bending) can be considered as an additional term depending on $f ^ { - 4 }$ , for instance using expression (9.37).

Then, to evaluate $\delta \rho _ { I , p } ^ { ( 1 ) }$ and $\delta \rho _ { I , c } ^ { ( 1 ) }$ we need as well an STEC source for $S$ , as in the case of single frequency users (see previous subsection). In this case, the double frequency measurements can be used, to provide a direct estimate of $S$ , from the first order term which contains more than $9 9 . 9 \%$ of it. For instance in GPS $S$ can be estimated from the ionospheric (geometry-free) combination of carrier phases $L _ { I } = L _ { 1 } - L _ { 2 }$ and codes ${ \cal P } _ { I } = { \cal P } _ { 2 } - { \cal P } _ { 1 }$ , where $L _ { i }$ and $P _ { i }$ are the carrier phase and code measurements for carrier frequency $f _ { i }$ , in length units. Indeed, writing ${ L _ { I } } ^ { 1 4 }$ and $P _ { I }$ in terms of the corresponding $B _ { I }$ term (which includes the carrier phase ambiguity and the interfrequency phase biases) and interfrequency delay code biases (DCBs) for receiver and transmitter $D$ and $D ^ { \prime }$ :

$$
{ \cal L } _ { I } = \alpha { \cal S } + { \cal B } _ { I } , \qquad { \cal P } _ { I } = \alpha { \cal S } + { \cal D } + { \cal D } ^ { \prime } ,
$$

where $\alpha = 4 0 . 3 0 9 \cdot ( f _ { 2 } ^ { - 2 } - f _ { 1 } ^ { - 2 } ) \simeq 1 . 0 5 \cdot 1 0 ^ { - 1 7 } \mathrm { m } ^ { 3 }$ , the STEC $S$ can be estimated as $S = ( L _ { I } - < L _ { I } - P _ { I } > - D - D ^ { \prime } ) / \alpha$ , where $< \cdot >$ is the average along a carrier phase continuous arc of transmitter-receiver data with no phase cycle-slips. This way of computing the STEC has certain advantages, specially when no external sources of STEC are available (such as in real-time conditions) or at low latitudes and elevations, see Hern´andez-Pajares et al. (2007) for corresponding discussion. Equations (9.44) to (9.47), with an adequate source of STEC and magnetic field (see above) provide a conventional method to correct the ionospheric higher order terms for dual frequency users.

An alternative approach to correcting the GPS measurements is to apply the second order ionospheric correction by means of redefining the first-order ionospheric free combination of observables (Brunner and Gu 1991), for instance in terms of the line-of-sight magnetic field projection term 15. This approach has the disadvantage of producing a time dependent carrier phase bias. More details on pros and cons of different approaches for higher order ionospheric corrections, including regional models such as Hoque and Jakowski (2007), can be found in Hern´andez-Pajares et al. (2008).

In the case of DORIS instruments, the measurements are directly the phase variations between successive epochs (intervals of 7 or 10 seconds). They can be processed using the time-differenced first-order-ionospheric-free combination (9.43). For example, for ionospheric studies, this leads to a differential VTEC. VTEC may be deduced with an iterative process (Fleury and Lassudrie, 1992, Li and Parrot, 2007). For the recent instruments (Jason 2 and after), the undifferenced phase and pseudo-range measurements are also available. The pseudo-range measurements are only used to synchronize the on-board oscillator in order to estimate with a sufficient accuracy the measurement time. The first order ionospheric effect can also be removed here using the corresponding combination. For higher order terms, it possible to use as corrections for Doppler the time differences of those for the carrier phase, calculated using the equations for phase given above. But some caution is necessary for DORIS, where the second order effect on the equivalent carrier phase is several times larger than for GPS, on account of the different choice of frequencies. The errors made in the phase correction, and therefore, in the time-differenced phase correction, will be larger. It is not necessary to apply these corrections on the code measurements because the required precision for synchronisation is not so high as for phase processing.

# Correcting the ionospheric term for multi (three or more)-frequency users

GNSS systems offering simultaneous observations in 3 or more frequencies should be available soon. Thence, in principle, it should be possible to cancel, from these $k$ simultaneous observations of the same transmitter-receiver pair, up to the first $k - 1$ ionospheric order terms.

As an example, and from Equation (9.43) applied to two pairs of three consecutive frequencies ( $f _ { a }$ , $f _ { b }$ and $f _ { c }$ ), is possible to define a combination of carrier phase observables that is first and second order ionospheric free, $\rho _ { p } ^ { ( 2 ) }$ :

$$
\rho _ { p } ^ { ( 2 ) } = \frac { f _ { a } f _ { b } ( f _ { a } + f _ { b } ) \rho _ { p } ^ { ( 1 ) } ( a , b ) - f _ { b } f _ { c } ( f _ { b } + f _ { c } ) \rho _ { p } ^ { ( 1 ) } ( b , c ) } { f _ { a } f _ { b } ( f _ { a } + f _ { b } ) - f _ { b } f _ { c } ( f _ { b } + f _ { c } ) }
$$

And in terms of the basic observables, given by Equation (9.43), it can be written as:

$$
\rho _ { p } ^ { ( 2 ) } = \frac { 1 } { f _ { a } + f _ { b } + f _ { c } } \left( \frac { f _ { a } ^ { 3 } \rho _ { p } ^ { ( a ) } } { ( f _ { a } - f _ { b } ) ( f _ { a } - f _ { c } ) } + \frac { f _ { b } ^ { 3 } \rho _ { p } ^ { ( b ) } } { ( f _ { b } - f _ { a } ) ( f _ { b } - f _ { c } ) } + \frac { f _ { c } ^ { 3 } \rho _ { p } ^ { ( c ) } } { ( f _ { c } - f _ { a } ) ( f _ { c } - f _ { b } ) } \right)
$$

From here and from Equation (9.44) the following remaining higher order ionospheric dependence can be deduced:

$$
\delta \rho _ { I , p } ^ { ( 2 ) } = \frac { s _ { 3 } } { f _ { a } f _ { c } ( f _ { b } ^ { 2 } + f _ { b } [ f _ { a } + f _ { c } ] ) }
$$

A similar definition to Equation (9.49) can be derived for the code observations resulting, by using Equation (9.45), in the following remaining higher order ionospheric dependency:

$$
\delta \rho _ { I , c } ^ { ( 2 ) } = \frac { - 2 s _ { 3 } } { f _ { a } f _ { c } ( f _ { b } ^ { 2 } + f _ { b } [ f _ { a } + f _ { c } ] ) }
$$

However it must be pointed out that the combination significantly increases the measurement noise. Indeed, from Equation (9.50), considering a simple hypothesis of gaussian independent and identical gaussian distribution for the measurement noise at different frequencies, it is easy to show that the increase of measurement noise is very important (e.g. 25x in Galileo E1, E6, E5 frequencies, 34x in GPS L1, L2, L5, 52x in Galileo E1, E5a, E5b).

# References

Arag´on, A., Or´us, R., Amarillo, F., Hern´andez-Pajares, M., Juan, J. M., and Sanz, J., 2004, “Performance of NeQuick ionospheric predictions compared with different ionospheric data,” Navitec04, December 2004, ESTEC/ESA, Noordwijk, The Netherlands.   
Bar-Sever, Y. E., Kroger, P. M., and Borjesson, J. A., 1998, “Estimating horizontal gradients of tropospheric path delay with a single GPS receiver,” J. Geophys. Res., 103(B3), pp. 5019–5035, doi: 10.1029/97JB03534.   
Bassiri, S., and Hajj, G., 1993, “High-order ionospheric effects on the global positioning system observables and means of modeling them,” Manuscr. Geod., 18, 280–289.   
Bilitza, D., 1990, “International reference ionosphere 1990,” URSI/COSPAR, NSSDC/WDC-A-R&S 90-22, http://iri.gsfc.nasa.gov/docs/IRI1990pp0-84.pdf.

Bilitza, D., Hern´andez-Pajares, M., Juan, J. M., and Sanz, J., 1999, “Comparison between IRI and GPS-IGS derived electron content during 1991-1997,” Phys. Chem. Earth, Part C, 24(4), pp. 311–319, doi: 10.1016/S1464- 1917(99)00004-5.

Boehm, J., Werl, B., and Schuh, H., 2006a, “Troposphere mapping functions for GPS and very long baseline interferometry from European Centre for Medium-Range Weather Forecasts operational analysis data,” J. Geophys. Res., 111, B02406, doi:10.1029/2005JB003629.

Boehm, J., Niell, A. E., Tregoning, P., and Schuh, H., 2006b, “Global Mapping Function (GMF): A new empirical mapping function based on numerical weather model data,” Geophys. Res. Lett., 33, L07304, doi:10.1029/2005GL025546.

Boehm, J., Heinkelmann, R., and Schuh, H., 2007b, “Short Note: A global model of pressure and temperature for geodetic applications,” J. Geod., 81(10), pp. 679–683, doi:10.1007/s00190-007-0135-3.

Brunner, F., and Gu, M., (1991), “An improved model for the dual frequency ionospheric correction of GPS observations,” Manuscr. Geod., 16, 205–214.

Chen, G. and Herring, T. A., 1997, “Effects of atmospheric azimuthal asymmetry on the analysis of space geodetic data,” J. Geophys. Res., 102(B9), pp. 20,489–20,502, doi: 10.1029/97JB01739.

Ciddor, P. E., 1996, “Refractive index of air: New equations for the visible and near infrared,” Applied Optics, 35(9), pp. 1566–1573, doi: 10.1364/AO.35.001566.

Ciddor, P. E. and Hill, R. J., 1999, “Refractive index of air. 2. Group index,” Applied Optics, 38(9), pp. 1663–1667, doi: 10.1364/AO.38.001663.

Daniell, R. E., Brown, L. D., Anderson, D. N., Fox, M. W., Doherty, P. H., Decker, D. T., Sojka, J. J., and Schunk, R. W., 1995, “Parameterized Ionospheric Model: A global ionospheric parameterization based on first principles models,” Radio Sci., 30(5), pp. 1499–1510, doi: 10.1029/95RS01826.

Datta-Barua, S., Walter, T., Blanch, J., and Enge, P., 2008, “Bounding higherorder ionosphere errors for the dual-frequency GPS user,” Radio Sci., 43, RS5010, doi:10.1029/2007RS003772.

Davies, K., 1990, Ionospheric Radio, IEE Electromagnetic Waves Series 31, PeterPergrinus Ltd., London, UK.

Davis, J. L., Herring, T. A., Shapiro, I. I., Rogers, A. E. E., and Elgered, G., 1985, “Geodesy by radio interferometry: effects of atmospheric modeling errors on estimates of baseline length,” Radio Sci., 20(6), pp. 1593–1607, doi: 10.1029/RS020i006p01593.

Fleury, R., and Lassudrie-Duchesne, P., 1992. “TEC measurements by means of the DORIS Satellite Positioning System,” Proceedings of International beacon satellite symposium (URSI-COSPAR), Cambridge , MA, USA, July 6-10, 1992.

Fritsche, M., Dietrich, R., Kn¨ofel, C., R¨ulke, A., Vey, S., Rothacher, M., and Steigenberger, P., 2005, “Impact of higher-order ionospheric terms on GPS estimates,” Geophys. Res. Lett., 32, L23311, doi:10.1029/2005GL024342.

Hern´andez-Pajares, M., 2004, “IGS Ionosphere WG Status Report: Performance of IGS Ionosphere TEC Maps -Position Paper-,” IGS Workshop, Bern, Switzerland, 2004 http://igs.org/igscb/resource/pubs/04 rtberne/Session11 1.pdf.

Hern´andez-Pajares, M., Juan, J. M., Sanz, J., and Colombo, O. L., 2002, “Improving the real-time ionospheric determination from GPS sites at very long distances over the equator,” J. Geophys. Res., 107(A10), 1296, doi:10.1029/2001JA009203.

Hern´andez-Pajares, M., Juan, J. M., and Sanz, J., 2005, “Towards a more realistic mapping function,” A: XXVIII General Assembly of URSI. International Union of Radio Science, p. 34-38.

Hern´andez-Pajares, M., Juan, J. M., Sanz, J., and Or´us, R., 2007, “Secondorder ionospheric term in GPS: Implementation and impact on geodetic estimates,” J. Geophys. Res., 112, B08417, doi:10.1029/2006JB004707.

Hern´andez-Pajares, M., Fritsche, M., Hoque, M., Jakowski, N., Juan, J. M., Kedar, S., Krankowski, A., Petrie, E., and Sanz, J., 2008, “Methods and other considerations to correct for higher-order ionospheric delay terms in GNSS,” IGS Analysis Center Workshop 2008, Miami Beach, Florida, USA, http://www.ngs.noaa.gov/IGSWorkshop2008/docs/Higher order iono terms IGSWS08 v18.ppt.

Herring, T. A., 1992, “Modeling atmospheric delays in the analysis of space geodetic data,” in Proceedings of refraction of transatmospheric signals in geodesy, Netherlands Geodetic Commission Series, 36, The Hague, Netherlands, pp. 157–164, http://www.ncg.knaw.nl/Publicaties/Geodesy/pdf/36DeMunck.pdf.

Hoque, M. M., and Jakowski, N., 2007, “Higher order ionospheric effects in precise GNSS positioning,” J. Geod., 81(4), pp. 259–268, doi: 10.1007/s00190-006- 0106-0.

Hoque, M. M., and Jakowski, N., 2008, “Estimate of higher order ionospheric errors in GNSS positioning,” Radio Sci., 43, RS5008, doi:10.1029/2007RS003817.

Hugentobler, U., Schaer, S., Beutler, G., Bock, H., Dach, R., J¨aggi, A., Meindl, M., Urschl, C., Mervart, L., Rothacher, M., Wild, U., Wiget, A., Brockmann, E., Ineichen, D., Weber, G., Habrich, H., and Boucher, C., 2002, “CODE IGS Analysis Center Technical Report 2002,” (see as well http://aiuws.unibe.ch/ionosphere/mslm.pdf.

Hulley, G. C., and Pavlis E. C., 2007, “A ray-tracing technique for improving Satellite Laser Ranging atmospheric delay corrections, including the effects of horizontal refractivity gradients,” J. Geophys. Res., 112, B06417, doi:10.1029/2006JB004834.

Ifadis, I. I., 1986, “The atmospheric delay of radio waves: modeling the elevation dependence on a global scale,” Technical Report No. 38L, Chalmers U. of Technology, G¨oteborg, Sweden.

International Union of Geodesy and Geophysics (IUGG), 1999, “Resolution 3 of the International Association of Geodesy,” Comptes Rendus of the XXII General Assembly, 19–30 July 1999, Birmingham, pp. 110–111.

Jakowski, N., Porsch, F., and Mayer, G., 1994, “Ionosphere-induced ray-path bending effects in precision satellite positioning systems,” Zeitschrift f¨ur Satellitengest¨utzte Positionierung, Navigation und Kommunikation, 1/94, pp. 6–13.

Kedar, S., Hajj, G. A., Wilson, B. D., and Heflin, M. B., 2003, “The effect of the second order GPS ionospheric correction on receiver positions,” Geophys. Res. Lett., 30(16), 1829, doi:10.1029/2003GL017639.

Komjathy, A., and Langley, R. B., 1996, “The effect of shell height on high precision ionospheric modelling using GPS,” Proceedings of the 1996 IGS Workshop, pp. 193–203, Silver Spring, MD, http://igs.org/igscb/resource/pubs/ac ws96b.pdf.

Kouba, J., 2008, “Implementation and testing of the gridded Vienna Mapping Function 1 (VMF1),” J. Geod., 82(4-5), pp. 193–205, doi:10.1007/s00190- 007-0170-0.

Lanyi, G., 1984, “Tropospheric delay effects in radio interferometry,” TDA Progress Report 42-78, pp. 152–159, http://ipnpr.jpl.nasa.gov/progress report/ 42-78/78N.PDF; see also Observation Model and Parameter Partials for the JPL VLBI Parameter Estimation Software ‘MASTERFIT’-1987, 1987, JPL Publication 83-39, Rev. 3, http://hdl.handle.net/2060/19880009139.   
Li, F., and Parrot, M., 2007, “Study of the TEC data obtained from the DORIS stations in relation to seismic activity,” Annals Geophys., 50(1), pp. 39–50.   
MacMillan, D. S., 1995, “Atmospheric gradients from very long baseline interferometry observations,” Geophys. Res. Lett., 22(9), pp. 1041–1044, doi: 10.1029/95GL00887.   
MacMillan, D. S., and Ma, C., 1997, “Atmospheric gradients and the VLBI terrestrial and celestial reference frames”, Geophys. Res. Lett., 24(4), pp. 453–456, doi:10.1029/97GL00143.   
Marini, J. W., 1972, “Correction of satellite tracking data for an arbitrary tropospheric profile,” Radio Sci., 7(2), pp. 223–231, doi: 10.1029/RS007i002p00223.   
Marini, J. W. and Murray, C. W., 1973, “Correction of laser range tracking data for atmospheric refraction at elevations above 10 degrees,” NASA-TM-X-70555, Goddard Space Flight Center, Greenbelt, MD, http://hdl.handle.net/2060/19740007037.   
Mendes, V. B., Prates, G., Pavlis, E. C., Pavlis, D. E., and Langley, R. B., 2002, “Improved mapping functions for atmospheric refraction correction in SLR,” Geophys. Res. Lett., 29(10), 1414, doi:10.1029/2001GL014394.   
Mendes, V. B., and Pavlis, E. C., 2003, “Atmospheric refraction at optical wavelengths: problems and solutions,” in Proceedings of the $1 3 ^ { t h }$ International Laser Ranging Workshop, Washington D.C., Noomen, R., Klosko, S., Noll, C., and Pearlman, M. (eds.), NASA/CP-2003-212248, http://cddis.gsfc.nasa.gov/lw13/docs/papers/atmos mendes 1m.pdf.   
Mendes, V. B., and Pavlis, E. C., 2004, “High-accuracy zenith delay prediction at optical wavelengths,” Geophys. Res. Lett., 31, L14602, doi:10.1029/2004GL020308.   
Mercier, F., 2009, personal communication (see ftp://tai.bipm.org/iers/conv2010/chapter9/add info/IonoDoris.pdf).   
Niell, A. E., 1996, “Global mapping functions for the atmosphere delay of radio wavelengths,” J. Geophys. Res., 101(B2), pp. 3227–3246, doi: 10.1029/95JB03048.   
Niell, A. E., 2001, “Preliminary evaluation of atmospheric mapping functions based on numerical weather models,” Phys. Chem. Earth, Part A, 26(6-8), pp. 475–480, doi: 10.1016/S1464-1895(01)00087-4.   
Niell, A. E., 2006, “Interaction of atmosphere modeling and VLBI analysis strategy,” in IVS 2006 General Meeting Proceedings, Behrend, D. and Baver, K. (eds.), NASA/CP-2006-214140, pp. 252–256, ftp://ivscc.gsfc.nasa.gov/pub/general-meeting/2006/pdf/niell.pdf.   
Or´us, R., Hern´andez-Pajares, M., Juan, J. M., Sanz, J., and Garcia-Fernandez, M., 2002, “Performance of different TEC models to provide GPS ionospheric corrections,” J. Atmos. Sol. Terr. Phys., 64(18), pp. 2055–2062, doi: 10.1016/S1364-6826(02)00224-9.   
Petrie, E. J., King, M. A., Moore, P., and Lavall´ee, D. A., 2010, “Higher-order ionospheric effects on the GPS reference frames and velocities,” J. Geophys. Res., 115(B3), B03417, doi: 10.1029/2009jb006677.   
Saastamoinen, J., 1972, “Atmospheric correction for the troposphere and stratosphere in radio ranging of satellites,” The Use of Artificial Satellites for Geodesy, Geophysical Monograph Series, 15, Henriksen, S. W., Mancini, A., Chovitz, B. H. (eds.), pp. 247–251.   
Schaer, S., Gurtner, W., and Feltens, J., 1998, “IONEX: The IONosphere Map EXchange Format Version 1,” ftp://igscb.jpl.nasa.gov/igscb/data/format/ionex1.ps.   
Sovers, O. J., and Jacobs, C. S., 1996, Observation Model and Parameter Partials for the JPL VLBI Parameter Estimation Software ‘MODEST’-1996, JPL Pub. 83–89, Rev. 6.   
Tesmer, V., Boehm, J., Heinkelmann, R., and Schuh, H., 2007, “Effect of different tropospheric mapping functions on the TRF, CRF, and position time series estimated from VLBI,” J. Geod., 81(6-8), pp. 409–421, doi:10.1007/s00190- 006-0126-9.   
Titov, O. A., 2004, “Construction of a celestial coordinate reference frame from VLBI data,” Astron. Rep., 48(11), pp. 941–948, doi:10.1134/1.1822976.   
Tregoning, P. and Herring, T. A., 2006, “Impact of a priori zenith hydrostatic delay errors on GPS estimates of station heights and zenith total delays, Geophys. Res. Lett., 33, L23303, doi:10.1029/2006GL027706.

# 10 General relativistic models for space-time coordinates and equations of motion

# 10.1 Time coordinates

IAU resolution A4 (1991) set the framework presently used to define the Barycentric Reference System (BRS) and the Geocentric Reference System (GRS). Its third recommendation defined Barycentric Coordinate Time (TCB) and Geocentric Coordinate Time (TCG) as time coordinates of the BRS and GRS, respectively. In the fourth recommendation another time coordinate is defined for the GRS, namely Terrestrial Time (TT). This framework was further refined by the IAU Resolutions B1.3 and B1.4 (2000) to provide consistent definitions for the coordinates and the metric tensor of the reference systems at the full post-Newtonian level (Soffel, 2000). The BRS was renamed Barycentric Celestial Reference System (BCRS) and the GRS was renamed Geocentric Celestial Reference System (GCRS). At the same time IAU Resolution B1.5 (2000) applied this framework to time coordinates and time transformations between reference systems, and IAU Resolution B1.9 (2000) re-defined Terrestrial Time (Petit, 2000). TT differs from TCG by a constant rate, $d T T / d T C G = 1 - L _ { G }$ , where $L _ { G } = 6 . 9 6 9 2 9 0 1 3 4 \times 1 0 ^ { - 1 0 }$ is a defining constant (see Chapter 1 Table 1.1). The value of $\boldsymbol { L } _ { G }$ has been chosen to provide continuity with the former definition of TT, i.e. that the unit of measurement of TT agrees with the SI second on the geoid. The difference between TCG and TT is equal to

$$
\mathrm { T C G } - \mathrm { T T } = \left( \frac { L _ { G } } { 1 - L _ { G } } \right) \times ( \mathrm { J D _ { T T } } - T _ { 0 } ) \times 8 6 4 0 0 ~ \mathrm { s } ,
$$

where JDTT is the TT Julian date and $T _ { 0 } = 2 4 4 3 1 4 4 . 5 0 0 3 7 2 5$ . To within $1 0 ^ { - 1 8 }$ in rate, it may be approximated as $\mathrm { T C G } - \mathrm { T T } = L _ { G } \times ( \mathrm { M J D } - 4 3 1 4 4 . 0 ) \times 8 6 4 0 0 \propto$ s where MJD refers to the modified Julian date of International Atomic Time (TAI). TAI is a realization of TT, apart from a constant offset: $\mathrm { T T } = \mathrm { T A I } + 3 2 . 1 8 4 ~ \mathrm { s }$ .

Before 1991, previous IAU definitions of the time coordinates in the barycentric and geocentric frames required that only periodic differences exist between Barycentric Dynamical Time (TDB) and Terrestrial Dynamical Time (TDT; Kaplan, 1981). As a consequence, the spatial coordinates in the barycentric frame had to be rescaled to keep the speed of light unchanged between the barycentric and the geocentric frames (Misner, 1982; Hellings, 1986). In these systems, a quantity with the dimension of time or length has a TDB-compatible value which differs from its TDT-compatible value by a scale (see also Chapter 1). This is no longer required with the use of the TCG/TCB time scales.

The relation between TCB and TDB is linear, but no precise definition of TDB had been provided by the IAU. In the IERS Conventions (2003) the relation was given in seconds by

$$
\mathrm { T C B } - \mathrm { T D B } = L _ { B } \times ( \mathrm { M J D } - 4 3 1 4 4 . 0 ) \times 8 6 4 0 0 ~ \mathrm { s } + P _ { 0 } , P _ { 0 } \approx 6 . 5 5 \times 1 0 ^ { - 5 } \mathrm { s } ,
$$

with the provision that no definitive value of $L _ { B }$ exists and such an expression should be used with caution.

In order to remove this ambiguity while keeping consistency with the time scale (formerly known as $\mathbf { \Delta T } _ { e p h }$ ) used in the Jet Propulsion Laboratory (JPL) solarsystem ephemerides (see Chapter 3) and with existing TDB implementations such as (Fairhead and Bretagnon, 1990), IAU Resolution B3 (2006) was passed to redefine TDB as the following linear transformation of TCB:

$$
\mathrm { T D B } = \mathrm { T C B } - L _ { B } \times ( \mathrm { J D } _ { \mathrm { T C B } } - T _ { 0 } ) \times 8 6 4 0 0 \ \mathrm { s } + T D B _ { 0 } ,
$$

where JDTCB is the TCB Julian date and where $L _ { B } = 1 . 5 5 0 5 1 9 7 6 8 \times 1 0 ^ { - 8 }$ and $T D B _ { 0 } = - 6 . 5 5 \times 1 0 ^ { - 5 } \mathrm { s }$ are defining constants (see Chapter 1 Table 1.1).

Figure 10.1 shows graphically the relationships between the time scales. See $< ^ { 1 } >$ for copies of the resolutions of the IAU General Assemblies (1991, 2000, 2006)

relating to reference systems and time coordinates. IAU Resolution A4 (1991) may also be found in IERS Technical Note 13, pp. 137–142, IAU Resolutions B1 and B2 (2000) in IERS Technical Note 32, pp. 117–126, and Resolutions of the $2 6 ^ { t h }$ IAU General Assembly (2006) in Appendix A of this document.

![](images/2cdfb49c78116e81b299034fdb301310c2cf4e495243b91b11f3d59eb3963193.jpg)  
Figure 10.1: Various relativistic time scales and their relations. Each of the coordinate time scales TCB, TCG, TT and TDB can be related to the proper time $\tau$ of an observer, provided that the trajectory of the observer in the BCRS and/or GCRS is known. Transformations shown as dashed lines are not explicitly described in this document.

The difference between Barycentric Coordinate Time (TCB) and Geocentric Coordinate Time (TCG) for any event ( $T C B$ , $\vec { x }$ ) in the barycentric frame involves a four-dimensional transformation,

$$
\mathrm { T C B } - \mathrm { T C G } = c ^ { - 2 } \Biggl \{ \int _ { t _ { 0 } } ^ { t } \lbrack \frac { v _ { e } ^ { 2 } } { 2 } + U _ { e x t } ( \vec { x } _ { e } ) \rbrack d t + \vec { v } _ { e } \cdot ( \vec { x } - \vec { x } _ { e } ) \Biggr \} + { \cal O } ( c ^ { - 4 } ) ,
$$

where $\vec { x } _ { e }$ and $\vec { v _ { e } }$ denote the barycentric position and velocity of the Earth’s center of mass, and $U _ { e x t }$ is the Newtonian potential of all of the solar system bodies apart from the Earth evaluated at the geocenter. In this formula, $t$ is TCB and $t _ { 0 }$ is chosen to be consistent with 1977 January 1, $0 ^ { \mathrm { h } } 0 ^ { \mathrm { m } } 0 ^ { \mathrm { s } }$ TAI, i.e. the value $T _ { 0 } = 2 4 4 3 1 4 4 . 5 0 0 3 7 2 5$ given above. Terms not specified in (10.4) are of order $1 0 ^ { - 1 6 }$ in rate, and IAU Resolution B1.5 (2000) provides formulas to compute the $O ( c ^ { - 4 } )$ terms and Equation (10.4) within given uncertainty limits up to $5 0 0 0 0 ~ \mathrm { k m }$ from the Earth.

The TCB $-$ TCG formula (10.4) may be expressed as

$$
\mathrm { T C B } - \mathrm { T C G } = \frac { L _ { C } \times ( T T - T _ { 0 } ) + P ( T T ) - P ( T _ { 0 } ) } { 1 - L _ { B } } + c ^ { - 2 } \vec { v _ { e } } \cdot ( \vec { x } - \vec { x } _ { e } )
$$

where the values of $L _ { C }$ and $L _ { B }$ may be found in Chapter 1 Table 1.1. Non-linear terms denoted by $P ( T T )$ have a maximum amplitude of around 1.6 ms.

Any of the recent solar system ephemerides mentioned in Chapter 3 could be numerically integrated to obtain a realization of Equation (10.4) with ns accuracy, see e.g. (Fienga et al., 2009) for INPOP08. For consistency with past versions of this document, we provide in the following different realizations of Equation (10.5):

• The terms $P ( T T ) - P ( T _ { 0 } )$ may be provided by a numerical time ephemeris such as TE405 (Irwin and Fukushima, 1999), with an accuracy of 0.1 ns from 1600 to 2200. TE405 is available in a Chebyshev form at $< ^ { 2 } >$ and at the IERS Conventions Center website ${ < } ^ { 3 } >$ . A similar product for the INPOP08 ephemeris (Fienga et al., 2009) is available at ${ < } ^ { 4 } >$ . • The terms $P ( T T )$ can be evaluated by the “FB” analytical model (Fairhead and Bretagnon, 1990; Bretagnon 2001). The 2001 version of the FB model is available at the IERS Conventions Center website ${ < } ^ { 3 } { > }$ or $< ^ { 5 } >$ , where the files of interest are fb2001.f, fb2001.dat, fb2001.in, fb2001.out, and README.fb2001.f. The SOFA (Standards of Fundamental Astronomy) service ${ < } ^ { 6 } >$ also provides a routine iau DTDB in both Fortran 77 and ANSI C to perform the computation, based on a less accurate version of the FB model.

• A series, HF2002, providing the value of $L _ { C } \times ( T T - T _ { 0 } ) + P ( T T ) - P ( T _ { 0 } )$ as a function of TT over the years 1600–2200 has been fit (Harada and Fukushima, 2002) to TE405. The HF2002 model is available at the IERS Conventions Center website ${ < } ^ { 3 } { > }$ , where the files of interest are xhf2002.f, HF2002.DAT and xhf2002.out (However, see below the updated version XHF2002 IERS.F).

Note that TE405 is an integration of Equation (10.4) and does not account for terms in $c ^ { - 4 }$ , and neither does HF2002 which was fit to TE405. On the other hand, the $L _ { C }$ value provided in Chapter 1 Table 1.1 includes a $1 . 1 5 \times 1 0 ^ { - 1 6 }$ contribution from terms in $c ^ { - 4 }$ and from the effect of asteroids. For best accuracy, the linear term $1 . 1 5 \times 1 0 ^ { - 1 6 } \times \left( T T - T _ { 0 } \right)$ should be added to the original TE405 and HF2002 results. For convenience, a version XHF2002 IERS.F is provided at ${ < } ^ { 3 } { > }$ , that directly provides the correct result of Equation (10.5) based on HF2002 and can be considered as the conventional TCB-TCG transformation.

Irwin (2003) has shown that TE405 and the 2001 version of the FB model differ by less than 15 ns over the years 1600 to 2200 and by only a few ns over several decades around the present time. HF2002 has been shown (Harada and Fukushima, 2002) to differ from TE405 by less than 3 ns over the years 1600–2200 with an RMS error of 0.5 ns. Note that in this section TT is assumed to be the time argument for computing TCB−TCG, while the actual time argument is that of the underlying solar-system ephemerides, i.e. a realization of TDB (see Chapter 3). The resulting error in TCB−TCG is at most approximately 20 ps.

# 10.2 Transformation between proper time and coordinate time in the vicinity of the Earth

Similarly to the time coordinate transformation, the formalism of the IAU resolutions is used to provide the transformation between the proper time of a clock and coordinate time. Formulas and references are presented here to perform this transformation in the vicinity of the Earth (typically up to geosynchronous orbit or slightly above). Evaluating the contributions of the higher order terms in the metric of the geocentric reference system (see IAU Resolution B1.3 (2000)), it is found that the IAU 1991 framework is sufficient for time and frequency applications in the GCRS in light of present clock accuracies. Nevertheless, in applying the IAU 1991 formalism, some care needs to be taken when evaluating the Earth’s potential at the location of the clock, especially when accuracy of order $1 0 ^ { - 1 8 }$ is required (Klioner, 1992; Wolf and Petit, 1995; Petit and Wolf, 1997; Soffel et al., 2003).

In this framework, the proper time of a clock $A$ located at the GCRS coordinate position ${ \bf x } _ { A } ( t )$ , and moving with the coordinate velocity $\mathbf { v } _ { A } = d \mathbf { x } _ { A } / d t$ , where t is TCG, is

$$
{ \frac { d \tau _ { A } } { d t } } = 1 - 1 / c ^ { 2 } \left[ { \bf v } _ { A } ^ { 2 } / 2 + U _ { \mathrm { E } } ( { \bf x } _ { A } ) + V ( X _ { \mathrm { A } } ) - V ( X _ { \mathrm { E } } ) - x _ { A } ^ { i } \partial _ { i } V ( X _ { \mathrm { E } } ) \right] .
$$

Here, $U _ { \mathrm { E } }$ denotes the Newtonian potential of the Earth at the position $\mathbf { x } _ { A }$ of the clock in the geocentric frame, and $V$ is the sum of the Newtonian potentials of the other bodies (mainly the Sun and the Moon) computed at a location $X$ in barycentric coordinates, either at the position $X _ { \mathrm { E } }$ of the Earth’s center of mass, or at the clock location $X _ { \mathrm { A } }$ . Only terms required for frequency transfer with uncertainty of order $1 0 ^ { - 1 8 }$ have been kept. For application to a given experiment, one should also consider the time amplitude of terms in Equation (10.6) that happen to be periodic and compare those terms to the expected time accuracy of the measurements. For example, the contribution of tidal terms (the last three terms in Equation (10.6)) will be limited to below $1 \times 1 0 ^ { - 1 5 }$ in frequency and a few ps in time amplitude up to the GPS orbit. In such cases, one can keep only the first three terms in relation (10.6) between the proper time $\tau _ { A }$ and the coordinate time $t$ :

$$
\frac { d \tau _ { A } } { d t } = 1 - 1 / c ^ { 2 } \left[ { \bf v } _ { A } ^ { 2 } / 2 + U _ { \mathrm { E } } ( { \bf x } _ { A } ) \right] .
$$

When using TT as coordinate time, following its defining relation $d T T / d T C G =$ $1 - L _ { G }$ , equations (10.6) and (10.7) are rewritten with the same accuracy as

$$
{ \frac { d \tau _ { A } } { d T T } } = 1 + L _ { G } - 1 / c ^ { 2 } \left[ { \bf v } _ { A } ^ { 2 } / 2 + U _ { \mathrm { E } } ( { \bf x } _ { A } ) + V ( X _ { \mathrm { A } } ) - V ( X _ { \mathrm { E } } ) - x _ { A } ^ { i } \partial _ { i } V ( X _ { \mathrm { E } } ) \right]
$$

and

$$
\frac { d \tau _ { A } } { d T T } = 1 + L _ { G } - 1 / c ^ { 2 } \left[ { \bf v } _ { A } ^ { 2 } / 2 + U _ { \mathrm { E } } ( { \bf x } _ { A } ) \right] ,
$$

respectively. In general, the relation between the proper time of a clock and coordinate time may be obtained by numerical integration of the adequate differential equation (10.6 to 10.9). In doing so, care should be taken to evaluate the Newtonian potential $U _ { E }$ with the uncertainty required by each use.

For GPS satellites, with nearly circular orbits at an altitude of approximately 20200 km, the combined relativistic frequency shift given by Equation (10.9) is about $4 . 5 \times 1 0 ^ { - 1 0 }$ and it consists of a constant offset of about $4 . 4 6 \times 1 0 ^ { - 1 0 }$ and periodical variations with amplitudes up to $1 0 ^ { - 1 1 }$ . The constant relativistic frequency offset is nearly compensated simply by proportionally offsetting the nominal frequency of all GPS satellite frequency standards by a conventional hardware offset of $- 4 . 4 6 4 7 \times 1 0 ^ { - 1 0 }$ . However, due to differences of mean orbit altitudes of GPS satellites, the actual relativistic frequency offsets for individual satellites can differ from the above conventional hardware offset by up to $1 0 ^ { - 1 3 }$ .

When retaining only the first term of the Newtonian potential, assuming a Keplerian orbit and that the constant relativistic offset is exactly compensated, integrating Equation (10.9) yields

$$
\mathrm { T T } = \tau _ { A } - \Delta \tau _ { A } ^ { p e r } , \Delta \tau _ { A } ^ { p e r } = - \frac { 2 } { c ^ { 2 } } \sqrt { a \cdot G M _ { \oplus } } \cdot e \cdot \sin { E } ,
$$

where $a$ , $e$ and $E$ are the orbit semi-major axis, eccentricity and eccentric anomaly angle. Thus $\Delta \tau _ { A } ^ { p e r }$ is the conventional GPS correction (see the GPS Interface Control Document available at $< ^ { \prime } >$ ) for the periodical relativity part, which is equally due to eccentricity induced velocity and potential variations in Equation (10.9). From the above equation, one can readily see that the amplitude of the periodical correction is proportional to the orbit eccentricity, i.e. equal to about $2 . 2 9 \mu \mathrm { s } \times e$ . Since the eccentricity $e$ for GPS orbits can reach up to 0.02, consequently the amplitude of $\Delta \tau _ { A } ^ { p e r }$ can reach up to 46 ns. An alternative expression for the relativistic periodic correction is

$$
\Delta \tau _ { A } ^ { p e r } = - \frac { 2 } { c ^ { 2 } } { \bf v } _ { A } \cdot { \bf x } _ { A } ,
$$

which is exactly equivalent to the preceding Keplerian orbit formulation, provided that the osculating Keplerian orbit elements are used. This formulation is used e.g. by the IGS (International GNSS Service) for its official GPS and GLONASS clock solution products.

By retaining also the oblateness term ( $J _ { 2 }$ ) of the potential, one can derive (Ashby, 2003; Kouba, 2004) a simple analytical approximation that contains an apparent relativistic clock rate 8 and a 6-h term due to $J _ { 2 }$ . Comparing to a complete numerical integration, Kouba (2004) finds that the conventional periodic relativistic correction (10.11) differs by periodic terms with amplitudes of about 0.1 and 0.2 ns, and periods of about 6 hours and 14 days, respectively, and that, for most of the new (Block IIR) GPS satellites, the 6-h term is already detectable by statistical analysis in the recent IGS final clock combinations. The deficiencies of the conventional relativistic correction (10.10, 10.11) will become even more significant for Galileo (see the Galileo Interface Control Document available at $< ^ { 9 } >$ ) as the frequency instability of the Galileo passive Hydrogen maser clocks is at a few parts in $1 0 ^ { 1 5 }$ for an averaging time of several hours (Droz et al., 2009). As the 6-h $J _ { 2 }$ term is of similar magnitude, it should be accounted for when determining and using the broadcast satellite clock model.

For low Earth orbit satellites (see e.g. Larson et al., 2007 for GRACE and TOPEX), the term in $J _ { 2 }$ is more important than at the GPS altitude so that Equation (10.11) may be significantly in error or even completely misleading. It is necessary to perform a numerical integration of Equation (10.9) using the term in $J _ { 2 }$ for the potential.

# 10.3 Equations of motion for an artificial Earth satellite $_ { 1 0 }$

The relativistic treatment of the near-Earth satellite orbit determination problem includes corrections to the equations of motion, the time transformations, and the measurement model. The two coordinate systems generally used when including relativity in near-Earth orbit determination solutions are the solar system barycentric frame of reference (BCRS) and the geocentric or Earth-centered frame of reference (GCRS), see Section 5.1.

Ashby and Bertotti (1986) constructed a locally inertial E-frame in the neighborhood of the gravitating Earth and demonstrated that the gravitational effects of the Sun, Moon, and other planets are basically reduced to their tidal forces, with very small relativistic corrections. Thus the main relativistic effects on a near-Earth satellite are those described by the Schwarzschild field of the Earth itself. This result makes the geocentric frame more suitable for describing the motion of a near-Earth satellite (Ries et al., 1989). Later on, two advanced relativistic formalisms have been elaborated to treat the problem of astronomical reference systems in the first post-Newtonian approximation of general relativity. One formalism is due to Brumberg and Kopeikin (Kopeikin, 1988; Brumberg and Kopeikin, 1989; Brumberg, 1991) and another one is due to Damour, Soffel and Xu (Damour, Soffel, Xu, 1991, 1992, 1993, 1994). These allow a full post-Newtonian treatment (Soffel, 2000) and form the basis of IAU Resolutions B1.3 and B1.4 (2000).

In the GCRS, the relativistic correction to the acceleration of an artificial Earth satellite is

$$
\begin{array} { r c l } { { \Delta \vec { r } } } & { { = } } & { { \frac { G M _ { E } } { c ^ { 2 } r ^ { 3 } } \bigg \{ \Big [ 2 ( \beta + \gamma ) \frac { G M _ { E } } { r } - \gamma \vec { \bar { r } } \cdot \vec { \vec { r } } \Big ] \vec { r } + 2 ( 1 + \gamma ) ( \vec { r } \cdot \vec { \bar { r } } ) \vec { \hat { r } } \bigg \} + } } \\ { { } } & { { } } & { { ( 1 + \gamma ) \frac { G M _ { E } } { c ^ { 2 } r ^ { 3 } } \bigg [ \frac { 3 } { r ^ { 2 } } ( \vec { r } \times \vec { \bar { r } } ) ( \vec { r } \cdot \vec { \bar { J } } ) + ( \vec { \bar { r } } \times \vec { J } ) \bigg ] + } } \\ { { } } & { { } } & { { \bigg \{ ( 1 + 2 \gamma ) \Big [ \vec { \hat { R } } \times \Big ( \frac { - G M _ { S } \vec { R } } { c ^ { 2 } R ^ { 3 } } \Big ) \Big ] \times \vec { \hat { r } } \bigg \} , } } \end{array}
$$

where

c = speed of light,

$\beta , \gamma = \mathrm { P P N }$ (parameterized post-Newtonian) parameters, equal to 1 in General

Relativity,

$\vec { r }$ is the position of the satellite with respect to the Earth, $\vec { R }$ is the position of the Earth with respect to the Sun, $\vec { J }$ is the Earth’s angular momentum per unit mass $( | \vec { J } | \cong 9 . 8 \times 1 0 ^ { 8 } \mathrm { m } ^ { 2 } / \mathrm { s }$ ), and

$G M _ { E }$ and $G M s$ are the gravitational coefficients of the Earth and

Sun, respectively.

For satellites in the vicinity of the Earth (up to geostationary orbit) the terms in Equation (10.12) can be evaluated with respect to the main Newtonian acceleration, as follows. The Schwarzschild terms (first line) are a few parts in $1 0 ^ { 1 0 }$ (high orbits) to $1 0 ^ { 9 }$ (low orbits) smaller; the effects of Lense-Thirring precession (frame-dragging, second line) and the geodesic (de Sitter) precession (third line) are about $1 0 ^ { 1 1 }$ to $1 0 ^ { 1 2 }$ smaller. The main effect of the Schwarzschild terms is a secular shift in the argument of perigee while the Lense-Thirring and de Sitter terms cause a precession of the orbital plane at a rate of the order of $0 . 8 \mathrm { \ m a s / y }$ (geostationary) to $1 8 0 \mathrm { \ m a s / y }$ (low orbit) for Lense-Thirring and $1 9 \mathrm { { \ m a s / y } }$ (independent of orbit height) for de Sitter. The Lense-Thirring terms are less important than the geodesic terms for orbits higher than Lageos (altitude above 6000 km) and more important for orbits lower than Lageos. The observable effects and their magnitude depend on the particular characteristics of each satellite orbit and on the set-up of the analysis software. E.g., neglecting the Schwarzschild terms while adjusting orbit parameters may cause an apparent reduction of the orbit radius by 4 mm for circular orbits at all heights (Hugentobler, 2008).

The relativistic effects of the Earth’s oblateness have been neglected here as they are typically even smaller but, if necessary, they could be included using the full post-Newtonian framework of IAU Resolutions B1.3 and B1.4 (2000). The independent variable of the satellite equations of motion may be, depending on the time transformation being used, either TT or TCG. Although the distinction is not essential to compute this relativistic correction, it is important to account for it properly in the Newtonian part of the acceleration.

# 10.4 Equations of motion in the barycentric frame (see footnote 10)

The n-body equations of motion for the solar system frame of reference (the isotropic Parameterized Post-Newtonian system with Barycentric Coordinate Time (TCB) as the time coordinate) are required to describe the dynamics of the solar system and artificial probes moving about the solar system (for example, see Moyer, 1971). These are the equations applied to the Moon’s motion for lunar laser ranging (Newhall et al., 1987). In addition, relativistic corrections to the laser range measurement, the data timing, and the station coordinates are required (see Chapter 11).

# References

Ashby, N. and Bertotti, B., 1986, “Relativistic effects in local inertial frames,” Phys. Rev. D, 34(8), pp. 2246–2259, doi: 10.1103/PhysRevD.34.2246.   
Ashby, N., 2003, “Relativity in the Global Positioning System”, Living Rev. Relativity, 6, 1, http://www.livingreviews.org/lrr-2003-1.   
Bretagnon, P., 2001, personal communication.

Brumberg, V. A., 1991, Essential Relativistic Celestial Mechanics, Adam Hilger, Bristol, 280 pp.

Brumberg, V. A., and Kopejkin, S. M., 1989, “Relativistic reference systems and motion of test bodies in the vicinity of the Earth,” Nuovo Cimento B, 103(1), pp. 63–98, doi: 10.1007/BF02888894.

Damour, T., Soffel, M., and Xu, C., 1991, “General-relativistic celestial mechanics I. Method and definition of reference systems,” Phys. Rev. D, 43(10), pp. 3273–3307, doi: 10.1103/PhysRevD.43.3273.

Damour, T., Soffel, M., and Xu, C., 1992, “General-relativistic celestial mechanics II. Translational equations of motion,” Phys. Rev. D, 45(4), pp. 1017–1044, doi: 10.1103/PhysRevD.45.1017.

Damour, T., Soffel, M., and Xu, C., 1993, “General-relativistic celestial mechanics III. Rotational equations of motion,” Phys. Rev. D, 47(8), pp. 3124–3135, doi: 10.1103/PhysRevD.47.3124.

Damour, T., Soffel, M., and Xu, C., 1994, “General-relativistic celestial mechanics IV. Theory of satellite motion,” Phys. Rev. D, 49(2), pp. 618–635, doi: 10.1103/PhysRevD.49.618.

Droz, F., Mosset, P., Wang, Q., Rochat, P., Belloni, M., Gioia, M., Resti, A., and Waller, P., 2009, “Space passive hydrogen maser - Performances and lifetime data,” Proc. EFTF-IFCS 2009, pp. 393–398, doi: 10.1109/FREQ.2009.5168208.

Fairhead, L. and Bretagnon, P., 1990, “An analytical formula for the time transformation TB $-$ TT,” Astron. Astrophys., 229(1), pp. 240–247.

Fienga, A., Laskar, J., Morley, T., Manche, H., Kuchynka, P., Le Poncin-Lafitte, C., Budnik, F., Gastineau, M. and Somenzi, L., 2009, “INPOP08, a 4-D planetary ephemeris: from asteroid and time-scale computations to ESA Mars Express and Venus Express contributions,” Astron. Astrophys., 507(3), pp. 1675–1686, doi: 10.1051/0004-6361/200911755.

Harada, W. and Fukushima, T., 2003, “Harmonic decomposition of time ephemeris TE405,” Astron. J., 126(5), pp. 2557–2561, doi: 10.1086/378909.

Hellings, R. W., 1986, “Relativistic effects in astronomical timing measurement,” Astron. J., 91(3), pp. 650–659, doi: 10.1086/114048. Erratum, ibid., 92(6), p. 1446, doi: 10.1086/114282.

Hugentobler U., 2008, personal communication.

Irwin A. W. and Fukushima, T., 1999, “A numerical time ephemeris of the Earth,” Astron. Astrophys., 348(2), pp. 642–652.

Irwin A., 2003, personal communication.

Kaplan, G. H., 1981, The IAU Resolutions on astronomical constants, time scales and the fundamental reference frame, U. S. Naval Observatory Circular No. 163, see http://www.usno.navy.mil/USNO/astronomical-applications/publications/ Circular 163.pdf.

Klioner, S.A., 1992, “The problem of clock synchronization: A relativistic approach,” Celest. Mech. Dyn. Astron. 53(1), pp. 81–109, doi: 10.1007/BF00049363.

Kopejkin, S. M., 1988, “Celestial coordinate reference systems in curved spacetime,” Celest. Mech., 44(1-2), pp. 87–115, doi: 10.1007/BF01230709.

Kouba, J., 2004, “Improved relativistic transformations in GPS,” GPS Solutions 8(3), pp. 170–180, doi: 10.1007/s10291-004-0102-x.

Larson, K. M., Ashby, N., Hackman, C., Bertiger, W., 2007, “An assessment of relativistic effects for low Earth orbiters: the GRACE satellites,” Metrologia 44(6), pp. 484–490, doi: 10.1088/0026-1394/44/6/007.

Misner, C. W., 1982, Scale Factors for Relativistic Ephemeris Coordinates, NASA Contract NAS5-25885, Report, EG&G, Washington Analytical Services Center, Inc.   
Moyer, T. D., 1971, Mathematical formulation of the double-precision orbit determination program (DPODP), JPL Technical Report 32–1527, see http://hdl.handle.net/2060/19710017134.   
Newhall, X. X., Williams, J. G., and Dickey, J. O., 1987, “Relativity modeling in lunar laser ranging data analysis,” in Proc. of the International Association of Geodesy (IAG) Symposia, Vancouver, pp. 78–82.   
Petit, G., 2000, “Report of the BIPM/IAU Joint Committee on relativity for space-time reference systems and metrology”, in Proc. of IAU Colloquium 180, Johnston, K. J., McCarthy, D. D., Luzum, B. J. and Kaplan, G. H. (eds.), U. S. Naval Observatory, Washington, D. C., pp. 275–282.   
Ries, J. C., Huang, C., Watkins, M. M., and Tapley, B. D., 1990, “The effects of general relativity on near-Earth satellites,” Astrodynamics 1989, Advances in the Astronautical Sciences, 71, Thornton, C. L., Proulx, R. J., Prussing, J. E., and Hoots, F. R. (eds.), pp. 85–93.   
Soffel, M., 2000, “Report of the working group Relativity for Celestial Mechanics and Astrometry”, in Proc. of IAU Colloquium 180, Johnston, K. J., McCarthy, D. D., Luzum B. J., and Kaplan, G. H. (eds.), U. S. Naval Observatory, Washington, D. C., pp. 283–292.   
Soffel, M., Klioner, S., Petit, G., Wolf, P., et al., 2003, “The IAU2000 resolutions for astrometry, celestial mechanics and metrology in the relativistic framework: explanatory supplement,” Astron. J. 126(6), pp. 2687–2706, doi: 10.1086/378162.   
Wolf, P. and Petit, G., 1995, “Relativistic theory for clock syntonization and the realization of geocentric coordinate times,” Astron. Astrophys. 304, pp. 653–661.

# 11 General relativistic models for propagation

# 11.1 VLBI time delay

# 11.1.1 Historical background

To resolve differences between numerous procedures used in the 1980s to model the VLBI delay, and to arrive at a standard model, a workshop was held at the U. S. Naval Observatory on 12 October 1990. The proceedings of this workshop have been published (Eubanks, 1991) and the model given there was called the ‘consensus model.’ It was derived from a combination of five different relativistic models for the geodetic delay. These are the Masterfit/MODEST model, due to Fanselow and Thomas (see Treuhaft and Thomas, in Eubanks, 1991; Sovers and Fanselow, 1987), the I. I. Shapiro model (see Ryan, in Eubanks, 1991), the Hellings-Shahid-Saless model (Shahid-Saless et al., 1991, and in Eubanks, 1991), the Soffel, M¨uller, Wu and Xu model (Soffel et al., 1991, and in Eubanks, 1991), and the Zhu-Groten model (Zhu and Groten, 1988, and in Eubanks, 1991). At the same epoch, a relativistic model of VLBI observations was also presented in Kopeikin (1990) and in Klioner (1991).

The ‘consensus model’ formed the basis of that proposed in the IERS Standards (McCarthy, 1992). Over the years, there was considerable discussion and misunderstanding on the interpretation of the stations’ coordinates obtained from the VLBI analyses. Particularly the IERS Conventions (McCarthy, 1996) proposed a modification of the delay, erroneously intending to comply with the XXIst General Assembly of the International Astronomical Union in 1991 and the XXth General Assembly of the International Union of Geodesy and Geophysics in 1991 Resolutions defining the Geocentric Reference System. It seems, however, that this modification was not implemented by IERS analysis centers.

In the presentation below, the model is developed in the frame of the IAU Resolutions i.e. general relativity ( $\gamma$ is a PPN (parameterized post-Newtonian) parameter equal to 1 in GRT) using the Barycentric Celestial Reference System (BCRS) and Geocentric Celestial Reference System (GCRS). However two approaches are presented for its usage, depending on the choice of coordinate time in the geocentric system. It is discussed how the Terrestrial Reference System (TRS) VLBI station coordinates submitted to the IERS, and the resulting ITRF coordinates (Chapter 4), should be interpreted in relation to the IAU and IUGG Resolutions.

The ‘step-by-step’ procedure presented here to compute the VLBI time delay is taken from Eubanks (1991) and the reader is urged to consult that publication for further details.

# 11.1.2 Specifications and domain of application

The model is designed primarily for the analysis of VLBI observations of extragalactic objects acquired from the surface of the Earth.1 All terms of order $1 0 ^ { - 1 3 }$ seconds or larger are included to ensure that the final result is accurate at the picosecond level. It is assumed that a linear combination of dual frequency measurements is used to remove the dispersive effect of the ionosphere, so that atmospheric effects are only due to the troposphere.

The model is not intended for use with observations of sources in the solar system, nor is it intended for use with observations made from space-based VLBI, from either low or high Earth orbit, or from the surface of the Moon (although it would be suitable with obvious changes for observations made entirely from the Moon).

The GCRS is kinematically non-rotating (not dynamically non-rotating) and, included in the precession constant and nutation series, are the effects of the geodesic precession $\mathrm { { \Omega } ^ { \prime } \sim 1 9 \ m a s / y }$ ). If needed, Soffel et al. (1991) and Shahid-Saless et al. (1991) give details of a dynamically inertial VLBI delay equation. At the picosecond level, there is no practical difference for VLBI geodesy and astrometry except for the adjustment in the precession constant.

In principle, the observable quantities in the VLBI technique are recorded signals measured in the proper time of the station clocks. On the other hand, the VLBI model is expressed in terms of coordinate quantities in a given reference system (see Chapter 10 for a presentation of the different coordinate times used). For practical considerations, particularly because the station clocks do not produce ideal proper time (they even are, in general, synchronized and syntonized to Coordinated Universal Time to some level, i.e. they have the same rate as the coordinate time Terrestrial Time (TT)), the VLBI delay produced by a correlator may be considered to be, within the uncertainty aimed at in this chapter, equal to the TT coordinate time interval $d _ { T T }$ between two events: the arrival of a radio signal from the source at the reference point of the first station and the arrival of the same signal at the reference point of the second station. Note that we model here only the propagation delay and do not account for the desynchronization or desyntonization of the station clocks. From a TT coordinate interval, $d _ { T T }$ , one may derive a Geocentric Coordinate Time (TCG) coordinate interval, $d _ { T C G }$ , by simple scaling: $d _ { T C G } = d _ { T T } / ( 1 - L _ { G } )$ , where $\boldsymbol { L } _ { G }$ is given in Table 1.1. In the following, two different approaches are presented using two different geocentric coordinate systems with either TCG or TT as coordinate time.

The VLBI model presented below (formula (9)) relates the TCG coordinate interval $d _ { T C G } = t _ { v _ { 2 } } - t _ { v _ { 1 } }$ to a baseline $\vec { b }$ expressed in GCRS coordinates (see the definition of notations in the next section). In the first approach, therefore, if the VLBI delay was scaled to a TCG coordinate interval, as described above, the results of the VLBI analysis would be directly obtained in terms of the spatial coordinates of the GCRS, as is recommended by the IUGG Resolution 2 (1991) and IAU Resolution B6 (1997), i.e. one would obtain TRS coordinates that are termed “TCG-compatible,” here denoted $x _ { T C G }$ .

In the second approach, if the VLBI model (formula (9)) is used with VLBI delays as directly provided by correlators (i.e. equivalent to a TT coordinate interval $d _ { T T }$ without transformation to TCG), the baseline $\vec { b }$ is not expressed in GCRS but in some other coordinate system. The transformation of these coordinates to GCRS results, at the level of uncertainty considered here, in a simple scaling. The TRS space coordinates resulting from the VLBI analysis (here denoted $\mathcal { X } V L B I$ ) are then termed “TT-compatible” and the TRS coordinates recommended by the IAU and IUGG resolutions, xT CG, may be obtained a posteriori by $x _ { T C G } = x _ { V L B I } / ( 1 { - } L _ { G } )$ (see Petit, 2000).

All VLBI analysis centers submitting results to the IERS have used this second approach and, therefore, the VLBI space coordinates are of the type $x V L B I$ . For continuity, an ITRF workshop (November 2000) decided to continue to use this approach, making it the present conventional choice for submission to the IERS. Note that the use of TT-compatible space coordinates is also the present conventional choice for SLR analysis results submitted to the IERS. At the ITRF workshop, it was also decided that the coordinates should not be re-scaled to $x _ { T C G }$ for the computation of ITRF2000 (see Chapter 4) so that the scale of ITRF realizations since ITRF2000 does not comply with IAU and IUGG resolutions.

# 11.1.4 The VLBI delay model

Although the delay to be calculated is the time of arrival at station 2 minus the time of arrival at station 1, it is the time of arrival at station 1 that serves as the time reference for the measurement. Unless explicitly stated otherwise, all vector and scalar quantities are assumed to be calculated at $t _ { 1 }$ , the time of arrival at station 1 including the effects of the troposphere. The VLBI hardware provides the UTC time tag for this event. For quantities such as $\vec { X } _ { J }$ , $\mathrm { v } _ { \oplus }$ , $\vec { w } _ { i }$ , or $U$ it is assumed that a table (or numerical formula) is available as a function of a given time argument. The UTC time tag should be transformed to the appropriate timescale corresponding to the time argument to be used to compute each element of the geometric model.

The baseline vector $\vec { b }$ is given in the kinematically non-rotating GCRS. It must

$t _ { i }$ the TCG time of arrival of a radio signal at the $i ^ { t h }$ VLBI receiver $T _ { i }$ the TCB time of arrival of a radio signal at the $i ^ { t h }$ VLBI receiver $t _ { g _ { i } }$ the “geometric” TCG time of arrival of a radio signal at the $i ^ { t h }$ VLBI receiver including the gravitational “bending” delay and the change in the geometric delay caused by the existence of the atmospheric propagation delay but neglecting the atmospheric propagation delay itself tvi the “vacuum” TCG time of arrival of a radio signal at the $i ^ { t h }$ VLBI receiver including the gravitational delay but neglecting the atmospheric propagation delay and the change in the geometric delay caused by the existence of the atmospheric propagation delay   
δtatmi the atmospheric propagation TCG delay for the $i ^ { t h }$ $\mathbf { \nabla } ^ { n } \mathrm { \ r e c e i v e r } = t _ { i } - t _ { g _ { i } }$ $T _ { i , \ j }$ the approximation to the TCB time that the ray path to station $i$ passed closest to gravitating body $J$   
∆Tgrav the differential TCB gravitational time delay $\vec { x } _ { i } ( t _ { i } )$ the GCRS radius vector of the $i ^ { t h }$ receiver at $t _ { i }$ $\vec { b }$ $\vec { x } _ { 2 } ( t _ { 1 } ) - \vec { x } _ { 1 } ( t _ { 1 } )$ , the GCRS baseline vector at the time of arrival $t _ { 1 }$ $\delta \vec { b }$ a variation (e.g. true value minus $a$ priori value) in the GCRS baseline vector $\vec { w } _ { i }$ the geocentric velocity of the $i ^ { t h }$ receiver $\hat { K }$ the unit vector from the barycenter to the source in the absence of gravitational or aberrational bending $\hat { k } _ { i }$ the unit vector from the $i ^ { t h }$ station to the source after aberration $\vec { X _ { i } }$ the barycentric radius vector of the $i ^ { t h }$ receiver $\vec { X _ { \oplus } }$ the barycentric radius vector of the geocenter $\vec { X } _ { J }$ the barycentric radius vector of the $J ^ { t h }$ gravitating body $\vec { R } _ { i J }$ the vector from the $J ^ { t h }$ gravitating body to the $i ^ { t h }$ receiver R\~ ⊕J the vector from the $J ^ { t h }$ gravitating body to the geocenter $\vec { R } _ { \oplus _ { \odot } }$ the vector from the Sun to the geocenter NˆiJ the unit vector from the $J ^ { t h }$ gravitating body to the $i ^ { t h }$ receiver $\vec { V } _ { \oplus }$ the barycentric velocity of the geocenter $U$ the gravitational potential at the geocenter, neglecting the effects of the Earth’s mass. At the picosecond level, only the solar potential need be included in $U$ so that $U = G M _ { \odot } / | \vec { R } _ { \oplus _ { \odot } } |$ $M _ { i }$ the rest mass of the $i ^ { t h }$ gravitating body $M _ { \oplus }$ the rest mass of the Earth $c$ the speed of light $G$ the Gravitational Constant

Vector magnitudes are expressed by the absolute value sign $[ | x | = ( \Sigma x _ { i } ^ { 2 } ) ^ { \frac { 1 } { 2 } } ]$ . Vectors and scalars expressed in geocentric coordinates are denoted by lower case (e.g. $\vec { x }$ and $t$ ), while quantities in barycentric coordinates are in upper case (e.g. $\vec { X }$ and $T$ ). A lower case subscript (e.g. $\vec { x } _ { i }$ ) denotes a particular VLBI receiver, while an upper case subscript (e.g. ${ \vec { x } } _ { J }$ ) denotes a particular gravitating body. The SI system of units is used throughout.

be transformed to the rotating terrestrial reference frame defined in Chapter 4 of the present VLBI Conventions in accordance to the transformations introduced in Chapter 5.

(a) Gravitational delay2

The general relativistic delay, $\Delta T _ { g r a v }$ , is given for the $J ^ { t h }$ gravitating body by

$$
\Delta T _ { g r a v _ { J } } = 2 \frac { G M _ { J } } { c ^ { 3 } } \ln \frac { | \vec { R } _ { 1 _ { J } } | + \vec { K } \cdot \vec { R } _ { 1 _ { J } } } { | \vec { R } _ { 2 _ { J } } | + \vec { K } \cdot \vec { R } _ { 2 _ { J } } } .
$$

At the picosecond level it is possible to simplify the delay due to the Earth, $\Delta T _ { g r a v _ { \oplus } }$ , which becomes

$$
\Delta T _ { g r a v _ { \oplus } } = 2 \frac { G M _ { \oplus } } { c ^ { 3 } } \ln \frac { | \vec { x } _ { 1 } | + \vec { K } \cdot \vec { x } _ { 1 } } { | \vec { x } _ { 2 } | + \vec { K } \cdot \vec { x } _ { 2 } } .
$$

The Sun, the Earth and Jupiter must be included, as well as the other planets in the solar system along with the Earth’s Moon, for which the maximum delay change is several picoseconds. The major satellites of Jupiter, Saturn and Neptune should also be included if the ray path passes close to them. This is very unlikely in normal geodetic observing but may occur during planetary occultations. Note that in case of observations very close to some massive bodies, extra terms (e.g. due to the multipole moments and spin of the bodies) should be taken into account to obtain an uncertainty of 1 ps (see Klioner, 1991).

The effect on the bending delay of the motion of the gravitating body during the time of propagation along the ray path is small for the Sun but can be several hundred picoseconds for Jupiter (see Sovers and Fanselow, 1987, page 9). Since this simple correction, suggested by Sovers and Fanselow (1987) and Hellings (1986) among others, is sufficient at the picosecond level, it was adapted for the consensus model. It is also necessary to account for the motion of station 2 during the propagation time between station 1 and station 2. In this model $\vec { R } _ { i _ { J } }$ , the vector from the $J ^ { t h }$ gravitating body to the $i ^ { t h }$ receiver, is iterated once, giving

$$
t _ { 1 _ { J } } = \operatorname* { m i n } \left[ t _ { 1 } , t _ { 1 } - \frac { \hat { K } \cdot ( \vec { X } _ { J } ( t _ { 1 } ) - \vec { X } _ { 1 } ( t _ { 1 } ) ) } { c } \right] ,
$$

so that

$$
\vec { R } _ { 1 _ { J } } ( t _ { 1 } ) = \vec { X } _ { 1 } ( t _ { 1 } ) - \vec { X } _ { J } ( t _ { 1 _ { J } } ) ,
$$

and

$$
\vec { R } _ { 2 _ { J } } = \vec { X } _ { 2 } ( t _ { 1 } ) - \frac { \vec { V } _ { \oplus } } { c } ( \hat { K } \cdot \vec { b } ) - \vec { X } _ { J } \big ( t _ { 1 _ { J } } \big ) .
$$

Only this single iteration is needed to obtain picosecond level accuracy for solar system objects.

$\vec { X _ { 1 } } ( t _ { 1 } )$ is not tabulated, but can be inferred from $\vec { X } _ { \oplus } ( t _ { 1 } )$ using

$$
\vec { X _ { i } } ( t _ { 1 } ) = \vec { X _ { \oplus } } ( t _ { 1 } ) + \vec { x _ { i } } ( t _ { 1 } ) ,
$$

which is of sufficient accuracy for use in equations (11.3) to (11.5), when substituted into Equation (11.1) but not for use in computing the geometric delay. The total gravitational delay is the sum over all gravitating bodies including the Earth,

$$
\Delta T _ { g r a v } = \sum _ { J } \Delta T _ { g r a v _ { J } } .
$$

(b) Geometric delay

In the barycentric frame the vacuum delay equation is, to a sufficient level of approximation:

$$
T _ { 2 } - T _ { 1 } = - \frac { 1 } { c } \hat { K } \cdot ( \vec { X } _ { 2 } ( T _ { 2 } ) - \vec { X } _ { 1 } ( T _ { 1 } ) ) + \Delta T _ { g r a v } .
$$

This equation is converted into a geocentric delay equation using known quantities by performing the relativistic transformations relating the barycentric vectors $\vec { X _ { i } }$ to the corresponding geocentric vectors $\vec { x } _ { i }$ , thus converting Equation (11.8) into an equation in terms of $\vec { x } _ { i }$ . The related transformation between barycentric and geocentric time can be used to derive another equation relating $T _ { 2 } - T _ { 1 }$ and $t _ { 2 } - t _ { 1 }$ , and these two equations can then be solved for the geocentric delay in terms of the geocentric baseline vector $\vec { b }$ . In the rational polynomial form the total geocentric vacuum delay is given by

$$
t _ { v _ { 2 } } - t _ { v _ { 1 } } = \frac { \Delta T _ { g r a v } - \frac { \hat { K } \cdot \vec { b } } { c } \left[ 1 - \frac { ( 1 + \gamma ) U } { c ^ { 2 } } - \frac { | \vec { V } _ { \oplus } | ^ { 2 } } { 2 c ^ { 2 } } - \frac { \vec { V } _ { \oplus } \cdot \vec { w } _ { 2 } } { c ^ { 2 } } \right] - \frac { \vec { V } _ { \oplus } \cdot \vec { b } } { c ^ { 2 } } ( 1 + \hat { K } \cdot \vec { V } _ { \oplus } / 2 c ) } { 1 + \frac { \vec { K } \cdot ( \vec { V } _ { \oplus } + \vec { w } _ { 2 } ) } { c } } .
$$

where the PPN parameter $\gamma$ is equal to $^ { 1 }$ in GRT.

Given this expression for the vacuum delay, the total delay is found to be

$$
t _ { 2 } - t _ { 1 } = t _ { v _ { 2 } } - t _ { v _ { 1 } } + \left( \delta t _ { a t m _ { 2 } } - \delta t _ { a t m _ { 1 } } \right) + \delta t _ { a t m _ { 1 } } \frac { \hat { K } \cdot ( \vec { w } _ { 2 } - \vec { w } _ { 1 } ) } { c } .
$$

For convenience the total delay can be divided into separate geometric and propagation delays. The geometric delay is given by

$$
t _ { g _ { 2 } } - t _ { g _ { 1 } } = t _ { v _ { 2 } } - t _ { v _ { 1 } } + \delta t _ { a t m _ { 1 } } \frac { \hat { K } \cdot ( \vec { w } _ { 2 } - \vec { w _ { 1 } } ) } { c } ,
$$

and the total delay can be found at some later time by adding the propagation delay:

$$
t _ { 2 } - t _ { 1 } = t _ { g _ { 2 } } - t _ { g _ { 1 } } + ( \delta t _ { a t m _ { 2 } } - \delta t _ { a t m _ { 1 } } ) .
$$

The tropospheric propagation delay in Equations (11.11) and (11.12) need not be from the same model. The estimate in Equation (11.12) should be as accurate as possible, while the $\delta t _ { a t m }$ model in Equation (11.11) need only be accurate to about an air mass ( $\sim 1 0$ ns). If Equation (11.10) is used instead, the model should be as accurate as possible. Note that the tropospheric delay is computed in the rest frame of each station and can be directly added to the geocentric delay (Equation (11.11)), at the uncertainty level considered here (see Eubanks, 1991; Treuhaft and Thomas, 1991).

If $\delta \vec { b }$ is the difference between the a priori baseline vector and the true baseline, the true delay may be computed from the $a$ priori delay as follows. If $\delta \vec { b }$ is less than roughly three meters, then it suffices to add $- ( \hat { K } \cdot \delta \vec { b } ) / c$ to the $a$ priori delay. If this is not the case, however, the $a$ priori delay must be modified by adding

$$
\Delta ( t _ { g _ { 2 } } - t _ { g _ { 1 } } ) = - \frac { \frac { \hat { K } \cdot \delta \vec { b } } { c } } { 1 + \frac { \hat { K } \cdot ( \vec { V } _ { \oplus } + \vec { w } _ { 2 } ) } { c } } - \frac { \vec { V } _ { \oplus } \cdot \delta \vec { b } } { c ^ { 2 } } .
$$

(c) Observations close to the Sun

For observations made very close to the Sun, higher order relativistic time delay effects become increasingly important. The largest correction is due to the change in delay caused by the bending of the ray path by the gravitating body described in Richter and Matzner (1983) and Hellings (1986). The change to ${ \Delta T _ { g r a v } }$ is

$$
\delta T _ { g r a v _ { i } } = { \frac { 4 G ^ { 2 } M _ { i } ^ { 2 } } { c ^ { 5 } } } { \frac { { \vec { b } } \cdot ( { \hat { N } } _ { 1 i } + { \hat { K } } ) } { ( \vert { \vec { R } } \vert _ { 1 i } + { \vec { R } } _ { 1 i } \cdot { \hat { K } } ) ^ { 2 } } } ,
$$

which should be added to the ${ \Delta T _ { g r a v } }$ in Equation (11.1).

# (d) Summary

Assuming that the reference time is the UTC arrival time of the VLBI signal at receiver 1, and that it is transformed to the appropriate timescale to be used to compute each element of the geometric model, the following steps are recommended to compute the VLBI time delay.

1. Use Equation (11.6) to estimate the barycentric station vector for receiver 1.

2. Use Equations (11.3) to (11.5) to estimate the vectors from the Sun, the Moon, and each planet except the Earth to receiver 1.

3. Use Equation (11.1) to estimate the differential gravitational delay for each of those bodies.

4. Use Equation (11.2) to find the differential gravitational delay due to the Earth.

5. Sum to find the total differential gravitational delay, Equation (11.7).

6. Compute the vacuum delay from Equation (11.9).

7. Calculate the aberrated source vector for use in the calculation of the tropospheric propagation delay:

$$
\vec { k } _ { i } = \hat { K } + \frac { \vec { V } _ { \oplus } + \vec { w } _ { i } } { c } - \hat { K } \frac { \hat { K } \cdot ( \vec { V } _ { \oplus } + \vec { w } _ { i } ) } { c } .
$$

8. Add the geometric part of the tropospheric propagation delay to the vacuum delay, Equation (11.11).

9. The total delay can be found by adding the best estimate of the tropospheric propagation delay

$$
t _ { 2 } - t _ { 1 } = t _ { g _ { 2 } } - t _ { g _ { 1 } } + [ \delta t _ { a t m _ { 2 } } ( t _ { 1 } - \frac { \hat { K } \cdot \vec { b } } { c } , { \vec { k } } _ { 2 } ) - \delta t _ { a t m _ { 1 } } ( \vec { k } _ { 1 } ) ] .
$$

10. If necessary, apply Equation (11.13) to correct for “post-model” changes in the baseline by adding Equation (11.13) to the total time delay from step $^ { 9 }$ .

# 11.2 Ranging techniques

In a reference system centered on an ensemble of masses, if an electromagnetic signal is emitted from $x _ { 1 }$ at coordinate time $t _ { 1 }$ and is received at $x _ { 2 }$ at coordinate time $t _ { 2 }$ , the coordinate time of propagation is given by

$$
t _ { 2 } - t _ { 1 } = { \frac { | { \vec { x } } _ { 2 } ( t _ { 2 } ) - { \vec { x } } _ { 1 } ( t _ { 1 } ) | } { c } } + \sum _ { J } { \frac { 2 G M _ { J } } { c ^ { 3 } } } \ln \left( { \frac { r _ { J 1 } + r _ { J 2 } + \rho } { r _ { J 1 } + r _ { J 2 } - \rho } } \right) ,
$$

where the sum is carried out over all bodies J with mass $M J$ centered at $x J$ and where $r _ { J 1 } = | \vec { x } _ { 1 } - \vec { x } _ { J } |$ , $r _ { J 2 } = | \vec { x } _ { 2 } - \vec { x } _ { J } |$ and $\rho = | \vec { x } _ { 2 } - \vec { x } _ { 1 } |$ .

For near-Earth satellites (e.g. SLR or GNSS), practical analysis is done in the geocentric frame of reference, and the only body to be considered is the Earth (Ries et al., 1988). For lunar laser ranging (LLR), which is formulated in the solar system barycentric reference frame, the Sun and the Earth must be taken into account, with the contribution of the Moon being of order 1 ps (i.e. about 1 mm for a return trip). Moreover, in the analysis of LLR data, the body-centered coordinates of an Earth station and a lunar reflector should be transformed into barycentric coordinates. The transformation of $\bar { r }$ , a geocentric position vector expressed in the GCRS, to $\vec { r _ { b } }$ , the vector expressed in the BCRS, is provided with an uncertainty below 1 mm by the equation

$$
\vec { r } _ { b } = \vec { r } \left( 1 - \frac { U } { c ^ { 2 } } \right) - \frac { 1 } { 2 } \left( \frac { \vec { V } \cdot \vec { r } } { c ^ { 2 } } \right) \vec { V } ,
$$

where $U$ is the gravitational potential at the geocenter (excluding the Earth’s mass) and $\vec { V }$ is the barycentric velocity of the Earth. A similar equation applies to the selenocentric reflector coordinates.

In general, however, the geocentric and barycentric systems are chosen so that the geocentric space coordinates are TT-compatible (position vector $\vec { r } _ { T T }$ ) and that the barycentric space coordinates are TDB-compatible (position vector $\vec { r } _ { T D B }$ ). The transformation of ${ \vec { r } } _ { T T }$ to $\vec { r } _ { T D B }$ is then given, again with an uncertainty below 1 mm, by

$$
\vec { r } _ { T D B } = \vec { r } _ { T T } \left( 1 - \frac { U } { c ^ { 2 } } - L c \right) - \frac { 1 } { 2 } \left( \frac { \vec { V } \cdot \vec { r } _ { T T } } { c ^ { 2 } } \right) \vec { V } ,
$$

where $L _ { C }$ is given in Table 1.1.

# References

Eubanks, T. M. (ed.), 1991, Proceedings of the U. S. Naval Observatory Workshop on Relativistic Models for Use in Space Geodesy, U. S. Naval Observatory, Washington, D. C.   
Hellings, R. W., 1986, “Relativistic effects in astronomical timing measurements,” Astron. J., 91(3), pp. 650–659, doi: 10.1086/114048. Erratum, ibid., 92(6), p. 1446, doi: 10.1086/114282.   
Klioner, S. A., 1991, “General relativistic model of VLBI observables,” in Proc. AGU Chapman Conf. on Geodetic VLBI: Monitoring Global Change, Carter, W. E. (ed.), NOAA Technical Report NOS 137 NGS 49, American Geophysical Union, Washington D.C, pp. 188–202.   
Klioner, S. A. and Soffel, M. H., 2001, personal communication.   
Kopeikin, S. M., 1990, “Theory of relativity in observational radio astronomy,” Sov. Astron., 34(1), pp. 5–10.   
Kopeikin, S. M. and Sch¨afer, G., 1999, “Lorentz covariant theory of light propagation in gravitational fields of arbitrary-moving bodies,” Phys. Rev. D, 60(12), pp. 124002/1–44, doi: 10.1103/PhysRevD.60.124002.   
McCarthy, D. D. (ed.), 1992, IERS Standards, IERS Technical Note, 13, Observatoire de Paris, Paris, available at http://www.iers.org/TN13   
McCarthy, D. D. (ed.), 1996, IERS Conventions, IERS Technical Note 21, Observatoire de Paris, Paris, available at http://www.iers.org/TN21   
Petit, G., 2000, “Importance of a common framework for the realization of spacetime reference systems,” Proc. “Towards an Integrated Global Geodetic Observing System (IGGOS), IAG Symposia 120”, Rummel, R., Drewes, H., Bosch, W., Hornik, H. (eds.), Springer-Verlag, pp. 3–7.   
Richter, G. W. and Matzner, R. A., 1983, “Second-order contributions to relativistic time delay in the parameterized post-Newtonian formalism,” Phys. Rev. D, 28(12), pp. 3007–3012, doi: 10.1103/PhysRevD.28.3007.   
Ries, J. C., Huang, C., and Watkins, M. M., 1988, “Effect of general relativity on a near-Earth satellite in the geocentric and barycentric reference frames,” Phys. Rev. Lett., 61(8), pp. 903–906, doi: 10.1103/PhysRevLett.61.903.   
Shahid-Saless, B., Hellings, R. W., and Ashby, N., 1991, “A picosecond accuracy relativistic VLBI model via Fermi normal coordinates,” Geophys. Res. Lett., 18(6), pp. 1139–1142, doi: 10.1029/91GL01187.   
Soffel, M. H., M¨uller, J., Wu, X., and Xu, C., 1991, “Consistent relativistic VLBI theory with picosecond accuracy,” Astron. J., 101(6), pp. 2306–2310, doi: 10.1086/115851.   
Sovers, O. J. and Fanselow, J. L., 1987, Observation model and parameter partials for the JPL VLBI parameter estimation software ‘MASTERFIT’-1987, JPL Pub. 83–39, Rev. 3, see http://hdl.handle.net/2060/19880009139.   
Treuhaft R. N. and Thomas J. B., 1991, “Incorporating atmospheric delay into the relativistic VLBI time delay,”JPL Technical Memorandum IOM 335.6– 91–016.   
Zhu, S. Y. and Groten, E., 1988, “Relativistic effects in VLBI time delay measurement,” man. geod., 13(1), pp. 33–39.

# A Recommendations on terminology by the 2003-2006 IAU NFA Working Group (August 2006)

The final recommendations on terminology associated with the IAU 2000/2006 resolutions of the IAU Working Group on “Nomenclature for fundamental astronomy” (NFA) are the following (see Capitaine et al., 2007):

1. Using existing terms (e.g. right ascension) in extended ways for the terminology associated with the new paradigm with a clear specification, rather than introducing new names.

2. Using “equinox based” and “CIO based” for referring to the classical and new paradigms, respectively.

Comment: the “Celestial/Terrestrial Intermediate Origin” with the acronym CIO/TIO is proposed here as the updated terminology to replace the IAU 2000 “Celestial/Terrestrial Ephemeris Origin” with the acronym CEO/TEO (see below items 3 and 4 and the proposed resolution).

3. Using “intermediate” to describe (i) the moving geocentric celestial reference system defined in the IAU 2000 resolutions (i.e. containing the CIP and the CIO), and (ii) the moving terrestrial reference system containing the CIP and the TIO.

Comment the term “intermediate” has been chosen to specify that these systems are intermediary systems between the geocentric celestial reference system and the terrestrial reference system, which are realized by using the models, constants and procedures that are conventionally accepted; it conventionally separates the instantaneous celestial orientation of the Earth into components we label polar motion (in the terrestrial reference system) and precession-nutation (in the celestial reference system).

4. Harmonizing the name of the pole and the origin to “intermediate” and therefore changing CEO/TEO to CIO/TIO.

5. Using “system” in a broad sense rather than “frame” in this context of the intermediary system/frame.

6. Using special designations for particular realizations of the intermediate celestial reference system.

Comment: this applies for example to “the IAU 2000A system” to designate the system which is realized by transforming the geocentric celestial reference system GCRS to the intermediate system using the IAU 2000A precession-nutation and associated frame biases at J2000.0 (the GCRS being transformed from the BCRS by using the coordinate transformation specified in the IAU 2000 Resolution B1.3).

7. Keeping the classical terminology for “true equator and equinox” (or “true equinox based”) for the classical equatorial system.

8. Choosing “equinox right ascension” (or “RA with respect to the equinox”) and “intermediate right ascension” (or “CIO right ascension”, or “RA with respect to the CIO”), for the azimuthal coordinate along the equator in the classical and new paradigms, respectively. (Note that right ascensions and declinations with respect to the ICRS are usually designated by $\alpha _ { I C R S }$ , δICRS).

Comment: this is to be specified only once in the presentation of a paper if there is some risk of misunderstanding. Afterwards, “right ascension” alone is sufficient.

9. Giving the name “equation of the origins” to the distance between the CIO and the equinox along the intermediate equator, the sign of this quantity being such that it represents the CIO right ascension of the equinox, or equivalently, the difference between the Earth Rotation Angle and Greenwich apparent sidereal time.

10. Retaining “apparent places” and “mean places” in the equinox based system.

11. Not introducing “apparent intermediate places” in the CIO based system, but introducing instead “intermediate places”.

12. Using “ITRF zero-meridian” to designate the plane passing through the geocenter, ITRF pole and ITRF x-origin and using, if necessary, “TIO meridian” to designate the moving plane passing through the geocenter, the CIP and the TIO.

13. Fixing the default orientation of the BCRS so that for all practical applications, unless otherwise stated, the BCRS is assumed to be oriented according to the ICRS axes.

Comment: Once the BCRS is spatially oriented according to the ICRS, the spatial GCRS coordinates get an “ICRS-induced” orientation.

14. Re-defining Barycentric Dynamical Time (TDB) as a fixed linear function of TCB:

$$
\mathrm { T D B } = \mathrm { T C B } - \mathrm { L _ { B } } \times ( \mathrm { J D _ { T C B } } - \mathrm { T _ { 0 } } ) \times 8 6 4 0 0 + \mathrm { T D B _ { 0 } } ,
$$

where $\mathrm { T _ { 0 } } = 2 4 4 3 1 4 4 . 5 0 0 3 7 2 5$ ,

and $\operatorname { L } _ { \mathrm { B } } = 1 . 5 5 0 5 1 9 7 6 8 \times 1 0 ^ { - 8 }$ and $\mathrm { T D B } _ { 0 } = - 6 . 5 5 \times 1 0 ^ { - 5 }$ s are defining constants.

Additional points

Considering a terminology associated with other types of apparent places, although it may be required for specific use, has not been considered as being essential for common astronomical use and is therefore not part of the NFA WG terminology recommendations.

- No WG consensus having been reached for having strict rules for using or not using capitals for names for origins, poles and systems, no recommendation on this issue is proposed by the WG. The policy adopted throughout the NFA document is to capitalize those terms that are defined in IAU or IUGG resolutions.

# B IAU Resolutions Adopted at the XXVIth General Assembly (2006)

# B.1 IAU 2006 Resolution B1 on Adoption of the P03 Precession Theory and Definition of the Ecliptic

The XXVIth International Astronomical Union General Assembly, Noting

1. the need for a precession theory consistent with dynamical theory,   
2. that, while the precession portion of the IAU 2000A precession-nutation model, recom-mended for use beginning on 1 January 2003 by resolution B1.6 of the XXIVth IAU General Assembly, is based on improved precession rates with respect to the IAU 1976 precession, it is not consistent with dynamical theory, and   
3. that resolution B1.6 of the XXIVth General Assembly also encourages the development of new expressions for precession consistent with the IAU 2000A precession-nutation model, and

Recognizing

1. that the gravitational attraction of the planets make a significant contribution to the motion of the Earths equator, making the terms lunisolar precession and planetary precession misleading,   
2. the need for a definition of the ecliptic for both astronomical and civil purposes, and   
3. that in the past, the ecliptic has been defined both with respect to an observer situated in inertial space (inertial definition) and an observer comoving with the ecliptic (rotating definition),

# Accepts

the conclusions of the IAU Division I Working Group on Precession and the Ecliptic published in Hilton et al. (2006, Celest. Mech. 94, 351), and

# Recommends

1. that the terms lunisolar precession and planetary precession be replaced by precession of the equator and precession of the ecliptic, respectively,

2. that, beginning on 1 January 2009, the precession component of the IAU 2000A precession-nutation model be replaced by the P03 precession theory, of Capitaine et al. (2003, A&A, 412, 567-586) for the precession of the equator (Eqs. 37) and the precession of the ecliptic (Eqs. 38); the same paper provides the polynomial developments for the P03 primary angles and a number of derived quantities for use in both the equinox based and CIO based paradigms,

3. that the choice of precession parameters be left to the user, and

4. that the ecliptic pole should be explicitly defined by the mean orbital angular momentum vector of the Earth-Moon barycenter in the Barycentric Celestial Reference System (BCRS), and this definition should be explicitly stated to avoid confusion with other, older definitions.

# Notes

1. Formulas for constructing the precession matrix using various parameterizations are given in Eqs. 1, 6, 7, 11, 12 and 22 of Hilton et al. (2006). The recommended polynomial developments for the various parameters are given in Table 1 of the same paper, including the P03 expressions set out in expressions (37) to (41) of Capitaine et al. (2003) and Tables 3-5 of Capitaine et al. (2005).

2. The time rate of change in the dynamical form factor in P03 is $d J _ { 2 } / d t = - 0 . 3 0 0 1 \times 1 0 ^ { - 9 } c e n t u r y ^ { - 1 }$

# B.2 IAU 2006 Resolution B2 on the Supplement to the IAU 2000 Resolutions on reference systems

Recommendation 1. Harmonizing the name of the pole and origin to “intermediate” The XXVIth International Astronomical Union General Assembly, Noting

1. the adoption of resolutions IAU B1.1 through B1.9 by the IAU General Assembly of 2000,

2. that the International Earth Rotation and Reference Systems Service (IERS) and the Standards Of Fundamental Astronomy (SOFA) activity have made available the models, procedures, data and software to implement these resolutions operationally, and that the Almanac Offices have begun to implement them beginning with their 2006 editions, and   
3. the recommendations of the IAU Working Group on “Nomenclature for Fundamental Astronomy” (IAU Transactions XXVIA, 2005), and

# Recognizing

1. that using the designation “intermediate” to refer to both the pole and the origin of the new systems linked to the Celestial Intermediate Pole and the Celestial or Terrestrial Ephemeris origins, defined in Resolutions B1.7 and B1.8, respectively would improve the consistency of the nomenclature, and   
2. that the name “Conventional International Origin” with the potentially conflicting acronym CIO is no longer commonly used to refer to the reference pole for measuring polar motion as it was in the past by the International Latitude Service,

# Recommends

1. that, the designation “intermediate” be used to describe the moving celestial and terrestrial reference systems defined in the 2000 IAU Resolutions and the various related entities, and 2. that the terminology “Celestial Intermediate Origin” (CIO) and “Terrestrial Intermediate Origin” (Terrestrial Intermediate Origin) be used in place of the previously introduced “Celestial Ephemeris Origin” (Celestial Ephemeris Origin) and “Terrestrial Ephemeris Origin” (Terrestrial Ephemeris Origin), and 3. that authors carefully define acronyms used to designate entities of astronomical reference systems to avoid possible confusion.

Recommendation 2. Default orientation of the Barycentric Celestial Reference System (BCRS) and Geocentric   
Celestial Reference System (GCRS)   
The XXVIth International Astronomical Union General Assembly,   
Noting

1. the adoption of resolutions IAU B1.1 through B1.9 by the IAU General Assembly of 2000,

2. that the International Earth Rotation and Reference Systems Service (IERS) and the Standards Of Fundamental Astronomy (SOFA) activity have made available the models, procedures, data and software to implement these resolutions operationally, and that the Almanac Offices have begun to implement them beginning with their 2006 editions,   
3. that, in particular, the systems of space-time coordinates defined by IAU 2000 Resolution B1.3 for (a) the solar system (called the Barycentric Celestial Reference System, BCRS) and (b) the Earth (called the Geocentric Celestial Reference System, GCRS) have begun to come into use,   
4. the recommendations of the IAU Working Group on “Nomenclature for Fundamental Astronomy” (IAU Transactions XXVIA, 2005), and   
5. a recommendation from the IAU Working Group on “Relativity in Celestial Mechanics, Astrometry and Metrology”,

Recognizing

1. that the BCRS definition does not determine the orientation of the spatial coordinates, 2. that the natural choice of orientation for typical applications is that of the ICRS, and 3. that the GCRS is defined such that its spatial coordinates are kinematically non-rotating with respect to those of the BCRS,

Recommends

that the BCRS definition is completed with the following: “For all practical applications, unless otherwise stated, the BCRS is assumed to be oriented according to the ICRS axes. The orientation of the GCRS is derived from the ICRS-oriented BCRS.”

# B.3 IAU 2006 Resolution B3 on the Re-definition of Barycentric Dynamical Time, TDB

The XXVIth International Astronomical Union General Assembly, Noting

1. that IAU Recommendation 5 of Commissions 4, 8 and 31 (1976) introduced, as a replacement for Ephemeris Time (ET), a family of dynamical time scales for barycentric ephemerides and a unique time scale for apparent geocentric ephemerides,   
2. that IAU Resolution 5 of Commissions 4, 19 and 31 (1979) designated these time scales as Barycentric Dynamical Time (TDB) and Terrestrial Dynamical Time (TDT) respectively, the latter subsequently renamed Terrestrial Time (TT), in IAU Resolution A4, 1991,   
3. that the difference between TDB and TDT was stipulated to comprise only periodic terms, and   
4. that Recommendations III and V of IAU Resolution A4 (1991) (i) introduced the coordinate time scale Barycentric Coordinate Time (TCB) to supersede TDB, (ii) recognized that TDB was a linear transformation of TCB, and (iii) acknowledged that, where discontinuity with previous work was deemed to be undesirable, TDB could be used, and

# Recognizing

1. that TCB is the coordinate time scale for use in the Barycentric Celestial Reference System,   
2. the possibility of multiple realizations of TDB as defined currently,   
3. the practical utility of an unambiguously defined coordinate time scale that has a linear relationship with TCB chosen so that at the geocenter the difference between this coordinate time scale and Terrestrial Time (TT) remains small for an extended time span,   
4. the desirability for consistency with the Teph time scales used in the Jet Propulsion Laboratory (JPL) solar-system ephemerides and existing TDB implementations such as that of Fairhead & Bretagnon (A&A 229, 240, 1990), and   
5. the 2006 recommendations of the IAU Working Group on “Nomenclature for Fundamental Astronomy” (IAU Transactions XXVIB, 2006),

Recommends

that, in situations calling for the use of a coordinate time scale that is linearly related to Barycentric Coordinate Time (TCB) and, at the geocenter, remains close to Terrestrial Time (TT) for an extended time span, TDB be defined as the following linear transformation of TCB: $T D B = T C B - L _ { B } \times ( J D _ { T C B } - T _ { 0 } ) \times 8 6 4 0 0 + T D B _ { 0 }$ , where $T _ { 0 } = 2 4 4 3 1 4 4 . 5 0 0 3 7 2 5$ , and $L _ { B } = 1 . 5 5 0 5 1 9 7 6 8 \times 1 0 ^ { - 8 }$ and $T D B _ { 0 } = - 6 . 5 5 \times 1 0 ^ { - 5 }$ s are defining constants.

# Notes

1. $J D _ { T C B }$ is the TCB Julian date. Its value is $T _ { 0 } = 2 4 4 3 1 4 4 . 5 0 0 3 7 2 5$ for the event 1977 January 1 00h $0 0 \mathrm { m } ~ 0 0 \mathrm { s }$ TAI at the geocenter, and it increases by one for each 86400 s of TCB.

2. The fixed value that this definition assigns to $L _ { B }$ is a current estimate of $L _ { C } + L _ { G } - L _ { C } \times L _ { G }$ , where $L _ { G }$ is given in IAU Resolution B1.9 (2000) and $L _ { C }$ has been determined (Irwin & Fukushima, 1999, A&A 348, 642) using the JPL ephemeris DE405. When using the JPL Planetary Ephemeris DE405, the defining $L _ { B }$ value effectively eliminates a linear drift between TDB and TT, evaluated at the geocenter. When realizing TCB using other ephemerides, the difference between TDB and TT, evaluated at the geocenter, may include some linear drift, not expected to exceed 1 ns per year.

3. The difference between TDB and TT, evaluated at the surface of the Earth, remains under 2 ms for several millennia around the present epoch.

4. The independent time argument of the JPL ephemeris DE405, which is called Teph (Standish, A&A, 336, 381, 1998), is for practical purposes the same as TDB defined in this Resolution.

5. The constant term $T D B _ { 0 }$ is chosen to provide reasonable consistency with the widely used $T D B -$ $T T$ formula of Fairhead & Bretagnon (1990). n.b. The presence of $T D B _ { 0 }$ means that TDB is not synchronized with TT, TCG and TCB at 1977 Jan 1.0 TAI at the geocenter.

6. For solar system ephemerides development the use of TCB is encouraged.

# C IUGG Resolution 2 Adopted at the XXIVth General Assembly (2007)

Resolution 2: Geocentric and International Terrestrial Reference Systems (GTRS and ITRS)   
The International Union of Geodesy and Geophysics   
Considering

the increasing importance of geodetic reference systems in geosciences, and more generally in numerous scientific or technical activities, such as satellite navigation systems or geo-information,

Noting

the IUGG Resolution 2 and IAG Resolution 1, both adopted in 1991 at the Vienna General Assembly, defining the Conventional Terrestrial Reference System (CTRS)

Recognizing

the quality of the work done by several IAG services (IERS, IGS, ILRS, IVS, IDS,. . .) to actually realize these systems and provide regular access for numerous users within and beyond the geoscience community,

Endorses

1. the definition of a Geocentric Terrestrial Reference System (GTRS) as system of geocentric spacetime coordinates within the framework of General Relativity, co-rotating with the Earth and related to Geocentric Celestial Reference System by a spatial rotation which takes into account the Earth orientation parameters, in agreement with the 2000 IAU resolution B1.3,   
2. the definition of the International Terrestrial Reference System (ITRS) as the specific GTRS for which the orientation is operationally maintained in continuity with past international agreements (so-called BIH orientation), and

# Adopts

the ITRS as preferred system for any scientific application, and

Urges

other communities such as geo-information, or navigation to do the same.

# D IAU Resolutions Adopted at the XXVIIth General Assembly (2009)

# D.1 IAU 2009 Resolution B2 on IAU 2009 astronomical constants

The XXVII General Assembly of International Astronomical Union, Considering

1. the need for a self-consistent set of accurate numerical standards for use in astronomy,   
2. that improved values of astronomical constants have been derived from recent observations and published in refereed journals, and   
3. that conventional values have been adopted by IAU GA 2000 and IAU GA 2006 resolutions for a number of astronomical quantities,

Recognizing

1. the continuing need for a set of Current Best Estimates (CBEs) of astronomical constants, and   
2. the need for an operational service to the astronomical community to maintain the CBEs

Recommends

1. that the list of previously published constants compiled in the report of the Working Group on Numerical Standards of Fundamental Astronomy (see http://maia.usno.navy.mil/NSFA/CBE.html) be adopted as the IAU (2009) System of Astronomical Constants.   
2. that Current Best Estimates of Astronomical Constants be permanently maintained as an electronic document,   
3. that, in order to ensure the integrity of the CBEs, IAU Division I develop a formal procedure to adopt new values and archive older versions of the CBEs, and   
4. that the IAU establish within IAU Division I a permanent body to maintain the CBEs for fundamental astronomy.

# D.2 IAU 2009 Resolution B3 on the Second Realization of the International Celestial Reference Frame

The XXVII General Assembly of International Astronomical Union, noting

1. that Resolution B2 of the XXIII General Assembly (1997) resolved “That, as from 1 January 1998, the IAU celestial reference system shall be the International Celestial Reference System (ICRS)”,   
2. that Resolution B2 of the XXIII General Assembly (1997) resolved that the “fundamental reference frame shall be the International Celestial Reference Frame (ICRF) constructed by the IAU Working Group on Reference Frames”,   
3. that Resolution B2 of the XXIII General Assembly (1997) resolved that the “That IERS should take appropriate measures, in conjunction with the IAU Working Group on reference frames, to maintain the ICRF and its ties to the reference frames at other wavelengths”,   
4. that Resolution B7 of the XXIII General Assembly (1997) recommended “high-precision astronomical observing programs be organized in such a way that astronomical reference systems can be maintained at the highest possible accuracy for both northern and southern hemispheres”,   
5. that Resolution B1.1 of the XIV General Assembly (2000) recognized “the importance of continuing operational observations made with Very Long Baseline (VLBI) to maintain the ICRF”,

# Recognizing

1. that since the establishment of the ICRF, continued VLBI observations of ICRF sources have more than tripled the number of source observations,   
2. that since the establishment of the iCRF, continued VLBI observations of extragalactic sources have significantly increased the number of sources whose positions are known with a high degree of accuracy,   
3. that since the establishment of the ICRF, improved instrumentation, observation strategies, and application of state-of-the-art astrophysical and geophysical models have significantly improved both the data quality and analysis of the entire relevant astrometric and geodetic VLBI data set,

4. that a working group on the ICRF formed by the International Earth Rotation and Reference Systems Service (IERS) and the International VLBI Service for Geodesy and Astrometry (IVS), in conjunction with the IAU Division I Working Group on the Second Realization of the International Celestial Reference Frame has finalized a prospective second realization of the ICRF in a coordinate frame aligned to that of the ICRF to within the tolerance of the errors in the latter (see note 1),

5. that the prospective second realization of the ICRF as presented by the IAU Working Group on the Second Realization of the International Celestial Reference Frame represents a significant improvement in terms of source selection, coordinate accuracy, and total number of sources, and thus represents a significant improvement in the fundamental reference frame realization of the ICRS beyond the ICRF adopted by the XXIII General Assembly (1997),

# Resolves

1. that from 01 January 2010 the fundamental astrometric realization of the International Celestial Reference System (ICRS) shall be the Second Realization of the International Celestial Reference Frame (ICRF2) as constructed by the IERS/IVS working group on the ICRF in conjunction with the IAU Division I Working Group on the Second Realization of the International Celestial Reference Frame (see note 1),

2. that the organizations responsible for astrometric and geodetic VLBI observing programs (e.g. IERS, IVS) take appropriate measures to continue existing and develop improved VLBI observing and analysis programs to both maintain and improve ICRF2,

3. that the IERS, together with other relevant organizations continue efforts to improve and densify high accuracy reference frames defined at other wavelengths and continue to improve ties between these reference frames and ICRF2.

Note 1: The Second Realization of the International Celestial Reference Frame by Very Long Baseline Interferometry, Presented on behalf of the IERS / IVS Working Group, Alan Fey and David Gordon (eds.). (IERS Technical Note ; 35) Frankfurt am Main: Verlag des Bundesamts f¨ur Kartographie und Geod¨asie, 2009. See www.iers.org/MainDisp.csl?pid=46-25772 $\bot$ or hpiers.obspm.fr/icrs-pc/.

The glossary includes some terms adopted verbatim from the IAU Division I Working Group “Nomenclature for Fundamental Astronomy (NFA)” found at http://syrte.obspm.fr/iauWGnfa/NFA Glossary.html.1 For a complete list of terms see the NFA website. Other terms have been adopted from http://www.iers.org2 and http://www.ngs.noaa.gov/CORS-Proxy/Glossary/xml/NGS Glossary.xml.3 The definition of the term geoid was adopted from the website at http://www.ngs.noaa.gov/GEOID/geoid def.html.4 The definition of the term IAU was adopted from the website at http://www.iau.org.5 The page number listed after each term indicates the first main occurence of that term.

# Glossary

# B

barycenter (barycentre) center of mass of the solar system. [NFA Glossary], p. 21.

Barycentric Celestial Reference System (BCRS) a system of barycentric space-time coordinates for the solar system within the framework of General Relativity with metric tensor specified by the IAU 2000 Resolution B1.3. Formally, the metric tensor of the BCRS does not fix the coordinates completely, leaving the final orientation of the spatial axes undefined. However, according to IAU 2006 Resolution B2, for all practical applications, unless otherwise stated, the BCRS is assumed to be oriented according to the ICRS axes. [NFA Glossary], p. 151.

Barycentric Coordinate Time (TCB) the coordinate time of the BCRS; it is related to Geocentric Coordinate Time (TCG) and Terrestrial Time (TT) by relativistic transformations that include secular terms. [NFA Glossary], p. 16.

Barycentric Dynamical Time (TDB) a time scale originally intended to serve as an independent time argument of barycentric ephemerides and equations of motion. In the IAU 1976 resolutions, the difference between TDB and TDT was stipulated to consist of only periodic terms, a condition that cannot be satisfied rigorously. The IAU 1991 resolutions introducing barycentric coordinate time (TCB) noted that TDB is a linear function of TCB, but without explicitly fixing the rate ratio and zero point, leading to multiple realizations of TDB. In 2006 TDB was re-defined via a linear transformation of the TCB (See IAU 2006 Resolution B3): $T D B = T C B - L _ { B } \times ( J D _ { T C B } - T _ { 0 } ) \times 8 6 4 0 0 + T D B _ { 0 }$ , where $T _ { 0 } = 2 4 4 3 1 4 4 . 5 0 0 3 7 2 5$ , and $L _ { B } =$ $1 . 5 5 0 5 1 9 7 6 8 \times 1 0 ^ { - 8 }$ and $T D B _ { 0 } = - 6 . 5 5 \times 1 0 ^ { - 5 }$ s are defining constants. [NFA Glossary], p. 17.

# C

Celestial Ephemeris Origin (CEO) the original name for the Celestial Intermediate Origin (CIO) given in the IAU 2000 resolutions. [NFA Glossary], p. 44.

Celestial Ephemeris Pole (CEP) used from 1984 to 2003 with the IAU 1980 Theory of Nutation as the reference pole for nutation and polar motion; the axis of figure for the mean surface of a model Earth in which the free motion has zero amplitude. This pole was originally defined as having no nearly-diurnal nutation with respect to a space-fixed or Earth-fixed coordinate system and being realized by the IAU 1980 nutation. It was afterwards determined by using VLBI observations of celestial pole offsets. It is now replaced by the CIP, which is defined by IAU 2000 Resolution B1.7. [NFA Glossary], p. 44.

Celestial Intermediate Origin (CIO) origin for right ascension on the intermediate equator in the Celestial Intermediate Reference System. It is the non-rotating origin in the GCRS that is recommended by the IAU 2000 Resolution B 1.8, where it was designated the Celestial Ephemeris Origin. The name Celestial Intermediate Origin was adopted by IAU 2006 Resolution B2. The CIO was originally set close to the GCRS meridian and throughout 1900-2100 stays within 0.1 arcseconds of this alignment. [NFA Glossary], p. 44.

ermediate Pole (CIP) geocentric equatorial pole defined by IAU 2000 Resolution B1.7 as being the intermediate pole, in the transformation from the GCRS to the ITRS, separating nutation from polar motion. It replaced the CEP on 1 January 2003. Its GCRS position results from (i)

the part of precession-nutation with periods greater than 2 days, and (ii) the retrograde diurnal part of polar motion (including the free core nutation, FCN) and (iii) the frame bias. Its ITRS position results from (i) the part of polar motion which is outside the retrograde diurnal band in the ITRS and (ii) the motion in the ITRS corresponding to nutations with periods less than 2 days. The motion of the CIP is realized by the IAU precession-nutation plus time-dependent corrections provided by the IERS. [NFA Glossary], p. 25.   
Celestial Intermediate Reference System (CIRS) geocentric reference system related to the GCRS by a time-dependent rotation taking into account precession-nutation. It is defined by the intermediate equator (of the CIP) and CIO on a specific date (IAU 2006 Resolution B2). It is similar to the system based on the true equator and equinox of date, but the equatorial origin is at the CIO. Since the acronym for this system is close to another acronym (namely ICRS), it is suggested that wherever possible the complete name is used. [NFA Glossary], p. 47.   
celestial pole offsets time-dependent corrections to the precession-nutation model, determined by observations. The IERS provides the celestial pole offsets in the form of the differences, $d X$ and $d Y$ , of the CIP coordinates in the GCRS with respect to the IAU 2000A precession-nutation model (i.e. the CIP is realized by the IAU 2000A precession-nutation plus these celestial pole offsets). In parallel the IERS also provides the offsets, $\mathrm { d } \psi$ and d, in longitude and obliquity with respect to the IAU 1976/1980 precession/nutation model. [NFA Glossary], p. 25.   
Chandler wobble a free prograde motion of the Earth’s rotational axis with respect to the Earth’s crust moving with a period of approximately 435 days. [2], p. 124.   
Coordinated Universal Time (UTC) a measure of time that conforms, within approximately 1 s, to the mean diurnal motion of the Sun and serves as the basis of all civil timekeeping. The term ‘UT’ is used to designate a member of the family of Universal Time scales (e.g. UTC, UT1). [NFA Glossary], p. 160.

# D

datum (plural datums) A geodetic reference frame. In surveying and geodesy, a datum is a set of reference points on the Earth’s surface, and (often) an associated model of the shape of the Earth (reference ellipsoid) used to define a geographic coordinate system. Horizontal datums are used to describe the location of a point on the Earth’s surface, in latitude and longitude or other appropriate coordinates. Vertical datums are used to describe site elevations or depths. [3], p. 32.   
DORIS DORIS (Doppler Orbitography and Radiopositioning Integrated by Satellite), a dual-frequency Doppler system, is used to determine geodetic positions from analyses of data transmitted from the sites of artificial satellites. Receivers are on board specialized satellites while the transmitters are on the ground. The complete set of observations is downloaded from the satellite to the ground centre for analysis. [2], p. 140.

# E

Earth Rotation Angle (ERA) angle measured along the intermediate equator of the Celestial Intermediate Pole (CIP) between the Terrestrial Intermediate Origin (TIO) and the Celestial Intermediate Origin (CIO), positively in the retrograde direction. It is related to UT1 by a conventionally adopted expression in which ERA is a linear function of UT1 (see IAU 2000 Resolution B1.8). Its time derivative is the Earth’s angular velocity. Previously, it has been referred to as the stellar angle. [NFA Glossary], p. 44.   
ecliptic the plane perpendicular to the mean heliocentric orbital angular momentum vector of the Earth-Moon barycentre in the BCRS (IAU 2006 Resolution B1). In the past, there was no unique interpretation; an ecliptic was defined by means of the angles of the precession theory. [NFA Glossary], p. 22.   
ellipsoid In geodesy, a reference ellipsoid is a mathematically-defined surface that approximates the shape of the Earth or other planetary body. [3], p. 40.   
epoch a fixed date used to reckon time for expressing time varying quantities. It is often expressed in the system of Julian date, marked by the prefix J (e.g. J2000.0), with the Julian year of 365.25 days as unit. The term is also used to designate the date and time of an observation, e.g. “epoch of observation”, which would be better expressed by “date of observation”. [NFA Glossary], p. 22.   
equation of the equinoxes (EE) the right ascension of the mean equinox referred to the true equator and equinox; alternatively the difference between apparent sidereal time and mean sidereal time (GAST−GMST). [NFA Glossary], p. 60.   
equation of the origins (EO) distance between the CIO and the equinox along the intermediate equator; it is the CIO right ascension of the equinox; alternatively the difference between the Earth Rotation Angle and Greenwich apparent sidereal time (ERA−GAST). [NFA Glossary], p. 60.   
equinox either of the two points at which the ecliptic intersects the celestial equator; also the time at which the Sun passes through either of these intersection points; i.e., when the apparent longitude of the Sun is 0deg or 180deg. When required, the equinox can be designated by the ephemeris of the Earth from which it is obtained (e.g. vernal equinox of DE 405). By 2100 the equinox will have moved 1.4deg from the ICRS meridian, due to the precession of the equinoxes. [NFA Glossary], p. 22.

# F

free core nutation (FCN) free mode in the motion of the Earth’s rotation axis with respect to the Earth, due to non-alignment of the rotation axis of the inner core with respect to the mantle; the period is retrograde diurnal in the terrestrial frame and prograde long-period in the celestial frame. [2], p. 57.

fundamental arguments a set of mathematical expressions for angles used to describe orbital parameters of solar system objects used in precession/nutation models. [2], p. 54.

# G

geocenter (geocentre) center of mass of the Earth including the atmosphere and oceans. [NFA Glossary], p. 31.

geocenter motion the motion, on the level of a few mm, of the mass center of the entire Earth system (solid Earth, ocean and atmosphere) relative to the origin of the ITRF. It is opposite in sign from the origin translation vector defined in Chapter 4. [2], p. 38.   
Geocentric Celestial Reference System (GCRS) a system of geocentric space-time coordinates within the framework of General Relativity with metric tensor specified by the IAU 2000 Resolution B1.3. The GCRS is defined such that the transformation between BCRS and GCRS spatial coordinates contains no rotation component, so that GCRS is kinematically non-rotating with respect to BCRS. The equations of motion of, for example, an Earth satellite, with respect to the GCRS will contain relativistic Coriolis forces that come mainly from geodesic precession. The spatial orientation of the GCRS is derived from that of the BCRS, that is (cf. IAU 2006 Resolution B2), unless otherwise stated, by the orientation of the ICRS. [NFA Glossary], p. 151.   
Geocentric Coordinate Time (TCG) coordinate time of the GCRS based on the SI second. It is related to Terrestrial Time (TT) by a conventional linear transformation provided by IAU 2000 Resolution B1.9. [NFA Glossary], p. 16.   
geocentric terrestrial reference system (GTRS) a system of geocentric space-time coordinates within the framework of General Relativity, co-rotating with the Earth, and related to the GCRS by a spatial rotation which takes into account the Earth orientation parameters. It was adopted by IUGG 2007 Resolution 2. It replaces the previously defined Conventional Terrestrial Reference System. [NFA Glossary], p. 34.   
geoid the equipotential surface of the Earth’s gravity field which best fits, in a least squares sense, global mean sea level. [4], p. 18.   
Global Positioning System (GPS) The Global Positioning System (GPS), the U.S. component of the Global Navigation Satellite System (GNSS). The GPS satellites, at an altitude of $2 0 0 0 0 ~ \mathrm { k m }$ , transmit down to the Earth carrier signals at two L-band frequencies (1.227 and 1.575 GHz) which are modulated by a pseudo-random noise code. When four satellites are in view, the user has enough information to solve for the station position and the clock offset from GPS time. [2], p. 135.   
Greenwich Mean Sidereal Time (GMST) Greenwich hour angle of the mean equinox defined by a conventional relationship to Earth Rotation Angle or equivalently to UT1. [NFA Glossary], p. 61.   
Greenwich Sidereal Time (GST) Greenwich apparent sidereal time (GAST), the hour angle of the true equinox from the Terrestrial Intermediate Origin (TIO) meridian (Greenwich or International meridian). [NFA Glossary], p. 47.

# H

# Hipparcos

Acronym for High Precision Parallax Collecting Satellite, a scientific mission of the European Space Agency (ESA), launched in 1989 and operated between 1989 and 1993. It was the first space experiment devoted to astrometry, the accurate measurement of star positions, parallaxes, and proper motions. The Hipparcos Catalogue, a high-precision catalogue of more than 100,000 stars, was published in 1997 and is the primary realization of the ICRS at optical wavelengths (see IAU 2000 Resolution B1.2). [2], p. 21.

# I

International Astronomical Union (IAU) Organization of professional astronomers from 90 countries to promote scientific and educational activities in astronomy. [5], p. 43.

International Atomic Time (TAI) a widely used practical realization of Terrestrial Time (TT) with a fixed shift from the latter due to historical reasons (see TT); it is a continuous time scale, now calculated at the Bureau International des Poids et Mesures (BIPM), using data from some three hundred atomic clocks in over fifty national laboratories in accordance with the definition of the SI second. [NFA Glossary], p. 151.

International Celestial Reference Frame (ICRF) a set of extragalactic objects whose adopted positions and uncertainties realize the ICRS axes and give the uncertainties of the axes. It is also the name of the radio catalog whose 212 defining sources is currently the most accurate realization of the ICRS. Note that the orientation of the ICRF catalog was carried over from earlier IERS radio catalogs and was within the errors of the standard stellar and dynamic frames at the time of adoption. Successive revisions of the ICRF are intended to minimize rotation from its original orientation. Other realizations of the ICRS have specific names (e.g. Hipparcos Celestial Reference Frame). [NFA Glossary], p. 22.

International Celestial Reference System (ICRS) the idealized barycentric coordinate system to which celestial positions are referred. It is kinematically non-rotating with respect to the ensemble of distant extragalactic objects. It has no intrinsic orientation but was aligned close to the mean equator and dynamical equinox of J2000.0 for continuity with previous fundamental reference systems. Its orientation is independent of epoch, ecliptic or equator and is realized by a list of adopted coordinates of extragalactic sources. [NFA Glossary], p. 21.

International Terrestrial Reference Frame (ITRF) a realization of ITRS, through the realization of its origin, orientation axes and scale, and their time evolution. [2], p. 35.

International Terrestrial Reference System (ITRS) according to IUGG 2007 Resolution 2, the ITRS is the specific GTRS for which the orientation is operationally maintained in continuity with past international agreements (BIH orientation). The co-rotation condition is defined as no residual rotation with regard to the Earth’s surface, and the geocenter is understood as the center of mass of the whole Earth system, including oceans and atmosphere (IUGG 1991 Resolution 2). For continuity with previous terrestrial reference systems, the first alignment was close to the mean equator of 1900 and the Greenwich meridian. The ITRS was adopted (IUGG 2007 Resolution 2) as the preferred GTRS for scientific and technical applications and is the recommended system to express positions on the Earth. [NFA Glossary], p. 34.

# J

J2000.0 defined in the framework of General Relativity by IAU 1994 Resolution C7 as being the event (epoch) at the geocenter and at the date 2000 January 1.5 TT = Julian Date 245 1545.0 TT. Note that this event has different dates in different time scales. [NFA Glossary], p. 22.

# L

length of day (LOD) common term for the difference in the duration of a day as measured by UT1 and 86,400 SI seconds. In practice this quantity is determined by differencing daily values of UT1 $-$ UTC. Units are generally given as ms day $^ { - 1 }$ [2], p. 123.   
LLR LLR (Lunar Laser Ranging) is a space geodetic technique that measures the round-trip travel times of light pulses between stations on the Earth and five retroreflectors (ca. 2010) on the surface of the Moon. [2], p. 22.

pole the position on the celestial sphere towards which the Earth’s axis points at a particular epoch, with the oscillations due to precession-nutation removed. [NFA Glossary], p. 21.

modified Julian date (MJD) The Modified Julian Date or Day (MJD) is defined as $M J D = J D - 2 4 0 0 0 0 0 . 5$ , where JD is the Julian Day. Start of the JD count is from 0 at 12 noon 1 January -4712 (4713 BC). [2], p. 151.

# N

non-rotating origin (NRO) in the context of the GCRS or the ITRS, the point on the intermediate equator such that its instantaneous motion with respect to the system (GCRS or ITRS as appropriate) has no component along the intermediate equator (i.e. its instantaneous motion is perpendicular to the intermediate equator). It is called the CIO and TIO in the GCRS and ITRS, respectively. [NFA Glossary], p. 44.

nutation (see precession-nutation), p. 21.

# P

permanent tide time-independent gravitational potential exerted on the Earth by the Sun, Moon, and planets. [3], p. 15.

polar motion the motion of the Earth’s pole with respect to the ITRS. The main components are the Chandlerian free motion with a period of approximately 435 days, and an annual motion. It also includes sub-daily variations caused by ocean tides and periodic motions driven by gravitational torques with periods less than two days. Sub-daily variations are not included in the values distributed by the IERS, and are therefore to be added, after interpolation to the date of interest, using a model provided by the IERS Conventions. [NFA Glossary], p. 124.

precession-nutation the ensemble of effects of external torques on the motion in space of the rotation axis of a freely rotating body, or alternatively, the forced motion of the pole of rotation due to those external torques. In the case of the Earth, a practical definition consistent with the IAU 2000 resolutions is that precession-nutation is the motion of the CIP in the GCRS, including FCN and other corrections to the standard models: precession is the secular part of this motion plus the term of 26000-year period and nutation is that part of the CIP motion not classed as precession. [NFA Glossary], p. 44.

# R

regularized UT1 (UT1R) LOD adjusted to remove the effects of zonal solid Earth tides with periods shorter than 35 days. [2], p. 123.

# S

site displacements time-varying changes in the coordinates of a terrestrial site due to local deformations. [2], p. 113.

SLR

SLR (Satellite Laser Ranging) measures the time intervals required for pulses emitted by a laser transmitter to travel to a satellite and return to the transmitting site. The “range”, or distance between the satellite and the observing site, is approximately equal to one half of the two-way travel time multiplied by the speed of light. [2], p. 132.

# T

$\boldsymbol { \mathsf { T } }$ eph $( T _ { e p h }$ ) independent time argument of JPL ephemerides (Standish, A&A, 336, 381, 1998) that is, for practical purposes, the same as Barycentric Dynamical Time (TDB). TDB is related to Barycentric Coordinate Time (TCB) by $^ { \Gamma } D B = T C B - L _ { B } \times ( J D _ { T C B } - T _ { 0 } ) \times 8 6 4 0 0 + T D B _ { 0 }$ , where $T _ { 0 } = 2 4 4 3 1 4 4 . 5 0 0 3 7 2 5$ , and $L _ { B } = 1 . 5 5 0 5 1 9 7 6 8 { \times } 1 0 ^ { - 8 }$ and $T D B _ { 0 } = - 6 . 5 5 \times 1 0 ^ { - 5 }$ s are defining constants. [IAU 2006 Resolution B3], p. 28.

Terrestrial Dynamical Time (TDT) time scale for apparent geocentric ephemerides defined by a 1979 IAU resolution and in 1991 was replaced by Terrestrial Time (TT). [NFA Glossary], p. 151.

Terrestrial Ephemeris Origin (TEO) the original name for the Terrestrial Intermediate Origin (TIO) given in the IAU 2000 resolutions. [NFA Glossary], p. 44.

Terrestrial Intermediate Origin (TIO) origin of longitude in the Intermediate Terrestrial Reference System. It is the non-rotating origin in the ITRS that is recommended by the IAU 2000 Resolution B1.8, where it was designated Terrestrial Ephemeris Origin. The name Terrestrial Intermediate Origin was adopted by IAU 2006 Resolution B2. The TIO was originally set at the ITRF origin of longitude and throughout 1900-2100 stays within 0.1 mas of the ITRF zero meridian. [NFA Glossary], p. 44.

Terrestrial Intermediate Reference System (TIRS) a geocentric reference system defined by the intermediate equator of the CIP and the TIO (IAU 2006 Resolution B2). It is related to the ITRS by polar motion and s’ (TIO locator). It is related to the Celestial Intermediate Reference System by a rotation of ERA around the CIP, which defines the common $\mathbf { Z }$ -axis of the two systems. Since the acronym for this system is close to another acronym (namely ITRS), it is suggested that wherever possible the complete name be used. [NFA Glossary], p. 47.

terrestrial reference frame (TRF) realization of the Terrestrial Reference System (TRS), through the realization of its origin, orientation axes and scale, and their time evolution. [2], p. 32.

terrestrial reference system (TRS) a Terrestrial Reference System (TRS) is a spatial reference system corotating with the Earth in its diurnal motion in space. [2], p. 32.

Terrestrial Time (TT) a coordinate time whose mean rate is close to the mean rate of the proper time of an observer located on the rotating geoid. At 1977 January 1.0 TAI exactly, the value of TT was 1977 January 1.0003725 exactly. It is related to the Geocentric Coordinate Time (TCG) by a conventional linear transformation provided by IAU 2000 Resolution B1.9. TT may be used as the independent time argument for geocentric ephemerides. An accurate realization of TT is $T T ( T A I ) = \mathrm { T A I } + 3 2 . 1 8 4$ seconds. In the past TT was called Terrestrial Dynamical Time (TDT). [NFA Glossary], p. 151.

# U

angle of the Earth’s rotation about the CIP axis defined by its conventional linear relation to the Earth Rotation Angle (ERA). It is related to Greenwich apparent sidereal time through the ERA (see equation of the origins). It is determined by observations (currently from VLBI observations of the diurnal motions of distant radio sources). UT1 can be regarded as a time determined by the rotation of the Earth. It can be obtained from the uniform time scale UTC by using the quantity UT1 $-$ UTC, which is provided by the IERS. [NFA Glossary], p. 123.

UTC difference between the UT1 parameter derived from observation and the uniform time scale UTC, the latter being currently defined as: UTC = TAI + n, where n is an integer number of seconds, such that $| U T 1 - U T C | < 0 . 9$ seconds. [NFA Glossary], p. 25.

#

# VLBI

VLBI (Very Long Baseline Interferometry) is a space geodetic technique that measures the time differences in the arrival of microwave signals from extragalactic radio sources received at two or more widely separated radio observatories. [2], p. 21.

# Z

zonal tides tides that produce zonal (constant along a circle of latitude) deformations. [3], p. 123.