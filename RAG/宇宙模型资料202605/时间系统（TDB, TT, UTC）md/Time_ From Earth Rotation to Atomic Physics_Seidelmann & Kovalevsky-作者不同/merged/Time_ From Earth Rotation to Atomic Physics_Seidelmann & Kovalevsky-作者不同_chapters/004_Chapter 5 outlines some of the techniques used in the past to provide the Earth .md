Chapter 5 outlines some of the techniques used in the past to provide the Earth orientation data. These have included visual and photographic telescopic observations, Doppler observations of artificial satellites, laser ranging to the Moon and artificial satellites, very long baseline interferometry, and analysis of the orbits of navigational satellites. A solution of Earth orientation parameters based on optical astrometry demonstrated the 28-year “Markowitz wobble” and an apparent 78-year period in polar motion (Vondrak et al., 2009). Not all of those techniques continue to be used. A variety of high-precision techniques are used currently to relate the CRS and the TRS and to make predictions of future Earth orientation. These are discussed in what follows.

![](images/365c8a01d6f40a4acd645b5ea85d5b2cf46be4c926e1de3306e9b08186126e58.jpg)  
Figure 18.1 The concept of VLBI used to monitor the Earth orientation parameters

# 18.2.1 Very Long Baseline Interferometry (VLBI)

The VLBI technique makes use of multiple radio telescopes observing very distant radio sources to determine the Earth’s orientation with respect to the celestial reference frame realized by the conventionally adopted radio source positions. The baselines defined by the vectors between the positions of the telescopes, rigidly attached to the Earth’s surface, are defined in the terrestrial frame (Altamimi et al., 2016). The radio sources are quasi-stellar radio sources, quasars, which are powerful radio emitters located at such great distances from the Earth that they can be considered to show minimal space motion. Monitoring of the changing aspect of the baseline vectors with respect to these sources provides the Earth orientation parameters required to implement the mathematical relationship shown in Equation (18.1) (see Johnston, 1979). The concept is shown in Figure 18.1.

![](images/dae39de2927d44b68e96291158c6de1560f1a717c47988a0a0472bd53e0295c0.jpg)  
Figure 18.2 Twin VLBI telescopes at Wetzel, Germany by permission of Wetzel Observatory

Quasars are thought to be the centers of some distant galaxies, probably with massive black holes at the center. Those that appear to be the most “point-like” with minimal observed space motion and variations in observed signal intensity form a group that defines the International Celestial Reference Frame (ICRF) (Fey et al., 2009). These objects broadcast strong radio signals composed essentially of random noise.

The radio telescopes used to monitor the signals have diameters on the order of tens of meters and are located at continental distances to provide a better representation of the global Earth orientation and better resolution of the radio sources themselves. Their positions are well determined and provide part of the definition of the International Terrestrial Reference Frame. Figure 18.2 shows the telescope located at Wetzel, Germany. Figure 18.3 shows the worldwide distribution of the antennas currently in use in geodetic VLBI operations and those sites used in the past for such operations. The operations are organized through the International VLBI Service for Geodesy and Astronomy (IVS). (See Chapter 19.)

Observations are made by multiple telescopes observing quasars widely distributed over the sky in order to determine all of the Earth orientation parameters with the best precision. Because the telescopes are located at different distances from the radio sources, differences occur in the times of arrival of the signals at each telescope. Each site uses a hydrogen maser that serves as a clock to measure precisely the difference in the arrival times. The digitized signals and the times are then sent to a correlator, where the signals are analyzed to determine the delays and the rate of change of the delays among the telescopes involved in the observation. The development of high-speed data transfer networks permits near real-time data transfer, without the necessity of recording the data on electronic media that have to be shipped to the correlator (Carter & Robertson, 1986; Carter et al., 1989).

![](images/cd8416ebf999b6e43b0afb2c58f29282c49f8d4feb451255d0c7a496507fb3ec.jpg)

![](images/957175830614ab4fda934cb35d20793aaed1ddb892b087d9019a6aae429bf2d4.jpg)  
Figure 18.4 VLBI process

At the correlator, the estimated delays can be calculated using the known positions of the telescopes and quasars and a priori estimates of the Earth orientation parameters. This information is used to determine the actual delays and delay rates, which can then be analyzed to determine the corrections to the a priori estimates of the Earth’s orientation. Figure 18.4 outlines the process graphically. Observations are typically made at frequencies of S band $( 2 . 3 ~ \mathrm { G H z } )$ and X band $( 8 . 4 \mathrm { G H z } )$ in order to take advantage of the dispersive nature of the ionosphere and calculate the delays due to the total electron content (TEC) in the ionosphere. This delay, τionosphere, depends on the frequency of the signal, $f ,$ and is proportional to the TEC and inversely proportional to $f ^ { 2 }$ .

![](images/cfcf30e0e26f9c0a863be4ec3402e8a313844679b8dabe328b2cbce8cd35d9af.jpg)  
Figure 18.5 Mathematical representation of VLBI delay

$$
\tau _ { \mathrm { i o n o s p h e r e } } \propto \frac { T E C } { f ^ { 2 } } .
$$

Two general types of delay measurements are possible using VLBI: group delay and phase delay. If $\varphi$ is the measured difference in phase (in radians) between the signals at the two telescopes, the phase delay is given by:

$$
\tau _ { \mathrm { p } } = - \frac { \varphi ( \omega ) } { \omega } ,
$$

and the group delay is given by:

$$
\tau _ { \mathrm { g } } = - \frac { d \varphi ( \omega ) } { d \omega } .
$$

Phase delays can be measured with precisions of a picosecond or better, but with an unknown integer number of phase cycles, which are 451 ps at S band and 122 ps at X band. Group delays can be measured with precisions of a few picoseconds without cycle ambiguities and these are the measures typically used in geodetic VLBI observations.

Mathematically, referring to Figure 18.5, where $\vec { \bf B }$ and $\vec { \mathbf { s } }$ are the baseline vector and unit vector in the direction of the source, respectively, the delay can be expressed as:

$$
\tau = \frac { \vec { \mathbf { B } } ^ { \bullet } \vec { \mathbf { s } } } { c } = \frac { | \mathbf { B } | | \mathbf { s } | \cos \theta } { c } ,
$$

where $c$ is the speed of light and $\theta$ is the angle between $\vec { \bf B }$ and $\vec { \mathbf { s } } .$ . The station coordinates used to create $\bar { \mathbf { B } }$ must be corrected for tectonic plate motion, the tides, and the loading of the site by the atmosphere and possibly nearby oceans. $\vec { \mathbf { s } }$ is computed using the conventionally adopted precession/nutation and the a priori Earth orientation estimates. Observational estimates of $\tau$ must be corrected for atmospheric and ionospheric delays as well as the delays caused by the gravitational attraction of solar system bodies along the path of the signal. The observations themselves are used to calculate the atmospheric and ionospheric effects.

Observations can be affected by instrumental errors, propagation modeling errors, and the fact that the sources may exhibit some extended structure. The instrumental errors include possible deformation of the structure due to temperature and wind loading and possible clock errors. The delay caused by the neutral atmosphere depends on temperature, pressure, and humidity along the path of the signal, and can vary significantly with direction and time at the observing site. Sources are chosen to be used in the observations with concern for any evidence of motion or extended structure. Only the most “point-like” are used to mitigate issues regarding source structure. The strategy for weighting observations has been investigated and improved solutions can be achieved, but automated VLBI analysis is difficult and user attention appears desirable (Wielgosz et al., 2016).

VLBI precision allows analysts to determine the relative distances between the telescopes to a few millimeters and the positions of the radio sources to fractions of a milliarcsecond. Because the telescopes are fixed rigidly in the terrestrial reference frame, the variations in the observed delays provide the information necessary to determine the orientation of the baseline in the celestial frame. From these data corrections to the a priori estimates of $x , y , U T I - U T C , X ,$ and $Y$ can be derived. The VLBI operations and analyses are coordinated internationally through the IVS (see Chapter 19) (Schlüter & Behrend, 2007) (http://ivscc.gsfc.nasa.gov/).

The CONT11 observing campaign, carried out between September 15 and 29, 2011, with 14 globally distributed VLBI stations, produced estimates of Earth orientation parameters (EOP) with rms differences of about $\pm 3 1 \mu \mathrm { a s }$ in polar motion and $\pm 7 ~ \mu \mathrm { s }$ in length of day (Nillsson et al., 2014), compared with Global Navigation Satellite Systems (see Section 18.2.2) data.

The Very Long Baseline Array (VLBA) is a network of 25-meter-diameter radio telescopes in North America, Hawaii, and Saint Croix. In 1997, Research and Development with VLBA (RDV) sessions were begun. These are a joint effort between NASA Goddard Spaceflight Center, the US Naval Observatory (USNO), and the National Radio Astronomy Observatory (NRAO) using the 10 VLBA antennas and 4–10 geodesy network antennas. Since January 2012, daily USNO/ NRAO UT1 40-minute sessions using Pietown and VLBA antennas have been conducted. The UT1 precision averages ${ \sim } 2 9 \mu \mathrm { s }$ with a median of ${ \sim } 2 1 \ \mu \mathbf { s } .$ . The daily IVS UT1 sessions achieve $1 3 ~ { \mu \mathrm { s } }$ mean and $1 1 ~ \mu \ s$ median. The lower precision of the prior sessions is due to the shorter baselines, but they provide rapid and independent UT1 measurements (Gordon, 2016). VLBI data can be used to determine the sub-daily terms in the tidal model at the level of $2 { \ - } 4 \mu \mathrm { a s }$ for polar motion and $0 . 2 \mathrm { - } 0 . 4 ~ \mu \mathrm { s }$ for UT1 (Panafidina et al., 2012).

![](images/a549e5c4b09415da89c97603b7ac80cc9a50f24d319c7d9004759454b5bed4fe.jpg)  
Figure 18.6 The concept of GPS used to monitor the Earth orientation parameters

The VLBI 2010 technology involves upgrading to next-generation VLBI stations around the world with fast slewing antennas, broadband observing systems, and a software correlator. The goals are $1 \mathrm { m m }$ position accuracy on global scales, continuous measurements of time series of station positions and Earth orientation parameters, and turnaround times of less than 24 hours (Petrachenko et al., 2013).

# 18.2.2 Global Positioning System (GPS)

Although VLBI is the only technique that provides all five of the Earth orientation parameters, GPS now provides the most accurate information regarding the polar motion portion $( x , y )$ of the Earth orientation parameters. Monitor stations, with locations well known with respect to the terrestrial reference system, receive signals from the satellites. This information is used to determine the precise orbits of the satellite in an inertial system. As part of the process, the polar motion parameters can be derived by relating the satellite positions with the locations of the monitor stations. (See Figure 18.6.)

The satellites orbit the Earth in planes that rotate in space. The motion of the planes cannot be separated strictly from variations in the Earth’s rotation. Consequently, GPS cannot be used to provide accurate UT1−UTC without some form of a priori knowledge of that part of the rotation of the planes that is independent of the Earth’s rotation. The daily rate of UT1−UTC is equivalent to the excess length of day (LOD), and this can be estimated. By integrating the LOD time series for relatively short periods of time it is possible to determine a UT1 −UTC time series if an accurate integration constant can be determined using VLBI observations.

The determination of the satellite orbits requires accurate knowledge of the Earth’s gravitational field, including any time variations. While the orbits are sensitive to the Earth’s center of mass, they are relatively insensitive to elements of the celestial reference system. As a result, the GPS orbits can provide no information regarding the celestial pole offsets, $X$ and $Y .$

![](images/763d37257be5f0e51e74b345b0b14eecf83c316519709bcbdbe3234e89510611.jpg)  
Figure 18.7 The GPS constellation of satellites. University of Colorado Boulder.

The constellation of GPS satellites is shown in Figure 18.7. It is composed nominally of a set of six orbital planes with inclinations of 55 degrees, each being populated with four satellites. The satellites orbit at an altitude of $2 0 { , } 2 0 0 \ \mathrm { k m }$ . In reality, more than 24 satellites are in orbit at any one time in order to ensure continuous operation of the system. GPS is one of a set of operational, or proposed, navigational satellite systems, but it is currently the only one that has been used operationally to provide reliable Earth orientation information.

The observations that are analyzed for Earth orientation information are coordinated by the International Global Navigation Satellite Services (GNSS) Service (IGS). (See Chapter 19.) The observing network consists of more than 500 sites around the world.

The accuracy of the polar motion observations is made possible by tracking the phase of the signals broadcast from the satellites. Currently, the GPS satellites make use of a number of L-band frequencies, but all GPS satellites broadcast signals at 1.227 and $1 . 5 7 5 \ : \mathrm { G H z }$ . These are modulated by a pseudo-random noise code. Most of the ionospheric delay in the reception of the signals can be eliminated by using the two frequencies, just as in the case of the analysis of the VLBI observations. Tracking the phase of the carrier signal provides no information regarding the time of transmission. That information is only provided by the code. Carrier-phase measurements are differences in carrier phase cycles and fractions of cycles over time. The carrier phase data and code information gathered from the observing sites shown in Figure 18.8 are used by the analysis centers of the

IGS to derive ionospheric maps, orbits of the satellites, and Earth orientation information, as well as to maintain a precise terrestrial reference frame.

The accuracy of the results depends on the accuracy of various physical models used in the orbital analyses. These include models of the tropospheric delays, geopotential, solid Earth tides, ocean tides, ocean and atmospheric loading at the observing sites, solar pressure, atmospheric drag, relativistic effects, and Earth albedo (Rothacher, 1999; Kouba et al., 2000). GPS observations can be particularly useful for investigating sub-daily changes in Earth orientation parameters (Panafidina et al., 2012).

# 18.2.3 Satellite Laser Ranging (SLR)

Satellite laser ranging is a technique that uses a network of special-purpose telescopes to measure the travel times of very short laser light pulses to and from a set of artificial Earth satellites equipped with laser retro reflectors. Just as in the case of the GPS analyses, these data are used to relate the orbits of the satellites determined in inertial space to a terrestrial reference frame defined by the accurate locations of the telescopes that contribute their observations. The concept is shown in Figure 18.8. These observations, like the GPS observations, are only used to provide polar motion and length of day observations. They also are important for the definition of the Earth’s gravitational field model.

Typically, pulses of light with wavelengths of 532 nanometers (nm) (green) and pulse lengths of 10–100 picoseconds (ps) are sent to these satellites and the length of time for the signal to be returned to the telescope is measured with nanosecond precision. Figure 18.9 shows the telescope used to carry out these observations at the Goddard Spaceflight Center and Figure 18.10 shows the geographic distribution of sites where observations have been made. SLR stations have been added in Brasilia, La Plata, India, and Hartebeethoek, providing better coverage from the Southern Hemisphere (Kehm et al., 2016). Not all of those sites have been used for

![](images/72f7ec2a01aa39fac7329e2c303d076d8d86aa118b21cc646e2d3cff3ef8ed37.jpg)  
Figure 18.8 The concept of SLR used to monitor the Earth orientation parameters

![](images/a1d5a7b76daa8fc8ceaf22be7e471a80f542600e70fcce416e9f257d55c33c69.jpg)  
Figure 18.9 Goddard Spaceflight Center SLR telescope. Courtesy of NASA.

Earth orientation determinations. Many have been used in various geodetic research efforts and to establish an accurate terrestrial reference frame (Schutz et al., 1989). However, the scale of the International Terrestrial Reference System (ITRF) determined from the SLR technique has been about 0.7 parts per billion too small due to systematic errors in the measurements, or treatment, of range measurements (Appleby et al., 2016).

The satellites primarily used for Earth orientation measurements are the Laser Geodynamics Satellite (LAGEOS) satellites, which are essentially spherical satellites covered with laser retro reflectors designed to improve the signal-to-noise ratio of the observations. (See Figure 18.11.) LAGEOS-I was built by NASA and launched in 1976 into a nearly polar circular orbit with an altitude of $6 { , } 0 0 0 ~ \mathrm { k m }$ . A second satellite of the same type (LAGEOS-II) was built by the Agenzia Spaziale Italiana of Italy and launched in 1992 into a similar orbit, but with an inclination of 51 degrees. Both are approximately $6 0 \mathrm { c m }$ in diameter, weigh 411 kilograms, and are covered by 426 retro reflectors. Other satellites that have been used include Starlette $( 1 , 0 0 0 ~ \mathrm { k m } )$ and Stella $( 8 0 0 ~ \mathrm { k m } )$ developed and launched by France, Etalon-I and $^ { - 2 }$ ( $1 9 , 0 0 0 ~ \mathrm { k m } )$ developed and launched by the former USSR, and Ajisai $( 1 , 5 0 0 \mathrm { k m } )$ developed and launched by Japan.

As was the case with GPS, the Earth orientation information is derived in the process of determining the satellite orbits using the ranges from the network of observing locations. However, in the case of SLR, ranges measured using visual light are used instead of ranges measured using radio transmissions. As a result, somewhat different physical effects must be accounted for in the SLR analyses. While both techniques are sensitive to the geopotential, solid Earth tides, ocean tides, ocean and atmospheric loading at the observing sites, solar pressure, atmospheric drag, relativistic effects, and Earth albedo, the SLR technique does not have to contend with the ionospheric problems. On the other hand, it does require clear skies to receive returns.

![](images/a900d1455260db6a10642c3ee410f7191951ba0659b76337cb05ae07854b0ae3.jpg)

![](images/6b61774c0cc49953a6bba0f077bb5da83c799105cb50080c385a0d913c7a3641.jpg)  
Figure 18.11 LAGEOS satellite. Courtesy of NASA.

SLR has been used for ranging to GPS and GLONASS satellites to improve the orbit determinations. Two GPS satellites and all GLONASS satellites are equipped with retro reflectors for this purpose. Single-photon SLR stations achieve residuals with precision less than $1 \mathrm { m m }$ . Using the center for orbit determination in Europe (CODE) new orbit model, the SLR mean residual is in the range of $0 . 1 { - } 1 . 8 ~ \mathrm { m m }$ observing GLONASS-M satellites with uncoated corner cubes (Sosnica et al., 2015).

The International Laser Ranging Service (ILRS) was created in 1998 to coordinate the observations and analyses (Gurtner et al., 2005). (See Chapter 19.) It provides data regarding the Earth orientation and terrestrial reference frame to the International Earth Rotation and Reference System Service (IERS) routinely. These data have also been used to produce a long wavelength gravity field reference model that supports all precision orbit determination and provides the basis for studying temporal gravitational variations due to mass redistribution and accurate determinations of tectonic plate motions.

In the past, Earth orientation information was also provided by ranging to targets placed on the Moon’s surface by the Apollo astronauts. While ranging to lunar targets continues, operational Earth orientation information is no longer contributed from the lunar ranges.

# 18.2.4 Doppler Orbit Determination and Radio Positioning Integrated on Satellite (DORIS)

A fourth technique, Doppler Orbit Determination and Radio Positioning Integrated on Satellite, also contributes data to the IERS, primarily for the extension of the terrestrial reference frame. While it can also be used to determine polar motion, the precision of the derived $x , y$ coordinates is not adequate for operational application in the area of Earth orientation parameters.

DORIS is a French system developed by the Centre National d’Etudes Spatiales (CNES) in conjunction with the Institut Géographique National (IGN) and the Groupe de Recherche de Géodésie Spatiale (GRGS). It uses specialized satellites to monitor signals from beacons placed at a number of locations worldwide. As the satellite approaches the beacon on the ground the Doppler effect shifts the frequency seen on the satellite to a higher frequency than that actually broadcast. When the satellite moves away from the beacon, the observed frequency is lower, again as predicted by the Doppler effect. This information, when combined with other data from a network of beacons (see Figure 18.12), allows analysts to determine the location of the beacons with high precision as well as determine the satellite orbits. The system has been placed on a number of satellites intended to carry out geodetic and geophysical research, including Jason-1 and ENVISAT altimetry satellites and the remote-sensing satellites SPOT-2, SPOT-4, and SPOT-5. It also flew with SPOT-3 and TOPEX/POSEIDON. As with the other techniques, a service organization called the International DORIS Service (IDS) has been created to coordinate the observations and data analyses (see Chapter 19) (Tavarnier et al., 2005).

The IDS provided the IERS with 1,140 weekly solutions of station coordinates and Earth orientation parameters from 1993.0 to 2015.0 for the ITRF 2014. The data were from 11 DORIS satellites and six analysis centers. The internal position consistency of $1 0 \ \mathrm { m m }$ or better was achieved (Moreaux et al., 2016). Details concerning the accuracies and problems with the data are given by Blossfeld et al. (2016).

# 18.2.5 Geophysical Modeling

Modern astronomical, meteorological, and geophysical observations have made clear that the atmosphere and oceans do affect the Earth’s orientation. This relationship has been explained by analyses of the conservation of angular momentum in the solid Earth, ocean, and atmosphere systems. If, for example, a component of atmospheric angular momentum (AAM) increases, the analogous angular momentum component of the solid Earth would decrease to conserve the system angular unevenly over the year. The omitted annual and semi-annual seasonal harmonic signal in the horizontal station coordinates affects the Earth orientation parameters, causing differences of several tens of microarcseconds (Krasna et al., 2015).

![](images/b7cf3088f1c2e674c5f22818da08e982e76f8970af0fe574b7b0fe53ab42070e.jpg)

![](images/a8f6b4b31ff34952f3d7bc6ef8fcf9e2388edb641b15c53bf8630c3091f2b764.jpg)  
Figure 18.13 Comparison of astronomical observations of excess length of day with effects derived from analyses of atmospheric angular momentum (AAM).

![](images/08bd232e3d78868693c766cf44476b0dab9a0a2b6536cced66745fc2e8e030ee.jpg)  
Figure 18.14 shows the relationship between the geodetic and AAM excitation functions

The core–mantle boundary (CMB) topography is bumpy (the mountains and valleys represent height differences of a kilometer) and causes pressures and torques that may enhance length of day changes and nutations at selected frequencies. These enhancements are not due to the choice of topography, but are a general fact for some frequencies close to internal wave frequencies. These variations are due to resonances with inertial waves in the incremental core flow. For frequencies far from internal wave frequencies, nutations might still be due to the larger topography variations (Dickman, 2003; Puica et al., 2015).

# 18.2.6 Geomagnetic Field

The geomagnetic field is generated in the Earth’s liquid metallic outer core. The Earth’s rotation and the topography of the coupling surfaces strongly affect core motions and consequently the geomagnetic field (Lambeck, 1980; Hide & Dickey, 1991; Hide et al., 2000; Miyagoshi & Hamano, 2013). The connection between the decadal geomagnetic field and LOD variations has been investigated (Yoshida & Hamano, 1995; Dumberry & Bloxham, 2006). Geomagnetic jerks (GMJ) are abrupt changes in the secular acceleration (second derivative) of motion of the Earth’s magnetic field. They are thought to be due to changes in the fluid flow at the surface of the Earth’s core, and they are not always observed at all stations and not always simultaneously (Gokhberg et al., 2016). Jerks occurred in 1910, 1969, 1972, 1978, 1982, 1991, 1999, 2003, 2007, 2011, and 2014 (Bloxham et al., 2002; Chulliat & Maus, 2014; Kotze, 2017). There appears to be a correlation between GMJs and changes in all five Earth orientation parameters (Vondrak & Ron, 2015). There is also evidence of free core nutation (FCN) changes correlated with GMJs (Malkin, 2013, 2016; Vondrak & Ron, 2014). Variations in the LOD within a period of about 10 years might be associated with GMJs (Gokhberg et al., 2016). The shorter period components of LOD variations correlate with GMJs for LOD oscillations contemporaneous with jerks in 1969, 1972, 1978, and 1982 (Holme & de Viron, 2013).

# 18.3 Earth Orientation Data

The IERS (see Chapter 19) routinely provides Earth orientation data produced from the observations available from the sources outlined earlier. Historical, current, and forecast values of the parameters are made available to users from two product centers, the Earth Orientation Center and the Rapid Service/Prediction Service. The Earth Orientation Center Product Center publishes long-term Earth orientation parameters with the monthly publication of IERS Bulletin B that lists the most recent values of the Earth’s orientation in the IERS Reference System. The IERS Rapid Service/Prediction Center provides Earth orientation parameters on a rapid turnaround basis, primarily for real-time users and others needing the highest-quality EOP information sooner than that available in the final series published by the IERS Earth Orientation Center. Table 18.1 lists the uncertainties of the IERS products.

Table 18.1 Uncertainties of IERS products   

<table><tr><td></td><td></td><td colspan="4">Precision</td></tr><tr><td>Technique</td><td>Sampling Time</td><td>Polar Motion</td><td>UT1-UTC</td><td>LOD</td><td>Celestial Pole Offsets</td></tr><tr><td>VLBI</td><td>1 day</td><td>0.000 08&quot;</td><td>0.000 005 s</td><td>0.000 007 s/day</td><td>0.000 085&quot;</td></tr><tr><td>VLBI</td><td>1 hr</td><td>一</td><td>0.000 020 s</td><td>0.000 028 s/day</td><td></td></tr><tr><td>SLR</td><td>1 day</td><td>0.000 15&quot;</td><td></td><td></td><td></td></tr><tr><td>GPS</td><td>1 day</td><td>0.000 02&quot;</td><td>一</td><td>0.000 020 s/day</td><td></td></tr><tr><td>Combination</td><td></td><td>0.000 004&quot;</td><td>0.000 006 s</td><td>0.000 009 s/day</td><td>0.000 1&quot;</td></tr><tr><td>Five-day Prediction</td><td></td><td>0.000 09&quot;</td><td>0.000 02 s</td><td>0.000 03 s/day</td><td>0.000 1&quot;</td></tr></table>

# References

Altamimi, Z., Rebischung, P., Métivier, L., & Collilieux, X. (2016). ITRF2014: A New Release of the International Terrestrial Reference Frame Modeling Nonlinear Station Motions, J. Geophys. Res. Solid Earth, 121. doi:10.1002/2016JB013098   
Appleby, G., Rodriguez, J., Altamimi, Z. (2016). Assessment of the Accuracy of Global Geodetic Satellite Laser Ranging Observations and Estimated Impact on ITRF Scale: Estimation of Systematic Errors in LAGEOS Observations 1993–2014, J. Geodesy, 90, 1371–1388.   
Barnes, R. T. H., Hide, R., White, A. A., & Wilson, C. A. (1983). Atmospheric Angular Momentum Fluctuations, Length-of-Day Changes and Polar Motion. Proceedings of the Royal Society of London Series A, 387, 31–73.   
Blossfeld, M., Seitz, M., Angermann, D., & Moreaux, G. (2016). Quality Assessment of IDS Contribution to ITRF2014 Performed by DGFI-TUM. Advances in Space Research, 58, 2505–2519.   
Bloxham, J., Zatman, S., & Dumberry, M. (2002). The Origin of Geomagnetic Jerks. Nature, 420, 65–68.   
Carter, W. E. & Robertson, D. S. (1986). Studying the Earth by Very-Long-Baseline Interferometry, Sci. Am., 255, 44–52.   
Carter, W. E., Robertson, D. S., & Fallon, F. W. (1989). Polar Motion and UT1 Time Series Derived from VLBI Observations. IERS Tech. Notes, No. 2, 35–39.   
Chen, J. L., Wilson, C. R., Ries, J. C., & Tapley, B. D. (2013). Rapid Ice Melting Drives Earth’s Pole to the East. Geophys. Res. Let., 40, 2625–2630. doi:10.1002/ grl.50552   
Chulliat, A. & Maus, S. (2013). Geomagnetic Secular Acceleration, Jerks, and a Localized Standing Wave at the Core Surface from 2000 to 2010. J. of Geophysical Research: Solid Earth, 10.1002/2013 JB010604.   
Dickman, S. R.(2003). Evaluation of “Effective Angular Momentum Function” Formulations with Respect to Core–Mantle Coupling. J. Geophys. Res., 108(B3), 2150. doi:10.1029/2001JB001603   
Dill, R., Dobslaw, H., & Thomas, M. (2013). Combination of Modeled Short-Term Angular Momentum Function Forecasts from Atmosphere, Ocean, and Hydrology with 90-Day EOP Predictions. Journal of Geodesy, 87, 567–577.   
314 Modern Earth Orientation   
Dumberry, M. & Bloxham, J. (2006). Azimuthal Flows in the Earth’s Core and Changes in Length of Day at Millennial Timescales. Geophys. J. Int. 165, 32–46. doi:10.1111/ j.1365-246X.2006.02903.x   
Fey, A., Gordon, D., & Jacobs, C., eds. (2009). The Second Realization of the International Celestial Reference Frame by Very Long Baseline Interferometry, Presented on Behalf of the IERS/IVS Working Group. In (IERS Technical Note 35). Frankfurt am Main: Verlag des Bundesamts für Kartographie und Geodäsie.   
Gokhberg, M. B., Olshanskaya, E. V., Chkhetiani, O. G., Shalimov, S. L., & Barsukov, O. M. (2016). Correlation between Large Scale Motions in the Liquid Core of the Earth and Geomagnetic Jerks, Earthquakes, and Variations in the Earth’s Length of Day. Doklady Earth Sciences, 467, 280–283.   
Gordon, D. (2016). Impact of the VLBA on Reference Frames and Earth Orientation Studies. J. Geodesy. doi:10.1007/s00190-016–0955–0   
Gross, R. S. (2012). Improving UT1 Predictions Using Short-Term Forecasts of Atmospheric, Oceanic, and Hydrologic Angular Momentum. In H. Schuh, S. Boehm, T. Nilsson, & N. Capitaine, eds., Journées Systèmes de Référence Spatiotemporels 2011. Vienna: Vienna University of Technology, pp. 117–120.   
Gurtner, W., Noomen, R., & Pearlman, M. R. (2005). The International Laser Ranging Service: Current Status and Future Developments. Advances in Space Research, 36, 327–332.   
Hide, R., Birch, N. T., Morrison, L. V., Shea, D. J., & White, A. A. (1980). Atmospheric Angular Momentum Fluctuations and Changes in the Length of the Day. Nature, 286, 114–117.   
Hide, R., Boggs, D. H., & Dickey, J. O. (2000). Angular Momentum Fluctuations within the Earth’s Liquid Core and Torsional Oscillations of the Core–Mantle System. Geophys. J. Int. 143, 777–786. doi:10.1046/j.0956-540X.2000.01283.x   
Hide, R. & Dickey, J. O. (1991). Earth’s Variable Rotation. Science 253, 629–637. doi:10.1126/science.253.5020.629   
Holme, R. T. & de Viron, O. (2013). Probing Geomagnetic Jerks Combining Geomagnetic and Earth Rotation Observations. American Geophysical Union, Fall Meeting, #GP52A–01.   
Johnston, K. J. (1979). The Application of Radio Interferometric Techniques to the Determination of Earth Rotation. In D. D. McCarthy & J. D. Pilkington, eds., Time and the Earth’s Rotation. Dordrecht: Reidel, pp. 183–190.   
Kehm, A., Blossfeld, M., & Pavlis, E. C. (2016). Future Global SLR Network Evolution and Its Impact on the Terrestrial Reference Frame. Geophysical Research Abstracts, 18, EGU2016–5848.   
Kotze, P. B. (2017). The 2014 Geomagnetic Jerk as Observed by Southern African Magnetic Observatories. Earth, Planets, and Space, 69(17). doi:10.1186/s40623- 017–0605–7.   
Koot, L., De Viron, O., & Dehant, V. (2006). Atmospheric Angular Momentum Time-Series: Characterization of Their Internal Noise and Creation of a Combined Series. J. Geodesy, 79, 663–674.   
Kouba, J., Beutler, G., & Rothacher, M. (2000). IGS Combined and Contributed Earth Rotation Parameter Solutions. In S. Dick, D. McCarthy, & B. Luzum, eds., Polar Motion: Historical and Scientific Problems. ASP Conference Series, Vol. 208, also IAU Colloquium #178. San Francisco, CA: ASP, pp. 277.   
Krasna, H., Malkin, Z., & Bohm, J. (2015). Non-Linear VLBI Station Motions and Their Impact on the Celestial Reference Frame and Earth Orientation Parameters. J. Geodesy, 89, 1019–1033. 18.3 Earth Orientation Data 315   
Lambeck, K. (1980). The Earth’s Variable Rotation. Cambridge: Cambridge University Press.   
Malkin, Z. (2013). Free Core Nutation and Geomagnetic Jerks. J. Geodynamics, 72, 53–58.   
Malkin, Z. (2016). Free Core Nutation: New Large Disturbance and Connection Evidence with Geomagnetic Jerks. arXiv:1603.03176v1.   
Miyagoshi, T. & Hamano, Y. (2013). Magnetic Field Variation Caused by Rotational Speed Change in a Magnetohydrodynamic Dynamo. Phys. Rev. Lett. 111, 124501. doi:10.1103/Phys Rev Lett.111.124501   
Moreaux, G., Lemoine, F. G., Capdeville, H., Kuzin, S., Otten, M., Štěpánek, P., Willis, P., & Ferrage, P. (2016). The International DORIS Service Contribution to the 2014 Realization of the International Terrestrial Reference Frame. Advances in Space Research, 58, 2479–2504.   
Nilsson, T., Heinkelmann, R., Karbon, M. R., Raposo-Pulido, V., Soja, B., & Schuh, H. (2014). Earth Orientation Parameters Estimated from VLBI during the CONT11 Campaign. J. Geodesy, 88, 491–502.   
Panafidina, N., Kurdubov, S., & Rothacher, M. (2012). Empirical Model of Subdaily Variations in the Earth Rotation from GPS and Its Stability. In H. Schuh, S. Boehm, T. Nilsson, & N. Capitaine, eds., Journées Systèmes de Référence Spatio-temporels 2011. Vienna: Vienna University of Technology, pp. 148–151.   
Petit, G. P. & Luzum, B. J., eds. (2010). IERS Conventions (2010) (IERS Technical Note 36). Frankfurt am Main: Verlag des Bundesamts für Kartographie und Geodäsie.   
Petrachenko, W., Behrend, D., Hase, H, Ma, C., Niell, A., Schuh, H., & Whitney, A. (2013). The VLBI2010 Global Observing System (VGOS). Geophysical Research Abstracts, 15, EGU2013–12867.   
Puica, M., Dehant, V., Folgueira, M., Trinh, A., & van Hoolst, T. (2015). Topographic Coupling at Core–Mantle Boundary in Rotation and Orientation Changes of the Earth. Geophysical Research Abstracts, 17, EGU2015-13930–1.   
Rothacher, M. (1999). The Contribution of GPS Measurements to Earth Rotation Studies. In Journées 1998: Systèmes de référence spatio-temporels: Conceptual, Conventional and Practical Studies Related to Earth Rotation. Paris: Observatoire de Paris, France. Département d‘Astronomie Fondamentale, pp. 239–247.   
Schlüter, W. & Behrend, D. (2007). The International VLBI Service for Geodesy and Astrometry (IVS): Current Capabilities and Future Prospects. J. Geodesy, 81, 379–387.   
Schutz, B. E., Tapley, B. D., Eanes, R. J., & Watkins, M. M. (1989). Earth Rotation from LAGEOS Laser Ranging. IERS Tech. Notes, No. 2, 53–57.   
Sosnica, K., Thaller, D., Dach, R., Steigenberger, P., Beutler, G., Arnold. D., & Jäggi, A. (2015). Satellite Laser Ranging to GPS and GLONASS. J. Geodesy, 89, 725–743.   
Tavernier, G., Fagard, H., Feissel-Vernier, M., Lemoine, F., . . . Willis, P. (2005). The International DORIS Service. Advances in Space Research, 36, 333–341.   
Vondrak, J. & Ron, C. (2014). Geophysical Excitation of Nutation and Geomagnetic Jerks. Geophysical Research Abstracts, 16, EGU2014–5691.   
Vondrak, J. & Ron, C. (2015). Earth Orientation and Its Excitations by Atmosphere, Oceans, and Geomagnetic Jerks. Serb. Astron. J., 191, 59–66.   
Vondrak, J., Ron, C., & Stefka, V. (2009). New Solution of Earth Orientation Parameters in 20th Century. Highlights of Astronomy, 15, XXVIIth IAU General Assembly, I. F. Corbett, editor.   
Wielgosz, A., Tercjak, M., & Brzezinski, A. (2016). Testing Impact of the Strategy of VLBI Data Analysis on the Estimation of Earth Orientation Parameters and Station Coordinates. Reports on Geodesy and Geoinformatics, 101, 1–15.   
Yoshida, S. & Hamano, Y. (1995). Geomagnetic Decadal Variations Caused by Length-of-Day Variation. Phys. Earth Planet. Int. 91, 117–129. doi:10.1016/0031–9201(95)03038-X

# 19

# International Activities

# 19.1 Time and International Activities

Because time has become an international standard, a variety of international organizations have evolved to deal with various aspects of time and timekeeping. These range from the political and commercial agencies concerned with issues related to international standards to scientific organizations dealing with subtle aspects of the technical definitions of timescales and organizations that promote the development of even more accurate devices and means for time dissemination.

# 19.2 Treaty of the Meter

Although the subject of time was not covered originally in the Treaty of the Meter signed on May 20, 1875 (Bureau International des Poids et Mesures, 2006), it has since become part of the mission of the organizational structure put in place by the Treaty. The Treaty of the Meter is also known as the Meter Convention or in French as the Convention du Mètre. Written in the French language, it was signed by 17 countries at the International Metric Convention that was called to organize formally the means to maintain the metric standards. The number of signatories increased to 21 in 1900, 32 in 1950, 44 by 1975, 48 by 1997, and 49 by 2001. As of August 2016, 58 signatories and 41 associate states and economies had signed the Treaty. It was revised in 1921, and the system of units it established was renamed the Système international d’unités (International System of Units) (SI) in 1960. To carry out the intentions of the treaty, three organizations were created: the Conférence Générale des Poids et Mesures (CGPM), the Comité International des Poids et Mesures (CIPM), and the Bureau International des Poids et Mesures (BIPM). The CGPM took responsibility for an international standard time in 1985 (Guinot, 2000).

# 19.2.1 General Conference on Weights and Measures (CGPM)

Delegates from each of the signatories along with observers from each of the associates comprise the CGPM. It meets every four years at the BIPM, where it receives the official report of the CIPM, discusses possible improvements in the SI units, and endorses new metrological results and international scientific recommendations regarding the fundamental units. It also makes decisions regarding the future direction of the BIPM. For example, the SI was established in 1960 by the 11th CGPM and is modified by the CGPM as required to reflect the latest advances.

# 19.2.2 International Committee on Weights and Measures (CIPM)

Eighteen individuals, each from a different member state, comprise the CIPM. Its mission is to promote uniformity in the international measurement units principally by submitting draft resolutions to the CGPM for its approval. It discusses the work of the BIPM and issues an annual report on the operations of the BIPM to the governments of the member states. Its members discuss and coordinate current metrological activities and prepare other reports, including the SI Brochure.

The CIPM has created a number of Consultative Committees (in French: Comités Consultatifs) to provide technical information on a wide range of metrological activities. Each committee is composed of technical experts from national metrology institutes, and the chair of each committee usually serves on the CIPM. These committees discuss scientific and technical advances related to metrology and formulate recommendations for the CIPM. They also advise the CIPM on the work of the BIPM. The committees with titles current as of 2017 are:

Consultative Committee for Acoustics, Ultrasound and Vibration (CCAUV), Consultative Committee for Electricity and Magnetism (CCEM),   
Consultative Committee for Length (CCL),   
Consultative Committee for Mass and Related Quantities (CCM),   
Consultative Committee for Photometry and Radiometry (CCPR),   
Consultative Committee for Amount of Substance – Metrology in Chemistry (CCQM),   
Consultative Committee for Ionizing Radiation (CCRI),   
Consultative Committee for Thermometry (CCT),   
Consultative Committee for Time and Frequency (CCTF), and the   
Consultative Committee for Units (CCU).

The CIPM meets annually at the BIPM to discuss the reports of the Consultative Committees. The CCU assists in the preparation of the SI Brochure. Suggested modifications of the SI are submitted to the CGPM by the CIPM for formal adoption. On matters relating to interpretation or usage of the SI, the CIPM may also adopt its own resolutions and recommendations.

![](images/207b2b2d61a3b1408085221cdc253f36759efef31a0699a271feb01d33f6de0b.jpg)  
Figure 19.1 Organizational structure within the Treaty of the Meter that deals with time

# 19.2.3 Bureau International des Poids et Mesures (BIPM)

The third organization created by the Meter Convention is the BIPM, located in Sèvres, a suburb of Paris. Its status is that of an intergovernmental organization financed by the member states of the Meter Convention. Its operations fall under the supervision of the CIPM, and its staff carries out its mission to ensure international unification of physical measurements. It provides the basis for a single, coherent system of measurements traceable to the SI.

The BIPM is currently organized in five technical departments: Physical Metrology, Time, Ionizing Radiation, Chemistry, and Information Technology Services (see Figure 19.1). These carry out a variety of tasks, including maintaining the kilogram, coordinating international measurement standards, and in the case of time, providing the actual SI unit, the second.

# 19.3 Scientific Unions

International scientific organizations have contributed to accurate timekeeping by promoting investigations of the associated scientific and technical problems. They have made recommendations that have affected modern timekeeping significantly in the past, and it is expected that they will continue to contribute to future developments. Two scientific unions concerned with precise time, the International Astronomical Union (IAU) and the International Union of Geodesy and Geophysics (IUGG), are members of the International Council for Science (ICSU), a nongovernmental organization of 31 international scientific unions and 22 national scientific bodies representing 142 countries. In pursuit of its mission to strengthen international science it seeks to address major scientific issues and facilitate interaction across disciplines and countries. It maintains close working relationships with a number of intergovernmental and nongovernmental organizations, especially the United Nations Educational, Scientific and Cultural Organization (UNESCO) and the Third World Academy of Sciences (TWAS). ICSU holds a General Assembly every three years to set general direction, policies, and priorities. Its funding is mainly through national members and scientific unions along with grants from UNESCO, the United States, and France.

# 19.3.1 International Astronomical Union (IAU)

The International Astronomical Union was founded in 1919 to promote the science of astronomy through international cooperation. It is made up of national and individual members. National members are organizations that represent national professional astronomical communities within their countries, and individual members are professional scientists whose research relates to astronomy. Individual members are elected by the Union’s Executive Committee following the recommendation of a National Member.

The IAU is currently organized into nine divisions. Each division is broken down further into commissions that deal with specific specialized topics. The number of commissions now totals 35. The organization also allows for any number of working groups that can report either to divisions or to commissions. As of 2017, there are 79 national members and more than 12,740 individual members. The Executive Committee sets and implements the overall policy, and the operations are overseen by a set of elected officers. The center for its business activities is the IAU Secretariat, which is hosted by the Institut d’Astrophysique de Paris in France.

In addition to sponsoring a number of symposia each year, the IAU holds a General Assembly every three years. The IAU defines fundamental astronomical and physical constants and astronomical nomenclature. It also promotes educational activities in astronomy and discusses future developments dealing with the science of astronomy. Matters related to the subject of time are discussed in Division A, Fundamental Astronomy, which operates through three commissions within the division: Commission A1, Astrometry; Commission A2, Rotation of the Earth; Commission A3, Fundamental Standards; one Inter-Division Commission

A4: Celestial Mechanics and Dynamical Astronomy; and one Cross-Division Commission: Solar System Ephemerides. The latter two are shared with Division F, Planetary Systems and Bioastronomy.

To undertake well-defined tasks, the IAU has also established Working Groups within Division A. These include Working Groups on (1) the Theory of Earth Rotation and Validation (joint with the International Association of Geodesy), (2) Multi-Waveband Realizations of International Celestial Reference System, (3) Numerical Standards in Fundamental Astronomy (NSFA), (4) Standards of Fundamental Astronomy (SOFA), (5) Third Realization of International Celestial Reference Frame, and (6) Time Metrology Standards. In addition, a joint Working Group with Division F has been established dealing with Cartographic Coordinates & Rotational Elements. The commissions are composed of technical experts dealing with detailed aspects of the commission’s tasks. Commissions A2 and A3 are of particular interest for those dealing with time.

The objectives of Commission A2, Rotation of the Earth, are to:

1. Encourage and develop cooperation and collaboration in observation and theoretical studies of Earth orientation variations.   
2. Serve the astronomical community by linking it to the official organizations that provide the International Terrestrial and Celestial Reference Systems/Frames and Earth orientation parameters (EOP), namely International Association of Geodesy (IAG), International Earth rotation and Reference systems Service (IERS), International VLBI Service for Geodesy and Astrometry (IVS), International GNSS Service (IGS), International Laser Ranging Service (ILRS), and International DORIS Service (IDS).   
3. Develop methods to improve the accuracy and understanding of Earth orientation variations and related reference systems/frames.   
4. Ensure agreement and continuity of the reference frames used for studying Earth orientation variations with other astronomical reference frames and their densification.   
5. Provide means of comparing observational and analysis methods and results to ensure accuracy of data and models and encourage the development of new observation techniques.

The activities of Commission A3, Fundamental Standards, include facilitating advances in astronomy and other fields in science and engineering, by developing, implementing, and communicating fundamental IAU-endorsed standards for fundamental astronomy. Such standards include, but are not limited to:

1. celestial and terrestrial reference systems/frames and the transformations among them;

2. timescales;   
3. precession/nutation models;   
4. Earth rotation and polar motion, including physical models (e.g., Earth’s gravity   
field, lunar gravity field, Earth interior model, solid Earth–tide modeling);   
5. star catalogs;   
6. ephemerides of solar system bodies; and   
7. special and general relativistic models for time and space.

The Working Group Time Metrology Standards has the objective of enhancing the interaction between astronomers and the time and frequency metrology community. The time metrology community provides the reference atomic timescale, which is the basis of coordinate times used for space-time referencing in astronomy. The dynamical timescale based on precision timing of pulsars has the potential of improving the long-term standard of time. Potential future developments will require common actions of both astronomers and metrologists. Examples include the possible new definition of the second, a consequence of the advent of optical clocks, and the contribution to the studies on the adoption of a uniform international reference timescale.

# 19.3.2 International Union of Geodesy and Geophysics (IUGG)

The International Union of Geodesy and Geophysics is a nongovernmental, scientific organization, established in 1919 to promote international coordination of scientific studies of the Earth and its environment in space. These studies include the shape of the Earth, its gravitational and magnetic fields, the dynamics of the Earth as a whole and of its component parts, the Earth’s internal structure, composition, and tectonics, the generation of magmas, volcanism, and rock formation, the hydrological cycle including snow and ice, all aspects of the oceans, the atmosphere, ionosphere, magnetosphere and solar–terrestrial relations, and analogous problems associated with the Moon and other planets. It is made up of eight semiautonomous associations, each responsible for specific topics within the Union activities:

• International Association of Cryospheric Sciences (IACS)   
• International Association of Geodesy (IAG)   
• International Association of Geomagnetism and Aeronomy (IAGA)   
• International Association of Hydrological Sciences (IAHS)   
• International Association of Meteorology and Atmospheric Sciences (IAMAS)   
• International Association for the Physical Sciences of the Ocean (IAPSO)   
• International Association of Seismology and Physics of the Earth’s Interior (IASPEI)

• International Association of Volcanology and Chemistry of the Earth’s Interior (IAVCEI)

These associations can organize individual assemblies in the interim between the IUGG General Assemblies that are held every four years. The IUGG has 59 regular member countries and 10 associate members, most of whom participate in the Union through their national academy or other adhering body.

Most of the activity dealing with timekeeping is carried out through the IAG, which was originally organized as the Mitteleuropäische Gradmessung (Central European Arc Measurement) in 1862 as the first significant international scientific organization. It became the Europäische Gradmessung (European Arc Measurement) in 1867 and in 1886 the Internationale Erdmessung. At the first IUGG General Assembly in 1922, it became one of the sections, and it took its present name at the IUGG General Assembly of 1930.

The official mission of the IAG is the advancement of geodesy. It is concerned with establishment of reference systems, monitoring the gravity field, Earth rotation, and deformation of the Earth’s surface, including oceans and ice. It holds symposia and workshops to promote international cooperation and knowledge. Its components include:

• Commission 1: Reference Frames, • Commission 2: Gravity Field, • Commission 3: Geodynamics and Earth Rotation, • Commission 4: Positioning and Applications, • Inter-Commission Committee on Theory, • Inter-Commission Committee on Theory, • Global Geodetic Observing System (GGOS), • 14 International Scientific Services.

The Global Geodetic Observing System is the observing system of the IAG. It works with the IAG components providing the geodetic infrastructure necessary for monitoring the Earth system and for global change research. To maintain a stable, accurate, and global reference frame, GGOS provides observations of the Earth’s shape, gravity field, and rotational motion. It does this by integrating different geodetic techniques, models, and approaches in order to ensure long-term, precise monitoring of geodetic observables.

# 19.3.3 International Telecommunications Union (ITU)

The International Telecommunications Union is a United Nations organization that deals with information and communications technologies. Based in Geneva,

Switzerland, the ITU has 193 member states and almost 800 sector members and associates. Sector members are recognized operating agencies, scientific or industrial organizations, financial or development institutions, and organizations of an international character representing them. The ITU is comprised of three sectors:

• Radiocommunication (ITU-R) • Telecommunications Standardization (ITU-T) • Telecommunication Development (ITU-D)

The ITU-R manages the international radio frequency spectrum and satellite orbit resources and is the primary sector of the ITU dealing with issues of time and frequency. The ITU-T deals with setting technical specifications so that elements of communications systems can interoperate seamlessly, and ITU-D creates policies and regulations and provides training programs and financial strategies in developing countries. The ITU also organizes TELECOM events that bring together leading elements of the information and communication technologies (ICT) as well as ministers and regulators for exhibitions, and high-level forums.

The ITU dates back to the days following the establishment of telegraph networks. To facilitate international communications, countries gradually established regional agreements, and in 1865 the International Telegraph Convention was signed, resulting in the formation of the International Telegraph Union. With the development of the telephone and wireless telegraphy, it was necessary to establish international agreements regarding radiotelegraphy. The first International Radiotelegraph Conference was held in 1906 in Berlin, resulting in the first International Radiotelegraph Convention and a set of regulations. These regulations, which have since been expanded and revised by the following radio conferences, are now known as the Radio Regulations.

Within the ITU, the International Telephone Consultative Committee (CCIF) was established in 1924, followed by the International Telegraph Consultative Committee (CCIT) in 1925, and the International Radio Consultative Committee (CCIR) in 1927. These organizations coordinated the technical studies, tests, and measurements and drew up international standards to ensure international communications. The 1927 International Radiotelegraph Conference was the first to allocate frequency bands to existing radio services, including fixed, maritime and aeronautical mobile, broadcasting, amateur, and experimental.

In 1932, the International Telecommunication Convention was formed by combining the International Telegraph Convention and the International Radiotelegraph Convention. At the same time, the name of the Union was changed to International Telecommunication Union to reflect its expanding scope. In 1947, it became a United Nations specialized agency and in 1956, the CCIT and the CCIF were merged to form the International Telephone and Telegraph Consultative

Committee (CCITT). In 1992, a plenipotentiary conference revised the structure of the ITU into the three sectors that integrated the functions carried out by the CCIR and the CCITT.

Some documents of the ITU have the status of international treaties. These are (1) the Constitution and Convention of the International Telecommunication Union originally signed in 1992 and subsequently amended at following plenipotentiary conferences and (2) the Administrative Regulations, which include the Radio Regulations (www.itu.int/publ/R-REG-RR/en) and the International Telecommunication Regulations (www.itu.int/ITU-T/itr/), which complement the Constitution and the Convention. The first version of what came to be called the Radio Regulations appeared in 1906 and they have been revised frequently since then. Previously adopted Telephone and Telegraph Regulations were merged in 1998 to create the International Telecommunication Regulations, and these were revised in 2012. The Radio Regulations incorporate the decisions of the World Radiocommunication Conferences, including all appendices, resolutions, recommendations, and ITU-R recommendations incorporated by reference. World radiocommunication conferences (WRCs) are held every two to three years to review and, if required, revise the Radio Regulations. The general program of world radiocommunication conferences is established four to six years in advance and the final agenda set by the ITU Council two years before the conference, with the concurrence of a majority of member states.

The Plenipotentiary Conference is held every four years to set the Union’s general policies, adopt plans for the future, and elect the management team. At this conference ITU member states decide on the future of the organization and sector members can attend as observers. The ITU Council, in the interval between Plenipotentiary Conferences, deals with broad telecommunication policies and prepares a report on the policy and strategic planning of the ITU. It is responsible for ensuring the smooth operation of the Union and facilitates the implementation of the provisions of the ITU Constitution, the ITU Convention, and the Administrative Regulations.

Within the ITU, matters relating to precise time and its dissemination fall within the tasks of the ITU-R, and within the ITU-R they are part of the agenda of Study Group 7. Study Group 7 is part of the structure of the Study Groups, which includes:

• Study Group 1 (SG 1) – Spectrum management • Study Group 3 (SG 3) – Radiowave propagation • Study Group 4 (SG 4) – Satellite services • Study Group 5 (SG 5) – Terrestrial services • Study Group 6 (SG 6) – Broadcasting services • Study Group 7 (SG 7) – Science services

![](images/bea0051d8c8d21c752cd05cbf4c974ac62656c8e2712164431f14a0360effafb.jpg)  
Figure 19.2 Organizational structure within the ITU dealing with time

Within Study Group 7, issues related to precise time fall within the purview of Working Party 7A. Study Group 7 is structured as follows:

• Working Party 7A (WP 7A) – Time signals and frequency standard emissions   
• Working Party 7B (WP 7B) – Space radiocommunication applications   
• Working Party 7C (WP 7C) – Remote sensing systems   
• Working Party 7D (WP 7D) – Radio astronomy

Issues related to precise time that might be expected to be included in the Radio Regulations would then be expected to be brought up first with Working Party 7A for discussion. They then would go to Study Group 7, then to ITU-R, before being accepted at a World Radio Conference (see Figure 19.2).

# 19.4 Service Organizations

Another set of time-related organizations deals with the coordination and analyses of observations relating to the Earth’s rotation. Administratively these organizations fall within the World Data System (ICSU-WDS), an interdisciplinary body of the ICSU created in 2008. Its mission is to promote long-term stewardship of, and access to, quality-assured scientific data and data services, products, and information across disciplines in the natural and social sciences, and the humanities. It aims to facilitate scientific research by coordinating and supporting trusted scientific data services for the provision, use, and preservation of relevant data, and is meant to combine the efforts of two previous organizations, World Data Centers and the Federation of Astronomical and Geophysical Data Analysis Services. The ICSU-WDS has 105 member organizations. Of these, 68 are regular members that are data stewards and/or data analysis services, 11 are network members representing groups of data stewardship organizations and/or data analysis services, 8 are partner members that contribute support or funding, and 18 are associate members organizations that are interested in the endeavor, but do not contribute direct funding or other material support.

# 19.4.1 International Earth rotation and Reference systems Service (IERS)

The IERS was established as the International Earth Rotation Service in 1987 by the International Astronomical Union and the International Union of Geodesy and Geophysics, and it began operation on January 1, 1988. In 2003, it was renamed the International Earth Rotation and Reference Systems Service, but retained the acronym IERS. It is a regular member of the ICSU-WDS whose objectives are to provide the International Celestial Reference System (ICRS) and its realization, the International Celestial Reference Frame (ICRF); the International Terrestrial Reference System (ITRS) and its realization, the International Terrestrial Reference Frame (ITRF); Earth orientation parameters required to transform between the ICRF and the ITRF; geophysical data to interpret and model variations in the ICRF, ITRF, or Earth orientation parameters; and the standards, constants, and models (i.e., conventions) necessary to use the products. Its products include the International Celestial Reference Frame, the International Terrestrial Reference Frame, monthly Earth orientation data, daily rapid service estimates of near realtime Earth orientation data and their predictions, announcements of the differences between astronomical and civil time for time distribution by radio stations, leap second announcements, products related to global geophysical fluids such as mass and angular momentum distribution, an annual report and technical notes on conventions and other topics, and long-term Earth orientation information.

It carries out its objectives with an organization made up of Technique Centers, Product Centers, Combination Centers, an Analysis Coordinator, and a Central Bureau. The Technique Centers are independent service organizations that have made commitments to the IERS to contribute observational material regarding various aspects of the Earth’s rotation. They control the organization of their observations, the analyses and archiving of data, and the development of possible improvements either in the technique or in the analyses of their data. The data are delivered without interruption and with minimal delay. Currently, the four Technique Centers are the International GNSS Service (IGS), the International Laser Ranging Service (ILRS), the International VLBI Service (IVS), and the International DORIS Service (IDS). The organization is shown in Figure 19.3 and the details of its individual products are outlined later in this chapter (Dick & Richter, 2004).

![](images/414f6cfc59006c3006541f72e1dd443fe3771cf98268e0225f82ea30c3f8f8a2.jpg)  
Figure 19.3 The organizational structure of the IERS

The Product Centers provide the actual products of the IERS. These are various self-supported organizations that have committed to provide these products operationally. The Product Centers include the Earth Orientation Center, the Rapid Service/Prediction Center, the Conventions Center, the International Celestial Reference System Center, the International Terrestrial Reference System Center, and the Global Geophysical Fluids Center. Within the latter Product Center, a number of sub-bureaus exist to handle particular aspects of the work. These include the Special Bureau for the Atmosphere, the Special Bureau for the Oceans, the Special Bureau for Tides, the Special Bureau for Hydrology, the Special Bureau for the Mantle, the Special Bureau for the Core, the Special Bureau for Gravity/ Geocenter, and the Special Bureau for Loading.

The Earth Orientation Center is situated at the Bundesamt für Kartographie und Geodäsie in Frankfurt am Main, Germany, and is responsible for monitoring the long-term aspects of the variations of Earth orientation parameters. It publishes monthly bulletins containing Earth orientation data as well as announcements regarding leap seconds and the difference between UT1 and UTC. The IERS Rapid Service/Prediction Center is provided by the US Naval Observatory, and it provides Earth orientation parameters on a rapid turnaround basis, primarily for real-time users and others needing the highest-quality EOP information sooner than that available in the final series published by the IERS Earth Orientation Center. It also provides forecasts of future variations in the Earth orientation parameters.

Table 19.1 Special Bureaus of the Global Geophysical Fluids Product Center   

<table><tr><td>Special Bureau</td><td>Location</td><td>Mission</td></tr><tr><td>Atmosphere</td><td>Atmospheric and Environmental Research, Inc.</td><td>relevant atmospheric data</td></tr><tr><td>Oceans</td><td>Jet Propulsion Laboratory</td><td>data relating to nontidal changes in oceanic processes</td></tr><tr><td>Hydrology</td><td>Center for Space Research, University of Texas at Austin</td><td>datasets and numerical models related to the changing distribution of water over the planet</td></tr><tr><td></td><td>Combination Faculté des Sciences,de la Technologie et de la Communication</td><td>combination of geophysical fluid data</td></tr></table>

The Conventions Center is a joint operation of the Bureau International des Poids et Mesures and the US Naval Observatory. It is responsible for the maintenance of the IERS conventional models, constants, and standards used in the definition and realization of the reference systems. The ICRS Center is responsible for the definition of the ICRS and its realization, the ICRF. This effort is carried out jointly by the Observatoire de Paris and the US Naval Observatory. Similarly, the ITRS Center is responsible for the definition of the ITRS and its realization, the ITRF. This work involves network coordination including collocation, local ties, and site quality, and is carried out by the Institut Géographique National (IGN) in France.

The Global Geophysical Fluids Center, through its four Special Bureaus, supports research in areas related to the variations in Earth rotation, gravitational field, and geocenter that are caused by mass transport in the geophysical fluids. It is housed at the University of Luxembourg. The sub-bureaus and their locations are shown in Table 19.1.

IERS Combination Research Centers develop methods to combine data or products provided by different techniques. The ITRS Combination Centers provide ITRF products to the ITRF Product Center after combining inputs from the Technique Centers. The Analysis Coordinator is responsible for the long-term internal consistency of the IERS products, and the Central Bureau provides the general administration of the IERS consistent with the Directing Board policies. It is the executive arm of the Directing Board, and facilitates communications among the components of the organization.

# 19.4.2 International VLBI Service for Geodesy and Astrometry (IVS)

The International VLBI Service for Geodesy and Astrometry, one of the services of GGOS and the ICSU-WDS, is an international collaboration of organizations that provides VLBI data to the IERS and other astrogeodetic users (Schlüter & Behrend, 2007; Schuh & Behrend, 2012; Behrend, 2013). The objectives of the IVS are to enhance the individual VLBI programs of the member organizations by creating a joint service that coordinates their activities, to promote research and development of the technique, and to serve as an interface with the users of VLBI data. To meet its objectives, the IVS coordinates observing programs, sets standards for observing stations, establishes VLBI data formats, recommends analysis software, and sets up data delivery processes. It carries out its tasks through an organization that includes a Coordinating Center, network stations, operation centers, correlators, data centers, analysis centers, and technology development centers.

The Coordinating Center coordinates both the day-to-day and the long-term activities of the IVS following the directions established by the Directing Board. The network stations are the global VLBI observing sites with geodetic capability that comply with the IVS performance standards for data quality. The operation centers coordinate routine operations of one or more networks. These activities include planning observing programs, establishing operating plans and procedures for the stations in the network, generating the observing schedules, and posting the observing schedule to an IVS Data Center for distribution and to the Coordinating Center for archiving.

# 19.4.3 International Laser Ranging Service (ILRS)

The International Laser Ranging Service (Pearlman et al., 2002; Pearlman et al., 2005) is an international collaboration of organizations providing data obtained by laser ranging to artificial Earth satellites or to the Moon. It is one of the services of GGOS and the ICSU-WDS. The ILRS collects, archives, and distributes observational data and provides products, including polar motion and excess length of day, coordinates and velocities of the ILRS observing sites, time-variable coordinates of the geocenter, static and time-variable models of the Earth’s gravity field, satellite ephemerides, lunar ephemerides and librations, and fundamental physical constants. An important user of this information is the IERS, where the data are of particular importance for the maintenance of the ITRF.

The ILRS observational data are obtained by its member tracking stations that range to a constellation of approved satellites and the Moon, using the most advanced laser-tracking equipment. They transmit the ranging data at least daily to one or more operations and/or data centers. These collect and merge the data from other stations in sub-networks, perform data quality checks, and reformat the data as necessary. Global data centers are the primary interfaces to the analysis centers and the outside users and they archive and provide online access to tracking data received from the operational/regional data centers. Analysis centers process tracking data from one or more data centers to produce the ILRS products operationally. At a minimum, every analysis center must process the global LAGEOS-1 and LAGEOS-2 datasets and provide Earth orientation parameters on a weekly or sub-weekly basis, as well as other products, such as station coordinates, as required by the IERS. Lunar Analysis Centers process normal point data from the Lunar Laser Ranging (LLR) stations and generate a variety of scientific products, including precise lunar ephemerides, librations, and orientation parameters, which provide insights into the composition and internal makeup of the Moon, its interaction with the Earth, tests of general relativity, and solar system ties to the ICRF.

A central bureau coordinates the activities on a daily basis, facilitating communications and information transfer within the organization and with outside users. It maintains the list of satellites approved for tracking support and their priorities, and carries out the directions of an international governing board composed of representatives of the member organizations.

# 19.4.4 International GNSS (Global Navigational Satellite Service) Service (IGS)

The International GNSS Service (Kouba et al., 1998; Beutler et al., 1999; Dow et al., 2005; Dow et al., 2009) is an international consortium of organizations that provides GNSS tracking data, orbits, and other data products in near real time. The IGS currently offers these products for two GNSS, the Global Positioning System (GPS) and GLONASS, and expects to provide similar data in the future for other systems as they become available. It is affiliated with the International Association of Geodesy, GGOS, and the ICSU-WDS.

IGS products are critical for the improvement and extension of the ITRF, monitoring of solid Earth deformations, and monitoring of polar motion. The accuracy of the monitoring station horizontal positions is $\pm 3 \mathrm { \ m m }$ , and station motion accuracy is $\pm 2 \textrm { m m }$ /year. IGS data are also used to evaluate Earth rotation and variations in sea level, ionospheric monitoring, and measuring precipitable water vapor in the atmosphere. The accuracy of the rapid polar motion data is $\pm 0 . 4$ mas, and excess length of day information is available with an accuracy of $\pm 0 . 0 1 ~ \mathrm { m s / d a y }$ .

The IGS accomplishes its objectives with an international network of more than 500 continuously operating dual-frequency GPS monitoring stations, more than 20 regional and operational data centers, four global data centers, 12 analysis centers, and a number of associate or regional analysis centers. The Central Bureau for the service maintains an Information System that provides access to IGS products. An international Governing Board oversees the services.

The monitoring stations track the satellites with high-accuracy geodetic receivers and send the tracking data to the data centers. They validate and archive the data, making it available to the other elements of the IGS and external users. The analysis centers process the data from the data centers and provide ephemerides, Earth orientation parameters, station coordinates, and clock information. An Analysis Coordinator develops analysis standards and monitors the activities of the analysis centers, providing quality control and performance evaluation. The Analysis Coordinator is also responsible for combining the output of the individual analysis centers into the single set of “official” IGS products that is sent to the global data centers for distribution. The Central Bureau coordinates the activities and operations of the service consistent with the policies set by an international directing board.

# 19.4.5 International DORIS Service (IDS)

Like the IVS, the ILRS, and the IGS, the International DORIS Service (Tavernier et al., 2006; Willis et al., 2010; Moreaux et al., 2016) provides data from an observational system related to the determination of Earth orientation parameters. DORIS is an acronym for “Doppler Orbitography and Radio-positioning Integrated by Satellite.” It is a microwave tracking system used to determine the precise location of the satellites on which it is installed. DORIS systems have been installed on 14 artificial Earth satellites. It measures the Doppler frequency shift of a radio signal transmitted from ground stations and received by the satellite. Within the IERS, the DORIS data are used primarily for the maintenance and extension of the ITRF.

The IDS, which is also a service affiliated with the IAG, the ICSU-WDS, and GGOS, collects, archives, and distributes DORIS observations that are then used to determine coordinates and velocities of the ground stations, the geocenter and scale of the Terrestrial Reference Frame, ionospheric information, high-accuracy ephemerides of DORIS satellites, and Earth orientation parameters. Its organization is much like those of the previously described organizations. The IDS coordinates an observational network made up of more than 50 ground stations along with two data centers and six analysis centers.

Web Sites of International Organizations   

<table><tr><td>Organization</td><td>Web Site</td></tr><tr><td>BIPM</td><td>www.bipm.org</td></tr><tr><td>IAG</td><td>www.iag-aig.org</td></tr><tr><td>IAU</td><td>www.iau.org</td></tr><tr><td>ICSU</td><td>www.icsu.org</td></tr><tr><td>IDS</td><td>ids-doris.org</td></tr><tr><td>IERS</td><td>www.iers.org</td></tr><tr><td>IGS</td><td>www.igs.org</td></tr><tr><td>ILRS</td><td>ilrs.cddis.eosdis.nasa.gov</td></tr><tr><td>ITU</td><td>www.itu.int</td></tr><tr><td>IUGG</td><td>www.iugg.org</td></tr><tr><td>IVS</td><td>ivscc.gsfc.nasa.gov</td></tr></table>

# References

Behrend, D. (2013). Data Handling within the International VLBI Service. Data Science Journal, 12, WDS81–WDS84, ISSN 1683–1470. doi:10.2481/dsj.WDS–011   
Beutler, G., Rothacher, M., Schaer, S., Springer, T. A., Kouba, J., & Neilan, R. E. (1999). The International GPS Service (IGS): An Interdisciplinary Service in Support of Earth Sciences. Adv. Space Res. 23, 631–635.   
Bureau International des Poids et Mesures (2006). The International System of Units (SI) (8th edn.). Paris: Bureau International des Poids et Mesures.   
Dick, W. R. & Richter, B. (2004). The International Earth Rotation and Reference Systems Service (IERS). Organizations and Strategies in Astronomy, 5. André Heck, ed., Strasbourg Astronomical Observatory, France. Astrophysics and Space Science Library 310, Dordrecht: Kluwer Academic Publishers, 159–168.   
Dow, J. M., Neilan, R. E., & Gendt, G. (2005). The International GPS Service (IGS): Celebrating the 10th Anniversary and Looking to the Next Decade. Adv. Space Res. 36, 320–326.   
Dow, J. M., Neilan, R. E., & Rizos, C. (2009). The International GNSS Service in a Changing Landscape of Global Navigation Satellite Systems. Journal of Geodesy, 83, 191–198. doi:10.1007/s00190-008–0300-3   
Guinot, B. (2000). History of the Bureau International de l’Heure. In S. Dick, D. McCarthy, & B. Luzum, eds., Polar Motion: Historical and Scientific Problems. ASP Conference Series, 208. San Francisco, CA: Astronomical Society of the Pacific, pp. 175–184.   
Kouba, J., Mireault, Y., Beutler, G., Springer, T., & Gendt, G. (1998). A Discussion of IGS Solutions and Their Impact on Geodetic and Geophysical Applications. GPS Solutions, 2, 3–15.   
Moreaux, G., Lemoine, F. G., & Capdeville, H. (2016). The International DORIS Service Contribution to the 2014 Realization of the International Terrestrial Reference Frame. Advances in Space Research, 58(12), 2479–2504.   
Pearlman, M. R., Degnan, J. J., & Bosworth, J. M. (2002). The International Laser Ranging Service. Advances in Space Research, 30, 135–143.   
Pearlman, M., Noll, C., Gurtner, W., & Noomen, R. (2005). The International Laser Ranging Service and Its Support for IGGOS. In P. Tregoning & C. Rizos, eds., Dynamic Planet: Monitoring and Understanding a Dynamic Planet with Geodetic and Oceanographic Tools. Berlin: Springer, p. 741.   
Schlüter, W. & Behrend, D. (2007). The International VLBI Service for Geodesy and Astrometry (IVS): Current Capabilities and Future Prospects. Journal of Geodesy, 81 (6–8), 379–387.   
Schuh, H. & Behrend, D. (2012). VLBI: A Fascinating Technique for Geodesy and Astrometry. Journal of Geodynamics, 61, 68–80. doi:10.1016/j.jog.2012.07.007.   
Tavernier, G., Fagard, H., Feissel-Vernier, M., Le Bail, K., Lemoine, F., Noll, C., Noomen, R., Ries, J. C., Soudarin, L., Valette, J. J., & Willis, P. (2006). The International DORIS Service: Genesis and Early Achievements. In DORIS Special Issue, P. Willis ed. Journal of Geodesy 80, 403–417.   
Willis, P., Fagard, H., Ferrage, P., Lemoine, F. G. . . . Valette, J. J. (2010). The International DORIS Service (IDS): Toward Maturity. Advances in Space Research, 45(12), 1408–1420.

20

# Time Applications

# 20.1 Time Enables the Infrastructure

The infrastructure of modern society depends critically on time and frequency services. We have grown to expect the universal convenience of time and frequency just as we expect the accessibility of electrical power and water services. However, the users of these services are often not aware of the fact that they play such important roles in their lives. Requirements for time and frequency with widely varying precision and accuracy exist in the areas of utility services, banking and finance, emergency services, communications, navigation, inventory control, environmental services, transportation management, surveying, agriculture, and recreation, as well as in scientific and technical applications.

# 20.2 Positioning and Navigation Services

The advent of Global Navigation Satellite Systems (GNSS), such as the Global Positioning System (GPS), GLONASS, and GALILEO, has not only provided users an easily accessible source of positioning, navigation, and timing information on a global scale, but it has also imposed new requirements on the providers of time and frequency. Synchronized timing signals are critical to the operation of these systems. (See Chapter 18.) The fact that a timing error of one nanosecond is roughly equivalent to an error of $3 0 \mathrm { c m }$ , or one foot, in position means that accurate positioning and navigation requires very precise timing information.

The requirements for timing are, in part, driven by the positioning and navigation applications of the GNSS signals. In addition to the military applications for which GPS was originally intended, these applications now include operation of emergency responders, location of transportation services such as trucks and trains, ship navigation, air traffic control, geodetic land surveys, earthquake monitoring, agricultural and fishing applications, and identification and location of inventory items,


<!-- chunk 0006: pages 351-402 -->
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
