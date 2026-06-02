# EXPLANATORY SUPPLEMENT to the ASTRONOMICAL ALMANAC

Edited by Sean E.UrbanandP.KennethSeidelmann

![](images/13bb7f8e5bf4f9edd5929b24d8e49b977fd0e9f7dad575dcbdd0ff90cb5756ed.jpg)

# Explanatory Supplement to the Astronomical Almanac

THIRD EDITION

Edited by

Sean E.Urban USNaval Observatory

P. Kenneth Seidelmann University of Virginia

Foreword by Roger Sinnott

# Explanatory Supplement to the Astronomical Almanac

THIRD EDITION

Sean E.Urban US Naval Observatory

P. Kenneth Seidelmann University of Virginia

Foreword by Roger Sinnott

University Science Books www.uscibooks.com

Production Manager:Paul C.Anagnostopoulos,Windfall Software TextDesign:Paul C.Anagnostopoulos   
Illustrator:LaurelMuller   
Compositor:Windfall Software   
CoverDesign:Genette ItokoMcGrew   
Printer&Binder:EdwardsBrothers,Inc.

This book was setin Times RomanandMyriad Pro and composed with ZzTEX,amacro package for Donald Knuth's TEX typesettingsystem.

This book is printed on acid-free paper.

Theappearance of non-US government website addresses does not constitute endorsement by the United StatesDepartment ofDefense(DoD),theUnited StatesDepartmentof theNavy,or theU.S. Naval Observatory of those websites,or the information,products or services contained therein.The above-mentioned parties donot exerciseany editorial controlover theinformation you mayfindatthese locations nor do they accept responsibility forloss or damage arising from the use of the information on these site.

ISBN:978-1-891389-85-6

Foreword xxvii   
Preface xxxi   
Contributing Authors xxxiii   
1 Introduction to Positional Astronomy 1   
2Relativity for Astrometry, Celestial Mechanicsand Metrology 45   
3Time 75   
4The Fundamental Celestial Reference System 105   
5Terrestrial Coordinates and the Rotation of the Earth 123   
6Precession,Nutation,Polar Motion,and Earth Rotation 199   
7Positions 249   
8Orbital Ephemerides of the Sun,Moon,and Planets 305   
9Planetary Satellites and Rings 347   
10Physical Ephemerides of Solar System Bodies 399   
11Eclipses of the Sun and Moon 453   
12Astronomical Phenomena 505   
13Stars and Stellar Systems 529   
14Computational Techniques 555   
15 Calendars 585   
A Bases and Constants 625   
B Acronyms 627   
C Glossary 633   
Index 661

Foreword xxvii Preface xxxi Contributing Authors xxxiii

# 1 Introduction to Positional Astronomy

1.1 Introduction1 1.1.1 Purpose1 1.1.2 Introductionto TheAstronomical Almanac 1 1.1.3 TheAstronomical Almanac and The Explanatory Supplement3 1.1.4 Conceptual Changes since the Last Edition 3 1.1.5 Implementation of the Changes7 1.1.6 Deletions from This Edition and The Astronomical Almanac9

1.2 Timescales and Calendars 9 1.2.1 Atomic Timescales 9 1.2.2 Dynamical Time 10 1.2.3 TimescalesBasedon Earth'sRotation1l 1.2.4 Coordinated Universal Time(UTC)13 1.2.5 Enumeration of Dates14

1.3 Celestial and Terrestrial Coordinates15 1.3.1 Coordinate Systems and Frames15 1.3.2 Celestial Coordinate Systems18 1.3.3 Terrestrial Coordinate Systems20 1.3.4 TheRotation ofthe Earth24 1.3.5 Connectionsbetween Terrestrial and Celestial Coordinates25 1.3.6 Effects of the Position and Motion of the Object and Observer27

1.4 Orbital Motion29 1.4.1 Motion in Two-Body Systems29 1.4.2 Ephemerides33 1.4.3 Perturbations by and on Extended Bodies35

1.5 Solar System36 1.5.1 Sun36 1.5.2 Planets37 1.5.3 Satellites37 1.5.4 Other Bodies38 1.5.5 Planetary Coordinates38

1.6 Astronomical Phenomena 38 1.6.1 Rising,Setting,and Twilight 39 1.6.2 Meridian Transit39 1.6.3 Conjunction,Opposition,and Elongation 40 1.6.4 Eclipses,Occultations,and Transits40 1.6.5 Satellite Phenomena41 1.6.6 Physical Observationsof theSun,Moon,and Planets 42 References43

# 2Relativityfor Astrometry,Celestial Mechanicsand Metrology 45

∠.1 Introaucuon 45   
2.2 Newtonian Formalism46   
2.3 Special Relativityand the Metric Tensor 48   
2.4 Einstein's Theory of Gravity 50   
2.5 The Problem of Observables52 2.5.1 TheRanging Observable52 2.5.2 The Spectroscopic Observable52 2.5.3 Astrometric Observables54   
2.6 The Post-Newtonian Framework55 2.6.1 Coordinate Timescales and Proper Time56 2.6.2 The Barycentric Celestial Reference System56 2.6.3 BCRS versus ICRS59 2.6.4 The Geocentric Celestial Reference System59 2.6.5 Coordinate Transformations62 2.6.6 Relativistic Potential Coeffcients62   
2.7 Applications63 2.7.1 Other Versions ofthe GeocentricCelestial Reference System63 2.7.2 Rotating Reference Systems64 2.7.3 The Einstein-Infeld-Hoffmann Equations of Motion64 2.7.4 Equations of Motion in the GCRS66 2.7.5 Astrometry66 2.7.6 VLBI Observations 68   
2.8 Relativistic Timescales,their Definitionsand Units 68 2.8.1 Practical Transformations ofTimescales68 2.8.2 ScaledCoordinateTimescales 69 2.8.3 Units of Timescales70 References 71

# 3Time

3.1 Introduction 75 3.1.1 Absolute (or Newtonian) Time75 3.1.2 Proper Time75 3.1.3 Coordinate Time 76

3.2Time and the Earth's Rotation76

3.2.1 Sidereal Time 77   
3.2.2 UT180

3.3 Dynamical Time 81 3.3.1 Ephemeris Time 82 3.3.2 TDT/TDB83

.4 Atomic Time83 3.4.1International Atomic Time,TAl 84 3.4.2 Terrestrial Time,TT84

3.5 Civil Time 85 3.5.1 Coordinated Universal Time,UTC85 3.5.2 Time Zones86

6 Barycentric and Geocentric Coordinate Time88 3.6.1 BarycentricCoordinate Time,TCBand Barycentric Ephemeris Time, $T _ { \mathrm { e p h } }$ 88 3.6.2 Geocentric Coordinate Time,TCG89

3.7Julian Date91

3.9 Timekeeping 93 3.9.1 Devices93 3.9.2 International Agencies95

3.10Time Dissemination 96 3.10.1 High-Frequency Radio Time Signals97 3.10.2 Low-Frequency Radio Time Signals97 3.10.3 LORAN-C97 3.10.4 Global Positioning System(GPS)98 3.10.5 GLONASS98 3.10.6 GALILEO98 3.10.7 Two-Way Satellite TimeTransfer(TWSTT) 99 3.10.8 Time Transfer by Internet99

3.11 Relativistic Effects 99 3.11.1 ClockTransport froma RotatingReferenceFrame 99 3.11.2 Non-rotating Local Inertial Reference Frame100 3.11.3 ElectromagneticSignal Transferfroma RotatingReference Frame 101 3.11.4 Electromagnetic Signal Transferfroma Non-rotating, Local Inertial Frame 101 References 101

# 4The Fundamental Celestial Reference System

4.1 Summary105   
4.2 TheICRS,the ICRF,and theHCRF 105   
4.3 Background: Reference Systems and Reference Frames 108   
4.4 The Effect ofCatalog Errors on Reference Frames 109   
4.5 Late 20th Century Developments111   
4.6 ICRS Implementation112 4.6.1 TheDefining Extragalactic Frame 112 4.6.2 TheFrame at Optical Wavelengths113 4.6.3 Standard Algorithms 114

4.6.4Relationship to Other Systems114   
4.6.5Data in the ICRS115   
4.7 Formulae 117   
References118

# 5Terrestrial Coordinatesand the Rotation of the Earth

5.1 Introduction 123   
5.2 Terrestrial Reference Systems 124 5.2.1 Reference Systems and Reference Frame Concepts124 5.2.2 TheFigureof the EarthandGeodeticReference Surfaces 127 5.2.3 Geodetic Datums128 5.2.4 Geocentric,Geodetic,and Astronomical Coordinates 131 5.2.5 Local Coordinate Systems134   
5.3 Gravity,Tides,and Motions of the Crust 148 5.3.1 Modelingthe Earth'sGravityField149 5.3.2 Representationofthe Earth'sGravityField 150 5.3.3 Solid Earth Tides153 5.3.4 Ocean TideModel 158 5.3.5 Site Displacement Due to Ocean and Atmospheric Loading 162 5.3.6 PlateMotions 169 5.3.7 Tidal Effects in UTl 170 5.3.8 TidalEffects inPolarMotion 171   
5.4 Monitoring the Orientation of the Earth 175 5.4.1 VeryLong BaselineInterferometry 176 5.4.2 Global NavigationSatellite System 177 5.4.3 Laser Ranging 179 5.4.4 Doppler Orbitography and Radiopositioning Integrated by Satellite(DORIS）181 5.4.5 Historical Methods 181 5.4.6 Alternative Techniques183 5.4.7 International Services 184 References 187

# 6Precession,Nutation,Polar Motion,and Earth Rotation

6.1 Introduction 199   
6.2 The Celestial Reference System(CRS)and the Terrestrial Reference System (TRS）200 6.2.1 Reference Systems in The Astronomical Almanac 202 6.2.2 TheConventional International Originand the International Terrestrial ReferenceFrame(ITRF) 203 6.2.3 TheCelestial Intermediate ReferenceSystemandtheCelestial IntermediatePole(CIP) 204 6.2.4 The Equinoxes206

6.3The Equation of the Equinoxes, $E _ { e } ( T )$ 207

6.4The Equationof the Origins, $E _ { o } ( T )$ 208

6.5The J2000.0 to ICRS Frame Bias Matrix208

Precession and Nutation 209   
6.6.1 TheIAU 2000 Precession-Nutation Theory and IAU 2006/2000A209   
6.6.2 Precession 211   
6.6.3 Nutation 223

6.7The Celestial Intermediate Origin(CIO）227

6.8 Time and Earth Orientation229 6.8.1 Apparent SolarTime,Mean Solar Time,andtheEquationofTime230 6.8.2 Greenwich Mean Time 231 6.8.3 Universal Time(UT）232 6.8.4 EarthRotation Angle(ERA or0） 233 6.8.5 Sidereal Time 234 6.8.6 Conversions between Universal Time and Sidereal Time235 6.8.7 Conversion ofLocal Apparent Sidereal Time to UTl 237 6.8.8 Local Time and Hour Angle238

6.9 The Terrestrial Intermediate Origin (TIO) 239 6.9.1 The Ephemeris Meridian239 6.9.2Polar Motion 240 References 244

# 7Positions

Introduction 249 7.1 Summary of Systems,Places,and Coordinates 250 7.1.1 Reference Systems251 7.1.2 Places252 7.1.3 Coordinates 253 7.1.4 Summary of Notations 257

7.2 Components Used in the Reduction of Positions 258 7.2.1 Space Motion 258 7.2.2 Parallax 261 7.2.3 Aberration 263 7.2.4 Gravitational Light-Deflection 270 7.2.5 Celestial“OfDate"Positions 272 7.2.6 Terrestrial “Of Date"Positions275 7.2.7 Refraction277

7.3 Reduction of Positions from the BCRS to the GCRS 281 7.3.1 Proper Place281 7.3.2 Local Place281 7.3.3 Astrometric Place 281 7.3.4 Differential Astrometry 283

7.4.1 Apparentand IntermediatePlace Algorithm for Planets283   
7.4.2 Apparent and Intermediate Place Algorithm for Stars290   
7.4.3 Topocentric Place Algorithm 293   
7.4.4 Summary of the Algorithms297   
7.4.5 Approximate Algorithms 298   
References301   
Further Reading 303

# 8Orbital Ephemerides of the Sun,Moon,and Planets

8.1 Fundamental Ephemerides 305   
8.2 PreviousEphemeridesUsed in TheAstronomical Almanac 306 8.2.1 EphemeridesPrior to1984 306 8.2.2 Ephemerides from 1984 through 2002307 8.2.3 Ephemerides Starting in 2003 307

8.3 Equations of Motion 307 8.3.1 Point-Mass Interactions 308 8.3.2 Solar System Barycenter 309 8.3.3 Figure Effects309 8.3.4 Lunar Gravity Coefficients310 8.3.5 Lunar Physical Libration:Coordinates311 8.3.6 Physical Libration Differential Equations311 8.3.7 TheMoment of Inertia Tensor312 8.3.8 Time Derivative of the Inertia Tensor312 8.3.9 Principal Moments 313 8.3.10 Figure-Point Mass Torques upon the Moon313 8.3.11 Figure-Figure Torque upon the Moon 313 8.3.12 Accelerationof the Moon from Earth Tides314

8.4 The Numerical Integration of DE405/LE405 315 8.4.1Estimated Integration Error315 8.4.2Adopted Constants315

8.5 Observational Data Fitby the Planetary and Lunar Ephemerides 316 8.5.1 Optical Data316 8.5.2 Meridian Transits 316 8.5.3 Photographic and CCD Astrometry317 8.5.4 Occultation Timings317 8.5.5 Astrolabe 317 8.5.6 RadiometricEmissionMeasurements 317 8.5.7 Ranging Data 317 8.5.8 Orbiter Range Points320 8.5.9 Lander Range Data320 8.5.10 VLBIData320 8.5.11 Lunar Laser Range Data320

8.6 The Orientation of DE405/LE405321 8.6.1Adjustmentof DE405 onto the ICRF Reference Frame321

8.7 Various Formulae Used in the Reduction of the Observational Data321 8.7.1 Phase Corrections322 8.7.2 Corrections to Precession and Equinox Drift322 8.7.3 Computation of Ranges322

8.7.4 Antenna Location 323   
8.7.5 TimeDelay forRelativity323   
8.7.6 TimeDelayfortheSolarCorona 323   
8.7.7 Time Delay for the Troposphere324   
8.7.8 Modeling the Surface ofMercury 324   
8.7.9 Modeling the SurfaceofVenus324   
8.7.10 Modeling the Surface ofMars-Closure Points325   
8.7.11 Viking Lander Computations 325

8.8 Initial Conditions and Constants of DE405/LE405325 8.8.1Asteroids 332

8.9 Positional Errors of the Planetary and Lunar Ephemerides332 8.9.1 InnerFour Planets:Ephemerides fromRangingand VLBl332 8.9.2 Uncertainties fromAsteroid Perturbations333 8.9.3 OuterPlanets:Reliance ontheClassical Optical Observations333 8.9.4 Planetary Positional Errors in the Almanacs,1984-20o2 333 8.9.5 Planetary Position Uncertainties in 20o3 333

8.10Keplerian Elements forApproximate Positionsof theMajorPlanets 338 8.10.1Formulae for Using the Keplerian Elements339 8.10.2Solution of Kepler's Equation, $M = E - e$ sin $E$ 340 8.10.3Approximate Accuracies ofthe Keplerian Formulae341

8.11The Availability of Ephemerides341 References342

# 9Planetary Satelites and Rings

9.1 Introduction 347   
9.2 Orbital Elements and Perturbations 347 9.2.1 Orbital Elements347 9.2.2 Secular Perturbations of the Orbit349 9.2.3 Perturbationsdue to Commensurabilities351 9.2.4 Long-Period Perturbations by Other Satellites352   
9.3 Planetocentric Rectangular Coordinates 353   
9.4 Traditional Method356 9.4.1 The Apparent Orbit 356 9.4.2 Calculating Tabulated Values360   
9.5 Modern Method361 9.5.1 The Apparent Orbit 361 9.5.2 Calculating Tabulated Values363   
9.6 SatelliteDatain The Astronomical AlmanacandNotation 365 9.6.1 Presented Data 365 9.6.2 Notation 365   
9.7 The Satellites ofMars 367   
9.8 The Satellites of Jupiter369 9.8.1 The Galilean Satellites369 9.8.2 Jupiter'sFifthSatellite,Amalthea373 9.8.3 Jupiter'sSixth throughThirteenth Satellites375   
9.9 The Rings and Satellites of Saturn 376 9.9.1The Rings of Saturn376 9.9.2The Satellites of Saturn 378   
9.10 The Rings and Satellites of Uranus 388   
9.11 The Satellites of Neptune 393 9.11.1Triton393 9.11.2Nereid394   
9.12 The Satellites of Pluto 396 References 397

# 10Physical Ephemerides of Solar System Bodies

10.1 Introduction 399   
10.2 Rotational Elements and Cartographic Coordinates 399 10.2.1 Planetocentric and Planetographic Coordinate Systems401 10.2.2Coordinate Systems of Small Bodies406   
10.3 Phases and Magnitudes410 10.3.1Absolute and Apparent Magnitudes410 10.3.2Surface Brightness412   
10.4 The Apparent Disk of a Solar System Body415 10.4.1Sub-Earth Points and Sub-Solar Points417 10.4.2The Greatest Defect of Illumination 422 10.4.3The Apparent Magnitudes of the Minor Planets422   
10.5 Physical Ephemeris of the Sun426   
10.6 Physical Ephemeris of the Moon427 10.6.1Calculating Librations429   
10.7 Physical Ephemerides of the Planets 434 10.7.1 Mercury435 10.7.2 Venus 435 10.7.3 Mars 436 10.7.4 Jupiter 436 10.7.5 Saturn 436 10.7.6 Uranus 437 10.7.7 Neptune 437   
10.8 Physical Ephemerides of the Dwarf Planets437   
10.9 Physical Ephemerides of the Satellites438 10.9.1 Satellites of Mars 438 10.9.2 Satellites ofJupiter 439 10.9.3 Satellites of Saturn 441 10.9.4 Satellites of Uranus 441 10.9.5 Satellites of Neptune443 10.9.6 Satellites of Pluto447 References 447

# 11Eclipses of the Sun and Moon

11.1 Introduction453 11.1.1Eclipse Data Available from the Nautical Almanac Offces454 11.1.2Corrections to the Ephemerides456   
11.2 The Occurrence of Lunar and Solar Eclipses 457 11.2.1 Overview457 11.2.2 Geocentric Least Angular Separation 457 11.2.3 Occurrence of Lunar Eclipses 459 11.2.4 Occurrence of Solar Eclipses461   
11.3 Solar Eclipses464 11.3.1 Fundamental Equations:Introduction 464 11.3.2 Besselian Elements 464 11.3.3 Coordinates of the Observer470 11.3.4 Conditional and Variational Equations 474 11.3.5 Calculation ofGeneral Solar Eclipse Phenomena 477 11.3.6 Local Circumstances487   
11.4 Lunar Eclipses491 11.4.1Introduction 491 11.4.2Computations492   
11.5 Eclipses Online495 11.5.1Solar Eclipses 495 11.5.2Lunar Eclipses497   
11.6 Transits 499 References 502 Further Reading 502

# 12Astronomical Phenomena

12.1General Aspects of the Night Sky505   
12.2Configurations of the Sun,Moon,and Planets506 12.2.1InterestingPhenomena ofthe Sun,Earth,andMoon 506 12.2.2 Geocentric Phenomena 508 12.2.3 Heliocentric Phenomena511   
12.3 Risings,Settings,and Twilight511 12.3.1 Sunrise,Sunset,and Twilight 512 12.3.2 Moonrise and Moonset 514 12.3.3 Formulae Associated with Rising and Seting515 12.3.4 Illumination 518   
12.4 Occultations 521 12.4.1Occultations of Stars521 12.4.2Occultations of Planets 524   
12.5 Pole Star Tables525 12.5.1Derivation of the Pole Star Coeficients527 References 528

# 13Stars and Stellar Systems

13.1Introduction529 13.1.1Data Presentation 529 13.1.2Sources of Data530 13.1.3Sources of Position530

13.2 StellarData 531 13.2.1 Bright Stars 531 13.2.2 Double Stars532 13.2.3 Photometric Standards534 13.2.4 Radial Velocity Standards536 13.2.5 Variable Stars537 13.2.6 Exoplanets and Host Stars 538 13.2.7 Pulsars539

13.3 Clusters and Galaxies539 13.3.1 Open Star Clusters539 13.3.2 Globular Star Clusters541 13.3.3 Bright Galaxies542 13.3.4 Quasi-Stellar Objects544

13.4Wavelength Specific Sources 545 13.4.1Radio-Source Positional Calibrators 545 13.4.2Radio-Flux Calibrators 546 13.4.3X-Ray and Gamma Ray Sources547 References548

# 14 Computational Techniques

14.1Introduction to Computing Techniques555

14.2Interpolation and Subtabulation 559 14.2.1 Introduction and Notation 559 14.2.2 Interpolation Formulae 560 14.2.3 Inverse Interpolation 561 14.2.4 Polynomial Representations561 14.2.5 Chebyshev Polynomials562

14.3Plane and Spherical Trigonometry563

14.4 Matrix and Vector Techniques565 14.4.1Matrix Multiplication565 14.4.2 Rotation of Axes Using Matrices565 14.4.3 Spherical Coordinates Using Vectors 567 14.4.4Specific Coordinate Transformations 569

14.5Numerical Calculus 572 14.5.1Numerical Differentiation 572 14.5.2Numerical Integration 574

14.6 Statistics578 14.6.1Accumulation of Error578 14.6.2The Method ofLeast-Squares579 References 583

15.1 Introduction585 15.1.1 Overview585 15.1.2 Uses ofCalendars586 15.1.3 Astronomical Bases ofCalendars 586 15.1.4 Astronomical,Observational and Arithmetic Calendars 587 15.1.5 Visibility of the Crescent Moon 588 15.1.6 Non-astronomical Cycles and the Week 588 15.1.7 Historical Eras and Chronology589 15.1.8 TheChristian Era589 15.1.9 Dates591 15.1.10 Julian Day Numbers and Julian Dates591 15.1.11 Luni-solar Calendars592 15.1.12 Accuracy of Calendars593

15.2The Ancient Egyptian Calendar593 15.2.1History of the Egyptian Calendars593 15.2.2Rules of the Egyptian Calendar594

15.3The Roman and Julian Calendars 594 15.3.1 Introduction 594 15.3.2 Divisions of the Roman Months595 15.3.3 Caesar'sReform 595 15.3.4 The Julian Calendar in Medieval Europe597 15.3.5 Rulesfor the Julian Calendar597

15.4The Gregorian Calendar598 15.4.1History ofthe Gregorian Reform598 15.4.2 Rulesfor the Civil Useof the Gregorian Calendar599 15.4.3 Rulesfor the Ecclesiastical Calendar599 15.4.4Calculation ofthe Date of Easter Sunday600

15.5The Jewish Calendar601 15.5.1 History of the Jewish Calendar601 15.5.2 Rulesfor the ModernJewish Calendar602 15.5.3 Rules for Postponement (Dehiyyot）603 15.5.4 Determining Tishri1 604 15.5.5 Determining the Lengthof the Year605 15.5.6Terminology ofthe Jewish Calendar606

15.6The Islamic Calendar606 15.6.1Introduction606 15.6.2History of the Islamic Calendar607 15.6.3Rules for the Arithmetic IslamicCalendar607

15.7The Indian Calendars 608 15.7.1History ofIndian Calendars608 15.7.2 The Traditional Indian Solar Calendar 609 15.7.3 The Traditional Indian Luni-solar Calendar609 15.7.4Rules of the Reformed Saka Calendar 610

15.8The Chinese Calendar610 15.8.1History of the Chinese Calendar610 15.8.2Sexagenary Cycle 612

15.8.3Major and Minor Terms612   
15.8.4 Rules for the Modern Chinese Calendar 613   
15.8.5 Finding the First Day ofa Chinese Year614   
15.8.6Finding the First Day of Each Month inaChinese Year615

15.9The French Republican Calendar616

15.10 The Baha'iCalendar616

15.11 Calendar Conversion Algorithms617 15.11.1 Introduction617 15.11.2 Calculating the Dayofthe Week618 15.11.3Interconverting DatesandJulianDay Numbers 618 15.11.4 Converting Dates in the Jewish Calendar619 15.11.5 Calculating the Date of Easter621

15.12 CalendarConversion Programs621References 622

# A Bases and Constants

625

A.1 Bases 625   
A.2 Astronomical Constants 625 A.2.1 CODATA626 A.2.2 Future of the Astronomical Unit 626 References 626

BAcronyms 627

C Glossary 633

Index 661

1.1 Calculation of sidereal time12   
1.2 Variation in the equation of time through the year13   
1.3 Representation of the vector r in rectangular coordinates17   
1.4 Equatorial and ecliptic reference planes19   
1.5 Geocentric and geodetic coodinates21   
1.6 Relation between geographic latitude and the altitude of the celestial pole24   
1.7 Parallax of an object27   
1.8 Geometric properties of conic sections31   
1.9 Angular orbital elements32   
2.1 Schematic of a ranging observable53   
2.2 Schematic of a spectroscopic observable53   
2.3 Schematic of an astrometric observable55   
3.1 World time zone map88   
3.2 Relationship among timescales90   
3.3 Interrelationship of timescales93   
4.1 Schematic of the celestial coordinates of a catalog object108   
4.2 Errors in proper motion resulting from the random errors in the measurement of position at   
various epochs111   
5.1 The Earth's surface and reference surfaces128   
5.2 Geocentric $( \phi ^ { \prime } )$ and geodetic $( \phi )$ latitude130   
5.3 Astronomical latitude and longitude130   
5.4 Deflection of the vertical on a unit sphere133   
5.5 Geocentric Cartesian coordinates and geographical coordinates133   
5.6 Horizon system altitude and azimuth135   
5.7 UTMand UPS grid zone designations138   
6.1 Relationship between origins of right ascension 202   
6.2 Motions on the sky of the ecliptic pole,the Earth’s mean pole and the CIP210   
6.3 General precession connects the mean equinox of epoch to the mean equinox of date213   
6.4 Precession angles connect the mean pole of epoch to the mean pole of date214   
6.5 The difference between Lieske et al.(1977) and the Newcomb (1895) definitions of the   
general precession 215   
6.6 The Lieske et al. (1977) precession angles217   
6.7 The nutations in longitude and latitude relate the mean pole of date to the CIP via the eclipti   
pole of date225   
6.8 Schematic representation of the relationships between the different fiducial meridians   
encountered in thecelestial and terrestrial coordinate systems 240   
6.9 Motion of the pole with respect to the Conventional International Origin from 1973.O throug   
2009.5241   
6.10 Polarmotion in x,y from 1973.0 through 2009.5242   
7.1 Relationships of origins 254   
7.2 Light-time displacement264   
7.3 Stellar aberration265   
7.4 Gravitational light-deflection271   
7.5 Light from the planets and stars deflected by the Sun273   
8.1 Differences in right ascension,declination and distance between DE2oo-DE409 334   
8.6 Differences in right ascension,declination and distance between DE2oo-DE409 335   
8.11 Differences in right ascension,declination and distance between DE4O5-DE409 336   
8.16 Differences in right ascension,declination and distance between DE4o5-DE409 337   
9.1 The orbital elements used to describe the orbital plane relative to a reference plane348   
9.2 An equivalent form of the orbital elements348   
9.3 The Laplacian plane350   
9.4 The satellite orbit referred toan intermediate plane355   
9.5 Coordinates of the satellite relative to the planet355   
9.6 Planetocentric celestial sphere 357   
9.7 Spherical triangle used to compute $U$ , $B$ ,and $P$ 358   
9.8 Spherical triangle used to compute $\sigma$ and $p - P$ 358   
9.9 Apparent orbit of a satellite as projected on the geocentric sphere359   
9.10 Apparent orbit of the satelite projected on to the tangent plane,and the coordinate system   
used362   
9.11 Reference system for Phobos and Deimos368   
9.12 Reference system for Amalthea and Thebe374   
9.13 Reference plane for Mimas,Enceladus,Tethys,and Dione379   
9.14 Reference system forRhea,Titan,Hyperion,Iapetus,andPhoebe 383   
9.15 Angles needed to evaluate solar perturbations on Titan383   
9.16 Reference system for the Uranian satellites392   
9.17 Reference system for Triton394   
9.18 Reference system for Nereid395   
10.1 The position of the north pole and prime meridian of a solar system body in Earth equatoria   
coordinates400   
10.2 Planetocentric and planetographic coordinates systems403   
10.3 The basic vectors and angle of illumination, $i$ ,in the Earth-Sun-planet plane411   
10.4 The geometric appearance of the apparent polar radius, $b ^ { \prime }$ 416   
10.5 The disk of a planet as seen from an observer on the Earth418   
10.6 Planetocentric unit vectors and angles420   
10.7 Lunar angles given in the JPL ephemerides Vs.the traditional angles430   
10.8 The angles of the lunar orbit used in the determination of the apparent librations of   
the Moon432   
11.1 Geometric construct for determining whether an eclipse will occur458   
11.2 Geometric parameters of the Earth's penumbral shadow460   
11.3 Geometric parameters of the Earth's umbral shadow460   
11.4 Limiting conditions for lunar eclipses461   
11.5 Geometric parameters for a partial solar eclipse when Moon is externally tangent462   
11.6 Geometric parameters for a partial solar eclipse when Moon is internally tangent463   
11.7 Transformation of geocentric equatorial coordinates to the fundamental plane465   
11.8 Components of shadow cones in the Besselian fundamental reference system467   
11.9 Relationships among angular semidiameter,apparent semidiameter,and parallax468   
11.10 Vertex angle of the penumbra469   
11.11 Vertex angle of theumbra469   
11.12 Angular quantities in the geocentric equatorial plane470   
11.13 Relationship between rectangular and polar reference systems478   
11.14 Definition of auxiliary quantity $\psi$ 484   
11.15 Visualization of the magnitude of a solar eclipse489   
11.16 Visualization of the obscuration of a solar eclipse490   
11.17 Total solareclipsediagram from EclipsesOnline 496   
11.18 Total lunar eclipse diagram from Eclipses Online 498   
11.19 Transits across the Sun501   
12.1 The analemmic curve514   
12.2 The horizon at rising or setting 517   
12.3 Ground illumination from various sources519   
12.4 Fundamental plane showing path of occultation 524   
12.5 PZS triangle for Polaris525   
12.6 Polaris north polar distance 2096-2105527   
14.1 Spherical triangle 556   
14.2 Thefirst few Chebyshev polynomials of the first kind563   
14.3 Arc of circle565   
14.4 Triangle on unit sphere 568   
1.1 Variations in the Earth's rate of rotation25   
3.1 TAI-UTC(△AT)87   
3.2 Low-frequency radio time signals97   
5.1 Earth ellipsoids143   
5.2 Historical geodetic datums144   
5.3 Suggested truncation levels for use of EGM2oo8 at different orbits151   
5.4 Low-degree coeficients of the conventional geopotential model. 152   
5.5 Solid tide corrections when $k _ { 2 } = 0 . 3 0$ 154   
5.6 Ocean tide coefficients from the Schwiderski model160   
5.7 Displacement due to ocean loading164   
5.8 Cartesian rotation vector for each plate using absolute plate model NNR-NUVEL-1A (no net   
rotation）170   
5.9 Zonal tide terms with periods up to 35 days172   
5.10 Zonal tide terms with periods greater than 35 days173   
5.11 Ocean tidal variations in polar motion and polar motion excitation174   
5.12 Estimated accuracies of EOP techniques175   
6.1 Coefficients of the series for the equation of the equinoxes, $E _ { e }$ ,larger than 0.5μas207   
6.2 Coefficients describing the position of the ecliptic of date with respect to the ecliptic of   
J2000.0 213   
6.3 IAU recommended coefcients describing the position of the ecliptic of date with respect to   
the ecliptic of J2000.0216   
6.4 Lieske et al.(1977) coefficients describing the position of the ecliptic of date with respect to   
the ecliptic of J2000.0 (obsolete）216   
6.5 Precession angles with respect to the mean equator and equinox of B195o.0 at 1984 Jan. $1 ^ { d } 0 ^ { h }$   
for various precession theories222   
6.6 Critical arguments for the IAU 20ooA nutation227   
7.1 Summary of reference systems250   
7.2 Summary of places250   
7.3 Coefficients (nma/c) for the planets267   
7.4 Apparent deflection angles272   
8.1 Observational data fit by DE405318   
8.2 Initial conditions at JED $\mathrm { ( T _ { e p h } ) }$ 2440400.5(June 28,1969)326   
8.3 J2000.0 angular coordinates of the lunar physical librations326   
8.4 Dynamical constants used in the integration of DE405/LE405327   
8.5 Auxiliary constants used in the observational reductions for DE405/LE405 329   
8.6 The297 non-Big 3 individual asteroids used in the integration of DE4o5330   
8.7 Keplerian elements and their rates,with respect to the mean ecliptic and equinox of J2000.0,   
valid for the time-interval A.D.1800-A.D.2050338   
8.8 Keplerian elements and their rates,with respect to the mean ecliptic and equinox of J2000.0,   
valid for the time-interval 3000 B.C.-A.D.3000339   
8.9 Additional terms for the computation of $M$ for Jupiter through Pluto339   
8.10 Approximate errors in right ascension, $\alpha$ ,declination, $\delta$ ,and distance, $\rho$ ,from the Keplerian   
formulation of $\ S 8 . 1 0 . 3$ 341   
9.1 Principal commensurabilities among satellites353   
9.2 Summary of satellite positional data in The Astronomical Almanac366   
9.3 The starting planetocentric coordinates and velocities of some Jovian satellites 376   
10.1 The positions of the poles and prime meridians of the planets and Pluto402   
10.2 The equatorial radii and flattenings of the planets and Pluto403   
10.3 The radii of planetary satellites404   
10.4 The radii and effective radius of selected asteroids and comets408   
10.5 The diameters of the asteroids408   
10.6 The visual magnitudesand phase coefficients forthe planets,Pluto,and the Galilean satellites   
ofJupiter413   
10.7 The visual magnitudes and Johnsoncolors of the satelltes413   
10.8 The $H$ and $G$ parameters for the minor planets424   
10.9 The rotation parameters for Mars’satelltes439   
10.10 The rotation parameters for Jupiter's satellites440   
10.11 Standard cartographic longitudes for Jupiter'ssatellites 441   
10.12 Rotation parameters for Saturn's satellites442   
10.13 Standard cartographic longitudes for Saturn's satelites443   
10.14 Rotation parameters for Uranus’satellites444   
10.15 Rotation parameters for Neptune's satellites446   
10.16 Rotation parameters for Pluto's satelite,ICharon447   
11.1 Selected USNO eclipse circulars455   
11.2 Sequences and conditions for contact times494   
11.3 Transits of Mercury for 112 years500   
12.1 Time of commencement of the seasons during the 21st century 507   
12.2 Geocentric phenomena for which $f ( t ) = 0$ 509   
12.3 Geocentric phenomena for which $f ^ { \prime } ( t ) = 0$ 510   
12.4 Visibility criteria for geocentric phenomena 510   
12.5 Synodic periods of selected solar system objects510   
12.6 Long-period cycles of Mercury,Venus,and Mars511   
12.7 Heliocentric phenomena 511   
12.8 Coefficients for calculating ground illumination519   
14.1 Precision of angle and number of decimals for trigonometric functions557   
14.2 The method of inverse use 558   
14.3 Range of precision of the inverse determination of an angle558   
14.4 Differences in tabular arguments560   
14.5 Formulae for plane and spherical triangles564   
14.6 Derivatives to an order of 10575   
14.7 Accumulation of error in arithmetical operations 579   
15.1 Approximate lengths of the astronomical cycles587   
15.2 Some eras590   
15.3 Months in theancient Egyptian calendar594   
15.4 Roman datingin the Julian calendar596   
15.5 Monthsand days therein of the Julian and Gregoriancalendars 597   
15.6 Number of daysin the six categories of the Jewish year 603   
15.7 Monthsand days therein of the Jewish calendar603   
15.8 Periods corresponding to different numbers of lunations 605   
15.9 Monthsand daysthereinof the formal Islamic calendar 607   
15.10 Months of the Indian solar calendar609   
15.11 Months in the Indian luni-solar calendar610   
15.12Celestial Stems and the Earthly Branches of the sexagenary cycle612   
15.13Chinese solar terms613   
15.14Selected arithmeticcalendars,with parameters for algorithms617   
15.15Number of days in theJewish calendar that precede the first day of the mon

From ancient times,astronomers have crafted almanacs and star lists.Mariners once needed them to steertheir ships at sea,andfarmers to plant crops.Rulers have used them to schedule holydaysand holidaysalike.Andastronomers themselves havealways reliedonsuchworks for fedback about their understanding of the universe.(Do follow-up observations match predictions?Is anything amiss with established theories?)

To the majority of almanac users it makes little difference how the calculations are done, solong as they can be trusted.Butto the last category ofuser—astronomers—the underlying basis is just as important as any ephemeris.They need to know exactly where the numbers came from,and how the calculations might be carried forward into the future.Responsible parties,in their rush to issue timely tabular data orfor other reasons,have not always met this last need adequately.

To take one early example,Alexandrian astronomer Claudius Ptolemy might have been alittle clearer about the positions of1,O28 stars in his Almagest.Exactly how he updated an earlier star catalog for precession,or revised it using his own observations,are questions that still vex historians of astronomy two millennia later.

Infact,a detailed explanatory supplement is a fairly new feature in the long saga of astronomical tables.During the193Os the British Nautical Almanac began providing more detailed information about the derivation anduse of its tabular data,only to see the page count swell and make the annual volumes unwieldy.Plans to migrate explanatory material to a separate companion book,initially delayed byWorld War I,were further postponed by the decision to distinguish between Universal Time and Ephemeris Time.Not until1961 did thefirst Explanatory Supplement appear on the scene.Jointly produced and applying to the astronomical almanacs of both theUnited Kingdomand the United States,itwas the direct ancestor of the present volume.

Thatfirst Explanatory Supplement reflecteda tranquil time when planetary motions and the celestial reference frame seemed mostly under control.Newtonian mechanics was still state of the art,apart from minorrelativistic or empirical corrections for certain fast-moving bodies.Analytical theoriesworkedout decadesearlierby SimonNewcomb for theinner planets and Ernest W.Brown for the Moon continued to reign.The physical ephemerides of afew planetsand their satellites were stilltied to values derived in the19th century.Many pages in the back of the book listed constants connected with the planets’masses,motions, and physical characteristics that were intended to serve for years to come.

The philosophy of those years was leave well enough alone.So long as the astronomical almanacs provided enough accuracy for all civil and navigational purposes (which they did),itwas perfectlyall right—even desirable-tolet thepredictions drift fromreality by tiny amounts that only astronomers with delicate equipment might detect.The 1961 work explained the situation in a classic pronouncement:

Most non-astronomers,and even many astronomers not working in the dynamics of the solar system,expect to find ina national ephemeris a listofconstants the values of which,if they arenot absolutely accurate,areat least asup to dateaspossible.The importance of selfconsistency in the systemis litleappreciated,and the even greater importance of perpetuating avalue that is known to be incorrect is admited but seldom.The guardians of the system are accused of inactionand negligence,and even prejudice,by those who for one reason or another wish to introduce a new value for some constant.

Thatapproach,admirable inits day,helped in the way orbits and constants were eventually improved.To work on aparticular body,an astronomer could simplylook up its ephemeris in a long run of almanacs,compare that against an equally long run of observations,and solve forcorrections to form an improved theory.Calculating positions anew would have made thetask formidable.It's been said that a skilled astronomer needed six hours of pencil-andpaper work with Brown's1919 Tablesof theMotionof theMoon tocalculatea single,highly accurate position.

But the widespread use of computers has changed all that.Today it is easier to program an old theory,run off “calculated”values,and compare them on the fly with the“observed” ones.There is no longer a need to resist updating constants and planetary theories every few years.Startingwith the1984 almanacs and documented in the much revamped Explanatory Supplement of 1992,tweaks to the traditional ephemerides became more frequent.

The 2012 Explanatory Supplement goes a big step further.Readers may be surprised to see no master list of constants,past or present, in the back of this book.As Appendix A explains,such constantsare being refined so often that it makesbetter sense to state them in theyearly almanacs to which they apply and onappropriate websites.By focusing instead on procedures and minimizing numerical specifics,the printed Explanatory Supplement can retain its authority and usefulness longer.

Several other realities made this third edition necessary.Notice theup-front treatment of relativity (Chapter2).Those who doubt the impact of relativistic effectson daily life need look no further than the GPS devices in their cars.Similarly,to reduce the stellar data from the European Space Agency's Hipparcos mission,astronomers had to take into account the bendingof starlight by the Sun's gravity at elongationsup to $9 0 ^ { \circ }$ and beyond. Since 1992 we've also seen the wholesale replacement of the celestial reference frame,an outcome from thelinking of Hipparcos’soptical stellar positions with those from radio interferometry.

But the book isn't entirely about rigorous measurements and procedures.Along with specialists,a far broader audience will welcome the handy shortcuts,sprinkled throughout, when simple approximations are okay for things like atmospheric refraction,precession,and the equation of time.Historians will want to bookmark the thorough treatise on calendars (Chapter15).Turning to thecarefully honed glossary in the back,readers will finda better guide to common astronomical terms than any of the world's great dictionaries.

In recent years,with solar-system exploration and breakthroughs in cosmology in the limelight,the general public and even some scientists probably came to regard astrometry as an unglamorous backwater,a field of quaint techniques,echoing a sailor with a sextant.The stunning success ofHipparcos helped jar things back into perspective,and futureastrometric missions like Gaia will drive the point home.Careful measurements have always been the key to mastery of planetary and stellar dynamics and the cosmic distance scale.The material detailed in this book is the very bedrock underlying much else that we know about our own solar system and beyond.

Roger W. Sinnott Senior ContributingEditor,Sky&Telescope

Theprimarygoal ofTheExplanatory Supplement totheAstronomical Almanacistooffer explanatorymaterial,supplemental information,and detailed descriptionsof thecomputational models and algorithms used to produce The Astronomical Almanac.A secondary goal is to provide complementary information that does not change annually,such as conceptual explanations,data,and bibliographic references.To fulfill these goals,this book covers many aspects of modern positional astronomy; it iswritten at a scientifically technical-but non-expert—level.We hope it provides a useful reference fora fullrange of users including astronomers,engineers,navigators,surveyors,space sientists,ducators,historiansaswell as the general public.

The genesis of this work actually took place over 1OO years ago,beginning with the “Astronomical Papers of the American Ephemeris and Nautical Almanac”series.The material was compiled in one publication, now commonly known as“The Explanatory Supplement.” Thefirst edition,titled Explanatory Supplement totheAstronomical Ephemerisand The AmericanEphemerisandNauticalAlmanac,wasprepared jointlybytheUSNaval Observatory (USNO) Nautical Almanac Office (USNAO) and HerMajesty's Nautical Almanac Office(HMNAO); it was published byHerMajesty’sStationery Office(London)in1961and reprinted in1974.Thesecond edition,titled Explanatory Supplement totheAstronomical Almanac,waspreparedbyUSNOstaff,HMNAO staff,andafewnon-governmentsubjectmatterexperts;it was published in1992by UniversityScience Books.Thisbook is the third in the series.It is essentially a complete revision of the 1992 edition.Each chapter was updated; several of them completely re-written.Along with subjects covered in the previous two editions,it also contains descriptions of the major advancements in positional astronomy over the last 20 years.

Since the previous edition,several changes have taken place in positional astronomy. The International Celestial Reference System,new precession and nutation models,and a new positional paradigm no longer using the ecliptic and equinox have all come into existence. Thus,the staffsofHMNAOandUSNAO decided itis time fora new edition.

Theintention of the book is to explain theinformationin The Astronomical Almanac, not to form a complete discourse on astronomy.Because The Astronomical Almanac prints primarily positional data,this book goes into great detail on techniques to get astronomical positions.The book,however,isnotabasic textbook onspherical,dynamical,orpositional astronomy.We hope it supplements such textbooks because it contains detailed explanations and current methods of application.

Although most of the authorsare from either the USNOorHMNAO,some other subjectmatter experts wereasked to write abouttheir area of expertise.They includedMichael Soffel, SergeiKlioner,Bernard Guinot,Brent Archinal, JamesSlater,NikolaosPavlis,E.Myles Standish,James Williams,JamesRhode,Andrew Sinclair,Raynor Duncombe,and Edward Richards.Weare indebted to eachof them for their contributions.The glossary hasbeen evolving for years and the entire staffs of the USNO Astronomical Applications Department andHMNAO have contributed; DennisMcCarthy,Sergei Klioner,and Sergei Kopekin helped as well.We thank the management team of the UK Hydrographic Ofice for supporting the contributions of the HMNAO staff,without which this book would have been impossible. Finally,we acknowledge the support given over the yearsby the management team at USNO, specifically John Bangert,Head of the Astronomical Applications Department;Kenneth Johnston,Scientific Director of the USNO,and the various superintendents that have led USNO while thiswork was being compiled.

SeanE.Urban Chief,Nautical Almanac Office USNaval Observatory

P. Kenneth Seidelmann Department of Astronomy University ofVirginia

BrentA.Archinal US Geological Survey. Chapter 5.

John A.Bangert US Naval Observatory. Chapter 11.

Steven A.Bell HerMajesty'sNautical Almanac Ofice.Chapter11,Chapter12.

RaynorL.Duncombe University of Texas at Austin. Chapter 14.

Alan Fiala USNaval Observatory (retired,deceased).Chapter11.

Barnard Guinot Observatoire de Paris (retired).Chapter 3.

James L.Hilton US Naval Observatory. Chapter 6,Chapter 10.

CatherineHohenkerk HerMajesty's Nautical Almanac Office.Chapter7,Chapter 12.

George H. Kaplan US Naval Observatory (retired).Chapter 4,appendixes.

Sergei Klioner Lohrmann Observatory,Technical University,Dresden, Germany.Chapter 2.

Dennis D. McCarthy US Naval Observatory. Chapter 3,Chapter 6.

NikolaosK.Pavlis National Geospatial-Intelligence Agency. Chapter 5.

E. G.Richards The University of London. Chapter15.

JamesR.Rohde National Geodetic Survey. Chapter 9.

P.Kenneth Seidelmann University of Virginia.Chapter1,appendixes.

JamesA.Slater National Geospatial-Inteligence Agency (retired). Chapter 5.

Michael HermannSoffel Lohrmann Observatory,Technical University,Dresden, Germany.Chapter2.

E.Myles Standish Jet Propulsion Laboratory/California Institute of Technology (retired).Chapter 8.

Beth E. Stetzler US Naval Observatory. Chapter 5.

Susan G.Stewart USNaval Observatory.Chapter13.

Mark T. Stollberg US Naval Observatory.Chapter 9.

Sean E. Urban USNaval Observatory.Preface,appendixes.

JamesG.Williams Jet Propulsion Laboratory/California Institute of Technology (retired).Chapter 8.

Bernard Yallop HerMajesty'sNautical Almanac Office (retired).Chapter 12.

# Introduction to Positional Astronomy

P.KENNETHSEIDELMANN

# 1.1 Introduction

# 1.1.1 Purpose

TheAstronomical Almanac gives data on the positionsand,where appropriate,orientations ofthe Sun,Moon,planets,satellites,and stars during the courseofayear.These datadepend upon the fundamental concepts of spherical and dynamical astronomy. Spherical astronomy provides the tools,algorithms,and theories to determine the varying directionsof celestial objects;dynamical astronomy provides the tools,algorithms,and theories to predict their motions.Together,they determine thepositionalastronomy that underlies the data presented in The Astronomical Almanac and this volume.The Explanatory Supplement provides the theoretical background and expanded explanations concerning the material tabulated annuallyinTheAstronomicalAlmanac,as wellasotherpublicationsuchatTheNauticalAlmanac and The AirAlmanac.To aid the user of these books,thischapter introduces the concepts, terminology,and notation of spherical and dynamical astronomy,and also introduces the changes to The AstronomicalAlmanac since the 1992 edition of the Explanatory Supplement (Seidelmann 1992).Rigorous definitions,formulae,and explanations appear in later chapters ofthis book.The glossary gives concise definitions of words particular to spherical and dynamical astronomy.A summary list of the many acronyms used in the book is provided. The reference data are presented in a summary of tables or websites for the convenience of thereader.

# 1.1.2 Introduction to The Astronomical Almanac

The precise measurement of positions of the Sun,Moon,planets,and stars were necessary for the development of mechanics as wellas solar system dynamics.The great world system of Ptolemy (c.A.D.140) depended upon the stellar catalog ofHipparchus (c.150 B.c.).Nicholas Copernicus(A.D.1473-1543)depended uponPtolemy'scatalogs.Similarly,Johannus Kepler (A.D.1571-1630) needed the stellar catalogsby Tycho Brahe(A.D.1546-1601)to develop his famous three laws,and Brahe started with the positions of Hipparchus.The great synthesis of mechanics created by Isaac Newton (A.D.1643-1727),combined with Kepler'sLaws,the furtherdevelopments by Carl Friedrich Gauss (1777-1855),Pierre-Simon LaPlace (1749- 1827),Simon Newcomb (1835-1909)and many others,all standing on the works of these early scientists,led to the entire fields of celestial mechanicsand solar system dynamics, upon which the computations of modern spacecraft orbits and celestial positions depend so heavily.Their greatchain of knowledge anddreams led to the sophisticated sciences of today. The Astronomical Almanac,drawing from the works of these great scientists,provides ayearlysynthesisof the celestial kinematicsand dynamics needed for today'sprecise astronomy and related sciences.

TheAstronomical Almanac isa joint publication of the United StatesNautical Almanac Office (USNAO)and HerMajesty's Nautical Almanac Ofice (HMNAO).First published in1767asTheAstronomical EphemerisandNautical AlmanacbytheUK,theycontinued topublish it as The Astronomical Ephemerisuntil 1981.TheU.S.began publishing the American EphemerisandNautical Almanacin1852for the year1855.In1912the U.S.and UK began their long and successful collaboration to share production of the data.In 1981 the two countries combined the two books into one edition—The Astronomical Almanac. TheNautical Almanac became a separate publication in the UK and U.S.in 1915 and 1916,respectively.Thiscollaboration between the two offices preceded the formation of theIntermational Astronomical Union (IAU),which was established in 1921 to encourage communication, cooperation,and standards in astronomy.

The almanac offices of France,Germany,andRussia,inaddition to the U.S.and UK, first met in 1896 to discuss cooperation and began sharing the work between them to avoid duplication of effort and minimize overall costs.This led eventually to many countries using The Astronomical Almanac and to sharing of data for other publications between the offices.

The Astronomical Almanac serves a diverse group of users:astronomers,other scientists, lawyers,surveyors,navigators,themilitary,government agencies,historians,teachers,the generalpublic,calendarmakers,and manyothersaround theworld.Thebookishighly leveraged; i.e.,one book may serve a wide audience through a central resource such as a library or observatory.Itisa worldwide standard for its data.

TheAstronomical Almanac presents a variety of data, each data type appropriate to the celestial object.Most of the data are positional;i.e.,coordinates of the various objects. Also included are photometric and rotational data,timescales,astronomical standards,and observatory information.The selected catalog data list the positions for the mid-year of publication. Sun and most planet coordinates are with respect to the mean equator and ecliptic of date.Theastrometric coordinates (α,δ) for Pluto and the minor planets use the mean equator and equinox of J2ooo.0. Rectangular coordinates and osculating elements are also given.Some data (Sun,Moon,major planets,planetary satelites) list apparent places $( \alpha , \delta )$ as tabulated ephemerides;i.e.,the apparent place versus time—usually for each day of the year at $0 ^ { \mathrm { h } }$ TT.In many cases additional data (e.g.，physical properties） accompany each entry.

TheAstronomical Almanac followsaspecific structure.The book has several independent sections,each section addressinga different scientific area. Traditionally either the U.S. orUKhas technical responsibility for an entire section.The almanac ofces provide the information inthe book’s first section—Phenomena—a yearearlier than the restasabooklet, Astronomical Phenomena.

The book contains some useful,often-overlooked sections.The Notes and References Sectionat the back provides an overview and description of the theories and data.Errata appear in the next edition.Some information appears regularly and changes onlywhen warranted;e.g.,the section that lists the coordinates of observatories around the world.

Observatories can request addition to this listby writing to thealmanac offices.Thesection on Tables and Data lists the astronomical constants used by the almanac offices to produce the data aswell as other useful information.

Each country provides its data which are collected at the USNAO.Although the book is a joint publication of the UKHydrographic Office(UKHO)inthe UK and the U.S.Govermment Printing Offce(GPO),it is printed solelyat GPO; it is available forsale bothat UKHO,GPO and other booksellers.The GPO provides copies to Depository Libraries around the United States.The data from the U.S.are in the public domain;the data from HMNAO are under copyright.The Preface of each edition contains detailsregarding the copyright information.

# 1.1.3TheAstronomical Almanacand The Explanatory Supplement

Asa guide to the various chapters inthis book,use the sections in The Astronomical Almanac itself as a guide.

Phenomena．See Chapters11,12,and15 for information on this section.   
Time Scales and Coordinate Systems.See Chapter3 for information on time.See Chapters 4,5,6,and7for information on reference systems and positional astronomy.   
Sun.See Chapters 8 and 1O for information on this section.   
Moon.See Chapters8 and 1O for information on this section.   
Major Planets.See Chapters 8 and 1O for information on this section.   
Satellites of the Planets.See Chapter9 for information on this section.   
Minor Planetsand Comets.See Chapter1O for information on this section.   
Stars and Stellar Systems.See Chapter13 for information on this section.   
Tables and Data．See Chapters 1,6,and Appendix A for information on this section.   
Notesand References.This book gives the detailsupon which the section is based.

# 1.1.4 Conceptual Changes since the Last Edition

There have been a number of major changes since the 1992 edition of The Explanatory Supplement.The International Celestial Reference System (ICRS) hasreplaced theFK5 reference system.New precession and nutation theories have beenadopted.New timescales and coordinate transformations have been introduced.Earth Orientation methods have been improved.

Increasesinaccuracy,and the theories requiredby theincreased accuracies,have driven mostof thesechanges.For example,VeryLong Baseline Interferometers(VLBI) have achieved sub-milliarcsecond accuracies forobservations of extragalactic radio sources.These observations have been used to define a conceptually new reference system. Space astrometry led to milliarcsecond (mas) optical observations of stars brighter than ninth magnitude by the Hipparcos satelite.The Hipparcos and Tycho-2 Catalogues contain positions,proper motions,and parallaxes of mas or tens of mas accuracy. The Global Positioning System