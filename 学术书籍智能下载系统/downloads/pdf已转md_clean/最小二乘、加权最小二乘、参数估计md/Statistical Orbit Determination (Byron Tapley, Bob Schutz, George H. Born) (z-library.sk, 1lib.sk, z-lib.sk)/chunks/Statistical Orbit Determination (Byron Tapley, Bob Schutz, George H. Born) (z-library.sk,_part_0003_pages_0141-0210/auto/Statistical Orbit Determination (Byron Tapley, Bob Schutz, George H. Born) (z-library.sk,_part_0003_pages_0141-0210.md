# Satellite-to-Satellite Tracking (SST)

Various forms of satellite-to-satellite tracking (SST) are in use. This terminology usually applies to measurements collected between a pair of satellites, but the common terminology enables identification of the respective satellite altitude. If a GPS receiver is carried on a LEO satellite, then the previously described GPS measurements would be categorized as high-low SST measurements. For some GPS satellites, an inter-satellite range measurement is made, known as cross-link ranging, that would be a high-high SST measurement.

A recent example of low-low SST measurements is represented by the Gravity Recovery And Climate Experiment (GRACE). The SST measurements are primarily used to detect components of the Earth’s gravitational field and especially gravity variations associated with redistribution of mass. Two low-altitude satellites are used and each satellite transmits signals at two frequencies in the K-band ${ ( 2 4 \mathrm { G H z } ) }$ and Ka-band $( 3 2 \mathrm { G H z } $ ), but the actual frequencies used by each satellite are not identical. The satellites have approximately the same $5 0 0 \mathrm { - k m }$ altitude and are in the same orbit plane, but separated in the along-track direction by about $2 0 0 \mathrm { k m }$ . Each satellite carries a GPS receiver, but these receivers have been modified to track both the GPS signals and the K-band signals transmitted by the other GRACE satellite.

The GRACE SST measurements in the K-band are similar to GPS one-way measurements of carrier phase made in the L-band. Two K-band measurements are made at different frequencies on each satellite to enable a correction for the ionosphere using the technique discussed in Section 3.4.2. The measurements made and recorded by each GRACE satellite are a form of one-way carrier phase similar to GPS. Each GRACE satellite carries an ultra-stable oscillator as the frequency reference $\mathrm { ( { \sim } 4 . 8 M H z }$ ) that is used to generate the transmitted signal and to mix with the signal that arrives from the other satellite. Simply stated, each satellite measures the carrier phase signal it receives from the other satellite relative to the signal that it transmits. In an approach similar to measurement differencing (Section 3.6), the measurements collected on each satellite can be added to obtain a measurement that is proportional to the range between the satellites, while at the same time removing long-term oscillator instability. This form of SST measurement has been termed dual-one-way-ranging. The measurement and instrumentation has been described by Dunn et al. (2003).

# 3.5.2 TWO-WAY RANGE

# SLR

The basic concept of a two-way range was described in Section 3.3.1. Examples of this measurement type include ground-based satellite laser ranging (SLR) systems and satellite-borne altimeters. SLR was applied for the first time by

![](images/4cade39067ab2c869d7f6132206044b360fa8590687093fd918aa1f46c94ef9c.jpg)  
Figure 3.5.3: The illustrated SLR-2000 is designed for autonomous operation, whereas previous designs have required operators. The SLR concept is based on the measurement of time-of-flight between laser pulse transmission and receipt of echo photons. The telescope collects the echo photons and the electronics provide the time-of-flight (Degnan and McGarry, 1997).

NASA Goddard Space Flight Center in 1965 to Explorer 22 (Beacon Explorer-B).

Modern SLR stations use a Nd:YAG (neodymium yttrium aluminum garnet) laser to illuminate a satellite, usually at 0.532 micrometers (green). SLR systems rely on specially designed cube corners to reflect the incoming laser light back to the source, where a telescope collects the returning photons to measure the round-trip time from pulse transmission to pulse reception. Since lasers operate in the optical wavelengths, their operation will be dependent on local weather conditions. Nevertheless, the optical cube corners carried on a satellite to support SLR are simple and completely passive.

After conversion into a distance, the question arises for purposes of the computed range: what does the measured distance represent? Clearly, the range is measured to the cube corner on the satellite that reflected the arriving photons, but the originating point in the SLR may be more complex. In some cases, the distances of the laser paths within the instrument are carefully measured and a correction to some adopted reference point is made. In other cases, the instrument may be used to range to a calibration target at a very precisely (and independently) measured distance to derive a correction to an adopted reference point. As a consequence, a range measurement represents the distance from some adopted reference point within the SLR system to a cube corner on the satellite.

The collimated laser beam has a divergence with a diameter of a few hundred meters at satellite altitude; hence, the satellite must be within the beam to achieve a successful echo. Errors that contribute to the satellite’s position with respect to the laser beam include (a) satellite position prediction and (b) the instrument’s telescope mount.

Position prediction errors result from the generation of a predicted ephemeris, usually obtained from the solution of the satellite equations of motion (e.g., Eq. 2.3.46) with a specified initial state. The initial state usually is determined from the application of the estimation techniques described in later chapters. The resulting ephemeris can be expected to contain errors from uncertainties in the force parameters in the equations of motion (e.g., the value of the drag coefficient) , errors in the force modeling, and errors in the initial conditions.

In some systems, the position prediction errors are exceeded by errors in the telescope mount, which contributes to the laser pointing direction. In such cases, an adaptive search technique may be applied during the tracking pass to compensate for all of these errors.

A concept under development by NASA for an autonomous system is illustrated in Fig. 3.5.3, known as SLR-2000, which is expected to be deployed around 2005 (Degnan and McGarry, 1997). In the SLR system, the predicted ephemeris is used to drive the laser/telescope pointing. A clock is an essential element, although different clocks may be used. A time-interval counter or an event timer is used to measure time over the short duration between the emission of the transmit, $t _ { T }$ , pulse, and the reception of the echo pulse, $t _ { R }$ . A second clock, usually synchronized to GPS-Time using a time-transfer receiver, provides the absolute time required for time tagging the measurement.

The International Laser Ranging Service (ILRS) coordinates the global operation of independent SLR stations. The global network of SLR stations is supported by national agencies, and the recorded data from these stations are made available with a few hours latency through the ILRS data centers. The range data are regularly used to monitor geocenter motion and Earth orientation, and to determine SLR station velocities.

Several satellites have been designed to support SLR geodetic science. These satellites are spherical with a small area-to-mass ratio to reduce the effects of nongravitational forces. The relation of target cross-section to altitude is evident by the characteristics of the three satellite pairs summarized in Table 3.5.2. The solution of the satellite equations of motion (Eq. 2.3.46) provide the position of the satellite center of mass in an appropriate reference frame, but the SLR measurements are made to the outer surface of the satellite, so a correction to the measured range for satellite center of mass is required. This correction is essentially the radius of the sphere, though in a precise sense it will account for the effective radius based on the laser pulse interaction with the cube corners.

Table 3.5.2:   
Geodetic Satellite “T wins”   

<table><tr><td>Satellite</td><td>Launch</td><td>Diameter (cm)</td><td>Mass (kg)</td><td>a (km)</td><td>e</td><td>i</td></tr><tr><td>Starlette</td><td>1975 France</td><td>24</td><td>47</td><td>7326</td><td>0.020</td><td>(deg) 50</td></tr><tr><td>Stella</td><td>1993 France</td><td>24</td><td>48</td><td>7184</td><td>0.001</td><td>99</td></tr><tr><td>Lageos-I</td><td>1976 U.S.</td><td>60</td><td>411</td><td>12254</td><td>0.005</td><td>110</td></tr><tr><td>Lageos-II</td><td>1992 U.S./Italy</td><td>60</td><td>405</td><td>12145</td><td>0.010</td><td>53</td></tr><tr><td>Etalon-I</td><td>1989 Soviet Union</td><td>129</td><td>1415</td><td>25514</td><td>0.001</td><td>65</td></tr><tr><td>Etalon-II</td><td>1989 Soviet Union</td><td>129</td><td>1415</td><td>25490</td><td>0.001</td><td>65</td></tr></table>

Lageos: LAser GEOdynamics Satellite Etalon satellites are in GLONASS orbit planes

Nonspherical satellites, such as TOPEX/Poseidon and ICESat, carry arrays of cube corners to support SLR tracking. These arrays usually mount the cube corners in some hemispheric-like pattern to enable ranging returns from the expected SLR directions. The array carried on ICESat is shown in Fig. 3.5.4. The necessary corrections from the SLR array optical center to the satellite center of mass are obviously more complicated than those for a spherical satellite.

The single shot precision of modern SLR systems is better than $1 \mathrm { { c m } }$ , which is usually representative of the measurement accuracy from the hardware viewpoint. Another interpretation of accuracy, however, involves the application of all corrections in the orbit determination process. Orbits determined for Lageos-I from SLR, for example, usually are characterized with an accuracy at the centimeter level, in an RMS sense.

# PRARE

Another modern two-way ranging system was developed in Germany and carried for the first time on the European Earth Resources Satellites (ERS), known as ERS-1 and ERS-2. PRARE (Precise Range and Range Rate Equipment) places the primary transmitter and receiver in the satellite, but ground stations have both transmit/receive functions as well. Two signals are transmitted by the satelliteborne PRARE, one at $2 . 2 \ : \mathrm { G H z }$ (S-band) and the other at $8 . 5 \ : \mathrm { G H z }$ (X-band), and both signals have a PRN code imposed. The time delay between the two frequencies is determined by the ground receiver and transmitted to the satellite. The received X-band signal is retransmitted to the satellite on a 7.2-GHz carrier frequency with the PRN code. A two-way range is obtained in X-band by measurement of the transmit and receive times of the X-band signal. The ionosphere correction is applied with the ground-transmitted determination based on the downlink signal. A one-way Doppler measurement is also made using the X-band.

![](images/03d3b8c0c558fcfaeb4a6a9def463fcca846015cce97222c981629ac813f970b.jpg)  
Figure 3.5.4: The ICESat SLR array. The circular components on each fla t face contain a cube corner with the optical property of reflecting incoming light back to the source. There are nine corner cubes, each with a diameter of $3 . 2 \mathrm { c m }$ . (Photo courtesy of ITE, Inc.)

# Altimeter

A radar altimeter, such as those carried on TOPEX/Poseidon (T/P), operates similarly to the SLR system as a two-way measurement. The altimeter sends a chirp and measures the round-trip time. The TOPEX altimeter (U.S.) operates with two frequencies to enable a correction for the ionosphere, whereas the Poseidon altimeter (France) uses a single frequency and relies on other data to provide the ionosphere correction. The TOPEX frequencies are $1 3 . 6 \ : \mathrm { G H z }$ and 5.3 GHz, and the Poseidon frequency is $1 3 . 6 5 \ : \mathrm { G H z }$ . The altimeters share a common antenna, but only one altimeter is operated at a time. The TOPEX ionosphere correction can be obtained from Eq. (3.4.12), and the antenna is shown in Fig. 3.5.5. As shown, TOPEX carried several tracking systems that supported determination of the TOPEX orbit.

![](images/452677711303e29510ab1416d21a1886f861f1a331e8e51f79803328b970e9ee.jpg)  
Figure 3.5.5: The TOPEX/Poseidon satellite. The radar altimeter antenna (A) is directed toward the Earth (nadir direction), the DORIS receiver antenna is D, the SLR array (S) consists of corner cubes mounted on the circumference of the altimeter antenna, the GPS receiver choke-ring antenna (G) is mounted at the end of a long boom to reduce multipath effects, and the TDRSS antenna is shown.

Laser altimeters, such as the Mars Orbiter Laser Altimeter (MOLA) and Earth-orbiting versions (such as the Geoscience Laser Altimeter System, or GLAS, carried on ICESat), function similarly to SLR. Both MOLA and GLAS operate with a near-infrared Nd:YAG wavelength of 1064 nanometers.

# TDRSS

It is apparent from the discussion in Section 3.2.4 that tracking measurements collected by ground-based instrumentation will be limited to those time periods when the satellite is above the horizon at the ground location. For a low-altitude satellite, say $1 0 0 0 \mathrm { k m }$ , such viewing opportunities will be limited to a few passes per day, with an individual pass duration of about 10 minutes or less. On the other hand, an appropriately positioned geosynchronous satellite always remains above a ground station’s horizon and the geosynchronous satellite will have a very broad region to view the low-altitude satellite. The NASA Tracking and Data Relay Satellite System (TDRSS) takes advantage of this latter characteristic by enabling range and range-rate measurements collected between a satellite in the TDRSS constellation and a low-altitude satellite. In principle, a constellation of three satellites in equatorial, geosynchronous orbit separated by 120 degrees can provide continuous tracking coverage of low Earth orbiters. In addition to the satellite constellation, a ground station provides the crucial link back to the ground.

The basic TDRSS constellation consists of two operational satellites with an angular separation of $1 3 0 ^ { \circ }$ , which provides $8 5 \% \mathrm { - } 1 0 0 \%$ coverage for low-altitude satellites. For redundancy, on-orbit satellite spares are included in the constellation. Most of the operational satellites and stored spares are clustered near $4 1 ^ { \circ }$ W and $1 7 1 ^ { \circ } \mathrm { ~ W ~ }$ , with one satellite at $2 7 5 ^ { \circ }$ W. The system is supported by a ground complex located at White Sands, New Mexico, with a remote extension in Guam. The constellation consisted of eight satellites in mid-2002, including some of the original satellites and two of a new generation of satellites, known as TDRS-H, -I, and $\_ \mathrm { J }$ in the prelaunch naming convention. TDRS-H was launched on June 30, 2000, and it was renamed TDRS-8 when it was accepted in October, 2001. The position of TDRS-8 is $1 7 1 ^ { \circ }$ W. TDRS-I and $\mathrm { - J }$ were launched in 2002 and were stationed at $1 5 0 ^ { \circ }$ W and $1 5 0 . 7 ^ { \circ }$ W.

With the definitions applied previously, the TDRSS employs multiway measurements. For example, a signal is transmitted from the White Sands complex to a TDRS in the K-band with a ranging code. This signal is retransmitted at the TDRS to a user satellite on S-band or K-band and, in turn, retransmitted back to the TDRS, where it is transmitted back to White Sands. Although the signal travels multiple paths, the basic observation equation is given by Eq. (3.3.10) for two-way range. In the case of TDRSS, however, corrections to this equation are required to account for delays at the respective instrumentation for signal retransmital, or transponder delays. Furthermore, the problem of determining the orbit of a user satellite is now linked to the problem of determining the orbit of the TDRS satellite used in the transmission links. It is evident that any errors in the TDRS orbit will map into errors for the user satellite, but the TDRS orbit errors may be accommodated by estimating the TDRS orbit parameters as well as those for the user satellite. For detailed discussion on orbit determination using TDRSS, see papers by Rowlands et al. (1997) , Marshall et al. (1996), and Visser and Ambrosius (1997).

# 3.5.3 DOPPLER SYSTEMS

# One-Way

A classic example of this technique has been the Navy Navigation Satellite System (NNSS) or Transit, which consisted of a constellation of several satellites in polar orbit. The NNSS began operation in the 1960s with the purpose that the constellation was to support navigation of U.S. Navy submarines. Operations in support of Navy applications ceased in the 1990s with the operational use of GPS. Each satellite carried a beacon that broadcasted signals with two frequencies for ionosphere correction: $1 5 0 ~ \mathrm { M H z }$ and $4 0 0 ~ \mathrm { M H z }$ . As described in Section 3.3.2, the receiver measured the Doppler count over specified intervals of time (e.g., 3.8 sec), thereby providing a measure of the Doppler shift or range-rate as the basic measurement for the navigation process.

In the 1970s, another spaceborne beacon was used for geodetic applications. For example, the satellite GEOS-3 carried an SLR reflector and beacons that broadcast signals at $1 6 2 \mathrm { M H z }$ and $3 2 4 ~ \mathrm { M H z }$ , as well as a single-frequency radar altimeter operating at $1 3 . 9 \mathrm { G H z }$ .

The French space agency, Centre National d’Etudes Spatiales (CNES), operates a Doppler system that utilizes ground-based beacons. In this system, the less expensive beacons are placed on the ground and a single receiver is carried on the satellite. This system, known as DORIS (Doppler Orbitography and Radio positioning Integrated by Satellite), was used for the first time on the French imaging satellite, SPOT, in the 1980s, but this application was followed by use on TOPEX/Poseidon (see Fig. 3.5.5) in the early 1990s. DORIS will be used on several satellites to be operated in the early years of the 21st century. DORIS uses two frequencies for ionosphere correction: $4 0 1 . 2 5 \mathrm { M H z }$ and $2 0 3 6 . 2 5 \mathrm { M H z }$ . DORIS measurements are usually processed as range-rate and the precision is better than $0 . 5 \ : \mathrm { m m } / \mathrm { s e c }$ .

The GPS carrier phase is another form of Doppler, although it is typically converted into a range measurement for processing. The basic measurement is usually extracted from the instrumentation as an integer number of cycles, measured since some start time, plus the fractional part of a cycle. The accumulated phase from the start time, expressed by Eq. (3.3.23), usually is converted into a distance measurement by multiplying with the wavelength of the signal (Eq. (3.5.3)), but the phase measurement can be converted into Doppler as an alternate measurement.

![](images/17965033e8ee4a77f66b806e74b281b8ba4f0d8fd65c5808b05a62641004a101.jpg)  
Figure 3.5.6: McDonald Observatory (MDO1) L1 pseudorange from PRN-6 on 19 June 1999. The uncorrected pseudorange as recorded by the receiver at a 30 second interval is shown. No pseudoranges were recorded for 200 seconds at about 67000 seconds.

![](images/e9f7caf7ac1d949f252583ddc77e3b23f147bc6bb07b91551c8ec1b1edfc3129.jpg)  
Figure 3.5.7: McDonald Observatory (MDO1) L1 carrier phase from PRN-6 on 19 June 1999. The uncorrected carrier phase as recorded by the receiver at a 30 second interval is shown. A 200 second interval where the receiver loses count of cycles is evident as the discontinuity.

# 3.5.4 EXAMPLES GPS

Figures 3.5.6 and 3.5.7 illustrate measurements acquired by a GPS receiver (known as MDO1) at McDonald Observatory, near Ft. Davis, Texas. The receiver was a TurboRogue SNR8000 with a choke-ring antenna. The data were obtained on June 19, 1999, and recorded at a 30-second interval. Figure 3.5.6 shows the L1 pseudorange, expressed in kilometers, obtained from PRN-6. The measurements were recorded by the receiver at a 30-second interval. The SNR8000 receiver performs a clock-steering, meaning that the receiver reference oscillator is changed (a disciplined oscillator) so that the clock is steered toward GPS-Time, thereby closely synchronizing the receiver with GPS-Time to better than $1 0 0 ~ \mathrm { { n s } }$ . However, the MDO1 receiver uses an externally controlled high-quality quartz reference oscillator that is also used by the SLR system (known as MLRS), which is adjusted to GPS-Time separately.

The SNR8000 is an example of a class of geodetic quality receivers available from several vendors (e.g., Trimble Navigation, Ashtech, and Leica). These receivers simultaneously track the signals from up to 12 GPS satellites. The receiver used at MDO1 could track up to eight satellites. In spite of Y-code transmission (encrypted P-code) by the GPS satellites, the receivers provide measurements of pseudorange and carrier phase on L1 and L2 at a selected time interval.

The L1 pseudorange measurement for PRN-6 as recorded by the receiver is illustrated in Fig. 3.5.6, which simply illustrates the expected pattern. Comparing this figure to the simulated case in Fig. 3.2.2 shows the expected effect of the higher altitude GPS satellite on the magnitude of the range and the point of closest approach.

The L1 carrier phase measurement for PRN-6 is illustrated in Fig. 3.5.7, where the units are in cycles. Aside from the difference in units, the carrier phase exhibits similar characteristics to the pseudorange, except for the obvious discontinuity at 67000 seconds that does not appear in the pseudorange. This discontinuity results from an event that caused the receiver to lose lock on all GPS satellites for about 200 seconds and when tracking resumes, the carrier phase count was reinitialized to zero. On the other hand, since the pseudorange is based on codecorrelation, there is no discontinuity. A discontinuity in carrier phase is referred to as cycle slip, which may produce dramatic discontinuities such as the Fig. 3.5.7 case, but they commonly produce cases where a small number of cycles are lost. Various techniques have been developed to fix cycle slips, which amount to using the carrier phase data before and after the discontinuity to estimate the integer number of cycles to adjust the data to create a continuous change in carrier phase. The data sampling of 30 seconds and the 200-second data gap make this particular cycle slip difficult to fix, but cases where the break may be a few cycles within the 30-second recording are straightforward to repair. If the cycle slip cannot be fix ed,

Table 3.5.3: ITRF-2000 Coordinates and Velocities for MDO1 and PIE1 Reference Points   

<table><tr><td>ID</td><td>P/V</td><td>x</td><td>y</td><td>2</td></tr><tr><td>MD011</td><td>P</td><td>-1329998.6780</td><td>-5328393.3870</td><td>3236504.1990</td></tr><tr><td></td><td>V</td><td>-0.0125</td><td>-0.0001</td><td>-0.0065</td></tr><tr><td>PIE12</td><td>P</td><td>-1640916.7930</td><td>-5014781.2040</td><td>3575447.1420</td></tr><tr><td></td><td>V</td><td>-0.0147</td><td>-0.0006</td><td>-0.0084</td></tr></table>

1Location: McDonald Observatory, Texas 2Location: Pie Town, New Mexico

Position $( P )$ for January 1, 1997, in meters; velocity $( V )$ in meters per year. The station velocity is caused primarily by tectonic plate motion. Since both stations are fix ed to the North American Plate, which is rotating as a rigid plate, their velocities are similar. $( x y z )$ is the ECF realized by ITRF-2000.

the single pass may be divided into two passes where the pass division occurs at the break.

The $L _ { 1 }$ carrier phase can be converted to phase-range, a form of pseudorange, by multiplying by the signal wavelength $( 1 9 \mathrm { c m } )$ . This form of the range is given in Eq. (3.3.23), where the linear term disappears when $f _ { G }$ equals $f _ { T }$ , which is the case for this receiver. Direct comparison of the phase-range to the pseudorange derived from the transmitted code (Figs. 3.5.6 and 3.5.7) shows that there is a large bias between the two forms of pseudorange. This bias is caused by an ambiguity in the phase measurement (the term $\widetilde N$ in Eq. (3.5.2)), which results from the lack of any unique feature in individual cycles that can be correlated with time. In the pseudorange measurement based on a code, the correlation with time is performed because of the unique character of the code sequence. With carrier phase measurements, various techniques have been developed for ambiguity resolution; that is, determination of $\widetilde N$ . Such techniques are attractive since the precision of phase-range is a few millimeters, whereas code pseudorange is decimeter-level. By resolving the ambiguity in the carrier phase measurement, the phase-range is significa ntly more precise than code pseudorange.

The quality of the measurements cannot be ascertained from Figs. 3.5.6 and 3.5.7, since the character is dominated by the orbital motion. For this example, the orbit position will be assumed to be known, thereby allowing a computed range, $C$ , to be obtained and the residual O-C to be generated. By removing the dominant orbital motion effect, the measurement quality (including the quality of the computed range) can be more readily exhibited.

Table 3.5.4: Contributing Errors to Figs. 3.5.8 and 3.5.9   

<table><tr><td>(0-C) Contributing Errors</td><td>Expected Error Magnitude</td></tr><tr><td>Use of geometric range</td><td>~ 100m</td></tr><tr><td>Satellite and receiver clock corrections</td><td>~ 100m</td></tr><tr><td>Selective Availability (SA)</td><td>~ 50m</td></tr><tr><td>Ionosphere and troposphere corrections</td><td>~10m</td></tr><tr><td>Transmit phase center</td><td>&lt;1m</td></tr><tr><td>Receiver phase center</td><td>&lt;0.1m</td></tr><tr><td>Receiver noise</td><td>0.5m</td></tr><tr><td>IGS ephemeris and ITRF coordinates</td><td>0.1m</td></tr></table>

Using the IGS final ephemeris and ECF coordinates of the receiver, the O-C can be computed for both code pseudorange and phase-range. For the cases described in the following paragraphs, the ITRF-2000 coordinates for the MDO1 site are given in Table 3.5.3. The time tag of each measurement recorded by this receiver is the receive time and the IGS ephemeris for the satellite is provided at an interval of $1 5 ~ \mathrm { m i n }$ . The MDO1 coordinates refer to the location of a specific reference point expressed with respect to the Earth center of mass as implied by the use of ITRF-2000. The IGS ephemeris for the PRN-6 center of mass actually refers to ITRF-97, but the difference between ITRF-97 and ITRF-2000 ephemerides is small.

The residual O-C for MDO1 is shown in Fig. 3.5.8, after removal of the computed range from the recorded pseudorange shown in Fig. 3.5.6. For this example, the computed range, $C$ , was formed in the ECF using Eq. (3.2.4), with no corrections applied. Since no corrections have been made and geometric range was used for $C$ , the error sources contributing to these residuals are summarized in Table 3.5.4.

When the residuals are computed for an IGS receiver located at Pie Town, New Mexico (known as PIE1 and located about $5 5 0 ~ \mathrm { k m }$ northwest of MDO1), strong similarities are observed. Figure 3.5.9 shows the PIE1 residuals, with the computed range formed under the same assumptions as those for MDO1 in Fig. 3.5.8. Both Figs. 3.5.8 and 3.5.9 are dominated by two characteristics: an average linear trend and periodic variations. Close inspection of the periodic variations shows that this effect is essentially identical at both receivers. Using terminology introduced later in this book, one would say that the two characteristics have a high correlation. Of the sources listed in Table 3.5.4, only Selective Availability (SA) is expected to exhibit the somewhat periodic variations shown. In fact, repeating the same experiment one year later after SA has been “turned off” shows no evidence of these variations. The direct removal of SA is limited by the fact that information about the SA characteristics is classified, which eliminates the direct removal for nonclassified applications. The usual alternate approach, which is described in a later section, is to difference Figs. 3.5.8 and 3.5.9, which removes errors that are common to both receivers, such as SA.

![](images/4c0805c462d4e592e6c9737810f265a1c26eb90a21de427d502ec337215283ee.jpg)  
Figure 3.5.8: MDO1 $L _ { 1 }$ pseudorange residuals (O-C) from 19 June 1998 for PRN6. The computed pseudorange (C) was obtained from the geometric range at signal receive time with no corrections. The one meter measurement noise is not evident at this scale since the O-C characteristics are dominated by an overall drift and high-frequency variations.

After SA, the next dominant characteristics in the residuals are the nonzero mean and the linear slope that remains after “remo val” of the mean and the periodic variations. Both the nonzero mean and the linear slope are caused by uncorrected clock errors, with some contribution from the generation of the computed range using the geometric range.

With the expectation that the receiver coordinates and the IGS ephemerides for the GPS satellites have errors at the decimeter level (see Table 3.5.4), the plots for (O-C) would show only random noise at the $5 0 \mathrm { - c m }$ level if the one-way range were properly computed from the available information, the clock errors were corrected, and the atmospheric delays were accounted for. The two receivers used in this example record pseudorange and carrier phase at a 30-second interval.

![](images/dccf087e48f6de634dd851ba8fe1f3be2cbf0bb38f628aabf9647cdfd2b1cddd.jpg)  
Figure 3.5.9: PIE1 $L - 1$ pseudorange residuals (O-C) for PRN6 from 19 June 1998. These residuals were formed with the same procedure used in Fig. 3.5.8. The high-frequency variations have a high correlation with those observed for the same time period at MDO1; therefore, these variations are not produced by the receiver. The variations are associated with Selective Availability.

If carrier phase is converted to range, the plots for (O-C) would be dominated by a very large bias: the phase ambiguity term. However, removal of the ambiguity results in residual plots with characteristics very similar to Figs. 3.5.8 and 3.5.9. Since phase-range noise is usually a few millimeters, removal of the effects described in the preceding paragraph would illustrate the low noise level. The instrument noise statistics are usually used to describe the measurement precision.

# DORIS

An example of DORIS measurements obtained from TOPEX/Poseidon is shown in Fig. 3.5.10. The data in this figure are based on a DORIS beacon located at Fairbanks, Alaska. Both DORIS frequencies were used to remove the ionosphere, but there would be no noticeable difference on the scale shown if the plot had been made using a single-frequency measurement.

# Altimeter

As previously described, the altimeter measurement is based on two-way time of flight. The altimeter antenna is directed toward the nadir and a one-way range (altitude) is formed by dividing the round-trip time-of-flight by two. The TOPEX altimeter data collected during a long pass over the Pacific (TOPEX/Poseidon Repeat Cycle 303) are shown in Fig. 3.5.11. For this example, the dual-frequency correction for the ionosphere was made, along with other corrections, at the meter level. The T/P orbit is frozen (see Chapter 2) with argument of perigee at $9 0 ^ { \circ }$ , which occurs just past 35500 seconds. As illustrated, the minimum altitude occurs near 34500 seconds, approximately corresponding to a latitude of $0 ^ { \circ }$ . The apparent contradiction of the perigee location and the minimum altitude is explained by the ellipsoidal character of the Earth, which plays a dominant role in Fig. 3.5.11, since the eccentricity of the T/P orbit is small $( < 0 . 0 0 1 )$ ).

![](images/6aed504863288061a89f304507bd2bec53f60fb0e58d9be08167fb847f572903.jpg)  
Figure 3.5.10: DORIS Range-rate from TOPEX/Poseidon on June 8, 1999.

Using an ephemeris of high accuracy for T/P, a computed altitude $( C )$ to the Earth ellipsoid can be formed. The altitude residual, O-C, can be generated and is shown in Fig. 3.5.12, using satelllite geodetic latitude for the abscissa. The geodetic latitude at $- 6 5 . 7 ^ { \circ }$ corresponds to the initial time of 32759 seconds. The residuals illustrate the profile of the ocean surface, expressed with respect to a reference ellipsoid, since this pass crosses mostly ocean.

# 3.6 DIFFERENCED MEASUREMENTS

In some cases, the measurements made by a particular technique are differenced in special ways. The differencing of the measurements removes or dimin-

![](images/9545143a923bcad3cc794435709b4268b39714af9e2590722a68371c6395356e.jpg)  
Figure 3.5.11: The TOPEX altimeter data collected during a long pass over the Pacific (TOPEX/Poseidon Repeat Cycle 303) are shown here.

ishes one or more error sources. The most common use of such differencing is with GPS pseudorange and carrier phase measurements and with altimeter measurements.

# 3.6.1 DIFFERENCED GPS MEASUREMENTS

Figures 3.5.8 and 3.5.9 show a very clear correlation in high-frequency variations in the PRN-6 pseudorange residuals collected with two receivers separated by $5 5 0 \mathrm { k m }$ , as discussed in Section 3.5.4. These variations are caused by Selective Availability (SA), an intentional dithering of the broadcasting satellite clock. SA was turned off in May 2000, but provides an excellent example of the application of differenced data. An obvious approach to removing this effect is to difference the residuals (or the measurements) shown in Figs. 3.5.8 and 3.5.9, which is referred to as a single difference $( S D )$ . In this case, the pseudorange measurements (or carrier phase) from a specific GPS satellite recorded at two different receivers can be differenced to produce:

$$
S D _ { j k } ^ { i } = \rho _ { j } ^ { i } - \rho _ { k } ^ { i }
$$

where $i$ identifies the GPS satellite, $j$ identifies one receiver, and $k$ identifies the other receiver. Alternatively, the single difference could be formed using mea-

![](images/406ea1b6541b1ed8eb2f70fa1bcc0cc6ae43af040b3f07aa93dcbb4430f39e99.jpg)  
Figure 3.5.12: The geodetic altitude residual, O-C, can be illustrated using satellite geodetic latitude for the abscissa, as shown here. The O-C is generated from the observed geodetic altitude (Fig. 3.5.11) and a computed altitude formed from a TOPEX ephemeris determined form DORIS and SLR. The residual illustrates the along-track ocean surface profile with respect to the reference ellipsoid.

surements collected by one receiver and two different satellites.

An SD residual can be formed from the a priori receiver coordinates and the given coordinates for the broadcasting satellites to generate the computed $S D$ . Hence, the SD residual is

$$
S D ( O - C ) _ { j k } ^ { i } = ( O - C ) _ { j } ^ { i } - ( O - C ) _ { k } ^ { i } ,
$$

where $O$ can be either pseudorange or carrier phase and $\mathrm { S D } ( O - C )$ represents the single difference residual using satellite $i$ and receivers $j$ and $k$ . Using Eq. (3.6.2), if the residuals shown in Fig. 3.5.8 are differenced with those in Fig. 3.5.9, the result is shown in Fig. 3.6.1, where it is evident that the SA high-frequency variations have been removed.

The single-difference residuals formed using a different satellite, PRN-30, are shown in Fig. 3.6.2. Although they are not shown, the residuals formed in the same way as Fig. 3.5.8 or 3.5.9, but using PRN-30 instead of PRN-6, exhibit similar high-frequency variations. Since the SA effect is satellite-dependent, the difference in the specific characteristics of the high-frequency variations is expected.

![](images/5f426bf954c27a54291fcbac7d75fbbd3f98137aabb3fdc989bb84c47ed6ee90.jpg)  
Figure 3.6.1: Single difference L1 pseudorange residuals formed with PRN-6, MDO1, and PIE1.

The SD behavior shown in Figs. 3.6.1 and 3.6.2 warrants further discussion. The formation of the SD has removed most of the high-frequency variations that are evident in Figs. 3.5.8 and 3.5.9. The remaining SD residuals exhibit a linear slope, a discontinuity at about 67000 sec, and some very small amplitude variations with an apparent high frequency. The remaining linear slope suggests that the effect is caused by sources that are not common in the data collected by the two receivers. Such effects include errors in the respective receiver clocks, errors contributed by atmosphere delays, and errors in the approximation of the computed range by the geometric range. Although the receiver separation of $5 5 0 \mathrm { k m }$ perhaps seems large, it is not when compared to the GPS orbit radius of 26000 km. Since both PRN-6 and PRN-30 are within view of each receiver, the lineof-sight to each satellite from the respective receiver is similar, which means that the atmospheric delays will be very similar and some portion (but not all) of the atmospheric delay will be removed in the SD formation. Errors associated with use of geometric range will partially cancel in the SD as well. However, the clock behavior of each receiver will be different and cannot be expected to cancel. As a consequence, receiver clock errors are expected to be the dominant error source that produces the linear variation in SD residuals shown in Figs. 3.6.1 and 3.6.2.

![](images/2abd23e9c2559bf9e358051de79ed1e53eb414f8cf2429bbb5cb78308b650e42.jpg)  
Figure 3.6.2: Single difference L1 pseudorange residuals formed with PRN-30, MDO1, and PIE1.

The discontinuity in Figs. 3.6.1 and 3.6.2 is another matter. This discontinuity occurs when the MDO1 receiver did not record data, but the PIE1 receiver does not show a gap in the data record. Although the precise cause of the discontinuity is not known, it appears to be associated with some event at MDO1, such as a clock anomaly related to the data gap.

The third characteristic evident in the SD residuals is an apparently small amplitude variation, which exhibits larger amplitude at the endpoints. These endpoints correlate with satellite rise and satellite set of one or both satellites. Clearly, SD measurements require that data from two satellites be available, so the difference between satellites requires that both satellites are located above the receiver horizon. The nature of these apparent high-frequency variations will become clearer in the following discussion.

The single differences for PRN-6 and PRN-30 can be further differenced to remove additional common errors. The resulting double difference (DD) is

$$
D D _ { j k } ^ { i m } = S D _ { j } ^ { i } - S D _ { k } ^ { m }
$$

![](images/98e25d19d87833d5b59641974ffda9a481a324c9d1daa3af63f0c168600738b3.jpg)  
Figure 3.6.3: Double difference L1 pseudorange residuals formed from PRN-6, PRN-30, MDO1, and PIE1.

where DD represents the DD residual, formed between satellites $i$ and $m$ , and receivers $j$ and $k$ . The DD residual can be formed by differencing the single difference residuals, for example.

Double difference residuals can be formed by differencing the data used to create the plots of Figs. 3.6.1 and 3.6.2. The corresponding pseudorange DD residuals are shown in Fig. 3.6.4. It is evident that the dominant characteristics observed in the SD residuals have disappeared and the residuals are now scattered near zero. These residuals now exhibit a more random character and the only systematic characteristic is a slight linear slope. The fact that the Fig. 3.6.4 residuals are near zero demonstrates that the coordinates of the receivers given in Table 3.5.3 and the IGS ephemerides are quite accurate. If the receiver coordinates or the satellite ephemerides contained significant errors, the resulting DD residuals would reflect those errors, though not necessarily in a one-to-one ratio.

Note these additional points from Fig. 3.6.4. The obvious scatter is referred to as a measurement noise or measurement precision. The scatter seems to increase near the initial times and the final times, which is likely caused by low elevation effects at one or both receivers where the signal-to-noise ratio is degraded.

If the SD residuals had been computed using carrier phase (converted to phase range) and if the computations had been performed in the same way as those for pseudorange described earlier, the residuals would have a large bias caused by the phase ambiguity. Without any correction for this ambiguity, the ambiguities in each of the phase range measurements would combine to produce a constant bias in the phase range DD residuals. Determination of the respective phase ambiguities is referred to as ambiguity resolution. In many cases the ambiguity may be estimated with other parameters in the estimation process. Once the phase ambiguity has been removed, either in the individual receiver/satellite measurements or as a combined term in the DD, the residuals formed after ambiguity removal would exhibit characteristics similar to Fig. 3.6.4, with the major exception that the residuals would be at the level of a few millimeters instead of the meter level evident in Fig. 3.6.4.

![](images/2051e990bcd024d9d89eb8fd1e385bf0efde8e3de2d28c97c0ee61bcb4bb18bb.jpg)  
Figure 3.6.4: Double difference L1 pseudorange residuals formed from PRN-6, PRN-30, MDO1, and PIE1.

# 3.6.2 DIFFERENCED ALTIMETER DATA

Although a satellite-borne altimeter has a distinct advantage in its global distribution of data, consideration of possible error sources when altimeter data are directly used for orbit determination suggests several disadvantages. In particular, long wavelength oceanographic features and nontemporal ocean topography can be absorbed into the orbit when altimeter data are directly used for orbit and geodetic parameter determination. The nontemporal ocean topography, mostly due to error in the global geoid, has meter-level uncertainty and is significant when decimeter radial orbit accuracy of certain satellites, such as TOPEX/Poseidon, is desired.

A technique that eliminates the altimeter dependence on the nontemporal ocean topography is the use of altimeter measurements at the points where the orbit ground track intersects. These points are referred to as crossover points, and the differenced altimeter measurements at these points are referred to as crossover measurements.

Crossovers have been valuable for the evaluation of radial orbit ephemeris error. Although the nontemporal portion of the ocean topography can be eliminated at the crossover point, the remaining temporal changes, such as ocean tide, unmodeled orbit error, short wavelength phenomena, as well as altimeter time tag error, can still be aliased into the radial orbit error on a global basis. With the exception of the geographically correlated error due to inaccuracy in the Earth’s gravity field (Christensen et al., 1994) , global computation and analysis of crossover residuals can provide valuable information about radial orbit error sources.

In order to use crossover measurements, several procedures that are unique to these measurements must be employed. First the crossover times, $t _ { i }$ and $t _ { j }$ , must be generated from a nominal orbit. This nominal orbit may have been previously determined from a least squares estimate using GPS data or ground-based tracking data such as laser range. The crossover times $t _ { i }$ and $t _ { j }$ are computed using a ground track corresponding to the nominal orbit. The final results of this step are $t _ { i }$ and $t _ { j }$ for all crossover points in the nominal ephemeris.

The crossover measurements are generated using the crossover times. Since the altimeter measurements are usually recorded at a fix ed time interval, it is rare that a measurement will exactly correspond to the crossover times $( t _ { i }$ and $t _ { j }$ ). As a consequence, the altimeter measurements in the vicinity of each crossover time are used to create a pseudo-measurement, by the application of an interpolating function evaluated at the crossover time. Candidate interpolating functions include a least squares cubic spline, but other functions may be used. Depending on the nature of the surface (such as laser altimeter data on rough land surfaces), which may produce altimeter data with more noise than on a smooth surface, care must be taken in the application of an interpolating function to minimize the effect of the noise. With pseduo-measurements at each crossover time, the crossover measurement is obtained by differencing the two measurements and the crossover is assigned two time tags, $t _ { i }$ and $t _ { j }$ . For most applications, the crossovers should be formed consistently, such as the ascending track pseudo-measurement minus the descending track pseudo-measurement. To facilitate subsequent application in the estimation process, these crossover measurements may be sorted in chronological order of the ascending track time. Additional information on altimeter crossover measurements can be found in Born et al. (1986) , Shum et al. (1990), and Lemoine et al. (2001).

# 3.7 SATELLITE POSITIONS

In some cases, the observational set may be an ephemeris of satellite positions. The estimation techniques of the following chapters can be applied to such observations. Depending on the source of the ephemeris, it may exhibit a variety of error sources that depend on the methodology used to derive the ephemeris.

A commonly used ephemeris can be readily obtained if the satellite carries a GPS receiver. The GPS receiver usually provides its position in near real time from pseudorange measurements and the ephemeris information broadcast by the GPS satellites. As described in Section 3.5.1, a GPS receiver extracts the broadcast ephemeris and clock parameters from the information superimposed on the carrier signal. Equation (3.5.1) gives the relationship for pseudorange as

$$
\tilde { \rho } = \rho + c ( \delta t _ { R } - \delta t _ { T } ) + \delta \rho _ { \mathrm { t r o p } } + \delta \rho _ { \mathrm { i o n } } + \epsilon .
$$

With a receiver carried on a LEO satellite, the GPS signals arriving at the antenna do not pass through the troposphere unless the antenna is oriented at a significa nt angle with respect to the zenith direction, so the term $\delta \rho _ { \mathrm { t r o p } }$ usually can be ignored. The ionosphere contribution, $\delta \rho _ { \mathrm { i o n } }$ , may be small at LEO satellite altitude (e.g., $< 1 0 \mathrm { c m }$ at TOPEX altitude). As a consequence, the term can be ignored for some applications, but it is required for the most demanding applications with high accuracy. For those applications where the ionosphere term is required, some GPS receiver provides two frequency measurements and the correction for the ionosphere can readily be made with Eq. (3.4.14). Another approach is to apply a model for the ionosphere if a single-frequency receiver is available, but the accuracy of the correction will be degraded with respect to the dual-frequency measurement.

The transmitter clock correction in Eq. (3.5.1), $\delta t _ { T }$ , can be determined from the set of parameters broadcast by the satellite (or from other sources) for its clock and $\rho$ is dependent on the GPS satellite position at the transmit time and the receiver position at the receive time. In the preceding equation, the unknowns are the receiver clock correction $( \delta t _ { R } )$ and the position vector of the GPS receiver carried on a LEO, which defines four unknowns. If the receiver measures the pseudorange from a minimum of four or more GPS satellites, then four equations similar to the preceding equation can be formed for each of the observed GPS satellite, which defines a system of four nonlinear algebraic equations. If more than four GPS satellites are visible, then an overdetermined system of equations exists. Such a system of equations can be solved using, for example, the Newton Raphson method. This method is described and applied to the solution of an overdetermined system of least squares equations in Section 4.3.4.

The solution for receiver position and clock offset is referred to as the navigation solution and it is commonly computed in near real time by GPS receivers, especially those designed for use on LEO satellites. Depending on the characteristics of the receiver, the accuracy of the position in the absence of Selective Availability is about 10 meters, where the error in the solution is dominated by the error in the GPS broadcast ephemerides. Nevertheless, an ephemeris formed by the navigation solution could be used as a set of observations in the application of an estimation algorithm (e.g., Thompson et al., 2002).

The navigation solution is one form of kinematic solution. As the term implies, the solution is not dependent on the dynamical description of the satellite and the equations of motion (Eq. 2.3.46) are not required. A significant advantage for some applications is the fact that this solution can be generated in near real time. Another form of kinematic solution makes use of carrier phase measurements and the resolution of ambiguities to obtain a more accurate solution (Hofmann-Wellenhof et al., 1997), but these solutions typically make use of highaccuracy GPS ephemerides, which usually preclude real-time LEO applications.

# 3.8 ANGLES

At the beginning of the space age, tracking of artifici al satellites included an extension of astronomical techniques based on the use of photographic plates. With a camera mounted on a telescope, a photographic plate was produced for a region of the sky during a specified exposure time. Since the mount would compensate for the rotation of the Earth, stars would appear as dots but celestial bodies and artificial satellites would produce a streak on the plate since they move at non-sidereal rates. The Baker-Nunn system was introduced to track satellites using photographic techniques. In the modern era, the photographic plates have been replaced by a Charge Coupled Device (CCD) camera, but the methodology remains much the same. Calibration of the camera/mount is an important part of the operation of these instruments.

A photograph of a satellite streak against a background of stars provides a set of observations that can be deduced from the location of the satellite with respect to the nearby stars. The stellar coordinates can be determined from a star catalog, such as the catalog derived from the European Space Agency Hipparcos astrometry satellite. The basic set of satellite observations derived from the stellar coordinates are right ascension and declination, typically expressed with respect to J2000. One modern application of right ascension and declination observations of a satellite is in space surveillance applications. For example, the Air Force Maui Optical and Supercomputing (AMOS) site operates several telescopes on Mt. Haleakala to support surveillance.

The remainder of the Minitrack system built to track the Vanguard satellites is now confined to the continental U.S., but this space fence (operated by the U.S. Navy to support space surveillance) provides angular measurements in terms of direction cosines. The space fence consists of a network of transmitters and receivers located along a great circle. When a satellite (including space debris) crosses the electronic fence, a set of measurements given by time and direction cosines are determined, which is introduced into a process to determine both the orbit of the object and its identity.

# 3.9 REFERENCES

Ashby, N., “Relati vity and the Global Positioning System,” Physics Today, Vol. 55, No. 5, pp. 41–47, May 2002.

Born, G. H., B. D. Tapley, and M. L. Santee, “Orbit determination using dual crossing arc altimetry,” Acta Astronautica, Vol. 13, No. 4, pp. 157–163, 1986.

Christensen, E., B. Haines, K. C. McColl, and R. S. Nerem, “Observ ations of geographically correlated orbit errors for TOPEX/Poseidon using the Global Positioning System,” Geophys. Res. Ltrs., Vol. 21, No. 19, pp. 2175–2178, Sept. 15, 1994.

Degnan, J., and J. McGarry, “SLR2000: Eyesafe and autonomous satellite laser ranging at kilohertz rates,” SPIE Vol. 3218, Laser Radar Ranging and Atmospheric Lidar Techniques, pp. 63–77, London, 1997.

Dunn, C., W. Bertiger, Y. Bar-Sever, S. Desai, B. Haines, D. Kuang, G. Franklin, I. Harris, G. Kruizinga, T. Meehan, S. Nandi, D. Nguyen, T. Rogstad, J. Thomas, J. Tien, L. Romans, M. Watkins, S. C. Wu, S. Bettadpur, and J. Kim, “Instrument of GRACE,” GPS World, Vol. 14, No. 2, pp. 16–28, February 2003.

Herring, T., “Modeli ng atmospheric delays in the analysis of space geodetic data,” in Refraction of Transatmospheric Signals in Geodesy, J. C. DeMunck and T. A. Th. Spoelstra (eds.), Netherlands Geodetic Commission Publications in Geodesy, 36, pp. 157–164, 1992.

Hofmann-Wellenhof, B., H. Lichtenegger, and J. Collins, Global Positioning System: Theory and Practice, Springer-Verlag, Wien-New York, 1997.

Leick, A., GPS Satellite Surveying, J. Wiley & Sons, Inc., New York, 2003.

Lemoine, F., D. Rowlands, S. Luthcke, N. Zelensky, D. Chinn, D. Pavlis, and G. Marr, “Precis e orbit determination of GEOSAT follow-on using satellite laser ranging and intermission altimeter crossovers,” NASA/CP-2001- 209986, Flight Mechanics Symposium, John Lynch (ed.), NASA Goddard Space Flight Center, Greenbelt, MD, pp. 377–392, June 2001.

Marini, J. W., and C. W. Murray, “C orrection of laser range tracking data for atmospheric refraction at elevations above 10 degrees,” NASA GSFC X591- 73-351, Greenbelt, MD, 1973.

Marshall, J. A., F. J. Lerch, S. B. Luthcke, R. G. Williamson, and C. Chan, “An Assessment of TDRSS for Precision Orbit Determination,” J. Astronaut. Sci., Vol. 44, No. 1, pp. 115–127, January–M arch, 1996.

Montenbruck, O., and E. Gill, Satellite Orbits: Models, Methods, and Applications, Springer-Verlag, Berlin, 2001.

Parkinson, B., J. Spilker, P. Axelrad, and P. Enge (eds.), Global Positioning System: Theory and Applications, Vols. 1–3, American Institute of Aeronautics and Astronautics, Inc., Washington DC, 1966.

Ries, J. C., C. Huang, M. M. Watkins, and B. D. Tapley, “Orbit determination in the relativistic geocentric reference frame,” J. Astronaut. Sci., Vol. 39, No. 2, pp. 173–181, April–June 1991.

Rowlands, D. D., S. B. Luthcke, J. A. Marshall, C. M. Cox, R. G. Williamson, and S. C. Rowton, “Space Shuttle precision orbit determination in support of SLA-1 using TDRSS and GPS tracking data,” J. Astronaut. Sci., Vol. 45, No. 1, pp. 113–129, January–Marc h 1997.

Saastamoinen, J., “Atmospheric correction for the troposphere and stratosphere in radio ranging of satellites,” Geophysical Monograph Series, Vol. 15, S. Henriksen, A. Mancini, B. Chovitz (eds.), American Geophysical Union, Washington, DC, pp. 247–251, 1972.

Seeber, G., Satellite Geodesy: Foundations, Methods & Applications, Walter deGruyter, New York, 1993.

Shum, C. K., B. Zhang, B. Schutz, and B. Tapley, “Altimeter crossover methods for precise orbit determination and the mapping of geophysical parameters,” J. Astronaut. Sci., Vol. 38, No. 3, pp. 355–368, July–September 1990.

Skolnik, M.I. (ed.), Radar Handbook, McGraw-Hill, New York, 1990.

Thompson, B., M. Meek, K. Gold, P. Axelrad, G. Born, and D. Kubitschek, “Orbit determination for the QUIKSCAT spacecraft,” J. Spacecr. Rockets, Vol. 39, No. 6, pp. 852–858, November–December 2002.

Visser, P., and B. Ambrosius, “Orbit determination of TOPEX/Poseidon and TDRSS satellites using TDRSS and BRTS tracking,” Adv. Space Res., Vol. 19, pp. 1641–1644, 1997.

Wells, D., Guide GPS Positioning, Canadian GPS Associates, Fredericton, 1987.

# 3.10 EXERCISES

1. Determine the Doppler shift in frequency over a pass for:

a. TRANSIT: 150 MHz b. GPS: 1575 MHz

To simplify this problem, assume the satellite is in a posigrade equatorial orbit and the observer is located on the equator. Determine the Doppler shift when the satellite rises and sets on the observer’s local horizon and when the satellite is at closest approach to the observer.

2. The TOPEX/Poseidon spacecraft, launched in August 1992, carried a GPS receiver. At the following date and time, the receiver made the following measurements:

Date/time: 31 March 1993 02:00:00.000 (receiver time)   
GPS PRN L1 pseudorange (m) 21 −16049870.249 28 −14818339.994

From other sources, the T/P position at this time was determined to be where $( x , y , z )$ is ECF. The positions of the GPS satellites at this time were where these positions are expressed in the same reference frame as T/P.

<table><tr><td></td><td>PRN21</td><td>PRN28</td></tr><tr><td>x</td><td>10800116.93m</td><td>10414902.30</td></tr><tr><td>y</td><td>23914912.70</td><td>13538107.48</td></tr><tr><td>2</td><td>1934886.67</td><td>-20329185.40</td></tr></table>

Determine the T/P GPS receiver clock offset using both satellites. Ignore the GPS transmitter clock correction. State and justify any assumptions.

3. Repeat the example in Section 3.3.1 but use orbit altitudes of

a. Lageos $( 5 9 0 0 \mathrm { k m } )$ b. GPS $( 2 0 , 0 0 0 \mathrm { k m } )$ c. Moon (380,000 km)

# The following data apply to Exercises 4–13:

GPS Ephemerides

The following ephemerides were taken from the “IGS final ephemerides” and the format is similar to the SP-3 format used by IGS:

<table><tr><td colspan="6">*YR/MO/DA HR:MN:SEC</td></tr><tr><td>P</td><td>PRN</td><td>X</td><td>y</td><td>Z</td><td>StT</td></tr><tr><td></td><td>：</td><td></td><td></td><td></td><td></td></tr><tr><td>P</td><td>PRN</td><td>X</td><td>y</td><td>Z</td><td>8tT</td></tr></table>

where time is given in GPS-Time as

$$
{ \begin{array} { r l } & { { \mathrm { Y R } } = { \mathrm { Y e a r } } } \\ & { { \mathrm { M O } } = { \mathrm { M o n t h ~ o f ~ y e a t } } } \\ & { { \mathrm { D A } } = { \mathrm { D a y ~ o f ~ m o n t h } } } \\ & { { \mathrm { H R } } = { \mathrm { H o u r ~ o f ~ d a y } } } \\ & { { \mathrm { M N } } = { \mathrm { M i n u t e s } } } \\ & { { \mathrm { S E C } } = { \mathrm { S e c o n d s } } } \end{array} }
$$

The lines following the epoch line are

$\boldsymbol { \mathrm { P } } =$ Position ephemeris   
$\mathrm { P R N } = \mathrm { G P S }$ Satellite identifier   
$\mathrm { x , y , z = I T R F { - } 2 0 0 0 }$ position of GPS PRN, in km   
$\delta t _ { T } = \mathrm { I G S }$ -determined clock offset for PRN, in microseconds

<table><tr><td colspan="6">* 2003/7/3 5:45:0.00000000</td></tr><tr><td>P</td><td>1</td><td>4566.504088</td><td>-17778.663761</td><td>-19019.826900</td><td>292.783269</td></tr><tr><td>P</td><td>4</td><td>-10978.897783</td><td>-10863.301011</td><td>-21544.271426</td><td>44.796690</td></tr><tr><td>P</td><td>7</td><td>-16743.206878</td><td>-20415.491050</td><td>-3315.879862</td><td>556.798655</td></tr><tr><td>P</td><td>8</td><td>-4587.665320</td><td>-17960.987250</td><td>18706.552158</td><td>378.701406</td></tr><tr><td>P</td><td>11</td><td>14431.377269</td><td>-21405.604003</td><td>6070.147167</td><td>54.319645</td></tr><tr><td>P</td><td>13</td><td>-4652.983492</td><td>-23260.723995</td><td>-12070.391803</td><td>-29.105842</td></tr><tr><td>P</td><td>27</td><td>1214.284685</td><td>-23377.459743</td><td>12442.855885</td><td>377.394607</td></tr><tr><td>P</td><td>28</td><td>-14937.324209</td><td>-12545.945359</td><td>18318.739786</td><td>-28.452370</td></tr><tr><td>P</td><td>29</td><td>-17278.539907</td><td>-1224.933899</td><td>20384.228178</td><td>155.457984</td></tr><tr><td>P</td><td>31</td><td>13278.146508</td><td>-8114.211495</td><td>21225.174835</td><td>300.884498</td></tr><tr><td colspan="6">* 2003//3 6:0:0.00000000</td></tr><tr><td>P</td><td>1</td><td>5861.745350</td><td>-15901.667555</td><td>-20276.875963</td><td>292.785440</td></tr><tr><td>P</td><td>4</td><td>-9777.977569</td><td>-12987.742895</td><td>-20912.838681</td><td>44.796231</td></tr><tr><td>P</td><td>7</td><td>-16651.970525</td><td>-20805.209726</td><td>-525.893274</td><td>556.811719</td></tr><tr><td>P</td><td>8</td><td>-3449.706143</td><td>-19727.772705</td><td>17096.293643</td><td>378.709764</td></tr><tr><td>P</td><td>11</td><td>14464.812694</td><td>-20477.667957</td><td>8654.011503</td><td>54.321275</td></tr><tr><td>P</td><td>13</td><td>-3700.036312</td><td>-22089.587975</td><td>-14378.853276</td><td>-29.106054</td></tr><tr><td>P</td><td>27</td><td>1969.580616</td><td>-24408.106473</td><td>10001.540814</td><td>377.440654</td></tr><tr><td>P</td><td>28</td><td>-12810.474492</td><td>-12772.984277</td><td>19707.048914</td><td>-28.448653</td></tr><tr><td>P</td><td>29</td><td>-18461.999653</td><td>-3089.021101</td><td>19091.163769</td><td>155.460061</td></tr><tr><td>P</td><td>31</td><td>14725.051413</td><td>-6093.976687</td><td>20978.562271</td><td>300.903599</td></tr><tr><td colspan="6">* 2003/7/3 6:15:0.00000000</td></tr><tr><td>P</td><td>1</td><td>7328.259794</td><td>-13996.483360</td><td>-21179.722738</td><td>292.788770</td></tr><tr><td>P</td><td>4</td><td>-8727.133318</td><td>-15090.465960</td><td>-19918.643118</td><td>44.795835</td></tr><tr><td>P</td><td>7</td><td>-16383.736913</td><td>-20953.296813</td><td>2273.086980</td><td>556.824434</td></tr><tr><td>P</td><td>8</td><td>-2489.551621</td><td>-21368.525118</td><td>15184.136954</td><td>378.718629</td></tr><tr><td>P</td><td>11</td><td>14449.564065</td><td>-19284.658838</td><td>11088.302121</td><td>54.322742</td></tr><tr><td>P</td><td>13</td><td>-2536.235846</td><td>-20774.358288</td><td>-16441.402012</td><td>-29.106257</td></tr><tr><td>P</td><td>27</td><td>2578.663020</td><td>-25207.610015</td><td>7386.006812</td><td>377.487071</td></tr><tr><td>P</td><td>28</td><td>-10560.925449</td><td>-13127.209192</td><td>20763.433991</td><td>-28.445536</td></tr><tr><td>P</td><td>29</td><td>-19645.300961</td><td>-4758.653980</td><td>17476.041504</td><td>155.462272</td></tr><tr><td>P</td><td>31</td><td>16233.527710</td><td>-4186.595815</td><td>20362.080900</td><td>300.922651</td></tr></table>

# Observations

The following data are given in a format that is similar to the Receiver INdependent EXchange (RINEX) format for GPS receiver observations (refer to IGS for RINEX details):

<table><tr><td>YR/MO/DA HR:MN:SEC</td><td></td><td>EF N</td><td>PRN-List</td></tr><tr><td>L1</td><td>L2</td><td>P2</td><td>P1</td></tr><tr><td>：</td><td></td><td></td><td></td></tr><tr><td>L1</td><td>L2</td><td>P2</td><td>P1</td></tr></table>

where time is given in GPS receiver time (close to GPS-Time) and

$\mathrm { Y R } = \mathrm { Y e a r }$   
$\mathbf { M O } =$ Month of year   
DA $=$ Day of month   
$\mathrm { H R } =$ Hour of day   
$\mathbf { M N } =$ Minutes   
$\mathrm { S E C = }$ Seconds   
$\mathrm { E F = }$ Epoch Flag (0 means no problem)   
$\mathbf { N } =$ Number of tracked GPS satellites   
PRN-List $=$ list of PRN-identifiers of tracked GPS satellites

The lines following the epoch line contain the observations for the PRN satellites, given in the same order as the PRN-list. In the observations:

$\mathrm { L } 1 = \mathrm { L } 1$ carrier phase (cycles) $\mathrm { L } 2 = \mathrm { L } 2$ carrier phase (cycles) ${ \bf P } 2 = { \bf L } 2$ pseudorange (meters) $\mathrm { P } 1 = \mathrm { L } 1$ pseudorange (meters)

(Note that fourth and fifth digits to right of decimal for carrier phase pertain to signal strength.)

The following data were recorded by a Black Jack receiver carried on ICE-Sat:

<table><tr><td colspan="4">2003/7/3 6:0:0.0000000 08147811132728</td></tr><tr><td>13313150.27606</td><td>10373859.94706</td><td>25276179.66000</td><td>25276168.63500</td></tr><tr><td>3638113.46106</td><td>2834889.84706</td><td>25214111.21600</td><td>25214104.18700</td></tr><tr><td>-8930705.47408</td><td>-6958991.53008</td><td>20768986.07800</td><td>20768979.92300</td></tr><tr><td>-6413864.84708</td><td>-4997816.68208</td><td>20025186.23300</td><td>20025180.71900</td></tr><tr><td>-10979121.08307</td><td>-8555158.14008</td><td>22308126.25500</td><td>22308121.45400</td></tr><tr><td>-2786774.49707</td><td>-2171514.86607</td><td>22773866.90400</td><td>22773861.60000</td></tr><tr><td>-23434105.64308</td><td>-18260340.20309</td><td>19833911.31900</td><td>19833905.82300</td></tr><tr><td>-7593037.70208</td><td>-5916651.79208</td><td>21846321.76500</td><td>21846317.42700</td></tr><tr><td colspan="4">2003/7/3 6:0:10.0000000 0814781113 27 28</td></tr><tr><td>13739083.01006</td><td>10705752.39405</td><td>25357229.60300</td><td>25357220.91900</td></tr><tr><td>3975221.46206</td><td>3097571.22406</td><td>25278260.02000</td><td>25278253.89400</td></tr><tr><td>-8829945.83208</td><td>-6880477.50608</td><td>20788159.91600</td><td>20788153.76600</td></tr><tr><td>-6629467.22309</td><td>-5165818.45908</td><td>19984158.47600</td><td>19984153.00800</td></tr><tr><td>-10987968.90807</td><td>-8562052.48708</td><td>22306442.29400</td><td>22306437.67400</td></tr><tr><td>-2390872.85807</td><td>-1863020.13207</td><td>22849204.79500</td><td>22849199.34400</td></tr><tr><td>-23466816.37608</td><td>-18285829.03209</td><td>19827686.48700</td><td>19827681.02000</td></tr><tr><td>-7876627.23108</td><td>-6137630.55108</td><td>21792356.26200</td><td>21792351.82000</td></tr><tr><td colspan="4">2003/7/3 6:4:0.0000000 08 7811 13 27 28 29 31</td></tr><tr><td>-5513215.18608</td><td>-4296011.91608</td><td>21419312.62400</td><td>21419306.89400</td></tr><tr><td>-9854402.24209</td><td>-7678754.03309</td><td>19370472.81400</td><td>19370467.60200</td></tr><tr><td>-10546995.52107</td><td>-8218436.17807</td><td>22390355.62500</td><td>22390351.48800</td></tr><tr><td>7267464.77706</td><td>5662956.04106</td><td>24687125.70900</td><td>24687120.66100</td></tr><tr><td>-22384357.99608</td><td>-17442354.31309</td><td>20033670.90000</td><td>20033665.56700</td></tr><tr><td>-13406848.48208</td><td>-10446892.85208</td><td>20739989.40200</td><td>20739985.24200</td></tr><tr><td>-4806438.03607</td><td>-3745274.75407</td><td>22815283.89300</td><td>22815278.35000</td></tr><tr><td>-1904315.82106</td><td>-1483881.67706</td><td>23910972.26500</td><td>23910967.00200</td></tr><tr><td colspan="4">2003/7/3 6:4:10.0000000 08781113 2728 2931</td></tr><tr><td>-5327807.74108</td><td>-4151538.49708</td><td>21454594.42700</td><td>21454588.71500</td></tr><tr><td>-10500588.28407</td><td>-8182274.62907</td><td>22399186.76600</td><td>22399182.59700</td></tr><tr><td>7703560.72106</td><td>6002770.96806</td><td>24770114.33000</td><td>24770107.20000</td></tr><tr><td>-22259480.22808</td><td>-17345046.90309</td><td>20057434.39800</td><td>20057428.92100</td></tr><tr><td>-13598356.03208</td><td>-10596119.48608</td><td>20703546.53400</td><td>20703542.38700</td></tr><tr><td>-5057074.29907</td><td>-3940575.68207</td><td>22767589.44100</td><td>22767583.83300</td></tr><tr><td>-2109142.85306</td><td>-1643487.08006</td><td>23871994.45100</td><td>23871989.67700</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

The following data were collected by a Turbo Rogue GPS receiver at Pie Town (NM):

<table><tr><td>2003/7/3 6:0:0.0000000</td><td colspan="3">088 272611 29 28 317</td></tr><tr><td>-24388891.10649</td><td>-19004308.54347</td><td>19950321.918</td><td>19950319.447</td></tr><tr><td>-23612111.74249</td><td>-18399018.28147</td><td>20633681.740</td><td>20633678.842</td></tr><tr><td>-354035.84848</td><td>-275871.64045</td><td>23938856.683</td><td>23938853.490</td></tr><tr><td>-6053270.88448</td><td>-4716827.20645</td><td>22881055.819</td><td>22881053.542</td></tr><tr><td>-11945499.34248</td><td>-9308173.13145</td><td>22918548.923</td><td>22918545.380</td></tr><tr><td>-21453687.95449</td><td>-16717124.87047</td><td>21107802.248</td><td>21107800.600</td></tr><tr><td>12464204.51048</td><td>9712367.70644</td><td>23823735.311</td><td>23823729.233</td></tr><tr><td>-4481731.59449</td><td>-3492253.10746</td><td>22002748.155</td><td>22002743.741</td></tr><tr><td colspan="4">2003/7/3 6:4:0.0000000 088 27 2611 29 28 317</td></tr><tr><td>-24416407.84949</td><td>-19025750.07047</td><td>19945085.523</td><td>19945082.850</td></tr><tr><td>-23327037.21349</td><td>-18176882.46347</td><td>20687929.760</td><td>20687926.774</td></tr><tr><td>-898114.97748</td><td>-699828.98244</td><td>23835323.854</td><td>23835317.574</td></tr><tr><td>-6258015.55248</td><td>-4876368.11345</td><td>22842093.804</td><td>22842091.419</td></tr><tr><td>-12296146.77548</td><td>-9581404.44246</td><td>22851822.101</td><td>22851818.825</td></tr><tr><td>-21614641.52349</td><td>-16842543.10147</td><td>21077173.381</td><td>21077172.008</td></tr><tr><td>13324935.88948</td><td>10383067.35145</td><td>23987526.176</td><td>23987521.928</td></tr><tr><td>-5099063.91549</td><td>-3973290.68546</td><td>21885273.341</td><td>21885269.023</td></tr></table>

The following data were collected by a Turbo Rogue GPS receiver at Mc-Donald Observatory (TX):

<table><tr><td>2003/7/3 6:0:0.0000000</td><td colspan="3">08 292711813 26287</td></tr><tr><td>-9944212.12448</td><td>-7748726.63345</td><td>23401416.592</td><td>23401412.281</td></tr><tr><td>-24875552.81149</td><td>-19383519.73947</td><td>20395733.147</td><td>20395730.434</td></tr><tr><td>-11346725.95449</td><td>-8841595.17445</td><td>22528013.534</td><td>22528011.897</td></tr><tr><td>-28075193.49449</td><td>-21876748.09447</td><td>19982685.387</td><td>19982683.005</td></tr><tr><td>-4164302.39448</td><td></td><td></td><td>24437530.876</td></tr><tr><td>-2296772.12848</td><td></td><td></td><td>24480165.844</td></tr><tr><td>-18590371.83649</td><td>-14485969.70246</td><td>21419438.945</td><td>21419437.517</td></tr><tr><td>-16001981.31449</td><td>-12469051.09846</td><td>21932274.397</td><td>21932270.319</td></tr><tr><td>2003/7/3 6:4:0.0000000</td><td colspan="3">08 292711813 26287</td></tr><tr><td>-10328700.49948</td><td>-8048327.52545</td><td>23328248.166</td><td>23328245.981</td></tr><tr><td>-24679310.88249</td><td>-19230604.03647</td><td>20433076.681</td><td>20433074.090</td></tr><tr><td>-11480544.84549</td><td>-8945869.42745</td><td>22502548.387</td><td>22502546.906</td></tr><tr><td>-28204694.64049</td><td>-21977658.03247</td><td>19958042.069</td><td>19958039.765</td></tr><tr><td>-3297123.18548</td><td></td><td></td><td>24602548.472</td></tr><tr><td>-2850548.61348</td><td>-2221193.01544</td><td>24374788.863</td><td>24374785.477</td></tr><tr><td>-18774076.61449</td><td>-14629116.05246</td><td>21384480.700</td><td>21384479.692</td></tr><tr><td>-16569301.13749</td><td>-12911117.94346</td><td>21824316.532</td><td>21824312.371</td></tr></table>

4. Use the ICESat data for any of the given epochs to determine:

a. ionosphere-free pseudoranges for each satellite b. ionosphere correction to the L1 pseudoranges c. convert carrier phase to “phase range” d. ionosphere-free phase ranges for all satellites

5. Use the ICESat data separated by 10 sec and by 4 min to determine:

a. range change over the respective time interval from pseudorange and phase range   
b. an approximate value of phase range ambiguity for each observed GPS. satellite

6. a. Determine an ICESat position at 06:00:00.000000 (and any other relevant parameters). Provide justification for the solved for parameter set and identify the measurements used. Strive for highest accuracy. Use all observed satellites, but provide justification for any satellites that should be edited from the solution. Identify and justify assumptions. b. Provide the O-C for each of the satellites used in a. c. Determine the azimuth and elevation of each GPS satellite with respect to the ICESat local horizontal plane and vertical direction using true north as a reference direction.

7. Repeat Exercise 6, but use the epoch 06:04:00.000000.

8. a. Form pseudorange single differences with the ICESat data at 06:00:00.000000. Identify the measurements used and strive for highest accuracy. Identify and justify assumptions.

b. Determine an ICESat position and any other relevant parameters using the single differences of a. Provide justification for the solved for parameter set.   
c. Provide the O-C for all measurements used in b.

9. Repeat Exercise 8, but use the epoch 06:04:00.000000.

10. a. Form pseudorange double-difference measurements between ICESat and Pie Town at 06:00:00.000000. The coordinates for Pie Town and McDonald are given in Table 3.5.3. b. Determine an ICESat position and any other relevant parameters using double differences of a. Provide justification for the solved for parameter set. Are the double differences in your solution independent (see Hoffman-Wellenhof et al., 1997)? Strive for high accuracy. Identify and justify assumptions. c. Provide the O-C for all measurements used in b.

11. Repeat Exercise 10, but use the epoch 06:04:00.000000.

12. Repeat Exercise 10, but use McDonald instead of Pie Town. State any assumptions.

13. Form double-difference pseudorange measurements between Pie Town and McDonald and compute the O-C using the available ephemerides and information from Table 3.5.3.

# Fundamentals of Orbit Determination

# 4.1 INTRODUCTION

During the decade of the 1960s, the accuracy of the radio frequency and optical measurement systems, the force models that govern the satellite motion, and the analysis techniques, combined with relatively primitive computing technology, restricted the positioning of Earth-orbiting satellites to accuracies of hundreds of meters. With the decade of the 1970s, improvements in all of these areas, particularly in mathematical force models and computing capability, facilitated orbit determination accuracy at the level of a few tens of meters by mid-decade and to a few meters by the end of the decade. During the 1980s, significant improvements were made in the models for the Earth’s gravity field, including solid body and ocean tides, and in the models for the surface force effects. All these improvements, which were greatly advanced by the significant developments in computer technology, allowed orbit determination accuracies to increase to the tens-of-centimeter level by the end of the decade.

This improvement in orbit determination accuracy was motivated by the everincreasing demands of scientists in the oceanographic and geodetic communities. In particular, the need for centimeter-level accuracy in global ocean topography obtained from altimetric satellites spurred extensive and unprecedented model improvements during the past two decades. These studies have led to even further improvements in the technology; today the orbit of the oceanographic satellite TOPEX/Poseidon, launched in 1992, is routinely computed with an accuracy approaching $2 \ \mathrm { c m }$ RMS in the radial component and $8 \ \mathrm { c m } \ \mathrm { R S S }$ for all components (Tapley et al.,1994; Schutz et al., 1994; Marshall et al., 1995; Bertiger et al., 1995). Orbits for the Jason-1 altimetric satellite, launched in 2001, are routinely computed with an accuracy of $1 \mathrm { c m }$ in the radial component and $4 \mathrm { { c m } }$ RSS in all components in a post-processing mode using GPS, SLR, and DORIS data (Lutchke et al., 2003). In near-real time (3–5 hours) the Jason-1 radial component is computed to better than $2 . 5 \mathrm { c m }$ RMS using GPS data (Desai and Haines, 2003).

The discussion in the following sections will focus on the techniques used to estimate the orbits. The approach adopted here will follow that given by Tapley (1973, 1989). The role of the estimation process in improving the force and measurement models as an integral step in the process will be illustrated.

# 4.2 LINEARIZATION OF THE ORBIT DETERMINATION PROCESS

In Chapter 1, the general formulation of the orbit determination problem was discussed using a dynamical system governed by a simple linear force model. The role of the measurement model in introducing nonlinearity to the process was described. In the general orbit determination problem, both the dynamics and the measurements involve significant nonlinear relationships. For the general case, the governing relations involve the nonlinear expression

$$
\begin{array} { r } { \dot { \mathbf { X } } = F ( \mathbf { X } , t ) , \qquad \mathbf { X } ( t _ { k } ) \equiv \mathbf { X } _ { k } } \\ { \mathbf { Y } _ { i } = G ( \mathbf { X } _ { i } , t _ { i } ) + \epsilon _ { i } ; \qquad i = 1 , \dots , \ell } \end{array}
$$

where ${ \bf X } _ { k }$ is the unknown $n$ -dimensional state vector at the time $t _ { k }$ , and $\mathbf { Y } _ { i }$ for $i = 1 , \ldots , \ell$ , is a $p$ -dimensional set of observations that are to be used to obtain a best estimate of the unknown value of ${ \bf X } _ { k }$ (i.e., $\hat { \mathbf { X } } _ { k }$ ). In general, $p < n$ and $m = p \times \ell \gg n$ . The formulation represented by Eqs. (4.2.1) and (4.2.2) is characterized by: (1) the inability to observe the state directly, (2) nonlinear relations between the observations and the state, (3) fewer observations at any time epoch than there are state vector components $( p < n )$ ), and (4) errors in the observations represented by $\epsilon _ { i }$ . The problem of determining the trajectory of a space vehicle in the presence of these effects is referred to as the nonlinear estimation (or orbit determination) problem. If the state vector and the observation vector can be related in a linear manner, then several powerful techniques from the field of linear estimation theory can be applied to the orbit determination problem.

If a reasonable reference trajectory is available and if $\mathbf { X }$ , the true trajectory, and $\mathbf { X } ^ { * }$ , the reference trajectory, remain sufficient ly close throughout the time interval of interest, then the trajectory for the actual motion can be expanded in a Taylor’s series about the reference trajectory at each point in time. If this expansion is truncated to eliminate higher order terms, then the deviation in the state from the reference trajectory can be described by a set of linear differential equations with time-dependent coeffici ents. A linear relation between the observation deviation and the state deviation can be obtained by a similar expansion procedure. Then, the nonlinear orbit determination problem in which the complete state vector is to be estimated can be replaced by a linear orbit determination problem in which the deviation from some reference solution is to be determined.

To conduct this linearization procedure, let the $n \times 1$ state deviation vector, $\mathbf { x }$ and the $p \times 1$ observation deviation vector, y, be defined as follows:

$$
{ \bf x } ( t ) = { \bf X } ( t ) - { \bf X } ^ { * } ( t ) , \mathrm {  ~ { \bf ~ y } ( } t ) = { \bf Y } ( t ) - { \bf Y } ^ { * } ( t ) .
$$

It follows that

$$
\dot { { \mathbf x } } ( t ) = \dot { { \mathbf X } } ( t ) - \dot { { \mathbf X } } ^ { * } ( t ) .
$$

Expanding Eqs. (4.2.1) and (4.2.2) in a Taylor’s series about the reference trajectory leads to

$$
\begin{array} { r c l } { \dot { \mathbf { X } } ( t ) } & { = } & { F ( \mathbf { X } , t ) = F ( \mathbf { X } ^ { * } , t ) + \left[ \frac { \partial F ( t ) } { \partial \mathbf { X } ( t ) } \right] ^ { * } \left[ \mathbf { X } ( t ) - \mathbf { X } ^ { * } ( t ) \right] } \\ & & { + O _ { F } \left[ \mathbf { X } ( t ) - \mathbf { X } ^ { * } ( t ) \right] } \\ { \mathbf { Y } _ { i } } & { = } & { G ( \mathbf { X } _ { i } , t _ { i } ) + \epsilon _ { i } = G ( \mathbf { X } _ { i } ^ { * } , t _ { i } ) + \left[ \frac { \partial G } { \partial \mathbf { X } } \right] _ { i } ^ { * } \left[ \mathbf { X } ( t _ { i } ) - \mathbf { X } ^ { * } ( t _ { i } ) \right] _ { i } } \\ & & { + O _ { G } \left[ \mathbf { X } ( t _ { i } ) - \mathbf { X } ^ { * } ( t _ { i } ) \right] + \epsilon _ { i } } \end{array}
$$

where $[ \quad ] ^ { * }$ indicates that the partial derivative matrix is evaluated on the reference solution, $\mathbf { X } ^ { * } ( t )$ , which is obtained by integrating Eq. (4.2.1) with the specifie d initial conditions, $\mathbf { X } ^ { * } ( t _ { 0 } )$ . The symbols $O _ { F }$ and $O _ { G }$ indicate terms in the expansion containing products of the difference, $\mathbf { X } ( t ) - \mathbf { X } ^ { * } ( t )$ , higher than the first order. If the terms of order higher than the fir st in Eq. (4.2.5) are neglected, under the assumption that the higher order products are small compared to the first order terms, and if the condition $\dot { \mathbf { X } } ^ { * } = \dot { F } ( \mathbf { X } ^ { * } , t )$ and $\mathbf { Y } _ { i } ^ { * } = G ( \mathbf { X } _ { i } ^ { * } , t _ { i } )$ are used, Eq. (4.2.5) can be written as

$$
\begin{array} { r l } { \dot { \mathbf { x } } ( t ) = A ( t ) \mathbf { x } ( t ) } & { { } } \\ { \mathbf { y } _ { i } = \widetilde { H } _ { i } \mathbf { x } _ { i } + \epsilon _ { i } \quad } & { { } ( i = 1 , \dots , \ell ) } \end{array}
$$

where

$$
A ( t ) = \left[ { \frac { \partial F ( t ) } { \partial { \bf X } ( t ) } } \right] ^ { * } \qquad { \widetilde { \cal H } } _ { i } = \left[ { \frac { \partial G } { \partial { \bf X } } } \right] _ { i } ^ { * } .
$$

Hence, the original nonlinear estimation problem is replaced by the linear estimation problem described by Eq. (4.2.6), where

$$
\begin{array} { r c l } { \mathbf { x } ( t ) } & { = } & { \mathbf { X } ( t ) - \mathbf { X } ^ { * } ( t ) , } \\ { \mathbf { x } _ { i } } & { = } & { \mathbf { X } ( t _ { i } ) - \mathbf { X } ^ { * } ( t _ { i } ) } \end{array}
$$

and

$$
\begin{array} { r c l } { \mathbf { y } _ { i } } & { = } & { \mathbf { Y } _ { i } - G ( \mathbf { X } _ { i } ^ { * } , t _ { i } ) . } \end{array}
$$

Notice that if the original system of differential equations $\dot { \mathbf { X } } = F ( \mathbf { X } , t )$ is linear, the second and higher order partial derivatives of $F ( \mathbf { X } , t )$ are zero (i.e., $\begin{array} { r } { \frac { \partial ^ { i } F } { \partial \mathbf { X } ^ { i } } = 0 } \end{array}$ , $i \geq 2$ ). The same statements apply to $G ( \mathbf { X } _ { i } , t _ { i } )$ in Eq. (4.2.5). Hence, for a linear system there is no need to deal with a state or observational deviation vector or a reference solution. However, for the orbit determination problem, $F ( \mathbf { X } , t )$ and $G ( \mathbf { X } _ { i } , t _ { i } )$ will always be nonlinear in $\mathbf X ( t )$ , thus requiring that we deal with deviation vectors and a reference trajectory in order to linearize the system.

Generally in this text, uppercase $\mathbf { X }$ and $\mathbf { Y }$ will represent the state and the observation vectors and lowercase $\mathbf { x }$ and $\mathbf { y }$ will represent the state and observation deviation vectors as defined by Eq. (4.2.3). However, this notation will not always be adhered to and sometimes $\mathbf { x }$ and $\mathbf { y }$ will be referred to as the state and observation vectors, respectively.

# Example 4.2.1

Compute the $A$ matrix and the $\widetilde { H }$ matrix for a satellite in a plane under the influence of only a central force. Assume that the satellite is being tracked with range observations, $\rho$ , from a single ground station. Assume that the station coordinates, $( X _ { \mathrm { { S } } } , Y _ { \mathrm { { S } } } )$ , and the gravitational parameter are unknown. Then, the state vector, $\mathbf { X }$ , is given by

$$
\mathbf { X } = { \left[ \begin{array} { l } { X } \\ { Y } \\ { U } \\ { V } \\ { \mu } \\ { X _ { \mathrm { { S } } } } \\ { Y _ { \mathrm { { S } } } } \end{array} \right] }
$$

![](images/03348afeac62a904729c993877ee66c9d871afa5f4312c4105a3fdbafa53ce6c.jpg)

where $U$ and $V$ are velocity components and $X _ { \mathrm { { S } } }$ and $Y _ { \mathrm { S } }$ are coordinates of the tracking station. From Newton’s Second Law and the law of gravitation,

$$
{ \ddot { \mathbf { r } } } = - { \frac { \mu \mathbf { r } } { r ^ { 3 } } }
$$

or in component form,

$$
\ddot { X } = - \frac { \mu X } { r ^ { 3 } }
$$

$$
\ddot { Y } = - \frac { \mu Y } { r ^ { 3 } } .
$$

If these equations are expressed in firs t-order form, the following expression is obtained:

$$
{ \dot { \mathbf { X } } } = { \left[ \begin{array} { l } { { \dot { X } } } \\ { { \dot { Y } } } \\ { { \dot { U } } } \\ { { \dot { V } } } \\ { { \dot { V } } } \\ { { \dot { H } } } \\ { { \dot { H } } } \\ { { \dot { X } } _ { \mathrm { s } } } \\ { { \dot { Y } _ { \mathrm { s } } } } \end{array} \right] } = { \left[ \begin{array} { l } { F _ { 1 } } \\ { F _ { 2 } } \\ { F _ { 3 } } \\ { F _ { 4 } } \\ { F _ { 5 } } \\ { F _ { 6 } } \\ { F _ { 7 } } \end{array} \right] } =  \left[ \begin{array} { l } { { \begin{array} { l } { { U } } \\ { { U } } \\ { { \dot { V } } } \\ { - { \frac { \mu X } { T ^ { 3 } } } } \\ { - { \frac { \mu Y } { T ^ { 3 } } } } \\ { 0 } \\ { 0 } \\ { 0 } \end{array} \right] } } \end{array}
$$

Then,

$$
\begin{array} { r l } { = { } } & { { } { \left| \begin{array} { l l l l l l } { \ 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { } & { } & { } & { } & { } & { } \\ { } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { - { \frac { \mu } { r ^ { 3 } } } + { \frac { 3 \mu X ^ { 2 } } { r ^ { 5 } } } } & { { \frac { 3 \mu X Y } { r ^ { 5 } } } } & { 0 } & { 0 } & { - { \frac { X } { r ^ { 3 } } } } & { 0 } & { 0 } \\ { } & { } & { } & { } & { } & { } & { } \\ { { \frac { 3 \mu X Y } { r ^ { 5 } } } } & { - { \frac { \mu } { r ^ { 3 } } } + { \frac { 3 \mu Y ^ { 2 } } { r ^ { 5 } } } } & { 0 } & { 0 } & { - { \frac { Y } { r ^ { 3 } } } } & { 0 } & { 0 } \\ { } & { } & { } & { } & { } & { } & { } \\ { 0 } & { } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { } & { } & { } & { } & { } & { } & { } & { } \\ { } & { } & { } & { } & { } & { } & { } & { } \end{array} \right| } . } \end{array}
$$

The $\widetilde { H }$ matrix is given by

$$
{ \widetilde { H } } = { \frac { \partial \rho } { \partial \mathbf { X } } } = { \left[ \begin{array} { l l l l l l l } { { \frac { \partial \rho } { \partial X } } } & { { \frac { \partial \rho } { \partial Y } } } & { { \frac { \partial \rho } { \partial U } } } & { { \frac { \partial \rho } { \partial V } } } & { { \frac { \partial \rho } { \partial \mu } } } & { { \frac { \partial \rho } { \partial X _ { \mathrm { S } } } } } & { { \frac { \partial \rho } { \partial Y _ { \mathrm { S } } } } } \end{array} \right] } ^ { * }
$$

where

$$
\rho = \left[ \left( X - X _ { \mathrm { S } } \right) ^ { 2 } + \left( Y - Y _ { \mathrm { S } } \right) ^ { 2 } \right] ^ { 1 / 2 } .
$$

It follows then that

$$
\widetilde { H } = \left[ \begin{array} { l l l l l l l } { X - X _ { \mathrm { S } } } & { Y - Y _ { \mathrm { S } } } & { 0 } & { 0 } & { 0 } & { - \frac { \left( X - X _ { \mathrm { S } } \right) } { \rho } } & { - \frac { \left( Y - Y _ { \mathrm { S } } \right) } { \rho } } \end{array} \right] ^ { \ast } .
$$

# 4.2.1 THE STATE TRANSITION MATRIX

The first of Eq. (4.2.6) represents a system of linear differential equations with time-dependent coefficients. The symbol $[ ] ^ { * }$ indicates that the values of $\mathbf { X }$ are derived from a particular solution to the equations $\dot { \mathbf { X } } = F ( \mathbf { X } , t )$ which is generated with the initial conditions $\mathbf { X } ( t _ { 0 } ) = \mathbf { X } _ { 0 } ^ { * }$ . The general solution for this system, $\dot { \mathbf { x } } ( t ) = A ( t ) \mathbf { x } ( t )$ , can be expressed as

$$
{ \bf x } ( t ) = \Phi ( t , t _ { k } ) { \bf x } _ { k }
$$

where $\mathbf { x } _ { k }$ is the value of $\mathbf { x }$ at $t _ { k }$ ; that is, $\mathbf { x } _ { k } = \mathbf { x } ( t _ { k } )$ . The matrix $\Phi ( t _ { i } , t _ { k } )$ is called the state transition matrix and was introduced in Chapter 1, Section 1.2.5. The state transition matrix for the two-body problem was discussed in Chapter 2, Section 2.2.6. $\Phi ( t , t _ { k } )$ has the following useful properties, which can be demonstrated from Eq. (4.2.7).

$$
\begin{array} { l c l c l } { { 1 . } } & { { \Phi ( t _ { k } , t _ { k } ) } } & { { = } } & { { I } } & { { } } \\ { { 2 . } } & { { \Phi ( t _ { i } , t _ { k } ) } } & { { = } } & { { \Phi ( t _ { i } , t _ { j } ) \Phi ( t _ { j } , t _ { k } ) } } & { { } } \\ { { 3 . } } & { { \Phi ( t _ { i } , t _ { k } ) } } & { { = } } & { { \Phi ^ { - 1 } ( t _ { k } , t _ { i } ) . } } & { { } } \end{array}
$$

The differential equation for $\Phi ( t _ { i } , t _ { k } )$ can be obtained by differentiating Eq. (4.2.7) (noting that $\mathbf { x } _ { k }$ is a constant). This yields

$$
\dot { { \bf x } } ( t ) = \dot { \Phi } ( t , t _ { k } ) { \bf x } _ { k } .
$$

Substituting Eq. (4.2.9) into the first of Eq. (4.2.6) and using Eq. (4.2.7) yields

$$
{ \dot { \Phi } } ( t , t _ { k } ) \mathbf { x } _ { k } = A ( t ) \Phi ( t , t _ { k } ) \mathbf { x } _ { k } .
$$

Since this condition must be satisfied for all $\mathbf { x } _ { k }$ , it follows that

$$
{ \dot { \Phi } } ( t , t _ { k } ) = A ( t ) \Phi ( t , t _ { k } )
$$

with initial conditions

$$
\Phi ( t _ { k } , t _ { k } ) = I .
$$

By differentiating ${ \bf x } _ { k } = \Phi ^ { - 1 } ( t , t _ { k } ) { \bf x } ( t )$ from Eq. (4.2.7) and using the first of Eq. (4.2.6) it can be shown that

$$
\dot { \Phi } ^ { - 1 } ( t , t _ { k } ) = - \Phi ^ { - 1 } ( t , t _ { k } ) A ( t ) ,
$$

with initial conditions

$$
\Phi ^ { - 1 } ( t _ { k } , t _ { k } ) = I .
$$

Under certain conditions on $A ( t )$ , the state transition matrix may be inverted analytically (Battin, 1999).

If the matrix $A ( t )$ can be partitioned in the form

$$
A ( t ) = \left[ { \frac { A _ { 1 } \mid A _ { 2 } } { A _ { 3 } \mid A _ { 4 } } } \right]
$$

where the submatrices have the properties that

$$
A _ { 1 } ^ { T } = - A _ { 4 } , ~ A _ { 2 } ^ { T } = A _ { 2 } ~ \mathrm { a n d } ~ A _ { 3 } ^ { T } = A _ { 3 } .
$$

Then $\Phi ( t , t _ { k } )$ can be similarly partitioned as

$$
\Phi ( t , t _ { k } ) = \left[ \frac { \Phi _ { 1 } \ \biggr | \ \Phi _ { 2 } } { \Phi _ { 3 } \ \biggr | \ \Phi _ { 4 } } \right]
$$

and $\Phi ^ { - 1 } ( t , t _ { k } )$ may be written as

$$
\Phi ^ { - 1 } ( t , t _ { k } ) = [ \frac { \Phi _ { 4 } ^ { T } } { - \Phi _ { 3 } ^ { T } } | \begin{array} { c } { { - \Phi _ { 2 } ^ { T } } } \\ { { \Phi _ { 1 } ^ { T } } } \end{array} ] .
$$

The proof follows: Define

$$
J = \left[ { \begin{array} { r r } { 0 } & { I } \\ { - I } & { 0 } \end{array} } \right]
$$

where $I$ is the identity matrix and 0 is the null matrix. Then

$$
\begin{array} { r c l } { \displaystyle \frac { d } { d t } ( J \Phi ( t , t _ { k } ) J ) } & { = } & { J \dot { \Phi } ( t , t _ { k } ) J } \\ & { = } & { - ( J A ( t ) J ) ( J \Phi ( t , t _ { k } ) J ) , } \end{array}
$$

where we have used the fact that $J ^ { 2 } = - I$ and ${ \dot { \Phi } } ( t , t _ { k } ) = A ( t ) \Phi ( t , t _ { k } )$ .

Define

$$
V ( t , t _ { k } ) \equiv - ( J \Phi ( t , t _ { k } ) J ) ^ { T } .
$$

Taking the transpose of Eq. (4.2.16) and using Eq. (4.2.17),

$$
\begin{array} { l l l } { ( J \dot { \Phi } ( t , t _ { k } ) J ) ^ { T } } & { = } & { - \dot { V } ( t , t _ { k } ) } \\ & { = } & { - ( J \Phi ( t , t _ { k } ) J ) ^ { T } ( J A ( t ) J ) ^ { T } } \end{array}
$$

or

$$
\dot { V } ( t , t _ { k } ) = - V ( t , t _ { k } ) ( J A ( t ) J ) ^ { T } .
$$

Using Eq. (4.2.12) for $A ( t )$ yields

$$
( J A ( t ) J ) ^ { T } = \left[ \frac { - A _ { 4 } ^ { T } \nonumber \left. ~ A _ { 2 } ^ { T } \right. } { \left. A _ { 3 } ^ { T } \right. ~ \left. ~ - A _ { 1 } ^ { T } \right. } \right] .
$$

Consequently, if $A ( t )$ satisfies Eq. (4.2.13) and

$$
( J A ( t ) J ) ^ { T } = A ( t ) ,
$$

then

$$
\dot { V } ( t , t _ { k } ) = - V ( t , t _ { k } ) A ( t )
$$

and

$$
V ( t _ { 0 } , t _ { 0 } ) = - ( J \Phi ( t _ { 0 } , t _ { 0 } ) J ) ^ { T } = I .
$$

Hence, from Eq. (4.2.11) and Eq. (4.2.21),

$$
V ( t , t _ { k } ) = \Phi ^ { - 1 } ( t , t _ { k } )
$$

or

$$
\begin{array} { c c l } { \Phi ^ { - 1 } ( t , t _ { k } ) } & { = } & { - ( J \Phi ( t , t _ { k } ) J ) ^ { T } } \\ & { = } & { \left[ \frac { \Phi _ { 4 } ^ { T } } { - \Phi _ { 3 } ^ { T } } \left| \begin{array} { c } { \mathbf { \Phi } - \Phi _ { 2 } ^ { T } } \\ { \mathbf { \Phi } \Phi _ { 1 } ^ { T } } \end{array} \right] \right. } \end{array}
$$

which is identical to Eq. (4.2.14).

An even dimensional matrix, $B$ , which has the property that $B ^ { T } J B = J$ (where $J$ is defined by Eq. (4.2.15)) is called symplectic (Battin, 1999). It easily is shown that $\Phi ( t , t _ { k } )$ has this property when $A$ satisfies Eq. (4.2.13). An important case where $\Phi ( t , t _ { k } )$ is symplectic arises when the acceleration can be written as the gradient of a potential function; that is,

$$
\ddot { \mathbf { r } } = \nabla U .
$$

# 4.2.2 SOLUTION FOR THE STATE TRANSITION MATRIX

A linear differential equation of the type ${ \dot { \mathbf { x } } } ( t ) = A ( t ) \mathbf { x } ( t )$ or $\dot { \Phi } ( t , t _ { 0 } ) ~ =$ $A ( t ) \Phi ( t , t _ { 0 } )$ has an infinite number of solutions in terms of arbitrary constants. However, when initial conditions, $\mathbf { x } ( t _ { 0 } )$ and $\Phi ( t _ { 0 } , t _ { 0 } )$ , are specified and the elements of $A ( t )$ are continuous functions of time, the solution becomes unique. One could ask the question “Wh y bother to solve for the state transition matrix when the state deviation vector can be determined directly by solving ${ \dot { \bf x } } ( t ) =$ $A ( t ) \mathbf { x } ( t )$ ?” The answer is that the computational algorithms for determining the best estimate of $\mathbf { x }$ and for mapping the associated error covariance matrices are most easily formulated in terms of the state transition matrix. Since $\mathbf { x } _ { k }$ in Eq. (4.2.7) is unknown in the orbit determination problem, the state transition matrix allows the solution, ${ \bf x } ( t )$ , to be expressed in terms of the unknown initial state, $\mathbf { x } _ { k }$ . Hence, it is essential in relating observations made at different times.

The solution for $\Phi ( t , t _ { 0 } )$ is facilitated by noting that the individual columns of the differential equation for $\dot { \Phi } ( t , t _ { 0 } )$ are uncoupled and independent. To illustrate this, consider a one-dimensional case where the state vector consists of a single position and velocity coordinate. Equation (4.2.10) can be written in terms of the individual elements of the state transition matrix as follows:

$$
\dot { \Phi } ( t , t _ { 0 } ) = \left[ \begin{array} { l l } { \dot { \phi } _ { 1 1 } } & { \dot { \phi } _ { 1 2 } } \\ { \dot { \phi } _ { 2 1 } } & { \dot { \phi } _ { 2 2 } } \end{array} \right] = \left[ \begin{array} { l l } { A _ { 1 1 } } & { A _ { 1 2 } } \\ { A _ { 2 1 } } & { A _ { 2 2 } } \end{array} \right] \left[ \begin{array} { l l } { \phi _ { 1 1 } } & { \phi _ { 1 2 } } \\ { \phi _ { 2 1 } } & { \phi _ { 2 2 } } \end{array} \right]
$$

subject to the following initial conditions at $t _ { 0 }$

$$
\left[ \begin{array} { l l } { \phi _ { 1 1 } } & { \phi _ { 1 2 } } \\ { \phi _ { 2 1 } } & { \phi _ { 2 2 } } \end{array} \right] = \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] .
$$

Equation (4.2.24) expands to

$$
\left[ \begin{array} { l l } { \dot { \phi } _ { 1 1 } } & { \dot { \phi } _ { 1 2 } } \\ { \dot { \phi } _ { 2 1 } } & { \dot { \phi } _ { 2 2 } } \end{array} \right] = \left[ \begin{array} { l l } { A _ { 1 1 } \phi _ { 1 1 } + A _ { 1 2 } \phi _ { 2 1 } } & { A _ { 1 1 } \phi _ { 1 2 } + A _ { 1 2 } \phi _ { 2 2 } } \\ { A _ { 2 1 } \phi _ { 1 1 } + A _ { 2 2 } \phi _ { 2 1 } } & { A _ { 2 1 } \phi _ { 1 2 } + A _ { 2 2 } \phi _ { 2 2 } } \end{array} \right] .
$$

Recall that the $A _ { i j }$ are known quantities obtained by evaluating

$$
A _ { i j } ( t ) = \left[ \frac { \partial F _ { i } ( t ) } { \partial \mathbf { X } _ { j } ( t ) } \right] ^ { * }
$$

on the reference trajectory. From Eq. (4.2.26) we see that the columns of $\dot { \Phi } ( t , t _ { 0 } )$ are independent; for example, the first column of $\dot { \Phi } ( t , t _ { 0 } )$ does not contain elements of $\Phi ( t , \ t _ { 0 } )$ from the second column. Hence, we can solve for $\Phi ( t , \ t _ { 0 } )$ by integrating independently two $2 \times 1$ vector differential equations. For any practical orbit determination application, the solution for $\Phi ( t , \ t _ { 0 } )$ will be obtained via numerical integration. Hence, we can supply a vector of derivative values for the differential equation of the nominal state vector and $\dot { \Phi } ( t , t _ { 0 } )$ to the numerical integration routine. For this 1D case we would supply the integrator with the following vector at each time point:

$$
\left[ \begin{array} { l } { \dot { X } } \\ { \dot { U } } \\ { \dot { \phi } _ { 1 1 } } \\ { \dot { \phi } _ { 2 1 } } \\ { \dot { \phi } _ { 1 2 } } \\ { \dot { \phi } _ { 2 2 } } \end{array} \right] .
$$

The first two elements would provide the reference orbit, $\mathbf { X } ^ { * } ( t )$ , and the next four would yield the elements of $\Phi ( t , t _ { 0 } )$ . The reference orbit is used to evaluate $A ( t )$ , which is needed to evaluate $\dot { \Phi } ( t , t _ { 0 } )$ in Eq. (4.2.26).

Notice that when ${ \dot { \Phi } } = A { \dot { \Phi } }$ is numerically integrated for the two-body case given in Example 4.2.1 we need to concern ourselves only with the upper $4 \times 5$ portion of $\dot { \Phi }$ . The final three rows and two columns of $\Phi$ remain zero except for the values of unity in the last three diagonal elements. Hence, the numerical integration algorithm should be structured to take advantage of this fact.

Another approach to solving the linearized equations of motion is given in Appendix F. Additional clarification on the structure of $\Phi$ and associated matrices also is given.

Generally all orbit determination problems will result in $A ( t )$ being a function of time. For example, the simple two-body Example 4.2.1 involves a time-varying matrix for $A ( t )$ . However, it is instructive to consider the case where $A$ is a constant matrix because of the insight gained about the state transition matrix. Such a case is illustrated in the following example.

# Example 4.2.2

Consider a system of linear first-order differential equations with constant coefficient s

$$
\begin{array} { l } { \dot { x } _ { 1 } = x _ { 1 } } \\ { \dot { x } _ { 2 } = \beta x _ { 1 } } \end{array}
$$

where $\beta$ is a constant. Initial conditions are $x _ { 1 } ( t _ { 0 } ) = x _ { 1 0 }$ and $x _ { 2 } ( t _ { 0 } ) = x _ { 2 0 }$ .

a) Write Eq. (4.2.28) in state space form; that is, ${ \dot { \mathbf { X } } } = A \mathbf { X }$ ,

$$
\begin{array} { r } { \dot { \mathbf { X } } = \left[ \begin{array} { l } { \dot { \mathbf { x } } _ { 1 } } \\ { \dot { \mathbf { x } } _ { 2 } } \end{array} \right] = \left[ \begin{array} { l l } { 1 } & { 0 } \\ { \beta } & { 0 } \end{array} \right] \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \end{array} \right] = A \mathbf { X } . } \end{array}
$$

b) Solve Eq. (4.2.29) by determining the state transition matrix; that is, ${ \bf X } ( t ) =$ $\Phi ( t , t _ { 0 } ) { \bf X } ( t _ { 0 } )$ , where $\dot { \Phi } ( t , t _ { 0 } ) = \dot { A } ( t ) \Phi ( t , t _ { 0 } )$ . Because $A ( t )$ is a constant matrix there are a number of ways to solve for $\Phi ( t , t _ { 0 } )$ . These include but are not limited to the following:

1. Because Eq. (4.2.28) is linear with constant coefficients it can be solved directly. From the first equation

$$
{ \begin{array} { r c l } { { \frac { d x _ { 1 } } { x _ { 1 } } } } & { = } & { d t } \\ { x _ { 1 } ( t ) } & { = } & { c e ^ { t } ; } \\ { c } & { = } & { x _ { 1 0 } e ^ { - t _ { 0 } } } \\ { x _ { 1 } ( t ) } & { = } & { x _ { 1 0 } e ^ { \left( t - t _ { 0 } \right) } , } \end{array} } \ a t \ t = t _ { 0 } , \ x _ { 1 } = x _ { 1 0 }
$$

from the second of Eq. (4.2.28)

$$
\begin{array} { r c l } { { d x _ { 2 } } } & { { = } } & { { \beta x _ { 1 0 } e ^ { ( t - t _ { 0 } ) } d t } } \\ { { x _ { 2 } ( t ) } } & { { = } } & { { \beta x _ { 1 0 } e ^ { ( t - t _ { 0 } ) } + c ; \qquad \mathrm { a t } \ t = t _ { 0 } , \ x _ { 2 } = x _ { 2 0 } . } } \end{array}
$$

Hence,

$$
x _ { 2 } ( t ) = x _ { 2 0 } + \beta x _ { 1 0 } ( e ^ { ( t - t _ { 0 } ) } - 1 ) .
$$

The state transition matrix can be determined from a direct differentiation of the solution

$$
\boldsymbol \Phi ( t , t _ { 0 } ) \equiv \frac { \partial { \mathbf X } ( t ) } { \partial { \mathbf X } ( t _ { 0 } ) } = \left[ \begin{array} { l l } { \frac { \partial x _ { 1 } ( t ) } { \partial x _ { 1 } ( t _ { 0 } ) } } & { \frac { \partial x _ { 1 } ( t ) } { \partial x _ { 2 } ( t _ { 0 } ) } } \\ { \frac { \partial x _ { 2 } ( t ) } { \partial x _ { 1 } ( t _ { 0 } ) } } & { \frac { \partial x _ { 2 } ( t ) } { \partial x _ { 2 } ( t _ { 0 } ) } } \end{array} \right] .
$$

The elements of Eq. (4.2.32) are obtained by differentiating Eqs. (4.2.30) and (4.2.31) to yield

$$
\Phi ( t , t _ { 0 } ) = \left[ \begin{array} { l l } { e ^ { ( t - t _ { 0 } ) } } & { 0 } \\ { \beta ( e ^ { ( t - t _ { 0 } ) } - 1 ) } & { 1 } \end{array} \right] .
$$

2. We may integrate ${ \dot { \Phi } } = A \Phi$ directly:

$$
\left[ \begin{array} { l l } { \dot { \phi } _ { 1 1 } } & { \dot { \phi } _ { 1 2 } } \\ { \dot { \phi } _ { 2 1 } } & { \dot { \phi } _ { 2 2 } } \end{array} \right] = \left[ \begin{array} { l l } { 1 } & { 0 } \\ { \beta } & { 0 } \end{array} \right] \left[ \begin{array} { l l } { \phi _ { 1 1 } } & { \phi _ { 1 2 } } \\ { \phi _ { 2 1 } } & { \phi _ { 2 2 } } \end{array} \right] ; ~ \Phi ( t _ { 0 } , t _ { 0 } ) = I .
$$

The equations to be integrated are

$$
\begin{array} { r l } & { \dot { \phi } _ { 1 1 } = \phi _ { 1 1 } } \\ & { \dot { \phi } _ { 2 1 } = \beta \phi _ { 1 1 } } \\ & { \dot { \phi } _ { 1 2 } = \phi _ { 1 2 } } \\ & { \dot { \phi } _ { 2 2 } = \beta \phi _ { 1 2 } \mathrm { . } } \end{array}
$$

Solving Eq. (4.2.34) yields

$$
\begin{array} { r c l } { \phi _ { 1 1 } } & { = } & { c e ^ { t } ; } \\ { c } & { = } & { e ^ { - t _ { 0 } } } \\ { \phi _ { 1 1 } } & { = } & { e ^ { \left( t - t _ { 0 } \right) } . } \end{array}
$$

Next,

$$
\begin{array} { l c l } { { \dot { \phi } _ { 2 1 } } } & { { = } } & { { \beta e ^ { ( t - t _ { 0 } ) } } } \\ { { \phi _ { 2 1 } } } & { { = } } & { { \beta e ^ { ( t - t _ { 0 } ) } + c ; \qquad \phi _ { 2 1 } ( t _ { 0 } ) = 0 . } } \end{array}
$$

If this expression is evaluated at $t _ { 0 }$ , it follows that

$$
c = - \beta
$$

and

$$
\phi _ { 2 1 } = \beta ( e ^ { ( t - t _ { 0 } ) } - 1 ) .
$$

Finally, the second two of Eq. (4.2.34) along with the initial conditions lead to

$$
\begin{array} { l c l } { { \phi _ { 1 2 } } } & { { = } } & { { 0 } } \\ { { } } & { { } } & { { } } \\ { { \phi _ { 2 2 } } } & { { = } } & { { 1 . } } \end{array}
$$

These solutions are identical to the elements given by Eq. (4.2.33).

3. We may use Laplace transforms to solve for $\Phi ( t , t _ { 0 } )$ . In this case

$$
\begin{array} { r c l } { \Phi ( t , t _ { 0 } ) } & { = } & { \mathcal { L } ^ { - 1 } \left[ S I - A \right] ^ { - 1 } = \mathcal { L } ^ { - 1 } \left[ \begin{array} { c c } { S - 1 } & { 0 } \\ { - \beta } & { S } \end{array} \right] ^ { - 1 } } \\ & { = } & { \mathcal { L } ^ { - 1 } \left[ \begin{array} { c c } { \frac { 1 } { S - 1 } } & { 0 } \\ { \frac { \beta } { S \left( S - 1 \right) } } & { \frac { 1 } { S } } \end{array} \right] . } \end{array}
$$

Using a table of Laplace transforms yields

$$
\Phi ( t , t _ { 0 } ) = \left[ \begin{array} { c c } { e ^ { ( t - t _ { 0 } ) } } & { 0 } \\ { \beta ( e ^ { ( t - t _ { 0 } ) } - 1 ) } & { 1 } \end{array} \right] .
$$

4. Another solution, whenever $A$ is a constant matrix, uses the eigenvalues and eigenvectors of $A$ to yield the solution

$$
\Phi ( t , t _ { 0 } ) = V e ^ { \lambda ( t - t _ { 0 } ) } V ^ { - 1 } ,
$$

where $V$ is the matrix of normalized eigenvectors of $A$ . Also,

$$
e ^ { \lambda ( t , t _ { 0 } ) } = \left[ \begin{array} { c c c c } { { e ^ { \lambda _ { 1 } ( t - t _ { 0 } ) } } } & { { } } & { { } } & { { } } \\ { { } } & { { e ^ { \lambda _ { 2 } ( t - t _ { 0 } ) } } } & { { } } & { { 0 } } \\ { { } } & { { } } & { { \ddots } } & { { } } \\ { { 0 } } & { { } } & { { } } & { { e ^ { \lambda _ { n } ( t - t _ { 0 } ) } } } \end{array} \right]
$$

where $\lambda _ { 1 }$ $_ 1 , \lambda _ { 2 } \ldots \lambda _ { n }$ are the eigenvalues of the $n \times n$ matrix, $A$ .

This method requires that $A$ have a complete set of linearly independent eigenvectors. Otherwise there is no invertible matrix of eigenvectors, $V$ , and the algorithm fails.

For the example we are considering, the matrix

$$
A = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { \beta } & { 0 } \end{array} \right] }
$$

has eigenvalues (see Appendix B, Section B.6)

$$
\begin{array} { r } { \begin{array} { r c l } { \lambda _ { 1 } } & { = } & { 0 } \\ { \lambda _ { 2 } } & { = } & { 1 } \end{array} } \end{array}
$$

and normalized eigenvectors

$$
V _ { 1 } = \left[ \begin{array} { l } { { 0 } } \\ { { 1 } } \end{array} \right] \ , \qquad V _ { 2 } = \left[ \begin{array} { l } { { \displaystyle \frac { 1 } { \sqrt { 1 + \beta ^ { 2 } } } } } \\ { { \displaystyle \frac { \beta } { \sqrt { 1 + \beta ^ { 2 } } } } } \end{array} \right] .
$$

Hence,

$$
\begin{array} { r l r } { V } & { = } & { \left[ \begin{array} { c c } { 0 } & { \displaystyle \frac { 1 } { \sqrt { 1 + \beta ^ { 2 } } } } \\ { 1 } & { \displaystyle \frac { \beta } { \sqrt { 1 + \beta ^ { 2 } } } } \end{array} \right] , \qquad V ^ { - 1 } = \left[ \begin{array} { c c } { - \beta } & { 1 } \\ { \sqrt { 1 + \beta ^ { 2 } } } & { 0 } \end{array} \right] } \\ { e ^ { \lambda ( t , t _ { 0 } ) } } & { = } & { \left[ \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { e ^ { ( t - t _ { 0 } ) } } \end{array} \right] } \end{array}
$$

and from Eq. (4.2.35)

$$
\Phi ( t , t _ { 0 } ) = \left[ \begin{array} { l l } { e ^ { ( t - t _ { 0 } ) } } & { 0 } \\ { \beta ( e ^ { ( t - t _ { 0 } ) } - 1 ) } & { 1 } \end{array} \right] .
$$

Moler and Van Loan (1978) describe 19 ways to compute the exponential of a matrix, including the methods presented here.

# 4.2.3 RELATING THE OBSERVATIONS TO AN EPOCH STATE

Note from the second of Eq. (4.2.6) that there is an unknown state vector $\mathbf { x } _ { i }$ corresponding to each observation $\mathbf { y } _ { i }$ . Hence, it is desirable to use the state transition matrix to express all observations in terms of the state at a single epoch in order to reduce the number of unknown state vectors from $\ell \times n$ to $n$ . Using Eq. (4.2.7), the second of Eq. (4.2.6) may be written in terms of the state at $t _ { k }$ as

$$
\begin{array} { r l r } { { \bf y } _ { 1 } } & { = } & { \tilde { H } _ { 1 } \Phi ( t _ { 1 } , t _ { k } ) { \bf x } _ { k } + \epsilon _ { 1 } } \\ { { \bf y } _ { 2 } } & { = } & { \tilde { H } _ { 2 } \Phi ( t _ { 2 } , t _ { k } ) { \bf x } _ { k } + \epsilon _ { 2 } } \\ & { \vdots } & \\ { { \bf y } _ { \ell } } & { = } & { \tilde { H } _ { \ell } \Phi ( t _ { \ell } , t _ { k } ) { \bf x } _ { k } + \epsilon _ { \ell } . } \end{array}
$$

Equation (4.2.37) now contains $m = p \times \ell$ observations and only $n$ unknown components of the state. If $\epsilon _ { i }$ , $i = 1 , \ldots , \ell$ is zero, any linearly independent $n$ of Eq. (4.2.37) can be used to determine $\mathbf { x } _ { k }$ .

If the following definitions are used

$$
\begin{array} { r } { \mathbf { y } \equiv \left[ \begin{array} { c } { y _ { 1 } } \\ { \vdots } \\ { y _ { \ell } } \end{array} \right] ; \quad H \equiv \left[ \begin{array} { c } { \widetilde { H } _ { 1 } \Phi ( t _ { 1 } , t _ { k } ) } \\ { \vdots } \\ { \widetilde { H } _ { \ell } \Phi ( t _ { \ell } , t _ { k } ) } \end{array} \right] ; \quad \epsilon \equiv \left[ \begin{array} { c } { \epsilon _ { 1 } } \\ { \vdots } \\ { \epsilon _ { \ell } } \end{array} \right] } \end{array}
$$

and if the subscript on $\mathbf { x } _ { k }$ is dropped for convenience, then Eq. (4.2.37) can be expressed as follows:

$$
\mathbf { y } = H \mathbf { x } + \epsilon
$$

where $\mathbf { y }$ is an $m \times 1$ vector, $\mathbf { x }$ is an $n \times 1$ vector, $\epsilon$ is an $m \times 1$ vector, $H$ is an $m \times n$ mapping matrix, where $m = p \times \ell$ is the total number of observations. If $p$ or $\ell$ is sufficient ly large, the essential condition $m > n$ is satisfied. However, we are still faced with $m$ unknown observation errors resulting in $m + n$ total unknowns and only $m$ equations. The least squares criterion provides us with conditions on the $m$ observation errors that allow a solution for the $n$ state variables, $\mathbf { x }$ , at the epoch time $t _ { k }$ .

# 4.3 THE LEAST SQUARES SOLUTION

The least squares solution selects the estimate of $\mathbf { x }$ as that value that minimizes the sum of the squares of the calculated observation residuals. That is, $\mathbf { x }$ is selected to minimize the following performance index (Lawson and Hanson, 1974; Bjorck, 1997): ¨

$$
J ( \mathbf { x } ) = 1 / 2 \epsilon ^ { T } \epsilon .
$$

The least squares criterion was fir st proposed by Gauss (1809) and is commonly used today. The sum of the squares of the calculated observation errors is a logical choice for the performance index. A criterion define d, for example, by the sum of the calculated observation errors could be identically zero with very large observation errors having plus and minus signs that cancel each other. Whether the observation error is positive or negative, its square will be positive and the performance index defined by Eq. (4.3.1) can vanish only if each of the observation errors is identically zero. If $\epsilon$ , as defined by Eq. (4.2.39), is substituted into Eq. (4.3.1), the following expression is obtained:

$$
J ( \mathbf { x } ) = 1 / 2 \epsilon ^ { T } \epsilon = \sum _ { i = 1 } ^ { \ell } 1 / 2 \epsilon _ { i } ^ { T } \epsilon _ { i } = 1 / 2 ( \mathbf { y } - H \mathbf { x } ) ^ { T } ( \mathbf { y } - H \mathbf { x } ) .
$$

Note that Eq. (4.3.2) is a quadratic function of $\mathbf { x }$ , and as a consequence the expression will have a unique minima when (see Appendix B, Eq. (B.8.2))

$$
{ \frac { \partial J } { \partial \mathbf { x } } } = 0 , \mathrm { a n d } \delta \mathbf { x } ^ { T } { \frac { \partial ^ { 2 } J } { \partial \mathbf { x } ^ { 2 } } } \delta \mathbf { x } > 0
$$

for all $\delta \mathbf { x } \neq 0$ . The second condition implies that the symmetric matrix

$$
\frac { \partial ^ { 2 } J } { \partial \mathbf { x } ^ { 2 } }
$$

is positive definite.

Carrying out the first operation on Eq. (4.3.2) (see Appendix B, Eq. (B yields

$$
\frac { \partial J } { \partial \mathbf { x } } = 0 = - ( \mathbf { y } - H \mathbf { x } ) ^ { T } H = - H ^ { T } ( \mathbf { y } - H \mathbf { x } ) .
$$

The value of $\mathbf { x }$ that satisfies Eq. (4.3.3) will be the best estimate of $\mathbf { x }$ , which we will call $\hat { \bf x }$ . Hence,

$$
\begin{array} { r } { ( H ^ { T } H ) \hat { \mathbf { x } } = H ^ { T } \mathbf { y } . } \end{array}
$$

Also, from Eqs. (4.3.3) and (B.7.3) it follows that

$$
\frac { \partial ^ { 2 } J } { \partial { \bf x } ^ { 2 } } = H ^ { T } H
$$

which will be positive definite if $H$ is full rank.

Equation (4.3.4) is referred to as the normal equation, and $( H ^ { T } H )$ is referred to as the normal matrix. Note that the matrix $H ^ { T } H$ is an $n \times n$ symmetric matrix, and if this matrix is positive definite $H$ is rank $n$ ) then the solution for the best estimate of $\mathbf { x }$ is given by

$$
\begin{array} { r } { \hat { \mathbf { x } } = ( H ^ { T } H ) ^ { - 1 } H ^ { T } \mathbf { y } . } \end{array}
$$

Equation (4.3.6) is the well-known least squares solution for the best estimate of $\mathbf { x }$ given the linear observation state relationship expressed by Eq. (4.2.39). With the observations, $\mathbf { y }$ , and a specified value of $\hat { \bf x }$ , the value for the best estimate of the observation errors, $\hat { \epsilon }$ , can be computed from Eq. (4.2.39) as

$$
\hat { \mathbf { \epsilon } } = \mathbf { y } - H \hat { \mathbf { x } } .
$$

# 4.3.1 THE MINIMUM NORM SOLUTION

For the solution given by Eq. (4.3.6) to exist, it is required that $m \geq n$ and $H$ have rank $n$ . Consider the case where $m \ < \ n$ ; that is, $H$ is of rank $< n$ .

In other words, there are more unknowns than linearly independent observations. One could choose to specify any $n - m$ of the $n$ components of $\mathbf { x }$ and solve for the remaining $m$ components of $\mathbf { x }$ using the observation equations with $\epsilon = 0$ . However, this leads to an infinite number of solutions for $\hat { \bf x }$ . As an alternative, to obtain a unique solution, one can use the minimum norm criterion to determine $\hat { \bf x }$ . Generally, a nominal or initial guess for $\mathbf { x }$ exists. Recall that the differential equations have been linearized and $\mathbf { x } = \mathbf { X } - \mathbf { X } ^ { * }$ . The minimum norm criterion chooses $\mathbf { x }$ to minimize the sum of the squares of the difference between $\mathbf { X }$ and $\mathbf { X } ^ { * }$ , subject to the constraint that $\epsilon = 0$ ; that is, $\mathbf { y } = H \mathbf { x }$ . Hence, the performance index becomes

$$
J ( \mathbf { x } , \pmb { \lambda } ) = 1 / 2 \mathbf { x } ^ { T } \mathbf { x } + \lambda ^ { T } ( \mathbf { y } - H \mathbf { x } )
$$

where the constraint has been adjoined with an $m$ -dimensional vector of Lagrange multipliers (see Appendix B, Section B.8). Since both $\mathbf { x }$ and $\lambda$ are unknown, the necessary condition for a minimum of $J ( \mathbf { x } , \lambda )$ is that its derivative with respect to $\mathbf { x }$ and $\boldsymbol { \lambda }$ vanish. This leads to

$$
\begin{array} { r l r } { \frac { \partial J ( \mathbf { x } , \lambda ) } { \partial \mathbf { x } } } & { = 0 = } & { \mathbf { x } - H ^ { T } \lambda } \\ { \frac { \partial J ( \mathbf { x } , \lambda ) } { \partial \lambda } } & { = 0 = } & { \mathbf { y } - H \mathbf { x } . } \end{array}
$$

Substituting the expression for $\hat { \bf x }$ from Eq. (4.3.9) into Eq. (4.3.10) yields

$$
\mathbf { y } = H H ^ { T } \lambda ,
$$

and solving for $\lambda$ ,

$$
\begin{array} { r } { \pmb { \lambda } = ( H H ^ { T } ) ^ { - 1 } \mathbf { y } . } \end{array}
$$

Substituting Eq. (4.3.12) into Eq. (4.3.9) yields

$$
\hat { \mathbf { x } } = H ^ { T } ( H H ^ { T } ) ^ { - 1 } \mathbf { y }
$$

where $H H ^ { T }$ is an $m \times m$ matrix of rank $m$ . The quantities $H ^ { T } ( H H ^ { T } ) ^ { - 1 }$ of Eq. (4.3.13) and $( H ^ { T } H ) ^ { - 1 } H ^ { T }$ of Eq. (4.3.6) are called the pseudo inverses of $H$ in the equation $H \hat { \mathbf { x } } = \mathbf { y }$ . They apply when there are more unknowns than equations or more equations than unknowns, respectively. Eq. (4.3.13) is the solution for $\mathbf { x }$ of minimum length. In summary,

$$
\begin{array} { r l } { \hat { \mathbf { x } } = ( H ^ { T } H ) ^ { - 1 } H ^ { T } \mathbf { y } , \quad } & { \mathrm { i f } \ m > n } \\ { \hat { \mathbf { x } } = H ^ { - 1 } \mathbf { y } , \quad } & { \mathrm { i f } \ m = n } \\ { \hat { \mathbf { x } } = H ^ { T } ( H H ^ { T } ) ^ { - 1 } \mathbf { y } , \quad } & { \mathrm { i f } \ m < n . } \end{array}
$$

# 4.3.2 SHORTCOMINGS OF THE LEAST SQUARES SOLUTION

Three major shortcomings of the simple least squares solution are:

1. Each observation error is weighted equally even though the accuracy of observations may differ.   
2. The observation errors may be correlated (not independent), and the simple least squares solution makes no allowance for this.   
3. The method does not consider that the errors are samples from a random process and makes no attempt to utilize any statistical information.

The first of these objections is overcome through the use of the weighted least squares approach.

# 4.3.3 WEIGHTED LEAST SQUARES SOLUTION

Equation (4.3.14) has no means of preferentially ordering one observation with respect to another. A more general expression can be obtained by considering the following formulation. Given a vector sequence of observations $\mathbf { y } _ { 1 }$ , $\mathbf { y } _ { 2 } , \ldots .$ , $\mathbf { y } _ { \ell }$ related through the state transition matrix to the state at some epoch time, $\mathbf { x } _ { k }$ , and an associated weighting matrix, $w _ { i }$ , for each of the observation vectors, one can write

$$
\begin{array} { r l } { \mathbf { y } _ { 1 } = H _ { 1 } \mathbf { x } _ { k } + \boldsymbol { \epsilon } _ { 1 } ; } & { { } \quad w _ { 1 } } \\ { \mathbf { y } _ { 2 } = H _ { 2 } \mathbf { x } _ { k } + \boldsymbol { \epsilon } _ { 2 } ; } & { { } \quad w _ { 2 } } \\ { \vdots \vdots \vdots \vdots } \\ { \mathbf { y } _ { \ell } = H _ { \ell } \mathbf { x } _ { k } + \boldsymbol { \epsilon } _ { \ell } ; } & { { } \quad w _ { \ell } } \end{array}
$$

where

$$
H _ { i } = \widetilde { H } _ { i } \Phi ( t _ { i } , t _ { k } ) .
$$

In Eq. (4.3.15) the weighting matrices, $w _ { i }$ , are assumed to be diagonal with their elements normalized to a range between zero and one. Observations weighted with a one would be given the highest possible weight and those weighted with zero would be neglected. To reduce Eq. (4.3.15) to an expression similar to (4.2.14), the following definitions can be used:

$$
\mathbf { y } = \left[ \begin{array} { c } { \mathbf { y } _ { 1 } } \\ { \mathbf { y } _ { 2 } } \\ { \vdots } \\ { \mathbf { y } _ { \ell } } \end{array} \right] ; \quad H = \left[ \begin{array} { c } { H _ { 1 } } \\ { H _ { 2 } } \\ { \vdots } \\ { H _ { \ell } } \end{array} \right] ;
$$

$$
\begin{array} { r } { \epsilon = \left[ \begin{array} { l } { \epsilon _ { 1 } } \\ { \epsilon _ { 2 } } \\ { \vdots } \\ { \epsilon _ { \ell } } \end{array} \right] ; \quad W = \left[ \begin{array} { l l l l } { w _ { 1 } } & { 0 } & { \cdot \cdot } & { 0 } \\ { 0 } & { w _ { 2 } } & { \cdot \cdot } & { 0 } \\ & & { \cdot } & \\ { 0 } & { 0 } & { \cdot \cdot } & { w _ { \ell } } \end{array} \right] . } \end{array}
$$

Each observation $\mathbf { y } _ { i }$ is assumed to be a $p$ -vector and $\mathbf { x } _ { k }$ is an $n$ -vector. Equation (4.3.15) now can be expressed as

$$
\mathbf { y } = H \mathbf { x } _ { k } + \epsilon ; \quad W .
$$

One can then pose the weighted least squares problem as follows. Given the linear observation state relationship expressed by (4.3.17), find the estimate of $\mathbf { x } _ { k }$ to minimize the weighted sum of the squares of the calculated observation errors. The performance index is

$$
J ( \mathbf { x } _ { k } ) = 1 / 2 { \boldsymbol { \epsilon } } ^ { T } W { \boldsymbol { \epsilon } } = \sum _ { i = 1 } ^ { \ell } 1 / 2 \epsilon _ { i } ^ { T } w _ { i } \epsilon _ { i } .
$$

Using Eq. (4.3.17), $J ( \mathbf { x } _ { k } )$ can be expressed as

$$
J ( \mathbf { x } _ { k } ) = 1 / 2 ( \mathbf { y } - H \mathbf { x } _ { k } ) ^ { T } W ( \mathbf { y } - H \mathbf { x } _ { k } ) .
$$

A necessary condition for a minimum of $J ( \mathbf { x } _ { k } )$ is that its first derivative with respect to $\mathbf { x } _ { k }$ vanishes (see Eq. B.7.4),

$$
\frac { \partial J } { \partial \mathbf { x } _ { k } } = 0 = - ( y - H \mathbf { x } _ { k } ) ^ { T } W H = - H ^ { T } W ( \mathbf { y } - H \mathbf { x } _ { k } ) .
$$

This expression can be rearranged to obtain the normal equations analogous to Eq. (4.3.6) in the least squares formulation as

$$
( H ^ { T } W H ) \mathbf { x } _ { k } = H ^ { T } W \mathbf { y } .
$$

If the normal matrix $H ^ { T } W H$ is positive defini te, it will have an inverse and the solution to (4.3.21) is

$$
\begin{array} { r } { \hat { \mathbf { x } } _ { k } = ( H ^ { T } W H ) ^ { - 1 } H ^ { T } W \mathbf { y } . } \end{array}
$$

The value of $\hat { \mathbf { x } } _ { k }$ given by Eq. (4.3.22) is the weighted least squares estimate and is the estimate that minimizes the sum of squares of the weighted observation errors. Note that Eq. (4.3.22) can be expressed as

$$
\begin{array} { r } { \hat { \mathbf { x } } _ { k } = P _ { k } H ^ { T } W \mathbf { y } , } \end{array}
$$

where

$$
P _ { k } = ( H ^ { T } W H ) ^ { - 1 } .
$$

The $n \times n$ matrix $P _ { k }$ is symmetric, as can be seen from the definiti on. Furthermore, if it exists, it must be positive definite, since it is computed as the inverse of the positive definite matrix, $H ^ { T } W H$ . The parameter observability is related to the rank of this matrix. If all the parameters in $\mathbf { x } _ { k }$ are observable (i.e., can be uniquely determined with the observation set y), then $P _ { k }$ will be full rank and $P _ { k }$ will have an inverse. The number of independent observations must be greater than or equal to the number of parameters being estimated if $P _ { k }$ is to be invertible. Furthermore, $P _ { k }$ is related to the accuracy of the estimate, $\hat { \mathbf { x } } _ { k }$ . In general, the larger the magnitude of the elements of the matrix, $P _ { k }$ , the less accurate the estimate. Since the weighting matrix, $W$ , usually results from an initial judgment on the accuracy of the observations followed by a normalization procedure to scale the weights to values between zero and one, this interpretation is not strictly valid in the statistical sense. Hence, some caution should be used when attempting to infer the accuracy of an estimate from the magnitude of $P _ { k }$ as obtained in the weighted least squares estimate. In Section 4.4, it will be shown that, with proper selection of $W$ , $P _ { k }$ is the variance-covariance matrix of the estimation error associated with $\hat { \mathbf { x } } _ { k }$ .

If an $a$ priori value, $\bar { \mathbf { x } } _ { k }$ , is available for $\mathbf { x } _ { k }$ and an associated weighting matrix, $\overline { { W } } _ { k }$ , is given, the weighted least squares estimate for $\mathbf { x } _ { k }$ can be obtained by choosing for $\hat { \mathbf { x } } _ { k }$ the value of $\mathbf { x } _ { k }$ , which minimizes the performance index

$$
J ( { \bf x } _ { k } ) = 1 / 2 ( { \bf y } - H { \bf x } _ { k } ) ^ { T } W ( { \bf y } - H { \bf x } _ { k } ) + 1 / 2 ( \bar { \bf x } _ { k } - { \bf x } _ { k } ) ^ { T } \overline { { W } } _ { k } ( \bar { \bf x } _ { k } - { \bf x } _ { k } ) .
$$

This results in

$$
\hat { \mathbf { x } } _ { k } = ( H ^ { T } W H + \overline { { W } } _ { k } ) ^ { - 1 } ( H ^ { T } W \mathbf { y } + \overline { { W } } _ { k } \bar { \mathbf { x } } _ { k } ) .
$$

Here $\bar { \bf x } _ { k }$ represents an a priori estimate of $\mathbf { x } _ { k }$ and $\overline { { W } } _ { k }$ represents a weighting matrix for the a priori estimate of $\mathbf { x } _ { k }$ . In Section 4.4 these terms will be introduced in terms of their statistical significance .

# 4.3.4 AN ALTERNATE LEAST SQUARES APPROACH

A somewhat classic approach to the problem of least squares that was introduced in Section 1.2.3 is described in this section. Assume that we have $\ell$ scalar

observations. The following least squares performance index, or cost function, can be defined:

$$
J = \sum _ { j = 1 } ^ { \ell } { ( O _ { j } - C _ { j } ) ^ { 2 } } ,
$$

where $O _ { j }$ is the observation, such as range, provided by an instrument; $C _ { j }$ is the computed observation using the reference value of $\mathbf { X } _ { j } ^ { * }$ ; and $\ell$ is the number of observations. $C _ { j }$ is computed from the appropriate observation-state model for the measurement, and is based on a reference set of coordinates for the instrument and for the satellite. In classic terminology, $( O _ { j } - C _ { j } )$ is referred to as $o$ minus $C$ and represents an observation residual. The coordinates of the satellite are available as the solution to the equations of motion; for example, Eq. (2.3.31) with a specified set of initial conditions, represented by the position and velocity of the satellite at time $t _ { 0 }$ . The state vector at $t _ { 0 }$ , $\mathbf { X } ( t _ { 0 } )$ , represents the initial position and velocity, specifically

$$
\begin{array} { r } { \mathbf { X } ( t _ { 0 } ) = \left[ \begin{array} { l } { X _ { 0 } } \\ { Y _ { 0 } } \\ { Z _ { 0 } } \\ { \dot { X } _ { 0 } } \\ { \dot { Y } _ { 0 } } \\ { \dot { Z } _ { 0 } } \end{array} \right] . } \end{array}
$$

As in the traditional least squares problem, the goal is to determine the initial conditions that minimize $J$ in Eq. (4.3.26). Thus, the partial derivatives with respect to $\mathbf { X } ( t _ { 0 } )$ must be zero:

$$
\begin{array} { r c l } { \displaystyle \frac { \partial J } { \partial X _ { 0 } } } & { = 0 } & { \displaystyle = \sum _ { j = 1 } ^ { \ell } 2 ( O _ { j } - C _ { j } ) \left( - \frac { \partial C _ { j } } { \partial X _ { 0 } } \right) } \\ & & { \vdots } \\ { \displaystyle \frac { \partial J } { \partial \dot { Z } _ { 0 } } } & { = 0 } & { \displaystyle = \sum _ { j = 1 } ^ { \ell } 2 ( O _ { j } - C _ { j } ) \left( - \frac { \partial C _ { j } } { \partial \dot { Z } _ { 0 } } \right) . } \end{array}
$$

These nonlinear algebraic equations can be written as

$$
\begin{array} { r c l } { { { \cal F } _ { 1 } } } & { { = } } & { { \displaystyle \sum _ { j = 1 } ^ { \ell } ( { \cal O } _ { j } - C _ { j } ) \left( \frac { \partial C _ { j } } { \partial X _ { 0 } } \right) } } \\ { { . } } & { { } } & { { } } \\ { { \vdots } } & { { } } & { { } } \end{array}
$$

$$
\begin{array} { r c l } { F _ { 6 } } & { = } & { \displaystyle \sum _ { j = 1 } ^ { \ell } ( { \cal O } _ { j } - C _ { j } ) \left( \frac { \partial C _ { j } } { \partial \dot { Z } _ { 0 } } \right) . } \end{array}
$$

From Eqs. (4.3.28) and (4.3.29), the following vector equation is defined:

$$
\mathbf { F } = { \left[ \begin{array} { l } { F _ { 1 } } \\ { F _ { 2 } } \\ { F _ { 3 } } \\ { F _ { 4 } } \\ { F _ { 5 } } \\ { F _ { 6 } } \end{array} \right] } = 0 .
$$

The problem is to solve these equations for the value of $\mathbf { X } ( t _ { 0 } )$ , which produces the condition that $\mathbf { F } = 0$ . Eq. (4.3.30) represents a set of nonlinear algebraic equations in the $n$ unknown components of $\mathbf { X } ( t _ { 0 } )$ .

The solution to a set of nonlinear algebraic equations can be accomplished with the well-known Newton–Raphson method, which usually is derived for a single equation. As shown by Dahlquist and Bjorck (1974), a nonlinear set of ¨ equations can be solved in a recursive manner by

$$
{ \bf X } ( t _ { 0 } ) _ { n + 1 } = { \bf X } ( t _ { 0 } ) _ { n } - \left[ \frac { \partial { \bf F } } { \partial { \bf X } } \right] _ { n } ^ { - 1 } [ { \bf F } ] _ { n } ,
$$

where

$$
{ \frac { \partial \mathbf { F } } { \partial \mathbf { X } } } = \left[ \begin{array} { c c c c c c } { { \frac { \partial F _ { 1 } } { \partial X _ { 0 } } } } & { { \frac { \partial F _ { 1 } } { \partial Y _ { 0 } } } } & { { \frac { \partial F _ { 1 } } { \partial Z _ { 0 } } } } & { { \frac { \partial F _ { 1 } } { \partial \dot { X } _ { 0 } } } } & { { \frac { \partial F _ { 1 } } { \partial \dot { Y } _ { 0 } } } } & { { \frac { \partial F _ { 1 } } { \partial \dot { Z } _ { 0 } } } } \\ { \vdots } & & & & & { \vdots } \\ { { \frac { \partial F _ { 6 } } { \partial X _ { 0 } } } } & { { \frac { \partial F _ { 6 } } { \partial Y _ { 0 } } } } & { { \frac { \partial F _ { 6 } } { \partial Z _ { 0 } } } } & { { \frac { \partial F _ { 6 } } { \partial \dot { X } _ { 0 } } } } & { { \frac { \partial F _ { 6 } } { \partial \dot { Y } _ { 0 } } } } & { { \frac { \partial F _ { 6 } } { \partial \dot { Z } _ { 0 } } } } \end{array} \right]
$$

and where $n$ represents the iteration number. It is evident that the method requires an initial guess corresponding to $n = 0$ . Consider, for example,

$$
\frac { \partial F _ { 1 } } { \partial X _ { 0 } } = \sum _ { j = 1 } ^ { \ell } \left[ \left( - \frac { \partial C _ { j } } { \partial X _ { 0 } } \right) \left( \frac { \partial C _ { j } } { \partial X _ { 0 } } \right) + ( O _ { j } - C _ { j } ) \left( \frac { \partial ^ { 2 } C _ { j } } { \partial X _ { 0 } ^ { 2 } } \right) \right]
$$

and

$$
\frac { \partial F _ { 1 } } { \partial Y _ { 0 } } = \sum _ { j = 1 } ^ { \ell } \left[ \left( - \frac { \partial C _ { j } } { \partial Y _ { 0 } } \right) \left( \frac { \partial C _ { j } } { \partial X _ { 0 } } \right) + ( O _ { j } - C _ { j } ) \left( \frac { \partial ^ { 2 } C _ { j } } { \partial X _ { 0 } \partial Y _ { 0 } } \right) \right] .
$$

In a converged solution, or nearly converged case, the $( O _ { j } - C _ { j } )$ can be expected to be small, thereby providing a reasonable justifica tion for ignoring the terms involving the second partial derivative of $C _ { j }$ .

The solution to these nonlinear equations, $\mathbf { X } ( t _ { 0 } )$ , can then be written as

$$
{ \bf X } ( t _ { 0 } ) _ { n + 1 } =
$$

$$
\mathbf { X } ( t _ { 0 } ) _ { n } + \left[ \begin{array} { c c c c } { \displaystyle \sum _ { j } \left( \frac { \partial C _ { j } } { \partial X _ { 0 } } \right) _ { n } ^ { 2 } } & { \cdots } & { \displaystyle \sum _ { j } \left( \frac { \partial C _ { j } } { \partial X _ { 0 } } \right) _ { n } \left( \frac { \partial C _ { j } } { \partial \tilde { Z } _ { 0 } } \right) _ { n } } \\ { \vdots } & { } & { } & { } \\ { \displaystyle \sum _ { j } \left( \frac { \partial C _ { j } } { \partial X _ { 0 } } \right) _ { n } \left( \frac { \partial C _ { j } } { \partial \tilde { Z } _ { 0 } } \right) _ { n } } & { \cdots } & { \displaystyle \sum _ { j } \left( \frac { \partial C _ { j } } { \partial \tilde { Z } _ { 0 } } \right) _ { n } ^ { 2 } } \\ { \vdots } & { } & { } & { } \\ { \displaystyle \sum _ { j } \left( \frac { \partial C _ { j } } { \partial \tilde { Z } _ { 0 } } \right) _ { n } \left( \mathcal { O } _ { j } - C _ { j } \right) _ { n } } \end{array} \right]
$$

where the terms involving the second partial derivatives have been ignored. Note that, for example,

$$
{ \frac { \partial C _ { j } } { \partial X _ { 0 } } } = { \frac { \partial C _ { j } } { \partial X } } { \frac { \partial X } { \partial X _ { 0 } } } + { \frac { \partial C _ { j } } { \partial Y } } { \frac { \partial Y } { \partial X _ { 0 } } } + \cdots + { \frac { \partial C _ { j } } { \partial \dot { Z } } } { \frac { \partial \dot { Z } } { \partial X _ { 0 } } }
$$

and it can be readily shown from

$$
H = \widetilde { H } \Phi
$$

that Eq. (4.3.31) is

$$
\mathbf { X } ( t _ { 0 } ) _ { n + 1 } = \mathbf { X } ( t _ { 0 } ) _ { n } + ( H _ { n } ^ { T } H _ { n } ) ^ { - 1 } H _ { n } ^ { T } \mathbf { y } _ { n }
$$

where ${ \bf y } _ { n }$ represents a vector of residuals $( \mathbf { O } - \mathbf { C } ) _ { n }$ where $\mathbf { O }$ and $\mathbf { C }$ correspond to $\mathbf { Y }$ and $\mathbf { Y ^ { * } }$ in the notation used in Section 4.2. Furthermore, if

$$
\hat { \mathbf { x } } _ { n + 1 } = \mathbf { X } ( t _ { 0 } ) _ { n + 1 } - \mathbf { X } ( t _ { 0 } ) _ { n } ,
$$

it follows that

$$
\hat { \mathbf { x } } _ { n + 1 } = ( H _ { n } ^ { T } H _ { n } ) ^ { - 1 } H _ { n } ^ { T } \mathbf { y } _ { n }
$$

corresponding to Eq. (4.3.6).

Some further conclusions can be drawn using this approach:

(1) For the orbit determination application, the least squares solution should be iterated, especially when the reference trajectory has significant deviations from the true trajectory.

(2) Ignoring the second partial derivatives in Eq. (4.3.33) may influence the convergence process if the deviations are large.

(3) Since the process is based on the Newton–Raphson method, it will exhibit quadratic convergence when near to the solution, namely

$$
| | \hat { \mathbf { x } } _ { n } | | < | | \hat { \mathbf { x } } _ { n - 1 } | | ^ { 2 } .
$$

(4) The least squares formulation allows accumulation in a sequential manner as illustrated by the summations in Eq. (4.3.33). That is, the method can be formulated to accumulate the measurements sequentially, followed by a matrix inversion or linear system solution.

(5) The iterative process for a specified set of observations can be repeated until, for example, $| | \hat { \mathbf { x } } _ { n + 1 } | |$ is smaller than some convergence criteria.

# Example 4.3.1

Section 3.6 illustrated the range residuals that would be obtained from two stations (Easter Island and Fortaleza, Brazil) for a specified error in the initial conditions of the two-body problem. The orbit error is illustrated in Fig. 2.2.9. For this case, the satellite is observed twice by Easter Island and once by Fortaleza in the time interval shown in Fig. 2.2.9, ignoring one pass from Fortaleza that rises less than one degree in elevation above the horizon. The true (and presumably unknown) initial conditions are given by Example 2.2.6.2 and the nominal or reference initial conditions (presumably known) are given by Example 2.2.4.1.

Using the algorithm described in this section for the three passes, assuming that error-free geometric ranges are collected every 20 seconds when the satellite is above the station’s horizon, the results for the state corrections are shown in Table 4.3.1. To obtain these results, the Goodyear state transition matrix (Section 2.2.6) was used, but a numerically integrated state transition matrix, as given by Eqs. (4.2.1) and (4.2.10), could have been used. Note that the initial state being determined is expressed in the nonrotating system, so the partial derivatives comprising H must be found in that system. To form these partial derivatives, the station coordinates must be transformed from Earth-fix ed to nonrotating. It is apparent from Table 4.3.1 that the method converges rapidly, since the error that exists after the first iteration is small (see Fig. 2.2.9).

Estimated Corrections1   

<table><tr><td></td><td colspan="3">Iteration Number</td></tr><tr><td>X</td><td>1</td><td>2</td><td>3</td></tr><tr><td>x</td><td>0.808885</td><td>0.000566</td><td>0.000000</td></tr><tr><td>9</td><td>0.586653</td><td>0.000536</td><td>0.000000</td></tr><tr><td>20</td><td>0.000015</td><td>0.000425</td><td>0.000000</td></tr><tr><td>30</td><td>0.000000</td><td>0.000000</td><td>0.000000</td></tr><tr><td>： y</td><td>0.000000</td><td>0.000000</td><td>0.000000</td></tr><tr><td>之</td><td>0.000000</td><td>0.000000</td><td>0.000000</td></tr></table>

1 Data: three passes described in Section 3.6 2 Compare to Example 2.2.6.2

Table 4.3.1:   

<table><tr><td>Converged State²</td><td></td></tr><tr><td>(X(to))</td><td></td></tr><tr><td>X0</td><td>5492001.14945 m 3984001.98719</td></tr><tr><td></td><td>m 2955.81044</td></tr><tr><td></td><td>m</td></tr><tr><td></td><td>-3931.046491 m/sec</td></tr><tr><td></td><td>5498.676921 m/sec</td></tr><tr><td></td><td>3665.980697 m/sec</td></tr></table>

If only the firs t pass from Easter Island is used instead of three passes, a dramatically different result is obtained. With 33 observations, the correction on the first iteration is at the 100-meter level in position and the $0 . 1 \mathrm { - m / s e c }$ level in velocity. The subsequent iteration produces corrections at a comparable level, but numerical instabilities are encountered on the third iteration. Close examination shows that $( H ^ { T } H )$ in Eq. (4.3.37) is ill conditioned. Explanation of this behavior is discussed in Section 4.12.

# 4.4 THE MINIMUM VARIANCE ESTIMATE

As noted, the least squares and weighted least squares methods do not include any information on the statistical characteristics of the measurement errors or the a priori errors in the values of the parameters to be estimated. The minimum variance approach is one method for removing this limitation. The minimum variance criterion is used widely in developing solutions to estimation problems because of the simplicity in its use. It has the advantage that the complete statistical description of the random errors in the problem is not required. Rather, only the first and second moments of the probability density function of the observation errors are required. This information is expressed in the mean and covariance matrix associated with the random error.

If it is assumed that the observation error $\epsilon _ { i }$ is random with zero mean and specified covariance, the state estimation problem can be formulated as follows:

Given: The system of state-propagation equations and observation state equations

$$
\begin{array} { r l } & { { \mathbf x } _ { i } = \Phi ( t _ { i } , t _ { k } ) { \mathbf x } _ { k } } \\ & { { \mathbf y } _ { i } = \widetilde { H } _ { i } { \mathbf x } _ { i } + \epsilon _ { i } \quad i = 1 , \dots , \ell . } \end{array}
$$

Find: The linear, unbiased, minimum variance estimate, $\hat { \mathbf { x } } _ { k }$ , of the state $\mathbf { x } _ { k }$

The solution to this problem proceeds as follows. Using the state transition matrix and the definit ions of Eq. (4.3.16), reduce Eq. (4.4.2) to the following form

$$
\mathbf { y } = H \mathbf { x } _ { k } + \epsilon
$$

where

$$
\begin{array} { r } { E [ \epsilon ] = \left[ \begin{array} { l } { E [ \epsilon _ { 1 } ] } \\ { E [ \epsilon _ { 2 } ] } \\ { \vdots } \\ { E [ \epsilon _ { \ell } ] } \end{array} \right] = \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { \vdots } \\ { 0 } \end{array} \right] \quad E [ \epsilon \epsilon ^ { T } ] = \left[ \begin{array} { l l l } { R _ { 1 1 } R _ { 1 2 } } & { \cdots } & { R _ { 1 \ell } } \\ { R _ { 1 2 } ^ { T } R _ { 2 2 } } & { \cdots } & { R _ { 2 \ell } } \\ { \vdots } & { \ddots } & { \vdots } \\ { R _ { 1 \ell } ^ { T } } & { \cdots } & { R _ { \ell \ell } } \end{array} \right] = R . } \end{array}
$$

Generally, $R _ { 1 1 } = R _ { 2 2 } = \ldots = R e _ { }$ and $R _ { i j } ~ = ~ 0$ $( i \neq j )$ , but this is not a necessary restriction in the following argument. $R _ { i j } \neq 0 \ ( i \neq j )$ corresponds to the more general case of time-correlated observation errors.

From the problem statement, the estimate is to be the best linear, unbiased, minimum variance estimate. The consequences of each of these requirements are addressed in the following steps.

(1) Linear: The requirement of a linear estimate implies that the estimate is to be made up of a linear combination of the observations:

$$
{ \hat { \mathbf { x } } } _ { k } = M \mathbf { y } .
$$

The $( n \times m )$ matrix $M$ is unspecified and is to be selected to obtain the best estimate.

(2) Unbiased: If the estimate is unbiased, then by definition

$$
E [ { \hat { \mathbf { x } } } ] = \mathbf { x } .
$$

Substituting Eqs. (4.4.5) and (4.4.3) into Eq. (4.4.6) leads to the following requirement:

$$
E [ { \hat { \mathbf { x } } } _ { k } ] = E [ M \mathbf { y } ] = \ E [ M H \mathbf { x } _ { k } + M \mathbf { \epsilon } ] = \mathbf { x } _ { k } .
$$

But, since $E [ \epsilon ] = 0$ , this reduces to

$$
M H \mathbf { x } _ { k } = \mathbf { x } _ { k }
$$

from which the following constraint on $M$ is obtained

$$
M H = I .
$$

That is, if the estimate is to be unbiased, the linear mapping matrix $M$ must satisfy Eq. (4.4.7). This condition requires the rows of $M$ to be orthogonal to the columns of $H$ .

(3) Minimum Variance: If the estimate is unbiased, then the estimation error covariance matrix can be expressed as (see Appendix A)

$$
\begin{array} { r l } & { P _ { k } = E \left\{ \left[ ( \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ) - E ( \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ) \right] \left[ ( \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ) - E ( \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ) \right] ^ { T } \right\} } \\ & { \quad = E \big [ ( \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ) ( \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ) ^ { T } \big ] . } \end{array}
$$

Hence, the problem statement requires that $\hat { \mathbf { x } } _ { k }$ be selected to minimize $P _ { k }$ while satisfying Eqs. (4.4.6) and (4.4.7). By minimizing $P _ { k }$ , we mean that $P _ { k } ^ { * } - P _ { k }$ is nonnegative definite for any $P _ { k } ^ { * }$ that results from an $M$ that satisfies Eq. (4.4.7) (Deutsch, 1965). Substituting Eqs. (4.4.5) and (4.4.3) into Eq. (4.4.8) leads to the following result:

$$
\begin{array} { r l } & { P _ { k } = E [ ( M \mathbf { y } - \mathbf { x } _ { k } ) ( M \mathbf { y } - \mathbf { x } _ { k } ) ^ { T } ] } \\ & { \quad = E [ \{ M ( H \mathbf { x } _ { k } + \epsilon ) - \mathbf { x } _ { k } \} \{ M ( H \mathbf { x } _ { k } + \epsilon ) - \mathbf { x } _ { k } \} ^ { T } ] } \\ & { \quad = E [ M \epsilon \epsilon ^ { T } M ^ { T } ] } \end{array}
$$

where we have used $M H = I$ . It follows from Eq. (4.4.4) that the covariance matrix can be written as

$$
P _ { k } = M R M ^ { T }
$$

where $M$ is to be selected to satisfy Eq. (4.4.7). To involve the constraint imposed by Eq. (4.4.7) and to keep the constrained relation for $P _ { k }$ symmetric, Eq. (4.4.7) is adjoined to Eq. (4.4.9) in the following form

$$
P _ { k } = M R M ^ { T } + \Lambda ^ { T } ( I - M H ) ^ { T } + ( I - M H ) \Lambda
$$

where $\Lambda$ is a $n \times n$ matrix of unspecified Lagrange multipliers. The fina l term is added to ensure that $P _ { k }$ remains symmetric. For a minimum of $P _ { k }$ , it is necessary that its first variation with respect to $M$ vanish, and that $I - M H = 0$ . Accordingly,

$$
\delta P _ { k } = 0 = ( M R - \Lambda ^ { T } H ^ { T } ) \delta M ^ { T } \ + \delta M ( R M ^ { T } - H \Lambda ) .
$$

Now, if $\delta P _ { k }$ is to vanish for an arbitrary $\delta M$ , one of the following conditions must be met:

1. $R M ^ { T } - H \Lambda = 0$

2. δM and/or $R M ^ { T } - H \Lambda$ must not be of full rank.

We will impose condition 1 and show that this yields a minimum value of $P$ . Hence, it is required that

$$
M R - \Lambda ^ { T } H ^ { T } = 0 , \quad I - M H = 0 .
$$

From the firs t of these conditions

$$
M = \Lambda ^ { T } H ^ { T } R ^ { - 1 }
$$

since $R$ is assumed to be positive definite. Substituting Eq. (4.4.13) into the second of Eqs. (4.4.12) leads to the following result

$$
\begin{array} { r } { \Lambda ^ { T } ( H ^ { T } R ^ { - 1 } H ) = I . } \end{array}
$$

Now, if the matrix $H ^ { T } R ^ { - 1 } H$ is full rank, which requires that $m \geq n$ , then the inverse matrix will exist and

$$
\begin{array} { r } { \Lambda ^ { T } = ( H ^ { T } R ^ { - 1 } H ) ^ { - 1 } . } \end{array}
$$

Then, in view of Eq. (4.4.13),

$$
M = ( H ^ { T } R ^ { - 1 } H ) ^ { - 1 } H ^ { T } R ^ { - 1 } .
$$

This is the value of $M$ that satisfies the unbiased and minimum variance requirements. Substitution of Eq. (4.4.16) into Eq. (4.4.9) leads to the following expression for the covariance matrix:

$$
P _ { k } = ( H ^ { T } R ^ { - 1 } H ) ^ { - 1 } .
$$

With Eqs. (4.4.16) and (4.4.5), the linear unbiased minimum variance estimate of $\mathbf { x } _ { k }$ is given as

$$
\begin{array} { r } { \hat { \mathbf { x } } _ { k } = ( H ^ { T } R ^ { - 1 } H ) ^ { - 1 } H ^ { T } R ^ { - 1 } \mathbf { y } . } \end{array}
$$

It is not obvious that requiring $R M ^ { T } - H \Lambda = 0$ yields the minimum estimation error covariance matrix. We now demonstrate that $P _ { k } ^ { * } - P _ { k }$ is nonnegative definite, where $P _ { k } ^ { * }$ is the covariance matrix associated with any other linear unbiased estimator, $\tilde { \mathbf { x } }$ . Without loss of generality let

$$
\widetilde { \mathbf { x } } = \hat { \mathbf { x } } + B \mathbf { y } .
$$

Then

$$
\begin{array} { r } { E [ \widetilde { \mathbf { x } } ] = E [ \hat { \mathbf { x } } ] + B E [ \mathbf { y } ] } \\ { = \mathbf { x } + B H \mathbf { x } . \qquad } \end{array}
$$

Hence, $B H = 0$ in order for $\widetilde { \mathbf { x } }$ to be unbiased. Since $H$ is full rank, $B$ cannot be full rank. We ignore the trivial solution $B = 0$ .

Computing the estimation error covariance matrix associated with $\widetilde { \mathbf { x } }$ yields

$$
\begin{array} { r l } & { P _ { \tilde { \mathbf { x } } } = E \Big [ \big ( \tilde { \mathbf { x } } - E ( \tilde { \mathbf { x } } ) \big ) \big ( \tilde { \mathbf { x } } - E ( \tilde { \mathbf { x } } ) \big ) ^ { T } \Big ] } \\ & { \quad = E \left[ \big ( \hat { \mathbf { x } } + B \mathbf { y } - \mathbf { x } - B H \mathbf { x } \big ) \big ( \hat { \mathbf { x } } + B \mathbf { y } - \mathbf { x } - B H \mathbf { x } \big ) ^ { T } \right] } \\ & { \quad = E \left[ \big ( ( \hat { \mathbf { x } } - \mathbf { x } ) + B \boldsymbol { \epsilon } \big ) \big ( ( \hat { \mathbf { x } } - \mathbf { x } ) + B \boldsymbol { \epsilon } \big ) ^ { T } \right] } \\ & { \quad = P + B R B ^ { T } + E \left[ \big ( \hat { \mathbf { x } } - \mathbf { x } \big ) \boldsymbol { \epsilon } ^ { T } \right] B ^ { T } + B E \left[ \boldsymbol { \epsilon } \big ( \hat { \mathbf { x } } - \mathbf { x } \big ) ^ { T } \right] . } \end{array}
$$

Also,

$$
\begin{array} { r l } & { B E \left[ \epsilon ( \hat { \mathbf { x } } - \mathbf { x } ) ^ { T } \right] = B E \left[ \epsilon ( P H ^ { T } R ^ { - 1 } \mathbf { y } - \mathbf { x } ) ^ { T } \right] } \\ & { \qquad = B E \left[ \epsilon ( P H ^ { T } R ^ { - 1 } ( H \mathbf { x } + \epsilon ) - \mathbf { x } ) ^ { T } \right] } \\ & { \qquad = B E ( \epsilon \epsilon ^ { T } ) R ^ { - 1 } H P } \\ & { \qquad = B H P = 0 , } \end{array}
$$

since $B H = 0$ .

Hence,

$$
P _ { \tilde { \mathbf { x } } } - P = B R B ^ { T }
$$

Because $B$ is not of full rank, $B R B ^ { T }$ must be positive semidefinite (i.e., its diagonal elements are each $\geq 0$ ). Hence, the requirement that the difference of the two covariance matrices be nonnegative defini te has been met. Consequently, all variances associated with $P _ { \tilde { \mathbf { x } } }$ must be greater than or equal to those of $P$ and the trace of $P _ { \tilde { \mathbf { x } } }$ must be greater than that of $P$ .

Note that computation of the estimate, $\hat { \mathbf { x } } _ { k }$ , requires inverting the $n \times n$ normal matrix, $H ^ { T } R ^ { - 1 } H$ . For a large dimension system the computation of this inverse may be difficul t. The solution given by Eq. (4.4.18) will agree with the weighted least squares solution if the weighting matrix, $W$ , used in the least squares approach is equal to the inverse of the observation noise covariance matrix; that is, if $W = R ^ { - 1 }$ .

# 4.4.1 PROPAGATION OF THE ESTIMATE AND COVARIANCEMATRIX

If the estimate at a time $t _ { j }$ is obtained by using Eq. (4.4.18), the estimate may be mapped to any later time by using Eq. (4.4.2):

$$
\begin{array} { r } { \overline { { \bf x } } _ { k } = \Phi ( t _ { k } , t _ { j } ) \hat { \bf x } _ { j } . } \end{array}
$$

The expression for propagating the covariance matrix can be obtained as follows:

$$
\overline { { P } } _ { k } \equiv E \big [ ( \overline { { \mathbf { x } } } _ { k } - \mathbf { x } _ { k } ) \big ( \overline { { \mathbf { x } } } _ { k } - \mathbf { x } _ { k } \big ) ^ { T } \big ] .
$$

In view of Eq. (4.4.19), Eq. (4.4.20) becomes

$$
\begin{array} { r } { \overline { { P } } _ { k } = E [ \Phi ( t _ { k } , t _ { j } ) ( \hat { \mathbf { x } } _ { j } - \mathbf { x } _ { j } ) ( \hat { \mathbf { x } } _ { j } - \mathbf { x } _ { j } ) ^ { T } \Phi ^ { T } ( t _ { k } , t _ { j } ) ] . } \end{array}
$$

Since the state transition matrix is deterministic, it follows from Eq. (4.4.8) that

$$
\overline { { \boldsymbol { P } } } _ { k } = \Phi ( t _ { k } , t _ { j } ) P _ { j } \Phi ^ { T } ( t _ { k } , t _ { j } ) .
$$

Equations (4.4.19) and (4.4.22) can be used to map the estimate of the state and its associated covariance matrix from $t _ { j }$ to $t _ { k }$ .

# 4.4.2 MINIMUM VARIANCE ESTIMATE WITH A Priori INFORMATION

If an estimate and the associated covariance matrix are obtained at a time $t _ { j }$ , and an additional observation or observation sequence is obtained at a time $t _ { k }$ , the estimate and the observation can be combined in a straightforward manner to obtain the new estimate $\hat { \mathbf { x } } _ { k }$ . The estimate, $\hat { \mathbf { x } } _ { j }$ , and associated covariance, $P _ { j }$ , are propagated forward to $t _ { k }$ using Eqs. (4.4.19) and (4.4.22) and are given by

$$
\begin{array} { r } { \overline { { \bf x } } _ { k } = \Phi ( t _ { k } , t _ { j } ) \hat { \bf x } _ { j } , ~ \overline { { P } } _ { k } = \Phi ( t _ { k } , t _ { j } ) P _ { j } \Phi ^ { T } ( t _ { k } , t _ { j } ) . } \end{array}
$$

The problem to be considered can be stated as follows:

Given: $\overline { { \mathbf { x } } } _ { k }$ , $\overline { { P } } _ { k }$ and $\mathbf { y } _ { k } = \widetilde { H } _ { k } \mathbf { x } _ { k } + \boldsymbol { \epsilon } _ { k }$ , where $E [ \epsilon _ { k } ] = 0 , E [ \epsilon _ { k } \epsilon _ { j } ^ { T } ] = R _ { k } \delta _ { k j }$ , and $E [ ( \bar { \bf x } _ { j } - { \bf x } _ { j } ) \epsilon _ { k } ^ { T } ] = 0$ , find the linear, minimum variance, unbiased estimate of $\mathbf { x } _ { k }$ .

The solution to the problem can be obtained by reducing it to the previously solved problem. To this end, note that if $\hat { \mathbf { x } } _ { j }$ is unbiased, $\overline { { \mathbf { x } } } _ { k }$ will be unbiased since

$E [ \overline { { \mathbf { x } } } _ { k } ] = \Phi ( t _ { k } , t _ { j } ) E [ \hat { \mathbf { x } } _ { j } ] = \mathbf { x } _ { k }$ . Hence, $\overline { { \mathbf { x } } } _ { k }$ can be interpreted as an unbiased observation of $\mathbf { x } _ { k }$ and we may treat it as an additional data equation at $t _ { k }$ ,

$$
\begin{array} { l } { { \mathbf { y } _ { k } = \widetilde { H } _ { k } { \mathbf { x } _ { k } } + \epsilon _ { k } } } \\ { { \mathbf { \overline { { x } } } _ { k } = { \mathbf { x } _ { k } } + \pmb { \eta } _ { k } } } \end{array}
$$

where

$$
\begin{array} { r l r } & { E [ \epsilon _ { k } ] = 0 , \quad E [ \epsilon _ { k } \epsilon _ { k } ^ { T } ] = R _ { k } , \quad } & { E [ \eta _ { k } ] = 0 , } \\ & { E [ \eta _ { k } \epsilon _ { k } ^ { T } ] = 0 , \mathrm { a n d } E [ \eta _ { k } \eta _ { k } ^ { T } ] = \overline { { P } } _ { k } . } & \end{array}
$$

It is assumed that the errors in the observations, $\epsilon _ { k }$ , are not correlated with the errors in the a priori estimate, $\eta _ { k }$ . That is, $E [ \eta _ { k } \epsilon _ { k } ^ { T } ] = 0$ . Now, if the following definitions are used

$$
\begin{array} { l } { { { \bf { y } } } = \left[ \begin{array} { l } { { { \bf { y } } _ { k } } } \\ { { \ldots } } \\ { { { \bf { \overline { { x } } } } _ { k } } } \end{array} \right] ; H = \left[ \begin{array} { l } { { { \widetilde { H } } _ { k } } } \\ { { \ldots } } \\ { { \cal I } } \end{array} \right] ; } \\ { { \epsilon } = \left[ \begin{array} { l } { { \epsilon _ { k } } } \\ { { \ldots } } \\ { { \eta _ { k } } } \end{array} \right] ; R = \left[ \begin{array} { l } { { R _ { k } } } \\ { { \ldots } } \\ { { \cal I } } \end{array} \right] ; } \end{array}
$$

Eq. (4.4.24) can be expressed as $\mathbf { y } = H \mathbf { x } _ { k } + \epsilon$ as in Eq. (4.4.3), and the solution for $\hat { \mathbf { x } } _ { k }$ is given by Eq. (4.4.18),

$$
\begin{array} { r } { \hat { \mathbf { x } } _ { k } = ( H ^ { T } R ^ { - 1 } H ) ^ { - 1 } H ^ { T } R ^ { - 1 } \mathbf { y } . } \end{array}
$$

In view of the definitions in Eq. (4.4.26),

$$
\begin{array} { r l r } & { } & { \hat { \bf x } _ { k } = \left\{ \left[ \widetilde { H } _ { k } ^ { T } : I \right] \left[ \begin{array} { c c } { R _ { k } ^ { - 1 } } & { 0 } \\ { \cdots } & { \cdots } \\ { 0 } & { \overline { { P } } _ { k } ^ { - 1 } } \end{array} \right] \left[ \begin{array} { c } { \widetilde { H } _ { k } } \\ { \cdots } \\ { I } \end{array} \right] \right\} ^ { - 1 } } \\ & { } & { \left\{ \left[ \widetilde { H } _ { k } ^ { T } : I \right] \left[ \begin{array} { c c } { R _ { k } ^ { - 1 } } & { 0 } \\ { \cdots } & { \cdots } \\ { 0 } & { \overline { { P } } _ { k } ^ { - 1 } } \end{array} \right] \left[ \begin{array} { c } { { \bf y } _ { k } } \\ { \cdots } \\ { \overline { { \bf x } } _ { k } } \end{array} \right] \right\} } \end{array}
$$

or

$$
\begin{array} { r } { \hat { \mathbf { x } } _ { k } = \big ( \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } + \overline { { P } } _ { k } ^ { - 1 } ) ^ { - 1 } \big ( \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \mathbf { y } _ { k } + \overline { { P } } _ { k } ^ { - 1 } \overline { { \mathbf { x } } } _ { k } \big ) . } \end{array}
$$

Using Eq. (4.4.17) the covariance matrix associated with the estimation error in $\hat { \bf x }$ easily is shown to be

$$
\begin{array} { r } { P _ { k } = E [ ( \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ) ( \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ) ^ { T } ] } \\ { = ( \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } + \overline { { P } } _ { k } ^ { - 1 } ) ^ { - 1 } . } \end{array}
$$

The inverse of the covariance matrix is called the information matrix,

$$
\Lambda _ { k } = P _ { k } ^ { - 1 } .
$$

Equation (4.4.29) often is seen written in normal equation form as

$$
\Lambda _ { k } \hat { \mathbf { x } } _ { k } = \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \mathbf { y } _ { k } + \overline { { P } } _ { k } ^ { - 1 } \bar { \mathbf { x } } _ { k } .
$$

The following remarks relate to Eq. (4.4.29):

1. The vector $\mathbf { y } _ { k }$ may be only a single observation or it may include a batch of observations mapped to $t _ { k }$ .   
2. The a priori estimate, $\overline { { \mathbf { x } } } _ { k }$ , may represent the estimate based on a priori initial conditions or the estimate based on the reduction of a previous batch of data.   
3. The $n \times n$ normal matrix of Eq. (4.4.29) must be inverted and if the dimension $n$ is large, this inversion can lead to computational problems. However, alternate solution techniques that avoid the accumulation and inversion of the normal matrix have been developed and are discussed in Chapter 5.   
4. The algorithm for using Eq. (4.4.29) is referred to as the batch processor. The name derives from the fact that all data generally are accumulated prior to solving for $\hat { \mathbf { x } } _ { k }$ ; that is, the data are processed in a single batch.   
5. Note that Eq. (4.4.29) could also be implemented as a sequential processor; that is, after each observation the state estimate and covariance matrix could be mapped to the time of the next observation, where it would become the a priori information. This could then be combined with the observation at that time to yield the estimate for $\hat { \bf x }$ using Eq. (4.4.29).

# 4.5 MAXIMUM LIKELIHOOD AND BAYESIAN ESTIMATION

The method of Maximum Likelihood Estimation for determining the best estimate of a variable is due to Fisher (1912). The Maximum Likelihood Estimate (MLE) of a parameter $\Theta$ —gi ven observations $y _ { 1 } , \ y _ { 2 } , \ \dots { } y _ { k }$ and the joint probability density function

$$
f \left( y _ { 1 } , \ y _ { 2 } , \ldots \ y _ { k } ; \ \Theta \right)
$$

is defined to be that value of $\Theta$ that maximizes the probability density function (Walpole and Myers, 1989). However, if $\Theta$ is a random variable and we have knowledge of its probability density function, the MLE of $\Theta$ is defined to be the

value of $\Theta$ , which maximizes the probability density function of $\Theta$ conditioned on knowledge of the observations $y _ { 1 } , \ y _ { 2 } , \ \dots { } y _ { k }$ :

$$
f ( \Theta / y _ { 1 } , y _ { 2 } , \dots y _ { k } ) .
$$

The Bayes estimate for $\Theta$ is defined to be the mean of the conditional density function given by Eq. (4.5.2) (Walpole and Myers, 1989). The joint density function, Eq. (4.5.1), and the conditional density function, Eq. (4.5.2), are referred to as the likelihood function, $L$ . The logic behind maximizing $L$ is that of all the possible values of $\Theta$ we should choose the one that maximizes the probability of obtaining the observations that actually were observed. If $\Theta$ is a random variable, this corresponds to the mode, or peak, of the conditional density function. In the case of a symmetric, unimodal, density function such as a Gaussian function, this will correspond to the mean of the conditional density function. Hence, the MLE and the Bayes estimate for a Gaussian density function are identical.

Since the logarithm of the density function is a monotonically increasing function of the density function, it is often simpler to determine the value of $\Theta$ that maximizes ln $( L )$ .

For example, assume we are given the following joint probability density function of the independent random variables $y _ { i } , i ~ = ~ 1 , 2 \ldots k$ with common mean, $\alpha$ , and common standard deviation, $\sigma$ , and we wish to determine the MLE of the parameter $\alpha$ :

$$
f ( y _ { 1 } , \mathrm {  ~ \psi ~ } , y _ { 2 } \cdot \cdot \cdot y _ { k } ; \alpha , \sigma ) = f ( y _ { 1 } ; \alpha , \sigma ) f ( y _ { 2 } ; \alpha , \sigma ) \cdot \cdot \cdot f ( y _ { k } ; \alpha , \sigma ) .
$$

We are able to factor the joint density function into the product of the marginal density functions because the random variables $y _ { i }$ are independent. If the joint density function is Gaussian, we may write (see Eq. (A.19.1))

$$
L = f ( y _ { 1 } , y _ { 2 } \cdot \cdot \cdot y _ { k } ; \alpha , \sigma ) = \frac { 1 } { ( 2 \pi ) ^ { k / 2 } \sigma ^ { k } } \exp \left\{ \frac { - 1 } { 2 \sigma ^ { 2 } } \sum _ { i = 1 } ^ { k } ( y _ { i } - \alpha ) ^ { 2 } \right\}
$$

then

$$
\ln { \cal L } = - \frac { k } { 2 } \ln 2 \pi - k \ln \sigma - \frac { 1 } { 2 \sigma ^ { 2 } } \sum _ { i = 1 } ^ { k } ( y _ { i } - \alpha ) ^ { 2 }
$$

and for a maximum

$$
{ \frac { \partial \ln L } { \partial \alpha } } = { \frac { 1 } { \sigma ^ { 2 } } } \sum _ { i = 1 } ^ { k } ( y _ { i } - \alpha ) = 0
$$

and

$$
\frac { \partial ^ { 2 } \ln L } { \partial \alpha ^ { 2 } } = - \frac { k } { \sigma ^ { 2 } } < 0 .
$$

Hence,

$$
\sum _ { i = 1 } ^ { k } ( y _ { i } - { \hat { \alpha } } ) = 0
$$

and the MLE of $\alpha$ is

$$
\hat { \alpha } = \frac { 1 } { k } \sum _ { i = 1 } ^ { k } y _ { i } .
$$

In terms of the orbit determination problem, we are given observations $\mathbf { y } _ { 1 }$ , $\mathbf { y } _ { 2 } \ldots \mathbf { y } _ { k }$ and we wish to determine the MLE of the state, $\hat { \bf x }$ . Hence, we wish to find the value of the state vector, $\mathbf { x } _ { k }$ , which maximizes the conditional density function

$$
f ( \mathbf { x } _ { k } / \mathbf { y } _ { 1 } , \mathbf { y } _ { 2 } \ldots \mathbf { y } _ { k } ) .
$$

We will assume that all density functions for this derivation are Gaussian. Using the first of Eq. (A.21.1) of Appendix A, we may write

$$
f ( \mathbf { x } _ { k } / \mathbf { y } _ { 1 } , \mathbf { y } _ { 2 } \ldots \mathbf { y } _ { k } ) = { \frac { f \left( \mathbf { x } _ { k } , \mathbf { y } _ { 1 } , \mathbf { y } _ { 2 } \ldots \mathbf { y } _ { k } \right) } { f ( \mathbf { y } _ { 1 } , \mathbf { y } _ { 2 } \ldots \mathbf { y } _ { k } ) } } .
$$

Using the second of Eq. (A.21.1) yields

$$
f ( \mathbf { x } _ { k } , \mathbf { y } _ { 1 } , \mathbf { y } _ { 2 } \ldots \mathbf { y } _ { k } ) = f ( \mathbf { y } _ { k } / \mathbf { x } _ { k } , \mathbf { y } _ { 1 } , \ldots { \mathbf { y } } _ { k - 1 } ) f ( \mathbf { x } _ { k } , \mathbf { y } _ { 1 } , \ldots { \mathbf { y } } _ { k - 1 } ) .
$$

Assuming independent observations results in

$$
f ( \mathbf { y } _ { k } / \mathbf { x } _ { k } , \mathbf { y } _ { 1 } , \ldots \mathbf { y } _ { k - 1 } ) = f ( \mathbf { y } _ { k } / \mathbf { x } _ { k } ) ,
$$

and again using the first of Eq. (A.21.1) we have

$$
f ( \mathbf x _ { k } , \mathbf y _ { 1 } , \dots \mathbf y _ { k - 1 } ) = f ( \mathbf x _ { k } / \mathbf y _ { 1 } , \dots \mathbf y _ { k - 1 } ) f ( \mathbf y _ { 1 } , \dots \mathbf y _ { k - 1 } ) .
$$

Hence, Eq. (4.5.11) may be written as

$$
f ( \mathbf { x } _ { k } , \mathbf { y } _ { 1 } , \mathbf { y } _ { 2 } \ldots \mathbf { y } _ { k } ) = f ( \mathbf { y } _ { k } / \mathbf { x } _ { k } ) f ( \mathbf { x } _ { k } / \mathbf { y } _ { 1 } , \ldots \mathbf { y } _ { k - 1 } ) f ( \mathbf { y } _ { 1 } , \ldots \mathbf { y } _ { k - 1 } ) .
$$

Substituting Eq. (4.5.14) into Eq. (4.5.10) yields

$$
f ( \mathbf { x } _ { k } / \mathbf { y } _ { 1 } , \mathbf { y } _ { 2 } \ldots \mathbf { y } _ { k } ) = { \frac { f ( \mathbf { y } _ { k } / \mathbf { x } _ { k } ) f ( \mathbf { x } _ { k } / \mathbf { y } _ { 1 } , \ldots \mathbf { y } _ { k - 1 } ) } { f ( \mathbf { y } _ { k } ) } } ,
$$

where we have used the fact that the observations, $\mathbf { y } _ { i }$ , are independent so we can write

$$
f ( \mathbf { y } _ { 1 } , \mathbf { y } _ { 2 } \ldots \mathbf { y } _ { k } ) = f ( \mathbf { y } _ { 1 } ) f ( \mathbf { y } _ { 2 } ) \ldots f ( \mathbf { y } _ { k } ) .
$$

For our system,

$$
\begin{array} { r l } & { \mathbf { x } _ { k } = \Phi ( t _ { k } , \ t _ { i } ) \mathbf { x } _ { i } } \\ & { \mathbf { y } _ { i } = \widetilde { H } _ { i } \mathbf { x } _ { i } \ + \ \epsilon _ { i } , \quad i = 1 \ldots k } \end{array}
$$

where $\epsilon _ { i } \sim N ( 0 , R _ { i } )$ ; that is, $\epsilon _ { i }$ has a normal distribution with zero mean and covariance $R _ { i }$ . We are assuming independent observations; hence,

$$
E \ \left[ \epsilon _ { j } \epsilon _ { k } ^ { T } \right] = \delta _ { j k } R _ { k } .
$$

We seek the MLE estimate of $\mathbf { x } _ { k }$ , the value of $\mathbf { x } _ { k }$ that maximizes the conditional density function of Eq. (4.5.15). Note that $f ( \mathbf { y } _ { k } )$ , the marginal density function of $\mathbf { y } _ { k }$ , is by definition independent of $\mathbf { x } _ { k }$ . Hence, only the numerator of Eq. (4.5.15) is dependent on $\mathbf { x } _ { k }$ . ${ \bf y } _ { k } / { \bf x } _ { k }$ has mean

$$
\begin{array} { r } { E ( \mathbf { y } _ { k } / \mathbf { x } _ { k } ) = E \left[ ( \widetilde { H } _ { k } \mathbf { x } _ { k } + \epsilon _ { k } ) / \mathbf { x } _ { k } \right] } \\ { = \widetilde { H } _ { k } \mathbf { x } _ { k } } \end{array}
$$

and covariance

$$
\begin{array} { r l } & { \quad E \left[ ( { \bf y } _ { k } - \widetilde { H } _ { k } { \bf x } _ { k } ) ( { \bf y } _ { k } - \widetilde { H } _ { k } { \bf x } _ { k } ) ^ { T } / { \bf x } _ { k } \right] } \\ & { = E \left[ \epsilon _ { k } \epsilon _ { k } ^ { T } \right] = R _ { k } . } \end{array}
$$

Hence,

$$
\mathbf { y } _ { k } / \mathbf { x } _ { k } \sim N ( \widetilde { H } _ { k } \mathbf { x } _ { k } , R _ { k } ) .
$$

Also,

$$
E \left[ { \bf x } _ { k } / { \bf y } _ { 1 } , { \bf y } _ { 2 } \ldots { \bf y } _ { k - 1 } \right] \equiv \overline { { \bf x } } _ { k } .
$$

The associated covariance is

$$
E [ ( { \bf x } _ { k } - \bar { \bf x } _ { k } ) ( { \bf x } _ { k } - \bar { \bf x } _ { k } ) ^ { T } ] \equiv \overline { { P } } _ { k } .
$$

Hence,

$$
\mathbf { x } _ { k } / \mathbf { y } _ { 1 } , . . . \mathbf { y } _ { k - 1 } \sim N ( \overline { { \mathbf { x } } } _ { k } , \overline { { P } } _ { k } ) .
$$

The likelihood function defined by Eq. (4.5.15) is given by

$$
\begin{array} { l } { { \displaystyle { \cal L } = f ( { \bf x } _ { k } / { \bf y } _ { 1 } , { \bf y } _ { 2 } \ldots { \bf y } _ { k } ) = \frac { 1 } { ( 2 \pi ) ^ { p / 2 } | R _ { k } | ^ { 1 / 2 } } } \ ~ } \\ { { \displaystyle ~ \times \exp - 1 / 2 \left\{ ( { \bf y } _ { k } - \widetilde { \cal H } _ { k } { \bf x } _ { k } ) ^ { T } R _ { k } ^ { - 1 } ( { \bf y } _ { k } - \widetilde { \cal H } _ { k } { \bf x } _ { k } ) \right\} } \ ~ } \\ { { \displaystyle ~ \times \ \frac { 1 } { ( 2 \pi ) ^ { n / 2 } | \overline { { { \cal P } } } _ { k } | ^ { 1 / 2 } } \exp - 1 / 2 \left\{ ( { \bf x } _ { k } - \bar { \bf x } _ { k } ) ^ { T } \overline { { { \cal P } } } _ { k } ^ { - 1 } ( { \bf x } _ { k } - \bar { \bf x } _ { k } ) \right\} \frac { 1 } { f ( { \bf y } _ { k } ) } . } } \end{array}
$$

Because this is a Gaussian density function, the mean, median (having equal probability weight on either side), and mode will be identical. Hence, any criterion that chooses one of these values for $\hat { \mathbf { x } } _ { k }$ will yield the same estimator.

Accumulating the logarithms of all terms in $f ( \mathbf { x } _ { k } / \mathbf { y } _ { 1 }$ , $\mathbf { y } _ { 2 } \ldots \mathbf { y } _ { k } )$ that are a function of $\mathbf { x } _ { k }$ and calling this function $\ln { \cal L ^ { \prime } }$ yields

$$
\begin{array} { r l } & { \ln { \cal L } ^ { \prime } = - 1 / 2 [ ( { \bf y } _ { k } - \widetilde { H } _ { k } { \bf x } _ { k } ) ^ { T } R _ { k } ^ { - 1 } ( { \bf y } _ { k } - \widetilde { H } _ { k } { \bf x } _ { k } ) } \\ & { ~ + ( { \bf x } _ { k } - \overline { { \bf x } } _ { k } ) ^ { T } \overline { { P } } _ { k } ^ { - 1 } ( { \bf x } _ { k } - \overline { { \bf x } } _ { k } ) ] . } \end{array}
$$

Differentiating ln $L ^ { \prime }$ with respect to $\mathbf { x } _ { k }$ ,

$$
\frac { \partial \ln { \cal L } ^ { \prime } } { \partial { \bf x } _ { k } } = - \left[ - ( { \widetilde { \cal H } } _ { k } ^ { T } R _ { k } ^ { - 1 } ) ( { \bf y } _ { k } - { \widetilde { \cal H } } _ { k } { \bf x } _ { k } ) + { \overline { { { \cal P } } } } _ { k } ^ { - 1 } ( { \bf x } _ { k } - { \overline { { { \bf x } } } } _ { k } ) \right] = 0 .
$$

The value of $\mathbf { x } _ { k }$ that satisfies Eq. (4.5.28) is $\hat { \mathbf { x } } _ { k }$

$$
\left( \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } + \overline { { P } } _ { k } ^ { - 1 } \right) \hat { \mathbf { x } } _ { k } = H _ { k } ^ { T } R _ { k } ^ { - 1 } \mathbf { y } _ { k } + \overline { { P } } ^ { - 1 } \overline { { \mathbf { x } } } _ { k }
$$

$$
\hat { \mathbf { x } } _ { k } = \left( \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } + \overline { { P } } _ { k } ^ { - 1 } \right) ^ { - 1 } \left( \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \mathbf { y } _ { k } + \overline { { P } } _ { k } ^ { - 1 } \overline { { \mathbf { x } } } _ { k } \right)
$$

which is identical to the minimum variance estimate of $\hat { \mathbf { x } } _ { k }$ as well as the weighted least squares estimate if $W _ { k } = { \boldsymbol { R } } _ { k } ^ { - 1 }$ .

Furthermore, from Eq. (4.5.28),

$$
\frac { \partial ^ { 2 } \ln L ^ { \prime } } { \partial { \bf x } ^ { 2 } } = - \left[ \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } + \overline { { { P } } } _ { k } ^ { - 1 } \right] .
$$

Because − ∂2 ln L is positive definite, we have maximized the likelihood function (see Appendix B).

# 4.6 COMPUTATIONAL ALGORITHM FOR THE BATCH PROCESSOR

Assume that we wish to estimate the state deviation vector $\mathbf { x } _ { \mathrm { 0 } }$ at a reference time, $t _ { 0 }$ . Given a set of initial conditions $\mathbf { X } ^ { * } ( t _ { 0 } )$ , an $a$ priori estimate $\overline { { \mathbf { x } } } _ { \mathrm { 0 } }$ and the associated error covariance matrix, ${ \overline { { P } } } _ { 0 }$ , the computational algorithm for the batch processor generally uses the normal equation form for $\hat { \mathbf { x } } _ { 0 }$ . Writing Eqs. (4.3.25) and (4.4.29) in normal equation form for a batch of observations and recognizing in Eq. (4.3.25) that $W = R ^ { - 1 }$ and $\overline { { W } } = \overline { { P } } _ { 0 } ^ { - 1 }$ yields

$$
( H ^ { T } R ^ { - 1 } H + \overline { { P } } _ { 0 } ^ { - 1 } ) \hat { \mathbf { x } } _ { 0 } = H ^ { T } R ^ { - 1 } \mathbf { y } + \overline { { P } } _ { 0 } ^ { - 1 } \overline { { \mathbf { x } } } _ { 0 } .
$$