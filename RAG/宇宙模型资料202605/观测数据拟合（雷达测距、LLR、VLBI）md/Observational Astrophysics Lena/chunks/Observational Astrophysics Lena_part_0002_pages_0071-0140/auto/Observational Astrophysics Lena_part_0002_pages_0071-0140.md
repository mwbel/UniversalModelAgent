is around $76 \%$ at this wavelength, that is, $\tau ( 2 . 6 \mathrm { m m } ) = 0 . 2 7$ . The atmospheric Dtransmission therefore corresponds to an antenna temperature (see Sect. 7.5) of $0 . 2 7 { \times } 2 7 3 = 7 5 \mathrm { K }$ , or to a spectral flux of 10 Jy $( 1 \mathrm { J y } = 1 0 ^ { - 2 6 } \mathrm { W } \mathrm { m } ^ { - 2 } \mathrm { H z } ^ { - 1 } )$ ), whereas  Dthe astronomical source under study may be much less intense, by three or four orders of magnitude.

To distinguish the source from the sky background in each of these cases, an offsetting or on–off technique is used, which involves pointing the telescope successively at the source and then at a neighbouring part of the sky, supposed to be free of sources. A neighbourhood of several minutes of arc is adequate, and the hypothesis that atmospheric emission remains spatially uniform over such a region seems to be borne out. Taking the difference between the two measurements, the signal of the source alone can be reconstituted (subtraction of sky background). However, new techniques in spectroscopy, using fibre optics (see Sect. 8.3), detect light, very locally, over several hundred pixels spread across a field of several minutes of arc. Subtraction of the sky background can then reveal spatial fluctuation residues, representing an additional spatial noise. We shall discuss this in more detail in Chap. 9 (see Sect. 9.4), which deals with the precautions needed to carry out this type of observation.

A second effect creates difficulties for this method. Atmospheric emission generally fluctuates in time (movement of invisible clouds of water vapour, variable excitation of fluorescence during the night, ionospheric winds, and so on), and the frequencies are rather high $\cdot f \sim 0 . 1 \mathrm { - } 1 0 \mathrm { H z } )$ . The differential measurement thus compares two emissions which differ randomly, and the result of the subtraction will be affected by a random noise, referred to as sky noise.

This noise is weaker as the modulation between the two fields increases. To use this fact, the secondary mirror of a Cassegrain or Coude telescope (see Chap.´ 5) is given a sinusoidal, or better, a square-wave vibration which displaces the source image on the diaphragm determining the field (sky chopping). Meanwhile the thermal emission produced by the telescope itself, which also crosses the field diaphragm and reaches the detector, is kept absolutely constant. Radiotelescopes are generally too large, and so have too great an inertia, to allow this rapid modulation $\mathbf { \Sigma } ( > \mathrm { ~ l ~ H z } )$ ) of the pointing or of the secondary mirror. It is thus usual to obtain modulation by applying the on–off technique to the whole instrument, although naturally this is less fast.

To be more precise, the beam is displaced on the primary mirror during modulation by the secondary mirror, since the field diaphragm is generally chosen to be the secondary mirror itself. Any variation, even minimal, in the temperature or emissivity of the primary mirror then produces a further modulation, called the offset signal. These signals which cause very significant perturbation, are discussed in Chap. 9. It is this effect which renders infrared and millimetre measurements so difficult, and which disappears whenever it is possible, in space, to cool the telescope itself.

The principle of differential modulation has been described here in the context of dealing with atmospheric background emission, but it applies equally well in any situation where the problem is one of distinguishing a weak and spatially restricted source from a more or less uniform and bright background. Thus the detection of infrared galactic sources requires elimination of the zodiacal background (see Sect. 2.9.2). The same is true in the search for fluctuations in the diffuse cosmological background, which are of the order of $1 0 ^ { 6 }$ times less than the mean radiative background and require, this time in the submillimetre range, a subtraction of galactic interstellar emission. Figure 2.10 shows the grain of this galactic background quantitatively, by its spatial power spectrum.

![](images/93121cb3f1d72671e213aac63de549dcdbf8e96ac402ecbbd1f937fefa4f591f.jpg)  
Fig. 2.10 Power spectrum of sky brightness as observed from an orbit around the Earth, in the direction of the North Galactic Pole, at $\lambda = 1 0 0 \mu \mathrm { m }$ . Continuous Dcurve : low frequency part sampled by the satellite IRAS (1983) with resolution 2 arcmin. Dotted curve : high frequency part deduced from CCD measurements in the visible. (After Low F.J., Cutri R.M., Infrared Phys. 35, 29, 1994)

# 2.4 Scattering of Radiation

Atmospheric scattering is caused by the molecules which make up the air and by aerosols suspended in it. The vertical distribution of the former is directly related to density and thus decreases with altitude, whilst that of the latter is more capricious, depending on winds, climate, type of ground, volcanic activity, industrial pollution, and many other factors. The scattering of light by the brighter celestial bodies — the Sun and the Moon — gives rise in the daytime to the blue colour of the sky, and at night, to a veiling of faint astronomical sources. In the same way as atmospheric emission, scattering makes it difficult to discriminate faint sources. The highly chromatic nature of scattering only disturbs observation in the visible and very near infrared, for the day and night alike.

The molecular scattering in the visible and near infrared is Rayleigh scattering. The cross-section for Rayleigh scattering, integrated over all directions, is given by

$$
\sigma _ { \mathrm { R } } ( \lambda ) = \frac { 8 \pi ^ { 3 } } { 3 } \frac { ( n ^ { 2 } - 1 ) ^ { 2 } } { N ^ { 2 } \lambda ^ { 4 } } ,
$$

where $n$ is the refractive index and $N$ the number of molecules per unit volume. The refractive index of air at $\lambda = 0 . 5 \mu \mathrm { m }$ can be approximated by Gladstone’s law, which gives

$$
n - 1 \simeq 8 0 \times 1 0 ^ { - 6 } \frac { P [ \mathrm { m b } ] } { T [ \mathrm { K } ] } .
$$

Rayleigh scattering is not isotropic and $\sigma _ { \mathrm { R } } = \sigma _ { \mathrm { R } } ( \theta , \lambda )$ is a function of the angle $\theta$ Dbetween the directions of the incident and scattered radiation [see Astrophysical Quantities, 3rd edn., Athlone, London 1973 (AQ), Chap. 5]. For an incident intensity $I$ , the intensity $j$ scattered into solid angle ${ \mathrm { d } } \omega$ is given by

$$
j = \sigma _ { \mathrm { R } } \frac { 3 } { 4 } ( 1 + \cos ^ { 2 } \theta ) \frac { \mathrm { d } \omega } { 4 \pi } I .
$$

Even in the absence of any aerosols, the sky brightness due to Rayleigh scattering cannot be neglected. At an altitude of $2 0 0 0 \mathrm { m }$ , at an angular distance $\theta \ : = \ : 9 0 ^ { \circ }$ from the Sun, and at the wavelength of red light $\lambda \ : = \ : 7 0 0 \mathrm { n m }$ D, the ratio of sky brightness to that of the Sun’s disk is about $1 0 ^ { - 7 }$ .

Aerosol scattering is governed by a different law, because the scattering particles are bigger than molecules.

The total effective cross-section of a sphere of radius $a$ is given by Mie’s theory as

$$
\sigma = \pi a ^ { 2 } ( Q _ { \mathrm { s c a t t e r i n g } } + Q _ { \mathrm { a b s o r p t i o n } } ) .
$$

The general theory of scattering by small particles can be found in the classic text by van de Hulst H.C., Light Scattering by Small Particles (Wiley, New York, 1957). Some useful results are also included in AF, Sect. 1.41.

If $a \gg \lambda$ ; $Q _ { \mathrm { s } } = Q _ { \mathrm { a } } = 1$ , the scattered power is equal to the absorbed power, D Dand the effective cross-section is twice the geometrical cross-section. If $a > \lambda$ , $Q \mathrm { { s } }$ and $Q \mathrm { { a } }$ have a complicated $\lambda$ -dependence, but for dielectric spheres (water droplets or dust grains such as silicates), the relation $Q _ { \mathrm { s } } \ \propto \ \lambda ^ { - 1 }$ holds, i.e., the scattered intensity varies as $\lambda ^ { - 1 }$ .

The above description of the scattering of sunlight applies equally to the scattering of moonlight, whence infrared observation from Earth-based observatories is favoured on nights close to the full Moon. The scattering of urban lighting is also a problem (see Sect. 2.8).

# Daylight Observations from the Ground

The thermal emission of the atmosphere grows exponentially (Wien part of the Planck curve) as the wavelength increases from the visible to the near infrared. Indeed, there is a wavelength beyond which this emission exceeds daytime scattering emissions, and hence in this range the brightness of the sky is largely independent of the day–night cycle. This is shown in Fig. 2.11. For telescopes with absolute pointing (i.e., to an accuracy of several seconds of arc, and without reference star), observations become feasible during the day. This could significantly increase the time available for use at large ground-based optical telescopes. Unfortunately, there are problems associated with the thermal control of instruments which limit this possibility. Of course, in the millimetre range, round-the-clock observation has become commonplace.

![](images/e2276b0ce0a8c211e5fe00e8b7debf7d19ecab688de790f2a519d63a8a90e912.jpg)  
Fig. 2.11 Contributions to the sky brightness in the visible and near infrared. Molecular scattering is given for the altitude $z = 2 0 0 0 \mathrm { m }$ , at $9 0 ^ { \circ }$ from the Sun. The wavelength dependence is $\lambda ^ { - 4 }$ , Dand does not include correction for variation of refractive index $n ( \lambda )$ with $\lambda$ . Thermal emission is also shown, assuming uniform mean emissivity of 0.1, the exact value depending in particular on the quantity of precipitable water. The intersection of the two curves shows, in the absence of aerosols, the wavelength beyond which observation can be carried out during the night or the day regardless. The dashed line shows the possible additional contribution due to aerosols, varying as $\lambda ^ { - 1 }$ , which moves the above wavelength threshold to the right. For comparison, $( \bullet )$ marks the sky brightness measured at 0.5 arcmin from the Sun’s limb at an astronomical site (Kitt Peak National Observatory, Arizona. Source P. Lena, unpublished)´

# Solar Eclipses

Visible emissions from the solar corona immediately above the Sun’s limb $( 1 . 0 3 R _ { \odot }$ from the centre of the disk, or 30 arcsec from the limb) are around $1 0 ^ { 6 }$ ˇtimes less bright than the photospheric emission. The coronal emission is thus greater than the Rayleigh scattered intensity, but generally less than the light scattered by aerosols (solar aureole), which is generally quite considerable for scattering angles very close to zero (see Fig. 2.11).

Even from a high altitude site, observation of the white corona (continuous or ˇ $K$ corona) is therefore very difficult, except during an eclipse of the Sun (see Fig. 2.12), for the intensity lies between $1 0 ^ { - 6 }$ and $1 0 ^ { - 9 }$ times that of the photosphere, and within just 1 $R _ { \odot }$ of the Sun’s limb. On the other hand, for wavelengths at which chromospheric $\mathrm { H } \alpha$ line) or coronal (Fe XIV line at $\lambda = 5 3 0 . 3 \mathrm { n m } )$ emission is significant and quasi-monochromatic, atmospheric scattering can Dbe practically eliminated by using a narrow filter. A ground-based coronagraph (see Sect. 6.6), fitted with a filter, eliminates part of the instrumental and atmospheric scattering, which have values around $1 0 ^ { - 5 }$ times the photospheric emission for a good site. This allows observation of the monochromatic corona out of eclipse. In space, only instrumental scattering remains and it is easier to observe the corona. Photospheric emission at $\mathrm { X }$ -ray wavelengths is negligible, and the X-ray corona can therefore be observed from space without the use of a coronagraph. Eclipses, although romantic events in the life of an astronomer, have had their importance diminished by space observation.

![](images/159bf1391a62c57c13454405342dcb4010ecc803c402d5f6a82d6759dbbf13e7.jpg)  
Fig. 2.12 The eclipse observation which confirmed general relativity. This photograph was obtained by the British astronomer Arthur Eddington during the total solar eclipse of 29 May 1919. By comparing the relative position of stars close to the solar limb with their positions on a photograph taken several months before, the deflection of light while grazing the Sun was measured and shown to be in agreement with the prediction made by Einstein on the basis of the curvature of space due to the Sun’s gravitational field. Picture from the original article Dyson F.W., Eddington A.S., Davidson C., A determination of the deflection of light by the Sun’s gravitational field, from observations made at the total eclipse of May 29, 1919, Phil. Trans. R. Soc. Lond. A 220, 291–333, 1920

# 2.5 Atmospheric Refraction and Dispersion

The refractive index of air $n ( \lambda )$ depends on the vacuum wavelength $\lambda _ { 0 }$ . In dry air, between 0.2 and $4 \mu \mathrm { m }$ , the following expression holds at pressure $P = 1$ atm and temperature $T = 1 5 ^ { \circ } \mathrm { C }$ :

$$
[ n ( \lambda ) - 1 ] \times 1 0 ^ { 6 } = 6 4 . 3 2 8 + \frac { 2 9 4 9 8 . 1 } { 1 4 6 - 1 / \lambda _ { 0 } ^ { 2 } } + \frac { 2 5 5 . 4 } { 4 1 - 1 / \lambda _ { 0 } ^ { 2 } } ,
$$

where $\lambda _ { 0 }$ is measured in $\mu \mathrm { m }$ .

At radiofrequencies (centimetre and beyond), refraction is hardly chromatic at all. Atmospheric refraction is manifested by a flattening of the solar disk at the horizon. Its dispersive character produces the green flash phenomenon at sunrise and sunset, and also the sometimes coloured appearance of stellar scintillation. More important for observation is the fact that the zenith distance $\theta ^ { \prime }$ of a star is deviated from its true value $\theta$ . Refraction is a function of the thickness of air traversed, thus, for an atmosphere stratified in parallel planes, it is also a function of the quantity $m \ = \ 1 / \cos \theta$ , called the air mass. This effect is weak, but not negligible: $\theta ^ { \prime } - \theta \sim - 2 ^ { \prime \prime }$ between 0.3 and $0 . 8 \mu \mathrm { m }$ , for $\theta = 4 5 ^ { \circ }$ . In addition, there    Dis chromatic dispersion, whence the coloured spreading in images of stars observed far from the zenith. These effects of differential refraction and dispersion cannot be ignored when angular resolution is significantly greater than 1 arcsec, which is the case in high resolution imaging, and more specifically in adaptive optics (see Sect. 6.3) and optical interferometry (see Sect. 6.4). A compensating optical device (an atmospheric dispersion corrector) must then be used.

The analogous effects of ionospheric refraction and dispersion are observed at radiofrequencies, since the refractive index of the ionospheric plasma is highly chromatic (see Sect. 2.2).

# 2.6 Turbulence Structure of the Earth Atmosphere

A static and homogeneous description of the atmosphere is clearly inadequate. It is a fundamentally variable medium, whose fluctuations have wide-ranging effects on astronomical observation, but cannot be described by a single model of those fluctuations. Its spatial fluctuations have wavelengths ranging from several thousand kilometres (depressions and anticyclones) down to millimetres (viscous dissipation); and likewise, its temporal fluctuations have time scales ranging from the secular, for certain climatic changes, to the millisecond, for image deformations.

In addition, these spatial and temporal variations are clearly not stationary. Largescale spatial fluctuations $( \gg 1 \mathrm { k m } )$ ) can lead to systematic effects, for example, errors in position determinations in astrometry resulting from corrections for atmospheric refraction (see Chap. 4). The present discussion will be limited to a description of effects on a small spatial scale $( \lesssim 1 \mathrm { k m } )$ , and a small time scale $( \lesssim 1 \mathrm { s } )$ , these being typical scales at which atmospheric turbulence phenomena can directly affect astronomical observation.

The stationarity assumption, often inescapable in any reasonably simple statistical treatment, does not generally correspond to the reality in the context of observation. It is nevertheless possible, under this assumption, to derive a statistical description of atmospheric fluctuations, and to determine the various moments (mean, standard deviation) of those quantities which influence the propagation of electromagnetic waves. This will be dealt with in detail in Sect. 6.2, in the context of image formation.

# 2.6.1 Turbulence in the Lower and Middle Atmosphere

The layers under consideration here are the troposphere $( z \lesssim 1 2 \mathrm { k m } )$ and possibly the lower regions of the stratosphere $( 1 2 ~ \lesssim ~ z ~ \lesssim ~ 2 0 \mathrm { k m } )$ . We study here the way turbulence develops in these layers in the presence of winds, giving a rather simplified model, but one which satisfies our requirements.

# A Simple Model of Turbulence

Turbulence develops in a fluid when the Reynolds number, a dimensionless quantity characterising the flow, exceeds a critical value. This number is defined as

$$
\mathrm { R e } = { \frac { V L } { \nu } } ,
$$

where $V$ is the flow velocity, $\nu$ the kinematic viscosity of the fluid, and $L$ a characteristic length (e.g., diameter of the pipe in which the flow takes place, or width of an obstacle normal to the flow).

In air, $\nu = 1 . 5 \times 1 0 ^ { - 5 } \mathrm { m } ^ { 2 } \mathrm { s } ^ { - 1 }$ . Taking $L \ = \ 1 5 \mathrm { m }$ and $V = 1 \mathrm { m s ^ { - 1 } }$ , we obtain $\mathrm { R e } = 1 0 ^ { 6 }$ D  D, and this is far greater than the critical value $\begin{array} { l l l } { \mathrm { R e } } & { \approx } & { 2 0 0 0 } \end{array}$ which D corresponds to the transition from laminar to turbulent flow. For such high values of Re, turbulence is highly developed; the kinetic energy of large scale movements $( \sim L )$ is gradually transferred to smaller scales of movement, with isotropisation, down to a scale $l$ at which the energy is dissipated by viscous friction. The local velocity of a turbulent fluid is a random variable $V ( \boldsymbol { r } , t )$ (see Appendix B), depending on the point $r$ and the time $t$ . At any instant $t ~ = ~ t _ { 0 }$ , $V ( r , t _ { 0 } )$ can be decomposed into spatial harmonics of the wave vector $\kappa$ D, giving a further random variable $\vartheta ( \kappa )$ :

$$
V ( \boldsymbol { r } ) = \iiint \vartheta ( \boldsymbol { \kappa } ) \mathrm { e } ^ { 2 \mathrm { i } \pi \boldsymbol { \kappa } \cdot \boldsymbol { r } } \mathrm { d } \boldsymbol { \kappa } .
$$

The mean kinetic energy (in the sense of an ensemble average) $\mathrm { d } E ( \kappa )$ in the interval between $\kappa$ and $\kappa + \mathrm { d } \kappa$ , where $\kappa = | \kappa |$ , is proportional to $\langle | \vartheta ( \pmb { \kappa } ) | ^ { 2 } \rangle$ , which is the Cpower spectrum of the velocity $V ( r )$ j j hj j i. Straightforward dimensional analysis leads to the formula

$$
V \propto ( \varepsilon _ { 0 } R ) ^ { 1 / 3 }
$$

for the fluid velocity, where $\varepsilon _ { 0 }$ is the rate of production (or dissipation) of turbulent energy, and $R$ the scale under consideration . $R = 1 / \kappa$ /. We thus obtain

$$
\mathrm { d } E ( \kappa ) \propto \kappa ^ { - 2 / 3 } \mathrm { d } \kappa .
$$

The dimensional argument mentioned above is based upon the following observation: at scales $R$ which are large compared with the scale at which viscous dissipation takes place, the turbulent velocity $V$ should be independent of viscosity. Indeed, it should depend only on the energy production rate " $\mathrm { : \ [ J \ s ^ { - 1 } k g ^ { - 1 } ] }$ , the scale $R$ , and the mass density $\rho$ of the fluid. The only combination of these quantities having the dimensions of a velocity is the one given above. See Landau L., Lifschitz E., Fluid Mechanics (Pergamon, Oxford).

By integration, we obtain the spectrum of the kinetic energy, known as the onedimensional Kolmogorov spectrum,6

$$
E ( \kappa ) d \propto \kappa ^ { - 5 / 3 } ,
$$

provided $\kappa$ is in the so-called inertial range

$$
L _ { 0 } ^ { - 1 } \lesssim \kappa \lesssim l _ { 0 } ^ { - 1 } ,
$$

where $l _ { 0 }$ and $L _ { 0 }$ are called the internal and the external scale of the turbulence, respectively. The assumed ergodicity (see Appendix B) of fully developed turbulence allows us to identify the ensemble and time averages

$$
\big \langle | \vartheta ( \kappa ) | ^ { 2 } \big \rangle = \big \langle | \vartheta ( \kappa , t ) | ^ { 2 } \big \rangle _ { t } .
$$

Turbulence described by a $\kappa ^ { - 5 / 3 }$ one-dimensional power spectrum is said to be homogeneous. Outside the inertial range, the spectrum is governed by generation and dissipation processes. Near ground level, the value of the external scale $L _ { 0 }$ varies between several metres and several hundred metres.

When turbulence occurs in a layer with a temperature gradient differing from the adiabatic one, it mixes air of different temperatures at the same altitude, and hence produces temperature fluctuations.

It can be shown that the equations governing velocity and temperature fluctuations are analogous, and that the one-dimensional spatial spectral density of the temperature fluctuations is

$$
\begin{array} { r } { \Phi _ { \theta } ( \kappa ) \propto \kappa ^ { - 5 / 3 } , } \end{array}
$$

where

$$
\phi _ { \theta } ( \kappa ) = 4 \pi \kappa ^ { 2 } \left| \iiint \Theta ( \boldsymbol { r } ) \mathrm { e } ^ { - 2 \mathrm { i } \pi r \cdot \kappa } \mathrm { d } \boldsymbol { r } \right| ^ { 2 } ,
$$

and $\Theta ( r )$ is the temperature fluctuation about the mean $\langle T ( r ) \rangle$

$$
\Theta ( r ) = T ( r ) - \langle T ( r ) \rangle .
$$

More generally, Obukhov A.M. (Izv. Nauk. SSSR. Ser. Geograf. Geofiz. 13, 58, 1949) has shown that the concentration of an impurity which is passive (i.e., does not affect the dynamics of

![](images/84feb3ab6824fef29261a08d08c1df87b45dcb9495f518baa9995fad309764e5.jpg)  
Fig. 2.13 One-dimensional power spectrum $E ( \kappa )$ of the velocity fluctuations in a turbulent fluid, where the turbulence is isotropic and fully developed between the two scales $L _ { 0 }$ and $l _ { 0 }$ (turbulence obeying Kolmogorov’s law in this interval). The corresponding wave numbers are $\kappa _ { \mathrm { m } } = 1 / L _ { 0 }$ and $\kappa _ { \mathrm { M } } = 1 / l _ { 0 }$ . DThe ordinate is $\log E ( \kappa )$ . A variation in intensity of the turbulence (or of the energy injected at the scale $L _ { 0 }$ ) results in a vertical shift of the curve

the fluid) and additive (i.e., does not react chemically) is also governed by the Kolmogorov law.

The spectral density of the temperature fluctuations also has low and high frequency cutoffs, just like the energy spectrum (Fig. 2.13).

It thus follows that the three-dimensional spectrum is

$$
\begin{array} { r } { \phi _ { \mathrm { T } } ( \pmb { \kappa } ) \propto \kappa ^ { - 1 1 / 3 } . } \end{array}
$$

The covariance of the temperature fluctuations is defined by

$$
B _ { \mathrm { T } } ( \pmb { \rho } ) = \langle \theta ( \pmb { r } ) \Theta ( \pmb { r } + \pmb { \rho } ) \rangle ,
$$

where $\langle \quad \rangle$ denotes a mean over the space variable $r$ . $B _ { \mathrm { T } } ( \pmb { \rho } )$ is the Fourier transform of $\varPhi _ { \mathrm { T } } ( \kappa )$ i(Wiener’s theorem, see Appendix B):

$$
B _ { \mathrm { T } } ( \rho ) = \iiint \phi _ { \mathrm { T } } ( \kappa ) \mathrm { e } ^ { - 2 \mathrm { i } \pi \kappa \cdot \rho } \mathrm { d } \kappa .
$$

This integral diverges if $\boldsymbol { \varPhi } _ { \mathrm { T } } ( \boldsymbol { \kappa } )$ follows the power law down to zero, but remains finite with the cutoff at $\kappa _ { \mathrm { m } } = 1 / L _ { 0 }$ .

DThe structure function of the random variable $\Theta ( r )$ is defined as

$$
D _ { \mathrm { T } } ( \pmb { \rho } ) = \langle | \Theta ( \pmb { r } + \pmb { \rho } ) - \Theta ( \pmb { r } ) | ^ { 2 } \rangle ,
$$

and remains defined for all values of $\pmb { \rho }$ , which indeed motivates the definition. It can then be shown, once again by dimensional considerations, that

$$
D _ { \mathrm { T } } ( \ b \rho ) = C _ { \mathrm { T } } ^ { 2 } \rho ^ { 2 / 3 } ,
$$

![](images/cc900e8f91efbf061b70b9d6c72dd2d22b0a50be0031bd4b562ac38bdbe6e02a.jpg)  
Fig. 2.14 Schematic representation of the generation of turbulence in the atmosphere by different obstacles. The amplitude of the temperature fluctuations depends on the amplitude of the turbulence and on the deviation of the actual temperature gradient from the adiabatic gradient. The scales $L _ { 1 }$ , $L _ { 2 }$ , $L _ { 3 }$ are characteristic of the external scales of turbulence caused by wind around the obstacles 1, 2, and 3. Clearly, the choice of an astronomical observation site must take into account the prevailing winds and the relief upwind, as whirlwinds and eddies in turbulence damp down very slowly

and the three-dimensional temperature fluctuation spectrum is

$$
\phi _ { \mathrm { T } } ( \kappa ) = { \frac { \displaystyle { \cal T } ( 8 / 3 ) \sin ( \pi / 3 ) } { \displaystyle 4 \pi ^ { 2 } } } C _ { \mathrm { T } } ^ { 2 } \kappa ^ { - 1 1 / 3 } = 0 . 0 3 3 C _ { \mathrm { T } } ^ { 2 } \kappa ^ { - 1 1 / 3 } .
$$

$C _ { \mathrm { T } } ^ { 2 }$ is called the structure constant of the temperature fluctuations for homogeneous turbulence. The numerical value of $C _ { \mathrm { T } } ^ { 2 }$ characterises the intensity of the turbulence.

Turbulence in the atmosphere can be generated on different scales. Near ground level, the planetary boundary layer has thickness of the order one kilometre, and turbulence is produced by the flow of winds over surface (orographic) irregularities (see Fig. 2.14). Figure 2.15 shows a measurement of the vertical structure of turbulence in the first twenty kilometres above ground level. The structure constant $C _ { \mathrm { T } } ^ { 2 } ( z )$ is determined locally by measuring the correlation in scintillation of the two components of a double star, using a technique called SCIDAR (SCIntillation Detection And Ranging).

The external scale $L _ { 0 }$ is still not very well known. It varies enormously with the site and the conditions of excitation of the turbulence (wind), and its values range from several metres to several hundred, or thousand, metres. A good knowledge of $L _ { 0 }$ is particularly important for optical interferometry (see Sect. 6.2.3), determining as it does the amplitude of the differential phase perturbation (piston effect) between two widely separated pupils.

At any altitude, the shearing motions of winds can produce a turbulent interface between layers in laminar flow. In the tropopause, this mechanism can lead to large values of $C _ { \mathrm { T } } ^ { 2 }$ , because of the high velocity $( 1 0 0 { - } 2 0 0 \mathrm { k m h ^ { - 1 } } .$ ) of the winds associated with the general circulation of the atmosphere (the jet stream). In addition, this general circulation can interact with large surface features (mountains) and cause gravity waves, which are likely to break in the non-linear regime of turbulent flow.

![](images/1486d469e6cc998826a7178ed59b80ba37b3f941b53f7baec03b88487cfaeb2e.jpg)  
Fig. 2.15 Optical sounding of atmospheric turbulence. The ordinate gives the altitude and the abscissa the time (total duration of measurement was $4 5 \mathrm { { m i n } }$ ). The level of intensity gives the value of $C _ { \mathrm { T } } ^ { 2 } ( z , t )$ . The vertical resolution is $\pm 8 0 0 \mathrm { m }$ , and the time resolution $2 0 \mathrm { s }$ . Three turbulent layers ˙can be seen: the planetary boundary layer near ground level, a layer at $4 . 8 \mathrm { k m }$ , and the layer at the tropopause $( 1 0 { - } 1 1 \mathrm { k m } )$ . The sudden time variations show the intermittent nature of the turbulence. (Measurements carried out at the Observatoire de Haute-Provence, 1981, by Azouit M., Vernin J., J. Atm. Sci. 37, 1550)

The criterion for the onset of turbulence caused by wind shear is given by the Richardson number

$$
\mathrm { R i } = \frac { g } { T } \frac { \partial T / \partial z } { ( \partial V / \partial z ) ^ { 2 } } ,
$$

where $V ( z )$ is the wind velocity at altitude z. When $\mathrm { R i } < 0 . 2 5$ , the flow generally becomes turbulent.7 This is a commonly occurring situation in the generation of terrestrial turbulence, when there is density and/or temperature stratification.

Strictly speaking, the quantity which should appear in the above expression is $T _ { \mathrm { P } }$ , the potential temperature, and not $T$ . The potential temperature is the temperature that a volume element of dry air would have if it were transformed adiabatically to a pressure of 1 bar.

It is thus possible, from a set of vertical soundings of the atmosphere (sounding balloons), to establish the distribution $C _ { \mathrm { T } } ^ { 2 } ( z )$ . The structure function $D _ { \mathrm { T } } ( \pmb { \rho } )$ of temperature variations is measured at various altitudes using rapidly-responding thermal probes with spatial separation $\pmb { \rho }$ . This distribution can also be measured from the ground using optical methods (Fig. 2.15), or indirectly from its effect on astronomical images, by determining the Fried parameter $r _ { 0 }$ and its time development (see Sect. 6.2).

Knowledge of local turbulence is an essential parameter in the choice of an observing site.

# Temperature Fluctuations and the Refractive Index of Air

Fluctuations in temperature and the concentration of $_ { \mathrm { H } _ { 2 } \mathrm { O } }$ cause fluctuations in the refractive index of air. This can be written

$$
n = n _ { 0 } ( T , C _ { \mathrm { H } _ { 2 } \mathrm { O } } ) + \mathrm { i } k ( C _ { \mathrm { H } _ { 2 } \mathrm { O } } ) ,
$$

where the imaginary part $k$ corresponds to absorption by $_ { \mathrm { H } _ { 2 } \mathrm { O } }$ and is important in the infrared and millimetre regions. (The concentrations of other constituents are ignored, their mixing ratios varying only by small amounts locally.) Fluctuations $\Delta n = n _ { 0 } - \left. n _ { 0 } \right.$ of the real part can be written

$$
\Delta n = \frac { \partial n _ { 0 } } { \partial T } \Theta + \frac { \partial n _ { 0 } } { \partial C } c .
$$

For low values of the concentration $C _ { \mathrm { H } _ { 2 } \mathrm { O } }$ , such as characterise astronomical sites, we obtain

$$
\langle \Delta n ^ { 2 } \rangle = \left( \frac { \partial n _ { 0 } } { \partial T } \right) ^ { 2 } \langle \Theta ^ { 2 } \rangle .
$$

As the fluctuations are isobaric, Gladstone’s relation gives

$$
\frac { \partial n _ { 0 } } { \partial T } = \frac { 8 0 \times 1 0 ^ { - 6 } } { T ^ { 2 } } P ,
$$

for $P$ in millibars (1 millibar $[ \mathrm { m } \mathbf { b } ] = 1 0 0$ pascal [Pa]) and $T$ in kelvin [K]. The Dstructure function for the refractive index can be written

$$
D _ { n } ( \pmb { \rho } ) = C _ { n } ^ { 2 } \rho ^ { 2 / 3 } ,
$$

with a structure constant $C _ { n }$ related to $C _ { \mathrm { T } }$ by

$$
C _ { n } = \frac { 8 0 \times 1 0 ^ { - 6 } P \left[ \mathrm { { m b } } \right] } { T ^ { 2 } \left[ \mathrm { { K } } \right] } C _ { \mathrm { { T } } } .
$$

Any fluctuation in the concentration of the absorber will lead to fluctuation in the imaginary part of the refractive index, and hence to fluctuation in the thermal absorption and emission of the volume element under consideration (sky noise, see Sects. 2.3.3 and 9.4).

As a first approximation, when studying the propagation of a wave, it is sufficient to know the integral of fluctuations along the line of sight. Hence the atmospheric turbulence of a given layer is characterised by the product $C _ { \mathrm { T } } ^ { 2 } \Delta h$ for the temperature, or $C _ { n } ^ { 2 } \Delta h$ for the refractive index, where $\Delta h$ is the thickness of that layer. Table 2.4 gives some typical values of the latter product, which is the only relevant parameter in image formation (see Sect. 6.2), for thin layers (several hundred metres) situated at various altitudes.

Table 2.4 Typical intensities of atmospheric turbulence   

<table><tr><td>Altitude of layer [km]</td><td>3</td><td>6</td><td>10</td></tr><tr><td>C△h [cm1/3]</td><td>4×10-13</td><td>13×10-13</td><td>7×10-13</td></tr></table>

![](images/1842081f6d7790a27c8e9a353949c1f251ba7763706acde7b15ae983f6051400.jpg)  
Fig. 2.16 Motion of a ‘frozen’ phase screen. The sequence of pictures shows the time development of the cross-correlation function (contours) of the phase of the wave emitted by a star (quasipoint source), reaching the circular pupil of a telescope (diameter $D = 3 . 6  { \mathrm { m } }$ ) after crossing the Datmosphere. The cross-correlation is calculated between time 0 and successive instants at intervals of $4 0 \mathrm { m s }$ (see Appendix B). The uniform displacement of the cross-correlation peak can be clearly seen, pushed across by the wind, whose speed and direction can then be determined $( 1 4 \mathrm { m } \mathrm { s } ^ { - 1 } )$ . $3 . 6 \mathrm { m }$ ESO telescope, La Silla, Chile. (Gendron E., 1994)

# Time Dependence of Turbulence

At a given point $r$ , the temperature is a random function $T ( \boldsymbol { r } , t )$ of time. In the stationary case, it becomes possible to define a temporal power spectrum, characterising the time frequency content of the phenomenon (see Appendix B).

A simple model is made by considering the turbulence as ‘frozen’ (the Taylor hypothesis), with the above spatial power spectrum $E ( \kappa )$ , and assuming that a uniform wind is translating the air mass with velocity $V$ (see Fig. 2.16). The temporal spectrum is then found by letting

$$
\rho = V \kappa .
$$

The temporal cutoff frequency is thus $f _ { \mathrm { c } } = V / l _ { 0 }$ , which gives, for $l _ { 0 } = 1 0 \mathrm { m m }$ and $V = 1 0 \mathrm { m s ^ { - 1 } }$ , the value $f _ { \mathrm { c } } = 1 0 ^ { 3 } \mathrm { H z }$ D D. Indeed, this value is in good agreement with D Dthe order of magnitude of the highest frequencies observed in image deformation.

At a given site, the turbulence occurring in the various atmospheric layers, if indeed there are several, is generally a superposition of ‘frozen’ turbulence and of a turbulence which is more local, in the sense that it does not result from translation by a horizontal wind, but rather from vertical convection, for example near the tube or the dome of the telescope (boiling).

The physical origin of the Taylor hypothesis is simple: the time scales involved in development of turbulence are much longer than the time taken for a turbulent volume element, displaced by wind, to pass across the aperture of a telescope. It is therefore more correct to speak of a ‘frozen phase screen’, for a short time scale, than of ‘frozen turbulence’.

# 2.6.2 Ionospheric Turbulence

In the weakly ionised plasma which makes up the ionosphere, the electron density $N _ { \mathrm { e } }$ fluctuates. The expression for the refractive index $n ( \nu )$ is

$$
n ( \nu ) = \left( 1 - \frac { \nu _ { \mathrm { p } } ^ { 2 } } { \nu ^ { 2 } } \right) ^ { 1 / 2 } .
$$

Observation reveals that the relative electron density fluctuations are small.8 It is found that

$$
\langle \Delta N _ { \mathrm { e } } ^ { 2 } \rangle ^ { 1 / 2 } \simeq 1 0 ^ { - 3 } \langle N _ { \mathrm { e } } \rangle .
$$

The correlation function for the refractive index is well represented by a Gaussian distribution

$$
\frac { \langle n ( \rho ) n ( \pmb { r } + \pmb { \rho } ) \rangle } { \langle n ( \pmb { \rho } ) ^ { 2 } \rangle } \approx \exp \left[ - \frac { r ^ { 2 } } { 2 a ^ { 2 } ( \nu ) } \right] ,
$$

where $a ( \nu )$ is a typical correlation length. For $N _ { \mathrm { e } } = 1 0 ^ { 5 } \mathrm { c m } ^ { - 3 }$ $( \nu _ { \mathrm { p } } = 4 5 \mathrm { M H z } )$ ), it is found that $a$ takes values between 0.1 and $1 \mathrm { k m }$ D D. The power spectrum, which is the Fourier transform of the autocorrelation function, is then also Gaussian.

# 2.7 The Atmosphere as Radiation Converter

# 2.7.1 Ground-Based Gamma-Ray Astronomy

The detection of photons with energies of several hundred GeV takes us into the regime of very high energy $\gamma$ ray astronomy. Here an atmospheric emission that is at first sight undesirable is used to detect the $\gamma$ radiation from sources of astronomical interest. The atmosphere can be considered here as a huge, indirect detector (in fact, an electromagnetic calorimeter) of $\gamma$ radiation. The following could thus have been discussed in Chap. 7.

When high-energy $\gamma$ rays of astronomical origins enter the atmosphere, they produce $\mathrm { e ^ { + } e ^ { - } }$ which emit other high-energy photons as they slow down. These photons in turn produce other pairs and the process repeats itself. In the upper atmosphere, the particles involved in these cascade reactions are relativistic, and in fact move faster than the speed of light for this medium, whence they emit Cherenkov radiation (see Sect. 7.6). This very short emission of blue light, lasting only a few nanoseconds, can be detected. The signal is nevertheless very weak and must be focused by very big mirrors to be recorded by photomultiplier tubes placed in their focal plane. Observation conditions are the same as for observatories in the visible region, i.e., the sky must be very clear and without light pollution. The short duration of the Cherenkov signal is used to eliminate photon noise due to night sky emission, whence the main source of noise is in fact from cosmic radiation. Indeed, high-energy cosmic charged particles produce air showers, analogous to those initiated by $\gamma$ -rays photons. Only a careful analysis of events can distinguish one effect from the other.

# 2.7.2 Air Showers and Cosmic Rays

When a proton or charged heavy nucleus of cosmic origin reaches the Earth, it will collide with a nucleus in the upper atmosphere, thereby producing a large number of secondary particles. The latter, which share the energy of the incident particle, will in turn collide with other atmospheric nuclei, creating an even greater number of high-energy particles. This process is repeated right down to ground level, where billions of particles of many different kinds are observed, covering an area of several tens of square kilometers. The first ground-based or balloonborne cosmic ray observatories sought high altitudes in order to be closer to the primary source of the shower (the French cosmic ray laboratory which operated between 1940 and 1950 was situated at $3 8 4 2 \mathrm { m }$ on the Aiguille du Midi in the Mont Blanc massif, France). We shall examine the many uses of this phenomenon in Chap. 7.

# 2.8 Terrestrial Observing Sites

The high cost of a modern observatory makes it essential, for ground-based observation, to choose the best possible site, whatever logistic difficulties it may involve. It is quite probable that there are very few exceptional sites, taking into account the criteria mentioned in the following, which refer, firstly, to the visible, infrared and millimetre ranges, and then to radio waves (centimetre and above). 9

# 2.8.1 Visible, Infrared, and Millimetre Observations

The visible and infrared wavelength range is $\lambda ~ \lesssim ~ 3 0 \mu \mathrm { m }$ , while the millimetre wavelength range is $\lambda \gtrsim 0 . 5 \mathrm { m m }$ . Criteria common to the choice of these sites are: absence of cloud, photometric quality, infrared and millimetre transparency, and image quality.

# Cloud Cover

Tropical and desert regions are clearly the best with regard to satisfying this criterion. In such regions, diurnal convection, caused by large increases in surface temperature, can lead to cloud formation, especially around mountain peaks. The most favourable situation is one in which temperature inversion occurs (Fig. 2.17), stabilising those layers closest to ground level and preventing the cloud layer from rising above the inversion layer. Such a configuration exists at the volcanic peaks of Teide and La Palma (Canary Islands), and Mauna Kea (Hawaii), and also along the coastal mountain ranges of Chile and Namibia. Satellite surveys of the Earth provide information accurate to resolutions of around ten metres (Spot satellites).

![](images/130d9d614cf47767721edf9bf72104c40826da5fc71aba3b986959e7f6c4aa68.jpg)  
Fig. 2.17 Inversion layer above the Pacific Ocean, near the island of Hawaii (latitude $3 0 ^ { \circ } \mathrm { N }$ ). This is a subsidence inversion, caused by reheating of cold, descending air layers; the latter movement is itself caused by the general circulation of the atmosphere observed in Hadley cells. (Sounding balloon measurements, kindly communicated by P. Bely and the Hilo Weather Bureau, Hawaii, USA)

Regions with the least cloud are located in two bands on either side of the equator $1 0 ^ { \circ }$ to $3 5 ^ { \circ } \mathrm { N }$ and $0 { - } 1 0 ^ { \circ } \mathrm { S }$ to $3 5 \mathrm { - } 4 0 ^ { \circ } \mathrm { S }$ ), but fluctuate over different longitudes.10

# Photometric Quality

The photometric quality of a site refers to the stability of atmospheric transparency in the visible. The necessary photometric quality is considered to be reached in the visible when there are six consecutive hours of clear sky, for this allows sufficient time to apply extinction corrections (see Sect. 2.2).

Fluctuations in transmission are then of the order of $2 \%$ , or about 0.02 magnitudes. The above criterion is inadequate for infrared observation, affected by the passage of invisible clouds of water vapour, which mean that considerable fluctuations in IR transmission can coexist with an apparently clear sky.

# Infrared and Millimetre Transparency

It was shown above that atmospheric absorption, thermal emission, and the spatial and temporal fluctuation (grain and sky noise, respectively) of the latter are all harmful phenomena caused by the presence of water vapour. For this reason, the choice of a site requires minimisation of the height of precipitable water, a criterion which once again favours polar sites and dry tropical sites, with seasonally anticyclonic weather conditions, and high altitude sites, given that the scale height of water is of the order of 2 to $3 \mathrm { k m }$ in the lower troposphere (Table 2.5). For example, the site Cerro Chajnantor, in the Andes at the frontier between Chile, Argentina, and Bolivia, was chosen at the end of the 1990s to set up the Atacama Large Millimeter Array (ALMA) (see Sect. 6.5.1).

Table 2.5 Column of precipitable water at various sites. Values of $h$ are mean values and may be subject to large seasonal variations. (After Chandrasekar T., Sahu K.C., Desai J.N., Infrared Phys. 23, 119, 1983)   

<table><tr><td>Site</td><td>Country</td><td>Altitude [m]</td><td>Mean column of precipitable water [mm]</td></tr><tr><td>South Pole</td><td>Antarctic</td><td>3000</td><td>&lt;1.0 (summer)</td></tr><tr><td>Jungfraujoch</td><td>Switzerland</td><td>3 570</td><td>2.8</td></tr><tr><td>Kardung La</td><td>India</td><td>5200</td><td>1.5</td></tr><tr><td>KittPeak</td><td>Arizona</td><td>2130</td><td>7.1</td></tr><tr><td>La Silla</td><td>Chile</td><td>2440</td><td>3.9</td></tr><tr><td>Mauna Kea</td><td>Hawaii</td><td>4200</td><td>2.2</td></tr><tr><td>Mount Lemmon</td><td>Arizona</td><td>2600</td><td>4.9</td></tr><tr><td>Mount Palomar</td><td>California</td><td>1706</td><td>6.0</td></tr><tr><td>Cerro Paranal</td><td>Chile</td><td>2660</td><td>2.3</td></tr><tr><td>Chajnantor</td><td>Chile</td><td>5100</td><td>&lt;0.5</td></tr><tr><td>Tenerife</td><td>Canaries</td><td>3600</td><td>3.8</td></tr><tr><td>Zelenchuskaya</td><td>Caucasus</td><td>2070</td><td>5.7</td></tr></table>

# Image Quality

Variations in temperature, and hence in the refractive index of the air, perturb the phase of electromagnetic wavefronts (see Sect. 6.2). This in turn affects the quality of images and measurements at visible and millimetre wavelengths.

To first order, these effects on astronomical images are characterised by several parameters:

The integral of the turbulence along the line of sight

$$
\begin{array} { l } { { \displaystyle \int _ { z _ { 0 } } ^ { \infty } C _ { \mathrm { T } } ^ { 2 } ( z ) \mathrm { d } z \simeq \sum _ { i } C _ { \mathrm { T } _ { i } } ^ { 2 } \Delta h _ { i } , } } \end{array}
$$

where the summation is over $i$ distinct turbulent layers of thickness $\Delta h _ { i }$ .

The evolution time of the turbulence, which is directly related to wind speed $V _ { i }$ in the various layers. The external scale $L _ { i }$ of the turbulence in each of the layers.

A more careful analysis of the effects of turbulence on images shows that the same turbulence but occurring at different altitudes will have different effects on an image.

In addition, turbulence is clearly not stationary over the periods of time considered (days, months, or even years), and so the histogram of its intensity over time must also be taken into consideration. Thus a site of average quality which benefits from periods of exceptional quality, such as the Pic du Midi in the French Pyrenees, may be preferred to a site with more uniform quality.

Local effects due to surface irregularities, as shown in Fig. 2.14, are often the dominant ones in the generation of turbulence, and so general rules cannot be given. Each potential astronomical site must undergo an in-depth study.

# 2.8.2 Centimetre and Metre Wave Radioastronomy

Radiofrequency interference is the main cause of perturbation in this range, and its avoidance has guided the choice of sites such as the Nanc¸ay centimetre telescope (France), the Very Large Array (VLA) in New Mexico (USA), and the Giant Meterwave Radio Telescope (GMRT) in Pune (India).

Other criteria enter into the choice of a good site: the latitude, with a view to covering as much as possible of the two celestial hemispheres; the horizontal surface area available for setting up interferometers (the Very Large Array occupies an area about $3 5 \mathrm { k m }$ in diameter); and the accessibility. This last criterion will no doubt become less and less relevant, given the possibility of remote control of observatories and transmission of their observational data. Completely automated space observatories have clearly demonstrated the feasibility of this procedure, which will be a characteristic feature of observatories in the twenty-first century.

# 2.8.3 Very High Energy Gamma-Ray Astronomy

The detection of very weak blue Cherenkov radiation from the upper atmosphere imposes the same conditions as for observatories observing in the visible and near infrared: clear skies, almost total absence of precipitation, and absence of light pollution. To satisfy these conditions, combined with the need to view the galactic center which can only be seen from the Southern Hemisphere, the site for the four 12 metre mirrors of the High Energy Stereoscopic System (HESS) was chosen in Namibia at the beginning of the 2000s (see Sect. 7.6).

# 2.8.4 Very High Energy Cosmic Radiation

The optimal altitude for direct detection of the particles producing extensive air showers, themselves created by very high energy cosmic rays, lies between 1 000 and $1 5 0 0 \mathrm { m }$ . Sites must be flat over several thousand square kilometers so that radio links between detectors are not blocked by orographic features. In addition, the detection of near ultraviolet radiation $( \approx 3 0 0 \mathrm { n m } )$ ) produced by fluorescence of atmospheric nitrogen, itself excited by passing particles, involves similar constraints to those affecting observatories in the visible region of the spectrum.

The international Pierre Auger observatory,11 located in the flat deserts of the Pampa Amarilla in the west of Argentina, uses two detection techniques: observation of Cherenkov radiation produced locally in $1 6 0 0$ water tanks, and observation of fluorescence from atmospheric nitrogen.

# 2.8.5 Man-Made Pollution and Interference

Human activity generates many difficulties for the running of a modern observatory, with its extremely sensitive detectors. To name but a few: light pollution in the visible, radiofrequency interference, heat sources such as nuclear power stations, which modify microclimates, vibrations, industrial aerosols, and the risks of an overexploitation of space in the vicinity of the Earth.

Light pollution results mainly from scattering of light from street lighting, by atmospheric aerosols and molecules.

The following empirical expression can be used to estimate light pollution:

$$
\log I = 3 - 2 . 5 \log R + \log P ,
$$

where $P$ is the population of a town in units of $1 0 ^ { 5 }$ inhabitants, $R$ is the distance in kilometres, and $I$ is the ratio of artificial intensity to natural intensity (see Sect. 2.3.1) at a zenith distance of $4 5 ^ { \circ }$ . A town of $1 0 0 0 0 0$ inhabitants at $4 0 \mathrm { k m }$ thereby increases the brightness of the night sky by $10 \%$ . For a source of luminosity $L$ lumens at a distance $R$ , the expression becomes

$$
\log { I } = - 4 . 7 - 2 . 5 \log { R } + \log { L } .
$$

Aeroplanes also perturb photographic plates with their light signals, as do artificial satellites with scattering of sunlight. Such objects often turn up on astronomical images!

These preoccupations are clearly analysed in Cayrel R. et al. (eds.), Guidelines for Minimizing Urban Sky Glow near Astronomical Observatories, IAU, 1980; in Rapport sur la protection des observatoires astronomiques et g´eophysiques, Academie des Sciences, Paris, 1984; and also in ´ publications of the International Dark Sky Association, NOAO, Tucson, Arizona.

Radiofrequency pollution comes from various sources: fixed or mobile emitters, radiotelephones, radars, high voltage transmission lines, industrial ovens, and many others. Specific spectral bands essential for radioastronomy are protected as part of the general problem of allocating frequencies, and the International Astronomical Union has established a threshold of $2 \times 1 0 ^ { - 6 } \mathrm { W } \mathrm { m } ^ { - 2 }$ as the maximum tolerable level.

The question of man-made vibrations has become relevant with the advent of optical interferometry and the detection of gravitational waves, which both require a high degree of stability for the instruments, of the order of $1 0 \mathrm { n m \ r m s }$ or better. Up until now, tests carried out in good sites have always shown that natural microseismicity dominates over distant perturbations. It will nevertheless be essential to regulate nearby sources, in particular road traffic.

The control of aerosols and, more generally, the rejection of industrial effluents into the atmosphere is a general preoccupation in environmental protection. However, industrial activity and, in particular, mining, which may develop near to astronomical sites, has to be watched with great care.

For a while it was feared that commercial exploitation of space might lead to a proliferation of low orbit light sources (advertising, lighting of ground areas by large scale solar mirrors), and also of radio-reflecting screens, and stations producing energy transported by microwave beams. All these possibilities would represent a threat to Earth-based astronomical observation, but regulation, monitored by the International Astronomical Union (UAI), has been introduced to control this.

# 2.8.6 The Antarctic

The ice cap covering the Antarctic continent offers possibilities for astronomy which have hardly been investigated yet. The plateau, at a mean altitude of

$3 0 0 0 \mathrm { m }$ and reaching a maximum height of $5 1 4 0 \mathrm { m }$ , includes a wide range of different sites which are already equipped for intensive geophysical study under international collaboration (the South Pole, and nearby peaks on which bases have been established: Dome A, Dome C).

The temperature is very low on this plateau, the tropopause lying practically tangent to ground level. The atmosphere is extremely dry, with a quantity of precipitable water which can be less than $0 . 1 \mathrm { m m }$ . Transmission in the infrared, submillimetre, and millimetre regions is certainly higher than anywhere else on the Earth’s surface, and the emissivity correspondingly weak, both factors which contribute to increasing sensitivity of observation. It is likely that turbulence is much reduced by the absence of both low altitude convection and the high altitude jet stream, the atmosphere being stratified with a weak vertical temperature gradient. This fact also implies vastly improved image quality. Indeed, the systematic analyses12 of image quality, now carried out both in summer and winter alike, have shown that there is a weakly turbulent layer confined to within roughly $3 0 \mathrm { m }$ of the surface (Fig. 2.18).

Furthermore, astronomical objects are observable at zenith distances which remain constant over long periods of time. This is invaluable for making uninterrupted time sequences, when studying solar or stellar oscillations, determining stellar oscillation periods, or observing temporal micro-variations, with sensitivity greater than one thousandth of a magnitude.

Antarctic sites manifest some similarities with space or Moon-based sites, providing a transition from more conventional terrestrial sites. The establishment of permanent, high capacity astronomical observatories seems a likely possibility during the twenty-first century, bearing in mind that some instruments (e.g., a $1 . 7 \mathrm { m }$ millimetre antenna) are already operating at the South Pole, set up by the United States in 1995, while many projects are under assessment for the French–Italian Concordia Station at Dome C, under the impetus of the International Polar Year (2007–2008).

# 2.9 Observation from Space

Space travel, from its beginnings in 1959, has revolutionised astronomical observation. The equipment put into orbit, usually unmanned, has shown a steady increase in both size and complexity, and its lifetime in orbit around the Sun, the Earth, or other planets has also increased, reaching more than a decade in the case of the Voyager probes and the satellite IUE (International Ultraviolet Explorer).

In the present book we have chosen to leave aside the possibilities of in situ observations and measurements in the Solar System, exemplified in the many exploratory missions to the planets and their satellites. These missions would require a whole book for themselves, as already stressed in Chap. 1. We shall thus restrict the discussion here to space observatories designed to observe the remote universe. A space observatory is not fundamentally different in principle from an observatory on the surface of the Earth. It contains telescopes, spectrographs, detectors, data processing equipment, and so on, the principles of which are dealt with in the following chapters. It is almost invariably unmanned, and therefore does not require any human intervention beyond remote control, although possibly in one of its more advanced forms, such as artificial intelligence or techniques involving virtual reality.

![](images/d8895f45820d8baed48948582eca2d6a7a73d4100dd91879ab56a9e7e52c4a33.jpg)  
Fig. 2.18 Image quality at Dome C on the Antarctic plateau. The average size of a stellar image (seeing due to turbulence) is measured at different times of the year and at three different altitudes above the ground ( $3 . 5 \mathrm { m }$ , $8 . 5 \mathrm { m }$ , and $2 0 \mathrm { m }$ ), with an instrument called a differential image motion monitor (DIMM), used in site survey campaigns. These average values do not show the daily variability, which may occasionally reveal an exceptional seeing. From Aristidi, E., Fossat, E., Agabi, A., Mekarnia, D., Jeanneaux, F. ´ , Bondoux, E., Challita, Z., Ziad, A., Vernin, J., Trinquet, H., Dome C site testing, Astron. Astrophys. 499, 955 (2009)

It is clearly not possible to cover all the details of space technology in this book. It is a fascinating subject, which includes many different aspects: the launchers, which determine the orbits and the mass of equipment; the energy supply, which determines manoeuverability and data transmission capacity; the various protection systems, which fend off particles, micrometeorites, and the like, and the cryogenic systems which guarantee whatever lifetime is required for the mission; and the quality control and reliability studies, which test the system as a whole. Some of these points are discussed briefly in the following chapters, in particular in Sect. 9.2, which deals with models for space observatories.

Traditionally, observations from atmospheric platforms, such as aircraft $( 1 0 -$ $2 0 \mathrm { k m }$ ), stratospheric balloons $( 2 0 { - } 4 0 \mathrm { k m } )$ , and rockets (up to $3 0 0 \mathrm { k m }$ ), have been included under the denomination of space observation. Figure 2.4 shows the spectral ranges relevant to each of these platforms.

# 2.9.1 The Advantages of Observation from Space

The discussion earlier in this chapter has exposed three main causes of perturbation for astronomical observation: absorption of radiation, turbulence, and interfering emissions. The first of these considerably restricts access to the electromagnetic spectrum; the second affects image quality (resolution); and the third has a double effect, creating a uniform background from which faint sources must be extracted, but also, through spatial fluctuations (grain) and temporal fluctuations (sky noise), introducing a source of noise which reduces the sensitivity of observations.

Although atmospheric absorption practically disappears when an observatory is placed in low orbit $( z > 5 0 0 \mathrm { k m }$ ), some interference remains. Indeed, the transition is continuous between the upper atmosphere, the solar wind, with which it reacts (the magnetosphere), and the zodiacal dust cloud, which scatters the light from the Sun and emits its own thermal radiation. Moreover, the flux of particles coming from the Sun or diffusing through the Galaxy (cosmic rays) can interfere with detectors on board a space observatory, or even the materials they are made from. In the same way as the atmospheric signal, albeit invaluable for the study of the atmosphere, perturbs observation from the Earth, so the astronomical signals of nearby sources (the zodiacal nebula, the Sun, or even the Galaxy) are invaluable for the study of those sources, but perturb the observation of more distant and often fainter objects.

Some of these effects can be overcome by suitable choice of orbit; the problems caused by particles trapped in the terrestrial magnetosphere are to a large extent avoided by using low equatorial orbits (below $5 0 0 \mathrm { k m } )$ or very distant orbits $6 0 0 0 0 \mathrm { k m }$ and beyond). Other effects, such as zodiacal emission, are unavoidable as long as the orbit of the observatory is close to the Earth.

# 2.9.2 Sources of Perturbation

Although the conditions of observation from space are free from all those perturbing atmospheric phenomena which have been examined in this chapter, other perturbations come into play when an observatory has been put into space. These will be examined in the present section.

# The Zodiacal Nebula

This is a distribution of dust grains in orbit around the Sun, in the neighbourhood of a plane of symmetry very close to the ecliptic (inclination ${ \sim } 3 ^ { \circ }$ ). The thermal emission from this zodiacal cloud is considerable, because of the temperature of the dust grains, heated by the Sun ${ \sim } 3 0 0 \mathrm { K }$ at 1 AU). The spatial distribution of the dust grains, and also the distribution of their sizes, has been determined by studying the way they scatter sunlight (see Fig. 2.19).

The number of grains with radius between $a$ and- $a + \mathrm { d } a$ , at a distance $r$ from the Sun (measured in astronomical units), and at ecliptic latitude $\beta$ C, is given by

$$
n ( r , \beta , a ) = N _ { 0 } ( a ) \frac { a ^ { - k } } { r \left[ \mathrm { A U } \right] } \exp ( - 2 . 6 | \sin \beta | ^ { 1 . 3 } ) ,
$$

where the value of $k$ determines one of the three grain populations involved, as shown in Table 2.6. This early model [Frazier E.N., Infrared Radiation of the Zodiacal Light, SPIE 124, 139, 1977] uses too high a value for the grain albedo (ratio of scattered to received energy), as shown by Mauser M.G., Ap. J. 278, L19, 1984.

The monochromatic intensity received at the Earth can be expressed as

$$
I ( \lambda , \varepsilon , \beta ) = I _ { \mathrm { S } } ( \lambda , \varepsilon , \beta ) + I _ { \mathrm { E } } ( \lambda , \varepsilon , \beta ) ,
$$

where $\varepsilon$ and $\beta$ are the ecliptic coordinates of the line of sight (solar elongation $\varepsilon$ and latitude $\beta$ ), and $I _ { \mathrm { S } }$ ; $I _ { \mathrm { E } }$ are the contributions from scattered sunlight and intrinsic thermal emission, respectively.

![](images/e60ef600c0a979a041fcde93cb3f490f5a1d32f3ba16c6db1d0fa6089ab8c814.jpg)  
Fig. 2.19 Scattered zodiacal light. Isophotes of the scattered intensity measured in the direction $\varDelta$ , characterised by its azimuth $\varepsilon$ (measured from the Sun), and its ecliptic latitude $\beta . ~ P$ is the ecliptic north pole. The intensity contours are specified in $S _ { 1 0 }$ units, that is, in numbers of starsˇ ˇ of magnitude $m _ { \mathrm { v } } ~ = ~ 1 0$ per square degree (see AQ, Sect. 73). For $S _ { 1 0 } ~ = ~ 1$ , the brightness at $\lambda = 5 4 0 \mathrm { n m }$ is $1 . 2 6 \times 1 0 ^ { - 8 } \mathrm { W } \mathrm { m } ^ { - 2 } \mu \mathrm { m } ^ { - 1 } \mathrm { s r } ^ { - 1 }$ , or $4 . 3 \times 1 0 ^ { - 1 6 } \overline { { B } } _ { \odot }$ D, where $\overline { { B } } _ { \odot }$ is the average D  brightness of the Sun at that wavelength. (Levasseur-Regourd A.C., Dumont R., Astr. Ap. 84, 277, 1980)

Table 2.6 Size of interplanetary dust grains   

<table><tr><td>a[μm]</td><td>k</td><td>No[cm-3]</td></tr><tr><td>0.008-0.16</td><td>2.7</td><td>10-12</td></tr><tr><td>0.16-0.29</td><td>2.0</td><td>1.1 × 10-14</td></tr><tr><td>0.29-340</td><td>4.33</td><td>1.9 × 10-17</td></tr></table>

![](images/c7ce91502400694b267e80284a5a4450d1504f96f0bb90fb42dd5d4f8eda1ec7.jpg)  
Fig. 2.20 Spectrum of zodiacal light in the visible and the whole of the infrared. The ordinate is the reduced brightness $\lambda I ( \lambda )$ . (The advantage of using this quantity is explained in Sect. 3.1.) The inset shows the line of sight $\varDelta$ . The measurement points for $I _ { \mathrm { S } }$ are from the satellite IRAS. (After Hauser M.G. et al., Ap. J. 278, L19, 1984)

The scattered intensity $I _ { \mathrm { S } }$ manifests exactly the colour of the Sun’s photosphere, which has colour index $( \mathbf { B } - \mathbf { V } ) _ { \odot } = 0 . 6 5$ , to be compared with $( \mathrm { B } - \mathrm { V } ) _ { \mathrm { S } } = 0 . 6 4$ . The spatial dependence of $I _ { \mathrm { S } }$  D  Dis shown in Fig. 2.19 (see also AQ, Sect. 84) and the spectrum is given in Fig. 2.20.

Figure 2.20 gives the radiated intensity of the zodiacal nebula in the whole of the infrared region. This intensity depends very much on the position of observation, which corresponds, in the figure, to a choice of orbit close to the Earth and a line of sight lying in the ecliptic plane, at $9 0 ^ { \circ }$ to the direction of the Sun. The emission is fitted to measurement points obtained by the satellite IRAS (InfraRed Astronomical Satellite, 1983). It can be well represented by the curve corresponding to grey grains of constant emissivity $3 . 8 \times 1 0 ^ { - 7 }$ , with a mean temperature of $T =$ $2 3 5 \mathrm { K }$ ; but even better by the curve for grains of $\lambda$ D-dependent emissivity (in fact, a function of $\lambda ^ { - 1 }$ , see Sect. 2.4), with temperature $1 6 4 \mathrm { K }$ . Note the deep minimum between the scattered and thermal components, near $3 . 5 \mu \mathrm { m }$ . This minimum in the background emission due to the interplanetary ‘atmosphere’, is sometimes called the cosmological window, permitting, as it does, observation of distant, and therefore faint, objects. At wavelengths above $1 0 0 \mu \mathrm { m }$ , great care must be taken to extract the contribution of the zodiacal nebula when measuring the weak signals of the cosmological background: the WMAP and Planck missions (the latter was launched in 2008) will thus refine our knowledge of this emission (see Sect. 7.4).

The observations made possible by this window may be carried out from the ground or from higher altitudes. The background zodiacal emission, which decreases as the wavelength increases from 1 to $3 \mu \mathrm { m }$ , makes way for atmospheric emission, or indeed emission from the instrument itself, should the latter not have been cooled. Hence, the point of minimum emission is shifted anywhere between $\lambda = 1 . 6 \mu \mathrm { m }$ (for the non-cooled Hubble telescope, emissivity 0.2) and $\lambda = 2 \mu \mathrm { m }$ (for D Da ground-based telescope optimised in the infrared, emissivity 0.03), but attaining its lowest value at $2 . 5 \mu \mathrm { m }$ (as envisaged for a $_ { 6 \mathrm { m } }$ telescope project, at temperature $2 0 0 \mathrm { K }$ , emissivity 0.03, to be carried by stratospheric dirigible at altitude $1 2 \mathrm { k m }$ over the Antarctic).

# High-Energy Particles and Photons

Diffuse Cosmic Background

In the $\mathrm { X }$ and $\gamma$ ray regions, this background (see Fig. 2.21) consists mainly of a superposition of emissions with different redshifts, originating in active galactic nuclei (quasars, Seyfert galaxies). Visibility of a specific object in the field of view is reduced, because fluctuations in this cosmic background act as a source of noise when measuring the flux from the object. Between $1 0 \mathrm { k e V }$ and $1 \mathrm { M e V } ,$ the spectrum is governed approximately by the power law $I = 8 7 . 4 { \times } 1 0 ^ { - 2 . 3 } \mathrm { c m } ^ { - 2 } \mathrm { s } ^ { - 1 } \mathrm { s r } ^ { - 1 } \mathrm { k e } \mathrm { V } ^ { - 1 }$ . DThis source of noise, which dominates in the $\mathrm { X }$  region $( E < 5 0 \mathrm { k e V } )$ , becomes negligible at higher energies $E > 5 0 0 \mathrm { k e V } ,$ ), where another background signal takes over, namely the one produced by interactions of charged particles with the detector and its environment. Collimators restricting the instrument’s field of view are used to minimise background noise from this source.

![](images/e518fa78cf8a5034e74d8f113154778fe8f5b954ce4dbd55a64125ccde9825f9.jpg)  
Fig. 2.21 Observed spectrum of diffuse electromagnetic cosmic background between $3 \mathrm { k e V }$ and $1 0  { \mathrm { M e V } }$ (X and $\gamma$ rays). The straight line represents the power law $E ^ { - 2 . 3 }$ , which gives a good fit to the observations. (After Gruber D.E. et al., Ap. J. 520, 124 1999)

# Solar Wind

The solar wind is hydrogen plasma ejected from the Sun, which travels at high speeds along the field lines of the heliosphere. It varies with solar activity and its intensity determines the size of the heliosphere. In active solar periods, solar flares send huge quantities of particles into interplanetary space (see Fig. 6.37). The flux of particles can then increase by a factor of 1 000 for almost one day. Such events greatly perturb the running of observatories in orbit. Indeed, their measurements often become unusable, and the instruments, or even the spacecraft, may suffer considerable damage (e.g., electronic failure). It is of the utmost importance to assess the radiation impinging on each part of an experiment, and this throughout the mission, in order to select components of the appropriate quality (particularly, resistance to irradiation).

# Radiation Belts

The trajectories of charged particles in the solar wind, electrons and protons, are modified by the lines of force of the Earth’s magnetic field, and some particles are trapped in what are referred to as radiation belts (van Allen belts).13 The proton belt extends roughly between altitudes $1 0 0 0$ and $1 5 0 0 0 \mathrm { k m }$ . The electron belts extend as far as $5 0 0 0 0 \mathrm { k m }$ , and at high geomagnetic latitudes have ‘horns’ which descend to low altitude. There are two belts, or two maxima, in the distribution of electrons, the main one being at about $2 0 0 0 0 \mathrm { k m }$ , with a secondary maximum at about $3 0 0 0 \mathrm { k m }$ (Fig. 2.22). Moreover, the motion of the geomagnetic axis relative to the axis of the Earth’s rotation tends to bring the belts closer together in the austral region of the Atlantic ocean, and this creates the so-called South Atlantic Anomaly (Fig. 2.23).

![](images/722bbfe8dbaee05aa69c70571dd66342c6697572c3b26fe2c916311fa74bf527.jpg)  
Fig. 2.22 Radiation belts of the Earth. Iso-intensity curves represent the mean flux, integrated over all directions, of electrons (right) and protons $( l e f t )$ ; $z$ is the axis of the Earth’s magnetic poles and $x$ lies in the plane perpendicular to it, with units equal to $R _ { \mathrm { e } }$ , the Earth’s radius. Flux units are the number of particles $\mathrm { c m } ^ { - 3 } \mathrm { s } ^ { - 1 }$ above an energy threshold indicated in MeV. [After Daly E.J., Evaluation of the space radiation environment for ESA projects, ESA Journal 88 (12), 229, 1988]

![](images/a2dcef4994e6ab5dda6aa06fa093bb3ab8e4a3d21f0d5924c56afa9c3858aaa9.jpg)  
Fig. 2.23 Distribution of electron flux ( $E > 5$ MeV) at altitude $1 0 0 0 \mathrm { k m }$ . Contours refer to number of electrons $\mathrm { c m } ^ { - 2 } \mathrm { s } ^ { - 1 }$ . The flux is essentially directed along the lines of force of the Earth’s magnetic field. Note the South Atlantic Anomaly, and the concentrations in the auroral zones. The data shown is only quantitatively correct for the epoch 1968–1970. (After Stassinopoulos E.G., NASA SP-3054, 1970. With the kind permission of E.G. Stassinopoulos)

Cosmic Rays

The protons, electrons, and nuclei comprising cosmic rays enter the Solar System and interact with the heliosphere, which opposes their penetration. The extent of the heliosphere, made by the solar wind, increases as the Sun is active, and hence the penetration of cosmic rays is governed by solar activity; the flux of cosmic rays in the neighbourhood of the Earth is maximum when solar activity is minimum, and conversely (Fig. 2.24). This phenomenon is called solar modulation. The Earth’s magnetosphere also opposes the penetration of cosmic rays.

![](images/86e79a7268231f1fbe60d989430c6c89220acc17e0456134ee7b4c8939dc1e66.jpg)  
Fig. 2.24 Flux of cosmic ray particles outside the Earth’s cavity, for various nucleons. The ordinate $\varPhi$ is a differential energy distribution (number of nucleons considered $\mathrm { m } ^ { - 2 } \mathrm { s r } ^ { - 1 } \mathrm { s } ^ { - 1 } \mathrm { M e V } ^ { - 1 } ,$ , and the abscissa is the nucleon energy. Modulation due to solar activity is visible at low energies: dashed curves indicate maximum and minimum levels of the solar cycle (upper and lower curves, respectively); continuous curves refer to mean solar activity. (After Webber W.R., Lezniak J.A., Astrophys. Sp. Sci. 30, 361, 1974)

# Background from Interaction with Surrounding Matter

Orbiting observatories, and all measurements they carry out, are affected by the arrival of these particles. Protons from the Sun or in cosmic rays induce spallation in all matter constituting or surrounding experiments. This matter thus becomes radioactive, emitting neutrons or $\gamma$ rays, either immediately (instantaneous de-excitation), or after a lapse of time determined by the lifetime of whatever radioactive isotopes have been created. Hence, not only do charged particles interfere directly with $\gamma$ -ray detectors, simulating the detection of high energy photons, but also the detectors are blinded by $\gamma$ ray emission from de-excitation of surrounding matter.

This emission has a highly complex spectrum, containing many de-excitation lines superposed upon a continuous emission. This emission contributes to the background and limits the sensitivity of the experiment. As its spectrum has a slope less than the spectrum of diffuse emission, the former greatly exceeds the latter in the $\gamma$ ray region. The contribution varies with the particle environment of the satellite, which is due to belts and cosmic rays, and therefore depends on the orbit, the position of the satellite on this orbit, and solar activity.

# 2.9.3 Choice of Orbits

With the advent of space travel, it has become possible to launch probes to make measurements, and to explore in situ, or in the vicinity of, objects in the Solar System; and also to launch observatories to measure electromagnetic radiation, for the main part, but possibly gravitational radiation in the future, which has been emitted from distant objects outside the Solar System, thus complementing in this case the role of ground-based observatories.

The choice of orbit for a probe depends at the outset on the object under study, e.g., the Moon, Mars, Saturn, cometary nucleus, and so on, the problem being one of organising an encounter, with the help of calculations in the realm of celestial mechanics. The aims of the observation dictate the choice of location for the observatory. But other factors must nevertheless be taken into account: the power and availability of launchers; the cost of the mission; and the location of receiving stations on the Earth or of relay satellites in direct view of the space observatory, given that rates of data production are often such that it cannot be stored even temporarily aboard, but must be continuously transmitted. A compromise is often necessary between the ideal location and the one eventually opted for.

In low equatorial orbits (300 to $5 0 0 \mathrm { k m }$ ), which are used by the space shuttle and the International Space Station (ISS), communication is easy and repairs are possible. On the other hand, their lifetime is reduced by residual atmospheric friction, the Earth blocks $2 \pi$ sr of the field of view, and changes between night and day take place very quickly, leading to breaks in visibility of the studied source about once every hour. Such an orbit was chosen for the Hubble telescope because it could be easily accessed by the space shuttle.

In high circular orbit (6 000 to $1 0 0 0 0 0 0 \mathrm { k m }$ ), pointing is easier, observation periods are long, blocking of the field of view by the Earth is reduced, and interference from scattering, or radiofrequency and thermal emissions, due to the Earth is weaker. On the other hand, the energy required for the launch and for communication is greater, and the costs are therefore higher. Such an orbit was chosen for the satellite Hipparcos (1989), but was never attained, owing to failure of a boost motor.

A compromise can be made by choosing a highly elliptical orbit, which requires less power for the launch, and passes close to the Earth to transmit its data, although this involves storing data on board; the satellite nevertheless spends most of its time far from the Earth and its associated interference emissions. The distance of the ISO satellite (Infrared Space Observatory, 1995), placed in an elliptical orbit, thus varied between 2 000 and $7 0 0 0 0 \mathrm { k m }$ .

The best orbits for $\gamma$ ray astronomy are either very distant, avoiding the radiation belts, or else close circular equatorial orbits, avoiding the South Atlantic Anomaly and protected from cosmic rays by the magnetosphere. The latter offer by far the most suitable conditions for observation, but, unfortunately, are rather inaccessible from most of the larger launch pads (Cape Canaveral in Florida and Baikonour in Central Asia), and represent no interest whatsoever from the economic point of view (for telecommunications or remote sensing), or from a military point of view (observation of the Earth’s surface). They are thus left unexploited by the space agencies. Indeed, there are some problems associated with them. Their occultation by the Earth limits observation periods and complicates manoeuvres. Radio links with the satellite are usually very short, unless a large number of relay satellites are available (a system of relay satellites called Transmission Data Relay Satellite System, TDRSS). In general, a mass memory must be installed aboard the satellite. For all these reasons, distant circular orbits $( > 6 0 0 0 0 \mathrm { k m } )$ , or eccentric orbits (apogee around $2 0 0 0 0 0 0 \mathrm { k m } ,$ ), are considered to represent the best compromise; although there is more noise, observation and transmission conditions are less restrictive.

Finally, the Lagrange points14 should be mentioned. These are rather special locations in space at which the gravitational fields of the Earth and the Sun combine to give a local minimum of gravitational potential, thus favouring a stable orbit there. Given two bodies, there are five points at which a small object can remain in stable or unstable equilibrium while co-orbiting with the Earth (E) around the Sun: three are located on the line SE, $\mathrm { L } _ { 1 }$ (between S and E) and $\mathrm { L } _ { 2 }$ at $1 . 5 \times 1 0 ^ { 6 } \mathrm { k m }$ symmetrically with respect to E, $\mathrm { L } _ { 3 }$ opposite E; $\mathrm { L } _ { 4 }$ and $\mathrm { L } _ { 5 }$ sit at the vertices of two symmetrical equilateral triangles with base SE. If a satellite is placed at one of these points, it can maintain a fixed position with respect to the Earth and the Sun, which is a great help for communications, but also for controlling thermal conditions. The European solar observatory SOHO (1995) occupies the point $\mathrm { L } _ { 1 }$ , while $\mathrm { L } _ { 2 }$ is or will be occupied by the European missions Planck (2008), Herschel (2008), and Gaia (2011), then NASA’s JWST (2013), successor to the Hubble Space Telescope.

As yet, no observatory operating beyond the confines of the Solar System, and therefore outside the interference emissions of the Sun or the zodiacal nebula, has been seriously envisaged, for reasons of cost and owing to the problem of fast transmission to Earth.

# 2.10 The Moon as an Astronomical Site

The Moon was explored for the last time by the astronauts of the mission Apollo 17 in 1972, and completely surveyed by the unmanned probe Clementine in 1994. The density of the lunar atmosphere is a factor of $1 0 ^ { 1 4 }$ less than that of the Earth at its surface, and the Moon can be considered to be practically without atmosphere. It thus offers observation conditions very similar to those encountered in interplanetary space, which give access to the whole of the electromagnetic spectrum.

We briefly discuss the main features of the Moon’s surface that are relevant to setting up astronomical observatories:

The lunar day lasts 27.321 terrestrial days. Such a long night allows long integration periods on a single source. In the polar craters, and in particular in the deep crater discovered at the south pole, the Sun only grazes the horizon, offering simultaneously a source of energy and a permanent state of half-night. The lunar surface is stable, seismic activity being less by a factor of $1 0 ^ { 8 }$ than on Earth. This could provide an almost infinitely stable foundation for telescopes. The stability would be invaluable for long baseline interferometry, which could extend over hectometres or kilometres, in the seas or in the depths of craters, and could observe at wavelengths anywhere from the ultraviolet to the millimetre range.   
. The absolute instantaneous position of the Moon relative to stellar reference frames (see Chap. 4) is known to a very high degree of accuracy, far greater than the accuracy to which the position of an orbiting observatory can be known. The absolute position of the Moon, and its position relative to the Earth, are known to within a few millimetres, which is quite remarkable.   
. The ground temperature varies widely between day and night, from 90 to $4 0 0 \mathrm { K }$ except perhaps at high latitudes. This is a major disadvantage as regards thermal protection of instrumentation, but the very low temperatures reached by the ground provide a potential cryogenic source which would be invaluable for the cooling of telescopes, in the infrared and submillimetre regions, and for the cooling of detectors.   
. The weak gravity on the Moon $_ { ( 0 . 1 6 ~ g ) }$ makes it possible to build large structures which are both rigid and light. It is sufficiently strong, however, to bring surface dust back down to the ground, whereas any debris in space tends to co-orbit with its source. There nevertheless remains some uncertainty concerning the effects of a surface electric field on the dust; the surface of the dust grains is charged by the photoelectric effect of solar UV and by the space charge associated with it.   
. The face of the Moon which remains permanently hidden from the Earth is entirely free of man-made radiofrequency interference, a fact which would strongly favour the setting up of radiotelescopes. Moreover, there is no ionosphere, and this would open the way to very low frequency radioastronomy, between $3 0 \mathrm { M H z }$ and $1 0 0 \mathrm { k H z }$ , which means wavelengths between $1 0 \mathrm { m }$ and $3 0 \mathrm { k m }$ , a range quite inaccessible on the Earth, unless conditions are exceptional. Combination with a radiotelescope carried by satellite would then provide very long baseline observations, even at these frequencies. This part of the spectrum has hardly been explored as yet. Apart from the cost of setting up a lunar base, either manned or operated by robots, the main disadvantages are: the continual bombardment of the lunar surface by the solar wind and cosmic rays; the intense solar radiation in the EUV and X-ray regions; and the incessant impacts of micrometeorites (100 microcraters larger than $0 . 0 5 \mathrm { m m }$ across are created per square metre per year).

Even though the construction of an astronomical base on the Moon is not for the immediate future, it is important to bear the idea in mind, because in some ways a lunar site could compete with orbital sites.

# Problems

2.1. Using the fractional content of water vapour in air (Fig. 2.3), calculate the total quantity of precipitable water above the altitudes $4 \mathrm { k m }$ (Hawaii-sized mountain) and $1 2 \mathrm { k m }$ (airborne observatory).

2.2. The absorption cross-section of molecular oxygen is roughly $\kappa = 1 0 ^ { - 1 } \mathrm { c m } ^ { 2 }$ $\mathbf { g } ^ { - 1 }$ D. Calculate the horizontal optical depth of the atmosphere over a length $l \ =$ $1 \mathrm { k m }$ at altitude $z = 4 \mathrm { k m }$ D, in the molecular oxygen absorption band at wavelength $\lambda = 4 . 8 \mathrm { m m }$ $\nu = 6 2 . 5 \mathrm { G H z }$ ). Compare the result with the values given in Fig. 2.6. D DCalculate the integrated optical depth for the whole atmosphere.

Answer. The mass of $\mathrm { O } _ { 2 }$ along a horizontal line of length $l$ , and per unit normal area, is

$$
\frac { l \rho _ { 0 } ( z ) M ( \mathrm { O } _ { 2 } ) } { 5 M _ { 0 } } ,
$$

where $\rho _ { 0 } ( z ) / M _ { 0 }$ is the molecular density at altitude $z$ , and $M ( \mathbf { O } _ { 2 } )$ is the molecular mass of $\mathrm { O } _ { 2 }$ . At $z = 4 \mathrm { k m }$ , $M _ { 0 } = 2 9 \mathrm { g }$ and

$$
\rho _ { 0 } ( z ) =  { \mathrm { e } } ^ { - z / H } M _ { 0 } \frac { P } { R T _ { 0 } } = 7 7 4  { \mathrm { g } }  { \mathrm { m } } ^ { - 3 } ,
$$

which gives $\tau = 1 0 ^ { 3 } \times 7 7 4 \times 3 2 \times 1 0 ^ { - 1 } \times 1 0 ^ { - 4 } / 2 9 \times 5 = 1 . 7 .$ This should be com-D      Dpared with the value given in Fig. 2.6; the attenuation in db $\mathrm { k m } ^ { - 1 }$ is approximately 5, which implies $\tau = 5 \times 0 . 2 3 = 1 . 1 5$ .

D Vertically, the mass of $\mathrm { O } _ { 2 }$ Dper unit area normal to the vertical line is

$$
\frac { M ( \mathrm { O } _ { 2 } ) } { 5 M _ { 0 } } \int \rho _ { 0 } ( z ) \ : \mathrm { d } z ,
$$

which implies that $\tau = 2 2 . 6$ from ground level, and $\tau = 1 3 . 6$ from $z = 4 \mathrm { k m }$ . The Datmosphere is thus optically thick at this wavelength.

2.3. Find the damping coefficient $\gamma$ for the pure rotational transition of the $_ { \mathrm { H } _ { 2 } \mathrm { O } }$ molecule at $\lambda = 2 . 1 \mathrm { m m }$ , assuming that the band profile is Lorentzian (Fig. 2.6). DCompare the value obtained with the collision frequency at the given pressure.

2.4. From the variation of horizontal attenuation of a band of $\mathrm { O } _ { 2 }$ as a function of altitude (Fig. 2.6), calculate the scale height of this component in the troposphere. Calculate the scale height of $_ { \mathrm { H } _ { 2 } \mathrm { O } }$ for the concentrations used in Fig. 2.6.

Answer. The $z$ dependence of the horizontal attenuation $A$ is

$$
A ( \mathbf { O } _ { 2 } ) \propto \rho _ { \mathrm { O } _ { 2 } } ( z ) \propto \mathrm { e } ^ { - z / H } ,
$$

which implies $H = ( z _ { 2 } - z _ { 2 } ) / \log ( A _ { 1 } / A _ { 2 } )$ . Then, from Fig. 2.6, $H = 8 \mathrm { k m }$ for $\mathrm { O } _ { 2 }$ and $H = 4 . 5 \mathrm { k m }$ Dfor $_ { \mathrm { H } _ { 2 } \mathrm { O } }$ .

2.5. What is the wavelength limit for near ultraviolet observations from a site at an altitude of $z = 2 . 8 6 \mathrm { k m }$ (Pic du Midi observatory, France), or $z = 4 . 2 \mathrm { k m }$ (Mauna DKea, Hawaii)?

2.6. Calculate the collision frequency of atmospheric constituents at an altitude of $z = 1 0 0 \mathrm { k m }$ , and compare it with the frequency of spontaneous radiative decay of Dneutral oxygen O I by the transition $^ { 1 } S$ to $^ 1 D$ , with wavelength $\lambda = 5 5 7 . 5 \mathrm { n m }$ , for which $A _ { \mathrm { r a d } } = 1 . 3 4 \mathrm { s } ^ { - 1 }$ . Adopt a collision cross-section of $\sigma \approx 1 0 ^ { - 2 0 } \mathrm { m } ^ { 2 }$ .

Answer. For $z = 1 0 0 \mathrm { k m }$ , $T = 2 1 0 \mathrm { K }$ and $P = 1 0 ^ { - 3 } \mathrm { m b }$ , and the typical speed $\nu$ of Da molecule is given by

$$
\frac { 3 } { 2 } k T = \frac { M _ { 0 } \langle \nu ^ { 2 } \rangle } { 2 \mathbf { N } } \quad \mathrm { i m p l y i n g } \quad \nu = \sqrt { \frac { 3 k T \mathbf { N } } { M _ { 0 } } } ,
$$

where $_ \mathrm { N }$ is Avogadro’s number. The typical molecular density is $n = P \mathrm { N } / \mathrm { R } T$ , and the typical time between two collisions

$$
t = A _ { \mathrm { c o l } } ^ { - 1 } \approx \frac { 1 } { n \sigma \nu } = 0 . 8 \ : \mathrm { s } ,
$$

implying $A _ { \mathrm { c o l } } = 1 . 2 \mathrm { s } ^ { - 1 } \gg A _ { \mathrm { r a d } }$ . At this altitude, the collisional de-excitation rate D 	has decreased sufficiently for spontaneous radiative de-excitation to become significant.

2.7. At an astronomical site of average quality, the seeing disc of a star has an angular size of $2 ^ { \prime \prime }$ . At an exceptional site, and at the right moment, an optimised telescope can give an image ten times smaller. What is the gain in contrast obtained for the detection of a quasar (angular size $\ll 1 ^ { \prime \prime }$ ), or for the detection of a galaxy (angular size $> 1 ^ { \prime \prime }$ )?

![](images/87e23fe61b0f224a91c9650d1f5e6e9aa25b1b57422d0517c25b655de3c2801d.jpg)  
Fig. 2.25 Space and time fluctuations of the atmosphere at submillimetric wavelengths (Mauna Kea, Hawaii, $4 2 0 0 \mathrm { m }$ )

Answer. The energy of an unresolved source (in this case, a quasar) is diluted in the marks it generates across the image plane. The gain in spatial resolution thus leads directly to a gain in contrast. On the other hand, for a resolved source, there is no effect whatsoever, the flux received per pixel being the same. Apart from improving image resolution, the techniques of adaptive optics can thus increase the capacity to detect weak unresolved sources.

2.8. Submillimetre Observations on Hawaii. The space and time fluctuations $I _ { \sigma } ( \theta , t )$ of atmospheric emission are measured at Mauna Kea, altitude $z = 4 . 2 \mathrm { k m }$ , $\sigma = 1 1 \mathrm { c m } ^ { - 1 }$ , where $\theta$ is the azimuth of the line of site and $t$ Dthe time. Rayleigh– DJeans emission is assumed, with brightness temperature $\langle T \rangle = 1 0 0 \mathrm { K }$ . Figure 2.25 shows the fluctuation $\Delta T$ h i D(mK) (ordinate) for this brightness temperature. From the figure, estimate the mean emissivity $\varepsilon$ of the atmosphere, and also the standard deviations $\sigma _ { \theta }$ and $\sigma _ { t }$ , in space and time, respectively, of the received emission. Given that the average wind speed is $\nu = 3 5 \mathrm { k m h r ^ { - 1 } }$ during these measurements, Dcalculate the average size of the atmospheric inhomogeneities causing the observed fluctuations. (After Pajot F., Thesis, 1983.)

# Chapter 3 Radiation and Photometry

This chapter deals with several fundamental properties of electromagnetic radiation.

We first define the basic notions of radiometry, namely, the physical quantities associated with the energy transported by electromagnetic radiation. Those photometric quantities and units related to lighting techniques, photography, and so on, are all adapted to the sensitivities of the human eye. This means that they refer to visible wavelengths, and thus are not suitable for astronomical observations, which cover the whole electromagnetic spectrum and must therefore be independent of the properties of the human eye.

We then consider the coherence properties of radiation, which are related to the space and time distributions of the energy transported. These properties are particularly relevant in the study of image formation (see Chap. 6), and the study of spectra (see Chap. 8).

Blackbody radiation plays a central, although not exclusive, role in the emission of astrophysical objects, and also in the limitations on observation. Several relevant properties will be discussed. A detailed treatment of radiative transfer in astrophysical objects, or the physical mechanisms producing the various emissions, will not be given here.

Absolute calibration aims to provide a way of converting measurements into the absolute energy values emitted at one or another wavelength by the objects under study, be they stars, interstellar clouds, molecules or dust grains, pulsars, galactic nuclei, accreting X-ray sources, cosmological background, or any other. These values determine the overall balance of mass or energy in the Universe, and its evolutionary time scales, even revealing, from time to time, the presence of previously unknown physical phenomena. Hence their great importance in astrophysics and physical cosmology.

The difficulty involved in constructing calibration sources in the laboratory, which remain accurate over a wide range of wavelength regions, should not be underestimated. Comparison of these sources with astronomical sources is also a difficult task, when the Earth’s atmosphere, or the observation conditions of unmanned telescopes in space, are taken into account. It is not unusual, under these conditions, for certain physical quantities to be revised by quite large amounts, with significant consequences for any previously elaborated models. As a result, astrophysics has sometimes earned itself the undeserved reputation of being a science in which only orders of magnitude are possible, rather than precise values. This situation is rather a sign of the great experimental difficulty involved in observation.

# 3.1 Radiometry

Originally, the term photometry was used by opticians, and referred to measurement of the various energy quantities associated with visual sensations. It was thus closely linked to the spectral properties of a rather specific detector, the human eye. Radiometry, in the same classical sense, deals more generally with the energy transported by electromagnetic radiation, at whatever wavelength.

Astronomy has developed its own terminology, although more or less in agreement with the existing official definitions, as it passed through stages of visual, then photographic, and then photoelectric observation. And astrophysics, which deals with radiative transfer from a theoretical point of view, has also adopted a language not always perfectly coherent with existing terms. We shall try to clarify these points.

The term photometry, as it is used in astronomy, covers the quite general meaning of radiometry. We use it in this way, noting that most of the quantities to be defined refer to some specified wavelength or frequency, and that, strictly speaking, the correct term would be spectrophotometry, which is indeed often used. Photometry is very closely linked to the general ideas of spectroscopy, dealt with in Chap. 8.

# Definitions

Etendue (Throughput)

This geometrical notion defines the limits of a set of rays carrying energy (Fig. 3.1). Considering a pencil of rays emitted by the surface element $\mathrm { d } S _ { 1 }$ , and received by the element $\mathrm { d } S _ { 2 }$ at a distance $r$ , the etendue´ or throughput is defined as

$$
{ \frac { 1 } { r ^ { 2 } } } \mathrm { d } S _ { 1 } \cos \theta _ { 1 } \mathrm { d } S _ { 2 } \cos \theta _ { 2 } = \mathrm { d } \sigma _ { 1 } \mathrm { d } \varOmega ,
$$

where $\mathrm { d } \sigma _ { 1 }$ is the projection of $\mathrm { d } S _ { 1 }$ normal to the direction of propagation $\pmb { k }$ , and d˝ is the solid angle subtended by the pencil at $\mathrm { d } S _ { 1 }$ .

It can be shown that conservation of energy by the propagation implies that the product of the etendue and the square of the refractive index is constant. In vacuum, ´ $n = 1$ and therefore the etendue is a conserved quantity. ´

![](images/9edf441a273667aed1067d983b8b08a76ace608d052dcc0c9c4408fb277cb1da.jpg)  
Fig. 3.1 Beam etendue ´

Transported Power

The power transported by radiation of wave vector $\pmb { k }$ , across surface element d normal to $\pmb { k }$ at a point $M$ , in the frequency range between $\nu$ and $\nu + \mathrm { d } \nu$ , and in the solid angle $\mathrm { d } \varOmega$ , is written

$$
\mathrm { d } P _ { \nu } = I _ { \nu } ( k , M ) \mathrm { d } \sigma \mathrm { d } \varOmega \mathrm { d } \nu .
$$

$I _ { \nu }$ is called the specific intensity at $M$ in the direction $\pmb { k }$ and is measured in $\mathrm { ~ W ~ m ~ } ^ { - 2 } \ \mathrm { s r } ^ { - 1 } \ \mathrm { H z } ^ { - \mathrm { i } }$ . The term is used in the theory of radiative transfer, and is also the usual terminology in astronomy, although it differs from the one adopted internationally in standard radiometry, where intensity refers to the total emitted power (in watts), integrated over the whole surface of the emitter.

It will be shown in Chap. 7 that a distinction must be made between detectors which measure intensity and detectors which measure electric field $ { \boldsymbol { E } } _ { \nu }$ . The quantities $I _ { \nu }$ and $ { \boldsymbol { E } } _ { \nu }$ are related by the Poynting vector, whose average flux across a surface is the power crossing that surface. This gives

$$
I _ { \nu } = { \frac { 1 } { 2 } } \varepsilon _ { 0 } c \langle E _ { \nu } ^ { 2 } \rangle .
$$

When the quantity $I _ { \nu }$ refers to the power emitted by a surface, it is also called the specific or monochromatic intensity. The integral of this intensity over all space directions, divided by $4 \pi$ , is called the mean monochromatic intensity $[ \mathrm { W ~ m } ^ { - 2 } \mathrm { H z } ^ { - 1 } ]$ .

Monochromatic Flux

The power received per unit area normal to the propagation direction $\pmb { k }$ is

$$
\frac { \mathrm { d } P _ { \nu } } { \mathrm { d } S _ { 2 } \cos \theta _ { 2 } } = \mathcal { E } _ { \nu } \mathrm { d } \nu ,
$$

where $\boldsymbol { \mathcal { E } } _ { \nu } ^ { o }$ is called the monochromatic flux produced by those sources illuminating the receiving surface (the observation site), and has units $\mathrm { ~ W ~ } \mathrm { { m } } ^ { - 2 } \mathrm { ~ H z ^ { - 1 } }$ . In radiometry, it is also called the monochromatic irradiance. It follows that

$$
\mathcal { E } _ { \nu } = \int _ { \mathrm { s o u r c e } } I _ { \nu } \cos \theta _ { 1 } \mathrm { d } \Omega ,
$$

noting that the total monochromatic flux does not depend on the angular size of the source.

Although this quantity is called a flux, and this use is in perfect accord with the terminology of radiative transfer, it does not agree with the official use of the term in radiometry, where the flux is the total power transported by the radiation, and is thus measured in watts.

The flux unit (FU), which is often used in astrophysics, is actually a unit of monochromatic flux, also called the jansky (Jy), in honour of Karl Jansky who was the first to make radioastronomical observations:

$$
1 \mathrm { j a n s k y } = 1 0 ^ { - 2 6 } \mathrm { W } \mathrm { m } ^ { - 2 } \mathrm { H z } ^ { - 1 } .
$$

Magnitudes are logarithmic units of relative monochromatic flux, and their frequent use in astronomy justifies a detailed presentation (see Sect. 3.3). The term monochromatic flux should be adhered to in astrophysical discussions.

Other Units

Units measured per unit frequency interval, as above, can be replaced by units measured per interval of photon energy $( h \nu )$ , per wavelength interval $( \lambda )$ , or per wave number interval $( \sigma ~ = ~ \lambda ^ { - 1 }$ , measured in $\mathrm { c m } ^ { - 1 }$ ). Similarly, power can be Dmeasured in watts, but also in photon number per unit time, for photons of given frequency. Table 3.1 summarises the various units and the terminology encountered in astrophysical literature.

There is not always a satisfactory correspondence between the names of quantities used in astronomy and their official counterparts in radiometry. Power in the former becomes flux (in watts) in the latter, mean intensity becomes emittance or intensity (in $\mathrm { W ~ m } ^ { - 2 }$ ), and flux becomes irradiance (in $\mathrm { W ~ m } ^ { - 2 }$ ). The terms monochromatic and/or spectral, and the dimension $\mathrm { H z } ^ { - 1 }$ , can be added quite naturally to whichever term is used.

able 3.1 Units used in astronomy for the measurement of radiation   

<table><tr><td>Quantity</td><td>Symbol</td><td>S.I. unit</td><td>Other units</td></tr><tr><td>Etendue</td><td></td><td>m² sr</td><td></td></tr><tr><td rowspan="4">Specific intensity</td><td>1</td><td>W m-² sr-1 Hz-1</td><td></td></tr><tr><td>I</td><td>Wm-² sr-1 m-1</td><td>W m-² sr-1 μm-1,etc.</td></tr><tr><td>I</td><td></td><td>W m-² sr-1 cm-1</td></tr><tr><td>Nv</td><td>quanta m-² sr-1 Hz-1</td><td>quanta m-² sr-1 eV-1,etc.</td></tr><tr><td rowspan="2">Monochromatic flux</td><td>6</td><td>Wm-² Hz-1</td><td> jansky</td></tr><tr><td>8</td><td>Wm-² μm-1</td><td>quanta m-² μm-1,etc.</td></tr></table>

Reduced Brightness

The quantity

$$
\lambda I _ { \lambda } = \nu I _ { \nu } \qquad [ \mathrm { W } \mathrm { m } ^ { - 2 } \mathrm { s r } ^ { - 1 } ]
$$

is independent of the units of wavelength or frequency. Figure 3.2 shows how useful it can be in cases when spectra extend over broad wavelength ranges. Clearly, for a graph giving the quantity $\lambda I _ { \lambda }$ (or $\nu I _ { \nu }$ ) as a function of $\log \lambda$ (or $\log \nu$ , respectively), the powers emitted in various spectral intervals can be compared directly by comparing the areas under the relevant parts of the curve. This is a consequence of the equation

$$
\int _ { \Delta \nu } \nu I ( \nu ) \mathrm { d } \ln \nu = \int _ { \Delta \nu } I ( \nu ) \mathrm { d } \nu .
$$

A further illustration is given in Fig. 2.20.

Luminosity

The total power in watts emitted by an astrophysical source is called its luminosity, and is given by the integral

$$
L = \int _ { S } \int _ { 4 \pi } \int _ { \nu } \mathrm { d } P _ { \nu } = \int _ { \nu } L _ { \nu } \mathrm { d } \nu ,
$$

where $S$ denotes a surface bounding the source and $L _ { \nu }$ is called the monochromatic luminosity [W $\mathrm { H z ^ { - 1 } }$ ].

Polarisation

Several factors make this an important parameter. Firstly, it may reveal properties of the source (magnetic field, aligned dust grains, anisotropic scattering, etc.). Secondly, the detector may only be sensitive to one component of polarisation (e.g., at radiofrequencies). And thirdly, the telescope may alter the polarisation (optics, waveguides).

Consider a plane wave described by

$$
\begin{array} { r l } & { E _ { x } = a _ { 1 } \cos ( 2 \pi \nu t - \boldsymbol { k } \cdot \boldsymbol { r } + \phi _ { 1 } ) , } \\ & { } \\ & { E _ { y } = a _ { 2 } \cos ( 2 \pi \nu t - \boldsymbol { k } \cdot \boldsymbol { r } + \phi _ { 2 } ) , } \end{array}
$$

where $a _ { 1 }$ and $a _ { 2 }$ are the amplitudes in the $x$ and $y$ directions, respectively, $\nu$ the frequency, $\pmb { k }$ the wave vector, and $\phi _ { 1 }$ and $\phi _ { 2 }$ the phases. There are four quantities to be determined, namely $a _ { 1 } , a _ { 2 } , \phi _ { 1 }$ , and $\phi _ { 2 }$ . Putting $\phi = \phi _ { 2 } - \phi _ { 1 }$ , the polarisation of

![](images/c4cbb945f1c7fe987343e1540bb04dfd0d3dacfb76130ecad2b854c4964a4b8e.jpg)  
Fig. 3.2 Upper: Observed sky background radiation, plotting reduced brightness $\nu I _ { \nu }$ against wavelength (lower scale) or against photon energy (upper scale). From left to right are the extragalactic ultraviolet, visible, and infrared contributions, the cosmological blackbody contribution, and finally the radiofrequency radiation in the Galaxy. The interplanetary component (zodiacal emission) has been subtracted. Lower: Smoothed extract from the above spectrum, showing the cosmic optical background (COB), cosmic infrared background (CIB), and cosmic microwave background (CMB). Numerical values indicate the total brightness of each component in $\mathrm { n W } \mathrm { m } ^ { - 2 } \mathrm { s r } ^ { - 1 }$ . Note that the infrared background (formation and evolution of galaxies) is comparable with the optical background (stars), and that the latter is a small fraction of the microwave background. (Figures with the courtesy of Herve Dole, private communication, 2007)´

an arbitrary wave is conveniently specified by the Stokes parameters

$$
\begin{array} { r l } & { I = a _ { 1 } ^ { 2 } + a _ { 2 } ^ { 2 } , } \\ & { Q = a _ { 1 } ^ { 2 } - a _ { 2 } ^ { 2 } = I \cos 2 \chi \cos 2 \psi , } \\ & { U = 2 a _ { 1 } a _ { 2 } \cos \phi = I \cos 2 \chi \sin 2 \psi , } \\ & { V = 2 a _ { 1 } a _ { 2 } \sin \phi = I \sin 2 \chi , } \end{array}
$$

which are related by

$$
I ^ { 2 } = Q ^ { 2 } + U ^ { 2 } + V ^ { 2 } .
$$

The degree of polarisation $\varPi$ of a general wave is defined as

$$
\Pi = \frac { ( Q ^ { 2 } + U ^ { 2 } + V ^ { 2 } ) ^ { 1 / 2 } } { I } ,
$$

where $I , \ Q , \ U , \ V$ are time averages. For the plane wave (above), we obtain $\varPi = 1$

# 3.2 Aspects of Radiation

# 3.2.1 Blackbody Radiation

Although no astronomical source emits exactly as a blackbody, many are sufficiently close to this case to allow their emitted radiation to be approximately characterised by a single temperature. Stellar spectra and the cosmological background provide good examples. Moreover, as telescopes are never at absolute zero temperature, they radiate, as do their surroundings. And detectors are immersed in this radiation, a fact which partly determines their performance.

The specific intensity of a blackbody is given by the Planck law

$$
B _ { \nu } ( T ) = \frac { 2 h \nu ^ { 3 } } { c ^ { 2 } } \left[ \exp { \left( \frac { h \nu } { k T } \right) } - 1 \right] ^ { - 1 } ,
$$

with units $\mathrm { W } \mathrm { m } ^ { - 2 } \mathrm { s r } ^ { - 1 } \mathrm { H z } ^ { - 1 }$ . At high frequencies, this is approximated by the Wien distribution

$$
B _ { \nu } ( T ) \sim { \frac { 2 h \nu ^ { 3 } } { c ^ { 2 } } } \exp { \left( - { \frac { h \nu } { k T } } \right) } , \qquad h \nu \gg k T .
$$

At low frequencies, it is approximated by the Rayleigh–Jeans law

$$
B _ { \nu } ( T ) \sim { \frac { 2 \nu ^ { 2 } } { c ^ { 2 } } } k T = { \frac { 2 k T } { \lambda ^ { 2 } } } , \qquad h \nu \ll { k T } .
$$

The total power radiated per unit surface of the blackbody is

$$
\int _ { \Omega } \int _ { \nu } B _ { \nu } ( T ) \mathrm { d } \nu \mathrm { d } \Omega = \sigma T ^ { 4 } \quad [ \mathrm { W } \mathrm { m } ^ { - 2 } ] ,
$$

where $\sigma = 5 . 6 7 0 \times 1 0 ^ { - 8 } \mathrm { W } \mathrm { m } ^ { - 2 } \mathrm { K } ^ { - 4 }$ is the Stefan–Boltzmann constant. Blackbody D radiation obeys Lambert’s law

$$
\mathrm { d } P _ { \nu } = B _ { \nu } \mathrm { d } S \cos \theta \mathrm { d } \varOmega \mathrm { d } \nu = B _ { \nu } \mathrm { d } \sigma \mathrm { d } \varOmega \mathrm { d } \nu ,
$$

which says that intensity is independent of direction of observation $\theta$ . The fact that the brightness of the Sun, or indeed a star, varies between the centre of the disk and the limb demonstrates that it is not strictly radiating as a blackbody.

The specific intensity is a maximum for a given temperature when

$$
\begin{array} { l } { { \displaystyle { \frac { c } { \nu _ { \mathrm { m } } } } T = 5 . 0 9 9 6 \times 1 0 ^ { - 3 } \mathrm { m K ~ f o r ~ } \frac { \mathrm { d } B _ { \nu } } { \mathrm { d } \nu } = 0 , } } \\ { { } } \\ { { \lambda _ { \mathrm { m } } T = 2 . 8 9 8 \times 1 0 ^ { - 3 } \mathrm { m K ~ f o r ~ } \frac { \mathrm { d } B _ { \lambda } } { \mathrm { d } \lambda } = 0 . } } \end{array}
$$

The intensity given by the Planck formula is only a mean intensity. We will see in Sect. 7.2, in the context of noise phenomena, that this mean value is subject to thermodynamic fluctuations.

# 3.2.2 Coherence

Coherence can be understood intuitively by considering two extreme types of radiation. Total coherence is manifested by a uni-directional monochromatic wave (frequency $\nu$ , wave vector $\pmb { k }$ ). Indeed, it is possible to define the relative phase of this wave at two arbitrarily separated points in space and time. On the other hand, blackbody radiation exhibits the minimal coherence; at two separate points in space, or at two different instants of time, the phase relation of the field is arbitrary, unless the spatial and temporal separations between these two points are very small.

Intermediate cases exist: radiation which is more or less pure spectrally, and nonthermal radiation. The idea of coherence can be defined either in terms of classical electromagnetic wave propagation, or from the photon point of view.

The idea of spatial coherence is crucial in the treatment of image formation (see Chap. 6), whereas temporal coherence comes into the treatment of spectral analysis (see Chap. 8).

# Field Coherence and Mutual Degree of Coherence

We consider a complex field $\mathbf { V } ( t )$ , which will be taken in the most general case as an ergodic and stationary random process, with power spectrum $\mathbf { S } ( \nu )$ . It is

assumed that $\langle \mathbf { V } ( t ) \rangle \ = \ 0$ , so that the autocorrelation and autocovariance are h i Dequal (see Appendix B for definitions and properties). We consider a well-defined polarisation of the field.

Let $\mathbf { V } ( r _ { 1 } , t )$ and $\mathbf { V } ( r _ { 2 } , t )$ be the fields measured at any two points in space, denoted $\mathbf { V } _ { 1 } ( t )$ and $\mathbf { V } _ { 2 } ( t )$ to simplify. Then the complex degree of mutual coherence of these fields is the quantity

$$
\gamma _ { 1 2 } ( \tau ) = \frac { \varGamma _ { 1 2 } ( \tau ) } { [ \varGamma _ { 1 1 } ( 0 ) \varGamma _ { 2 2 } ( 0 ) ] ^ { 1 / 2 } } ,
$$

where

$$
{ { T } _ { 1 2 } } ( \tau ) = \left. { { \bf { V } } _ { 1 } ( t ) { \bf { V } } _ { 2 } ^ { * } ( t + \tau ) } \right.
$$

is the cross-correlation of $\mathbf { V } _ { 1 }$ and $\mathbf { V } _ { 2 }$ . The quantity ${ \cal { T } } _ { 1 1 } ( 0 ) \ = \ \langle \bf { V } \mathrm { _ { 1 } } ( \it { t } ) \bf { V } \mathrm { _ { 1 } ^ { * } } ( \it { t } ) \rangle$ D hrepresents the mean intensity of the field at point 1. The ensemble averages $\langle \quad \rangle$ can be taken over time, given the ergodicity assumption (see Appendix B).

The quantity $\gamma _ { 1 2 } ( \tau )$ describes the spatial coherence, since it correlates the fields at two distinct points of space, and also the temporal coherence, since it compares them at two different instants of time, separated by $\tau$ .

# Quasi-Monochromatic Radiation

Radiation whose spectral density is confined to a neighbourhood of some frequency $\nu _ { 0 }$ is referred to as quasi-monochromatic radiation. For example, for $\Delta \nu \ll \nu _ { 0 }$ ,

$$
S ( \nu ) = \exp \left[ - \frac { ( \nu - \nu _ { 0 } ) ^ { 2 } } { \Delta \nu ^ { 2 } } \right] .
$$

The autocorrelation of the field $\mathbf { V } ( t )$ is then given by

$$
R ( \tau ) = \exp { \left( - \frac { \tau ^ { 2 } } { \tau _ { \mathrm { c } } ^ { 2 } } \right) } ,
$$

with the following important relation holding between the spectral width and the temporal width (Fig. 3.3):

$$
\tau _ { \mathrm { c } } \Delta \nu \simeq 1 .
$$

![](images/089c1fb3b074b181a003247ac5460c0cef07ef512702ae9905dc59f8cdbf41ac.jpg)  
Fig. 3.3 Quasi-monochromatic radiation. Spectral width and temporal coherence

The coherence length, measured along the wave vector $\pmb { k }$ , is $c \tau _ { \mathrm { c } }$ . It is the length over which the field retains the memory of its phase. Further

$$
l _ { \mathrm { c } } = c \tau _ { \mathrm { c } } = \frac { \lambda _ { 0 } ^ { 2 } } { \Delta \lambda } , \qquad \frac { \Delta \lambda } { \lambda _ { 0 } } = \frac { \Delta \nu } { \nu _ { 0 } } ,
$$

and the coherence length is the distance beyond which the waves $\lambda$ and $\lambda + \Delta \lambda$ are out of step by $\lambda$ .

When the length $l$ is such that $l \ll c \tau _ { \mathrm { c } }$ , it follows that

$$
\gamma _ { 1 2 } ( \tau ) \sim \gamma _ { 1 2 } ( 0 ) \mathrm { e } ^ { - 2 \mathrm { i } \pi \nu _ { 0 } \tau } ,
$$

and the coherence is determined by $\gamma _ { 1 2 } ( 0 )$ . Consequently, $\gamma _ { 1 2 } ( 0 )$ is often referred to as the degree of coherence, in the case of quasi-monochromatic radiation.

# Interference Measurements of Coherence

Consider a simple Young slit experiment (Fig. 3.4), in which two diffracted beams interfere. The visibility of the observed interference fringes is defined to be

$$
\mathcal { V } = \frac { I _ { \mathrm { m a x } } - I _ { \mathrm { m i n } } } { I _ { \mathrm { m a x } } + I _ { \mathrm { m i n } } } ,
$$

where $I _ { \mathrm { m a x } }$ and $I _ { \mathrm { m i n } }$ are the maximum and minimum intensities observed. It is not difficult to show that

$$
| \gamma _ { 1 2 } ( \tau ) | = \mathcal { V } .
$$

In the same way, a Michelson interferometer (Fig. 3.5) measures temporal coherence.

![](images/7d12638d3d70fa1737b78ed87520e34a65f71679f89490d733c56df2a827c4a4.jpg)  
Fig. 3.4 Measurement of spatio-temporal coherence by interference

![](images/e9ca84f75341bf514826c5bd2644eeff14e57333865b4a2a74aa3273826baaf9.jpg)  
Fig. 3.5 Measurement of temporal coherence by interference. (a) Schematic representation of a Michelson interferometer. (b) Measurement of output intensity

# Coherence of Blackbody Radiation

Quasi-monochromatic radiation is a particular case of a Gaussian process, where $R ( \tau )$ is itself Gaussian. We recall that there exist infinitely many stationary Gaussian processes, determined by their mean and their autocorrelation $R ( \tau )$ (see Appendix B).

As the radiation of a blackbody is a stationary Gaussian process, its coherence is completely defined by the quantity $R ( \tau )$ . This temporal coherence can be deduced by Fourier transform from the Planck blackbody spectrum $S ( \nu )$ .

# Higher Order Moments

In the case of an arbitrary stationary process, the higher order moments must be specified:

$$
{ \cal T } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { 2 n } ) = \langle { \bf V } ( x _ { 1 } ) { \bf V } ( x _ { 2 } ) \ldots { \bf V } ^ { * } ( x _ { n + 1 } ) \ldots { \bf V } ^ { * } ( x _ { 2 n } ) \rangle ,
$$

where $x _ { i }$ denotes a point $( r _ { i } , t )$ . The complex degree of coherence of order $n$ is defined as

$$
\gamma _ { n } ( x _ { 1 } , \dots , x _ { 2 n } ) = { \frac { \Gamma ( x _ { 1 } , \dots , x _ { 2 n } ) } { \left[ \prod _ { i } { \Gamma ( x _ { i } , x _ { i } ) } \right] ^ { 1 / 2 } } } .
$$

It is straightforward to check that a strictly monochromatic wave gives $\gamma _ { n } = 1$ for any $n$ .

# Coherence and Photon Statistics

Coherence has been presented here from the wave point of view, as the quantity

$$
\langle \mathbf { V } ( t ) \mathbf { V } ^ { * } ( t + \tau ) \rangle .
$$

We now consider how this relates to the particle point of view.

Strictly monochromatic radiation $\exp ( 2 \pi \mathrm { i } \nu _ { 0 } t )$ has infinite coherence time. The wave point of view has nothing to say about fluctuations. In contrast, photons can be described as classical particles, and for any $\tau$ , the number of photons detected in time $\tau$ obeys a Poisson distribution. If $\overline { { n } }$ is the mean number of photons detected per unit time, the variance of $n$ is

$$
\langle \Delta n ^ { 2 } \rangle = \overline { n } \tau .
$$

Quasi-monochromatic radiation (for example, an optically broad spectral line, formed at local thermodynamic equilibrium LTE, and of Gaussian profile), has a finite coherence time $\tau _ { \mathrm { c } } ~ \sim ~ 1 / \Delta \nu$ . If $\tau \gg \tau _ { \mathrm { c } }$ , the fluctuation in the number of photons detected in time $\tau$  	is given by calculation using Bose–Einstein statistics

$$
\langle \Delta n ^ { 2 } \rangle = \overline { { { n } } } \tau ( 1 + \delta ) , \qquad \delta = ( \mathrm { e } ^ { h \nu / k T } - 1 ) ^ { - 1 } ,
$$

and contains both particle and wave terms.

In contrast, for thermal radiation (Gaussian), if $\tau ~ < ~ \tau _ { \mathrm { c } }$ , the photons no longer obey stationary Poisson statistics. Indeed, the photons show a tendency to group together (bunching). The effect becomes significant when $\delta \sim 1$ (Fig. 3.6).

Finally, for non-thermal radiation, this phenomenon becomes more significant as the quantity ı, known as the degeneracy factor, increases.

The study of coherence, that is, the correlation of photons over short time intervals $( < \tau _ { \mathrm { c } } )$ , can be used to detect deviations from LTE in spectral line formation. Progress in the development of quantum detectors may lead to interesting applications of this idea in astrophysics.

For a general introduction to the effects of coherence, and a bibliography, see Harvey A., Coherent Light. See also the interesting discussion in Dravins D. et al., Appl. Opt., 1995. A detailed analysis of thermodynamic fluctuations can be found in Landau L., Lifshitz E.M., Statistical Physics. See also Harvey A., Coherent Light, Chap. 1.

# 3.3 Magnitudes

The magnitude system1 has its origins in the classification of stars according to their visual brightness, introduced by the Greek astronomers. In the nineteenth century, this classification was formulated (by Pogson, 1856) in the form of a logarithmic law, which corresponded roughly to the visual sense.

Magnitudes are relative measures of the monochromatic flux of a source. When referring to stars, which are effectively point-like for observational purposes, the apparent size of the object is irrelevant; but in the case of extended sources, such as galaxies or the sky background, the extent must be taken into account, and a further unit, the magnitude per square second of arc, is introduced, so that the solid angle of observation is equal to 1 arcsec $\times 1$ arcsec.

![](images/4138df65d987e296eaf6ea13070588e3aa09d04a757f11b1d0a6c712322859fc.jpg)  
Fig. 3.6 Schematic representation of the semi-classical model of radiation. .a/ Constant classical intensity leading to photoelectric events with Poisson time distribution. .b/ Classical intensity of a thermal source, with fluctuations leading to a Poisson process combined with a Bose–Einstein distribution, and bunching. (Extract from Dainty J.C., in Image Science)

If $e ( \lambda )$ is the monochromatic flux of a source, measured outside the Earth’s atmosphere, the magnitude at wavelength $\lambda _ { 0 }$ is defined as

$$
m _ { \lambda _ { 0 } } = - 2 . 5 \log { \frac { e ( \lambda _ { 0 } ) } { e _ { 0 } } } = - 2 . 5 \log e ( \lambda _ { 0 } ) + q _ { \lambda _ { 0 } } ,
$$

where the constant $q _ { \lambda _ { 0 } }$ defines magnitude zero.

Table 3.2 Standard photometry. $1 ~ \mathrm { J y } = ~ 1 0 ^ { - 2 6 }$ W $\mathrm { m } ^ { - 2 } ~ \mathrm { H z } ^ { - 1 }$ . It is convenient to note that the magnitude $m _ { \mathrm { v } } = 0$ Dcorresponds to a monochromatic flux of $1 0 ^ { 1 1 }$ photons $\mathrm { m } ^ { - 2 } \mathrm { s } ^ { - 1 } \mu \mathrm { m } ^ { - 1 }$   

<table><tr><td>Name</td><td>λo[μm]</td><td>△λo[μm]</td><td>eo[Wm-² μm-1]</td><td>eo[Jy]</td><td></td></tr><tr><td>U</td><td>0.36</td><td>0.068</td><td>4.35×10-8</td><td>1880</td><td>Ultraviolet</td></tr><tr><td>B</td><td>0.44</td><td>0.098</td><td>7.20 × 10-8</td><td>4650</td><td>Blue</td></tr><tr><td>V</td><td>0.55</td><td>0.089</td><td>3.92 × 10-8</td><td>3 950</td><td>Visible</td></tr><tr><td>R</td><td>0.70</td><td>0.22</td><td>1.76 × 10-8</td><td>2870</td><td>Red</td></tr><tr><td>I</td><td>0.90</td><td>0.24</td><td>8.3 ×10-9</td><td>2240</td><td>Infrared</td></tr><tr><td>J</td><td>1.25</td><td>0.30</td><td>3.4×10-9</td><td>1770</td><td>Infrared</td></tr><tr><td>H</td><td>1.65</td><td>0.35</td><td>7×10-10</td><td>636</td><td>Infrared</td></tr><tr><td>K</td><td>2.20</td><td>0.40</td><td>3.9 ×10-10</td><td>629</td><td>Infrared</td></tr><tr><td>L</td><td>3.40</td><td>0.55</td><td>8.1 ×10-11</td><td>312</td><td>Infrared</td></tr><tr><td>M</td><td>5.0</td><td>0.3</td><td>2.2 ×10-11</td><td>183</td><td>Infrared</td></tr><tr><td>N</td><td>10.2</td><td>5</td><td>1.23 × 10-12</td><td>43</td><td>Infrared</td></tr><tr><td>Q</td><td>21.0</td><td>8</td><td>6.8 ×10-14</td><td>10</td><td>Infrared</td></tr></table>

In practice, any measurement necessarily includes some finite band of wavelengths, possibly characterised by a transmission filter $t _ { 0 } ( \lambda )$ , and this explains why there exist several magnitude systems, depending on the choice of spectral bands. The magnitude $m _ { \lambda _ { 0 } }$ of a source producing a monochromatic flux $e ( \lambda )$ is then

$$
m _ { \lambda _ { 0 } } = - 2 . 5 \log \int _ { 0 } ^ { \infty } t _ { 0 } ( \lambda ) e ( \lambda ) { \mathrm d } \lambda + 2 . 5 \log \int _ { 0 } ^ { \infty } t _ { 0 } ( \lambda ) { \mathrm d } \lambda + q _ { \lambda _ { 0 } } .
$$

Table 3.2 gives the reference intensities $q _ { \lambda _ { 0 } }$ and the central wavelengths $\lambda _ { 0 }$ for the photometric magnitude system, which makes the best use possible of the atmospheric transmission windows in the near UV, the visible, and the near and mid-infrared. The use of magnitude systems to measure fluxes is indeed limited to these three spectral ranges, for historical reasons.

The functions $t _ { 0 } ( \lambda )$ , centred on $\lambda _ { 0 }$ , can be found in AQ. See also Low F., in Methods of Experimental Physics, Vol. 12A. Photographic visual magnitudes differ from those given in the table; the associated functions $t _ { 0 } ( \lambda )$ are chosen to represent the sensitivity of the eye or photographic plates as closely as possible.

The photometry of a source, sometimes obtained through the Earth atmosphere, sometimes from space, uses filters optimised for these different conditions (chromatic sensitivity of the detector, atmospheric absorption bands to be eliminated, etc.). The various magnitude systems have sought to optimise the choice of bands, while new observing conditions, e.g., space, can lead to new systems being devised, which must then be matched up with the previous ones via a form of absolute calibration — the star Vega as primary standard, with which a whole series of secondary standards can subsequently be associated. The proliferation of magnitude systems up until the year 2000 can also lead to a certain confusion, and difficulties in going from one system to another.

In 2007, a more intrinsic definition of magnitudes was gradually introduced, based on (3.1):

• Space Telescope Magnitude (STMAG). If the flux unit is $e _ { \lambda }$ , hence given per wavelength interval with units $\mathrm { ~ W ~ m ~ } ^ { - 2 } \mu \mathrm { m } ^ { - 1 }$ , the STMAG magnitude (used for observations by the Hubble Space Telescope) is defined by

$$
m _ { \lambda } = - 2 . 5 \log _ { 1 0 } e _ { \lambda } - 1 8 . 6 .
$$

• AB Magnitude. If the flux unit is $e _ { \nu }$ , hence given per frequency interval with units $\mathrm { W } \mathrm { m } ^ { - 2 } \mathrm { H z } ^ { - 1 }$ , the AB magnitude is defined by

$$
m _ { \nu } = - 2 . 5 \log _ { 1 0 } e _ { \nu } - 5 6 . 1 .
$$

This magnitude system is the one used by the Sloan Digital Sky Survey, for example (see Sect. 10.2).

The advantage with these systems is that they allow immediate conversion, whatever the wavelength or frequency, from the magnitude to a monochromatic flux without atmosphere, which is a perfectly well-defined physical quantity.

# Bolometric Magnitude

The apparent bolometric magnitude is a measure of the integral of the monochromatic flux over all wavelengths:

$$
m _ { \mathrm { b o l } } = - 2 . 5 \log { \frac { \displaystyle \int _ { 0 } ^ { \infty } e ( \lambda ) \mathrm { d } \lambda } { e _ { \mathrm { b } } } } , \qquad e _ { \mathrm { b } } = 2 . 5 2 \times 1 0 ^ { - 8 } \mathrm { W } \mathrm { m } ^ { - 2 } .
$$

It thus gives the luminosity, if the source radiates isotropically, if its distance $D$ is known (in parsecs), and if there is no absorption between the source and the observer:

$$
m _ { \mathrm { b o l } } = - 0 . 2 5 + 5 \log D \ - 2 . 5 \log { \frac { L } { L _ { \odot } } } ,
$$

where $L _ { \odot } = 3 . 8 2 7 \times 1 0 ^ { 2 6 } \mathrm { W }$ is the luminosity of the Sun.

# Absolute Magnitude

Apparent magnitude is a measure of the flux received at the Earth. Comparison between sources is made possible by introducing absolute magnitude, which is the apparent magnitude the source would have at a distance of $1 0 \ \mathrm { p c }$ (where $1 \ \mathrm { p c } = \ 3 . 0 8 6 \times 1 0 ^ { 1 6 } \ \mathrm { m } = 3 . 2 6 1$ light years), correction being made for any D  Dinterstellar absorption effects (reddening, denoted by $A$ ). The relation between apparent magnitude $m$ and absolute magnitude $M$ of an object at distance $D$ is

$$
M = m + 5 - 5 \log D - A .
$$

Colour Indices

Quantities like $\mathrm { U - } \mathbf { B }$ and $\mathrm { V - K }$ , and more generally, differences $m _ { \lambda _ { 2 } } - m _ { \lambda _ { 1 } }$ , are   called colour indices. They measure the ratio of fluxes at two different wavelengths.

The quantities $q _ { \lambda _ { 0 } }$ are chosen so that all the colour indices beyond the $\mathrm { v }$ band of a star with spectral type A0 (dwarf) are zero. Explicitly, for a high temperature blackbody, whose spectrum thus obeys the Rayleigh–Jeans law $( B _ { \lambda } \propto \lambda ^ { - 4 }$ ) in the UV, the visible, and the infrared, the colour indices are

$$
\begin{array} { r l r } & { \mathbf { B } - \mathbf { V } = - 0 . 4 6 , } & { \mathbf { U } - \mathbf { B } = - 1 . 3 3 , } \\ & { } & \\ & { \mathbf { V } - \mathbf { R } , } & { \mathbf { V } - \mathbf { I } , } & { \ldots , } & { \mathbf { V } - \mathbf { N } = 0 . 0 . } \end{array}
$$

By comparing colour indices, the fluxes at two wavelengths can be related using this reference spectrum, and the spectral slope or colour of the emitted radiation can be calculated (Fig. 3.7). The colour index is extremely useful for classifying large numbers of sources or stars, observed in sky surveys, into different types of objects.

![](images/79dbf0c3221ea0072390171f10ea232fc5622ef6fa6ec53ec8ec303b6a89ec0d.jpg)  
Fig. 3.7 Colour indices. The figure shows the fluxes $e _ { \lambda }$ of three sources: a greybody source, whose spectrum has the same slope as a blackbody of infinite temperature, a blackbody source of temperature $T$ , and a source of temperature $T$ and variable emissivity $\mathcal { E } ( \lambda )$ . The colour indices $\mathrm { U - B }$ and $_ { \mathrm { K - L } }$ are also shown

In the Hertzsprung–Russell diagram, the colour index $\mathrm { B - V } ,$ , which defines a colour temperature for the star, is plotted as a function of the absolute magnitude $M _ { \mathrm { v } }$ , which itself is directly related to the luminosity $L$ .

# 3.4 Photometry Through the Atmosphere

Even at wavelengths for which the atmosphere is almost transparent (see Sect. 2.2), there is nonetheless a modification of radiation measured at ground level. An extinction correction must be applied. This is straightforward, provided the atmosphere can be modelled as a set of parallel-plane absorbing layers, with absorption coefficient $k _ { \nu } ( z )$ . If the line of sight makes an angle $\alpha$ to the zenith, and the incident intensity is $I _ { \nu _ { 0 } }$ , the transmitted intensity can be calculated from

$$
I _ { \nu } ( \alpha ) = I _ { \nu _ { 0 } } \exp \left[ - \sec \alpha \int _ { 0 } ^ { \infty } k _ { \nu } ( z ) \mathrm { d } z \right] ,
$$

where the quantity sec $\alpha = 1 / \cos \alpha$ is called the air mass. If the atmosphere Dis stable in time, measurements made at different zenith angles and plotted on a graph of $\log { I _ { \nu } ( \alpha ) }$ against $\operatorname { s e c } \alpha$ will lie on a straight line Bouguer’s line. Extrapolating this line to zero air mass, determines the intensity outside the atmosphere. The assumptions of temporal stability and horizontal stratification often fail, and precision photometry at ground level becomes a difficult exercise. This is particularly true in the infrared, affected by the considerable lack of homogeneity in the space and time distribution of water vapour, its principal absorber. Clearly, precision photometry is improved by measurements made in space, and indeed, these measurements are the only ones possible at wavelengths which are totally absorbed by the Earth’s atmosphere. With great care, a photometric accuracy of one thousandth of a magnitude can be achieved.

Measurement conditions in space are excellent, since variations in atmospheric extinction are eliminated, and also because objects can be followed over longer periods of time. Space missions observing stars, their variability, and especially their oscillations (asteroseismology), such as the Corot mission of the French space agency CNES in 2006 (see Sect. 9.4) or NASA’s Kepler mission, can achieve a photometric accuracy of $2 \times 1 0 ^ { - 7 }$ on a star of magnitude $m _ { \mathrm { v } } = 8$ , or of $5 \times 1 0 ^ { - 6 }$ on a star of magnitude $m _ { \mathrm { v } } = 1 5$ , using a $1 \textrm { m }$ D telescope and an integration time of around one month.

In order to calculate an emitted intensity, correction for interstellar extinction is required. This is an important correction, demanding an astrophysical interpretation of the measurements (for example, direction of the line of sight relative to the galactic plane), and goes beyond the present discussion.

# 3.5 Calibration and Intensity Standards

Determining the absolute values of astrophysical quantities in terms of the basic units of power, time, frequency, and so on, is a fundamental and difficult problem for observational astronomy: it is fundamental because the consistency of the physical models depends on these values; and difficult because astronomical instruments are complex machines, observing in conditions which are often hard to reproduce, whereas, in the laboratory, reference standards are permanently available and highly controllable.

Calibration can be divided into several categories:

• Energy calibrations, in which the aim is typically to measure a specific intensity $B _ { \nu } ( \theta )$ , as a function of the angular position $\theta$ of the source, and at a given frequency . The techniques of energy calibration vary enormously with wavelength, and will be reviewed below for each of the main spectral regions. Spectral calibrations, in which the aim is to establish the absolute frequency of observed spectral lines. This will be discussed briefly, in the context of each of the main spectral regions, since techniques vary once again. Angular calibrations, in which the aim is to find the absolute angular positions of a set of reference sources, and then determine the angular position of a given source relative to these. This is astrometry, dealt with in Chap. 4. Time calibration, or chronometry, in which the aim is to time the variations of a source (for example, a pulsar).

# 3.5.1 Radiofrequencies

We take this to mean the wavelength range $\lambda \gtrsim 0 . 5 \mathrm { m m }$ . The calibration standard is the blackbody, whose intensity is given by the Rayleigh–Jeans approximation, which is normally valid for the temperatures under consideration:

$$
B _ { \nu } \approx { \frac { 2 \nu ^ { 2 } } { c ^ { 2 } } } k T .
$$

We will see later (see Sect. 7.5) that radiofrequency detectors are limited to a coherence ´etendue $A \varOmega = \lambda ^ { 2 }$ , and only detect one polarisation of the field.

Method One

Consider a receiving antenna totally immersed in blackbody radiation at temperature $T$ . Assuming its response to be a box function $\Pi ( \nu / \Delta \nu )$ , the power detected in the frequency interval $\Delta \nu$ is

$$
P = \frac { 1 } { 2 } \int _ { 4 \pi } \int _ { 0 } ^ { \infty } B _ { \nu } ( \theta ) \mathrm { d } \nu \mathrm { d } \omega = k T \Delta \nu .
$$

Measuring $\Delta \nu$ and $T$ now calibrates the receiver output voltage. For this method, the Earth’s surface can be used as the blackbody source $T \approx 3 0 0 ~ \mathrm { K }$ , emissivity $\approx 1 \dot { }$ ), the radiotelescope being pointed at the ground to carry out calibration.

Method Two

The receiver is disconnected from the antenna and linked to a noise source; a resistance $R$ at temperature $T$ generates a randomly fluctuating signal. The available electric power is given by the average value of the square of the instantaneous voltage across $R$ caused by the thermal noise (Sect. 7.2.2):

$$
P = \frac { \langle V \rangle ^ { 2 } } { R } = \frac { 4 k T R \Delta \nu } { R } = 4 k T \Delta \nu .
$$

If the resistance is matched to the entry impedance $Z$ of the receiver (i.e., $R = Z$ ), the received power is $2 k T \Delta \nu$ D. A measurement of the transmission of the antenna, taking into account the imperfect reflectivity of the telescope surface, and waveguide losses between focus and detector, is required to complete calibration. Systematic error can be reduced by carrying out a differential measurement using sources at different temperatures, one of which is cryogenic.

Method Three

The voltage $V ( t )$ across a resistance fluctuates randomly, and with white spectral density if $h \nu < k T$ (see Sect. 7.2.2). Any other voltage with the same features can be used for calibration, the result being all the more precise as the signal is stronger. A noise generator can provide a random voltage $V ( t )$ with spectral density roughly constant over the frequencies used, and such that $\langle V ( t ) \rangle = 0$ . This generator could h i Dbe a noise diode, in which the passage of a current produces a randomly fluctuating voltage, or a discharge tube, in which a discharge in a gas produces a high electron temperature and, consequently, a random electric field. Such sources do not have a well-defined thermodynamic temperature but, in so far as they are stable in time, they do provide convenient secondary standards, once calibrated themselves relative to some reference blackbody.

# Spectral Calibration

The availability of a signal in the form of an electrical oscillation in a waveguide, a cavity, or a circuit, allows direct comparison with the clocks or oscillators providing

frequency standards; and these are directly linked to the measurement of time (see Chap. 4), and hence to the frequency unit, the hertz. These frequency calibrations are therefore extremely accurate.

# 3.5.2 Submillimetre, Infrared, and Visible

# Absolute Photometric Calibration

Blackbody radiation is the main standard in this domain. The source temperature must be higher as the wavelength is shorter, for the intensity decreases exponentially at wavelengths below that corresponding to the maximum of the Planck function, and this would make the source too weak and introduce inaccuracies. The maximum of $B _ { \lambda } ( t )$ occurs for $\lambda = \lambda _ { \mathrm { m } }$ , where

$$
\lambda _ { \mathrm { m } } T = 2 8 9 8 \mu \mathrm { m } \mathrm { K } .
$$

In a calibration setup, the power received by the detector is

$$
P = \iiint \mathcal { E } ( \lambda ) B ( \lambda , T ) t ( \theta , \boldsymbol { r } , \lambda ) \mathrm { d } \lambda \mathrm { d } \theta ,
$$

where $\mathcal { E } ( \lambda )$ is the emissivity of the reference source, $t ( \pmb \theta , \pmb r , \lambda )$ the transparency and/or spectral transmission of the instrument, defined by its diaphragms, its beam geometry, its filters, and the spectral reflectivity of the mirrors. $r$ is a variable defining a point of the surface $S$ of the pupil, and $\pmb \theta$ the direction of the radiation. Each of these quantities must be determined to great accuracy, using spectroscopic techniques (Chap. 8).

Temperature

A precise determination can be made using standard methods of pyrometry, for example, thermocouples or optical pyrometry. Relay calibration by lamps with ribbon filaments can be used.

Emissivity

The quantity $\mathcal { E } ^ { \circ } ( \lambda )$ depends on the geometry of the source, and the type of material constituting the filament or the emitting cavity. The exact determination of $\mathcal { E } ( \lambda )$ remains the main source of uncertainty in absolute infrared calibrations, whereas uncertainty over temperature measurements dominates in calibration at visible wavelengths.

![](images/cb0b8695c81d8d44214dedd95a2c503891c24a07963264ae6abdc990b00fb6fd.jpg)  
Fig. 3.8 Sidelobes of a radiotelescope. The source is in the direction $\pmb \theta$ , but a non-zero power is nonetheless received from the direction $\pmb \theta - \pmb \theta _ { 2 }$ (thermal emission from the ground)

Beam Geometry

This comes in through the term $t ( \pmb \theta , \pmb r , \lambda )$ . At short wavelengths $( \lambda \lesssim 5 ~ \mu \mathrm { m } )$ , for which the sizes of optical elements are large in comparison, diffraction barely enters the definition of $t$ , and it can be considered as resulting wholly from geometric considerations, such as the sizes of diaphragms, distances, and so on. This is no longer the case in the mid-infrared and submillimetre regions, where diffraction produces sidelobes. The detector then receives power from other directions than the line of sight (Fig. 3.8). The radiation pattern is the polar representation of the relative sensitivity of the detector as a function of $\pmb \theta$ .

This phenomenon is particularly awkward for very low temperature detectors, when the observed source is very faint, whereas the surroundings of the detector, for example, the mirror of the telescope, emit significant power because of their higher temperature, thus making a non-negligible contribution to the signal. Absolute calibration methods for spaceborne submillimetre telescopes, e.g., the WMAP or Planck missions (see Sect. 7.4.7), have come a long way since 1990, stimulated by the difficulties involved in accurate measurement of the cosmological blackbody radiation.

Apodisation methods can reduce the diffraction lobes and bring the effective etendue closer to the geometric value. (See, for example, Born and Wolf, ´ Principles of Optics, and also the discussion on diffraction by pupils in Sect. 6.6 and Problem 8.1.)

Synchrotron radiation sources are becoming increasingly available and could soon be used in the submillimetre to visible regions instead of blackbodies. They are already the classic calibration source at higher energies, as described in Sect. 3.5.3.

# Relative Calibration

Absolute calibration implies the use of a standard source, something which is not always easily available during observation. Secondary standards, such as stars or reference objects, are then used. These are assumed to be constant in time and are more accessible during an observing sequence.

![](images/967b60b60152d144eb1c8e6ea13dec3e67c95aa6485e5e870ab12264ec3ff072.jpg)  
Fig. 3.9 Absolute flux of the star Vega, in the visible and near infrared regions, after various authors (Tug et al., Oke and Schild, Kharitonov, Glushneval)

Visible

This is the region $0 . 3 \leq \lambda \leq 0 . 7 \mu \mathrm { m }$ . The reference object is the star Vega $\scriptstyle { \alpha }$ Lyrae), whose absolute spectrum is shown in Fig. 3.9. Note the non-negligible fluctuations caused by uncertainties of measurement. Using the functions $t _ { 0 } ( \lambda )$ which come into the definitions of magnitudes, the spectrum gives the magnitudes of Vega, and thus by comparison (flux ratios), the magnitudes of other stars. The Sun is rarely used as a secondary standard, its brightness being too great for the dynamic range of most detectors.

Absolute stellar photometry can reach an accuracy of 0.001 magnitudes in the visible.

Near Infrared

This region $( \lambda \lesssim 3 0 ~ \mu \mathrm { m } )$ ) is observable from ground level. A series of stars has been chosen as secondary standards, and their fluxes have been determined in the following way:

• It is assumed that the absolute solar flux has been precisely measured in the range 1 to $2 5 ~ { \mu \mathrm { m } }$ . As an example, Fig. 3.10 shows the determination of the specific intensity of the Sun.2 This measurement results from a comparison of the solar flux with the standards discussed above. Having fixed the constants $q _ { \lambda _ { 0 } }$ of the magnitude scale, the colour indices of the Sun can be calculated.

![](images/8d0736e86c45d1bd28e463b44e7bdbc1977f15d0eff060aa3322a77af1522981.jpg)  
Fig. 3.10 Observational determination of (a) solar brightness (expressed in terms of brightness temperature $T _ { \mathrm { B } }$ ) in the far infrared, and (b) monochromatic flux from the centre of the disk (quiet region) in the ultraviolet. The continuous curve shows the prediction of solar atmosphere models. Note the scatter of the measurements even for an object as intense as the Sun. (After Vernazza J. et al., Ap. J. 184, 605, 1973. With the kind permission of the Astrophysical Journal)

• A series of reference stars is chosen, having a similar spectral type to the Sun (G0 to G4), and whose infrared spectra are assumed to be strictly proportional to that of the Sun.

This assumption implies another, namely that these stars are not surrounded by dust clouds, whose thermal emission in the near infrared would add to that of the photosphere of the star. The existence of a zodiacal nebula around stars, which have been assumed to be ‘naked’ up until recently, has been demonstrated in the case of Vega $\scriptstyle ( { \alpha }$ Lyr), and indeed a certain number of other stars (e.g., $\beta$ Pictoris, Polaris, Fomalhaut, etc.).

The magnitude V of these stars is measured, for example, by comparison with $\alpha$ Lyr, and their magnitudes R, : : :, Q can be deduced.

• This intermediate series of stars is then compared with bright stars, in order to establish secondary standards with a good signal-to-noise ratio. These standards should be well placed in the sky, at small zenith distances, and accessible at any time. Their spectral type is arbitrary and their magnitudes R, : : :, Q are determined by comparison with the previous series.

Far Infrared

This is the region $3 0 ~ { \mu \mathrm { m } } ~ \lesssim ~ \lambda ~ \lesssim ~ 0 . 5 ~ \mathrm { m m }$ , which is observed from above the atmosphere. There are no standard spectral bands for normalising measurements, and so the literature gives values of the monochromatic fluxes $B ( \lambda )$ of sources, or else the flux in jansky when the source is limited in spatial extent or unresolved by the observation.

Observations made from aircraft or balloons use the intrinsic radiation of the planets as a secondary standard. Planetary radiation is assumed identical to that of a blackbody with a brightness temperature $T ( \lambda )$ in the spectral region considered, and $T ( \lambda )$ is found by independent comparison with a standard blackbody.

The brightness temperature of a planet is a function of wavelength. The approximate values given in Table 3.3 are valid to within $10 \%$ for the far infrared, and are improved with each space exploration mission.

Table 3.3 Brightness temperatures of the planets, for $5 0 \lesssim \lambda \lesssim 5 0 0 \mu \mathrm { m }$   

<table><tr><td></td><td>TB()</td></tr><tr><td>Venus</td><td>255K</td></tr><tr><td>Mars</td><td>235K</td></tr><tr><td>Jupiter</td><td>145K</td></tr><tr><td>Saturn</td><td>85K</td></tr></table>

The sensitivity of a spaceborne telescope is greatly superior, and the planets are too bright, or sometimes too extended in space, to be used as standard sources. Calibration proceeds in several steps. First, an absolute internal standard is provided on board, by a blackbody whose emissivity has been calibrated before the launch, and whose temperature is maintained at an accurately known value. Such is the case for the instruments on board the satellite ISO (1995), and also for the Spitzer observatory (2004), named after the astrophysicist Lyman Spitzer and dedicated to the near and far infrared, with a cooled telescope of diameter $0 . 8 5 \mathrm { ~ m ~ }$ (see Sect. 5.2.3).

The next step is the observation of asteroids. The dimensions of these objects are known, as are their brightness temperatures and their emissivities. Indeed, these quantities are relatively easy to model, depending on the mineralogical composition of the asteroid and its distance from the Sun. Magnitudes and fluxes can thus be determined at any wavelength.

During the mission it is also necessary, in order to better establish such a calibration, to use a standard star which is simultaneously observable from the ground, and hence well calibrated. The star $\alpha$ Tau has been used in this way as a ‘photometric relay’ at $\lambda = 1 2 \mu \mathrm { m }$ for calibration of the satellite IRAS (1983). In the range $2 { \mathrm { - } } 4 2 \mu \mathrm { m }$ D, the Spitzer mission (2004) uses a set of standard stars whose synthetic spectra (at a resolution of 1 200) have been calculated on the basis of everything we now know about these stars.

# Spectral Calibration

In the visible, this calibration is carried out using spectral lamps (thorium, for example) which emit lines at very precisely known wavelengths. Certain spectroscopic techniques (see Chap. 8) provide an absolute measurement of wavelengths, either by comparison with lasers (Fourier spectrometers), or by comparison with the atomic emission line of a gas (resonance cells, see Sect. 8.5). In the near infrared, the atmospheric emission lines of the radical OH provide a good standard for groundbased observations. Beyond, the instrument must be pre-calibrated using a laser standard, for example, with many lines (see Chap. 8).

# 3.5.3 Ultraviolet and X Rays

Use of blackbodies becomes more difficult in this region $( 0 . 1 ~ \lesssim ~ \lambda ~ \lesssim ~ 3 0 0 ~ \mathrm { n m } )$ , where very high temperatures are required to obtain an acceptable brightness. Inaccuracy in temperature measurements limits the feasibility of absolute calibration using thermal sources in these spectral regions. On the other hand, the availability of synchrotron radiation sources, which are non-thermal, provides an accurate and reliable method of absolute calibration for UV and X-ray instrumentation. In either case, calibration is made easier by the absence of interfering radiation from the environment, which is so harmful in the infrared region.

# Thermal Sources

These are considered in two wavelength regions.

The Region 100–300 nm

It is possible to produce very hot plasmas ${ T } \approx 1 4 0 0 0 { \mathrm { K } } )$ whose temperature is nevertheless accurately known $( \sim 2 \% )$ . On experimentally accessible length scales l $_ { 1 - 1 0 \mathrm { c m } }$  in Ar), this plasma is only optically thick in the resonance lines of the gas atoms, viz., the Ly˛ line $( 1 2 1 . 5 \mathrm { n m }$ ) of hydrogen, N II lines ( $1 0 8 . 5 \mathrm { n m }$ ), and various lines of $\mathrm { ~ C ~ I , ~ K r ~ I ~ }$ , and so on.

In these lines, the emitted intensity

$$
I _ { \lambda } = B _ { \lambda } ( T ) \left[ 1 - \exp ( - \kappa _ { \lambda } l ) \right]
$$

is very close to that of a blackbody $B _ { \lambda } ( T )$ , if the optical depth $\kappa _ { \lambda } l$ is larger than unity. Nevertheless, with $\Delta T / T \sim 2 \times 1 0 ^ { - 2 }$ , we still have $\Delta B / B = 0 . 2$ , which is far from ideal.

# The Region 0.1–100 nm

Optically thick sources can no longer be created and the idea of using blackbody radiation to calibrate instruments must be abandoned. Instead, the thermal free–free emission of a hot and optically thin plasma can be used. The power radiated per unit volume of plasma (volume emissivity) is

$$
\mathcal { E } _ { \nu } = 6 . 3 6 \times 1 0 ^ { - 4 7 } N _ { \mathrm { i } } N _ { \mathrm { e } } Z ^ { 2 } g ( \nu , T ) \frac { \exp ( - h \nu / k T ) } { ( k T ) ^ { 1 / 2 } } \quad \mathrm { W m } ^ { - 3 } \mathrm { s r } ^ { - 1 } \mathrm { H z } ^ { - 1 } ,
$$

where $N _ { \mathrm { i } }$ and $N _ { \mathrm { e } } \ [ \mathrm { c m } ^ { - 3 } ]$ are the ion and electron number densities, respectively, $Z$ the ionic charge number, and $g ( \nu , T )$ the Gaunt factor. (The radiation emitted by a hot plasma is given in AF, Sect. 1.30, and also in AQ, Sect. 43, where a table of Gaunt factors can be found.)

This plasma is created in a pulsed discharge tube, where the temperature reaches $T = 1 . 5 \times 1 0 ^ { 6 } \mathrm { K }$ , and the electron density $N _ { \mathrm { e } } = 2 \times 1 0 ^ { 1 7 } \mathrm { c m } ^ { - 3 }$ . Initial ionisation is D  D achieved by applying a radiofrequency field which preheats the discharge. Heating then results from compression of the matter by an intense magnetic field $( 0 . 5 ~ \mathrm { T } )$ . Electromagnetic emission only lasts for a few microseconds.

![](images/4692ec9e72414902816581ba8e906802cf03c75260c6d8a6727926d93f97130f.jpg)  
Fig. 3.11 Spectral distribution of synchrotron radiation from an electron in a magnetic field. (Lang K.R., Astrophysical Formulae)

# Non-Thermal Sources: Synchrotron Radiation

Synchrotron radiation is emitted by relativistic electrons accelerated in a magnetic field, and its easily quantifiable and reproducible character makes it a useful calibration standard.

The radiation emitted by an electron of energy $\mathcal { E }$ , orbiting in a magnetic field $B$ is concentrated around a frequency $\nu _ { \mathrm { m } }$ given by3

$$
\nu _ { \mathrm { m } } = \frac { e B } { 2 \pi m _ { \mathrm { e } } } \left( \frac { \mathcal { E } } { m _ { \mathrm { e } } c ^ { 2 } } \right) ^ { 2 } ,
$$

where $m _ { \mathrm { e } }$ is the mass of the electron. Figure 3.11 shows how the spectrum is distributed around $\nu _ { \mathrm { m } }$ . The radiated power is given by

$$
\mathrm { d } P ( \nu ) = \frac { 1 6 e ^ { 3 } B c } { 4 \pi \varepsilon _ { 0 } m _ { \mathrm { e } } c ^ { 2 } } p ( \nu / \nu _ { \mathrm { m } } ) \mathrm { d } \nu .
$$

The radiation is directional, in a narrow cone with axis along the tangent to the electron trajectory, and opening angle $2 \theta$ given by

$$
\theta ( \mathrm { r a d } ) \simeq \frac { m _ { \mathrm { e } } c ^ { 2 } } { \mathcal { E } } = \frac { 0 . 5 1 1 } { \mathcal { E } [ \mathrm { M e V } ] } .
$$

Although synchrotron radiation is particularly suitable in the UV and X-ray regions, it also provides an excellent calibration source in the visible and near infrared, in view of its precise directionality.

Since the mid-1990s, many synchrotron radiation sources have become available, e.g., the European Synchrotron Research Facility (ESRF) (Grenoble, France), DORIS (Hamburg, Germany), Brookhaven (New York, USA), Tsukuba (Japan), Daresbury (Great Britain), and Argonne (Chicago, USA). To give some idea of the values of the parameters, the ESRF provides a beam with $\theta \ : = \ : 0 . 1$ mrad and intensity reaching between $1 0 ^ { 1 4 }$ and $1 0 ^ { 1 8 }$ photons $\mathrm { { s } } ^ { - 1 } \mathrm { { m m } } ^ { - 2 } \mathrm { { m r a d } } ^ { - 2 }$ Dspectral interval 1. The spectral interval at an energy $E$ is of the order of $\Delta E / E \approx 1 0 ^ { - 3 }$ . It is also possible to produce $\gamma$ radiation from synchrotron electrons, using the inverse Compton effect on a laser beam. $\gamma$ radiation with well-defined spectral properties is obtained, in the range $1 { \mathrm { - } } 1 . 5 \operatorname { G e V } .$

# 3.5.4 Gamma-Ray Radiation

In this region, detectors always function in counting mode, and with two possible objectives: an energy calibration of each photon (spectrometry), and some measurement of the efficiency of detection (photometry).

At low energies $\mathbf { \zeta } < 2 \mathbf { M e V } ,$ ), the reference standards are radioactive samples with known emission (for example, $^ { 6 0 } \mathrm { C o }$ , which emits lines at 1.17 and $1 . 3 3 \mathrm { M e V }$ ), and whose activity has been calibrated.

In the case of photometry, there are two problems worth noting with radioactive calibration sources. To begin with, the activity of these radioactive sources is not generally known to better than a few percent. Furthermore, for sources with a short half-life, less than 10 yr, the activity of the source must be regularly updated. Indeed, when the half-life is very short, say less than a week, the decay of the source must be taken into account during its use.

At high energies, particle accelerators are used. Once again, the accuracy obtained in photometry is barely better than a few percent.

Calibration of instruments can also be carried out in flight (on balloons, or in space), for the response of an instrument may evolve in time, particularly after launching. Photometric calibration can be made by observing some stable reference object of known spectrum (the Crab Nebula, for example); and spectral calibration can be carried out by observing emission lines from radioactive de-excitation, either of sources intentionally placed aboard, or of the material of the instrument itself, activated by radiation received in orbit.

# 3.5.5 Some Examples of Spectrophotometry

Determining the specific intensity of a source with spatially limited extent, in various wavelength ranges, requires very diverse instrumental techniques. Accuracy of calibration itself varies with wavelength. Putting together all the observations produces a global spectrum of the object, and this is the only way to penetrate the underlying physics of the processes involved. A few examples are given here.

# The Sun

It would be easy to imagine that the absolute spectrophotometry of such a close and bright object would be perfectly established over the whole electromagnetic spectrum. This is not the case, as is shown in Figs. 3.10 and 3.12. Apart from the obvious difficulty in obtaining measurements of $\lambda E _ { \lambda }$ which cover eighteen powers of ten, the definition of a uniform flux over time is made impossible in certain spectral domains, by the variability of the Sun in those domains. The same remark applies equally to most stars, or other astrophysical objects, and consequently, it is rare for some improvement in photometric accuracy not to reveal a variability in the luminosity of objects which were previously supposed to be stable.

# Extragalactic Radiofrequency Sources

Determining the spectrum of an object across a wide range of frequencies is essential in order to understand the physical origins of the radiation which it emits; for example, to establish whether it is thermal or non-thermal. The difficulty here comes from the fact that the sources are distant and weak, requiring long integration times, and thus opening the way to all kinds of interference from the atmosphere, or from internal fluctuations of the instrument, which can modify any initial calibration. Figure 3.13 gives several examples of absolute photometry of extragalactic sources, from which either thermal or non-thermal spectra can be attributed to them.

# Cosmological Background Radiation

The great difficulty involved in measuring this radiation provides a remarkable illustration of the accuracy which can be achieved in absolute spectrophotometry, and also of the fundamental consequences that these measurements can have for astrophysics. The satellite COBE (COsmic Background Explorer, 1989) carried an absolute spectrophotometry instrument (FIRAS), comprising a Michelson interferometer, followed by bolometric detectors, with the aim of determining the spectrum of the cosmological background in the spectral range $0 . 1 \ \mathrm { { m m } } \ < \lambda < 1 0 \ \mathrm { { m m } }$ . Absolute calibration was carried out using an internal thermal radiation source, approximating a blackbody in this range by an emissivity better than 0.9999.

After subtracting the intrinsic emission of the Galaxy, also detected by the instrument and suitably modelled, the spectrum of the cosmic background can be calculated. A best fit over $0 . 5 \ \mathrm { m m } < \lambda < 5 \ \mathrm { m m }$ is obtained with a blackbody of temperature $T = 2 . 7 2 6 \pm 0 . 0 1 0 \mathrm { K } .$ Across this range, the greatest deviation from D ˙the Planck spectrum is only $0 . 0 3 ~ \%$ , a quite exceptional accuracy, achieved in extremely difficult experimental conditions.4 In 2007, not only was the accuracy of these measurements improved, but a detailed map of the spatial fluctuations of this radiation was established by NASA’s WMAP mission (2000). This in turn will be improved by the European Planck mission (2008), discussed in Sect. 7.4.7.

![](images/beec02ea77d55e4eed77c7a9096612bda2982de535594e27f0e266306c345e35.jpg)  
Fig. 3.12 Composite view of the integrated radiation from the solar disc. The monochromatic flux outside the Earth’s atmosphere is plotted as a function of wavelength. The temperature of various blackbodies is given. The symbol $\odot$ denotes the Sun. (After White O.R., The Physical Output of ˇthe Sun, Boulder, 1976. With the kind permission of Boulder Press, CO)

![](images/897fbf29533ef8da80fe3570bbdbe0e8932224b60d6876b3ff74fdf9ef715bb8.jpg)  
Fig. 3.13 Photometry in the radio region: the radio source Cassiopeia A (synchrotron radiation); the thermal bremsstrahlung source of the Orion Nebula (H II region); the galactic nucleus NGC 1275, which has a partly thermal and partly synchrotron spectrum at low frequency. (After Lang K.R., Astrophysical Formulae. The figure collects the results of several authors.) Note the model indicated by continuous curves, measurement points, and error bars. (With the kind permission of the publisher)

# 3.6 Calibration of Angular Dimensions

With the advent of very high angular resolutions, which can range from the millisecond of arc to the microsecond of arc $( 5 \times 1 0 ^ { - 1 2 }$ rad) thanks to optical and radio interferometers (see Sect. 6.4), it has become necessary to be able to specify an unresolved source on this same scale. This is then called a point source, with the understanding that it is a point source for the given instrument. Indeed, when such an instrument measures the visibility of the source at a given spatial frequency, the observation mixes instrumental effects, discussed in detail in Chap. 6, and spatial properties of the object, e.g., if it is a star, its angular diameter and its centre–limb darkening.

To distinguish the two parameters, we must be able to observe, with the same instrument and under like conditions, a source that can be considered as known spatially, i.e., in practice, as unresolved or pointlike (having very small dimensions compared with the resolution of the instrument). A perfect solution would be to use the disk of a distant star, observed at visible wavelengths (radiation from the photosphere), but its magnitude will generally be too faint to be observable. If for instance we were to choose a star of the same type as the Sun, and if we required its angular diameter to be less than $1 0 0 ~ \mu$ arcsec, it would have to be at a distance of $1 0 ~ \mathrm { k p c }$ , and its magnitude (V) would then be around 19, much too faint for the sensitivity of the interferometer.

The solution to this problem in 2007 is to use less remote stars, hence partially resolved, but for which the center–limb darkening, and more generally the photospheric brightness distribution, can be considered as sufficiently well modelled to allow calibration of the interferometer. In the near-infrared, the problem is complicated by the possible, but not necessarily known, presence of circumstellar material which emits radiation and may be modifying the observed spatial structure.

# Problems

3.1. Colour Indices. Table 3.4 gives the colour indices of main sequence stars. Find the colour temperature of the various spectral types (that is, the temperature of the blackbody with the most similar spectrum in a given wavelength interval). For simplicity, represent each band by its central wavelength.

Answer. A blackbody at temperature $T$ has colour index

$$
\mathrm { V - L } \left( T \right) = \mathrm { c o n s t a n t } _ { \mathrm { V L } } - 2 . 5 \log \frac { B ( \lambda _ { \mathrm { V } } , T ) } { B ( \lambda _ { \mathrm { L } } , T ) } ,
$$

where $\lambda _ {  { \mathrm { V } } }$ and $\lambda _ { \mathrm { L } }$ are the representative wavelengths of the corresponding bands (to simplify). The constant is determined by the requirement that $\mathrm { \Delta V - L = \Omega 0 }$ for a

Table 3.4 Colour indices of main sequence stars   

<table><tr><td>Spectral type</td><td>V-R</td><td>V-I</td><td>V-J</td><td>V-K</td><td>V-L</td><td>V-N</td></tr><tr><td>AO</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>FO</td><td>0.30</td><td>0.47</td><td>0.55</td><td>0.74</td><td>0.80</td><td>0.00</td></tr><tr><td>GO</td><td>0.52</td><td>0.93</td><td>1.02</td><td>1.35</td><td>1.50</td><td>1.40</td></tr><tr><td>KO</td><td>0.74</td><td>1.40</td><td>1.50</td><td>2.0</td><td>2.50</td><td></td></tr><tr><td>MO</td><td>1.10</td><td>2.20</td><td>2.30</td><td>3.5</td><td>4.30</td><td></td></tr><tr><td>M5</td><td></td><td>2.80</td><td></td><td></td><td>6.40</td><td></td></tr></table>

blackbody of infinite temperature. The flux of such a blackbody varies as $\lambda ^ { - 2 }$ so

$$
\mathrm { c o n s t a n t } _ { \mathrm { V L } } = 2 . 5 \times 2 \times \log ( \lambda _ { \mathrm { L } } / \lambda _ { \mathrm { V } } ) = 3 . 9 6 .
$$

From Table 3.4, the colour temperature $T _ { \mathrm { M O } }$ of an MO star satisfies

$$
3 . 9 6 - 2 . 5 \log { \frac { B ( \lambda _ { \mathrm { V } } , T _ { \mathrm { M O } } ) } { B ( \lambda _ { \mathrm { L } } , T _ { \mathrm { M O } } ) } } = 4 . 3 0 ,
$$

which, in turn, implies that $T _ { \mathrm { M O } } = 4 { , } 1 0 0 \mathrm { K }$ .

3.2. A telescope cooled to a very low temperature is used to measure the cosmological background at $\lambda = 1 ~ \mathrm { m m }$ . Calculate the power received in the coherence etendue´ $\lambda ^ { 2 }$ Dper frequency interval $\Delta \nu$ . Calculate also the power received from the Earth, assuming its temperature to be $3 0 0 \mathrm { K }$ , observed at $9 0 ^ { \circ }$ from the principal line of sight (the telescope is in orbit and pointing towards the local zenith). Comparing these two values, deduce the angular rejection needed to make a measurement of the cosmological background, accurate to within $1 \%$ . (The configuration of the diffraction lobes of a pupil can be found in Chap. 6.) Take $D \ = \ 1 0 \ \mathrm { c m }$ for the diameter of the telescope.

3.3. A thermal source (H II region of ionised hydrogen) is optically thick at all wavelengths, and its thermal radiation (bremsstrahlung) is such that $I _ { \nu } = $ constant D(see AF, Sect. 1.30). Given that it radiates 10 mJy at radiofrequencies, calculate its magnitude $\mathrm { m } _ { \mathrm { v } }$ at visible wavelengths.

Answer. Firstly, the radiation from the source satisfies

$$
I _ { \nu } = 1 0 \mathrm { m J y } = 1 0 ^ { - 2 8 } \mathrm { W m } ^ { - 2 } \mathrm { H z } ^ { - 1 } ,
$$

for all wavelengths, and in particular, in the visible. Secondly, in the visible

$$
m _ { \mathrm { v } } = - 2 . 5 \log { ( I _ { \lambda } / 3 . 9 2 \times 1 0 ^ { - 8 } \mathrm { W } \mathrm { m } ^ { - 2 } \mu \mathrm { m } ^ { - 1 } ) } .
$$

The link between these two relations is made using

$$
I _ { \nu } \Delta \nu = I _ { \lambda } \Delta \lambda \quad { \mathrm { w h e r e } } \quad \Delta \nu = ( c / \lambda ^ { 2 } ) \Delta \lambda .
$$

Thus, $I _ { \lambda } = 9 . 9 2 \times 1 0 ^ { - 1 4 } \mathrm { W } \mathrm { m } ^ { - 2 } \mu \mathrm { m } ^ { - 1 }$ , and the visible magnitude of the source is $m _ { \mathrm { v } } = 1 4$ .

# Chapter 4 Space–Time Reference Frames

An essential part of astrophysical observation and data analysis consists in measuring the positions of astronomical objects and in dating events. Obtaining the photometric magnitudes of the emitted radiation is not enough. The source must be identified in catalogues or data bases, and the position must be determined to great accuracy, since spatial resolutions of the order of several tenths of a millisecond of arc can now be attained in images, and this trend is certain to continue. Concerning the absolution positioning accuracies of celestial objects, over the past 20 years or so, these have gone from a few hundredths of a second of arc before the Hipparcos satellite was launched to about ten microseconds of arc with the Gaia mission. In terms of sensitivity, detectors can now measure the characteristics of phenomena whose time of variation is less than one millisecond. And further, extremely accurate time scales, taking into account the effects of general relativity, are required for space travel and exploration of specific sites in the Solar System.

This chapter treats the recent progress in astronomical reference systems, first for space and then for time, even though the primary source for time scales is now linked to a phenomenon quite distinct from the Earth’s movement. The notions involved also have important applications for the everyday life of Earthlings like ourselves, e.g., with the advent of GPS or the synchronisation of clocks in transport and telecommunications. The objective is to provide a basis for the space and time coordinates needed in practical calculations that do not aim for accuracies better than a few $0 . 0 1 ^ { \prime \prime }$ for absolute positions. To compare this requirement with past and current performance in astrometry, we need only examine the way accuracies in position and parallax measurements have evolved over time, as shown in Fig. 4.1.

The Hipparchos–Ptolemy catalogue1 as transmitted in the Almagest can be used to calculate true star positions relative to the equator or the ecliptic of that epoch and thereby determine the statistical quality of the measurements. The result is an accuracy of the order of 0.3–0.5 degrees. Figure 4.1 shows a very slow improvement in the accuracy of astronomical pointing. There is a very slight inflexion with the advent of optical instruments toward the end of the seventeenth century. The refracting telescope became available with Galileo2 in 1610, but its use as a sighting instrument came rather later, coinciding with the foundation of the observatories in Paris and Greenwich. Refracting telescopes were above all used to observe faint objects, but that step forward did not necessarily improve direction measurements. Later, progress in mechanical construction and clock-making proved to be just as important in this respect as developments in optics.

![](images/d4f00879cb93dc58529edfea761c65425230d47fb6f835d28e0b0910a106477e.jpg)  
Fig. 4.1 Improving astrometric accuracy in the observations of stars and planets at different epochs

However, the most recent part of the curve is highly instructive and illustrates the significant progress made in astrometry (measurement of positions, proper motions, and parallaxes of heavenly bodies) by virtue of space techniques. While it took about 20 centuries to improve astrometric accuracy by 4 to 5 orders of magnitude, it subsequently took a mere 20 years with Hipparcos, Gaia, and SIM to achieve a similar leap forward. In the end, the DIVA and FAME projects in Germany and the USA, respectively, put forward just after the success of the Hipparcos mission, were never funded.

Modelling requirements depend significantly on the level of accuracy one hopes to achieve, and the degree of difficulty grows rapidly with this accuracy. It is thus essential to adopt the right tools for each situation. It is pointless to use the