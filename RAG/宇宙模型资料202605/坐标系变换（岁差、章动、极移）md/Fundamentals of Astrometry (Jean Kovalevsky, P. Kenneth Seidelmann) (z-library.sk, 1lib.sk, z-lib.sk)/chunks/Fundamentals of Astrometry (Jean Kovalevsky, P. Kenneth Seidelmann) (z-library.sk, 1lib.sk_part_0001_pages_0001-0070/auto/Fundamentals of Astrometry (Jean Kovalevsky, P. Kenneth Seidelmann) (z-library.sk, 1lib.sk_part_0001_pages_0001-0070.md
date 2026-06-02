# Fundamentals

# of Astrometry

Jean Kovalevsky and P. Kenneth seidelmann

# FUNDAMENTALS OF ASTROMETRY

Astrometry encompasses all that is necessary to provide the positions and motions of celestial bodies. This includes observational techniques, instrumentation, processing and analysis of observational data, reference systems and frames, and the resulting astronomical phenomena. Astrometry is fundamental to all other fields of astronomy, from the pointing of telescopes, to navigation and guidance systems, to distance and motion determinations for astrophysics. In the past few decades, new observational techniques have facilitated improvements in accuracy by orders of magnitude. Starting from basic principles, this book provides the fundamentals for this new astrometry at milli- and microarcsecond accuracies. Topics include basics of general relativity; coordinate systems; vectors, tensors, quaternions, and observational uncertainties; determination and use of the celestial and terrestrial reference systems and frames; applications of new observational techniques; and present and future star catalogs and double-star astrometry. Examples of astronomical computations and a large glossary are also provided. This comprehensive text is an invaluable reference for graduate students and research astronomers.

j e a n kova l e v s k y is an associate (retired) astronomer of the Centre d’Etudes et de Recherches G´eodynamiques et Astronomiques (CERGA), at the Observatoire de la Cˆote d’Azur, France. He is President of the International Committee of Weights and Measures and is a member of the French Academy of Sciences.

p. k e n n e t h s e i d e l m a n n is a research professor in the Department of Astronomy, University of Virginia. Until 2000 he was Director of Astrometry at the US Naval Observatory, and a visiting professor at the University of Maryland.

# FUNDAMENTALS OF ASTROMETRY

JEAN KOVALEVSKY CERGA, Observatoire de la Cote d’Azur ˆ

P. KENNETH SEIDELMANN Department of Astronomy, University of Virginia published by the press syndicate of the university of cambridge The Pitt Building, Trumpington Street, Cambridge, United Kingdom

cambridge university press The Edinburgh Building, Cambridge CB2 2RU, UK 40 West 20th Street, New York, NY 10011-4211, USA 477 Williamstown Road, Port Melbourne, VIC 3207, Australia Ruiz de Alarc´on 13, 28014 Madrid, Spain Dock House, The Waterfront, Cape Town 8001, South Africa

http://www.cambridge.org

$©$ Jean Kovalevsky and P. Kenneth Seidelmann 2004

This book is in copyright. Subject to statutory exception and to the provisions of relevant collective licensing agreements, no reproduction of any part may take place without the written permission of Cambridge University Press.

First published 2004

Printed in the United Kingdom at the University Press, Cambridge

Typeface Times 11/14 pt. System LATEX 2ε [tb]

A catalog record for this book is available from the British Library

Library of Congress Cataloging in Publication data

Kovalevsky, Jean.   
Fundamentals of astrometry / Jean Kovalevasky and P. Kenneth Seidelmann. p. cm.   
Includes bibliographical references and index.   
ISBN 0 521 64216 7 (hardback)   
1. Astrometry. I. Seidelmann, P. Kenneth. II. Title.   
QB807.K682 2003   
522–dc21 2003053227

ISBN 0 521 64216 7 hardback

In memory of the late Jeannine Kovalevsky and to Bobbie Seidelmann in appreciation for their continuing support, encouragement, and love during the preparation of this book by their respective husbands

Contents

Preface page xi List of abbreviations xiii

1 Introduction 1

1.1 Classical astrometry 2

1.2 New astrometry 5

1.3 Time 6

1.4 Earth orientation and reference frames 8

2 New observational techniques 11

2.1 New detectors 11

2.2 Basics of interferometry 12

2.3 Stellar interferometry 16

2.4 Applications of time measurements 23

2.5 Launched space astrometry satellites 29

2.6 Proposed space missions 33

# 3 Basic principles and coordinate systems 39

.1 Vectors 39

Vector derivatives 43

3.3 Gradient 45

3.4 Matrices 46

3.5 Tensors 50

3.6 Quaternions 54

3.7 Spherical trigonometry 57

3.8 Coordinate systems 59

3.9 Differential coordinates 61

# vii

viii Contents

3.10 Reference coordinates 64   
3.11 Time 68   
3.12 Extragalactic reference frame 68

# 4 Treatment of astronomical data 71

4.1 Introduction to data reduction 71

4.2 Random errors 74

4.3 Systematic errors 81

4.4 Method of least squares 82

4.5 Additional aspects 89

# 5 Principles of relativity 93

5.1 Relativity principles 94

5.2 Special relativity 94

5.3 General relativity 103

5.4 Space-time coordinate systems 111

5.5 Time scales 115

5.6 Astrometric effects 117

# 6 Apparent displacements of celestial objects 121

# 6.1 Atmospheric refraction 121

6.2 Parallactic corrections 131

6.3 Aberration 135

6.4 Relativistic light deflection 144

6.5 Retardation of light 154

# 7 Extragalactic reference frame 157

7.1 International Celestial Reference System (ICRS) 157

7.2 International Celestial Reference Frame (ICRF) 159

7.3 Optical realizations of the ICRF 162

7.4 Dynamical reference frame tie to the ICRF 163

7.5 Transformation between GCRS and BCRS 164

7.6 ICRF stars at other epochs 165

7.7 Consequences of adoption of the ICRS and ICRF 166

7.8 Transformations to ecliptic and galactic coordinates 167

# 8 Dynamical reference frame 171

8.1 Our Solar System 172

8.2 Ephemerides 172

8.3 Reference planes 174

Contents ix

8.4 New definitions of a reference frame and fiducial point 174

8.5 Generalities on precession and nutation 176

8.6 Precession 177

8.7 Nutation 183

# 9 Terrestrial coordinate systems 187

9.1 Introduction 187

9.2 Terrestrial reference systems 188

9.3 The ITRF series 189

9.4 Geodetic coordinates 193

9.5 Physical geodesy 195

9.6 Coordinates of a point on the Earth 199

9.7 Topocentric astronomical coordinates 201

9.8 Time variations 206

9.9 Dynamical consequences 214

# 10 Earth orientation 217

#

10.1 Earth orientation presentation 217

10.2 Observation of the Earth’s rotation 221

10.3 Celestial and terrestrial moving frames

10.4 Description of the Earth’s orientation

10.5 Universal Time

223   
228   
231   
234

10.6 ITRF to ICRF transformations

10.7 Other effects 237

# 11 Stars 239

#

11.1 Star positions 239

11.2 Distance of stars 241

11.3 Space motions 246

11.4 Magnitudes 254

11.5 Pre-Hipparcos star catalogs 259

11.6 Hipparcos-based catalogs 267

11.7 Optical reference star densification 271

# 12 Double and multiple star systems 275

12.1 The two-body problem 275

12.2 Apparent orbits of double stars 281

12.3 Resolved double stars 285

12.4 Astrometric double stars 289

12.5 Spectroscopic binaries 292   
12.6 Photometric binaries 297   
12.7 Particular objects 300   
12.8 Determination of stellar masses 302   
12.9 Catalogs of double and multiple stars 305

# 13 Astronomical phenomena 307

13.1 Motions involved 307   
13.2 Periods 308   
13.3 Rising/setting 309   
13.4 Phases 312   
13.5 Oppositions, conjunctions, stationary points, elongations 314   
13.6 Eclipses 314   
13.7 Occultations 315   
13.8 Transits 318   
13.9 Mutual events 318   
13.10 Physical ephemerides 318   
3.11 Calendar 319

# 14 Applications to observations 323

14.1 Observing differences, classical and new systems 323

14.2 Determinations of positions 324

14.3 CCD observations 325

14.4 Plate reduction 327

14.5 Overlapping plate solutions 329

14.6 Radio observations 338

14.7 Millisecond pulsars 338

14.8 Extrasolar planets 345

Appendix A Examples 353   
Appendix B Astronomical values 363   
Glossary 371   
References 387   
Index 399

Preface

Astrometry is undergoing fundamental changes. The celestial reference frame based on bright optical stars is being replaced by the extragalactic reference frame observed at radio wavelengths by Very Long Baseline Interferometry (VLBI); Hipparcos has proven the capabilities of astrometry from space; photographic plates are being replaced by charge coupled devices (CCDs) as the detectors of choice; optical interferometers are replacing transit circles and astrolabes; accuracies of tenths of arcseconds are being replaced by milli- and microarcseconds; the dynamical reference frame is being replaced by a kinematic reference frame; Global Positioning System observations are changing the determinations of Earth Orientation Parameters; and the theory of general relativity is required as the basis of astrometry.

This book is designed to provide the fundamentals for the new astrometry at the milli- and microarcsecond accuracies. The intent is to start from basic principles, without approximations, and develop the fundamentals of astrometry at microarcsecond accuracies. It is based on the general theory of relativity and the concepts introduced by the International Astronomical Union (IAU) in the past decade. The book provides the definitions and applications of the International Celestial Reference System (ICRS) to astronomy and astrometry. It is also designed to provide the philosophy and concepts of astrometry for the future, the principles behind the algorithms, the reasons for astrometry and its relationships with astronomy, geophysics, planetary sciences, astrophysics, cosmology, and celestial mechanics. It defines and describes the reference systems, reference frames, their relationships and realizations. Definitions, astronomical values, and examples are given in Appendixes.

Other volumes provide the methods for almanacs (Explanatory Supplement to the Astronomical Almanac), and observational techniques in detail (Kovalevsky, Modern Astrometry). New developments in astronomical data and star catalogs, algorithms and software, latest values of constants, ephemerides, and Solar System bodies can be found in specialized documents like the IERS Conventions, astronomical data banks and SOFA software. It is indeed expected that the latest information, data, and software will be available by the world wide web and so some web sites are given in the book as sources of the latest data.

It is our pleasure to acknowledge and thank Dr Thomas Corbin, who reviewed all the chapters of the book and provided suggestions concerning content and language. We also thank Dr Serguei Kopeikin who has reviewed and given very useful suggestions in the parts concerning general relativity. We have also profited from discussions with Dr Nicole Capitaine, Dr Dennis McCarthy, and Dr Patrick Wallace.

# Abbreviations

AC Astrographic Catalogue   
ACRS Astrographic Catalogue Reference Stars   
ACT Astrographic Catalog Tycho   
ADC Astronomical Data Center at Goddard Space Flight Center   
AGK1 Katalog der Astronomischen Gesellschaft   
AGK2 Zweiter Katalog der Astronomischen Gesellschaft   
AGK2A Astronomischen Gesellschaft Katalog Reference stars   
AGK3 Dritter Astronomischen Gesellschaft Katalog   
AGK3-R Astronomischen Gesellschaft Katalog Reference stars   
AGU American Geophysical Union   
BCRS Barycentric Celestial Reference System   
BGI Bureau Gravim´etrique International (at Toulouse)   
BIH Bureau International de l’Heure   
BIPM Bureau International des Poids et Mesures   
BdL Bureau des Longitudes (now IMCCE)   
BPT binary pulsar time scale   
CCD charge coupled device   
CDS Centre de Donn´ees stellaires (in Strasbourg)   
CEO Celestial Ephemeris Origin   
CEP Celestial Ephemeris Pole   
CERGA Centre d’Etudes et de Recherches G´eodynamiques et Astronomiques (in OCA)   
CHARA Center for High Angular Resolution Astronomy   
CIP Celestial Intermediate Pole   
CIRF Celestial Intermediate (or True) Reference Frame   
CNES Centre National d’Etudes Spatiales   
COAST Cambridge Optical Aperture Synthesis Telescope   
CPC Cape Photographic Catalogue   
CTE charge transfer efficiency   
CTI charge transfer inefficiency   
CTRF Conventional Terrestrial Reference Frame   
CTRS Conventional Terrestrial Reference System   
DGFI Deutsches Geodatisches Forschungsinstitut   
DIVA Double Interferometer for Visual Astrometry   
DMA Defense Mapping Agency (now NIMA)   
DUT1 UT1-UTC   
EOP Earth Orientation Parameters   
ERS European Remote Sensing Satellite   
ESA European Space Agency   
ET Ephemeris Time   
FAME Full-sky Astrometric Mapping Explorer   
FCN Free Core Nutation   
FGS Fine Guidance Sensors   
FK3 Fundamental Katalog 3   
FK4 Fundamental Catalogue 4   
FK5 Fundamental Catalogue 5   
GAIA Global Astrometric Instrument for Astrophysics   
GC General Catalogue   
GCRF Geocentric Celestial Reference Frame   
GCRS Geocentric Celestial Reference System   
GEM Goddard Earth Model   
GI2T Grand interf´erom\`etre \`a deux t´elescopes   
GMST Greenwich Mean Sidereal Time   
GPS Global Positioning System   
GRGS Groupe de Recherches de G´eod´esie Spatiale   
GRIM GRGS – Institute of Munich (Earth gravity model)   
GRS Geocentric Reference System   
GRS Geodetic Reference System   
GSC Guide Star Catalog   
GSD Greenwich Sidereal Date   
GST Greenwich Sidereal Time   
GTRF Geocentric True Reference Frame   
HCRS Hipparcos Catalogue Reference System   
HST Hubble Space Telescope   
IAG International Association for Geodesy   
IAU International Astronomical Union   
ICRF International Celestial Reference Frame   
ICRS International Celestial Reference System   
IERS International Earth Rotation Service   
IGS International GPS Service   
IHRF International Hipparcos Reference Frame   
IOTA Infrared-optical Telescope Array   
IRS International Reference Star catalog   
ISI Infrared Spatial Interferometer   
ITRF International Terrestrial Reference Frame   
ITRS International Terrestrial Reference System   
IUGG International Union of Geodesy and Geophysics   
JD Julian Date   
JDN Julian Day Number   
JGM Joint Gravity Model   
K kelvin (degree)   
KI Keck Interferometer   
LBT Large Binocular Telescope   
LHA local hour angle   
LOD length of Day   
MACHOS Massive Compact Halo Objects   
mas milliarcsecond   
MJD Modified Julian Day   
nas nanoarcsecond   
NASA National Aeronautical and Space Agency   
NPMP Northern Proper Motion Program   
NPOI Navy Protoype Optical Interferometer   
OCA Observatoire de la Cˆote d’Azur   
pdf probability density function   
PGC Preliminary General Catalogue   
POSS Palomar Optical Sky Survey   
p.p.b. parts per billion   
PPM Positions and Proper Motions catalog   
psf point spread function   
PT pulsar time scale   
PTI Palomar Testbed Interferometer   
RGC reference great circle   
r.m.s. root mean square   
SAO Smithsonian Astrophysical Observatory   
SDSS Sloan Digital Sky Survey   
SI Syst\`eme International (d’Unit´es)   
SIMBAD main data base of the CDS   
SPMP Southern Proper Motion Program   
STScI Space Telescope Science Institute   
SUSI Sydney University Stellar Interferometer   
TAI International Atomic Time   
TCB Barycentric Coordinate Time   
TCG Geocentric Coordinate Time   
TDB Barycentric Dynamical Time   
TDI time delay integration   
TEO Terrestrial Ephemeris Origin   
TT Terrestrial Time   
UCAC USNO CCD Astrographic Catalog   
USNO US Naval Observatory   
UT Universal Time   
UTC Coordinated Universal Time   
UT1 Univeral Time 1   
VLA Very Large Array   
VLBA Very Large Baseline Array   
VLBI Very Long Baseline Interferometry   
VLTI The Very Large Telescope Interferometer   
WGD World Geodetic Datum   
WGD2000 World Geodetic Datum 2000   
WGS World Geodetic System   
2MASS 2 Micron Astronomical Sky Survey   
-as microarcsecond

# 1 Introduction

Astrometry is positional astronomy. It encompasses all that is necessary to provide the positions and motions of celestial bodies. This includes observational techniques, instrumentation, processing and analysis of observational data, positions and motions of the bodies, reference frames, and the resulting astronomical phenomena.

The practical side of astrometry is complemented by a number of theoretical aspects, which relate the observations to laws of physics and to the distribution of matter, or celestial bodies, in space. Among the most important are celestial mechanics, optics, theory of time and space references (particularly with regards to general relativity), astrophysics, and statistical inference theory. These scientific domains all contribute to the reduction procedures which transform the observed raw data acquired by the instruments into quantities that are useable for the physical interpretation of the observed phenomena. The goals of this book are to present the theoretical bases of astrometry and the main features of the reduction procedures, as well as to give examples of their application.

Astrometry is fundamental to, and the basis for, all other fields of astronomy. At minimal accuracy levels the pointing of telescopes depends on astrometry. The cycle of days, the calendar, religious cycles and holidays are based on astrometry. Navigation and guidance systems are based on astrometry, previously for nautical purposes and now primarily for space navigation.

Astronomy and astrophysics are also strongly dependent on astrometry. The dynamics in the Solar System and in other gravitationally linked celestial bodies, stellar motions as obtained from the determination of proper motions, masses of double and multiple star systems, distances of stars in the vicinity of the Sun, apparent dimensions and shapes of planets, stars and other celestial objects, are all derived from astrometric observations.

Improvements in accuracies of observational techniques have been accompanied by increases in knowledge and improvements in theories. This process should continue in the future.

A very touchy but essential feature of astrometry is the expression of the uncertainties of the observations. It is customary, and actually very important, to distinguish precision, which describes the capability of an instrument to reproduce the observations, and accuracy, which represents how much these results deviate from what are thought to be the true values (which are by nature not attainable). The precision is improved by increasing the power, the resolution, or the sensitivity of the instrument. The accuracy is improved by measuring, or modeling, all effects that possibly can bias the results. This is done during the reduction process, even though it may mean additional measurements (temperature or humidity of air, optical distortions of the instrument, etc.). A given instrument’s observations of stars may have a precision of 20 milliarcseconds (mas), but when compared with a catalog from many instruments, one may infer that its accuracy is 50 mas (assuming, however, some evaluation of the accuracy of the reference catalog itself). Evaluating the accuracy of observations is one of the most difficult and fundamental tasks of astrometry.

# 1.1 Classical astrometry

Astrometry began with the first naked-eye observations of the sky. These observations led to the discovery of wanderers (planets) among the stars, knowledge of the cycles of days and years, predictions of eclipses, the concept of almanacs and calendars, and the catalogs of observations. The naked eye limited both the faintness of objects and the accuracies of the positions observed. The observations of phenomena, such as eclipses and occultations, along with the location on Earth of the observer are the most accurate observations from ancient times.

From the beginning, astrometric observations were the basis for theories and discoveries. In $1 5 0 ~ \mathrm { B C }$ , Hipparchus discovered precession, the long period (26 000 year) motion of the Earth’s pole with respect to the fixed stars, from observations with a precision of $1 2 0 0 ^ { \prime \prime }$ (Dick, 1997). This was possible due to observations of Spica from 160 years earlier. Hipparchus may have prepared the first star catalog, but certainly Ptolemy’s (ad 150) star catalog, as in his Almagest, is the first passed down from ancient times. Ptolemy developed theoretical explanations of the motions of the wanderers around the Earth. In 1496 Copernicus concluded that the wanderers moved around the Sun, not the Earth.

The Islamic culture produced the star catalogs of Al-Sufi (960), using armillary spheres, and Ulugh Beg (1430), who used a huge sextant, of precision of the order of $5 \mathrm { - } 1 0 ^ { \prime }$ . Tycho Brahe (1546–1601) constructed improved instruments using sights and scales on quadrant- and sextant-type instruments. His observations, at a precision of $1 5 { - } 3 5 ^ { \prime \prime }$ , had a wide impact on astronomy. However, even these improved observations were unable to measure stellar parallax, the angle through which a star seems to be displaced due to the orbital motion of the Earth, and this raised questions about the Copernican theory, since the parallactic displacement due to the motion of the Earth around the Sun was not detected. On the other side, the observations of the planets, in particular Mars, which was the only planet whose observations were of the necessary precision, led Kepler to develop his laws of motion, which in turn led to Newton’s Universal Law of Gravity. The invention of the telescope permitted Galileo to discover the satellites of Jupiter and make astrometric observations of those objects, the first astrometric observations made with a telescope.

The application of astrometry for navigation and time-keeping led to the establishment of national observatories in Paris (1667), Greenwich (1675), Berlin (1701), and St Petersburg (1725). Telescopes were mounted on instruments similar to those used by Tycho Brahe. At the Royal Observatory at Greenwich, John Flamsteed produced the Historiae Coelestis (1725), the first great star catalog based on telescopic observations. In 1718 Edmond Halley, who would succeed Flamsteed as Astronomer Royal, showed that the bright stars, Aldebaran, Sirius, and Arcturus, were displaced by many minutes of arc from their positions in antiquity. Thus, the star positions are not fixed, but they move, perpendicular to the line of sight, by stellar proper motions. In 1728 James Bradley, Halley’s successor, discovered a stellar aberration of $3 0 ^ { \prime \prime }$ due to the Earth’s orbital motion. Aberration is the displacement of the angular position of an object due to the finite speed of light, in combination with the motion of the observer and the observed object. In 1748 Bradley detected the periodic motion of the Earth’s celestial pole with respect to the stars due to nutation, an effect which can amount to $1 8 ^ { \prime \prime }$ . William Herschel, who discovered Uranus in 1781, detected the motion of the Sun toward the constellation Hercules from an analysis of stellar proper motions.

Improvements in the precision of astrometric observations were sufficient that in 1838–40 Fredrich Wilhelm Bessel, Wilhelm Struve, and Thomas Henderson independently announced observations of a few tenths of an arcsecond precision showing that star positions shifted as the observer changed position in the Earth’s orbit. Thus, the effect of parallax was observed, the truth of the Copernican theory solidified, and a method of directly measuring accurate stellar distances was established. In 1844 at Pulkovo, Bessel, from positional observations of 0.7 and proper motions of 0.5/year precision, announced unseen stellar companions, which were producing variations in proper motions of Procyon and Sirius. Direct telescope observations confirmed the companions later in the century. In 1885 Chandler detected, from stellar measurements, the motion of the Earth’s axis of rotation with respect to the Earth’s crust. This is called polar motion and amounts to 0.5/year.

For most of the twentieth century, the primary instrument for large-angle astrometry was the transit circle. The transit instrument, which could observe only right ascensions, was first used by Ole Roemer in Copenhagen in 1689. The transit circle, which has a circle to measure declination, was succesfully introduced by Troughton in 1806 for Groombridge. By the mid nineteenth century most observatories had transit circles and for 150 years they were the prime instruments of large-angle astrometry. The observations from transit circles were the bases for the positions and proper motions of the fundamental catalogs through the FK5, which provided the astronomical reference frames.

The transit circle is a specialized telescope that can be moved only along the meridian, a North–South arc passing through the observer’s zenith. This restriction of motion and the rigid mounting provides the stability necessary for precise observations. Observations are made in the East–West coordinate (right ascension) by timing when the star crosses, or transits, the meridian due to the Earth’s rotation, while the North–South coordinate (declination) is measured on a very finely divided circle.

While the transit circle was good for accurate measurements of individual stars on the hour circle of the instrument all over the sky, the photographic plate could observe many stars in a small field of view. David Gill began a photographic survey of the southern sky from Cape Observatory at the end of the nineteenth century. The plates were measured and the positions analyzed by J. C. Kapteyn. The 1887 International Astrophotographic Congress in Paris coordinated the first international photographic survey of the sky, the Carte du Ciel, and the resulting Astrographic Catalogue (AC). This sky survey reached about 12th magnitude, while subsequent photographic surveys using Schmidt telescopes have gone as deep as 21st magnitude. Schmidt telescopes achieve wide fields of view by a correcting glass at the center of curvature and a concave focal plane, which the plate must be bent to form.

Long-focus refractors were being used at the end of the nineteenth century in small fields for observations of double stars, asteroids and satellites. The advantage of long-focus astrometry is that it provides a large scale on the plate, proportional to the focal length. One gets better precision in positions of star images, namely a few hundreds of arcseconds. A large number of stars are thought to be in multiple star systems. In some cases the components can be detected individually; others can be detected photometrically by changes in magnitude, some by astometry due to their nonlinear proper motions, some by periodicities in their radial velocities and others by multiple spectral characteristics (Chapter 12). At the beginning of the twentieth century Frank Schlesinger at Yerkes, Allegheny and Yale Observatories began the application of photography on long-focus refractors for the determination of parallaxes (Section 11.2).

# 1.2 New astrometry

The last decades of the twentieth century have experienced a revolution in astrometry. This was because of the charge coupled device (CCD) as a detector replacing the photographic plate and measuring machine, optical interferometers able to observe at milliarcsecond levels, space astrometry pioneered by the Hipparcos project, and radio astrometry by Very Long Baseline Interferometers (VLBI, Section 2.4.2) producing a celestial reference frame of extragalactic sources at milliarcsecond accuracy levels.

The CCD is a silicon chip that converts photons into electrons. The CCD directly provides a digital output, eliminating the need for the measuring machine. It is a small-size detector compared with the photographic plate, but it is extremely efficient, more than $50 \%$ , dependent on the filter used, compared with $1 \%$ for photographic plates (see Sections 2.1 and 14.3). Also, the data can be processed to eliminate backgrounds, subtract bright stars, etc. The small pixel sizes and the point spread function across many pixels provides the means of measuring the centroids of star positions very accurately. As a result, parallaxes of faint stars with respect to the mean parallax of background stars (relative parallaxes) can be determined with accuracies of better than 0.5 milliarcseconds (mas); and relative positions with 20 mas accuracies are possible from ground-based observations.

Albert A. Michelson, in the late nineteenth century, developed interferometry, which uses the interference of light waves for its measurement. The first stellar interferometer was not built until 1920 and only in the 1970s was it used for astrometry, other than double-star observations. Optical interferometers (Section 2.3) are currently being developed for astrometric positional measurements at the mas level, double-star measurements, and imaging of individual stars.

The Hubble Space Telescope (Section 2.5.2) is capable of astrometric observations with the Wide Field Planetary Camera, and the Fine Guidance Sensors. Double stars, parallaxes, proper motions in clusters, planetary satellite positions, and planetary nebulae motions have been measured (Section 2.4). The Hipparcos satellite (Section 2.5.1) was developed as an astrometric satellite to determine parallaxes. It has determined the positions and proper motions of 120 000 stars to accuracies of 1 mas and 1.1 mas/year for stars of 9th magnitude and brighter and parallaxes for 60 000 stars to 1 mas accuracies.

There are now plans for interferometer and astrometric satellite missions that could reach microarcsecond accuracies for stars as faint as 20th magnitude. The Space Interferometer Mission (SIM) and the Global Astrometric Instrument for Astrophysics (GAIA) are two such missions under study (Section 2.6).

In parallel with these developments in optical astrometry, the field of radio interferometric techniques (Section 2.4.2) applied to astrometry was developed primarily for geodesy and Earth orientation purposes, but the accuracies and the wealth of data have had a significant impact on astrometry via the recently adopted International Celestial Reference System (ICRS).

Observations at a few microarcsecond precision imply that, in parallel, one must model the light path between the source and the observer with a similar accuracy (Chapter 6). This means, in particular, that one uses general relativity to describe the space-time (Chapter 5). Another consequence is that sophisticated mathematical methods must be used for the treatment of astrometric data (Chapter 4).

# 1.3 Time

From early times people kept track of time based on the apparent diurnal motion of the Sun. This is called apparent solar time and undergoes seasonal variations, because of the obliquity of the ecliptic and the eccentricity of the Earth’s orbit. This is the time from sundials. Clocks and chronometers are not subject to the variations of the Earth’s orbit, so mean solar time was introduced based on a fictitious mean Sun with a constant rate of motion and Earth rotation. It was known that the diurnal rotation with respect to the stars was different from that with respect to the Sun. Sidereal time is defined by the apparent diurnal motion of the catalog equinox, and, hence, is a measure of the rotation of the Earth with respect to the stars, rather than the Sun. The rotation of the Earth with respect to the Sun is called Universal Time (UT), and is related to sidereal time (now, stellar angle), by means of a numerical formula (see Section 10.5).

For ephemerides of Solar System bodies’ motions, the tabular times are the values of a uniform measure of time. Discrepancies between observed and computed positions were most evident for the Moon, because its motion is both complicated and rapid. Adams (1853) showed that the observed secular acceleration of the mean motion of the Moon could not be produced by gravitational perturbations. Ferrel (1864) and Delaunay (1865) showed that the tides exert a retarding action on the rotation of the Earth, accompanied by a variation of the orbital velocity of the Moon in accordance with the conservation of momentum. Newcomb (1878) considered the possibility of irregular variations of the Earth’s rotation as an explanation of lunar residuals, but he could not find collaboration from planetary data (Newcomb, 1912). De Sitter (1927) and Spencer Jones (1939) correlated irregularities of the motions of the inner planets with those of the Moon, thus proving the irregularity of the rotation of the Earth.

Danjon (1929) recognized that mean solar time did not satisfy the need for a uniform time scale, and suggested a time scale based on the Newtonian laws of planetary motion. Unaware of Danjon’s paper, Clemence (1948) proposed a uniform fundamental standard of time which was adopted by the International Astronomical Union (IAU) in 1952 and designated as Ephemeris Time (ET). The tropical year of 1900.0, the period of one complete revolution of the longitude of the Sun with respect to the dynamical equinox, was the basis for the definition of Ephemeris Time.

Until 1960, the unit of time, the second, was defined as a specific fraction (1/86 400) of the mean solar day. With the adoption of ephemeris time, the second was defined in the Syst\`eme International (SI) of units as a specific fraction of the tropical year. This definition was more accurate, but its determination was less precise, because the motions of the Sun and Moon being slow, one could not transform the observations of their positions, made to a few tenths of an arcsecond, into time measurements of better than a few hundredths of a second. So, in 1967, a new definition of the second was adopted, following a proposal by Markowitz et al. (1958), in terms of a cesium beam frequency standard. Since then, it has been the fundamental unit of time. Whenever another unit is used, it has to be specified (e.g. ET second, etc.).

The second is defined as the duration of 9 192 631 770 periods of radiation corresponding to the transition between two hyperfine levels of the ground state of the cesium-133 atom. International Atomic Time (TAI) is a practical time scale determined by the Bureau International des Poids et Mesures from time and frequency standards worldwide and conforms as closely as possible to the definition of the second (Section 5.5.1). The second is the unit that is the most accurately and precisely realized at present, and thus, with the conventional value of the speed of light, is the basis for the definition of the meter. Coordinated Universal Time (UTC) is based on TAI and kept within $0 . 9 \ : \mathrm { s }$ of Universal Time (UT1) by the introduction of leap seconds as needed. UTC is the standard time scale defined for the zero meridian and used with appropriate time differences for time zones all over the Earth (Section 10.5.3).

Ephemeris Time was difficult to determine and its definition was not consistent with the theory of relativity. In 1976 and 1991 the IAU adopted resolutions clarifying the relationships between space-time coordinates. Terrestrial Time (TT), previously named Terrestrial Dynamical Time (TDT), is the time reference for apparent geocentric ephemerides, has a unit of measurement so that it agrees with the SI second on the geoid, and is offset from TAI by $+ 3 2 . 1 8 4 \mathrm { ~ s ~ }$ . Geocentric Coordinate Time (TCG) is the coordinate time appropriate for a coordinate system with its spatial origin at the center of mass of the Earth (Section 5.5.1). TCG differs from TT by a scaling factor. Barycentric Coordinate Time (TCB, section 5.5.2) is the coordinate time appropriate for a coordinate system with its spatial origin at the barycenter of the Solar System. The relationship between TCB and TCG involves a full four-dimensional transformation involving the position and velocity of the center of mass of the Earth, a scaling factor, and periodic terms. Thus, the resulting space-time coordinates are consistent with the theory of relativity.

The time scale Barycentric Dynamical Time (TDB) was introduced in 1976 to be a time scale for the barycenter of the Solar System such that it differed from TDT only by periodic terms. This results in a definitional ambiguity dependent upon the length of time being considered. Also, the definition results in different values of some constants, such as the unit of length, to be used with the two time scales. These time scales can be precisely determined from atomic clocks and the theory of relativity. They do not consider the variability of the rotation of the Earth as needed for actual observations.

# 1.4 Earth orientation and reference frames

During the first three quarters of the twentieth century, the rotation of the Earth and polar motion were determined by observations with visual or photographic zenith tubes, transit circles, and astrolabes. Then the techniques of lunar and satellite laser ranging (Section 2.4.3), radio interferometry (Section 2.4.2), and the Global Positioning System (Section 2.4.1) became available and much better accuracy could be achieved. The International Earth Rotation Service (IERS) was founded to coordinate these activities and to provide international values for polar motion and other Earth rotation parameters.

In determining Earth orientation parameters by means of Very Long Baseline Interferometry (VLBI) many observations of radio sources have been made. The accuracies of the positions are about a milliarcsecond and the sources are very distant, so they have no appreciable proper motions. Thus, it became apparent that an accurate, fixed, stellar reference frame could be developed, improving the preceding FK5 reference frame.

A list of stable, point-like radio sources was needed. The ties between these generally optically faint sources and optical and dynamical reference frames were necessary. Such a list of sources was prepared and investigated for structural motions so that an International Celestial Reference Frame (ICRF) could be designated (Section 7.2). Optically this reference frame is represented by the Hipparcos Catalogue (Section 11.6.1). The reference frame is independent of the dynamical reference frame, defined by the equator and the ecliptic planes which are dependent on the Solar System bodies. The origin of the ICRF has been selected to be as close as possible to the FK5 origin and the dynamical equinox of J2000.0. However, in principle, the ICRF is based on observations from the Earth and the kinematics of the Earth’s equator. A new Celestial Intermediate Pole (CIP), and Celestial Ephemeris Origin (CEO) were adopted in 2000 by the IAU. Solar System observations can be made on this reference frame and the equinox and ecliptic determined on that system.

The Hipparcos satellite has provided milliarcsecond accuracies for optical sources. VLBI is determining radio sources at sub-milliarcsecond levels and detecting motions of 25 microarcseconds per year. Optical interferometers in space are planned for microarcsecond accuracies. Thus, astrometry must be developed fundamentally on an extragalactic reference frame to microarcsecond accuracies.

# 2 New observational techniques

What characterizes the new observational techniques is, of course, not only that they appeared recently – say in the past couple of decades – but also that they strive to reach one or two orders of magnitude better accuracy than the classical techniques. The unit for describing the new astrometric capabilities is no longer one tenth of a second of arc, but one thousandth of a second of arc, a subunit that we shall designate throughout this book by the abbreviation mas (milliarcsecond). Plans are underway to reach microarcsecond $( \mu \mathrm { a s } )$ accuracies. Such a gain in precision impacts directly on all aspects of astronomy and, particularly, on the reduction procedures. One may divide these new techniques into three major groups: interferometry, timemeasuring techniques, and space astrometry.

# 2.1 New detectors

Many astrometric techniques take advantage of the development of much more sensitive new detectors. Among them, one must mention the following.

- The CCD detector. The CCD (for charge coupled device) has become a major tool in astronomy since the 1970s (Monet, 1988). It consists of a semiconductor device, where a photoelectric effect takes place when light reaches it, producing an electronic image. This image is preserved by arrays of small positive electrodes, which attract photoelectrons and keep them in a similar array of potential wells, providing the possibility of long exposure times by adding photoelectrons in the same pack (Kovalevsky, 2002). Once the exposure is over, one shifts, by a periodic change of the potential of electrodes, the electronic image along the array. It is then recovered pack by pack at the edge of the array, digitized, and registered in a computer. There, software can analyse it and produce images, determine relative positions or magnitudes of the objects, or deduce any other information that is needed. It is also possible to synchronize the transfer speed with the image shift due to the rotation of the Earth. This is the drift–scan mode, which allows registration of a long strip of the sky with a fixed telescope. The CCD technique has completely superseded astronomical photography. For more information, see Martinez and Klotz (1999).

- Infrared detectors. Infrared astronomy and astrometry are now gaining importance. Photon detectors have the property to absorb photons, which cause electron transitions and alter the electrical properties of the substrate. The photons may change the electrical conductivity (photoconductive detectors) or generate electron pairs, which are separated and produce a detectable potential difference (photovoltaic detectors). Now, they are often associated with a CCD, which ensures the readout. For instance, the NICMOS receiver (Near Infrared Camera for Multi Object Spectrograph), has an array dimension of $1 0 2 4 \times 1 0 2 4$ pixels. These, and a few other infrared detectors, are presented by L´ena (1996).

# 2.2 Basics of interferometry

The principle of interferometry is based upon the propagation properties of electromagnetic waves, whatever their domain (optical, radio, microwaves, etc.). The propagation of an electro-magnetic wave along a certain direction $O x$ is represented by its instantaneous amplitude $U$ at time $t$ :

$$
U = a \cos \omega \left( t - t _ { 0 } \right) ,
$$

where $a$ is the amplitude of the wave, $t _ { 0 }$ is a time at which $U$ is maximum, and $\omega$ is the angular frequency. It is related to the frequency by

$$
f = \omega / 2 \pi ,
$$

to the period of the wave

$$
T = 1 / f = 2 \pi / \omega ,
$$

and to the wavelength $\lambda ^ { \prime }$ by

$$
\lambda ^ { \prime } = { \frac { v } { f } } ,
$$

where $v$ is the speed of light in the medium. In vacuum, $v = c = 2 9 9 7 2 9 4 5 8 { \mathrm { m / s } }$ exactly. This actually defines the meter as the length of the path traveled by light in vacuum during a time interval of $1 / 2 9 9 7 2 9 4 5 8$ of a second. The quantity $c / v$ depends upon properties of the medium. It is the index of refraction of the medium

$$
n = { \frac { c } { v } } .
$$

It is always larger than one. For vacuum, $n = 1$ and is, therefore, often neglected in the equations. Generally, one considers only the wavelengths $\lambda$ in a vacuum, so that

$$
\lambda = { \frac { c } { f } } = { \frac { 2 \pi c } { \omega } } ,
$$

and

$$
\lambda ^ { \prime } = \frac { c } { f } = \frac { 2 \pi n c } { \omega } .
$$

Let us now assume that, at time $t _ { 0 }$ , the light has already propagated along the $O x$ axis by a distance $x$ . Then $t _ { 0 } = x / v$ and using the previous equations, (2.1) transforms into

$$
U = a \cos \left( \omega t - { \frac { 2 \pi n x } { \lambda } } \right) ,
$$

where the quantity $n x$ is called the optical path. For simplicity, one sometimes introduces a phase $\phi$

$$
\phi = { \frac { 2 \pi n x } { \lambda } } ,
$$

and $U$ becomes

$$
U = a \cos ( \omega t - \phi ) .
$$

These two results are fundamental for interferometry.

# 2.2.1 The superposition principle

This principle states that when two (or several) waves with the same wavelength are superposed and propagate along the same direction, they can be considered as being a single wave whose instantaneous amplitude is the geometric sum of the individual instantaneous amplitudes of the separate waves.

As an example, let us consider two monochromatic waves with the same amplitude, but different phases, $\phi$ and $\phi ^ { \prime }$ ,

$$
U = a \cos ( \omega t - \phi ) ; \quad U ^ { \prime } = a \cos ( \omega t - \phi ^ { \prime } ) .
$$

The combined instantaneous amplitude is

$$
\begin{array} { c } { { V = U + U ^ { \prime } = a [ \cos ( \omega t - \phi ) + \cos ( \omega t - \phi ^ { \prime } ) ] } } \\ { { = 2 a \cos \frac \phi 2 \cos \left( \omega t - \frac { \phi + \phi ^ { \prime } } 2 \right) . } } \end{array}
$$

The new amplitude,

$$
\begin{array} { l } { { \displaystyle { \cal A } = 4 a ^ { 2 } \cos ^ { 2 } \frac { \pi } { \lambda } ( n x n x ^ { \prime } ) } } \\ { { \displaystyle ~ = 2 a ^ { 2 } \left( 1 + \cos \frac { 2 \pi n ( x - x ^ { \prime } ) } { \lambda } \right) , } } \end{array}
$$

depends upon the difference of optical paths of each wave as expressed in units of wavelengths. Thus, there can be both constructive and destructive interference between the two waves, and the resulting amplitude can be anything between 0 and $2 a$ .

# 2.2.2 Illumination

The intensity of light (or the illumination) is proportional to the square of the instantaneous amplitude of the wave

$$
I \cong { \frac { 1 } { T } } \int _ { 0 } ^ { T } U ^ { 2 } \mathrm { d } t = { \frac { a ^ { 2 } } { 2 } } .
$$

Applying this to the amplitude (2.7), one gets

$$
I \cong 2 a ^ { 2 } \cos \frac { 2 \pi } { \lambda } ( n x - n ^ { \prime } x ) .
$$

If we assume that the resulting wave is observed in such a way that the difference of optical paths varies with time, the illumination will change with time. If different paths correspond to different points on a screen, one will see periodic patterns of illuminated and dark regions; these are the interference fringes. The most classical example is Young’s experiment in which two small holes in a diaphragm allow only a plane wavefront (hence with the same phase) to cross. By diffraction, each of them illuminates a large surface of the screen (Fig. 2.1). In some places, the difference of optical paths is exactly an integer number of wavelengths, and the illumination is maximum. In other places, when this difference is equal to an integer number of wavelengths plus half a wavelength, then $I = 0$ . The pattern of illumination is a succession of dark and light regions called interference fringes.

# 2.2.3 Coherence length and bandwidth

Natural light is never strictly monochromatic. Even with the most narrow filters, a light beam contains rays of different wavelengths, or frequencies,

$$
\begin{array} { r } { \lambda _ { 0 } - \Delta \lambda \le \lambda \le \lambda _ { 0 } + \Delta \lambda } \\ { f _ { 0 } - \Delta f \le f \le f _ { 0 } + \Delta f . } \end{array}
$$

![](images/da75a40dd3975ee80a2bc9f219e86a063cf4852e33dd44f2728c13e4c69fe8f5.jpg)  
Fig. 2.1. Scheme of Young’s experiment and the structure of fringes.

If such a beam is allowed to interfere, for instance in Young’s experiment, each ray system with a given wavelength, $\lambda$ , will produce a fringe pattern of its own and the ensemble will mix. In points for which $x = x ^ { \prime }$ , for all $\lambda$ , $I$ is maximum. It is called white, or central fringe. But the next ones will be slightly displaced, resulting in a blurring which increases when $x ^ { \prime } - x$ increases. It increases more quickly for large $\Delta \lambda$ than for small $\Delta \lambda$ . At a certain limit, fringes become indistinguishable. There is a mathematical definition of this limit. It is called the coherence length, whose value is

$$
\Delta x = \lambda ^ { 2 } / \Delta \lambda .
$$

Transforming this into frequencies one gets the bandwidth

$$
\Delta f = c \Delta \lambda / \lambda ^ { 2 } .
$$

The time taken by the light to travel $\Delta x$ is called the coherence time

$$
\Delta t = 1 / \Delta f .
$$

Examples. For $\lambda = 0 . 5 \mu \mathrm { m }$ and a filter (bandwidth) of $1 \mathrm { n m }$ , the coherence length is $\Delta x = 0 . 2 5 \mathrm { n m }$ .

For $f = 1 0$ GHz $\lambda _ { 0 } = 3 \mathrm { m }$ ) and a bandwidth of $2 \ : \mathrm { M H z }$ , the coherence time is $0 . 5 ~ \mu \mathrm { s }$ .

![](images/a2f10dccff42d1e821c1a499ff9881ee43d8e02daceaba096cc72ba7b3600b7a.jpg)  
Fig. 2.2. Principle of a Michelson North–South interferometer. In this figure, it is assumed, for simplicity, that the star is in the meridian plane containing the two telescopes.

# 2.3 Stellar interferometry

# 2.3.1 Principle of the Michelson interferometer

Let two identical telescopes point at some given star. Let us first assume that it is a unique point-like source and all rays in a plane perpendicular to the direction of the star have the same phase $\phi$ . Let us place some mirrors in such a way that the two beams are recombined into a single one. Figure 2.2 presents a schematic view of such an interferometer at a moment when the star and the two axes of the telescopes are in the same vertical (meridian) plane. If $R$ is the receiver, the optical path from the wavefront $P$ , for telescope 1, is

$$
x _ { 1 } = A B + B C + C D + D R .
$$

For telescope 2, it is

$$
x _ { 2 } = P P ^ { \prime } + A ^ { \prime } B ^ { \prime } + B ^ { \prime } C ^ { \prime } + C ^ { \prime } D ^ { \prime } + D ^ { \prime } R .
$$

We assume that the segments directly attached to the interferometer are well known or can be calibrated.

If the mirror $D R D ^ { \prime }$ is mobile along $C C ^ { \prime }$ , one can put it in such a way that $x _ { 1 } = x _ { 2 }$ , so that $R$ receives the central fringe of the interferometric pattern built up by the two beams.

If now $D D ^ { \prime }$ is servo controlled by $R$ in such a way that $R$ always receives the central fringe, the measurement of $C D - C ^ { \prime } D ^ { \prime }$ equals $P P ^ { \prime }$ and its variations with time, while the direction of the star changes because of the rotation of the Earth. The quantity $P P ^ { \prime }$ is the optical path difference of the rays at the entrance of each telescope or, at the arrival at the baseline $C C ^ { \prime } = d$ of the interferometer. In the case described by Fig. 2.2, this path difference $\Delta x = d \sin z$ where $z$ , is the angle of the zenith distance of the star.

This property can be extended to any configuration of the interferometer, and if, in some local system of coordinates, the unit vector of the direction of the star is S and $\mathbf { B }$ is the base vector of the interferometer, one has

$$
\Delta x = \mathbf { S } \cdot \mathbf { B } .
$$

In other terms, measuring $\Delta x$ gives a relation between the apparent direction of the star and the base vector attached to the Earth.

The main limitations in Michelson astrometric interferometry are the stability of the baseline throughout the night, the accuracy of the laser interferometers that monitor the positions of vital parts of the optical design, and the evaluation of the refraction in a consistent manner throughout the night. Another difficulty comes from the instability of the images due to atmospheric turbulence. More critical is the fact that this turbulence deforms the wavefront differently in each telescope, so that a stochastic additional error in the optical path difference is introduced. The region of the sky within which the refraction effect is sufficiently uniform to permit interferometry is called the isoplanatic patch. Its importance varies depending on the seeing during the observation. In any case, it represents a natural limitation to the precision of the instrument, generally a few milliarcseconds. To get rid of it, one should use active, or adaptive, optics, which are now commonly in use in large telescopes, but are very expensive and would represent an additional complication to the instrument.

# 2.3.2 Other uses of optical interferometry

Since A. Labeyrie (1975) obtained the first fringes on a two-telescope interferometer, many other optical interferometers have been built and become operational. But they have had an objective that is less difficult to reach than determination of star positions over wide angles. The objective was to determine the apparent diameters of stars.

Each point of a star’s surface emits independently of the others, so that it produces an independent interference pattern. The superposition principle does not apply, and the illumination produced is the sum of the individual illuminations by elementary fringes.

If the baselines are small, the differences of optical paths between various points on the star are small, and the interference patterns are very similar, resulting in a blurring, which is measured by the fringe visibility

$$
V = { \frac { I _ { \mathrm { m a x } } - I _ { \mathrm { m i n } } } { I _ { \mathrm { m a x } } + I _ { \mathrm { m i n } } } } .
$$

One can show that, in the case of a North–South horizontal interferometer observing in the meridian plane,

$$
V = \frac { J _ { 1 } ( 2 \pi D R \cos \phi \cos \delta ) } { \pi D R \cos \phi \cos \delta } ,
$$

where $R$ is the radius of the star expressed in radians, $\delta$ is its declination, and $\phi$ is the latitude of the observatory. $J _ { 1 }$ is the first-order Bessel function. For different directions, the formula is somewhat more complicated, but the principle remains. Interferometers designed to determine $R$ can observe with different baselines, $D$ , so that by fitting the observed visibilities to formula (2.14), one determines $R$ . Various existing interferometers have baselines ranging from 12 to $6 0 \mathrm { m }$ or more, and the precision with which radii are determined is of the order of a few milliarcseconds. The result, however, may be biased, if the star has a noticeable limb darkening which, in this case, has to be modeled.

The same instruments are also able to determine the separation, the position angle, and the magnitude difference between the components of a double star. The observations must be performed in different directions of the sky using the Earth’s rotation to get a variety of viewing orientations. The modeling of the illumination is that of two separate point sources. In this case, the precision of a few milliarcseconds is also attained. Of course, an astrometric optical interferometer can also be used to measure visibilities, or interferometric responses, of a double star in what is called the imaging mode.

# 2.3.3 The main interferometers

The technology has advanced to the state that optical interferometers are now built in many places. Specifically, computer-controlled delay lines, laser metrology systems, and detectors are now possible at the accuracies and speeds necessary for optical interferometric astrometry measurements. Thus, a number of optical interferometers have been designed and are in stages between construction and routine operation. Space-based optical interferometers are under development. Short descriptions and references to these interferometers follow. All interferometers feature one or more actively controlled optical elements to compensate for atmospheric turbulence and image motion. Several have vacuum feed systems to avoid the effects of ground turbulence. All the smaller-aperture interferometers are Michelson interferometers, where the combination of the afocal beams takes place at one or more beam splitters. All interferometers employ optical delay lines (with the exception of ISI, which uses electronic delays) to remove the path difference in order to combine the beams of light within their coherence length. Note the large step between the classic interferometers and the new giant large-aperture interferometers. The latter require adaptive optics to co-phase the apertures.

![](images/0c230929bce182c0e3e4c8d131555b7fb6250021b952fed2cbb3ceb2f165ddf8.jpg)  
Fig. 2.3. General scheme of the main elements of the NPOI interferometer. Black dots indicate two possible observing configurations; (a) and (b) give different coverages of imaging planes.

# (i) Cambridge Optical Aperture Synthesis Telescope (COAST)

COAST incorporates five $4 0 ~ \mathrm { c m }$ telescopes in a Y configuration with a maximum separation of $4 8 \mathrm { ~ m ~ }$ . Up to four telescopes can be used simultaneously. It is designed to have telescopes up to $1 0 0 ~ \mathrm { m }$ apart. This is primarily an imaging system and they plan to image the surfaces of giant stars. More information is at http://www.mrao.cam.ac.uk/telescopes/coast/status.html.

(ii) Navy Prototype Optical Interferometer (NPOI)

NPOI is a large optical interferometer for both astrometry and imaging. There are three $2 5 0 \mathrm { ~ m ~ }$ legs in a Y configuration with four astrometric huts within the inner $3 8 \mathrm { m }$ baselines and stations for imaging siderostats providing baselines between $2 \textrm { m }$ and $4 4 0 \mathrm { ~ m ~ }$ as shown in Fig. 2.3. Six fast vacuum delay lines for astrometry can be augmented by long delay lines for imaging. The siderostats are $5 0 \mathrm { c m }$ feeding image compressors and vacuum light pipes to the delay lines and detectors. The beam combiners will accept up to six beams. This is a joint project of the US Naval Observatory, Naval Research Laboratory, and Lowell Observatory, being built on Anderson Mesa in Arizona. More information is available at http://usno.navy.mil/projects/npoi.

# (iii) Sydney University Stellar Interferometer (SUSI)

SUSI has been designed to operate with North–South baselines from $5 \mathrm { m }$ to $6 4 0 \mathrm { m }$ , with intermediate baselines forming a geometric progression increasing in steps of $\sim 4 0 \%$ . This gives resolutions from 20 mas to $7 0 \mu \mathrm { a s }$ at wavelengths of $4 5 0 \ \mathrm { n m }$ . There is one East station for a potential East–West arm of the interferometer.

This interferometer has the highest resolving power of all on the longest baseline, making it suitable for the determination of the diameters of early type dwarfs. More information is available at http://www.physics.usyd.edu.au/astron/susi/susi baselines.html.

(iv) Infrared-optical Telescope Array (IOTA)

IOTA is a Michelson stellar interferometer located on Mt Hopkins, Arizona, with three $4 5 \ \mathrm { c m }$ collectors which can be located on different stations on each arm of an L-shaped array of $1 5 \mathrm { ~ m ~ }$ by $3 5 \mathrm { ~ m ~ }$ , with a maximum baseline of $3 8 ~ \mathrm { m }$ . At visible and near-infrared (near-IR) wavelengths, combination occurs at a beam splitter. Also at near-IR wavelengths, the FLUOR experiment combination occurs in single-mode fibers. Detection is done in the near-IR with an HgCdTe NICMOS3 array and in the visible with a CCD. Organizations operating this array include the Smithsonian Astrophysical Observatory, Harvard University, and the University of Massachusetts. More information is at   
http://cfa-www.harvard.edu/cfa/oir/IOTA/Description.html.

(v) Infrared Spatial Interferometer (ISI)

ISI is a two-telescope interferometer operated by the University of California at Berkeley on Mt Wilson Observatory. The telescopes are 65 inch fixed parabolic mirrors and 80 inch flat mirrors, operating as siderostats. Observations are made at mid-infrared wavelengths of $1 1 \mu \mathrm { m }$ using the heterodyne technique with a CO laser as a local oscillator. The telescopes, electronics, and computer control systems are contained in trailors, which can be moved to reconfigure the baselines. A third telescope is being added to the interferometer and three baselines will be operated simultaneously. More information is at http://isi.ssl.berkeley.edu/system.html.

(vi) Palomar Testbed Interferometer (PTI)

The PTI is a K-band $1 1 0 \mathrm { ~ m ~ }$ maximum baseline stellar interferometer located at Palomar Observatory. Two different baselines are available. This interferometer was conceived, designed, and constructed primarily as an engineering facility to demonstrate ground-based differential astrometry for the detection of faint companions and planets. More information is available at   
http://huey.jpl.nasa.gov/palomar/.

(vii) Center for High Angular Resolution Astronomy (CHARA) Array The CHARA Array has six $1 \mathrm { m }$ telescopes dispersed in a two-dimensional layout with a maximum baseline of $3 5 0 ~ \mathrm { m }$ on Mt Wilson in California. The light from the six telescopes is conveyed through vacuum tubes to a central Beam Synthesis Facility. More information about CHARA can be found at http://www.chara.gsu.edu/CHARA/array.html.

(viii) The Grand interferometre \` a deux t \` elescopes (GI2T) ´

This optical and infrared interferometer in France allows siderostats to be placed along a North–South baseline with separations between $1 2 \textrm { m }$ and $6 5 \mathrm { ~ m ~ }$ . The telescopes have $1 . 5 \mathrm { m }$ diameter primaries and feature a unique alt-azimuth mount based on a concrete sphere. More information can be found at http://www.obs-nice.fr/fresnel/gi2t/en/.

# (ix) Keck Interferometer $( K I )$

The Keck Interferometer will combine the two $1 0 ~ \mathrm { m }$ Keck telescopes with four proposed $1 . 8 \mathrm { m }$ outrigger telescopes as an interferometric array. A Michelson beam combination will be used for the $8 5 \mathrm { ~ m ~ }$ baseline of the Kecks and the $2 5 \mathrm { - } 1 4 0 \mathrm { ~ m ~ }$ baselines of the outriggers. The Kecks have adaptive optics and the outriggers will have fast tip–tilt correction. The co-phasing system uses active delay lines in the beam combining room and dual-star modules at each telescope. Back-end beam combiners will be two-way beam combiners at $1 . 5 { - } 3 . 4 ~ \mu \mathrm { m }$ for fringe tracking, astrometry, and imaging, a multi-way combiner at $1 . 5 \mathrm { - } 5 ~ \mu \mathrm { m }$ for imaging, and a nulling combiner for high dynamic range observations at $1 0 ~ { \mu \mathrm { m } }$ . The first interferometric fringes were observed in March 2001. More information is available at http://huey.jpl.nasa.gov/keck/publicWWW/techdesc/index.html.

(x) Large Binocular Telescope (LBT)

The LBT is two $8 . 4 \mathrm { m } F / 1 . 1 4 2$ primary mirrors on a common mount on Mt Graham in Arizona. This gives the light-gathering power of a single $1 1 . 8 \mathrm { m }$ telescope and the resolving power of a $2 2 . 8 \mathrm { m }$ telescope. The focal stations will be infrared, dual $F / 1 5$ , Gregorian, and phased combined, reimaged $F / 1 5$ , center. The instruments will be interferometric imaging at $0 . 4 { \ - } 4 0 0 \ \mu \mathrm { m }$ , infrared imaging/photometry at $2 . 0 { - } 3 0 ~ \mu \mathrm { m }$ , wide-field multi-object spectroscopy at $0 . 3 \mathrm { - } 1 . 6 ~ \mu \mathrm { m }$ , faint-object/ long-slit spectroscopy at $0 . 3 \mathrm { - } 3 0 ~ \mu \mathrm { m }$ , and high-resolution spectroscopy at $0 . 3 -$ $3 0 ~ { \mu \mathrm { m } }$ . More information is at   
http://medusa.as.arizona.edu/ibtwww/tech/lbtbook.html.

(xi) The Very Large Telescope Interferometer (VLTI)

This array will ultimately combine all four $8 \mathrm { m }$ telescopes of the European Southern Observatory’s VLT on Cerro Paranal in Chile. Five auxiliary telescopes with $1 . 8 \mathrm { m }$ primaries are planned to provide more baselines with a maximum length of about $2 0 0 \mathrm { m }$ . Interference fringes were observed between two of the $8 \textrm { m }$ telescopes in October of 2001. The instruments include near- and far-infrared beam combiners, as well as a camera for phase-referenced imaging and microarcsecond astrometry. More information is available at http://www.eso.org/projects/vlti/.

# 2.3.4 Fizeau interferometer

The major drawback of Michelson interferometry is that the useful field of view is very small and does not exceed a few seconds of arc. There are essentially two reasons for this. One is that the collimated light has to travel for at least one half of the baseline $B$ . A small displacement in the field of view by an angle $\alpha$ displaces the ray by $B \alpha$ , assuming no magnification. In practice, it is much larger unless the intermediary optics are very large. The second reason is that there is no geometric relation between the images produced by the two telescopes, so that the superposition of rays disappears very quickly from the recombination center and no fringes are built.

The solution to suppress these problems is that a single telescope is used to produce the two interfering rays. These are separated by occulting the whole mirror with the exception of two entry pupils. This is the principle of the Fizeau interferometer: both entrance pupils produce the same image, and therefore the rays interfere uniformly all over the field of view, limited only by the aberrations of the optics in places where images are distorted differently. Therefore, the useful field can be as large as $1 ^ { \circ }$ , as large as the field of view of the full telescope.

A Fizeau interferometer is much more difficult to build and the baselines are necessarily small, of the order of the diameter of a telescope mirror. Actually, it is not necessary to have the full telescope built, but the two areas must be shaped and solidly placed, one with respect to the other, as if they are parts of a unique, large mirror. Such systems have not yet been built, but they have been proposed to be flown in several future astrometric space missions. The advantage would have been that interferences would be produced for all stars present in the field of view, allowing simultaneous determinations of their relative positions. But actually, the Fizeau interferometer design has not been retained.

# 2.3.5 Speckle interferometry

This new observational method was introduced by A. Labeyrie (1970). The turbulent atmosphere near the ground consists of cells $5 { - } 2 0 \mathrm { c m }$ across, depending on the wind and the thermal response of the ground. The light coming from a point-like source and the crossing cells interfere and produce irregular patterns at the focus of the telescope called speckles, each corresponding in size to the resolving power of the instrument. Hence, the speckles contain all the angular information that the instrument might have provided were the atmosphere ideally calm. The speckles move and produce fuzzy and spread out images, whose dimensions depend on the seeing. But if the exposure time is as short as $1 / 1 0 0 \mathrm { { t h } }$ of a second, they do not have the time to move, or deform significantly, and each is a noisy image of the star’s Airy diffraction disk. The theory of the speckle interferometry was made first by Korff (1973) and improved by Roddier and Roddier (1975). In practice, it consists of combining the information of these speckles, recorded on a fast CCD (see Section 2.1), and transferred to a computer which computes an autocorrelation function of a large number of images taken during the observation. Finally, one has to smooth out the autocorrelations and subtract the background. One way is to compute the Fourier transform of the autocorrelation function and interpret the information contained in the Fourier space.

This technique recovers much of the resolution power of telescopes. For instance, a $4 \mathrm { m }$ telescope with the best seeing gives images larger than 0.5, while the resolving power of the speckle interferometry is 0.03. This is illustrated in Section 12.3.2 as applied to observations of double stars.

# 2.4 Applications of time measurements

Several new astrometric techniques are not based on direct measurements of angles, but on an indirect method. The observation consists either of a measure of time intervals, or involves synchronization of very stable clocks.

Time or frequencies are, at present, the physical quantities that are measured with the greatest accuracy. The time scale universally adopted is the international atomic time (TAI: Temps Atomique International), which is based on cesium frequency standards operated by some primary metrological laboratories. At present, the most accurate is the atomic fountain based upon cold – and consequently with very small Doppler broadening – cesium atoms producing the spectral line selected to define the second, and set by definition as having a frequency $f _ { 0 } =$ $9 1 9 2 6 3 1 7 7 0 \mathrm { H z }$ . The first ever built operates regularly at the Paris Observatory with an uncertainty of $1 0 ^ { - 1 5 }$ . It is now approaching $5 \times 1 0 ^ { - 1 6 }$ . Several other such cesium fountain clocks have been built using the same technology, and have similar accuracies.

# 2.4.1 The Global Positioning System and TAI

In principle, the Global Positioning System (GPS) is a ranging system that allows the determination of the position of a point on the Earth from measured distances and Doppler shifts to several satellites, whose orbits are very well known with respect to a terrestrial reference frame (see Chapter 9). It is essentially a navigation and geodetic tool, but it is used as an off-line tool in many astrometric applications, so that it is natural to present it here. A detailed description of the system and its uses can be found in Hofmann-Wallenhoff et al. (1992).

All satellites have on-board clocks that are synchronized to a unique time scale, called the GPS time scale, which is, in turn, well defined with respect to the TAI. They emit signals at some specified instant, $t _ { \mathrm { s } }$ , of the on-board clock, and the ground stations record the arrival time, $t _ { \mathrm { g } }$ , in its own scale, which has to be corrected to fit the GPS time scale. The range is derived from $R = c ( t _ { \mathrm { g } } - t _ { \mathrm { s } } )$ after corrections for ionospheric and atmospheric refraction and relativistic effects.

The GPS satellites transmit the orbit ephemerides, but more precise orbital elements are available after a few days from the International GPS Service (IGS), which determines them anew from observations made at about 40 sites around the world. In the satellite transmission, a formula to transform the on-board time into the GPS time is given. The signal is emitted at two frequencies, which allow determination of the first-order propagation refraction correction.

By using the improved IGS orbit, and accumulating data over several days, it is possible to locate the receiving station with an uncertainty of $1 \mathrm { c m }$ in the dualfrequency mode.

GPS also plays a major role in establishing TAI. If a satellite is observed simultaneously by two stations with known positions on the Earth, one gets the difference between the times provided by the two ground clocks.

The TAI unit interval is set to agree with the observations of atomic standards, but the stability is ensured by the comparison of more than 200 atomic clocks dispersed around the world and intercompared using the GPS-based technique. The clocks on board the satellites are intermediary between the users and master clocks in the US Naval Observatory, well connected to TAI. The relative accuracy of TAI is of the order of one in $1 0 ^ { 1 4 }$ , and its stability is evaluated to be of a few units in $1 0 ^ { 1 5 }$ . Many clocks are built industrially and have an accuracy and stability better than one in $1 0 ^ { 1 3 }$ for periods ranging from one hour to one year. A much better short-range stability is achieved by hydrogen masers (down to one part in $1 0 ^ { 1 5 }$ during a few hours, $1 0 ^ { 1 4 }$ for up to one month), but the link to the actual definition of the second is not yet as good. The frequency standards are very useful in some astronomical applications, such as Very Long Baseline Radio Interferometry, in which a very good, short-term stability of frequencies is needed.

# 2.4.2 VLBI (Very Long Baseline Interferometry)

The resolving power of an interferometer is of the order of $\lambda / D$ . So, for $D = 2 0 \mathrm { m }$ at $\lambda = 0 . 5 \mu \mathrm { m }$ , it is about $1 0 \mathrm { \ m a s }$ , a result that can be somewhat improved by adding up many observations. Unless $D$ becomes very large, the milliarcsecond seems to be a limiting boundary. But for observations in the radio domain, with wavelengths of a few centimeters, to reach analogous precision necessitates a very large $D$ , namely a few thousand kilometers. While there exist connected radio interferometers, which are based on the same principles as optical, as for instance the Very Large Array (VLA; Thomson et al., 1980), their dimensions hardly reach 230 kilometers (MERLIN in England; Thomasson, 1986). For better accuracy, a completely different approach is taken. This is the case of VLBI. A basic book on VLBI is by Felli and Spencer (1989). Its applications to astrometry are discussed in Walter and Sovers (2000).

The basic idea is to record signals that are received in each radio telescope, and then correlate them in a computer. An antenna transforms the electro-magnetic field of a radio wave into an electric potential, $v$ , proportional to the instantaneous amplitude of the wavefront

$$
v = b \cos ( \omega t - \phi ) ,
$$

where $\phi$ is the phase of the wave to which a constant, instrumental dephasing is added. Remembering that $3 \ \mathrm { c m }$ wavelength corresponds to a $1 0 \ \mathrm { G H z }$ frequency,

such a frequency cannot be continuously analyzed. A local oscillator, generally a hydrogen maser, produces a stable reference frequency,

$$
v ^ { \prime } = b ^ { \prime } \cos \omega _ { 0 } t ,
$$

where $\omega _ { 0 }$ is close to $\omega$ .

These frequencies are mixed in a special heterodyne circuit. After filtering out high-frequency terms, there remains a periodic electrical intensity proportional to $b$ and $b ^ { \prime }$ , an angular frequency $\omega - \omega _ { 0 }$ , and the same phase $\phi$

$$
\begin{array} { r } { I \cong b b ^ { \prime } \cos \left( ( \omega - \omega _ { 0 } ) t - \phi \right) . } \end{array}
$$

Choosing $\omega _ { 0 }$ in such a way that the frequency of $\omega - \omega _ { 0 }$ is of the order of $1 { - } 2 \mathrm { M H z }$ , it is now possible to sample this frequency and represent numerically on a tape the time variations of (2.15). The timing is accurately marked on the same tape.

At a second radio telescope the same procedure is followed on the same radio source. Then both recordings are brought together and compared. The better the local clocks are synchronized, the better one can recognize that the two records correspond to the same wavefront. An approximate reckoning of the path difference produces a first approximation to the time delay, $\Delta t _ { 0 }$ , between the two wavefronts. Let $\Delta t$ be the correction to $t _ { 0 }$ that gives the exact time delay. Then the correlation between the two signals is a maximum. So, the special computer, called a correlator, computes the value of $\Delta t$ such that the normalized correlation function

$$
R ( \Delta t ) = \frac { \int _ { t _ { 1 } } ^ { t _ { 2 } } I _ { 1 } ( t ) I _ { 2 } ( t + t _ { 0 } + \Delta t ) \mathrm { d } t } { \int _ { t _ { 1 } } ^ { t _ { 2 } } I _ { 1 } ^ { 2 } \mathrm { d } t \int _ { t _ { 1 } } ^ { t _ { 2 } } I _ { 2 } ^ { 2 } \mathrm { d } t }
$$

is a maximum.

The actual determination of the time delay at a reference instant is much more complex. One has first to correct for the unknown ionospheric and tropospheric refractions. This is done by observing simultaneously at two frequencies, the $S$ band $( 2 3 0 0 ~ \mathrm { M H z } )$ ) and the $X$ band $( 8 4 0 0 ~ \mathrm { M H z } )$ ). One has also to take into account the continuous variation of the received frequency due to the Doppler shift produced by the rotation of the Earth.

In order to increase the precision of the result, two techniques are simultaneously used. First one increases the time interval $t _ { 1 } - t _ { 2 }$ present in formula (2.16), but this implies a very strict identification of the time markers in both tapes. Independent of the stability provided by hydrogen masers, the station clocks must indicate the same time scale. This is done through frequent synchronization using the GPS system. The other technique is to separate the observed band into a number of adjacent narrow bands and make a simultaneous reduction on a parallel computer. The Mark III receiver and correlator work simultaneously on the $S$ and $X$ bands, subdivided into 28 channels of $2 \mathrm { M H z }$ bandwidth. Even with a two-point sampling per period, more than 100 million bits have to be processed for each second of observation.

![](images/2fde3983f81e385d3a178da990cebc8ae483b044d896c4e3856139b2c2525071.jpg)  
Fig. 2.4. Histograms of uncertainties of the coordinates of the 212 defining radio sources of the ICRF (Ma et al., 1998).

The fundamental equation applied to interpret the data is formula (2.13). So VLBI can be used to determine the baseline, assuming the celestial coordinates of the sources, usually quasars, are known. This gives information both on the geodetic position of the antennae and the parameters of the rotation of the Earth. Conversely, knowing the position of antennae and the elements of the Earth’s rotation, one can determine the directions, S, of sources.

Actually, there are too many parameters to be determined from a single baseline. So, networks of several radio telescopes are operated for any observing program. The uncertainty of a single observation of a source is about 5 mas, but synthetic treatment of many baselines gives the parameters of the rotation of the Earth with uncertainties of about 0.2 mas. A combined solution for source positions has been iterated by IERS (International Earth Rotation Service). It uses results from the several existing VLBI networks. A total of 606 sources constitutes the final solution, the International Celestial Reference Frame (ICRF). But most of them have changing structures, and must be continuously monitored. Only 212 have very good observing records, and are considered as primary reference sources (see Fig. 2.4, and Section 7.2).

Furthermore, the positions of about 20 radio telescopes contributing to the VLBI networks are determined with uncertainties of the order of $0 . 5 ~ \mathrm { m m }$ . They are the primary net of positions upon which the International Terrestrial Reference Frame (ITRF) is based (see Chapter 9).

A difficulty with VLBI – in addition to its very complex and costly operations – is that the great majority of observable radio sources are optically faint extragalactic objects. This is optimum for defining a non-rotating reference system. But such a reference frame is necessary also for stars, and the problem is that there are almost no stars emitting radio waves with a sufficient intensity to be observable by VLBI. The link between radio and optical reference coordinates relies at present on only 11 radio stars observed with VLBI and a few dozens of other stars which have been observed with connected interferometry (VLA, MERLIN), but, in those cases, with only a few milliarcsecond uncertainty.

# 2.4.3 Laser ranging

Another use of timing is measuring distances. Since the meter is defined as a function of the velocity of light in vacuum, measuring the time during which a light pulse travels from a terrestrial source to and back from a target is actually a measure of twice the distance, provided the necessary corrections for velocity through air, relative motions, and the instrument delays are applied. In addition to artificial satellites, widely used as targets for geodetic purposes (see Chapter 9), the astronomical application is laser ranging to the Moon. Let us describe first the lunar laser ranging, which is the most difficult to realize and operate.

The main part of laser ranging equipment is a Q-switched laser which provides very short light pulses. The most common type is a crystal containing neodymium (YAG) which emits in near infrared $( 1 . 0 6 4 ~ \mu \mathrm { m } )$ ). The light beam then crosses a frequency-doubling system, so that the actual emission includes both 1.064 and $0 . 5 3 2 \mu \mathrm { m }$ . The width of a pulse can now be as short as 0.1 ns with a repetition rate of $1 0 \ \mathrm { H z }$ or more. Note that the length of a 0.1 ns pulse is only $3 \mathrm { \ c m }$ , so that the uncertainty of the distance due to the scatter of photons around the center of the pulse is only $0 . 7 5 \mathrm { c m }$ .

The light pulse is collimated towards the Moon by a large telescope ( $1 . 5 0 \mathrm { ~ m ~ }$ aperture in the case of the CERGA lunar laser, which has the best performance) guided by an ephemeris of one of the retroreflectors deposited on the Moon by three US Apollo and one Soviet Lunokhod missions (Kovalevsky, 2002). These return the received light beam in the direction of its source. On the ground, the same telescope directs the return photons to a photomultiplier. The return time is determined by an event timer that receives signals from the outcoming laser pulse and the receiver.

The main difficulty is to recognize the return signal from noise generated by Moon light. This is done using a very narrow band filter in front of the photomultiplier, which is opened during only 50 ns around the theoretical return time as computed from the ephemeris. Because of the tremendous loss of photons due to atmospheric turbulence, the diffraction in the telescope and the retroreflector, and the transmission factors of the optics, the atmosphere, and the receiver, a real return is only occasionally detected. Generally an observing session lasts $1 0 { - } 1 5 \ \mathrm { m i n }$ , representing something like 6000 pulses, out of which about 10–40 are recorded in good nights. They are recognized from the background by computing the residuals from comparing with the ephemerides; they all have the same residual whereas noise photons have a random distribution in time.

At present, after various instrumental and calibration corrections, the uncertainty achieved is of the order of $5 \mathrm { m m }$ and the accuracy is probably about $1 \ \mathrm { c m }$ . This is a major tool for the study of the Earth–Moon dynamics, including the rotations of both bodies. It also provides information on general relativity parameters and dynamical reference frames.

Satellite laser ranging systems are built under the same scheme. However, the satellites being much closer to the Earth, the efficiency of the illumination is much larger than in the case of the Moon. This allows the recognition of the returns by the fact that two or more photoelectrons are received within the pulse time. This is achieved in spite of the fact that artificial satellite ephemerides are not as accurate. It is necessary to broaden the outcoming beam to several tens of arcseconds. Many of the satellite laser ranging systems in existence have accuracies of the order of $2 \mathrm { c m }$ .

# 2.4.4 Planetary radars

Although optical ranging is limited to the neighborhood of the Earth and where retroreflectors are located, it is possible to use large radio telescopes to send pulses to planets, minor planets, or satellites, and then to receive return signals, so that, with the same principles, the distance between a point on the Earth and the closest portion of the surface of the planet may be obtained. The terrestrial planets, Jupiter satellites, and many asteroids have been ranged by this technique. Difficulties arise from the fact that the points on the surface are located at different distances from the center of mass of the planet, so that the main source of error is not the timing – which is made to a microsecond precision – but the uncertainty of the shape of the satellite or the planet, which can be of the order of a few kilometers. Nevertheless, ranging provides the most accurate measurements of Solar System positions for the construction of planetary ephemerides.

In the case of minor planets, the radar technique has been used to determine the shapes of some of these bodies and their rotation periods. Additional information is provided, in this case, by the broadening of the Doppler width of the signal. Radar observations of asteroids are also essential to the preparation of space missions to these bodies and to the control of the operations of the space probe around the encounter.

# 2.4.5 Pulsar timing

This is a very important development of timing techniques applied to astronomy. It consists of observing the time variations of the emissions of a pulsar, and studying their periods and the evolution of the period with time. These observations are useful in discussing the reference frames and are used as a test of Solar System ephemerides accuracies. Their contribution as a time source has been suggested, but is still uncertain.

The various aspects of the interpretation of these observations are discussed in Section 14.7.

# 2.5 Launched space astrometry satellites

Among the most limiting factors in ground-based astrometric observations are the atmospheric refraction and turbulence, the deformations of the mechanical parts of an instrument, and the fact that from no single point on the Earth can one observe the whole sky. These drawbacks are suppressed for an astrometric instrument in space. However, other difficulties then arise: the cost of space instrumentation, launch, and operations, and the instability of the satellite which is subject to a number of disturbing forces, while the Earth is a very stable platform whose motions are very well monitored and modeled.

Space astrometry was born in 1989 with the launch of Hipparcos and, in 1990, of the Hubble Space Telescope. While the first satellite was essentially an astrometric satellite – although it also obtained important results in photometry – the second is a multi-purpose space telescope which has, among others, astrometric capabilities. We will briefly describe them, referring the reader to more complete descriptions of the instruments and their reduction procedures, which are much too complex to be summarized in a few pages.

# 2.5.1 Hipparcos

The main principle of Hipparcos is to scan the sky along great circles in order to determine, on a reference great circle (RGC), the abscissae of stars situated in a small ring around the RGC.

Then, by varying the position of the RGCs following a certain scanning law, which allows all the parts of the sky to be successively observed, one gets, for each star, a certain number of values of abscissae in different directions at different times. From this one can determine the five astrometric parameters of the stars, namely two positional coordinates, two components of the proper motion, and the parallax. Additional information on double and multiple stars is also obtainable from the data.

![](images/e69358e44fe1a97186a39b2c75174b6ccb265cc4284dc756371052a0b9b0a672.jpg)  
Fig. 2.5. Schematic view of the Hipparcos instrument. The images $I _ { 1 }$ and $I _ { 2 }$ of stars $S _ { 1 }$ and $S _ { 2 }$ are formed on the same grid which modulates the illumination while the satellite rotates around an axis perpendicular to the plane of the figure.

The instrument essentially consists of a Schmidt telescope receiving light from two regions of the sky separated by a basic angle of $5 8 ^ { \circ }$ . This is achieved by two glued mirrors at an angle of $2 9 ^ { \circ }$ , as shown in Fig. 2.5. As the satellite rotates around an axis parallel to the intersection of the mirrors, the stellar images transit through a double grid formed of a star-mapper and a main grid. The star-mapper consists of four chevron slits and four slits perpendicular to the motion of the images. Its primary task is to recognize the stars whose positions have been determined before launch from ground-based astrometry. They are contained in the Input Catalogue of more than 118 000 stars of the observing program of the satellite (Turon et al., 1992a). This recognition provides an equation to the continuous determination of the orientation of the satellite as a function of time. It is indeed of the utmost importance to the project that, at each instant, the orientation is known. It is actually represented either by spline functions or by trigonometric functions associated with linear functions of time defined between successive gas jet thrusts used to maintain the scanning law. The on-board determined orientation is used to compute at every instant the position of a star image on the main grid.

![](images/388c750258d82c818c66a4350e7b6195cfc88cd944a3753d3520330cbbaf9baf.jpg)  
Fig. 2.6. Example of modulations by the main grid of a single star (upper curve) or a double star (lower curve). The vertical scale is the intensity in an arbitrary scale. The abscissae represent time.

The main grid is composed of 2688 parallel slits with a separation of 1.208. An image dissector tube collects the light in a small field of $3 0 ^ { \prime \prime }$ around the assumed position of the image, and registers the photon counts while the star light is modulated by the grid. Several stars can be observed successively during an observing frame of about $2 . 1 3 \mathrm { ~ s ~ }$ . The modulation is represented by a constant term and the first two harmonics, the phase of which represents the fraction of a grid step where the star was located at a given reference time $t _ { i }$ within each observing frame i. This gives the grid coordinate at time $t _ { i }$ provided that the positions given in the Input Catalogue and the orientation are precise enough to recognize on what grid step the star was located. The uncertainty for each grid coordinate is of the order of 15 mas. In the case of double stars, the modulations of the two components are combined and the phases of the harmonics are not equal (see Fig. 2.6). It is still possible, by comparing the modulation curves obtained at different RGCs, to reconstruct the relative positions and magnitudes of the components and correct the phases to represent that of the primary, or of the photocenter. From grid coordinates, it is possible to determine, for most of the 1500 stars observed during about $^ { 8 \mathrm { ~ h ~ } }$ , their abscissae on a fixed RGC and, in addition, to improve the orientation along the scan. This involves modeling of the instrument and the along-scan orientation, writing equations of condition for each star present in each observing frame, and solving about 40–50 thousand equations with about 3000 unknowns for abscissae, orientation spline functions, and calibration parameters. Each star is observed between 15 and 40 times, so that the average uncertainty of abscissae falls to about 3 mas.

During the mission, observations were made on about 2400 RGCs. A synthesis of all the results on the RGCs is made, each star having between 20 and 50 abscissae on independent RGCs. The principle of this synthesis is sketched in Fig. 2.7; the star moves along a curve representing the combination of its proper motion and its parallax, and the abscissa points are projections at different times of a point on the curve on the RGC. Descriptions of the reduction procedures of Hipparcos data are sketched in Chapter 8 of Kovalevsky (2002), or in van Leeuwen (1997). Full details appear in Volume 3 of the Hipparcos Catalogue (ESA, 1997). As a final result of the reductions, uncertainties in positions, yearly proper motions and parallaxes range between 0.5 and 1.5 mas for stars of magnitude brighter than 10 depending on their positions on the sky and the efficiency for these positions of the adopted scanning law (see also Section 11.6.1).

![](images/d7731166c742d0c6cd37b1e95dff119e96588b972d665e86675527783e952c38.jpg)  
Fig. 2.7. Apparent motion of a star, $S$ , and its projections $H _ { 1 } , \ldots , H _ { 5 }$ on reference great circles $C _ { 1 } , \ldots , C _ { 5 }$ .

# 2.5.2 Hubble Space Telescope

The Hubble Space Telescope (HST) is a $2 . 4 \mathrm { m }$ aperture Ritchey–Chr´etien telescope with a field of view of $1 4 ^ { \prime }$ radius. There are six instruments that share the focal surface and two of the initial instruments can be used for astrometry: the Fine Guidance Sensors and the Wide Field/Planetary Camera.

The Fine Guidance Sensors (FGS) occupy three $9 0 ^ { \circ }$ segments of an annulus of inner and outer radii $1 1 ^ { \prime }$ and $1 4 ^ { \prime }$ . They are essentially meant to be the guidance system of the telescope, but two are sufficient, so that the third one is available for astrometry (Fig. 2.8). A general description of the design, mode of operation and calibration were presented by Duncombe et al. (1991). The position of a point on the FGS is defined by two star selectors, which are two beam deflectors of fixed lengths, $a$ and $b$ , whose rotation angle is measured, and that bring the light from the star image to a detector assembly. The detector consists of two Koester interferometric prisms which produce different intensities, if the selectors are not exactly centered on the star image. The difference controls the positioning of the star selectors until the pointing is correct. The angles, $\theta _ { A }$ and $\theta _ { B }$ , together with the nominal angular projections of $a$ and $b$ on the sky, suffice to define the position of the star in some local system of coordinates. Pointing successively to several objects, while the telescope remains fixed through the other two FGSs, gives the relative positions of the observed objects in the sky with uncertainties of the order of 3–4 mas, essentially limited by the general jitter of the telescope.

![](images/5256c2da45e467aee35c29ef959708b15daade17e6511075530d9a365a7e9f52.jpg)  
Fig. 2.8. Fine Guidance Sensors and the positioning of star selectors.

The Wide Field/Planetary Camera is a combination of two cameras each based on four $8 0 0 \times 8 0 0$ CCD detectors. The planetary camera has a field of view of $6 8 ^ { \prime \prime }$ while for the wide field camera it is $1 6 0 ^ { \prime \prime }$ . The reduction of data for these cameras is based on the same principle as ground-based photography or CCD camera scanning (see Chapter 14). Let us note that while the Hubble repair mission did not improve the FGS, the Wide Field/Planetary Camera was replaced with the Wide Field Planetary Camera 2, with four CCDs and correcting optics in the re-imaging system, so the expected point-spread functions were achieved. More details are given in Seidelmann (1991).

# 2.6 Proposed space missions

The successes of Hipparcos and the astrometric use of the Hubble Space Telescope have led astrometrists to propose more sophisticated future missions that would greatly improve the results already obtained. Three projects are Hipparcos-like scanning missions allowing complete sky surveys: DIVA, FAME and GAIA. Another type of mission, SIM, consists of observations of individually selected stars as with the HST. All of them have been thoroughly studied and designed, but none of them has yet reached the stage of building. The first two have even been, possibly temporarily, descoped by the respective space agencies. Anyhow, we describe them all, because their principles will be the bases of future space astrometry.

![](images/46bfbff9f69cb1fc84ccde96b01db866eb4b5ddcb66e82d43d7ebb679ab71cb1.jpg)  
Fig. 2.9. Schematic view of the SIM configuration.

# 2.6.1 Space interferometry

The US Space Interferometry Mission (SIM) is an orbiting stellar interferometer consisting of two siderostats with equal apertures of $3 0 \mathrm { c m }$ collecting the light with a distance of $1 0 \mathrm { m }$ (Fig. 2.9). In addition, each pod has two steerable mirrors which are the collectors of two guide interferometers directed towards bright stars and are used to determine the orientation in space of the baseline during the observation period. The collected light is directed towards delay lines and a beam combiner. An accurate positioning of the collecting mirrors with respect to the beam combiner will be performed by infrared stabilised interferometers with an absolute accuracy of $1 ~ { \mu \mathrm { m / m } }$ . It is expected that SIM will be launched on an Earth-trailing solar orbit about 2010. During its five years of operation, about 10 000 objects as faint as magnitude 20 should be observed, with an uncertainty of $4 \mu \mathrm { a s }$ for wide-angle astrometric observations $3 \mu \mathrm { a s }$ for parallaxes). This will need an integration time of $1 \mathrm { ~ s ~ }$ for stars of magnitude smaller than 10, 200 s at magnitude 15, and more than $^ { 4 \mathrm { h } }$ for the faintest objects. For narrow-angle $( < 1 ^ { \circ } )$ astrometry, one expects to reduce uncertainties to $0 . 5 \mu \mathrm { a s }$ . More information is at http://sim.jpl.nasa.gov.

# 2.6.2 DIVA

DIVA was a proposed German project (Bastian et al., 1996; R¨oser, 1999) which has unfortunately been delayed. The scanning law and the rotation period were very similar to those of Hipparcos. A solid-angle beam combiner assembles two fields of view separated by $1 0 0 ^ { \circ }$ . The apertures are two rectangles of $2 2 . 5 \times 1 1 \mathrm { c m }$ . The equivalent focal length is $1 1 . 2 \mathrm { m }$ . The detection is done by four identical CCD mosaics, each consisting of ten $1 0 2 4 \times 2 0 4 8$ pixel CCDs.

A star image first crosses two star-mapper mosaics used for the recognition of the position of the incoming star and collecting data for astrometry and attitude determination. Then, the two science mosaics receive light by a diffraction grid. The scan direction is perpendicular to the fringes. Because the fringe separation is a function of the wavelength, the star-mapper is used to evaluate the color of the star, while the dispersed fringes provide spectrophotometric information.

The DIVA project was expected to produce a star map of 40 million stars to magnitude 15, a spectroscopic survey of 12 million stars, and a UV survey of 30 million stars. More information is at www.ari.uni-heidelberg.de/diva/diva.html.

# 2.6.3 FAME

FAME (Full-sky Astrometric Mapping Explorer) is another project that was expected to be launched on a geosynchronous orbit with a total expected lifetime of five years (Urban et al., 2000) but, like DIVA, it has been stopped. Based on Hipparcos principles with two fields of view separated by 84.◦3, it scans the sky with a $3 5 ^ { \circ }$ separation of the spin axis from the Sun, but with faster rotation and scanning periods. The aperture sizes are $4 0 \times 9$ cm and the effective focal length is $1 0 . 5 \mathrm { m }$ .

The receiving system consists of thirteen $2 0 4 8 \times 4 0 9 6$ pixel CCD arrays, two of which are covered with filters, providing data in three photometric SLOAN Digital Sky Survey bands (Section 11.4.3). Eleven CCDs are used for astrometry, with the brighter stars, of 4–8 magnitudes, being observed through neutral density filters on three CCDs, by means of a start–stop technique, or by centroiding on extended point-spread functions of saturated images. The read-out is in drift scanning mode, the drift speed being determined from the on-board attitude determination.

It was designed in such a way that 40 million stars would have been observed with, for a five-year mission, accuracies in astrometric parameters of 0.050 mas, and 0.5 mas, respectively for stars of magnitude 9 and 15. More information is at www.usno.navy.mil/fame/.

![](images/c315a4a1d217d546a083be354eb41776ec94fe11b471207e5eca45ea67e6f4a9.jpg)  
Fig. 2.10. Tentative GAIA payload configuration: A1 and A2 are the astrometric mirrors and Sp is the photometric collector.

# 2.6.4 GAIA

GAIA (Global Astrometry Instrument for Astrophysics) is being studied by the ESA and is approved for a launch in 2011–2012. As with the previous missions, it is based upon the Hipparcos main principles with two fields of view separated by $1 0 6 ^ { \circ }$ and a rotation duration of $^ { 6 \mathrm { h } }$ (Kovalevsky et al., 2000; ESA, 2000). It is intended to be placed on an orbit around the Lagrange point, $L _ { 2 }$ , of the Earth–Sun system, designed in such a way that it avoids eclipses of the Sun by the Earth.

After some reduction in size, the astrometric instrumentation now consists of two telescopes A1 and A2 with a rectangular entrance pupil whose dimensions are $1 4 0 \times 5 0 \mathrm { c m }$ with a $4 6 . 7 \mathrm { m }$ equivalent focal length (Fig. 2.10). The common focal plane covers a field of view of $0 . ^ { \circ } 6 6 \times 0 . ^ { \circ } 6 6$ filled with some $1 8 0 \mathrm { C C D s }$ operating in drift scanning mode. The first two columns of the mosaic are star-mappers which detect images above some given threshold and determine their positions and speeds in the focal plane. Then the image reaches the astrometric CCDs and the five broad-band photometers, but only small pixel windows around the predicted path are read and transmitted to the ground after some on-board treatment.

The expected accuracies of positions and parallaxes for a five-year mission range from $4 \mu \mathrm { a s }$ for stars up to magnitude 12, degrading to $1 1 \mu \mathrm { a s }$ at magnitude 15, $2 7 \mu \mathrm { a s }$ at magnitude 17, and $1 6 0 \mu \mathrm { a s }$ for magnitude 20. The accuracy of yearly proper motions should be about three quarters of these numbers.

A third telescope, placed midway between the two astrometric instruments, has a square $5 0 \mathrm { c m }$ entrance pupil with a $2 . 1 \mathrm { m }$ equivalent focal length. The field of view is split into a central part devoted to the radial velocity measurements, and two outer regions, for medium-band photometry recording in 10 different spectral bands. More information is at http://astro.estec.esa.nl/SA-general/Projects/GAIA/gaia.html.

# 3 Basic principles and coordinate systems

Astronomy and astrometry began with observations of directions, or spherical angles, without knowledge of distances. So the concept of a celestial sphere and the use of spherical trigonometry have long traditions. With the increased knowledge and improved accuracies of distances, or parallaxes, and radial velocities, the use of space coordinates and vectors and matrices have become appropriate. In this chapter, the development of vectors can be used as the basis for the equations of spherical trigonometry and matrix algebra. In addition, tensors and quaternions are now used in the Theory of Relativity and artificial satellite applications. Then, differential coordinates, coordinate frames and the various coordinate systems used in astronomy will be discussed. In the process the changes in concepts being introduced with the new International Celestial Reference System (ICRS) will be presented.

# 3.1 Vectors

While a scalar has magnitude and a sign, a vector has a length and a direction. A scalar $k$ multipling a vector AB changes its length.

$$
\begin{array} { l } { \mathbf { A B } + \mathbf { B A } = 0 } \\ { k \mathbf { A B } = \mathbf { A B } k . } \end{array}
$$

Vectors can be added (see Fig. 3.1) and the commutative and associative laws apply.

$$
\begin{array} { r l } & { \mathbf { A } \mathbf { B } + \mathbf { B } \mathbf { C } = \mathbf { A } \mathbf { C } } \\ & { \mathbf { a } + \mathbf { b } = \mathbf { b } + \mathbf { a } \quad ( \mathrm { c o m m u t a t i v e ~ l a w } ) } \\ & { ( \mathbf { a } + \mathbf { b } ) + \mathbf { c } = \mathbf { a } + ( \mathbf { b } + \mathbf { c } ) \quad ( \mathrm { a s s o c i a t i v e ~ l a w } ) . } \end{array}
$$

A vector can be specified in components. If i and j are not parallel unit vectors and $\mathbf { i } , \mathbf { j }$ , and $\mathbf { r }$ are coplanar, then unique scalars $x$ , $y$ exist so that

$$
\mathbf { r } = x \mathbf { i } + y \mathbf { j } .
$$

![](images/a0c12343b9e3390781229f4e6445548b4ca1bceb99fb469619138e2d5557749d.jpg)  
Fig. 3.1. Addition of vectors.

![](images/f0769ac7b80e8d5d62b38c1619148be9f86aee6e16371c4207b1a43592eb9f45.jpg)  
Fig. 3.2. Components of a vector.

If we add $\mathbf { k }$ , not in the plane, then r can be three dimensional and specified by:

$$
\mathbf { r } = x \mathbf { i } + y \mathbf { j } + z \mathbf { k } .
$$

$\mathbf { r }$ is then resolved along directions i, j, $\mathbf { k }$ by its components $x , y , z$ .

In general, i, j, k are mutually perpendicular unit vectors in a right-hand triad with positive directions as shown in Fig. 3.2. We shall generally use such a triad for reference in space. The components are written without ambiguity as ${ \bf r } = ( x , y , z )$ . Let $r$ be the length of $\mathbf { r }$ and, if $\alpha$ is the angle between OP and i, then

$$
\cos \alpha = x / r = l .
$$

With $m$ and $n$ similarly defined with respect to the $j$ and $k$ axes, $l , m , n$ are the direction cosines of $\mathbf { r }$ with respect to the triad i, j, k, and

$$
l ^ { 2 } + m ^ { 2 } + n ^ { 2 } = 1 .
$$

If we denote u as a unit vector along the direction of the vector $\mathbf { r }$ , then $\mathbf { r }$ is written as

$$
\mathbf { O P } = \mathbf { r } = x \mathbf { i } + y \mathbf { j } + z \mathbf { k } = ( x , y , z ) = ( r l , r m , r n ) = r ( l , m , n ) = r \mathbf { u } .
$$

If ${ \bf r } _ { 1 } = ( x _ { 1 } , y _ { 1 } , z _ { 1 } )$ and ${ \bf r } _ { 2 } = ( x _ { 2 } , y _ { 2 } , z _ { 2 } )$ , then

$$
{ \bf r } _ { 1 } + { \bf r } _ { 2 } = ( x _ { 1 } + x _ { 2 } , \ y _ { 1 } + y _ { 2 } , \ z _ { 1 } + z _ { 2 } ) .
$$

In addition to the above representation of a vector in Cartesian coordinates, two other types of coordinate system are in use (see Fig. 3.2).

(i) Cylindrical coordinates $( \rho , \ \phi , \ z )$ , where $\rho$ and $\phi$ are the polar coordinates of the projection of the vector $\mathbf { r }$ on the $x { - } y$ plane.   
(ii) Spherical coordinates $( r , \ \theta , \ \phi )$ where $r = | \mathbf { r } | , \phi$ has the same definition as in cylindrical coordinates, and $\theta$ is the angle between $O z$ and $\mathbf { r }$ , with its origin along $O z$ .

The components in these three coordinate systems are related by the following equations.

$$
{ \begin{array} { r l r l } & { x = r \sin \theta \cos \phi } & & { = \rho \cos \phi } \\ & { y = r \sin \theta \sin \phi } & & { = \rho \sin \phi } \\ & { z = r \cos \theta } & & { = z } \\ & { r = { \sqrt { ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ) } } } & & { = { \sqrt { ( \rho ^ { 2 } + z ^ { 2 } ) } } } \\ & { \theta = \operatorname { a r c c o s } ( z / { \sqrt { ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ) } } ) = \arcsin ( \rho / z ) } \\ & { \phi = \arctan ( y / x ) } & & { = \phi \quad { \mathrm { i f ~ } } x > 0 } \\ & { \phi = \arctan ( y / x ) + 1 8 0 ^ { \circ } } & & { = \phi \quad { \mathrm { i f ~ } } x < 0 } \\ & { \rho = { \sqrt { ( x ^ { 2 } + y ^ { 2 } ) } } } & & { = r \sin \theta } \end{array} }
$$

# 3.1.1 Dot product

Taking the vectors a and b and the angle $\theta$ between them, the scalar, or dot, product is

$$
\mathbf { a } \cdot \mathbf { b } = a b \cos \theta .
$$

By the commutative law, one has

$$
\mathbf { a } \cdot \mathbf { b } = a b \cos \theta = b a \cos \theta = \mathbf { b } \cdot \mathbf { a } .
$$

This can be interpreted as $a$ times the projected length of $\mathbf { b }$ on a $( b \cos \theta )$ .

Since a $\mathbf { \nabla } \cdot \left( \mathbf { b } + \mathbf { c } \right)$ is the projection of the sum of separate projections on a, it follows that

$$
\mathbf { a } \cdot ( \mathbf { b } + \mathbf { c } ) = \mathbf { a } \cdot \mathbf { b } + \mathbf { a } \cdot \mathbf { c } .
$$

Also

$$
m ( \mathbf { a } \cdot \mathbf { b } ) = ( m \mathbf { a } ) \cdot \mathbf { b } = \mathbf { a } \cdot ( m \mathbf { b } ) .
$$

If i, j, k are a unit triad, the components of $\mathbf { r }$ on the orthogonal triad are $\mathbf { r } \cdot \mathbf { i } , \mathbf { r } \cdot \mathbf { j }$ , $\mathbf { r } \cdot \mathbf { k }$ , and

$$
\mathbf { i } \cdot \mathbf { j } = \mathbf { i } \cdot \mathbf { k } = \mathbf { j } \cdot \mathbf { k } = 0 .
$$

The square of a vector $\mathbf { r }$ is

$$
\mathbf { r } \cdot \mathbf { r } = r r = r ^ { 2 } .
$$

If $\mathbf { r } = \mathbf { x } \cdot \mathbf { i } + \mathbf { y } \cdot \mathbf { j } + \mathbf { z } \cdot \mathbf { k }$ , then

$$
r ^ { 2 } = x ^ { 2 } + y ^ { 2 } + z ^ { 2 } .
$$

# 3.1.2 Vector product

Remark. We shall now need to orient the three-dimensional space and its triad. We shall assume the right hand convention. It is defined in such a way that screws advance in the direction $\mathbf { k }$ when rotated from i toward j (see Fig. 3.2).

Let us now define the vector, or cross, product

$$
\mathbf { a } \times \mathbf { b } = ( a b \sin \theta ) \mathbf { n } ,
$$

where $\mathbf { n }$ is the unit vector perpendicular to the a–b plane, and such that the triad $( \mathbf { a } , \mathbf { b } , \mathbf { n } )$ is right handed.

Note that $\times$ is the accepted symbol for the cross product and care must be taken not to confuse this with a variable $x$ . The vector product is distributive, but it is not commutative.

$$
\begin{array} { c } { \mathbf { a } \times ( \mathbf { b } + \mathbf { c } ) = \mathbf { a } \times \mathbf { b } + \mathbf { a } \times \mathbf { c } . } \\ { \mathbf { a } \times \mathbf { b } = - \mathbf { b } \times \mathbf { a } . } \end{array}
$$

In a right-hand triad i, j, k, one has

$$
{ \begin{array} { r } { { \mathbf { i } } \times { \mathbf { j } } = { \mathbf { k } } , \quad { \mathbf { j } } \times { \mathbf { i } } = - { \mathbf { k } } , } \\ { { \mathbf { j } } \times { \mathbf { k } } = { \mathbf { i } } , \quad { \mathbf { k } } \times { \mathbf { j } } = - { \mathbf { i } } , } \\ { { \mathbf { k } } \times { \mathbf { i } } = { \mathbf { j } } , \quad { \mathbf { i } } \times { \mathbf { k } } = - { \mathbf { j } } . } \end{array} }
$$

Note that $\mathbf { r } \times \mathbf { r } = 0$ .

If the components of $a$ and $b$ are respectively $( a _ { x } , ~ a _ { y } , ~ a _ { z } )$ and $( b _ { x } , \ b _ { y } , \ b _ { z } )$ , then

$$
\mathbf { a } \times \mathbf { b } = ( a _ { y } b _ { z } - a _ { z } b _ { y } , \ a _ { z } b _ { x } - a _ { x } b _ { z } , \ a _ { x } b _ { y } - a _ { y } b _ { x } ) ,
$$

or in determinant form:

$$
\mathbf { a } \times \mathbf { b } = { \left| \begin{array} { l l l } { \mathbf { i } } & { \mathbf { j } } & { \mathbf { k } } \\ { a _ { x } } & { a _ { y } } & { a _ { z } } \\ { b _ { x } } & { b _ { y } } & { b _ { z } } \end{array} \right| } .
$$

# 3.1.3 Triple scalar product

The triple scalar product is defined by $\mathbf { a } \cdot ( \mathbf { b } \times \mathbf { c } )$ . It can be noted [a, b, c]. If a, $\mathbf { b }$ , c are considered in their components, then

$$
\mathbf { a } \cdot ( \mathbf { b } \times \mathbf { c } ) = \left| { \begin{array} { c c c } { a _ { x } } & { a _ { y } } & { a _ { z } } \\ { b _ { x } } & { b _ { y } } & { b _ { z } } \\ { c _ { x } } & { c _ { y } } & { c _ { z } } \end{array} } \right| .
$$

Note that

$$
[ \mathbf { a } , \mathbf { b } , \mathbf { c } ] = [ \mathbf { b } , \mathbf { c } , \mathbf { a } ] = [ \mathbf { c } , \mathbf { a } , \mathbf { b } ] = - [ \mathbf { a } , \mathbf { c } , \mathbf { b } ] .
$$

One may also define the triple vector product as

$$
\mathbf { a } \times ( \mathbf { b } \times \mathbf { c } ) = ( \mathbf { a } \cdot \mathbf { c } ) \mathbf { b } - ( \mathbf { a } \cdot \mathbf { b } ) \mathbf { c } .
$$

# 3.2 Vector derivatives

A vector can vary as a function of a scalar, such as time, or as a function of another vector such as position. We assume the variation is continuous, so it can be differentiated.

If a particle moves along the path $A B$ , $P$ is a position at time $t$ , and $P ^ { \prime }$ is a position at time $t + 8 t$ . If $\delta t$ is a small time interval, then $P P ^ { \prime }$ is $\delta r$ (Fig. 3.3). Letting $\delta t$ tend to zero, one can define the derivative of a vector, ${ \bf V } ( t ) \left( x ( t ) , \ y ( t ) , \ z ( t ) \right)$ ,

![](images/ac1bd8d2c2318bdb9fa680ce24267c38e13e894a818ec9aafbc33f4dcd248999.jpg)  
Fig. 3.3. Derivative of a vector.

as:

$$
{ \frac { \mathrm { d } \mathbf { V } } { \mathrm { d } t } } = \left( { \frac { \mathrm { d } x } { \mathrm { d } t } } , { \frac { \mathrm { d } y } { \mathrm { d } t } } , { \frac { \mathrm { d } z } { \mathrm { d } t } } \right) .
$$

If $\mathbf { u }$ is a unit vector along $P P ^ { \prime }$ and $s$ is the distance along the curve,

$$
\delta \mathbf { r } = \mathbf { u } \delta s ,
$$

so that,

$$
\operatorname* { l i m } _ { { \hat { \mathbf { \theta } } }  0 } { \frac { \mathbf { P } \mathbf { P } ^ { \prime } } { { \hat { \mathbf { \theta } } } t } } = \operatorname* { l i m } _ { { \hat { \mathbf { \theta } } }  0 } { \frac { \hat { \mathbf { \theta } } \mathbf { r } } { { \hat { \mathbf { \theta } } } t } } = { \frac { \mathrm { d } \mathbf { r } } { \mathrm { d } t } } = \mathbf { u } { \frac { \mathrm { d } s } { \mathrm { d } t } } .
$$

This is the velocity of a particle at $P$ , commonly written as $\dot { \mathbf { r } }$ or v. It has magnitude and direction. The components of $\dot { \mathbf { r } }$ are $( { \dot { x } } , \ { \dot { y } } , \ { \dot { z } } )$ and those of $\mathbf { u }$ are $( \mathrm { d } x / \mathrm { d } s , \ \mathrm { d } y / \mathrm { d } s , \ \mathrm { d } z / \mathrm { d } s )$ .

In modern conventions, velocity is a vector $\mathbf { V }$ ; speed, $v$ , is a scalar value of velocity, $\mathrm { d } s / \mathrm { d } t$ .

# 3.2.1 Rotating axes

Rotating axes is a common phenomenon that must be commonly dealt with. Let p be the unit vector along r. Writing $\mathbf { r } = r \mathbf { p }$ and differentiating

$$
\dot { \mathbf { r } } = \dot { r } \mathbf { p } + r \frac { \mathrm { d } \mathbf { p } } { \mathrm { d } t } ,
$$

where the first term is the change along $\mathbf { r }$ , or the change in length, and the second term is the change perpendicular to $\mathbf { r }$ , or a rotation. Suppose a vector r has a rate of change of $\mathrm { d } \mathbf { r } / \mathrm { d } t$ with respect to a fixed frame $F _ { 1 }$ , and a change $\partial \mathbf { r } / \partial t$ with respect to a frame $F _ { 2 }$ , which is rotating with respect to $F _ { 1 }$ with an angular velocity $\vec { \omega }$ (which is not necessarily constant). In the case where $F _ { 2 }$ is rotating with $\mathbf { r }$ , then $\partial \mathbf { r } / \partial t$ can be written instead of $\dot { r } \mathbf { r }$ . Then (3.7) can be written in the form

$$
{ \frac { \mathrm { d } \mathbf { r } } { \mathrm { d } t } } = { \frac { \partial \mathbf { r } } { \partial t } } + { \vec { \omega } } \times \mathbf { r } .
$$

This is a general result, which will be illustrated. Let i, j, $\mathbf { k }$ be an orthogonal triad, rigidly attached to $F _ { 2 }$ . Then,

$$
\mathbf { r } = ( \mathbf { r } \cdot \mathbf { i } ) \mathbf { i } + ( \mathbf { r } \cdot \mathbf { j } ) \mathbf { j } + ( \mathbf { r } \cdot \mathbf { k } ) \mathbf { k } = \sum _ { \mathbf { i } , \mathbf { j } , \mathbf { k } } ( \mathbf { r } \cdot \mathbf { i } ) \mathbf { i } ,
$$

with a summation over i, j, k. Then (3.7) can be written as

$$
{ \frac { \mathrm { d } \mathbf { r } } { \mathrm { d } t } } = \sum _ { \mathbf { i } , \mathbf { j } , \mathbf { k } } \left( { \frac { \mathrm { d } ( \mathbf { r } \cdot \mathbf { i } ) } { \mathrm { d } t } } \mathbf { i } \right) + \sum _ { \mathbf { i } , \mathbf { j } , \mathbf { k } } \left( { \big ( } \mathbf { r } \cdot \mathbf { i } { \big ) } { \frac { \mathrm { d } \mathbf { i } } { \mathrm { d } t } } \right) .
$$

Since di $/ \mathrm { d } t = \vec { \omega } \times \mathbf { i }$ , then

$$
\sum _ { \mathbf { i } , \mathbf { j } , \mathbf { k } } \left( ( \mathbf { r } \cdot \mathbf { i } ) { \frac { \mathrm { d } \mathbf { i } } { \mathrm { d } t } } \right) = { \vec { \omega } } \times \sum _ { \mathbf { i } , \mathbf { j } , \mathbf { k } } ( \mathbf { r } \cdot \mathbf { i } ) \mathbf { i } = { \vec { \omega } } \times \mathbf { r } .
$$

If we treat i, j, $\mathbf { k }$ as constant non-rotating vectors, then

$$
{ \frac { \mathrm { d } \mathbf { r } } { \mathrm { d } t } } = \sum _ { \mathbf { i } , \mathbf { j } , \mathbf { k } } \left( { \frac { \mathrm { d } ( \mathbf { r } \cdot \mathbf { i } ) } { \mathrm { d } t } } \mathbf { i } \right) .
$$

Hence, the derivative of the vector $\mathbf { r }$ , with a rotation can be given in the general form

$$
{ \frac { \mathrm { d } \mathbf { r } } { \mathrm { d } t } } = { \frac { \partial \mathbf { r } } { \partial t } } + { \vec { \omega } } \times \mathbf { r } .
$$

# 3.3 Gradient

Consider, defined and continuous in space, a scalar function of a position which is written $f ( x , y , z )$ or $f ( \mathbf { r } )$ . The move from $f ( x , y , z )$ to $f ( x + \delta x , y , z )$ produces a change in $f$ which can be written $( \partial f / \partial x ) \delta x$ , where $( \partial f / \partial x )$ is the conventional partial differentiation with respect to $x$ , while $y$ and $z$ are assumed constant. This could be written

$$
{ \begin{array} { l } { { \frac { \partial f } { \partial x } } \delta x = \left( { \frac { \partial f } { \partial x } } { \dot { \mathbf { i } } } + { \frac { \partial f } { \partial y } } { \dot { \mathbf { j } } } + { \frac { \partial f } { \partial z } } \mathbf { k } \right) \cdot \mathbf { i } \delta x } \\ { { \frac { \partial f } { \partial x } } \delta x = \nabla f \cdot \mathbf { i } \delta x . } \end{array} }
$$

The differential operator $\begin{array} { r } { \nabla = \frac { \partial } { \partial x } { \bf i } + \frac { \partial } { \partial y } { \bf j } + \frac { \partial } { \partial z } { \bf k } } \end{array}$ is called del or nabla.

Likewise the changes from $y$ to $y + \delta y$ and $z$ to $z + 8 z$ take the same form. In general, the change from $r$ to $r + \delta r$ is $\nabla f \cdot \mathbf { r }$ . The vector with the elements $( \partial f / \partial x , \ \partial f / \partial y , \ \partial f / \partial z )$ is called the “gradient” of $f$ , and is represented by grad $f$ or $\nabla f$ .

Consider a curve $C$ and the values that $f$ assumes along the curve. The rate of change of $f$ along $C$ with respect to the arc length is

$$
{ \frac { \partial f } { \partial s } } = { \frac { \partial f } { \partial x } } { \frac { \partial x } { \partial s } } + { \frac { \partial f } { \partial y } } { \frac { \partial y } { \partial s } } + { \frac { \partial f } { \partial z } } { \frac { \partial z } { \partial s } } = \mathbf { u } \nabla f .
$$

Consider a surface with $f ( x , y , z ) =$ constant. Along a line on the surface one has $\mathrm { d } f / \mathrm { d } s = 0$ , so $ { \mathbf { u } } \cdot \nabla f = 0$ .

Thus, $\nabla f$ is perpendicular to the surface. In general, $\nabla f$ is a field vector that is a function of position.

# 3.4 Matrices

A matrix is an array of $m \times n$ numbers, $a _ { q } ^ { p }$ , set out in $m$ rows and $n$ columns. The superscript $p$ indicates the row and the subscript $q$ indicates the column. It is a matrix of order $m \times n$ . In this book, we shall essentially use $3 \times 3$ matrices, exceptionally $2 \times 2$ . A shortened notation of an $m \times n$ matrix is

$$
\mathcal { A } ( a _ { q } ^ { p } ) = \left\| a _ { q } ^ { p } \right\| .
$$

Matrices are mathematical objects that obey a certain number of transformation and combination laws. For instance, a linear function of matrices of the same structure is a matrix whose components are the same combination of the components of the given matrices; for instance:

$$
A \mathcal { M } \big ( a _ { q } ^ { p } \big ) + B \mathcal { M } ^ { \prime } \big ( b _ { q } ^ { p } \big ) = S \big ( A a _ { q } ^ { p } + B b _ { q } ^ { p } \big ) .
$$

An important transformation is the transposition, which inverts the roles of rows and columns and transforms an $m \times n$ matrix into an $n \times m$ matrix:

$$
\mathcal { M } ^ { \top } ( a _ { q } ^ { p } ) = \mathcal { M } \big ( a _ { p } ^ { q } \big ) .
$$

The product of two matrices can be defined only if the number $n$ of columns of the first matrix, $\mathcal { A }$ , is equal to the number $m ^ { \prime }$ of rows of the second matrix $\boldsymbol { B }$ $\zeta n = m ^ { \prime } = N$ ). The result is a matrix, $\mathcal { C }$ , with $m$ rows and $n ^ { \prime }$ columns, whose general element of row $i$ and column $j$ is obtained by multiplying the rows of the first matrix into the columns of the second matrix, element by element, and summing the products algebraically

$$
c _ { j } ^ { i } = \sum _ { k = 1 , N } a _ { k } ^ { i } b _ { j } ^ { k } .
$$

As an example, the product of two $3 \times 3$ matrices

$$
\mathcal { A } \big ( a _ { q } ^ { p } \big ) = \left( \begin{array} { l l l } { a _ { 1 } ^ { 1 } } & { a _ { 2 } ^ { 1 } } & { a _ { 3 } ^ { 1 } } \\ { a _ { 1 } ^ { 2 } } & { a _ { 2 } ^ { 2 } } & { a _ { 3 } ^ { 2 } } \\ { a _ { 1 } ^ { 3 } } & { a _ { 2 } ^ { 3 } } & { a _ { 3 } ^ { 3 } } \end{array} \right)
$$

and

$$
B \big ( b _ { q } ^ { p } \big ) = \left( \begin{array} { l l l } { b _ { 1 } ^ { 1 } } & { b _ { 2 } ^ { 1 } } & { b _ { 3 } ^ { 1 } } \\ { b _ { 1 } ^ { 2 } } & { b _ { 2 } ^ { 2 } } & { b _ { 3 } ^ { 2 } } \\ { b _ { 1 } ^ { 3 } } & { b _ { 2 } ^ { 3 } } & { b _ { 3 } ^ { 3 } } \end{array} \right)
$$

is

$$
\mathscr { C } ( c _ { j } ^ { i } ) = \left( \begin{array} { l l } { a _ { 1 } ^ { 1 } b _ { 1 } ^ { 1 } + a _ { 2 } ^ { 1 } b _ { 1 } ^ { 2 } + a _ { 3 } ^ { 1 } b _ { 1 } ^ { 3 } } & { a _ { 1 } ^ { 1 } b _ { 2 } ^ { 1 } + a _ { 2 } ^ { 1 } b _ { 2 } ^ { 2 } + a _ { 3 } ^ { 1 } b _ { 2 } ^ { 3 } } & { a _ { 1 } ^ { 1 } b _ { 3 } ^ { 1 } + a _ { 2 } ^ { 1 } b _ { 3 } ^ { 2 } + a _ { 3 } ^ { 1 } b _ { 3 } ^ { 3 } } \\ { a _ { 1 } ^ { 2 } b _ { 1 } ^ { 1 } + a _ { 2 } ^ { 2 } b _ { 1 } ^ { 2 } + a _ { 3 } ^ { 2 } b _ { 1 } ^ { 3 } } & { a _ { 1 } ^ { 2 } b _ { 2 } ^ { 1 } + a _ { 2 } ^ { 2 } b _ { 2 } ^ { 2 } + a _ { 3 } ^ { 2 } b _ { 2 } ^ { 3 } } & { a _ { 1 } ^ { 2 } b _ { 3 } ^ { 1 } + a _ { 2 } ^ { 2 } b _ { 3 } ^ { 2 } + a _ { 3 } ^ { 2 } b _ { 3 } ^ { 3 } } \\ { a _ { 1 } ^ { 3 } b _ { 1 } ^ { 1 } + a _ { 2 } ^ { 3 } b _ { 1 } ^ { 2 } + a _ { 3 } ^ { 3 } b _ { 1 } ^ { 3 } } & { a _ { 1 } ^ { 3 } b _ { 2 } ^ { 1 } + a _ { 2 } ^ { 3 } b _ { 2 } ^ { 2 } + a _ { 3 } ^ { 3 } b _ { 2 } ^ { 3 } } & { a _ { 1 } ^ { 3 } b _ { 3 } ^ { 1 } + a _ { 2 } ^ { 3 } b _ { 3 } ^ { 2 } + a _ { 3 } ^ { 3 } b _ { 3 } ^ { 3 } } \end{array} \right) .
$$

A vector in space may be considered as a $1 \times 3$ matrix:

$$
\mathbf { V } = ( { \boldsymbol { x } } \quad y \quad z ) .
$$

The product of a vector, $\mathbf { V }$ , represented as a row matrix, $\nu$ , by a square $3 \times 3$ matrix, $\mathcal { A }$ , is the vector, $\mathbf { V } ^ { \prime }$ , represented by $\mathcal { V } ^ { \prime }$ :

$$
\mathcal { V } ^ { \prime } = ( x y z ) \times \left( \begin{array} { c c c } { { a _ { 1 } ^ { 1 } } } & { { a _ { 2 } ^ { 1 } } } & { { a _ { 3 } ^ { 1 } } } \\ { { a _ { 1 } ^ { 2 } } } & { { a _ { 2 } ^ { 2 } } } & { { a _ { 3 } ^ { 2 } } } \\ { { a _ { 1 } ^ { 3 } } } & { { a _ { 2 } ^ { 3 } } } & { { a _ { 3 } ^ { 3 } } } \end{array} \right) = ( x ^ { \prime } \mathrm { ~  ~ \mathscr ~ { y } ^ { \prime } ~  ~ \mathscr ~ { z } ^ { \prime } ~ } ) ,
$$

with

$$
\begin{array} { r } { x ^ { \prime } = a _ { 1 } ^ { 1 } x + a _ { 1 } ^ { 2 } y + a _ { 1 } ^ { 3 } z , } \\ { y ^ { \prime } = a _ { 2 } ^ { 1 } x + a _ { 2 } ^ { 2 } y + a _ { 2 } ^ { 3 } z , } \\ { z ^ { \prime } = a _ { 3 } ^ { 1 } x + a _ { 3 } ^ { 2 } y + a _ { 3 } ^ { 3 } z . } \end{array}
$$

One may also represent a vector, $\mathbf { V }$ , by a column matrix, the transpose of the row matrix. Conversely, the row matrix is the transpose of the column matrix:

$$
\mathcal { V } = \left( x \quad y \quad z \right) = \left( \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right) ^ { \top } .
$$

The equivalent of Equation (3.17) with the column matrix is

$$
\mathcal { V } ^ { \prime } = \mathcal { A } ^ { \top } \times \mathcal { V } ^ { \top } = { \binom { a _ { 1 } ^ { 1 } } { a _ { 2 } ^ { 1 } } } \quad a _ { 2 } ^ { 2 } \quad a _ { 2 } ^ { 3 } ) \times { \binom { x } { y } } = { \binom { x ^ { \prime } } { y ^ { \prime } } } .
$$

Note that the multiplication rule imposes that in the horizontal representation of a vector, the latter must be placed before the matrix. In the case of vertical representation, it has to be placed after the matrix.

An important case of a $3 \times 3$ matrix is the unit matrix, $\mathcal { T }$ ,

$$
\mathcal { T } = \left( \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) .
$$

It is such that

$$
\mathcal { M } \times \mathcal { T } = \mathcal { T } \times \mathcal { M } = \mathcal { M } .
$$

# 3.4.1 Rotation matrices

Let us now describe a special class of $3 \times 3$ matrices, the rotation matrices. A first property of a square matrix is that one can associate a numerical value to a matrix, the value of the determinant having the same elements:

$$
D = \operatorname* { d e t } ( \boldsymbol { \mathscr { A } } ) = \left| a _ { 1 } ^ { 1 } \quad a _ { 2 } ^ { 1 } \quad a _ { 3 } ^ { 1 } \right| .
$$

Rotation matrices are characterized by $D = 1$ . They are called orthogonal. The product of such a matrix by a vector transforms the vector to another one having the same length. This transformation is therefore a rotation. If the matrix is the unit matrix, the transformation is an identity. We shall generally use, in this book, column representations of vectors.

There are three fundamental rotation matrices in the Ox yz orthogonal righthanded triad:

(i) rotation of a vector $\mathbf { V }$ about the $O x$ axis positively through $\theta$ , operated by the matrix $\mathcal { R } _ { 1 }$

$$
( x ^ { \prime } \quad y ^ { \prime } \quad z ^ { \prime } ) = ( x \quad y \quad z ) \times \left( { \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { \cos \theta } & { - \sin \theta } \\ { 0 } & { \sin \theta } & { \cos \theta } \end{array} } \right)
$$

or

$$
\begin{array} { r } { \left( \begin{array} { c } { x ^ { \prime } } \\ { y ^ { \prime } } \\ { z ^ { \prime } } \end{array} \right) = \left( \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { \cos \theta } & { \sin \theta } \\ { 0 } & { - \sin \theta } & { \cos \theta } \end{array} \right) \times \left( \begin{array} { c } { x } \\ { y } \\ { z } \end{array} \right) = \mathcal { R } _ { 1 } \times \left( \begin{array} { c } { x } \\ { y } \\ { z } \end{array} \right) ; } \end{array}
$$

(ii) rotation of a vector $\mathbf { V }$ about the $O y$ axis positively through $\omega$ , operated by the matrix $\mathcal { R } _ { 2 }$

$$
\begin{array} { c c c } { { ( x ^ { \prime } } } & { { y ^ { \prime } } } & { { z ^ { \prime } ) = ( x } } & { { y } } & { { z ) \times \left( \begin{array} { c c c } { { \cos \omega } } & { { 0 } } & { { \sin \omega } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { - \sin \omega } } & { { 0 } } & { { \cos \omega } } \end{array} \right) } } \end{array}
$$

or

$$
\left( \begin{array} { c } { x ^ { \prime } } \\ { y ^ { \prime } } \\ { z ^ { \prime } } \end{array} \right) = \left( \begin{array} { c c c } { \cos \omega } & { 0 } & { - \sin \omega } \\ { 0 } & { 1 } & { 0 } \\ { \sin \omega } & { 0 } & { \cos \omega } \end{array} \right) \times \left( \begin{array} { c } { x } \\ { y } \\ { z } \end{array} \right) = \mathcal { R } _ { 2 } \times \left( \begin{array} { c } { x } \\ { y } \\ { z } \end{array} \right) ;
$$

(iii) rotation of a vector $\mathbf { V }$ about the $O z$ axis positively through $\phi$ , operated by the matrix $\mathcal { R } _ { 3 }$

$$
( x ^ { \prime } \quad y ^ { \prime } \quad z ^ { \prime } ) = ( x \quad y \quad z ) \times \left( { \begin{array} { c c c } { \cos \phi } & { - \sin \phi } & { 0 } \\ { \sin \phi } & { \cos \phi } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} } \right)
$$

or

$$
\binom { x ^ { \prime } } { y ^ { \prime } } = \left( \begin{array} { c c c } { \cos \phi } & { \sin \phi } & { 0 } \\ { - \sin \phi } & { \cos \phi } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) \times \left( \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right) = \mathcal { R } _ { 3 } \times \left( \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right) .
$$

An example is the Eulerian coordinate transformation defined in Section 3.8.

# 3.4.2 Cartesian coordinate transformation

If $\mathbf { r }$ and $\mathbf { r } ^ { \prime }$ are the Cartesian coordinates of a vector in two different coordinate systems, they can be related by

$$
\mathbf { r } ^ { \prime } = { \mathcal { A } } \mathbf { r } + \mathbf { a } ,
$$

where a is the translation of the origin of the unprimed system in the primed system, and matrix $\mathcal { A }$ represents a rotation. The matrix $\mathcal { A }$ , or direction cosine matrix, can be obtained from the product of matrices of successive rotations about the three coordinate axes. The elements of $\mathcal { A }$ are direction cosines of the primed axes in the unprimed axes, and satisfy the orthogonality condition. Since $\mathcal { A }$ is an orthogonal matrix, the inverse transformation is the transposed matrix. Thus,

$$
\begin{array} { r } { A ^ { - 1 } = A ^ { \top } . } \end{array}
$$

The direction cosine matrix, in terms of the orthogonal unit vectors $( \mathbf { i } , \ \mathbf { j } , \ \mathbf { k } )$ and $( \mathbf { i } ^ { \prime } , \ \mathbf { j } ^ { \prime } , \ \mathbf { k } ^ { \prime } )$ in the two coordinate systems, can be given by

$$
\begin{array} { r } { \mathcal { A } \equiv \left( \begin{array} { l l l } { \mathbf { i } ^ { \prime } \cdot \mathbf { i } } & { \mathbf { i } ^ { \prime } \cdot \mathbf { j } } & { \mathbf { i } ^ { \prime } \cdot \mathbf { k } } \\ { \mathbf { j } ^ { \prime } \cdot \mathbf { i } } & { \mathbf { j } ^ { \prime } \cdot \mathbf { j } } & { \mathbf { j } ^ { \prime } \cdot \mathbf { k } } \\ { \mathbf { k } ^ { \prime } \cdot \mathbf { i } } & { \mathbf { k } ^ { \prime } \cdot \mathbf { j } } & { \mathbf { k } ^ { \prime } \cdot \mathbf { k } } \end{array} \right) . } \end{array}
$$

Euler’s theorem states that any finite rotation of a rigid body can be expressed as a rotation through some angle about some fixed axis. Therefore, the most general transformation matrix is a rotation by some angle, $\varPhi$ , about some fixed axis, e. This axis is unaffected by the rotation and must have the same components in both primed and unprimed systems. Denoting the components by $e _ { 1 } , e _ { 2 }$ and $e _ { 3 }$ , the matrix

$\mathcal { A }$ is

$$
\mathcal { A } = \left( \begin{array} { l l l } { a _ { 1 } ^ { 1 } } & { a _ { 1 } ^ { 2 } } & { a _ { 1 } ^ { 3 } } \\ { a _ { 2 } ^ { 1 } } & { a _ { 2 } ^ { 2 } } & { a _ { 2 } ^ { 3 } } \\ { a _ { 3 } ^ { 1 } } & { a _ { 3 } ^ { 2 } } & { a _ { 3 } ^ { 3 } } \end{array} \right) ,
$$

with

$$
\begin{array} { r l } & { a _ { 1 } ^ { 1 } = \cos \phi + e _ { 1 } ^ { 2 } ( 1 - \cos \phi ) } \\ & { a _ { 1 } ^ { 2 } = e _ { 1 } e _ { 2 } ( 1 - \cos \phi ) + e _ { 3 } \sin \phi } \\ & { a _ { 3 } ^ { 1 } = e _ { 1 } e _ { 3 } ( 1 - \cos \phi ) - e _ { 2 } \sin \phi } \\ & { a _ { 2 } ^ { 1 } = e _ { 1 } e _ { 2 } ( 1 - \cos \phi ) - e _ { 3 } \sin \phi } \\ & { a _ { 2 } ^ { 2 } = \cos \phi + e _ { 2 } ^ { 2 } ( 1 - \cos \phi ) } \\ & { a _ { 3 } ^ { 2 } = e _ { 2 } e _ { 3 } ( 1 - \cos \phi ) + e _ { 1 } \sin \phi } \\ & { a _ { 3 } ^ { 1 } = e _ { 1 } e _ { 3 } ( 1 - \cos \phi ) + e _ { 2 } \sin \phi } \\ & { a _ { 3 } ^ { 2 } = e _ { 2 } e _ { 3 } ( 1 - \cos \phi ) - e _ { 1 } \sin \phi } \\ & { a _ { 3 } ^ { 3 } = \cos \phi + e _ { 3 } ^ { 2 } ( 1 - \cos \phi ) . } \end{array}
$$

The inverse transformation matrix may be obtained by Equation (3.15) or replacing $\phi$ by $- \phi$ in (3.20), that is a rotation of the same amount in the opposite direction.

# 3.5 Tensors

Tensors, like matrices, are tables of numbers or functions. They are mathematical tools that are particularly linked with changes in coordinate systems. Their existence is independent of coordinate systems, although their expression depends on them.

In a $n$ -dimensional space, a tensor has $n ^ { q }$ components, where $q$ is the order, or rank, of the tensor. So, in classical three-dimensional space:

- a rank-zero tensor is a scalar, - a rank-one tensor is a vector, - a rank-two tensor is a matrix, - a rank-three tensor has 27 components.

Although tensor analysis is a generalization of vector analysis, one cannot, in general, visualize tensors. In physics, they are important insofar as they are used to express physical laws that remain valid after coordinate system transformations. The rules on tensor calculus depend on rank and dimensions of space. We shall consider only those cases that are useful in the present book.

# 3.5.1 Rank-two tensors in three-dimensional space

An example in mechanics is the moment of inertia tensor. It is an order-two tensor in three-dimensional space $( x , y , z )$ . The $3 \times 3$ table expressing the tensor is

$$
[ I ] = \left[ \begin{array} { c c c } { { I _ { 1 } ^ { 1 } } } & { { I _ { 2 } ^ { 1 } } } & { { I _ { 3 } ^ { 1 } } } \\ { { I _ { 1 } ^ { 2 } } } & { { I _ { 2 } ^ { 2 } } } & { { I _ { 3 } ^ { 2 } } } \\ { { I _ { 1 } ^ { 3 } } } & { { I _ { 2 } ^ { 3 } } } & { { I _ { 3 } ^ { 3 } } } \end{array} \right] ,
$$

where the diagonal terms $I _ { i } ^ { i }$ are the inertia moments,

$$
I _ { 1 } ^ { 1 } = I _ { x x } = \sum _ { i = 1 } ^ { 3 } m _ { i } \bigl ( y _ { i } ^ { 2 } + z _ { i } ^ { 2 } \bigr ) ,
$$

and the other terms are the products of inertia.

$$
I _ { 1 } ^ { 2 } = I _ { 2 } ^ { 1 } = I _ { x y } = \sum _ { i = 1 } ^ { 3 } m _ { i } x _ { i } y _ { i } ,
$$

so that the expression of the moment of inertia tensor is

$$
[ I ] = \left[ \begin{array} { l l l } { I _ { x x } } & { I _ { x y } } & { I _ { x z } } \\ { I _ { x y } } & { I _ { y y } } & { I _ { y z } } \\ { I _ { x z } } & { I _ { y z } } & { I _ { z z } } \end{array} \right] .
$$

It is a symmetrical tensor. Let us now apply the following most general transformation of the system of coordinates,

$$
\begin{array} { r } { x ^ { \prime } = a _ { 1 } ^ { 1 } x + a _ { 1 } ^ { 2 } y + a _ { 1 } ^ { 3 } z , } \\ { y ^ { \prime } = a _ { 2 } ^ { 1 } x + a _ { 2 } ^ { 2 } y + a _ { 2 } ^ { 3 } z , } \\ { z ^ { \prime } = a _ { 3 } ^ { 1 } x + a _ { 3 } ^ { 2 } y + a _ { 3 } ^ { 3 } z . } \end{array}
$$

Let it satisfy the condition that it is a transformation which, when followed by its inverse, is unity. In this particular case, it is a rotation,

$$
\sum _ { i } a _ { i } ^ { j } a _ { i } ^ { k } = 0 \quad \mathrm { f o r } \quad j \neq k , \ : \ : \ : \mathrm { a n d } \ : \ : \ : \sum _ { i } a _ { i j } ^ { 2 } = 1 .
$$

One then finds that the current element of the transformed tensor $[ I ^ { \prime } ]$ is

$$
I _ { i j } ^ { \prime } = \sum _ { l , m } a _ { i l } a _ { j m } I _ { m } ^ { l } .
$$

Let us now consider a linear transformation, whose coefficients are the components of the tensor $I$ . A vector, $\mathbf { u }$ , of components, $( x , y , z )$ , is transformed into a vector,

$ { \mathbf { u } } ^ { \prime }$ , of components, $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ , by

$$
\begin{array} { r } { x ^ { \prime } = I _ { 1 } ^ { 1 } x + I _ { 1 } ^ { 2 } y + I _ { 1 } ^ { 3 } z , } \\ { y ^ { \prime } = I _ { 2 } ^ { 1 } x + I _ { 2 } ^ { 2 } y + I _ { 2 } ^ { 3 } z , } \\ { z ^ { \prime } = I _ { 3 } ^ { 1 } x + I _ { 3 } ^ { 2 } y + I _ { 3 } ^ { 3 } z . } \end{array}
$$

These equations are formally identical to Equations (3.17). One can write these equations symbolically as

$$
\mathbf { u } ^ { \prime } = [ I ] \times \mathbf { u } .
$$

This can be shown as follows. The components of $\mathbf { u }$ are transformed by Equations (3.22), and the components of the tensor by Equations (3.23). Computing the transform of $\mathbf { u }$ , using in (3.22), as coefficients, the components of $[ I ]$ , one reproduces exactly Equations (3.22). Actually, it is a consequence of the condition imposed on the components that the transformation, followed by its inverse, is an identity.

An application of this is the determination of the principal axes of inertia. One defines a proper vector of a tensor, any vector, $\mathbf { u }$ , that is colinear with the product $[ I ] \times \mathbf { u }$ . It is therefore given by the equations

$$
\begin{array} { r } { x ^ { \prime } = I _ { 1 } ^ { 1 } x + I _ { 1 } ^ { 2 } y + I _ { 1 } ^ { 3 } z = \lambda x , } \\ { y ^ { \prime } = I _ { 2 } ^ { 1 } x + I _ { 2 } ^ { 2 } y + I _ { 2 } ^ { 3 } z = \lambda y , } \\ { z ^ { \prime } = I _ { 3 } ^ { 1 } x + I _ { 3 } ^ { 2 } y + I _ { 3 } ^ { 3 } z = \lambda z . } \end{array}
$$

To get the solution, one must determine the values of $\lambda$ , for which the characteristic equation of the tensor is equal to zero,

$$
\begin{array} { r l } { \left| \begin{array} { c c c } { I _ { x x } - \lambda } & { } & { I _ { x y } } \\ { I _ { x y } } & { I _ { y y } - \lambda } & { I _ { y z } } \\ { I _ { x z } } & { I _ { y z } } & { I _ { z z } - \lambda } \end{array} \right| = 0 . } \end{array}
$$

This equation has three solutions $\lambda _ { i }$ . The moment of inertia with respect to a principal axis $i$ is

$$
I _ { \lambda _ { i } } = \mathbf { u } \times [ I ] \times \mathbf { u } = \mathbf { u } \times \lambda _ { i } \mathbf { u } = \lambda _ { i } .
$$

# 3.5.2 Tensors in a four-dimensional space

In the framework of the Theory of Relativity (Chapter 5), the reference is a fourdimensional space-time, and tensors of rank two that are introduced are square symmetric tables of $4 \times 4$ components. The most general form is:

$$
\left[ { \begin{array} { l l l l } { g _ { 0 0 } } & { g _ { 0 1 } } & { g _ { 0 2 } } & { g _ { 0 3 } } \\ { g _ { 1 0 } } & { g _ { 1 1 } } & { g _ { 1 2 } } & { g _ { 1 3 } } \\ { g _ { 2 0 } } & { g _ { 2 1 } } & { g _ { 2 2 } } & { g _ { 2 3 } } \\ { g _ { 3 0 } } & { g _ { 3 1 } } & { g _ { 3 2 } } & { g _ { 3 3 } } \end{array} } \right] .
$$

It represents the relationship between the square of the distance of two generalized events separated by $\mathrm { d } s = ( \mathrm { d } x _ { 0 } , \mathrm { d } x _ { 1 } , \mathrm { d } x _ { 2 } , \mathrm { d } x _ { 3 }$ ) (Section 5.3.3),

$$
\mathrm { d } s ^ { 2 } = \sum _ { i = 0 } ^ { 3 } \sum _ { j = 0 } ^ { 3 } g _ { i j } \mathrm { d } x _ { i } \mathrm { d } x _ { j } ,
$$

with $g _ { i j } = g _ { j i }$

Another application of four-dimensional rank-two tensors is the energy– momentum tensor. Let us consider a collection of non-interacting particles, $n$ per volume unit, each having an energy $m$ . The energy density is, evidently,

$$
T _ { 0 0 } = n m .
$$

But this is not all the energy of the system. One must consider also the energy flux, which has three components. For instance, the $x$ component is the amount of energy transported through a unit $y z$ area, if the velocity is $v _ { x }$ . So, the energy flux density has three components,

$$
T _ { 0 i } = n m v _ { i } \qquad \mathrm { w i t h } i = 1 \mathrm { t o } 3 .
$$

It can also be regarded as the density of momentum.

Finally, one must also consider the momentum flux. The $x { - } y$ momentum flux is the amount of $x$ momentum that flows in the $y$ direction. It is expressed by $m n v _ { x } v _ { y }$ . Again, there are three components,

$$
T _ { j i } = n m v _ { i } v _ { j } = T _ { i j } \qquad { \mathrm { w i t h ~ } } i , j = 1 \mathrm { ~ t o ~ } 3 , i \neq j .
$$

These three types of energy can be expressed in a single entity, the energy– momentum tensor,

$$
\left( { \begin{array} { c c c c } { T _ { 0 0 } } & { T _ { 0 1 } } & { T _ { 0 2 } } & { T _ { 0 3 } } \\ { T _ { 1 0 } } & { 0 } & { T _ { 1 2 } } & { T _ { 1 3 } } \\ { T _ { 2 0 } } & { T _ { 2 1 } } & { 0 } & { T _ { 2 3 } } \\ { T _ { 3 0 } } & { T _ { 3 1 } } & { T _ { 3 2 } } & { 0 } \end{array} } \right) .
$$

The application to electro-magnetism is more complex (see, for instance, Mould, 1994). We shall only give the result. Let ${ \bf E } \left( E _ { x } , E _ { y } , E _ { z } \right)$ and ${ \bf B } \left( B _ { x } , B _ { y } , B _ { z } \right)$ be, respectively, the electrical and the magnetic fields and $c$ is the speed of light, the field tensor is, in complex notation:

$$
\left( \begin{array} { c c c c } { 0 } & { B _ { z } } & { - B _ { y } } & { - \mathrm { i } E _ { x } / c } \\ { - B _ { z } } & { 0 } & { B _ { x } } & { - \mathrm { i } E _ { y } / c } \\ { B _ { y } } & { - B _ { x } } & { 0 } & { - \mathrm { i } E _ { z } / c } \\ { \mathrm { i } E _ { x } / c } & { \mathrm { i } E _ { y } / c } & { \mathrm { i } E _ { z } / c } & { 0 } \end{array} \right) .
$$