<!-- source: IERS Conventions (2010), IERS Technical Note No.36.pdf -->

<!-- pdf_type: normal; pages: 179; chunk_pages: 70 -->


<!-- chunk 0001: pages 1-70 -->
# International Earth Rotation and Reference Systems Service (IERS) Service International de la Rotation Terrestre et des Syst\`emes de R´ef´erence

IERS Technical Note No. 36

# IERS Conventions (2010)

G´erard Petit1 and Brian Luzum2 (eds.)

IERS Conventions Centre

1 Bureau International des Poids et Mesures (BIPM)   
2 US Naval Observatory (USNO)

# Verlag des Bundesamts f¨ur Kartographie und Geod¨asie Frankfurt am Main 2010

# IERS Conventions (2010)

G´erard Petit and Brian Luzum (eds.)

(IERS Technical Note; No. 36)

Technical support: Beth Stetzler, Sabine Bachmann, and Wolfgang R. Dick

International Earth Rotation and Reference Systems Service   
Central Bureau   
Bundesamt f¨ur Kartographie und Geod¨asie   
Richard-Strauss-Allee 11   
60598 Frankfurt am Main   
Germany   
phone: ++49-69-6333-273/261/250   
fax: ++49-69-6333-425   
e-mail: central bureau@iers.org   
URL: www.iers.org

ISSN: 1019-4568 (print version)

# Table of Contents

# 0 Introduction 6

0.1 Models in the IERS Conventions 7   
0.1.1 Classification of models 7   
0.1.2 Criteria for choosing models . 7   
0.2 Differences between this document and IERS Technical Note 32 8   
0.3 Conventions Center . 14

# 1 General definitions and numerical standards 15

1.1 Permanent tide 15   
1.2 Numerical standards 16

# 2 Conventional celestial reference system and frame 21

# 2.1 The ICRS 21

2.1.1 Equator . 21   
2.1.2 Origin of right ascension 22   
2.2 The ICRF . 22   
2.2.1 Optical realization of the ICRF 23   
2.2.2 Availability of the frame . . 25

# 3 Conventional dynamical realization of the ICRS 28

# 4 Terrestrial reference systems and frames 31

# 4.1 Concepts and terminology . . 31

4.1.1 Basic concepts 31   
4.1.2 TRF in space geodesy 32   
4.1.3 Crust-based TRF 34   
4.1.4 The International Terrestrial Reference System 34   
4.1.5 Realizations of the ITRS 35

# 4.2 ITRF products 35

4.2.1 The IERS network 35   
4.2.2 History of ITRF products 36   
4.2.3 ITRF2005 . . 37   
4.2.4 ITRF2008, the current reference realization of the ITRS 39   
4.2.5 ITRF as a realization of the ITRS 39   
4.2.6 Transformation parameters between ITRF solutions 40

4.3 Access to the ITRS . 40

# 5 Transformation between the ITRS and the GCRS 43

5.1 Introduction 43

5.2 The framework of IAU 2000/2006 resolutions 43

5.2.1 IAU 2000 resolutions 44   
5.2.2 IAU 2006 resolutions 45

Implementation of IAU 2000 and IAU 2006 resolutions 45

5.3.1 The IAU 2000/2006 space-time reference systems 45   
5.3.2 Schematic representation of the motion of the Celestial Intermediate Pole (CIP) 45   
5.3.3 The IAU 2000/2006 realization of the Celestial Intermediate Pole (CIP) 46   
5.3.4 Procedures for terrestrial-to-celestial transformation consistent with IAU 2000/2006   
resolutions 47

5.4 Coordinate transformation consistent with the IAU 2000/2006 resolutions 47

5.4.1 Expression for the transformation matrix for polar motion 48   
5.4.2 Expression for the CIO based transformation matrix for Earth rotation . . . . 48   
5.4.3 Expression for the equinox based transformation matrix for Earth rotation . . 48   
5.4.4 Expression for the transformation matrix for the celestial motion of the CIP . 48   
5.4.5 Expression for the equinox-based transformation matrix for precession-nutation 49   
5.5 Parameters to be used in the transformation 49   
5.5.1 Motion of the Celestial Intermediate Pole in the ITRS 49   
5.5.2 Position of the Terrestrial Intermediate Origin in the ITRS 51   
5.5.3 Earth Rotation Angle 52   
5.5.4 Forced motion of the Celestial Intermediate Pole in the GCRS 54   
5.5.5 Free Core Nutation . 57   
5.5.6 Position of the Celestial Intermediate Origin in the GCRS 59   
5.5.7 ERA based expressions for Greenwich Sidereal Time 59   
5.6 Description of the IAU 2000/2006 precession-nutation model 61   
5.6.1 The IAU 2000A and IAU 2000B nutation model 61   
5.6.2 Description of the IAU 2006 precession 63   
5.6.3 IAU 2006 adjustments to the IAU 2000A nutation 64   
5.6.4 Precession developments compatible with the IAU 2000/2006 model 64   
5.6.5 Summary of different ways of implementing IAU 2006/2000A precession-nutation 65   
5.7 The fundamental arguments of nutation theory . 66   
5.7.1 The multipliers of the fundamental arguments of nutation theory 66   
5.7.2 Development of the arguments of lunisolar nutation 66   
5.7.3 Development of the arguments for the planetary nutation 67   
5.8 Prograde and retrograde nutation amplitudes 68   
5.9 Algorithms for transformations between ITRS and GCRS 69   
5.10 Notes on the new procedure to transform from ICRS to ITRS 71

# 6 Geopotential 79

6.1 Conventional model based on the EGM2008 model 79

6.2 Effect of solid Earth tides 81   
6.2.1 Conventional model for the solid Earth tides 81   
6.2.2 Treatment of the permanent tide 88   
6.3 Effect of the ocean tides . 89   
6.3.1 Background on ocean tide models 90   
6.3.2 Ocean tide models 91   
6.4 Solid Earth pole tide 93   
6.5 Ocean pole tide 94   
6.6 Conversion of tidal amplitudes defined according to different conventions . 96

# 7 Displacement of reference points 99

7.1 Models for conventional displacement of reference markers on the crust . . 99

7.1.1 Effects of the solid Earth tides 99   
7.1.2 Local site displacement due to ocean loading 108   
7.1.3 S1-S $^ 2$ atmospheric pressure loading . . 112   
7.1.4 Rotational deformation due to polar motion 114   
7.1.5 Ocean pole tide loading . . 116

7.2 Models for other non-conventional displacement of reference markers on the crust . . . 11

7.3 Models for the displacement of reference points of instruments 118   
7.3.1 Models common to several techniques 118   
7.3.2 Very long baseline interferometry . 119   
7.3.3 Global navigation satellite systems 119

# 8 Tidal variations in the Earth’s rotation 123

8.1 Effect of the tidal deformation (zonal tides) on Earth’s rotation 123   
8.2 Diurnal and semi-diurnal variations due to ocean tides . 124   
8.3 Tidal variations in polar motion & polar motion excitation due to long period ocean tides124

# 9 Models for atmospheric propagation delays 132

# 9.1 Tropospheric model for optical techniques . . 132

9.1.1 Zenith delay models 132   
9.1.2 Mapping function 133   
9.1.3 Future developments 134   
9.2 Tropospheric model for radio techniques 135   
9.3 Sources for meteorological data 136   
9.4 Ionospheric model for radio techniques 137   
9.4.1 Ionospheric delay dependence on radio signals including higher order terms . . 137   
9.4.2 Correcting the ionospheric effects on code and phase 142

# 10 General relativistic models for space-time coordinates and equations of motion 151

10.1 Time coordinates . 151   
10.2 Transformation between proper time and coordinate time in the vicinity of the Earth . 153   
10.3 Equations of motion for an artificial Earth satellite . 155   
10.4 Equations of motion in the barycentric frame . . 156

# 11 General relativistic models for propagation 159

.1 VLBI time delay

11.1.1 Historical background 159   
11.1.2 Specifications and domain of application . 159   
11.1.3 The analysis of VLBI measurements: definitions and interpretation of results . 160   
11.1.4 The VLBI delay model . 160   
11.2 Ranging techniques . . 164

# A IAU NFA WG Recommendations 166

# B IAU Resolutions Adopted at the XXVIth General Assembly (2006)

B.1 IAU 2006 Resolution B1 on Adoption of the P03 Precession Theory & Definition of the Ecliptic 168 B.2 IAU 2006 Resolution B2 on Supplement to IAU 2000 Resolutions on reference systems 168 B.3 IAU 2006 Resolution B3 on the Re-definition of Barycentric Dynamical Time, TDB . 170

C IUGG Resolution 2 Adopted at the XXIVth General Assembly (2007)

D.1 IAU 2009 Resolution B2 on IAU 2009 astronomical constants 172   
D.2 IAU 2009 Resolution B3 on Second Realization of International Celestial Reference Frame172

This document is intended to define the standard reference systems realized by the International Earth Rotation and Reference Systems Service (IERS) and the models and procedures used for this purpose. It is a continuation of the series of documents begun with the Project MERIT (Monitor Earth Rotation and Intercompare the Techniques) Standards (Melbourne et al., 1983) and continued with the IERS Standards (McCarthy, 1989; McCarthy, 1992) and IERS Conventions (McCarthy, 1996; McCarthy and Petit, 2004). The current issue of the IERS Conventions is called the IERS Conventions (2010).

The reference systems and procedures of the IERS are based on the resolutions of international scientific unions. The celestial system is based on IAU (International Astronomical Union) Resolution A4 (1991). It was officially initiated and named International Celestial Reference System (ICRS) by IAU Resolution B2 (1997) and its definition was further refined by IAU Resolution B1 (2000) and by IAU Resolution B3 (2009). The terrestrial system is based on IUGG (International Union of Geodesy and Geophysics) Resolution 2 (1991). It was officially endorsed as the International Terrestrial Reference System (ITRS) by IUGG Resolution 2 (2007). The transformation between celestial and terrestrial systems is based on IAU Resolution B1 (2000) and was complemented by IAU Resolutions B1 and B2 (2006). The definition of time coordinates and time transformations, the models for light propagation and the motion of massive bodies are based on IAU Resolution A4 (1991), further refined by IAU Resolution B1 (2000) and IAU Resolution B3 (2006). In some cases, the procedures used by the IERS, and the resulting conventional frames produced by the IERS, do not completely follow these resolutions. These cases are identified in this document and procedures to obtain results consistent with the resolutions are indicated. Following IAU resolutions, the IERS reference systems are defined in the framework of the General Relativity Theory (GRT). In a few cases, models are expressed in the parameterized post-Newtonian (PPN) formalism using parameters $\beta$ and $\gamma$ (equal to 1 in GRT). These cases are identified with a note.

The units of length, mass, and time are in the International System of Units (Le Syst\`eme International d’Unit´es (SI), 2006) as expressed by the meter (m), kilogram (kg) and second (s). The astronomical unit of time is the day containing 86400 SI seconds. The Julian century contains 36525 days and is represented by the symbol c. When possible, the notations in this document have been made consistent with ISO Standard 80000 on quantities and units. The numerical standards in Table 1.1 have been revised in order to conform to the new IAU (2009) System of Astronomical Constants adopted with IAU Resolution B2 (2009; cf. Appendix D.1).

The basis for this edition was set at an IERS Workshop on Conventions, held on September 20-21 2007 at the Bureau International des Poids et Mesures in S\`evres (France). This document and the associated information (e.g. software) essentially follow the recommendations specified in the executive summary of the workshop ${ < } ^ { 1 } >$ . All electronic files associated with the IERS Conventions (2010) may be found on identical web pages maintained at the BIPM 2 (this pages will be referenced in this document) and at the USNO 3. The recommended models, procedures and constants used by the IERS follow the research developments and the recommendations of international scientific unions. When needed, updates to this edition of the Conventions will be available electronically at the IERS Conventions Center website ${ < } ^ { 4 } >$ . The principal changes between this edition and the IERS Conventions (2003) are listed in Section 0.2 below.

# 0.1 Models in the IERS Conventions

This section provides guidelines and criteria for models included in the IERS Conventions and for their usage in generating IERS reference products. All of the contributions used for generating IERS reference products should be consistent with the description in this document. If contributors to the IERS do not fully comply with these guidelines, they should carefully identify the exceptions. In these cases, the contributor provides an assessment of the effects of the departures from the conventions so that his/her results can be referred to the IERS Reference Systems. Contributors may use models equivalent to those specified herein if they assess the equivalence.

# 0.1.1 Classification of models

Models to represent physical effects can be classified into three categories:

Class 1 (“reduction”) models are those recommended to be used a priori in the reduction of raw space geodetic data in order to determine geodetic parameter estimates, the results of which are then subject to further combination and geophysical analysis. The Class 1 models are accepted as known a priori and are not adjusted in the data analysis. Therefore their accuracy is expected to be at least as good as the geodetic data (1 mm or better). Class 1 models are usually derived from geophysical theories. Apart from a few rare exceptions, the models and their numerical constants should be based on developments that are fully independent of the geodetic analyses and results that depend on them. Whenever possible, they should preferably be in closed-form expressions for ease of use, and their implementation should be flexible enough to allow testing alternate realizations, if needed. A good example is the solid Earth tide model for station displacements (see Chapter 7).

Class 2 (“conventional”) models are those that eliminate an observational singularity and are purely conventional in nature. This includes many of the physical constants. Other examples are the ITRF rotational datum, specifying the rotation origin and the rotation rate of the ITRF (see Chapter 4). As indicated by their name, Class 2 models may be purely conventional or the convention may be to realize a physical condition. When needed, choices among possible conventions are guided by Union resolutions and historic practice, which may differ in some cases.

Class 3 (“useful”) models are those that are not required as either Class 1 or 2. This includes, for instance, the zonal tidal variations of UT1/LOD (see Chapter 8), as an accurate zonal tide model is not absolutely required in data analysis though it can be helpful and is very often used internally in a remove/restore approach. In addition, such a model is very much needed to interpret geodetic LOD results in comparisons with geophysical excitation processes, for instance. Class 3 also includes models which cannot (yet) fulfill the requirements for Class 1 such as accuracy or independence of geodetic results, but are useful or necessary to study the physical processes involved.

In the external exchange of geodetic results for the generation of IERS products, all Class 1 effects and specified Class 2 effects should be included, i.e. the models should be removed from the observational estimates. On the other hand, Class 3 effects should never be included in generating such results.

As much as possible, the documentation of the software provided by the IERS Conventions Center indicates the class associated with the model.

# 0.1.2 Criteria for choosing models

The IERS Conventions intend to present a complete and consistent set of the necessary models of the Class 1 and Class 2 types, including implemented software. Where conventional choices must be made (Class 2), the Conventions provide a unique set of selections to avoid ambiguities among users. The resolutions of the international scientific unions and historical geodetic practice provide guidance when equally valid choices are available. Class 3 models are included when their use is likely to be sufficiently common, as a guidance to users.

For station displacement contributions (Chapter 7), the Conventions clearly distinguish models which are to be used in the generation of the official IERS products from other (Class 3) models. Models in the first category, used to generate the IERS realization of the celestial and terrestrial reference systems and of the transformation between them, are referred to as “conventional displacement contributions.” Conventional displacement contributions include Class 1 models (essential and geophysically based) that cover the complete range of daily and sub-daily variations, including all tidal effects, and other accurately modeled effects (mostly at longer periods). They relate the regularized positions of reference markers on the crust to their conventional instantaneous positions (see Chapter 4) and are described in Section 7.1. In addition, models for technique-specific effects, described in Section 7.3, relate the positions of reference markers to the reference points of instruments.

# 0.2 Differences between this document and IERS Technical Note 32

The structure of the IERS Conventions (2003) has been retained in this document, but the titles of some chapters have been changed, as indicated. Authors and major contributors of the previous (2003) version of the chapters may be found in the introduction to the Conventions (2003). The most significant changes from the previous version are outlined below for each chapter, along with the major contributors to the changes. These changes are also indicated in two tables that present the realization of reference frames and their accuracy estimates (Table 0.1) and the models along with estimates of the magnitude of the effects (Table 0.2).

The IERS Conventions are one of the products of the IERS Conventions Center. However, this volume would not be possible without the contributions acknowledged below for each chapter. In addition, we would also like to acknowledge the work of the Advisory Board for the IERS Conventions update, that was set up in 2005 under the chairmanship of Jim Ray to advise the Conventions Center in its work of updating the Conventions, with members representing all components of the IERS. Among those, special thanks are due to Ralf Schmid for providing detailed comments and corrections to nearly all chapters in this volume.

Table 0.1: Estimates of accuracy of reference frames   

<table><tr><td rowspan=1 colspan=1>Ch.</td><td rowspan=1 colspan=1>Reference frame</td><td rowspan=1 colspan=1>Conventions2003</td><td rowspan=1 colspan=1>Conventions2010</td><td rowspan=1 colspan=1>Accuracy &amp; difference/improvement between Con-ventions</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>celestial referencesystem &amp; frame</td><td rowspan=1 colspan=1>ICRF-Ext.1</td><td rowspan=1 colspan=1>ICRF-2</td><td rowspan=1 colspan=1>Noise floor ≈ 40 μas (5 times better than ICRF-Ext.1).Axis stability ≈ 10 μas (twice as stable asICRF-Ext.1).From 717 to 3414 total objects； from212 to 295“defining”sources</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>dynamical realiza-tion of ICRS</td><td rowspan=1 colspan=1>DE405</td><td rowspan=1 colspan=1>DE421</td><td rowspan=1 colspan=1>From 1 mas to 0.25 mas for alignment to ICRF</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>terrestrial refer-encesystem&amp;frame</td><td rowspan=1 colspan=1>ITRF2000</td><td rowspan=1 colspan=1>ITRF2008</td><td rowspan=1 colspan=1>Accuracy over 1985-2008:1cm in origin，1.2 ppbin scale. Most important systematic difference vs.ITRF2000: drift in z-direction by 1.8 mm/yr.</td></tr></table>

Table 0.2: Models of the Conventions (2010): some information on the magnitude of effects and changes vs. Conventions (2003). Sec. indicates the section number in this document; Cl. stands for Class (see section 0.1.1).   

<table><tr><td colspan="1" rowspan="1">Sec.</td><td colspan="1" rowspan="1">Cl.</td><td colspan="1" rowspan="1">Phenomenon</td><td colspan="1" rowspan="1">Amplitude ofeffect</td><td colspan="1" rowspan="1">Conventions 2003</td><td colspan="1" rowspan="1">Conventions 2010</td><td colspan="1" rowspan="1">Accuracy &amp;difference/improvementbetween Conventions</td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="5" rowspan="1">Transformation between the ITRS and GCRS</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">5.5.1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">libration inpolar motion</td><td colspan="1" rowspan="1">tens of μas</td><td colspan="1" rowspan="1">No specificroutine</td><td colspan="1" rowspan="1">BrzezinskiPMSDNUT2model</td><td colspan="1" rowspan="1">Specific routine</td></tr><tr><td colspan="1" rowspan="1">5.5.3</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">libration inthe axialcomponent ofrotation</td><td colspan="1" rowspan="1"> several μs in UT1</td><td colspan="1" rowspan="1">Not available</td><td colspan="1" rowspan="1">Brzezinski &amp;Capitaine (2003)UTLIBR model</td><td colspan="1" rowspan="1">New model</td></tr><tr><td colspan="1" rowspan="1">5.5.4</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">precession-nutation ofthe CIP</td><td colspan="1" rowspan="1">tens of as/yr andtens of as for theperiodic part inX and Y</td><td colspan="1" rowspan="1">IAU2000 PN</td><td colspan="1" rowspan="1">IAU2006/2000PN</td><td colspan="1" rowspan="1">100 μas/c. + 7 mas/c.2in X; 500 μas/c. in Y</td></tr><tr><td colspan="1" rowspan="1">5.5.5</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">FCN</td><td colspan="1" rowspan="1">Few hundred μas</td><td colspan="1" rowspan="1">not available</td><td colspan="1" rowspan="1">Lambert model</td><td colspan="1" rowspan="1">Accuracy: 50 μas rms,100 μas at one yearextrapolation</td></tr><tr><td colspan="1" rowspan="1">5.5.6</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1"> space motionof the CIO</td><td colspan="1" rowspan="1">mas/c.</td><td colspan="1" rowspan="1">IAU2000 PN</td><td colspan="1" rowspan="1">IAU2006/2000PN</td><td colspan="1" rowspan="1">no change larger than 1μas after one century</td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="5" rowspan="1">Geopotential</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">6.1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Global geopotentialmodel</td><td colspan="1" rowspan="1">10-³ of centralpotential</td><td colspan="1" rowspan="1">EGM96</td><td colspan="1" rowspan="1">EGM2008; C20and rates of lowdegree coefs fromother sources</td><td colspan="1" rowspan="1">EGM96: degree andorder 360;EGM2008:complete to degree andorder 2159; rate termsfor low degree coefs.</td></tr><tr><td colspan="1" rowspan="1">6.2</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Solid Earthtides</td><td colspan="1" rowspan="1">10-8 on C2m,10-12on C3m,C4m</td><td colspan="1" rowspan="1">Eanes et al.,1983; Mathews etal., 2002</td><td colspan="1" rowspan="1">Unchanged</td><td colspan="1" rowspan="1">No change</td></tr><tr><td colspan="1" rowspan="1">6.3</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Ocean tides</td><td colspan="1" rowspan="1">For LEO orbitintegration:decimetric over 1day</td><td colspan="1" rowspan="1">CSR 3.0</td><td colspan="1" rowspan="1">FES2004;Treatment ofsecondary wavesspecified</td><td colspan="1" rowspan="1">Effect of new model forLEO /MEO: few mmover several daysintegration; Treatmentof secondary waves forLEO: 20% of totaleffect</td></tr><tr><td colspan="7" rowspan="1">continued on next page</td></tr><tr><td colspan="7" rowspan="1">continued from previous page</td></tr><tr><td colspan="1" rowspan="1">6.4</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Solid Earthpole tide</td><td colspan="1" rowspan="1">10-9 on C21,S21</td><td colspan="1" rowspan="1">Centrifugal effectvs.conventionalmean pole (2003)</td><td colspan="1" rowspan="1">Centrifugal effectvs. conventionalmean pole (2010)</td><td colspan="1" rowspan="1">Change of conventionalmean pole: effect of afew 10-11 on C21, S21</td></tr><tr><td colspan="1" rowspan="1">6.5</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1"> Ocean poletide</td><td colspan="1" rowspan="1">Few 10-11 on lowdegree coefs</td><td colspan="1" rowspan="1">Not available</td><td colspan="1" rowspan="1">Desai (2002)</td><td colspan="1" rowspan="1">New model</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="5" rowspan="1">Displacement of reference points</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">7.1.1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Solid Earthtides</td><td colspan="1" rowspan="1">decimetric</td><td colspan="1" rowspan="1">Conventionalroutine fromDehant &amp;Mathews</td><td colspan="1" rowspan="1">Unchanged</td><td colspan="1" rowspan="1">No change</td></tr><tr><td colspan="1" rowspan="1">7.1.2</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1"> Ocean loading</td><td colspan="1" rowspan="1">centimetric</td><td colspan="1" rowspan="1">Loading responsefrom Scherneck(several tidemodels); noconventionalimplementation.</td><td colspan="1" rowspan="1">Loading responsefrom Scherneck(several tidemodels);Implementationby Agnewsoftware (342constituent tides)</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">7.1.3</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">S1-S2Atmosphericpressureloading</td><td colspan="1" rowspan="1">millimetric</td><td colspan="1" rowspan="1">not available</td><td colspan="1" rowspan="1">Implementationof Ray &amp; Ponte(2003)byvanDam</td><td colspan="1" rowspan="1">New model</td></tr><tr><td colspan="1" rowspan="1">7.1.4</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Conventionalmean pole</td><td colspan="1" rowspan="1">Hundreds of mas</td><td colspan="1" rowspan="1">linear model</td><td colspan="1" rowspan="1">cubic model from1976.0 until2010.0; linearmodel after2010.0</td><td colspan="1" rowspan="1">tens of mas.</td></tr><tr><td colspan="1" rowspan="1">7.1.4</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Pole tide</td><td colspan="1" rowspan="1">2 cm radial, fewmm tangential</td><td colspan="1" rowspan="1">Centrifugal effectvs. conventionalmean pole (2003)</td><td colspan="1" rowspan="1">Centrifugal effectvs. conventionalmean pole (2010)</td><td colspan="1" rowspan="1">Change of conventionalpole: effect may reach1mm</td></tr><tr><td colspan="1" rowspan="1">7.1.5</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Ocean poletide loading</td><td colspan="1" rowspan="1">2 mm radial,&lt;1 mm tangential</td><td colspan="1" rowspan="1">Not available</td><td colspan="1" rowspan="1">Desai (2002)</td><td colspan="1" rowspan="1">New model</td></tr><tr><td colspan="1" rowspan="1">7.3.1</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">Referencepoints ofinstruments:effect oftemperatureand pressure</td><td colspan="1" rowspan="1">~1mm</td><td colspan="1" rowspan="1">Not specified</td><td colspan="1" rowspan="1">Referencetemperature andpressure: GPTmodel, Boehm etal. (2007)</td><td colspan="1" rowspan="1">Between using averagein situ temperaturemeasurements andGPT:&lt; 0.5 mm siteheight change due toantenna thermaldeformation</td></tr><tr><td colspan="1" rowspan="1">7.3.2</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Thermaldeformation ofVLBI antenna</td><td colspan="1" rowspan="1">&gt; 10 ps on VLBIdelay, severalmm variation incoordinates</td><td colspan="1" rowspan="1">Nothnagel et al.(1995)</td><td colspan="1" rowspan="1">Nothnagel (2009)</td><td colspan="1" rowspan="1">Reference temperaturesdefined according toGPT model; reduction in annual scalevariations of about1mm</td></tr><tr><td colspan="1" rowspan="1">7.3.3</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">GNSS antennaphase centeroffsets andvariations</td><td colspan="1" rowspan="1">decimetric</td><td colspan="1" rowspan="1">Not specified</td><td colspan="1" rowspan="1">Schmid et al.(2007)</td><td colspan="1" rowspan="1">10-9 on scale;tropospheric zenithdelay and GPS orbitconsistency improved</td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="5" rowspan="1">Tidal variations in the Earth's rotation</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">8.1</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">Zonal tides onUT1</td><td colspan="1" rowspan="1">785 μs at Mf</td><td colspan="1" rowspan="1">Defraigne andSmits (1999) 62terms</td><td colspan="1" rowspan="1">Combination ofYoder et al.(1981) elasticbody tide, Wahrand Bergen(1986) inelasticbody tide,andKantha et al.(1998) ocean tidemodels</td><td colspan="1" rowspan="1">6 μs at Mf</td></tr><tr><td colspan="1" rowspan="1">8.2</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Subdaily tides</td><td colspan="1" rowspan="1">~ 0.5 μas for PM~ 0.05 ms forUT1</td><td colspan="1" rowspan="1">Ray et al.(1994)；conventionalimplementationby Eanes</td><td colspan="1" rowspan="1">No change</td><td colspan="1" rowspan="1">No change</td></tr><tr><td colspan="1" rowspan="1">8.3</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">long-periodtides, polarmotion</td><td colspan="1" rowspan="1">(pro- grade,retrograde)polar motionamplitude of (66,74) μas at Mf</td><td colspan="1" rowspan="1">Not available</td><td colspan="1" rowspan="1">Dickman andNam (1995),Dickman andGross (2009)</td><td colspan="1" rowspan="1">(prograde, retrograde)polar motion amplitudeof (66,74) μas at Mf</td></tr><tr><td colspan="1" rowspan="1">9</td><td colspan="5" rowspan="1"> Models for atmospheric propagation delays</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">9.1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Troposphere;optical</td><td colspan="1" rowspan="1">~ 2.2m at zenithto ~ 14m at 10°above horizon</td><td colspan="1" rowspan="1">Marini andMurray (1973)</td><td colspan="1" rowspan="1">Mendes andPavlis (2004)zenith delay;Mendes andPavlis (2003)"Fcul” mappingfunction (MF)</td><td colspan="1" rowspan="1">more accurate delaysbelow 20° elevation andall the way to 3° abovehorizon; accurate to ~7 mm (Total error due to ZTD and MF)</td></tr><tr><td colspan="1" rowspan="1">9.2</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Troposphere;radio</td><td colspan="1" rowspan="1">Hydrostaticzenith delays ~2.3 m Wet zenithdelays typically~ 10-150mm</td><td colspan="1" rowspan="1">Several MFe.g. Neill (1996)or Lanyi (1984)</td><td colspan="1" rowspan="1">MF: VMF1based on 6-hourECMWF data.GMF based only on latitude, siteheight, time ofyear (Boehm etal., 2006)</td><td colspan="1" rowspan="1">Both VMF1 and GMFremovelatitude-dependentmapping function bias(average ~ 4mm in siteheight).VMF1 reducesshort-term verticalscatter (average ~4-5mm)</td></tr><tr><td colspan="7" rowspan="1">continued on next page</td></tr><tr><td colspan="1" rowspan="1">9.2</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Troposphere;horizontal gradients</td><td colspan="1" rowspan="1">can lead tosystematic errorsin the scale ofestimated TRFat level of ~ 1ppb</td><td colspan="1" rowspan="1">Not available</td><td colspan="1" rowspan="1">J. Boehm APG apriori model</td><td colspan="1" rowspan="1">New model</td></tr><tr><td colspan="1" rowspan="1">9.4</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Ionosphere;radio: Firstorder term</td><td colspan="1" rowspan="1">can reach 100 nsfor GPS</td><td colspan="1" rowspan="1">Not available</td><td colspan="1" rowspan="1">Sources forVertical TEC +conventionalmapping function</td><td colspan="1" rowspan="1">New model</td></tr><tr><td colspan="1" rowspan="1">9.4</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Ionosphere;radio: Higher order termsfordual-frequency</td><td colspan="1" rowspan="1">can reach 100 psfor GPS; a few psfor wide-bandVLBI</td><td colspan="1" rowspan="1">Not available</td><td colspan="1" rowspan="1">Conventionalmodel based onSlant TEC +Magnetic fieldmodel</td><td colspan="1" rowspan="1">New model</td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="6" rowspan="1">General relativistic models for spacetime coordinates and equations of motion</td></tr><tr><td colspan="1" rowspan="1">10.1</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">Timecoordinates</td><td colspan="1" rowspan="1">TCB, TDB inbarycentric;TCG, TT ingeocentric</td><td colspan="1" rowspan="1">IAU1991-IAU2000</td><td colspan="1" rowspan="1">IAU1991-IAU2000;IAU2006 TDBdefinition</td><td colspan="1" rowspan="1">New TDB definition</td></tr><tr><td colspan="1" rowspan="1">10.1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">TCB-TCGtransforma-tion</td><td colspan="1" rowspan="1">1.5 ms annual; 2 μs diurnal onEarth</td><td colspan="1" rowspan="1">FB2001; TE405;HF2002</td><td colspan="1" rowspan="1">HF2002_IERS</td><td colspan="1" rowspan="1">HF2002_IERS vs.HF2002: 1.15 × 10-16in rate;</td></tr><tr><td colspan="1" rowspan="1">10.2</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">transforma-tion between proper timeandcoordinatetime nearEarth</td><td colspan="1" rowspan="1">GNSS: frequencyshift of~4-5×10-10 +periodic term ofseveral tens of ns</td><td colspan="1" rowspan="1">Not specified</td><td colspan="1" rowspan="1">ConventionalGNSS modelspecified;Information onnext mostsignificant term.</td><td colspan="1" rowspan="1">New model</td></tr><tr><td colspan="1" rowspan="1">11</td><td colspan="5" rowspan="1">General relativistic models for propagation</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">11.1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">VLBI delay</td><td colspan="1" rowspan="1">tens of ms</td><td colspan="1" rowspan="1">conventional‘consensus'model</td><td colspan="1" rowspan="1">no change</td><td colspan="1" rowspan="1">Uncertainty of model:1ps</td></tr><tr><td colspan="1" rowspan="1">11.2</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">time ofpropagationfor rangingtechniques</td><td colspan="1" rowspan="1">up to a few s</td><td colspan="1" rowspan="1">conventionalmodel</td><td colspan="1" rowspan="1"> no change</td><td colspan="1" rowspan="1">Uncertainty of model:3ps</td></tr></table>

# Chapter 1: General definitions and numerical standards

The section “Numerical standards” has been re-written and the list of constants ensures consistency with the IAU (2009) system of astronomical constants. It is derived mostly from the work of the IAU Working Group on Numerical Standards of Fundamental Astronomy, headed by B. Luzum.

# Chapter 2: Conventional celestial reference system and frame

This chapter has been rewritten to present the second realization of the ICRF, following the work of the IAU working group with the same name, headed by C. Ma. The primary contributors are E. F. Arias, S. Bouquillon, A. Fey, G. Francou and N. Zacharias.

# Chapter 3: Conventional dynamical realization of the ICRS

The chapter has been re-written (with W. M. Folkner as the primary contributor) and provides information on recently released ephemerides. When a conventional choice is needed, DE421 is recommended to provide continuity for implementation by users.

# Chapter 4: Terrestrial reference systems and frames

The chapter (with a new title) has been significantly rewritten with Z. Altamimi and C. Boucher as the primary authors. It incorporates the new realization ITRF2008, which was introduced in 2010.

# Chapter 5: Transformation between the International Terrestrial Reference System and Geocentric Celestial Reference System

The chapter (with a new title) has been significantly rewritten, with N. Capitaine and P. Wallace as the primary authors, in order to make the chapter compliant with the IAU 2000/2006 resolutions and the corresponding terminology. A presentation of the IAU 2006 resolutions has been added, and a description of the models, procedures and software to implement the IAU 2000/2006 resolutions has been included. The organization of the chapter has been modified in order to clarify the successive steps to be followed in the coordinate transformation. Additional contributors include A. Brzezi´nski, G. Kaplan and S. Lambert.

# Chapter 6: Geopotential

A new conventional geopotential model based on EGM2008 is presented. The section on ocean tides has been rewritten and a new section describes the oceanic pole tide. The primary contributors are S. Bettadpur, R. Biancale, J. Chen, S. Desai, F. Flechtner, F. Lemoine, N. Pavlis, J. Ray and J. Ries.

# Chapter 7: Displacement of reference points

A new conventional mean pole model, to be referenced as the IERS (2010) mean pole model, is given consistently with Chapter 6. The section on ocean loading has been rewritten and new sections describe the oceanic pole tide loading and the S1-S2 atmospheric loading. The section “Models for the displacement of reference points of instruments” has been updated: It contains models for a reference temperature, the thermal expansion of VLBI antennas and GNSS antenna phase center offsets and variations. The primary contributors are D. Agnew, J. Boehm, M. Bos, T. van Dam, S. Desai, D. Gambis, A. Nothnagel, G. Petit, J. Ray, H.-G. Scherneck, R. Schmid, and J. Wahr.

# Chapter 8: Tidal variations in the Earth’s rotation

The model to evaluate the effects of zonal Earth tides on the Earth’s rotation has been updated, with software included, and a model to evaluate tidal variations in polar motion and polar motion excitation due to long period ocean tides has been added. The primary contributors are C. Bizouard and R. Gross.

# Chapter 9: Models for atmospheric propagation delays

This chapter (with a new title) has been completely rewritten. The models for tropospheric delay have been updated and a new section “Ionospheric models for radio techniques” has been added. The primary contributors are J. Boehm, M. Hern´andez Pajares, U. Hugentobler, G. Hulley, F. Mercier, A. Niell, and E. Pavlis.

# Chapter 10: General relativistic models for space-time coordinates and equations of motion

The chapter has been updated following IAU Resolution B3 (2006) and the new description of the relations between time scales. A new section “Transformation between proper time and coordinate time in the vicinity of the Earth” and numerical examples have been added. The primary contributors are U. Hugentobler, J. Kouba, S. Klioner, R. Nelson, G. Petit, J. Ray, and J. Ries.

# Chapter 11: General relativistic models for propagation

The chapter has been updated for minor wording corrections.

# 0.3 Conventions Center

At the time of this edition, the IERS Conventions Center is composed of E. F. Arias, B. Luzum, D. D. McCarthy, G. Petit and B. E. Stetzler. P. Wolf has also contributed over past years.

# References

Le Syst\`eme International d’Unit´es (SI), $8 ^ { t h }$ edition, 2006, Bureau International des Poids et Mesures, S\`evres, France, http://www.bipm.org/en/si/si brochure/   
McCarthy, D. D. (ed.), 1989, IERS Standards (1989), IERS Technical Note 3, Observatoire de Paris, Paris, available at http://www.iers.org/TN03   
McCarthy, D. D. (ed.), 1992, IERS Standards (1992), IERS Technical Note 13, Observatoire de Paris, Paris, available at http://www.iers.org/TN13   
McCarthy, D. D. (ed.), 1996, IERS Conventions (1996), IERS Technical Note 21, Observatoire de Paris, Paris, available at http://www.iers.org/TN21   
McCarthy, D. D., Petit, G. (eds.), 2004, IERS Conventions (2003), IERS Technical Note 32, BKG, Frankfurt am Main, available at http://www.iers.org/TN32   
Melbourne, W., Anderle, R., Feissel, M., King, R., McCarthy, D., Smith, D., Tapley, B., Vicente, R., 1983, Project MERIT Standards, U.S. Naval Observatory Circular No. 167.

# 1 General definitions and numerical standards

This chapter provides definitions for some topics that are relevant to several chapters of the document, such as the tide systems in Section 1.1 and the units of relativistic time scales and associated quantities in Section 1.2. The latter section also provides the values of numerical standards that are used in the document. Those are based on the most recent reports of the appropriate working groups of the International Association of Geodesy (IAG) and the International Astronomical Union (IAU) which can be found in the references below Table 1.1.

# 1.1 Permanent tide

Some geodetic parameters are affected by tidal variations. The gravitational potential in the vicinity of the Earth, which is directly accessible to observation, is a combination of the tidal gravitational potential of external bodies (the Moon, the Sun, and the planets) and the Earth’s own potential which is perturbed by the action of the tidal potential. The (external) tidal potential contains both time-independent (permanent) and time-dependent (periodic) parts, and so does the tide-induced part of the Earth’s own potential. Similarly, the observed site positions are affected by displacements associated with solid Earth deformations produced by the tidal potential; these displacements also include permanent and time-dependent parts. Removing the time-dependent part of the tidal contributions from the observed site positions/potential, the resulting station positions are on the “mean tide” (or simply “mean”) crust; and the potential which results is the “mean tide” potential. The permanent part of the deformation produced by the tidal potential is present in the mean crust; the associated permanent change in the geopotential, and also the permanent part of the tidal potential, are included in the mean tide geopotential. These correspond to the actual mean values, free of periodic variations due to tidal forces. The “mean tide” geoid, for example, would correspond to the mean ocean surface in the absence of nongravitational disturbances (currents, winds). In general, quantities referred to as “mean tide” (e.g. flattening, dynamical form factor, equatorial radius, etc.) are defined in relation to the mean tide crust or the mean tide geoid.

If the deformation due to the permanent part of the tidal potential is removed from the mean tide crust, the result is the “tide free” crust. Regarding the potential, removal of the permanent part of the external potential from the mean tide potential results in the “zero tide” potential which is strictly a geopotential. The permanent part of the deformation-related contribution is still present; if that is also removed, the result is the “tide free” geopotential. It is important to note that unlike the case of the potential, the term “zero tide” as applied to the crust is synonymous with “mean tide.”

In a “tide free” quantity, the total tidal effects have been removed with a model. Because the perturbing bodies are always present, a truly “tide free” quantity is unobservable. In this document, the tidal models used for the geopotential (Chapter 6) and for the displacement of points on the crust (Chapter 7) are based on nominal Love numbers; the reference geopotential model and the terrestrial reference frame, which are obtained by removal of tidal contributions using such models, are termed “conventional tide free.” Because the deformational response to the permanent part of the tide generating potential is characterized actually by the secular (or fluid limit) Love numbers (Munk and MacDonald, 1960; Lambeck, 1980), which differ substantially from the nominal ones, “conventional tide free” values of quantities do not correspond to truly tide free values that would be observed if tidal perturbations were absent. The true effect of the permanent tide could be estimated using the fluid limit Love numbers for this purpose, but this calculation is not included in this document because it is not needed for the tidal correction procedure.

Resolution 16 of the 18th General Assembly of the IAG (1984), “recognizing the need for the uniform treatment of tidal corrections to various geodetic quantities such as gravity and station positions,” recommended that “the indirect effect due to the permanent yielding of the Earth be not removed,” i.e. recommends the use of “zero-tide” values for quantities associated with the geopotential and “mean-tide” values for quantities associated with station displacements. This recommendation, however, has not been implemented in the algorithms used for tide modeling by the geodesy community in the analysis of space geodetic data in general. As a consequence, the station coordinates that go with such analyses (see Chapter 4) are “conventional tide free” values.

The geopotential can be realized in three different cases (i.e., mean tide, zero tide or tide free). For those parameters for which the difference is relevant, the values given in Table 1.1 are “zero-tide” values, according to the IAG Resolution.

The different notions related to the treatment of the permanent tide are shown pictorially in Figures 1.1 and 1.2.

![](../chunks/IERS Conventions (2010), IERS Technical Note No.36_part_0001_pages_0001-0070/auto/images/bddf43bf2c8bdaa83b143b35fdd7713da303df15551ab2ee0a8973b7b6f8aec5.jpg)  
Figure 1.1: Treatment of observations to account for tidal deformations in terrestrial reference systems (see Chapters 4 and 7).

# 1.2 Numerical standards

Table 1.1, that lists adopted numerical standards, is organized into 5 columns: constant, value, uncertainty, reference, and description. Values of defining constants are provided without an uncertainty. The IAU (2009) System of Astronomical Constants (Luzum et al., 2010) is adopted for all astronomical constants which do not appear in Table 1.1. Note that, except for defining constants, the values correspond to best estimates which are valid at the time of this publication and may be re-evaluated as needed. They should not be mistaken for conventional values, such as those of the Geodetic Reference System GRS80 (Moritz, 2000) shown in Table 1.2, which are, for example, used to express geographic coordinates (see Chapter 4).

Unless otherwise stated, the values in Table 1.1 are TCG-compatible or TCBcompatible, i.e. they are consistent with the use of Geocentric Coordinate Time TCG as a time coordinate for the geocentric system, and of Barycentric Coordinate Time TCB for the barycentric system. Note that for astronomical constants such as mass parameters $\it G M$ of celestial bodies having the same value in BCRS and GCRS, the formulations “TCB-compatible” and “TCG-compatible”

![](../chunks/IERS Conventions (2010), IERS Technical Note No.36_part_0001_pages_0001-0070/auto/images/2afb94a8062811946dd061d057f76d1d4c446b5ca6adef70eebf36397f5ef29d.jpg)  
Figure 1.2: Treatment of observations to account for tidal effects in the geopotential (see Chapter 6).

are equivalent and the values may be called “unscaled” (Klioner et al., 2010). In this document some quantities are also given by TT-compatible values, having been determined using Terrestrial Time TT as a time coordinate for the geocentric system. See Chapter 10 for further details on the transformations between time scales and Chapter 3 for a discussion of the time scale used in the ephemerides.

Using SI units (Le Syst\`eme International d’Unit´es (SI), 2006) for proper quantities, coordinate quantities may be obtained as TCB-compatible when using TCB as coordinate time or as TDB-compatible when using Barycentric Dynamical Time as a coordinate time (Klioner et al., 2010). The two coordinate times differ in rate by $( 1 - L _ { B } )$ , where $L _ { B }$ is given in Table 1.1. Therefore a quantity $_ x$ with the dimension of time or length has a TCB-compatible value $x _ { T C B }$ which differs from its TDB-compatible value $x T D B$ by

$$
x _ { T D B } = x _ { T C B } \times ( 1 - L _ { B } ) .
$$

Table 1.1: IERS numerical standards.   

<table><tr><td colspan="2">Constant Value</td><td>Uncertainty</td><td>Ref. Description</td></tr><tr><td colspan="4">Natural defining constants</td></tr><tr><td>C</td><td>299792458 ms-1</td><td>Defining</td><td>[1] Speed of light</td></tr><tr><td colspan="4">Auxiliary defining constants</td></tr><tr><td>k</td><td>1.720209895× 10-2</td><td>Defining</td><td>[2] Gaussian gravitational constant</td></tr><tr><td>LG</td><td>6.969290134× 10-10</td><td>Defining</td><td>[3] 1-d(TT)/d(TCG)</td></tr><tr><td>LB</td><td>1.550519768 × 10-8</td><td>Defining</td><td>[4]1-d(TDB)/d(TCB)</td></tr><tr><td>TDB0</td><td>-6.55 × 10-5 s</td><td>Defining</td><td>[4] TDB-TCB at JD 2443144.5 TAI</td></tr><tr><td>0</td><td>0.7790572732640 rev</td><td>Defining</td><td>[3] Earth Rotation Angle (ERA) at J2000.0 [3] Rate of advance of ERA</td></tr><tr><td>de/dt</td><td colspan="4">1.00273781191135448 rev/UT1day Defining</td></tr><tr><td colspan="5">Natural measurable constant</td></tr><tr><td>G</td><td>6.67428 × 10-11 1mkg-1s-2</td><td>6.7×10-15 m³kg-1s-²</td><td></td><td>[1] Constant of gravitation</td></tr><tr><td colspan="5">Body constants</td></tr><tr><td>GM#</td><td>1.32712442099 × 1020 ms-2</td><td>1×1010ms-2</td><td></td><td>[5] Heliocentric gravitational constant</td></tr><tr><td>J20</td><td>2.0 ×10-7</td><td>(adopted for DE421)</td><td></td><td>[5] Dynamical form factor of the Sun</td></tr><tr><td>片</td><td>0.0123000371</td><td>4×10-10</td><td></td><td>[6] Moon-Earth mass ratio</td></tr><tr><td colspan="5">Earth constants</td></tr><tr><td>GM+</td><td>ms-2 3.986004418 × 1014</td><td>8×105 m3s-2</td><td></td><td>[7] Geocentric gravitational constant</td></tr><tr><td>apt</td><td>6378136.6 m</td><td>0.1m</td><td></td><td>[8]Equatorial radius of the Earth</td></tr><tr><td>J2</td><td>1.0826359 × 10-3</td><td>1 ×10-10</td><td></td><td>[8] Dynamical form factor of the Earth</td></tr><tr><td>1/f</td><td>298.25642</td><td>0.00001</td><td>[8]</td><td>Flattening factor of the Earth</td></tr><tr><td>gEtt</td><td>9.7803278 ms-2</td><td>1 × 10-6ms-²</td><td>[8]</td><td>Mean equatorial gravity</td></tr><tr><td>W</td><td>62636856.0 m2s-2</td><td>0.5 m²s-2</td><td>[8]</td><td>Potential of the geoid</td></tr><tr><td>R+</td><td>6363672.6 m</td><td>0.1m</td><td>[8]</td><td>Geopotential scale factor (GM /Wo)</td></tr><tr><td>H</td><td>3273795 ×10-9</td><td>1×10-9</td><td></td><td>[9] Dynamical flattening</td></tr><tr><td colspan="5">Initial value at J2000.0</td></tr><tr><td>E</td><td>84381.406&quot;</td><td>0.001&quot;</td><td></td><td>[4] Obliquity of the ecliptic at J2000.0</td></tr><tr><td colspan="5">Other constants</td></tr><tr><td>autt</td><td>1.49597870700 × 1011m</td><td>3m</td><td></td><td>[6] Astronomical unit</td></tr><tr><td>Lc</td><td>1.48082686741 × 10-8</td><td>2×10-17</td><td></td><td>[3] Average value of 1-d(TCG)/d(TCB)</td></tr></table>

$\#$ TCB-compatible value, computed from the TDB-compatible value in [5].

The value for $G M _ { \oplus }$ is TCG-compatible. For $a _ { E }$ , $g _ { E }$ and $R _ { 0 }$ the difference between TCG-compatible and TT-compatible is not relevant with respect to the uncertainty.

The values for $a _ { E }$ , $1 / f$ , $J _ { 2 \oplus }$ and $_ { g \scriptscriptstyle E }$ are “zero tide” values (see the discussion in Section 1.1 above). Values according to other conventions may be found in reference [8].

TDB-compatible value. An accepted definition for the TCB-compatible value of au is still under discussion.   
[1] Mohr et al., 2008. [2] Resolution adopted at the IAU XVI General Assembly (M¨uller and Jappel, 1977), see http://www.iau.org/administration/resolutions/general assemblies/.   
[3] Resolution adopted at the IAU XXIV General Assembly (Rickman, 2001), see http://www.iau.org/administration/resolutions/general assemblies/.   
[4] Resolution adopted at the IAU XXVI General Assembly (van der Hucht, 2008), see http://www.iau.org/administration/resolutions/general assemblies/.   
[5] Folkner et al., 2008.   
[6] Pitjeva and Standish, 2009.   
[7] Ries et al., 1992. Recent studies (Ries, 2007) indicate an uncertainty of $4 \times 1 0 ^ { 5 } ~ \mathrm { { m ^ { 3 } s ^ { - 2 } } }$ .   
[8] Groten, 2004.   
[9] Value and uncertainty consistent with the IAU2006/2000 precession-nutation model, see (Capitaine et al., 2003).

Table 1.2: Parameters of the Geodetic Reference System GRS80   

<table><tr><td>Constant</td><td>Value</td><td>Description</td></tr><tr><td>GM</td><td>3.986005 × 1014 ms-2</td><td>Geocentric gravitational constant</td></tr><tr><td>aE</td><td>6378137 m</td><td>Equatorial radius of the Earth</td></tr><tr><td>J2</td><td>1.08263 × 10-3</td><td>Dynamical form factor</td></tr><tr><td>W</td><td>7.292115 × 10-5 rads-1</td><td>Nominal mean Earth&#x27;s angular velocity</td></tr><tr><td>1/f</td><td>298.257222101</td><td>Flattening factor of the Earth</td></tr></table>

Similarly, a TCG-compatible value $x _ { T C G }$ differs from a TT-compatible value $x _ { T T }$ by

$$
x _ { T T } = x _ { T C G } \times ( 1 - L _ { G } ) ,
$$

where $\boldsymbol { L } _ { G }$ is given in Table 1.1.

As an example, the TT-compatible geocentric gravitational constant is 3.986004415 $\times$ $1 0 ^ { 1 4 } ~ \mathrm { m ^ { 3 } s ^ { - 2 } }$ , as obtained from the above equation applied to the TCG-compatible value from Table 1.1. It shall be used to compute orbits in a TT-compatible reference frame, see Chapter 6. Most ITRS realizations are given in TT-compatible coordinates (except ITRF94, 96 and 97), see Chapter 4.

# References

Capitaine, N., Wallace, P. T., and Chapront, J., 2003, “Expressions for IAU 2000 precession quantities,” Astron. Astrophys., 412(2), pp. 567–586, doi:10.1051/0004-6361:20031539.   
Folkner, W. M., Williams, J. G., and Boggs, D. H., 2008, “The Planetary and Lunar Ephemeris DE 421,” IPN Progress Report 42–178, August 15, 2009, 31 pp., see http://ipnpr.jpl.nasa.gov/progress report/42-178/178C.pdf.   
Groten, E., 2004, “Fundamental parameters and current (2004) best estimates of the parameters of common relevance to astronomy, geodesy, and geodynamics,” J. Geod., 77(10-11), pp. 724–731, doi:10.1007/s00190-003-0373-y.   
IAG, 1984, “Resolutions of the XVIII General Assembly of the International Association of Geodesy, Hamburg, Germany, August 15-27, 1983,” J. Geod., 58(3), pp. 309–323, doi:10.1007/BF02519005.   
Klioner, S. A., Capitaine, N., Folkner, W., Guinot, B., Huang, T.-Y., Kopeikin, S., Pitjeva, E., Seidelmann, P. K., Soffel, M., 2010, “Units of relativistic time scales and associated quantities,” in Relativity in Fundamental Astronomy: Dynamics, Reference Frames, and Data Analysis, Proceedings of the International Astronomical Union Symposium No.261, 2009, S. Klioner, P. K. Seidelmann & M. Soffel, eds., Cambridge University Press, pp. 79–84, doi:10.1017/S1743921309990184.   
Lambeck, K., 1980, “The Earth’s variable rotation,” Cambridge University Press, pp. 27–29, ISBN: 978-0-521-22769-8.   
Le Syst\`eme International d’Unit´es (SI), 2006, Bureau International des Poids et Mesures, S\`evres, France, 180 pp.   
Luzum, B., Capitaine, N., Fienga, A., Folkner, W., Fukushima, T., Hilton, J., Hohenkerk, C., Krasinsky, G., Petit, G., Pitjeva, E., Soffel, M., Wallace, P., 2010, “Report of the IAU Working Group on Numerical Standards of Fundamental Astronomy” to be submitted to Celest. Mech. Dyn. Astr.   
Mohr, P. J., Taylor, B. N., and Newell, D. B., 2008, “CODATA recommended values of the fundamental physical constants: 2006,” Rev. Mod. Phys., 80(2), pp. 633–730, doi:10.1103/RevModPhys.80.633.   
Moritz, H., 2000, “Geodetic Reference System 1980,” J. Geod., 74(1), pp. 128– 162, doi:10.1007/S001900050278.   
Munk, W. H., and MacDonald, G. J. F., 1960, “The rotation of the Earth: A geophysical discussion,” Cambridge University Press, pp. 23–37, ISBN: 978- 0-521-20778-2.   
M¨uller, E. and Jappel, A., 1977, “Proceedings of the 16th General Assembly,” Grenoble, France, August 24-September 21, 1976, Transactions of the International Astronomical Union, 16B, Association of Univ. for Research in Astronomy, ISBN 90-277-0836-3.   
Pitjeva, E. and Standish, E. M., 2009, “Proposals for the masses of the three largest asteroids, the Moon-Earth mass ratio and the Astronomical Unit,” Celest. Mech. Dyn. Astr., 103(4), pp. 365–372, doi:10.1007/s10569-009- 9203-8.   
Rickman, H., 2001, “Proceedings of the 24th General Assembly,” Manchester, UK, August 7-18, 2000, Transactions of the International Astronomical Union, 24B, Astronomical Society of the Pacific, ISBN 1-58381-087-0.   
Ries, J. C., Eanes, R. J., Shum, C. K., and Watkins, M. M., 1992, “Progress in the determination of the gravitational coefficient of the Earth,” Geophys. Res. Lett., 19(6), pp. 529–531, doi:10.1029/92GL00259.   
Ries, J. C., 2007, “Satellite laser ranging and the terrestrial reference frame; Principal sources of uncertainty in the determination of the scale,” Geophysical Research Abstracts, Vol. 9, 10809, EGU General Assembly, Vienna, Austria, April 15-20, 2007 [SRef-ID: 1607-7962/gra/EGU2007-A-10809].   
van der Hucht, K. A., 2008, “Proceedings of the 26th General Assembly,” Prague, Czech Republic, August 14-25, 2006, Transactions of the International Astronomical Union, 26B, Cambridge University Press, ISBN 978-0-521-85606- 5.

The celestial reference system is based on a kinematical definition, yielding fixed axis directions with respect to the distant matter of the universe. The system is materialized by a celestial reference frame consisting of the precise coordinates of extragalactic objects, mostly quasars, BL Lacertae (BL Lac) sources and a few active galactic nuclei (AGNs), on the grounds that these sources are that far away that their expected proper motions should be negligibly small. The current positions are known to better than a milliarcsecond, the ultimate accuracy being primarily limited by the structure instability of the sources in radio wavelengths. A large amount of imaging data is available at the USNO Radio Reference Frame Image Database ${ < } ^ { 1 } >$ and at the Bordeaux VLBI Image Database ${ < } ^ { 2 } >$ .

The IAU recommended in 1991 (21st IAU GA, Rec. VII, Resol. A4) that the origin of the celestial reference system is to be at the barycenter of the solar system and the directions of the axes should be fixed with respect to the quasars. This recommendation further stipulates that the celestial reference system should have its principal plane as close as possible to the mean equator at J2000.0 and that the origin of this principal plane should be as close as possible to the dynamical equinox of J2000.0. This system was prepared by the IERS and was adopted by the IAU General Assembly in 1997 (23rd IAU GA, Resol. B2) under the name of the International Celestial Reference System (ICRS). It officially replaced the FK5 system on January 1, 1998, considering that all the conditions set up by the 1991 resolutions were fulfilled, including the availability of the Hipparcos optical reference frame realizing the ICRS with an accuracy significantly better than the FK5. Responsibilities for the maintenance of the system, the frame and its link to the Hipparcos reference frame have been defined by the IAU in 2000 (24th IAU GA, Resol. B1.1)

# 2.1 The ICRS

The necessity of keeping the reference directions fixed and the continuing improvement in the source coordinates requires regular maintenance of the frame. Realizations of the IERS celestial reference frame have been computed every year between 1989 and 1995 (see the IERS annual reports) keeping the same IERS extragalactic celestial reference system. The number of defining sources has progressively grown from 23 in 1988 to 212 in 1995. Comparisons between successive realizations of the IERS celestial reference system have shown that there were small shifts of order 0.1 mas from year to year until the process converged to better than 0.02 mas for the relative orientation between successive realizations after 1992. The IERS proposed that the 1995 version of the IERS system be taken as the International Celestial Reference System (ICRS). This was formally accepted by the IAU in 1997 and is described in Arias et al. (1995).

The process of maintenance of the system and improvement of the frame since its first realization in 1995 resulted in an increase of the stability of the axes of the system. The comparison between the latest two realizations of the ICRS, ICRF2 and ICRF-Ext.2, indicates that the axes of the ICRS are stable within 10 µas (IERS, 2009).

# 2.1.1 Equator

The IAU recommendations call for the principal plane of the conventional reference system to be close to the mean equator at J2000.0. The VLBI observations used to establish the extragalactic reference frame are also used to monitor the motion of the celestial pole in the sky (precession and nutation). In this way, the VLBI analyses provide corrections to the conventional IAU models for precession and nutation (Lieske et al., 1977; Seidelmann, 1982) and accurate estimation of the shift of the mean pole at J2000.0 relative to the Conventional Reference Pole of the ICRS. Based on the VLBI solutions submitted to the IERS in 2001, the shift of the pole at J2000.0 relative to the ICRS celestial pole has been estimated by using (a) the updated nutation model IERS (1996) and (b) the MHB2000 nutation model (Mathews et al., 2002). The direction of the mean pole at J2000.0 in the ICRS is $+ 1 7 . 1$ mas in the direction $1 2 ^ { \mathrm { h } }$ and $+ 5 . 0$ mas in the direction $1 8 ^ { \mathrm { h } }$ when the IERS (1996) model is used, and $+ 1 6 . 6$ mas in the direction $1 2 ^ { \mathrm { h } }$ and $+ 6 . 8$ mas in the direction $1 8 ^ { \mathrm { h } }$ when the MHB2000 model is adopted (IERS, 2001).

The IAU recommendations stipulate that the direction of the Conventional Reference Pole should be consistent with that of the FK5. The uncertainty in the direction of the FK5 pole can be estimated (1) by considering that the systematic part is dominated by a correction of about $- 0 . 3 0 ^ { \prime \prime } / \mathrm { c }$ . to the precession constant used in the construction of the FK5 system, and (2) by adopting Fricke’s (1982) estimation of the accuracy of the FK5 equator $( \pm 0 . 0 2 ^ { \prime \prime } )$ , and Schwan’s (1988) estimation of the limit of the residual rotation $\left( \pm 0 . 0 7 ^ { \prime \prime } / \mathrm { c } . \right)$ , taking the epochs of observations from Fricke et al. (1988). Assuming that the error in the precession rate is absorbed by the proper motions of stars, the uncertainty in the FK5 pole position relative to the mean pole at J2000.0 estimated in this way is $\pm 5 0$ mas. The ICRS celestial pole is therefore consistent with that of the FK5 within the uncertainty of the latter.

# 2.1.2 Origin of right ascension

The IAU recommends that the origin of right ascension of the ICRS be close to the dynamical equinox at J2000.0. The x-axis of the IERS celestial system was implicitly defined in its initial realization (Arias et al., 1988) by adopting the mean right ascension of 23 radio sources in a group of catalogs that were compiled by fixing the right ascension of the quasar 3C 273B to the usual (Hazard et al., 1971) conventional FK5 value ( $1 2 ^ { \mathrm { h } } 2 9 ^ { \mathrm { m } } 6 . 6 9 9 7 ^ { \mathrm { s } }$ at J2000.0) (Kaplan et al., 1982).

The uncertainty of the determination of the FK5 origin of right ascensions can be derived from the quadratic sum of the accuracies given by Fricke (1982) and Schwan (1988), considering a mean epoch of 1955 for the proper motions in right ascension (see last paragraph of Section 2.1.1 for further details). The uncertainty thus obtained is $\pm 8 0$ mas. This was confirmed by Lindegren et al. (1995) who found that the comparison of FK5 positions with those of the Hipparcos preliminary catalog shows a systematic position error in FK5 of the order of 100 mas. This was also confirmed by Mignard and Froeschl´e (2000) when linking the final Hipparcos catalog to the ICRS.

Analyses of LLR observations (Chapront et al., 2002) indicate that the origin of right ascension in the ICRS is shifted from the inertial mean equinox at J2000.0 on the ICRS reference plane by $- 5 5 . 4 \pm 0 . 1$ mas (direct rotation around the polar axis). Note that this shift of $- 5 5 . 4$ mas on the ICRS equator corresponds to a shift of $- 1 4 . 6$ mas on the mean equator of J2000.0 that is used in Chapter 5. The equinox of the FK5 was found by Mignard and Froeschl´e (2000) to be at $- 2 2 . 9 \pm 2 . 3$ mas from the origin of the right ascension of the IERS. These results indicate that the ICRS origin of right ascension complies with the requirements established in the IAU recommendations (21st IAU GA, Rec. VII, Resol. A4).

# 2.2 The ICRF

The ICRS is realized by the International Celestial Reference Frame (ICRF). A realization of the ICRF consists of a set of precise coordinates of compact extragalactic radio sources. Defining sources should have a large number of observations over a sufficiently long data span to assess position stability; they maintain the axes of the ICRS. The ICRF positions are independent of the equator, equinox, ecliptic, and epoch, but are made consistent with the previous stellar and dynamical realizations within their respective uncertainties.

The first realization of the ICRF (hereafter referred to as ICRF1) was constructed in 1995 by using the very long baseline interferometry (VLBI) positions of 212 “defining” compact extragalactic radio sources (IERS, 1997; Ma et al., 1998). In addition to the defining sources, positions for 294 less observed “candidate” sources along with 102 less suitable “other” sources were given to densify the frame. The position formal uncertainties of the set of positions obtained by this analysis were calibrated to render their values more realistic. The 212 defining sources are distributed over the sky with a median uncertainty of $\pm 0 . 3 5$ mas in right ascension and of $\pm 0 . 4 0$ mas in declination. The uncertainty from the representation of the ICRS is then established to be smaller than 0.01 mas. The set of positions obtained by this analysis was rotated to the ICRS. The scattering of rotation parameters of different comparisons performed shows that these axes are stable to $\pm 0 . 0 2$ mas. Note that this frame stability is based upon the assumption that the sources have no proper motion and that there is no global rotation of the universe. The assumption concerning proper motion was checked regularly on the successive IERS frames (Ma and Shaffer, 1991; Eubanks et al., 1994) as well as the different subsets of the final data (IERS, 1997).

Following the maintenance process which characterizes the ICRS, two extensions of the frame were constructed: 1) ICRF-Ext.1 by using VLBI data available until April 1999 (IERS, 1999) and 2) ICRF-Ext.2 by using VLBI data available until May 2002 (Fey et al., 2004). The positions and errors of defining sources are unchanged from ICRF1. For candidate and other sources, new positions and errors have been calculated. All of them are listed in the catalogs in order to have a larger, usable, consistent catalog. The total number of objects is 667 in ICRF-Ext.1 and 717 in ICRF-Ext.2.

The generation of a second realization of the International Celestial Reference Frame (ICRF2) was constructed in 2009 by using positions of 295 new “defining” compact extragalactic radio sources selected on the basis of positional stability and the lack of extensive intrinsic source structure (IERS, 2009). Future maintenance of the ICRS will be made using this new set of 295 sources. ICRF2 contains accurate positions of an additional 3119 compact extragalactic radio sources; in total the ICRF2 contains more than five times the number of sources as in ICRF1. The position formal uncertainties of the set of positions obtained by this analysis were calibrated to render their values more realistic. The noise floor of ICRF2 is found to be only $\approx 4 0$ $\mu$ as, some $5 - 6$ times better than ICRF1. Alignment of ICRF2 with the ICRS was made using 138 stable sources common to both ICRF2 and ICRF-Ext.2. The stability of the system axes was tested by estimating the relative orientation between ICRF2 and ICRF-Ext.2 on the basis of various subsets of sources. The scatter of the rotation parameters obtained in the different comparisons indicate that the axes are stable to within $1 0 ~ \mu \mathrm { a s }$ , nearly twice as stable as for ICRF1. The position stability of the 295 ICRF2 defining sources, and their more uniform sky distribution, eliminates the two largest weaknesses of ICRF1.

The Resol. B3 of the XXVII IAU GA resolved that from 1 January 2010 the fundamental realization of the ICRS is the Second Realization of the International Celestial Reference Frame (ICRF2) as constructed by the IERS/IVS Working Group on the ICRF in conjunction with the IAU Division I Working Group on the Second Realization of the ICRF.

The most precise direct access to the extragalactic objects in ICRF2 is done through VLBI observations, a technique which is not widely available to users. Therefore, while VLBI is used for the maintenance of the primary frame, the tie of the ICRF to the major practical reference frames may be obtained through the use of the IERS Terrestrial Reference Frame (ITRF, see Chapter 4), the HIPPARCOS Galactic Reference Frame, and the JPL ephemerides of the solar system (see Chapter 3).

# 2.2.1 Optical realization of the ICRF

In 1997, the IAU decided to replace the optical FK5 reference frame, which was based on transit circle observations, with the Hipparcos Catalogue (ESA, 1997; IAU, 1997).

The Hipparcos Catalogue provides the equatorial coordinates for 117,955 stars on the ICRS at epoch 1991.25 along with their proper motions, their parallaxes and their magnitudes in the wide band Hipparcos system. The median uncertainties for bright stars (Hipparcos wide band magnitude $< 9$ ) are 0.77 and 0.64 mas in right ascension and declination, respectively. Similarly, the median uncertainties in annual proper motion are 0.88 and 0.74 mas/yr.

The alignment of the Hipparcos Catalogue to the ICRF was realized with a standard error of 0.6 mas for the orientation at epoch 1991.25 and 0.25 mas/yr for the spin (Kovalevsky et al., 1997). This was obtained by a variety of methods, with VLBI observations of a dozen radio stars having the largest weight.

However, due to the short epoch span of Hipparcos observations (less than 4 years) the proper motions of many stars affected by multiplicity are unreliable in the Hipparcos Catalogue. Therefore, the 24th IAU General Assembly adopted resolution B1.2 which defines the Hipparcos Celestial Reference Frame (HCRF) by excluding the stars of the Hipparcos Catalogue with C, G, O, V and X flags for the optical realization of the ICRS (IAU, 2000).

A new reduction of the Hipparcos data (van Leeuwen 2007) resulted in significant improvements mainly for the parallaxes of bright stars (magnitude $\leq 7$ ). However, the coordinate system remained unchanged. Both the original and the new reductions of the Hipparcos data are on the ICRS to within the limits specified above.

Absolute proper motions (and parallaxes) from optical data can be obtained without the HCRF by observing extragalactic sources like galaxies and quasars at multiple epochs. This has been achieved for example through the Northern Proper Motion (NPM) program (Klemola et al., 1987) and its southern counterpart, SPM (Girard et al., 1998). These proper motion data are on an inertial system, thus also on the ICRS.

To obtain absolute positions with this approach is much more difficult. Optical counterparts of ICRF sources would need to be utilized in wide-field imaging of overlapping observations to be able to bridge the large gaps between ICRF sources. This has not yet been accomplished in a practical application, thus all current optical position observations rely on a set of reference stars beginning with the HCRF as primary realization of the ICRS at optical wavelengths and the densification catalogs derived from the HCRF.

The first step of the densification of the optical reference frame is the Tycho-2 Catalogue (Høg et al., 2000) for about 2.5 million stars. The Hipparcos satellite star tracker observations (Tycho) provide the late epoch data, very well tied into the Hipparcos Catalogue. The early epoch data of Tycho-2 and thus its proper motions are derived from many ground-based catalogs which have been reduced to the HCRF with Hipparcos reference stars. The Astrographic Catalogue (AC) (Urban et al., 1998) provided the highest weight of the early observations for the Tycho-2 proper motions.

Recently the limitations of the Tycho-2 Catalogue seem to have become noticeable. Systematic errors as a function of magnitude and declination zones found in the UCAC3 (Zacharias et al., 2010, Finch et al., 2010) may be caused by the Tycho-2 itself. Similarly, systematic errors on the 2 degree scale were found in reductions of SPM data (Girard, priv. comm.). These systematic errors are on the $1 - 2 \mathrm { m a s } / \mathrm { y r }$ level, plausible with estimates of residual magnitude equations in the AC data (S. Urban, priv. comm.).

Further steps in densifications of the optical reference frame use the Tycho-2 Catalogue for reference stars. The UCAC3 (Zacharias et al., 2010) is an example of a recent all-sky, astrometric catalog based on CCD observations, providing positions and proper motions for about 100 million stars. The PPMXL (Roeser et al., 2010) is a very deep, compiled catalog giving positions and proper motions on the ICRS for over 900 million stars. Extending beyond the visual wavelengths, the 2MASS near-IR catalog $( < ^ { 3 } > )$ provides accurate positions of over 470 million stars at individual mean epochs (around 2000), however, without proper motions. An overview of other current and future, ground- and space-based densification projects is given at ${ < } ^ { 4 } >$ .

# 2.2.2 Availability of the frame

The second realization of the international celestial reference frame ICRF2 (IERS, 2009) provides the most precise access to the ICRS in radio wavelengths. ICRF2 contains 3414 compact extragalactic radio sources, almost five times the number of sources in ICRF-Ext.2 (Fey et al., 2004). The maintenance of the ICRS requires the monitoring of the source’s coordinate stability based on new observations and new analyses. Programs of observations have been established by different organizations (United States Naval Observatory (USNO), Goddard Space Flight Center (GSFC), National Radio Astronomy Observatory (NRAO), National Aeronautics and Space Administration (NASA), Bordeaux Observatory) for monitoring and extending the frame. Observations in the southern hemisphere organized under the auspices of the IVS make use of the USNO and the Australia Telescope National Facility (ATNF) for contributing to a program of source imaging and astrometry.

The IERS Earth Orientation Parameters provide the permanent tie of the ICRF to the ITRF. They describe the orientation of the Celestial Intermediate Pole (CIP) in the terrestrial system and in the celestial system (polar coordinates $\mathbf { X }$ y; celestial pole offsets $\mathrm { d } \psi$ , d) and the orientation of the Earth around this axis (UT1 $-$ UTC), as a function of time. This tie is available daily with an accuracy of $\pm 0 . 1$ mas in the IERS publications. The principles on which the ITRF is established and maintained are described in Chapter 4.

The other ties to major celestial frames are established by differential VLBI observations of solar system probes, galactic stars relative to quasars and other groundor space-based astrometry projects. The tie of the solar system ephemeris of the Jet Propulsion Laboratory (JPL) is described by Standish et al. (1997). The later JPL ephemerides (DE421) is aligned to the ICRS with an accuracy of better than 1 mas (Folkner et al., 2008, see also Chapter 3).

The lunar laser ranging (LLR) observations contribute to the link of the planetary dynamical system to the ICRS. The position of the dynamical mean ecliptic with respect to the ICRS resulting from LLR analysis is defined by the inclination of the dynamical mean ecliptic to the equator of the ICRS $( \epsilon ^ { ( I C R S ) } )$ and by the angle between the origin of the right ascension on the equator of the ICRS and the ascending node of the dynamical mean ecliptic on the equator of the ICRS $\left( \phi ^ { ( I C R S ) } \right)$ . Evaluations of $\epsilon ^ { ( I C R S ) }$ and $\phi ^ { ( I C R S ) }$ made by the Paris Observatory Lunar Analysis Centre (Chapront et al., 2002, Zerhouni et al., 2007) give the following values for these angles at the epoch J2000:

$$
\begin{array} { c } { { { ( \mathrm { I C R S } ) } = 2 3 ^ { \circ } 2 6 ^ { \prime } 2 1 . 4 1 1 ^ { \prime \prime } \pm 0 . 1 ~ \mathrm { m a s } ; } } \\ { { { } } } \\ { { \phi ^ { ( \mathrm { I C R S } ) } = - 0 . 0 5 5 ^ { \prime \prime } \pm 0 . 1 ~ \mathrm { m a s } ; } } \\ { { { } } } \\ { { d \alpha _ { 0 } = \left( - 0 . 0 1 4 6 0 \pm 0 . 0 0 0 5 0 \right) ^ { \prime \prime } . } } \end{array}
$$

Ties to the frames related to catalogs at other wavelengths will be available from the IERS as observational analyses permit.

# References

Arias, E. F., Feissel, M., and Lestrade, J.-F., 1988, “An extragalactic celestial reference frame consistent with the BIH Terrestrial System (1987),” BIH Annual Rep. for 1987, pp. D-113–D-121.   
Arias, E. F., Charlot, P., Feissel, M., Lestrade, J.-F., 1995, “The extragalactic reference system of the International Earth Rotation Service, ICRS,” Astron. Astrophys., 303, pp. 604–608.   
Chapront, J., Chapront-Touz´e, M., and Francou, G., 2002, “A new determination of lunar orbital parameters, precession constant and tidal acceleration from LLR measurements,” Astron. Astrophys., 387(2), pp. 700–709. doi: 10.1051/0004-6361:20020420.   
ESA, 1997, “The Hipparcos and Tycho catalogues,” European Space Agency Publication, Noordwijk, SP–1200, June 1997, 19 volumes.   
Eubanks, T. M., Matsakis, D. N., Josties, F. J., Archinal, B. A., Kingham, K. A., Martin, J. O., McCarthy, D. D., Klioner, S. A., Herring, T. A., 1994, “Secular motions of extragalactic radio sources and the stability of the radio reference frame,” Proc. IAU Symposium 166, E. Høg, P. K. Seidelmann (eds.), p. 283.   
Fey, A. L., Ma, C., Arias, E. F., Charlot, P., Feissel-Vernier, M., Gontier, A.-M., Jacobs, C. S., Li, J., and MacMillan, D. S., 2004. “The Second Extension of the International Celestial Reference Frame: ICRF-EXT.1,” Astron. J., 127(6), pp. 3587–3608. doi: 10.1086/420998.   
Finch, C. T., Zacharias, N., and Wycoff, G. L., 2010, “UCAC3: Astrometric Reductions,” Astron. J., 139(6), pp. 2200–2207, doi: 10.1088/0004-6256/139/6/2200.   
Folkner, W. M., Williams, J. G., and Boggs, D. H., 2009, “The Planetary and Lunar Ephemeris DE 421,” IPN Progress Report 42-178, August 15, 2009, 34 pp., see http://ipnpr.jpl.nasa.gov/progress report/42-178/178C.pdf.   
Fricke, W., 1982, “Determination of the equinox and equator of the FK5,” Astron. Astrophys., 107(1), pp. L13–L16.   
Fricke, W., Schwan, H., and Lederle, T., 1988, Fifth Fundamental Catalogue, Part I. Ver¨off. Astron. Rechen-Inst., Heidelberg.   
Girard, T. M., Platais, I., Kozhurina-Platais, V., van Altena, W. F., Lopez, C. E., 1998, “The Southern Proper Motion program. I. Magnitude equation correction,” Astron. J., 115(2), pp. 855–867, doi: 10.1086/300210.   
Hazard, C., Sutton, J., Argue, A. N., Kenworthy, C. N., Morrison, L. V., and Murray, C. A., 1971, “Accurate radio and optical positions of 3C273B,” Nature Phys. Sci., 233, pp. 89–91.   
Høg, E., Fabricius, C., Makarov, V. V., Urban, S., Corbin, T., Wycoff, G., Bastian, U., Schwekendiek, P., and Wicenec, A., 2000, “The Tycho-2 Catalogue of the 2.5 million brightest stars,” Astron. Astrophys., 355, pp. L27–L30.   
IAU 1997 Resolution B2, “On the international celestial reference system (ICRS),” XXIIIrd IAU GA, Kyoto, 1997, http://www.iau.org/static/resolutions/IAU1997 French.pdf   
IAU 2000 Resolution B1.2, “Hipparcos Celestial Reference Frame,” XXIVth IAU GA, Manchester, 2000, http://syrte.obspm.fr/IAU resolutions/Resol-UAI.htm   
IERS, 1995, 1994 International Earth Rotation Service Annual Report, Observatoire de Paris, Paris.   
IERS, 1997, IERS Technical Note 23, “Definition and realization of the International Celestial Reference System by VLBI Astrometry of Extragalactic Objects,” Ma, C. and Feissel, M. (eds.), Observatoire de Paris, Paris, available at http://www.iers.org/TN23   
IERS, 1999, 1998 International Earth Rotation Service Annual Report, Observatoire de Paris, Paris.   
IERS, 2001, 2000 International Earth Rotation Service Annual Report, Observatoire de Paris, Paris.   
IERS, 2009, IERS Technical Note 35, “The Second Realization of the International Celestial Reference Frame by Very Long Baseline Interferometry, Presented on behalf of the IERS / IVS Working Group, Fey A. L., Gordon, D., and Jacobs, C. S. (eds.). Frankfurt am Main: Verlag des Bundesamts f¨ur Kartographie und Geod¨asie, 2009. 204 p., available at http://www.iers.org/TN35   
Kaplan, G. H., Josties, F. J., Angerhofer, P. E., Johnston, K. J., and Spencer, J. H., 1982, “Precise radio source positions from interferometric observations,” Astron. J., 87(3), pp. 570–576, doi: 10.1086/113131.   
Klemola, A. R., Jones, B. F., and Hanson, R. B., 1987, “Lick Northern Proper Motion program. I. Goals, organization, and methods,” Astron. J., 94(2), pp. 501–515, doi: 10.1086/114489.   
Kovalevsky, J., Lindegren, L., Perryman, M. A. C., Hemenway, P. D., Johnston, K. J., Kislyuk, V. S., Lestrade, J.-F., Morrison, L. V., Platais, I., R¨oser, S., Schilbach, E., Tucholke, H.-J., de Vegt, C., Vondr´ak, J., Arias, F., Gontier, A.-M., Arenou, F., Brosche, P., Florkowski, D. R., Garrington, S. T., Preston, R. A., Ron, C., Rybka, S. P., Scholz, R.-D., and Zacharias, N., 1997, “The Hipparcos Catalogue as a realization of the extragalactic reference system,” Astron. Astrophys., 323(2), pp. 620–633.   
Lieske, J. H., Lederle, T., Fricke, W., and Morando, B., 1977, “Expressions for the precession quantities based upon the IAU (1976) System of Astronomical Constants,” Astron. Astrophys., 58(1-2), pp. 1–16.   
Lindegren, L., R¨oser, S., Schrijver, H., Lattanzi, M. G., van Leeuwen, F., Perryman, M. A. C., Bernacca, P. L., Falin, J. L., Froeschl´e, M., Kovalevsky, J., Lenhardt, H., and Mignard, F., 1995, “A comparison of ground-based stellar positions and proper motions with provisional Hipparcos results,” Astron. Astrophys., 304, pp. 44–51.   
Ma, C., and Shaffer, D. B., 1991, “Stability of the extragalactic reference frame realized by VLBI,” in Reference Systems, Hughes, J. A., Smith, C. A., and Kaplan, G. H. (eds.), Proceedings of IAU Colloquium 127, U. S. Naval Observatory, Washington, pp. 135–144.   
Ma, C., Arias, E. F., Eubanks, T. M., Fey, A. L., Gontier, A.-M., Jacobs, C. S., Sovers, O. J., Archinal, B. A. and Charlot, P., 1998, “The International Celestial Reference Frame as realized by Very Long Baseline Interferometry,” Astron. J., 116(1), pp. 516–546, doi: 10.1086/300408.   
Mathews, P. M., Herring T. A., and Buffett, B. A., 2002, “Modeling of nutation and precession: New nutation series for nonrigid Earth, and insights into the Earth’s interior,” J. Geophys. Res., 107(B4), 10.1029/2001JB000390.   
Mignard, F. and Froeschl´e, M., 2000, “Global and local bias in the FK5 from the Hipparcos data,” Astron. Astrophys., 354, pp. 732–739.   
Roeser, S., Demleitner, M., and Schilbach, E., 2010, “The PPMXL Catalog of positions and proper motions on the ICRS. Combining USNO-B1.0 and the Two Micron All Sky Survey (2MASS),” Astron. J., 139(6), pp. 2440–2447, doi: 10.1088/0004-6256/139/6/2440.   
Schwan, H., 1988, “Precession and galactic rotation in the system of the FK5,” Astron. Astrophys., 198(1-2), pp. 116–124.   
Seidelmann, P. K., 1982, “1980 IAU theory of nutation: The final report of the IAU Working Group on Nutation,” Celest. Mech., 27(1), pp. 79–106, doi: 10.1007/BF01228952.   
Standish, E. M., Newhall, X X, Williams, J. G., and Folkner, W. M., 1997, “JPL Planetary and Lunar Ephemerides,” Willmann-Bell Inc., Richmond, VA.   
Urban, S. E., Corbin, T. E., Wycoff, G. L., Martin, J. C., Jackson, E. S., Zacharias, M. I., and Hall, D. M., 1998, “The AC 2000: The Astrographic Catalogue on the system defined by the Hipparcos Catalogue,” Astron. J., 115(3), pp. 1212–1223, doi: 10.1086/300264.   
van Leeuwen, F. 2007, “Hipparcos, the new reduction of the raw data,” ASPL series, Springer, doi: 10.1007/978-1-4020-6342-8.   
Zacharias, N., Finch, C., Girard, T., Hambly, N., Wycoff, G., Zacharias, M. I., Castillo, D., Corbin, T., DiVittorio, M., Dutta, S., Gaume, R., Gauss, S., Germain, M., Hall, D., Hartkopf, W., Hsu, D., Holdenried, E., Makarov, V., Martines, M., Mason, B., Monet, D., Rafferty, T., Rhodes, A., Siemers, T., Smith, D., Tilleman, T., Urban, S., Wieder, G., Winter, L., and Young, A., 2010, “The Third US Naval Observatory CCD Astrograph Catalog (UCAC3),” Astron. J., 139(6), pp. 2184–2199, doi: 10.1088/0004-6256/139/6/2184.   
Zerhouni, W., Capitaine, N., and Francou, G., 2008, “The use of LLR observations (1969-2006) for the determination of the celestial coordinates of the pole,” Journ´ees 2007 Syst\`emes de R´ef´erence Spatio-temporels, N. Capitaine (ed.), Observatoire de Paris, pp. 123–124, http://syrte.obspm.fr/journees2007/index.php?page=proceedings.pdf

The planetary and lunar ephemerides are used in a number of models and analysis methods. In some cases, e.g. interplanetary spacecraft navigation, lunar laser ranging and pulsar timing, the accuracy of the ephemeris is critical to the quality of results and so the best ephemerides should be used. In other cases, e.g. to model the gravitational attraction of external bodies for nutations and tides, use of the latest released ephemerides is not critical.

Ephemerides are updated frequently with accuracy improved through the use of more data, especially spacecraft radio tracking data and increasingly accurate astronomical observations from Earth, and by improved dynamical modeling. Recent ephemerides include the DE421 ${ < } ^ { 1 } >$ from the Jet Propulsion Laboratory (JPL) (Folkner et al., 2008), INPOP08 from the Institut de M´ecanique C´eleste et de Calcul des Eph´em´erides (IMCCE) (Fienga et al., 2009) and EPM2008 from the Institute of Applied Astronomy (IAA) (Pitjeva, 2009). These three ephemerides are expected to be of comparable quality (Folkner, 2009), e.g. a comparison between INPOP08 and DE421 (Fienga et al., 2009) shows differences mostly comparable to the expected uncertainties. When an application is sensitive to the accuracy of the ephemeris, as discussed earlier, it is recommended that DE421 be the conventional ephemeris. This recommendation is intended to provide continuity for implementation by users as the DE series have provided the dynamical realization of the celestial reference system in previous versions of the IERS Conventions, the latest being DE405 (Standish et al., 1997) in the IERS Conventions (2003).

Each of the mentioned ephemerides is integrated using the Einstein-Infeld-Hoffman equations (Einstein et al., 1938) with dynamical time consistent with Barycentric Dynamical Time (TDB) as defined by Resolution 3 from IAU General Assembly XXVI (van der Hucht, 2008). Consequently the time argument of the DE421 is TDB, which is consistent, within observational uncertainties, with $T _ { e p h }$ used as the time argument in previous JPL ephemerides (IERS Technical Note 32, Standish 1998). The ephemerides have been aligned with the International Celestial Reference Frame (ICRF) by means of Very Long Baseline Interferometry (VLBI) observations of spacecraft in orbit about Venus and Mars relative to extragalactic radio sources. The alignment of DE405 to the ICRF was done using the Magellan spacecraft in orbit about Venus with an accuracy of $0 . 0 0 1 ^ { \prime \prime }$ . Through the use of VLBI observations of Mars Global Surveyor, Mars Odyssey, and Mars Reconnaissance Orbiter, the later ephemerides (thus DE421) are aligned to the ICRF with an accuracy of $\mathrm { 0 . 0 0 0 2 5 ^ { \prime \prime } }$ .

The mass parameter (GM) of the Sun is most accurately determined by fitting planetary spacecraft range data in the planetary ephemeris fitting process. From Resolution 10 from IAU General Assembly XVI (M¨uller and Jappel, 1977), the TDB-compatible value of the mass parameter of the Sun is related to the defined value given by Gauss’ constant in units of $\mathrm { { a u } ^ { 3 } / d a y ^ { 2 } }$ by an estimated value of the Astronomical Unit (au). The TDB-compatible value of the au estimated with DE421 is 149597870.6996262 km and is consistent with the value given in Chapter 1 (Table 1.1).

The mass parameters for the planets are most accurately estimated by means of spacecraft encounters or in orbit about them. The planetary ephemerides are also sensitive to the mass parameters of asteroids, and values have been estimated through their effect on the Earth-Mars range as measured by spacecraft and by astronomical observations of asteroid mutual encounters. Table 3.1 lists mass parameters used in the DE421 ephemeris. Each solar system body’s GM is also given as a TDB-compatible value in $\mathrm { k m } ^ { 3 } / \mathrm { s } ^ { 2 }$ since all ratios change when the solar GM estimate changes. In this table, the GM values expressed in SI units indicate the accuracy by the number of significant digits. The values in Table 3.1 are provided directly with the DE421 ephemerides and should be considered to be an integral part of them; they will sometimes differ from a more standard set, but the differences are necessary for the optimal fitting of the data. A list of current best estimates of these mass parameters has been compiled by Luzum et al. (2009) and is available at ${ < } ^ { 2 } { > }$ .

Table 3.1: Mass parameters from DE421 expressed as ratios and as TDB-compatible values.   

<table><tr><td>GM/GMi</td><td>GMi/km³s-2</td></tr><tr><td>Mercury 6023597.400017</td><td>22032.090000</td></tr><tr><td>Venus</td><td>408523.718655 324858.592000</td></tr><tr><td>Earth</td><td>332946.048166 398600.436233</td></tr><tr><td>Moon</td><td>27068703.185436 4902.800076</td></tr><tr><td>Mars 3098703.590267</td><td>42828.375214</td></tr><tr><td>Jupiter</td><td>1047.348625 126712764.800000</td></tr><tr><td>Saturn</td><td>3497.901768 37940585.200000</td></tr><tr><td>Uranus</td><td>22902.981613 5794548.600000</td></tr><tr><td>Neptune</td><td>19412.237346 6836535.000000</td></tr><tr><td>Pluto 135836683.767599</td><td>977.000000</td></tr><tr><td colspan="2">GM/GMi</td></tr><tr><td>Earth-Moon mass ratio 81.3005690699</td><td></td></tr></table>

# References

Einstein, A., Infeld, L. and Hoffmann, B., 1938, “The gravitational equations and the problem of motion,” Ann. Math., 39(1), pp. 65–100, http://www.jstor. org/stable/1968714.   
Fienga, A., Laskar, J., Morley, T., Manche, H., Kuchynka, P., Le Poncin-Lafitte, C., Budnik, F., Gastineau, M. and Somenzi, L., 2009, “INPOP08, a 4-D planetary ephemeris: from asteroid and time-scale computations to ESA Mars Express and Venus Express contributions,” Astron. Astrophys., 507(3), pp. 1675–1686, doi: 10.1051/0004-6361/200911755.   
Folkner, W. M., Williams, J. G. and Boggs, D. H., 2008, “The Planetary and Lunar Ephemeris DE 421,” IPN Progress Report 42–178, August 15, 2009, 31 pp., see http://ipnpr.jpl.nasa.gov/progress report/42-178/178C.pdf   
Folkner, W. M., 2009, personal communication.   
Luzum, B., Capitaine, N., Fienga, A., Folkner, W. M., Fukushima, T., Hilton, J. L., Hohenkerk, C. Y., Krasinsky, G. A., Petit, G., Pitjeva, E. V., Soffel, M. H. and Wallace, P. T., 2009, “Report of the Division I Working Group on Numerical Standards for Fundamental Astronomy,” http://maia.usno.navy.mil/NSFA/CBE.html   
McCarthy, D. D. and Petit, G. (eds.), 2004, “IERS Conventions (2003),” IERS Technical Note 32, Frankfurt am Main: Verlag des Bundesamts f¨ur Kartographie und Geod¨asie, 127 pp, ISBN 3-89888-884-3, see http://www.iers.org/TN32   
M¨uller, E. and Jappel, A., 1977, “Proceedings of the 16th General Assembly,” Grenoble, France, August 24-September 21, 1976, Transactions of the International Astronomical Union, 16B, Association of Univ. for Research in Astronomy, ISBN 90-277-0836-3, see http://www.iau.org/administration/resolutions/general assemblies/.   
Pitjeva, E. V., 2009, “Ephemerides EPM2008: The updated model, constants, data,” in Proceedings of the “Journ´ees 2008 Syst\`emes de r´ef´erence spatiotemporels,” M. Soffel and N. Capitaine (eds.), Lohrmann-Observatorium and Observatoire de Paris, pp. 57–60.   
Standish, E. M., 1998, “Time scales in the JPL and CfA ephemerides,” Astron. Astrophys., 336, pp. 381–384.   
Standish, E. M., Newhall, X X, Williams, J. G. and Folkner, W. M., 1997, “JPL Planetary and Lunar Ephemerides,” Willmann-Bell Inc., Richmond, VA.   
van der Hucht, K. A., 2008, “Proceedings of the 26th General Assembly,” Prague, Czech Republic, August 14-25, 2006, Transactions of the International Astronomical Union, 26B, Cambridge University Press, ISBN 978-0-521-85606- 5, see http://www.iau.org/administration/resolutions/general assemblies/.

# 4 Terrestrial reference systems and frames

# 4.1 Concepts and terminology

# 4.1.1 Basic concepts

Terrestrial Reference Systems and their realizations. A Terrestrial Reference System (TRS) is a spatial reference system co-rotating with the Earth in its diurnal motion in space. In such a system, positions of points attached to the solid surface of the Earth have coordinates which undergo only small variations with time, due to geophysical effects (tectonic or tidal deformations). In the physical model adopted in astrogeodesy, a TRS is modeled as a reference trihedron close to the Earth and co-rotating with it. In the Newtonian framework, the physical space is considered as a Euclidean affine space of dimension 3. In this case, such a reference trihedron is a Euclidean affine frame $( O , E )$ . $O$ is a point of the space named origin and $E$ is a basis of the associated vector space. The currently adopted restrictions on $E$ are to be right-handed, orthogonal with the same length for the basis vectors. The triplet of unit vectors collinear to the basis vectors expresses the orientation of the TRS and the common length of these vectors its scale,

$$
\lambda = \| \vec { E } _ { i } \| _ { i } \qquad i = 1 , 2 , 3 .
$$

Here, we consider geocentric TRSs for which the origin is close to the Earth’s center of mass (geocenter), the orientation is equatorial (the $Z$ axis is the direction of the pole) and the scale is close to an SI meter. In addition to Cartesian coordinates (naturally associated with such a TRS), other coordinate systems, e.g. geographical coordinates, could be used. For a general reference on coordinate systems, see Boucher (2001).

Under these hypotheses, the general transformation of the Cartesian coordinates of any point close to the Earth from TRS (1) to TRS (2) is given by a threedimensional similarity ( $\vec { T } _ { 1 , 2 }$ is a translation vector, $\lambda _ { 1 , 2 }$ a scale factor and $R _ { 1 , 2 }$ a rotation matrix)

$$
\vec { X } ^ { ( 2 ) } = \vec { T } _ { 1 , 2 } + \lambda _ { 1 , 2 } \cdot R _ { 1 , 2 } \cdot \vec { X } ^ { ( 1 ) } .
$$

This concept can be generalized in the frame of a relativistic background model such as Einstein’s General Theory of Relativity, using the spatial part of a local Cartesian coordinate system (Boucher, 1986). For more details concerning general relativistic models, see Chapters 10 and 11.

In the application of Equation (4.2), the IERS uses the linearized formulas and notation. The standard transformation between two reference systems is a Euclidean similarity of seven parameters: three translation components, one scale factor, and three rotation angles, designated respectively, $_ { \textrm { \tiny 1 1 } }$ , $^ { \prime } T 2$ , $^ { \prime } 3$ , $D$ , $R 1$ , $R 2$ , $R 3$ , and their first time derivatives: $\dot { T } 1$ , $\dot { T } 2$ , $\dot { T } 3$ , $\dot { D }$ , $\dot { R } 1$ , $\dot { R } 2$ , $\dot { R 3 }$ . The transformation of a coordinate vector $\vec { X } _ { 1 }$ , expressed in reference system (1), into a coordinate vector $\vec { X _ { 2 } }$ , expressed in reference system (2), is given by

$$
\vec { X } _ { 2 } = \vec { X } _ { 1 } + \vec { \mathcal { T } } + D \vec { X } _ { 1 } + \mathcal { R } \vec { X } _ { 1 } ,
$$

where $\vec { \mathcal { T } } = \vec { T } _ { 1 , 2 }$ , $D = \lambda _ { 1 , 2 } - 1$ , $\mathcal { R } = ( R _ { 1 , 2 } - I )$ , and $I$ is the identity matrix so that

$$
\mathcal { T } = \left( \begin{array} { c } { T 1 } \\ { T 2 } \\ { T 3 } \end{array} \right) , \quad \mathcal { R } = \left( \begin{array} { c c c } { 0 } & { - R 3 } & { R 2 } \\ { R 3 } & { 0 } & { - R 1 } \\ { - R 2 } & { R 1 } & { 0 } \end{array} \right) .
$$

It is assumed that Equation (4.3) is linear for sets of station coordinates provided by space geodesy techniques. Origin differences are about a few hundred meters, and differences in scale and orientation are at the level of $1 0 ^ { - 5 }$ . Generally, $\vec { X } _ { 1 } , \vec { X } _ { 2 } , \tau , D$ and $_ { \mathcal { R } }$ are functions of time. Differentiating Equation (4.3) with respect to time gives

$$
\dot { \vec { X } } _ { 2 } = \dot { \vec { X } } _ { 1 } + \dot { \vec { T } } + \dot { D } \vec { X } _ { 1 } + D \dot { \vec { X } } _ { 1 } + \dot { \mathcal { R } } \vec { X } _ { 1 } + \mathcal { R } \dot { \vec { X } } _ { 1 } .
$$

$D$ and $_ { \mathcal { R } }$ are at the $1 0 ^ { - 5 }$ level and $\dot { \vec { X } }$ is about 10 cm per year, so the terms $D \dot { X } _ { 1 }$ and $\mathcal { R } \dot { \vec { X } } _ { 1 }$ which represent about $0 . 1 \mathrm { m m }$ over 100 years are negligible. Therefore, Equation (4.4) could be written as

$$
\dot { \vec { X } } _ { 2 } = \dot { \vec { X } } _ { 1 } + \dot { \vec { \tau } } + \dot { D } \vec { X } _ { 1 } + \dot { \mathcal { R } } \vec { X } _ { 1 } .
$$

It is fundamental to distinguish between a TRS, having a theoretical definition, and its realization, a Terrestrial Reference Frame (TRF), to which users have access.

Terrestrial Reference Frame (TRF). A Terrestrial Reference Frame is defined as the realization of a TRS, through the realization of its origin, orientation axes and scale, and their time evolution. We consider here that the realization is achieved by a set of physical points with precisely determined coordinates in a specific coordinate system as a realization of a Terrestrial Reference System. It is also designated as a crust-based TRF and described in more detail in Section 4.1.3.

# 4.1.2 TRF in space geodesy

Seven parameters are needed to fix a TRF at a given epoch, to which are added their time derivatives to define the TRF time evolution. The selection of the 14 parameters, called “datum definition,” establishes the TRF origin, scale, orientation and their time evolution.

Space geodesy techniques are not sensitive to all the parameters of the TRF datum definition. The origin is theoretically accessible through dynamical techniques (LLR, SLR, GNSS, DORIS), being the center of mass (point around which the satellite orbits). The scale depends on some physical parameters (e.g. geogravitational constant $\it G M$ and speed of light $c$ ) and relativistic modeling. The orientation, unobservable by any technique, is arbitrary or conventionally defined. Meanwhile it is recommended to define the orientation’s time evolution using a no-net-rotation condition with respect to horizontal motions over the Earth’s surface.

Since space geodesy observations do not contain all the necessary information to completely establish a TRF, some additional information is needed to complete the datum definition. In terms of normal equations, usually constructed upon space geodesy observations, this situation is reflected by the fact that the normal matrix, $N$ , is singular, since it has a rank deficiency corresponding to the number of datum parameters which are not reduced by the observations.

In order to cope with this rank deficiency, the analysis centers currently add one of the following constraints upon all or a sub-set of stations:

1. Removable constraints: solutions for which the estimated station positions and/or velocities are constrained to external values within an uncertainty $\sigma \approx 1 0 ^ { - 5 }$ m for positions and $\mathrm { m } / \mathrm { y }$ for velocities. This type of constraint is easily removable, see for instance Altamimi et al. (2002a; 2002b).   
2. Loose constraints: solutions where the uncertainty applied to the constraints is $\sigma \geq 1$ m for positions and $\geq 1 0 \ \mathrm { c m / y }$ for velocities.   
3. Minimum constraints used solely to define the TRF using a minimum amount of required information. For more details on the concepts and practical use of minimum constraints, see for instance Sillard and Boucher (2001) or Altamimi et al. (2002a).

Note that the old method, where very tight constraints $\sigma \leq 1 0 ^ { - 1 0 } ~ \mathrm { m }$ ) are applied (which are numerically not easy to remove), is no longer suitable and may alter the real quality of the estimated parameters.

In case of removable or loose constraints, this amounts to adding the following observation equation

$$
{ \vec { X } } - { \vec { X } } _ { 0 } = 0 ,
$$

where $\vec { X }$ is the vector of estimated parameters (positions and/or velocities) and ${ \vec { X } } _ { 0 }$ is that of the $a$ priori parameters.

Meanwhile, in the case of minimum constraints, the added equation is of the form

$$
B ( \vec { X } - \vec { X } _ { 0 } ) = 0 ,
$$

where $B = ( A ^ { T } A ) ^ { - 1 } A ^ { T }$ and $A$ is the design matrix of partial derivatives, constructed upon $a$ priori values $( \vec { X } _ { 0 } )$ given by either

$$
A = \left( \begin{array} { c c c c c c c c } { { . } } & { { . } } & { { . } } & { { . } } & { { . } } & { { . } } & { { . } } \\ { { 1 } } & { { 0 } } & { { 0 } } & { { x _ { 0 } ^ { i } } } & { { 0 } } & { { z _ { 0 } ^ { i } } } & { { - y _ { 0 } ^ { i } } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { y _ { 0 } ^ { i } } } & { { - z _ { 0 } ^ { i } } } & { { 0 } } & { { x _ { 0 } ^ { i } } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { . } } & { { } } & { { . } } & { { . } } & { { . } } & { { . } } & { { } } & { { . } } \end{array} \right)
$$

when solving for only station positions, or

$$
\begin{array} { r } { A = \left( \begin{array} { l l l l l l l l l l l l l } { ~ . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } \\ { ~ 1 } & { 0 } & { 0 } & { x _ { 0 } ^ { i } } & { 0 } & { z _ { 0 } ^ { i } } & { - y _ { 0 } ^ { i } } & & & & & { . } & { . } & { . } & { . } \\ { ~ 0 } & { 1 } & { 0 } & { y _ { 0 } ^ { i } } & { - z _ { 0 } ^ { i } } & { 0 } & { x _ { 0 } ^ { i } } & & & & & { 0 } \\ { ~ 0 } & { 0 } & { 1 } & { z _ { 0 } ^ { i } } & { y _ { 0 } ^ { i } } & { - x _ { 0 } ^ { 0 } } & { 0 } & & & & & { 0 } \\ & & & & & { 1 } & { 0 } & { 0 } & { x _ { 0 } ^ { i } } & { 0 } & { z _ { 0 } ^ { i } } & { - y _ { 0 } ^ { i } } \\ & & { \approx 0 } & & & { 0 } & { 1 } & { 0 } & { y _ { 0 } ^ { i } } & { - z _ { 0 } ^ { i } } & { 0 } & { x _ { 0 } ^ { i } } \\ & & & & & & { 0 } & { 0 } & { 1 } & { z _ { 0 } ^ { i } } & { y _ { 0 } ^ { i } } & { - x _ { 0 } ^ { i } } & { 0 } \\ { ~ . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } \end{array} \right) } \end{array}
$$

when solving for station positions and velocities.

The fundamental distinction between the two approaches is that in Equation (4.6), we force $\vec { X }$ to be equal to $\vec { X } _ { 0 }$ (to a given $\sigma$ ), while in Equation (4.7) we express $\vec { X }$ in the same TRF as $\vec { X _ { 0 } }$ using the projector $B$ containing all the necessary information defining the underlying TRF. Note that the two approaches are sensitive to the configuration and quality of the subset of stations ( ${ \vec { X } } _ { 0 }$ ) used in these constraints. In terms of normal equations, Equation (4.7) could be written as

$$
B ^ { T } \Sigma _ { \theta } ^ { - 1 } B ( \vec { X } - \vec { X _ { 0 } } ) = 0 ,
$$

where $\Sigma _ { \theta }$ is a diagonal matrix containing small variances for each of the transformation parameters.

The general form of the singular normal equation constructed upon space geodesy observations could be written as

$$
N ( \Delta { \vec { X } } ) = K ,
$$

where $\Delta \vec { X } = \vec { X } - \vec { X _ { 0 } }$ designates the linearized unknowns and $K$ is the right-hand side of the normal equation. Adding Equation (4.10) to the normal equation (4.11) allows it to be inverted and simultaneously to express the estimated solution $\vec { X }$ in the same TRF as the a priori solution $\vec { X _ { 0 } }$ . Note that the 7 columns of the design matrix $A$ correspond to the 7 datum parameters (3 translations, 1 scale factor and 3 rotations). Therefore, this matrix should be reduced to those parameters which need to be defined (e.g. 3 rotations in almost all techniques and 3 translations in case of VLBI). For more practical details, see, for instance, Altamimi et al. (2002a).

Crust-based TRFs are those currently determined in IERS activities, either by analysis centers or by combination centers, and ultimately as IERS products (see Section 4.1.5).

The general model connecting the instantaneous position of a point anchored on the Earth’s crust at epoch $t$ , $\vec { X } ( t )$ , and a regularized position $\vec { X _ { R } } ( t )$ is

$$
\Vec { X } ( t ) = \Vec { X } _ { R } ( t ) + \sum _ { i } \Delta \Vec { X } _ { i } ( t ) .
$$

The purpose of the introduction of a regularized position is to remove highfrequency time variations (mainly geophysical ones) using conventional corrections $\Delta \vec { X _ { i } } ( t )$ , in order to obtain a position with more regular time variation.

It is essential that the same conventional models be adopted and used by all analysis centers dealing with space geodesy data. The currently adopted models are described in Chapter 7.

# 4.1.4 The International Terrestrial Reference System

The IERS is in charge of defining, realizing and promoting the International Terrestrial Reference System (ITRS). The ITRS has been recently formally adopted by the IUGG at its General Assembly in Perugia (2007), through its Resolution 2 (see Appendix C).

To summarize and synthesize these legal texts (IAG and IUGG resolutions of 1991 and 2007, consistent with latest IAU Resolutions)

• GTRS (geocentric terrestrial reference system) is the new designation of CTRS (conventional terrestrial reference system), while the term CTRS is now used as a generic term to designate the identification of a specific TRS through a list of conventional rules fixing the origin, scale and orientation. • The GTRS origin is the geocenter, considered for the whole Earth system body, including oceans and atmosphere. • The GTRS time coordinate is TCG (Geocentric Coordinate Time). Therefore, the scale of the spatial coordinates is consistent with this fact. The time evolution of the orientation of GTRS follows a no-net-rotation (NNR) condition with regards to the horizontal Earth surface.

In fact, the IAG Resolution of 1991, as well as various scientific and practical considerations, led explicitly to defining the ITRS as three-dimensional. For example, we note that accurate geophysical models are presently developed within the Newtonian framework and that all practical applications (mapping, navigation) consider ITRS as a three-dimensional system.

The Perugia text should be read in such a way that the ITRS is assimilated to the spatial part of GTRS (and not to the 4d coordinate system). Following the previous summary, the ITRS is therefore fully fixed, considering the statement that its orientation fulfills the international agreements (Bureau International de l’Heure (BIH) orientation). The practical procedure adopted by the IERS at the beginning of its work led to the consideration that the ITRS orientation coincides with the previous BIH system at the epoch 1984.0.

The ITRS definition fulfills the following conditions:

1. It is geocentric, its origin being the center of mass for the whole Earth, including oceans and atmosphere;   
2. The unit of length is the meter (SI). The scale is consistent with the TCG time coordinate for a geocentric local frame, in agreement with IAU and IUGG (1991) resolutions. This is obtained by appropriate relativistic modeling;   
3. Its orientation was initially given by the BIH orientation at 1984.0;   
4. The time evolution of the orientation is ensured by using a no-net-rotation condition with regards to horizontal tectonic motions over the whole Earth.

# 4.1.5 Realizations of the ITRS

Primary realizations of the ITRS are produced by the IERS ITRS Center (ITRS-PC) under the name International Terrestrial Reference Frame (ITRF). Twelve ITRF versions were produced, starting with ITRF88 and ending with the ITRF2008. Up to the ITRF2000 solution, long-term global solutions (comprising station positions and velocities) from four techniques (VLBI, SLR, GPS and DORIS) were used as input for the ITRF generation. As described in more detail later, starting with the ITRF2005, time series of station positions and Earth Orientation Parameters (EOPs) are used as input data for the ITRF construction. The current procedure is to combine the technique TRF solutions using a combination model which is essentially based on the transformation formulas (4.3) and (4.5). The combination method makes use of local ties in co-location sites where two or more geodetic techniques are operated. The local ties are used as additional observations with proper variances. They are usually derived from local surveys using either classical geodesy or the global navigation satellite systems (GNSS). As they represent a key element of the ITRF combination, they should be more, or at least as accurate as the individual space geodesy solutions incorporated in the ITRF combination.

Up to ITRF2000 ITRF solutions were published by the ITRS-PC in Technical Notes (cf. Boucher et al., 1996, 1998, 1999, 2004). The number following the designation “ITRF” specifies the last year whose data were used for the formation of the frame. Hence, ITRF2008 designates the frame of station positions and velocities constructed in 2010 using data available until the end of 2008 (2009.5 for GPS).

The current ITRF model is linear (position at a reference epoch $t _ { 0 }$ and velocity). Therefore, the station position at an epoch $t$ is expressed as:

$$
\vec { X } ( t ) = \vec { X } _ { 0 } + \dot { \vec { X } } \cdot ( t - t _ { 0 } ) .
$$

The numerical values are $( \vec { X } _ { 0 } , \dot { \vec { X } } )$ . In the past (ITRF88 and ITRF89), constant positions were used as models ${ \vec { X } } _ { 0 }$ ), the linear motion being incorporated as conventional corrections derived from a tectonic plate motion model (see Section 4.2.2).

The reader may also refer to an earlier report of the ITRF Working Group on the ITRF Datum (Ray et al., 1999), which contains useful information related to the history of the ITRF datum definition. It also details technique-specific effects on some parameters of the datum definition, in particular the origin and the scale. More details on the formation of ITRF2000 and ITRF2005 are available in Altamimi et al. (2002b, 2007).

# 4.2 ITRF products

# 4.2.1 The IERS network

# The initial definition of the IERS network

The IERS network was initially defined through all tracking instruments used by the various individual analysis centers contributing to the IERS. All SLR, LLR and VLBI systems were included. Eventually, GPS stations from the IGS were added as well as the DORIS tracking network. The network also included, from its beginning, a selection of ground markers, specifically those used for mobile equipment and those currently included in local surveys performed to monitor local eccentricities between instruments for co-location sites or for site stability checks.

Each point is currently identified by the assignment of a DOMES (Directory of MERIT Sites) number. The explanation of the DOMES numbering system is given below. Close points are clustered into one site. The current rule is that all points which could be linked by a co-location survey (up to $3 0 ~ \mathrm { k m }$ ) should be included into the IERS network as a unique site having a unique DOMES site number. In reality, for a local tie to be precise at the 1 mm level, the extension of a co-location site should not exceed 1 km.

# Co-locations

In the frame of the IERS, the concept of co-location can be defined as the fact that two instruments are occupying simultaneously or subsequently very close locations that are very precisely surveyed in three dimensions. These include situations such as simultaneous or non-simultaneous measurements and instruments of the same or different techniques. Usually, co-located points should belong to a unique IERS site.

# Extensions of the IERS network

Following the requirements of various user communities, the initial IERS network was expanded to include new types of systems which are of potential interest. Consequently, the current types of points allowed in the IERS and for which a DOMES number can be assigned are (IERS uses a one character code for each type):

• L for satellite laser ranging (SLR),   
• M for lunar laser ranging (LLR),   
• R for very long baseline interferometry (VLBI),   
• P for global navigation satellite systems (GNSS),   
• D for d´etermination d’orbite et radiopositionnement int´egr´es par satellite (DO-RIS; also Doppler Navy Navigation Satellite System (NNSS) in the past), • A for optical astrometry (formerly used by the BIH),   
• X for precise range and range rate equipment (PRARE),   
• T for tide gauge,   
• W for meteorological sensor.

For instance, the cataloging of tide gauges co-located with IERS instruments, in particular GNSS or DORIS, is of interest for the Global Sea Level Observing System (GLOSS) program under the auspices of UNESCO.

Another application is to collect accurate meteorological surface measurements, in particular atmospheric pressure, in order to derive raw tropospheric parameters from tropospheric propagation delays that can be estimated during the processing of radio measurements, e.g. made by the GNSS, VLBI, or DORIS. Other systems could also be considered, if it was regarded as useful (for instance systems for time transfer, super-conducting or absolute gravimeters, etc.).

Another important extension is the wish of some continental or national organizations to see their fiducial networks included into the IERS network, either to be computed by IERS (for instance the European Reference Frame (EUREF) permanent GNSS network) or at least to get DOMES numbers (for instance the Continuously Operating Reference Stations (CORS) network in the USA).

# 4.2.2 History of ITRF products

The history of the ITRF goes back to 1984, when for the first time a combined TRF (called BIH Terrestrial System 1984 BTS84) was established using station coordinates derived from VLBI, LLR, SLR and Doppler/TRANSIT (the predecessor of GPS) observations (Boucher and Altamimi, 1985). BTS84 was realized in the framework of the activities of BIH, being a coordinating center for the international MERIT project (Monitoring of Earth Rotation and Intercomparison of Techniques; Wilkins, 2000). Three other successive BTS realizations were then achieved, ending with BTS87, before in 1988, the IERS was created by the IUGG and the IAU.

Until the time of writing, twelve versions of the ITRF were published, starting with ITRF88 and ending with ITRF2008, each of which superseded its predecessor.

From ITRF88 till ITRF93, the ITRF datum definition can be summarized as follows:

• Origin and scale: defined by an average of selected SLR solutions;

• Orientation: defined by successive alignment since BTS87 whose orientation was aligned to the BIH EOP series. Note that the ITRF93 orientation and its rate were again realigned to the IERS EOP series;   
• Orientation time evolution: No global velocity field was estimated for ITRF88, ITRF89 and ITRF90, so the AM0-2 model of Minster and Jordan (1978) was recommended. Starting with ITRF91 and till ITRF93, combined velocity fields were estimated. The ITRF91 orientation rate was aligned to that of the NNR-NUVEL-1 model (Argus and Gordon, 1991), and ITRF92 to NNR-NUVEL-1A, adapted from NNR-NUVEL-1 according to DeMets et al. (1994), while ITRF93 was aligned to the IERS EOP series.

Since the ITRF94, full variance matrices of the individual solutions incorporated in the ITRF combination have been used. At that time, the ITRF94 datum was achieved as follows (Boucher et al., 1996):

• Origin: defined by a weighted mean of selected SLR and GPS solutions;   
• Scale: defined by a weighted mean of VLBI, SLR and GPS solutions, corrected by 0.7 ppb to meet the IUGG and IAU requirement to be compatible with TCG, while analysis centers provide solutions that are compatible with TT (Terrestrial Time);   
• Orientation: aligned to the ITRF92;   
• Orientation time evolution: velocity field aligned to the model NNR-NUVEL-1A, using the 7 rates of the transformation parameters.

The ITRF96 was then aligned to the ITRF94, and the ITRF97 to the ITRF96 using the 14 transformation parameters (Boucher et al., 1998; 1999).

The ITRF2000 was intended to be a standard solution for geo-referencing and all Earth science applications. Therefore, in addition to primary core stations observed by VLBI, LLR, SLR, GPS and DORIS, the ITRF2000 was densified by regional GPS networks in Alaska, Antarctica, Asia, Europe, North and South America and the Pacific.

The individual solutions used for the ITRF2000 combination were generated by the IERS analysis centers using removable, loose or minimum constraints.

In terms of datum definition, the ITRF2000 is characterized by the following properties:

• Origin: realized by setting to zero the translation components and their rates between ITRF2000 and a weighted average of the most consistent SLR solutions; Scale: realized by setting to zero the scale and scale rate parameters between ITRF2000 and a weighted average of VLBI and the most consistent SLR solutions. Unlike the ITRF97 scale which is compatible with TCG, that of the ITRF2000 is compatible with TT;   
• Orientation: aligned to that of the ITRF97 at 1997.0;   
• Orientation time evolution: aligned, conventionally, to that of the geological model NNR-NUVEL-1A (Argus and Gordon, 1991; DeMets et al., 1990; 1994).

The ITRF network has improved with time in terms of the number of sites and colocations as well as their distribution over the globe. Figure 4.1 shows the ITRF88 network including about 100 sites and 22 co-locations (VLBI/SLR/LLR), and the ITRF2008 network containing 580 sites and 105 co-locations (VLBI/SLR/GPS/- DORIS).

For the first time in ITRF history, the ITRF2005 used as input data time series of station positions (weekly from satellite techniques and 24-hour session-wise from VLBI) and daily EOPs. One set of time series per space geodesy technique was considered as input to the ITRF2005 combination. These solutions are the official time series provided by the international services of the 4 techniques, known as Technique Centers (TC) within the IERS. Note that these official TC solutions result from a combination at the weekly (daily) basis of the corresponding individual solutions provided by the analysis centers participating in the activities of each TC. Official time series were submitted to the ITRF2005 by the International VLBI Service for Geodesy and Astrometry (IVS), the International Laser Ranging Service (ILRS) and the International GNSS Service (IGS). At the time of the ITRF2005 release, official weekly combined solutions from the International DORIS Service (IDS) were not available, so that individual solutions were submitted by two DORIS analysis centers. For more details the reader may refer to Altamimi et al. (2007).

![](../chunks/IERS Conventions (2010), IERS Technical Note No.36_part_0001_pages_0001-0070/auto/images/76c5e2eaf588a52dfd295864d7772bdf039d721318508ea2157582180b8c153e.jpg)  
Figure 4.1: ITRF88 (left) and ITRF2008 (right) sites and co-located techniques.

The ITRF2005 generation consisted of two steps: (1) stacking the individual time series to estimate a long-term solution per technique comprising station positions at a reference epoch and velocities as well as daily EOPs; and (2) combining the resulting long-term solutions of the four techniques together with the local ties in co-location sites. Therefore, in addition to the usual ITRF products (station positions and velocities), other important ITRF2005 results are also available to the users, namely:

1. full ITRF2005 and per technique SINEX files containing station positions, velocities and EOPs with complete variance-covariance matrices; 2. time series of station position residuals resulting from the stacking of the individual time series of the 4 techniques; 3. geocenter time series from SLR and DORIS. There is no useful geocenter motion information from GPS/IGS because it has been removed ${ < } ^ { 1 } >$ , the submitted weekly solutions being aligned to ITRF2000; 4. full time series of EOPs consistent with the ITRF2005.

The ITRF2005 origin is defined in such a way that it has zero translations and translation rates with respect to the Earth center of mass, averaged by the SLR time series spanning 13 years of observations. Its scale is defined by nullifying the scale and its rate with respect to the VLBI time series spanning 26 years of observations. It should be noted that after the release of the ITRF2005 it was discovered that the IVS VLBI solutions used for the ITRF2005 construction did not include pole tide corrections referenced to the mean pole path recommended by the IERS Conventions 2003. Post-ITRF2005 analyses of IVS solutions where the mean pole tide correction was applied revealed a constant scale offset of -0.5 ppb with respect to the IVS solutions used for ITRF2005 (Altamimi and Collilieux, 2008). The ITRF2005 orientation (at epoch 2000.0) and its rate are aligned to ITRF2000 using 70 stations of high geodetic quality.

# 4.2.4 ITRF2008, the current reference realization of the ITRS

Following the same strategy initiated with the ITRF2005 release, the ITRF2008 is a refined solution based on reprocessed solutions of four space geodesy techniques: VLBI, SLR, GPS and DORIS, spanning 29, 26, 12.5 and 16 years of observations, respectively.

The ITRF2008 is composed of 934 stations located at 580 sites as illustrated in Fig. 4.1, with an imbalanced distribution between the northern (463 sites) and the southern hemisphere (117 sites).

As illustrated by Fig. 4.1, there are in total 105 co-location sites; 91 of these have local ties available for the ITRF2008 combination. Note that, unfortunately, not all these co-located instruments are currently operating. For instance, among the 6 sites having 4 techniques, only two are currently fully operational: Hartebeesthoek, South Africa and Greenbelt, MD, USA.

The ITRF2008 is specified by the following frame parameters:

• Origin: The ITRF2008 origin is defined in such a way that there are zero translation parameters at epoch 2005.0 and zero translation rates with respect to the ILRS SLR time series.   
• Scale: The scale of the ITRF2008 is defined in such a way that there is a zero scale factor at epoch 2005.0 and a zero scale rate with respect to the mean scale and scale rate of VLBI and SLR time series.   
• Orientation: The ITRF2008 orientation is defined in such a way that there are zero rotation parameters at epoch 2005.0 and zero rotation rates between ITRF2008 and ITRF2005. These two conditions are applied over a set of 179 reference stations located at 131 sites, including 107 GPS, 27 VLBI, 15 SLR and 12 DORIS sites.

# 4.2.5 ITRF as a realization of the ITRS

The procedure used by the IERS to determine ITRF products includes the following steps:

1. definition of individual TRF used by contributing analysis centers. This implies knowing the particular conventional corrections adopted by each analysis center;   
2. determination of the ITRF by the combination of individual TRF and datum fixing. This implies the adoption of a set of conventional corrections for the ITRF and ensures the consistency of the combination by removing possible differences between corrections adopted by each contributing analysis center.

Meanwhile, for various reasons, there are particular cases where users would need to add specific corrections to ITRF coordinates in order to meet their particular applications. The currently identified cases are the following:

# A) Solid Earth tides

To account for the displacement due to solid Earth tides, all analysis centers use a model $\Delta \vec { X } _ { t i d M }$ that contains a time-independent part, so that the regularized positions obtained are termed “conventional tide-free”, according to the nomenclature in the Introduction of the Conventions. Such a hypothesis has been taken since the first solid Earth tides model of the MERIT Standards. Consequently, the ITRF has adopted the same option and is therefore a “conventional tidefree” frame. To adopt a different model, $\Delta \vec { X } _ { t i d }$ , a user would need to apply the following formula to obtain coordinates $\vec { X }$ consistent with this model:

$$
\vec { X } = \vec { X } _ { I T R F } + ( \Delta \vec { X } _ { t i d } - \Delta \vec { X } _ { t i d M } ) .
$$

For more details concerning tidal corrections, see Chapter 7.

# B) Relativistic scale

All individual centers use a scale consistent with TT. In the same manner the ITRF has also adopted this option (except ITRF94, 96 and 97, see Section 4.2.2).

It should be noted that the ITRS scale is specified to be consistent with TCG. Consequently, if coordinates $\vec { X }$ consistent with TCG are needed, users need to apply the following formula:

$$
\vec { X } = ( 1 + L _ { G } ) \vec { X } _ { I T R F }
$$

where $L _ { G }$ is according to Table 1.1 in Chapter 1. Note that consistency between numerical constants should be ensured as described in Chapter 1.

# C) Geocentric positions

The ITRF origin should be considered as the mean Earth center of mass, averaged over the time span of the SLR observations used and modeled as a secular (linear) function of time. If an instantaneous geocentric position $\vec { X }$ is required, it should be computed as

$$
\vec { X } = \vec { X } _ { I T R F } - \vec { O } _ { G } ,
$$

where $\vec { O } _ { G }$ represents the geocenter motion in ITRF (vector from the ITRF origin to the instantaneous center of mass) ${ < } ^ { 2 } >$ .

# 4.2.6 Transformation parameters between ITRF solutions

Table 4.1 lists transformation parameters and their rates from ITRF2008 to previous ITRF versions, which should be used with Equations (4.3) and (4.5). The values listed in this table have been compiled from those already published in previous IERS Technical Notes as well as from ITRF97/ITRF2000, ITRF2000/ITRF2005 and ITRF2005/ITRF2008 comparisons. Moreover, it should be noted that these parameters are adjusted values which are heavily dependent on the weighting as well as the number and distribution of the implied common sites between these frames. Therefore, using different subsets of common stations between two ITRF solutions to estimate transformation parameters would not necessarily yield values consistent with those of Table 4.1.

ITRF solutions are specified by Cartesian equatorial coordinates $X$ , $Y$ and $Z$ . If needed, they can be transformed to geographical coordinates $( \lambda , \phi , h )$ referred to an ellipsoid. In this case the GRS80 ellipsoid is recommended (semi-major axis $a = 6 3 7 8 1 3 7 . 0 \mathrm { m }$ , inverse flattening $1 / f = 2 9 8 . 2 5 7 2 2 2 1 0 1$ , see Table 1.2 in Chapter 1). See the IERS Conventions’ web page for the subroutine, GCONV2.F, at ${ < } ^ { 3 } >$ . The SOFA (Standards of Fundamental Astronomy) service ${ < } ^ { 4 } >$ also provides a routine iau GC2GDE in both Fortran 77 and ANSI C to perform the transformation.

# 4.3 Access to the ITRS

Several ways could be used to express point positions in the ITRS, e.g.

• direct use of ITRF station positions and velocities;   
• use of IGS products (e.g. orbits and clocks) which are nominally all referred to the ITRF. However, users should be aware of the ITRF version used for the generation of the IGS products.   
• fixing or constraining some ITRF station coordinates in the analysis of GNSS measurements of campaign or permanent stations;   
• use of transformation formulas which would be estimated between a particular TRF and an ITRF solution.

Other useful details are also available in Boucher and Altamimi (1996). All information on ITRF solutions since ITRF94 may be found at $< ^ { 5 } >$ .

Table 4.1: Transformation parameters from ITRF2008 to past ITRFs. “ppb” refers to parts per billion (or $1 0 ^ { - 9 }$ ). The units for rates are understood to be “per year.”   

<table><tr><td colspan="9">ITRF</td></tr><tr><td>Solution</td><td>T1</td><td>T2</td><td>T3</td><td>D</td><td>R1</td><td>R2</td><td>R3</td><td></td></tr><tr><td></td><td>(mm)</td><td>(mm)</td><td>(mm)</td><td>(ppb)</td><td>(mas)</td><td>(mas)</td><td>(mas)</td><td>Epoch</td></tr><tr><td>ITRF2005</td><td>-2.0</td><td>-0.9</td><td>-4.7</td><td>0.94</td><td>0.00</td><td>0.00</td><td>0.00</td><td>2000.0</td></tr><tr><td>rates</td><td>0.3</td><td>0.0</td><td>0.0</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td></td></tr><tr><td>ITRF2000</td><td>-1.9</td><td>-1.7</td><td>-10.5</td><td>1.34</td><td>0.00</td><td>0.00</td><td>0.00</td><td>2000.0</td></tr><tr><td>rates</td><td>0.1</td><td>0.1</td><td>-1.8</td><td>0.08</td><td>0.00</td><td>0.00</td><td>0.00</td><td></td></tr><tr><td>ITRF97</td><td>4.8</td><td>2.6</td><td>-33.2</td><td>2.92</td><td>0.00</td><td>0.00</td><td>0.06</td><td>2000.0</td></tr><tr><td>rates</td><td>0.1</td><td>-0.5</td><td>-3.2</td><td>0.09</td><td>0.00</td><td>0.00</td><td>0.02</td><td></td></tr><tr><td>ITRF96</td><td>4.8</td><td>2.6</td><td>-33.2</td><td>2.92</td><td>0.00</td><td>0.00</td><td>0.06</td><td>2000.0</td></tr><tr><td>rates</td><td>0.1</td><td>-0.5</td><td>-3.2</td><td>0.09</td><td>0.00</td><td>0.00</td><td>0.02</td><td></td></tr><tr><td>ITRF94</td><td>4.8</td><td>2.6</td><td>-33.2</td><td>2.92</td><td>0.00</td><td>0.00</td><td>0.06</td><td>2000.0</td></tr><tr><td>rates</td><td>0.1</td><td>-0.5</td><td>-3.2</td><td>0.09</td><td>0.00</td><td>0.00</td><td>0.02</td><td></td></tr><tr><td>ITRF93</td><td>-24.0</td><td>2.4</td><td>-38.6</td><td>3.41</td><td>-1.71</td><td>-1.48</td><td>-0.30</td><td>2000.0</td></tr><tr><td>rates</td><td>-2.8</td><td>-0.1</td><td>-2.4</td><td>0.09</td><td>-0.11</td><td>-0.19</td><td>0.07</td><td></td></tr><tr><td>ITRF92</td><td>12.8</td><td>4.6</td><td>-41.2</td><td>2.21</td><td>0.00</td><td>0.00</td><td>0.06</td><td>2000.0</td></tr><tr><td>rates</td><td>0.1</td><td>-0.5</td><td>-3.2</td><td>0.09</td><td>0.00</td><td>0.00</td><td>0.02</td><td></td></tr><tr><td>ITRF91</td><td>24.8</td><td>18.6</td><td>-47.2</td><td>3.61</td><td>0.00</td><td>0.00</td><td>0.06</td><td>2000.0</td></tr><tr><td>rates</td><td>0.1</td><td>-0.5</td><td>-3.2</td><td>0.09</td><td>0.00</td><td>0.00</td><td>0.02</td><td></td></tr><tr><td>ITRF90</td><td>22.8</td><td>14.6</td><td>-63.2</td><td>3.91</td><td>0.00</td><td>0.00</td><td>0.06</td><td>2000.0</td></tr><tr><td>rates</td><td>0.1</td><td>-0.5</td><td>-3.2</td><td>0.09</td><td>0.00</td><td>0.00</td><td>0.02</td><td></td></tr><tr><td>ITRF89</td><td>27.8</td><td>38.6</td><td>-101.2</td><td>7.31</td><td>0.00</td><td>0.00</td><td>0.06</td><td>2000.0</td></tr><tr><td>rates</td><td>0.1</td><td>-0.5</td><td>-3.2</td><td>0.09</td><td>0.00</td><td>0.00</td><td>0.02</td><td></td></tr><tr><td>ITRF88</td><td>22.8</td><td>2.6</td><td>-125.2</td><td>10.41</td><td>0.10</td><td>0.00</td><td>0.06</td><td>2000.0</td></tr><tr><td>rates</td><td>0.1</td><td>-0.5</td><td>-3.2</td><td>0.09</td><td>0.00</td><td>0.00</td><td>0.02</td><td></td></tr></table>

# References

Altamimi, Z., Boucher, C., and Sillard, P., 2002a, “New trends for the realization of the International Terrestrial Reference System,” Adv. Space Res., 30(2), pp. 175–184, doi: 10.1016/S0273-1177(02)00282-X.   
Altamimi, Z., Sillard, P., and Boucher, C., 2002b,“ITRF2000: A new release of the International Terrestrial Reference Frame for Earth science applications,” J. Geophys. Res., 107(B10), 19 pp., doi: 10.1029/2001JB000561.   
Altamimi, Z., Collilieux, X., Legrand, J., Garayt, B., and Boucher, C., 2007, “ITRF2005: A new release of the International Terrestrial Reference Frame based on time series of station positions and Earth Orientation Parameters,” J. Geophys. Res., 112(B9), B09401, 19 pp., doi: 10.1029/2007JB004949.   
Altamimi , Z., and Collilieux, X., 2009, “Institut G´eographique National (IGN) Combination Center,” in IERS Annual Report 2007, Dick, W. R., Richter, B. (eds.), Bundesamt f¨ur Kartographie und Geod¨asie, Frankfurt/Main, pp. 130–132.   
Argus, D. F., and Gordon, R. G., 1991, “No-net-rotation model of current plate velocities incorporating plate motion model NUVEL-1,” Geophys. Res. Lett., 18(11), pp. 2039–2042, doi: 10.1029/91GL01532.   
Boucher, C., 1986, “Relativistic effects in geodynamics,” in Relativity in Celestial Mechanics and Astrometry, Kovalevsky, J. and Brumberg, V. A. (eds.), Reidel, pp. 241–253.   
Boucher, C., 2001, “Terrestrial coordinate systems and frames,” in Encyclopedia of Astronomy and Astrophysics, Version 1.0, Nature Publishing Group, and Bristol: Institute of Physics Publishing, pp. 3289–3292, doi: 10.1888/0333750888/1906.   
Boucher, C., and Altamimi, Z., 1985, “Towards an improved realization of the BIH terrestrial frame,” The MERIT/COTES Report on Earth Rotation and Reference Frames, Vol. 2, Mueller, I. I. (ed.), OSU/DGS, Columbus, Ohio, USA.   
Boucher, C., and Altamimi, Z., 1996, “International Terrestrial Reference Frame,” GPS World, 7(9), pp. 71–74.   
Boucher, C., Altamimi, Z., Feissel, M., and Sillard, P., 1996, “Results and analysis of the ITRF94,” IERS Technical Note, 20, Observatoire de Paris, Paris,, available at http://www.iers.org/TN20   
Boucher, C., Altamimi, Z., and Sillard, P., 1998, “Results and analysis of the ITRF96,” IERS Technical Note, 24, Observatoire de Paris, Paris, available at http://www.iers.org/TN24   
Boucher, C., Altamimi, Z., Sillard, P., and Feissel-Vernier, M., 2004, “The ITRF-2000,” IERS Technical Note, 31, Verlag des Bundesamts f¨ur Kartographie und Geod¨asie, available at http://www.iers.org/TN31   
Boucher, C., Altamimi, Z., and Sillard, P., 1999, “The 1997 International Terrestrial Reference Frame (ITRF97),” IERS Technical Note, 27, Observatoire de Paris, Paris,, available at http://www.iers.org/TN27   
DeMets, C., Gordon, R. G., Argus, D. F., and Stein, S., 1990, “Current plate motions,” Geophys. J. Int., 101(2), pp. 425–478, doi: 10.1111/j.1365- 246X.1990.tb06579.x.   
DeMets, C., Gordon, R. G., Argus, D. F., and Stein, S., 1994, “Effect of recent revisions to the geomagnetic reversal time scale on estimates of current plate motions,” Geophys. Res. Lett., 21(20), pp. 2191–2194, doi: 10.1029/94GL02118.   
Minster, J. B., and Jordan, T. H., 1978, “Present-day plate motions,” J. Geophys. Res., 83(B11), pp. 5331–5354, doi: 10.1029/JB083iB11p05331.   
Ray, J., Blewitt, G., Boucher, C., Eanes, R., Feissel, M., Heflin, M., Herring, T., Kouba, J., Ma, C., Montag, H., Willis, P., Altamimi, Z., Eubanks, T. M., Gambis, D., Petit, G., Ries, J., Scherneck, H.-G., and Sillard, P., 1999, “Report of the Working Group on ITRF datum.”   
Sillard, P., and Boucher, C., 2001, “A review of algebraic constraints in terrestrial reference frame datum definition,” J. Geod., 75(2-3), pp. 63–73, doi: 10.1007/s001900100166.   
Wilkins, G. A. (ed.), 2000, “Report on the third MERIT workshop and the MERIT-COTES joint meeting,” Part 1, Columbus, Ohio, USA, 29–30 July and 3 August 1985, Scientific Technical Report STR 99/25, GeoForschungs-Zentrum Potsdam.

# 5 Transformation between the International Terrestrial Reference System and the Geocentric Celestial Reference System

# 5.1 Introduction

The transformation to be used to relate the International Terrestrial Reference System (ITRS) to the Geocentric Celestial Reference System (GCRS) at the date $t$ of the observation can be written as:

$$
[ \mathrm { G C R S } ] = Q ( t ) R ( t ) W ( t ) ~ [ \mathrm { I T R S } ] ,
$$

where $Q ( t )$ , $R ( t )$ and $W ( t )$ are the transformation matrices arising from the motion of the celestial pole in the celestial reference system, from the rotation of the Earth around the axis associated with the pole, and from polar motion respectively.

Note that Eq. (5.1) is valid for any choice of celestial pole and origin on the equator of that pole.

The definition of the GCRS and ITRS and the procedures for the ITRS to GCRS transformation that are provided in this chapter comply with the IAU 2000/2006 resolutions (provided at ${ < } ^ { 1 } >$ and in Appendix B). More detailed explanations about the relevant concepts, software and IERS products corresponding to the IAU 2000 resolutions can be found in IERS Technical Note 29 (Capitaine et al., 2002), as well as in a number of original subsequent publications that are quoted in the following sections.

The chapter follows the recommendations on terminology associated with the IAU 2000/2006 resolutions that were made by the 2003-2006 IAU Working Group on “Nomenclature for fundamental astronomy” (NFA) (Capitaine et al., 2007). We will refer to those recommendations in the following as “NFA recommendations” (see Appendix A for the list of the recommendations). This chapter also uses the definitions that were provided by this Working Group in the “IAU 2006 NFA Glossary”(available at   
http://syrte.obspm.fr/iauWGnfa/).

Eq. (5.1), as well as the following formulas in this chapter, are theoretical formulations that refer to reference “systems”. However, it should be clear that the numerical implementation of those formulas involves the IAU/IUGG adopted realization of those reference systems, i.e. the International Terrestrial Reference Frame (ITRF) and the International Celestial Reference Frame (ICRF), respectively.

Numerical values contained in this chapter have been revised from the IERS 2003 values in order to be compliant with the IAU 2006 precession. Software routines implementing the transformations are described towards the end of the chapter.

The transformation between the celestial and terrestrial reference systems also being required for computing directions of celestial objects in intermediate systems, the process to transform among these systems consistently with the IAU resolutions is also set out at the end of this chapter, including a chart provided by the IAU NFA Working Group in order to illustrate the various stages of the process.

# 5.2 The framework of IAU 2000/2006 resolutions

Several resolutions were adopted by the XXIVth and XXVIth General Assemblies of the International Astronomical Union (Manchester, August 2000, and Prague, August 2006) that concern the transformation between the celestial and terrestrial reference systems (see 1 and Appendix B for the complete text of those resolutions). Those resolutions were endorsed by the IUGG in 2003 and 2007, respectively.

The IAU 2000 resolutions ${ } ^ { - 1 } > { }$ ) that are relevant to this chapter are described in the following:

• IAU 2000 Resolution B1.3 specifies that the systems of space-time coordinates as defined by IAU 1991 Resolution A4 for the solar system and the Earth within the framework of General Relativity are now named the Barycentric Celestial Reference System (BCRS) and the Geocentric Celestial Reference System (GCRS) respectively. It also provides a general framework for expressing the metric tensor and defining coordinate transformations at the first post-Newtonian level.

• IAU 2000 Resolution B1.6 recommends that, beginning on 1 January 2003, the IAU 1976 precession model (Lieske et al., 1977) and the IAU 1980 theory of nutation (Wahr, 1981; Seidelmann, 1982) be replaced by the precessionnutation model IAU 2000A (MHB2000 based on the transfer functions of Mathews et al. (2002)) for those who need a model at the 0.2 mas level, or its shorter version IAU 2000B for those who need a model only at the 1 mas level, together with their associated celestial pole offsets, published in this document. See Dehant et al. (1999) for more details. In addition to that model are frame bias values between the mean pole and equinox at J2000.0 and the GCRS.

The precession part of the IAU 2000A model consists only of corrections to the precession rates of the IAU 1976 precession, and hence does not correspond to a dynamical theory. This is why IAU 2000 Resolution B1.6, that recommended the IAU 2000A precession-nutation model, encouraged at the same time the development of new expressions for precession consistent with dynamical theories and with IAU 2000A nutation.

• IAU 2000 Resolution B1.7 recommends that the Celestial Intermediate Pole (CIP) be implemented in place of the Celestial Ephemeris Pole (CEP) as of 1 January 2003, and specifies how to implement its definition through its direction at $J 2 0 0 0 . 0$ in the GCRS as well as the realization of its motion both in the GCRS and ITRS. Its definition is an extension of that of the CEP in the high frequency domain and coincides with that of the CEP in the low frequency domain (Capitaine, 2000).

• For longitude origins on the CIP equator in the celestial and the terrestrial reference systems, IAU 2000 Resolution B1.8 recommends the “non-rotating origin” (Guinot, 1979). They were designated Celestial Ephemeris Origin and Terrestrial Ephemeris Origin , but renamed Celestial Intermediate Origin and Terrestrial Intermediate Origin, respectively, by IAU 2006 Resolution B2 (see below).

The “Earth Rotation Angle” (ERA) is defined as the angle measured along the equator of the CIP between the CIO and the TIO, and UT1 is defined by a conventionally adopted linear proportionality to the ERA. IAU 2000 Resolution B1.8 also recommends that the transformation between the ITRS and GCRS be specified by the position of the CIP in the GCRS, the position of the CIP in the ITRS, and the Earth Rotation Angle. It was finally recommended that the IERS take steps to implement this by 1 January 2003 and that the IERS continue to provide users with data and algorithms for the conventional transformation.

IAU 2000 Resolutions B1.6, B1.7 and B1.8 came into force on 1 January 2003. By that time, the required models, procedures, data and software had been made available by the IERS Conventions 2003 and the Standards Of Fundamental Astronomy (SOFA) service (Section 5.9 and Wallace, 1998) and the resolutions were implemented operationally.

# 5.2.2 IAU 2006 resolutions

The IAU 2006 resolutions (cf. Appendix B) that are relevant to this chapter are the following:

• IAU 2006 Resolution B1, proposed by the 2003-2006 IAU Working Group on “Precession and the Ecliptic” (Hilton et al., 2006), recommends that, beginning on 1 January 2009, the precession component of the IAU 2000A precession-nutation model be replaced by the P03 precession theory of Capitaine et al. (2003c) in order to be consistent with both dynamical theories and the IAU 2000 nutation. We will refer to that model as “IAU 2006 precession”. That resolution also clarifies the definitions of the precession of the equator and the precession of the ecliptic.   
• IAU 2006 Resolution B2, which is a supplement to the IAU 2000 resolutions on reference systems, consists of two recommendations: 1. harmonizing “intermediate” in the names of the pole and the origin (i.e. celestial and terrestrial intermediate origins, CIO and TIO instead of CEO and TEO, respectively) and defining the celestial and terrestrial “intermediate” systems; and 2. fixing the default orientation of the BCRS and GCRS, which are, unless otherwise stated, assumed to be oriented according to the ICRS axes.

The IAU precession-nutation model resulting from IAU 2000 Resolution B1.6 and IAU 2006 Resolution B1, will be denoted IAU 2006/2000 precession-nutation in the following. A description of that model is given in Section 5.6.1 and Section 5.6.2.

# 5.3 Implementation of IAU 2000 and IAU 2006 resolutions

# 5.3.1 The IAU 2000/2006 space-time reference systems

In order to follow IAU 2000 Resolution B1.3, the celestial reference system to be considered in the terrestrial-to-celestial transformation expressed by Eq. (5.1) must correspond to the geocentric space coordinates of the GCRS. IAU 1991 Resolution A4 specified that the relative orientation of barycentric and geocentric spatial axes in BCRS and GCRS are without any time-dependent rotation. This requires that the geodesic precession and nutation be taken into account in the precession-nutation model. Moreover, IAU 2006 Resolution B2 specifies that the BCRS and GCRS are oriented according to the ICRS axes.

Concerning the time coordinates, IAU 1991 Resolution A4 defined TCB and TCG of the BCRS and GCRS respectively, as well as another time coordinate in the GCRS, Terrestrial Time (TT), which is the theoretical counterpart of the realized time scale $\mathrm { \Delta T A I } + \mathrm { 3 2 . 1 8 4 } \ \mathrm { \Omega }$ s. The IAU 2000/2006 resolutions have clarified the definition of the two time scales TT and TDB. TT has been re-defined (IAU 2000 Resolution B1.9) as a time scale differing from TCG by a constant rate, which is a defining constant. In a very similar way, TDB has been re-defined (IAU 2006 Resolution B3) as a linear transformation of TCB, the coefficients of which are defining constants. See Chapter 10 for the relationships between these time scales. The parameter $t$ , used in Eq. (5.1) as well as in the following expressions, is defined by

$$
t = \mathrm { ( T T - 2 0 0 0 ~ J a n u a r y ~ 1 d ~ 1 2 h ~ T T ) ~ i n ~ d a y s / 3 6 5 2 5 . }
$$

This definition is consistent with IAU 1994 Resolution C7 which recommends that the epoch J2000.0 be defined at the geocenter and at the date 2000 January 1.5 TT = Julian Date 2451545.0 TT.

# 5.3.2 Schematic representation of the motion of the Celestial Intermediate Pole (CIP)

According to IAU 2000 Resolution B1.7, the CIP is an intermediate pole separating, by convention, the motion of the pole of the ITRS in the GCRS into a celestial part and a terrestrial part. The convention is such that:

• the celestial motion of the CIP (precession-nutation), includes all the terms with periods greater than 2 days in the GCRS (i.e. frequencies between $- 0 . 5$ cycles per sidereal day (cpsd) and $+ 0 . 5$ cpsd),   
• the terrestrial motion of the CIP (polar motion), includes all the terms outside the retrograde diurnal band in the ITRS (i.e. frequencies lower than $- 1 . 5$ cpsd or greater than $- 0 . 5$ cpsd).

The following chart illustrates the conventional frequency separation between the precession-nutation of the CIP and its polar motion, either viewed in the ITRS (top), or the GCRS (bottom), with a 1 cpsd shift due to the rotation of the ITRS with respect to the GCRS.

![](../chunks/IERS Conventions (2010), IERS Technical Note No.36_part_0001_pages_0001-0070/auto/images/40db1ae717a43e380251653ad79c092af077a23938557137fb108d80661737f0.jpg)

# 5.3.3 The IAU 2000/2006 realization of the Celestial Intermediate Pole (CIP)

In order to follow IAU 2000 Resolution B1.6 and IAU 2006 Resolution B1, the precession-nutation quantities to be used in the transformation matrix $Q ( t )$ of Eq. (5.1) must, starting on 1 January 2009, be based on the IAU 2006 precession and on the nutation model IAU 2000A or IAU 2000B depending on the required precision (the corresponding precession-nutation being denoted IAU 2006/2000A and IAU 2006/200B, respectively). IAU 2006 Resolution B1 adopting the IAU 2006 precession does not stipulate a specific parameterization, expressly stating that the user makes this choice. Various ways of forming the precession-nutation matrix based on a rigorous procedure in the IAU 2006 framework have been discussed in Capitaine and Wallace (2006), and the precession-nutation procedures consistent with IAU 2006 resolutions have been provided in Wallace and Capitaine (2006). The procedures provided in the following sections are based on the results of that paper.

In order to follow IAU 2000 Resolution B1.7, the realized celestial pole must be the CIP. This requires an offset at epoch in the conventional model for precessionnutation as well as diurnal and higher frequency variations in the Earth’s orientation. According to this resolution, the direction of the CIP at J2000.0 has to be offset from the pole of the GCRS in a manner consistent with the IAU 2006/2000A precession-nutation model. The motion of the CIP in the GCRS is realized (see Section 5.3.2) by the IAU model for precession and forced nutation for periods greater than two days plus additional time-dependent corrections provided by the IERS through appropriate astro-geodetic observations. The motion of the CIP in the ITRS is provided by the IERS through astro-geodetic observations and models including variations with frequencies outside the retrograde diurnal band.

The realization of the CIP thus requires that the IERS monitor the observed differences (reported as “celestial pole offsets”) with respect to the conventional celestial position of the CIP in the GCRS based on the IAU 2006/2000 precessionnutation model together with its observed offset at epoch. It also requires that the motion of the CIP in the ITRS be provided by the IERS by observations taking into account a predictable part specified by a model including the terrestrial motion of the pole corresponding to the forced nutations with periods less than two days (in the GCRS) as well as the tidal variations in polar motion.

# 5.3.4 Procedures to be used for the terrestrial-to-celestial transformation consistent with IAU 2000/2006 resolutions

Two equivalent procedures have been given in the IERS Conventions 1996 and 2003 for the coordinate transformation from the ITRS to the GCRS expressed by Eq. (5.1). According to the NFA recommendations, these procedures, which differ by the origin that is adopted on the CIP equator (i.e. the equinox or the CIO), will be called in the following “equinox based” and “CIO based”, respectively. Each of these procedures is based on a specific representation of the transformation matrix components $Q ( t )$ and $R ( t )$ of Eq. (5.1), which depends on the corresponding origin on the CIP equator, while the representation of the transformation matrix component $W ( t )$ is common to the two procedures.

IAU 2000 Resolutions B1.3, B1.6 and B1.7 as well as IAU 2006 B1 can be implemented in any of these two procedures if the requirements described in Sections 5.3.1 and 5.3.3 are followed for the space-time coordinates in the geocentric celestial reference system, for the precession and nutation model on which are based the precession and nutation quantities used in the transformation matrix $Q ( t )$ and for the polar motion used in the transformation matrix $W ( t )$ . On the other hand, only the CIO based procedure can be in agreement with IAU 2000 Resolution B1.8, which requires the use of the “non-rotating origin” in both the GCRS and the ITRS as well as the position of the CIP in the GCRS and in the ITRS. This is why this chapter of the IERS Conventions provides the expressions for the implementation of the IAU resolutions with more emphasis on the CIO based procedure. However, the IERS must also provide users with data and algorithms for the conventional transformation, which implies in particular that the expression of Greenwich Sidereal Time (GST) has to be consistent with the new procedure. Consequently, this chapter also provides the expressions which are necessary to be compatible with the resolutions when using the conventional transformation.

The following sections give the details of the CIO based procedure and the standard expressions necessary to obtain the numerical values of the relevant parameters for both procedures at the date of observation.

# 5.4 Coordinate transformation consistent with the IAU 2000/2006 resolutions

The coordinate transformation (5.1) from the ITRS to the GCRS corresponding to the procedure consistent with IAU 2000 Resolution B1.8 is expressed in terms of the three fundamental components $W ( t )$ , $R ( t )$ and $Q ( t )$ , as described in the following.

According to IAU 2006 Resolution B2, the system at date $t$ as realized from the ITRS by applying the transformation $W ( t )$ in both procedures is the “Terrestrial Intermediate Reference System” (TIRS). It uses the CIP as its $z$ -axis and the TIO as its $x$ -axis.

The CIO based procedure realizes an intermediate celestial reference system at date $t$ that uses the CIP as its $z$ -axis and the CIO as its $_ x$ -axis. According to IAU 2006 Resolution B2, it is called the “Celestial Intermediate Reference System” (CIRS). It uses the “Earth Rotation Angle” in the transformation matrix $R ( t )$ , and the two coordinates of the CIP in the GCRS (Capitaine, 1990) in the transformation matrix $Q ( t )$ .

The classical procedure realizes an intermediate celestial reference system at date $t$ that uses the CIP as its $z$ -axis and the equinox as its $x$ -axis. It is called the “true equinox and equator of date system”. It uses apparent Greenwich Sidereal Time (GST) in the transformation matrix $R ( t )$ and the classical precession and nutation parameters in the transformation matrix $Q ( t )$ .

Each of the transformation matrix components $W ( t )$ , $R ( t )$ and $Q ( t )$ of Eq. (5.1) is a series of rotations about the axes $^ { 1 }$ , 2 and 3 of the coordinate frame. In the following, $R _ { 1 }$ , $R _ { 2 }$ and $R _ { 3 }$ denote rotation matrices with positive angle about the axes $^ { 1 }$ , 2 and 3. The position of the CIP both in the ITRS and GCRS is provided by the $_ { x }$ and $_ y$ components of the CIP unit vector. These components are called “coordinates” in the following, and their numerical expressions are multiplied by the factor $1 2 9 6 0 0 0 ^ { \prime \prime } / 2 \pi$ in order to represent the approximate values in arcseconds of the corresponding “angles” (strictly their sines) with respect to the $z$ -axis of the reference system.

# 5.4.1 Expression for the transformation matrix for polar motion

The transformation matrix arising from polar motion (i.e. relating ITRS and TIRS) can be expressed as:

$$
W ( t ) = R _ { 3 } ( - s ^ { \prime } ) \cdot R _ { 2 } ( x _ { p } ) \cdot R _ { 1 } ( y _ { p } ) ,
$$

$x _ { p }$ and $y _ { p }$ being the “polar coordinates” of the Celestial Intermediate Pole (CIP) in the ITRS and $s ^ { \prime }$ being a quantity, named “TIO locator”, which provides the position of the TIO on the equator of the CIP corresponding to the kinematical definition of the “non-rotating” origin (NRO) in the ITRS when the CIP is moving with respect to the ITRS due to polar motion.

The expression of $s ^ { \prime }$ as a function of the coordinates $x _ { p }$ and $y _ { p }$ is:

$$
s ^ { \prime } ( t ) = { \frac { 1 } { 2 } } \ \int _ { t _ { 0 } } ^ { t } ( x _ { p } { \dot { y } } _ { p } - { \dot { x } } _ { p } y _ { p } ) \ d t .
$$

The use of the quantity $s ^ { \prime }$ , which was neglected in the classical form prior to 1 January 2003, is necessary to provide an exact realization of the “instantaneous prime meridian” (designated by “TIO meridian”).

# 5.4.2 Expression for the CIO based transformation matrix for Earth rotation

The CIO based transformation matrix arising from the rotation of the Earth around the axis of the CIP (i.e. relating TIRS and CIRS), can be expressed as:

$$
R ( t ) = R _ { 3 } ( - E R A ) ,
$$

where ERA is the Earth Rotation Angle between the CIO and the TIO at date $t$ on the equator of the CIP, which provides a rigorous definition of the sidereal rotation of the Earth.

# 5.4.3 Expression for the equinox based transformation matrix for Earth rotation

The equinox based transformation matrix $R ( t )$ for Earth rotation transforms from the TIRS to the true equinox and equator of date system. It uses Apparent Greenwich Sidereal Time, i.e. the angle between the equinox and the TIO, to represent the Earth’s angle of rotation, instead of the ERA.

# 5.4.4 Expression for the transformation matrix for the celestial motion of the CIP

The CIO based transformation matrix arising from the motion of the CIP in the GCRS (i.e. relating CIRS and GCRS), can be expressed as:

$$
Q ( t ) = R _ { 3 } ( - E ) \cdot R _ { 2 } ( - d ) \cdot R _ { 3 } ( E ) \cdot R _ { 3 } ( s ) ,
$$

$E$ and $d$ being such that the coordinates of the CIP in the GCRS are:

$$
X = \sin d \cos E , \qquad Y = \sin d \sin E , \qquad Z = \cos d ,
$$

and $s$ being a quantity, named “CIO locator”, which provides the position of the CIO on the equator of the CIP corresponding to the kinematical definition of the NRO in the GCRS when the CIP is moving with respect to the GCRS, between the reference epoch and the date $t$ due to precession and nutation. Its expression as a function of the coordinates $X$ and $Y$ is (Capitaine et al., 2000)

$$
s ( t ) = - \int _ { t _ { 0 } } ^ { t } \frac { X ( t ) \dot { Y } ( t ) - Y ( t ) \dot { X } ( t ) } { 1 + Z ( t ) } d t - ( \sigma _ { 0 } N _ { 0 } - \Sigma _ { 0 } N _ { 0 } ) ,
$$

where $\sigma _ { 0 }$ and $\Sigma _ { 0 }$ are the positions of the CIO at J2000.0 and the $x$ -origin of the GCRS respectively and $N _ { 0 }$ is the ascending node of the equator at $J 2 0 0 0 . 0$ in the equator of the GCRS. Or equivalently, within 1 microarcsecond over one century:

$$
s ( t ) = - \frac { 1 } { 2 } [ X ( t ) Y ( t ) - X ( t _ { 0 } ) Y ( t _ { 0 } ) ] + \int _ { t _ { 0 } } ^ { t } \dot { X } ( t ) Y ( t ) d t - ( \sigma _ { 0 } N _ { 0 } - \Sigma _ { 0 } N _ { 0 } ) .
$$

The arbitrary constant $\sigma _ { 0 } N _ { 0 } - \Sigma _ { 0 } N _ { 0 }$ , which had been conventionally chosen to be zero in previous references (e.g. Capitaine et al., 2000), was afterwards chosen to ensure continuity with the classical procedure on 1 January 2003 (see expression (5.31)).

$Q ( t )$ can be given in an equivalent form directly involving $X$ and $Y$ as

$$
Q ( t ) = \left( \begin{array} { c c c } { { 1 - a X ^ { 2 } } } & { { - a X Y } } & { { X } } \\ { { - a X Y } } & { { 1 - a Y ^ { 2 } } } & { { Y } } \\ { { - X } } & { { - Y } } & { { 1 - a ( X ^ { 2 } + Y ^ { 2 } ) } } \end{array} \right) \cdot R _ { 3 } ( s ) ,
$$

with $a = 1 / ( 1 + \cos d )$ , which can also be written, with an accuracy of $1 \mu \mathrm { a s }$ , as $a = 1 / 2 + 1 / 8 ( X ^ { 2 } + Y ^ { 2 } )$ . Such an expression of the transformation (5.1) leads to very simple expressions of the partial derivatives of observables with respect to the terrestrial coordinates of the CIP, UT1, and celestial coordinates of the CIP.

# 5.4.5 Expression for the equinox-based transformation matrix for precession-nutation

The equinox based matrix $Q ( t )$ that transforms from the true equinox and equator of date system to the GCRS can be expressed in several ways corresponding to different parameterization choices.

• One rigorous way is that recommended in the previous version of the IERS Conventions. It is composed of the classical nutation matrix (using the nutation angles $\Delta \psi$ , $\Delta \epsilon$ in longitude and obliquity referred to the ecliptic of date and the mean obliquity of date, $\epsilon A$ ), the precession matrix including four rotations $\begin{array} { r l } { \big ( R _ { 1 } ( - \epsilon _ { 0 } ) \cdot R _ { 3 } ( \psi _ { A } ) \cdot R _ { 1 } ( \omega _ { A } ) \cdot R _ { 3 } ( - \chi _ { A } ) \big ) } & { { } } \end{array}$ , and a separate rotation matrix for the frame biases. The precession angles are those of Lieske et al. (1977), in which $\epsilon _ { \mathrm { 0 } }$ is the obliquity of the ecliptic at J2000.0, $\psi _ { A }$ and $\omega _ { A }$ are the precession quantities in longitude and obliquity referred to the ecliptic of epoch and $\chi A$ is the precession of the ecliptic along the equator. • Another rigorous way is that proposed by Fukushima (2003) as an extension to the GCRS of the method originally proposed by Williams (1994). This way is more concise than the previous one, as it can be referred directly to the GCRS pole and origin without requiring the frame bias to be applied separately, and there is no need for separate precession and nutation steps. It is composed of the four rotations: $R _ { 1 } ( - \epsilon ) \cdot R _ { 3 } ( - \psi ) \cdot R _ { 1 } ( \phi ) \cdot R _ { 3 } ( \bar { \gamma } ) )$ , where the angles $\epsilon$ and $\psi$ are each obtained by summing the contributions from the bias, precession and nutation in obliquity and ecliptic longitude, respectively, $\phi$ is the obliquity of the ecliptic of date on the GCRS equator, and $\gamma$ is the GCRS right ascension of the intersection of the ecliptic of date with the GCRS equator.

# 5.5 Parameters to be used in the transformation

# 5.5.1 Motion of the Celestial Intermediate Pole in the ITRS

The standard pole coordinates to be used for the parameters $x _ { p }$ and $y _ { p }$ appearing in Eq. (5.3) of Section 5.4.1, if not estimated from the observations, are those published by the IERS with additional components to account for the effect of ocean tides $( \Delta x , \Delta y ) _ { \mathrm { o c e a n t i d e s } }$ and for forced terms $( \Delta x , \Delta y ) _ { \mathrm { l i b r a t i o n } }$ with periods less than two days in space:

$$
( x _ { p } , y _ { p } ) = ( x , y ) _ { \mathrm { I E R S } } + ( \Delta x , \Delta y ) _ { \mathrm { o c e a n t i d e s } } + ( \Delta x , \Delta y ) _ { \mathrm { l i b r a t i o n } } ,
$$

where $( x , y ) _ { \mathrm { I E R S } }$ are pole coordinates provided by the IERS, $( \Delta x , \Delta y ) _ { \mathrm { o c e a n } }$ tides are the diurnal and semi-diurnal variations in pole coordinates caused by ocean tides, and $( \Delta x , \Delta y ) _ { \mathrm { l i b r a t i o n } }$ are the variations in pole coordinates corresponding to motions with periods less than two days in space that are not part of the IAU 2000 nutation model. These variations are described in detail below.

5.5.1.1 Account of ocean tidal and libration effects in pole coordinates $x _ { p }$ and $y _ { p }$

The subdaily variations are not part of the polar motion values reported to and distributed by the IERS and are therefore to be added after interpolation. This is appropriately done by the routine “INTERP.F” of the IERS EOP Product Center, which interpolates series of xIERS, yIERS values to a chosen date and then adds the contribution for this date of (i) the tidal terms $( \Delta x , \Delta y ) _ { \mathrm { o c e a n t i d e s } }$ derived from Tables 8.2a and 8.2b, and (ii) the diurnal components of the $( \Delta x , \Delta y ) _ { \mathrm { l i b r a t i o n } }$ terms, derived from Table 5.1a. The long-period terms, as well as the secular variation of the libration contribution, are already contained in the observed polar motion and need not be added to the reported values $( x , y ) _ { \mathrm { I E R S } }$ .

# 5.5.1.2 Variations $( \Delta x , \Delta y ) _ { \mathrm { o c e a n t i d e s } }$ s in polar motion

These are tidal variations in Earth orientation considered in Chapter 8, including diurnal and semi-diurnal variations in pole coordinates caused by ocean tides. Tables 8.2a and 8.2b provide the amplitudes and arguments for the 71 tidal constituents of those diurnal and semi-diurnal variations that have been derived from the routine “ORTHO EOP.F” based on the model from Ray et al. (1994). That routine is available on the website of the IERS Conventions (see Chapter 8).

# 5.5.1.3 Variations $( \Delta x , \Delta y )$ libration in polar motion

According to the definition of the CIP (IAU 2000 Resolution B1.7; see Appendix A7), forced motions with periods less than two days in space are not included in the IAU 2000 nutation model and therefore have to be considered using a model for the corresponding motion of the pole in the ITRS.

Recent models for rigid Earth nutation (Bretagnon et al., 1997; Folgueira et al., 1998a and b; Souchay et al., 1999; Roosbeek, 1999; Bizouard et al., 2000 and 2001) include prograde diurnal and prograde semi-diurnal terms with respect to the GCRS with amplitudes up to $\sim 1 5$ µas. The semi-diurnal terms in nutation have also been provided both for rigid and nonrigid Earth models based on Hamiltonian formalism (Getino et al., 2001; Escapa et al., 2002 and 2003).

These diurnal and semi-diurnal nutations, which, according to Chao et al. (1991), are designated here as “libration”, originate from the direct effect of the external (mainly luni-solar) torque on the non-axisymmetric part of the Earth as expressed by the non-zonal terms of the geopotential. This effect is also called the “tidal gravitation” effect, and has been designated in the past as the “nutation” effect on polar motion.

The prograde diurnal nutations correspond to prograde and retrograde longperiod variations in polar motion including the linear term, and the prograde semi-diurnal nutations correspond to prograde diurnal variations in polar motion (see for example Folgueira et al., 2001). A table for operational use of the model for these variations in polar motion for a nonrigid Earth has been provided by an ad hoc Working Group (Brzezi´nski, 2002; Brzezi´nski and Mathews, 2003), based on nonrigid Earth models and developments of the tide generating potential (TGP; Brzezi´nski, 2001; Brzezi´nski and Capitaine, 2003; Mathews and Bretagnon, 2003). All components with amplitudes greater than $0 . 5 \mu \mathrm { a s }$ are given in Table 5.1a. The amplitudes of the diurnal terms are in very good agreement with those estimated by Getino et al. (2001). The contribution from the triaxiality of the core to the diurnal terms, while it can exceed the adopted cut-off level (Escapa et al., 2002; Mathews and Bretagnon, 2003), has not been taken into account in the table due to the large uncertainty in the triaxiality of the core (Brzezi´nski and Capitaine, 2003; Dehant, 2002, private communication). The coefficients of Table 5.1a are based on Stokes coefficients of the JGM-3 geopotential model (Tapley et al., 1996), but any of the geopotential models commonly used in current precision orbital analysis would give values that would agree within the adopted cut-off level of 0.1 µas with those of Table 5.1a.

The diurnal components of $( \Delta x , \Delta y )$ libration can be computed with the routine

PMSDNUT2.F, available on the Conventions Center website at ${ < } ^ { 2 } >$ . These diurnal components (namely, the 10 terms listed in Table 5.1a with periods near 1 day) should be considered similarly to the diurnal and semi-diurnal variations due to ocean tides (see above).

Note that the 10 diurnal terms of Table 5.1a due to the influence of tidal gravitation on the non-axisymmetric part of the Earth are a subset of the 41 diurnal terms of Table 8.2a with, for each common term, an amplitude about 10 times lower than the corresponding amplitude for the variation in UT1 (or LOD) caused by ocean tides provided in Table 8.2a.

Table 5.1a: Coefficients of sin(argument) and cos(argument) in $( \Delta x , \Delta y ) _ { \mathrm { l i b r a t i o n } }$ due to tidal gravitation (of degree n) for a nonrigid Earth. Listed are all terms with amplitudes greater than 0.5 muas. Units are $\mu$ as, $\gamma$ denotes GMST $+ \pi$ (where GMST = ERA $^ +$ precession in RA (see Eq. (5.32))). The expressions for the fundamental arguments (Delaunay arguments) are given by Eq. (5.43).   

<table><tr><td></td><td></td><td colspan="6">Argument</td><td>Doodson</td><td colspan="2">Period</td><td colspan="2">yp</td></tr><tr><td>n</td><td>Tide</td><td>Y</td><td>1</td><td>l</td><td>F</td><td>D</td><td>Ω</td><td>number</td><td>(days)</td><td>sin</td><td>COs</td><td>sin</td><td>Cos</td></tr><tr><td>4</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-1</td><td>055.565</td><td>6798.3837</td><td>0.0</td><td>0.6</td><td>-0.1</td><td>-0.1</td></tr><tr><td>3</td><td></td><td>0</td><td>-1</td><td>0</td><td>1</td><td>0</td><td>2</td><td>055.645</td><td>6159.1355</td><td>1.5</td><td>0.0</td><td>-0.2</td><td>0.1</td></tr><tr><td>3</td><td></td><td>0</td><td>-1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>055.655</td><td>3231.4956</td><td>-28.5</td><td>-0.2</td><td>3.4</td><td>-3.9</td></tr><tr><td>3</td><td></td><td>0</td><td>-1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>055.665</td><td>2190.3501</td><td>-4.7</td><td>-0.1</td><td>0.6</td><td>-0.9</td></tr><tr><td>3</td><td></td><td>0</td><td>1</td><td>1</td><td>-1</td><td>0</td><td>0</td><td>056.444</td><td>438.35990</td><td>-0.7</td><td>0.2</td><td>-0.2</td><td>-0.7</td></tr><tr><td>3</td><td></td><td>0</td><td>1</td><td>1</td><td>-1</td><td>0</td><td>-1</td><td>056.454</td><td>411.80661</td><td>1.0</td><td>0.3</td><td>-0.3</td><td>1.0</td></tr><tr><td>3</td><td></td><td>0</td><td>0</td><td>0</td><td>1</td><td>-1</td><td>1</td><td>056.555</td><td>365.24219</td><td>1.2</td><td>0.2</td><td>-0.2</td><td>1.4</td></tr><tr><td>3</td><td></td><td>0</td><td>1</td><td>0</td><td>1</td><td>-2</td><td>1</td><td>057.455</td><td>193.55971</td><td>1.3</td><td>0.4</td><td>-0.2</td><td>2.9</td></tr><tr><td>3</td><td></td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>2</td><td>065.545</td><td>27.431826</td><td>-0.1</td><td>-0.2</td><td>0.0</td><td>-1.7</td></tr><tr><td>3</td><td></td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>065.555</td><td>27.321582</td><td>0.9</td><td>4.0</td><td>-0.1</td><td>32.4</td></tr><tr><td>3</td><td></td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>065.565</td><td>27.212221</td><td>0.1</td><td>0.6</td><td>0.0</td><td>5.1</td></tr><tr><td>3</td><td></td><td>0</td><td>-1</td><td>0</td><td>1</td><td>2</td><td>1</td><td>073.655</td><td>14.698136</td><td>0.0</td><td>0.1</td><td>0.0</td><td>0.6</td></tr><tr><td>3</td><td></td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>075.455</td><td>13.718786</td><td>-0.1</td><td>0.3</td><td>0.0</td><td>2.7</td></tr><tr><td>3</td><td></td><td>0</td><td>0</td><td>0</td><td>3</td><td>0</td><td>3</td><td>085.555</td><td>9.1071941</td><td>-0.1</td><td>0.1</td><td>0.0</td><td>0.9</td></tr><tr><td>3</td><td></td><td>0</td><td>0</td><td>0</td><td>3</td><td>0</td><td>2</td><td>085.565</td><td>9.0950103</td><td>-0.1</td><td>0.1</td><td>0.0</td><td>0.6</td></tr><tr><td>2</td><td>Qi</td><td>1</td><td>-1</td><td>0</td><td>-2</td><td>0</td><td>-1</td><td>135.645</td><td>1.1196992</td><td>-0.4</td><td>0.3</td><td>-0.3</td><td>-0.4</td></tr><tr><td>2</td><td>Q1</td><td>1</td><td>-1</td><td>0</td><td>-2</td><td>0</td><td>-2</td><td>135.655</td><td>1.1195149</td><td>-2.3</td><td>1.3</td><td>-1.3</td><td>-2.3</td></tr><tr><td>2</td><td>p1</td><td>1</td><td>1</td><td>0</td><td>-2</td><td>-2</td><td>-2</td><td>137.455</td><td>1.1134606</td><td>-0.4</td><td>0.3</td><td>-0.3</td><td>-0.4</td></tr><tr><td>2</td><td>01</td><td>1</td><td>0</td><td>0</td><td>-2</td><td>0</td><td>-1</td><td>145.545</td><td>1.0759762</td><td>-2.1</td><td>1.2</td><td>-1.2</td><td>-2.1</td></tr><tr><td>2</td><td>O1</td><td>1</td><td>0</td><td>0</td><td>-2</td><td>0</td><td>-2</td><td>145.555</td><td>1.0758059</td><td>-11.4</td><td>6.5</td><td>-6.5</td><td>-11.4</td></tr><tr><td>2</td><td>M1</td><td>1</td><td>-1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>155.655</td><td>1.0347187</td><td>0.8</td><td>-0.5</td><td>0.5</td><td>0.8</td></tr><tr><td>2</td><td>P1</td><td>1</td><td>0</td><td>0</td><td>-2</td><td>2</td><td>-2</td><td>163.555</td><td>1.0027454</td><td>-4.8</td><td>2.7</td><td>-2.7</td><td>-4.8</td></tr><tr><td>2</td><td>K1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>165.555</td><td>0.9972696</td><td>14.3</td><td>-8.2</td><td>8.2</td><td>14.3</td></tr><tr><td>2</td><td>K1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-1</td><td>165.565</td><td>0.9971233</td><td>1.9</td><td>-1.1</td><td>1.1</td><td>1.9</td></tr><tr><td>2</td><td>J1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>175.455</td><td>0.9624365</td><td>0.8</td><td>-0.4</td><td>0.4</td><td>0.8</td></tr></table>

Rate of secular polar motion $\left( \mu \mathrm { a s } / \mathrm { y } \right)$ due to the zero frequency tide

<table><tr><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>555.555</td><td>3.8</td><td>-4.3</td></tr></table>

# 5.5.2 Position of the Terrestrial Intermediate Origin in the ITRS

The quantity $s ^ { \prime }$ (i.e. the TIO locator) appearing in Eq. (5.3) and expressed by Eq. (5.4) is sensitive only to the largest variations in polar motion. Some components of $s ^ { \prime }$ have to be evaluated, in principle, from the measurements and can be

extrapolated using the IERS data. Its main component can be written as:

$$
s ^ { \prime } = - 0 . 0 0 1 5 \left( a _ { c } ^ { 2 } / 1 . 2 + a _ { a } ^ { 2 } \right) t ,
$$

$a _ { c }$ and $a _ { a }$ being the average amplitudes (in as) of the Chandlerian and annual wobbles, respectively, in the period considered (Capitaine et al., 1986). The value of $s ^ { \prime }$ will therefore be less than 0.4 mas through the next century, even if the amplitudes for the Chandlerian and annual wobbles reach values of the order of $0 . 5 ^ { \prime \prime }$ and $0 . 1 ^ { \prime \prime }$ , respectively. Using the current mean amplitudes for the Chandlerian and annual wobbles gives (Lambert and Bizouard, 2002):

$$
s ^ { \prime } = - 4 7 ~ \mu \mathrm { a s } ~ t .
$$

# 5.5.3 Earth Rotation Angle

The conventional relationship defining UT1 from the Earth Rotation Angle (ERA) to be used in Eq. (5.5) of Section 5.4.2 is that given by Capitaine et al. (2000):

$$
E R A ( T _ { u } ) = 2 \pi ( 0 . 7 7 9 0 5 7 2 7 3 2 6 4 0 + 1 . 0 0 2 7 3 7 8 1 1 9 1 1 3 5 4 4 8 T _ { u } ) ,
$$

where $T _ { u }$ =(Julian UT1 date−2451545.0), and UT1=UTC $^ +$ (UT1 $\mathbf { \Phi } _ { \cdot } -$ UTC), or equivalently (modulo $2 \pi$ ), in order to reduce possible rounding errors,

$$
\begin{array} { l l l } { { E R A ( T _ { u } ) } } & { { = } } & { { 2 \pi ( \mathrm { U T 1 ~ J u l i a n ~ d a y ~ f r a c t i o n } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + 0 . 7 7 9 0 5 7 2 7 3 2 6 4 0 + 0 . 0 0 2 7 3 7 8 1 1 9 1 1 3 5 4 4 8 T _ { u } ) . } } \end{array}
$$

This definition of UT1 based on the CIO is insensitive at the microarcsecond level to the precession-nutation model and to the observed celestial pole offsets. Therefore, in processing observational data, the quantity $s$ provided by Table 5.2d must be considered as independent of observations.

The above relationship also provides the ERA corresponding to a given UT1, the quantity UT1 $-$ UTC to be used (if not estimated from the observations) being the IERS value. Note that, for $0 ^ { h }$ UT1, the UT1 Julian day fraction in Eq. (5.15) is 0.5.

Similarly to polar motion (cf. Section 5.5.1), additional components should be added to the values published by the IERS for UT1 and LOD to account for the effects of ocean tides and libration. These effects are described in detail below.

# .5.3.1 Account of ocean tidal and libration effects in UT1 and LOD

The subdaily variations are not part of the UT1 or LOD values reported to and distributed by the IERS and are therefore to be added after interpolation. This is appropriately done for the first effect by the routine “INTERP.F” of the IERS EOP Product Center, which interpolates series of UT1IERS and LODIERS values to a chosen date and then adds the contribution for this date of the tidal terms $\Delta$ UT1ocean tides, or ∆LODocean tides, derived from Tables 8.3a and 8.3b. The semi-diurnal components of the libration contribution $\Delta$ UT1libration, or $\Delta$ LODlibration derived from Table 5.1b should be included in that routine.

# 5.5.3.2 Variations ∆UT1ocean tides and ∆LODocean tides in UT1 and LOD

These are tidal variations in Earth orientation considered in Chapter 8, including diurnal and semi-diurnal variations in UT1 or LOD caused by ocean tides. Tables 8.3a and 8.3b provide the amplitudes and arguments for the 71 tidal constituents of those diurnal and semi-diurnal variations that have been derived from the routine “ORTHO EOP.F” (available on the website of the IERS Conventions at ${ < } ^ { 3 } { > }$ ) based on the model from Ray et al. (1994).

The axial component of Earth rotation contains small variations due to the direct effect of the external (mainly luni-solar) torque on the non-axisymmetric part of the Earth as expressed by the non-zonal terms of the geopotential. This effect was theoretically predicted by Tisserand (1891) and Kinoshita (1977), but was neglected in current practical applications due to its very small size (maximum peak-to-peak variation of about 0.1 mas, i.e. 0.007 ms in UT1). More complete descriptions were published when the effect, also designated as “tidal gravitation”, became observationally detectable by, e.g. Chao et al. (1991), W¨unsch (1991), Chao et al. (1996) and Brzezi´nski and Capitaine (2003; 2010).

An analytical solution for the sub-diurnal libration in UT1 has been derived by Brzezi´nski and Capitaine (2003) for the structural model of the Earth consisting of an elastic mantle and a liquid core which are not coupled to each other. The reference solution for the rigid Earth has been computed by using the satellite-determined coefficients of geopotential and the recent developments of the tide generating potential. Table 5.1b provides the amplitudes and arguments for all components in UT1 and LOD with amplitudes greater than $0 . 5 \mu \mathrm { a s }$ (i.e. $0 . 0 3 3 \mu \mathrm { s }$ in UT1.) It consists of 11 semi-diurnal harmonics due to the influence of the TGP term $u _ { 2 2 }$ on the equatorial flattening of the Earth expressed by the Stokes coefficients $C _ { 2 2 }$ , $S _ { 2 2 }$ . There is excellent agreement between the values for the rigid Earth and the amplitudes derived by W¨unsch (1991), except for the term with the tidal code $\nu _ { 2 }$ , which seems to have been overlooked in the latter model. The amplitudes computed for an elastic Earth with liquid core are in reasonable agreement with those derived by Chao et al. (1991), but the latter model was not complete.

Table 5.1b: Coefficients of sin(argument) and cos(argument) of semi-diurnal variations in UT1 and LOD due to libration for a non-rigid Earth. Listed are all terms with amplitudes of UT1 greater than $0 . 0 3 3 ~ \mu \mathrm { s }$ . Units are µs, $\gamma$ denotes $\mathrm { G M S T } { + } \pi$ . Expressions for the fundamental arguments are given by Eq. (5.43).   

<table><tr><td></td><td colspan="6">Argument</td><td>Doodson</td><td>Period</td><td colspan="2">UT1</td><td colspan="2">LOD</td></tr><tr><td>Tide</td><td>Y</td><td>l</td><td>1</td><td>F</td><td>D</td><td>m</td><td>number</td><td>(days)</td><td>sin</td><td>Cos</td><td>sin</td><td>Cos</td></tr><tr><td>2N2</td><td>2</td><td>-2</td><td>0</td><td>-2</td><td>0</td><td>-2</td><td>235.755</td><td>0.5377239</td><td>0.05</td><td>-0.03</td><td>-0.3</td><td>-0.6</td></tr><tr><td>μ2</td><td>2</td><td>0</td><td>0</td><td>-2</td><td>-2</td><td>-2</td><td>237.555</td><td>0.5363232</td><td>0.06</td><td>-0.03</td><td>-0.4</td><td>-0.7</td></tr><tr><td>N2</td><td>2</td><td>-1</td><td>0</td><td>-2</td><td>0</td><td>-2</td><td>245.655</td><td>0.5274312</td><td>0.35</td><td>-0.20</td><td>-2.4</td><td>-4.2</td></tr><tr><td>V2</td><td>2</td><td>1</td><td>0</td><td>-2</td><td>-2</td><td>-2</td><td>247.455</td><td>0.5260835</td><td>0.07</td><td>-0.04</td><td>-0.5</td><td>-0.8</td></tr><tr><td>M</td><td>2</td><td>0</td><td>0</td><td>-2</td><td>0</td><td>-1</td><td>255.545</td><td>0.5175645</td><td>-0.07</td><td>0.04</td><td>0.5</td><td>0.8</td></tr><tr><td>M2</td><td>2</td><td>0</td><td>0</td><td>-2</td><td>0</td><td>-2</td><td>255.555</td><td>0.5175251</td><td>1.75</td><td>-1.01</td><td>-12.2</td><td>-21.3</td></tr><tr><td>L2</td><td>2</td><td>1</td><td>0</td><td>-2</td><td>0</td><td>-2</td><td>265.455</td><td>0.5079842</td><td>-0.05</td><td>0.03</td><td>0.3</td><td>0.6</td></tr><tr><td>T</td><td>2</td><td>0</td><td>-1</td><td>-2</td><td>2</td><td>-2</td><td>272.556</td><td>0.5006854</td><td>0.05</td><td>-0.03</td><td>-0.3</td><td>-0.6</td></tr><tr><td>S</td><td>2</td><td>0</td><td>0</td><td>-2</td><td>2</td><td></td><td>273.555</td><td>0.5000000</td><td>0.76</td><td>-0.44</td><td>-5.5</td><td>-9.5</td></tr><tr><td>K2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>275.555</td><td>0.4986348</td><td>0.21</td><td>-0.12</td><td>-1.5</td><td>-2.6</td></tr><tr><td>K</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-1</td><td>275.565</td><td>0.4985982</td><td>0.06</td><td>-0.04</td><td>-0.4</td><td>-0.8</td></tr></table>

Note that the 11 semi-diurnal terms of Table 5.1b due to the influence of tidal gravitation on the triaxiality of the Earth are a subset of the 30 semi-diurnal terms of Table 8.3b, with, for each common term, an amplitude about 10 times lower than the corresponding amplitude for the variation in UT1 (or LOD) caused by ocean tides provided in Table 8.3b. Nevertheless, the maximum peak-to-peak size of the triaxiality effect on UT1 is about 0.105 mas, hence definitely above the current uncertainty of UT1 determinations. A comparison with the corresponding model of prograde diurnal polar motion associated with the Earth’s libration (Table 5.1a) shows that the two effects are of similar size and that there is consistency between the underlying dynamical models and the parameters employed. The sub-diurnal libration in UT1, $\Delta U T 1 _ { \mathrm { l i b r a t i o n } }$ , can be computed with the routine UTLIBR.F, provided by A. Brzezi´nski, available on the Conventions Center website at ${ < } ^ { 2 } { > }$ .

# 5.5.4 Forced motion of the Celestial Intermediate Pole in the GCRS

The coordinates of the CIP in the GCRS to be used for the parameters $X$ and $Y$ appearing in Eq. (5.10) of Section 5.4.4 can be given by developments as function of time of those quantities. Developments valid at the microarcsecond level, based on the IAU 2006 precession and IAU 2000A nutation (see Section 5.6 for more details) and on their corresponding pole and equinox offsets at J2000.0 with respect to the pole of the GCRS have been computed (Capitaine and Wallace, 2006). They replace the previous developments based on the IAU 2000 model for precessionnutation and frame biases that had been provided by Capitaine et al. (2003a) and in the IERS 2003 Conventions.

The IAU 2006/2000A developments are as follows:

$$
\begin{array} { r l } { X = } & { - 0 . 0 1 6 6 1 7 ^ { \prime \prime } + 2 0 0 4 . 1 9 1 8 9 8 ^ { \prime \prime } t - 0 . 4 2 9 7 8 2 9 ^ { \prime \prime } t ^ { 2 } } \\ & { - 0 . 1 9 8 6 1 8 3 4 ^ { \prime \prime } t ^ { 3 } + 0 . 0 0 0 0 0 7 5 7 8 ^ { \prime \prime } t ^ { 4 } + 0 . 0 0 0 0 0 5 9 2 8 5 ^ { \prime \prime } t ^ { 5 } } \\ & { + \sum _ { i } [ ( a _ { \mathrm { s } , 0 } ) _ { i } \sin ( \mathrm { A R G U M E N T } ) + ( a _ { \mathrm { c } , 0 } ) _ { i } \cos ( \mathrm { A R G U M E N T } ) ] } \\ & { + \sum _ { i } [ ( a _ { \mathrm { s } , 1 } ) _ { i } t \sin ( \mathrm { A R G U M E N T } ) + ( a _ { \mathrm { c } , 1 } ) _ { i } t \cos ( \mathrm { A R G U M E N T } ) ] } \\ & { + \sum _ { i } [ ( a _ { \mathrm { s } , 2 } ) _ { i } t ^ { 2 } \sin ( \mathrm { A R G U M E N T } ) + ( a _ { \mathrm { c } , 2 } ) _ { i } t ^ { 2 } \cos ( \mathrm { A R G U M E N T } ) ] } \\ & { + \cdot \cdot , } \end{array}
$$

$$
\begin{array} { r l } { Y = } & { - 0 . 0 0 6 9 5 1 ^ { \prime \prime } - 0 . 0 2 5 8 9 6 ^ { \prime \prime } t - 2 2 . 4 0 7 2 7 4 7 ^ { \prime \prime } t ^ { 2 } } \\ & { + 0 . 0 0 1 9 0 0 5 9 ^ { \prime \prime } t ^ { 3 } + 0 . 0 0 1 1 1 2 5 2 6 ^ { \prime \prime } t ^ { 4 } + 0 . 0 0 0 0 0 0 1 3 5 8 ^ { \prime \prime } t ^ { 5 } } \\ & { + \sum _ { i } [ ( b _ { \mathrm { c , 0 } } ) _ { i } \cos ( \mathrm { A R G U M E N T } ) + ( b _ { \mathrm { s , 0 } } ) _ { i } \sin ( \mathrm { A R G U M E N T } ) ] } \\ & { + \sum _ { i } [ ( b _ { \mathrm { c , 1 } } ) _ { i } t \cos ( \mathrm { A R G U M E N T } ) + ( b _ { \mathrm { s , 1 } } ) _ { i } \ t \sin ( \mathrm { A R G U M E N T } ) ] } \\ & { + \sum _ { i } [ ( b _ { \mathrm { c , 2 } } ) _ { i } t ^ { 2 } \cos ( \mathrm { A R G U M E N T } ) + ( b _ { \mathrm { s , 2 } } ) _ { i } t ^ { 2 } \sin ( \mathrm { A R G U M E N T } ) ] } \\ & { + \cdots , } \end{array}
$$

the parameter $t$ being given by expression (5.2) and ARGUMENT being a function of the fundamental arguments of the nutation theory, whose expressions are given by Eq. (5.43) for the lunisolar ones and Eq. (5.44) for the planetary ones. The full IAU 2000/2006 series are available electronically on the IERS Conventions Center website (Tables 5.2a and 5.2b) at $< { } ^ { 2 } >$ , tab5.2a.txt for the $X$ coordinate and tab5.2b.txt for the $Y$ coordinate. The polynomial terms of $X$ and $Y$ are given in (5.16). An extract from Tables $5 . 2 \mathrm { a }$ and 5.2b for the largest non-polynomial terms in $X$ and $Y$ is given below.

The numerical values of the coefficients of the polynomial part of $X$ and $Y$ (cf. (5.16)) are derived from the development as a function of time of the precession in longitude and obliquity and pole offset at J2000.0 and the amplitudes $( a _ { s , j } ) _ { i }$ , $( a _ { c , j } ) _ { i }$ , $( b _ { c , j } ) _ { i }$ , $( b _ { s , j } ) _ { i }$ for $j = 0 , 1 , 2$ , ... are derived from the amplitudes of the precession and nutation series. The amplitudes $( a _ { s , 0 } ) _ { i }$ , $( b _ { c , 0 } ) _ { i }$ of the sine and cosine terms in $X$ and $Y$ respectively are equal to the amplitudes $A _ { i } \times \sin \epsilon _ { 0 }$ and $B _ { i }$ of the series for nutation in longitude $[ \times \sin \epsilon _ { 0 } ]$ and obliquity, except for a few terms in each coordinate $X$ and $Y$ which contain a contribution from crossednutation effects. The coordinates $X$ and $Y$ contain Poisson terms in $t \sin$ , $t \cos$ , $t ^ { 2 } \sin$ , $t ^ { 2 }$ cos, ... which originate from crossed terms between precession and nutation.

Table 5.2a: Extract from Table 5.2a (available at $< { } ^ { 2 } >$ ) for the largest non-polynomial terms (i.e. coefficients of the Fourier and Poisson terms, with $t$ in Julian centuries) in the development (5.16) for $X ( t )$ compatible with the IAU 2006/2000A precession-nutation model (unit µas). The expressions for the fundamental arguments appearing in columns 4 to 17 are given by Eq. (5.43) and Eq. (5.44). (Because the largest terms are all luni-solar, columns 9-17 contain only zeros in the extract shown.)   

<table><tr><td>i</td><td>(as,0）i</td><td>(ac,0）i</td><td></td><td></td><td>FD</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>）Ω LMe Lve LE LMa Lj Lsa LU I</td><td></td><td>LNe</td><td>PA</td></tr><tr><td>1</td><td>-6844318.44</td><td>1328.67</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>-523908.04</td><td>-544.75</td><td>0</td><td>0</td><td>2</td><td>-2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>3</td><td>-90552.22</td><td>111.23</td><td>0</td><td>0</td><td>2</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>4</td><td>82168.76</td><td>-27.64</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>5</td><td>58707.02</td><td>470.05</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>i</td><td>(as,1)i</td><td>(ac,1)i</td><td>l</td><td>1</td><td>F</td><td>D</td><td></td><td></td><td>Ω LMe Lve</td><td></td><td></td><td></td><td>LE LMa Lj Lsa</td><td>Lu</td><td>LNe</td><td>PA</td></tr><tr><td>1307</td><td>-3309.73</td><td>205833.11</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1308</td><td>198.97</td><td>12814.01</td><td>0</td><td>0</td><td>2</td><td>-2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1309</td><td></td><td>2187.91</td><td>0</td><td>0</td><td>2</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td></td><td>41.44</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

The contributions (in $\mu \mathrm { a s }$ ) to expression (5.16) from the frame biases are

$$
\begin{array} { r l r } { d X } & { = } & { - 1 6 6 1 7 . 0 - 1 . 6 \ t ^ { 2 } + 0 . 7 \ \cos \Omega , } \\ { d Y } & { = } & { - 6 8 1 9 . 2 - 1 4 1 . 9 \ t + 0 . 5 \ \sin \Omega , } \end{array}
$$

the first term in each coordinate being the contribution from the celestial pole offset at J2000.0 and the following ones from the equinox offset at J2000.0, also called “frame bias in right ascension.”

The polynomial changes in $X$ and $Y$ due to the change in the precession model from IAU 2000 to IAU 2006 can be written in $\mu$ as as (Capitaine and Wallace, 2006, after correcting a typographical error in the $t ^ { 2 }$ term of $d Y$ ):

$$
\begin{array} { r l } { d X = } & { { } 1 5 5 t - 2 5 6 4 t ^ { 2 } + 2 t ^ { 3 } + 5 4 t ^ { 4 } , } \\ { d Y = } & { { } - 5 1 4 t - 2 4 t ^ { 2 } + 5 8 t ^ { 3 } - 1 t ^ { 4 } - 1 t ^ { 5 } . } \end{array}
$$

In addition, there are slight changes in a few periodic terms of the IAU 2006 version of the $X , Y$ series with respect to the IAU 2000 version, corresponding to additional Poisson terms in nutation caused by introducing the IAU 2006 $J _ { 2 }$ rate value (see Section 5.6.3). The largest changes (Capitaine and Wallace, 2006) in $\mu { \mathrm { a s } }$ are:

$$
\begin{array} { r l } { d X _ { J 2 d } = } & { { } 1 8 . 8 ~ t \sin \Omega + 1 . 4 ~ t \sin 2 ( F - D + \Omega ) , } \\ { d Y _ { J 2 d } = } & { { } - 2 5 . 6 ~ t \cos \Omega - 1 . 6 ~ t \cos 2 ( F - D + \Omega ) . } \end{array}
$$

The periodic terms expressed by (5.19) are included in the IAU 2006/2000A version of the $X , Y$ series. The difference between the IAU 2006 and IAU 2000A expressions for $X$ and $Y$ is available electronically on the IERS Conventions Center website (Table 5.2f) at $< { } ^ { 2 } >$ in file tab5.2f.txt.

The relationships between the coordinates $X$ and $Y$ and the precession-nutation quantities are (Capitaine, 1990):

$$
\begin{array} { r l r } { X } & { { } = } & { \bar { X } + \xi _ { 0 } - d \alpha _ { 0 } \bar { Y } , } \\ { Y } & { { } = } & { \bar { Y } + \eta _ { 0 } + d \alpha _ { 0 } \bar { X } , } \end{array}
$$

where $\xi _ { 0 }$ and $\eta _ { 0 }$ are the celestial pole offsets at the basic epoch J2000.0 and $d \alpha _ { 0 }$ the right ascension of the mean equinox of $J 2 0 0 0 . 0$ in the GCRS (i.e. frame bias in right ascension). (See the numbers provided below in (5.21) and (5.33) for these quantities.)

Table 5.2b: Extract from Table 5.2b (available at $< { } ^ { 2 } >$ ) for the largest non-polynomial terms (i.e. coefficients of the Fourier and Poisson terms, with $t$ in Julian centuries) in the development (5.16) $Y ( t )$ compatible with the IAU 2006/2000A precession-nutation model (unit $\mu$ as). The expressions for the fundamental arguments appearing in columns 4 to 17 are given by Eq. (5.43) and Eq. (5.44). (Because the largest terms are all luni-solar, columns 9-17 contain only zeros in the extract shown.)   

<table><tr><td>i</td><td>(bs,0)i</td><td>(bc,0）i</td><td>1</td><td>1</td><td>F</td><td>D</td><td>Ω LMe Lve </td><td></td><td></td><td>LE LMa</td><td></td><td>LJ</td><td>Lsa</td><td>Lu</td><td>LNe</td><td>PA</td></tr><tr><td>1</td><td>1538.18</td><td>9205236.26</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>-458.66</td><td>573033.42</td><td>0</td><td>0</td><td>2</td><td>-2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>3</td><td>137.41</td><td>97846.69</td><td>0</td><td>0</td><td>2</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>4</td><td>-29.05</td><td>-89618.24</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>5</td><td>-17.40</td><td>22438.42</td><td>0</td><td>1</td><td>2</td><td>-2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>i</td><td>(bs,1)i</td><td>(bc,1)i</td><td>1</td><td>1</td><td>F</td><td>D</td><td>Ω</td><td>LMe</td><td>Lve</td><td>LE</td><td>LMa</td><td>LJ</td><td>Lsa</td><td>Lu</td><td>LNe</td><td>PA</td></tr><tr><td>963</td><td>153041.79</td><td>853.32</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>964</td><td>11714.49</td><td>-290.91</td><td>0</td><td>0</td><td>2</td><td>-2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>965</td><td>2024.68</td><td>-51.26</td><td>0</td><td>0</td><td>2</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>…</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

The mean equinox of J2000.0 to be considered is not the “rotational dynamical mean equinox of J2000.0” as used in the past, but the “inertial dynamical mean equinox of $\mathrm { J 2 0 0 0 . 0 ^ { \circ } }$ to which the recent numerical or analytical solutions refer. The latter is associated with the ecliptic in the inertial sense, which is the plane perpendicular to the angular momentum vector of the orbital motion of the Earth-Moon barycenter as computed from the velocity of the barycenter relative to an inertial system. The rotational equinox is associated with the ecliptic in the rotational sense, which is perpendicular to the angular momentum vector computed from the velocity referred to the rotating orbital plane of the Earth-Moon barycenter. (The difference between the two angular momenta is the angular momentum associated with the rotation of the orbital plane.) See Standish (1981) for more details. The numerical value for $d \alpha _ { 0 }$ as derived from Chapront et al. (2002) to be used in expression (5.20) is:

$$
d \alpha _ { 0 } = ( - 0 . 0 1 4 6 0 \pm 0 . 0 0 0 5 0 ) ^ { \prime \prime } .
$$

Quantities $X$ and $Y$ are given by:

$$
\begin{array} { r c l } { { \bar { X } } } & { { = } } & { { \sin \omega \sin \psi , } } \\ { { \bar { Y } } } & { { = } } & { { - \sin \epsilon _ { 0 } \cos \omega + \cos \epsilon _ { 0 } \sin \omega \cos \psi } } \end{array}
$$

where $\epsilon _ { 0 }$ $= 8 4 3 8 1 . 4 0 6 ^ { \prime \prime }$ ) is the IAU 2006 value for the obliquity of the ecliptic at J2000.0 (from Chapront et al., 2002), $\omega$ , and $\psi$ is the longitude, on the ecliptic of epoch, of the node of the true equator of date on the fixed ecliptic of epoch; these quantities are such that

$$
\omega = \omega _ { A } + \Delta \epsilon _ { 1 } ; \qquad \psi = \psi _ { A } + \Delta \psi _ { 1 } ,
$$

where $\psi _ { A }$ and $\omega _ { A }$ are the precession quantities in longitude and obliquity (Lieske et al., 1977) referred to the ecliptic of epoch and $\Delta \psi _ { 1 }$ , $\Delta \epsilon _ { 1 }$ are the nutation angles in longitude and obliquity referred to the ecliptic of epoch. (See the numerical developments provided for the precession quantities in (5.39).) $\Delta \psi _ { 1 }$ , $\Delta \epsilon _ { 1 }$ can be obtained from the nutation angles $\Delta \psi$ , $\Delta \epsilon$ in longitude and obliquity referred to the ecliptic of date. The following formulation from Aoki and Kinoshita (1983) is accurate to better than one microarcsecond after one century:

$$
\begin{array} { r l r } { \Delta \psi _ { 1 } \sin \omega _ { A } } & { = } & { \Delta \psi \sin \epsilon _ { A } \cos \chi _ { A } - \Delta \epsilon \sin \chi _ { A } , } \\ { \Delta \epsilon _ { 1 } } & { = } & { \Delta \psi \sin \epsilon _ { A } \sin \chi _ { A } + \Delta \epsilon \cos \chi _ { A } , } \end{array}
$$

$\epsilon _ { A }$ being the mean obliquity of date and $\chi A$ the precession of the ecliptic along the equator (Lieske et al., 1977).

As VLBI observations have shown that there are deficiencies in the IAU 2006/2000A precession-nutation model of the order of 0.2 mas, mainly due to the fact that the free core nutation (FCN) (see Section 5.5.5) is not part of the model, the IERS will continue to publish observed estimates of the corrections to the IAU precessionnutation model. The observed differences with respect to the conventional celestial pole position defined by the models are monitored and reported by the IERS as “celestial pole offsets.” Such time-dependent offsets from the direction of the pole of the GCRS must be provided as corrections $\delta X$ and $\delta Y$ to the $X$ and $Y$ coordinates. These corrections can be related to the equinox based celestial pole offsets $\delta \psi$ (along the ecliptic of date) and $\delta \epsilon$ (in the obliquity of date) using the relationships (5.22) between $X$ and $Y$ and the precession-nutation quantities and (5.24) for the transformation from ecliptic of date to ecliptic of epoch. The relationship (5.25) below, which is to first order in the quantities, ensures an accuracy of one microarcsecond for one century, for values of $\delta \psi$ and $\delta \epsilon$ lower than 1 mas:

$$
\begin{array} { r l r } { \delta X } & { = } & { \delta \psi \sin \epsilon _ { A } + ( \psi _ { A } \cos \epsilon _ { 0 } - \chi _ { A } ) \delta \epsilon , } \\ { \delta Y } & { = } & { \delta \epsilon - ( \psi _ { A } \cos \epsilon _ { 0 } - \chi _ { A } ) \delta \psi \sin \epsilon _ { A } . } \end{array}
$$

These observed offsets include the contribution of the FCN described in Section 5.5.5. Using these offsets, the corrected celestial position of the CIP is given by

$$
X = X ( \mathrm { I A U ~ 2 0 0 6 } / 2 0 0 0 ) + \delta X , \qquad Y = Y ( \mathrm { I A U ~ 2 0 0 6 } / 2 0 0 0 ) + \delta Y .
$$

This is practically equivalent to replacing the transformation matrix $Q$ with the rotation

$$
\tilde { Q } = \left( \begin{array} { c c c } { { 1 } } & { { 0 } } & { { \delta X } } \\ { { 0 } } & { { 1 } } & { { \delta Y } } \\ { { - \delta X } } & { { - \delta Y } } & { { 1 } } \end{array} \right) Q _ { \mathrm { I A U } } ,
$$

where $Q _ { \mathrm { I A U } }$ represents the $Q ( t )$ matrix based on the IAU 2006/2000 precessionnutation model.

# 5.5.5 Free Core Nutation

Free core nutation is a free retrograde diurnal motion of the Earth’s rotation axis with respect to the Earth caused by the interaction of the mantle and the fluid, ellipsoidal core as it rotates. Due to the definition of the CIP, this free motion appears as a motion of the CIP in the GCRS. Because this effect is a free motion with time-varying excitation and damping resulting in a variable amplitude and phase, a FCN model was not included in the IAU 2000A nutation model. As a result, a quasi-periodic un-modeled motion of the CIP in the GCRS at the 0.1–0.3 mas level still exists after the IAU 2006/2000A model has been taken into account.

Depending on accuracy requirements, the lack of a FCN model should cause negligible problems. However, for the most stringent accuracy applications, a FCN model may be incorporated to account for the FCN contribution to the CIP motion in the GCRS.

The FCN model of Lambert (2007) can be found at ${ < } ^ { 4 } >$ and a copy is kept at the IERS Conventions Center website $< ^ { 2 } >$ . It is expected that the coefficients of the model will be updated regularly by the IERS to describe the most currently observed FCN motion of the CIP. Successive versions are identified by a date included in their name, the current realization (fcnnut100701) has been established on July $1 ^ { s t }$ , 2010.

Table 5.2c: Table for the coefficients of the empirical model of the retrograde FCN during the interval 1984-2010 (unit µas).   

<table><tr><td>Year</td><td>MJD</td><td>Xc</td><td>Xs</td><td>Sx</td></tr><tr><td>1984.0</td><td>45700.0</td><td>4.5</td><td>-36.6</td><td>19.7</td></tr><tr><td>1985.0</td><td>46066.0</td><td>-141.8</td><td>-105.3</td><td>11.1</td></tr><tr><td>1986.0</td><td>46431.0</td><td>-246.6</td><td>-170.2</td><td>9.5</td></tr><tr><td>1987.0</td><td>46796.0</td><td>-281.9</td><td>-159.2</td><td>8.6</td></tr><tr><td>1988.0</td><td>47161.0</td><td>-255.0</td><td>-43.6</td><td>8.1</td></tr><tr><td>1989.0</td><td>47527.0</td><td>-210.5</td><td>-88.6</td><td>7.3</td></tr><tr><td>1990.0</td><td>47892.0</td><td>-187.8</td><td>-57.4</td><td>6.4</td></tr><tr><td>1991.0</td><td>48257.0</td><td>-163.0</td><td>26.3</td><td>5.5</td></tr><tr><td>1992.0</td><td>48622.0</td><td>-141.2</td><td>44.6</td><td>4.8</td></tr><tr><td>1993.0</td><td>48988.0</td><td>-128.7</td><td>28.6</td><td>4.6</td></tr><tr><td>1994.0</td><td>49353.0</td><td>-108.9</td><td>19.5</td><td>3.9</td></tr><tr><td>1995.0</td><td>49718.0</td><td>-96.7</td><td>19.7</td><td>3.1</td></tr><tr><td>1996.0</td><td>50083.0</td><td>-104.0</td><td>11.9</td><td>2.9</td></tr><tr><td>1997.0</td><td>50449.0</td><td>-126.8</td><td>30.4</td><td>2.8</td></tr><tr><td>1998.0</td><td>50814.0</td><td>-81.9</td><td>25.0</td><td>2.6</td></tr><tr><td>1999.0</td><td>51179.0</td><td>-19.7</td><td>-20.1</td><td>2.6</td></tr><tr><td>2000.0</td><td>51544.0</td><td>10.8</td><td>-76.8</td><td>2.7</td></tr><tr><td>2001.0</td><td>51910.0</td><td>65.6</td><td>-137.4</td><td>2.5</td></tr><tr><td>2002.0</td><td>52275.0</td><td>78.2</td><td>-127.1</td><td>2.3</td></tr><tr><td>2003.0</td><td>52640.0</td><td>108.7</td><td>-42.3</td><td>2.1</td></tr><tr><td>2004.0</td><td>53005.0</td><td>117.6</td><td>-1.4</td><td>2.2</td></tr><tr><td>2005.0</td><td>53371.0</td><td>115.7</td><td>5.7</td><td>2.9</td></tr><tr><td>2006.0</td><td>53736.0</td><td>159.7</td><td>24.2</td><td>4.2</td></tr><tr><td>2007.0</td><td>54101.0</td><td>154.7</td><td>61.2</td><td>4.5</td></tr><tr><td>2008.0</td><td>54466.0</td><td>161.1</td><td>98.4</td><td>4.3</td></tr><tr><td>2009.0</td><td>54832.0</td><td>143.4</td><td>147.0</td><td>4.5</td></tr><tr><td>2010.0</td><td>55197.0</td><td>81.8</td><td>152.9</td><td>5.6</td></tr></table>

The model describes the quantities to be added to the X, Y coordinates of the CIP in the GCRS to account for the FCN effect. It provides this information in the form of a time-varying sinusoidal representation that assumes a constant period of $P = - 4 3 0 . 2 3$ days. The equations for the model are

$$
\begin{array} { r l } { X _ { F C N } } & { { } = X _ { S } \sin ( \sigma t ) + X _ { C } \cos ( \sigma t ) , } \\ { Y _ { F C N } } & { { } = Y _ { S } \sin ( \sigma t ) + Y _ { C } \cos ( \sigma t ) , } \end{array}
$$

where $\sigma$ is the angular frequency of the FCN $( = 2 \pi / P$ rad/d) and $t$ is given in days since J2000.0.

Table 5.2c provides the coefficients for the model fcnnut100701. Older versions and updates can be found at $< { } ^ { 4 } >$ . $X _ { C }$ and $X _ { S }$ are the amplitudes of the cosine and sine terms, respectively, and are piecewise defined in time. $S _ { X }$ is the formal error of the amplitude estimates. All amplitudes are in units of microarcseconds. Note that the values for $Y _ { S }$ and $Y _ { C }$ can be determined from the relationships $Y _ { S } = - X _ { C }$ and $Y _ { C } = X _ { S }$ .

Over the period for which the model has been determined, the model should provide accuracies better than 0.05 mas rms while for the period of extrapolation the model should provide accuracies better than 0.1 mas rms until the next annual update is provided.

Note that the unmodeled FCN motion of the CIP is included in the published IERS celestial pole offsets dX and dY. These offsets should not be applied when the FCN model is used.

# 5.5.6 Position of the Celestial Intermediate Origin in the GCRS

The numerical development of the quantity $s$ (i.e. the CIO locator) appearing in Eq. (5.10), compatible with the IAU 2006/2000A precession-nutation model as well as the corresponding celestial offset at J2000.0, has been derived in a way similar to that based on the IERS Conventions 2003 (Capitaine et al., 2003b). It results from expression (5.8) for $s$ using the developments of $X$ and $Y$ as functions of time given by (5.16) (Capitaine et al., 2003a). The numerical development is provided for the quantity $s + X Y / 2$ , which requires fewer terms to reach the same accuracy than a direct development for $s$ .

Table 5.2d: Development of $s ( t )$ compatible with the IAU 2006/2000A precession-nutation model: all terms exceeding 0.5 µas during the interval 1975–2025 (unit $\mu$ as). The expressions for the fundamental arguments appearing in column 1 are given by Eq. (5.43).   

<table><tr><td colspan="2">s(t) ）= -XY/2+94+3808.65t -122.68t²-72574.11t³ +∑k Ck sin αk +1.73t sin Ω + 3.57t cos 2Ω + 743.52t² sin Ω + 56.91t² sin(2F - 2D + 2Ω) +9.84t² sin(2F + 2) -8.85t² sin 2Ω</td></tr><tr><td>Argument &amp;k</td><td>Amplitude Ck</td></tr><tr><td>Ω</td><td>-2640.73</td></tr><tr><td>2Ω</td><td>-63.53</td></tr><tr><td>2F-2D+3Ω</td><td>-11.75</td></tr><tr><td>2F-2D+Ω</td><td>-11.21</td></tr><tr><td>2F-2D+2Ω</td><td>+4.57</td></tr><tr><td>2F+3Ω</td><td>-2.02 -1.98</td></tr><tr><td>2F+Ω 3Ω</td><td>+1.72</td></tr><tr><td>l&#x27;+Ω</td><td>+1.41</td></tr><tr><td>l-Ω</td><td>+1.26</td></tr><tr><td>1+Ω</td><td>+0.63</td></tr><tr><td>1-Ω</td><td>+0.63</td></tr></table>

The constant term for s, which was previously chosen so that $s ( J 2 0 0 0 . 0 ) = 0$ , was subsequently fitted (Capitaine et al., 2003b) so as to ensure continuity of UT1 at the date of change (1 January 2003) consistent with the Earth Rotation Angle (ERA) relationship and the current VLBI procedure for estimating UT1 (see (5.31)).

The complete series for $s + X Y / 2$ with all terms larger than $0 . 1 \mu \mathrm { a s }$ is available electronically on the IERS Conventions Center website $< { } ^ { 2 } >$ in file tab5.2d.txt and the terms larger than 0.5 µas over 25 years in the development of $s$ are provided in Table 5.2d with $\mu$ as accuracy. (There is no term where the change from IAU 2000 precession to IAU 2006 precession causes a change in $s$ larger than $1 \mu \mathrm { a s }$ after one century.)

# 5.5.7 ERA based expressions for Greenwich Sidereal Time

Greenwich Sidereal Time (GST), which refers to the equinox, is related to the “Earth Rotation Angle” ERA, that refers to the Celestial Intermediate Origin (CIO), by the following relationship (Aoki and Kinoshita, 1983; Capitaine and Gontier, 1993) at the microarcsecond level:

$$
\mathrm { G S T } = d T _ { 0 } + \mathrm { E R A } + \int _ { t _ { 0 } } ^ { t } ( \dot { \psi _ { A } } + \widehat { \Delta \psi _ { 1 } } ) \cos ( \omega _ { A } + \Delta \epsilon _ { 1 } ) d t - \chi _ { A } + \Delta \psi \cos \epsilon _ { A } + \Delta \psi _ { 1 } \cos \omega _ { A } ,
$$

$\Delta \psi _ { 1 }$ , $\Delta \epsilon _ { 1 }$ , given by (5.24), being the nutation angles in longitude and obliquity referred to the ecliptic of epoch and $\chi A$ , whose development is given in (5.40), the precession of the ecliptic along the equator (i.e. the right ascension component of the precession of the ecliptic).

This can be written as:

$$
\mathrm { G S T } = \mathrm { E R A } ( \mathrm { U T 1 } ) - \mathrm { E O } ,
$$

where EO is the “equation of the origins”, defined by:

$$
\mathrm { E O } = - \ d T _ { 0 } - \int _ { t _ { 0 } } ^ { t } ( \stackrel { \cdot \cdot } { \psi _ { A } + \Delta \psi _ { 1 } } ) \cos ( \omega _ { A } + \Delta \epsilon _ { 1 } ) d t + \chi _ { A } - \Delta \psi \cos \epsilon _ { A } + \Delta \psi _ { 1 } \cos \omega _ { A } ,
$$

which is the CIO based right ascension of the equinox along the moving equator. The EO accounts for the accumulated precession and nutation in right ascension from J2000.0 to the date $\mathrm { t }$ ; the constant term $d \%$ was chosen to ensure continuity in UT1 at the date of change. A numerical expression for EO consistent with the IAU 2006/2000A precession-nutation model was provided by Capitaine et al. (2003c). The expression was obtained using computations similar to those performed for $s$ and following a procedure, described below, that ensured consistency at the microarcsecond level among the transformations, as well as continuity in UT1 at the date of change (Capitaine et al., 2003b).

The full series providing the expression for Greenwich Sidereal Time based on the IAU 2006/2000A precession-nutation model are available on the IERS Conventions Center website $< { } ^ { 2 } >$ in file tab5.2e.txt; the terms larger than 0.5 µas over 25 years in the development of the EO are provided in Table 5.2e. to 0.01 microarcsecond accuracy (i.e. with two digits).

Table 5.2e: Development of EO compatible with IAU 2006/2000A precession-nutation model: all terms exceeding $0 . 5 \mu \mathrm { a s }$ during the interval 1975–2025 (unit µas).   

<table><tr><td colspan="2">EO = - 0.014506&quot; - 4612.156534&quot;t - 1.3915817&quot;t² +0.00000044&quot;t³ - △ψcos ∈A - ∑k C sin αk</td></tr><tr><td>Argument αk Ω</td><td>Amplitude Ck +2640.96</td></tr></table>

The $C _ { k } ^ { \prime }$ coefficients are similar to the $C _ { k }$ coefficients appearing in Table 5.2d providing the development for $s$ , and are equal to these coefficients up to $1 \mu \mathrm { a s }$ . The last term in the EO expression, i. $\begin{array} { r } { \mathrm { ~ \ -- ~ } \sum _ { k } C _ { k } ^ { \prime } \sin \alpha _ { k } } \end{array}$ , comprises the complementary terms to be subtracted from the classical “equation of the equinoxes,” $\Delta { \psi } \cos \epsilon _ { A }$ , to provide the relationship between GST and ERA with microarcsecond accuracy. These were introduced in the IERS Conventions 2003, replacing the two complementary terms provided in the IERS Conventions 1996. A secular term similar to that appearing in the quantity $s$ is included in expression (5.31). This expression for GST used in the equinox based transformation ensures consistency with the CIO based transformation at the microarcsecond level after one century, using expressions (5.14) for ERA, (5.16) for the celestial coordinates of the CIP and Table 5.2d for $s$ .

As an alternative to using the developments set out in Table 5.2e, the EO can be calculated from the quantity $s$ and the classical (i.e. equinox based) nutation $\times$ precession $\times$ bias matrix: see Wallace and Capitaine (2006), Eq. (5.16). This is the method used by SOFA.

The numerical values chosen for the constant term $d \%$ in GST to achieve continuity in UT1 at the transition date (1 January 2003), and for the corresponding constant term in $s$ are $d T _ { 0 } = + 1 4 5 0 6 \mu \mathrm { a s }$ and $s _ { 0 } = + 9 4 \mu { \mathrm { a s } }$ . The polynomial part of GST (i.e. of ERA(UT1) − EO(t)) provides the IAU 2006 expression for Greenwich Mean Sidereal Time, GMST (Capitaine et al., 2003c):

$$
\begin{array} { l c l } { { \mathrm { M S T } } } & { { = } } & { { \mathrm { E R A } ( \mathrm { U T 1 } ) + 0 . 0 1 4 5 0 6 ^ { \prime \prime } + 4 6 1 2 . 1 5 6 5 3 4 ^ { \prime \prime } t + 1 . 3 9 1 5 8 1 7 ^ { \prime \prime } t ^ { 2 } - 0 . 0 0 0 0 0 0 0 4 4 ^ { \prime \prime } t ^ { 3 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - 0 . 0 0 0 0 2 9 9 5 6 ^ { \prime \prime } t ^ { 4 } - 0 . 0 0 0 0 0 0 0 0 3 6 8 ^ { \prime \prime } t ^ { 5 } . } } \end{array}
$$

This expression for GMST clearly distinguishes between ERA, which is expressed as a function of UT1, and the EO (i.e. mainly the accumulated precession-nutation in right ascension), which is expressed as a function of TDB (or, in practice, TT), in contrast to the GMST1982(UT1) expression (Aoki et al., 1982), which used only UT1. The difference between these two processes gives rise to a term in GMST of (TT $^ { \circ } -$ UT1) multiplied by the speed of precession in right ascension. Using TT $^ { 1 } -$ TAI = 32.184 s, this was: [47+1.5(TAI $-$ UT1)] µas, where TAI−UT1 is in seconds. On 1 January 2003, this difference was about $9 4 \mu \mathrm { a s }$ (see Gontier in Capitaine et al., 2002), using the value of 32.3 s for TAI $-$ UT1. This is included in the values for $d \bar { \cal I } _ { 0 } ^ { \prime }$ and $s _ { 0 }$ .

# 5.6 Description of the IAU 2000/2006 precession-nutation model

The following sections describe the main features of the IAU 2006/2000 precessionnutation. Comparisons of the IAU 2000/2006 precession-nutation with other models and VLBI observations can be found in Capitaine et al. (2009).

# 5.6.1 The IAU 2000A and IAU 2000B nutation model

The IAU 2000A model, developed by Mathews et al., (2002) and denoted MHB-2000, is based on the REN2000 rigid Earth nutation series of Souchay et al. (1999) for the axis of figure (available at: ftp://syrte.obspm.fr/pub/REN2000/). The REN2000 solution is provided as a series of luni-solar and planetary nutations in longitude and obliquity, referred to the ecliptic of date, expressed as “in-phase” and “out-of-phase” components with their time variations. The sub-diurnal terms arising for the imperfect axial symmetry of the Earth are not part of this solution, so that the axis of reference of the nutation model be compliant with the definition of the CIP.

The rigid Earth nutation was transformed to the non-rigid Earth nutation by applying the MHB2000 “transfer function” to the full REN2000 series of the corresponding prograde and retrograde nutations and then converting back into elliptical nutations. This “transfer function” is based on the solution of the linearized dynamical equation of the wobble-nutation problem and makes use of estimated values of seven of the parameters appearing in the theory (called “Basic Earth Parameters” (BEP)), obtained from a least-squares fit of the theory to an up-to-date precession-nutation VLBI data set (Herring et al., 2002). The estimation of the dynamical ellipticity of the Earth resulting in a value differing slightly from that of the reference rigid Earth series (i.e. by the multiplying factor 1.000012249) was a part of the estimation of the parameters needed for the non-rigid Earth series. The MHB2000 model improves the IAU 1980 theory of nutation by taking into account the effect of mantle anelasticity, ocean tides, electromagnetic couplings produced between the fluid outer core and the mantle as well as between the solid inner core and fluid outer core (Buffett et al., 2002) and the consideration of nonlinear terms which have hitherto been ignored in this type of formulation. The axis of reference is the axis of maximum moment of inertia of the Earth in steady rotation (i.e. ignoring time-dependent deformations).

The resulting nutation series includes 678 lunisolar terms and 687 planetary terms which are expressed as “in-phase” and “out-of-phase” components with their time variations (see expression(5.35)). That model is expected to have an accuracy of about $1 0 \mu \mathrm { a s }$ for most of its terms. On the other hand, the FCN, being a free motion which cannot be predicted rigorously (see Section 5.5.5), is not considered a part of the IAU 2000A model, which limits the accuracy in the computed direction of the celestial pole in the GCRS to about 0.3 mas.

The IAU 2000A nutation series is associated with the following offset (originally provided as frame bias in $\mathrm { d } \psi _ { b i a s }$ and $\mathrm { d } \epsilon _ { b i a s }$ ) of the direction of the CIP at J2000.0 from the direction of the pole of the GCRS:

$$
\begin{array} { r l r } { \xi _ { 0 } } & { { } = } & { ( - 0 . 0 1 6 6 1 7 0 \pm 0 . 0 0 0 0 1 0 0 ) ^ { \prime \prime } , } \\ { \eta _ { 0 } } & { { } = } & { ( - 0 . 0 0 6 8 1 9 2 \pm 0 . 0 0 0 0 1 0 0 ) ^ { \prime \prime } . } \end{array}
$$

The IAU 2000A nutation includes the geodesic nutation contributions to the annual, semiannual and 18.6-year terms to be consistent with including the geodesic precession ( $p _ { g } = 1 . 9 2 ^ { \prime \prime }$ /century) in the precession model and so that the BCRS and GCRS are without any time-dependent rotation. The theoretical geodesic nutation contribution (Fukushima, 1991) used in the MHB2000 model (Mathews et al., 2002) is, in $\mu \mathrm { a s }$ , for the nutations in longitude $\Delta \psi _ { g }$ and obliquity $\Delta \epsilon _ { g }$

$$
\begin{array} { r c l } { { \Delta \psi _ { g } } } & { { = } } & { { - 1 5 3 \ \sin l ^ { \prime } - 2 \ \sin 2 l ^ { \prime } + 3 \ \sin \Omega , } } \\ { { } } & { { } } & { { } } \\ { { \Delta \epsilon _ { g } } } & { { = } } & { { 1 \ \cos \Omega , } } \end{array}
$$

where $l ^ { \prime }$ is the mean anomaly of the Sun and $\Omega$ the longitude of the ascending node of the Moon.

The IAU 2000 nutation model is given by a series for nutation in longitude $\Delta \psi$ and obliquity $\Delta \epsilon$ , referred to the ecliptic of date, with $t$ measured in Julian centuries from epoch J2000.0:

$$
\begin{array} { r l r } { \Delta \psi } & { = } & { \sum _ { i = 1 } ^ { N } ( A _ { i } + A _ { i } ^ { \prime } t ) \sin ( \mathrm { A R G U M E N T } ) + ( A _ { i } ^ { \prime \prime } + A _ { i } ^ { \prime \prime \prime } t ) \cos ( \mathrm { A R G U M E N T } ) , } \\ & { } & \\ { \Delta \epsilon } & { = } & { \sum _ { i = 1 } ^ { N } ( B _ { i } + B _ { i } ^ { \prime } t ) \cos ( \mathrm { A R G U M E N T } ) + ( B _ { i } ^ { \prime \prime } + B _ { i } ^ { \prime \prime \prime } t ) \sin ( \mathrm { A R G U M E N T } ) . } \end{array}
$$

More details about the coefficients and arguments of these series will be given in Section 5.7.

The original IAU 2000A nutation series are available electronically on the IERS Conventions Center website at $< ^ { 5 } >$ in the files tab5.3a.txt and tab5.3b.txt for the lunisolar and planetary components, respectively. The “total nutation” includes all components.

The series corresponding to nutation “IAU $2 0 0 0 \mathrm { { A _ { R 0 6 } } ^ { 3 } }$ ” (see Section 5.6.3 for the definition of the subscript “R06”) are available electronically at ${ < } ^ { 2 } { > }$ . They are provided by the files tab5.3a.txt (Table 5.3a) and tab5.3b.txt (Table 5.3b), for nutation in longitude $\Delta \psi$ and obliquity $\Delta \epsilon$ , respectively. An extract from Tables 5.3a and 5.3b for the largest nutation components is given below. (Note that the headings of those files as well as the caption below have changed with respect to the IERS Conventions (2003) available at $< ^ { 5 } >$ .)

As recommended by IAU 2000 Resolution B1.6, an abridged model, designated IAU 2000B, is available for those who need a model only at the 1 mas level. Such a model has been developed by McCarthy and Luzum (2003). It includes fewer than 80 lunisolar terms plus a bias to account for the effect of the planetary terms in the time period under consideration. It provides the celestial pole motion with an accuracy that does not result in a difference greater than 1 mas with respect to that of the IAU 2000A model during the period 1995–2050. The model is implemented in the Fortran subroutine IAU2000B.f, available electronically on the IERS Conventions Center website at $< ^ { 5 } >$ .

Table 5.3a: Extract from Table 5.3a (nutation in longitude) (available at $< { } ^ { 2 } >$ ) providing the largest components for the “in-phase” and “out-of-phase” terms of the “IAU $2 0 0 0 \mathrm { A _ { R 0 6 } }$ ” nutation. Units are $\mu$ as and $\mu$ as/century for the coefficients and their time variations, respectively. The expressions for the Delaunay arguments appearing in columns 1 to 5 are given by Eq. (5.43); those for the additional fundamental arguments of the planetary nutations appearing in columns 6 to 14 (bottom part) are given by Eq. (5.44). (Because the largest terms are all luni-solar, columns 9-17 contain only zeros in the extract shown.)   

<table><tr><td>i</td><td>Ai</td><td>A</td><td>1</td><td>l</td><td>F</td><td>D</td><td>Ω LMe Lve LE LMa Lj Lsa</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Lu</td><td>LNe</td><td>PA</td></tr><tr><td>1</td><td>-17206424.18</td><td>3338.60</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>-1317091.22</td><td>-1369.60</td><td>0</td><td>0</td><td>2</td><td>-2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>3</td><td>-227641.81</td><td>279.60</td><td>0</td><td>0</td><td>2</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>4</td><td>207455.50</td><td>-69.80</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>5</td><td>147587.77</td><td>1181.70</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>i</td><td>A</td><td>A</td><td>l</td><td>l</td><td>F</td><td>D</td><td></td><td>Ω LMe</td><td>Lve</td><td>LE</td><td>LMa</td><td>Lj</td><td>Lsa</td><td>Lu</td><td>LNe</td><td>PA</td></tr><tr><td>1321</td><td>- 17418.82</td><td>2.89</td><td>0</td><td></td><td></td><td></td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td><td></td><td>0</td><td>0</td><td>0</td></tr><tr><td>1322</td><td>-363.71</td><td>-1.50</td><td>0</td><td>0 1</td><td>0 0</td><td>0 0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0 0</td><td>0 0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1323</td><td>-163.84</td><td>1.20</td><td>0</td><td>0</td><td>2</td><td>-2</td><td>2</td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td>0</td><td></td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td><td>0</td><td>0</td><td></td><td>0</td><td></td></tr></table>

Table 5.3b: Extract from Table 5.3b (nutation in obliquity) (available at $< { } ^ { 2 } >$ ) providing the largest components for the “in-phase” and “out-of-phase” terms of the “IAU 2000AR06” nutation. Units are $\mu$ as and $\mu$ as/century for the coefficients and their time variations, respectively. The expressions for the Delaunay arguments appearing in columns 1 to 5 are given by Eq. (5.43); those for the additional fundamental arguments of the planetary nutations appearing in columns 6 to 14 (bottom part) are given by Eq. (5.44). (Because the largest terms are all luni-solar, columns 9-17 contain only zeros in the extract shown.)   

<table><tr><td>i</td><td>B</td><td>B</td><td>l</td><td>l</td><td>F</td><td>D</td><td></td><td>Ω LMe Lve Le LMa Lj LSa</td><td></td><td></td><td></td><td></td><td></td><td>LU</td><td>LNe</td><td>pA</td></tr><tr><td>1</td><td>1537.70</td><td>9205233.10</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>-458.70</td><td>573033.60</td><td>0</td><td>0</td><td>2</td><td>一 -2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>3</td><td>137.40</td><td>97846.10</td><td>0</td><td>0</td><td>2</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>4</td><td>-29.10</td><td>-89749.20</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>5</td><td>-17.40</td><td>22438.60</td><td>0</td><td>1</td><td>2</td><td>-2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>i</td><td>B</td><td>B&quot;</td><td>1</td><td>1</td><td>F</td><td>D</td><td>Ω</td><td>LMe</td><td>Lve</td><td>LE</td><td>LMa</td><td>LJ</td><td>Lsa</td><td>LU</td><td>LNe</td><td>PA</td></tr><tr><td>1038</td><td>0.20</td><td>883.03</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1039</td><td>-0.30</td><td>-303.09</td><td>0</td><td>0</td><td>2</td><td>-2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1040</td><td>0.00</td><td>-67.76</td><td>0</td><td>1</td><td>2</td><td>-2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

# 5.6.2 Description of the IAU 2006 precession

The IAU 2006 precession (Capitaine et al., 2003c) provides improved polynomial expressions up to the 5th degree in time $t$ , both for the precession of the ecliptic and the precession of the equator, the latter being consistent with dynamical theory while matching the IAU 2000A precession rate for continuity reasons.

While the precession part of the IAU 2000A model consists only of corrections $\delta \psi _ { A } = ( - 0 . 2 9 9 6 5 \pm 0 . 0 0 0 4 0 ) ^ { \prime \prime } / \mathrm { c e n t } \mathrm { \Omega }$ ry, $\delta \omega _ { A } = ( - 0 . 0 2 5 2 4 \pm 0 . 0 0 0 1 0 ) ^ { \prime \prime } .$ /century) to the precession rates of the IAU 1976 precession, the IAU 2006 precession of the equator was derived from the dynamical equations expressing the motion of the mean pole about the ecliptic pole, with $\epsilon _ { 0 } = 8 4 3 8 1 . 4 0 6 ^ { \prime \prime }$ for the mean obliquity at J2000.0 of the ecliptic (while the IAU 2000 value was $8 4 3 8 1 . 4 4 8 ^ { \prime \prime }$ ). The IAU 2006 value for the Earth’s dynamical flattening is quite consistent with the IAU 2000 value; the IAU 2006 precession includes the Earth’s $J _ { 2 }$ rate effect (i.e. ${ \dot { J } } _ { 2 } ~ =$ $- 3 \times 1 0 ^ { - 9 }$ /century), mostly due to the post-glacial rebound, which was not taken into account in IAU 2000. The other contributions to the IAU 2006 precession rates are from Williams (1994) and MHB2000, and the geodesic precession is from Brumberg (1991). These also include corrections for the perturbing effects in the observed quantities.

# 5.6.3 IAU 2006 adjustments to the IAU 2000A nutation

The difference between IAU 2006 and IAU 2000 lies essentially in the precession part, though very small changes are needed in a few of the IAU 2000A nutation amplitudes in order to ensure compatibility with the IAU 2006 values for 0 and the $J _ { 2 }$ rate.

• Introducing the IAU 2006 $J _ { 2 }$ rate value gives rise to additional Poisson terms in nutation, the coefficients of which are proportional to $\dot { J } _ { 2 } / J _ { 2 }$ (i.e. $- 2 . 7 7 7 4 \times$ $1 0 ^ { - 6 }$ /century). The largest changes (cf. (5.19) for the corresponding changes in the $X , Y$ series) in $\mu { \mathrm { a s } }$ are (Capitaine and Wallace, 2006):

$$
\begin{array} { r l } { d \psi _ { J 2 d } = } & { { } + 4 7 . 8 t \sin \Omega + 3 . 7 t \sin 2 ( F - D + \Omega ) + 0 . 6 t \sin 2 ( F + \Omega ) - 0 . 6 t \sin 2 \Omega , } \\ { d \varepsilon _ { J 2 d } = } & { { } - 2 5 . 6 t \cos \Omega - 1 . 6 t \cos 2 ( F - D + \Omega ) . } \end{array}
$$

• The effect of the adjustment to the IAU 2006 value for $\epsilon _ { \mathrm { 0 } }$ results from the fact that the IAU 2006 obliquity is different from the IAU 1980 obliquity that was used when estimating the IAU 2000A nutation amplitudes. To compensate for this change, it is necessary to multiply the amplitudes of the nutation in longitude by $\sin \epsilon _ { \mathrm { I A U 2 0 0 0 } } / \sin \epsilon _ { \mathrm { I A U 2 0 0 6 } } = 1 . 0 0 0 0 0 4 7 0$ . (No such adjustment is needed in the case of $X , Y$ .)

The largest terms in the correction applied to the IAU 2000A nutation in longitude for this effect are, in µas:

$$
\begin{array} { r l } { d _ { \epsilon } \psi = } & { { } - 8 . 1 \ \sin \Omega - 0 . 6 \ \sin 2 ( F - D + \Omega ) . } \end{array}
$$

Whenever these small adjustments are included, the notation “IAU 2000AR06” can be used to indicate that the nutation has been revised for use with the IAU 2006 precession. The adjustments are taken into account in the SOFA implementation of the IAU 2006/2000A precession-nutation (Section 5.9). The difference between the IAU $2 0 0 0 \mathrm { A _ { R 0 6 } }$ and IAU 2000 expressions for the nutation in longitude and obliquity is available electronically on the IERS Conventions Center website (Table 5.2f) at $< { } ^ { 2 } >$ in file tab5.2f.txt.

# 5.6.4 Precession developments compatible with the IAU 2000/2006 model

The IAU 2006 precession polynomial developments (Capitaine et al., 2003c) provide separately the developments for the basic quantities for the ecliptic and the equator that are direct solutions of the dynamical equations, and derived quantities, such as those for the GCRS coordinates of the CIP, $X , Y$ , which were given by (5.16), or for sidereal time (see Section 5.5.7). The latter can be obtained from the expression for the Earth Rotation Angle, which is independent of the precession-nutation model, and the expression for the equation of the origins (i.e. the distance between the CIO and the equinox along the CIP equator), which is directly model-dependent.

The basic expressions for the precession of the ecliptic and the equator are provided by (5.38) and (5.39), respectively, with $\epsilon _ { 0 } = 8 4 3 8 1 . 4 0 6 ^ { \prime \prime }$ :

The precession quantities $P _ { A } = \sin \pi _ { A } \sin \Pi _ { A }$ and $Q _ { A } \ = \ \sin \pi _ { A } \cos \Pi _ { A }$ are the secular parts of the developments of the quantities $P = \sin \pi \sin 1 1$ and $Q \ =$ $\sin \pi \cos \Pi$ , $\pi$ and $1 1$ being the osculating elements (i.e. the inclination and longitude of the ascending node, respectively) of the Earth-Moon barycenter orbit referred to the fixed ecliptic for J2000.0. The precession quantities $\psi _ { A }$ and $\omega _ { A }$ , defined in Section 5.4.5, are solutions of the dynamical equations expressing the motion of the mean pole about the ecliptic pole.

Derived expressions for other precession quantities are given below:

where $\chi A$ is the precession of the ecliptic along the equator and $\epsilon A$ is the mean obliquity of date; $\gamma$ , $\phi$ and $\psi$ are the angles (Williams 1994, Fukushima 2003) referred to the GCRS. $\gamma$ is the GCRS right ascension of the intersection of the ecliptic of date with the GCRS equator, $\phi$ is the obliquity of the ecliptic of date on the GCRS equator and $\psi$ is the precession angle plus bias in longitude along the ecliptic of date. The last three series are from Table 1 of Hilton et al. (2006).

Due to their theoretical bases, the original development of the precession quantities as functions of time can be considered as being expressed in TDB. However, in practice, TT is used in the above expressions in place of TDB. The largest term in the difference TDB $-$ TT being $1 . 7 { \mathrm { ~ m s ~ } } \times { \sin { l ^ { \prime } } }$ (where $l ^ { \prime }$ is the mean anomaly of the Sun), the resulting error in the precession quantity $\psi _ { A }$ is periodic, with an annual period and an amplitude of $2 . 7 ^ { \prime \prime } \times 1 0 ^ { - 9 }$ , which is significantly below the required microarcsecond accuracy. This applies to Eq. (5.38)-(5.40), as well as to the polynomial part of Eq. (5.16) (i.e. the expression for the CIP’s GCRS $X$ , $Y$ coordinates).

# 5.6.5 Summary of the different ways of implementing the IAU 2006/2000A precessionnutation

There are several ways to implement the precession-nutation model, and the precession developments to be used should be consistent with the procedure being used.

Using the CIO based paradigm, the complete procedure to transform between the ITRS and the GCRS compatible with the IAU 2006/2000A precession-nutation is based on the IAU 2000 expression (i.e. Eq. (5.15)) for the ERA and on expressions provided by (5.16) and Tables 5.2a–5.2d for the positions of the CIP and the CIO in the GCRS. These already contain the proper expressions for the new precessionnutation model and the frame biases.

Implementing the IAU 2006/2000A/B model using the equinox based transformation between the ITRS and the GCRS requires following one of the rigorous procedures mentioned in Section 5.4.5 that are supported by SOFA routines (Section 5.9). They are based upon the IAU 2000 bias, IAU 2006 precession (cf. Eq. (5.39)) and the (adjusted) IAU 2000A nutation. These transformations should be used in conjunction with the IAU 2006 expression for Greenwich Sidereal Time (cf. Eq. (5.31) and Table 5.2e).

# 5.7 The fundamental arguments of nutation theory

# 5.7.1 The multipliers of the fundamental arguments of nutation theory

Each of the lunisolar terms in the nutation series is characterized by a set of five integers $N _ { j }$ which determines the argument for the term as a linear combination of the five Fundamental Arguments , namely the Delaunay variables $\left( l , l ^ { \prime } , F , D , \Omega \right)$ : ARGUMENT $\begin{array} { r } { { \bf \Sigma } = { \bf \Sigma } \sum _ { j = 1 } ^ { 5 } N _ { j } F _ { j } } \end{array}$ , where the values $( N _ { 1 } , \cdots , N _ { 5 } )$ of the multipliers characterize the term. The $F _ { j }$ are functions of time, and the angular frequency of the nutation described by the term is given by

$$
\omega \equiv d \big ( \mathrm { A R G U M E N T } \big ) / d t .
$$

The frequency thus defined is positive for most terms, and negative for some. Planetary nutation terms differ from the luni-solar nutation terms only in the fact that ARGUMENT $\begin{array} { r } { = \sum _ { j = 1 } ^ { 1 4 } N _ { j } ^ { \prime } F _ { j } ^ { \prime } } \end{array}$ , $F _ { 6 } ^ { \prime }$ to $F _ { 1 3 }$ , as noted in Tables 5.2a-5.2b and 5.3b, are the mean longitudes of the planets including the Earth $( L _ { M e } , L _ { V e } , L _ { E } , L _ { M a }$ $L _ { J }$ , $L _ { S a }$ , $\boldsymbol { L } _ { \boldsymbol { U } }$ , $\ell _ { N e }$ ) and $F _ { 1 4 } ^ { \prime }$ is the general precession in longitude $p . s$ .

Over time scales involved in nutation studies, the frequency $\omega$ is effectively timeindependent, and one may write, for the $k$ th term in the nutation series,

$$
\mathrm { A R G U M E N T } = \omega _ { k } t + \beta _ { k } .
$$

Tables of IAU 2000 nutation provide, for each (ARGUMENT), the coefficients of the “in phase” and “out-of-phase” components in longitude $\Delta \psi$ and obliquity $\Delta \epsilon$ , plus their time variations in the case of the luni-solar nutations.

Different tables of nutations in longitude and obliquity do not necessarily assign the same set of multipliers $N _ { j }$ to a particular term in the nutation series. The differences in the assignments arise from the fact that the replacement $( N _ { j = 1 , 1 4 } ) \to - ( N _ { j = 1 , 1 4 } )$ accompanied by reversal of the sign of the coefficient of sin(ARGUMENT) in the series for $\Delta \psi$ and $\Delta \epsilon$ leaves these series unchanged.

In the original expressions for the fundamental arguments $F _ { 1 }$ - $F _ { 1 4 } ^ { \prime }$ of luni-solar and planetary nutations as functions of time, $t$ is measured in TDB. However, the changes in the nutation amplitudes resulting from the contributions, $\omega _ { k } ( \mathrm { T D B - T T } )$ , of the difference TDB $-$ TT (whose largest term is $1 . 7 ~ \mathrm { m s } \times \sin l ^ { \prime }$ ) to the nutation arguments $\left( \omega _ { k } t + \beta _ { k } \right)$ are responsible for a difference in the CIP location that is less than 0.01 $\mu$ as, which is significantly below the required microarcsecond accuracy. Consequently, TT can be used in practice in place of TDB in the expressions for the fundamental nutation arguments, as it is the case for the precession expressions (cf. Section 5.6.4). This also applies to the non-polynomial part of Eq. (5.16) for the GCRS CIP coordinates.

# 5.7.2 Development of the arguments of lunisolar nutation

The expressions for the fundamental arguments of nutation are given by the following developments where $t$ is measured in Julian centuries of TDB (Simon et al., 1994: Tables 3.4 (b.3) and 3.5 (b)) based on IERS 1992 constants and Williams

F1 ≡ l = Mean Anomaly of the Moon $= 1 3 4 . 9 6 3 4 0 2 5 1 ^ { \circ } + 1 7 1 7 9 1 5 9 2 3 . 2 1 7 8 ^ { \prime \prime } t + 3 1 . 8 7 9 2 ^ { \prime \prime } t ^ { 2 }$ $+ 0 . 0 5 1 6 3 5 ^ { \prime \prime } t ^ { 3 } - 0 . 0 0 0 2 4 4 7 0 ^ { \prime \prime } t ^ { 4 } .$ ,   
F2 ≡ l0 = Mean Anomaly of the Sun = 357.52910918◦ + 129596581.048100t − 0.553200t2 $+ 0 . 0 0 0 1 3 6 ^ { \prime \prime } t ^ { 3 } - 0 . 0 0 0 0 1 1 4 9 ^ { \prime \prime } t ^ { 4 } .$   
F3 ≡ F = L − Ω = 93.27209062◦ + 1739527262.847800t − 12.751200t2 (5 −0.00103700t3 + 0.0000041700t4,   
F4 ≡ D = Mean Elongation of the Moon from the Sun $= 2 9 7 . 8 5 0 1 9 5 4 7 ^ { \circ } + 1 6 0 2 9 6 1 6 0 1 . 2 0 9 0 ^ { \prime \prime } t - 6 . 3 7 0 6 ^ { \prime \prime } t ^ { 2 }$ $+ 0 . 0 0 6 5 9 3 ^ { \prime \prime } t ^ { 3 } - 0 . 0 0 0 0 3 1 6 9 ^ { \prime \prime } t ^ { 4 } ,$   
F5 ≡ Ω = Mean Longitude of the Ascending Node of the Moon $= 1 2 5 . 0 4 4 5 5 5 0 1 ^ { \circ } - 6 9 6 2 8 9 0 . 5 4 3 1 ^ { \prime \prime } t + 7 . 4 7 2 2 ^ { \prime \prime } t ^ { 2 }$ $+ 0 . 0 0 7 7 0 2 ^ { \prime \prime } t ^ { 3 } - 0 . 0 0 0 0 5 9 3 9 ^ { \prime \prime } t ^ { 4 }$

where $L$ is the Mean Longitude of the Moon.

Note that the SOFA implementation of the IAU 2000A nutation takes the MHB2000 code (T. Herring 2002) as its definition of the IAU 2000A model. As part of this strict compliance, SOFA uses the original MHB2000 expressions for the Delaunay variables ${ \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } l ^ { \prime }$ and $D$ , that differ from Eq. (5.43) in that the fixed term is rounded to five digits (i.e. 1287104.7930500 instead of $1 2 8 7 1 0 4 . 7 9 3 0 4 8 ^ { \prime \prime }$ for the Eq. (5.43) value in the $\mathbf { \xi } _ { l }$ expression converted into arcseconds and $1 0 7 2 2 6 0 . 7 0 3 6 9 ^ { \prime \prime }$ instead of $1 0 7 2 2 6 0 . 7 0 3 6 9 2 ^ { \prime \prime }$ for the Eq. (5.43) value in the $\it { l }$ expression converted into arcseconds), respectively. The CIP location is insensitive to this difference of 2 µas in the nutation arguments at a level better than $1 0 ^ { - 9 }$ arcsec accuracy.

It should also be noted that the SOFA equinox based implementation of the IAU 2000A nutation follows the MHB2000 Fortran code in neglecting time variations of the out of phase components, i.e. the $A _ { i } ^ { \prime \prime \prime }$ and $B _ { i } ^ { \prime \prime \prime }$ columns of Table 5.3a (see Section 5.6.1). The difference in the CIP location is just over 2 $\mu$ as after one century.

# 5.7.3 Development of the arguments for the planetary nutation

The mean longitudes of the planets used in the arguments for the planetary nutations are essentially those provided by Souchay et al. (1999), based on theories and constants of VSOP82 (Bretagnon, 1982) and ELP 2000 (Chapront-Touz´e and Chapront, 1983) and developments of Simon et al. (1994: Tables 5.8.1-5.8.8). Their developments are given in Eq. (5.44) in radians with $t$ in Julian centuries.

Another part of the strict compliance of SOFA with the MHB2000 code is that simplified expressions are used for the Delaunay variables $F _ { 1 } ^ { \prime }$ - $F _ { 5 } ^ { 1 }$ in the planetary nutation case. The maximum difference this makes to the CIP location is 0.013 $\mu$ as after one century. The SOFA implementation also uses the original MHB2000 expression for the longitude of Neptune (slightly different from that in Eq. (5.44), i.e. $L _ { N e } \ = \ 5 . 3 2 1 1 5 9 0 0 0 + \ 3 . 8 1 2 7 7 7 4 0 0 \times t$ instead of $L _ { N e } ~ = ~ 5 . 3 1 1 8 8 6 2 8 7 ~ + ~ 3 . 8 1 3 3 0 3 5 6 3 8 ~ \times ~ t )$ . The maximum difference in the CIP is less than 0.01 $\mu$ as after one century.

# 5.8 Prograde and retrograde nutation amplitudes

The quantities $\Delta { \psi } ( t ) \sin \epsilon _ { 0 }$ and $\Delta \epsilon ( t )$ may be viewed as the components of a moving two-dimensional vector in the mean equatorial system, with the positive $X$ and $Y$ axes pointing along the directions of increasing $\Delta \psi$ and $\Delta \epsilon$ , respectively. The purely periodic parts of $\Delta { \psi } ( t ) \sin \epsilon _ { 0 }$ and $\Delta \epsilon ( t )$ for a term of frequency $\omega _ { k }$ are made up of in-phase and out-of-phase parts

$$
\begin{array} { r l } & { ( \Delta \psi ^ { i p } ( t ) \sin \epsilon _ { 0 } , \ \Delta \epsilon ^ { i p } ( t ) ) = ( \Delta \psi _ { k } ^ { i p } \sin \epsilon _ { 0 } \sin ( \omega _ { k } t + \beta _ { k } ) , \ \Delta \epsilon _ { k } ^ { i p } \cos ( \omega _ { k } t + \beta _ { k } ) ) , } \\ & { } \\ & { ( \Delta \psi ^ { o p } ( t ) \sin \epsilon _ { 0 } , \ \Delta \epsilon ^ { o p } ( t ) ) = ( \Delta \psi _ { k } ^ { o p } \sin \epsilon _ { 0 } \cos ( \omega _ { k } t + \beta _ { k } ) , \ \Delta \epsilon _ { k } ^ { o p } \sin ( \omega _ { k } t + \beta _ { k } ) ) , } \end{array}
$$

respectively. Each of these vectors may be decomposed into two uniformly rotating vectors, one constituting a prograde circular nutation (rotating in the same sense as from the positive $X$ axis towards the positive $Y$ axis) and the other a retrograde one rotating in the opposite sense. The decomposition is facilitated by factoring out the sign $q _ { k }$ of $\omega _ { k }$ from the argument, $q _ { k }$ being such that

$$
q _ { k } \omega _ { k } \equiv | \omega _ { k } |
$$

and writing

$$
\omega _ { k } t + \beta _ { k } = q _ { k } ( | \omega _ { k } | t + q _ { k } \beta _ { k } ) \equiv q _ { k } \chi _ { k } ,
$$

with $\chi _ { k }$ increasing linearly with time. The pair of vectors above then becomes

$$
\begin{array} { r l } & { ( \Delta { \psi } ^ { i p } ( t ) \sin \epsilon _ { 0 } , \ \Delta \epsilon ^ { i p } ( t ) ) = ( q _ { k } \Delta \psi _ { k } ^ { i p } \sin \epsilon _ { 0 } \sin \chi _ { k } , \ \Delta \epsilon _ { k } ^ { i p } \cos \chi _ { k } ) , } \\ & { } \\ & { ( \Delta \psi ^ { o p } ( t ) \sin \epsilon _ { 0 } , \ \Delta \epsilon ^ { o p } ( t ) ) = ( \Delta \psi _ { k } ^ { o p } \sin \epsilon _ { 0 } \cos \chi _ { k } , \ q _ { k } \Delta \epsilon _ { k } ^ { o p } \sin \chi _ { k } ) . } \end{array}
$$

Because $\chi _ { k }$ increases linearly with time, the mutually orthogonal unit vectors $( \sin \chi _ { k } , - \cos \chi _ { k } )$ and $( \cos \chi _ { k } , \sin \chi _ { k } )$ rotate in a prograde sense and the vectors obtained from these by the replacement $\chi _ { k }  - \chi _ { k }$ , namely $( - \sin \chi _ { k } , - \cos \chi _ { k } )$ and $( \cos \chi _ { k } , - \sin \chi _ { k } )$ are in retrograde rotation. On resolving the in-phase and out-of-phase vectors in terms of these, one obtains

$$
\begin{array} { r l } & { ( \Delta \psi ^ { i p } ( t ) \sin \epsilon _ { 0 } , \ \Delta \epsilon ^ { i p } ( t ) ) = A _ { k } ^ { p r o \ i p } ( \sin \chi _ { k } , \ - \cos \chi _ { k } ) + A _ { k } ^ { r e t \ i p } ( - \sin \chi _ { k } , \ - \cos \chi _ { k } ) , } \\ & { } \\ & { ( \Delta \psi ^ { o p } ( t ) \sin \epsilon _ { 0 } , \ \Delta \epsilon ^ { o p } ( t ) ) = A _ { k } ^ { p r o \ o p } ( \cos \chi _ { k } , \ \sin \chi _ { k } ) + A _ { k } ^ { r e t \ o p } ( \cos \chi _ { k } , \ - \sin \chi _ { k } ) , } \end{array}
$$

where

$$
\begin{array} { l c l } { { A _ { k } ^ { p r o \ i p } } } & { { = } } & { { \frac { 1 } { 2 } \ ( q _ { k } \Delta \psi _ { k } ^ { i p } \sin \epsilon _ { 0 } - \Delta \epsilon _ { k } ^ { i p } ) , } } \\ { { A _ { k } ^ { r e t \ i p } } } & { { = } } & { { - \frac { 1 } { 2 } \ ( q _ { k } \Delta \psi _ { k } ^ { i p } \sin \epsilon _ { 0 } + \Delta \epsilon _ { k } ^ { i p } ) , } } \\ { { A _ { k } ^ { p r o o p } } } & { { = } } & { { \frac { 1 } { 2 } \ ( \Delta \psi _ { k } ^ { o p } \sin \epsilon _ { 0 } + q _ { k } \Delta \epsilon _ { k } ^ { o p } ) , } } \\ { { A _ { k } ^ { r e t \ o p } } } & { { = } } & { { \frac { 1 } { 2 } \ ( \Delta \psi _ { k } ^ { o p } \sin \epsilon _ { 0 } - q _ { k } \Delta \epsilon _ { k } ^ { o p } ) . } } \end{array}
$$

The expressions providing the corresponding nutation in longitude and in obliquity from circular terms are

$$
\begin{array} { r c l } { { \Delta \psi _ { k } ^ { i p } } } & { { = } } & { { \frac { q _ { k } } { \sin \epsilon _ { 0 } } \left( A _ { k } ^ { p r o ~ i p } - A _ { k } ^ { r e t ~ i p } \right) , } } \\ { { } } & { { } } & { { } } \\ { { \Delta \psi _ { k } ^ { o p } } } & { { = } } & { { \frac { 1 } { \sin \epsilon _ { 0 } } \left( A _ { k } ^ { p r o ~ o p } + A _ { k } ^ { r e t ~ o p } \right) , } } \\ { { } } & { { } } & { { } } \\ { { \Delta \epsilon _ { k } ^ { i p } } } & { { = } } & { { - \left( A _ { k } ^ { p r o ~ i p } + A _ { k } ^ { r e t ~ i p } \right) , } } \\ { { } } & { { } } & { { } } \\ { { \Delta \epsilon _ { k } ^ { o p } } } & { { = } } & { { q _ { k } \left( A _ { k } ^ { p r o ~ o p } - A _ { k } ^ { r e t ~ o p } \right) . } } \end{array}
$$

The contribution of the $k$ -term of the nutation to the position of the Celestial Intermediate Pole (CIP) in the mean equatorial system is thus given by the complex coordinate

$$
\Delta \psi ( t ) \sin \epsilon _ { 0 } + i \Delta \epsilon ( t ) = - i \left( A _ { k } ^ { p r o } e ^ { i \chi _ { k } } + A _ { k } ^ { r e t } e ^ { - i \chi _ { k } } \right) ,
$$

where $A _ { k } ^ { p r o }$ and $A _ { k } ^ { r e t }$ are the amplitudes of the prograde and retrograde components, respectively, and are given by

$$
A _ { k } ^ { p r o } = A _ { k } ^ { p r o ~ i p } + i A _ { k } ^ { p r o ~ o p } , ~ A _ { k } ^ { r e t } = A _ { k } ^ { r e t ~ i p } + i A _ { k } ^ { r e t ~ o p } .
$$

The decomposition into prograde and retrograde components is important for studying the role of resonance in nutation because any resonance (especially in the case of the nonrigid Earth) affects $A _ { k } ^ { p r o }$ and $A _ { k } ^ { r e t }$ unequally.

In the literature (Wahr, 1981) one finds an alternative notation, frequently followed in analytic formulations of nutation theory, that is:

$$
\Delta \epsilon ( t ) + i \Delta \psi ( t ) \sin \epsilon _ { 0 } = - i \left( A _ { k } ^ { p r o } - e ^ { - i \chi _ { k } } + A _ { k } ^ { r e t } - e ^ { i \chi _ { k } } \right) ,
$$

with

$$
A _ { k } ^ { p r o \mathrm { ~ - ~ } } = A _ { k } ^ { p r o \mathrm { ~ } i p } - i A _ { k } ^ { p r o \mathrm { ~ } o p } , \qquad A _ { k } ^ { r e t \mathrm { ~ - ~ } } = A _ { k } ^ { r e t \mathrm { ~ } i p } - i A _ { k } ^ { r e t \mathrm { ~ } o p } .
$$

Further details can be found in Defraigne et al. (1995) and Bizouard et al. (1998).

# 5.9 Algorithms for transformations between ITRS and GCRS

Software routines to implement the IAU 2006/2000A transformations are provided by the IAU Standards Of Fundamental Astronomy service.6 The routines vary in complexity from simple modules to complete transformations, allowing the application developer to trade off simplicity of use against computational efficiency and flexibility. Implementations in Fortran77 and C are available.

The SOFA software supports two equivalent ways of implementing the IAU resolutions in the transformation from ITRS to GCRS provided by expression (5.1), namely (a) the transformation based on the Celestial Intermediate Origin and the Earth Rotation Angle (i.e. the CIO based procedure described in Sections 5.4.1, 5.4.2 and 5.4.4, using parameters described in Section 5.5) and (b) the classical transformation based on the equinox and Greenwich Sidereal Time (i.e. the equinox based procedure described in Sections 5.4.1, 5.4.3 and 5.4.5, with the use of classical precession and nutation angles). The quantity that links the two systems is the “equation of the origins”, $\alpha _ { \mathrm { C I O } } - \alpha _ { \Upsilon }$ (difference between right ascensions, $\alpha _ { \mathrm { { C I O } } }$ and $\alpha \Upsilon$ , referred to the CIO and the equinox, respectively), or equivalently ERA−GST. For both transformations, the procedure is to form the various components of expression (5.1), choosing for the $Q ( t )$ and $R ( t )$ pair either the CIO based or classical forms, and then to combine these components into the complete terrestrial-to-celestial matrix.

In all cases, the polar motion matrix, $W ( t )$ in expression (5.1), is needed, using the polar coordinates $x _ { p } , y _ { p }$ . This can be accomplished by calling the SOFA routine POM00 and then transposing the result (e.g. using the support routine TR). Also required is the quantity $s ^ { \prime }$ , modeled by the routine SP00.

SOFA routines that support the IAU 2006/2000A models include the following (among others):

<table><tr><td>BP06</td><td>celestial-to-true matrix (etc.),given △ and △e</td></tr><tr><td>C2I06A</td><td>celestial-to-intermediate matrix,IAU 2006/2000A</td></tr><tr><td>C2IXYS</td><td>celestial-to-intermediate matrix,given X,Y and s</td></tr><tr><td>C2T06A</td><td>celestial-to-terrestrial matrix, IAU 2006/2000A</td></tr><tr><td>C2TCIO</td><td>CIO based celestial-to-terrestrial matrix</td></tr><tr><td>EORS</td><td>equation of the origins,given celestial-to-true matrix and s</td></tr><tr><td>ERA00</td><td>Earth Rotation Angle</td></tr><tr><td>GMST06</td><td>Greenwich Mean Sidereal Time,IAU 2006</td></tr><tr><td>GST06A</td><td>Greenwich (apparent） Sidereal Time,IAU 2Oo6/2000A</td></tr><tr><td>NUM06A</td><td>nutation matrix,IAU 2006/2000A</td></tr><tr><td>NUT06A</td><td>nutation components,IAU 20o6/2000A</td></tr><tr><td>PNM06A</td><td>celestial-to-true matrix,IAU 2006/2000A</td></tr><tr><td>POMOO</td><td>polar motion matrix</td></tr><tr><td>SP00</td><td>the quantity s&#x27;</td></tr><tr><td>XY06</td><td>X,Y from semi-analytical series,IAU 20o6/2000A</td></tr><tr><td>XYS06A</td><td>X,Y,s,IAU 2006/2000A</td></tr></table>

The matrix for the combined effects of nutation, precession and frame bias is $Q ( t )$ in expression (5.1). For the CIO based transformation, this is the intermediateto-celestial matrix, it can be obtained (as the transpose) using the SOFA routine C2IXYS, starting from the CIP position $X , Y$ and the quantity $s$ that defines the position of the CIO. The IAU 2006/2000A $X , Y , s$ are available by calling the SOFA routine XYS06A. In the case of the equinox based transformation, the counterpart to matrix $Q ( t )$ is the true-to-celestial matrix. To obtain this matrix requires the nutation components $\Delta \psi$ and $\Delta \epsilon$ ; these can be predicted using the IAU 2000A model, with adjustments to match IAU 2006 precession, by means of the SOFA routine NUT06A. Faster, but less accurate, predictions are available from the NUT00B routine, which implements the IAU 2000B truncated model. Once $\Delta \psi$ and $\Delta \epsilon$ are known, the true-to-celestial matrix can be obtained by calling the routine PN06 and taking the transpose with TR.

The intermediate component is the angle for Earth rotation that defines matrix $R ( t )$ in expression (5.1). For the CIO based transformation, the angle in question is the Earth Rotation Angle, ERA, which can be obtained by calling the SOFA routine ERA00. The counterpart in the case of the equinox based transformation is the Greenwich (apparent) Sidereal Time. This can be obtained by calling the


<!-- chunk 0002: pages 71-140 -->
SOFA routine GST06, given the celestial-to-true matrix that was obtained earlier. The three components – the precession-nutation matrix, the Earth rotation quantity and the polar motion matrix – are then assembled into the final terrestrialto-celestial matrix by means of the SOFA routine C2TCIO (CIO based) or C2TEQX (equinox based), followed by TR as required.

Two methods to generate the terrestrial-to-celestial (i.e. ITRS-to-GCRS) matrix $Q ( t ) R ( t ) W ( t )$ , given TT and UT1, are set out below. In each case it is assumed that observed small corrections to the IAU 2006/2000A model, either as $\Delta X , \Delta Y$ or as $d \Delta \psi , d \Delta \epsilon$ , are available and need to be included.

Method (1): the CIO based transformation

The CIO based transformation is a function of the CIP coordinates $X , Y$ and the quantity $s$ .

For the given TT, call the SOFA routine XY06 to obtain the IAU 2006/2000A $X , Y$ from series (see Section 5.5.4) and then the routine S06 to obtain $s$ . Any CIP corrections $\Delta X , \Delta Y$ can now be applied, and the corrected $X , Y , s$ can be used to call the routine C2IXYS, giving the GCRS-to-CIRS matrix. Next call the routine ERA00 to obtain the ERA corresponding to the current UT1, and apply it as an $R _ { 3 }$ rotation using the routine RZ, to form the CIRS-to-TIRS matrix. Given $x _ { p } , y _ { p }$ , and obtaining $s ^ { \prime }$ by calling the routine SP00, the polar motion matrix (i.e. TIRS-to-ITRS) is then produced by the routine POM00. The product of the two matrices (GCRS-to-TIRS and TIRS-to-ITRS), obtained by calling the routine RXR, is the GCRS-to-ITRS matrix, which can be inverted by calling the routine TR to give the final result.

# Method (2): the equinox based transformation

The classical transformation, based on angles and using sidereal time is also available.

Given TT, the IAU 2006/2000A nutation components $\Delta \psi , \Delta \epsilon$ are obtained by calling the SOFA routine NUT06A. Any corrections $d \Delta \psi , d \Delta \epsilon$ can now be applied. Next, the GCRS-to-true matrix is obtained using the routine PN06 (which employs the 4-rotation Fukushima-Williams method described in Section 5.3.4, final paragraph). The classical GCRS-to-true matrix can also be generated by combining separate frame bias, precession and nutation matrices. The SOFA routine BI00 can be called to obtain the frame bias components, the routine P06E to obtain various precession angles, and the routine NUM06A to generate the nutation matrix. The product N $\times$ P $\times$ B is formed by using the routine RXR. Next call the routine GST06 to obtain the GST corresponding to the current UT1, and apply it as an $R _ { 3 }$ rotation using the routine RZ to form the true matrix-to-TIRS. Given $x _ { p } , y _ { p }$ and obtaining $s ^ { \prime }$ with the routine SP00, the polar motion matrix (i.e. TIRS-to-ITRS) is then obtained using the routine POM00. The product of the two matrices (GCRS-to-TIRS and TIRS-to-ITRS), obtained by calling the routine RXR, is the GCRS-to-ITRS matrix, which can be inverted by calling the routine TR to give the final result.

Methods (1) and (2) agree to microarcsecond precision.

Both methods can be abridged to trade off speed and accuracy (see Capitaine and Wallace, 2008). The abridged nutation model IAU 2000B (see Section 5.5.1) can be substituted in Method (2) by calling NUT00B instead of NUT06A. Depending on the application, the best compromise between speed and accuracy may be to evaluate the full series to obtain sample values for interpolation.

# 5.10 Notes on the new procedure to transform from ICRS to ITRS

The transformation between the GCRS and the ITRS, which is provided in detail in this chapter for use in the IERS Conventions, is also part of the more general transformation for computing directions of celestial objects in intermediate systems or terrestrial systems.

The procedure to be followed in transforming from the celestial (ICRS) to the terrestrial (ITRS) systems has been clarified to be consistent with the improving observational accuracy. See Figure 5.1 in the IAU NFA Working Group documents (Capitaine et al., 2007) for a diagram of the CIO based and equinox based procedures to be followed.

The purpose of this chart is to show the ICRS-to-BCRS-to-GCRS-to-ITRS transformation in general relativity (IAU 2000 Resolution B1.3) and the parallel CIO and equinox based processes (IAU 2000 Resolution B1.8).

As before, we make use of celestial and terrestrial intermediate reference systems in transforming to a terrestrial reference system (See also Seidelmann and Kovalevsky (2002).)

The Celestial Intermediate Pole (CIP) that is realized by the IAU 2006/2000A precession-nutation model defines its equator and the Conventional Intermediate Origin replaces the equinox.

The position in this reference system is called the intermediate right ascension and declination and is analogous to the previous designation of “apparent right ascension and declination.”

![](../chunks/IERS Conventions (2010), IERS Technical Note No.36_part_0002_pages_0071-0140/auto/images/2970f0d14458760b8342a5ec1999551db12ff573f23d5937e6f19763c5812a3e.jpg)  
Figure 5.1: Process to transform from celestial to terrestrial reference systems (Chart from the IAU Working Group on Nomenclature for Fundamental Astronomy (2006)). The chart summarizes the system, and the elements that are associated with that system, i.e. the name for the positions (place), the processes/corrections, the origin to which the coordinates are referred, and the time scale to use. In particular the blue type in the box in the “Process” column is the operation/correction to be applied, and the purple type indicates the quantities required for that process. CIO and equinox based processes are indicated using grey and yellow shading, respectively.

Aoki, S., Guinot, B., Kaplan, G. H., Kinoshita, H., McCarthy, D. D., and Seidelmann, P. K., 1982, “The New Definition of Universal Time,” Astron. Astrophys., 105(2), pp. 359–361.   
Aoki, S. and Kinoshita, H., 1983, “Note on the relation between the equinox and Guinot’s non-rotating origin,” Celest. Mech., 29(4), pp. 335–360, doi:10.1007/BF01228528.   
Bizouard, Ch., Brzezi´nski, A., and Petrov, S., 1998, “Diurnal atmospheric forcing and temporal variations of the nutation amplitudes,” J. Geod., 72(10), pp. 561–577, doi:10.1007/s001900050195.   
Bizouard, Ch., Folgueira, M., and Souchay, J., 2000, “Comparison of the short period rigid Earth nutation series,” in Proc. IAU Colloquium 178, Publications of the Astron. Soc. Pac. Conf. Ser., Vol. 208, Dick, S., McCarthy, D., and Luzum, B. (eds.), pp. 613–617.   
Bizouard, Ch., Folgueira, M., and Souchay, J., 2001, “Short periodic nutations: comparison between series and influence on polar motion,” in Proc. of the Journ´ees 2000 - Syst\`emes de R´ef´erence Spatio-Temporels, Capitaine, N. (ed.), Observatoire de Paris, pp. 260–265.   
Bretagnon, P., 1982, “Th´eorie du mouvement de l’ensemble des plan\`etes. solution VSOP82,” Astron. Astrophys., 114(2), pp. 278–288.   
Bretagnon, P., Rocher, P., and Simon, J.-L., 1997, “Theory of the rotation of the rigid Earth,” Astron. Astrophys., 319(1), pp. 305–317.   
Brumberg, V. A., 1991, Essential Relativistic Celestial Mechanics, Adam Hilger Pub.   
Brzezi´nski, A., 2001, “Diurnal and sub-diurnal terms of nutation: a simple theoretical model for a nonrigid Earth,” in Proc. of the Journ´ees 2000 - Syst\`emes de R´ef´erence Spatio-temporels, N. Capitaine (ed.), Observatoire de Paris, pp. 243–251.   
Brzezi´nski, A., July 2002, Circular 2, IAU Commission 19 WG “Precessionnutation”.   
Brzezi´nski, A. and Capitaine N., 2003, “Lunisolar perturbations in Earth rotation due to the triaxial figure of the Earth: geophysical aspects,” in Proc. of the Journ´ees 2001 - Syst\`emes de R´ef´erence Spatio-temporels, N. Capitaine (ed.), Observatoire de Paris, pp. 51–58.   
Brzezi´nski, A. and Mathews, P. M., 2003, “Recent advances in modeling the lunisolar perturbation in polar motion corresponding to high frequency nutation: report on the discussion of the IAU Commission 19 WG on Nutation,” in Proc. of the Journ´ees 2002 - Syst\`emes de R´ef´erence Spatio-temporels, N. Capitaine and M. Stavinschi (eds.), Observatoire de Paris, pp. 101–108.   
Brzezi´nski, A. and Capitaine, N., 2010, “Semi-diurnal signal in UT1 due to the influence of tidal gravitation on the triaxial structure of the Earth,” in Highlights of Astronomy, 15, Ian F. Corbett (ed.).   
Buffett, B. A., Mathews, P. M., and Herring, T., 2002, “Modeling of nutation and precession: Effects of electromagnetic coupling,” J. Geophys. Res., 107(B4), doi: 10.1029/2000JB000056.   
Capitaine, N., 1990, “The celestial pole coordinates,” Celest. Mech. Dyn. Astr., 48(2), pp. 127–143, doi:10.1007/BF00049510   
Capitaine, N., 2000, “Definition of the Celestial Ephemeris Pole and the Celestial Ephemeris Origin,” in Towards Models and Constants for Sub-Microarcsecond Astrometry, Johnston, K. J., McCarthy, D. D., Luzum, B. J., and Kaplan, G. H. (eds.), U.S. Naval Observatory, pp. 153–163.   
Capitaine, N., Guinot, B., and Souchay, J., 1986, “A Non-rotating Origin on the Instantaneous Equator: Definition, Properties and Use,” Celest. Mech., 39(3), pp. 283–307, doi:10.1007/BF01234311.   
Capitaine, N. and Gontier, A.-M., 1993, “Accurate procedure for deriving UT1 at a submilliarcsecond accuracy from Greenwich Sidereal Time or from the stellar angle,” Astron. Astrophys., 275, pp. 645–650.   
Capitaine, N., Guinot, B., and McCarthy, D. D., 2000, “Definition of the Celestial Ephemeris origin and of UT1 in the International Celestial Reference Frame,” Astron. Astrophys., 355(1), pp. 398–405.   
Capitaine, N., Gambis, D., McCarthy, D. D., Petit, G., Ray, J., Richter, B., Rothacher, M., Standish, M., and Vondr´ak, J., (eds.), 2002, IERS Technical Note, 29, Proceedings of the IERS Workshop on the Implementation of the New IAU Resolutions, 2002, Verlag des Bundesamts f¨ur Kartographie und Geod¨asie, Frankfurt am Main, available at http://www.iers.org/iers/publications/tn/tn29/   
Capitaine, N., Chapront, J., Lambert, S., and Wallace, P., 2003a, “Expressions for the Celestial Intermediate Pole and Celestial Ephemeris Origin consistent with the IAU 2000A precession-nutation model,” Astron. Astrophys., 400(3), pp. 1145–1154, doi:10.1051/0004-6361:20030077   
Capitaine, N., Wallace, P. T., and McCarthy, D. D., 2003b, “Expressions to implement the IAU 2000 definition of UT1,” Astron. Astrophys., 406(3), pp. 1135-1149, doi:10.1051/0004-6361:20030817   
Capitaine, N., Wallace, P. T., and Chapront, J., 2003c, “Expressions for IAU 2000 precession quantities,” Astron. Astrophys., 412(2), pp. 567–586, doi:10.1051/0004-6361:20031539   
Capitaine, N. and Wallace, P. T., 2006, “High precision methods for locating the celestial intermediate pole and origin,” Astron. Astrophys., 450, pp. 855– 872, doi:10.1051/0004-6361:20054550.   
Capitaine, N., Andrei, A., Calabretta, M., Dehant, V., Fukushima, T., Guinot, B., Hohenkerk, C., Kaplan, G., Klioner, S., Kovalevsky, J., Kumkova, I., Ma, C., McCarthy, D., Seidelmann, K., and Wallace, P., 2007, “Proposed terminology in fundamental astronomy based on IAU 2000 resolutions,” in Transactions of the IAU XXVIB, van der Hucht, K.A. (ed), 14, pp. 474–475, doi:10.1017/S1743921307011490.   
Capitaine, N. and Wallace, P. T., 2008, “Concise CIO based precession-nutation formulations,” Astron. Astrophys., 478(1), pp. 277–284. doi:10.1051/0004- 6361:20078811.   
Capitaine, N., Mathews, P. M., Dehant, V., Wallace, P. T. and Lambert, S. B., 2009, “On the IAU 2000/2006 precession-nutation and comparison with other models and VLBI observations,” Celest. Mech. Dyn. Astr., 103, 2, pp. 179–190, doi:10.1007/s10569-008-9179-9.   
Cartwright, D. E. and Tayler, R. J., 1971, “New Computations of the Tide-Generating Potential,” Geophys. J. Roy. astr. Soc., 23(1), pp. 45–74, doi:10.1111/j.1365-246X.1971.tb01803.x.   
Chao, B. F., Dong, D. N., Liu, H. S., and Herring, T. A., 1991, “Libration in the Earth’s rotation,” Geophys. Res. Letters, 18, No. 11, 2007–2010, doi:10.1029/91GL02491.   
Chao, B. F., Ray, R. D., Gipson, J. M., Egbert, G. D., and Ma, C., 1996, “Diurnal/semi-diurnal polar motion excited by oceanic tidal angular momentum,” J. Geophys. Res., 101(B9), 20151–20163, doi:10.1029/96JB01649.   
Chapront-Touz´e, M. and Chapront, J., 1983, “The lunar ephemeris ELP 2000,” Astron. Astrophys., 124(1), pp. 50–62.   
Chapront, J., Chapront-Touz´e, M., and Francou, G., 2002, “A new determination of lunar orbital parameters, precession constant and tidal acceleration from LLR measurements,” Astron. Astrophys., 387(2), pp. 700–709, doi:10.1051/0004-6361:20020420.   
Defraigne, P., Dehant, V., and Pˆaquet, P., 1995, “Link between the retrogradeprograde nutations and nutations in obliquity and longitude,” Celest. Mech. Dyn. Astr., 62(4), pp. 363–376, doi:10.1007/BF00692286.

Escapa, A., Getino, J., and Ferr´andiz, J. M., 2002, “Indirect effect of the triaxiality in the Hamiltonian theory for the rigid Earth nutations,” Astron. Astrophys., 389(3), pp. 1047–1054, doi: 10.1051/0004-6361:20020734.

Escapa, A., Getino, J., and Ferr´andiz, J. M., 2003, “Influence of the triaxiality of the non-rigid Earth on the J2 forced nutations,” in Proc. of the Journ´ees 2001 - Syst\`emes de R´ef´erence Spatio-temporels, N. Capitaine (ed.), Observatoire de Paris, pp. 275–281.

Folgueira, M., Souchay, J., and Kinoshita, H., 1998a, “Effects on the nutation of the non-zonal harmonics of third degree,” Celest. Mech. Dyn. Astr., 69(4), pp. 373–402, doi:10.1023/A:1008298122976.

Folgueira, M., Souchay, J., and Kinoshita, H., 1998b, “Effects on the nutation of C4m and S4m harmonics,” Celest. Mech. Dyn. Astr., 70(3), pp. 147–157, doi:10.1023/A:1008383423586.

Folgueira, M., Bizouard, C., and Souchay, J., 2001, “Diurnal and sub-diurnal luni-solar nutations: comparisons and effects,” Celest. Mech. Dyn. Astr., 81(3), pp. 191–217, doi:10.1023/A:1013290523560.

Fukushima, T., 1991, “Geodesic Nutation,” Astron. Astrophys., 244(1), pp. L11– L12.

Fukushima, T., 2003, “A new precession formula,” Astron. J., 126, pp. 494–534.

Getino, J., Ferr´andiz, J. M., and Escapa, A., 2001, “Hamiltonian theory for the non-rigid Earth: semi-diurnal terms,” Astron. Astrophys., 370(1), pp. 330– 341.

Guinot, B., 1979, “Basic Problems in the Kinematics of the Rotation of the Earth,” in Time and the Earth’s Rotation, McCarthy, D. D. and Pilkington, J. D. (eds.), D. Reidel Publishing Company, pp. 7–18.

Herring, T. A., Mathews, P. M., and Buffett, B. A., 2002, “Modeling of nutationprecession: Very long baseline interferometry results,” J. Geophys. Res., 107(B4), doi: 10.1029/2001JB000165.

Hilton, J.L., Capitaine, N., Chapront, J., Ferrandiz, J.M., Fienga, A., Fukushima, T., Getino, J., Mathews, P., Simon, J.-L., Soffel, M., Vondrak, J., Wallace, P., and Williams, J., 2006, “Report of the International Astronomical Union Division I Working Group on Precession and the Ecliptic”, Celest. Mech. Dyn. Astron., 94(3), pp. 351–367, doi:10.1007/s10569-006-0001-2.

Kinoshita, H., 1977, “Theory of the rotation of the rigid Earth,” Celest. Mech. 15(3), 277–326, doi:10.1007/BF01228425.

Kinoshita, H. and Souchay, J., 1990, “The theory of the nutation for the rigid Earth model at the second order,” Celest. Mech. Dyn. Astron., 48(3), pp. 187–265, doi:10.1007/BF02524332.

Lambert, S., 2007, “Empirical modeling of the retrograde Free Core Nutation,” available at ftp://hpiers.obspm.fr/eop-pc/models/fcn/notice.pdf.

Lambert, S. and Bizouard, C., 2002, “Positioning the Terrestrial Ephemeris Origin in the International Terrestrial Reference Frame,” Astron. Astrophys., 394(1), pp. 317–321, doi:10.1051/0004-6361:20021139.

Lieske, J. H., Lederle, T., Fricke, W., and Morando, B., 1977, “Expressions for the Precession Quantities Based upon the IAU (1976) System of Astronomical Constants,” Astron. Astrophys., 58(1-2), pp. 1–16.   
Ma, C., Arias, E. F., Eubanks, T. M., Fey, A. L., Gontier, A.-M., Jacobs, C. S., Sovers, O. J., Archinal, B. A., and Charlot, P., 1998, “The International Celestial Reference Frame as realized by Very Long Baseline Interferometry,” Astron. J., 116(1), pp. 516–546, doi:10.1086/300408.   
Mathews, P. M., Herring, T. A., and Buffett B. A., 2002, “Modeling of nutation and precession: New nutation series for nonrigid Earth, and insights into the Earth’s Interior,” J. Geophys. Res., 107(B4), doi: 10.1029/2001JB000390.   
Mathews, P. M. and Bretagnon, P., 2003, “High frequency nutation,” in Proc. of the Journ´ees 2001 - Syst\`emes de R´ef´erence Spatio-temporels, N. Capitaine (ed.), Observatoire de Paris, pp. 28–33.   
McCarthy, D. D. (ed.), 1996, “IERS Conventions”, IERS Technical Note, 21, Observatoire de Paris, Paris, available at http://www.iers.org/TN21   
McCarthy, D. D. and Luzum, B. J., 2003, “An Abridged Model of the Precession-Nutation of the Celestial Pole,” Celest. Mech. Dyn. Astr., 85(1), pp. 37–49, doi:10.1023/A:1021762727016.   
Ray, R. D., Steinberg, D. J., Chao, B. F., and Cartwright, D. E., 1994, “Diurnal and semi-diurnal variations in the Earth’s rotation rate induced by oceanic tides”, Science, 264(5160), 830–832, doi:10.1126/science.264.5160.830.   
Roosbeek, F., 1999,“Diurnal and sub-diurnal terms in RDAN97 series,” Celest. Mech. Dyn. Astr., 74(4), pp. 243–252, doi:10.1023/A:1008312424283.   
Seidelmann, P. K., 1982, “1980 IAU Theory of Nutation: The Final Report of the IAU Working Group on Nutation,” Celest. Mech., 27(1), pp. 79–106, doi:10.1007/BF01228952.   
Seidelmann, P. K. and Kovalevksy, J., 2002, “Application of the new concepts and definitions (ICRS, CIP and CEO) in fundamental astronomy,” Astron. Astrophys., 392(1), pp. 341–351, doi:10.1051/0004-6361:20020931.   
Simon, J.-L., Bretagnon, P., Chapront, J., Chapront-Touz´e, M., Francou, G., and Laskar, J., 1994, “Numerical Expressions for Precession Formulae and Mean Elements for the Moon and the Planets,” Astron. Astrophys., 282(2), pp. 663–683.   
Souchay, J. and Kinoshita, H., 1997, “Corrections and new developments in rigid-Earth nutation theory. II. Influence of second-order geopotential and direct planetary effect,” Astron. Astrophys., 318, pp. 639–652.   
Souchay, J., Loysel, B., Kinoshita, H., and Folgueira, M., 1999, “Corrections and new developments in rigid Earth nutation theory: III. Final tables REN-2000 including crossed-nutation and spin-orbit coupling effects,” Astron. Astrophys. Suppl. Ser., 135(1), pp. 111–131, doi:10.1051/aas:1999446.   
Standish, E. M., 1981, “Two differing definitions of the dynamical equinox and the mean obliquity,” Astron. Astrophys., 101, pp. L17–L18.   
Tapley, B. D., Watkins, M. M., Ries, J. C., Davis, G. W., Eanes, R. J., Poole, S. R., Rim, H. J., Schutz, B. E., Shum, C. K., Nerem, R. S., Lerch, F. J., Marshall, J. A., Klosko, S. M., Pavlis, N. K., and Williamson, R. G., 1996, “The Joint Gravity Model 3,” J. Geophys. Res., 101(B12), pp. 28029– 28049, doi:10.1029/96JB01645.   
Tisserand, F., 1891, Trait´e de M´ecanique C´eleste, Tome II, Paris, Gauthier-Villars, 1891.   
Wahr, J. M., 1981, “The forced nutations of an elliptical, rotating, elastic and oceanless Earth,” Geophys. J. Roy. astr. Soc., 64(3), pp. 705–727, doi: 10.1111/j.1365-246X.1981.tb02691.x.   
Wallace, P. T., 1998, “SOFA: Standards of Fundamental Astronomy”, Highlights of Astronomy, Vol. 11A, J. Andersen (ed.), Kluwer Academic Publishers, p. 191.   
Wallace, P. T., Capitaine, N., 2006, “Precession-nutation procedures consistent with IAU 2006 resolutions”, Astron. Astrophys., 459(3), pp. 981–985, doi:10.1051/0004-6361:20065897.   
Williams, J. G., 1994, “Contributions to the Earth’s obliquity rate, precession, and nutation,” Astron. J., 108(2), pp. 711–724, doi:10.1086/117108.   
Williams, J. G., Newhall, X. X., and Dickey, J. O., 1991, “Luni-solar precession: determination from lunar laser ranges,” Astron. Astrophys., 241(1), pp. L9–L12.   
W¨unsch, J., 1991, “Small waves in UT1 caused by the inequality of the equatorial moments of inertia A and B of the Earth,” Astron. Nachr., 312(5), 321–325, doi:10.1002/asna.2113120510.

Gravitational models commonly used in current (2010) precision orbital analysis represent a significant improvement with respect to geopotential model EGM96, the past conventional model of the IERS Conventions (2003), thanks to the availability of CHAMP ${ < } ^ { 1 } >$ and, most importantly, GRACE ${ < } ^ { 2 } >$ data in the 2000s. The IERS, recognizing the recent development of new gravitational models derived from the optimal combination of GRACE data with high resolution gravitational information obtained from surface gravimetry and satellite altimetry data, recommends at this time the EGM2008 model as the conventional model.

The conventional model that is presented in Section 6.1 describes the static part of the field and the underlying background model for the secular variations of some of its coefficients. In addition, other time varying effects should be taken into account: solid Earth tides (Section 6.2), ocean tides (Section 6.3), solid Earth pole tide (Section 6.4), and ocean pole tide (Section 6.5).

The geopotential field $V$ at the point (r, $\phi$ , $\lambda$ ) is expanded in spherical harmonics up to degree N as

$$
V ( r , \phi , \lambda ) = \frac { G M } { r } \sum _ { n = 0 } ^ { N } \left( \frac { a _ { e } } { r } \right) ^ { n } \sum _ { m = 0 } ^ { n } \left[ \bar { C } _ { n m } c o s ( m \lambda ) + \bar { S } _ { n m } s i n ( m \lambda ) \right] \bar { P } _ { n m } ( \sin \phi )
$$

(with $S _ { n 0 } = 0$ ), where $C _ { n m }$ and $S _ { n m }$ are the normalized geopotential coefficients and $\bar { P } _ { n m }$ are the normalized associated Legendre functions. The normalized Legendre function is related to the classical (unnormalized) one by

$$
\bar { P } _ { n m } = N _ { n m } P _ { n m } ,
$$

where

$$
N _ { n m } = { \sqrt { \frac { ( n - m ) ! ( 2 n + 1 ) ( 2 - \delta _ { 0 m } ) } { ( n + m ) ! } } } , \qquad \delta _ { 0 m } = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } m = 0 } \\ { 0 } & { { \mathrm { i f ~ } } m \neq 0 } \end{array} \right. }
$$

Correspondingly, the normalized geopotential coefficients $( \bar { C } _ { n m } , \bar { S } _ { n m } )$ are related to the unnormalized coefficients $\left( C _ { n m } , S _ { n m } \right)$ by

$$
C _ { n m } = N _ { n m } \bar { C } _ { n m } , \quad S _ { n m } = N _ { n m } \bar { S } _ { n m } .
$$

The scaling parameters $( G M , ~ a _ { e } )$ associated with the model are described in Section 6.1. Sections 6.2 to 6.5 provide variations to the normalized coefficients $\left( C _ { n m } , S _ { n m } \right)$ due to the physical effects described in each section.

# 6.1 Conventional model based on the EGM2008 model

The EGM2008 model (Pavlis et al., 2008) is complete to degree and order 2159, and contains additional spherical harmonic coefficients up to degree 2190 and order 2159. The $G M _ { \oplus }$ and $a _ { \mathrm { e } }$ values reported with EGM2008 $( 3 9 8 6 0 0 . 4 4 1 5 ~ \mathrm { k m ^ { 3 } / s ^ { 2 } }$ and 6378136.3 m) should be used as scaling parameters with its gravitational potential coefficients. They are to be considered as TT-compatible values. The recommended TCG-compatible value, $G M _ { \oplus } = 3 9 8 6 0 0 . 4 4 1 8 ~ \mathrm { k m ^ { 3 } / s ^ { 2 } }$ , should be used with the two-body term when working with Geocentric Coordinate Time (TCG) (398600.4415 or 398600.4356 should be used by those still working with Terrestrial Time (TT) or Barycentric Dynamical Time (TDB), respectively). The EGM2008 model (including error estimates) is available at ${ < } ^ { 3 } >$ .

Although EGM2008 is complete to degree and order 2159, most users in space geodesy will find their needs covered by a truncated version of the model. Suggested truncation levels as a function of the orbit of interest are listed in Table 6.1 It is expected that these truncation levels provide a 3-dimensional orbit accuracy of better than $0 . 5 \mathrm { m m }$ for the indicated satellites (Ries, 2010).

Table 6.1: Suggested truncation levels for use of EGM2008 at different orbits   

<table><tr><td>Orbit radius /km</td><td>Example</td><td>Truncation level</td></tr><tr><td>7331</td><td>Starlette</td><td>90</td></tr><tr><td>12270</td><td>Lageos</td><td>20</td></tr><tr><td>26600</td><td>GPS</td><td>12</td></tr></table>

The EGM2008 model was based on the ITG-GRACE03S GRACE-only gravitational model ( ${ < } ^ { 4 } >$ , see also Mayer-G¨urr, 2007) which is available along with its complete error covariance matrix to degree and order 180. Therefore the static gravitational field was developed assuming models complying with the IERS Conventions (2003) and complemented by the following:

• ocean tides: FES2004 (Lyard et al., 2006), • ocean pole tide: Desai (2003, see Section 6.5), • atmosphere and ocean de-aliasing: AOD1B RL04 (Flechtner, 2007).

For some of the low-degree coefficients, the conventional geopotential model uses values which are different from the original EGM2008 values. The static field also assumes values for the secular rates of low-degree coefficients. In order to use the static field properly and project it in time, the secular rates should be accounted for. The instantaneous values of coefficients $C _ { n 0 }$ to be used when computing orbits are given by:

$$
\bar { C } _ { n 0 } ( t ) = \bar { C } _ { n 0 } ( t _ { 0 } ) + d \bar { C } _ { n 0 } / d t \times ( t - t _ { 0 } )
$$

where $t _ { 0 }$ is the epoch J2000.0 and the values of $C _ { n 0 } ( t _ { 0 } )$ and $d C _ { n 0 } / d t$ are given in Table 6.2. Note that the zero-tide $C _ { 2 0 }$ coefficient in the conventional geopotential model is obtained from the analysis of 17 years of SLR data approximately centered on year 2000 and has an uncertainty of $2 \times 1 0 ^ { - 1 1 }$ (Cheng et al., 2010). It differs significantly from the EGM2008 value obtained from 4 years of GRACE data, as it is expected that tide-like aliases will affect GRACE-based $C _ { 2 0 }$ values, depending on the averaging interval used. The tide-free value of $C _ { 2 0 }$ can be obtained as described in Section 6.2.2.

Table 6.2: Low-degree coefficients of the conventional geopotential model   

<table><tr><td>Coefficient</td><td>Value at 2000.0</td><td>Reference</td><td>Rate yr-1</td><td>Reference</td></tr><tr><td>C20 (zero-tide)</td><td>-0.48416948×10-3</td><td>Cheng et al., 2010</td><td>11.6 × 10-12</td><td>Nerem et al., 1993</td></tr><tr><td>C30</td><td>0.9571612×10-6</td><td>EGM2008</td><td>4.9 ×10-12</td><td>Cheng et al., 1997</td></tr><tr><td>C40</td><td>0.5399659×10-6</td><td>EGM2008</td><td>4.7 ×10-12</td><td>Cheng et al., 1997</td></tr></table>

Values for the $C _ { 2 1 }$ and $S _ { 2 1 }$ coefficients are included in the conventional geopotential model. The $C _ { 2 1 }$ and $S _ { 2 1 }$ coefficients describe the position of the Earth’s figure axis. When averaged over many years, the figure axis should closely coincide with the observed position of the rotation pole averaged over the same time period. Any differences between the averaged positions of the mean figure and the mean rotation pole would be due to long-period fluid motions in the atmosphere, oceans, or Earth’s fluid core (Wahr, 1987; 1990). At present, there is no independent evidence that such motions are important. The conventional values for $C _ { 2 1 } ( t )$ and $S _ { 2 1 } ( t )$ are intended to give a mean figure axis that corresponds to the mean pole position consistent with the terrestrial reference frame defined in Chapter 4.

This choice for $C _ { 2 1 }$ and $S _ { 2 1 }$ is realized as follows. First, to use the gravitational potential coefficients to solve for a satellite orbit, it is necessary to rotate from the Earth-fixed frame, where the coefficients are pertinent, to an inertial frame, where the satellite motion is computed. This transformation between frames should include polar motion. We assume the polar motion parameters used are relative to the IERS Reference Pole. Then the values

$$
\begin{array} { r l r } { \bar { C } _ { 2 1 } ( t ) } & { = } & { \sqrt { 3 } \bar { x } _ { p } ( t ) \bar { C } _ { 2 0 } \mathrm { ~ ~ - ~ } \bar { x } _ { p } ( t ) \bar { C } _ { 2 2 } + \bar { y } _ { p } ( t ) \bar { S } _ { 2 2 } , } \\ { \bar { S } _ { 2 1 } ( t ) } & { = } & { - \sqrt { 3 } \bar { y } _ { p } ( t ) \bar { C } _ { 2 0 } \mathrm { ~ ~ - ~ } \bar { y } _ { p } ( t ) \bar { C } _ { 2 2 } - \bar { x } _ { p } ( t ) \bar { S } _ { 2 2 } , } \end{array}
$$

where $\bar { x } _ { p } ( t )$ and $\bar { y } _ { p } ( t )$ (in radians) represent the IERS conventional mean pole (see Section 7.1.4), provide a mean figure axis which coincides with the mean pole consistent with the TRF defined in Chapter 4. Any recent value of $C _ { 2 0 }$ , $C _ { 2 2 }$ and $S _ { 2 2 }$ is adequate for $1 0 ^ { - 1 4 }$ accuracy in Equation (6.5), e.g. the values of the present conventional model (−0.48416948 $\times 1 0 ^ { - 3 }$ , $2 . 4 3 9 3 8 3 6 \times 1 0 ^ { - 6 }$ and $- 1 . 4 0 0 2 7 3 7 { \times } 1 0 ^ { - 6 }$ respectively) can be used.

The models for the low degree terms are generally consistent with the past longterm trends, but these are not strictly linear in reality. There may be decadal variations that are not captured by the models. In addition, they may not be consistent with more recent surface mass trends due to increased ice sheet melting and other results of global climate change.

# 6.2 Effect of solid Earth tides

# 6.2.1 Conventional model for the solid Earth tides

The changes induced by the solid Earth tides in the free space potential are most conveniently modeled as variations in the standard geopotential coefficients $C _ { n m }$ and $S _ { n m }$ (Eanes et al., 1983). The contributions $\Delta C _ { n m }$ and $\Delta S _ { n m }$ from the tides are expressible in terms of the Love number $k$ . The effects of ellipticity and of the Coriothree $k$ s force due toparameters, $k _ { n m } ^ { ( 0 ) }$ rth rand $k _ { n m } ^ { ( \pm ) }$ on on tidal (except for $n = 2$ ations necessitate the use of) to characterize the changes produced in the free space potential by tides of spherical harmonic degree and order $k _ { 2 m } ^ { ( - ) } = 0$ $( n m )$ due to mass conservation. (Wahr, 1981); only two parameters are needed for $n = 2$ because

Anelasticity of the mantle causes $k _ { n m } ^ { ( 0 ) }$ and $k _ { n m } ^ { ( \pm ) }$ to acquire small imaginary parts (reflecting a phase lag in the deformational response of the Earth to tidal forces), and also gives rise to a variation with frequency which is particularly pronounced within the long period band. Though modeling of anelasticity at the periods relevant to tidal phenomena (8 hours to 18.6 years) is not yet definitive, it is clear that the magnitudes of the contributions from anelasticity cannot be ignored (see below). Recent evidence relating to the role of anelasticity in the accurate modeling of nutation data (Mathews et al., 2002) lends support to the model employed herein, at least up to diurnal tidal periods; and there is no compelling reason at present to adopt a different model for the long period tides.

Solid Earth tides within the diurnal tidal band (for which $( n m ) = ( 2 1 )$ ) are not wholly due to the direct action of the tide generating potential (TGP) on the solid Earth; they include the deformations (and associated geopotential changes) arising from other effects of the TGP, namely, ocean tides and wobbles of the mantle and the core regions. Deformation due to wobbles arises from the incremental centrifugal potentials caused by the wobbles; and ocean tides load the crust and thus cause deformations. Anelasticity affects the Earth’s deformational response to all these types of forcing.

The wobbles, in turn, are affected by changes in the Earth’s moment of inertia due to deformations from all sources, and in particular, from the deformation due to loading by the $( n m ) = ( 2 1 )$ part of the ocean tide; wobbles are also affected by the anelasticity contributions to all deformations, and by the coupling of the fluid core to the mantle and the inner core through the action of magnetic fields at its boundaries (Mathews et al., 2002). Resonances in the wobbles—principally, the Nearly Diurnal Free Wobble resonance associated with the FCN —and the consequent resonances in the contribution to tidal deformation from the centrifugal perturbations associated with the wobbles, cause the body tide and load Love/Shida number parameters of the diurnal tides to become strongly frequency dependent. For the derivation of resonance formulae of the form (6.9) below to represent this frequency dependence, see Mathews et al., (1995). The resonance expansions assume that the Earth parameters entering the wobble equations are all frequency independent. However the ocean tide induced deformation makes a frequency dependent contribution to deformability parameters which are among the Earth parameters just referred to. It becomes necessary therefore to add small corrections to the Love number parameters computed using the resonance formulae. These corrections are included in the tables of Love number parameters given in this chapter and the next.

The deformation due to ocean loading is itself computed in the first place using frequency independent load Love numbers (see Section 7.1.2). Corrections to take account of the resonances in the load Love numbers are incorporated through equivalent corrections to the body tide Love numbers, following Wahr and Sasao (1981), as explained further below. These corrections are also included in the tables of Love numbers.

The degree 2 tides produce time dependent changes in $k _ { 2 m } ^ { ( 0 ) }$ , which can exceed $1 0 ^ { - 8 }$ in magnitude. They also produce changes exceeding $C _ { 2 m }$ and $S _ { 2 m }$ , through $3 \times 1 0 ^ { - 1 2 }$ in $C _ { 4 m }$ and $S _ { 4 m }$ through $k _ { 2 m } ^ { ( + ) }$ . (The direct contributions of the degree 4 tidal potential to these coefficients are negligible.) The only other changes exceeding this cutoff are in $C _ { 3 m }$ and $S _ { 3 m }$ , produced by the degree 3 part of the TGP.

The computation of the tidal contributions to the geopotential coefficients is most efficiently done by a three-step procedure. In Step 1, the ( $z m$ ) part of the tidal potential is evaluated in the time domain for each $m$ using lunar and solar ephemerides, and the corresponding chusing frequency independent nominal values s f $\Delta C _ { 2 m }$ and resp $\Delta S _ { 2 m }$ computed. The contributions of the degree 3 tides to the degree 2 tides to $C _ { 4 m }$ and $S _ { 4 m }$ $C _ { 3 m }$ and ugh $k _ { 2 m }$ $S _ { 3 m }$ $k _ { 2 m } ^ { ( + ) }$ through may be computed by a similar $k _ { 3 m } ^ { ( 0 ) }$ and also those of $k _ { 2 m } ^ { ( 0 ) }$ procedure; they are at the level of 10−11.

Step 2 corrects for the deviations of the $k _ { 2 1 } ^ { ( 0 ) }$ of several of the constituent tides of the diurnal band from the constant nominal value $k _ { 2 1 }$ assumed for this band in the first step. Similar corrections need to be applied to a few of the constituents of the other two bands also.

Steps 1 and 2 can be used to compute the total tidal contribution, including the time independent (permanent) contribution to the geopotential coefficient $C _ { 2 0 }$ , which is adequate for a “conventional tide free” model such as EGM96. When using a “zero tide” model, this permanent part should not be counted twice, this is the goal of Step 3 of the computation. See Section 6.2.2.

With frequency-independent values $k _ { n m }$ (Step 1), changes induced by the $( n m )$ part of the TGP in the normalized geopotential coefficients having the same $( n m )$ are given in the time domain by

$$
\Delta \bar { C } _ { n m } - i \Delta \bar { S } _ { n m } = \frac { k _ { n m } } { 2 n + 1 } \sum _ { j = 2 } ^ { 3 } \frac { G M _ { j } } { G M _ { \oplus } } \Big ( \frac { R _ { e } } { r _ { j } } \Big ) ^ { n + 1 } \bar { P } _ { n m } \big ( \sin \Phi _ { j } \big ) e ^ { - i m \lambda _ { j } }
$$

where

$$
\begin{array} { r l } { k _ { n m } } & { = \mathrm { ~ n o m i n a l ~ L o v e ~ n u m b e r ~ f o r ~ d e g r e e ~ } n \mathrm { ~ a n d ~ o r d e r ~ } m , } \\ { R _ { e } } & { = \mathrm { ~ e q u a t o r i a l ~ r a d i u s ~ o f ~ t h e ~ E a r t h } , } \\ { G M _ { \oplus } } & { = \mathrm { ~ g r a v i t a t i o n a l ~ p a r a m e t e r ~ f o r ~ t h e ~ E a r t h } , } \\ { G M _ { j } } & { = \mathrm { ~ g r a v i t a t i o n a l ~ p a r a m e t e r ~ f o r ~ t h e ~ M o o n ~ } ( j = 2 ) a n d \mathrm { ~ S u m ~ } ( j \mathrm { ~ } ; } \\ { r _ { j } } & { = \mathrm { ~ d i s t a n c e ~ f r o m ~ g e o c e n t e r ~ t o ~ M o o n ~ o r ~ S u m } , } \\ { \Phi _ { j } } & { = \mathrm { ~ b o d - h r e a d ~ g e o c e n t r i c ~ l a t i u d e ~ o f ~ M o o n ~ o r ~ S u m } , } \\ { \lambda _ { j } } & { = \mathrm { ~ b o d - h r e a d ~ e n s t ~ l o n g ~ t i n d e ~ ( f r o m ~ G r e e n v i c h ) ~ o f ~ M o o n ~ o r ~ S u m } } \end{array}
$$

Equation (6.6) yields $\Delta C _ { n m }$ and $\Delta S _ { n m }$ for both $n = 2$ and $n = 3$ for all $m$ , apart from the corrections for frequency dependence to be evaluated in Step 2. (The particular case $( n m ) = ( 2 0 )$ needs special consideration, however, as already indicated.)

One further computation to be done in Step 1 is that of the changes in the degree 4 coefficients produced by the degree 2 tides. They are given by

$$
\begin{array} { r l r } { \Delta \bar { C } 4 m - i \Delta \bar { S } 4 m } & { { } = } & { \frac { k _ { 2 m } ^ { ( + ) } } { 5 } \sum _ { j = 2 } ^ { 3 } \frac { G M _ { j } } { G M _ { \oplus } } \left( \frac { R _ { c } } { r _ { j } } \right) ^ { 3 } \bar { P } _ { 2 m } ( \sin \Phi _ { j } ) e ^ { - i m \lambda _ { j } } , \quad ( m = 0 , 1 , 2 ) , } \end{array}
$$

which has the same form as Equation (6.6) for $n = 2$ except for the replacement of $k _ { 2 m }$ by $k _ { 2 m } ^ { ( + ) }$ .

The parameter values for the computations of Step 1 are given in Table 6.3. The choice of these nominal values has been made so as to minimize the number of terms for which corrections will have to be applied in Step 2. The nominal value for has to be chosen real because there is no closed expression for the contribution to $C _ { 2 0 }$ from the imaginary part of $k _ { 2 0 } ^ { ( 0 ) }$ .

Table 6.3: Nominal values of solid Earth tide external potential Love numbers.   

<table><tr><td colspan="4">Elastic Earth</td><td colspan="3">Anelastic Earth</td></tr><tr><td>n</td><td>m</td><td>knm</td><td>k+</td><td>Re knm</td><td>Im knm</td><td>k+</td></tr><tr><td>2</td><td>0</td><td>0.29525</td><td>-0.00087</td><td>0.30190</td><td>-0.00000</td><td>-0.00089</td></tr><tr><td>2</td><td>1</td><td>0.29470</td><td>-0.00079</td><td>0.29830</td><td>-0.00144</td><td>-0.00080</td></tr><tr><td>2</td><td>2</td><td>0.29801</td><td>-0.00057</td><td>0.30102</td><td>-0.00130</td><td>-0.00057</td></tr><tr><td>3</td><td>0</td><td>0.093</td><td>·</td><td></td><td></td><td></td></tr><tr><td>3</td><td>1</td><td>0.093</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>2</td><td>0.093</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>3</td><td>0.094</td><td></td><td></td><td></td><td></td></tr></table>

The frequency dependent corrections to the $\Delta C _ { n m }$ and $\Delta S _ { n m }$ values obtained from Step 1 are computed in Step 2 as the sum of contributions from a number of tidal constituents belonging to the respective bands. The contribution to $\Delta C _ { 2 0 }$ from the long period tidal constituents of various frequencies $f$ is

$$
\begin{array} { r l r } { \mathrm { R e } \sum _ { f ( 2 , 0 ) } ( A _ { 0 } \delta k _ { f } H _ { f } ) e ^ { i \theta _ { f } } } & { { } = } & { \sum _ { f ( 2 , 0 ) } [ \left( A _ { 0 } H _ { f } \delta k _ { f } ^ { R } \right) \cos \theta _ { f } - \left( A _ { 0 } H _ { f } \delta k _ { f } ^ { I } \right) \sin \theta _ { f } ] , } \end{array}
$$

while the contribution to $\left( \Delta C _ { 2 1 } - i \Delta S _ { 2 1 } \right)$ from the diurnal tidal constituents and to $\Delta C _ { 2 2 } - i \Delta S _ { 2 2 }$ from the semidiurnals are given by

$$
\Delta \bar { C } _ { 2 m } - i \Delta \bar { S } _ { 2 m } = \eta _ { m } \sum _ { f ( 2 , m ) } \left( A _ { m } \delta k _ { f } H _ { f } \right) e ^ { i \theta _ { f } } , \quad ( m = 1 , 2 ) ,
$$

where

$$
\begin{array} { l } { { A _ { 0 } = \displaystyle \frac { 1 } { R _ { e } \sqrt { 4 \pi } } = 4 . 4 2 2 8 \times 1 0 ^ { - 8 } \mathrm { m } ^ { - 1 } , } } \\ { { } } \\ { { A _ { m } = \displaystyle \frac { ( - 1 ) ^ { m } } { R _ { e } \sqrt { 8 \pi } } = ( - 1 ) ^ { m } ( 3 . 1 2 7 4 \times 1 0 ^ { - 8 } ) \mathrm { m } ^ { - 1 } , \qquad ( m \neq 0 ) , } } \\ { { } } \\ { { \displaystyle \eta _ { 1 } = - i , \eta _ { 2 } = 1 , } } \end{array}
$$

$\begin{array} { r c l } { { \delta k _ { f } } } & { { = } } & { { \mathrm { { \normalfont ~ d i f f e r e n c e ~ b e t w e e n ~ } } k _ { f } \mathrm { ~ d e f i n e d ~ a s ~ } k _ { 2 m } ^ { ( 0 ) } \mathrm { { \normalfont ~ a t ~ f r e q u e } } } } \\ { { } } & { { } } & { { \mathrm { { \normalfont ~ t h e ~ n o m i n a l ~ v a l u e ~ } } k _ { 2 m } , \mathrm { { \normalfont ~ i n ~ t h e ~ s e n s e ~ } } k _ { f } - k _ { 2 m } , } } \\ { { } } & { { } } & { { \mathrm { { \normalfont ~ c o t r i b u t i o n ~ f r o m ~ o c e a n ~ n o d i n g } } , } } \\ { { \delta k _ { f } ^ { R } } } & { { = } } & { { \mathrm { { \normalfont ~ r e a l ~ p a r t ~ o f ~ } } \delta k _ { f } , \mathrm { { \normalfont ~ a n d } ~ } } } \\ { { } } & { { } } & { { \mathrm { { \normalfont ~ \delta ~ i n a g i n a r y ~ p a r t ~ o f ~ } } \delta k _ { f } , \mathrm { { \normalfont ~ i . e . } } , \delta k _ { f } = \delta k _ { f } ^ { R } + i \delta k _ { f } ^ { R } , } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle H _ { f } } } & { { = } } & { { \mathrm { { \normalfont ~ a n p l i t a d e ~ ( i n ~ m e t e r s ) ~ o f ~ t h e ~ t e r m ~ a t ~ f r e q u e n c e } } } } \\ { { } } & { { } } & { { \mathrm { { \normalfont ~ t h e ~ h a r m o n i c ~ e x p a n s i o n ~ o f ~ t h e ~ t i d e ~ g e n e r a t i n g } } } } \\ { { } } & { { } } & { { \mathrm { { \normalfont ~ d e f i n e d ~ a c o r d i n g ~ t o ~ c o n v e n t i o n ~ o f ~ c a r t w r i } } } } \\ { { } } & { { } } &  { \mathrm { { \normalfont ~ { \it ~ T } a n e r ~ } } ( 1 9 \mathrm { { \normalfont ~ \cdot ~ } } n \mathrm { { \normalfont ~ a n d } ~ } ) \mathrm { { \normalfont ~ a n d } ~ } } \end{array}$ at frequency $f$ and plus a $f$ from potential, ght and   
$\begin{array} { r l r } { \theta _ { f } } & { { } = } & { { \bar { n } } \cdot { \bar { \beta } } = \sum _ { i = 1 } ^ { 6 } n _ { i } \beta _ { i } , \qquad \mathrm { o r } } \\ { \theta _ { f } } & { { } = } & { m ( \theta _ { g } + \pi ) - { \bar { N } } \cdot { \bar { F } } = m ( \theta _ { g } + \pi ) - \sum _ { j = 1 } ^ { 5 } N _ { j } F _ { j } , } \end{array}$   
where   
$\begin{array} { r c l } { { \bar { \beta } } } & { { = } } & { { \mathrm { s i x - v e c t o r ~ o f ~ D o o d s o n ' s ~ f u n d a m e n t a l ~ a r g u m e n t s ~ } \beta _ { i } , } } \\ { { } } & { { } } & { { ( \tau , s , h , p , N ^ { \prime } , p _ { s } ) , } } \\ { { } } & { { \bar { n } } } & { { = } } & { { \mathrm { s i x - v e c t o r ~ o f ~ m u l t i p l i e r s ~ } n _ { i } \mathrm { ~ ( f o r ~ t h e ~ t e r m ~ a t ~ f r e q u e n c y ~ } f } } \\ { { } } & { { } } & { { \mathrm { o f ~ t h e ~ f u n d a m e n t a l ~ a r g u m e n t s , } } } \\ { { \bar { F } } } & { { = } } & { { \mathrm { f i v e - v e c t o r ~ o f ~ f u n d a m e n t a l ~ a r g u m e n t s ~ } F _ { j } \qquad \quad } } \\ { { } } & { { } } & { { \mathrm { ( t h e ~ D e l a u n a n y ~ v a r i a b l e s ~ } l , l ^ { \prime } , F , D , \Omega ) \mathrm { ~ o f ~ n u t a t i o n ~ t h e o r y } } } \\ { { } } & { { } } & { { \mathrm { ( f i v e - v e c t o r ~ o f ~ m u l t i p l i e r s ~ } N _ { j } \mathrm { ~ o f ~ t h e ~ D e l a u m a y ~ v a r i a b l e s ~ f ~ } } } \\ { { } } & { { } } & { { \mathrm { t h e ~ n u t a t i o n ~ o f ~ f e e q u e n c y ~ } - f + \omega _ { g } / d t , } } \end{array}$ ) , or   
and $\theta _ { g }$ is the Greenwich Mean Sidereal Time expressed in angle   
units (i.e. $2 4 ~ \mathrm { h } = 3 6 0 ^ { \circ }$ ; see Chapter 5).   
( $^ { - \prime \prime }$ in $( \theta _ { g } + \pi )$ is now to be replaced by $1 8 0 ^ { \circ }$ .)

For the fundamental arguments $\left( l , l ^ { \prime } , F , D , \Omega \right)$ of nutation theory and the convention followed here in choosing their multipliers $N _ { j }$ , see Chapter 5. For conversion of tidal amplitudes defined according to different conventions to the amplitude $H _ { f }$ corresponding to the Cartwright-Tayler convention, use Table 6.8 given at the end of this chapter.

For diurnal tides, the frequency dependent values of any load or body tide Love number parameter $L$ (such as $k _ { 2 1 } ^ { ( 0 ) }$ or $k _ { 2 1 } ^ { ( + ) }$ in the present context) may be represented as a function of the tidal excitation frequency $\sigma$ by a resonance formula

$$
L ( \sigma ) = L _ { 0 } + \sum _ { \alpha = 1 } ^ { 3 } \frac { L _ { \alpha } } { ( \sigma - \sigma _ { \alpha } ) } ,
$$

except for the small corrections referred to earlier. (They are to take account of frequency dependent contributions to a few of the Earth’s deformability parameters, which make (6.9) inexact.) The $\sigma _ { \alpha }$ , $( \alpha = 1 , 2 , 3$ ), are the respective resonance frequencies associated with the Chandler wobble (CW), the retrograde FCN, and the prograde free core nutation (also known as the free inner core nutation), and the $L _ { \alpha }$ are the corresponding resonance coefficients. All the parameters are complex. The $\sigma _ { \alpha }$ and $\sigma$ are expressed in cycles per sidereal day (cpsd), with the convention that positive (negative) frequencies represent retrograde (prograde) waves. (This sign convention, followed in tidal theory, is the opposite of that employed in analytical theories of nutation.) In particular, given the tidal frequency $f$ in degrees per hour, one has

$$
\sigma = f / ( 1 5 \times 1 . 0 0 2 7 3 7 9 0 9 ) ,
$$

the factor 1.002737909 being the number of sidereal days per solar day. The values used herein for the $\sigma _ { \alpha }$ are from Mathews et al. (2002), adapted to the sign

convention used here:

They were estimated from a fit of nutation theory to precession rate and nutation amplitude estimates found from an analyis of very long baseline interferometry (VLBI) data.

Table 6.4 lists the values of $L _ { 0 }$ and $L _ { \alpha }$ in resonance formulae of the form (6.9) for k(0)21 and $k _ { 2 1 } ^ { ( + ) }$ . They were obtained by evaluating the relevant expressions from Mathews et al. (1995), using values taken from computations of Buffett and Mathews (unpublished) for the needed deformability parameters together with values obtained for the wobble resonance parameters in the course of computations of the nutation results of Mathews et al. (2002). The deformability parameters for an elliptical, rotating, elastic, and oceanless Earth model based on the 1- second reference period preliminary reference Earth model (PREM) (Dziewonski and Anderson, 1981) with the ocean layer replaced by solid, and corrections to these for the effects of mantle anelasticity, were found by integration of the tidal deformation equations. Anelasticity computations were based on the Widmer et al. (1991) model of mantle $Q$ . As in Wahr and Bergen (1986), a power law was assumed for the frequency dependence of $Q$ , with 200 $s$ as the reference period; the value $\alpha = 0 . 1 5$ was used for the power law index. The anelasticity contribution (out-of-phase and in-phase) to the tidal changes in the geopotential coefficients is at the level of $1 - 2 \%$ in-phase, and $0 . 5 - 1 \%$ out-of-phase, i.e., of the order of $1 0 ^ { - 1 0 }$ . The effects of anelasticity, ocean loading and currents, and electromagnetic couplings on the wobbles result in indirect contributions to $k _ { 2 1 } ^ { ( 0 ) }$ and $k _ { 2 1 } ^ { ( + ) }$ which are almost fully accounted for through the values of the wobble resonance parameters. Also shown in Table 6.4 are the resonance parameters for the load Love numbers $h _ { 2 1 } ^ { \prime }$ , $k _ { 2 1 } ^ { \prime }$ , and $l _ { 2 1 } ^ { \prime }$ , which are relevant to the solid Earth deformation caused by ocean tidal loading and to the consequential changes in the geopotential. (Only the real parts are shown: the small imaginary parts make no difference to the effect to be now considered which is itself small.)

Table 6.4: Parameters in the resonance formulae for $k _ { 2 1 } ^ { ( 0 ) }$ $k _ { 2 1 } ^ { ( + ) }$ and the load Love numbers.   

<table><tr><td colspan="3"></td><td colspan="2">（）</td></tr><tr><td>α</td><td>ReLα</td><td>Im Lα</td><td>Re Lα</td><td>Im Lα</td></tr><tr><td>0</td><td>0.29954</td><td>-0.1412 × 10-2</td><td>-0.804 × 10-3</td><td>0.237 × 10-5</td></tr><tr><td>1</td><td>-0.77896 × 10-3</td><td>-0.3711 × 10-4</td><td>0.209 × 10-5</td><td>0.103 × 10-6</td></tr><tr><td>2</td><td>0.90963 × 10-4</td><td>-0.2963 × 10-5</td><td>-0.182 × 10-6</td><td>0.650 × 10-8</td></tr><tr><td>3</td><td>-0.11416 × 10-5</td><td>0.5325 ×10-7</td><td>-0.713 × 10-9</td><td>-0.330 × 10-9</td></tr><tr><td colspan="5">Load Love numbers (Real parts only)</td></tr><tr><td></td><td>h1</td><td>1</td><td>K21</td><td></td></tr><tr><td>0</td><td>-0.99500</td><td>0.02315</td><td>-0.30808</td><td></td></tr><tr><td>1</td><td>1.6583 × 10-3</td><td>2.3232 ×10-4</td><td>8.1874 × 10-4</td><td></td></tr><tr><td>2</td><td>2.8018 × 10-4</td><td>-8.4659 × 10-6</td><td>1.4116 × 10-4</td><td></td></tr><tr><td>3</td><td>5.5852 × 10-7</td><td>1.0724 × 10-8</td><td>3.4618 × 10-7</td><td></td></tr></table>

The expressions given in Section 6.3 for the contributions from ocean tidal loading assume the constant nominal value $k _ { 2 } ^ { \prime ( \mathrm { n o m ) } } = - 0 . 3 0 7 5$ for $k ^ { \prime }$ of the degree 2 tides. Further contributions arise from the frequency dependence of $k _ { 2 1 } ^ { \prime }$ . These may be expressed, following Wahr and Sasao (1981), in terms of an effective ocean tide contribution $\delta k ^ { ( O T ) } ( \sigma )$ to the body tide Love number $k _ { 2 1 } ^ { ( 0 ) }$ :

$$
\delta k ^ { ( O T ) } ( \sigma ) = [ k _ { 2 1 } ^ { \prime } ( \sigma ) - k _ { 2 } ^ { \prime ( \mathrm { n o m } ) } ] \left( \frac { 4 \pi G \rho _ { w } R } { 5 \bar { g } } \right) A _ { 2 1 } ( \sigma ) ,
$$

where $G$ is the constant of universal gravitation, $\rho _ { w }$ is the density of sea water $( 1 0 2 5 ~ \mathrm { k g ~ m } ^ { - 3 }$ ), $R$ is the Earth’s mean radius $( 6 . 3 7 1 \times 1 0 ^ { 6 } \mathrm { ~ m }$ ), $g$ is the mean acceleration due to gravity at the Earth’s surface $( 9 . 8 2 0 \mathrm { ~ m ~ s ~ } ^ { - 2 }$ ), and $A _ { 2 1 } ( \sigma )$ is the admittance for the degree 2 tesseral component of the ocean tide of frequency $\sigma$ in cpsd:

$$
A _ { 2 1 } ( \sigma ) = \zeta _ { 2 1 } ( \sigma ) / \bar { H } ( \sigma ) .
$$

$\zeta _ { 2 1 }$ is the complex amplitude of the height of the $( n m ) = ( 2 1 )$ component of the ocean tide, and $H$ is the height equivalent of the amplitude of the tide generating potential, the bar being a reminder that the spherical harmonics used in defining the two amplitudes should be identically normalized. Wahr and Sasao (1981) employed the factorized form

$$
A _ { 2 1 } ( \sigma ) = f _ { F C N } ( \sigma ) f _ { O D } ( \sigma ) ,
$$

wherein the first factor represents the effect of the FCN resonance, and the second, that of other ocean dynamic factors. The following empirical formulae (Mathews et al., 2002) which provide good fits to the FCN factors of a set of 11 diurnal tides (Desai and Wahr, 1995) and to the admittances obtainable from the ocean load angular momenta of four principal tides (Chao et al., 1996) are used herein:

$$
\begin{array} { c l c r } { { f _ { O D } ( \sigma ) = ( 1 . 3 1 0 1 - 0 . 8 0 9 8 i ) - ( 1 . 1 2 1 2 - 0 . 6 0 3 0 i ) \sigma , } } \\ { { f _ { F C N } ( \sigma ) = 0 . 1 7 3 2 + 0 . 9 6 8 7 f _ { e q m } ( \sigma ) , } } \\ { { f _ { e q m } ( \sigma ) = \displaystyle \frac { \gamma ( \sigma ) } { 1 - ( 3 \rho _ { w } / 5 \bar { \rho } ) \gamma ^ { \prime } ( \sigma ) } , } } \end{array}
$$

where $\gamma = 1 + k - h$ and $\gamma ^ { \prime } = 1 + k ^ { \prime } - h ^ { \prime }$ , is the Earth’s mean density. (Here $k$ stands for $k _ { 2 1 } ^ { ( 0 ) }$ , and similarly for the other symbols. Only the real parts need be used.) $f _ { e q m }$ is the FCN factor for a global equilibrium ocean.

Table 6.5a shows the values of

$$
\delta k _ { f } \equiv ( k _ { 2 1 } ^ { ( 0 ) } ( \sigma ) - k _ { 2 1 } ) + \delta k _ { 2 1 } ^ { O T } ( \sigma ) ,
$$

along with the real and imaginary parts of the amplitude $\left( A _ { 1 } \delta k _ { f } H _ { f } \right)$ . The tides listed are those for which either of the parts is at least $1 0 ^ { - 1 3 }$ after round-off. (A cutoff at this level is used for the individual terms in order that accuracy at the level of $3 \times 1 0 ^ { - 1 2 }$ be not affected by the accumulated contributions from the numerous smaller terms that are disregarded.) Roughly half the value of the imaginary part comes from the ocean tide term, and the real part contribution from this term is of about the same magnitude.

The values used for $k _ { 2 1 } ^ { ( 0 ) } ( \sigma )$ in evaluating $\delta k _ { f }$ are from an exact computation necessarily involving use of the framework of nutation-wobble theory which is outside the scope of this chapter. If the (approximate) resonance formula were used instead for the computation, the resulting numbers for $\delta k _ { f } ^ { R }$ and $\delta k _ { f } ^ { I }$ would require small corrections to match the exact values. In units of $1 0 ^ { - 5 }$ , they are (inphase, out-of-phase) (1, 1) for $\mathrm { Q _ { 1 } }$ , (1, 1) for O $^ { 1 }$ and its companion having Doodson numbers 145,545, (1, 0) for $N o _ { 1 }$ , $( 0 , - 1 )$ for $\mathrm { P _ { 1 } }$ , (244, 299) for $\psi _ { 1 }$ , (12, 12) for $\phi _ { 1 }$ , (3, 2) for $\mathrm { J } _ { 1 }$ , and (2, 1) for $O o _ { 1 }$ and its companion with Doodson numbers 185,565. These are the only tides for which the corrections would contribute nonnegligibly to the numbers listed in the last two columns of the table.

Calculation of the correction due to any tidal constituent is illustrated by the following example for $K _ { 1 }$ . Given that $A _ { m } = A _ { 1 } = - 3 . 1 2 7 4 \times 1 0 ^ { - 8 }$ , and that $H _ { f } = 0 . 3 6 8 7 0$ , $\begin{array} { r } { \theta _ { f } = ( \theta _ { g } + \pi ) } \end{array}$ , and $k _ { 2 1 } ^ { ( 0 ) } = ( 0 . 2 5 7 4 6 + 0 . 0 0 1 1 8 i )$ for this tide, one finds on subtracting the nominal value $( 0 . 2 9 8 3 0 - 0 . 0 0 1 4 4 i )$ that $\delta k _ { f } = ( - 0 . 0 4 0 8 4 +$ $0 . 0 0 2 6 2 i$ ). Equation (6.8b) then yields:

$$
\begin{array} { r l r } { \left( \Delta \bar { C } _ { 2 1 } \right) _ { K _ { 1 } } } & { = } & { 4 7 0 . 9 \times 1 0 ^ { - 1 2 } \sin ( \theta _ { g } + \pi ) - 3 0 . 2 \times 1 0 ^ { - 1 2 } \cos ( \theta _ { g } + \pi ) , } \\ { \left( \Delta \bar { S } _ { 2 1 } \right) _ { K _ { 1 } } } & { = } & { 4 7 0 . 9 \times 1 0 ^ { - 1 2 } \cos ( \theta _ { g } + \pi ) + 3 0 . 2 \times 1 0 ^ { - 1 2 } \sin ( \theta _ { g } + \pi ) . } \end{array}
$$

Table 6.5a: The in-phase ( of the corrections for frequency dependence of $\imath p$ ) amplitudes $( A _ { 1 } \delta k _ { f } ^ { R } H _ { f } )$ and the out-of-phase ( $k _ { 2 1 } ^ { ( 0 ) }$ , taking the nominal value ) amplitudes $( A _ { 1 } \delta k _ { f } ^ { I } H _ { f } )$ $k _ { 2 1 }$ for the diurnal tides as $\mathrm { 0 . 2 9 8 3 0 - } i 0 . 0 0 1 4 4 \mathrm { ) }$ . Units: $1 0 ^ { - 1 2 }$ . The entries for $\delta k _ { f } ^ { R }$ and $\delta k _ { f } ^ { I }$ are in units of $1 0 ^ { - 5 }$ . Multipliers of the Doodson arguments identifying the tidal terms are given, as also those of the Delaunay variables characterizing the nutations produced by these   

<table><tr><td colspan="3">terms.</td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2">TshpN&#x27;</td><td rowspan="2">ps</td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2">leFdΩ</td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2">8</td><td rowspan="2"></td><td rowspan="2">Amp.Amp.</td></tr><tr><td>Name</td><td>deg/hr</td><td>Doodson</td><td></td><td>8k</td></tr><tr><td></td><td></td><td>No.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>/10-5</td><td>/10-5</td><td>(ip)</td><td>(op)</td></tr><tr><td>2Q1</td><td>12.85429</td><td>125,755</td><td>1 -3</td><td>0</td><td>2 0</td><td>0</td><td>2</td><td>0</td><td>2 0</td><td></td><td>-29</td><td>3</td><td>-0.1</td><td>0.0</td></tr><tr><td>01</td><td>12.92714</td><td>127,555</td><td>1 -3</td><td>2</td><td>0 0</td><td>0</td><td>0</td><td>0</td><td>2 2</td><td>2</td><td>-30</td><td>3</td><td>-0.1</td><td>0.0</td></tr><tr><td></td><td>13.39645</td><td>135,645</td><td>1 -2</td><td>0</td><td>1 -1</td><td>0</td><td>1</td><td>0</td><td>2 0</td><td>1</td><td>-45</td><td>5</td><td>-0.1</td><td>0.0 0.1</td></tr><tr><td rowspan="4">Q1 p1</td><td>13.39866</td><td>135,655</td><td>1 -2</td><td>0 1</td><td>0</td><td>0</td><td>1 0</td><td>2</td><td>0</td><td>2</td><td>-46</td><td>5</td><td>-0.7 -0.1</td></tr><tr><td>13.47151 13.94083</td><td>137,455</td><td>1 -2</td><td>2 -1</td><td>0</td><td>0</td><td>-1 0</td><td>2</td><td>2</td><td>2</td><td>-49</td><td>5</td><td>0.0 0.1</td></tr><tr><td></td><td>145,545</td><td>1 -1</td><td>0</td><td>0 -1</td><td>0</td><td>0</td><td>0 2</td><td>0</td><td>1</td><td>-82</td><td>7</td><td>-1.3</td></tr><tr><td>01 13.94303</td><td>145,555</td><td>1 -1</td><td>0 2</td><td>0 0</td><td>0</td><td>0 0</td><td>2</td><td>0</td><td>2</td><td>-83</td><td>7</td><td>-6.8 0.6</td></tr><tr><td rowspan="4">T1 NT1</td><td>14.02517</td><td>147,555 1</td><td>-1</td><td>0 1</td><td>0 0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>-91 -168</td><td>9</td><td>0.1</td><td>0.0 0.0</td></tr><tr><td>14.41456</td><td>153,655</td><td>1 0</td><td>-2 0</td><td>0</td><td>0</td><td>1 0</td><td>2</td><td>-2</td><td>0</td><td></td><td>14 16</td><td>0.1</td></tr><tr><td>14.48520 14.48741</td><td>155,445 155,455</td><td>1 0 0</td><td>-1 -1</td><td>-1</td><td>0 -1</td><td>0</td><td>2</td><td>0</td><td>1 -193</td><td></td><td></td><td>0.1 0.0</td></tr><tr><td rowspan="2">Lk1 N01</td><td></td><td>1</td><td>0 0</td><td>0 0</td><td>0</td><td>-1</td><td>0 2</td><td>0</td><td>2</td><td>-194</td><td>16</td><td>0.4 0.0</td></tr><tr><td>14.49669 155,655</td><td>1 0</td><td>0</td><td>1 1</td><td>0 0</td><td>1</td><td>0 0</td><td>0</td><td>0</td><td>-197</td><td>16</td><td>1.3 -0.1</td></tr><tr><td rowspan="2">X1</td><td>14.49890 14.56955</td><td>155,665 157,455</td><td>1 0 0</td><td>-1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0 1</td><td>-198</td><td>16</td><td>0.3</td><td>0.0 0.0</td></tr><tr><td>14.57176</td><td></td><td>1 1</td><td>2 2 -1</td><td>0 1</td><td>0</td><td>-1 0</td><td>0</td><td>2</td><td>0</td><td>-231</td><td>18</td><td></td><td>0.3</td></tr><tr><td rowspan="2">T1</td><td>14.91787</td><td>157,465 162,556</td><td>0 1 1</td><td>-3 0</td><td>0</td><td>0 -1</td><td>0</td><td>0</td><td>2</td><td>1</td><td>-233</td><td>18</td><td>0.1 0.0</td></tr><tr><td>14.95673</td><td>1</td><td>1</td><td>-2 0</td><td>-1</td><td>1 0</td><td>0 1 0</td><td>2 2</td><td>-2 心</td><td>2 1</td><td>-834</td><td>58</td><td>-1.9 0.1 0.5</td></tr><tr><td rowspan="2">P1</td><td>14.95893</td><td>163,545 163,55</td><td>1</td><td>-2 0</td><td>0 0</td><td>0 0</td><td>0</td><td>2</td><td>-2</td><td>-1117 -1138</td><td>76 77</td><td>-43.4</td><td>0.0 2.9</td></tr><tr><td>15.00000</td><td>164,54</td><td>1 1 1</td><td>-1 0</td><td>0</td><td>-1</td><td>0 -1</td><td>2</td><td>-2</td><td></td><td>-1764</td><td>104</td><td>0.0</td><td>0.6</td></tr><tr><td rowspan="4">S1</td><td>15.00000</td><td>164,556 1</td><td>1</td><td>-1 0</td><td>0</td><td>1 0</td><td>1</td><td>0</td><td>0</td><td>0 -1764</td><td>104</td><td></td><td>1.6 -0.1</td></tr><tr><td>15.02958</td><td>165,345 1</td><td>1</td><td>-2 0</td><td>-1</td><td>0 -2</td><td>0</td><td>2</td><td>0</td><td>1 -3048</td><td></td><td>92</td><td>0.0</td></tr><tr><td>15.03665</td><td>165,535</td><td>1 1</td><td>0 0</td><td>-2</td><td>0</td><td>0 0</td><td>0</td><td>0</td><td>-2</td><td></td><td></td><td>0.1 0.1</td></tr><tr><td>15.03886</td><td>165,545 1</td><td>1</td><td>0 0</td><td>-1</td><td>0 0</td><td>0</td><td>0</td><td>0 -1</td><td>-3630 -3845</td><td>195 229</td><td>-8.8</td><td>0.0 0.5</td></tr><tr><td rowspan="6">K1 15.07993</td><td>15.04107 15.04328</td><td>165,555 1</td><td>1</td><td>0 0</td><td>0 0</td><td>0</td><td>0</td><td>0 0</td><td>0</td><td>-4084</td><td>262</td><td>470.9</td><td>-30.2</td></tr><tr><td></td><td>165,565</td><td>1 1</td><td>0 0</td><td>1</td><td>0</td><td>0 0</td><td>0</td><td>0</td><td>1 -4355</td><td>297</td><td>68.1</td><td>-4.6</td></tr><tr><td>15.04548</td><td>165,575 1</td><td>1</td><td>0 0</td><td>2 0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2 -4665</td><td>334</td><td>-1.6</td><td>0.1</td></tr><tr><td>15.07749</td><td>166,455 1</td><td>1</td><td>1 -1</td><td>0</td><td>0 -1</td><td>0</td><td>0 1</td></table>

The variation of $k _ { 2 0 } ^ { ( 0 ) }$ across the zonal tidal band, $( n m ) = ( 2 0 )$ , is due to mantle anelasticity; it is described by the formula

$$
k _ { 2 0 } ^ { ( 0 ) } = 0 . 2 9 5 2 5 - 5 . 7 9 6 \times 1 0 ^ { - 4 } \left\{ \cot \frac { \alpha \pi } { 2 } \left[ 1 - \left( \frac { f _ { m } } { f } \right) ^ { \alpha } \right] + i \left( \frac { f _ { m } } { f } \right) ^ { \alpha } \right\}
$$

on the basis of the anelasticity model referred to earlier. Here $f$ is the frequency   
of the zonal tiof 200 s, and tuent, . The $f _ { m }$ is the refein Table frequency are the d a peween $\alpha = 0 . 1 5$ $\delta k _ { f }$ $6 . 5 \mathrm { b }$ $k _ { 2 0 } ^ { ( 0 ) }$ $k _ { 2 0 } = 0 . 3 0 1 9 0$   
Table 6.3.

The total variation in geopotential coefficient $\bar { C } _ { 2 0 }$ is obtained by adding to the result of Step 1 the sum of the contributions from the tidal constituents listed in Table 6.5b computed using Equation (6.8a). The tidal variations in $C _ { 2 m }$ and $S _ { 2 m }$ for the other $m$ are computed similarly, except that Equation (6.8b) is to be used together with Table 6.5a for $m = 1$ and Table 6.5c for $m = 2$ .

Table 6.5b: Corrections for frequency dependence of $k _ { 2 0 } ^ { ( 0 ) }$ of the zonal tides due to anelasticity. Units: . The nominal value $k _ { 2 0 }$ for the zonal tides is taken as 0.30190. The real and imaginary parts $\delta k _ { f } ^ { R }$ and $\delta k _ { f } ^ { I }$ of $\delta k _ { f }$ are listed, along with the corresponding in-phase   

<table><tr><td>Equation (6.8a).</td><td>(ip) amplitude(AoHfδkf） and out-of-phase (op) amplitude(AoHfδkf）to be used in</td></tr><tr><td>Name</td><td>Doodson(</td><td>deg/hr T s h p N&#x27; psl l&#x27; FD Ω</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>sk L</td><td>Amp. (ip)</td><td>sk</td><td>Amp.</td></tr><tr><td rowspan="9">Sa Ssa</td><td>No.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>(op)</td></tr><tr><td>55,565</td><td>0.00221</td><td>0 0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1 0.01347</td><td>16.6</td><td>-0.00541</td><td>-6.7</td></tr><tr><td>55,575</td><td>0.00441</td><td>0 0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0 2</td><td>0.01124</td><td>-0.1</td><td>-0.00488</td><td>0.1</td></tr><tr><td>56,554</td><td>0.04107</td><td>0 0</td><td>1</td><td>0</td><td>0</td><td>-1</td><td>0</td><td>-1</td><td>0</td><td>0 0</td><td>0.00547</td><td>-1.2</td><td>-0.00349</td><td>0.8</td></tr><tr><td>57,555</td><td>0.08214</td><td>0 0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-2</td><td>2 -2</td><td>0.00403</td><td>-5.5</td><td>-0.00315</td><td>4.3</td></tr><tr><td>57,565</td><td>0.08434</td><td>0 0</td><td>2</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>-2</td><td>2 -1 -2</td><td>0.00398</td><td>0.1</td><td>-0.00313</td><td>-0.1</td></tr><tr><td>58,554</td><td>0.12320</td><td>0 0</td><td>3</td><td>0</td><td>0</td><td>-1</td><td>0</td><td>-1</td><td>-2</td><td>2</td><td>0.00326</td><td>-0.3</td><td>-0.00296</td><td>0.2</td></tr><tr><td>Msm 63,655</td><td>0.47152</td><td>0 1</td><td>-2</td><td>1 -1</td><td>0 -1</td><td>0 0</td><td>1 -1</td><td>0 0</td><td>0 0</td><td>-2 0</td><td>0</td><td>0.00101 -0.3</td><td>-0.00242</td><td>0.7</td></tr><tr><td rowspan="2">Mm</td><td>65,445</td><td>0.54217 0</td><td>1 1</td><td>0 0 -1</td><td></td><td></td><td></td><td></td><td></td><td>0</td><td>-1 0</td><td>0.00080 0.00080</td><td>0.1 -1.2</td><td>-0.00237</td><td>-0.2</td></tr><tr><td>65,455</td><td>0.54438 0</td><td>01</td><td>0-1</td><td></td><td>0 1</td><td>0 0</td><td>-1 -1</td><td>0 0</td><td>0 0</td><td>0 1</td><td>0.00079</td><td>0.1</td><td>-0.00237 -0.00237</td><td>3.7</td></tr><tr><td rowspan="3">Msf</td><td>65,465</td><td>0.54658</td><td>1</td><td></td><td></td><td>0</td><td>0</td><td>1</td><td>0</td><td>-2</td><td>0</td><td>-2</td><td>0.00077</td><td>0.1</td><td>-0.00236</td><td>-0.2 -0.2</td></tr><tr><td>65,655</td><td>0.55366</td><td>0</td><td>0</td><td>1 0</td><td></td><td></td><td></td><td>0</td><td>0</td><td>0 -2</td><td>0</td><td>-0.00009</td><td>0.0</td><td>-0.00216</td><td></td></tr><tr><td>73,555</td><td>1.01590</td><td>0 2 0</td><td>-2 0</td><td>-2</td><td>0 0</td><td>0 0</td><td></td><td></td><td>0</td><td>0 0</td><td>0</td><td>-0.00018</td><td>0.0</td><td>-0.00213</td><td>0.6</td></tr><tr><td rowspan="3">Mf</td><td>75,355</td><td>1.08875</td><td>2</td><td></td><td></td><td></td><td></td><td>-2</td><td>0</td><td>-2</td><td>0</td><td>-2</td><td>-0.00019</td><td>0.6</td><td>-0.00213</td><td>0.3 6.3</td></tr><tr><td>75,555</td><td>1.09804</td><td>0 2</td><td>0</td><td>0 0</td><td>0</td><td>0</td><td></td><td>0 0</td><td>0-2</td><td>0</td><td>-1</td><td>-0.00019</td><td>0.2</td><td>-0.00213</td><td></td></tr><tr><td>75,565</td><td>1.10024</td><td>0 2</td><td>0 0</td><td>0</td><td>1 2</td><td>0 0</td><td>0</td><td></td><td>0-2</td><td>0</td><td>0</td><td>-0.00019</td><td>0.0</td><td>-0.00213</td><td>2.6 0.2</td></tr><tr><td rowspan="4">Mstm Mtm</td><td>75,575</td><td>1.10245</td><td>0 2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-2</td><td>-2</td><td>-0.00065</td><td>0.1</td><td>-0.00202</td><td></td></tr><tr><td>83,655</td><td>1.56956</td><td>0</td><td>3-2</td><td>1</td><td>0</td><td>0</td><td>1</td><td></td><td>0-2</td><td>0</td><td>-2</td><td>-0.00071</td><td>0.4</td><td>-0.00201</td><td>0.2</td></tr><tr><td>85,455</td><td>1.64241</td><td>0 3</td><td>0</td><td>-1</td><td>0 1</td><td>0 0</td><td>-1 -1</td><td>0</td><td>-2 0-2</td><td>0</td><td>-1</td><td>-0.00071</td><td>0.2</td><td>-0.00201</td><td>1.1</td></tr><tr><td>85,465</td><td>1.64462</td><td>0 3</td><td>-2</td><td>0-1 0</td><td>0</td><td>0</td><td></td><td>0</td><td>0 -2</td><td>-2</td><td>-2</td><td>-0.00102</td><td>0.1</td><td>-0.00193</td><td>0.5 0.2</td></tr><tr><td>Msqm</td><td>93,555</td><td>2.11394</td><td>0 4</td><td></td><td></td><td>0</td><td>0</td><td>-2</td><td></td><td>0-2</td><td></td><td>0-2</td><td>-0.00106</td><td>0.1</td><td>-0.00192</td><td>0.1</td></tr><tr><td>Mqm</td><td>95,355</td><td>2.18679</td><td>0 4</td><td></td><td>0-2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

# 6.2.2 Treatment of the permanent tide

The degree 2 zonal tide generating potential has a mean (time average) value that is nonzero. This time independent $( n m ) = ( 2 0 )$ potential produces a permanent deformation and a consequent time independent contribution to the geopotential coefficient $C _ { 2 0 }$ . In formulating a geopotential model, two approaches may be taken (see Chapter 1). When the time independent contribution is included in the adopted value of $C _ { 2 0 }$ , then the value is termed “zero tide” and will be noted here $C _ { 2 0 } ^ { z t }$ . If the time independent contribution is not included in the adopted value of $C _ { 2 0 }$ , then the value is termed “conventional tide free” and will be noted here $\hat { C } _ { 2 0 } ^ { t f }$ .

Table 6.5c: Amplitudes $\left( A _ { 2 } \delta k _ { f } H _ { f } \right)$ of the corrections for frequency dependence of $k _ { 2 2 } ^ { ( 0 ) }$ ng the nominal value $k _ { 2 2 }$ for the sectorial tides as . Units: $1 0 ^ { - 1 2 }$ corrections are only to the real part.   

<table><tr><td></td><td>Name Doodsondeg/hrTsh p N&#x27;pse e F D Ωδk</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Amp.</td></tr><tr><td></td><td>No. 245,655</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N2 M</td><td>255,555</td><td>28.439732-10100102020.00006</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>28.98410200000002020.00004</td><td>-0.3 -1.2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

In the case of a “zero tide” geopotential model, the model of tidal effects to be added should not once again contain a time independent part. One must not then use the expression (6.6) as it stands for modeling $\Delta C _ { 2 0 }$ ; its permanent part must first be restored. This is Step 3 of the computation, which provides $\Delta C _ { 2 0 } ^ { z t }$ , to b e used with a “zero tide” geopotential model.

$$
\Delta \bar { C } _ { 2 0 } ^ { z t } = \Delta \bar { C } _ { 2 0 } - \Delta \bar { C } _ { 2 0 } ^ { p e r m }
$$

where $\Delta C _ { 2 0 }$ is given by Equation (6.6) and where $\Delta C _ { 2 0 } ^ { p e r m }$ is the time-independent part:

$$
\Delta \bar { C } _ { 2 0 } ^ { p e r m } = A _ { 0 } H _ { 0 } k _ { 2 0 } = ( 4 . 4 2 2 8 \times { 1 0 } ^ { - 8 } ) ( - 0 . 3 1 4 6 0 ) k _ { 2 0 } .
$$

In the case of EGM2008, the difference between the zero-tide and tide-free value of $C _ { 2 0 }$ is $- 4 . 1 7 3 6 \times 1 0 ^ { - 9 }$ . Assuming the same values for $A _ { 0 }$ , $H _ { 0 }$ and $k _ { 2 0 }$ , the tide-free value of $C _ { 2 0 }$ corresponding to Table 6.2 would be $- 0 . 4 8 4 1 6 5 3 1 \times 1 0 ^ { - 3 }$ .

The use of “zero tide” values and the subsequent removal of the effect of the permanent tide from the tide model is presented for consistency with the 18th IAG General Assembly Resolution 16.

# 6.3 Effect of the ocean tides

The dynamical effects of ocean tides are most easily incorporated as periodic variations in the normalized Stokes’ coefficients of degree n and order m $\Delta C _ { n m }$ and $\Delta S _ { n m }$ . These variations can be evaluated as

$$
[ \Delta \bar { C } _ { n m } - i \Delta \bar { S } _ { n m } ] ( t ) = \sum _ { f } \bar { \sum _ { + } } ( \mathcal { C } _ { f , n m } ^ { \pm } \mp i S _ { f , n m } ^ { \pm } ) e ^ { \pm i \theta _ { f } ( t ) } ,
$$

where C± $\mathcal { C } _ { f , n m } ^ { \pm }$ and $S _ { f , n m } ^ { \pm }$ are the geopotential harmonic amplitudes (see more information below) for the tide constituent $f$ $\theta _ { f } ( t )$ is the argument of the tide constituent $f$ as defined in the explanatory text below Equation (6.8e).

Ocean tide models are typically developed and distributed as gridded maps of tide height amplitudes. These models provide in-phase and quadrature amplitudes of tide heights for selected, main tidal frequencies (or main tidal waves), on a variable grid spacing over the oceans. Using standard methods of spherical harmonic decomposition and with the use of an Earth loading model, the maps of ocean tide height amplitudes have been converted to spherical harmonic coefficients of the geopotential, and provided for direct use in Equation (6.15). This computation follows Equation (6.21) and has been carried out for the tide model proposed in Section 6.3.2.

Typically, an ocean tide model provides maps for only the largest tides or main waves. The spectrum of tidal geopotential perturbations can be completed by interpolation from the main waves to the smaller, secondary waves, using an assumption of linear variation of tidal admittance between closely spaced tidal frequencies. For each secondary wave, the geopotential harmonic amplitudes can be derived from the amplitudes of two nearby main lines, or pivot waves, (labeled with subscripts 1 and 2) as

$$
\begin{array} { r l r } { \mathcal { C } _ { f , n m } ^ { \pm } } & { = } & { \frac { \dot { \theta } _ { f } - \dot { \theta } _ { 1 } } { \dot { \theta } _ { 2 } - \dot { \theta } _ { 1 } } . \frac { H _ { f } } { H _ { 2 } } \mathcal { C } _ { 2 , n m } ^ { \pm } + \frac { \dot { \theta } _ { 2 } - \dot { \theta } _ { f } } { \dot { \theta } _ { 2 } - \dot { \theta } _ { 1 } } . \frac { H _ { f } } { H _ { 1 } } \mathcal { C } _ { 1 , n m } ^ { \pm } } \\ { \mathcal { S } _ { f , n m } ^ { \pm } } & { = } & { \frac { \dot { \theta } _ { f } - \dot { \theta } _ { 1 } } { \dot { \theta } _ { 2 } - \dot { \theta } _ { 1 } } . \frac { H _ { f } } { H _ { 2 } } \mathcal { S } _ { 2 , n m } ^ { \pm } + \frac { \dot { \theta } _ { 2 } - \dot { \theta } _ { f } } { \dot { \theta } _ { 2 } - \dot { \theta } _ { 1 } } . \frac { H _ { f } } { H _ { 1 } } \mathcal { S } _ { 1 , n m } ^ { \pm } } \end{array}
$$

where $H$ is the astronomic amplitude of the considered wave. See an example in Table 6.7 developed for the main waves of FES2004 (see Section 6.3.2).

Some background information on the determination of the coefficients is given in Section 6.3.1, and is included here for completeness. It is not necessary for the evaluation of tidal perturbations to the geopotential. Information on selected tidal models and their use is provided in Section 6.3.2.

# 6.3.1 Background on ocean tide models

Ocean tide models are conventionally expressed in terms of amplitude and phase of waves at certain discrete frequencies.

$$
\xi ( \phi , \lambda , t ) = \sum _ { f } Z _ { f } ( \phi , \lambda ) \cos \left( \theta _ { f } ( t ) - \psi _ { f } ( \phi , \lambda ) \right)
$$

where $Z _ { f }$ is the amplitude of wave $f _ { i }$ , $\psi _ { f }$ is the phase at Greenwich and $\theta _ { f }$ is the Doodson argument, see the explanatory text below Equation (6.8e).

When expanding amplitudes $\smash { \boldsymbol { Z } _ { f } }$ ) and phases $\left( \psi _ { f } \right)$ of the different waves of tides (from cotidal grids) in spherical harmonic functions of $Z _ { f } c o s ( \psi _ { f } )$ and $Z _ { f } s i n ( \psi _ { f } )$ , it yields:

$$
\xi ( \phi , \lambda , t ) = \sum _ { f } \sum _ { n = 1 } ^ { N } \sum _ { m = 0 } ^ { n } \bar { P } _ { n m } ( \sin \phi ) \sum _ { + } ^ { - } \xi _ { f , n m } ^ { \pm } ( \lambda , t )
$$

where

$$
\xi _ { f , n m } ^ { \pm } ( \lambda , t ) = \bar { C } _ { f , n m } ^ { \pm } \cos ( \theta _ { f } + \chi _ { f } \pm m \lambda ) + \bar { S } _ { f , n m } ^ { \pm } \sin ( \theta _ { f } + \chi _ { f } \pm m \lambda )
$$

The couples of coefficients $\left( \bar { C } _ { f , n m } ^ { \pm } , \bar { S } _ { f , n m } ^ { \pm } \right)$ represent prograde and retrograde normalized spherical harmonic coefficients of the main wave $f$ at degree $n$ and order $m$ , and can be alternately expressed in terms of amplitude $\hat { \bar { C } } _ { f , n m } ^ { \pm }$ and phase $\varepsilon _ { f , n m } ^ { \pm }$ such as:

$$
\begin{array} { r c l } { \bar { C } _ { f , n m } ^ { \pm } } & { = } & { \hat { \bar { C } } _ { f , n m } ^ { \pm } \sin ( \varepsilon _ { f , n m } ^ { \pm } ) } \\ { \bar { S } _ { f , n m } ^ { \pm } } & { = } & { \hat { \bar { C } } _ { f , n m } ^ { \pm } \cos ( \varepsilon _ { f , n m } ^ { \pm } ) } \end{array}
$$

The $\chi _ { f }$ values agree with the so-called Shureman convention which is traditionally applied in cotidal maps. They comply with the Doodson-Warburg convention which is defined according to the sign of the harmonic amplitude $H _ { f }$ (see Table 6.6 according to Cartwright and Eden, 1973).

For each wave $f$ , the coefficients $\mathcal { C } _ { f , n m } ^ { \pm }$ and $S _ { f , n m } ^ { \pm }$ to be used in Equation (6.15)

$$
\begin{array} { r l r } { \mathcal { C } _ { f , n m } ^ { \pm } } & { = } & { \frac { 4 \pi G \rho _ { w } } { g _ { e } } \left( \frac { 1 + k _ { n } ^ { \prime } } { 2 n + 1 } \right) \hat { \bar { C } } _ { f , n m } ^ { \pm } \sin ( \varepsilon _ { f , n m } ^ { \pm } + \chi _ { f } ) } \\ { \mathcal { S } _ { f , n m } ^ { \pm } } & { = } & { \frac { 4 \pi G \rho _ { w } } { g _ { e } } \left( \frac { 1 + k _ { n } ^ { \prime } } { 2 n + 1 } \right) \hat { \bar { C } } _ { f , n m } ^ { \pm } \cos ( \varepsilon _ { f , n m } ^ { \pm } + \chi _ { f } ) } \end{array}
$$

Table 6.6: Values of the phase bias $\chi _ { f }$ according to the sign of $H _ { f }$   

<table><tr><td></td><td>Hf&gt;0</td><td>Hf&lt;0</td></tr><tr><td>n1=0, long period wave</td><td></td><td>0</td></tr><tr><td>diurnal wave n1=1,</td><td>T</td><td>元</td></tr><tr><td></td><td></td><td></td></tr><tr><td>n1=2, semi-diurnal wave</td><td></td><td>T</td></tr></table>

where $G$ and $g _ { e }$ are given in Chapter 1, $\rho _ { w }$ is the density of seawater (1025 kg $\mathrm { m } ^ { - 3 }$ ) and where $k _ { n } ^ { \prime }$ is the load deformation coefficient of degree n ( $k _ { 2 } ^ { \prime } = - 0 . 3 0 7 5$ , $k _ { 3 } ^ { \prime } = - 0 . 1 9 5$ , $k _ { 4 } ^ { \prime } = - 0 . 1 3 2$ , $k _ { 5 } ^ { \prime } = - 0 . 1 0 3 2$ , $k _ { 6 } ^ { \prime } = - 0 . 0 8 9 2$ ).

# 6.3.2 Ocean tide models

The practical implementation of ocean tide models in this form begins with identification of the underlying ocean tide height model. Once this model is identified, further needed information can include the specification of maximum degree and order of the expansion, the identification of the pivot waves for interpolation, the special handling (if necessary) of the solar (radiational) tides, or the long-period tidal bands.

For the case of the FES2004 ocean tide model, these details of implementation are provided next.

# FES2004

The FES2004 ocean tide model (Lyard et al., 2006) includes long period waves ( $S _ { a }$ , $S _ { s a }$ , $M _ { m }$ , $M _ { f }$ , $M _ { t m }$ , $M _ { s q m }$ ), diurnal waves $( Q _ { 1 } , { \cal O } _ { 1 } , { \cal P } _ { 1 } , { \cal K } _ { 1 } )$ , semi-diurnal waves and the quarter-diurnal wave $( M _ { 4 } ^ { \mathrm { ~ 5 ~ } } )$ . For direct use in Equation (6.15), the coefficients $\mathcal { C } _ { f , n m } ^ { \pm }$ and $S _ { f , n m } ^ { \pm }$ for the main tidal waves of FES2004 can be found at $< ^ { 6 } >$

The tide height coefficients can be found in the file $< ^ { 7 } >$ , both in the form of the coefficients $\bar { C } _ { f , n m } ^ { \pm }$ and $\bar { S } _ { f , n m } ^ { \pm }$ and in the form of the amplitudes $\hat { \bar { C } } _ { f , n m } ^ { \pm }$ and phases $\varepsilon _ { f , n m } ^ { \pm }$ , as defined in Equations (6.19) and (6.20). They have been computed up to degree and order 100 by quadrature method from quarter-degree cotidal grids. Then ellipsoidal corrections to spherical harmonics were applied (Balmino, 2003) in order to take into account that tidal models are described on the oblate shape of the Earth.

Table 6.7 provides a list of admittance waves which can be taken into account to complement the model. It indicates the pivot waves for linear interpolation following Equation (6.16), where indices 1 and 2 refer to the two pivot waves.

It is to be noticed that radiational waves like $S _ { 1 }$ and $S _ { 2 }$ require special handling, since the common altimetric models (including FES2004) for these tides include the contributions of atmospheric pressure variations on the ocean height (i.e. the radiational tide). As a result, neither $S _ { 1 }$ and $S _ { 2 }$ are used as pivot waves for interpolation in Table 6.7. While an $S _ { 2 }$ wave is available as a part of the FES2004 model, a mean $S _ { 1 }$ wave is given outside FES2004 and available in file $< ^ { 8 } >$ .

The additionally provided mean S1 wave should only be used in case the gravitational influences of mass transport from an ocean circulation model like MOG2D (Carr\`ere and Lyard, 2003) are not also modeled. This is because the S1 signal is generally part of such ocean circulation models provided with an interval of 6 hours.

Moreover, very long period waves like $\Omega _ { 1 }$ (18.6 yr) and $\Omega _ { 2 }$ (9.3 yr) which are not yet correctly observed can be modeled as equilibrium waves. Their amplitudes (and phases) are computed from the astronomical amplitude $H _ { f }$ considering the elastic response of the Earth through the Love numbers:

$$
\hat { \bar { C } } _ { f , 2 0 } = \frac { 1 + k _ { 2 } - h _ { 2 } } { \sqrt { 4 \pi } } | H _ { f } | , \quad \epsilon _ { f , 2 0 } = - \frac { \pi } { 2 }
$$

where $k _ { 2 } ~ = ~ 0 . 2 9 5 2 5$ and $h _ { 2 } ~ = ~ 0 . 6 0 7 8$ are the Love numbers of potential and deformation, respectively.

# Influence of tidal models

For a satellite like Stella (altitude 800 km, inclination $9 8 . 7 ^ { \circ }$ and eccentricity 0.001), for one day of integration, the effects of ocean tides are typically of order several cm and can reach 20 cm. It is estimated that the main waves of the FES2004 model typically represent $8 0 \%$ of the effect (Biancale, 2008).

For Starlette (altitude 800 km, inclination $4 9 . 8 ^ { \circ }$ and eccentricity 0.02) and Lageos1 (altitude 5900 km, inclination $1 0 9 . 8 ^ { \circ }$ and eccentricity 0.005), integration time of 6 and 7 days, respectively, showed a 3-D RMS difference (mostly along-track) of 9 and 7 mm, respectively, for the difference between FES2004 and the older CSR3.0 ocean tide model (Ries, 2010).

Table 6.7: List of astronomical amplitudes $H _ { f }$ (m) for main waves of FES2004 (in bold) and for some secondary waves (with their pivot waves when they have to be linearly interpolated).   

<table><tr><td>Darwin&#x27;s symbol</td><td>Doodson&#x27;s number</td><td>Hf</td><td>Pivot wave 1</td><td>Pivot wave 2</td></tr><tr><td>Ω1</td><td>055.565</td><td>.02793</td><td></td><td></td></tr><tr><td>22</td><td>055.575</td><td>-.00027</td><td></td><td></td></tr><tr><td>Sa</td><td>056.554</td><td>-.00492</td><td></td><td></td></tr><tr><td>Ssa</td><td>057.555</td><td>-.03100</td><td></td><td></td></tr><tr><td>Sta</td><td>058.554</td><td>-.00181</td><td>057.555</td><td>065.455</td></tr><tr><td>Msm</td><td>063.655</td><td>-.00673</td><td>057.555</td><td>065.455</td></tr><tr><td>Mm</td><td>065.445</td><td>.00231</td><td>057.555</td><td>065.455</td></tr><tr><td></td><td>065.455</td><td>-.03518</td><td></td><td></td></tr><tr><td></td><td>065.465</td><td>.00229</td><td>065.455</td><td>075.555</td></tr><tr><td></td><td>065.555</td><td>-.00375</td><td>065.455</td><td>075.555</td></tr><tr><td>Msf</td><td>065.655</td><td>.00188</td><td>065.455</td><td>075.555</td></tr><tr><td></td><td>073.555</td><td>-.00583</td><td>065.455</td><td>075.555</td></tr><tr><td>Mf</td><td>075.355</td><td>-.00288</td><td>065.455</td><td>075.555</td></tr><tr><td></td><td>075.555</td><td>-.06663</td><td></td><td></td></tr><tr><td></td><td>075.565</td><td>-.02762</td><td>075.555</td><td>085.455</td></tr><tr><td>Mstm</td><td>075.575</td><td>-.00258</td><td>075.555</td><td>085.455</td></tr><tr><td></td><td>083.655</td><td>-.00242</td><td>075.555</td><td>085.455</td></tr><tr><td>Mtm</td><td>083.665</td><td>-.00100</td><td>075.555</td><td>085.455</td></tr><tr><td></td><td>085.455</td><td>-.01276</td><td></td><td></td></tr><tr><td>Msqm</td><td>085.465</td><td>-.00529</td><td>085.455</td><td>093.555</td></tr><tr><td></td><td>093.555</td><td>-.00204</td><td></td><td></td></tr><tr><td></td><td>095.355</td><td>-.00169</td><td>085.455</td><td>093.555</td></tr><tr><td></td><td>117.655</td><td>-.00194</td><td>135.455</td><td>145.555</td></tr><tr><td>2Q1</td><td>125.755</td><td>-.00664</td><td>135.655</td><td>145.555</td></tr><tr><td>01</td><td>127.555</td><td>-.00802</td><td>135.655</td><td>145.555</td></tr><tr><td>01</td><td>135.645</td><td>-.00947</td><td>135.655</td><td>145.555</td></tr><tr><td>Q1</td><td>135.655</td><td>-.05020</td><td></td><td></td></tr><tr><td></td><td>137.445</td><td>-.00180</td><td>135.655</td><td>145.555</td></tr><tr><td>p1</td><td>137.455</td><td>-.00954</td><td>135.655</td><td>145.555</td></tr><tr><td>01</td><td>145.545</td><td>-.04946</td><td>135.655</td><td>145.555</td></tr><tr><td></td><td>145.555</td><td>-.26221</td><td></td><td></td></tr><tr><td></td><td>145.755</td><td>.00170</td><td>145.555</td><td>165.555</td></tr><tr><td>T1</td><td>147.555</td><td>.00343</td><td>145.555</td><td>165.555</td></tr><tr><td></td><td>153.655</td><td>.00194</td><td>145.555</td><td>165.555</td></tr><tr><td></td><td>155.455</td><td>.00741</td><td>145.555</td><td>165.555</td></tr></table>

continued

<table><tr><td>Darwin&#x27;s symbol</td><td>Doodson&#x27;s number</td><td>Hf</td><td>Pivot wave 1</td><td>Pivot wave 2</td></tr><tr><td rowspan="3">M1</td><td>155.555</td><td>-.00399</td><td>145.555</td><td>165.555</td></tr><tr><td>155.655</td><td>.02062</td><td>145.555</td><td>165.555</td></tr><tr><td>155.665</td><td>.00414</td><td>145.555</td><td>165.555</td></tr><tr><td>X1</td><td>157.455</td><td>.00394</td><td>145.555</td><td>165.555</td></tr><tr><td>T1</td><td>162.556</td><td>-.00714</td><td>145.555</td><td>165.555</td></tr><tr><td>P1</td><td>163.555</td><td>-.12203</td><td></td><td></td></tr><tr><td>S1</td><td>164.556</td><td>.00289</td><td></td><td></td></tr><tr><td>K1-</td><td>165.545</td><td>-.00730</td><td>145.555</td><td>165.555</td></tr><tr><td>K1</td><td>165.555</td><td>.36878</td><td></td><td></td></tr><tr><td>K1+</td><td>165.565</td><td>.05001</td><td>145.555</td><td>165.555</td></tr><tr><td>1</td><td>166.554</td><td>.00293</td><td>145.555</td><td>165.555</td></tr><tr><td>1</td><td>167.555</td><td>.00525</td><td>145.555</td><td>165.555</td></tr><tr><td>01</td><td>173.655</td><td>.00395</td><td>145.555</td><td>165.555</td></tr><tr><td>J1</td><td>175.455</td><td>.02062</td><td>145.555</td><td>165.555</td></tr><tr><td rowspan="3">S01</td><td>175.465</td><td>.00409</td><td>145.555</td><td>165.555</td></tr><tr><td>183.555</td><td>.00342</td><td>145.555</td><td>165.555</td></tr><tr><td>185.355</td><td>.00169</td><td>145.555</td><td>165.555</td></tr><tr><td>001</td><td>185.555</td><td>.01129</td><td>145.555</td><td>165.555</td></tr><tr><td></td><td>185.565</td><td>.00723</td><td>145.555</td><td>165.555</td></tr><tr><td>V1</td><td>195.455</td><td>.00216</td><td>145.555</td><td>165.555</td></tr><tr><td>3N2</td><td>225.855</td><td>.00180</td><td>235.755</td><td>245.655</td></tr><tr><td>€2</td><td>227.655</td><td>.00467</td><td>235.755</td><td>245.655</td></tr><tr><td>2N2</td><td>235.755</td><td>.01601</td><td></td><td></td></tr><tr><td>μ2</td><td>237.555</td><td>.01932</td><td>235.755</td><td>245.655</td></tr><tr><td></td><td>245.555</td><td>-.00389</td><td>237.755</td><td>245.655</td></tr><tr><td></td><td>245.645</td><td>-.00451</td><td>237.755</td><td>245.655</td></tr><tr><td>N2</td><td>245.655</td><td>.12099</td><td></td><td></td></tr><tr><td>V2</td><td>247.455</td><td>.02298</td><td>245.655</td><td>255.555</td></tr><tr><td>2</td><td>253.755</td><td>-.00190</td><td>245.655</td><td>255.555</td></tr><tr><td>Q2</td><td>254.556</td><td>-.00218</td><td>245.655</td><td>255.555</td></tr><tr><td></td><td>255.545</td><td>-.02358</td><td>245.655</td><td>255.555</td></tr><tr><td>M2</td><td>255.555</td><td>.63192</td><td></td><td></td></tr><tr><td>β</td><td>256.554</td><td>.00192</td><td>255.555</td><td>275.555</td></tr><tr><td>入2</td><td>263.655</td><td>-.00466</td><td>255.555</td><td>275.555</td></tr><tr><td>L2</td><td>265.455</td><td>-.01786</td><td>255.555</td><td>275.555</td></tr><tr><td></td><td>265.555</td><td>.00359</td><td>255.555</td><td>275.555</td></tr><tr><td></td><td>265.655</td><td>.00447</td><td>255.555</td><td>275.555</td></tr><tr><td>T2</td><td>265.665</td><td>.00197</td><td>255.555</td><td>275.555</td></tr><tr><td>S2</td><td>272.556</td><td>.01720</td><td>255.555</td><td>275.555</td></tr><tr><td></td><td>273.555</td><td>.29400</td><td></td><td></td></tr><tr><td>R2</td><td>274.554</td><td>-.00246</td><td>255.555</td><td>275.555</td></tr><tr><td>K2</td><td>275.555</td><td>.07996</td><td></td><td></td></tr><tr><td>K2+</td><td>275.565</td><td>.02383</td><td>255.555</td><td>275.555</td></tr><tr><td>K2++</td><td>275.575</td><td>.00259</td><td>255.555</td><td>275.555</td></tr><tr><td>m2</td><td>285.455</td><td>.00447</td><td>255.555</td><td>275.555</td></tr><tr><td rowspan="2">M4</td><td>285.465</td><td>.00195</td><td>255.555</td><td>275.555</td></tr><tr><td>455.555</td><td></td><td></td><td></td></tr></table>

# 6.4 Solid Earth pole tide

The pole tide is generated by the centrifugal effect of polar motion, characterized by the potential

$$
\begin{array} { r l r } { \Delta V ( r , \theta , \lambda ) } & { = } & { - \frac { \Omega ^ { 2 } r ^ { 2 } } { 2 } \sin 2 \theta \left( m _ { 1 } \cos \lambda + m _ { 2 } \sin \lambda \right) } \\ & { = } & { - \frac { \Omega ^ { 2 } r ^ { 2 } } { 2 } \sin 2 \theta { \bf R e } \left[ \left( m _ { 1 } - i m _ { 2 } \right) e ^ { i \lambda } \right] . } \end{array}
$$

(See Section 7.1.4 for further details, including the relation of the wobble variables $( m _ { 1 } , m _ { 2 } )$ to the polar motion variables $( x _ { p } , y _ { p } )$ .) The deformation which constitutes this tide produces a perturbation

$$
- \frac { \Omega ^ { 2 } r ^ { 2 } } { 2 } \sin { 2 \theta } \mathrm { \bf ~ R e } \left[ k _ { 2 } \left( m _ { 1 } - i m _ { 2 } \right) e ^ { i \lambda } \right]
$$

in the external potential, which is equivalent to changes in the geopotential coefficients $C _ { 2 1 }$ and $S _ { 2 1 }$ . Using for $k _ { 2 }$ the value $0 . 3 0 7 7 + 0 . 0 0 3 6 i$ appropriate to the polar tide yields

$$
\begin{array} { r l r } { \Delta \bar { C } _ { 2 1 } } & { = } & { - 1 . 3 3 3 \times 1 0 ^ { - 9 } ( m _ { 1 } + 0 . 0 1 1 5 m _ { 2 } ) , } \\ & { } & \\ { \Delta \bar { S } _ { 2 1 } } & { = } & { - 1 . 3 3 3 \times 1 0 ^ { - 9 } ( m _ { 2 } - 0 . 0 1 1 5 m _ { 1 } ) , } \end{array}
$$

where $m _ { 1 }$ and $m _ { 2 }$ are in seconds of arc.

# 6.5 Ocean pole tide

The ocean pole tide is generated by the centrifugal effect of polar motion on the oceans. This centrifugal effect is defined in Equation (6.22) from Section 6.4. Polar motion is dominated by the 14-month Chandler wobble and annual variations. At these long periods, the ocean pole tide is expected to have an equilibrium response, where the displaced ocean surface is in equilibrium with the forcing equipotential surface.

Desai (2002) presents a self-consistent equilibrium model of the ocean pole tide. This model accounts for continental boundaries, mass conservation over the oceans, self-gravitation, and loading of the ocean floor. Using this model, the ocean pole tide produces the following perturbations to the normalized geopotential coefficients, as a function of the wobble variables $( m _ { 1 } , m _ { 2 } )$ .

$$
\begin{array} { r } { \left[ \begin{array} { c } { \Delta \bar { C } _ { n m } } \\ { \Delta \bar { S } _ { n m } } \end{array} \right] = R _ { n } \left\{ \left[ \begin{array} { c } { \bar { A } _ { n m } ^ { R } } \\ { \bar { B } _ { n m } ^ { R } } \end{array} \right] \left( m _ { 1 } \gamma _ { 2 } ^ { R } + m _ { 2 } \gamma _ { 2 } ^ { I } \right) + \left[ \begin{array} { c } { \bar { A } _ { n m } ^ { I } } \\ { \bar { B } _ { n m } ^ { I } } \end{array} \right] \left( m _ { 2 } \gamma _ { 2 } ^ { R } - m _ { 1 } \gamma _ { 2 } ^ { I } \right) \right\} } \end{array}
$$

where

$$
R _ { n } = { \frac { \Omega ^ { 2 } a _ { E } ^ { 4 } } { G M } } { \frac { 4 \pi G \rho _ { w } } { g _ { e } } } \left( { \frac { 1 + k _ { n } ^ { \prime } } { 2 n + 1 } } \right)
$$

and

$\Omega$ , $a _ { E }$ , $\it G M$ , $g _ { e }$ , and $G$ are defined in Chapter 1,   
$\rho _ { w } =$ density of sea water $= 1 0 2 5 \ k g m ^ { - 3 }$ ,   
$k _ { n } ^ { \prime } = \mathrm { l o a d }$ deformation coefficients $( k _ { 2 } ^ { \prime } = - 0 . 3 0 7 5 , k _ { 3 } ^ { \prime } = - 0 . 1 9 5 , k _ { 4 } ^ { \prime } = - 0 . 1 3 2 , k _ { 5 } ^ { \prime } =$ $- 0 . 1 0 3 2 , k _ { 6 } ^ { \prime } = - 0 . 0 8 9 2 ,$ ,   
$\gamma = \gamma _ { 2 } ^ { R } + i \gamma _ { 2 } ^ { I } = ( 1 + k _ { 2 } - h _ { 2 } ) = 0 . 6 8 7 0 + i 0 . 0 0 3 6$   
(Values of $k _ { 2 }$ and $h _ { 2 }$ appropriate for the pole tide are as given in Sections 6.4 and 7.1.4),   
$( m _ { 1 } , m _ { 2 } )$ are the wobble parameters in radians. Refer to Section 7.1.4 for the relationship between the wobble variables $( m _ { 1 } , m _ { 2 } )$ and the polar motion variable $( x _ { p } , y _ { p } )$ .efficients from the self-consistent equilibrium model,   
$\bar { A } _ { n m } = \bar { A } _ { n m } ^ { R } + i \bar { A } _ { n m } ^ { I }$ and $\bar { B } _ { n m } = \bar { B } _ { n m } ^ { R } + i \bar { B } _ { n m } ^ { I }$ , are provided to degree and order 360 at $< ^ { 9 } >$ .   
The $( n , m ) = ( 2 , 1 )$ coefficients are the dominant terms of the ocean pole tide. Using the values defined above yields the following $( n , m ) = ( 2 , 1 )$ coefficients for the ocean pole tide:

$$
\begin{array} { r l r } { \Delta \bar { C } _ { 2 1 } } & { = } & { - 2 . 1 7 7 8 \times 1 0 ^ { - 1 0 } ( m _ { 1 } - 0 . 0 1 7 2 4 m _ { 2 } ) , } \\ { \Delta \bar { S } _ { 2 1 } } & { = } & { - 1 . 7 2 3 2 \times 1 0 ^ { - 1 0 } ( m _ { 2 } - 0 . 0 3 3 6 5 m _ { 1 } ) , } \end{array}
$$

where $m _ { 1 }$ and $m _ { 2 }$ are in seconds of arc. Approximately $9 0 \%$ of the variance of the ocean pole tide potential is provided by the degree $n = 2$ spherical harmonic components, with the next largest contributions provided by the degree $n = 1$ and $n = 3$ components, respectively (see Figure 6.1). Expansion to spherical harmonic degree $n = 1 0$ provides approximately $9 9 \%$ of the variance. However, adequate representation of the continental boundaries will require a spherical harmonic expansion to high degree and order. The degree $n = 1$ components are shown in Figure 6.1 to illustrate the size of the ocean pole tide contribution to geocenter motion but these terms should not be used in modeling station displacements.

![](../chunks/IERS Conventions (2010), IERS Technical Note No.36_part_0002_pages_0071-0140/auto/images/0c2147ea87fa366887e8c88432c34bc54c4c9dcc556adfab4d77f887d281fa3f.jpg)  
Figure 6.1: Ocean pole tide: first spherical harmonic components.

# 6.6 Conversion of tidal amplitudes defined according to different conventions

The definition used for the amplitudes of tidal terms in the recent high-accuracy tables differ from each other and from Cartwright and Tayler (1971). Hartmann and Wenzel (1995) tabulate amplitudes in units of the potential $\mathrm { ( m ^ { 2 } s ^ { - 2 } ) }$ , while the amplitudes of Roosbeek (1996), which follow the Doodson (1921) convention, are dimensionless. To convert them to the equivalent tide heights $H _ { f }$ of the Cartwright-Tayler convention, multiply by the appropriate factors from Table 6.5. The following values are used for the constants appearing in the conversion factors: Doodson constant $D _ { 1 } = 2 . 6 3 3 5 8 3 5 2 8 5 5 ~ \mathrm { m } ^ { 2 } ~ \mathrm { s } ^ { - 2 }$ $g _ { e } \ = \ g$ at the equatorial radius = 9.79828685 (from $G M = 3 . 9 8 6 0 0 4 4 1 5 \times 1 0 ^ { 1 4 } ~ \mathrm { m } ^ { 3 } ~ \mathrm { s } ^ { - 2 }$ , $R _ { e } = 6 3 7 8 1 3 6 . 5 5$ m).

Table 6.8: Factors for conversion to Cartwright-Tayler amplitudes from those defined according to Doodson’s and Hartmann and Wenzel’s conventions.   

<table><tr><td>From Doodson</td><td>From Hartmann &amp; Wenzel</td></tr><tr><td>f20=-D=-0.426105 √5ge</td><td>f20=2 = 0.361788 ge</td></tr><tr><td>f21=-2VD=-0.695827 3√5ge</td><td>f21 =1√8π = -0.511646 ge</td></tr><tr><td>f22= √96元D =0.695827</td><td>f22 √8π = 0.511646 》</td></tr><tr><td>3√5ge V20元D1 = -0.805263</td><td>ge f0 2√元 = 0.361788</td></tr><tr><td>f30=1 7ge</td><td>ge √8π</td></tr><tr><td>V720元D =0.603947 f31= 8√7 ge</td><td>f1 = 0.511646 ge</td></tr><tr><td>√1440元D =0.683288 f2= 10√7 ge</td><td>f32 √8π = 0.511646 ge</td></tr><tr><td>V2880元D =-0.644210 f33= 15√7 ge</td><td>f3 √8π = -0.511646 ge</td></tr></table>

# References

Balmino, G., 2003, “Ellipsoidal corrections to spherical harmonics of surface phenomena gravitational effects,,” Special publication in honour of H. Moritz, Technical University of Graz, pp. 21–30.   
Biancale, R., 2008, personal communication.   
Carr\`ere, L. and Lyard, F., 2003, “Modeling the barotropic response of the global ocean to atmospheric wind and pressure forcing - comparison with observations,” Geophys. Res. Lett. 30(6), 1275, doi: 10.1029/2002GL016473.   
Cartwright, D. E. and Tayler, R. J., 1971, “New computations of the tide-generating potential,” Geophys. J. Roy. astr. Soc., 23(1), pp. 45–73., doi: 10.1111/j.1365-246X.1971.tb01803.x.   
Cartwright, D. E. and Edden, A. C., 1973, “Corrected tables of tidal harmonics,” Geophys. J. Roy. astr. Soc., 33(3), pp. 253–264, doi: 10.1111/j.1365- 246X.1973.tb03420.x.   
Casotto, S., 1989, “Nominal ocean tide models for TOPEX precise orbit determination,” Ph.D. dissertation, The Univ. of Texas at Austin.   
Chapman, S. and Lindzen, R., 1970, Atmospheric Tides, D. Reidel, Dordrecht, 200 pp.   
Chao, B. F., Ray, R. D., Gipson, J. M., Egbert, G. D. and Ma, C., 1996, “Diurnal/semidiurnal polar motion excited by oceanic tidal angular momentum,” J. Geophys. Res., 101(B9), pp. 20151–20163, doi: 10.1029/96JB01649.   
Cheng, M.K., Shum, C.K., Tapley, B.D., 1997, “Determination of long-term changes in the Earth’s gravity field from satellite laser ranging observations,” J. Geophys. Res., 102(B10), pp. 22377–22390, doi:10.1029/97JB01740.   
Cheng, M. K., Ries, J. C., and Tapley, B. D., 2010, “Variations of the Earth’s figure axis from satellite laser ranging and GRACE,” J. Geophys. Res., submitted.   
Desai, S. D. and Wahr, J. M., 1995, “Empirical ocean tide models estimated from Topex/Poseidon altimetry,” J. Geophys. Res., 100(C12), pp. 25205–25228.   
Desai, S. D., 2002, “Observing the pole tide with satellite altimetry,” J. Geophys. Res., 107(C11), 3186, doi:10.1029/ 2001JC001224.   
Doodson, A. T., 1921, “The Harmonic development of the tide-generating potential,” Proc. R. Soc. A., 100, pp. 305–329.   
Dziewonski, A. and Anderson, D. L., 1981, “Preliminary reference earth model,” Phys. Earth Planet. In., 25, pp. 297–356.   
Eanes, R. J., Schutz, B., and Tapley, B., 1983, “Earth and ocean tide effects on Lageos and Starlette,” in Proc. of the Ninth International Symposium on Earth Tides, Kuo, J. T. (ed.), E. Sckweizerbart’sche Verlagabuchhandlung, Stuttgart.   
Eanes R. J. and Bettadpur, S., 1995, “The CSR 3.0 global ocean tide model,” Technical Memorandum CSR-TM-95-06, Center for Space Research, University of Texas, Austin, TX.   
Flechtner, F., 2007, “AOD1B Product Description Document,” GRACE project document 327-750, Rev. 3.1.   
Hartmann, T. and Wenzel, H.-G., 1995, “The HW95 tidal potential catalogue,” Geophys. Res. Lett., 22(24), pp. 3553–3556, doi:10.1029/95GL03324.   
Lyard, F., Lefevre, F., Letellier, T., Francis, O., 2006, “Modelling the global ocean tides: modern insights from FES2004,” Ocean Dyn., 56(5-6), pp. 394–415, doi: 10.1007/s10236-006-0086-x.   
Mathews, P. M., Buffett, B. A., and Shapiro,. I. I., 1995, “Love numbers for diurnal tides: Relation to wobble admittances and resonance expansions,” J. Geophys. Res., 100(B9), pp. 9935–9948, doi:10.1029/95JB00670.

Mathews, P. M., Herring, T. A., and Buffett, B. A., 2002, “Modeling of nutationprecession: New nutation series for nonrigid Earth, and insights into the Earth’s interior,” J. Geophys. Res., 107(B4), doi: 10.1029/2001JB000390.

Mayer-G¨urr, T., “ITG-Grace03s: The latest GRACE gravity field solution computed in Bonn,” Joint International GSTM and DFG SPP Symposium Potsdam, 15-17 October 2007, see http://www.igg.uni-bonn.de/apmg/fileadmin/DatenModelle/media/ mayer-guerr gstm potsdam 2007.pdf.

Nerem, R. S., Chao, B. F., Au, A. Y., Chan, J. C., Klosko, S. M., Pavlis, N. K. and Williamson, R. G., 1993, “Temporal variations of the Earth’s gravitational field from satellite laser ranging to Lageos,” Geophys. Res. Lett., 20(7), pp. 595–598, doi: 10.1029/93GL00169.

Pavlis, N. K., Holmes, S. A., Kenyon, S. C., and Factor, J. K., 2008, “An Earth gravitational model to degree 2160: EGM2008,” presented at the 2008 General Assembly of the European Geosciences Union, Vienna, Austria, April 13-18, 2008, see http://earth-info.nga.mil/GandG/wgs84/gravitymod/egm2008/ NPavlis&al EGU2008.ppt.

Ray, R. D. and Cartwright, D. E., 1994, “Satellite altimeter observations of the $M _ { f }$ and $M _ { m }$ ocean tides, with simultaneous orbit corrections,” Gravimetry and Space Techniques Applied to Geodynamics and Ocean Dynamics, Geophysical Monograph 82, IUGG Volume 17, pp. 69–78.

Ries, J.C., 2010, personal communication.

Roosbeek, F., 1996, “RATGP95: a harmonic development of the tide-generating potential using an analytical method,” Geophys. J. Int., 126(1), pp. 197– 204, doi: 10.1111/j.1365-246X.1996.tb05278.x.

Schwiderski, E., 1983, “Atlas of ocean tidal charts and maps, Part I: The semidiurnal principal lunar tide M2,” Mar. Geod., 6(3-4), pp. 219–265, doi: 10.1080/15210608309379461.

Souchay, J. and Folgueira, M., 1998, “The effect of zonal tides on the dynamical ellipticity of the Earth and its influence on the nutation,” Earth, Moon and Planets, 81(3), pp. 201–216, doi: 10.1023/A:1006331511290.

Wahr, J. M., 1981, “The forced nutations of an elliptical, rotating, elastic, and oceanless Earth,” Geophys. J. Roy. Astron. Soc., 64(3), pp. 705–727, doi: 10.1111/j.1365-246X.1981.tb02691.x.

Wahr, J., 1987, “The Earth’s C $^ { 2 1 }$ and S $^ { 2 1 }$ gravity coefficients and the rotation of the core,” Geophys. J. Roy. astr. Soc., 88, pp. 265–276.

Wahr, J. M. and Sasao, T., 1981, “A diurnal resonance in the ocean tide and the Earth’s load response due to the resonant free “core nutation”,” Geophys. J. Roy. astr. Soc., 64, pp. 747–765.

Wahr, J., 1990, “Corrections and update to ‘The Earth’s C21 and S21 gravity coefficients and the rotation of the core’,” Geophys. J. Int., 101, pp. 709– 711.

Wahr, J. and Bergen, Z., 1986, “The effects of mantle elasticity on nutations, Earth tides, and tidal variations in the rotation rate,” Geophys. J. Roy. astr. Soc., 87, 633–668.

Widmer, R., Masters, G., and Gilbert, F., 1991, “Spherically symmetric attenuation within the Earth from normal mode data,” Geophys. J. Int., 104, pp. 541–553.

# 7 Displacement of reference points

Models describing the displacements of reference points due to various effects are provided. In the following, three kinds of displacements are distinguished:

• Conventional displacements of reference markers on the crust (see Section 7.1) relate the regularized positions $X _ { R } ( t )$ of the reference points (see Chapter 4) to their conventional instantaneous positions. Generally these conventional instantaneous positions are used in data analyses as a priori coordinates for subsequent adjustment of observational data. They include tidal motions (mostly near diurnal and semidiurnal frequencies) and other accurately modeled displacements of reference markers (mostly at longer periods); • Other displacements of reference markers (Section 7.2, presently, at the time of publication, under development) include non-tidal motions associated with changing environmental loads (very broad spectral content); • Displacements that affect the internal reference points within the observing instruments, which are generally technique-dependent, are mentioned in Section 7.3.

The first two categories of displacements are described by geophysical models or gridded convolution results derived from geophysical models. The last category includes empirical physical effects that have been demonstrated to affect geodetic observing instruments.

As the non-tidal load displacements (Section 7.2) normally change very little over typical integration spans and because models for these effects are usually less accurate, it is generally recommended that they not be included in computing conventional instantaneous positions. Instead, the corresponding non-tidal loading effects will remain as signals embedded in the geodetic time series results. These signals can be extracted and compared with the model results referenced here in post-analysis studies.

In combinations of diverse analysis results, it is particularly important that equivalent displacement models are applied for like effects. Non-tidal load displacements should be consistently excluded from the conventional instantaneous positions, as recommended here, or else the same geophysical loading models together with the same environmental inputs should be applied.

# 7.1 Models for conventional displacement of reference markers on the crust

This section describes conventional models for displacement due to the body tides arising from the direct effect of the external tide generating potential (7.1.1), displacement due to ocean tidal loading (7.1.2) and due to diurnal and semidiurnal atmospheric pressure loading (7.1.3), displacement due to the centrifugal perturbations caused by Earth rotation variations, including the pole tide (7.1.4) and the loading caused by the ocean pole tide (7.1.5).

# 7.1.1 Effects of the solid Earth tides

# 7.1.1.1 Conventional model for solid Earth tides

Site displacements caused by tides of spherical harmonic degree and order (nm) are characterized by the Love number $h _ { n m }$ and the Shida number $\boldsymbol { l } _ { n m }$ . The effective values of these numbers depend on station latitude and tidal frequency (Wahr, 1981). The latitude dependence and a small interband variation are caused by the Earth’s ellipticity and the Coriolis force due to Earth rotation. A strong frequency dependence within the diurnal band is produced by the Nearly Diurnal Free Wobble resonance associated with the FCN in the wobbles of the Earth and its core regions which contribute to the tidal deformations via their centrifugal effects. Additionally, the resonance in the deformation due to ocean tidal loading, which is not included in the computations of the last section which use constant load Love numbers, may be represented in terms of effective contributions to $h _ { 2 1 }$ and $l _ { 2 1 }$ . A further frequency dependence, which is most pronounced in the long-period tidal band, arises from mantle anelasticity leading to corrections to the elastic Earth Love numbers. The contributions to the Love number parameters from anelasticity and ocean tidal loading as well as those from the centrifugal perturbations due to the wobbles have imaginary parts which cause the tidal displacements to lag slightly behind the tide generating potential. All these effects need to be taken into account when an accuracy of 1 mm is desired in determining station positions.

In order to account for the latitude dependence of the effective Love and Shida numbers, the representation in terms of multiple $h$ and $\mathbf { \xi } _ { l }$ parameters employed by Mathews et al. (1995) is used. In this representation, parameters ${ h ^ { ( 0 ) } }$ and ${ l ^ { ( 0 ) } }$ play the roles of $h _ { 2 m }$ and $l _ { 2 m }$ , while the latitude dependence is expressed in terms of additional parameters ${ h ^ { ( 2 ) } , h ^ { \prime } }$ and $l ^ { ( 1 ) } , l ^ { ( 2 ) } , l ^ { \prime }$ . These parameters are defined through their contributions to the site displacement as given by equations (7.1a-7.1c) below. Their numerical values as listed in the Conventions 1996 have since been revised, and the new values presented in Table 7.2 are used here. These values pertain to the elastic Earth and anelasticity models referred to in Chapter 6.

The vector displacement $\Delta \vec { r _ { f } }$ due to a tidal term of frequency $f$ is given by the following expressions that result from evaluation of the defining equation (7.2) of Mathews et al. (1995):

For a long-period tide of frequency $f$ :

$$
\begin{array} { r l r } { \Delta \vec { r } _ { f } } & { = } & { \sqrt { \frac { 5 } { 4 \pi } } H _ { f } \quad \Bigg \{ \quad \Big [ h ( \phi ) \left( \frac { 3 } { 2 } \sin ^ { 2 } \phi - \frac { 1 } { 2 } \right) + \sqrt { \frac { 4 \pi } { 5 } } h ^ { \prime } \Big ] \cos \theta _ { f } \ \hat { r } } \\ & { } & { + 3 l ( \phi ) \sin \phi \cos \phi \cos \theta _ { f } \ \hat { n } } \\ & { } & { + \cos \phi \left[ 3 l ^ { ( 1 ) } \sin ^ { 2 } \phi - \sqrt { \frac { 4 \pi } { 5 } } l ^ { \prime } \right] \sin \theta _ { f } \ \hat { e } \Bigg \} . } \end{array}
$$

For a diurnal tide of frequency $f$ :

$$
\begin{array} { r c l } { \Delta \vec { r } _ { f } } & { = } & { - \sqrt { \frac { 5 } { 2 4 \pi } } H _ { f } \quad \Bigg \{ \quad h ( \phi ) 3 \sin \phi \cos \phi \sin ( \theta _ { f } + \lambda ) \hat { r } } \\ & & { + \left[ 3 l ( \phi ) \cos 2 \phi - 3 l ^ { ( 1 ) } \sin ^ { 2 } \phi + \sqrt { \frac { 2 4 \pi } { 5 } } l ^ { \prime } \right] \sin ( \theta _ { f } + \lambda ) \hat { n } } \\ & & { + \left[ \left( 3 l ( \phi ) - \sqrt { \frac { 2 4 \pi } { 5 } } l ^ { \prime } \right) \sin \phi - 3 l ^ { ( 1 ) } \sin \phi \cos 2 \phi \right] \cos ( \theta _ { f } + \lambda ) \hat { e } \Bigg \} . } \end{array}
$$

For a semidiurnal tide of frequency $f$ :

$$
\begin{array} { r c l } { { \Delta \vec { r } _ { f } } } & { { = } } & { { \sqrt { \frac { 5 } { 9 6 \pi } } H _ { f } \quad \Bigg \{ \quad h ( \phi ) 3 \cos ^ { 2 } \phi \cos ( \theta _ { f } + 2 \lambda ) \hat { r } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - 6 \sin \phi \cos \phi \left[ l ( \phi ) + l ^ { ( 1 ) } \right] \cos ( \theta _ { f } + 2 \lambda ) \hat { n } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - 6 \cos \phi \left[ l ( \phi ) + l ^ { ( 1 ) } \sin ^ { 2 } \phi \right] \sin ( \theta _ { f } + 2 \lambda ) \hat { e } \Bigg \} . } } \end{array}
$$

In the above expressions,

$$
\begin{array} { l } { { h ( \phi ) = h ^ { ( 0 ) } + h ^ { ( 2 ) } ( 3 \sin ^ { 2 } \phi - 1 ) / 2 , } } \\ { { \ l ( \phi ) = l ^ { ( 0 ) } + l ^ { ( 2 ) } ( 3 \sin ^ { 2 } \phi - 1 ) / 2 , } } \end{array}
$$

$$
\begin{array} { r c l } { H _ { f } } & { = } & { \mathrm { ~ a m p l i t u d e ~ ( ~ m ) ~ o f ~ t h e ~ t i d a l ~ t e r m ~ o f ~ f r e q u e n c y ~ } f , } \\ { \phi } & { = } & { \mathrm { ~ g e o c t u r t i c ~ i n d i t u d e ~ o f ~ s t a t i o n } , } \\ { \lambda } & { = } & { \mathrm { ~ e a s t ~ l o n g i t u d e ~ o f ~ s t a t i o n } , } \\ { \theta _ { f } } & { = } & { \mathrm { ~ t i d e ~ a r g u m e n t ~ f o r ~ t i d a l ~ c o n s i t i u e n t ~ w i t h ~ f r e q u e n c y ~ } f , } \\ { \hat { r } } & { = } & { \mathrm { ~ u n i t ~ v e c t o r ~ i n ~ r a d i a l ~ d i r e c t i o n } , } \\ { \hat { \theta } } & { = } & { \mathrm { ~ u n i t ~ v e c t o r ~ i n ~ e a s t ~ d i r e c t i o n } , } \\ { \hat { \pi } } & { = } & { \mathrm { ~ u n i t ~ v e c t o r ~ n e a s t ~ d i r e c t i o n } . } \end{array}
$$

The convention used in defining the tidal amplitude $H _ { f }$ is the one from Cartwright and Tayler (1971). To convert amplitudes defined according to other conventions that have been employed in recent more accurate tables, use the conversion factors given in Chapter 6, Table 6.8.

Equations (7.1) assume that the Love and Shida number parameters are all real. Generalization to the case of complex parameters is done simply by making the following replacements for the combinations $L \cos ( \theta _ { f } + m \lambda )$ and $L \sin ( \theta _ { f } + m \lambda )$ , wherever they occur in those equations:

$$
\begin{array} { r l } & { L \cos ( \theta _ { f } + m \lambda )  L ^ { R } \cos ( \theta _ { f } + m \lambda ) - L ^ { I } \sin ( \theta _ { f } + m \lambda ) , } \\ & { } \\ & { L \sin ( \theta _ { f } + m \lambda )  L ^ { R } \sin ( \theta _ { f } + m \lambda ) + L ^ { I } \cos ( \theta _ { f } + m \lambda ) , } \end{array}
$$

where $L$ is a generic symbol for $h ^ { ( 0 ) } , h ^ { ( 2 ) } , h ^ { \prime } , l ^ { ( 0 ) } , l ^ { ( 1 ) } , l ^ { ( 2 ) }$ , and $l ^ { \prime }$ , and where $L ^ { R }$ and $L ^ { I }$ stand for their respective real and imaginary parts.

The complex values of these 7 parameters are computed for the diurnal body tides from resonance formulae of the form given in Equation (6.9) of Chapter 6 using the values listed in Equation (6.10) of that chapter for the resonance frequencies $\sigma _ { \alpha }$ and those listed in Table 7.1 for the coefficients $L _ { 0 }$ and $L _ { \alpha }$ relating to each of the multiple $h$ and $l$ Love/Shida numbers. The manner in which $\sigma _ { \alpha }$ and $L _ { \alpha }$ were computed is explained in Chapter 6, where mention is also made of the models used for the elastic Earth and for mantle anelasticity. As was noted in that chapter, the frequency dependence of the ocean tide contributions to certain Earth parameters in the equations of motion for the wobbles has the effect of making the resonance formulae included in the tabulated values of inexact. The difference between the exact and resonance formula values is $h _ { 2 1 } ^ { ( 0 ) }$ and $l _ { 2 1 } ^ { ( 0 ) }$ in Table 7.2. (The only case where this difference makes a contribution above the cut-off in Table 7.3a is in the radial displacement due to the $\psi _ { 1 }$ tide.) Also included in the values listed in Table 7.2 are the resonant ocean tidal loading corrections outlined in the next paragraph.

Site displacements caused by solid Earth deformations due to ocean tidal loading have been dealt with in the first section of this chapter. Constant nominal values were assumed for the load Love numbers in computing these. The values used for tides of degree 2 were $h _ { 2 } ^ { \prime ( n o m ) } = - 1 . 0 0 1$ , $l _ { 2 } ^ { \prime } { } ^ { ( n o m ) } = 0 . 0 2 9 5$ $k _ { 2 } ^ { \prime ( n o m ) } = - 0 . 3 0 7 5$ . Since resonances in the diurnal band also cause the values of the load Love numbers to vary, corrections need to be applied to the results of the first section. These corrections can be expressed in terms of effective ocean tide contributions δh(OT ) and $\delta l ^ { ( O T ) }$ to the respective body tide Love numbers $h _ { 2 1 } ^ { ( 0 ) }$ and $l _ { 2 1 } ^ { ( 0 ) }$ . $\delta h ^ { ( O T ) }$ and $\delta l ^ { ( O T ) }$ are given by expressions of the form (6.11) of Chapter 6, with appropriate replacements. They were computed using the same ocean tide admittances as in that chapter, and using the resonance parameters listed in Table 6.4 for the load Love numbers; they are included in the values listed in Table 7.2 under ${ h ^ { ( 0 ) R } }$ and $h ^ { ( 0 ) I }$ for the diurnal tides.

Table 7.1: Parameters in the resonance formulae for the displacement Love numbers.   

<table><tr><td colspan="5">h(0)</td></tr><tr><td>α</td><td>ReLα</td><td>Im Lα</td><td>h(2) ReLα</td><td>Im Lα</td></tr><tr><td>0</td><td>.60671 × 10+0</td><td>-.2420 × 10-2</td><td>-.615 × 10-3</td><td>-.122 × 10-4</td></tr><tr><td>1</td><td>-.15777 × 10-2</td><td>-.7630 × 10-4</td><td>.160 ×10-5</td><td>.116 × 10-6</td></tr><tr><td>2</td><td>.18053 × 10-3</td><td>-.6292 × 10-5</td><td>.201 × 10-6</td><td>.279 ×10-8</td></tr><tr><td>3</td><td>-.18616 × 10-5</td><td>.1379 × 10-6</td><td>-.329 × 10-7</td><td>-.217 × 10-8</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>1（0）</td><td></td><td>1(1)</td><td></td></tr><tr><td>α</td><td>ReLα</td><td>Im Lα</td><td>ReLα</td><td>Im Lα</td></tr><tr><td>0</td><td>.84963 × 10-1</td><td>-.7395 × 10-3</td><td>.121 ×10-2</td><td>.136 ×10-6</td></tr><tr><td>1</td><td>-.22107 × 10-3</td><td>-.9646 × 10-5</td><td>-.316 × 10-5</td><td>-.166 × 10-6</td></tr><tr><td>2</td><td>-.54710 × 10-5</td><td>-.2990 × 10-6</td><td>.272 × 10-6</td><td>-.858 ×10-8</td></tr><tr><td>3</td><td>-.29904 × 10-7</td><td>-.7717 × 10-8</td><td>-.545 × 10-8</td><td>.827 × 10-11</td></tr><tr><td></td><td>1(2)</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>1&#x27;</td><td></td></tr><tr><td>α 0</td><td>ReLα .19334× 10-3</td><td>Im Lα</td><td>ReLα</td><td>Im Lα</td></tr><tr><td></td><td></td><td>-.3819 × 10-5</td><td>-.221 × 10-3</td><td>-.474 × 10-7</td></tr><tr><td>1</td><td>-.50331 × 10-6</td><td>-.1639 × 10-7</td><td>.576 ×10-6</td><td>.303 ×10-7</td></tr><tr><td>2</td><td>-.66460 × 10-8</td><td>.5076 × 10-9</td><td>.128× 10-6</td><td>-.378 × 10-8</td></tr><tr><td>3</td><td>.10372 × 10-7</td><td>.7511 × 10-9</td><td>-.655 ×10-8</td><td>-.291 × 10-9</td></tr></table>

The variation of $h _ { 2 0 } ^ { ( 0 ) }$ and $l _ { 2 0 } ^ { ( 0 ) }$ across the zonal tidal band, ( $n m = 2 0$ ), due to mantle anelasticity, is described by the formulae

$$
\begin{array} { r } { h _ { 2 0 } ^ { ( 0 ) } = 0 . 5 9 9 8 - 9 . 9 6 \times 1 0 ^ { - 4 } \left\{ \cot \frac { \alpha \pi } { 2 } \left[ 1 - \left( \frac { f _ { m } } { f } \right) ^ { \alpha } \right] + i \left( \frac { f _ { m } } { f } \right) ^ { \alpha } \right\} , } \\ { l _ { 2 0 } ^ { ( 0 ) } = 0 . 0 8 3 1 - 3 . 0 1 \times 1 0 ^ { - 4 } \left\{ \cot \frac { \alpha \pi } { 2 } \left[ 1 - \left( \frac { f _ { m } } { f } \right) ^ { \alpha } \right] + i \left( \frac { f _ { m } } { f } \right) ^ { \alpha } \right\} } \end{array}
$$

on the basis of the anelasticity model already referred to. Here $f$ is the frequency of the zonal tidal constituent, $f _ { m }$ is the reference frequency equivalent to a period of 200 s, and $\alpha = 0 . 1 5$ .

Table 7.2 lists the values of $h ^ { ( 0 ) } , h ^ { ( 2 ) } , h ^ { \prime } , l ^ { ( 0 ) } , l ^ { ( 1 ) } , l ^ { ( 2 ) }$ , and ${ \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } l ^ { \prime }$ for those tidal frequencies for which they are needed for use in the computational procedure described below. The tidal frequencies shown in the table are given in cycles per sidereal day (cpsd). Periods, in solar days, of the nutations associated with the diurnal tides are also shown.

Computation of the variations of station coordinates due to solid Earth tides, like that of geopotential variations, is done most efficiently by the use of a two-step procedure. The evaluations in the first step use the expression in the time domain for the full degree 2 tidal potential or for the parts that pertain to particular bands ( $m = 0 , 1$ , or 2). Nominal values common to all the tidal constituents involved in the potential and to all stations are used for the Love and Shida numbers $h _ { 2 m }$ and $l _ { 2 m }$ in this step. They are chosen with reference to the values in Table 7.2 so as to minimize the computational effort needed in Step 2. Along with expressions for the dominant contributions from $h ^ { ( 0 ) }$ and ${ l ^ { ( 0 ) } }$ to the tidal displacements, relatively small contributions from some of the other parameters are included in Step 1 for reasons of computational efficiency. The displacements caused by the degree 3 tides are also computed in the first step, using constant values for $h _ { 3 }$ and $l _ { 3 }$ .

Corrections to the results of the first step are needed to take account of the frequency-dependent deviations of the Love and Shida numbers from their respective nominal values, and also to compute the out-of-phase contributions from the zonal tides. Computations of these corrections constitute Step 2. The total displacement due to the tidal potential is the sum of the displacements computed in Steps 1 and 2.

The full scheme of computations is outlined in the chart on page 103.

CORRECTIONS FOR THE STATION TIDAL DISPLACEMENTS   
Step 1: Corrections to be computed in the time domain   

<table><tr><td rowspan="3">in-phase</td><td>for degree 2 and 3</td><td>Nominal values</td></tr><tr><td>.for degree 2 → eq (7.5)</td><td>h2→h()=h(0）+h(2)[(3sin²Φ-1)/2] l2→l(Φ）=t0）+(2）[(3sin²Φ-1）/2]</td></tr><tr><td></td><td>h(0)=0.6078,h(2) = -0.0006; t(0)=0.0847,t(2) = 0.0002</td></tr><tr><td rowspan="3">out-of-phasef</td><td>.for degree 3 → eq (7.6)</td><td>h3 = 0.292 and l3 = 0.015</td></tr><tr><td>for degree 2 only</td><td>Nominal values</td></tr><tr><td>.diurnal tides → eq (7.10) .semidiurnal tides → eq (7.11)</td><td>h= -0.0025 and 𝑙 = -0.0007 h = -0.0022 and 𝑙 = -0.0007</td></tr><tr><td rowspan="3">contribution</td><td></td><td></td></tr><tr><td>from latitude dependence .diurnal tides → eq (7.8)</td><td>Nominal values (1）= 0.0012</td></tr><tr><td>.semidiurnal tides → eq (7.9)</td><td>(1）= 0.0024</td></tr></table>

<table><tr><td colspan="3">Step 2: Corrections to be computed in the frequency domain and to be added to the results of Step 1</td></tr><tr><td rowspan="3"> in-phase</td><td>for degree 2</td><td></td></tr><tr><td>.diurnal tides→ eqs (7.12)</td><td>→ Sum over all the components of Table 7.3a</td></tr><tr><td>.semidiurnal tides</td><td>→negligible</td></tr><tr><td rowspan="2"> in-phase</td><td>and out-of-phase for degree 2</td><td></td></tr><tr><td>. long-period tides→ eqs (7.13)</td><td>→ Sum over all the components of Table 7.3b</td></tr></table>

# Displacement due to degree 2 tides, with nominal values for $h _ { 2 m } ^ { ( 0 ) }$ 1

The first stage of the Step 1 calculations employs real nominal values $h _ { 2 }$ and $l _ { 2 }$ common to all the degree 2 tides for the Love and Shida numbers. It is found to be computationally most economical to choose these to be the values for the semidiurnal tides (which have very little intra-band variation). On using the nominal values, the displacement vector of the station due to the degree 2 tides is given by

$$
\Delta \Vec { r } = \sum _ { j = 2 } ^ { 3 } \frac { G M _ { j } R _ { e } ^ { 4 } } { G M _ { \oplus } R _ { j } ^ { 3 } } \Bigg \{ h _ { 2 } ~ \hat { r } \left( \frac { 3 ( \hat { R } _ { j } \cdot \hat { r } ) ^ { 2 } - 1 } { 2 } \right) + 3 l _ { 2 } ( \hat { R } _ { j } \cdot \hat { r } ) \left[ \hat { R } _ { j } - \left( \hat { R } _ { j } \cdot \hat { r } \right) \hat { r } \right] \Bigg \} ,
$$

where $h _ { 2 2 } ^ { ( 0 ) }$ and $l _ { 2 2 } ^ { ( 0 ) }$ of the semidiurnal tides are chosen as the nominal values $h _ { 2 }$ and $l _ { 2 }$ . The out-of-phase displacements due to the imaginary parts of the Love numbers are dealt with separately below. In Equation (7.5),

Table 7.2: Displacement Love number parameters for degree 2 tides. Superscripts $R$ and $I$ identify the real and imaginary parts, respectively. Periods are given in solar days and frequencies in cpsd.   

<table><tr><td>Name</td><td>Period</td><td>Frequency</td><td>h(0）R</td><td>（0）1</td><td>h(2）</td><td>h&#x27;</td></tr><tr><td>Semidiurnal</td><td></td><td>-2</td><td>.6078</td><td>-.0022</td><td>-.0006</td><td></td></tr><tr><td>Diurnal</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2Q1</td><td>6.86</td><td>0.85461</td><td>.6039</td><td>-.0027</td><td>-.0006</td><td></td></tr><tr><td>01</td><td>7.10</td><td>0.85946</td><td>.6039</td><td>-.0026</td><td>-.0006</td><td></td></tr><tr><td>135,645</td><td>9.12</td><td>0.89066</td><td>.6036</td><td>-.0026</td><td>-.0006</td><td></td></tr><tr><td>Q1</td><td>9.13</td><td>0.89080</td><td>.6036</td><td>-.0026</td><td>-.0006</td><td></td></tr><tr><td>p1</td><td>9.56</td><td>0.89565</td><td>.6035</td><td>-.0026</td><td>-.0006</td><td></td></tr><tr><td>145,545</td><td>13.63</td><td>0.92685</td><td>.6028</td><td>-.0025</td><td>-.0006</td><td></td></tr><tr><td>01</td><td>13.66</td><td>0.92700</td><td>.6028</td><td>-.0025</td><td>-.0006</td><td></td></tr><tr><td>T1</td><td>14.77</td><td>0.93246</td><td>.6026</td><td>-.0025</td><td>-.0006</td><td></td></tr><tr><td>NT1</td><td>23.94</td><td>0.95835</td><td>.6011</td><td>-.0024</td><td>-.0006</td><td></td></tr><tr><td>N01</td><td>27.55</td><td>0.96381</td><td>.6005</td><td>-.0023</td><td>-.0006</td><td></td></tr><tr><td>X1</td><td>31.81</td><td>0.96865</td><td>.5998</td><td>-.0023</td><td>-.0006</td><td></td></tr><tr><td>T1</td><td>121.75</td><td>0.99181</td><td>.5878</td><td>-.0015</td><td>-.0006</td><td></td></tr><tr><td>P1</td><td>182.62</td><td>0.99454</td><td>.5817</td><td>-.0011</td><td>-.0006</td><td></td></tr><tr><td>S1</td><td>365.26</td><td>0.99727</td><td>.5692</td><td>-.0004</td><td>-.0006</td><td></td></tr><tr><td>165,545</td><td>6798.38</td><td>0.99985</td><td>.5283</td><td>.0023</td><td>-.0007</td><td></td></tr><tr><td>K1</td><td>infinity</td><td>1.00000</td><td>.5236</td><td>.0030</td><td>-.0007</td><td></td></tr><tr><td>165,565</td><td>-6798.38</td><td>1.00015</td><td>.5182</td><td>.0036</td><td>-.0007</td><td></td></tr><tr><td>165,575</td><td>-3399.19</td><td>1.00029</td><td>.5120</td><td>.0043</td><td>-.0007</td><td></td></tr><tr><td>1</td><td>-365.26</td><td>1.00273</td><td>1.0569</td><td>.0036</td><td>-.0001</td><td></td></tr><tr><td>166,564</td><td>-346.64</td><td>1.00288</td><td>.9387</td><td>-.0050</td><td>-.0003</td><td></td></tr><tr><td>1</td><td>-182.62</td><td>1.00546</td><td>.6645</td><td>-.0059</td><td>-.0006</td><td></td></tr><tr><td>01</td><td>-31.81</td><td>1.03135</td><td>.6117</td><td>-.0030</td><td>-.0006</td><td></td></tr><tr><td>J1</td><td>-27.55</td><td>1.03619</td><td>.6108</td><td>-.0030</td><td>-.0006</td><td></td></tr><tr><td>001</td><td>-13.66</td><td>1.07300</td><td>.6080</td><td>-.0028</td><td>-.0006</td><td></td></tr><tr><td>Long period</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>55,565</td><td>6798.38</td><td>.000147</td><td>.6344</td><td>-.0093</td><td>-.0006</td><td>.0001</td></tr><tr><td>Ssa</td><td>182.62</td><td>.005461</td><td>.6182</td><td>-.0054</td><td>-.0006</td><td>.0001</td></tr><tr><td>Mm</td><td>27.55</td><td>.036193</td><td>.6126</td><td>-.0041</td><td>-.0006</td><td>.0001</td></tr><tr><td>Mf</td><td>13.66</td><td>.073002</td><td>.6109</td><td>-.0037</td><td>-.0006</td><td>.0001</td></tr><tr><td>75,565</td><td>13.63</td><td>.073149</td><td>.6109</td><td>-.0037</td><td>-.0006</td><td>.0001</td></tr><tr><td>Name</td><td>Period</td><td>Frequency</td><td>(0)R</td><td>10）1</td><td>1(1)</td><td>1(2) 1</td></tr><tr><td>Semidiurnal</td><td></td><td>-2</td><td>.0847</td><td>-.0007</td><td>.0024 .0002</td><td></td></tr><tr><td>Diurnal</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Q1</td><td>9.13</td><td>0.89080</td><td>.0846</td><td>-.0006</td><td>.0012 .0002</td><td>-.0002</td></tr><tr><td>145,545</td><td>13.63</td><td>0.92685</td><td>.0846</td><td>-.0006 .0012</td><td>.0002</td><td>-.0002</td></tr><tr><td>O1</td><td>13.66</td><td>0.92700</td><td>.0846</td><td>-.0006 .0012</td><td>.0002</td><td>-.0002</td></tr><tr><td>N01</td><td>27.55</td><td>0.96381</td><td>.0847</td><td>-.0006 .0012</td><td>.0002</td><td>-.0002</td></tr><tr><td>P1</td><td>182.62</td><td>0.99454</td><td>.0853</td><td>-.0006 .0012</td><td>.0002</td><td>-.0002</td></tr><tr><td>165,545</td><td>6798.38</td><td>0.99985</td><td>.0869</td><td>-.0006 .0011</td><td>.0002</td><td>-.0003</td></tr><tr><td>K1</td><td>infinity</td><td>1.00000</td><td>.0870</td><td>-.0006 .0011</td><td>.0002</td><td>-.0003</td></tr><tr><td>165,565</td><td>-6798.38</td><td>1.00015</td><td>.0872</td><td>-.0006 .0011</td><td>.0002</td><td>-.0003</td></tr><tr><td>1</td><td>-365.26</td><td>1.00273</td><td>.0710</td><td>-.0020 .0019</td><td>.0002</td><td>.0001</td></tr><tr><td>1</td><td>-182.62</td><td>1.00546</td><td>.0828</td><td>-.0007 .0013</td><td>.0002</td><td>-.0002</td></tr><tr><td>J1</td><td>-27.55</td><td>1.03619</td><td>.0845</td><td>-.0006 .0012</td><td>.0002</td><td>-.0002</td></tr><tr><td>001</td><td>-13.66</td><td>1.07300</td><td>.0846</td><td>-.0006</td><td>.0012 .0002</td><td>-.0002</td></tr><tr><td>Long period</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>55,565</td><td>6798.38</td><td>.000147</td><td>.0936</td><td>-.0028</td><td>.0000 .0002</td><td></td></tr><tr><td>Ssa</td><td>182.62</td><td>.005461</td><td>.0886</td><td>-.0016</td><td>.0000 .0002</td><td></td></tr><tr><td>Mm</td><td>27.55</td><td>.036193</td><td>.0870</td><td>-.0012 .0000</td><td>.0002 .0002</td><td></td></tr><tr><td>Mf</td><td>13.66</td><td>.073002</td><td>.0864</td><td>-.0011 .0000</td><td></td><td></td></tr><tr><td>75,565</td><td>13.63</td><td>.073149</td><td>.0864</td><td>-.0011</td><td>.0000 .0002</td><td></td></tr></table>

$$
\begin{array} { r c l } { G M j } & { = } & { \mathrm { g r a s i t i a l o n a l ~ p a r a m e t e r ~ f o r ~ t h e ~ M o o n ~ ( } j = 2 ) } \\ & & { \mathrm { o r ~ t h e ~ s i m e ~ ( } j = 3 ) , } \\ { G M _ { \perp } } & { = } & { \mathrm { g r a v i l a t i o n a l ~ p a r a m e t e r ~ f o r ~ t h e ~ E a r t h } , } \\ { \hat { H } _ { \perp } , } & { = } & { \mathrm { ~ u n i t ~ v e c t o r ~ f r o m ~ t h e ~ g e c e n t e r ~ t o ~ M e o n ~ o r ~ S A m } } \\ & & { \mathrm { ~ a n d ~ t h e ~ m a g n i t i a l e ~ e q ~ C l u a t i v e t o r , ~ w e c t o r , } } \\ { R _ { e } } & { = } & { \mathrm { E a r t h } ^ { 3 } \mathrm { ~ e q u a t i o n a l ~ n e ~ d i n t e s , } } \\ { \hat { r } , } & { = } & { \mathrm { ~ u n i t ~ v e c t o r ~ f r o m ~ t h e ~ g e c e n t e r ~ t o ~ t h e ~ s t a t i o n ~ a n c } } \\ & & { \mathrm { t h e ~ m a g n i t i o n ~ o f ~ t h e ~ t e t o , } } \\ { h _ { 2 } } & { = } & { \mathrm { n o m i n a l ~ d e g e r e e ~ 2 . } \mathrm { ~ L o w e ~ n o m b e r } , } \\ { l _ { 2 } } & { = } & { \mathrm { n o m i n a l ~ d e g e r e e ~ 2 . } \mathrm { ~ S h i d a } _ { 1 } \mathrm { ~ n u m b e r } . } \end{array}
$$

Note that the part proportional to $h _ { 2 }$ gives the radial (not vertical) component of the tide-induced station displacement, and the terms in $l _ { 2 }$ represent the vector displacement perpendicular to the radial direction (and not in the horizontal plane).

The computation just described may be generalized to include the latitude dependence arising through ${ h ^ { ( 2 ) } }$ by simply adding $h ^ { ( 2 ) } \left[ ( 3 \sin ^ { 2 } \phi - 1 ) / 2 \right]$ to the constant nominal value given above, with $h ^ { ( 2 ) } = - 0 . 0 0 0 6$ . The addition of a similar term (with $l ^ { ( 2 ) } = 0 . 0 0 0 2$ ) to the nominal value of $l _ { 2 }$ takes care of the corresponding contribution to the transverse displacement. The resulting incremental displacements are small, not exceeding 0.4 mm radially and 0.2 mm in the transverse direction.

# Displacement due to degree 3 tides

The Love numbers of the degree 3 tides may be taken as real and constant in computations to the degree of accuracy aimed at here. The displacement vector due to these tides is then given by

$$
\Delta \vec { r } = \sum _ { j = 2 } ^ { 3 } \frac { G M _ { j } R _ { e } ^ { 5 } } { G M _ { \oplus } R _ { j } ^ { 4 } } \biggl \{ h _ { 3 } \hat { r } \biggl ( \frac { 5 } { 2 } ( \hat { R } _ { j } \cdot \hat { r } ) ^ { 3 } - \frac { 3 } { 2 } ( \hat { R } _ { j } \cdot \hat { r } ) \biggr ) + l _ { 3 } \biggl ( \frac { 1 5 } { 2 } ( \hat { R } _ { j } \cdot \hat { r } ) ^ { 2 } - \frac { 3 } { 2 } \biggr ) \left[ \hat { R } _ { j } - ( \hat { R } _ { j } \cdot \hat { r } ) \hat { r } \right] \biggr \} .
$$

Only the Moon’s contribution ( $j = 2$ ) needs to be computed, the term due to the Sun being negligible. The transverse part of the displacement (7.6) does not exceed 0.2 mm, but the radial displacement can reach 1.7 mm.

Contributions to the transverse displacement due to the $l ^ { ( 1 ) }$ term The imaginary part of $l ^ { ( 1 ) }$ is negligible, as is the intra-band variation of Re $l ^ { ( 1 ) }$ ; and $l ^ { ( 1 ) }$ is effectively zero in the zonal band.

In the expressions given below, and elsewhere in this chapter,

$\Phi _ { j } = $ body fixed geocentric latitude of Moon or Sun, and

$\lambda _ { j } =$ body fixed east longitude (from Greenwich) of Moon or Sun.

The following formulae may be employed when the use of Cartesian coordinates $X _ { j } , Y _ { j } , Z _ { j }$ of the body relative to the terrestrial reference frame is preferred:

$$
\begin{array} { r l } & { P _ { 2 } ^ { 0 } \big ( \sin \Phi _ { j } \big ) = \frac { 1 } { R _ { j } ^ { 2 } } \left( \frac { 3 } { 2 } Z _ { j } ^ { 2 } - \frac { 1 } { 2 } R _ { j } ^ { 2 } \right) , } \\ & { P _ { 2 } ^ { 1 } \big ( \sin \Phi _ { j } \big ) \cos \lambda _ { j } = \frac { 3 X _ { j } Z _ { j } } { R _ { j } ^ { 2 } } , } \\ & { P _ { 2 } ^ { 1 } \big ( \sin \Phi _ { j } \big ) \sin \lambda _ { j } = \frac { 3 Y _ { j } Z _ { j } } { R _ { j } ^ { 2 } } , } \\ & { P _ { 2 } ^ { 2 } \big ( \sin \Phi _ { j } \big ) \cos 2 \lambda _ { j } = \frac { 3 } { R _ { j } ^ { 2 } } ( X _ { j } ^ { 2 } - Y _ { j } ^ { 2 } ) , } \\ & { P _ { 2 } ^ { 2 } \big ( \sin \Phi _ { j } \big ) \sin 2 \lambda _ { j } = \frac { 6 } { R _ { j } ^ { 2 } } X _ { j } Y _ { j } . } \end{array}
$$

Contribution from the diurnal band (with $l ^ { ( 1 ) } = 0 . 0 0 1 2$ ):

$$
\delta \vec { t } = - l ^ { ( 1 ) } \sin \phi \sum _ { j = 2 } ^ { 3 } \frac { G M _ { j } R _ { e } ^ { 4 } } { G M _ { \oplus } R _ { j } ^ { 3 } } P _ { 2 } ^ { 1 } ( \sin \Phi _ { j } ) \left[ \sin \phi \cos ( \lambda - \lambda _ { j } ) \ \hat { n } - \cos 2 \phi \sin ( \lambda - \lambda _ { j } ) \ \hat { e } \right] .
$$

Contribution from the semidiurnal band (with $l ^ { ( 1 ) } = 0 . 0 0 2 4$ ):

$$
\delta \vec { t } = - \frac { 1 } { 2 } l ^ { ( 1 ) } \sin \phi \cos \phi \sum _ { j = 2 } ^ { 3 } \frac { G M _ { j } R _ { e } ^ { 4 } } { G M _ { \oplus } R _ { j } ^ { 3 } } P _ { 2 } ^ { 2 } ( \sin \Phi _ { j } ) \left[ \cos 2 ( \lambda - \lambda _ { j } ) { \ \hat { n } } + \sin \phi \sin 2 ( \lambda - \lambda _ { j } ) { \ \hat { e } } \right] .
$$

The contributions of the $l ^ { ( 1 ) }$ term to the transverse displacement caused by the diurnal and semidiurnal tides could be up to $0 . 8 \mathrm { m m }$ and $1 . 0 \mathrm { m m }$ respectively.

# Out-of-phase contributions from the imaginary parts of $h _ { 2 m } ^ { ( 0 ) }$ and

$h ^ { I }$ $l ^ { I }$ $h _ { 2 m } ^ { ( 0 ) }$ $l _ { 2 m } ^ { ( 0 ) }$

Contributions $\delta r$ to radial and $\delta \bar { t }$ to transverse displacements from diurnal tides (with $h ^ { I } = - 0 . 0 0 2 5 , ~ l ^ { I } = - 0 . 0 0 0 7 )$ :

$$
\delta r = - \frac { 3 } { 4 } h ^ { I } \sum _ { j = 2 } ^ { 3 } \frac { G M _ { j } R _ { e } ^ { 4 } } { G M _ { \oplus } R _ { j } ^ { 3 } } \sin 2 \Phi _ { j } \sin 2 \phi \sin ( \lambda - \lambda _ { j } ) ,
$$

$$
\delta \vec { t } = - \frac { 3 } { 2 } l ^ { I } \sum _ { j = 2 } ^ { 3 } \frac { G M _ { j } R _ { e } ^ { 4 } } { G M _ { \oplus } R _ { j } ^ { 3 } } \sin 2 \Phi _ { j } \left[ \cos 2 \phi \sin ( \lambda - \lambda _ { j } ) \hat { n } + \sin \phi \cos ( \lambda - \lambda _ { j } ) \hat { e } \right] .
$$

Contributions from semidiurnal tides (with $h ^ { I } { = } { - } 0 . 0 0 2 2$ , $l ^ { I } { = } { - } 0 . 0 0 0 7$ :

$$
\delta r = - \frac { 3 } { 4 } h ^ { I } \sum _ { j = 2 } ^ { 3 } \frac { G M _ { j } R _ { e } ^ { 4 } } { G M _ { \oplus } R _ { j } ^ { 3 } } \cos ^ { 2 } \Phi _ { j } \cos ^ { 2 } \phi \sin 2 ( \lambda - \lambda _ { j } ) ,
$$

$$
\delta \vec { t } = \frac { 3 } { 4 } \imath ^ { I } \sum _ { j = 2 } ^ { 3 } \frac { G M _ { j } R _ { e } ^ { 4 } } { G M _ { \oplus } R _ { j } ^ { 3 } } \cos ^ { 2 } \Phi _ { j } \left[ \sin 2 \phi \sin 2 ( \lambda - \lambda _ { j } ) \hat { n } - 2 \cos \phi \cos 2 ( \lambda - \lambda _ { j } ) \hat { e } \right] .
$$

The out-of-phase contribution from the zonal tides has no closed expression in the time domain.

Computations of Step 2 take account of the intra-band variation of $h _ { 2 m } ^ { ( 0 ) }$ and l(0)2m. Variations of the imaginary parts are negligible except as stated below (see Table 7.3a). For the zonal tides, however, the contributions from the imaginary part have to be computed in Step 2.

# Correction for frequency dependence of the Love and Shida numbers

(a) Contributions from the diurnal band

Corrections, which include both in-phase $( i p )$ and out-of-phase ( $_ { o p }$ ) parts, to the radial and transverse station displacements $\delta r$ and $\delta \bar { t }$ due to a diurnal tidal term of frequency $f$ are obtainable from Equation (7.1b):

$$
\begin{array} { r l r } { \delta r } & { = } & { [ \delta R _ { f } ^ { ( i p ) } \sin ( \theta _ { f } + \lambda ) + \delta R _ { f } ^ { ( o p ) } \cos ( \theta _ { f } + \lambda ) ] \sin 2 \phi , } \end{array}
$$

$$
\begin{array} { r l r l } { \delta \vec { t } } & { = } & { [ \delta T _ { f } ^ { ( i p ) } \cos ( \theta _ { f } + \lambda ) - \delta T _ { f } ^ { ( o p ) } \sin ( \theta _ { f } + \lambda ) ] \sin \phi \hat { e } } \\ & { } & { + } & { [ \delta T _ { f } ^ { ( i p ) } \sin ( \theta _ { f } + \lambda ) + \delta T _ { f } ^ { ( o p ) } \cos ( \theta _ { f } + \lambda ) ] \cos 2 \phi \hat { n } , } \end{array}
$$

where

$$
\begin{array} { r l } & { \left( \begin{array} { l } { \delta R _ { f } ^ { ( i p ) } } \\ { \delta R _ { f } ^ { ( o p ) } } \end{array} \right) = - \frac { 3 } { 2 } \sqrt { \frac { 5 } { 2 4 \pi } } H _ { f } \left( \begin{array} { l } { \delta h _ { f } ^ { R } } \\ { \delta h _ { f } ^ { I } } \end{array} \right) , } \\ & { \left( \begin{array} { l } { \delta T _ { f } ^ { ( i p ) } } \\ { \delta T _ { f } ^ { ( o p ) } } \end{array} \right) = - 3 \sqrt { \frac { 5 } { 2 4 \pi } } H _ { f } \left( \begin{array} { l } { \delta l _ { f } ^ { R } } \\ { \delta l _ { f } ^ { I } } \end{array} \right) , } \end{array}
$$

and

$\delta h _ { f } ^ { R }$ and $\delta h _ { f } ^ { I }$ are the differences of ${ h ^ { ( 0 ) R } }$ and $h ^ { ( 0 ) I }$ at frequency $f$ from the nominal values $h _ { 2 }$ and $h ^ { I }$ used in Equations (7.5) and (7.10a), respectively,   
$\delta l _ { f } ^ { R }$ and $\delta l _ { f } ^ { I }$ are the differences of $l ^ { ( 0 ) R }$ and $l ^ { ( 0 ) I }$ at frequency $f$ from the nominal values $l _ { 2 }$ and $l ^ { I }$ used in Equations (7.5) and (7.10b), respectively.

Table 7.3a: Corrections due to the frequency dependence of Love and Shida numbers for diurnal tides. Units: mm. All terms with radial correction $\geq 0 . 0 5$ mm are shown. Nominal values are $h _ { 2 } = 0 . 6 0 7 8$ and $l _ { 2 } = 0 . 0 8 4 7$ for the real parts, and $h ^ { I } = - 0 . 0 0 2 5$ and $l ^ { I } = - 0 . 0 0 0 7$ for the imaginary parts. Frequencies are given in degrees per hour.   

<table><tr><td></td><td>Name Frequency Doodson T s h p N&#x27; p: l e F D Ω △Rp) △R(p △T(ip) △T(p)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Q1</td><td>13.39866</td><td>135,6551 -201</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-0.08</td><td>0.00</td><td>-0.01</td><td>0.01</td></tr><tr><td></td><td>13.94083</td><td>145,545</td><td>1-1</td><td></td><td>0</td><td>0</td><td>-1</td><td>0</td><td>0</td><td>0</td><td>2 0</td><td>1</td><td>-0.10</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>01</td><td>13.94303</td><td>145,555</td><td>1-1</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2 0</td><td>2</td><td>-0.51</td><td>0.00</td><td>-0.02</td><td>0.03</td></tr><tr><td>N01</td><td>14.49669</td><td>155,655</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0 0</td><td>0</td><td>0.06</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>T1</td><td>14.91787</td><td>162,556</td><td>1</td><td>1-3</td><td></td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>2-2</td><td>2</td><td>-0.06</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>P1</td><td>14.95893</td><td>163,555</td><td>1</td><td>1-2</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2 -2</td><td>2</td><td>-1.23</td><td>-0.07</td><td>0.06</td><td>0.01</td></tr><tr><td></td><td>15.03886</td><td>165,545</td><td>1</td><td>1</td><td>0</td><td>0</td><td>-1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0-1</td><td>-0.22</td><td>0.01</td><td>0.01</td><td>0.00</td></tr><tr><td>K1</td><td>15.04107</td><td>165,555</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0 0</td><td>0</td><td>12.00</td><td>-0.78</td><td>-0.67</td><td>-0.03</td></tr><tr><td></td><td>15.04328</td><td>165,565</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0 0</td><td>1</td><td>1.73</td><td>-0.12</td><td>-0.10</td><td>0.00</td></tr><tr><td>1</td><td>15.08214</td><td>166,554</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>-1</td><td>0 -1</td><td>0</td><td>0</td><td>0</td><td>-0.50</td><td>-0.01</td><td>0.03</td><td>0.00</td></tr><tr><td>1</td><td>15.12321</td><td>167,555</td><td>1</td><td>12</td><td></td><td>0</td><td>0 </td><td>0</td><td>0</td><td>0-2</td><td></td><td>2-2</td><td>-0.11</td><td>0.01</td><td>0.01</td><td>0.00</td></tr></table>

(b) Contributions from the long-period band Corrections $\delta r$ and $\delta \bar { t }$ due to a zonal tidal term of frequency $f$ include both $_ { i p }$ and $o p$ parts. From Equations (7.1a) and (7.3) one finds

$$
\delta { r } = \left( \frac { 3 } { 2 } \sin ^ { 2 } \phi - \frac { 1 } { 2 } \right) ( \delta { R } _ { f } ^ { ( i p ) } \cos \theta _ { f } + \delta { R } _ { f } ^ { ( o p ) } \sin \theta _ { f } ) ,
$$

$$
{ \delta \vec { t } } = ( \delta T _ { f } ^ { ( i p ) } \cos \theta _ { f } + \delta T _ { f } ^ { ( o p ) } \sin \theta _ { f } ) \sin 2 \phi ~ \hat { n } ,
$$

where

$$
\begin{array} { r l r } { \left( \begin{array} { c } { \delta R _ { f } ^ { ( i p ) } } \\ { \delta R _ { f } ^ { ( o p ) } } \end{array} \right) } & { = } & { \sqrt { \frac { 5 } { 4 \pi } } H _ { f } \left( \begin{array} { c } { \delta h _ { f } ^ { R } } \\ { - \delta h _ { f } ^ { I } } \end{array} \right) , } \\ { \left( \begin{array} { c } { \delta T _ { f } ^ { ( i p ) } } \\ { \delta T _ { f } ^ { ( o p ) } } \end{array} \right) } & { = } & { \frac { 3 } { 2 } \sqrt { \frac { 5 } { 4 \pi } } H _ { f } \left( \begin{array} { c } { \delta l _ { f } ^ { R } } \\ { - \delta l _ { f } ^ { I } } \end{array} \right) . } \end{array}
$$

Table 7.3b: Corrections due to the frequency dependence of Love and Shida numbers for zonal tides. Units: mm. All terms with radial correction $\geq 0 . 0 5$ mm are shown. Nominal values are $h = 0 . 6 0 7 8$ and $l = 0 . 0 8 4 7$ . Frequencies are given in degrees per hour.   

<table><tr><td></td><td>Name Frequency Doodson T s h p N&#x27; p:l l F D Ω △R(𝑖p) △R(p) △T(ip）△T(p)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0.00221</td><td>55,5650000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0０001</td><td>0.47</td><td>0.16</td><td>0.23</td><td>0.07</td></tr><tr><td>Ssa</td><td>0.08214</td><td>57,555</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0 -2</td><td>2</td><td>-2</td><td>-0.20</td><td>-0.11</td><td>-0.12</td><td>-0.05</td></tr><tr><td>Mm</td><td>0.54438</td><td>65,455</td><td>0</td><td>1</td><td></td><td>0-1</td><td>0</td><td>0</td><td>-1</td><td>0 0</td><td>0</td><td>0</td><td>-0.11</td><td>-0.09</td><td>-0.08</td><td>-0.04</td></tr><tr><td>Mf</td><td>1.09804</td><td>75,555</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0 -2</td><td>0-2</td><td></td><td>-0.13</td><td>-0.15</td><td>-0.11</td><td>-0.07</td></tr><tr><td></td><td>1.10024</td><td>75,565</td><td>0</td><td>2</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0 -2</td><td>0-1</td><td></td><td>-0.05</td><td>-0.06</td><td>-0.05</td><td>-0.03</td></tr></table>

Values of $\Delta R _ { f }$ and $\Delta T _ { f }$ listed in Table 7.3a and 7.3b are for the constituents that must be taken into account to ensure an accuracy of $1 \mathrm { m m }$ .

A Fortran program (DEHANTTIDEINEL.F) for computing the steps 1 and 2 corrections is available at ${ < } ^ { 1 } >$ .

7.1.1.2 Permanent deformation The tidal model described above in principle contains a time-independent part so that the coordinates obtained by taking into account this model in the analysis will be “conventional tide free” values. (Note that they do not correspond to what would be observed in the absence of tidal perturbation. See the discussion in Chapter 1.) This section allows a user to compute “mean tide” coordinates from “conventional tide free” coordinates.

Specifically, the degree 2 zonal tide generating potential includes a spectral component of zero frequency and amplitude $H _ { 0 } ~ = ~ - 0 . 3 1 4 6 0 \mathrm { ~ m ~ }$ , and its effect enters the tidal displacement model through the time-independent component of expression (7.5). Evaluation of this component may be done using Equations (7.1a) and (7.2) with ${ \cal H } _ { f } = { \cal H } _ { 0 } , \theta _ { f } = 0$ , and with the same nominal values for the Love number parameters as were used in Step 1: $h _ { 2 } = 0 . 6 0 7 8 , l _ { 2 } = 0 . 0 8 4 7$ along with $h ^ { ( 2 ) } = - 0 . 0 0 0 6$ and $l ^ { ( 2 ) } = 0 . 0 0 0 2$ . One finds the radial component of the permanent displacement according to (7.5) to be

$$
\left[ - 0 . 1 2 0 6 + 0 . 0 0 0 1 P _ { 2 } ( \sin \phi ) \right] P _ { 2 } ( \sin \phi )
$$

in meters, and the transverse component to be

$$
[ - 0 . 0 2 5 2 - 0 . 0 0 0 1 P _ { 2 } ( \sin \phi ) ] \sin 2 \phi
$$

in meters northwards, where $P _ { 2 } ( \sin \phi ) = ( 3 \sin ^ { 2 } \phi - 1 ) / 2$ .

These are the components of the vector to be added to the “conventional tide free” computed tide-corrected position to obtain the “mean tide” position. The radial component of this restitution to obtain the “mean tide” value amounts to about $- 1 2$ cm at the poles and about $+ 6$ cm at the equator.

# 7.1.2 Local site displacement due to ocean loading

Ocean tides cause a temporal variation of the ocean mass distribution and the associated load on the crust and produce time-varying deformations of the Earth that can reach $1 0 0 ~ \mathrm { { m m } }$ . The modeling of the associated site displacement is dealt with in this section.

# Note on motion of the center of mass of the solid Earth

When the solid Earth together with the fluid masses are considered as a system without any external forces acting upon it, the position of the common center of mass remains fixed in space. When a phenomenon, such as the ocean tides, causes displacements of fluid masses, the center of mass of the fluid masses moves periodically and must be compensated by an opposite motion of the center of mass of the solid Earth. The stations, being fixed to the solid Earth, are subject to this counter-motion.

For observing techniques that rely upon the dynamical motion of satellites, which respond to the center of mass of the total Earth system, the modeled motions of crust-fixed stations should include the “geocenter motion” contributions that counterbalance the effects of the fluid components. For other observing techniques, such as VLBI, neglect of geocenter motion should have no observable consequences.

# Models for ocean tidal loading

The tide generating potential due to the gravitational attraction of the Moon and the Sun can be described by an expansion into a set of tidal harmonics (e.g. Hartmann and Wenzel, 1995; Tamura, 1987; Cartwright and Tayler, 1971; Cartwright and Edden, 1973). The response of the oceans, unlike for the solid Earth, is strongly dependent on local and regional conditions that affect fluid flow. Closed-form analytical expressions are not adequate to describe the ocean tidal response globally. Instead, gridded formulations are needed. Table 7.4 lists the leading global ocean tidal models that have been developed since Schwiderski and Szeto (1981). Most modern models assimilate sea surface height measurements made by altimetry satellites.

The crustal loading at a particular location due to a given tidal harmonic is computed by integrating the tide height with a weighting function (Green’s function, see Farrell, 1972), carrying the integration over all the ocean masses. The total loading may be obtained by summing the effect of all harmonics. In practice, the three-dimensional site displacements due to ocean tidal loading are computed using the following scheme. Let $\Delta c$ denote a displacement component (radial, west, south) at a particular site at time $t$ . $\Delta c$ is obtained as

$$
\Delta c = \sum _ { j } A _ { c j } \cos ( \chi _ { j } ( t ) - \phi _ { c j } ) ,
$$

where the summation is carried out for a set of tidal constituents. The amplitudes $A _ { c j }$ and phases $\phi _ { c j }$ describe the loading response for the chosen site. The astronomical argument $\chi _ { j } ( t )$ for the 11 main tides can be computed with the subroutine ARG2.F, which can be obtained at ${ < } ^ { 1 } >$ .

Conventionally, only a discrete set of harmonics in the long-period (order $m = 0$ ), diurnal ( $m = 1$ ) and semidiurnal ( $m = 2$ ) bands are usually considered explicitly. The 11 main tides considered are the semidiurnal waves $M _ { 2 } , S _ { 2 } , N _ { 2 } , K _ { 2 }$ , the diurnal waves $K _ { 1 } , O _ { 1 } , P _ { 1 } , Q _ { 1 }$ , and the long-period waves $M _ { f } , M _ { m }$ , and $S _ { s a }$ . The site-dependent amplitudes $A _ { c j }$ and phases $\phi _ { c j }$ for these 11 tides are obtained as described in the next sub-section. Amplitudes and phases for other tidal constituents can be obtained from those of the 11 main tides by a variety of approximation schemes. For instance, if one wishes to include the effect of sidelobes of the main tides generated by modulation with the 18.6-year lunar node, then suitable adjustments in the 11 amplitudes and phases can be applied so that

$$
\Delta c = \sum _ { k = 1 } ^ { 1 1 } f _ { k } A _ { c k } \cos ( \chi _ { k } ( t ) + u _ { k } - \phi _ { c k } ) ,
$$

where $f _ { k }$ and ${ u } _ { k }$ depend on the longitude of the lunar node. See Scherneck (1999) for the expression of these arguments.

In more complete methods, the lesser tides are handled by interpolation of the admittances using some full tidal potential development (e.g. Hartmann and Wenzel, 1995). One of these methods has been chosen as the conventional IERS method, and has been implemented in a subroutine that is recommended as a conventional computation of the loading displacement (see sub-section “Conventional routine to compute the ocean loading displacement” below).

Note that complete neglect of the minor tides and nodal modulations, using (7.15) with only the 11 main tides, is not recommended and may lead to errors of several mm, up to 5 mm rms at high latitudes (Hugentobler, 2006).

Additional contributions to ocean-induced displacement arise from the frequency dependence of the load Love numbers due to the Nearly Diurnal Free Wobble in the diurnal tidal band. The effect of this dependence has been taken into account, following Wahr and Sasao (1981), by incrementing the body tide Love numbers as explained in Section 7.1.1.

# Site-dependent tidal coefficients

For a given site, the amplitudes $A _ { c j }$ and phases $\phi _ { c j } , 1 \le j \le 1 1$ , for the 11 main tides may be obtained electronically from the ocean loading service site at ${ < } ^ { 2 } >$ ; see Scherneck (1991). They are provided in either the so-called BLQ format or in the HARPOS format. An example for the BLQ format is given in Table 7.5. Note that tangential displacements are to be taken positive in west and south directions. The service allows coefficients to be computed selectably from any of eighteen ocean tide models; see Table 7.4.

The accuracy of the ocean tide loading values depends on the errors in the ocean tide models, the errors in the Green’s function, the coastline representation and the numerical scheme of the loading computation itself. To have a correct representation of the water areas one normally uses a high resolution coastline of around $6 0 0 \mathrm { m }$ to 2 km. Note that still some problems exist near Antarctica where one should use the real land coastline instead of the ice shelve edges. Different elastic Earth models produce different Green’s functions but their differences are small, less than $2 \%$ . Most numerical schemes to compute the loading are good to about 2-5%. Currently, the largest contributor to the uncertainty in the loading value are the errors in the ocean tide models. Therefore it is recommended to use the most recent ocean tide models (TPXO7.2, see ${ < } ^ { 3 } { > }$ for a solution derived using tide gauge and TOPEX/Poseidon data; FES2004 for a hydrodynamic solution with altimetry data). However, older models might sometimes be preferred for internal consistency. Since many space geodesy stations are inland or near coasts, the accuracy of the tide models in the shelf areas is more crucial than in the open sea. Load convolution adopts land-sea masking according to the high resolution coastlines dataset included in the Generic Mapping Tools (GMT, Wessel and Smith, 1998). Ocean tide mass budgets have been constrained using a uniform co-oscillation oceanic layer. The integrating loading kernel employs a disk-generating Green’s function method (Farrell, 1972; Zschau, 1983; Scherneck, 1990).

When generating tables of amplitudes and phases using the ocean loading service, one has to answer the question “Do you want to correct your loading values for the [geocenter] motion?”

Answering “No” means that the coefficients do not include the large-scale effect of the geocenter motion caused by the ocean tide. This is appropriate for station coordinates given in a “crust-fixed” frame that is not sensitive to the Earth’s center of mass.

Answering “Yes” means that the coefficients include the large-scale effect of the geocenter motion caused by the ocean tide. This is consistent with data analyses that realize a near-instantaneous “center of mass” frame using observations of satellite dynamics.

# Conventional routine to compute the ocean loading displacement

D. Agnew has provided a Fortran program (HARDISP.F) to compute the ocean tide loading displacements for a site, given the amplitudes $A _ { c j }$ and phases $\phi _ { c j } , 1 \leq$ $j \le 1 1$ , as generated by the Bos-Scherneck website (in BLQ format, see above). The implementation considers a total of 342 constituent tides whose amplitudes and phases are found by spline interpolation of the tidal admittances based on the 11 main tides. Tests have been carried out showing that differences with an earlier version of HARDISP.F with 141 constituent tides are of order $0 . 1 \mathrm { m m } \mathrm { r m s }$ . Comparisons with the ETERNA software of Wenzel (1996) have been carried out by M. Bos (2005), who concludes that the routine is precise to about $1 \%$ . Uncertainties in the ocean models are generally larger. The code for the routine can be obtained at ${ < } ^ { 1 } >$ .

Table 7.4: Ocean tide models available at the automatic loading service.   

<table><tr><td>Model code</td><td>Reference</td><td>Input</td><td>Resolution</td></tr><tr><td>Schwiderski</td><td>Schwiderski (1980)</td><td>Tide gauge</td><td>1°×1°</td></tr><tr><td>CSR3.0, CSR4.0</td><td>Eanes (1994)</td><td>TOPEX/Poseidon altim.</td><td>1°×1°</td></tr><tr><td>TPXO5</td><td>Eanes and Bettadpur (1995) Egbert et al. (1994)</td><td>T/P + Le Provost loading inverse hydrodyn. solution</td><td>0.5° × 0.5°</td></tr><tr><td>TPXO6.2</td><td>Egbert et al. (2002), see &lt;&gt;</td><td>from T/P altim. idem</td><td>256 × 512 0.25°× 0.25°</td></tr><tr><td>TPXO7.0, TPXO7.1</td><td>idem</td><td>idem</td><td>idem</td></tr><tr><td>FES94.1</td><td>Le Provost et al. (1994)</td><td>numerical model</td><td>0.5° × 0.5°</td></tr><tr><td>FES95.2</td><td>Le Provost et al. (1998)</td><td>num.model + assim.altim.</td><td>0.5° × 0.5°</td></tr><tr><td>FES98</td><td>Lefevre et al. (2000)</td><td>num.model + assim.tide gauges</td><td>0.25°× 0.25°</td></tr><tr><td>FES99</td><td>Lefevre et al. (2002)</td><td>numerical model + assim.</td><td>0.25°× 0.25°</td></tr><tr><td>FES2004</td><td>Letellier (2004)</td><td>tide gauges and altim. numerical model</td><td>0.125°× 0.125°</td></tr><tr><td>GOT99.2b, GOT00.2</td><td>Ray (1999)</td><td>T/P</td><td>0.5° × 0.5°</td></tr><tr><td>GOT4.7</td><td>idem</td><td>idem</td><td>idem</td></tr><tr><td>EOT08a</td><td>Savcenko et al. (2008)</td><td>Multi-mission altimetry</td><td>0.125°× 0.125°</td></tr><tr><td>AG06a</td><td>Andersen (2006)</td><td>Multi-mission altimetry</td><td>0.5°× 0.5°</td></tr><tr><td>NAO.99b</td><td>Matsumoto et al. (2000)</td><td>num. + T/P assim.</td><td>0.5°× 0.5°</td></tr></table>

Table 7.5: Sample of an ocean loading table file in BLQ format. Each site record shows a header with information on the ocean tide model and the site name and geographic coordinates. First three rows of numbers designate amplitudes (meter), radial, west, south, followed by three lines with the corresponding phase values (degrees).   

<table><tr><td colspan="17">Columns designate partial tides M2,S2, N2,K2,K1,O1,P1,Qi,Mf,Mm,and Ssa: $$</td></tr><tr><td>ONSALA</td><td></td><td>$$ CSR4.0_f-PP ID: 2009-06-25 20:02:03</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="10"> $$ Computed by OLMPP by H G Scherneck, Onsala Space Observatory, 2009</td><td colspan="3"></td></tr><tr><td>$$ Onsala,</td><td></td><td></td><td></td><td></td><td></td><td>lon/lat: 11.9264</td><td></td><td>57.3958</td><td></td><td></td><td></td></tr><tr><td>.00352</td><td>.00123</td><td>.00080</td><td>.00032</td><td>.00187</td><td>.00112</td><td>.00063</td><td>.00003</td><td>.00082</td><td></td><td>.00044</td><td>.00037</td></tr><tr><td>.00144</td><td>.00035</td><td>.00035</td><td>.00008</td><td>.00053</td><td>.00049</td><td>.00018</td><td>.00009</td><td></td><td>.00012</td><td>.00005</td><td>.00006</td></tr><tr><td>.00086</td><td>.00023</td><td>.00023</td><td>.00006</td><td>.00029</td><td>.00028</td><td>.00010</td><td></td><td>.00007</td><td>.00004</td><td>.00002</td><td>.00001</td></tr><tr><td>-64.7</td><td>-52.0</td><td>-96.2</td><td>-55.2</td><td>-58.8</td><td>-151.4</td><td></td><td>-65.6</td><td>-138.1</td><td>8.4</td><td>5.2</td><td>2.1</td></tr><tr><td>85.5</td><td>114.5</td><td>56.5</td><td>113.6</td><td>99.4</td><td></td><td>19.1</td><td>94.1</td><td>-10.4</td><td>-167.4</td><td>-170.0</td><td>-177.7</td></tr><tr><td>109.5</td><td>147.0</td><td>92.7</td><td>148.8</td><td>50.5</td><td>-55.1</td><td></td><td>36.4</td><td>-170.4</td><td>-15.0</td><td>2.3</td><td>5.2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

# Center of mass correction

If necessary, the crust-frame translation (geocenter motion) due to the ocean tidal mass, $d X ( t )$ , $d Y ( t )$ , and $d Z ( t )$ , may be computed according to the method given

by Scherneck at ${ < } ^ { 4 } >$ , e.g. for $d X ( t )$ as

$$
d X ( t ) = \sum _ { k = 1 } ^ { 1 1 } X _ { i n } ( k ) \cos ( \chi _ { k } ( t ) ) + X _ { c r } ( k ) \sin ( \chi _ { k } ( t ) )
$$

where the in-phase ( $_ { i n }$ ) and cross-phase ( $_ { c r }$ ) amplitudes (in meters) are tabulated for the various ocean models. Similarly for $d Y ( t )$ and $d Z ( t )$ . This correction should be applied, for instance, in the transformation of GPS orbits from the center-of-mass to the crust-fixed frame expected in the sp3 orbit format

$$
X _ { c r u s t - f i x e d } = X _ { c e n t e r - o f - m a s s } - d X ,
$$

i.e. the translation vector should be substracted when going from center-of-mass to sp3.

# 7.1.3 $\mathbf { S } _ { 1 }  – \mathbf { S } _ { 2 }$ atmospheric pressure loading

The diurnal heating of the atmosphere causes surface pressure oscillations at diurnal $\mathrm { S _ { 1 } }$ , semidiurnal $\mathrm { S _ { 2 } }$ , and higher harmonics. These “atmospheric tides” induce periodic motions of the Earth’s surface (Petrov and Boy, 2004). Previously, the $\mathrm { S } _ { 1 }$ and S $^ 2$ loading effects have not been included in the station motion model. Figure 7.1 shows the amplitude and phase of the predicted vertical deformation of the S1 and $j _ { 2 }$ tides derived from the model of Ray and Ponte (2003) using elastic Green’s functions (Farrell, 1972) in the center of mass of Earth $^ +$ fluid masses (CM) frame. Horizontal deformations (not shown) are a factor of 10 smaller in amplitude. The amplitude of the vertical deformation is equal to that of some ocean tide loading effects and should, therefore, be considered in the station motion model. Being close to the orbital period of the GPS satellites, modeling of the $\mathrm { S _ { 2 } }$ effect is especially important for this technique in order to minimize aliasing (Tregoning and Watson, 2009).

The conventional recommendation is to calculate the station displacement using the Ray and Ponte (2003) S2 and S1 tidal model, hereafter referred to as RP03.

# Tidal model

The S1 and S2 RP03 tidal model is derived from the European Centre for Medium-Range Weather Forecasts (ECMWF) operational global surface pressure fields, using a procedure outlined by van den Dool et al. (1997). The S2 model has been tested by comparison against 428 barometer stations (Ray and Ponte, 2003). It is expected that National Centers for Environmental Prediction (NCEP) operational data provide equivalent results (van den Dool, 2004). Similar comparisons were found for the $\mathrm { S } _ { 1 }$ models, although those tests were far less extensive. The barometer stations have also revealed small phase errors in the derived tidal fields. The origin of these errors is not understood, but the models can be corrected $a$ posteriori. The RP03 phases have been adjusted by 20 minutes to correct for this error.

# Calculation of loading effects

We use elastic Green’s functions (Farrell, 1972) derived in the various reference frames to generate the predicted in-phase and out-of-phase surface displacement from RP03. The spatial resolution of the input surface pressure grid is $1 . 1 2 5 ^ { \circ }$ .

Elastic Green’s functions (versus frequency-dependent Green’s functions) are sufficient for this computation. By considering changes in viscoelasticity, Francis and Mazzega (1990) demonstrated that the amplitude of the M $^ 2$ ocean tidal radial surface displacement can vary by $1 . 5 \%$ and the phase by $3 \%$ , i.e. a negligible amount in comparison to uncertainties in the ocean tide model itself. A $1 . 5 \%$ effect on the $\mathrm { S _ { 2 } }$ radial displacement is $0 . 0 5 ~ \mathrm { { m m } }$ in amplitude which is certainly less than the uncertainty in the $\delta _ { 1 }$ and $\mathrm { S _ { 2 } }$ pressure models and can be ignored.

![](../chunks/IERS Conventions (2010), IERS Technical Note No.36_part_0002_pages_0071-0140/auto/images/068962327783f69968c730dff16a38fbdfc529b6e666935756004f96e9a2c9d2.jpg)  
Figure 7.1: Amplitude (in mm) and phase (in degrees) of the predicted vertical surface displacement from the $\mathrm { S _ { 1 } }$ and $\mathrm { S _ { 2 } }$ atmospheric tides from the model by Ray and Ponte (2003).

In addition, differences in predicted displacements derived from different Green’s functions are on the order of 0.1 mm rms, so it seems unnecessary to generate corrections using Green’s functions derived for different Earth models. The threedimensional surface displacements are determined by assuming that the oceans respond as the solid Earth to the load, i.e. no inverted barometer. At these frequencies, the ocean does not have time to achieve equilibrium. Furthermore, it should be noted that the ocean’s response to these atmospheric tides is already modeled separately through the site displacements due to ocean tidal loading described in Section 7.1.2.

The phase convention follows that of RP03. At any geographic location, at any time, the tidal deformation, expressed in terms of up, east and north components, is the sum of $d ( u , e , n ) _ { S _ { 1 } }$ and $d ( u , e , n ) _ { S _ { 2 } }$ defined as

$$
d ( u , e , n ) _ { S _ { 1 } } = A _ { d 1 } ( u , e , n ) * c o s ( \omega _ { 1 } T ) + B _ { d 1 } ( u , e , n ) * s i n ( \omega _ { 1 } T )
$$

$$
d ( u , e , n ) _ { S _ { 2 } } = A _ { d 2 } ( u , e , n ) * c o s ( \omega _ { 2 } T ) + B _ { d 2 } ( u , e , n ) * s i n ( \omega _ { 2 } T ) ,
$$

where $A _ { d 1 } , B _ { d 1 } , A _ { d 2 } , B _ { d 2 }$ are the surface displacement coefficients expressed in the same length unit as the deformation components, $T$ is UT1 in days and $\omega _ { 1 }$ and $\omega _ { 2 }$ are the frequencies of the $\mathrm { S } _ { 1 }$ and S $^ 2$ atmospheric tides, e.g. $\omega _ { 1 } = 1$ cycle/day and $\omega _ { 2 } = 2$ cycles/day.

The surface displacement coefficients $A _ { d 1 } , B _ { d 1 } , A _ { d 2 } , B _ { d 2 }$ are determined for each site by performing a global convolution sum of the Green’s functions with the $c o s _ { S _ { 1 } } , s i n _ { S _ { 1 } } , c o s _ { S _ { 2 } } , s i n _ { S _ { 2 } }$ pressure mass coefficients. Gridded values of the threedimensional predicted surface displacements from the RP03 model may be found at $< ^ { 5 } >$ . Corrections for the vertical surface displacement are usually sufficient, whereas estimates of horizontal effects are provided for completeness. The grids are provided for the two fundamental reference frames used for geodetic data analysis: center of solid Earth (CE) and center of mass of Earth $^ +$ atmosphere $^ +$ ocean $^ +$ water storage (CM). In most applications, e.g. corrections of satellitebased techniques at the observation level, the CM frame is most appropriate. A description of the grid indexing as well as a program grdintrp.f for interpolating the grids are also available at $< ^ { 5 } >$ .

# Center of mass correction

As with ocean tidal loading (see preceding section), it may be necessary to compute the crust-frame translation (geocenter motion) due to the atmospheric tidal mass. $d X ( t )$ , $d Y ( t )$ , and $d Z ( t )$ may be computed according to the method given by Scherneck at ${ < } ^ { 6 } >$ , e.g. for $d X ( t )$ as

$$
{ } _ { 1 } c o s ( \omega _ { 1 } T ) + B _ { 1 } s i n ( \omega _ { 1 } T ) + A _ { 2 } c o s ( \omega _ { 2 } T ) + B _ { 2 } s i n ( \omega _ { 2 } T
$$

where, as above, $\omega _ { 1 } = 1$ cycle/day and $\omega _ { 2 } = 2$ cycles/day and $A _ { 1 } , B _ { 1 } , A _ { 2 } , B _ { 2 }$ are the amplitudes of the in-phase and out-of-phase components of the atmospheric tides (in meters) and are given in Table 7.6 and in the file com.dat available at ${ < } ^ { 5 } >$ . As with ocean tidal loading (see preceding section), this correction should be applied in transforming GPS orbits from the center-of-mass to the crust-fixed frame expected in the sp3 orbit format.

Table 7.6: Coefficients for the center of mass correction of the $\mathrm { S _ { 1 } { - } S _ { 2 } }$ atmospheric pressure loading   

<table><tr><td></td><td>A1</td><td>B1</td><td>A2</td><td>B2</td></tr><tr><td>dX</td><td>2.1188E-04</td><td>-7.6861E-04</td><td>1.4472E-04</td><td>-1.7844E-04</td></tr><tr><td>dY</td><td>-7.2766E-04</td><td>-2.3582E-04</td><td>-3.2691E-04</td><td>-1.5878E-04</td></tr><tr><td>dZ</td><td>-1.2176E-05</td><td>3.2243E-05</td><td>-9.6271E-05</td><td>1.6976E-05</td></tr></table>

# 7.1.4 Rotational deformation due to polar motion

The variation of station coordinates caused by the pole tide can amount to a couple of centimeters and needs to be taken into account.

Let us choose $\hat { x } , \hat { y }$ and $\hat { z }$ as a terrestrial system of reference. The $\hat { z }$ -axis is oriented along the Earth’s mean rotation axis, the $\hat { x }$ -axis points in the direction of the adopted origin of longitude and the $\hat { y }$ -axis is orthogonal to the $\hat { x }$ - and $\hat { z }$ - axes and in the plane of the $9 0 ^ { \circ }$ $\mathrm { E }$ meridian.

The centrifugal potential caused by the Earth’s rotation is

$$
V = \frac { 1 } { 2 } \left[ r ^ { 2 } | \vec { \Omega } | ^ { 2 } - \left( \vec { r } \cdot \vec { \Omega } \right) ^ { 2 } \right] ,
$$

where $\vec { \Omega } = \Omega ( m _ { 1 } \ \hat { x } + m _ { 2 } \ \hat { y } + ( 1 + m _ { 3 } ) \ \hat { z } )$ . $\Omega$ is the mean angular velocity of the Earth’s rotation; $m _ { 1 }$ , $m _ { 2 }$ describe the time-dependent offset of the instantaneous rotation pole from the mean, and ${ } ^ { m _ { 3 } }$ , the fractional variation in the rotation rate; $r$ is the geocentric distance to the station.

Neglecting the variations in $m _ { 3 }$ which induce displacements that are below the mm level, the $_ { m 1 }$ and $m _ { 2 }$ terms give a first order perturbation in the potential $V$ (Wahr, 1985)

$$
\Delta V ( r , \theta , \lambda ) = - \frac { \Omega ^ { 2 } r ^ { 2 } } { 2 } \sin { 2 \theta } ( m _ { 1 } \cos \lambda + m _ { 2 } \sin \lambda ) .
$$

The radial displacement $S _ { r }$ and the horizontal displacements $S _ { \theta }$ and $S _ { \lambda }$ (positive upwards, south and east, respectively, in a horizon system at the station) due to $\Delta V$ are obtained using the formulation of tidal Love numbers $h _ { 2 }$ and $\ell _ { 2 }$ (Munk and MacDonald, 1960):

$$
S _ { r } = h _ { 2 } \frac { \Delta V } { g } , \qquad S _ { \theta } = \frac { \ell _ { 2 } } { g } \partial _ { \theta } \Delta V , \qquad S _ { \lambda } = \frac { \ell _ { 2 } } { g } \frac { 1 } { \sin \theta } \partial _ { \lambda } \Delta V .
$$

The position of the Earth’s mean rotation pole has a secular variation, and its coordinates in the Terrestrial Reference Frame discussed in Chapter 4 are given, in terms of the polar motion variables $( x _ { p } , y _ { p } )$ defined in Chapter 5, by appropriate running averages $x _ { p }$ and $- \bar { y } _ { p }$ . Then

$$
m _ { 1 } = x _ { p } - \bar { x } _ { p } , \qquad m _ { 2 } = - ( y _ { p } - \bar { y } _ { p } ) .
$$

For the most accurate results, an estimate of the wander of the mean pole should be used, that represents the secular variation to within about 10 mas. This ensures that the geopotential field is aligned to the long term mean pole (see Section 6.1) within the present geodetic accuracy. This is no longer the case (Ries, 2010) with the conventional mean pole of the IERS Conventions (2003) which is to be replaced with the model given below. In the future, the IERS conventional mean pole will be revised as needed with sufficient advance notice. The present version (2010) of the conventional mean pole is composed of a cubic model valid over the period 1976.0–2010.0 and a linear model for extrapolation after 2010.0, ensuring continuity and derivability at 2010.0. The cubic model was derived by the IERS Earth Orientation Centre from a fit over the period 1976.0–2010.0 of the data in $< ^ { \prime } >$ . This data itself was obtained (Gambis, 2010) by filtering periodic terms in the EOP(IERS) C01 series $< ^ { 8 } >$ with an X11 Census process (Shiskin et al., 1967). The IERS (2010) mean pole model reads

$$
\bar { x } _ { p } ( t ) = \sum _ { i = 0 } ^ { 3 } ( t - t _ { 0 } ) ^ { i } \times \bar { x } _ { p } ^ { i } , \qquad \bar { y } _ { p } ( t ) = \sum _ { i = 0 } ^ { 3 } ( t - t _ { 0 } ) ^ { i } \times \bar { y } _ { p } ^ { i } ,
$$

where $t _ { 0 }$ is $2 0 0 0 . 0 < ^ { 9 } >$ and the coefficients $\bar { x } _ { p } ^ { i }$ and $\bar { y } _ { p } ^ { i }$ are given in Table 7.7.

Table 7.7: Coefficients of the IERS (2010) mean pole model   

<table><tr><td colspan="2"></td><td>Until</td><td>2010.0</td><td>After</td><td>2010.0</td></tr><tr><td>Degree i</td><td></td><td>x/mas yr-i</td><td>g/mas yr-i</td><td>x/mas yr-i</td><td>/ mas yr-i</td></tr><tr><td>0</td><td></td><td>55.974</td><td>346.346</td><td>23.513</td><td>358.891</td></tr><tr><td>1</td><td></td><td>1.8243</td><td>1.7896</td><td>7.6141</td><td>-0.6287</td></tr><tr><td></td><td>2</td><td>0.18413</td><td>-0.10729</td><td>0.0</td><td>0.0</td></tr><tr><td>3</td><td></td><td>0.007024</td><td>-0.000908</td><td>0.0</td><td>0.0</td></tr></table>

Using Love number values appropriate to the frequency of the pole tide ( $h _ { 2 } =$ 0.6207, $l _ { 2 } = 0 . 0 8 3 6$ ) and $r = a = 6 . 3 7 8 \times 1 0 ^ { 6 } \mathrm { ~ m }$ , one finds

$$
\begin{array} { r l } & { S _ { r } = - 3 3 \sin 2 \theta \left( m _ { 1 } \cos \lambda + m _ { 2 } \sin \lambda \right) \mathrm { i n m m } , } \\ & { S _ { \theta } = - 9 \cos 2 \theta \left( m _ { 1 } \cos \lambda + m _ { 2 } \sin \lambda \right) \mathrm { i n m m } , } \\ & { S _ { \lambda } = 9 \cos \theta \left( m _ { 1 } \sin \lambda - m _ { 2 } \cos \lambda \right) \mathrm { i n m m } , } \end{array}
$$

with $m _ { 1 }$ and $m _ { 2 }$ given in arcseconds. Note that the values of the Love numbers include the anelastic contributions to the real part, which induce a contribution to the displacement of order $1 \mathrm { m m }$ , but do not include the contributions to the imaginary part, whose effects are about 5 times smaller. Taking into account that $_ { T / l 1 }$ and $m _ { 2 }$ vary, at most, by 0.8 as, the maximum radial displacement is approximately $2 5 \mathrm { m m }$ , and the maximum horizontal displacement is about 7 mm. If $X$ , $Y$ , and $Z$ are Cartesian coordinates of a station in a right-handed equatorial coordinate system, the changes in them due to polar motion are (note that the order of components is different in Equations (7.26) and (7.27))

$$
[ d X , d Y , d Z ] ^ { T } = R ^ { T } [ S _ { \theta } , S _ { \lambda } , S _ { r } ] ^ { T } ,
$$

where

$$
\begin{array} { r } { R = \left( \begin{array} { c c c } { \cos \theta \cos \lambda } & { \cos \theta \sin \lambda } & { - \sin \theta } \\ { - \sin \lambda } & { \cos \lambda } & { 0 } \\ { \sin \theta \cos \lambda } & { \sin \theta \sin \lambda } & { \cos \theta } \end{array} \right) . } \end{array}
$$

# 7.1.5 Ocean pole tide loading

The ocean pole tide is generated by the centrifugal effect of polar motion on the oceans. This centrifugal effect is defined in Equation (6.10) of Section 6.2. Polar motion is dominated by the 14-month Chandler wobble and annual variations. At these long periods, the ocean pole tide is expected to have an equilibrium response, where the displaced ocean surface is in equilibrium with the forcing equipotential surface.

Desai (2002) presents a self-consistent equilibrium model of the ocean pole tide. This model accounts for continental boundaries, mass conservation over the oceans, self-gravitation, and loading of the ocean floor. Using this model, the load of the ocean pole tide produces the following deformation vector at any point on the surface of the Earth with latitude $\phi$ and longitude $\lambda$ . The load deformation vector is expressed here in terms of radial, north and east components, $u _ { r }$ , $u _ { n }$ , and $u _ { e }$ , respectively, and is a function of the wobble parameters $( m _ { 1 } , m _ { 2 } )$ .

$$
\left[ \begin{array} { l } { u _ { r } ( \phi , \lambda ) } \\ { u _ { n } ( \phi , \lambda ) } \\ { u _ { e } ( \phi , \lambda ) } \end{array} \right] = K \left\{ \left( \begin{array} { l } { \boldsymbol { u } _ { r } ^ { R } ( \phi , \lambda ) } \\ { \left( \boldsymbol { m } _ { 1 } \gamma _ { 2 } ^ { R } + \boldsymbol { m } _ { 2 } \gamma _ { 2 } ^ { I } \right) } \\ { \boldsymbol { u } _ { e } ^ { R } ( \phi , \lambda ) } \end{array} \right) \left[ \begin{array} { l } { \boldsymbol { u } _ { r } ^ { R } ( \phi , \lambda ) } \\ { \boldsymbol { u } _ { n } ^ { R } ( \phi , \lambda ) } \\ { \boldsymbol { u } _ { e } ^ { R } ( \phi , \lambda ) } \end{array} \right] + \left( \boldsymbol { m } _ { 2 } \gamma _ { 2 } ^ { R } - \boldsymbol { m } _ { 1 } \gamma _ { 2 } ^ { I } \right) \left[ \begin{array} { l } { \boldsymbol { u } _ { r } ^ { I } ( \phi , \lambda ) } \\ { \boldsymbol { u } _ { n } ^ { I } ( \phi , \lambda ) } \\ { \boldsymbol { u } _ { e } ^ { I } ( \phi , \lambda ) } \end{array} \right] \right\}
$$

where

$$
\begin{array} { c } { { K = \displaystyle \frac { 4 \pi G a _ { E } \rho _ { w } H _ { p } } { 3 g _ { e } } } } \\ { { { } } } \\ { { H _ { p } = \left( \displaystyle \frac { 8 \pi } { 1 5 } \right) ^ { 1 / 2 } \displaystyle \frac { \Omega ^ { 2 } a _ { E } ^ { 4 } } { G M } } } \end{array}
$$

and

$\Omega$ , $a _ { E }$ , $\it G M$ , $g _ { e }$ , and $G$ are defined in Chapter 1,   
$\rho _ { w } = \mathrm { d e n s i t } .$ y of sea water $= 1 0 2 5 ~ \mathrm { k g ~ m ^ { - 3 } }$ ,   
$\gamma = ( 1 + k _ { 2 } - h _ { 2 } ) = \gamma _ { 2 } ^ { R } + i \gamma _ { 2 } ^ { I } = 0 . 6 8 7 0 + 0 . 0 0 3 6 i$ (Values of $k _ { 2 }$ and $h _ { 2 }$ appropriate   
for the pole tide are as given in Sections 6.2 and 7.1.4),

![](../chunks/IERS Conventions (2010), IERS Technical Note No.36_part_0002_pages_0071-0140/auto/images/57f6d43f43ad0d2e83323b8b644729c74f2b5868e273be122a7b741d20c118a3.jpg)  
Figure 7.2: Loading from ocean pole tide: Amplitude as a function of the amplitude of wobble variable.

$( m _ { 1 } , m _ { 2 } )$ are the wobble parameters. Refer to Section 7.1.4 for the relationship between the wobble variables $( m _ { 1 } , m _ { 2 } )$ and the polar motion variables $( x _ { p } , y _ { p } )$ . $u _ { r } ^ { R } ( \phi , \lambda )$ , $u _ { n } ^ { R } ( \phi , \lambda )$ , $u _ { e } ^ { R } ( \phi , \lambda )$ are the real part of the ocean pole load tide coefficients. ${ u } _ { r } ^ { I } ( \phi , \lambda ) , ~ { u } _ { n } ^ { I } ( \phi , \lambda ) , ~ { u } _ { e } ^ { I } ( \phi , \lambda )$ are the imaginary part of the ocean pole load tide

coefficients.

Maps of the required ocean pole load tide coefficients are available on an equally spaced 0.5 by 0.5 degree global grid at ${ < } ^ { 1 0 } >$ . These coefficients provide the surface deformations with respect to the instantaneous center of mass of the deformed Earth including the mass of the loading ocean pole tide.

The amplitude of this loading deformation is shown in Figure 7.2 in mm per arcsecond as a function of the amplitude $m$ of the wobble components $( m _ { 1 } , ~ m _ { 2 } )$ . Given that the amplitude of the wobble variable is typically of order 0.3 arcseconds, the load deformation is typically no larger than about (1.8, 0.5, 0.5) mm in (radial, north, east) component, but it may occasionally be larger.

# 7.2 Models for other non-conventional displacement of reference markers on the crust

It is envisioned that this section describes methods of modeling non-tidal displacements associated with changing environmental loads, e.g. from atmosphere, ocean and hydrology. For this purpose, models should be made available to the user community through the IERS Global Geophysical Fluid Center and its special bureaux, together with all necessary supporting information, implementation documentation, and software.

At the time of this registered edition of the IERS Conventions, it is recommended not to include such modeling in operational solutions that support products and services of the IERS. Nevertheless, the non-tidal loading effects can be considered in other studies, and this section will be updated as adopted models become available.

# 7.3 Models for the displacement of reference points of instruments

This section lists effects which are to be considered when relating the reference point of an instrument used in a given technique to a marker that may be used as a reference by other techniques. Typical examples are antenna phase center offsets. These effects are technique-dependent and the conventional models for these effects are kept and updated by the technique services participating to the IERS: The IVS ${ < } ^ { 1 1 } >$ for very long baseline interferometry, the ILRS ${ < } ^ { 1 2 } >$ for satellite laser ranging, the IGS ${ < } ^ { 1 3 } >$ for global navigation satellite systems and the IDS ${ < } ^ { 1 4 } >$ for DORIS. This section provides a short description of these models and directs the user to the original source of information.

# 7.3.1 Models common to several techniques

As some of the effects depend on local environmental conditions, conventional models for these effects need to be based on a reference value for local temperature. A conventional model to determine reference temperature is given below.

# Reference temperature

If necessary, it is recommended to determine the reference temperature values with the model GPT (Boehm et al., 2007) which is based on a spherical harmonic expansion of degree and order 9 with an annual periodicity, and is provided as a Fortran routine, GPT.F, at ${ < } ^ { 1 5 } >$ and ${ < } ^ { 1 6 } >$ . The arguments of the routine are described in its header. The model assumes a yearly signature and no secular variation, so should not impact secular terms in the modeled geodetic data. If only a constant reference temperature is needed (no yearly term), the model value at the $1 1 9 ^ { t h }$ day of year, 07:30 UTC (e.g. MJD 44357.3125) should be used.

# 7.3.2 Very long baseline interferometry

# Thermal expansion

VLBI antennas are subject to structural deformations due to temperature variations that can cause variations in the VLBI delay exceeding 10 ps. Correspondingly, the coordinates of the reference point may vary by several mm. For this reason the IVS has developed a model for VLBI antenna thermal deformation (Nothnagel, 2008) that is to be used in its routine product generation. The conventional model for VLBI antenna thermal deformation may be found at ${ < } ^ { 1 7 } >$ .

# 7.3.3 Global navigation satellite systems

Antenna phase center offsets and variations The exact phase center position of the transmitting as well as of the receiving antenna depends on the line of sight from the satellite to the receiver. This anisotropy is modeled by a phase center offset from a physical reference point to the mean electrical phase center together with its corresponding elevation- and azimuth-dependent variations. Since November 2006, the IGS applies consistent absolute phase center corrections for satellite and receiver antennas (Schmid et al., 2007). The current model is available at $< ^ { 1 8 } >$ .

# References

Andersen, O. B., 2006, see http://www.spacecenter.dk/data/global-ocean-tide-model-1/.   
Boehm, J., Heinkelmann, R., and Schuh, H., 2007, “Short Note: A global model of pressure and temperature for geodetic applications,” J. Geod., 81(10), pp. 679–683, doi:10.1007/s00190-007-0135-3.   
Bos, M. S., 2005, personal communication.   
Cartwright, D. E. and Tayler, R. J., 1971, “New computations of the tide-generating potential,” Geophys. J. Roy. astr. Soc., 23(1), pp. 45–74.   
Cartwright, D. E. and Edden, A. C., 1973, “Corrected tables of tidal harmonics,” Geophys. J. Roy. astr. Soc., 33(3), pp. 253–264, doi:10.1111/j.1365- 246X.1973.tb03420.x.   
Chelton, D. B. and Enfield, D. B., 1986, “Ocean signals in tide gauge records,” J. Geophys. Res., 91(B9), pp. 9081–9098, doi: 10.1029/JB091iB09p09081   
Desai, S. D., 2002, “Observing the pole tide with satellite altimetry,” J. Geophys. Res., 107(C11), 3186, doi:10.1029/2001JC001224.   
Doodson, A. T., 1928, “The Analysis of Tidal Observations,” Phil. Trans. Roy. Soc. Lond., 227, pp. 223–279, http://www.jstor.org/stable/91217   
Eanes, R. J., 1994, “Diurnal and semidiurnal tides from TOPEX/Poseidon altimetry,” paper G32B-6, presented at the Spring Meeting of the AGU, Baltimore, MD, EOS Trans AGU, 75, p. 108.   
Eanes R. J. and Bettadpur, S., 1995, “The CSR 3.0 global ocean tide model,” Technical Memorandum CSR-TM-95-06, Center for Space Research, University of Texas, Austin, TX.   
Egbert, G. D., Bennett, A. F., and Foreman, M. G. G., 1994, “TOPEX/ Poseidon tides estimated using a global inverse model,” J. Geophys. Res., 99(C12), pp. 24821–24852, doi: 10.1029/94JC01894   
Egbert, G. D., Erofeeva, S.Y., 2002, “Efficient inverse modeling of barotropic ocean tides,” J. Atmos. Ocean. Technol., 19(2), pp. 183–204.

Farrell, W. E., 1972, “Deformation of the Earth by surface loads,” Rev. Geophys. Space Phys., 10(3), pp. 761–797, doi: 10.1029/RG010i003p00761.

Francis, O. and P. Mazzega, 1990, “Global charts of ocean tide loading effects,” J. Geophys Res., 95(C7), pp. 11411–11424, doi:10.1029/JC095iC07p11411.

Gambis, D., personal communication, 2010.

Haas, R., 1996, “Untersuchungen zu Erddeformationsmodellen f¨ur die Auswertung von geod¨atischen VLBI-Messungen”, PhD Thesis, Deutsche Geod¨atische Kommission, Reihe C, Heft Nr. 466, 103 pp.

Haas, R., Scherneck, H.-G., and Schuh, H., 1997, “Atmospheric loading corrections in Geodetic VLBI and determination of atmospheric loading coefficients,” in Proc. of the 12 Working Meeting on European VLBI for Geodesy and Astronomy, Pettersen, B.R. (ed.), Honefoss, Norway, 1997, pp. 122–132.

Hartmann, T. and Wenzel, H.-G., 1995, “The HW95 tidal potential catalogue,” Geophys. Res. Lett., 22(24), pp. 3553–3556, doi: 1029/95GL03324

Hugentobler, U., 2006, personal communication.

Le Provost, C., Genco, M. L., Lyard, F., Vincent, P., and Canceil, P., 1994, “Spectroscopy of the world ocean tides from a finite element hydrodynamic model,” J. Geophys. Res., 99(C12), pp. 24777–24797, doi: 10.1029/94JC01381

Le Provost, C., Lyard, F., Molines, J. M., Genco, M. L., and Rabilloud, F., 1998, “A hydrodynamic ocean tide model improved by assimilating a satellite altimeter-derived data set,” J. Geophys. Res., 103(C3), pp. 5513–5529, doi: 10.1029/97JC01733

Lef\`evre, F., Lyard, F. H., and Le Provost, C., 2000, “FES98: A new global tide finite element solution independent of altimetry,” Geophys. Res. Lett., 27(17), pp. 2717–2720, doi: 10.1029/1999GL011315

Lef\`evre, F., Lyard, F. H., Le Provost, C., and Schrama, E.J.O., 2002, “FES99: A global tide finite element solution assimilating tide gauge and altimetric information,” J. of Atmos. Ocean. Technol., 19(9), pp. 1345–1356.

Letellier, T., 2004, “Etude des ondes de mar´ee sur les plateaux continentaux,” Th\`ese doctorale, Universit´e de Toulouse III, 237pp.

MacMillan, D. S. and Gipson, J. M., 1994, “Atmospheric pressure loading parameters from Very Long Baseline Interferometry observations,” J. Geophys. Res., 99(B9), pp. 18081–18087, doi: 10.1029/94JB01190

Mathers, E. L. and Woodworth, P. L., 2001, “Departures from the local inverse barometer model observed in altimeter and tide gauge data and in a global barotropic numerical model,” J. Geophys. Res., 106(C4), pp. 6957–6972, doi: 10.1029/2000JC000241

Mathews, P. M., Buffett, B. A., and Shapiro, I. I., 1995, “Love numbers for a rotating spheroidal Earth: New definitions and numerical values,” Geophys. Res. Lett., 22(5), pp. 579–582, doi: 10.1029/95GL00161

Matsumoto, K., Takanezawa, T. and Ooe, M., 2000, “Ocean tide models developed by assimilating TOPEX/Poseidon altimeter data into hydrodynamical model: A global model and a regional model around Japan,” J. Oceanog., 56(5), pp. 567–581.

Munk, W. H. and MacDonald, G. J. F., 1960, The Rotation of the Earth, Cambridge Univ. Press, New York, pp. 24–25.

Nothnagel, A., 2009, “Conventions on thermal expansion modelling of radio telescopes for geodetic and astrometric VLBI ,” J. Geod., 83(8), pp. 787–792, doi: 10.1007/s00190-008-0284-z.

Petrov, L. and J.-P. Boy, 2004, “Study of the atmospheric pressure loading signal in very long baseline interferometry observations,” J. Geophys. Res., 109, B03405, 14 pp., doi: 10.1029/2003JB002500.

Ponte, R. M., Salstein, D. A., and Rosen, R. D., 1991, “Sea level response to pressure forcing in a barotropic numerical model,” J. Phys. Oceanogr., 21(7), pp. 1043–1057.   
Ray, R., 1999, “A global ocean tide model From TOPEX/Poseidon altimetry: GOT99.2,” NASA Technical Memorandum, NASA/TM-1999-209478, National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, MD.   
Ray, R. D. and R. M. Ponte, 2003, “Barometric tides from ECMWF operational analyses,” Ann. Geophys., 21(8), pp. 1897–1910, doi:10.5194/angeo-21- 1897-2003.   
Ries, J.C., personal communication, 2010.   
Row, L. W., Hastings, D. A., and Dunbar, P. K., 1995, “TerrainBase Worldwide Digital Terrain Data,” NOAA, National Geophysical Data Center, Boulder CO.   
Savcenko, R., Bosch, W., 2008, “EOT08a - empirical ocean tide model from multi-mission satellite altimetry,” Report No. 81, Deutsches Geod¨atisches Forschungsinstitut (DGFI), M¨unchen, ftp://ftp.dgfi.badw.de/pub/EOT08a/doc/EOTO8a.pdf   
Schmid, R., Steigenberger, P., Gendt, G., Ge, M., and Rothacher, M., 2007, “Generation of a consistent absolute phase center correction model for GPS receiver and satellite antennas,” J. Geod., 81(12), pp. 781–798, doi:10.1007/s00190-007-0148-y.   
Scherneck, H.-G., 1990, “Loading Green’s functions for a continental shield with a Q-structure for the mantle and density constraints from the geoid,” Bull. d’Inform. Mar´ees Terr., 108, pp. 7775–7792.   
Scherneck, H.-G., 1991, “A parameterized solid earth tide model and ocean tide loading effects for global geodetic baseline measurements,” Geophys. J. Int., 106(3), pp. 677–694, doi: 10.1111/j.1365-246X.1991.tb06339.x   
Scherneck, H.-G., 1993, “Ocean tide loading: propagation of errors from the ocean tide into loading coefficients,” man. Geod., 18(2), pp. 59–71.   
Scherneck, H.-G., 1999, in Explanatory supplement to the section “Local site displacement due to ocean loading” of the IERS Conventions (1996) Chapters 6 and 7, Schuh, H. (ed.), DGFI Report 71, pp. 19–23.   
Schwiderski, E. W., 1980, “On charting global ocean tides,” Rev. Geophys. Space Phys., 18(1), pp. 243–268, doi: 10.1029/RG018i001p00243   
Schwiderski, E. W. and Szeto, L. T., 1981, “The NSWC global ocean tide data tape (GOTD), its features and application, random-point tide program,” NSWC-TR 81–254, Naval Surface Weapons Center, Dahlgren, VA, 19 pp.   
Shiskin, J., Young, A., Musgrave, J.C., 1967, “The X11 variant of the Census method II seasonal adjustment program,” Washington DC, Technical Paper n15, Bureau of Census, US Department of Commerce.   
Sun, H. P., Ducarme, B., and Dehant, V., 1995, “Effect of the atmospheric pressure on surface displacements,” J. Geod., 70(3), pp. 131–139, doi: 10.1007/BF00943688   
Tamura, Y., 1987, “A harmonic development of the tide-generating potential,” Bull. d’Inform. Mar´ees Terr., 99, pp. 6813–6855.   
Tregoning, P. and C. Watson, 2009, “Atmospheric effects and spurious signals in GPS analyses”, J. Geophys. Res., 114(B9), B09403, 15 pp., doi: 10.1029/2009JB006344.   
van den Dool, H. M., S. Saha, J. Schemm, and J. Huang, 1997, “A temporal interpolation method to obtain hourly atmospheric surface pressure tides in Reanalysis 1979-1995,” J. Geophys. Res., 102(D18), pp. 22013–22024, doi:10.1029/97JD01571.   
van den Dool, H. M., 2004, personal communication.   
Wahr, J. M., 1981, “Body tides on an elliptical, rotating, elastic, and oceanless Earth,” Geophys. J. Roy. astr. Soc., 64(3), pp. 677–703.   
Wahr, J. M., 1985, “Deformation induced by polar motion,” J. Geophys. Res., 90(B11), pp. 9363–9368, doi:10.1029/JB090iB11p09363.   
Wahr, J. M. and Sasao, T., 1981, “A diurnal resonance in the ocean tide and the Earth’s load response due to the resonant free “core nutation”,” Geophys. J. R. astr. Soc., 64, pp. 747–765.   
Wenzel, H.-G., 1996 “The nanogal software: Earth tide data processing package Eterna 3.3,” Bull. d’Inform. Mar´ees Terr., 124, pp. 9425–9439.   
Wessel, P. and Smith, W. H. F., 1998, “New, improved version of the Generic Mapping Tools released,” EOS Trans. AGU, 79, 579.   
Zschau, J., 1983, “Rheology of the Earth’s mantle at tidal and Chandler Wobble periods,” Proc. Ninth Int. Symp. Earth Tides, New York, 1981, Kuo, J. T. (ed.), Schweizerbart’sche Verlagsbuchhandlung, Stuttgart, pp. 605–630.

# 8 Tidal variations in the Earth’s rotation

# 8.1 Effect of the tidal deformation (zonal tides) on Earth’s rotation

Periodic variations in UT1 due to tidal deformation of the polar moment of inertia were first derived by Yoder et al. (1981) and included the tidal deformation (zonal tides) of the Earth with a decoupled core, an elastic mantle and equilibrium oceans. This model used effective Love numbers that differ from the bulk value of 0.301 because of the oceans and the fluid core, producing different theoretical values of the ratio $k / C$ (defined as the quantity which scales the rotational series, where $k$ is that part of the Love number which causes the tidal variation in the moment of inertia of the coupled mantle and oceans and $C$ is the dimensionless polar moment of inertia of the coupled values) for the fortnightly and monthly terms. However, Yoder et al. (1981) recommend the value of 0.94 for $k / C$ for both cases.

Past versions of the IERS Conventions defined regularized UT1 $^ { 1 }$ as UT1 with the effect of the corrected tides with periods less than 35 days removed and UT1S as UT1 with the effects of all tidal constituents removed, including the long-period tides (up to 18.6 years). However, the IERS Conventions recommend that only UT1 and length of day (here noted $\Delta$ ) be used in routine data exchange applications in order to avoid possible confusion regarding the exact implementation of tidal models. In research applications, analysts must be careful to specify unambiguously any tidal models used.

Table 8.1 provides corrections for the tidal variations in the Earth’s rotation with periods from 5 days to 18.6 years. These corrections (δUT1, $\delta \Delta$ , $\delta \omega$ ) represent the effect of tidal deformation on the physical variations in the rotation of the Earth and are the sum of: (1) the Yoder et al. (1981) elastic body and equilibrium ocean tide model assuming a value of 0.94 for $k / C$ ; (2) the in-phase and outof-phase components of the Wahr and Bergen (1986) inelastic body tide model for the QMU Earth model of Sailor and Dziewonski (1978) assuming a frequency dependence of $( f _ { m } / f ) ^ { \alpha }$ where $\alpha = 0 . 1 5$ , $f _ { m }$ is the seismic frequency corresponding to a period of $2 0 0 \mathrm { s }$ , and $f$ is the tidal frequency; and (3) the data assimilating dynamic ocean tide model “A” of Kantha et al. (1998) from which the equilibrium model of Yoder et al. (1981) was removed (see Gross (2009) for an evaluation of these and other tide models). To obtain variations free from tidal effects, these corrections should be subtracted from the observed UT1 $-$ UTC, length of day ( $\Delta$ ) and rotation velocity ( $\omega$ ). The difference between this newly recommended model and that in the Conventions ${ \it 2 0 0 3 }$ is mainly at the fortnightly tidal period where the UT1 amplitude difference is approximately 6 $\mu \mathrm { s }$ . The total amplitude of the fortnightly tide in UT1 is about 785 µs.

$$
\delta \mathrm { U T } 1 = \sum _ { i = 1 } ^ { 6 2 } B _ { i } \sin \xi _ { i } + C _ { i } \cos \xi _ { i } ,
$$

$$
\delta \Delta = \sum _ { i = 1 } ^ { 6 2 } B _ { i } ^ { \prime } \cos \xi _ { i } + C _ { i } ^ { \prime } \sin \xi _ { i } ,
$$

$$
\delta \omega = \sum _ { i = 1 } ^ { 6 2 } B _ { i } ^ { \prime \prime } \cos \xi _ { i } + C _ { i } ^ { \prime \prime } \sin \xi _ { i } ,
$$

$$
\xi _ { i } = \sum _ { j = 1 } ^ { 5 } a _ { i j } \alpha _ { j } ,
$$

$B _ { i }$ , $C _ { i }$ , $B _ { i } ^ { \prime }$ , $C _ { i } ^ { \prime }$ , $B _ { i } ^ { \prime \prime }$ , and $C _ { i } ^ { \prime \prime }$ are given in columns 7–12 respectively in Table 8.1. $a _ { i j }$ are the integer multipliers of the for the $i ^ { \mathrm { t h } }$ tide given in the first five columns $\alpha _ { j }$ of Table 8.1. The arguments $\alpha _ { j }$ (l, $l ^ { \prime }$ , $F ^ { \prime }$ , $D$ or $\Omega$ ) are given in Section 5.7.2.

The routine “RG ZONT2.F”, available from the IERS Conventions website ${ < } ^ { 2 } >$ implements the model from Table 8.1.

In the past there has been some confusion over comparison of models appearing in the IERS Conventions and the values published in the Yoder et al. (1981) paper. J. Williams (2005, private communication) points out that there are four known errors in the Yoder et al. (1981) table. (1) The amplitude of term 22 (14.73-day period) should read $^ { - 5 0 }$ instead of 50. (2) The period of term 58 (1095.17-day period) should read −1095.17 instead of 1095.17, (i.e. the motion is retrograde). (3) The amplitude of term 59 (1305.47-day period) should read $- 4 4 8$ instead of −449. (4) The amplitude of term 60 (3232.85-day period) should read $+ 4 3$ instead of $^ { - 4 3 }$ .

To avoid confusion among possible tidal models, it is recommended that the terms δUT1, $\delta \Delta$ , $\delta \omega$ be followed by the model name in parenthesis, e.g. δUT1(Yoder et al., 1981).

# 8.2 Diurnal and semi-diurnal variations due to ocean tides

The routine “ORTHO EOP.F”, available from the IERS Conventions website $< { } ^ { 3 } >$ , provides corrections for modeling the diurnal and sub-diurnal variations in polar motion and UT1. It was provided by Eanes (2000) and based on Ray et al. (1994). The difference with the older model of the Conventions (1996) can exceed 100 microarcseconds for polar motion and 10 microseconds for UT1.

The model includes 71 tidal constituents with amplitudes on the order of tenths of milliarcseconds in polar motion and tens of microseconds in UT1. The coefficients of these terms have been derived by the IERS Earth Orientation Center from time series of these variations determined from “ORTHO EOP.F”, and are reported in Tables 8.2a and 8.2b for polar motion and in Tables 8.3a and 8.3b for UT1 and length of day (LOD). Previous versions of Tables 8.3a and 8.3b provided LOD with a resolution that was better than that for UT1. For consistency between the two and between these tables and Table 5.1b in Chapter 5, one digit has been removed for the LOD values in Tables 8.3a and 8.3b. Because these tables cannot be found in the code of “ORTHO EOP.F”, the IERS Earth Orientation Center has implemented them in the alternative software “interp.f” ${ < } ^ { 3 } { > }$ . The two routines agree at the level of a few microarcseconds in polar motion and a few tenths of a microsecond in UT1.

# 8.3 Tidal variations in polar motion and polar motion excitation due to long period ocean tides

Table 8.4 provides corrections for the tidal variations in polar motion and polar motion excitation with periods from 9 days to 18.6 years in terms of the amplitude $A$ and phase $\phi$ of the prograde (subscript $p$ ) and retrograde (subscript $r$ ) components defined for polar motion $\vec { \bf p } ( t )$ by:

$$
\begin{array} { r } { \vec { \bf p } ( t ) = p _ { x } ( t ) - i p _ { y } ( t ) = A _ { p } e ^ { i \phi _ { p } } e ^ { i \alpha ( t ) } + A _ { r } e ^ { i \phi _ { r } } e ^ { - i \alpha ( t ) } , } \end{array}
$$

and for polar motion excitation ${ \vec { \chi } } ( t ) \equiv { \vec { \mathbf { p } } } ( t ) + { \frac { i } { \sigma _ { 0 } } } { \frac { d { \vec { \mathbf { p } } } ( t ) } { d t } }$ by:

$$
\begin{array} { r } { \vec { \chi } ( t ) = \chi _ { x } ( t ) + i \chi _ { y } ( t ) = A _ { p } e ^ { i \phi _ { p } } e ^ { i \alpha ( t ) } + A _ { r } e ^ { i \phi _ { r } } e ^ { - i \alpha ( t ) } } \end{array}
$$

where by convention $p _ { y } ( t )$ is defined to be positive toward $9 0 ^ { \circ } \mathrm { W }$ longitude, $\chi _ { y } ( t )$ is defined to be positive toward $9 0 ^ { \circ } \mathrm { E }$ longitude, $\sigma _ { 0 }$ is the complex-valued frequency of the Chandler wobble, and $\alpha ( t )$ is the tidal argument, the expansion of which in terms of $( l , l ^ { \prime } , F , D$ , and $\Omega$ ) is given in Table 8.4. These corrections are from the Dickman and Nam (1995) long-period spherical harmonic ocean tide model as reported by Dickman and Gross (2010). To obtain variations free from tidal effects, the sum of these corrections should be subtracted from the observed polar motion and polar motion excitation values. The effect on polar motion is largest for the fortnightly tide. Empirical fits to polar motion data give (prograde, retrograde) amplitudes of (69, 89) $\mu \mathrm { a s }$ at $M _ { f }$ . The model yields (prograde, retrograde) polar motion amplitudes of (66, 74) µas at $M _ { f }$ .

Table 8.1: Zonal tide terms. Columns headed by the titles $\delta$ UT1, $\delta \Delta$ , and $\delta \omega$ provide the regularized forms of UT1, the duration of the day $\Delta$ , and the angular velocity of the Earth, $\omega$ . The units are $1 0 ^ { - 4 }$ s for UT1, $1 0 ^ { - 5 }$ s for $\Delta$ , and $1 0 ^ { - 1 4 }$ rad/s for $\omega$ . The column titled “Period” provides the approximate value of the period with a positive or negative sign to indicate a prograde or retrograde motion.   

<table><tr><td colspan="4">ARGUMENT</td><td colspan="2">PERIOD</td><td colspan="2">8UT1</td><td colspan="2">8△</td><td colspan="2">s</td></tr><tr><td>1</td><td>1</td><td>F</td><td>D</td><td>Ω</td><td>Days</td><td>B</td><td>Ci</td><td>B</td><td>C</td><td>B</td><td>C</td></tr><tr><td>1</td><td>0</td><td>2</td><td>2</td><td>2</td><td>5.64</td><td>-0.0235</td><td>0.0000</td><td>0.2617</td><td>0.0000</td><td>-0.2209</td><td>0.0000</td></tr><tr><td>2</td><td>0</td><td>2</td><td>0</td><td>1</td><td>6.85</td><td>-0.0404</td><td>0.0000</td><td>0.3706</td><td>0.0000</td><td>-0.3128</td><td>0.0000</td></tr><tr><td>2</td><td>0</td><td></td><td>0</td><td>2</td><td>6.86</td><td>-0.0987</td><td>0.0000</td><td>0.9041</td><td>0.0000</td><td>-0.7630</td><td>0.0000</td></tr><tr><td>0</td><td>0</td><td>2</td><td>2</td><td>1</td><td>7.09</td><td>-0.0508</td><td>0.0000</td><td>0.4499</td><td>0.0000</td><td>-0.3797</td><td>0.0000</td></tr><tr><td>0</td><td>0</td><td></td><td>2</td><td>2</td><td>7.10</td><td>-0.1231</td><td>0.0000</td><td>1.0904</td><td>0.0000</td><td>-0.9203</td><td>0.0000</td></tr><tr><td>1</td><td>0</td><td>2</td><td>0</td><td>0</td><td>9.11</td><td>-0.0385</td><td>0.0000</td><td>0.2659</td><td>0.0000</td><td>-0.2244</td><td>0.0000</td></tr><tr><td>1</td><td>0</td><td>2</td><td>0</td><td>1</td><td>9.12</td><td>-0.4108</td><td>0.0000</td><td>2.8298</td><td>0.0000</td><td>-2.3884</td><td>0.0000</td></tr><tr><td>1</td><td>0</td><td>2</td><td>0</td><td>2</td><td>9.13</td><td>-0.9926</td><td>0.0000</td><td>6.8291</td><td>0.0000</td><td>-5.7637</td><td>0.0000</td></tr><tr><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>9.18</td><td>-0.0179</td><td>0.0000</td><td>0.1222</td><td>0.0000</td><td>-0.1031</td><td>0.0000</td></tr><tr><td>-1</td><td>0</td><td>2</td><td>2</td><td>1</td><td>9.54</td><td>-0.0818</td><td>0.0000</td><td>0.5384</td><td>0.0000</td><td>-0.4544</td><td>0.0000</td></tr><tr><td>-1</td><td>0</td><td>2</td><td>2</td><td>2</td><td>9.56</td><td>-0.1974</td><td>0.0000</td><td>1.2978</td><td>0.0000</td><td>-1.0953</td><td>0.0000</td></tr><tr><td>1</td><td>0</td><td>0</td><td>2</td><td>0</td><td>9.61</td><td>-0.0761</td><td>0.0000</td><td>0.4976</td><td>0.0000</td><td>-0.4200</td><td>0.0000</td></tr><tr><td>2</td><td>0</td><td>2</td><td>-2</td><td>2</td><td>12.81</td><td>0.0216</td><td>0.0000</td><td>-0.1060</td><td>0.0000</td><td>0.0895</td><td>0.0000</td></tr><tr><td>0</td><td>1</td><td>2</td><td>0</td><td>2</td><td>13.17</td><td>0.0254</td><td>0.0000</td><td>-0.1211</td><td>0.0000</td><td>0.1022</td><td>0.0000</td></tr><tr><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>13.61</td><td>-0.2989</td><td>0.0000</td><td>1.3804</td><td>0.0000</td><td>-1.1650</td><td>0.0000</td></tr><tr><td>0</td><td>0</td><td>2</td><td>0</td><td>1</td><td>13.63</td><td>-3.1873</td><td>0.2010</td><td>14.6890</td><td>0.9266</td><td>-12.3974</td><td>-0.7820</td></tr><tr><td>0</td><td>0</td><td>2</td><td>0</td><td>2</td><td>13.66</td><td>-7.8468</td><td>0.5320</td><td>36.0910</td><td>2.4469</td><td>-30.4606</td><td>-2.0652</td></tr><tr><td>2</td><td>0</td><td>0</td><td>0</td><td>-1</td><td>13.75</td><td>0.0216</td><td>0.0000</td><td>-0.0988</td><td>0.0000</td><td>0.0834</td><td>0.0000</td></tr><tr><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>13.78</td><td>-0.3384</td><td>0.0000</td><td>1.5433</td><td>0.0000</td><td>-1.3025</td><td>0.0000</td></tr><tr><td>2</td><td>0</td><td>0</td><td>0</td><td>1</td><td>13.81</td><td>0.0179</td><td>0.0000</td><td>-0.0813</td><td>0.0000</td><td>0.0686</td><td>0.0000</td></tr><tr><td>0</td><td>-1</td><td>2</td><td>0</td><td>2</td><td>14.19</td><td>-0.0244</td><td>0.0000</td><td>0.1082</td><td>0.0000</td><td>-0.0913</td><td>0.0000</td></tr><tr><td>0</td><td>0</td><td>0</td><td>2</td><td>-1</td><td>14.73</td><td>0.0470</td><td>0.0000</td><td>-0.2004</td><td>0.0000</td><td>0.1692</td><td>0.0000</td></tr><tr><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>14.77</td><td>-0.7341</td><td>0.0000</td><td>3.1240</td><td>0.0000</td><td>-2.6367</td><td>0.0000</td></tr><tr><td>0</td><td>0</td><td>0</td><td>2</td><td>1</td><td>14.80</td><td>-0.0526</td><td>0.0000</td><td>0.2235</td><td>0.0000</td><td>-0.1886</td><td>0.0000</td></tr><tr><td>0</td><td>-1</td><td>0</td><td>2</td><td>0</td><td>15.39</td><td>-0.0508</td><td>0.0000</td><td>0.2073</td><td>0.0000</td><td>-0.1749</td><td>0.0000</td></tr><tr><td>1</td><td>0</td><td>2</td><td>-2</td><td>1</td><td>23.86</td><td>0.0498</td><td>0.0000</td><td>-0.1312</td><td>0.0000</td><td>0.1107</td><td>0.0000</td></tr><tr><td>1</td><td>0</td><td>2</td><td>-2</td><td>2</td><td>23.94</td><td>0.1006</td><td>0.0000</td><td>-0.2640</td><td>0.0000</td><td>0.2228</td><td>0.0000</td></tr><tr><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>25.62</td><td>0.0395</td><td>0.0000</td><td>-0.0968</td><td>0.0000</td><td>0.0817</td><td>0.0000</td></tr><tr><td>-1</td><td>0</td><td>2</td><td>0</td><td>0</td><td>26.88</td><td>0.0470</td><td>0.0000</td><td>-0.1099</td><td>0.0000</td><td>0.0927</td><td>0.0000</td></tr><tr><td>-1</td><td>0</td><td>2</td><td>0</td><td>1</td><td>26.98</td><td>0.1767</td><td>0.0000</td><td>-0.4115</td><td>0.0000</td><td>0.3473</td><td>0.0000</td></tr><tr><td>-1</td><td>0</td><td>2</td><td>0</td><td>2</td><td>27.09</td><td>0.4352</td><td>0.0000</td><td>-1.0093</td><td>0.0000</td><td>0.8519</td><td>0.0000</td></tr></table>

(Table 8.1: continued)   

<table><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>-1</td><td>27.44</td><td>0.5339</td><td>0.0000</td><td>-1.2224</td><td>0.0000</td><td>1.0317</td><td>0.0000</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>27.56</td><td>-8.4046</td><td>0.2500</td><td>19.1647</td><td>0.5701</td><td>-16.1749</td><td>-0.4811</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>27.67</td><td>0.5443</td><td>0.0000</td><td>-1.2360</td><td>0.0000</td><td>1.0432</td><td>0.0000</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>29.53</td><td>0.0470</td><td>0.0000</td><td>-0.1000</td><td>0.0000</td><td>0.0844</td><td>0.0000</td></tr><tr><td>1</td><td>-1</td><td>0</td><td>0</td><td>0</td><td>29.80</td><td>-0.0555</td><td>0.0000</td><td>0.1169</td><td>0.0000</td><td>-0.0987</td><td>0.0000</td></tr><tr><td>-1</td><td>0</td><td>0</td><td>2</td><td>-1</td><td>31.66</td><td>0.1175</td><td>0.0000</td><td>-0.2332</td><td>0.0000</td><td>0.1968</td><td>0.0000</td></tr><tr><td>-1</td><td>0</td><td>0</td><td>2</td><td>0</td><td>31.81</td><td>-1.8236</td><td>0.0000</td><td>3.6018</td><td>0.0000</td><td>-3.0399</td><td>0.0000</td></tr><tr><td>-1</td><td>0</td><td>0</td><td>2</td><td>1</td><td>31.96</td><td>0.1316</td><td>0.0000</td><td>-0.2587</td><td>0.0000</td><td>0.2183</td><td>0.0000</td></tr><tr><td>1</td><td>0</td><td>-2</td><td>2</td><td>-1</td><td>32.61</td><td>0.0179</td><td>0.0000</td><td>-0.0344</td><td>0.0000</td><td>0.0290</td><td>0.0000</td></tr><tr><td>-1</td><td>-1</td><td>0</td><td>2</td><td>0</td><td>34.85</td><td>-0.0855</td><td>0.0000</td><td>0.1542</td><td>0.0000</td><td>-0.1302</td><td>0.0000</td></tr><tr><td>0</td><td>2</td><td>2</td><td>-2</td><td>2</td><td>91.31</td><td>-0.0573</td><td>0.0000</td><td>0.0395</td><td>0.0000</td><td>-0.0333</td><td>0.0000</td></tr><tr><td>0</td><td>1</td><td>2</td><td>-2</td><td>1</td><td>119.61</td><td>0.0329</td><td>0.0000</td><td>-0.0173</td><td>0.0000</td><td>0.0146</td><td>0.0000</td></tr><tr><td>0</td><td>1</td><td>2</td><td>-2</td><td>2</td><td>121.75</td><td>-1.8847</td><td>0.0000</td><td>0.9726</td><td>0.0000</td><td>-0.8209</td><td>0.0000</td></tr><tr><td>0</td><td>0</td><td>2</td><td>-2</td><td>0</td><td>173.31</td><td>0.2510</td><td>0.0000</td><td>-0.0910</td><td>0.0000</td><td>0.0768</td><td>0.0000</td></tr><tr><td>0</td><td>0</td><td>2</td><td>-2</td><td>1</td><td>177.84</td><td>1.1703</td><td>0.0000</td><td>-0.4135</td><td>0.0000</td><td>0.3490</td><td>0.0000</td></tr><tr><td>0</td><td>0</td><td>2</td><td>-2</td><td>2</td><td>182.62</td><td>-49.7174</td><td>0.4330</td><td>17.1056</td><td>0.1490</td><td>-14.4370</td><td>-0.1257</td></tr><tr><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>182.63</td><td>-0.1936</td><td>0.0000</td><td>0.0666</td><td>0.0000</td><td>-0.0562</td><td>0.0000</td></tr><tr><td>2</td><td>0</td><td>0</td><td>-2</td><td>-1</td><td>199.84</td><td>0.0489</td><td>0.0000</td><td>-0.0154</td><td>0.0000</td><td>0.0130</td><td>0.0000</td></tr><tr><td>2</td><td>0</td><td>0</td><td>-2</td><td>0</td><td>205.89</td><td>-0.5471</td><td>0.0000</td><td>0.1670</td><td>0.0000</td><td>-0.1409</td><td>0.0000</td></tr><tr><td>2</td><td>0</td><td>0</td><td>-2</td><td>1</td><td>212.32</td><td>0.0367</td><td>0.0000</td><td>-0.0108</td><td>0.0000</td><td>0.0092</td><td>0.0000</td></tr><tr><td>0</td><td>-1</td><td>2</td><td>-2</td><td>1</td><td>346.60</td><td>-0.0451</td><td>0.0000</td><td>0.0082</td><td>0.0000</td><td>-0.0069</td><td>0.0000</td></tr><tr><td>0</td><td>1</td><td>0</td><td>0</td><td>-1</td><td>346.64</td><td>0.0921</td><td>0.0000</td><td>-0.0167</td><td>0.0000</td><td>0.0141</td><td>0.0000</td></tr><tr><td>0</td><td>-1</td><td>2</td><td>-2</td><td>2</td><td>365.22</td><td>0.8281</td><td>0.0000</td><td>-0.1425</td><td>0.0000</td><td>0.1202</td><td>0.0000</td></tr><tr><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>365.26</td><td>-15.8887</td><td>0.1530</td><td>2.7332</td><td>0.0263</td><td>-2.3068</td><td>-0.0222</td></tr><tr><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>386.00</td><td>-0.1382</td><td>0.0000</td><td>0.0225</td><td>0.0000</td><td>-0.0190</td><td>0.0000</td></tr><tr><td>1</td><td>0</td><td>0</td><td>-1</td><td>0</td><td>411.78</td><td>0.0348</td><td>0.0000</td><td>-0.0053</td><td>0.0000</td><td>0.0045</td><td>0.0000</td></tr><tr><td>2</td><td>0</td><td>-2</td><td>0</td><td>0</td><td>-1095.18</td><td>-0.1372</td><td>0.0000</td><td>-0.0079</td><td>0.0000</td><td>0.0066</td><td>0.0000</td></tr><tr><td>-2</td><td>0</td><td>2</td><td>0</td><td>1</td><td>1305.48</td><td>0.4211</td><td>0.0000</td><td>-0.0203</td><td>0.0000</td><td>0.0171</td><td>0.0000</td></tr><tr><td>-1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>3232.86</td><td>-0.0404</td><td>0.0000</td><td>0.0008</td><td>0.0000</td><td>-0.0007</td><td>0.0000</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>-3399.19</td><td>7.8998</td><td>0.0000</td><td>0.1460</td><td>0.0000</td><td>-0.1232</td><td>0.0000</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>-6798.38</td><td>-1617.2681</td><td>0.0000</td><td>-14.9471</td><td>0.0000</td><td>12.6153</td><td>0.0000</td></tr></table>

Table 8.2a: Coefficients of sin(argument) and cos(argument) of diurnal variations in pole coordinates $x _ { p }$ and $y _ { p }$ caused by ocean tides. The units are $\mu \mathrm { a s }$ ; $\gamma$ denotes GMST $+ \pi$ .   

<table><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=6>argument</td><td rowspan=1 colspan=2>Doodson</td><td rowspan=1 colspan=1>Period</td><td rowspan=1 colspan=3>xp</td><td rowspan=1 colspan=2>yp</td></tr><tr><td rowspan=1 colspan=2>Tide</td><td rowspan=1 colspan=6>Y   1  l F D m</td><td rowspan=1 colspan=2>number</td><td rowspan=1 colspan=1>(days)</td><td rowspan=1 colspan=3>sin   cos</td><td rowspan=1 colspan=2>sin  cos</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=6>1 -1  0 -2 -2 -2</td><td rowspan=1 colspan=2>117.655</td><td rowspan=1 colspan=1>1.2113611</td><td rowspan=1 colspan=3>0.0     0.9</td><td rowspan=1 colspan=2>-0.9   -0.1</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=6>1 -2  0 -2  0 -1</td><td rowspan=1 colspan=2>125.745</td><td rowspan=1 colspan=1>1.1671262</td><td rowspan=1 colspan=3>0.1     0.6</td><td rowspan=1 colspan=2>-0.6   0.1</td></tr><tr><td rowspan=1 colspan=2>2Q1</td><td rowspan=1 colspan=6>1  -2  0 -2  0 -2</td><td rowspan=1 colspan=2>125.755</td><td rowspan=1 colspan=1>1.1669259</td><td rowspan=1 colspan=3>0.3     3.4</td><td rowspan=1 colspan=2>-3.4   0.3</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=3>1  0  0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>-2 -1</td><td rowspan=1 colspan=2>127.545</td><td rowspan=1 colspan=1>1.1605476</td><td rowspan=1 colspan=3>0.1     0.8</td><td rowspan=1 colspan=2>-0.8   0.1</td></tr><tr><td rowspan=1 colspan=2>01</td><td rowspan=1 colspan=3>1  0  0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>-2 -2</td><td rowspan=1 colspan=2>127.555</td><td rowspan=1 colspan=1>1.1603495</td><td rowspan=1 colspan=3>0.5     4.2</td><td rowspan=1 colspan=2>-4.1    0.5</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=3>1 -1  0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>0 -1</td><td rowspan=1 colspan=2>135.645</td><td rowspan=1 colspan=1>1.1196993</td><td rowspan=1 colspan=3>1.2     5.0</td><td rowspan=1 colspan=2>-5.0   1.2</td></tr><tr><td rowspan=1 colspan=2>Q1</td><td rowspan=1 colspan=2>1 -1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>0 -2</td><td rowspan=1 colspan=2>135.655</td><td rowspan=1 colspan=1>1.1195148</td><td rowspan=1 colspan=3>6.2   26.3</td><td rowspan=1 colspan=2>-26.3   6.2</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>1  1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>-2 -1</td><td rowspan=1 colspan=2>137.445</td><td rowspan=1 colspan=1>1.1136429</td><td rowspan=1 colspan=3>0.2     0.9</td><td rowspan=1 colspan=2>-0.9   0.2</td></tr><tr><td rowspan=1 colspan=2>RO1</td><td rowspan=1 colspan=2>1   1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>-2 -2</td><td rowspan=1 colspan=2>137.455</td><td rowspan=1 colspan=1>1.1134606</td><td rowspan=1 colspan=3>1.3     5.0</td><td rowspan=1 colspan=2>-5.0    1.3</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>1  0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>0  0</td><td rowspan=1 colspan=2>145.535</td><td rowspan=1 colspan=1>1.0761465</td><td rowspan=1 colspan=3>-0.3    -0.8</td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>-0.3</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>1  0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>0 -1</td><td rowspan=1 colspan=2>145.545</td><td rowspan=1 colspan=1>1.0759762</td><td rowspan=1 colspan=3>9.2   25.1</td><td rowspan=1 colspan=1>-25.1</td><td rowspan=1 colspan=1>9.2</td></tr><tr><td rowspan=1 colspan=2>01</td><td rowspan=1 colspan=2>1  0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>0 -2</td><td rowspan=1 colspan=2>145.555</td><td rowspan=1 colspan=1>1.0758059</td><td rowspan=1 colspan=3>48.8  132.9</td><td rowspan=1 colspan=1>-132.9</td><td rowspan=1 colspan=1>48.8</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>1 -2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>0  0</td><td rowspan=1 colspan=2>145.755</td><td rowspan=1 colspan=1>1.0750901</td><td rowspan=1 colspan=3>-0.3    -0.9</td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>-0.3</td></tr><tr><td rowspan=1 colspan=2>TO1</td><td rowspan=1 colspan=2>1  0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>147.555</td><td rowspan=1 colspan=1>1.0695055</td><td rowspan=1 colspan=3>-0.7    -1.7</td><td rowspan=1 colspan=1>1.7</td><td rowspan=1 colspan=1>-0.7</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>153.655</td><td rowspan=1 colspan=1>1.0406147</td><td rowspan=1 colspan=1>-0.4</td><td rowspan=1 colspan=2>-0.9</td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>-0.4</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=2>155.445</td><td rowspan=1 colspan=1>1.0355395</td><td rowspan=1 colspan=1>-0.3</td><td rowspan=1 colspan=2>-0.6</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>-0.3</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>155.455</td><td rowspan=1 colspan=1>1.0353817</td><td rowspan=1 colspan=1>-1.6</td><td rowspan=1 colspan=2>-3.5</td><td rowspan=1 colspan=1>3.5</td><td rowspan=1 colspan=1>-1.6</td></tr><tr><td rowspan=1 colspan=2>M1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>155.655</td><td rowspan=1 colspan=1>1.0347187</td><td rowspan=1 colspan=1>-4.5</td><td rowspan=1 colspan=2>-9.6</td><td rowspan=1 colspan=1>9.6</td><td rowspan=1 colspan=1>-4.5</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=2>155.665</td><td rowspan=1 colspan=1>1.0345612</td><td rowspan=1 colspan=1>-0.9</td><td rowspan=1 colspan=2>-1.9</td><td rowspan=1 colspan=1>1.9</td><td rowspan=1 colspan=1>-0.9</td></tr><tr><td rowspan=1 colspan=2>X1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>157.455</td><td rowspan=1 colspan=1>1.0295447</td><td rowspan=1 colspan=1>-0.9</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1.8</td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1>-0.9</td></tr><tr><td rowspan=1 colspan=2>T1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>162.556</td><td rowspan=1 colspan=1>1.0055058</td><td rowspan=1 colspan=1>1.5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>-3.0</td><td rowspan=1 colspan=1>1.5</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>163.545</td><td rowspan=1 colspan=1>1.0028933</td><td rowspan=1 colspan=1>-0.3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-0.6</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>-0.3</td></tr><tr><td rowspan=1 colspan=2>P1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>163.555</td><td rowspan=1 colspan=1>1.0027454</td><td rowspan=1 colspan=1>26.1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>51.2</td><td rowspan=1 colspan=1>-51.2</td><td rowspan=1 colspan=1>26.1</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>164.554</td><td rowspan=1 colspan=1>1.0000001</td><td rowspan=1 colspan=1>-0.2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-0.4</td><td rowspan=1 colspan=1>0.4</td><td rowspan=1 colspan=1>-0.2</td></tr><tr><td rowspan=1 colspan=2>S1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>164.556</td><td rowspan=1 colspan=1>0.9999999</td><td rowspan=1 colspan=1>-0.6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1.2</td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1>-0.6</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>165.545</td><td rowspan=1 colspan=1>0.9974159</td><td rowspan=1 colspan=1>1.5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>-3.0</td><td rowspan=1 colspan=1>1.5</td></tr><tr><td rowspan=1 colspan=2>K1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>165.555</td><td rowspan=1 colspan=1>0.9972696</td><td rowspan=1 colspan=1>-77.5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-151.7</td><td rowspan=1 colspan=1>151.7</td><td rowspan=1 colspan=1>-77.5</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>165.565</td><td rowspan=1 colspan=1>0.9971233</td><td rowspan=1 colspan=1>-10.5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-20.6</td><td rowspan=1 colspan=1>20.6</td><td rowspan=1 colspan=1>-10.5</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>165.575</td><td rowspan=1 colspan=1>0.9969771</td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.4</td><td rowspan=1 colspan=1>-0.4</td><td rowspan=1 colspan=1>0.2</td></tr><tr><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>166.554</td><td rowspan=1 colspan=1>0.9945541</td><td rowspan=1 colspan=1>-0.6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1.2</td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1>-0.6</td></tr><tr><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>167.555</td><td rowspan=1 colspan=1>0.9918532</td><td rowspan=1 colspan=1>-1.1</td><td rowspan=1 colspan=2>-2.1</td><td rowspan=1 colspan=1>2.1</td><td rowspan=1 colspan=1>-1.1</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>TT1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>173.655</td><td rowspan=1 colspan=1>0.9669565</td><td rowspan=1 colspan=1>-0.7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1.4</td><td rowspan=1 colspan=1>1.4</td><td rowspan=1 colspan=1>-0.7</td></tr><tr><td rowspan=1 colspan=2>J1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>175.455</td><td rowspan=1 colspan=1>0.9624365</td><td rowspan=1 colspan=1>-3.5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-7.3</td><td rowspan=1 colspan=1>7.3</td><td rowspan=1 colspan=1>-3.5</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>175.465</td><td rowspan=1 colspan=1>0.9623003</td><td rowspan=1 colspan=1>-0.7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1.4</td><td rowspan=1 colspan=1>1.4</td><td rowspan=1 colspan=1>-0.7</td></tr><tr><td rowspan=1 colspan=2>S01</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>183.555</td><td rowspan=1 colspan=1>0.9341741</td><td rowspan=1 colspan=1>-0.4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1.1</td><td rowspan=1 colspan=1>1.1</td><td rowspan=1 colspan=1>-0.4</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>1  2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>185.355</td><td rowspan=1 colspan=1>0.9299547</td><td rowspan=1 colspan=1>-0.2</td><td rowspan=1 colspan=2>-0.5</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>-0.2</td></tr><tr><td rowspan=1 colspan=2>001</td><td rowspan=1 colspan=2>1   0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>2</td><td rowspan=1 colspan=1>185.555</td><td rowspan=1 colspan=1>0.9294198</td><td rowspan=1 colspan=1>-1.1</td><td rowspan=1 colspan=2>-3.4</td><td rowspan=1 colspan=1>3.4</td><td rowspan=1 colspan=1>-1.1</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>1  0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=1>185.565</td><td rowspan=1 colspan=1>0.9292927</td><td rowspan=1 colspan=1>-0.7</td><td rowspan=1 colspan=2>-2.2</td><td rowspan=1 colspan=1>2.2</td><td rowspan=1 colspan=1>-0.7</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>1  0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=3>0   185.575</td><td rowspan=1 colspan=1>0.9291657</td><td rowspan=1 colspan=1>-0.1</td><td rowspan=1 colspan=2>-0.5</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>-0.1</td></tr><tr><td rowspan=1 colspan=2>V1</td><td rowspan=1 colspan=2>1  1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=4>0  2   195.455</td><td rowspan=1 colspan=2>0.8990932   0.0</td><td rowspan=1 colspan=2>-0.6</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>0.0</td></tr><tr><td rowspan=1 colspan=4>1  1</td><td rowspan=1 colspan=6>0  2  0  1   195.465</td><td rowspan=1 colspan=6>0.8989743   0.0    -0.4     0.4   0.0</td></tr></table>

Table 8.2b: Coefficients of sin(argument) and cos(argument) of semidiurnal variations in pole coordinates $x _ { p }$ and $y _ { p }$ caused by ocean tides. The units are $\mu \mathrm { a s }$ ; $\gamma$ denotes GMST+ $\pi$   

<table><tr><td rowspan="2">Tide</td><td colspan="6">argument</td><td rowspan="2">Doodson</td><td rowspan="2">Period</td><td colspan="2">xp</td><td colspan="2">yp</td></tr><tr><td>Y</td><td>1</td><td>l</td><td>F</td><td>D Ω</td><td>number</td><td>(days)</td><td>sin</td><td>Cos</td><td>sin COs</td></tr><tr><td></td><td>2</td><td>-3</td><td>0</td><td>-2</td><td>0</td><td>-2</td><td>225.855</td><td>0.5484264</td><td>-0.5</td><td>0.0</td><td>0.6</td><td>0.2</td></tr><tr><td>2N2</td><td>2</td><td>-1</td><td>0</td><td>-2</td><td>-2</td><td>-2</td><td>227.655</td><td>0.5469695</td><td>-1.3</td><td>-0.2</td><td>1.5</td><td>0.7</td></tr><tr><td>μ2</td><td>2</td><td>-2</td><td>0</td><td>-2</td><td>0</td><td>-2</td><td>235.755</td><td>0.5377239</td><td>-6.1</td><td>-1.6</td><td>3.1</td><td>3.4</td></tr><tr><td></td><td>2</td><td>0</td><td>0</td><td>-2</td><td>-2</td><td>-2</td><td>237.555</td><td>0.5363232</td><td>-7.6</td><td>-2.0</td><td>3.4</td><td>4.2</td></tr><tr><td></td><td>2</td><td>0</td><td>1</td><td>-2</td><td>-2</td><td>-2</td><td>238.554</td><td>0.5355369</td><td>-0.5</td><td>-0.1</td><td>0.2</td><td>0.3</td></tr><tr><td></td><td>2</td><td>-1</td><td>-1</td><td>-2</td><td>0</td><td>-2</td><td>244.656</td><td>0.5281939</td><td>0.5</td><td>0.1</td><td>-0.1</td><td>-0.3</td></tr><tr><td>N2</td><td>2</td><td>-1</td><td>0</td><td>-2</td><td>0</td><td>-1</td><td>245.645</td><td>0.5274721</td><td>2.1</td><td>0.5</td><td>-0.4</td><td>-1.2</td></tr><tr><td></td><td>2</td><td>-1</td><td>0</td><td>-2</td><td>0</td><td>-2</td><td>245.655</td><td>0.5274312</td><td>-56.9</td><td>-12.9</td><td>11.1</td><td>32.9</td></tr><tr><td>V2</td><td>2</td><td>-1</td><td>1</td><td>-2</td><td>0</td><td>-2</td><td>246.654</td><td>0.5266707</td><td>-0.5</td><td>-0.1</td><td>0.1</td><td>0.3</td></tr><tr><td></td><td>2</td><td>1</td><td>0</td><td>-2</td><td>-2</td><td>-2</td><td>247.455</td><td>0.5260835</td><td>-11.0</td><td>-2.4</td><td>1.9</td><td>6.4</td></tr><tr><td></td><td>2</td><td>1</td><td>1</td><td>-2</td><td>-2</td><td>-2</td><td>248.454</td><td>0.5253269</td><td>-0.5</td><td>-0.1</td><td>0.1</td><td>0.3</td></tr><tr><td></td><td>2</td><td>-2</td><td>0</td><td>-2</td><td>2</td><td>-2</td><td>253.755</td><td>0.5188292</td><td>1.0</td><td>0.1</td><td>-0.1</td><td>-0.6</td></tr><tr><td></td><td>2</td><td>0</td><td>-1</td><td>-2</td><td>0</td><td>-2</td><td>254.556</td><td>0.5182593</td><td>1.1</td><td>0.1</td><td>-0.1</td><td>-0.7</td></tr><tr><td>M2</td><td>2</td><td>0</td><td>0</td><td>-2</td><td>0</td><td>-1</td><td>255.545</td><td>0.5175645</td><td>12.3</td><td>1.0</td><td>-1.4</td><td>-7.3</td></tr><tr><td></td><td>2</td><td>0</td><td>0</td><td>-2</td><td>0</td><td>-2</td><td>255.555</td><td>0.5175251</td><td>-330.2</td><td>-27.0</td><td>37.6</td><td>195.9</td></tr><tr><td></td><td>2</td><td>0</td><td>1</td><td>-2</td><td>0</td><td>-2</td><td>256.554</td><td>0.5167928</td><td>-1.0</td><td>-0.1</td><td>0.1</td><td>0.6</td></tr><tr><td>入2 L2</td><td>2</td><td>-1</td><td>0</td><td>-2</td><td>2</td><td>-2</td><td>263.655</td><td>0.5092406</td><td>2.5</td><td>-0.3</td><td>-0.4</td><td>-1.5</td></tr><tr><td></td><td>2</td><td>1</td><td>0</td><td>-2</td><td>0</td><td>-2</td><td>265.455</td><td>0.5079842</td><td>9.4</td><td>-1.4</td><td>-1.9</td><td>-5.6</td></tr><tr><td></td><td>2</td><td>-1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>265.655</td><td>0.5078245</td><td>-2.4</td><td>0.4</td><td>0.5</td><td>1.4</td></tr><tr><td></td><td>2</td><td>-1</td><td>0</td><td>0</td><td>0</td><td>-1</td><td>265.665</td><td>0.5077866</td><td>-1.0</td><td>0.2</td><td>0.2</td><td>0.6</td></tr><tr><td>T</td><td>2</td><td>0</td><td>-1</td><td>-2</td><td>2</td><td>-2</td><td>272.556</td><td>0.5006854</td><td>-8.5</td><td>3.5</td><td>3.3</td><td>5.1</td></tr><tr><td></td><td>2</td><td>0</td><td>0</td><td>-2</td><td>2</td><td>-2</td><td>273.555</td><td>0.5000000</td><td>-144.1</td><td>63.6</td><td>59.2</td><td>86.6</td></tr><tr><td>R2</td><td>2</td><td>0</td><td>1</td><td>-2</td><td>2</td><td>-2</td><td>274.554</td><td>0.4993165</td><td>1.2</td><td>-0.6</td><td>-0.5</td><td>-0.7</td></tr><tr><td>K2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>275.545</td><td>0.4986714</td><td>0.5</td><td>-0.2</td><td>-0.2</td><td>-0.3</td></tr><tr><td></td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>275.555</td><td>0.4986348</td><td>-38.5</td><td>19.1</td><td>17.7</td><td>23.1</td></tr><tr><td></td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-1</td><td>275.565</td><td>0.4985982</td><td>-11.4</td><td>5.8</td><td>5.3</td><td>6.9</td></tr><tr><td></td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-2</td><td>275.575</td><td>0.4985616</td><td>-1.2</td><td>0.6</td><td>0.6</td><td>0.7</td></tr><tr><td></td><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>285.455</td><td>0.4897717</td><td>-1.8</td><td>1.8</td><td>1.7</td><td>1.0</td></tr><tr><td></td><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td><td>-1</td><td>285.465</td><td>0.4897365</td><td>-0.8</td><td>0.8</td><td>0.8</td><td>0.5</td></tr><tr><td></td><td>2</td><td>0</td><td>0</td><td>2</td><td>0</td><td>2</td><td>295.555</td><td>0.4810750</td><td>-0.3</td><td>0.6</td><td>0.7</td><td>0.2</td></tr></table>

Table 8.3a: Coefficients of sin(argument) and cos(argument) of diurnal variations in UT1 and LOD caused by ocean tides. The units are $\mu \mathrm { s }$ ; $\gamma$ denotes GMST+ $\pi$ .   

<table><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=6>argument</td><td rowspan=1 colspan=2>Doodson</td><td rowspan=1 colspan=1>Period</td><td rowspan=1 colspan=4>UT1</td><td rowspan=1 colspan=2>LOD</td></tr><tr><td rowspan=1 colspan=2>Tide</td><td rowspan=1 colspan=6>Y   1  1  F  D m</td><td rowspan=1 colspan=2>number</td><td rowspan=1 colspan=1>(days)</td><td rowspan=1 colspan=4>sin   cos</td><td rowspan=1 colspan=2>sin  cos</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=3>1 -1  0</td><td rowspan=1 colspan=3>-2 -2 -2</td><td rowspan=1 colspan=2>117.655</td><td rowspan=1 colspan=1>1.2113611</td><td rowspan=1 colspan=4>0.40   -0.08</td><td rowspan=1 colspan=2>-0.4   -2.1</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=3>1 -2  0</td><td rowspan=1 colspan=3>-2  0 -1</td><td rowspan=1 colspan=2>125.745</td><td rowspan=1 colspan=1>1.1671262</td><td rowspan=1 colspan=4>0.19   -0.06</td><td rowspan=1 colspan=2>-0.3   -1.1</td></tr><tr><td rowspan=1 colspan=2>2Q1</td><td rowspan=1 colspan=3>1 -2  0</td><td rowspan=1 colspan=3>-2  0 -2</td><td rowspan=1 colspan=2>125.755</td><td rowspan=1 colspan=1>1.1669259</td><td rowspan=1 colspan=4>1.03   -0.31</td><td rowspan=1 colspan=2>-1.7   -5.6</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=3>1  0  0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>-2 -1</td><td rowspan=1 colspan=2>127.545</td><td rowspan=1 colspan=1>1.1605476</td><td rowspan=1 colspan=4>0.22   -0.07</td><td rowspan=1 colspan=2>-0.4   -1.2</td></tr><tr><td rowspan=1 colspan=2>01</td><td rowspan=1 colspan=3>1  0  0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>-2 -2</td><td rowspan=1 colspan=2>127.555</td><td rowspan=1 colspan=1>1.1603495</td><td rowspan=1 colspan=4>1.19   -0.39</td><td rowspan=1 colspan=2>-2.1   -6.4</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=3>1 -1  0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>0 -1</td><td rowspan=1 colspan=2>135.645</td><td rowspan=1 colspan=1>1.1196993</td><td rowspan=1 colspan=4>0.97   -0.47</td><td rowspan=1 colspan=2>-2.7   -5.4</td></tr><tr><td rowspan=1 colspan=2>Q1</td><td rowspan=1 colspan=2>1 -1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>0 -2</td><td rowspan=1 colspan=2>135.655</td><td rowspan=1 colspan=1>1.1195148</td><td rowspan=1 colspan=4>5.12   -2.50</td><td rowspan=1 colspan=2>-14.0  -28.7</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>1  1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>-2 -1</td><td></td><td rowspan=1 colspan=1>137.445</td><td rowspan=1 colspan=1>1.1136429</td><td rowspan=1 colspan=4>0.17   -0.09</td><td rowspan=1 colspan=2>-0.5   -1.0</td></tr><tr><td rowspan=1 colspan=2>RO1</td><td rowspan=1 colspan=2>1  1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=3>-2 -2</td><td rowspan=1 colspan=1>137.455</td><td rowspan=1 colspan=1>1.1134606</td><td rowspan=1 colspan=3>0.91</td><td rowspan=1 colspan=1>-0.47</td><td rowspan=1 colspan=1>-2.7</td><td rowspan=1 colspan=1>-5.1</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>1  0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=3>0  0</td><td rowspan=1 colspan=1>145.535</td><td rowspan=1 colspan=1>1.0761465</td><td rowspan=1 colspan=3>-0.09</td><td rowspan=1 colspan=1>0.07</td><td rowspan=1 colspan=1>0.4</td><td rowspan=1 colspan=1>0.5</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>1   0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=3>0 -1</td><td rowspan=1 colspan=1>145.545</td><td rowspan=1 colspan=1>1.0759762</td><td></td><td rowspan=1 colspan=3>3.03   -2.28</td><td rowspan=1 colspan=1>-13.3</td><td rowspan=1 colspan=1>-17.7</td></tr><tr><td rowspan=1 colspan=2>01</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>-2</td><td rowspan=1 colspan=1>145.555</td><td rowspan=1 colspan=1>1.0758059</td><td></td><td rowspan=1 colspan=3>16.02 -12.07</td><td rowspan=1 colspan=2>-70.5  -93.6</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>145.755</td><td rowspan=1 colspan=1>1.0750901</td><td></td><td rowspan=1 colspan=3>-0.10   0.08</td><td rowspan=1 colspan=2>0.5    0.6</td></tr><tr><td rowspan=1 colspan=2>T01</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>147.555</td><td rowspan=1 colspan=1>1.0695055</td><td></td><td rowspan=1 colspan=3>-0.19   0.15</td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>1.1</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=2>-2</td><td rowspan=1 colspan=1>153.655</td><td rowspan=1 colspan=2>1.0406147</td><td rowspan=1 colspan=2>-0.08</td><td rowspan=1 colspan=1>0.07</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>0.5</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>-1</td><td rowspan=1 colspan=1>155.445</td><td rowspan=1 colspan=2>1.0355395</td><td rowspan=1 colspan=2>-0.06</td><td rowspan=1 colspan=1>0.05</td><td rowspan=1 colspan=1>0.3</td><td rowspan=1 colspan=1>0.4</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>-2</td><td rowspan=1 colspan=1>155.455</td><td rowspan=1 colspan=2>1.0353817</td><td rowspan=1 colspan=2>-0.31</td><td rowspan=1 colspan=1>0.27</td><td rowspan=1 colspan=1>1.7</td><td rowspan=1 colspan=1>1.9</td></tr><tr><td rowspan=1 colspan=2>M1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>155.655</td><td rowspan=1 colspan=2>1.0347187</td><td rowspan=1 colspan=2>-0.86</td><td rowspan=1 colspan=1>0.75</td><td rowspan=1 colspan=1>4.6</td><td rowspan=1 colspan=1>5.2</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>-1</td><td rowspan=1 colspan=1>155.665</td><td rowspan=1 colspan=2>1.0345612</td><td rowspan=1 colspan=2>-0.17</td><td rowspan=1 colspan=1>0.15</td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>1.0</td></tr><tr><td rowspan=1 colspan=2>X1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>157.455</td><td rowspan=1 colspan=1>1.0295447</td><td></td><td rowspan=1 colspan=2>-0.16</td><td rowspan=1 colspan=1>0.14</td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>1.0</td></tr><tr><td rowspan=1 colspan=2>T1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=2>-2</td><td rowspan=1 colspan=1>162.556</td><td rowspan=1 colspan=1>1.0055058</td><td></td><td rowspan=1 colspan=2>0.31</td><td rowspan=1 colspan=1>-0.19</td><td rowspan=1 colspan=1>-1.2</td><td rowspan=1 colspan=1>-2.0</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=2>-1</td><td rowspan=1 colspan=1>163.545</td><td rowspan=1 colspan=1>1.0028933</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>-0.06</td><td rowspan=1 colspan=1>0.03</td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1>0.4</td></tr><tr><td rowspan=1 colspan=2>P1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=2>-2</td><td rowspan=1 colspan=1>163.555</td><td rowspan=1 colspan=2>1.0027454</td><td rowspan=1 colspan=2>5.51</td><td rowspan=1 colspan=1>-3.10</td><td rowspan=1 colspan=1>-19.4</td><td rowspan=1 colspan=1>-34.5</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=2>-2</td><td rowspan=1 colspan=1>164.554</td><td rowspan=1 colspan=2>1.0000001</td><td rowspan=1 colspan=2>-0.05</td><td rowspan=1 colspan=1>0.02</td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1>0.3</td></tr><tr><td rowspan=1 colspan=2>S1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>164.556</td><td rowspan=1 colspan=2>0.9999999</td><td rowspan=1 colspan=2>-0.13</td><td rowspan=1 colspan=1>0.07</td><td rowspan=1 colspan=1>0.4</td><td rowspan=1 colspan=1>0.8</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=1>165.545</td><td rowspan=1 colspan=2>0.9974159</td><td rowspan=1 colspan=2>0.35</td><td rowspan=1 colspan=1>-0.17</td><td rowspan=1 colspan=1>-1.1</td><td rowspan=1 colspan=1>-2.2</td></tr><tr><td rowspan=1 colspan=2>K1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>165.555</td><td rowspan=1 colspan=2>0.9972696</td><td rowspan=1 colspan=2>-17.62</td><td rowspan=1 colspan=1>8.55</td><td rowspan=1 colspan=1>53.9</td><td rowspan=1 colspan=1>111.0</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>165.565</td><td rowspan=1 colspan=2>0.9971233</td><td rowspan=1 colspan=2>-2.39</td><td rowspan=1 colspan=1>1.16</td><td rowspan=1 colspan=1>7.3</td><td rowspan=1 colspan=1>15.1</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>-2</td><td rowspan=1 colspan=1>165.575</td><td rowspan=1 colspan=2>0.9969771</td><td rowspan=1 colspan=2>0.05</td><td rowspan=1 colspan=1>-0.03</td><td rowspan=1 colspan=1>-0.2</td><td rowspan=1 colspan=1>-0.3</td></tr><tr><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=3>0   166.554</td><td rowspan=1 colspan=2>0.9945541</td><td rowspan=1 colspan=2>-0.14</td><td rowspan=1 colspan=1>0.06</td><td rowspan=1 colspan=1>0.4</td><td rowspan=1 colspan=1>0.9</td></tr><tr><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=2>2</td><td rowspan=1 colspan=1>167.555</td><td rowspan=1 colspan=2>0.9918532</td><td></td><td rowspan=1 colspan=1>-0.27</td><td rowspan=1 colspan=1>0.11</td><td rowspan=1 colspan=1>0.7</td><td rowspan=1 colspan=1>1.7</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>TT1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>173.655</td><td rowspan=1 colspan=2>0.9669565</td><td></td><td rowspan=1 colspan=1>-0.29</td><td rowspan=1 colspan=1>0.04</td><td rowspan=1 colspan=1>0.3</td><td rowspan=1 colspan=1>1.9</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>J</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>175.455</td><td rowspan=1 colspan=2>0.9624365</td><td></td><td rowspan=1 colspan=1>-1.61</td><td rowspan=1 colspan=1>0.19</td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1>10.5</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=3>-1   175.465</td><td rowspan=1 colspan=2>0.9623003</td><td></td><td rowspan=1 colspan=1>-0.32</td><td rowspan=1 colspan=1>0.04</td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1>2.1</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S01</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=3>0   183.555</td><td rowspan=1 colspan=2>0.9341741</td><td></td><td rowspan=1 colspan=1>-0.41</td><td rowspan=1 colspan=1>-0.01</td><td rowspan=1 colspan=1>-0.0</td><td rowspan=1 colspan=1>2.7</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=3>0   185.355</td><td rowspan=1 colspan=3>0.9299547</td><td rowspan=1 colspan=1>-0.21</td><td rowspan=1 colspan=1>-0.01</td><td rowspan=1 colspan=1>-0.0</td><td rowspan=1 colspan=1>1.4</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>001</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=3>2   185.555</td><td rowspan=1 colspan=3>0.9294198</td><td rowspan=1 colspan=1>-1.44</td><td rowspan=1 colspan=1>-0.04</td><td rowspan=1 colspan=1>-0.3</td><td rowspan=1 colspan=1>9.7</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=3>1   185.565</td><td rowspan=1 colspan=3>0.9292927</td><td rowspan=1 colspan=1>-0.92</td><td rowspan=1 colspan=1>-0.02</td><td rowspan=1 colspan=1>-0.2</td><td rowspan=1 colspan=1>6.2</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=3>0   185.575</td><td rowspan=1 colspan=3>0.9291657</td><td rowspan=1 colspan=1>-0.19</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>-0.0</td><td rowspan=1 colspan=1>1.3</td></tr><tr><td rowspan=1 colspan=2>V1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=3>0  2  0</td><td rowspan=1 colspan=3>2   195.455</td><td rowspan=1 colspan=7>0.8990932  -0.40   -0.02   -0.2    2.8</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=6>0  2  0  1   195.465</td><td rowspan=1 colspan=7>0.8989743  -0.25  -0.02  -0.1    1.8</td></tr></table>

Table 8.3b: Coefficients of sin(argument) and cos(argument) of semidiurnal variations in UT1 and LOD caused by ocean tides. The units are $\mu \mathrm { s }$ ; $\gamma$ denotes GMST+ $\pi$ .   

<table><tr><td rowspan="2">Tide</td><td colspan="6">argument</td><td rowspan="2">Doodson</td><td colspan="2">Period UT1</td><td colspan="2">LOD</td></tr><tr><td>Y</td><td>l</td><td>l&#x27; F</td><td>D</td><td>Ω</td><td>number</td><td>(days)</td><td>sin</td><td>COs</td><td>sin COS</td></tr><tr><td rowspan="5">2N2 μ2</td><td>2</td><td>-3</td><td>0</td><td>-2</td><td>0 -2</td><td>225.855</td><td>0.5484264</td><td>-0.09</td><td>-0.01</td><td>-0.1</td><td>1.0</td></tr><tr><td>2</td><td>-1</td><td>0</td><td>-2</td><td>-2 -2</td><td>227.655</td><td>0.5469695</td><td>-0.22</td><td>-0.03</td><td>-0.4</td><td>2.6</td></tr><tr><td>2</td><td>-2</td><td>0</td><td>-2</td><td>0 -2</td><td>235.755</td><td>0.5377239</td><td>-0.64</td><td>-0.18</td><td>-2.1</td><td>7.4</td></tr><tr><td>2</td><td>0</td><td>0</td><td>-2</td><td>-2</td><td>-2 237.555</td><td>0.5363232</td><td>-0.74</td><td>-0.22</td><td>-2.6</td><td>8.7</td></tr><tr><td>2</td><td>0</td><td>1</td><td>-2</td><td>-2</td><td>-2 238.554</td><td>0.5355369</td><td>-0.05</td><td>-0.02</td><td>-0.2</td><td>0.6</td></tr><tr><td></td><td>2</td><td>-1 -1</td><td></td><td>-2</td><td>0 -2</td><td>244.656</td><td>0.5281939</td><td>0.03</td><td>0.01</td><td>0.2</td><td>-0.4</td></tr><tr><td></td><td>2</td><td>-1</td><td>0</td><td>-2</td><td>0 -1</td><td>245.645</td><td>0.5274721</td><td>0.14</td><td>0.06</td><td>0.7</td><td>-1.7</td></tr><tr><td>N2</td><td>2</td><td>-1</td><td>0</td><td>-2</td><td>0 -2</td><td>245.655</td><td>0.5274312</td><td>-3.79</td><td>-1.56</td><td>-18.6</td><td>45.2</td></tr><tr><td></td><td>2</td><td>-1</td><td>1</td><td>-2</td><td>0 -2</td><td>246.654</td><td>0.5266707</td><td>-0.03</td><td>-0.01</td><td>-0.2</td><td>0.4</td></tr><tr><td>V2</td><td>2</td><td>1</td><td>0</td><td>-2</td><td>-2 -2</td><td>247.455</td><td>0.5260835</td><td>-0.70</td><td>-0.30</td><td>-3.6</td><td>8.3</td></tr><tr><td rowspan="5"></td><td>2</td><td>1</td><td>1</td><td>-2</td><td>-2 -2</td><td>248.454</td><td>0.5253269</td><td>-0.03</td><td>-0.01</td><td>-0.2</td><td>0.4</td></tr><tr><td>2</td><td>-2</td><td>0</td><td>-2</td><td>2 -2</td><td>253.755</td><td>0.5188292</td><td>0.05</td><td>0.02</td><td>0.3</td><td>-0.6</td></tr><tr><td>2</td><td>0</td><td>-1</td><td>-2</td><td>0 -2</td><td>254.556</td><td>0.5182593</td><td>0.06</td><td>0.03</td><td>0.3</td><td>-0.7</td></tr><tr><td>2</td><td>0</td><td>0</td><td>-2</td><td>0 -1</td><td>255.545</td><td>0.5175645</td><td>0.60</td><td>0.27</td><td>3.2</td><td>-7.3</td></tr><tr><td>2</td><td>0</td><td>0</td><td>-2</td><td>0 -2</td><td>255.555</td><td>0.5175251</td><td>-16.19</td><td>-7.25</td><td>-86.8</td><td>196.6</td></tr><tr><td>M2</td><td>2</td><td>0</td><td>1</td><td>-2</td><td>0 -2</td><td>256.554</td><td>0.5167928</td><td>-0.05</td><td>-0.02</td><td>-0.3</td><td>0.6</td></tr><tr><td>X2</td><td>2</td><td>-1</td><td>0</td><td>-2</td><td>2 -2</td><td>263.655</td><td>0.5092406</td><td>0.11</td><td>0.03</td><td>0.4</td><td>-1.4</td></tr><tr><td>L2</td><td>2</td><td>1 0</td><td>-2</td><td></td><td>0 -2</td><td>265.455</td><td>0.5079842</td><td>0.42</td><td>0.12</td><td>1.4</td><td>-5.3</td></tr><tr><td></td><td>2 -1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>265.655</td><td>0.5078245</td><td>-0.11</td><td>-0.03</td><td>-0.4</td><td>1.3</td></tr><tr><td></td><td>2 -1</td><td>0</td><td>0</td><td>0</td><td>-1</td><td>265.665</td><td>0.5077866</td><td>-0.05</td><td>-0.01</td><td>-0.2</td><td>0.6</td></tr><tr><td>T</td><td>2</td><td>0 -1</td><td></td><td>-2</td><td>2 -2</td><td>272.556</td><td>0.5006854</td><td>-0.44</td><td>-0.02</td><td>-0.2</td><td>5.5</td></tr><tr><td>S R2</td><td>2</td><td>0</td><td>0 -2</td><td></td><td>2 -2</td><td>273.555</td><td>0.5000000</td><td>-7.55</td><td>-0.16</td><td>-2.0</td><td>94.8</td></tr><tr><td></td><td>2</td><td>0 1</td><td>-2</td><td></td><td>2 -2</td><td>274.554</td><td>0.4993165</td><td>0.06</td><td>0.00</td><td>0.0</td><td>-0.8</td></tr><tr><td rowspan="5">K2</td><td>2 0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>275.545</td><td>0.4986714</td><td>0.03</td><td>0.00</td><td>-0.0</td><td>-0.3</td></tr><tr><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0 275.555</td><td>0.4986348</td><td>-2.10</td><td>0.04</td><td>0.5</td><td>26.5</td></tr><tr><td>2</td><td>0</td><td>0</td><td>0</td><td>0 -1</td><td>275.565</td><td>0.4985982</td><td>-0.63</td><td>0.01</td><td>0.2</td><td>7.9</td></tr><tr><td>2</td><td>0</td><td>0</td><td>0</td><td>0 -2</td><td>275.575</td><td>0.4985616</td><td>-0.07</td><td>0.00</td><td>0.0</td><td>0.9</td></tr><tr><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0 285.455</td><td>0.4897717</td><td>-0.15</td><td>0.04</td><td>0.5</td><td>1.9</td></tr><tr><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td><td>-1</td><td>285.465</td><td>0.4897365</td><td>-0.06</td><td>0.02</td><td>0.2</td><td>0.8</td></tr><tr><td></td><td>2 0</td><td>0</td><td>2</td><td>0</td><td>2</td><td>295.555</td><td>0.4810750</td><td>-0.05</td><td>0.02</td><td>0.2</td><td>0.6</td></tr></table>

Table 8.4: Ocean tidal variations in polar motion and polar motion excitation.   

<table><tr><td rowspan="2">Tide Argument</td><td colspan="4"></td><td rowspan="2"></td><td colspan="2">Polar Motion Prograde</td><td colspan="2">Retrograde</td><td colspan="2">Prograde</td><td colspan="2">Polar Motion Excitation Retrograde</td></tr><tr><td>lFDΩ</td><td></td><td></td><td>Period (days)</td><td>amp (μas)</td><td>phase （）</td><td>ampphase</td><td>（）</td><td>amp phase</td><td>amp</td><td></td><td>phase</td></tr><tr><td>mtm</td><td>1</td><td>0</td><td>2</td><td>0 1</td><td>9.12</td><td></td><td>4.43 -112.62</td><td>(μas) 5.57</td><td>21.33</td><td>(μas) 205.83</td><td>（） 67.21</td><td>(μas)</td><td>（）</td></tr><tr><td>Mtm</td><td>1</td><td>0</td><td>2</td><td>0 2</td><td>9.13</td><td>10.72 -112.56</td><td></td><td>13.48</td><td>21.30</td><td>497.59</td><td>67.27</td><td>269.95 652.59</td><td>21.17 21.14</td></tr><tr><td>mf</td><td>0</td><td>0</td><td>2</td><td>0 1</td><td>13.63</td><td>27.35</td><td>-91.42</td><td>30.59</td><td>13.31</td><td>841.32</td><td>88.42</td><td>1002.12</td><td>13.15</td></tr><tr><td>Mf</td><td>0</td><td>0</td><td>2</td><td>0 2</td><td>13.66</td><td>66.09</td><td>-91.31</td><td>73.86</td><td>13.27</td><td>2028.73</td><td></td><td>88.53 2414.94</td><td>13.11</td></tr><tr><td>Msf</td><td>00</td><td></td><td>0</td><td>2 0</td><td>14.77</td><td>5.94</td><td>-87.13</td><td>6.42</td><td>11.75</td><td>168.13</td><td>92.70</td><td>194.74</td><td>11.60</td></tr><tr><td>Mm</td><td>1</td><td>.00</td><td></td><td>0 0</td><td>27.56</td><td>43.74</td><td>-56.70</td><td>31.12</td><td>-0.91</td><td>643.61</td><td>123.13</td><td>520.16</td><td>-1.06</td></tr><tr><td>Msm</td><td>-1</td><td>0</td><td>0</td><td>2 0</td><td>31.81</td><td>8.85</td><td>-51.11</td><td>5.42</td><td>-4.21</td><td>111.62</td><td>128.72</td><td>79.23</td><td>-4.36</td></tr><tr><td>Ssa</td><td>0</td><td>0</td><td>2</td><td>-2 2</td><td>182.62</td><td>86.48</td><td>-20.30</td><td>99.77</td><td>175.57</td><td>118.56</td><td>159.42</td><td>336.32</td><td>175.46</td></tr><tr><td>Sa</td><td>0</td><td>1</td><td>0</td><td>0 0</td><td>365.26</td><td>17.96</td><td>-17.38</td><td>152.15 170.60</td><td></td><td></td><td>3.33 161.60</td><td>332.53 170.51</td><td></td></tr><tr><td>Mn</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1 -6798.38 208.17</td><td></td><td></td><td>166.89 186.98 166.67</td><td></td><td></td><td>221.43 166.88</td><td>175.07 166.68</td><td></td></tr></table>

# References

Dickman, S. R. and Nam, Y. S., 1995, “Revised predictions of long-period ocean tidal effects on Earth’s rotation rate,” J. Geophys. Res., 100(B5), pp. 8233–8243, doi:10.1029/95JB00028.   
Dickman, S. R. and Gross, R. S., 2010, “Rotational evaluation of a long-period spherical harmonic ocean tide model,” J. Geod., 84(7), pp. 457–464, doi: 10.1007/s00190-010-0383-5.   
Eanes, R., 2000, personal communication.   
Gross, R. S., 2009, “Ocean tidal effects on Earth rotation,” J. Geodyn., 48(3–5), pp. 219–225, doi: 10.1016/j.jog.2009.09.016.   
Kantha, L. H., Stewart, J. S., and Desai, S. D., 1998, “Long-period lunar fortnightly and monthly ocean tides,” J. Geophys. Res., 103(C6), pp. 12639– 12647, doi:10.1029/98JC00888.   
Ray, R. D., Steinberg, D. J., Chao, B. F., and Cartwright, D. E., 1994, “Diurnal and semidiurnal variations in the Earth’s rotation rate induced by oceanic tides,” Science, 264(5160), pp. 830–832, doi:10.1126/science.264.5160.830.   
Sailor, R. V. and Dziewonski, A. M., 1978, “Measurements and interpretation of normal mode attentuation,” Geophys. J. Roy. astr. Soc., 53(3), pp. 559–581, doi:10.1111/j.1365-246X.1978.tb03760.x.   
Wahr, J. and Bergen, Z., 1986, “The effects of mantle anelasticity on nutations, Earth tides, and tidal variations in rotation rate,” Geophys. J. Roy. astr. Soc., 87(2), pp. 633–668, doi:10.1111/j.1365-246X.1986.tb06642.x.   
Yoder, C. F., Williams, J. G., and Parke, M. E., 1981, “Tidal variations of Earth rotation,” J. Geophys. Res., 86(B2), pp. 881–891, doi:10.1029/JB086iB02p00881.

Techniques operated for the realization of the IERS reference systems make use of electromagnetic signals received on the surface of the Earth. During their transit of the atmosphere, the signals experience delays which must be modeled in the analysis software. This chapter presents models for the propagation of optical signals in the troposphere (9.1), for radio signals in the troposphere (9.2) and for radio signals in the ionosphere (9.4). For Doppler techniques which use timedifferenced phases as observables, the models presented in this chapter should be time-differenced as well.

# 9.1 Tropospheric model for optical techniques

The accuracy of satellite and lunar laser ranging (SLR & LLR) is greatly affected by the residual errors in modeling the effect of signal propagation through the troposphere and stratosphere. Although several models for atmospheric correction have been developed, the more traditional approach in LR data analysis uses a model developed in the 1970s (Marini and Murray, 1973). Mendes et al. (2002) pointed out some limitations in that model, namely the modeling of the elevation dependence of the zenith atmospheric delay, i.e. the mapping function (MF) component of the model. The MFs developed by Mendes et al. (2002) represent a significant improvement over the MF in the Marini-Murray model and other known MFs. Of particular interest is the ability of the new MFs to be used in combination with any zenith delay (ZD) model to predict the atmospheric delay in the line-of-sight direction. Subsequently, Mendes and Pavlis (2004) developed a more accurate ZD model, applicable to the range of wavelengths used in modern LR instrumentation. The combined set of the new mapping function and the new ZD model were adopted in October 2006 by the Analysis Working Group of the International Laser Ranging Service (ILRS) as the new standard model to be used for the analysis of LR data starting January 1, 2007. The alternative to correct the atmospheric delay using two-color ranging systems is still at an experimental stage.

# 9.1.1 Zenith delay models

The atmospheric propagation delay experienced by a laser signal in the zenith direction is defined as

$$
d _ { a t m } ^ { z } = 1 0 ^ { - 6 } \int _ { r _ { s } } ^ { r _ { a } } N d z = \int _ { r _ { s } } ^ { r _ { a } } \left( n - 1 \right) d z ,
$$

or, if we split the zenith delay into hydrostatic ( $d _ { h } ^ { z }$ ) and non-hydrostatic ( $d _ { n h } ^ { z }$ ) components,

$$
d _ { a t m } ^ { z } = d _ { h } ^ { z } + d _ { n h } ^ { z } = 1 0 ^ { - 6 } \int _ { r _ { s } } ^ { r _ { a } } N _ { h } d z + 1 0 ^ { - 6 } \int _ { r _ { s } } ^ { r _ { a } } N _ { n h } d z ,
$$

where $N = ( n - 1 ) \times 1 0 ^ { 6 }$ is the (total) group refractivity of moist air, $n$ is the (total) refractive index of moist air, $N _ { h }$ and $N _ { n h }$ are the hydrostatic and the nonhydrostatic components of the refractivity, $r _ { s }$ is the geocentric radius of the laser station, $r _ { a }$ is the geocentric radius of the top of the (neutral) atmosphere, and $d _ { a t m } ^ { \boldsymbol { z } }$ and $d z$ have length units.

In the last few years, the computation of the group refractivity at optical wavelengths has received special attention and, as a consequence, the International Association of Geodesy (IAG) (IUGG, 1999) recommended a new procedure to compute the group refractivity, following Ciddor (1996) and Ciddor and Hill (1999). Based on this procedure, Mendes and Pavlis (2004) derived closed-form expressions to compute the zenith delay. For the hydrostatic component, we have

$$
d _ { h } ^ { z } = 0 . 0 0 2 4 1 6 5 7 9 { \frac { f _ { h } ( \lambda ) } { f _ { s } ( \phi , H ) } } P _ { s } ,
$$

where $d _ { h } ^ { z }$ is the zenith hydrostatic delay, in meters, and $P _ { s }$ is the surface barometric pressure, in hPa. The function $f _ { s } ( \phi , H )$ is given by

$$
f _ { s } ( \phi , H ) = 1 - 0 . 0 0 2 6 6 \cos 2 \phi - 0 . 0 0 0 0 0 2 8 H ,
$$

where $\phi$ is the geodetic latitude of the station and $H$ is the geodetic height of the station in meters ${ < } ^ { 1 } >$ , $f _ { h } \left( \lambda \right)$ is the dispersion equation for the hydrostatic component

$$
f _ { h } \left( \lambda \right) = { 1 0 } ^ { - 2 } \times \left[ { k _ { 1 } ^ { * } \frac { \left( { k _ { 0 } + \sigma ^ { 2 } } \right) } { \left( { k _ { 0 } - \sigma ^ { 2 } } \right) ^ { 2 } } + k _ { 3 } ^ { * } \frac { \left( { k _ { 2 } + \sigma ^ { 2 } } \right) } { \left( { k _ { 2 } - \sigma ^ { 2 } } \right) ^ { 2 } } } \right] C _ { \mathrm { C O _ { 2 } } } ,
$$

with $k _ { 0 } = \mathrm { 2 3 8 . 0 1 8 5 ~ \mu m ^ { - 2 } }$ , $k _ { 2 } = 5 7 . 3 6 2 ~ \mu \mathrm { m } ^ { - 2 }$ , $k _ { 1 } ^ { * } = 1 9 9 9 0 . 9 7 5 \ \mu \mathrm { m } ^ { - 2 }$ , and $k _ { 3 } ^ { * } =$ $5 7 9 . 5 5 1 7 4 ~ \mu \mathrm { m } ^ { - 2 }$ , $\sigma$ is the wave number $\sigma = \lambda ^ { - 1 }$ , where $\lambda$ is the wavelength, in $\mu \mathrm { m }$ ), $C _ { C O _ { 2 } } = 1 + 0 . 5 3 4 \times 1 0 ^ { - 6 } \left( x _ { c } - 4 5 0 \right)$ , and $x _ { c }$ is the carbon dioxide (CO $^ 2$ ) content, in ppm. In the conventional formula, a CO $^ 2$ content of 375 ppm should be used, in line with the IAG recommendations, thus $C _ { \mathrm { C O _ { 2 } } } = 0 . 9 9 9 9 5 9 9 5$ should be used.

For the non-hydrostatic component, we have:

$$
d _ { n h } ^ { z } = 1 0 ^ { - 4 } \left( 5 . 3 1 6 f _ { n h } ( \lambda ) - 3 . 7 5 9 f _ { h } ( \lambda ) \right) \frac { \mathrm { e _ { s } } } { f _ { s } ( \phi , H ) } ,
$$

where $d _ { n h } ^ { z }$ is the zenith non-hydrostatic delay, in meters, and $e _ { s }$ is the surface water vapor pressure, in hPa. $f _ { n h }$ is the dispersion formula for the non-hydrostatic component:

$$
f _ { n h } \left( \lambda \right) = 0 . 0 0 3 1 0 1 \left( \omega _ { 0 } + 3 \omega _ { 1 } \sigma ^ { 2 } + 5 \omega _ { 2 } \sigma ^ { 4 } + 7 \omega _ { 3 } \sigma ^ { 6 } \right) ,
$$

where $\omega _ { 0 } = 2 9 5 . 2 3 5$ , $\omega _ { 1 } = 2 . 6 4 2 2 ~ \mu \mathrm { m } ^ { 2 }$ , $\omega _ { 2 } = - 0 . 0 3 2 3 8 0 ~ \mu \mathrm { m } ^ { 4 }$ , and $\omega _ { 3 } = 0 . 0 0 4 0 2 8$ $\mu \mathrm { m } ^ { 6 }$ .

The subroutine FCUL ZTD HPA.F to compute the total zenith delay is available at ${ < } ^ { 2 } >$ .

From the assessment of the zenith models against ray tracing for the most used wavelengths in LR, it can be concluded that these zenith delay models have overall rms errors for the total zenith delay below $1 \mathrm { m m }$ across the whole frequency spectrum (Mendes and Pavlis, 2003; Mendes and Pavlis, 2004).

# 9.1.2 Mapping function

Due to the small contribution of water vapor to atmospheric refraction at visible wavelengths, we can consider a single MF for laser ranging. In this case, we have:

$$
d _ { a t m } = d _ { a t m } ^ { z } \cdot m ( e ) ,
$$

where $d _ { a t m } ^ { z }$ is the total zenith propagation delay and $m ( e )$ the (total) MF. Mendes et al. (2002) derived a MF, named FCULa, based on a truncated form of the continued fraction in terms of $1 / s i n ( e )$ (Marini, 1972), normalized to unity at the zenith

$$
m ( e ) = \frac { 1 + \displaystyle \frac { a _ { 1 } } { 1 + \displaystyle \frac { a _ { 2 } } { 1 + a _ { 3 } } } } { \sin e + \displaystyle \frac { a _ { 1 } } { \sin e + \displaystyle \frac { a _ { 2 } } { \sin e + \displaystyle \frac { a _ { 2 } } { \sin e + a _ { 3 } } } } } .
$$

Note that the same formula is used for radio techniques, but with different variables, see Equation (9.13). The FCULa MF is based on ray tracing through one full year of radiosonde data from 180 globally distributed stations. It is valid for a wide range of wavelengths from $0 . 3 5 5 \ \mu \mathrm { m }$ to $1 . 0 6 4 \ \mu \mathrm { m }$ (Mendes and Pavlis, 2003) and for elevation angles greater than 3 degrees, if we neglect the contribution of horizontal refractivity gradients. The coefficients $a _ { i }$ (i=1,2,3) have the following mathematical formulation:

Table 9.1: Coefficients ( $a _ { i j }$ ) for the FCULa mapping function, see Equation (9.10). Coefficients ( $a _ { i 1 }$ ) are in $C ^ { - 1 }$ and coefficients ( $a _ { i 3 }$ ) in $m ^ { - 1 }$ .   

<table><tr><td>aij</td><td>FCULa</td></tr><tr><td>a10 a11 a12</td><td>(12100.8±1.9) ×10-7 (1729.5±4.3) ×10-9 (319.1±3.1) ×10-7 ×10-11</td></tr><tr><td>α13 a20 a21</td><td>(-1847.8±6.5) (30496.5±6.6) × 10-7 (234.6±1.5) × 10-8 (-103.5±1.1) ×10-6</td></tr><tr><td>a22 a23</td><td>(-185.6±2.2) ×10-10</td></tr><tr><td>a30 a31 a32</td><td>(6877.7±1.2) × 10-5 (197.2±2.8) × 10-7 (-345.8±2.0) × 10-5 (106.0±4.2) × 10-9</td></tr></table>

$$
a _ { i } = a _ { i 0 } + a _ { i 1 } t _ { s } + a _ { i 2 } \cos \phi + a _ { i 3 } H ,
$$

where $t _ { s }$ is the temperature at the station in Celsius degrees, $H$ is the geodetic height of the station, in meters, and the coefficients are given in Table 1, see Mendes et al. (2002) for details. The subroutine FCUL A.F to compute the FCULa mapping function is available at ${ < } ^ { 2 } >$ .

The new mapping functions represent a significant improvement over other mapping functions available and have the advantage of being easily combined with different zenith delay models. The analysis of two years of SLR data from LAGEOS and LAGEOS 2 indicate a clear improvement in the estimated station heights $8 \%$ reduction in variance), while the simultaneously adjusted tropospheric zenith delay biases were all consistent with zero (Mendes et al., 2002).

For users who do not have extreme accuracy requirements or do not know the station temperature, the FCULb mapping function, which depends on the station location and the day of the year, has been developed, see Mendes et al. (2002) for details. The subroutine FCUL B.F to compute the FCULb mapping function is available at ${ < } ^ { 2 } { > }$ .

# 9.1.3 Future developments

The accuracy of the new atmospheric delay models are still far from the accuracy required for global climate change studies. The goal as set forth by the International Laser Ranging Service (ILRS) is better than one millimeter. The LR community has been looking into ways to achieve that accuracy. One significant component that is missing from the above models is to account for the effect of horizontal gradients in the atmosphere, an error source that contributes up to 5 cm of delay at low elevation angles. Ranging at low elevation angles improves the de-correlation of errors in the vertical coordinate with errors in the measurement process (biases). Stations thus strive to range as low as possible, thence the need for model improvements.

Global meteorological fields are now becoming more readily accessible, with higher spatio-temporal resolution, better accuracy and more uniform quality. This is primarily due to the availability of satellite observations with global coverage twice daily. Hulley and Pavlis (2007) developed a new technique, and tested it with real data, computing the total atmospheric delay, including horizontal gradients, via three-dimensional atmospheric ray tracing (3D ART) with meteorological fields from the Atmospheric Infrared Sounder (AIRS). This technique has already been tested and applied to two years of SLR data from LAGEOS 1 and 2, and for ten core, globally-distributed SLR stations. Replacing the atmospheric corrections estimated from the Mendes-Pavlis ZD and MF models with 3D ART resulted in reducing the variance of the SLR range residuals by up to $2 5 \%$ for all the data used in the analysis. As of May 2007, an effort is in progress to establish a service that will compute these corrections for all of the collected SLR and LLR data in the future. Once this service is in place, it is expected that this new approach will be adopted as the standard for SLR and LLR data reductions.

# 9.2 Tropospheric model for radio techniques

The non-dispersive delay imparted by the atmosphere on a radio signal up to 30 GHz in frequency, which reaches a magnitude of about $2 . 3 \textrm { m }$ at sea level, is conveniently divided into “hydrostatic” and “wet” components. The hydrostatic delay is caused by the refractivity of the dry gases (mainly $N _ { 2 }$ and $O _ { 2 }$ ) in the troposphere and by most of the nondipole component of the water vapor refractivity. The rest of the water vapor refractivity is responsible for most of the wet delay. The hydrostatic delay component accounts for roughly $9 0 \%$ of the total delay at any given site globally, but can vary between about 80 and $1 0 0 \%$ depending on location and time of year. It can be accurately computed $a$ priori based on reliable surface pressure data using the formula of Saastamoinen (1972) as given by Davis et al. (1985):

$$
D _ { h z } = \frac { [ ( 0 . 0 0 2 2 7 6 8 \pm 0 . 0 0 0 0 0 0 5 ) ] P _ { 0 } } { f _ { s } ( \phi , H ) }
$$

where $D _ { h z }$ is the zenith hydrostatic delay in meters, $P _ { 0 }$ is the total atmospheric pressure in hPa (equivalent to millibars) at the antenna reference point (e.g. antenna phase center for Global Positioning System, the intersection of the axes of rotation for VLBI 3), and the function $f _ { s } ( \phi , H )$ is given in Equation (9.4).

There is currently no simple method to estimate an accurate $a$ priori value for the wet tropospheric delay, although research continues into the use of external monitoring devices (such as water vapor radiometers) for this purpose. So, in most precise applications where sub-decimeter accuracy is sought, the residual delay must usually be estimated with the other geodetic quantities of interest. The estimation is facilitated by a simple parameterization of the tropospheric delay, where the line-of-sight delay, $D _ { L }$ , is expressed as a function of four parameters as follows:

$$
D _ { L } = m _ { h } ( e ) D _ { h z } + m _ { w } ( e ) D _ { w z } + m _ { g } ( e ) [ G _ { N } \cos ( a ) + G _ { E } \sin ( a ) ] .
$$

The four parameters in this expression are the zenith hydrostatic delay, $D _ { h z }$ , the zenith wet delay, $D _ { w z }$ , and a horizontal delay gradient with components $G _ { N }$ and $G _ { E }$ . $m _ { h }$ , $m _ { w }$ and $m _ { g }$ are the hydrostatic, wet, and gradient mapping functions, respectively, and $e$ is the elevation angle of the observation direction in vacuum. $a$ is the azimuth angle in which the signal is received, measured east from north.

Horizontal gradient parameters are needed to account for a systematic component in the N/S direction towards the equator due to the atmospheric bulge (MacMillan and Ma, 1997), which are about $- 0 . 5 / + 0 . 5$ mm at mid-latitudes in the northern and southern hemispheres, respectively. They also capture the effects of random components in both directions due to weather systems. Failing to model gradients in radiometric analyses can lead to systematic errors in the scale of the estimated terrestrial reference frame at the level of about 1 ppb, as well as cause latitude and declination offsets in station and source positions, the latter also depending on the station distribution (Titov, 2004). A mean a priori model for the gradients which is based on re-analysis data of the European Centre for Medium-Range Weather

Forecasts (ECMWF) is provided by the subroutine APG.F available at ${ < } ^ { 4 } >$ and ${ < } ^ { 2 } { > }$ . However, an a priori model cannot replace the (additional) estimation of gradient parameters, if observations at elevation angles below $1 5 ^ { \circ }$ are analyzed. In the case of GPS analyses, such low-elevation data could be deweighted because of multipath effects.

Horizontal tropospheric gradients can reach or exceed 1 mm and their estimation was shown by Chen and Herring (1997) and MacMillan (1995) to be beneficial for VLBI, and by Bar-Sever et al. (1998) to be beneficial for GPS. Chen and Herring (1997) propose to use $m _ { g } ( e ) \ = \ 1 / ( \sin e \tan e + 0 . 0 0 3 2 )$ . Unlike other gradient mapping functions this equation is not affected by singularity at very low elevations (below $5 ^ { \circ }$ ).

The hydrostatic and wet mapping functions, $m _ { h }$ and $_ { T l \ w }$ , for the neutral atmosphere depend on the vertical distribution of the hydrostatic and wet refractivity above the geodetic sites. With the availability of numerical weather models (NWM) this information can currently be extracted globally with a temporal resolution of six hours (Niell, 2001). Unlike previous mapping functions these are not limited in their accuracy by the use of only surface meteorological data, as in the functions of Ifadis (1986) or in MTT (Herring, 1992), or of the lapse rate and the heights of the isothermal layer and the tropopause as additionally used in the function of Lanyi (1984), nor by the use of average in situ properties of the atmosphere, even if validated with radiosonde data, as in NMF (Niell, 1996). The general form of the hydrostatic and wet mapping functions is (Herring, 1992)

$$
m _ { h , w } \left( e \right) = \frac { 1 + \displaystyle \frac { a } { 1 + \displaystyle \frac { b } { 1 + c } } } { \sin e + \displaystyle \frac { a } { \sin e + \displaystyle \frac { b } { \sin e + \displaystyle \frac { b } { \sin e + \displaystyle c } } } } .
$$

The Vienna Mapping Function 1 (VMF1) (Boehm et al., 2006a) is based on exact ray traces through the refractivity profiles of a NWM at $3 ^ { \circ }$ elevation and empirical equations for the $b$ and $c$ coefficients of the continued fraction in Equation (9.13). Niell (2006) compared mapping functions determined from radiosonde data in 1992 with VMF1 and found that the equivalent station height standard deviations are less than 3 mm, which is significantly better than for other mapping functions available. These results are confirmed by VLBI analyses as shown by Boehm et al. (2007a) and Tesmer et al. (2007), respectively. Thus, VMF1 is recommended for any global application, such as the determination of the terrestrial reference frame and Earth orientation parameters.

At the webpage ${ < } ^ { 4 } >$ , the $a$ coefficients of VMF1 as derived from data of the ECMWF are provided with a time interval of 6 hours for the positions of most sites of the International GNSS Service (IGS), the International VLBI Service for Geodesy and Astrometry (IVS), and the International DORIS Service (IDS), as well as on a global $2 . 5 ^ { \circ } \times 2 . 0 ^ { \circ }$ grid. Kouba (2008) compares results from the grids with VMF1 given at the sites and provides algorithms on how to use the grids.

The Global Mapping Function (GMF) (Boehm et al., 2006b) is an empirical mapping function in the tradition of NMF that can be calculated using only station latitude, longitude (not used by NMF), height, and day of the year. GMF, which is based on spherical harmonics up to degree and order 9, was developed with the goal to be more accurate than NMF and to be consistent with VMF1. Some comparisons of GMF, VMF1 and other MFs with radiosonde data may be found in (Niell, 2006). GMF is easy to implement and can be used when the best accuracy is not required or when VMF1 is not available. The Fortran subroutines VMF1.F and GMF.F are available at $< ^ { 2 } >$ and ${ < } ^ { 4 } >$ .

# 9.3 Sources for meteorological data

Because 1 mbar pressure error causes an a priori delay error of about 2.3 mm at sea level, it is essential to use accurate estimates of meteorological data (Tregoning and

Herring, 2006). If meteorological instrumentation is not available, meteorological data may be retrieved from a NWM, e.g. the ECMWF as provided together with VMF1 at ${ < } ^ { 4 } >$ . In both cases adjustments of the pressure should be applied for the height difference between the location of the pressure measurement (from in situ instrumentation or from NWM) and the reference point of the space geodesy instrument. Commonly used formulas for the adjustment can be found in (Boehm et al., 2007b). Alternatively, local pressure and temperature estimates could be determined with the empirical model GPT (Boehm et al., 2007b) that has been developed similarly to the GMF, and is provided as a Fortran routine, GPT.F, at ${ < } ^ { 2 } >$ and ${ < } ^ { 4 } >$ .

# 9.4 Ionospheric model for radio techniques

Dispersive effects of the ionosphere on the propagation of radio signals are classically accounted for by linear combination of multi-frequency observations. In past years it has been shown that this approach induces errors on the computed time of propagation that can reach 100 ps for GPS due to the fact that higher order dispersive effects are not considered. For wide-band VLBI observations, the induced errors might reach a couple of ps. In this section the estimation of the effect of higher-order neglected ionospheric terms and possible conventional models are summarized for the microwave range, with frequencies from hundreds of MHz to few tens of GHz.

# 9.4.1 Ionospheric delay dependence on radio signals including higher order terms

The delay $\delta \rho _ { I }$ experienced by the transionospheric electromagnetic signals, travelling from the transmitter $T$ at ${ \vec { r } } _ { T }$ to the receiver $R$ at ${ \vec { r } } _ { R }$ , separated by a distance $\rho$ , can be expressed by the integral of the refractive index $n$ along the ray path:

$$
\delta \rho _ { I } = \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } c \frac { d l } { v } - \rho = \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } ( n - 1 ) d l
$$

where $c = 2 9 9 7 9 2 4 5 8 ~ \mathrm { m / s }$ is the light speed in free space, $v$ is the actual transionospheric signal propagation velocity at the given place and $d l$ is the differential length element.

# Effects on carrier phase data

By neglecting the frictional force, assuming that we are in a cold, collisionless, magnetized plasma such as the ionosphere, the refractive index for the carrier phase, $n _ { p }$ , can be expressed by the Appleton expression, for both ordinary (upper sign) and extraordinary (lower sign) waves, see for instance Davies (1990) page 72:

$$
n _ { p } ^ { 2 } = 1 - \frac { X } { 1 - \frac { Y _ { T } ^ { 2 } } { 2 ( 1 - X ) } \pm \left[ \frac { Y _ { T } ^ { 4 } } { 4 ( 1 - X ) ^ { 2 } } + Y _ { L } ^ { 2 } \right] ^ { \frac { 1 } { 2 } } }
$$

where

$$
X = \frac { \omega _ { p } ^ { 2 } } { \omega ^ { 2 } } , \qquad Y _ { L } = - \frac { \omega _ { g } } { \omega } \cos \theta , \qquad Y _ { T } = - \frac { \omega _ { g } } { \omega } \sin \theta ,
$$

where $\theta$ is the angle between the magnetic field $\vec { B }$ and the electromagnetic (EM) propagation direction $\vec { k }$ , and where $\omega = 2 \pi f$ is the circular frequency corresponding to a frequency $f$ . This applies to the carrier circular frequency $\omega$ , and to the plasma $\omega _ { p }$ and gyro $\omega _ { g }$ circular frequencies associated to the free electrons of the ionosphere:

$$
\omega _ { p } ^ { 2 } = { \frac { N _ { e } q ^ { 2 } } { m _ { e } \epsilon _ { 0 } } } \qquad \omega _ { g } = { \frac { B q } { m _ { e } } }
$$

where $N _ { e }$ is the number density of free electrons and $B$ is the magnetic field modulus (both depending on time and position along the EM ray), $q \simeq 1 . 6 0 2 2 \times$ $1 0 ^ { - 1 9 } \mathrm { C }$ is the absolute value of the electron charge, $m _ { e } \simeq 9 . 1 0 9 4 \times 1 0 ^ { - 3 1 } \mathrm { k g }$ is the electron mass and $\epsilon _ { 0 } \simeq 8 . 8 5 4 2 \times 1 0 ^ { - 1 2 } \mathrm { F / m }$ is the electric permittivity in free space (vacuum). Extraordinary waves (lower sign) can be typically associated to right hand polarized EM signals such as those of GPS antennas, and most $\mathrm { L }$ and S Band antennas that receive satellite signals.

For signals with frequencies $\omega > > \omega _ { p }$ (and hence $\omega > > \omega _ { g }$ ) as for GNSS we may expand (9.15) into a second-order Taylor approximation and retain only terms up to $f ^ { - 4 }$ , similarly to the approach of Bassiri and Hajj (1993). The result is, see (Datta-Barua et al. 2008) for a detailed discussion of several approximation ways adopted by different authors:

$$
n _ { p } = 1 - { \frac { 1 } { 2 } } X \pm { \frac { 1 } { 2 } } X Y _ { L } - { \frac { 1 } { 8 } } X ^ { 2 } - { \frac { 1 } { 4 } } X \cdot Y ^ { 2 } ( 1 + \cos ^ { 2 } \theta )
$$

where $\begin{array} { r } { Y ^ { 2 } = Y _ { L } ^ { 2 } + Y _ { T } ^ { 2 } = \left( \frac { \omega _ { g } } { \omega } \right) ^ { 2 } } \end{array}$ and again upper sign represents ordinary wave, and lower sign represents extraordinary wave.

The following explicit expression for $n _ { p }$ can be obtained for extraordinary EM signals in terms of the main physical constants and parameters, after substituting $X$ , $Y _ { L }$ and $Y _ { T }$ from equations (9.16):

$$
\begin{array} { c } { { n _ { p } = 1 - { \displaystyle \frac { q ^ { 2 } } { 8 \pi ^ { 2 } m _ { e } \epsilon _ { 0 } } } \cdot { \frac { N _ { e } } { f ^ { 2 } } } - { \displaystyle \frac { q ^ { 3 } } { 1 6 \pi ^ { 3 } m _ { e } ^ { 2 } \epsilon _ { 0 } } } \cdot { \frac { N _ { e } B \cos \theta } { f ^ { 3 } } } } } \\ { { - { \displaystyle \frac { q ^ { 4 } } { 1 2 8 \pi ^ { 4 } m _ { e } ^ { 2 } \epsilon _ { 0 } ^ { 2 } } } \cdot { \frac { N _ { e } ^ { 2 } } { f ^ { 4 } } } - { \displaystyle \frac { q ^ { 4 } } { 6 4 \pi ^ { 4 } m _ { e } ^ { 3 } \epsilon _ { 0 } } } \cdot { \frac { N _ { e } B ^ { 2 } ( 1 + \cos ^ { 2 } \theta ) } { f ^ { 4 } } } } } \end{array}
$$

Inserting equation (9.19) into (9.14) leads to the following ionospheric dependent terms in the carrier phase, up to third ( $f ^ { - 4 }$ ) order:

$$
\delta \rho _ { I , p } = - { \frac { s _ { 1 } } { f ^ { 2 } } } - { \frac { s _ { 2 } } { f ^ { 3 } } } - { \frac { s _ { 3 } } { f ^ { 4 } } }
$$

After substituting the physical constants, $m _ { e }$ , $q$ , $\epsilon _ { 0 }$ , with 5 significant digits the first, second and third order coefficients, $s _ { 1 }$ , $s _ { 2 }$ and $s _ { 3 }$ , read (note that the International System of Physical Units (SI) is used, e.g. magnetic field is expressed in Tesla):

$$
\begin{array} { l } { { s _ { 1 } = 4 0 . 3 0 9 \int _ { \tilde { \tau } _ { T } } ^ { \tilde { \tau } _ { R } } N _ { e } d l } } \\ { { \ } } \\ { { s _ { 2 } = 1 . 1 2 8 4 \cdot 1 0 ^ { 1 2 } \int _ { \tilde { \tau } _ { T } } ^ { \tilde { \tau } _ { R } } N _ { e } B \cos \theta d l } } \\ { { \ } } \\ { { \ } } \\ { { s _ { 3 } = 8 1 2 . 4 2 \int _ { \tilde { \tau } _ { T } } ^ { \tilde { \tau } _ { R } } N _ { e } ^ { 2 } d l + 1 . 5 7 9 3 \times 1 0 ^ { 2 2 } \int _ { \tilde { \tau } _ { T } } ^ { \tilde { \tau } _ { R } } N _ { e } B ^ { 2 } \left( 1 + \cos ^ { 2 } \theta \right) d l } } \end{array}
$$

These expressions are fully equivalent for instance to Equations (2) to (5) in Fritsche et al. (2005).

It can be seen in the last expressions (9.20) to (9.23) that the ionospheric delay on the carrier phase is negative, indicating an increase of the phase velocity of the EM transionospheric signal propagation.

In order to assess the importance of the different ionospheric terms for $\delta \rho _ { I , p }$ in Equation (9.20), we start with the first term, assuming a high value of Slant Total Electron Content (STEC, see Section 9.4.2 for more details) of $\begin{array} { r } { S = \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } d l \sim } \end{array}$ $3 0 0 \times 1 0 ^ { 1 6 } \mathrm { m ^ { - 2 } }$ :

$$
\delta \rho _ { I , p , 1 } = - \frac { 4 0 . 3 0 9 S } { f ^ { 2 } } \sim - \frac { 1 . 2 \times 1 0 ^ { 2 0 } } { f ^ { 2 } }
$$

In this case we obtain a first ionospheric order term $\delta \rho _ { I , p , 1 }$ of up to several km of delay for $f \simeq 1 5 0$ MHz (negative for the carrier phase), corresponding to the lower frequency of the NIMS satellite system (U.S. Navy Ionospheric Measuring System, formerly TRANSIT), and of up to several tens of meters for $f = 1 5 7 5 . 4 2$ MHz ( $L _ { 1 }$ GPS carrier frequency).

The relative importance of the first $( \delta \rho _ { I , p , 1 } = - s _ { 1 } / f ^ { 2 } $ ), second $( \delta \rho _ { I , p , 2 } = - s _ { 2 } / f ^ { 3 } )$ and third order terms $\langle \delta \rho _ { I , p , 3 } = - s _ { 3 } / f ^ { 4 } \rangle$ also depends on the frequency. The higher order terms are increasingly less important for increasing frequencies (e.g. for VLBI frequencies compared to GPS frequencies). Indeed, from Equations (9.20) to (9.23):

$$
\frac { \delta \rho _ { I , p , 2 } } { \delta \rho _ { I , p , 1 } } = \frac { 2 . 7 9 9 4 \times 1 0 ^ { 1 0 } } { f } \cdot \frac { \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } B \cos \theta d l } { \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } d l }
$$

By taking typical values reflecting the order of magnitude of $| B _ { 0 } \cos \theta _ { 0 } | \simeq 1 0 ^ { 4 } \mathrm { n T }$ at a given effective height to evaluate both integrals, the order of magnitude of the ratio of second to first order ionospheric term can be approximated by:

$$
\frac { \delta \rho _ { I , p , 2 } } { \delta \rho _ { I , p , 1 } } \simeq \frac { 2 . 7 9 9 4 \times 1 0 ^ { 1 0 } } { f } \vert B _ { 0 } \cos \theta _ { 0 } \vert \sim \frac { 2 . 8 \times 1 0 ^ { 5 } } { f }
$$

The value of $\delta \rho _ { I , p , 2 }$ is thus typically only $1 \%$ of that of $\delta \rho _ { I , p , 1 }$ for $f \simeq 1 5 0$ MHz (NIMS), and only $0 . 1 \%$ for $f = 1 5 7 5 . 4 2$ MHz (GPS $L _ { 1 }$ carrier).

Similarly, the order of magnitude of the relative value between third and second order ionospheric terms can be estimated as:

$$
\frac { \delta \rho _ { I , p , 3 } } { \delta \rho _ { I , p , 2 } } = \frac { 7 . 1 9 9 8 \times 1 0 ^ { - 1 0 } } { f } \cdot \frac { \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } ^ { 2 } d l } { \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } B \cos \theta d l } + \frac { 1 . 3 9 9 6 \times 1 0 ^ { 1 0 } } { f } \cdot \frac { \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } B ^ { 2 } \left( 1 + \cos ^ { 2 } \theta \right) d l } { \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } B \cos \theta d l }
$$

Considering the typical values used above reflecting order of magnitude of $\left| B _ { 0 } \cos \theta _ { 0 } \right|$ $\mathrm { \simeq 1 0 ^ { 4 } n T }$ at a given effective height to evaluate the integrals, an intermediate aneffective electron density fulfilling N0 · R \~rR\~rT gle of $\theta _ { 0 } = 4 5$ deg, and taking $N _ { 0 } \simeq 1 0 ^ { 1 2 } \mathrm { m ^ { - 3 } }$ $\begin{array} { r } { N _ { 0 } \cdot \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } d l = \int _ { \vec { r } _ { T _ { . } } } ^ { \vec { r } _ { R } } N _ { e } ^ { 2 } d l } \end{array}$ a raw order of magnitude value of , we get the following relative order of magnitude value between third and second order ionospheric terms:

$$
\begin{array} { r l r } {  { \frac { \delta \rho _ { I , p , 3 } } { \delta \rho _ { I , p , 2 } } \simeq \frac { 1 } { f } ( 7 . 1 9 9 8 \times 1 0 ^ { - 1 0 } \frac { N _ { 0 } } { | B _ { 0 } \cos \theta _ { 0 } | } + 1 . 3 9 9 6 \times 1 0 ^ { 1 0 } \cdot \frac { 3 } { 2 } | B _ { 0 } \cos \theta _ { 0 } | ) } } \\ & { } & { \sim \frac { 7 . 2 \times 1 0 ^ { 7 } + 2 . 1 \times 1 0 ^ { 5 } } { f } \qquad ( \mathbb { S } _ { \varepsilon } \times 1 0 ^ { - 1 0 } \cdot \frac { 1 } { 2 } ) \qquad \mathrm { ( } \varepsilon \times 1 0 ^ { - 1 0 } \cdot \frac { 3 } { 2 } | B _ { 0 } \cos \theta _ { 0 } | ) } \end{array}
$$

The order of magnitude of the ratio between third and second order ionospheric terms can thus be as high as about 50% for NIMS frequency $f \simeq 1 5 0$ MHz but less than $1 0 \%$ for $f = 1 5 7 5 . 4 2$ MHz, the $L _ { 1 }$ GPS carrier frequency.

Another conclusion from this approximation is that the second integral in (9.23) can typically be neglected compared to the first integral depending only on the electron density, as it is typically two orders of magnitude smaller, see Equation (9.28):

$$
s _ { 3 } \simeq 8 1 2 \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } ^ { 2 } d l
$$

Finally, in order to show that third order ionospheric approximation should be adequate for most of the radio astronomic-geodetic techniques, we can consider the fourth order term $\delta \rho _ { I , p , 4 }$ in the carrier phase delay. It can be deduced in a similar way as the first to third order terms, but now keeping the terms $f ^ { - 5 }$ in the Taylor expansion of Equation (9.15) in the corresponding fourth order term $\delta n _ { p , 4 }$ of the carrier phase ionospheric refraction index term

$$
\delta n _ { p , 4 } = - \frac { 1 } { 2 } X Y _ { L } \left( \frac { X } { 2 } + Y ^ { 2 } \left[ 1 + \frac { 1 } { 8 } \sin ^ { 2 } \theta \tan ^ { 2 } \theta \right] \right)
$$

which is expressed with the same notation as in the previous expressions. Using Equations (9.16) and (9.17) as well as Equation (9.14), the fourth order ionospheric term in delay can be expressed as:

$$
\delta \rho _ { I , p , 4 } = - { \frac { s _ { 4 } } { f ^ { 5 } } }
$$

where

$$
s _ { 4 } = \frac { q ^ { 5 } } { 1 2 8 \pi ^ { 5 } m _ { e } { ^ 3 } \epsilon _ { 0 } { ^ 2 } } \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } ^ { 2 } B \cos \theta d l + \frac { q ^ { 5 } } { 6 4 \pi ^ { 5 } m _ { e } { ^ 4 } \epsilon _ { 0 } } \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } B ^ { 3 } f ( \theta ) d l
$$

and where $\begin{array} { r } { f ( \theta ) = \cos \theta \left( 1 + \frac { 1 } { 8 } \sin ^ { 2 } \theta \tan ^ { 2 } \theta \right) } \end{array}$ . Substituting the values of the constants we get:

$$
s _ { 4 } = 4 . 5 4 8 1 \times 1 0 ^ { 1 3 } \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } ^ { 2 } B \cos \theta d l + 8 . 8 4 1 3 \times 1 0 ^ { 3 2 } \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } B ^ { 3 } f ( \theta ) d l
$$

Taking into account Equations (9.31), (9.33), (9.20) and (9.29), the ratio between the fourth and third ionospheric order terms can be written as:

$$
\frac { \delta \rho _ { I , p , 4 } } { \delta \rho _ { I , p , 3 } } = \frac { 1 } { f } \left( 5 . 5 9 8 2 \times 1 0 ^ { 1 0 } \frac { \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } ^ { 2 } B \cos \theta d l } { \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } ^ { 2 } d l } + 1 . 0 8 8 3 \times 1 0 ^ { 3 0 } \frac { \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } B ^ { 3 } f ( \theta ) d l } { \int _ { \vec { r } _ { R } } ^ { \vec { r } _ { R } } N _ { e } ^ { 2 } d l } \right)
$$

Taking into account the same approximations and typical values than before, the ratio can be expressed as:

$$
\begin{array} { c } { \frac { \delta \rho _ { I , p , 4 } } { \delta \rho _ { I , p , 3 } } \simeq \frac { 1 } { f } \left( 5 . 6 \times 1 0 ^ { 1 0 } | B _ { 0 } \cos \theta _ { 0 } | + 1 . 1 \times 1 0 ^ { 3 0 } \frac { | B _ { 0 } \cos \theta _ { 0 } | ^ { 3 } f ( \theta _ { 0 } ) } { N _ { 0 } | \cos ^ { 3 } \theta _ { 0 } | } \right) } \\ { \sim \frac { 1 } { f } \left( 5 . 6 \times 1 0 ^ { 5 } + 2 . 3 \times 1 0 ^ { 3 } \right) } \end{array}
$$

According to this expression the fourth order ionospheric term is only $1 \%$ of the third order term for $f \simeq 1 5 0$ MHz (NIMS) and less than $0 . 1 \%$ for the L1 GPS carrier at $f = 1 5 7 5 . 4 2$ MHz. Another conclusion from this development is that the fourth order term can be approximated by the first term in Equation (9.33):

$$
s _ { 4 } \simeq 4 . 5 5 \times 1 0 ^ { 1 3 } \int _ { \vec { r } _ { T } } ^ { \vec { r } _ { R } } N _ { e } ^ { 2 } B \cos \theta d l
$$

Table 9.2 provides delays corresponding to ionospheric terms of different order and different frequencies of interest in radio astronomic-geodetic research, with the same approximations and particular values as above $( | B _ { 0 } \cos \theta _ { 0 } | \sim 1 0 ^ { 4 } n T$ , $N _ { 0 } \mathrm { ~ \sim ~ } 1 0 ^ { 1 2 } \mathrm { m ^ { - 3 } }$ and $S \sim 3 \times 1 0 ^ { 1 8 } \mathrm { m ^ { - 2 } }$ ). It can be seen, taking as significant threshold the delay value of 1mm, that:

• The first order ionospheric term, as expected, is significant for all the considered frequencies.   
The second order ionospheric term should be taken into account for all the frequencies, except for the high VLBI frequency and those used for $\mathrm { K u }$ band time transfer.   
• The third order ionospheric term should be taken into account in NIMS and DORIS low frequencies. It is at the significance limit for GPS and high DORIS frequencies and can be neglected for VLBI and time transfer Ku band frequencies.   
• The fourth order can be neglected, except for the very low NIMS frequency of $1 5 0 ~ \mathrm { M H z }$ .

# Ray bending effects on geometric path excess and ionospheric delay

Moreover the effect of the curvature (or bending) of the ray in terms of geometric path excess can be considered as an additional correction $\Delta { s } _ { 3 }$ (typically up to few millimeters at low elevation for GPS frequencies), appearing as a $f ^ { - 4 }$ dependence too, which can be easily added to the $s _ { 3 }$ coefficient of Equation (9.47). In


<!-- chunk 0003: pages 141-179 -->
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

![](../chunks/IERS Conventions (2010), IERS Technical Note No.36_part_0003_pages_0141-0179/auto/images/02af0500ed6ec808b267d4f0da04cf26a2910a175725293e8e7d1660173d6da5.jpg)  
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

![](../chunks/IERS Conventions (2010), IERS Technical Note No.36_part_0003_pages_0141-0179/auto/images/2cdfb49c78116e81b299034fdb301310c2cf4e495243b91b11f3d59eb3963193.jpg)  
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
