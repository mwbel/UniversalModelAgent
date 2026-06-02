as well as a host of recreational uses. Land surveying applications and optimization of agricultural operations are further examples of specific applications of improved positioning made possible through precise timing, and some intelligent transportation systems require navigation accuracies of a few centimeters. See Section 20.3.

Navigation with systems other than GNSS that depend on the timing of electronic signals also requires a level of precision in timing synchronization that is compatible with the system’s expected positional accuracy. As an example, LORAN (LOng Range Aid to Navigation) is a hyperbolic navigation system that provides multiple synchronized low-frequency transmitters so that the user equipment can determine the difference in the time of arrival from pairs of transmitters to determine a position. e-LORAN (enhanced LORAN) can be expected to need timing at the level of $\pm 5$ to a few tens of nanoseconds to meet their navigational objectives. The status of e-LORAN, as a backup to GPS, is under consideration in a number of countries.

# 20.3 Time Domain Astronomy (TDA)

Time Domain Astronomy is the study of astronomical objects and phenomena that change with time, such as asteroids, comets, variable stars, quasi-stellar objects, eclipses, planetary transits, gravitational lensing, and such. Advances in observing, data storage, and processing technologies have made possible astronomical surveys of sky regions, e.g., MACHO (Alcock et al., 2000), EROS (Rahal et al., 2009), OGLE (Udalski, Kubiak, & Szymanski, 1997), Pan-STARRS (Kaiser et al., 2002), and CRTS (Larson et al., 2003). New telescopes are being planned with the Large Synoptic Survey Telescope (LSST) (Ivezic et al., 2011) expected to generate a 150 Petabyte $( 1 5 0 \times 2 ^ { 5 0 }$ bytes) database, and a 40 Petabyte catalog of 50 billion astronomical objects during 10 years. LSST could issue 2 million alerts of transient events nightly. These events are supernovae, planetary occultations, near-Earth objects, gamma-ray bursts, stellar flares, comets, gravitational microlensing events, and supermassive black holes flares, for example (Tyson & Borne, 2012).

This flow of data will require real-time mining of approximately 2 terabytes per hour, real-time classification of 50 billion objects, and analysis, evaluation, and knowledge extraction of 2 million events per night (Borne, 2013). This will require accurate timing of events and processing the observations with appropriate timescales.

# 20.4 Intelligent Transportation Systems

Intelligent transportation systems include self-driving cars, connected vehicles, driving assistance and warning systems, car navigation, emergency vehicle notification systems, automatic road enforcement, variable speed limits, collision avoidance systems, dynamic traffic light sequence, traffic signal control systems, container management systems, variable message signs, automatic number plate recognition, speed cameras, parking guidance and information systems, weather information, bridge de-icing systems, and others. These systems require time, frequency, and navigation resources. It is likely that such systems will impose requirements for navigational errors less than a few centimeters, implying timing precision needs better than a 10th of a nanosecond. History of intelligent transportation systems is given at www.its.dot.gov/index.htm. For example, self-driving cars are being developed by Waymo (Google), Apple, Tesla, Volvo, Ford, General Motors, Fiat, Toyota, and others.

# 20.5 Communications

Precise timing is perhaps most critical in communications applications. Common clocks are used, for example, in switching voice and data traffic through the telephone networks. Precise timing is also needed to time stamp information packets and to allow several transmitters to send information simultaneously over a single communication channel. This process, called “multiplexing,” can be accomplished by means of various techniques. All of them require some form of precise timing or frequency. In this application, it is often the case that, while precision may be critical, accuracy may not be required. This is because a communications network may be operated with internal standards for time and frequency, and accuracy is only needed if different networks are required to interoperate with others. At that point, they may require an external standard for time and frequency.

Time-division-multiplexing (TDM) is a process in which multiple bit streams of information are sent as sub-channels on one communication channel at what appears to be at the same time. In reality, the streams are taking turns in time. Fixed time intervals are created so that, for example, a block of data from sub-channel 1 is sent during time interval 1, a block from subchannel 2 is sent during time interval 2, etc. The process continues until a frame, which consists of one time interval for each sub-channel, is completed. At that point, a new cycle begins with the next block of information from each sub-channel being transmitted. TDM, in the case where several stations are connected to the same physical medium such as the same frequency channel, is called time division multiple access (TDMA). This process is often used in cellular phone networks, for example. Clearly the time slots must be synchronized at each end of the transmit–receive network to enable the process to work.

Frequency division multiple access (FDMA) divides the radio spectrum into a series of individual frequency bands allowing each user access to an allocated frequency band without interfering with other users. Code division multiple access (CDMA) uses spread-spectrum technology and a coding scheme to allow a number of users to share a frequency band. Spectrum management is critical and that capability depends on accurate frequency standards being available along the communications networks. Each transmitter has an assigned code that is known to the user. The spread-spectrum technique spreads the signal in a particular bandwidth over a frequency domain. To reconstruct the signal at the receiver, the transmitter and receiver must use the same coding scheme to spread the signal over the frequency domain.

The American National Standards Institute (ANSI) describes telecommunications timing requirements by means of four “stratum” levels. According to the ANSI standard “Synchronization Interface Standards for Digital Networks” (ANSI/T1.101–1987), a Stratum 1 timing source is an autonomous source of timing requiring no other input than possibly a yearly calibration. It must perform with a maximum drift rate, defined in terms of fractional frequency $\Delta \mathrm { f } / \mathrm { f } ,$ better than $\pm 1 \times { 1 0 } ^ { - 1 1 }$ over a year. A properly calibrated Stratum 1 source, then, is capable of providing bit-stream timing that will not slip relative to a perfect standard more than once every four to five months. When a frame slip does occur in network voice equipment, it generally reacquires frame synchronization quickly, resulting in an audible pop or click, but data circuits lose a number of bits depending on the data rate being transmitted, and on whether or not an error correction protocol is being used. A typical Stratum 1 timing source is often an atomic standard (caesium beam or hydrogen maser) or an oven-controlled quartz crystal oscillator, even though atomic standards are capable of better accuracy than these specifications. A properly calibrated clock system controlled by means of a GPS timing signal may also be considered for use as a Stratum 1 timing source. In telecommunications networks, Stratum 1 sources are considered the primary sources of time and frequency for networks.

Stratum 2 sources must be capable of being adjusted to match the frequency of the Stratum 1 source within a range of $^ { \pm 1 . 6 \times 1 0 ^ { - 8 } }$ in one year and drift no more than $\pm 1 \times { 1 0 } ^ { - 1 0 }$ in a day. This will provide a frame slip rate of about one slip in seven days when the Stratum 2 source is not being updated by a Stratum 1 source. Typical Stratum 2 sources are rubidium standards and oven-controlled quartz oscillators. Table 20.1 compares all of the stratum level definitions.

Stratum 3E was developed after Stratum 3 was standardized in order to meet SONET (synchronous optical networking) equipment requirements. SONET is a protocol that is used to transfer multiple digital bit streams over an optical fiber using lasers or light-emitting diodes (LEDs). Stratum 4 sources are designed to track Stratum 2 or 3 sources and have no holdover capability. They are not recommended as a timing source for any other system outside the network.

Table 20.1 Standards for stratum levels   

<table><tr><td>Stratum</td><td></td><td></td><td>Adjustment Accuracy Maximum Drift Rate Time between Frame Slips</td></tr><tr><td>1</td><td>1 ×10-11</td><td></td><td>72 days</td></tr><tr><td>2</td><td>1.6 ×10-8</td><td>1 × 10-10/day</td><td>7 days</td></tr><tr><td>3E</td><td>4.6 ×10-6</td><td>1 × 10-8/day</td><td>3.5 hours</td></tr><tr><td>3</td><td>4.6 × 10-6</td><td>3.7 × 10-7/day</td><td>6 minutes</td></tr><tr><td>4</td><td>32 ×10-6</td><td>32 × 10-%/day</td><td></td></tr></table>

In Network Time Protocol (NTP) applications, the term “stratum level” is used differently. For these purposes, stratum level refers to the distance of a network server from a reference clock. Thus, a Stratum 0 source is assumed to be an accurate source of time and frequency with minimal delays that cannot be used on the network. They can be connected to computers and these act as Stratum 1 servers. A Stratum 1 time server must be directly linked to a reliable source of UTC time, not over a network path, and acts as a primary network time standard. A Stratum 2 server gets its time over a network link, using NTP, from a Stratum 1 server, and a Stratum 3 server gets its time over a network link, using NTP, from a Stratum 2 server, etc.

# 20.6 Power Grid

Precise timing becomes a concern for the distribution of electrical power in more than one specific application. The efficiency of transmitting power throughout grids depends on precise matching of the phases of the alternating electrical current. This requires an accurate frequency reference across the network of power grids. Typically, this phase information is obtained by individual power companies by maintaining local sources of time that are referred to a standard timing signal. GPS supplies a cheap, easy-to-use timing signal that provides time with an accuracy orders of magnitude better than that necessary for phase matching. For example, a $\pm$ one-degree phase difference in a $6 0 ~ \mathrm { H z }$ oscillation corresponds to a $\pm 4 6 ~ \mu \mathrm { s }$ time difference, so maintaining phase matching at the level of $\pm 0 . 1 ^ { \circ }$ would require timing at the level of $\pm 5 ~ { \mu \mathrm { s } }$ . In general, adequate capability can be maintained using rubidium standards and quartz oscillators that are steered to a GNSS timing signal. Temporary loss of that signal could be mitigated by the holdover capacity of the time and frequency standards and their backups.

A second application of precise timing in electrical power applications is in locating faults or breaks in the grid. $\mathrm { A \pm 1 ~ \mu s }$ timing capability is adequate to meet these applications. Other applications of timing information deal with billing and secondary aspects of power distribution. These requirements lie in the range of $\pm 0 . 1$ s to $\pm 1 ~ \mathrm { m s }$ .

# 20.7 Banking and Finance

Timing information with relatively low accuracy is used by banking and finance institutions to time stamp financial transactions. Generally, an accuracy of only three seconds is needed for time stamping transactions. For this purpose, a timing system with accuracy of $\pm 0 . 1$ s is more than adequate and easily achievable by a number of means. Typically timing networks are used that involve rubidium or quartz clocks that are steered using NTP or GPS. These clocks would be capable of relatively long periods without being steered in the event of the loss of an outside source of timing information.

# 20.8 Emergency Services

Timing requirements for time stamping standard emergency service operations is about the same as that for the banking and finance sector. Emergency service centers generally rely on radio services and NTP as sources for accurate time, with backup systems of rubidium or quartz clocks. Enhanced emergency services locate callers through the GNSS services. This capability delivers fast responses and good geolocation of required services. It is an application of existing GNSS positioning, and, as such, the timing requirements are equivalent to those discussed in Section 20.2.

# 20.9 Water Flow

Precise timing information is even used for time stamping by water utilities to control flow in and out of local systems through remotely controlled valves and to control the chemical treatment of water and sewage. As with banking and finance applications, the accuracy required is relatively low and easily achievable using widely available sources of time and low precision clocks.

# 20.10 Scientific

There are a wide range of scientific applications of time and frequency in many fields. In astronomy, time is critical for observations and theories of the motion of objects. Pulsar observations and analysis requires precise time and ephemerides. Determination of Earth rotation, kinematics, and geodesy depends on precisely timed observations. Planetary sciences and ephemerides computations require the family of relativistic dynamical timescales. Measurements in physics depend on accurate time and the relativistic relations between timescales. Precise frequencies are required for many scientific purposes.

# 20.11 Religions

The religious uses of time do not require great accuracy and are basically tied to the motion of the Sun and Moon. Jewish Sabbath and holidays begin at sunset, which is location dependent and the times are affected by the weather and terrain. Islamic prayer times are determined by the altitude of the Sun and the lunar months are determined by the observations of the crescent Moon after new moon, which can be predicted computationally. Both are location dependent.

# 20.12 General Public

The general public obtains time from many sources and at various accuracies. Many people get the time from their smartphones or from their computers. Radio signals can automatically maintain the time on clocks and wristwatches. Communication systems, such as radio and television, provide the time.

# 20.13 Summary

Table 20.2 provides an outline of the applications of precise time and frequency along with representative one-sigma accuracy and precision needs. Some need only precision, but others require accuracy or the ability to be traceable to a conventional standard. The table shows that many users of precise time and frequency information do not require the ultimate in either quantity, and that there is a very large range in the needs of users. Consequently, the relative cost of the apparatus is likely to drive the choices of equipment used in the various applications.

Table 20.2 Representative estimates of time and frequency needs   
anageme   

<table><tr><td rowspan="2">Community</td><td rowspan="2">Application Purpose</td><td rowspan="2"></td><td colspan="2">Accuracy</td><td colspan="2">Precision</td></tr><tr><td>Time</td><td>Frequency</td><td>Time</td><td>Frequency</td></tr><tr><td rowspan="7">Positioning and Navigation</td><td>Aviation</td><td>Fuel management, traffic spacing, course navigation</td><td>±3 ns</td><td>±3.5 × 10-14</td><td></td><td></td></tr><tr><td>Space</td><td>Artificial satellite location, surveillance</td><td>±25 ns</td><td>±3.0 × 10-13</td><td></td><td></td></tr><tr><td>Maritime</td><td>Fuel management, routing, cargo location</td><td>±25 ns</td><td>±3.0 ×10-13</td><td></td><td></td></tr><tr><td>Transportation</td><td>Fuel management, real-time routing, cargo location, intelligent</td><td>±1 ns</td><td>±1.0 × 10-14</td><td></td><td></td></tr><tr><td>Agriculture</td><td>transportation system Field management, fertilizer optimization, livestock tracking</td><td>±10 ns</td><td>±1.0 × 10-13</td><td></td><td></td></tr><tr><td>Railroad</td><td>Asset location, real-time routing</td><td>±10 ns</td><td>±1.0 × 10-13</td><td></td><td></td></tr><tr><td>Automotive</td><td>Intelligent highway system</td><td>±1 ns</td><td>±1.0 × 10-14</td><td></td><td></td></tr><tr><td></td><td>Recreation</td><td>Small boat navigation,hiking, bicycle ±25 ns touring</td><td></td><td>±3.0 ×10-13</td><td></td><td></td></tr><tr><td rowspan="2">Communications</td><td>Voice</td><td>Cellular phones</td><td></td><td></td><td>±1.0 ns</td><td>±1.0 × 10-14</td></tr><tr><td>Data</td><td>Data transmission, secure communications</td><td></td><td></td><td>±1.0 ns</td><td>±1 ×10-11</td></tr><tr><td rowspan="2">Survey and Mapping</td><td>Geographic information systems</td><td>Asset location</td><td>±10 ns</td><td>±1.0 ×10-13</td><td></td><td></td></tr><tr><td>Datum</td><td>Land management</td><td>±25 ns</td><td>±3.0 ×10-13</td><td></td><td></td></tr></table>

Table 20.2 (cont.)   

<table><tr><td></td><td></td><td></td><td colspan="2"> Accuracy</td><td colspan="2">Precision</td></tr><tr><td>Community</td><td>Application</td><td>Purpose</td><td>Time</td><td>Frequency</td><td>Time</td><td>Frequency</td></tr><tr><td>Energy</td><td>Power grid</td><td>Phase matching</td><td>±50 μs</td><td>±6.0×10-10</td><td></td><td></td></tr><tr><td></td><td>Oil and gas location</td><td>Exploration</td><td>±25 ns</td><td>±3.0 × 10-13</td><td></td><td></td></tr><tr><td></td><td>Power line management</td><td>Fault location</td><td></td><td></td><td>±10 ns</td><td>±1.0 × 10-13</td></tr><tr><td>Banking and Finance</td><td> Asset management Time stamping</td><td></td><td>±0.1 s</td><td>±1.0 × 10-6</td><td></td><td></td></tr><tr><td>Emergency Services</td><td>Fire, police, medical services</td><td> Search and rescue, vehicle location</td><td>±10 ns</td><td>±1.0 ×10-13</td><td></td><td></td></tr><tr><td>Water</td><td>System operation</td><td>Flow management</td><td></td><td></td><td>±0.1 s</td><td>±1.0 ×10-6</td></tr><tr><td>Environmental</td><td>Resource management</td><td>Hazardous waste containment</td><td>±25 ns</td><td>±3.0 ×10-13</td><td></td><td></td></tr><tr><td>Scientific</td><td>Geodesy</td><td>Plate tectonics, ocean level</td><td>±1.0 ns</td><td>±1.0 × 10-14</td><td></td><td></td></tr><tr><td></td><td>Astronomy</td><td>Pulsar investigations</td><td>±1.0 ns</td><td>±1.0 ×10-14</td><td></td><td></td></tr><tr><td></td><td>Physics</td><td>Measurement precision</td><td>±0.01 ns</td><td>±1.0 ×10-16</td><td></td><td></td></tr></table>

# References

Alcock, C., Allsman, R. A., Alves, D. R., Axelrod, T. S., Becker, A. C., Bennett, D. P., Cook, K. H., Dalal, N., Drake, A. J., Freeman, K. C., Geha, M., Griest, K., Lehner, M. J., Marshall, S. L., Minniti, D., Nelson, C. A., Peterson, B. A., Popowski, P., Pratt, M. R., Quinn, P. J., Stubbs, C. W., Sutherland, W., Tomaney, A. B., Vandehei, T., & Welch, D. (2000). The MACHO Project: Microlensing Results from 5.7 Years of LMC Observations. Astrophys. Journal, 542, 281–307.   
Borne, K. (2013). Virtual Observatories, Data Mining and Astroinformatics. In T. Oswalt & H. Bond, eds., Planets, Stars and Stellar Systems. Astronomical Techniques, Software, and Data, vol. 2. Hoboken, NJ: Wiley, pp. 404–443.   
Ivezic, Z. et al. (2011). LSST: From Science Drivers to Reference Design and Anticipated Data Products, ArXiv e-prints, 0805.2366, www.lsst.org/lsst/overview/.   
Kaiser, N., Aussel, H., Burke, B. E., Boesgaard, H., Chambers, K., Chun, M. R., Heasley, J. N., Hodapp, K.-W., Hunt, B., Jedicke, R., Jewitt, D., Kudritzki, R., Luppino, G. A., Maberry, M., Magnier, E., Monet, D. G., Onaka, P. M., Pickles, A. J., Rhoads, P. H. H., Simon, T., Szalay, A., Szapudi, I., Tholen, D. J., Tonry, J. L., Waterson, M., & Wick, J. (2002). Pan-STARRS: A Large Synoptic Survey Telescope Array. Society of Photo-Optical Instrumentation Engineers (SPIE) Conference Series, 4836, 154–164.   
Larson, S., et al. (2003). The CSS and SSS NEO Surveys. AAS/Division for Planetary Sciences Meeting Abstracts #35, Bulletin of the AAS, 982.   
LSST Science Collaborations and LSST Project 2009 (2013). LSST Science Book, Version 2.0, arXiv:0912.0201, www.lst.org/lsst/scibook.   
Rahal, Y. R., Afonso, C., Albert, J.-N., Andersen, J., Ansari, R., et al. (2009). The EROS-2 Search for Microlensing Events towards the Spiral Arms: The Complete Seven Season Results. Astron. Astrophys., 500, 1027–1044.   
“Synchronization Interface Standards for Digital Networks” (ANSI/T1.101–1987), American National Standards Institute, New York.   
Tyson, J. & Borne, K. (2012). Future Sky Surveys, New Discovery Frontiers. In M. Way, J. D. Scargle, K. Ali, & A. Srivastava, eds., Advances in Machine Learning and Data Mining for Astronomy. Boca Raton, FL: CRC Press, pp. 161–181.   
Udalski, A., Kubiak, M., & Szymanski, M. (1997). Optical Gravitational Lensing Experiment. OGLE-II: The Second Phase of the OGLE Project. Acta Astronomica, 47, 319–344.   
York, D. G., et al. (2000). The Sloan Digital Sky Survey: Technical Summary. Astron. J., 120, 1579.

# 21

# Future of Timekeeping

# 21.1 Future Needs for Time

The demand for improvements in the precision and accuracy of time and frequency will drive the developments in the field for years to come. The applications on the horizon that would make use of this improved capability are as varied as the current applications.

Efficient means to improve the transportation methods of the future are just one of those applications. More accurate positioning of aircraft made possible through improved synchronization of future timing standards will enable more efficient use of air space. This might mean that, not only could aircraft be spaced more efficiently, but air traffic could make use of more direct flight paths, rather than being constrained. Methods of managing ground transportation are being developed. Self-driving cars and vehicle-to-vehicle communication systems are being developed and tested. This could mean that at some future time drivers could take advantage of a managed network of roads controlled through precise navigation of vehicles. The efficiency of such a system will depend on precise positioning, again made possible by synchronized timing signals.

Currently, the inability to navigate indoors, or in areas where Global Navigation Satellite System (GNSS) signals are too weak to be effective, limits the effectiveness of responses to emergency situations. It is likely that building planners of the future will consider indoor navigation capabilities, enabled by precise time signals within buildings. GNSS signals currently aid in locating emergency situations using existing GNSS timing signals. These types of services are likely to be improved in the future as timing capabilities improve.

The management of resources currently takes advantage of accurate location of inventory items. Identification of items and their whereabouts is an important tool available to managers. The usefulness of such identification and location systems depends directly on the resolution precision of those systems. This capability depends on precise positioning made possible by timing capabilities and can be expected to be expanded and improved by increased accuracies and signal availability.

The communications facilities of the future may be direct beneficiaries of improved time and frequency. Currently systems are operating at the edge of our capability to provide sufficient bandwidth. More precise spectrum allocation, made possible by improved frequency standards, will enable a greater throughput of data in the future.

The scientific community will also benefit significantly with enhanced time and frequency capability. Measurements depending on accurate time or precise frequency resolution will be instrumental in future developments. This should benefit the fields of geodesy, physics, astronomy, space sciences, Earth dynamics, and optical measurements, to mention just a few fields affected by the accuracies of time and frequency.

# 21.2 Modeling the Earth’s Rotation

Future improvements in Earth rotation modeling are likely to depend on both improved observations and improvements in understanding the physics of the Earth. In the area of astronomical observations of the Earth’s orientation, we can expect observations to be made more accurately and with higher time resolution, so that observations of the Earth’s rotation vector in space and in the terrestrial frame could be available routinely with sub-daily frequency. We can also expect that observations of the phenomena known to affect the rotation vector will also be made available with higher resolution in both time and space. For example, observations of winds and ocean currents are likely to be available from observing platforms in space and from a dense grid of terrestrial observing locations. This information will conceivably lead to estimates of atmospheric and ocean angular momentum with hourly frequency.

Improved modeling of lower frequency variations in the Earth’s rotation will depend on improved understanding of the physical processes of the Earth’s interior. Advances in the measurement of the gravity and magnetic fields could be helpful in this endeavor. The understanding of the variations in these fields, both in time and in space, is likely to improve knowledge of the response of the Earth’s rotation vector to the physical phenomena occurring within the Earth. This knowledge may lead to understanding of the drivers of polar motion and the forces changing the Earth rotation.

Using these observations, together with improved capacity to analyze the data quickly, we might expect true real-time estimates of the Earth’s rotation angle in space as well as nearly real-time values of the variations in the Earth’s rotational speed. We may even get to the point that we could predict more reliably the Earth’s rotation for months in advance, but that capability will continue to be a challenge for the future.

# 21.3 Clocks of the Future

Future clocks will be available to cover a wide range of users’ needs. Chip-scale atomic clocks are becoming readily available now, and we can imagine a future when individuals interested in extremely precise time could be wearing watches that offer time based on atomic energy-level transitions. Assuming that such devices can be made sufficiently robust, these clocks are likely to be adapted to a number of applications depending on user requirements.

Optical clock technology is being developed and provides highly precise laboratory standards. Developments of spectroscopic techniques are making available extremely high-Q transitions for laboratory standards. Fountains using alkali atoms may gradually replace the caesium beam oscillators of today.

The necessity for development of improved devices will come from the need for improvements in positioning and navigation, as well as the growing requirements for the transfer of information. Expectations for improved communications capabilities continue to grow. These expected improvements include higher data rates and more efficient use of the radiofrequency spectrum in order to provide greater information throughput. All of these applications are likely to take advantage of improvements in frequency standards.

The use of pulsars to provide long-term frequency stability to current timescales has led to an ensemble pulsar-based timescale that can be expected to improve in accuracy. The investigation of the physics of pulsars will lead to a better understanding of their rotational speeds and improved accuracies. The pulsar-based timescale will be an independent source of time, not subject to solar system gravitational effects and, thus, able to identify possible systematic variations in TAI.

Limited data are available for forming a timescale based on white dwarf rotations, but it may be possible to identify additional white dwarfs with accurate rotational rates that could form an ensemble white dwarf timescale (Kepler et al., 2000; Kepler, 2012).

# 21.4 Future Timescales

Timescales can be expected to keep pace with the development of the future time and frequency standards. This will not happen without development of statistical models to evaluate the performance of contributing clocks and the development of robust algorithms to combine the best features of the contributors to the timescale. The accuracy of clock comparisons will need to be developed to make this process viable, and for this purpose, improved calibration techniques will need to be developed.

The future of leap seconds, as a means to reconcile the use of atomic time with observations of the Earth’s rotation, will not be resolved at least until 2023. The GNSS currently makes available a timescale free of unpredictable onesecond adjustments. The future will decide if a leap-second-less timescale will be in the realm of the everyday user, or if the users of time and frequency will prefer two timescales: one for “everyday” use related to the Earth’s rotation and another for use in precise time applications without leap seconds. By 2023, a more precise timescale, a redefinition of the second, and applications requiring more precision and accuracy may lead to a redefinition of timescales. In any event we can expect that the future timescales will continue to be based on atomic energy-level transitions.

A need for more accurate and rapid information that is readily available concerning the Earth’s rotation, as given now by UT1, can be expected. Improved observations and distribution methods can be expected to make more accurate Earth rotation data available.

The SI second of today’s timescales is defined by the hyperfine transition of the caesium atom. As new time and frequency standards are being developed that take advantage of higher-Q spectral lines, the redefinition of the second, its basis, and when it is introduced, will be considered. We would expect that the second will be redefined in some way so as to be compatible with the past and with the precision needed for future applications. Many scientific and technological standards today (e.g., the meter) are based on the current definition of the second, so it is difficult to imagine a revised definition of the second that would not be compatible with the past (Arias, 2009, 2017). In the future, we might expect observed timescales, such as TAI, pulsar, and maybe white dwarf-based timescales. We expect operationally standard timescales, such as the atomic timescale, UTC, or a more accurate version thereof, and the Earth rotation scale, UT1. We can also expect that the timescales implicit in the global navigation satellite systems of the future will play a large role in everyday usage. We hope that these scales might be part of the international standards.

The need for accurate, realizable timescales for use in space can be expected. We have defined such timescales, e.g., TT, TCB, TCG, and TDB, for use in dynamical applications in the solar system. With the expected improvements in accuracies, the family of dynamical timescales will need to have better definitions based on higher orders of relativity and the post-post-Newtonian parameters. While these scales are necessary for the development of ephemerides and reduction of planetary and lunar observations, observations made during space missions are made using UTC. We anticipate the need for relativistically correct timescales, easily comparable to clocks on the Earth, for future planetary expeditions. The timing accuracy required for navigation and communications for missions at Mars indicates the need for an accurate relation between UTC and a Martian proper time. Missions to other planets will require accurate models of transformations among the proper times for those planets.

# 21.5 Future Time Distribution

With all of the developments likely to occur as outlined earlier, questions remain about how we might expect to get time to the user of the future. There is no reason to expect that the future satellite navigation systems will not continue to provide precise time to the vast majority of precise time users. We might also expect that time provided by those systems will be limited only by the ability to calibrate the user’s receiver. Those needing time and frequency with qualities similar to those provided by laboratory standards are likely to make use of optical fibers. This technology is currently being used, but requires dedicated fibers for precise time transfer. It is likely to be extended in the future, and we might imagine a future when the use of optical fiber for time and frequency applications is ubiquitous (Kodet et al., 2016).

An intriguing possibility that has been discussed is that of quantum entanglement. This is a theoretical phenomenon in which objects that are separated in space have quantum states that are linked in such a manner that, when one changes state, the other must also change. Should this be true, it would have obvious implications for instantaneous time synchronization. However, many have argued that information cannot be transferred faster than the speed of light, so that this technique would not be a viable means to transfer time (Coecke, 2003).

Another possibility more likely for development in the future is that of a distributed clock, in which the clock that is to be used as the conventional standard will actually be made up of a large number of interrelated clocks both on the Earth’s surface and in space. The relationship between these clocks might be known through optical fiber connections or laser ranging connections. If the potential bias and rate of any clock in this distributed system is known nearly instantaneously, then that clock provides a nearly instantaneous traceability to the conventional standard. Such a system will depend critically on our future ability to calibrate the time comparison network of the future (Tanenbaum & van Steen, 2007).

# References

Arias, E. F. (2009). Current and Future Realizations of Coordinate Time Scales. In A. Klioner, P. K. Seidelmann, & M. H. Soffel, eds., Relativity in Fundamental Astronomy. Proceedings of IAU Symposium 261. Paris: International Astronomical Union.   
Arias, E. F. (2017). New Technologies and the Future of Time Keeping. In E. F. Arias, L. Combrink, P. Gabor, C. Hohenkerk, & P. K. Seidelmann, eds., Science of Time 2016. Springer.   
Coecke, B. (2003). The Logic of Entanglement. Research Report PRG-RR-03–12, 2003. arXiv:quant-ph/0402014.   
Kepler, S. O. (2012). White Dwarf Stars: Pulsations and Magnetism. In H. Shibahashi, M. Takata, & A. E. Lynas-Gray, eds., 61st Fujihara Seminar: Progress in Solar/Stellar Physics with Helio- and Asteroseismology. ASP Conference Series, 462. San Francisco, CA: Astronomical Society of the Pacific, pp. 322–325.   
Kepler, S. O., Mukadam, A., Winget, D. E., & Bradley, P. A. (2000). Evolutionary Timescale of the Pulsating White Dwarf G117-b15a: The Most Stable Optical Clock Known. Astron. J., 534, L185–L188.   
Kodet, J., Pánek, P., & Procházka, I. (2016). Accuracy of Two-Way Time Transfer via a Single Coaxial Cable. Metrologia, 50, 18–26.   
Tanenbaum, A. S. & van Steen, M. (2007). Distributed Systems: Principles and Paradigms. Upper Saddle River, NJ: Prentice-Hall.

<table><tr><td>2MASS</td><td>2 Micron Astronomical Sky Survey</td></tr><tr><td>α</td><td>right ascension</td></tr><tr><td>A1</td><td>USNO atomic timescale</td></tr><tr><td>A3</td><td>BIH atomic timescale</td></tr><tr><td>AAM</td><td>atmospheric angular momentum</td></tr><tr><td>ACES</td><td>Atomic Clock Ensemble in Space</td></tr><tr><td>AD</td><td>Anno Domini(Common Era)</td></tr><tr><td>AGU</td><td>American Geophysical Union</td></tr><tr><td>AM</td><td>formerBIH timescale</td></tr><tr><td>ANSI</td><td>American National Standards Institute</td></tr><tr><td>au</td><td>astronomical unit</td></tr><tr><td>BC</td><td>Before Christ (Before Common Era)</td></tr><tr><td>BCE</td><td>Before Common Era</td></tr><tr><td>BCRS</td><td>Barycentric Celestial Reference System</td></tr><tr><td>BDS</td><td>BeiDou Navigation Satellite System</td></tr><tr><td>BGI</td><td>Bureau Gravimétrique International</td></tr><tr><td>BIH</td><td>Bureau Internationale de l&#x27;Heure</td></tr><tr><td>BIPM</td><td>Bureau International des Poids et Mesures</td></tr><tr><td>C</td><td>speed of light</td></tr><tr><td>CCAUV</td><td>Consultative Committee for Acoustics, Ultrasound and Vibration</td></tr><tr><td>CCD</td><td>charge coupled device</td></tr><tr><td>CCDS</td><td>Comite Consultatif pour la Définition de la Seconde</td></tr><tr><td>CCEM</td><td>Consultative Committee for Electricity and Magnetism</td></tr><tr><td>CCIF</td><td>International Telephone Consultative Committee</td></tr><tr><td>CCIR</td><td>International Radio Consultative Committee</td></tr><tr><td>CCIT</td><td>International Telegraph Consultative Committee</td></tr><tr><td>CCITT</td><td>International Telephone and Telegraph Consultative Committee</td></tr><tr><td>CCL</td><td>Consultative Committee for Length</td></tr></table>

<table><tr><td>CCM</td><td>Consultative Committee for Mass and Related Quantities</td></tr><tr><td>CCPR</td><td>Consultative Committee for Photometry and Radiometry</td></tr><tr><td>CCQM</td><td>Consultative Committee for Amount of Substance -Metrology i Chemistry</td></tr><tr><td>CCRI</td><td>Consultative Committee forIonizingRadiation</td></tr><tr><td>CCT</td><td>Consultative Committee for Thermometry</td></tr><tr><td>CCTF</td><td>Consultative Committee for Time and Frequency</td></tr><tr><td>CCU</td><td>Consultative Committee for Units</td></tr><tr><td>CDMA</td><td>code division multiple access</td></tr><tr><td>CDS</td><td>Centre des Données astronomiques de Strasbourg</td></tr><tr><td>CD-TWSTFT</td><td>Carrier Doppler TWSTFT</td></tr><tr><td>CE</td><td>Common Era (Anno Domini)</td></tr><tr><td>CEO</td><td>Celestial Ephemeris Origin</td></tr><tr><td>CEP</td><td>Celestial Ephemeris Pole</td></tr><tr><td>CGPM</td><td>Conférence Général des Poids et Mesures</td></tr><tr><td>CIF</td><td>Celestial Intermediate Frame</td></tr><tr><td>CIO</td><td>Celestial Intermediate Origin</td></tr><tr><td>CIP</td><td>Celestial IntermediatePole</td></tr><tr><td>CIPM</td><td>Comite International des Poids et Mesures</td></tr><tr><td>CIRF</td><td>Celestial Intermediate (or True) Reference Frame</td></tr><tr><td>CIRS</td><td>Celestial Intermediate Reference System</td></tr><tr><td>CMB</td><td>cosmic microwave background</td></tr><tr><td>CMB</td><td>core-mantle boundary</td></tr><tr><td>CNES</td><td>Centre National d'Etudes Spatiales</td></tr><tr><td>CODE</td><td>Center for Orbit Determination in Europe</td></tr><tr><td>cpsd</td><td>cycles per sidereal day</td></tr><tr><td>CRS</td><td>Celestial Reference System</td></tr><tr><td>Cs</td><td>Caesium</td></tr><tr><td>CSNNPC</td><td>China Satellite Navigation Project Center</td></tr><tr><td>CTRF</td><td>Conventional Terrestrial Reference Frame</td></tr><tr><td>CTRS</td><td>Conventional Terrestrial Reference System</td></tr><tr><td>8</td><td>declination</td></tr><tr><td>DE</td><td>Development Ephemeris</td></tr><tr><td>DGFI-TUM</td><td>Deutsches Geodatisches Forschungsinstitut der Technischen UniversitatMunchen</td></tr><tr><td>DMA</td><td>Defense Mapping Agency (then NIMA, now NGA)</td></tr><tr><td>DORIS</td><td>Doppler Orbit Determination and Radiopositioning Integrated or</td></tr><tr><td>DoV</td><td>Satellite Deflection of the Vertical</td></tr><tr><td>DST</td><td>Daylight Savings Time</td></tr><tr><td>△T</td><td>TT-UT1</td></tr><tr><td></td><td></td></tr><tr><td>DUT1</td><td>low-precision prediction of UT1-UTC</td></tr><tr><td>DWDM</td><td>Dense Wavelength Division Multiplexing</td></tr><tr><td>EAL</td><td>Echelle Atomique Libre (Free Atomic Timescale)</td></tr><tr><td>EDT</td><td>Eastern Daylight Time</td></tr><tr><td>eLORAN</td><td>enhanced LORAN</td></tr><tr><td>EOP</td><td>Earth orientation parameters</td></tr><tr><td>EPS</td><td>Ensemble Pulsar Scale</td></tr><tr><td>ERA</td><td>Earth rotation angle</td></tr><tr><td>EROS</td><td>Earth Resources Observation Systems</td></tr><tr><td>ESA</td><td>European Space Agency</td></tr><tr><td>EST</td><td>Eastern Standard Time</td></tr><tr><td>ET</td><td>Ephemeris Time</td></tr><tr><td>ETR</td><td>Ephemeris TimeRevised</td></tr><tr><td>FAGS</td><td>Federation of Astronomical and Geophysical Data Analysis Services</td></tr><tr><td>FCN</td><td>Free Core Nutation</td></tr><tr><td>FDMA</td><td>frequency division multiple access</td></tr><tr><td>FK3</td><td>Third Fundamental Katalog</td></tr><tr><td>FK4</td><td>Fourth Fundamental Katalog</td></tr><tr><td>FK5</td><td>Fifth Fundamental Katalog</td></tr><tr><td>FLRW</td><td>Friedman-Lemaitre-Robertson-Walker</td></tr><tr><td>G GA</td><td>billion</td></tr><tr><td>GAST</td><td>Greenwich atomic timescale</td></tr><tr><td>GCRF</td><td>Greenwich Apparent Sidereal Angle</td></tr><tr><td></td><td>Geocentric Celestial Reference Frame</td></tr><tr><td>GCRS</td><td>Geocentric Celestial Reference System</td></tr><tr><td>GCT</td><td>Greenwich Civil Time</td></tr><tr><td>GEM</td><td>Goddard Earth Model</td></tr><tr><td>GGOS</td><td>Global Geodetic Observing System</td></tr><tr><td>GHz</td><td>gigahertz</td></tr><tr><td>GHA</td><td>Greenwich Hour Angle</td></tr><tr><td>GIA</td><td>Glacial Isostatic Adjustment</td></tr><tr><td>GMAT</td><td>Greenwich Mean Astronomical Time</td></tr><tr><td>GMJ</td><td>geomagnetic jerks</td></tr><tr><td>GMST</td><td>Greenwich Mean Sidereal Time</td></tr><tr><td>GMT</td><td>GreenwichMean Time</td></tr><tr><td>GNSS</td><td>Global Navigation Satellite Service</td></tr><tr><td>GPS</td><td>Global Positioning System</td></tr><tr><td>GR</td><td>general relativity</td></tr><tr><td>GRGS</td><td>Groupe de Recherche de Géodésie Spatiale</td></tr><tr><td>GRS</td><td>Geocentric Reference System</td></tr><tr><td>GRS</td><td>Geodetic Reference System</td></tr><tr><td>GSD</td><td>Greenwich Sidereal Date</td></tr><tr><td>GST</td><td>Greenwich Sidereal Time</td></tr><tr><td>GTRF</td><td>Geocentric True Reference Frame</td></tr><tr><td>HA</td><td>hour angle</td></tr><tr><td>HCRS</td><td>Hipparcos Catalog Reference System</td></tr><tr><td>HMNAO</td><td>Her Majesty's Nautical Almanac Office</td></tr><tr><td>HST</td><td>Hubble Space Telescope</td></tr><tr><td>IAA</td><td>Institute of Applied Astronomy</td></tr><tr><td>IACS</td><td>International Association of Cryospheric Sciences</td></tr><tr><td>IAG</td><td>International Association for Geodesy</td></tr><tr><td>IAGA</td><td>International Association of Geomagnetism and Aeronomy</td></tr><tr><td>IAHS</td><td>International Association of Hydrological Sciences</td></tr><tr><td>IAMAS</td><td>International Association of Meteorology and Atmospheric Sciences</td></tr><tr><td>IAPSO</td><td>International Association for the Physical Sciences of the Ocean</td></tr><tr><td>IASPEI</td><td>International Association of Seismology and Physics of the Earth's Interior</td></tr><tr><td>IAU</td><td>International Astronomical Union</td></tr><tr><td>IAVCEI</td><td>International Association of Volcanology and Chemistry of the Earth's Interior</td></tr><tr><td>ICET</td><td>International Center for Earth Tides</td></tr><tr><td>ICRF</td><td>International Celestial Reference Frame</td></tr><tr><td>ICRS</td><td>International Celestial Reference System</td></tr><tr><td>ICSU</td><td>International Council of Science (formerly the International Council of Scientific Unions)</td></tr><tr><td>IDS</td><td>International DORIS Service</td></tr><tr><td>IERS</td><td>International Earth Rotation and Reference System Service</td></tr><tr><td>IGN</td><td>Institut Géographique National</td></tr><tr><td>IGS</td><td>International GNSS Service</td></tr><tr><td>IHRF</td><td>International Hipparcos Reference Frame</td></tr><tr><td>ILE</td><td>ImprovedLunar Ephemeris</td></tr><tr><td>ILRS</td><td>International Laser Ranging Service</td></tr><tr><td>ILS</td><td>International Latitude Service</td></tr><tr><td>IMCCE</td><td>Institut de Mécanique Céleste et de Calcul des Ephemerides</td></tr><tr><td>IPMS</td><td>International Polar Motion Service</td></tr><tr><td>ISES</td><td>International Space Environment Service</td></tr><tr><td>ISGI</td><td>International Service of Geomagnetic Indices</td></tr><tr><td>ISS</td><td>International Space Station</td></tr><tr><td>ITRF</td><td>International TerrestrialReference Frame</td></tr><tr><td>ITRS</td><td>International Terrestrial Reference System</td></tr><tr><td>ITU-D</td><td>International Telecommunications Union-Development Sector</td></tr><tr><td>ITU-R</td><td>International Telecommunications Union-Radiocommunication Sector</td></tr><tr><td>ITU-T</td><td>International Telecommunications Union - Standardization Sector</td></tr><tr><td>IUGG</td><td>International Union of Geodesy and Geophysics</td></tr><tr><td>IVS</td><td>International VLBI Service for Geodesy and Astrometry</td></tr><tr><td>JD</td><td> Julian Date</td></tr><tr><td>JDN</td><td>Julian Day Number</td></tr><tr><td>JGM</td><td>Joint Gravity Model</td></tr><tr><td>K</td><td>degrees kelvin</td></tr><tr><td>kHz</td><td>kilohertz</td></tr><tr><td>LAGEOS</td><td>Laser Geodynamics Satellite</td></tr><tr><td>LAT</td><td>Local Apparent Solar Time</td></tr><tr><td>ΛCDM</td><td>Lambda-Cold Dark Matter</td></tr><tr><td>LCT</td><td>Local Civil Time</td></tr><tr><td>LED</td><td>light-emitting diode</td></tr><tr><td>LHA</td><td>local hour angle</td></tr><tr><td>LITS</td><td>Linear Ion Trap Frequency Standard</td></tr><tr><td>LLR</td><td>lunar laser ranging</td></tr><tr><td>LMT</td><td>Local Mean Time</td></tr><tr><td>LOD</td><td>length of day, commonly used to designate excess length of day</td></tr><tr><td>LORAN</td><td>Long Range Aid to Navigation</td></tr><tr><td>LSST</td><td>Large Synoptic Survey Telescope</td></tr><tr><td>LST</td><td>Local Sidereal Time</td></tr><tr><td>MACHO</td><td>MAssive Compact Halo Objects</td></tr><tr><td>mas</td><td>milliarcsecond</td></tr><tr><td>μas</td><td>microarcsecond</td></tr><tr><td>μs</td><td>microsecond</td></tr><tr><td>MCXO</td><td>microcomputer-controlled crystal oscillator</td></tr><tr><td>MEO</td><td>MediumEarthOrbit</td></tr><tr><td>MJD</td><td>Modified Julian Day</td></tr><tr><td>mm</td><td>millimeter</td></tr><tr><td>Mpc</td><td>Megaparsecs</td></tr><tr><td>ms</td><td>millisecond</td></tr><tr><td>MT</td><td>Mars Time</td></tr><tr><td>nas</td><td>nanoarcsecond</td></tr><tr><td>NASA</td><td>National Aeronautical and Space Agency</td></tr><tr><td>NBS</td><td>National Bureau of Standards (now NIST)</td></tr><tr><td></td><td>National Geospatial Intelligence Agency (Formerly NIMA and DM</td></tr><tr><td>NGA</td><td>National Institute of Information and Communications</td></tr><tr><td>NICT</td><td>National Institute of Metrology (Beijing, China)</td></tr><tr><td>NIM NIMA</td><td>National Imaging and Mapping Agency (Now NGA)</td></tr><tr><td>NIST</td><td>National Institute of Standards and Technology</td></tr><tr><td>nm</td><td>nanometer</td></tr><tr><td></td><td>National Physical Laboratory</td></tr><tr><td>NPL</td><td></td></tr></table>

<table><tr><td>NRC</td><td>National Research Laboratory of Canada</td></tr><tr><td>ns</td><td>nanosecond</td></tr><tr><td>NSFA</td><td>Numerical Standards of Fundamental Astronomy</td></tr><tr><td>NTP</td><td>Network TimeProtocol</td></tr><tr><td>OAM</td><td>ocean angular momentum</td></tr><tr><td>OCXO</td><td>oven-controlled crystal oscillator</td></tr><tr><td>OGLE</td><td>optical gravitational lensing experiment</td></tr><tr><td>ON</td><td>Observatoire de Neuchatel</td></tr><tr><td>OP</td><td>Observatoire de Paris</td></tr><tr><td>OTS</td><td>optical-to-THz synthesizer</td></tr><tr><td>PanSTARRS</td><td>Panoramic Survey Telescope and Rapid Response System</td></tr><tr><td>PHARAO</td><td>Projet d'Horloge Atomique par Refroidissement d'Atomes en orbite</td></tr><tr><td>POSS</td><td>Palomar Optical Sky Survey</td></tr><tr><td>ppb</td><td> parts per billion</td></tr><tr><td>PPN</td><td>parameterized post-Newtonian</td></tr><tr><td>PPP</td><td>Precise Point Positioning</td></tr><tr><td>PPTA</td><td>Parkes Pulsar Timing Array</td></tr><tr><td>ps</td><td>picosecond</td></tr><tr><td>PSMSL</td><td>Permanent ServiceforMean SeaLevel</td></tr><tr><td>PTB</td><td>Physikalische TechnischeBundesanstalt</td></tr><tr><td>PZT</td><td>photographic zenith tube</td></tr><tr><td>QBSA</td><td>Quarterly Bulletin of Solar Activity</td></tr><tr><td>Rb</td><td>Rubidium</td></tr><tr><td>RDV</td><td>Research and Development with the VLBA</td></tr><tr><td>RGO</td><td>Royal Greenwich Observatory</td></tr><tr><td>rms</td><td>root mean square</td></tr><tr><td>S</td><td>second</td></tr><tr><td>SAO</td><td>Smithsonian Astrophysical Observatory</td></tr><tr><td>SEC</td><td>Security and Exchange Commission</td></tr><tr><td>SHM</td><td>Satellite Hydrogen Maser</td></tr><tr><td>SI</td><td>SystemeInternational</td></tr><tr><td>SIDC</td><td>Solar Influences Data Analysis Center</td></tr><tr><td>SLR</td><td>Satellite Laser Ranging</td></tr><tr><td>SOFA</td><td>Standards of Fundamental Astronomy</td></tr><tr><td>SONET</td><td>synchronous optical networking</td></tr><tr><td>ST</td><td>sidereal time</td></tr><tr><td>STScI</td><td>Space Telescope Science Institute</td></tr><tr><td>TA(BIH)</td><td>BIH atomic timescale</td></tr><tr><td>TA(k)</td><td>atomic timescales from source k</td></tr><tr><td>TAI</td><td>International Atomic Time</td></tr><tr><td>TCA</td><td>Areocentric Coordinate Time</td></tr><tr><td></td><td>Barycentric Coordinate Time</td></tr><tr><td>TCB TCG</td><td>Geocentric Coordinate Time</td></tr><tr><td>TCM</td><td>Mars Coordinate Time</td></tr><tr><td>TCXO</td><td>temperature-compensated crystal oscillator</td></tr><tr><td>TDA</td><td>Time Domain Astronomy</td></tr><tr><td>TDB</td><td>Barycentric Dynamical Time</td></tr><tr><td>TDM</td><td>time division multiplexing</td></tr><tr><td>TDMA</td><td> time division multiple access</td></tr><tr><td>TDT</td><td>Terrestrial Dynamical Time</td></tr><tr><td>TEC</td><td>total electron content</td></tr><tr><td>TEO</td><td>Terrestrial Ephemeris Origin</td></tr><tr><td>Teph</td><td>Barycentric Ephemeris Time</td></tr><tr><td>THz</td><td>terahertz</td></tr><tr><td>TIO</td><td>Terrestrial Intermediate Origin</td></tr><tr><td>TOS</td><td>THz-to-optical synthesizer</td></tr><tr><td>TT</td><td>Terrestrial Time</td></tr><tr><td>TVAR</td><td>time variation</td></tr><tr><td>TWAS</td><td>Third World Academy of Sciences</td></tr><tr><td>TWSFT</td><td>Two-way Satellite Time and Frequency Transfer</td></tr><tr><td>UCAC</td><td>USNO CCD Astrographic Catalog</td></tr><tr><td>UNESCO</td><td>United Nations Educational, Scientific and Cultural Organization</td></tr><tr><td>URSI</td><td>International Union of Radio Science</td></tr><tr><td>USNAO</td><td>US Nautical Almanac Office</td></tr><tr><td>USNO</td><td>US Naval Observatory</td></tr><tr><td>UT</td><td>Universal Time</td></tr><tr><td>UT0</td><td>Universal Time 0</td></tr><tr><td>UT1</td><td>Universal Time 1</td></tr><tr><td>UT2</td><td>Universal Time 2</td></tr><tr><td>UTC</td><td>Coordinated Universal Time</td></tr><tr><td>VGOS</td><td>VLBI2010 Global Observing System</td></tr><tr><td>VieVS</td><td>Vienna VLBI Software</td></tr><tr><td>VLBA</td><td>Very Long Baseline Array</td></tr><tr><td>VLBI</td><td>Very Long Baseline Interferometer</td></tr><tr><td>VLF</td><td>very low frequency</td></tr><tr><td>WDS</td><td>World Data System</td></tr><tr><td>WGD</td><td>World Geodetic Datum</td></tr><tr><td>WGD2000</td><td>World Geodetic Datum 2000</td></tr><tr><td>WGFS</td><td>Frequency Standards Working Group</td></tr><tr><td>WGMS</td><td>World Glacier Monitoring Service</td></tr><tr><td>WGS</td><td>World Geodetic System</td></tr><tr><td>WIPM</td><td>Wuhan Institute of Physics and Mathematics</td></tr><tr><td>WRC</td><td>World Radiocommunication Conference</td></tr><tr><td>Z</td><td>zenith distance</td></tr></table>

# Glossary

ΔT: the difference between Terrestrial Time and Universal Time; specifically the difference between Terrestrial Time (TT) and UT1: $\Delta \mathrm { T } = \mathrm { T } \mathrm { T } - \mathrm { U } \mathrm { T } 1$ .

aberration: the apparent angular displacement of the observed position of a celestial object from its geometric position, caused by the finite velocity of light in combination with the motions of the observer and of the observed object. Annual aberration is due to the motion of the Earth around the Sun, while diurnal aberration is due to the Earth’s rotation.

accuracy: closeness of an estimated (e.g., measured or computed) value to a standard or accepted value of a particular quantity.

Allan variance: the square root of the sum of the squares of the differences between consecutive readings divided by twice the number of differences.

almanac, astronomical: an annual publication containing information on the locations of celestial bodies, together with the times and circumstances of various astronomical events such as sunset and sunrise, of particular use for navigation.

altitude: the angular distance of a celestial body above or below the horizon, measured along the great circle passing through the body and the zenith. Altitude is $9 0 ^ { \circ }$ minus zenith distance.

analemma: a curve showing the angular offset of a celestial body (usually the Sun) from its mean position on the celestial sphere as viewed from another celestial body (usually the Earth). In the case of the Sun as seen from the Earth, this is a curve resembling a figure of eight that is commonly printed on globes.

angular momentum: measure of the extent to which an object will continue to rotate about a reference point unless acted upon by an external torque. Angular momentum is related to the mass, velocity, and distance of an object from the reference point.

anomaly: angular measurement of a body in its orbit from its pericenter.

aphelion: the point in a planetary orbit that is at the greatest distance from the Sun.

apogee: the point at which a body in orbit around the Earth reaches its farthest distance from the Earth. Apogee is sometimes used with reference to the apparent orbit of the Sun around the Earth.

apparent place: the position at which the object would actually be seen from the center of the Earth, as described by apparent right ascension and declination.

apparent right ascension and declination: angular coordinates in the true equator and equinox of date reference system at a specified date. They are geocentric positions differing from the ICRS positions by annual parallax, gravitational light deflection due to the solar system bodies except the Earth, annual aberration, and the time-dependent rotation describing the transformation from the GCRS to the Celestial Intermediate Reference System (they are similar to intermediate positions in the CIO-based system but the apparent right ascension origin is at the equinox). Note that apparent declination is identical to intermediate declination.

apparent solar time: the measure of time based on the diurnal motion of the true Sun. The rate of diurnal motion undergoes seasonal variation because of the obliquity of the ecliptic and the eccentricity of the Earth’s orbit. Additional small variations result from irregularities in the rotation of the Earth on its axis.

aspect: the apparent angular position of any of the planets or the Moon relative to the Sun, as seen from Earth.

asterism: a pattern of stars seen in the Earth’s sky which is not an official constellation.

astrometric ephemeris: an ephemeris of a solar system body in which the tabulated positions are essentially comparable to catalog mean places of stars at a standard epoch. An astrometric position is obtained by adding to the geometric position, computed from gravitational theory, the correction for light-time.

astronomical coordinates: the longitude and latitude of a point on Earth relative to the geoid. These coordinates are influenced by local gravity anomalies.

astronomical horizon: locus of points with a zenith distance of $9 0 ^ { \circ }$ .

astronomical unit (au): 149 597 870 700 meters. Prior to 2012, the au was the distance from the center of the Sun at which a particle of negligible mass, in an unperturbed circular orbit, would have an orbital period of 365.2568983 days. This is slightly less than the semimajor axis of the Earth’s orbit.

atomic second: see second, Système International.

axis of inertia: the axis of a principal moment of inertia. In the case of Earth, if it is considered symmetrical under rotation about a given axis, the symmetry axis is a principal axis. Also referred to as the axis of figure.

axis of rotation: the instantaneous axis about which the Earth’s rotation is taking place.   
It moves slowly around the axis of figure and this motion is referred to as polar motion.

azimuth: the angular distance measured clockwise along the horizon from a specified reference point (usually north) to the intersection with the great circle drawn from the zenith through a body on the celestial sphere.

barycenter: the center of mass of a system of bodies, e.g., the center of mass of the solar system or the Earth-Moon system.

Barycentric Celestial Reference System (BCRS): a system of barycentric space-time coordinates for the solar system within the framework of general relativity with metric tensor specified by the IAU. Formally, the metric tensor of the BCRS does not fix the coordinates completely, leaving the final orientation of the spatial axes undefined. However, for all practical applications, the BCRS is assumed to be oriented according to the ICRS axes.

Barycentric Coordinate Time (TCB): the coordinate time of the BCRS; it is related to Geocentric Coordinate Time (TCG) by relativistic transformations that include secular terms.

Barycentric Dynamical Time (TDB): a timescale originally intended to serve as an independent time argument of barycentric ephemerides and equations of motion. In the

IAU 1976 resolutions, the difference between TDB and TDT was stipulated to consist of only periodic terms, a condition that cannot be satisfied rigorously. The IAU 1991 resolutions introducing barycentric coordinate time (TCB) noted that TDB is a linear function of TCB, but without explicitly fixing the rate ratio and zero point, leading to multiple realizations of TDB. In 2006, TDB was redefined through a linear transformation of TCB.

Barycentric Ephemeris Time $\mathbf { ( T _ { e p h } ) }$ : the timescale of the JPL DE ephemeris that has been scaled to Terrestrial Time. It is equivalent to the redefined TDB.

Baryon: a composite subatomic particle made up of three quarks. Baryons and mesons belong to the hadron family of particles.

Baryonic dark matter: dark matter, which is undetectable from emitted radiation, but its presence is inferred from gravitational effects on visible matter. It is composed of baryons, which are protons and neutrons and combinations of these.

Big Bang theory: the favored cosmological model for the universe. This model explains the expansion of the universe from a high-density and high-temperature state, and a range of current observed phenomena, including abundance of light elements, cosmic microwave background, large-scale structure, and Hubble’s law. The big bang is estimated to have occurred approximately 13.8 billion years ago, which is the current age of the universe.

Boltzmann constant: a physical constant relating energy at the individual particle level with temperature. Its dimension is energy divided by temperature. The SI value is $1 . 3 8 0 6 4 8 \dot { 5 } 2 ( 7 9 ) \times 1 0 ^ { - 2 3 } \mathrm { J / K }$ .

caesium fountain: an apparatus that realizes the SI definition of the second by vertically launching caesium atoms through a microwave cavity and allowing gravity to bring the atoms back down through the cavity.

calendar: a system of reckoning time in which days are enumerated according to their position in cyclic patterns.

catalog equinox: the intersection of the hour circle of zero right ascension of a star catalog with the celestial equator.

Celestial Ephemeris Origin (CEO): the original name for the Celestial Intermediate Origin (CIO) given in the IAU 2000 resolutions.

Celestial Ephemeris Pole (CEP): the reference pole for nutation and polar motion used from 1984 to 2003 with the IAU 1980 Theory of Nutation; the axis of figure for the mean surface of a model Earth in which the free motion has zero amplitude. This pole was originally defined as having no nearly diurnal nutation with respect to a space-fixed or Earth-fixed coordinate system and being realized by the IAU 1980 nutation. It is now replaced by the CIP.

celestial equator: the plane perpendicular to the Celestial Ephemeris Pole. Colloquially, the projection onto the celestial sphere of the Earth’s equator.

Celestial Intermediate Origin (CIO): origin for right ascension on the intermediate equator in the Celestial Intermediate Reference System. It is the nonrotating origin in the GCRS that is recommended by the IAU. The CIO was originally set close to the GCRS meridian and throughout 1900–2100 stays within 0.1 arcseconds of this alignment.

Celestial Intermediate Pole (CIP): geocentric equatorial pole defined as being the intermediate pole, in the transformation from the GCRS to the ITRS, separating nutation from polar motion. It replaced the CEP on January 1, 2003. Its GCRS position results from (i) the part of precession/nutation with periods greater than two days, and (ii) the retrograde diurnal part of polar motion (including the free core nutation [FCN]) and (iii) the frame bias. Its ITRS position results from (i) the part of polar motion that is outside the retrograde diurnal band in the ITRS and (ii) the motion in the ITRS corresponding to nutations with periods less than two days. The motion of the CIP is realized by the IAU precession/ nutation plus time-dependent corrections provided by the IERS.

Celestial Intermediate Reference System (CIRS): geocentric reference system related to the GCRS by a time-dependent rotation taking into account precession/nutation. It is defined by the intermediate equator (of the CIP) and CIO on a specific date. It is similar to the system based on the true equator and equinox of date, but the equatorial origin is at the CIO.

celestial pole: either of the two points projected onto the celestial sphere by the extension of the Earth’s axis of rotation to infinity.

celestial pole offsets: time-dependent corrections to the precession/nutation model, determined by observations. The IERS provides the celestial pole offsets in the form of the differences, dX and dY, of the CIP coordinates in the GCRS with respect to the IAU 2000A precession/nutation model (i.e., the CIP is realized by the IAU 2000A precession/nutation plus these celestial pole offsets). In parallel the IERS also provides the offsets, dψ and dε, in longitude and obliquity with respect to the IAU 1976/1980 precession/nutation model.

celestial pole offsets at J2000.0: offset of the direction of the mean pole at J2000.0, provided by the current model, with respect to the GCRS. These offsets are part of what is often called frame bias.

celestial sphere: an imaginary sphere of arbitrary radius upon which celestial bodies may be considered to be located. As circumstances require, the celestial sphere may be centered at the observer, at the Earth’s center, or at any other location.

center of figure: that point so situated relative to the apparent two-dimensional figure of a body that any line drawn through it divides the figure into two parts having equal apparent volumes. If the body is oddly shaped, the center of figure may lie outside the figure itself.

Chandler wobble: the approximately 435-day periodic motion of the CIP in the ITRF corresponding to the free motion of the non-rigid Earth.

chronometer: high-precision, portable timekeeping device.

clepsydra: a device to measure time based on the uniform flow of water. From the Greek, literally it means a water thief.

clock: any device for indicating the time.

conjunction: the phenomenon in which two bodies have the same apparent celestial longitude or right ascension as viewed from a third body. Conjunctions are usually tabulated as geocentric phenomena. For Mercury and Venus, geocentric inferior conjunction occurs when the planet is between the Earth and Sun, and superior conjunction occurs when the Sun is between the planet and Earth.

constellation: a grouping of stars, usually with pictorial or mythical associations, that serves to identify an area of the celestial sphere. Also, one of the precisely defined areas of the celestial sphere, associated with a grouping of stars that the IAU has designated as a constellation.

Conventional International Origin: the international origin of polar motion adopted for use by the former International Latitude Service (ILS). It was defined in 1967 by an adopted set of astronomical latitudes of the five stations of the ILS. It approximately coincided with the mean pole of 1903.0 as determined by the ILS. To avoid ambiguity, this origin should be designated by its full name. This designation should be avoided for the current origin (the ITRF pole) of the polar motion, which no longer coincides with the conventional international origin.

coordinate time: the time coordinate, which, together with three spatial coordinates specify an event in a four-dimensional space-time reference system. An unambiguous way of dating and the time based on the theory of motion in a specific reference system.

Coordinated Universal Time (UTC): the timescale differing from TAI by an integral number of seconds; it is maintained within $\pm 0 . 9 0$ second of UT1 by the introduction of onesecond steps (leap seconds).

Coriolis effect: an apparent deflection of moving objects when they are viewed from a rotating frame. The Coriolis effect is caused by a fictitious Coriolis force, which appears in the equation of motion of an object in a rotating frame of reference.

Cosmic Microwave Background (CMB): the thermal radiation left from the hot early phase of the big bang. CMB is the oldest light in the Universe, which today is strongest in the microwave wavelengths.

cosmic time: proper time of co-moving observers in the universe.

cosmology: the study of the origin, evolution, and future of the universe and the physical laws involved.

Coulomb interaction: the static interaction between two charges, $\mathrm { Q } _ { 1 }$ and $\mathrm { Q } _ { 2 } .$ separated by a distance r producing a force proportional to $\mathrm { Q } _ { 1 } \mathrm { Q } _ { 2 } / \mathrm { r } ^ { 2 }$ .

crustal motion: the motion of large surface areas of the Earth with respect to other surface areas, also referred to as plate tectonics and continental drift.

culmination: passage of a celestial object across the observer’s meridian; also called “meridian passage.” More precisely, culmination is the passage through the point of greatest altitude in the diurnal path. Upper culmination (also called “culmination above pole” for circumpolar stars and the Moon) or transit is the crossing closer to the observer’s zenith. Lower culmination (also called “culmination below pole” for circumpolar stars and the Moon) is the crossing farther from the zenith.

dark energy: an unknown form of energy that is thought to exist and cause the acceleration of the expansion of the universe. Its primary characteristic is that its density does not decrease with cosmic expansion.

dark matter: the unidentified $2 7 \%$ of the mass and energy in the observable universe, not accounted for by dark energy, baryonic matter, radiation, and neutrinos. It does not emit or interact with electromagnetic radiation and is, hence, invisible in the electromagnetic spectrum.

day: an interval of 86 400 SI seconds, unless otherwise indicated.

decadal variations: quasi-periodic components of polar motion or observed variations of the Earth’s rotation with periods between 2 and 40 years apparently due to interactions between the Earth’s mantle and liquid core. Also decadal polar motion, decadal irregularities, decadal fluctuations.

decans: 36 groupings of stars used to reckon time in ancient Egypt.

declination: angular distance on the celestial sphere north or south of the celestial equator.   
It is measured along the hour circle passing through the celestial object.

deferent: In representing the motion of planets with epicycles, the circle centered around a point halfway between a point called the equant and the Earth on which an epicycle moves with uniform motion, not with respect to the center, but with respect to the equant.

deflection of light: the angle by which the apparent path of a photon is altered from a straight line by the gravitational field of a massive object situated along the path of the photon. In the case of the Sun, the path is deflected radially away from the Sun by up to

$1 " . 7 5$ at the Sun’s limb. Correction for this effect, which is independent of wavelength, is included in the reduction from mean place to apparent place.

deflection of the vertical: the angle between the astronomical and the geodetic vertical.

delta T: See ΔT.

delta UT1: See ΔUT1.

direct motion: for planetary movement in the solar system, motion that is counterclockwise in the orbit as seen from the north pole of the ecliptic; for an object observed on the celestial sphere, motion that is from west to east, resulting from the motion of the object relative to the Earth.

diurnal motion: the apparent daily motion, caused by the Earth’s rotation, of celestial bodies across the sky from east to west.

Doppler cooling: a mechanism based on the Doppler effect used to trap and cool atoms, and sometimes used synonymously with laser cooling.

Doppler effect: the change in frequency of a received signal due to the relative motion of an observer with respect to the source of the signal.

DUT1: predicted value of UT1−UTC with an accuracy of $\pm 0 . 1 \mathrm { s }$ .

dynamical equinox: the ascending node of the Earth’s mean orbit on the Earth’s true equator; i.e., the intersection of the ecliptic with the celestial equator at which the Sun’s declination changes from south to north.

dynamical time: the independent variable of the equations of motion of solar system bodies.

Earth’s inner core: a solid sphere of nickel and iron at the center of the Earth about $1 { , } 2 2 0 \mathrm { k m }$ in radius.

Earth’s mantle: a highly viscous layer directly under the crust and above the outer core, about $2 { , } 9 0 0 \mathrm { k m }$ thick.

Earth orientation: information specifying the relationship of terrestrial and celestial reference frames.

Earth’s outer core: liquid layer, approximately $2 , 3 0 0 ~ \mathrm { k m }$ thick, composed of iron and nickel above the solid inner core.

Earth Rotation Angle (ERA): angle measured along the intermediate equator of the Celestial Intermediate Pole (CIP) between the Terrestrial Intermediate Origin (TIO) and the Celestial Intermediate Origin (CIO), positively in the retrograde direction. It is related to UT1 by a conventionally adopted expression in which ERA is a linear function of UT1. Its time derivative is the Earth’s angular velocity.

eccentric anomaly: in undisturbed elliptic motion, the angle measured at the center of the ellipse from pericenter to the point on the circumscribing auxiliary circle from which a perpendicular to the major axis would intersect the orbiting body.

eccentricity: a parameter that specifies the shape of a conic section; one of the standard elements used to describe an elliptic orbit.

eclipse: the obscuration of a celestial body caused by its passage through the shadow cast by another body.

eclipse, annular: a solar eclipse in which the solar disk is never completely covered but is seen as an annulus or ring at maximum eclipse. An annular eclipse occurs when the apparent disk of the Moon is smaller than that of the Sun.

eclipse, lunar: an eclipse in which the Moon passes through the shadow cast by the Earth. The eclipse may be total (the Moon passing completely through the Earth’s umbra), partial (the Moon passing partially through the Earth’s umbra at maximum eclipse), or penumbral (the Moon passing only through the Earth’s penumbra).

eclipse, solar: an eclipse in which the Earth passes through the shadow cast by the Moon. It may be total (observer in the Moon’s umbra), partial (observer in the Moon’s penumbra), or annular.

ecliptic: the plane perpendicular to the mean heliocentric orbital angular momentum vector of the Earth-Moon barycenter in the Barycentric Celestial Reference System, commonly the mean plane of the Earth’s orbit.

elements, Besselian: quantities tabulated for the calculation of accurate predictions of an eclipse or occultation for any point on or above the surface of the Earth.

elements, orbital: parameters that specify the position and motion of a body in orbit.

entropy: a measure of the number of microscopic configurations in a thermodynamic system specified by certain macroscopic variables. If each microscopic configuration is equally probable, the entropy of the system is the natural logarithm of that number of configurations multiplied by the Boltzmann constant.

epact: the number of days in the age of the moon on January 1 of any given year in the Gregorian calendar system.

ephemeris: a tabulation of the positions of a celestial object in an orderly sequence for a number of dates.

ephemeris second: the second defined in 1960 as 1/31556925.9747 of the tropical year for 1900 January 0 12 hours ET.

Ephemeris Time (ET): the timescale used from 1960 to 1984 as the independent variable in gravitational theories of the solar system, with its unit and origin conventionally defined. It was superseded by TT and TDB.

epicycle: in representing the motion of planets with epicycles, a circular orbit, whose center moves uniformly over a circular orbit around the Earth called the deferent.

epoch: a fixed instant of time used as a chronological reference datum for calendars, celestial reference systems, star catalogs, or orbital motions.

equation of center: in elliptic motion, the true anomaly minus the mean anomaly. It is the difference between the actual angular position in the elliptic orbit and the position the body would have if its angular motion were uniform.

equation of the equinoxes: the right ascension of the mean equinox referred to the true equator and equinox; alternatively the difference between apparent sidereal time and mean sidereal time (GAST−GMST).

equation of the origins: distance between the CIO and the equinox along the intermediate equator; it is the CIO right ascension of the equinox; alternatively the difference between the Earth Rotation Angle and Greenwich Apparent Sidereal Time (ERA−GAST).

equation of time: the hour angle of the true Sun minus the hour angle of the fictitious mean sun; alternatively, apparent solar time minus mean solar time.

equator: the great circle on the surface of a body formed by the intersection of the surface with the plane passing through the center of the body perpendicular to the reference axis.

equinox: either of the two points on the celestial sphere at which the ecliptic intersects the celestial equator; also, the time at which the Sun passes through either of these intersection points; i.e., when the apparent longitude of the Sun is $0 ^ { \circ }$ or $1 8 0 ^ { \circ }$ .

era: a system of chronological notation reckoned from a given date.

escapement: a device that controls the continuous motion of the clock’s driving mechanism using the periodic motion of its regulator.

fictitious mean sun: an imaginary body introduced to define mean solar time; essentially the name of a mathematical formula that defined mean solar time. This concept is no longer used in high-precision work.

flattening: a parameter that specifies the degree by which the shape of an ellipsoid of revolution differs from a sphere; the ratio $\mathbf { f } = ( \mathbf { a } { - } \mathbf { b } ) / \mathbf { a }$ , where a is the equatorial radius and b is the polar radius.

flicker frequency noise: a type of statistical noise observed in the output frequency of a oscillator that has a 1/f spectrum, where f is the sampling frequency.

flicker phase noise: a type of statistical noise observed in the timing signal of a clock that has a 1/f spectrum, where f is the sampling frequency.

foliot: in a verge and foliot clock, the crossbar on the verge that controls the time it takes for the verge to rotate.

frame bias: the three offsets of the mean equator and (dynamical) mean equinox of J2000.0, provided by the current model, with respect to the GCRS; the first two offsets are the mean pole offsets at J2000.0 and the third is the offset in right ascension of the mean dynamical equinox of J2000.0.

free core nutation (FCN): free retrograde diurnal mode in the motion of the Earth’s rotation axis with respect to the Earth, due to nonalignment of the rotation axis of the core and of the mantle; it is a long-period (432 days) free nutation of the CIP in the GCRS.

free-falling frame: an isolated local frame that is electrically and magnetically shielded, sufficiently small that inhomogeneities in external fields can be ignored, and self-gravitating effects are negligible.

frequency: the number of cycles or complete alternations per unit time of a carrier wave, band, or oscillation.

frequency comb: a tool for measuring different colors, or frequencies, of light in which a mode-locked laser provides an optical spectrum consisting of equidistant lines, which can be used as an optical ruler.

frequency standard: a stable oscillator whose output is used as a precise frequency reference; a primary frequency standard is one whose frequency corresponds to the adopted definition of the second, with its specified accuracy achieved without calibration of the device.

GALILEO: a European satellite navigation system.

Gaussian gravitational constant: used as a constant in the definition of the au prior to 2012 $\left( \mathbf { k } = \mathbf { 0 . 0 1 7 } ~ 2 0 2 ~ 0 9 8 ~ 9 5 \right)$ : the gravitational constant specified in units of length (astronomical unit), mass (solar mass), and time (day).

geocentric: with reference to, or pertaining to, the center of the Earth.

Geocentric Celestial Reference System (GCRS): a system of geocentric space-time coordinates within the framework of general relativity with metric tensor specified by the IAU. The GCRS is defined such that the transformation between BCRS and GCRS spatial coordinates contains no rotation component, so that GCRS is kinematically nonrotating with respect to the BCRS. The equations of motion of, for example, an Earth satellite, with respect to the GCRS will contain relativistic Coriolis forces that come mainly from geodesic precession. The spatial orientation of the GCRS is derived from that of the BCRS, that is, by the orientation of the ICRS.

geocentric coordinates: the latitude and longitude of a point on the Earth’s surface relative to the center of the Earth; also, celestial coordinates given with respect to the center of the Earth.

Geocentric Coordinate Time (TCG): coordinate time of the GCRS based on the SI second. It is related to Terrestrial Time (TT) by a conventional linear transformation.

Geocentric Terrestrial Reference System (GTRS): a system of geocentric space-time coordinates within the framework of general relativity, co-rotating with the Earth, and related to the GCRS by a spatial rotation that takes into account the Earth orientation parameters. It was adopted by IUGG 2007 Resolution 2. It replaces the previously defined Conventional Terrestrial Reference System.

geodesic precession and nutation: a Coriolis-like effect from relativistic theory in the transformations of the fixed directions of the GCRS referred to the BCRS. They are the largest components of the relativistic rotation of the GCRS with respect to a dynamically nonrotating geocentric reference system in the framework of general relativity. Geodesic precession is the secular part of the rotation and geodesic nutation is the periodic part. Geodesic precession and nutation are included in the IAU 2000 precession/nutation model.

geodetic coordinates: the latitude and longitude of a point on the Earth’s surface determined using the geodetic vertical (normal to the specified spheroid).

geoid: an equipotential surface that coincides with mean sea level in the open ocean. On land, it is the level surface that would be assumed by water in an imaginary network of frictionless channels connected to the ocean.

geometric position: the geocentric position of an object on the celestial sphere referred to the true equator and equinox, but without including the displacement due to planetary aberration.

getter: component of a caesium beam tube frequency standard that absorbs caesium atoms.

glacial isostatic adjustment: the ongoing movement of land once covered by ice-age glaciers.

Global Positioning System (GPS): a US satellite navigation system.

GLONASS: a Russian satellite navigation system.

GPS Time: a timescale based on the clocks of the GPS that is maintained within better than one microsecond of UTC, or TAI, modulo one second. It differs from UTC depending on the number of leap seconds, since GPS Time is not adjusted for leap seconds.

gravitational constant: denoted G, is an empirical physical constant used to specify the gravitational attraction between objects.

great circle: the circle formed by the intersection of a sphere with a plane that passes through the center of the sphere.

great empirical term: a periodic term introduced into lunar theories prior to the 20th century in an attempt to make the theories agree with the observations.

Greenwich Apparent Sidereal Time (GAST): the hour angle of the true equinox from the Terrestrial Intermediate Origin (TIO) meridian. Also Greenwich Sidereal Time.

Greenwich Civil Time (GCT): Term used from 1925 until 1952 to refer to Greenwich Mean Time reckoned from midnight. Replaced by Universal Time, officially, in 1952.

Greenwich Mean Astronomical Time (GMAT): the name recommended for use to designate mean solar time reckoned from noon at Greenwich when a 12-hour discontinuity was introduced in 1925 in GMT.

Greenwich Mean Sidereal Time (GMST): Greenwich hour angle of the mean equinox of date defined by a conventional relationship to the Earth rotation angle, or equivalently to UT1.

Greenwich Mean Time (GMT): currently the civil time of the United Kingdom. Once the predecessor of UTC for civil time and UT1 for celestial navigation. Prior to 1925, hours counted from noon.

Greenwich Sidereal Date (GSD): the number of sidereal days elapsed at Greenwich since the beginning of the Greenwich sidereal day that was in progress at Julian date 0.0.

Greenwich Sidereal Day Number: the integral part of the Greenwich Sidereal Date.

Gregorian calendar: the calendar Pope Gregory XIII introduced in 1582 to replace the Julian calendar; the calendar now used as the civil calendar in most countries. Every year that is exactly divisible by four is a leap year, except for centurial years, which must be exactly divisible by 400 to be leap years.

height: elevation above ground or distance upward from a given level (especially sea level) to a fixed point.

heliacal rising: rising of a celestial object at the same time as the Sun rises.

heliocentric: with reference to, or pertaining to, the center of the Sun.

high altitude winds: winds in the upper atmosphere.

horizon: a plane perpendicular to the direction of the zenith. The great circle formed by the intersection of the celestial sphere with a plane perpendicular to the direction of the zenith is called the astronomical horizon.

horizontal parallax: angle subtended by the Earth’s radius at the distance of a celestial body.

horologium: historical term for a clock, either a water clock, or verge and foliot clock.

hour angle: angular distance measured westward along the celestial equator from the meridian to the hour circle that passes through a celestial object.

hour circle: a great circle on the celestial sphere that passes through the celestial poles and is therefore perpendicular to the celestial equator.

Hubble constant: the rate of expansion of the universe, expressed as a velocity gradient, $\mathrm { k m / s / M p c }$ .

Hubble’s law: the observation that very distant objects have a redshift due to relative velocity away from Earth and that redshift is approximately proportional to their distance from Earth.

Hubble time: the reciprocal of the Hubble Constant, $1 4 \mathrm { G }$ (billion) years.

hydrogen maser: device that produces coherent electromagnetic waves through amplification due to stimulated emission of the hydrogen atom to serve as a precision frequency reference.

hyperfine levels: energy levels in the structure of individual atoms that originate from the interaction of the magnetic moments of the electron and the nucleus.

IAU 2000A precession nutation model: the IAU-recommended precession/nutation model representing the motion of the CIP for those who need a model at 0.2 mas level. An abridged model, designated IAU 2000B, is available for those who require a model at the 1 mas level. Standard programs are available from IERS and SOFA.

inclination: the angle between two planes or their poles; usually the angle between an orbital plane and a reference plane; one of the standard orbital elements that specifies the orientation of an orbit.

International Atomic Time (TAI): the continuous scale resulting from analyses by the Bureau International des Poids et Mesures of atomic time standards in many countries. The fundamental unit of TAI is the SI second, and the epoch is 1958 January 1.

International Celestial Reference Frame (ICRF): a set of extragalactic objects whose adopted positions and uncertainties realize the International Celestial Reference System axes and give the uncertainties of the axes. It is also the name of the radio catalog whose defining sources are currently the most accurate realization of the ICRS. The orientation of the ICRF catalog is within the errors of the standard stellar and dynamic frames at the time of adoption. Successive revisions of the ICRF are intended to minimize rotation from its original orientation. Other realizations of the ICRS have specific names (e.g., Hipparcos Celestial Reference Frame).

International Celestial Reference System (ICRS): the idealized barycentric coordinate system to which celestial positions are referred. It is kinematically nonrotating with respect to the ensemble of distant extragalactic objects. It has no intrinsic orientation but was aligned close to the mean equator and dynamical equinox of J2000.0 for continuity with previous fundamental reference systems. Its orientation is independent of epoch, ecliptic, or equator and is realized by a list of adopted coordinates of extragalactic sources.

International Terrestrial Reference Frame (ITRF): a realization of ITRS by a set of instantaneous coordinates (and velocities) of reference points distributed on the topographic surface of the Earth (mainly space geodetic stations and related markers). Currently the ITRF provides a model for estimating, to high accuracy, the instantaneous positions of these points, which is the sum of conventional corrections provided by the IERS Convention Center (solid Earth tides, pole tides) and of a “regularized” position. At present, the latter is modeled by a piecewise linear function, the linear part accounting for such effects as tectonic plate motion, glacial isostatic adjustment, and the piecewise aspect representing discontinuities such as seismic displacements. The initial orientation of the ITRF is that of the BIH Terrestrial System at epoch 1984.0.

International Terrestrial Reference System (ITRS): the ITRS is the specific GTRS for which the orientation is operationally maintained in continuity with past international agreements. The co-rotation condition is defined as no residual rotation with regard to the Earth’s surface, and the geocenter is understood as the center of mass of the whole Earth system, including oceans and atmosphere. For continuity with previous terrestrial reference systems, the first alignment was close to the mean equator of 1900 and the Greenwich meridian. The ITRS was adopted as the preferred GTRS for scientific and technical applications and is the recommended system to express positions on the Earth.

invariable plane: the plane through the center of mass of the solar system perpendicular to the angular momentum vector of the solar system.

ion: atom or molecule with a net electric charge due to the loss or gain of one or more electrons.

ITRF zero-meridian: the plane passing through the geocenter, ITRF pole, and ITRF $x$ -origin.

ITRS CIP coordinates: direction cosines of the CIP in the ITRS, also called pole coordinates. They are currently expressed in the form of $x$ and $y$ angular coordinates, in arcseconds, the values of which represent the corresponding angles with respect to the polar axis of the ITRS. The sign convention is such that $x$ is positive toward the $x \cdot$ -origin of the ITRS and $y$ is in the direction $9 0 ^ { \circ }$ to the west of $x$ .

J2000.0: defined in the framework of general relativity by IAU as being the event (epoch) at the geocenter and at the date 2000 January $1 . 5 \mathrm { T T } =$ Julian Date 245 1545.0 TT. Note that this event has different dates in different timescales.

Julian calendar: the calendar Julius Caesar introduced in $4 6 ~ \mathrm { B C }$ to replace the Roman calendar. In the Julian calendar, a common year is defined to comprise 365 days, and every fourth year is a leap year of 366 days. The Julian calendar was superseded by the Gregorian calendar.

Julian date (JD): the interval of time in days and fraction of a day since $4 7 1 3 \mathrm { ~ B C }$ , January 1, Greenwich noon, Julian proleptic calendar. In precise work, the timescale, e.g., dynamical time or Universal Time, should be specified.

Julian date, modified (MJD): the Julian date minus 2400000.5.

Julian day number: the integral part of the Julian date.

Julian proleptic calendar: the calendar system employing the rules of the Julian calendar, but extended and applied to dates preceding the introduction of the Julian calendar.

Julian year: a period of 365.25 days. This period served as the basis for the Julian calendar.

Laplacian plane: for planets, see invariable plane; for a system of satellites, the fixed plane relative to which the vector sum of the disturbing forces has no orthogonal component.

latitude, celestial: angular distance on the celestial sphere measured north or south of the ecliptic along the great circle passing through the poles of the ecliptic and the celestial object.

latitude, terrestrial: angular distance on the Earth measured north or south of the equator along the meridian of a geographic location.

leap second: a second added or subtracted at announced times to maintain UTC within 0.9 s of UT1. Generally, leap seconds are applied at the end of June or December.

length of day: strictly the number of fixed length seconds in the day determined from the rotation of the Earth, but most often used to refer to the excess length of day or the difference between the length of day and 86,400 SI seconds.

Lense-Thirring effect: also referred to as frame dragging. The rotation of an object alters the space and time, dragging a nearby object out of its position compared to the predictions of Newtonian physics.

librations: (1) variations in the orientation of the Moon’s surface with respect to an observer on the Earth. Physical librations are due to variations in the orientation of the Moon’s rotational axis in inertial space. The much larger optical librations are due to variations in the rate of the Moon’s orbital motion, the obliquity of the Moon’s equator to its orbital plane, and the diurnal changes of geometric perspective of an observer on the Earth’s surface. (2) variations in pole coordinates corresponding to motions with periods less than two days in space that are not part of the IAU 2000 nutation model.

light-time: the interval of time required for light to travel from a celestial body to the Earth. During this interval, the motion of the body in space may cause an angular displacement of its apparent place from its geometric place.

light-year: the distance that light traverses in a vacuum during one year $( 9 . 4 6 1 \times 1 0 ^ { 1 5 } \mathrm { m } )$ .

limb: the apparent edge of the Sun, Moon, a planet or any other celestial body with a detectable disk.

limb correction: angular correction made to the observed angular distance between the center of mass of the Moon and its limb due to the irregular surface of the Moon.

Liouville equation: basic mathematical formulation used to describe the changes in the angular momentum of a rotating system in response to applied torques.

local sidereal time: the local hour angle of a catalog equinox.

longitude, celestial: angular distance measured eastward along the ecliptic from the dynamical equinox to the great circle passing through the poles of the ecliptic and the celestial object.

longitude, terrestrial: angular distance measured along the Earth’s equator from the Greenwich meridian to the meridian of a geographic location.

Lorentz transformation: mathematical formulation to convert between two different observers’ measurements of space and time, where one observer is in constant motion with respect to the other.

lunar phases: cyclically recurring apparent forms of the Moon. New moon, first quarter, full moon, and last quarter are defined as the times at which the excess of the apparent celestial longitude of the Moon over that of the Sun is $0 ^ { \circ }$ , $9 0 ^ { \circ }$ , $1 8 0 ^ { \circ }$ , and $2 7 0 ^ { \circ }$ , respectively.

lunar secular acceleration: see Secular acceleration of the Moon.

lunation: the period of time between two consecutive new moons.

lunisolar tidal deceleration: the deceleration of the rotation of the Earth due to tidal interactions. Conservation of angular momentum is maintained by the acceleration of the Moon’s orbital motion.

Markowitz wobble: a small-amplitude, irregular, long-period ${ \sim } 3 0$ years) feature in the Earth’s polar motion reported by Wm. Markowitz in 1960, thought to be due to geophysical causes.

magnitude, stellar: a measure on a logarithmic scale of the brightness of a celestial object considered as a point source.

maser: an instrument that uses the monochromatic emission from a narrow band in the spectrum of a suitable molecule or atom to control the frequency of a radio-resonant circuit.

mean anomaly: in undisturbed elliptic motion, the product of the mean motion of an orbiting body and the interval of time since the body passed the pericenter. The mean anomaly is the angle from pericenter of a hypothetical body moving with a constant angular speed that is equal to the mean motion.

mean distance: the semi major axis of an elliptic orbit.

mean elements: elements of an adopted reference orbit that approximates the actual, perturbed orbit and may serve as the basis for calculating perturbations.

mean equator and equinox: equator and equinox associated with a celestial pole whose direction is determined only by the precession portion of the precession/nutation transformation.

mean motion: in undisturbed elliptic motion, the constant angular speed required for a body to complete one revolution in an orbit of a specified semi major axis.

mean place: position of an object on the celestial sphere referred to the mean equator and equinox at a standard epoch.

mean solar time: a measure of time based conceptually on the diurnal motion of the fictitious mean sun, under the assumption that the Earth’s rate of rotation is constant.

megaparsec: one million parsecs.

meridian: a great circle passing through the reference poles and through the zenith of any location on Earth. For planetary observations, a meridian is half the great circle passing through the planet’s poles and through any location on the planet.

metric space: a set where a notion of distance between elements is defined. The choice of the metric defines the geometric properties of the space.

microwave standard: device providing frequency based on energy-level transitions in atoms with wavelengths ranging from $1 \mathrm { m m }$ to $1 \textrm { m }$ .

moment of inertia: measure of an object’s resistance to changes in rotational velocity.

month: the period of one complete synodic or sidereal revolution of the Moon around the Earth; also, a calendrical unit that approximates the period of revolution of the Moon.

moonrise, moonset: the times at which the apparent upper limb of the Moon is on the astronomical horizon.

nadir: the point on the celestial sphere diametrically opposite to the zenith.

Newcomb’s Theory of the Sun: The theory of the Sun developed by Simon Newcomb and published in The Astronomical Papers for the American Ephemeris, volume VI, in 1898. It was the basis of the ephemeris of the Sun, timescales, and astronomical constants for about 80 years.

Newtonian mechanics: description of motions based on Newton’s Universal Law of Gravity.

node: either of the points on the celestial sphere at which the plane of an orbit intersects a reference plane. The position of a node is one of the standard orbital elements used to specify the orientation of an orbit.

non-rigid Earth: model of the Earth that includes the effects of core flattening, coremantle interactions, oceans, etc.

nonrotating origin: in the context of the GCRS or the ITRS, the point on the intermediate equator such that its instantaneous motion with respect to the system (GCRS or ITRS as appropriate) has no component along the intermediate equator (i.e., its instantaneous motion is perpendicular to the intermediate equator). It is called the CIO and TIO in the GCRS and ITRS, respectively.

numerical integration: the process of calculating the motion of a body by integrating the equations of motion.

nutation: the short-period oscillations in the motion of the pole of rotation of a freely rotating body that is undergoing torque from external gravitational forces.

obliquity: in general, the angle between the equatorial and orbital planes of a body or, equivalently, between the rotational and orbital poles. For the Earth, the obliquity of the ecliptic is the angle between the planes of the equator and the ecliptic.

occultation: the obscuration of one celestial body by another of greater apparent diameter; especially the passage of the Moon in front of a star or planet, or the disappearance of a satellite behind the disk of its primary. If the primary source of illumination of a reflecting body is cut off by the occultation, the phenomenon is also called an eclipse. The occultation of the Sun by the Moon is a solar eclipse.

opposition: a configuration of the Sun, Earth, and a planet in which the apparent geocentric longitude of the planet differs by $1 8 0 ^ { \circ }$ from the apparent geocentric longitude of the Sun.

optical clock: time standards based on energy-level transitions in atoms that provide precise frequencies in the optical range.

optical molasses: a cloud of atoms slowed in three dimensions by laser cooling.

optical pumping: process in which electromagnetic energy is used to raise (or “pump”) electrons from a lower energy level in an atom or molecule to a higher one.

orbit: the path in space followed by a celestial body.

orientation: the set of direction angles made by the axes of one coordinate system with the axes of the other.

oscillation: the repeated movement of an object, at equal time intervals, from one point to another and back again.

osculating elements: a set of parameters that specifies the instantaneous position and velocity of a celestial body in its perturbed orbit. Osculating elements describe the unperturbed (two-body) orbit that the body would follow, if perturbations were to cease instantaneously.

parallax: the difference in apparent direction of an object as seen from two different locations; annual parallax refers to the difference in directions as seen from the barycenter and the geocenter, while diurnal parallax refers to the component of parallax due to the observer’s separation from the geocenter.

parsec: the distance at which one astronomical unit subtends an angle of one second of arc; equivalently, the distance to an object having an annual parallax of one second of arc (3.09 $\times \ : 1 0 ^ { 1 9 } \mathrm { k m } )$ .

Paul trap: a quadrupole ion trap that exists in both linear and three-dimensional varieties that uses constant DC and radio frequency oscillating fields to trap ions.

pendulum clock: clock whose timing is based on the swinging of a pendulum.

Penning trap: a quadrupole ion trap using a constant static magnetic field and spatially inhomogeneous static electric field to trap ions.

penumbra: the portion of a shadow in which light from an extended source is partially but not completely cut off by an intervening body; the area of partial shadow surrounding the umbra.

pericenter: the point in an orbit that is nearest to the center of force.

perigee: the point at which a body in orbit around the Earth most closely approaches the Earth. Perigee is sometimes used with reference to the apparent orbit of the Sun around the Earth.

perihelion: the point at which a body in orbit around the Sun most closely approaches the Sun.

period: the interval of time required to complete one revolution in an orbit or one cycle of a periodic phenomenon.

perturbations: deviations between the actual orbit of a celestial body and an assumed reference orbit; also, the forces that cause deviations between the actual and reference orbits. Perturbations, according to the first meaning, are usually calculated as quantities to be added to the coordinates of the reference orbit to obtain the precise coordinates.

petabytes: $2 ^ { 5 0 }$ bytes, 1,024 terabytes, a million gigabytes where a byte is a unit of data that is eight binary digits long.

phase: in astronomical phenomena, the ratio of the illuminated area of the apparent disk of a celestial body to the area of the entire apparent disk taken as a circle. For eclipses, phase designations (total, partial, penumbral, etc.) provide general descriptions of the phenomena. More generally, for use with oddly shaped bodies, phase might be defined as $0 . 5 ( 1 + \cos$ (phase angle)); the phase of an oscillation or wave is the fraction of a complete cycle corresponding to an offset in the displacement from a specified reference point.

phase angle: the angle measured at the center of an illuminated body between the light source and the observer.

photometry: a measurement of the intensity of light usually specified for a specific frequency range.

piezoelectric effect: the ability of some materials (e.g., quartz crystals) to generate an electric potential in response to applied mechanical stress.

Planck’s Constant: (denoted h) a physical constant to describe the sizes of quanta in quantum mechanics. It is the proportionality constant between energy of a photon and the frequency of its associated electromagnetic wave.

polar motion: the motion of the Earth’s pole with respect to the ITRS.

post-glacial rebound: the rise of land masses that were depressed by the weight of ice sheets during the last glacial period. Also called continental rebound, glacial isostatic rebound, post-ice age isostatic recovery.

precession/nutation: the ensemble of effects of external torques on the motion in space of the rotation axis of a freely rotating body or alternatively, the forced motion of the pole of rotation due to those external torques. In the case of the Earth, a practical definition is that precession/nutation is the motion of the CIP in the GCRS, including the free core nutation and other corrections to the standard models. Precession is the secular part of this motion plus the term of a 26,000-year period and nutation is that part of the CIP motion not classed as precession.

precession of the ecliptic: the secular part of the motion of the ecliptic with respect to the fixed ecliptic.

precession of the equator (and CIP): the uniformly progressing motion of the pole of rotation of a freely rotating body, undergoing torque from external gravitational forces. In the case of the Earth, the precession of the equator is caused by solar system objects acting on the Earth’s equatorial bulge making the pole of rotation describe an approximately 26,000-year orbit around the ecliptic pole.

precession of the equinox: combination of the precession of the equator and the precession of the ecliptic.

precision: a measure of the tendency of a set of random numbers to cluster about a number determined by the set.

prograde annual wobble: the component of polar motion of the Earth with a period of one year.

prograde semiannual wobble: the component of polar motion of the Earth with a period of one half a year.

proper motion: the projection onto the celestial sphere of the space motion of a star relative to the solar system; thus, the angular transverse component of the space motion of a star with respect to the solar system. Proper motion is usually tabulated in star catalogs as changes in right ascension and declination per year or century.

proper time: time measured along the trajectory of an observer in space-time and invariant in any coordinate change.

pulsar: highly magnetized rotating neutron star that is observed to emit periodically a beam of radio waves with a period ranging between $1 . 5 ~ \mathrm { m s }$ and $8 . 5 \mathrm { ~ s ~ }$ .

quality factor (Q): the quality factor for oscillating systems is defined as the ratio of total energy in a system to the energy lost per cycle. Also, the ratio that provides an indication of the sharpness of the peak of a resonance curve.

quantum logic clock: a frequency standard based on optical frequencies produced by energy-level transitions in single ions.

quartz crystal clock: a clock based on the use of quartz crystal to regulate the oscillations in an electrical circuit.

radial velocity: the rate of change of the distance to an object.

Ramsey fringe: the sinusoidal fringe pattern in the excited-state population, as a function of detuning from resonance, caused by the interaction between an atomic wave function and a probe, which is transferred between the ground and excited states, depending upon the phase between the excitation field and the atomic oscillation.

random walk frequency noise: variations in frequency that can be described by a succession of random changes.

redshift: change in the frequency of electromagnetic radiation, toward longer wavelengths. Examples are the Doppler effect, as seen in the observed expansion of the universe, and gravitational redshift, which is a relativistic effect in electromagnetic radiation in gravitational fields. The redshift is described by the relative difference between the observed and emitted wavelengths of the radiation, and specified by the dimensionless quantity $\mathbf { Z }$ , where z is determined from $1 + z =$ observed wavelength/emitted wavelength.

refraction, astronomical: the bending of a ray of light as it passes through the Earth’s atmosphere, depending on atmospheric pressure, temperature, humidity, and wavelength.

residuals: the difference between actual observations and theoretical estimates of a variable.

retrograde motion: for orbital motion in the solar system, motion that is clockwise in the orbit as seen from the north pole of the ecliptic; for an object observed on the celestial sphere, motion that is from east to west, resulting from the relative motion of the object and the Earth.

Riefler clock: precision pendulum clock using an invar pendulum in a low-pressure tank.

Riemannian space time: the four-dimensional coordinates of space and time in Riemannian geometry, which is the study of smooth, curved surfaces, as opposed to Euclidean geometry, which is the study of flat spaces.

right ascension: angular distance given either in arc or time units measured eastward along the celestial equator from the equinox, or CIO, to the hour circle passing through the celestial object, usually given in combination with declination.

Sagnac effect: the interference observed in two beams of light sent in opposite directions around a rotating loop, caused by the fact that the pulse sent in the same direction as the rotation of the loop must travel further than the pulse sent in the opposite direction of the rotation.

seasonal hours: hours of variable length due to the seasonal change in the length of daylight.

second, Système International (SI): the duration of 9 192 631 770 cycles of radiation corresponding to the transition between two hyperfine levels of the ground state of caesium 133.

Second Law of Thermodynamics: statement that the total entropy of a closed system increases with time, or remains constant in ideal cases, when the system is in a steady state or undergoing a reversible process.

secular acceleration of the Moon: the acceleration of the mean motion of the Moon due to gravitational perturbations and tidal retardation of Earth rotation.

secular deceleration of Earth: change in the length of the day by about $1 . 7 \mathrm { m s }$ per day per century, due to a combination of lunar tides and glacial isostatic adjustment of portions of the Earth’s crust.

secular polar motion: a non-periodic motion of the Earth’s pole toward the direction of approximately $7 5 ^ { \circ }$ west longitude.

selenocentric: with reference to, or pertaining to, the center of the Moon.

semidiameter: the angle at the observer subtended by the equatorial radius of the Sun, Moon, or a planet.

semimajor axis: half the length of the major axis of an ellipse; a standard element used to describe an elliptical orbit.

Shortt clock: a pendulum clock in which a “slave pendulum” performs the mechanical work such as turning the hands of the clock, opening and closing contacts, and giving impulses to the master pendulum, thus leaving the master pendulum free of most perturbations.

sidereal day: the interval of time between two consecutive transits of the equinox.

sidereal hour angle: angular distance measured westward along the celestial equator from the catalog equinox to the hour circle passing through the celestial object. It is equal to $3 6 0 ^ { \circ }$ minus the right ascension in degrees.

sidereal time: the measure of time defined by the apparent diurnal motion of the catalog equinox; hence, a measure of the rotation of the Earth with respect to the stars rather than the Sun.

signal-to-noise ratio: the ratio between the amplitude of the signal to that of the noise.

Sisyphus cooling: a mechanism for laser cooling of atoms using light forces. The mechanism involves a polarization gradient that introduces non-conservative light forces, which can reduce the average kinetic energy of atoms.

solar time: time based on the rotation of the Earth with respect to the position of the Sun.

solstice: either of the two points on the ecliptic at which the apparent longitude of the Sun is $9 0 ^ { \circ }$ or $2 7 0 ^ { \circ }$ ; also, the time at which the Sun is at either point.

spacetime: the combination of three dimensions of space and a time dimension.

spacetime metric: a chosen specification defining the properties of time and distance in the general theory of relativity.

stability: ability of a standard to maintain its synchronization, or syntonization, over time.   
A stable clock would produce the same measures over a range of time intervals.

standard epoch: a date and time used to specify a reference frame. Prior to 1984, coordinates of star catalogs were commonly referred to the mean equator and equinox of the beginning of a Besselian year. Beginning with 1984, the Julian year has been used, as denoted by the prefix J, e.g., J2000.0.

Stark effect: the shifting and splitting of spectral lines of atoms and molecules due to the presence of an external electric field. The Stark effect is the electric analog of the Zeeman effect, and is responsible for pressure broadening (Stark broadening) of spectral lines by charged particles.

sunrise, sunset: the times at which the apparent upper limb of the Sun is on the astronomical horizon; i.e., when the true zenith distance, referred to the center of the Earth, of the central point of the disk is $9 0 ^ { \circ } 5 0 ^ { \prime }$ , based on adopted values of $3 4 ^ { \prime }$ for horizontal refraction and $1 6 ^ { \prime }$ for the Sun’s semidiameter.

synchronization: the process of setting two standards to read the same time.

synodic period: time taken for an object to reappear at the same point in the sky, relative to the Sun, as observed from Earth.

syntonization: the process of setting two standards to the same frequency.

Teph: the independent time argument of the JPL and MIT/CfA solar-system ephemerides. It differs from Barycentric Coordinate Time (TCB) by an offset and a constant rate. The linear drift between Teph and TCB is such that the rates of Teph and TT are as close as possible for the time span covered by the particular ephemeris. Each ephemeris defines its own version of Teph; the Teph of the JPL ephemeris DE405 is for practical purposes the same as TDB defined earlier.

terminator: the boundary between the illuminated and dark areas of the apparent disk of the Moon, a planet, or a planetary satellite.

Terrestrial Dynamical Time (TDT): timescale for apparent geocentric ephemerides defined by a 1979 IAU resolution and replaced by Terrestrial Time (TT) in 1991.

Terrestrial Ephemeris Origin (TEO): the original name for the Terrestrial Intermediate Origin (TIO) given in the IAU 2000 resolutions.

Terrestrial Intermediate Origin (TIO): origin of longitude in the Intermediate Terrestrial Reference System. It is the nonrotating origin in the ITRS that is recommended by the IAU, where it was originally designated Terrestrial Ephemeris Origin. The name Terrestrial Intermediate Origin was adopted by IAU in 2006. The TIO was originally set at the ITRF origin of longitude and throughout 1900–2100 it stays within 0.1 mas of the ITRF zero meridian.

Terrestrial Intermediate Reference System (TIRS): a geocentric reference system defined by the intermediate equator of the CIP and the TIO. It is related to the ITRS by polar motion and $\mathrm { \mathbf { s } } ^ { \prime }$ (TIO locator). It is related to the Celestial Intermediate Reference System by a rotation of ERA around the CIP, which defines the common $z$ -axis of the two systems.

Terrestrial Time (TT): a coordinate time whose mean rate is close to the mean rate of the proper time of an observer located on the rotating geoid. At 1977 January 1.0 TAI exactly, the value of TT was 1977 January 1.0003725 exactly. It is related to the Geocentric Coordinate Time (TCG) by a conventional linear transformation. An accurate realization of TT is TT $( \mathrm { T A I } ) = \mathrm { T A I } + 3 2 \mathrm { s } . 1 8 4$ . In the past, TT was called Terrestrial Dynamical Time (TDT).

tidal acceleration, tidal deceleration: the rate of slowing of the Earth’s rotation caused by tidal forces between the Moon and the Earth causing a gradual increase of the distance between the Earth and the Moon.

tidal friction: the frictional force caused by the interaction between the tides and the Earth’s surface.

tides, ocean: periodic rise and fall of ocean waters due to the attraction of the Moon and Sun.

tides, solid Earth: periodic rise and fall of areas of the Earth crust due to the attraction of the Moon and Sun.

time dilation: difference of elapsed time between two events as measured by observers moving with respect to each other or being situated in different gravitational fields. In special relativity clocks moving with respect to an inertial system are measured to be running slower. In general relativity clocks at lower potentials in a gravitational field are measured to be running slower.

time variation (TVAR): a statistic used to describe clock noise.

TIO locator (denoted $\mathbf { \boldsymbol { s } } ^ { \prime }$ ): the difference between the ITRS longitude and the instantaneous longitude of the intersection of the ITRS and intermediate equators. The TIO was originally set at the ITRF origin of longitude. As a consequence of polar motion, the TIO moves according to the kinematical property of the nonrotating origin. The TIO is currently located using the quantity $s ^ { \prime }$ , the rate of which is of the order of $5 0 \mu \mathrm { a s } / \mathrm { c y }$ and is due to the current polar motion.

TIO meridian: moving plane passing through the geocenter, the CIP, and the TIO.

topocentric: with reference to, or pertaining to, a point on the surface of the Earth.

transit: the passage of the apparent center of the disk of a celestial object across a meridian; also, the passage of one celestial body in front of another of greater apparent diameter (e.g., the passage of Mercury or Venus across the Sun or Jupiter’s satellites across its disk); however, the passage of the Moon in front of the larger apparent Sun is called an annular eclipse. The passage of a body’s shadow across another body is called a shadow transit; however, the passage of the Moon’s shadow across the Earth is called a solar eclipse.

trapped ions: ions trapped in an electromagnetic field to provide a timing source.

true anomaly: the angle, measured at the focus nearest the pericenter of an elliptical orbit, between the direction of the pericenter and the radius vector from the focus to the orbiting body; one of the standard orbital elements.

true equator and equinox: the celestial coordinate system determined by the instantaneous positions of the celestial equator defined by the Celestial Intermediate Pole and the ecliptic.

twilight: the interval of time preceding sunrise and following sunset during which the sky is partially illuminated. Civil twilight comprises the interval when the zenith distance, referred to the center of the Earth, of the central point of the Sun’s disk is between $9 0 ^ { \circ } 5 0 ^ { \prime }$ and $9 6 ^ { \circ }$ ; nautical twilight comprises the interval from $9 6 ^ { \circ }$ to $1 0 2 ^ { \circ }$ ; astronomical twilight comprises the interval from $1 0 2 ^ { \circ }$ to $1 0 8 ^ { \circ }$ .

umbra: the portion of a shadow cone in which none of the light from an extended light source (ignoring refraction) can be observed.

uniform time scale: a timescale having the same unit of time consistently.

Universal Time (UT): a measure of time that conforms, within a close approximation, to the mean diurnal motion of the Sun and serves as the basis of all civil timekeeping. The term “UT” is used to designate a member of the family of Universal Time scales (e.g., UTC, UT1).

Universal Time (UT1): angle of the Earth’s rotation about the CIP axis defined by its conventional linear relation to the Earth Rotation Angle (ERA). It is related to Greenwich apparent sidereal time through the ERA, and determined by observations. UT1 can be regarded as a time determined by the rotation of the Earth, and can be obtained from the uniform timescale UTC by using the quantity UT1−UTC.

UT1−UTC: difference between the UT1 parameter derived from observations and the uniform time scale UTC, the latter being currently defined as: $\mathrm { U T C } = \mathrm { T A I } + \mathbf { n }$ , where n is an integer number of seconds, such that $| \mathrm { U T 1 - U T C } | < 0 . 9 \mathrm { s }$ .

verge: in a verge and foliot clock, a lever, with projections, which intermittently locks the escape wheel and transmits impulses from the escape wheel to the pendulum.

vernal equinox: the ascending node of the ecliptic on the celestial sphere; also, the time at which the apparent longitude of the Sun is $0 ^ { \circ }$ .

vertical: the apparent direction of gravity at the point of observation (normal to the plane of a free level surface).

week: an arbitrary period of days, usually seven days; approximately equal to the number of days counted between the four phases of the Moon.

white frequency noise: a type of statistical noise observed in the output frequency of a oscillator that has no dependency on sampling frequency.

white phase noise: a type of statistical noise observed in the timing signal of a clock that has no dependency on sampling frequency.

year: a period of time based on the revolution of the Earth around the Sun. The calendar year is the time between two dates with the same designation in a calendar. The tropical year is the period of one complete revolution of the mean longitude of the Sun through $3 6 0 ^ { \circ }$ . The anomalistic year is the mean interval between successive passages of the Earth through perihelion. The sidereal year is the mean period of revolution with respect to the background stars.

year, Besselian: the period of one complete revolution in right ascension of the fictitious mean sun, as defined by Newcomb. The beginning of a Besselian year, traditionally used as a standard epoch, is denoted by the suffix “. $0 ^ { \circ }$ . Since 1984, standard epochs have been defined by the Julian year rather than the Besselian year. For distinction, the beginning of the Besselian year is now identified by the prefix B (e.g., B1950.0).

Zeeman effect: the splitting of a spectral line into several components in the presence of a static magnetic field.

zenith: in general, the point directly overhead on the celestial sphere. The astronomical zenith is the extension to infinity of a plumb line. The geocentric zenith is defined by the line from the center of the Earth through the observer. The geodetic zenith is the normal to the geodetic ellipsoid at the observer’s location.

zenith distance: angular distance measured along the great circle from the zenith to the celestial object. Zenith distance is $9 0 ^ { \circ }$ minus altitude.

zij: a generic name for an Arabic astronomical book that includes tabular parameters for calculating positions of astronomical bodies.

# Index

A.1, 225, 226   
A3, 227   
absolute time, 2   
accuracy, 163   
active hydrogen maser, 190   
Adams, John Couch, 31, 48   
Alfonsine Tables, 27   
alkali, 172, 173, 175, 177, 180, 191   
Allan deviation, 176   
Allan variance, 165, 226   
Almagest, 27, 215   
aluminum, 210   
AM, 227   
ammonia molecule, 177   
analemma, 11   
anchor escapement, 155   
angular momentum of the atom, 173   
annual polar motion, 78   
Apollonius, 26   
apparent sidereal time, 14, 62   
apparent solar time, 10, 11, 21   
Areocentric Coordinate Time (TCA), 275   
Aristarchus, 26   
Aristotle, 26   
artificial satellites, 42   
Aryabhata, 27   
asterisms, 149   
astrodynamics, 42   
astrolabe, 4   
Astronomia Carolina, 30   
astronomical constants, 40, 69   
astronomical latitude, 70, 77   
astronomical regulators, 156   
astronomical time, 62   
astronomical unit, 41   
atmospheric angular momentum, 308   
Atomic Clock Ensemble in Space (ACES),   
197, 292   
atomic clocks, 63, 174, 225, 252

atomic resonator, 176   
atomic second, 95   
atomic time, 96, 97, 99, 101, 131, 132, 133, 135, 142, 143, 181   
Atomichron, 181, 225   
Babbage, Charles, 35   
banking, 339   
barycenter, 68, 70, 131, 132, 133, 134, 136, 137, 139, 142   
Barycentric Celestial Reference System (BCRS), 70, 114, 137   
Barycentric Coordinate Time (TCB), 119, 121, 137, 139, 141, 144   
Barycentric Dynamical Time (TBD), 101, 121, 132, 134, 141, 142, 143   
Barycentric Ephemeris Time, 142   
barycentric gravitational potentials, 118   
barycentric metric, 115   
BCRS, 70, 137. See Barycentric Celestial Reference System   
Beidou (Compass), 270   
beryllium, 210   
Bessel, Friedrich Wilhelm, 3   
Besselian year, 16, 38, 39   
Big Bang, 123   
BIH Terrestrial System, 70   
BIPM, 138. See Bureau Inernational des Poids et Mesures   
black body radiation, 176   
Bradley, James, 3, 33   
Brahe, Tycho, 28, 216   
Brouwer, D., 91, 97, 101   
Brown, Ernest, 33   
Brown’s Lunar Tables, 33   
Brown’s lunar theory, 94   
Brown’s theory, 34   
Bureau International de l’Heure (BIH), 20, 70, 71, 85, 227–228, 252   
Bureau International des Poids et Mesures (BIPM), xiii, 138, 228–246, 316, 318   
caesium, 108, 171, 172, 173, 174, 175, 177, 179, 180, 181, 182, 183, 184, 185, 186, 188, 190, 191, 193, 194, 197, 200, 218, 219, 221, 222, 223, 224   
caesium atomic clock, 171, 180   
caesium beam tube, 181   
caesium fountain, 186, 187, 193   
caesium standards, 193, 225   
calcium, 207, 208   
calendar, 2   
calibration of signal delays, 280   
candles, 150   
carrier Doppler TWSTFT, 291   
carrier phase, 289, 293   
catalog equinox, 38, 95   
cavity pulling, 177   
CCIR, 20, 21. See International Radio Consultative Committee   
CCTF, 223, 224   
Celestial Ephemeris Pole, 72   
Celestial Intermediate Origin, 17, 72, 73, 79, 80, 82   
Celestial Intermediate Pole, 17, 72, 73, 74, 75, 76, 78, 79, 82, 84   
Celestial Intermediate Reference System, 72, 73   
celestial pole offsets, 76   
Celestial Reference Frame, 68   
Celestial Reference System, 68, 82, 136, 294   
cellular phone networks, 336   
CEP. See Celestial Ephemeris Pole   
CGPM, 217, 218, 221, 222   
Chandler Motion, 77, 78   
Chandler wobble, 77   
Chandler, Seth, 7   
characterizing atomic clocks, 198   
chronological eras, 2   
chronometers, 156   
CIO, 17. See Celestial Intermediate Origin   
CIP. See Celestial Intermediate Pole   
CIPM, 217, 218, 221, 222, 223, 224. See International Committee for Weights and Measures   
Circular T, 243   
CIRS. See Celestial Intermediate Reference System   
civil time, 254, 259   
Clemence, G. M., 49, 56, 64, 89, 90, 91, 101   
clepsydra, 149   
clock, 148, 175   
clock transitions, 173   
coaxial cable, 283   
code division multiple access (CDMA), 337   
Comite Consultatif pour la Définition de la Seconde (CCDS), 218, 230   
Comité International des Poids et Mesures (CIPM), 316   
Commission Nationale de l’Heure of France, 227   
communications, 336, 345   
Comrie, L. J., 35

Conférence Générale des Poids et Mesures (CGPM   
316   
Connaissance des Temps, 30   
Consultative Committee for Time and Frequency   
(CCTF), 317   
Consultative Committee for Units (CCU), 317   
Consultative Committees, 317   
Conventional Intermediate Pole,   
295   
coordinate clock comparison, 280   
coordinate time, 107, 108, 111, 122, 133,   
137, 144   
Coordinated Universal Time, 20, 132, 253,   
254   
Copernicus, Nicolaus, 28, 47   
core–mantle boundary, 311   
Coriolis force, 117   
correlator, 299   
cosmic time, 126   
cosmology, 123   
cosmopolitan time, 250   
Coulomb interaction, 210   
Cowell, P. H., 36   
CRTS, 335   
crystal-controlled clocks, 62   
cycloid, 154   
ΔT, 97, 142   
d’Alembert, Jean le Rond, 33   
d’Arrest, Heinrich Louis, 31   
Danjon, André, 89, 91, 92   
daylight saving stime, 21, 22   
de Sitter, W., 55   
DE200, 32   
DE430/LE430, 37   
dead-beat escapement, 155   
decadal irregularities, 59   
decans, 149   
declination, 3   
definition of the second, 181, 229   
Deflection of the Vertical, 71   
Delaunay, Charles-Eugène, 33, 48, 49,   
64   
Delaunay’s method, 33   
distributed clock, 348   
Division A, Fundamental Astronomy,   
319   
Doppler effect, 112, 177, 274, 308   
DORIS, 331   
double-bulb rubidium maser, 194   
DoV. See Deflection of the Vertical   
Dunthorne, Richard, 48, 64   
DUT1, 255, 256   
dynamical equinox, 38, 95   
dynamical equinox of J2000.0, 137   
dynamical time, 11, 91, 131   
dynamical timescale, 40, 89, 131, 132, 133, 134, 1   
143, 347   
Earth orientation, 63, 68, 70, 73, 80, 84, 85   
Earth Orientation Center, 327   
Earth orientation data, 312   
Earth orientation parameters, 296, 299, 301, 302, 304,   
308, 310, 312, 315   
Earth rotation, 7, 34, 47, 48, 49, 50, 51, 52, 53, 55, 56,   
58, 59, 61, 62, 345   
Earth Rotation Angle, 17, 18, 73, 79, 80, 84, 95, 295   
Earth’s magnetic field, 31   
Earth’s potentials, 116   
Earth-fixed, rotating frame, 282   
Echelle Atomic Libre (EAL), 233–242   
Eckert, Wallace, 35   
eclipses, 1, 264   
ecliptic, 2, 3, 69, 75, 82   
Egyptian calendar, 149   
electromagnetic coupling, 59   
electromagnetic signals transfer, 282   
electromagnetic spectrum, 203   
electron angular momentum, 173   
e-LORAN, 335   
emergency service, 339   
energy-level transitions, 172, 175   
Ensemble Pulsar Scale (EPS), 276   
entropy, 128, 129   
ephemerides, 4, 25, 27, 28, 29, 30, 31, 33, 35, 36, 37, 38,   
39, 40, 41, 42, 99, 131, 132, 133, 134, 135, 136, 140,   
141, 142, 143, 263, 264, 265, 266, 267, 268, 275   
ephemeris second, 92, 95, 99, 217   
Ephemeris Time (ET), 40, 63, 88, 91, 92, 93, 94, 96, 97,   
99, 131, 133, 138, 142, 143, 180, 218, 244   
Ephemeris Time Revised $( \mathrm { E T _ { R } } )$ , 143   
epicycles, 26   
EPM 2011, 37   
epoch, 5   
equal hours, 149   
equation of the equinoxes, 14, 80   
equation of the origins, 18, 80   
equation of time, 11   
equator, 3, 4   
equinoctial hours, 6   
equinox, 3, 11, 12, 13, 14, 16, 17, 34, 38, 39, 94   
equinox motion correction, 39   
equivalence principle, 113   
ERA, 17. See Earth Rotation Angle   
EROS, 335   
Essen, Louis, 171, 172, 179, 180, 225   
ET, 131, 133, 134, 139, 142, 143, 145. See Ephemeris   
Time   
Euler, Leonhard, 7, 32   
extended linear ion trap (LITE), 197   
Ferrel, William, 48, 49, 64   
fictitious mean Sun, 10, 18,   
19, 39   
finance, 339   
FK4 star catalog, 95, 101   
FK5, 4, 17, 38, 73   
FK5 star catalog, 95   
Flamsteed, John, 32, 47   
flicker frequency noise, 165   
flicker phase noise, 165   
foliot regulator, 151   
Foucault, Léon, 47   
fractional frequency measurement, 176   
frame bias, 72   
free core nutation, 72, 75, 312   
free-falling laboratory, 113   
frequency accuracy, 226   
frequency comb technology, 284   
frequency combs, 203   
frequency division multiple access (FDMA), 337   
frequency stability, 226   
Frequency Standards Working Group, 223, 224   
Friedman-Lemaître-Robertson-Walker metric, 123   
Fromanteel, Johannes, 155   
future clocks, 346   
future timescales, 346

Gaia, 39   
Galilean principle of relativity, 105   
Galileo, 47, 152   
GALILEO, 270, 289   
Galle, Johannes Gottfried, 31   
Gauss, Carl Friedrich, 30   
Gaussian constant, 41   
GCRS, 17, 137. See Geocentric Celestial Reference System   
GCT, 13, 21   
general four-dimensional metric, 113   
general precession, 82   
general relativity, 112, 114, 133   
general theories, 29   
Geocentric Celestial Reference System (GCRS), 17, 70, 72, 73, 75, 76, 79, 115, 118, 137, 280   
Geocentric Coordinate Time (TCG), 119, 121, 137, 139, 143, 280   
geocentric ephemeris, 133   
geocentric metric, 115   
geocentric system, 27   
Geocentric Terrestrial Reference System, 280   
geodesic, 114   
geodesic precession, 70   
geoid, 71, 212   
geomagnetic jerks, 312   
geophysical modeling, 308   
glacial isostatic adjustment, 59   
Global Geophysical Fluids Center, 328   
Global Navigation Satellite System (GLONASS), 270, 289   
Global Navigation Satellite Systems (GNSS), 334   
Global Positioning System (GPS), 17, 71, 85, 171, 233, 270, 289, 302   
GMAT, 13, 21. See Greenwich Mean Astronomical Time   
GMST, 16. See Greenwich Mean Sidereal Time   
GMT, 13, 21. See Greenwich Mean Time   
GPS Time, 289   
Graham, George, 155   
gravitational constant, 31   
gravitational mass, 113   
gravitational redshift, 273   
gravity vector, 70   
great empirical term, 4, 34, 55, 94   
Greenwich apparent solar time, 10   
Greenwich Atomic, 225   
Greenwich Civil Time (GCT), 13, 21, 252   
Greenwich Mean Astronomical Time, 13, 21, 252   
Greenwich Mean Civil Time, 6   
Greenwich Mean Sidereal Time, 18, 73, 80   
Greenwich Mean Solar Time, 13, 252   
Greenwich Mean Time, 6, 12, 13, 21, 249, 252   
Greenwich meridian, 10, 12, 15, 21, 69, 73, 249   
Greenwich Sidereal Time, 14, 73, 80   
Gregorian calendar, 2   
group delay, 300   
GST, 80. See Greenwich Sidereal Time

H4, 156   
Hadamard Variance, 168   
Halley, Edmond, 3, 29, 30, 47   
Handy Tables, 27   
Hansen, Peter, 33   
harmonic coordinates, 115   
Harrison, John, 5, 156   
Heisenberg uncertainty principle, 173   
heliacal rising, 149   
heliocentric system, 28   
Henderson, Thomas, 3   
Herschel, William, 3, 30   
Hevelius, Johannes, 153   
high-frequency radio signals, 285   
Hill, G. W., 31, 33   
Hipparchus, 3, 6, 26, 32   
Hipparcos Catalogue, 39, 70   
horologium, 148   
hours, 149   
Hubble Constant, 124, 129   
Hubble’s Law, 124   
Huygens, Christiaan, 152   
hydrogen, 173, 175, 177, 178, 189, 190, 191, 194, 198,   
200, 202   
hydrogen masers, 189   
IAU 1976 System of Astronomical Constants, 17   
IAU 1976/1980 precession/nutation model, 76   
IAU 1980 Theory of Nutation, 69, 72   
IAU 2000A precession-nutation model, 72, 76   
IAU Resolutions, 114   
IBM Selective Sequence Electronic Calculator,   
35

ICRF. See International Celestial Reference Frame   
ICRS, 17. See International Celestial Reference System   
IERS. See International Earth Rotation and Reference Systems Service   
IERS conventional models, 328   
IERS Rapid Service/Prediction Center, 327   
Improved Lunar Ephemeris, 33, 94   
improvement in timekeeping accuracy with time, 163   
incense sticks, 150   
inertia tensor, 78, 80, 81   
inertial ecliptic, 39   
inertial mass, 113   
inertial reference frame, 104, 114   
Innes, R. T. A., 52, 53   
INPOP13b, 37   
instability in atomic clocks, 176   
intelligent transportation systems, 335   
International Astronomical Union (IAU), 131, 132, 134, 136, 137, 140, 141, 228, 232, 244, 245, 319   
International Atomic Time (TAI), 96, 121, 131, 132, 246   
International Celestial Reference Frame, 70   
International Celestial Reference System (ICRS), 39, 70, 72, 73, 85, 328   
International Committee for Weights and Measures, 20, 228   
International DORIS Service (IDS), 326, 331   
International Earth Rotation and Reference System Service (IERS), 21, 39, 68, 73, 85, 326   
International GNSS Service (IGS), 326, 330   
International Laser Ranging Service (ILRS), 326, 329   
International Latitude Service (ILS), 7   
International Meridian Conference, 15, 21, 251   
International Radio Consultative Committee (CCIR), 20, 228, 323   
International Telecommunication Regulations, 324   
International Telecommunications Union, 228, 322   
International Terrestrial Reference Frame, 71, 73, 308   
International Terrestrial Reference System (ITRS), 17, 39, 71, 72, 73, 79, 85, 328   
International Union of Geodesy and Geophysics (IUGG), 321   
International Union of Radio Sciences, 20, 228   
International VLBI Service, 320, 326, 329, 332, 333   
Internet, 285   
iodine, 211   
ionosphere, 299   
Islamic prayer times, 340   
ITRF 2014, 308   
ITRS, See International Terrestrial Reference System   
ITU-R, 324   
J2000.0, 38   
Jewish Sabbath, 340

Julian date, 17

Julian day numbers, 6   
Julian year, 38   
Kant, Immanuel, 48   
Kepler, Johannes, 26, 28, 29, 30   
Kepler’s laws, 4, 28   
LAGEOS, 305   
Lalande, Jérôme, 30, 48   
Lambda-Cold Dark Matter, 125   
Laplace, Pierre-Simon, 33, 48   
Large Synoptic Survey Telescope (LSST), 335   
Laser-cooled linear ion trap, 197   
laser ranging, 269   
law of universal gravitation, 4   
LCT, 13. See local civil time   
leap second, 19, 255, 257, 347   
least-squares, 31, 36   
length of day, 56, 59, 65, 97, 302   
Lense-Thirring effect, 118   
LeVerrier, Urbain Jean Joseph, 31   
librations of the Moon, 33   
light cones, 109   
limb corrections, 94   
Linear Ion Trap Frequency Standard (LITS), 197   
Liouville equation, 81   
local apparent solar time, 10   
local civil time, 13   
local inertial reference frame, 114   
local mean solar time, 16   
local sidereal time, 14   
longcase clocks, 155   
LORAN, 227, 270, 335   
LORAN-C, 227   
Lorentz transformation, 100, 106, 110   
low-frequency radio signals, 286   
lunar distance method, 32   
lunar eclipses, 264   
lunar ephemeris, 32, 94   
lunar laser ranging, 37, 97   
lunar occultations, 265   
lunar secular acceleration, 34   
lunar tables, 32   
lunar theories, 4, 31, 32, 33, 34   
lunar tides, 59   
Lyons, Harold, 177, 178   
MACHO, 335   
Markowitz wobble, 296   
Markowitz, William, 93, 95, 102, 181   
Mars Time, 274   
Martian proper time, 348   
Mayer, Julius Robert, 58   
Mayer, Tobias, 29, 30, 33, 48   
mean equator of J2000.0, 136   
mean equinox, 14   
mean longitude of the Sun, 217   
mean pole, 78   
mean sidereal time, 14   
mean solar day, 251   
mean solar second, 91, 96   
mean solar time, 10, 11, 12, 14, 15, 16, 17, 18, 21, 38,   
40, 90, 91, 95, 252   
mean solar time at Greenwich, 18   
mean sun, 10   
mean, bias, and standard deviation, 164   
mechanical clock, 5, 6, 150   
mercury, 173, 195, 196, 197, 199, 202, 207, 210   
meter definition, 268   
metric tensor, 115, 119   
Michelson, 105   
microcomputer-controlled crystal oscillators (MCXO),   
171   
micromotion, 195   
microwave frequencies, 203   
microwave links, 284   
microwave spectroscopy, 177   
Minkowski diagram, 109   
Minkowski metric, 107   
minute, 216, 217   
mode-locked lasers, 203   
moment of inertia, 58   
month, 2   
Moon, 1, 2, 3, 4, 5, 7   
Moon Camera, 221   
Moon’s motion, 47, 48, 53   
Moonrise, 266   
Moonset, 266   
multiplexing, 336   
multipole moments, 119   
N30 catalog, 38   
national observatories, 3   
National Physical Laboratory, 225, 227, 238, 239   
National Research Laboratory of Canada, 227   
Nautical Almanac, 30, 249   
navigate indoors, 344   
navigation, 5   
navigation satellite broadcast signals, 288   
NBS-A, 226   
Neptune, 31   
Network Time Protocol (NTP), 285, 338   
Newcomb, Simon, 7, 8, 11, 18, 31, 33, 34, 38, 39, 40,   
49, 50, 52, 55   
Newcomb’s constants, 4   
Newcomb’s Tables of the Sun, 92   
Newton, Isaac, 2, 26, 28, 29, 30, 31, 32, 45, 47   
Newton’s law of gravitation, 29   
Newtonian gravitational constant, 41   
Newtonian gravitational theory, 104   
Newtonian mechanics, 104, 112, 131   
Newtonian potential, 113   
Newtonian time, 52, 89, 90   
Newtonian universal law of gravity, 104   
noise, 165   
non-rigid Earth, 7

# Index

nonrotating local inertial frame, 283   
nonrotating local inertial reference frame, 282   
nonrotating origin, 17   
NPL caesium frequency standard, 225   
numerical integration, 25, 31, 34, 35, 36, 40, 99   
numerically integrated ephemerides, 32   
nutation, 3, 14, 69, 70, 72, 73, 74, 75, 80, 81, 82, 84, 85   
Observatoire de Neuchâtel, 226, 227   
Observatoire de Paris, 227, 239   
occultation, 34, 56, 93, 264   
ocean angular momentum, 310   
OGLE, 335   
optical atomic clocks, 223   
optical clock, 205   
optical clock technology, 346   
optical detection, 183   
optical fiber, 283, 348   
optical ion clocks, 207   
optical lattice, 203, 208, 209, 211, 212, 213, 214   
optical neutral atom clocks, 208   
optical pumping, 183, 196   
optical transition frequencies, 203   
optical TWTFT, 291   
optically pumped caesium beam tube, 185   
oven-controlled crystal oscillators (OCXO), 171   
Pan-STARRS, 335   
parallaxes, 4   
parameterized post Newtonian (PPN), 42, 100   
Parkes Pulsar Timing Array (PPTA), 276   
Parry, J. V. L., 179   
passive hydrogen maser, 191   
Paul trap, 194, 207, 210   
pendulum clock, 5, 8, 152   
Penning trap, 194   
perihelion of mercury, 31   
PHARAO, 197, 292   
phase delay, 300   
Photographic Zenith Tube (PZT), 219   
Physikalische Technische Bundesanstalt, 227   
piezoelectricity, 159   
planetary ephemerides, 32   
planetary precession, 82   
polar motion, 7, 72, 73, 74, 76, 78, 81, 84, 85, 294, 295,   
296, 301, 302, 303, 304, 308, 310   
portable clock, 234, 281   
post-Newtonian potential coefficients, 118   
power grids, 338   
power spectrum of clock noise, 165   
precession, 3, 14, 17, 69, 70, 72, 73, 74, 75, 80, 81, 82,   
84, 85, 267   
precession/nutation, 294   
precision, 162   
Prime Meridian, 71   
propagation effects, 279   
proper motion, 3   
proper time, 107, 108, 133, 137, 144   
Prutenic Tables, 28   
Ptolemy, 3, 6, 26, 40, 215   
pulsar-based timescale, 276   
pulsars, 128, 275, 346   
punched card equipment, 35   
Quality (Q) Factor, 161   
quantum entanglement, 348   
quantum logic clock, 210   
quartz crystal clocks, 63, 157, 252   
quartz-crystal oscillators, 171   
quasars, 296   
Rabi, Isaac, 172, 178   
radar, 31, 36, 39   
radar ranging, 269   
Radio Regulations, 324   
radio telescopes, 297   
Radiocommunication (ITU-R), 323   
Ramsey, Norman, 178   
random walk frequency noise, 165   
redefinition of the second, 223, 347   
reference frame, 3   
reference system, 4   
refraction, 4   
Regiomontanus, 27   
relativistic aspects of TAI, 234   
relativistic effects, 280   
relativistic effects for the fiber, 281   
relativistic time comparisons, 281   
relativity, 31, 41, 42   
Riefler escapement, 156   
Riefler, Siegmund, 156   
Riemannian space time, 112   
right ascension, 3   
right ascension of the fictitious mean Sun, 18   
rotating ecliptic, 39   
rotating reference frame, 281   
rotation of the Earth, 294   
rotation time, 52   
Royal Greenwich Observatory, 32, 225, 227   
rubidium, 172, 173, 175, 191, 192, 193, 194, 199, 211   
rubidium cell clocks, 192   
rubidium fountains, 193   
Rudolphine Tables, 28   
Sagnac delay, 273   
sand clock, 5   
sandglasses, 217   
satellite laser ranging (SLR), 304   
seasonal hours, 6, 149   
seasonal station displacements, 310   
second, 215, 216, 217, 218, 219, 221, 222, 223, 224   
secular acceleration, 32, 33   
secular acceleration of the Moon, 4, 7, 48, 58   
self-driving cars, 336   
sexagesimal system, 149, 215   
Shortt clock, 158   
Shortt, William, 156   
shuttle trap, 197   
SI. See Système International   
SI ampere, 222   
SI base units, 223   
SI candela, 222   
SI meter, 222   
SI second, 95, 134, 137, 218, 221, 245, 255   
sidereal day, 14   
sidereal time, 13, 14, 16   
sidereal year, 91   
Sisyphus effect, 186   
solar eclipse, 264   
solar mass parameter, 41, 42   
solar system, 262   
solar time, 7   
SONET, 337   
space coordinates, 107   
space-time, 109, 114   
space-time coordinates, 136   
special relativity, 104, 111, 112, 114   
special relativity metric, 113   
spectral densities, 165   
speed of light, 268   
Spencer Jones, H., 53, 54, 55, 56, 57, 58, 59, 90, 91,   
94, 102   
stability, 163   
stability of TAI, 242   
Standard Model, 123   
statistical uncertainty, 234   
stellar aberration, 3   
Stepped Atomic Time, 254   
stratum levels, 337, 338   
stratum level definitions, 337   
Streete, Thomas, 30   
strontium, 207, 208   
von Struve, Friedrich Georg Wilhelm, 3   
subdaily EOP, 304   
Sun, 1, 2, 3, 4, 5, 8   
sundials, 4, 6   
sunrises, 266   
sunsets, 266   
synchronization, 160   
Synchronization Interface Standards for Digital   
Networks, 337   
syntonization, 160   
systematic uncertainty, 234   
Système International, 107, 135, 228,   
232   
Système international d’unités (SI), 316   
Tables of Toledo, 27   
TAI, 132, 133, 134, 135, 138, 139, 141, 142,

143, 253, 255. See International Atomic Time TAI second, 134 TAI, distribution of, 242 TAI, steering of, 240–242

TCB, 139, 140, 141, 142, 143, 144. See Barycentric Coordinate Time   
TCG, 137, 139, 140, 141, 142, 143, 144, 245. See Geocentric Coordinate Time   
TDB, 134, 135, 141, 142, 143. See Barycentric Dynamical Time   
TDT, 134, 135, 142, 143, 145. See Terrestrial Dynamical Time   
telegraph, 6, 278   
telephone, 283   
television broadcast, 285   
temperature-compensated crystal oscillators (TCXO), 171   
Teph, 121, 141, 142. See Barycentric Ephemeris Time   
Terrestrial Dynamical Time (TDT), 101, 132, 134   
Terrestrial Intermediate Origin (TIO), 17, 73, 79   
Terrestrial Intermediate Reference System, 73   
Terrestrial Reference Frame, 68, 70, 71   
Terrestrial Reference System, 68, 69, 72, 81, 294   
Terrestrial Time (TT), 121, 138, 140, 141, 142, 143, 145, 243–246, 280   
theory of relativity, 100   
Thomson, William (Lord Kelvin), 49, 58   
thorium, 208   
THz frequency reference transfer, 284   
tidal deceleration, 49, 50, 55   
tidal friction, 4, 33, 58   
tidal potential, 117   
tidal secular acceleration, 94   
Timation system, 270   
time ball, 6, 278   
time dilation, 106, 108, 109, 111, 112, 114, 273   
time dissemination systems, 278   
time division multiple access (TDMA). 336   
Time Domain Astronomy (TDA), 335   
time ephemeris, 140   
time transfer, 6, 122   
time variation, 168   
time zones, 22   
Time’s Arrow, 128   
Time-division-multiplexing (TDM), 336   
TIO, 17. See Terrestrial Intermediate Origin   
total solar eclipse, 95   
transit circle observations, 36   
transit circles, 93   
transition frequencies, 175   
transits, 264   
transportation methods, 344   
trapped ion clocks, 194   
trapped ionized atoms, 196   
Treaty of the Meter, 316   
Tropic of Cancer, 267   
Tropic of Capricorn, 267   
tropical year, 38, 39, 91, 92, 267, 277   
true equinox, 14   
TT(BIPM), 139

# Index

# Two-Way Satellite Time and Frequency Transfer (TWSTFT), 233, 290

US National Bureau of Standards, 226, 227   
US Naval Observatory, 225, 227   
US Signal Service, 7   
uniform time, 2, 88, 263   
uniform timescale, 132   
uniformity, 263   
units of time, 216   
universal constant of gravity, 113   
Universal Day, 15   
Universal Time, 11, 13, 15, 16, 17, 20, 21, 90, 91, 93, 95, 99, 249, 252   
universe, 123, 124, 125, 126, 127, 128, 129   
Uranus, 30   
URSI, 20. See International Union of Radio Science   
UT, 13, 15, 16, 20, 21. See Universal Time   
UT0, 16, 21, 252   
UT0-UTC, 70   
UT1, 15, 16, 17, 21, 70, 71, 72, 74, 79, 80, 84, 85, 252   
UT1−UTC, 70, 71, 74, 79, 80, 85   
UT2, 16, 20, 21, 252   
UTC, 20, 21, 255, 257. See Coordinated Universal Time

variable rotation of the Earth, 4   
velocity of light, 105

verge escapement, 151, 154   
vernal equinox, 68, 69, 73   
vertical, 70, 71   
Very Long Baseline Array (VLBA), 301   
Very Long Baseline Interferometry (VLBI), 17, 21, 296   
VLBI, 17. See Very Long Baseline Interferometry   
VLBI observations, 97   
VSOP 2013 analytical theory, 18

water clock, 5   
water utilities, 339   
Watts, C. B., 94   
weak equivalence principle, 113   
Weltzeit, 21   
WGS 84, 71   
white dwarf stars, 276, 346   
white frequency noise, 165   
white phase noise, 165   
Working Party 7A (WP 7A), 325   
world line, 107, 109   
year, 2   
ytterbium, 207, 208   
Zeeman effect, 173   
zij, 27