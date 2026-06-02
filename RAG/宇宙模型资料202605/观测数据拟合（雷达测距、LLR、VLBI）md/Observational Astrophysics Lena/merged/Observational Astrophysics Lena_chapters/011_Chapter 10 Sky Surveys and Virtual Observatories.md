# Chapter 10 Sky Surveys and Virtual Observatories

Astronomers have always catalogued the objects they observe and study. In ancient times, the Greek astronomer Hipparchos (between 161 and $1 2 7 \mathrm { B C }$ ) and the Chinese astronomers Shi Shen and Gan De (in the Warring States period, around $5 0 0 ~ \mathrm { B C }$ ) built up the first systematic catalogues of the celestial regions accessible from their parts of the world. Tycho Brahe did likewise, followed by surveys of non-stellar objects, such as Messier’s.1 At the end of the nineteenth century, sky surveys marked the beginning of the great modern catalogues. Computers completely transformed this landscape in the last decade of the twentieth century, by vastly increasing the volumes of data that could be stored, while improving accessibility, addressability, and communications through a range of automated systems. In this chapter, we shall consider some of the results of this revolution. In addition to the development of statistical astrophysics and systematic whole sky surveys across all wavelengths, we will also discuss the advent of virtual observatories which bring together all available maps and data about a specific object, to assist in solving whatever astrophysical problem is under investigation.

# 10.1 Statistical Astrophysics

Modern astronomy is characterised by a genuine flood of data, growing exponentially. There are several reasons for this rapid evolution. The first, rather obvious, stems from growing instrumental capacities in terms of telescope size (see Chap. 5), number of pixels on 2D detectors (see Chap. 7), and resolution and spectral range of spectrometers (see Chap. 8). Another, more subtle reason is that, in several areas of astrophysics, the desired information, whether it concern a phenomenon on the cosmic scale or a particular class of objects, can now only be firmly established by analysing a sample containing thousands up to tens of millions of individual objects. Only these large samples suffice to reduce the effects of dispersion or lack of resolution in order to isolate some very dilute effect. Very ambitious observing programmes called large surveys often involve dedicated instruments as well as general purpose instruments on large telescopes. They are carried out over months or years by international consortiums, bringing together dozens of researchers.

Galactic astronomy and modern cosmology are two disciplines that depend heavily on this type of observation. And recently, scientists interested in the more remote regions of the Solar System have also become active in the development of sky surveys, in their search for objects beyond the orbit of Neptune.

The study of the Galaxy, e.g., stellar populations, structure, and components of the interstellar medium, has given rise to many exhaustive surveys, particularly in the centimetre and millimetre wave radio regions. In other wavelength regions, satellites observing in the infrared and at high energies have supplemented these surveys. Figure 1.7 illustrates the exceptional spectral coverage obtained in this way.

Cosmology has generated some very extensive programmes, and is continuing to do so. In each endeavour, whether it be the identification of large-scale structures as instantiated by clusters and associations of galaxies, the study of the evolution of the first galaxies in the remote universe, witness to the processes involved in assembly of the first structures, or the mapping of dark matter by weak gravitational lensing effects, the images of millions of galaxies must be acquired and analysed in order to identify statistically significant trends. In this context, the need for a statistical dimension covering very large numbers of objects is well exemplified by attempts to determine cosmological parameters as accurately as possible.

The search for rare objects is rather different but nevertheless involves quite analogous needs in terms of the amount of information that must be acquired and analysed. In this case, the desired property is not shared in some tenuous way by millions of individual sources, but is particular feature of a rarefied population that can only be tracked down within a huge population of superficially similar objects by identifying some specific signature. The search for quasars, planetary nebulas, brown dwarfs, free-floating planets,2 and trans-Neptunian objects are all the subject of such ambitious programmes.

One particular type of large survey is the class of exhaustive sky surveys, i.e., covering the whole celestial sphere in a certain wavelength region. This kind of survey was first attempted in the visible at the end of the nineteenth century with the ambitious international undertaking known as the Carte du ciel.3 The aim was to produce a complete photographic atlas of the sky in the two hemispheres, comprising no fewer than 22 000 photographic plates. Unfortunately, it was never quite finished, but was taken up again with more success at the beginning of the second half of the twentieth century by the Palomar Optical Sky Survey (POSS). This particularly effective survey was carried out using the very wide field telescope invented by Bernhardt Schmidt. It was then supplemented by equivalent surveys carried out in the southern hemisphere from the vantage point of Australia and Chile. A little later, radioastronomy was to catch up, e.g., with the Parkes–MIT–NRAO (PMN) survey, closely followed by infrared astronomy with the IRAS satellite in 1983, which mapped the sky in the far infrared. And high energies have not been neglected. With surveys like the one carried out by ROSAT in the X-ray region in 1992, there is scarcely any wavelength region in which the whole sky has not already been surveyed at the time of writing (2007). Astrometric surveys are also extremely important, with the Hipparcos mission in 1989, and the even more impressive GAIA mission, planned for 2012, which should investigate a billion stars (see Chap. 4).

Concerning the analysis of data generated in this way, a large survey is characterised by several parameters, of which the most important are the field covered, the sensitivity (or depth), the completeness, and the confusion limit:

• Field. This is the area covered by the large survey. Some surveys cover the whole sky, or just one of the two hemispheres. The field must be extensive to ensure that the results are not dominated by specific effects of concentration or rarity. The term cosmic variance is generally used in observational cosmology to qualify this cause of uncertainty.   
. Sensitivity or Depth. This is the magnitude or flux of the faintest unambiguously detected objects. This is often a criterion of the kind flux $> \ n \sigma$ , where $\sigma$ is the uncertainty in the flux measurement. The depth of the survey generally depends directly on the exposure time in a given direction. The survey must be deep to ensure that reliable statistics can be obtained for particularly remote or intrinsically faint objects. Depending on the objects under investigation, a compromise is always sought between sensitivity and field, since the total time allocated to such a programme must remain within reasonable bounds of months or years.   
. Completeness. This is closely related to the last feature. It is defined as the apparent magnitude (or flux) beyond (or below) which only a given fraction (usually $50 \%$ ) of the relevant objects is effectively detected. A conventional method for determining this completeness limit is to introduce simulated data into the real data in a realistic way and then to determine the fraction effectively detected by the algorithm. A survey can by complete, in the case where almost no member of the relevant class of objects has been omitted.   
. Confusion Limit. If several sources are located in the element of spatial resolution of the observing instrument, the counts obtained will be incorrect because the apparent position and flux of the sources will be modified by the mixing with generally fainter sources. This is known as source confusion, and the resulting measurement error is referred to as confusion noise. This problem first appeared in radioastronomy, where antenna sidelobes are significant.

![](images/9506e8f956db5e7b2008d1fa35028b8c9dd2dac4de2527321daf3f470044b719.jpg)  
Fig. 10.1 Source confusion and spatial resolution in the images of a field of $6 . 6 ^ { \prime } \times 6 . 6 ^ { \prime }$ observed in the infrared and containing galaxies. Top: ISO mission, $\lambda = 1 7 0 ~ \mu \mathrm { m }$  and Spitzer mission, $\lambda = 1 6 0 \mu \mathrm { m }$ . Bottom: $\lambda = 7 0 \mu \mathrm { m }$ , $\lambda = 2 4 \mu \mathrm { m }$ D. G. Lagache et al. ARAA 43, 727, 2005, with the D Dkind permission of the publisher

The infrared region can also be sensitive to this limit, whenever the sensitivity becomes high while the angular resolution remains modest. This is exemplified by infrared space observatories like IRAS (1983), ISO (1995), and Spitzer (2003), where the telescopes, with diameters less than one metre, provide angular resolutions in the range between a few arcsec and one arcmin, while the sensitivities achieved are excellent owing to the absence of thermal background in space (see Fig. 10.1).

# 10.2 Large Sky Surveys

The period from 1980 to 2007 has certainly been the golden age for large sky surveys. A series of such programmes led to major changes in our understanding, particularly in cosmology, which until then had been restricted to largely theoretical developments, owing to the lack of sufficient observational data. This golden age is set to continue for a few more years at least, with ever more ambitious projects. Without trying to be exhaustive, we shall discuss here the large photometric, spectroscopic, and cosmic microwave background surveys summarised in Table 10.1.

Table 10.1 Some large sky surveys currently available or in progress (2007)   

<table><tr><td>Name</td><td>Means</td><td>入</td><td>Field</td></tr><tr><td colspan="4">Photometric sky surveys</td></tr><tr><td>APM</td><td>Measuring machine</td><td>Visible</td><td>Southern hemisphere</td></tr><tr><td>SDSS</td><td>Camera (ground)</td><td>Visible</td><td>10000 deg²</td></tr><tr><td>CFHTLegacy</td><td>Camera (ground)</td><td>Visible</td><td>410 +170+ 4 deg²</td></tr><tr><td>IRAS</td><td>Satellite (1983)</td><td>12,25,60,100 μm</td><td>Southern hemisphere</td></tr><tr><td>2MASS</td><td>Camera (ground)</td><td>Near infrared</td><td>Whole sky</td></tr><tr><td>DENIS</td><td>Camera (ground)</td><td>Nearinfrared</td><td>Whole sky</td></tr><tr><td>Einstein</td><td>Satellite (1979)</td><td>X ray</td><td>Whole sky</td></tr><tr><td>XMM</td><td>Satellite (1999)</td><td>X ray</td><td>5deg²</td></tr><tr><td colspan="4">Spectroscopic sky surveys</td></tr><tr><td>CfA2</td><td>Ground</td><td>Visible</td><td>17 000 deg²</td></tr><tr><td>DEEP2</td><td>Ground</td><td>Visible</td><td>3.5 deg²</td></tr><tr><td>SDSS</td><td>Ground</td><td>Visible</td><td>10000 deg²</td></tr><tr><td>VVDS wide</td><td>Ground</td><td>Visible</td><td>16 deg²</td></tr><tr><td>VVDS deep</td><td>Ground</td><td>Visible</td><td>1.5 deg²</td></tr><tr><td>ZCOSMOS</td><td>Ground</td><td>Visible</td><td>1.7 + 1.0 deg²</td></tr><tr><td colspan="4">Cosmic microwave background surveys</td></tr><tr><td>COBE</td><td>Satellite (1989)</td><td>1.25 μm-5 mm</td><td>Whole sky</td></tr><tr><td>BOOMERANG</td><td>Balloon</td><td>25-412 GHz</td><td>Southern hemisphere</td></tr><tr><td>WMAP</td><td>Satellite (2001)</td><td>22-90 GHz</td><td>Whole sky</td></tr><tr><td>PLANCK</td><td>Satellite (2008)</td><td>30-857 GHz</td><td>Whole sky</td></tr></table>

The list is impressive, but reflects the spectacular progress in cosmology over the years 1995–2005, including the discovery that the expansion of the Universe is actually accelerating, with the accompanying dark energy hypothesis, confirmation of inflation, confirmation of the flat universe model, measurements of most cosmological parameters with ever increasing accuracy, evidence for dark matter, and so on.

Large sky surveys generally use dedicated systems either in the form of a specialised instrument at the focus of a telescope that can be used for other purposes, or as a complete telescope/instrument system custom built for the task at hand. In the latter case, this system may be spaceborne.

# 10.2.1 Sky Surveys at Visible Wavelengths

# Schmidt Sky Surveys and Their Digitisation

To work effectively, these surveys must be able to access a wide field in one go, while nevertheless keeping a good angular resolution. In the optical region, the large photographic plate set up at the focus of a Schmidt telescope served this purpose well for several decades. The surveys made with these instruments from 1950 to 2000 nevertheless have a rather poor quantum efficiency, limiting them to magnitudes below 19 to 21, depending on the colour, and poor photometric quality owing to the non-linearity of the photographic emulsion. Despite these limitations and their age, these surveys are still the only ones providing access to the whole sky at resolutions of the order of a few arcsec, so they remain genuinely useful. The main drawback with them, namely that they could not directly provide digital information suitable for mass processing and archiving, is no longer a problem, thanks to systematic digitisation of the plates.

The three large Schmidt surveys were:

• SERC/AAO (Siding Spring Telescope, Australia) for the southern hemisphere $( \delta < 0 ^ { \circ }$ ). The two series of plates are denoted by J (blue) and I, from 1974 to 1987, and R from 1990 to 2000. POSSI/POSSII (Palomar Schmidt Telescope): E (red) and O (blue) for $\delta > - 2 0 ^ { \circ }$ , from 1950 to 1958. J (blue), F (red), N (band I) for $\delta > 0 ^ { \circ }$ , from 1987 to 2000. The field of a POSS plate is in general $5 ^ { \circ } \times 5 ^ { \circ }$ with mean angular resolution 3 arcsec. ESO: R (red) for $\delta < - 2 0 ^ { \circ }$ from 1978 to 1990.

These surveys were distributed to observatories the world over in the form of copies on large format photographic paper, filling enormous amounts of shelving and generally accompanied by superposable transparent sheets containing multiwavelength information about identified sources.

Today, the Schmidt sky surveys have been made available by digitising the photographic plates. This was done using specialised machines which explore the plates point by point with high mechanical accuracy, thereby translating their grey levels into digitised pixels.

The Automatic Plate Scanner (APS) at the University of Minnesota produced the POSSI E and O plate digitisations. The resulting catalogue contains 200 million objects (north) from the first epoch along with a catalogue of galaxies. All the recorded objects correspond to double detections in two colours. The Proper Motion Machine (PMM) was implemented by the US Naval Observatory (Washington, USA). The POSSI and POSSII measurements of the AAO-J, SERC, and ESO were used to produce the USNO catalogue, containing 520 million objects. Two rough magnitudes (R and B) are given for these objects. This is a reference catalogue for astrometry. The Automated Plate Measurer (APM) is in Cambridge (UK). This machine digitised the AAO-R, SERC-J, and POSSI plates. A galaxy catalogue well known to cosmologists was produced first. In 2007, two whole-sky catalogues of the northern and southern hemispheres are available. In France, MAMA is a high accuracy measuring machine at the Paris Observatory, which has been used for specific programmes rather than exhaustive coverage of sky surveys.

![](images/6560e9d09252c4beb04ae2cf9301a3e8909d690a045850fb52cc3d5a8260b0ad.jpg)  
Fig. 10.2 Focal plane of the MEGACAM camera, showing the array of 40 thinned $4 6 1 2 \times 2 0 4 8$ pixel CCDs made by EEV (UK). Source SApCEA

# Large CCD Sky Surveys

With the advent of CCD detectors (see Chap. 7) around 1980, the photographic plate was gradually superseded, although it was only during the 1990s that surveys could finally be produced with any real efficiency. It had to be possible to form very large area arrays of CCD detectors, developed specifically for this purpose. The whole area had to be sensitive without loss at edges, using rear face connections to keep the sides free, and highly accurate juxtaposition techniques had to be developed. A good example is the MEGACAM camera (see Fig. 10.2), developed by the astrophysics department of the French atomic energy authority (CEA). This simultaneously operates, at low temperatures, an array of $4 0 ~ \mathrm { C C D }$ detectors each with $4 6 1 2 \times 2 0 4 8$ pixels, manufactured by the British company EEV. This camera is set up at the primary focus of the CFH telescope (CFHT) (Hawaii) behind a dedicate focal reducer, comprising a sophisticated combination of very large lenses and a mobile image stabilisation component. An excellent image quality is achieved over almost the whole of the impressive field of view of $1 ^ { \circ } \times 1 ^ { \circ }$ .

Deep Wide-Field Photometric Surveys

These are used to probe regions exceeding the characterise size of the large scale structures in the Universe $( { \approx } 6 0 \ \mathrm { M p c } )$ , and their measurements are thus barely affected by cosmic variance. One classic use of these surveys is to measure the angular correlation function. They can also be used to select sub-samples of rare objects in the Universe.

As an illustration, let us consider the observational means and corresponding performance of deep wide-field surveys made with the CFH telescope in Hawaii:

• The first such survey, the Canada–France Deep Field (CFDF) survey, was carried out from 1996 to 1997 using the UH8K camera, an array of 8 CCDs with a field of view of 29 arcmin $\times$ 29 arcmin. This survey covered $1 \deg ^ { 2 }$ and included over 100 000 objects, down to the detection limit $I _ { A B } = 2 5 . 5$ . D The CFH12K camera, an array of $1 2 { \mathrm { ~ C C D s } }$ with a field of view of 42 arcmin $\times ~ 2 8$ arcmin, was then used to carry out the VIMOS VLT Deep Survey (VVDS) from 1999 to 2000, which covered $1 6 \mathrm { d e g ^ { 2 } }$ to a depth of $I _ { A B } = 2 4 . 8$ . D Since 2004, the MEGACAM camera has been producing a survey with an even wider field of view. The CFHT Legacy Survey (CFHT-LS) has taken five years and a half years. The aim is to image $1 7 0 \mathrm { d e g } ^ { 2 }$ of the sky (the Wide component) in 5 colours $( \mathbf { u } ^ { * } , \mathbf { g } ^ { \prime } , \mathbf { r } ^ { \prime } , \mathbf { i } ^ { \prime } , z ^ { \prime } )$ , up to magnitude $I _ { A B } = 2 5 . 5$ , and $4 ~ \mathrm { d e g } ^ { 2 }$ (the Deep component) up to magnitude $I _ { A B } = 2 8 . 3$ . CFHT-LS also D Dincludes a Very Wide component in the plane of the ecliptic to seek out trans-Neptunian objects.

Among the most important large sky surveys, we should mention the Sloan Digital Sky Survey (SDSS) carried out at the Apache Point Observatory in New Mexico (USA) since 1998. This CCD survey, which covers quarter of the northern sky around the galactic pole $( 1 0 0 0 0 ~ \mathrm { d e g ^ { 2 } } )$ and part of the galactic plane, includes 5 colours $( \mathrm { u } ^ { \prime } , \mathrm { g } ^ { \prime } , \mathrm { r } ^ { \prime } , \mathrm { i } ^ { \prime } , \mathrm { z } ^ { \prime } )$ using the filters of the US Naval Observatory (USNO) photometric system, and reaches magnitude 23 in $\mathbf { r } ^ { \prime }$ . A dedicated $2 . 5 \mathrm { ~ m ~ }$ telescope was designed to acquire $3 \times 3 ~ \mathrm { d e g } ^ { 2 }$ images, using a $5 \times 6$ array of $2 0 4 8 \times 2 0 4 8$   CCDs operating in continuous scanning mode. More than 40 Tbytes of data will be generated. A subset of around 1 Tbyte will include 1 million spectra, together with positions and mini images in each colour for more than 100 million objects.

# Ultra-Deep Field Photometric Surveys

The Hubble Space Telescope (HST) was equipped from 2002 with the Advanced Camera for Surveys (ACS), which could make images with a field of view of $2 0 2 \times 2 0 2$ arcsec2 and a pixel size of 0.049 arcsec. Before the failure that put it out of action at the beginning of 2007, it was indeed a remarkable tool for observing the faintest objects, by virtue of the unequalled resolution and contrast of its images. Two deep photometric surveys have been particularly spectacular, namely the Hubble Deep Field North and South (HDF-N and HDF-S). Objects were detected up to magnitudes $I _ { A B } = 2 7 . 6$ , although the field of view remained limited to $4 \times 4$ Darcmin2. Hence only 2 500 galaxies were observed over these two fields. The angular resolution of the images obtained with the HST was unique for studying the morphology of galaxies and spectral shifts $z > 1$ , until the advent around 2005 of the first near-infrared surveys using adaptive optics, which are in the process of changing this situation.

# Spectroscopic Sky Surveys

It is particularly in observational cosmology that the large spectroscopic surveys have been conceived as indispensable supplements to the large imaging surveys. This is because they provide a way to access the third dimension, i.e., distance, by measuring the spectral shift toward the red of light from receding galaxies.

Note that multicolour photometric surveys contain information that can be treated as a very low resolution spectrum, and can be used to estimate the distance to galaxies by examining photometric redshifts. To obtain sufficiently accurate measurements of $z$ , one must cover the broadest possible spectral region with a large number of narrow bandpass filters.

The COMBO-17 survey is a deep field survey with imaging over $0 . 7 8 \ \mathrm { d e g ^ { 2 } }$ , made using the Wide Field Imager (WFI) camera installed on the $2 . 2 \mathrm { m }$ MPG/ESO telescope at La Silla in Chile. Images are obtained in 17 optical bands, including 12 narrow filters, covering the spectral region 300– $9 0 0 \mathrm { n m }$ . The COMBO-17 sample contains 25 000 photometric spectral shifts.

Compared with the use of spectroscopic shifts, the measurement is less robust and less accurate. The error is estimated to be 10 times as great. For this reason, true spectroscopic surveys soon came to the fore.

Since it is not feasible to measure this shift efficiently galaxy by galaxy, even at the low spectral resolutions required, multi-object spectroscopic methods flourished. These fall into two main families: multi-slit spectrographs and optical fibre spectrographs in medusa mode (see Sect. 8.3).

In the nearby Universe $( z < 0 . 1 $ ), two large spectroscopic surveys have acquired a considerable amount of data since 2001:

• Two Degree Field Galaxy Redshift Survey (2dFGRS). This is an Anglo-Australian project, using the $3 . 9 \mathrm { ~ m ~ }$ telescope of the Anglo-Australian Observatory, with the Two Degree Field (2dF) multi-object spectrograph, where 400 optical fibres are automatically arranged by a robot to measure the target objects (see Chap. 8). These objects are selected automatically from digitised photographic plates of the APM Galaxy Survey. This survey covers $2 0 0 0 \ \mathrm { d e g } ^ { 2 }$ and contains at total of $2 3 0 0 0 0 z$ measurements on as many galaxies. Sloan Digital Sky Survey (SDSS). Apart from its camera (see above), the SDSS has a fibre-fed multi-object spectrograph able to acquire 640 spectra at the same time. The aim of this survey, in progress at the time of writing (2011), is to obtain the spectra of a million galaxies.

At redshifts $z$ higher than 0.3, there is still no spectroscopic sample of the size of the 2dFGRS and SDSS surveys. To illustrate the difficulty involved at high z, note that the flux observed from a galaxy at $z = 4$ is 6 000 times fainter than the flux from a similar galaxy located at $z ~ = ~ 0 . 1$ D. The compromise between the size of Dthe observed field of view, depth of observations, and fraction of objects targeted generally leads to a selection of sources established purely on the basis of a limiting apparent magnitude.

Surveys carried out between 1994 and 2000 were made using telescopes in the $4 \textrm { m }$ category and multi-object spectrographs with multiplex gain in the range 50–70. The broadest spectroscopic sample contains 2 000 galaxies with magnitudes $R < 2 1 . 5$ for the CNOC2 Galaxy Redshift Survey, which is 100 times less than the size of samples made in the near Universe. The Canada–France Redshift Survey (CFRS) made statistical analyses up to $z = 1 . 3$ , thanks to a selection of faint objects. DThe results established by CFRS are spectacular, but the sample contains fewer than 250 galaxies in each age range.

Telescopes in the $8 \textrm { m }$ category have made much deeper surveys. The K20 spectroscopic survey was carried out with the Very Large Telescope (VLT) in Chile, using the FORS1 and FORS2 spectrographs which have multiplex gains of 19 and 52, respectively. This survey measured the redshift $z$ of 550 objects. However, it was a combination of multi-object spectrographs (MOS) with very high multiplex gain and intensive use of $8 \textrm { m }$ telescopes which, in 2007, produced spectroscopic surveys containing several tens of thousands of galaxies with redshifts up to $z \approx 6$ .

Two such large, deep-field spectroscopic surveys are underway at the time of writing (2007), namely, DEEP2 and the VIMOS-VLT Deep Survey (VVDS). DEEP2 uses the DEIMOS spectrograph of the Keck II telescope. DEIMOS is a slit MOS, obtaining 75 spectra simultaneously with spectral resolution $R = 4 0 0 0$ . DEEP2 will measure the spectra of $6 5 0 0 0$ galaxies at $z > 0 . 7$ .

DThe VVDS project is based at the VLT and uses the VIsible Multi-Object Spectrograph (VIMOS). This spectrograph can observe up to 1 000 spectra simultaneously at low resolution $R = 2 0 0$ ). The aim is to acquire 150 000 galaxy redshifts up to $z = 6$ . The field of the VLT is D D30 arcmin, this being split into four subfields, each imaged spectrally through a slit mask and a grism on a CCD array. Each mask is a thin sheet of aluminium in which a high power laser has cut narrow slits. Simultaneous spectral analysis of 1 000 objects is possible with this instrument.

# 10.2.2 Infrared Sky Surveys

The first infrared survey worthy of the name was carried out from space. This was the almost complete coverage of the sky by the IRAS satellite (1983) in four bands, viz., 12, 25, 60, and $1 0 0 ~ { \mu \mathrm { m } }$ , with a resolution of about 1 arcmin. The sky was scanned continuously by placing the satellite on a polar orbit held perpendicular to the direction of the Sun, with the telescope pointing to the local vertical. The excellent sensitivity achieved here is due to the fact that the whole setup, including telescope and detectors, was cooled. Over the past 15 years, the quality of the final product has been greatly improved by three complete reprocessing operations.

Ground-based surveys in the near infrared only became feasible at the beginning of the 1990s, with the advent of detectors of appreciable size $( 2 5 6 \times 2 5 6$ pixels). The two main programmes of this kind were 2MASS and DENIS (see Table 10.1):

• $2 \ \mu \mathbf { m }$ All Sky Survey (2MASS). This is a whole-sky survey in the spectral bands J, H, and K of the near infrared, carried out using two purpose-built telescopes, one in each hemisphere. The limiting magnitudes were 17, 16.4, and 15.6, respectively.

• Deep Near Infrared Southern Sky Survey (DENIS). This is a European survey of the southern sky in the spectral bands I, J, and K, reaching limiting magnitudes of 18.5, 16.5, and 14, respectively. The survey was carried out between 1997 and 2003, using the general purpose $1 \textrm { m }$ telescope at the ESO in La Silla, Chile, which was allocated to this project on a full time basis. The survey is available in the form of images and a catalogue of point sources, supplemented by a specific catalogue for the Magellanic Clouds.

# 10.3 A Virtual Observatory

At the beginning of the twenty-first century, it became desirable to develop ways of exploiting this extraordinary wealth of survey data, so that all multiwavelength information about a region or object could be put together simultaneously in order to extract the maximum possible astrophysical value. This idea has now become a reality for any research scientist around the world. Thanks to a set of standardised tools, any scientist can obtain access to several of these databases through a computer terminal, superposing information in a uniform manner in the form of maps. This is the notion of virtual observatory, now a priority development in many countries and the subject of international coordination.

Hundreds of terabits $1 0 ^ { 1 2 }$ bits) of observation data, corresponding to several thousand billion pixels are generated by ground-based and spaceborne observatories, and at ever increasing rates. Of course, this information, stored in digital form in huge databases, is exploited by the scientists responsible for producing it, but often only to extract some rather narrow set of information, while the full content of these databases would allow others to find a wealth of other information, e.g., concerning other, previously ignored sources, nevertheless worthy of analysis in some different context. Making this data available to a wider community would certainly avoid the unnecessary duplication of costly observation nights. Observatories and space agencies have understood this simple fact and most offer this service today to the broader scientific community, providing free access to their archives after generally rather short periods of one or two years, during which exclusive access is maintained for those who made the observations.

There is now a clear desire to take a further step and provide the possibility of reconstructing the sky virtually, at all wavelengths. Online access to databases held in observatories around the world, in a user friendly format that can be directly exploited scientifically, will require the help of new information technologies and up-to-date research and analysis tools that are fast and simple to use. The aim of the European project Astrophysical Virtual Observatory (AVO), born in 2001, is precisely to provide scientific research with such tools. Supported by the European Commission, this project is piloted by the ESO with several European partners.

![](images/2f2e4ef1d83e943a9f64447869042857e769b7361c9fb1b3923bfb43624057c4.jpg)

![](images/1579dafd2bf8b25c8202359fd37699ea58eadc2ceec57d3262d654a075dec348.jpg)  
Fig. 10.3 Upper: Example of what is possible with the Aladin software at the CDS. Comparing images produced by large sky surveys, in this case, IRAS $1 0 0 \ \mu \mathrm { m }$ (left) and POSS visible (right), and superposing object identification and photometry from other catalogues (here 2MASS). Measurement values appear at the bottom. Lower: User interface for selecting image database or catalogue

The American counterpart of the AVO, also born in 2001, is the US National Virtual Observatory (NVO).4

Among those developing the AVO, two French institutes are playing an exemplary role. One is the Centre de donn´ees astronomiques de Strasbourg (CDS), run by the CNRS and the Louis Pasteur university, which specialises in archiving, and the other is the TERAPIX data centre (Traitement El´ementaire, Analyse et R´eduction des PIXels) based at the Institut d’Astrophysique de Paris, and run by the CNRS and the University of Paris 6, working upstream by processing the huge amounts of data from these large sky surveys in a fully automated way.

For many years now, the CDS has been a reference in the gathering, identification, and archiving of astronomical and bibliographical data. Its unique SIMBAD database can be accessed online. The CDS has also pioneered the notion of virtual observatory with the development of the ALADIN system, which can already be used to visualise and superpose images from the main large imaging sky surveys on a personal computer, identifying catalogued sources and supplying the corresponding photometric and astrometric data (see the example in Fig. 10.3).

The TERAPIX center was set up to exploit data provided by the MEGACAM (visible) and WIRCAM (infrared) CCD cameras operating at the focal point of the $3 . 6 \mathrm { ~ m ~ }$ Canada–France– Hawaii (CFH) telescope. It was in particular the very ambitious CFHT Legacy Survey which originally mobilised a significant fraction of the efforts at this centre. Since then, its missions have been extended and TERAPIX now processes data from other very large sky surveys.

# Appendix A Fourier Transforms

The reviews given in Appendices A and B are intended to help with the understanding of Chaps. 6, 7, and 9, and to introduce the notation used throughout the book. Although they have been written with a certain minimum of rigour, mathematical proof and systematic formalism were not the main aim. Examples have been chosen as close as possible to the themes of the book.

# A.1 Definitions and Properties

# A.1.1 Definitions

Given a function $f ( x )$ , where $x \in \mathbb { R }$ , the Fourier transform of $f ( x )$ is the function $\tilde { f } ( s )$ , where $s \in \mathbb { R }$ , and

$$
{ \tilde { f } } ( s ) = \int _ { - \infty } ^ { \infty } f ( x ) { \mathrm { e } } ^ { - 2 \mathrm { i } \pi s x } \mathrm { d } x ~ .
$$

The functions $f$ and $\tilde { f }$ are said to form a Fourier pair, and we sometimes write

$$
\tilde { f }  f \quad \mathrm { o r } \quad \tilde { f } = \mathrm { F T } [ f ] .
$$

The function $\tilde { f } ( s )$ exists if the function $f ( x )$ is bounded, integrable and has only a finite number of maxima, minima, and discontinuities. This does not necessarily imply that the transform of $\tilde { f }$ is $f$ . For the Fourier transformation to be reciprocal, i.e.,

$$
f ( x ) = \int _ { - \infty } ^ { \infty } \tilde { f } ( s ) \mathrm { e } ^ { 2 \mathrm { i } \pi s x } \mathrm { d } s ,
$$

it is sufficient that $f$ should be square-integrable, that is, that the integral

$$
\int _ { - \infty } ^ { \infty } | f ( x ) | ^ { 2 } \mathrm { d } x
$$

should exist. The definition of the FT can be extended to distributions. The FT of a distribution is not necessarily square-integrable.

The functions $f$ and $\tilde { f }$ may be either real or complex.

# Generalisation

It is possible to generalise the FT to several dimensions, if $f$ is defined on $\mathbb { R } ^ { n }$ (i.e., is a function of $n$ real variables). Let $r , w \in \mathbb { R } ^ { n }$ . Then

$$
\tilde { f } ( \boldsymbol { w } ) = \int _ { - \infty } ^ { \infty } f ( r ) \mathrm { e } ^ { - 2 \mathrm { i } \pi r \cdot \boldsymbol { w } } \mathrm { d } r \mathrm { ~ . ~ }
$$

# A Simple Interpretation

If $f ( t )$ is a function of time, $\tilde { f } ( s )$ represents its content of temporal frequencies. Similarly, if $f ( r )$ is defined on $\mathbb { R } ^ { 2 }$ , representing a two-dimensional space, the function $\tilde { f } ( \boldsymbol w )$ , where ${ \pmb w } \in \mathbb { R } ^ { 2 }$ , represents its content of spatial frequencies.

# A.1.2 Some Properties

Linearity

$$
\begin{array} { r c l } { { } } & { { } } & { { \mathrm { F T } \left[ a f \right] = a \mathrm { F T } \left[ f \right] , \quad a = \mathrm { c o n s t . } \in \mathbb { R } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \mathrm { F T } \left[ f + g \right] = \mathrm { F T } \left[ f \right] + \mathrm { F T } \left[ g \right] . } } \end{array}
$$

# Symmetry and Parity

Symmetry considerations are useful in the study of FTs. Let $P ( x )$ and $Q ( x )$ be the even and odd parts of $f ( x )$

$$
f ( x ) = P ( x ) + Q ( x ) .
$$

Then

$$
\tilde { f } ( s ) = 2 \int _ { 0 } ^ { \infty } P ( x ) \cos { ( 2 \pi x s ) } \mathrm { d } x - 2 \mathrm { i } \int _ { 0 } ^ { \infty } { Q ( x ) } \sin { ( 2 \pi x s ) } \mathrm { d } x \ .
$$

We also have the trivial relation

$$
\tilde { f } ( 0 ) = \int _ { - \infty } ^ { \infty } f ( x ) \mathrm { d } x \ ,
$$

Table A.1 Symmetry of Fourier pairs   

<table><tr><td>f(x)</td><td>f（s）</td></tr><tr><td>Real and even</td><td>Real and even</td></tr><tr><td>Real and odd</td><td>Imaginary and odd</td></tr><tr><td>Imaginary and even</td><td>Imaginary and even</td></tr><tr><td>Complex and even</td><td>Complex and even</td></tr><tr><td>Complex and odd</td><td>Imaginary and odd</td></tr><tr><td>Real,arbitrary</td><td>Real part even,imaginary part odd</td></tr><tr><td>Imaginary,arbitrary</td><td>Imaginarypart even,real part odd</td></tr></table>

![](images/1620660b43bba3f0e98a75a99daf2d142f76da842aaf0ecec344775fad97cf11.jpg)  
Fig. A.1 Representation of the Fourier Transform $\tilde { f } ( s )$ of an arbitrary real function $f ( x )$ , showing the real and imaginary parts

which says that the zeroth order moment corresponds to the zero frequency. This result leads to Table A.1. Figure A.1 gives a simple representation of the transform $\tilde { f } ( s )$ .

# Similarity

The similarity relation is written

$$
f ( a x )  { \frac { 1 } { | a | } } { \tilde { f } } ( { \frac { s } { a } } ) , \qquad a = { \mathrm { c o n s t a n t } } \in \mathbb { R } .
$$

The dilatation of a function causes a contraction of its transform. This easilyvisualised property is useful in understanding why the transform of a function with very compact support (i.e., which is non-zero on only a small region), has a very extended transform. In analysing temporal frequencies, we find that an impulse of short duration contains a very wide spectrum of frequencies, i.e., the shorter the impulse, the higher the frequencies its transform contains. This is the classic relation for the spectrum of a wave packet, according to which our knowledge of the properties of a signal cannot be arbitrarily precise simultaneously in both time and frequency.

# Translation

The translation of a function gives

$$
f ( x - a )  \mathrm { e } ^ { - 2 \mathrm { i } \pi a s } \ \tilde { f } ( s ) \ .
$$

A translation in one space is a phase rotation in the transform space.

# Derivative

It follows directly from the definition of a Fourier pair that

$$
\frac {  { \mathrm { d } } f ( x ) } {  { \mathrm { d } } x }  ( 2 \pi  { \mathrm { i } } s ) \tilde { f } ( s ) , \qquad \frac {  { \mathrm { d } } ^ { n } f ( x ) } {  { \mathrm { d } } x ^ { n } }  ( 2 \pi  { \mathrm { i } } s ) ^ { n } \tilde { f } ( s ) .
$$

# A.1.3 Important Special Cases in One Dimension

# Box Function

The box function, written $\varPi ( x )$ , is defined by

$$
\begin{array} { c } { { \pi ( x ) = 1 \quad \mathrm { f o r } \quad x \in \displaystyle \mathrm { \biggr ] } { - \frac { 1 } { 2 } } , + \frac { 1 } { 2 } \biggl [ \ , } } \\ { { \nonumber } } \\ { { \pi ( x ) = 0 \quad \mathrm { f o r } \quad x \in \displaystyle \mathrm { \biggr ] } { - \infty } , - \frac { 1 } { 2 } \biggl ] \ \mathrm { o r } \left[ \frac { 1 } { 2 } , + \infty \right[ \ , } } \end{array}
$$

and shown in Fig. A.2. We have likewise, for the box of width $a > 0$ ,

$$
\begin{array} { c c c } { { \displaystyle \pi \left( \frac { x } { a } \right) = 1 } } & { { \mathrm { f o r } } } & { { x \in \displaystyle \left] - \frac { a } { 2 } , + \frac { a } { 2 } \right[ , } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle \pi \left( \frac { x } { a } \right) = 0 } } & { { \mathrm { f o r } \quad x \in \displaystyle \left] - \infty , - \frac { a } { 2 } \right] \mathrm { o r } \left[ \frac { a } { 2 } , + \infty \right[ . } } \end{array}
$$

![](images/334a41cf5f7beb1b069a1798041274159035871711409c5a274acfa4d195dbb7.jpg)  
Fig. A.2 The box function and its Fourier transform

The FT of the box function $\varPi ( x )$ is written

$$
\mathrm { s i n c } s = \frac { \sin ( \pi s ) } { \pi s }  \pi ( x ) ~ ,
$$

and, using the similarity relation,

$$
\pi ( { \frac { x } { a } } )  | a | \operatorname { s i n c } ( a s ) ~ .
$$

# The Dirac Distribution

The Dirac distribution $\displaystyle \delta ( \boldsymbol { x } )$ , also known as the Dirac delta function, is not strictly speaking a function. It is defined by

$$
\delta ( x ) = \int _ { - \infty } ^ { \infty } { \mathrm { e } } ^ { 2 { \mathrm { i } } \pi s x } { \mathrm { d } } s .
$$

Its Fourier transform is thus 1 on the whole interval $\mathbf { \tau } ] - \infty , \infty [$ .

# The Dirac Comb

This distribution is constructed by periodic repetition of the Dirac distribution. It is written $\sqcup \left( x \right)$ , and sometimes called the Shah function (after the Cyrillic character ttwhich it resembles):

$$
\sqcup ( x ) = \sum _ { n = - \infty } ^ { + \infty } \delta ( x - n ) ~ .
$$

This distribution has the remarkable property of being identical to its FT, i.e.,

$$
\sqcup ( x )  \sqcup ( s ) .
$$

It is also called the sampling function, because of the following property, illustrated in Fig. A.3:

$$
\sqcup ( x ) f ( x ) = \sum _ { n = - \infty } ^ { + \infty } f ( n ) \delta ( x - n ) ~ .
$$

This may be intuitively understood as follows: starting from a continuous function $f ( x )$ , the operator reads a number (here infinite) of discrete values of $f ( x )$ , which we consider as being samples from $f ( x )$ . The term sample is understood here in a meaning close to the familiar one. (See also Appendix B and Sect. 9.1.)

This function can also be used as replication operator (Fig. A.3)

$$
\sqcup ( x ) \star f ( x ) = \sum _ { n = - \infty } ^ { + \infty } f ( x - n ) ~ ,
$$

where $\star$ denotes convolution (see below).


<!-- chunk 0010: pages 631-700 -->
![](images/18150b1995e22f0f802db9d3fea32780d26b1dad5719bff114c89880399a2620.jpg)  
Fig. A.3 (a) Sampling of a function $f ( x )$ by a Dirac comb. (b) Replication of a function $f ( x )$ by convolution with a Dirac comb

![](images/e175b40c5167026430381fa87aa8c0d1e27e10e7950915ecfc9c4b47100b2859.jpg)  
Fig. A.4 Fourier transforms of trigonometric functions (dashed arrows indicate imaginary quantities)

This distribution plays an important role in the study of signal sampling, for example, when digitising, but also in the study of periodic structures such as interferometer antennas, or the lines of diffraction gratings.

# Trigonometric Functions

As they are not square integrable, trigonometric functions do not have FTs in function space. The Fourier transforms nevertheless exist in the form of distributions (Fig. A.4).

![](images/9ce3f0d0f33826458fea249861069252c840415bade3cc33f1f2c5a6a39bf7d4.jpg)  
Fig. A.5 Fourier transform of the two-dimensional axisymmetric box function

$$
\begin{array} { r c l } { { } } & { { } } & { { \cos \pi x \Rightarrow \displaystyle \frac { 1 } { 2 } \left[ \delta \left( s + \displaystyle \frac { 1 } { 2 } \right) + \delta \left( s - \displaystyle \frac { 1 } { 2 } \right) \right] \quad \mathrm { s y m m e t r i c } \ , } } \\ { { } } & { { } } & { { \sin \pi x \equiv \displaystyle \frac { \mathrm { i } } { 2 } \left[ \delta \left( s + \displaystyle \frac { 1 } { 2 } \right) - \delta \left( s - \displaystyle \frac { 1 } { 2 } \right) \right] \quad \mathrm { a n t i s y m m e t r i c } \ . } } \end{array}
$$

# A.1.4 Important Special Cases in Two Dimensions

# Box Function in Two Dimensions

This function is defined (Fig. A.5) as a constant inside the unit circle and zero outside, with $r ^ { 2 } = x ^ { 2 } + y ^ { 2 }$ :

$$
\pi \left( { \frac { r } { 2 } } \right) = { \left\{ \begin{array} { l l } { 1 r < 1 } \\ { 0 r \geq 1 . } \end{array} \right. }
$$

The FT of this function can be written, with $w ^ { 2 } = u ^ { 2 } + \nu ^ { 2 }$ ,

$$
\pi ( { \frac { r } { 2 } } )  { \frac { J _ { 1 } ( 2 \pi w ) } { w } } ,
$$

where $J _ { 1 } ( x )$ is the Bessel function of order 1. The similarity relation implies

$$
\varPi \left( \frac { r } { 2 a } \right) \varepsilon \equiv a \frac { J _ { 1 } ( 2 \pi a w ) } { w } \ : , \quad a > 0 \ : .
$$

# Dirac Distribution in Two Dimensions

This distribution is defined by

$$
\delta ( x , y ) = \delta ( r ) = \iint _ { \mathrm { p l a n e } } \mathrm { e } ^ { 2 \mathrm { i } \pi r \cdot w } \mathrm { d } w \ ,
$$

and its FT takes the value 1 on the whole plane ${ \pmb w } \in \mathbb { R } ^ { 2 }$ .

# Two-dimensional Sampling Function

This distribution is constructed by repetition of the two-dimensional Dirac function in the plane:

$$
\sqcup ( x , y ) = \sum _ { m = - \infty } ^ { + \infty } \sum _ { n = - \infty } ^ { + \infty } \delta ( x - m , y - n ) .
$$

It is identical to its own Fourier transform

$$
\sqcup ( x , y )  \sqcup ( u , \nu ) .
$$

# Pairs of Frequently Used Fourier Transforms

Figures A.6 and A.7 show graphically some frequently used Fourier pairs in one and two dimensions, respectively.

Note in particular the one-dimensional Gauss function

$$
\mathrm { e } ^ { - \pi x ^ { 2 } }  \mathrm { e } ^ { - \pi s ^ { 2 } } ,
$$

and in two dimensions

$$
\mathrm { e } ^ { - \pi r ^ { 2 } } \gtrless \mathrm { e } ^ { - \pi w ^ { 2 } } ,
$$

which are preserved under Fourier transformation. The similarity relation leads to

$$
\exp [ - \pi ( { \frac { x } { a } } ) ^ { 2 } ]  | a | \exp [ - \pi ( a s ) ^ { 2 } ] ~ .
$$

# A.1.5 Important Theorems

# Convolution

The convolution of two functions (or distributions) is defined by the integral

$$
h ( x ) = f ( x ) \star g ( x ) = \int _ { - \infty } ^ { + \infty } f ( u ) g ( x - u ) \mathrm { d } u .
$$

The convolution can be considered as a linear transformation determined by $g ( x )$ and applied to $f ( x )$ . This transformation represents the behaviour of many physical systems which impose a linear operation on the input signal, represented by $f ( x )$ , and lead to the output signal $h ( x )$ (Fig. A.8).

![](images/71dde984faad43bba65e3fdd7f4100a6eb4999c6cfcded4195aa08396e1df919.jpg)  
Fig. A.6 Common Fourier pairs. From Bracewell R.N., The Fourier Transform and Its Applications, McGraw-Hill, New York, 1965. With the kind permission of the McGraw-Hill Book Co

![](images/dc81ff0244c547cc3670db2f359f8f4e31ce56d5aeec60aaa848ee9e124fc47c.jpg)  
Fig. A.7 Common Fourier pairs in two dimensions. From Bracewell R.N., The Fourier Transform and Its Applications, McGraw-Hill, New York, 1965. With the kind permission of the McGraw-Hill Book Co. Note that the FT of $\sin ( \pi y )$ takes purely imaginary values

![](images/dbc06b6618c276400c2ab282926d0e8ee6eadf371e56e9b54f187adc866e8b76.jpg)  
Fig. A.8 Convolution of two functions $f ( u )$ and $g ( u )$

The Fourier transform acts on convolutions in a remarkable way

$$
\begin{array} { c } { { f ( x )  \tilde { f } ( s ) , } } \\ { { } } \\ { { g ( x )  \tilde { g } ( s ) , } } \\ { { } } \\ { { h ( x ) = f ( x ) \star g ( x )  \tilde { f } ( s ) \tilde { g } ( s ) = \tilde { h } ( s ) . } } \end{array}
$$

The convolution of two functions (or distributions) is transformed into the pointwise product of their FTs. The convolution product is commutative, associative and distributive over addition. All results mentioned here extend to higher dimensions. For example,

$$
H ( \pmb { r } ) = F ( \pmb { r } ) \star G ( \pmb { r } ) = \iint F ( \pmb { \rho } ) G ( \pmb { r } - \pmb { \rho } ) \mathrm { d } \pmb { \rho } ,
$$

$$
\tilde { H } ( w ) = \tilde { F } ( w ) \tilde { G } ( w ) \ .
$$

# Correlation

The correlation product or cross- correlation of two real functions (or distributions) is defined by

$$
k ( x ) = \int _ { - \infty } ^ { + \infty } f ( u ) g ( u + x ) \mathrm { d } u ,
$$

and its interpretation is straightforward, with the help of Fig. A.9. Note that it differs from the convolution only by a change of sign in the argument of the second function. There is no universally accepted notation for the correlation product. We can write

$$
k = C _ { f g } \quad \mathrm { o r } \quad k = f \otimes g .
$$

![](images/23a5f0c5a898990f82b2c6600defe1ebe53e64f02f0dc3ae7f90fc75d104c7e5.jpg)  
Fig. A.9 The value of the correlation function $k ( x ) = f ( x ) \otimes g ( x )$ , calculated for a particular value of $x$ , is equal to the area shaded

If $f$ and $g$ are complex, the correlation product is defined by

$$
f \otimes g = \int _ { - \infty } ^ { + \infty } f ^ { * } ( u ) g ( u + x ) \mathrm { d } u ,
$$

where the asterisk denotes complex conjugation.

The autocorrelation of a function (or distribution) is given by

$$
k ( x ) = \int _ { - \infty } ^ { + \infty } f ( u ) f ( u + x ) \mathrm { d } u .
$$

# Parseval’s (Rayleigh’s) Theorem

This theorem says that a function and its FT have the same norm

$$
\int | f ( x ) | ^ { 2 } \mathrm { d } x = \int \left| \tilde { f } ( s ) \right| ^ { 2 } \mathrm { d } s = \int f f ^ { * } \mathrm { d } x \int \tilde { f } \tilde { f } ^ { * } \mathrm { d } s .
$$

Similarly, for two functions (or distributions),

$$
\int f g ^ { * } \mathrm { d } x = \int \tilde { f } \tilde { g } ^ { * } \mathrm { d } s .
$$

# Spectral Density

The spectral density, or power spectral density of the function $f ( x )$ is the quantity

$$
S _ { f } ( s ) = \left| \tilde { f } ( s ) \right| ^ { 2 } ,
$$

and $\tilde { f } ( s )$ is generally called the spectrum of $f ( x )$ . These terms are sometimes confused. In optics or spectroscopy, what is commonly called the spectrum is in fact a spectral density (see Chap. 5). The spectral density is also very commonly called the power spectrum.

Finally, we call the quantity

$$
\Big | \tilde { f } ( s ) \Big | = \Big \{ \Big [ \mathrm { R e } \tilde { f } ( s ) \Big ] ^ { 2 } + \Big [ \mathrm { I m } \tilde { f } ( s ) \Big ] ^ { 2 } \Big \} ^ { 1 / 2 }
$$

the amplitude spectrum, and the quantity

$$
\arg \tilde { f } ( s ) = \arctan \left( \frac { \mathrm { I m } \tilde { f } ( s ) } { \mathrm { R e } \tilde { f } ( s ) } \right)
$$

the phase spectrum. We collect these definitions together for convenience:

$$
\begin{array} { r l } & { \tilde { f } ( s ) \mathrm { s p e c t r u m ~ , } } \\ & { \left| { \tilde { f } } ( s ) \right| \mathrm { a m p l i t u d e s p e c t r u m ~ , } } \\ & { \arg { \tilde { f } } ( s ) \mathrm { p h a s e s p e c t r u m ~ , } } \\ & { \left| { \tilde { f } } ( s ) \right| ^ { 2 } \mathrm { s p e c t r a l d e n s i t y , ~ p o w e r ~ s p e c t r u m ~ . } } \end{array}
$$

# Autocorrelation (Wiener–Khinchine) Theorem

The Fourier transform of the autocorrelation of $f ( x )$ is the power spectrum of $f ( x )$

$$
\begin{array} { c c c } { { f ( x ) } } & { { } } & { { f ( x ) \otimes f ( x ) \nonumber } } \\ { { \downarrow \uparrow } } & { { } } & { { \downarrow \uparrow } } \\ { { \tilde { f } ( s ) } } & { { } } & { { \left| \tilde { f } ( s ) \right| ^ { 2 } } } \end{array}
$$

The power spectrum $| \tilde { f } ( s ) | ^ { 2 }$ is a real positive quantity. The phase information in the complex function $f ( x )$ j, which is contained in the real and imaginary parts of $\tilde { f } ( s )$ , is lost in the operation of autocorrelation.

# Cross-Power Spectrum and Cross-Correlation

If the functions (or distributions) $f ( x )$ and $g ( x )$ have FTs $\tilde { f } ( s )$ and $\tilde { g } ( s )$ , respec-Qtively, the cross-power spectrum or, better, the cross-spectral density, is defined by

$$
S _ { f g } ( s ) = \tilde { f } ( s ) \tilde { g } ^ { \ast } ( s ) ,
$$

so that $S _ { f g } ( s ) = S _ { g f } ^ { * } ( s )$ ; and the cross-correlation of $f$ and $g$ was defined above. DThen we find the relation

$$
S _ { g f } ( s )  C _ { f g } ( x ) .
$$

# A.2 Physical Quantities and Fourier Transforms

The FT proves to be invaluable for the representation of physical quantities. It can be used to isolate, in a complicated signal, simple (sinusoidal) components which are easy to handle, represent and interpret. However, it should be borne in mind that no information whatever is lost or gained when we go to the Fourier transform space.

Physical quantities, whether represented by functions or by distributions, are restricted in certain ways, and this allows us to develop some of the above ideas.

# Support of $f ( x )$

The Fourier transform of $f ( x )$ is defined if $f ( x )$ is defined on a support $] - \infty , + \infty [$ . 1 C1A physical quantity is generally only known on a bounded support. For example, a signal $f ( t )$ which is a function of time is only known on a finite time interval $[ - T / 2 , T / 2 ]$ . It is clearly possible to extend $f ( t )$ outside this interval by setting

$$
f ( t ) = 0 \quad \mathrm { f o r } \quad t \in ] - \infty , - \frac { T } { 2 } \bigg [ \quad \mathrm { o r } \quad ] \frac { T } { 2 } , + \infty [ \ .
$$

(This is an example of windowing.) Then we can calculate the FT and find the spectrum without ambiguity if $f ( t )$ is known at all points of the interval, or rather, if $f ( t )$ is known from an infinitely dense sampling. If on the other hand $f ( t )$ is unspecified outside the interval $[ - T / 2 , T / 2 ]$ , we can give no precise information about its spectrum without further assumptions (for example, concerning periodicity, or square-integrability, and the like). The method of windowing described here can be generalised. For example, the width $T$ of the window can be left undetermined, in the case of a function of time. This Fourier analysis on a variable and translatable window (adaptive Fourier analysis) is known as time–frequency analysis. A powerful tool is the Wigner–Ville representation.

# Negative Frequencies

The function $\tilde { f } ( s )$ is also defined on the support $] - \infty , + \infty [$ , and therefore refers to 1 C1negative frequencies. Is it possible to give some physical interpretation of negative frequencies? A physical quantity is real, and all we need to know its FT on the whole of $] - \infty , + \infty [$ are the values taken by the real and imaginary parts of the FT on $[ 0 , + \infty [$ C1, extending these symmetrically and antisymmetrically, respectively. C1The function ${ \ddot { f } } ( s )$ is then Hermitian (even real part, odd imaginary part). Its Fourier transform $f ( x )$ is real. Suppose we wish to carry out a numerical filtering on $f ( x )$ , which amounts to multiplying its FT by a certain function $\tilde { h } ( s )$ . We carry out the operation of pointwise multiplication of $\tilde { f } ( s )$ and $\tilde { h } ( s )$ on the whole support $] - \infty , + \infty [$ , before taking the inverse FT. This is shown in the following diagram.

$f ( x ) \mathop { \mathrm { r e a l } } _ { \downarrow }$ !FT $\begin{array} { l } { { \widetilde { f } ( s ) \ \mathrm { c a l c u l a t e d \ o n \ [ 0 , \infty ] } } } \\ { { \downarrow } } \\ { { \widetilde { f } ( s ) \quad \mathrm { c o m p l e t e d } } } \\ { { \mathrm { o n \ [ 0 , - \infty ] } } } \\ { { \downarrow } } \\ { { \widetilde { f } ( s ) \widetilde { h } ( s ) } } \end{array}$   
#Filtering operation   
.i:e:; convolution/   
$f ( x ) \star h ( x )$ FT

# Power of a Signal

Let $f ( x )$ be some signal, which may be complex; for example, a complex electric field whose amplitude and phase are functions of time.

We define the instantaneous power of the signal as

$$
p ( x ) = f ( x ) f ^ { * } ( x ) .
$$

When the variable $x$ is time and $f$ is a current or a voltage, this definition agrees with the normal usage.

The average power over an interval $X$ centred on $x _ { 0 }$ is defined as

$$
P ( x _ { 0 } , X ) = { \frac { 1 } { X } } \int _ { x _ { 0 } - X / 2 } ^ { x _ { 0 } + X / 2 } f ( x ) f ^ { * } ( x ) \mathrm { d } x \ .
$$

The integral of the instantaneous power is the energy associated with the signal

$$
\int _ { - \infty } ^ { + \infty } p ( x ) \mathrm { d } x ~ .
$$

If the signal is zero outside the interval $X$ , the integral generally converges without problems. If this is not the case, the signal may have an infinite energy, although its average power is finite. For example, the signal

$$
f ( x ) = \cos ( 2 \pi x )
$$

has average power

$$
\langle P \rangle = { \frac { 1 } { 2 } } ,
$$

although its energy is infinite.

The average power of a signal with support $[ - \infty , + \infty ]$ is defined by the limit

$$
\left. P \right. = \operatorname* { l i m } _ { X \to \infty } \frac { 1 } { X } \int _ { - X / 2 } ^ { + X / 2 } f ( x ) f ^ { * } ( x ) \mathrm { d } x \ ,
$$

if it exists.

Although the terms energy and power only agree with their usual physical meanings for signals which are functions of time, they are universally used in the senses defined above.

# Power Spectrum of a Signal

Finite Energy Signal

If $f ( x )$ is a signal, we can calculate $\tilde { f } ( s )$ , and the quantity

$$
S _ { f } ( s ) = \tilde { f } ( s ) \tilde { f } ^ { \ast } ( s ) = \left| \tilde { f } ( s ) \right| ^ { 2 } ,
$$

already defined as the spectral density of $f ( x )$ is also called the power spectrum of $f ( x ) . S _ { f } ( s )$ has the dimensions of energy per frequency interval (spectral energy density) and not a power. The designation as the power spectrum or power spectral density (PSD) is nevertheless standard.

The total energy of the signal is clearly

$$
\int _ { - \infty } ^ { + \infty } S _ { f } ( s ) \mathrm { d } s ~ ,
$$

if the integral exists.

Infinite Energy Signal

In this case, $\tilde { f } ( s )$ cannot be calculated. Nevertheless, the autocorrelation function of $f ( x )$ may exist, given by

$$
C _ { f f } ( x ) = \operatorname* { l i m } _ { X \to \infty } \frac { 1 } { X } \int _ { - X / 2 } ^ { + X / 2 } f ( u ) f ( x + u ) \mathrm { d } u ,
$$

and the Wiener–Khinchine theorem gives the spectral density of the signal $f ( x )$

$$
{ \cal S } _ { f } ( s ) = \mathrm { F T } \left[ C _ { f f } ( x ) \right] .
$$

Here $S _ { f } ( s )$ is an energy, or a power per frequency interval, which is consistent with previous definitions and makes it appropriate to use the term power spectral density. For example, if we consider a signal in the form of a voltage $\nu ( t )$ , the PSD is measured in $\mathrm { V } ^ { 2 } \mathrm { H z } ^ { - 1 }$ , and the amplitude spectrum in $\mathrm { V H z } ^ { - 1 / 2 }$ .

# Cross-Spectral Density and Cross-Correlation

The definitions and remarks above apply equally to the combination of two functions $f ( x )$ and $g ( x )$ .

For example, in the case of a signal of finite energy, the cross-spectral density is written

$$
S _ { f g } ( s ) = \tilde { f } ( s ) \tilde { g } ^ { \ast } ( s ) ,
$$

and the cross-correlation is

$$
C _ { f g } ( x ) = \int _ { - \infty } ^ { + \infty } f ( u ) g ( u + x ) \mathrm { d } u .
$$

If the energies are infinite, the cross-correlation is the limit

$$
C _ { f g } ( x ) = \operatorname * { l i m } _ { X \to \infty } \frac { 1 } { X } \int _ { - X / 2 } ^ { + X / 2 } f ( u ) g ( u + x ) \mathrm { d } u \ ,
$$

if it exists, and the cross-spectral density is defined by

$$
S _ { f g } ( s ) = \mathrm { F T } \left[ C _ { f g } ( x ) \right] .
$$

# A.3 Wavelets

By Fourier analysis, a signal can be decomposed into periodic functions of infinite support. This is a global transformation which is well-suited to signals with little or no evolution in time, the main example being stationary or quasi-stationary signals. Nevertheless, a physical signal is always defined on a bounded support, its emission being locally defined in time. The most important information is often contained in its non-stationarity (its beginning and end). The same comment could be made about an image bounded in space, or other types of signal, as well as the time signals referred to above. A partial solution is provided by the windowing technique mentioned earlier, which replaces a definition on an infinite support by a definition of the signal including a minimum number of significant coefficients. In a word, it compresses the signal in the most efficient way possible.

Two methods have been specifically developed to represent and analyse this type of signal. They are relevant here, because they are more and more frequently used in astronomy, to process data as varied as observed spectra, images, temporally variable emissions such as solar flares and periodic bursts of a pulsar, and many others. In these methods the time variable can, of course, be replaced by a space coordinate, or several (the two coordinates of an image), or indeed any other variable, such as the wavelength of a spectrum.

The time–frequency representation takes into account the time development of the frequency content of a signal. It gives the instantaneous frequency of the signal and the time dependence of this instantaneous frequency.

The wavelet transform, or time–scale representation, describes the development of a signal relative to some observation scale. Wavelets are oscillating functions, localised in time, unlike the sinusoidal functions of the Fourier transform. They all have the same shape, differing only in the instant of their appearance and in their duration. Wavelets of short duration and small amplitude thus represent very localised components of the signal, which would be missed upon a larger scale examination.

These two methods are particularly useful for classification and morphological analysis, which are all-important in astronomy. A signal (for example, the image of a type of galaxy) will thus have a unique signature on the wavelet transform of the image of a cluster. The relevant information is concentrated, in such a way that, in the Fourier transform, a particular frequency, drowned out by the rest of the signal, will stand out as a spike in its spectrum.

# Appendix B Random Processes and Variables

Noise phenomena, due to the fluctuations of a thermodynamic system or the quantum nature of interactions, impose a practical and theoretical limit on any measurement. Some basic mathematical notions are useful, given the importance of this subject in the book (but see the note at the beginning of Appendix A).

# B.1 Random Variables

# Definition of a Random Variable (r.v.)

Consider a process (for example, dice-throwing or absorption of a photon by the photoelectric effect), which has a number of possible outcomes $\zeta$ . A pre-assigned rule associates a quantity $\mathbf { x } ( \zeta )$ with each outcome. (The r.v. is denoted $\mathbf { X }$ , not to be confused with the notation for a vector $\boldsymbol { x }$ . The difference should be clear from the context. Naturally, a vector can also be a random variable, but we shall not introduce any specific notation to cover this case.) $\mathbf { x } ( \zeta )$ is called a random variable of probability $P ( \zeta )$ , where $P ( \zeta )$ is the probability of getting the result $\zeta$ (Fig. B.1).

We denote by $\{ \mathbf { x } \leq x \}$ the set of outcomes for which the random variable $\mathbf { X }$ has f 
 ga value no larger than a number $x$ . This set may be empty, or contain just one, or several, or all the outcomes, and each of these cases is called an event. Each event, in turn, has a probability associated with it, so that probability becomes a positive definite function on the set of events, satisfying certain rules to be stated below.

A real random variable is defined when the set $\{ \mathbf { x } \leq x \}$ is an event for any real number $x$ f 
 g. It is also required that the probabilities of the events $\{ { \bf x } = - \infty \}$ and $\{ { \bf x } = + \infty \}$ should be zero.

D C1gA complex random variable is defined by a process which associates with each outcome $\zeta$ a complex number

$$
{ \bf z } ( \zeta ) = { \bf x } ( \zeta ) + \mathrm { i } { \bf y } ( \zeta ) ,
$$

![](images/3b8d14aca7850afb4a1775b0d93cd1709e2f196e5b04ca262f0ab4402b727330.jpg)  
Fig. B.1 An experiment $\varepsilon$ formed by the set of outcomes $\zeta$ (here discrete), with each of which is associated the value $\mathbf { x } ( \zeta )$ of the r.v. x

in such a way that the functions $\mathbf { X }$ and $\mathbf { y }$ are themselves real random variables. Unless otherwise stated, all random variables in the following are real.

# Distribution Function

Given a real number $x$ , the set $\{ \mathbf { x } \leq x \}$ of all outcomes $\zeta$ such that $\mathbf { x } ( \zeta ) \le x$ , is an event. The probability $P \{ \mathbf { x } \leq x \}$ gof this event is a number depending on $x$ , and therefore a function of $x$ f 
 g, which we denote by $F _ { \mathbf { x } } ( x )$ , or simply $F ( x )$ if there is no risk of ambiguity regarding the r.v. it refers to. Hence,

$$
F _ { \bf x } ( x ) = P { \bf \{ x \leq }  x  \bf \} .
$$

This is called the distribution function (not to be confused with distributions) of the r.v. x. It has the following properties:

$$
F ( - \infty ) = 0 , \qquad F ( + \infty ) = 1 ,
$$

it is a non-decreasing function of $x$ , i.e.,

$$
F ( x _ { 1 } ) \leq F ( x _ { 2 } ) \qquad { \mathrm { f o r } } \ x _ { 1 } < x _ { 2 } \ ,
$$

and $F ( x )$ is right continuous, i.e.,

$$
F ( x ^ { + } ) = F ( x ) .
$$

# Probability Density

The derivative of the distribution function, in the sense of distributions,

$$
f _ { \mathbf { x } } ( x ) = \frac { \mathrm { d } F _ { \mathbf { x } } ( x ) } { \mathrm { d } x }
$$

is called the density (or density function, or sometimes frequency) of the r.v. x. (The theory of distributions makes differentiation possible even when the function is not continuous. The derivative is then not a function, but a distribution.)

If $F ( x )$ is continuous and differentiable everywhere except at a countable number of values of $x$ , the r.v. is said to be continuous. Attributing arbitrary positive values

![](images/60a54d685d9645af8c89243b935536024f22b41f99d44d0c5d151d13890550f4.jpg)  
Fig. B.2 Probability density function $f ( x )$ and corresponding Poisson . $( a = 3$ / distribution Dfunction $F ( x )$

to $f ( x )$ at the set of values of $x$ (of measure zero) at which $F$ is not differentiable, we can treat $f ( x )$ as a function defined for all $x$ .

If there are a discrete number of outcomes, $F ( x )$ has a staircase appearance, as shown in Fig. B.2. The density is then

$$
f ( x ) = \sum _ { i } p _ { i } \delta ( x - x _ { i } ) \ ,
$$

a succession of Dirac distributions of amplitude $p _ { i }$ , where $p _ { i }$ is the probability of outcome $i$ . We obtain

$$
\frac { \mathrm { d } F ( x ) } { \mathrm { d } x } \bigg | _ { x = x _ { i } } = \big [ F ( x _ { i } ) - F ( x _ { i } ^ { - } ) \big ] \delta ( x - x _ { i } ) .
$$

The probability density is normalised to unity:

$$
\int _ { - \infty } ^ { + \infty } f ( x ) \mathrm { d } x = F ( + \infty ) = 1 .
$$

# Expectation Values

The expectation of any function $\phi$ of the continuous r.v. $\mathbf { X }$ of density $f$ is written

$$
E \{ \phi ( x ) \} = \int _ { - \infty } ^ { + \infty } \phi ( x ) f ( x ) \mathrm { d } x \mathrm { ~ . ~ }
$$

Similarly, if $\mathbf { X }$ is a discrete r.v., taking values $x _ { n }$ with probabilities $p _ { n }$ , then

$$
E \{ \phi ( x ) \} = \sum _ { n } \phi ( x _ { n } ) P _ { n } \ .
$$

In physics, the expectation value of $\phi$ is called the ensemble average and denoted $\langle \phi \rangle$ .

h iBesides having other useful properties, the expectation value is the moment generating operator for the probability measure.

# Moments

Any probability measure is completely described by either its distribution function or its density function, but these both contain more information than we can easily apprehend. A small number of global parameters, called the moments of the distribution, already provide the essential content of the model.

For any whole positive number $k$ , the moment of order $k$ of the r.v. $\mathbf { X }$ is defined by $\mu _ { k } ^ { \prime } = E \{ \mathbf { x } ^ { k } \}$ , and the central moment of order $k$ by $\mu _ { k } = E \{ ( { \bf x } - E \{ { \bf x } \} ) ^ { k } \}$ .

D f gWe always have $\mu _ { 0 } ~ = ~ 1$ D f  f g g. Knowing all the moments (an infinite number) of a Ddistribution function amounts to knowing the distribution function $F ( x )$ .

Mean

The mean value of a continuous random variable $\mathbf { X }$ is

$$
\eta = E \{ \mathbf { x } \} = \int _ { - \infty } ^ { + \infty } x f ( x ) \mathrm { d } x \ ,
$$

where $f ( x )$ is the density of the variable. If $\mathbf { X }$ is a discrete random variable, taking the values $x _ { n }$ with probability $p _ { n }$ , then

$$
E \{ \mathbf { x } \} = \sum _ { n } x _ { n } p _ { n } \mathrm { ~ . ~ }
$$

The quantity $\eta$ gives information about how the density $f ( x )$ is centred. We can also define the most probable value of $x$ , which is that value $x _ { 1 }$ such that $f ( x _ { 1 } )$ is a maximum.

The median of $\mathbf { X }$ is that value $x _ { \mathrm { m } }$ such that

$$
P \{ \mathbf { x } \leq x _ { \mathrm { m } } \} = F ( x _ { \mathrm { m } } ) = 1 / 2 .
$$

Variance

The variance or dispersion is defined as the central moment of order two

$$
\mu _ { 2 } = E \left\{ ( \mathbf { x } - \boldsymbol { \eta } ) ^ { 2 } \right\} = \int _ { - \infty } ^ { + \infty } ( x - \boldsymbol { \eta } ) ^ { 2 } f ( x ) \mathrm { d } x \mathrm { ~ . ~ }
$$

This quantity, usually denoted $\sigma ^ { 2 }$ , describes how the r.v. is concentrated about its mean $\eta$ . Its positive square root is called the standard deviation or root mean square deviation (rms). It follows that

$$
\sigma ^ { 2 } = E \left\{ { \bf x } ^ { 2 } - 2 { \bf x } \eta + \eta ^ { 2 } \right\} = E \left\{ { \bf x } ^ { 2 } \right\} - 2 \eta E \left\{ { \bf x } \right\} + \eta ^ { 2 } = E \left\{ { \bf x } ^ { 2 } \right\} - \eta ^ { 2 } ,
$$

which gives the important relation

$$
\sigma ^ { 2 } = E \left\{ { \bf x } ^ { 2 } \right\} - ( E \left\{ { \bf x } \right\} ) ^ { 2 } .
$$

# Characteristic Function

The characteristic function $\varPhi ( \omega )$ of a random variable $\mathbf { X }$ is the expectation value of the new random variable exp i!x defined in terms of $\mathbf { X }$ . Hence

$$
\phi ( \omega ) = E \left\{ \exp \mathrm { i } \omega \mathbf { x } \right\} = \int _ { - \infty } ^ { + \infty } \mathrm { e } ^ { \mathrm { i } \omega x } f ( x ) \mathrm { d } x \mathrm { ~ . ~ }
$$

This is just the Fourier transform of $f ( x )$

$$
\Phi ( \omega )  f ( x ) .
$$

Similarly, if $\mathbf { X }$ is a discrete random variable

$$
\phi ( \omega ) = \sum _ { k } \mathrm { e } ^ { \mathrm { i } \omega x _ { k } } P \left\{ { \bf x } = x _ { k } \right\} .
$$

# Some Important Random Variables

It can be shown that, given a function $G ( x )$ such that

$$
\begin{array} { c l c r } { { G ( - \infty ) = 0 \ , } } & { { G ( + \infty ) = 1 \ , } } & { { \displaystyle \operatorname* { l i m } _ { x  \infty } G ( x ) = 1 \ , } } \\ { { } } & { { } } & { { } } \\ { { G ( x _ { 1 } ) \leq G ( x _ { 2 } ) \quad \mathrm { i f } \quad x _ { 1 } < x _ { 2 } \ , } } \\ { { } } & { { } } & { { } } \\ { { G ( x ^ { + } ) = G ( x ) \ , } } & { { } } \end{array}
$$

there exists a random process and a random variable defined on it with distribution function $G ( x )$ .

The functions $G ( x )$ below thus define random variables. Indeed, they provide a good approximation to the random behaviour of certain physical quantities.

Normal or Gaussian Distribution

The probability density of the normal distribution is given by

$$
f ( x ) = \frac { 1 } { \sigma \sqrt { 2 \pi } } \exp \left[ - \frac { ( x - \eta ) ^ { 2 } } { 2 \sigma ^ { 2 } } \right] = N \left( x ; \eta , \sigma ^ { 2 } \right) .
$$

The distribution has two parameters: $\eta$ (position) and $\sigma$ (scale).

The corresponding distribution function is

$$
F ( x ) = \int _ { - \infty } ^ { x } f ( u ) \mathrm { d } u = 0 . 5 + \mathrm { e r f } \left( \frac { x - \eta } { \sigma } \right) ,
$$

where $\operatorname { e r f } ( x )$ denotes the error function, which can be found in tables of functions or programmed.

The parameter $\eta$ is the mean and $\sigma ^ { 2 }$ is the variance of the distribution. The odd moments about the mean are zero, and the even moments about the mean are given by

$$
\mu _ { 2 r } = \frac { ( 2 r ) ! } { 2 ^ { r } r ! } \sigma ^ { 2 r } .
$$

The two parameters $\eta$ and $\sigma$ completely specify the normal distribution. The width half way up to the peak, called the full width at half maximum or FWHM, is given by

$$
\mathrm { F W H M } = 2 \sigma \sqrt { 2 \ln 2 } \approx 2 . 3 5 4 8 \sigma .
$$

The r.v. $\mathbf { y } = ( \mathbf { x } - \eta ) / \sigma$ is a normally distributed r.v. with mean zero and variance D one. It is called the reduced normal r.v.

We shall see later that a great number of physical phenomena lead to quantities which are distributed normally. It is useful to be able to give the interval $[ - Q , + Q ]$ such that the reduced r.v. should lie with probability almost 1 in that interval:

$$
P \left\{ \left| { \frac { \mathbf { x } - \eta } { \sigma } } \right| < Q \right\} = 1 - \alpha .
$$

The parameter $Q$ determines the $( 1 - \alpha )$ confidence interval. Table B.1 gives the values of $Q$ for various values of $\alpha$ .

We deduce that a r.v. distributed as $N ( x ; \eta , \sigma )$ has probability $9 9 . 7 \%$ of lying in the interval $[ \eta - 3 \sigma , \eta + 3 \sigma ]$ Iduring a trial. The $9 9 . 7 \%$ confidence level thus  Ccorresponds to the three sigma rule.

Table B.1 Confidence intervals for the normal distribution   

<table><tr><td>(1-α)[%]</td><td>50.0</td><td>68.3</td><td>90.0</td><td>95.0</td><td>95.4</td><td>99.0</td><td>99.7</td><td>99.9</td></tr><tr><td>Q</td><td>0.6745</td><td>1</td><td>1.64</td><td>1.96</td><td>2</td><td>2.5758</td><td>3</td><td>3.2905</td></tr></table>

Poisson Distribution

The Poisson distribution gives the probability of finding $k$ events in a certain interval (an interval of time, or more generally, a range), when the events are independent of each other, unlimited in number, and occur at a constant rate in time or with a constant spacing over the range (space, for example). The probabilities of the various values of the discrete r.v. $\mathbf { X }$ , which lie in $\{ 0 , 1 , 2 , 3 , . . . \}$ , are given by

$$
P \{ { \bf x } = k \} = { \mathrm e } ^ { - a } \frac { a ^ { k } } { k ! } .
$$

The single parameter $a$ is called the parameter of the distribution. The probability density is given by

$$
f ( x ) = \mathrm { e } ^ { - a } \sum _ { 0 } ^ { \infty } { \frac { a ^ { k } } { k ! } } \delta ( x - k ) \ ,
$$

an infinite series of Dirac distributions. The mean and variance of the Poisson distribution are both equal to $a$ .

$\chi ^ { 2 }$ Distribution

A random variable has a $\chi ^ { 2 }$ distribution if its probability density is

$$
f ( x ) = \left\{ \begin{array} { l l } { \displaystyle { \frac { 1 } { 2 T ( n / 2 ) } } \left( \frac { x } { 2 } \right) ^ { n / 2 - 1 } \mathrm { e } ^ { - 1 / 2 } \mathrm { f o r } x > 0 \ : , \medskip } \\ { 0 \quad \quad \quad \quad \quad \quad \quad \mathrm { f o r } x < 0 \ : . } \end{array} \right.
$$

There is only one parameter, $n$ , which is strictly positive and called the degree of freedom. Note that if $n = 3$ , we obtain the Maxwell distribution in the kinetic theory of gases. The $\varGamma$ Dfunction is tabulated and programmable. The mean and variance of the r.v. are $n$ and $2 n$ , respectively.

The main feature of the $\chi ^ { 2 }$ distribution is as follows: if $\{ \mathbf { x } _ { i } , i = 1 , 2 , \ldots , n \}$ are $n$ f D gindependent random variables with the reduced normal distribution, then the r.v. $\chi$ defined by

$$
\chi ^ { 2 } = \sum _ { i = 1 } ^ { n } \mathbf { x } _ { i } ^ { 2 }
$$

has a $\chi ^ { 2 }$ distribution with $n$ degrees of freedom.

# Central Limit Theorem

Let $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \mathbf { x } _ { 3 } , \ldots , \mathbf { x } _ { n }$ be a sequence of independent random variables with the same density $f _ { \mathbf { x } } ( x )$ , with mean $\eta$ and variance $\sigma ^ { 2 }$ . it can be shown that their arithmetic mean

$$
{ \overline { { \mathbf { x } } } } = { \frac { 1 } { n } } \sum _ { 1 } ^ { n } \mathbf { x } _ { i }
$$

has mean $\mu$ and variance $\sigma ^ { 2 } / n$ . It thus tends to $\mu$ when $n$ tends to infinity (law of large numbers). Furthermore, the central limit theorem (from a German term meaning that it is of central importance in probability theory) states that this variable behaves in the limit as a normal r.v. with mean $\mu$ and variance $\sigma ^ { 2 } / n$ . This result barely depends on the precise nature of the density $f$ . It is only required to have a well-defined mean and variance. There are less restrictive versions of these conclusions, e.g., when the distributions of the $\mathbf { X } _ { i }$ are different but all have a welldefined mean $\mu _ { i }$ and variance $\sigma _ { i } ^ { 2 }$ . The variable $\overline { { \mathbf { X } } }$ then behaves as a normal r.v. with mean $\eta$ and variance $\sigma ^ { 2 }$ given by

$$
\eta = \frac { 1 } { n } \sum \eta _ { i } \quad \mathrm { a n d } \quad \sigma ^ { 2 } = \frac { 1 } { n ^ { 2 } } \sum \sigma _ { i } ^ { 2 } .
$$

As $n \to \infty$ , the density $f _ { \overline { { \mathbf { x } } } } ( x )$ of $\overline { { \mathbf { X } } }$ tends to the normal distribution

$$
f ( x ) = \frac { 1 } { \sigma \sqrt { 2 \pi } } \exp \left[ - \frac { ( x - \eta ) ^ { 2 } } { 2 \sigma ^ { 2 } } \right] .
$$

An intuitive idea of the proof of the theorem is obtained by noting that the density $f _ { \overline { { \mathbf { x } } } } ( x )$ is the $n$ -fold convolution

$$
f _ { \overline { { \mathbf { x } } } } ( x ) = f _ { 1 } ( x ) \star f _ { 2 } ( x ) \star \cdot \cdot \star f _ { n } ( x ) ~ .
$$

But the convolution of an increasing number of positive functions, each of which tends to zero at $\pm \infty$ , tends to a Gaussian. This is easy to visualise for an $n$ -fold ˙1convolution of box functions $\varPi ( x )$ .

The central limit theorem is very useful in physics, where the statistical behaviour of a system often results from the accumulation of a large number of independent effects.

# B.2 Random or Stochastic Processes

# Definition

Consider an experiment having a set of possible outcomes $\zeta$ , where $P ( \zeta )$ is the probability. A real or complex function of time $t$ denoted by $\mathbf { x } ( t , \zeta )$ is assigned to each outcome. The family of functions thus created is called a stochastic process (abbreviated to s.p. in the following). $\zeta$ belongs to the set of outcomes of the experiment, and $t$ is a real number in $\mathrm { \Phi } ] - \infty , + \infty [$ . The notation $\mathbf { x } ( t )$ will be used to represent the process. This notation can be considered as representing four different aspects of the process:

(a) A family of functions depending on time (indexed by $\zeta$ ).   
(b) A particular function of time ( $\zeta$ being fixed).   
(c) A random variable (at fixed $t$ , for a set of trial outcomes $\zeta$ ).   
(d) A number (at fixed $t$ , and for fixed $\zeta$ ).

Aspect (c) is clearly a necessary condition if we hope to speak of a random process. The following three examples should motivate these definitions:

• The experiment consists in choosing a molecule of a gas and the quantity $\mathbf { x } ( t )$ is the component of its velocity along a given axis. This component varies in time. • The experiment consists in choosing an oscillator from the production line. The output voltage of the oscillator can be written

$$
{ \bf x } ( t , \zeta ) = { \bf a } ( \zeta ) \sin \omega _ { \zeta } t \ ,
$$

where amplitude and frequency depend on the oscillator. The sequence of output voltages is a stochastic process. Note that in this case the function ${ \bf x } ( t )$ is completely determined for any given outcome, i.e., for any choice of oscillator.

• The experiment consists in throwing a die, and

$$
\begin{array} { r } { { \mathbf x } ( t ) = \left\{ \begin{array} { l l } { \sin t \quad \quad \quad \mathrm { f o r h e a d s } , } \\ { { \mathbf x } ( t ) = 2 t \quad \quad \quad \mathrm { f o r t a i l s } . } \end{array} \right. } \end{array}
$$

The function representing $\mathbf { x } ( t )$ is random, but completely specified after each throw.

Figure B.3 illustrates the various ways of thinking about random processes. $\mathbf { x } ( t )$ is assumed to be real.

![](images/44fe72ad53a193237390f9e5f45bba7a1c16694a8941e012d44209594c473aa7.jpg)  
Fig. B.3 Different representations of a continuous stochastic process $\mathbf { x } ( t )$ . (a) $\mathbf { x } ( t , \zeta )$ is a random function of $t$ . (b) $\mathbf { x } ( t , \zeta )$ is a determinate function of $t$

# Distribution Function

The first order distribution function of the stochastic process ${ \bf x } ( t )$ is

$$
F ( x ; t ) = P \{ { \bf x } ( t ) \leq x \} ,
$$

the probability of the event $\{ \mathbf { x } ( t ) \leq x \}$ , consisting of all the outcomes $\zeta$ such that, at time $t$ , the functions $\mathbf { x } ( t , \zeta )$ gdo not exceed the value $x$ .

The corresponding density function is

$$
f ( x , t ) = \frac { \partial F ( x ; t ) } { \partial x } .
$$

The second order distribution function of the stochastic process ${ \bf x } ( t )$ is defined as follows. For two times $t _ { 1 }$ and $t _ { 2 }$ , the two r.v.s $\mathbf { x } ( t _ { 1 } )$ and ${ \bf x } ( t _ { 2 } )$ are used to write

$$
F ( x _ { 1 } , x _ { 2 } ; t _ { 1 } , t _ { 2 } ) = P \left\{ \mathbf { x } ( t _ { 1 } ) \leq x _ { 1 } , \mathbf { x } ( t _ { 2 } ) \leq x _ { 2 } \right\} .
$$

The corresponding density function is

$$
f ( x _ { 1 } , x _ { 2 } ; t _ { 1 } , t _ { 2 } ) = \frac { \partial ^ { 2 } F ( x _ { 1 } , x _ { 2 } ; t _ { 1 } , t _ { 2 } ) } { \partial x _ { 1 } \partial x _ { 2 } } .
$$

# Mean of a Stochastic Process

The mean of a stochastic process is the expectation value

$$
\eta ( t ) = E \{ \mathbf { x } ( t ) \} ,
$$

and is generally time dependent.

# Autocorrelation and Autocovariance of a Stochastic Process

The autocorrelation of the stochastic process $\mathbf { x } ( t )$ is the expectation of the product of the random variables $\mathbf { x } ( t _ { 1 } )$ and ${ \bf x } ( t _ { 2 } )$ , viz.,

$$
R ( t _ { 1 } , t _ { 2 } ) = E \{ \mathbf { x } ( t _ { 1 } ) \mathbf { x } ( t _ { 2 } ) \} = \int _ { - \infty } ^ { + \infty } x _ { 1 } x _ { 2 } f ( x _ { 1 } , x _ { 2 } ; t _ { 1 } , t _ { 2 } ) \mathrm { d } x _ { 1 } \mathrm { d } x _ { 2 } .
$$

The autocovariance of $\mathbf { x } ( t )$ is the mathematical expectation of the product of the random variables $\mathbf { x } ( t _ { 1 } )$ and ${ \bf x } ( t _ { 2 } )$ , viz.,

$$
C ( t _ { 1 } , t _ { 2 } ) = E \{ [ { \bf x } ( t _ { 1 } ) - \eta ( t _ { 1 } ) ] [ { \bf x } ( t _ { 2 } ) - \eta ( t _ { 2 } ) ] \} .
$$

It follows immediately that

$$
\begin{array} { r l } & { C ( t _ { 1 } , t _ { 2 } ) = R ( t _ { 1 } , t _ { 2 } ) - \eta ( t _ { 1 } ) \eta ( t _ { 2 } ) \ , } \\ & { } \\ & { \sigma _ { \mathbf { x } ( t ) } ^ { 2 } = C ( t , t ) = R ( t , t ) - \eta ^ { 2 } ( t ) \ , } \end{array}
$$

and the autocorrelation is equal to the autocovariance for a stochastic process with zero mean. The autocovariance is centred and the autocorrelation is not.

# Stationary Processes

A particularly simple case, which often arises in physics, is one in which the various moments of the r.v. ${ \bf x } ( t )$ are invariant under time translation. The time origin is thus arbitrary, and although the process is time dependent, it is conserved in a probabilistic sense.

A stochastic process $\mathbf { X }$ is said to be stationary if the random variables

$$
\mathbf { x } ( t ) \quad { \mathrm { a n d } } \quad \mathbf { x } ( t + \varepsilon )
$$

have the same statistics, for any $\varepsilon$ . A weaker definition, which is often sufficient in practice, requires the mean of the s.p. to be time independent and the autocorrelation to depend only on the interval $\tau = t _ { 2 } - t _ { 1 }$ and not on $t _ { 2 }$ :

$$
E \{ { \bf x } ( t ) \} = \eta = \mathrm { c o n s t a n t } , \quad E \{ { \bf x } ( t + \tau ) { \bf x } ( t ) \} = R ( \tau ) .
$$

# Spectral Density

The spectral density or power spectrum of a stationary s.p. ${ \bf x } ( t )$ is defined to be the Fourier transform $S ( f )$ , if it exists, of the autocorrelation function $R ( \tau )$ of the process.

# Examples of Stochastic Processes

Bearing in mind the most common applications, two random processes are described here which use the probability distributions discussed previously, namely the normal distribution and the Poisson distribution.

# Normal Process

A process $\mathbf { x } ( t )$ is said to be normal if, for all $n , t _ { 1 } , t _ { 2 } , \ldots , t _ { n }$ , the random variables $\mathbf { x } ( t _ { 1 } )$ ; : : : ; $\mathbf { x } ( t _ { n } )$ have a joint normal distribution. The statistics of a normal s.p. are completely determined by its mean $\eta ( t )$ and autocovariance $C ( t _ { 1 } , t _ { 2 } )$ . Since

$$
E \{ { \bf x } ( t ) \} = \eta ( t ) , \qquad \sigma _ { { \bf x } ( t ) } ^ { 2 } = C ( t , t ) ,
$$

the first order density of the s.p. is given by

$$
f ( x , t ) = \frac { 1 } { \sqrt { 2 \pi C ( t , t ) } } \exp \left\{ - \frac { [ x - \eta ( t ) ] ^ { 2 } } { 2 C ( t , t ) } \right\} .
$$

If the s.p. is stationary, it follows that

$$
E \{ { \bf x } ( t ) \} = \eta , \qquad \sigma _ { \bf x } ^ { 2 } = C ( 0 ) .
$$

The autocorrelation $R ( \tau )$ and the autocovariance $C ( \tau )$ of the s.p. are not determined a priori. There are infinitely many normal stochastic processes, with the same mean $\eta$ and variance $C ( 0 )$ , which differ in the function $C ( \tau )$ for $\tau \neq 0$ .

¤The power spectrum of this process is the Fourier transform of the autocorrelation function,

$$
S ( f ) = \mathrm { F T } [ R ( \tau ) ] \ ,
$$

if it exists (Wiener–Khinchine theorem).

Poisson Process

Consider an interval $[ 0 , T ]$ within which $n$ points are chosen at random. The probability of finding exactly $k$ points within the sub-interval $[ t _ { 1 } , t _ { 2 } ]$ of $[ 0 , T ]$ is given by

$$
P \left\{ k \mathrm { i n } \left[ t _ { 1 } , t _ { 2 } \right] \right\} = C _ { n } ^ { k } p ^ { k } ( 1 - p ) ^ { n - k } = \frac { n ! } { k ! ( n - k ) ! } p ^ { k } ( 1 - p ) ^ { n - k } ,
$$

where

$$
p = \frac { t _ { 2 } - t _ { 1 } } { T } .
$$

Suppose we have

$$
n \gg 1 \quad \mathrm { a n d } \quad \frac { t _ { 2 } - t _ { 1 } } { T } \ll 1 , \quad n  \infty , T  \infty , \frac { n } { T } = \mathrm { c o n s t a n t } .
$$

Then, putting $n / T = \lambda$ , the probability of finding $k$ points in an interval of length $t _ { 2 } - t _ { 1 }$ D, placed anywhere along the time axis, is

$$
P \{ k \ \mathrm { i n } \ ( t _ { 2 } - t _ { 1 } ) \} = \mathrm { e } ^ { - \lambda ( t _ { 2 } - t _ { 1 } ) } { \frac { [ \lambda ( t _ { 2 } - t _ { 1 } ) ] ^ { k } } { k ! } } \ .
$$

We thus obtain a set of point events randomly distributed in time, the probabilities associated with each interval being independent, provided that the intervals do not intersect.

![](images/62f9e018fe0cee258a4e81336b5a28ef5bd3d5b575f515be9e28d2a98e7d44b2.jpg)  
Fig. B.4 $\mathbf { x } ( t )$ is a Poisson process and $\mathbf { y } ( t )$ is a Poisson impulse process

We now define the Poisson process ${ \bf x } ( t )$ in the following way: we set $\mathbf { x } ( 0 ) = 0$ and $\mathbf { x } ( t _ { 2 } ) - \mathbf { x } ( t _ { 1 } )$ equal to the number of points in the interval $[ t _ { 1 } , t _ { 2 } ]$ D. The family of functions resulting from this definition is called the Poisson process (Fig. B.4). At a given time $t$ , the constructions $\mathbf { x } ( t )$ constitute a random variable with a Poisson distribution of parameter $\lambda t$ .

It follows immediately that

$$
\begin{array} { c } { { E \{ { \bf x } ( t _ { \mathrm { a } } ) - { \bf x } ( t _ { \mathrm { b } } ) \} = \lambda ( t _ { \mathrm { a } } - t _ { \mathrm { b } } ) ~ , } } \\ { { { } } } \\ { { E \left\{ \left[ { \bf x } ( t _ { \mathrm { a } } ) - { \bf x } ( t _ { \mathrm { b } } ) \right] ^ { 2 } \right\} = \lambda ^ { 2 } \left( t _ { \mathrm { a } } - t _ { \mathrm { b } } \right) ^ { 2 } + \lambda ( t _ { \mathrm { a } } - t _ { \mathrm { b } } ) ~ . } } \end{array}
$$

As an example of a Poisson process, consider a distant star emitting photons which are collected by a telescope. A photoelectric detector (see Chap. 7) gives an impulse at the arrival of each photon. These impulses are registered by a counter, and the counter reading constitutes a Poisson process ${ \bf x } ( t )$ .

Poisson Impulses

Consider the process $\mathbf { y } ( t )$ ,

$$
\mathbf { y } ( t ) = \sum _ { i } \delta ( t - t _ { i } ) \ ,
$$

formed from a series of Dirac distributions at the random instants $t _ { i }$ described in the last section. The process can be regarded as the limit as $\varepsilon$ tends to zero of the stochastic process

$$
{ \bf z } ( t ) = \frac { { \bf x } ( t + \varepsilon ) - { \bf x } ( t ) } { \varepsilon } ,
$$

where $\mathbf { x } ( t )$ is the Poisson s.p. It is therefore the derivative of $\mathbf { X }$ in the sense of distributions. Then

$$
{ \bf y } ( t ) = \frac { \mathrm { d } { \bf x } ( t ) } { \mathrm { d } t } = \operatorname * { l i m } _ { \varepsilon  0 } { \bf z } ( t ) { \bf \Psi } ,
$$

and in the stationary case

$$
E \{ \mathbf { y } ( t ) \} = \lambda , \quad R ( \tau ) = \lambda ^ { 2 } + \lambda \delta ( \tau ) , \quad C ( \tau ) = \lambda \delta ( \tau ) .
$$

The spectral density $S ( f )$ of the process $\mathbf { y } ( t )$ is the Fourier transform of $R ( \tau )$

$$
S ( f ) = \lambda ^ { 2 } \delta ( f ) + \lambda .
$$

Apart from an impulse at the origin, this spectral density consists of a term independent of the frequency, and is said to have a white spectral density.

# Transformation of a Process

Consider a process ${ \bf x } ( t )$ , and a rule associating a new function $\mathbf { y } ( t )$ with each function $\mathbf { x } ( t )$ . The statistics of $\mathbf { y } ( t )$ can, in general, be deduced from those of ${ \bf x } ( t )$ . There are many applications, when we regard $\mathbf { x } ( t )$ as the input of a system $S$ , and $\mathbf { y } ( t )$ as its output (Fig. B.5). The output s.p. depends partly on the input s.p. and partly on the properties of the system. One important application is filtering (see Sect. 9.1.3).

Example

Consider a stationary and central normal s.p., and the transformation

$$
\mathbf { y } ( t ) = \mathbf { x } ^ { 2 } ( t ) .
$$

The density of $\mathbf { x } ( t )$ is given by

$$
f _ { \mathbf { x } } ( x ) = \frac { 1 } { \sigma \sqrt { 2 \pi } } \mathbf { e } ^ { - x ^ { 2 } / 2 \sigma ^ { 2 } } ,
$$

and it can be shown that the density of the s.p. $\mathbf { y } ( t )$ , which is not a normal s.p., is

$$
f _ { { \bf y } } ( y ) = \frac { 1 } { \sqrt { 2 \pi R ( 0 ) y } } \exp \left[ - \frac { y } { 2 R ( 0 ) } \right] H ( y ) ,
$$

where $R ( \tau )$ is the autocorrelation of $\mathbf { x } ( t )$ and $H$ is the Heaviside step function.

The autocorrelation of the s.p. $\mathbf { y } ( t )$ can be deduced from the relation

$$
E \{ \mathbf { x } ^ { 2 } ( t + \tau ) \mathbf { x } ^ { 2 } ( t ) \} = E \{ \mathbf { x } ^ { 2 } ( t + \tau ) \} E \{ \mathbf { x } ^ { 2 } ( t ) \} + 2 E ^ { 2 } \{ \mathbf { x } ( t + \tau ) \mathbf { x } ( t ) \} ,
$$

which gives

$$
R _ { \mathbf { y } } ( \tau ) = R ^ { 2 } ( 0 ) + 2 R ^ { 2 } ( \tau ) \ .
$$

The variance of $\mathbf { y } ( t )$ is then

$$
\sigma _ { \mathbf { y } } ^ { 2 } = E \{ \mathbf { y } ^ { 2 } ( t ) \} - E ^ { 2 } \{ \mathbf { y } ( t ) \} = 2 R ^ { 2 } ( 0 ) ~ .
$$

# Ergodicity of a Stochastic Process

The ergodicity of an s.p. bears on the question of whether, starting from a single outcome $\mathbf { x } ( t , \zeta )$ of an experiment, it is possible to determine the statistical properties of the stochastic process ${ \bf x } ( t )$ . Put another way, are the mean, variance, autocorrelation, and so on, calculated from a single outcome $x ( t )$ , identical to the same quantities evaluated for the entire set of outcomes as we have defined them above?

It is intuitively clear that such a result can only hold if the process is stationary and if $x ( t )$ takes all possible values in the course of time. Not all stochastic processes will satisfy this condition. Consider the example of the oscillators given above; the variance of the s.p. is not equal to the variance of the voltage measured for a particular outcome.

In a physical process, the time variation of the variable is easily accessible using some measuring device. On the other hand, it is generally difficult to measure a large number of independent outcomes of the s.p. at the same instant $t _ { 0 }$ . Ergodicity is therefore a property which facilitates statistical analysis. (Brownian motion is an example of an ergodic process: it makes no difference whether we take the time average of the velocity of one molecule, or the mean over the whole set of molecules at a given time. The velocity of any molecule will range over all possible values in the course of time.)

Definition. A stochastic process $\mathbf { x } ( t )$ is ergodic if the averages taken over time are equal to the averages taken over the ensemble, that is, the expectation values.

We can establish criteria for the ergodicity of a stationary s.p. by formulating the notion of a time average. Define

$$
\begin{array} { c } { { \displaystyle x _ { T } = \frac { 1 } { T } \int _ { 0 } ^ { T } x ( t ) \mathrm { d } t \mathrm { ~ , ~ } } } \\ { { \displaystyle \hat { R } _ { T } ( \tau ) = \frac { 1 } { T } \int _ { 0 } ^ { T } x ( t ) x ( t + \tau ) \mathrm { d } t \mathrm { ~ . ~ } } } \end{array}
$$

Then $\mathbf { X } _ { T }$ and $\hat { \mathbf { R } } _ { T } ( \tau )$ are respectively a random variable and a stochastic process, whose values are determined for each outcome $\zeta$ . We wish to establish conditions for the following to hold:

$$
\begin{array} { c } { { \displaystyle \operatorname* { l i m } _ { T  \infty } x _ { T } = \eta = E \{ { \bf x } ( t ) \} ~ , } } \\ { { \displaystyle \operatorname* { l i m } _ { T  \infty } \hat { R } _ { T } ( \tau ) = R ( \tau ) = E \{ { \bf x } ( t ) { \bf x } ( t + \tau ) \} ~ . } } \end{array}
$$

The question is closely related to the following: starting from a physical measurement made over a finite time $T$ and giving the values of one outcome $x ( t )$ of the stochastic process during this interval, is it possible to obtain significant information about the expectation values characterising the s.p., such as the mean, variance, autocorrelation, and so on?

The expressions $x _ { T }$ and $\hat { R } _ { T } ( \tau )$ do not always converge to the corresponding expectation values. This point will be discussed in more detail later (see Sect. B.3), when measurements of random physical quantities are considered.

# Filtering

Frequency Filtering

Consider the linear operation

$$
y ( t ) = \int _ { - \infty } ^ { + \infty } x ( t - \theta ) h ( \theta ) \mathrm { d } \theta
$$

applied to a stationary process $\mathbf { x } ( t )$ , where $h ( \theta )$ is a given function. This convolution is called filtering of the process $\mathbf { x } ( t )$ by the filter $h$ :

$$
y ( t ) = x ( t ) \star h ( t ) .
$$

From the convolution theorem

$$
\tilde { y } ( s ) = \tilde { x } ( s ) \tilde { h } ( s ) ,
$$

where

$$
\tilde { h } ( s ) = \int _ { - \infty } ^ { + \infty } h ( t ) \mathrm { e } ^ { 2 \mathrm { i } \pi s t } \mathrm { d } t
$$

is called the transfer function of the filter and is generally complex. If we set $x ( t ) =$ $\delta ( t )$ , we obtain

$$
\begin{array} { r } { y ( t ) = h ( t ) . } \end{array}
$$

This implies that the function $h ( t )$ is the response of the filter to an instantaneous impulsive input signal. It is also called the impulsive filter response.

The function $| \tilde { h } ( s ) | ^ { 2 }$ is the transfer function for the spectral power, or power, of j jthe filter. It is real and positive, but only gives information about the modification of the amplitude spectrum of the process by the filter. It reveals nothing about modifications to the phase.

Time Filtering

When a process $\mathbf { x } ( t )$ is measured over an interval $[ - T / 2 , T / 2 ]$ , and assumed to be zero outside this interval, this is equivalent to considering a second process $\mathbf { y } ( t )$ such that

$$
{ \bf y } ( t ) = \pi \left( \frac { t } { T } \right) { \bf x } ( t ) .
$$

Such a situation is typical of a physical measurement, where a signal can only be measured during some finite time $T$ . The Fourier transform of the above expression is

$$
\tilde { y } ( s ) = \tilde { x } ( s ) \star T \mathrm { s i n c } ( T s ) \ ,
$$

so that multiplication by the box function in time amounts to a convolution in frequency space. This convolution constitutes a blurring of the spectrum of the original process due to the fact that the signal is only measured for a finite time. It should be noted in particular that all information about frequencies below $1 / T$ is lost.

# B.3 Physical Measurements and Estimates

In this section we discuss physical problems for which the rigorous mathematical theory of probability was developed. In real physical situations, a continuous or discrete quantity is only ever measured finitely often or over a finite time. It is in the nature of things that the results of repeating the same experiment should be different and random in character. As seen in Sect. 7.2, this fluctuation or noise is an apparently unavoidable feature of all physical measurement.

The physicist studying some physical phenomenon, for example a quantity $x$ varying in time, can only do so over some finite period of time $T$ . He can then evaluate the mean, variance, or other attributes, for the resulting discrete or continuous measurements. The same situation would arise if he measured a quantity $y$ (for example, a pressure) a certain number of times. Each measurement would give a different result, and he could once again evaluate a mean and a variance. It could then be said that we are studying the statistics of the phenomenon $x ( t )$ or the quantity $y$ . The change in terminology, from speaking of probabilities to speaking of statistics, is an indication that a priori we do not know whether or not $x ( t )$ or $y$ have the properties of a process or a random variable.

Measurements provide an instance or an observation of the underlying phenomenon. Statistical calculation (of mean, variance, and so on), carried out on the values thus obtained, provides estimators of the mean and variance of the underlying process $\mathbf { x } ( t )$ or random variable $\mathbf { y }$ , insofar as these can be supposed to constitute a correct representation of the physical phenomena. These estimators are themselves fluctuating quantities; a further set of measurements leads to a new value of the estimators. The problem facing the statistician is to evaluate the validity of these estimators with a view to describing some underlying reality.

As physical measurement always involves estimation, it is actually an abuse of language to speak of measuring the moments of a variable or a stochastic process. This abuse is so widespread that we shall also indulge in it, having drawn attention to the problem.

# B.3.1 An Example of Estimation: The Law of Large Numbers

Consider a random variable $\mathbf { X }$ with mean $\eta$ and variance $\sigma ^ { 2 }$ , and an experiment $E _ { n }$ consisting of the $n$ -fold repetition of an identical experiment. The latter leads to $n$ variables $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { n }$ , from which the sample mean can be calculated:

$$
{ \overline { { \mathbf { x } } } } = { \frac { 1 } { n } } ( \mathbf { x } _ { 1 } + \mathbf { x } _ { 2 } + \cdots + \mathbf { x } _ { n } ) \ .
$$

We know that

$$
E \{ \overline { { { \bf x } } } \} = \eta , \qquad \sigma _ { \overline { { { \bf x } } } } ^ { 2 } = \frac { \sigma ^ { 2 } } { n } ,
$$

and it can be shown that

$$
P \{ \eta - \varepsilon < \overline { { \mathbf { x } } } < \eta + \varepsilon \} \ge 1 - \frac { \sigma ^ { 2 } } { n \varepsilon ^ { 2 } } .
$$

The experiment $E _ { n }$ is now carried out once, giving a set of values $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ . The quantity

$$
x = { \frac { 1 } { n } } ( x _ { 1 } + x _ { 2 } + \cdots + x _ { n } )
$$

is considered to be a reliable estimate of the mean $\eta$ , for we can be practically certain that the inequality

$$
\eta - \varepsilon < x < \eta + \varepsilon
$$

will hold. Put another way, if we were to repeat the experiment a very large number of times, the quantity $x$ would satisfy these inequalities $9 9 \%$ of the time, provided

$$
1 - \frac { \sigma ^ { 2 } } { n \varepsilon ^ { 2 } } = 0 . 9 9 .
$$

We see that, compared to the rigorous results of probability theory, statistical conclusions suffer from a certain fuzziness.

# B.3.2 Estimating the Moments of a Process

Consider a stationary ergodic process $\mathbf { x } ( t )$ , with mean $\eta$ and autocorrelation $R _ { \bf x } ( t )$ . The physical measurement only provides information concerning a single instance of this process, and only during the time interval $[ 0 , T ]$ . From the measurement, the quantities

$$
\begin{array} { c } { \displaystyle { x _ { T } = \frac { 1 } { T } \int _ { 0 } ^ { T } x ( t ) \mathrm { d } t \mathrm { ~ , ~ } } } \\ { \displaystyle { \hat { R } _ { T } ( \tau ) = \frac { 1 } { T } \int _ { 0 } ^ { T } x ( t ) x ( t + \tau ) \mathrm { d } t \mathrm { ~ , ~ } } } \end{array}
$$

can be calculated. A priori, these quantities are not equal to $\eta$ and $R _ { \bf x } ( t )$ . They can be regarded as instances of a random variable and a stochastic process, respectively, resulting from a transformation of the s.p. ${ \bf x } ( t )$ . Indeed, these quantities are defined for any given outcome. The physical measurement gives a single value for each and these values are called estimators of $\eta$ and $R _ { \bf x } ( t )$ .

An estimator is said to be unbiased if

$$
E \{ { \bf x } _ { T } \} = \eta , \qquad E \{ { \hat { \bf R } } _ { T } ( \tau ) \} = R _ { \bf x } ( \tau ) .
$$

We can show that, under certain convergence restrictions, the quantities $x _ { T }$ and $\hat { R } _ { T } ( \tau )$ tend to $\eta$ and $\hat { R } _ { \bf x } ( \tau )$ , respectively, as $T$ tends to infinity (see Chap. 9).

# Mean

It can be shown that the variance of the estimate $\mathbf { X } _ { T }$ is given as a function of $T$ by the expression

$$
\sigma _ { \mathbf { x } _ { T } } ^ { 2 } = \frac { 1 } { T } \int _ { - \infty } ^ { + \infty } \left[ R _ { \mathbf { x } } ( \tau ) - \eta ^ { 2 } \right] \left[ \pi \left( \frac { \tau } { T } \right) \star \pi \left( \frac { \tau } { T } \right) \right] \mathrm { d } \tau \ .
$$

# Application

Let ${ \bf x } ( t )$ be a stationary r.v. with zero mean $\mathit { \Pi } _ { \mathcal { I } } = 0 \mathit { \Pi } _ { , }$ ) and constant spectral density (i.e., white)

$$
S _ { \bf x } ( f ) = S ( 0 ) = \mathrm { c o n s t a n t } ,
$$

filtered by a low-pass filter

$$
h ( f ) = \pi \left( { \frac { f } { 2 f _ { \mathrm { c } } } } \right) .
$$

After filtering, the process $\mathbf { y } ( t )$ has variance

$$
\sigma _ { \mathbf { y } } ^ { 2 } = R ( 0 ) - \eta ^ { 2 } = R ( 0 ) = \int _ { - \infty } ^ { + \infty } S _ { \mathbf { y } } ( f ) \mathrm { d } f = 2 f _ { \mathrm { c } } S ( 0 ) .
$$

Let us now calculate the variance of the estimate ${ \bf y } _ { T }$ made on the interval $[ 0 , T ]$ :

$$
\begin{array} { l } { { \displaystyle y _ { T } = \frac { 1 } { T } \int _ { 0 } ^ { T } y ( t ) \mathrm { d } t \ : , } } \\ { { \displaystyle \sigma _ { \mathrm { y } _ { T } } ^ { 2 } = \frac { 1 } { T } \int _ { - \infty } ^ { + \infty } R _ { \mathrm { y } } ( \tau ) \left[ \pi \left( \frac { \tau } { T } \right) \star \cal I \left( \frac { \tau } { T } \right) \right] \mathrm { d } \tau } } \\ { { \displaystyle \quad = \frac { 1 } { T } \left| \mathrm { F T } [ R _ { \mathrm { y } } ( \tau ) ] \star T [ \mathrm { s i n c } ( T f ) ] ^ { 2 } \right| _ { f = 0 } } } \\ { { \displaystyle \quad = \frac { 1 } { T } \int _ { - \infty } ^ { + \infty } { \cal S } ( f ) \left| \mathrm { s i n c } ( T f ) \right| ^ { 2 } T \mathrm { d } f \ : , } } \end{array}
$$

noting that

$$
\Pi \left( \frac { \tau } { T } \right) \star \Pi \left( \frac { \tau } { T } \right) = \Lambda \left( \frac { \tau } { T } \right) , \quad \mathrm { F T } [ R _ { \mathbf { y } } ( \tau ) ] = S ( f ) .
$$

If $T \gg 1 / f _ { \mathrm { c } }$ , a condition that is easily satisfied, $\sigma _ { \mathbf { y } _ { T } } ^ { 2 }$ is approximated by

$$
\sigma _ { \mathbf { y } _ { T } } ^ { 2 } \simeq \frac { 1 } { T } S _ { \mathbf { y } } ( 0 ) ,
$$

and hence

$$
\sigma _ { \mathbf { y } _ { T } } ^ { 2 } \simeq \frac { \sigma _ { \mathbf { y } } ^ { 2 } } { 2 f _ { \mathrm { c } } T } .
$$

The estimate ${ \bf y } _ { T }$ of the mean of the s.p. has indeed a variance tending to zero as $T$ increases.

# Autocorrelation

In a similar way, the estimator of the autocorrelation function is taken to be

$$
\hat { R } ( \tau ) = \frac { 1 } { T } \int _ { 0 } ^ { T } x ( t ) x ( t + \tau ) \mathrm { d } t \mathrm { ~ . ~ }
$$

It can be shown that this estimator is unbiased and that its variance

$$
\mathrm { V a r } \{ \hat { \mathbf { R } } ( \tau ) \} = E \left\{ | \hat { \mathbf { R } } ( \tau ) - R _ { \mathbf { x } } ( \tau ) | ^ { 2 } \right\}
$$

tends to zero, when $T$ tends to infinity. For large $\tau$

$$
\operatorname { V a r } \{ \hat { \mathbf { R } } ( \tau ) \} \simeq \frac { 1 } { T } \int _ { - \infty } ^ { + \infty } R _ { \mathbf { x } } ^ { 2 } ( \tau ) \mathrm { d } \tau .
$$

When the process has white spectral density and is limited to frequencies $f < f _ { \mathrm { c } }$ , it follows that

$$
\mathrm { V a r } \{ \hat { \mathbf { R } } ( \tau ) \} \leq \frac { R _ { \mathrm { x } } ^ { 2 } ( 0 ) } { f _ { \mathrm { c } } T } \ .
$$

# Spectral Density

Can the quantity

$$
{ \frac { 1 } { T } } \left| \int _ { 0 } ^ { T } x ( t ) \mathrm { e } ^ { - 2 \pi \mathrm { i } f t } \mathrm { d } t \right| ^ { 2 }
$$

be regarded as an unbiased estimator for the spectral density $S _ { \mathbf { x } } ( f )$ of the process ${ \bf x } ( t ) ?$ This could only be the case if

$$
\operatorname* { l i m } _ { T \to \infty } { \frac { 1 } { T } } \left| \int _ { 0 } ^ { T } x ( t ) \mathrm { e } ^ { - 2 \pi \mathrm { i } f t } \mathrm { d } t \right| ^ { 2 } = S _ { \mathrm { x } } ( f )
$$

and, moreover, the variance of the estimator tends to zero as $T$ tends to infinity. In general, these conditions are not met, the estimator is biased, and care is needed over the limit as $T$ becomes large. We refer to more specialised treatments for further discussion.

The power spectrum can also be estimated by measuring the signal through a filter $\tilde { g } ( f )$ of width $\Delta f$ , centred on the frequency $f _ { 0 }$ . Then

$$
{ \hat { S } } ( f _ { 0 } ) = { \mathrm { e s t i m a t o r ~ o f ~ } } S _ { \mathbf { x } } ( f _ { 0 } ) = { \frac { 1 } { T } } \int _ { 0 } ^ { T } | y ( t ) | ^ { 2 } \mathrm { d } t
$$

![](images/5c01bd532b2acf9c0fa75077d9224b4a30386f76155aebe60edb75f097c26fb0.jpg)  
Fig. B.6 Estimation of the mean and power spectrum of a stochastic process $\mathbf { x } ( t )$ . (a) An instance $x ( t , \zeta )$ of the process. (b) The process $\mathbf { y } ( t )$ obtained from $\mathbf { x } ( t )$ by the low-pass filtering $h ( f )$ , with cutoff frequency $f _ { \mathrm { c } }$ . The high frequencies have disappeared. (c) Physical measurement of $\mathbf { y } ( t )$ over a time $T$ . (d) Autocorrelation function $R _ { \bf x } ( \tau )$ of the process $\mathbf { x } ( t )$ , and autocorrelation function $\hat { R } _ { \bf y } ( \tau )$ of the measurement, Othe dashed curves giving the confidence interval $\sigma _ { \mathrm { c } }$ . The mean $\eta = 0$ of the s.p. $\mathbf { x } ( t )$ , Dand the estimate $y _ { T }$ of this mean . $( y _ { T } \neq 0 )$ /, have also ¤been indicated

with

$$
\tilde { y } ( f ) = \tilde { x } ( f ) .
$$

It can then be shown that

$$
\operatorname { V a r } \{ \hat { \mathbf { S } } ( f _ { 0 } ) \} = \frac { S _ { \mathbf { x } } ^ { 2 } ( f ) } { T \Delta f } .
$$

Figure B.6 illustrates the above discussion.

# Appendix C Physical and Astronomical Constants

The vast majority of physical and astronomical constants required in this book can be found in Allen C.W., Astrophysical Quantities (AQ). A few of the most frequently used quantities are quoted here.

<table><tr><td>Speed of light</td><td>C</td><td>2.999792 458×10m s-1</td></tr><tr><td>Gravitational constant</td><td>G</td><td>6.670 × 10-1 N m² kg-2</td></tr><tr><td>Planck&#x27;s constant</td><td>h</td><td>6.626 20 × 10-34 J s</td></tr><tr><td>Electron charge</td><td>e</td><td>1.602 192 × 10-19 C</td></tr><tr><td>Electron mass</td><td>me</td><td>9.109 56 × 10-31 kg</td></tr><tr><td>Boltzmann&#x27;s constant</td><td>k</td><td>1.380 62 ×10-23 JK-1</td></tr><tr><td>Proton mass</td><td>mp</td><td>1.672 661 × 10-27 kg</td></tr><tr><td>Rydberg constant</td><td>RH</td><td>109 677.576cm-1</td></tr><tr><td>Zeeman shift</td><td>△v/B</td><td>1.399 61 × 10l° Hz T-1</td></tr><tr><td>Wavelength associated with1eV</td><td>20</td><td>1.23985×10-6m</td></tr><tr><td>Frequency associated with1eV</td><td>Vo</td><td>2.417 965 ×1014 Hz</td></tr><tr><td>Temperature associated with1eV</td><td></td><td>11604.8K</td></tr><tr><td>Astronomical unit</td><td>AU</td><td>1.495 979 × 10ll m</td></tr><tr><td>Parsec</td><td>pc</td><td>3.085 678 ×1016 m 3.261 633 light yr</td></tr><tr><td>Mass of Sun</td><td>Mo</td><td>1.989 × 1030 kg</td></tr><tr><td>Radius of Sun</td><td>R</td><td>6.9599×10m</td></tr><tr><td>Luminosity of Sun</td><td>LO</td><td>3.826×1026W</td></tr></table>

# Blackbodies

<table><tr><td>Stefan-Boltzmann constant Planck&#x27;s law</td><td>g = 5.66956×10-8Wm-²K-4 Bx =2hc²λ-5/(ehc/kλT-1) [W m-² m-1 sr-1]</td></tr></table>

# Appendix D Tables of Space Missions

Space missions at all wavelengths, as mentioned in the book.

<table><tr><td>Mission</td><td>Objective</td><td>Launch</td></tr><tr><td>Apollo</td><td>Lunar missions</td><td>1963-1972</td></tr><tr><td>AXAF(Advanced X-ray Astrophysics Facility)</td><td>X-ray observatory</td><td>1999</td></tr><tr><td>Boomerang</td><td>Balloon studying the diffuse cosmological background</td><td>1998</td></tr><tr><td>Cassini-Huygens</td><td>Exploration of Saturn</td><td>1997</td></tr><tr><td>CHANDRA (AXAF)</td><td>X-ray observatory</td><td>1999</td></tr><tr><td>Clementine</td><td>Exploration of the Moon</td><td>1994-1994</td></tr><tr><td>Corot (COnvection ROtation and</td><td>Search for exoplanets and</td><td>2006</td></tr><tr><td>planetary Transits)</td><td>asteroseismology</td><td></td></tr><tr><td>Cos-B (Cosmic ray Satellite)</td><td>y-ray observatory</td><td>1975-1982</td></tr><tr><td>Darwin</td><td>Search for exo-Earths</td><td>2010</td></tr><tr><td>Einstein FUSE (Far Ultraviolet Spectroscopic</td><td>X-ray observatory</td><td>1979</td></tr><tr><td>Explorer)</td><td>UVobservatory</td><td>1999</td></tr><tr><td>Gaia</td><td>Astrometry</td><td>2010</td></tr><tr><td>Galex (Galaxy Evolution Explorer) Glast (Gamma-ray Large Area Space</td><td>UV Observatory</td><td>2003</td></tr><tr><td>Telescope)</td><td>Y-ray observatory</td><td>2008</td></tr><tr><td>Granat</td><td>X-ray observatory</td><td>1989-1998</td></tr><tr><td>GRO (Gamma-Ray Observatory)</td><td>Y-ray observatory</td><td>1991-2000</td></tr><tr><td>HEAO (High Energy Astronomy Observatories)</td><td>High energy observatories</td><td>1979-1981</td></tr><tr><td>Hipparcos-Tycho</td><td>Astrometry</td><td>1989-1993</td></tr><tr><td>HST (Hubble Space Telescope)</td><td>Visible-IRobservatory</td><td>1990</td></tr><tr><td>Integral (International Gamma-Ray</td><td>Xandyobservatory</td><td>2002</td></tr><tr><td>Astrophysics Laboratory) IRAS (Infrared Astronomical Satellite)</td><td>IR observatory</td><td>1983</td></tr></table>

(continued)

(continued)   

<table><tr><td>Mission</td><td>Objective</td><td>Launch</td></tr><tr><td>ISO (Infrared Space Observatory)</td><td>IR observatory</td><td>1995-1998</td></tr><tr><td>IUE (International Ultraviolet Explorer)</td><td>UV observatory</td><td>1978-1996</td></tr><tr><td>JWST (James Webb Space Telescope)</td><td>Visible-IR observatory</td><td>2013</td></tr><tr><td>KAO (Kuiper Airborne Observatory)</td><td>Visible-IR observatory</td><td>1993</td></tr><tr><td>Kepler</td><td>Search for exo-Earths</td><td>2009</td></tr><tr><td>LISA (Laser Interferometer Space Antenna)</td><td>Gravitational wave detection</td><td>2018</td></tr><tr><td>Maxim (Microarcsecond X-ray Imaging Mission)</td><td>X-ray observatory</td><td>2020</td></tr><tr><td>OAO (Orbiting Astronomical Observatories)</td><td>UV observatories</td><td>1976</td></tr><tr><td>ODIN</td><td>Submillimetre observatory</td><td>2001</td></tr><tr><td>Opportunity</td><td>Exploration of Mars</td><td>2003</td></tr><tr><td>OSO8 (Orbiting Solar Observatory)</td><td>Y-ray observation of the Sun</td><td>1975-1978</td></tr><tr><td>Planck</td><td>Exploration of diffuse</td><td>2007</td></tr><tr><td>Pronaos (Projet National</td><td>cosmological background Submillimetre balloon</td><td>1994</td></tr><tr><td>d&#x27;AstronOmie Submillimétrique) Rosat (ROentgen SATellite X-ray</td><td>X-ray observatory</td><td>1992-1999</td></tr><tr><td>observatory) Rosetta</td><td>Study of a comet</td><td>2004</td></tr><tr><td>Rosita</td><td>X-ray observatory</td><td>？</td></tr><tr><td>Sas2 (Small Astronomy Satellite)</td><td>y-ray observatory</td><td>1970</td></tr><tr><td>Sigma</td><td>y-ray observatory</td><td>1989</td></tr><tr><td>SIM (Space Interferometry Mission)</td><td>X-ray observatory</td><td>2013</td></tr><tr><td>Skylab</td><td>Space station</td><td>1973-1979</td></tr><tr><td>SOFIA (Stratospheric Observatory For Infrared Astronomy)</td><td>IR and submillimetre</td><td>2004</td></tr><tr><td>Spitzer</td><td>observatory IR observatory</td><td>2003</td></tr><tr><td>STARS</td><td>Stellar photometry</td><td>2002</td></tr><tr><td>SUZAKU</td><td>X-ray observatory</td><td>2005</td></tr><tr><td>TPF(Terrestrial Planet Finder)</td><td>Search for exo-Earths</td><td>2020</td></tr><tr><td>UHURU (SAS-1)</td><td>X-ray observatory</td><td>1970-1973</td></tr><tr><td></td><td></td><td>1990</td></tr><tr><td>Ulysses</td><td>Exploration of the Sun Exploration of Mars</td><td>1975-1976</td></tr><tr><td>Viking Voyager</td><td>Exploration of the Solar</td><td>1977</td></tr><tr><td>WMAP (Wilkinson Microwave</td><td>System Exploration of diffuse</td><td>2001</td></tr><tr><td>Anisotropy Probe) XEUS (X-Ray Evolving Universe</td><td>cosmological background X-ray observatory</td><td>2010</td></tr><tr><td>Spectroscopy Mission) XMM-Newton (X-ray Multi-Mirror Mission)</td><td>X-ray observatory</td><td>1999</td></tr></table>

# Appendix E Webography

# E.1 Main Earth-Based Telescopes

<table><tr><td>Site</td><td>Name</td><td>Type and diameter</td><td>Nationality</td><td>URL</td></tr><tr><td colspan="5">Radio and submillimetre</td></tr><tr><td>Australia</td><td>Australia Telescope Compact</td><td>Radio (6 m × 22 m)</td><td>Australia</td><td>http://www.narrabri. atnf.csiro.au/</td></tr><tr><td>Australia</td><td>Array Mopra Antenna</td><td>Radio (22 m)</td><td>Australia</td><td>http://www.atnf.csiro. au/</td></tr><tr><td>Australia</td><td>Parkes Observatory</td><td>Radio (64 m)</td><td>Australia</td><td>http://www.parkes.atnf. csiro.au/</td></tr><tr><td>Chile</td><td>Atacama Large Millimeter/ Submillimeter Array</td><td>Europe, Japan, USA, Chile</td><td>mm (0.3-9.6)</td><td>http://science.nrao.edu/ alma/index.shtml</td></tr><tr><td>England</td><td>(ALMA) Cambridge Ryle Telescope</td><td>Radio (8×13 m)</td><td>England</td><td>http://www.mrao.cam. ac.uk/telescopes/</td></tr><tr><td>England</td><td>Jodrell Bank Observatory</td><td>Radio (76 m)</td><td>England</td><td>ryle/ http://www.jb.man.ac. uk/</td></tr><tr><td>England</td><td>Cosmic Anisotropy Telescope</td><td>mm (3 × 0.7 m)</td><td>England</td><td>http://www.mrao.cam. ac.uk/telescopes/ cat/</td></tr><tr><td>France</td><td>Nancay Radio Observatory</td><td>Radio (100 m)</td><td>France</td><td>http://www.obs-nancay. fr/</td></tr><tr><td>Germany</td><td>Effelsberg Radio Telescope</td><td>Radio (100 m)</td><td>Germany</td><td>http://www.mpifr-bonn mpg.de/div/ effelsberg/index_e.</td></tr><tr><td>Holland</td><td>Westerbork Synthesis Radio</td><td>Radio (14 × 25 m)</td><td>Holland</td><td>http://www.astron.nl/ radio-observatoryl public/public-0</td></tr><tr><td>India</td><td>Telescope Giant Metrewave Radio Telescope</td><td>Radio (30 × 45 m)</td><td>India</td><td>http://gmrt.ncra.tifr.res. in/</td></tr><tr><td>Japan</td><td>Nobeyama Radio Observatory</td><td>Radio (45 m)</td><td>Japan</td><td>http://www.nro.nao.ac. jp/indextop-e.html</td></tr><tr><td>Mexico</td><td>Large Millimeter Telescope</td><td>mm (50 m)</td><td>Mexico, USA</td><td> http://www.lmtgtm.org/</td></tr><tr><td>Puerto Rico</td><td>Arecibo Observatory</td><td>Radio (305 m)</td><td>USA</td><td>http://www.naic.edu/</td></tr><tr><td>Sweden</td><td>Onsala Space Observatory</td><td>mm (20 and 25 m)</td><td>Sweden</td><td>http://www.oso. chalmers.se/</td></tr><tr><td>USA</td><td>Five College Radio Astronomy</td><td>Radio (14 m)</td><td>USA</td><td>http://donald.phast. umass.edu/~fcrao/</td></tr><tr><td>USA</td><td>Observatory Green Bank</td><td>Radio (45 and 100 m)</td><td>USA</td><td> http://www.gb.nrao.</td></tr><tr><td>USA</td><td>Hat Creek Radio Observatory</td><td>Radio (6 ×6 m)</td><td>USA</td><td>edu/ http://www.hcro.org/</td></tr><tr><td>USA</td><td>Owens Valley Radio</td><td>Radio (6 × 10.4 m)</td><td>USA</td><td>http://www.ovro. caltech.edu/</td></tr><tr><td>USA</td><td>Observatory Very Large Array</td><td>Radio</td><td>USA</td><td>http://www.vla.nrao.</td></tr><tr><td>USA (Hawaii, Mauna</td><td>Caltech Submil- limeter</td><td>(27 × 25 m) mm (10.4 m)</td><td>USA</td><td>edu/ http://www.submm. caltech.edu/cso/</td></tr><tr><td>Kea) USA (Hawaii, Mauna</td><td>Observatory James Clerk Maxwell</td><td>mm (15 m)</td><td>Canada, UK,</td><td>http://www.jach. Hawaii.edu/JCMT/</td></tr><tr><td>Kea) Optical and infrared</td><td>Telescope</td><td></td><td>Holland</td><td></td></tr><tr><td colspan="3">Australia Anglo-Australian Optical (3.9 m)</td><td>Australia,</td><td>http://www.aao.gov.au/</td></tr><tr><td>Australia</td><td>Observatory Mount Stromlo and Siding</td><td>Optical (1.85</td><td>UK Australia</td><td>http://msowww.anu.</td></tr><tr><td>Chile (Cerro</td><td>Spring Observatories Gemini</td><td>and 2.3 m) Optical-IR (8 m)</td><td>USA,UK,</td><td>edu.au/observing/ http://www.gemini.edu/</td></tr><tr><td>Panch6n) and USA (Hawaii)</td><td>Observatory</td><td></td><td>Canada, Chile, Argentina, Brazil</td><td></td></tr><tr><td>Chile (Cerro Tololo)</td><td>Cerro Tololo Interamerican Observatory</td><td>optique (1, 1.5 et 4m)</td><td>USA</td><td>http://www.ctio.noao. edu/ctio.html</td></tr><tr><td>Chile (La Silla)</td><td>La Silla-ESO Facilities</td><td>Optical (1.5,2.2, 3.5,and</td><td>Europe</td><td>http://www.ls.eso.org/</td></tr><tr><td>Chile (Cerro Paranal)</td><td>Very Large Telescope</td><td>3.6 m) Optical (4 × 8 m)</td><td>Europe</td><td>http://www.eso.org/ public/teles-instr/</td></tr><tr><td>Chile</td><td>European Extremely Large</td><td>Optical (42 m)</td><td>Europe</td><td>vlt.html http://www.eso.org/ projects/e-elt/</td></tr><tr><td>England</td><td>(E-ELT) Cambridge Optical Aperture Synthesis</td><td>Optical (4 × 0.4 m)</td><td>England</td><td>http://www.mrao.cam. ac.uk/telescopes/ coast/</td></tr><tr><td>France</td><td>Telescope Observatoire de Haute- Provence</td><td>Optical (1.2, 1.5, and 1.93 m)</td><td>France</td><td>http://www.obs-hp.fr/</td></tr><tr><td>France</td><td>Observatoire Midi-Pyrenées</td><td>Optical (1 and 2 m)</td><td>France</td><td>http://www.obs-mip.fr/</td></tr><tr><td>Italy</td><td>Loiano Telescopes</td><td>Optical (0.6 and 1.5 m)</td><td>Italy</td><td>http://www.bo.astro.it/ loiano/</td></tr><tr><td>Mexico</td><td>Guillermo Haro Observatory</td><td>Optical (2.1 m)</td><td>Mexico</td><td>http://www.inaoep. mx/~astrofi/ cananea/</td></tr><tr><td>South Africa</td><td>South African Astronomical</td><td>Optical (2 m)</td><td>South Africa</td><td>http://www.saao.ac.za/</td></tr><tr><td>Spain (Calar Alto)</td><td>Observatory Calar Alto Observatory</td><td>Optical (3.5 m)</td><td>Germany,</td><td>www.caha.es</td></tr><tr><td>Spain (Canary Islands)</td><td>Telescopio Nazionale</td><td>Optical (3.5 m)</td><td>Spain Italy</td><td>http://www.tng.iac.es/</td></tr><tr><td>Spain (Canary Islands)</td><td>Galileo THEMIS Heliographic Telescope for the Study of the Magnetism</td><td>Optical (2 m)</td><td>France, Italy</td><td>http://www.themis.iac. es/</td></tr><tr><td>Spain (Canary Islands)</td><td>Gran Telescopio de Canarias</td><td>Optical (10 m)</td><td>Spain</td><td>http://www.gtc.iac.es/</td></tr><tr><td>Spain (Canary Islands)</td><td>Nordic Optical Telescope</td><td>Optical (2.6 m)</td><td>Denmark</td><td>http://www.not.iac.es/</td></tr><tr><td>Spain (Canary Islands)</td><td>Isaac Newton Group</td><td>Optical (4.2, 2.5, and 1 m)</td><td>UK,Holland</td><td>http://www.ing.iac.es/</td></tr><tr><td>USA (Hawaii, Mauna</td><td>Infra-Red Telescope Facility</td><td>IR (3 m)</td><td>USA</td><td>http://irtfweb.ifa. hawaii.edu</td></tr><tr><td>Kea) USA</td><td>Giant Magellan Telescope (GMT)</td><td>Optical (24.5 m)</td><td>USA</td><td>http://www.gmto.org/</td></tr><tr><td>USA</td><td>Thirty Meter Telescope</td><td>Optical (30 m)</td><td>USA</td><td>http://www.tmt.org/</td></tr><tr><td>USA</td><td>(TMT) UK Infra-Red Telescope</td><td>IR (3.8 m)</td><td>UK</td><td>http://www.jach. hawaii.edu/</td></tr><tr><td>USA (Hawaii, Mauna Kea)</td><td>Air Force Maui Optical Station</td><td>Optical (3.7 m)</td><td>USA</td><td>UKIRT/ http://www.fas.org/ spp/military/ program/track/</td></tr><tr><td>USA</td><td>Apache Point Observatory</td><td>Optical (3.5 m)</td><td>USA</td><td>amos.htm http://www.apo.nmsu. edu/</td></tr><tr><td>USA</td><td>Palomar Observatory</td><td>Optical (1.2, 1.5, and 5 m)</td><td>USA</td><td>http://astro.caltech. edu/observatories/ palomar/</td></tr><tr><td>USA (Hawaii, Mauna Kea)</td><td>SUBARU Telescope</td><td>Optical (8.3 m)</td><td>Japan</td><td>http://subarutelescope. org/</td></tr><tr><td>USA</td><td>Lick Observatory</td><td>Optical (3 m)</td><td>USA</td><td>http://www.ucolick. org/</td></tr><tr><td>USA (Hawaii, Mauna Kea)</td><td>University of Hawaii Telescope</td><td>Optical (2.2 m)</td><td>USA</td><td>http://www.ifa.hawaii. edu/88inch/88inch. html</td></tr><tr><td>USA</td><td>Hobby Eberly Telescope</td><td>Optical (9 m)</td><td>USA, Germany</td><td>http://www.astro.psu. edu/het/</td></tr><tr><td>USA (Hawaii, Mauna Kea)</td><td>Canada-France- Hawaii Telescope</td><td>Optical (3.6 m)</td><td>Canada, France, USA</td><td>http://www.cfht. hawaii.edu/</td></tr><tr><td>USA (Hawaii, Mauna Kea)</td><td>Keck Observatory</td><td>Optical (2 ×10m)</td><td>USA</td><td>http://www. keckobservatory. org/</td></tr><tr><td>USA</td><td>Kitt Peak National Observatory</td><td>Optical (0.9,2.1, and 4 m)</td><td>USA</td><td>http://www.noao.edu/ kpno/</td></tr><tr><td>USA</td><td>Large Binocular Telescope Observatory</td><td>Optical (2 × 8.4 m)</td><td>USA, Italy</td><td>www.lbto.org</td></tr><tr><td>USA</td><td>Mount Wilson Observatory</td><td>Optical (1.5, 2.5m)</td><td>USA</td><td>http://www.mtwilson. edu/</td></tr><tr><td>USA</td><td>Multiple Mirror Telescope Observatory</td><td>Optical (6 × 1.8 m)</td><td>USA</td><td>http://cfa-www.harvard. edu/mmt/, http:/l www.mmto.org/</td></tr><tr><td colspan="3">Gravitational waves and neutrinos</td><td></td><td></td></tr><tr><td>Antartic</td><td>Antarctic Muon and Neutrino Detector Array</td><td>mm (13 m X 0.2 m)</td><td>USA</td><td>http://amanda.uci.edu/</td></tr><tr><td>Canada</td><td>Sudbury Neutrino Observatory</td><td>Neutrinos</td><td>Canada, UK, USA</td><td>http://www.sno.phy. queensu.ca/</td></tr><tr><td>Italy</td><td>Virgo Interferometer Laser</td><td>Gravitational waves Gravitational</td><td>France, Italy</td><td>https://wwwcascina. virgo.infn.it/</td></tr><tr><td>USA</td><td>Interferometer Gravitational Wave Observatory</td><td>waves</td><td>USA</td><td>http://www.ligo.caltech. edu/</td></tr></table>

# E.2 Recent Space Missions

<table><tr><td>Name</td><td>Period of activity</td><td>Owners</td><td>Main scientific objective and URL</td></tr><tr><td>AKARI</td><td>2006-2007</td><td>Japan, Europe</td><td>Photometric and spectroscopic observation in the region 2-180 μm in 13 spectral bands.http://www.astro-f. esac.esa.int/</td></tr><tr><td>Cassini-Huygens Mission to Saturn&amp; Titan</td><td>1997-present</td><td>Europe</td><td>Study of Saturn and Titan from the visible to the infrared. http://saturn.jpl.nasa. gov/home/</td></tr><tr><td>Chetra X-ray Observatory</td><td>1999-present</td><td>USA</td><td>Observation of X-ray emissions from high-energy phenomena such as supernovas. http://chandra.harvard.</td></tr><tr><td>COnvection ROtation et planetary Transits (COROT)</td><td>2006-2012 (or beyond)</td><td>France</td><td>edu/ Asteroseismology and search for exoplanets. http://smsc.cnes.fr/ COROT/</td></tr><tr><td>COsmic Background Explorer</td><td>1989-present</td><td>USA</td><td>IR and microwave measurement of diffuse cosmological background. http://lambda. gsfc.nasa.gov/product/cobe/</td></tr><tr><td>(COBE) Far Ultraviolet Spectroscopic Explorer (FUSE)</td><td>1999-2008</td><td>USA, France, Canada</td><td>Exploration of the Universe with high-resolution spectroscopy in the extreme UV. htp://fuse.pha.jhu.edu/</td></tr><tr><td>GALaxy Evolution2003-present EXplorer (GALEX)</td><td></td><td>USA, Korea, France</td><td>UV observation of nearby and remote galaxies. http://www.galex.caltech.edu/</td></tr><tr><td>Global Astrometric Interferometer for Astrophysics (GAIA)</td><td>~2012</td><td>Europe</td><td>Astrometry of around a billion stars in our Galaxy. http://www.rssd.esa.int/gaia/</td></tr><tr><td>High Energy Transient Explorer</td><td>2002-presentI</td><td>USA, Japan, France, Brazil, Italy,</td><td>Detection and localisation of gamma-ray bursts. http://space.mit.edu/HETE/</td></tr><tr><td>Hubble Space Telescope</td><td>1990-present</td><td>India USA</td><td>UV to IR observatory. http://www.stsci.edu/ hst/</td></tr><tr><td>(HST) INTErnational Gamma-Ray Astrophysics Laboratory (INTEGRAL)</td><td>2002-presentEurope</td><td></td><td>Detection of the highest energy phenomena in the Universe. http://sci.esa.int/science- e/www/area/index.cfm?fareaid=21</td></tr><tr><td>Infrared Space Observatory</td><td>1995-1998</td><td>Europe</td><td>Exploration of the IR Universe. http://www. sci.esa.int/iso/</td></tr><tr><td>James Webb Space Telescope</td><td>～2014</td><td>USA</td><td>Optical-IR observatory (successor to HST). http://www.jwst.nasa.gov/</td></tr><tr><td>(JWST) Kepler mission</td><td>2009-2014</td><td>USA</td><td>Detection of exoplanets. http://kepler.nasa. gov/</td></tr><tr><td>PLANCK</td><td>2009-present</td><td>Europe</td><td>Probing anisotropies in the diffuse cosmological background. http://www. rssd.esa.int/index.php?project=PLANCK</td></tr><tr><td>ROSAT</td><td>1990-1999</td><td>Germany, UK, USA</td><td>Global UV exploration of the Universe. http://heasarc.nasa.gov/docs/rosat/rosgof. html</td></tr><tr><td>ROSETTA</td><td>2004-present</td><td>Europe</td><td>Study of the comet 67P/Churyumov-Gerasimenko. http:// www.esa.int/esaSC/120389_index_0_m.</td></tr><tr><td>SOlar and Heliospheric Observatory (SOHO)</td><td>1995-present</td><td>Europe, USA</td><td>Study of the internal structure and atmosphere of the Sun. http://sohowww. nascom.nasa.gov/</td></tr><tr><td>Solar TErrestrial RElations Observatory (STEREO)</td><td>2006-present</td><td>USA</td><td>Study of coronal mass ejections from the Sun using 3D data. http://stp.gsfc.nasa. gov/missions/stereo/stereo.htm</td></tr><tr><td>Spitzer Space Telescope</td><td>2003-present</td><td>USA</td><td>Imaging and spectroscopy between 3 and 180 microns. http://www.spitzer.caltech. edu/</td></tr><tr><td>Stardust</td><td>1999-present</td><td>USA</td><td>Exploration of a comet. http://stardust.jpl. nasa.gov/</td></tr><tr><td>Wilkinson Microwave Anisotropy Probe (WMAP)</td><td>2001-present</td><td>USA</td><td>Mapping the diffuse cosmological background to investigate the formation of the first galaxies.http://map.gsfc.nasa.</td></tr><tr><td>XMM-Newton</td><td>1999-present</td><td>tEurope</td><td>gov/ To study the violent Universe,from the neighbourhood of black holes to the formation of the first galaxies.http:/ www.esa.int/science/xmmnewton, http://xmm.esac.esa.int/</td></tr></table>

# E.3 Databases

<table><tr><td>Nom</td><td>Description</td><td>URL</td></tr><tr><td>Aladin Sky Atlas</td><td>Interactive sky map giving access to digital images of every region of the sky</td><td>http://aladin.u-strasbg.fr/</td></tr><tr><td>Astrophysical CATalogs support System (CATS) of the Special Astrophysical Observatory</td><td>Several astrophysical catalogues, especially in the radio region</td><td>http://cats.sao.ru/</td></tr><tr><td>Atomic Data for Astrophysics</td><td>Data for collisional ionisation and photoionisation,recombination, opacities,etc.</td><td>http://www.pa.uky.edu/~ verner/atom.html</td></tr><tr><td>Besangon Double and Multiple Star Database</td><td>Photometric and spectroscopic data on binary and multiple star systems</td><td>http://bdb.obs-besancon.fr/</td></tr><tr><td>Canadian Astronomy Data Centre</td><td>Storage of ground and space data</td><td>http://cadcwww.dao.nrc. ca/</td></tr><tr><td>(CADC) Cassini-Huygens Mission to Saturn</td><td>Data from the Cassini-Huygens mission</td><td>http://saturn.jpl.nasa.gov/ home/</td></tr><tr><td>&amp;Titan Catalog of Infrared Observations</td><td>Access to published data on more than 10 ooo sources observed in</td><td>http://ircatalog.gsfc.nasa. gov</td></tr><tr><td>Catalogue of Galactic Supernova</td><td>the infrared Catalogue supernova remnants in the Galaxy</td><td>http://www.mrao.cam.ac. uk/surveys/snrs/</td></tr><tr><td>Remnants Center for Earth et Planetary Studies</td><td>Several thousand images of the Solar System</td><td>http://www.nasm.si.edu/ ceps/</td></tr><tr><td>(CEPS) Centre de Donnees de la Physique des</td><td>Data on plasma physics</td><td>http://cdpp.cesr.fr/</td></tr><tr><td>Plasmas Centre de Données Astronomiques de</td><td>Several thousand astronomical catalogues</td><td>http://vizier.u-strasbg.fr/</td></tr><tr><td>Strasbourg Digitized Sky Survey at LEDAS</td><td>Access to the digitised data of the STScI Digitised Sky Surveys</td><td>http://ledas- www.star.le. ac.uk/DSSimage</td></tr><tr><td>ELODIE archive</td><td>DSS and DSS-II More than 16 000 echelle spectrograms obtained with ELODIE at the Observatoire de</td><td>http://atlas.obs-hp.fr/ elodie/</td></tr><tr><td>ESO Science Archive Facility</td><td>Haute Provence Archives from all data obtained with ESO telescopes</td><td>http://archive.eso.org/</td></tr><tr><td>European Asteroidal Occultation</td><td>Observations of stellar occultations by asteroids in Europe since</td><td>http://www.euraster.net/</td></tr><tr><td>Results European Pulsar Network Data</td><td>1997 Measurements of pulsar profiles</td><td>http://www.mpifr-bonn. mpg.de/old_mpifr/div/</td></tr><tr><td>Archive Extrasolar Planets</td><td>Catalogue of all extrasolar planets</td><td>pulsar/data/ http://exoplanet.eu/</td></tr><tr><td>Encyclopedia Galactic Classical</td><td>discovered up to now List of all known population I Cepheids in our Galaxy</td><td>http://www.astro.utoronto ca/DDO/research/</td></tr><tr><td>Cepheid Database High Energy</td><td>Archives from several high energy</td><td>cepheids/ http://heasarc.gsfc.nasa.</td></tr><tr><td>Astrophysics Science Archive Research Center</td><td>space missions</td><td>gov/</td></tr><tr><td>Hypercat</td><td>Interface foracces to several extragalactic databases</td><td>http://www-obs.univ- lyon1.fr/hypercat/</td></tr></table>

(continued)

(continued)   

<table><tr><td>Nom</td><td>Description</td><td>URL</td></tr><tr><td>INTErnational Real-time MAGnetic</td><td>Data and information relating to magnetic observatories</td><td>http://www.intermagnet. org/</td></tr><tr><td>Observatory NETwork InfraRed Science</td><td>DatafromNASA's infrared and</td><td>http://irsa.ipac.caltech.edu/</td></tr><tr><td>Archive Italian Database of</td><td>millimetre missions Around 280 catalogues developed</td><td>http://db.ira.cnr.it/dira2/</td></tr><tr><td>Astronomical Catalogues LEicester Database</td><td>since 1984 by the Astronet group in Italy Access to data from high energy</td><td>http://ledas- www.star.le.</td></tr><tr><td>and Archive Service Libraries of stellar</td><td>space missions like EXOSAT and ROSAT Catalogue of stellar spectra</td><td>ac.uk/ http://www.ucm.es/info/</td></tr><tr><td>spectra McMaster Cepheid</td><td>Photometric and radial velocity data</td><td>Astrof/invest/actividad/ spectra.html http://www.physics.</td></tr><tr><td>Photometry and Radial Velocity Archive</td><td>from galactic and extragalactic Cepheids</td><td></td></tr><tr><td>Minor Planet Center Multimission Archive</td><td>Astrometric data and orbits of comets and small objects A wide range of astronphysical</td><td>http://minorplanetcenter. net/ http://archive.stsci.edu/</td></tr><tr><td>at STScI</td><td>archives,mainly in the optical, near-infrared,and UV regions</td><td>mast.html</td></tr><tr><td>NASA National Space Science Data Center</td><td>36 Tb of digital data from 440 NASA space missions</td><td>http://nssdc.gsfc.nasa.gov/</td></tr><tr><td>NASA/IPAC Extragalactic Database</td><td>Access to a large amount of published extragalactic data</td><td>http://nedwww.ipac. caltech.edu/</td></tr><tr><td>NCSA Astronomy Digital Image Library</td><td>Collection of astronomical images in FITS format</td><td>http://www.dlib.org/dlib/ october97/adil/ 10plante.html</td></tr><tr><td>Open Cluster Database</td><td>Information on more than 100 000 stars belonging to about 500 open clusters</td><td>http://www.univie.ac.at/ webda/</td></tr><tr><td>POLLUX database of stellar spectra</td><td>High-resolution optical stellar spectra</td><td>http://pollux.graal.univ- montp2.fr/</td></tr><tr><td>SDSS</td><td>Access to data from the SDSS extragalactic sky survey</td><td> http://www.sdss.org</td></tr><tr><td>SkyCat</td><td>Tool developed at the ESO for visualising images and accessing astronomical catalogues</td><td>http://archive.eso.org/ skycat/</td></tr><tr><td>TOPbase at CDS: The Opacity</td><td>Energy levels of the most abundant elements in astrophysics</td><td>http://cdsweb.u-strasbg.fr/ topbase/topbase.html</td></tr><tr><td>UK Astronomy Data Centre</td><td>Selection of data obtained by Earth-based telescopes in the UK</td><td>http://casu.ast.cam.ac.uk/ casuadc</td></tr><tr><td>VizieR Catalogue Service</td><td>Access to a complete library of published astronomical</td><td>http://vizier.u-strasbg.fr/</td></tr><tr><td>Washington Double Star Catalog</td><td>catalogues Main astrometric database of double and multiple star systems</td><td>http://ad.usno.navy.mil/ wds/wds.html</td></tr><tr><td>Wide Field Plate Database</td><td>Descriptive information about wide field photographic data stored in several places around the world</td><td>http://www.skyarchive. org/</td></tr><tr><td>XMM-Newton catalogue interface</td><td>Public interface providing access to the catalogue of sources observed byXMM-Newton</td><td>http://xcatdb.u-strasbg.fr/</td></tr></table>

# E.4 Journals

<table><tr><td>Name</td><td>URL</td></tr><tr><td>Acta Astronomica</td><td>http://acta.astrouw.edu.pl/</td></tr><tr><td>Annual Reviews of Astronomy and Astrophysics</td><td>http://www.annualreviews.org/journal/astro</td></tr><tr><td>ASP Conference Series</td><td>http://www.astrosociety.org/pubs/cs/confseries.html</td></tr><tr><td>Astronomical Journal</td><td>http://iopscience.iop.org/1538-3881</td></tr><tr><td>Astronomy&amp; Geophysics</td><td>http://www.blackwellpublishing.com/journals/AAG/</td></tr><tr><td>Astronomy and Astrophysics</td><td>http://www.aanda.org/</td></tr><tr><td>Astrophysical Journal</td><td>http://iopscience.iop.org/0004-637X/</td></tr><tr><td>Astrophysical Journal Supplement</td><td>http://iopscience.iop.org/0067-0049/</td></tr><tr><td>Astrophysics and Space Science</td><td>http://www.wkap.nl/journalhome.htm/0oo4-640X</td></tr><tr><td>Cambridge University Press</td><td>http://www.cup.cam.ac.uk</td></tr><tr><td>Classical and Quantum Gravity</td><td>http://www.iop.org/Journals/cq/</td></tr><tr><td>ESO Publications</td><td>http://www.eso.org/gen-fac/pubs/</td></tr><tr><td>IAU publications</td><td>http://www.iau.org/science/publications/iau/</td></tr><tr><td>Icarus</td><td>http://icarus.cornell.edu</td></tr><tr><td>Journal of Astronomical Data</td><td>http://www.vub.ac.be/STER/JAD/jad.htm</td></tr><tr><td>Journal of Cosmology and Astroparticle Physics</td><td>http://www.iop.org/EJ/journal/JCAP/</td></tr><tr><td>Journal of Optics A :Pure and Applied Optics</td><td>http://www.iop.org/Journals/oa</td></tr><tr><td>Journal of the British Astronomical Association</td><td>http://www.britastro.org/journal/</td></tr><tr><td>Monthly Notices of the Royal</td><td>http://www.blackwellpublishing.com/journal.asp?</td></tr><tr><td>Astronomical Society Nature</td><td>ref=0035-8711 http://www.nature.com/</td></tr><tr><td>Observatory Magazine</td><td>http://www.ulo.ucl.ac.uk/obsmag/</td></tr><tr><td>Optics Express</td><td>http://www.opticsexpress.org/</td></tr><tr><td>Physical Review Letters</td><td>http://prl.aps.org/</td></tr><tr><td>Publications of the Astronomical Society of Australia</td><td>http://www.publish.csiro.au/nid/138.htm</td></tr><tr><td>Publications of the Astronomical Society of Japan</td><td>http://pasj.asj.or.jp/</td></tr><tr><td>Publications of the Astronomical Society of the Pacific.Electronic Edition</td><td>http://www.journals.uchicago.edu/PASP/journal/</td></tr><tr><td></td><td>http://pasp.phys.uvic.ca/</td></tr><tr><td>Science</td><td>http://www.sciencemag.org/</td></tr></table>

# E.5 Bibliographical Research

<table><tr><td>Name</td><td>URL</td></tr><tr><td>Astrophysics Data System</td><td> http://adswww.harvard.edu/</td></tr><tr><td>E-print archive in Astrophysics (astro-ph, arXiv)</td><td>http://arxiv.org/archive/astro-ph/</td></tr></table>

# E.6 Image Sources

<table><tr><td>Name</td><td>Description</td><td>URL</td></tr><tr><td>APM Galaxy Survey</td><td>About 2 million galaxies</td><td>http://www.nottingham.ac. uk/~ppzsjm/apm/apm. html</td></tr><tr><td>Astronomy Picture of the Day</td><td>A different astronomical image for everyday of the week</td><td>http://antwrp.gsfc.nasa. gov/apod/astropix.html</td></tr><tr><td>Big Bear Solar Observatory CCD Images of</td><td>Images of the Sunat several wavelengths,updated each day Images ofMessier objects obtained</td><td>http://www.bbso.njit.edu/ http://zebu.uoregon.edu/</td></tr><tr><td>Messier Objects Center forEarth and</td><td>with several instruments Alarge collection of images of</td><td>messier.html http://www.nasm.si.edu/</td></tr><tr><td>Planetary Studies Color Stereo Photos</td><td>planets in the Solar System</td><td>ceps/ http://astro.uchicago.edu/</td></tr><tr><td>of Mars from the 2004 Rovers</td><td>Images of the surface of Mars</td><td>cosmus/projects/ marsstereo/</td></tr></table>

(continued)

(continued)   

<table><tr><td>Name</td><td>Description</td><td>URL</td></tr><tr><td>Digital Archive of Historical Astronomy</td><td>Collection of historical images</td><td>http://www42.pair.com/ infolund/bolaget/ DAHAP/</td></tr><tr><td>Pictures ESO Photo Gallery. Astronomical</td><td>Images obtained with ESO telescopes</td><td>http://www.eso.org/ outreach/gallery/astro/</td></tr><tr><td>Images Galaxy Zoo</td><td>Project for classifying a large</td><td>http://www.galaxyzoo.org/</td></tr><tr><td>Hubble Heritage</td><td>number of nearby galaxies Large collection of images obtained</td><td>http://heritage.stsci.edu/</td></tr><tr><td>Project Hubble Space Telescope</td><td>with the Hubble Space Telescope Images from the Hubble Space</td><td>http://hubblesite.org/ gallery/</td></tr><tr><td>picture gallery Infrared Space Observatory</td><td>Telescope Images from the ISO satellite</td><td>http://iso.esac.esa.int/</td></tr><tr><td>Science Gallery IPAC Image Gallery</td><td>Images fromseveral infrared space</td><td>http://coolcosmos.ipac. caltech.edu/image_</td></tr><tr><td>JPL Planetary</td><td>Images of the Solar System</td><td>galleries/missions_ gallery.html http://photojournal.jpl.</td></tr><tr><td>Photojournal Messier Pages at</td><td>Images of the Messier catalogue</td><td>nasa.gov/ http://www.seds.org/</td></tr><tr><td>SEDS Multiwavelength</td><td>Images of several nearby galaxies at</td><td>messier/ http://astronomy.swin.edu.</td></tr><tr><td>Atlas of Galaxies Multiwavelength</td><td>several wavelengths Images of the Milky Wayat several</td><td>au/staff/gmackie/atlas/ atlas_edu.html http://mwmw.gsfc.nasa.</td></tr><tr><td>Milky Way NASA JSC Digital Image</td><td>wavelengths Images from several NASA missions</td><td>gov/ http://images.jsc.nasa.gov/</td></tr><tr><td>Collection NOAO Image</td><td>Images obtained with the NOAO</td><td>http://www.noao.edu/</td></tr><tr><td>Gallery NSSDC Photo Gallery</td><td>telescope Collection of images classified in terms of the type of astrophysical</td><td>image-gallery/ http://nssdc.gsfc.nasa.gov/ photo_gallery/</td></tr><tr><td>Radio Galaxy and Quasar</td><td>object Images of extragalactic radio sources obtained with the VLA</td><td>photogallery.html http://www.cv.nrao.edu/~ abridle/images.htm</td></tr><tr><td>Images Two Micron All Sky Survey</td><td>Images from the 2MASS survey</td><td>http://www.ipac.caltech. edu/2mass/gallery/</td></tr></table>

# E.7 Education

<table><tr><td>Name</td><td>Description</td><td>URL</td></tr><tr><td colspan="3">Associations and Organisations</td></tr><tr><td>Astronomical Society of the Pacific</td><td>Education in astronomy</td><td>http://www.astrosociety.org/</td></tr><tr><td>European Association for Astronomy Education</td><td>Association with the aim of encouraging and propagating astronomy</td><td>http://www.eaae-astro.org/</td></tr><tr><td>Hands On Universe</td><td>Educational programme for students to learn about the Universe</td><td>http://www.handsonuniverse. org/</td></tr><tr><td colspan="3">Educational Sites</td></tr><tr><td>A website for popularization of Astrophysics and</td><td>Several basis lessons in astronomy</td><td>http://www.astrophysical. org/</td></tr><tr><td>Astronomy A knowledge for extragalactic astronomy and cosmology</td><td>Documents around the theme of extragalactic astronomy</td><td>http://nedwww.ipac.caltech. edu/level5/</td></tr><tr><td>Astrocentral</td><td>Popularisation</td><td>http://www.astrocentral.co. uk</td></tr><tr><td>Atlas of the Universe</td><td>Overview of the Universe on different scales</td><td>http://www. atlasoftheuniverse.com/</td></tr><tr><td>Constellations and Their Stars</td><td>A page for each constellation</td><td>http://www.astro.wisc.edu/~ dolan/constellations/</td></tr><tr><td>Curious About Astronomy?Ask an Astronomer</td><td>Site for asking professional astronomers questions</td><td>http://curious.astro.cornell. edu/</td></tr><tr><td>Falling into a Black Hole</td><td>Some information about the physics of</td><td>http://casa.colorado.edu/~</td></tr><tr><td>Imagine the Universe</td><td>black holes Astronomical site for children</td><td>ajsh/schw.shtml http://imagine.gsfc.nasa.gov/</td></tr><tr><td>Infrared Astronomy Tutorial</td><td>On the subject of infrared astronomy</td><td>http://colcosmos.ipac. caltech.edu/</td></tr><tr><td>MAP Introduction to Cosmology Page</td><td>Introduction to cosmology</td><td>http://map.gsfc.nasa.gov/m_ uni.html</td></tr><tr><td>NASA Spacelink</td><td>NASA's outreach site</td><td>http://www.nasa.gov/ audience/foreducators/ index.html</td></tr><tr><td>Ned Wright's Cosmology</td><td>Lectures on cosmology</td><td>http://www.astro.ucla.edu/~ wright/cosmolog.htm</td></tr><tr><td>Tutorial sci.astro Frequently Asked Questions</td><td>Answers to frequently asked questions</td><td>http://sciastro.astronomy.net/</td></tr><tr><td>Science Fiction Stories Using</td><td>Introduction to astrophysics through science fiction</td><td>http://www.astrosociety.org/ education/resources/scif.</td></tr><tr><td>Good Astronomy Space Time Travel</td><td>Illustrations by simulations of predictions from general relativity</td><td>html http://www.spacetimetravel.</td></tr><tr><td>StarChild</td><td>Basic lessons for children</td><td>http://starchild.gsfc.nasa.gov/</td></tr><tr><td>Windows to the Universe</td><td>General astronomy site</td><td>http://www.windows.ucar. edu/</td></tr><tr><td>History of astronomy</td><td></td><td></td></tr><tr><td>Astronomiae Historia</td><td>General history of astronomy</td><td>http://www.astro.uni-bonn. de/~pbrosche/astoria.html</td></tr><tr><td>Galileo Project</td><td>Information about Galileo</td><td>http://www.rice.edu/Galileo/</td></tr></table>

# E.8 Computing and Astronomy

<table><tr><td>Description</td><td>URL</td></tr><tr><td>Work environment</td><td></td></tr><tr><td>Basic UNIX commands</td><td>http://mally.stanford.edu/~sr/computing/basic-unix.html</td></tr><tr><td>Word processing</td><td></td></tr><tr><td>LTEX</td><td>http://www.latex-project.org/</td></tr><tr><td>An introduction to LTEX</td><td>http://www.maths.tcd.ie/~dwilkins/LaTeXPrimer/</td></tr><tr><td>LIEX mathematical symbols</td><td>http://web.ift.uib.no/Fysisk/Teori/KURS/WRK/TeX/ symALL.html</td></tr><tr><td>Text editors (programming)</td><td></td></tr><tr><td>Emacs</td><td>http://www.gnu.org/software/emacs/</td></tr><tr><td>An introduction to Emacs</td><td>http://www2.lib.uchicago.edu/~keith//tcl-course/emacs- tutorial.html</td></tr><tr><td>IDL under Emacs</td><td>http://idlwave.org/</td></tr><tr><td>Data processing software</td><td></td></tr><tr><td>Matlab</td><td>http://mathworks.com</td></tr><tr><td>Octave (Free version of Matlab)</td><td>http://www.gnu.org/software/octave/</td></tr><tr><td>IDL</td><td>http://www.ittvis.com/index.asp</td></tr><tr><td>An introduction to IDL</td><td>http://nstx.pppl.gov/nstx/Software/IDL/idl_intro.html</td></tr><tr><td>Library of IDL routines astronomy</td><td>http://idlastro.gsfc.nasa.gov/contents.html</td></tr><tr><td>GDL (Free Version of IDL)</td><td>http://gnudatalanguage.sourceforge.net/</td></tr><tr><td>IRAF</td><td>http://iraf.noao.edu/</td></tr><tr><td>Python</td><td>http://www.python.org/</td></tr><tr><td>TOPCAT</td><td>http://www.star.bris.ac.uk/~mbt/topcat/</td></tr><tr><td>Graphics</td><td></td></tr><tr><td>Gnuplot</td><td>http://www.gnuplot.info/</td></tr><tr><td>SuperMongo</td><td>http://www.astro.princeton.edu/~rhl/sm/</td></tr></table>

# E.9 Resources

<table><tr><td>Name</td><td>URL</td></tr><tr><td>Astronomical Internet Resources</td><td>http://www.stsci.edu/resources/</td></tr><tr><td>Astronomy resources on the Internet</td><td>http://www.cv.nrao.edu/fits/www/astronomy.html</td></tr><tr><td>AstroWeb at CDS: yellow-page services</td><td>http://cdsweb.u-strasbg.fr/astroweb.html</td></tr><tr><td>WebStars</td><td>http://heasarc.gsfc.nasa.gov/docs/www_info/webstars. html</td></tr></table>

# Appendix F Acronyms

For improved readability, most of these acronyms will be given in capital letters.

AAT Anglo-Australian Telescope   
ACS Advanced Camera for Surveys   
AIC Achromatic Interferential Coronagraphy   
AIPS Astronomical Image Processing System   
ALMA Atacama Large Millimeter Array   
a.m. ante meridiem   
AMANDA Antartic Muon And Neutrino Detector Array   
AMBER Astronomical Multi-Beam Combiner   
ANTARES Astronomy with a Neutrino Telescope and Abyss environmental Research   
ASIC Application Specific Integrated Circuit   
AVO Astronomical Virtual Observatory   
AXAF Advanced X-ray Astronomical Facility   
BAT Burst Alert Telescope   
BATSE Burst And Transient Source Experiment   
BDL Bureau des Longitudes   
BIB Blocked Impurity Band   
BIH Bureau International de l’Heure   
BIMA Berkeley Illinois Maryland Array   
BIPM Bureau International des Poids et Mesures   
CAD Computer Aided Design   
CARMA Combined Array for Research in Millimeter-wave Astronomy   
CAT Cherenkov Array at Themis   
CCD Charge Coupled Device   
CDA Centre de Donnees Astronomiques (Strasbourg) ´   
CEA Commissariat a l’ \` Energie Atomique (France) ´   
CFHT Canada–France–Hawaii Telescope   
CFRS Canada–France Redshift Survey   
CHARA Center for High Angular Resolution Astronomy   
CIA   
CIAXE   
CIB   
CID INECA

Coronographe Interferom´ etrique Achromatique Ax´ e´ Cosmic Infrared Background Charge Injection Device Consorzio Interuniversitario per il Calcolo Automatico dell’Ita Nord Orientale LV Center-to-Limb Variation MA Channel Multiplier Array MB Cosmic Microwave Background MOS Complementary Metal Oxide Semiconductor NES Centre National d’Etudes Spatiales (France)´ NOC Canadian Network for Observational Cosmology NRS Centre National de la Recherche Scientifique (France) OAST Cambridge Optical Array Synthesis Telescope OB Cosmic Optical Background OBE COsmic Background Experiment OMBO Classifying Objects by Medium Band Observation OROT Convection, Rotation, et Transits planetaires ´ RIRES Cryogenic High Resolution Infrared Echelle Spectrograph SO CalTech Submillimeter Observatory ARA Deutsche Agentur f¨ur Raumfahrt Angelegenheiten (Germany) AT Digital Audio Tape EIMOS Deep Imaging Multi-Object Spectrograph ENIS Deep Near Infrared Survey IMM Differential Monitor IVA Deutsches Interferometer f¨ur Vielkanalphotometrie und Astrometrie Deutsches Luft- und Raumfahrt DORIS Determination d’Orbite et ´ Radiopositionnement Integr ´ e par ´ Satellite QE Detector Quantum Efficiency RO Direct Read Out SB Double Side Band UMAND Deep Underwater Muon And Neutrino Detector VR Direct Voltage Readout BCCD Electron Bombarded Charge Coupled Device BS Electron Bombarded Silicon CU European Currency Unit GO European Gravitation Observatory GRET Energetic Gamma-Ray Experiment Telescope LT Extremely Large Telescope -ELT European Extremely Large Telescope SA European Space Agency SO European Southern Observatory SRF European Synchrotron Research Facility

DLR

ET Ephemeris Time   
EUV Extreme Ultra Violet   
EVN European VLBI Network   
FAME Full Sky Astrometric Mapping Explorer   
FET Field Effect Transistor   
FFT Fast Fourier Transform   
FGRS (2D) Field Galaxy Redshift Survey   
FIRAS Far InfraRed Astronomical Spectrometer   
FIRST Far InfraRed Space Telescope   
FK Fundamental Katalog   
FOC Faint Object Camera (Hubble)   
FORS Focal Reducer and Spectrograph   
FP Fabry–Perot   
FT Fourier Transform   
FTS Fourier Transform Spectrometer   
FU Flux Unit   
FUSE Far Ultraviolet Spectroscopic Explorer   
FWHM Full Width at Half Maximum   
GAIA Global Space Astrometry   
GALLEX Gallium Experiment   
GHz Gigahertz   
GI2T Grand Interferom´ etre\` a deux T\` elescopes´   
GLAO Ground Layer Adaptive Optics   
GLAST Gamma-ray Large Area Space Telescope   
GLONASS GLObal’naya NAvigatsionnaya Sputnikovaya Sistema   
GMRT Giant Meter Radio Telescope   
GNO Gallium Neutrino Observatory   
GPS Global Positioning System   
HALCA Highly Advanced Laboratory for Communications and Astronomy   
HARPS High Accuracy Radial velocity Planet Searcher   
HCRF Hipparcos Celestial Reference Frame   
HDF Hubble Deep Field   
HEAO High Energy Astronomical Observatory   
HEB Hot Electron Bolometer   
HEMT High Electron Mobility Transistor   
HESS High Energy Stereoscopic System   
HETG High Energy Transmission Spectrometer   
HIPPARCOS HIgh Precision PARallax COllecting Satellite   
HPBW Half Power Beam Width   
HRS High Resolution Spectrograph (Hubble Space Telescope)   
HST Hubble Space Telescope   
HURA Hexagonal Uniform Redundant Array   
IAU International Astronomical Union   
IBC Impurity Band Conduction   
IBIS Imager on Board Integral

ICRF ICRS IDL IDRIS

International Celestial Reference Frame   
International Celestial Reference System   
Interactive Data Language   
Institut du Developpement et des Ressources en Infor´   
Scientifique (France)   
Intermediate Frequency   
Institut National des Sciences de l’Univers (France)   
Infrared Optical Telescope Array   
Image Photon Counting System   
Infrared   
Infrared Camera   
Image Reduction and Analysis Facility   
Institut de RadioAstronomie Millimetrique (France) ´   
InfraRed Astronomy Satellite   
Integral Soft Gamma Ray Imager   
Infrared Spatial Interferometer   
Interstellar Medium   
Infrared Space Observatory   
International Space Station   
International Ultraviolet Explorer   
James Clerk Maxwell Telescope   
Julian Day   
Junction Supraconducting Effect Transistor   
James Webb Space Telescope   
Kuiper Airborne Observatory   
Keck Interferometer   
Large Meter Optical Spectroscopy Telescope   
Large Binocular Telescope   
Laser Guide Star   
LIght Detection And Ranging   
Laser Interferometer Gravitational wave Observatory   
Large Interferometric Space Antenna   
Local Oscillator   
Low Frequency Array   
Least Squares   
Local Standard of Rest   
Local Thermodynamic Equilibrium   
Multi Application Curvature Adaptive Optics   
Machine A Mesurer pour l’Astronomie (France) \`   
See WMAP   
Micro Arcsecond X-ray Imaging Mission   
Multi Conjugate Adaptive Optics   
Maximum Entropy Method   
Micro Electro Mechanical System   
Magnetohydrodynamic   
IF   
INSU   
IOTA   
IPCS   
IR   
IRAC   
IRAF   
IRAM   
IRAS   
ISGRI   
ISI   
ISM   
ISO   
ISS   
IUE   
JCMT   
JD   
JSET   
JWST   
KAO   
KI   
LAMOST   
LBT   
LGS   
LIDAR   
LIGO   
LISA   
LO   
LOFAR   
LS   
LSR   
LTE   
MACAO   
MAMA   
MAP   
MAXIM   
MCAO   
MEM   
MEMS   
MHD   
MIDAS M¨unich Interactive Data Analysis System   
MIDI Mid-Infrared Interferometric Instrument   
MIRA Mitaka Optical InfraRed Interferometer   
MIS Metal Insulator Semiconductor   
MISTRAL Myopic Edge-Preserving Image Restoration Method, with Application to Astronomical Adaptive-Optics-Corrected Long-Exposure Images   
ML Maximum Likelihood   
MMT MultiMirror Telescope   
MOS Metal Oxide Semiconductor   
MPG Max-Planck Gesellschaft   
MRO Magdalena Ridge Observatory   
MTF Modulation Transfer Function   
MURA Modified Uniform Redundant Array   
NACO NAOS-Conica   
NAOS Nasmyth Adaptive Optics System   
NASA National Aeronautic and Space Administration (USA)   
NASDA National Air and Space Development Agency (Japan)   
NBS National Bureau of Standards   
NEC Noise Equivalent Charge   
NEF Noise Equivalent Flux   
NEMO Neutrino Ettore Majorana Observatory   
NEP Noise Equivalent Power   
NESTOR Neutrino Extended Submarine Telescope with Oceanographic Research   
NGC New General Catalog   
NGS Natural Guide Star   
NICMOS Near Infrared Camera for Multi-Object Spectrograph   
NOAO National Optical Astronomy Observatory (USA)   
NPOI Navy Prototype Optical Interferometer   
NRAO National RadioAstronomy Observatory (USA)   
NSF National Science Foundation   
NSO National Solar Observatory   
NTT New Technology Telescope   
OAO Orbiting Astronomical Observatory   
OECD Organisation for Economic Cooperation and Development   
OHANA Optical Hawaiian Array for Nanoradian Astronomy   
OVLA Optical Very Large Array   
OVRO Owens Valley Radio Observatory   
PACS Photodetector Array Camera and Spectrometer (Herschel missi   
PAPA Precision Analog Photon Address   
PC Photoconductor   
p.d. Potential difference   
PIAA Phase Induced Amplitude Apodization   
PICSIT Pixelated CsI Telescope (Integral mission)   
PM PhotoMultiplier   
p.m. post meridiem   
PMM Precision Measuring Machine   
POSS Palomar Optical Sky Survey   
POST POlar Stratospheric Telescope   
ppb Parts per billion   
ppm Parts per million   
PSD Power Spectral Density   
PSD Pulse Shape Discrimination   
PSF Point Spread Function   
PSR Pulsar   
PSS Palomar Sky Survey   
QSO QuasiStellar Object (quasar)   
RADAR RAdio Detection and Ranging   
RENATER Reseau National de la Recherche et de la Technologie (France)´   
RF Radiofrequency   
RGS Resolution Grating Spectrometer (X-ray mission)   
RISC Reduced Instruction Set Computer   
rms Root mean square   
ROSAT Roentgen Space Astronomical Telescope   
ROSITA Roentgen Survey with an Imaging Telescope on the ISS   
SAGE Russian American Gallium Experiment   
SALT South African Large Telescope   
SAO Smithsonian Astronomical Observatory   
SCIDAR SCIntillation Detection and Ranging   
SDSS Sloane Digital Sky Survey   
SEC Secondary Electron Conduction   
SERC Science and Engineering Research Council (UK)   
SIM Space Interferometry Mission   
SIN Superconductor Insulator Normal   
SINFONI Spectrograph for Integral Field Observation in the Near Infrared   
SIS Superconductor Insulator Superconductor   
SIT Silicon Intensified Target   
SKA Square Kilometer Array   
SMA SubMillimeter Array   
SNO Sudbury Neutrino Observatory   
SNR SuperNova Remnant   
SNU Solar Neutrino Unit   
SODAR Sonic Detection And Ranging   
SOFIA Stratospheric Observatory for Far Infrared Astronomy   
SOHO Space HelioSpheric Observatory   
SPAN Space Physics Analysis Network   
SPI Spectrometer on Integral $\gamma$ -ray mission)   
SPIRE Spectral and Photometric Imaging Receiver   
SPOT Satellite Probatoire d’Observation de la Terre   
SQUID Superconducting Quantum Interference Device   
SSB Single Side Band   
SSPM Solid State PhotoMultiplier   
STJ Superconducting Tunnel Junction   
STP Standard Temperature Pressure   
TAI Temps Atomique International   
TCP Transmission Control Protocol   
TDRSS Transmission Data and Relay Satellite System   
THz Terahertz   
TIMMI Thermal Infrared MultiMode Instrument   
TMT Thirty Meter Telescope   
TPF Terrestrial Planet Finder   
TV Television   
UCAC USNO CCD Astrograph Catalog   
UHF UltraHigh Frequency   
UKIRT United Kingdom InfraRed Telescope   
USNO United States Naval Observatory   
UT Universal Time   
UTC Universal Time Coordinated   
UV UltraViolet   
UVES UltraViolet Echelle Spectrograph   
VESPA Versatile Spectrometer Assembly   
VIMOS Visible Multiple Object Spectrograph   
VISIR VLT Imager and Spectrometer in the InfraRed   
VLA Very Large Array   
VLBI Very Long Baseline Interferometry   
VLT Very Large Telescope   
VLTI Very Large Telescope Interferometer   
VSOP VLBI Space Observatory Program   
VVDS VIMOS VLT Deep Survey   
WFPC Wide Field Planetary Camera   
WMAP Wilkinson Microwave Anisotropy Probe   
XMM X-ray Multimirror Mission   
ZIMPOL Zurich Imaging Polarimeter   
ZOG Zero Order Grating

# Bibliography

Since this book is intended as a reference, only a very limited number of books or papers have been cited, and then explicitly. The present bibliography, like the webography, supplements these references with books and review articles considered to be of fundamental importance. They are organised here by theme, with headings and subheadings that do not necessarily correspond to chapter titles in the book. We have not included atlases, which can be found in the CFHT bibliography below.

The general bibliographic sources to follow can be consulted by a highly efficient search using key words. These sources sometimes require a password, which must be obtained through a university library:

Base enterBooks.com. Bibliographic search for books, with access in French, English, or Spanish. Online address: www.enterbooks.com.   
Libraries of the European Southern Observatory (ESO). An exceptional collection of books and professional review. Online address: http://libhost.hq.eso.org:8088/uhtbin/webcat. SAO/NASA Database: Astrophysics Data System — Centre de donnees astronomiques de ´ Strasbourg (CDS). Access to all scientific journals for the professional astronomer. Online address: http://cdsads.u-strasbg.fr.   
Bibliographic Data at the Centre national de la recherche scientifique (CNRS) — Institut national des sciences de l’univers (INSU). Access to sources and open archives (HAL, ArXiv). Online address: http://biblioplanets.inist.fr.

Since the tools and methods of astronomical observation are changing fast, many useful references do not feature in didactic works, but appear rather in conference proceedings. The latter provide up-to-date results and original contributions, but do not always have the synoptic value of a textbook, nor the same level of refereeing as in a peer-reviewed journal. However, it is worth listing some particularly important organisations, to be cited generically under the more detailed subject headings below:

Experimental Astronomy. A good refereed review, published by Springer and bringing together publications on experimental aspects of astronomical observation.   
European Astronomical Society Publication Series (EAS). This series began in 2001 and can be accessed online at www.eas-journal.org.   
Astronomical Society of the Pacific Conference Series (ASP). All titles published since 2003 are available as e-books at the address www.aspbooks.org.   
Society of Photographic Instrumentation Engineers (SPIE). Professional and commercial society founded in the USA in 1955. Only the acronym is used today. Among other things, the SPIE Digital Library contains a section entitled Astronomy and Astronomical 0ptics, bringing together a large number of conference proceedings at very different levels but

well up to date, dealing with astronomical observation both on the ground and from space, telescopes, their instrumentation, and so on. The sections entitled Electronic Imaging and Processing and Optics and Electro-optics may also provide useful information. Online address: spiedigitallibrary.aip.org/.

# General References

Annual Review of Astronomy and Astrophysics. Annual Reviews Series. Annual volume published since 1963, containing a dozen review articles, generally excellent. The state of the art in observational techniques and methods is often described. This reference is denoted by ARAA (volume, page, year) in this book and in the bibliographic references below.

The Astronomy & Astrophysics Review, Springer, Berlin. European equivalent of the previous, published since 1989, edited by Th. Courvoisier in the form of several volumes each year. This contains few review articles on observation in astronomy.

The Astronomy & Astrophysics Encyclopædia, Maran S.P. Ed., Van Nostrand, New York, 1992.   
An excellent synopsis, with detailed discussions and bibliography for all astrophysical themes.   
Also discusses the main observational tools.

Encyclopedia of Astronomy and Astrophysics, Murdin, P. Ed., 4 vol., Institute of Physics, London, 2001. High-quality, up-to-date professional encyclopedia, available at http://eaa.crcexpress.com.

ALLEN C.W., Astrophysical Quantities, Cox, A. Ed. Springer, 4th edn., 2000. Defines key quantities and provides numerical values of useful constants. This is a basic reference for any astronomer, denoted by AQ in this book.

HARWIT M., Astrophysical Concepts, Springer, 2000. An excellent reference book, presenting the main physical concepts used in astrophysics.

HEYVAERTS, J., Astrophysique. Etoiles, univers et relativit ´ e, Dunod, Paris, 2006. An excellent ´ astrophysics manual at MSc and doctoral levels, with exercises.

LANG K.R., Astrophysical Formulae, Astronomy & Astrophysics Library, Springer, 3rd edn., 1999, 2 volumes, reprinted in 2006. A compendium of basic physical tools used in the main astrophysical problems. This standard reference is denoted by AF in this book.

PECKER J.C., SCHATZMAN E., Astrophysique gen´ erale, Masson, Paris, 1959. Standard but ´ sometimes out-of-date reference work. The section on observation gives a good description of conventional astronomy in the 1960s.

# Historical Works

HAWKING, S., On the Shoulders of Giants, Running Press, 2003. The main foundational texts of astronomy.

HOCKEY, T. et al. The Biographical Encyclopedia of Astronomers, Springer, 2 volumes, 2007. This book contains more than a thousand biographical descriptions of astronomers, from historical times to the present day.

LANG K.R., GINGERICH O., A Source Book in Astronomy and Astrophysics 1900–1975, Harvard University Press, 1979. Collection of key papers, reporting particularly on the considerable progress made in observational methods and associated discoveries.

VERDET J.P., Astronomie et astrophysique, Larousse, Paris, 1993. Collection of key papers, with comments and historical context.

WALLERSTEIN G., OKE J.B., The First 50 Years at Palomar, 1949–1999, Another View: Instruments, Spectroscopy, and Spectrophotometry in the Infrared, ARAA 38, 113–141, 2000.

Most annual volumes of the ARAA begin with an article in which an eminent astronomer, usually American, gives a personal account of his or her life of research and contributions. These portrayals thus form part of the rich history of twentieth century astronomy.

# Terminology

HECK A., Star Briefs 2001: A Dictionnary of Abbreviations, Acronyms, and Symbols in Astronomy and Related Space Sciences, Kluwer, 2000..

HOPKINS J., Glossary of Astronomy and Astrophysics, University of Chicago Press, 2nd edn., 1980. Rather physically oriented introduction to English and American terminology.

LANG K.R., A Companion to Astronomy and Astrophysics: Chronology and Glossary with Data Tables, Springer, 2006.

Desktop Publishing in Astronomy and Space Sciences, Heck A. Ed., World Scientific Publishing, Singapore, 1992.

HECK A., HOUZIAUX L. Future Professional Communication in Astronomy, Academie royale ´ de Belgique, 2007. Detailed analysis of the way publication has evolved with the advent of digital communications.

# Research Policy in Astronomy

HECK A. Star Guides 2001: A Worldwide Directory of Organizations in Astronomy, Related Space Sciences and Other Related Fields, Kluwer, 2003. An invaluable practical guide to all centres of research and observation, with references, addresses, and so on.

Cosmic Vision 2015–2025, European Space Agency 2008, www.esa.int/esaCP/index.html. Conclusions concerning orientations and choices for the ESA’s astronomical space missions in the specified decade.

Towards a Strategic Plan for European Astronomy, Astronet European Network, 2006. Document available at www.astronet-eu.org, and also published as a book (see next item). The result of a wide-ranging consultation on the aims and means of both ground-based and spaceborne European astronomy.

DE ZEEUW T., A Science Vision for European Astronomy, Astronet, 2007.

WOLTJER L., Europe’s Quest for the Universe, EDP, Paris, 2006. A comprehensive overview of the rebirth of European astronomy in the second half of the twentieth century, both on the ground and in space.

OECD Science, Technology, and Industry Outlook, OECD, Paris, 2010. Annual review of the main trends in public policy in member countries of the OECD.

UNESCO Science Report 2010, UNESCO, Paris, 2010. Global picture of scientific development in the world, and in particular in astronomy.

New Worlds, New Horizons in Astronomy and Astrophysics, National Academies (USA), National Academic Press, 2010. Guidelines for Earth-based and spaceborne astronomy in the USA, prepared every ten years.

JAXA Vision — JAXA 2025. Japan Aerospace Exploration Agency, Tokyo, 2005, available online at www.jaxa.jp/about/2025/index e.html. Prospects for the Japanese space programme.

Les sciences spatiales: Adapter la recherche franc¸aise aux enjeux de l’espace, Academie des´ sciences (France), Report no. 30, ed. by Puget J.L., EDP Sciences, Paris, 2010. Overview of the development of space research in France and Europe.

Long Range Plan 2010 for Canadian Astronomy and Astrophysics, National Research Council of Canada, www.casca.ca/lrp2010/index.php, 2010. Guidelines for Earth-based and spaceborne astronomy in Canada, prepared every ten years.

# Observation in Astrophysics

Modern Technology and Its Influence in Astronomy, Wall J.V. & Boksenberg A. Eds., Cambridge University Press, New York, 1990. Collective work describing trends in imaging and radiation detection.

Compendium of Practical Astronomy, Roth G.D. Ed., Vols. I, II, and III, Springer-Verlag, New York, 1994. Extremely comprehensive textbook built up from individual contributions with many references. The first volume is more specifically devoted to observation, its tools, and its techniques.

BRADT H., Astronomy Methods, Cambridge University Press, 2004.

HARWIT M., Cosmic Discovery: The Search, Scope, and Heritage of Astronomy, MIT Press, 1984. Excellent book, showing in particular how observational capabilities have conditioned astrophysical discovery.

KITCHIN C.R., Astrophysical Techniques, Taylor & Francis, 4th edn., 2003.

Exploring the Cosmic Frontier: Astrophysical Instruments for the 21st Century, Lobanov A.P. et al (Eds.), Springer, 2008.

WILSON T.L., ROHLFS K., HITTEMEISTER S., Tools of Radio Astronomy, 5th edn., Astronomy and Astrophysics Library, Springer-Verlag, New York, 2009.

SMITH R.C., Observational Astrophysics, Cambridge University Press 1995. This book ‘borrowed’ the title of the original book by LENA, P., published by Springer in 1988.

SPIE Digital Library. Instrumentation in Astronomy, CDP27. Two CDROMs presenting a set of particularly significant papers in this area, appearing in the SPIE volumes, 2002.

# Astronomical Photometry

BESSELL M.S., Standard Photometric Systems, ARAA 43, 293–336, 2005.

BUDDING E. & DEMIRCAN O., Introduction to Astronomical Photometry, 2nd edn., Cambridge University Press, 2007.

STERKEN C. & MANFROID J., Astronomical Photometry: A Guide, Kluwer, 1992. Clear and comprehensive reference.

TINBERGEN J., Astronomical Polarimetry, Cambridge University Press, 1996.

# Terrestrial Atmosphere

# Structure and Properties

VALLEY S., Handbook of Geophysics and Space Environnement, McGraw-Hill, New York, 1965. A good general reference for all properties and numerical values associated with the atmosphere and space environment of the Earth.

HOUGHTON J.T., The Physics of the Atmosphere, Cambridge University Press, 1977. Excellent introductory monograph on the physics and dynamics of the atmosphere.

HUMPHREYS W.J., Physics of the Air, Dover Publishing Inc., 1964. Old textbook (1920), but in a more recent edition that contains a good elementary description of many meteorological and atmospheric phenomena.

SALBY M.L. Fundamentals of Atmospheric Physics, International Geophysics Series, Vol. 61, Academic Press, New York, 1996. Excellent didactic book on the fundamental properties of the Earth atmosphere.

# Atmospheric and Interplanetary Radiation

GOODY R.M., Atmospheric Radiation, Cambridge University Press, 1977.

McCORMAC B.M., The Radiating Atmosphere, Reidel, Dordrecht, 1971.

REACH F.E. & GORDON J.L., The Light of the Night Sky, Reidel, Dordrecht, 1973.

Optics of Cosmic Dust, Videen G., Kocifaj M. (Eds.), NATO Workshop, Kluwer, 2002.

Interplanetary Dust, Gr¨un E., Gustafson B.A.S., Dermott S., et al. (Eds.), Springer, 2001.

Scattering in the Atmosphere (Selected Papers on), S.P.I.E. MS 07, 1989. A collection of fundamental articles on atmospheric scattering.

SPIE Digital Library. See the volumes of conference proceedings in the section on Atmospheric Sciences.

# Transmission of Electromagnetic Radiation

Atlases of the solar spectrum obtained with very high resolutions also identify telluric lines.

The Infrared Handbook. US Govt. Print. Off., Washington, 1979. Although outdated, this remains an excellent reference for theory and practice in the region $1 { - } 1 0 0 0 \mu \mathrm { m }$ .

MIGEOTTE M., NEVEN L., SWENSSON J., Le Spectre Solaire de 2.8 a\` $2 3 . 7 ~ \mu \mathrm { m }$ , Mem. Soc.´ Roy. Sc. Liege \` 2, 1957.

DELBOUILLE L., ROLAND G., BRAULT J., TESTERMAN L., Spectre solaire de $1 8 5 0 \ \mathrm { \texthat { a } }$ $1 0 0 0 0 \mathrm { c m } ^ { - 1 }$ , Universite de Li´ ege, 1981.\`

WALLACE L., HINKLE K., LIVINGSTON W., An Atlas of the Photospheric Spectrum (735– $1 1 2 3 \mathrm { n m }$ ), National Solar Observatory, Tucson, 1994.

# Atmospheric Turbulence

The Journal of Atmospheric Sciences contains research directly relating to atmospheric properties.   
For many other references, see also under the heading Adaptive Optics and Radioastronomy.

LESIEUR M., Turbulence in Fluids, 4th edn., revised and updated, Springer, 2007.

LUMLEY J.L. & PANOFSKY H.A., The Structure of Atmospheric Turbulence, Interscience, Paris, 1964.

# Astronomical Sites on Earth

Astronomical Site Evaluation in the Visible and Radio Range, Vernin J., Benkhaldoun Z., Munoz-˜ Tunon C. Eds., ASP Series vol. 266, 2002.˜

ARENA — Large Astronomical Infrastructures at CONCORDIA. Prospects and Constraints for Antarctic Optical & Infrared Astronomy, Candidi M., Epchtein N. Eds., EAS Series vol. 25, EDP, Paris, 2007.

A Vision for European Astronomy and Astrophysics at the Antarctic station CONCORDIA Dome C in the next decade 2010–2020. The ARENA Consortium, Epchtein N. Ed., arena.unice.fr, 2009.

Dome C Astronomy & Astrophysics Meeting, Giard M., Casoli F., Paletou F. (Eds.), EAS Series, vol. 14, EDP, 2005.

The Protection of Astronomical and Geophysical Sites, Kovalevsky J. Ed., Editions Frontieres,\` Gif-sur-Yvette, 1992.

ABAHAMID A., VERNIN J., BENKHALDOUN Z., Seeing, outer scale of optical turbulence, and coherence outer scale at different astronomical sites using instruments on meteorological balloons, Astron. Astrophys. 422, 1123, 2004. Interesting article for site comparisons.

GARSTANG R.H., The status and prospects for ground-based observatory sites, ARAA 27, 19–40, 1989.

# Spaceborne Observation

# Space Missions

This is not the place to give an exhaustive bibliography of spaceborne observation. The reader can consult the initial reports and feasibility studies published by the European Space Agency and other large space agencies (USA, Japan, China, Russia, etc.) whenever a new mission is under study or new guidelines are being established. See the webography for more details.

SPIE Digital Library. See the volumes of conference proceedings in the sections entitled Astronomy, Astronomical Instrumentation, Space Technologies.

# Moon-Based Observation

Towards a World Strategy for the Exploration and Utilization of our Natural Satellite, European Space Agency SP-1170, 1994.

Astrophysics from the Moon, Mumma M.J. & Smith H.J. Eds., AIP Proceedings 207, Amer. Inst.   
Phys., 1990.

# Spatial and Temporal Reference Systems

AUDOIN C., GUINOT B., LYLE S. (transl.), The Measurement of Time: Time, Frequency, and the Atomic Clock, Cambridge University Press, 2001. This book discusses the ideas and techniques involved in time measurement and the establishment of time scales.

GREEN R.M., Spherical Astronomy, Cambridge University Press, 1985. Very good and up-to-date elementary textbook, with vector formulations and taking into account relativistic effects.

KOVALEVSKY J., Modern Astrometry, 2nd edn., Astronomy and Astrophysics Library, Springer-Verlag, 2002. Recent, general work covering in some detail the many aspects of astrometry, such as image formation, instrumentation, and data compression.

KOVALEVSKY J. & SEIDELMAN P.K., Fundamentals of Astrometry, Cambridge University Press, 2004. For advanced students. The most recent textbook on current astrometry, including the most recent conventions of the International Astronomical Union.

MIGNARD F., LES echelles de temps, Introduction aux Eph ´ em´ erides Astronomiques, Connais- ´ sance des temps, Chap. 2, EDP Sciences. Updated annually in Connaissance des temps.

MURRAY C.A., Vectorial Astrometry, Adam Hilger, Bristol, 1983. This book deals above all with the relevant concepts in a very general relativistic framework which makes it difficult to follow. However, the reader’s efforts will be rewarded by the quality of the contents.

VANIER J. and AUDOIN C., The Quantum Physics of Atomic Frequency Standards, Adam Hilger, Bristol, 1989. The most comprehensive book on the physics of frequency standards. High level.

WALTER H.G., SOVERS O.J., Astrometry of Fundamental Catalogues, Springer, 2000. Monograph discussing the underlying ideas and construction of fundamental catalogues, with a detailed presentation of FK5, the Hipparcos Catalogue, and the ICRF with the VLBI technique.

The Hipparcos Mission, SP-1111, European Space Agency, 1989. Three volumes published for the launch of Hipparcos, describing the instrument, preparation and contents of the initial catalogue, and compression methods.

The Hipparcos Catalogue, SP-1200, European Space Agency, 1997. Final publication of the Hipparcos Catalogue. Volume 1 specifies the properties of the catalogue and volume 3 presents all the data processing techniques.

Reference Frames in Astronomy and Geophysics, Kovalevsky J., Mueller I.I. & Kolaczek B. Eds., Kluwer Academic Publishers, 1989. About twenty synoptic papers written by the best specialists, making a real pedagogical effort. The work covers celestial and terrestrial reference systems, the relationships between these systems, and also temporal reference systems.

High-Accuracy Timing and Positional Astronomy, van Paradijs J. & Maitzen H.M. Eds. Lecture Notes in Physics 418, Springer-Verlag, New York, 1993. Excellent didactic book resulting from the European Astrophysical Doctoral Network (EADN).

GAIA: A European Space Project, ESA Publication Series 2, O. Bienayme & C. Turon Eds., EDP´ 2002. Report from a Les Houches School on the GAIA mission and its scientific objectives.

GAIA: Composition, Formation and Evolution of the Galaxy, ESA-SCI(2000)4, 2000. Official document containing the scientific proposal for the GAIA mission, and providing a lot of information about the current situation and issues in stellar and galactic physics.

# Telescopes

BAARS J.W.M., The Paraboloidal Reflector Antenna in Radio Astronomy and Communication.   
Theory and Practice, Springer, 2007.

BELY P., The Design and Construction of Large Optical Telescopes, Springer, 2003. Excellent introductory work on new telescopes in the twenty-first century.

DANJON A. & COUDER A., Lunettes et Telescopes, Blanchard, Pa´ ris, 1983. Re-edition of an excellent classical textbook on visible observation.

KING H.C., The History of the Telescope, Dover Publish. Inc., New York, 2nd edn. 1977. Excellent historical introduction.

KITCHIN C., Solar Observing Techniques, Springer, 2002. Telescopes and instruments for observing the Sun.

LEMAITRE G., Astronomical Optics and Elasticity Theory: Active Optics Methods, Springer, 2010. Basic principles of active optics.

Astronomical Optics (selected papers on), Schroeder D. Ed., MS 73, 1993. A collection of fundamental historical articles on optical astronomy (telescopes, interferometers, turbulence, etc.), from 1920 to the present day.

ROHLFS K. & WILSON T.L., Tools of Radio Astronomy, Springer, 2004. Telescopes and instrumentation used in radio astronomy.

WILSON R.W., Reflecting Telescope Optics I. Basic Design, Theory and Its historical Developments, 2nd revised edn., Springer, 2007.

WILSON R.W., Reflecting Telescope Optics II. Manufacture, Testing, Alignement, Modern techniques, Springer, 2001. Two fundamental works dealing with the design and construction of optical telescopes.

SPIE Digital Library. See the volumes of conference proceedings in the sections entitled Astronomical Instrumentation, Astronomy.

# Optics and Image Formation

BORN M. & WOLF E., Principles of Optics, Pergamon Press, Oxford, 6th edn., 1980. Fundamental reference book, especially for the formalism of geometric or wave optics, the complete theory of diffraction, etc. Also contains the general principles of interferometers, e.g., Michelson, Fabry–Perot, particularly useful in the ultraviolet, visible, infrared, and submillimetre regions.


<!-- chunk 0011: pages 701-724 -->
BRUHAT G. & KASTLER A., Optique, Masson, Paris, 1954, 6th edn. dating from 1965. Key textbook, although sometimes out of date.

GOODMAN J.W., Introduction to Fourier Optics, 3rd edn., Roberts & Co., 2005. Excellent reference.

HARBURN G., TAYLOR C.A. & WELBERRY T.R., Atlas of Optical Transforms, Bell, 1975.   
Useful depictions of Fourier transforms.

HARVEY A.F., Coherent Light, Wiley, New York, 1970. A particularly clear discussion of issues relating to radiation coherence.

HECHT E., Optics: International Edition, Pearson Education, 4th edn. 2003. Excellent book with a very comprehensive didactic introduction to optics.

MERTZ L., Transformations in Optics, Wiley, New York, 1965. Original work, with many direct references to astronomy.

SCHNEIDER P., EHLERS J. & FALCO E.E., Gravitational Lenses, Springer, 1992, reprinted 1999.

Handbook of Optics, vols. I and II, Bass M. Ed., McGraw-Hill, 2001. Reference book discussing all features of image formation, light sources, and light detectors used in astronomy.

# Guided Optics

AGRAWAL G., Nonlinear Fiber Optics, 3rd edn., Academic Press, 2006.

BUCK J.A., Fundamentals of Optical Fibers, Wiley, New York, 1995. Reference work on all aspects of optical fibres.

HEACOX W.D. & CONNES P., Astronomy & Astrophysics Review 3, 169, 1992.

YOUNG M., Optics and Lasers, Fibers and Optical Waveguides, Springer, 2000.

# Image Formation in Turbulent Media

GOODMAN J.W., Statistical Optics, Wiley, New York, 1985. The main reference book for imaging in random media and partial coherence properties of radiation.

RODDIER F., The Effects of Atmospheric Turbulence in Optical Astronomy, Progress in Optics XIX, 281, 1981. Old paper but of fundamental importance, clearly describing the formalism and the main results needed to understand the effects of the atmosphere on light propagation.

TATARSKI V.I., Wave Propagation in Turbulent Media, Dover Publ. Inc., New York, 1961.   
Standard work on the physics of wave propagation in random media.

WOOLF N.J., High Resolution Imaging from the Ground, ARAA 20, 367, 1982. Motivations and techniques leading to the construction of very large ground-based telescopes in the 1980s.

# Adaptive Optics

Adaptive Optics for Astronomy, Alloin D.M. & Mariotti J.-M. Eds., NATO-ASI Series 423, 1994.

Adaptive Optics in Astronomy, Roddier F. Ed., Cambridge University Press, 1999. Basic work for the study of adaptive optics.

BECKERS J., Adaptive Optics for Astronomy: Principles, Performances, and Applications, ARAA 31, 13–62, 1993. A review written early in the development of adaptive optics.

HUBIN N., MAX C.E., WIZINOWICH P., Adaptive Optics Systems, SPIE, 2008. A compendium of the state of the art in this technique, as applied to astronomy.

TYSON R.K., Principles of Adaptive Optics, Academic Press, 1991.

SPIE Digital Library. See the volumes of conference proceedings under the heading Adaptive Optics.

# High Dynamic Range Imaging

Optical techniques for direct imaging of exoplanets, C. R. Acad. Sc. 8, 273–380, Aime C. Ed., 2007.

Astronomy with High Contrast Imaging II, Aime C. Ed., European Astronomical Society Publ., vol. 12, 2004.

BRACEWELL R.N., Detecting non-solar planets by spinning infrared interferometer, Nature 274, 780, 1978. The original idea for nulling interferometry.

JACQUINOT P., ROIZEN-DOSSIER B., Prog. Opt. 3, 31, 1964. Fundamental historical paper.

LYOT B., ZEIT. F. Astrophys. 5, 73, 1932. Key historical paper.

# Interferometry

# Radio Interferometry

CORNWELL T.J. & PERLEY R.A., Radio Interferometry: Theory, Techniques, Applications, American Society of the Pacific Conference Series 19, 1991.

HALL P.J. Ed., The Square Kilometer Array: An Engineering Perspective, Springer, 2004.

KELLERMANN K.I., MORAN J.M., The development of high-resolution imaging in radioastronomy, ARAA 39, 457–509, 2001.

THOMSON A.R., MORAN J.M. & SWENSON G.W., Interferometry and Synthesis in Radioastronomy, Wiley, New York, 1986. Standard work for the study of imaging in radioastronomy.

WILSON T.L. & HUTTEMEISTER S., Tools of Radio Astronomy. Problems and Solutions, ¨ Springer, 2005.

Subarcsecond Radioastronomy, Davis R.J. & Booth R.S. Eds., Cambridge University Press, 1993.

# Optical Interferometry

ALLOIN D.M. & MARIOTTI J.M., Diffraction-Limited Imaging with Large Telescopes, NATO ASI Series 274, Kluwer Academic Publishers, Dordrecht, 1989. Lectures from a summer school, providing a didactic introduction at the beginnings of adaptive optics and optical interferometry.

FELLI M. & SPENCER R.E., Very Long Baseline Interferometry: Techniques and Applications, Reidel, Dordrecht, 1989.

GLINDEMAN A., Principles of Stellar Interferometry, Astronomy and Astrophysics Library, Springer, 2011. Standard reference for optical interferometry, and especially the setting up of the European VLT.

HANBURY-BROWN R., Photons, Galaxies, and Stars (selected papers on), Indian Academy of Science, Bangalore, 1985. Collection of original papers on optical interferometry by photon correlation.

LABEYRIE A., LIPSON S.G., NISENSON P., An Introduction to Optical Stellar Interferometry, Cambridge University Press, 2006.

LAWSON P., Principles of Long-baseline Stellar Interferometry, Wiley Blackwell, 2010.

QUIRRENBACH A., Optical Interferometry, ARAA 39, 353–401, 2001.

SAHA S.K., Aperture Synthesis: Methods and Applications to Optical Astronomy, Astronomy and Astrophysics Library, Springer, 2010.

SHAO M. & COLAVITA M.M., Long Baseline Optical and Infrared Stellar Interferometry, ARAA 30, 457–498, 1992.

The Power of Optical & Infrared Interferometry: Recent Scientific Results, Paresce F., Richichi A., Delplancke F. & Chelli A. (Eds.), Springer, 2008.

SPIE Digital Library. See the volumes of conference proceedings under the heading Astronomical Instrumentation.

# Detectors and Receivers

# General Features

COHEN-TANNOUDJI C., DUPONT-ROC J., GRYNBERG G., Photons et atomes. Introduction l’electrodynamique quantique, EDP, Paris, 1987. ´

COHEN-TANNOUDJI C., DUPONT-ROC J., GRYNBERG G., Processus d’interaction entre photons et atomes, EDP, Paris, 1996.

GRYNBERG G., ASPECT A., FABRE C., Introduction to Quantum Optics: From the Semi-Classical Approach to Quantized Light, Cambridge University Press, 2010.

HARRIS A.I., Coherent Detection at Millimetric Waves and Their Application, Nova Science Publ., Conmack, 1991.

KITTEL C., Introduction to Solid State Physics, Wiley, 8th edn., 2004. Essential source for the basics of solid state physics, relevant to most radiation detectors in all energy regions.

LAMARRE J.M., Photon noise in photometric instruments at far infrared and submillimeter wavelengths, Appl. Opt. 25, 870–876, 1986.

LANDAU L., LIFSHITZ E.M., Statistical Physics, 3rd edn., Part I, Course on Theoretical Physics, Vol. 5, Butterworth–Heinemann, 1980.

PITAEVSKII L.P., LIFSHITZ E.M., Statistical Physics, Part 2, Course on Theoretical Physics, Vol. 9, Butterworth–Heinemann, 1980.

LONGAIR M., High Energy Astrophysics, vol. I, Particles, Photons and Their Detection, Cambridge University Press, 1992. Very comprehensive textbook, including a section on the ultraviolet to radiofrequency regions and associated techniques. Good bibliography.

MACKAY C.D., Charge coupled devices in astronomy, ARAA 24, 255–283, 1986.

MATHER J., Bolometer noise: Non-equilibrium theory, Appl. Opt. 21, 1125, 1982. Detailed analysis of thermal noise.

OLIVIER B.M., Thermal and quantum noise, Proc. IEEE 53, 436, 1965.

RIEKE G.H., Detection of Light from the Ultraviolet to the Submillimeter, Cambridge University Press, 1994. Synoptic view of light detection, written by an astronomer for researchers.

SZE S.M., Physics of Semiconductor Devices, Wiley, New York, 1981. This can be considered as the basic reference for all aspects of semiconductor physics.

# Radiofrequencies

PHILIPS T.G. & WOODY D.P., Millimeter and submillimeter wave receivers, ARAA 20, 285, 1982.

ROBINSON B., Frequency allocation: The first forty years, ARAA 37, 65–96, 1999.

# Infrared and Submillimeter

Millimetric Astronomy, Les Houches, Winter Workshop, March 1990, Nova science Publ., New York, 1991. Millimetre and submillimetre detectors.

The Infrared and Electro-optical Systems Handbook, Accetta & Shumaker Executive Eds., copubl.   
ERIM and SPIE, 1993. Eight volumes.

The Infrared Handbook. US Govt. Print. Off., Washington, 1985. Although somewhat out of date, still an excellent reference work for theory and practice in the region $1 { - } 1 0 0 0 \mu \mathrm { m }$ .

LOW F.J., RIEKE G., GEHRZ R.D., The beginning of modern infrared astronomy, ARAA 45, 43–65, 2007. Up-to-date discussion by the pioneers in this area.

RIEKE G., Infrared dectector arrays for astronomy, ARAA 45, 77–115, 2007.

WOLSTENCROFT R.D. & BURTON W.B., Millimeter & Submillimeter Astronomy, Kluwer Academic Publishers, New York, 1988.

# Visible and CCD Detectors

Astronomy with Schmidt-Type Telescopes, Capaccioli M. Ed., Reidel, Dordrecht, 1984. General review of the uses of photographic plates and the photography of faint objects.

BUIL C., CCD Astronomy: Construction and Use of an Astronomical CCD Camera, Willmann– Bell, 1991.

HOWELL S.B., Handbook of CCD Astronomy, Cambridge University Press, 2006.

JANESICK J.R., Scientific Charge-Coupled Devices, SPIE, Bellingham, 2001.

McLEAN I.S., Modern Instrumentation in Astronomy, Springer-Verlag, New York, 1989. High quality textbook on CCDs.

# Ultraviolet

BOWYER S., DRAKE J.J., VENNES S., Extreme ultraviolet astronomy, ARAA 38, 231–288, 2000.

# X-Ray Astronomy

BEIERSDORFER P., Laboratory X-ray astrophysics, ARAA 41, 343–390, 2003.

BRANDT H.V.D., OHASHI T. & POUNDS K.A., X-ray astronomy missions, ARAA 30, 391– 427, 1992.

GIACCONI R. & GURSKY H., X-Ray Astronomy, Reidel, Dordrecht, 1974.

PAERELS F.B.S., KAHN S.M., High resolution X-ray spectroscopy with Chandra and XMM– Newton, ARAA 41, 291–342, 2003.

TRUMPER J., ROSAT, Physica Scripta ¨ T7, 209–215, 1984. Detailed description of the X-ray astronomy mission (Roentgen Satellite). ¨

# Gamma-Ray Astronomy

DEBERTIN K. & HELMER R.G., Gamma-Ray and X-Ray Spectrometry with Semiconductor Detectors, Elsevier Science Publishers, North-Holland, 1988.

Towards a Major Atmospheric Cerenkov Detector for TeV Astro/particle Physics, Fleury P. & Vacanti G. Eds., Editions Fronti´ eres, Gif-sur Yvette, 1992.\`

GILMORE G., HEMINGWAY J., Practical Gamma-Ray Spectrometry, John Wiley & Sons, 1995.

Semiconductor Radiation Systems, K. Iniewski, CMOS Emerging Technologies Inc., Vancouver 2009.

KNOLL G.F., Radiation Detection and Measurement, Wiley, 1999. A standard reference.

LECOQ P., ANNENKOV, A., GEKTIN, A., KORZHIK, M., PEDRINI, C., Inorganic Scintillators for Detector Systems, Springer, 2006.

LUTZ G., Semiconductor Radiation Detector Device Physics, Springer, 1999.

RODNYI P., Physical Processes in Inorganic Scintillators, CRC Press, New York, 1997.

SPIELER H., Semiconductor Detector Systems, Oxford University Press 2005.

# Cosmic Rays

SCHLICKEISER R., Cosmic Ray Astrophysics, Springer, 2002.

# Neutrino Astronomy

ANSELMANT P. et al., Phys. Lett. B 285, 1992. Contains a discussion of solar neutrinos and their detection.

BAHCALL J.N., Highlights in Astrophysics: Concepts and Controversies, Shapiro S. & Tevkolsky S. Eds., Wiley, New York, 1985.

BAHCALL J.N. & DAVIS R., Essays in Nuclear Astrophysics, Cambridge University Press, 1982.

# Gravitational Astronomy

Gravitational Radiation, Deruelle N. & Piran T. Eds., Cours de l’Ecole de Physique Th ´ eorique des ´ Houches, North Holland, 1983.

HAKIM R., Gravitation relativiste, InterEditions, 1994. ´

SCHNEIDER P., EHLERS J. & FALCO E.E., Gravitational Lenses, Springer-Verlag, Heidelberg, 1991.

VINET J.-Y., Optical detection of gravitational waves, Compte-Rendus Acad.Sc. 8, 2007.

# Spectrometry

Precision Spectroscopy in Astrophysics, Santos N.C., Pasquini L., Correia A.C.M., Romaniello M.   
(Eds), Springer, 2008.

Next Generation Wide-Field Multi-Object Spectroscopy, Brown M.J., Dey A. (Eds.), PASP 2002.

AERTS C., CHRISTENSEN-DALSGAARD J., KURTZ D.W., Asteroseismology, Springer, 2008.

CHAFFEE F. & SCHROEDER D., Astronomical Applications of Echelle Spectroscopy, ARAA 14, 23, 1976.

CONNES P., Astronomical Fourier Spectroscopy, ARAA 8, 209, 1970. Comprehensive overview of Fourier spectroscopy.

JAMES J., Spectrograph Design Fundamentals, Cambridge University Press, 2007.

KITCHIN C.R., Optical Astronomical Spectroscopy, Institute of Physics, London, 1995.

TENNYSON J., Astronomical Spectroscopy. An Introduction to the Atomic and Molecular Physics of Astronomical Spectra, Imperial College Press, London, 2005.

SPIE Digital Library. See the volumes of conference proceedings in the section entitled Astronomical Instrumentation.

# Signal Processing

TASSI Ph., Methodes statistiques, Economica, Paris, 1985. Clear synopsis. ´

ANDREWS H.C. & HUNT B.R., Digital Image Restoration, Prentice Hall, 1977. Basic techniques of information restoration in image processing.

BIJAOUI A., Image et information: Introduction au traitement numerique des images, Masson, ´ Paris, 1981.

BLANC-LAPIERRE A. & FORTET R., Theorie des fonctions al´ eatoires, Masson, Paris, 1953.´

CLARKE R.J., Transform Coding of Images, Academic Press, Orlando, 1985. Standard reference for signal processing.

DAS P.K., Optical Signal Processing, Springer-Verlag, New York, 1991. Basics of optical signal processing.

KENDALL M. & STUART A., The Advanced Theory of Statistics, Vols. 1 and 2, Ch. Griffin & Co. Ltd., London & High Wycombe, 1977, 1979. Standard reference book for statistical treatment of data.

KENDALL M., STUART A. & ORD J.K., The Advanced Theory of Statistics, Vol. 3, Ch. Griffin & Co. Ltd., London & High Wycombe, 1983. Third and final part of this standard reference. Half the volume is devoted to time series.

LEVINE B., Fondements theoriques de la radiotechnique statistique, Vols. I, II, and III, Ed ´ itions Mir, Moscow 1973, 1973, 1976. A remarkable, didactic introductory text, but unfortunately out of print.

MAX J., Methodes et techniques de traitement du signal et applications aux mesures physiques, ´ Masson, Paris, 4th edn., 1985–1987. This can be considered as a basic reference on noise-affected measurement.

NARAYAN R. & NITYANANDA R., Maximum entropy image restoration in astronomy, ARAA 24, 127–170, 1986.

PAPOULIS A., Probability, Random Variables, and Stochastic Processes, McGraw-Hill, New York, 3rd edn., 1991. Standard reference for random variables and stochastic processes, including proofs and applications to physics.

PUETTER R.C., GOSNELL T.R., YAHIL A., Digital image reconstruction: Deblurring and denoising, ARAA 43, 139–194, 2005.

STARCK J.-L., MURTAGH F., Astronomical Image and Data Analysis, Springer, 2006.

# Inverse Problems

TITTERINGTON D.M., General structure of regularization procedures in image reconstruction, Astron. & Astrophys. 144, 381–387.

DEMOMENT G., Image reconstruction and restoration: Overview of common estimation structures and problems, IEEE Trans. Acoust. Speech Signal Process 37 (12), 2024–2036, December 1989.

Bayesian Approach to Inverse Problems, Idier J., Ed., ISTE, London, 2008

MUGNIER L.M., BLANC A., Idier J., Phase diversity: A technique for wavefront sensing and for diffraction-limited imaging, In Hawkes P., ed., Advances in Imaging and Electron Physics, vol. 141, Chap. 1, pp. 1–76, Elsevier, 2006.

MUGNIER L.M., LE BESNERAIS G., MEIMON S., Inverse problems in optical imaging through atmospheric turbulence, In Idier J., Ed., Bayesian Approach for Inverse Problems, Chap. 10. ISTE, London, 2008.

STIGLER, S.M., Gauss and the invention of least squares, Annals of Statistics 9 (3), 465–474, May 1981.

# Data Processing and Archiving

Astronomy from Large Data Bases II, Heck A. & Murtagh F. Eds., European Southern Observatory Proc. 43, Garching, 1992.

Statistical Challenges in Modern Astronomy, Babu G.J. & Feigelson E.D. Eds., Springer-Verlag, New York, 1993

# Mathematics

BRACEWELL R.M., The Fourier Transform and Its Applications, McGraw-Hill, New York, 1965.   
An invaluable book for its wide range of exercises relating to astronomy and physics.

JAFFARD S., MEYER Y., RYAN R.D., Wavelets: Tools for Science and Technology, Society for Industrial Mathematics, 2001.

RODDIER F., Distributions et transformation de Fourier, Ediscience, Paris, 1971.

SCHWARTZ L., Mathematics for the Physical Sciences, Dover, 2008. Fundamental work for understanding optics and signal processing in astronomy.

Error, Bias, and Uncertainties in Astronomy, Jaschek C. & Murtagh F. Eds., Cambridge University Press, New York, 1990.

# Index

AB magnitude, 107   
Abbe’s condition, 200   
Aberration optical, 179 Seidel, 180 spherical, 180   
Absorption coefficient of, 443 spectrum, 443   
Abundance, 6, 453   
Acceptance of a fibre, 263   
Accretion, 21   
Acoustic spectrometer, 498   
Active optics, 181, 191   
Adaptive Fourier analysis, 632   
Adaptive optics, 240 extreme, 254 ground layer, 253 multi-conjugate, 252 multi-object, 254 NAOS, 536   
ADU, 538   
Aerosols, 76 scattering by, 59   
AIC, 308   
Air mass, 62   
Air shower, 71, 410   
Airglow, 50   
Airy function, 224 profile, 247   
Aladdin detector, 376   
Aladin database, 24, 616   
Aliasing, 522   
Alkali halide, 413   
Allocating frequencies, 76   
Altazimuth mount, 178, 192

AMANDA, 426   
Amateur astronomy, 29   
AMBER instrument, 289   
Amplitude detector, 325   
Analogue-to-digital converter (ADC), 519   
Anamorphic factor, 472   
Anastigmatic optics, 177   
Angel’s cross, 314   
Anglo-Australian Telescope (AAT), 190, 479   
Angular resolution, 23   
Anisoplanicity, 244   
Annihilation, 445   
Anomaly, South Atlantic, 83   
Antarctic, 76   
ANTARES, 426, 429   
Antenna temperature, 388   
Anticoincidence devices, 414   
Aperture, 12   
Aperture supersynthesis, 277   
Aperture synthesis, 227, 276   
APEX telescope, 501   
APM digitisation, 610   
Apodisation, 113, 225, 299, 305, 505   
Application specific integrated circuits (ASIC),   
527   
APS digitisation, 610   
Arecibo radiotelescope, 186   
Array of detectors, 365   
Artificial intelligence, 78   
Artificial reference star, 250   
Astigmatism, 180, 242   
Astrometry, 276   
VLBI, 149   
Astrophysical Virtual Observatory (AVO), 615   
Astrophysics Data System (ADS), 37   
Atacama Large Millimeter Array (ALMA), 74,   
282

Atmospheric constituents, 41 minor, 41 degradation of image, 228 refraction, 61 scattering, 58 transmission, 53 turbulence, 62   
Attenuation, 263   
Autocorrelation, 630, 631 of stochastic process, 646   
Autocovariance of stochastic process, 646   
Avalanche photodiode, 248, 363   
AXAF mission, 201   
Azimuthal angle, 132

Bragg–Fresnel lens, 201   
Brightness, reduced, 97   
Bunching, 104   
Bure interferometer, 281, 533   
Bureau des Longitudes, 157   
Bureau International de l’Heure, 164   
Bureau of Standards (US), 161

Baffle, 193   
Baikal telescope, 428   
Band gap, 345   
BAT, 207   
Bayes estimator, 553   
Bayes principle, 553   
BEAR, 488   
Bias, 517, 545, 547, 552, 555   
BIB detector, 377   
Bimorphic mirror, 245   
Bin, 337, 457   
Binning mode, 373   
Blackbody fluctuations, 100 radiation, 99   
Blaze, 466 angle, 466 wavelength, 466   
Blocked impurity band detector, 377   
Boiling, 70   
Bolometer, 383 germanium, 383 hot electron, 383, 385 superconducting, 385 X-ray, 386   
BOOMERANG mission, 197   
Bootstrap method, 559   
Bose–Einstein statistics, 104   
Bouguer’s line, 109   
Box function, 622 in two dimensions, 625   
Bracewell interferometer, 313   
Bragg diffraction, 206, 493 lens, 206 reflection, 498 spectrometer, 491   
Cadmium telluride, 419   
Caesium clocks, 158, 161   
Calar Alto telescope, 190, 251   
Calendar, 170   
Calibration, 110 angular, 110 energy, 110 gamma, 120 infrared, 114 radiofrequency, 110 spectral, 110, 117 time, 110 ultraviolet, X, 117 visible, 114   
Calorimeter, 355   
Caltech Submillimeter Observatory, 385   
Camera obscura, 202   
Capella, 294   
Carbon dioxide, 44   
Carcinotron, 396   
CARMA array, 281   
Carte du ciel, 606   
Cartesian coordinates, 129   
CASIMIR instrument, 501   
Cassegrain focus, 178   
Cat’s-eye mirror, 488   
Catalogue FK4, 146 FK5, 24, 146 GSC, 146 Hipparcos, 146, 152 PPM, 146 SAO, 146 Tycho, 146, 152 UCAC, 146   
Cauchy distribution, 573   
CCD astrograph catalog, 154 controller, 367, 372 format, 371 frame transfer, 368, 539 full frame, 368 intensified, 361 low light level, 372 readout noise, 370

thinned, 368 time delay integration, 549 windowing mode, 373 for X-ray detections, 372 CDS, 37 CELESTE, 411 Celestial sphere, 176 Central limit theorem, 643 Centre–limb darkening, 124 Cerenkov radiation, 71 CFH telescope, 190, 611 Chacaltaya site, 46 Chajnantor site, 73 Chandra mission, 493 Characteristic function of random variable, 641 Charge loss, 416 Cherenkov air shower, 411 Cherenkov effect, 353 Cherenkov radiation for neutrino detection, 424 Cherenkov telescope, 410 Chopping, 545 Chopping secondary mirror, 192 Chronometry, 110 CID detector, 366 Circadian cycle, 44 Citations, 37 CLEAN algorithm, 270 Clementine mission, 87 Clocks, stability of, 284 Cloud, 72 CMOS detector, 373 COBE satellite, 121, 198 Coded mask, 202, 541 Coding, image, 203 Coherence area of, 235, 236 complex degree of, 101 order n, 103 etendue,´ 211, 214, 333 length, 102 of radiation, 100 spatial, 101 temporal, 101 time, 101 Collimating mirror, 465 Colour indices, 108 Coma, 180, 242 Compton observatory, 207 Compton scattering, 202, 352, 412 Compton telescope, 407 Concordia Station, 77 Conduction band, 345 Confidence interval, 518, 642

Confusion noise, 607   
CONICA, 536   
Continuous spectrum, 443   
Contrast, 54   
Convective instability, 41   
Convergence of an estimator, 554   
Convolution, 626   
Cooper pairs, 349   
CORALIE, 474   
CORAVEL, 474   
Coronagraph   
AIC, 308   
Guyon, 308   
Kasdine–Spergel, 306   
visible nulling, 309   
Coronagraphic interferometer, 311   
Coronagraphy, 298, 299   
Coronography, 60   
COROT mission, 532, 538   
Correlation product, 629   
Correlator, 275   
Cosmic background radiation, 121   
Cosmic infrared background, 98   
Cosmic microwave background, 98   
Cosmic optical background, 98   
Cosmic rays, 5, 79, 85, 420   
on CCDs, 513   
Cosmic variance, 607   
Cosmological background, gravitational, 436   
Cosmological horizon, 9   
Cosmological window, 82   
COSMOS, 358   
Cost of equipment, 33   
Coude focus,´ 178   
Counting, 360   
photon, 361   
Coupler, 389   
Coupling efficiency, 263   
Crab Nebula, 205   
Cross talk, 363   
Cross-correlation, 629, 635   
Cross-power spectrum, 631   
Cross-spectral density, 631, 635   
Cross-validation, 525   
CSO telescope, 396   
Current–voltage characteristic, 401   
Curvature of focal plane, 183   
Curve of growth, 453   
Cutoff wavelength, 263   
Dark charge, 546   
Dark current, 359, 371, 512, 545   
Dark signal, 324

Darwin mission, 296   
Data, 35   
Data bank, 26   
Data compression, 26, 206, 527   
Data-processing software, 26   
Decision theory, 551   
Declination, 133   
Deconvolution, 459   
Defocus, 242   
Deformable mirror, 245   
Degeneracy factor, 104, 334   
Degree of confidence, 515   
Degree of freedom, 643   
Densified pupils, 291   
Densitometry, 330   
Depletion zone, 401   
Detection coherent, 325 of gamma rays, 412 of gravitational waves, 431 incoherent, 326 limit, 515 lock-in, 603 of radiofrequencies, 387 submillimetre, 326, 343, 355, 387 ultraviolet, 344, 368 video, 392 visible, 344 X rays, 328, 344   
Detector amplitude, 325 array, 365 CMOS, 373 format, 371, 382 hybrid, 373 multichannel, 328 quadratic, 325 single channel, 326   
Detector quantum efficiency (DQE), 356   
Diatomic molecule, 447   
Differential measurement, 56   
Diffraction, 210 Bragg, 206, 493 Fraunhofer, 216 Fresnel, 231, 321 at infinity, 216   
Diffuse cosmic background, 82   
Digital correlator, 601   
Digitisation, 519 step, 520   
Dilution refrigerator, 384   
Diode, avalanche, 363   
Dirac comb, 623

distribution, 623 distribution in two dimensions, 625 Direct voltage readout, 381 Dirty beam, 269 Dirty map, 269 Discharge tube, 111 Discrimination of weak source, 53 Dispersion corrector, 62 of a grating, 464 in optical fibre, 264 of random variable, 640 Distortion, 180 $\chi ^ { 2 }$ distribution, 643 Distribution function of random variable, 638 of stochastic process, 646 Dome C, 77 Dopant, 346 Doppler effect, 450 imaging, 451 lines, 453 profile, 453 width, 454 Double sideband reception (DSB), 394 DUMAND, 425 Dynamic range, 519

E-ELT, 194   
Earth’s atmosphere, 40   
EB-CCD tube, 248, 362, 363   
Ebert–Fastie mounting, 470   
Echellogram, 468   
Ecliptic, 136   
frame, 136   
inclination angle, 136   
Edison tasimeter, 375   
Effelsberg radiotelescope, 188   
EGRET instrument, 408   
Einstein effect, 452   
Einstein observatory, 199, 494   
Einstein ring, 519   
Electromagnetic spectrum, 4   
Electrometer, 350, 359   
Electron bombarded silicon (EBS) tube, 362   
Electronic camera, 360   
Electronic transitions, 444, 445   
fine structure, 446   
hyperfine structure, 446   
Electronographic tube, 360   
Emission spectrum, 443   
Emissivity, 112

Emittance, 96   
Emulsion density of, 358 nuclear, 350, 360   
End-to-end model, 532   
Ensemble average, 640   
Entropy of data, 527   
Epitaxy, 403 molecular, 402   
Equation of time, 160   
Equatorial frame, 134 mount, 178   
Equinox, 135   
Ergodicity of stochastic process, 651 of turbulence, 64   
Error function, 642   
ESRF, synchrotron, 201   
Estimation, 515, 550, 654 error, 551   
Estimator, 512, 551 biased, 568 convergence, 554 efficient, 564 of mean, 656 minimax, 554 reliable, 571 robust, 572 unbiased, 555, 655   
Etendue, 94, 211, 215, 457, 472   
Ethics, 37   
Euler angles, 137   
Event, 637   
EVN, 285   
Exhaustive statistic, 561   
EXOSAT mission, 493   
Exosat satellite, 201, 365   
Exozodi, 314   
Expectation value, 639   
Exposure time calculator, 532   
External scale of turbulence, 64, 2   
Extinction, 109 interstellar, 109   
Extrasolar planet, 296   
Extreme adaptive optics, 254   
Extremely large telescopes, 33   
FFT, 501   
Fibre graded-index, 263 multimode, 263 single-mode, 263 step-index, 263   
Field curvature, 180 fully illuminated, 180 of a telescope, 177 of view, 12 vignetted, 180   
Field derotator, 192   
Field effect transistor (FET), 367   
FIFI instrument, 379   
Figure of merit, 462   
Filling factor, geometrical, 329   
Filtering frequency, 652 online, 524 optimal, 523 of stochastic process, 652 time, 653   
Finesse of a spectrometer, 490   
Fisher information, 570 matrix, 571   
Fisher–Neyman criterion, 561   
Fizeau interferometry, 257, 291   
Flat field, 548   
Flop, 27   
Fluctuations, 332   
Fluorescence, 50   
Fluoride glasses, 263   
Flux unit, 96   
Flux, monochromatic, 95   
Focal ratio, 179 scale, 179   
Format of detector, 371, 382   
Fourier pairs, 627   
Fourier transform, 619   
Frame change of, 138 ecliptic, 136 equatorial, 134 galactic, 137 horizontal, 131 hour, 133   
Frechet inequality,´ 564   
Free spectral interval, 468, 490   
Frequency change, 494   
Frequency doubler, 396   
Frequency of random variable, 63

Fabry–Perot etalon,´ 490   
Factor analysis, 528   
Faint Object Camera, 362   
Fano factor, 417   
Fast Fourier transform, 501

Frequency standards, 161 atomic, 159 primary, 164   
Fresnel lens, 201   
Fried parameter, 233, 322   
Fringe tracker, 264, 289   
Fringe visibility, 102, 227   
Full width at half maximum (FWHM) of normal distribution, 642   
Fundamental catalogues, 145   
Fundamental plane, 130, 144   
FUSE mission, 195   
GMRT array, 278   
GPS, 285 satellite network, 284 time, 166   
Graham, Mount, 190   
Grain of photographic plate, 328, 350, 513   
Grating, 463 blazed, 466 dispersion of, 464 echelle, 466   
Gravitational lens, 184 optics, 175 telescope, 183 waves, 9 detection, 431 telescope, 431   
Greenbank radiotelescope, 501   
Gregorian calendar, 171   
Gregorian reform, 171   
Grism, 469   
Ground layer adaptive optics, 253   
GSPC, 364   
Gunn effect, 396   
Gurney–Mott theory, 350   
GAIA, 87, 155, 607 characteristics, 156 ICRF, 156   
Galactic background, 57 centre, 137 frame, 137 pole, 137   
GALEX mission, 195   
Galileo time, 166   
Gallium Neutrino Observatory (GNO), 422   
Gamma background noise, 514 burst telescope, 206 burster, 207 bursts, 20, 21, 206, 438 collimator, 407 detection, 412 function, 643 imaging, 202 instruments, 406 spectrometry, 412 telescopes, 201 transmission, 82   
Gaunt factor, 118   
Gauss–Markov theorem, 574   
Gaussian distribution, 642   
Gemini telescopes, 190   
Generalised inverse, 581   
Geocorona, 52   
Geodesics, 183   
Geodesy, space, 142   
Geometric optics, 177   
Geometric reference system, 147   
Germanium, 346   
Giant Meterwave Radio Telescope (GMRT), 74   
GIRAFFE spectrometer, 479   
Gladstone’s relation, 68   
GLAST mission, 408

Hadley cells, 72   
HALCA mission, 286   
Half power beam width, 222   
Harmonic generator, 396   
HARPS, 475   
spectroscopy, 474   
Hecht’s equation, 416, 440   
HEGRA instrument, 412   
Height, 132   
Heliosphere, 83   
Helium, 445, 450, 496   
HEMT, 397, 398   
Herschel mission, 87, 190, 198, 480, 501   
Hertzsprung–Russell diagram, 109   
HESS observatory, 411   
Heterodyne detection, 393   
Heterodyne interferometry, 260   
infrared, 287   
Heterojunction, 348   
HETG, 493   
HIFI, 385   
High dynamic range imaging, 298   
High Energy Stereoscopic System (HESS), 75   
High resolution spectrograph (HRS), 473   
Hipparcos   
catalogue, 146   
frame, 151

HCRF, 155 mission, 152, 607 satellite, 87 Hodges–Lehmann median, 573 Holographic etching, 468 Homodyne interferometry, 261 Horizontal frame, 131 Horn, 388 Hot electron bolometer (HEB), 383, 385, 401 Hot electron mixer, 400 Hour angle, 133 Hour frame, 133 HPBW, 222 Hubble Space Telescope (HST), 195, 612 HURA mask, 204 Hybrid array, 374 Hybrid detector, 373 Hybrid mapping, 273 Hydrogen atom, 444 maser, 284 molecular, 447 Hydrogen-like atom, 444, 445 Hygrometer, spectral, 56 Hyperfine structure, 445, 446 Hypersensitised photographic plate, 350 Hypertelescope, 291

spectrometry, 463, 486, 487, 490 telescopes, 192 transmission of, 46, 53, 73, 81 Instrumental MTF, 268 profile, 483 spectral, 456 signature, 544 Integral field spectroscopy (IFS), 461, 479 INTEGRAL mission, 206, 408, 541 spectrometer, 418 Integration time, 518 Intensity interferometry, 335 Intensity standards, 110 Interference filter, 463 grid, 463 Interferogram, 482 Interferometer intensity, 320 Michelson, 102 spectral, 481 Interferometry, 256 Bracewell, 313 coronagraphic, 311 differential, 238 direct, 257, 259 fibre, 292 Fizeau, 257, 291 heterodyne, 260 heterodyne infrared, 287 homodyne, 261 intensity, 335 Michelson, 259 nulling, 296, 311 pupil plane, 228 radio, 256 space-based, 294 speckle, 236 VLBI, 149, 282 X-ray, 297 Intermediate frequency (IF), 394 Internal scale of turbulence, 64 International Astronomical Union, 29, 148, 159, 169 Interplanetary dust, 80 Inversion layer, 40 subsidence, 72 temperature, 72 Ionosphere, 44 Ionospheric layers, 44 IRAC instrument, 376 IRAM millimetre interferometer, 533 IRAS mission, 197, 381, 607, 614

IBIS instrument, 408   
IBIS/ISGRI instrument, 541   
Ice, 448   
IceCube Neutrino Observatory, 426, 428   
ICRF, 148   
ICRS, 148   
Image agitation, 228 coding, 203 geometric, 177 intensifier, 360 long-exposure, 232 quality, 182 sampling, 222 short-exposure, 234 slicer, 473, 480   
Image–object relation, 218   
Impartiality, principle of, 553   
Impurity, 346   
Inertial range, 64   
Infrared detection, 339 imaging, 234 interferometry, 287 photometry, 108, 112

Irradiance, 95   
IRS, 501   
ISGRI, 206, 420   
ISI interferometer, 287   
ISO mission, 381, 608   
Isoplanatic   
angle, 237   
patch, 236   
Isoplanicity, 219   
IUE satellite, 25, 195, 467

Jackknife method, 560   
Jansky, 96   
JCMT radiotelescope, 186, 400   
Jensen inequality, 559   
Jet stream, 66   
Johnson noise, 382   
Joule–Thomson refrigerator, 374   
Julian calendar, 170 date, 170 day, 169   
Junction, 348   
JWST mission, 87, 195

Laser Interferometer Space Antenna (LISA),   
435   
Law of large numbers, 551, 654   
LBT, 190, 191, 194, 264, 291   
Lehmann–Scheffe theorem, 563   
Lepton, 7   
Lidar, 52   
Light interference, 547   
LIGO experiment, 432   
Likelihood function, 554   
Line of sight, 176   
Line spectrum, 443   
Lithium fluoride, 493   
Lithium niobate, 498   
Littrow condition, 466   
Lobe of radiotelescope, 389   
Local oscillator, 284, 389, 394   
Local Standard of Rest (LSR), 451   
Local thermodynamic equilibrium (LTE), 55,   
104   
LOFAR, 280   
Lorentz profile, 49, 455   
Loss function, 552   
Low light level (L3-CCD), 372   
Luminosity, 97   
monochromatic, 97   
Lunar occultation, 225   
Lyot coronagraph, 302   
Kamiokande, 424   
Karhunen–Loeve polynomials, \` 243, 528   
Kasdine–Spergel coronagraph, 306   
Keck interferometer, 289   
Keck telescopes, 190, 193   
Kepler mission, 296   
Kinematic reference system, 147   
Kirchoff–Fresnel relation, 217   
Kitt Peak, 73, 190   
Klein–Nishina formula, 352   
Klystron, 396   
Km3Net telescope, 431   
Kolmogorov turbulence, 64, 243   
Kuiper Airborne Observatory (KAO), 47, 196

MACAO, 247   
Mach’s principle, 148   
Magellan telescope, 194   
Magnetograph, 452, 481   
Magnetosphere, 79   
Magnitude, 104 AB, 107 absolute, 107 bolometric, 107 photometric, 106 STMAG, 107 systems, 106   
MAMA, 358, 610   
Maser amplifier, 398   
Maser line, 454   
Mauna Kea site, 55, 72, 73, 190   
MAXIM mission, 298   
Mean intensity, 96   
Mean of stochastic process, 646   
Mean squared error, 568   
Mean value, 640   
Median of random variable, 640   
MEGACAM, 371, 611   
MEMS, 245

La Palma site, 190   
La Silla site, 73, 190   
Labview, 531   
Lagrange equation, 183   
Lagrange points, 87   
Lallemand, A., 360   
Lambert’s law, 100   
LAMOST telescope, 191   
Large optical mirrors, 189   
construction of, 191   
Laser guide star, 248, 250, 480

Mercury iodide, 420   
Meridian, astronomical, 132   
Mesopause, 41   
Mesosphere, 41   
Meteorites, 6   
Meton cycle, 170   
Michelson interferometer, 102, 259 spectral, 481   
Microchannel plate, 360, 365   
Microdensitometer, 358   
Microlens array, 480   
MIDI instrument, 289   
Mie scattering, 59   
MilliCrab, 544   
Minimax principle, 554   
Minimax risk, 554   
Minimum variance bound, 566, 568   
Mixer, 349, 355, 387, 394, 399 hot electron, 400 noise temperature of, 391 SIS, 349   
Mixing ratio, 42   
Modulation transfer function detector, 328   
Modulation transfer function (MTF), 182, 220   
Modulation, rapid, 57   
Molecular aggregates, 448 laser, 396 transitions, 446   
Moliere scattering,\` 408   
Moments, 640   
Moon, 87 laser telemetry, 148   
MOS capacitance, 366   
Most probable value, 640   
Multi-object adaptive optics, 254   
Multi-object spectrometer, 461   
Multi-object spectroscopy (MOS), 475   
Multichannel detector, 328   
Multiplex advantage, 486 gain, 486   
Neutrino detection, 420 using Cherenkov radiation, 424 using chlorine, 421 using gallium, 422 using heavy water, 423 using indium, 423   
NICMOS detector, 376   
Nodding, 545   
Noise, 511, 512 background, 339, 512 gamma, 514 thermal, 513 detector, 512 diode, 111 Gaussian, 517 generator, 111 Johnson, 382 photon, 334 pointing, 540 quantum, 334, 336 readout, 357, 370 scintillation, 515 seismic, 434 shot, 334 signal, 514 temperature, 335, 390, 402, 497 thermal, 340 transmission, 514 white, 584   
Noise equivalent charge (NEC), 357   
Noise equivalent flux (NEF), 339   
Noise equivalent power (NEP), 339, 383   
Non-linearity, 546   
Normal distribution, 642   
Normal process, 647   
Notch filter mask, 304   
NTT telescope, 190, 192, 381   
Nuclear lines, 447 transitions, 445   
Nucleosynthesis, 447   
Nulling fringe mode, 291   
Nulling interferometry, 296, 311   
Numerical aperture, 179, 263   
Nutation, 134, 137   
Nyquist formula, 342

Nadir, 132   
Nanc¸ay radiotelescope, 186, 280   
NAOS, 536   
Nasmyth focus, 178   
National Virtual Observatory (NVO), 617   
Natural guide star, 480   
Negative frequencies, 632   
NEMO telescope, 429   
NESTOR telescope, 428

OAO satellite, 195   
Observation daytime, 59 from space, 77 in situ, 11 sites, 71   
Observing block, 537   
Observing system, 12 astrophysical model, 531 computing model, 531 detector, 530 electrical model, 531 environmental model, 531 mechanical model, 530 optical model, 530 thermal model, 530   
Obukhov’s law, 64   
ODIN mission, 398   
Offset signal, 57   
OH radical, 55   
OHANA, 292   
On–off technique, 57   
Open acess, 36   
Opticad, 530   
Optical absorption, 347   
Optical depth, 443   
Optical fibre, 263   
Optical telescopes, 189   
Optimal filtering, 26   
Orbit high circular, 86 low equatorial, 86   
Oversampling, 179, 522   
Oxygen, molecular, 89   
Ozone, 44

intrinsic, 345 stressed, 347 Photocurrent, 337 Photodetector Array Camera and Spectromete (PACS), 379, 480, 501 Photoelectric effect, 202 Photographic plate, 357 Photography, 350 Photoionisation of gas, 350 Photometric quality, 73 Photometry gamma-ray, 201 infrared, 108, 112 radiofrequency, 110 ultraviolet, 117 visible, 114 X-ray, 118 Photomultiplier (PM), 359 solid- state (SSPM), 379 Photon correlation, 261 counting camera, 362 properties of, 13 statistics, 103 Photovoltaic effect, 347 Pico Veleta radiotelescope, 189 PICSIT, 206 Pierre Auger observatory, 75 Piston, 242 Piston effect, 66 Pixel, 328, 510 dead, 549 frequency, 373 hot, 549 Planck mission, 87, 198, 385 Planck’s law, 99 Planetary boundary layer, 66 PlanetQuest, 295 Plasma frequency, 50 ionospheric, 46, 50, 62 PMM digitisation, 610 Point estimation, 551 Point source response function, 222 Point spread function (PSF), 219, 222, 224, 580 Pointing noise, 540 Poisson distribution, 643 parameter of, 643 impulse, 649 process, 648 statistics, 104 Polarisation, 24, 97

Pair creation, 202, 351, 353   
Pair effect, 408   
Palomar Optical Sky Survey (POSS), 607   
Palomar, Mount, 73, 190   
Paraboloid, 177   
Parallax, 152   
Parametric amplifier, 398   
Paranal site, 73, 190   
Parent population, 550   
Parkes–MIT–NRAO (PMN) survey, 607   
Parseval’s theorem, 630   
Partial correction, 247   
Partial ordering, 552   
Peltier refrigerator, 359   
Phase closure, 239, 271   
Phase mask, 304   
Phase noise, 239   
Phonons, 347, 413, 448   
Phoswich detector, 415   
Photocathode, 345   
Photochemical effect, 350   
Photoconductor   
extrinsic, 346

Pollution light, 76 radiofrequency, 76, 88   
Polycyclic aromatic hydrocarbons, 448   
Positronium, 447   
Power spectral density (PSD) of random variable, 630 of signal, 634   
Power spectrum, 647   
Precession, 133, 134   
Precipitable water, quantity of, 43   
Predisperser, 468, 491   
Primary mirror, 177   
Primary standard, 106   
Principal components, 528   
Probability, 637   
Probability density, 638   
Proleptic calendar, 171   
PRONAOS balloon, 47   
Proper motion, 133, 135, 145, 146   
Proportional counter, 364, 493   
Prouhet–Thue–Morse sequence,´ 314   
Publications, 34   
Pulse shape discrimination (PSD), 415   
Pupil, 216, 218 circular, 223 disconnected, 226 function, 217 masking, 273 non-redundant, 277 redundant, 277   
Pyrometry, 112

spectrometry, 494 telescopes, 185 transmission, 74 Radiometry, 94 Radiotelescope, 185 Ramo’s theorem, 416, 440 Random process, 644 Random variable, 637 reduced normal, 642 Rao–Blackwell theorem, 562 Rao–Cramer inequality,´ 564 Raster scanning, 186, 328 Ray tracing, 179, 181, 182 Rayleigh resolution criterion, 224 scattering, 58 star, 251 theorem, 630 unit, 51 Rayleigh–Jeans law, 99 Readout noise, 357 rate, 381 Real-time data handling, 26 Realisation, 550 Recycling of light, 432 Reddening, 108 Redundancy of data, 527 Reflection grating spectrometer (RGS), 468, 494 Refracting telescope, 189 Refractive index of air, 61 Reliability, 78 Remote sensing, 10 Resistor, thermal noise of, 341 Resonant cavity, 388 Reynold’s number, 63 Richardson number, 67 Richardson’s law, 359 Right ascension at Greenwich, 142 Risk, 552 Roddier and Roddier coronagraph, 302 Root mean square (rms) deviation, 641 ROSAT mission, 201, 607 ROSITA mission, 372 Rotation lines, 445, 446 Rotation of field, 192 Rotation of the Earth, 132, 134, 141, 165 Rotation–vibration lines, 445, 446 Rouan coronagraph, 304 Rowland mounting, 470 Ruby maser, 399 Running mean, 339, 599

Quadratic detector, 325, 342   
Quantisation of EM field, 332   
Quantum efficiency, 337, 344   
Quantum noise, 334, 336   
compression, 339   
Quantum well, 348   
Quantum yield, 350   
Quasar, 148, 155   
Quasi-monochromatic radiation, 101   
Quasi-optical mode, 380   
Quenouille method, 559   
Radiation belts, 83   
Radiation pattern, 113   
Radiative transfer, 94   
Radio dish, 185   
Radiofrequency   
detection, 335, 339, 387

Rydberg formula, 444   
Rydberg maser, 399   
SALT telescope, 191   
Sample, 550, 623   
Sampling, 520 function, 623 rate, 520   
Saturation threshold, 324   
Scale height, 40   
Schmidt sky surveys, 610   
Schmidt telescope, 183   
Schottky diode, 396, 401   
Scidar, 66   
Scintillation, 228, 515 interplanetary, 237 interstellar, 237   
Scintillator, 413 conversion yield of, 413   
Second (time), 158, 162   
Secondary electron conduction tube (SEC), 362   
Secondary standard, 106   
Seeing, 23 angle, 234   
Self-coherent camera, 309   
Semi-classical model of light, 332   
Semiconductor detector, 415   
Sensitised photographic plate, 350   
Sensitivity of detection, 18   
Shack–Hartmann analysers, 244   
Shah function, 623   
Shannon’s theorem, 521   
Shear, wind, 66   
Shift-and-add, 236   
Shot noise, 334   
SI units, 162   
Sidelobes, 113   
Sidereal angle, 141 Greenwich, 142   
Signal average power of, 633 energy of, 633 instantaneous power of, 633 power spectrum of, 634   
Signal-to-noise ratio (S/N), 512, 516, 518 in spectrometry, 459   
Silicates, 448   
Silicon, 346   
Silicon intensified target (SIT) tube, 362   
SIMBOL-X mission, 202   
Similarity relation, 621   
Sinc function, 622, 623   
SINFONI, 480   
Single sideband (SSB) reception, 394   
Single-channel detector, 326   
Single-mode propagation, 263   
SIS junction, 349, 400   
SIS mixer, 349   
SKA, 279   
Sky background magnitude of, 52 subtraction of, 57 chopping, 57 coverage, 250 noise, 57, 68 subtraction, 538   
Sky survey, 608 CCD, 611 CFDF, 612 CFHT-LS, 612 completeness, 607 confusion limit, 607 cosmic microwave background, 609 DEEP2, 614 DENIS, 614 depth, 607 2dFGRS, 613 ESO, 610 field, 607 HDF-N and -S, 612 infrared, 614 2MASS, 614 photometric, 609, 612 POSSI/POSSII, 610 Schmidt, 610 SDSS, 612, 613 SERC/AAO, 610 spectroscopic, 609, 613 VVDS, 612, 614   
Slit mask, 475   
Smearing, 228   
Snapshot mode, 273   
SOFIA telescope, 47, 197, 501   
SOHO, 87   
Solar aureole, 60 corona, 60 eclipse, 60 flares, 83, 122, 280 granulation, 601 modulation, 85 spectrum, 121 wind, 5, 83   
Solid transitions, 447   
Solid-state imagers, 365   
Soviet–American Gallium Experiment (SAGE), 422   
Space Interferometry Mission, 295   
Space telescopes, 194   
Space–time frames, 24   
Spallation, 86   
Spark chamber, 410, 513   
Spatial cutoff frequency, 222 filter, 220, 226, 263 filtering by turbulence, 233 frequencies, 620 modes, 241 reference systems, 129   
Specific intensity, 95 of the Sun, 114   
Speckle, 236, 334 cancellation, 310   
Speckle interferometry, differential, 238   
Spectral coverage, 15 element, 457 lamp, 117 line, 444 equivalent width, 444, 449 flanks of, 444 intensity, 449 polarisation, 450 profile, 449 wings of, 444 mask, 475 multiplexing, 482 resolution, 456 width, 101   
Spectral density estimator of, 657 of random variable, 630 of stochastic process, 647 white, 650   
Spectroheliogram, 481, 482   
Spectroheliograph, 461, 481   
Spectrometer, 455 acoustic, 498 autocorrelation, 499 Bragg, 491 Fabry–Perot,´ 489 fibre optic, 477 finesse of, 490 Fourier transform, 481, 488 grating, 463 heterodyne, 494 holographic Fourier, 485 imaging, 455, 460 interferometric, 462

multi-object, 461, 475 multichannel, 460, 497 resonance, 503 robot arm, 479 sequential, 460 Spectrometry gamma, 412 heterodyne, 503 infrared, 463, 490 integral field, 471, 479 radiofrequency, 494 submillimetre, 501 ultraviolet, 463 visible, 490 X-ray, 491 Spectrophotometry, 94 Spectrum, 630 amplitude, 630 phase, 631 SPHERE, 307 Spherical coordinates, 129 Spin–orbit coupling, 445 SPIRE, 488 Spitzer mission, 117, 198, 376, 501 SQUID, 385 Standard deviation, 641 Stationary process, 647 Statistical contrast, 586 Statistics, 550 Stenope, 202 STMAG, 107 Stochastic process, 644 transformation of, 650 Stokes parameters, 99, 500 Storage capacity, 381 Stratopause, 41 Stratosphere, 40, 41 Stratospheric balloon, 197 Strehl ratio, 247 Structure constant of refractive index, 68, 230 of temperature, 66 Structure function, 65 of phase, 230 Sub-pupil, 226 Subaru telescope, 190 Submillimetre detection, 326, 339, 343, 355, 387 spectrometry, 501 telescope, 192, 196 transmission of, 53 Submillimetron project, 397 Sudbury Neutrino Observatory (SNO) Sun, mean displacement of, 142

Super-Kamiokande, 424   
Super-resolution, 238, 319   
Supercomputers, 27   
Superconducting tunnel junction (STJ), 349   
Supernova remnant (SNR), 494   
Supernova SN 1987A, 425   
Surface wave, 499   
SWIFT satellite, 207   
Synchrotron radiation, 119   
Synchrotron sources, 120   
System temperature, 390   
Systematic error, 555

Taylor turbulence, 69   
TDRSS, 87   
Telluric absorption bands, 45   
Temperature antenna, 388 brightness, 116 colour, 124 noise, 335, 390, 402, 497 potential, 67 system, 390   
Temporal frequencies, 620   
Temporal reference system, 157   
Temporal width, 101   
TERAPIX, 617   
Thermal emission of atmosphere, 55   
Thermal noise of resistor, 341   
Thermosphere, 41   
Thinned CCD, 368   
Thirty Meter Telescope (TMT), 33, 194   
Thomson scattering cross-section, 350   
Throughput, 94, 211, 457, 472 advantage, 485 of a spectrometer, 484   
Time apparent solar, 159 atomic, 161 civil, 161 Coordinated Universal (UTC), 164 dynamical, 167 Ephemeris (ET), 167 International Atomic (TAI), 163 local sidereal, 140 mean solar, 159 Terrestrial Dynamical (TDT), 169 Universal (UT), 161   
Time delay integration, 549   
Time scales, 157   
Time variability, 20   
Time–frequency analysis, 632   
TIMMI instrument, 381   
Tip–tilt, 242 correction, 244 fluctuation, 244   
Tololo site, 190   
Transfer equation, 442 inversion of, 443   
Transparency function, 203   
Triad, local, 132   
Triangulation, localisation by, 207   
Triplet corrector, 181   
Tropopause, 40   
Troposphere, 40, 63   
Truncated mean, 572   
Truncation, 600   
Turbulence effect on images, 228 frozen, 69 homogeneous, 64 ionospheric, 70 spatial filtering by, 233   
Turbulent dissipation, 63   
UCAC, 154   
UKIRT telescope, 190   
Ultraviolet detection, 335, 344, 368 photometry, 117 spectrometry, 463 telescopes, 195 transmission of, 46   
Ultraviolet Visible Echelle Spectrograph (UVES), 468   
Undersampling, 522   
Uniform minimum variance unbiased (UMVU) estimator, 553   
URA mask, 205

Valence band, 345   
Van Allen belts, 83   
Varactor, 398   
Variance of random variable, 640   
Vega, 114   
Venus, spectrum of, 487   
Vernal equinox, 134, 145   
Vertical, local, 131   
Very Large Array (VLA), 74, 277, 278, 391   
Very Large Telescope (VLT), 190, 193   
Very long baseline interferometry (VLBI), 148,   
260, 282   
VESPA correlator, 500   
Vibrations, man-made, 76   
Video detection, 392

Vidicon tube, 361   
VIMOS, 476   
VIRGO experiment, 432   
Virtual instrument, 529   
Virtual observatory, 615   
Virtual reality, 78   
Viscosity, 63   
Visible detection, 335, 344 imaging, 234 nulling coronagraph, 309 photometry, 114 spectrometry, 490 telescopes, 189, 193, 194 transmission of, 73   
VISTA, 190   
VLBA, 285, 286   
VLTI, 288   
Voigt profile, 455   
Volume holographic grating, 46   
VSOP mission, 286

Wiener–Khinchine theorem, 598, 631   
Wiener–Kolmogorov filter, 523   
Wigner–Ville representation, 632   
Windowing, 632   
Windowing mode of CCD, 373   
Winsorized mean, 572   
Wire chamber, 351   
WMAP mission, 123   
Wolter telescope, 200

X-ray detection, 328, 344 photometry, 118 spectrometry, 491 telescopes, 199 transmission, 82   
Xing Long, 190   
XMM–Newton mission, 201, 468, 493

Young slits, 102

Wave number, 96   
Wave packet, 621   
Wavefront analyser, 244 measurement of, 241 perturbations of, 229 sensor, 537   
Waveguide, 262, 388   
Wavelets, 635   
Weber’s experiment, 431   
Weighting telescope, 207   
White paper, 33   
White spectral density, 650   
Wien’s law, 99   
Zeeman effect, 450, 451, 455, 481   
Zelenchuskaya site, 73, 190   
Zemax, 530   
Zenith, 132 distance, 45   
Zentralen Grenzversatz, 518   
Zernike polynomials, 181, 241   
Zernike theorem, 211   
Zernike–Van Cittert theorem, 213   
Zodiacal emission, 80 light, 80, 314 nebula, 80
