# Chapter 7 Detectors

This chapter is concerned with devices used to turn information, transported by the incident energy coming from astronomical sources, into signals which the astrophysicist can study. Such devices are called receivers or detectors.

The terminology depends on which scientific community is using it. Radioastronomers systematically talk about receivers, no doubt due to the traditions in telecommunications, i.e., radio and TV. In the spectral range from infrared to $\mathrm { X }$ rays, the term detector is generally used, in particular to refer to CCDs, which have become the most commonly used detectors, but the word receiver is also possible here. Then in the very high energy range of $\gamma$ radiation, only the term detector is used. Here the terminology has naturally been imposed by the traditions of nuclear physics, where particles are considered to be detected.

In every case, the receiver or detector is of course a subsystem achieving the same objective of transforming the incident electromagnetic radiation into a signal, usually electrical, which can then be measured.

Detectors can be based on profoundly different physical principles, depending on which information carrier is involved. Electromagnetic radiation will clearly be the primary concern, occupying most of the chapter. However, detectors associated with the measurement of neutrinos and gravitational waves will also be examined, for these two areas represent a ‘new astronomy’, with a potential for discovery which, if not for the immediate future, is nonetheless considerable.

Any technical description of the immense variety of detectors used would be rather dull, and would almost immediately become obsolete. Therefore, the present discussion will deal first with general properties, and the main families of physical processes which underlie all detection devices.

The next section will deal with a selection of the main detectors used in astronomy today (2007). These have been classified according to the main wavelength regions, partly because this largely determines the technology, and particle because it determines the range of energies to be detected, bearing in mind that there is a factor of $1 0 ^ { 1 6 }$ or more between the energies of $\gamma$ radiation and radiofrequency waves.

An important aim will be to show how closely practical realisations approach the fundamental limitations due to the statistical properties of the radiation, which are outlined at the beginning of the chapter. This will provide an opportunity to measure the astonishing progress made, particularly in sensitivity, over the last decades of the twentieth century. These developments have often been due to the needs of medicine, defence, and telecommunications, from which astronomy has benefited, without itself being the principal motivation. Lallemand’s1 photomultiplier (1936) shows that this is not a new phenomenon.

Given any observation programme, the experimenter must apply effective criteria in choosing from the great diversity of tools available. For this reason, an attempt will be made to compare the optimal use of the various detectors. In practice, it is often difficult to find the dividing line between the detector itself and the full radiation detection and analysis system, as it was presented in Chap. 1. For example, spectral selectivity can be obtained by using a spectrometer before the detector (see Chap 8), but it can also result from an intrinsic selectivity in the detector itself. Finally, the coupling between the detector and the telescope, or radiation collector, can be improved by using devices such as fibre optics, amplifiers, and the like. Several examples will be given, which will show a marked evolution, as mentioned earlier in the book: an astronomical observing instrument has become an integrated system, whose various components interact closely and contribute together to the overall performance. This point will be taken up again in Chap 9, where several examples will be discussed for instruments in use today.

# 7.1 General Properties

By referring to the detection subsystem of an observing system, a very general expression can be given to represent the signal coming from one detection element of the detector (which may indeed contain a great number of such elements):

$$
x ( t ) = x _ { 0 } ( t ) + f \left[ \int _ { \Delta \nu } \varPhi ( \nu ) \mathrm { d } \nu \int _ { \Delta \varOmega } I ( \theta , \nu , t ) P ( \theta ) \mathrm { d } \theta \right] .
$$

$I ( \pmb \theta , \nu , t )$ is the specific intensity of the radiation arriving at the detector, $P ( \pmb \theta )$ is the angular response of the detector (e.g., field, lobes), and $\varPhi ( \nu )$ is its spectral response. $x _ { 0 } ( t )$ represents any signal delivered by the detector in the absence of an incident signal, and is called the dark signal. The function $f$ can be considered to characterise the input–output relation of the detector. The most favourable situation is one in which this function is linear. $I$ can also be considered as the input intensity of the whole observing system, the functions $P , \phi$ , and $f$ then characterising the complete system, and not just the detector.

If the detector is such that $f ( I ) = 0$ for $I \ < \ I _ { \mathrm { t } }$ , the detector is said to have a sensitivity threshold $I _ { \mathrm { t } }$ . Similarly, if $f ( I )$ is approximately constant for $I > I _ { \mathrm { s } }$ , the detector is said to saturate for $I > I _ { \mathrm { s } }$ (non-linearity).

It has been assumed, for simplicity, that the variables $\pmb \theta$ and $\nu$ do not mix together in the responses $\varPhi$ and $P$ , although this is not always valid (e.g., chromatic effects of diffraction).

# 7.1.1 Amplitude Detectors. Quadratic Detectors

Depending on which physical process is being exploited, a detector may be linear, with respect to the field amplitude, or it may be quadratic, and thereby linear in the power. In the latter case, the phase information required for coherent detection and image formation in interferometry is generally lost (see Chap. 6).

# Amplitude Detectors

This type of detector measures the instantaneous amplitude of the electric or magnetic field of a wave of frequency $\nu$ ,

$$
x ( t ) = \mathrm { R e } \big [ E _ { 0 } \exp ( 2 \pi \mathrm { i } \nu t + \phi ) \big ] \ .
$$

There is therefore an instantaneous linearity between the signal and the amplitude, and this justifies calling it a linear, or a coherent detector, although in a more restricted sense than in the general definition given above. In this way, the antenna of a radio receiver converts the field into a current in the antenna, and this current signal is proportional to the field (Fig. 7.1).

In Sect. 7.5, it will be shown how a quadratic detector can be transformed into an amplitude detector by means of a local oscillator.

# Quadratic Detectors

This kind of detector delivers a signal proportional to the mean power of the wave,

$$
x ( t ) = \frac { 1 } { \Delta T } \int _ { t } ^ { t + \Delta T } E ( t ^ { \prime } ) E ^ { * } ( t ^ { \prime } ) \mathrm { d } t ^ { \prime } = \Pi \left( \frac { t } { \Delta T } \right) \star [ E ( t ) E ^ { * } ( t ) ] .
$$

where $\star$ denotes convolution and the mean is a running mean, taken over a time $\Delta T$ (the integration time) much longer than the wave period. An equivalent relation is

![](images/0aede50e732aadba0e89e7a7ab350fbaf4737d227be3ce66ed91b00ee1931f4e.jpg)  
Fig. 7.1 Conversion of an electric field into a current by a receiving aerial

$$
x ( t ) = \frac { 1 } { \Delta T } \int _ { t } ^ { t + \Delta T } N ( t ^ { \prime } ) \mathrm { d } t ^ { \prime } ,
$$

where $N ( t )$ describes the arrival of photons, which is usually a Poisson process.

The time $\Delta T$ , over which the running mean is taken, defines the temporal passband of the detector. Indeed, the relation giving $\tilde { x } ( f )$ is

$$
\tilde { x } ( f ) = S _ { \mathrm { E } } ( f ) \Delta T \mathrm { s i n c } ( f \Delta T ) ,
$$

which makes the low-pass filtering of incident information explicit, defining an equivalent passband by

$$
\Delta f = \frac { 1 } { \mathrm { s i n c } ^ { 2 } ( 0 ) } \int _ { - \infty } ^ { + \infty } \mathrm { s i n c } ^ { 2 } ( f \Delta T ) \mathrm { d } f = \frac { 1 } { \Delta T } \ .
$$

This type of quadratic detector, also known as a power, or an intensity, or again an incoherent detector, is therefore linear in the incident power (unless it exhibits threshold or saturation effects). These are the most commonly used detectors, operating by detection and/or counting of photons (the eye, photomultipliers, television cameras, channeltron, photoconductor and photovoltaic detectors, photographic plates, scintillators, spark chambers, etc.), and receiving radio diodes (video mode). In the following, an expression of the type

$$
x ( t ) = \left. E ( t ^ { \prime } ) E ^ { * } ( t ^ { \prime } ) \right. _ { ( t - \Delta T / 2 , t + \Delta T / 2 ) }
$$

will be assumed to represent the signal. This is a simplification, because in practice several parameters should be taken into account: the solid angle $\Delta \pmb \theta$ , frequency $\Delta \nu$ , and so on, as already mentioned. The mean $\langle ~ \rangle$ is taken over the interval $\Delta T$ around the instant $t$ .

It is interesting to compare performances within the category of coherent detectors, which necessarily isolate a narrow spectral band $\Delta \nu$ , with those within the category of incoherent detectors, which are not limited in this way. Figure 7.2 illustrates such a comparison, made for the spectral region between $\lambda = 3 ~ \mathrm { m m }$ and $\lambda = 3 0 ~ \mu \mathrm { m }$ D, a region in which both types of detector can be made, using the Dappropriate technology. It can be seen that the domain of incoherent detection is the one with lower spectral resolutions, and this all the more so as the frequency is low.

# 7.1.2 Spatial Structure of Detectors

# Single-Channel Detectors

These are detectors which, at any given instant, can only measure a single point $( x , y )$ of the image, spectrum, etc. After an interval of time, called the integration time, the telescope or array, or whatever, is moved, so as to bring a new point to the centre of the detector (Fig. 7.3). This scanning can be continuous or made up of discrete steps. If it is continuous, the spatial frequencies of the intensity distribution are transformed into temporal frequencies. The temporal filtering effected by the detector, and the scanning rate, must then be chosen according to whatever spatial frequencies are being sought in the image. If the scanning is step-by-step, the sampling rate is chosen by reference to the sampling theorem.

![](images/5006105cdb55d16575171858986523f507f6723af13cb6edd1998483809ad5a7.jpg)  
Fig. 7.2 Comparison of coherent and incoherent detection. Abscissa: frequency (lower scale) and wavelength in $\mu \mathrm { m }$ (upper scale). Ordinate: Spectral resolution $R = \nu / \Delta \nu$ . Curves, established for three different spectral widths from $1 0 0 \mathrm { M H z }$ to $1 0 \mathrm { G H z }$ D, give the locus of points at which the two methods give the same signal-to-noise ratio, equal to 3 on the curves. Above, it is incoherent detection which has the advantage with regard to the signal-to-noise ratio, and below, it is coherent detection. The discontinuity at $\lambda \sim 2 0 0 \mu \mathrm { m }$ comes from the fact that, for incoherent detection, bolometers (Sect. 7.4.10) are used in the submillimeter region and photoconductors (Sect. 7.3.1) at shorter wavelengths, the latter having better noise characteristics. Note that coherent detection has the advantage with regard to the signal-to-noise ratio when the spectral band is narrow. From Philips T., cited by McWatson D., Physica Scripta, 1986

This type of image analysis, known as raster scanning, is similar to the movement of the electron beam in a television cathode ray tube. Its advantage is that the whole image is analysed with a single detector, which occupies the same position relative to the instrumental setup, if it is the telescope which is displaced, and this guarantees a strictly uniform instrumental response. Its drawback is clearly the concomitant inefficiency, for the greater part of the energy of the image, or the spectrum, at any given instant, is simply lost.

![](images/0644357a3cfb6354a04c7a3c3cc5b4bf31c5528513475e84173acda080dd93a7.jpg)  
Fig. 7.3 Television (raster) scanning of a field

Radiofrequency receivers are still usually single channel, although it becomes possible in the millimetre region to build arrays containing a few tens of elements.

# Multichannel Detectors

These detectors comprise $N$ independent detectors (pixels) which receive photons simultaneously. If each detector is assigned a different direction $\pmb \theta$ , the setup is an imaging detector (e.g., a photoconducting array in the focal plane of a telescope). If each pixel receives a different wavelength, the setup is a spectral multichannel detector, as exemplified by a CCD array placed at the focus of a grating spectrometer.

Because of their high efficiency, multichannel detectors have been developed for use right across the electromagnetic spectrum. The photographic plate covered only the regions between X rays and the visible, but modern array detectors (the CCD and its spin-offs, and bolometers) already extend from $\mathrm { X }$ rays to the far infrared, and are gradually moving into the millimetre region.

# Response of a Multichannel Detector

Consider first the simple case of a detector which is continuous in an ideal sense, such as a photographic plate with uniform quantum efficiency $\eta$ , and hence no grain. Within its domain of linearity, the signal $S ( x , y )$ is found from the incident intensity by a convolution

$$
S ( x , y ) = G ( x , y ) \star I ( x , y ) ,
$$

where the function $G ( x , y )$ characterises the spatial response of the plate. The Fourier transform $\tilde { G } ( u , \nu ) = \tilde { G } ( w )$ of $G$ is referred to as the modulation transfer Dfunction (MTF) (Fig. 7.4). The MTF relates the spatial spectrum of the signal to that of the incident information by

$$
\tilde { S } ( w ) = \tilde { G } ( w ) \tilde { I } ( w ) .
$$

In a real photographic plate, for which grain is taken into account by assuming that the quantum efficiency can be modelled by a random variable $\eta ( x , y )$ , the MTF itself becomes random, at least for high spatial frequencies $\sim 1 / g$ , where $g$ is the

![](images/6fa54a84d1ed8c03e9c8ed4bcfc7a334ad385e6baefb99ea87db179b79ce2209.jpg)  
Fig. 7.4 Spatial point source response $G ( x , y )$ and its Fourier transform $\tilde { G } ( u , \nu )$ . In the case shown, $\tilde { G }$ is real. $\mathsf { \tilde { G } } ( u , \nu )$ is the modulation transfer function of the detector

![](images/49c58fa53a9c5cf71dc673d56021ae6ff53c164c1791a4f98b4d5e3d0c844249.jpg)  
Fig. 7.5 Coverage of the image plane by a multichannel detector. Each detector pixel is shaded. Note, in this example, the relatively low geometrical filling factor. Progress in making CCD substrates means that this factor can now be made close to unity. In other cases, a microlens array in the focal plane can improve the exploitation of incident photons

mean grain size. If the detector has isotropic properties, the MTF will clearly exhibit circular symmetry.

A multichannel detector may also be composed of discrete elements (e.g., CCDs) which cover the image plane (Fig. 7.5). Let $p$ be the distance between the centres of the elements, and $a$ the length of their sides, with $a < p$ . The signal is then obtained from:

$$
\begin{array} { r l } & { I ( x , y ) \qquad \mathrm { i n c i d e n t ~ i n t e n s i t y } , } \\ & { I ^ { \prime } ( x , y ) = I ( x , y ) \star I I ( x / a , y / a ) } \\ & { S ( x , y ) = \sqcup \amalg ( x / p , y / p ) I ^ { \prime } ( x , y ) } \end{array}
$$

Hence, after normalisation at the origin, the MTF is given by

$$
\mathrm { \bf M T F } \propto \mathrm { F T } \left[ \pi \left( \frac { x } { a } , \frac { y } { a } \right) \right] = \mathrm { s i n c } ( a x ) \mathrm { s i n c } ( a y ) ,
$$

and it can be observed that the spacing $p$ does not necessarily represent a sampling adequate to the task of completely reconstructing $I ( x , y )$ , since $\tilde { G } ( \boldsymbol { w } )$ does not have bounded support. The appropriate value of $p$ thus depends on the spectrum $\tilde { I } ( \boldsymbol w )$ : if $\tilde { I } ( w ) = 0$ for $| { \boldsymbol w } | > w _ { \mathrm { c } }$ , $w _ { \mathrm { c } }$ being a cutoff frequency for the system, then a suitable choice is simply $p = 1 / 2 w _ { \mathrm { c } }$ .

# 7.1.3 Temporal Response

In the study of rapidly varying phenomena, such as a pulsar, by rapid photometry, the temporal capabilities of a detector must be determined. To this end, the temporal

![](images/34aea36b2af0dad5697e194181bed4b40549f365194376161bd6124e0e030a97.jpg)  
Fig. 7.6 (a) Point source response, and (b) complex transfer function of a low-pass filter. $\tau$ is the temporal width and $f _ { \mathrm { c } }$ the frequency width, so that $\tau f _ { \mathrm { c } } \approx 1$

response of a detector is defined by a time filter $H ( f )$ , or by the impulse response $\tilde { H } ( t )$ of the detector. The time constant of the detector is found from $\bar { \tilde { H } } ( t )$ (Fig. 7.6).

# Integrating Detectors

The duration $T$ of any measurement is always finite (so as to involve only a finite quantity of energy). If the incident signal is $x ( t )$ , the detector delivers

$$
y ( t ) = \int \pi \left( { \frac { t ^ { \prime } - t } { 2 T } } \right) x ( t ^ { \prime } ) \mathrm { d } t ^ { \prime } = \Pi \left( { \frac { t } { 2 T } } \right) \star x ( t ) .
$$

The integration is thus a case of filtering, by a sinc function (the FT of $\boldsymbol { \Pi }$ ) in the frequency space.

The photographic plate is an example of an integrator, since the instant $t$ is fixed and $T$ is the exposure time. The signal is then the density (blackening) of the photographic emulsion which, under certain conditions, is indeed proportional to the intensity (in the domain of linearity of the emulsion). The signal, or blackening of the emulsion, is then defined as the quantity

$$
X ( x , y ) = i ( x , y ) / i _ { 0 } ,
$$

or as

$$
- \log _ { 1 0 } X ( x , y ) ,
$$

where $i ( x , y )$ denotes the intensity transmitted by the plate at the point $( x , y )$ when it is illuminated by an intensity $i _ { 0 }$ (densitometry of a photographic image).

# 7.1.4 Noise

Below we shall examine in some detail the issue of physical fluctuations, which affect the detection of any form of radiation. A detector can augment these by adding further fluctuations, due to the way it is constituted or the way it is used. For example, this may be the dark current, amplifier noise, readout noise, or the grain of a photographic plate, etc. We shall return to these different forms of noise intrinsic to detectors after studying fundamental fluctuations. Ways of taking them into account and correcting for them, insofar as this is possible, will be examined in Sect. 9.6.

# 7.1.5 Characterisation of Detectors

Detectors are too complex to be characterised by a few simple parameters. Table 7.1 summarises all the properties that must be specified when two detectors, operating in the same spectral range, are to be compared, or when a detector must be chosen for some specific observation, or use with a specific instrument (spectrometer, camera, etc.).

The nomenclature here is very general. In any particular case, it can be simplified. The single-channel detector has only one pixel; the modulation transfer function or power spectrum of spatial noise are specific to two-dimensional imaging detectors and are irrelevant at radiofrequencies; readout noise is a specific property of solidstate imagers (CCDs); and so on.

Table 7.1 Detector characteristics   

<table><tr><td>Dynamic range</td><td>Sensitivity threshold Domain of linearity</td></tr><tr><td>Spectral properties</td><td>Saturation level Quantum efficiency n Domain of sensitivity△v (or△,or△E)</td></tr><tr><td></td><td>Spectral response n(v) Spectral resolution V/△v</td></tr><tr><td>Temporal response</td><td>Impulse response H(t)</td></tr><tr><td></td><td>Response time</td></tr><tr><td></td><td>Temporal filter function H(s)</td></tr><tr><td></td><td></td></tr><tr><td>Geometrical properties</td><td>Geometrical dimensions</td></tr><tr><td></td><td>Modulation transfer function G(w)</td></tr><tr><td>Noise (see below)</td><td>Homogeneity of spatial properties</td></tr><tr><td></td><td>Multichannel: pixel number or format N × M</td></tr><tr><td></td><td></td></tr><tr><td></td><td>Amplifier noise: gain g,fluctuations Og</td></tr><tr><td></td><td></td></tr><tr><td></td><td>Readout noise: NEC or OR</td></tr><tr><td></td><td>Intrinsic noise:NEP or noise temperature</td></tr><tr><td></td><td>Spatial noise characteristics:PSD</td></tr><tr><td></td><td>Temporal noise characteristics:PSD</td></tr><tr><td></td><td>Detector quantum efficiency DQE</td></tr><tr><td>Polarisation</td><td>Polarisation selectivity</td></tr></table>

# 7.2 Fundamental Fluctuations

In principle, in order to give a complete treatment of light and its interactions with matter, the most correct physical model available should be used, namely the quantisation of the electromagnetic field, and the associated concept of the photon (quantum electrodynamics QED). However, the great complexity of this model is hardly ever necessary for the cases studied in this text. Indeed, a designer of optical instrumentation (see Chap. 5) can sometimes even make do with the ultra-simple model which uses light rays. Consequently, the semi-classical model, will serve the purposes of this book. This describes field propagation (e.g., diffraction, see Chap. 6) by means of the classical electromagnetic wave, and the interaction with matter (e.g., detection, see below) by means of random Poisson processes. It is not the quantised field, but rather its observables, namely photoelectrons, which are described. Nevertheless, the terminology refers to ‘detected photons’, and is not quite appropriate when using the semi-classical model, as J.C. Dainty has pointed out. It is so common that the same term will be used here.

The semi-classical model is presented in Mandel L. and Wolf E., Rev. Mod. Phys. 37, 231, 1965.   
The discussion here is based on Dainty J.C., in Modern Technology and Its Influence on Astronomy.

In this model, light is subject to irreducible fluctuations when interacting with matter (detection), and this whatever the nature of the detector. The general features of these fluctuations will be presented here, followed by two limiting cases, the quantum and the thermal limits, which are sufficient in practice to give a simple description of the fluctuations of an electromagnetic signal.

Consider a vacuum enclosure at a uniform temperature $T$ , within which the radiation is in thermal equilibrium. The time-averaged electromagnetic energy density per unit frequency interval is given by

$$
\langle u ( \nu ) \rangle = \frac { 8 \pi h \nu ^ { 3 } } { c ^ { 3 } } \left[ \exp \left( \frac { h \nu } { k T } \right) - 1 \right] ^ { - 1 } \qquad \left[ \mathrm { J H z ^ { - 1 } m ^ { - 3 } } \right] .
$$

At any point inside the enclosure, the electromagnetic field $\mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf \Psi \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf \Psi \mathbf { } \mathbf { } \mathbf { } \mathbf \Psi \mathbf { } \mathbf { } \mathbf \Psi \mathbf { } \mathbf { } \mathbf \Psi \mathbf { } \mathbf { } \mathbf \Psi \mathbf { } \mathbf \Psi \mathbf { } \mathbf \Psi \Psi \mathbf { } \mathbf \Psi \mathbf { } \mathbf \Psi \mathbf { } \mathbf \mathbf { } \mathbf \Psi \mathbf \Psi \Psi \Psi \mathbf \Psi \Psi \mathbf \Psi \Psi \mathbf \Psi \Psi \mathbf \Psi \Psi \mathbf \Psi \mathbf \Psi \mathbf \Psi \Psi \mathbf \Psi \mathbf \Psi \Psi \mathbf \Psi \mathbf \Psi \mathbf \Psi \mathbf \Psi \mathbf \Psi \mathbf \Psi \mathbf \mathbf \Psi \mathbf \Psi \mathbf \mathbf \Psi \mathbf \Psi \mathbf \mathbf \Psi \mathbf \mathbf \mathbf \mathbf \Psi \mathbf \Psi \mathbf \mathbf \mathbf \mathbf \Psi \mathbf \mathbf \mathbf \mathbf \Psi \mathbf \mathbf \mathbf \mathbf \mathbf \Psi \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \Psi \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf$ results from a superposition of the fields radiated by a large number of incoherent elementary oscillators. This field is an ergodic stationary random (or stochastic) process, with zero mean. (For the terminology and results concerning stochastic processes, see Appendix B.) The central limit theorem (see Sect. 9.1) shows that this process is Gaussian (or normal), since $\mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } ^ { \mathbf { } } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \alpha \mathbf { } \mathbf { } \alpha \mathbf { } \mathbf { } \alpha \mathbf { } \mathbf { } \alpha \mathbf { } \mathbf { } \mathrm { } \mathbf { } \mathrm { } \mathrm { } \mathrm { } \mathbf { } { } \mathrm { } \mathrm { } \mathbf { } { } \mathrm { } \mathbf { } \alpha \mathbf { } \mathbf { } \alpha \mathbf { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathbf { } { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { \mathrm } \mathrm \mathrm \mathrm  \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm \mathrm { \mathrm } \mathrm \mathrm \mathrm \mathrm  \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm { \mathrm \mathrm \mathrm } \mathrm \mathrm \mathrm \mathrm  \mathrm$ is the sum of a large number of independent elementary fields. (It can also be shown that the normal distribution is the one which maximises the entropy for a given mean power.

In order to homogenise the physical dimensions, $\mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } ^ { \mathbf { } } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \alpha \mathbf { } \mathbf { } \alpha \mathbf { } \mathbf { } \alpha \mathbf { } \mathbf { } \alpha \mathbf { } \mathbf { } \mathbf { } \mathrm { } \mathrm { } \mathrm { } \mathbf { } \alpha \mathbf { } \mathbf { } \mathrm { } \mathrm { } \mathrm { } \mathbf { } \alpha \mathbf { } \mathbf { } \alpha \mathbf { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathbf { } { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathbf { } { } \alpha \mathbf { } \mathbf { } \alpha \mathbf { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm  \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm \mathrm { \mathrm \mathrm } \mathrm \mathrm \mathrm  \mathrm \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm  \mathrm \mathrm \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm  \mathrm$ is not the electric field of the wave with wave vector $\pmb { k }$ and frequency $\nu$ , but is proportional to it:

$$
{ \pmb a } ( t ) = ( \varepsilon _ { 0 } c \lambda ^ { 2 } ) ^ { 1 / 2 } { \pmb E } ( t ) \ .
$$

The square is then a power [W], and this is also the dimension of the autocorrelation $R ( \tau )$ , of which an estimator is

$$
R ( \tau ) = \frac { 1 } { T } \int _ { 0 } ^ { T } a ( t ) a ( t + \tau ) \mathrm { d } t \mathrm { ~ . ~ }
$$

The quantity $P ( \nu ) = R ( \tau ) \times$ time is measured in joules, or equivalently, in W $\mathrm { H z ^ { - 1 } }$ , as a power Dper unit frequency interval.

The autocorrelation of this stochastic process, identical to its covariance up to a scale factor, is determined from the power spectrum. The spectral density of $\mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } ^ { \mathbf { } } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } \mathbf { } ^ { \mathbf { } } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \alpha \mathbf { } \mathbf { } \alpha \mathbf { } \mathbf { } \alpha \mathbf { } \mathbf { } \alpha \mathbf { } \mathbf { } \mathrm { } \mathrm { } \mathbf { } \mathrm { } \mathrm { } \mathrm { } \mathbf { } \alpha \mathbf { } \mathbf { } \alpha \mathbf { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathbf { } { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathbf { } { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { \mathrm } \mathrm \mathrm \mathrm { \mathrm } \mathrm \mathrm \mathrm  \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm \mathrm { \mathrm } \mathrm \mathrm \mathrm \mathrm { \mathrm \mathrm } \mathrm \mathrm \mathrm  \mathrm \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm { \mathrm \mathrm } \mathrm $ is the electromagnetic power associated with the field of frequency $\nu$ , in a coherence etendue´ equal to $\lambda ^ { 2 }$ . In order to define a finite monochromatic power, a solid angle $\varOmega$ and an associated surface element $S$ must be defined (Fig. 7.7). We refer to Sect. 3.2 for the demonstration that the radiation can be considered as coherent when attention is limited to the etendue´ $S \varOmega = \lambda ^ { 2 }$ . For either of the two polarisations, the associated monochromatic power is

$$
P ( \nu ) = \frac { 1 } { 2 } \overline { { u } } ( \nu ) \frac { \lambda ^ { 2 } } { 4 \pi } c = h \nu \left[ \exp \left( \frac { h \nu } { k T } \right) - 1 \right] ^ { - 1 } \qquad [ \mathrm { W H z ^ { - 1 } } ] .
$$

The $4 \pi$ factor just normalises the solid angle, and the presence here of the speed of light is due to an integration of the energy contained in a cylinder of length $c$ and unit cross-section.

Thermodynamics shows that a system of mean energy $\langle W \rangle$ fluctuates about this mean, over time, with a variance given by

$$
\langle \Delta W ^ { 2 } \rangle = \langle W ^ { 2 } \rangle - \langle W \rangle ^ { 2 } = k T ^ { 2 } { \frac { \mathrm { d } \langle W \rangle } { \mathrm { d } T } } .
$$

Applying this result to the mean power calculated above, it follows that

$$
\left. \left[ \Delta P ( \nu ) \right] ^ { 2 } \right. = k T ^ { 2 } { \frac { \mathrm { d } P ( \nu ) } { \mathrm { d } T } } = P ( \nu ) h \nu \left\{ 1 + \left[ \exp \left( \frac { h \nu } { k T } \right) - 1 \right] ^ { - 1 } \right\} \ .
$$

![](images/0f29ef2d9c0a90b83e965e6866f1aca2736e93732b035178c2847a79e606e523.jpg)  
Fig. 7.7 A vacuum enclosure, with perfectly reflecting walls, contains a small quantity of matter at temperature $T$ , in equilibrium with the radiation, at the same temperature. An antenna, symbolised by the circular area $S$ , receives radiation in a cone of solid angle $\varOmega$ . The coherence etendue is then ´ $\dot { S } \varOmega = \lambda ^ { 2 }$

Inside a blackbody cavity in thermal equilibrium, the fluctuations of the radiation field2 are manifested by the presence of two terms:

• A term h $P ( \nu )$ which can be interpreted as a photon number fluctuation. Letting $\langle n \rangle$ denote the mean number of photons received per unit time, Poisson statistics h iimplies

$$
\langle \Delta n ^ { 2 } \rangle = \langle n \rangle \ .
$$

• A term

$$
h \nu \left[ \exp \left( \frac { h \nu } { k T } \right) - 1 \right] ^ { - 1 } P ( \nu ) = \left. [ P ( \nu ) ] ^ { 2 } \right. ,
$$

in which the radiation temperature appears explicitly. This fluctuation term can be interpreted as being due to the random phase differences of the wave fields, and the beats between field components of different frequency. These fluctuations are low frequency, because of the exponential term. This phenomenon is analogous to the production of speckles (see Sect. 6.2) by interference between waves of random relative phase.

The structure of these two terms means that, to a first approximation, and depending on the value of $h \nu / k T$ , one or other of them will dominate. For this reason, they can be studied separately.

If the first term dominates, the fluctuations are referred to as photon noise, quantum noise, or shot noise, and correspond to the quantum limit.

The discussion here will be limited to quantum noise associated with incoherent radiation, which is the type most frequently encountered in astrophysics (for example, in blackbody radiation). In Sect. 3.2, the quantum fluctuations of partially coherent radiation were examined, in the context of temporal and spatial coherence.

If the second term dominates, the fluctuations are referred to as thermal noise. In the general case when both fluctuations coexist,

$$
\langle \Delta n ^ { 2 } \rangle = \langle n \rangle ( 1 + \delta ) ~ , ~ \mathrm { w i t h } ~ \delta = ( \mathrm { e } ^ { h \nu / k T } - 1 ) ^ { - 1 } ,
$$

where $\delta$ is called the degeneracy factor and results directly from the Bose–Einstein statistics satisfied by photons. $\delta$ is the number of photons which are coherent with each other (refer to the discussion on temporal coherence in Chap. 3).

# Remark 1

The expression for the fluctuations applies only to the radiation inside a blackbody. If this condition is not fulfilled, the dominant term in the fluctuations may be different.

Consider an observation of a star, whose spectrum is assumed similar to that of a blackbody of temperature $T$ . The radiation is observed at some frequency $\nu$ such that $h \nu \ll k T$ . According to the general formula, if it were applicable, the thermal noise should dominate. Imagine, however, that the star is observed from far enough away to ensure that the photons $( h \nu )$ arrive at the detector at well-separated times. Clearly, quantum noise should then dominate. Indeed, the radiation is unidirectional here, the beam etendue sampled by the observation much less than´ $\lambda ^ { 2 }$ , and the number of photons sampled in $P ( \nu )$ remains very small.

# Remark 2

This second term triggered the idea of intensity interferometry discussed earlier (see Sect. 6.4). Indeed, when an extended light source is observed simultaneously from two distant points, the intensity fluctuations remain correlated if the separation between these two points is rather small. More precisely, the distance at which the correlation disappears depends on the coherence etendue of the source, whose´ angular size can thus be determined. This possibility, put forward by the physicist Robert Hanbury-Brown in the 1940s, raised much skepticism until he demonstrated it, first in the laboratory, and then on the stars.

# Remark 3

A simple argument explains why quantum noise dominates at high frequencies. The exponential decrease in $P ( \nu )$ , as $\nu$ increases, implies that the power required to transmit a given quantity of information could be made to tend to zero, by using a high enough frequency $\nu$ . In the limit, less than one quantum $h \nu$ of energy would suffice. Quantisation must therefore create some other source of fluctuation, to prevent such a physically unacceptable state of affairs, and indeed it is exactly what was referred to as quantum or photon noise which forbids the programme described here.

Figure 7.8 shows the characteristic domains of these two fundamental fluctuations, which are independent of the type of detector used. It is worth noting that the detector does not detect radiation only from the source, but also from its environment (the laboratory, the telescope, the atmosphere, the ground, and so on), whose temperature is generally around $3 0 0 \mathrm { K }$ , unless it is located in space and cooled.

• In the visible and ultraviolet regions, quantum noise dominates. • At radiofrequencies, thermal noise dominates, even if the system can be cooled, so as to reduce its noise temperature.

By contrast, in the infrared and submillimetre regions, it may be necessary to take both types of fluctuation into account.

![](images/5f7fc99c4e75beafa86ee1835b903da8c96e9a062d0d00c1583cc8509fc8ba71.jpg)  
Fig. 7.8 Regions of predominant quantum or thermal noise, separated by the straight line $h \nu = k T$

# 7.2.1 Quantum Noise

Consider a flux of photons defining a stochastic process $\mathbf { x } ( t )$ made up of Poisson impulses. The parameter is $\overline { { n } }$ , the mean number of photons received per unit time, within the etendue ´ $S \varOmega$ defined by the detection system, e.g., the telescope optics. Then the probability of obtaining $p$ events during a time $T$ is given by

$$
P \left[ \int _ { T } \mathbf { x } ( t ) \mathrm { d } t = p \right] = { \frac { ( { \overline { { n } } } T ) ^ { p } \operatorname { e } ^ { - { \overline { { n } } } T } } { p ! } } \ ,
$$

which leads to a mean number of events $n _ { T }$ during the time $T$ given by

$$
n _ { T } = { \overline { { n } } } T \ ,
$$

with variance given by

$$
\sigma ^ { 2 } = \langle n _ { T } ^ { 2 } \rangle - \langle n _ { T } \rangle ^ { 2 } = \overline { { n } } T \ .
$$

When $n _ { T } \gg 1$ , the random variable

$$
\delta n _ { T } = n _ { T } - \langle n _ { T } \rangle
$$

is normal (Gaussian), with standard deviation $( \overline { { n } } T ) ^ { 1 / 2 }$ .

If the measurement involves counting the number of photons received in time $T$ , the signal-to-noise ratio is

$$
R = \frac { \overline { { n } } T } { ( \overline { { n } } T ) ^ { 1 / 2 } } = ( \overline { { n } } T ) ^ { 1 / 2 } ,
$$

and it varies as the square root of the measurement time.

Example

Photon counting in $\gamma$ -ray astronomy. The COS-B satellite, put into orbit in 1975, detected the brightest source in the sky, the Vela pulsar, at $5 0 \mathrm { M e V } .$ . This pulsar has period $8 9 . 2 \mathrm { m s }$ . Using an accurate clock, the signal-to-noise ratio can be improved, by accumulation of successive cycles. With 89 bins, a total of 2 963 detected events were accumulated, over 38 days of observation (Fig. 7.9). (A bin is the interval $\Delta x _ { i }$ of the variable $x$ , of constant width, over which the average value of some function is measured.) Although there is a modulation in the intensity over the cycle, the average number of events per bin, and the standard deviation giving the confidence interval, are

$$
\overline { { { N } } } _ { T } = \frac { 2 9 6 3 } { 8 9 } = 3 3 . 2 9 , \qquad \sigma _ { N _ { T } } = 5 . 8 .
$$

# Conversion of Photons into Photocurrent

A photoelectric detector (see below) converts photons into current impulses. The quantum efficiency $\eta$ of the detector is defined as the ratio of the mean number of photoelectrons produced to the mean number of incident photons over some period $T$ .

![](images/2108e4e958d48da42d949c5694f3454eed029b84f474c7f84fd91495353aeed4.jpg)  
Fig. 7.9 Accumulated $\gamma$ -ray photon counts, during an observation of the pulsar PSR 0833-45 by the satellite COS-B, at high energy $h \nu > 5 0 \mathrm { M e V } ,$ ). (Benett K. et al., Astr. Ap. 61, 279, 1977.) The period was divided into 100 bins, and successive cycles were added bin by bin, to improve the signal-tonoise ratio

If $\mathbf { x } ( t )$ describes the arrival process of the photons, the process $\mathbf { i } ( t )$ describing the photocurrent is

$$
\mathbf { i } ( t ) = { \left\{ \begin{array} { l l } { e \mathbf { x } ( t ) { \mathrm { ~ p r o b a b i l i t y ~ } } \eta ~ , } \\ { 0 \qquad { \mathrm { p r o b a b i l i t y ~ } } 1 - \eta ~ . } \end{array} \right. }
$$

$\mathbf { i } ( t )$ is a new process, constructed from the process $\mathbf { x } ( t )$ , and

$$
\mathbf { i } ( t ) = G [ \mathbf { x } ( t ) ]
$$

would be a correct representation, if the passband of the detector were infinite. Real detectors (photomultiplier, photoconductor, etc.) always have a finite frequency passband. The temporal filtering property of the detector can be represented by the idealised low-pass transfer function

$$
\tilde { H } ( f ) = \pi \left( { \frac { f } { 2 f _ { \mathrm { c } } } } \right) ,
$$

which cuts off the frequency at $f _ { \mathrm { c } }$ (Fig. 7.10). The photocurrent is now

$$
\mathbf { i } ( t ) = G [ \mathbf { x } ( t ) ] \star H ( t ) \ ,
$$

where $H ( t )  \tilde { H } ( f )$ (Fourier transform). Its spectral density is

$$
S _ { \mathbf { i } } ( f ) = \left[ \overline { { { n } } } ^ { 2 } \delta ( f ) + \overline { { { n } } } \right] \eta \tilde { H } ( f ) ,
$$

where the general expression for the spectral density of a Poisson s.p. has been used (see Appendix B). The variance of the photocurrent can be calculated as

$$
\sigma _ { \mathbf { i } } ^ { 2 } = R ( 0 ) - \eta \overline { { n } } ^ { 2 } = \int _ { - \infty } ^ { + \infty } S _ { \mathbf { i } } ( f ) \mathrm { d } f - \eta \overline { { n } } ^ { 2 } = 2 \eta \overline { { n } } f _ { \mathrm { c } } ,
$$

and the signal-to-noise ratio S/N for incident power $P ( \nu ) = { \overline { { n } } } h \nu$ is

$$
\frac { i ^ { 2 } } { \sigma _ { \mathbf { i } } ^ { 2 } } = \eta \frac { P ( \nu ) } { 2 h \nu f _ { \mathrm { c } } } .
$$

![](images/6837e0e3007f9be9ca9d185bd58ca1a58beb80eb24d39e39bf525f48375c124f.jpg)  
Fig. 7.10 Filtering of the stationary process assumed to describe the photocurrent

The incident power producing a unit signal-to-noise ratio is thus

$$
P ( \nu ) = \frac { 2 h \nu } { \eta } f _ { \mathrm { c } } .
$$

A simple interpretation of this result can be given. When photon noise dominates the signal, the signal-to-noise ratio is unity for two photoelectrons per hertz of passband, or one photoelectron per polarisation per hertz of passband.

The S/N ratio can evidently be improved by imposing a narrow passband, which means a long integration time (smoothing by running mean). Some recent ideas (1990) suggest that the above noise limit could be reduced by quantum noise compression.

# Background Noise

It often happens that the detector receives simultaneously:

• source photons, leading to a photocurrent $i _ { \mathrm { s } } ( t )$ , • background photons, leading to a photocurrent $i _ { \mathrm { b } } ( t )$ .

This background emission may be due to the thermal environment of the detector (at infrared or millimetre frequencies), the dark current of the detector (e.g., for photocathodes), or to the secondary particle environment (for high energy astronomy).

The independence of the two signals implies

$$
\sigma _ { \mathrm { i } } ^ { 2 } = \sigma _ { \mathrm { s } } ^ { 2 } + \sigma _ { \mathrm { b } } ^ { 2 } \ ,
$$

and when the source is faint,

$$
i _ { \mathrm { b } } \gg i _ { \mathrm { s } } , \qquad \sigma _ { \mathrm { i } } ^ { 2 } \sim \sigma _ { \mathrm { b } } ^ { 2 } .
$$

The minimum detectable signal $( \mathrm { S } / \mathrm { N } = 1 $ ) is then

$$
i _ { \mathrm { s } } = \sigma _ { \mathrm { b } } ~ ,
$$

which implies an incident power at the detector given by

$$
P _ { \mathrm { s } } = h \nu \left( \frac { 2 } { \eta } \frac { P _ { \mathrm { b } } } { h \nu } \ : f _ { \mathrm { c } } \right) ^ { 1 / 2 } .
$$

This power is called the noise equivalent power (NEP), when referred to a unit passband fc 1 Hz. It is measured in W Hz 1=2.

DGiven the characteristics of the reception system, namely the collecting area $A$ , the transmission $t$ , the spectral passband $\Delta \nu \ll \nu$ (a prerequisite for the definition), we can further define the noise equivalent flux (NEF) to be

$$
\mathrm { N E F } = \frac { P _ { \mathrm { s } } } { A \Delta \nu f _ { \mathrm { c } } ^ { 1 / 2 } t } \quad \mathrm { [ W m ^ { - 2 } H z ^ { - 1 } H z ^ { - 1 / 2 } ] } .
$$

The NEF is often given in Jy $\mathrm { H } z ^ { - 1 / 2 }$ $( 1 ~ \mathrm { J y } = 1 0 ^ { - 2 6 } ~ \mathrm { W } ~ \mathrm { m } ^ { - 2 } ~ \mathrm { H z } ^ { - 1 } ,$ . It is a convenient Dunit for determining the detectability of source, by comparing the flux it emits with the efficiency of the system.

At the high energies of $\gamma$ radiation, the background signal will be expressed by the number of counts in a given spectral interval of the detector, i.e., in counts per keV, and its fluctuations will once again be of Poisson type for low fluxes and approximately Gaussian for high fluxes.

# 7.2.2 Thermal Noise

We return now to the approximate expression for the radiated power density, at low frequency, of a blackbody at temperature $T$ , under the assumption that $h \nu \ll k T$ :

$$
P ( \nu ) \approx \frac { h \nu } { \mathrm { e } ^ { h \nu / k T } - 1 } \quad [ \mathrm { W } \mathrm { H z } ^ { - 1 } ] \ .
$$

The process ${ \bf a } ( t )$ , proportional to the electric field, thus has an almost-white power spectral density (PSD) (Fig. 7.11)

$$
P ( \nu ) \approx k T \quad [ \mathrm { W H z ^ { - 1 } } ] ,
$$

up to a frequency $\nu \sim k T / h$ . In practice, the receiving system (antenna, mixer, diode, etc.) always has a cutoff frequency $\nu _ { \mathrm { c } }$ less than $k T / h$ . If $T = 3 0 0 ~ \mathrm { K }$ , the condition $h \nu ~ = ~ k T$ corresponds to a wavelength of $5 0 ~ { \mu \mathrm { m } }$ $( \nu = 6 \times 1 0 ^ { 1 2 } \mathrm { H z } )$ , D D shorter than that of the sensitivity threshold. The effect of the receiving system can thus be represented by a filter, modelled by the transfer function

$$
\tilde { H } ( \nu ) = \varPi \left( \frac { \nu } { 2 \nu _ { \mathrm { c } } } \right) .
$$

Let ${ \bf a } _ { 1 } ( t )$ be the stochastic process resulting from this filtering. It has zero mean, so its autocorrelation and autocovariance are equal, and its variance can be written

![](images/6ca86ff59fd4b047d13104ef7eb9ca67c0db94c2fbf145064bee4ed96e560d26.jpg)  
Fig. 7.11 Spectral density of thermal noise. Note that the curve is asymptotic to zero, at frequencies where quantum noise must be added. The dashed lines show the filtering produced by a low-pass filter associated with a detector

$$
\sigma _ { \mathbf { a } _ { 1 } } ^ { 2 } = R _ { \mathbf { a } _ { 1 } } ( 0 ) = \int _ { - \infty } ^ { + \infty } P ( \nu ) \mathrm { d } \nu = 2 k T \nu _ { \mathrm { c } } \ .
$$

The numerical coefficient relating $\sigma _ { \mathbf { a } _ { 1 } } ^ { 2 }$ to the characteristic quantity $k T \nu _ { \mathrm { c } }$ depends on the exact form of $\tilde { H } ( \nu )$ .

An Important Special Case

The detector can be treated as a simple low-pass resistance–capacitance filter, whose power transfer function is known to be

$$
\tilde { H } ( \nu ) = \frac { 1 } { 1 + ( 2 \pi R C \nu ) ^ { 2 } } , \quad f _ { \mathrm { c } } = ( 2 \pi R C ) ^ { - 1 } .
$$

Consequently,

$$
P _ { { \bf a } _ { 1 } } ( \nu ) = \frac { k T } { 1 + ( 2 \pi R C \nu ) ^ { 2 } } ,
$$

and also

$$
\sigma _ { \mathbf { a } _ { 1 } } ^ { 2 } = { \frac { k T } { 2 R C } } = \pi k T f _ { \mathrm { c } } ~ .
$$

By Fourier transformation (the appropriate Fourier pairs are given in tables of functions, see also Appendix A), the autocorrelation (or, equivalently, the autocovariance) of ${ \bf a } _ { 1 } ( t )$ is given by

$$
R _ { \mathrm { a } _ { 1 } } ( \tau ) = C _ { \mathrm { { a } _ { 1 } } } ( \tau ) = \frac { k T } { 2 R C } \exp \left( - \frac { | \tau | } { R C } \right) = \pi k T f _ { \mathrm { c } } \exp ( - 2 \pi f _ { \mathrm { c } } | \tau | ) \ .
$$

The normal process is therefore completely specified. A different filtering $\tilde { H } ( \nu )$ leads to a normal process with different autocorrelation and spectrum.

# Thermal Noise of a Resistor

This simple case is of interest because it provides an invaluable relation between the power associated with noise and the temperature of a physical system (a simple resistor, for this example), in a state of statistical equilibrium. In a resistor at temperature $T$ , the free electrons are subject to thermal excitation. A random voltage $\mathbf { v } ( t )$ therefore appears across the resistor, and this voltage depends on the temperature $T . { \bf v } ( t )$ is a zero mean, stationary, normal random process. The nonzero capacitance $C$ associated with the resistance $R$ determines, as above, the form of the spectral density of $\mathbf { v } ( t )$ :

$$
S _ { \mathbf { v } } ( \nu ) = A \frac { 1 } { 1 + 4 \pi ^ { 2 } R ^ { 2 } C ^ { 2 } \nu ^ { 2 } } ,
$$


<!-- chunk 0006: pages 351-420 -->
where $A$ is determined by the equipartition of energy in thermodynamic equilibrium. The latter implies, at low frequencies $\nu \ll ( R C ) ^ { - 1 }$ ,

$$
\frac { S _ { \mathbf { v } } ( \nu ) } { R } = 2 k T ~ ,
$$

and hence

$$
A = 2 k T R \ ,
$$

where $2 k T$ is the power per unit frequency in unpolarised radiation from a blackbody at temperature $T$ , provided the frequencies are low (Rayleigh–Jeans law). The cutoff frequency $( R C ) ^ { - 1 }$ of this thermal noise is associated with the mean free path of the electrons between atoms, and is of the order of $1 0 ^ { 1 3 } ~ \mathrm { H z }$ at $3 0 0 ~ \mathrm { K }$ . After filtering $\mathbf { v } ( t )$ with a filter of frequency bandwidth $\Delta \nu \ll ( R C ) ^ { - 1 }$ , the noise power of the filtered voltage is then given by

$$
\langle \nu ^ { 2 } \rangle = \int _ { - \infty } ^ { + \infty } S _ { \mathbf { v } } ( \nu ) \mathrm { d } \nu = 4 k T R \Delta \nu ,
$$

which is the Nyquist formula.

This formula is particularly useful in determining the thermal noise associated with a detector which behaves like a resistance at temperature $T$ .

# Quadratic Detectors and Thermal Noise

A quadratic detector has been defined as one which delivers, for example, the quantity proportional to the square ${ \bf b } ( t )$ of the process ${ \bf a } _ { 1 } ( t )$ resulting from the filtering of the electric field ${ \bf a } ( t )$ .

The autocorrelation of the stochastic process ${ \bf b } ( t )$ is given by the expression (see Appendix B)

$$
R _ { \bf b } ( \tau ) = R _ { { \bf a } _ { 1 } } ^ { 2 } ( 0 ) + 2 R _ { { \bf a } _ { 1 } } ^ { 2 } ( \tau ) \ .
$$

Taking the Fourier transform of this relation,

$$
S _ { \bf b } ( \nu ) = R _ { { \bf a } _ { 1 } } ^ { 2 } ( 0 ) \delta ( \nu ) + 2 S _ { { \bf a } _ { 1 } } ( \nu ) \star S _ { { \bf a } _ { 1 } } ( \nu ) .
$$

Letting ${ \bf a } _ { 1 } ( t )$ be a stochastic process filtered by a low-pass box-function filter, with cutoff at $\nu _ { \mathrm { c } }$ , it follows that

$$
S _ { \mathbf { a } _ { 1 } } ( \nu ) = k T \pi \left( \frac { \nu } { 2 \nu _ { \mathrm { c } } } \right) , \qquad R _ { \mathbf { a } _ { 1 } } ( \tau ) = 2 k T \nu _ { \mathrm { c } } \operatorname { s i n c } ( 2 \nu _ { \mathrm { c } } \tau ) ,
$$

$$
S _ { \mathbf { b } } ( \nu ) = ( 2 k T ) ^ { 2 } \nu _ { \mathrm { c } } ^ { 2 } \delta ( \nu ) + 2 ( k T ) ^ { 2 } 2 \nu _ { \mathrm { c } } \left( 1 - \frac { \nu } { 2 \nu _ { \mathrm { c } } } \right) ,
$$

![](images/a09c96a379c57068d9053c4d1a5f6eb28cd18bc5d3e7b1eb129c81dbe8d5b0c0.jpg)  
Fig. 7.12 Spectral density of a filtered stochastic process ${ \bf a } ( t )$ , and of its square ${ \bf b } ( t )$

as illustrated in Fig. 7.12. The PSD of the stochastic process ${ \bf b } ( t )$ is no longer white, and its mean no longer zero, as is shown by the non-zero value of $S _ { \mathbf { b } } ( 0 )$ .

Note. A similar method could be used to study the probability distributions of the amplitude and phase of ${ \bf a } _ { 1 } ( t )$ , and of its instantaneous mean power, etc., in those experimental arrangements which involve these quantities.

We now have at our disposal all the tools needed to find variances and autocorrelations associated with thermal noise. These will be used in the next chapter to establish the ultimate limits of receiving systems with respect to this type of noise.

# 7.3 Physical Principles of the Detection of Electromagnetic Radiation

Detection involves a matter–radiation interaction and a transfer of energy towards the matter, which causes it to change state in a measurable way. Clearly, this change of state, which constitutes the signal, must be chosen to correspond to the mean energy $h \nu$ of the detected photons. If it involves too low an energy, the signal will be non-existent or undetectable, but if its energy is too high, the detector may be damaged or destroyed. Figure 7.13 gives an overview of the main interactions used in the detection of photons.

The photoelectric detection of radiation quanta is possible provided that their energies exceed several meV, which means wavelengths less than about $2 0 0 \mu \mathrm { m }$ . At longer wavelengths, thermal fluctuations dominate, so that radiofrequency quanta are hard to detect. This is not, however, a fundamental limitation, and in practice, radiofrequency detectors (in the millimetre and centimetre ranges, and beyond) detect the electric field of the wave directly. Finally, calorimetric detection of radiant energy constitutes a third approach, which is useful in the submillimetre and $\gamma$ ray regions of the spectrum.

![](images/22ffecae56847e53d02a946498ed6ab85f3f57ae2ec77d2225760ec6acc39a31.jpg)  
Fig. 7.13 Physical interactions and detection of radiation

# 7.3.1 Detection of Quanta

Here we discuss the physical principles applied in the detection of individual photons and the production of a measurable signal. Recent developments in microelectronics have profoundly changed, improved, and diversified the processes used by astronomers in their dectectors.

# Photoelectric Emission in Vacuum

The surface of a conducting solid presents a potential barrier which opposes the extraction of electrons from that solid. The height $E _ { \mathrm { s } }$ of this barrier is called the work function of the surface. Only photons with energy greater than this threshold can produce a photoelectron. The first photoelectric cell was devised in 1890 by Elster and Geitel. The work function $E _ { \mathrm { s } }$ depends on the crystal structure and the state of the surface of the material, but is generally around $1 \ \mathrm { e V } ,$ which limits the use of the photoelectric effect in vacuum to detection of wavelengths shorter than the micron (visible, UV, and X ray).

When the photon energy is greater than this threshold, the probability of photoelectron production is the quantum efficiency $\eta$ , defined by

$$
\eta = \frac { \mathrm { m e a n ~ n u m b e r ~ o f ~ p h o t o e l e c t r o n s ~ p r o d u c e d } } { \mathrm { m e a n ~ n u m b e r ~ o f ~ i n c i d e n t ~ p h o t o n s } } .
$$

This probability (Fig. 7.14) can be determined theoretically from the atomic structure of the material and the thickness of the emitting layer. It is generally

![](images/036556c629aa7c67a2b3b9605f740e5145ca053f5f2f93cae4cddf102055e8ad.jpg)  
Fig. 7.14 Quantum efficiency $\eta$ of photocathodes (in $\%$ ): (a) in the visible and near ultraviolet and $\mathbf { ( b ) }$ in the far ultraviolet. The S1 layer is a $\mathrm { A g - O - C s }$ photocathode (1930), and the S20 layer is tri-alkali ${ \mathrm { N a } } _ { 2 } { \mathrm { K S b } }$ (Sommer, 1955). Note the extremely poor response in the red, and excellent response in the far UV

less than unity, unless the photon energies become large compared with the energy differences between levels in the material (i.e., at UV or X wavelengths).

Detectors using the photoelectric effect in vacuum are the photomultiplier, the electronic camera, and image intensifiers.

# The Photoelectric Effect in Solids

Even when the energy of a photon is insufficient to eject an electron from the solid surface, it may nevertheless cause the ionisation of an atom in the solid, thus releasing charge carriers within the crystal lattice, and modifying the electrical conductivity of the material. This photoconducting effect can be used to detect the incident photon (Smith W., 1873).

Photoconducting materials are semiconducting crystals, and electrons within the crystal lattice have a characteristic energy level structure (Fig. 7.15). The conduction band is separated from the valence band by a gap, and the energy difference $E _ { \mathrm { s } }$ associated with this gap is exactly the photoelectric threshold of the material.

The width of this gap depends on the wave vector $\pmb { k }$ of the electrons. Let $E ( k )$ be this width. Its minimum value is $E _ { \mathrm { s } }$ , which is usually between a half and a quarter of its mean value. A photon of energy $E _ { \gamma }$ can transfer an electron of wave vector $\pmb { k }$ into the conduction band, and thus leave a hole in the valence band, if $E _ { \gamma } > E ( k )$ . This pair of charge carriers will move under the effect of an externally applied electric field, producing a current, or photocurrent. A pure crystal which manifests this effect is known as an intrinsic photoconductor (Table 7.2).

![](images/b231cdb7e86ddcb26cebf7a1fc78671b7a769a000483d0743869b84114623a0f.jpg)  
Fig. 7.15 Energy levels in a semiconducting solid. (a) Intrinsic photoconductivity. (b) Extrinsic photoconductivity of a doped semiconductor

Table 7.2 Intrinsic photoconductivity   

<table><tr><td>Material</td><td>Threshold wavelength [μm]</td><td>Working temperature [K]</td><td>Applications</td></tr><tr><td>Germanium Ge</td><td>1.88</td><td>77</td><td>Solar energy</td></tr><tr><td>Silicon Si</td><td>1.14</td><td>300</td><td>Astronomical detectors</td></tr><tr><td>Cadmium sulphide CdS</td><td>0.52</td><td>77 to 150</td><td>Photography (exposure meters)</td></tr><tr><td>Indium antinomide InSb</td><td>5.50 (77 K)</td><td>4 to 77</td><td>Astronomical detectors</td></tr><tr><td>Hg1-xCdxTe</td><td>Varies with x but ≤ 20μm</td><td>20 to 300</td><td>Thermal surveillance and astronomical detectors</td></tr></table>

In an extrinsic photoconductor (Fig. 7.15b), further energy levels appear in the band gap. These are caused by adjoining atoms of impurities within the crystal lattice, at very low concentrations $( \lesssim 1 0 ^ { - 8 }$ ). As these atoms can trap charge carriers, the energy threshold is lowered, and this explains why all infrared detectors, beyond about $\lambda = 5 ~ { \mu \mathrm { m } }$ , make use of extrinsic photoconduction. For example, replacing Done silicon atom (group IV of the periodic table) by one arsenic atom (group V of the same) in the silicon lattice, means adding an atom of similar electronic structure to the other atoms in the lattice, but with one extra, easily removed electron, and it is this extra electron that is responsible for the extrinsic photoconductivity ( $\overset { \cdot } { n }$ -type electron conductivity). Group III atoms inserted into a lattice of group IV atoms will lead to $p$ -type hole conductivity. The threshold can be adjusted, by making a suitable choice of impurity, or dopant, and this selects the wavelength region to which the detector is sensitive (Table 7.3). This idealised picture of photoconductivity should also take into account the effects of temperature and impurities.

Photoconductors are used in two ways: firstly, to measure electric current (photoconduction), and secondly, to measure pulses. In the first case, a flux is measured (photometry), and in the second, the energy of quanta is measured (spectrometry). In both cases, the performance of the photoconductor depends on its conductivity.

The conductivity, in turn, depends on the concentration of charge carriers in the conduction band. At low temperatures, this concentration depends on the temperature, and also the level of impurities, whereas at high temperature, it no longer depends on the level of impurities. For an intrinsic semiconductor, the concentration of charge carriers follows from the law of mass action, and can be written

Table 7.3 Extrinsic photoconductivity   

<table><tr><td>Matrix material: dopant</td><td>Threshold wavelength [μm]</td><td>Working temperature [K]</td></tr><tr><td>Si:As</td><td>24</td><td>&lt;20</td></tr><tr><td>Si:In</td><td>7.4</td><td>77</td></tr><tr><td>Si:Bi</td><td>18.7</td><td>29</td></tr><tr><td>Si:Ga</td><td>17.8</td><td>27</td></tr><tr><td>Ge:Ga</td><td>120</td><td>4</td></tr><tr><td>Ge:Gaa</td><td>195</td><td>4</td></tr></table>

a Threshold decreased by mechanical pressure on the crystal (stressed photoconductor).

$$
n _ { \mathrm { i } } = p _ { \mathrm { i } } \approx T ^ { 3 / 2 } \exp \left( - { \frac { E _ { \mathrm { s } } } { 2 k T } } \right) .
$$

For $k T > 2 \times 1 0 ^ { - 2 } E _ { \mathrm { s } }$ , the current is dominated by thermal excitation of the electrons near the conduction band, and not by photoionisation. This explains why a photoconductor must be cooled to a temperature $T \ll E _ { \mathrm { s } } / k$ , and the temperature must decrease as the energy of the quanta decrease, or if their their flux is low (photometry), or again when higher accuracy is required in the measurement of their energy (spectrometry).

Moreover, the crystals can never be perfectly pure, and it is difficult to go below an impurity level of $1 0 ^ { 1 1 } \mathrm { c m } ^ { - 3 }$ . Some atoms, occurring as an impurity, create energy levels which are very close to the conduction band, and which can be excited by very low temperatures. Even for $T \ll T _ { \mathrm { s } }$ , and in the absence of photons, the current will be non-zero (dark current). Hence, the quality of a photoconducting detector can be represented by the value of its impedance at its working temperature, and in the absence of any illumination (typically, $R \gg 1 \mathrm { G } \Omega$ ).

Only a fraction of incident photons create electron–hole pairs. Indeed, some photons lose their energy by exciting vibrations in the crystal lattice (phonons). This heats the crystal (optical absorption). When the optical depth of the material is sufficient, taking into account the photoabsorption cross-section $( \tau _ { \lambda } \sim 1 )$ , the quantum efficiency $\eta$ of the material is then determined.

The photoelectric effect in solids has become the basis for a large family of detectors used in astronomy: avalanche diodes, photoconducting or photovoltaic infrared detectors, solid-state imagers (also called Reticons, CCDs, or CIDs), blocked impurity band (BIB) detectors, television tubes, and photodiodes.

The Photovoltaic Effect. Junctions

Consider two doped semiconductors, one with impurities giving $n$ -type (electron) conductivity, the other with impurities giving $p$ -type (hole) conductivity. This would be the case for a silicon (group IV) matrix doped respectively with phosporous (group V) and gallium (group III). When put into contact with each other, these form a junction (Fig. 7.16). If two charge carriers, an electron and a hole, are released by an incident photon on the unbiased junction, then the voltage across it changes by an amount

![](images/59dfe3b3a37f28ce2f7f6e3c8aad19cdf9fe582cdc364bdc5f5488296e5b6486.jpg)  
Fig. 7.16 The principle of a junction between two semiconductors

$$
\Delta V = { \frac { e \delta x } { \varepsilon S } } \ ,
$$

where $\ S x$ is the thickness of the junction, $S$ its area, and $\varepsilon$ the electrical permittivity of the material. Absorption of a photon thereby results in a voltage across the junction, and this voltage can be measured by a high impedance circuit. This is the photovoltaic effect, discovered by A. Becquerel in 1839.

# Quantum Wells

Junctions can be made either from the same semiconducting material, but with different dopants in each part, or from two different materials (heterojunctions), in which case the band gap will differ from one side to the other. Starting from gallium arsenide AsGa, aluminium atoms can be inserted in the lattice to make $\mathrm { { A l } } _ { x } \mathrm { { G a } } _ { 1 - x } \mathrm { { A s } }$ . This is compatible with the crystal structure, and the result can be used to make junctions. A thin layer of AsGa sandwiched between two layers of $\mathrm { { A l } } _ { x } \mathrm { { G a } } _ { 1 - x } \mathrm { { A s } }$ has the effect of pushing the conduction band down to the level of AsGa. An electron crossing the junction remains trapped in the AsGa, which is thus a potential well. In such a quantum well, the electron can only have certain discrete and well-defined energies.

Infrared detectors can be made using this principle to construct a series of quantum wells, whose levels correspond in such a way that a photoelectron can pass from well to well by tunnelling, as far as the external electrodes.

![](images/a894dddf0f3ecd96ff660c23dbbd7232cf9cdd07eefdff9748bc511971f86791.jpg)  
Fig. 7.17 Superconductor–insulator–superconductor tunnel effect junction. (a) Energy level structure on either side of the insulator. Occupied states are shaded. The ordinate gives the energy and the abscissa the density of states. The superconductor energy gap is $2 \Delta$ . When $V$ is large enough to place occupied states on the left opposite vacant states on the right, a current can easily flow by the tunnel effect. If $e V < 2 \Delta$ , a photon may nevertheless excite a charge carrier to the energy at which the tunnel effect occurs (assisted tunnel effect). (b) Current–voltage characteristic of the junction. Continuous line: no flux. Dashed line: photons arriving. (Philips T.G., Woody D.P., ARAA 20, 285, 1982. Reproduced with the kind permission of the Annual Review of Astronomy and Astrophysics, 1982, Annual Reviews Inc.)

Photon Counting by Tunnel Effect

Consider a device made by sandwiching a thin insulating film ${ \approx } 1 0 ~ \mathrm { n m }$ ) between two superconducting electrodes. At low temperatures, this forms a junction called a superconductor–insulator–superconductor (SIS) junction. These junctions are commonly used as mixers in radiofrequency receivers (see Sect. 7.5). However, they also have promising applications for direct photon counting from X rays to the near infrared, where they are referred to as superconducting tunnel junctions (STJ).

Figure 7.17 shows how photons can be detected by such a junction.3 When there is no light flux and at temperature zero, a quasiparticle current can only pass through the insulating layer when the applied potential difference exceeds the sum of the gaps of the two superconductors, e.g., niobium, hafnium. If $T > 0$ , a dark current circulates whenever $\ S V \ne 0$ . Absorption of a photon in the superconductor breaks ¤a number of Cooper pairs that is directly proportional to the energy of the photon. This generates quasiparticles, which are then collected as current passing through the junction. The charges collected in this way can be amplified. Furthermore, an avalanche effect occurs because a quasiparticle induced by the photon can couple with a Cooper pair after crossing the insulating barrier, cross it again and be counted once more. Photon counting is a quantum mechanism, contains intrinsic amplification without noise (avalanche), and exhibits a certain spectral selectivity $( \leq 1 0 0 )$ .

# The Photochemical Effect

This effect is the basis of photography (developed by Nicephore Niepce, 1822, and Charles Daguerre, 1829). An incident photon excites an electron of the emulsion into the conduction band, and leaves a positively charged hole. The released electron is recaptured by a defect in the crystal lattice, and attracts a silver ion ${ \mathrm { A g } } ^ { + }$ to the site, thereby forming a neutral silver atom. The process repeats until a small cloud of silver atoms is produced, constituting one pixel, or element, of the latent image. The residual positively charged holes are able to move through thermal effects and then recombine with the silver atoms, which gives back silver ions. The processes of sensitising and hypersensitising photographic plates aim to destroy these residual holes. The production process for the emulsion creates the required defects in the crystal structure of silver chloride (AgCl) grains, by adding a suitable reducing agent (Gurney–Mott theory).

During development of the plate, a considerable amplification is produced, and a single silver atom released by a photon can give up to $1 0 ^ { 9 }$ atoms in the final image. The noise, or grain, of the plate is due to the formation of silver grains at the lattice defects without the action of an incident photon.

The quantum efficiency of a photographic emulsion is low, being of the order of $8 \times 1 0 ^ { - 3 }$ . This is indeed the main drawback of the photochemical effect. The threshold of the photochemical effect is governed by the value of the electron excitation energy in $\mathrm { A g C l }$ , or some other halide of this kind. This limits the sensitivity of plates at the infrared boundary of the visible $\lambda \le 8 0 0 \mathrm { n m }$ .

The detector using the photochemical effect is, of course, the photographic plate. As the bombardment of an emulsion by electrons can produce a latent image by the same process as the one described above, nuclear emulsions have been developed for the purpose of making latent images from electron impacts, and this is the principle of the electronic camera.

# Photoionisation of Gases

If the energy of incident photons is high enough $( \gtrsim ~ 1 0 ~ \mathrm { e V } ,$ ultraviolet or $\mathrm { X }$ -ray regions), an atom may be photoionised. The released electrons are then accelerated by an external electric field, and cause further ionisations by collision. The charges collected on the accelerating electrode are measured by a charge amplifier, or electrometer. The operating limit is reached when the multiplier effect leads to a discharge in the gas. Below this limit, the response is linear. It is not strictly correct to speak here of a quantum efficiency in the sense described earlier, for a photon may produce more than one electron, by double ionisation. However, extending the notion, $\eta$ will be used to denote the mean number of electrons obtained per incident photon. This quantity, which may exceed unity, is referred to as the quantum yield. The photoionisation cross-section in a gas is a function of the incident energy $E$ , varying as $E ^ { - 7 / 2 }$ . At around $1 0 \mathrm { k e V } ,$ , it becomes smaller than the Thomson scattering cross-section, and photoionisation is no longer usable.

The noble gases, neon, argon, and xenon, are used because of their high gain, the other common excitation mechanisms, such as rotation or vibration, being absent. An impurity, opaque to the UV radiation emitted by radiative de-excitation of the excited gas atoms, is added to the noble gas, in order to be able to use the energy for further ionisations. These impurities also de-excite the metastable states of the noble gas, by collisions.

The ionisation of gases is the basis of proportional counters. Wire chambers, invented by Georges Charpak,4 are used to detect events in the vicinity of particle accelerators. They are also based upon the photoionisation effect. The difference is that, in this case, the ionisation is not exclusively due to photons.

# Photon–Matter Interaction at High Energy $\mathbf { \Lambda } ( > 1 0 \mathrm { k e V } )$

The interaction of gamma rays with matter produces charged particles $\mathrm { e ^ { + } }$ and $\mathrm { e ^ { - } }$ ), which carry off the photon energy in kinetic form. The information concerning the energy and direction of the gamma photon is transferred to these particles, which interact, in turn, with other matter by ionisation, bremsstrahlung, annihilation, and so on. At low energies, loss of energy by ionisation is the dominant effect, the charged particles creating a series of electron–ion and electron–hole pairs. Most detectors use these charged pairs to detect the passage of a gamma photon, or to measure its energy by the number of charges produced.

The three main interaction processes are photoelectric absorption, Compton scattering, and pair creation.

# Photoelectric Absorption

In this process, all the photon energy $E _ { \gamma }$ goes to an electron in some atom. This interaction tends to occur with the inner shells (which have higher energy). The electron is ejected with kinetic energy equal to the difference between the incident photon energy and the energy required to extract the electron from its shell. As it propagates, the electron ionises atoms along its path. All the ions so formed then de-excite in a series of recombinations. In particular, the ion formed by the initial interaction of the photon de-excites, by emitting an X-ray photon which is characteristic of the shell of the ejected electron $( K , L )$ . If a thin layer of material is used for detection, some of these $\mathrm { X }$ -ray photons escape without further interaction, but in the majority of cases, they are not able to escape, and the totality of the energy of the gamma photon is then transmitted to the medium. The cross-section for the photoelectric interaction thus depends on the incident photon energy, and on the energy of atomic electrons in the medium. Discontinuities are observed at energies corresponding to the various shells of atomic electrons (see Fig. 7.18). However, to a first approximation, this cross-section is given by

![](images/84dea2a499230c880bb46ecb885d6e83d410243554f683c9e2edc3f1e9ac01dc.jpg)  
Fig. 7.18 Mass absorption coefficient as a function of incident photon energy. Note the $K$ shell ionisation discontinuities at low energy, and the energy dependence of the cross-section. (After Gursky H., Schwartz D., $X$ -ray Astronomy, Reidel, Dordrecht, 1974. With the kind permission of D. Reidel Publishing Company)

$$
\sigma _ { \mathrm { p } } = Z ^ { 4 . 5 } E _ { \gamma } ^ { - 3 . 5 } .
$$

Compton Scattering

In Compton scattering, only a part of the incident photon energy is transferred to the electron. The rest of the energy is carried away by the scattered photon, while the scattered electron, as in the case of the photoelectric effect, loses its energy mainly by ionisation of atoms along its trajectory. The scattered photon may also interact with the medium by a further Compton scattering, or by a photoelectric absorption. The directions of the incident and the scattered photon are determined by conservation of energy and momentum. The angle $\theta$ between them is related to the energy $E _ { \gamma }$ of the incident photon, and the energy $E _ { \mathrm { s } }$ of the scattered photon by

$$
\cos \theta = 1 - \frac { m _ { 0 } c ^ { 2 } } { E _ { \mathrm { s } } } + \frac { m _ { 0 } c ^ { 2 } } { E _ { \gamma } } .
$$

Figure 7.19 shows that the various scattering directions are not equiprobable. The dependence of the differential cross-section for the Compton interaction on the scattering angle $\theta$ is given by the Klein–Nishina formula

$$
\frac { \mathrm { d } \sigma _ { \mathrm { c } } } { \mathrm { d } \Omega } = \frac { 1 } { 2 } r _ { \mathrm { e } } ^ { 2 } \frac { E _ { \mathrm { s } } } { E _ { \gamma } } \left( \frac { E _ { \gamma } } { E _ { \mathrm { s } } } + \frac { E _ { \mathrm { s } } } { E _ { \gamma } } - \sin ^ { 2 } \theta \right) ,
$$

![](images/2d6369c8422911c3b53def0a08d38ce196fc146f8e8f4e16ee1c1a3e8116c49b.jpg)  
Fig. 7.19 Microscopic cross-section for Compton scattering, as a function of the scattering angle, at various energies. $r _ { \mathrm { e } }$ is the classical electron radius. The cross-section is given in $\mathrm { r a d } ^ { - 1 }$ , and is therefore an angular differential quantity

where $r _ { \mathrm { e } }$ is the classical electron radius $( r _ { \mathrm { e } } = 2 . 8 2 \times 1 0 ^ { - 1 5 } \mathrm { m } )$ , and $\mathrm { d } \varOmega$ the element of solid angle around direction $\theta$ D . The higher the energy, the more likely it is that the photon will scatter forwards. The total cross-section for the Compton interaction goes approximately as

$$
\sigma _ { \mathrm { c } } \propto Z E ^ { - 1 } .
$$

# Pair Creation

In this process, a high energy photon $E \gg 1 \mathrm { M e V }$ ) interacts with the electric field of a heavy nucleus to create an electron–positron pair. The photon energy is divided between the mass energy of the pair, equal to $1 . 2 2 \mathrm { M e V } _ { \mathrm { : } }$ , and their subsequent kinetic energy. Although the momentum carried by the nucleus ensures conservation of momentum for the reaction, its recoil energy can be neglected. In the centre of mass frame, the electron and positron are emitted in opposite directions. During propagation, they gradually lose their energy, mainly by ionisation, bremsstrahlung, and the Cherenkov effect. When the positron energy is low enough $( \approx 1 \mathrm { \ k e V }$ ), it will annihilate with an electron in the medium, by the inverse reaction, emitting two photons at $5 1 1 \mathrm { k e V }$ in opposite directions. These photons may escape, or they may in turn interact with the medium by Compton scattering or photoelectric absorption.

The cross-section for pair creation varies roughly as $Z ^ { 2 }$ , and is characterised by its threshold of $1 . 2 2 \mathrm { M e V } .$

# Comparison of Processes

The energy dependence of the three interaction processes mentioned above means that each one will be predominant in some energy domain determined by the interaction medium. At low energies, photoelectric absorption dominates, and at high energies, pair creation is the main channel. The energy domain for Compton scattering is situated between the two. Its width is highly dependent on the atomic number $Z$ of the material (Fig. 7.20), increasing for lighter materials. Generally speaking, for equal mass surface densities, light materials tend to scatter, and heavy materials tend to absorb.

Compton scattering and pair creation are the physical processes exploited in scintillation counters or scintillators, as well as in semiconductor detectors. The applications to $\gamma$ ray astronomy will be discussed in Sect. 7.6.

Thermal Effects. Calorimetry

Once the photon energy has been transferred to the solid, which constitutes the detector, and transformed into thermal excitations, the incident radiation is revealed by the slight temperature change it has produced, and which can be measured by the consequent variation in resistivity. In order for this to work correctly, the only condition is that the solid should be as absorbent to photons as possible, not only absorbing incident photons, but also any products of secondary events.

![](images/a45758c76fc21b07a127093324de7a7d2e93b3050ca34d66065ccd18bb0a1231.jpg)  
Fig. 7.20 Energy domains associated with each interaction process between $\gamma$ rays and a material, as a function of its atomic number Z. Curves correspond to loci of equal cross-sections for the two processes they separate

The thermal effect is used in detectors called bolometers, mainly in the infrared and submillimetre regions. It is also used in calorimeters, which measure the energy of $\gamma$ rays.

# 7.3.2 Detection of the Electromagnetic Field

At wavelengths above about $0 . 2 \ \mathrm { m m }$ , no quantum detector in the sense described above, involving release of one photocharge by one incident photon, has yet been devised. Across the whole of the radiofrequency region, other detection processes must be employed to measure the electric field of the incident wave. Its electromagnetic field, or the current it induces in an antenna, are applied to a nonlinear element called a diode or a mixer, usually superposing this field on the field of a local oscillator. The choice of non-linear element and mixer determines the final detection performance. We shall thus postpone discussion of these issues to a full presentation of the various elements.

# 7.4 Astronomical Detectors from X Ray to Submillimetre

Since the 1970s and 1980s, a genuine revolution has transformed the kind of detectors used in astronomy. The driving force here has been the emergence of microtechnologies, contributing to the design of light detectors across the board from X ray to submillimetre wavelengths with levels of sensitivity (quantum efficiencies) that have quickly superseded traditional photography, along with the various systems that had been developed to supplement it. In addition to this new level of performance, direct digitisation of the signal has greatly facilitated transmission, storage, and processing, and it has also brought mechanical advantages by making it easier to equip space observatories or remote missions.

In this context of rapid progress, yesterday’s detectors are often mentioned only for completeness, to describe the historical role they have played and explain references to them in the literature. However, one must not forget the extraordinary wealth of data contained in photographic astronomical archives, collected throughout the twentieth century and available today for the main part in digitised form (see Chap. 10). In the first section here, we consider more traditional detectors, mainly exploiting the generation and transfer of charge in semiconductors and appealing to microelectronics for their fabrication.

Outside this broad spectral range from X ray to submillimetre wavelengths, detectors in the $\gamma$ ray region on the one hand and radiofrequency receivers on the other have not witnessed similar revolutions. Figure 7.21 gives an overview.

![](images/ce93b361e5e4166219477dd2d08f80f38f13a93051d69f11bec873d0ad73ba6a.jpg)  
Fig. 7.21 Astronomical detectors

# 7.4.1 Noise Performance

At the beginning of this chapter, we discussed fundamental physical noise due to the Poissonian nature of the light–matter interaction or the thermodynamics of a thermal equilibrium. Of course, a given detector rarely achieves this ultimate level of performance. The true performance of a detector thus depends on what fluctuations it may add to those of the signal itself (signal noise) and to those of the detector environment (background noise). It is therefore important to qualify these real performance levels since they will influence the final quality of an observation.

# Detector Quantum Efficiency

The detector quantum efficiency (DQE) $\delta$ quantifies this notion. It extends the idea of quantum efficiency $\eta$ already introduced, but should not be confused with it. The definition is

$$
\delta = \mathrm { D Q E } = \frac { \left( \langle \Delta N ^ { 2 } \rangle / \overline { { N } } ^ { 2 } \right) _ { \mathrm { r e a l \ d e t e c t o r } } } { \left( \langle \Delta N ^ { 2 } \rangle / \overline { { N } } ^ { 2 } \right) _ { \mathrm { i d e a l \ d e t e c t o r } } } \ .
$$

It is straightforward to show that, if the detector, of quantum efficiency $\eta$ , introduces no further fluctuations, only the Poisson statistics of the incident photons remains, and

$$
\begin{array} { c } { { \langle \Delta N ^ { 2 } \rangle _ { \mathrm { i d e a l } } = \overline { { { N } } } \ , } } \\ { { \langle \Delta N ^ { 2 } \rangle _ { \mathrm { r e a l } } = \eta \overline { { { N } } } \ , \qquad \overline { { { N } } } _ { \mathrm { r e a l } } = \eta \overline { { { N } } } _ { \mathrm { i d e a l } } \ . } } \end{array}
$$

In this case, $\delta = \eta$ , which justifies the name given to $\delta$ .

DAs well as the fundamental fluctuations linked to the radiation itself, a detector may be subject to amplifier noise and readout noise.

# Amplifier Noise

Some photoelectric detectors (photomultipliers, the avalanche effect in avalanche diodes, or CCDs in the X-ray region) exploit the following sequence of events upon impact by a photon: 1 photon $ \eta$ photoelectrons amplification $\to \eta g$ electrons !measurement. The amplification gain $g$ ! !is a random variable of mean $\overline { { g } }$ and !standard deviation $\sigma _ { g }$ , from one photon impact to another. The noise this creates in the signal is not additive but multiplicative, degrading the DQE by the factor

$$
\left( \frac { 1 + \sigma _ { g } ^ { 2 } } { \overline { { g } } ^ { 2 } } \right) ^ { - 1 } .
$$

# Readout Noise

Some detectors (e.g., CCDs, see Sect. 7.4.6) measure at regular intervals the photocharges accumulated since the last measurement. Each charge transfer is then accompanied by a fluctuation, whose standard deviation is measured in numbers of electrons per reading. This number is the readout noise, or noise equivalent charge (NEC). Being a standard deviation, it will be denoted $\sigma _ { \mathrm { R } }$ , given in rms electron number.

The value of $\sigma _ { \mathrm R }$ for a given device may depend on the rate at which readings are made, and therefore on the integration time $T$ . In general, $\sigma _ { \mathrm R }$ increases as $T$ decreases. However, $\sigma _ { \mathrm R }$ no longer exhibits the standard $T ^ { 1 / 2 }$ dependence of integrated noise (see below).

The DQE is degraded by a factor

$$
\left( \frac { \sigma _ { \mathrm { R } } } { \overline { { g } } \eta \sqrt { \overline { { N } } T } } \right) ^ { 2 } \ ,
$$

so that, in the most general case,

$$
\delta = \eta \left[ \left( 1 + { \frac { \sigma _ { g } ^ { 2 } } { \overline { { { g } } } ^ { 2 } } } \right) + { \frac { \sigma _ { \mathrm { R } } ^ { 2 } } { \overline { { { g } } } ^ { 2 } \eta ^ { 2 } \overline { { { N } } } T } } \right] ^ { - 1 } ,
$$

where $\overline { { N } }$ is the mean photon flux per second, $T$ the readout time, the fluctuations being quadratically additive.

Problem 7.4 concerns the expression for the DQE when the dark current is included, and also an extension of the definition of $\boldsymbol { \delta }$ to the case of an imaging detector, including spatial frequencies.

# 7.4.2 Photographic Plates

Considerable progress has been made in the sensitivity of photographic plates, over the period since their invention, going from a flux of $1 0 ^ { - 4 } \ \mathrm { J } \mathrm { c m } ^ { - 2 }$ as required to print a plate in 1850, to a flux $1 0 ^ { 6 }$ times lower a century later. We can nevertheless consider that it has reached its limit today. The main advantages are simplicity of use, ability to integrate low fluxes over long periods, and, above all, the high number of pixels that can be simultaneously exposed (up to $1 0 ^ { 1 0 }$ ). It is its own mass memory.

![](images/00493fefe1af14e4636cbe8072174a21a6706bbf445574b1d77a7448c02ca7d3.jpg)  
Fig. 7.22 Left: Microphotometry of a photographic or electronographic plate. The light source L emits a ray, received by the photosensitive cell C. The intensity i measured, together with the $x$ and $y$ coordinates, read by a position sensor, are digitised. L performs a two-dimensional raster scan. Right: Isophotes of the jet emerging from the quasar 3C 273 obtained by digitising the plate. Note the oscillation of the jet around its mean direction. Picture courtesy of Wlerick ´ G., Lelievre G., Canada–France–Hawaii telescope, wide field electronic camera, U filter (near\` ultraviolet), exposure $1 6 5 \mathrm { m i n }$ , 1984

The drawbacks are its non-linearity, its rather restricted dynamic range, the grain effect, and also the need to use a microdensitometer (Fig. 7.22) to transform analogue information, stored in the form of blackening on the plate, into digital information, which can then be processed quantitatively. This point by point scanning process is still used by the modern scanner to digitise documents.

In order to set up digital archives of photographic records like those described in Chap. 10, machines have been built to measure and digitise astronomical photographic plates. These machines, which were developed in the 1990s, are capable of processing enormous numbers of pixels. Examples are MAMA, or Machine $\grave { a }$ Mesurer pour l’Astronomie, in France, and COSMOS, in the United Kingdom.

The registered signal is measured by the density of the emulsion. If the pixel being examined by microdensitometer transmits a fraction $I / I _ { 0 }$ of the incident radiation, the density $d$ is defined by

$$
d = - \log _ { 1 0 } { \frac { I } { I _ { 0 } } } .
$$

The photographic plate remains a useful detector but, despite its high number of pixels (up to $\sim 1 0 ^ { 1 0 }$ ), it has now been superseded by CCD arrays which, at the time of writing (2007), can count up to $1 0 ^ { 8 }$ pixels.

# 7.4.3 Photomultipliers and Classical Cameras: X Ray, UV, and Visible

Once again, these detectors played an important role over the period 1950–1990, but were then completely superseded by CCDs and similar detectors. They worked by photon counting.

# Photomultipliers (PM)

For many years regarded as the ideal detector, the photomultiplier (abbreviated to PM) consists of an evacuated tube containing a series of electrodes, the first of which is exposed to the radiation. When a photoelectron is released, it is extracted from the photocathode by means of a first dynode, or positive electrode, creating secondary electrons by impact. These are in turn accelerated, causing further electrons to be released, and the process continues. The final current is measured with a charge amplifier or electrometer. The photomultiplier nevertheless remains widely used in high energy $\gamma$ -ray) detectors, where it detects the photons induced by interactions and counts them (see below).

Based on the photoelectric effect, there is no sensitivity threshold, and indeed the photomultiplier can detect a single quantum. It is perfectly linear up to the point where the flux is high enough to cause an electron cascade, which destroys the electrodes. Its sensitivity is limited to the region 20 to $1 2 0 0 \ \mathrm { n m }$ , by cascade effects in the far UV, and the photocathode response in the near IR. Figure 7.14 gives the response and the quantum efficiency. The PM has almost no spectral selectivity, and its response time is extremely short (the transit time of the electrons between dynodes, which is several nanoseconds). It clearly has no multichannel capabilities (except for certain configurations, which channel the photoelectrons and can discriminate between points of the photocathode), and the response of the photocathode may vary somewhat across its surface. These characteristics are summarized in Table 7.4.

At non-zero temperatures, thermoelectronic emission from the cathode produces accelerated electrons, even when there are no incident photons. Richardson’s law gives the value of the current density $j$ extracted at temperature $T$ , for an extraction potential of $E _ { \mathrm { s } } / e$ :

$$
\begin{array} { l } { { \displaystyle j = \frac { 4 \pi e k ^ { 2 } } { h ^ { 3 } } \left( 1 - \rho _ { \mathrm { e } } \right) T ^ { 2 } \exp \left( - \frac { E _ { \mathrm { s } } } { k T } \right) } } \\ { { \displaystyle = 1 . 2 \times 1 0 ^ { 6 } \left( 1 - \rho _ { \mathrm { e } } \right) T ^ { 2 } \exp \left( - \frac { E _ { \mathrm { s } } } { k T } \right) \mathrm { A m } ^ { - 2 } , } } \end{array}
$$

where $\rho _ { \mathrm { e } }$ is the coefficient of reflection, measuring the probability of the electrodes recapturing an emitted electron. At $T = 3 0 0 \mathrm { K }$ , and for $S = 1 \mathrm { c m } ^ { 2 }$ , $E _ { \mathrm { s } } = 1 \mathrm { e V } ,$ it follows that $I = j S = 0 . 2 \mathrm { n A }$ . D DThis is a large dark current. For comparison, with $\eta = 0 . 5$ D D, a flux of one photon per second would produce a current of $0 . 8 \times 1 0 ^ { - 1 9 }$ A (Table 7.4).

The dark current decreases rapidly with $T$ (if the photomultiplier is cooled with dry ice or a Peltier refrigerator). It also decreases when $E _ { \mathrm { s } }$ increases (this concerns UV photocathodes). Although the mean value $\begin{array} { l l l } { \langle j S \rangle } & { = } & { \left. i _ { \mathrm { B } } \right. } \end{array}$ of the dark current can be subtracted from the hmeasurements, its fluctuations $\langle \ S i _ { \mathrm { B } } ^ { 2 } \rangle = 2 e \langle i _ { \mathrm { B } } \rangle \Delta f$ , where $\Delta f$ is the passband of the electric filter h i D h iwhich follows the PM, set a fundamental limit to the sensitivity (Problem 7.1).

Table 7.4 Photomultipliers   

<table><tr><td>Threshold</td><td>One quantum</td></tr><tr><td>Format</td><td>Up to 8×8pixels</td></tr><tr><td>Quantum efficiency</td><td>0.43 (Ag-O-Cs at 800 nm) to 0.1</td></tr><tr><td>Spectral response</td><td>Wide</td></tr><tr><td>Temporal response</td><td>Nanosecond</td></tr><tr><td>Size</td><td>About 10 cm² (cathode)</td></tr><tr><td>Noise</td><td>Dark current OB ~ 10 counts Hz-1/2</td></tr><tr><td>Polarisation</td><td>Insensitive</td></tr></table>

With the above current, and taking $\Delta f = 1 \ : \mathrm { H z }$

$$
\langle \ S i _ { \mathrm { B } } ^ { 2 } \rangle ^ { 1 / 2 } = 9 \times 1 0 ^ { - 1 5 } \mathrm { A H z ^ { - 1 / 2 } } .
$$

The signal can be measured in various ways.

• By integration of charge: a filter circuit (resistor and capacitor), or an integrating circuit (running mean), provides a continuously variable analogue voltage. By counting photon arrivals: a counter registers each burst of electrons, whatever their number and whatever the duration of the burst. The signal is digitised, and the intensity and duration of the pulses can be used to protect against unwanted signals.

# Other Photon Counting Detectors

Much effort has been made to combine the advantages of the photoelectric effect in vacuum and the detection of 2D images. Here we give a brief overview of the sometimes imaginative systems devised through 1950–1990, but which have for the main part been superseded by CCDs (see below).

Electronic Camera (or Electronographic Tube)

Invented and first exploited by A. Lallemand, the electronic camera consists of a photocathode on which an image $I ( x , y )$ is formed. The photoelectrons produced are accelerated by electron optics with electrostatic or magnetic focusing, and then an electron image is formed on a high contrast photographic plate (nuclear emulsion). The camera can operate at extremely low levels of intensity. Indeed, it does not exhibit the threshold effect of the normal photographic plate, and can almost detect single photoelectrons. The time integration capacity in long exposures is excellent (there is no fogging), and the advantages for astronomical photography are clear, particularly for faint objects, such as quasars, which require an accumulation of long exposures (Fig. 7.22).

Image Intensifiers Using Microchannel Plates

The input for an image intensifier is an image, formed by a low flux of photons, at a certain wavelength. The output from such device consists of an image with the same number of pixels. Each output pixel behaves as a source of photons, whose number is proportional to the number of incident photons, but whose wavelength is different. The system is therefore characterised by a gain g.

![](images/76e8689a3c65489acf671def8cdb2015d219d3089da7e071d857c10a632ec891.jpg)  
Fig. 7.23 (a) Microchannel in a semiconductor, constituting one element of a microchannel plate. The incident photon releases a photoelectron, which is accelerated by the field $E$ , and multiplied by successive electronic collisions. The phosphor is excited at the exit and emits a large number of photons. (b) The phosphor emits across a wide solid angle and this requires fibre optic coupling. Each fibre is in contact with the phosphor and transmits the photons corresponding to one pixel to the CCD detector. The figure shows straight channels to simplify, but in general they are curved in order to prevent ion movement

The microchannel plate or channeltron is an intensifier, exploiting the photoelectric effect in solids. The photoelectrons are guided and multiplied in a channel with accelerating voltage gradient (Fig. 7.23). The final impact is on a phosphor, which emits in the visible. The incident photons may be visible, ultraviolet, or soft X rays. Several microchannel plates can be arranged in series, in order to increase the amplification factor.

A microchannel plate has no information storage capacity, and so could not be used alone. Hence it is coupled to a CCD, and the two together are referred to as an intensified CCD.

# Photon Counting Television

Inspired by the tubes developed for commercial television in the 1950s, many improvements were brought to bear to increase their sensitivity, to arrive at a genuine photon counting device (Fig. 7.24). A whole series of astronomical detectors was thereby developed.

Vidicon Tubes and Derivatives. Television tubes use the photoelectric effect in silicon. Released photoelectrons are stored in a layer of microcapacitors, which are periodically recharged (25 times a second) by a scanning electron beam, the Vidicon tube. The recharge current of the microcondenser is modulated by the light intensity. Passing through the charge resistance of the target, it produces a potential difference, which is the video signal, at a frequency of a few tens of MHz. The readout noise is high $( \sigma \sim 2 \times 1 0 ^ { 3 }$ electrons pixel $^ { - 1 } \mathrm { H z } ^ { - 1 / 2 }$ ), and is easily observed on the TV screen: the background, in the absence of any signal, appears as a random pattern of white on black, like snow.

![](images/062c1905c36161a93b188e2142850258b49914a08a435e0e990c288d5a2b4545.jpg)  
Fig. 7.24 Photon counts, as they appear on the TV screen of a Nocticon tube (exposure $2 5 ~ \mathrm { m s }$ ). Note the variable gain, manifested by the varying brightness of the events. Note also the noise events, fainter and easy to discriminate. The image is read on a $5 1 2 \times 5 1 2$ CCD array. Each event is digitally centered. (Observatoire de Marseille, image due to Boulesteix J. in the 1980s)

In the secondary electron conduction tube or SEC tube, the photoelectrons are accelerated onto a target where they produce a secondary emission of electrons. The latter are read by standard TV scanning. The gain of around 1 000 is obtained at the cost of high non-linearity.

In the silicon intensified target (SIT) tube, or the electron bombarded silicon (EBS) tube, the photoelectrons are accelerated onto a silicon target at sufficiently high energy to create several thousand electron–hole pairs upon each impact. These are then collected by an array of junctions or diodes. The electric field of the diode separates them and they discharge a microcapacitor, which is then recharged by the scanning electron beam. An analogous principle is used in the electron bombarded CCD (EB-CCD).

The Photon Counting Camera. The image photon counting system (IPCS) combines the linearity and sensitivity of the electronographic camera with the convenience of the TV camera, and a capacity for digital storage of information, which can be processed at a later date. It was developed by Alec Boksenberg5 in Cambridge (UK), and was soon being widely used in astronomical observatories, until it was replaced by CCDs. A photon counting camera was designed and made in Europe to equip the Hubble Space Telescope in the 1990s. This camera, the Faint Object Camera (FOC), was used to make the first deep sky observations with this telescope, before being replaced in orbit by CCD detectors, installed by astronauts during servicing missions.

This camera includes an image intensifier : photons incident on the photocathode generate photoelectrons, which are accelerated and focused magnetically onto a phosphor. The latter re-emits photons upon each impact. The amplification process is repeated in three successive stages, to give a final gain of $1 . 3 \times 1 0 ^ { 5 }$ .

The intensifier is followed by optics. The image, formed on the output phosphor of the intensifier, is re-formed by an objective on the entry side of a cylindrical bundle of optical fibres, which define each pixel with great precision. The photons are then channelled onto the photocathode of an EBS television tube. Each photon impact is converted into a pulse in the output video signal, and the timing of each pulse is used to determine exactly which event should be assigned to which pixel in the image. The digitised video signal increases by one the number of photons so far counted in the pixel.

This sequence of devices had many advantages: the system involved almost no noise, reading was non-destructive, the $5 1 2 \times 5 1 2$ pixel format was good at the time, and photon impacts could be accurately localised. Figure 7.24 gives an example of the instantaneous image obtained using a photon counting camera.

Other versions of the photon counting camera were developed during the 1980s, such as the connection of two image intensifiers in series, followed by a CCD. Another idea couples an electronic camera (photocathode with acceleration of the photoelectrons) to a CCD operating in an unusual but effective way: bombarded by the accelerated electrons, each pixel releases a large number of charges which are then read by the readout circuit (EB-CCD, or electron bombarded CCD).

# Avalanche Photodiodes

Consider a junction which is strongly biased in the opposite direction, and hence non-conducting. The diode material being silicon, an incident photon generates a photoelectron. The very high bias (several $\mathrm { \Delta V _ { \mathrm { \ : \mu } m } } ^ { - 1 }$ ) accelerates this electron, which photoionises in series the Si atoms it encounters. The process is amplified by avalanche multiplication until a current pulse is created across the poles of the diode. This current pulse may reach $1 0 ^ { 9 }$ charges, which is easy to detect above the intrinsic noise of the diode. Count rates can reach $1 0 ^ { 6 }$ photocharges per second.

This device has a very fast response, reaching several nanoseconds. The photoimpulses can thus be counted individually, a pause of several hundred nanoseconds being required to restore the charges (quenching). A promising application may be the study of radiation coherence by correlation.

The great advantage of these ‘solid-state photomultipliers’ is that they can work in counting mode (and therefore with the limit imposed by the Poisson noise of the signal), whilst benefiting from the excellent quantum efficiency of silicon $( > 0 . 6 )$ . An extension of this idea to the near infrared, using germanium, can be envisaged. Their limitation is two-fold. Firstly, the diodes are cumbersome and it is difficult to assemble them into arrays, although arrays containing several units or several tens of units became available by the 2000s, and it may be that $1 0 0 0 \times 1 0 0 0$ arrays will appear one day. Secondly, the recombination of charges produces a flash of light, and although this presents no problem when limited to a single diode, it soon becomes problematic in the case of arrays, because it leads to cross talk between neighbouring pixels.

Compared with photomultipliers, which are their close relatives, they are still limited by the smaller dimensions of their photosensitive zone. Nevertheless, they are fast developing, and sizes up to $2 0 0 ~ \mathrm { m m } ^ { 2 }$ have been achieved. In 2007, these detectors face serious competition from L3- CCDs (see below).

# 7.4.4 X-Ray Detection (0.1–10 keV)

Here we discuss a family of photon counting detectors developed hand in hand with the emergence of X-ray astronomy, and which in the 2000s have gradually been superseded by CCD detectors, presented later.

# Proportional Counters

Figure 7.25 gives a schematic view of a proportional counter. The window enclosing the gas must be thin, and it is the specific combination of the absorption properties of this window and those of the gas which determines the spectral response of the counter. Table 7.5, which is not exhaustive, thus specifies the spectral ranges that can be covered. Note the extreme thinness of the windows, and the properties of the ionisation thresholds in the absence of the window.

The energy resolution is, like the quantum efficiency, determined by the combination of the gas properties (photoelectric cross-section of the gas) and those of the window (Fig. 7.26). This resolution is determined by the Poisson statistics of the photoelectrons, and is thus proportional to ${ \sqrt { E } } .$ In general,

$$
\Delta E _ { \mathrm { k e V } } \approx 0 . 4 \sqrt { E _ { \mathrm { k e V } } } ~ ,
$$

the proportionality factor dropping to 0.2 in gas scintillation proportional counters (GSPC).

![](images/58a5964ee790f73d1f96829698496d5769e50a333d68f012d652ca1c1451cb0e.jpg)  
Fig. 7.25 Exploded view of a proportional counter

Table 7.5 Proportional Counters   

<table><tr><td>Window</td><td>Thickness [μm]</td><td>Gas filling</td><td>Spectral response [nm]</td></tr><tr><td>Beryllium</td><td>125</td><td>Neon or argon</td><td>0.02-0.8</td></tr><tr><td>Aluminium</td><td>6</td><td>Neon</td><td>0.02-0.6 and 0.8-1.6</td></tr><tr><td>Mylar</td><td>6</td><td>Nitrogen or helium</td><td>0.02-1.5 and 4.4-6</td></tr><tr><td>Nitrocellulose</td><td>0.1</td><td>Argon</td><td>&lt;30</td></tr><tr><td>No window</td><td>1</td><td>Helium</td><td>&lt;50.43</td></tr><tr><td>No window</td><td>1</td><td>Xenon</td><td>&lt;102.21</td></tr><tr><td>Lithium fluoride</td><td>1000</td><td>Ethyl bromide</td><td>104-120</td></tr><tr><td>Quartz (silicon)</td><td>1000</td><td>Tri-n-propyl amine</td><td>160-171.5</td></tr></table>

![](images/cedde8b5b0bf0669ad844d1d9ef4af52ea8f28d02ad9b587ecab5099185e67e6.jpg)  
Fig. 7.26 Quantum efficiency of a proportional counter filled with argon (column density $5 . 4 \mathrm { m g } \mathrm { c m } ^ { - 2 }$ ). The effect of different windows is shown. From Giacconi R. and Gusky H., $X$ -Ray Astronomy, Reidel, Dordrecht, 1974. With the kind permission of D. Reidel Publishing Company

The proportional counter has no intrinsic noise, but suffers from amplification noise (gains of the order of $1 0 ^ { 3 } – 1 0 ^ { 5 }$ ). Only the statistics of the signal, whether it be the source or a background signal, can therefore create fluctuations, and this alone will determine the signal-to-noise ratio. This idea was extended in the 1970s to the position sensitive proportional counter, which equipped the camera of the Einstein satellite, launched in 1978.

# Microchannel Plates

Already described in the context of image intensifiers used in the detection of visible and ultraviolet radiation (see Sect. 7.4.3), this device can be used to make multichannel detectors, without energy resolution, for energies up to several keV. Figure 7.27 shows an image obtained with such a detector on the Exosat satellite, launched in 1982, the first X-ray satellite of the European Space Agency.

# 7.4.5 Solid-State Imagers

These detectors exploit the photoelectric effect in solids. Their multichannel character results from integrating elementary photoconducting pixels into an integrated array, which includes a readout circuit. State-of-the-art microelectronics is used in their manufacture. They have developed considerably since their introduction in 1970 and the trend continues, with improved performance in sensitivity, dynamic range, format, miniaturisation, reliability, and integrated intelligence. They produce a digital output signal which is easy to process and have a temporal integration capacity.

![](images/da696558ddc963d397b7726dec84065693c81b1a6496be6192dadcf118701685.jpg)  
Fig. 7.27 Historical X-ray image of the supernova remnant Cassiopea A, obtained with the microchannel camera (Channel Multiplier Array, or CMA) on the European satellite Exosat. Spectral band $0 . 1 { - } 2 \mathrm { k e V } .$ Spatial resolution 18 arcsec, on the optical axis. (Picture provided by the Exosat Observatory, European Space Agency, 1985)

These detectors are known generically as solid-state imagers. The term covers many variations, such as Reticons, charge coupled devices (CCDs), and charge injection devices (CIDs). At visible wavelengths, it is the CCD exploiting the photoconductivity of silicon which has taken the lead since the end of the 1980s. For infrared detection, microelectronic integration techniques have made it possible to superpose a suitable photosensitive material for the given wavelength and readout circuits, thus constructing the equivalent of a CCD at these wavelengths. Finally, recent developments, in the 2000s, have created a competitor for the CCD, namely the CMOS (complementary metal oxide semiconductor) detector.

The strategy in solid-state imagery is to accept a gain close to unity, but to reduce the readout noise $\sigma _ { \mathrm { R } }$ to near zero, so that the detector quantum efficiency ı attains the value of the photoelectric quantum efficiency $\eta$ . The trend is also to make the latter tend toward unity.

# 7.4.6 Charge Coupled Device (CCD)

The basic structure of a charge coupled device is a metal–oxide–semiconductor (MOS) capacitance. It is a capacitance consisting of an insulator sandwiched between a metal electrode and a semiconductor exhibiting the photoelectric effect (Fig. 7.28). The insulator may be formed by direct oxidation of the semiconductor ( $\mathrm { S i O } _ { 2 }$ on silicon), or it may be deposited by vaporisation, sputtering, or condensation in the vapour phase. The semiconductor is usually silicon.

![](images/c750034d4495e563d110c5b0dd30229d3ea503f7d80b5d3c756da86534f34d30.jpg)  
Fig. 7.28 Metal–oxide–semiconductor (MOS) capacitance. The voltage applied at the upper electrode acts on mobile charges in the $n$ -type semiconductor. For $V > 0$ , the majority carriers $( \mathrm { e } ^ { - } )$ accumulate at the surface under the insulator. For $V < 0$ , the majority carriers $( \mathrm { e } ^ { - } )$ are repelled far from the surface, creating a depopulated or depletion zone, without mobile charges, which is thus insulating. For $V \ll 0$ , a positively charged inversion layer is formed at the surface, and this is a potential well for the minority carriers ( $^ +$ holes). The photocharges caused by incident photons $( h \nu )$ C modify the surface potential. The lower electrode can be made transparent to radiation, freeing the upper part for the electrical connections of the readout circuit

The applied potential difference creates an electric field which modifies the charge distribution in the semiconductor. A potential well appears, capable of storing in the capacitance any photocharges released in the semiconductor by an incident photon, as well as any thermally excited mobile charges. This last phenomenon makes it necessary to cool solid-state imagers, in order to reduce the thermally generated signal.

Each pixel of the CCD comprises a capacitance of this kind, and the full set of pixels is organised in a 2D array forming the detector array of $N \times M$ pixels which specifies the $N \times M$ format of the CCD. Once the charges have accumulated, the CCD contains a readout circuit, using field effect transistors (FET) that function as switches and also a clock, which transfers the charges of a given column one after the other into an output series register and then, having done this, moves on to the next column, until all the stored charges have been read. The charges are transformed into successive voltage pulses by the series register, and these are amplified then digitised in a synchronised way by the clock controlling readout. The CCD controller oversees the electronic functions. Photosites have been gradually reduced in size with progress in silicon etching techniques, to reach a few micrometres.

Figure 7.29 illustrates the idea of charge transfer driven by a clock-controlled variation of potential at successive electrodes in rows and columns. The output signal is thus a video-type signal, in which each pulse is proportional to the stored photocharge. The image can then be generated at the standard TV rate of 25 frames per second (in Europe), but it can also be read at an arbitrarily slow rate (long exposures).

![](images/ddfa0d63d2a9e75a749146dd6fc1337323b21d582913a96648d918d85e2a9737.jpg)  
Fig. 7.29 Principle of charge transfer in the CCD detector. Each pixel is defined by three electrodes. Electrons are represented by balls, which move within the potential wells created by the electrodes, and evolve in time. (After Fauconnier T., doctoral thesis, University of Paris VII, 1983)

When all functions, i.e., release of photocharges, storage, and transfer to the output register, are handled within the same pixel, the CCD is said to be full frame. However, it also possible to separate these functions in the so-called frame transfer $C C D$ . A $2 N \times N$ array is divided into two parts, with one $N \times N$ piece used to generate the charges and the other $N \times N$ piece storing them. If the transfer from one to the other is very fast $\mathit { \Theta } _ { \prec \phantom { \infty } 1 0 }$ ms for a $1 \mathrm { k } \times 1 \mathrm { k }$ format, the time depending on the number of rows), the use of time is optimal, since the charges can be read out while the exposure is still underway. This doubles the size of the final array, which may complicate image formation when a large focal plane is to be covered by CCDs placed side by side.

# Quantum Efficiency. Thinned CCDs

Impressive progress has been made with the quantum efficiency of CCDs in the visible wavelengths $( 4 0 0 { - } 9 0 0 ~ \mathrm { n m } )$ . Figure 7.30b shows efficiencies almost equal to unity in the extreme red, and greater than $50 \%$ in the blue. Most of the loss of efficiency is due to reflection losses. There is a great reduction in sensitivity when CCDs are used in the blue $\leq 4 0 0 \ \mathrm { n m }$ ) and ultraviolet, because silicon can absorb photons at these wavelengths.

![](images/a141bc568903b18aff5619f22c3c66328f0a78163dd175dd6b8f6b1c4ac5563d.jpg)  
Fig. 7.30 (a) Schematic cross-section of a thinned CCD. The limited extent of the potential wells is shown, as is the depletion zone that the photocharges must reach. (b) DQEs for front illumination and for anti-reflectance treatment. (After Lesser M., 1994)

The electrodes placed on the front face absorb the radiation. This led to the idea of illuminating the CCD from behind, so that the radiation would only encounter silicon immediately effective in photoelectric conversion. However, as a CCD was around $3 0 0 ~ { \mu \mathrm { m } }$ thick, the photocharges had to cover such a distance before encountering the potential wells, whose extension under the electrodes barely exceeds $1 0 ~ { \mu \mathrm { m } }$ , that the charges would never be able to recombine. Illuminating the CCD from behind therefore required the CCD to be thinned down, to a thickness of about $1 5 ~ { \mu \mathrm { m } }$ . A compromise must be found between the capture of photocharges and their generation, which requires a photon path in the silicon that increases with the wavelength. Thinning is thus necessary in the blue, and of course for UV and $\mathrm { X }$ -ray detection, but unfavourable for the high quantum efficiency in the red. It is impossible to make silicon wafers of this thickness directly. A standard CCD is thus turned round, with its front face stuck onto a suitable substrate, and then its back face is thinned by mechanical or chemical processes, passivated (antioxidant treatment), and treated to reduce reflection losses (Fig. 7.30a).

# Readout Noise

The transfer of photocharges and ensuing amplification are accompanied by two sources of noise, whose (quadratic) sum is generally observed. On the one hand, there is a fluctuation in this number of charges. This has thermal origins and depends on the capacitance storing the charges. On the other hand, there is a further fluctuation $\sigma _ { \mathrm R }$ due to transfer and amplification of the signal, called the readout noise of the CCD. Each of these terms is reduced by cooling the CCD, generally to the temperature $7 7 ~ \mathrm { K }$ of liquid nitrogen.

The ultimate readout noise depends on the read rate. Indeed, the noise level decreases as the CCD is read more slowly, going as $1 / f$ in the amplification stages. But increasing formats implies reading a larger number of pixels, and this has consequences for the readout noise, which has decreased at the time of writing (2007) to a few photocharges (1–2 electrons rms) at rates of 50 kilopixels per second (or 20 s to read a $1 0 2 4 \times 1 0 2 4 \mathrm { C C D } )$ . Very high readout rates $\leq 1$ Mpixels per  
second) are sought for certain applications, such as image or wavefront reading in times less than the coherence time of atmospheric turbulence (e.g., in adaptive optics). The objective is a noise $\sigma _ { \mathrm { R } } ~ \approx ~ 2$ electrons rms for a readout rate of the order of 1 Mpixel per second. Another solution to the problem of increasing the readout rate, without increasing the readout noise, consists in having parallel exits, by dividing the CCD into 2, 4, or 8, with a separate exit for each part.

For a fixed number of generated photocharges, let us evaluate the number of charges read. Just as it was possible to characterise the thermal noise output by a resistance $R$ at temperature $T$ (see Sect. 7.2.2), in terms of a power $4 k T R \Delta f$ , it can be shown that, across a capacitance $C$ , the charge $q$ has variance

$$
\sigma _ { q } ^ { 2 } = k T C \Delta f .
$$

This is therefore the fundamental limit of the noise across $C$ . Assuming a capacitance of 50 femtoF, below which it is difficult to go, this gives $\sigma _ { q } = 4 6 \mathrm { e } ^ { - }$ at $7 7 ~ \mathrm { K }$ , and $1 0 \mathrm { e } ^ { - }$ at $4 \mathrm { K }$ . It is thus useful Dto reduce this capacitance, but that in turn would reduce the maximum amount of charge that couldbe stored, whence a lower flux would saturate the CCD.

Concerning the maximum charge that can be stored by this capacitor under a voltage $V$ , namely $C V$ , a value of $V = 1$ gives $6 . 2 5 \times 1 0 ^ { 6 } \mathrm { e } ^ { - }$ per pF. There is thus a simple relation for the dynamic D range of this capacitor, in the absence of any other source of noise which would reduce it:

$$
\mathrm { d y n a m i c ~ r a n g e } = V { \sqrt { \frac { C } { k T } } } .
$$

An important property of CCDs is their linearity up to a high charge storage capacity, around $1 0 ^ { 6 }$ charges per pixel in the best cases. This makes possible very long exposures of faint objects, with no increase in readout noise (Problem 7.11).

Table 7.6 CCD detectors. The table gives mean values, open to improvement in the future-  

<table><tr><td>Threshold</td><td>One quantum</td></tr><tr><td>Dynamic range</td><td>≤ 10 charges pixel-1</td></tr><tr><td>Quantum efficiency</td><td>η ≥ 0.8 between 500 and 900 nm</td></tr><tr><td>Spectral response</td><td>Normal CCD: 400-1100 nm Thinned CCD: soft X ray (0.1-50 keV)</td></tr><tr><td>Temporal response</td><td>Around 50 ms</td></tr><tr><td>Format</td><td>Up to 2 048 × 4096 pixels</td></tr><tr><td>Noise</td><td>Readout Or ~ 2-5 erms depending on rate</td></tr><tr><td>Information storage</td><td>Digital, destructive readout</td></tr></table>

Very long exposures nevertheless increase the chances of superposing a further type of noise in addition to readout noise, for example, due to the impact of cosmic rays, which is random and may saturate a pixel. Such events can occur both in space and at ground level, particularly during solar flares, or during a crossing of the South Atlantic anomaly (see Sect. 2.9.2). They then contribute to background noise. A specific treatment of the pixels can reduce this noise for spaceborne CCDs (see below).

# CCD Formats

At the time of writing (2007), the $2 0 4 8 \times 4 0 9 6$ format is a technological limit that would appear to be rather hard to improve upon, given the great difficulty involved in maintaining uniformity over surfaces including several tens of millions of pixels. In 2007, it is commonplace to make CCDs with format $1 0 2 4 \times 1 0 2 4$ (usually denoted by $1 \mathrm { k } \times 1 \mathrm { k } )$ ), but $4 \mathrm { k } \times 4 \mathrm { k }$  is possible. Beyond this, it is easy to place CCDs side  by side in order to construct large arrays. The present trend is therefore towards the tiling of focal planes by juxtaposition, which can give formats up to $8 \mathrm { k } \times 8 \mathrm { k }$ , or $8 1 9 2 \times 8 1 9 2$ . There is, of course, a dead space between the CCDs, which can be reduced to the area of a few dozen pixels. If one of the four sides of the CCD is reserved for electrical contacts, then juxtaposition can make a $4 \times 2$ array.

For example, the Megacam camera of the Canada–France–Hawaii telescope comprises 40 thinned CCDs, each with format $2 \mathrm { k } \times 4 . 5 \mathrm { k }$ , laid side by side to cover a total field of 1.4 degrees with $3 . 6 \times 1 0 ^ { 8 }$ pixels. The size of the CCDs is $1 3 . 5 \mu \mathrm { m }$ . Each exposure lasts at most $2 0 \mathrm { s }$ (to avoid risk of saturation) and provides 0.77 Gbits of data. A specific processing centre called Terapix (see Chap. 10) has been set up to process this considerable volume of information (Table 7.6).

# Dark Current

Thermal generation of charges in the CCD creates a signal, even when there is no illumination. This signal, mainly produced by traps at the $\mathrm { S i } { - } \mathrm { S i O } _ { 2 }$ interface, must therefore be calibrated on average and subtracted from the signal, an exercise referred to as doing a dark frame subtraction. The dark current decreases with temperature. It can be significantly reduced by means of a charge sloshing or dithering mode, which modulates readout voltages faster than the lifetime of surface states.

# The Low Light Level CCD (L3-CCD)

As the name suggests, the low light level CCD or L3-CCD is one that operates at low light levels. Here the readout noise becomes negligible, up to high readout rates $( \sim \mathrm { ~ 1 ~ k H z } )$ ). This is achieved by virtue of a multiplicative avalanche effect in the transfer register which transforms the incident photoelectron into a charge packet. A gain of around 500 is possible, making this L3-CCD a promising detector, operating in photon counting mode. It looks like becoming a serious competitor for the avalanche photodiode.

# CCDs for X-Ray Detection

By thinning, the sensitivity of the CCD can be extended as far as X rays. The European mission XMM–Newton (1999–2010) is equipped with two cameras, each using 7 CCDs with format $6 0 0 \times 6 0 0$ . A third camera uses $1 2 \mathrm { C C D s }$ , laid side by side, each containing $6 4 \times 1 8 9$ pixels. The CCDs are used either in full-frame mode or in frame transfer mode, so as to minimise the readout noise and maximise the useful exposure time.6 Analogous setups are in preparation for the future German mission ROSITA (around 2010), with quantum efficiencies exceeding 0.8 for X rays in the range $0 . 2 { - } 2 0 \mathrm { k e V } .$

The pn-CCD differs from conventional CCDs by the structure of its transfer registers, here formed by p–n junctions in the silicon. This ensures low sensitivity to undesirable hard radiation like $\gamma$ rays or cosmic rays, but also fast charge transfer and high charge storage capacity.7

Finally, the CCDs used in the X-ray region have a certain spectral selectivity, i.e., an intrinsic energy resolution, of $\Delta E \sim 1 0 0 \mathrm { e V }$ for $E < 1 \mathrm { k e V } ,$ and $\Delta E \sim 1 4 0 \mathrm { e V }$ for $E \sim 6 \ \mathrm { k e V } .$  Indeed, a photon with energy in the $\mathbf { k e V }$  range releases a large number of photocharges, a number which then becomes a measure of the incident photon energy. To measure the energy of each photon, it is thus essential to read the CCD before another photon causes a release of photocharges at the same place. A summary of the CCD performances is given in Table 7.6.

# The CCD Controller

This electronic device is an essential element in the use of CCDs. It generates the clock signals and controls the charges and their transfer:

• It modifies the readout frequency (also called the pixel frequency), depending on whether the readout noise must be minimised (slow frequency) or not.   
• It modifies the gain, that is the number of electrons per level of digitisation, depending on the strength of the signal and the required dynamic range.   
It can read the CCDs in binning mode, in which adjacent pixels are summed according to a predefined geometry $2 \times 2$ , $4 \times 4$ , etc.). In this case, spatial  resolution is lost, but the signal-to-noise ratio is improved, since the signal is increased for the same level of readout noise. This mode, which reduces the volume of data collected and the readout time, is useful for making adjustments in order to take into account variable image quality in photometry, if a high spatial resolution is not required, and so on.   
• It also provides a windowing mode, in which a subset of pixels is selected within a window of the array.

As an example of the way CCD pixels are manipulated, let us consider a device proposed for the detection of an exoplanet which measures the tiny differential polarisation over time of the radiation recieved from the star–planet system when the planet orbits around the star. Indeed, the stellar radiation scattered by the atmosphere of the exoplanet is polarised, and depends on the phase angle. The polarisation of the incident signal is analysed very rapidly $( 1 \mathrm { k H z } )$ , then transformed into an intensity variation. The image is formed on a CCD in which every other column is masked. The masked columns are used to store the photocharges generated in the first column and transferred to the second at the fast rate of the modulation. After many cycles, the difference between the two columns indicates the presence of a possible polarisation. This is the so-called ZIMPOL technique, proposed by Schmid, H.M. et al., and described at the website saturn.ethz.ch/instrument/zimpol.

# 7.4.7 The Hybrid CMOS Detector

CMOS stands for complementary metal oxide semiconductor and refers to a whole family of 2D detectors, also fabricated by conventional techniques of microelectronics, but based on a different idea to the CCD. In this case, each pixel comes with its own readout and amplification transistors (3 or 4 in all). These transistors take up some space on the sensitive surface and this reduces the filling factor of the array, whence it may be necessary to use microlens arrays to improve photon gathering in the image. Furthermore, the CMOS technology is not amenable to rear illumination, which would avoid absorption of a fraction of the radiation by the surface layers. Instead of transferring the charges to registers as in a CCD, a clock device addresses the pixels of the array one by one to read the signal.

![](images/c488312a080ccb8763ce9db76ba2c96d87cc26db69849eb41324145afe256f94.jpg)  
Fig. 7.31 Growing formats of imaging detectors in the near and mid-infrared using CMOS technology. Ordinate: Number of pixels on the detector. The straight line shows a doubling every 18 months (known as Moore’s law). Figure established in 2004, courtesy of Hodapp K.W., Hall D.N., University of Hawaii

This technique was first developed for the near infrared, in order to make imaging detectors beyond the photoconductivity of silicon. It was subsequently extended to the mid- and far infrared in the middle of the 1990s. Based on the photovoltaic effect, these detectors couple a photodiode, made from a material that is photosensitive at the desired wavelength, with a readout circuit made from silicon, the whole thing being in a large format array. They are sometimes called hybrid arrays since they employ two different materials hybridised together. Since the 1980s, these arrays led to the rapid development of astronomical imaging in the infrared region (Fig. 7.31).

It is interesting to situate these advances with respect to the history of astronomical exploration in the infrared region, which developed slowly at first, then leapt forward, largely due to the quality of the available detectors, as can be seen from Fig. 7.32, for the period up to 2000.

The very low energies involved (a fraction of an electron-volt) make it necessary to cool the devices, in order to avoid the thermal generation of charges (dark current). The temperature ranges from $7 7 \mathrm { K }$ (liquid nitrogen), at the lower wavelengths $( \leq 2 . 5 ~ \mu \mathrm { m } )$ , and from 4 to $2 0 ~ \mathrm { K }$ , at the longer wavelengths, where the band gap is narrower (Fig. 7.33). The use of consumable cryogenic liquids, such as ${ \bf N } _ { 2 }$ and He, is gradually giving way, on Earth and in space alike, to closed circuit cryogenic systems (Joule–Thomson refrigerators).

![](images/736e715819a58fdc2bda22a663daa1a71f8761e3a0356ab03f589a4e4b7543cd.jpg)  
Fig. 7.32 Progress in infrared detection. The Edison tasimeter (Eddy A., J. Hist. Astr. 3, 187, 1972) was remarkably sensitive for its day $( \mathrm { N E P } \approx 1 0 ^ { - 8 } \mathrm { W } \mathrm { H z } ^ { - 1 / 2 } )$ . The thin continuous curve represents a mean sensitivity obtained with single pixel detectors. The dashed curve shows the arrival of array detectors (CID and CCD), and the formats are given. The readout noise $\sigma _ { R }$ is given by the thick continuous curve, with a brief indication of trends in performance levels beyond 2000 for different wavelength regions: $\bullet = 1 - 2 . 5 \mu \mathrm { m }$ , $\circ = 2 . 5 { - } 5 { \mu \mathrm { m } }$ , $\vartriangle { \ d t } = 5 \ – 2 0 \ \mu \ m$

![](images/f0e6c11c19a22f88f33d23b0c0aa5d447b3ebc53759902df9ebd1285701795cf.jpg)  
Fig. 7.33 Operating temperature of CMOS arrays at different wavelengths. Different regions are covered by silicon Si, then InGaAs, $\mathrm { H g C d T e }$ , InSb, and S:As. Courtesy of Hodapp K.W., Hall D.N., University of Hawaii

# Visible Region

CMOS technology competes with CCDs in this region, coupling a silicon diode with the pixel transistors, also fabricated in the same silicon substrate (see Table 7.7).

Table 7.7 Comparing CCDs and CMOS devices. From Hodapp K.W., Hall D.N.B, Institute of Astronomy, Hawaii, 2005   

<table><tr><td>Property</td><td>CCD</td><td>Hybrid CMOS</td></tr><tr><td>Resolution</td><td>&gt; 4k×4k</td><td>4k × 4k (under development)</td></tr><tr><td>Pixel (μm)</td><td>10-20</td><td>18-40 (&lt;10 under development)</td></tr><tr><td>Domaine spectral</td><td>400-1000 nm</td><td>400-1000 (Si PIN)</td></tr><tr><td>Noise</td><td>Several e-rms</td><td>Same with multiple sampling</td></tr><tr><td>Shutter</td><td>Manual</td><td>Electronic</td></tr><tr><td>Consumption</td><td>High</td><td>10 times lower</td></tr><tr><td>Sensitivity to radiation</td><td>Sensitive</td><td>Barely sensitive</td></tr><tr><td>Control electronics</td><td>High voltage clock</td><td>Low voltage</td></tr><tr><td>Special modes</td><td>Binning</td><td>Windowing</td></tr><tr><td></td><td>Adaptive optics</td><td>Random access</td></tr><tr><td></td><td></td><td>High dynamic range</td></tr></table>

The popular invention known as the webcam is equipped with detectors using this technology.

# Near and Mid-Infrared

The hybrid $\mathrm { H g C d T e }$ arrays originally commercialised under the trade name NIC-MOS, which stands for Near Infrared Camera and Multi-Object Spectrometer, were designed for the Hubble Space Telescope with a $1 0 2 4 \times 1 0 2 4$ format in the 1990s (Fig. 7.33). They are now called Hawaii detectors and have become more or less universal for the spectral bands J, H, and K, to be found on all the major groundbased and spaceborne telescopes (see Figs. 7.34 and 7.35).

The format and readout noise of these detectors have seen constant improvement and they now have excellent noise performance in the region $1 { - } 2 . 5 \mu \mathrm { m }$ , viz., $\sigma _ { \mathrm { R } } \approx 1 0 \mathrm { e } ^ { - }$ . At the time of writing (2006), formats of $6 1 4 4 \times 6 1 4 4$ have been achieved with $1 0 \mu \mathrm { m }$ pixels. They contain 248 million field effect transistors (FET). Thermal charge generation (dark current) is low, which means that, in the absence of background radiation, exposures of several tens of minutes are feasible. It can also be read quickly, in several tens of milliseconds, an invaluable asset in adaptive optics or optical interferometry, where rates are linked to the evolution times of atmospheric turbulence. The storage capacity of the potential wells is not very high (around $1 0 ^ { 5 }$ photocharges), and this limits use to long exposures with high incident fluxes or in the presence of a significant background signal (spectral bands J and H).

Hybrid InSb (indium antimonide) arrays, commercialised under the trade name Aladdin, pick up from there, up to the photoconductivity limit of thise material, in formats reaching $5 1 2 \times 4 0 9 6$ on one of the CRIRES focal instruments of the European Very Large Telescope.

Hybrid Si:As arrays, in a $2 5 6 \times 2 5 6$ format, then bridge the gap to the groundbased observation window of the $_ \mathrm { N }$ band around $\lambda = 1 0 \mu \mathrm { m }$ (the VISIR instrument Dof the VLT). They work in BIB mode described below. The IRAC camera of the Spitzer space mission launched in 2003 is also equipped with this detector, operating at $5 . 8 \mathrm { - } 8 \mu \mathrm { m }$ . The imaging photometer (MIP) of this mission comprises a $1 2 8 \times 1 2 8$ Si:As array, observing around $\lambda = 2 4 \mu \mathrm { m }$ . It also works on the blocked impurity Dband (BIB) principle discussed below.

![](images/5b769b3b15f64cdcf3a08d6664401dbe93cf3026aacc6162c02f62d316d70be5.jpg)  
Fig. 7.34 The Orion nebula observed in 2001 with the European Very Large Telescope and the ISAAC instrument. This image is put together using images taken in three different spectral bands (J, H, and K) and is in fact a $3 \times 3$ array of individual images, with the $1 0 2 4 \times 1 0 2 4$ format of the $\mathrm { H g C d T e }$ detector. Field $7 ^ { \prime } \times 7 ^ { \prime }$ , pixel $0 . 1 5 ^ { \prime \prime }$ . North is at the top and east on the left. Source ESO and M. McCaughrean

The same hybridisation scheme can be used with Si:Sb, for which photoconductivity extends up to $4 0 ~ { \mu \mathrm { m } }$ , in $2 5 6 \times 2 5 6$ formats, for use in space. The IRS spectrometer of this same mission is equipped with a $1 2 8 \times 1 2 8$ format camera.

# Blocked Impurity Band (BIB) Detectors

Two opposing requirements must be balanced when an extrinsic photoconductor is used in a detector: the level of dopant should be low in order to ensure a high resistivity, but it should be sufficient to maintain an adequate quantum efficiency when absorbing photons. The principle of the blocked impurity band (BIB) is to separate these two requirements spatially, in the material of the photoconductor, so that each can be optimised. An added benefit is an amplification effect, which improves noise performance.

![](images/de65d792f704b7aa998871d56ae94e3831f741a796fcbb315868f4f4d1c5dcce.jpg)  
Fig. 7.35 An image obtained with a NICMOS detector, on the $1 \textrm { m }$ telescope at the European Southern Observatory (La Silla, Chile). Field $1 2 ^ { \prime } \times 1 2 ^ { \prime }$ in the central region of Orion, showing molecular cloud and star formation region. The same region has been shown at radiofrequencies in Fig. 5.5. Wavelength and spectral band J $( 1 . 2 \mu \mathrm { m } )$ . Image format $7 8 0 \times 7 8 0$ , although the solidstate device includes only $2 5 6 \times 2 5 6$ pixels, the telescope being displaced by offsets of one third of a pixel and the image reconstructed by interpolation. Total exposure time $9 \times 1$ s. (Photo by Copet E., DENIS programme, 1995)

Consider the material Si:As, silicon doped with arsenic, with a band gap which situates the photoelectric effect in the region $\lambda \le 2 3 ~ \mu \mathrm { m }$ . The photosensitive layer (Fig. 7.36) is highly $n$ - doped, implying a good quantum efficiency, and also a small volume, which makes the detector less sensitive in an environment of high energy particles (e.g., in space, see Sect. 2.9.2). This layer is preceded by a thin blocking layer, made of a pure material, which ensures a high resistivity between the two electrodes. A photoelectron released in the sensitive layer drifts in the electric field, towards the blocking layer. A strong field can then transmit enough energy for the photoelectron to produce secondary electrons, by ionising collisions. This does not happen in the blocking layer, for the material there is too pure, and the ionisation energy is therefore high (around 1 eV). Amplification can reach a factor of ten. This is presented in detail by Rieke G.H., Detection of Light: from the Ultraviolet to the Submillimetric, 2nd edn., Cambridge 2003, and the discussion here follows closely.

![](images/9698803d631444e49fa7b5084ed2e2a7e2f88ae0c6f84e07aa1fe4cc93293ad1.jpg)  
Fig. 7.36 Schematic cross-section of a BIB detector. The electron is released in the photosensitive layer and drifts towards the blocking layer. The electrodes are on either side. Here, the BIB is illuminated from the front. (After Rieke G.H., 1994)

The amplification technique in the BIB detector is pushed a step further in the solidstate photomultiplier or SSPM. One difficulty with the BIB is that the amplification zone, situated at the interface of the blocking and photosensitive layers, is not very clearly defined. If this role is assigned specifically to a third layer, a significant cascade effect is obtained, in which a single electron may generate a current peak of 40 000 charges. Further, this current pulse is very brief, lasting only a few nanoseconds, if followed by high speed electronics. The detector then operates as a photon counter, and is able to discriminate events which are highly fluctuating in time. This constitutes, in the infrared domain, a property already mentioned for silicon avalanche diodes.

# Detection in the Far Infrared

The only photoconductor that can be used beyond $4 0 \mu \mathrm { m }$ is the material Ge:Ga, with a sensitivity region extendable to $2 1 0 \mu \mathrm { m }$ by applying pressure (stressed detector). However, the stressing device requires space and microelectronic techniques are no longer applicable, whence hybridisation is carried out pixel by pixel. This in turn reduces the available format sizes. These detectors equip the imaging photometer of the Spitzer mission (format $2 \times 2 0$ ), the PACS instrument of the European space mission Herschel (format $5 \times 5$ ), and the FIFI instrument of the airborne telescope SOFIA (format $2 5 \times 1 6$ ).

# Quasi-Optical Coupling

At wavelengths lying between the far infrared and millimetre, diffraction phenomena become significant, for the size of the detectors becomes comparable with the order of magnitude of the wavelength. In order to better concentrate the energy on the detector, guides are used in quasi-optical mode, which means that they operate somewhere between the classical image formation by a lens (see Chap. 5) and the standard waveguide (see Sect. 6.4). This is illustrated in Fig. 7.37, for detection in the range 100 to $2 4 0 \mu \mathrm { m }$ .

![](images/1d51f40c2b4ffbca99c83e4c3480e8c54ce052dcc04c5eb8c895c6110ed3d64b.jpg)  
Fig. 7.37 Quasi-optical arrangement of a detector array $( 5 \times 5 )$ , in gallium-doped germanium, operating at $\lambda < 2 4 0 \mu \mathrm { m }$ . (After Geis N., doctoral thesis, Max Planck Institut f¨ur Extraterrestrische Physik, 1991)

# 7.4.8 Observing Conditions in the Infrared

The radiation received at the detector includes the signal from the source and also the signal from the thermal background. The latter may be due to the optics of the telescope itself, if it is not cooled, or to the thermal background of the atmosphere. These two components can be reduced or even totally eliminated, when the detector is placed in space and equipped with cooled optics. Except in the latter case, the readout noise of the detector does not need to be reduced below the thermal noise generated by the background signal.

Two spectral regions thus stand out clearly, particularly for ground-based observations: wavelengths less than about $1 . 8 ~  { \mu \mathrm { m } }$ , where the background signal is negligible and the reduction of readout noise can be pushed to its limit. Beyond this point, the fluorescence of atmospheric OH radical enters the picture, as discussed in

Sect. 2.3, followed by a significant rise in the thermal background radiation. This region does not therefore require extreme performance with regard to the readout noise $\sigma _ { \mathrm { R } }$ .

In space, the absence of thermal background, and the very limited background due to a fully cooled telescope and optics, require the readout noise to be as low as possible.

An Instrument from the 1990s: The ISO Satellite. It is interesting to consider the progress achieved by describing the performance of the long wavelength observations $( 5 { - } 1 7 . 8 ~ \mu \mathrm { m } )$ of the ISO satellite, which was designed in the mid-1980s, launched in 1995, and exhausted its cryogenic fluid in 1998 (a joint project backed by the USA, GB, and ND). This camera (ISOCAM) was equipped with a $3 2 \times 3 2$ array made with Si:Ga hybridised on Si, and had a readout device that prefigured the CMOS system. (This was called direct voltage readout or DVR, which no longer transferred the charges, but read the amplified voltages on each pixel in sequence.) The readout noise $\sigma _ { \mathrm R }$ was approximately $1 8 0 \mathrm { e } ^ { - }$ rms, lower than the background noise, the integration time was at most $1 0 0 \mathrm { m s }$ before saturation by the residual thermal background, and the pixels had a storage capacity of $1 0 ^ { 6 }$ charges. This camera, which provided the first quality images in the near infrared with the $3 2 \times 3 2$ format (with two arrays, HgCdTe and Si:Ga), produced an extraordinary crop of new results.

The important development of the ISO satellite camera in France between 1985 and 1993 had many spinoffs. It is interesting to see how a single idea can be adapted to different contexts. At ground level, the thermal background is very much higher than that which prevails in space, for a cooled telescope. A solid-state device, based on the same principles, but with a storage capacity of $1 0 ^ { 7 }$ charges per pixel, was devised to equip the camera of a ground-based telescope (the TIMMI camera of the $3 . 5 \mathrm { ~ m ~ N T T }$ at the European Southern Observatory). It originally had a format of $1 2 8 \times 1 2 8$ but, after extension to a format of $2 5 6 \times 2 5 6$ and a change of dopant from Ga to As,  it equipped the Very Large Telescope (VLT), operating in the atmospheric transmission window between 8 and $1 2 \mu \mathrm { m }$ . It is interesting to compare the performance of the same detector at ground level (high background signal) and in space, with totally cooled optics (low background signal).

Even earlier, before the advent of detector arrays, NASA’s Infrared Astronomical Satellite (IRAS), which was the first to map the infrared sky, throughout the year 1983, carried individual detectors arranged side by side (Fig. 7.38).

# 7.4.9 Development of Solid-State Imaging Arrays

As in the case of many other astronomical detectors, many parameters are required to completely characterise these detectors. Three examples are listed here:

• The Maximum Storage Capacity of Photocharges per Pixel. This is an important quantity when faint sources are sought in the vicinity of some bright object. Saturation by the bright object determines the dynamic range of the detector. Furthermore, as already mentioned, the wells can be very quickly saturated, in a few milliseconds, by any thermal background radiation, so that it is pointless trying to extract the signal, after subtraction of this background. The solution is therefore to increase the capacity, which may reach a few times $1 0 ^ { 6 }$ or $1 0 ^ { 7 }$ photocharges per pixel. The Dependence of 
R on the Readout Rate. The faster the readout, the larger $\sigma _ { \mathrm { R } }$ becomes, and this may be harmful in rapid readout applications, such as optical interferometry, adaptive optics, and speckle interferometry, in which wavefront and image vary on the time-scale of atmospheric turbulence. The same is true for rapidly varying sources, such as pulsars and bursts.

![](images/ae9589b001327a5b755bd14d0ced968b53fc6b1c88a272db38abdf1e4a644a30.jpg)  
Fig. 7.38 A historic mission: the focal plane of the IRAS satellite $6 0 \mathrm { c m }$ telescope (1983). The individual detectors are arranged to obtain the maximum accuracy in locating a source as it crosses the focal plane. The visible sensors locate the field by detecting stars known in the visible, as they pass across. From Neugebauer G. et al., Ap. J. 278, L1, 1984. With the kind permission of the Astrophysical Journal

• The Format. The trend is towards larger formats. Although technology is unlikely to provide formats greater than $4 0 9 6 \times 4 0 9 6$ per unit of a detector array at affordable prices,8 the technique of juxtaposing solid-state imagers to form arrays can increase the useful format, and thus give a better use of the field at the telescope focus.

# Noise Equivalent Power

A photoconductor, operating at a temperature $T$ , has a non-zero resistance, even in the absence of illumination, because of the thermal release of charge carriers. The thermodynamic fluctuations in this resistance at temperature $T$ , called Johnson noise, are generally negligible compared with other noise sources.

Each incident photon produces $\eta$ electron–hole pairs, rather than $\eta$ electrons, as happens in the vacuum photoelectric effect, and so the quantum noise, due to the signal or the thermal background, has twice the variance.

The dominant source of noise from the detector itself is usually due to the transistor in the first stage of amplification. Denoting the detector response by $R \ [ \mathrm { V } \mathrm { W } ^ { - 1 } ]$ , and the noise of this transistor by $\sigma _ { \mathrm { R } } ~ [ \mathrm { V } \mathrm { H z } ^ { - 1 / 2 } ]$ , the noise equivalent power of the transistor, often used to characterise the detector (see Sect. 7.2.1), is given by

$$
{ \mathrm { N E P } } = \sigma _ { \mathrm { R } } / R \qquad { \mathrm { [ W H z ^ { - 1 / 2 } ] } } ~ .
$$

Typical values are $1 0 ^ { - 1 6 } – 1 0 ^ { - 1 7 } \mathrm { ~ W H z } ^ { - 1 / 2 }$ . Table 7.8 summarises some common properties of solid-state devices used in the near and mid-infrared.

# 7.4.10 Bolometers

In this type of detector, the energy of the incident photon is no longer used to excite the quantum jump of an electron into the conduction band. Instead, it is directly converted into thermal agitation, either of the crystal lattice, or of the free electron gas, if this is indeed decoupled from the lattice (the hot electron bolometer). These detectors therefore measure the temperature variation in either the crystal lattice or the electron gas, by a change in electrical resistance. They played a very important role in the development of infrared astronomy over the period 1960–1990, and then, considerably improved, continued to do so in the 2000s in the submillimetre region, where the fact that they have no intrinsic spectral selectivity gives them a significant advantage over heterodyne detection. With the use of microelectronic and multiplexing techniques, large format arrays can be made for both ground-based and spaceborne telescopes.

# Standard Germanium Bolometer

The germanium bolometer doped with gallium (Ga) is shown schematically in Fig. 7.39. The idea is to measure a slight change in resistance due to a rise in temperature of the material. Developed in the 1960s by F. Low,9 it covered the near and mid-infrared (infrared photometry or spectrophotometry) and led to many discoveries. A semiconductor crystal is used here, cooled to $2 { \mathrm { - } } 4 \mathrm { K }$ by liquid helium.

Table 7.8 Infrared solid-state devices   

<table><tr><td>Spectral range</td><td>Depends on material and dopant</td></tr><tr><td>Threshold</td><td>One quantum</td></tr><tr><td>Dynamic range</td><td>104-107 photocharges</td></tr><tr><td>Quantum efficiency</td><td>Generally &gt; 0.5</td></tr><tr><td>Temporal response</td><td>≤1ms</td></tr><tr><td>Integration time</td><td>About1O min if limited by thermal generation</td></tr><tr><td>Readout noise</td><td>About 1O ms if limited by thermal background</td></tr><tr><td>Storage</td><td>10-500 e- depending on device</td></tr><tr><td>Format</td><td>1024×1024→ 4096× 4096 (4k× 4k)</td></tr><tr><td>Operating temperature</td><td>77K(≤2.5 μm)→4K(longλ)</td></tr><tr><td>Special features</td><td>Addressable pixels</td></tr></table>

![](images/c38d7eaf5b858dbbc2dbe8b397849509aa37b1175f5e6aca597722771f8374c7.jpg)  
Fig. 7.39 The germanium bolometer (Ge:Ga). The resistivity of the semiconductor crystal varies rapidly with temperature $( \rho ~ \propto ~ T ^ { - 2 } )$ . A blackened shield efficiently $( \sim 1 0 0 \% )$ absorbs the / incident photons. The cross-section is improved by surrounding the crystal by a reflecting sphere. The crystal (of heat capacity $C$ ) is linked to the thermostat by wires (of heat conductance G). The time constant is $\tau \sim C / G$ . A bias $V _ { 0 }$ is applied across the resistor $R _ { \mathrm { { C } } }$ . The variation of the resistance $\Delta R _ { \mathrm { B } }$ of the bolometer, caused by the heating, is transformed into a signal $\Delta V = \Delta R _ { \mathrm { B } } / R _ { \mathrm { C } } + R _ { \mathrm { B } }$ . The solid angle within which radiation is received is controlled by a D Clow temperature screen

The bolometer can be considered to comprise two thermally coupled parts which are to be optimised separately. One is a radiation absorber, and the other a resistance serving as thermometer. The noise in this type of bolometer is thermal, and corresponds to its operating temperature $T$ (Johnson noise of the resistance and phonon noise leading to thermal energy). Noise equivalent powers from NEP $\sim$ $\mathrm { \overline { { 1 0 ^ { - 1 5 } } } ~ W } \mathrm { H z } ^ { - 1 / 2 }$ at $T = 2 \mathrm { ~ K ~ }$ to $1 0 ^ { - 1 6 }$ W $\mathrm { H z } ^ { - 1 / 2 }$ at $T = 0 . 3 \mathrm { ~ K ~ }$ are achieved with this type of device.

This conventional bolometer has witnessed considerable improvements.10 An example is the array equipping the European space mission Herschel (launch 2008) to cover the spectral region $6 0 { - } 2 1 0 ~ { \mu \mathrm { m } }$ . This array contains 2 560 silicon bolometers, arranged into $1 6 \times 1 6$ subsystems and operating at a temperature of $0 . 3 \ \mathrm { K }$ , obtained by a $^ 3 \mathrm { H e }$ dilution refrigerator. The NEP reaches $1 0 ^ { - 1 6 }$ W $\mathrm { H } z ^ { - 1 / 2 }$ , comparable with the noise induced by the thermal background in the observed beam etendue, whence there is no point in attempting further improvements. The signals, ´ produced by individual amplifiers, are multiplexed in order to reduce the number of connecting wires.

# Superconducting Bolometer

Here a superconducting material such as an Nb–Si alloy is held very close to the critical temperature at which the resistivity depends sensitively on the temperature. If energy in input by absorption of incident radiation, the resistance is altered. The resulting change in the current induces a magnetic field which is measured by a superconducting quantum interference device (SQUID). The operating temperature is close to $0 . 1 \mathrm { ~ K ~ }$ , obtained using a $^ 3 \mathrm { H e }$ refrigerator. These cooling systems can operate in closed circuit, and provide an elegant solution when long lifetimes are required for space missions, without depending on a cryogenic fluid which would eventually be used up. The NEP can be of the order of $1 0 ^ { - 1 7 } \mathrm { ~ W } \mathrm { H z } ^ { - 1 / 2 }$ , and improves as the temperature is lowered.

One difficulty lies in coupling the bolometer surface with the incident radiation. Indeed, it must be similar in size to the wavelength, while having a heat capacity, which determines the time constant of the bolometer, as low as possible. Finally, it is desirable to construct $N \times N$ bolometer arrays to obtain images efficiently.

The $1 0 . 4 \mathrm { ~ m ~ }$ telescope of the Caltech Submillimeter Observatory $( \mathrm { C S O } ) ^ { 1 1 }$ in Hawaii is equipped with a linear array of 24 thermal (Si) bolometers operating at a temperature of $0 . 3 \mathrm { K }$ obtained by a $^ 3 \mathrm { H e }$ dilution refrigerator. Atmospheric windows at 0.35, 0.45, and $0 . 8 7 \mathrm { m m }$ are accessible in broad band photometry $( \Delta \lambda / \lambda \sim 0 . 1 )$ . The CSO is also equipped with a hexagonal bolometer array $( 1 1 \times 1 1 )$ ) operating at 1.2 and $2 . 1 \mathrm { m m }$ (BOLOCAM).

The European space mission Planck, launched in 2008, is designed to study the cosmological blackbody radiation and its spatial structure. It seeks maximal sensitivity and imaging capacity at submillimetre wavelengths, using a $1 . 5 \mathrm { ~ m ~ }$ telescope cooled to $6 0 ~ \mathrm { ~ K ~ }$ . The High Frequency Instrument12 (HIFI) uses $4 \times 4$ and $8 \times 8$ bolometer arrays cooled to $0 . 1 \mathrm { ~ K ~ }$ to cover the range  100–857 GHz in six bands at low spectral resolution $( \sim 0 . 3 )$ . Cooling is carried out in several stages: hydrogen desorption, then Joule–Thomson expansion to reach $4 \mathrm { K }$ , then $^ 3 \mathrm { H e }$ dilution. The NEP can reach around $\mathrm { \dot { 1 } 0 ^ { - 1 7 } \ W H z ^ { - 1 / 2 } }$ .

In less than three decades, the spectacular progress made in bolometer design has made them invaluable submillimetre detectors, both on the ground and in space (see Fig. 7.40).

# Hot Electron Bolometer

In a very pure material like InSb $\sim 3 \times 1 0 ^ { 1 3 }$ carriers $/ \mathrm { c m } ^ { 3 }$ ) at low temperatures $( \sim 4 \ : \mathrm { K } )$  , a fraction of the conduction electrons remain free and interact weakly with the crystal lattice. Photon absorption by electrons raises their temperature and quickly modifies the resistivity of the material. This is photoconductivity by free carriers, exploited in the hot electron bolometer (HEB).13 However, the resistivity is proportional to the incident energy, hence also to the square of the electric field, whence the system functions as a mixer, and is frequently used as such in the radiofrequency range (see Sect. 7.5).

![](images/6c0cf9cdd4acc828a3ff6a854db19f2752463379f14f7210bda7819765a8ce61.jpg)  
Fig. 7.40 A particularly difficult measurement using a bolometer: the continuum emission of the $2 . 7 ~ \mathrm { K }$ cosmological background near its maximum. The $2 . 7 ~ \mathrm { K }$ and $2 . 9 \mathrm { ~ K ~ }$ Planck functions have been plotted with the following measurements: (a) using a $0 . 3 \mathrm { ~ K ~ }$ bolometer $\mathrm { ( N E P \sim }$ $1 0 ^ { - 1 5 } \mathrm { W } \mathrm { H z } ^ { - 1 / 2 }$ ), Woody and Richards measured the spectrum from a balloon at altitude $4 0 ~ \mathrm { k m }$ ; (b) the result of a similar measurement, made by Gush from a rocket between 150 and $3 7 0 ~ \mathrm { k m }$ altitudes. The shaded areas correspond to the error bars given by the authors. (After Weiss R., ARAA 18, 489, 1980. Reproduced with the kind permission of the Annual Review of Astronomy and Astrophysics, $\circledcirc$ 1980, Annual Review Inc.) These historical results have been considerably -improved by the COBE satellite, since 1990, then by the BOOMERANG and WMAP missions at the beginning of the 2000s

# X-Ray Bolometer

At the high energies characteristic of X rays $\mathrm { ( > 0 . 1 ~ k e V }$ ), the energy delivered is enough to produce a temperature pulse in the bolometer, indicating the arrival of individual photons. The amplitude of the pulse can be used to determine the energy. This is therefore a detector with an intrinsic spectral selectivity, invaluable for spectroscopic applications. Since the energy threshold and spectral resolution are proportional to the volume of the detector, small detectors are favoured. This is also advantageous in imaging, which requires small pixels. On the other hand, detection efficiency depends on the thickness of the detector.

A diamond crystal of several $\mathrm { m m } ^ { 3 }$ , cooled to below $0 . 1 ~ \mathrm { K }$ , is thermally coupled to a germanium component, whose conductivity varies sensitively with temperature (Fig. 7.41). If X-ray photon arrivals are separated by time intervals greater than the time constant of the bolometer, which is of millisecond order, individual events can be discriminated. An energy resolution of a few $\mathrm { e V }$ can be achieved with these detectors in the laboratory at the time of writing (2007).

![](images/2975e0464dba1e713cf4e430380d6701c6a5efcae351ddedd58e6086d1839f3d.jpg)  
Fig. 7.41 (a) Schematic view of a doped germanium bolometer. At the centre, the germanium resistance, stuck on the absorbing diamond disk. (b) Display of the time constant of the bolometer, after absorbing the energy of a photon (or any other absorbed particle). (c) Spectrum for emission of $\alpha$ particles by a radioactive material, with $T _ { \mathrm { b o l } } = 1 . 3 \ : \mathrm { K }$ . Data kindly provided by Coron N., 1985

# 7.5 Astronomical Detectors: Radiofrequencies

The principle of radiofrequency detection using non-linear elements as mixers, with a frequency change, then detection, was first developed at metre wavelengths, and then extended gradually down to centimetre, millimetre, and finally submillimetre wavelengths, at which point it joined up with quantum and thermal detection techniques (photoconductors and bolometers, respectively, which were discussed earlier). Frequency-changing techniques are sometimes successfully applied in infrared spectroscopy, using photoconductors as mixers (see Sect. 8.4).

In this section, we begin by discussing concepts which apply across the whole radiofrequency region, before examining some practical realisations and the performance of detection systems they use.

# 7.5.1 General Features

Here we discuss how to convert the incident electric field into current, either directly or by frequency change, then describe the noise characteristics affecting the signal produced by the measurement, taking into account the thermal nature of the received radiation, both from the source and from the environment of the telescope.

# The Conversion of Field into Current

The wave, focused at the focal point of a telescope, enters a horn, which matches the vacuum impedance to that of a waveguide. The latter selects a polarisation. The wave is guided into a resonant cavity, which defines a passband $\Delta \nu$ , through its selectivity $Q = \nu / \Delta \nu$ , close to the frequency $\nu$ of the radiation (Fig. 7.42).

# Received Power. Antenna Temperature

Consider first the simple case of a thermal source of radiation, of emissivity $\varepsilon _ { \nu }$ and temperature $T$ . The power reaching the non-linear element is given by

$$
\frac { \mathrm { d } P _ { \nu } } { \mathrm { d } \nu } = \frac { 1 } { 2 } \varepsilon _ { \nu } B _ { \nu } ( T ) \eta _ { \nu } \mathcal { E } ,
$$

where $\mathcal { E } ^ { \mathcal { O } }$ is the beam etendue sampled, and the factor of´ $1 / 2$ comes from the selection of one polarisation. $\eta _ { \nu }$ denotes the total transmission, and $B _ { \nu } ( T )$ is the Planck function. It is assumed that the arrangement is as in Fig. 7.42a above.

It was shown, in Chap. 6, that the beam etendue ´ $\mathcal { E }$ is limited by the coherence of the radiation, and must be taken as equal to $\lambda ^ { 2 }$ . In other words, for a given telescope area $S$ , the field on the sky, which is imposed by coherence, is given by the solid angle $\omega = \lambda ^ { 2 } / S$ . Any radiofrequency receiver is intrinsically limited to analysis of Da single pixel, with field equal to $\omega$ . (In aperture synthesis, the receiver is limited to one ‘Fourier space pixel’, rather than one pixel in the image plane.)

The power per frequency interval is then

$$
\frac { \mathrm { d } P _ { \nu } } { \mathrm { d } \nu } = \frac { 1 } { 2 } \varepsilon _ { \nu } \eta _ { \nu } \lambda ^ { 2 } B _ { \nu } ( T ) \ ,
$$

![](images/b9a1ea6fecb9b251d40001b122c7e5d740d7992c3d3f9143c77411505f03aa51.jpg)  
Fig. 7.42 Three receiver configurations for radio waves. In the first arrangement (a), a coil, normal to the magnetic field vector for example, is excited by induction and transforms the field into a current, which is transported by coaxial cable. A variation on this arrangement consists in directly exciting the non-linear element by the electric field. In the second arrangement $\mathbf { ( b ) }$ , an amplifier is placed on the waveguide axis and amplifies the wave before it excites the coil, or is detected. In the third arrangement (c), a local oscillator, of frequency $\nu _ { 0 }$ , superposes its field on that of the incident signal, by means of a coupler. The summed field is then applied to the non-linear element. An amplifier can be incorporated into this arrangement

and, in the case of blackbody radiation $\mathbf { \xi } _ { \mathcal { E } _ { \nu } } = 1 \mathbf { \xi } _ { \mathcal { E } }$ ), in the Rayleigh–Jeans approximation,

$$
\frac { \mathrm { d } P _ { \nu } } { \mathrm { d } \nu } = \eta _ { \nu } k T ~ .
$$

The received power is then simply given by a temperature, known as the antenna temperature, which is independent of the transmission of the system.

If the source is:

1. optically thick at the wavelength considered,   
2. at a temperature justifying use of the Rayleigh–Jeans approximation for the frequency considered $( h \nu \ll k T$ ),   
3. sufficiently extended to fill the field of lobe $\omega$ of the instrument,   
4. in local thermodynamic equilibrium,

then the antenna temperature $T _ { \mathrm { A } }$ is also the physical temperature of the radiation from the source. In the case of a non-thermal source, or one with an arbitrary intensity function, the power received at the telescope is clearly given by

$$
\mathrm { d } P _ { \nu } = k T _ { \mathrm { A } } ( \nu ) \mathrm { d } \nu ~ ,
$$

where $T _ { \mathrm { A } }$ is the antenna temperature measured at the frequency $\nu$

# Noise Temperature

In practice, even when an instrument is pointed towards a region containing no sources of radiation, and at zero temperature, a non-zero current is measured, whose power is also non-zero. There are several causes of this residual signal:

• Residual thermal emission from the atmosphere (see Sect. 2.3.2), the telescope, and the waveguide.   
Contribution from the thermal emission of the ground, detected in the sidelobes of the diffraction pattern.   
• Thermal noise generated in the detector itself (for example, fluctuations in the tunnelling current, in the AsGa diode).

The fields of these different sources are incoherent, and therefore add quadratically, so that the equation for the total noise power as the sum of the powers gives

$$
T _ { \mathrm { n o i s e } } = T _ { \mathrm { a t m o s p h e r e } } + T _ { \mathrm { l o b e s } } + T _ { \mathrm { d e t e c t o r } } ,
$$

even if the ‘temperatures’ do not correspond to actual physical temperatures. They merely represent the power from which the signal must be distinguished. The first two terms are highly dependent on wavelength, for the same is true of atmospheric emission and diffraction. They are usually around $1 0 0 \mathrm { K }$ for Earth-based telescopes, and around $1 0 \mathrm { K }$ for space telescopes. In the best of cases, the limit will be imposed by $T _ { \mathrm { d e t e c t o r } }$ , also known as the system temperature, which cannot be less than the physical temperature of the detector, and indeed, it is generally much higher than this value.

Consider now each of the configurations in Fig. 7.42a, b, and c, and their total noise temperatures, excluding contributions from the antenna and atmospheric emission:

$$
\begin{array} { r l } & { T _ { \mathrm { n o i s e } } = T _ { \mathrm { q u a d r a t i c ~ d e t e c t o r } } \ . } \\ & { T _ { \mathrm { n o i s e } } = T _ { \mathrm { a m p l i f i e r } } + T _ { \mathrm { m i x e r } } / \mathrm { g a i n } \ . } \\ & { T _ { \mathrm { n o i s e } } = T _ { \mathrm { R F ~ a m p l i f i e r } } + T _ { \mathrm { m i x e r } } / \mathrm { R F ~ a m p l i f i e r ~ g a i n } } \\ & { + T _ { \mathrm { I F ~ a m p l i f i e r } } + T _ { \mathrm { I F ~ m i x e r } } / \mathrm { I F ~ a m p l i f i e r ~ g a i n } \ . } \end{array}
$$

Case (c) has been written in the most general case of heterodyne detection.

The critical factor in each case is the mixer, whose noise temperature varies from a few tens to a few thousands of degrees kelvin (Fig. 7.43). The key features will be discussed below.

Note that the best receivers approach the quantum limit (Problem 7.9). At frequencies below $1 0 0 \mathrm { G H z }$ (centimetre or metre), the RF signal must be amplified, and this use of an amplifier reduces $T _ { \mathrm { n o i s e } }$ to between $5 0 \ \mathrm { K }$ (6 to $2 1 \ \mathrm { c m }$ ) and

![](images/517b1e1f50bf43bf9b1c5183e4bc8561c532614a6829920140fde558c1936929.jpg)  
Fig. 7.43 Noise temperature of mixers used in radioastronomy. $( + )$ Schottky diodes at $3 0 0 \mathrm { K }$ , $( \times )$ cooled Schottky diodes, $( \diamond )$ C  SIS junctions, ( ) hot electron bolometer (HEB). All these detectors have an intrinsically wide passband $\mathrm { ( > 1 0 0 M H z }$ ), except the bolometer. The straight line indicates the limit $h \nu = k T _ { \mathrm { n } }$ . (After Philips T.G., Woody D.P., ARAA 20, 285, 1982. Reproduced with the Dkind permission of the Annual Review of Astronomy and Astrophysics, Vol. 20, $\textcircled{9} 1 9 8 0$ , Annual Reviews Inc.) The initial values given in the figure $T _ { \mathrm { n } } \geq 1 0 0 \mathrm { K } )$ - are those of the mid-1980s. By the mid-1990s, little progress had been made in the region below $5 0 0 \mathrm { G H z }$ , the greatest being a factor of 2 for SIS junctions. By the mid-2000s (black symbols), SIS junctions are still being improved, e.g., $T _ { \mathfrak { n } }$ in the range $5 0 – 1 5 0 \mathrm { K }$ for the detectors of the $3 0 \mathrm { m }$ IRAM telescope or those of the HIFI instrument on board the European mission Herschel (launch 2008) beyond 1 THz, whereas the hot electron bolometer takes this mission beyond 1 THz, viz., $\lambda = 3 3 0 \mu \mathrm { m }$ . (Values for 2007 with the courtesy of G. Beaudin)

$3 0 0 ~ \mathrm { K }$ $( 1 . 3 ~ \mathrm { c m } )$ . These values are typical of receivers for the aperture synthesis radiotelescope known as the Very Large Array (VLA) in New Mexico.

By pointing the receiver alternately at the source and at a neighbouring point of the sky, assumed empty of sources, two values of the antenna temperature can be measured:

$$
T _ { \mathrm { s y s t e m } } + T _ { \mathrm { s o u r c e } } \quad \mathrm { a n d } \quad T _ { \mathrm { s y s t e m } } .
$$

On averaging, the difference of these gives the desired quantity, subject to fluctuations in each of the terms.

# Minimum Detectable Power and Signal-to-Noise Ratio

Figure 7.44 shows the simplest possible detection scheme. It can be used at metre wavelengths for low signal frequencies $\mathit { \Theta } ^ { ' } < 1 0 0 \ : \mathrm { M H z }$ ). Following the antenna, the

![](images/4564a1c89512a313185a40317c5856bf5a2c67ca291e132d76395cd0e6739862.jpg)  
Fig. 7.44 Simple detection scheme (referred to as video detection) for the field of an electromagnetic wave

cavity, behaving as a bandpass filter, isolates a frequency band $\Delta \nu _ { \mathrm { s } }$ in the signal, centered on a frequency $\nu _ { \mathrm { s } }$ .

It is assumed, to simplify the calculation, that the non-linear element has the effect of transforming the signal $x ( t )$ into the quantity

$$
y ( t ) = x ( t ) ^ { 2 } , \mathrm { c u r r e n t } i ( t ) \propto E ( t ) ^ { 2 } .
$$

In practice, the transformation may be slightly different, for example,

$$
y ( t ) = \left| x ( t ) \right| , \qquad \mathrm { c u r r e n t } i ( t ) \propto \left| E ( t ) \right| ,
$$

but the conclusions would be similar. It will suffice to consider the appropriate transformation of the random variable ${ \bf x } ( t )$ , which is assumed to be a Gaussian process, with white spectral density, characterised by a noise temperature $T ( \mathrm { n o i s e } ) = T _ { \mathrm { n } }$ . The current $i ( t )$ is then filtered by a filter (Fig. 7.45) of passband $( \varepsilon , \ f _ { \mathrm { c } } )$ D, which excludes zero. Finally, the signal is recorded in digital or analogue form.

The result giving the power spectrum of the square of a random process, which is described in Appendix B, can be applied, noting that $\Delta \nu _ { \mathrm { s } } \ll \nu _ { \mathrm { s } }$ (for example, in the case of a centimetre receiver, $\nu _ { \mathrm { s } } \sim 1 0 ^ { 1 0 } \ \mathrm { H z }$ , and $\Delta \nu _ { \mathrm { s } } \sim 1 0 ^ { 7 } ~ \mathrm { H z } )$ ). The PSD of the signal is then given by the convolution

$$
S _ { \mathrm { s } } ( \nu ) \simeq ( 2 k T _ { \mathrm { n } } ) ^ { 2 } \Delta \nu _ { \mathrm { s } } \left[ \delta \left( \nu - \frac { f _ { \mathrm { c } } } { 2 } \right) + \delta \left( \nu + \frac { f _ { \mathrm { c } } } { 2 } \right) \right] \star \varPi \left( \frac { \nu } { f _ { \mathrm { c } } } \right) ,
$$

for $f _ { \mathrm { c } } \ll \Delta \nu _ { \mathrm { s } }$ . Fourier transforming gives the autocovariance $C _ { \mathrm { s } } ( \tau )$ , and finally

$$
\begin{array} { r } { \sigma _ { \mathrm { s } } ^ { 2 } = C _ { \mathrm { s } } ( 0 ) = ( 2 k T _ { \mathrm { n } } ) ^ { 2 } 2 \Delta \nu _ { \mathrm { s } } f _ { \mathrm { c } } . } \end{array}
$$

The signal due to the source is obtained simply by putting $T _ { \mathrm { n } } = 0$ ,

$$
\mathrm {  ~ \ s i g n a l } = \langle \boldsymbol { s } ( t ) \rangle = \langle E _ { \mathrm { \mathrm { s o u r c e } } } ^ { 2 } ( t ) \rangle = \sigma _ { \mathrm { E } } ^ { 2 } = 2 k T _ { \mathrm { s o u r c e } } \Delta \nu _ { \mathrm { s } } ,
$$

and the signal-to-noise ratio is then

$$
\frac { 2 k T _ { \mathrm { s o u r c e } } \Delta \nu _ { \mathrm { s } } } { 2 k T _ { \mathrm { n } } ( 2 \Delta \nu _ { \mathrm { s } } f _ { \mathrm { c } } ) ^ { 1 / 2 } } = \frac { T _ { \mathrm { s o u r c e } } } { T _ { \mathrm { n } } } \left( \frac { \Delta \nu _ { \mathrm { s } } } { 2 f _ { \mathrm { c } } } \right) ^ { 1 / 2 } .
$$

![](images/e87f45445998fe7b098c1da04f5cf5f3bc31bad04ab35a58c893cd1a5e1a4575.jpg)  
Fig. 7.45 Spectral densities: (a) of the filtered incident signal at $\nu _ { \mathrm { s } }$ , (b) after quadratic detection, only the low frequency part being shown, (c) after low frequency filtering, on an expanded scale. The bandpass filter cuts out zero frequency, and hence the impulse at the origin. Since $f _ { \mathrm { c } } \ll \Delta \nu _ { \mathrm { s } }$ , the PSD is almost constant across the whole filter width

The bandpass $f _ { \mathrm { c } }$ of the filter is related to the integration time $\tau$ by an equation of the form

$$
f _ { \mathrm { c } } \tau = \alpha , \qquad \alpha \sim 1 .
$$

The exact value of the coefficient $\alpha$ depends on the transfer function of the filter used. The general rule stating that the signal-to-noise ratio only increases as the square root of the measurement time is once again satisfied. Moreover, this ratio only increases as the square root of the passband $\Delta \nu _ { \mathrm { s } }$ . Indeed, when $\Delta \nu _ { \mathrm { s } }$ increases, the signal increases, but then so does the noise power.

The unwanted contributions from atmospheric emission and instrumental noise can be eliminated by pointing the antenna at two neighbouring points of the sky, and taking the difference, so that the minimum detectable power is, for a signal-to-noise ratio equal to one,

$$
P _ { \mathrm { m i n } } = k T _ { \mathrm { n } } \left( \frac { 2 f _ { \mathrm { c } } } { \Delta \nu _ { \mathrm { s } } } \right) ^ { 1 / 2 } \Delta \nu _ { \mathrm { s } } \quad [ \mathrm { W } ] \ .
$$

In the model considered here, it was assumed that the same filter $\Delta \nu _ { \mathrm { s } }$ was applied to all components of $i ( t )$ , namely, the signal due to the source, the signal from instrumental emission, and the signal due to the fluctuations of the detector. If this were not the case, it would be a simple matter to modify the argument.

# 7.5.2 Heterodyne Detection

This is the method now most commonly used on radiotelescopes, both on the ground and in space, from the submillimetre to the metre wave region. It was presented briefly in Fig. 7.42c. Here we shall discuss the different components required, together with the underlying physical principles and the way they are implemented.

Figure 7.46 gives a more detailed overview of the successive operations to which the incident signal is subjected. Its frequency is first changed by superposition, without loss of information, at a quadratic detector, of the signal field at frequency $\nu _ { \mathrm { s } }$ , and the field of a local oscillator at frequency $\nu _ { 0 }$ . The current output by the mixer is then, up to proportionality,

$$
i ( t ) \propto E _ { 0 } ( t ) E _ { \mathrm { s } } ( t ) ~ .
$$

It therefore depends linearly on the field $E _ { \mathrm { s } } ( t )$ , and has a component at the frequency $( \nu _ { 0 } - \nu _ { \mathrm { { s } } } )$ . This current, which is called the intermediate frequency (IF) signal, is then amplified and filtered, before being detected again and averaged by the exit filter of width $f _ { \mathrm { c } }$ . The first advantage of this setup (Fig. 7.46) is the possibility of precisely controlling the filtering after the IF stage, which allows a spectral analysis of the signal. The second advantage is the amplification of the signal due to the mixing of the two frequencies. If the local oscillator produces a strictly coherent field, the current $i ( t )$ can be made large compared with all noise sources within the receiver, leaving only those fluctuations originating in the signal itself. This argument fails for wavelengths at which quantum noise in the local oscillator can no longer be neglected. In the end, the noise properties of the system as a whole are determined by those of the amplifier(s) and the mixer. The spectral properties are determined by the feasibility and stability of the local oscillator, the operating frequency and frequency bandwidth of the mixer, and then the properties of the spectral analysis stages to be described later (see Sect. 8.4).

The mixer does not in itself differentiate between two signal frequencies which are symmetrical about the frequency $\nu _ { 0 }$ of the local oscillator. This confusion can perturb the measurement (analysis of a spectral line), in which case a filter can be placed before the mixer to block frequencies $\nu \ < \ \nu _ { 0 }$ . This is referred to as single sideband reception or SSB reception, as opposed to double sideband reception or DSB reception. In the latter case, the signal-to-noise ratio is clearly reduced by a factor of $\sqrt { 2 }$ (Problem 7.8), but the spectral coverage is doubled.

The intermediate frequency stage, after the mixer, and the ensuing stages are independent of $\nu _ { \mathrm { s } }$ and $\nu _ { 0 }$ . They depend only on the difference $\nu _ { 0 } - \nu _ { \mathrm { { s } } }$ . The heterodyne setup is thus applicable at all wavelengths, provided that one has a suitable local oscillator, amplifier, and mixer for the chosen frequency, sensitivity, and spectral characteristics of the source under investigation.

# Local Oscillator

The role of this subsystem is to provide a coherent signal, hence with stable frequency, without noise, at a frequency $\nu _ { 0 }$ very close to the frequency $\nu _ { \mathrm { s } }$ of the signal. In addition, the power supplied must be large enough to ensure if possible that the signal after mixing exceeds the noise of the mixer. The three requirements made of a local oscillator are thus: matched frequency, sufficient power, and absence of noise.

![](images/11506bf460a24e5dd0956400ce40309fcd33f5faa7bf6830ec512ae2a0047500.jpg)  
Fig. 7.46 Successive stages of a single sideband (SSB) heterodyne receiver. (a) Subsystems. (b) The time dependent signal. (c) Spectral density of the signals. Note the image frequency $\nu _ { \mathrm { I } }$ eliminated by the filter $\Delta \nu$

![](images/85d0a9f168bb9d7c207e5da1c6fa24ed8df9d20c0dc933e931a8d47a81f08299.jpg)  
Fig. 7.47 Frequency regions covered by molecular lasers between 150 and $8 5 0 \mathrm { G H z }$ $( 0 . 3 5 { - } 2 \mathrm { m m } )$ ) (frequencies indicated by vertical arrows) and mixers whose bandwidth would be $\pm 5 \ : \mathrm { G H z }$ . The ˙shaded area shows frequencies that can be reached by using these lasers as local oscillators. (After Roeser H.P. et al., Astron. Astrophys. 165, 287, 1986)

Let us mention briefly two types of local oscillator which played an important role in the development of radioastronomy throughout the second half of the twentieth century.

The klystron is a wave generator that was used for $\nu _ { 0 } \lesssim 1 8 0 \mathrm { G H z }$ . Capable of supplying high power $( 2 5 { - } 1 0 0 ~ \mathrm { m W } )$ ), it was developed mainly for telecommunications and radar.

The carcinotron is a wave generator, working on the following principle. A beam of electrons, of the same kinetic energy, move parallel to a grill. Modulation of the grill potential creates a variable electric field, whose frequency is related to the grill spacing. This can emit a few tens of mW up to $1 0 0 0 \mathrm { G H z }$ , and is a high quality source, but cumbersome and power-consuming, and impossible to send into space, for example.

Harmonic generators are frequency doublers or multipliers, using a non-linear element, such as a Schottky diode, excited by a klystron. The non-linear element then radiates the harmonics 2, 3, . . . , of the excitation frequency. The power obtained can reach several mW, up to around $5 0 0 \mathrm { G H z }$

Molecular lasers offer great spectral purity and stability, together with a very large number of lines, covering not only the submillimetre, but also the far and middle infrared $2 0 ~  { \mu \mathrm { m } }$ and beyond). The available power is from 0.1 to $1 \mathrm { m W } .$ . The main drawback is that they provide only spectral lines at discrete frequencies, which may not be close to the frequency $\nu$ under study (see Fig. 7.47).

Modern oscillators (2007) are Gunn effect generators. A solid-state diode is designed so that its current–voltage characteristic in a certain region has negative resistance $( \mathrm { d } V / \mathrm { d } I < 0 )$ ). With direct current, the diode begins to oscillate and the desired frequency $\nu _ { 0 }$ is obtained by placing the diode in a resonant cavity at this frequency, from which it is extracted by a waveguide. These diodes are made with semiconducting materials like GaAs (from a few $\mathrm { G H z }$ to $1 0 0 \ \mathrm { G H z }$ ), then gallium nitride (up to THz). Once they had become the standard local sources, they greatly facilitated the development of submillimetre astronomy, e.g., on the California Submillimeter Observatory14 (CSO) in Hawaii, or the HIFI instrument on board the Herschel space mission.

Another possible configuration has a powerful amplifier after the diode, in fact a high electron mobility transistor (HEMT) described further below, then a frequency multiplier producing a harmonic at the desired frequency. Noise temperatures lower than $1 0 0 \mathrm { K }$ can be achieved at $3 0 0 \mathrm { G H z }$ , and lower than $1 0 0 0 \mathrm { K }$ at $7 0 0 \mathrm { G H z }$ .

Other methods for making oscillators are under development at the time of writing (2007), using Josephson junctions,15 laser beats, up to very high frequencies (THz), or beyond and up to the mid-infrared, the quantum cascade laser (QCL).

In conclusion, we have presented a rather general radiofrequency detection setup, and we have shown that, in practice, a wide range of configurations is possible on this basis (see Table 7.9).

# Amplifiers

In most radiofrequency detection systems, the non-linear element is a significant source of noise. It is useful, therefore, to amplify the signal of frequency $\nu _ { \mathrm { s } }$ , or the IF signal $\nu _ { \mathrm { I F } } = \nu _ { 0 } - \nu _ { \mathrm { s } }$ , before detection.

D The principle of the various types of amplifiers is as follows. Energy is extracted from a local radiation source and transferred to the incident wave, in proportion with the incident energy, and in phase with the incident field. A coherent amplification effect is obtained, and the signal-to-noise ratio is improved as long as the amplifier gain remains less than

$$
g = { \frac { T _ { \mathrm { n } } } { T _ { \mathrm { a } } } } \ ,
$$

where $T _ { \mathrm { a } }$ is the noise temperature at the amplifier input, and $T _ { \mathfrak { n } }$ the noise temperature of the detection element.

Table 7.9 Radiofrequency reception. RF radiofrequency, IF intermediate frequency   

<table><tr><td>Component parts</td><td>RF amplifier Local oscillator</td></tr><tr><td></td><td>Non-linear RF element IF amplifier, filter(s),and correlator</td></tr><tr><td></td><td>IF detector (transistor)</td></tr><tr><td>Geometrical properties</td><td>Single pixel, fixed étendue λ² Small arrays (N≤10)</td></tr><tr><td>Polarisation</td><td>One polarisation detected</td></tr><tr><td>Spectral properties</td><td></td></tr><tr><td></td><td>Intrinsically wideband components</td></tr><tr><td></td><td>Post-IF spectral selectivity</td></tr><tr><td>Noise</td><td>Close to the thermodynamic limit</td></tr><tr><td></td><td></td></tr><tr><td></td><td>imposed by the system temperature</td></tr><tr><td></td><td></td></tr><tr><td>Temporal response</td><td>No particular limit</td></tr></table>

The modern method of amplification, which can be applied either directly to the incident RF signal or to the intermediate frequency (IF) signal, uses so-called high electron mobility transistors (HEMT). These are field-effect transistors based on a heterojunction, i.e., two semiconducing materials with different bandgaps. For example, the ODIN space mission (Sweden, Canada, Finland, and France), launched in 2001 and still running in 2007, includes a $1 . 1 \mathrm { m }$ radiotelescope and focal systems operating between 180 and $5 2 0 \mathrm { G H z }$ , with IF amplifiers based on this idea.

Here we briefly mention some of the systems developed over the period 1950–2000.

The parametric amplifier exploits the following idea. Consider an oscillator represented, for example, by a circuit with a resistor $R$ , an inductance $L$ , and a capacitance $C$ , in which one of the elements determining the resonant frequency, e.g., $C$ , can be varied. Let $\omega _ { 0 }$ be the original frequency, and $2 \omega _ { 0 }$ the frequency of modulation of $C$ . Assuming low damping, that is

$$
Q = \frac { 1 } { \omega _ { 0 } R C } \gg 1 ,
$$

the oscillator equation is

$$
\ddot { x } + \frac { 1 } { \tau } \dot { x } + \omega _ { 0 } ^ { 2 } ( 1 - \varepsilon \sin 2 \omega _ { 0 } t ) x = 0 ,
$$

with

$$
C = C _ { 0 } ( 1 - \varepsilon \sin 2 \omega _ { 0 } t ) , \quad \varepsilon \ll 1 , \quad L C _ { 0 } \omega _ { 0 } ^ { 2 } = 1 , \quad \tau = \frac { L } { R } .
$$

Seeking a solution of the form

$$
x = f ( t ) \sin \omega _ { 0 } t \ ,
$$

it follows that

$$
f ( t ) = K \exp \left( \frac { \varepsilon \omega _ { 0 } } { 2 } - \frac { 1 } { 2 \tau } t - \frac { \varepsilon } { 4 } \sin { 2 \omega _ { 0 } t } \right) \sim K \exp \left( \frac { \varepsilon \omega _ { 0 } } { 2 } - \frac { 1 } { 2 \tau } \right) .
$$

Amplification occurs if the two conditions

$$
\varepsilon > \frac { 1 } { \omega _ { 0 } \tau } \quad \mathrm { a n d } \quad \varepsilon \ll 2 + \frac { 1 } { \omega _ { 0 } \tau }
$$

are simultaneously satisfied. This is indeed possible, when the selectivity $Q$ is much greater than unity, as we assumed.

The system is only linear in a restricted amplitude range. An appreciable gain can be obtained. Power is transferred to the signal by modulation of the capacitance $C$ . It therefore comes from the oscillator which modulates this capacitance at the frequency $2 \omega _ { 0 }$ . In practice, the variable capacitance, sometimes called a Varactor, is a Schottky junction barrier (see below), whosecapacitance depends on the applied voltage by the relation

$$
C = C _ { 0 } \left( 1 - \frac { V } { V _ { 0 } } \right) ^ { - n } ,
$$

where $0 . 3 \lesssim n \lesssim 0 . 5$ . The typical noise temperature of a cooled parametric amplifier is 10 to $2 0 \mathrm { K }$ .

The idea of the maser amplifier is to use an external power source to populate the excited levels of a solid or gas beyond the population which would correspond to thermodynamic equilibrium. The stimulated emission produced by the incident radiation is in phase with that radiation, and in the same direction, so that amplification occurs.

![](images/d1a9921683dbecc18a51fb5a9e545e7ac0413093f6ef1e44527b7e1de987ecd7.jpg)  
Fig. 7.48 Energy states in a ruby maser, as a function of the applied magnetic field

A ruby maser is a crystal of alumina $\mathbf { A l } _ { 2 } \mathbf { O } _ { 3 }$ , in which $0 . 0 5 \%$ of the $\mathrm { A l } ^ { 3 + }$ ions are replaced by chromium ions ${ \mathrm { C r } } ^ { 3 + }$ . The combined effect of the $\mathrm { A l } _ { 2 } \mathrm { O } _ { 3 }$ lattice electric field and an external magnetic field creates four energy levels (Fig. 7.48) for the electron spin $S = 3 / 2$ of the ${ \mathrm { C r } } ^ { 3 + }$ ion.

DMagnetic dipole transitions are possible between these levels. The maser can be pumped by a local oscillator (Fig. 7.48) at the frequency $( E _ { 4 } - E _ { 2 } ) / h$ , and it will then emit the energy $( E _ { 4 } - E _ { 3 } )$ (stimulated emission). The crystal must be cooled so that the differences of population are significant:

$$
{ \frac { E _ { 3 } - E _ { 1 } } { h } } \quad ( { \mathrm { a t ~ } } B = 0 ) = 1 1 . 4 6 { \mathrm { ~ G H z } }
$$

corresponds to a temperature

$$
T = \frac { E _ { 3 } - E _ { 1 } } { k } = 0 . 5 5 \mathrm { K } .
$$

The typical noise temperature of a maser amplifier lies between 15 and $5 0 ~ \mathrm { K }$ .

The Rydberg maser uses states close to the ionisation continuum of the hydrogen atom. The energy difference between two of these states is given by

$$
\Delta E = R \left[ \frac { 1 } { n ^ { 2 } } - \frac { 1 } { ( n + 1 ) ^ { 2 } } \right] \sim R n ^ { - 3 } ,
$$

for $n \gg 1$ . For $n \sim 3 0$ , the energy difference corresponds to millimetre wavelengths. Electrical  dipole transitions between these levels are easy to excite, and the amplification principle is as before.

# Mixers

We said above that there were two key factors in the design of a mixer, i.e., the spectral bandwidth $B$ it accepts and the noise temperature that characterises it. All things being equal, the desired value of $B$ increases with the frequency $\nu _ { \mathrm { s } }$ of the incident signal. This observation means that simpler mixing techniques are possible at frequencies below $8 0 \ : \mathrm { G H z }$ $\lambda \gtrsim 4 ~ \mathrm { m m }$ ). Today, HEMT transistors can be used, operating at ever higher frequencies and able to amplify then detect IF signals, while maintaining a sufficiently broad spectral bandwidth $B$ .

At higher frequencies, viz., millimetre and submillimetre, the predominant mixer is the SIS superconducting junction and the hot electron mixer (HEB). The Schottky diode is still used, but performs less well with regard to noise.

![](images/0d3a4f4c8112b506e643f77025c9d69a90d0d9dd7b72e5db22fb096653b865db.jpg)  
Fig. 7.49 Electron microscope image of a SIS junction made at the Paris Observatory (LERMA) for the frequency band 385–500 GHz of the European telescope ALMA in Chile. Document courtesy of LERMA

SIS Junction

The underlying principle of the superconductor–insulator–superconductor (SIS) junction has already been mentioned in Sect. 7.3. The circulation of a quasiparticle current in the insulator is a non-linear effect, as can be seen from the current–voltage characteristic of the junction shown in Fig. 7.17. It can thus be used as a frequency mixer.16 Since the interaction between the radiation and the material occurs by quanta, the theoretical noise temperature limit is very low, viz., $T _ { 0 } ~ = ~ h \nu / k$ . At $1 0 0 ~ \mathrm { G H z }$ , we have $T _ { 0 } ~ = ~ 5 ~ \mathrm { K }$ , whereas the best diodes reach $T _ { \mathrm { n } } ~ \approx ~ 2 0 ~ \mathrm { K }$ , and at $1 \ \mathrm { T H z }$ , $T _ { \mathrm { n } } ~ \approx ~ 1 0 0 0 ~ \mathrm { K }$ . This favourable factor means that a low power local oscillator can be used, and it can even be integrated into the diode. However, the intrinsic capacitance of the geometry (see Fig. 7.49) does not authorise a use exceeding the THz range.

The high frequency behaviour depends on the product of the resistance and the capacitance of the junction. At the time of writing (2007), Nb(niobium)– $\mathrm { A l O } _ { 2 }$ (alumina)–PbBi junctions are used up to $1 . 2 \mathrm { T H z }$ $\lambda = 0 . 3 5 \mathrm { m m }$ ).

DSIS junctions are small and can thus be arranged in small format 2D arrays to make multipixel image detectors at radiofrequencies. For example, the $3 0 \mathrm { m }$ IRAM telescope is equipped with a $3 \times 3$ array, fed by juxtaposed horns (which reduces the filling factor), and the James Clerk Maxwell Telescope (JCMT) in Hawaii has a $4 \times 4$ array, operating at $\lambda = 8 0 0 \mu \mathrm { m }$ .

Hot Electron Mixer

We have already seen how the free electron gas in a very pure InSb semiconductor is heated by incident radiation, modifying its resistivity when this energy is transferred to the crystal lattice, and thereby constituting a hot electron bolometer (HEB). However, this change in resistivity, proportional to the incident energy, is thus proportional to the square of the electric field incident on the material, whence it can function as a mixer.

In this case, a nanoscale superconducting bridge made from niobium nitride (NbN) and connecting two gold electrodes17 The signal (source and local oscillator) is focused on this bridge by a lens or quasi-optical waveguide. Heterodyne mixing results from the purely resistive transition between the superconducting and normal states, induced when the RF signal heats the material. A broad IF bandwidth (up to $B = 2$ GHz) is obtained by reducing the volume of the NbN film to give the lowest Dpossible thermal time constant. A noise temperature of $T _ { \mathrm { n } } = 7 5 0 ~ \mathrm { K }$ is obtained at $1 . 5 \mathrm { T H z }$ , rising to $3 0 0 0 \mathrm { K }$ at $3 \ \mathrm { T H z }$ Din double sideband (DSB) mode.

Schottky Diode

This non-linear component, also called a Schottky barrier, 18 was long considered the ideal radiofrequency mixer. It has gradually been superseded by detectors coming closer to the quantum noise limit, such as those we have just described. However, it remains widely used when the signal is strong enough not to be significantly degraded by the mixer noise. This is the case, for example, when a millimetre wave instrument is used to observe the Earth atmosphere from space, or the surface of Mars from a probe in orbit around the planet. The signal, similar to a blackbody at around $2 5 0 \mathrm { K }$ , is then strong enough.

The aim here is to outline the effects of contact between a metal and a semiconductor. Figure 7.50 illustrates the phenomena resulting from such a contact. In equilibrium, the majority charge carriers in the semiconductor move away from the contact area, in such a way that the Fermi levels in the metal coincide with those in the semiconductor. A barrier, or depletion zone, emptied of majority charge carriers, appears in the semiconductor. A simple calculation shows that the width of this barrier is given by the expression

$$
x _ { \mathrm { b } } = \left( \frac { 2 \varepsilon | V _ { 0 } | } { N e } \right) ^ { 1 / 2 } ,
$$

where $\varepsilon$ is the permittivity of the material, $V _ { 0 }$ is the difference between Fermi levels, and $N$ is the carrier number density. For $\varepsilon = 1 6 \varepsilon _ { 0 }$ , $V _ { 0 } = 0 . 5 \ V$ , $N = 1 0 ^ { 1 6 } \mathrm { c m } ^ { - 3 }$ , this gives ${ x _ { \mathrm { b } } = 0 . 3 \ \mu \mathrm { m } }$ .

D D D DThe current–voltage characteristic of the junction or diode is shown in Fig. 7.51. In the absence of any applied voltage, a current may nevertheless cross the junction, either because the thermal energy of the electrons is large enough to allow them to cross the potential barrier, or because, having insufficient energy, they still manage to cross it by tunnelling. At low temperatures $\begin{array} { r } { T \ll 3 0 0 \mathrm { K } , } \end{array}$ , this latter effect dominates, and the characteristic can be written

![](images/a7282319d3702371ff6e837305356db441465c89790b2e8d50b2aeefdcffa16b.jpg)  
Fig. 7.50 Contact between a metal and an $n$ -type semiconductor. The dashed line represents the Fermi level in each material. The ordinate is the electrostatic potential

![](images/77c8f4cfba1836aa6f4e6da410472aeb5cb1ec17093e8d7dcbd0dfa149b9f8db.jpg)  
Fig. 7.51 Current–voltage behaviour of a metal/n-type semiconductor. A positive voltage increases the potential barrier, and the current is decreased

$$
I \sim I _ { \mathrm { s } } \exp \left( \frac { e V } { E _ { \infty } } \right) ,
$$

where $I _ { \mathrm { s } }$ is the saturation current, and $E _ { \infty } \propto x _ { \mathrm { b } } ^ { - 1 } \propto N ^ { 1 / 2 }$ .

If $\Delta f$ / /is the frequency passband of the filter which follows the diode, the current $i$ will produce a fluctuation (see Sect. 7.2)

$$
\langle \Delta i ^ { 2 } \rangle = 2 e i \Delta f \ ,
$$

and the corresponding noise power is (Problem 7.2)

$$
P = { \frac { R \langle \Delta i ^ { 2 } \rangle } { 4 } } = { \frac { \mathrm { d } V } { \mathrm { d } I } } { \frac { 2 e i \Delta f } { 4 } } .
$$

This power can be characterised by a noise temperature, using the power spectrum of thermal noise (see Sect. 7.2). It follows that

$$
P = k T _ { \mathrm { d } } \Delta f = { \frac { 1 } { 2 } } { \frac { \mathrm { d } V } { \mathrm { d } I } } e i \Delta f ,
$$

implying

$$
T _ { \mathrm { d } } = \frac { E _ { \infty } } { 2 k } .
$$

The noise temperature $T _ { \mathrm { d } }$ characterises the intrinsic quality of the diode.

In practice, the semiconductor used is highly doped gallium arsenide (AsGa). A thin layer of lower dopant concentration is formed on the surface by molecular epitaxy, and this surface is then put into contact with the metal.

Epitaxy is the name for the process which consists in growing a thin layer of different composition on the surface of a monocrystalline structure, in such a way that the layer has the same crystal structure as the substrate. This process is commonly used in microelectronics, for example, to deposit doped silicon onto pure silicon. The layer is deposited by condensation of a vapour, or crystallisation of a liquid.

The drive to reduce noise requires low operating temperatures $( \lesssim 2 0 ~ \mathrm { K } )$ , and low dopant levels in the epitaxial layer, in order to reduce tunnelling. Moreover, the thickness of this layer must not exceed that of the depletion zone, for this would introduce extra resistance.

There is a high frequency limit to the response of these diodes. Beyond $3 0 0 \mathrm { G H z }$ $\lambda < 1 \mathrm { m m } )$ ), the intrinsic capacitance of the diode creates a resistance–capacitance filter which reduces the response. Certain processes have been devised to reduce this capacitance to $1 . 5 \times 1 0 ^ { - 1 5 } \mathrm { F } ,$ thereby extending the domain of operation up to $7 0 0 \mathrm { G H z }$ .

# Wide Band Receiver

Heterodyne detection has intrinsic spectral selectivity by spectral analysis of the IF signal (see Chap. 8). However, the total received power, limited only by the passband $B$ of the mixer, can be measured directly at the mixer output, hence with very low spectral selectivity. An example is shown in Fig. 7.52.

# 7.5.3 The Diversity of Radioastronomy

Radiofrequency detection covers a vast spectral region which today links up with the infrared via the submillimetre region. Needless to say, this involves a wide range of different technologies for the components used in observing systems. Table 7.9 sums up the basic properties of detectors, on the basis of which many different observational combinations are possible.

![](images/29aa462ae90f85752a2a1d9dcd1ba9c573f55fe412a3839fb7a6e6c69f8f9cfe.jpg)  
Fig. 7.52 Wide band receiver. A measurement of the power radiated by the planet Venus at $\lambda = 6 ~ \mathrm { c m }$ , with the $4 2 . 6 \mathrm { ~ m ~ }$ radiotelescope at Kitt Peak (Arizona). The planet is alternated with Dthe sky background in its neighbourhood (E, W, N, S). CAL denotes a calibration (Sect. 3.5.1). The selected polarisation is in the N–S direction. The size $\theta$ of the planet is small compared with the field of coherence, and the deviation is proportional to $\textstyle \int _ { \Delta \nu } B _ { \nu } ( T _ { \mathrm { v e n u s } } ) \pi \theta ^ { 2 } \mathrm { d } \nu / 4$

As in other wavelength regions, the observing system couples an Earth-based or spaceborne telescope, sometimes part of an array (see Sect. 6.5.1), with these receivers, associated with a spectroscopic capacity to be examined in detail in Chap. 8. These different components are arranged and combined as dictated by the desired observation and the given astrophysical problem. By visiting the websites of radioastronomy observatories, the reader will be able to confirm the extreme diversity and wealth of possible combinations, put together in each case to optimise the observation. Here are some examples:

• Detection of a very faint extragalactic radio source, using a large collecting area, a spectral band $\Delta \nu _ { \mathrm { s } }$ as wide as possible, and an integration time as long as possible. Analysis of the very rapid variations of a pulsar, in order to determine the period, the spectral band again being wide, but the integration time short (less than one millisecond). Analysis of solar flares, in which the rapid variations of the emission depend on the frequency, and high spectral selectivity and temporal response must be achieved, whilst maintaining the signal-to-noise ratio. Analysis of the spectral line profile of an interstellar molecule, which requires very high spectral resolution $( \nu _ { \mathrm { s } } / \Delta \nu _ { \mathrm { s } } \sim 1 0 ^ { 5 } )$ , using the kind of spectrometer described in more detail in Sect. 8.4. Measurement of the angular size and imaging of a radiosource. This requires the use of an interferometer array, with comparison of the phase of a wave at two spatially separated receivers, in order to obtain information about the size of the source. The spectral resolution is not necessarily high, unless the emission is spectrally narrow, e.g., an emission line.

Figure 7.53 shows schematically the various configurations that can be associated with such problems. A fourth dimension could be added, to show the frequency of the received signal.

# 7.6 Observing Systems for Gamma-Ray Astronomy

In this high energy region, which we shall define as having a lower limit of the order of $1 0 \ \mathrm { k e V }$ $( \lambda \sim 0 . 1 \ \mathrm { n m } )$ ), continuing on from the X-ray region, the notions of telescope, detector, and spectrometer considered up to now to be independent entities tend to merge into a single system which fulfills all these functions. This is mainly because, in contrast to other wavelengths, there are no mirrors available that could form images from incident $\gamma$ radiation. The lower limit, clearly fixed in the years 1970–2000 at around $1 0 \mathrm { k e V }$ by the limits to the possible use of mirrors, is tending to move toward ever higher energies, and will no doubt exceed a few hundred keV in the near future, while the $\mathrm { X }$ -ray region moves up to higher energies by means of its own techniques. This illustrates the somewhat arbitrary but merely practical nature of the way the electromagnetic spectrum has been divided up for the purposes of this book. At the very highest energies, the $\gamma$ ray region continues to move upwards, and now extends beyond $1 0 \mathrm { T e V } .$ .

![](images/eeee4b94cf89fbf038915b43adf137e6ba4f6f8a386526310c53480ca337894c.jpg)  
Fig. 7.53 The diversity of observing combinations in radioastronomy. Domains of application are only given up to an order of magnitude. A fourth dimension is needed to represent frequency, but each subject identified is treated successively over the whole frequency range from $1 \ \mathrm { T H z }$ to at least $1 0 0 \mathrm { M H z }$

In Chap. 5, we presented certain features of image formation at $\gamma$ ray wavelengths which tended rather to resemble those of conventional telescopes. Here we bring together the notions which for other wavelength regions have been distributed throughout the first part of this chapter on detectors and Chap. 8 on spectrometers. In addition, we shall retain the term telescope, which is commonly used to refer to the whole system receiving, detecting, and analysing the $\gamma$ radiation energy from astronomical sources. Such systems began to appear naturally enough at the beginning of the 1960s, in particle or nuclear physics laboratories which have their own traditions of instrumentation. In particular, since the 1990s, a field known as astroparticle physics has come into being, bringing together the problems of high energy astrophysics, where the relevant mechanisms involve the nuclei of atoms rather than their electronic shells. Instrumentation for observing astronomical sources emitting at such energies has also been developing at a considerable rate.

It should be said, however, that, despite immense progress accomplished since the 1970s in the $\gamma$ ray region, angular resolutions remain less good than in other spectral regions at the time of writing (2007), and most sources must still be considered as unresolved by today’s instruments. But considerable progress has been made in levels of sensitivity for the detection of faint sources, spectral resolution, and the very high energy frontier. We shall thus discuss the question of spatial resolution, then spectral resolution, both being closely related to the type of detector used. Tables 7.10 and 7.11 give an overview. Each of these devices is then used in a specific instrument, generally carried in space, although occasionally exploiting the Earth atmosphere as detector.

Table 7.10 Detection in ” ray astronomy   

<table><tr><td>Interaction</td><td>Type of detector</td><td>Energy range</td><td>Imaging</td></tr><tr><td rowspan="3">Photoelectric absorption</td><td>CdTe crystal</td><td>10 keV-1MeV</td><td>Coded mask and segmented imager (104 pixels)</td></tr><tr><td>Scintillators</td><td>100keV-10MeV</td><td>Coded mask and segmented imager (10³ pixels)</td></tr><tr><td>Ge crystal</td><td>10keV-10MeV</td><td>Coded mask and segmented imager (10 pixels)</td></tr><tr><td>Compton scattering</td><td>Scintillators or CdTe+ CsI Si+ Ge Si + CdTe</td><td>100keV-10MeV</td><td>Intrinsic and/or coded mask</td></tr><tr><td>Pair effect</td><td>Spark chamber then Si trackers</td><td>20MeV-300GeV</td><td>Intrinsic</td></tr><tr><td>Pair effect (air shower formation and Cherenkov radiation)</td><td>Photomultiplier tubes</td><td>100 GeV-100TeV</td><td>Intrinsic</td></tr></table>

Table 7.11 Main instruments for ” ray astronomy   

<table><tr><td>Mission</td><td>Date</td><td>Energy range</td><td>Instrument</td><td>Separating power</td><td>Spectral resolution E/△E</td></tr><tr><td>HEAO-1</td><td>1977-1979</td><td>80keV-2MeV</td><td>A4-MED</td><td>17°</td><td>4</td></tr><tr><td>HEAO-3</td><td>1979-1981</td><td>50keV-10MeV</td><td>HRGRS</td><td>30°</td><td>500</td></tr><tr><td>COS-B</td><td>1975-1982</td><td>50MeV-10 GeV</td><td></td><td>0°</td><td>2</td></tr><tr><td>GRANAT</td><td>1989-1998</td><td>30keV-1MeV</td><td>SIGMA</td><td>20&#x27;</td><td>5-10</td></tr><tr><td>CGRO</td><td>1991-2000</td><td>20keV-10MeV</td><td>BATSE</td><td>5°</td><td>10</td></tr><tr><td>CGRO</td><td>1991-2000</td><td>20keV-10MeV</td><td>OSSE</td><td>3.8°×11.4°</td><td>10</td></tr><tr><td>CGRO</td><td>1991-2000</td><td>1-30 MeV</td><td>Comptel</td><td>2-4°</td><td>10-20</td></tr><tr><td>CGRO</td><td>1991-2000</td><td>20MeV-30 GeV</td><td>EGRET</td><td>1-50</td><td>5</td></tr><tr><td>INTEGRAL</td><td>2002-</td><td>15keV-1MeV</td><td>IBIS/ISGRI</td><td>12&#x27;</td><td>3-30</td></tr><tr><td>INTEGRAL</td><td>2002-</td><td>15keV-8MeV</td><td>SPI</td><td>2.6°</td><td>50-500</td></tr><tr><td>AGILE</td><td>2007-</td><td>10MeV-10 GeV</td><td>LAT</td><td>0.1-3°</td><td>10</td></tr><tr><td>GLAST</td><td>2008-</td><td>10 MeV-100 GeV</td><td>LAT</td><td>0.1-3°</td><td>10</td></tr><tr><td>Telescope</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Whipple</td><td>1989-2000</td><td>500GeV-5TeV</td><td></td><td>0.5°</td><td>5</td></tr><tr><td>HEGRA</td><td>1993-2002</td><td>500 GeV-10 TeV</td><td></td><td>20&#x27;</td><td>5</td></tr><tr><td>CAT</td><td>1996-2002</td><td>200 GeV-10 TeV</td><td>1</td><td>20&#x27;</td><td>5</td></tr><tr><td>HESS</td><td>2003-</td><td>100 GeV-100TeV</td><td></td><td>10&#x27;</td><td>7</td></tr><tr><td>MAGIC</td><td>2004-</td><td>50GeV-50TeV</td><td>1</td><td>18&#x27;</td><td>7</td></tr></table>

# 7.6.1 Spatial Resolution of Gamma-Ray Sources

Here we discuss several types of $\gamma$ ray telescopes, in the sense of generalised system using different physical processes to determine the direction of the incident radiation.

# Compton Telescope

In the energy region extending from several hundred keV to several MeV, the interactions of $\gamma$ rays with matter are dominated by Compton scattering1 (see Sect. 7.3.1). An acceptable measurement of the incident photon energy can only generally be made in this region by instigating a series of interactions which end in a photoelectric absorption, and such a succession of interactions can only be guaranteed by a detector of a certain thickness. This kind of detector, bombarded by radiation belt protons (see Sect. 2.9.2) and cosmic rays, suffers from a great deal of noise. If it is split into two separate parts and only those events simultaneously triggering the two parts are retained, almost all background events are eliminated, because these events generally only trigger one of the two detectors. On the other hand, a large proportion of events undergoing Compton scattering is conserved. Consequently, a significant background reduction is obtained, usually by more than an order of magnitude, and this can procure a considerable gain in terms of signalto-noise ratio if the system is designed to favour the Compton scattering of photons along the telescope axis. The nature and size of the first part of the detector must be chosen so as to maximise the probability of single Compton scattering (low atomic number $Z$ of the material). In contrast, the second detector must maximise absorption (high $Z$ , high mass), in order to ensure total absorption of energy.

Equipped with a collimator, such a Compton telescope can give an image of the whole celestial sphere by scanning. This is analogous to the technique used in the HEAO1-A4 experiment (1977– 1979), but operating at higher energies. If the detectors are position sensitive, such scanning is not necessary, but one is faced with a classic dilemma: a large aperture results in high sensitivity but poor angular resolution, while a small aperture guarantees good angular resolution at the expense of the sensitivity. As we saw in Sect. 5.2.5, the coded mask provides a solution to this problem and can be profitably applied here. The idea is then analogous to the Sigma experiment: imaging would be of comparable quality, being linked to coded mask techniques, but at higher energies (greater than $1 \mathrm { M e V } _ { \cdot }$ ).

Still considering the case of position sensitive detectors, it is also possible to use the ballistics of the Compton interaction to restrict the direction at which the photons arrive (scattering angle) and deduce the position of the source statistically. In this case, imaging performance depends on the spectral resolution of the two detectors and the distance between them. However, efficiency decreases rapidly with this distance and a compromise must be found between sensitivity and angular resolution. This latter method is used in the COMPTEL experiment aboard the Compton

Gamma-Ray Observatory (GRO) which flew from 1991 to 2000. The distance of about $1 . 2 ~ \mathrm { m }$ between the two detectors leads to a separating power of around 5 degrees. It is also possible in the case of very closely positioned detectors to use both a coded mask for imaging and also Compton ballistics for a further background reduction. One then selects only those events for which all calculated incident directions lie within the solid angle subtended by the mask at the point of first interaction. This method is used by the IBIS instrument carried on board the INTEGRAL mission (launched in 2002).

The spectral performance of this type of telescope with regard to sensitivity and imaging are governed by the energy resolution of the weakest of the two detectors.

# Pair Effect Telescope

Beyond energies of a few MeV, the pair effect dominates the interactions between photons and matter (see Sect. 7.3.1). The photons are detected in two stages: first conversion, i.e., pair creation, then measurement of the electron and positron trajectories, from which the direction of the incident $\gamma$ ray can be deduced.

Indeed, in the center of mass system, the electron and positron are emitted in opposite directions, while in the laboratory system, they are emitted in the direction of the photon, modified by the recoil motion of the nucleus responsible for the electric field in which electron–positron production occurred. Up to this recoil, the directions of the electron and positron are related to the direction of the incident photon.

Pair creation becomes more efficient in stronger electric fields. In matter, it occurs in the electric fields of atomic nuclei, and the strength of these fields depends on the number of protons in the nucleus. This is why materials with high atomic number (high $Z$ ) provide the most efficient conversion (see Fig. 7.20), and lead is usually used for this purpose. On the other hand, good conversion efficiency also requires a thick converter, and the electrons will tend to scatter more (Moliere scattering) \` as the atomic number of the converter material and thickness of the converter are increased. This means that electrons leaving a thick converter are likely to have lost all memory of the direction of the incident $\gamma$ ray.

This difficulty has given rise to the basic design of the pair effect telescope. In order to limit electron scattering, thin plates of lead are used, inserted between devices able to measure the electron trajectories. Good conversion efficiency is guaranteed by using many plates, while the fact that they are thin ensures an accurate measurement of electron and positron trajectories (Fig. 7.54). The latter are measured using techniques developed for particle accelerators, such as spark chambers up until the mid-2000s in missions like SAS-2, COS-B, Compton/EGRET (Energetic Gamma Ray Telescope), and silicon strip trackers in the future, e.g., in the Gamma ray Large Area Space Telescope (GLAST) mission (launch 2008).

The angular resolution of such a telescope thus depends on the photon energies, since the error resulting from electron scattering increases as the energy decreases, being a few degrees at $5 0 \mathrm { M e V } ,$ , and only a few tens of arcmin in the GeV range and beyond. The photon energies, generally measured using a calorimeter absorbing the pair, can also be estimated from the observed scattering of the electron and positron. The event rate is high, but events due to celestial $\gamma$ rays are rather rare, and observation times and data processing are thus very long (of the order of a month). The production of $\mathrm { e ^ { + } e ^ { - } }$ pairs is an unambiguous signature of $\gamma$ rays with energies greater than a few MeV. This signature provides an efficient way of rejecting the background, whence pair effect telescopes can claim relatively good sensitivity: $\approx$ $1 0 ^ { - 7 } \mathrm { c m } ^ { - 2 } \mathrm { s } ^ { - 1 }$ in one month of observation by EGRET.

![](images/2e841e2c5273a8b5faea1cfbdedf9c0bdccf0628140589e7fef4a989f1ecd7b6.jpg)  
Fig. 7.54 Telescopes for $\gamma$ -ray observation. Top right: The telescope carried by COS-B, one of the first $\gamma$ -ray observation satellites (1975–1982). The plates of the spark chamber can be seen, and also the scintillators (shaded) placed around the main detector as anticoincidence devices, which are designed to detect and eliminate the background signal due to charged particles. The scintillators $B _ { 1 }$ , $C$ and $B _ { 2 }$ trigger the chamber, and the calorimeter $E$ measures the energy of the particles. PMT stands for photomultiplier tube. Top left: View of an event (pair formation) in the spark chamber. From Paul J., 1979, private communication. See also Bignami et al., Sp. Sci. Instrum. 1, 245, 1975. With the kind permission of D. Reidel Publishing Company. Bottom: Schematic diagram of the Fermi Large Area Telescope (LAT). The telescope has dimensions $1 . 8 ~ \mathrm { m } \times 1 . 8 ~ \mathrm { m } \times 0 . 7 2 ~ \mathrm { m }$ . The required power and the mass are $6 5 0 \mathrm { W }$ and $2 7 8 9 \mathrm { k g }$  , respectively. From Atwood W.B. et al., Ap. J. 697, 1071, 2009

# Spark Chambers

In a spark chamber, $\gamma$ rays interact by pair effect in plates made from a high $Z$ material. Alternatively, charged sheets of wires are inserted between the plates. A created electron and positron ionise a gas (neon) and a spark is produced in the gas between the electrodes formed by the sheets of wires. The trajectories of the particles are thus materialised (Fig. 7.54) and recorded either photographically or using a vidicon tube (see Sect. 7.4).

# Silicon Strip Tracking Systems

Once again, converter plates are used for pair creation, but the gas and wires are replaced by grids of silicon detectors (Fig. 7.54). The electron or positron ionises the silicon encountered along their trajectories. The resulting electrons and holes migrate under the effect of the electric field toward the electrodes and induce a current pulse at the terminals of these electrodes. The track followed by the pair can be reconstructed by analysing the coincidence signals in the tracker ensemble.

# Atmospheric Cherenkov Telescope

A 1 TeV photon entering the Earth atmosphere interacts with it at an altitude of around 10 kilometres, producing an electron–positron pair. The electron quickly generates high energy $\gamma$ rays by inverse Compton scattering, while the positron annihilates to emit a further two high energy $\gamma$ rays. These $\gamma$ rays will in turn create $\mathrm { e ^ { + } e ^ { - } }$ pairs and the process repeats, generating an air shower. The electrons in the shower are relativistic, moving a speed $\nu$ close to the speed of light in vacuum, and in fact faster than the speed of light in the atmosphere $( c / n$ , where $n$ is the refractive index of the atmosphere). The result is a very brief flash of blue Cherenkov emission,20 lasting only a few nanoseconds, emitted along a cone with axis close to the direction of the $\gamma$ ray which originated the shower and with greater apex angle $\theta$ for higher values of the speed $\nu$ of the electrons. In fact, co $\mathfrak { s } \theta = c / \nu n$ . At an altitude of around $1 0 0 0 \mathrm { m }$ D, an electromagnetic shower contains only Cherenkov photons and extends over about a kilometre.

![](images/441487c00be8d7845310352e3d78a66d8f712e0742f4d4837d2f043005d68c5e.jpg)  
Fig. 7.55 Two of the four light collectors forming the HESS instrument in the Namibian desert. Photo courtesy of the HESS collaboration and CEA/DAPNIA

There are two techniques for measuring Cherenkov air showers. In the more popular imaging technique — used, for example, in the High Energy Stereoscopic System (HESS), set up in Namibia in $2 0 0 4 ^ { 2 1 }$ (see Fig. 7.55) — each Cherenkov cone, reflected by a parabolic mirror, forms an ellipse in the focal plane of the mirror. The dispersion in the directions and speeds of the electrons produces ellipses with different centers and different sizes, forming a relatively uniform quasi-elliptical spot. This feature is used to distinguish electromagnetic showers from hadronic showers, which produce much less regular spots. The orientation of the ellipse is related to the direction of the initial $\gamma$ ray. By measuring the angular distribution of the Cherenkov light, $9 9 \%$ of the cosmic ray protons can be rejected, and at the same time angular resolutions of a tenth of a degree can be achieved. The detection threshold with this technique is of the order of a few hundred GeV.

The second, so-called sampling technique consists in measuring as accurately as possible the shape of the blue light wavefront by means of fine spatial sampling and accurate time measurements. This wavefront is almost spherical for an electromagnetic shower and more spread out for a hadronic shower. This technique, which requires an array of optical reflectors with large collecting area, has been developed by reusing former solar energy production units. This is exemplified by the CELESTE experiment, set up since 2000 at the Themis power generating site in´ the French Pyren´ ees. At the present time, sampling s´ ystems are less sensitive than imagers, but have an energy detection threshold ten times lower.

Whatever technique is used, the brevity and colour of the Cherenkov emission necessitates photomultiplier tubes as detecting element (see Sect. 7.4.3).


<!-- chunk 0007: pages 421-490 -->
Between 1996 and 2007, decisive progress was made with this method. On the one hand, the imaging technique, developed in particular in the United States for the Whipple instrument in the 1980s, is now in a dominant position. On the other hand, new instruments are improving this technique. The French CAT experiment, set up at the Themis site in France in 1996, uses a 600 pixel high resolution´ camera able to carry out detailed analysis of Cherenkov images, with a consequently improved separation between $\gamma$ photons and hadrons. At the same time, the German High Energy Gamma Ray Astronomy (HEGRA) experiment22 in the Canaries has implemented an innovative stereoscopic technique, able to observe a single air shower simultaneously with four telescopes. This robust method can achieve angular resolutions of the order of one tenth of a degree and further reduces the hadron background noise.

In 2004, a new generation of detectors came on the scene with the French– German High Energy Stereoscopic System (HESS).23 This experiment associates the methods used successfully in CAT and HEGRA, viz., high resolution Cherenkov imaging and stereoscopy.

HESS comprises 4 large mirrors of $1 0 0 ~ \mathrm { m } ^ { 2 }$ each, placed at the corners of a square of side $1 2 0 \mathrm { m }$ . The focal length of the mirrors is $1 5 \mathrm { ~ m ~ }$ . A camera consisting of 960 small photomultiplier tubes is placed at the focal point of each mirror. These PMTs are particularly well suited to detecting the flash of Cherenkov light thanks to their fast response, sensitivity in the blue region, and low noise levels. The sensitivity achieved above $1 \ \mathrm { T e V }$ is $1 0 ^ { - 1 3 } \mathrm { c m } ^ { - 2 } \mathrm { s } ^ { - 1 }$ . The gain in sensitivity over previous experiments (an order of magnitude) is such that, between 2004 and 2006, about thirty new sources of very high energy $\gamma$ radiation were discovered, mainly in the galactic plane. The experiment is set up in Namibia, giving access to the southern sky and hence to the central region of our Galaxy, a region known to contain many $\gamma$ ray sources. For the first time it has become possible to resolve extended sources, and in particular to study the morphology of supernova remnants, by virtue of the field of view of 5 degrees and resolution of around 10 arcmin (FWHM).

# 7.6.2 Spectral Analysis of Gamma-Ray Sources

Spatial resolution and detection efficiency are clearly the criteria for quality in an image-forming (or imaging) detector. But those for a spectrometer are more subtle. Indeed, although spectral resolution is an obvious criterion, the total efficiency, on the other hand, is not in itself a good criterion in the $\gamma$ ray region. This is because Compton scattering, in which the scattered photon escapes, does not lead to a determination of the incident photon. In fact, it is the efficiency in the peak of the total absorption that must be considered, and this increases with the charge number $Z$ , and the mass (volume $\times$ density) of the detector. The spatial resolution of a $\gamma$ ray detector depends on the energies involved, being limited by the Compton scattering events. It will improve if the scattering is minimal, which implies a high $Z$ and dense material, and these are therefore the working criteria for selecting materials, whether for an imager or for a spectrometer. In contrast, high volume is advantageous in spectrometry, but not in segmented imaging, in which each pixel is an independent detector. These simple remarks can be used to classify some materials (Table 7.12).

Table 7.12 Materials for $\gamma$ -ray detection. S scintillator, SC semiconductor   

<table><tr><td rowspan="2">Material</td><td rowspan="2">Type</td><td rowspan="2">Z</td><td rowspan="2">Density [g cm-³]Volume [cm³]</td><td colspan="2"></td><td colspan="2">Spectral Resolution at</td></tr><tr><td>Min</td><td>Max</td><td>122 keV</td><td>511keV</td></tr><tr><td>NaI(Tl)</td><td>S</td><td>23-53</td><td>3.7</td><td>1</td><td>104</td><td>0.12</td><td>0.09</td></tr><tr><td>CsI(Tl)</td><td>S</td><td>50-53</td><td>4.5</td><td>1</td><td>104</td><td>0.16</td><td>0.12</td></tr><tr><td>Ge</td><td>SC</td><td>32</td><td>5.3</td><td>1</td><td>10²</td><td>0.015</td><td>0.004</td></tr><tr><td>CdTe</td><td>SC</td><td>48-52</td><td>6.1</td><td>10-3</td><td>1</td><td>0.016</td><td>0.010</td></tr><tr><td>HgI2</td><td>SC</td><td>53-80</td><td>6.4</td><td>10-3</td><td>10-1</td><td>0.1</td><td>0.04</td></tr></table>

It would have made perfect sense to place the following in previous sections, in particular, the one dealing with the physical principles of detection (see Sect. 7.3). This necessarily somewhat arbitrary choice reflects once again the extent to which the boundaries between wavelength regions, physical principles, and methods for making detectors are fuzzy and mutable, depending as they do on advances made in physics and technology.

# Scintillators (100 keV–10 MeV)

Photoelectric absorption or Compton scattering of $\mathrm { X }$ or $\gamma$ rays by the electrons in a solid transfers a large fraction of the incident photon energy to those electrons. This electron energy is progressively passed on to the atoms of the solid, either by excitation of electrons and molecules in bound states, or by excitation of acoustic vibrations (phonons) in the crystal lattice. These excited states decay radiatively, by emitting, in particular, visible and near UV photons. If the material is transparent at these wavelengths, it suffices to measure the intensity of the observed scintillation, in order to deduce the energy loss of the incident photon, and hence, within certain limits, its energy. A photomultiplier is used, with very low, or zero, intrinsic noise, high spectral sensitivity in the de-excitation wavelengths (blue), and very short time constant, which allows excellent time discrimination (around $1 0 ^ { - 3 }$ s, Problem 7.7).

Two classes of scintillators are inorganic and organic scintillators. In the first class, the material is an alkali halide, such as NaI, or CsI, doped with impurities, such as thallium. These produce interstitial centres in the crystal lattice, which are easily ionised and luminescent when recombination occurs. The conversion yield depends on the temperature: around $20 \%$ of the incident $\mathrm { X }$ or $\gamma$ -ray energy is converted into visible photons, a $1 0 0 \mathrm { k e V }$ photon producing something like 4 000 photons at around $4 2 0 \mathrm { n m }$ .

Many scintillators were developed following the use of NaI:T1 in 1948, mainly to meet the needs of nuclear medicine. Table 7.13 gives the characteristics of the most commonly used scintillators. Scintillators have no intrinsic directivity and must be combined with optics (for X rays), and collimators or masks (for $\gamma$ rays), if the aim is to form and detect an image (see Chap. 5).

Table 7.13 Properties of scintillators. BGO $\mathrm { B i } _ { 4 } \mathrm { G e } _ { 3 } \mathrm { O } _ { 1 } 2$ , GSO ${ \mathrm { G d } } _ { 2 } { \mathrm { S i O } } _ { 5 }$ , LSO $\mathrm { L u } _ { 2 } \mathrm { S i O } _ { 5 }$ , YAP $\mathrm { Y A l O } _ { 3 }$   

<table><tr><td>Crystals</td><td>NaI (T1)</td><td>CsI (Tl)</td><td>BGO</td><td>GSO</td><td>LSO</td><td>YAP</td></tr><tr><td>Density</td><td>3.67</td><td>4.5</td><td>7.1</td><td>6.7</td><td>7.4</td><td>5.5</td></tr><tr><td>Effective Z</td><td>51</td><td>54</td><td>75</td><td>59</td><td>66</td><td>33.5</td></tr><tr><td>Attenuation length at 500 keV [mm]</td><td>29.1</td><td>22</td><td>10.4</td><td>14.1</td><td>11.4</td><td>21.3</td></tr><tr><td>Number of scintillation photons for 100 keV</td><td>4100</td><td>1800</td><td>900</td><td>800</td><td>3000</td><td>1700</td></tr><tr><td>Response time (μs)</td><td>0.23</td><td>1</td><td>0.3</td><td>0.06</td><td>0.04</td><td>0.03</td></tr><tr><td>Hygroscopic</td><td>Yes</td><td>≈no</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Refractive index</td><td>1.85</td><td>1.79</td><td>2.15</td><td>1.85</td><td>1.82</td><td>1.95</td></tr></table>

# Anticoincidence Devices

The effects of charged particles can be limited, at least as regards their direct effects and spontaneous de-excitation emission, by equipping $\gamma$ ray telescopes with anticoincidence systems. The idea is to surround the main detector with another detector. If this is triggered, a ‘veto’ signal is generated, which prevents the main detector from being triggered in its turn, but for a very short lapse of time, although longer than the response time of the main detector and the anticoincidence detector. Used to limit the field of view of an experiment, this system has the advantage over the collimator of eliminating its own spontaneous de-excitation emission. In addition, it can improve the spectral response of spectrometers by eliminating a large proportion of Compton scattering events taking place in the main detector. However, this system has some disadvantages, too. For example, it increases the production of neutrons and the contribution from delayed de-excitation. Moreover, it limits the useful experiment time.

The anticoincidence device is probably the most delicate part in the design of a $\gamma$ ray experiment in astronomy, because it is essential, but at the same time highly complex. The design of such a system involves Monte Carlo simulations, as well as measurements in proton accelerators. Due to their fast response and simple implementation, scintillators are usually chosen to make anticoincidence detectors. Those designed to reject charged particles use a plastic scintillator. Those that must also stop $\gamma$ rays off the telescope axis use heavy scintillators like CsI or BGO (see Table 7.13), which have photon detection efficiencies as high as $100 \%$ up to energies of several hundred keV.

Phoswich Detectors

A phoswich detector is a sandwich of two scintillators, which are chosen so that their characteristic times are very different (see Table 7.13). Light emitted by the two detectors is collected by a photomultiplier (or a photodiode), and a selection made on the basis of the pulse shape discrimination (PSD) signal. This selection distinguishes those events having interacted in both scintillators (charged particles or Compton interactions) from those which have interacted only in the upper scintillator. The phoswich detector is equivalent to a detector–anticoincidence ensemble. This requires more complicated electronics, but the readout system for the upper scintillator is no longer needed. The significant reduction in mass within the anticoincidence device implies a large decrease in detector background, which, in the $\gamma$ ray region, is predominantly due to de-excitation of the surrounding matter. NaI–CsI sandwiches are often used, as they give good spectral results and effective selection of events.

# Semiconductor Detectors (10 keV–10 MeV)

In this energy domain, semiconductor detectors are no longer used for photoconduction (measurement of a direct current as in Sect. 7.4), but rather as spectrometers, that is, measuring the energy deposits induced by the interaction of photons with the matter (see Sect. 7.3.1). The electrons produced by these interactions generally have a much higher energy than the energy levels of atoms in the detector. They lose this energy very quickly while propagating, by ionising atoms on their path, thereby creating electron–hole pairs or charge carriers which themselves propagate, following the electric field lines. This drift under the effect of the electric field, until they reach the collecting electrodes (Fig. 7.56), constitutes the current charging up the capacitor. The collected signal $Q$ (the charge) is then the product of the elementary charge and the sum over the electrons and holes of the path elements, relative to the interelectrode distance $x _ { i } / d$ (Ramo’s theorem):

![](images/06fa66ad25a9e324770a5191de48cca0cfdd9d79b592d94e0905fe0a8075f845.jpg)  
Fig. 7.56 PIN diode. The base material is $p$ -doped silicon (or germanium). Supplementary doping with lithium compensates for the $p$ -doping in the volume, making the silicon intrinsic by compensation. The surface layer has an excess of lithium $( n )$ . The pair created by the $\mathrm { X }$ -ray photon moves in the applied electric field

$$
Q = { \frac { e } { d } } \sum x _ { i } \ .
$$

Charge Losses

In general, this migration involves charge losses, since each electron and hole has a certain probability of capture per unit time, characterised by its mean lifetime ( $\cdot \mathrm { \Delta } \tau _ { \mathrm { e } }$ and $\tau _ { \mathrm { h } }$ , respectively). If the transit time of a type of charge carrier is not negligible compared with the lifetime of these carriers, part of the signal will be lost, and this is referred to as charge loss. The transit time of carriers depends on their distance from the collecting electrode, the applied electric field $E$ , and also on their mobility, which is a characteristic of the semiconductor ( $\mu _ { \mathrm { e } }$ and $\mu _ { \mathrm { h } }$ , respectively, for electrons and holes). Charge losses therefore depend on the mean free paths of the carriers, $\lambda _ { \mathrm { e } } = \mu _ { \mathrm { e } } E \tau _ { \mathrm { e } }$ and $\lambda _ { \mathrm { h } } = \mu _ { \mathrm { h } } E \tau _ { \mathrm { h } }$ . For $n$ electron–hole pairs, produced at distance $x$ D Dfrom the negative electrode, the charge collected is given by Hecht’s equation (see Problem 7.13)

$$
Q = { \frac { n e } { d } } \left\{ \lambda _ { \mathrm { e } } \left[ 1 - \exp \left( - { \frac { d - x } { \lambda _ { \mathrm { e } } } } \right) \right] + \lambda _ { \mathrm { h } } \left[ 1 - \exp \left( - { \frac { x } { \lambda _ { \mathrm { h } } } } \right) \right] \right\} \ .
$$

The number of electron–hole pairs created in semiconductors is well above the number of photoelectrons created in scintillators, which explains their superior spectral resolution (Fig. 7.57).

It is therefore possible to minimise the charge loss in a given detector by increasing the electric field, that is, by increasing the voltage across the detector. In practice, too high a voltage generates a lot of noise, which can then decrease the resolution of the detector. If all interactions of the photons were to take place at the same distance from the collecting electrode, the charge loss would always be the same, and, as the loss of gain could be corrected for, its only effect would be a reduction in spectral resolution.

In reality, the interactions occur at a range of distances from the electrode, and a continuous range of losses is observed. These losses are manifested by the appearance of a continuum in the amplitude spectrum of pulses produced by a radioactive source (Fig. 7.58). They therefore amount to an energy loss, analogous to the one observed when Compton scattering occurs. However, when the charge loss is high, this means that the carriers must have travelled over a longer period, and if it is possible to accurately observe the pulse shape, it will be found that the growth time is much longer. A measurement of the pulse growth time can therefore lead to a correction for charge loss, and this correction allows for a symmetrisation of the observed lines (Fig. 7.58). However, charge loss always results in line broadening, which means a loss of resolution.

Table 7.14 gives some characteristics of semiconductors susceptible to charge loss effects.

![](images/97b812e06d49f2bdd41905fe8e8687bf3da65e0168c51c77039b9b8237c877b0.jpg)  
Fig. 7.57 Spectral resolution of detectors. (a) Thallium-doped NaI scintillator. (b) Ge–Li semiconductor detector. Ordinates are in units of $5 \times 1 0 ^ { - 4 }$ counts per second

Fano Factor

If all the energy deposited in a semiconductor were converted into electron– hole pairs, the number of these produced would depend only on the total energy deposited. On the other hand, if the energy was distributed in a completely uncorrelated way between electron–hole pairs and phonons, the number of electron– hole pairs would obey Poisson statistics, and its variance would be equal to its average value. In fact, it is found that the variance of this number is always less than the average value. The ratio of the variance and the average is called the Fano factor. This factor is of order 0.1 for most semiconductors.

# Germanium

Cooled germanium offers by far the best spectral resolution. Charge losses are low, but can nevertheless be corrected for, so improving the resolution even further. The feasibility of obtaining large volume crystals undoubtedly makes it the best possible choice for a laboratory spectrometer. In contrast, the need to cool it down to $7 7 ~ \mathrm { K }$ considerably limits its feasibility for a space spectrometer. In addition, it is relatively sensitive to irradiation by charged particles, its spectral resolution degrading at a rate of $50 \%$ per year. However, the example of the INTEGRAL spectrometer24 shows that the semiconductor can be periodically annealed in orbit to repair radiation damage and recover spectral performance levels. Annealing involves heating the detector to $3 0 0 \mathrm { ~ K ~ }$ for several days, then cooling it back down to its operating temperature of $7 7 ~ \mathrm { \ K }$ . This procedure removes most of the traps created by the passage of protons. As far as imaging is concerned, the crystal can be divided into several pixels, of about one centimetre in size, by depositing conducting bands on opposite faces of it. This gives a spectral resolution of centimetre order, although limited at high energies by Compton scattering in this material, which has a very high atomic number $Z = 3 2$ ).

![](images/d77454683ef0e46af58e70fdf38c1393c35b30623b0570eda3121a04e48b7a54.jpg)  
Fig. 7.58 Correction for the phenomenon of charge loss in the material CdTe. The count per energy channel is given as a function of energy, for laboratory radioactive sources $^ { 5 7 } \mathrm { C o }$ and $^ { 1 3 3 } \mathrm { { B } a }$ ). This spectrum, obtained in 1995, is amplified beyond $1 6 0 \mathrm { k e V . }$ Dotted curve: amplitude spectrum of pulses. Continuous curve: spectrum corrected for charge loss

Table 7.14 Semiconductor characteristics   

<table><tr><td></td><td>Si (300 K)</td><td>Ge (77K)</td><td>CdTe (300 K)</td><td>HgI2 (300 K)</td></tr><tr><td>Band gap width [eV]</td><td>1.12</td><td>0.74</td><td>1.45</td><td>2.1</td></tr><tr><td>Pair creation energy [eV]</td><td>3.61</td><td>2.96</td><td>4.43</td><td>4.22</td></tr><tr><td>μe[cm² V-1 s-1]</td><td>1300</td><td>36 000</td><td>1100</td><td>100</td></tr><tr><td>μh [cm² V-1 s-1]</td><td>500</td><td>42 000</td><td>80</td><td>4</td></tr><tr><td>Te[μs]</td><td>3000</td><td>1000</td><td>1</td><td>1</td></tr><tr><td>Th [μs]</td><td>3000</td><td>1000</td><td>1</td><td>1</td></tr><tr><td>Emax[V cm-1]</td><td>1000</td><td>100</td><td>1000</td><td>10000</td></tr></table>

# Cadmium Telluride

This material exhibits significant charge loss, due essentially to low hole mobility. These losses can be corrected for by measuring the rise time of the pulses or the ratio of the signals on each electrode, but these measurements are difficult to make and somewhat inaccurate. A more effective method is to segment the anode into small pixels in such a way that the signal induced by the holes becomes negligible while that induced by the electrons depends only weakly on the interaction depth. With this configuration and thanks to progress in microelectronics and hybridisation, its spectral performance at the time of writing (2007) is close to what can be achieved with germanium (see Fig. 7.59), but with the considerable advantage that it can work at room temperature, i.e., $2 0 ^ { \circ } \mathrm { C }$ . However, it does perform significantly better at lower temperatures, in the range $- 4 0$ to $0 ^ { \circ } \mathrm { C }$ . On the other hand, the resulting detectors remain relatively small and limit the application of this semiconductor to energies below $\mathbf { M e V } .$ .

![](images/ebcfcb4db53b26a4020840415f1921b6aa528fa16af91f645e78e022e57091ae.jpg)  
Fig. 7.59 Amplitude spectrum obtained in 2007 by summing the response of pixels in an $8 \times 8$ format CdTe Schottky array, illuminated by a radioactive source $( ^ { 2 4 1 } \mathrm { A m } )$ . Pixel size $1 \mathrm { m m } ^ { 2 }$ . Crystal thickness $2 ~ \mathrm { m m }$ . The array is hybridised on a substrate connected to ASIC readout components (IDEF-X). Credit: O. Limousin, CEA/DAPNIA/SAP

In orbit, irradiation by protons in cosmic rays and solar flares slightly degrades the electron transport properties. For the INTEGRAL Soft Gamma Ray Imager (ISGRI), carried on board the European INTEGRAL mission, a $3 \%$ loss of gain per year has been observed. In contrast to germanium, it is not therefore necessary to anneal CdTe detectors.

CdTe is now produced on an industrial scale, usually being obtained by zone refining. Crystals produced by this method exhibit limited resistivity of the order of $1 0 ^ { 9 } ~ \Omega \mathrm { { c m } }$ , which precludes the possibility of applying the high voltages required to minimise charge loss, since the leakage current, which generates noise, becomes too large. But a new method has been available since the mid-1990s, where growth occurs under high pressure ${ \mathrm { 1 0 0 ~ a t m ) } }$ , including $20 \%$ zinc. This gives larger and more resistant crystals, which can be used in higher fields (up to $1 0 0 0 0 \mathrm { V ~ c m ^ { - 1 } }$ ). CdTe crystals produced by zone refining can be equipped with an indium electrode to create a Schottky barrier (see Sect. 7.5.2). These diodes exhibit extremely low leakage currents, whence it is possible to apply very high fields. Charge loss is then minimised (see Fig. 7.59).

As regards imaging, the small size of these detectors is not a disadvantage, and CdTe seems to be a good choice for the construction of a segmented imager, operating up to a few hundred keV.

Mercury Iodide

Roughly speaking, the same advantages and disadvantages as CdTe are present in mercury iodide $\mathrm { ( H g I } _ { 2 } )$ , but it is more difficult to produce. It is highly resistant to irradiation. The thickness of present detectors does not exceed one millimetre, and this limits use to energies below $1 0 0 \mathrm { k e V } ,$ despite its having a better intrinsic stopping power due to the properties of the mercury atoms. Moreover, the deposition process of the electrodes is rather delicate, and rules out industrial production for the present (2007). Despite these drawbacks, mercury iodide has been used in X-ray astronomy. Trials carried by stratospheric balloons have shown the advantage of using a high $Z$ detector. Indeed, for the same stopping power, there is around five times less noise than with a germanium or scintillation detector, working been 40 and $8 0 \mathrm { k e V } .$

# 7.7 Neutrino Observing Systems

In Chap. 1 we described how neutrinos have recently joined the panoply of information carriers exploited by astrophysics, alongside electromagnetic radiation.25 Even more so than for $\gamma$ radiation, it is no longer possible to separate the notions of telescope, spectrometer, and detector. In this section, we shall thus discuss all these functions together. We shall consider neutrinos with energies from $1 0 0 \mathrm { k e V }$ (solar neutrinos) up to neutrinos from supernovas $\mathrm { \Phi } ( \sim 1 0 ~ \mathrm { M e V }$ ) or active galactic nuclei (TeV and beyond).

# 7.7.1 Radiochemical Detection of Solar Neutrinos

Historically, the first encounter between neutrinos and astrophysics occurred when John Bahcall26 contacted Raymond Davis to enquire about the means available for detecting solar neutrinos. The basic idea of these radiochemical techniques is the so-called inverse $\beta$ reaction, which leads to the transmutation of a target nucleus $( A , Z )$ to a generally unstable nucleus $( A , Z { + } 1 )$ :

$$
\nu _ { \mathrm { e } } + { } ^ { A } X _ { Z } \longrightarrow { \mathrm e } ^ { - } + { } ^ { A } X _ { Z + 1 } \ .
$$

The great advantage with this detection method is that it is virtually insensitive to undesirable effects. Several targets have been successfully used here, such as chlorine and gallium. The following conditions must be satisfied for a target nucleus to be viable:

1. A threshold for the transmutation reaction that is compatible with the neutrinos   
one hopes to detect.   
2. A sufficiently high probability of inducing this reaction.   
3. A sufficient isotopic abundance of the target nucleus.   
4. The resulting nucleus must produce an exploitable signature.

# Detection Using Chlorine

In the mid-1960s, Raymond Davis constructed the first experiment for detecting solar neutrinos. He used the inverse $\beta$ “ reaction proposed by Pontecorvo27 in 1946:

$$
\mathrm { v _ { e } } + { } ^ { 3 7 } \mathrm { C l } \longrightarrow \mathrm { e } ^ { - } + { } ^ { 3 7 } \mathrm { A r } .
$$

Five or six times a year, the isotope $^ { 3 7 } \mathrm { A r }$ is extracted by flushing the system with helium. This radioactive isotope of argon (Ar) decays with a half-life of 35 days, emitting characteristic radiation. The cross-section of the transmutation reaction is very small, and the reaction only occurs when the neutrino energy is greater than $8 1 4 { \mathrm { ~ k e V } } .$ Davis put 615 tonnes of carbon tetrachloride $\mathrm { C } _ { 2 } \mathrm { C l } _ { 4 }$ at the bottom of a gold mine in South Dakota (USA). Applied to the Sun, the theories of nuclear physics predict that a certain number of neutrinos should be emitted per unit time. Then, given the mass of the detector and the reaction cross-section, one $^ { 3 7 } \mathrm { A r }$ atom was expected to be produced every day. However, the experiment produced only one such atom every three days. This significant difference was the basis of the solar neutrino enigma, only solved in 2002, and today attributed to the property of neutrino oscillation between different neutrino species. Raymond Davis received the Nobel Prize for Physics for this result in 2002.

# Detection Using Gallium

The idea of using a gallium target to detect solar neutrinos is due to Kuz’min, who suggested the transmutation of the gallium isotope $^ { 7 1 } \mathrm { G a }$ into the radioactive isotope $^ { 7 1 } \mathrm { G e }$ of germanium by the reaction

$$
\mathrm { v _ { e } } + \mathrm { ^ { 7 1 } G a } \longrightarrow \mathrm { e ^ { - } } + \mathrm { ^ { 7 1 } G e } .
$$

The advantage compared with the experiment using $^ { 3 7 } \mathrm { C l }$ is that, thanks to the lower threshold of $2 3 3 \mathrm { k e V } ,$ $^ { 7 1 } \mathrm { G a }$ can be used to detect so-called primordial neutrinos, not emitted by the Sun. The GALLEX detector (1991–1997), later called the Gallium Neutrino Observatory (GNO), was set up in the underground Gran Sasso laboratory, in the Abruzzo region of central Italy, with 30 tonnes of gallium. The Soviet– American Gallium Experiment (SAGE) set up in the Baksan laboratory in the Russian Caucasus in the 1990s operates on the same principle.

The isotope $^ { 7 1 } \mathrm { G e }$ decays with a half-life of 11.4 days. After exposing the gallium to solar neutrinos for several weeks, the germanium atoms that have been produced must be recovered, and their decay observed. Given the mass of gallium used and the theoretical prediction for solar production, the expected rate of production by solar neutrinos is a little over one germanium atom per day.

The gallium is in the form of a liquid compound, gallium trichloride in solution in hydrochloric acid, in a large cylindrical tank $8 \textrm { m }$ high and $4 \textrm { m }$ in diameter. The germanium produced is then in the form of germanium tetrachloride, which is extremely volatile in the presence of hydrochloric acid. Every three or four weeks, several thousand cubic metres of nitrogen is passed through the tank to flush out the germanium tetrachloride. A trap is placed at the tank outlet, comprising a glass column containing tiny glass threads, designed to capture the germanium tetrachloride. Pure water is passed through from top to bottom while the gas flow goes from bottom to top. The water dissolves the germanium tetrachloride and allows the nitrogen to escape.

The next step is to form germanium hydride $\mathrm { G e H _ { 4 } }$ . This gas, very similar to methane, is placed in a small proportional counter. In order not to swamp the tenuous signal of the $^ { 7 1 } \mathrm { G e }$ under a signal due to tritium decay, this chemical reaction is carried out with water taken from 3 000 metres underground in the Negev desert, which contains no tritium atoms. The decay of the germanium by electron capture is observed in the proportional counter. This yields a characteristic electrical signal. Each counter is left for several months in its lead shielding (dating from ancient Rome), itself placed in a Faraday cage where undesirable radiation is reduced to a minimum. The counters are made from quartz, sculpted and worked by hand and selected to produce the least possible unwanted noise.

# Detection Using Heavy Water

The Sudbury Neutrino Observatory (SNO) is a detector operating in real time, comprising $1 0 0 0$ tonnes of heavy water ${ \bf D } _ { 2 } { \bf O }$ , placed in a nickel mine in Canada, some $2 0 0 0 \mathrm { ~ m ~ }$ underground. The detection of electron neutrinos exploits the following reactions:

$$
\begin{array} { r } { \mathrm { v _ { e } } + \mathrm { ^ { 2 } H } \longrightarrow { \mathrm { e ^ { - } } } + \mathrm { p } + \mathrm { p } , } \\ { \mathrm { v _ { e } } + { \mathrm { e ^ { - } } } \longrightarrow \mathrm { v _ { e } } + { \mathrm { e ^ { - } } } . } \end{array}
$$

In the first reaction, the electron energy provides a direct determination of the neutrino energy, but with rather limited information about the direction of the incident neutrino. In the second, which is elastic scattering, information about the neutrino energy is limited, while more can be found out about the direction of the incident neutrino. But for the first time, this experiment can explicitly measure the flux of other neutrino flavours, via the decay of the deuteron induced by the neutrino, to produce a neutron and a proton:

$$
v _ { x } + { } ^ { 2 } \mathrm { H } \longrightarrow v _ { x } + { \mathrm { p } } + { \mathrm { n } } , \qquad x = { \mathrm { e } } , \| , { \mathrm { \ u ~ } } { \mathrm { \ u ~ } } .
$$

Thanks to the complementarity of these reactions, the SNO experiment has made a major contribution to solving the solar neutrino problem, showing that all the neutrinos from the Sun which seemed to be missing were transformed during their trip into neutrinos of another flavour by the oscillation phenomenon.

The detector comprises a sphere of acrylic material of diameter $1 2 \mathrm { m }$ , containing 1 000 tonnes of ultrapure heavy water, itself immersed in a tank of diameter $2 2 \textrm { m }$ and height $3 4 \mathrm { ~ m ~ }$ containing very pure ordinary water, the whole thing subjected to the permanent scrutiny of $9 6 0 0$ photomultipliers. The radioactive purity requirements are very strict indeed.

To detect the neutrons that are the signature of the third reaction, two tonnes of highly purified sodium chloride have to be dissolved in the heavy water, while maintaining the same level of purity. But it has to be possible to extract all the dissolved salt in a few days to restore the initial purity of the heavy water, in order to proceed with another neutron detection method using $^ 3 \mathrm { H e }$ proportional counters immersed in the water.

# The Prospects for Neutrino Detection Using Indium

Indium was proposed as neutrino target by the physicist Raju Raghavan in 1968. The inverse $\beta$ reaction used here results in an excited state of the final nucleus, with a mean lifetime of $4 . 7 ~ \mu \mathrm { s }$ , decaying with the emission of two photons:

$$
\begin{array} { r } { \mathfrak { v } _ { \mathrm { e } } + { } ^ { 1 1 5 } \mathrm { I n } \longrightarrow \mathrm { e } ^ { - } + { } ^ { 1 1 5 } \mathrm { S n } ^ { * * } \ , } \end{array}
$$

followed by

$$
{ } ^ { 1 1 5 } \mathrm { S n } ^ { * * } \longrightarrow { } ^ { 1 1 5 } \mathrm { S n } + \gamma _ { 1 } \left( 1 1 6 \mathrm { k e V } \right) + \gamma _ { 2 } \left( 4 9 6 \mathrm { k e V } \right) .
$$

What is interesting here is to obtain a direct detection, with a threshold of $1 1 7 \mathrm { k e V }$ which makes it possible to detect primordial neutrinos, determining their energies individually by measuring the energy of the resulting electrons, and hopefully improving discrimination thanks to the different spatial coincidences $( \mathrm { e } ^ { - } , \gamma _ { 1 } )$ , temporal coincidences $( \gamma _ { 1 } , \gamma _ { 2 } )$ , and the characteristic energies of the photons.

Despite ingenious experimental ideas, the problem shared by all these detectors remains the lack of selectivity of the final radiation, which makes it difficult to deal efficiently with intrinsic background noise (the natural radioactivity of indium) or external noise sources. In 2011, this approach has been more or less abandoned, particularly since the initial motivation of explaining the mystery of solar neutrinos has since been removed.

# 7.7.2 Neutrino Detection by Cherenkov Radiation

To detect the particles resulting from the interactions of incident neutrinos, the Super-Kamiokande detector and similar detection systems use Cherenkov radiation, already encountered earlier in the context of detection via the Earth atmosphere. Charged particles, and only charged particles, moving through water at speeds $7 5 \%$ greater than the speed of light in water will radiate blue light in a conical configuration around the direction of their trajectory. This so-called Cherenkov light will cross the pure water of the reservoir without absorption, and can then be detected on its inner wall, lined with photomultiplier tubes operating in counting mode.

Each photomultiplier measures the total amount of light reaching it, and the time of arrival of each photon. These measurements are used to reconstruct the trajectory and energy of the particles crossing the water. The Cherenkov light cone produces a more or less regular ring of light on the walls. If this ring appears distinctly, the particle was a muon, but if the edges of the ring are fuzzy, the particle was an electron whose multiple scattering has modified the direction. This latter feature is used to distinguish between muon neutrino and electron neutrino interactions.

This technique has been successfully used for neutrinos with energies of a few MeV (Super-Kamiokande), but also for high energy neutrinos (AMANDA, ANTARES, etc.).

Since 1987, the Kamioka Nucleon Decay Experiment (Kamiokande), and since May 1996, Super-Kamiokande, developed by Masatoshi Koshiba,28 have been measuring the upper region of the solar neutrino spectrum with a Cherenkov detector using water. The Super-Kamiokande experiment comprises $5 0 0 0 0 \mathrm { m } ^ { 3 }$ of pure water, monitored by 11 000 photomultiplier tubes (PMT). The neutrinos are scattered by electrons in the target $\mathrm { ( v _ { e } + e ^ { - }  v _ { e } + e ^ { - } ) }$ and transmit a large C ! Cpart of their energy to them. The Cherenkov radiation produced by the scattered electron provides information about the energy and direction of the incident neutrino. The rate of production of photons by solar neutrinos is around 10 per day. The energy threshold of Super-Kamiokande is around $5 . 5 \mathrm { M e V } .$ . Below this threshold, the Cherenkov light is too faint to exceed the background signal, produced by undesirable phenomena. Super-Kamiokande can measure the energies of neutrinos and also the direction from which they arrive. These detectors have confirmed the solar origin of the observed neutrinos, and also detected neutrinos produced by the supernova SN 1987A.

# Neutrinos from the Supernova SN 1987A

This type of water Cherenkov detector, e.g., Kamiokande and IMB in the USA, recorded neutrinos produced in the supernova SN 1987A, using the same idea of Cherenkov emission, on 23 February 1987. Experimentally, this is easier than detecting solar neutrinos, owing to the generally higher energy $ { \widetilde { \mathbf { \Lambda } } } \approx 2 0  { \mathrm { M e V } }$ ) and the narrow time window $\approx 1 2 \ : \mathrm { s }$ ) in which the 20 detected events were concentrated.

# 7.7.3 High Energy Neutrino Astronomy

Since the 1990s, enormous detectors have been built to make neutrino telescopes for neutrinos reaching energies of several TeV. Indeed, very high energy $\gamma$ rays $( \geq 1 0 ^ { 1 2 } { \mathrm { e V } } )$ have been detected from active galactic nuclei and the Crab nebula. The underlying mechanisms in these compact sources simultaneously produce neutrinos which can escape and cross intergalactic space without deviating from their initial trajectory.

Detection of these high energy but rare neutrinos uses the Earth both to filter unwanted radiation and as a target to convert the neutrinos into muons travelling in the same direction as their progenitors. These upwardly moving muons travel hundreds of metres, and in water, emit electromagnetic radiation by the Cherenkov effect. This radiation can in turn be measured by optical detectors (called optical modules) distributed along detection strings several hundred metres long. The first attempt to build a high-energy neutrino telescope goes back to the end of the 1980s with the Deep Underwater Muon and Neutrino Detector (DUMAND), just off the coast of Hawaii. A prototype string attached by cable to a vessel at the surface was deployed in 1987. Following this success, a project was put forward to build a network of 9 strings, anchored to the seabed at a depth of $4 8 0 0 \mathrm { ~ m ~ }$ . Although only the first detection string was set up, it was able to detect the signatures of atmospheric muons. However, it had only been operating for 10 hours when a leak occurred in one of the electrical units. The experiment was eventually stopped in 1996 due to lack of funds. In the meantime, other projects had been set up, some persevering with the idea of using a liquid medium (the sea or a lake), others preferring ice. Today, the telescope known as IceCube, set up under the Antarctic ice and hence sensitive to sources in the northern hemisphere, and the ANTARES telescope, operating from $2 5 0 0 \mathrm { m }$ under the Mediterranean sea, just off the French coast at Toulon, form a complementary pair that can observe the whole sky.

# Southern Hemisphere

# AMANDA

The Antarctic Muon and Neutrino Detector Array (AMANDA) was started in the 1990s, under the Antarctic ice at the geographical South Pole. It comprises a network of 676 optical modules, distributed over twenty detection strings. These were deployed by drilling a vertical holes in the ice by means of high pressure hot water jets, setting up the detection strings, then letting the water freeze them rapidly into place. Apart from the relative ease of deployment, ice has the advantage of inducing a low optical background noise, of the order of $1 \mathrm { k H z }$ per optical module, making it possible to detect very low energy neutrinos (tens of $\mathrm { M e V } _ { \it \cdot }$ ) as might be emitted by supernova explosions. However, the ice layer traps air bubbles and these induce light scattering that makes it difficult to reconstruct the particle trajectories. The angular resolution is thus only a few degrees, so it is a delicate matter to study point sources (see Fig. 7.60). By increasing the size of the detector, and hence the data available for reconstructing trajectories, it should be possible to improve the angular resolution. This explains how AMANDA’s successor IceCube can achieve angular accuracies better than one degree.

After 7 years of data acquisition, the AMANDA telescope accumulated a total of 6 595 candidate neutrinos (compatible with the expected background), and thereby measured the energy spectrum of atmospheric neutrinos down to two orders of magnitude below previous investigations carried out in underground detectors, i.e., down to about $1 0 0 \mathrm { T e V . }$ Regarding the high energy diffuse cosmic neutrino flux, an upper limit was established by studying the selected batch of neutrinos, and on this basis it was possible to reject a certain number of production models, e.g., by active galactic nuclei (see Figs. 7.60 and 7.62).

![](images/3c1f7c5b6365f25ea7e429c8cd49ea6a020685da0ae9fad1bbf2e2c097c1faef.jpg)  
Fig. 7.60 Sky map of the northern hemisphere showing the results of observations made by AMANDA since 2000. The grey scale at the bottom, in units of $1 0 ^ { - 8 } \mathrm { ~ c m } ^ { - 2 } \mathrm { ~ s } ^ { - 1 }$ , gives the upper limits of the high energy neutrino flux, above $1 0 \ \mathrm { G e V } ,$ , with a spectrum assumed to go as $E ^ { - 2 }$ , measured from muon events over a total of 607 days. No correlation has yet been observed with potential high energy neutrino sources such as quasars or supernovas. With the kind permission of the IceCube collaboration

![](images/47b7fc18e7d46e675090e8164b4beed32de33bc855d18602eb0e8ba2102cf547.jpg)  
Fig. 7.61 Left: Photograph of a detection string in the assembly room, folded up on a pallet, just prior to immersion. Right: Photograph of one storey of a detector string, showing the photodetectors inside their protective spheres. The associated electronics is housed in a central titanium container

![](images/248331e43d9b024dc4d6e2e9f7ce7fa6f1e5829d5ed96c9777063ceca77ebbe5.jpg)  
Fig. 7.62 Upper bounds on a diffuse flux of high energy cosmic neutrinos, compared with theoretical predictions (W&B and MPR). The most restrictive bound yet published comes from ANTARES, but the sensitivity expected from analysis of recent data gathered by IceCube will exceed it by almost an order of magnitude

IceCube Neutrino Observatory

The IceCube detector has taken over from its predecessor AMANDA. It is the largest neutrino telescope in the world. Most of the results obtained after the 7 years of data acquisition by AMANDA have already been superseded by data from the first few detector strings of IceCube. Each string carries 60 optical modules frozen into the ice at a depth of $1 5 0 0 { - } 2 5 0 0 \ \mathrm { m }$ . The first string was set up in January 2005, and the detector has had its full complement of 86 strings since January 2011. At the surface is the IceTop detector, which serves to calibrate IceCube and also to study the composition of cosmic radiation above $1 0 ^ { 1 7 }$ eV. It comprises tanks for detecting Cherenkov light emitted by charged particles reaching ground level. When data was taken with the 40 string detector, a total of 14 139 candidate upwardly moving neutrinos were selected over 375.5 days. A search for point sources was then carried out, but no significant accumulation was observed. The limits obtained with this batch of data are now tighter by a factor of 7 than those laid down by AMANDA, and they should be improved in the near future through analysis of data from the final configuration.

# Northern Hemisphere

Baikal

Located in Lake Baikal in Siberia, this neutrino telescope was the first to go into operation. Deployment and maintenance of the sensor strings are carried out in the winter in order to take advantage of the thick ice on the lake. After several research and development stages, beginning in 1980, followed by construction, beginning in 1990, the Baikal telescope now runs with 192 photomultipliers distributed over 8 strings. The modest size of the detector and the poor transparency of the water in the lake limit sensitivity to cosmic neutrinos. An extension of the detector has nevertheless been planned to increase sensitivity to the highest energies. This will involve deploying 3 further strings, each $1 4 0 \mathrm { m }$ long and carrying 36 optical modules, with operations beginning in April 2005. This new configuration should provide a fourfold increase in sensitivity over results already published, and it may itself constitute the first step toward the construction of a detector on the kilometre scale.

# NESTOR

The Neutrino Extended Submarine Telescope with Oceanographic Research (NESTOR) project was the first to have begun R & D studies in the Mediterannean sea, in 1989. The original aim was to deploy a set of towers, $4 1 0 \mathrm { m }$ high, to detect Cherenkov light, eventually forming a kilometre-sized detector made up of over 1 000 photodetectors, at a depth of almost $4 0 0 0 \mathrm { m }$ , just off the bay of Navarino, near Pylos in Greece. A first, reduced-size prototype storey, $5 \mathrm { m }$ in radius and equipped with 12 optical modules, was set up temporarily in March 2003. Several events were then recorded which triggered 4 of the 12 optical modules in coincidence. A reconstruction algorithm was used to extract the zenithal angular dependence of atmospheric muons, and also to measure the muon flux at a depth of about $4 0 0 0 \mathrm { m }$ . The Nestor team are now concentrating their activities within the $\mathrm { K m } 3 \mathrm { N e T }$ consortium, which aims to deploy a kilometre-sized neutrino telescope in the Mediterranean.

# NEMO

The NEMO collaboration, created in 1999, originally planned to build a neutrino telescope with kilometre dimensions in the Mediterranean sea at a site about $8 0 ~ \mathrm { k m }$ off the coast of Capo Passero in Sicily, at a depth of about $3 5 0 0 \mathrm { ~ m ~ }$ . This site seems to ensure a low concentration of bioluminescent bacteria, which are a source of background noise for the detector. The design is based on semi-rigid towers. The underlying idea is that these towers will require a smaller number of in situ connections than the detector strings used elsewhere. A mini prototype tower comprising 4 storeys was deployed at a depth of $2 0 0 0 \mathrm { m }$ , only $2 5 ~ \mathrm { k m }$ away from Catania, and operated between 18 December 2006 and 18 May 2007, leading to about 200 hours of data acquisition. Tracks of atmospheric muons were thereby reconstructed and their angular distribution compared with simulations, revealing a good agreement with predictions. The project has now entered a new phase, integrated into the common programme of the $\mathrm { K m } 3 \mathrm { N e T }$ consortium. In July 2007, an electro-optical cable $1 0 0 \mathrm { k m }$ long was laid between the Capo Passero site and a completely new coastal station in the port of Portopalo.

# ANTARES

The ANTARES project, begun in 1996, is the most advanced Mediterranean project. The site chosen for the telescope is in the Porquerolles trench, about $4 0 \mathrm { k m }$ off the coast of Toulon (France). The water is pure with limited scattering of Cherenkov light, so it is possible to achieve good accuracy in measuring the direction of the muon, and hence also the neutrino $( < 0 . 5 ^ { \circ }$ at $1 0 \mathrm { T e V } _ { \cdot }$ ). The $2 4 7 5 \mathrm { m }$ of water above the detector ensure partial shielding against atmospheric muons. The telescope comprises 12 independent detection strings, some 60 to $7 5 ~ \mathrm { m }$ apart, distances comparable with the absorption length of Cherenkov light. This distance also satisfies constraints imposed by safety and maintenance. In particular, a submarine must be able to move between the detector strings to ensure connection to the main junction box. The latter controls the electricity supply to the detectors and centralises the optical fibres coming from the various strings before data is sent to the land station by means of an electro-optical cable. The junction box contains an optical distributor to connect the clock to each string through a signal sent from the coastal station.

Each string is made up of 5 identical sectors, each comprising 5 storeys with a vertical spacing of $1 4 . 5 \mathrm { m }$ (see Figs. 7.61 and 7.63). Each storey in turn holds three optical modules linked to the control module for that storey. As well as ensuring voltage distribution and signal transmission, this module is equipped with a compass and a tiltmeter to determine the orientation of the storey. Each string is anchored to the seabed, while its upper end is attached to a buoy which moves around according to the sea currents, together with the all the optical modules. The position and orientation of each optical module must be continuously monitored. The tiltmeters measure the inclination of a storey with respect to the horizontal plane, while the compass measures the components of the Earth’s magnetic field in three directions. Each string also carries five acoustic detectors (hydrophones), spread out along its length. Moreover, the anchor holds an acoustic transponder. The hydrophones receive signals emitted by one of the three beacons arranged on the sea floor around the detector or by one of the emitters carried by the strings. By measuring the different travel times between acoustic emitters and receivers, the position of each hydrophone can be obtained by triangulation. The combination of acoustic data and information from the tiltmeters is used to fix the positions of the optical modules to an accuracy of $1 0 \mathrm { c m }$ . This level of accuracy is needed to guarantee the desired angular resolution.

The detector was gradually deployed over the period from March 2006, when the first detector string was immersed, to May 2008. Since then, ANTARES has been the largest neutrino telescope in the northern hemisphere, with unequalled sensitivity over a large region of the galactic plane and in particular toward its centre. The data already recorded have been analysed to search for cosmic neutrinos, among other things, in the form of an isotropic diffuse signal. This study has established an upper bound comparable with theoretical predictions (see Fig. 7.62). Further data is currently under analysis.

![](images/31c45a5070307a888b44aef6e4cc42801552085d366c7f49555d07c164ec0bbe.jpg)  
Fig. 7.63 Artist’s representation of the strings of light sensors making up the ANTARES detector in the Mediterranean sea. A total of 1 000 photomultipliers are distributed over the 12 strings, covering a horizontal area of $0 . 1 \mathrm { ~ k m } ^ { 2 }$ over a height of $3 5 0 ~ \mathrm { m }$ . Image courtesy of the ANTARES collaboration

Km3Net

The ANTARES, NEMO, and NESTOR groups have joined together to form a European consortium called $\mathrm { K m } 3 \mathrm { N e T } .$ , with a view to designing and determining the site for the next generation of cosmic neutrino telescope in the Mediterranean. The European Union will fund this operation in two stages. The first, called Design Study, began in February 2006 and was completed in 2009 with the publication of a Technical Design Report (TDR) detailing the proposed technical solutions. The fundamental requirements for such a detector are first of all an instrumented volume of more than one cubic kilometre and in addition an angular precision of the order of $0 . 1 ^ { \circ }$ around $1 0 \mathrm { T e V . }$ Furthermore, the detector must be sensitive to the three flavours of neutrino. The second stage, or Preparatory Phase (PP), began in March 2008. It focuses on strategic and financial issues but nevertheless includes prototyping activities. Construction of the detector should begin in 2013. The $\mathrm { K m } 3 \mathrm { N e T }$ project forms part of a broad cross-disciplinary field bringing together a wide range of scientific activities from oceanography, to seismology, geochemistry, and others. The site will be an entirely novel submarine observatory, accessible to a varied scientific community.

# 7.8 Gravitational Wave Detection

Gravitational waves were briefly presented in Chap. 1, in the context of astronomical information carriers.29 We defined the dimensionless quantity $h = \ S L / L$ , which Dcharacterises the amplitude of a gravitational wave and allows an assessment of detector capabilities. Detection involves measuring the relative displacement of two free masses (which means that non-gravitational forces can be neglected in the relevant temporal frequency band). Maximal sensitivity is achieved when the masses are separated by a distance equal to half a wavelength, and this property fixes the optimal scale for detection, although it is not necessarily attained, or even possible. Baselines of the order of a million kilometres would be required for the lower frequency waves (less than $1 \ \mathrm { H z }$ ), and a hundred kilometres for the higher frequency waves $( 1 0 \mathrm { k H z } )$ .

It is still not clear what to call such instruments. The terms gravitational wave telescope, gravitational antenna, or gravitational wave detector are all sometimes used.

# Mechanical Resonance Detectors

The aim here is to measure the deformation of a solid as the wave passes through it. This was the approach followed by Weber in the first attempt at detection (1969). The sensitivity was already quite remarkable $( h \sim 3 \times 1 0 ^ { - 1 6 }$ ), but much  too low for the predicted signals. A metal cylinder is insulated from terrestrial seismic perturbations by a high-pass mechanical filter. Excitation of the mechanical resonance of the cylinder produces a relative variation of its length (this being defined by the measurement itself as a mean value, which smooths out local atomic effects), measured by piezoelectric sensors. Various improvements, such as cooling the cylinder down to a temperature of a few kelvin, so as to reduce the effects of Brownian motion, have increased sensitivity by about two orders of magnitude in the $\mathrm { k H z }$ frequency domain, by using a $4 8 0 0 ~ \mathrm { k g }$ aluminium cylinder.30 This type of detector, of intrinsically narrow spectral range, will ultimately be limited by quantum uncertainty (square root of spectral density $\approx 1 . 5 \times 1 0 ^ { - 2 2 } \mathrm { H z } ^ { - 1 / 2 } )$ ,  assuming that the antenna can be cooled sufficiently to remove thermal noise.

# Interferometric Detectors

The aim is to build a detector, operating over a broad frequency band, and capable of reaching a spectral sensitivity

$$
\lesssim 3 \times 1 0 ^ { - 2 3 } \mathrm { H z } ^ { - 1 / 2 } \ .
$$

It can be shown31 that a Michelson interferometer, with arms of length $L > 1 \mathrm { k m }$ , illuminated by a $1 0 \ \mathrm { W }$ continuous-wave laser, would achieve this sensitivity in the frequency range between $5 0 \mathrm { H z }$ and several kHz (Fig. 7.64).

The great length of the arms pushes back the quantum uncertainty limit. The photon noise of a laser of wavelength $\lambda$ and power $P$ leads to a spectral uncertainty in the path length difference $x$ , viz.,

$$
\Delta x = \frac { \lambda } { \pi } \sqrt { \frac { h \nu } { 2 P } } \approx 1 0 ^ { - 1 6 } \mathrm { m H z } ^ { - 1 / 2 } \quad \mathrm { f o r } \ P = 1 \mathrm { W } , \ \lambda = 0 . 5 \mu \mathrm { m } \ .
$$

The required sensitivity would impose $P = 5 0 0 \mathrm { W }$ , which is quite unrealistic. The Dlight must therefore be ‘recycled’. This means reinjecting the light which leaves the interferometer, in order to increase the stored energy without increasing the equivalent length of the arms. The desired spectral sensitivity is then within reach (Fig. 7.65), provided that laser fluctuations in frequency $( \Delta \dot { \nu } / \nu < 1 0 ^ { - 1 7 } \mathrm { H z } ^ { - 1 / 2 } )$ , in power $( \Delta { \bf \bar { P } } / P < 1 0 ^ { - 6 } { \mathrm { H z } ^ { - 1 / 2 } } )$ ), and in angular spread $\mathrm { ( } \Delta \phi < 1 0 ^ { - 7 } \mathrm { r a d ) }$ , can be reduced.

In the mid-1990s, construction began on two interferometers of this type: LIGO in the USA, and VIRGO in Pisa, Italy. They have baselines around $3 \ \mathrm { k m }$ long.

![](images/1324a08531359fae9229f9d3cf4100ee526264ee9bab1c0df9eb9d56023da89a.jpg)  
Fig. 7.64 Interferometric detector of gravitational waves. The stabilised single frequency laser illuminates, via a separator $S$ , the two arms of the interferometer, and these are arranged so that the light passes several times, in order to increase sensitivity (the sensitivity is multiplied by $n$ for $n$ passes). Recycling light by mirrors $M _ { 5 }$ and $M _ { 6 }$ involves adjusting the interferometer to give destructive interference at the detector $D$ , and then adjusting the laser frequency and the mirrors $M _ { 1 }$ and $M _ { 2 }$ to minimise the signal at the auxiliary detector $d$ . The pairs of mirrors $M _ { 1 }$ , $M _ { 4 }$ and $M _ { 2 }$ , $M _ { 3 }$ are suspended and insulated from seismic vibrations, so that they behave like free masses. The passage of any gravitational wave, whose wave plane coincided with the arms of the interferometer, would cause a variation in the flux of light received at $D$ . (After Brillet A., Virgo project, private communication, 1985)

![](images/bb87bca09b548e99b4c8ca2d02e1656677b0a2614bcc43b22bb2a46ca33ec5f4.jpg)  
Fig. 7.65 Sensitivity limit imposed by photon noise, for an interferometer of length $L$ , illuminated by a laser of power $P = 1 0$ W. Optical loss factors are shown, in a reasonable range of values, Dgiven the present state of optical surface technology. The desired sensitivity requires recycling and low losses. (After Brillet A., Virgo project, private communication, 1985)

![](images/6412abd4eef38e90dfda20c59e240aa9bfd5c8e8569c56910c84cd18c11d62b8.jpg)  
Fig. 7.66 Sensitivity, expressed by the amplitude of the power spectrum of $h \ [ \mathrm { H z ^ { - 1 / 2 } } ]$ , as a function of the frequency $\nu$ [Hz] of the gravitational wave to be detected. The different noise sources and their amplitude in a VIRGO-type interferometer are indicated between 1 and $1 0 ^ { 4 } ~ \mathrm { H z }$ . The continuous curve gives the resultant, and hence, the best possible performance

Figure 7.66 shows the various noise sources affecting the ultimate sensitivity of an interferometer:

• Seismic noise, reduced by the anti-vibration suspension of the mirrors.   
• Thermal noise of this suspension, which manifests macroscopically the Brownian fluctuations in the position of their centre of gravity. Thermal noise of the mirrors, whose surface also contributes a position uncertainty, due to the thermal motions of its atoms, despite a certain degree of cooling. Photon noise, due to the finite power of the laser. Collision noise, due to residual atoms in the vacuum surrounding the mirrors and beams. The VIRGO and LIGO instruments32 are extremely difficult to realise in practice.   
Results are expected in the decade 2010–2020 and beyond.

The size of the Earth, and seismic effects, set limits which can only be surmounted by placing instruments in space. The baseline could then be increased, using two or three satellites, separated by distances of $1 0 ^ { 6 } ~ \mathrm { k m }$ or more. Low frequency gravitational waves would then become detectable $( \nu = 1 0 ^ { - 1 }$ to $1 0 ^ { - 4 } ~ \mathrm { H z } )$ , with spectral sensitivity up to $1 0 ^ { - 2 3 } \mathrm { H z } ^ { - 1 / 2 }$ D. The distance between satellites can be measured using laser beams, and the detection limit will very likely be set by perturbing accelerations, due to radiation pressure from solar photons, and impacts of solar wind protons and electrons.

![](images/01a9529fe558e2ff14728836b0b1cc349d0932af9a58f71d13fd286aea04b12d.jpg)  
Fig. 7.67 Orbits suggested for the proposed European mission LISA. The four satellites constituting the interferometer orbit in a plane at $6 0 ^ { \circ }$ to the ecliptic, and $2 0 ^ { \circ }$ behind the Earth

The Laser Interferometer Space Antenna (LISA) is an extraordinarily ambitious joint project by NASA and ESA for observing gravitational waves. The project was first considered in the 1990s, with a possible launch in the decade 2010–2020. It will comprise three spacecraft, separated from one another by distances of around 5 million kilometres, but keeping their relative positions to an extremely high level of accuracy, of micrometric order. When a gravitational wave goes by, the spacecraft will be displaced relative to one another, just like a fleet of ships when an ocean wave goes by.

The orbits of the three satellites will be situated on a circle, which will itself lie in a plane tilted at an angle of $6 0 ^ { \circ }$ to the ecliptic, with center trailing the Earth by $2 0 ^ { \circ }$ in its orbit around the Sun (Fig. 7.67). Each satellite will carry two test masses held in free fall, by virtue of an electrostatic servosystem which compensates for the drag effects due to the interaction of the satellite with the interplanetary medium. The distance between the test masses of each satellite will be continually monitored by laser interferometry (Fig. 7.67).

The space interferometer LISA will complement Earth-based detectors for a different frequency range, viz., $1 0 ^ { - 4 }$ to $0 . 1 \ \mathrm { H z }$ . LISA is planned for launch in 2012 or 2013. The very advanced technology used for LISA will have to be tested during a preparatory mission called LISA Pathfinder, which should be launched in 2008.

LISA should be able to detect gravitational waves emitted by very close compact binary systems. One or other of these objects may be a black hole, a neutron star, or a white dwarf. Since these binary systems have small masses, observations of such systems are limited to our own Galaxy and nearby galaxies. However, most galaxies probably contain a black hole at their centre, with a mass several million times the solar mass. It may be that two galaxies sufficiently close to one another could attract gravitationally, with the result that their black holes eventually merge into one. Our best hope of studying this phenomenon lies in gravitational radiation. The rate of occurrence of this type of event is estimated at about one per galaxy per million years. Considering the millions of galaxies in the visible Universe, LISA may be able to detect several such events, associated with these supermassive objects, every year.

Figure 7.68 gives the expected sensitivity, comparing it with predicted amplitudes for several particularly interesting low frequency sources: the gravitational background of cosmological origin, the low frequency signal of binary stars in the galaxy, which are many, and a black hole collision.

![](images/446abf1486733000b9072841050ffcc248b8b15c27aa0134e3301fea0f88b674.jpg)  
Fig. 7.68 The ultimate sensitivity which could be envisaged for a low frequency gravitational wave detector in space (European mission LISA). The calculated amplitudes of various sources are given. The dashed line shows the theoretical contribution of the cosmological background of gravitational waves. Integration period 1 year, and signal-to-noise equal to 5. (LISA Working Group project and European Space Agency, 1994)

# Problems

7.1. A photomultiplier (PM) receives a flux of $N$ photons per second. Its quantum efficiency is $\eta$ . Describe the Poisson process for the photocurrent $i ( t )$ (mean density, power spectral density). The PM is assumed to filter $i ( t )$ by the transfer function $\varPi ( f / f _ { \mathrm { c } } )$ . Calculate the variance of the photocurrent.

Answer. $\sigma ^ { 2 } = 2 \eta N e ^ { 2 } f _ { \mathrm { c } } = 2 e \langle i \rangle f _ { \mathrm { c } } .$

7.2. Starting from the noise power at the ends of a resistor $R$ , at temperature $T$ (see Sect. 7.2), calculate the variance $\langle \Delta i ^ { 2 } \rangle$ of the current in the resistor.

Answer. $\langle \Delta i ^ { 2 } \rangle = 4 k T \Delta f / R$

7.3. Consider a sighting, formed by strips of equal width, alternately opaque and transparent, with $n$ strips per mm. Describe the image observed in a system for which the MTF is zero beyond the spatial frequency: (a) $w _ { \mathrm { c } } ~ < ~ n ~ \mathrm { m m ^ { - 1 } }$ , (b) $n < w _ { \mathrm { c } } < 2 n \mathrm { m m } ^ { - 1 }$ , (c) $w _ { \mathrm { c } } \gg n \mathrm { \ m m ^ { - 1 } }$ . Answer the same question for an MTF such that $\tilde { G } ( w _ { \mathrm { c } } ) = 0 . 5 G ( 0 )$ (value at 3 dB). The magnification of the system is 1.

7.4. DQE in the Presence of a Dark Current. If the photocathode of the receiver (or its equivalent in the case of a semiconductor detector) emits $\gamma$ electrons $\mathrm { c m } ^ { - 2 } \mathrm { s } ^ { - 1 }$ , the pixel area being $a$ , show that the DQE is

$$
\delta = \left[ \left( 1 + { \frac { \sigma _ { g } ^ { 2 } } { \overline { { g } } ^ { 2 } } } \right) \left( 1 + { \frac { a \gamma } { \eta \overline { { N } } } } \right) + { \frac { \sigma _ { \mathrm { L } } ^ { 2 } } { \overline { { g } } ^ { 2 } \eta \overline { { N } } T } } \right] ^ { - 1 } .
$$

7.5. Signal-to-Noise Ratio and Spatial Frequencies. Consider a multichannel detector, with MTF $\tilde { G } ( \boldsymbol { w } )$ , assumed isotropic to simplify. The detector gives an image $I ( r )$ . In the absence of a signal, the ‘dark image’ (i.e., the grain of the unexposed photographic plate) is the random function $I _ { 0 } ( r )$ , with spectral density $\tilde { I } _ { 0 } ( w )$ . This noise is assumed additive. The signal noise is the photon noise on each pixel, expressed by the spectral density $S _ { 0 } ( w )$ . Show that the DQE is

$$
\delta ( w ) = \eta \frac { S _ { 0 } ( w ) } { | \tilde { I } _ { 0 } ( w ) | ^ { 2 } / | \tilde { G } ( w ) | ^ { 2 } + S _ { 0 } ( w ) } .
$$

Deduce that, in the presence of grain, the signal-to-noise ratio S/N is generally smaller when the high frequencies of an image are studied than when the low frequencies are studied.

7.6. High-Speed Television. Calculate the passband needed to transmit a high resolution TV image (1 000 lines), at a rate of 50 images per second. The intensity of each pixel is defined on 12 bits.

![](images/163e79f7d2e5352fbbe33c04015f01b5144d6e332f537a18d139594ed1877cfe.jpg)  
Fig. 7.69 Structure of an intense $\gamma$ -ray emission

7.7. Gamma-Ray Bursts. Figure 7.69 shows the structure of an intense $\gamma$ -ray burst, detected on 13 June 1979 by the Venera II probe. The time resolution is less than $1 ~ \mathrm { m s }$ (scintillator). Deduce the maximum possible size of the unknown source which produced this emission. (Vedrenne G., Les sursauts $\gamma$ , La Recherche 12, 536, 1981.)

7.8. Noise in Heterodyne Detection. Show that the general expression

$$
\frac { S } { N } = \frac { T _ { \mathrm { { s o u r c e } } } } { T _ { \mathrm { { n } } } } \left( \frac { \Delta \nu _ { \mathrm { { s } } } } { 2 f _ { \mathrm { { c } } } } \right) ^ { 1 / 2 } ,
$$

which gives the signal-to-noise ratio in a direct detection, applies equally to heterodyne detection, where $\Delta \nu _ { \mathrm { s } }$ is then the bandwidth of the IF filter, and $T _ { \mathfrak { n } }$ the total noise temperature. When is the result independent of the power of the local oscillator (assumed noise-free)? At fixed $\nu _ { 0 }$ , how should the signal $\nu _ { \mathrm { s } }$ be filtered before the mixer to avoid superposition of frequencies $\nu _ { \mathrm { { s } } } + \alpha$ and $\nu _ { \mathrm { { s } } } - \alpha ?$ Why is C a single-band receiver used in spectroscopy, when double-band receivers are used to measure continuum spectra? Why is the signal-to-noise ratio S/N increased by a factor of $\sqrt { 2 }$ in the latter case?

7.9. Quantum Noise Limit. Starting from the analysis of quantum noise in Sect. 7.2, show that the quantum fluctuation of blackbody radiation is reached when the noise temperature $T _ { \mathfrak { n } }$ of a detector, sensitive to only one polarisation of radiation at frequency $\nu$ , is such that $k T _ { \mathrm { n } } = h \nu$ . Reconsider Fig. 7.43 in the light of this result.

7.10. The Structure of the Universe at Large Distances. Figure 7.70 (after Kellerman and Toth, ARAA 19, 373, 1981) shows the number $N ( S )$ of radiogalaxies as a function of their flux $S$ . The abscissa is the flux density $S$ at $\lambda = 6 ~ \mathrm { c m }$ , and the ordinate is the difference $\Delta N ~ = ~ \log { [ N ( S ) / 6 0 ] }$ Dbetween the observed distribution $N ( S )$ Dand a uniform distribution in volume in a static Euclidean universe, as it is observed over short distances. All the galaxies are assumed to have the same luminosity. Determine the antenna temperature $T _ { \mathrm { A } }$ corresponding to the faintest sources ( $\mathrm { 1 0 ~ m J y ) }$ . Determine the telescope time $\tau$ required to observe a source with $\mathrm { S } / \mathrm { N } = 1 0$ , $\Delta \nu _ { \mathrm { s } } = 1 0 0 \mathrm { k H z }$ , $T _ { \mathrm { n } } = 3 0 0 ~ \mathrm { K }$ .

![](images/3f60605cce45398f3288a508b81b6a32a721b5c429b0b79b4dc994ef1ca40265.jpg)  
Fig. 7.70 Density of radiogalaxies as a function of their flux

Answer. $\tau \sim 1 0 ^ { 4 } \mathrm { s }$

7.11. A field contains two galaxies, of magnitudes $m _ { \mathrm { v } } = 1 8$ and 28. An image is Dformed in such a way that each one only occupies a single pixel of the detector. The telescope, of diameter $3 . 6 \mathrm { m }$ , is assumed to have unit transmission, and a standard V filter is used (of effective bandwidth ${ \Delta \lambda = 0 . 0 8 9 \mu \mathrm { m } } ,$ ). Assuming reasonable Dquantum efficiencies for (a) a CCD detector, (b) a photon counting camera, study how the signal-to-noise ratio varies for each object, as a function of exposure time. The CCD can be assumed to have readout noise 30 electrons rms.

Answer. The flux from the source is, in $\mathrm { W } \mathrm { m } ^ { - 2 } \mu \mathrm { m } ^ { - 1 }$ ,

$$
e = e _ { 0 } 1 0 ^ { - m / 2 . 5 } ,
$$

and, in terms of counts at the detector,

$$
n = \frac { e S \Delta \lambda } { ( h c / \lambda ) \eta t } \ : ,
$$

where $S \approx 1 0 \mathrm { m } ^ { 2 }$ is the collecting area, $\Delta \lambda = 0 . 0 8 9 \mu \mathrm { m }$ is the effective bandwidth of the filter, $\lambda = 0 . 5 5 \mu \mathrm { m }$ D is the wavelength of the filter, $\eta$ is the quantum efficiency, and $t$ Dis the exposure time.

(a) CCD detector. The readout noise is a fixed, additive noise, independent of the read time, hence the expression

$$
{ \frac { \mathrm { S } } { \mathrm { N } } } = { \frac { n } { { \sqrt { n } } + 3 0 } }
$$

![](images/20ee7522b514162547933325680314a65f77832ef6f08ab6344850538904aa1c.jpg)  
Fig. 7.71 Hecht’s formula

for the signal-to-noise ratio. The readout noise becomes significant when the number of counts accumulated during an exposure is low (in this case, less than 1 000). For an efficiency of $70 \%$ , and $t = 1 ~ \mathrm { m s }$ , $\mathsf { S } / \mathrm { N } = 2 \times 1 0 ^ { 3 }$ for $m _ { \mathrm { v } } = 1 8$ , and $\mathrm { S } / \mathrm { N } = 8 . 5 $ for $m _ { \mathrm { v } } = 2 8$ .

(b) Photon counting camera. $\mathrm { S } / \mathrm { N } = { \sqrt { n } }$ (proportional to $\sqrt { t }$ ). For an efficiency of $10 \%$ , and $t = 1 ~ \mathrm { m s }$ , $\mathrm { S } / \mathrm { N } = 7 . 9 \times 1 0 ^ { 2 }$ for $m _ { \mathrm { v } } = 1 8$ , and $\mathrm { S } / \mathrm { N } = 7 . 9$ for $m _ { \mathrm { v } } = 2 8$ . D D  D DThese values must be corrected for a real transmission of less than unity.

7.12. The photon counting camera is rapidly saturated by bright objects in the field. Calculate the magnitude of a quasar, which saturates such a camera, used with a $3 . 6 \mathrm { m }$ telescope of unit transmission, in the B photometric band, using the fact that saturation occurs at 100 counts per pixel per second.

7.13. Prove Hecht’s equation from Ramo’s theorem, which gives the charge collected in a semiconductor detector (Fig. 7.71) at energies above a few tens of keV.

Answer. The number of charges trapped in $\mathrm { d } x$ , after travelling a path length $x$ (Fig. 7.71), is

$$
\mathrm { d } n = \mathrm { d } x \frac { n _ { 0 } } { \lambda } \mathrm { e } ^ { - x / \lambda } ~ .
$$

Calculating then the total charge $Q$ deposited, for a given type of charge carrier,

$$
Q = e \left( \int _ { 0 } ^ { l } \frac { x } { d } \mathrm { d } n + \frac { l } { d } n _ { 0 } \mathrm { e } ^ { - l / \lambda } \right) \mathrm { ~ , ~ }
$$

Hecht’s formula is obtained by integration.
