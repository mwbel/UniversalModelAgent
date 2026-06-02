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
