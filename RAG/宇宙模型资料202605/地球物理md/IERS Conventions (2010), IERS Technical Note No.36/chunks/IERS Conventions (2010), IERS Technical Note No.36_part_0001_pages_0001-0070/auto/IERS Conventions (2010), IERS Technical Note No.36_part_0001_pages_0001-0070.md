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

![](images/bddf43bf2c8bdaa83b143b35fdd7713da303df15551ab2ee0a8973b7b6f8aec5.jpg)  
Figure 1.1: Treatment of observations to account for tidal deformations in terrestrial reference systems (see Chapters 4 and 7).

# 1.2 Numerical standards

Table 1.1, that lists adopted numerical standards, is organized into 5 columns: constant, value, uncertainty, reference, and description. Values of defining constants are provided without an uncertainty. The IAU (2009) System of Astronomical Constants (Luzum et al., 2010) is adopted for all astronomical constants which do not appear in Table 1.1. Note that, except for defining constants, the values correspond to best estimates which are valid at the time of this publication and may be re-evaluated as needed. They should not be mistaken for conventional values, such as those of the Geodetic Reference System GRS80 (Moritz, 2000) shown in Table 1.2, which are, for example, used to express geographic coordinates (see Chapter 4).

Unless otherwise stated, the values in Table 1.1 are TCG-compatible or TCBcompatible, i.e. they are consistent with the use of Geocentric Coordinate Time TCG as a time coordinate for the geocentric system, and of Barycentric Coordinate Time TCB for the barycentric system. Note that for astronomical constants such as mass parameters $\it G M$ of celestial bodies having the same value in BCRS and GCRS, the formulations “TCB-compatible” and “TCG-compatible”

![](images/2afb94a8062811946dd061d057f76d1d4c446b5ca6adef70eebf36397f5ef29d.jpg)  
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

![](images/76c5e2eaf588a52dfd295864d7772bdf039d721318508ea2157582180b8c153e.jpg)  
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

![](images/40db1ae717a43e380251653ad79c092af077a23938557137fb108d80661737f0.jpg)

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