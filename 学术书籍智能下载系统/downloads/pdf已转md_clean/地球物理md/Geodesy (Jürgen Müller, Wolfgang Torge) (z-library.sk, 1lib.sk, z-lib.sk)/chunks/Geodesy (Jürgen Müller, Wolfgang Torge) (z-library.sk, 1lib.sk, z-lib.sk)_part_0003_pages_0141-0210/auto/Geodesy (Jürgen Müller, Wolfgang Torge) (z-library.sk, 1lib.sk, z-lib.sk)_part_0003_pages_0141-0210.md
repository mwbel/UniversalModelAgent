the Earth ellipsoid $a _ { \mathrm { e } ^ { \prime } }$ ), cf. [3.3.2], [6.7.3]. Consequently, the relative errors of the harmonic coeffi cients increase rapidly at higher degrees $I .$ For $I = 2 0$ , the amplitude of the corresponding structure of wavelength $2 0 0 0 ~ \mathrm { k m }$ is only $5 \%$ at a satellite altitude of $1 0 0 0 ~ \mathrm { k m } ,$ , as compared to the Earth’s surface. This attenuation is increased by the fact that the harmonic coeffi cients become smaller with increasing degree and order, cf. [6.6.2]. In order to resolve the gravitational fi eld from an orbital analysis with a certain degree l at the equator, it follows from (5.38) that the satellite has to perform $2 I$ revolutions/day, or a longer observation time is required. As seen from (5.35), the recovery of the harmonic coeffi cients also strongly depends on the satellite’s inclination. Corresponding satellite coverage is needed in order to avoid ill conditioning; too small inclinations and eccentricities should be avoided. An improved resolution of the gravitational fi eld has been achieved by range and range-rate measurements between satellites (low- and high-orbiting) and ground stations, while an even higher resolution can be obtained by gravity gradiometers carried on board low-orbiting satellites. Satellite altimetry fi nally delivers the distance between the satellite and the ocean surface, and thus a high-resolution approximation to the geoid, cf. [3.4.2]. Dedicated gravity fi eld and satellite altimetry missions require a precise orbit determination and an orientation with respect to the vertical.

Non-gravitational perturbing effects on the satellite can be reduced by a small crosssectional surface and large mass; a spherical shape offers special advantages. Atmospheric drag and solar radiation pressure may also be compensated by a drag-free system. In such a system, a proof mass is shielded by a shell attached to the satellite. The mass is affected only by gravitation, while surface forces act in addition on the shell. By continuously measuring the position changes between proof mass and shell, a feedback system keeps the satellite centered on the proof mass. In order to detect variations with time, in position (station velocities) of observation sites and in the gravitational fi eld, adequate temporal observations series have to be carried out, preferably by the same satellite system.

Satellites used in geodesy may be equipped with the following techniques, of which combinations are used in many missions:

• Direction measurements have been made available by a sun-light refl ecting skin (early balloon satellites), by fl ashing light devices, and by mirror arrays, cf. [5.2.4],   
. transmitters/receivers serve for the continuous emission/reception of modulated radio waves which are used for range and range rate (Doppler) measurements between the ground station and the satellite or between satellites, cf. [5.2.4], [5.2.5], [5.2.8], retrorefl ector arrays of fused silica corner cubes refl ect laser light pulses and are employed for laser distance measurements, cf. [5.2.6],   
vertical distance measurements to the ocean surface are performed by radar altimeters, cf. [5.2.7], gravity gradiometers measure gravitational gradients within the body of the satellite, cf. [5.2.8].

High demands are placed on the determination of time. At orbital velocities of several ${ \mathrm { k m } } / { \mathrm { s } } ,$ the time epoch has to be determined to $\pm 1 ~ \mu \varsigma$ in order to keep orbital errors less than 1 cm. Distance measurements to satellites require time interval measurements to $\pm 0 . 1$ ns in order to obtain cm-accuracy. Rubidium or cesium frequency standards, which are tied to UTC by time signals, are capable of reaching this level of accuracy. Quartz oscillators can be used in satellite receivers if an external control is provided, e.g., through the satellite system, cf. [5.2.5].

More details on satellites employed in geodesy are given in the following chapters.

# 5.2.4 Direction, range and range rate (Doppler, DORIS) measurements

Satellite observations began in 1957. They were based partly on methods developed for the observation of the moon and of high-fl ying balloons. While some of the classical techniques applied up to the 1980s are no longer of importance, other methods have been developed further and are used extensively today. Some results of the early satellite missions are still of relevance for the strengthening and orientation of geodetic networks and for the calculation of Earth models (e.g., Seeber, 2003, p. 158 ff.).

Direction measurements to satellites prevailed until about 1970 and led for the fi rst time to global and regional three-dimensional networks. Orbital analysis also provided the low-degree harmonic coeffi cients of the gravitational potential development.

For optical direction measurements, an illuminated satellite is photographed on fi lm or glass plates together with the fi xed stars.

Balloon satellites refl ecting sunlight (e.g., Pageos, 1966 –1972, diameter of $3 0 { \mathfrak { m } } _ { \ r }$ , $i = 8 7 ^ { \circ } ,$ , $h = 2 8 0 0$ to $5 6 0 0 ~ \mathrm { k m } )$ and light fl ashes from active satellites were used. Ballistic cameras (e.g., Wild BC4) mounted azimuthally were easy to operate and had a large fi eld of view. Equatorially-mounted astronomic cameras could follow the motion of the stars. Using a large focal length, even faint stars could thus be detected and observed with high precision. Orbital cameras were designed so that they could also follow the motion of a satellite. Upon developing the photographs and identifying the stars, the satellite and star image points were measured on a precision comparator $( \pm 1 \ \mu \mathrm { m } )$ . The plate coordinates of the satellite were then transformed to the spatial directions right ascension and declination, whereby the transformation parameters were derived from the known directions to the stars, cf. [2.4.1]. Since the satellite travels in the atmosphere, astronomic refraction reduction as applied to the stars, cf. [5.3.3], had to be reduced by the satellite refraction (Fig. 5.43), with

$$
\Delta Z _ { _ { \mathrm { s a t } } } = 0 . 4 8 ^ { \prime \prime } \frac { \tan z } { h \left[ 1 0 0 0 ~ \mathrm { k m } \right] } .
$$

The accuracy of the direction measurements was $0 . 2 { ^ { \prime \prime } }$ to $2 ^ { \prime \prime } .$ An increase in accuracy was not possible mainly due to scintillation effects and comparator measuring errors. An outstanding example of a geometric satellite network established by stellar triangulation is the global net (45 stations) of the U.S. National Geodetic Survey (1966–1970). It was constructed by direction measurements with Wild BC4 cameras to the Pageos satellite, and the scale was derived from long traverses measured with electronic distance meters; an accuracy of 4 to $5 \textrm { m }$ was achieved (Schmid, 1974).

The Japanese satellite EGS (Experimental Geodetic Satellite), also Ajisai $( h = 1 5 0 0 \mathrm { k m } ,$ $i = 5 0 ^ { 0 }$ , nearly circular orbit) is a more recent example of direction measurements. The spherical-shaped (diameter $2 . 1 4 \mathrm { ~ m }$ ) satellite was launched in 1986. Its surface is equipped with both mirror and laser refl ector assemblies. By rotation of the satellite about its axis, incident sunlight is refl ected periodically with two fl ashes per second. The satellite has been used for laser range and for photographic direction measurements, in order to improve the Japanese horizontal control network and to connect remote islands. Precise orbit determination is also exploited for gravity fi eld improvement.

Microwave distance-measurements started in the 1960s and still play a fundamental role today.

The Secor (Sequential Collation of Range) system used modulated microwaves (two frequencies) emitted from ground stations and re-transmitted from transponders on board the satellites. Distances were derived from signal’s travel time, using the phase comparison method, cf. [5.5.2]. Using this method and employing spatial trilateration, isolated geodetic networks were connected to a global reference system. The precision obtained was a few ${ \mathsf { m } } ,$ although systematic errors up to several $^ { 1 0 \mathrm { ~ m ~ } }$ also occurred.

Starting in the 1970s, Doppler positioning (named after the Austrian Christian Doppler, 1803–1853) soon became an effi cient tool for establishing 3D-networks, or for improving classical geodetic horizontal control. By orbital analysis, it also delivered improved geopotential models and Earth rotation parameters (Seeber, 2003, p. 181 ff.).

With Doppler measurements, a transmitter on-board a satellite $S$ continuously emits a stable frequency $f _ { _ s }$ (Fig. 5.8). A signal is received at the ground station (distance $s$ to the satellite) with the frequency $f _ { g }$ and a time shift $\Delta t$ with respect to the transmission time $t .$ $f _ { g }$ is shifted againstbserver (Doppler $f _ { _ { \mathscr { s } } }$ due to the relative velocityfect). Neglecting higher orde $\dot { \mathbf { s } } = d \mathbf { s } / d t$ between the satellite and thehe Doppler frequency shift for satellites with velocities much smaller than $C$ is given by

$$
f _ { _ { g } } - f _ { _ s } = - \frac { f _ { _ s } } { C } \dot { s } .
$$

The Doppler shift is proportional to ${ \dot { s } } ;$ a reversal in sign occurs at the time of the closest approach of the satellite to the observer $( \dot { s } = 0 )$ ). In principle, a range difference (range rate) can be determined from (5.40) by integration over time. In practice, $f _ { g }$ is compared with a stable reference frequency $f _ { \mathrm { 0 } }$ generated within the Doppler receiver, with $f _ { _ 0 } \approx f _ { _ s }$ . Integration over a time interval yields the Doppler count

$$
N _ { _ { i j } } = \int _ { t _ { i } + \Delta t _ { i } } ^ { t _ { j } + \Delta t _ { j } } { } d t .
$$

![](images/7b094dfc99663155d07c9ce3b8c84fb63570b27402e1ff85e7cabe46aaa39b05.jpg)  
Fig. 5.8: Satellite Doppler positioning.

With (5.40), we obtain the observation equation

$$
N _ { _ { i j } } = \big ( f _ { _ 0 } - f _ { s } \big ) \big ( t _ { j } - t _ { i } \big ) + \frac { f _ { _ 0 } } { C } \big ( s _ { j } - s _ { i } \big ) ,
$$

which provides the range rate $s _ { j _ { . } } { - } s _ { . }$ from the Doppler counts.

As with any microwave technique, Doppler measurements do not depend on weather conditions, and they allow large amounts of data to be accumulated within short time intervals. Today, Doppler measurements are used with several satellite missions and with the DORIS positioning system, see below. Range rate measurements also represent the basic technique for satellite-to-satellite tracking, which is employed for high-resolution gravity fi eld determination, cf. [5.2.8].

The Navy Navigation Satellite System (NNSS) or Transit System was an important application of Doppler measurements (Anderle, 1986). Developed as a navigation system for the U.S. Navy, it was opened to civil use early on and operated successfully between 1964 and 1996. Positioning was based on four to seven Transit satellites in orbit $h \approx 1 1 0 0 ~ \mathrm { k m }$ , $i \approx 9 0 ^ { \circ }$ ), which continuously transmitted frequencies of 150 and $4 0 0 ~ M { \sf H } z$ . With the orbital planes of the satellites evenly distributed in longitude, and due to Earth rotation, a satellite became visible at least every two hours along the equator. The satellite orbits were determined by Doppler measurements from four tracking stations located in the U.S.A. Initially they referred to the World Geodetic System 1972 (WGS72) and later to WGS84, cf. [5.2.5]. The satellites transmitted their “broadcast ephemeris” at twominute intervals, together with UTC time signals, with an accuracy of 10 to $2 0 ~ \mathsf { m }$ . “Precise ephemeris” $( \pm 1$ to $2 \textrm { m }$ ) were later made available to authorized users. A number of portable Doppler navigation receivers were commercially produced for geodetic purposes. These contained a reference oscillator, a microprocessor, a data-recording unit, the antenna, and an energy supply. The infl uence of ionospheric refraction was practically eliminated by the use of two frequencies, cf. [5.1.3], and tropospheric refraction was computed using atmospheric models and observed meteorological data, cf. [5.1.2]. A positional error of 10 to $3 0 \textrm { m }$ was obtained at the observation of a single satellite pass. This error could be reduced to 2 to $5 \textrm { m }$ (broadcast ephemeris) with 30 to 50 passes and to 5 to $1 \textrm { \textrm { m } }$ using precise ephemeris, the latter being derived from a network of about 20 globally distributed stations. Relative positioning employed simultaneous observations on two or more stations, which strongly reduced orbital and refraction errors and led to baseline accuracies of 0.2 to $_ { 0 . 5 \textrm { m } }$ (Seeber et al., 1982). With GPS becoming operational, the NNSS was no longer maintained.

Another successful application of the Doppler method started in the 1990s with the French DORIS (Doppler Orbitography and Radio Positioning Integrated by Satellite) system (Fagard, 2006). In contrast to the Transit system, the radio signals (2.03 and $0 . 4 0 ~ \mathrm { G H z } )$ ) are emitted here continuously by ground beacons, and received and processed as Doppler frequency shifts (integration, e.g., over 10 s) onboard of satellites which also carry an ultra-stable crystal oscillator for time-tagging. The system was originally developed by the French Space Agency CNES, in cooperation with the Institut Géographique National and the Groupe de Recherches de Géodésique Spatiale, in order to support precise orbit determination for altimeter and remote sensing missions. DORIS receivers are fl own on a number of satellites, including the altimeter satellites Topex/Poseidon, Jason-2 and Envisat, and remote sensing SPOT satellites (DORIS, 2006).

Meanwhile, a global network of 50 to 60 permanently emitting DORIS ground stations has been built up, containing dual-frequency receiver, oscillator, microprocessor, power supply and antenna. The stations are well monumented, for example by concrete pillars or rigid towers (Fig. 5.9), and through co-location well tied to other IERS techniques and to tide gauges. They are evenly distributed around the globe, including oceanic areas (Fig. 5.10), which is an advantage when compared with global networks based on other space techniques. The precise orbit determination also allows the calculation of the coordinates and the velocities of the DORIS global network ground stations, as well as the positioning of dedicated location beacons. Precise orbit determination is now possible with cm-accuracy in post-processing, and the International DORIS Service (IDS) of IAG provides coordinates and velocities of the tracking stations with an accuracy of better than 1 cm resp. $2 \ \mathsf { m m }$ /year, and also UT1 time rates, polar motion and polar motion rates as well as geocenter and scale information of the International Terrestrial Reference Frame (Tavernier et al., 2006).

![](images/cbcc347e0620d809f8bb2a28da1710e66431e941bbbcb498a20e943cfa8841da.jpg)  
Fig. 5.9: DORIS antenna (standard layout $2 \textrm { m }$ tower), from Fagard (2006).

![](images/62636a747fdca41c6bde18bb79230efbac5e5b39bec4732c32f2e75405f5ee3e.jpg)  
Fig. 5.10: Stations of the DORIS network (status 2006), Tavernier et al. (2006).

We fi nally mention that range rate measurements represent the basic technique for satellite-to-satellite tracking, which is employed for high-resolution gravity fi eld determination, cf. [5.2.8].

# 5.2.5 Global Navigation Satellite Systems GNSS (GPS, GLONASS, Galileo and others)

Global navigation satellite systems have been built up since the 1960s, for world-wide navigation and positioning. Using radio waves as carriers of signals, these systems utilize observed signal travel times in order to derive distances between satellites and ground-based receivers. With the satellites’ orbits and time being known, the positions (coordinates) of the terrestrial stations then can be computed within a well-defi ned terrestrial reference system. Main driver for the development and establishment of these systems came (and to a large part still comes) from military agencies, but the benefi t for civilian use was early recognized and proved to become a strong impetus for further development and improvement of the systems.

While ground-based radio navigation systems of regional and global range like DECCA, LORAN and Omega became in use since the 1940s, the U.S. TRANSIT Navy Navigation Satellite System based on Doppler-measurements was the fi rst satellite-based system, and was available for civilian users since the 1960s, cf. [5.2.4]. The development of satellite navigation systems using one-way microwave distance measurement between satellites and ground stations started in the 1970s, with the U.S. GPS and the Russian GLONASS systems, both being fully operational now. The European Galileo- and the Chinese COMPASS-system are built up since a couple of years, and will in future enable the joint use of several global satellite navigation systems, with eventual augmentation by regional systems as developed, e.g., in Japan and India. In the following, we concentrate on the description of GPS being the most effi cient navigation and positioning system since the 1990s, with widespread application reaching far beyond classical geodetic problems, but also regard the other systems mentioned above.

The NAVSTAR (Navigation System with Time and Range) Global Positioning System GPS was the fi rst spaceborne radio navigation system based on timing and ranging, which became operational worldwide. It is under the responsibility of the U.S. Department of Defense (DOD), which started development of the system in 1973. The fi rst GPS satellites were launched in 1978, and the system became fully operational in 1993. GPS provides real time navigation and positioning by one-way microwave distance measurements between the satellites and the GPS receivers. The system was developed and is maintained in order to satisfy the requirements of the U.S. military forces, but early on its use for geodetic applications was investigated (Bossler et al., 1980). Since the 1990s, the U.S. GPS policy strongly encouraged the civilian use of the system, and today GPS positioning is extensively employed in geodesy (and in a multitude of other geo-referenced applications) at all spatial scales, and also for kinematic positioning and the determination of crustal movements (Evans et al., 2002; Blewitt, 2009).

A large number of textbooks and monographs on GPS (and other global navigation systems) are available. Among the textbooks we have Teunissen and Kleusberg (1998a), Leick (2004), Misra and Enge (2006) and Hofmann-Wellenhof et al. (2008), see also Seeber (2003). A standard reference is given by Parkinson and Spilker (1996), while Kaplan and Hegarty (2006) “provide the reader with a systems engineering treatment”, and Xu (2007) concentrates on theory and algorithms. New developments and results are given, among others, in the proceedings of the meetings of the Satellite Division/Institute of Navigation (ION), and in the journals “Navigation”, “GPS World” and “GPS Solutions”.

The basic idea of GPS is to have at least four satellites above the horizon available $2 4 ~ \mathrm { h }$ everywhere on the Earth. In principle, the position of the receiver’s antenna could be derived already from three observed distances, with the computation of three-dimensional coordinates being based on the known ephemerides of the satellites and the intersection of spherical shells. As the clocks of the satellite and the receiver are not synchronized, a fourth distance measurement is necessary in order to determine the clock synchronization error. Therefore, the original distances derived from the travel time of a signal are called pseudoranges (Fig. 5.11).

We distinguish between the space, the control, and the user segment of GPS.

The space segment consists of 21 active satellites (plus three additional spares) arranged in six nearly circular orbits $( i = 5 5 ^ { \circ }$ , $1 2 \mathrm { ~ h ~ }$ period of revolution) at an altitude of about $2 0 2 0 0 ~ \mathrm { k m }$ (Fig. 5.12, Fig. 5.13). The full satellite constellation provides a global $2 4 { \mathrm { - h } }$ coverage with four to eight satellites visible above $1 5 ^ { \circ }$ elevation. Due to the limited lifetime of a satellite (10 years on average), some additional active spare satellites are usually in space. In addition, a regular replacement in blocks is taking place which results in a regular constellation of more than 30 satellites. This updating also takes improvements in satellite technology and refi ned mission strategies into account, as the inclusion of laser retrorefl ectors for orbit determination (block IIA satellites since 1990), the possibility of distance measurements between satellites (cross links), the on-board computation of ephemeris, and the introduction of new carrier frequencies and ranging codes for military and civilian services.

![](images/31a66c94a912517a7270e8f442463e8e29820b723ab50aeb347b4b24581018b8.jpg)  
Fig. 5.11: GPS positioning (principle).

![](images/e8d90f311f478e1ca38f24436cfbfe9a12df17336e18adb28fff28dacfba11aa.jpg)  
Fig. 5.12: GPS IIR-M (Global Positioning System) satellite, from http://www.gps.gov.

![](images/f1cd8f9b69f11723f5dab2905a01524595582ea7e7672d70dd1ecfbc843b5dcb.jpg)  
Fig. 5.13: GPS orbit constellation, from http://www.gps.gov.

Atomic clocks (two rubidium and two cesium clocks per satellite) provide a highprecision frequency standard, with a few $1 0 ^ { - 1 3 }$ to $1 0 ^ { - 1 4 }$ frequency stability over 1 day, and the future hydrogen masers will even reach a stability of $1 0 ^ { - 1 4 }$ to $1 0 ^ { - 1 5 }$ , cf. [2.2.1]. These clocks produce the fundamental frequency of $1 0 . 2 3 ~ \mathsf { M H z }$ . By multiplication, the L1 ( $1 5 7 5 . 4 2 ~ \mathsf { M H z }$ corresponding to $1 9 . 0 ~ \mathrm { c m }$ wavelength) and the L2 (1227.60 MHz corresponding to $2 4 . 4 ~ \mathrm { c m }$ ) carrier frequencies have been initially derived and continuously emitted. L1 and L2 serve as carriers for two code modulations and for a data signal (navigation message). The codes are given as binary signals $^ { + 1 }$ and $^ { - 1 }$ sequence) in a pseudo-random noise (PRN) form (Fig. 5.14). The $C / A$ -code (coarse/ acquisition code) is modulated on L1 only, with a frequency of $1 . 0 2 3 M { \sf H z }$ (corresponding to $2 9 3 \mathrm { ~ m ~ }$ wavelength) and a repetition rate of $1 \ \mathsf { m s }$ . The $P .$ -code (precise code, now available only as encrypted Y-code, see below) is modulated on L1 and L2 and has a frequency of $1 0 . 2 3 ~ \mathsf { M H z }$ (corresponding to $2 9 . 3 \mathrm { ~ m ~ }$ wavelength) and a repetition sequence of 266 days. Within the frame of modernization of GPS, the block IIR-M satellites (since 2005) carry a further freely accessible code on L2, and a third carrier frequency L5 ( $1 1 7 6 . 4 5 ~ \mathsf { M H z }$ corresponding to $2 5 . 5 \ \mathrm { c m }$ ) is introduced with the block IIF satellites (since 2009).

![](images/9936826960e008bdeadd4b3b3e385e77f54e40df5275eb25cdb05e6ad0aebbf1.jpg)  
Fig. 5.14: GPS signals (principle).

The GPS control segment is responsible for maintaining the operation of the GPS satellites, the determination of GPS time, and the calculation and storage of the navigation data. It consists of the master control station (Schriever AFB, Colorado Springs, Colorado) and a number of globally distributed monitoring stations (originally fi ve stations, with additional 11 stations at the GPS modernization in 2005/2006). The stations are equipped with cesium standards and GPS receivers. They continuously measure pseudoranges to all GPS-satellites in view and transfer the results to the master station. After computation of the satellite orbits and the clock corrections, the (extrapolated) broadcast ephemeris and GPS time are transmitted to the satellites for storage and retransmission by four dedicated ground antennas co-located with monitoring stations. This operational control system is supplemented by the monitor station network of the National Geospatial-Intelligence Agency (NGA), resulting in an accuracy increase of satellite orbits and clock information.

The GPS ephemerides refer to an Earth-fi xed system, realized by the coordinates of the monitoring stations: World Geodetic System (WGS). WGS has been used by the U.S. Department of Defense since the end of the 1950s, and it has been fi rst realized through the versions WGS60, WGS72 and WGS84 (DMA, 1987). The system was originally derived from Doppler observations from the Transit satellite system, cf. [5.2.4], while the refi ned versions (since the 1990s) of WGS84 are based on GPS. Defi ned by NGA, the system is now upgraded at shorter intervals, under the name of WGS84 $( \operatorname { G x } \times \times )$ , where xxx (e.g., 1400) indicates the GPS week number of implementation. The system is intended to serve for mapping, charting, positioning and navigation, following international standards for geodetic reference systems. The defi ning parameters of the WGS84-ellipsoid (tide-free system) are as follows (Slater and Malys, 1998; NIMA, 2000):

semi-major axis $a = 6 \ 3 7 8 \ 1 3 7 \mathrm { m } ,$   
reciprocal fl attening $1 / f = 2 9 8 . 2 5 7 \ 2 2 3 \ 5 6 3 ,$ ,   
geocentric gravitational constant $\mathrm { G } M = 3 9 8 ~ 6 0 0 . 4 4 1 8 \times 1 0 ^ { 9 } \mathrm { m ^ { 3 } s ^ { - 2 } }$ which includes   
the atmospheric part G M  = 0.35 × 1 0 9 m 3 s –2 ,   
angular velocity of the Earth’s rotation $\omega = 7 . 2 9 2 \ 1 1 5 \times 1 0 ^ { - 5 } \mathrm { r a d s } ^ { - 1 } .$

The WGS84-ellipsoid thus practically coincides with the parameters of the Geodetic Reference System 1980, cf. [4.3]. The associated gravity fi eld is given by the global geopotential model EGM96 resp. EGM2008, cf. [6.6.3]. The coordinates of the monitoring stations are given for the epoch 1997.0, taking Earth tides (tide-free system), cf. [3.4.1], and plate tectonic motions into account. The accuracy of the recent WGS84 (G1400)-coordinates is at the cm-order of magnitude, which is also the level of agreement between WGS84 and the International Terrestrial Reference Frame (ITRF, 2008), cf. [2.4.2].

GPS-time (unit SI-second) as a continuous time scale is defi ned by the cesium clocks of the control segment stations and the satellites. Its initial epoch is January 5, 1980 at $_ { \textrm { 0 h } }$ UTC, and since then it differs from UTC because of the UTC “leap seconds”, cf. [2.2.2], and the drift in the GPS clocks. The actual difference between GPS-time and UTC (some 10 s) is part of the GPS navigation message $( \pm 5$ ns). GPS thus is also a very effi cient system of time transfer. An accuracy of some 10 ns can be obtained already with automatically operating single-frequency receivers, while multi-station and multi-satellite constellations allow the time transfer with $\pm 1$ to 0.1 ns (Larson and Levine, 1999).

The user segment is composed of the many different type GPS receivers operating in navigation, geodesy, and surveying. The main components of a receiver include the antenna, the receiver electronics, the microprocessor, the oscillator, the memory, the user interface, and a power supply. An additional telemetry unit can be used for data transfer between different receivers (differential mode, see below).

The signals transmitted from the satellites are received and amplifi ed by the antenna. After identifi cation (comparison with the receiver’s code copy) the signals are processed to pseudoranges in the channels of the receiver electronics. One channel is generally responsible for the tracking of one satellite. Hence, a minimum of four channels is necessary to determine position and time. Dual-frequency receivers contain 12 or more channels for each frequency (multi-channel technique), which results in a total of 72, 120 or even 220 channels, and enables the simultaneous tracking of a large set of GPS, GLONASS and Galileo satellites. The microprocessor controls the operation of the receiver and calculates the three-dimensional position of the antenna in WGS 84, as well as the velocity and azimuth of moving objects. A quartz oscillator is used for generating the reference frequency, which is approximately synchronized with GPS-time. All data (pseudoranges, phases, time, navigation message) are stored in receiver memory for post-processing, which is typical for multi-station observation sessions often employed in geodesy, cf. [6.2.1]. The user interface includes a keyboard and a display, which provides a communication link between the user and receiver. Power is provided by internal, rechargeable nickel-cadmium batteries.

While GPS code-signals (see below) generally are suffi cient for navigation, geodetic GPS receivers use the carrier phases as observables which leads to higher accuracies, in the static as well as in the kinematic mode (e.g., Langley, 1997; Seeber, 2003, p. 234 ff.). This is achieved by dual-frequency (L1 and L2) multi-channel instruments and the full carrier wave information available on L1 and L2. Other characteristics include low receiver-noise in code and carrier phase, a high data rate $( > 1 \ \mathsf { H z } ,$ and up to a $5 0 ~ \mathsf { H z }$ sampling rate), and a large memory capacity. The antenna phase center should be stable and protected against multipath effects (see below).

The Macrometer (1982) was the fi rst GPS receiver for geodetic applications (code-free, single frequency, 6 parallel channels), Counselman and Shapiro (1979). The Texas Instruments TI4100 (1984) provided all geodetically relevant observables (P- and C/A-code pseudo ranges, carrier phases on L1 and L2) in a multiplex channel technique (Seeber et al., 1985). Today, a large number of geodetic receivers is available (see the relevant journals as ${ } ^ { \prime \prime } \mathrm { C P S }$ Solutions”), and their effi ciency is discussed in the geodetic literature. Figs. 5.15 to 5.19 show some examples of actual GNSS-receivers. These instruments are generally able to track any combination of GPS, GLONASS and Galileo satellites, where 20 to 30 satellites will be visible with fully deployed systems. This will improve the satellites-receiver geometry as well as the integrity of the solution, and lead to a higher accuracy for absolute positioning.

![](images/8ecc497404bc76e1abd54e14e869b4b67ead71e289f2fe012ef02735f431c76a.jpg)  
Fig. 5.15: GPS continuously operating reference station (CORS) with receiver (Trimble 5700 GPS and GNSS Choke Ring Antenna, courtesy Trimble Navigation Ltd., Sunnyvale, CA, U.S.A.).

![](images/7e047fb033b295a2d67b2f9f075f27ba500e6e8e223a896fcbe712c6ec00faf7.jpg)  
Fig. 5.16: Geodetic GNSS two-frequency receiver (Leica Viva GS15), with controller (Leica Viva Controller CS15), courtesy Leica Geosystems AG, Heerbrugg, Switzerland.

![](images/a2837f5022d72e79e62cc6a18d97f51e7fd599d0d661c0a28030d456ee8e2331.jpg)  
Fig. 5.17: JAVAD-TRIUMPH-1 Integrated GNSS receiver with fully integrated GNSS antenna, courtesy JAVAD GNSS, Inc., San Jose, CA, U.S.A.

![](images/9ef744e778bbf0648cfffd6eed5a4ed25b80da2613d4317100c0096e89fb7245.jpg)  
Fig. 5.18: GPS/GLONASS rover TOPCON HiPer II, courtesy TOPCON Europe B.V., Capelle a/d IJssel, Netherlands.

![](images/b40bb17b55df2f897e9de1c39f200b77de084a9c2a16a46ad18353ed02551590.jpg)  
Fig. 5.19: Septentrio AsteRx3 HDC GPS/Galileo/GLONASS and COMPASS receiver and PolaNt G antenna, courtesy Septentrio Satellite Navigation NV, Leuven, Belgium.

We now discuss in more detail code and carrier phase measurements employed for GPS navigation and positioning.

Code measurements use the travel time $\Delta t$ of a signal between the satellite and the antenna of the receiver. The time difference is determined by cross-correlating an arriving code sequence with a code copy generated in the receiver. Multiplication of $\Delta t$ with the velocity of light $C$ gives the distance between the satellite and the antenna, cf. [5.1.1]. Considering the receiver clock synchronization error $\delta t ,$ the observation equation for the pseudoranges $R$ reads as

$$
R = c \Delta t = s + c \delta t
$$

The distance is given by

$$
s = \big ( \big ( X _ { s } - X _ { p } \big ) ^ { 2 } + \big ( Y _ { s } - Y _ { p } \big ) ^ { 2 } + \big ( Z _ { s } - Z _ { p } \big ) ^ { 2 } \big ) ^ { \frac { 1 } { 2 } } ,
$$

where $X _ { { _ s } } , ~ Y _ { { _ s } } , ~ Z _ { { _ s } }$ and $X _ { p } , \ Y _ { p } , \ Z _ { p }$ are the geocentric coordinates of the satellite and the ground stations, respectively. The navigation message needed for the evaluation of (5.43) is transmitted on L1 and L2. It contains the satellite’s ephemeris (broadcast ephemeris, accuracy now about $\pm 1 \textrm { m }$ ) in the form of Keplerian elements and certain time derivatives and orbital corrections, the satellite’s clock correction with respect to GPS time, ionospheric correction parameters, and information on the status of the GPS system. Equations (5.43) then provide the coordinates of the ground station and the receiver clock correction from simultaneous measurements to at least four satellites. This presupposes that atmospheric refraction effects are taken into account by proper reductions (see below). The accuracy limit of this method is given by the random noise of the code measurement noise where the noise level may be estimated by $1 \%$ of the signal’s wavelength. This leads to $\pm 3 \textrm { m }$ for the C/A-code and $\pm 0 . 3 \mathrm { ~ m ~ }$ for the P-code, and has in geodesy generally led to the use of carrier phase measurements (see below).

GPS provides two different services for navigation (positioning and timing). The Standard Positioning Service (SPS) only delivers the C/A-code, and is available for all kind of users. An average positioning accuracy $^ { 2 4 \mathrm { ~ h ~ } }$ measurement interval, $9 5 \%$ probality level) of about $\pm 1 0$ m (horizontal) and $\pm 2 0 \textrm { m }$ (vertical) or better can be achieved, but may be worse by a factor of two or more under unfavourable atmospheric and site conditions. The Precise Positioning Service (PPS) uses the P-code (Y-code). It provides all GPS signals and thus the full accuracy of the system, but is reserved to authorized users (U.S. military, U.S. federal agencies, selected allied armed forces). Real-time positional accuracies of better than $\pm 1 0 \textrm { m }$ are attainable with dual-frequency receivers. With GPS being fully operational, an accuracy deterioration for civil users had been introduced by DOD consisting of “selective availability” and “Anti-Spoofi ng”.

Under Selective Availability (SA), the fundamental frequency of the satellite clocks was destabilized, and the ephemeris data were manipulated. This degraded the absolute accuracy to about $1 0 0 ~ \mathrm { ~ m ~ }$ in horizontal position and $1 5 0 ~ \mathrm { ~ m ~ }$ in height. SA was applied only between 1990 and 2000, and after suspension the accuracy of positioning and time transfer reached the previous standard. A more rigorous measure was the introduction of Anti-Spoofi ng (AS) in the middle of the 1990s. Since that time, the P-code has been replaced by the encrypted Y-code, which is non-accessible for civilian users.

Pseudorange differences can be derived from integrated Doppler frequency shifts (Doppler counts) of the carrier frequency according to (5.41) and (5.42). These differences are used for the determination of velocity in navigation. Doppler solutions also play a role in the removal of ambiguities, which occur with carrier phase measurements (see below). The method is not suitable for real-time positioning due to the long observation time required.

Geodesy and surveying require accuracies of at least two orders of magnitude better than that required for navigation. This is achieved by carrier phase measurements. Due to the shorter wavelength of carrier phases, the random measurement noise is now only about $2 \textrm { m m }$ or even less (Beutler et al., 1987; Langley, 1997).

The carrier phase is detected by comparing the received carrier signal with the reference frequency generated in the receiver after subtraction of the code. In order to reconstruct L2 under AS conditions (P-code encryption), different techniques have been developed, such as squaring of L2 (eliminates the code signal) and cross-correlation of L1 and L2. The measured phase difference

$$
\Delta \varphi = \varphi _ { _ c } - \varphi _ { _ 0 }
$$

$( \varphi _ { _ { c ^ { \prime } } } ^ { } \varphi _ { _ { 0 } }$ are phase of the carrier and reference waves, respectively) is related to the distance $s$ by the observation equation

$$
\Delta \varphi = \frac { 2 \pi } { \lambda } ( s - N \lambda + c \delta t ) ,
$$

which is well known also from terrestrial distance measurements, cf. [5.5.2]. $N$ is an integer number of complete carrier cycles within the range $S _ { \prime }$ and $\delta t$ is the receiver clock synchronization error. The ambiguity introduced by $N$ poses a primary problem for the evaluation of (5.45). Among the algorithms available for ambiguity determination, we have the inclusion of ambiguity-free Doppler solutions, the combination of code and carrier phases, and statistical search methods applied to combinations of L1 and L2. Diffi culties arise when the phase lock is lost due to signal obstruction. Such sudden jumps of the carrier phase by an integer number of cycles are called cycle slips. They are either removed during pre-processing or taken into account by introducing an additional ambiguity for the affected pseudorange.

The error budget of GPS pseudorange measurements (as that of other GNSS positioning) contains satellite-specifi c, signal propagation-specifi c and user-specifi c effects, in addition to the random noise. The satellite part contains the satellite’s orbit and clock errors, and the signal propagation is affected by ionospheric and tropospheric refraction. Among the user-specifi c effects are the receiver clock errors and signal propagation delays, antenna phase center variations, multipath effects, and diffraction and signal interference (Seeber, 2003, p. 297 ff.).

Orbital errors are at the order of a few meters for the Standard Positioning Service, while the International GNSS Service (IGS) is able to provide the precise rapid or fi nal (post-processing!) orbits with cm-accuracy (see below). The broadcast clock error corresponds to an orbital error of about $1 \textrm { m }$ , and with the IGS products this error is reduced to the cm-level.

Atmospheric refraction strongly affects the electromagnetic waves while traveling through the atmosphere. Ionospheric refraction acts in a different way on the code signal and the carrier phase, causing a code group delay (pseudorange too long) and a phase advance (pseudorange too short). The effect depends on the (strongly variable) electron content along the signal path and may cause range errors of some meters, reaching eventually some 10 or even $1 0 0 ~ \mathrm { { m } }$ . When only a single-frequency receiver is available, a corresponding reduction has to be based on models of the electron density, cf. [5.1.3]. Among the ionospheric correction models is the development by Klobuchar (1996), which provides the vertical time delay at GPS measurements by exploiting the GPS ionospheric coeffi cients broadcast message. Global (IGS) and regional GPS services also offer ionospheric reduction models, containing TEC information with high time resolution and nearly real-time.

The most effi cient way to eliminate the largest part of the ionospheric refraction effect is the use of two-frequency receivers. The application of (5.23) to the frequencies $f _ { _ 1 }$ and $f _ { _ 2 }$ leads to the reduced distance (for code measurements)

$$
s = \frac { s _ { 1 } f _ { 1 } ^ { 2 } - s _ { 2 } f _ { 2 } ^ { 2 } } { f _ { 1 } ^ { 2 } - f _ { 2 } ^ { 2 } } .
$$

Here, the ionospheric refraction is eliminated, and $s _ { \scriptscriptstyle 1 }$ and $s _ { _ 2 }$ are the observed distances on L1 and L2 respectively; the residual errors do not exceed the cm-order of magnitude. A corresponding equation can be derived for carrier phase observations.

Tropospheric refraction may cause propagation delays of $2 . 3 \textrm { m }$ (zenith direction) to about $2 5 ~ \mathsf { m }$ (at $5 ^ { \circ }$ elevation). It is accounted for by tropospheric models and observed surface weather data, cf. [5.1.2]. The “wet” component remains a critical part of these reductions, which may be accurate to a few cm under ideal conditions and large elevation angles, but could reach a meter uncertainty and more at elevations less than $5 ^ { \circ }$ . Other strategies for reducing the effect of tropospheric refraction include the estimation of a station dependent “zenith scale factor” for each satellite pass and real-time monitoring in active multiple reference station networks (Bevis et al., 1992), cf. [7.3].

Multipath effects result from signal refl ection (at streets, buildings, waterways, etc.) near the antenna. They affect code and carrier phase measurements and can produce errors of a few meters and more at the C/A-code, and of a few cm to dm at carrier phase measurements. Signal diffraction at obstacles and interference with other radiowave sources may also occur. A reduction of these effects is possible by a proper design of the antenna (e.g., at the low-multipath choke-ring antenna used at the IGS stations) and by careful site selection. As the antenna’s electrical phase center does not coincide with the geometric center, a phase center offset occurs (a few mm), which is usually provided by the manufacturer. More critical are the phase center variations, which depend on the satellite’s elevation and azimuth and amount to a few mm to cm (up to $1 0 ~ \mathrm { c m }$ in the vertical). Relative (with respect to a reference antenna) and absolute (using a robot’s rotation and tilting) fi eld calibration methods have been developed in order to model this effect (Görres et al., 2006). These effects also become visible when antennas are changed at continuously operating reference stations, and have to be taken into account accordingly (Wanninger, 2009). Corresponding considerations regarding phase center offsets and variations also have to be made with respect to the satellites’ antennas (Schmid et al., 2005).

The accuracy of GPS positioning depends, in addition to the accuracy of the pseudorange, on the geometric confi guration of the satellites with respect to the receivers and on the duration of the observation time. A longer observation time increases the accuracy, especially for long baselines and for the height component. The accuracy at the kinematic mode (moving GPS antenna) generally is slightly lower than that of the static mode.

The accuracy of an observed pseudorange can be expressed by its standard deviation (also user equivalent range error). The strength of the satellite geometry is characterized by a quantity called “Positional Dilution of Precision” (PDOP). It is defi ned as the ratio between the standard deviation of a position $\sigma _ { p }$ derived from a certain satellite constellation and the standard deviation of an observed pseudorange $\sigma _ { r }$ according to $\sigma _ { _ p } = \mathsf { P D O P } \times \sigma _ { _ r }$ (Langley, 1999). The numerator of this quotient follows from the trace of the coordinates covariance matrix, which depends on the design of the network. PDOP values can be calculated in advance, and then serve for the planning of observations and for rapid information on expected positioning quality. For instance, a PDOP value of 2 (this value is now seldom exceeded) means that the accuracy of positioning is two times worse than the accuracy of the pseudorange observation. If separated into the horizontal and the vertical components, it turns out that the determination of heights is less accurate than horizontal positioning by a factor of about 2. This results from the fact that all observed satellites are above the receiver but azimuthally distributed over the total horizon, and that the receiver clock corrections are strongly correlated with height (Rothacher, 2002).

With respect to the GPS positioning strategy and the accuracy obtained, we may (like in other geodetic space techniques) distinguish between the absolute and the relative mode.

Absolute positioning employs a single receiver and uses the Standard Positioning Service for determining the station coordinates (see above). The accuracy thus remains restricted and does not signifi cantly increase with the observation time. With the use of precise ephemerides and satellite clock corrections provided by IGS (see below) and exploiting code and carrier phase observations this situation is changing, leading to cmaccuracy at post-processing of longer observation series, cf. [7.3].

For orbital errors, a (pessimistic) rule of thumb allows an estimate of the error to be expected in a baseline $b$ from the orbital error dr :

$$
\frac { d b } { b } = \frac { d r } { s } ,
$$

where $s$ is the distance between the satellite and the receiver (maximum $2 5 ~ 0 0 0 ~ \mathrm { k m }$ ). Hence, if an accuracy of $1 \mathrm { { \ c m } }$ is required for the baseline, the orbital error should not exceed $2 . 5 \textrm { m }$ at $b = 1 0 0 ~ \mathrm { k m }$ and $0 . 2 5 ~ \mathrm { m }$ at $b = 1 0 0 0 { \mathrm { k m } }$ . When the precise ephemerides from the IGS are used, orbital errors no longer play a major role.

Relative positioning is accomplished by simultaneous observations (code and/or phase measurements) on two or more stations, including at least one with known coordinates (reference station). This strategy signifi cantly reduces the distance-dependent effects that occur in the absolute mode (orbital errors as well as ionospheric and tropospheric refraction), due to the high error correlation at neighboring stations.

This strategy has been extended by combining observations of different satellites and at different epochs, and code with carrier phase observations. As a consequence, satellite and receiver clock errors can be eliminated, and rapid ambiguity solutions become possible. Station specifi c effects, on the other hand, are uncorrelated and cannot be reduced by differencing, they must be kept small by proper selection of the station and corresponding calibration procedures. At post-processing, this relative GPS solution delivers differences of coordinates (“baseline vectors”) with high accuracy.

Differential GPS (DGPS) has been developed in order to improve the position of a roving station by applying corrections transmitted from a permanently operating reference station to the user in real-time. Corrections may be derived from code observations at the reference station and refer to position or the observed pseudorange. If code-range and (the more precise) carrier phase data are transmitted to the user station (“rover”), the procedure is called precise DGPS or Real-Time Kinematic (RTK) GPS. It delivers the baseline vector in real-time (cm-accuracy over shorter distances) and includes the simultaneous resolution of ambiguities at the rover station. The method can be extended to a network of reference stations (Seeber, 2003, p. 325 ff.; Schön, 2010), cf. [7.3]. For code measurements, the accuracy obtained at relative positioning with good PDOP conditions is $0 . 2 5 \textrm { m + 1 }$ ppm/horizontal, and $0 . 5 \mathrm { ~ m ~ } +$ 1 ppm/vertical. Carrier phase measurements in the static mode can deliver $5 \ : \mathrm { m m } + 0 . 5$ ppm/horizontal and $1 0 \ \mathrm { m m } + 0 . 5$ ppm/vertical in real-time, and could be improved by a factor of about two through post-processing. In the kinematic mode, the accuracy decreases by a factor of about 2. Here and in the following, the distance dependent error part ppm is relative to the baseline length. More details on three-dimensional positioning are given in [6.2.1] and [7.3].

The Global Positioning System (and other GNSS) has drastically changed surveying methods in geodesy, navigation, and other applications. This is mainly due to the high accuracy achieved with static and kinematic positioning, real-time evaluation, and operational fl exibility. Direct visibility between the ground stations is not necessary any more, only visibility to the satellites is required. The system is weather independent and usable day and night. The use of GPS and other GNSS is still increasing and is strongly supported by global and regional services, cf. [7.3].

High-quality GNSS data and products are available through the International GNSS Service (IGS), which operates under the auspices of IAG (Beutler et al., 1999; Dow et al., 2005). Starting as International GPS Service in 1994, more than 200 institutions and agencies now cooperate within this enterprise, with a Central Bureau located at the U.S. Jet Propulsion Laboratory. IGS operates a global network of (today nearly 400) GNSS tracking stations, Fig. 5.20, and some data and data analysis centers, in order to supply observed data and derived products for Earth science research, positioning, navigation and timing. The sites have been carefully selected and monumented (Combrinck and Chin, 2001), and use high performance antennas (Fig. 5.21).

![](images/9e9b72718711a19ea5f284d6b04ec8ebfc08c9708463c3dd1947ee2b475ad7b4.jpg)  
Fig. 5.20: Network stations of the International GNSS Service IGS (status 2010), courtesy IGS (http://igscb.jpl.nasa.gov/ ).

![](images/dd2f36d040d77f6a80aee71be0b6c7e0f3fad1dfee631bdd03ca9e9e69102466.jpg)  
Fig. 5.21: IGS sites HOFN in Höfn, Iceland (left side) and BUCU in Bucharest, Romania (right side), Bundesamt für Kartographie und Geodäsie (BKG), Frankfurt a.M., Germany (http://www.fs.wettzell.de).

The stations are equipped with geodetic two-frequency GPS (GNSS) receivers and generally operate permanently; raw tracking data (phase and pseudorange observations) are provided on hourly basis or even real-time. The IGS products include GPS satellite ephemerides, satellite and station clock parameters, Earth rotation parameters, station coordinates, and ionospheric and tropospheric information. GPS orbits and satellite clock offsets are given on a daily basis, in an ultra rapid (real-time and $3 \mathrm { ~ h ~ }$ delay), rapid and fi nal version. The fi nal “precise” ephemeris (from post-processing) has a precision of about $2 \ \mathrm { c m }$ , the “rapid” ephemeris is only slightly less precise. Satellite and station clock parameters are precise to 0.05 ns, and the quality of derived Earth orientation parameters (polar motion and LOD) is given by 0.05 mas and $0 . 0 2 \ \mathrm { m s } / \mathrm { d a y } ,$ , respectively. Weekly solutions for the station coordinates are characterized by a precision of $2 \textrm { m m }$ (horizontal) resp. $4 \ : \mathrm { m m }$ (vertical), and by 2 resp. $4 \ \mathrm { m m }$ /year for station velocities (Kouba, 2009). By co-location with other geodetic space techniques, the IGS network is connected to the International Terrestrial Reference Frame (ITRF) and contributes signifi cantly to it; IGS stations also play an important role at densifying ITRF on continental scale, cf. [2.4.2], [7.3].

In addition to GPS, there are a number of other Global Navigation Satellite Systems (GNSS) already operating or in the state of development, at global and regional scale (Feairheller and Clark, 2006; Becker, 2009).

A global navigation satellite system similar to GPS has been developed in the former Soviet Union since the 1970s: GLONASS (Global’naya Navigatsionnaya Sputnikovaya Sistema), Hegarty and Chatre (2008). Like GPS, GLONASS is a military system, but it has been stepwise opened to civilian users since the end of the 1980s. The system became fully operational in 1996, and after some drawbacks (lack of satellites) again in 2010. GLONASS operates as a one-way ranging system, with a space segment comprising 24 (including three spares) satellites, Fig. 5.22.

![](images/1bf0d9a41b067c45956994cc8c9db23be8357d7aa20eada38910198c6b46cb42.jpg)  
Fig. 5.22: GLONASS-M satellite, courtesy Russian Federal Space Agency ROSCOSMOS (http://www.federalspace.ru).

The satellites are arranged at a regular spacing of $4 5 ^ { \circ }$ in three nearly circular orbits separated $1 2 0 ^ { \circ }$ apart from each other $( i = 6 4 . 8 ^ { \circ } )$ , $h = 1 9 \ 1 0 0 \ \mathrm { k m } ,$ revolution time 11 h 15 min). This confi guration assures the simultaneous visibility of six to 11 (minimum fi ve) satellites all over the Earth. The satellites transmit on two carrier frequency bands (G1 around $1 6 0 2 ~ { \cal M } { \sf H } z$ and G2 around $1 2 4 6 ~ \mathsf { M H z } )$ , but contrary to GPS with different frequencies for each satellite. The standard-accuracy C/A-code and the high-accuracy P-code modulated onto the carrier frequencies are the same for all satellites. The GLONASS-K generation (since 2010) provides a third carrier frequency (G3: $1 2 0 5 ~ \mathsf { M H z } )$ with an additional civil and military ranging code. There is no degradation of the GLONASS signals, but the P-code has not been offi cially released and may be changed without prior notice. All GLONASS satellites are equipped with laser retrorefl ectors for laser tracking, and timing is provided by three atomic clocks (cesium standards). The control segment consists of a master control station near Moscow and a large number of secondary tracking stations distributed over the territory of the former Soviet Union. The satellite’s navigation message contains the broadcast ephemerides (positions and velocities) and the satellite clock corrections, among others. The accuracy of the predicted orbits and velocities varies between $2 0 ~ \mathsf { m }$ resp. $0 . 0 5 ~ \mathrm { c m / s }$ (along-track) and $5 \textrm { m }$ resp. $0 . 3 ~ \mathrm { c m } / s$ (radially), and will increase by a factor of two to three with the GLONASS-M satellites. The GLONASS results refer to the reference system PZ-90, which is based on the former Soviet Geodetic Reference System 1985 (SGS85), Misra and Abbot (1994). The recent realization (2007) agrees within a few decimeters with the World Geodetic System 1984 (WGS84) and with ITRF. GLONASS uses its own time system $( \mathsf { U T C } + 3 \mathsf { h } )$ which is synchronized to UTC within $1 ~ \mu \mathrm { s }$ by the use of leap-seconds.

By combination of GLONASS with GPS, about 12 to 16 satellites are visible at any place of the Earth, which leads to a better coverage of the sky and an improved (with respect to accuracy and surveying of “shadow areas”) positioning. Consequently, GNSS receivers with GPS and GLONASS (and also Galileo and other satellite navigation systems) capability are commercially produced now, where 20 dual frequency channels are required for a GPS/GLONASS combination (Fig. 5.19).

An European navigation satellite system called Galileo started with a defi nition phase, between 1999 and 2001 (Deisting and Hein, 2006; Hofmann-Wellenhof et al., 2008, p. 341 ff.). The fundamental intention of this enterprise, which is under the supervision of the European Commission and the European Space Agency (ESA), is to establish a global civilian navigation and positioning system especially for Europe and surroundings, serving different demands and providing different levels of accuracy and availability. The system shall be independent from GPS and GLONASS, although it should be inter-operable with those systems. In 2007, the European Union took direct control of the Galileo project (Schüler et al., 2009).

The space segment of Galileo shall consist of $2 7 + 3$ satellites (Fig. 5.23) distributed at $4 0 ^ { \circ }$ distance over three circular Earth orbits which are separated by $1 2 0 ^ { \circ }$ $i = 5 6 ^ { \circ }$ , $h =$ $2 3 ~ 2 6 0 ~ \mathrm { k m }$ , revolution time $1 4 \mathrm { ~ h ~ } 0 4 \mathrm { ~ m i n }$ ), Fig. 5.24. Satellite-borne timing is provided by two rubidium frequency standards and two hydrogen masers, with time stability of 10 and 1 ns/day, respectively. All satellites carry laser refl ectors in order to support the microwave-based orbit determination.

![](images/46c5b35eaf19b27b2f7b02386569e279487cc1075c053a5378db106dcf53fd05.jpg)  
Fig. 5.23: Galileo satellite GIOVE B (Galileo In-Orbit Validation Element), courtesy ESA.

![](images/b08bd6614c2d77580bb2956aa15149eecc3de62b801db4ef198041de19ee7504.jpg)  
Fig. 5.24: Galileo satellite constellation, courtesy ESA.

The following three L-band carrier frequencies bands will be used for navigation and positioning: 1176/1207 and 1192 MHz (E5a, E5b; E5), 1278 MHz (E6), 1575 MHz (E1); the overlay on GPS L1 and L5 and GLONASS G3 frequencies should strengthen the interoperability between the systems. There is an individual code modulation for each satellite (like GPS), and ranging codes and navigation messages will differ according to the application requirements (see below). The system will be operated by three ground control centers, providing orbital data and time synchronization, and supported by about 30 to 40 globally distributed monitoring stations. The “Galileo Terrestrial Reference System” will refer to the actual ITRF. The Galileo system time (GST) is a coordinate time scale, with only small offsets from TAI.

The navigation message, as generated by the ground segment and uploaded to the satellites, will, among others, contain the satellites ephemerides (modifi ed osculating Keplerian elements) and the satellite clock offset GST-TAI. From a total of ten navigation signals, six will be accessible on E5a, E5b and E1 for all users of the Open Service, while two signals on E6 with encrypted ranging codes and correction data are dedicated to users of the Commercial Service. Authorized users of the Public Regulated Service will have access to another two encrypted ranging codes, on E6 and E1. Depending on the carrier frequency, the noise-level of the code-distances is expected to be at the few centimeter to decimeter level, with multipath effects ranging from a few decimeter (open area) to a few meter (urban environment). An accuracy $9 5 \%$ level) of $4 \textrm { m } ( 8 \textrm { m } )$ is envisaged for the horizontal (vertical) position, and 50 ns for the time offset.

The Galileo system has been successfully tested by the GIOVE-A/B satellites (Galileo In-Orbit Validation Element) launched in 2005 and 2008. Further satellites followed in 2011, while the full operational capability is expected not before 2020. As with the GPS/ GLONASS combination, a joint use of Galileo with these systems will result in an increased accuracy and extended application of satellite navigation and positioning. For instance, fully operational GPS and Galileo would allow simultaneous visibility to 15 or more satellites, resulting in improved geometric confi gurations $( \mathsf { P D O P } < 1 . 6 )$ , better ambiguity fi xing, and an improvement of position accuracy by a factor of 2 to 3. For the reduction of ionospheric refraction effects at single-frequency positioning, the Nequick model has been proposed. It will employ ionospheric information from the satellite navigation message together with data from a global sensor network, and thus deliver the time-dependent state of electron density (Leitinger et al., 2005).

Regional satellite navigation systems have been developed or are under development also in other parts of the world, and will partly be extended to global systems (Feairheller and Clark, 2006; Hofmann-Wellenhof et al., 2008, p. 406 ff.). As with the European Galileo system, a main impetus for building up these systems is the desire to become independent from the military-managed systems of the U.S.A. and Russia, with a system completely under national control.

China started the development of a regional satellite navigation system under the name of Beidou-1 in the 1970s. Since the 1990s, the system is upgraded to a global one, with one-way distance measurements similar to GPS and GLONASS: Beidou-2/COMPASS.

The system is operated by the China National Space Administration, and designed as a combination of $2 4 + 3$ satellites in medium height (around $2 1 5 0 0 ~ \mathrm { k m } )$ , which are evenly arranged in three orbital planes $( \mathrm { i } = 5 6 ^ { \circ } )$ ), with additional fi ve geostationary satellites and three satellites in inclined geosynchronous orbits $3 6 ~ 0 0 0 ~ \mathrm { k m } )$ ), Bian et al. (2005). Carrier signals will be emitted in three frequency bands (1575, 1192, $1 2 6 8 ~ \mathsf { M H z } )$ , with satellite-specifi c codes. The fi rst COMPASS-M1 experimental satellite started in 2007, and further satellites followed in 2009/2010, an operational service is expected for 2020. The accuracy of the system’s broadcast information available for civilian use is expected to be at the order of 10 m, $0 . 2 ~ \mathrm { m } / s ,$ and 50 ns for position (geocentric Earth-fi xed reference system compatible with ITRF), velocity and time, respectively (Huang and Tsai, 2008).

Further regional navigation satellite systems are under development in Japan and India. The Japanese Quasi-Zenith Satellite System (QZSS) is a proposed satellite system (fi rst satellite launch in 2010), consisting of at least three satellites in orbital planes $( i = 4 5 ^ { \circ } ,$ , $a = 4 2 ~ 1 6 0 ~ \mathrm { k m } ,$ , $e = 0 . 1$ ) with geosynchronous periods. The system shall complement GPS, but also serve as an autonomous positioning system for eastern Asia and Oceanica, if necessary. The Indian regional navigation satellite system (fi rst satellite launch planned for 2011, system implementation by 2014) is scheduled for a constellation of seven satellites, three of them in geostationary orbit, and the other four operating in geosynchronous orbits $( i = 2 9 ^ { \circ }$ ). With continuous radio visibility to the Indian control stations, dual-frequency operation should provide a position accuracy of better than $2 0 ~ \mathsf { m }$ for India and the surrounding areas.

# 5.2.6 Laser distance measurements

Laser distance measurements are made from ground stations to satellites equipped with corner cube refl ectors: Satellite Laser Ranging (SLR). This method provides high accuracy due to the favorable propagation of laser light in the atmosphere, and it offers a low-cost, long-lifetime space segment. On the other hand, laser measurements depend on weather conditions and require a considerable operational effort at the ground segment (Combrinck, 2010).

At the ground station, ultra-short laser pulses are emitted at epoch $t ,$ refl ected at the satellite, and received again at epoch $t + \Delta t .$ If refraction effects are suffi ciently taken into account by corresponding reductions, the distance is obtained by

$$
s = \frac { c } { 2 } \Delta t ,
$$

it refers to the satellite’s position at the time of refl ection.

We distinguish between the space and the ground segment of SLR. The space segment consists of a laser refl ector array arranged on the satellite’s surface. Since the 1970s, a large number of satellites have been equipped with such arrays, and employed for geodetic positioning and crustal deformation monitoring, determination of Earth rotation parameters, gravity fi eld modeling, and precise orbit determination of dedicated satellite missions.

Dedicated SLR missions for positioning and geodynamic research include the satellites Starlette (France, 1975, $h = 8 0 0$ to $1 1 0 0 ~ \mathrm { k m }$ , $i = 5 0 ^ { \circ }$ ), the Laser Geodynamics Satellites Lageos 1 and 2 (U.S.A., 1976/1992, $h \approx 5 9 0 0 ~ { \mathrm { k m } }$ , $i = 1 1 0 ^ { \circ } / 5 2 ^ { \circ }$ , Cohen et al., 1985; Tapley et al., 1993), Ajisai (Japan, 1986, $h \approx 1 5 0 0 ~ \mathrm { k m }$ , $i = 5 0 ^ { \circ } ,$ , and Etalon 1 and 2 (USSR, 1989, each of the two satellites occupying one of the orbital planes used by GLONASS, Appleby, 1998). These satellites are spherical in shape (diameter 0.2 to

![](images/75c67fc5a7eb1f18f7de8f675c3503cd82adf81497cd819ca6655f92f57dc584.jpg)  
Fig. 5.25: Laser satellite LAGEOS, courtesy National Aeronautics and Space Administration (NASA).

$2 \textrm { m i }$ ) and heavy, and they possess a favorable surface-to-mass ratio (Fig. 5.25). Satellites employed for altimetry and gravity field missions also carry laser retroreflectors on board as well as the GLONASS and a few GPS satellites, and the future Galileo satellites shall also be equipped correspondingly.

The SLR ground segment is represented by the Laser distance measuring system. It consists of the laser unit (Nd:Yag-laser $=$ Yttrium-aluminum garnet crystal doped with neodymium ions), the transmitting and receiving optics (telescopes), and the receiver electronics (secondary-electron photomultiplier). The mechanical mounting provides an automatic tracking (required pointing accuracy $1 ^ { \prime \prime }$ and better) of the satellite’s precalculated orbit, with proper on-line corrections. The travel time is measured by a timeinterval counter, controlled by an atomic clock, which is regularly compared to UTC. A process computer controls the complete measurement, registration and evaluation process.

The accuracy of laser distance measurements depends on the pulse length, the stability of the photomultiplier, and the time resolution. Atmospheric delay is corrected with standard atmospheric models, cf. [5.1.2]. A dual-color laser development aims at the improvement of the refraction correction by exploiting the dispersion of light. Depending on the satellite’s altitude and the constraints of the observation program, some 100 to 1000 distances can be measured during one passage. Third generation lasers operate with pulse lengths of 0.1 to 0.2 ns which corresponds to an accuracy of 1 to $3 \ \mathrm { c m } _ { \rho }$ ; and the single-shot precision is now 5 to $1 0 ~ \mathrm { m m }$ . The amount of photons per pulse reduces signifi cantly on the way from the emission (about $1 0 ^ { 1 5 }$ per pulse) to the receiver, by about 12 or more orders of magnitude, which led to the use of pulse trains (3 to 10 pulses) at a fi xed interval, and the development of single photon detectors. By compressing the data to “normal points” (e.g., at Lageos as the average over $3 0 ~ 5$ to

120 s), sub-cm precision is achieved. Fourth generation lasers will be characterized by repetition rates of $1 0 ^ { 2 }$ to ${ 1 0 ^ { 3 } H z }$ (“kHz-laser”).

About 40 laser-satellite systems are nowadays operating worldwide, either in the stationary (and partly permanent) or in the mobile mode. As an example, the actual Wettzell laser ranging system employs a Nd:Yag laser $5 3 2 \ \mathrm { n m } )$ and a $7 5 ~ \mathrm { c m }$ telescope. It operates with high-energy short pulses (pulse length $1 8 0 ~ \mathsf { p s } ,$ pulse energy $1 0 0 \mathrm { ~ m } |$ ) at a pulse repetition rate of 1 to $1 0 ~ \mathsf { H z }$ in the single-shot mode. Visible and/or infrared light is used, allowing a day-and-night operation to satellites at altitudes between a few 100 and $4 0 \ 0 0 0 \ \mathrm { k m } ,$ Fig. 5.26. Further developments are directed to reduce the pulse length to some 10 ps and to reduce the pulse energy.

Mobile systems have been developed in the U.S.A. and in Germany/Netherlands, among others (Silverberg, 1978). Operating with low energy and single-photon detection, these systems are employed mainly for the investigation of recent crustal movements, cf. [8.3.4]. The NASA SLR-network consists of a number of mobile laser ranging systems distributed worldwide. A transportable, integrated geodetic-observatory (TIGO) is operated by BKG (Bundesamt für Kartographie und Geodäsie, Germany). In addition to the laser unit, it includes a VLBI module and a GPS unit. TIGO is employed for strengthening fundamental reference networks, especially in the southern hemisphere, and is now operating near Concepcion/Chile.

Laser retrorefl ector arrays have been placed on the moon by the U.S. Apollo 11 (1969), 14, and 15 (1971) missions, and the French refl ectors Luna 17 (return signals obtained only in 2010) and Luna 21 were deployed 1970/1973 by the Soviet automatic lunar missions Lunokhod 1 and Lunokhod 2. These refl ectors provide targets for lunar laser ranging (LLR), Shelus (2001) (Fig. 5.27). Pulsed lasers with a tightly bundled beam and a powerful telescope are necessary in order to recapture the weak returning signal. A single photon technique has to be applied as eventually only one photon out of an emitted amount of $1 0 ^ { 1 9 }$ has to be detected. The tracking system must provide a $2 ^ { \prime \prime }$ pointing accuracy. The accuracy of these measurements is about $1 \ \mathrm { c m }$ , and will probably be improved to a few mm.

![](images/d72af7f1b6db18517580ff514a2a0589ff77f4062261c6df651faa4fa3844a97.jpg)  
Fig. 5.26: $7 5 \ \mathrm { c m }$ telescope, Wettzell Laser Ranging System (WLRS), Geodetic Observatory Wettzell, Germany, courtesy Bundesamt für Kartographie und Geodäsie (BKG), Frankfurt a.M., Germany (http://www.fs.wettzell.de).

Observations to the moon have been carried out regularly since 1969 by the McDonald Observatory, University of Texas, and since the 1980s also at the Observatoire de la Côte d’Azur, Grasse/France. At the beginning of the twenty fi rst century a new laser ranging station (APOLLO) with lunar capability was established at Apache Point Observatory, New Mexico, U.S.A. It is equipped with a $3 . 5 \textrm { m }$ -telescope, designed for mm-accuracy. Actual plans for joining the LLR tracking network include the laser ranging systems in Wettzell/Germany and Matera/Italy.

Due to the high accuracy and the long-term stability, LLR results especially contribute to investigations of the dynamics of the Earth-moon system including lunar ephemerides and lunar libration, testing of the theory of relativity, connection of celestial and terrestrial reference frames, and research on terrestrial geodynamic processes and the lunar interior (Müller, 1991; Müller et al., 2007, 2009; Williams et al., 2009).

![](images/37c8fa01e4e859110a07eb3975eed5ee3502559d2ba0b9ecfc5445e0031ead73.jpg)  
Fig. 5.27: Lunar Laser Refl ector, courtesy Lunar and Planetary Institute, Houston, TX, U.S.A. (http://www.lpi.usra.edu).

![](images/b84758c1f3366df54886e97119dae2faadc9c142a495f1942ddb2ac361394d84.jpg)  
Fig. 5.28: Network stations of the International Laser Ranging Service ILRS (status 2011), courtesy ILRS (http://ilrs.gsfc.nasa.gov/ ).

The International Laser Ranging Service (ILRS) of IAG collects, analyzes and distributes the SLR and LLR data sets of presently about 40 stations, heterogeneously distributed over the globe (Fig. 5.28), Pearlman et al. (2007), Pavlis and Müller (2011). In addition to the ephemerides of the observed satellites (cm-accuracy), the service products include weekly solutions of the station coordinates and velocities with an accuracy of $6 \mathrm { { m m } }$ and $2 \ \mathsf { m m }$ /year, respectively; in contrast to other space methods the height accuracy is here better than the accuracy of the horizontal coordinates. The data also contribute to the determination of polar motion and length of day, and they are of special importance for the defi nition of the scale and the origin of the terrestrial reference frame (together with VLBI), and for monitoring the movement of the Earth’s center of mass with respect to the ground stations. SLR observations fi nally are an important data set for the computation of gravity fi eld coeffi cients, providing the long-wavelength part of the fi eld including its variations with time.

# 5.2.7 Satellite altimetry

Satellite altimetry is based on a satellite-borne radar altimeter that transmits short pulses in the vertical direction to the Earth’s surface (Chelton et al., 2001; Chambers, 2009). The ocean surface (and also ice and open water on land) partly refl ects the pulses

perpendicularly, and the measurement of the travel time $\Delta { \sf t }$ furnishes the height of the satellite above the instantaneous sea surface (Fig. 5.29):

$$
a = { \frac { c } { 2 } } \Delta t .
$$

(The denotation a should not be confused with the abbreviation for the semi-major axes of the satellite’s orbit and of the Earth ellipsoid.)

In spherical approximation, the altimetric result can be expressed as

$$
a = r _ { s } - r _ { p } - ( N + 5 5 \mathsf { T } ) ,
$$

where $r _ { s }$ and $r _ { p }$ are the geocentric distances to the satellite and to the subsatellite point $P$ on the ellipsoid, and $r _ { \mathfrak { s } } - r _ { \mathfrak { p } }$ is the satellite’s height above the ellipsoid; $N$ is the geoid height and SST the height of the sea surface topography. A proper reduction of atmospheric refraction effects and ocean tides is presupposed in (5.49b). Tracking provides the satellite’s orbit and thus $r _ { s ^ { \prime } }$ and geodetic positioning gives $r _ { p } .$ . According to (5.49b), altimetry thus delivers information on the geoid and on sea surface topography. An ellipsoidal development of (5.49b) is given by Gopalapillai (1974).

Radar altimeters operate in the $1 4 ~ \mathrm { { G H z } }$ frequency range (corresponding to a wavelength of $2 . 2 \ \mathrm { c m } )$ with short (a few ns) pulses and a high-pulse frequency (e.g., 100 pulses/s). The effects of beam divergence and fi nite pulse length result in measurements that refer to a “mean” sea surface within a circular “footprint” (few km diameter); shortwavelength features of the ocean (waves) are thereby smoothed out. For example, by averaging the measurements over one second, the along-track resolution is about $7 ~ \mathrm { k m }$ .

Satellite altimetry missions are designed to provide either an exact repetition of ground tracks (days to weeks) or a dense pattern of profi les. The different modes are achieved by orbital maneuvers (Knudsen, 1993). The latter is for determination of the altimetric geoid according to (5.49b), and the former for investigation of ocean variability (Fig. 5.30).

The fi rst global survey with a radar altimeter was accomplished by the GEOS-3 satellite (U.S.A., 1975–1978). The oceanographic satellites SEASAT (1978) and GEOSAT (U.S. Navy, $1 9 8 5 -$ 1990) carried improved altimeter systems and operated in heights close to $8 0 0 ~ \mathrm { k m }$ with $1 0 8 ^ { \circ }$ inclination and repetition rates of 3 and 17 days (McAdoo and Sandwell, 1988). The European Remote Sensing Satellites ERS-1 (1991–1996) and ERS-2 (1995–2007) operated at similar heights with $9 8 ^ { \circ }$ inclination (Fig. 5.31). Repetition rates were 35 and 168 days, respectively, and ground track distances at the equator $8 0 ~ \mathrm { k m }$ and $8 ~ \mathrm { k m }$ for geodetic missions (JGR, 1998). The NASA/ CNES (French space agency) TOPEX/Poseidon satellite (1992–2005, 5.3 and $1 3 . 6 ~ \mathrm { { G H z } } )$ was placed in a circular orbit at an altitude of $1 3 4 0 ~ \mathrm { k m }$ and an inclination of $6 6 ^ { \circ }$ . Repetition time was 10 days, and the equatorial ground track interval $3 1 6 ~ \mathrm { k m }$ (Fu et al., 1994; Cheney, 1995), see Fig. 5.32. GEOSAT follow-on (GFO, launch 1998), JASON-1 (2001–2008) and JASON-2 (since 2009), and the Environmental Satellite ENVISAT (since 2002) are successor missions of GEOSAT, TOPEX/Poseidon and ERS-1/-2, with similar orbital parameters. GPS and DORIS as well as laser retro-refl ector arrays serve for orbit determination at these recent altimetry missions.

![](images/8acdb2f204390de534dffffcb57240ce40fdeec136613f8b962134d8946236ee.jpg)  
Fig. 5.29: Satellite altimetry principle.

![](images/1f20c71ea18370a92ff1242fd329c0dbde34f3e50b5c39e090ca8952601ddb82.jpg)  
Fig. 5.30: TOPEX/Poseidon subsatellite tracks covered within the 9.9 days repeat cycle, Bosch (2001a).

![](images/e75898ab89ebd3883420482206063ade6a78cdfbce30c445f88ed8ab9cea82af.jpg)  
Fig. 5.31: European Remote Sensing (altimeter) Satellite ERS, courtesy ESA.

![](images/5ce504f42fb0af649e2b213f804deba80586ed7c388b9bd0835888b80ed92166.jpg)  
Fig. 5.32: TOPEX/Poseidon (altimeter) satellite, courtesy JPL/NASA, Pasadena, CA, U.S.A.

Dedicated altimetry missions deal with the repeated survey of the polar ice caps and the sea ice, in order to get more insight into the ice sheet mass balance. The NASA ICESat $\mathrm { l c e } ,$ Cloud, and land Elevation Satellite) operated from 2003 to 2009 in a near-polar orbit (altitude $6 0 0 ~ \mathrm { k m }$ , $i = 9 4 ^ { \circ }$ ). The satellite carried, among others, a laser altimeter (pulse length 5 ns, 40 $\mathsf { H } z$ shot repetition rate) and a dual-frequency GPS receiver. The laser range precision (0.1 m) decreased with increasing ice slope, and the vertical orbit error was $0 . 0 5 \mathrm { ~ m ~ }$ . An ICESat-2 mission is scheduled for 2015. Determination of ice topography and monitoring of ice height changes is also pursued by the ESA CryoSat-2 mission (altitude $7 2 0 ~ \mathrm { k m }$ , $i = 9 2 ^ { \circ }$ ) which was launched again in 2010, after the launch failure of CryoSat-1 in 2005. Height measurements are performed with a radar altimeter (few cm precision, horizontal resolution about $3 0 0 ~ \mathrm { { m } }$ ), and for orbit determination the satellite is equipped with a DORIS receiver and laser retro - r efl ectors (Wingham et al., 2006).

The error budget of satellite altimetry is composed of orbit errors, instrumental errors, and signal propagation errors.

In order to achieve high radial-orbit accuracy, the satellites are equipped with laser retrorefl ectors for SLR, and additionally with microwave-based positioning systems such as Doppler, GPS, and DORIS (Andersen et al., 1998), cf. [5.2.3]. Further orbital improvements have been achieved by “tailored” gravitational fi eld models developed for each dedicated altimeter mission (Tapley et al., 1996). The orbital error thus has been reduced from about $0 . 5 ~ \mathsf { m }$ for the GEOS-3 mission to a few cm for TOPEX/Poseidon and other more recent altimeter missions.

The precision (instrumental noise) of a one-second-mean altimeter observation is now better than $2 \mathrm { \ c m }$ . Systematic instrumental effects (altimeter bias and drift) can be determined by calibration over ground-truth test areas, while the correction of sea state effects requires a careful signal analysis. The atmospheric propagation delay is taken into account by appropriate models, improved by simultaneous radiometer measurements of the water vapor for tropospheric refraction, and by the use of two frequencies for modeling the ionospheric refraction, cf. [5.1.3]. After reduction of the ocean tides and large-scale air pressure effects, the altimetric results refer to the quasi-stationary sea surface and yield its height with an accuracy of a few cm. For the evaluation of a region sampled multiple times with high spatial-resolution altimeter profi les, the track crossover discrepancies can be adjusted by minimum conditions modeling the errors by time-dependent functions as low-degree polynomials (e.g., shift and inclination), splines or Fourier series (Van Gysen and Coleman, 1997). A multi-mission discrete crossover analysis of nearly simultaneous tracks has proved to be a powerful tool for cross calibration and detection of relative range biases (Bosch and Savcenko, 2007).

Monitoring of the sea surface by means of refl ected GPS signals is still in the experimental stage. This method could possibly supplement satellite altimetry especially with respect to real-time determination of sea level and wave heights.

# 5.2.8 Satellite-to-satellite tracking, satellite gravity gradiometry

High-resolution gravity-fi eld determination from space requires low-orbiting satellites and highly sensitive sensors, cf. [5.2.3]. This can be achieved by satellite-to-satellite tracking and satellite gravity gradiometry (Balmino et al., 1999; Rummel et al., 2002; Ilk et al., 2005a).

Satellite-to-satellite tracking (SST) employs microwave systems (laser distance measurements are under investigation) for measuring range and range rates between two satellites. High-low (several high and one low-fl ying satellite) and low-low (two lowfl ying satellites at the same altitude) confi gurations have been designed, a combination of both confi gurations is possible, Fig. 5.33. The basic observables are the range rates and the changes of the range rates along the line of sight between the satellites, these variations are due to gravitational and non-gravitational “disturbing” forces, cf. [5.2.2]. The gravitational fi eld parameters (harmonic coeffi cients) can be derived after proper reduction of the effects of surface forces derived from dedicated accelerometer measurements, cf. (5.35). In order to achieve a gravity fi eld resolution of $1 0 0 \mathrm { k m } ,$ , the orbital altitude of the lower satellite must not exceed a few $1 0 0 ~ \mathrm { k m }$ (Jekeli, 2001b). The relative velocity between the satellites has to be determined with an accuracy of 1 to $1 0 \ : \mu \mathrm { m } / s ,$ and precise orbit determination should be guaranteed by on-board satellite systems (GPS), supported by ground tracking stations.

![](images/e339f8f6565cac6ba041400e74ebaf27d52164976e3661e98c694508fb58e92c.jpg)  
Fig. 5.33: Satellite-to-satellite tracking principle: a) high-low mode and b) low-low mode for the determination of range and range rate.

SST experiments started in the 1970s, e.g., between GEOS-3 and the geostationary satellite ATS-6 (nearly circular equatorial orbit, $h \approx 3 6 0 0 0 ~ \mathrm { k m } )$ . The CHAMP satellite (GFZ and DLR/ Germany, 2000–2010) started a series of dedicated gravity fi eld missions (Reigber et al., 2006; Flechtner, 2010). It was launched into a decaying orbit starting at an altitude of $4 5 0 \mathrm { k m } ,$ , which was raised several times in order to extend the satellite’s lifetime. CHAMP (dimensions $4 \mathrm { m } \times 1$ $\mathsf { m } \times 1 . 6 \mathsf { m } )$ ) moved in a nearly circular polar-orbit $( i = 8 7 ^ { \circ } )$ ), Fig. 5.34. It carried a special (NASA) GPS receiver for continuous tracking (high-low mode) and a laser refl ector array for ground support, cm-accuracy was thus achieved for the satellite’s orbit. A three-axis accelerometer was used for measuring (precision $ { | 0 ^ { - 8 } \mathrm { m } \mathrm { s } ^ { - 2 } \mathrm { \Omega } }$ ) non-conservative forces as air drag and solar radiation, for later correction in post-processing. As this instrument was located in the satellite’s center of mass, where gravity is compensated by the centrifugal force, it measured only the nongravitational accelerations. A star imager provided attitude information and spatial orientation with respect to the inertial system. A magnetometer and a digital ion drift meter augmented the instrumentation. Gravity fi eld recovery up to degree and order 120 was achieved, and the longwavelength part of the geoid (until degree and order 30) could be derived with “cm-accuracy”. Atmospheric sounding by GPS radio occultation was another result of the mission (Wickert et al., 2010).

The GRACE mission (NASA/German Aerospace Center DLR) started in 2002, and is now expected to continue until 2015. Primary mission objectives are the determination of the global highresolution gravity fi eld and especially its temporal variations. The mission employs two satellites of the CHAMP type orbiting at the same altitude (initially about $4 9 0 \mathrm { k m } )$ ) and in a nearly circular orbit $( i = 8 9 . 5 ^ { \circ } )$ , with a varying (around $2 2 0 \mathrm { k m }$ ) along-track separation (Fig. 5.35), Tapley et al. (2004). The intersatellite tracking (low-low mode) delivers range and range rate measurements (K-band microwave measurements with two frequencies $2 4 \ \mathrm { G H z } ,$ $3 2 \mathrm { \ G H z }$ , μm-accuracy,

![](images/c1fb39de2372f60b6030a7a935620dcbe2da5c1492b4b61e615fd399b1693b42.jpg)  
Fig. 5.34: CHAMP satellite, courtesy GFZ German Research Centre for Geosciences, Potsdam, Germany.

![](images/9936b69b8651823c8a74278fd22660295169fe18c650338a375a3d104b79be7f.jpg)  
Fig. 5.35: GRACE satellites, courtesy NASA.

$1 0 \ H z$ sampling rate) between the satellites. Kinematic orbit determination is based on GPStracking (high-low mode) supported by laser distance measurement from ground stations to the satellites’ nadir-directed laser retrorefl ector. Based on 5-minutes position series, an orbital accuracy of 1 to $2 \mathrm { \ c m }$ is achieved. Attitude control is provided by star sensors, in connection with a GPS navigation solution. As at the CHAMP mission, a three-axis accelerometer is located in each satellite’s center of mass and measures the non-conservative forces.

As a result from the GRACE mission, the static gravity fi eld could be signifi cantly improved in the long- and medium-part, and modeled up to spherical degree and order 150 to 180, with accuracies of 10 to $3 0 \mu \mathrm { m } \mathrm { s } ^ { - 2 }$ for the gravity anomalies and $_ { 0 . 1 \textrm { m } }$ for the geoid (“cm-accuracy” for the geoid part until degree 100), cf. [6.6.3]. Temporal variations of different origin have been found from monthly resp. weekly solutions, which are complete to degree and order 120,120 and 30, 30 respectively, cf. [8.3.5].

In satellite gravity gradiometry, the second derivatives of the gravitational potential $V$ are used for gravity fi eld determination, and derived from the output of a gravity gradiometer (Fig. 5.36, Fig. 5.37), Rummel (1986), Esa (1999). The individual derivatives are generally combined in the gravitational gradient tensor (Marussi tensor)

$$
\mathbf { V ^ { \prime \prime } } = { \left| \begin{array} { l l l } { V _ { _ { x x } } } & { V _ { _ { x y } } } & { V _ { _ { x z } } } \\ { V _ { _ { y x } } } & { V _ { _ { y y } } } & { V _ { _ { y z } } } \\ { V _ { _ { z x } } } & { V _ { _ { z y } } } & { V _ { _ { z z } } } \end{array} \right| } ,
$$

with the $x$ -axis pointing in fl ight direction, the $\gamma$ -axis in cross-track direction, and the $Z$ -axis in the outward radial direction, cf. [3.2.2]. From the nine elements in (5.50) only fi ve are mutually independent, due to the tensor’s symmetry and Laplace’s equation, as demostrated by (3.46) and (3.49) for the gravity fi eld. By different orientation of the sensors, different components of the gravity gradient can be determined.

On the Earth’s surface, gravity gradiometry has been employed since about 1900 with sensor pairs (accelerometers) sensitive to local changes of the gravity fi eld in a certain direction, advanced gradiometric airborne techniques are used today in geophysics, cf. [5.4.5].

![](images/477c5ae532fdec897dd0951d660fe74fd9e32a0a314634bc5ba88d4f2eb41013.jpg)  
Fig. 5.36: Satellite gravity gradiometry principle, modifi ed after Rummel et al. (2002).

![](images/f15b22f7afa7b1adc8ab7d92951ce34ff1cb5d51845fbfc604be7c6504047186.jpg)  
Fig. 5.37: GOCE Gravity gradiometer, courtesy ESA, modifi ed after Rummel et al. (2009).

For space-borne applications, the attenuation of the gravity fi eld with height (the second derivatives of the potential diminish with the third order of the radial distance!) requires a high measurement accuracy for the second derivatives. In the frequencies of interest (medium- and short-wavelengths’ parts of the gravity fi eld), the signals to be detected____ are of the order of ${ { 1 0 ^ { - 9 } } } { \varsigma ^ { - 2 } } / { \sqrt { \mathsf { H z } } }$ only, at heights of a few $1 0 0 \mathrm { k m }$ . This requires a measurement accuracy at the order of $1 0 ^ { - 1 \mathrm { i } }$ to ${ 1 0 } ^ { - 1 \breve { 3 } } { \varsigma } ^ { - 2 }$ (Rummel, 1997). In addition to the gravity gradient tensor, the gradiometer output contains two terms which describe the orientation of the satellite with respect to an inertial system, and the effect of non-gravitational forces. The latter effects can be derived from the sum of the accelerometer pair outputs, and they cancel partly (linear parts) when differencing them (Moritz, 1968b). They can be compensated by a drag control system using thrusters (“drag-free” system). After proper compensation, the observation equation of satellite gravity gradiometry then reads as (Müller, 2001; Rummel et al., 2011)

$$
\Gamma = \mathbf { V } ^ { \prime \prime } + \Omega \boldsymbol { \Omega } + \dot { \boldsymbol { \Omega } } .
$$

The skew-symmetric matrices $\pmb { \Omega }$ and $\dot { \Omega }$ contain the components of the angular velocity around the $x \mathrm { - , ~ } y \mathrm { - }$ and $Z$ -axes and the corresponding angular acceleration, the tensor $\Omega \Omega$ is symmetric:

$$
\begin{array} { r l } & { \Omega \Omega = \left( \begin{array} { c c } { - \Omega _ { y } ^ { 2 } - \Omega _ { z } ^ { 2 } } & { \Omega _ { x } \Omega _ { y } } & { \Omega _ { x z } } \\ { \Omega _ { x } \Omega _ { y } } & { - \Omega _ { x } ^ { 2 } - \Omega _ { z } ^ { 2 } } & { \Omega _ { y } \Omega _ { z } } \\ { \Omega _ { x z } } & { \Omega _ { y } \Omega _ { z } } & { - \Omega _ { x } ^ { 2 } - \Omega _ { y } ^ { 2 } } \end{array} \right) , } \\ & { \dot { \Omega } = \left( \begin{array} { c c } { 0 } & { \dot { \Omega } _ { z } } & { - \dot { \Omega } _ { y } } \\ { - \dot { \Omega } _ { z } } & { 0 } & { \dot { \Omega } _ { x } } \\ { \dot { \Omega } _ { y } } & { - \dot { \Omega } _ { x } } & { 0 } \end{array} \right) . } \end{array}
$$

This rotational part of the observation equations can be derived from combinations of the gradiometer observation equations, supported by orientation data from star trackers. Special emphasis has to be laid on the accelerometers’ calibration (scale, orientation, misalignments) realized in space and through comparison with ground truth. High requirements are posed on the satellite’s orbit, which by orbital analysis also delivers the long-term parts of the gravitational fi eld. Orbit determination is nowadays usually based on GNSS-tracking, with support through ground-based laser measurements (Jarecki and Müller, 2009).

![](images/9af5f45bff3dbab30125f33cf861787961f4024f3b0bb6ef5e973f1fb808309a.jpg)  
Fig. 5.38: GOCE satellite, courtesy ESA.

ESA has started (launch 2009) the fi rst dedicated gravity gradiometry mission called GOCE (Gravity Field and Steady-State Ocean Circulation Explorer, Fig. 5.38.), with a drag-free satellite in a sun-synchronous near circular orbit $( h = 2 6 5 ~ \mathrm { k m }$ , $i = 9 7 ^ { \circ }$ ), Drinkwater and Haagmans (2007), Rummel et al. (2009), Rummel and Gruber (2010), also Rummel, 2011). Orbit determination is performed by satellite-to-satellite tracking, from the on-board dual-frequency GPS receiver (high-low mode positioning), and the satellite is also equipped with laser retrorefl ectors. Three___ accelerometer pairs (precision of a few ${ 1 0 ^ { - 1 2 } \mathrm { s } ^ { - 2 } } / { \sqrt { \mathsf { H } z } } ,$ , sampling rate 1 s) are arranged over three mutually orthogonal directions, with baselines of $5 0 \mathrm { c m } _ { \rho }$ , and Earth-pointing orientation (attitude control) is provided by star trackers and gradiometer data. While the diagonal element of the gradient tensor and the horizontal gravity gradient’s component in fl ight direction $( V _ { x z ^ { \prime } } , V _ { z x } )$ can be determined with high accuracy, the off-diagonal elements are less accurate due to specifi c constraints at ground-based pre-calibration. At modeling, the low-degree potential terms (up to about degree and order 50) will be determined primarily through orbital analysis from GPS tracking, while the higher degrees will be derived from the gradiometer measurements. Based on orbital data and gradiometer results, a fi rst gravity model could be derived complete to degree and order 224, with an accuracy of better than $0 . 1 \textrm { m }$ (geoid) and $3 0 \mu \mathrm { m } \mathsf { s } ^ { - 2 }$ (gravity anomalies). Accuracies around $2 \mathrm { \ c m }$ and $1 0 ~ { \mu \mathrm { m s } } ^ { - 2 } ,$ , respectively, are expected for the full mission period originally planned for about 1.5 years (Pail et al., 2010a).

# 5.3 Geodetic astronomy

Classical geodetic astronomy is concerned with the determination of astronomic latitude, longitude, and azimuth from ground-based optical direction measurements to fi xed stars, which also requires time determination (Mueller, 1969; Schödlbauer, 2000). Several types of observational instruments are available for this purpose [5.3.1], and different methods of observation have been developed [5.3.2]. A number of reductions are necessary in order to refer the observations to the celestial reference frame [5.3.3].Geodetic astronomy is based on astrometric methods and spherical astronomy (Eichhorn, 1974; Kovalevsky, 2002; Kovalevsky and Seidelmann, 2004).

The importance of optical astrometry has decreased since the development of effi - cient satellite positioning and gravity fi eld determination methods, and is now restricted to more local applications of gravity fi eld (plumb line direction, geoid) and azimuth determinations. On the other hand, radio waves emitted from extragalactic sources are used extensively in order to derive base-line vectors between fundamental terrestrial stations and to determine Earth orientation parameters: Very Long Base Line Interferometry [5.3.4].

# 5.3.1 Optical observation instruments

Optical observations to fi xed stars are carried out in the local level (horizon) system. The direction to a star is determined by the astronomic azimuth $A$ and the zenith angle $Z$ (sometimes the altitude or elevation angle $9 0 ^ { \circ } - Z$ is used), cf. [2.5]. Due to the relative movement of the observer with respect to the stars, simultaneous time measurements are required.

Time determination in optical geodetic astronomy requires an accuracy of $1 \ \mathsf { m s }$ . This is provided by quartz clocks, which are based on quartz crystal oscillators (frequency stability $1 0 ^ { - 8 }$ to $1 0 ^ { - 9 }$ over a few hours) and synchronized by time signals. Nowadays a simple time measurement is possible with a GNSS receiver, cf. [5.2.5]. In order to record the time of a star transit through the horizontal or vertical thread of a telescope, a registration device has to be implemented in the measurement system.

Astronomic instruments are either permanently installed in observatories or constructed as transportable devices for fi eld operation.

Until the 1980s, observations of highest precision with stationary instruments have been utilized by the former International Time Service and International Polar Motion Service. Among other instruments, the photographic zenit tube has been employed. In this case, stars near the zenith are photographed symmetrically with respect to the meridian, and the direction of the vertical was established by a mercury pool. By employing CCD-techniques, this method is still of signifi cance for astronomy. Comparable precision $\left( 0 . 0 5 ^ { \prime \prime } \right)$ ) was achieved by the Danjon prism astrolabe, measuring the transit time of stars crossing a defi ned almucantar (see also below under “prism astrolab”). These observatory measurements, in connection with satellite-based astrometry, still contribute to the realization of an optical celestial reference frame, cf. [2.4.1].

The universal instrument was employed for fi eld measurements of fi rst-order precision $( 0 . 1 ^ { \prime \prime }$ to $0 . 3 ^ { \prime \prime } .$ ). It consists of a high-precision theodolite, cf. [5.5.1], of very stable design with a few attachments for astronomic observations (Fig. 5.39).

An angled telescope permits observations near the zenith. The movable thread of the registering micrometer is driven to follow the star so that impulses are generated and recorded at uniform intervals. The suspension level serves to measure the tilt of the horizontal axis. The Horrebow level, mounted at right angles to the horizontal axis, registers any changes in the tilt of the telescope. The Kern DKM3-A and the Wild T4 universal theodolites were used widely.

The prism astrolab is used for the simultaneous observation of astronomic latitude and longitude. With this device, one measures the transit times of those stars that cross the same small-circle parallel to the horizon (almucantar). The constant zenith distance (usually $\approx 3 0 ^ { \circ } .$ ) is realized by a prism placed in front of the telescope, and the direction of the vertical is defi ned by the surface of a pool of mercury or by a compensator pendulum. Astrolabe attachments were particularly common. They have been mounted either on a theodolite (e.g., the Wild T3 astrolabe with a mercury pool) or on an automatic level (Zeiss Ni2 astrolabe, Fig. 5.40).

![](images/7288f575b8c0a4fa9dde595270223cc7ab3699b2caad33dd3b7993c235dd445b.jpg)  
Fig. 5.39: Universal instrument Kern DKM3-A, Kern/Leica Geosystems AG, Heerbrugg, Switzerland.

![](images/0a5f59caa346ca6dbfa460403428f96a994e9fe66ea24f45643aa5368122dce1.jpg)  
Fig. 5.40: ZEISS Ni2 level with prism astrolab, Carl Zeiss, Oberkochen, Germany.

Transportable zenith cameras have been developed for the rapid determination of astronomic latitude and longitude, and have proved to be very effi cient (Seeber and Torge, 1985; Kovalevsky, 2002). The development started with photographic instruments, consisting of a camera oriented in the direction of the plumb line (focal length 300 to $1 0 0 0 ~ \mathrm { { m m } }$ , relative aperture $\approx 1 { : } 5$ ), which could be rotated around the plumbline axis in any azimuth. The photography of the zenith-near fi eld of stars with the subsequent (tedious) comparator measurement of the photographic plate coordinates has been substituted now by an electronic image procedure using CCD-technique, followed by the transformation into the astronomical system.

The principle of CCD (charge-coupled device) is based on the photoelectric effect produced on a semiconductor plate. The number of collected photoelectrons is proportional to the light received. A CCD-matrix is composed of a number of linear arrays and may contain several 1000 $\times ~ 1 0 0 0$ pixels, of $1 0 \mu \mathrm { m }$ or less size, with a resolution of 0.1 pixels.

In addition to the camera-system and a timing device, a digital zenith camera system contains two electronic tilt meters that are arranged at right angles to each other, and serve for the automatic alignment of the camera to the plumb line. A single observation comprises two images of zenithal stars, exposed in opposite camera directions, and the exposure epochs and tilt measurements. Using an image processing unit and a ${ \mathsf { P C } } ,$ an automatic on-line evaluation of the star observations is achieved, which includes the transformation of the CCD-coordinates into the $\alpha ,$ $\scriptstyle { \delta }$ system, and results in the astronomic latitude and longitude of the observation site. Digital zenith camera systems have been developed over the past decades at a few institutions, and are now employed for the determination of vertical defl ections along profi les or in areas of limited extension, cf. [6.7.4], Fig. 5.41. These systems include a GPS receiver which is used for time tagging of the exposure epochs and for determining geodetic latitude and longitude. Main error sources are of astrometric type (image centering, catalogue positions, scintillation), followed by tilt corrections, while errors of time tagging and geodetic coordinates play a minor role (Hirt and Bürki, 2003; Hirt and Seeber, 2008).

![](images/4c7d9c5980f27767d103fdcfa66499a051c5eae9cc575cd4534aad5cd81ec043.jpg)  
Fig. 5.41: Digital Astronomical Defl ection Measuring System (DIADEM), Geodesy and Geodynamics Laboratory, ETH Zürich and Digital Transportable Zenith Camera, TZK2-D System, Institut für Erdmessung, Universität Hannover (Hirt and Bürki, 2006).

With the Hannover Digital Zenith Camera System a single observation takes approximately 30s, and the image usually contains 20 to 50 stars. The evaluation results in an accuracy of about $0 . 2 { ^ { \prime \prime } }$ to $0 . 3 ^ { \prime \prime } ,$ , which can be improved by multiple observations. With a one-hour observation time (100 observations) an accuracy of $0 . 0 5 ^ { \prime \prime }$ to $0 . 1 { ^ { \prime \prime } }$ is obtained.

# 5.3.2 Astronomic positioning and azimuth determination

The determination of astronomic latitude, longitude and azimuth is based on the relations given in [2.5], where the star positions $( \alpha , \delta )$ are provided by star catalogues.

Star catalogues have been compiled since ancient times, cf. [2.4.1], and in a more regular manner since the nineteenth century. Derived from Earth-based astrometry, the number of stars observed and their positional accuracy had reached a certain limit in the second half of the twentieth century, examples are the AGK-catalogues (northern hemisphere) of the “Astronomische Gesellschaft” and the SAO (Smithsonian Astrophysical Observatory) Catalogue of 1966. These rather heterogeneous compilations fi nally included a few $1 0 0 ~ 0 0 0$ stars, with accuracies not exceeding $0 . 1 ^ { \prime \prime } . . . 0 . 2 ^ { \prime \prime }$ . The HIPPARCOS space mission (since 1989) and the introduction of CCD-techniques signifi cantly improved quantity and quality of star catalogues. The TYCHO catalogue (2000) is based on star-mapper data from the HIPPARCOS satellite, it contains about 2.5 million stars with an accuracy of $0 . 0 1 ^ { \prime \prime } . . . 0 . 0 2 ^ { \prime \prime }$ (Høg et al., 2000). We further mention the UCAC Astrograph Catalogues of the U.S.Naval Observatory which provide positions with an accuracy between $0 . 0 2 ^ { \prime \prime }$ and $0 . 1 ^ { \prime \prime } ,$ , for stars down to a magnitude of $1 6 ^ { \mathfrak { m } } ,$ and about 2000 stars per square degree (Zacharias et al., 2004). For future space missions as GAIA see [2.4.1].

As the relevance of astrometry in geodesy has decreased during the last decades, we mention here only a few of the many methods developed in geodetic astronomy.

In determining the astronomic latitude $\Phi$ , it is required, according to (2.20), to ascertain the zenith angle $Z$ and the hour angle $h .$ . The zenith angle can be directly observed, while the hour angle has to be derived from the rectascension $\alpha$ and the measured time, see (2.21).

By total differentiation of (2.20) we obtain differential formulas for estimating the effect of observational errors on the results and for fi nding optimum confi gurations for the observations, e.g., Schödlbauer (2000, pp. 34 and 505 ff.). For the latitude we obtain

$$
d \Phi = - \frac { 1 } { \cos A } d z - \cos \Phi \tan A d h ,
$$

where we have neglected the (small) declination error. The accuracy of $\Phi$ hence strongly depends on the azimuth, with minimum effects of errors in $Z$ and $h$ at $A = 0 ^ { \circ }$ and $A = 1 8 0 ^ { \circ } ,$ , i. e., at meridian transits of the star.

For an upper culmination (the smaller zenith angle) of a northern star $( A = 0 ^ { \circ }$ ) or a southern star $\mathit { \Pi } ^ { ' } A = 1 8 0 ^ { \circ }$ ), the latitude is given by (see also Fig. 2.4)

$$
\Phi = \delta _ { _ { N } } - z _ { _ { N } } \mathrm { a n d } \Phi = \delta _ { _ { S } } + z _ { _ { S } } ,
$$

respectively. Measuring the meridian zenith angle (e.g., to Polaris) is therefore most suitable for the determination of the latitude.

If one observes a pair of stars consisting of both a northern and a southern star having approximately the same zenith angle, averaging (5.54) signifi cantly reduces the uncertainties in $Z$ due to refraction (Sterneck method):

$$
\Phi = \frac { 1 } { 2 } \big ( \delta _ { _ { N } } + \delta _ { _ { S } } \big ) + \frac { 1 } { 2 } ( Z _ { _ { S } } - Z _ { _ { N } } ) \cdot
$$

In the Horrebow-Talcott method, the small difference between the meridian zenith angle of the northern and southern stars in a star pair is measured by a registering micrometer. The optical axis in each case is adjusted to the same zenith angle using the Horrebow level that is mounted on the horizontal axis. Since accurate circle and time readings are not required, this method provides precise results, with an accuracy of $0 . 1 { ^ { \prime \prime } }$ when about 20 star pairs are observed.

The astronomic longitude $\Lambda$ is given by the difference between the local sidereal time LAST and the Greenwich sidereal time GAST (2.22):

$$
\Lambda = \mathsf { L A S T } - \mathsf { G A S T } ,
$$

where 1 s corresponds to $1 5 ^ { \prime \prime }$ . According to (2.21), LAST is related to the hour angle h:

$$
\mathsf { L A S T } = h + \alpha .
$$

If the latitude is known, $h$ can be computed from the zenith angle according to (2.20):

$$
\cos h = \frac { \cos z - \sin \Phi \sin \delta } { \cos \Phi \cos \delta } .
$$

Converting measured universal time UT to GAST then allows the determination of $\Lambda$ according to (5.56).

By differentiating (2.20), we get the differential relation for the hour angle:

$$
d h = - \frac { d z } { \sin A \cos \Phi } - \frac { \cot A } { \cos \Phi } d \Phi .
$$

The effect due to errors in $Z$ is minimum when observations are made on the prime vertical $( A = 9 0 ^ { \circ } )$ ), while the effect is zero for errors in $\Phi$ . The infl uence of refraction is largely eliminated when observing east and west stars of the same altitude that are symmetric with respect to the meridian. On the other hand, by observing the time of transit across the meridian $( h = 0 )$ ) we get LAST $= \alpha .$ An accuracy of 0.01 to $0 . 0 2 \ s$ is obtained from approximately 30 transits.

The accuracy of the determination of longitude primarily depends on the systematic errors of the observer, the instrument, and the time comparison. If the determinations are made by the same observer, using the same instrument and the same time signal transmitting station as well as the same stars, then longitude differences are essentially free from these errors. Longitude determinations of high accuracy have thus been carried out as measurements of differences with respect to a reference station.

An economical method to determine the latitude and longitude simultaneously is known as the method of position lines.

The zenith angles $Z _ { 1 } , Z _ { 2 }$ of two stars $S _ { 1 } ( \alpha _ { 1 } , \delta _ { 1 } ) ,$ , $S _ { 2 } \big ( \alpha _ { _ 2 ^ { \prime } } \delta _ { 2 } \big )$ are observed at sidereal times $\mathsf { L A S T } _ { \tau ^ { \prime } }$ $\mathsf { L A S T } _ { 2 }$ and at azimuths $A _ { \underline { { { \scriptscriptstyle 1 } } } } , A _ { \underline { { { \scriptscriptstyle 2 } } } }$ . If $S _ { \ l _ { 1 } \prime }$ $S _ { _ 2 }$ are projected on the Earth’s surface, then the intersections of the circles centered at the projections $S _ { \mathbf { \Omega } _ { 1 } } ^ { \prime } , \ S _ { \mathbf { \Omega } _ { 2 } } ^ { \prime }$ having radii $Z _ { 1 } , ~ Z _ { 2 }$ represent two geometric positions $P$ and $( P )$ for the point of observation (Fig. 5.42). Near $P ,$ the circles can be replaced by their tangent lines (position lines), while the point $( P )$ can be excluded from the solution if approximate coordinates are known. The intersection of the position lines then yields an approximation to $P .$ .

![](images/50f0574288964ac7f6cf951499d40995a048b46c68b770dcfaba8be7c7621e27.jpg)  
Fig. 5.42: Method of position lines.

Computationally, one obtains the corrections $\Delta \Phi = \Phi - \Phi _ { _ { 0 } }$ and $\Delta \Lambda = \Lambda - \Lambda _ { _ 0 }$ upon introducing an approximate position $P _ { 0 } ( \Phi _ { 0 ^ { \prime } } \mid \Lambda _ { 0 ^ { \prime } } )$ . When observations are made with the prism astrolabe, cf. [5.3.1], the zenith angle predetermined by the prism is treated as an additional unknown. One obtains accuracies of a few $0 . 1 ^ { \prime \prime }$ from about 20 stars evenly distributed above the horizon.

As explained in [5.3.1], a transportable zenith camera also permits the rapid and accurate simultaneous determination of latitude and longitude. From the coordinates $\alpha _ { _ Z ^ { \prime } } \delta _ { _ Z }$ of the zenith, derived from the observations, we obtain

$$
\Phi = \delta _ { _ { z ^ { \prime } } } \Lambda = \alpha _ { _ z } - \mathrm { { C A S T } , }
$$

see also Figs. 2.2, 2.4. Repeated observations with a digital camera system deliver an accuracy of better than $0 . 1 ^ { \prime \prime } ,$ with further improvements at longer observation times.

If the latitude is known, then the azimuth $A$ can be obtained, according to (2.20), from the hour angle $h$ derived from the sidereal time and the rectascension (5.57):

$$
\tan A = { \frac { \sin h } { \sin \Phi \cos h - \cos \Phi \tan \delta } } .
$$

Differentiation of (2.20) yields

$$
d A = { \frac { \cos q \cos \delta } { \sin z } } d h + \cot z \sin A \ d \Phi ,
$$

where $q$ is the parallactic angle, cf. [2.5]. An error in $h$ has a minimum effect for $\delta \approx 9 0 ^ { \circ }$ (stars near the pole). For some 10 observations, we get an accuracy of $0 . 3 { ^ { \prime \prime } }$ to $0 . 5 ^ { \prime \prime } .$ The azimuth of a terrestrial station is obtained by additionally measuring the angle between the directions to the star and the target on the Earth’s surface.

# 5.3.3 Reductions

In order to refer the “observed” positions (epoch $t )$ of fi xed stars to the system of the star catalogue (mean positions at the reference epoch $t _ { \mathrm { 0 } } ^ { \mathrm { ~ } }$ , several reductions have to be applied on the observed (topocentric) directions:

• Astronomic refraction causes an apparent increase in the star’s altitude (Fig. 5.43). The true zenith angle $Z$ is obtained from the observed quantity $z ^ { \prime }$ by adding the astronomic refraction angle $\Delta z _ { \infty }$ :

$$
Z = Z ^ { \prime } + \Delta z _ { \infty } .
$$

![](images/1369634c921b742323c4376f623a23a7632129b364314b44cd0920ce1e85cbfb.jpg)  
Fig. 5.43: Astronomic and satellite refraction.

According to (5.10) and (5.11), the refraction angle depends on the vertical gradient of the refractive index along the path of the ray. For a standard atmosphere (temperature $2 8 8 . 1 5 ~ \mathsf { K } ,$ atmospheric pressure $1 0 1 3 . 2 5 ~ \mathsf { h P a } )$ , we obtain from Snell’s law, and with a layered standard atmosphere for $z ^ { \prime } < 7 0 ^ { \circ }$ :

$$
\Delta z _ { 0 } = 5 7 . 0 8 ^ { \prime \prime } \tan z ^ { \prime } - 0 . 0 6 7 ^ { \prime \prime } \tan ^ { 3 } z ^ { \prime } .
$$

For actual conditions (temperature $T ,$ pressure $p )$ , we have the transformation

$$
\Delta { Z _ { \infty } } = \Delta { Z _ { 0 } } \frac { p } { 1 0 1 3 } \frac { 2 8 8 } { T } ,
$$

(Kovalevsky, 2002). The uncertainty of $\Delta Z _ { \infty }$ varies between a few $0 . 0 1 ^ { \prime \prime }$ and a few $0 . 1 { ^ { \prime \prime } }$ and depends strongly on systematic deviations from the atmospheric model (turbulences, slope of the atmospheric layers).

The diurnal aberration is an apparent displacement in direction resulting from the fi nite velocity of light and the relative velocity of the observer with respect to the stars, due to the Earth’s rotation. The corresponding latitude dependent reduction reaches a maximum of $0 . 3 { ^ { \prime \prime } }$ at the equator. The geocentric (or diurnal) parallax represents the difference between the topocentric and the geocentric direction; it can be neglected for star observations.

Through these reductions, the “observed” position is transformed to the “apparent” position (apparent place) at epoch t. The reduction of the star coordinates from the “mean” position (epoch $t _ { 0 } ^ { \phantom { + } }$ to the apparent position (epoch $t )$ involves the following steps:

Applying precession and proper motion (generally ${ < } 0 . 1 { ^ { \prime \prime } } ,$ /year, maximum $1 0 ^ { \prime \prime } / $ year) for the time interval $t - t _ { \mathrm { o } }$ transforms the mean position $( t _ { 0 } )$ to the mean position at epoch $t ,$ cf. [2.3.2], [2.4.3]. Accounting for nutation transforms the mean position $t )$ to the true position $( t )$ . The origin of the system is still at the barycenter of the solar system.

According to the IAU2000 precession-nutation model, these two effects have been combined, but the separate treatment may continue for a certain time. The combined reduction now leads to the Intermediate Reference System, cf. [2.4.3], and the difference between “mean” and “true” coordinates disappears.

The transition to the (geocentric) apparent position ( $t )$ is performed by applying the following reductions:

• Annual aberration, resulting from the revolution of the Earth about the sun. It may reach values up to $2 0 ^ { \prime \prime }$ , and is calculated from the ephemerides of the sun and the Earth.   
. Annual parallax, arising from the difference between the heliocentric and the geocentric directions. Its maximum value as obtained for a close star remains less than $0 . 8 ^ { \prime \prime }$ .   
The relativistic light defl ection remains small and can be easily taken into account. For light rays passing the edge of the sun, it reaches the extreme value of $1 . 7 5 ^ { \prime \prime }$ .

Instead of reducing from the mean position $( t _ { 0 } )$ to the apparent position (t), the apparent places of fundamental stars for a particular year can be used. They can be drawn from astronomic almanacs, as the “Apparent Places of Fundamental Stars”, Astronomisches Recheninstitut Heidelberg.

Finally, we must consider that the results (astronomic latitude, longitude and azimuth) refer to the instantaneous spin-axis of the Earth. They are transformed into the IERS reference pole by applying reductions for polar motion, cf. [2.4.2]. Multiplying the polar motion rotation matrix (2.16b) with the unit vector of the local vertical (2.18) gives the corresponding polar motion reductions (Mueller, 1969, p. 86 ff ):

$$
\begin{array} { r l } & { \Delta \Phi _ { _ P } = \Phi _ { _ { \mathrm { I T R S } } } - \Phi = - \big ( x _ { _ p } \cos \Lambda - y _ { _ p } \sin \Lambda \big ) } \\ & { \Delta \Lambda _ { _ P } = \Lambda _ { _ { \mathrm { I T R S } } } - \Lambda = - \big ( x _ { _ p } \sin \Lambda + y _ { _ p } \cos \Lambda \big ) \tan \Phi , } \\ & { \Delta A _ { _ P } = A _ { _ { \mathrm { I T R S } } } - A = - \big ( x _ { _ p } \sin \Lambda + y _ { _ p } \cos \Lambda \big ) \sec \Phi } \end{array}
$$

where $x _ { p ^ { \prime } } y _ { p }$ are the pole coordinates with respect to ITRS.

# 5.3.4 Very Long Baseline Interferometry

Extragalactic radio sources (quasars: quasi-stellar radio sources, radio galaxies) emit waves in the cm to dm range, which can be detected by large antennas (radio telescopes) used in radio astronomy. The approximate angular resolution of such a telescope is given by the wavelength/diameter ratio, and thus it is limited to a few arcmin for telescope diameters less than $^ { 1 0 0 \mathrm { m } }$ . By employing a receiving system of two widely (a few 1000 to $1 0 \ 0 0 0 \ \mathrm { k m } ,$ ) separated radio telescopes (baseline), the resolution can be increased to $0 . 0 0 1 ^ { \prime \prime }$ and better: Very Long Baseline Interferometry VLBI (Moritz and Mueller, 1987, p. 381 ff.; Seeber, 2003, p. 485 ff.).

The wave train from an extragalactic radio source arrives at the telescope $P _ { _ 2 }$ with a phase difference $\Phi$ with respect to the telescope $P _ { \mathrm { \uparrow } }$ . $\Phi$ is related to the time delay $\tau _ { r }$ the time the wave requires to travel the path difference $c \tau ( c$ velocity of light in vacuum),

Fig. 5.44. Due to the Earth’s rotation, $\Phi$ and $\tau$ depend on time $t .$ The following relation is valid:

$$
\Phi ( t ) = 2 \pi \frac { c } { \lambda } \tau ( t ) = 2 \pi \nu \tau ( t ) ,
$$

where $\lambda$ and $\nu$ are the respective wavelength and the frequency of the received radio wave. We introduce the baseline vector

$$
\mathbf { b } _ { _ { \mathrm { I T R S } } } = \mathbf { r } _ { _ 2 } - \mathbf { r } _ { 1 } = \left[ Y _ { _ 2 } - Y _ { 1 } \right] ,
$$

described in the terrestrial geocentric system ITRS (2.13) and the unit vector to the quasar:

$$
\begin{array} { r } { \mathbf { S } _ { \mathrm { _ { l C R S } } } = \left[ \begin{array} { c } { \cos \alpha \cos \delta } \\ { \sin \alpha \cos \delta } \\ { \sin \delta } \end{array} \right] , } \end{array}
$$

given in the celestial reference system ICRS (2.10). After transformation of s to the terrestrial system, performed by means of the Earth orientation parameters according to (2.16), we obtain the time delay (see Fig. 5.44),

$$
\boldsymbol { \tau } ( t ) = - \frac { 1 } { C } \mathbf { b } \cdot \mathbf { s } ( t ) .
$$

The negative sign takes the direction of s into account, which is opposite to the direction of wave propagation. By comparing the two wave trains received at $P _ { \mathrm { \uparrow } }$ and $P _ { _ { 2 ^ { \prime } } }$ interferences are obtained. The frequency of the interference fringes (maxima and minima) changes due to the Earth’s rotation:

$$
f ( t ) = \frac { 1 } { 2 \pi } \frac { d \Phi ( t ) } { d t } .
$$

![](images/f93190797266e8ebb1e64e8d9c5f01c6ff00838514b7d0028a44b79ff7159ab7.jpg)  
Fig. 5.44: Very long baseline interferometry.

With (5.67) and (5.70), the fringe frequency can be expressed as

$$
\boldsymbol { f } ( t ) = \nu \frac { d \tau ( t ) } { d t } = - \frac { \nu } { c } \mathbf { b } \cdot \dot { \mathbf { s } } ( t ) ,
$$

$\dot { \mathbf { s } } = d \mathbf { s } / d t .$ Equations (5.70) and (5.72) represent the VLBI observation equations. The complete observation equation will be found in the IERS Conventions 2010 (Petit and Luzum, 2010, p. 159 ff.).

The VLBI observables are the time delay $\tau$ (or the phase delay, respectively) which is regarded as the primary observation quantity, and the delay rate dt /dt. They are derived by a comparison of the digital signals received at each telescope. These signals are digitized, time-tagged and recorded on magnetic tapes or hard disks, the precise time being provided by hydrogen maser frequency standards. The transportation of the data to the few correlators available worldwide is mostly done still by courier service, but electronic data transfer is rapidly supporting and replacing this costly procedure. The correlation process consists of a relative shifting of the signals until a correlation maximum is found. The correlation function then furnishes the time delay and the delay rate for the two stations involved. The observable $\tau$ represents a group delay, while $\Phi$ is a phase delay, cf. [5.1.1], which involves the problem of ambiguity resolution, cf. [5.2.5]. The fringe frequency (delay rate) observation is free of this problem but of less importance due to its lower accuracy as compared to the delay observation, and since it allows only the determination of a reduced set of parameters. A VLBI observing session usually comprises between fi ve to nine radio telescopes (Fig.5.45), which form geometrical networks between the baselines. Typically, about 50 radio sources are tracked several times over periods of $3 { \mathrm { - } } 6 { \mathrm { ~ } } { \mathrm { m i n } }$ , at the usual 24-h observation session.

Reductions are applied for the daily aberration, cf. [5.3.3], for systematic clock differences (clock synchronization), for the effects of the tropospheric refraction, cf. [5.1.2], and for relativistic effects. The effect of the ionosphere is compensated for by observing in two frequency-bands, namely $2 . 3 \ \mathrm { G H z }$ (S-band) and $8 . 4 ~ \mathrm { G H z }$ (X-band), cf. [5.1.3]. Main error sources result from timing $\pm 1$ ps) and frequency instabilities ( $\pm 1 0 ^ { - 1 5 }$ over a few days) as well as from tropospheric models (MacMillan and Ma, 1997). The determination of the “wet” component plays a major part in this aspect. Attempts have been made to measure the water vapor content along the signal path by water vapor radiometers in order to estimate the wet component with cm-accuracy, cf. [5.1.2]. The vertical baseline component is mainly affected by the uncertainty of the wet component, and by atmospheric pressure loading. Special care is required with respect to the defi - nition of the telescope’s reference point, its connection to a ground marker, and the control of the antenna’s thermal deformation (Nothnagel, 2008).

![](images/22b52f97f9e30c67b867c8fc87ffc0ea52aa41b34f25359a41d986630968bb19.jpg)  
Fig. 5.45: $2 0 \mathsf { m }$ -radio telescope, Geodetic Observatory Wettzell, courtesy Bundesamt für Kartographie und Geodäsie (BKG), Frankfurt a.M., Germany (http://www.fs.wettzell.de).

Among the parameters to be estimated from (5.70) and (5.72) are the components of the baseline vector in the terrestrial reference system (few mm-precision at a $2 4 { \mathrm { ~ h ~ } }$ session). Global solutions for a given epoch deliver a corresponding accuracy for the station coordinates, and a mm/year and better accuracy for station velocities; they also contribute to the determination of the scale of the terrestrial system. Another VLBI product are the Earth orientation parameters, entering through the transformation between the terrestrial and the celestial system, cf. [2.4.3]. From a $2 4 ~ \mathrm { h }$ -session, the pole coordinates and Universal Time UT1 can be determined with an accuracy of better than 30 to $1 0 0 \mu \mathrm { a s }$ and 5 to $1 0 \mu \mathrm { s } ,$ , respectively; corrections to the precession and nutation models can be derived with comparable accuracy (Vennebusch et al., 2007). Solutions derived from a few hours observation time are less accurate by a factor of two or three.

VLBI for geodetic and astrometric purposes started in the 1970s (Shapiro, 1978; Campbell and Witte, 1978). Today, about 40 radio telescopes (some of mobile type) with antenna diameters from $3 \textrm { m }$ to $1 0 0 ~ \mathrm { m } ,$ ) cooperate within the framework of the International VLBI Service for Geodesy and Astrometry (IVS), and six correlators are available for processing the raw VLBI data (Schlüter and Behrend, 2007), Fig. 5.46. This network provides the celestial reference frame ICRF, and contributes to the maintenance of the terrestrial reference frame ITRF, including the determination of the Earth orientation parameters, cf. [2.4.1] to [2.4.3]. The stations are mainly located in North America, Europe, and Japan, but the global coverage has been strengthened in the last time (Fig. 5.46). As an example, the U.S. Very Long Baseline Array VLBA (National Radio Astronomy Observatory/National Science Foundation) consists of ten $2 5 \ \mathsf { m }$ -antennas spread over the US territory, and is operating since 1994. The results obtained include seasonal signals at the mm-order and a number of co-seismic deformations, occurring at tectonic plate boundaries (Petrov et al., 2009).

Mobile radio telescopes have been developed for rapid surveying of regions with recent crustal movements, such as California or the Eastern Mediterranean, and to fi ll gaps of the terrestrial reference frame in the southern hemisphere. We mention the antenna, incorporated in the Transportable Integrated Geodetic Observatory (TIGO), Fig 5.47, operating since 2002 within a German-Chilenean cooperation project at Conception/Chile (Nothnagel et al., 2004). Future VLBI development is directed towards increased accuracy $1 \textrm { m m }$ for baselines and $0 . 1 \mathrm { \ m m }$ /year for station velocities) and more continuous measurements, with near real-time solutions for the Earth orientation parameters (Behrend et al., 2009). One strategy in this direction is the installation of a “twin”-telescope, e.g., at the Geodetic Observatory Wettzell, consisting of two identical telescopes ( $1 3 \mathrm { m }$ diameter) with improved optics and fast moving capability (Hase et al., 2008).

![](images/514f647b8196e0e045c419f567c792b5c20716e5f0484294dd491368dac3f7da.jpg)  
Fig. 5.46: Radio telescopes participating in the International VLBI Service for Geodesy and Astrometry IVS (status 2010), http://ivscc.gsfc.nasa.gov.

![](images/4409b5b6f18d460687e5023e96ba37fdc10cac9bf860839246d9971b3da020d5.jpg)  
Fig. 5.47: 6m-radio telescope as part of the Transportable Integrated Geodetic Observatory (TIGO), courtesy Bundesamt für Kartographie und Geodäsie (BKG), Frankfurt a.M., Germany (http://www.fs.wettzell.de).

# 5.4 Gravimetry

Gravimetry deals with the measurement of the gravity intensity (gravity) and the gravity gradient by terrestrial methods on or close to the Earth’s surface (Marson and Faller, 1986; Torge, 1989; Timmen, 2010). “Absolute” gravity measurements refer directly to the standards of length and time [5.4.1], while modern “relative” measurements use a counterforce for the determination of gravity differences [5.4.2]. A conventional gravity reference system is needed in order to provide a global standard of high metrological quality, serving as a basis for global, regional and local gravity measurements [5.4.3]. Gravity measurements on moving platforms permit the economic survey of areas diffi cult to access [5.4.4]. Local gravity-fi eld information can be obtained by the measurement of the gravity gradient [5.4.5]. The continuous record of gravity provides temporal gravity variations at different time scales, especially the effects of solid Earth tides [5.4.6].

The unit of gravity in the SI-system is $\mathsf { m } \mathsf { s } ^ { - 2 }$ . The units $\mathrm { m } \mathrm { G a l } = 1 0 ^ { - 5 } \mathrm { m } \mathrm { s } ^ { - 2 }$ and $\mu { \sf G a l } =$ $1 0 ^ { - 8 } \mathrm { m s ^ { - 2 } } = 1 0 \mathrm { n m s ^ { - 2 } }$ are still in widespread use in geodesy and geophysics. They are derived from the unit $G a I$ (after Galilei) of the former cgs-system and serve for a simple description of gravity fi eld differences resp. measurement accuracy. The unit of the gravity gradient components is $\mathsf { S } ^ { - 2 }$ . In view of the magnitude of the components and the obtainable accuracy, the components are generally expressed in ${ 1 0 } ^ { - 9 ^ { * } } { \mathsf { s } } ^ { - 2 } = { \mathsf { n } } { \mathsf { s } } ^ { - 2 } .$ , traditionally called Eötvös unit (E).

# 5.4.1 Absolute gravity measurements

An “absolute” gravity measurement determines the gravity $g$ from the fundamental acceleration quantities length and time. We distinguish between the pendulum and the free-fall method, both going back to Galileo Galilei (1564 –1642), see Faller and Marson (1988), Niebauer (2009).

The pendulum method is no longer applied today but governed gravimetry for about 300 years. Because of its fundamental importance, and because more recent results are still part of some gravity networks, a short introduction is given here.

The pendulum method is based on the measurement of the period and the length of a freely swinging pendulum. For a mathematical pendulum (point mass $m$ suspended on a weightless wire of length $\ I )$ we have the equation of oscillation

$$
m { \cal { I } } \ddot { \varphi } + m g \sin \varphi = 0 ,
$$

with the phase angle $\varphi = \varphi ( t ) ,$ and the angular acceleration $\varphi = \ d ^ { 2 } \varphi / d t ^ { 2 }$ (Fig. 5.48). Integration over a full period leads to an elliptical integral. After expansion into a series, we obtain the period $T$ of oscillation

$$
T = 2 \pi \sqrt { \frac { I } { g } } \left( 1 + \frac { \varphi _ { 0 } ^ { 2 } } { 1 6 } + \ldots \right) ,
$$

where the amplitude $\varphi _ { \mathrm { 0 } }$ is kept small. Thus, gravity is derived from the measurement of $T$ and $I .$

The mathematical pendulum is diffi cult to realize. But equations (5.73) and (5.74 also hold for a physical pendulum if $I$ is replaced by the reduced pendulum length

$$
I _ { _ { r } } = { \frac { J } { m a } } .
$$

![](images/1991ffbb336735d18e87e93a02574291c248fa8ffa2694d0b6541638dbe4ae92.jpg)  
Fig. 5.48: Absolute pendulum method: a) mathematical pendulum, b) reversible pendulum.

Here, $J$ is the moment of inertia with respect to the axis of rotation $O _ { \prime }$ $m$ the total mass, and a the distance between $O$ and the center of mass $S .$ The reversible pendulum is characterized by two axes of rotation, for which, after a corresponding adjustment, the same oscillation time is achieved. The distance between the two axes is then equal to the reduced pendulum length, thus avoiding the direct determination of $J , m ,$ and a (Fig. 5.48).

Early pendulum measurements using mathematical pendulums were carried out at the classical arc measurements of the eighteenth century, and also with respect to the introduction of a “natural” unit for length (Borda and Cassini in Paris, 1792; Bessel in Berlin, 1835), cf. [1.3.2]. The reversible pendulum was introduced by Henry Kater (1818), and a limited number of observations were carried out, primarily after the 1860s (transportable devices by Repsold, Brunner, and others). After the fundamental gravity determination in Potsdam, cf. [5.4.3], only a few more experiments were performed in the twentieth century. The accuracy achieved fi nally remained at a few $\mu \mathrm { m } \mathrm { s } ^ { - 2 }$ , which is mainly due to problems in determining the length of the swinging pendulum, and keeping the pendulum length constant over an observation set comprising a large number of oscillations (Schüler et al., 1971).

The free-fall method is based on the equation of motion

$$
m \ddot { z } = m g ( z )
$$

of a freely falling body. Here $m$ is mass; $Z$ is along the local vertical axis, and $\ddot { z } = d ^ { 2 } z / d t ^ { 2 }$ (Fig. 5.49). Assuming a homogeneous gravity fi eld along the falling distance, double integration of (5.76a) yields the free-fall equation

$$
Z = Z _ { 0 } + \dot { Z } _ { 0 } t + \frac { g } { 2 } t ^ { 2 } .
$$

![](images/f0c9a8862ed5384e1253900c4278406145da239818cf00a9b93d9c24efdaafca.jpg)  
Fig. 5.49: Distance-time diagram: a) free-fall method, b) symmetrical rise and fall.

Equation (5.76b) relates the position $Z$ of the falling body at the time $t$ to gravity. The integration constants $Z _ { 0 }$ and $\dot { Z } _ { 0 }$ represent $Z$ and $\dot { z } = d z / d t$ at the starting time of the experi ment $\mathit { \Omega } \left( t = 0 \right)$ ). These quantities slightly deviate from zero, due to problems in accurately defi ning the starting position (resting position of the gravity center of the test mass at the start of the experiment) and small microseismic accelerations.

If at least three position/time pairs are measured, $Z _ { 0 }$ and $\dot { Z } _ { 0 }$ can be eliminated in (5.76b), and gravity is given by

$$
g = 2 \frac { ( Z _ { 3 } - Z _ { 1 } ) \left( t _ { 2 } - t _ { 1 } \right) - ( Z _ { 2 } - Z _ { 1 } ) \left( t _ { 3 } - t _ { 1 } \right) } { \left( t _ { 3 } - t _ { 1 } \right) \left( t _ { 2 } - t _ { 1 } \right) \left( t _ { 3 } - t _ { 2 } \right) } .
$$

For the symmetrical rise and fall, the test mass is thrown vertically upward and falls back after having reached the apex (Fig. 5.49). Now, it is suffi cient to measure time at the same two positions during rise and fall. Evaluation of (5.76a) then yields

$$
g = \frac { 8 \Delta Z } { \Delta t _ { 2 } ^ { 2 } - \Delta t _ { 1 } ^ { 2 } } ,
$$

with $\Delta z = z _ { _ 2 } - z _ { _ 1 } , \Delta t _ { _ 1 } = t _ { _ 3 } - t _ { _ 2 } , \Delta t _ { _ 2 } = t _ { _ 4 } - t _ { _ 1 }$ .

With modern technology (see below), considerably more than the necessary number of position/time pairs is measured at one site. A least-squares adjustment of (5.76b) then provides the parabolic fi tting curve, and also $Z _ { 0 }$ and $\dot { Z } _ { 0 }$ .

Present accuracy also requires that the gravity change along the falling distance has to be taken into account (non-homogeneous gravity fi eld) by introducing $\partial g / \partial z = g _ { z }$ . Equation (5.76a) then reads as

$$
m \ddot { z } = m ( g _ { 0 } + g _ { z } z ) ,
$$

with $g _ { o } = g$ at the resting position $Z = 0$ . Double integration now leads to

$$
Z = \frac { g _ { 0 } } { g _ { z } } \left( \cosh \sqrt { \mathrm { g } _ { z } } \ : t - 1 \right) ,
$$

for $Z _ { 0 } = \dot { Z } _ { 0 } = 0$ . A series development of $Z$ (up to order $t ^ { 4 }$ ) with inclusion of $Z _ { 0 } , ~ \dot { Z } _ { 0 }$ gives the observation equation (Cook, 1965)

$$
Z = Z _ { 0 } \left( 1 + \frac { 1 } { 2 } g _ { z } t ^ { 2 } \right) + \dot { Z } _ { 0 } \left( t + \frac { 1 } { 6 } g _ { z } t ^ { 3 } \right) + \frac { 1 } { 2 } g _ { 0 } \left( t ^ { 2 } + \frac { 1 } { 1 2 } g _ { z } t ^ { 4 } \right) + \ldots .
$$

The vertical gradient is generally determined independently by repeated relative gravity measurements along a vertical tripod, and the adjusted fi nal gravity value is referred to a fi xed reference height (with minimum effect of vertical gradient error!), e.g., $1 . 2 ~ \mathsf { m }$ at the FG5 gravimeter (Timmen, 2003).

Accuracy demands for absolute gravimetry are at the order of ${ { 1 0 } ^ { - 9 } } \mathrm { ~ g ~ }$ or $1 0 ^ { - 8 } ~ \mathrm { m } \mathrm { s } ^ { - 2 }$ . Hence, according to (5.76b), for a falling distance of $0 . 2 ~ \mathsf { m }$ (falling time $0 . 2 s \mathrm { ) }$ , accuracies of $0 . 2 \ \mathrm { n m }$ and 0.1 ns are required for position and time, respectively. This is achieved by interferometric distance measurements and simultaneous electronic timing.

For recent free-fall gravimeters, a polarization or iodine stabilized He-Ne gas laser $( \lambda = 6 3 3 ~ \mathrm { { n m } }$ ) serves as the length standard and an atomic (rubidium) frequency normal as the time standard. A Michelson interferometer is used for the distance measurement, with two corner-cube refl ectors as the main components (Fig. 5.50). One of the refl ectors is fi xed and serves as a reference; the other one represents the falling body (test mass). By splitting the laser light into a measurement and a reference beam, and superimposing them again after parallel refl ection, light interferences occur. The zero crossings of this fringe signal have a distance of $\lambda / 2$ , and the fringe frequency increases with time due to the velocity increase of the test mass according to $\dot { Z } ( t ) = g t$ (Fig. 5.51). The zero crossings are sensed by a photodiode, converted to an electronic signal, amplifi ed, triggered, and counted. A time measurement (atomic clock and time interval counter) is carried out after a preset number $n$ of zero crossings, which corresponds to a falling distance of

![](images/d42a80d7602d22613846216a1a7ecced0d8cca5b18332a4b31a96548d8846b92.jpg)  
Fig. 5.50: Michelson interferometer principle.

$$
\Delta z = n { \frac { \lambda } { 2 } } .
$$

![](images/60fb5bc07da4a651ef4425f131a7e43edc042339c0c120288137b1374390ae97.jpg)  
Fig. 5.51: Timing of scaled fringe pulses, after Zumberge et al. (1982).

The experiments are performed in vacuum $\left( 1 0 ^ { - 4 } \mathrm { P a } \right)$ in order to eliminate air resistance. Microseismicity is to a large part absorbed by long-period ( $T > 1 0 \ s )$ compensation devices. A further reduction is achieved by randomization, performing a large number (several 100 to a few 1000) of drops per station. For the rise and fall method, systematic errors that are proportional to the falling body’s velocity (residual air drag, timing errors) cancel to a large degree according to (5.78). On the other hand, the rise and fall method is handicapped by the problems which arise at the realization of a perfect vertical trajectory.

Several reductions have to be applied to the observed gravity values. The gravimetric tides being caused by the Earth’s body and ocean tides, can be reduced with an accuracy of a few $0 . 0 1 ~ { \mu \mathrm { m s } } ^ { - 2 }$ or better in most parts of the world, cf. [8.3.6]. The polar motion reduction (“gravity pole tide”), according to (3.109) and (5.66), is given by

$$
\delta g _ { \mathrm { p o l e } } = - \delta _ { \mathrm { p o l e } } \omega ^ { 2 } R \sin { 2 \varphi } ( x _ { p } \cos { \lambda } - \gamma _ { p } \sin { \lambda } ) ,
$$

where $\omega$ is the rotational velocity of the Earth, $R$ the Earth’s radius, and $X _ { p }$ and $\gamma _ { p }$ the coordinates of the instantaneous pole with respect to the IERS reference pole. The geodetic coordinates $\varphi , \lambda$ suffi ciently approximate astronomic latitude and longitude. The factor $\varphi _ { \mathrm { p o l e } } = 1 . 1 6$ accounts for the Earth’s elasticity, cf. [5.4.6].

The direct (gravitation) and indirect (deformation) effect of air pressure variations is taken into account by a reduction

$$
\delta g _ { \mathrm { p } } = 3 ( p - p _ { n } ) \mathsf { n m s } ^ { - 2 } ,
$$

with $p$ being the actual air pressure, and $p _ { n }$ the normal air pressure as given by a standard atmosphere, cf. [5.1.1], both in hPa (Niebauer, 1988). Current weather conditions may cause larger deviations from the global regression factor used in (5.81b). Improvements are possible by means of local/global weather data and deformation models (Gitlein and Timmen, 2007), cf. [8.3.1]. Finally, the fi nite velocity of light $C$ must be taken into account by adding the term $z / c$ to the observed time values. The reduction of the adjusted gravity value from the reference height to the ground mark is performed by relative gravity measurements, with an accuracy of 0.01 to $0 . 0 2 ~ \mu \mathrm { m } \mathrm { s } ^ { - 2 } ,$ , cf. [5.4.5].

The long-term stability of the length and time standards is controlled by calibration of the laser ( $1 0 ^ { - 9 }$ to $1 0 ^ { - 1 0 }$ frequency stability) and the atomic clock $( 1 0 ^ { - 1 0 } )$ . The repeatability of the gravimeter system (hard- and software) can be checked by regular measurements at a reference station, (Fig. 5.52), the data may be systematically biased by environmental effects (Fig. 5.53). The accuracy of the absolute gravimeter results, on the other hand, can be estimated only by comparisons with other instruments, with possibly different design and evaluation procedure, cf. [5.4.3].

![](images/751cf8d9570bbd81a505302b984d60818936578067d2beb06f479a86ef6b0de0.jpg)  
Fig. 5.52: Long-term stability control of JILAG-3 and FG5-220 absolute gravimeters at station Clausthal, Germany (hard bedrock). An instrumental offset of $- 0 . 0 9 \ \mu \mathrm { m s } ^ { - 2 }$ was applied to the JILAG-3 results, after Timmen (2010).

![](images/43e22ab82f72d325c3a4b04d3551b3dbb756e1575af74d5a37f6f1417c1b50db.jpg)  
Fig. 5.53: Long-term repeatability of JILAG-3 (offset corrected) and FG5-220 absolute gravimeters at station Hannover/Germany (glacial sediments close to a river-bed), after Timmen (2010).

The accuracy of absolute gravity measurements strongly depends on site conditions. Stable sites (hard bedrock, low man-made noise) provide better results than locations in sediments, close to the coast, or in urban environment. The drop-to-drop scatter (0.05 to a few $\mu \mathrm { m } \mathsf { s } ^ { - 2 } )$ is reduced by a large number of measurements. The adjusted station gravity-value (generally several 1000 drops distributed over 1 to 3 days) is derived with a standard deviation of 0.01 to $0 . 0 3 \mu \mathrm { m } \mathrm { s } ^ { - 2 }$ . The accuracy is at the order of a few $0 . 0 1 \mu \mathrm { m s } ^ { - 2 } ,$ due to unmodeled instrumental effects (e.g., fl oor recoil, electronic phase shift, laser instabilities) or environmental “noise” (atmospheric loading, groundwater table variations etc.). Systematic discrepancies (“offsets”) between different instruments may reach $0 . 0 5 \mu \mathrm { m } \mathrm { s } ^ { - 2 }$ and more, cf. [5.4.3].

The free-fall method was developed in the 1950s (Volet and Sakuma at the BIPM Sèvres, Cook at the National Physical Laboratory, Teddington). A fi rst transportable instrument was designed by Faller in 1968 and employed at the establishment of a wordwide gravity net, cf. [5.4.3], it was followed by a small series of operational JILA (Joint Institute for Laboratory Astrophysics, Boulder, CO, U.S.A.) gravimeters (Faller et al., 1983). A commercial absolute gravimeter version is available now with the FG5 (Micro-g LaCoste, Inc., U.S.A.) free-fall instrument (Niebauer et al., 1995). With these instruments, around 200 (JILA gravimeter) respectively 700 (FG5 gravimeter) position/time data pairs are collected over one drop, which are evenly distributed in distance over the drop length of $2 0 \ \mathrm { c m } ,$ , and adjusted on-line to a fi tting parabola. The time interval between two drops is between 10 and $3 0 \ s ,$ which includes the reset of the falling corner-cube and the online adjustment. The falling object moves in a co-accelerated “drag-free” chamber. The chamber eliminates residual air drag and serves, by adequate acceleration, for dropping and catching the corner-cube as well as for transporting it back to the initial position. The reference corner-cube is isolated from ground motions by a “super-spring”, which by a feed-back system electronically generates effective free-oscillation periods between 30 and $6 0 ~ \mathsf { s }$ . While the JILA gravimeters have a horizontal interferometer basis, the FG5 instruments employ the Mach-Zender interfero meter arrangement. Here, the falling and fi xed corner-cube are arranged in the vertical, with corresponding laser beam splitting (Figs. 5.54, 5.55). The vertical basis strongly reduces the infl uence of fl oor recoil and tilt on the optical path length. The iodine-stabilized laser is separated from the instrumental vibrations induced by dropping, by routing the laser light through a fi bre optic cable to the interferometer base. The instruments are disassembled for transportation (FG5: $2 4 0 \mathrm { k g }$ in eight containers). Setting up at a station requires about $2 \ \mathrm { h } ,$ , and observations (e.g., 1500-3000 computer-controlled drops, subdivided into sets of 50 drops each) are generally carried out over 1 to 3 days, depending on local noise (Torge et al., 1987; Timmen, 2010). A portable modifi cation (drop length $0 . 1 5 { \mathrm { m } } )$ ) of the FG5 gravimeter (A-10 absolute gravimeter) can be used in outdoor environment on quiet sites. It allows a sampling rate of $1 \ H z ,$ and provides a precision of $0 . 1 ~ \mu \mathrm { m s } ^ { - 2 }$ after $1 0 \ \mathrm { m i n }$ of operation (Liard and Gagnon, 2002), Fig. 5.56. Other absolute gravimeter developments (e.g., in Russia, Japan, China) also date back to the 1970s, and partly also operated worldwide (e.g., the gravimeter of the Institute of Automation and Electrometry, Siberian Branch, Russian Academy of Sciences).

![](images/9bfb4e6e3e4b7af924a44887c0abb44e6e7e06fe03897d061409a04af916dead.jpg)  
Fig. 5.54: Free-fall gravimeter FG5 principle, courtesy Micro- $\mathrm { g - A } ,$ Division of LRS, Lafayette, CO, U.S.A.

![](images/d589eaa449f6557b5123b2ac6514de3adbad5c6fabef3d0fc9f9dfa015f175ec.jpg)  
Fig. 5.55: Free-fall gravimeter FG5 view, courtesy Micro-g Lacoste – A Division of LRS, Lafayette, CO, U.S.A.

Based on the research work of Sakuma at BIPM, transportable rise-and-fall instruments have been developed at the Istituto Nazionale di Ricerca Metrologica (formerly Istituto di Metrologia “G.Colonnetti” IMGC), Torino, Italy (Alasia et al., 1982) and by Jaeger S.A., France (Sakuma, 1983). The recent IMGC-02 construction is highly operational and applied, among others, for the investigation of active volcanoes. The rise-and-fall range amounts to $2 0 ~ \mathrm { c m }$ , and the reference refl ector is fi xed to a 20 s-seismometer. With a launch carried out every $3 0 \ s ,$ the result of a 12 h-observation session is better than $0 . 1 \ \mu \mathrm { m } s ^ { - 2 }$ (D’Agostino et al., 2008).

Cold atom gravimeters represent a promising alternative to the corner cube free fall instruments (Kasevich and Chu, 1992). At this method, a source of cooled atoms is introduced into a free-fall chamber, and the free-fall acceleration of the atoms is measured by atomic interferometry. There are no moving parts which can wear off, and measurements can be performed with a high repetition rate (e.g., $3 H z$ ). A transportable device developed at LNE-SYRTE, Paris, already provides an accuracy of a few $0 . 0 1 ~ \mu \mathrm { m } s ^ { - 2 }$ from a 1-night observation series (Merlet et al., 2010).

![](images/a370469b236f236db01e5e705c4bda62a1b2db48f25a31de2048535103953892.jpg)  
Fig. 5.56: Portable absolute gravimeter A-10, courtesy Micro-g LaCoste – A Division of LRS, Lafayette, CO, U.S.A.

![](images/e5827b01f9363b7c4d6494541181c4b25977d38857735465e1d7d214bb919d19.jpg)  
Fig. 5.57: Rise and fall transportable absolute gravimeter IMGC-02 principle, modifi ed after $\mathsf { D ^ { \prime } }$ Agostino et al. (2008).

# 5.4.2 Relative gravity measurements

“Relative” gravity measurements yield the gravity differences between different stations or – if carried out in the stationary mode – the variations of gravity with time, cf. [5.4.6]. Either time or length is measured, keeping the other quantity fi xed. As a consequence, relative measurements can be performed more easily than absolute ones.

For the pendulum method, the oscillation periods $T _ { \tau }$ and $T _ { _ 2 }$ of the same pendulum are measured at two stations $P _ { \mathrm { \uparrow } }$ and $P _ { _ 2 }$ . From (5.74) we obtain

$$
\frac { g _ { 2 } } { g _ { 1 } } = \frac { T _ { 1 } ^ { 2 } } { T _ { 2 } ^ { 2 } }
$$

or, after simple transformation, the gravity difference

$$
\Delta g _ { 1 , 2 } = g _ { 2 } - g _ { 1 } = - 2 g _ { 1 } \frac { T _ { 2 } - T _ { 1 } } { T _ { 2 } } + g _ { 1 } \frac { ( T _ { 2 } - T _ { 1 } ) ^ { 2 } } { T _ { 2 } ^ { 2 } } .
$$

“Relative” pendulum measurements were carried out already at the fi rst modern arc measurements (Bouguer, Maupertuis and others) and at the marine expeditions of the early nineteenth century (Sabine, Biot and others). At these surveys, the “mathematical” and the Kater reversible pendulum were used in the relative mode, in order to derive the gravity differences to “reference” stations as the Paris or Greenwich Observatory, cf. [5.4.1]. The method was employed extensively since R.v. Sterneck (1887) developed a transportable device (pendulum length $2 5 \ \mathrm { c m } ,$ , two pendulums swinging on the same support in opposite phase in order to eliminate fl oor recoil effects). Although the systematic effects that are independent of time and position cancel with this differential method, the accuracy could not be increased over a few $\mu \mathrm { m } s ^ { - 2 }$ due to problems in keeping the pendulum length constant during a fi eld survey. The pendulum method was superseded in the 1930s by relative measurements employing elastic spring gravimeters (see below). Nevertheless, the method was still used until the 1960s for establishing gravimeter calibration lines, exploiting the fact that pendulum results are given in the unit of acceleration and do not need to be calibrated.

Relative gravity meters use a counterforce in order to keep a test mass in equilibrium with gravity. Gravity changes in space or time are monitored by corresponding changes of the counterforce, which are transformed to the gravity unit by a calibration function. An elastic counterforce is used at most constructions, but magnetic counterforces are also employed, mainly in instruments operating on moving platforms and in the stationary mode, cf. [5.4.4], [5.4.6].

The elastic spring gravimeter is based on the principle of a spring balance. If gravity changes, the spring length will also change in order to maintain static equilibrium between gravity and the elastic force. According to Hooke’s law, the strain is proportional to the stress for small elongations. We distinguish between translational and rotational systems.

In a translational system (vertical spring balance), the condition of equilibrium is given by (Fig. 5.58a)

$$
m g - k \big ( I - I _ { \mathrm { 0 } } \big ) = 0 ,
$$

where $k$ is the spring constant and $I$ (resp. $I _ { 0 } )$ is the length of the spring with (resp. without) load. Applying (5.84) on a gravity difference $\Delta g$ furnishes a linear relationship between $\Delta g$ and the observed difference in length $\Delta { } t$

$$
\Delta g = \frac { k } { m } \Delta I = \frac { g } { I - I _ { 0 } } \Delta I .
$$

An undamped spring generates a harmonic oscillation with the proper frequency

$$
\omega _ { \scriptscriptstyle 0 } = \sqrt { \frac { k } { m } }
$$

and the oscillation time

$$
T _ { \scriptscriptstyle 0 } = 2 \pi \sqrt { \frac { m } { k } } = 2 \pi \sqrt { \frac { I - I _ { \scriptscriptstyle 0 } } { g } } .
$$

By differentiation, we obtain the mechanical sensitivity

$$
\frac { d I } { d g } { = } \frac { m } { k } { = } \frac { T _ { 0 } ^ { 2 } } { 4 \pi ^ { 2 } } .
$$

In order to assess gravity changes with a relative accuracy of ${ 1 0 } ^ { - 8 } ,$ , length changes of a $_ { 0 . 1 \textrm { m } }$ long spring would have to be determined to $1 \ \mathrm { n m }$ .

![](images/766afd4ae192a5a14e8ce10c7e9c23ac3ab082157c6d51f6061e8f899ff2359f.jpg)  
Fig. 5.58: Elastic spring gravimeter principle: a) vertical spring balance, b) lever torsion spring balance, c) general lever spring balance.

Rotational systems (lever spring balance) consist of a lever that supports a mass $m$ and rotates about an axis $O _ { \ l }$ . Equilibrium can be obtained through a horizontal torsion spring or through a vertically or obliquely acting helical spring. The equilibrium of the torques for the lever torsion spring balance (Fig. 5.58b) yields

$$
m g \cos \alpha - \tau ( \alpha _ { _ 0 } + \alpha ) = 0 ,
$$

where a is the length of the lever, $\alpha$ the angle between the horizontal and the lever, $\tau$ the torsion constant, and $\alpha _ { _ 0 }$ the pretension angle of the spring. This non-linear system becomes a linear one for $\alpha = 0$ , with

$$
\Delta g = \frac { \tau } { m a } \Delta \alpha .
$$

For the general lever spring balance, the spring counterforce acts under an arbitrary angle on the lever carrying the mass. The line connecting the rotation axis $O$ with the upper point where the spring is mounted deviates by an angle $\delta$ from the vertical (Fig. 5.58c). With the vertical distance

$$
h = \left( { \frac { b d } { I } } \right) \sin \alpha
$$

between the axis of rotation and the spring, the equilibrium condition for the torques reads

$$
m g a \sin ( \alpha + \delta ) - k b d \frac { I - I _ { 0 } } { I } \sin \alpha = 0 .
$$

The sensitivity of this non-linear system can be signifi cantly increased by approximating the torques of gravity and of the elastic spring (astatization). With a zero-length spring $( \boldsymbol { I } _ { 0 } = \boldsymbol { 0 } )$ , we have the sensitivity

$$
\frac { d \alpha } { d g } = \frac { \sin ( \alpha + \delta ) \sin \alpha } { g \sin \delta } .
$$

High sensitivity is achieved at a small angle $\delta$ and $\alpha \approx 9 0 ^ { \circ }$ . For $a = 0 . 1 \textrm { m }$ , $\alpha + \delta \stackrel { } { = } 9 0 ^ { \circ }$ , and $\delta \mathrm { = } 1 0 0 ^ { \prime \prime }$ , displacements have to be measured with a precision of $2 \mu \mathrm { m }$ in order to obtain a relative accuracy of ${ { 1 0 } ^ { - 8 } }$ . Compared to the linear system, the sensitivity is thus increased by a factor of 2000.

The required accuracies of $0 . 1 ~ \mu \mathrm { m } \mathrm { s } ^ { - 2 } ,$ or better, place high demands on the reading systems as well as on the stability of the counterforce with time.

Optical and/or electrical reading systems are used to observe the position of the test mass. A capacitive position-indicator is usually employed and is connected to a digital readout unit. The zero-method is preferred for the measurement of the displacement, with a compensation device for restoring the zero position. Mechanical compensation is performed by a measurement screw. Since the 1980s, electronic feedback systems are preferred as they are not affected by screw errors (Röder et al., 1988).

The elasticity of the spring should exhibit a time stability of ${ { 1 0 } ^ { - 8 } }$ over several hours, which is the time interval required for transporting the gravimeter between the stations of a large-scale network, cf. [7.4]. Spring materials include NiFe alloys (small thermoelastic coeffi cient) and fused quartz (large but linear thermoelastic coeffi cient, small coeffi cient of thermal expansion, less sensitivity to mechanical shocks). In addition, the measurement system has to be protected against changes in temperature (thermostat), air pressure (air-tight sealing), and magnetic fi eld (shielding of metal alloy springs). The effects of mechanical shocks and vibrations can be reduced by a damping device, in addition to air-damping.

Spring gravimeters have been developed since the 1930s for use in geophysical exploration. From the 1950s, instruments were available which could be used for establishing large-scale gravity networks (Woollard, 1950). Most of these early gravimeters had a limited measuring range (e.g., $2 0 0 0 \mu \mathrm { m } \mathrm { s } ^ { - 2 } )$ and required a reset screw for changing to another gravity range (Askania gravimeter: torsion spring balance, metal alloy; Worden gravimeter: fused quartz system with horizontal beam and vertical counter spring). The LaCoste and Romberg astatized gravimeters employ a metal alloy zero-length spring, acting at $4 5 ^ { \circ }$ inclination on the horizontal beam (model G: $7 0 0 0 0 \ \mu \mathrm { m s } ^ { - 2 }$ range, measuring screw with $\mathsf { \bar { 1 0 } ~ } \mathsf { \mu m s } ^ { - 2 }$ per one rotation), Krieg (1981), Kanngieser (1983). Recently developed instruments are microprocessor-controlled and are highly automated. They employ capacitive transducers and electronic feedback systems with worldwide range (Valliant et al., 1986). Self-leveling by electronic levels, a high data acquisition rate (e.g., 1 s-reading cycle and $3 0 ~ 5$ -sampling over $1 5 \ \mathrm { m i n } ;$ ) and on-line evaluation (automatic data compression and analysis, Earth tides reduction, drift control and correction) are further characteristics of these state-of-theart instruments. We mention the Scintrex CG-3 and CG-5 Autograph gravimeters (non-astatized linear fused-silica system with vertical spring, pick-off resolution $0 . 2 \ \mathrm { n m }$ , world-wide range, constant calibration factor and no periodic errors (Timmen and Gitlein, 2004) and the automated Burris Gravity Meter of ZLS Corporation based on the LaCoste and Romberg system, with a digital feedback range of $5 0 0 \mu \mathrm { m } \mathrm { s } ^ { - 2 }$ (Jentzsch, 2008), Figs. 5.59, 5.60.

Options of conventional land gravimeters include underwater and bore-hole instruments. After sealing in a pressure and water protected diving bell, an underwater gravimeter is lowered to the sea bottom and remotely operated from on board a survey vessel. Underwater gravimeters have been used since several decades, mainly in the shelf areas at water depths less than $2 0 0 \textrm { m }$ (Beyer et al., 1966). A remotely operated deep ocean seafl oor gravimeter has been developed recently using three gravity sensors (Scintrex CG-3M) in one watertight pressure case, with motorized gimbals for leveling and quartz pressure gauges for depth information. Repeated measurements atop seafl oor benchmarks yielded a repeatability of better than $0 . 1 \mu \mathrm { m } \mathrm { s } ^ { - 2 }$ (Sasagawa et al., 2003). A bore-hole gravimeter (Micro-g LaCoste Inc.) is characterized by small dimensions and remote-controlled operation at high temperatures. It is used for the estimation of rock densities from vertical profi les, and corresponding modelling of geological layers (LaFehr, 1983).

![](images/a6920821f060626b3445dd0feb296480c8cc027a03c73d8745674ca03f094052.jpg)  
Fig. 5.59: ZLS Burris Gravity Meter, courtesy ZLS Corporation, Austin, TX, U.S.A.

![](images/3669b3ada0f81e2744c27535e0c345cdb9ab7120569ea9327321c9dc3378695c.jpg)  
Fig. 5.60: Scintrex Autograph CG-5 Gravity Meter, courtesy Scintrex, Concord, Ontario, Canada.

Air/sea gravimeters will be described in [5.4.4], and recording (Earth tide) gravimeters in [5.4.6].

Despite all measures to protect the gravimeter’s measuring system against environmental disturbances, the zero reading changes with time: drift and tares. The drift is caused by aging of the spring material (approximating zero after some years) and short-term changes which occur during a fi eld survey. This “transportation” drift results from reactions of the spring to vibrations and small shocks, uncompensated temperature fl uctuations, and elastic effects after unclamping the lever. It depends on the spring material and on measurement conditions and can reach a few $\mu \mathrm { m } \mathrm { s } ^ { - 2 } .$ /day. Larger mechanical shocks may produce sudden tares of the same order of magnitude or more. The drift is determined by repeated station occupations during one day and subsequent modeling. Different methods have been developed depending on the instrumental behavior and the network structure; among them are the profi le, the star, and the step method (Fig. 5.61).

After reducing the gravimeter reading for the Earth tides, cf. [8.3.6], the drift function can be modeled by a low-order polynomial with time (Fig. 5.62):

$$
D ( t ) = d _ { 1 } \left( t - t _ { 0 } \right) + d _ { 2 } \left( t - t _ { 0 } \right) ^ { 2 } + . . . ,
$$

![](images/efb5224982a3d371908300d7d2822ed7917889aba20b58b972e71152826b85e6.jpg)  
Fig. 5.61: Drift determination methods: a) profi le method, b) star method, c) step method.

![](images/4c5f5adc35c57441a4b38d82829975fc5ad6187213ad265fc0577ae693f26b75.jpg)  
Fig. 5.62: Drift determination (profi le method).

with $t _ { \mathrm { _ 0 } }$ being the starting time (e.g., beginning of the survey) and $d _ { \scriptscriptstyle 1 } , \ d _ { \scriptscriptstyle 2 } , \ldots$ the drift parameters. The network adjustment delivers the drift parameters, based on repeated observations, cf. [7.4].

The gravimeter reading $Z$ (in counter units) is converted to the gravity unit by means of the calibration function:

$$
g = F ( z ) .
$$

$F ( Z )$ depends on the physical and geometrical parameters of the measuring system, see (5.85), (5.90), (5.92), which cannot be determined individually with the desired accuracy.

Therefore, the calibration function is derived by comparing reading differences with known differences of gravity. Modeling is performed by a low degree polynomial (generally only a linear “scale factor”), periodic calibration terms may be added for taking cyclic errors of a measuring skrew into account. Restricting ourselves to the linear calibration coeffi cient, the transformation from the readings to the gravity reads

$$
g _ { i } = N _ { \scriptscriptstyle 0 } + Y _ { \scriptscriptstyle 1 } z _ { i } = N _ { \scriptscriptstyle 0 } + ( 1 + Y _ { \scriptscriptstyle 1 } ) z _ { i } ,
$$

where $Y _ { \scriptscriptstyle 1 }$ is the scale factor and $\gamma _ { \scriptscriptstyle 1 }$ the (small) scale correction, $N _ { \mathrm { 0 } }$ represents the level unknown.

Laboratory and fi eld methods are available for determining the coeffi cients of the calibration function. In the laboratory, gravity changes can be simulated and compared with the corresponding gravimeter readings. The tilt-table method uses the inclination by a known angle for producing an apparent gravity variation, and the mass method uses the defi ned change of the gravimeter mass. Special methods have been developed for recording gravimeters, cf. [5.4.6]. Calibration lines provide gravity differences, determined by absolute gravimeters, and eventually densifi ed by relative gravimetry. They exploit the fact that gravity varies with latitude (horizontal calibration line) and height (vertical calibration line), Kanngieser et al. (1983), Timmen et al. (2006). The limited gravity range of these lines only allows determination of an approximate value for the linear calibration factor; an improved estimate of the linear and eventual non-linear parameters must be based on a global gravity reference system, cf. [5.4.3]

Gravity networks are generally adjusted by the method of parameter variation (Torge, 1993). Absolute gravity measurements and relative gravimeter readings are introduced as observations, and gravity values as well as (for relative gravimeters) drift and calibration coeffi cients are to be determined. The observation equation for an absolute gravity measurement on the station $i$ reads

$$
\begin{array} { r } { \bar { Z } _ { i } = g _ { i } , } \end{array}
$$

where $\overline { { Z } } _ { i }$ represents the observed mean value corrected for polar montion and Earth tides and reduced to ground level, cf. [5.4.1]. By combining (5.93) with (5.94b) we obtain the observation equation for relative gravimeter readings:

$$
Z _ { i } = g _ { i } - N _ { \mathrm { o } } - Y _ { \mathrm { } } Z _ { i } + d _ { \mathrm { } } ( t _ { i } - t _ { \mathrm { 0 } } ) .
$$

In most applications, reading differences between the stations $\boldsymbol { i }$ and $j$ are introduced as “observations”, hereby eliminating the level unknowns:

$$
\Delta z _ { i j } = z _ { j } - z _ { i } = g _ { j } - g _ { i } - Y _ { 1 } ( z _ { j } - z _ { i } ) + d _ { 1 } ( t _ { j } - t _ { i } ) .
$$

The accuracy of gravity differences $\mathit { \Delta } \Delta g < 1 0 0 0$ to $2 0 0 0 ~ \mu \mathrm { m } \mathrm { s } ^ { - 2 } )$ observed with well calibrated and drift-controlled instruments is 0.1 to $0 . 2 ~ { \mu \mathrm { m s } } ^ { - 2 }$ . Repeated measurements and the use of several instruments increase the accuracy to $0 . 0 5 ~ \mu \mathrm { m } s ^ { - 2 }$ and better, and 0.01 to $0 . 0 2 ~ { \mu \mathrm { m s } } ^ { - 2 }$ for local ties (Becker et al., 2000; Timmen, 2010).

# 5.4.3 Gravity reference systems and gravity standard

Gravity reference systems provide homogeneity of gravimetric surveys by realizing a gravity standard through the gravity values of a selected number of stations.

The need to establish a global reference system arose at the end of the nineteenth century when larger sets of absolute and relative pendulum measurements had to be combined. The Potsdam Gravity System was introduced in 1909 by IAG. It was based on reversible pendulum measurements carried out in the Geodetic Institute Potsdam by Kühnen and Furtwängler (1898–1904). Relative pendulum ties to national base stations transferred the Potsdam absolute value to other parts of the world. Since the 1930s, new absolute and relative gravity measurements revealed that the Potsdam gravity value was $1 4 0 ~ { \mu \mathrm { m s } } ^ { - 2 }$ too high and that transfer errors of several $1 0 \mu \mathrm { m } \mathsf { s } ^ { - 2 }$ had occurred.

The Potsdam Gravity System was superseded by the International Gravity Standardization Net 1971 (IGSN71), recommended by the IUGG (Morelli et al., 1974). This network contains 1854 gravity stations (among them about 500 primary stations) determined by 10 absolute and about 25 000 relative measurements, including 1 200 relative pendulum ties (Fig. 5.63).

The mean uncertainty of the adjusted gravity values is less than $1 ~ { \mu \mathrm { m s } } ^ { - 2 }$ . High relativeaccuracy is provided at gravimeter calibration lines, which extend in the north-south direction in America, Europe and Africa, and in the western Pacifi c. Meanwhile the IGSN71 has been extended to previously uncovered parts of the world. Regional networks have been connected to IGSN71, or transformed (shift and scale factor) to it, with the help of identical stations. The IGSN71 gravity values can be used to derive the linear calibration factor of relative gravimeters with a relative accuracy of some $1 0 ^ { - 5 }$ .

![](images/50d4d5b00f429fde01e7ae30e97d5a7489152b4897c164bfe619567b49908ed9.jpg)  
Fig. 5.63: International Gravity Standardization Net 1971 (IGSN71): absolute gravity stations and selected network ties, after Morelli et al. (1974).

With the increasing availability of transportable absolute gravimeters with accuracy of $0 . 0 5 ~ { \mu \mathrm { m s } } ^ { - 2 }$ and better, the gravity standard can be established independently from a global system with any gravity survey, through the length and time standards inherent in the gravity meter (Torge, 1998). The linear calibration factors of relative gravimeters then are derived from the absolute values available in the survey area. The IGSN71 consequently does not need a readjustment but rather is improved continuously by networks based on absolute gravimetry. This strategy requires a regular quality control of the absolute gravimeter systems, cf. [5.4.1]. As a consequence, international comparisons of absolute gravimeters have been carried out since the 1980s at the BIPM, Sèvres (Vitushkin et al., 2010), and since 2003 also at the European Centre of Geodynamics and Seismology in Walferdange, Luxembourg (Francis et al., 2010), see Fig. 5.64. For advanced absolute gravimeters, both the r.m.s. scatter around the reference station mean value and the long-term stability is a few $0 . 0 1 ~ \mu \mathrm { m s } ^ { - 2 } ,$ , which characterizes the present state of the realization of the gravity standard.

![](images/1e122b3ed0b4a7a06af573f58ec0244b21ffd2248c3383f810a38d78f4746e71.jpg)  
Fig. 5.64: Absolute gravimeter compaison, BIPM Sevres 2005: Deviations from mean value and standard deviations for different gravimeter types (FG5, A10, JILAG, rise and fall instruments, others), after Vitushkin et al. (2010), courtesy L. Vitushkin.

# 5.4.4 Gravity measurements on moving platforms

Kinematic methods have been developed for rapid and high-resolution gravimetric surveys in areas of having challenging environmental conditions, such as the oceans, the polar regions, high mountains, and tropical forests. Ships and airplanes are predominantly used as carriers, but helicopters and land vehicles also have been employed for local surveys. Sea gravimetry concentrates on regions of geological interest and geophysical exploration, especially at border seas and in shelf areas. Regional and local airborne surveys serve for covering areas lacking in terrestrial gravity data, and thus support high-resolution geoid calculations as well as geology, geophysics, and glaciology.

Compared to stationary gravimetry, additional diffi culties arise in kinematic gravi metry, i.e., the continuous orientation of the gravity sensor with respect to the vertical, and the separation of gravity from non-gravitational accelerations, which occur at a broad frequency range (Brozena and Peters, 1995; Schwarz, 2001).

The principle of kinematic gravimetry is based on Newton’s law of motion (e.g., Jekeli, 2001a). In an inertial system it reads as

$$
\displaystyle { \ddot { \boldsymbol { \mathsf { r } } } } = \mathbf { f } + \mathbf { g } ,
$$

where $\ddot { \mathbf { r } } = d ^ { 2 } \mathbf { r } / d t ^ { 2 }$ is the kinematic acceleration of a body, f the acceleration due to action forces (also called specifi c force, i.e., force per unit mass), and g the gravitational vector. The specifi c force is measured by accelerometers (employing a mechanical spring, an electromagnetic force or a vibrating string as a sensor), with mechanical or computational orientation provided by gyros. The kinematic acceleration has to be determined independently by geometric methods of positioning and navigation, e.g., through GNSS (Fig. 5.65).

For an accelerometer resting on the surface of the rotating Earth and aligned with the local vertical, the kinematic acceleration in (5.96a) is zero. The accelerometer now measures gravity and is designated as gravity meter, see (5.84).

Based on (5.96a), modeling of kinematic gravimetry can be done in the local ellipsoidal system orientated in the system of global ellipsoidal coordinates, cf. [4.1.3], Timmen et al. (1998), Schwarz (2001). In kinematic gravimetry, this system is called local level system (subscript $I _ { \rho }$ ), and generally defi ned as a north-east-down-system. We assume that the kinematic acceleration is given in this system (e.g., by GPS/GNSS positioning), and that the accelerometers are fi xed to the vehicle, the specifi c force is then measured in the vehicle’s body frame (subscript $b$ ). The transformation from the body frame to the local level system is carried out by the rotation matrix R containing the orientation angles between the two frames which vary with time. The gravity vector (the measurement takes place on the rotating Earth, which introduces the centrifugal acceleration!) is now expressed by:

$$
\mathbf { g } ^ { I } = \ddot { \mathbf { r } } ^ { I } - \mathbf { R } _ { b } ^ { I } \mathbf { f } ^ { b } + ( 2 \Omega _ { i e } ^ { I } + \Omega _ { e l } ^ { I } ) \times \dot { \mathbf { r } } ^ { I } ,
$$

where again r¨ is the platform kinematic acceleration and r. its velocity, $\boldsymbol { \mathsf { r } }$ is the position vector and f is the measured acceleration vector. g now represents gravity instead of gravitation as defi ned in (5.96a). As the platform moves with r. with respect to the rotating Earth, inertial accelerations arise. These accelerations are taken into account by the last term in (5.96b). $\Omega _ { _ { i e } }$ and $\Omega _ { e I }$ are the skew-symmetric matrices of angular velocities due to the Earth’s rotation rate and the vehicle’s rate, referenced

![](images/765146182f5c61a24d0984c1510aa78b204f96dfffbe15aa84d176e72505afb6.jpg)  
Fig. 5.65: Airborne gravity meter principle, modifi ed after Timmen (2010).

to the ellipsoid (Earth-fi xed frame e): Coriolis effect, see below (Jekeli, 2001a, p.   
123 ff.).

The Earth’s and the vehicle’s rotational matrices depend on latitude and longitude rates (horizontal velocities), and on the Earth’s angular velocity. Introducing the individual parameters into (5.96b) fi nally leads to a set of non-linear differential equations for position and velocity. Integration delivers the fundamental equations of inertial navigation/positioning. In kinematic gravimetry, they are solved for gravity, by introducing independently measured position and velocity. Inertial positioning, on the other hand, utilizes gravity fi eld models, and solves for position, cf. [5.5.3].

At the practical evaluation of (5.96b) the normal gravity vector f is subtracted from gravity, which introduces the gravity disturbance as the unknown parameter, in contrast to the gravity anomaly which is used traditionally at gravimetric geodesy, cf. [6.5.1].

Gravity sensors used in kinematic gravimetry are either land gravimeters (including special constructions) converted for use under dynamic conditions, or force-balanced accelerometers. They operate either on a stable platform or are (accelerometers) part of an inertial platform rigidly connected to the carrier (Glennie et al., 2000).

Operational sea and airborne gravimetry generally employs modifi ed land gravimeters mounted on a damped two-axes gyro-stabilized platform. Stabilization occurs in the local-level frame by two gyroscope/accelerometer pairs operating in a feed-back mode. At this “scalar” gravimetry, only the magnitude of gravity is determined, and (5.96b) reduces to (Jekeli, 2001a, p. 334)

$$
g = f _ { _ { z } } - { \ddot { z } } + 2 \omega \cos \varphi \sin \alpha v + \frac { v ^ { 2 } } { r } .
$$

Here, $f _ { _ Z }$ and $\ddot { Z }$ are the vertical (upward) components of the specifi c force and the platform acceleration, respectively. $\omega$ is the angular velocity of the Earth rotation, $\varphi$ the geodetic latitude, $\alpha$ the geodetic azimuth, $V$ the platform velocity with respect to the Earth, and $r$ the distance to the Earth’s center. Again, for the static case, (5.97) transforms into the equilibrium conditions of relative gravimetry, cf. [5.4.2].

The velocity dependent terms on the right-hand side of (5.97) represent the Eötvös reduction (Harlan, 1968). From Fig. 5.66, it can be identifi ed as the Coriolis acceleration, which increases (for a west-east directed course) the angular velocity of the Earth rotation, and the centrifugal acceleration arising from the platform’s angular velocity ${ v } / r$ around the center of the Earth. Close to the Earth $( r = R = 6 3 7 1 ~ \mathrm { k m } )$ ) the Eötvös reduction amounts to

![](images/a7afe7a40a5e7aafbf8456e39d40457a3cfedf04cf8200c22bf0ba5ae7c8ab14.jpg)  
Fig. 5.66: Eötvös effect.

$$
\delta g _ { \mathrm { { t o t } } } = 4 0 v \cos \varphi \sin \alpha + 0 . 0 1 2 v ^ { 2 } \mu \mathrm { { m s } ^ { - 2 } , }
$$

with $V$ in $\mathrm { k m / h }$ . The second term is small for sea gravimetry but attains large values with airborne applications. As velocities can be determined by GNSS navigation with an accuracy of $0 . 0 5 ~ \mathrm { m } / s$ and better, the uncertainty of the Eötvös reduction is now less than $1 0 \mu \mathrm { m s } ^ { - 2 }$ .

Instead of using a gravimeter on a stabilized platform, the gravity sensor can be rigidly connected to the vehicle. GNSS supported inertial navigation systems (INS) are employed with this strapdown inertial gravimetry, characterized by the use of force-rebalanced accelerometers with a high digital data rate (Jekeli, 2001a, p. 320 ff.). This vector gravimetry mode requires three orthogonally mounted accelerometers in order to determine the specifi c force vector. According to (5.96b), the orientation angles between the body-frame and the local level-frame are needed continuously, and are computed by integrating the output of the INS gyros and from GNSS multiantenna systems. One advantage of vector gravimetry would be the simultaneous determination of gravity disturbances and defl ections of the vertical, with the possibility of a direct determination of geoid profi les, cf. [6.7.4]. Due to the high demands on attitude control (gyro drift!) vector gravimetry is still in the experimental stage (Jekeli and Kwon, 1999; Kreye et al., 2006), but it offers an inexpensive and robust tool for airborne gravimetry. In the scalar mode, only one approximately vertical accelerometer is used. Demands are now less stringent, especially if the output of an accelerometer triad is used for the determination of the magnitude of gravity (rotation invariant scalar gravimetry), Wei and Schwarz (1998).

The methods for separating gravity from non-gravitational accelerations depend on the frequency of the accelerations and differ for sea and airborne gravimetry, after strong reduction of high-frequency vibrations by damping of the measuring system.

At sea gravimetry (stabilized platform), “disturbing” accelerations occur with periods between 2 and $2 0 \ s ,$ and they may reach amplitudes of $0 . 1 \ g .$ Due to low ship velocity (10 to $2 0 \ \mathrm { k m / h } ,$ ) and the nearly constant reference surface (sea level), low-pass fi ltering suffi ciently suppresses the vertical accelerations. By averaging the recorded data over time intervals of 1 to 5 minutes, mean gravity values over some 0.1 to $2 ~ \mathrm { k m }$ are thus obtained. The effect of horizontal accelerations remains small because of the stabilization. Off-leveling effects generally can be neglected at an attitude accuracy of about $1 0 ^ { \prime \prime }$ . More critical are cross-coupling effects, which occur with horizontal lever spring gravimeters between the horizontal and the vertical component of the disturbing acceleration. They may reach $5 0 ~ { \mu \mathrm { m } } { \varsigma } ^ { - 2 }$ or more and must be corrected using the horizontal acceleration records. Straight line gravimeters (vertical sensitivity axis) are free from these errors. This is also valid for vibrating string gravimeters which are based on the fact that the resonant vibrational frequency of a string under tension is proportional to the square root of $g .$ . Other advantages of this design are the large dynamic measurement range and the little shock sensitivity.

For airborne gravimetry, accelerations vary with periods from 1 to $3 0 0 s$ (long-periodic eigenmotion of the airplane), and with amplitudes up to $0 . 0 1 \ldots 1 g$ and more. Large airplane velocities (250 to $4 5 0 \mathrm { k m / h } ,$ ) prevent an effective fi ltering, and thus with a long fi lterlength (one minute to several minutes) only mean gravity values over some km to $1 0 ~ \mathrm { k m }$ and more are obtained. In addition, the attenuation of the gravity fi eld with height, cf. [3.3.3], prevents a high resolution at high fl ight altitudes of several km. These problems in principle require the employment of low-velocity and low-fl ying airborne vehicles. The vehicle’s kinematic accelerations have to be determined independently by geodetic methods, nowadays practically performed through differential GNSS (carrier phase measurements), using the second derivative of height or the fi rst derivative of velocity. As the measurement noise is amplifi ed by these time differentiation, the fi rst time derivative of velocity as obtained from Doppler shifts is preferred in this context. Over water and ice areas, radar and laser altimetry can also be employed for height determination. Heights are also needed in order to reduce the gravity data to a common reference level, by applying the free air reduction, cf. [6.5.3], this is achieved satisfactorily by GPS/GNSS heighting (Forsberg and Olesen, 2010).

Gravity observations on sea started at the beginning of the twentieth century, when O. Hecker obtained gravity data along several ocean-wide ship-tracks by exploiting the gravity correction to be applied to mercury thermometer readings, when compared with hypsometer (thermometer operating at the boiling point of water) results. In 1923, F.A.Vening-Meinesz constructed a threependulum instrument for gravity measurements in a submerged submarine; world-wide cruises followed until the 1960s. At that time, sea gravimeters (e.g., modifi ed Askania and LaCoste and Romberg land gravimeters) mounted on gyro-stabilized platforms became operational on board of surface vessels (Dehlinger, 1978), Fig. 5.67. First attempts for airborne gravimetry were also made in the 1960s, using stable platform mounted sea gravimeters on board of high fl ying aircrafts (LaCoste, 1967). Conventional sea-air gravimeters on platforms are now employed operationally on board of helicopters and airplanes. A more recent development especially for use under rough conditions consists of a rotational double quartz fi laments system embedded in a viscous fl uid (Krasnov et al., 2008).

Since the 1970s, force-balanced accelerometers, as developed for inertial navigation, became another tool for sea-air gravimetry. These instruments are small and robust with respect to strong dynamics but have less resolution and larger drift rates than conventional land gravimeters, linear and rotational systems are available (Fig. 5.68). For a linear system, the proof mass is constrained to move in only one direction and maintained at the zero position by an electromagnetic fi eld, the electrical current needed to maintain zero is proportional to the acceleration. Depending on the direction of the sensitive axis, dedicated components of the specifi c force are measured. Force-balanced accelerometers are especially suited for use under rough conditions on sea and in air; they have also been employed on board of deep sea vessels (Bell and Watts, 1986; Cochran et al., 1999).

![](images/f98e56708a3bfe3c10110f668168d1b493b88b80efa0b870d929df8262f8b6d6.jpg)  
Fig. 5.67: Gravimeter System KSS31M with Gravity sensor Gss30 and gyro-stabilized platform KT 31, Bodenseewerk Geosystem, Überlingen, Germany, courtesy Bundesanstalt für Geowissenschaften und Rohstoffe (BGR).

![](images/2ae640eabf324073e38082e2a411d3cb82abe48a1d7cd4578ce854af2823ef62.jpg)  
Fig. 5.68: Force-balanced accelerometer principle: translational (suspended mass) system (left) and rotational (pendulum) system (right).

Sea and airborne gravimetric surveys generally are carried out along parallel tracks, with track distances ranging from a few km to $1 0 ~ \mathrm { k m }$ and more. Orthogonal tracks serve for control and accuracy improvement by adjustment of the crossover discrepancies, (Denker and Roland, 2005), Fig. 5.69. The accuracy of sea and airborne gravity measurements (data recording generally with 1 s average) depends on the survey conditions (sea state, air turbulence, ship and aircraft properties, fl ight altitude and velocity), on attitude errors, and, for airborne gravimetry, on the separation between gravity and disturbing accelerations. Accuracies of 5 to $2 0 ~ { \mu \mathrm { m } } s ^ { - 2 }$ are achieved with sea gravimetry with a resolution of about $1 ~ \mathrm { k m }$ along track (track distances 1 to $5 \mathrm { k m }$ and more), Wessel and Watts (1988). Airborne gravimetry generally is carried out at fl ight heights of a few km, but low speed and elevation (several $1 0 0 ~ \mathrm { m } )$ ) surveys are also performed, especially with helicopters (Hammer, 1983; Segawa et al., 2002). A resolution of 5 to $1 0 ~ \mathrm { k m }$ is routinely obtained now (helicopter 1 to $3 \ \mathrm { k m } )$ ), with accuracies of 20 to $5 0 \mu \mathrm { m } \mathrm { s } ^ { - 2 }$ (helicopter $5 ~ { \mu \mathrm { m s } } ^ { - 2 }$ ). An increase in resolution and accuracy by a factor of two has been reached at surveys carried out at low altitudes and under favorable environmental conditions (e.g., Brozena and Peters, 1995; Skourop et al., 2009). It must be remembered that the attenuation of the gravity fi eld with height prevents a high frequency resolution at high fl ight altitudes. Also high frequency disturbances through turbulence still pose severe problems, and may lead to corresponding changes at fl ight planning.

Among the areas covered by airborne gravity surveys since the 1990s are the Arctic (Fig. 5.70) including Greenland (Brozena et al., 1997; Kenyon et al., 2008), alpine Switzerland and France (Verdun et al., 2002), the Amazon region, and parts of central Asia and Africa. An international Antarctic project has started in order to obtain a homogeneous gravity fi eld information over that continent which is only at small parts covered by terrestrial or airborne gravimetry (Scheinert, 2005).

![](images/74971564c20339d858393f238096a9a2b766c8b53a22f9acbbfae9cb75e46807.jpg)  
Fig. 5.69: Sea gravimetry profi les (1965–1972), Western Mediterranean Sea, Osservatorio Geofi sico Sperimentale, Trieste, after Finetti and Morelli (1973).

![](images/3b142d0ce98e10aff8e8f59c171fc83c8c697bfebc5a136e2f6ab1067be8a061.jpg)  
Fig. 5.70: Airborne gravity surveys over Greenland (1991/1992) and the Arctic (1998, 2003), Forsberg and Kenyon (1995) and Forsberg and Olesen (2010).

# 5.4.5 Gravity gradiometry

The gravity gradient tensor (3.68) contains local gravity fi eld information, and thus is of interest for high-resolution gravity fi eld determination. It is generally expressed in the local astronomic (local level) system, cf. [3.2.2]. The unit of the components of grad g is ${ \mathsf { S } } ^ { - 2 } ,$ with ${ { 1 0 } ^ { - 9 } } \ { { s } ^ { - 2 } } = { { 1 } \ { { \mathsf { n s } } ^ { - 2 } } }$ traditionally called Eötvös unit (E).

A gravity gradiometer determines the components of grad $\mathbf { g } ,$ either all, several or linear combinations of them. This is achieved by exploiting the reaction of neighboring proof masses to the gravity fi eld. A gradiometer unit consequently consists of two gravity sensors (mostly accelerometers) rigidly connected and generally orientated in the local level system. Taylor expansions of gravity in the two sensors 1 and 2, with respect to the center of mass $C$ of the system, and differences in the output of the sensors (specifi c force f ) yields in the stationary mode

$$
\mathbf { f } _ { _ { 2 } } - \mathbf { f } _ { _ { 1 } } = \big ( \mathrm { g r a d } \ \mathbf { g } \big ) _ { C } \big ( \mathbf { r } _ { _ { 2 } } - \mathbf { r } _ { _ { 1 } } \big ) ^ { I } ,
$$

where $\boldsymbol { \mathsf { r } } _ { 1 } , \boldsymbol { \mathsf { r } } _ { 2 }$ are the position vectors of the sensors in the local level system. A gradiometer system is composed of several gradiometer units orientated in different directions in order to derive the corresponding components (Fig. 5.71). Rotation of the gradiometer units in the gravity fi eld provides another means for the determination of different components (Torge, 1989, p. 300 ff.).

The torsion balance, developed by R.v. Eötvös around 1900, was the fi rst dedicated gravity gradiometer. It consists of two equal masses situated at different heights and rigidly connected by a beam system. At the center of mass the system is suspended by a torsional thread. Equilibrium of the torques acting on the masses is achieved by horizontal rotation, which depends on the components $W _ { _ { y y } } - W _ { _ { x x ^ { \prime } } } W _ { _ { x y ^ { \prime } } } W _ { _ { x z ^ { \prime } } } W _ { _ { y z } } .$ These quantities and the zero position of the beam are determined by observing the beam direction at fi ve different azimuths. A precision of 1 to $3 ~ \mathsf { n } \mathsf { s } ^ { - 2 }$ was obtained (Mueller et al., 1963). The torsion balance was widely employed in applied geophysics between 1920 and 1940, with great success at the early oil exploration, for example, at the reconnaissance of salt domes in Texas. The effect of rugged topography and close man-made constructions limited the application of the torsion balance to fl at areas and reduced the accuracy of the results to about $1 0 ~ \mathrm { { n s } ^ { - 2 } }$ . A dedicated borehole gravity gradiometer has been developed in order to detect changes in oil/gas/water pore space (Nukut, 1989).

![](images/398a82216c5f84b8439bb278b3a13ab4deceb97f4ceb74156a7292db405d2d96.jpg)  
Fig. 5.71: Gravity gradiometer translational system principle with longitudinal (left and center) and transverse (right) constellation.

On the Earth’s surface, gravimeters can also be used to approximate the components of grad $g$ by measuring gravity differences between adjacent stations. The horizontal gradient $( W _ { z x ^ { \prime } } W _ { z y } )$ can be derived with a precision of $1 0 ~ \mathrm { { n s } } ^ { - 2 }$ from gravity profi les or area surveys, with station distances of 10 to $1 0 0 ~ \mathrm { { m } }$ (Hammer, 1979). The vertical component $W _ { z z }$ can be determined with the same precision by repeated relative gravity measurements on tripods, with heights up to $3 \textrm { m }$ (Timmen, 2010, p.26 ff.).

Terrestrial gravity gradiometry in the stationary mode is time consuming and strongly affected by local mass anomalies. Terrain reductions have to be taken into account even in the immediate surrounding (within $1 0 0 \mathrm { ~ m } )$ , which limits the application to fl at or moderate hilly areas.

Measurements on moving platforms allow rapid data collection (e.g., with a 1 s rate or more). Terrain effects are signifi cantly reduced with height above ground, this favors airborne and satellite applications. With increasing height, on the other hand, the gradient signal decreases with the cube of the distance, which requires sophisticated data processing for the separation of signal and noise. We now concentrate on airborne gradiometry, satellite application have been presented in [5.2.8]. In this kinematic mode, the gradiometer unit consists of two accelerometer pairs, mounted orthogonally on a slowly rotating disk (Fig. 5.72), and set up on a gyro-stabilized platform. The disk’s rotation (rotation rate, e.g., $0 . 5 \mathsf { H z }$ minimizes systematic effects related to the instrument’s orientation. By subtracting the readings of a pair of opposing accelerometers, non-gravitational accelerations of linear type mostly cancel. As in airborne gravimetry, effects of the platform’s rotation about the Earth have to be taken into account, cf. [5.4.4].

Gravity gradiometry on moving platforms was adopted from military developments for U.S. Navy nuclear submarines (Bell Aerospace design), and further developed for geodetic and geophysical purposes (Jekeli, 1993). It reached commercial use at exploration geophysics (mineral deposits, cavities, groundwater) in the 1990s. Survey areas are limited in extension (few km to $1 0 ~ \mathrm { k m }$ or more), and are surveyed by parallel profi les with line spacing ranging from

![](images/48691d819a79713f28f4b90eba3d3a6578d8e4704cc5aa2e29884f6ba7a3cc64.jpg)  
Fig. 5.72: Rotating gravity gradiometer principle, after Jekeli (1988a).

$5 0 ~ \mathsf { m }$ to $2 ~ \mathrm { k m }$ . Small fi xed-wings aircrafts serve as gradiometer carrier, and fl ight height above ground may be less than $1 0 0 \mathrm { ~ m ~ }$ . By combining three gradiometer units mounted on rotating disks under different orientation, the full tensor gravity gradient containing fi ve independent elements can be derived. The additional hardware employed at a gravity gradiometry survey includes GPS for positioning and timing, and altimeter hardware for the construction of a highresolution digital elevation model. With present-day technology, an accuracy of a few $\mathsf { n } \mathsf { s } ^ { - 2 }$ and better can be obtained, with a gravity fi eld resolution down to about $5 0 \textrm { m }$ (Murphy, 2004; Dransfi eld and Lee, 2004).

Gravity gradiometry in the airborne mode is primarily applied in exploration geophysics, while geodetic application concentrates on dedicated satellite missions, cf. [5.2.8].

# 5.4.6 Continuous gravity measurements

Continuous gravity records contain information especially on Earth and ocean tides, but also on a multitude of other geodynamic phenomena, ranging from seismic normal modes over atmospheric and ocean loading, free core nutation, polar motion and hydrologic effects to post-glacial rebound, tectonics, and volcanic and earthquake activity (Wilhelm et al., 1997). These effects occur at time scales between seconds and several years and have amplitudes of about 1 to 1000 (tides) $\mathsf { n m s } ^ { - 2 }$ , cf. [8.3.6]. Hence, a recording gravimeter should provide a resolution of 0.01 to $1 ~ \mathrm { { n m s } ^ { - 2 } }$ and a high stability with time (low drift rates). It should be time-controlled within $1 0 ~ \mathsf { m s }$ . In order to reduce environmental effects (temperature changes, microseismicity, local surface inclinations), recording gravimeters generally are installed at underground sites (basement, tunnel).

Recording gravimeters operate in an electronic feedback mode, cf. [5.4.2], over a limited measuring range, e.g., $1 0 ~ { \mu \mathrm { m s } } ^ { - 2 }$ . The voltage output is proportional to gravity and fi rst undergoes an analog fi ltering in order to reduce the high-frequency noise. It is then digitized by an A/D converter. Digital fi ltering delivers a data set (1 to 10 s samples), which is stored on a PC. Further numerical fi ltering and data reduction may be appropriate as well as the reduction of spikes due to earthquakes and the interpolation of data gaps. Corresponding procedures are part of data processing software for Earth tides analysis (Wenzel, 1996). An analogue output offers a convenient on-line control of the data acquisition.

Spring-type and superconducting (also cryogenic) gravimeters are used for gravity recording (Melchior, 1983).

Elastic spring gravimeters can be employed if supplemented with a low-pass fi lter, a recording unit, and a quartz clock. Special Earth tide gravimeters with small measuring range have also been developed and are characterized by long-term stability (e.g., by a double thermostat). Some recent land gravimeters also offer the option of an Earth tides mode through increased sensitivity, large memory, and computer-controlled remote operation. The long-term drift of these elastic-spring type instruments has to be removed by fi ltering. Consequently, only short-period effects (e.g., diurnal and higher-frequency tides) can be determined, at a noise level of a few 0.1 to $1 \ \mathrm { n m s } ^ { - 2 }$ (Fig. 5.73).

For the superconducting gravimeter (Goodkind, 1999) the gravity acting on the proof mass (hollow Niobium sphere of $2 . 5 \mathrm { c m }$ diameter) is compensated by a magnetic counterforce (Fig. 5.74). The magnetic fi eld is generated by superconducting coils and thus is extremely stable with time. The position of the mass levitating in the magnetic fi eld is monitored by capacitive sensing plates, with the zero position restored by a feedback system. Cooling by liquid helium provides the superconducting state at a temperature