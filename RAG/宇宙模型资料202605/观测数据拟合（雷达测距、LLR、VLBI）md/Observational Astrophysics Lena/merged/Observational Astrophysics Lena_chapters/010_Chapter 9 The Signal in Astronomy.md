# Chapter 9 The Signal in Astronomy

Astronomy has often developed by pushing instruments to the limits of their capacities. Many discoveries spring from a combination of noise reduction, by careful design of instrumentation, and efficient signal processing.

Light, or any other information carrier, sent out from a source, crosses various media which influence it on its path, including in some cases the Earth’s atmosphere. It then reaches the observing system and its components: an image is formed by a telescope, the spectrum is analysed by a spectrometer, and a measurable and storable signal is finally produced by a detector. For the astrophysicist, the signal represents a translation of the information emitted by the source, and it is on this signal that the work of interpreting observations will be based.

Since the beginning of the 1990s, there has been a genuine revolution in signal processing thanks to developments in computing. It is now possible to digitise all the information provided by an instrument, which can itself be controlled precisely and automatically by computer. That information can then be stored in practically unlimited quantities, while nevertheless keeping it easily accessible, and it can be processed by extremely sophisticated algorithms, without requiring exorbitant computation times. Observing instruments and systems, comparison of data with models, use of a priori known information to reduce uncertainties due to noise or the limitations of a given instrument, here are some of the novelties made available by extremely elaborate processing of astronomical signals. Clearly this exploits tools developed in a wide range of different applications, but it can also inspire the scientific community to original ideas, born from particular features specific to astronomical observations, such as stringent sensitivity or image quality requirements.

After a brief review of the basic elements of signal processing, this chapter shows how an observing system can be completely modelled by computer, whence its operation can be simulated in every conceivable configuration. This is typical of a common practice today when dealing with complex systems. For example, an aircraft is fully modelled in this way before it makes its first real flight. The previous chapters have dealt individually with the various subsystems, such as imaging devices, spectrographs, and detectors, but the aim here will be to provide a more global point of view of several complete systems through several specific examples, describing how they actually work when carrying out real observations: a radiotelescope, infrared adaptive optics, a photometric satellite, and a $\gamma$ ray observatory. We shall then be able to determine whether the desired observation of the given astronomical source will in fact be possible.

The maximal correction for all effects due to known properties of the instrument, referred to as the instrumental signature, is discussed in the following section. Then comes a more mathematical section, describing the ideas most frequently used in the problem of estimation, where the aim is to deduce the properties of the observed object from the acquired data, using where necessary any information that looks a priori as though it is likely to be true on the basis of the available models of the object.

The last section deals with the tools used to solve the inverse problem, presenting a certain number of applications to the problem of image processing, central to the interpretation and use of observations in astrophysics.

Questions of archiving the immense volume of data produced by all the astronomical instruments that have ever operated or are still operating today, both on Earth and in space, and in particular the methods used to maintain accessibility to this data, are postponed until Chap. 10.

Some of the mathematical tools required in this chapter and throughout the book, such as Fourier transforms, probability, and statistics, are reviewed in Appendices A and B, to ensure consistency of notation insofar as possible.

# 9.1 The Signal and Its Fluctuations

In this section, the subjects will be the role of the detector, the relation between the signal and information from the source, and, finally, the perturbation or noise to which the signal is subjected during an observation.

# 9.1.1 Observing System and Signal

A detector (the general term transducer is also used) transforms the photon flux into a current, a voltage, a charge, or some other measurable or storable quantity, which is usually digitised and processed immediately by computer.

If the detector has imaging capabilities, it provides $N$ distinct pieces of information, each corresponding to an image element of field ${ \mathrm { d } } \omega$ (solid angle), called a pixel.

One particularly important class of detection systems in astronomy (interferometry, see Sect. 6.4) has the remarkable property of sampling information from the source, not in the $\pmb \theta$ plane of the sky, but rather in the conjugate Fourier transform space. Hence, the information element is not defined by its direction of observation, but rather by its position in the conjugate space of spatial frequencies. Instead of measuring the quantity $I ( \pmb \theta ) \mathrm { d } \omega$ , which is the specific intensity received in the direction $\pmb \theta$ , in the solid angle ${ \mathrm { d } } \omega$ , we measure

Table 9.1 Examples of information sampling   

<table><tr><td>· Direction</td><td>·Direction</td></tr><tr><td>· Temporal frequency</td><td>· Time</td></tr><tr><td>e.g.,mirror+ field diaphragm</td><td>e.g.,imaging detector+FT spectrometer</td></tr><tr><td>+ photographic plate + spectral filter · Spatial frequency</td><td>· Spatial frequency</td></tr><tr><td>· Temporal frequency</td><td>· Time</td></tr><tr><td>e.g.,pair of radiotelescopes + electric filter</td><td>e.g., pair of IR telescopes +FT spectrometer</td></tr><tr><td>·Direction</td><td>· Direction</td></tr><tr><td>Energy</td><td>· Polarisation</td></tr><tr><td>e.g.,Y coded mask + scintillator</td><td>e.g.,submillimetre telescope + heterodyne detector</td></tr></table>

$$
{ \tilde { I } } ( w ) = \iint I ( \pmb \theta ) \mathrm { e } ^ { - 2 \mathrm { i } \pi \pmb \theta \cdot w } \mathrm { d } \pmb \theta
$$

in a spatial frequency interval dw.

Since Fourier transforms are one-to-one, knowing $\tilde { I } ( \boldsymbol w )$ on the whole $w$ space is completely equivalent to knowing $I ( \pmb \theta )$ in all directions $\pmb \theta$ . Aperture synthesis methods (see Chap. 8) make use of this approach.

In the same way, spectral filtering involves picking out from the spectral density $S ( \nu )$ of the incident radiation a spectral element of frequency width $\Delta \nu$ , and this is equivalent to sampling the information in a time interval $\Delta t$ and measuring the Fourier transform of the spectral distribution of the radiation (see Chap. 8).

It is also possible to combine these two approaches, as shown schematically in Table 9.1. In each example, the symbol $( \bullet )$ marks the two variables sampled by the -system. Clearly, the signal may take a wide variety of forms, extracting information from the source via some specific filter.

# 9.1.2 Signal and Fluctuations. Noise

In most cases, the raw signal delivered by a detector has the form

$$
\begin{array} { r } { x ( t ) = x \mathrm { _ s } ( t ) + n ( t ) , } \end{array}
$$

where $x _ { \mathrm { s } } ( t )$ is the signal from the source and $n ( t )$ may be a background signal, background noise, detector noise, or a combination of all three. The problem is, firstly, to understand the causes and characteristics of the noise $n ( t )$ , and, secondly, to optimise the acquisition and recording of $x ( t )$ .

For a source of constant intensity, the quantity $x ( t )$ measured by the detection system would have a perfectly well-defined value, but in the reality of physical observation, it has the character of a random variable or process. In the following, therefore, it will be denoted by a bold-type letter $\mathbf { x } ( t )$ .

The physical measurement made of $\mathbf { x } ( t )$ consists in observing one realisation $\zeta$ of this random or stochastic process (abbreviated to s.p. in the following). A measurement carried out over the time interval $\Delta T$ will only be indicative of a process if certain restrictive assumptions can be made about that process, for example, stationarity, or ergodicity.

The causes of fluctuation, which give the signal its random character, are various. Some are due to interference from the measurement itself, and can be compensated for, or eliminated. Some are of a fundamental nature and connected to the physics of the detection process itself, or to the quantum and discrete nature of the electromagnetic interaction (see Sect. 7.2).

The term noise will mean those fluctuations whose effect is to introduce a random deviation between the estimators of the signal, that is, measurements made over a time $\Delta T$ , and the true mean values of the signal. The quantity called the signal-tonoise ratio is a relative measure of this deviation between the desired quantity and its estimator.

This idea of signal-to-noise ratio, which is indeed a ratio of two quantities, denoted by S/N, always refers to a measurement of a specific quantity. There is no such thing as intrinsic signal-to-noise. If $\mathbf { X }$ is a positive random variable, aiming to estimate the physical quantity $x$ , then the S/N of this measurement is defined as the average of $\mathbf { X }$ divided by its standard deviation.

# Background Noise

Even when there is no signal from the source, the detector may nevertheless deliver a signal $\mathbf { x } _ { 0 } ( t )$ , with the character of an s.p. A few examples are given here. Other noise phenomena typical of detectors were introduced in Chap. 7.

Dark Current (Detector Noise)

Even when no photons are incident on its photocathode, a photomultiplier or the pixels of a CCD will produce a non-zero photocurrent, resulting from random electron impacts due to charges whose thermal agitation energies exceed the work function of the metal (the potential holding them in the metal) or the photoconductor gap. The statistics of these fluctuations was discussed in Sect. 7.2. $\mathbf { x } _ { 0 } ( t )$ is called the dark current, and adds to the source signal. Its fluctuations lead to fluctuations in the measured signal.

Grain of a Photographic Plate (Detector Noise)

When an unexposed plate is developed, it exhibits a random blackening $X _ { 0 } ( x , y )$ , at points $( x , y )$ of the plate. This quantity has a non-zero mean value, the continuous background or veiling, and a variance which is the background noise of the plate, caused by the grain of the emulsion.

# Gamma-Ray Background

When used as a detector in a $\gamma$ -ray telescope, a spark chamber detects events even in the absence of radiation from the source. These events are due to $\gamma$ photons produced by the interaction of cosmic rays with the Earth’s atmosphere (see Sect. 2.9), or with the material of the detector itself, and also natural radiation, or other sources. They are random events and give a signal, whose mean value, evaluated as the number of parasitic counts per unit time, is the background signal, and whose variance is the background noise (Fig. 9.1).

# Cosmic Rays on CCDs

The impact of a high energy particle on the photoconducting material of a CCD creates a large number of charges by photo-ionisation. These are detected as if they came from incident photons. This extraneous signal will affect one or more pixels and must be eliminated from the final image. The level of events depends on the location of the detector (on the Earth, at a high altitude, in space, in a radiation belt, etc.). At ground level, it is usually around one event per frame (i.e., over all the pixels), for a $2 5 6 \times 2 5 6$ pixel format, and per minute of observation time.

Thermal Background Noise in the Infrared

A detector placed at the focus of an infrared or submillimetre telescope will receive photons even in the absence of any source in the field of view. There are thermal photons emitted by the Earth’s atmosphere, by the telescope mirrors, and by the optical components encountered (windows, filters, and so on). This flux of photons gives an average background signal, whose fluctuations are called the thermal background noise (see Sect. 7.2).

In each of these cases, the aim will be to understand the nature and statistics of the process $\mathbf { x } _ { 0 } ( t )$ , in order to deduce its effect on measurement of the signal $\mathbf { x } ( t )$ .

![](images/f2f8a634724613596ef2b8f275e50d6248f9bac8cd995bb555e327500b0199ad.jpg)  
Fig. 9.1 Background noise measured during observation of gamma radiation in the Earth’s stratosphere. The smooth curve gives the background modelled as a superposition of local atmospheric background, elastic scattering of neutrons, and the induced $\beta$ radioactivity. The noisy curve, in good agreement with the model, results from measurements made in the spectral range $5 \mathrm { k e V }$ to $1 0 \ \mathrm { M e V } .$ Any astronomical signal would be superposed on this background. (Hexagone instrument, on a stratospheric balloon, altitude 3.6 mbar, Alice Springs, Australia, 1989. Document courtesy of Vedrenne G.) ´

# Signal Noise

The signal from the source itself may also exhibit random fluctuations.

Transmission Noise (Multiplicative Noise)

If the absorption properties of the medium vary randomly in time, the transmitted signal will have the form

$$
\mathbf { x } ( t ) = A ( t ) \mathbf { x } _ { \mathrm { s } } ( t ) ,
$$

where ${ \bf x } _ { \mathrm { s } } ( t )$ is the source signal and $A ( t )$ a fluctuating transmission. This is the case when there is scintillation at visible or radio frequencies, this phenomenon being related to fluctuations in the refractive index of the air (see Sect. 6.2), or of the electron density in the ionosphere, respectively. It is also the case in the infrared, when there is variation in the water vapour content of the atmosphere.

Signal Noise (Thermodynamic or Photon Noise)

An electromagnetic wave emitted by a thermal process (e.g., blackbody) is incoherent. The field $\mathbf { } E ( t )$ is a random process, whose fluctuations are explained by a lack of phase correlation over the atoms radiating the macroscopic field. A photon description can also be given. The rate of arrival of photons from the source is a random function, whose mean value is the mean received flux.

In brief, these phenomena can be classified into three main categories, according to the various causes of fluctuation:

• Fundamental limitations, of thermodynamic origin, related to the physical nature of the radiation (photon noise of the signal), to its incoherence, or to its interaction with matter in the detection process (irreducible detector noise). Practical limitations, resulting from the quality of the detectors, whose design is constrained by the present state of understanding and technology. Such limitations are constantly being pushed back: thus, the intrinsic noise of near infrared detectors $( 1 { - } 1 0 \mu \mathrm { m } )$ is characterised by a variance whose value has been reduced by a factor of $1 0 ^ { 8 }$ , a gain of eight orders of magnitude, between 1960 and 1990, while the format progressed from 1 pixel to almost $1 0 ^ { 7 }$ pixels in 2007. Observational limitations, where the signal is affected by the local environment in which observations are made. These observation conditions can almost always be improved, by changing the instrumental arrangement, or the site, going outside the Earth’s atmosphere, and so on.

Recall that the first category here, of fundamental limitations, was discussed in Sect. 7.2, along with the practical performance of detectors. It is quite clear that these fundamental limitations will determine the performance that can ultimately be attained by any measurement system.

# Signal-to-Noise Ratio. Detection Limits

The signal $x ( t )$ is one realisation of a random process $\mathbf { x } ( t )$ , and extraction of the information it contains constitutes an estimate (see Appendix B and Sect. 9.5). The degree of confidence which can be accorded to this estimate will depend on the type of information contained in the signal, as well as the statistics of the fluctuations it manifests.

The signal is written in the form

$$
x ( t ) = x _ { 0 } ( t ) + x _ { \mathrm { s } } ( t ) .
$$

In the case of statistically independent additive noise, the variance of the signal is written

$$
\sigma _ { x } ^ { 2 } = \sigma _ { x _ { 0 } } ^ { 2 } + \sigma _ { x _ { \mathrm { s } } } ^ { 2 } .
$$

We examine the simple case in which the desired quantity is the mean $\langle x _ { \mathrm { s } } \rangle$ . An h iexample would be the measurement of a spectrum by making a best estimate of the intensity in each spectral element. Assume that $\langle x _ { 0 } ( t ) \rangle$ can be estimated with h irelatively low uncertainty by means of an independent experiment (determining the statistical properties of the noise). The signal estimate is then1

$$
\langle x ( t ) \rangle _ { T } - \langle x _ { 0 } ( t ) \rangle .
$$

If the statistics of $x _ { \mathrm { s } } ( t )$ and $x _ { 0 } ( t )$ are known, then so are $\sigma _ { x _ { 0 } }$ and $\sigma _ { x _ { \mathrm { s } } }$ , and the estimate of the signal-to-noise ratio is

$$
\frac { \mathrm { S } } { \mathrm { N } } = \frac { \langle x ( t ) \rangle _ { T } - \langle x _ { 0 } ( t ) \rangle } { \bigl ( \sigma _ { x _ { 0 } } ^ { 2 } + \sigma _ { x _ { \mathrm { s } } } ^ { 2 } \bigr ) ^ { 1 / 2 } } .
$$

If the statistics are not known, then the quantities $\sigma _ { x _ { 0 } }$ and $\sigma _ { x _ { \mathrm { s } } }$ must be estimated, by repeating the measurements, so that the next order moment (the variance of the variance) is small (see Sect. 9.5).

If $\langle x _ { 0 } ( t ) \rangle$ could not be determined without error, the signal estimate would be

$$
x ( t ) - { \mathrm { e s t i m a t e ~ o f ~ } } \langle x _ { 0 } ( t ) \rangle ,
$$

and the signal-to-noise ratio would be

$$
{ \frac { \mathrm { s i g n a l } \mathrm { e s t i m a t e } } { \left( \sigma _ { x _ { 0 } } ^ { 2 } + 2 \sigma _ { x _ { \mathrm { s } } } ^ { 2 } \right) ^ { 1 / 2 } } } .
$$

It must be decided what value of this ratio allows us to assert that the source is detectable. The question can only be answered by making some hypothesis concerning the statistical properties of the random process which constitutes the noise.

![](images/06f68c4827b5508be30a7948b7a3d1ee5d4817bc6ff48747ee96678a8fd0de43.jpg)  
Fig. 9.2 Spectral characteristics of a particular example of Gaussian noise. The spectral density $S _ { \mathbf { N } } ( f )$ is almost constant (white) at frequencies $f \lesssim f _ { \mathrm { c } }$

The determination of a signal from measurements is therefore a process of estimation. Care must be taken to use unbiased estimators, or else to correct for any bias (see Appendix B and Sect. 9.5.4). For example, in order to estimate the variance of the noise, with a view to evaluating the signal-to-noise ratio, a simple estimate of the variance on the measurement sample gives a biased value, which must be corrected for.

The term bias is used in a more general context, when the aim is to measure a physical quantity $X$ using some measuring instrument. The latter gives, in reality, $X + B$ , where $B$ is Ca measurement bias due to some extraneous signal, a background, or the like. $B$ must then be estimated independently in order to subtract the bias.

Gaussian Noise

Consider a signal represented by

$$
\begin{array} { r } { x ( t ) = x \mathrm { { s } } + N ( t ) , } \end{array}
$$

where $\mathbf { N } ( t )$ is a Gaussian s.p. with zero mean, autocorrelation $R ( \tau )$ , and spectral density $S ( f )$ , supposed approximately constant (almost-white noise)2 for $f \lesssim f _ { \mathrm { c } }$ (Fig. 9.2). Consider a measurement made over a time $T$ .

We wish to determine the degree of confidence that can be attributed to the estimate $\hat { x }$ of $\langle x ( t ) \rangle$ given by

$$
\hat { x } = \frac { 1 } { T } \int _ { 0 } ^ { T } x ( t ) \mathop { } \mathrm { d } t .
$$

It can be shown (see Appendix B) that

$$
\sigma _ { \hat { x } } ^ { 2 } = \frac { R ( 0 ) } { 2 f _ { \mathrm { c } } T } .
$$

The Gaussian probability distribution gives a degree of confidence for intervals centred on $x _ { s }$ , with extent $\pm \sigma$ , $\pm 3 \sigma$ , etc. (see Table B.1 in Appendix B).

˙ ˙The central limit theorem3 shows that many of the fluctuation phenomena encountered in measurement can be considered as Gaussian processes. In the presence of Gaussian noise, a confidence interval of $\pm 1 . 5 \sigma$ is often taken as satisfactory.

In order to be intelligible, every curve and every measurement result published in the literature must be accompanied by an error bar $\pm n \sigma$ based on the variance $\sigma$

Signal-to-Noise Ratio and Integration Times

The relation

$$
\sigma _ { \hat { x } } ^ { 2 } = \frac { R ( 0 ) } { 2 f _ { \mathrm { c } } T }
$$

shows that the variance of the noise decreases as the $- 1 / 2$ power of the measure-ment time, although exceptions are sometimes encountered. This very general result fixes a practical limit on how much the signal-to-noise ratio can be improved by increasing the measurement time, taking into account the average lifespan of an astronomer. Indeed, it is altogether feasible to gain a factor of $1 0 ^ { 3 }$ by extending the time from $1 ~ \mu \mathrm { s }$ to $1 \mathrm { ~ s ~ }$ , and a further factor of 300 in increasing the time to one day. However, the next factor of 200 would require extension from one day to one century.

Averaging is the most straightforward procedure for improving the signal-tonoise ratio, as shown in Fig. 9.3. It is implicit in this analysis that the noise can be assumed stationary, and that the required quantity $x _ { \mathrm { s } }$ does not itself fluctuate, during the period considered.

It is sometimes observed that this rule no longer holds for faint sources superposed on a strong sky emission background. Subtraction of the sky background (see Sect. 2.3) then creates a noise increasing as $T ^ { 1 / 2 }$ , when this background is intense. The signal-to-noise ratio, instead of continuing to increase with $T$ , tends to some constant value as $T$ increases. In some approaches using CCDs, it is possible to subtract the background at frequent and regularly spaced intervals of time, so avoiding the saturation effect (sloshing mode).

Figure 9.3 illustrates the gain in the signal-to-noise ratio by averaging, both in a 1D scan and in an image. The latter shows the superposition of 3 000 individual images, obtained with a TV camera (exposure $1 / 3 0 \mathrm { s }$ ), using a broad band filter $4 1 0 { - } 7 6 0 ~ \mathrm { n m }$ ), of a magnitude 16 quasar. First, the thirty images taken each second are cumulated, and realigned on the brightest pixel, and then all these one second images are again cumulated. Image realignment techniques are important and we shall return to this matter in Sect. 9.6. This simultaneously improves the S/N ratio, by the averaging effect, and corrects for atmospheric activity (see Sect. 6.2), hence improving the resolution of the image. The brightest image was extended (i.e., had two barely resolved components), and was later fully resolved by speckle interferometry (see Sect. 5.2), then by adaptive optics. The four components constitute a gravitational mirage of the same quasar, but the galaxy causing it is too faint to be extracted from the noise. It was observed in the 1990s from the ground and also by the Hubble Telescope. More recently, this same quasar was observed in the infrared by the Japanese Subaru telescope in Hawaii (see Fig. 9.4). The image shows not only the four components, but also the whole gravitational mirage in the form of a beautiful Einstein ring.

![](images/dcf9c9722eebc31c940a8d7af05588577667e279993592b309027e8b82af43b2.jpg)  
Fig. 9.3 Extraction of a signal from noise by averaging. (a) Thermal emission from cold dust in the plane of the Galaxy, at a wavelength $\lambda = 0 . 9 \mathrm { m m }$ . The brightness temperature is in millikelvin $[ \mathrm { m K } ]$ D, measured as a function of galactic latitude, at a given longitude. $\mathbf { A } =$ single scan, $T = 0 . 7 ~ \mathrm { s }$ , and $\mathbf { B } =$ D Dmean over 1 400 successive scans. From Pajot F., doctoral thesis, Paris VII, 1983. See also DProblem 2.8. (b) The triple quasar QSO PG $1 1 1 5 + 0 8$ . The second quasar was discovered in the Cform of a gravitational mirage. This observation was made using a $1 . 8 \mathrm { ~ m ~ }$ telescope (one element of the Multi-Mirror Telescope). Scale $5 1 2 \times 5 1 2$ pixels, $1 { \mathrm { p i x e l } } = 1 0 ^ { - 2 }$ arcsec. Image courtesy of  DHege E.K. For the speckle observing method, see Hege E.K. et al., Ap. J. 248, L1, 1981. With the kind permission of the Astrophysical Journal

# 9.1.3 Elementary Signal Processing

# Digitisation

Although certain operations, such as filtering, can be carried out by analogue techniques, the trend in modern methods of signal processing is towards digital processing, in which the signal $x ( t )$ is simultaneously sampled and transformed into a binary-coded numerical value by means of an analogue-to-digital converter (ADC). The number of bits of information used to represent the maximum value of the analogue variable $x ( t )$ is called the dynamic range of the converter. The value of the analogue variable corresponding to one bit is called the digitisation step. The operation thus amounts to replacing $x ( t )$ by $\hat { x }$ , if $x ( t )$ lies between ${ \hat { x } } - q / 2$ and ${ \hat { x } } + q / 2$ , where $q$ is the digitisation step.

![](images/83effcd41b20c07bba4a2397571d11f50d554f301f6152e99cff21a9a6f715f8.jpg)  
Fig. 9.4 The quasar QSO PG $1 1 1 5 { + } 0 8 $ , observed in the near infrared (J and $\mathrm { K } ^ { \prime }$ spectral bands) with the Japanese Subaru lescope in Hawaii. The resolution of the image is 0.12 arcsec, thanks to a combination of adaptive optics and deconvolution. (a) An Einstein ring (gravitational mirage). (b) Composite image $( \mathrm { J } { + } \mathrm { K } ^ { \prime } )$ showing the four components. Compare with Fig. 9.3, obtained two decades earlier. Reproduced with the kind permission of Iwamuro, F. et al., Publ. Astr. Soc. Jap. 52, 25–32, 2000

CThe moments of the new random variable $\hat { x }$ are clearly different from those of $x ( t )$ O. It can be shown, for example, that the error in taking the autocorrelation function $\hat { C } ( \tau )$ , rather than the autocorrelation function $C ( \tau )$ of $x ( t )$ , is negligible, provided that $q$ is chosen less than $\sigma$ , where $\sigma ^ { 2 }$ is the variance of $x ( t )$ . For certain operations, it is enough to digitise using just one bit. For example, if $\mathbf { x } ( t )$ is a r.v. with zero mean, digitising can be limited to specifying the sign of $x ( t )$ . There is a significant gain in calculation time (Problem 9.11).

# Sampling

Sampling means reading off the value of the signal at times $t$ (or, more generally, at discrete values of the variable labelling the signal, such as $x$ and $y$ coordinates on a photographic plate). The interval between two successive readings is called the sampling rate.

This rate is usually constant, but it need not be so. Sometimes it is random. Suppose the aim is to study the magnitude variations of a star, possibly periodic, in a site affected by uncertain weather conditions. The nights when measurement is possible are distributed randomly in time, and the brightness $b ( t )$ of the star is thus randomly sampled. An analogous problem occurs in the sampling of a signal due to the photospheric oscillations of the Sun (helioseismology), or a star (astroseismology).

Using the Dirac comb distribution, defined in Appendix A, to describe sampling at rate $\Delta t$ ,

$$
x ( t ) { \mathrm { ~ s a m p l e d ~ } } = \sqcup { \bigg ( } { \frac { t } { \Delta t } } { \bigg ) } x ( t ) .
$$

Choice of Sampling Rate. Shannon’s Theorem

Consider a function $f ( x )$ whose spectrum $\tilde { f } ( s )$ has bounded support $[ - s _ { \mathrm { m } } , + s _ { \mathrm { m } } ]$ The sampling of $f ( x )$ defined by the distribution

$$
F ( x ) = f ( x ) \sqcup \left( { \frac { x } { \Delta x } } \right) ,
$$

with the sampling rate

$$
\Delta x = \frac { 1 } { 2 s _ { \mathrm { m } } } ,
$$

is enough to be able to reconstruct $f ( x )$ for all $x$ , by the convolution

$$
f ( x ) = F ( x ) \star \mathrm { s i n c } \left( { \frac { x } { \Delta x } } \right) .
$$

A sufficient condition to ensure the converse is $\tilde { f } ( s _ { \mathrm { m } } ) = 0$ . For sampling in which $\Delta x = 1 / 2 s _ { \mathrm { m } }$ holds exactly, information can be lost (Fig. 9.5).

DTherefore, with the exception of this component, $f ( x )$ is completely specified by the discrete sampling $F ( x )$ . This is confirmed by

![](images/f2f87bb937a54bc14943c6a2dedf67041be632bd24a438dd34571aceda5ce99c.jpg)  
Fig. 9.5 Shannon’s theorem, or sampling theorem. The representation of $F ( x )$ uses a sequence of Dirac distributions, symbolised by an arrow whose height is proportional to the weight. In (a) is shown a component of $f ( x )$ which would be lost in the sampling

$$
F ( x ) * ( \frac { x } { \Delta x } )  \tilde { F } ( s ) \Pi ( s \Delta x ) ,
$$

which is equivalent to

$$
f ( x )  \tilde { f } ( s ) , \quad \mathrm { i f } \quad \Delta x = \frac { 1 } { 2 s _ { \mathrm { m } } } ,
$$

where the arrows denote Fourier transform.

The great importance of this theorem, known as Shannon’s theorem, 4 springs from the physical nature of the functions sampled. A receiver does not respond to infinitely large frequencies, and always behaves as a low-pass filter, with a cutoff at some temporal or spatial frequency $s _ { \mathrm { m } }$ .

Sampling at any rate above or below the Shannon rate is called oversampling or undersampling, respectively. The only drawback of oversampling is the amount of redundant measurement data, whilst undersampling leads to the phenomenon of aliasing. The latter can have a considerable adverse effect on the results of measurement, by re-injecting into the spectrum, and at low frequencies, Fourier components of frequency above the cutoff frequency (Problem 9.10).

# Filtering

In some cases it is useful to be able to examine a signal in real time, that is, without waiting until the end of the measurement. The optimal signal processing may then differ from the one that is most appropriate when the signal is available in its totality, over the whole measurement period.

Filtering a signal implies keeping only a part of the information it carries, by reducing or modifying its initial frequency spectrum. Only frequencies containing relevant information are conserved, if they are known beforehand, or else those at which the noise has a tolerable level, or those satisfying a combination of these criteria.

Optimising the way the signal is processed, whether in real time or otherwise, leads to the idea of optimal filtering. An analogue signal (that is, in the form of a continuous physical quantity, such as a voltage, or the blackening of a photographic plate) is digitised. This means that it is transformed into a finite set of numerical values, and hence coded by a finite number of bits of information. If this is a very small electric charge (the pixel of a CCD), or a flux of singly detected photons, digitisation is immediate, since the signal is already a discretised quantity. This digitisation occurs at discrete time intervals: the signal has been sampled.

Let us examine how these operations modify the information content of $x _ { \mathrm { s } } ( t )$ , and how they may improve the signal-to-noise ratio of the measurement.

Optimal Filtering

Suppose first that $x ( t )$ is measured over an infinitely long time ( $T \to \infty$ ). Suppose also that the statistics of the stochastic processes ${ \bf x } _ { \mathrm { s } } ( t )$ and ${ \bf n } ( t )$ ! 1are known, and that they are both stationary processes. This would be the case in the following situation: ${ \bf x } _ { \mathrm { s } } ( t )$ could be the arrival of photons from some periodically varying source, with frequency $f _ { 0 }$ , such as a pulsar, and ${ \bf n } ( t )$ could be the background noise due to temporal fluctuations in the sky background.

The problem is to find the best possible estimate of ${ \bf x } _ { \mathrm { s } } ( t )$ , which will be denoted ${ \hat { x } } _ { \mathrm { s } } ( t )$ . Set

$$
\hat { x } ( t ) = \int _ { - \infty } ^ { + \infty } x ( t - u ) h ( u ) \mathrm { d } u ,
$$

where the function $h ( u )$ is chosen in such a way as to minimise the expectation value

$$
E \left\{ \left| x ( t ) - \hat { x } ( t ) \right| ^ { 2 } \right\} .
$$

It can be shown that the linear filter $h ( t )$ may be found in the following way. Let $S _ { \mathbf { x } } ( f )$ be the spectral density of $\mathbf { x } ( t )$ , and $S _ { \mathbf { x x } _ { \mathrm { s } } } ( f )$ be the cross-spectrum between the observed quantity and the desired signal. (As explained in Appendix A, the crossspectrum is simply the Fourier transform of the cross-correlation function.) Then, denoting the FT of $h ( t )$ by $\tilde { h } ( f )$ ,

$$
\tilde { h } ( f ) = \frac { S _ { \mathrm { x x } _ { \mathrm { s } } } ( f ) } { S _ { \mathrm { x } } ( f ) } .
$$

The transfer function $\tilde { h } ( f )$ is that of the optimal linear filter, or Wiener–Kolmogorov filter. 5 In Sect. 9.6, we shall return in more detail to the question of how this filtering can use a priori information about the source.

• In the particular case when signal and noise are uncorrelated, it follows that

$$
\begin{array} { r l } { S _ { \mathbf { x } _ { s } \mathbf { n } } = 0 , \quad S _ { \mathbf { x } } ( f ) = S _ { \mathbf { x } _ { s } } ( f ) + S _ { \mathbf { n } } ( f ) , \quad S _ { \mathbf { x } \mathbf { x } _ { s } } ( f ) = S _ { \mathbf { x } _ { s } } ( f ) , } & { } \\ { \tilde { h } ( f ) = \frac { S _ { \mathbf { x } _ { s } } ( f ) } { S _ { \mathbf { x } _ { s } } ( f ) + S _ { \mathbf { n } } ( f ) } . } & { } \end{array}
$$

If the spectra $S _ { \mathbf { x } _ { \mathrm { s } } } ( f )$ and $S _ { \mathbf { n } } ( f )$ do not overlap, then $\tilde { h } ( f ) ~ = ~ 1$ wherever $S _ { \mathbf { n } } ( f ) = 0$ , and $\tilde { h } ( f ) = 0$ wherever $S _ { \mathbf { n } } ( f ) \neq 0$ . Note that $\tilde { h } ( f )$ is arbitrary D D ¤outside these intervals. It is also true that the error in the estimate ${ \hat { x } } ( t )$ for ${ \bf x } _ { \mathrm { s } } ( t )$ is everywhere zero.

• If there is some overlap between the supports of $S _ { \mathbf { x } _ { \mathrm { s } } } ( f )$ and $S _ { \mathbf { n } } ( f )$ , then filtering by $\tilde { h } ( f )$ leads to an estimate ${ \hat { x } } ( t )$ for ${ \bf x } _ { \mathrm { s } } ( t )$ with error, given in least squares by

$$
\varepsilon = \frac { 1 } { 2 \pi } \int _ { - \infty } ^ { + \infty } \frac { S _ { \mathbf { x } _ { \mathrm { s } } } ( f ) S _ { \mathbf { n } } ( f ) } { S _ { \mathbf { x } _ { \mathrm { s } } } ( f ) + S _ { \mathbf { n } } ( f ) } \mathrm { d } f .
$$

The idea of a signal-to-noise ratio is difficult to apply here, for the estimated signal ${ \hat { x } } ( t )$ can take a wide range of values on $( - \infty , + \infty )$ , whereas $\varepsilon$ is a well-Odefined quantity. On the other hand, since ${ \bf x } _ { \mathrm { s } } ( t )$ 1 C1is periodic in the example chosen, the signal- to-noise ratio is well-defined in the Fourier space, where the signal is concentrated around the frequency $f _ { 0 }$ .

The results, obtained here for a signal depending on the single parameter $t$ , can easily be extended to the optimal filtering of an image, in which case the signal and the noise are both functions of the two coordinates describing a point in the image plane.

Online Filtering

We have studied the case in which all the information is available before the Wiener filter is applied to it. A different case occurs when the signal must be processed in real time, because of some communications problem. Then, the message must be decoded or extracted from the noise before it has all been transmitted. Indeed, we wish to give the best possible estimate of the message at each instant of time.

An example would be the transmission of an image of Uranus from a probe in flyby. Because of the great distance and the limited power available on board, the image is transmitted pixel by pixel, and the transmission is affected by various noise sources. After receiving the whole image, the ground base can process it by means of an appropriate filter, eliminating noise as far as possible and producing a filtered image. The astronomer may also wish to have an incomplete image but in real time, in which case the intensity of each pixel must be estimated online from the raw signal.

Another example can be given, concerning the variability of an $\mathrm { X }$ -ray source, observed by an orbiting X-ray telescope. The measured flux is transmitted to Earth, affected by noise of known statistical behaviour. After several months of observation, the raw signal is analysed, for example, in order to determine periodic fluctuations by filtering and Fourier analysis. But, considering the length of the observation, it may also be desirable to make a best estimate, at each instant $t$ , of the true flux of the source.

This type of filtering is particularly suitable for real time telecommunications (e.g., telephone, television), in which there is no question of awaiting the end of a signal before processing it.

Other Applications of Filtering

The linear filtering described by the convolution

$$
y ( t ) = h ( t ) \star x ( t ) ,
$$

or by its equivalent in the Fourier space

$$
\tilde { y } ( f ) = \tilde { h } ( f ) \tilde { x } ( f ) ,
$$

can be used to eliminate the continuous component of a signal [setting $\tilde { h } ( 0 ) = 0 ]$ , or an extraneous frequency $f _ { 0 }$ [setting $\tilde { h } ( f _ { 0 } ) \doteq 0 ]$ D, or high frequencies (using a lowpass filter, cutting off at $f > f _ { \mathrm { c } } )$ D. For example, a photometer measuring the flux from a star would be followed up by a low-pass filter, eliminating fluctuations due to scintillation, and providing a photometric measurement of the mean brightness.

A wide range of filters exists for specific applications, and their description can be found in specialised texts.

Here we shall give an example, serving to introduce the methods discussed in Sect. 9.5. It concerns an important method of filtering known as cross-validation. It often happens that the best processing of a set of raw data depends on an unknown parameter $\alpha$ . This may be a cutoff frequency, or a whole number, such as the degree $n$ of an interpolating polynomial, or the number $n$ of components (spectral lines) giving the best fit to an observed spectrum. For any given value of this parameter $\alpha$ , the data processing procedure is known (e.g., filtering, regression, fitting, etc.), but the value of $\alpha$ is unknown. The cross-validation method provides a way of estimating a good value for $\alpha$ , precisely by minimising prediction errors.

In order to illustrate this claim, consider the problem of smoothing some experimentally determined points by means of a polynomial of degree $n$ . As the degree is fixed, the smoothing procedure consists in fitting the observational data to a polynomial, by applying the least squares criterion. $n$ is then a parameter controlling the degree of smoothing. If $n = 1$ , the experimental Dpoints are simply fitted to a straight line by least squares (maximal smoothing, Fig. 9.6a). If $\textit { n } = \textit { N } - \textit { 1 }$ , where $N$ is the number of points, the polynomial goes through every point, D corresponding to a minimal smoothing.

Experience shows that, in the latter case, the polynomial will oscillate a great deal between the experimental points which constrain it (Fig. 9.6b). If a further point were given between two already known points, it would be possible to say whether the prediction given by the polynomial was a good one or not. We could then quantify the error in the prediction, between the interpolated value and the new experimental point. Clearly, such an extra piece of data is not available, for if it had been, it would have been treated in the same way as the others, without obtaining any further benefit from it. However, it is possible to ‘simulate’ these hidden, and then rediscovered, data points. This is the principle of cross-validation, which tests a certain degree $n$ by ‘hiding’ the second point, then smoothing and comparing the interpolated value with the hidden value, whence a prediction error denoted $\varepsilon _ { 2 } ^ { ( n ) }$ . This procedure is repeated, omitting successively all the points, from the second to the $( N - 1 ) \mathrm { t h }$ . A prediction error $Q ( n )$ can then be given, which depends on the degree $n$ ,

![](images/91e25bc7a428c2180760afc15bdc9330172d938e84cf78718c5e7f1e7d875a39.jpg)  
Fig. 9.6 (a) Smoothing of $N$ experimental points by a least squares straight line $\mathbf { \Phi } ( n \ = \ 1 )$ . (b) Smoothing of the same points by a polynomial of degree $N - 1$

![](images/1d495a5dd64b1a1c802024162d19d6ca434984fa54d8296ab63395cd255b817a.jpg)  
Fig. 9.7 Simulated cross-validation. The ‘experimental points’ are shown with their variance. The continuous curve is the smoothing (or regression) obtained for a polynomial whose degree $n = 3$ was itself obtained by cross-validation. The dashed line is the least squares straight line $( n = 1$ ). DThe dotted curve is the theoretical curve used to generate the ‘experimental points’. It is well reproduced by the data processing method here

$$
Q ( n ) = \sum _ { i = 2 } ^ { N - 1 } \varepsilon _ { i } ^ { ( n ) 2 } .
$$

Note that the first and last points have been omitted, as they would not allow interpolation, but rather an extrapolation.

Cross-validation consists in choosing that value of $n$ which minimises the error $Q ( n )$ . It is mainly a fact of experience that, whatever the nature of the control parameter $\alpha$ , this method gives good results, as can be seen in Fig. 9.7.

# Data Compression

Data produced by an instrument can show a high level of internal redundancy. In particular, the value of a pixel in an image is often strongly correlated with the values of the neighbouring pixels. In order to determine the level of data redundancy and, hence, how much the data might possibly be compressed during a transmission, it is useful to measure the quantity of information contained in the image. The notion of entropy is thus introduced (see also Sect. 9.6).6

Consider an image whose pixels are coded on $N$ bits, which implies $2 ^ { N }$ possible values. Let $P _ { i }$ be the number of pixels taking the $i$ th value, as $i$ runs from 0 to $2 ^ { N } - 1$ . The histogram giving $P _ { i }$ as a function of $i$ represents the probability that the signal takes a given value on any pixel. Starting from this empirical probability distribution $P _ { i }$ , the entropy $H$ of the image can be constructed by

$$
H = - \sum _ { i = 0 } ^ { 2 ^ { N } - 1 } P _ { i } \log _ { 2 } P _ { i } .
$$

The entropy is expressed in bits per pixel and represents the number of bits necessary to code the image without loss of information. The entropy is calculated for an image whose redundancy has already been reduced, and which therefore requires fewer coding bits. Decorrelation algorithms exist to this effect. For example, a simple method consists in replacing each pixel $p _ { i , j }$ by the difference between the value of this pixel and that of its neighbour, namely $p _ { i , j } - p _ { i , j - 1 }$ .

Applying this to the example of a field of stars, each of which occupies just one or a very small number of pixels, on a uniform background, the operation described amounts to replacing the value of the uniform field by zero almost everywhere. This leads to a considerable saving in coding bits.

If all the available values are equiprobable, then $H \ = \ N$ is constant, and no Dcompression can be applied. If on the contrary the image is binary, as is the case for a text of black letters on a white background, then $H \ < \ N$ , and compression algorithms can be applied with a high level of reduction $( \approx 1 0 0 )$ . Generally speaking, the maximum compression ratio applicable to an image of entropy $H$ coded on $N$ bits, after eliminating redundancy between neighbours, is just $N / H$ .

Application specific integrated circuits (ASIC) carry out compression operations in real time. Apart from their use in satellites for terrestrial observation (e.g., SPOT satellites), compression methods are used mainly for transmissions within computer networks. They were also used during an observation mission by the satellite Clementine (1993), in lunar orbit, which mapped the whole surface of the moon in more than ten colours and at high resolution.

# 9.1.4 A Specific Example of Data Processing

Data such as spectra, images, and so on, can be treated in many ways. Analysis into principal components (or factor analysis) aims to expose any linear structure underlying large amounts of data. Karhunen–Loeve series are used when this data\` is a realisation of a stochastic process.

In order to illustrate the method in a specific case, consider a random vector $X = ( X _ { 1 } , X _ { 2 } , \ldots , X _ { n } )$ , which will be analysed into its principal components.

DAny particular realisation of $X$ can be represented by a point in an $n$ -dimensional space. Note that this analysis into principal components only really becomes useful when $n$ is large. A set of $N$ realisations of the random vector, $N \ > \ n$ , will be spread out in the space like a sort of ‘cloud’ of points. It may happen, in so-called degenerate cases, that these points do not fill out all the dimensions available, but rather remain within some affine submanifold of $\mathbb { R } ^ { n }$ (a hyperspace, for example), of dimension $k \ : < n$ . If this is the case, the data can be compressed by describing it using only the $k$ parameters of the submanifold, rather than all the $n$ components of the canonical basis. Along the normal to the submanifold, the variance of the data is zero, and this immediately eliminates an axis which supplies no information about the way the cloud of points is distributed in the space. The new basis of dimension $k$ gives a better description of the data than did the original basis.

This ideal case is rarely encountered in practice. More common is the case in which the spread of data along a certain axis is not exactly zero, but is nevertheless small. The points are almost distributed on a $k$ -dimensional submanifold. If the cloud of points is described using the $k$ -dimensional basis, then the mean squared error incurred will correspond to the spread of the data along the neglected axis. Finding this axis amounts to identifying the direction along which the variance of the data, as a measure of its spread, is a minimum.

The problem is solved by placing the origin of the space at the mean of the data, and then choosing as basis the eigenvectors of the variance/covariance matrix of the vector $X$ . The notation $X$ will hereafter refer to the components in this new, centred basis. The corresponding eigenvalues are exactly the data variances along these axes. If a loss of information can be accepted up to a certain level, then the proper axes can be neglected until the sum of their associated eigenvalues, classed in increasing order, reaches that level.

In order to formulate this, the data can be written

$$
X = \sum _ { i = 1 } ^ { n } A _ { i } { \mathbf { \mathit { f } } } _ { i } ,
$$

where $X$ is the centered random vector, and $A _ { i }$ the random components of $X$ in the fixed basis $\pmb { f } _ { i }$ ; $i = 1 , \ldots , n$ . The eigenvalue equation is

$$
E \left\{ X X ^ { \mathrm { T } } \right\} f _ { i } = \lambda _ { i } ^ { 2 } f _ { i } ,
$$

where $E \left\{ X X ^ { \mathrm { { T } } } \right\}$ is the expected value of the variance–covariance matrix and $\lambda _ { i } ^ { 2 }$ is the variance of $X$ in the direction of $\pmb { f } _ { i }$ . This basis is orthonormal, being the set of eigenvectors of a symmetric matrix, and the $A _ { i }$ are uncorrelated random variables, in the sense that

$$
E \left\{ A _ { i } A _ { j } \right\} = \lambda _ { i } ^ { 2 } \delta _ { i j } .
$$

In the special case when $X$ is a normal random variable, the $A _ { i }$ are, in addition, independent random variables.

In this way, the stochastic process is replaced by a set of random variables, ideally independent. Apart from the linear analysis already mentioned, this leads to a simplification of the data processing.

# 9.2 Complete Model of an Observing System

Since astronomical instruments are ever more sophisticated and expensive, it is easy to understand the importance of carrying out studies before they are actually put together for real. For one thing, there must be no risk of error in predicted performance when millions of euros are involved, not to mention the work of dozens of people over several years. For another, the increasing complexity of instruments also multiplies the risk of malfunction, or unexpected interactions between subsystems or between a priori unconnected functions.

A good instrumental model is now an essential tool for several reasons:

• To obtain the best possible design for the given scientific requirements and to make good choices, or at least the best possible compromise, e.g., when working out the error budget for the various subsystems. To predict performance in order to convince the scientific community and funding organisations that a new instrument is worthwhile and that the chosen solutions are the best. To provide users with a virtual instrument, whereby they may estimate the feasibility of the astrophysical programme they have in mind and begin to plan their observations.

In the latter case, forward planning is absolutely necessary, both on Earth and in space, because observations are highly automated for reasons of efficiency and safety.

This instrumental model is generally put together during the project, on the basis of submodels which are each linked to some specific technical area and/or a specific type of knowhow. Ever more sophisticated computational tools now allow increasingly accurate simulations of the behaviour intrinsic to each of these areas. When an instrument is designed today, several different submodels are generally made, which we shall now discuss.

# Thermal Model

The aim is to calculate the temperature distribution, energy exchange, e.g., by conduction, radiation, or convection, transient departures from equilibrium and their evolution, and so on. This model is particularly important for spaceborne instrumentation, because of the extreme environmental conditions, and also in the infrared to submillimetre region where background radiation is a key problem and optical systems and especially detectors must be cooled to low temperatures.

# Mechanical and Thermoelastic Model

This is the model most familiar to us, since it uses computer aided design (CAD) software to produce usually 3D depictions, sometimes animated, which provide a concrete view of the instrument. The model is used to build a consistent mechanical architecture, choose materials, predict relative motions, calculate bending, distortion, and thermal expansion, and to estimate mechanical errors and tolerances in the manufacture of parts. Impressive software is available to visualise mechanisms and even to produce the digital codes required to command machine tools making the basic parts.

# Optical Model

The aim here is to calculate the paths of light rays from one optical component to the next, e.g., mirrors, lenses, prisms, etc., using the laws of geometrical optics, and generate the final point spread functions (PSF). Optical aberrations can be minimised and the best compromises achieved by optimising different characteristics of the optical components, such as refractive index, surface curvature, and so on. The model also helps to take into account the phenomena of physical optics, such as diffraction, scattering, dispersion, and reflections on optical surfaces, and to assess their various impacts. Many programs are available commercially. Among the most widely used are Zemax and Opticad. More subtle effects, or at least effects that are difficult to estimate roughly, can now be taken into account in models. An example is light pollution, often a critical issue in astronomy, which can now be modelled in a more and more realistic way using software, admittedly still somewhat cumbersome, to simulate secondary sources and reflections from the surfaces and edges of the mechanical structure (as described by textures and their microstructure), and to optimise the geometry of protective screens or baffles.

# Model of Detectors and Detection Chain

The aim here is to take into account, as realistically as possible, the pixel geometry, electrical response to the photon flux, efficiency as a function of wavelength, nonlinearity, pixel saturation and overflow effects, detector noise, dark current, pixel

cross-talk, electrical biases, and so on. Such models are often tailor-made, injecting a detailed knowledge of the detector built up from experience.

# Electrical Model

The development of both digital and analogue electronic circuits is more and more often accompanied by detailed simulations of their electrical behaviour. This is done using software exploiting a universal data bank that contains detailed characteristics of most components now on the market. In this way, without connecting up any real components, it then becomes possible to create a circuit, test it, refine the choice of components, generate realistic dynamic responses, and simulate its behaviour under extreme conditions, such as extreme temperature conditions, for example. An example of this kind of software is Spice, which is in the public domain and widely used. The special case of servosystems is often handled more functionally using dedicated software.

# Computing Model

This is rather a model for the computer architecture controlling and piloting the instrument. Software systems like Labview, are able to design genuine virtual instruments carrying out all the functions of a measuring instrument or combinations of several sub-instruments, along with their control by virtual control panels, i.e., screens with indicators, graphics, buttons, and cursors. Such software systems can assemble well defined functionalities and join them together by data exchange connections. The parameters of the instrument can be optimised by clicking on the buttons, and carry out data acquisition operations, while piloting the various functions of the instrument.

# Astrophysical Model

The characteristics of sources, such as their morphology, size, emission spectrum, environment, and so on, are generally supplied by an ad hoc model. This serves to check in a genuinely convincing way that, with the estimated level of performance, it really will be possible to achieve the initial astrophysical objectives. It also provides a way for future observers to prepare for their observations by working with a model of the source that is close to what is expected.

# Environmental Model

In some cases, this kind of model is also necessary in order to achieve the desired level of realism. This is the case in particular for instruments using an adaptive optics system, or optical interferometric arrays. In order to simulate their operation and estimate their performance, it is essential to use a model reproducing the spatial and temporal behaviour of atmospheric turbulence, along with vibrations of the telescope, the effects of wind on the outer structure, and so on.

![](images/9219ce17cb4fbdbd3f35d7739ead86fe545ec93dc51cd67f5cbc9ae76c7fe16c.jpg)  
Fig. 9.8 Raw CCD image of part of the first field of view observed by the COROT satellite in January 2007. Left: CCD image actually obtained. Right: Simulation on the basis of a detailed model of the detector, optics, and star catalogues. The striking likeness between the two images illustrates the quality that can now be achieved in instrument simulation. Images kindly provided by M. Auvergne, Lesia, Paris Observatory

Finally, all these submodels are put together into a global or end-to-end model. This general involves a command metalanguage that can interface the software building blocks described above, or rather their inputs and outputs, and put together a complete measurement chain from the celestial object emitting its radiation right down to correction for instrumental signatures and data compression. This model is often the basis for an exposure time calculator, provided for future observers to assess the feasibility of their scientific programme and the time required to carry out a specific observation in order to obtain a given level of performance, given the various constraints and random factors.

The level of realism that can be achieved today in global simulations of the measurement chain is illustrated in Fig. 9.8. This compares the simulated image of the first field of view observed by the photometric satellite COROT in January 2007 with the image that was actually obtained, without any correction. It is hard to find any difference at all between the simulation and the reality!

# 9.3 Overall Performance of an Observing System

This book has aimed at a systematic presentation of the different aspects of an observing system:

• Telescopes which collect light and form images, the phenomena of diffraction and coherence loss which affect the latter, and the way in which telescope arrays can improve them.

• Spectrometers which decompose and analyse radiation.   
• Detectors which transform the electromagnetic radiation received from celestial bodies into a signal that can be processed digitally.

As discussed in Chap. 1 and stressed again above, observation combines all these features into a single observing system, which may be exceedingly complex, whether Earth-based or spaceborne. While the performance and fundamental limitations of each subsystem, e.g., atmosphere, telescope, spectrometer, detector, etc., will have been carefully investigated in its turn, the final performance, which is after all the main concern of the astrophysicist, nevertheless results from the combination and compatibility of the subsystems. This is the role of the integration process leading to qualification of the instrument.

Performance estimates generally lead to a quantitative response to the following question: what is the faintest object that a particular system can observe, in a given time, with given spectral and angular resolutions, for a given polarisation, and with a given signal-to-noise ratio? However, the question may take other forms, such as: what is the fastest temporal fluctuation of a given object that can be observed with this system?

In this section, we shall give several examples to illustrate the way the overall performance of an instrument appears to the user. This is important because the user rarely has an intimate knowledge of the many complex subsystems making up the instrument, or even of their individual performance levels. The important thing is the final result.

# 9.3.1 Observing with the IRAM Millimetre Interferometer

Here we consider the millimetre interferometer of the Institut de radioastronomie millim´etrique on the Plateau-de-Bure in France, already presented in Sect. 6.5.1. What sensitivity can be obtained in spectral and angular resolution using this system, which consists of a high-altitude station $( 2 5 6 0 \mathrm { m } )$ equipped with 6 radiotelescopes of $1 5 ~ \mathrm { m }$ , detectors, and digital correlators, e.g., with a view to observing quasars? The first step is to visit the internet site7 which gives the characteristics in some detail. Table 9.2 provides a summary.

Table 9.2 Characteristics of the Plateau-de-Bure interferometer in 2007   

<table><tr><td>Number of telescopes</td><td>6</td></tr><tr><td>Telescope diameters Altitude</td><td>D=15m 2 560 m</td></tr><tr><td>Maximal baselines</td><td>N-S 230 m,E-W408 m</td></tr><tr><td>Receivers (per antenna)</td><td>81-115 GHz and 205-250 GHz</td></tr><tr><td>Correlators</td><td>8 units,resolution 0.39-2.5 MHz</td></tr></table>

# Detection Mode

For observation of a point source, i.e., unresolved with the chosen baseline configuration, and in the detection mode, i.e., aiming to extract a point source from the background, the sensitivity, defined as the signal leading to unit signal-to-noise ratio, is a value expressed in jansky (Jy) and given by the following expression, supplied by the IRAM website and easily derived from the considerations of Sect. 7.5:

$$
\delta S \ [ \mathrm { J y } ] = \frac { \rho _ { \mathrm { e } } T _ { \mathrm { s y s } } } { \eta _ { \mathrm { c } } \eta _ { \mathrm { p } } \eta _ { \mathrm { j } } \sqrt { N ( N - 1 ) } \sqrt { \delta \nu \delta t } } ,
$$

where the notation is explained as follows:

• $N$ is the number of antennas used in the chosen interferometric configuration.   
• $\delta \nu$ is the passband used, which determines the noise level.   
• $\ S t$ is the observation time. $T _ { \mathrm { s y s } }$ is the system temperature (see Sect. 7.5), taking into account atmospheric transmission $[ T _ { \mathrm { s y s } } \approx 1 5 0 \ : \mathrm { K }$ below a frequency of $1 1 0 \mathrm { G H z }$ , both in summer and winter]. $\rho _ { \mathrm { e } } ~ = ~ 2 k / \eta A$ is the efficiency of an antenna (or mirror), measured in Jy $\mathrm { K } ^ { - 1 }$ , Dwith $A ( \mathrm m ^ { 2 } )$ its area, $\eta$ its reflection efficiency, $k$ is Boltzmann’s constant $[ \rho _ { \mathrm { e } } \approx$ $2 2 \mathrm { J y K ^ { - 1 } } ]$ . $\eta _ { \mathrm { c } }$ is the correlator efficiency $\left[ \eta _ { \mathrm { c } } \approx 0 . 8 8 \right]$ .   
• $\eta _ { \mathrm { j } } = \mathrm { e } ^ { - \sigma _ { \mathrm { j } } ^ { 2 } / 2 }$ is the coherence loss, or instrumental decorrelation coefficient, due Dto phase instability of the local oscillator $[ \sigma _ { \mathrm { j } } \approx 4 ^ { \circ } ]$ . $\eta _ { \mathrm { p } } = \mathrm { e } ^ { - \sigma _ { \mathrm { p } } ^ { 2 } / 2 }$ is the coherence loss due to phase instability (or phase noise) of the Datmosphere above the instrument $[ \sigma _ { \mathrm { p } }$ depends on the baseline $B$ and atmospheric humidity, and is about $1 5 ^ { \circ }$ rms for $B \leq 1 0 0 \mathrm { m } ]$ .

The characteristic numerical values for the system around the frequency $9 0 ~ \mathrm { H z }$ (corresponding to $\lambda \ : = \ : 3 . 3 \mathrm { \ m m }$ ), as provided by IRAM, are specified in square Dbrackets. We then obtain the following result. Using the full interferometer configuration $N = 6$ baselines) for one hour of integration and with a spectral width $\delta \nu \ = \ 5 8 0 \ \mathrm { M H z }$ , the detection threshold $\delta S _ { \mathrm { t h r e s h o l d } }$ (unit signal-to-noise ratio) at $\lambda = 3 ~ \mathrm { m m }$ is between 0.4 and $0 . 8 \mathrm { m J }$ y depending on the atmospheric conditions.

![](images/e7917bcc25f4ae3599c1262894c4445231eff028e954b4316e2a4e79649d932e.jpg)  
Fig. 9.9 Point spread function (left, on a scale of arcsec) and spatial frequency coverage (right, on a scale of metres, dividing by $\lambda$ to obtain spatial frequencies $u$ and $\nu$ ) for the Bure interferometer in its highest resolution configuration, for two values ( $+ 4 0$ and $+ 2 0 ^ { \circ }$ ) of the declination $D$ of the source. Figure kindly provided by IRAM

# Imaging Mode

Now consider the interferometer operating in imaging mode. The choice of baseline configuration is dictated by the desired angular resolution. Assuming we select the highest value possible, i.e., around 0.6 arcsec at $\nu ~ = ~ 2 3 0$ GHz, Fig. 9.9 shows Dthe interferometer point spread function (PSF) and the coverage of the $u { - } \nu$ plane obtained with the corresponding arrangement of the six telescopes, depending on the declination of the observed source.

What sensitivity can be obtained in mapping mode for the same observation time? From the sensitivity $\ S S$ to a point source calculated above, the noise (rms value) in the brightness temperature (see Sect. 7.5) is given by

$$
\delta T _ { \mathrm { m } } = \frac { \lambda ^ { 2 } } { 2 k ( f \theta _ { 1 } \theta _ { 2 } ) } \delta S ,
$$

where $k$ is Boltzmann’s constant, $\theta _ { 1 }$ and $\theta _ { 2 }$ are the values in arcsec of the PSF axes (assuming the PSF to be close to an ellipse), and $f$ is a numerical factor close to unity and depending on the choice of apodisation (or tapering) mode used on the antenna lobes. With $\delta S$ as calculated above, $\lambda$ given in mm, and angles in arcsec (at

Table 9.3 Infrared imaging with the VLT (2007)ı 0   

<table><tr><td>UT4 telescope (Yepun)</td><td>D=8.2m</td></tr><tr><td>Location</td><td>24°40&#x27;S,7025&#x27;W,H=2 535 m</td></tr><tr><td>Adaptive optics (NAOS)</td><td>Cassegrain focus</td></tr><tr><td>Wavefront sensors</td><td>Visible (0.4-1.0 μm) and infrarouge (0.8-2.5 μm)</td></tr><tr><td>Reference star</td><td>mv ≤16.7 and m k ≤12</td></tr><tr><td>Maximal correction field</td><td>55 arcsec</td></tr><tr><td>Camera (CONICA)</td><td>1024×1024InSb array</td></tr><tr><td>Spectral region</td><td>1-5 μm</td></tr><tr><td>Modes</td><td>Imaging,polarimetry,spectroscopy,coronography</td></tr></table>

$9 0 \mathrm { G H z }$ , $\theta _ { 1 } = \theta _ { 2 } = 1 . 5$ arcsec), the result is

$$
8 T _ { \mathrm { m } } = 1 5 { \frac { \lambda ^ { 2 } } { f \theta _ { 1 } \theta _ { 2 } } } 8 S _ { \mathrm { t h r e s h o l d } } = 0 . 0 6 \mathrm { m K } .
$$

Once the observed sky region has been mapped, this value $\delta T _ { \mathrm { m } } = 0 . 0 6 \mathrm { m K }$ indicates Dthe noise level, hence the confidence interval relevant to the details of the map.

# Spectroscopic Mode

Let us now consider the interferometer operating in spectroscopic mode. If it observes an unresolved source, the bandwidth $\delta \nu = 5 8 0 ~ \mathrm { M H z }$ used for the above calculation of $\ S S _ { \mathrm { t h r e s h o l d } }$ Dmust be reduced to the spectral resolution used by the correlator (up to the maximal resolution of $0 . 3 9 ~ \mathrm { M H z }$ ). The same was true in imaging mode.

# 9.3.2 Observing with NAOS Adaptive Optics

Consider the imaging system operating at the diffraction limit in the near infrared, including one of the telescopes of the Very Large Telescope (C. Paranal, Chile), with its adaptive optics system NAOS, and the CONICA camera that follows it. The main characteristics of this system,8 which is just one of the many possible configurations of the VLT, are summarised in Table 9.3. However, this table only gives a very limited idea of the wide range of observation modes possible with the VLT–NAOS– CONICA system, since the observer manual contains more than a hundred pages, and it would not be possible to summarise all that here. The layout of the manual is typical of such a complex system, containing a description of the performance of each subsystem, and a presentation of all the instructions the observer must prepare prior to using the telescope, in the form of computer information sheets or templates, in order to minimise the decisions that need to be taken in real time, which can lead to handling errors, and in order to automate the observation procedure as far as possible. The aim is to reduce dead time and obtain the best possible use of nights when the weather is favourable, bearing in mind the high cost of telescope time.

The observation procedure must be prepared in the greatest detail, with the help of automated observing blocks, which break down into: acquisition of the source, i.e., locating the sky field that contains it, the observation itself, and calibration of the properties of the instrument and the atmosphere at the measurement time.

Since each subsystem involves many variables or possible configurations, e.g., atmospheric seeing, pixel size, spectral filters, dichroic elements separating the light between wavefront sensor and imaging camera, polarisers, and so on, many examples would be required to illustrate all these possibilities and their corresponding performance. We shall expand on just one of these here.

Consider the following project: to observe the galactic center $( { \mathrm { S g r A } } ^ { * } )$ and obtain an image of its immediate neighbourhood, in order to monitor the motions of the stars there in the gravitational field of the massive black hole, in the spectral band $K _ { s }$ $( 2 . 2 \mu \mathrm { m } )$ . What is the faintest magnitude $m _ { K }$ of such a star that can be observed?

• Adaptive Optics. While extinction eliminates any reference star in the visible, by pure chance there is a bright supergiant (IRS7) of magnitude $m _ { K } = 6 . 4$ at $9 ^ { \prime \prime }$ from $\operatorname { S g r A } ^ { * }$ D(see Fig. 6.24 in Sect. 6.3 for an image of this field). This can be taken as reference by using the infrared wavefront sensor (WFS), since the guide tells us that this has a radius of $5 5 ^ { \prime \prime }$ and limiting magnitude $m _ { K } = 1 2$ . The Strehl ratio $\mathcal { S } \approx 4 0$ is given as accessible at a distance $9 ^ { \prime \prime }$ D, and this is a good correction value. Since the reference star is bright, it suffices to use $20 \%$ of its flux for the WFS and to send $80 \%$ to the camera via a suitable dichroic component.

• Camera. There are two important choices to make: the field and the spectral band. Given the good value of $\mathcal { S } \approx 4 0$ , we may choose a pixel equal to the diffraction spot in the K band, with $\lambda / D = 5 4$ milliarcsec (mas). One of the Davailable cameras (S54) has a magnification leading to 54 mas per pixel and covering a field $5 6 ^ { \prime \prime } \times 5 6 ^ { \prime \prime }$ . Since the aim is to detect the faintest stars in the field of view, we use the filter with the greatest possible width $\Delta \lambda$ . Indeed, the sensitivity is determined here by the existence of atmospheric background radiation and thus varies as $\sqrt { \Delta \lambda }$ . In order to obtain the spectral type of these stars once detected, it could be interesting to use a spectroscopic mode with narrower filters, or a grism, while increasing the exposure time.

• Background Radiation. In the K band, the thermal background is negligible and it is OH emission that dominates. Under the conditions prevailing at the Paranal site, with the chosen dichroic, this background has brightness $\begin{array} { r l } { m _ { K _ { s } } } & { { } = } \end{array}$ 12:5 arcsec $^ { - 2 }$ D. It will thus have to be subtracted for observation of faint stars, by alternating observation of the field containing them with observation of a neighbouring field that is as empty as possible, in order to be able to carry out a sky subtraction during data compression. With the chosen pixel size, the background signal per pixel is reduced by a factor of $( 1 0 0 0 / 5 4 ) ^ { 2 } ~ = ~ 3 4 3$ corresponding to $2 . 5 \log _ { 1 0 } ( 3 4 3 ) = 6 . 3 4$ Dmagnitudes. It is thus equivalent to a star of magnitude $m _ { K _ { s } } = 1 8 . 8$ Dwith flux concentrated on this single pixel.

D• Detector. This InSb array $( 1 0 2 4 \times 1 0 2 6$ pixels), first implemented in 2004, has an excellent quantum efficiency $\eta \approx 0 . 8 – 0 . 9$ . The dark current (superposition of a slight thermal background produced by the instrument itself and the dark current of the photoconductor proper) is $0 . 0 5 { - 0 . 0 1 5 } \mathrm { A D U s ^ { - 1 } p i x e l ^ { - 1 } }$ . Dark frames must therefore be carried out, i.e., exposures with no signal, in order to subtract the pseudo-signal due to this current.9

• Signal. The photometric values of the standard star $\alpha$ Lyrae (Vega) are a monochromatic flux of $e _ { \lambda } = 4 . 3 \times 1 0 ^ { - 1 0 } \mathrm { W } \mathrm { m } ^ { - 2 } \mu \mathrm { m } ^ { - 1 }$ for a magnitude $m _ { K _ { s } } =$ 1:86 at $\lambda = 2 . 1 4 9 \mu \mathrm { m }$ ( $K _ { s }$ D band). With a telescope of area $S = \pi ( 8 . 2 ) ^ { 2 } / 4 \mathrm { m } ^ { 2 }$ Din the band $\Delta \lambda = 0 . 3 5 \mu \mathrm { m }$ D, a star with the same magnitude as the background, Di.e., 18.8, will thus give a signal of $1 . 3 6 \times 1 0 ^ { 4 } t$ photons $\mathrm { s } ^ { - 1 }$ , where $t$ is the overall transmission (atmosphere $^ +$ telescope $^ +$ instrument). With $t \approx 0 . 3$ and $\eta = 0 . 8 5$ , the current will be $3 5 0 0 \mathrm { e } ^ { - } \mathrm { s } ^ { - 1 }$ . With a gain of $1 1 \mathrm { e } ^ { - }$  Dper ADU, the background signal will be $3 1 8 \mathrm { \ A D U s ^ { - 1 } }$ and its quadratic fluctuation $1 8 \mathrm { H z } ^ { - 1 / 2 }$ .

With the Strehl ratio obtained here, about $50 \%$ of the energy of a star is focused on the pixel of the chosen size. For an exposure time of $1 \mathrm { m i n }$ , a star of magnitude 18.8 will give a signal of $1 5 9 \times 6 0$ ADU, whereas the background noise corresponds to $1 8 \times \sqrt { 6 0 }$ , or $\mathrm { S } / \mathrm { N } = 6 8$ . With this exposure time by integration on the CCD, and for $\mathrm { S } / \mathrm { N } = 5$ , the detection limit is then an object 13.6 times fainter, i.e., a magnitude $m _ { K _ { s } } = 2 1 . 6 .$ . This could be further improved by a longer exposure, up to a limit Ddetermined by pixel saturation due to the background.

# 9.3.3 Observing with the Photometric Satellite COROT

The satellite COROT, launched by the French space agency CNES in December 2007, is designed for very high accuracy photometry with the specific aim, for one of its two channels, of identifying extrasolar planets by the transit technique. The idea is to measure the reduced brightness of a star when one of the planets in its system passes between the star and the observer during a transit. Naturally, this assumes the rare situation in which the observer (COROT) is almost exactly in the orbital plane of the planet. What performance may we expect from COROT for the detection of extrasolar planets by this method? For example, what is the smallest planet that we could hope to detect in this way? The main features of the COROT system are summarised in Table 9.4.

Table 9.4 Main characteristics of the COROT satellite   

<table><tr><td>Telescope diameter</td><td>27cm</td></tr><tr><td>Focal length</td><td>1.2 m</td></tr><tr><td>Detector</td><td>2 CCD 20482</td></tr><tr><td>Pixel</td><td>13.5 μm</td></tr><tr><td>Readout noise (RON)</td><td>14 electrons</td></tr><tr><td>Elementary exposure time</td><td>32 s</td></tr><tr><td>Global efficiency</td><td>0.7</td></tr><tr><td>Relative dispersion of efficiency</td><td>.01</td></tr><tr><td>Pointing fluctuations</td><td>0.4 pixels</td></tr></table>

The sensor is a frame transfer CCD, so no time is lost during readout and the CCD detects photons all the time (see Sect. 7.4.6). There is no wavelength filtering, so in order to evaluate the signal, it is assumed that this is equivalent to simultaneously observing with the three juxtaposed filters B, V, and R of the Johnson photometric system (see Sect. 3.1), with central wavelengths $\lambda _ { \mathrm { B } } , \lambda _ { \mathrm { V } }$ , and $\lambda _ { \mathrm { R } }$ , respectively, and widths $\Delta \lambda _ { \mathrm { B } }$ , $\Delta \lambda _ { \mathrm { V } }$ , and $\Delta \lambda _ { \mathrm { R } }$ , respectively. To simplify, it is also assumed that the overall efficiency $\eta$ (optical $^ +$ quantum) of photon–electron conversion does not depend on the wavelength.

Consider two stars of solar spectral type G2V and apparent magnitude $m _ { V } = 1 0$ Dand 15, i.e., in the magnitude range covered by COROT. The Johnson colour indices for this spectral type are $\mathrm { B } - \mathrm { V } = 0 . 6 3$ and $\mathsf { V } - \mathsf { R } = 0 . 5 3$ . We begin by calculating the fluxes $f _ { \mathrm { B } } , f _ { \mathrm { V } }$ , and $f _ { \mathrm { R } }$  D of the star in each filter:

$$
\begin{array} { r l } & { f _ { \mathrm { B } } = F _ { \mathrm { B } } \times 1 0 ^ { - 0 . 4 ( m _ { \mathrm { V } } + \mathrm { B } - \mathrm { V } ) } , } \\ & { f _ { \mathrm { V } } = F _ { \mathrm { V } } \times 1 0 ^ { - 0 . 4 m _ { \mathrm { V } } } , } \\ & { f _ { \mathrm { R } } = F _ { \mathrm { R } } \times 1 0 ^ { - 0 . 4 ( m _ { \mathrm { V } } - \mathrm { V } + \mathrm { R } ) } , } \end{array}
$$

where $F _ { \mathrm { B } } , \ F _ { \mathrm { V } }$ , and $F _ { \mathrm { R } }$ are the reference fluxes in $\mathrm { W } \mathrm { m } ^ { - 2 } \mu \mathrm { m } ^ { - 1 }$ of a star of magnitude $\begin{array} { r l r } { m _ { \mathrm { V } } } & { { } = } & { 0 } \end{array}$ . The next task is to evaluate the total number $N _ { \mathrm { t o t } }$ of Dphotoelectrons produced during an exposure time $\tau$ by making the reasonable approximation that the filters are narrow enough to ensure that, in a filter, the energy of each photon corresponds to the average wavelength of the filter. Then

$$
N _ { \lambda } = \pi \frac { D ^ { 2 } } { 4 } \tau \gamma F _ { \lambda } \Delta \lambda \frac { c \lambda } { h } ,
$$

and

$$
N _ { \mathrm { t o t } } = \pi \frac { D ^ { 2 } } { 4 } \tau \gamma \frac { F _ { \mathrm { B } } \lambda _ { \mathrm { B } } \Delta \lambda _ { \mathrm { B } } + F _ { \mathrm { V } } \lambda _ { \mathrm { V } } \Delta \lambda _ { \mathrm { V } } + F _ { \mathrm { R } } \lambda _ { \mathrm { R } } \Delta \lambda _ { \mathrm { R } } } { h / c } .
$$

We thus obtain $N _ { { \mathrm { t o t } } } = 3 . 1 6 \times 1 0 ^ { 6 }$ for $m _ { \mathrm { V } } = 1 0$ and $N _ { { \mathrm { t o t } } } = 3 . 1 6 \times 1 0 ^ { 4 }$ for $m _ { \mathrm { V } } = 1 5$ .

Table 9.5 Change in the number of photoelectrons during a transit for two different planet sizes and two cumulative exposure times   

<table><tr><td>mv</td><td>Jupiter,32 s</td><td>Earth,32 s</td><td>Noise</td><td>Jupiter, 4 h</td><td>Earth, 4 h</td><td>Noise</td></tr><tr><td>10</td><td>2.32×104</td><td>232</td><td>1.78×10</td><td>1.04×107</td><td>1.04×105</td><td>3.78×104</td></tr><tr><td>15</td><td>232</td><td>2.3</td><td>177</td><td>1.04 × 105</td><td>1.04 × 103</td><td>3.78×103</td></tr></table>

We now estimate the change $\Delta N$ in the number of photoelectrons received during an elementary exposure when the planet passes in front of the stellar disk. If the radius of the planet is $R _ { \mathrm { P } }$ and the radius of the star is $R _ { S }$ , we have

$$
\Delta N = N _ { \mathrm { t o t } } \left( { \frac { R _ { \mathrm { P } } } { R _ { \mathrm { S } } } } \right) ^ { 2 } .
$$

Table 9.5 sums up the results for $R _ { \mathrm { S } } = 7 . 0 { \times } 1 0 ^ { 8 } \mathrm { k m }$ , $R _ { \mathrm { P } } = 6 0 0 0 0 \mathrm { k m }$ (an exoplanet like Jupiter) and $R _ { \mathrm { P } } = 6 0 0 0 { \mathrm { k m } }$ D  D (an exoplanet like Earth), comparing then with the P D   photon noise of the star alone, which is simply $b _ { \mathrm { S } } = N _ { \mathrm { t o t } } ^ { 1 / 2 }$ .

DLet us now examine the various sources of noise or error affecting the measurement. Note first that the image spot of a star is spread over about 80 pixels, due to a slight defocusing, designed to limit problems of saturation and reduce the noise due to small pointing fluctuations.

# Readout Noise

If for reasons of convenience we choose to sum the pixels over a square of $1 0 \times 1 0$ pixels, centered on the star spot, the readout noise $n _ { \mathrm { R } }$ of the measurement will be $n _ { \mathrm { R } } = ( 1 0 \times 1 0 ) ^ { 1 / 2 } \times R O N = 1 4 0 \mathrm { e } ^ { - }$ .

# Background Photon Noise

For reasons associated with the choice of orbit, COROT’s pointing direction must lie in a plane close to the ecliptic, so the zodiacal light (light from the Sun reflected by tiny particles in the plane of the Solar System, see Sect. 2.9) is an important source of spurious radiation. Its specific intensity $I _ { \lambda }$ is $2 6 0 { \times } 1 0 ^ { - 8 } \mathrm { W } \mathrm { m } ^ { - 2 } \mu \mathrm { m } ^ { - 1 } \mathrm { s r } ^ { - 1 }$ . The number $N _ { Z }$ of photoelectrons due to zodiacal light detected in the $1 0 \times 1 0$ square during the elementary exposure time is given by $N _ { \mathrm { Z } } = 3 6 8 0 0 \mathrm { e } ^ { - }$ and the corresponding photon noise is $n _ { \mathrm { Z } } = N _ { \mathrm { Z } } ^ { 1 / 2 } = 1 9 \mathrm { i e } ^ { - }$ .

# Pointing Noise

A further source of noise can be ascribed to small changes in the satellite pointing and this must also be taken into account. The image spot moves over the CCD which does not have uniform response, and this induces changes in the measurements. The effect can be reduced by the defocusing of the image on the CCD already mentioned.

Table 9.6 Noise assessment for the COROT satellite. The table sums up the various contributions (in $\mathrm { e } ^ { - } \mathrm { r m s } )$ ) to the total noise for two different stars $( m _ { \mathrm { V } } )$ and an integration time of $4 \mathrm { h r }$   

<table><tr><td>Readout noise</td><td>Pointing noise</td><td>Zodiacal noise</td><td>Star photon Jupiter noise</td><td>signal</td><td>Earth signal</td></tr><tr><td colspan="6">mv=10 2.97 ×103 1.70 ×1044.05×103.77×1041.31×1071.05×105</td></tr><tr><td colspan="6">Source photon noise dominates and all planets are detectable</td></tr><tr><td colspan="6">mv =15</td></tr><tr><td colspan="6"></td></tr><tr><td colspan="6"></td></tr><tr><td colspan="6">2.97 ×10²1.70 ×10²4.05×10²3.77×10²1.31×101.05×10²</td></tr><tr><td colspan="6">Zodiacal photon noise dominates and only planets of Jovian dimensions are detectable</td></tr><tr><td colspan="6"></td></tr></table>

Consider a small displacement $\delta$ (a fraction of a pixel) of the spot. The surface area not shared by the two spots is then $4 R \delta$ , where $R$ is the radius of the spot in pixels. On average, the relative change $\Delta N / N$ in the number of photoelectrons for a pixel at the edge of the spot is then

$$
\frac { \Delta N } { N } = \frac { 4 \delta } { ( \pi R ) ^ { 2 } } .
$$

The normalised quantum efficiency or flat field of the pixels can be treated as a normal random variable centered on 1 and with standard deviation $\sigma$ . The corresponding noise $n _ { \mathrm { D } }$ , i.e., the standard deviation of the change in the number of photoelectrons due to pointing fluctuations is then

$$
n _ { \mathrm { D } } = { \delta N \sigma } ( 2 \pi R ) ^ { 1 / 2 } ,
$$

so that, with $R = ( 8 0 / \pi ) ^ { 1 / 2 }$ , $\sigma = 0 . 0 1$ , and $\delta = 0 . 4$ pixel, we have $n _ { \mathrm { D } } = 8 0 1 \mathrm { e } ^ { - }$

D D DTable 9.6 sums up the different noise sources $n _ { \mathrm { S } } , n _ { \mathrm { Z } } , n _ { \mathrm { R } }$ , and $n _ { \mathrm { D } }$ D, for the cases $m _ { \mathrm { V } } ~ = ~ 1 0$ and $m _ { \mathrm { V } } ~ = ~ 1 5$ , for a cumulative measurement time of $4 \ \mathrm { h r }$ . It is thus D Daffirmed that COROT has the capacities required to detect planets much smaller than Jupiter, and indeed it did as proven by the detection of Corot-7b a planet with R 1:7REarth.

# 9.3.4 Observing with a Coded Mask Gamma-Ray Instrument

Consider the IBIS/ISGRI instrument on board the INTEGRAL satellite.10 This uses a coded mask to form images, as described in Sect. 5.2.5. The image, which is recorded on board, comprises a background and the superposition of shadows of the mask projected by all the sources in the field of view. A pseudo-image of the sky and the $\gamma$ ray sources it contains is thereby formed by correlation between the recorded image and a decoding or inverse matrix deduced from the pattern of the coded mask.

Let $\mathcal { M }$ be the matrix representing the mask, made up solely of ones (transparent elements) and zeros (opaque elements). The image formed on the detector is the convolution of the sky image $\mathcal { S }$ and $\mathcal { M }$ , to which the background noise $\mathcal { B }$ must be added:

$$
{ \mathcal { D } } = S \star { \mathcal { M } } + { \mathcal { B } } .
$$

If $\mathcal { M }$ has an inverse $\mathcal { G }$ such that $\mathcal { M } \star \mathcal { G } = \delta$ , we find

$$
\mathcal { S } ^ { \prime } = \mathcal { D } \star \mathcal { G } = \mathcal { S } \star \mathcal { M } \star \mathcal { G } + \mathcal { B } \star \mathcal { G } = \mathcal { S } \star \delta + \mathcal { B } \star \mathcal { G } = \mathcal { S } + \mathcal { B } \star \mathcal { G } ,
$$

and ${ \mathcal { S } } ^ { \prime }$ only differs from $\mathcal { S }$ by addition of the term $\mathcal { B } \star \mathcal { G }$ . When the mask carries a cyclic repetition of the same basic pattern and the background $\mathcal { B }$ is uniform, the term $\mathcal { B } \star \mathcal { G }$ is a constant that can be ignored. In practice, if the background is not uniform but its structure is known, the image $\mathcal { D }$ can be corrected to make the background uniform. Replication of the basic pattern, which allows one to obtain a fully coded field, implies the existence of a strong correlation between the partial patterns projected by sources separated by an angle equal to the one subtended by the basic pattern of the mask at the detector.

Deconvolution will therefore produce a ghost of the main source at each of these positions. For a basic pattern that is square and a fully coded source, there will be 8 main ghosts11 located in the middle of the sides and at the corners of a square surrounding the actual position of the source. If the source is partially coded, only a part of the ghosts will be visible. Since each source produces up to 9 peaks (8 ghosts plus the source) in a deconvoluted image, a field containing more than 3 sources will produce an extremely confused image in which it will be hard to detect faint sources. It may also be that one source is hidden by the ghost of another. It is thus important to exorcise the ghosts.

This is done using an iterative process, similar to the CLEAN method used in radioastronomy (see Sect. 6.4.5). This process, shown in Fig. 9.10, consists in identifying the brightest source, modelling the point spread function at the position of the source, and subtracting it from the image. This process is repeated until there is no longer any significant source. The main peak of the point spread function is then added at the position of each of the sources found in this way.

Since INTEGRAL is an observatory, there is a committee in charge of allocating observing time to those who respond to a yearly call for tender. The latter, published by the European Space Agency, comes with documentation and computing tools to help the astronomer work out an appropriate duration and strategy for observation in order to achieve his or her objectives. With the exception of $\gamma$ ray bursts and extremely bright sources, the count rate of coded mask instruments is dominated by the instrumental background. The sensitivity, or more precisely, the minimum detectable flux, is thus limited by background noise. Let $B ( E )$ be the background count rate in an energy band $E$ of width $\delta E$ , $\ S t$ the observing time, $A ( E )$ the detection area, $\epsilon _ { \mathrm { i } }$ the imaging efficiency, $\epsilon _ { \mathrm { p } } ( E )$ the detection efficiency in the total absorption peak, $\eta _ { 0 } ( E )$ the transparency of the mask and $\eta _ { 1 } ( E )$ the transparency of the holes in the mask. The detection sensitivity for a point source, expressed in $\mathrm { c m } ^ { - 2 } \mathrm { s } ^ { - 1 } \mathrm { k e V } ^ { - 1 }$ , for a signal level $n$ times stronger than noise of standard deviation $\sigma$ , is well approximated by

![](images/9c9f1574d3b77dd83f4702d5cddda2eb87b4b37fa5aa299138d21e73c0adc062.jpg)  
Fig. 9.10 Illustration of the image cleaning process for IBIS/ISGRI. Left: Images of the detector at different stages in the process, going from top to bottom. Right: Deconvoluted images corresponding to the images of the detector. Top line: Images from the detector and sky background at the beginning of the process. Second line: Images obtained after background substraction. Third line: Images resulting from subtraction of the brightest source (Cygnus X-1). Bottom left: Detector image after subtracting the second brightest source (Cygnus X-3). Bottom right: Final image obtained by deconvoluting the detector image on the left and adding the central peak of the point spread function at the position of each of the sources

$$
S = \frac { 2 n \sqrt { B ( E ) \delta t } } { \epsilon _ { \mathrm { i } } \epsilon _ { \mathrm { p } } ( E ) ( 1 - \eta _ { 0 } ) \eta _ { 1 } A \delta t \delta E } .
$$

The imaging efficiency $\epsilon _ { \mathrm { i } }$ results from imperfect sampling of the mask shadow. In the best possible case, it is given by $( 1 - 1 / 3 R )$ , where $R$ is the ratio between the size of the basic element of the mask and the size of a detector pixel ( $R = 2 . 4 3$ for IBIS/ISGRI).

In the case of ISGRI, for $E$ in the range $2 0 { \mathrm { - } } 4 0 \ \mathrm { k e V } ,$ , $B ~ \approx ~ 1 5 0 ~ \mathrm { s } ^ { - 1 }$ , $A \ \approx$ $2 0 0 0 ~ \mathrm { c m } ^ { 2 }$ , $\epsilon _ { \mathrm { i } } ~ = ~ 0 . 8 6$ , $\epsilon _ { \mathrm { p } } \approx 0 . 9$ , and $\eta _ { 0 } ~ = ~ 0$ , $\eta _ { 1 } \approx 0 . 8$  . For an exposure time of $1 0 ^ { 6 }$ D s (about 10 days), at the $3 \sigma$ D detection level, we may thus expect a sensitivity of the order of $3 \times 1 0 ^ { - 6 } \mathrm { \ c m ^ { - 2 } s ^ { - 1 } k e V ^ { - 1 } }$ , or around 3 000 times less than the flux from the $\gamma$ ray source in the Crab nebula, a supernova remnant. This is sometimes expressed by referring to a sensitivity equal to one third of a milliCrab.

# 9.4 Removing Instrumental Signatures

An astrophysical measurement is always affected by several forms of bias and uncertainty. Some are intrinsic to the measurement, such as photon noise, and are almost impossible to control other than by increasing the integration time, while others are related to imperfections in the instrumental chain and can usually be taken into account to improve the accuracy of the measurement and thereby make it as close as possible to the fundamental limits. In this section, we discuss the set of operations designed to deal with the latter problem during data reduction, and referred to as correction for the instrumental signature.

Since it would be impossible to give an exhaustive account for the whole panoply of instrumentation used in observational astrophysics, we shall focus on instruments used in the visible and near infrared, a spectral region in which the strategy employed to remove instrumental signatures has been well established and appeals to relatively standardised tools. Similarly inspired processes are implemented in the observational protocols applied at radiofrequencies and high energies (X and $\gamma$ rays).

The term bias refers to any spurious signal adding systematically to the photosignal from the source. This may be sky background emission, detector dark current, detector voltage interference, light pollution, ghost images, diffraction spikes, and so on.

For their part, uncertainties correspond to some random feature affecting each measurement. This may be statistical noise, scintillation, temporal variations in atmospheric transmission and emission, variations in quantum efficiency between detector pixels or transmission over the field, or impacts by cosmic rays. In addition, these two families of phenomena are not mutually independent. For example, there is random noise associated with a dark current.

# 9.4.1 Intrinsic Emission from the Instrument

While the night sky is not actually truly dark at infrared and millimetre wavelengths (see Sect. 2.3), the situation gets worse due to the instrument itself, and in particular its thermal emission, which makes a major contribution to the background radiation picked up by the detector. This background can even become much brighter than the target sources. Such emission is spatially structured owing to non-uniformities in the beam and the different emissivities of the various parts of the instrument, and it is also time variable. It must therefore be included in the instrumental signature.

To limit this signature, at least to first order, the solution is to carry out another measurement on an empty sky region and then subtract it. In doing so, it should not be forgotten that the statistical noise of the photoelectrons due to the sky or the instrument cannot be subtracted in this operation. Quite the opposite, in fact: the variance of this noise will be doubled. In order to measure the reference sky region faster than the typical time of its variation, which is generally a fraction of a second, the beam is switched between the two positions, either by offsetting the telescope, or by using an oscillating secondary mirror, which is faster. This is known as chopping.

In the latter case, since the telescope optics is also emissive, displacing the beam on the primary mirror will induce a further undesirable signal due to dust or other inhomogeneities. A structured background is thus superposed on the sky image. One then evaluates this contribution, which is due only to the rapid chopping, by regularly offsetting the telescope itself to some other region of the sky. This is the basic principle of nodding. Correction for this particular signature is thus achieved by carrying out a double subtraction, as shown in Fig. 9.11.

# 9.4.2 Dark Current

This signal corresponds to the charges produced in the detector by thermal excitation, even in the absence of any photons. For example, in a photosensitive semiconducting material, the probability of producing an electron–hole pair is proportional to the quantity $T ^ { 3 / 2 } \exp ( - E _ { \mathrm { g a p } } / 2 k T )$ , where $E _ { \mathrm { g a p } }$ is the energy difference or gap between the valence band and the conduction band, i.e., $E _ { \mathrm { g a p } } =$ $h \nu _ { \operatorname* { m i n } } ~ = ~ h c / \lambda _ { \operatorname* { m a x } }$ , where $\lambda _ { \mathrm { m a x } }$ Dis the wavelength beyond which the detector is Dno longer sensitive. For silicon, the photosensitive material used to make CCDs, $\lambda _ { \operatorname* { m a x } } = 1 . 1 5 \mu \mathrm { m }$ (see Sect. 7.3). More charges are thus produced as $T$ increases and Dthe threshold decreases, whence the cutoff wavelength of the detector is longer. This is why infrared detectors always have larger dark current than visible wavelength detectors. The longer the operating wavelength, the more they must be cooled (see Sect. 7.4.7). Since the dark current produced after a given integration time differs slightly from one pixel to another, a structure signature appears, superimposed on the photon signal. It is generally reproducible if the detector temperature is well stabilised. This signature, which may be quite significant in the infrared, is simply removed by carrying out measurements with the shutter closed for the same time as the sky observation, then subtracting the resulting signal.

![](images/73581cdc188b6ca7b2a608fa9e78acbaf66be926ea90742c677fd58c1dc5a4c2.jpg)  
Fig. 9.11 Chopping. The shaded background in the detector field, represented by a disk, represents variable emission from the sky background, from which the star signal must be extracted. A, B, and C are different positions of the field on the sky. $( \mathrm { A } - \mathrm { B } )$ and $\left( \mathbf { B } ^ { \prime } - \mathbf { C } \right)$ represent chopping, while their difference $( \mathbf { B } ^ { \prime } - \mathbf { C } ) - ( \mathbf { A } - \mathbf { B } )$  leaves only twice the source signal, having eliminated the sky background (nodding)

There are two things to note here. First of all, it is important to remember that subtracting the dark charge does not remove the statistical uncertainty associated with it. It is thus always useful to reduce this effect as much as possible by cooling the detector. The second point is that an accurate value for the dark charge is obtained by accumulating many measurements, and thereby reducing statistical noise.

# 9.4.3 Non-Linearity Defects

The non-linearity of the detector is another example of instrumental signature which must often be taken into account. The response of a detector always saturates above a certain level of photon signal called the saturation threshold. It is thus important never to exceed this threshold. However, the response generally starts to become non-linear at a lower level than this threshold. The aim is usually to remain well below this limit to ensure that the measurement can be given a simple interpretation in terms of light flux. If the detector is in fact non-linear over its whole operating range, the measurement must then be corrected for this non-linearity. This is therefore established by prior laboratory measurements, e.g., by observing a source, usually calibrated, but most importantly, highly stable, and by increasing the exposure time in precise steps in order to explore the whole signal range.

# 9.4.4 Bias

In general, even for zero exposure time and closed shutter, a non-zero signal is measured at the detector output, varying from one pixel to another. This bias has several origins. It depends on the controlling electronics and/or effects within the detector, such as impurity levels, voltages arising at the junctions, and characteristics of the readout circuit integrated within the detector.

The bias is measured by carrying almost zero exposures which are averaged and can be subtracted from the image made on the object. In fact, this operation is rarely necessary, because this undesirable signal is necessarily included in the measurement of the dark charge and is therefore subtracted along with that.

# 9.4.5 Light Interference

Bright sources in the field or close to the sighting axis, such as the Moon or stars, can produce ghost images, caused by unwanted reflections on the optical surfaces, in particular in dioptric systems. These images, which correspond to longer optical paths, are generally out of focus and appear in the form of a halo reproducing the shape of the pupil. Figure 9.12 gives an example of this type of artifact in an image obtained using the MEGACAM camera at the prime focus of the Canada–France–Hawaii telescope.

Ghost images arising from off-axis sources are difficult to anticipate and remove because they vary over time (relative motions of celestial objects or field rotation) and they depend on the finer details of the pointing direction. For example, microscanning can introduce ghost images which move significantly on the field.

Diffraction by the arms of the spider holding the secondary mirror of the telescope in place produces spikes on the brighter star images which can also perturb measurements (see Fig. 9.12). In an equatorially mounted telescope, the resulting pattern is fixed and can be subtracted from one exposure to another using a measurement on a bright star. However, for a telescope with altazimuth mounting, rotation of the field and pupil renders this operation impossible, or at least much less efficient.

![](images/a66d3f4ac76dca54f632d67d4d4ec84512e69ebed6c76813927954872ca9dc63.jpg)  
Fig. 9.12 Part of an image of a very deep field obtained with the MEGACAM camera at the focus of the Canada–France–Hawaii telescope. Note two types of artifacts around the bright stars. First, there are two extended and overlapping halos due to unwanted reflections on the lenses of the focal reducer. These are circular and reproduce an image of the telescope pupil with its central obstruction. Then there are spikes in the shape of a cross. These result from the diffraction of light on the arms of the spider which holds the mechanical structure in which the camera is installed at the primary focus

# 9.4.6 Flat Field Corrections

This instrumental signature reflects a combination of non-uniformities in the detector quantum efficiency and the optical transmission over the field. It is also sometimes called fixed spatial noise. Indeed, if we observe a scene with perfectly uniform brightness, the measurement will nevertheless produce a spatial fluctuation in the signal from one pixel to another, and generally in a reproducible way. This is in fact a multiplicative effect, as indeed are non-linearity defects, since this noise is proportional to the flux of the uniformly bright source. To correct for this, several techniques can be combined. The first is to observer a scene of highly uniform brightness and then to divide by its median in order to produce the normalised flat field by which to divide all our images.

Certain precautions must be taken. Firstly, a good flat field must be affected by much less noise than the noise it is supposed to correct for. It must therefore be built up from a very large number of photocharges per pixel. This will involve adding up a large number of exposures, each with an average value close to the maximum number of charges that can be stored per pixel. Secondly, the flat field must be obtained using the whole optical train, including the telescope, so that nonuniformities in the optical transmission can be eliminated. A region of the sky observed at sunrise or sunset is generally considered to provide a good flat field source.

In order to limit the effects of differential response, a second technique is to carry out a microscan, i.e., displacing the telescope by a few pixels, usually in a random manner, from one exposure to the next. The image is reconstructed by recentering numerically to the nearest fraction of a pixel before adding up the exposures. A given region of the sky is thereby viewed by several different pixels and the average of their response reduces the variance of the spatial noise.

Another technique is time delay integration, specific to CCD detectors. In this mode, the scene is allowed to drift across the detector in the direction of the CCD rows, e.g., stopping the telescope motion, while ensuring charge transfer from pixel to pixel at exactly the same speed as the image drift. In this way, a source contributes to the construction of a photocharge throughout the scan on the CCD, but having successively illuminated a very large number of different pixels whose responses are thus averaged. This technique is used in the SLOANE sky survey and it is the one planned for the astrometric satellite GAIA.

# 9.4.7 Defective Pixels

A panoramic detector is never perfect. Owing to microscopic pollution during the manufacturing process or following deterioration by high energy particles, several pixels may become inoperative (dead pixels) or noisier, or they may produce a large dark current (hot pixels). These defects can be corrected for by exploiting the microscanning technique mentioned above. During an exposure, when the flux from one sky region has not been measured because it corresponds to a dead pixel, a good approximation can nevertheless be obtained by averaging the other spatially shifted measurements, i.e., having displaced the position of the dead pixel. If the microscanning technique cannot be implemented, an acceptable estimate of this flux can still be given by averaging the eight pixels surrounding the defective pixel. This does of course assume that image sampling has been correctly chosen with regard to its spatial frequency content (see Sect. 9.1.3).

# 9.4.8 Effects of High Energy Particle Impacts

High energy cosmic rays continually bombard our environment with a frequency that increases with altitude and hence becomes significant for many modern observatories. Indeed, it is always significant for satellites (see Sect. 2.9). When these particles deposit their energy in the bulk of the detector substrate, they create thousands of unwanted charges that are quite indistinguishable from photocharges. This effect increases with the thickness of the photosensitive material. In general, a particle only affects a single pixel on a CCD, but with the thicker infrared detectors, cosmic particle impacts can leave a trail across several pixels. The image produced by a very long exposure is thus scattered with bright pixels, namely those that have been impacted. The most effective solution here is to divide the exposure into several short exposures in order to be able to identify the measurements that must be rejected for a given pixel before addition. It is nevertheless important not to fall into the trap of making the exposures too short, for they would then be limited by readout noise.

# 9.5 The Problem of Estimation

Chance and randomness are everywhere. Humans would certainly have noticed this very early on in their evolution, and it must have been commonplace to note that, during a series of apparently identical experiments, different results were always obtained. Indeed, this same observation would have inspired games of chance, so widespread in all civilisations. On the other hand, it seems that the idea that chance could itself obey laws was one that long escaped the wisdom of our ancestors. There does appear to be a component to natural phenomena that fluctuates about an unchanging part, but it was not until the advent of probability theory and its laws that it became possible to estimate this invariable part.

When probability theory came upon the experimental scene, it imposed its way of viewing things: an observation is a realisation of one or more random variables which obey an underlying distribution, e.g., the normal distribution. This distribution is governed by unknown parameters $\theta _ { k }$ , e.g., its average and standard deviation. And it is these parameters that often form the ‘unchanging part’ of the phenomenon mentioned above, and which constitute the information to be extracted from the noise. This is the approach of statistical data processing, and more precisely the theory of estimation to be discussed in this chapter.

# 9.5.1 Samples and Statistics

Theoretically, statistical data processing is based on probability theory, but it uses a different vocabulary to refer to its basic objects. From a statistical standpoint, a set $( X _ { 1 } , \ldots , X _ { n } )$ of $n$ random variables is a sample and $n$ is its size. We then say that we have a sample of size $n$ , or an $n$ -sample. A set $( x _ { 1 } , \ldots , x _ { n } )$ of $n$ numbers from this $n$ -sample is called an realisation or an observation of this sample. The probability distribution of the random variables $X _ { i }$ is called the parent population. Finally, in order to support their decisions, statisticians use functions $g ( X _ { 1 } , \ldots , X _ { n } )$ of the random variables $X _ { i }$ which they call statistics.

# Example: Typical Problem Expressed in the Language of the Statistician

An experiment has led to the observation of $n$ numbers $( x _ { 1 } , \ldots , x _ { n } )$ , identified as one realisation of an $n$ -sample $( X _ { 1 } , \ldots , X _ { n } )$ . We assume that the $n$ -sample comprises independent random variables resulting from the same parent population with mean $\mu$ . In order to estimate $\mu$ , we propose to use the statistic

$$
g ( X _ { 1 } , \ldots , X _ { n } ) = { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } X _ { i } .
$$

This statistic, often denoted by $\overline { { X } }$ , leads to an estimate for the mean $\mu$ by the arithmetic mean of the $x _ { i }$ , viz.,

$$
{ \overline { { x } } } = { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } x _ { i } .
$$

This is a reasonable choice since a result from probability theory, namely the law of large numbers, asserts that $\overline { { X } }$ converges almost surely to $\mu$ when the sample size tends to infinity.

# 9.5.2 Point Estimation

In order to estimate the unknown parameters of a parent population, we use functions $\delta ( X _ { 1 } , \ldots , X _ { n } )$ of the sample called estimators No? These are statistics. An estimator for $\theta$ constructed using a sample of size $n$ is traditionally denoted by ${ \widehat { \theta } } _ { n }$ , while an estimator of $\tau ( \theta )$ is denoted by $T _ { n }$ , but note that in general, $T _ { n } \neq \tau ( \widehat { \theta } _ { n } )$ . ¤A realisation of these estimators will be called an estimate. An estimator is thus a random variable, whereas an estimate is a number. However, they will be denoted by the same symbol. Finally, to simplify, the sample $( X _ { 1 } , \ldots , X _ { n } )$ will often be denoted simply by $X$ and its realisation $( x _ { 1 } , \ldots , x _ { n } )$ simply by $x$ .

The problem of point estimation is to specify what is to be understood by a good estimator of the unknown parameter $\theta$ or a function $\tau$ of this parameter. This amounts to choosing, among all the different ways $\delta ( X )$ of combining the data, the one for which there are good reasons for preferring it above all others. Since the estimation of $\tau ( \theta )$ covers the case of $\theta$ itself, we shall consider only the first case, and let $\displaystyle { \delta ( X ) }$ denote the estimator of $\tau ( \theta )$ .

# 9.5.3 Elements of Decision Theory

In order to motivate the above considerations, it is useful to introduce some objective criteria for comparing estimators. These criteria are taken from decision theory, which we shall outline below.

# Estimation Error

The first thing to do is to define an estimation error. The error involved in estimating $\tau ( \theta )$ by $\displaystyle { \delta ( X ) }$ is $\delta ( X ) - \tau ( \theta )$ . If the error is positive, then $\tau ( \theta )$ is overestimated, and otherwise it is underestimated.

# Loss Function

One must then face the consequences of estimation errors. This is the role of the loss function, which specifies the cost associated with these errors. This function $L ( \theta , t )$ is positive and its value is the ‘price to pay’ for the estimation errors. It is zero if and only if $t = \theta$ . For largely practical reasons, the quadratic loss function is often chosen:

$$
L { \big ( } \tau ( \theta ) , \delta ( X ) { \big ) } = { \big [ } \delta ( X ) - \tau ( \theta ) { \big ] } ^ { 2 } .
$$

# Risk

Estimators are random variables and as such are likely to yield different outcomes from one experiment to another. In order to be able to compare them, one must have a global measurement that takes into account all the possible outcomes of these variables, and risk is the notion that fulfills this demand. The risk $R$ is the expectation value of the loss function:

$$
R ( \theta , \delta ) = \operatorname { E } \{ L { \big ( } \theta , \delta ( X ) { \big ) } \} .
$$

The expectation refers to all possible values of the sample $X$ , so the risk is a function of $\theta$ . If the loss function is quadratic, the risk attached to the estimator $\displaystyle { \delta ( X ) }$ for $\tau ( \theta )$ is the mean squared error of $\displaystyle { \delta ( X ) }$ about $\tau ( \theta )$ , or

$$
R { \big ( } \tau ( \theta ) , \delta ( X ) { \big ) } = \operatorname { V a r } { \big ( } \delta ( X ) { \big ) } + { \Big [ } \mathrm { E } { \big \{ } \delta ( X ) - \tau ( \theta ) { \big \} } { \Big ] } ^ { 2 } .
$$

The quantity $\Vdash ( \delta ( X ) )$ is the variance of $\displaystyle { \delta ( X ) }$ and $\operatorname { E } \{ \delta ( X ) - \tau ( \theta ) \}$ is called the bias.

# Partial Ordering of Estimators

When comparing two estimators for $\tau ( \theta )$ , we shall say that $ \delta _ { 1 }$ is better than $\displaystyle { \delta _ { 2 } }$ in the sense of risk if

$$
\forall \theta , \quad R \big ( \tau ( \theta ) , \delta _ { 1 } \big ) < R \big ( \tau ( \theta ) , \delta _ { 2 } \big ) .
$$

This ordering relation ‘is better than’ is only a partial ordering. The condition cannot be satisfied for all $\theta$ and the estimators are not then comparable. The obvious question here is this: for a given loss function, is there a best estimator, better than all others in the sense of risk?

In fact, no estimator can fulfill this requirement. Indeed, consider the trivial estimator $ \delta _ { 0 }$ which, regardless of the value of $X$ , declares that $\delta _ { 0 } ( X ) ~ = ~ \tau ( \theta _ { 0 } )$ , where $\theta _ { 0 }$ is an arbitrary value. The risk attached to $ \delta _ { 0 }$ Dwill generally be very high, unless we should happen to have $\theta = \theta _ { 0 }$ , in which case it will be zero. No other


<!-- chunk 0009: pages 561-630 -->
estimator can then be better than this one for $\theta _ { 0 }$ , so there is no estimator that is preferable to all the others in the sense of the above partial ordering.

The problem is that we were trying to compare a candidate optimal estimator with a class containing all the others and for all $\theta$ . This class is much too big and the problem is too general to hope to find an estimator that stands out above all the rest. If we are to have any chance of finding optimal estimators, we must be less ambitious and restrict the class of estimators. To do this, there are three conventional methods which, for a given problem, supply objective reasons for preferring one estimator in a class which nevertheless remains extremely large.

Principle of Impartiality

The problem with the trivial estimator is that it favours the value $\theta _ { 0 }$ to the detriment of all the others, whence the idea of seeking estimators in a class that does not possess this shortcoming. The most conventional way is to restrict the search for the best estimator to the class of unbiased estimators and impose $\operatorname { E } { \big \{ } \delta ( X ) { \big \} } ~ =$ $\tau ( \theta )$ D. Comparing estimators in the sense of risk then amounts to comparing their variances. Effectively, it can be shown that, in this class, optimal estimators can be found. These are called uniform minimum variance unbiased (UMVU) estimators, with the understanding that the loss function is the quadratic function.

Bayes’ Principle

Another, less ambitious approach is to abandon any hope of minimising the risk uniformly, i.e., for all $\theta$ , and to seek the estimator which minimises a risk calculated on average over all $\theta$ . For this average to have any meaning, it must be calculated using a weighting function $\pi ( \theta )$ . We then calculate the average risk or Bayes risk $R _ { \pi }$ from

$$
R _ { \pi } ( \delta ) = \int _ { \theta } R { \big ( } \tau ( \theta ) , \delta { \big ) } \pi ( \theta ) \mathrm { d } \theta .
$$

In the Bayesian interpretation of this average, $\theta$ is a random variable with a priori probability density $\pi ( \theta )$ . A Bayes estimator is one that minimises the Bayes risk.

When taken in this way, the above notion is not controversial, but some practitioners criticise it when it is not conceivable for $\theta$ to be a random variable. They then reject the idea accepted by the Bayesian school and interpret $\pi ( \theta )$ as a measure of the subjective confidence level attributed to the possible values of $\theta$ . In any case, the Bayesian approach has the advantage that it gives a framework within which it becomes possible on the basis of acquired experience to refine the a priori density $\pi ( \theta )$ by replacing it by the a posteriori density $\psi ( \theta | X )$ . Indeed, according to the Bayes relation,

$$
\psi ( \theta | X ) = \frac { l ( X | \theta ) \pi ( \theta ) } { \int _ { \theta } l ( X | \theta ) \pi ( \theta ) } .
$$

In this expression, $l ( X \vert \theta )$ is the likelihood function, i.e., the probability density for observing $X$ , knowing $\theta$ j. The function $\psi$ is then taken as an improvement on $\pi$ in view of the experimental results $X$ .

Minimax Principle

According to this principle, the overall performance of an estimator is accounted for by noting the maximum of its attached risk, and this maximum risk is then minimised. Hence, an estimator $\delta ^ { * }$ will be a minimax estimator if

$$
\operatorname* { m a x } _ { \theta } R \big ( \tau ( \theta ) , \delta ^ { * } \big ) = \operatorname* { m i n } _ { \delta } \operatorname* { m a x } _ { \theta } R \big ( \tau ( \theta , \delta ) \big ) .
$$

The minimax risk $R _ { \mathrm { m } }$ is defined as

$$
R _ { \mathrm { m } } ( \delta ) = \operatorname* { m a x } _ { \theta } R \big ( \tau ( \theta , \delta ) \big ) .
$$

It can be shown that the minimax risk is always greater than or equal to the risk of an arbitrary Bayes estimator. If $\theta$ has finite domain of definition, it can be shown that the minimax estimator corresponds to the Bayes estimator of the most unfavourable a priori density $\pi$ . The minimax principle turns out to be a precautionary principle, which may even be qualified as pessimistic.

There are other principles leading to interesting estimators. An example is provided by non-deterministic estimates in which the same sample does not necessarily lead to the same estimate.

# 9.5.4 Properties of Estimators

The ideas discussed above suggest a more careful investigation of the properties that should be satisfied by good estimators. It is convenient to begin with convergence, which is a property that all estimators should possess, whether they are UMVU, Bayesian, or something else. The next issue is the bias and variance of estimators, and the methods available for reducing them. Finally, we discuss a fundamental result in the class of unbiased estimators, namely the non-zero lower bound of their variance.

# Convergence

Definition. A sequence of estimators $\{ { \widehat { \theta } } \}$ or, more concisely, an estimator ${ \widehat { \theta } } _ { n }$ , is f gconvergent when it converges in probability to the value it claims to estimate. According to this definition, an estimator is convergent if

$$
\forall \epsilon > 0 , \qquad \operatorname* { l i m } _ { n  \infty } \operatorname* { P r } \Bigl \{ | \hat { \theta } _ { n } - \theta | \ge \epsilon \Bigr \} = 0 .
$$

This convergence is expressed by writing ${ \widehat { \theta } } _ { n } \ { \xrightarrow { \operatorname* { P r } } } \ \theta$ .

The notion of convergence in probability is used to state the law of large numbers, which stipulates that the arithmetic mean $M$ of $n$ independent realisations $( X _ { 1 } , \ldots , X _ { n } )$ of the same random variable $X$ is a convergent estimator of its average $\mu$ (provided it exists):

$$
M = { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } X _ { i } \ { \stackrel { \mathrm { P r } } { \to } } \ \mu .
$$

This result, first discovered at the beginning of the seventeenth century, was the point of departure for probability theory in the field of experiment.

# Unbiasedness

Definition. An estimator ${ \widehat { \theta } } _ { n }$ for $\theta$ or $T _ { n }$ for $\tau ( \theta )$ is said to be unbiased if

$$
\mathbb { E } \big \{ \widehat { \theta } _ { n } \big \} = \theta \quad \mathrm { o r } \quad \mathbb { E } \big \{ T _ { n } \big \} = \tau ( \theta ) ,
$$

for all possible values of $\theta$ . If the bias is defined to be the quantity ${ \mathrm { E } } \{ { \widehat { \theta } } _ { n } \} - \theta$ , an unbiased estimator is one with zero bias.

Example. The arithmetic mean

$$
M = { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } X _ { i }
$$

is an unbiased estimator of the average $\mu$ and of the variance $\sigma ^ { 2 }$ of the parent population (provided it exists):

$$
\operatorname { E } \{ M \} = \mu .
$$

This is a simple consequence of the linearity of mathematical expectation.

The notion of bias, introduced by Gauss in 1821, corresponds to the idea of systematic error as used by physicists. Apart from the theoretical considerations discussed above, it seems reasonable to regard it as a good property if the average of the estimator is equal to the parameter that it is supposed to estimate. However, it is not necessarily a good idea to insist on dealing only with unbiased estimators, if only because there are cases where no such estimator actually exists. The following counterexample is a classic.

Example of a Situation with No Unbiased Estimator. Let $K$ be a random variable distributed according to the binomial distribution $\mathcal { B } ( n , p )$ . The number of trials $n$ is given, but the probability $p$ of success in a given trial is unknown. However, it is not $p$ that we are trying to estimate, but rather $\tau ( p ) = 1 / p$ . Let $t ( k )$ by the values taken by the estimator $T$ for $1 / p$ when we observe $k$ Dsuccesses in $n$ trials. By definition, for $T$ to be unbiased, we must have

$$
\sum _ { k = 0 } ^ { n } t ( k ) C _ { n } ^ { k } p ^ { k } ( 1 - p ) ^ { n - k } = \frac { 1 } { p } \quad \mathrm { f o r } \quad 0 < p \leq 1 .
$$

Suppose now that for a certain $p$ , the estimator $T$ is unbiased. Then the sum on the left is finite, which implies in particular that $t ( 0 )$ is finite. Now when $p  0$ , the term on the left tends to $t ( 0 )$ , whereas the term $1 / p$ !on the right can be as large as we like. Hence, $T$ cannot be unbiased for all $p$ .

This is not such an artificial example. It corresponds to the so-called capture–recapture method, which aims to estimate an animal population. Let $N$ be the population of animal species, e.g., fish in a lake. To estimate $N$ , we capture $m$ animals which are then tagged and released. After tagging, the probability of recapturing an animal is $p = m / N$ , and estimating the population $N = m / p$ amounts to estimating $1 / p$ .

In fact, to estimate $1 / p$ in an unbiased way, the animals must be recaptured up to the point where the number of tagged individuals is equal to a prechosen number $r$ . If $r + Y$ is the total number of animals that must be recaptured in order to obtain $r$ Ctagged animals, it can be shown that $( r + Y ) / r$ is the best unbiased estimator for $1 / p .$ . In this procedure, it is assumed either that $N$ Cis very large or that animals are recaptured and released immediately (drawing with replacement).

Asymptotically Unbiased Estimators

When defining asymptotic properties, it is essential to specify the order of operations when taking the limit. In the case that concerns us here, will a sequence of estimators ${ \widehat { \theta } } _ { n }$ be declared asymptotically unbiased if the limit of the expectation tends to zero, or if the expectation of the limit tends to zero? There are thus two possible definitions.

Definition: Limit of Expectation. A sequence of estimators $\{ { \widehat { \theta } } \}$ for $\theta$ will be called asymptotically unbiased if the sequence of expectations of ${ \widehat { \theta } } _ { n }$ tends to $\theta$ , i.e., if

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname { E } \{ { \widehat { \theta } } _ { n } \} = \theta .
$$

No particular comment is needed here, because this is just a sequence of scalars.

Definition: Expectation of the Limit. A sequence of estimators $\{ { \widehat { \theta } } \}$ for $\theta$ will be called asymptotically unbiased if the sequence of differences ${ \widehat { \theta } } _ { n } - \theta$ , suitably

normalised, tends in probability to a random variable of zero expectation, i.e., if there is a sequence $k _ { n }$ such that

$$
\begin{array} { r } { k _ { n } ( \widehat { \theta } _ { n } - \theta ) \xrightarrow { \mathrm { D i s t } } Y \quad \mathrm { a n d } \quad \mathrm { E } \{ Y \} = 0 . } \end{array}
$$

The normalisation constant $k _ { n }$ is often proportional to $\sqrt { n }$ , as for the central limit theorem. Convergence in distribution means that, at the limit, the two random variables obey the same distribution function, except perhaps on a set of zero measure.

An estimator can be asymptotically unbiased according to one definition and not for the other. In practice, the first definition, i.e., the limit of expectations, is assumed.

# Convergence and Absence of Bias

Convergence refers to the distribution function while absence of bias refers to the first order moment of this function. There is no particular reason for the properties of convergence and absence of bias to be related. They are independent notions. In addition, a convergent estimator is not necessarily asymptotically unbiased by either definition of the absence of asymptotic bias. The following example shows this for the limit of expectations definition. (For the expectation of the limit definition, it is easy to find a counterexample in which the limiting distribution has no average, e.g., the Cauchy distribution.)

Example. Let $\{ { \widehat { \theta } } \}$ be a sequence of estimators for zero, where the estimator ${ \widehat { \theta } } _ { n }$ is a bdiscrete random variable equal to 0 with probability $1 - 1 / n$ and $n ^ { 2 }$ bwith probability $1 / n$ . The sequence of estimators is obviously convergent since the probability associated with the point which is not at zero tends to 0 as $1 / n$ when $n  \infty$ . !However, it is biased, and its bias does not tend to zero, but rather to infinity:

$$
{ \mathrm { E } } \big \{ \widehat { \theta } _ { n } \big \} = 0 ( 1 - 1 / n ) + n ^ { 2 } / n = n .
$$

# Reduction of Bias

Unbiased estimators are of great theoretical importance since they define a class where optimal estimators can exist, but they have another advantage outside this class. If we attempt to apply the law of large numbers by taking the arithmetic mean of a set of biased estimators, we will converge toward the average of the underlying distribution, but this will not be the parameter we hoped to estimate. It will entail an error equal to the bias. This is the whole point about trying to correct any bias, or at least trying to reduce it.

Note, however, that, if we try to reduce the bias using the methods presented below when there is no unbiased estimator, we may reduce the bias of the estimator, but we will increase its variance in such a way that its mean squared error will end up being large.

When the Bias is Easy to Calculate

In certain situations, a simple calculation can correct a bias. This happens when estimating the variance of a population we shall use here as an example. Suppose we have an independent sample $( X _ { 1 } , \ldots , X _ { n } )$ for a distribution with average $\mu$ and variance $\sigma ^ { 2 }$ . The parameter to be estimated is $\sigma ^ { 2 }$ , e.g., a noise power. There are two possible cases: either the average $\mu$ is known or it is not.

If the population average is known, it can be shown that the estimator

$$
S ^ { \prime 2 } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( X _ { i } - \mu ) ^ { 2 } ,
$$

called the sample variance, is unbiased, i.e., ${ \mathrm { E } } \{ S ^ { \prime } { } ^ { 2 } \} = \sigma ^ { 2 }$ . However, if we estimate the population average by the sample mean

$$
M = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } X _ { i } ,
$$

the estimator $S ^ { \prime 2 }$ is only asymptotical unbiased. Indeed, it can be shown that for

$$
S ^ { \prime 2 } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( X _ { i } - M ) ^ { 2 } ,
$$

we have

$$
\operatorname { E } \big \{ S ^ { \prime 2 } \big \} = \sigma ^ { 2 } - \frac { \sigma ^ { 2 } } { n } .
$$

he sample variance is thus systematically smaller than the population variance.

In this case, it is easy to correct for the bias by considering the estimator

$$
S ^ { 2 } = { \frac { n } { n - 1 } } S ^ { ^ { \prime } 2 } .
$$

It follows that

$$
\operatorname { E } \left\{ S ^ { 2 } \right\} = \operatorname { E } \left\{ { \frac { n } { n - 1 } } S ^ { \prime 2 } \right\} = { \frac { n } { n - 1 } } ( \sigma ^ { 2 } - \sigma ^ { 2 } / n ) = \sigma ^ { 2 } .
$$

In order to estimate the variance of a population without bias, it is thus worth considering the estimator

$$
S ^ { 2 } = { \frac { 1 } { n - 1 } } \sum _ { i = 1 } ^ { n } ( x _ { i } - M ) ^ { 2 } .
$$

Note, however, that it has higher variance than the biased estimator $S ^ { \prime 2 }$ . Indeed, we have

$$
\mathrm { V a r } ( S ^ { 2 } ) = \frac { 2 \sigma ^ { 4 } } { n - 1 } > \mathrm { V a r } ( S ^ { \prime 2 } ) = 2 \sigma ^ { 4 } \frac { n - 1 } { n ^ { 2 } } .
$$

If an estimator $\widehat { \theta }$ is unbiased for $\theta$ , there is no reason why $g ( { \widehat { \theta } } )$ should be an unbiased estimator for $g ( \theta )$ . For example, if $g$ is a convex function, the Jensen inequality holds: ${ \mathrm { E } } \{ g ( X ) \} ~ \geq ~ g ( { \mathrm { E } } \{ X \} )$ , which shows that we should expect to observe a bias.

This is the case when estimating the standard deviation $\sigma$ . We have $\operatorname { E } \{ S ^ { 2 } \} ~ >$ $( \operatorname { E } \{ S \} ) ^ { 2 }$ , so we should expect the estimator $S ~ = ~ \sqrt { S ^ { 2 } }$ f gto be a biased estimator ffor $\sigma$ g. For a normal variable ${ \mathcal N } \mu , \sigma ^ { 2 }$ D, for example, the unbiased estimator for the standard deviation $\sigma$ is

$$
S ^ { * } = k _ { n } \left[ { \frac { 1 } { n - 1 } } \sum _ { i } ( X _ { i } - M ) ^ { 2 } \right] ^ { 1 / 2 } , \quad k _ { n } = { \sqrt { \frac { n - 1 } { 2 } } } { \frac { { \cal T } \left( { \frac { n - 1 } { 2 } } \right) } { { \cal T } \left( { \frac { n } { 2 } } \right) } } , \quad n \geq 2 ,
$$

where $\varGamma$ is the Euler function of the second kind.

When the Bias is Hard to Calculate

We then resort to resampling methods or bootstrap methods. The archetypal example is the following.

# Quenouille’s Method

If there is a bias of order $1 / n$ , this method can reduce it to order $1 / n ^ { 2 }$ . We assume that the mean value of the estimator can be expanded in powers of $1 / n$ . Half the sample is extracted, having removed one point if the sample size was odd to begin with. We then have

$$
\begin{array} { l } { { { \displaystyle { \mathbb E } \Bigl \{ \widehat \theta _ { n } \} = \theta + \frac { 1 } { n } \beta + { \cal O } ( 1 / n ^ { 2 } ) , } \ ~ } } \\ { { { \displaystyle { \mathbb E } \Bigl \{ \widehat \theta _ { 2 n } \} = \theta + \frac { 1 } { 2 n } \beta + { \cal O } ( 1 / n ^ { 2 } ) , } } } \end{array}
$$

whence

$$
\mathrm { E } \big \{ 2 \widehat { \theta } _ { 2 n } - \widehat { \theta } _ { n } \big \} = \theta + O ( 1 / n ^ { 2 } ) .
$$

The bias going as $1 / n$ has disappeared, but in general the variance of this new estimator will increase by a factor of order $1 / n$ . A better method would be to divide the $2 n$ -sample at random into two equal parts, evaluate the corresponding estimators ${ \widehat { \theta } } _ { n }$ and $\widehat { \theta } _ { n } ^ { \prime }$ , and calculate the new estimator

$$
2 \widehat { \theta } _ { 2 n } - \frac { 1 } { 2 } \widehat { ( \theta } _ { n } + \widehat { \theta } _ { n } ^ { \prime } ) .
$$

Jackknife Method

There is another method which only increases the variance by a term in $1 / n ^ { 2 }$ . This is the jackknife method. (For more details, see The Jackknife. A Review, Miller, 1974.) This involves more sophisticated calculation, but with today’s ever faster and ever cheaper electronic means of computation, the jackknife is superior to the Quenouille method described above.

Let ${ \widehat { \theta } } _ { n }$ be an estimator for $\theta$ , calculated from an $n$ -sample. Once again, expand its mean value in powers of $1 / n$ :

$$
\operatorname { E } { \big \{ } { \widehat { \theta } } _ { n } { \big \} } = \theta + \sum _ { k = 1 } ^ { \infty } { \frac { a _ { k } } { n ^ { k } } } .
$$

Now recalculate the $n$ estimators $\widehat { \theta } _ { - i }$ , each time removing a point $i$ from the $n$ -sample, and calculate the arithmetic mean of these estimators, viz.,

$$
{ \overline { { \widehat { \theta } } } } _ { n - 1 } = { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } { \widehat { \theta } } _ { - i } .
$$

Finally, define the jackknife $\widehat { \theta } _ { n } ^ { \prime }$ as

$$
\widehat { \theta } _ { n } ^ { \prime } = n \widehat { \theta } _ { n } - ( n - 1 ) \overline { { { \widehat { \theta } } } } _ { n - 1 } = \widehat { \theta } _ { n } + ( n - 1 ) \big ( \widehat { \theta } _ { n } - \overline { { { \widehat { \theta } } } } _ { n - 1 } \big ) .
$$

It can be shown that, for this estimator, the order $1 / n$ bias has also vanished.

# Efficiency

We have seen that, for unbiased estimators and for a quadratic loss function, these can be ordered according to the values of their variances. According to this idea, the estimator $\widehat { \theta } _ { 1 }$ will be preferable to $\widehat { \theta } _ { 2 }$ if $\operatorname { V a r } \left( { \widehat { \theta } } _ { 1 } \right) < \operatorname { V a r } \left( { \widehat { \theta } } _ { 2 } \right)$ . We then say that $\widehat { \theta } _ { 1 }$ is more efficient than $\widehat { \theta } _ { 2 }$ .

This raises two questions:

1. For a given unbiased estimator, can its variance be reduced?   
2. Is it possible, at least in principle, to make its variance arbitrarily small?

The answer to the first question is affirmative in some cases, but for this to be possible, there must be an exhaustive statistic. We shall see below what this involves. The answer to the second question is negative, if there is a lower bound below which the variance cannot be reduced. In general, this lower bound is not known, but an approximation can be given, viz., the Rao–Cramer bound. These considerations are ´ developed in the following.

# Reducing the Variance

Reduction of the variance involves the idea of an exhaustive summary, i.e., statistics containing everything we can hope to know about the parameter we are trying to estimate. Let us make this more precise.

Definition. A statistic $T$ is said to be exhaustive if the conditional distribution of the sample $X$ given that $T ( X ) ~ = ~ t$ does not depend on the parameter $\theta$ . If $f \left( x | T ( x ) = t \right)$ Ddenotes this conditional probability density of the sample $X$ , we jhave

$$
{ \frac { \partial } { \partial \theta } } f \bigl ( x | T ( x ) = t \bigr ) = 0 .
$$

Although abstract, this definition corresponds to what is usually done when compressing data. By keeping only the value $T ( X )$ from the original sample $X = ( X _ { 1 } , \ldots , X _ { n } )$ , we keep only what depended on $\theta$ . Indeed, the equation $T ( x ) =$ $t$ Dspecifies a hypersurface in the sample space $\mathbb { R } ^ { n }$ , and saying that $T$ Dprovides an exhaustive summary amounts to saying that only the value $t$ of this statistic is important. The distribution of ‘points’ $X _ { i }$ actually on this hypersurface is of no importance, since it does not depend on what we seek here. If we had to reconstruct a sample with the same characteristics as the original sample with regard to estimation of $\theta$ , the points could be distributed at random over the hypersurface $\textit { T } = \textit { t }$ according to the corresponding conditional distribution.

In order to show that a statistic is exhaustive, it is often simpler to appeal to the following criterion.

Theorem. Factorisation or Fisher–Neyman Criterion. A statistic $T$ is exhaustive for estimating $\theta$ if and only if the likelihood function of the sample can be factorised in the form

$$
L ( x , \theta ) = l ( t , \theta ) h ( x ) ,
$$

where $x$ denotes a value taken by the sample, i.e., . $( X _ { 1 } = x _ { 1 } , \ldots , X _ { n } = x _ { n } )$ /, and $L$ D Dis the probability distribution at this point (or just the probability if the variables are discrete). The functions $l$ and $h$ must be positive.

Example: Poisson Distribution. For an independent and identically distributed sample with Poisson distribution, we have

$$
\operatorname* { P r } \{ X = x \} = \prod _ { i = 1 } ^ { n } { \frac { \lambda ^ { x _ { i } } } { x _ { i } ! } } \mathrm { e } ^ { - \lambda } = { \frac { \lambda ^ { \sum x _ { i } } \mathrm { e } ^ { - n \lambda } } { \prod x _ { i } ! } } .
$$

This satisfies the factorisation criterion with $h ( x ) = 1 / \prod x _ { i } !$ and the statistic $T =$ $\textstyle \sum _ { i = 1 } ^ { n } x _ { i }$ is exhaustive for the parameter $\lambda$ D of the Poisson distribution.

With this idea in hand, we can now state a version of the Rao–Blackwell theorem for the case of quadratic loss functions.

Rao–Blackwell Theorem. If $\widehat { \theta }$ is an unbiased estimator of $\tau ( \theta )$ and if the sampling law admits an exhaustive statistic $T$ , then the estimator $\widehat { \theta } _ { 1 }$ calculated from

$$
\widehat { \theta } _ { 1 } = \mathrm { E } \big \{ \widehat { \theta } | T = t \big \}
$$

is unbiased and has smaller variance than the original estimator:

$$
\forall \theta , \quad \operatorname { V a r } ( { \widehat { \theta } } _ { 1 } ) < \operatorname { V a r } ( { \widehat { \theta } } ) ,
$$

unless the estimators turn out to be identical.

The improvement achieved by the Rao–Blackwell theorem does not guarantee that the new estimator has minimal variance, however. For this to be the case, the statistic $T$ must also be complete.

Definition. The statistic $T$ is said to be complete if the expectation of all integrable functions of $T$ is non-degenerate, i.e., if

$$
\forall \theta , g \in L ^ { 1 } , \quad \operatorname { E } \{ g ( T ) \} = 0 \Longrightarrow g ( t ) = 0 .
$$

The $\theta$ dependence is contained in the sampling distribution used to calculate the expectation.

Example: Binomial Distribution. The sample $X$ of size $k = 1$ is drawn from a binomial distribution with unknown parameter $\theta$ D, while the parameter $n$ is known. The statistic $T = X$ is trivially exhaustive. Show that it is also complete. For all integrable $g$ ,

$$
\begin{array} { c l c } { \displaystyle \forall \theta \in ( 0 , 1 ) , \quad \operatorname { E } \{ g ( T ) \} = \sum _ { x = 0 } ^ { n } g ( x ) C _ { n } ^ { x } \theta ^ { x } ( 1 - \theta ) ^ { n - x } = 0 } \\ { \displaystyle } & { \qquad = ( 1 - \theta ) ^ { n } \sum _ { x = 0 } ^ { n } g ( x ) C _ { n } ^ { x } \left( \frac { \theta } { 1 - \theta } \right) ^ { x } = 0 . } \end{array}
$$

The last expression is a polynomial in $\theta / ( 1 - \theta )$ of degree $n$ which vanishes for infinitely many values of its variable. It is therefore identically zero and $g ( x ) = 0$ . A similar result can be proven for a sample of arbitrary size $k$ and for $\textstyle T = \sum _ { i = 1 } ^ { k } X _ { i }$

Lehmann–Scheffe Theorem.´ If $T$ is an exhaustive and complete statistic, then the improvement of $\widehat { \theta }$ under the conditions of the Rao–Blackwell theorem has smaller variance. The resulting estimator $\widehat { \theta } _ { 1 }$ is thus the UMVU estimator.

Example. Following Tassi (see the bibliography), consider the case where an object has probability $p$ of possessing some feature considered to be exceptional in some sense. The objects are arranged into $r$ classes and $n$ objects are then drawn independently from each class. The number of objects per class is relatively unimportant, provided it is greater than $n$ . The class itself is said to be exceptional if there is at least one exceptional object among the $n$ objects drawn out, and otherwise it is said to be ordinary. Let $X _ { i }$ be the number of exceptional objects in the sample of size $n$ drawn from class $i$ . The problem is to estimate without bias, given the data $( X _ { 1 } , \ldots , X _ { r } )$ , the probability $\theta$ that a class is ordinary.

Consider the variable $\mathbf { 1 } _ { X _ { i } = 0 }$ , which is the indicator function for class $i$ to be ordinary. If we set $\widehat { \theta } = \mathbf { 1 } _ { X _ { i } = 0 }$ D, the estimator is a Bernoulli variable with parameter $\theta$ . We then have

$$
\mathbb { E } \big \{ \widehat { \theta } \big \} = \mathbb { E } \{ { \bf 1 } _ { X _ { i } = 0 } \} = \theta ,
$$

and this estimator is thus unbiased. In order to improve it using the Rao–Blackwell theorem, we require an exhaustive statistic for estimation of $\theta$ . The likelihood function of the data $( X _ { 1 } , \ldots , X _ { r } )$ is the product of $r$ binomially distributed random variables. We have

$$
L ( x , \theta ) = \prod _ { i = 1 } ^ { r } C _ { n } ^ { X _ { i } } p ^ { X _ { i } } ( 1 - p ) ^ { n - X _ { i } } = \left( \frac { p } { 1 - p } \right) ^ { \sum _ { i } X _ { i } } ( 1 - p ) ^ { n r } \prod _ { i = 1 } ^ { r } C _ { n } ^ { X _ { i } } .
$$

This is indeed in the form (9.26) and the statistic $\textstyle T = \sum _ { i = 1 } ^ { r } X _ { i }$ is exhaustive for $p$ . It is also exhaustive for $\theta$ , which depends only on $p$ D D. The estimator $h ( \widehat { \theta } )$ improved by Rao–Blackwell is then

$$
h ( \widehat { \theta } ) = \mathrm { E } \big \{ \widehat { \theta } | T = t \big \} .
$$

Considering the class $i = 1$ for calculation of $\widehat { \theta }$ , it follows that

$$
h ( \widehat { \theta } ) = \mathrm { E } \big \{ \widehat { \theta } | T = t \big \} = \mathrm { P r } \{ X _ { 1 } = 0 | T = t \} = \frac { \mathrm { P r } \{ X _ { 1 } = 0 , T = t \} } { \mathrm { P r } \{ T = t \} } .
$$

The sampling model is binomial, whence

$$
\frac { \operatorname* { P r } \left\{ X _ { 1 } = 0 , \sum _ { i = 2 } ^ { r } X _ { i } = t \right\} } { \operatorname* { P r } \left\{ \sum _ { i = 1 } ^ { r } X _ { i } = t \right\} } = \frac { C _ { n r - n } ^ { \mathrm { T } } } { C _ { n r } ^ { \mathrm { T } } } .
$$

This estimator depends only on the value of the variable $T$ , denoted by $h ( T )$ . Then

$$
h ( T ) = { \frac { C _ { n r - n } ^ { T } } { C _ { n r } ^ { T } } } .
$$

Since we have seen that this statistic is also complete, $h ( T )$ is therefore the UMVU estimator for $\theta$ .

# 9.5.5 Frechet or Rao–Cram ´ er Inequality ´

Since the variance of an estimator can be reduced under certain conditions, it is then legitimate to ask how far such a reduction can be taken. Clearly, the variance cannot be less than zero, but is there a strictly positive bound below which, for a given problem, it is impossible to find an estimator achieving this level of performance? The problems relating to the search for this bound involve theoretical and practical features of great importance, which we shall discuss in this section.

An unbiased estimator which reaches this limiting variance will be preferable to all others in the sense of quadratic risk. It will be called the optimal estimator and hence will be the UMVU estimator. However, in the general case, there is no way to find the optimal limit. On the other hand, it is possible to give an approximation, namely the Rao–Cramer bound, or´ minimum variance bound. Furthermore, there is a large class of estimators that actually reach this bound, known as efficient estimators, which we shall now examine.

Such an estimator $T$ , by assumption unbiased, has mean $\operatorname { E } \{ T \} = \tau ( \theta )$ and variance $\operatorname { V a r } ( T ) ~ = ~ \operatorname { E } \{ { \bigl [ } T - \tau ( \theta ) { \bigr ] } ^ { 2 } \}$ f g D. To calculate this variance, we use the D mathematical expectation operator, which is a linear operator and with which we can associate a scalar product. This scalar product obeys the Cauchy–Schwartz inequality. Let $\psi$ be a function of the $n$ -sample (denoted by $X$ ) and the parameter $\theta$ to be estimated. By the Cauchy–Schwartz inequality,

$$
\begin{array} { r } { \mathrm { E } \{ \big [ T - \tau ( \theta ) \big ] ^ { 2 } \} \mathrm { E } \{ \psi ( X , \theta ) ^ { 2 } \} \geq \Big [ \mathrm { E } \{ \big [ T - \tau ( \theta ) \big ] \psi ( X , \theta ) \} \Big ] ^ { 2 } , } \end{array}
$$

whence, given that $\mathbb { E } \{ [ T - \tau ( \theta ) ] ^ { 2 } \} = \mathrm { V a r } ( T )$

$$
\operatorname { V a r } ( T ) \geq { \frac { \left[ \operatorname { E } \left\{ { \bigl [ } T - \tau ( \theta ) { \bigr ] } \psi ( X , \theta ) \right\} \right] ^ { 2 } } { \operatorname { E } \left\{ \psi ( X , \theta ) ^ { 2 } \right\} } } .
$$

Equality obtains if and only if the function $\psi$ is proportional to $T - \tau ( \theta )$ , that is, if and only if

$$
\psi ( X , \theta ) = A ( \theta ) \big [ T - \tau ( \theta ) \big ] .
$$

The inequality (9.32) can in principle be used to find the optimal bound, since

$$
\mathrm { V a r } ( T ) \geq \operatorname* { m a x } _ { \psi } \frac { \Big [ \mathrm { E } \big \{ \big [ T - \tau ( \theta ) \big ] \psi ( X , \theta ) \big \} \Big ] ^ { 2 } } { \mathrm { E } \big \{ \psi ( X , \theta ) ^ { 2 } \big \} } .
$$

However, it is almost impossible for all $T$ and $\tau ( \theta )$ and all parent populations to exhibit the optimal bound by calculating the maximum. The best that can be done is to find a function $\psi$ that provides a bound close enough to the optimal bound. If the function $\psi$ is not well chosen, we find a lower bound that is too small, e.g., if $\psi$ does not depend on $X$ , we will find $\mathrm { V a r } ( T ) \geq 0$ , which we already knew. In order to find a best lower bound, we must identify a common case where the function $\psi$ has the above form (9.33), so that the bound is attained. For this particular case, the bound obtained will be the optimal one.

Let us consider the case where the $n$ -sample $X$ comes from a normal parent distribution with known mean $\mu$ and variance $\sigma ^ { 2 }$ , and the parameter $\theta$ to be estimated is the mean $\mu$ , estimated by the empirical average $M$ . Assume also that the sample is made up of independepent and identically distributed random variables.

First we calculate the likelihood function for this $n$ -sample:

$$
L ( X | \theta ) = \prod _ { i = 1 } ^ { n } { \frac { 1 } { \sigma { \sqrt { 2 \pi } } } } \exp \left[ - { \frac { 1 } { 2 } } \left( { \frac { X _ { i } - \theta } { \sigma } } \right) ^ { 2 } \right] .
$$

The product is eliminated by taking the logarithm of the expression to give

$$
\ln { \cal L } = - n \ln ( \sigma \sqrt { 2 \pi } ) - \sum _ { i = 1 } ^ { n } \frac { 1 } { 2 } \left( \frac { X _ { i } - \theta } { \sigma } \right) ^ { 2 } .
$$

We now eliminate the constant and the square by differentiating with respect to $\theta$ to obtain

$$
{ \frac { \partial \ln L } { \partial \theta } } = { \frac { 1 } { \sigma ^ { 2 } } } \sum _ { i = 1 } ^ { n } x _ { i } - { \frac { n \theta } { \sigma ^ { 2 } } } = { \frac { n } { \sigma ^ { 2 } } } ( M - \theta ) .
$$

We then see that in the particular case of estimation of the mean $\mu$ of a normal population with known variance by the arithmetic mean $M$ , the function $\partial \ln L / \partial \theta$ has precisely the form (9.33) which makes the Cauchy–Schwartz inequality into an equality. In this case the resulting bound is the optimal bound.

For an arbitrary population and when estimating a function of an arbitrary parameter $\theta$ by a statistic $T$ , we can be sure that the variance of $T$ will always be greater than or equal to the limit found if we replace the function $\psi$ by $\partial \ln L / \partial \theta$ in the Cauchy–Schwartz inequality. It will not be the optimal bound but it is of great practical importance because of the case giving rise to it. It is called the minimum variance bound (MVB).

It remains to actually calculate this bound, and to do this, we have to find the various expectation values appearing in (9.32). The calculation is relatively simple and we shall not go into the details here. Note, however, that the final result is only valid when the operations of integration and differentiation with respect to the parameter to be estimated can be legitimately interchanged, e.g., when the integration bounds do not depend on this parameter. With this proviso, if the estimator $T$ is unbiased, we deduce the following inequality for the variance, known as the Rao–Cramer or Fr ´ echet inequality: ´

$$
\boxed { \mathrm { V a r } ( T ) \geq \frac { \left[ \tau ^ { \prime } ( \theta ) \right] ^ { 2 } } { \mathrm { E } \{ - \partial ^ { 2 } \ln L / \partial \theta ^ { 2 } \} } . }
$$

We have seen that the relatively arbitrary choice of function $\psi$ implies that this lower bound is not necessarily attained. For it to be attained, a necessary and sufficient condition is

$$
\frac { \partial } { \partial \theta } \ln { \cal L } = A ( \theta ) \big [ T - \tau ( \theta ) \big ] ,
$$

where $A ( \theta )$ is an arbitrary function of the parameter $\theta$ to be estimated. If the variance of an estimator reaches this bound, it is called the minimum variance bound (MVB).

# 9.5.6 Efficient Estimators

When the MVB is attained, we have

$$
\frac { \partial \ln { \cal L } } { \partial \theta } = A ( \theta ) \big [ T - \tau ( \theta ) \big ] .
$$

Substituting this directly into (9.38), we obtain

$$
\operatorname { V a r } ( T ) = { \frac { \tau ^ { \prime } ( \theta ) } { A ( \theta ) } } ,
$$

and if $\tau ( \theta ) = \theta$ ,

$$
\operatorname { V a r } ( T ) = { \frac { 1 } { A ( \theta ) } } .
$$

The last two expressions can in some cases be used to find the variance of an MVB estimator rather easily, as illustrated by the following examples.

Example: Variance of the Arithmetic Mean of a Normal Distribution. For an $n$ -sample drawn from a normal distribution with known variance $\sigma ^ { 2 }$ and for estimation of the mean $\theta$ by the arithmetic mean $T \ = \ M$ , we saw earlier that we had

$$
{ \frac { \partial } { \partial \theta } } \ln L = { \frac { n } { \sigma ^ { 2 } } } ( M - \theta ) , \quad { \mathrm { h e n c e } } \quad A ( \theta ) = { \frac { n } { \sigma ^ { 2 } } } ,
$$

so that

$$
\operatorname { V a r } ( T ) = { \frac { \sigma ^ { 2 } } { n } } .
$$

Example: Variance of the Sample Variance of a Normal Distribution. Consider a normal population with probability distribution

$$
f ( x ) = \frac { 1 } { \sqrt { 2 \pi } \theta } \exp \left( - \frac { x ^ { 2 } } { 2 \theta ^ { 2 } } \right) .
$$

The average is known and can be assumed to be zero, but the variance $\theta ^ { 2 }$ is not known. We then have

$$
{ \frac { \partial \ln L } { \partial \theta } } = { \frac { n } { \theta ^ { 3 } } } \left( { \frac { 1 } { n } } \sum X _ { i } ^ { 2 } - \theta ^ { 2 } \right) = { \frac { n } { \theta ^ { 3 } } } { \bigl ( } S ^ { \prime 2 } - \theta ^ { 2 } { \bigr ) } .
$$

The form of the function $\partial \ln L / \partial \theta$ naturally suggests choosing the statistic

$$
S ^ { \prime 2 } = { \frac { 1 } { n } } \sum X _ { i } { } ^ { 2 }
$$

as estimator for $\theta ^ { 2 }$ . This estimator will be MVB provided that it is unbiased. It is easy to demonstrate that this last condition is satisfied since

$$
\operatorname { E } \{ S ^ { \prime 2 } \} = \int { s ^ { 2 } } L \mathrm { d } \mathbf { x } = { \frac { 1 } { n } } \sum _ { i } \int { X _ { i } } ^ { 2 } L \mathrm { d } \mathbf { x } = { \frac { 1 } { n } } \sum _ { i } \theta ^ { 2 } = \theta ^ { 2 } .
$$

Therefore, $S ^ { \prime 2 }$ is indeed an MVB estimator for the function $\tau ( \theta ) = \theta ^ { 2 }$ . We can immediately calculate its variance to be

$$
\operatorname { V a r } ( S ^ { \prime 2 } ) = { \frac { \tau ^ { \prime } ( \theta ) } { n / \theta ^ { 3 } } } = { \frac { 2 \theta } { n / \theta ^ { 3 } } } = { \frac { 2 \theta ^ { 4 } } { n } } .
$$

The standard deviation, denoted here by $\theta$ , is usually denoted by $\sigma$ , whence

$$
\operatorname { V a r } ( S ^ { \prime 2 } ) = { \frac { 2 \sigma ^ { 4 } } { n } } .
$$

We thus find the variance of the sample variance for a normal sample with known mean.

# 9.5.7 Efficiency of an Estimator

Let $T$ be a convergent unbiased estimator for estimating $\tau ( \theta )$ . Its efficiency is measured by the reciprocal of the ratio of its variance to the limiting variance given by the MVB:

$$
\mathrm { E f f } ( T ) = \frac { \mathrm { V a r } _ { \mathrm { M V B } } ( \theta ) } { \mathrm { V a r } ( T ) } .
$$

The estimator $T$ will be said to be efficient if it has efficiency equal to 1 (or $100 \%$ ), or in other words if it attains its MVB. As already noted, the MVB is not necessarily attained and an optimal estimator is not necessarily efficient.

# 9.5.8 Biased Estimators

Let $T$ be a biased estimator for $\theta$ . By the definition of bias, we have

$$
\mathrm { e } T = \theta + b ( \theta ) .
$$

If we choose the function $\tau ( \theta ) = \theta + b ( \theta )$ , we have

$$
\mathrm { e } T = \tau ( \theta ) ,
$$

which shows that $T$ is an unbiased estimator for $\tau ( \theta )$ . Let us apply the Rao–Cramer´ formula for this function $\tau$ . We find $\tau ^ { \prime } ( \theta ) = 1 + b ^ { \prime } ( \theta )$ , and also

$$
\operatorname { V a r } ( T ) \equiv \operatorname { E } \{ \left[ t - { \bigl ( } \theta + b ( \theta ) { \bigr ) } \right] ^ { 2 } \} = \operatorname { E } \{ ( T - \theta ) ^ { 2 } \} - b ^ { 2 } ( \theta ) .
$$

The term $\mathrm { E } \big \{ ( T - \theta ) ^ { 2 } \big \}$ is the mean squared error (MSE) in $T$ . We have just seen that it is always greater than or equal to the variance of $T$ . Finally, we may write

$$
\mathbb { E } \big \{ ( T - \theta ) ^ { 2 } \big \} = \operatorname { V a r } ( T ) + b ^ { 2 } ( \theta ) \geq \frac { \big [ 1 + b ^ { \prime } ( \theta ) \big ] ^ { 2 } } { \mathbb { E } \big \{ - \partial ^ { 2 } \ln L / \partial \theta ^ { 2 } \big \} } + b ^ { 2 } ( \theta ) .
$$

While it is true that the mean squared error in a biased estimator is always greater than its variance, the example below shows that it is possible to find a biased estimator for which the mean squared error is smaller than the smallest variance associated with the class of unbiased estimators.

Example: Estimating the Parameter of an Exponential Distribution. Consider an independent and identically distributed $n$ -sample $( X _ { 1 } , \ldots , X _ { n } )$ drawn from a population with exponential distribution having mean $\theta$ :

$$
f ( x ) = { \frac { 1 } { \theta } } \exp \left( - { \frac { x } { \theta } } \right) , \quad { \mathrm { w h e r e } } \quad \operatorname { E } \{ X _ { i } \} = \theta , \quad \operatorname { V a r } ( X _ { i } ) = \theta ^ { 2 } .
$$

Let us choose the arithmetic mean $\overline { { X } }$ as estimator for $\theta$ . We know that it is an unbiased estimator for the population average, and hence $\operatorname { E } \{ { \overline { { X } } } \} = \theta$ . In this case, its mean squared error with respect to $\theta$ is equal to its variance:

$$
\mathsf { e } ( \overline { { X } } - \theta ) ^ { 2 } = \mathrm { E } \Big \{ \big ( \overline { { X } } - \mathrm { E } \big \{ \overline { { X } } \big \} \big ) ^ { 2 } \big \} \equiv \mathrm { V a r } ( \overline { { X } } ) .
$$

We now show that $\overline { { X } }$ is MVB by calculating $\partial \ln L / \partial \theta$ :

$$
\ln { \cal L } = - n \ln \theta - \frac { 1 } { \theta } \sum _ { i = 1 } ^ { n } X _ { i } ,
$$

$$
{ \frac { \partial \ln L } { \partial \theta } } = - { \frac { n } { \theta } } + { \frac { 1 } { \theta ^ { 2 } } } \sum _ { i = 1 } ^ { n } X _ { i } = { \frac { n } { \theta ^ { 2 } } } ( \overline { { X } } - \theta ) .
$$

This shows that $\overline { { X } }$ is indeed MVB for estimating $\theta$ , whence it follows immediately that

$$
\operatorname { V a r } ( { \overline { { X } } } ) = { \frac { \theta ^ { 2 } } { n } } .
$$

On the other hand, the estimator $\widehat { X } = n \overline { { X } } / ( n + 1 )$ is biased but its mean squared error is smaller than the MVB $\theta ^ { 2 } / n$ D Cof the unbiased estimators. Indeed, it is biased:

$$
\operatorname { E } \{ \widehat { X } \} = \frac { n } { n + 1 } \theta , \qquad b _ { n } ( \theta ) = - \frac { \theta } { n + 1 } ,
$$

but we have the inequalities

$$
\operatorname { V a r } ( { \widehat { X } } ) = { \frac { n } { ( n + 1 ) ^ { 2 } } } \theta ^ { 2 } < \operatorname { E } \left\{ ( { \widehat { X } } - \theta ) ^ { 2 } \right\} = { \frac { \theta ^ { 2 } } { n + 1 } } < \operatorname { V a r } ( { \overline { { X } } } ) = { \frac { \theta ^ { 2 } } { n } } .
$$

This example shows that it can be too restrictive to search for the best estimator only in the class of unbiased estimators.

# 9.5.9 Minimum Variance Bound and Fisher Information

The non-negative quantity

$$
I _ { n } ( \theta ) \equiv \operatorname { E } { \Biggl \{ } \left( { \frac { \partial } { \partial \theta } } \ln L \right) ^ { 2 } { \Biggr \} } = \operatorname { E } { \Biggl \{ } - { \frac { \partial ^ { 2 } } { \partial \theta ^ { 2 } } } \ln L { \Biggr \} }
$$

is called the Fisher information contained in the $n$ -sample. Since the random variable $\partial \ln L / \partial \theta$ has zero mean, the Fisher information is just the reciprocal of the variance of this random variable.

For independent and identically distributed samples, this quantity depends only the size of the $n$ -sample and the probability distribution of the parent population, and we have shown that $I _ { n } ( \theta ) = n I _ { 1 } ( \theta )$ . This means that, in the case where the Rao– DCramer inequality applies, the variance of an estimator ´ $T$ decreases more slowly than $1 / n$ . The inequality then becomes

$$
\operatorname { V a r } ( T ) \geq { \frac { \left[ \tau ^ { \prime } ( \theta ) \right] ^ { 2 } } { n I _ { 1 } ( \theta ) } } .
$$

When estimating the midpoint of a uniform probability density on $( 0 , \theta ]$ , the estimator

$$
\frac { 1 } { 2 } \big [ X _ { ( n ) } + X _ { ( 1 ) } \big ]
$$

of the mean $\theta / 2$ has asymptotic variance

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname { v a r } \left( { \frac { 1 } { 2 } } \big [ X _ { ( n ) } + X _ { ( 1 ) } \big ] \right) = { \frac { 1 } { 2 n ^ { 2 } } } .
$$

This asymptotic variance decreases faster than the Rao–Cramer bound because this´ is exactly the case where this bound does not apply. Indeed, the mathematical expectation is given by the integral $\begin{array} { r } { \int _ { 0 } ^ { \theta } \mathrm { d } x } \end{array}$ , and the upper bound is a function of the parameter to be estimated, whence the Rao–Cramer does not apply. ´

The bounds deduced from the Rao–Cramer inequalities are adapted to the case´ where measurement errors are small around the estimated parameter. By this we mean that these errors have a distribution close to normal. When the errors are large, e.g., close to a Cauchy distribution, there are then better suited bounds, i.e., greater than the Rao–Cramer bounds.´

# 9.5.10 Multidimensional Case

When the experimenter wishes to make joint estimates of a set of $k$ parameters $( \theta _ { 1 } , \ldots , \theta _ { k } )$ , there is a generalisation of the Rao–Cramer inequality. This appeals to ´

the Fisher information matrix $J$ , with elements $J _ { i j }$ given by

$$
J _ { i j } = \operatorname { E } \left\{ - { \frac { \partial ^ { 2 } } { \partial \theta _ { i } \partial \theta _ { j } } } \log L \right\} .
$$

If $V$ denotes the matrix of variances and covariances for the paramters $\theta$ , the inequality is given symbolically by $V ~ \geq ~ J ^ { - 1 }$ . We use the convention that an inequality sign $>$ between matrices means that their difference is a positive definite matrix, i.e., all its eigenvalues are positive, while $\geq$ means that at least one eigenvalue may be zero.

From a practical standpoint, this means that the error ellipse at the confidence level $\gamma$ , i.e.,

$$
\begin{array} { r } { ( \theta - \widehat { \theta } ) ^ { \mathrm { T } } \mathsf { V } ^ { - 1 } ( \theta - \widehat { \theta } ) = k _ { \gamma } ^ { 2 } , } \end{array}
$$

encompasses the confidence region calculated with the matrix $J$ , i.e.,

$$
\begin{array} { r } { ( \boldsymbol { \theta } - \widehat { \boldsymbol { \theta } } ) ^ { \mathrm { T } } \mathbf { J } ( \boldsymbol { \theta } - \widehat { \boldsymbol { \theta } } ) = k _ { \gamma } ^ { 2 } . } \end{array}
$$

This last confidence region can be used as an approximation to the actual confidence region. The scalar $k _ { \gamma } ^ { 2 }$ is calculated (under the normal distribution hypothesis) using the distribution function $F$ of a $\chi ^ { 2 }$ distribution with $k$ degrees of freedom: $k _ { \gamma } ^ { 2 } =$ $F ^ { - 1 } ( 1 - \gamma )$ .

# 9.5.11 Robust Estimators

As we have already seen, there are generally several estimators for the same parameter $\theta$ . Among other things, the arithmetic mean, median, and midpoint of the sample are often considered to estimate the population average. For example, for a normal distribution, the arithmetic mean of the sample is unbiased and MVB. It is thus the best possible estimator and there is no reason to look for any other. But which one should we choose when we do not know the nature of the parent population, or when we do know that but there is contamination by measurement errors of unknown type? To fix ideas, we shall consider three very different parent populations and give the asymptotic variances of the three previous estimators. As these three densities are symmetric, it is in fact the position of the axis of symmetry that we seek to determine. To simplify, we shall take all scale factors equal to unity. We then obtain Table 9.7, in which values in bold type are the smallest possible.

We see in this example that, if we have no idea what kind of underlying parent population we are dealing with, it is safer to use the median, in order to obtain a finite variance in all cases. We may consider Table 9.7 as the loss matrix for a game against nature, where we can in fact only lose in this case. The median is chosen according to the minimax strategy, i.e., minimising the maximum loss. The median is said to be a reliable or robust estimator for this set of populations.

Table 9.7 Asymptotic variance of three different populations. The uniform distribution is taken here over the interval from 0 to 1   

<table><tr><td></td><td>Uniform distribution</td><td>Normal distribution</td><td>Cauchy distribution</td></tr><tr><td rowspan="2">Median</td><td>1</td><td>元</td><td>π²</td></tr><tr><td>4n</td><td>2n</td><td>4n</td></tr><tr><td rowspan="2">Mean</td><td>1</td><td>1</td><td rowspan="2">8</td></tr><tr><td>12n</td><td>n</td></tr><tr><td rowspan="2">Midpoint</td><td>1</td><td>π²</td><td rowspan="2">8</td></tr><tr><td>2n2</td><td>24 ln n</td></tr></table>

There are several other reliable estimators for the symmetry axis of a population with symmetric distribution. Depending on their type, they can be suitable for a range of different populations. Here are some of them:

• Truncated or Trimmed Mean. Consider the symmetric bilateral truncated mean. We remove $2 q$ points from the ordered $n$ -sample

$$
( X _ { ( 1 ) } \leq X _ { ( 2 ) } \leq \ldots \leq X _ { ( n ) } ) ,
$$

namely the $q$ smallest and the $q$ largest, to obtain the new sample

$$
( X _ { ( q + 1 ) } \leq . . . \leq X _ { ( n - q ) } ) .
$$

The truncation parameter is defined here as

$$
\alpha = { \frac { q } { n } } ,
$$

and the arithmetic mean of the remaining $( n - 2 q )$ -sample will be called the mean symmetrically truncated at $100 \%$  and denoted by $T _ { \alpha }$ . We will thus have

$$
T _ { \alpha } = \frac { 1 } { ( n - 2 q ) } \sum _ { i = q + 1 } ^ { n - q } X _ { ( i ) } .
$$

Note that $\alpha$ is generally fixed between 0 and 1. We then calculate $q = \lfloor \alpha n \rfloor$ . In this case, the mean is truncated by at most $100 \%$ and at least $1 0 0 ( \alpha - 1 / n ) \%$ .

• Winsorized Mean. The procedure is the same as for the truncated mean, except that we replace the $q$ smallest values by $X _ { ( q + 1 ) }$ and the $q$ largest by $X _ { ( n - q ) }$ , then calculate the mean:

$$
W _ { \alpha } = \frac { 1 } { n } \left[ \sum _ { i = q + 1 } ^ { n - q } X _ { ( i ) } + q \big [ X _ { ( q + 1 ) } + X _ { ( n - q ) } \big ] \right] .
$$

• Hodges–Lehmann Median. We construct the new sample $( Y _ { 1 1 } , Y _ { 1 2 } , \ldots , Y _ { n n } )$ from the sample $( X _ { 1 } , \ldots , X _ { n } )$ by the rule

$$
Y _ { i j } = \frac { 1 } { 2 } ( X _ { i } + X _ { j } ) ,
$$

and we define the Hodges–Lehmann median $\mathrm { H L }$ as the median of the $Y _ { i j }$ .

• Midpoint. This statistic is the point located at equal distance from the two outermost points, and it is thus equal to

$$
P = { \frac { 1 } { 2 } } \bigl [ X _ { ( 1 ) } + X _ { ( n ) } \bigr ] .
$$

Example: Asymptotic Variances of Several Estimators for the Cauchy Distribution. Consider an independent and identically distributed $n$ -sample drawn from a Cauchy distribution with probability distribution

$$
f ( x ) = { \frac { 1 } { \pi { \big [ } 1 + ( x - \theta ) ^ { 2 } { \big ] } } } .
$$

The asymptotic variances of different estimators for $\theta$ are given in Table 9.8. From the table, we see that the mean truncated at $38 \%$ is only slightly less efficient, but much easier to calculate than the estimate of the maximum likelihood in this optimal case.

# 9.5.12 Some Classic Methods

It seems that effective estimators can be obtained by implementing a method that takes into account both the observed data $x$ and what is known about the unknown parameter $\theta$ . For this purpose, we might consider looking for the value of $\theta$ that maximises the a posteriori probability density $\psi ( \theta | x )$ , or a functional of this. However, $\psi$ jis written as the product of the likelihood $l ( x | \theta )$ and the a priori probability density $\pi ( \theta )$ , and if we do not possess information about $\theta$ , $\pi ( \theta )$ remains undetermined. We may then attempt to maximise the likelihood and look for $\widehat { \theta }$ as solution of the implicit equation: $l ( x | \theta ) = \mathrm { m a x } _ { \theta } l ( x | \theta )$ . The estimator j Dfound in this way is the estimator for the maximum likelihood.

Table 9.8 Asymptotic variance of various estimators for $\theta _ { 0 }$   

<table><tr><td>Estimator</td><td>Asymptotic variance</td></tr><tr><td>Maximumlikelihood</td><td>2 n</td></tr><tr><td>Mean truncated at 38%</td><td>2.28 R n</td></tr><tr><td>Median</td><td>2.47 3 4n</td></tr></table>

This estimator is often found as a solution to the equations $\partial l / \partial \theta \ : = \ : 0$ with $\partial ^ { 2 } l / \partial \theta ^ { 2 } \ < \ 0$ D. Under these conditions, it can be shown that the estimator $\widehat { \theta }$ is convergent. In addition, the quantity

$$
\left( - \frac { \partial ^ { 2 } l } { \partial \theta ^ { 2 } } \bigg | _ { \theta = \widehat { \theta } } \right) ^ { 1 / 2 } ( \widehat { \theta } - \theta )
$$

behaves roughly like a normal random variable with zero mean and unit variance. This shows that, provided that the associated moments exist, the maximum likelihood estimator is asymptotically unbiased and asymptotically efficient. It is this result that gives the maximum likelihood estimator its special status.

If the problem reduces to estimating the mean $\mu = \mu ( \theta )$ of a normal sample, the likelihood function is equal to $\exp ( - \chi ^ { 2 } / 2 )$ Dup to a multiplicative constant, where $\chi ^ { 2 }$ is a quadratic form equal to $( x - \mu ) ^ { \mathrm { { T } } } V ^ { - 1 } ( x - \mu )$ , with $V$ the variance– covariance matrix of $x$ and $X ^ { \mathrm { T } }$ the transpose of $X$ . This therefore amounts to looking for the maximum of $l$ or $\log { l }$ and the maximum likelihood then corresponds to the minimum of the form $( x - \mu ) ^ { \mathrm { { T } } } V ^ { - 1 } ( x - \mu )$ . This remark introduces the  underlying idea of the least squares method, discussed here in the normal case and for measurements of unequal accuracy.

Outside the normal case, the least squares method (or least $\chi ^ { 2 }$ for measurements of unequal accuracy) does not always yield optimal estimators. However, there is another favourable situation, namely the linear case. This refers to a situation in which the mean $\mu$ depends linearly on the unknown parameters $\theta$ , and no assumptions are made about the type of data apart from the existence of $\mu$ and $V$ . In particular, we do not necessarily know the probability density. The decomposition of $\mu$ in terms of a polynomial basis or in a Fourier series expansion are two examples of linear situations. The coefficients of these expansions are the unknown parameters $\theta$ . If $\mu = X \theta$ is the matrix equation expressing the linear dependence of the model $\mu$ on $\theta$ Dand if $y$ denotes the data (it is traditional to use $y$ rather than $x$ in this case), the least squares estimators are given by the expression ${ \widehat { \theta } } = ( X ^ { \operatorname { T } } X ) ^ { - 1 } X ^ { \operatorname { T } } y$ in the case where the matrix $V$ Dis the identity matrix (and we may always reduce to this case by a change of variables). The Gauss–Markov theorem states that these estimators are unbiased and that, for each parameter $\theta$ , they have the smallest variance in the class of linear estimators. It is remarkable that the estimator $\widehat { \theta }$ has optimal properties without any reference to the probability density of the measurements $y$ .

The maximum likelihood and least squares methods often provide good estimators, but they can prove to be unacceptable. They may be the best in a class that turns out to be too small, e.g., normal case or class of unbiased estimators. They may also exhibit anomalies, e.g., if the operator $( X ^ { \mathrm { T } } X ) ^ { - 1 }$ does not exist. In this case, one must revert to the idea mentioned at the beginning of this section, namely to introduce a certain dose of a priori knowledge about the desired estimator. This aim can be achieved by means of a regularising function $g$ which reflects the faithfulness of the solution with respect to what is expected of $\theta$ . The likelihood $l$ reflects the faithfulness to the data. With this in mind, we look for estimators maximising the quantity $f = \lambda _ { 0 } l + \lambda _ { 1 } g$ , where $\lambda _ { 0 } + \lambda _ { 1 } = 1 .$ The scalars $\lambda _ { 0 }$ and $\lambda _ { 1 }$ D C C Dare Lagrange multipliers, accounting respectively for the relative importance of data fidelity and the relative importance of the a priori knowledge of $\theta$ . The Bayesian framework provides a natural probabilistic interpretation of this method. Indeed, the maximum of $\psi$ coincides with the maximum of $\log \psi$ , which can be written $\log \psi = \log l + \log \pi$ , a form which can be identified with $f$ . Many methods D Cfor finding estimators are based on this idea whenever the conventional methods fail. They are classified according to the nature of the regularising function, e.g., entropy maximum, Tikhonov regularisation, pseudo-inverse, etc., or the nature of its probabilistic interpretation in the Bayesian framework. Examples of these methods can be found elsewhere in this book. The difficulty is often to find the weighting by the multipliers $\lambda _ { 0 }$ and $\lambda _ { 1 }$ which leads to optimal estimators. Cross-validation is one approach that tackles this very problem.

# 9.6 From Data to Object: the Inverse Problem

In this section,12 we discuss the procedures for obtaining the best possible estimate of the observed object, using all the information available about the instrument used for the observation and about sources of noise intrinsic to the instrument or to the received signal, but also the information we possess concerning the source itself, which is generally not totally unknown. We use the term data to refer to the complete set of measured values resulting from the observation process. By taking into account all this information in a suitable way, not only is the object better reconstructed by data processing, but error bars affecting this reconstruction can be estimated. Figure 9.13 illustrates these procedures schematically.

The developments and tools described in the following can be applied to a very broad range of data types encountered in astrophysical observation: images with any format and at all wavelengths, spectra, polarisation rates as a function of frequency, and so on. However, in order to make the following more concrete and to illustrate it with examples, we have chosen to discuss only wavefront sensing and image processing, and to develop examples taken from the areas of adaptive optics, which began in the 1990s (see Sect. 6.3), and interferometry (see Sect. 6.4). Indeed, these two areas have considerably stimulated such processing techniques. Readers will then be able to adapt the ideas discussed here to other cases they may encounter in radioastronomy, high energy observation, etc.

![](images/bfeda1025597adbd3628625c60d84535d58cf85f0a7bfbc21e002b8ff20c6106.jpg)  
Fig. 9.13 Schematic view of the inverse problem and of the various solutions discussed in this section

# 9.6.1 Posing the Problem

# Forward Problem

Consider the following classic problem in physics. An initial object such as an electromagnetic wave propagates through a system that will affect it in some way, e.g., atmospheric turbulence, an instrument involving aberrations and diffraction, etc. We can deduce the properties of the output wave if we know all the properties of the system, such as would be included in a forward or direct model, or data formation model for this system. This is the basic principle of end-to-end models, discussed in Sect. 9.2.

This can be illustrated by wavefront sensing as carried out in adaptive optics, i.e., the measurement of aberrations intrinsic to the telescope or due to the passage through turbulent atmospheric layers, using a (Hartmann–Shack) wavefront sensor. The relevant physical quantity here is the phase $\varphi ( \boldsymbol { r } , t )$ on the exit pupil of the telescope, which contains all the information regarding the aberrations suffered by the wave. The measurement data are the average slopes of the phase in two perpendicular directions, viz., $\partial \phi ( \boldsymbol { r } , t ) / \partial x$ and $\partial \phi ( \boldsymbol { r } , t ) / \partial y$ , on each Hartmann–Shack subaperture, which can be recorded together in a vector i . The calculation of the slopes $_ i$ given the phase $\varphi$ is a classic forward problem in physics. It requires a choice of data formation model.

An end-to-end forward model includes models for data formation right up to detection, and even up to data storage when data are transmitted with compression. It thus takes into account photon noise, detector readout noise, digitiser quantisation noise, and data compression noise, if any (see Sect. 9.2).

# Inverse Problem

The problem here is work back up from the data to knowledge of the object that originated the data. This is called the inverse problem. It involves inverting the data formation model. Our senses and our brains solve such inverse problems all the time, analysing the information received, e.g., by the retina, and deducing positions in space, 3D shapes, and so on. This is also the most common situation for the observer in astronomy, who makes deductions from observations and attempts to conclude as accurately as possible about some set of properties of the source.

In physics, and especially in astronomy, the processing of experimental data thus consists in solving an inverse problem, in practice, after a data reduction or preprocessing stage which aims to correct for instrumental defects in such a way that the data can be correctly described by the chosen forward model (see Sect. 9.4).

Estimating (see Sect. 9.5) or working back up to the phase $\varphi$ from the slope vector $_ i$ is the inverse problem of Hartmann–Shack wavefront sensing. It involves inverting the corresponding data formation model.

Let us consider another example, taken from another spectral region. The $\gamma$ ray astronomy mission INTEGRAL (see Sect. 5.2.5) has three instruments capable of carrying out spectral analysis, namely, JEM-X, IBIS ISGRI+PICSIT, and SPI. Each of these can measure the spectrum of the observed source, here the black hole binary system Cygnus X-1. The data formation model is contained in a software called XSPEC, and an a priori model of the source containing a certain number of free parameters is injected into this. The simulated output of this software is then compared with measurements from each of the instruments, and the free parameters are fitted in the best possible way, in a sense to be made precise shortly, as shown in Fig. 9.14.

We shall see below that inversion can often take advantage of statistical knowledge regarding measurement error, generally modelled as noise. Naive inversion methods are often characterised by instability, in the sense that the inevitable measurement noise is amplified in an uncontrolled way during inversion, leading to an inacceptable solution. In this case, where the data alone are insufficient to obtain an acceptable solution, more sophisticated inversion methods, called regularised inversion methods, are brought to bear. They incorporate further constraints to impose a certain regularity on the solution, compatible with what is known $a$ priori about it. This is a key point: in data processing, we introduce supplementary information as dictated by our prior knowledge of the object. For example, a brightness can only take positive values, an object such as a stellar disk is bounded spatially by a contour, a temporal fluctuation cannot contain frequencies above a certain threshold, and so on.

![](images/e338e716c61557abab2c29554edc05b2500b409d78b65cda6c37e8c5e9a290c8.jpg)  
Fig. 9.14 Spectrum of the accreting binary system Cygnus X-1, viewed by the various instruments of the $\gamma$ -ray observatory INTEGRAL. The model fitted to the data is a hybrid model, in which electrons in the corona have a non-thermal distribution. From Cadolle-Bel M. et al., Soc. Fr. Astron. Astroph., Scientific Highlights 2006, p. 191

It is extremely productive to conceive of data processing explicitly as the inversion of a forward problem. To begin with, this forces us to model the whole data formation process, so that each step can be taken into account in the inversion. It also allows us to analyse existing methods, e.g., a typical deconvolution, or filtering, as discussed in Sect. 9.1.3, and to clearly identify the underlying assumptions, or the defects. It is then possible to conceive of methods that take advantage of knowledge concerning the data formation process as well as knowledge of the source or the relevant physical quantity, available a priori, i.e., before the measurements are made.

In the following, we discuss the basic notions and tools required to tackle the resolution of an inverse problem, a subject that has been deeply transformed by the advent of powerful computational tools. For the purposes of this textbook,13 the tools discussed are illustrated on several relatively simple, i.e., linear, inverse problems encountered in astronomy: wavefront reconstruction from measurements by a Hartmann–Shack sensor, adaptive optics corrected image restoration and multispectral image reconstruction in nulling interferometry (see Sect. 6.6). We shall not discuss extensions to non-linear problems, which do exist, however.

# 9.6.2 Well-Posed Problems

Let the relevant physical quantity be $o$ , referred to as the object in what follows. It could be the phase of the wave in the case of a wavefront sensor, a star or galaxy in the case of an image in the focal plane of a telescope, the spectrum of a quasar in the case of a spectrograph, etc. Let $i$ be the measured data.14 This could be the slopes measured by the Hartmann–Shack sensor, an image, a spectrum, etc. We shall consider for the moment that $o$ and $i$ are continuous quantities, i.e., functions of space, time, or both, belonging to Hilbert spaces denoted by $X$ and $Y$ .

The forward model, deduced from physics and from the known properties of the instrument, can be used to calculate a model of the data in the case of observation of a known object. This is what is done in a data simulation operation:

$$
i = H ( o ) .
$$

We shall restrict attention here to linear forward models, whence

$$
i = H o ,
$$

where $H$ is a continuous linear operator mapping $X$ into $Y$ . It was in this context that Hadamard15 introduced the concept of well-posed problems.

When the forward model is linear and translation invariant, e.g., for imaging by a telescope within the isoplanatic patch (see Sect. 6.2), $H$ is a convolution operator and there is a function $h$ called

the point spread function $( P S F )$ such that

$$
i = H o = h \star o .
$$

We seek to invert (9.71), i.e., to find $o$ for a given $i$ . We say that the problem is well posed in the sense of Hadamard if the solution $o$ satisfies the usual conditions for existence and uniqueness, but also the less well known condition of stability, i.e., the solution depends continuously on the data $i$ . In other words, a small change in the data — in practice, another realisation of the random noise — only brings about a small change in the solution. These three conditions, known as Hadamard’s conditions, are expressed mathematically in the following way:

• Existence. There exists $o \in X$ such that $i = H o$ , i.e., $i \in \operatorname { I m } ( H )$ , the image or range of $H$ .   
• Uniqueness. The kernel of $H$ contains only zero, i.e., $\operatorname { K e r } ( H ) = \{ 0 \}$ .   
• Stability. The inverse of $H$ on $\operatorname { I m } ( H )$ is continuous.

Note that for the stability condition the inverse of $H$ on $\operatorname { I m } ( H )$ , denoted by $H ^ { - 1 }$ , is well defined, because we assume that $\begin{array} { l l l } { \operatorname { K e r } ( H ) } & { = } & { \{ 0 \} } \end{array}$ . Note also that the stability condition is equivalent to requiring the set $\operatorname { I m } ( H )$ gto be closed, i.e., $\operatorname { I m } ( H ) = { \dot { \overline { { \operatorname { I m } ( H ) } } } }$ .

DFor many inverse problems, even the first two of these conditions are not satisfied, let alone the third. Indeed, on the one hand $\operatorname { I m } ( H )$ is the set of possible images when there is no noise, a smaller set than the space of noisy data to which $i$ belongs. For example, in imaging, $\operatorname { I m } ( H )$ is a vector space that contains no frequency greater than the optical cutoff frequency of the telescope $( D / \lambda )$ , whereas the noise will contain such frequencies. In general, the existence of a solution is therefore not guaranteed. On the other hand, the kernel of $H$ contains all objects unseen by the instrument. So for a Hartmann–Shack sensor, these are the unseen spatial modes, e.g., described in terms of Zernike polynomials, such as the piston mode $( Z _ { 1 } )$ or the so-called waffle mode. For an imager, these are the spatial frequencies of the object above the optical cutoff frequency of the telescope. The kernel is therefore generally not just $\{ 0 \}$ and uniqueness is not granted.

f gThe mathematician Nashed introduced the idea of a well-posed problem in the sense of least squares, which provides a way to ensure existence (in practice) and uniqueness of the solution and then to show that inversion in the least squares sense does not lead to a good solution of the inverse problem owing to its instability, also called non-robustness to noise.16 It thus remains ill-posed.

We say that $\hat { o } _ { \mathrm { L S } }$ is a least-squares solution to the problem (9.71) if

$$
\| i - H \hat { o } _ { \mathrm { L S } } \| ^ { 2 } = \operatorname* { i n f } _ { o } \| i - H o \| ^ { 2 } ,
$$

where $\parallel \parallel$ is the Euclidean or $L _ { 2 }$ norm. Nashed then showed the following:

• Existence. A least-squares solution exists if and only if $i \in \operatorname { I m } ( H ) + \operatorname { I m } ( H ) ^ { \perp }$ . This condition is always satisfied if $\operatorname { I m } ( H )$ is closed.

• Uniqueness. If several solutions exist, we choose the unique solution with minimal norm, i.e., we project the solution on to the orthogonal complement $\operatorname { K e r } ( H ) ^ { \perp }$ of the kernel. We denote this by $H ^ { \dagger } i$ , and call it the generalised inverse. The operator $H ^ { \dagger }$ associates the least-squares solution of $i ~ = ~ H o$ of minimal norm, i.e., the only solution in $\operatorname { K e r } ( H ) ^ { \perp }$ , to all $i \in \operatorname { I m } ( H ) + \operatorname { I m } ( H ) ^ { \perp }$ .

Moreover, it can be shown that $H ^ { \dagger }$ is continuous if and only if $\operatorname { I m } ( H )$ is closed.

We say that the problem (9.71) is well-posed in the least-squares sense if there exists a unique least-squares solution (with minimal norm) and it is stable, i.e., it depends continuously on the data $i$ . We then see that the problem (9.71) is indeed well posed in the sense of least squares if and only if $H ^ { \dagger }$ is continuous, i.e., if and only if $\operatorname { I m } ( H )$ is closed. And for many operators, e.g., when $H$ is the convolution with a square-integrable response $h$ , this condition is not satisfied.

We can understand the meaning of such a solution intuitively by characterising the least-squares solutions. Let $H$ be a continuous linear operator from a Hilbert space $X$ to the Hilbert space $Y$ . Then the following three propositions are equivalent:

1. $\begin{array} { r } { \| i - H \hat { o } _ { \mathrm { L S } } \| ^ { 2 } = \operatorname* { i n f } _ { o \in X } \| i - H o \| ^ { 2 } } \end{array}$ :   
2. $H ^ { * } H \hat { o } _ { \mathrm { L S } } = H ^ { * } i$ 2 k, where $H ^ { * }$ kis the adjoint of $H$ (normal equation).   
3. $H \hat { o } _ { \mathrm { L S } } = P i$ , where $P$ is the (orthogonal) projection operator of $Y$ on $\overline { { \mathrm { I m } ( H ) } }$ .

In particular, characterisation (3) tells us that the least-squares solution exactly solves the original equation (9.71) when the data $i$ are projected onto the (closure of the) set of all possible data in the absence of noise, i.e., $\overline { { \mathrm { I m } ( H ) } }$ .

In finite dimensions, i.e., for all practical (discretised) problems, a vector subspace is always closed. As a consequence, we can be sure of both the existence and the continuity of the generalised inverse. However, the ill-posed nature of the continuous problem does not disappear by discretisation. It simply looks different: the mathematical instability of the continuous problem, reflected by the non-continuity of the generalised inverse in infinite dimensions, resurfaces as a numerical instability of the discretised problem. The discretised inverse problem in finite dimensions is ill-conditioned, as we shall explain shortly. The conditioning of a discretised inverse problem characterises the robustness to noise during inversion. It is related to the dynamic range of the eigenvalues of $H ^ { * } H$ (a matrix in finite dimensions), and worsens as the dynamic range increases.

# 9.6.3 Conventional Inversion Methods

In the following, we shall assume that the data, which have been digitised (see Sect. 9.1.3), are discrete, finite in number, and gathered together into a vector $_ i$ . In imaging, for an image of size $N \times N$ , $_ i$ is a vector of dimension $N ^ { 2 }$ which concatenates the rows or the columns of the image (in a conceptual rather than computational sense).

The first step in solving the inverse problem is to discretise also the sought object $\pmb { o }$ by expanding it on to a finite basis, that is, a basis of pixels or cardinal sine functions for an image, or a basis of Zernike polynomials for a phase representing aberrations. The model relating $\pmb { o }$ and $_ i$ is thus an approximation to the continuous forward model of (9.70) or (9.71). By explicitly incorporating the measurement errors in the form of additive noise $\pmb { n }$ (a vector whose components are random variables), this can be written

$$
\pmb { i } = H ( \pmb { o } ) + \pmb { n } ,
$$

in the general case, and

$$
\pmb { i } = H \pmb { o } + \pmb { n } ,
$$

in the linear case, where $H$ is a matrix. In the special case where $H$ represents a discrete convolution, the forward model can be written

$$
i = h \star o + n ,
$$

where $\pmb { h }$ is the PSF of the system and $\star$ denotes the discrete convolution.

Note that, in the case of photon noise, the noise is not additive in the sense that it depends on non-noisy data $H o$ . Equation (9.74) then abuses notation somewhat.17

# Least-Squares Method

The most widely used method for estimating the parameters $\pmb { o }$ from the data $_ i$ is the least-squares method. The idea is to look for $\hat { \pmb { o } } _ { \mathrm { L S } }$ which minimises the mean squared deviation between the data $_ i$ Oand the data model $H ( o )$ :

$$
\hat { \pmb { o } } _ { \mathrm { L S } } = \arg \operatorname* { m i n } _ { \pmb { o } } \| \pmb { i } - \pmb { H } ( \pmb { o } ) \| ^ { 2 } ,
$$

where arg min is the argument of the minimum and $\parallel \parallel$ is the Euclidean norm. k kThis method was first published by Legendre18 in 1805, and was very likely discovered by Gauss19 a few years earlier but without publishing. Legendre used the

least-squares method to estimate the ellipticity of the Earth from arc measurements, with a view to defining the metre.

When the measurement model is linear and given by (9.75), the solution is analytic and can be obtained by setting the gradient of the criterion (9.77) equal to zero:

$$
H ^ { \mathrm { T } } H \hat { \pmb { \ o } } _ { \mathrm { L S } } = H ^ { \mathrm { T } } \pmb { i } .
$$

If $H ^ { \mathrm { T } } H$ can be inverted, i.e., if the rank of the matrix $H$ is equal to the dimension of the unknown vector $\mathbf { \delta } _ { \pmb { o } }$ , then the solution is unique and given by

$$
\begin{array} { r } { \hat { \pmb \sigma } _ { \mathrm { L S } } = \left( H ^ { \mathrm { T } } H \right) ^ { - 1 } H ^ { \mathrm { T } } \pmb { i } . } \end{array}
$$

Otherwise, as in infinite dimension (see Sect. 9.6.2), there are infinitely many solutions, but only one of them has minimal norm (or ‘energy’). This is the generalised inverse, written $H ^ { \dagger } i$ .

# Relation Between Least Squares and Inverse Filter

When the image formation process can be modelled by a convolution, the translation invariance of the imaging leads to a particular structure of the matrix $H$ . This structure is approximately the structure of a circulant matrix (for a 1D convolution), or block circulant with circulant blocks (for a 2D convolution). In this approximation, which amounts to making the PSF $\pmb { h }$ periodic, the matrix $H$ is diagonalised by discrete Fourier transform (DFT), which can be calculated by an FFT algorithm, and its eigenvalues are the values of the transfer function $\tilde { h }$ (defined as the DFT of $\pmb { h }$ ). The minimal norm least-squares solution of the last section can then be written in the discrete Fourier domain:20

$$
\tilde { \partial } _ { \mathrm { L S } } ( \boldsymbol { u } ) = \frac { \tilde { h } ^ { * } ( \boldsymbol { u } ) \tilde { i } ( \boldsymbol { u } ) } { | \tilde { h } ( \boldsymbol { u } ) | ^ { 2 } } = \frac { \tilde { i } } { \tilde { h } } ( \boldsymbol { u } ) \qquad \forall \boldsymbol { u } \ \mathrm { s u c h ~ t h a t } \ \tilde { h } ( \boldsymbol { u } ) \neq 0 , \quad \mathrm { a n d } \ 0 \ \mathrm { i f } \ \tilde { h } ( \boldsymbol { u } ) = 0 ,
$$

where the tilde represents the discrete Fourier transform. In the case of a convolutive data model, the least-squares solution is thus identical to the inverse filter, up to the above-mentioned approximation.

# Maximum Likelihood Method

In the least-squares method, the choice of a quadratic measure of the deviation between the data $_ i$ and the data model $H ( o )$ is only justified by the fact that the solution can then be obtained by analytical calculation. Furthermore, this method makes no use whatever of any knowledge one may possess about the statistical properties of the noise. But this information about the noise can be used to interpret the least-squares method, and more importantly to extend it.

We model the measurement error $\pmb { n }$ as noise with probability distribution $p _ { \mathrm { n } } ( \pmb { n } )$ . According to (9.74), the distribution of the data $_ i$ conditional to the object, i.e., for a given object o (hence supposed known), is then21

$$
p ( i | \pmb { o } ) = p _ { \mathrm { n } } \big ( i - H ( \pmb { o } ) \big ) .
$$

Equation (9.81) can be used to draw realisations of noisy data knowing the object, i.e., to simulate data. On the other hand, in an inverse problem, one has only one realisation of the data, namely those actually measured, and the aim is to estimate the object. The maximum likelihood (ML) method consists precisely in reversing the point of view on $p ( i | o )$ by treating $\mathbf { \delta } _ { \pmb { o } }$ as variable, with $_ i$ fixed equal to the data, and seeking the object $\pmb { o }$ j that maximises $p ( i | o )$ . The quantity $p ( i | o )$ viewed as a function of $\pmb { o }$ j jis then called the likelihood of the data, and the object $\hat { \pmb { o } } _ { \mathrm { M L } }$ which Omaximises it is the one which makes the actually observed data the most likely:22

$$
{ \hat { \pmb { o } } } _ { \mathrm { M L } } = \arg \operatorname* { m a x } _ { \pmb { o } } p ( i | \pmb { o } ) .
$$

The most widely used model for noise is without doubt the centered (i.e. zero mean) Gaussian model, characterised by its covariance matrix $C _ { \mathrm { n } }$ :

$$
p ( i | o ) \propto \exp \left\{ - \frac { 1 } { 2 } \big [ i - H ( o ) \big ] ^ { \mathrm { T } } C _ { \mathrm { n } } ^ { - 1 } \big [ i - H ( o ) \big ] \right\} .
$$

The noise is called white noise (see Appendix B) if its covariance matrix is diagonal. If this matrix is also proportional to the identity matrix, then the noise is called stationary or homogeneous (white noise). The readout noise of a CCD detector (see Sect. 7.4.6) is often modelled by such a stationary centered Gaussian noise. Photon noise is white, but it has a Poisson distribution (see Appendix B), which can be shown, for high fluxes, to tend towards a non-stationary Gaussian distribution with variance equal to the signal detected on each pixel.

Maximising the likelihood is obviously equivalent to minimising a criterion defined to be the negative of the logarithm of the likelihood and called the neg-log-likelihood:

$$
J _ { i } ( \pmb { \sigma } ) = - \ln p ( i | \pmb { \sigma } ) .
$$

In the case of Gaussian noise, the neg-log-likelihood is

$$
J _ { i } ( \pmb { o } ) = \frac { 1 } { 2 } \big [ i - H ( \pmb { o } ) \big ] ^ { \mathrm { T } } C _ { \mathrm { n } } ^ { - 1 } \big [ i - H ( \pmb { o } ) \big ] .
$$

If the noise is also white, we have

$$
J _ { i } ( \pmb { o } ) = \frac { 1 } { 2 } \sum _ { k } \frac { | i ( k ) - H ( \pmb { o } ) ( k ) | ^ { 2 } } { \pmb { \sigma } _ { \mathrm { n } } ^ { 2 } ( k ) } ,
$$

where ${ \pmb \sigma } _ { \mathrm { n } } ^ { 2 } ( k )$ are the elements on the diagonal of the matrix $C _ { \mathfrak { n } }$ . $J _ { i } ( \pmb { o } )$ is a weighted least squares criterion. If the noise is also stationary with variance $\sigma _ { \mathrm { n } } ^ { 2 }$ , then $J _ { i } ( \pmb { \sigma } ) = \| i - H ( \pmb { \sigma } ) \| ^ { 2 } / 2 \sigma _ { \mathrm { n } } ^ { 2 }$ is precisely the ordinary, as opposed to weighted, least squares criterion.

The least squares method can thus be interpreted as a maximum likelihood method in the case of stationary white Gaussian noise. Conversely, if the noise distribution is known but different, the maximum likelihood method can take this knowledge of the noise into account and then generalises the least squares method.

# Example: Wavefront Reconstruction by the Maximum Likelihood Method

Consider a Hartmann–Shack wavefront sensor that measures aberrations due to atmospheric turbulence on a ground-based telescope. The phase at the exit pupil is expanded on a basis of Zernike polynomials $Z _ { k }$ , the degree of which is necessarily limited in practice to some maximal value $k _ { \mathrm { m a x } }$ :

$$
\varphi ( x , y ) = \sum _ { k = 1 } ^ { k _ { \mathrm { m a x } } } o _ { k } Z _ { k } ( x , y ) .
$$

We thus seek $\pmb { o }$ , the set of coefficients $o _ { k }$ of this expansion, by measuring the average slopes and inserting them into a measurement vector $_ i$ . The data model is precisely (9.75), viz., $i = H \pmb { \sigma } + \pmb { n }$ , where $H$ is basically the differentiation operator and is D Cknown as the interaction matrix.

In the simulation presented below, the sensor contains $2 0 \times 2 0$ subapertures of which only 276 receive light, owing to a central obstruction of $33 \%$  by the secondary mirror. This gives 552 slope measurements. The true turbulent phase $\varphi$ is a linear combination of $k _ { \mathrm { m a x } } = 8 6 1$ Zernike polynomials, drawn from a Kolmogorov distribution. The matrix $H$ Dthus has dimensions $5 5 2 \times 8 6 1$ . The noise on the slopes is stationary white Gaussian noise with variance equal to the variance of the non-noisy slopes, implying a signal-to-noise ratio of 1 on each measurement. Under such conditions, the maximum likelihood estimate of the phase is identical to the least squares solution (see last subsection). The matrix $H ^ { \mathrm { T } } H$ in (9.79) has dimensions $k _ { \mathrm { m a x } } \times k _ { \mathrm { m a x } }$ and cannot be inverted because we only have 552 measurements. The generalised inverse solution cannot be used because it is completely dominated by noise. A remedy often adopted here is to reduce the dimension $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } }$ of the space of unknowns $\mathbf { \delta } _ { \pmb { o } }$ during reconstruction of the wavefront. This remedy is one of the known regularisation methods, referred to as regularisation by dimension control. An example of reconstruction for different values of $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } }$ is shown in Fig. 9.15.

For $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } } = 2 1 0$ max , a value well below the number of measurements, the reconstructed phase Dis already unacceptable. The particular shape is due to the fact that the telescope has a central obstruction, whence there are no data at the centre of the pupil.

![](images/5d0d52d8e9b33b86571ea0aae03f3196b743f1df96912e23b466af198d06d7dc.jpg)  
Fig. 9.15 Wavefront sensing on a pupil. Top left: Simulated phase (called true phase). Other figures: Phases reconstructed by maximum likelihood (ML) by varying the number of reconstructed modes

This example clearly illustrates the case where, although the matrix $H ^ { \mathrm { T } } H$ can be inverted, it is ill-conditioned, i.e., it has eigenvalues very close to 0, leading to uncontrolled noise amplification.

Truncating the solution space to lower values of $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } }$ produces more reasonable solutions, but on the one hand the optimal choice of $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } }$ depends on the levels of turbulence and noise and this adjustment is difficult to achieve in practice, while on the other hand this truncation introduces a modelling error, since it amounts to neglecting all the components of the turbulent phase beyond $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } }$ . We shall see below how the introduction of a priori knowledge regarding the spatial regularity of the phase (Kolmogorov spectrum) can lead to a better solution without this ad hoc reduction of the space of unknowns.

# Interpreting the Failure of Non-Regularised Methods

The failure of the maximum likelihood method illustrated in the above example may seem surprising given the good statistical properties of this method, which is an estimator that converges towards the true value of the parameters when the number of data tends to infinity, which is asymptotically efficient, etc. However, these good properties are only asymptotic, i.e., they only concern situations where there is good statistical contrast, defined simply as the ratio of the number of measurements to the number of unknowns.

In practice, and in particular in the previous example, the problem is often to estimate a number of parameters of the same order of magnitude as the number of measurements, and sometimes greater, in which case these asymptotic properties are of little help. In this commonly encountered situation of unfavourable statistical contrast, the inversion is unstable, i.e., highly sensitive to noise, which can often be interpreted as arising due to the ill-posed nature of the underlying infinite dimensional problem.

Image restoration is another typical case of this situation. Obviously, for an image containing $N \times N$ pixels, we try to reconstruct an object of the same size, and if we increase the image size, we also increase the number of unknown parameters relating to the object, without improving the statistical contrast, which remains of order unity. We have seen that the least-squares solution was in this case given by the inverse filter, and we know that this is highly unstable with regard to noise. This instability is easily understood by reinserting the measurement equation (9.76), in the Fourier domain, into the solution (9.80):

$$
\tilde { \hat { \pmb { o } } } _ { \mathrm { L S } } = \frac { \tilde { i } } { \tilde { h } } = \tilde { \pmb { o } } + \frac { \tilde { { \pmb { m } } } } { \tilde { h } } .
$$

According to this, it is clear that the noise is highly amplified for all frequencies for which the value of the transfer function $\widetilde { h }$ is close to zero. One way to reduce noise amplification would be to modify (9.80) and divide $\widetilde { i }$ by $\tilde { h }$ only for frequencies $\pmb { u }$ where the transfer function $\widetilde { h }$ is not too small. This is also a form of regularisation by controlling the dimension of the solution, very similar to the choice of $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } }$ when reconstructing a wavefront, and it suffers from the same ad hoc character and the same difficulty in its tuning.

To sum up, simple inversion methods like least squares or maximum likelihood only give satisfactory results if there is good statistical contrast. For example, maximum likelihood can be successfully applied to problems like image registration, where we seek a 2D vector in order to register two images comprising a large number of pixels. More generally, it applies to the search for the few variables of a parsimonious parametric model from a large enough data set, e.g., estimating a star’s diameter from visibilities in optical interferometry, estimating the Earth’s ellipticity from arc measurements, etc.

In many problems where the statistical contrast is not favourable, the problem is ill-conditioned and regularisation, i.e., the addition during inversion of a priori knowledge and constraints on the solution, becomes highly profitable, as we shall now show.

# 9.6.4 Inversion Methods with Regularisation

Regularisation of an inverse problem corresponds to the idea that the data alone cannot lead to an acceptable solution, so that a priori information about the regularity of the considered observed object must necessarily be introduced. Here the term regularity implies that, for physical reasons intrinsic to the object, it must have certain properties, or obey certain rules regarding sign, size, or frequency, for example. The solution then results from a compromise between the requirements of the object’s postulated regularity and of the data fidelity.

Indeed, several very different solutions, some very poor and some rather good, may be compatible with the data. For instance, in the previous example of wavefront reconstruction, the true and reconstructed phases for $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } } ~ = ~ 2 1 0$ (Fig. 9.15) give very similar likelihood values, whence Dthey are both faithful to the data. In addition, the smoother, more regular solution obtained for $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } } = 5 5$ is less well fitted, i.e., less faithful to the data than the one obtained for $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } } = 2 1 0$ D Dsince it was obtained by optimising in fewer degrees of freedom, and yet it is much closer to the true phase.

# Bayesian Estimation and the Maximum a Posteriori (MAP) Estimator

Bayesian estimation, presented briefly here, provides a natural way of combining the information brought by measurements and information available a priori. Let us assume that we have expressed our a priori knowledge of the observed object in the form of a probability distribution $p ( \pmb { o } )$ , called the a priori distribution. The idea is not to assume that the observed object really is the realisation of a random phenomenon with distribution $p ( \pmb { o } )$ . This distribution is simply taken to be representative of our a priori knowledge, i.e., it takes small values for reconstructed objects that would be barely compatible with the latter and larger values for highly compatible objects.

The Bayes rule23 provides a way of expressing the probability $p ( \pmb { o } \mid i )$ for the object $\pmb { o }$ that is conditional upon the measurement data $_ i$ jas a function of the prior probability distribution $p ( \pmb { o } )$ of the object and the probability $p ( i \mid o )$ of the jmeasurements conditional upon the object. The latter contains our knowledge of the data formation model, including the noise model. This probability $p ( \pmb { o } \mid i )$ is jcalled the posterior distribution, since it is the probability of the object given the results of the measurements. The Bayes rule is (see Sect. 9.5)

$$
p ( \pmb { \mathscr { o } } \mid i ) = \frac { p ( i \mid \pmb { \mathscr { o } } ) \times p ( \pmb { \mathscr { o } } ) } { p ( i ) } \propto p ( i \mid \pmb { \mathscr { o } } ) \times p ( \pmb { \mathscr { o } } ) .
$$

Using the last expression, how should we choose the reconstructed object $\hat { \pmb { o } }$ that Owould best estimate the true object? One commonly made choice is the maximum a posteriori (MAP) estimator. The idea is to define as solution the object that maximises the posterior distribution $p ( \pmb { o } | i )$ , so that

$$
\sigma _ { \mathrm { M A P } } = \arg \operatorname* { m a x } _ { o } p ( o \mid i ) = \arg \operatorname* { m a x } _ { o } p ( i \mid o ) \times p ( o ) .
$$

This is the most likely object given the data and our prior knowledge. The posterior distribution, viewed as a function the object, is called the posterior likelihood. Through (9.89), it takes into account the measurement data $_ i$ , the data formation model, and any prior knowledge of the object. In particular, it should be noted that, when the prior distribution $p ( \pmb { o } )$ is constant, i.e., when we have no information about the object, the MAP estimator reduces to the maximum likelihood method.

It can be shown that choosing the MAP estimator amounts to minimising the mean risk (see Sect. 9.5) for a particular cost function called the all-or-nothing cost function. However, this goes beyond the scope of this introduction to inverse problems. Other choices of cost function, such as a choice of $\hat { \pmb { o } }$ minimising the mean squared error with respect to the true object $\mathbf { \delta } _ { \pmb { o } }$ Ounder the posterior probability distribution, can also be envisaged, but they generally lead to longer computation times for obtaining the solution.24

# Equivalence with Minimisation of a Regularised Criterion

Maximising the posterior likelihood is equivalent to minimising a criterion $J _ { \mathrm { M A P } } ( \pmb { o } )$ defined as minus its logarithm. According to (9.90), this criterion can be written as the sum of two terms, viz.,

$$
J _ { \mathrm { M A P } } ( o ) = - \ln p ( i \mid o ) - \ln p ( o ) = J _ { \mathrm { i } } ( o ) + J _ { \mathrm { o } } ( o ) ,
$$

where $J _ { \mathrm { i } }$ is the data fidelity criterion deduced from the likelihood [see (9.84)], which is often a least-squares criterion, while $J _ { \mathrm { o } } ( \pmb { o } ) \triangleq - \ln p ( \pmb { o } )$ is a regularisation or penalisation criterion (for the likelihood) which reflects faithfulness to prior knowledge.

The expression for the MAP solution as the object that minimises the criterion (9.91) shows clearly that it achieves the compromise between faithfulness to the data and faithfulness to prior knowledge asserted at the beginning of this section.

When $\pmb { o }$ is not a realisation of a random phenomenon with some probability distribution $p ( \pmb { o } )$ , e.g., in the case of image restoration, $J _ { \mathrm { o } } ( \pmb { o } )$ generally includes a multiplicative factor called the regularisation coefficient or hyperparameter.25 Its value controls the exact position of the compromise. Unsupervised, i.e., automatic, fitting methods exist for this coefficient, but they go beyond the scope of this introductory account.26

# The Linear and Gaussian Case. Relation with the Wiener Filter

Here we consider the case where the data model is linear [see (9.75)], the noise is assumed to be Gaussian, and the prior probability distribution adopted for the object is also Gaussian,27 with mean $\overline { { \pmb { o } } }$ and covariance matrix $C _ { 0 }$ :

$$
p ( \pmb { \sigma } ) \propto \exp \left[ - \frac { 1 } { 2 } ( \pmb { o } - \overline { { \pmb { o } } } ) ^ { \mathrm { T } } C _ { \circ } ^ { - 1 } ( \pmb { o } - \overline { { \pmb { o } } } ) \right] .
$$

Using (9.85), we see that the criterion to minimise in order to obtain the MAP solution is

$$
J _ { \mathrm { M A P } } ( \boldsymbol { o } ) = \frac { 1 } { 2 } ( \dot { \iota } - H \boldsymbol { o } ) ^ { \mathrm { T } } C _ { \mathrm { n } } ^ { - 1 } ( \dot { \iota } - H \boldsymbol { o } ) + \frac { 1 } { 2 } ( \boldsymbol { o } - \overline { { \boldsymbol { o } } } ) ^ { \mathrm { T } } C _ { \circ } ^ { - 1 } ( \boldsymbol { o } - \overline { { \boldsymbol { o } } } ) .
$$

This criterion is quadratic in $\pmb { o }$ and thus has analytic minimum, obtained by setting the gradient equal to zero:

$$
\begin{array} { r } { \hat { \boldsymbol \sigma } _ { \mathrm { M A P } } = \left( H ^ { \mathrm { T } } C _ { \mathrm { n } } ^ { - 1 } H + C _ { \mathrm { o } } ^ { - 1 } \right) ^ { - 1 } \left( H ^ { \mathrm { T } } C _ { \mathrm { n } } ^ { - 1 } \boldsymbol { i } + C _ { \mathrm { o } } ^ { - 1 } \overline { { \boldsymbol \sigma } } \right) . } \end{array}
$$

Several remarks can throw light upon this otherwise slightly dull looking result. To begin with, the maximum likelihood solution is obtained by taking $C _ { \mathrm { o } } ^ { - 1 } = 0$ in Dthis equation. Incidentally, this shows that this solution corresponds in the Bayesian framework to assuming an infinite energy for $\mathbf { \delta } _ { \pmb { o } }$ . Then if we also take $C _ { \mathrm { n } }$ proportional to the identity matrix, we see that we recover precisely the least-squares solution of (9.79).

Finally, the case of deconvolution is particularly enlightening. The noise is assumed stationary with power spectral density (PSD) $S _ { \mathrm { n } }$ , while the prior probability distribution for the object is also assumed stationary with PSD $S _ { \mathrm { o } }$ . For all the relevant quantities, we make the same periodicity approximation as on p. 583 when examining the relation between least squares and inverse filter. All the matrices in (9.94) are then diagonalised in the same discrete Fourier basis, and the solution can be written in this basis, with ordinary rather than matrix multiplications and inverses:

$$
\tilde { \partial } _ { \mathrm { M A P } } ( u ) = \frac { \tilde { h } ^ { * } ( u ) } { | \tilde { h } | ^ { 2 } ( u ) + S _ { \mathrm { n } } / S _ { \mathrm { o } } ( u ) } \tilde { i } ( u ) + \frac { S _ { \mathrm { n } } / S _ { \mathrm { o } } ( u ) } { | \tilde { h } | ^ { 2 } ( u ) + S _ { \mathrm { n } } / S _ { \mathrm { o } } ( u ) } \tilde { \overline { { \sigma } } } ( u ) .
$$

In this expression, $S _ { \mathrm { n } } / S _ { \mathrm { o } } ( { \pmb u } )$ is the reciprocal of a signal-to-noise ratio at the spatial frequency $\pmb { u }$ and $\tilde { \mathbf { \Gamma } }$ is the Fourier transform of the a priori object, generally taken to be zero or equal to an object of constant value.

This expression is just the Wiener filter (see Sect. 9.1.3) for the case where the a priori object is not zero. For frequencies where the signal-to-noise ratio is high, this solution tends toward the inverse filter, and for frequencies where this ratio is low, the solution tends toward the a priori object. It can even be seen that, at each spatial frequency $\pmb { u }$ , the solution is on a segment that connects the maximum likelihood solution (inverse filter) to the a priori solution, with the position on the segment given by the signal-to-noise ratio:

$$
\tilde { \sigma } _ { \mathrm { M A P } } ( \boldsymbol { u } ) = \alpha \frac { \tilde { i } { ( \boldsymbol { u } ) } } { \tilde { h } } + ( 1 - \alpha ) \tilde { \bar { \sigma } } ( \boldsymbol { u } ) ,
$$

where

$$
\alpha = \frac { | \tilde { \pmb { h } } | ^ { 2 } ( \pmb { u } ) } { | \tilde { \pmb { h } } | ^ { 2 } ( \pmb { u } ) + S _ { \mathrm { n } } / S _ { 0 } ( \pmb { u } ) } .
$$

This expression clearly illustrates the fact that regularisation achieves a compromise between bias and variance that enables us to reduce the estimation error. The mean squared error on the estimated object is the square root of the sum of the squared bias and the variance of the estimator. The solution of the inverse filter (obtained for $S _ { \mathrm { n } } / S _ { \mathrm { o } } ~ = ~ 0 )$ has zero bias but amplifies the noise in an uncontrolled way, Di.e., has unbounded variance. Compared with the maximum likelihood solution, the solution (9.95) is biased toward the a priori solution $\overline { { \pmb { o } } }$ . By accepting this bias, we can significantly reduce the variance and globally reduce the mean squared error on the estimated object.

# Application to Wavefront Reconstruction

We return to the example of wavefront reconstruction from data provided by a Hartmann–Shack sensor, as discussed in Sect. 9.6.3. The noise is still assumed to be Gaussian and white with covariance matrix $C _ { \mathrm { n } } = \sigma ^ { 2 } I$ . We assume that the phase Dobeys Kolmogorov statistics and is therefore Gaussian, with known covariance matrix $C _ { 0 }$ , and depends only on the Fried parameter $r _ { 0 }$ which quantifies the strength of turbulence. The true phase has spatial variance $\sigma _ { \varphi } ^ { 2 } = 3 . 0 \ \mathrm { r a d } ^ { 2 }$ . The most likely Dphase given the measurements and taking into account this a priori information is the MAP solution given by (9.94). This solution is shown in Fig. 9.16. The estimation error corresponds to a spatial variance $\sigma _ { \mathrm { e r r } } ^ { 2 } = 0 . 7 ~ \mathrm { r a d } ^ { 2 }$ , which is lower than the Dbest solutions obtained previously by truncating the representation of the phase to a small number of Zernike polynomials $( \sigma _ { \mathrm { e r r } } ^ { 2 } = 0 . 8 \mathrm { r a d } ^ { 2 }$ , obtained for $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } } = 5 5$ ).

![](images/30cefda75073c746e068fbb9c88458d40198220b5437d616139a26fac0e4c9e5.jpg)  
Fig. 9.16 Comparing reconstructed phases on a pupil. Left: Simulated turbulent phase, to be estimated. Centre: Phase estimated by MAP. Right: Best phase estimated by maximum likelihood on a truncated basis

The MAP solution takes advantage of a priori knowledge of the spatial statistics of the turbulence. To use this in adaptive optics, where the sample rate is generally well above $1 / \tau _ { 0 }$ , it is judicious to opt for a natural extension of this estimator that also exploits a priori knowledge of the temporal statistics of the turbulence. This extension is the optimal estimator of Kalman filtering.

# 9.6.5 Application to Adaptive Optics Imaging

Here we apply these tools to solve a specific inverse problem, namely, adaptive optics imaging. We shall illustrate with several examples, either by simulation or by the processing of genuine astronomical observations.

# Ingredients of the Deconvolution

Long exposure images corrected by adaptive optics (AO) must be deconvolved, because the correction is only partial. Considering that the PSF $\pmb { h }$ is known, the object $ { \hat { \mathbf { o } } } _ { \mathrm { M A P } }$ estimated by MAP is given by (9.90), i.e., it minimises the criterion O(9.91). Let us see how to define the two components of this criterion.

To be able to measure objects with high dynamic range, which are common in astronomy, the data fidelity term $J _ { \mathrm { i } }$ must incorporate a fine model of the noise, taking into account both photon noise and electronic noise. This can be done by treating the photon noise as a non-stationary Gaussian noise, and it leads to a weighted leastsquares criterion $J _ { \mathrm { i } }$ [see (9.86)] rather than an ordinary least-squares term.

For objects with sharp edges, such as artificial satellites, asteroids, or planets, a Gaussian prior (like the one leading to the Wiener filter on p. 590), or equivalently, a quadratic regularisation criterion, tends to smooth the edges and introduce spurious oscillations or ringing in their vicinity. One interpretation of this effect is that, when minimising the criterion $J _ { \mathrm { M A P } } ( \pmb { o } )$ , a quadratic regularisation attributes to a step a cost proportional to the square of its value, e.g., at the edge of an object, where there is a large difference in value between adjacent pixels. One solution is then to use an edge-preserving criterion, such as the so-called quadratic–linear or $L _ { 2 } L _ { 1 }$ criteria. These are quadratic for small discontinuities and linear for large ones. The quadratic part ensures good noise smoothing and the linear part cancels edge penalisation.

In addition, for many different reasons, we are often led to treat the PSF $\pmb { h }$ as imperfectly known. Carrying out a classic deconvolution, i.e., assuming that the point spread function is known but using an incorrect point spread function, can lead to disastrous results. Conversely, a so-called blind deconvolution, where the same criterion (9.91) is minimised but simultaneously seeking $\pmb { o }$ and $\pmb { h }$ , is highly unstable, rather like unregularised methods. A myopic deconvolution consists in jointly estimating both $\mathbf { \delta } _ { \pmb { o } }$ and $\pmb { h }$ in a Bayesian framework with a natural regularisation for the point spread function and without having to fit an additional hyperparameter. The joint MAP estimator is given by

$$
\begin{array} { l } { { ( \hat { o } , \hat { h } ) = \mathop { \arg \operatorname* { m a x } } _ { o , h } p ( o , h | i ) = \mathop { \arg \operatorname* { m a x } } _ { o , h } p ( i | o , h ) \times p ( o ) \times p ( h ) } } \\ { { \qquad = \mathop { \arg \operatorname* { m i n } } _ { o , h } \Big [ J _ { i } ( o , h ) + J _ { o } ( o ) + J _ { h } ( h ) \Big ] , } } \end{array}
$$

where $J _ { h }$ is a regularisation criterion for $\pmb { h }$ , which introduces constraints on the possible variability of the PSF.

The next section presents experimental results obtained by the MISTRAL restoration method,28 which combines the three ingredients discussed above: fine noise modelling, non-quadratic regularisation, and myopic deconvolution.

# Image Restoration from Experimental Astronomical Data

Figure 9.17a shows a long exposure image of Ganymede, a natural satellite of Jupiter, corrected by adaptive optics. This image was made on 28/09/1997 on ONERA’s adaptive optics testbed installed on the $1 . 5 2 \mathrm { ~ m ~ }$ telescope at the Observatoire de Haute-Provence in France. The imaging wavelength is $\lambda \ : = \ : 0 . 8 5 \mathrm { \ : \mu m }$ and the exposure time is $1 0 0 \mathrm { s } .$ . The estimated total flux is $8 \times 1 0 ^ { 7 }$ Dphotons and the estimated ratio $D / r _ { 0 }$ is 23. The total field of view is 7.9 arcsec, of which only half is shown here. The mean and variability of the point spread function were estimated from recordings of 50 images of a bright star located nearby. Figures 9.17b and c show restorations obtained using the Richardson–Lucy algorithm (ML for Poisson noise), stopped after 200 and 3 000 iterations, respectively.29 In the first case, similar to restoration with quadratic regularisation, the restored image is somewhat blurred and displays ringing, while in the second, very similar to the result of inverse filtering, noise dominates the restoration.

![](images/fe7ae2e62165861695695fd41fdb326927e6f3cdfa9440e1778b58edca837550.jpg)  
Fig. 9.17 (a) Corrected image of Ganymede obtained using the ONERA adaptive optics testbed on 28 September 1997. (b) Restoration using the Richardson–Lucy algorithm, stopped after 200 iterations. (c) Likewise, but stopped after 3 000 iterations. From Mugnier, L. et al., Chap. 10 of Idier, J. op. cit.

![](images/2accd8889effe86b388cece322c64d243b1f59a0913b0dd64757d6402c58fcaf.jpg)  
Fig. 9.18 (a) Deconvolution of the Ganymede image in Fig. 9.17 by MISTRAL. (b) Comparison with a wide band synthetic image obtained using the NASA/JPL database. (c) The same synthetic image, but convolved by the perfect point spread function of a $1 . 5 2 \mathrm { m }$ telescope. From Mugnier, L.M. et al., MISTRAL: A myopic edge-preserving image restoration method, with application to astronomical adaptive-optics-corrected long-exposure images, J. Opt. Soc. Am. A 21, 1841–1854, 2004

Figure 9.18a shows a myopic deconvolution implementing an edge-preserving prior, while Fig. 9.18b is a wide band synthetic image obtained by a NASA/JPL space probe30 during a Ganymede flyby. Comparing the two, we find that many features of the moon are correctly restored. A fairer comparison consists in jointly examining the myopic deconvolution carried out by MISTRAL with the image of Fig. 9.18b convolved by the perfect PSF of a $1 . 5 2 \mathrm { ~ m ~ }$ telescope, as shown in Fig. 9.18c.

# 9.6.6 Application to Nulling Interferometry

We now discuss a second example of the inversion problem, this time relating to the detection of extrasolar planets by means of a nulling interferometer (see Sect. 6.6). With the Darwin instrument, or NASA’s Terrestrial Planet Finder Interferometer, both under study during the 2000s, data will be very different from an image in the conventional sense of the term, and their exploitation will require implementation of a specific reconstruction process. They will consist, at each measurement time $t$ , of an intensity in each spectral channel . This intensity can be modelled as the integral over a certain angular region of the instantaneous transmission map of the interferometer, denoted by $R _ { t , \lambda } ( \pmb \theta )$ , which depends on the time $t$ owing to rotation of the interferometer relative to the plane of the sky, multiplied by the intensity distribution $o _ { \lambda } ( \pmb \theta )$ of the observed object. The data model is thus linear, but notably non-convolutive, thus very different from the one used in imaging. The transmission map is a simple sinusoidal function in the case of a Bracewell interferometer, but becomes more complex when more than two telescopes interfere simultaneously.

By judiciously combining the data, and with asymmetrical transmission maps, the contribution to the measured signal of the components of the observed object with even spatial distribution can be eliminated. These components are stellar leakage, exozodiacal light, and a fortiori zodiacal light and thermal emission from the instrument itself (which have constant level in the field of view). It is then possible to seek out only planets during image reconstruction, which corresponds to the following object model:

$$
\pmb { o } _ { \lambda } ( \pmb { \theta } ) = \sum _ { k = 1 } ^ { N _ { \mathrm { s r c } } } F _ { k , \lambda } \delta ( \pmb { \theta } - \pmb { \theta } _ { k } ) ,
$$

where $N _ { \mathrm { s r c } }$ is the number of planets, assumed known here, and $F _ { k , \lambda }$ is the spectrum of the $k$ th planet in a spectral interval $[ \lambda _ { \operatorname* { m i n } } , \lambda _ { \operatorname* { m a x } } ]$ fixed by the instrument. This parametric model can substantially constrain the inversion in so as to counterbalance the fact that the data are distinctly poorer than an image.

With this model of the object, the data formation model is

$$
i _ { t , \lambda } = \sum _ { k = 1 } ^ { N _ { \mathrm { s r c } } } R _ { t , \lambda } ( \pmb \theta _ { k } ) F _ { k , \lambda } + n _ { t , \lambda } ,
$$

where $n _ { t , \lambda }$ is the noise, assumed to be white Gaussian, whose variance $\sigma _ { t , \lambda } ^ { 2 }$ can be estimated from the data and is assumed known here. The inverse problem to be solved is to estimate the positions $\pmb \theta _ { k }$ and spectra $F _ { k , \lambda }$ of the planets, these being grouped together into two vectors $( \pmb \theta , \pmb F )$ . The ML solution is the one that minimises the following weighted least-squares criterion, given the assumptions made about the noise:

$$
J _ { \mathrm { i } } ( \theta , F ) = \sum _ { t , \lambda } { \frac { 1 } { \sigma _ { t , \lambda } ^ { 2 } } } \left[ i _ { t , \lambda } - \sum _ { k = 1 } ^ { N _ { \mathrm { s r c } } } R _ { t , \lambda } ( \theta _ { k } ) F _ { k , \lambda } \right] ^ { 2 } .
$$

As we shall see from the reconstruction results, the inversion remains difficult under the high noise conditions considered here. The object model (9.98), separable into spatial and spectral variables, already contains all spatial prior information concerning the object. It is nevertheless possible to constrain the inversion even more by including the further knowledge that the spectra we seek are positive quantities (at all wavelengths), and furthermore that they are relatively smooth functions of the wavelength. The latter fact is taken into account by incorporating a spectral regularisation into the criterion to be minimised, which measures the roughness of the spectrum:

$$
J _ { \mathrm { o } } ( F ) = \sum _ { k = 1 } ^ { N _ { \mathrm { s r c } } } \mu _ { k } \sum _ { \lambda = \lambda _ { \mathrm { m i n } } } ^ { \lambda _ { \mathrm { m a x } } } \left( \frac { \partial ^ { m } F _ { k , \lambda } } { \partial \lambda ^ { m } } \right) ^ { 2 } ,
$$

where the $m$ th derivative of the spectrum $\mathbf { \Phi } _ { m } ~ = ~ 1$ or 2 in practice) is calculated by finite differences and where the $\mu _ { k }$ Dare hyperparameters used to adjust the weight allocated to the regularisation. The MAP solution is the one minimising the composite criterion $J _ { \mathrm { M A P } } ( \pmb \theta , \pmb F ) = J _ { \mathrm { i } } ( \pmb \theta , \pmb F ) + J _ { \mathrm { o } } ( \pmb F )$ . It is a rather delicate matter to D Cimplement this minimisation because there are many local minima. We use the fact that, for each assumed position $\pmb \theta$ of the planets, the MAP estimate of the spectra, $\hat { F } ( \pmb \theta )$ , can be obtained simply because $J _ { \mathrm { M A P } }$ is quadratic in the spectra $F$ . If the latter are replaced by $\hat { F } ( \pmb \theta ) ^ { 1 }$ in $J _ { \mathrm { M A P } }$ , we obtain a partially optimised function for minimisation, which now only depends explicitly on the positions:

$$
J _ { \mathrm { M A P } } ^ { \dagger } ( \pmb { \theta } ) = J _ { \mathrm { M A P } } \big [ \pmb { \theta } , \hat { \pmb { F } } ( \pmb { \theta } ) \big ] .
$$

This criterion is minimised by a sequential search for the planets, as in the CLEAN algorithm. Figure 9.19 shows the maps of $J _ { \mathrm { M A P } } ^ { \dagger }$ obtained for a single planet as a function of the prior information used. It is clear that the constraints of positivity and smoothness imposed on the spectra significantly improve estimates of the position of the planet, by discrediting (Fig. 9.19 right) positions compatible with the data (Fig. 9.19 left and centre) but corresponding to highly chaotic spectra.

Figure 9.20 shows the estimated spectrum of an Earth-like planet. As expected, spectral regularisation avoids noise amplification and has a beneficial effect on the estimate.

![](images/c4c308e051f9c1ea0782cd234ff9c3ec4a1887bea56f605d8a9b33e50d8432ba.jpg)  
Fig. 9.19 Likelihood maps for the position of a planet. Left: Likelihood alone. Centre: Likelihood under the constraint that spectra are positive. Right: MAP, i.e., likelihood penalised by a spectral regularisation criterion. The true position of the planet is at the bottom, slightly to the left, and clearly visible on the right-hand image. From Mugnier, L., Thiebaut, E., Belu, A., in ´ Astronomy with High Contrast Imaging III, EDP Sciences, Les Ulis, 2006, and also Thiebaut, E., Mugnier, L., ´ Maximum a posteriori planet detection with a nulling interferometer, in Proceedings IAU Conf. 200, Nice, 2006

![](images/6996ebf28dbc083f229007e258502a76b5da50162ef8f88a925d20faf5b9cc31.jpg)  
Fig. 9.20 Reconstructed spectrum at the estimated position of the planet. Red: Without regularisation. Green: With regularisation. Black: True spectrum of the Earth. Same reference as for Fig. 9.19

# Problems

Note. These exercises refer also to the subjects treated in Appendixes A and B.

9.1. In each of the three examples, use the Fourier transform on the left to deduce the one on the right. Fourier transform is indicated by an arrow:

$$
\begin{array} { l } { { \displaystyle { \frac { \sin x } { x } }  \pi \pi ( \pi s ) , ( \frac { \sin x } { x } ) ^ { 2 }  \Lambda ( \pi s ) , \ } } \\ { { \displaystyle { \mathrm { e } ^ { - x ^ { 2 } }  \sqrt { \pi } \mathrm { e } ^ { - \pi ^ { 2 } s ^ { 2 } } } , \qquad \delta ( a x )  \frac { 1 } { | a | } , \ } } \\ { { \displaystyle { \mathrm { e } ^ { - x ^ { 2 } / 2 \sigma ^ { 2 } }  \sqrt { 2 \pi \sigma } \mathrm { e } ^ { - 2 \pi ^ { 2 } \sigma ^ { 2 } s ^ { 2 } } } , \mathrm { e } ^ { \mathrm { i } x }  \delta ( s - \frac { 1 } { 2 \pi } ) . \ } } \end{array}
$$

9.2. Using the convolution theorem, give an expression for

$$
\mathbf { e } ^ { - a x ^ { 2 } } \star \mathbf { e } ^ { - b x ^ { 2 } } .
$$

(Problem 6.15 is an application of this result.)

Answer. The following property is used: the Fourier transform of a convolution product is the pointwise product of the Fourier transforms of the factors in that product. This property is very useful in numerical calculations, the algorithms for multiplication being so much more rapid. Linearity and similarity properties are also used in the following deduction:

$$
\begin{array} { r l } & { F ( x ) = \mathrm { e } ^ { - a x ^ { 2 } } \star \mathrm { e } ^ { - b x ^ { 2 } } } \\ & { \qquad = \mathrm { F T } \left[ \mathrm { F T } \left[ \mathrm { e } ^ { - a x ^ { 2 } } \right] \cdot \mathrm { F T } \left[ \mathrm { e } ^ { - b x ^ { 2 } } \right] \right] } \\ & { \qquad = \mathrm { F T } \left[ \sqrt { \cfrac { \pi } { a } } \mathrm { e } ^ { - x ^ { 2 } / a } \sqrt { \cfrac { \pi } { b } } \mathrm { e } ^ { - x ^ { 2 } / b } \right] } \\ & { \qquad = \frac { \pi } { \sqrt { a b } } \mathrm { F T } \left[ \exp \left( - \frac { a + b } { a b } x ^ { 2 } \right) \right] , } \end{array}
$$

so that, finally,

$$
F ( x ) = { \frac { \pi ^ { 3 / 2 } } { \sqrt { a + b } } } \exp \left( - { \frac { a b } { a + b } } x ^ { 2 } \right) .
$$

9.3. Prove the Wiener–Khinchine theorem: The autocorrelation and spectral density are a Fourier pair. Apply it to the case of a time-dependent electric current $i ( t )$ , and its Fourier transform $\tilde { i } ( \nu )$ , where $\nu$ is a temporal frequency, and thus interpret the theorem physically in terms of power.

9.4. Compare the FTs of the convolution and the correlation products of two functions.

9.5. A signal $X ( t )$ , whose spectrum has bounded support, passes through a linear filter which has instantaneous response $F ( t )$ . Let $Y ( t )$ be the output signal. $X ( t )$ and $Y ( t )$ are sampled, giving sequences of results $\{ X _ { i } \}$ and $\left\{ Y _ { i } \right\}$ . Show that

$$
\{ Y _ { i } \} = \{ I _ { i } \} \star \{ X _ { i } \} .
$$

How can the sequence $\left\{ I _ { i } \right\}$ be found?

9.6. Filtering by Running Mean (Smoothing). Let $x ( t ) = x _ { \mathrm { s } } + n ( t )$ be a signal, where $x _ { \mathrm { s } }$ is a constant to be determined, and $n ( t )$ D Cis the stationary random noise affecting the measurement, such that $\langle n ( t ) \rangle = 0$ . Define

$$
y _ { T } ( t ) = \frac { 1 } { T } \int _ { t } ^ { t + T } x ( \theta ) \mathrm { d } \theta ,
$$

which is called the running mean of $x ( t )$ . Put $y _ { T } ( t )$ into the form of a convolution, and deduce that it is the result of a linear filtering of $x ( t )$ . Determine the transfer function $\tilde { H } ( f )$ of this filter, and its equivalent bandpass $\Delta f$ defined by

$$
\Delta f = \int _ { - \infty } ^ { + \infty } | \tilde { H } ( f ) | ^ { 2 } \mathrm { d } f .
$$

Answer. An expression equivalent to the running mean is given, up to a translation by $T / 2$ , by

$$
y _ { T } ( t ) = x ( t ) \star { \frac { 1 } { T } } \varPi \left( { \frac { t } { T } } \right) .
$$

The running mean is therefore the result of linear filtering by the filter

$$
\tilde { H } ( f ) = \mathrm { s i n c } ( T f ) ,
$$

and so, by Parseval’s theorem,

$$
\Delta f = \int \left| { \frac { 1 } { T } } \pi \left( { \frac { t } { T } } \right) \right| ^ { 2 } { \mathrm { d } } t = { \frac { 1 } { T } } .
$$

9.7. Find the autocorrelation function $R ( \tau )$ of a Gaussian process after filtering by the linear filter

$$
\tilde { H } ( \nu ) = \frac { 1 } { 1 + ( 2 \pi R C \nu ) ^ { 2 } } .
$$

9.8. Consider a stochastic process $\mathbf { x } ( t )$ . Define a new process ${ \bf x } _ { T } ( t )$ , referred to as the estimate of the mean of ${ \bf x } ( t )$ , by

$$
x _ { T } ( t ) = \frac { 1 } { 2 T } \int _ { t - T } ^ { t + T } x ( t ) \mathrm { d } t .
$$

Show that, when ${ \bf x } ( t )$ is stationary,

$$
\langle x _ { T } ( t ) \rangle = \langle x ( t ) \rangle = \eta ,
$$

and

$$
\sigma _ { { \bf x } _ { T } } ^ { 2 } = \frac { 1 } { 4 T ^ { 2 } } \int _ { - T } ^ { + T } \int _ { - T } ^ { + T } C ( t _ { 1 } - t _ { 2 } ) \mathrm { d } t _ { 1 } \mathrm { d } t _ { 2 } ,
$$

where

$$
C ( t _ { 1 } - t _ { 2 } ) = R ( t _ { 1 } - t _ { 2 } ) - \eta ^ { 2 } .
$$

Express $\sigma _ { \mathbf { x } _ { T } } ^ { 2 }$ as a function of $t _ { 1 } - t _ { 2 } = \tau$

 DApply this result to the filtering process in Problem 9.7 and deduce a simple analytic form for its variance. Graph the quantity $\sigma _ { \mathbf { x } _ { T } } ^ { 2 } ( \tau )$ and give a simple interpretation.

Apply these results to the following astrophysical problem, frequently encountered in Fourier transform spectroscopy, speckle interferometry, the study of solar oscillations, and other areas. An astronomer wishes to measure the spectral density of a process $\mathbf { x } ( t )$ , which he knows to be normal and centred. Give a practical procedure for doing this. What value of $T$ should be chosen so that the estimate of the spectral density $S _ { T } ( \nu )$ will lie within a previously chosen confidence interval?

9.9. Optimal Sampling Rate and Shannon’s Theorem. In a turbulent fluid, viscous dissipation gives a wave number cutoff $\kappa _ { \mathrm { M } }$ to the spectrum of spatial frequencies in the turbulence (see Chap. 2). Assuming the medium to be isotropic, what geometrical arrangement of temperature sensors should be set up in order to be able to reconstruct by interpolation the full temperature distribution of the medium?

A sinusoidal plane temperature wave, with wave number $\kappa _ { 0 }$ in a given direction, is superposed upon the turbulence. How is the spectral density modified?

9.10. Shannon Optimal Sampling Rate. The aim is to determine to great accuracy the period $T _ { \mathfrak { p } }$ of the Vela optical pulsar PSR 0833-45 (Fig. 7.9), knowing that it is close to $8 9 \mathrm { m s }$ . The signal is received by a photomultiplier and then sampled at the frequency $f _ { \mathrm { S } }$ . The dark current of the detector produces Poissonian noise, with a white spectral density up to $f _ { \mathrm { c } } \gg f _ { \mathrm { p } }$ , where $f _ { \mathrm { p } } = 1 / T _ { \mathrm { p } }$ . What is the optimal value of $f _ { \mathrm { S } } \mathrm { ? }$ DDetermine the signal-to-noise ratio if the measurement lasts for a time $T$ (assuming availability of all the required quantities: the magnitude of the pulsar, the transmission and quantum efficiency of the setup, the aperture of the telescope, and the noise current).

Show that $f _ { \mathrm { S } }$ must be modified if information is sought concerning the shape of the periodic signal, and explain how it must be modified. What would be the effect of such a change on the signal-to-noise ratio of the PSD?

9.11. Digitisation and Truncation. Consider two centred normal processes ${ \bf x } ( t )$ and $\mathbf { y } ( t )$ , with the same variance $\sigma ^ { 2 }$ , whose correlation is given by

$$
\langle x ( t ) y ( t ) \rangle = \rho \sigma ^ { 2 } .
$$

This is equivalent to the joint probability distribution

$$
\begin{array} { r l } & { \mathrm { p r o b } \{ X \le \mathbf { x } < X + \mathrm { d } X , ~ Y \le \mathbf { y } < Y + \mathrm { d } Y \} } \\ & { \qquad = \frac { 1 } { 2 \pi \sigma ^ { 2 } ( 1 - \rho ^ { 2 } ) ^ { 1 / 2 } } \exp \left[ - \frac { X ^ { 2 } + Y ^ { 2 } - 2 \rho X Y } { 2 \sigma ^ { 2 } ( 1 - \rho ^ { 2 } ) } \right] . } \end{array}
$$

Let $a _ { i }$ and $b _ { i }$ be samples of $x ( t )$ and $y ( t )$ taken at regular intervals $t _ { i }$ . Instead of digitising $x$ and $y$ , only their signs are recorded:

$$
a _ { i } = \left\{ { \begin{array} { l l } { + 1 { \mathrm { ~ i f ~ } } } & { x ( t ) \geq 0 , } \\ { - 1 { \mathrm { ~ i f ~ } } } & { x ( t ) < 0 , } \end{array} } \right.
$$

and similarly for $b _ { i }$ with reference to $y ( t )$ . This digitisation on one bit is extremely rapid. Show that the correlation between the new discrete random variables $a _ { i }$ and $b _ { i }$ is given by

$$
\langle a _ { i } b _ { i } \rangle = \frac { 2 } { \pi } \arcsin \rho ,
$$

so that, for weak correlation $\rho \ll 1$ ,

$$
\langle a _ { i } b _ { i } \rangle \sim \frac { 2 \rho } { \pi } \propto \langle x ( t ) y ( t ) \rangle .
$$

Assume that the spectral densities of $x ( t )$ and $y ( t )$ have bounded support (filtered signals). Let $R ( \tau )$ be the autocorrelation of the processes a and $\mathbf { b }$ , and $S ( \nu )$ their cross-spectrum (the FT of $R$ ). Show that the signal-to-noise ratio for an estimate of $S$ is only a factor $2 / \pi$ less than the signal-to-noise ratio that would be obtained by measuring the original processes $\mathbf { X }$ and $\mathbf { y }$ over the same period of time. Real time digital correlators use this property, referred to as clipping, to increase their speed of calculation.

9.12. The whole visible face of the Sun (integrated flux) is observed with a highresolution spectrometer (see Sect. 8.3.3), in the wing of an absorption line of the photosphere. The received intensity is highly-dependent on the Doppler shift of the line, which in turn depends on the line-of-sight component of the mean velocity. Once the Doppler effects due to the various relative motions of the Sun and the Earth have been corrected for, any non-zero residue is interpreted as a large scale oscillation of the Sun’s surface. A period of $1 6 0 \mathrm { m i n }$ is observed.

What is the optimal sampling of the signal? At non-polar latitudes on Earth, only daytime observation is possible. What effect does this truncation have on the observed spectrum? Show that it will contain artificial or ghost lines. If, in addition, randomly occurring cloud formations sometimes prevent sampling, what will be their effect on the PSD? This could be simulated on a personal computer. (See Grec G. et al., Nature 288, 541, 1980, for a description of such observations.)

9.13. The spectral density of an image of photospheric solar granulation, observed in white light, is given in Fig. 9.21. The frame has dimensions $1 3 \times 1 3$ arcsec. What is the spatial frequency resolution obtained in the figure? The calculation has been simplified by replacing each granulation cell by a Dirac spike. How can the calculated two-dimensional PSD be interpreted, and in particular, the apparent hexagonal structure at low frequency and the noise at high frequency?

![](images/5006120b5bba2f12935e9f838daba23cd733680c9f4888f1a384b12f813a85a0.jpg)  
Fig. 9.21 Spectral density of solar granulation. From Aime C. et al., Astr. Ap. 79, 1, 1979. With the kind permission of Astronomy and Astrophysics

9.14. Given the brightness of the sky background around $5 0 0 ~ \mathrm { { n m } }$ (see Sect. 2.3), determine the number of counts resulting from the sky background given by each pixel of a CCD (quantum efficiency $\eta \ : = \ : 0 . 6 ,$ , observing a field of $2 \times 2$ arcsec through a $3 . 6 \mathrm { m }$ Dtelescope, whose transmission is assumed to be $100 \%$ . What is the limiting magnitude of a galaxy which could be detected against this background, with a reasonable degree of confidence, in an observation lasting one hour? (Be careful not to confuse the sky background with the fluctuation of this background.) What would be gained by observing over one month, or one year?

Answer. According to Sect. 2.3.1, the sky has magnitude $m _ { \mathrm { V } } = 2 2$ arcsec $^ { - 2 }$ , which implies a sky background flux per square arcsec given by

$$
F _ { \mathrm { c } } = 3 . 9 2 \times 1 0 ^ { - 8 } \cdot 1 0 ^ { - 2 2 / 2 . 5 } = 6 . 2 1 \times 1 0 ^ { - 1 7 } \mathrm { { W m ^ { - 2 } \mu { \mathrm { m } } ^ { - 1 } \mathrm { { a r c s e c } ^ { - 2 } . } } }
$$

The number of counts due to the sky background is

$$
{ n _ { \mathrm { c } } = F _ { \mathrm { c } } S \varOmega t / ( h c / \lambda ) , }
$$

where $S$ is the collecting area of the telescope, and hence $S = 1 . 8 ^ { 2 } \pi \mathrm { ~ m } ^ { 2 }$ , $t$ is the integration time, $\varOmega$ Dis the solid angle subtended at each pixel, namely 4 arcsec2, and $h c / \lambda$ is the energy of each photon.

The number of photons required from the galaxy in order to give a reasonable confidence interval $( 3 \sigma )$ is

$$
n _ { \mathrm { g } } = 3 \sqrt { F _ { \mathrm { c } } S \varOmega t / ( h c / \lambda ) } ,
$$

implying a flux from the galaxy of

$$
\begin{array} { l } { { F } _ { \mathrm { g } } = n _ { \mathrm { g } } ( h c / \lambda ) / S t } \\ { = 3 \sqrt { ( h c / \lambda ) \Omega { F } _ { \mathrm { c } } / S t } \quad \mathrm { W } \mathrm { m } ^ { - 2 } \mu \mathrm { m } ^ { - 1 } . } \end{array}
$$

Note that the smallest detectable flux varies as $t ^ { - 1 / 2 }$ .

For $t ~ = ~ 3 6 0 0 ~ \mathrm { s }$ , $F _ { \mathrm { g } } ~ = ~ 1 . 5 6 \times 1 0 ^ { - 1 9 } { \mathrm { W } } { \mathrm { m } } ^ { - 2 } { \mu \mathrm { m } } ^ { - 1 }$ , which corresponds to a magnitude $m _ { \mathrm { V } } = 2 8 . 5$ D. For $t = 1$ month, a factor of ${ \sqrt { 2 4 \times 3 0 } } = 2 6 . 8$ is gained, D Dcorresponding to 3.5 magnitudes. For $t = 1$  Dyear, only a further 1.35 magnitudes is Dgained. This does assume that the noise remains stationary over such long periods.

9.15. A photoconducting infrared detector is placed at the focus of a $4 \mathrm { m }$ telescope, with a field of view of 10 arcsec, in the photometric $_ \mathrm { N }$ band, of spectral width $0 . 5 ~ { \mu \mathrm { m } }$ . Two terms contribute to the received signal. Firstly, the flux of photons emitted by the star, and secondly, the emission of the Earth’s atmosphere, with emissivity $\varepsilon ( \lambda )$ . How can $\varepsilon ( \lambda )$ be evaluated (Sect. 2.3)?

Taking $\varepsilon ( \lambda ) ~ = ~ 0 . 5$ for the site under consideration, calculate the thermal Datmospheric background noise. What is the limiting magnitude $m _ { \mathrm { N } }$ imposed by this background for an observation of duration $1 \mathrm { ~ s ~ }$ , or $1 \ \mathrm { h r } ?$ Suggest ways of improving the observation.

9.16. Lock-in Detection. A procedure for extracting a signal from noise. In order to extract a signal, drowned out by noise, any available information concerning the signal, such as positivity, periodicity, and so on, should be put to use, with a view to reducing the final uncertainty. Detection is particularly simple if both the frequency and the phase of the signal are known. In Fig. 9.22, the radiation $\mathbf { x } ( t )$ is periodically modulated by a rotating disk (or some equivalent device), with frequency $\omega$ and

![](images/eeba2642c146586d1c91b4611f2f18392baa256493e2b4495053a1489c4d2113.jpg)  
Fig. 9.22 Signal modulated by a rotating disk

phase $\phi$ . The signal measured is then

$$
X _ { 0 } ( t ) = n ( t ) + x ( t ) F ( t ) ,
$$

where $n ( t )$ is the detector noise, $F ( t )$ the periodic, and in general non-sinusoidal, function characterising the chopper.

The following operations are then carried out, using either analogue electronic or digital techniques:

• Filtering, $X _ { 1 } ( t ) ~ = ~ X _ { 0 } ( t ) \star H ( t )$ , where $H ( t )$ is a narrow passband filter, $\Delta \omega \ll \omega$ D, centred on $\omega$ .   
• Multiplication, $X _ { 2 } ( t ) = X _ { 1 } ( t ) \cos ( \omega t + \phi ^ { \prime } )$ .   
D C• Low-frequency filtering, for example, by running mean,

$$
X _ { 3 } ( t ) = X _ { 2 } ( t ) \star \varPi ( t / T ) , \quad \mathrm { w i t h } \quad T \gg 2 \pi / \omega .
$$

Show that this sequence of operations only leaves the part of the noise $n ( t )$ with power spectrum in $\Delta \omega$ , and then uses the phase information. In the case of white noise, estimate the output signal-to-noise ratio. If ${ \bf x } ( t )$ is random (e.g., a Poissonian process for the arrival of photons), what is the effect on the measurement?
