![](images/fe116a9ce0d307dcae5a3031e6c4b4ad9d0f52f06ec0c7e4cd95916720eee261.jpg)  
Fig. 8.21 Solar spectroheliogram obtained in the H˛ line. Image courtesy of Henoux J.-C., Observatoire de Paris Meudon, 1985

If $x$ is the difference in the path length (Fig. 8.22) of the two waves, the exit intensity is given by

$$
\tilde { I } ( x ) = \frac { I _ { 0 } } { 2 } ( 1 + \cos 2 \pi \sigma x ) ,
$$

for monochromatic incident intensity $I _ { 0 }$ of wave number $\sigma$ . An arbitrary source whose intensity has a spectral distribution $I _ { 0 } ( \sigma )$ limited to the range $[ \sigma _ { 1 } , \sigma _ { 2 } ]$ , produces the signal

$$
\tilde { I } ( x ) = \frac { 1 } { 2 } \int _ { \sigma _ { 1 } } ^ { \sigma _ { 2 } } I _ { 0 } ( \sigma ) ( 1 + \cos 2 \pi \sigma x ) \mathrm { d } \sigma .
$$

This signal, referred to as an interferogram, is measured by the detector placed at the exit. Up to a constant, it is the Fourier cosine transform of the spectrum of the object. This is spectral multiplexing since, for each value of $x$ , all the spectral elements of the incident spectrum contribute to the signal, each one being coded by a cosine function orthogonal to the others.

Recovering the Source Spectrum

$I _ { 0 } ( \sigma )$ can be recovered by inverse Fourier transformation. After subtracting the mean value

$$
\langle \tilde { I } ( x ) \rangle = \frac { 1 } { 2 } \int _ { \sigma _ { 1 } } ^ { \sigma _ { 2 } } I _ { 0 } ( \sigma ) \mathrm { d } \sigma ,
$$

we obtain

$$
I _ { 0 } ^ { \prime } ( \sigma ) = \mathrm { F T } \left[ \tilde { I } ( x ) - \langle \tilde { I } ( x ) \rangle \right] .
$$

![](images/d5a2db1fa30dd63f41efaf3d5f983d3b0e22129a81e7687a448ed4fa804bc453.jpg)  
Fig. 8.22 Optics of a Fourier transform spectrometer

If $\tilde { I } ( x )$ were known over the whole interval $x ~ \in ~ ( - \infty , + \infty )$ , $I _ { 0 } ^ { \prime }$ would equal $I _ { 0 }$ . When $\tilde { I } ( x )$ is only known on an interval $[ - x _ { \mathrm { m } } / 2 , + x _ { \mathrm { m } } / 2 ]$ , it can be shown (Problem 8.1) that

$$
I _ { 0 } ^ { \prime } ( \sigma ) = I _ { 0 } ( \sigma ) \star \mathrm { s i n c } ( x _ { \mathrm { m } } \sigma ) ,
$$

and the recovered spectrum differs from $I _ { 0 }$ by a degradation in resolution due to this convolution.

Resolution

The interferogram of a monochromatic source $I _ { 0 } ( \sigma ) = \delta ( \sigma - \sigma _ { 0 } )$ is the instrumental profile

$$
\mathrm { s i n c } ( x _ { \mathrm { m } } \sigma ) \star \delta ( \sigma - \sigma _ { 0 } ) ,
$$

where $x _ { \mathrm { m } }$ is the maximum optical path length difference. The first zero of the instrumental profile occurs at

$$
\sigma - \sigma _ { 0 } = \pm \frac { 1 } { x _ { \mathrm { m } } } ,
$$

and it is assumed that this value gives the separation at which it is just possible to discriminate between two lines. The resolution is therefore

$$
R = { \frac { \sigma _ { 0 } } { \Delta \sigma } } = x _ { \mathrm { m } } \sigma _ { 0 } .
$$

When high resolutions are sought, the size of the interferometer is determined by the displacement amplitude (equal to $x _ { \mathrm { m } } / 2$ ) of a moveable mirror. This size is therefore $\lambda R / 2$ , and comparable to the size of a grating spectrometer with the same resolution. In a typical application, $\lambda ~ = ~ 0 . 5 ~ { \mu \mathrm { m } }$ , $x _ { \mathrm { m } } ~ = ~ 2 ~ \mathrm { m }$ , and $R = x _ { \mathrm { m } } / \lambda = 4 \times 1 0 ^ { 6 }$ .

![](images/136741821b8753be724fdc96999617ecfbc1a66fc1a743be64d61f374c971c3f.jpg)  
Fig. 8.23 Field of the interferometer. The area $S$ and the angle $i _ { \mathrm { m } }$ define the beam etendue.´ $S$ is the area of the beam at the lens $L _ { 1 }$ shown in the previous figure

D D It can be shown (Problem 8.2) that the optimum sampling rate for the interferogram is an increment $\Delta x \ : = \ : 1 / 2 \sigma _ { \mathrm { m } }$ , where $\sigma _ { \mathrm { m } }$ is the maximum wave number Dcontained in the source spectrum. A finite number of samples of $\tilde { I } _ { 0 } ( x )$ is thus Qobtained, and a numerical Fourier transform can easily be carried out on them. Note, furthermore, that it is possible to control the sampling by using the interference pattern $\tilde { I } _ { 1 } ( x )$ given by a reference laser whose wave number is precisely known. The wavelength scale of the spectrum $I _ { 0 } ( \sigma _ { \mathrm { m } } )$ is then determined with the same precision, a considerable advantage over the grating spectrometer, which must be calibrated using reference spectra.7

Throughput. The aim here is to establish the maximal beam etendue, beyond which the resolution ´ would be degraded (determination of the $Q$ factor). Referring to Fig. 8.23, let

$$
\Omega _ { \mathrm { m a x } } = \pi i _ { \mathrm { m } } ^ { 2 } .
$$

Those rays inclined at an angle $i$ to the axis contribute

$$
\mathrm { d } \Omega = 2 \pi i \mathrm { d } i
$$

to the solid angle, and the associated variation in path difference is

$$
| \mathrm { d } x | = x ( 0 ) i \mathrm { d } i , \quad \mathrm { u s i n g } \quad x ( i ) = x ( 0 ) \left( 1 - \frac { i ^ { 2 } } { 2 } \right) ,
$$

so that

$$
\mathrm { d } \Omega = \frac { 2 \pi } { x ( 0 ) } \mathrm { d } x .
$$

The power delivered by a source of uniform brightness is thus

$$
\mathrm { d } \phi = S \frac { 2 \pi } { x ( 0 ) } \mathrm { d } x ( i ) \mathcal { C } [ x ( i ) ] ,
$$

where the factor $\mathcal { C }$ expresses the modulation due to the interference of the two waves. For a monochromatic source of unit brightness, the modulated part of the flux $\tilde { I } ( x ) - \langle \tilde { I } ( x ) \rangle$ can be written

$$
\phi [ x ( 0 ) ] = S \frac { 2 \pi } { x ( 0 ) } \int _ { 0 } ^ { \infty } { \cal D } [ x ( i ) ] \cos [ 2 \pi \sigma _ { 0 } x ( i ) ] \mathrm { d } x ( i ) ,
$$

where $D$ is a ‘diaphragm’ function, giving a first approximation to $\mathcal { C }$ :

$$
D = \left\{ { 1 , \quad x ( 0 ) \leq x ( i ) \leq \left( { 1 - \frac { i _ { \mathrm { m } } ^ { 2 } } { 2 } } \right) x ( 0 ) , } \right.
$$

It follows that

$$
\begin{array} { l } { { \phi [ x ( 0 ) ] = \displaystyle \frac { 2 \pi S } { x ( 0 ) } \frac { 1 } { 2 } \mathrm { F T } \big [ D [ x ( i ) ] \big ] } } \\ { { \qquad = \displaystyle \frac { \pi S } { x ( 0 ) } \mathrm { s i n c } \left[ \pi \sigma _ { 0 } x ( 0 ) \frac { i _ { \mathrm m } ^ { 2 } } { 2 } \right] \cos 2 \pi \sigma _ { 0 } \left( 1 - \frac { i _ { \mathrm m } ^ { 2 } } { 4 } \right) x ( 0 ) , } } \end{array}
$$

or simply

$$
\phi ( x ) = \frac { \pi S } { x } \operatorname { s i n c } \left( \pi \sigma _ { 0 } x \frac { i _ { \mathrm { m } } ^ { 2 } } { 2 } \right) \cos 2 \pi \sigma _ { 0 } x .
$$

The modulation term cos $2 \pi \sigma _ { 0 } x$ is therefore subject to a damping effect which tends to remove the modulation, either for large path differences at given $i _ { \mathrm { m } }$ , or for large fields $i _ { \mathrm { m } }$ at given $x _ { \mathrm { m } }$ .

The modulation is zero for

$$
\pi \sigma _ { 0 } x \frac { i _ { \mathrm { m } } ^ { 2 } } { 2 } = k \pi , \mathrm { i . e . , } x = k \frac { 2 \pi \lambda _ { 0 } } { \Omega } .
$$

The resolution is $R = x _ { \mathrm { m } } / \lambda$ , so the beam etendue is´

$$
U = S \Omega = 2 \pi \frac { S } { R } , \mathrm { i . e . , } Q = 2 \pi .
$$

This result reveals the throughput advantage of the Fourier transform spectrometer: at a resolution equal to that of a grating spectrometer, the throughput is increased by the factor

$$
\frac { 2 \pi } { \beta } \sim 1 0 ^ { 2 } \mathrm { t o } 1 0 ^ { 3 } .
$$

This greatly facilitates the observation of extended sources (that is, sources whose angular dimensions were incompatible with the slit width of the grating spectrometer). Note that this advantage is clearly related to the axisymmetry of this interference arrangement, possessed also by the Fabry–Perot spectrometer. ´

The Holographic Fourier Spectrometer. The moveable mirror is one of the less convenient aspects of the above setup. It has been suggested that one (or both) of the mirrors could be replaced by a grating, tilted in such a way that it acts as a plane mirror for some wavelength $\lambda _ { 0 }$ (Littrow reflection of the grating). Neighbouring wavelengths $\lambda$ are reflected at different angles, and each one of them produces straight-line interference fringes, like the ones produced by an air wedge, on the two-dimensional detector. The amplitude is proportional to the intensity $I ( \lambda )$ and Fourier analysis of the signal restores $I ( \lambda )$ . The name comes from the fact that the frequency $\nu _ { 0 }$ is reduced to zero (uniform flux at the detector) and so produces a holographic effect. (Douglas N. et al., Astroph. Sp. Sci. 171, 307, 1980.)

# The Multiplex Advantage

A simple argument readily establishes the principle here, due to Felgett. Suppose we wish to determine, over a total measurement time $T$ , the spectrum $I _ { 0 } ( \sigma )$ of a source, in the interval $( \sigma _ { 1 } , \sigma _ { 2 } )$ , and with resolution $R$ . The number of spectral elements is $M$ . Suppose that the intensity is comparable in each spectral element (absorption or continuum spectrum, the argument requiring modification in the case of a spectrum comprising a small number of emission lines). Suppose, finally, that the measurement is made by a detector whose intrinsic noise $\sigma _ { \mathrm { D } }$ dominates the other sources. For sequential scanning of the spectrum, the signal-to-noise ratio for each spectral element is

$$
r _ { 1 } = { \frac { I _ { 0 } ( \sigma ) \left( T / M \right) } { \sigma _ { \mathrm { D } } \sqrt { T / M } } } .
$$

For FT spectroscopy, the whole time $T$ is used for each spectral element, and the corresponding ratio is

$$
r _ { 2 } = \frac { 1 } { 2 } \frac { I _ { 0 } ( \sigma ) T } { \sigma _ { \mathrm { D } } \sqrt { T } } ,
$$

the factor $1 / 2$ coming from the light lost at the beam splitter. The multiplex gain is thus $\sqrt { M } / 2$ , and can be very large for extended spectra at very high resolution (Fig. 8.24). Historically, this gain made the FT spectrometer the optimal instrument for infrared observation, in which detector noise dominates, and for which, until the 1990s, no multichannel detectors were available to avoid sequential scanning.

Even though this advantage is now disappearing, with the progress made in detector technology, FT spectroscopy maintains its lead in throughput, in very high resolution (of the order of $1 0 ^ { 5 }$ ), and in rigorous wavelength calibration.

It is worth pointing out that the spectroscopic capacities of the FT spectrometer can be combined with imaging, by placing an array of detectors in the focal plane. The difficulties of data handling, whether related to the storage of measurement data or the calculation of spectra (Problem 8.3), are daunting.

# Astronomical Applications

The FT spectrometer was widely used in the near infrared over the period 1960– 2000, but progress in the sensitivity of 2D detectors has gradually eliminated it from ground-based observation. However, it is still used in space because of its high level of accuracy, compactness, and multiplex facilities.

![](images/7a50c3f7ee3f694317d1528a2bcc0336103b2df7c1529bbb7c4f77a620814715.jpg)  
Fig. 8.24 Progress in resolving the infrared spectrum of Venus, during the historical emergence of Fourier spectroscopy. (a) Grating spectrometer in the atmospheric window around $1 . 6 ~ { \mu \mathrm { m } }$ . Four intense rotational–vibrational bands of the $\mathrm { C O } _ { 2 }$ molecule are visible. (b) Fourier transform spectroscopy with $\Delta \sigma = 0 . 7 \mathrm { c m } ^ { - 1 }$ . (c) The same, with $\Delta \sigma = 0 . 0 8 ~ \mathrm { c m } ^ { - 1 }$ . The $\mathrm { C O } _ { 2 }$ bands are D Dresolved. The apertures of the telescopes used are given. From Connes P., ARAA 8, 209, 1970. Reproduced with the kind permission of the Annual Review of Astronomy and Astrophysics, Vol. 8, $\textcircled { \scriptsize { \mathrm { c } } } 1 9 7 0$ , Annual Reviews Inc

# Ground-Based Applications

In the infrared region observable from the ground, a background of thermal or OH emission is the predominant noise for $\lambda ~ \gtrsim ~ 1 . 5 ~ { \mu \mathrm { m } }$ , thanks to progress in detector technology. The multiplex advantage then disappears (Problem 8.4), but the throughput advantage remains, when the observed infrared sources are extended ${ \gg } 1$ arcsec). Moreover, as the wavelength is long, the need for mechanical precision is less restrictive, and the FTS is relatively easy to build. For this reason, they now equip several large telescopes (Fig. 8.25). When coupled to an array, it then operates as an integral field spectrometer (the BEAR instrument of the CFH telescope in Hawaii, Fig. 8.26).

![](images/7aa2145ef67c0ed0bd5014852cf592244cf424395b885be4e73a1a7f654a77ae.jpg)  
Fig. 8.25 Fourier transform spectrometer, Canada–France–Hawaii Telescope. The instrument is symmetrical, with signals, $I _ { 1 } ( x )$ and $I _ { 2 } ( x )$ , received at the two infrared detectors. The quantity $( I _ { 1 } - I _ { 2 } ) / ( I _ { 1 } + I _ { 2 } )$ is independent of atmospheric fluctuations. The beam from the visible He–  CNe laser provides reference fringes which control the sampling of the infrared signal. Upper and lower beams are spatially separated. The whole setup is mounted at the Cassegrain focus of the telescope. (After Maillard J.P., Michel G., I.A.U. Colloquium, 67, Reidel, Dordrecht, 1982. With the kind permission of D. Reidel Publishing Company)

# Spaceborne Applications

A nice example here is the ESA’s Herschel mission,8 observing the sky in the far infrared and submillimetre regions from Lagrange point L2 using a cooled $3 . 5 \mathrm { ~ m ~ }$ telescope from 2008. The Spectral and Photometric Imaging Receiver (SPIRE) is a Fourier transform integral field spectrometer (2:6 ), operating simultaneously in the two bands $2 0 0 { - } 3 0 0 ~ { \mu \mathrm { m } }$ and $3 0 0 { - } 6 7 0 ~ { \mu \mathrm { m } }$ , with spectral resolution as high as 1 000.

![](images/4c183e5f2581511a559c96409928cf9e77b649f22396c416af91d673fbb1c73b.jpg)  
Fig. 8.26 Integral field spectroscopy. High spatial and spectral resolution image of helium streamers, obtained with the Fourier spectrometer BEAR on the CFHT (Hawaii) in the HI Brackett $\gamma$ line at $\lambda = 2 . 0 5 8 ~ \mu \mathrm { m }$ , from the minispiral located in the immediate vicinity of the galactic Dcentre. Stellar contributions have been subtracted. The position of $\mathrm { S g r A } ^ { * }$ is marked by $^ +$ . The color coding of velocity is explicit in the insert, where it clearly appears that the spectral line in this particular pixel shows several radial velocities, proving the presence of several clouds with different velocities along the line of sight. Paumard, T. et al., 2001, courtesy of Astronomy & Astrophysics

# 8.3.5 The Fabry–Perot Spectrometer

This spectrometer (or interferometer) combines the throughput advantage of the FT spectrometer $Q = 2 \pi$ ) with a very high spectral resolution, whilst at the same time Dbeing far less bulky than the two previous instruments for the same resolution.9

![](images/58eaca5423d19d4d9c8610fba52dd32817a41dae4dab7fe366ddd47779fe5f7f.jpg)  
Fig. 8.27 Arrangement of the Fabry–Perot interferometer. (a) In the UV, visible, and near infrared, the plates are made of transparent material. (b) In the far infrared, the plates are self-supporting metallic grids

Principle

Two parallel plates, supposed non-absorbent, have a high reflection coefficient $r$ $( r ~ \lesssim ~ 1 )$ , and transmission $t = 1 - r$ (Fig. 8.27). This is called the Fabry–Perot D etalon (or FP etalon), and is so named because it allows a wavelength calibration by physical measurement of the distance between the plates, or conversely. Neglecting reflection by the faces $R _ { 0 }$ and $R _ { 0 } ^ { \prime }$ , the transmission of the FP etalon, illuminated by monochromatic radiation of wave number $\sigma$ at incidence angle $i$ , results from multiple wave interference and can be expressed by Airy’s formula

$$
I = I _ { 0 } \left( \frac { r } { 1 - r } \right) ^ { 2 } \left[ 1 + \frac { 4 r } { ( 1 - r ) ^ { 2 } } \sin ^ { 2 } ( 2 \pi e \sigma \cos i ) \right] ^ { - 1 } .
$$

At zero incidence, the FP etalon has transmission peaks when

$$
2 \pi e \sigma = m \pi , \quad m { \mathrm { ~ a n ~ i n t e g e r } } ,
$$

which means

$$
\sigma = { \frac { m } { 2 e } } , \quad m { \mathrm { ~ a n ~ i n t e g e r . } }
$$

These peaks are therefore more widely separated as the thickness $e$ is increased. The whole number $m$ is called the order of the interferometer, and $\Delta \sigma = 1 / 2 e$ is the free spectral interval.

At zero incidence, the full width at half maximum $\delta \sigma$ of a transmission peak is given by $I = I _ { 0 } / 2$ , which implies

$$
\sin \left[ 2 \pi e \left( \sigma + \frac { 8 \sigma } { 2 } \right) \right] \sim \pi e 8 \sigma = \frac { 1 - r } { 2 \sqrt { r } } .
$$

This width decreases as the reflection coefficient $r$ increases. Introducing the finesse of the FP by

$$
\mathcal { F } = \frac { \pi \sqrt { r } } { 1 - r } ,
$$

it follows that

$$
\delta \sigma = \frac { 1 } { 2 e \mathcal { F } } .
$$

The resolution is then given by

$$
R = \frac { \sigma } { 8 \sigma } = 2 e \mathcal { F } \sigma = m \mathcal { F } .
$$

This increases with both the finesse and the order.

As the FP has rotational symmetry about its axis, the interference pattern at infinity, when it is illuminated by monochromatic radiation of wave number $\sigma _ { 0 }$ , is a set of concentric rings. Let $\ S i$ be their angular size at half maximum. Then the ring maximum is given by

$$
\cos i = { \frac { m \pi } { 2 \pi e \sigma _ { 0 } } } ,
$$

and the width $\ S i$ is found by solving

$$
{ \frac { 4 r } { ( 1 - r ) ^ { 2 } } } \sin ^ { 2 } \left[ 2 \pi e \sigma _ { 0 } \cos \left( i + { \frac { 8 i } { 2 } } \right) \right] = 1 .
$$

A lens or mirror placed behind the FP forms an image of these rings in its focal plane. The maximum throughput for an FP without loss of resolution follows from an identical calculation to the one carried out above in the case of the FT spectrometer. Once again, if $S$ is the area of the etalon, the result is

$$
U = 2 \pi { \frac { S } { R } } .
$$

Use as a Spectrometer

The FP etalon can be used in different ways (Fig. 8.28). In any arrangement, it must be preceded by a predisperser (another etalon, interference filter, grating, or other), in order to isolate a single free spectral interval $\Delta \sigma$ on the FP.

In a scanning mode, and illuminated by arbitrary monochromatic radiation of spectrum $I _ { 0 } ( \sigma )$ , the FP is followed by a diaphragm isolating the central ring, which is received on the detector. The thickness $e$ is then varied, and the detector signal is proportional to the incident intensity $I _ { 0 } ( \sigma )$ . It is also possible to vary the pressure, and hence the refractive index, of a gas introduced between the plates.

# 8.3.6 The Bragg Crystal Spectrometer (X-Ray Region)

The first extragalactic spectral line observed in the X-ray region was the $2 p { - } 1 s$ line of iron XXIV, in the Virgo, Coma, and Perseus clusters of galaxies by NASA’s OSO-8 satellite. This observation (Fig. 8.29) used the low resolving power of the proportional counter, but demonstrated the potential of X-ray spectroscopy. Developments continued using crystals to produce diffraction, but in the 1980s, these were gradually replaced by conventional diffraction gratings with very close rulings (600 grooves/mm), first by transmission (the European EXOSAT mission), then by reflection (the European mission XMM–Newton, 1999), thereby covering the energy range $0 . 1 { - } 2 \ \mathrm { k e V } .$ In NASA’s Chandra X-ray observatory launched in 1999, the slitless high resolution spectrometer or High Energy Transmission Grating spectrometer $\mathrm { ( H E T G ) ^ { 1 0 } }$ uses a transmission grating formed by depositing gold microrods on a plastic substrate. Whether the disperser is a crystal or a grating, the X-ray spectrometer also includes a camera on which the dispersed image is formed (Sect. 7.4.6).

![](images/cab9f116309f0c4b208b8357b67a2cf1775a318ec0360df7c2d6eba6fa9a3295.jpg)  
Fig. 8.28 Interferograms of the galaxy NGC 2903, obtained using a scanning Fabry–Perot interferometer in the $\mathrm { H } \alpha$ line $( 6 5 6 . 3 ~ \mathrm { n m } )$ . The variation in order is obtained using piezoelectric wedges, and the free spectral interval is scanned in 24 steps (of which 12 are shown on the figure). Each photon is recorded on a $5 1 2 \times 5 1 2$ matrix by a photon counting camera. The number of photons measured is proportional to the intensity emitted at a given Doppler speed. The radial velocity of hydrogen in the galaxy is thus mapped. The integration time per step was $5 \ \mathrm { m i n }$ . (Observatoire de Marseille, $3 . 6 \mathrm { ~ m ~ C F H }$ telescope, Hawaii, Marcelin M. et al., Astron. Ap. 128, 140, 1983. With the kind permission of Astronomy and Astrophysics)

![](images/4bd07e40ee836c9744727bc38e8a821cc4335e6ab50478b1735c0e7736953265.jpg)  
Fig. 8.29 X-ray emission from the Virgo, Perseus and Coma clusters of galaxies. The spectral resolution, obtained by a proportional counter, is less than 10, but nevertheless sufficient to show an iron line at $7 \mathrm { k e V . }$ From Serlemitsos P.J. et al., Ap. J. 211, L63, 1977. With the kind permission of the Astrophysical Journal

![](images/98b6b8e43e8737564d2df974a104b5c6ac2f7929449f27a5d8b0b31b45ebb165.jpg)  
Fig. 8.30 Bragg diffraction. (a) Lattice plane of the crystal, with period $d$ . (b) Concave crystal forming the pseudo-images of a source at infinity

A high resolving power $R \sim 1 0 0 0 )$ can be obtained by means of a crystal, such as lithium fluoride LiF, which functions as a diffraction grating. Bragg diffraction occurs on a crystal of spacing $d$ (Fig. 8.30a), at an angle $\theta$ given by

$$
\sin \theta = { \frac { \lambda } { 2 a } } .
$$

Just as a Rowland mounting (Fig. 8.11) forms an image with a concave grating, a curved crystal produces a series of quasi-anastigmatic monochromatic images from a point source at infinity (Fig. 8.30b). If the crystal surface is part of a spherical surface of centre $C$ , the lattice planes being tangent to the sphere, dispersion is along the $z$ axis and the distance $C I$ to the image $I$ of radiation with wavelength $\lambda$ is given by

$$
C I = { \frac { r } { 2 \sin \theta } } .
$$

The resolution $R$ at which an energy interval $\mathrm { d } E$ can be separated is given by

$$
R = { \frac { E } { \mathrm { d } E } } = { \frac { \lambda } { \mathrm { d } \lambda } } = { \frac { r } { 2 \sin \theta \mathrm { d } z } } .
$$

The spacing of the LiF crystal is $2 . 0 1 \mathrm { ~ \AA ~ }$ , giving $\theta \ : = \ : 2 5 ^ { \circ }$ for an energy $E = 7 . 3 ~ \mathrm { k e V } .$ The resolution $R = 1 0 0 0$ corresponds to $\mathrm { d } z = 1$ Dmm for $r = 1 \textrm { m }$ D. A proportional counter is thus placed on the $z$ axis, to measure both the $z$ D Dcoordinate, and hence the energy, of the photon, as well as the corresponding intensity. The spatial resolution of the proportional counter may indeed limit the spectral resolution of the instrument. As the system is not perfectly anastigmatic for a point source at infinity, extended objects give a series of pseudo-images at different $z$ .

![](images/0b468e33f1a4b5a3a21ef0c261b92ecbbcb58e6b46a00dfbf16b3f8712b4d2e5.jpg)  
Fig. 8.31 Spectrum of the supernova remnant (SNR) Puppis A, observed with the curved grating spectrometer on the Einstein satellite. Lines due to various ions are identified. Note the profile of the rays, due to the limited resolution of the spectrometer. From Winkler P.F. et al., Ap. J. 246, L27, 1981. With the kind permission of the Astrophysical Journal

Note that such a spectrometer is sensitive to polarisation, since only the component of the electric field parallel to the crystal surface is reflected at the Bragg angle. Between 1978 and 1981, the Einstein satellite (High Energy Astronomical Observatory 2) was equipped with such a spectrometer, and provided a resolution of 50 to $1 0 0 ~ \mathrm { u p }$ to $0 . 4 \mathrm { \ k e V } ,$ , and 100 to 1 000 beyond (Fig. 8.31). Figure 8.32 shows a spectrum obtained 20 years later with the RGS instrument aboard the European XMM–Newton mission.

Finally, note that, as in other wavelength regions, a certain spectral selectivity can be introduced by the detector itself (Sect. 7.4.6), whence no further dispersive system is required.

# 8.4 Radiofrequency Spectrometry

Interference spectrometers use the spectral selectivity which results from interference of a wave with itself. Heterodyne spectrometers achieve this selectivity by interfering the incoming wave with a locally produced wave, and analysing the result in a set of electric filters, or by other methods outlined below. These methods cover the conventional radiofrequency region, from long wavelengths (centimetre to hectometre) down to the shortest, in the millimetre and submillimetre region which we first began to seriously explore at the beginning of the 2000s.

![](images/cbf9cb9027803efb9220c63ceab2dea37071886f00d68d32d786851d4a53687f.jpg)  
Fig. 8.32 Spectrum obtained with the reflection grating spectrometer (RGS) of the Newton mission. Spectrum of the young, active star AB Doradus between 2 and $0 . 3 \mathrm { k e V } .$ There are many ionised iron, magnesium, and neon lines. Image courtesy of J. Sanz-Forcada ESA XMM–Newton mission

The idea of heterodyne detection, from radiofrequencies to mid-infrared, was discussed in detail in Sect. 7.5. It involves a local oscillator (LO) with frequency very close to that of the incident radiation. The frequency change by heterodyning transfers the information carried by the incident wave to a lower frequency region called the intermediate frequency (IF), and this is where spectral analysis and final detection can be carried out. The detector remains limited to a coherence etendue´ $\lambda ^ { 2 }$ and one polarisation direction, but detectors can be juxtaposed to form small arrays $3 \times 3$ or $4 \times 4$ ), thereby speeding up image reception efficiency. Single wavelength  maps are produced either in the spatial frequency plane $w$ or in the image plane $\pmb \theta$ by combining spectral discrimination, the image formation properties discussed in Chaps. 5 and 6, and detector properties discussed in Chap. 7.

# 8.4.1 Spectral Discrimination Methods

Spectral discrimination on the intermediate frequency (IF) signal can be achieved in several ways, which we shall discuss in detail here:

• Using electrical filters connected in parallel and identifying each spectral band. • Using acousto-optical techniques forming a diffraction grating. By purely digital processing of the signal, either by digital correlator or by fast Fourier transform.

![](images/622182e801b470da66804921e98adf2921cdbbf8bf46ab3604cbb8aa4749907d.jpg)  
Fig. 8.33 Typical lines in the radio region 4.5 to $5 \ \mathrm { G H z }$ . (a) Molecular lines of formaldehyde $\mathrm { H } _ { 2 } \mathrm { C O }$ , and formamide $\mathrm { H } _ { 2 } \mathrm { C O N H }$ , and fine structure lines of the OH radical. (b) Recombination lines of hydrogen and helium, $\alpha$ and $\beta$ transition series. Values of the quantum number $n$ are given. A list of transitions and their frequencies is given in AQ, Sects. 2.12, 2.14

Any method will do, whatever the spectral region from submillimetre to metre wavelengths, since they all apply to the IF signal, and not directly to the incident signal. Only the mixing stage can differ here.

Considering the regions from $\lambda = 1 0 0 \mu \mathrm { m }$ $\langle \nu = 3 \mathrm { T H z } \rangle$ to $\lambda = 1 0 \mathrm { c m }$ $( \nu = 3 \mathrm { G H z }$ ), one seeks D D D Dpassbands for the IF stage able to exceed 1 GHz. What is the desired resolution? When a gas has thermal agitation speeds of the order of several $\mathrm { k m ~ s ^ { - 1 } }$ , an emission or absorption line (Fig. 8.33) will have relative width $\Delta \nu / \nu \sim 1 0 ^ { - 5 }$ , implying $\Delta \nu = 1 4 ~ \mathrm { k H z }$ at $\lambda = 2 1 ~ \mathrm { c m }$ , or $1 . 5 ~ \mathrm { M H z }$ at $\lambda = 2 0 0 ~ \mu \mathrm { m }$  D D. There is little point in pushing the spectral resolution to values much above $1 0 ^ { 5 } -$ $1 0 ^ { 6 }$ D, since for one thing the spectral lines are broader, and for another, a very high level of stability would have to be guaranteed for the local oscillator.

![](images/3357a00e6fe6459b47f7a519337e598f2572dd129e6cce1ab1787117ea328456.jpg)  
Fig. 8.34 Set of filters in parallel, and the resulting transfer function. The intermediate frequency signal from the mixer is amplified, then distributed through a series of electrical filters arranged in parallel, each one discriminating a spectral band $B$ and thereby fixing the spectral resolution

# Multichannel Filter Spectrometers

In the second half of the twentieth century, radioastronomy developed on the basis of this method of spectral discrimination, which is now tending to disappear (2007).

Consider the signal at intermediate frequency (IF) leaving the mixer (Fig. 8.34). A set of filters, with transfer functions $H _ { i } ( \nu )$ and passband $B$ , slice the frequency band $\Delta \nu$ into $\begin{array} { r } {  { \boldsymbol { N } } } { \ = \ \Delta  { \boldsymbol \nu } / B }  \end{array}$ channels, over which the IF signal is distributed Din parallel. Each filter is followed by a quadratic detector, then a commutator, which compares the signal with a reference signal (local calibration source, see Sect. 3.4). A linear integrator (e.g., low-pass filter, digital running mean) of equivalent passband $B _ { 0 }$ reduces the variance of the fluctuations, and the resulting noise temperature is given by

$$
T = T _ { \mathrm { s y s t e m } } \left( \frac { B _ { 0 } } { B } \right) ^ { 1 / 2 } ,
$$

where $T _ { \mathrm { s y s t e m } }$ is the system noise temperature defined for $B \ : = \ : B _ { 0 }$ . Note that half Dof the total measurement time is used for calibration, which therefore doubles the noise power. Each of the above operations is carried out digitally.

![](images/6a4c74ab9b8bf50c5cc768f58719589a1dfd94f5318df6e3157e20a2af6194f5.jpg)  
Fig. 8.35 Spectrum of the galactic object W49 OH (a very intense $\textrm { H I I }$ region). Spectral element $B = 2 \mathrm { k H z }$ . Number of channels $N = 1 0 0$ . Central Dfrequencies $\nu _ { 0 } = 1 6 6 5$ and $1 6 6 7 \mathrm { M H z }$ D, respectively (radical OH lines). Note the complex radial velocity structure of the various components of the object

In brief, the source spectrum is found in the frequency interval $\Delta \nu$ around the frequency $\nu _ { 0 }$ , with resolution $R \ = \ \nu _ { 0 } / B$ , averaged over a time interval of about $1 / B _ { 0 }$ .

Multichannel spectrometers (Fig. 8.35) can include up to 512 channels operating in parallel, and the width $B$ of each channel can be made almost arbitrarily narrow, but rarely less than $1 \mathrm { k H z }$ in practice.

# The Acoustic Spectrometer

This second method appeals to a different idea. The intermediate frequency signal excites vibrations in a piezoelectric crystal, which in turn generates an ultrasonic sound wave in a lithium niobate crystal $\left( \mathrm { L i N b } \mathrm { O } _ { 3 } \right)$ ). Other materials (tellurium dioxide or gallium phosphide) can be used to vary the useful band between 0.2 and 2 GHz. Promising tests (2007) aim to replace acoustic excitation of the crystal by laser excitation, keeping the crystal at low temperature $( \sim 4 \mathrm { K } )$ in order to extend the lifetime of metastable states created by the laser radiation. The band could then reach $2 0 \mathrm { G H z }$ .

The fluctuations of the refractive index at successive wavefronts are used to diffract the beam of an optical laser (for example, He–Ne, or a solid-state laser diode). The diffracted energy is distributed across a multichannel linear detector (a 1024 or 2048 pixel CCD array), in which each pixel has a size corresponding to the frequency spread $B$ , or less, if over-sampling is required. The frequency resolution is limited by diffraction and attenuation in the acoustic medium. If the IF signal is monochromatic, all the diffracted energy is concentrated on a single pixel (Bragg reflection), and the spectrum produced by the sequential readout of the diodes is indeed non-zero only on a single element. In the case of a more complicated spectrum, the energy distribution on the diodes is simply proportional to the IF spectrum (Fig. 8.36).

This instrument is particularly compact and low in power consumption (a few watts), factors which make it ideal for use on board a satellite. For example, the European Herschel mission (launch 2008) carries an acousto-optical spectrometer, the Wide Band Spectrometer (HIFI) with four juxtaposed units of $B = 1$ GHz each, to observe in the range 0.5–1.9 THz.

![](images/8fd77724cad649d51d32a673630c2c6b399d26d2291f1df272a2013bea1d36a0.jpg)  
Fig. 8.36 Principle of the acoustic spectrometer. The inset shows the intensity received by each of the diodes, namely, the spectral density (spectrum) of the IF signal applied to the piezoelectric crystal. For the purposes of clarity, the angle between the incident direction (laser) and the diffracted direction has been grossly exaggerated. In reality, it would not be more than a few degrees. Note that the lens forms the Fourier transform of the diffracted field on the detector (see Sect. 6.1)

Other spectrometers with similar inspiration may come to light in the future, e.g., using surface waves produced on a solid by interference between two lasers, and used to diffract the radiofrequency signal.

# The Autocorrelation Spectrometer

This has become the main method used in radioastronomy observatories, thanks to progress in speed and capacity of digital processing, and the correlator has become a standard tool for radiofrequency spectrometry.

The autocorrelation spectrometer makes use of the integral transformation property relating the Fourier transform of the spectral density to the autocorrelation function (see Appendix A). If $I ( \nu )$ is the spectrum (in fact, a spectral density, as already pointed out) of the time-dependent IF signal $x ( t )$ , then $I ( \nu )$ is also the Fourier transform of the autocorrelation $R ( \tau )$ of $x ( t )$ :

$$
R ( \tau ) = \langle x ( t ) x ( t + \tau ) \rangle .
$$

At the expense of a slight loss of efficiency, when $x ( t )$ is digitised on a small number of bits, the digitisation of $x ( t )$ followed by an autocorrelation calculation can give

![](images/1baec97f1e448f1207acd262cf51d67bec6012e85c5cc5282e4e732ab20ad5e5.jpg)  
Fig. 8.37 Spectrum of a cold molecular cloud, obtained using the VESPA instrument on the IRAM $3 0 ~ \mathrm { m }$ radiotelescope (Spain) at $8 8 ~ \mathrm { G H z }$ $\lambda = 3 . 4 \ : \mathrm { m m }$ ). Ordinate: Antenna temperature. Abcissa: DFrequency converted to radial velocity. Resolution $B = 3 0 ~ \mathrm { M H z }$ , and $3 . 3 \ \mathrm { k H z }$ (corresponding to a gas velocity width of $1 1 ~ \mathrm { m } \mathrm { s } ^ { - 1 }$ D) in the inserts, showing the hyperfine structure of the line. Document courtesy of G. Paubert and C. Thum

$R ( \tau )$ in real time, and hence also $I ( \nu )$ . Most correlators work on two bits (1 and 0) with efficiency reduced to 0.6, but sometimes on three (1,0, 1), and up to eight bits, whereupon the efficiency reaches 0.85. A correlator can cover up to $2 5 0 \mathrm { M H z }$ , and several correlators can work in parallel to cover a broader range. The spectral resolution $B = 1 / \tau _ { \mathrm { m a x } }$ is determined by the width of the support of $R$ , hence by the Damplitude of the maximum chosen shift $\tau$ .

Note that the technique can be generalised to the cross-correlation of two signals $x _ { 1 } ( t )$ and $x _ { 2 } ( t )$ , viz.,

$$
R _ { 1 2 } ( \tau ) = \langle x _ { 1 } ( t ) x _ { 2 } ( t + \tau ) \rangle ,
$$

and this makes it possible to study two perpendicular polarisations, hence giving direct access to the Stokes parameters.

An example is the Versatile Spectrometer Assembly (VESPA) correlator,11 set up on the IRAM $3 0 ~ \mathrm { m }$ millimetre wave radiotelescope in Spain in 2002. It covers an IF band of $4 8 0 ~ \mathrm { M H z }$ , which can be sliced into spectral elements of width $B = 4 0 ~ \mathrm { k H z }$ , while specific modes can increase the spectral resolution up to a maximum of $1 0 ~ \mathrm { k H z }$ , i.e., a velocity resolution of $1 0 \ \mathrm { m s ^ { - 1 } }$ at $\nu = 1 0 0 \mathrm { M H z }$ , as shown in Fig. 8.37. Spectra are often represented as a function of the LSR radial Dvelocity (Sect. 8.1).

Fast Fourier Transform (FFT)

The spectrum of the intermediate frequency (IF) signal can now be calculated directly almost in real time, thanks to the increasing speed of computer calculation. This spectrum is just the source spectrum but translated in frequency by the heterodyne setup. The $1 2 \textrm { m }$ millimetre wave radiotelescope Atacama Pathfinder EXperiment (APEX), set up at the future site of the ALMA millimetre array in Chile (Sect. 6.4), has a processing mode12 with 16 384 spectral channels in a total band of 1 GHz: the resolved bandwidth is thus $B = 6 1 \mathrm { k H z }$ . The $1 0 0 \times 1 1 0 \mathrm { m }$ metre D and centimetre wave radiotelescope at Greenbank (USA) is also equipped with this kind of processing system. The efficiency is excellent in principle since the digitised signal can be treated directly.

# 8.4.2 Submillimetre Spectroscopy

The submillimetre region $5 0 ~ { \mu \mathrm { m } }$ to $1 \ \mathrm { m m }$ ), still largely unexplored at the time of writing (2007), lies between the more conventional optical regions (mid-infrared) and the radiofrequencies. Both for radiation detection and spectroscopy, it usually borrows its observational methods from one or other of these regions. Very rich in spectral lines, particularly of molecular origin, in the interstellar medium, it also contains some quite fundamental lines, such as the neutral carbon C I fine structure line at $4 9 2 \mathrm { G H z }$ and also the fine structure line of $\mathrm { ~ O ~ I ~ }$ at $6 3 ~ { \mu \mathrm { m } }$ .

Observation in this region thus uses optical filters and grating spectrometers with moderate resolution $\left( < 1 0 0 0 \right)$ , as in the PACS instrument of the European Herschel mission (2008–2012) or in the IRS instrument (IRS) of the Spitzer mission (2003– 2008), operating up to wavelengths close to $2 0 0 \mu \mathrm { m }$ . However, the Herschel mission also carries a very high resolution heterodyne spectrometer, the HIFI instrument, covering the range 280–1 910 GHz $( 1 5 7 - 1 0 7 0 ~ \mu \mathrm { m } )$ . It works on the principle, typical to radiofrequency observation, of a local oscillator and mixers with a superconductor–insulator–superconductor (SIS) junction or hot electron bolometers (see Sect. 7.3). Likewise, the airborne telescope SOFIA13 is equipped with a heterodyne spectrometer covering the range $2 5 0 { - } 6 0 0 ~ { \mu \mathrm { m } }$ to study the interstellar medium.14

Consider again the arrangement of a heterodyne instrument (Fig. 8.38), with a laser as local source and using a quantum quadratic detector of efficiency $\eta$ to mix. The IF exit signal has frequency $\nu _ { \mathrm { s } } - \nu _ { \mathrm { 0 } }$ and the exit current at the detector is

![](images/856371e80242f8bdbca917ba7f6b9b38081d09b9f6598f536e2145a906c3294d.jpg)  
Fig. 8.38 Heterodyne spectrometer, with a laser as local oscillator

$$
i ( t ) \propto \eta \left[ \frac { E _ { 0 } ^ { 2 } } { 2 } + E _ { \mathrm { s } } E _ { 0 } \cos 2 \pi ( \nu _ { \mathrm { s } } - \nu _ { 0 } ) t \right] ,
$$

neglecting the term in $E _ { \mathrm { s } } ^ { 2 } ( E _ { \mathrm { s } } \ll E _ { 0 } )$ , and also the sum frequency term, which is too high for the frequency response of the detector. After filtering (bandwidth $B$ ) and linear integration (equivalent bandwidth $B _ { 0 }$ ), the signal-to-noise ratio is, in power,

$$
\eta \frac { P _ { \mathrm { s } } } { h \nu ( B B _ { 0 } ) ^ { 1 / 2 } } .
$$

Note that, if $B \ = \ B _ { 0 }$ , the expression $\eta P _ { \mathrm { s } } / h \nu B$ is recovered, which means that Dthe minimal detectable power $P$ (signal-to-noise ratio $\mathit { \Theta } = \mathit { \Theta } 1$ ) corresponds to one photoelectron per hertz of the passband (see Sect. 7.2.2).

In the special case when the source is a blackbody of temperature $T$ , and thus of intensity

$$
\frac { 2 h \nu ^ { 3 } } { c ^ { 2 } } \left( \mathrm { e } ^ { h \nu / k T } - 1 \right) ^ { - 1 } \qquad [ \mathrm { W } \mathrm { m } ^ { - 2 } \mathrm { s r } ^ { - 1 } \mathrm { H z } ^ { - 1 } ] ,
$$

the beam etendue is´ $\lambda ^ { 2 }$ , because coherence of the incident field is required in this method of measurement. The ideal signal-to-noise ratio is then deduced to be

$$
2 \eta \left( \mathrm { e } ^ { h \nu / k T } - 1 \right) ^ { - 1 } \left( \frac { B } { B _ { 0 } } \right) ^ { 1 / 2 } .
$$

The resolution of such a spectrometer is only limited by the frequency stability of the local oscillator and by the passband $B$ of the filter.

Extension to Mid-Infrared. The boundary between the submillimetre and infrared regions is fuzzy as far as observational techniques are concerned, as already emphasised. As an example, consider an infrared heterodyne spectrometer made in 1983 (Fig. 8.39). The local oscillator is a

Brightness temperature [K]

![](images/4daa12dbb018f28c92eda2b914c9cfa24f74f08c51e4f47def8c4bfa4431d1cf.jpg)  
Fig. 8.39 Heterodyne spectrometry in the mid-infrared $( 1 0 . 6 ~ \mu \mathrm { m } )$ . Measurement of an ethane $\mathrm { ( C _ { 2 } H _ { 6 } ) }$ line emitted by the atmosphere of Jupiter. Beam etendue ´ $\lambda ^ { 2 }$ , i.e., a field of $2 ^ { \prime \prime }$ for a $1 . 5 \mathrm { m }$ telescope. Rotational lines corresponding to levels $J = 1 6$ and 17 are fitted to a model (dashed Dline), which is corrected for line broadening due to rotation of the planet (continuous line). The estimated $\sigma$ is shown on the left. From Kostiuk T. et al., Ap. J. 265, 564, 1983. With the kind permission of the Astrophysical Journal

$^ { 1 4 } \mathrm { C } ^ { 1 6 } \mathrm { O } _ { 2 }$ laser, emitting at $8 2 9 . 9 3 \mathrm { c m } ^ { - 1 }$ , and the detector is a HgCdTe photoconductor mixer, with passband $\Delta \nu = 1 . 6 \mathrm { G H z }$ The intermediate bandwidth is $B _ { \mathrm { I F } } = 2 5 \mathrm { M H z }$ , and the resolution is $1 0 ^ { 6 }$ .

# 8.5 Resonance Spectrometers

A particularly elegant method of spectrometry is based upon the following principle. An atomic vapour is illuminated by the radiation under study. If this radiation contains photons whose frequency is equal to the characteristic frequency of some atomic transition in the vapour, then those photons will be absorbed. If a transition is chosen such that the lower level is a ground state, therefore highly populated, and the excited level a resonance, so that the probability of excitation is high, the number of absorbable photons can be maximised. This number is then measured by detecting the photons re-emitted in spontaneous de-excitation of the upper level, and the number of these is proportional to the number of incident photons (Fig. 8.40).

![](images/d8b03f59b57c36143f5e203dd92e2d01f23222a893e2a6901f83df040304db56.jpg)  
Fig. 8.40 Resonance spectrometer. The photons re-emitted by the vapour are measured at photomultiplier 1, while the signal proportional to the incident radiation is measured at photomultiplier 2. The ratio of the two is independent of atmospheric and instrumental fluctuations

A quite general tuning relation is

$$
\frac { V _ { \mathrm { s o u r c e / c e l l } } } { c } + \frac { V _ { \mathrm { s o u r c e } } } { c } = \frac { V _ { \mathrm { v a p o u r } } } { c } + \frac { e B } { 4 \pi m } ,
$$

which includes the thermal speeds of atoms in the source and in the vapour (both small relative to $c$ ), the motion of the source (e.g., the Sun) relative to the detecting cell (fixed to the Earth or a satellite in space), and also a Zeeman shift which may be imposed on the atoms of the vapour by a magnetic field $B$ . By varying $B$ , the profile of the excitation line can be scanned. A vapour at low temperature $T$ has $V _ { \mathrm { v a p o u r } } \ll V _ { \mathrm { s o u r c e } }$ , and the maximum resolving power of such a spectrometer is given by

$$
R \approx { \frac { c } { V _ { \mathrm { v a p o u r } } } } \approx c \left( { \frac { m } { 3 k T } } \right) ^ { 1 / 2 }
$$

where $m$ is the atomic mass of the vapour atoms. At $T = 5 0 0 \mathrm { K }$ , $R \approx 2 \times 1 0 ^ { 5 }$ for sodium vapour.

Although limited to certain favourable circumstances, this type of resonance spectrometer has been successfully used to measure the photospheric oscillations of the Sun and other stars (in the 1980s) when the velocities to be detected are of order cm $\mathrm { s } ^ { - 1 }$ , and also to study the velocity field of interstellar hydrogen.

# Problems

8.1. Resolution of a Fourier Transform Spectrometer. Consider an interferogram $I ( x )$ , taken over the optical path differences 0 to $x _ { \mathrm { m } }$ .

(a) Show that the observed interferogram is simply the product of the full interferogram ( $x$ varying from $- \infty$ to $+ \infty ,$ and a suitable box function. Deduce the 1 C1instrumental profile of the spectrometer.

(b) Show that, by multiplying the observed interferogram by a suitably chosen function, it is possible to modify the instrumental profile. For example, giving up some resolution in order to decrease the wings of the profile. Examine the use of the multiplying functions

$$
\cos \left( { \frac { \pi x } { 2 x _ { \mathrm { m } } } } \right)
$$

and the sawtooth function

$$
1 - { \frac { x } { x _ { \mathrm { m } } } } \quad { \mathrm { i f ~ } } x \leq x _ { \mathrm { m } } , \qquad { \mathrm { a n d } } \quad 0 \quad { \mathrm { i f ~ } } x > x _ { \mathrm { m } } .
$$

This weighting of the interferogram is called apodisation, because it suppresses the ‘feet’ of the instrumental response. It is also possible to apodise a pupil by the use of an appropriate amplitude or phase mask (see Sect. 6.6).

Answer. (a) The observed interferogram is truncated

$$
I ( x ) = I _ { \mathrm { { c } } } ( x ) I I ( x / x _ { \mathrm { { m } } } ) ,
$$

and in the frequency space,

$$
\tilde { I } ( \sigma ) = \tilde { I } _ { \mathrm { c } } ( \sigma ) \star \mathrm { s i n c } ( x _ { \mathrm { m } } \sigma ) .
$$

The instrumental profile is therefore sinc $( x _ { \mathrm { m } } \sigma )$ .

(b) Multiplying the interferogram by a cosine amounts to modifying the instrumental profile of the spectrometer by

$$
\mathrm { F T } \left[ P ( x / x _ { \mathrm { m } } ) \cos { \left( \frac { \pi x } { 2 x _ { \mathrm { m } } } \right) } \right] .
$$

The resulting profile is wider because the high frequencies are filtered, but the feet of the profile are cleaner (Fig. 8.41).

8.2. Sampling in Fourier Transform Spectroscopy. Let $\sigma _ { \mathbf { M } }$ be the highest wave number contained in the source spectrum. What step $\varDelta$ should be chosen for the moveable mirror so that the interferogram for this radiation is optimally sampled (in the sense of Shannon’s theorem)? (It is easily shown that the question amounts to finding the minimum sampling for a sinusoidal function.)

![](images/aff5fd5f46c33153ba0b195f811d5d07e7497f28fb1040cc8420bfff02cd0dc4.jpg)  
Fig. 8.41 Example of apodisation. Continuous line: Point source response of a circular pupil (Airy function). Dashed line: Point source response of a circular pupil after apodisation by a sawtooth function. Note the broadening of the central spike and the significant reduction of the wings

8.3. Imaging and Fourier Transform Spectroscopy. The multiplex capability of an FT spectrometer, combined with a digital detector with many pixels, can in principle be used to obtain a large number of monochromatic images of a source simultaneously, at adjacent frequencies. If the aim is to obtain such images over a $1 \times 1$ arcmin field, with an image quality limited by the atmosphere to 0.5 arcsec, and a resolution of $5 \times 1 0 ^ { 4 }$ , calculate the total number of bits of information accumulated in the interferograms, each data point being digitised on 16 bits.

Answer. The resolution requirement imposes on $x _ { \mathrm { m } }$ the condition: $R = \sigma x _ { \mathrm { m } }$ . The sampling of the interferogram requires $\Delta x = 1 / 2 \sigma$ D, whence the number of images $N = x _ { \mathrm { m } } / \Delta x$ D. Moreover, the information in an image is coded on

$$
( 2 \times 6 0 ) ^ { 2 } \times 1 6 = 2 . 3 \times 1 0 ^ { 5 } { \mathrm { b i t s } } .
$$

The digital dynamic range thus obtained with 16 bits is then $2 ^ { 1 6 } \ \sim \ 6 5 0 0 0$ , which corresponds to the usual dynamic range of CCD detectors. So this cube of information is coded on 23 Gbits.

8.4. An FT spectrograph is used in the photometric band $M$ (see Sect. 3.4), with a high-performance detector $\mathrm { ( N E P = 1 0 ^ { - 1 6 } W H z ^ { - 1 / 2 } } ,$ ). Calculate the thermal photon Dnoise due to atmospheric emission. Take its emissivity to be 0.05, and the beam size fixed by a $4 \mathrm { m }$ telescope with a 10 arcsec field of view at the detector. Show that the broadening of the spectral band allowed by the spectrograph (multiplex advantage) would not improve the signal-to-noise ratio.

# Part III Data Analysis

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