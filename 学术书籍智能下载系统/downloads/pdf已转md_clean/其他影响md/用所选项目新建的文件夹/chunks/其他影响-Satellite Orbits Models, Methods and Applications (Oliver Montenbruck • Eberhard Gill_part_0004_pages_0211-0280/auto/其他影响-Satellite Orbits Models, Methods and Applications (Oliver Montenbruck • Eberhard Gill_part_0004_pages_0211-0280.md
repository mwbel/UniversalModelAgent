frequencies, ${ \boldsymbol { v } } _ { t }$ and ${ \pmb v } _ { r }$ are the velocities of the transmitter and the receiver, $e$ is the unit vector in the direction of the signal propagation, and $U _ { t }$ and $U _ { r }$ are the Newtonian potentials at the transmitter and the receiver. The $c ^ { 2 }$ -terms in (6.3) result from the general and special theory of relativity.

The frequency shift cannot, however, be measured instantaneously. The Doppler shift is measured instead by counting accumulated cycles of zero-crossings between the received frequency $f _ { r }$ and a reference frequency $f _ { \mathrm { r e f } }$ over a count time $t _ { c }$ . The measurement is also referred to as integrated Doppler measurement and must be clearly distinguished from the instantaneous Doppler shift.

Table 6.1. Transponder turn-around ratios (CCSDS 1998)   

<table><tr><td rowspan=1 colspan=1>Band</td><td rowspan=1 colspan=1>fe [MHz]</td><td rowspan=1 colspan=1>fr [MHz]</td><td rowspan=1 colspan=1>T1,2</td></tr><tr><td rowspan=1 colspan=1>S/S</td><td rowspan=1 colspan=1>2025-2120</td><td rowspan=1 colspan=1>2200－2300</td><td rowspan=1 colspan=1>240/221</td></tr><tr><td rowspan=1 colspan=1>X/X</td><td rowspan=1 colspan=1>7145-7235</td><td rowspan=1 colspan=1>8400－8500</td><td rowspan=1 colspan=1>880/749</td></tr><tr><td rowspan=1 colspan=1>S/X</td><td rowspan=1 colspan=1>2025-2110</td><td rowspan=1 colspan=1>8450-8500</td><td rowspan=1 colspan=1>900/221</td></tr><tr><td rowspan=1 colspan=1>X/S</td><td rowspan=1 colspan=1>7190- 7235</td><td rowspan=1 colspan=1>2200－ 2290</td><td rowspan=1 colspan=1>240/765</td></tr></table>

Consider a two-way Doppler measurement, where a radar signal is emitted from a ground station with frequency $f _ { e }$ and is received at the satellite with a certain Doppler shift (Fig. 6.2b). To avoid interference of the received and transmitted signals at the satellite, a satellite transponder coherently multiplies the received frequency by the transponder turn-around ratio $T _ { 1 , 2 }$ before the transmission to the ground station. Within the transponder a phase locked loop (PLL) assures that the precise fidelity of the received signal is transmitted by the satellite. The transponder ratios are standardized and depend on the frequency bands involved (Table 6.1). The carrier signal is then received at the same ground station (two-way) with about twice the Doppler shift of the uplink or at a separate station (three-way). The Doppler measurement provides the number of accumulated cycle counts

$$
N = \int _ { t _ { 1 } } ^ { t _ { 2 } } \left( f _ { r } - f _ { \mathrm { r e f } } \right) d t
$$

in the interval $[ t _ { 1 } , t _ { 2 } ]$ . Under the assumption of a constant reference frequency over the count interval this can also be expressed as

$$
N = \int _ { t _ { 1 } } ^ { t _ { 2 } } f _ { r } d t - f _ { \mathrm { r e f } } ( t _ { 2 } - t _ { 1 } ) .
$$

The same number of accumulated cycles $N$ is present in the interval $[ t _ { 1 } - \tau _ { 1 } , t _ { 2 } - \tau _ { 2 } ]$ , where $\tau _ { 1 }$ and $\tau _ { 2 }$ are the signal travel times for signals received at the station at the start $t _ { 1 }$ and end $t _ { 2 }$ of the count interval. Let $T _ { 1 , 2 } f _ { e }$ be the reception frequency for zero Doppler, then

$$
\int _ { t _ { 1 } } ^ { t _ { 2 } } f _ { r } d t = T _ { 1 , 2 } \int _ { t _ { 1 } - \tau _ { 1 } } ^ { t _ { 2 } - \tau _ { 2 } } f _ { e } d t ~ .
$$

Assuming a constant transmission frequency over the count-time interval, the number of counts is given by

$$
N = T _ { 1 , 2 } f _ { e } [ ( t _ { 2 } - \tau _ { 2 } ) - ( t _ { 1 } - \tau _ { 1 } ) ] - f _ { \mathrm { r e f } } ( t _ { 2 } - t _ { 1 } ) .
$$

Provided that the reference frequency $f _ { \mathrm { r e f } }$ at the ground station is set to $T _ { 1 , 2 } f _ { e }$ the Doppler count may finally be expressed as

$$
N = T _ { 1 , 2 } f _ { e } ( \tau _ { 1 } - \tau _ { 2 } ) .
$$

As the two-way Doppler counts themself are abstract measurements, a conversion is usually applied to average range rate measurements $\bar { \dot { \rho } }$ according to

$$
\bar { \dot { \rho } } = - \frac { 1 } { 2 } \frac { c N } { T _ { 1 , 2 } f _ { e } t _ { c } } .
$$

Here $t _ { c } = t _ { 2 } - t _ { 1 }$ denotes the duration of the count interval and the negative sign relates a positive Doppler frequency shift (approach) to a negative range rate. The measurement may then be modeled as the difference of the two-way range at the a delta range over the count time

$$
\bar { \dot { \rho } } = \frac { 1 } { 2 } \frac { c ( \tau _ { 2 } - \tau _ { 1 } ) } { t _ { c } } = \frac { \rho _ { 2 } - \rho _ { 1 } } { t _ { c } } .
$$

Here $\rho _ { 1 } = 1 / 2 c \tau _ { 1 }$ is the two-way range, i.e. one half of the light path of a signal being transmitted at $t _ { 1 } - \tau _ { 1 }$ from the station and received again at the station at time $t _ { 1 }$ . Likewise $\rho _ { 2 }$ is the two-way range value for a ground reception time $t _ { 2 }$ .

Existing Doppler tracking systems usually derive the reference frequency from the transmitted carrier frequency. Furthermore, the electronic implementation must assure that the frequency being counted exhibits no zero-crossings. A known frrequency bias is therefore added to the received signal prior to subtracting the reference frequency from it. Basically two different realizations of cycle counters are available. The first method counts the number of cycles of the reference frequency $N$ required to accumulate a fixed number of cycles of the Doppler-plus-bias cycle counter. The count time $t _ { c }$ is not fixed for this measurement technique. The cycle counter is reset after each measurement. Therefore, this method is called a destructive Doppler measurement. The second approach accumulates the Doppler-plus-bias count over a pre-defined number of reference frequency cycles, or equivalently, a fixed count time $t _ { c }$ . The Doppler-plus-bias counter is not reset after each measurement, therefore this method is referred to as a non-destructive Doppler measurement. As the counter is not reset an accumulated phase variation over time is recorded and the non-destructive Doppler measurement may be referred to as a biased range measurement.

The noise of two-way Doppler data is often expressed by the phase noise $\sigma _ { \varphi }$ with typical values of 0.1 rad. This may be converted to the range rate noise according to (Segura 1998)

$$
\sigma _ { \dot { \rho } } = \frac { \sqrt { 2 } c } { 2 T _ { 1 , 2 } f _ { e } t _ { c } } \frac { \sigma _ { \varphi } } { 2 \pi } .
$$

For S-band signals $( 2 \ \mathrm { G H z } )$ and a count time of $1 \mathrm s$ a representative accuracy of about $1 \mathrm { m m / s }$ is achieved.

# DORIS

DORIS (Doppler Orbitography and Radiopositioning Integrated by Satellite) is a precise Doppler tracking system developed by CNES (Centre National d’Études Spatiales), GRGS (Groupe de Recherche en Géodésie Spatiale), and the IGN (Institut Géographique National). The first DORIS receiver was implemented on SPOT2 in 1990, followed by receivers on TOPEX/Poseidon, SPOT3, SPOT4, and a planned utilization for ENVISAT, Jason, and SPOT5.

DORIS is a one-way Doppler tracking system, where the frequency shift of a radio signal transmitted from a ground beacon is measured onboard the satellite (Fig. 6.2d). To this end, the satellite receiver applies an ultrastable oscillator (USO), i.e. a temperature-controlled crystal oscillator with an Allen variance of $5 { \cdot } 1 0 ^ { - 1 3 }$ over the count time of $1 0 \mathrm s$ , which results in a Doppler noise value of $0 . 3 \mathrm { m m } / \mathrm { s }$ for the precision measurements (Laudet et al. 1995). As DORIS is a single-channel, dualfrequency receiver, only signals from one ground station at a time are supported.

The DORIS ground segment comprises about 50 uniformly distributed small ground stations that provide a geographical coverage of better than $80 \%$ for the TOPEX/Poseidon mission. Each of the automated ground stations consists of a beacon that transmits two ultrastable frequencies: $2 0 3 6 . 2 5 \mathrm { M H z }$ for precise Doppler tracking and $4 0 1 . 2 5 \mathrm { M H z }$ for ionospheric Doppler correction. The latter frequency is also used for auxiliary data transmission, such as meteorological data at the ground site that are required for tropospheric corrections.

The DORIS control center is situated at Toulouse, France, where the daily schedule of the beacon contacts is computed. The command transmission and telemetry reception is performed using two master beacons at Toulouse and Kourou. In addition, the master beacon also provides the long-term frequency stability, as it is linked to a cesium atomic clock. To cope with deviations of the ground-based beacons and the satellite USO, biases are solved for each individual pass, and the satellite frequency is thus linked to the frequency of the master beacon. The tracking data collected at the satellite are stored in the receiver’s telemetry memory and dumped twice a day to the ground, where time-tagging, preprocessing, and orbit determination are performed.

# 6.1.2 Laser Tracking

Satellite laser ranging (SLR) is a technique for precisely measuring the range between a laser station and a satellite that is equipped with retroreflectors. SLR was demonstrated as early as 1964 and since then a continuous extension of laser tracking networks has been achieved together with a steady improvement of the measurement accuracy. Nowadays more than 40 laser stations track satellites like GFZ-1, Lageos I, TOPEX/Poseidon, ERS-2, as well as the GPS-35 and GPS-36 satellites with a precision in the range of one centimeter.

Modern laser transmitters use a solid-state pulsed laser that applies neodymium as a lasing impurity in a lattice of yttrium aluminum garnet (Nd:YAG) (Degnan & Pavlis 1994). This allows the generation of green laser light with a wavelength of

$5 3 2 \mathrm { n m }$ and ultra-short pulses of 30–200 ps width that are repeated at a rate of $5 -$ $1 0 \mathrm { H z }$ . When a laser pulse is transmitted by the telescope (Fig. 1.9), a discriminator starts a time interval counter for initialization of a range measurement. The laser pulse then propagates through the atmosphere until it is reflected by a retroreflector array onboard a satellite. When the pulse is received at the telescope, a high-speed photodetector stops the time interval counter with a time granularity of less than 20 ps, equivalent to a one-way range precision of better than $3 \ \mathrm { m m }$ . The half difference of the counter stop and start time multiplied by the velocity of light hence gives an unambiguous average one-way range. The measurement is timetagged with an accuracy of better than a microsecond, when a rubidium or cesium atomic clock is applied that is regularly synchronized by a GPS time receiver.

The precision of modern SLR systems is usually given as the root-mean-square of the single-shot accuracy over a single pass and is in the order of $5 { - } 5 0 ~ \mathrm { m m }$ . To further reduce the data scatter, normal points are formed at the laser stations by averaging individual range measurements over a two-minute data interval. This reduces the RMS values by a factor of 4–5 (Husson 1997) and thus leads to a normal point RMS of $1 { - } 1 2 \mathrm { m m }$ . Systematic errors in the station hardware, such as non-linearities in the tracking electronics, lead to biases that limit the absolute SLR accuracy to $\pm 1 \mathrm { c m }$ (Marshall et al. 1995).

Due to the high accuracy of SLR data, geodetic applications in the fields of crustal dynamics, gravity field determination, and Earth rotation parameter estimation are the major applications of SLR. In addition, the development of precise satellite force models, and the calibration of other tracking devices significantly benefit from SLR (Zhu et al. 1997).

It is noted that laser tracking (other than radar tracking) does not allow autotracking of satellites, but depends on the availability of high-precision a priori orbit elements for antenna pointing. Furthermore, the use of SLR for regular tracking is restricted due to its dependence on the weather at the laser stations and to the dense operations schedule of the ground segment.

# 6.1.3 The Global Positioning System

NAVSTAR GPS (NAVigation System with Time and Ranging Global Positioning System) is a satellite-based radio navigation, positioning, and time-transfer system. It was initiated in 1973 and achieved its full operational capability in 1995. GPS consists of three major segments: the space segment, the control segment, and the user segment.

The GPS space segment comprises 24 satellites deployed in six evenly spaced planes (A to F) with $5 5 ^ { \circ }$ inclination, and with four satellites per plane (Fig. 6.4). The GPS satellites move in near-circular orbits with an altitude of about $2 0 2 0 0 \mathrm { k m }$ and a period of 12 sidereal hours. The space segment provides a global and continuous coverage with at least four simultaneously visible satellites. A ground-based user will observe the same satellite constellation once per day but four minutes earlier each day due to the difference between the sidereal and solar day.

![](images/6dc3054e1f9275fbb3d2da9f1f425f0862e53ea9e4fb0859a53c1875170b68ed.jpg)  
Fig. 6.4. GPS Space Segment Constellation

The GPS control segment consists of five monitor stations, a master control station, and three ground control stations. The unmanned monitor stations are located at Colorado Springs, Hawaii, Kwajalein, Diego Garcia, and Ascension Island. They are equipped with a GPS receiver and a cesium atomic clock to perform continuous one-way pseudorange measurements to all GPS satellites in view as well as weather data measurements for tropospheric corrections. The coordinating master control station at the Schriever Air Force Base, Colorado Springs, Colorado, is responsible for the GPS satellite control and system operations. It collects the tracking data from the monitor stations and computes the satellite ephemerides and clock parameters that are transferred to the ground control stations for daily command upload. The ground control stations operate in the S-band and are collocated with the monitor stations at Ascension, Diego Garcia, and Kwajalein.

GPS provides two levels of service to the user segment. A Standard Positioning Service (SPS) provides position and timing information to any user on a continuous worldwide basis. The Precise Positioning Service (PPS) provides position, velocity, and timing information to authorized U.S. and allied military, federal government, and civil users who can satisfy specific U.S. requirements. The specified 50th percentile SPS and PPS accuracies are compiled in Table 6.2, and are based on instantaneous GPS measurement sets for the computation of the position and velocity in the presence of typical random and systematic errors.

The GPS satellites transmit microwave carrier signals at the L1 frequency (1575.42 MHz) and the L2 frequency (1227.60 MHz). The second frequency allows measurement of the ionospheric signal delay using PPS-capable receivers. Three binary codes are modulated on the L1 or L2 carrier or both:

Table 6.2. SPS and PPS 50th percentile accuracies for instantaneous measurements (NRC 1995)   

<table><tr><td>Specification</td><td>SPS</td><td>PPS</td></tr><tr><td>Position horizontal</td><td>40m</td><td>8m</td></tr><tr><td>vertical spherical</td><td>47m</td><td>9m</td></tr><tr><td>Velocity</td><td>76m</td><td>16m</td></tr><tr><td>any axis</td><td></td><td>0.07m/s</td></tr><tr><td>Time</td><td></td><td></td></tr><tr><td>GPS UTC</td><td>95ns 115ns</td><td>17ns 68ns</td></tr></table>

1. The Coarse Acquisition (C/A) code is a short pseudorandom noise (PRN) code of 1023 bits or $1 ~ \mathrm { m s }$ duration at a 1.023 Mbps bit rate (Spilker 1978). The C/A code modulates the L1 carrier and is the basis for the civil SPS. Since each satellite has a specific and different C/A code PRN, GPS satellites may uniquely be identified by their PRN number.   
2. The Precise (P) code is a PRN code with about $6 { \cdot } 1 0 ^ { 1 2 }$ bits, equivalent to a period of exactly one week and a bit rate of 10.23 Mbps. The P code modulates both the L1 and L2 carrier phases and is the basis for the military PPS. When the Anti-Spoofing (AS) mode is active, the P code is encrypted into the Y code and requires a classified AS module with cryptographic keys.   
3. The navigation data are transmitted in a 50 bit/s stream, added to the C/A and P(Y) codes on the L1 frequency and, depending on the satellite mode, also on the L2 P(Y) code. Each message word consists of 30 bits with 10 words in one subframe. Each frame consists of 5 subframes and a superframe consists of 25 frames. Thus the navigation message comprises 37 500 bits and is repeated every 12.5 minutes (Spilker 1994). The navigation message contains low-accuracy (almanac parameters) and high-accuracy (broadcast ephemeris) GPS satellite orbit data as well as clock corrections, and other system parameters (see Annex A.2).

An overview of the GPS signal characteristics is given in Table 6.3, where the frequency and wavelength for the PRN-codes refers to their chip length.

Table 6.3. GPS satellite signal characteristics (Spilker 1978)   

<table><tr><td>Signal</td><td>Type</td><td>f</td><td>Frequency [MHz]</td><td>Wavelength [cm]</td></tr><tr><td>Satellite Clock</td><td></td><td>fo</td><td>10.23</td><td>2931</td></tr><tr><td>Carrier Signal</td><td>L1</td><td>154 fo</td><td>1575.42</td><td>19.05</td></tr><tr><td></td><td>L2</td><td>120 fo</td><td>1227.60</td><td>24.45</td></tr><tr><td>PRN-Codes</td><td>P</td><td>f</td><td>10.23</td><td>2931</td></tr><tr><td></td><td>C/A</td><td>0.1fo</td><td>1.023</td><td>29310</td></tr></table>

The GPS-based positioning relies essentially on the measurement of biased one-way range data, called pseudoranges (Fig. 6.2f). To perform pseudorange measurements, the GPS receiver produces replicas of the C/A or P(Y) code for a specific GPS satellite and shifts the code in time until the cross-correlation of the satellite and the receiver codes achieves a maximum. The measured code phase $\varPhi ( t _ { r } )$ corresponds to a reception time $t _ { r }$ at the receiver clock while the signal transmission time $t _ { t }$ is provided via the PRN code. Hence the difference of the transmission and reception time readings multiplied by the velocity of light $c$ yields a range value of

$$
\rho _ { \phi } ( t _ { r } ) = c ( t _ { r } - t _ { t } ) .
$$

This is actually called a pseudorange (Hofmann-Wellenhof et al. 1997) since $t _ { r }$ and $t _ { t }$ are obtained by different clocks. Denoting GPS system time by a superscript GPS and offsets of the receiver and transmitter clocks from GPS time by the symbols $\delta t _ { r }$ and $\delta t _ { t }$ the pseudorange is obtained as

$$
\rho _ { \phi } ( t _ { r } ) = c \left( ( t _ { r } ^ { \mathrm { G P S } } + \delta t _ { r } ) - ( t _ { t } ^ { \mathrm { G P S } } + \delta t _ { t } ) \right) .
$$

Using $\Delta t ^ { \mathrm { G P S } } = t _ { r } ^ { \mathrm { G P S } } - t _ { t } ^ { \mathrm { G P S } }$ and $\delta t = \delta t _ { r } - \delta t _ { t }$ it can be seen that the pseudorange

$$
\rho _ { \phi } ( t _ { r } ) = c \left( \varDelta t ^ { \mathrm { G P S } } + \delta t \right)
$$

is larger than the actual signal path by a distance $c \delta t$ , which depends on the relative offset of the two clocks. Since the individual clock errors exhibit independent variations with time, the difference between the pseudorange and the actual range is also a time-varying quantity.

Due to the C/A code length of about $1 ~ \mathrm { m s }$ the C/A code pseudoranges are ambiguous at about $3 0 0 \mathrm { k m }$ , while the P(Y) code pseudoranges are unambiguous. As the code phases are determined with a typical accuracy of 0.1 rad $( 1 \sigma )$ or about 0.01591 cycles, the noise figures for code phases are $0 . 0 1 5 9 1 \cdot 2 9 3 \mathrm { m } \sim 5 \mathrm { m }$ for C/A code pseudoranges and $0 . 5 \mathrm { m }$ for $\mathrm { P }$ code pseudoranges.

Highly precise GPS carrier phase measurements or phase pseudoranges apply the carrier phase $\phi$ instead of the code phase $\varPhi$ and thus require no information modulated on the carrier. Here the phase of the GPS satellite signal received by the user at GPS system time $t$ is given as

$$
\phi _ { r } ( t ) = f _ { t } \left( t - \varDelta t ^ { \mathrm { G P S } } \right) + f _ { t } \delta t _ { t }
$$

where $f _ { t }$ is the emitted frequency and $f _ { t } \varDelta t ^ { \mathrm { G P S } }$ denotes the phase retardation due to the signal propagation from the transmitter to the receiver. At the receiver a reference signal with phase

$$
\phi _ { \mathrm { r e f } } ( t ) = f _ { \mathrm { r e f } } t + f _ { \mathrm { r e f } } \delta t _ { r }
$$

is generated using the receivers reference frequency $f _ { \mathrm { r e f } }$ . The phase difference

$$
\phi _ { r } ( t ) - \phi _ { \mathrm { r e f } } ( t ) = N + \Delta \phi
$$

which is also called the beat phase, may then be expressed by an integer number of cycles $N$ and the actual measurement value $\varDelta \phi$ , known as the instantaneous fractional beat phase. Provided that the reference frequency equals the transmitted frequency, insertion of (6.15) and (6.16) into equation (6.17) gives, the observation equation

$$
\rho _ { \phi } ( t ) = c \varDelta t ^ { \mathrm { G P S } } + \lambda N + c \delta t
$$

where $\rho _ { \phi } = - \lambda \varDelta \phi$ is the range equivalent of the measured phase difference. The integer number of carrier cycles $N$ is unknown, hence carrier phase measurements are ambiguous with one wavelength $\lambda$ of about $2 0 \mathrm { c m }$ . During a continuous signal lock of a GPS satellite by the receiver, the integer ambiguity $N$ remains constant for that satellite. The ambiguity resolution may be achieved with different techniques (Hofmann-Wellenhof et al. 1997). It has, however, to be kept in mind that ambiguity resolution may require a high computational effort or may even fail under certain conditions. When the signal lock is lost, the integer ambiguity after re-establishing the lock is changed, which is known as cycle slip. Considering that carrier phases are determined with an accuracy of at least 0.1 rad or about 0.01591 cycles, the noise figures for carrier phases are less than $3 \mathrm { m m }$ and $4 \mathrm { m m }$ for L2 and L1 signals, respectively.

GPS users with moderate or low-positioning requirements may directly apply the receiver’s navigation solution or position fixes, i.e. the receiver coordinates $( x , y , z )$ in the Earth-centered, Earth-fixed reference frame WGS-84. Position fixes are not raw GPS measurements, but are derived from code pseudoranges that may have been smoothed by carrier phases within the receiver for data noise reduction. The derivation of position fixes is based on the geometric method of triangulation, where three range measurements to three locations of known position uniquely determine the receiver’s coordinates. For GPS applications, pseudoranges to at least four GPS satellites simultaneously have to be available to determine, in addition to the position, the receiver’s instantaneous clock offset with respect to GPS system time.

As the inherent SPS performance leads to a positioning accuracy of about $1 0 \mathrm { m }$ (Parkinson 1994), an intentional degradation has been implemented, called Selective Availability (SA). SA consists of a manipulation of the navigation message orbit data ( $\cdot$ process) as well as the intentional degradation of the satellite clock frequency (δ process), also known as clock dither. The clock dither leads to oscillations in the C/A code and P code pseudoranges of $2 3 \mathrm { ~ m ~ } ( 1 \sigma )$ with a period of $2 { - } 5 ~ \mathrm { m i n }$ (van Graas & Braasch 1994), while the $\epsilon$ process leads to a slow variation of the satellite positions with an amplitude of $5 0 { - } 1 5 0 \mathrm { m }$ (Hofmann-Wellenhof et al. 1997) and a period of the order of hours. As a result, the achievable SPS position accuracy in the presence of SA amounts to roughly 100 meters and only authorized users are able to correct for these errors. In support of commercial GPS applications SA has been deactivated, however, on 1 May 2000 by decision of the US government. Since then every user of a single-frequency GPS receiver is able to achieve a position accuracy of $1 0 \mathrm { m }$ .

The GPS makes use of two dedicated representations of the GPS satellite orbits, which are known as almanac and (broadcast) ephemeris (see Annex A.2). Both parameter sets are transmitted as part of the GPS navigation message and enable a user receiver to compute positions of the GPS satellites with different levels of accuracy. Almanac data are mainly used to determine the constellation of visible satellites above the horizon, to select the best satellites for navigation and to determine approximate Doppler shifts for improved signal acquisition. The receiver has to demodulate the entire navigation data superframe within 12.5 minutes to completely retrieve all almanac data. The almanac accuracy is about $9 0 0 \mathrm { m }$ within a one-day interval from the transmission of the almanac and degrades to $1 2 0 0 \mathrm { m }$ and $3 6 0 0 \mathrm { m }$ respectively within a one-week and two-week interval (Spilker 1994). Almanac updates are performed at least once in six days. The ephemeris parameters, on the other hand, provide a much more accurate description of the spacecraft trajectory that is essential for the computation of precise user position fixes. The broadcast ephemerides are accurate to $5 { - } 1 0 \mathrm { m }$ in the absence of SA and $5 { - } 1 0 0 \mathrm { m }$ (Hofmann-Wellenhof et al. 1997) if SA is active. Broadcast ephemeris updates are performed approximately every hour and are valid through a period of four hours. In accordance with the envisaged usage, the low-accuracy almanac parameters are always provided for the full constellation of active satellites, whereas each satellite only transmits ephemeris parameters for itself.

In addition to the raw GPS measurement types, a variety of combinations of raw measurement types can be applied to facilitate the data analysis. These derived measurement types are, in general, constructed by computing the difference of raw GPS measurements referring to the same measurement epoch. Taking single carrier phase differences that involve two receivers and a single GPS satellite, it can e.g. be shown that the satellite clock error cancels. Likewise, double carrier phase differences are computed from single carrier phase differences to two GPS satellites. Both GPS satellite and user clock errors are cancelled for this data type. Vice-versa, the combination of raw measurement types allows the isolation of specific error contributions. As an example, multipath effects that are caused by reflecting surfaces in the vicinity of the GPS antenna can be evaluated by forming the difference of ionosphere-corrected code and carrier pseudoranges.

# 6.2 Tracking Data Models

# 6.2.1 Transmitter and Receiver Motion

Satellite tracking methods involve the propagation of a signal over a finite time span. The signal is recorded at the receiver at a certain time $t$ but originates from a transmitter at an earlier time $t - \tau < t .$ Thus, a rigorous observation model has to account for the motion of the transmitter and the receiver during the signal travel time $\tau$ .

The signal travel time $\tau$ ranges from 5 ms for low-Earth orbiting (LEO) satellites up to $1 0 0 ~ \mathrm { { m s } }$ for geostationary satellites (GEO). Thus, the computation of the satellite position at the time of signal transmission $r ( t - \tau )$ can be performed either by an interpolation of adjacent position values or by a Taylor expansion

$$
\pmb { r } ( t - \tau ) \approx \pmb { r } ( t ) - \pmb { \dot { r } } ( t ) \tau + \frac { 1 } { 2 } \pmb { \ddot { r } } ( t ) \tau ^ { 2 } ,
$$

where $\dot { \boldsymbol { r } }$ and $\ddot { r }$ are the inertial satellite velocity and acceleration, respectively. With a satellite velocity of $3 \mathrm { k m / s }$ for GEO’s and $7 . 5 \mathrm { k m / s }$ for LEO’s the linear term in (6.19) is about $4 0 0 \mathrm { m }$ for GEO’s and $1 0 0 \mathrm { m }$ for LEO’s, while the second-order term is about $2 \mathrm { m m }$ . When using numerical integration methods for the trajectory prediction the satellite position at signal transmission may be obtained from interpolation of subsequent integration steps. Preferrably, however, an integration method should be used that directly supports dense output generation (cf. Chap. 4).

The motion of a ground station in an inertial reference system is dominated by the Earth rotation with a velocity of $4 6 0 \mathrm { m / s }$ at the equator. When the motion of the ground station is modeled in the inertial International Celestial Reference System (ICRS, see Sect. 5.2), the position $R _ { \mathrm { { I T R S } } }$ of the station in the International Terrestrial Reference System (ITRS) has to be transformed using the matrices for precession $( P )$ , nutation $( N )$ , Earth rotation $( \pmb { \Theta } )$ and polar motion $( \pmb { I } )$ according to

$$
{ \cal R } _ { \mathrm { I C R S } } \ : = \ : P ^ { T } ( t ) \ : N ^ { T } ( t ) \ : \Theta ^ { T } ( t ) \ : { \cal { \cal { I } } } ^ { T } ( t ) { \cal { R } } _ { \mathrm { I T R S } } .
$$

In addition, the precise computation of the ground station position requires modeling site displacements due to tidal perturbations and plate motion. Due to the differential lunisolar acceleration, the solid Earth tides cause a maximum radial site displacement of $2 5 \mathrm { m m }$ with a daily period. Horizontal displacements are less than one millimeter, and are in general neglected. The ocean tides deform the Earth’s crust and hence each ground station undergoes a displacement that reaches a few centimeters near the coast and less than one centimeter for continental stations (Mc-Carthy 1996). The pole tides are caused by the contribution of the polar motion in the centrifugal potential due to the Earth rotation. They lead to a tidal response with a maximum radial displacement of $2 5 \mathrm { m m }$ and a maximum horizontal displacement of $7 \mathrm { m m }$ (McCarthy 1996). Similar amplitudes are found for atmospheric loading, i.e. temporal variations in the geographic distribution of atmospheric masses that deform the Earth’s surface (Manabe et al. 1991). For geodetic applications, the relative motion of stations on different tectonic plates with rates of $5 \mathrm { { c m } }$ per year or larger may be accounted for using a plate motion model (DeMets et al. 1994).

# 6.2.2 Angle Measurements

# Light Time and Aberration

Angle measurements are modeled using the vector $d = r - R$ from the ground station to the satellite. Due to the finite velocity of light, the geometric relative

position $\pmb { d } _ { 0 } = \pmb { r } ( t ) - \pmb { R } ( t )$ at the time $t$ of signal reception is different, however, from the true signal path. This is given by the vector

$$
\pmb { d } = \pmb { r } ( t - \tau ) - \pmb { R } ( t )
$$

that links the ground station position $\pmb { R } ( t )$ at the reception time to the satellite position $r ( t { - } \tau )$ at the transmission time (cf. Fig. 6.5). The signal travel time $\tau$ may thus be computed from the implicit light-time equation

$$
c \tau = | \pmb { r } ( t - \tau ) - \pmb { R } ( t ) | \quad .
$$

Starting from an initial value of $\tau ^ { ( 0 ) } = 0$ the light time is consecutively determined using the fixed-point iteration

$$
\tau ^ { ( i + 1 ) } = 1 / c \cdot | \pmb { r } ( t - \tau ^ { ( i ) } ) - \pmb { R } ( t ) | \quad .
$$

The iteration may be continued until successive values of $\tau$ agree to better than a certain threshold, such as $1 0 ^ { - 7 } \mathrm { s }$ for general data types. Given a light time of 0.01 s for a low-Earth orbiting satellite, the light-time correction for angle measurements is in the order of $7 ^ { \prime \prime }$ . Here, the correction refers to the difference between the true signal path $( d )$ and the geometric relative position $( d _ { 0 } )$ .

![](images/ceca910464b46fad941f9aef591b24db228294e7a69c14742543c88c42d73fea.jpg)  
Fig. 6.5. The motion of the satellite during signal travel time for the downlink

![](images/6639817938fe5d115cec117afdd1016d8563fc72465792b67c5d7ca6cfa55e7b.jpg)  
Fig. 6.6. The effect of aberration

The solution of the light-time equation yields the true signal path in the inertial system which is different, however, from the apparent direction to the spacecraft for a moving ground station. This effect is known as aberration and may be understood by considering the relative motion of the incoming signal and the observer (Fig. 6.6). Neglecting a rigorous formulation within the theory of special relativity, the observed direction is given by the vector

$$
\pmb { d } ^ { \prime } = \pmb { d } + \tau \pmb { V } \quad ,
$$

where $V$ is the inertial velocity of the ground station relative to the geocenter. Thus the apparent position

$$
d ^ { \prime } = d + \tau V = r ( t - \tau ) - R ( t ) + \tau V ( t ) \approx r ( t - \tau ) - R ( t - \tau )
$$

matches the geometric position at time $t - \tau$ to first order. The aberration is about $0 . 6 { ^ { \prime \prime } }$ for low-Earth satellites and $0 . 3 { ^ { \prime \prime } }$ for geostationary satellites. It can be neglected in most cases in view of the limited resolution of common radar tracking systems.

For a station with geodetic coordinates $( \lambda , \varphi , h )$ the three unit vectors

$$
\begin{array} { r } { e _ { \mathrm { E } } = \left( \begin{array} { c } { - \sin \lambda } \\ { + \cos \lambda } \\ { 0 } \end{array} \right) \quad e _ { \mathrm { N } } = \left( \begin{array} { c } { - \sin \varphi \cos \lambda } \\ { - \sin \varphi \sin \lambda } \\ { \cos \varphi } \end{array} \right) \quad e _ { \mathrm { Z } } = \left( \begin{array} { c } { \cos \varphi \cos \lambda } \\ { \cos \varphi \sin \lambda } \\ { \sin \varphi } \end{array} \right) } \end{array}
$$

that point to the east, north, and zenith direction provide a natural and convenient frame for describing a satellite’s motion with respect to an antenna (cf. Fig. 6.7). According to their definition, $e _ { \mathrm { E } }$ and $e _ { \mathrm { N } }$ span the tangential plane to the reference ellipsoid, while $e _ { Z }$ points to the geodetic zenith. Aside from small deviations of the geoid from the adopted reference ellipsoid, the tangential coordinate system is aligned with the horizon and the zenith as defined by the local direction of the plumb line.

![](images/fb066d144c04c06efd9eb9763c30c8e0b659aac17af84f4f1eb4130c1649041c.jpg)  
Fig. 6.7. Orientation of local horizontal coordinate systems

The satellite coordinates in the local tangential coordinate system may be obtained by projecting the station-satellite vector $r _ { \mathrm { e f } } - R _ { \mathrm { e f } }$ in the Earth-fixed system onto the axes $e _ { \mathrm { E } } , e _ { \mathrm { N } }$ , and $e _ { Z }$ :

$$
s \ = \ \left( \begin{array} { l } { s _ { \mathrm { E } } } \\ { s _ { \mathrm { N } } } \\ { s _ { \mathrm { Z } } } \end{array} \right) \ = \ E \left( r _ { \mathrm { e f } } - R _ { \mathrm { e f } } \right) .
$$

Here

$$
E ~ = ~ \left( { \begin{array} { c } { e _ { \mathrm { E } } ^ { T } } \\ { e _ { \mathrm { N } } ^ { T } } \\ { e _ { \mathrm { Z } } ^ { T } } \end{array} } \right) ~ = ~ \left( { \begin{array} { c c c } { - \sin \lambda } & { + \cos \lambda } & { 0 } \\ { - \sin \varphi \cos \lambda } & { - \sin \varphi \sin \lambda } & { + \cos \varphi } \\ { + \cos \varphi \cos \lambda } & { + \cos \varphi \sin \lambda } & { + \sin \varphi } \end{array} } \right)
$$

is an orthonormal matrix made up by the east, north, and zenith unit vectors. However, because the Cartesian coordinates cannot be measured directly by tracking radars, spherical coordinates are frequently employed to specify the satellite position in local tangential or horizontal coordinates.

![](images/15b47809c0126e2a14b34d7c2f3d52eb85779f45a2f4086b1eae8bd7de197bca.jpg)  
Fig. 6.8. Definition of azimuth and elevation

The most common spherical coordinates are known as azimuth and elevation. The azimuth angle $A$ measures the longitude in the horizontal plane and is counted positively from north to east as illustrated in Fig. 6.8. The elevation angle $E$ specifies the latitude above the horizontal plane and is measured positively to the zenith. The mutual conversion between the Cartesian and spherical coordinates is provided by the relations

$$
{ \binom { s _ { \mathrm { E } } } { s _ { \mathrm { N } } } } = { \binom { \sin A \cos E } { \cos A \cos E } }
$$

and

$$
A = \arctan \left( { \frac { s _ { \mathrm { { E } } } } { s _ { \mathrm { { N } } } } } \right) \quad \quad E = \arctan \left( { \frac { s _ { \mathrm { { Z } } } } { \sqrt { s _ { \mathrm { { E } } } ^ { 2 } + s _ { \mathrm { { N } } } ^ { 2 } } } } \right) \quad .
$$

![](images/676fe3bdfab8a16fb5c81075ecd37dc511ec9706637de6562fa8251011227e7f.jpg)  
Fig. 6.9. Definition of X-Y-angles for north-south antenna mount type (left) and east-west antenna mount (right)

Alternatively X-Y-angles are sometimes used that differ from azimuth and elevation by the choice of a reference plane at right angles to the horizon (cf. Fig. 6.9):

$$
X _ { \mathrm { N S } } = \arctan \left( \frac { s _ { \mathrm { E } } } { s _ { \mathrm { Z } } } \right) \qquad Y _ { \mathrm { N S } } = \arctan \left( \frac { s _ { \mathrm { N } } } { \sqrt { s _ { \mathrm { E } } ^ { 2 } + s _ { \mathrm { Z } } ^ { 2 } } } \right)
$$

and

$$
X _ { \mathrm { E W } } = \arctan \left( \frac { - s _ { \mathrm { N } } } { s _ { \mathrm { Z } } } \right) Y _ { \mathrm { E W } } = \arctan \left( \frac { s _ { \mathrm { E } } } { \sqrt { s _ { \mathrm { N } } ^ { 2 } + s _ { \mathrm { Z } } ^ { 2 } } } \right) .
$$

Both $X \mathrm { - }$ and Y-angles are less than $9 0 ^ { \circ } \left( \pi / 2 \right)$ by magnitude for all points above the horizon.

# 6.2.3 Range Measurements

# Round-trip Light Time

Two-way radar and laser ranging comprises the signal uplink from the ground station to the satellite and the downlink from the satellite to the ground station. When a two-way range measurements has been recorded at the ground station at time $t$ , the signal has been received and transmitted back by the satellite at $t - \tau _ { \mathrm { d } }$ , where $\tau _ { \mathrm { d } }$ is the downlink light travel time. The transmission time of the signal at the ground station is thus given by $t - \tau _ { \mathrm { d } } - \tau _ { \mathrm { u } }$ , where $\tau _ { \mathrm { u } }$ is the uplink light travel time.

Therefore, the modeling of range measurements requires the iterative solutions of two light-time equations for the downlink and the uplink path (cf. Fig. 6.10). The algorithm for the downlink light-time computation was described in (6.22) and (6.23) as part of the angle measurement modeling. For the uplink the light time is given by the implicit equation

$$
c \tau _ { \mathrm { u } } = \vert { \boldsymbol { r } } ( t - \tau _ { \mathrm { d } } ) - { \boldsymbol { R } } ( t - \tau _ { \mathrm { d } } - \tau _ { \mathrm { u } } ) \vert \quad .
$$

A fixed-point iteration for the uplink with

$$
\tau _ { \mathrm { u } } ^ { ( i + 1 ) } = 1 / c \cdot | \pmb { r } ( t - \tau _ { \mathrm { d } } ) - \pmb { R } ( t - \tau _ { \mathrm { d } } - \tau _ { \mathrm { u } } ^ { ( i ) } ) |
$$

is performed until successive values of $\tau _ { \mathrm { u } }$ agree to better than a certain threshold, e.g. $1 0 ^ { - 7 } \mathrm { s } .$ . It requires one iteration step less than for the downlink, since an initial value of τ (0) u $\tau _ { \mathrm { u } } ^ { ( 0 ) } = \tau _ { \mathrm { d } }$ can be applied. In addition, the light-time correction to the uplink is a factor of about 20–30 smaller than for the downlink, due to the ratio of the inertial ground station velocity and the inertial velocity of the satellite.

The two-way range measurement $\rho$ is then modeled from the average of the uplink and downlink range $\rho _ { \mathrm { u } }$ and $\rho _ { \mathrm { d } }$ , according to

$$
\rho = { \frac { 1 } { 2 } } ( \rho _ { \mathrm { u } } + \rho _ { \mathrm { d } } ) = { \frac { 1 } { 2 c } } ( \tau _ { \mathrm { u } } + \tau _ { \mathrm { d } } ) ~ .
$$

As can be shown by a first-order Taylor expansion the two-way range is almost identical to the geometric distance between the station and the satellite at time $t - \tau / 2$ . The total light-time correction for two-way range measurements is therefore given by $1 / 2 \tau \dot { \rho }$ . Thus the typical light-time correction is at most ${ 8 0 } \mathrm { m }$ for low-Earth orbiting satellites.

![](images/2cfde3e981acc07d6d36d15bf6cc769fcbd44b2188a3a5bcf4118c12b1681c62.jpg)  
Fig. 6.10. The motion of the satellite and the ground station during the signal travel time for two-way range measurements

Transponder Delay and Ambiguity Resolution

Up to now, it has been assumed that the satellite instantaneously retransmits the received range signal to the ground station. Actually, the satellite transponder delays the ranging signal and thus leads to an artificial increase of the range measurement that has to be corrected for in the orbit determination process. A typical value for an S-band transponder is 3000 ns, equivalent to a $4 5 0 \mathrm { m }$ range bias. High-precision range modeling has to account for the transponder delay variation with the signal frequency, the temperature at the satellite, and the signal strength. However, typical variations are of the order of a few nanoseconds that can be neglected for most applications.

In addition, corrections depending on the ground station hardware have to be applied. First, a geometrical reduction of the measurement to a common antenna reference point has to be applied. If the two antenna axes do not intersect this correction is not a constant, but depends on the orientation of the antenna. This is e.g. the case for X-Y-antenna mounts for which an additional (Moyer 1971) correction

$$
\varDelta \rho = - b \cos Y
$$

has to be applied that depends on the Y-angle at the time of the measurement. Here $b$ is the antenna axis offset with typical values of $1 { - } 1 0 \mathrm { m }$ .

Secondly, the propagation delay in the ranging equipment and the electronic link to the antenna equipment has to be considered. This delay varies slightly with time, for example due to changing meteorological conditions at the ground station. Therefore, a range calibration prior to the satellite pass is performed in a so-called closed-loop configuration. Typical range calibration values are in the order of several thousand nanoseconds.

Depending on the ranging method, the collected range value is ambiguous by a certain value $a$ . For a tone ranging system with a lowest frequency of $8 \ \mathrm { H z }$ the respective one-way ambiguity is $1 8 7 5 0 \mathrm { k m }$ . Other ranging systems may even provide range data with a varying ambiguity. The ambiguity resolution requires a priori knowledge of the satellite position to compute the expected range $\rho$ with an accuracy of better than the ambiguity value. The integer ambiguity $n$ is then computed from minimizing the expression $\lvert \rho - n a \rvert$ .

Since the satellite reception and transmission antennas are not located at the center of mass of the satellite, a corresponding correction has to be applied for highprecision range modeling. An adequate knowledge of the instantaneous attitude is necessary to compute the inertial antenna location with respect to the satellite’s center of mass.

# Multiple Ranging Links

The principle of two-way ranging may be generalized to arbitrary links with spaceborne as well as ground-based transmitters and receivers. An example is the fourway ranging of the geostationary satellite Meteosat, where ranging signals are broadcast from the Primary Ground Station (PGS) at Fucino, Italy, to the satellite. The satellite retransmits the signals to a land-based transponder (LBT), an unattended ground station near Kourou, French Guiana, that transponds the signals via the satellite back to the PGS for reception and range measurement recording (EUMETSAT 1999).

Another example is described in Chap. 6.1 and illustrated in Fig. 6.2, where TDRS four-way ranging measurements are initiated by sending a ranging signal to one of the geostationary relay satellites. From here it is forwarded to the user spacecraft, retransmitted and linked back to the ground station after passing the relay satellite a second time.

In each particular ranging configuration the light-time equations for the individual signal paths is formulated and solved along the principles described before. The case of TDRS four-way ranging is furthermore addressed in (9.23).

# 6.2.4 Doppler Measurements

# Two-Way Range Rate

Two-way Doppler measurements are obtained from the integration of Doppler counts over a count-time interval $t _ { c }$ . The measured range rate may be modeled as the difference of the two-way ranges at the end and at the beginning of the counttime interval. Thus a total of four light-time iterations is required for the modeling of a single average range rate measurement (cf. Fig. 6.11). When the Doppler measurement time tag $t$ refers to the end of the count interval $t _ { 2 }$ , the associated carrier signal was transponded by the satellite at $t _ { 2 } - \tau _ { \mathrm { 2 u } }$ and transmitted by the ground station at time $t _ { 2 } - \tau _ { 2 \mathrm { u } } - \tau _ { 2 \mathrm { d } }$ . Similarly, the signal at count interval start $t _ { 1 } = t _ { 2 } - t _ { c }$ was transponded at the satellite at time $t _ { 1 } - \tau _ { \mathrm { l u } }$ and broadcast from the ground station at time $t _ { 1 } - \tau _ { \mathrm { l u } } - \tau _ { \mathrm { l d } }$ . Thus the average range rate measurement may be modeled as

$$
\bar { \dot { \rho } } ( t ) = \frac { c } { 2 } \frac { ( \tau _ { 2 \mathrm { u } } + \tau _ { 2 \mathrm { d } } ) - ( \tau _ { 1 \mathrm { u } } + \tau _ { 1 \mathrm { d } } ) } { t _ { c } } = \frac { 1 } { 2 } \frac { ( \rho _ { 2 \mathrm { u } } + \rho _ { 2 \mathrm { d } } ) - ( \rho _ { 1 \mathrm { u } } + \rho _ { 1 \mathrm { d } } ) } { t _ { c } } ,
$$

where the $\rho _ { i } ~ = ~ c \tau _ { i }$ denote the individual one-way ranges involved. For threeway Doppler measurements, where the signal is transmitted from a ground station, transponded by the satellite, and received at a different ground station, the model is accordingly applicable.

![](images/2384fe25a7e12ce7d8c768a8b0ab09e0c754702d856c9f5f7642aba80c91e69c.jpg)  
Fig. 6.11. The motion of the satellite and the ground station during signal travel time for two-way Doppler measurements

# One-Way Range Rate

The model for one-way Doppler measurements is easily derived from the two-way range rate model. Here the carrier signal is transmitted from the ground to the satellite (DORIS) or from satellite to the ground. Considering a measurement with time tag $t$ that refers to the end of the count interval $t _ { 2 }$ , the signal transmission time is $t _ { 2 } - \tau _ { 2 }$ . The beginning of the count interval is then $t _ { 1 } = t _ { 2 } - t _ { c }$ and the associated transmission time is $t _ { 1 } - \tau _ { 1 }$ . Hence, the one-way range rate model is

$$
\bar { \dot { \rho } } = c \frac { ( \tau _ { 2 } - \tau _ { 1 } ) } { t _ { c } } = \frac { ( \rho _ { 2 } - \rho _ { 1 } ) } { t _ { c } } .
$$

It is noted that in contrast to two-way Doppler measurements, one-way Doppler measurements require precise frequency standards both at the transmitter and at the receiver. Nonetheless, the frequency difference of the transmitter and the receiver should be estimated as part of the orbit determination.

# Rotational Doppler Bias

A spinning spacecraft exhibits a modulation of the two-way Doppler shift due to the rotational motion of the spacecraft antenna onto the direction vector from the satellite to the ground station. Following Kallemeyn & Vaughan (1996) the average range rate during the count interval is changed by

$$
\delta \bar { \dot { \rho } } = \frac { 1 } { t _ { c } } \int _ { t - t _ { c } } ^ { t } d \cdot \omega \sin \alpha \sin ( \omega t ) d t \quad .
$$

Here $d$ is the distance of the spin axis to the electric antenna center, $\omega$ is the satellite’s angular velocity, and $\alpha$ is the angle between the spin axis and the direction to the ground station. In addition to the periodic Doppler modulation, a rotational Doppler bias is also present for circular polarized signals. To understand the principle of this bias, a satellite antenna is considered which rotates in a right-hand sense about the positive $z$ -axis of the antenna zenith. As the antenna emits a right-hand circular polarized wave along the positive $z$ -axis the transmission frequency is increased by the spin rate of the antenna. If the antenna emits a left-hand circular polarized signal along the positive $z$ -axis, the transmitted frequency is decreased by the spin rate of the satellite. Spinning satellites cause such frequency shifts both at the reception and at the transmission of the signal. According to Marini (1970) this frequency shift introduces a bias

$$
\Delta \bar { \dot { \rho } } = \frac { \lambda \omega } { 2 \pi } \frac { s _ { \mathrm { R } } + s _ { \mathrm { T } } / T _ { 1 , 2 } } { 2 }
$$

to the range rate measurements, where $\lambda$ is the signal wavelength, $T _ { 1 , 2 }$ is the transponder turn-around ratio and $s _ { \mathrm { R } }$ and $s _ { \mathrm { T } }$ denote the signs of the frequency shift on reception and transmission, respectively. Considering a satellite spinning at two revolutions per second and a satellite antenna with the same polarization for transmission and reception (i.e. $s _ { \mathrm { T } } = s _ { \mathrm { R } }$ ), the rotational Doppler bias is $2 8 \mathrm { c m } / \mathrm { s }$ in the S-band.

# 6.2.5 GPS Measurements

Pseudorange and Carrier Phase Measurements

As introduced in (6.1.3), GPS pseudorange measurements are obtained from the difference of the reception and transmission time of a ranging signal emitted by the GPS satellite. Taking into account the offsets of the receiver and transmitter clocks from GPS system time but ignoring atmospheric path delays as well as measurement errors, the pseudorange for a receiving antenna at position $r _ { r }$ at GPS time $t$ is described by the relation

$$
\rho _ { \phi } ( t ) = | { \pmb r } _ { r } ( t ) - { \pmb r } _ { t } ( t - \tau ) | + c ( \delta t _ { r } - \delta t _ { t } ) \quad .
$$

Here, $r _ { t }$ denotes the position of the GPS satellite and can be computed from the GPS navigation message (see Annex A.2) or interpolated from publicly available precise ephemeris products. The signal travel time $\tau$ from the GPS satellite to the receiver is obtained from an iterative solution of the light-time equation

$$
\tau ^ { ( i + 1 ) } = \frac { 1 } { c } | \pmb { r } _ { r } ( t ) - \pmb { r } _ { t } ( t - \tau ^ { ( i ) } ) |
$$

with $\tau ^ { ( 0 ) } = 0$ as a starting value. At representative distances of $1 9 , 0 0 0 { - } 2 5 , 0 0 0 { \mathrm { k m } }$ , the light time amounts to about 65-85 ms and a single iteration is typically enough for the observation modeling. Care must be taken, though, when describing the motion of the GPS satellite and the receiver in an Earth-fixed coordinate system, as it is common practice in terrestrial GPS navigation. In this case, $\boldsymbol { r } _ { t } ( t - \tau )$ in (6.41) and (6.42) must be replaced by $\pmb { R } ( \omega _ { \oplus } \tau ) \pmb { r } _ { t } ( t - \tau )$ to express the GPS satellite position and the receiver position in a consistent reference system (namely the Earth-fixed system at signal reception time $t$ ) prior to computing their difference.

Along with the orbit information of the GPS satellite, the broadcast ephemeris message also provides a second-order polynomial approximation for the satellite clock offset with respect to GPS system time. Based on the coefficients $a _ { f 0 } , a _ { f 1 }$ , and $a _ { f 2 }$ , the satellite clock offset

$$
\delta t _ { t } ( t ) = a _ { f 0 } + a _ { f 1 } ( t - t _ { c } ) + a _ { f 2 } ( t - t _ { c } ) ^ { 2 }
$$

can be predicted for any time $t$ within several hours of the reference epoch $t _ { c }$ . However, the resulting expression refers to the proper time of the clock and a supplementary correction

$$
\delta t _ { t , \mathrm { r e l } } ( t ) = - \frac { 2 } { c ^ { 2 } } ( \pmb { r } _ { t } ^ { T } \pmb { v } _ { t } )
$$

must be added to account for periodic relativistic effects in the observed clock. These depend on the position $r _ { t }$ and velocity ${ \boldsymbol { v } } _ { t }$ of the GPS satellite and vanish for rigorously circular orbits.

Other than the GPS satellite clock offset, the clock offset $\delta t _ { r } ( t )$ of the receiver clock represents an unknown quantity in the measurement model and must be estimated within the orbit determination program along with the motion of the user satellite.

In analogy with (6.41), the integrated carrier phase measurement may be modeled as

$$
\rho _ { \phi } ( t ) = | { \boldsymbol r } _ { r } ( t ) - { \boldsymbol r } _ { t } ( t - \tau ) | + c ( \delta t _ { r } - \delta t _ { t } ) + \lambda N ~ .
$$

The ambiguity $\lambda N$ is not known beforehand, but remains constant throughout continuous carrier tracking arcs. A coarse estimate of the ambiguity can be obtained from the difference of pseudorange and carrier phase measurements but the actual value must be adjusted in the orbit determination process along with other unknown parameters. Despite this added complexity, carrier phase measurements are preferred to pseudorange observations for precise positioning due their notably smaller measurement noise and multipath effects.

# Navigation Solution

The navigation solutions $( x , y , z )$ provided by the GPS receiver are not measurements in a rigorous sense, since they are actually derived from raw pseudorange measurements. Nevertheless, navigation solutions may in practice be applied as pseudo-measurements for satellite orbit determination (Carter et al. 1995, Gill 1997). The need for processing navigation solutions within an orbit determination software, instead of using the solutions itself, may arise for various reasons. Most notably the use of a dynamic model allows the smoothing of SA-effects, the detection of outliers, and the bridging of gaps without GPS measurements. Furthermore a dynamic filtering of the position solution can be used to obtain reliable velocity information. This is important, because the receiver-provided velocity solutions exhibit typical errors of $1 ~ \mathrm { m / s }$ , which prevents their use in orbit predictions. An inherent advantage of using navigation solutions instead of pseudoranges is their simple measurement modeling. As the user satellite orbit may be integrated in a mean-of-date reference system, the measurement modeling just requires the transformation from the mean-of-date system to the WGS84 coordinate system, where the navigation solution vector is given by

$$
r _ { \mathrm { W G S } } = \pi \Theta N r _ { \mathrm { m o d } } .
$$

Thus, any knowledge of the GPS satellite ephemerides is avoided as well as the need for light-time iterations. This renders the use of navigation solutions especially interesting for spaceborne applications.

# 6.3 Media Corrections

# 6.3.1 Interaction of Radiation and Atmosphere

Electromagnetic signals that are transmitted from a spacecraft traverse the Earth’s atmosphere before they are received by a ground station. As the signals propagate, the electromagnetic radiation interacts with the electrons, ions, atoms, and molecules constituting the Earth’s plasma environment and atmosphere to a various extent. As a consequence, the signals undergo a change of direction, known as refractive bending, and a change of the velocity of propagation. In addition, the atmosphere affects the signal polarization and field strength.

The velocity of propagation and the wavelength of electromagnetic waves depend on the refractive index $n$ of the surrounding medium. Given the vacuum wavelength $\lambda$ and speed of light $c$ , the corresponding values $\lambda _ { n }$ and $c _ { n }$ in a medium of refractive index $n$ are related by the expression

$$
n = { \frac { c } { c _ { n } } } = { \frac { \lambda } { \lambda _ { n } } } .
$$

As the refractive index of the Earth’s atmosphere deviates only slightly from unity the refractivity

$$
N = ( n - 1 ) 1 0 ^ { 6 }
$$

is introduced. The refractive index depends on the material properties of the medium, especially the dielectric constant, the permeability, and the conductivity. In the sequel different models of the refractive index will be discussed for the troposphere, which is composed of neutral gas, and the ionosphere, which is made up of a plasma of charged particles.

![](images/a8a0d95718743d28add3d16395a3a91c4250d934fb6e6edccd43e5840a9ffc22.jpg)  
Fig. 6.12. Atmospheric refraction

Irrespective of the detailed physical properties, the basic impact of the atmospheric refraction on the propagation of electromagnetic signals may be understood by considering the simplified model of a plane atmosphere with constant refractivity (Fig. 6.12). Based on Snellius’s law a signal entering the atmosphere at a zenith distance $z _ { 0 }$ , traverses the atmosphere at a smaller angle $z$ , which is given by the relation

$$
n \sin z = \sin z _ { 0 } .
$$

Upon substitution of the elevation $E = 9 0 ^ { \circ } - z$ and expansion in $\varDelta E = E - E _ { 0 }$ one obtains the expression

$$
\varDelta E = ( n - 1 ) \frac { 1 } { \tan E _ { 0 } }
$$

for the bending angle, where $n - 1$ is of the order of $3 { \cdot } 1 0 ^ { - 4 }$ rad or one arcminute for the troposphere.

Aside from the signal bending the reception time of a ranging signal is delayed due to the reduced velocity inside the atmosphere (assuming $n > 1$ ). From Fig. 6.12 the time required to traverse a layer of height $h$ is given by $\tau = n h / ( c \sin E )$ . The corresponding vacuum value would be obtained from $n = 1$ and $E = E _ { 0 }$ .

Neglecting the small bending angle, the difference between the two values may be expressed as a range difference

$$
\varDelta \rho = h ( n - 1 ) \frac { 1 } { \sin E _ { 0 } } .
$$

The measured range value is thus larger than the one that would be obtained in the absence of an atmosphere.

For the modeling of ionospheric refraction it is necessary to distinguish between the refractive index $n _ { \mathrm { p h } }$ of a single electromagnetic wave (e.g. the carrier phase) and the refractive index $n _ { \mathrm { g r } }$ of wave groups (e.g. ranging signals). This is due to the fact that the refractive index depends on the frequency $f$ of the respective waves in a dispersive medium like a plasma of charged particples. For a signal composed of different harmonic frequencies the resulting wave group propagates at the group velocity $c _ { \mathrm { g r } } = c / n _ { \mathrm { g r } }$ where

$$
n _ { \mathrm { g r } } = n _ { \mathrm { p h } } + f \frac { d n _ { \mathrm { p h } } } { d f }
$$

is the group refractive index. The resulting group velocity is always smaller than the vacuum speed of light $c$ . In contrast to this the phase velocity $\dot { c } _ { \mathrm { p h } } = c ^ { 2 } / c _ { \mathrm { g r } }$ is larger than $c$ for dispersive media. For non-dispersive media like the troposphere both refractive indices are equal as are the group and phase velocity $c _ { n } = c / n < c$ .

# 6.3.2 Tropospheric Refraction

The troposphere, composed almost totally of neutral gas, is the lower atmosphere extending from sea surface level to approximately $4 2 \ \mathrm { k m }$ . The extension of the different troposphere layers depends essentially on the temperature and the vertical temperature gradient. The troposphere is a non-dispersive medium for radio waves, hence the refractive index does not depend on the radiation frequency. The propagation of electromagnetic waves through the troposphere is mainly affected by the temperature $T$ , the atmospheric pressure $p$ , and the partial pressure of water vapor $e$ . An empirical expression for radio frequencies below $3 0 0 \mathrm { G H z }$ relates these parameters to the dry component

$$
N _ { 1 } = 7 7 . 6 2 4 \cdot p [ \mathrm { h P a } ] / T [ \mathrm { K } ]
$$

and the wet component

$$
N _ { 2 } = 3 7 1 9 0 0 { \frac { e [ \mathrm { h P a } ] } { ( T [ \mathrm { K } ] ) ^ { 2 } } } - 1 2 . 9 2 { \frac { e [ \mathrm { h P a } ] } { T [ \mathrm { K } ] } }
$$

of the refractivity $N = N _ { 1 } + N _ { 2 }$ (Goad & Goodman 1974). Since the tropospheric refractivity is positive, the tropospheric refractive index is always greater than one. Following Großkopf (1970) the partial pressure of water vapor, which is required

in the above equations, can be expressed as a function of the relative humidity of the air $f _ { h }$ $0 \leq f _ { h } \leq 1$ ) and the temperature $T _ { C }$ :

$$
e [ \mathrm { h P a } ] = 6 . 1 0 ~ f _ { h } \exp \left( \frac { 1 7 . 1 5 T _ { C } [ ^ { \circ } \mathrm { C } ] } { 2 3 4 . 7 + T _ { C } [ ^ { \circ } \mathrm { C } ] } \right) .
$$

The above expression for the radio refractive index is accurate to better than $1 \%$ . At sea surface level the refractivity for radio waves is about 320–380, whereas it is 282 for optical frequencies $( \lambda = 0 . 6 9 \mu \mathrm { m } )$ and standard atmospheric conditions (Jeske 1988). The tropospheric refractivity decreases with increasing altitude and approaches zero at the upper tropospheric boundary.

As shown above, the tropospheric refraction is composed of the refraction due to dry air and a contribution due to water vapor, which is denoted as wet term. Dry air contributions are dominant and can be modeled reasonably well. The contribution from water vapor amounts to about $10 \%$ and can be modeled only poorly due to the high temporal, horizontal, and altitude variations. In principle, two different approaches can be adopted to determine the wet troposphere refraction

# Modeling of the wet refraction contribution

The water vapor contributions may be modeled using theoretical considerations and observation data obtained from radio probes launched with sounding rockets. However, as continuous observation data are not available, the models have a limited validity and, moreover, imply a considerable expense and effort.

# • Measurement of the water vapor

Water-vapor measurements may be collected either from an infrared hydrometer or a water-vapor radiometer. Both techniques suffer from technical problems of calibrating the amount of wet water due to clouds or rain. Furthermore, considerable expenses are implied in the case of the radiometer.

A variety of refraction correction models for spacecraft tracking data has been established in the past, ranging from simple exponential formulas to sophisticated and numerically expensive algorithms that account for the light-path curvature in the atmosphere by applying ray-tracing methods. In Table 6.4 the refraction corrections for radar range and elevation data are given, as derived from the elaborate Hopfield-Goad model for representative meteorological conditions.

Table 6.4. Tropospheric refraction for $p = 9 3 8 \mathrm { h P a }$ , $T = 2 8 6 { \mathrm { K } }$ , and $f _ { h } = 0 . 7 3$   

<table><tr><td>E(）</td><td>1</td><td>3</td><td>5</td><td>7</td><td>10</td><td>15</td><td>20</td><td>30</td><td>40</td><td>50</td><td>70</td><td>90</td></tr><tr><td>△E(&quot;)</td><td>1358</td><td>836</td><td>589</td><td>449</td><td>328</td><td>222</td><td>166</td><td>106</td><td>73</td><td>52</td><td>23</td><td>0</td></tr><tr><td>△p(m)</td><td>58</td><td>34</td><td>23</td><td>17</td><td>13</td><td>9</td><td>7</td><td>5</td><td>4</td><td>3</td><td>2</td><td>2</td></tr></table>

As shown above a simple model for the tropospheric refraction of radar range and elevation measurements is given by

$$
\varDelta E = N \mathrm { ~ 1 0 ^ { - 6 } } \frac { 1 } { \tan E } \mathrm { ~ [ r a d ] }
$$

and

$$
\varDelta \rho = N 1 0 ^ { - 6 } h \frac { 1 } { \sin E } \quad ,
$$

where $h$ denotes the effective scale height of the troposphere. The scale height is about $7 . 5 \mathrm { k m }$ at sea level and may be computed from the Hopfield two-quartic model

$$
h = \frac { 1 } { 5 } h _ { d } - \frac { 1 } { 5 } \frac { N _ { 2 } } { N } ( h _ { d } - h _ { w } )
$$

(Hopfield 1969). Here the first term denotes the contribution from dry air and the second term gives the wet contributions. The top of the dry troposphere may be computed from $h _ { d } = 1 4 8 . 9 8 ( T - 4 . 1 2 ) \mathrm { m }$ (Black 1978), while the top of the wet troposphere is $h _ { w } = 1 2 \mathrm { k m }$ .

The above model yields an error of less than $10 \%$ for elevations above $5 ^ { \circ }$ . This renders the model attractive for many applications, in particular if no meteorological parameters are available that justify the use of more elaborate models. It should be noted, however, that errors up to $100 \%$ may arise at elevations of $1 ^ { \circ }$ .

A general and accurate tropospheric refraction model is the Hopfield model, modified by Goad to use the Saastamoinen zenith range correction (Goad & Goodman 1974). It is applicable both to radar data as well as to optical observations. In the Hopfield model, the dry troposphere height $h _ { 1 }$ is determined from

$$
h _ { 1 } [ \mathrm { m } ] = \frac { 5 . 0 \cdot 0 . 0 0 2 2 7 7 } { N _ { 1 } \cdot 1 0 ^ { - 6 } } \ p [ \mathrm { h P a } ] ,
$$

while the wet troposphere height $h _ { 2 }$ is given by

$$
h _ { 2 } [ \mathrm { m } ] = \frac { 5 . 0 \cdot 0 . 0 0 2 2 7 7 } { N _ { 2 } \cdot 1 0 ^ { - 6 } } \left[ \frac { 1 2 5 5 } { T [ \mathrm { K } ] } + 0 . 0 5 \right] ~ e [ \mathrm { h P a } ] ~ .
$$

The tropospheric range correction for the Hopfield model is given by a ninthorder polynomial

$$
\Delta \rho = C _ { \rho } \sum _ { j = 1 } ^ { 2 } \frac { N _ { j } } { 1 0 ^ { 6 } } \sum _ { i = 1 } ^ { 9 } \frac { \alpha _ { i j } r _ { j } ^ { i } } { i } ,
$$

where the constant

$$
C _ { \rho } = \left[ { \frac { 1 7 0 . 2 6 4 9 } { 1 7 3 . 3 - 1 / \lambda ^ { \prime 2 } } } \right] \left[ { \frac { 7 7 8 . 8 8 2 8 } { 7 7 . 6 2 4 } } \right] \left[ { \frac { 1 7 3 . 3 + 1 / \lambda ^ { \prime 2 } } { 1 7 3 . 3 - 1 / \lambda ^ { \prime 2 } } } \right]
$$

is approximately one for radio frequencies. The dimensionless signal wavelength $\lambda ^ { \prime } = \lambda / ( 1 \mu \mathrm { m } )$ and thus the term $1 / { \lambda ^ { \prime } } ^ { 2 }$ can be set to zero for radio frequencies. The distance to the top of the dry $( j = 1 )$ ) and wet $( j = 2 )$ ) troposphere is

$$
r _ { j } = \sqrt { ( R _ { \oplus } + h _ { j } ) ^ { 2 } - ( R _ { \oplus } \cos E ) ^ { 2 } } - R _ { \oplus } \sin E \quad .
$$

The coefficients of the polynomial are defined as

$$
\begin{array} { r c l } { { \alpha _ { 1 j } } } & { { = } } & { { 1 } } \\ { { \alpha _ { 2 j } } } & { { = } } & { { 4 \alpha _ { j } } } \\ { { \alpha _ { 3 j } } } & { { = } } & { { 6 \alpha _ { j } ^ { 2 } + 4 b _ { j } } } \\ { { \alpha _ { 4 j } } } & { { = } } & { { 4 \alpha _ { j } ( \alpha _ { j } ^ { 2 } + 3 b _ { j } ) } } \\ { { \alpha _ { 5 j } } } & { { = } } & { { a _ { j } ^ { 4 } + 1 2 a _ { j } ^ { 2 } b _ { j } + 6 b _ { j } ^ { 2 } } } \\ { { \alpha _ { 6 j } } } & { { = } } & { { 4 \alpha _ { j } b _ { j } ( a _ { j } ^ { 2 } + 3 b _ { j } ) } } \\ { { \alpha _ { 7 j } } } & { { = } } & { { b _ { j } ^ { 2 } ( 6 a _ { j } ^ { 2 } + 4 b _ { j } ) } } \\ { { \alpha _ { 8 j } } } & { { = } } & { { 4 \alpha _ { j } b _ { j } ^ { 3 } } } \\ { { \alpha _ { 9 j } } } & { { = } } & { { b _ { j } ^ { 4 } } } \end{array}
$$

with

$$
\begin{array}{c} \begin{array} { l } { { a _ { j } } } \end{array} = \begin{array} { l } { { \displaystyle - \sin E } } \\ { { \displaystyle h _ { j } } } \end{array}  \\ { { b _ { j } } } \end{array} = \begin{array} { l } { { \displaystyle - \cos ^ { 2 } E } } \\ { { \displaystyle 2 h _ { j } R _ { \oplus } } } \end{array} .
$$

The tropospheric correction of average range rate data is obtained from the correction of range data (Schmid & Lynn 1978). Hence, the range rate correction depends on the elevation angle as well as the elevation rate.

The tropospheric correction of the elevation angles according to the Hopfield model is

$$
\varDelta E = C _ { E } \frac { 4 \cos E } { \rho } \left[ \sum _ { j = 1 } ^ { 2 } \frac { N _ { j } } { 1 0 ^ { 6 } h _ { j } } \left\{ \sum _ { i = 1 } ^ { 7 } \left( \frac { \beta _ { i j } r _ { j } ^ { i + 1 } } { i ( i + 1 ) } + \frac { \beta _ { i j } r _ { j } ^ { i } } { i } \left( \rho - r _ { j } \right) \right) \right\} \right]
$$

where the constant $C _ { E }$

$$
C _ { E } = \left[ { \frac { 1 7 0 . 2 6 4 9 } { 1 7 3 . 3 - 1 / \lambda ^ { \prime 2 } } } \right] \left[ { \frac { 7 8 . 8 8 2 8 } { 7 7 . 6 2 4 } } \right]
$$

is approximately one for radio frequencies and $\rho$ is the range to the satellite. The elevation correction coefficients are computed from

$$
\begin{array} { r c l } { { \beta _ { 1 j } } } & { { = } } & { { 1 } } \\ { { } } & { { } } & { { } } \\ { { \beta _ { 2 j } } } & { { = } } & { { 3 a _ { j } } } \\ { { } } & { { } } & { { } } \\ { { \beta _ { 3 j } } } & { { = } } & { { 3 ( a _ { j } ^ { 2 } + b _ { j } ) } } \\ { { } } & { { } } & { { } } \\ { { \beta _ { 4 j } } } & { { = } } & { { a _ { j } ( a _ { j } ^ { 2 } + 6 b _ { j } ) } } \\ { { } } & { { } } & { { } } \\ { { \beta _ { 5 j } } } & { { = } } & { { 3 b _ { j } ( a _ { j } ^ { 2 } + b _ { j } ) } } \\ { { } } & { { } } & { { } } \\ { { \beta _ { 6 j } } } & { { = } } & { { 3 a _ { j } b _ { j } ^ { 2 } } } \\ { { } } & { { } } & { { } } \\ { { \beta _ { 7 j } } } & { { = } } & { { b _ { j } ^ { 3 } } } \end{array}
$$

For optical frequencies the above equations can be applied as well, when only the dry term is considered $N _ { 2 } = 0$ ). The azimuth measurements are not affected by refraction.

# 6.3.3 Ionospheric Refraction

From about $5 0 \mathrm { k m }$ up to a height of $1 0 0 0 \mathrm { k m }$ the ionosphere plays the major role for propagating electromagnetic waves. The abundance of ions and free electrons, resulting primarily from the absorption of solar ultraviolet radiation, is the cause of the ionospheric refraction. Due to small mass ratio of the electron and ion mass, free electrons play a more important role than ions. The electron density at $5 0 \mathrm { k m }$ altitude is about $1 0 ^ { 8 } \mathrm { e l e c t r o n s } / \mathrm { m } ^ { 3 }$ and increases with height due to the increasing intensity of the solar radiation. A maximum electron density of $1 0 ^ { 1 2 }$ electrons $/ \mathrm { m } ^ { 3 }$ near sunspot maxima can be found at about $3 0 0 \mathrm { k m }$ , decreasing towards higher altitudes due to the decreasing atmospheric density. Both photochemistry and transport processes contribute to the structure of the ionosphere, which is shown in Fig. 6.13. The electron density profile primarily depends on the altitude, the sunspot activity as well as day and night variations. Several regions can be identified that are designated as D region $( 6 0 { - } 9 0 \mathrm { k m } )$ , E region $( 1 0 5 { - } 1 6 0 \mathrm { k m } )$ and F region $1 6 0 { - } 1 0 0 0 \mathrm { k m } )$ . More detailed models distinguish further the F1 region ( $1 6 0 { - } 1 8 0 \mathrm { k m } )$ ) and the F2 region $( 2 0 0 { - } 1 0 0 0 \mathrm { k m } )$ . The D and F1 regions vanish at night, while the E region becomes considerably weaker and the F2 region shows a reduced marking.

![](images/6b70a7b553b60c56c1529ec1fc019e0c5e29c75b3a02379bdae436d5438bb27a.jpg)  
Fig. 6.13. Electron density profiles at mid-latitudes based on the International Reference Ionosphere IRI 1995 (Bilitza et al. 1993, 1995)

It is extremely difficult to construct global ionospheric models that accurately predict the electron density. Neglecting the perturbations due to ions, the contribution of the Earth’s magnetic field, and absorption effects, the ionospheric refractive indices are (Jeske 1988)

$$
n _ { \mathrm { p h } } = \sqrt { 1 - \frac { f _ { p } ^ { 2 } } { f ^ { 2 } } } \approx 1 - \frac { 1 } { 2 } \frac { f _ { p } ^ { 2 } } { f ^ { 2 } } ~ \mathrm { a n d } ~ n _ { \mathrm { g r } } \approx 1 + \frac { 1 } { 2 } \frac { f _ { p } ^ { 2 } } { f ^ { 2 } } ~ ,
$$

where

$$
f _ { p } = \frac { 1 } { 2 \pi } \sqrt { \frac { d _ { e } e _ { 0 } ^ { 2 } } { m _ { e } \epsilon _ { 0 } } }
$$

is the plasma frequency. Here, $d _ { e }$ denotes the electron number density, $e _ { 0 }$ the electron charge, $\epsilon _ { 0 }$ the vacuum dielectric constant, and $m _ { e }$ the electron mass. The plasma frequency varies from $1 0 \mathrm { M H z }$ ( $3 0 \mathrm { m }$ wavelength) by day to 3 MHz ( $[ 1 0 0 \mathrm { m }$ wavelength) at night and radio waves with longer wavelengths cannot penetrate the ionosphere. Inserting the constants yields the expression

$$
N _ { \mathrm { p h } } = - 4 0 . 3 \left[ \frac { \mathrm { m } ^ { 3 } } { \mathrm { s } ^ { 2 } } \right] \frac { d _ { e } } { f ^ { 2 } }
$$

for the ionospheric refractivity. As the refractivity is negative, the ionosphere exhibits a normal dispersion with a frequency dependence that is inverse to the square of the frequency. Thus, signals in the S-band frequency regime at $2 \ : \mathrm { G H z }$ are affected sixteen times more by ionospheric refraction than X-band frequency signals at $8 ~ \mathrm { G H z }$ . Furthermore, the described frequency dependence shows that optical signals are affected in a negligible manner by ionospheric refraction.

Table 6.5. Representative values of the ionospheric refraction for L-band signals $( 1 . 6 \mathrm { G H z } )$   

<table><tr><td>E（）</td><td>13571015203040507090</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>△E()</td><td></td><td>123117</td><td></td><td>1141018882 432310720</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>△p(m)</td><td>38</td><td>37</td><td>36</td><td>35</td><td>33</td><td>30</td><td>27</td><td>21</td><td>18</td><td>15</td><td>13</td><td>11</td></tr></table>

The ionospheric refraction leads to a reduction of the group velocity and an increase of the phase velocity. Since range measurements are based on timing measurements of wave groups the range correction due to the ionosphere is given as

$$
\varDelta \rho = \int _ { S } ^ { O } ( n _ { \mathrm { g r } } - 1 ) d s = + \frac { 4 0 . 3 } { f ^ { 2 } } \left[ \frac { \mathrm { m } ^ { 3 } } { \mathrm { s } ^ { 2 } } \right] \mathrm { T E C ~ } \ .
$$

Here the total electron content TEC along the signal path $s$ from the satellite $S$ to the observer $o$ is defined as

$$
\mathrm { T E C } = \int _ { S } ^ { O } d _ { e } ( s ) d s .
$$

It provides a measure of the ionospheric perturbation of radio waves and is given in units of $1 \mathrm { T E C U } = 1 \cdot 1 0 ^ { 1 6 } \mathrm { m } ^ { - 2 }$ . Carrier phase measurements depend on the phase velocity and experience a correction

$$
\frac { \varDelta \phi } { 2 \pi } \lambda = \int _ { S } ^ { O } ( n _ { \mathrm { p h } } - 1 ) d s = - \frac { 4 0 . 3 } { f ^ { 2 } } \left[ \frac { \mathrm { m } ^ { 3 } } { \mathrm { s } ^ { 2 } } \right] \mathrm { T E C }
$$

![](images/d775d249765762185d53d0326068fae890838ee94e84b4292734a9c0736be4ce.jpg)  
Fig. 6.14. Variation of the TEC with the time of the year and local time for a mid-latitude station based on the IRI 1995 model

which is opposite in sign to the range correction. Thus the measured radar range is increased when affected by the ionosphere, while the values of integrated carrier phase measurements are reduced.

Typical ionospheric effects on radar range and elevation data are listed in Table 6.5 for a transmission frequency of the GPS L1 carrier at $1 . 6 \ : \mathrm { G H z }$ . The variation of the total electron content in a zenith column for a mid-latitude station with local time and the date of the year is shown in Fig. 6.14.

As global ionospheric models do not, in general, provide the required modeling accuracy, the measurement of the total electron content is an adequate approach for determining the ionospheric refraction. Before the advent of the NAVSTAR GPS system, the Faraday rotation of linear polarized signals emitted from the user satellite or geostationary satellites was applied to determine the electron content along the signal path (Llewellyn et al. 1976). This technique, however, requires knowledge of the transmission characteristics of the satellite antenna as well as the satellite attitude. Another approach was to determine the change in the total electron content from building the Differenced Range Versus Integrated Doppler (DRVID). Since range measurements are determined by the group velocity and integrated Doppler counts by the phase velocity, both data types are affected in the same order but different sign (Radomski & Doll 1995). This technique has mainly been applied to correct the ionospheric and interplanetary plasma effects of deep-space probes.

As the ionospheric refraction depends on the signal frequency, the measurement of the signal delay or the signal frequency shift in two frequency bands allows the determination of the TEC value and the ionospheric measurement correction. This technique is applied for the DORIS system (2036 MHz and $4 0 1 \mathrm { M H z }$ ), the PRARE system $( 2 2 4 8 \mathrm { M H z }$ and ${ 8 4 8 9 } \mathrm { M H z }$ ) as well as for NAVSTAR GPS ( $1 5 7 5 \mathrm { M H z }$ and $1 2 2 8 ~ \mathrm { M H z }$ . The determination of ionospheric electron-density profiles from the

GPS Meteorology (GPS/MET) experiment aboard the MicroLab I satellite has been demonstrated by Hajj and Romans (1998). A GPS receiver for TEC determination may be collocated with a conventional single-frequency tracking system to provide the ionospheric refraction correction by interpolation of the TEC values along the directions to the GPS satellites at the direction to the user satellite. Alternatively, GPS-derived TEC observables from a worldwide network may be applied to derive global TEC information models, which enable ionospheric corrections for any user satellite (Feltens et al. 1997). Considering the GPS system, where pseudorange measurements $\rho _ { 1 }$ at the L1 frequency $f _ { 1 }$ and pseudoranges $\rho _ { 2 }$ at the L2 frequency $f _ { 2 }$ are available, the ionosphere-free pseudorange $\rho$ can be derived from (6.69) as

$$
\rho = { \frac { \rho _ { 2 } - ( f _ { 1 } / f _ { 2 } ) ^ { 2 } \rho _ { 1 } } { 1 - ( f _ { 1 } / f _ { 2 } ) ^ { 2 } } } \approx - 1 . 5 4 5 \rho _ { 2 } + 2 . 5 4 5 \rho _ { 1 } ~ .
$$

When precision accuracy requirements force the application of ionospheric corrections but measurements of the total electron content are not available, software models have to be applied that predict ionospheric properties either restricted to a dedicated ground station (local model) or worldwide (global model). In this case, models like the Penn state model (Nisbet 1974) that directly simulate the photochemical ionospheric reactions and processes are available as well as the empirical worldwide Bent model (Llewellyn et al. 1973). A recent development is the parameterized ionospheric model (PIM), which provides a near-real-time specification of the global ionosphere from near-real-time satellite and ground-based data (Daniell et al. 1995).

# Exercises

Exercise 6.1 (Light-Time Iteration) Solve the light-time equation for two-way range measurements of a polar satellite at $9 6 0 \mathrm { k m }$ altitude $( e = 0$ , $i = 9 7 ^ { \circ }$ , $\varOmega =$ $1 3 0 . 7 ^ { \circ } )$ and a ground station in central Europe $\lambda = + 1 1 ^ { \circ }$ East, $\varphi = + 4 8 ^ { \circ }$ ). The downleg (satellite to station) and upleg (station to satellite) light-time corrections are to be computed at $6 \mathrm { { m i n } }$ , $1 5 \mathrm { { m i n } }$ , and $2 4 \mathrm { m i n }$ past the passage of the ascending node, which is assumed to take place at $1 9 9 7 / 0 1 / 0 1 0 ^ { \mathrm { h } }$ UTC. The orbit propagation is to be based on Keplerian motion, neglecting precession and similar corrections in the reference system transformations.

Solution: The times of the light-time evaluation are close to the pass beginning, culmination, and end of the pass. To reach an accuracy level of $1 \mathrm { m m }$ , the downleg light-time iteration has to consider two iterations (I-1, I-2), while the upleg lighttime iteration may already be stopped after the first iteration:

<table><tr><td>UTC</td><td>Distance</td><td>Down I-1</td><td>Down I-2</td><td>Up I-1</td><td>Range</td></tr><tr><td>hh:mm:ss</td><td>[m]</td><td>[m]</td><td>[mm]</td><td>[m]</td><td>[m]</td></tr><tr><td>00:06:00.0</td><td>3644878.6</td><td>75.8</td><td>1.6</td><td>1.8</td><td>3644956.2</td></tr><tr><td>00:15:00.0</td><td>1167049.9</td><td>-6.4</td><td>0.0</td><td>0.5</td><td>1167044.0</td></tr><tr><td>00:24:00.0</td><td>4110978.7</td><td>-87.0</td><td>1.8</td><td>-0.7</td><td>4110891.0</td></tr></table>

Since the range and the amplitude of the range rate is largest at the beginning and end of the satellite pass, the range correction in the downleg is most pronounced near the rising and setting. As the light-time correction varies in proportion to the range rate, the correction vanishes near culmination (cf. Fig. 2.13) and changes its sign. The light-time corrections in the second iteration of the upleg (note the different units) are always positive due to their dependence on the rate of the relative velocity. The light-time correction in the upleg is small as compared to the downleg, since the inertial motion of the ground station due to the Earth rotation is smaller than the relative velocity of the satellite with respect to the station.

Exercise 6.2 (Range Rate Modeling) Compute the average two-way range rate measurements for the scenario described in Exercise 6.1. Assume a Doppler count interval $t _ { c }$ of 1 s and show that the average range rate measurement can be approximated by the instantaneous Doppler value at the middle of the count-time interval. The average and the instantaneous range rates as well as their differences are to be computed in steps of $3 \mathrm { m i n }$ .

Hint: The modeling of the average range rate measurement is described by (6.37), while the instantaneous range rate follows from

$$
\dot { d } _ { 0 } ( t ) = \frac { d _ { 0 } } { d _ { 0 } } \dot { d } _ { 0 } .
$$

Here, $\pmb { d } _ { 0 } = \pmb { r } ( t ) - \pmb { R } ( t )$ denotes the geometric distance of the satellite and the station at time $t$ .

Solution: In the limiting case of an infinite speed of light the average range rate can be approximated by the expression

$$
\bar { \dot { \rho } } ( t ) \approx \frac { 1 } { t _ { c } } \left( d _ { 0 } ( t ) - d _ { 0 } ( t - t _ { c } ) \right) \quad ,
$$

which follows from (6.37) by substitution of the geometric distance $d _ { 0 }$ for the twoway range $\rho$ . The right-hand side may further be expanded into a Taylor series around the center of the interval $[ t - t _ { c } , t ]$ , giving

$$
\frac { 1 } { t _ { c } } \left( d _ { 0 } ( t ) - d _ { 0 } ( t - t _ { c } ) \right) = \dot { d } _ { 0 } ( t - t _ { c } / 2 ) + \mathcal { O } ( t _ { c } ^ { 2 } \dddot { \rho } ) \enspace .
$$

Combining both approximations then shows the near-identity

$$
\bar { \dot { \rho } } ( t ) \approx \dot { d } _ { 0 } ( t - t _ { c } / 2 )
$$

of the measured average two-way range rate at time $t$ and the instantaneous range rate at the mid of the count interval. Applied to the example, the following numerical results are obtained:

<table><tr><td rowspan=1 colspan=1>UTC</td><td rowspan=1 colspan=3>(t）    do(t-tc/2)</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>hh:mm:ss</td><td rowspan=1 colspan=1>[m/s]</td><td rowspan=1 colspan=2>[m/s]</td><td rowspan=1 colspan=1>[m/s]</td></tr><tr><td rowspan=1 colspan=1>00:06:00.0</td><td rowspan=1 colspan=1>-6385.694</td><td rowspan=1 colspan=2>-6385.554</td><td rowspan=1 colspan=1>-0.140</td></tr><tr><td rowspan=1 colspan=1>00:09:00.0</td><td rowspan=1 colspan=1>-6113.312</td><td rowspan=1 colspan=2>-6113.161</td><td rowspan=1 colspan=1>-0.151</td></tr><tr><td rowspan=1 colspan=1>00:12:00.0</td><td rowspan=1 colspan=1>-4575.872</td><td rowspan=1 colspan=2>-4575.720</td><td rowspan=1 colspan=1>-0.153</td></tr><tr><td rowspan=1 colspan=1>00:15:00.0</td><td rowspan=1 colspan=1>1488.564</td><td rowspan=1 colspan=2>1488.732</td><td rowspan=1 colspan=1>-0.168</td></tr><tr><td rowspan=1 colspan=1>00:18:00.0</td><td rowspan=1 colspan=1>5500.474</td><td rowspan=1 colspan=1>5500.635</td><td></td><td rowspan=1 colspan=1>-0.161</td></tr><tr><td rowspan=1 colspan=1>00:21:00.0</td><td rowspan=1 colspan=1>6286.690</td><td rowspan=1 colspan=1>6286.839</td><td></td><td rowspan=1 colspan=1>-0.149</td></tr><tr><td rowspan=1 colspan=1>00:24:00.0</td><td rowspan=1 colspan=1>6392.679</td><td rowspan=1 colspan=1>6392.813</td><td></td><td rowspan=1 colspan=1>-0.134</td></tr></table>

Here, the Taylor expansion over the count interval contributes an error of less than $9 \mathrm { m m / s }$ to the overall approximation. The leading term resulting from the neglect of the light-time correction is given by $- ( \dot { \rho } ^ { 2 } + \rho \ddot { \rho } ) / c$ . In the present example this term is responsible for the dominant errors of $1 0 { - } 2 0 \mathrm { c m / s }$ . With a range rate measurement accuracy of $1 \mathrm { m m / s }$ it is obvious that both effects have to be modeled rigorously and that the instantaneous Doppler computation is inadequate for a precise range rate modeling.

Exercise 6.3 (User Clock Error from GPS Pseudorange) The user clock error of the GPS Rogue receiver at Goldstone is to be determined from pseudoranges of the PRN 1 GPS satellite. The PRN 1 position and clock errors at 1998/02/19 are taken from a precise ephemeris of the International GPS Service (IGS)   

<table><tr><td>GPS</td><td>XWGS</td><td>yWGS</td><td>ZWGS</td><td>8t</td></tr><tr><td>hh:mm:ss</td><td>[m]</td><td>[m]</td><td>[m]</td><td>[μs]</td></tr><tr><td>08:00:00.0</td><td>-15504.291797</td><td>-21530.763883</td><td>-1271.498273</td><td>40.018233</td></tr><tr><td>08:15:00.0</td><td>-15284.290679</td><td>-21684.703684</td><td>1573.435406</td><td>40.097295</td></tr><tr><td>08:30:00.0</td><td>-14871.711829</td><td>-21600.510259</td><td>4391.350089</td><td>40.028697</td></tr><tr><td>08:45:00.0</td><td>-14242.843546</td><td>-21306.712708</td><td>7133.948741</td><td>40.154941</td></tr><tr><td>09:00:00.0</td><td>-13380.818523</td><td>-20837.175663</td><td>9754.366309</td><td>40.193626</td></tr><tr><td>09:15:00.0</td><td>-12276.418004</td><td>-20229.688085</td><td>12207.953668</td><td>40.039288</td></tr><tr><td>09:30:00.0</td><td>-10928.585710</td><td>-19524.421024</td><td>14453.015617</td><td>40.012677</td></tr><tr><td>09:45:00.0</td><td>-9344.633744</td><td>-18762.314034</td><td>16451.492281</td><td>39.883106</td></tr><tr><td>10:00:00.0</td><td>-7540.134384</td><td>-17983.451817</td><td>18169.574686</td><td>40.181357</td></tr><tr><td>10:15:00.0</td><td>-5538.503062</td><td>-17225.491970</td><td>19578.246580</td><td>40.328261</td></tr><tr><td>10:30:00.0</td><td>-3370.289205</td><td>-16522.202377</td><td>20653.745961</td><td>40.039533</td></tr><tr><td>10:45:00.0</td><td>-1072.201838</td><td>-15902.162018</td><td>21377.940941</td><td>40.052642</td></tr><tr><td>11:00:00.0</td><td>1314.093678</td><td>-15387.672739</td><td>21738.615794</td><td>40.025493</td></tr></table>

To circumvent the effect of Selective Availability, the pseudoranges of PRN 1 are evaluated only at epochs where precise SP3 position and GPS clock errors are available. The pseudoranges on 1998/02/19 comprise the P code pseudoranges at the L2 frequency (P2) and the C/A code pseudoranges at the L1 frequency (C1):

<table><tr><td>GPS hh:mm:ss</td><td>P2 [m]</td><td>C1 [m]</td></tr><tr><td>08:30:00.0</td><td>21096577.475</td><td>21096579.501</td></tr><tr><td>09:00:00.0</td><td>20519964.850</td><td>20519966.875</td></tr><tr><td>09:30:00.0</td><td>20282706.954</td><td>20282709.233</td></tr><tr><td>10:00:00.0</td><td>20375838.496</td><td>20375840.613</td></tr><tr><td>10:30:00.0 11:00:00.0</td><td>20751678.769 21340055.129</td><td>20751680.997 21340057.362</td></tr></table>

The user clock error is to be determined from ionosphere-free pseudoranges derived from a suitable combination of P2 and C1. The signal travel time is to be determined from a rigorous iteration of the light-time equation that makes use of interpolated GPS positions. The WGS-84 coordinates of the receiver at Goldstone are

$$
X = - 2 3 5 3 . 6 1 4 1 2 8 \mathrm { k m } , \quad Y = - 4 6 4 1 . 3 8 5 4 4 7 \mathrm { k m } , \quad Z = + 3 6 7 6 . 9 7 6 5 0 1 \mathrm { k m } .
$$

Hint: The light-time iteration is usually performed in an inertial system with the station position vector $\pmb { R }$ and the satellite position vector $r$ . When $U$ denotes the transformation from the inertial to the Earth-fixed WGS84 system, the signal path is given by

$$
{ \pmb d } _ { \mathrm { W G S } } ( t ) = { \pmb U } ( t ) \left( { \pmb R } ( t ) - { \pmb r } ( t - \tau ) \right) \quad ,
$$

where $\tau$ denotes the signal travel time. Making use of the approximation

$$
U ( t ) \approx R _ { z } ( \omega _ { \oplus } \tau ) U ( t - \tau )
$$

the inertial position of the GPS satellite may be substituted by the corresponding Earth-fixed position

$$
r _ { \mathrm { W G S } } ( t - \tau ) = U ( t - \tau ) r ( t - \tau ) .
$$

This yields the light-time equation

$$
c \tau = d _ { \mathrm { W G S } } ( t ) = | R _ { z } ( \omega _ { \oplus } \tau ) r _ { \mathrm { W G S } } ( t - \tau ) - R _ { \mathrm { W G S } } |
$$

in the Earth-fixed reference frame, which is best suited for use with common tabular or analytical ephemerides of GPS satellites.

Solution: The residual of the ionosphere-free pseudorange yields the user clock bias, converted to meters, of the Goldstone GPS receiver at the time of the measurement. Over a time interval of $2 . 5 \mathrm { { h } }$ the clock drift can be neglected and the mean value of the residuals gives a clock bias of $1 7 6 7 4 . 7 7 \mathrm { m }$ . In particular the following pseudorange residuals and their deviations from the mean (Delta) are found:

<table><tr><td>GPS</td><td>ClockError</td><td>Delta</td></tr><tr><td>hh:mm:ss</td><td>[m]</td><td>[m]</td></tr><tr><td>08:30:00.0</td><td>17674.52</td><td>-0.25</td></tr><tr><td>09:00:00.0</td><td>17676.14</td><td>1.37</td></tr><tr><td>09:30:00.0</td><td>17675.59</td><td>0.82</td></tr><tr><td>10:00:00.0</td><td>17674.45</td><td>-0.33</td></tr><tr><td>10:30:00.0</td><td>17673.53</td><td>-1.25</td></tr><tr><td>11:00:00.0</td><td>17674.41</td><td>-0.36</td></tr></table>

A maximum variation of the pseudorange residuals of less than $3 \mathrm { m }$ is found in fair accord with the accuracy of the ionosphere-free pseudoranges.

Exercise 6.4 (Tropospheric Refraction) Compute the daily variation of the elevation of a geostationary satellite $( a = 4 2 1 6 4 \mathrm { k m }$ , $e \ = \ 0 . 0 0 2 9 6$ , $i \ : = \ : 0 . 0 5 ^ { \circ }$ , $\Omega = 1 5 0 . 7 ^ { \circ } ,$ ) for the ground station given in Exercise 6.1. Assume an epoch of $1 9 9 7 / 0 1 / 0 1 \ 0 ^ { \mathrm { h } }$ UTC and compute the elevation at intervals of $^ { 3 \mathrm { ~ h ~ } }$ . Compare the variation in elevation with the amplitude of the tropospheric refraction correction, as derived from (6.50) for a partial pressure of dry air of $1 0 2 4 \mathrm { h P a }$ , and a relative humidity of 0.7. Consider two cases with temperatures $T _ { 1 }$ and $T _ { 2 }$ of $2 8 3 \mathrm { ~ K ~ }$ and $3 0 3 ~ \mathrm { K }$ , respectively.

Solution: The elevation is $E _ { 0 } = 2 3 . 3 6 3 ^ { \circ }$ at the epoch and varies over a day with an amplitude of about $0 . 0 6 ^ { \circ }$ . The maximum elevation occurs $^ { 6 \mathrm { ~ h ~ } }$ past the epoch and the minimum elevation is reached at $1 8 \mathrm { { h } }$ . The daily variation of the elevation $E$ from $E _ { 0 }$ together with the elevation refraction corrections $\varDelta E _ { \mathrm { T 1 } }$ and $\varDelta E _ { \mathrm { T 2 } }$ are obtained as

<table><tr><td rowspan=1 colspan=5>UTC    E-Eo △ET1 △ET2</td></tr><tr><td rowspan=1 colspan=5>hh:mm:ss   [deg] [deg] [deg]</td></tr><tr><td rowspan=1 colspan=5>00:00:00.0   0.000 0.051 0.043</td></tr><tr><td rowspan=1 colspan=2>03:00:00.0   0.021</td><td rowspan=1 colspan=2>0.051</td><td rowspan=1 colspan=1>0.042</td></tr><tr><td rowspan=1 colspan=2>06:00:00.0   0.031</td><td rowspan=1 colspan=2>0.051</td><td rowspan=1 colspan=1>0.042</td></tr><tr><td rowspan=1 colspan=1>09:00:00.0</td><td rowspan=1 colspan=1>0.024</td><td rowspan=1 colspan=1>0.051</td><td></td><td rowspan=1 colspan=1>0.042</td></tr><tr><td rowspan=1 colspan=1>12:00:00.0</td><td rowspan=1 colspan=1>0.004</td><td rowspan=1 colspan=2>0.051</td><td rowspan=1 colspan=1>0.043</td></tr><tr><td rowspan=1 colspan=1>15:00:00.0</td><td rowspan=1 colspan=1>-0.017</td><td rowspan=1 colspan=2>0.051</td><td rowspan=1 colspan=1>0.043</td></tr><tr><td rowspan=1 colspan=1>18:00:00.0</td><td rowspan=1 colspan=1>-0.027</td><td rowspan=1 colspan=2>0.051</td><td rowspan=1 colspan=1>0.043</td></tr><tr><td rowspan=1 colspan=1>21:00:00.0</td><td rowspan=1 colspan=1>-0.020</td><td rowspan=1 colspan=2>0.051</td><td rowspan=1 colspan=1>0.043</td></tr><tr><td rowspan=1 colspan=1>24:00:00.0</td><td rowspan=1 colspan=1>-0.001</td><td rowspan=1 colspan=2>0.051</td><td rowspan=1 colspan=1>0.043</td></tr></table>

For the particular case considered, the refraction correction is of the order of the daily elevation variation but stays essentially constant for given meteorological conditions. The assumed temperature difference of $2 0 ~ \mathrm { K }$ changes the observed elevation by about $0 . 0 0 8 ^ { \circ }$ which may be compared to the $0 . 0 6 0 ^ { \circ }$ change resulting from the orbital inclination. At the distance of a geostationary satellite $0 . 0 0 1 ^ { \circ }$ corresponds to an along-track or cross-track position variation of about $7 0 0 \mathrm { m }$ .

# 7. Linearization

The trajectory and measurement model developed so far provides a concise and detailed description of a satellite’s motion with respect to an Earth-bound observer. Besides the state variables that define the initial conditions, these models depend on a variety of parameters that either affect the dynamical motion or the measurement process. Due to the complexity of the applied models it is hardly possible to solve directly for any of these parameters from a given set of observations. It is therefore customary to linearize the relation between the observables and the independent parameters to obtain simplified expressions that can be handled more easily. Within a statistical orbit determination one can then determine those state and model parameters that provide the best representation of a large set of measurements using a differential correction and parameter estimation algorithm.

A rigorous linearization of the trajectory and measurement model requires a large number of partial derivatives, which may be divided into four different categories:

The State Transition Matrix

The state vector $\mathbf { y } ( t _ { 0 } ) = ( \boldsymbol { r } ^ { T } ( t _ { 0 } ) , \boldsymbol { v } ^ { T } ( t _ { 0 } ) ) ^ { T }$ at some specified epoch $t _ { 0 }$ determines the form of the orbit and its orientation in space. Any change of these initial values results in a change of position and velocity at a later epoch $t$ which is described by the state transition matrix

$$
\left( \frac { \partial \mathbf { y } ( t ) } { \partial \mathbf { y } ( t _ { 0 } ) } \right) _ { 6 \times 6 } = \pmb { \phi } ( t , t _ { 0 } ) \quad .
$$

# • The Sensitivity Matrix

Aside from the initial state the orbit is also a function of various parameters $p _ { i }$ $( i = 1 , \ldots , n _ { p } )$ that determine the different forces acting on the satellite. This dependence is described by the sensitivity matrix, i.e. by the partial derivatives

$$
\left( \frac { \partial \pmb { y } ( t ) } { \partial \pmb { p } } \right) _ { 6 \times n _ { p } } = \pmb { S } ( t )
$$

with respect to the force model parameters. Depending on the application in mind, the parameter vector $\pmb { p }$ may e.g. contain the drag and radiation pressure coefficients $( C _ { \mathrm { D } } , C _ { \mathrm { R } } )$ , the thrust level of a maneuver or the size of certain gravity model coefficients.

Partials of the measurements with respect to the state vector

The linearized dependence of a measurement $z ( t )$ on the state vector $\mathbf { { \boldsymbol { y } } } ( t ) =$ $( r ^ { T } ( t ) , \pmb { v } ^ { T } ( t ) ) ^ { T }$ of the satellite at the time of the measurement is described by the partial derivatives

$$
\left( \frac { \partial z } { \partial \mathbf { y } ( t ) } \right) _ { 1 \times 6 } .
$$

It may be noted that the partials $\partial z / \partial v ( t )$ with respect to the instantaneous velocity vanish for all types of range and angle observations $\begin{array} { l } { \left( z \ = \right. } \end{array}$ $\rho , A , E , X , Y )$ if one neglects the light time and aberration correction and considers only geometrical values.

# • Partials with respect to measurement model parameters

Last but not least the predicted observations depend on certain measurement model parameters $q _ { i }$ $( i = 1 , \ldots , n _ { q } )$ like bias values due to an insufficient calibration of the zero point for angle readings or the transponder and ground station delay for range measurements. More elaborate measurement models may take care of further effects like antenna axis displacement and misalignment or ground station coordinate offsets that may be estimated during an orbit determination. The corresponding partial derivatives are given by an $n _ { q }$ -dimensional vector

$$
\left( \frac { \partial z } { \partial \pmb q } \right) _ { 1 \times n _ { q } } \quad .
$$

Combining these partial derivatives yields the dependence of an individual measurement $z$ on the initial state vector $\mathbf { \boldsymbol { y } } ( t _ { 0 } )$ , the vector $\pmb { p }$ of force model parameters and the vector $\pmb q$ of measurement model parameters:

$$
\begin{array} { r c l } { { \displaystyle \left( \begin{array} { c c c } { { \frac { \partial z } { \partial y ( t _ { 0 } ) } } } & { { \frac { \partial z } { \partial p } } } & { { \frac { \partial z } { \partial q } } } \end{array} \right) _ { 1 \times ( 6 + n _ { p } + n _ { q } ) } = } } \\ { { \displaystyle \left( \begin{array} { c c c } { { \left( \frac { \partial z } { \partial y ( t ) } \right) \cdot ( \pmb { \phi } ( t , t _ { 0 } ) \ \pmb { S } ( t ) ) } } & { { \frac { \partial z } { \partial q } } } \end{array} \right) } } & { { . } } \end{array}
$$

Given the models presented earlier, the analytical computation of the individual derivatives is tedious and cumbersome work, which provides little additional insight into the underlying concepts. Nevertheless, it forms an essential part of the overall orbit determination process, and may have a notable impact on the achievable performance and speed of convergence. The required relations are therefore derived and presented here in an adequate level of detail. Impatient readers may, however, skip to Chap. 8 on first reading and content themselves with the fact that any desired partial derivative could, in principle, be obtained from a numerical difference quotient approximation.

# 7.1 Two-Body State Transition Matrix

In the simplified case of unperturbed Keplerian orbits the state transition matrix and its inverse can be expressed as an analytical function of the Cartesian coordinates and the orbital elements. To this end, the state vector transition matrix is commonly factorized into the product of the more simple orbital elements transition matrix and the partial derivatives of the state vector with respect to the elements, both of which are derived in the sequel.

# 7.1.1 Orbital-Elements Transition Matrix

The orbital-elements transition matrix is given by

$$
\pmb { \phi } _ { \alpha } ( t , t _ { 0 } ) = \left( \frac { \partial \pmb { \alpha } ( t ) } { \partial \pmb { \alpha } ( t _ { 0 } ) } \right) _ { 6 \times 6 } \ \ \mathrm { ~ , ~ }
$$

where

$$
\pmb { \alpha } = ( a , e , i , \Omega , \omega , M ) ^ { T }
$$

denotes the vector of orbital elements. For an unperturbed orbit the orbital elements at time $t$ are the same as those at time $t _ { 0 }$ with the exception of the mean anomaly that changes by

$$
M ( t ) - M ( t _ { 0 } ) = n \left( t - t _ { 0 } \right) .
$$

Here, the mean motion

$$
n = { \sqrt { \frac { G M _ { \oplus } } { a ^ { 3 } } } }
$$

is a function of the semi-major axis $a$ . The orbital elements transition matrix may therefore be written as

$$
\Phi _ { \alpha } ( t , t _ { 0 } ) = \left( \begin{array} { c c c c c c } { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } \\ { { \displaystyle \frac { \partial M ( t ) } { \partial a ( t _ { 0 } ) } } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right) ~ ,
$$

where the only non-vanishing off-diagonal element is given by the term

$$
\frac { \partial M ( t ) } { \partial a ( t _ { 0 } ) } = - \frac { 3 } { 2 } \frac { n } { a } \left( t - t _ { 0 } \right)
$$

that describes the effect of small changes in the semi-major axis at time $t _ { 0 }$ on the mean anomaly $M ( t )$ at time $t$ .

# 7.1.2 Keplerian-to-Cartesian Partial Derivatives

According to the results of Chap. 2 the position $r$ and velocity $\pmb { v }$ of an unperturbed satellite in the central field of the Earth is given by

$$
r = \hat { x } P + \hat { y } Q ~ v = \hat { \hat { x } } P + \dot { \hat { y } } Q ~ ,
$$

where the Gaussian vectors $P$ and $\varrho$ are functions of the orbital elements $i , \varOmega$ and $\omega$ that define the orientation of the orbit in space, while the coordinates $\hat { x }$ and $\hat { y }$ inside the orbital plane are a function of the semi-major axis $a$ , the eccentricity $e$ and the mean anomaly $M$ . The partial derivatives of $r$ and $\dot { \boldsymbol { r } }$ with respect to an orbital element $\alpha$ may therefore be expressed as

$$
\frac { \partial r } { \partial \alpha } = \frac { \partial \hat { x } } { \partial \alpha } { \cal P } + \frac { \partial \hat { y } } { \partial \alpha } { \cal Q } \frac { \partial v } { \partial \alpha } = \frac { \partial \dot { \hat { x } } } { \partial \alpha } { \cal P } + \frac { \partial \dot { \hat { y } } } { \partial \alpha } { \cal Q }
$$

for $\alpha = a , e , M$ and as

$$
\frac { \partial r } { \partial \alpha } = \hat { x } \frac { \partial P } { \partial \alpha } + \hat { y } \frac { \partial Q } { \partial \alpha } \frac { \partial v } { \partial \alpha } = \dot { \hat { x } } \frac { \partial P } { \partial \alpha } + \dot { \hat { y } } \frac { \partial Q } { \partial \alpha }
$$

for $\alpha = \Omega , \omega , i$

The partial derivatives of the in-plane coordinates with respect to $a , e$ and $M$ follow from the basic equations

$$
\begin{array} { r c l r c l } { { \hat { x } } } & { { = } } & { { a \left( \cos { E } - e \right) } } & { { \dot { \hat { x } } } } & { { = } } & { { - \displaystyle \frac { \sqrt { G M _ { \oplus } a } } { r } \sin { E } } } \\ { { \hat { y } } } & { { = } } & { { a \sqrt { 1 - e ^ { 2 } } \sin { E } } } & { { \dot { \hat { y } } } } & { { = } } & { { + \displaystyle \frac { \sqrt { G M _ { \oplus } a } } { r } \sqrt { 1 - e ^ { 2 } } \cos { E } } } \end{array}
$$

with

$$
r = a \left( 1 - e \cos E \right) .
$$

Since the eccentric anomaly $E$ , which is implicitly defined by Kepler’s equation

$$
E - e \sin E = M
$$

as a function of $e$ and $M$ , does not depend on the semi-major axis $a$ , one obtains immediately

$$
{ \frac { \partial \hat { x } } { \partial a } } = \cos { E } - e = { \frac { \hat { x } } { a } } .
$$

For the derivatives with respect to $e$ and $M$ one has to consider the dependence of $E$ on both quantities, which is expressed by the total differential

$$
d E - e \cos E d E - d e \sin E = d M
$$

of Kepler’s equation. The partial derivatives of $E$ are therefore given by

$$
{ \frac { \partial E } { \partial e } } = { \frac { \sin E } { 1 - e \cos E } } = { \frac { a \sin E } { r } }
$$

and

$$
\frac { \partial E } { \partial M } = \frac { 1 } { 1 - e \cos E } = \frac { a } { r } .
$$

Using these results it follows that

$$
\frac { \partial \hat { x } } { \partial e } = a \left( - \sin E \cdot \frac { \partial E } { \partial e } - 1 \right) = - a - \frac { \hat { y } ^ { 2 } } { r ( 1 - e ^ { 2 } ) }
$$

and

$$
\frac { \partial \hat { x } } { \partial M } = a \left( - \sin E \right) \cdot \frac { \partial E } { \partial M } = \frac { \dot { \hat { x } } } { n } .
$$

The remaining derivatives are obtained in a completely analogous way yielding

$$
\frac { \partial ( \hat { x } , \hat { y } ) ^ { T } } { \partial ( a , e , M ) ^ { T } } = \left( \begin{array} { c c c } { \frac { \hat { x } } { a } } & { \left( - a - \frac { \hat { y } ^ { 2 } } { r ( 1 - e ^ { 2 } ) } \right) } & { \frac { \dot { \hat { x } } } { n } } \\ { \frac { \hat { y } } { a } } & { \left( \frac { \hat { x } \hat { y } } { r ( 1 - e ^ { 2 } ) } \right) } & { \frac { \dot { \hat { y } } } { n } } \end{array} \right)
$$

for the dependence of the in-plane position on $a , e$ and $M$ , while the velocity partials are given by

$$
\begin{array} { r l } { \frac { \partial ( \dot { \hat { x } } , \dot { \hat { y } } ) ^ { T } } { \partial ( a , e , M ) ^ { T } } = } & { { } } \\ { ( - \frac { \dot { \hat { x } } } { 2 a } } & { { } \dot { \hat { x } } ( \frac { a } { r } ) ^ { 2 } ( 2 ( \frac { \hat { x } } { a } ) + \frac { e } { 1 - e ^ { 2 } } ( \frac { \hat { y } } { a } ) ^ { 2 } ) } & { { } - n ( \frac { a } { r } ) ^ { 3 } \hat { x } \ ) } \\ { - \frac { \dot { \hat { y } } } { 2 a } } & { { } \frac { n } { \sqrt { 1 - e ^ { 2 } } } ( \frac { a } { r } ) ^ { 2 } ( \frac { \hat { x } ^ { 2 } } { r } - \frac { \hat { y } ^ { 2 } } { a ( 1 - e ^ { 2 } ) } ) } & { { } - n ( \frac { a } { r } ) ^ { 3 } \hat { y } \ ) } \end{array}
$$

(Broucke 1970, Long et al. 1989). The representation of these partial derivatives as a function of ${ \hat { x } } , { \dot { \hat { x } } } .$ , $\hat { y }$ and $\dot { \hat { y } }$ is convenient from the computational point of view, but one may equally well replace these quantities by the basic definitions given above. In this case one obtains the derivatives as a function of $a$ , $e$ and $E$ , where $E$ has to be obtained by solving Kepler’s equation for the given value of the mean anomaly $M$ .

In order to complete the computation of partial derivatives of the state vector with respect to the various orbital elements we may now turn to the derivatives of the Gaussian vectors with respect to $i , \varOmega$ and $\omega$ . Since changes in these angles correspond to rotations around the line of nodes vector $\pmb { n } = ( \cos \Omega , \sin \Omega , 0 ) ^ { T }$ , the unit vector $\pmb { e } _ { z } = ( 0 , 0 , 1 ) ^ { T }$ and the vector $W = P \times Q$ at right angles to the orbital plane, respectively, the partial derivatives of $P$ and $\varrho$ are given by

$$
\begin{array} { r c l } { { \displaystyle \frac { \partial P } { \partial i } } } & { { = } } & { { { \bf \nabla } n \times P \frac { \partial Q } { \partial i } = n \times Q } } \\ { { \displaystyle \frac { \partial P } { \partial \Omega } } } & { { = } } & { { e _ { z } \times P \frac { \partial Q } { \partial \Omega } = e _ { z } \times Q } } \\ { { \displaystyle \frac { \partial P } { \partial \omega } } } & { { = } } & { { W \times P \frac { \partial Q } { \partial \omega } = W \times Q . } } \end{array}
$$

Evaluating the cross products finally yields

$$
\begin{array} { r l r } { \frac { \partial P } { \partial i } } & { = } & { \sin ( \omega ) \cdot W \frac { \partial Q } { \partial i } = \cos ( \omega ) \cdot W } \\ { \frac { \partial P } { \partial \Omega } } & { = } & { \left( \begin{array} { c } { - P _ { y } } \\ { + P _ { x } } \\ { 0 } \end{array} \right) \frac { \partial Q } { \partial \Omega } = \left( \begin{array} { c } { - Q _ { y } } \\ { + Q _ { x } } \\ { 0 } \end{array} \right) } \\ { \frac { \partial P } { \partial \omega } } & { = } & { + Q \frac { \partial Q } { \partial \omega } = - P , } \end{array}
$$

where $P _ { x } , P _ { y }$ , $Q _ { x }$ and $Q _ { y }$ are the $x$ - and $y$ -components of $P$ and $\varrho$ , respectively. The same result may also be obtained by direct differentiation of the definition of $P$ and $\varrho$ given in Chap. 2.

# 7.1.3 Cartesian-to-Keplerian Partial Derivatives

The partial derivatives of the orbital elements $\pmb { \alpha }$ with respect to the state vector $\mathbf { y } = ( \boldsymbol { r } ^ { T } , \boldsymbol { v } ^ { T } ) ^ { T }$ may be obtained by computing the partial derivatives of the state vector with respect to the orbital elements and inverting the resulting $6 \times 6$ -matrix using appropriate numerical methods:

$$
\left( \frac { \partial \pmb { \alpha } } { \partial \pmb { y } } \right) _ { 6 \times 6 } = \left( \frac { \partial \pmb { y } } { \partial \pmb { \alpha } } \right) _ { 6 \times 6 } ^ { - 1 } .
$$

More favorably, however, the inverse is obtained from the analytical relationship

$$
\left( \begin{array} { l l } { { \displaystyle { \frac { \partial \alpha } { \partial r } } } } & { { \displaystyle { \frac { \partial \alpha } { \partial v } } } } \end{array} \right) = P ( \alpha , \alpha ) \left( \begin{array} { l } { { \displaystyle + \left( { \frac { \partial v } { \partial \alpha } } \right) ^ { T } - \left( { \frac { \partial r } { \partial \alpha } } \right) ^ { T } } } \end{array} \right) ,
$$

where $P$ is an anti-symmetric $6 \times 6$ matrix made up of the Poisson parentheses

$$
P ( \alpha _ { j } , \alpha _ { j } ) = \left( \frac { \partial \alpha _ { i } } { \partial r } \right) \cdot \left( \frac { \partial \alpha _ { j } } { \partial v } \right) ^ { T } - \left( \frac { \partial \alpha _ { j } } { \partial r } \right) \cdot \left( \frac { \partial \alpha _ { i } } { \partial v } \right) ^ { T } \mathrm { ~ . ~ }
$$

In total, only five independent matrix elements

$$
{ \begin{array} { r c l } { P ( a , M ) } & { = } & { - P ( M , a ) } \\ & & \\ { P ( e , \omega ) } & { = } & { - P ( \omega , e ) } & { = } & { { \frac { - 2 } { n a ^ { 2 } e } } } \\ & & & \\ { P ( e , M ) } & { = } & { - P ( M , e ) } & { = } & { { \frac { - ( 1 - e ^ { 2 } ) } { n a ^ { 2 } e } } } \\ & & & \\ { P ( i , \varOmega ) } & { = } & { - P ( \varOmega , i ) } & { = } & { { \cfrac { 1 } { n a ^ { 2 } { \sqrt { 1 - e ^ { 2 } } } \sin i } } } \\ & & & \\ { P ( i , \omega ) } & { = } & { - P ( \omega , i ) } & { = } & { { \cfrac { - \cot i } { n a ^ { 2 } { \sqrt { 1 - e ^ { 2 } } } } } } \end{array} }
$$

exist, while all other Poisson parentheses vanish. For further details and a proof of these relations the reader is referred to Broucke (1970).

# 7.1.4 The State Transition Matrix and Its Inverse

Making use of the results obtained so far, the state transition matrix can be partitioned into the product

$$
\pmb { \phi } ( t , t _ { 0 } ) = \left( \frac { \partial \pmb { y } ( t ) } { \partial \pmb { \alpha } ( t ) } \right) \cdot \pmb { \phi } _ { \alpha } ( t , t _ { 0 } ) \cdot \left( \frac { \partial \pmb { y } ( t _ { 0 } ) } { \partial \pmb { \alpha } ( t _ { 0 } ) } \right) ^ { - 1 }
$$

of the orbital elements transition matrix and the state vector partials with respect to the orbital elements. In evaluating this expression, care must be taken that the partial derivatives of the state vector with respect to the orbital elements need to be evaluated at two different epochs, namely $t _ { 0 }$ (right-hand matrix) and $t$ (left-hand matrix). As a consequence, only a small number of terms is common to the computation of both expressions (e.g. the derivatives of the Gaussian vectors with respect to the orientation elements). This problem may partly be overcome by improved formulations for the direct computation of the state transition matrix as given in Sconzo (1963), Goodyear (1965), and Shepperd (1985). Furthermore, it is noted that the use of orbital elements in the above factorization introduces an artificial singularity at zero eccentricity and inclination into the resulting expressions. To avoid this singularity, one may apply equivalent, but less common expressions for equinoctial elements (see Sect. 2.2.5) and the associated partial derivatives (Broucke & Cefola 1972, Dow 1975).

In computing the inverse of the state transition matrix, one benefits considerably from the fact that $\Phi$ is a symplectic matrix for Keplerian orbits. As shown in more detail in Sect. 7.2.4, $\Phi$ obeys the relation

$$
\begin{array} { r } { \Phi ^ { T } J \Phi = J \qquad \mathrm { w i t h } \qquad J = \left( \begin{array} { r r } { 0 } & { + 1 } \\ { - 1 } & { \ \mathbf { 0 } } \end{array} \right) _ { 6 \times 6 } } \end{array}
$$

(Wintner 1941, Battin 1987). Making use of the identity $J ^ { 2 } = - \mathbf { 1 }$ , the inverse of a symplectic matrix $\Phi$ is given by

$$
\pmb { \phi } ^ { - 1 } = - J \pmb { \phi } ^ { T } J
$$

in much the same way as the inverse of a symmetric matrix is equal to its transpose. Upon splitting the transition matrix

$$
\pmb { \phi } ( t , t _ { 0 } ) = \left( \begin{array} { l l } { \pmb { \phi } _ { r r } } & { \pmb { \phi } _ { r v } } \\ { \pmb { \phi } _ { v r } } & { \pmb { \phi } _ { v v } } \end{array} \right)
$$

into its position and velocity related blocks, the result finally takes the form

$$
\phi ^ { - 1 } ( t , t _ { 0 } ) = \left( \begin{array} { c c } { { + \pmb { \phi } _ { v v } ^ { T } } } & { { - \pmb { \phi } _ { r v } ^ { T } } } \\ { { - \pmb { \phi } _ { v r } ^ { T } } } & { { + \pmb { \phi } _ { r r } ^ { T } } } \end{array} \right) \quad .
$$

The inverse of the state transition matrix is thus obtained by simple rearrangement of its elements without a need to refer to general numerical matrix-inversion methods.

# 7.2 Variational Equations

Even though the state transition matrix of the two-body problem is a reasonable approximation of the actual transition matrix, it is sometimes desirable to take into account at least the major perturbations in the computation of $\Phi ( t , t _ { 0 } )$ . As with the treatment of the perturbed satellite motion, one may not, however, obtain an analytical solution anymore in this case, but has to solve a special set of differential equations – the variational equations – by numerical methods. Aside from the increased accuracy that may be obtained by accounting for perturbations, the concept of the variational equations offers the advantage that it is not limited to the computation of the state transition matrix, but may also be extended to the treatment of partial derivatives with respect to force model parameters.

# 7.2.1 The Differential Equation of the State Transition Matrix

The differential equation, which describes the change of the state transition matrix with time, follows from the equation of motion of the satellite. If the state vector

$$
\mathbf { \boldsymbol { y } } ( t ) = \binom { \boldsymbol { r } ( t ) } { \mathbf { \boldsymbol { v } } ( t ) }
$$

obeys the first-order differential equation

$$
\frac { d } { d t } { \bf y } ( t ) = { \bf \nabla } f ( t , { \bf y } ) = { \bf \Omega } \left( { { \bf \Omega } \bullet ( t ) } \right)
$$

then

$$
{ \frac { \partial } { \partial { \boldsymbol { y } } ( t _ { 0 } ) } } { \frac { d } { d t } } { \boldsymbol { y } } ( t ) = { \frac { \partial { \boldsymbol { f } } ( t , { \boldsymbol { y } } ( t ) ) } { \partial { \boldsymbol { y } } ( t _ { 0 } ) } } = { \frac { \partial { \boldsymbol { f } } ( t , { \boldsymbol { y } } ( t ) ) } { \partial { \boldsymbol { y } } ( t ) } } \cdot { \frac { \partial { \boldsymbol { y } } ( t ) } { \partial { \boldsymbol { y } } ( t _ { 0 } ) } } .
$$

The state transition matrix

$$
\pmb { \phi } ( t , t _ { 0 } ) = \frac { \partial \mathbf { y } ( t ) } { \partial \mathbf { y } ( t _ { 0 } ) }
$$

may therefore be obtained from

$$
\frac { d } { d t } \pmb \Phi ( t , t _ { 0 } ) = \frac { \partial f ( t , \pmb y ( t ) ) } { \partial \pmb y ( t ) } \cdot \pmb \Phi ( t , t _ { 0 } )
$$

or

$$
\frac { d } { d t } \pmb \phi ( t , t _ { 0 } ) = \left( \begin{array} { c c } { \mathbf 0 _ { 3 \times 3 } } & { \mathbf 1 _ { 3 \times 3 } } \\ { \partial \pmb { a } ( r , v , t ) } & { \partial \pmb { a } ( r , v , t ) } \\ { \partial \pmb { r } ( t ) } & { \frac { \partial \pmb { a } ( t ) } { \partial \pmb { v } ( t ) } } \end{array} \right) _ { 6 \times 6 } \cdot \pmb \phi ( t , t _ { 0 } )
$$

and the initial value $\pmb { \phi } ( t _ { 0 } , t _ { 0 } ) = \mathbf { 1 } _ { 6 \times 6 }$ .

# 7.2.2 The Differential Equation of the Sensitivity Matrix

The differential equation of the sensitivity matrix that gives the partial derivatives of the state vector with respect to the force model parameter vector may be obtained in a completely analogous way, yielding

$$
\frac { d } { d t } \frac { \partial \pmb { y } ( t ) } { \partial \pmb { p } } = \frac { \partial \pmb { f } ( t , \pmb { y } ( t ) , \pmb { p } ) } { \partial \pmb { y } ( t ) } \cdot \frac { \partial \pmb { y } ( t ) } { \partial \pmb { p } } + \frac { \partial \pmb { f } ( t , \pmb { y } ( t ) , \pmb { p } ) } { \partial \pmb { p } }
$$

or

$$
\left( \frac { \mathbf { 0 } _ { 3 \times 3 } } { \partial \pmb { a } ( t , r , v , p ) } \frac { \partial \pmb { a } ( t , r , v , p ) } { \partial \pmb { v } ( t ) } \right) _ { 6 \times 6 } \cdot S ( t ) + \left( \frac { \mathbf { 0 } _ { 3 \times n _ { p } } } { \partial \pmb { a } ( t , r , v , p ) } \right) _ { 6 \times n _ { p } } .
$$

Since the state vector at $t _ { 0 }$ does not depend on any force model parameter, the initial value of the sensitivity matrix is given by $\mathbf { } S ( t _ { 0 } ) = \mathbf { 0 }$ .

# 7.2.3 Form and Solution of the Variational Equations

By combining the differential equations for the state transition matrix and the sensitivity matrix one obtains the following form of the variational equations

$$
\frac { d } { d t } ( \Phi , S ) = \left( \begin{array} { l l } { { { \bf 0 } _ { 3 \times 3 } } } & { { { \bf 1 } _ { 3 \times 3 } } } \\ { { \displaystyle \frac { \partial a } { \partial r } } } & { { \displaystyle \frac { \partial a } { \partial v } } } \end{array} \right) _ { 6 \times 6 } \cdot ( \Phi , S ) + \left( \begin{array} { l l } { { { \bf 0 } _ { 3 \times 6 } } } & { { { \bf 0 } _ { 3 \times n _ { p } } } } \\ { { { \bf 0 } _ { 3 \times 6 } } } & { { \displaystyle \frac { \partial a } { \partial p } } } \end{array} \right) _ { 6 \times ( 6 + n _ { p } ) } ,
$$

which is adequate for use with numerical integration methods for the solution of first-order initial value problems. An alternate representation, which is suitable for methods that allow the direct integration of second-order differential equations, may be obtained by decomposing $\Phi$ and $s$ into

$$
\Phi = \left( \Phi _ { r } \right) = \left( \begin{array} { l } { \frac { \partial r ( t ) } { \partial ( r ( t _ { 0 } ) , v ( t _ { 0 } ) ) } } \\ { \frac { \partial v ( t ) } { \partial ( r ( t _ { 0 } ) , v ( t _ { 0 } ) ) } } \end{array} \right) \quad S = \left( \begin{array} { l } { S _ { r } } \\ { S _ { v } } \\ { S _ { v } } \end{array} \right) = \left( \begin{array} { l } { \frac { \partial r ( t ) } { \partial p } } \\ { \frac { \partial v ( t ) } { \partial p } } \end{array} \right) \quad .
$$

Since (by changing the order of differentiation)

$$
\frac { d } { d t } ( \pmb { \phi } _ { r } , \pmb { S } _ { r } ) = ( \pmb { \phi } _ { v } , \pmb { S } _ { v } ) \quad ,
$$

the variational equations may then be written as

$$
( \ddot { \pmb { \phi } } _ { r } , \ddot { \pmb { S } } _ { r } ) = \frac { \partial a } { \partial r } ( \pmb { \phi } _ { r } , \pmb { S } _ { r } ) + \frac { \partial a } { \partial v } ( \dot { \pmb { \phi } } _ { r } , \dot { \pmb { S } } _ { r } ) + \left( \pmb { 0 } _ { 3 \times 6 } \frac { \partial a } { \partial p } \right) .
$$

If the acceleration does not depend on the velocity, the $\partial \pmb { a } / \partial \pmb { v }$ term vanishes, which means that the right-hand side of the second-order variational equations does not depend on $( \dot { \pmb { \phi } } _ { r } , \ddot { \pmb { S } } _ { r } )$ anymore. This fact may be useful since it allows the use of very efficient numerical integration methods for solution of the variational equations (e.g. Runge–Kutta–Nystrøm or Stoermer–Cowell methods).

Independent of the preferred form of the variational equations it is important to note that the variational equations have to be integrated simultaneously with the state vector. Otherwise the position and velocity of the satellite, which are required to evaluate the acceleration partials in the right-hand side of the variational equations, would be unknown. The combined integration of the state vector $\textbf {  { y } }$ , the state transition matrix $\Phi$ and the sensitivity matrix $s$ therefore requires the solution of $( 7 + n _ { p } )$ six-dimensional first-order differential equations or, equivalently, the same number of three-dimensional second-order differential equations. It should be emphasized, however, that the total effort is usually much less than $( 7 + n _ { p } )$ -times the effort for integrating the differential equation of the orbit alone. The reason for this property lies in the fact that the highest amount of work during the numerical integration is generally spent in the evaluation of the variational equations and not in the integration routine. The total integration effort is therefore proportional to the work required for the computation of the partial derivatives of the acceleration. By computing these derivatives along with the acceleration itself one can make use of common sub-expressions, which reduces the computing effort considerably.

Since accuracy requirements for the partial derivatives are generally more relaxed than that for the trajectory itself, it is common to apply a simplified force model in the solution of the variational equations. While purely Keplerian state transition matrices may cause slow convergence of iterated differential correction methods for orbit determination, the incorporation of the lowest-order zonal gravity field perturbation $( C _ { 2 , 0 } )$ already provides an acceptable minimum model (see e.g. Ballani 1988).

As pointed out by various authors, considerable care must be taken, however, to use consistent models in the simultaneous integration of the state vector and variational equations. This is dramatically shown by the analytical solution of the combined equations for an equatorial orbiter and a second-order zonal gravity field given by Rice (1967). While a purely Keplerian formulation yields a transition matrix in fair agreement with the solution of the perturbed problem, a completely erroneous solution is obtained after a few orbits upon combining an unperturbed gravity field in the differential equation of the transition matrix with a second-order gravity field in the state equations! The problem is further confirmed by numerical studies of more elaborate force models (May 1980), giving clear indication for the need of a consistent modeling. From a practical point of view, one may thus choose to either perform a rigorous integration of the variational equations using the same sophisticated model as required for the state equations or to treat the variational equations as a separate problem. In the latter case, the state equations are once integrated individually with the full model and once along with the variational equations using a simplified force model (e.g. up to $C _ { 2 , 0 }$ ). Even though the trajectory of the simplified model diverges notably from the true orbit, the resulting state transition matrix will nevertheless be found to closely match the actual value.

# 7.2.4 The Inverse of the State Transition Matrix

Aside from the state transition matrix itself, a variety of applications requires the inverse matrix $\Phi ^ { - 1 } ( t , t _ { 0 } )$ to map a state vector change at time $t$ back to the initial epoch $t _ { 0 }$ . While numerical methods are generally available and well suited to performing the inversion, the special properties of the transition matrix offer various alternatives. In the case that the inverse state matrix is of primary interest, one may e.g. solve the adjoint matrix differential equation

$$
\frac { d } { d t } \pmb { \phi } ^ { - 1 } ( t , t _ { 0 } ) = - \pmb { \phi } ^ { - 1 } ( t , t _ { 0 } ) \cdot \left( \frac { \partial \pmb { f } } { \partial \pmb { y } } \right)
$$

(Curkendall 1974), which follows from (7.41) and the identity ${ d ( \pmb { \phi } \pmb { \phi } ^ { - 1 } ) } / { d t } = \pmb { 0 }$ (Battin 1987). Like the variational equations described before, this equation is integrated along with the state vector using the initial conditions $\pmb { \phi } ^ { - 1 } = \pmb { 1 }$ .

Another approach can be applied whenever the acceleration does not depend on the velocity and, at the same time, exhibits a symmetric gradient ${ G = \partial { \pmb a } / \partial r }$ . In this case, the partial derivatives

$$
\pmb { F } = \frac { \partial \pmb { f } } { \partial \pmb { y } } = \left( \begin{array} { c c } { \mathbf { 0 } } & { \mathbf { 1 } } \\ { \pmb { G } } & { \mathbf { 0 } } \end{array} \right) _ { 6 \times 6 }
$$

obey the relation

$$
{ \cal J } F = - F ^ { T } { \cal J } \quad \quad \mathrm { w i t h } \quad \quad { \cal J } = \left( \begin{array} { r r } { { { \bf 0 } } } & { { + { \bf 1 } } } \\ { { - { \bf 1 } } } & { { { \bf 0 } } } \end{array} \right) _ { 6 \times 6 } .
$$

As a consequence, the state transition matrix can be shown to be a symplectic matrix, which is characterized by the relation

$$
\pmb { \phi } ^ { T } J \pmb { \phi } = J \quad .
$$

Following Battin (1987) the time derivative of $\Phi ^ { T } J \Phi$ vanishes under the given conditions, while the relation at epoch $t _ { 0 }$ (i.e. $\pmb { \phi } = \pmb { 1 }$ ) is a trivial identity. The significance of this property lies in the ease of determining the inverse of a symplectic matrix. Making use of the identity $J ^ { 2 } = - \mathbf { 1 }$ , the inverse is given by

$$
\pmb { \phi } ^ { - 1 } = - J \pmb { \phi } ^ { T } J
$$

in much the same way as the inverse of a symmetric matrix is equal to its transpose. The state transition matrix is, in particular, symplectic for all types of gravitational forces due to the symmetry of the gravity gradient. Its inverse can then be found from (7.36) by simple rearrangement of the matrix elements. Care should be taken, however, that the symplectic property is evidently violated in the presence of aerodynamic drag, in which case reference to numerical matrix inversion methods should be made.

# 7.3 Partial Derivatives of the Acceleration

The variational equations depend on the partial derivatives of the acceleration with respect to the state and model parameters, which are discussed in more detail in the present section.

# 7.3.1 Geopotential

The most important contribution to the variational equations for the state transition matrix arises from the central term

$$
{ \ddot { r } } = - { \frac { G M _ { \oplus } } { r ^ { 3 } } } r
$$

of the Earth’s gravitational attraction. Using the general relation

$$
\frac { \partial r ^ { n } } { \partial r } = \frac { \partial ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ) ^ { n / 2 } } { \partial r } = n \cdot r ^ { n - 2 } \cdot r ^ { T }
$$

it follows that

$$
\frac { \partial \ddot { r } } { \partial r } = - G M _ { \oplus } \frac { \partial } { \partial r } \left( r \frac { 1 } { r ^ { 3 } } \right) = - G M _ { \oplus } \left( \frac { 1 } { r ^ { 3 } } { \bf 1 } _ { 3 \times 3 } - 3 r \frac { r ^ { T } } { r ^ { 5 } } \right) ~ .
$$

Here the factor $r r ^ { T }$ in the second term is a dyadic product, which yields a $3 { \times } 3$ -matrix and should not be confused with the dot product $r ^ { T } r$ . Evaluating the individual components of ${ \partial \ddot { r } } / { \partial r }$ yields

$$
\frac { \partial \ddot { r } } { \partial r } = \frac { G M _ { \oplus } } { r ^ { 5 } } \left( \begin{array} { c c c } { { 3 x ^ { 2 } - r ^ { 2 } } } & { { 3 x y } } & { { 3 x z } } \\ { { 3 y x } } & { { 3 y ^ { 2 } - r ^ { 2 } } } & { { 3 y z } } \\ { { 3 z x } } & { { 3 z y } } & { { 3 z ^ { 2 } - r ^ { 2 } } } \end{array} \right) ,
$$

which shows that the gravity gradient is symmetric with respect to the main diagonal and that the sum of the diagonal elements vanishes.

Both properties follow from the fact that the gravitational attraction may be written as the gradient

$$
{ \boldsymbol { \ddot { r } } } = \left( { \frac { \partial U } { \partial r } } \right) ^ { T }
$$

of a potential $U$ , which is given by

$$
U = G M _ { \oplus } { \frac { 1 } { r } }
$$

for the simplified case of a point mass $M _ { \oplus }$ in the center of the Earth.

The partial derivatives of $\ddot { r }$ with respect to $r$ are just the second partial derivatives of $U$ , which are clearly symmetric, since the order of differentiation with respect to the components of $r$ may be interchanged, i.e.

$$
{ \frac { \partial { \ddot { y } } } { \partial x } } = { \frac { \partial ^ { 2 } U } { \partial x \partial y } } = { \frac { \partial ^ { 2 } U } { \partial y \partial x } } = { \frac { \partial { \ddot { x } } } { \partial y } } \mathrm { e t c } .
$$

Since this symmetry is independent of the particular form of $U$ , it is not only valid for the central term of the Earth’s potential but also for all higher order harmonics. By considering the Laplacian

$$
\Delta U = \frac { \partial ^ { 2 } U } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } U } { \partial y ^ { 2 } } + \frac { \partial ^ { 2 } U } { \partial z ^ { 2 } } ,
$$

which reduces to

$$
\Delta U ( r ) = { \frac { 1 } { r } } { \frac { \partial ^ { 2 } } { \partial r ^ { 2 } } } ( r U ( r ) ) = 0 ( r > 0 )
$$

in the case of the radially symmetric $1 / r$ -potential, one may easily verify that the sum of the diagonal elements of ${ \partial \ddot { r } } / { \partial r }$ vanishes for the attraction of a point like body. For an extended body like the Earth the gravitational potential may be represented by a superposition

$$
U = G \int { \frac { \rho ( s ) d ^ { 3 } s } { | r - s | } }
$$

of the $1 / r$ -potentials arising from all mass elements $d m = \rho ( s ) d ^ { 3 } s$ and the Laplacian is therefore zero, too, for all points outside the surface of the body.

The symmetry property of the matrix ${ \partial \ddot { r } } / { \partial r }$ of partial derivatives of the Earth’s attraction with respect to the position and the condition of a vanishing sum of the diagonal elements reduces the number of independent components that have to be considered in the computation from nine to five. In an Earth-fixed frame these components may conveniently be obtained from

$$
\frac { \partial \ddot { \pmb { r } } } { \partial \pmb { r } } = \sum _ { n , m } \frac { \partial \ddot { \pmb { r } } _ { n m } } { \partial \pmb { r } }
$$

(cf. (3.33)) using expressions for the terms of degree $n$ and order $m$ derived by Cunningham (1970):

$$
\begin{array} { r l } { \frac { \partial \hat { x } _ { n m } ^ { + } } { \partial x } } & { ( m = 0 ) \frac { G M _ { \oplus } } { R _ { \oplus } ^ { 3 } } \cdot \frac { 1 } { 2 } \cdot \left\{ ( + C _ { n 0 } V _ { n + 2 , 2 } ) - \frac { ( n + 2 ) ! } { n ! } \cdot ( + C _ { n 0 } V _ { n + 2 , 0 } ) \right\} } \\ & { ( \stackrel { \mathrm { i n } } { = } - 1 ) \frac { G M _ { \oplus } } { R _ { \oplus } ^ { 3 } } \cdot \frac { 1 } { 4 } \cdot \left\{ ( + C _ { n 1 } V _ { n + 2 , 3 } + S _ { n 1 } W _ { n + 2 , 3 } ) \right. } \\ & { \left. \qquad + \frac { ( n + 1 ) ! } { ( n - 1 ) ! } \cdot ( - 3 C _ { n 1 } V _ { n + 2 , 1 } - S _ { n 1 } W _ { n + 2 , 1 } ) \right\} } \\ { \stackrel { \mathrm { O r e r } } { = } \frac { 1 } { R _ { \oplus } ^ { 3 } } \frac { G M _ { \oplus } } { 1 _ { \oplus } ^ { 3 } } \cdot \frac { 1 } { 4 } \cdot \left\{ ( + C _ { n n } V _ { n + 2 , m + 2 } + S _ { n n } W _ { n + 2 , m + 2 } ) \right. } \\ & { \left. \qquad + 2 \frac { ( n - m + 2 ) ! } { ( n - m ) ! } \cdot ( - C _ { n n } V _ { n + 2 , m } - S _ { n m } W _ { n + 2 , m } ) \right. } \\ & { \left. \qquad + \frac { ( n - m + 4 ) ! } { ( n - m ) ! } \cdot ( + C _ { n m } V _ { n + 2 , m - 2 } + S _ { n m } W _ { n + 2 , m - 2 } ) \right\} } \end{array}
$$

$$
\begin{array} { r l } { \frac { \partial \hat { \lambda } _ { \mathrm { t r u x } } } { \partial y _ { \mathrm { t r u x } } } } & { \iff \omega \hat { \boldsymbol { u } } } \\ { \frac { \partial \hat { \lambda } _ { \mathrm { t r u x } } } { \partial y _ { \mathrm { t r u x } } } } & { \succeq \omega \hat { \boldsymbol { u } } ^ { \mathrm { B R } } \hat { \boldsymbol { u } } ^ { \mathrm { B R } } + \frac { 1 } { L } \{ ( \epsilon C _ { \mathrm { G P H } } W _ { \mathrm { t r u x } ; 2 } \times S - \epsilon _ { \mathrm { G P H } ; 1 } \times 1 )  } \\ { \mathrm { s u p } } & { \Biggl . \hat { \mathcal { K } } _ { \mathrm { B R } } ^ { \mathrm { B R } } : \frac { 1 } { L } \cdot \{ ( \epsilon + C _ { \mathrm { G P H } } W _ { \mathrm { t r u x } ; 2 } \times S - \epsilon _ { \mathrm { G P H } ; 1 } V _ { \mathrm { t r u x } ; 2 } )  } \\ &  \quad \quad  + \frac { \omega \mathrm { H } _ { \mathrm { t r u x } } } { \Gamma } \cdot \mathrm { C - C - C _ { \mathrm { G P H } ; 1 } \cdot \nabla _ { \mathrm { H } ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } } \} } \\ & { \quad \times \frac { \omega \mathrm { B R } } { \omega \omega } \frac { \partial \boldsymbol { u } } { \partial x _ { \mathrm { 0 } } } \frac { 1 } { L } \cdot \{ [ ( C _ { \mathrm { G P H } } W _ { \mathrm { H } ; 2 ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } )  }  } \\ &  \quad   \hat { \mathcal { U } } _ { \mathrm { B R } } ^ { \mathrm { B R } } : \frac { 1 + \omega - \mathrm { i } \cdot \mathrm { i } \cdot \mathrm { i } } { L } \cdot ( C _ { \mathrm { G P H } } W _ { \mathrm { t r u x } ; 2 ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } ; \mathrm { H } \mathrm { H } ; \mathrm { H } \mathrm { H } ; \mathrm { H } \mathrm { H } ; \mathrm { H } \mathrm { H }   } \\ &  \quad    \hat { \mathcal { U } } _ { \mathrm { B R } } : \end{array}
$$$$
\begin{array} { r l } { \frac { \partial \vec { x } _ { \mathrm { a m } } } { \partial z } } & { \underset { \vec { R } _ { 0 } ^ { * } } { = } \frac { G \vec { R } _ { 0 } } { F } , \{ ( a + 1 ) \cdot ( \mathrm { \it ~ ( } C _ { m } \vec { R } _ { n + 2 , 1 } ) \} } \\ & { \stackrel { \mathrm { ( a s s ) ~ } } { = } \frac { G \vec { R } _ { 0 } } { R _ { 0 } ^ { * } } [ \frac { n - m + 1 } { 2 } \cdot ( \mathrm { \it ~ ( C - m ~ } V _ { n + 2 , n + 1 } + \mathrm { \it ~ S ~ _ { m } } \vec { R } _ { n + 2 , n + 1 } ) } \\ & { \quad \quad + \frac { ( n - m + 3 ) ! } { 2 ( n - m ) ! } \cdot ( - C _ { m } V _ { n + 2 , n - 1 } - \mathrm { \it ~ S ~ _ { m } } \vec { R } _ { n + 2 , n - 1 } ) ] } \\ & { \quad \quad + \frac { ( n - m + 3 ) ! } { 2 ( n - m ) ! } \cdot ( - C _ { m } V _ { n + 2 , n - 1 } \cdot - \mathrm { \it ~ S ~ _ { m } } \vec { R } _ { n - 2 , n - 1 } ) \Biggr \} } \\ { \frac { \partial \vec { R } _ { \mathrm { a m } } } { \partial z } } & { \underset { \vec { R } _ { 0 } ^ { * } } { = } \frac { G \vec { R } _ { 0 } } { F } , \{ ( a + 1 ) \cdot ( \mathrm { \it ~ ( } C _ { m } \vec { R } _ { n + 2 , 1 } ) \} } \\ & { \stackrel { \mathrm { ( a s s ) ~ } } { = } \frac { G \vec { R } _ { 0 } } { R _ { 0 } ^ { * } } [ \frac { n - m + 1 } { 2 } \cdot \mathrm { \it ~ ( C - a v ~ } \vec { R } _ { n + 2 , n + 1 } - \mathrm { \it ~ S ~ _ { a m } } V _ { n + 2 , n + 1 } )  } \\ & { \quad  \mathrm { ( } \frac { n - m + 3 ) ! } { 2 ( n - m ) ! } \cdot ( \mathrm { \it ~ ( C - a v ~ } \vec { R } _ { n + 2 , n - 1 } \cdot \mathrm { \it ~ S ~ _ { a m } ~ V _ { n + 2 , n - 1 } ~ ) } ) } \\ &  \quad  + \frac { ( n - m + 3 ) ! } { 2 ( n - m ) ! } \cdot ( \mathrm  \it ~ ( C ~  \end{array}
$$

$$
\begin{array} { r c l } { { \frac { \partial \stackrel { . . } { z } _ { n m } } { \partial z } } } & { { = } } & { { \frac { G M _ { \oplus } } { R _ { \oplus } ^ { 3 } } \Big \{ \frac { ( n - m + 2 ) ! } { ( n - m ) ! } \cdot ( + C _ { n m } V _ { n + 2 , m } + S _ { n m } W _ { n + 2 , m } ) \Big \} ~ . } } \end{array}
$$

Here $V _ { n m }$ and $W _ { n m }$ , which follow from the recurrence relations (3.29) and (3.30), are the same quantities that are used in the computation of the acceleration. If the partial derivatives of the acceleration due to geopotential coefficients up to $C _ { n n }$ and $S _ { n n }$ have to be calculated then $V _ { \nu \mu }$ and $W _ { \nu \mu }$ are required up to degree and order $n { + 2 }$ .

For a non-rotating Earth the expressions derived so far would directly represent the desired partial derivatives. Due the Earth’s rotation some additional transformations are, however, required, since the components of $r$ and $\ddot { r }$ in (7.65)…(7.69) refer to a coordinate system that is aligned with the instantaneous rotation axis of the Earth and the direction of the meridian of Greenwich. Using indices “sf” and “ef” to distinguish between space-fixed and Earth-fixed coordinates the desired partial derivatives in the space-fixed reference system are given by

$$
\left( \frac { \partial \ddot { \pmb { r } } } { \partial \pmb { r } } \right) _ { \mathrm { s f } } = \pmb { U } ^ { - 1 } ( t ) \cdot \left( \frac { \partial \ddot { \pmb { r } } } { \partial \pmb { r } } \right) _ { \mathrm { e f } } \cdot \pmb { U } ( t ) \quad ,
$$

where $U$ describes the time-dependent transformation to Earth-fixed coordinates according to

$$
\pmb { r } _ { \mathrm { e f } } = \pmb { U } ( t ) \cdot \pmb { r } _ { \mathrm { s f } } \quad \mathrm { a n d } \quad \ddot { \pmb { r } } _ { \mathrm { s f } } = \pmb { U } ^ { - 1 } ( t ) \cdot \ddot { \pmb { r } } _ { \mathrm { e f } } \quad .
$$

The term $( \partial \ddot { r } / \partial r ) _ { \mathrm { e f } }$ may be computed by evaluating (7.65)…(7.69) with $( x , y , z )$ replaced by the Earth-fixed coordinates $( x _ { \mathrm { e f } } , y _ { \mathrm { e f } } , z _ { \mathrm { e f } } )$ . It should further be emphasized that both $( \partial \ddot { r } / \partial r ) _ { \mathrm { s f } }$ and $( \partial \ddot { r } / \partial r ) _ { \mathrm { e f } }$ are partial derivatives of the acceleration in inertial coordinate systems which are rotated against each other by a given rotation $U$ . The acceleration in a rotating coordinate system would be different by Coriolis and centrifugal terms.

Since the acceleration due to the Earth’s attraction does not depend on the satellite’s velocity, the partial derivatives with respect to the position are all that is required to compute the contribution of the geopotential to the variational equations for the state transition matrix. In the case of the sensitivity matrix some further partials may, however, be of interest. Neglecting the influence of Earth rotation parameters on the acceleration the only model parameters of interest are the product $G M _ { \oplus }$ of the gravitational constant and the Earth’s mass as well as the gravity model coefficients $C _ { n m }$ and $S _ { n m }$ . Since $G M _ { \oplus }$ is a multiplicative factor in the computation of the Earth’s acceleration, the corresponding partials are simply given by

$$
{ \frac { \partial \ddot { \pmb r } } { \partial G M _ { \oplus } } } = { \frac { 1 } { G M _ { \oplus } } } \ddot { \pmb r } \quad .
$$

The derivatives with respect to the geopotential coefficients follow in a similar manner from the fundamental relations for the acceleration yielding e.g.

$$
\left( \frac { \partial \ddot { z } } { C _ { n m } } , \frac { \partial \ddot { z } } { S _ { n m } } \right) = ( n - m + 1 ) \frac { G M _ { \oplus } } { R _ { \oplus } ^ { 2 } } \cdot ( - V _ { n + 1 , m } , - W _ { n + 1 , m } ) .
$$

The corresponding expressions for the $x$ and $y$ -components may easily be derived from (3.33).

Even though the partials with respect to $G M _ { \oplus }$ , $C _ { n m }$ and $S _ { n m }$ may therefore be computed at almost no additional cost from known quantities, they are not considered in most orbit determination programs. This is due to the fact that the estimation of these force model parameters is not possible for individual satellites but requires the simultaneous consideration of a large set of observations from different types of satellite orbits. An estimation of $G M _ { \oplus }$ , $C _ { n m }$ and $S _ { n m }$ is therefore only foreseen in specialized programs for geodetic applications (see e.g. McCarthy et al. 1993).

# 7.3.2 Point-Mass Perturbations

According to (3.37) the perturbations of the Sun and the Moon in an Earth-centred reference frame are given by

$$
\ddot { r } = - G M \cdot \left( \frac { r - s } { | r - s | ^ { 3 } } + \frac { s } { | s | ^ { 3 } } \right) .
$$

Only the direct gravitational attraction depends on the satellite coordinates and the partial derivatives of the acceleration with respect to $r$ are therefore given by

$$
\frac { \partial \Ddot { \pmb { r } } } { \partial \pmb { r } } = - G M \left( \frac { 1 } { | \pmb { r } - \pmb { s } | ^ { 3 } } \mathbf { 1 } _ { 3 \times 3 } - 3 ( \pmb { r } - \pmb { s } ) \frac { ( \pmb { r } - \pmb { s } ) ^ { T } } { | \pmb { r } - \pmb { s } | ^ { 5 } } \right)
$$

in analogy with (7.56). The derivatives with respect to the solar or lunar mass $M$ may easily be computed from

$$
\frac { \partial \ddot { r } } { \partial G M } = \frac { 1 } { G M } \ddot { r }
$$

but are again only required in special applications.

# 7.3.3 Solar Radiation Pressure

For the most common solar radiation pressure model (3.75) the resulting acceleration varies with the satellite position in the same way as the gravitational attraction of the Sun. The corresponding partial derivatives are therefore given by

$$
\frac { \partial \ddot { r } } { \partial r } = + P _ { \odot } C _ { r } \frac { A } { m } \mathrm { A U } ^ { 2 } \left( \frac { 1 } { | r - s | ^ { 3 } } \mathbf { 1 } _ { 3 \times 3 } - 3 ( r - s ) \frac { ( r - s ) ^ { T } } { | r - s | ^ { 5 } } \right) .
$$

Here $r$ and $\pmb { S }$ are the geocentric coordinates of the satellite and the Sun, respectively.

Due to the large distance of the Sun this contribution to the variational equations is quite small and may therefore safely be neglected in most applications. What is more important, however, is the partial derivative

$$
\frac { \partial \ddot { r } } { C _ { r } } \ : = \ : \frac { 1 } { C _ { r } } \ddot { r } \ : = \ : - P _ { \odot } \frac { A } { m } \frac { r _ { \odot } } { r _ { \odot } ^ { 3 } } \mathrm { A U } ^ { 2 } ,
$$

which is required to compute the influence of variations in the radiation pressure coefficient on the satellite trajectory. This allows the estimation of $C _ { r }$ during an orbit determination, which cannot usually be predicted accurately enough from material constants and the satellite geometry.

# 7.3.4 Drag

Starting from the basic expression

$$
\ddot { \boldsymbol { r } } = - \frac { 1 } { 2 } C _ { D } \frac { \boldsymbol { A } } { m } \rho \boldsymbol { v } _ { r } \pmb { v } _ { r } \quad \mathrm { w i t h } \quad \pmb { v } _ { r } = \pmb { v } - \omega _ { \oplus } \times \boldsymbol { r }
$$

for the acceleration due to atmospheric drag (cf. Sect. 3.5) one easily obtains the derivative with respect to the drag coefficient as

$$
{ \frac { \partial \ddot { r } } { \partial C _ { D } } } = - { \frac { 1 } { 2 } } { \frac { A } { m } } \rho v _ { r } { \pmb v } _ { r } .
$$

Furthermore, the dependence on the spacecraft velocity is described by the partial derivatives

$$
\frac { \partial \ddot { r } } { \partial v } = - \frac { 1 } { 2 } C _ { D } \frac { A } { m } \rho \left( \frac { v _ { r } v _ { r } ^ { T } } { v _ { r } } + v _ { r } { \bf 1 } \right) .
$$

The partial derivatives with respect to position involve a direct term describing the atmospheric density variation as well as a minor contribution resulting from the changing atmospheric wind velocity:

$$
\frac { \partial \ddot { r } } { \partial r } \ = \ - \frac { 1 } { 2 } C _ { D } \frac { A } { m } v _ { r } v _ { r } \frac { \partial \rho } { \partial r } - \frac { 1 } { 2 } C _ { D } \frac { A } { m } \rho \left( \frac { v _ { r } v _ { r } ^ { T } } { v _ { r } } + v _ { r } { \bf 1 } \right) \frac { \partial v _ { r } } { \partial r } .
$$

Introducing the cross-product matrix

$$
X ( w ) \ = \ \left( \begin{array} { c c c } { { 0 } } & { { - w _ { z } } } & { { + w _ { y } } } \\ { { + w _ { z } } } & { { 0 } } & { { - w _ { x } } } \\ { { - w _ { y } } } & { { + w _ { x } } } & { { 0 } } \end{array} \right)
$$

to rewrite the cross-product term $\omega _ { \oplus } \times r$ as $X ( \omega _ { \oplus } ) r$ , one finally obtains the representation

$$
\frac { \partial \Ddot { \pmb r } } { \partial r } \ = \ - \frac { 1 } { 2 } C _ { D } \frac { A } { m } v _ { r } { v } _ { r } \frac { \partial \rho } { \partial r } \ - \ \frac { \partial \Ddot { r } } { \partial \pmb v } X ( { \pmb \omega } _ { \oplus } ) .
$$

Here $\partial \rho / \partial r$ describes the dependence of the atmospheric density on the spacecraft location. Except for simplistic models like that of Harris–Priester, the complexity of representative atmospheric density models renders the analytical computation of the density gradient extremely cumbersome. Numerical differentiation therefore provides a meaningful alternative, but care must still be taken to avoid singularities caused by a non-smooth or non-differentiable representations of the density functions.

# 7.3.5 Thrust

The thrust model developed in Sect. 3.6 represents the acceleration as a function of the total velocity increment $\varDelta v$ along a set of coordinate axes defined by the transformation matrix $E$ . Considering the boost start and stop times as well as the mass profile as known quantities, the acceleration depends in a linear way on the $\varDelta v$ components that may be calibrated within an orbit determination. The corresponding derivatives are easily obtained as

$$
\frac { \partial \pmb { a } } { \partial \Delta \pmb { v } } = \frac { | \dot { m } | } { m ( t ) } \frac { 1 } { - \ln \left( 1 - \frac { | \dot { m } | \Delta t } { m _ { 0 } } \right) } \pmb { E }
$$

throughout the thrust phase and zero otherwise. In case of an inertial reference frame $E = 1$ ) the acceleration is independent of the actual spacecraft position and velocity. A more complicated situation is encountered for the co-moving, orbital

frame, where the reference axes are aligned with the instantaneous radius vector, angular momentum vector and orbital plane. Partial derivatives of the unit vectors with respect to position and velocity may then be obtained from the basic relation

$$
\frac { \partial } { \partial x } \frac { f ( x ) } { | f ( x ) | } = \frac { 1 } { f } \frac { \partial f } { \partial x } + f \frac { \partial } { \partial x } \frac { 1 } { f } = \frac { 1 } { f } \left( 1 - \frac { f f ^ { T } } { f ^ { 2 } } \right) \frac { \partial f } { \partial x } ,
$$

where $1 - f f ^ { T }$ is a rank-2 matrix spanning the plane perpendicular to $f$ . Furthermore the notation of the cross-product matrix (7.83) is used to conveniently express partial derivatives of cross-products:

$$
{ \frac { \partial ( f ( x ) \times g ( x ) ) } { \partial x } } ~ = ~ X ( f ) { \frac { \partial g ( x ) } { \partial x } } - X ( g ) { \frac { \partial f ( x ) } { \partial x } } ~ .
$$

Making use of these relations, the partial derivatives of the unit vectors

$$
\pmb { { \cal E } } ( t ) = ( e _ { 1 } , e _ { 2 } , e _ { 3 } )
$$

in radial, along-track and cross-track direction with respect to the spacecraft position are given by

$$
\begin{array} { l c l } { { \displaystyle { \frac { \partial e _ { 1 } } { \partial r } } } } & { { = } } & { { \displaystyle { \frac { 1 } { r } } ( { \bf 1 } - e _ { 1 } e _ { 1 } ^ { T } ) } } \\ { { \displaystyle { \frac { \partial e _ { 2 } } { \partial r } } } } & { { = } } & { { \displaystyle X ( e _ { 3 } ) { \frac { \partial e _ { 1 } } { \partial r } } - X ( e _ { 1 } ) { \frac { \partial e _ { 3 } } { \partial r } } } } \\ { { \displaystyle { \frac { \partial e _ { 3 } } { \partial r } } } } & { { = } } & { { \displaystyle { \frac { 1 } { | r \times v | } } ( { \bf 1 } - e _ { 3 } e _ { 3 } ^ { T } ) ~ ( - X ( v ) ) ~ . } } \end{array}
$$

Likewise

$$
\begin{array} { l c l } { { \displaystyle { \frac { \partial e _ { 1 } } { \partial v } } } } & { { = } } & { { { \bf 0 } } } \\ { { \displaystyle { \frac { \partial e _ { 2 } } { \partial v } } } } & { { = } } & { { - X ( e _ { 1 } ) { \frac { \partial e _ { 3 } } { \partial v } } } } \\ { { \displaystyle { \frac { \partial e _ { 3 } } { \partial v } } } } & { { = } } & { { \displaystyle { \frac { 1 } { | r \times v | } } ( { \bf 1 } - e _ { 3 } e _ { 3 } ^ { T } ) \ ( + X ( r ) ) } } \end{array}
$$

are the partial derivatives with respect to the satellite velocity vector.

# 7.4 Partials of the Measurements with Respect to the State Vector

In the computation of partial derivatives that describe the dependence of a measurement on the instantaneous position and velocity of the satellite one may – to first order – neglect all light-time effects and consider the geometrical measurement equations, only. Both angle and distance measurements may then be expressed as functions of the topocentric local tangent coordinates $\pmb { S }$ , which are related to the

Earth-centered, space-fixed satellite position $r$ and the Earth-fixed station coordinates $\pmb { R }$ by

$$
{ \pmb s } ( t ) = { \pmb E } ( { \pmb U } ( t ) { \pmb r } ( t ) - { \pmb R } ) .
$$

Here $U$ is again the matrix describing the transformation from space-fixed to Earthfixed coordinates, while

$$
E ~ = ~ \left( { \begin{array} { c } { e _ { \mathrm { E } } ^ { T } } \\ { e _ { \mathrm { N } } ^ { T } } \\ { e _ { \mathrm { Z } } ^ { T } } \end{array} } \right) ~ = ~ \left( { \begin{array} { c c c } { - \sin \lambda } & { + \cos \lambda } & { 0 } \\ { - \sin \varphi \cos \lambda } & { - \sin \varphi \sin \lambda } & { + \cos \varphi } \\ { + \cos \varphi \cos \lambda } & { + \cos \varphi \sin \lambda } & { + \sin \varphi } \end{array} } \right)
$$

is the orthonormal matrix made up by the east, north and zenith unit vectors. The desired partials of a range or angle measurement $z$ may then be expressed as

$$
\frac { \partial z } { \partial r } = \frac { \partial z } { \partial s } { \cal E } U .
$$

Neglecting light-time corrections and propagation effects the partial derivative of a range measurement with respect to the instantaneous position vector is therefore given by

$$
{ \frac { \partial \rho } { \partial r } } = { \frac { \partial s } { \partial r } } = { \frac { s ^ { T } } { s } } E U
$$

with $s = | s |$ , while the partials with respect to velocity vanish completely. In a similar manner one obtains the partial derivatives

$$
\frac { \partial \dot { \rho } } { \partial r } = \frac { s \dot { s } ^ { T } - \dot { s } s ^ { T } } { s ^ { 2 } } E U
$$

and

$$
\frac { \partial \dot { \rho } } { \partial v } = \frac { s ^ { T } } { s } E U
$$

of the instantaneous and geometric range rate from the relation

$$
\dot { \rho } = \dot { s } = \frac { s \dot { s } } { s } .
$$

Using the basic expressions for azimuth and elevation one may furthermore verify that

$$
\frac { \partial A } { \partial r } = \left( \frac { s _ { \mathrm { N } } } { s _ { \mathrm { E } } ^ { 2 } + s _ { \mathrm { N } } ^ { 2 } } \frac { - s _ { \mathrm { E } } } { s _ { \mathrm { E } } ^ { 2 } + s _ { \mathrm { N } } ^ { 2 } } 0 \right) E U
$$

and

$$
\begin{array} { r } { \frac { \partial E } { \partial r } = \left( \frac { - s _ { \mathrm { E } } s _ { \mathrm { Z } } } { s ^ { 2 } \sqrt { s _ { \mathrm { E } } ^ { 2 } + s _ { \mathrm { N } } ^ { 2 } } } \frac { - s _ { \mathrm { N } } s _ { \mathrm { Z } } } { s ^ { 2 } \sqrt { s _ { \mathrm { E } } ^ { 2 } + s _ { \mathrm { N } } ^ { 2 } } } \frac { \sqrt { s _ { \mathrm { E } } ^ { 2 } + s _ { \mathrm { N } } ^ { 2 } } } { s ^ { 2 } } \right) E U . } \end{array}
$$

The appropriate partials for $X$ and $Y$ -angles are given by

$$
\frac { \partial X _ { \mathrm { N S } } } { \partial r } ~ = ~ \left( \frac { s _ { \mathrm { Z } } } { s _ { \mathrm { E } } ^ { 2 } + s _ { \mathrm { Z } } ^ { 2 } } ~ \frac { - s _ { \mathrm { E } } } { s _ { \mathrm { E } } ^ { 2 } + s _ { \mathrm { Z } } ^ { 2 } } ~ 0 \right) E U
$$

and

$$
\begin{array} { r } { \frac { \partial Y _ { \mathrm { N S } } } { \partial r } = \left( \frac { - s _ { \mathrm { E } } s _ { \mathrm { N } } } { s ^ { 2 } \sqrt { s _ { \mathrm { E } } ^ { 2 } + s _ { \mathrm { Z } } ^ { 2 } } } \frac { - s _ { \mathrm { Z } } s _ { \mathrm { N } } } { s ^ { 2 } \sqrt { s _ { \mathrm { E } } ^ { 2 } + s _ { \mathrm { Z } } ^ { 2 } } } \frac { \sqrt { s _ { \mathrm { E } } ^ { 2 } + s _ { \mathrm { Z } } ^ { 2 } } } { s ^ { 2 } } \right) E U } \end{array}
$$

as well as

$$
\frac { \partial X _ { \mathrm { E W } } } { \partial r } ~ = ~ \left( \frac { s _ { \mathrm { Z } } } { s _ { \mathrm { N } } ^ { 2 } + s _ { \mathrm { Z } } ^ { 2 } } ~ \frac { + s _ { \mathrm { N } } } { s _ { \mathrm { N } } ^ { 2 } + s _ { \mathrm { Z } } ^ { 2 } } ~ 0 \right) { \cal E } U
$$

and

$$
\begin{array} { r } { \frac { \partial Y _ { \mathrm { E W } } } { \partial r } = \left( \frac { + s _ { \mathrm { N } } s _ { \mathrm { E } } } { s ^ { 2 } \sqrt { s _ { \mathrm { N } } ^ { 2 } + s _ { \mathrm { Z } } ^ { 2 } } } \frac { - s _ { \mathrm { Z } } s _ { \mathrm { E } } } { s ^ { 2 } \sqrt { s _ { \mathrm { N } } ^ { 2 } + s _ { \mathrm { Z } } ^ { 2 } } } \frac { \sqrt { s _ { \mathrm { N } } ^ { 2 } + s _ { \mathrm { Z } } ^ { 2 } } } { s ^ { 2 } } \right) E U ~ . } \end{array}
$$

As with the range measurements, the geometric angles do not depend on the velocity and the corresponding partials are equal to zero.

# 7.5 Partials with Respect to Measurement Model Parameters

The precise prediction of an observation for a given satellite position involves various measurement model parameters like station coordinates, transponder delay, antenna axis displacement and others. In order to assess the influence of small errors in these parameters or to estimate their values in an orbit determination, one requires the corresponding partial derivatives of the measurements with respect to the model parameters. Since many parameters are of interest only in specialized applications, the following discussion is restricted to station coordinates and simple bias values, which are the most commonly considered measurement model parameters.

The partial derivatives with respect to the station coordinates, which are e.g. required for geodetic purposes, follow from (7.91) and (7.93). They are closely related to the measurement partials with respect to the satellite state vector and may easily be derived from the expressions given in the previous section. Since

$$
\frac { \partial { z } } { \partial { \pmb R } } \ = \ - \frac { \partial { z } } { \partial { s } } { \pmb E } \ = \ - \frac { \partial { z } } { \partial { \pmb r } } { \pmb U } ^ { T } ,
$$

it is simply necessary to replace $E U$ in any partial $\partial z / \partial r$ by $- \pmb { E }$ to obtain the corresponding value of $\partial z / \partial R$ .

For measurement biases $q = z - z ^ { * }$ , defined as the difference between the actual measurement $z$ (affected by the bias) and the corrected (bias-free) value $z ^ { * }$ , the corresponding partial derivatives

$$
\left( { \frac { \partial z } { \partial q _ { i } } } \right)
$$

are equal to $+ 1$ (if $q _ { i } = q _ { z }$ is the bias value related to the measurement $z$ ) or 0 (if $q _ { i }$ is the bias value of some other measurement type).

# 7.6 Difference Quotient Approximations

Due to the complex structure of the partial derivatives described in this chapter the computer implementation of the corresponding formulas is quite laborious and error prone. Since a finite accuracy of the derivates is sufficient for many applications it may therefore appear preferable to replace the rigorous computation by a simple difference quotient approximation. This technique is mainly applied to the computation of the state transition and sensitivity matrix and is illustrated here for the partial derivative $\partial \mathbf { y } ( t ) / \partial C _ { r }$ of the state vector with respect to the radiation pressure coefficient.

For a given initial state $\scriptstyle { y _ { 0 } }$ and the nominal coefficient $C _ { r , 0 }$ the equation of motion is first integrated from $t _ { 0 }$ to $t$ to obtain the reference state vector ${ \bf y } ( t , { \bf y } _ { 0 } , C _ { r , 0 } )$ . In parallel a varied trajectory is computed with $C _ { r , 0 }$ replaced by $C _ { r , 0 } + \varDelta C _ { r }$ and the desired partial derivative is then obtained from the first-order difference quotient

$$
\left. \frac { \partial y ( t ) } { \partial C _ { r } } \right| _ { C _ { r } , 0 } \approx \left. \frac { y ( t , y _ { 0 } , C _ { r , 0 } + \Delta C _ { r } ) - y ( t , y _ { 0 } , C _ { r , 0 } ) } { \Delta C _ { r } } \right. .
$$

Since the reference trajectory is usually available from the treatment of the nominal orbit, the partial derivatives can be computed at the expense of an additional integration of the equation of motion with slightly varied initial conditions or parameters. The same concept may be applied to obtain the partial derivatives with respect to other force model parameters as well as the initial conditions. If multiple partials are required, the reference trajectory need only be computed once, yielding a total of $7 + { n _ { p } }$ trajectory integrations for the computation of the state vector, the state transition matrix and the sensitivity matrix.

Despite the obvious algorithmic simplicity, it must be emphasized, however, that the difference quotient approximation should only be used deliberately. One major drawback of the approach lies in the difficulty of choosing a proper value of the parameter increment $\varDelta C _ { r }$ , which is important to minimize the overall error of the approximation. If $\varepsilon$ is the relative global accuracy of the numerical integration, the total error of the partial derivative is approximately given by

$$
\varDelta \frac { \partial { \bf y } ( t ) } { \partial C _ { r } } \approx \frac { 1 } { 2 } \varDelta C _ { r } \left| \frac { \partial ^ { 2 } { \bf y } } { \partial C _ { r } ^ { 2 } } \right| + 2 \frac { \varepsilon | { \bf y } | } { \varDelta C _ { r } } .
$$

Here the first term describes the discretization error which is proportional to the increment $\varDelta C _ { r }$ and the second-order Taylor coefficient in the expansion of $y ( C _ { r } )$ . The second term results from the numerical integration errors $\varepsilon | y |$ of both the reference trajectory and the varied trajectory. Unless special provision is taken, the individual integration errors are uncorrelated and therefore additive as expressed by the leading factor of two. $\varDelta C _ { r }$ must thus be sufficiently small to avoid the linearization error described by the first term, but must be large enough to ensure a small contribution from the integration error at the same time. Since it is difficult to find a general solution to these conflicting requirements, a reasonable value of the variation $\varDelta C _ { r }$ must usually be found by experiment for a particular application. This is even more a problem for the computation of the state transition matrix, which exhibits secularly growing components. Accordingly, the optimal choice of the variations $\varDelta y _ { i }$ depends on the overall time interval considered.

The simple procedure outlined above may be replaced by more sophisticated approaches to reduce either of the individual error terms. First, a symmetric difference quotient

$$
\left. \frac { \partial { \bf y } ( t ) } { \partial C _ { r } } \right| _ { C _ { r , 0 } } \approx \frac { { \bf y } ( t , { \bf y } _ { 0 } , C _ { r , 0 } + \Delta C _ { r } / 2 ) - { \bf y } ( t , { \bf y } _ { 0 } , C _ { r , 0 } - \Delta C _ { r } / 2 ) } { \Delta C _ { r } }
$$

can be used to obtain an approximation of the derivative which is correct up to second order in $\varDelta C _ { r }$ . Event though the discretization error can thus be reduced significantly, a separate reference trajectory is now required for each parameter. The computational workload is thus approximately doubled, yielding a total of $1 + 2 ( 6 + n _ { p } )$ trajectory integrations to be carried out.

The contribution of the numerical integration error may effectively be avoided by ensuring that the integration of the reference trajectory and the varied trajectory are performed with exactly the same integration steps (Hairer et al. 1987). Aside from choosing independent integrations with a fixed-stepsize method, one may also combine the individual problems into a single, $6 \cdot ( 7 + n _ { p } )$ dimensional vector and integrate all trajectories simultaneously with appropriate setting of the initial conditions and force model parameters. While each of the individual state vectors still suffers from an integration error of approximately $\varepsilon | y |$ , the respective errors become highly correlated. As as result, their impact on the difference quotient is significantly reduced.

Similar results may further be achieved by integrating the variational equations as described earlier (cf. Sect. 7.2.3) but computing the relevant partial derivatives of the acceleration at each time steps from a numerical difference quotient. This approach provides great flexibility, since it also allows a joint use of analytical and numerical derivatives. As an example, one may wish to rigorously compute the gravity gradient from the analytical expressions described above, but refer to a difference quotient approximation for the atmospheric density gradient due to the non-availability of an appropriate analytical formulation.

Aside from the aforementioned accuracy problems, it has to be emphasized that the computation of the state transition and sensitivity matrices using difference quotient approximations is generally computationally less efficient than the rigorous treatment of the variational equations. This is due to the fact that the total effort for the numerical solution of the variational equations is governed by the evaluation of the partial derivatives of the acceleration with respect to position, velocity and force model parameters. Due to common sub-expressions that are also required for the computation of the acceleration itself, the expense for the additional solution of the variational equations is notably smaller than that of the corresponding varied trajectories. As a rule of thumb, one may expect a 2–3 times increased performance when using variational equations instead of numerical differences.

The rigorous computation of the state transition and sensitivity matrix is therefore clearly preferable to the difference quotient approximation as regards precision and efficiency. Nevertheless the partial derivatives are rarely required with full precision and one may still look for a method that yields a reasonable approximation at moderate costs. The best way to accomplish this is to neglect small perturbations in the computation of the variational equations. Good results may e.g. be obtained by restricting the partials $\partial \pmb { a } / \partial \pmb { r }$ of the acceleration with respect to the satellite position to terms involving the low-order geopotential coefficients (Ballani 1988). In this case the computational effort for the evaluation of the variational equations and the integration of the transition and sensitivity matrix may be reduced considerably at the expense of a moderate loss in accuracy. Since the choice of the force model considered in the variational equations is essentially free, the method may individually be adapted to the accuracy and run-time requirements of a particular application. For further discussion and relevant caveats the reader is again referred to Sect. 7.2.3.

# Exercises

Exercise 7.1 (State Transition Matrix) Compute the state transition matrix for a near-circular orbit with osculating elements $a = R _ { \oplus } + 6 5 0 \mathrm { k m }$ , $e = 0 . 0 0 1 , i = 5 1 ^ { \circ }$ and $\Omega = \omega = M = 0 ^ { \circ }$ at the initial epoch J2000 over a time interval of one day, considering (a) Keplerian motion, (b) Earth oblateness and (c) a full $1 0 \times 1 0$ gravity model. Evaluate the accuracy of approximations (a) and (b) in comparison with the rigorous solution (c).

Hint: Choose a modified time scale $\tau = \sqrt { G M _ { \oplus } / a ^ { 3 } } \cdot t$ in the representation of the state transition matrices to obtain a uniform scaling of the position and velocity terms. The accuracy of a simplified transition matrix $\tilde { \Phi }$ can be assessed via the norm of the matrix

$$
M ( \tilde { \Phi } ) = 1 - \phi \tilde { \Phi } ^ { - 1 } .
$$

It describes how well a state error $\varDelta \mathbfit { y }$ at time $t$ can be corrected by an appropriate change $\varDelta y _ { 0 } = \tilde { \Phi } ^ { - 1 } \varDelta y$ of the epoch state vector in a differential correction process. Ideally, all elements of $M$ are zero if $\tilde { \Phi }$ matches the rigorous transition matrix $\Phi$ .

Matrix elements up to 0.1 can generally be tolerated, implying that each step of a differential correction process yields a $10 \%$ reduction of the residuals. Values of 1.0 or larger in contrast imply that the correction of the epoch state computed with the approximate transition matrix is completely in error and ultimately results in divergence of the correction process.

Solution: The integration of the variational equations for the full gravity model yields the following state transition matrix at $t = 8 6 4 0 0 \mathrm { s }$ after normalization of the velocity components:

<table><tr><td>(-279.76389 Φ=</td><td>-0.61436</td><td>-0.77128</td><td>-1.97749</td><td>-176.76882</td><td>-218.58094)</td></tr><tr><td>5.44482</td><td>0.46365</td><td>0.46751</td><td>0.67732</td><td>2.85186</td><td>4.76225</td></tr><tr><td>-20.31820</td><td>0.40525</td><td>0.58659</td><td>0.64261</td><td>-12.32589</td><td>-16.24931</td></tr><tr><td>9.26340</td><td>0.69774</td><td>0.76639</td><td>1.06876</td><td>5.85008</td><td>7.23464</td></tr><tr><td>-176.39686</td><td>0.19895</td><td>-0.98557</td><td>-1.26867</td><td>-111.02555</td><td>-137.36300</td></tr><tr><td>-216.94806</td><td>-0.92156</td><td>-0.14293</td><td>-1.46183</td><td>-136.56202</td><td>-168.92823</td></tr></table>

A similar result is obtained for the reduced force model accounting only for the second-order zonal gravity coefficient:

<table><tr><td rowspan="7">J2=</td><td rowspan="7">（-279.73142 4.94588</td><td>-0.61300</td><td>-0.76831</td><td>-1.97488</td><td>-176.73944</td><td>-218.54595)</td></tr><tr><td>0.46436</td><td>0.46459</td><td>0.67371</td><td>2.53764</td><td>4.37347</td></tr><tr><td>-20.94583 0.40252</td><td>0.58628</td><td>0.63834</td><td>-12.72045</td><td>-16.73746</td></tr><tr><td>10.08752 0.69945</td><td>0.76835</td><td>1.07427</td><td>6.37036</td><td>7.87800</td></tr><tr><td>-176.42392 0.20077</td><td>-0.98205</td><td>-1.26529</td><td>-111.03517</td><td>-137.37942</td></tr><tr><td>-216.90555 -0.91896</td><td>-0.13879</td><td>-1.45733</td><td>-136.52976</td><td>-168.88617</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr></table>

Finally the analytical solution of the Keplerian state transition matrix is given by:

<table><tr><td rowspan="6">Kep</td><td rowspan="6">-279.15804 15.74647 19.44527</td><td>-0.68758</td><td>-0.84909</td><td>-2.08471</td><td>-176.75552</td><td>-218.27488)</td></tr><tr><td>0.37945</td><td>0.58939</td><td>0.75689</td><td>9.33762</td><td>12.75888</td></tr><tr><td>0.58939</td><td>0.63001</td><td>0.93468</td><td>12.75888</td><td>14.76158</td></tr><tr><td>-28.38266 0.55643</td><td>0.68713</td><td>0.78578</td><td>-17.96557</td><td>-22.18563</td></tr><tr><td>-174.82513 0.13049</td><td>-1.06908</td><td>-1.37290</td><td>-110.35739</td><td>-136.16070</td></tr><tr><td>-215.89105 -1.06908</td><td>-0.32400</td><td>-1.69539</td><td>-136.16070</td><td>-168.24110</td></tr></table>

Significant relative errors may here be observed in the third and fourth lines, which even exhibit an erroneous sign in the major elements. Upon evaluating the above matrix functional for $\tilde { \Phi } _ { \mathrm { J } 2 }$ and $\tilde { \Phi } _ { \mathrm { K e p } }$ , one obtains maximum elements $m = \operatorname* { m a x } _ { i , j } ( M _ { i , j } )$ of 0.18 and 1.01, respectively. This quantifies that the accuracy of the $J _ { 2 }$ transition matrix is just about acceptable over the concerned time frame, whereas the Keplerian approximation is clearly inadequate. Defining a threshold of $m = 0 . 1$ , the Keplerian state transition matrix is applicable for slightly more than two hours, whereas the $J _ { 2 }$ model is valid for almost 18 hours.

# 8. Orbit Determination and Parameter Estimation

The equation of motion and the measurement model provide the basic framework for describing the motion of a satellite with respect to a ground station. Given an initial position and velocity vector and various model parameters the satellite’s position and the expected observations can be computed at arbitrary times. Even though an orbit prediction may require lengthy and time-consuming computations in case of high accuracy requirements, it does not pose any algorithmic difficulties, as outlined in the previous chapters. The situation becomes more involved, however, if one tries to solve the inverse problem, namely the determination of orbital elements and model parameters from a given set of observations of the satellite.

Depending on the application, it is customary to distinguish between preliminary orbit determination used for the direct computation of six orbital elements from six observations with no a priori knowledge of the spacecraft orbit and orbit estimation (or differential correction) used for the improvement of a priori orbital elements from a large set of tracking data. The need for a distinction between both approaches arises essentially from two reasons. First of all the complex mathematical formulation of orbit prediction and measurement modeling does not allow a direct inversion except for the simplified case of Keplerian orbits and a coarse measurement model. Second, the measurements employed for an orbit determination cannot be expected to be exact quantities due to inevitable measurement (and model) errors. Some means for smoothing out these errors by considering a larger amount of tracking data than required for an initial orbit determination are therefore necessary for a reliable reconstruction of a satellite orbit from actual measurements.

While preliminary orbit determination is of great importance for solar system bodies like comets and minor planets immediately following their detection, its significance for satellite orbits is limited by regular tracking campaigns for most satellites and orbital-element databases of reasonable accuracy. Nevertheless, a preliminary orbit determination may still, for example, be required in the case of launcher injection errors or for the identification of an uncatalogued spacecraft. Most methods for preliminary orbit determination are based on Gauss’ algorithm (cf. Chap. 2) for computing orbital elements from two position vectors (i.e. from two sets of range and angle measurements) or three direction vectors (i.e from three sets of angle measurements). A comprehensive discussion of these and other analytical methods is given in Escobal (1965).

In addition to the above methods a numerical root-finding technique – the homotopy continuation method (Allgower & Georg 1990) – has, furthermore, successfully been applied to the preliminary orbit determination problem. It avoids the restrictions of analytical methods as regards the required tracking data types by solving a system of six non-linear equations that relates six arbitrary observations to the unknown orbital elements. In contrast to other root-finding methods the homotopy method may even be used with a bad initial guess of the orbital elements and is able to cope with multiple solutions. The method is e.g. employed at the Goddard Space Flight Center to support preliminary orbit determination using tracking data from both the Tracking and Data Relay Satellite System (TDRSS) and from traditional ground-based tracking stations (Kirschner et al. 1990).

In view of their importance for practical applications of satellite orbit determination, the remaining part of the chapter is devoted to the discussion of batch and sequential estimation techniques that may be used for the improvement of a priori orbit information from an arbitrary set of tracking data (Fallon 1978, Tapley 1973, Tapley 1989, Tapley et al. 2004b). While the classical batch or least-squares estimator improves an epoch state estimate by processing a whole set of observations in each run, the sequential estimator or filter processes one measurement at a time and yields subsequent estimates of the state vector at the time of each measurement.

Both batch and sequential estimators are powerful estimation methods that have successfully been applied to various types of orbit determination problems in the past. While the method of weighted least-squares dates back to the end of the $1 8 ^ { \mathrm { t h } }$ century, where it was developed for the improvement of minor planet orbits by Gauss, the Kalman filter was introduced some thirty years ago, only. Nevertheless, it was immediately recognized as a fast and efficient method that is particularly suited for on-board and real-time applications and provides a unique way of considering process noise (Leondes 1970). As an example filters have extensively been applied in the Apollo program (Battin & Levine 1970, Battin 1987) and for interplanetary navigation (Moyer 1971, Curkendall 1974, Campbell et al. 1983). The batch least-squares method, on the other hand, is traditionally used in many programs for operational and scientific orbit determination (e.g. GTDS (Long et al. 1989), GEODYN (McCarthy et al. 1993), UTOPIA (Schutz & Tapley 1980), PEPSOC (Soop 1983)), where execution time and memory considerations do not pose severe restrictions on the ground-based and off-line operation of such programs.

# 8.1 Weighted Least-Squares Estimation

The basic idea of least-squares estimation as applied to orbit determination is to find the trajectory and the model parameters for which the square of the difference between the modeled observations and the actual measurements becomes as small as possible, or, in other words, a trajectory which best fits the observations in a least-squares of the residuals sense (cf. Fig. 8.1). In actuality, since different measurements have different units and reliability, a weighting factor is applied to each residual and it is the square of the weighted residuals which is minimized. In order to arrive at a mathematical formulation of this principle let

$$
\pmb { x } ( t ) = \left( \begin{array} { c } { { \pmb { r } ( t ) } } \\ { { \pmb { v } ( t ) } } \\ { { \pmb { p } } } \\ { { \pmb q } } \end{array} \right)
$$

denote a time-dependent, $m$ -dimensional vector comprising the satellite’s position $r$ and velocity $v$ as well as the free parameters $\pmb { p }$ and $\pmb q$ that affect the force and measurement model. No distinction need then be made between trajectory and parameter estimation, which can both be treated in a unified way. The time-evolution of $\boldsymbol { x }$ may always be described by an ordinary differential equation of the form

$$
{ \dot { \pmb x } } = f ( t , { \pmb x } )
$$

and an initial value

$$
\boldsymbol { x } _ { 0 } = \boldsymbol { x } ( t _ { 0 } )
$$

at epoch $t _ { 0 }$ . Furthermore, let

$$
z = \left( \begin{array} { c } { { z _ { 1 } } } \\ { { \vdots } } \\ { { z _ { n } } } \end{array} \right)
$$

denote an $n$ -dimensional vector of measurements taken at times $t _ { 1 } , \ldots , t _ { n }$ . The observations are described by

$$
z _ { i } ( t _ { i } ) = g _ { i } ( t _ { i } , \pmb { x } ( t _ { i } ) ) + \epsilon _ { i } = h _ { i } ( t _ { i } , \pmb { x } _ { 0 } ) + \epsilon _ { i }
$$

or briefly

$$
z = h ( x _ { 0 } ) + \epsilon . 
$$

Here $g _ { i }$ denotes the model value of the $i$ th observation as a function of time $t _ { i }$ and the instantaneous state $\pmb { x } ( t _ { i } )$ , whereas $h _ { i }$ denotes the same value as a function of the state $x _ { 0 }$ at the reference epoch $t _ { 0 }$ . The quantities $\epsilon _ { i }$ account for the difference between actual and modeled observations due to measurement errors, which are usually assumed to be randomly distributed with zero mean value.

the state The least-squares orbit determination problem may now be defined as finding $\pmb { x } _ { 0 } ^ { \mathrm { l s q } }$ , that minimizes the loss function

$$
J ( { \pmb x } _ { 0 } ) = \rho ^ { T } \pmb \rho = ( \pmb z - \pmb h ( { \pmb x } _ { 0 } ) ) ^ { T } ( \pmb z - \pmb h ( { \pmb x } _ { 0 } ) )
$$

(i.e. the squared sum of the residuals $\rho _ { i }$ ) for a given set of measurements z. It is noted that the given formulation of the loss function requires all measurements to be of equal type and quality. This assumption simplifies the subsequent presentation but will later be dropped to arrive at a completely general formulation (Sect. 8.1.2). In order to avoid a non-unique determination of $x$ , it is further assumed that the number of observations $n$ is at least equal to the number of unknowns $m$ .

![](images/48a52a06c4d06c3e6f401de08144500599174585644da2e4a75232c4cbd59989.jpg)  
Fig. 8.1. Least-squares orbit determination: the parameters of a reference trajectory are corrected to find the trajectory which best fits the observations in a least-squares of the residuals sense.

# 8.1.1 Linearization and Normal Equations

The practical solution of the least-squares orbit determination problem is complicated by the fact that $\pmb { h }$ is a highly non-linear function of the unknown vector $x _ { 0 }$ , which makes it difficult or impossible to locate the minimum of the loss function without additional information. As mentioned above, an approximate value $\pmb { x } _ { 0 } ^ { \mathrm { a p r } }$ of the actual epoch state is, however, often known, which may be used to simplify the least-squares problem considerably.

Linearizing all quantities around a reference state $\pmb { x } _ { 0 } ^ { \mathrm { r e f } }$ , which is initially given by $\pmb { x } _ { 0 } ^ { \mathrm { a p r } }$ , the residual vector is approximately given by

$$
\begin{array} { r c l } { \rho } & { = } & { z - h ( x _ { 0 } ) } \\ & { \approx } & { z - h ( x _ { 0 } ^ { \mathrm { r e f } } ) - \frac { \partial { \pmb h } } { \partial { \pmb x } _ { 0 } } ( { \pmb x } _ { 0 } - { \pmb x } _ { 0 } ^ { \mathrm { r e f } } ) } \\ & { = } & { \varDelta z - { \pmb H } \varDelta { \pmb x } _ { 0 } \quad . } \end{array}
$$

Here

$$
\varDelta { { \bf { x } } _ { 0 } } = { { \bf { x } } _ { 0 } } - { { \bf { x } } _ { 0 } ^ { \mathrm { { r e f } } } }
$$

denotes the difference between $x _ { 0 }$ and the reference state, while

$$
\varDelta z = z - \pmb { h } ( \pmb { x } _ { 0 } ^ { \mathrm { r e f } } )
$$

denotes the difference between the actual observations and the observations predicted from the reference trajectory. Furthermore, the Jacobian

$$
\pmb { H } = \left. \frac { \partial \pmb { h } ( \pmb { x } _ { 0 } ) } { \partial \pmb { x } _ { 0 } } \right| _ { \pmb { x } _ { 0 } = \pmb { x } _ { 0 } ^ { \mathrm { r e f } } }
$$

gives the partial derivatives of the modeled observations with respect to the state vector at the reference epoch $t _ { 0 }$ . Using the above abbreviations, eqn. (8.8) provides a prediction of the measurement residual after applying a correction $\varDelta { { x } _ { 0 } }$ to the reference state and recomputing the modeled observations $\pmb { h }$ .

The orbit determination problem is now reduced to the linear least-squares problem of finding $\varDelta { { x } _ { 0 } ^ { \mathrm { { l s q } } } }$ such that

$$
J ( \varDelta \mathbf { x } _ { 0 } ) = ( \varDelta z - \pmb { H } \varDelta \mathbf { x } _ { 0 } ) ^ { T } ( \varDelta z - \pmb { H } \varDelta \mathbf { x } _ { 0 } ) \quad ,
$$

i.e., the predicted loss function after applying a correction $\varDelta { { x } _ { 0 } }$ becomes a minimum. If the Jacobian has full rank $m$ , i.e. if the columns of $\pmb { H }$ are linearly independent, this minimum is uniquely determined by the condition that the partial derivatives of $J$ with respect to $\varDelta \ v { x } _ { 0 }$ vanish:

$$
\frac { \partial ( \varDelta z - H \varDelta \mathbf { x } _ { 0 } ) ^ { T } ( \varDelta z - H \varDelta \mathbf { x } _ { 0 } ) } { \partial \varDelta \mathbf { x } _ { 0 } } \bigg | _ { \varDelta \mathbf { x } _ { 0 } = \varDelta \mathbf { x } _ { 0 } ^ { \mathrm { l s q } } } = \mathbf { 0 } \quad .
$$

Using the relation

$$
\frac { \partial \pmb { a } ^ { T } \pmb { b } } { \partial \pmb { c } } = \pmb { a } ^ { T } \frac { \partial \pmb { b } } { \partial \pmb { c } } + \pmb { b } ^ { T } \frac { \partial \pmb { a } } { \partial \pmb { c } }
$$

to compute the derivatives of $\pmb { \rho } ^ { T } \pmb { \rho }$ , the general solution of the linear least-squares problem may be written as

$$
\Delta \boldsymbol { x } _ { 0 } ^ { \mathrm { l s q } } = ( \boldsymbol { H } ^ { T } \boldsymbol { H } ) ^ { - 1 } ( \boldsymbol { H } ^ { T } \Delta z )
$$

after a proper rearrangement. The matrix ${ \pmb { H } } ^ { T } { \pmb { H } }$ is an $m$ -dimensional symmetric square matrix, which is also known as the normal equations matrix. Since $\pmb { H }$ was assumed to have full rank, the inverse of ${ \pmb { H } } ^ { T } { \pmb { H } }$ exists, even though it need not actually be computed. Instead, $\varDelta { { x } _ { 0 } ^ { \mathrm { { l s q } } } }$ may be obtained by solving the $m$ -dimensional normal equations

$$
( \pmb { H } ^ { T } \pmb { H } ) \varDelta \pmb { x } _ { 0 } ^ { \mathrm { l s q } } = ( \pmb { H } ^ { T } \varDelta z )
$$

using standard techniques for positive definite linear systems of equations (e.g.   
Cholesky’s algorithm).

Due to the non-linearity of $\pmb { h }$ , the simplified loss function differs slightly from the rigorous one and the value of $\begin{array} { r } { \pmb { x } _ { 0 } ^ { \mathrm { l s q } } = \hat { \pmb { x } } _ { 0 } ^ { \mathrm { r e f } } + \varDelta \pmb { x } _ { 0 } ^ { \mathrm { l s q } } } \end{array}$ (cf. Fig. 8.1) determined so far is not yet the exact solution of the orbit determination problem. It may, however, be further improved by substituting it for the reference value $\pmb { x } _ { 0 } ^ { \mathrm { r e f } }$ and repeating the same procedure. Based on this idea the non-linear problem can be solved by an iteration

$$
{ \pmb x } _ { 0 } ^ { j + 1 } = { \pmb x } _ { 0 } ^ { j } + ( { \pmb H } ^ { j T } { \pmb H } ^ { j } ) ^ { - 1 } { \pmb H } ^ { j T } ( z - { \pmb h } ( { \pmb x } _ { 0 } ^ { j } ) ) ~ ,
$$

which is started from $\ v { x } _ { 0 } ^ { 0 } = \ v { x } _ { 0 } ^ { \mathrm { a p r } }$ and continued until the relative change of the loss function is smaller than a prescribed tolerance for successive approximations. The Jacobian

$$
\pmb { H } ^ { j } = \left. \frac { \partial \pmb { h } ( \pmb { x } _ { 0 } ) } { \partial \pmb { x } _ { 0 } } \right| _ { \pmb { x } _ { 0 } = \pmb { x } _ { 0 } ^ { j } }
$$

should be updated in each iteration to ensure an optimum convergence, but may also be replaced by the constant value $\pmb { H } ^ { 0 }$ . Even though the number of iterations increases in this case, the total computational effort can often be reduced, due to the high amount of work that is otherwise required for the integration of the state transition matrix.

# 8.1.2 Weighting

The algorithm developed so far suffers from the fact that all observations are treated equally, even though the observation vector $z$ is generally composed of different measurement types. The accuracy of each measurement type may, however, easily be accounted for by weighting all observations with the inverse of the mean measurement error $\sigma _ { i }$ , i.e. by replacing the residuals $\rho _ { i }$ with the normalized residuals

$$
\hat { \rho } _ { i } = \frac { 1 } { \sigma _ { i } } \rho _ { i } = \frac { 1 } { \sigma _ { i } } ( z _ { i } - h _ { i } ( \pmb { x } _ { 0 } ) ) .
$$

Here $\sigma _ { i }$ should consider the total expected error in the measurement due to both random noise and systematic errors (e.g. refraction). As a result the basic leastsquares equation

$$
\Delta \boldsymbol { x } _ { 0 } ^ { \mathrm { l s q } } = ( \hat { \boldsymbol { H } } ^ { T } \hat { \boldsymbol { H } } ) ^ { - 1 } ( \hat { \boldsymbol { H } } ^ { T } \Delta \hat { \boldsymbol { z } } )
$$

remains essentially unchanged, except that $\pmb { H }$ and $\varDelta z$ are replaced by the modified values

$$
\hat { H } = S H \quad \mathrm { ~ a n d ~ } \quad \varDelta \hat { z } = S \varDelta z .
$$

Here $s$ is a square diagonal matrix

$$
S = \mathrm { d i a g } ( \sigma _ { 1 } ^ { - 1 } , . . . , \sigma _ { n } ^ { - 1 } ) = \left( \begin{array} { c c c } { { \sigma _ { 1 } ^ { - 1 } } } & { { } } & { { 0 } } \\ { { } } & { { \ddots } } & { { } } \\ { { 0 } } & { { } } & { { \sigma _ { n } ^ { - 1 } } } \end{array} \right) ,
$$

which divides the $i$ th row of a matrix or vector by $\sigma _ { i }$ upon multiplication from the left.

Alternatively the solution of the weighted least-squares problem may be written as

$$
\varDelta \mathbf { x } _ { 0 } ^ { \mathrm { l s q } } = ( \pmb { H } ^ { T } \pmb { W } \pmb { H } ) ^ { - 1 } ( \pmb { H } ^ { T } \pmb { W } \varDelta z ) \quad ,
$$

using the weighting matrix

$$
W = S ^ { 2 } = \mathrm { d i a g } ( \sigma _ { 1 } ^ { - 2 } , \dots , \sigma _ { n } ^ { - 2 } ) ~ .
$$

Both representations are equally well suited to handling uncorrelated measurement errors, which are fully described by the corresponding values $\sigma _ { i }$ . The weighting matrix may, however, also be used for correlated measurement errors, in which case W becomes a non-diagonal matrix.

# 8.1.3 Statistical Interpretation

According to the definition of the weighted least-squares orbit determination problem xlsq is the state that minimizes the weighted squared sum of the residuals. In 0 the absence of measurement and modeling errors it is obvious that $\pmb { x } _ { 0 } ^ { \mathrm { l s q } }$ is equal to the actual state, for which all residuals vanish. As soon as the observations are affected by measurement errors, the question arises, however, in which way these errors influence the least-squares solution.

For this purpose let $x _ { 0 }$ and $\epsilon$ denote the actual state and the measurement errors. The observation vector is then given by

$$
z = h ( x _ { 0 } ) + \epsilon \quad ,
$$

which may be linearized to obtain

$$
\begin{array} { r } { \varDelta z = H ( { \boldsymbol { { \mathbf { \mathit { x } } } } } _ { 0 } - { \boldsymbol { \mathbf { \mathit { x } } } } _ { 0 } ^ { \mathrm { r e f } } ) + \epsilon \quad , } \end{array}
$$

where $\pmb { x } _ { 0 } ^ { \mathrm { r e f } }$ is a reference state sufficiently close to $x _ { 0 }$ . The solution of the corresponding least-squares problem is given by

$$
\begin{array} { r l r } { { \pmb x } _ { 0 } ^ { \mathrm { l s q } } } & { = } & { { \pmb x } _ { 0 } ^ { \mathrm { r e f } } + ( { \pmb H } ^ { T } { \pmb W } { \pmb H } ) ^ { - 1 } ( { \pmb H } ^ { T } { \pmb W } \varDelta z ) } \\ & { = } & { { \pmb x } _ { 0 } + ( { \pmb H } ^ { T } { \pmb W } { \pmb H } ) ^ { - 1 } ( { \pmb H } ^ { T } { \pmb W } \epsilon ) ~ , } \end{array}
$$

which shows that xlsq differs from the actual state in the presence of measurement errors.

Some further results may be derived by neglecting any systematic errors and considering $\epsilon$ as a random quantity. The statistical properties of the measurement errors can then be described by the expected values1 of $\epsilon$ and $\epsilon \epsilon ^ { T }$ . These are assumed as

$$
\operatorname { E } ( \epsilon ) = \mathbf { 0 }
$$

and

$$
\begin{array} { r } { \mathrm { E } ( \epsilon \epsilon ^ { T } ) = \mathrm { d i a g } ( \sigma _ { 1 } ^ { 2 } , \dots , \sigma _ { n } ^ { 2 } ) \quad , } \end{array}
$$

which means that the expected value of each component of $\epsilon$ is zero, that all components are uncorrelated $( \underline { { \mathrm { E } } } ( \epsilon _ { i } \epsilon _ { j } ) = 0$ for $i \neq j$ ) and that the standard deviation of the $i$ th component is $\sqrt { \mathrm { E } ( \epsilon _ { i } ^ { 2 } ) } = \sigma _ { i }$ .

An immediate consequence of the first assumption is that the expected value of the least-squares solution, which is also a random variable due to its dependence on $\epsilon$ , is equal to the actual state:

$$
\begin{array} { r } { \mathrm { E } ( \pmb { x } _ { 0 } ^ { \mathrm { { l s q } } } ) = \pmb { x } _ { 0 } + ( \pmb { H } ^ { T } \pmb { W } \pmb { H } ) ^ { - 1 } ( \pmb { H } ^ { T } \pmb { W } \pmb { \mathrm { E } } ( \pmb { \epsilon } ) ) = \pmb { x } _ { 0 } } \end{array} .
$$

The second important result concerns the covariance of the least-squares solution, i.e. the quantity

$$
\mathrm { C o v } ( \pmb { x } _ { 0 } ^ { \mathrm { l s q } } , \pmb { x } _ { 0 } ^ { \mathrm { l s q } } ) = \mathrm { E } ( ( \pmb { x } _ { 0 } ^ { \mathrm { l s q } } - \pmb { x } _ { 0 } ) ( \pmb { x } _ { 0 } ^ { \mathrm { l s q } } - \pmb { x } _ { 0 } ) ^ { T } )
$$

that describes the mean squared deviation of $\boldsymbol { x } _ { 0 } ^ { \mathrm { l s q } }$ from the actual state. Inserting the expression for $\pmb { x } _ { 0 } ^ { \mathrm { l s q } }$ yields

$$
\mathrm { C o v } ( { \pmb x } _ { 0 } ^ { \mathrm { l s q } } , { \pmb x } _ { 0 } ^ { \mathrm { l s q } } ) = ( { \pmb H } ^ { T } W { \pmb H } ) ^ { - 1 } ( { \pmb H } ^ { T } W ) { \mathbb E } ( \epsilon \epsilon ^ { T } ) ( W { \pmb H } ) ( { \pmb H } ^ { T } W { \pmb H } ) ^ { - 1 } ,
$$

which may further be simplified, provided that the weighting matrix has been choosen in accord with the measurement standard deviation. Then

$$
W = \mathrm { d i a g } ( \sigma _ { 1 } ^ { - 2 } , \dots , \sigma _ { n } ^ { - 2 } )
$$

is the inverse of $\mathrm { E } ( \epsilon \epsilon ^ { T } )$ and the covariance matrix is given by

$$
\mathrm { C o v } ( { \pmb x } _ { 0 } ^ { \mathrm { l s q } } , { \pmb x } _ { 0 } ^ { \mathrm { l s q } } ) = ( { \pmb H } ^ { T } { \pmb W } { \pmb H } ) ^ { - 1 } \quad ,
$$

which is just the inverse of the normal equations matrix. The diagonal elements of the covariance matrix yield the standard deviation

$$
\sigma ( x _ { 0 k } ^ { \mathrm { l s q } } ) = \sqrt { \mathrm { C o v } ( x _ { 0 k } ^ { \mathrm { l s q } } , x _ { 0 k } ^ { \mathrm { l s q } } ) }
$$

of the components of $\pmb { x } _ { 0 } ^ { \mathrm { l s q } }$ , while the off-diagonal terms are a measure of the correlation between errors of individual components.

![](images/4c911a3d88bb41dbf2cedc74d8e64ec4ba0a9116f0f4b8a85c6f8e4e69980c70.jpg)  
Fig. 8.2. Probability distribution of the least-squares orbit determination solution in the case of normally distributed measurement errors. The shaded area covers $67 \%$ of all cases.

Even though it is obvious that the expected value and the covariance of $\pmb { x } _ { 0 } ^ { \mathrm { l s q } }$ define an interval that most likely contains the actual state $x _ { 0 }$ , some care is required to use these data for a valuation of the orbit determination accuracy. A rigorous interpretation has to account for the fact that both $\epsilon$ and $\pmb { x } _ { 0 } ^ { \mathrm { l s q } }$ are considered as random variables. The expected value and the covariance therefore describe the distribution of values xlsq0 that would be obtained in a random experiment of repeated orbit determinations for the same trajectory but with randomly generated measurement errors. If the measurement errors exhibit a normal distribution, it can be shown that there is a $67 \%$ probability that $\pmb { x } _ { 0 } ^ { \mathrm { l s q } }$ as derived from the actual measurements deviates from $x _ { 0 }$ by less than $1 \pmb { \sigma }$ and a $9 9 . 7 \%$ probability that the deviation is less than $3 \pmb { \sigma }$ (cf. Fig. 8.2). In the case of systematic errors $\bar { \epsilon }$ there will further be an additional offset of

$$
\delta \pmb { x } _ { 0 } ^ { \mathrm { l s q } } = ( \pmb { H } ^ { T } \pmb { W } \pmb { H } ) ^ { - 1 } ( \pmb { H } ^ { T } \pmb { W } \mpb { \bar { \epsilon } } ) .
$$

Concerning the use and interpretation of the covariance matrix, it is furthermore important to emphasize that its correct computation relies on the a priori knowledge of the measurement standard deviation $\sigma ( \epsilon )$ , which enters the weighting matrix $W$ . Aside from that, the covariance depends only on the partial derivatives $\pmb { H }$ and therefore on the type and distribution of measurements. The actual measurement errors, in contrast, do not affect the computation of the covariance matrix. It is therefore obvious that the covariance is not an a-posteriori measure of the tracking data quality and accuracy. This can only be derived from an analysis of the final distribution of the measurement residuals and by solving for systematic errors.

# 8.1.4 Consider Parameters

While the covariance matrix clearly provides a measure of the achievable orbit determination accuracy, it is often found to be too optimistic in the presence of systematic force and measurement model errors. This is particularly true if a large number of redundant measurements is processed, since the computed covariance is inversely proportional to the number of measurements within a given data arc. The impact of systematic errors, on the other hand, does not depend on the number of data and eventually limits the attainable orbit determination accuracy. It is, therefore, worthwhile to consider the effect of unmodeled, systematic errors in the covariance computation. With proper assumptions on the expected size of these errors, the resulting consider covariance matrix then provides realistic estimates of the achievable orbit determination accuracy.

For the mathematical treatment of systematic errors in the covariance computation, the observation vector

$$
z = h ( x _ { 0 } , c ) + \epsilon
$$

is expressed as a function of the estimation parameters $x _ { 0 }$ , the consider parameters $c$ and the measurement noise $\epsilon$ . The vector $c$ comprises those force and measurement model parameters that are supposed to be uncertain but are not adjusted as part of the least-squares estimation. Without loss of generality, the consider parameters are assumed to be small quantities with an expected value of zero. The above expression for the observation vector may then be linearized around a reference state $\pmb { x } _ { 0 } ^ { \mathrm { r e f } }$ to obtain the differential relation

$$
\begin{array} { r } { \varDelta z = H _ { x } ( \pmb { x } _ { 0 } - \pmb { x } _ { 0 } ^ { \mathrm { r e f } } ) + H _ { c } \pmb { c } + \pmb { \epsilon } \quad , } \end{array}
$$

where $\pmb { H } _ { x }$ and $\pmb { H } _ { c }$ denote the partial derivatives of the modeled measurements $\pmb { h }$ with respect to $x _ { 0 }$ and $c$ , respectively. The resulting least-squares solution

$$
\pmb { x } _ { 0 } ^ { \mathrm { l s q } } = \pmb { x } _ { 0 } + ( \pmb { H } _ { x } ^ { T } \pmb { W } \pmb { H } _ { x } ) ^ { - 1 } \pmb { H } _ { x } ^ { T } \pmb { W } ( \pmb { H } _ { c } \pmb { c } + \epsilon )
$$

differs from the true values of the estimation parameters by an offset that depends on both the consider parameters $c$ and the measurement noise $\epsilon$ .

In the sequel, the consider parameters are assumed to be random quantities with zero mean and covariance $c$ that are uncorrelated with the measurement noise $( \mathrm { E } ( c \pmb { \epsilon } ^ { T } ) = \mathbf { 0 }$ ). The expected value

$$
\begin{array} { r } { \mathrm { E } ( { \boldsymbol x } _ { 0 } ^ { \mathrm { l s q } } ) = { \boldsymbol x } _ { 0 } + ( { \pmb H } _ { x } ^ { T } W { \pmb H } _ { x } ) ^ { - 1 } { \pmb H } _ { x } ^ { T } W ( { \pmb H } _ { c } \mathrm { E } ( { \pmb c } ) + \mathrm { E } ( { \pmb \epsilon } ) ) = { \pmb x } _ { 0 } } \end{array}
$$

of the least-squares solution is then again identical to the true state. The consider covariance matrix $P ^ { \mathrm { c } }$ , however, is larger than the noise-only covariance

$$
\pmb { P } = ( \pmb { H } _ { x } ^ { T } \pmb { W } \pmb { H } _ { x } ) ^ { - 1 } \quad ,
$$

which is also designated as formal or computed covariance. It is given by

$$
\begin{array} { r c l } { { P ^ { \mathrm { c } } } } & { { = } } & { { ( P H _ { x } ^ { T } W ) ( H _ { c } C H _ { c } + \mathrm { E } ( \epsilon \epsilon ^ { T } ) ) ( P H _ { x } ^ { T } W ) ^ { T } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { P + ( P H _ { x } ^ { T } W ) ( H _ { c } C H _ { c } ^ { T } ) ( P H _ { x } ^ { T } W ) ^ { T } ~ , } } \end{array}
$$

where the weighting matrix $W$ has again been taken as the inverse of the measurement covariance.

While both the consider parameters $c$ and the measurement noise $\epsilon$ are assumed to be random quantities in the above formulation, their interpretation is different and should be carefully distinguished. Data noise affects the individual measurements processed in a single orbit determination. By adopting a large number of measurements, the impact of the data noise is effectively averaged out and the uncertainty of the estimated parameters is decreased. Consider parameters, in contrast, are assumed to be constant throughout a single orbit determination but affected by a given uncertainty. This is mapped into a corresponding uncertainty of the estimated parameters and expressed by the respective contribution to the consider covariance. As may be expected, the additive term in (8.42) does not decrease with increasing data rate, but is essentially constant for a given data arc and tracking configuration. The consider covariance calculus is therefore well suited to assessing the impact of systematic errors in the orbit determination process. Typical examples of consider parameters are measurement biases, station location errors or uncertainties in the drag and radiation pressure model.

# 8.1.5 Estimation with A Priori Information

Aside from the approximate state $\pmb { x } _ { 0 } ^ { \mathrm { a p r } }$ that is required to start the least-squares orbit determination, some information on the accuracy of this value is often available. In

order to incorporate the a priori covariance $ { \boldsymbol { P } } _ { 0 } ^ { \mathrm { a p r } }$ into the least-squares estimation an alternative representation of the loss function

$$
J = { \rho ^ { T } } \rho = { ( \varDelta z - H \varDelta x _ { 0 } ) } ^ { T } { ( \varDelta z - H \varDelta x _ { 0 } ) }
$$

is first considered, which again assumes normalized observations. Using

$$
\Delta \boldsymbol { x } _ { 0 } ^ { \mathrm { l s q } } = ( \boldsymbol { H } ^ { T } \boldsymbol { H } ) ^ { - 1 } ( \boldsymbol { H } ^ { T } \Delta z )
$$

the loss function may also be written as

$$
\begin{array} { r c l } { { J ( x _ { 0 } ) } } & { { = } } & { { ( \varDelta { \bf { x } } _ { 0 } - \varDelta { \bf { x } } _ { 0 } ^ { \mathrm { { l s q } } } ) ^ { T } ( { \cal { H } } ^ { T } { \cal { H } } ) ( \varDelta { \bf { x } } _ { 0 } - \varDelta { \bf { x } } _ { 0 } ^ { \mathrm { l s q } } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + ( \varDelta z ^ { T } \varDelta z - \varDelta { \bf { x } } _ { 0 } ^ { \mathrm { { l s q } } T } { \cal { H } } ^ { T } { \cal { H } } \varDelta { \bf { x } } _ { 0 } ^ { \mathrm { { l s q } } } ) } } \\ { { } } & { { = } } & { { ( \varDelta { \bf { \bf { \bar { \Psi } } } } - { \bf { x } } _ { 0 } ^ { \mathrm { { l s q } } } ) ^ { T } P _ { 0 } ^ { - 1 } ( { \bf { x } } _ { 0 } - { \bf { x } } _ { 0 } ^ { \mathrm { { l s q } } } ) + \mathrm { { c o n s t } } ~ , } } \end{array}
$$

which is a quadratic form of $\pmb { x } _ { 0 } - \pmb { x } _ { 0 } ^ { \mathrm { l s q } }$ defined by the inverse covariance matrix $\pmb { P } _ { 0 } ^ { - 1 } = \pmb { H } ^ { T } \pmb { H }$ of $\pmb { x } _ { 0 } - \pmb { x } _ { 0 } ^ { \mathrm { l s q } }$ . The loss-function minimum and the covariance matrix therefore provide the same information for the least-squares estimation that is otherwise contained in the measurement vector $\varDelta z$ and the partial derivative matrix $\pmb { H }$ .

As a consequence, an a priori estimate xap0 $ { \boldsymbol { { x } } } _ { 0 } ^ { \mathrm { a p r } } =  { \boldsymbol { { x } } } _ { 0 } ^ { \mathrm { r e f } } + \varDelta  { \boldsymbol { { x } } } _ { 0 } ^ { \mathrm { a p r } }$ r = xref0 + of the state $x _ { 0 }$ can be considered using a modified loss function

$$
J = ( \pmb { x } _ { 0 } - \pmb { x } _ { 0 } ^ { \mathrm { a p r } } ) ^ { T } \pmb { A } ( \pmb { x } _ { 0 } - \pmb { x } _ { 0 } ^ { \mathrm { a p r } } ) + \rho ^ { T } \pmb { \rho } \quad .
$$

Here $\pmb { \Lambda } = ( P _ { 0 } ^ { \mathrm { a p r } } ) ^ { - 1 }$ , which is also known as information matrix, is used to penalize any deviations from $\pmb { x } _ { 0 } ^ { \mathrm { a p r } }$ by an appropriate contribution to the loss function.

Since $\pmb { \varDelta }$ denotes the inverse of the covariance matrix, it is always required to be positive semi-definite. It can therefore be factored into a product $\pmb { { \cal A } } = \pmb { { \cal S } } ^ { T } \pmb { { \cal S } }$ , which is useful for locating the minimum of the combined loss function. By writing $J$ as

$$
\begin{array} { r c l } { { J } } & { { = } } & { { ( \varDelta { \bf { x } } _ { 0 } - \varDelta { \bf { x } } _ { 0 } ^ { \mathrm { a p r } } ) ^ { T } A ( \varDelta { \bf { x } } _ { 0 } - \varDelta { \bf { x } } _ { 0 } ^ { \mathrm { a p r } } ) } } \\ { { } } & { { } } & { { + ( \varDelta z - H \varDelta { \bf { x } } _ { 0 } ) ^ { T } ( \varDelta z - H \varDelta { \bf { x } } _ { 0 } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \left( \left( \begin{array} { c } { { S \varDelta { \bf { x } } _ { 0 } ^ { \mathrm { a p r } } } } \\ { { \varDelta z } } \end{array} \right) - \left( \begin{array} { c } { { S } } \\ { { H } } \end{array} \right) \varDelta { \bf { x } } _ { 0 } \right) ^ { T } \left( \left( \begin{array} { c } { { S \varDelta { \bf { x } } _ { 0 } ^ { \mathrm { a p r } } } } \\ { { \varDelta z } } \end{array} \right) - \left( \begin{array} { c } { { S } } \\ { { H } } \end{array} \right) \varDelta { \bf { x } } _ { 0 } \right) } } \end{array}
$$

it may be seen that the information matrix can be treated like additional observations and the minimum is therefore obtained as

$$
\varDelta x _ { 0 } ^ { \mathrm { l s q } } = \left( \left( \begin{array} { l } { S } \\ { H } \end{array} \right) ^ { T } \left( \begin{array} { l } { S } \\ { H } \right) \right) ^ { - 1 } \left( \begin{array} { l } { S } \\ { H } \end{array} \right) ^ { T } \left( \begin{array} { c } { S \varDelta x _ { 0 } ^ { \mathrm { a p r } } } \\ { \varDelta z } \end{array} \right) ~ , \end{array}
$$

which simplifies to

$$
\varDelta \boldsymbol { { x } } _ { 0 } ^ { \mathrm { l s q } } = ( \boldsymbol { A } + \boldsymbol { { H } } ^ { T } \boldsymbol { { H } } ) ^ { - 1 } ( \boldsymbol { A } \boldsymbol { \varDelta } \boldsymbol { { x } } _ { 0 } ^ { \mathrm { a p r } } + \boldsymbol { { H } } ^ { T } \boldsymbol { \varDelta } z ) \quad .
$$

In the case of weighted observations the least-squares solution with a priori knowledge is given by the corresponding expression

$$
\varDelta \boldsymbol { x } _ { 0 } ^ { \mathrm { l s q } } = ( \boldsymbol { A } + \boldsymbol { H } ^ { T } \boldsymbol { W } \boldsymbol { H } ) ^ { - 1 } ( \boldsymbol { A } \boldsymbol { \varDelta } \boldsymbol { x } _ { 0 } ^ { \mathrm { a p r } } + \boldsymbol { H } ^ { T } \boldsymbol { W } \boldsymbol { \varDelta } z ) \quad .
$$

Here both $\pmb { \varDelta }$ and $\pmb { H } ^ { T } \pmb { W } \pmb { H }$ may be singular matrices and it is only required that the sum of both matrices has a non-zero determinant. A non-singular information matrix is, however, sufficient to ensure that the resulting normal equations can be solved independently of $\pmb { H } ^ { T } \pmb { W } \pmb { H }$ . This feature is often employed to avoid singularities in least-squares problems by giving a small a priori weight to each estimation parameter and adding the corresponding diagonal matrix $\pmb { \varDelta }$ to the normal equations matrix.

The expected value of the estimated state (8.50) is equal to the actual state $x _ { 0 }$ , if the a priori information xapr is itself a random variable with mean value $x _ { 0 }$ . The covariance $P _ { 0 }$ of the estimate is furthermore related to the a priori covariance and the measurement information matrix by

$$
( { \pmb P } _ { 0 } ) ^ { - 1 } = ( { \pmb P } _ { 0 } ^ { \mathrm { a p r } } ) ^ { - 1 } + ( { \pmb H } ^ { T } { \pmb W } { \pmb H } ) .
$$

# 8.2 Numerical Solution of Least-Squares Problems

While the presentation given so far provides a comprehensive conceptual discussion of the least-squares method, it does not specifically address its algorithmic implementation. In the sequel, focus is therefore given to the numerical aspects of least-squares estimation, which require careful attention in practical work. Readers that are mainly interested in orbit determination methodology are advised to skip this section on first reading and continue directly with Sect. 8.3.

# 8.2.1 QR Factorization

As is evident from the mathematical formulation of the least-squares problem, the number of observations must at least be equal to the number of unknowns, but should be considerably larger to reduce the influence of individual measurement errors. A large number of observations may still, however, be insufficient, if the tracking geometry and distribution do not provide enough information on all estimation parameters. The direct solution of the normal equations2

$$
( A ^ { T } A ) \pmb { x } = A ^ { T } b
$$

will then give rise to numerical difficulties, even if the normal equations matrix is not exactly singular.

In the case of near-singularity, the solution of the normal equations becomes extremely sensitive to small errors in the normal equation matrix, which are inevitable when forming the product $A ^ { T } A$ with a limited machine accuracy. Considering, for example, the simple matrix

$$
A = { \left( \begin{array} { l l } { 1 } & { 1 } \\ { \delta } & { 0 } \\ { 0 } & { \delta } \end{array} \right) }
$$

it may easily be seen that the computed value of

$$
\pmb { A } ^ { T } \pmb { A } = \left( \begin{array} { c c } { 1 + \delta ^ { 2 } } & { 1 } \\ { 1 } & { 1 + \delta ^ { 2 } } \end{array} \right) \overset { ( \delta ^ { 2 } < \epsilon _ { \mathrm { m a c h } } ) } { \doteq } \left( \begin{array} { c c } { 1 } & { 1 } \\ { 1 } & { 1 } \end{array} \right)
$$

becomes singular, if $\delta$ is smaller than the square root of the machine accuracy $\epsilon _ { \mathrm { m a c h } }$ (cf. Golub & Reinsch 1970).

A different treatment of the least-squares problem is possible, however, that avoids the normal equations and yields the same accuracy with single-precision computer arithmetic that otherwise requires a double-precision arithmetic. It is based on a QR factorization

$$
\mathbf { A } _ { n \times m } = { \pmb { Q } } _ { n \times n } \left( { \pmb { R } } _ { m \times m } \right)
$$

of $A$ into an orthonormal matrix $\varrho$ and an upper triangular matrix $\pmb { R }$ . Since $Q ^ { T } Q =$ $Q Q ^ { T } = \mathbf { 1 }$ , the loss function may be written as

$$
\begin{array} { l l l } { { J } } & { { = } } & { { ( b - A x ) ^ { T } ( b - A x ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { ( Q ^ { T } b - Q ^ { T } A x ) ^ { T } ( Q ^ { T } b - Q ^ { T } A x ) } } \\ { { } } & { { = } } & { { \left( { \binom { d } { r } } - { \binom { R } { \bf 0 } } x \right) ^ { T } \left( { \binom { d } { r } } - { \binom { R } { \bf 0 } } x \right) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { ( d - R x ) ^ { T } ( d - R x ) + r ^ { T } r ~ , } } \end{array}
$$

where $\pmb { Q } ^ { T } \pmb { b }$ has been partitioned into two vectors $\mathbf { \Delta } _ { d }$ and $r$ of dimension $m$ and $n { - } m$ , respectively. This expression shows that $r ^ { T } r$ is the minimum of the loss function, which is reached for

$$
R x = d \quad .
$$

If $A$ has rank $m$ , the same is also true for $\pmb { R }$ and the linear system of equations

$$
\begin{array} { r } { \left( \begin{array} { c c c c c } { R _ { 1 , 1 } } & { R _ { 1 , 2 } \cdot \cdot \cdot } & { R _ { 1 , m - 1 } } & { R _ { 1 , m } } \\ { 0 } & { R _ { 2 , 1 } \cdot \cdot \cdot } & { R _ { 2 , m - 1 } } & { R _ { 2 , m } } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { \cdot \cdot \cdot R _ { m - 1 , m - 1 } } & { R _ { m - 1 , m } } \\ { 0 } & { 0 } & { \cdot \cdot \cdot } & { 0 } & { R _ { m , m } } \end{array} \right) \left( \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { m - 1 } } \\ { x _ { m } } \end{array} \right) = \left( \begin{array} { c } { d _ { 1 } } \\ { d _ { 2 } } \\ { \vdots } \\ { d _ { m - 1 } } \\ { d _ { m } } \end{array} \right) } \end{array}
$$