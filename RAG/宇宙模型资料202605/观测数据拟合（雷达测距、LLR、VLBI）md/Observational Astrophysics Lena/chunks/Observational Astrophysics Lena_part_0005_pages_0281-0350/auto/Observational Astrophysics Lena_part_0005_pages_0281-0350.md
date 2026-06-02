![](images/0132fb78730b2e1fb7317a86d15c9452a585bb367d03ac9ee2065f1ed5e95c2f.jpg)  
Fig. 6.31 Image processing using the CLEAN algorithm. The radiosource CygX-3, discovered in 1967 with the first rocket-borne X-ray observations of the sky, is a binary system including a Wolf–Rayet star and a compact variable object (microquasar). Observed with the VLA array at00 frequency $5 \mathrm { G H z }$ , rapid bipolar ejection from the microquasar became clearly visible for the first time (speed 0:5c). The CLEAN process is adapted here to the case of a rapidly varying object, with a final resolution of $0 . 3 { ^ { \prime \prime } }$ and a logarithmic intensity scale. (J. Marti et al., Astron. Astrophys. 375, 476, 2001. With the kind permision of NRAO-AUI)

to note that the idea of phase closure, under the name of structural invariance, was already used in X-ray crystallography back in the 1950s to determine the electron distribution in solids (pointed out by K. Kellermann & J. Moran).

Consider to begin with an array comprising three non-redundant sub-pupils, e.g., arranged at the corners of a triangle. With no atmosphere and a perfect instrument, the phase of the fringes given by each pair of sub-pupils is $2 \pi \lambda ( D _ { i j } { \bf \cdot s } )$ , where $\pmb { S }$ is the unit vector in the direction of the source. Since $\sum { \pmb { D } } _ { i j } = 0$ , the sum of the three Dphases is also equal to zero. If an atmospheric or instrumental perturbation should affect one of the sub-pupils, the sum remains zero, the perturbation adding to one baseline and subtracting from the other. If all the sub-pupils are affected, the result is the same, and the sum of the measured phases is equal to the sum of the true phases from the source. Clearly, the object must be bright enough to be able to measure the fringes (and hence their phase), with a high enough signal-to-noise ratio and over a lapse of time during which the perturbation remains stable, hence shorter than the coherence time $\tau _ { \mathrm { c } }$ of the atmosphere. This is called snapshot mode.

In the case of a non-redundant array of $N$ telescopes, a total of $N ( N - 1 ) / 2$ frequencies is measured, but only $( N - 1 ) ( N - 2 ) / 2$ independent phase closure  relations are obtained, which is thus not enough to reconstruct the $N$ unknown (because perturbed) phases of the object at the measured frequencies. However, if $N$ is large, the fraction of phase information actually recovered, viz., $( N - 2 ) / N$ , tends to $100 \%$ . Since the spectrum of the source $S$ is known in amplitude and almost completely known in phase, high quality images of $S$ can be reconstructed, without a priori assumptions about $S$ . If this process is combined with the CLEAN procedure, i.e., by including a priori information, the reconstructed image can be further improved. This combination is then referred to as a hybrid mapping. An extension of the method has become known as self-calibration.

All of these procedures have their limitations, residues of artifacts due to a poorly corrected PSF. At the time of writing (2006), a residual artifact less than $0 . 1 \%$ is achieved with large radio arrays (VLA, VLBA). The magnificent images of extragalactic objects produced by these arrays are thus obtained through a large collecting area and long exposures (access to faint objects), very long baselines allowing very high angular resolutions, and the high quality of the final PSF thanks to phase closure and numerical image restitution procedures. It is not yet possible in 2007 to boast equivalent performances for interferometry at optical wavelengths, but there is little doubt that progress will be fast given that the problems are very similar.

Pupil Masking. In 1874, Edouard Stephan in Marseille (France) built upon Fizeau’s ideas for reducing the effects of atmospheric perturbations by arranging two small apertures at variable distances apart on a diameter of the mirror of his telescope pointing toward a star. The apertures were only a few centimetres in diameter, hence smaller than the Fried parameter $r _ { 0 }$ . The apertures produced fringes agitated by a random translatory motion (phase noise). He estimated the visibility of the fringes and concluded the observed stars to have diameters smaller than the diffraction limit (0.16 arcsec) of the telescope he was using.

Now suppose there are, not two, but $N$ apertures, all smaller than $r _ { 0 }$ , on the surface of a large primary mirror (or an image of it, reformed downstream). At optical wavelengths, the image of a star is poorly visible, formed from $N$ systems of agitated fringes. This is a fortiori the image of a resolved object. However, if the apertures are non-redundant, Fourier analysis of the instantaneous image (snapshot) will perfectly separate each of the frequencies $w _ { i }$ of the image, and provide its amplitude and phase. The situation is strictly the same as what we have just described at radiofrequencies, and phase closure methods along with information restitution techniques like CLEAN and others can be applied in exactly the same way, to obtain from the source an image of resolution $\lambda / D _ { \mathrm { m i r r o r } }$ , limited only by diffraction (Fig. 6.32). In some cases, this approach can compete with adaptive optics, since the instrumental setup is very simple here (comprising only a mask), whereafter all processing is done numerically.

![](images/e7bababc6219ef617ad3e6b49a0018aaa530b5f2401dfd162cbe871842fca2ed.jpg)  
Fig. 6.32 Image of the LkH˛ 101 circumstellar envelope (accretion), obtained by pupil masking and phase closure on the $1 0 \mathrm { m }$ Keck telescope (Hawaii) at $\lambda = 2 . 2 \mu \mathrm { m }$ . DThe image has been processed using a certain amount of a priori information in order to reveal the central star Herbig Ae-Be (see Sect 9.6). With the kind permission of P. Tuthill. See Tuthill, P. et al., Ap. J. 577, 826, 2002

# 6.5 Astronomical Interferometers

In this section, we shall describe current and future realisations of interferometer arrays in various wavelength ranges, from radiofrequencies, through visible and infrared, to certain projects for X-ray observation. This kind of tool is developing fast, aiming for angular resolutions less than the mas ( $1 0 ^ { - 3 }$ arcsec), or even the $\mu { } \mathrm { a s }$ ( $1 0 ^ { - 6 }$ arcsec). The latter corresponds to a resolution of $1 \ 0 0 0$ AU at a distance of $1 \mathrm { G p c }$ , and requires a baseline of 2 million kilometers at $1 \mathrm { { c m } }$ , or $2 0 0 \mathrm { m }$ at $\lambda = 1 \mathrm { n m } !$ DWe shall also describe some of the observations made using these techniques.

# 6.5.1 Radiotelescope Arrays

Although Stephan and Michelson made their pioneering experiments in the visible prior to 1921, the technique of astronomical interferometry only really developed with the advent of radioastronomy, in the 1950s. This is because the accuracies required of the instrumentation are obviously less stringent than at optical wavelengths, and above all it is easy to transfer the Hertzian antenna signals by cable whilst preserving phase information, so that they can subsequently be recombined. Finally, the frequency bandwidth used is relatively narrow $( \sim 1 0 ^ { 6 }$ to $1 0 ^ { 8 } ~ \mathrm { H z } )$ compared with optical bandwidths $( \sim 1 0 ^ { 1 4 } ~ \mathrm { H z } )$ . The temporal coherence length is therefore large, and this means that it is easier to obtain an interference signal from two coherent signals originating at widely separated antennas.

![](images/f8836191bd388ce61e5771b9e63440f3b8d6e31f46fd3b0fc10298b6b40699b0.jpg)  
Fig. 6.33 Radio interferometry. A pair of antennas with baseline $B$ point in the direction $\pmb \theta ( t )$ of the source. The angles $\psi ( t )$ and $\phi ( t )$ defining $\pmb \theta ( t )$ are functions of time due to the Earth’s rotation. The phase difference between the two antennas can easily be calculated. An additional phase difference $\Delta \phi$ can be introduced electrically (delay line $\tau _ { \mathrm { d } }$ ) and the signals mixed in a correlator which provides the fringe signal. The temporal coherence of the signals is sufficient (the pass band $\Delta \nu$ is small compared with the signal frequency), so there will be many fringes around the zero path length difference

Ground-based radio interferometers27 cover a broad spectrum, from decametre wave $\lambda = 3 0 \mathrm { m }$ corresponds to $1 0 \ \mathrm { M H z }$ ) to millimetre wave $1 ~ \mathrm { m m }$ corresponds to $3 0 0 ~ \mathrm { G H z }$ ). Even though the underlying principles of construction and use are largely the same, the breadth of the region justifies presenting these instruments in subfamilies. An important place is given to very long baseline interferometry (VLBI), which is the only one to appeal to observation from space.

# Obtaining the Interferometric Signal (Radiofrequencies)

A widely separated pair of telescopes (antennas), comprising the two sub-pupils 1 and 2 and forming a baseline of length $\pmb { B } _ { 1 2 }$ , or simply $\pmb { B }$ , are both pointing in the direction $\pmb \theta$ (Fig. 6.33). The electric fields received at their foci, which may be transported locally by a waveguide, first undergo a change of frequency (intermediate frequency or IF) at 1 and 2, whereupon these two IF signals are carried to a correlator which measures their coherence $\gamma _ { 1 2 } ( \tau )$ , or equivalently, the visibility of the fringes. In order to restore the temporal coherence between signals 1 and 2, a delay line can introduce a suitable phase shift $\delta \varphi \ = \ 2 \pi \nu \tau _ { \mathrm { d } }$ . The time delay $\tau$ Dis a function of the length and orientation of the baseline $\pmb { B }$ , and also the diurnal rotation of the Earth. The spatial frequency analysed is determined by the value of the baseline $\pmb { B }$ projected onto a plane normal to the incident wave vector. The sighting angle $\pmb \theta ( t )$ , with components $\psi ( t )$ and $\varphi ( t )$ (Fig. 6.33), induces a time shift which is given as a function of time by

$$
\tau = \tau _ { \mathrm { d } } + \frac { B } { \lambda c } \left[ \cos \varphi ( t ) \cos \psi ( t ) \right] .
$$

The spatial frequency analysed, with components $u$ and $\nu$ , is determined by the projected baseline, and given by

$$
| w | = ( u ^ { 2 } + \nu ^ { 2 } ) ^ { 1 / 2 } = \frac { B } { \lambda } \left[ \sin ^ { 2 } \varphi ( t ) + \sin ^ { 2 } \psi ( t ) \cos ^ { 2 } \varphi ( t ) \right] ^ { 1 / 2 } ~ .
$$

It lies in the direction of the baseline projected onto the plane of the wavefront, i.e., onto the sky. The Earth’s rotation thus gives, for a fixed value of $B$ , a partial sampling of the spatial frequency plane $( u , \nu )$ .

Measuring the phase of the fringes completely fixes the complex Fourier component. These phase measurements can lead to extremely precise results. Over a baseline $B = 1 \mathrm { k m }$ , at $\lambda = 1 \mathrm { c m }$ , a determination of the phase to within 10 degrees, D Dof a source known to be effectively pointlike will fix the angular position of that source in the coordinate system of the base (terrestrial coordinates) to an accuracy of

$$
\delta \theta = \frac { 1 0 } { 3 6 0 } \frac { \lambda } { B } = 0 . 0 6 \mathrm { a r c s e c } .
$$

Radioastronomical interferometry is thus a powerful tool in astrometry.

Note that such a phase measurement is never absolute and that a reference network of point sources across the sky (usually quasars, see Sect. 4.2) is therefore necessary in order to establish reference phases, as explained earlier.

# Aperture Synthesis

Heterodyne detection of radiofrequencies has one remarkable property that does not occur for visible and infrared interferometers. Suppose that, instead of a pair of sub-pupils, we have some number $N$ greater than 2, forming many baselines $\pmb { { B } } _ { i , j }$ between them. The IF signal of an arbitrary antenna $i$ can then be distributed over several correlators, to form all possible correlations $( i , j )$ , making a total of $N ( N - 1 ) / 2$ correlations. Thanks to the local oscillator, this division of the signal can be achieved without reducing the signal-to-noise ratio, as explained in Chap. 7 on detectors (see in particular Sect. 7.5).

![](images/1a4ad1ed4db54d20508bbfa2ea231a49a87b46f6be54e0efaeb0a9ab40f8bb4e.jpg)  
Fig. 6.34 Redundancy of a pupil. Left: A redundant pupil. Several pairs of elements sample the same spatial frequency $w _ { 1 }$ . Right: A non-redundant pupil. Only the pair $A B$ samples $w _ { 1 }$ , the other pairs each sampling different frequencies

In practice, a large number of antennas are used (an array), paired in such a way that, varying $\pmb { B }$ for each pair, coverage of the $w$ plane can be optimised. If each pair corresponds to a single value of $w$ without any overlapping, the pupil is said to be non-redundant, in contrast to the highly redundant pupil formed by a standard circular aperture (Fig. 6.34). A dedicated computer combines the signals from all the antennas, calculating all the possible correlation functions, after first introducing the dephasing $\tau _ { i , j } ( t )$ required to centre the correlations on a given instant, which amounts to referring all the measurements to a common wave plane. This is the operation known as aperture synthesis.

Since the spatial frequencies filtered by a pair of telescopes is determined by the projection of the baseline $\pmb { B }$ on the sky, the Earth’s rotation varies this quantity as time goes by, thereby increasing the number of spatial frequencies covered in the plane $( u , \nu )$ . This combination of aperature synthesis and the Earth’s rotation is sometimes called aperture supersynthesis.

The image $I ( \pmb \theta )$ of the source is then obtained by a numerical Fourier transformation of $\widetilde { I } ( w )$ . This operation requires sampling of the MTF of the array (see above), and also image processing, to be discussed later (see Sect. 9.6). The extraordinary progress in computer technology since 1980, combined with powerful processing algorithms based on information theory, have made it possible to produce excellent images even though the arrays do not sample the whole range of frequencies up to some cutoff value, in the way that a single circular pupil would.

# Arrays for Metre to Centimetre Observation

The Very Large Array (VLA)

After the arrays in Cambridge (UK) and Westerbork (Netherlands), which played an important role in the development of radio interferometry over the decades

![](images/5eefeabc5ea33ff2ec0b6df8c4ab958797c8c27d3719177418388343f33bc49f.jpg)  
Fig. 6.35 Aerial view of the antennas of the VLA (Very Large Array) aperture synthesis array. The antennas are arranged in the shape of a Y, with the northern branch on the right, the south-eastern branch on the left, and the south-western branch at the top. Each branch includes 24 possible antenna positions at which the 27 mobile antennas can be placed. (NRAO photograph, Associated Universities, with the kind permission of the National Science Foundation)

1960–1980 and remain active today, the VLA of the National Radio Astronomy Observatory (NRAO) in New Mexico (USA) has become the most powerful tool of its kind in the world today at centimetre wavelengths, since it went into operation in 1980. It comprises 27 mobile antennas (Fig. 6.35) with separations up to $3 0 \mathrm { k m }$ , and operates from $\lambda = 4 \mathrm { m }$ down to $\lambda \approx 7 ~ \mathrm { m m }$ , achieving a resolution of 20 mas D at this wavelength (Fig. 6.36). It provides more than 1 000 images $1 0 2 4 \times 4 0 9 6$ pixels) per day of observation and has 512 spectral channels. As commented by the radioastronomer Jim Moran at the Center for Astrophysics in Harvard in 2001:

Since its completion in 1980, the VLA has been used by over 2 000 scientists from hundreds of laboratories and universities around the world for more than 10 000 individual observing programs. It exceeds its design specifications by orders of magnitude in nearly all parameters and remains, today, by far the most powerful radiotelescope in the world, although much of the instrumentation dates from the 1970s.

The Giant Meter Radio Telescope (GMRT)

This instrument, which went into operation in 2001, is located near Pune in Maharashstra (India). The array comprises 30 fixed antennas, each of diameter $4 5 \mathrm { m }$ , of which 14 are within $1 \mathrm { k m } ^ { 2 }$ from the centre, surrounded by 16 others, arranged on the branches of a $\mathrm { Y }$ with baselines up to $2 5 \ \mathrm { k m }$ . With this flexible configuration, a total of $N ( N - 1 ) / 2 = 4 3 5$ different baselines are available, covering a wavelength region from $6 \mathrm { m }$ to $2 1 \mathrm { c m }$ , and reaching a maximal resolution of 2 arcsec.

This instrument was built by India alone and is today the best metre wave array in the world. Apart from its scientific production, it is being used to develop techniques for a future instrument which could be the subject of a very broad international collaboration for the 2020s, namely the Square Kilometric Array (SKA). This would operate in the centimetre and decimetre wave range and could have a collecting area as great as $1 \mathrm { k m } ^ { 2 }$ . An interesting idea is under investigation here. Instead of orienting each antenna of the array individually to point in the direction of the source, the direction $\pmb \theta$ of the maximum point source response of the array (peak of the PSF) is fixed by modifying the phase of the signal received by each antenna, which can thus be flat, horizontal, and fixed, giving what is called a phased array. This technique is highly conventional in the construction of certain radars, and spatial scanning is done without rotating the antenna mechanically, but rather by modulating the phase of the signal emitted or received by each of the elements making it up.

![](images/1abf9d377d414ab9ed4edd39c6d2499b55327ddc9cd5e609a529614f694926c3.jpg)  
Fig. 6.36 The galaxy $\textbf { M } 8 7$ and its jet, about $1 5 \mathrm { { M p c } }$ from the Sun, observed at radiofrequencies. Upper: VLA observations, left at $\lambda = 9 0 ~ \mathrm { c m }$ , right at $\lambda = 2 0 \mathrm { c m }$ . Lower: Observations by theˇ VLBA interferometric array at $\lambda = 7 \mathrm { m m }$ D. Scales are specified on each image. On the lower image, $r _ { \mathrm { s } }$ Dis the Schwarzschild radius of the central black hole, of mass $M = 3 \times 1 0 ^ { 9 } M _ { \odot }$ . Image by Junor, W., Biretta, J., Livio, M., courtesy of NRAO/AUI/NSF

![](images/f75987339eed838db0f41e7ee3a91768e2a1e11eea6a6f195a6921a774c4da4e.jpg)  
Fig. 6.37 A sequence of images of the Sun taken by the Nanc¸ay radioheliograph at $\lambda = 0 . 9 2 { \mathrm { m } }$ Dduring a solar flare. The emission is due to electron beams propagating in the magnetic structures of the corona at speeds of the order of $c / 3$ , and lasts only a few seconds. The white circle marks the edge of the visible disk of the Sun. Image kindly provided by L. Klein and published by Maia, D. et al., Solar Phys. 181, 121–132 (1998)

Another project known as the Low Frequency Array (LOFAR) is also under study at the time of writing (2007) to build an instrument comprising several thousand antennas distributed over more than $1 0 0 \mathrm { k m }$ of baseline. These would be simple and relatively inexpensive, because they would operate at a long wavelength $\lambda = 3 0 \mathrm { m }$ .

Solar Surveillance by Radio Interferometry

The radioheliograph at Nanc¸ay (France) is a metre wave instrument, consisting of two $1 0 \mathrm { m }$ antennas and sixteen $3 \mathrm { m }$ antennas, and operates at $1 6 9 \mathrm { M H z }$ $\langle \lambda = 1 . 7 \ : \mathrm { m }$ ). DThere are 32 possible combinations, giving baselines of lengths varying from 100 to $3 2 0 0 \mathrm { ~ m ~ }$ . The east–west resolution is good $( \sim 1 . 2 ^ { \prime } )$ near the solar equator, and mediocre in the direction of the poles. The solar longitude of an event (a prominence) on the Sun can thus be well determined. Because of the great sensitivity of the detectors, the rapid evolution of solar flares can be followed with a time constant of less than one second, and this allows for correlations to be made between radio emissions and X-ray or EUV emissions observed in the corona from space (Fig. 6.37).

# Millimetre Arrays

The first millimetre interferometers were those at Hat Creek (California), Owens Valley (California), and Nobeyama (Japan). They were followed later by another at the Plateau de Bure in France in the 1980s. Millimetre wave radio interferometry encounters specific difficulties due to atmospheric absorption by $_ { \mathrm { H } _ { 2 } \mathrm { O } }$ , which increases at these wavelengths, and the correlative effects of atmospheric turbulence which begin to make themselves felt. On the other hand, for the same length of baseline $\pmb { B }$ , the resolution increases considerably as compared with centimetre wave observation. The millimetre region is also very rich in astrophysical information, particularly with regard to molecular spectroscopy, not only in the galactic interstellar medium but also in very remote quasars and galaxies. The possible combination of very high angular resolution and high sensitivity inspired an ambitious project at the beginning of the 2000s, with worldwide participation (Europe, USA, and Japan), namely the Atacama Large Millimeter Array (ALMA). The first images should become available around 2010.

Table 6.4 The main millimetre and submillimetre arrays. $N$ number of antennas, $D$ diameter of antennas. Updated in 2007   

<table><tr><td>Organisation and partners</td><td>Year</td><td>Site</td><td>Telescopes N×D</td><td>Baseline [km]</td><td>2min [mm]</td></tr><tr><td>Japan</td><td>1993</td><td>Nobeyama</td><td>6×10m</td><td>≤0.6</td><td>1-3</td></tr><tr><td>CARMA</td><td>2005</td><td>BIMA+OVRO (California)</td><td>9× 6.1m</td><td>≤2</td><td>1.0</td></tr><tr><td>CalTech and others</td><td></td><td>Owens Valley</td><td>6 × 10.4 m</td><td></td><td></td></tr><tr><td>IRAM CNRS/MPG/Spain</td><td>1985</td><td>Plateau de Bure (France)</td><td>6×15m</td><td>≤1</td><td>1.0</td></tr><tr><td>ALMA</td><td>2011</td><td>Chajnantor 5 100 m (Chile)</td><td>50 ×12 m</td><td>14</td><td>0.35</td></tr><tr><td>Europe/USA Smithsonian,Acad. Sinica</td><td>2005</td><td>Mauna Kea 4080 m</td><td>8×6m</td><td>≤0.5</td><td>0.6</td></tr></table>

Table 6.4 shows the very fast development of millimetre interferometry, which now extends to higher frequencies by using very high altitude sites like Mauna Kea in Hawaii and Cerro Chajnantor in Chile, where atmospheric transmission allows observation down to $6 5 0 \mu \mathrm { m }$ $( 4 6 0 \mathrm { G H z } )$ .

The Plateau de Bure Interferometer

This instrument has 6 mobile $1 5 \mathrm { m }$ antennas on an east–west baseline $1 0 0 0 \mathrm { m }$ long (Fig. 6.38). The resolution obtained at $\lambda = 3 ~ \mathrm { m m }$ is of the order of 2 arcsec. The Dsite is chosen for its atmospheric properties (altitude and hygrometry). However, variations in the refractive index of the air due to the humidity lead to phase fluctuations in the wavefront. These fluctuations limit the operating wavelength to $3 \ \mathrm { m m }$ in the summer, while observation at shorter wavelengths $( \lambda ~ \gtrsim ~ 1 ~ \mathrm { m m } )$ is possible in the winter.

# The Combined Array for Research in Millimeter Astronomy (CARMA)

This array in California began observations in 2005. On a baseline of about a kilometre, it brings together two older arrays, BIMA and OVRO, set up by different

![](images/9ddbda88a699f6f8e347ab148c542f8c956d6dc7ab2cbc1388e4e4484c7fcf95.jpg)  
Fig. 6.38 The radio interferometer at the Plateau de Bure (France), operating at millimetre wavelengths

US institutions, whence the name Combined Array for Research in Millimeter Astronomy (CARMA). It includes 23 telescopes of different sizes, from 3.5 to $1 0 . 4 \mathrm { ~ m ~ }$ , now connected to form the highest performing millimetre interferometer in the world, at least until ALMA goes into operation. It illustrates the remarkable flexibility of interferometric combination now achieved at radiofrequencies.

The Atacama Large Millimeter Array (ALMA)

The Atacama Large Millimeter Array (ALMA) is a joint project involving Europe (ESO), the United States (National Science Foundation), and Japan, to build an interferometer covering the Chajnantor plateau, which is about $1 0 ~ \mathrm { k m }$ across and situated at an altitude of $5 1 0 0 \mathrm { ~ m ~ }$ and latitude $2 0 ^ { \circ } \mathrm { S }$ in the Atacama desert in the Chilean Andes. The array will include about 50 mobile antennas of diameter $1 2 \mathrm { m }$ , providing a total collecting area of $5 \ : 0 0 0 \ : \mathrm { m } ^ { 2 }$ and operating down to a wavelength of $3 5 0 ~ { \mu \mathrm { m } }$ $( 9 5 0 ~ \mathrm { G H z } )$ . The sensitivity and image quality of the array and the prevailing atmospheric stability at this altitude will allow a very wide-ranging scientific programme, from exoplanets in the Galaxy to the study of galaxies and quasars in the early Universe (see Fig. 6.39).

# Very Long Baseline Interferometry (VLBI)

To reach the resolutions required by the sizes of radiosources (mas) at radiofrequencies, the only solution is to extend the baseline $B$ to the dimensions of continents. But this means solving the problem of recording IF signals locally and correlating the phases of the incident fields on each aperture, since cable transfer of the signals is no longer feasible. This particular coupling technique is called very long baseline interferometry (VLBI) and has been evolving now since 1967. At the time of writing (2007), extraordinary levels of resolution and flexibility have become possible.

The IF signal is recorded locally with a clock reading (atomic clock or hydrogen maser), the two clocks having been synchronised beforehand. These recordings, originally made on magnetic tape, but today on disk (2006), are then conveyed to a common point some time after the observation and ‘replayed’ in such a way that they interfere in a correlator and produce the interferometric signal (Fig. 6.40). Soon it may be possible to digitise the signal directly and send it by Internet, at least for frequencies below a few GHz.

![](images/1a3a6fda42dd2e8ae538cf58bd574124a96c99008caa87aae6c73dd8e7683a86.jpg)  
Fig. 6.39 Artist’s view of the ALMA interferometric array under construction in 2008 at the Chanjnantor site in Chile, at an altitude of $5 1 0 0 \mathrm { ~ m ~ }$ . The array is represented here at maximal deployment. Insert: Prototype $1 5 \mathrm { m }$ antenna. Document courtesy of the ESO

![](images/eae652d627a1753c7e23048b35ff28bbf813b6ec4c3b2f1ec90a23071232f441.jpg)  
Fig. 6.40 Schematic view of a conventional VLBI arrangement. From Moran J.M., Methods of Experimental Physics, Vol. 12C

Many corrections must be made to ensure that the correlation function effectively measures the coherence of the field at the two points considered. These must deal with effects related to the Earth’s rotation, phase drifts of the clocks, frequency drifts of the local oscillators, and others. The stability of the clocks (better than $1 0 ^ { - 1 4 }$ ) is such that the ultimate limitation for long exposures on intercontinental baselines is imposed by random phase fluctuations due to the Earth’s atmosphere.

The primary clock (see Sect. 4.3) is either a broadcast time signal from the GPS (Global Positioning System) satellite network, accurate to within $0 . 1 ~ \mu \mathrm { s }$ after correction for propagation irregularities introduced by the ionosphere, or a caesium clock reading, with a drift of around $0 . 2 5 ~ { \mu \mathrm { s } }$ per month. The local oscillator is a hydrogen maser, whose phase is locked to the clock, and whose relative phase stability is about $1 0 ^ { - 1 4 }$ over a period of up to $1 0 ^ { 4 } :$ s.

The signal is converted to an intermediate frequency (IF) signal with bandwidth $\Delta \nu \sim 0 . 1 \mathrm { M H \Sigma }$ z, implying a timebase stability of the order of $1 / \Delta \nu \sim 1 0 ^ { - 5 } \mathrm { s }$ .

 VLBI measurements make use of the more or less random locations of the large radiotelescopes around the world. The $w$ plane is thus only partially covered, even though improved by the Earth’s rotation (Fig. 6.41). VLBI resolution at centimetre wavelengths has long held the absolute record $( \gtrsim 1 0 ^ { - 3 }$ arcsec) by comparison with other wavelengths, and it is only recently, since the 1990s, that aperture synthesis in the visible has begun to attain similar angular resolutions.

![](images/f1a26cdc30c2a9c395d89360484314bed2d81ecac5a80dafa5e37f16d95b4850.jpg)  
Fig. 6.41 Partial aperture synthesis by VLBI. Left: Location of North American antennas used. Right: Map of $\mathrm { H } _ { 2 } \mathrm { O }$ maser emission $( \lambda ~ = ~ 1 . 3 5 ~ \mathrm { c m }$ , $\nu = 2 2 . 2 \mathrm { G H z }$ ) from the young galactic Dsource GL 2591, an extremely dense cloud situated at $2 \mathrm { k p c }$ from the Sun. Note the high angular resolution and the beam profile. Inset: Spatial frequency coverage of the $( u , \nu )$ plane, resulting from the pairing of antennas and the Earth’s rotation $\scriptstyle ( u , \nu$ have units $D / 1 0 ^ { 7 } \lambda$ ). The baselines have lengths varying from $2 2 8 \mathrm { - } 3 9 2 9 \mathrm { k m }$ . After Walker et al., Ap. J. 226, 95, 1978. With the kind permission of the Astrophysical Journal

![](images/7a47fbaaa8bba909344dbaa76e93e7f4e05114c4a261889df1e2864125c3bbb9.jpg)  
Fig. 6.42 Worldwide network of radiotelescopes which can be combined in VLBI observations (2007). Regional networks are organised in Europe with the European VLBI Network (EVN), and in the USA with the Very Long Baseline Array (VLBA). Most of the instruments featured here are radiotelescopes, but some are specific to terrestrial geodesy, using VLBI to study continental drift and the deformations of the land masses over time. New instruments are frequently added to this network, e.g., the Antarctic

At the end of the decade 1980–1990, VLBI had been extended to millimetre wavelengths, thus putting large new antennas (30 to $5 0 \mathrm { m }$ ) to good use. In addition, the stability of frequency standards is improving (superconducting cavity oscillators, whose frequency width is thus reduced), the frequency range of recording equipment is increasing $\mathrm { ( > 1 0 0 M H z ) }$ ), and so, too, is the number of spectral channels (up to 1 024, see Sect. 8.4). Resolutions better than $1 0 ^ { - 4 }$ arcsec have been achieved in the millimetre region.

There is a very interesting application of VLBI to continental geodesy. Before the development of the Global Positioning System (GPS) in the 1990s, VLBI was able to detect the slow movements of continental drift over distances of the order of the size of the Earth.

The extension of VLBI to space observation is an interesting prospect. A telescope in a more or less elliptical orbit around the Earth, coupled to ground-based telescopes, would sweep out a large part of the spatial frequency plane during its orbit, and thus lead to measurements of high spatial frequencies, with good coverage of the $( u , \nu )$ plane. The onboard reference phase would be provided by a groundbased clock, of relative stability around $1 0 ^ { - 1 4 }$ , whose signal would be transmitted to the satellite and then returned to the ground by two-way telemetry. Before arbitrarily increasing the resolution, the brightness and compactness of the intended objects of study must be ascertained, so as to be sure that one resolution element does indeed emit sufficient power to stand out from the instrument noise.

The VLBI satellite now called the Space Observatory Project (VSOP then HALCA, Japan) was launched in 1997. Its maximum distance from Earth or apogee is at $2 1 4 0 0 { \mathrm { k m } }$ . Its $1 0 \mathrm { m }$ antenna operates at $\lambda = 6$ and $1 8 \mathrm { { c m } }$ (OH radical band), Dand its signals can be combined with data from terrestrial arrays like the VLBA (US), the European VLBI Network, or the Australian network (Fig. 6.42).

# 6.5.2 Ground-Based Optical Arrays

The three possible kinds of optical (visible and infrared) interferometry were described above, discussing the performance that can be achieved with each: direct, heterodyne, or homodyne combination of the beams delivered by the different telescopes. After abandoning the last around 1980, it was the first of these methods that attracted most interest at the beginning of the 2000s, resulting in the arrays set up around the world at the beginning of the twenty-first century. Figure 6.43 shows how these developments have gradually led to the arrays and networks we find today. However, the homodyne and heterodyne methods may reappear at some point in the future in other configurations, e.g., giant ground-based telescopes, space arrays, wavelengths in the far infrared, and so on.

![](images/fb74f9bbe6a23511a30c9e70002e5c5bf329e4daef221444da5b49f0fc4474c8.jpg)  
Fig. 6.43 Progress with the different approaches to ground-based optical (visible and infrared) interferometry between 1974 and 2006. Systems remaining in activity after this last date are extended with a . Diagram courtesy of Peter Lawson and completed by the authors

Here we examine the arrays based on two of the above methods, viz., heterodyne, then direct, and look at some of the results.

# Optical Interferometry: Infrared Heterodyne Method

The Infrared Spatial Interferometer (ISI) at the University of California, built on Mount Wilson in the 1980s, includes two mobile, $1 . 6 5 \mathrm { m }$ telescopes, with baselines of 4 to $7 0 \textrm { m }$ . Its special feature is that it uses the heterodyne technique at a wavelength of $1 0 . 6 ~ { \mu \mathrm { m } }$ , a $\mathrm { C O } _ { 2 }$ laser providing the local oscillator signal, and a mixer producing an IF signal in the usual way, with maximal frequency band 0.2 to $2 . 8 \ : \mathrm { G H z }$ . The sensitivity of the instrument is thus reduced by the narrowness of this spectral band. Nevertheless, the transfer of IF signals by cable is more convenient, using techniques tried and tested at radiofrequencies, and there exist several hundred stars in dust clouds which are bright enough to provide interference fringes with satisfactory signal-to-noise ratio, so the instrument is indeed a high quality tool (Fig. 6.44). On the other hand, high angular and spectral resolutions can be combined here, an advantage so far unique to this type of instrument, which can achieve a spectral resolution of $5 \times 1 0 ^ { 2 }$ . It has thus been possible to study the formation of ammonia $\mathrm { N H } _ { 3 }$ or silane $\mathrm { S i H _ { 4 } }$ molecules in evolved stellar atmospheres (like $\mathrm { I R C } + 1 0 2 1 6$ ).28

CGround-based heterodyne interferometry is unlikely to be a technique of the future for the reasons already stated. But in space, Table 6.3 shows that there is a crossover with the performance of direct interferometry in the far infrared and submillimetre regions, in particular when studying sources emitting in a spectral band. The future will no doubt tell whether this method can be successfully applied in space for these wavelength regions, which are still the least explored in the electromagnetic spectrum.

# Optical Interferometry: Michelson Method

As soon as optical interferometry came back on the scene in 1975, the idea of telescope arrays which had proved so effective at radiofrequencies became a major objective (Fig. 6.45). The family of optical interferometry arrays has moved forward very quickly since the 1980s, and the main technical problems have been resolved (Fig. 6.43 and Table 6.5). The advent of adaptive optics, which could make very large apertures (up to $1 0 \mathrm { m }$ ) spatially coherent, resulted in the use of large telescopes like VLT and Keck in interferometric mode.

![](images/c34baff480dc2c356e4a8a1e8c3e368871ebf5d18c77a18cb24a444881a112b5.jpg)  
Fig. 6.44 Power spectral density (in arbitrary units) of the interferometer signal (fringes) obtained using the heterodyne interferometer ISI at $\lambda = 1 0 . 6 \mu \mathrm { m }$ on the star $\alpha$ Orionis (Betelgeuse) in 1992. The frequency of the fringes, close to $1 0 0 \mathrm { H z }$ D, is determined by the Earth’s rotation, the position of the source in the sky, and the baseline vector $\pmb { B }$ . During the observation, the atmosphere causes a large and time-variable differential phase between the two optical paths, producing the ‘accordion’, or frequency modulation, effect on the fringes. This significantly widens the peak of the spectral density (by around $2 0 \mathrm { H z }$ ) and correlatively reduces its amplitude. Total observation time $4 . 5 \mathrm { { m i n } }$ . After Townes C.H. et al., Infrared Phys. 35, 1994

The Very Large Telescope Interferometer (VLTI)

The optical interferometer associated with the European Very Large Telescope went into operation in 2001, and at the time of writing (2007) is the most flexible and powerful instrument of its kind. High up on the Cerro Paranal in Chile, the four fixed $8 . 2 \textrm { m }$ telescopes are supplemented by an array of four mobile $1 . 8 \mathrm { ~ m ~ }$ telescopes that can be moved to any of 30 different positions (Fig. 6.46). Each telescope is equipped with adaptive optics. In the interferometric focal plane, the beams from two to at most four telescopes (in 2007), of either diameter, can be made to interfere after being brought by means of delay lines to a path length difference close to zero. Fringe detectors are positioned at the common focus. The first generation of instruments measures fringe visibility in the range $8 \mathrm { - } 1 3 ~ \mu \mathrm { m }$ (MIDI instrument, with spectral resolution up to 230) and $1 { - } 2 . 2 ~ { \mu \mathrm { m } }$ (AMBER instrument, spectral resolution up to 300). In addition, the system can operate in phase closure in order to measure the amplitude and phase of complex visibilities when simultaneously accepting the beams from three telescopes: 254 baselines are possible, extending up to $2 0 0 ~ \mathrm { m }$ , and able to supply up to 3 025 closure relations. A fringe tracker can compensate for random path length differences produced by atmospheric turbulence, provided one uses a bright enough star to ensure that the signal-to-noise ratio is sufficient during the atmospheric coherence time $\tau _ { \mathrm { c } }$ (similar magnitude limits to those for adaptive optics).

![](images/148aa4b448afdc3079a557469ad6607828e5d0edc0c1581d25c2cb772d7e0d47.jpg)  
Fig. 6.45 Artist’s impression of an array of $1 . 5 \mathrm { m }$ telescopes used for visible and infrared aperture synthesis. Note the rails allowing variation of $\pmb { B }$ , and also the common focus where the beams are recombined. The spherical mounting of the telescopes is novel. (Labeyrie A., La Recherche 76, 421, 1976. With the kind permission of La Recherche)

After 2009, a new generation of instruments should allow phase closure with four telescopes, high enough astrometric accuracy (around $1 0 0 ~ \mu \mathrm { a s } )$ for detecting the reflex motion of stars with massive exoplanets, and eventually the possibility of imaging the region close to the central black hole of the Galaxy with a desired astrometric accuracy of a few tens of $\mu { } \mathrm { a s }$ .

# The Keck Interferometer (KI)

Since 2001, the two $1 0 \textrm { m }$ telescopes located at the top of Mauna Kea (Hawaii), which are about $8 0 \textrm { m }$ apart, can be coherently coupled. This interferometer was specifically designed for observing exoplanets, and since 2005 has been equipped with a nulling fringe mode (see Sect. 6.6), which requires the use of high performance adaptive optics.

Table 6.5 Optical interferometric networks. In the uses column, $\lvert \mathcal { V } \rvert$ spectral amplitudes, I imagj jing, S spectroscopy, A astrometry, and N nulling. Data updated as of 2007   

<table><tr><td>Name</td><td>Site</td><td>Number and diameter of telescopes</td><td>Baselines [m]</td><td>Region [μm]</td><td>Uses</td></tr><tr><td>SUSI</td><td>Narrabri (Australia)</td><td>5 × 0.14</td><td>5-640</td><td>0.40-0.75</td><td>I,A</td></tr><tr><td>GI2T (Regain)</td><td>Calern (France)</td><td>2 ×1.5m</td><td>12-65</td><td>0.57-0.70</td><td>,S</td></tr><tr><td>VLT</td><td>Cerro Paranal</td><td>4×8.2m</td><td>20-200</td><td>1-12</td><td>I, S, A, N</td></tr><tr><td>interferometer PTI</td><td>(Chile) Mt. Palomar</td><td>4×1.8m 3 ×0.4m</td><td>110</td><td>2-2.4</td><td>A</td></tr><tr><td>Keck</td><td>(California) Mauna Kea</td><td>2×10m</td><td>85</td><td>2.2-10</td><td>||,N</td></tr><tr><td>interferometer NPOI</td><td>(Hawaii) Flagstaff</td><td>6×0.5m</td><td>2-437</td><td>0.45-0.85</td><td>A</td></tr><tr><td>COAST</td><td>(Arizona) Cambridge</td><td>5 × 0.65 m</td><td></td><td></td><td>I, S</td></tr><tr><td>IOTA</td><td>(UK) Mt. Hopkins</td><td>3×0.45m</td><td>5-38</td><td>1-2.4</td><td>I,S</td></tr><tr><td>CHARA</td><td>(Arizona) Mt. Wilson</td><td>6×1.0 m</td><td>34-331</td><td>0.55-2.4</td><td>I, S</td></tr><tr><td>MIRA</td><td>(California) Mitaka</td><td>2 × 0.3m</td><td>30</td><td>0.8</td><td></td></tr><tr><td>1 and 2 MROI</td><td>(Japan) Magdalena Mt.</td><td>6×1.4m</td><td>7.5-350</td><td>0.6-2.4</td><td>I, A, S</td></tr><tr><td>(2008) LBT</td><td>(New Mexico) Mt. Graham</td><td>2 ×6.5m</td><td>22.8</td><td>1-20</td><td>1,S</td></tr><tr><td>(Fizeau) ISI</td><td>(Arizona) Mt. Wilson</td><td>3 × 1.65 m</td><td>4-70</td><td>10.6</td><td>1,S</td></tr></table>

![](images/72a04d708cb46e2d8e5d2796c69ffc3b697131e87035bef2e167da8b7ff5d868.jpg)  
Fig. 6.46 Three of the mobile $1 . 8 \mathrm { m }$ telescopes of the VLTI, which is the interferometric configuration of the Paranal VLT. Original photo with the courtesy of Pierre Kervella

Optical Arrays and Densified Pupils. Consider a source $S _ { 1 }$ placed on the optical axis of two or more telescopes forming an interferometer. A fringe system is obtained at the common focus. Will a second source $S _ { 2 }$ situated at an angular distance $\alpha$ from $S _ { 1 }$ then be observable? For this to be the case, several conditions must be fulfilled. First of all, it must remain in the field of each telescope, which is usually quite wide. Secondly, the light beam from $S _ { 2 }$ must be able to propagate to the common focus, in particular through the delay lines, without being diaphragmed. This condition determines a maximum value $\alpha _ { \mathrm { m } }$ , which depends on the dimensions of the transfer optics. In the VLT interferometer, $\alpha \approx 2$ arcsec, which is a very small value, resulting from the hectometric optical paths to be travelled between telescope and common focus. One final condition concerns the configuration of the exit pupils, which must be homothetic to the configuration of the entrance pupils in order to ensure the fringe contrast for all $\alpha \leq \alpha _ { \mathrm { m } }$ . The latter condition, long considered intangible, is even referred to as the golden rule of an interferometer.

Now consider the common focal plane when an interferometer comprises several dilute entrance pupils, i.e., the diameter $D$ of the telescopes is very small compared with their separations $B$ , and observe a point source while satisfying the above homothety condition. The diffraction pattern of this telescope array leads to a significant spread of the PSF in the focal plane, making it very difficult to implement any coronagraph technique for eliminating the signal from this source in order to observe any very faint companions in its gravitational sphere. Suppose then that the exit pupil is rearranged, e.g., so that the exit pupils are now in contact with one another. The homothety condition is no longer satisfied, and the field $\alpha _ { \mathrm { m } }$ will be significantly reduced. On the other hand, the exit pupil will be more like that of a single telescope, and the PSF will have a bright central peak surrounded by secondary lobes. It will thus be easy to mask. It is straightforward to show that the reduction of the field is proportional to the rearrangement factor measuring how much the pupils are brought together as compared with the homothetic situation.

This remarkable idea of pupil densification, put forward by Antoine Labeyrie in 2000, led to the notion of hypertelescope. This could include, especially in space, several tens of apertures of metre dimensions, possibly several kilometers apart, but nevertheless delivering, in a tiny field, a highly concentrated interference pattern that would be easier to detect and cancel out if necessary.29

# Optical Interferometry: Fizeau Method

This refers to an arrangement in which delay lines serve no purpose since the equality of the optical path lengths between the different pupils and the common focal plane is satisfied by construction. Here is an example of just such a configuration.

The Large Binocular Telescope (LBT)

This instrument on Mt. Graham (Arizona) has been gradually set in operation since the end of 2005. It consists of two telescopes with diameter $D \ = \ 8 . 4 \ \mathrm { m }$ , fitted on the same altazimuth mount with their optical axes $B ~ = ~ 1 4 . 4 \mathrm { ~ m ~ }$ apart. The instrument thus looks like a conventional telescope, except that the entrance pupil is disconnected, comprising two distinct apertures. The highest observable spatial frequency is therefore $( B + D ) / \lambda$ . The baseline of the two telescopes is always Cnormal to the incident direction, so no delay line is required to compensate — except one of very small amplitude to adjust the zero PLD — and the interferometric field therefore has the same limitations as the normal imaging field of a telescope, i.e., several arcmin, much higher than an interferometer in the Michelson configuration. The mirror train is reduced to the strict minimum, i.e., primary, secondary, tertiary, then a return mirror on each beam is enough to supply the common focus. Alternatively, the two telescopes can be used with two independent instruments, but constrained to observe the same source, or at least the same region of the sky.

Roger Angel30 put forward the interesting idea known as $2 0 + 2 0$ , in which two independent telescopes of diameter $2 0 ~ \mathrm { m }$ each (for example) can move around a circular rail of diameter $B _ { \mathrm { M } }$ . Positioning the two telescopes at the ends of a chord of this circle of length $B \le B _ { \mathrm { M } }$ , arranging for the common focal plane to pass through the middle of this chord, and moving the two telescopes in such a way that the chord is always normal to the azimuth of the line of sight, the result is an interferometer with adjustable baseline $B$ , operating in Fizeau mode, hence without delay line. As in all interferometric setups using large pupils $\left( D \gg r _ { 0 } \right)$ ), the latter must be equipped with adaptive optics to restore coherence of the incident waves.

# Fibre Interferometry: Optical Hawaiian Array for Nanoradian Astronomy (’OHANA)

In fact, the acronym ’OHANA suggested by the French astronomer Jean-Marie Mariotti (1955–1998) has a double meaning, since it is also the Hawaiian word for ‘family’.

It is easy to understand how the need to transport the beams from each telescope to the common focus using a set of mirrors makes it practically impossible to achieve very long baselines, i.e., of hectometric order or more, on the ground. This stumbling block is avoided by extracting the light from the focus of each telescope and transferring it to the common focus by a single-mode optical fibre, which propagates the phase of the wave while preserving its temporal coherence (see Sect. 6.4.2). By choosing fibres of equal length from each telescope to the common focus, one can be sure that the optical paths are equal, and of course without atmospheric effects. It remains to obtain a zero path length difference using a variable delay line, as in a Michelson setup. Demonstrated in 2006 in the near infrared between the two Keck telescopes on Mauna Kea (Hawaii),31 this promising idea would make it possible, by coupling all the large telescopes located on this peak (Fig. 6.47), to obtain images of the cores of active galactic nuclei (AGN) like NGC1068 with resolutions as high as $2 0 0 \mu \mathrm { a s }$ .

![](images/c7efd180502996e5bf64c9dd095b8cd0cac990c6926a83918d39cfa9a82d353c.jpg)  
Fig. 6.47 Concentration of optical telescopes at the Mauna Kea site in Hawaii. The idea of fibre optic coupling can be used to connect two or more of these telescopes interferometrically, directly extracting light from Coude or Cassegrain focal points. The possible interferometric baselines are´ indicated on the left, while the insert on the upper right compares the arrangement of the four $8 . 2 \mathrm { m }$ telescopes of the VLT. Dotted circles show the first two configurations implemented in the first decade after 2000. From Mariotti J.M., 1995 and Perrin, G., 2006. Map due to the Institute for Astronomy, Honolulu. Altitudes are given in feet, where 1 foot $= 0 . 3 0 5 \mathrm { m }$

# Some Results from Optical Interferometry

Since the 2000s, optical interferomety has become a rapidly expanding technique in astronomy thanks to results that could be obtained in no other way. To see an example of this, consider Fig. 6.48, which shows the astrometric performance obtained in the 1970s with the first optical interferometers. The aim there was to measure stellar diameters, and the diameters of the orbits in close binary star systems from which the star masses could be deduced.

Figure 6.49 shows the accuracy that could be achieved in 2006 in the measurement of a visibility, and the way its wavelength dependence could be used to accurately specify the radial intensity distribution of a stellar atmosphere. In the example chosen here, the interferometric observation of Cepheid variables, crucial for determining distances in the Universe, provides a way of refining the accuracy of this fundamental length scale.

![](images/8e2b34fdf7be0cb106ff588ec31e4caf505ab50613602f864d4461cd61367f04.jpg)  
Fig. 6.48 Astrophysical and astrometric applications of aperture synthesis in the visible. Observations of the double system Capella $\scriptstyle ( { \alpha }$ Aurigae) A and B. Circles mark the two component stars, resolved and shown with their apparent diameters. X marks positions predicted for B on its orbit (Finsen). Shading indicates measured positions of B at different epochs (projections of baselines on the sky are shown at the same Julian dates, which are marked). Note the excellent resolution in the direction of the baseline, and the poor resolution in the perpendicular direction. Measurements obtained at the Plateau de Calern, France, with two $2 5 \mathrm { c m }$ telescopes. From Blazit A. et al., Ap. J. 217, L55, 1977. With the kind permission of the Astrophysical Journal

# 6.5.3 Space-Based Optical Interferometry

The difficulties caused by the Earth’s atmosphere, like those due to the Earth’s rotation (the need for continuously variable delay lines), have been sufficiently emphasised to show why space looks such a good place to set up optical interferometers, observing from the visible to the far infrared. But one should not underestimate the difficulties of quite another order raised by this undertaking: the need for telescopes flying in formation as soon as baselines exceed about ten metres and a supporting beam can no longer be used; variation of baselines to sample spatial frequencies; and holding optical paths to within a fraction of a wavelength. This is why, despite many proposals and projects, the spaceborne optical interferometers will not appear before 2010–2020. Two of these missions, currently under study, will be discussed here.

![](images/7df5a1ac8d1e143e75a2131f5280f77adc497c595b4700b6fbc29238ff9bc6de.jpg)  
Fig. 6.49 First demonstration of the presence of interstellar matter around the Cepheid star $l$ Carinae, using optical interferometry. The measured visibility (squared modulus) $\mathcal { V } ( \lambda ) ^ { 2 }$ is plotted versus $\lambda$ , in the atmospheric window around $\lambda = 1 0 ~ \mu \mathrm { m }$ . The VLTI works here with two $8 . 2 \textrm { m }$ telescopes, on a baseline $D = 4 0 ~ \mathrm { m }$ D, which sets the spatial frequency $D / \lambda$ at each $\lambda$ . At these wavelengths, the accuracy on $\mathcal { V } ( \lambda ) ^ { 2 }$ is limited by atmospheric and thermal noise. The star, with a photospheric radius of $2 . 7 0 \ \mathrm { m a s }$ , is practically unresolved, while the measured $\mathcal { V } ( \lambda ) ^ { 2 }$ shows the presence of a resolved envelope of ${ 8 \pm 3 }$ milliarcsec radius. Such envelopes are due to the periodic ˙ejection of matter by the pulsating star. The two curves (continuous and dashed) correspond to two different interferometric calibrations, using an unresolved star without envelope. Document Kervella, P. et al., Astron. Astroph. 448, 623 (2006)

# The Space Interferometry Mission (SIM) and NASA’s PlanetQuest

This astrometric mission aims to study extrasolar planets and at the same time to make exceptionally accurate measurements of the parallax of stars in the Galaxy.32

A 9-m beam, which can be oriented in space, will carry a series of $3 0 \mathrm { c m }$ telescopes that can be combined to form several interferometers. The common focal plane will be equipped with a CCD detector on which the fringes will form, in the spectral region $0 . 4 \mathrm { - } 0 . 9 ~ \mu \mathrm { m }$ . The instrument, placed in orbit around the Sun, will gradually move away from the Earth during its 5 year mission.

The key feature of the Space Interferometry Mission (SIM) is its high angular resolution. The diffraction limited resolution $\lambda / D$ is 20 mas. However, two factors allow the system to improve considerably on this limit. The first is instrumental stability since, in the absence of any atmosphere, the fringes are stable to better than $\lambda / 1 0 0$ for several minutes, allowing long time integrations, and hence extreme sensitivity (limiting magnitude $m _ { \mathrm { V } } = 2 0$ ). The second factor is that it can operate Din differential mode, comparing the positions of two nearby objects by the observed fringe shifts they each produce. This is how SIM can achieve resolutions in the range $1 { - } 4 \mu \mathrm { a s }$ . This mission could be launched in the decade from 2010.

In order to detect extrasolar planets, SIM would not observe the planet directly directly, since it would be too faint, but rather would measure the angular distance between the star $S$ thought to hold the planet and a distant reference star $S _ { \mathrm { R } }$ . Over time, the angle between $S$ and $S _ { \mathrm { R } }$ will vary for several reasons, i.e., proper motion of the stars and different parallaxes, but it will also vary if $S$ carries a planet, orbiting like $S$ around the centre of mass of the system. With a sensitivity of a few $\mu { } \mathrm { a s }$ , it will be possible to detect planets with comparable or even smaller masses than the Earth, after eliminating the two other effects, which can be determined independently.

To measure the distance of a star in the Galaxy, SIM will measure its parallax during the year, by simultaneous and oft-repeated observation of a reference star belonging to a reference grid distributed across the whole sky. With an ultimate resolution of $4 ~ \mu \mathrm { a s }$ , equal to the parallax of an object at a distance of $2 5 0 \mathrm { k p c }$ , SIM will be able to reach stars almost throughout the whole Galaxy with a very high level of accuracy.

With these two goals, SIM will complement the Corot and Kepler missions in search of exoplanets and also the GAIA mission for astrometry (see Sect. 4.2).

# ESA’s Darwin Mission

First proposed in 1993, just before the discovery of the first extrasolar planet in 1995, this mission33 exploits the technique of nulling interferometry This will be discussed in detail later (Sect. 6.6), in the context of coronagraphy techniques. For the moment, we shall just describe the array of telescopes, each with diameter $3 { \mathrm { - } } 4 \mathrm { m }$ , placed in a plane perpendicular to the line of sight as shown in Fig. 6.50. At the common focus, a dark interference fringe is formed at the position of the star, while the interference remains constructive at the suspected position of the planet, leading to a maximum amount of light, which must then be distinguished from the noise background, or the exozodiacal light, if there is any, due to dust present in the planetary system (as in our own Solar System). The instrument will operate in the wavelength range $6 . 5 \mathrm { - } 1 8 ~ \mu \mathrm { m }$ , in order to maximise the contrast between the star and the planet on the one hand, and in order to fall within the spectral region containing the spectral signature of ozone $\mathrm { O } _ { 3 }$ on the other. A low spectral resolution ( $R = 2 0$ ) suffices to reveal the presence of this molecule, which in turn indicates Dthe presence of oxygen. Placed at Lagrange point L2, it is relatively easy to protect it against radiation from the Earth, the Sun, and the Moon, since, viewed from L2, these three bodies remain more or less aligned all the time.

![](images/8fc8949d943c93662b6fd307ec36ce3d0a170f528c52fc077d427ee4712e9b73.jpg)  
Fig. 6.50 Artist’s view of a possible configuration for the ESA’s Darwin mission. A fleet of four independent satellites, each carrying a telescope and flying in formation, constitutes an interferometer. The interferometric signal is produced and processed by a fifth spacecraft, at which the four beams from the others are made to converge. It also provides the communications link with the Earth and the necessary energy via its solar panels. The whole system is placed at Lagrange point L2. Since its design in 1990, the configuration has been continually improved, in particular, by reducing the number of telescopes and hence the cost. (European Space Agency, 2007)

# Interferometry and X-Ray Radiation

It is already difficult at visible wavelengths to maintain the equality of optical paths at a small fraction of the wavelength. So how could one go about doing this at wavelengths a thousand times shorter, in the nanometre range, in order to resolve the X-ray emission produced in the immediate neighbourhood of a black hole? This is the challenge faced by the MAXIM space mission,34 under study at NASA. The environment of the black hole in the galaxy M87 (see Fig. 6.36), with estimated mass $M = 1 0 ^ { 8 } M _ { \odot }$ , is a bright $\mathrm { X }$ -ray source. The black hole has a Schwarzschild radius of $1 0 ^ { 1 1 } \mathrm { ~ m ~ }$ ˇ, which would require a resolution of $0 . 0 5 ~ \mu \mathrm { a s }$ at the distance of $1 8 \mathrm { { M p c } }$ to resolve it.

Young fringes have already been obtained with X rays in the laboratory,35 a natural consequence of their wave nature. In space, considering X rays of $1 \ \mathrm { k e V }$ $( \lambda \approx 1 \ \mathrm { n m } )$ , an angular resolution of $2 0 0 ~ \mu \mathrm { a s }$ could be achieved with a baseline of $B ~ = ~ 1 ~ \mathrm { m }$ , and telescopes with collecting areas of $1 0 0 ~ \mathrm { c m } ^ { 2 }$ would provide a Dcomparable sensitivity to the Einstein and Rosat missions. But the difficulty here lies in the detection of the fringes. On the one hand, their separation must be increased by interfering the beams (two or more, depending on the number of pupils used) over a very small angle. To obtain an fringe spacing of $1 0 0 ~ { \mu \mathrm { m } }$ with $\mathrm { X }$ rays of wavelength $1 \ \mathrm { n m }$ , the necessary amplification is $1 0 ^ { 5 }$ , which thus requires an angle of $1 0 ^ { - 5 }$ rad. The distance between the structure carrying the mirrors and the focal plane is therefore $1 0 ^ { 5 } B$ , or at least $1 0 0 \mathrm { k m }$ . As in the Darwin or LISA missions, the problem is to achieve highly accurate navigation of independent satellites (formation flight), here between the structure carrying the mirrors and the one carrying the detectors. At the same time, sufficient spectral selectivity is needed so that it is not necessary to obtain zero PLD in order to find the fringes: a spectral resolution of $1 0 ^ { 2 }$ to $1 0 ^ { 3 }$ is required to achieve this, leading to fringes that could be observed over several millimetres.

In a second stage, the baseline could be extended by further separating the satellites carrying each of the collecting mirrors. These ambitious missions involve complex technological development and are unlikely to see the light of day before 2020–2030.

# 6.6 High Dynamic Range Imaging (HDRI)

When imaging certain astronomical objects, there are some special cases in which the contrast in brightness between different regions of the field of view is extremely high, varying by a factor of as much as $1 0 ^ { 1 0 }$ . This is the case, for example, with the solar corona in the vicinity of the photosphere, circumstellar disks or exoplanets not far from a star, and active galactic nuclei. The generic term coronagraphy refers to all those methods aiming to obtain the image of a faint field around a very bright source by effectively masking the latter. These methods are also called high contrast imaging or high dynamic range imaging (HDRI).

# 6.6.1 Coronagraphy and Apodisation

In the case of an almost point source such as a star or active galactic nucleus, surrounded by structure of some kind separated by only a very small angle, e.g., disks or planets, high angular resolution is required, and adaptive optics and interferometry become essential. The dynamic range can be considerable, even as high as $1 0 ^ { 9 } – 1 0 ^ { 1 0 }$ .

Coronagraphy comes from the Latin word corona, meaning crown. Indeed, the technique was invented by Bernard Lyot,36 when attempting to image the solar corona in the years 1940–1950, by masking the solar disk, a million times brighter than the corona, in order to reveal the corona’s flamboyant activity.

Following the work by Lyot, who had the extremely powerful idea of putting a mask, not only in the focal plane, but also in the plane conjugate to the pupil, the only notable innovation over several decades was conceived by Jacquinot.37 He had the idea of reducing the amplitude of the feet of the diffraction pattern of the bright source by modulating the transmission by the pupil. This is the basic idea of apodisation, already mentioned briefly in Sect. 6.1.

It was only at the beginning of the 2000s, following the discovery of the first extrasolar planets, that this technique suddenly came back into the fore. The aim of forming the image of such planets in orbit around their star became a powerful driving force, resulting in an explosion of new concepts. It is important to realise just how difficult this is. The problem is to capture and identify, at a typical angular distance of 0.1 arcsec from a star, the photons from a companion that is $1 0 ^ { 1 0 }$ times (25 magnitudes) less bright, these values corresponding to the case of a system like the Sun–Earth system at a distance of $1 0 \ \mathrm { p c }$ from the observer (a frequently used case study).

# The General Problem

In almost all imagined solutions, the rule is to mask or otherwise extinguish the bright source, because the smallest leak of its photons would be disastrous. In addition, the wings of the diffraction pattern, which extend a long way, are sources of photon noise. Using the Fourier formalism, we first express the problem in complete generality, considering the optical system shown in Fig. 6.51 (lower). The entrance pupil modulates the amplitude of the incident wave, a phase and/or amplitude mask is placed in the focal plane on the axis of the bright source, and an image is once again formed on a pupil diaphragm, in order to block any residual diffracted light.

![](images/a17ccda7dca474b710d58bc8db24fe55a5c435a17ade2ed35f48bd47d4325dff.jpg)  
Fig. 6.51 Configuration of the Lyot coronograph. Light goes from left to right. Top: Without a stop in pupil C, the wings of the PSF appear in the final image plane D because of the diffracted light (edge rays). Bottom: The introduction of a stop in the reimaged pupil C blocks this contribution. The lens placed in the first focal plane B reimages the pupil, while the second lens in C provides the final focal plane image D. Source C. Aime & R. Soummer

Let $u ( x , y )$ be the amplitude in the pupil plane (1 in the pupil and 0 outside, if there is no modulation). Then the amplitude in the focal plane is $\nu ( x , y ) = \tilde { u } ( x , y )$ , where $\tilde { u }$ is the Fourier transform of $u$ D Q. Applying the focal mask amounts to writing

$$
\nu ( x , y ) = \widetilde u ( x , y ) \left[ 1 - M ( x , y ) \right] ,
$$

where $M$ is a complex quantity whose modulus $( \leq 1 )$ and argument describe the attenuation and phase shift introduced by the mask, respectively. In particular, $M$ equals unity where the mask is opaque and $M \ = \ 1 - \exp \mathrm { i } \pi \ = \ 2$ where the mask introduces a phase shift of $\pi$ D  D. In the conjugate pupil plane, the amplitude then becomes

$$
w = \tilde { \nu } = ( u - u \star \tilde { M } ) \times D ~ ,
$$

where $D$ is the diaphragm function. The amplitude $w$ thus results from the difference between the direct wave and the diffracted wave, a difference to which the pupil diaphragm is then applied.

The general problem raised by high dynamic range imaging is to make $w$ zero or minimal within the diaphragm. If we consider the space of free parameters represented by the modulation of the amplitude of the wave transmitted by the pupil, the modulations of the amplitude and phase of the wave transmitted by the focal plane, the amplitude of the wave transmitted by the pupil diaphragm and the shape of the latter, it is easier to understand how so many different solutions could have been put forward. However, we may consider two main families of solutions based on this scheme: those playing on the focal mask, referred to under the heading of coronagraphy, and those seeking to reconfigure the PSF, either on a bounded support, or by processing the residual faint regions in the final field, which come under the heading of apodisation.

Finally, the general heading of interferometric techniques will cover all other solutions, using a more sophisticated optical setup than the one shown in Fig. 6.52 and aiming explicitly to produce destructive interference to extinguish the bright source.

![](images/b6f2da8551564c89bc6365a72dfe8cb36100791f3d552b9db461a9608df1e7b4.jpg)  
Fig. 6.52 Example of the progression of light in a coronagraphic system. This basic Lyot scheme offers many possible variations and improvements, discussed in the text. From top to bottom: Uniform wave amplitude on the entrance pupil. Effect of an occulting mask in the first focal plane. Effect of a Lyot stop in the second pupil plane. Final image in the second focal plane. From R. Galicher

# Coronagraphy

The problem faced by Lyot when viewing the solar corona was to considerably reduce the light from the Sun’s disk, diffracted and scattered by all the optical defects.

The Lyot Coronagraph

The first and most natural idea is to place an opaque mask in the focal plane, slightly larger than the image of the solar photosphere. What Lyot then noted was that the diffraction by the mask itself, but also by all the tiny defects in the optical system, such as dust or phase defects, was the source of a significant diffuse background.

Indeed, consider an opaque particle of diameter $d$ in the focal plane. It diffracts a wave coming from a given direction into a solid angle of characteristic half-angle $\theta \ = \ \lambda / d$ . For example, if $d$ is of the order of the size of the diffraction spot, Di.e., $f \lambda / D$ ( $f$ being the focal length of the telescope and $D$ its diameter), then $\theta = D / f$ , i.e., the same angle as the geometrical beam. The convolution of the two Dsolid angles (geometrical and diffracted) means that a significant part of the light ends up outside the geometrical beam (of the order of $7 5 \%$ in our example). If an opaque mask containing a circular hole slightly smaller than the geometric pupil is placed in the plane conjugate to the pupil plane, then most of this diffracted light gets blocked, while light from another point of the field, not affected by our particle, will follow the path predicted by geometrical optics and will go through almost unaffected. Figure 6.51 shows this configuration.

Let us examine this result using the Fourier formalism introduced above. In the expression

$$
w = \mathrm { F T } \left( \nu \right) = \left( u - u \star \tilde { M } \right) \times D \ ,
$$

$D$ and $M$ are box or top-hat functions, equal to unity within the radius of the mask or diaphragm and zero outside. $\tilde { M }$ is a cardinal sine function which gets broader as the mask gets smaller. The left-hand side of Fig. 6.52 shows the evolution of the wave amplitude in successive planes, and in particular the different components of the amplitude in the pupil plane C: the direct wave (Fig. 6.52e), the wave diffracted by the mask (Fig. 6.52f), and their difference before (Fig. 6.52g) and after (Fig. 6.52h) inserting the mask. We see that the maximum intensity (modulus squared of the amplitude) is concentrated at the radius of the image of the pupil in the form of a bright ring. This is precisely what caught Lyot’s attention. We thus understand why the pupil diaphragm must be slightly smaller than the geometric image of the pupil if the diffracted light is to be effectively blocked.

The Roddier & Roddier Coronagraph38

Franc¸ois and Claude Roddier had the idea of replacing the amplitude focal mask by a phase mask, i.e., a transparent mask producing a path length difference as a function of its thickness. If this difference is equal to $\lambda / 2$ , it then introduces a phase shift of $\pi$ , in other words a change in the sign of the amplitude.

The relation established for the Lyot mask becomes

$$
\nu ( x , y ) = \tilde { u } ( x , y ) \left[ 1 - 2 M ( x , y ) \right] ,
$$

and in the conjugate pupil plane,

$$
w = \mathrm { F T } \left( \nu \right) = \left( u - 2 u \star \tilde { M } \right) \times D \ .
$$

If the size of the phase mask is chosen judiciously (radius $0 . 5 3 \lambda / D$ ), the level of extinction will be high and the amplitude of $w$ can be further reduced with respect to the Lyot solution. The increased efficiency of this solution can be interpreted by considering that the incident wave has been divided into two parts, with approximately equal integrated amplitudes, one undergoing a phase shift of $\pi$ , whereupon the destructive interference of these two waves produces the desired extinction effect.

![](images/c56d6ab2842afbd1dbb90dae3eb68001dbdd10a650e8df9502f0acde6dbf657d.jpg)  
Fig. 6.53 Four-quadrant phase mask coronagraph. In the focal plane, the image of the star to be extinguished is placed at the centre of symmetry of the mask. (a) The phase mask (schematic). (b) Function to be integrated to obtain the amplitude in the pupil. It can be shown that the integral is zero, however far off centre the disk may be

Rouan Coronagraph39

This solution is also based on the phase mask idea, producing destructive interference once again. The mask, which affects the whole focal field, is formed by juxtaposing four quadrants, two of which, in diagonally opposite positions, produce a phase shift of $\pi$ (Fig. 6.53a). It can then be shown that a source perfectly centered at the meeting point of the four quadrants will be totally extinguished, i.e., $w = 0$ Duniformly in the pupil, the diffracted light being rejected entirely outside the pupil.

The full pupil condition, in particular without central obstruction of the telescope, must nevertheless be satisfied for this to work. This is one of the desired cases where $w = 0$ . Indeed, the term $u \star \tilde { M }$ reduces here to the convolution product of the pupil Dfunction and $1 / x y$ , which is simply the integral of the function $1 / x y$ over a region corresponding to an off-centre disk, as shown in Fig. 6.53b. Exploiting the power of a point with respect to a circle, there is an elegant proof due to Jean Gay (2002) that this integral must be strictly zero, however far off centre the disk may be.

Several coronagraphs based on this idea have already been installed in telescopes: two devices operating at $2 . 2 ~ { \mu \mathrm { m } }$ on the NACO adaptive optics system of the VLT, and three others in the mid-infrared instrument (MIRI) camera, one of the four focal instruments of the James Webb Space Telescope (JWST) developed by NASA in collaboration with Europe. The latter instrument (expected launch in around 2014) is designed for direct detection of giant extrasolar planets in the $1 1 - 1 6 \mu \mathrm { m }$ range. The instrument known as spectropolarimetric high-contrast exoplanet research or SPHERE, expected to equip the VLT in 2012, is designed for an analogous purpose but at shorter wavelengths, and uses similar components.

Notch Filter Mask

This solution also uses a focal mask, but here it is the transmission that is modulated by what is known as a notch filter mask, whose radial transmission varies as $1 - \sin r / r$ . It can then be shown that $\tilde { M }$ is a box function and that its convolution with $u$ is flat over a large region which covers part of the pupil. The quantity $( u - u \star \tilde { M } )$ is thus zero over the main part of the pupil, as required, except for a ring-shaped region on which the pupil diaphragm is applied. Note that this mask can also be designed to modulate in just one dimension.

There are several limitations to the use of focal masks:

• To arrange for $u$ and $u \star \tilde { M }$ to be as similar as possible (the condition for cancelling w), $\tilde { M }$ must be as close as possible to a $\boldsymbol { \delta }$ function, i.e., it must have a very narrow support. This in turn means that the focal mask, its Fourier conjugate, must have a very broad support, which is barely compatible with the fact that the aim is to form an image of the field as close as possible to the central source. The four-quadrant phase mask is an exception here, and for this reason is rather large, since it extends over the whole field, while conserving good ‘transmission’ close to the axis. • The formalism used here assumes that the wavefront is perfectly plane, which is never the case in practice due to optical defects and atmospheric perturbations. In particular, it is absolutely essential to use adaptive optics for ground-based observation, because the PSF of the bright source must be quasi-coherent and must be maintained very accurately on the axis of the focal mask. This is therefore the main limitation of coronagraphs in use at the time of writing (2007), including those soon to be used in space. Ways of reducing the consequences of this limitation will be discussed below.

In phase mask systems, the phase shift introduced by the mask is not independent of the wavelength, since it is generally achieved using a slab of thickness $e$ and refractive index $n$ $( \phi = 2 \pi e n / \lambda$ ). This means that it will only be effective in a narrow spectral band centered on Dthe wavelength $\lambda = 2 e n$ .

Various solutions have been suggested to make the $\pi$ phase shift achromatic in the latter case. Undoubtedly one of the most promising, proposed by Mawet and coworkers, is to use a zero order grating (ZOG). Such components are obtained using nanotechniques, etching grooves of width smaller than the wavelength (so-called sub-lambda grooves) on a substrate. It can be shown that these gratings have birefringent properties with a different refractive index between the ordinary and extraordinary axes which can be made linear in . This amounts to having an achromatic phase shift between two perpendicular polarisations. The idea then is to etch grooves in one direction on two opposite quadrants, and perpendicular grooves on the other two quadrants. Whatever the polarisation state of the incident light, the desired $\pi$ phase shift is indeed introduced.

Following the same line of thinking, a very elegant solution is the achromatic groove phase mask (AGPM). This picks up the ZOG idea except that the sub-lambda grooves have circular symmetry. The effect of the differential path length difference between two perpendicular polarisations is indeed obtained, as with the four-quadrant ZOG, but the effect of the boundary between the quadrants disappears, which is a non-negligible advantage. Figure 6.54 illustrates the solutions based on the ZOG.

# Apodisation

In this family of techniques, the idea is to play rather on the function $u$ in the equation $w = \mathrm { F T } \left( \nu \right) = \left( u - \epsilon u \star \tilde { M } \right)$ . There are two aims:

• To ensure that the feet of the PSF of the bright source do not extend too far, or at least decrease more abruptly than in a classical Airy disk (in which the intensity decreases on average as $\theta ^ { - 3 }$ ). To round off the profile $u$ of the pupil so that it matches as well as possible the profile of the diffracted wave, i.e., the convolution product $u \star \tilde { M }$ . Indeed, just as we have seen that a narrow focal mask implies $\tilde { M }$ with wide support, so the convolution product is described by a function closer to a bell shape than a top hat.

Non-Circular Pupil

A first solution is to consider particular shapes of aperture so that, in one or more selected directions, the profile of the PSF decreases much faster than the Airy disk. This is the case with a square pupil: indeed, in the directions corresponding to the diagonals, the brightness profile of the PSF varies as $\theta ^ { 4 }$ , whereas it only decreases as $\theta ^ { 2 }$ in any other direction. Another solution, put forward by Kasdine and Spergel, is to consider apertures of Gaussian shape. Figure 6.55 shows such a pupil along with the corresponding PSF and the brightness profile in the optimal direction. Other combinations in which several different Gaussian profiles are juxtaposed are also possible.

![](images/41c41d43c43a3263d342bcc6c08c84ff4e0c9801c9fa32f9ca235849e4676e57.jpg)  
Fig. 6.54 ZOG version of the four-quadrant phase mask coronagraph. The quadrants are etched with grooves with spacing $p < \lambda$ using nanotechniques. The shape birefringence introduced in this way produces the desired $\pi$ phase shift between quadrants, as illustrated by the two configurations of the electric field components. Source: D. Mawet

![](images/ab52ad7c82da705e07c47e2298c87f45b174764ebf7a04d2d4728285efa27570.jpg)  
Fig. 6.55 The Kasdine–Spergel coronagraph. Left: the pupil shape; center: the point spread function; right: a cut along the $\mathbf { X }$ -direction revealing the very low level of residual light on each side of the main core

For all these solutions, the high contrast part of the field, i.e., the part in which faint structures might be sought, is rather limited. In particular, it must be possible to rotate the telescope about its optical axis in order to explore the whole environment of the bright source.

# Variable Transmission Pupil Mask

If $M$ is an indicator function (taking values 1 or 0), Aime and Soummer have shown that the equation $w = ( u - \epsilon u \star \tilde { M } ) \times D = 0$ can be construed as an eigenvalue D problem with solution the pair $[ u = \phi , \varLambda ]$ , where the eigenvalue, if it exists, is $\varLambda = 1 / \epsilon$ D. Such solutions exist for the Roddier–Roddier coronagraph $( \epsilon = 2$ ) for Da circular or rectangular aperture. The function $\varPhi$ Dis then a particular mathematical function, viz., a linear or circular prolate spheroidal function, respectively. In the case of a Lyot coronagraph $( \epsilon = 1 )$ ), there is no exact solution, but approximate Dsolutions can be defined using these same functions, solutions which become more efficient as the mask gets larger. What is remarkable in this case is the fact that the amplitude of the wave diffracted by the mask is proportional to the amplitude in the entrance pupil. The process can thus be reiterated by introducing a series of focal mask/pupil diaphragm pairs, each introducing the same reduction factor for the stellar light. The extinction then increases exponentially with the number of stages. This idea is under investigation for the SPHERE instrument to equip the VLT, as mentioned earlier.

The difficulties in making masks where the transmission varies according to a precise law may be overcome by using high-energy beam sensitive (HEBS) materials. These can become opaque in a stable manner under the effects of high energy electron bombardment. A narrow electron beam can be computer controlled to scan a HEBS film deposited on a glass slab in order to obtain a mask with very precise transmission profile.

In this same family of apodising pupil masks, a very elegant solution is phase induced amplitude apodization (PIAA), suggested by Olivier Guyon. To get round the fact that the resolution and equivalent transmission are degraded in conventional amplitude modulation (since a pupil mask necessarily absorbs light), Guyon suggested playing on the shape of the optical surfaces to concentrate or dilute the light rays in the exit pupil of an afocal system, as shown in Fig. 6.56. The apodisation effect on the PSF is the same as for a pupil mask but without the drawbacks. The collecting area of the primary mirror of the telescope is fully exploited.

Optical surfaces capable of producing the desired brightness distributions are highly aspherical, and since the optical arrangement no longer respects the Gauss conditions, the useful field becomes very small. However, this is not a serious problem, since the structures sought, e.g., exoplanets, are always very close in angular terms to the optical axis of the bright source. Moreover, by using an identical but reversed optical system after passing through a coronagraphic mask — a simple Lyot mask is perfectly suitable, since the resulting PSF has bounded support — the isoplanicity properties of the field can be reestablished. The main difficulty with this solution is in producing specific aspherical surfaces, whose radius of curvature must vary by several orders of magnitude along a diameter.

![](images/2ababaeba0200a1ba275bdfd29e9481bf00e9ef5c3c66f2feeecf1cbc3dc31e7.jpg)  
Fig. 6.56 The Guyon PIAA coronagraph. The pupil is reshaped thanks to aspheric optics. Source: O. Guyon

# Interferometric Solutions

Although inspired by Lyot’s idea, devices using phase masks already exploit the principle of destructive interference of the wave coming from the bright source. In this last part, we discuss methods aiming explicitly to produce such destructive interference, but without resorting to the focal mask/pupil diaphragm scheme originally proposed by Lyot.

Achromatic Interferential Coronagraph (AIC)

It was in fact just such a method, proposed by the French astronomers Jean Gay and Yves Rabbia, that triggered new interest in coronagraphy at the end of the 1990s. Achromatic interferential coronagraphy (AIC) exploits a Michelson interferometer to make the wave from the bright source interfere destructively with itself. The novelty here is to reverse the wave in one arm of the interferometer by passing it through the focal point of an optical system. Only the wave strictly on the axis will remain parallel to its counterpart in the other arm and hence be able to interfere uniformly and destructively with the latter, while a wave at a small angle of incidence $\theta$ , e.g., coming from a nearby companion, will meet its counterpart in the recombination output at an angle $2 \theta$ , preventing any effective interference. Moreover, recalling that the effect of passing through a focal point is to introduce a phase shift of $\pi$ , i.e., a change of sign of the amplitude, the two arms of the interferometer can be of strictly equal length, which simplifies the design, but above all allows destructive interference whatever the wavelength, a significant advantage which justifies calling the device achromatic.40

The visible nulling coronagraph (Lyon, 2005) is a further variation on the theme of destructive interference. This idea, which also exploits a Michelson interferometer, is analogous to the AIC in many ways. The main difference is that one of the two beams is not reversed but simply translated a distance $B$ (brought to the level of the entrance pupil, i.e., the diameter of the telescope): the pupils overlap significantly in a cat’s eye pattern. The phase shift $\pi$ which ensures destructive interference on one of the two interferometer outputs is introduced by adjusting the optical path difference in one of the arms. The effect of translating one pupil relative to the other is then analogous to the effect obtained in a nulling interferometer comprising two telescopes whose baseline would simply be $B$ . The field of view of the telescope is modulated by a series of fringes, alternately dark (extinguished) and bright (transmissive), placing the bright source that needs to be attenuated on a dark fringe. The further advantage with this setup is that the operation can be repeated by injecting the dark output into a similar interferometer, but applying the separation/translation operation in a perpendicular direction. The extinction profile then goes as $\theta ^ { 4 }$ , which attenuates the star more efficiently. Figure 6.57 shows how this works. Note, however, that this kind of optical system is difficult to implement in practice.

To end this discussion of single-pupil interferometric solutions, let us describe two methods which complement the other instruments invented to extinguish the bright source. The main limitation that must be faced by all these solutions when they are eventually set up and required to achieve the extreme levels of performance involved in detecting extrasolar planets, such as those mentioned in the introduction, will be the extreme difficulty in distinguishing a true planet from a speckle due to residual, even very small, defects in the optics. Indeed, even defects of the order of ten picometres on the wavefront of a very large telescope could very easily simulate an Earth-sized planet!

# Self-Coherent Camera

This instrument, proposed by Pierre Baudoz, exploits the fact that stellar and planetary photons are not coherent. If the final coronagraphic image is made to interfere with a beam of pure stellar light extracted upstream, the residual speckles will be modulated by a fringe system, while the spot formed by any planet will not be. A careful analysis of these fringes by Fourier transform methods would then provide a way, at least in principle, of removing any ambiguity.

![](images/13c8cadb5c6c2fbcd7495784ed3db806e656614aebdc48980d246e5ce345f5fb.jpg)  
Fig. 6.57 Visible nulling coronagraph due to Lyon and Shao based on a Michelson interferometer with a shear of one beam with respect to the other. ${ \boldsymbol { \mathrm { S } } } =$ beam splitter, $\mathbf { M } =$ dihedral mirror

Speckle Cancellation

Another way of reducing residual speckles, proposed by Traub and Borde (2005), ´ would be to measure them, and then cancel them using a deformable mirror. To begin with, a carefully chosen series of very small amplitude wave forms is applied to this mirror, of the same dimensions as residual defects in the wavefront after passing through whatever form of coronagraph has been used. Then, by analysing the resulting series of images and using a little linear algebra, it is possible to reconstruct the right form of wave to apply to the mirror in order to correct these residual defects. After a few iterations, the process should converge.

This solution is based on a remarkable property of the electric field in the pupil after passing through a coronagraph: to a first approximation, it is directly proportional to the perturbed phase $\varPhi$ , because in the truncated expansion of the input amplitude, viz., $\exp \mathrm { i } \phi \approx 1 + \mathrm { i } \phi$ , only the first term vanishes as a result of the action of the coronagraph. Put another way, a perfect coronagraph can only extinguish the coherent part of the image of the bright source.

# Conclusion

Which of these methods will meet the challenge of forming an image of a planet orbiting around a main sequence star? At the time of writing (2007), no one would be able to reply to this question. The development of such instruments is likely to remain highly active in the coming years. Looking beyond the design of theoretically excellent optical systems, the problem of implementing them in the real world has become a major preoccupation. A clear consensus has already been reached on one key point: only a complete system comprising telescope $^ +$ extreme adaptive optics $^ +$ Cfocal instrument, dedicated at the outset to this aim, will ever Cobtain the image of details of a sister planet to our own.

# 6.6.2 Nulling Interferometry

Here we discuss a variant of coronagraphy. The idea is still to use interference properties to reduce the extreme intensity contrast between two very close objects, usually a star and a planet, in order to study the fainter of the two. However, in this case, the solution is interferometric recombination of the beams from several telescopes. The term nulling interferometer could then be replaced by coronagraphic interferometer, as we shall in Sect 9.6.

# Basic Idea

The method of nulling interferometry suitably complements conventional coronagraphy. Indeed, the latter is a technique that is essentially applicable to the visible and near infrared regions. This is because it is only at these wavelengths that the angular resolution of a large telescope is of the same order of magnitude as the angle subtended by a typical planetary orbit of 1 AU at a distance of $1 0 \mathrm { p c }$ . While life does provide spectral signatures in this region of the visible — basically, through oxygen and the chlorophyll function — the star–planet intensity contrast remains extremely high, typically of the order of $1 0 ^ { 1 0 }$ .

On the other hand, in the mid-infrared region, this contrast is much more favourable, being of the order of $1 0 ^ { 6 . 5 }$ . Furthermore, a set of less ambiguous biological signatures than those observable in the visible has been identified. These are provided by ozone at $9 . 7 \mu \mathrm { m }$ , carbon dioxide, and water vapour (see Fig. 6.58). It has been shown that the simultaneous presence of these three signatures could constitute a very strong indication that life is present, at least in a form similar to life on Earth. The quest to identify this trio has been made the cornerstone of ESA’s Darwin programme (see above), while NASA’s TPF-I programme will pursue a similar aim, but today, both projects have been shelved.

![](images/68b3bdc4e6ce157b43301c9ea41700417351f9400cac8bea34ddcee7687ef563.jpg)  
Fig. 6.58 The mid-infrared spectrum of the Earth shows three spectral signals due to ozone, carbon dioxide, and water vapour which, if observed together, would constitute a biosignature that is in principle unambiguous. Upper: Observed and modelled infrared spectra of the Earth viewed from a distance. Lower: Laboratory spectra of various atmospheric components. See also Fig. 9.20

An angular resolution of 0.1 arcsec at $1 5 \mathrm { \ \mu \mathrm { m } }$ implies either a monolithic telescope of diameter $3 0 \mathrm { ~ m ~ }$ , whose feasibility in space is far from obvious, or an interferometer with a baseline longer than $3 0 ~ \mathrm { m }$ . The second option has been favoured for the Darwin project proposed back in 1996 by Alain Leger and cowork- ´ ers, based on the assumption that spacecraft could fly in stable and reconfigurable formations without excessive difficulty. However, the problem of dazzle by light from the star remains just as critical as ever with an interferometer, whence it is still essential to apply some blocking procedure analogous to coronagraphy.

![](images/3fdc68ce5084fd5bcc1b621fe70980552770e70ea14d50d667f0d42ea20689c7.jpg)  
Fig. 6.59 Principle of nulling interferometry, as proposed by Bracewell. Values for the baseline $D$ , the wavelength $\lambda$ , and the separation $\theta$ are given as examples. Left: Schematic of the interferometer, with a $\pi$ phase shift introduced in one arm. Right: The on-axis star is extinguished by the dark fringe, while the off-axis planet remains observable. Source: M. Ollivier

# The Bracewell Interferometer

The solution to this difficult problem was put forward by Ronald Bracewell41 as early as 1978, in a seminal paper, where he describes the principle of nulling interferometry. The idea, illustrated in Fig. 6.59, is to produce interference fringes, projected on the sky, by interferometrically recombining the beams from two telescopes a distance $B$ apart. If we can arrange for the star to lie on a dark fringe and for the fringe spacing to correspond to the distance between the star and the supposed planet, then the contrast is optimal.

However, it would be of little use to work at a single wavelength, because the planet is extremely faint and the spectral information required lies in a vast wavelength range, from 5 to $1 7 ~ { \mu \mathrm { m } }$ for the Darwin instrument. In a conventional interferometer, only the bright central fringe, the one corresponding to zero optical path difference, would be common to all wavelengths, while the fringe systems of different wavelengths would overlap and interfere mutually for every other position in the sky. The powerful idea put forward by Ronald Bracewell was to insert a phase shift of $\pi$ that did not depend on the wavelength, i.e., an achromatic phase shift, in one arm of the interferometer. This produces a dark fringe common to all the fringe systems. If this is placed on the star, efficient extinction becomes possible, without being limited to any spectral band.

The measured signal is the sum of the flux from the planet(s), light residues from the star, and local zodiacal light in the observed planetary system. The latter is generally called the exozodi. It corresponds to scattering of radiation from the star by a disk of micron-sized dusts left over from the protoplanetary disk, and constitutes a powerful source, much brighter than the planets themselves.

To distinguish the fraction intrinsic to the planet, its signal must be modulated. Bracewell suggested rotating the interferometer about the line of sight. The planet then follows a trajectory on the fringe system projected onto the sky, so that it is sometimes visible, sometimes extinguished, in such a way that only the signal modulated at the rotation frequency and agreeing with the expected pattern reflects the contribution from the planet.

# Difficulties

Several difficulties arose when more detailed studies of Bracewell’s ideas were carried out, with a view to detecting exoplanets. It will be instructive to give a brief analysis of these difficulties.

Non-Infinitesimal Angular Size of the Star

Even if it cannot strictly resolve the disk of the photosphere, the nulling interferometer allows photons from its most peripheral regions to escape. Indeed, the extinction zone is not a box shape, but a parabolic function of the angular distance, represented by a truncated expansion of $1 - \cos \theta$ . Naturally, very few of these photons get through, but the planet–star contrast is such that they are nevertheless predominant, and their statistical noise becomes a prohibitive limitation. Even more efficient extinction is thus required, going as $\theta ^ { n }$ with $n > 2$ . It can be shown that more than two telescopes are needed to achieve this.

Several configurations have been found, more or less empirically, to achieve this aim. One of the simplest is Angel’s cross. This produces a nulling function going as $\theta ^ { 4 }$ . It uses four telescopes placed at the ends of a cross, and introduces a $\pi$ phase shift in one of the two telescopes in each branch of the cross.

Other setups use telescopes of different sizes. Finally, one can also consider configurations where the phase shift is not $\pi$ but a fraction of $2 \pi$ , as in the three-telescope configuration studied a few years ago for the Darwin project. Recently, it has been shown that an arbitrary power $\theta ^ { n }$ can be obtained by combining $2 ^ { n }$ telescopes and associating a $\pi$ phase shift with half of them, chosen using a binary sequence known as the Prouhet–Thue–Morse sequence.´ 4 4 This sequence has the property that no finite subsequence is repeated more than twice consecutively in the sequence.

Achromatic $\pi$ Phase Shift

To obtain a signal of significant magnitude, a broad enough spectral interval must be analysed, and this requires a device that can obtain the $\pi$ phase shift as achromatically as possible throughout the interval. In 2007, several ideas are being explored and have been demonstrated in the laboratory:

![](images/7f89714195bbd2151b6da9b62f978cacee8d9310bd42b228afb0fe7efc87e201.jpg)  
Fig. 6.60 Various methods to produce an achromatic phase shift in a nulling interferometer. Left: using plates of different optical index (see text); center: using a periscopic setup to reverse the electric field direction; right: crossing the focus of a spherical mirror. Source: Y. Rabbia

• A first solution is to insert a set of transparent plates in each arm of the interferometer, choosing the materials and thicknesses so that the dependence of the path length difference on the wavelength is linear over the whole of the relevant spectral region. The phase difference is then achromatic. . A second solution exploits a property of Fresnel reflection on a mirror at $4 5 ^ { \circ }$ , viz., only the electric field component lying in the plane of the mirror undergoes a change of sign. The idea is to have the beam reflect on two symmetric pairs of periscopes (set of three successive mirrors at incidence $4 5 ^ { \circ }$ ), in such a way that the two components $s$ and $p$ of the electric field end up undergoing a reversal on one channel as compared with the other, as shown in the central part of Fig. 6.60. The third idea is to make use of the particular property that an electromagnetic wave undergoes a $\pi$ phase shift when it passes through a focal point. It is enough to arrange that the beam pass through the focal point of a spherical mirror in just one arm of the interferometer in order to obtain an achromatic $\pi$ phase shift.

Note that the last two solutions can only achieve phase shifts equal to $\pi$

Separating Planetary and Exozodi Light Signals

The symmetry of revolution of the exozodi light would only correspond to a planetary system viewed face on, which is a highly improbable configuration. Consequently, the elliptical brightness distribution of the exozodi generally produces a modulation by the fringe system, analogous to that of a planet. This is where the choice of interferometer configuration becomes crucial. Depending on the structure of the fringe system, or rather the maxima and minima of the transmission map, the signal modulations produced either by an isolated object like a planet or by a centrally symmetric structure like the exozodi will be more or less distinct. In 2007, investigations aim to identify the configurations that could best discriminate the two.

Temporal Stability of Stellar Flux Cancellation

This last difficulty is perhaps the most serious. Indeed, any deviation of the phase shift from $\pi$ , even very small, would produce very large relative fluctuations in leaks of stellar light, and these would largely dominate photon noise from the exozodiacal light, the latter fixing the fundamental detection limit. This question is very carefully considered in simulation experiments.

# Problems

6.1. Show that, for quasi-monochromatic radiation,

$$
| \gamma _ { 1 2 } ( \tau ) | = | \gamma _ { 1 2 } ( 0 ) | \quad \mathrm { i f } \quad \tau \ll \tau _ { \mathrm { c } } ,
$$

where $\tau _ { \mathrm { c } }$ is the correlation time. Set $V ( t ) = f ( t ) \exp ( 2 \pi \mathrm { i } \nu _ { 0 } t )$ , with $f ( t )$ slowly varying.

Answer. With the suggested notation,

$$
{ \cal T } _ { 1 2 } ( \tau ) = \langle V _ { 1 } ( t ) V _ { 2 } ^ { * } ( t + \tau ) \rangle = \langle f _ { 1 } ( t ) f _ { 2 } ^ { * } ( t + \tau ) \exp ( - 2 \pi \mathrm { i } \nu _ { 0 } \tau ) \rangle \ .
$$

The quasi-monochromatic approximation, $\tau \ll \tau _ { \mathrm { c } }$ , then implies $f _ { 2 } ( t + \tau ) \approx f _ { 2 } ( t )$ , whence

$$
\begin{array} { r } { T _ { 1 2 } ( \tau ) = T _ { 1 2 } ( 0 ) \exp ( - 2 \pi \mathrm { i } \nu _ { 0 } \tau ) \ . } \end{array}
$$

Taking the modulus and normalising, the result follows.

6.2. Consider an interference experiment with quasi-monochromatic light (Young’s slits) and express the visibility $\mathcal { V }$ of the fringes as a function of the fields $V _ { 1 } ( t )$ and $V _ { 2 } ( t )$ of the two sources. Show that

$$
| \gamma _ { 1 2 } ( \tau ) | = \mathcal { V } .
$$

Answer. At the point $Q$ observed and at time $t$ , the amplitude of the observed field is obtained from the superposition of the two sources

$$
V ( Q , t ) = V _ { 1 } ( t - \tau _ { 1 } ) + V _ { 2 } ( t - \tau _ { 2 } ) \ ,
$$

where $\tau _ { 1 }$ and $\tau _ { 2 }$ are the respective times taken by the light between the sources and the point $Q$ .

The observed intensity is $I ( \boldsymbol { Q } , t ) = \langle V ( \boldsymbol { Q } , t ) V ^ { * } ( \boldsymbol { Q } , t ) \rangle$ , which gives

$$
I ( \boldsymbol { \mathcal { Q } } , t ) = I _ { 1 } ( \boldsymbol { \mathcal { Q } } , t - \tau _ { 1 } ) + I _ { 2 } ( \boldsymbol { \mathcal { Q } } , t - \tau _ { 2 } ) + 2 \mathrm { R e } \langle V _ { 1 } ( t - \tau _ { 1 } ) V _ { 2 } ^ { * } ( t - \tau _ { 2 } ) \rangle ~ .
$$

The assumption that the light is quasi-monochromatic gives

$$
\tau _ { 1 } \ \mathrm { a n d } \ \tau _ { 2 } \ll \tau _ { \mathrm { c } } = 1 / \Delta \nu
$$

which allows simplification of the previous relation. Putting $\tau = \tau _ { 1 } - \tau _ { 2 }$

$$
I ( Q , t ) = \left[ I _ { 1 } ( Q , t ) + I _ { 2 } ( Q , t ) \right] + 2 \sqrt { I _ { 1 } ( Q , t ) I _ { 2 } ( Q , t ) } \mathrm { R e } \bigl ( \gamma _ { 1 2 } ( \tau ) \bigr ) .
$$

Finally, as $Q$ moves, the value of $\tau$ changes, so that the intensity exhibits fringes of visibility given by

$$
\frac { 2 \sqrt { I _ { 1 } ( \mathcal { Q } , t ) I _ { 2 } ( \mathcal { Q } , t ) } } { I _ { 1 } ( \mathcal { Q } , t ) + I _ { 2 } ( \mathcal { Q } , t ) } \left| \gamma _ { 1 2 } ( \tau ) \right| .
$$

In the simple case when $I _ { 1 } ( Q , t ) = I _ { 2 } ( Q , t )$ , this gives visibility $| \gamma _ { 1 2 } ( \tau ) |$ .

6.3. Check that the coherence degree of order $n$ of a quasi-monochromatic wave obeys

$$
| \gamma _ { n } ( \tau ) | = 1 .
$$

6.4. A source is in the form of a grid of brightness

$$
I ( \pmb \theta ) = I _ { 0 } \sin 2 \pi \frac { \theta _ { x } } a .
$$

(a) What is the spatial spectrum $\tilde { I } ( \boldsymbol w )$ of this grid?

(b) An astronomical source (a young star forming, or the nucleus of a galaxy) has profile

$$
I ( \theta ) = I _ { 0 } \exp \left( - \frac { \theta ^ { 2 } } { 2 a ^ { 2 } } \right) , \quad a = 0 . 1 \mathrm { a r c s e c } .
$$

What is its spatial spectrum?

(c) An optically thin circumstellar envelope around a star, is such that the brightness of the whole ensemble is given by

$$
I ( \theta ) = I _ { 0 } \exp \left( - \frac { \theta ^ { 2 } } { 2 a ^ { 2 } } \right) + I _ { 1 } \delta ( \theta - \theta _ { 0 } ) \ , \quad a = 0 . 1 \mathrm { a r c s e c } \ .
$$

The radius of the star is $1 0 ^ { 1 2 }$ cm and its distance $4 0 0 \ \mathrm { p c }$ $\mathrm { 1 p c } = 3 \times 1 0 ^ { 1 8 } \mathrm { c m } )$ The envelope extends out $1 0 ^ { 1 5 }$ D cm all round. What is its spatial spectrum?

(d) A double star is such that one component has twice the intensity of the other. What is its spatial spectrum?

In each of the four cases, analyse the filtering effect on the image produced by pupils of increasing size, for some fixed wavelength.

Answer. The spatial spectra are just the Fourier transforms of the intensities.

(a) For the grid,

$$
\tilde { I } ( w ) = { \frac { \mathrm { i } } { 2 } } I _ { 0 } { \frac { a } { 2 } } \left\{ \delta \left[ { \frac { a } { 2 } } \left( u - { \frac { 1 } { 2 } } \right) , \nu \right] - \delta \left[ { \frac { a } { 2 } } \left( u + { \frac { 1 } { 2 } } \right) , \nu \right] \right\} \ .
$$

(b) For the Gaussian source,

$$
\tilde { I } ( w ) = I _ { 0 } \sqrt { 2 \pi } a \exp \left( - 2 \pi ^ { 2 } a ^ { 2 } w ^ { 2 } \right) .
$$

(c) For the circumstellar envelope, using the result in (b) and linearity of the Fourier transform,

$$
\tilde { I } ( w ) = I _ { 0 } \sqrt { 2 \pi } a \exp \left( - 2 \pi ^ { 2 } a ^ { 2 } w ^ { 2 } \right) + I _ { 1 } \exp \left( - 2 \mathrm { i } \pi \theta _ { 0 } w \right) .
$$

(d) For the binary system,

$$
\begin{array} { r } { I ( \pmb \theta ) = 2 I _ { 1 } \delta ( \pmb \theta ) + I _ { 1 } \delta ( \pmb \theta - \pmb \theta _ { 0 } ) , } \end{array}
$$

which implies

$$
\tilde { I } ( w ) = I _ { 1 } \left[ 2 + \exp ( - 2 \mathrm { i } \pi \theta _ { 0 } w ) \right] .
$$

The modulus thus exhibits fringes.

The effect of the limited size of the pupil is to cut off spatial spectra at the spatial frequency $D / \lambda$ . In the image plane, the restored image is the convolution of the image source with the PSF, an Airy function which spreads as the pupil diminishes.

6.5. Consider an object $I ( \pmb \theta )$ whose spatial spectrum is circularly symmetric (e.g., a star or a solar granulation). Show that all the spatial information can be obtained by a simplified telescope whose pupil is limited to a slit:

$$
G ( r ) = \pi \left( \frac { x } { D } \right) \pi \left( \frac { y } { a } \right) , \quad D \gg a ,
$$

replacing a conventional telescope of diameter $D$ .

6.6. A telescope ${ \cal D } { = } 3 . 6 \mathrm { m }$ ) forms an image of a source at wavelength $\lambda { = } 0 . 5 \mu \mathrm { m }$ . Its focal ratio is $f / D = 1 0 0$ . What is the optimal sampling rate $x$ Dfor the image, if Dit is effectively limited by diffraction? The grain of the detecting photographic plate creates white detector noise up to a frequency corresponding to a grain size of $3  { \mu \mathrm { m } }$ .

Show that the choice of a finite sampling rate $x$ has the effect of increasing the noise spectral density in the frequency domain containing the useful information.

6.7. A star appears as a disk, assumed to have uniform surface brightness, at the wavelength $\lambda _ { 0 }$ :

$$
I ( \pmb \theta ) = I _ { 0 } \varPi \left( { \frac { \theta } { \theta _ { 0 } } } \right) \ .
$$

Calculate its spatial spectrum. Show that, if the image is formed by a pupil of diameter $D$ such that $\theta _ { 0 } = \alpha \lambda _ { 0 } / D$ , $( \alpha \ : < 1 )$ ), then the determination of $\tilde { I } ( w )$ on $( 0 , w _ { \mathrm { c } } )$ nevertheless gives $\theta _ { 0 }$ , provided that it is assumed a priori that the star is a uniformly bright disk (super-resolution).

Answer. The spatial spectrum of the star is

$$
\tilde { I } ( w ) = { \frac { I _ { 0 } } { \pi \theta _ { 0 } w } } J _ { 1 } ( \pi \theta _ { 0 } w ) \ .
$$

The central peak of the Bessel function $J _ { 1 }$ extends to greater spatial frequencies than those sampled by the mirror. Therefore, only a truncated sampling of this function is available, and moreover, it is affected by a certain degree of noise. This sampling can be used to determine the value of $\theta _ { 0 }$ , using least squares or cross-validation fitting methods, provided that the form of $\tilde { I } ( \boldsymbol w )$ is known a priori. In the object plane, this means that the size of the structure is smaller than the diffraction size.

6.8. Michelson Interferometer. Consider a pupil consisting of two circular apertures of diameter $d$ , with separation vector $\pmb { D }$ , where $d \gg D$ , and an object of spectrum $\tilde { I } ( \boldsymbol w )$ , observed at the zenith, at wavelength $\lambda$ .

(a) Write the transfer function $\tilde { T } ( \boldsymbol { w } )$ and approximate it in terms of Dirac distributions. (b) Express the visibility of the fringes as a function of $\tilde { I } ( \boldsymbol w )$ .

Answer. The transfer function is the autocorrelation of the pupil. We consider here the limiting case of two pointlike openings,

$$
G ( w ) = \delta ( { \bf 0 } ) + \delta \left( { \frac { \cal D } { \lambda } } \right) .
$$

Then, for any other shift than 0 and $\pm { \pm } \pm \lambda$ , the product $G ( w + r / \lambda ) G ^ { * } ( r / \lambda )$ is zero, whence the approximation is

$$
\tilde { T } ( w ) = \delta ( { \bf 0 } ) + { \frac { 1 } { 2 } } \delta \left( w - { \frac { \cal D } { \lambda } } \right) + { \frac { 1 } { 2 } } \delta \left( w + { \frac { \cal D } { \lambda } } \right) .
$$

The spatial spectrum of the object after this filtering is thus

$$
\hat { I } ( \mathbf { 0 } ) + 0 . 5 \hat { I } ( { \cal D } / \lambda ) + 0 . 5 \hat { I } ( - { \cal D } / \lambda ) ,
$$

so that, in the symmetric case, fringes of visibility $\hat { I } ( { \cal D } / \lambda ) / \hat { I } ( \mathbf { 0 } )$ are produced.

6.9. The intensity interferometer (Hanbury-Brown, ARAA 6, 13, 1968) is based on the following principle: two telescopes, separated by a distance $x$ , receive photons $\lambda = 0 . 5 \mu \mathrm { m } ,$ ) from the same source, on two photomultipliers delivering currents $I _ { 1 } ( t )$ and $I _ { 2 } ( t )$ .

(a) Show that the cross-correlation function of the two currents, formed in a correlator which introduces a delay $\tau$ , and given by

$$
C ( \tau ) = \langle I _ { 1 } ( t ) I _ { 2 } ( t + \tau ) \rangle ~ ,
$$

contains information about the spatial structure of the observed object. Use the complex degree of coherence of the radiation as an intermediate step.

(b) Before correlation, $I _ { 1 }$ and $I _ { 2 }$ are filtered by two low-pass electric filters, with transfer functions $H ( f ) ~ = ~ \varPi \left( f / 2 \Delta f \right)$ . If $\Delta f \sim 1 0 ^ { 6 } ~ \mathrm { H z }$ , what error is D tolerable along the cables bringing each signal to the correlator? Compare with the precision required in a Michelson interferometer, at the same wavelength, and with the spectral interval $\Delta \lambda = 1 \mathrm { n m }$ .

6.10. Consider a parabolic mirror forming an image on its axis of a point at infinity.

(a) The mirror deviates slightly from a true paraboloid by an error described by $\varepsilon ( r ) = \varepsilon _ { 0 } \cos ( 2 \pi x / a ) , a = D / n , \varepsilon _ { 0 } = \lambda / 5$ , where $n \gg 1$ . Show that, as D D D 	far as the image is concerned, this is as if the pupil function $G ( r )$ had been replaced by a new complex pupil function $G ^ { \prime } ( r )$ (a phase mask). Deduce the point source response (image of a point) of the imperfect mirror.

(b) Answer the same question if $\varepsilon ( r )$ is now a random function with constant power spectrum up to some characteristic frequency $s _ { 0 } = 1 / 1 0 \lambda$ .

D(c) Why is the criterion for mirror surface quality taken as $\sigma _ { \varepsilon } < \lambda / 2 0$ , where $\sigma _ { \varepsilon }$ is the standard deviation of the surface error?

(d) Why is the spatial spectrum of the random variable $\varepsilon ( r )$ important?

6.11. Calculate the coherence length for the electromagnetic signal transmitted by each antenna of a radio interferometer operating at $\lambda ~ = ~ 1 8 ~ \mathrm { c m }$ , and receiving a frequency bandwidth $\Delta \nu \ : = \ : 1 \ : \mathrm { M H z }$ D from the incident radiation. Is this length Daffected by the change in frequency brought about by means of a local oscillator on each antenna?

Answer. The autocorrelation of the field is the Fourier transform of its power spectrum. Hence, if this is truncated over a width $\Delta \nu$ , the corresponding coherence time is $\tau _ { \mathrm { c } } = \Delta \nu ^ { - 1 }$ . The coherence length is therefore $l _ { \mathrm { c } } = c \tau _ { \mathrm { c } } = c / \Delta \nu = 3 ~ \mathrm { m }$ . D D D DThis is not affected by any frequency change brought about by local oscillators.

6.12. Consider $N$ antennas, intended to be aligned in an aperture synthesis arrangement. The intervals between antennas are chosen to be multiples of some length $a$ . For each value of $N$ between 2 and 6, inclusive, find the distances which give the non-redundant pupil with the best coverage of spatial frequency, by combination of pairs of antennas. Bearing in mind the rotation of the Earth, should the configuration be arranged east–west or north–south?

6.13. An object is observed in the visible $\langle \lambda = 0 . 5 \mu \mathrm { m } \rangle$ , with spectral resolution $R = \lambda / \Delta \lambda$ increasing from 1 to $1 0 ^ { 5 }$ D. At ground level, the sky background produces Da continuous emission of 1 rayleigh $\textrm { \AA } ^ { - 1 }$ (Sect. 2.3). In a plot of telescope diameter $D$ , from 1 to $2 0 \mathrm { m }$ , against the magnitude $V$ of the object, trace, for different spectral resolutions $R$ , the loci of the points at which the noise from the sky background is equal to the signal noise. Take the field to be 1 arcsec, and the quantum efficiency multiplied by the total transmission to be 0.5. What conclusions can be drawn for the use of large telescopes in obtaining high spectral resolution?

6.14. An infrared telescope is used at the diffraction limit, at wavelength $\lambda \ =$ $1 0 0 ~ { \mu \mathrm { m } }$ , with spectral resolution $\lambda / \Delta \lambda ~ = ~ 1 0$ D. Calculate the power received Dat the focus, in the beam etendue corresponding to the diffraction limit, taking ´ $T _ { \mathrm { m i r r o r } } = 3 0 0 ~ \mathrm { K }$ , emissivity $\mathcal { E } ^ { \mathrm { ~ ~ } } = 0 . 1$ , and using the Rayleigh–Jeans approximation. D DCompare this with the sensitivity of a detector with noise equivalent power $\left( { \mathrm { N E P } } \right) =$ $1 0 ^ { - 1 \bar { 6 } }$ W $\mathrm { H } z ^ { - 1 / 2 }$ D(the definition of the NEP is given in Sect. 7.1). What can be concluded from this comparison?

Answer. The beam etendue is written´ $S \varOmega$ , where the solid angle observed satisfies $\begin{array} { l l l } { \Omega } & { = } & { ( \lambda / D ) ^ { 2 } } \end{array}$ at the diffraction limit, and this implies a beam etendue of´ $\pi \lambda ^ { 2 } / 4$ , regardless of the telescope diameter. Moreover, the flux of a blackbody at temperature $T$ is

$$
B _ { \nu } ( T ) = 2 k T / \lambda ^ { 2 } \qquad [ \mathrm { W } \mathrm { m } ^ { - 2 } \mathrm { s r } ^ { - 1 } \mathrm { H z } ^ { - 1 } ]
$$

in the Rayleigh–Jeans approximation.

In order to make the comparison with the sensitivity of the detector, calculate the received power per beam etendue, in ´ $\mathrm { V } \ \mathrm { H z } ^ { - 1 / 2 }$ , at the wavelength and resolution under consideration $\bar { \Delta } \nu = c \Delta \lambda / \lambda ^ { 2 }$ ):

$$
\frac { \varepsilon 2 k T } { \lambda ^ { 2 } } \frac { \pi \lambda ^ { 2 } } { 4 } \sqrt { \frac { c \Delta \lambda } { \lambda ^ { 2 } } } = \frac { \varepsilon \pi k T } { 2 } \sqrt { \frac { c } { R \lambda } } = 3 . 4 \times 1 0 ^ { - 1 6 } \mathrm { W H z ^ { - 1 / 2 } } \ .
$$

Therefore, with the given observational characteristics, detector sensitivity is not the limiting factor.

6.15. Invariance of the Complex Amplitude Correlation Function in Fresnel Diffraction. Let $\psi _ { z } ( \pmb { x } )$ be the complex amplitude of a wavefront at position $z .$ , with $\boldsymbol { x }$ the position variable in the wave plane. Show that the complex amplitude at the position 0 is given by the convolution

$$
\psi _ { 0 } ( \mathbf { x } ) = \psi _ { z } ( \mathbf { x } ) \star { \frac { 1 } { \mathrm { i } \lambda z } } \exp \left( \mathrm { i } \pi { \frac { x ^ { 2 } } { \lambda z } } \right) ~ .
$$

Answer. The method used in this chapter can also be applied here, ensuring the conservation of energy. Show that

$$
{ \cal B } _ { 0 } ( x ) = \langle \psi _ { 0 } ( \xi ) \psi _ { 0 } ^ { * } ( x + \xi ) \rangle = { \cal B } _ { z } ( x ) = \left. \psi _ { z } ( \xi ) \psi _ { z } ^ { * } ( x + \xi ) \right. .
$$

The convolution is converted into a multiplication by Fourier transform.

6.16. The Fried Parameter. Assuming the expression $I _ { \mathrm { A } } ( \pmb \theta )$ , given in this chapter, for the Airy image of a circular pupil, calculate the exact value of the Fried parameter $r _ { 0 } ( \lambda )$ , by carrying out the integration

$$
\int B _ { \mathrm { 0 } } ( \boldsymbol { w } ) \mathrm { d } \boldsymbol { w } = \int \tilde { T } _ { \mathrm { A } } ( \boldsymbol { w } ) \mathrm { d } \boldsymbol { w } , \qquad \tilde { T } _ { \mathrm { A } } ( \boldsymbol { w } ) = \mathrm { F T } \left[ I _ { \mathrm { A } } ( \pmb { \theta } ) \right] ,
$$

and with $B _ { 0 } ( w )$ equal to the long-exposure MTF. [The resulting $r _ { 0 } ( \lambda )$ is given in the text.]

6.17. The star T Tauri is observed as two sources in the near infrared. One of these sources also emits in the visible, and the other at radiofrequencies. The latter is separated by a distance 0.9 arcsec along the north–south axis, and the intensity ratio is $\alpha$ .

Show that a knowledge of $| \tilde { I } ( w ) |$ from speckle interferometry is not enough in j jitself to show which source is the more northerly. (Dyck H.M. et al., Ap. J. 255, L103, 1982.)

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