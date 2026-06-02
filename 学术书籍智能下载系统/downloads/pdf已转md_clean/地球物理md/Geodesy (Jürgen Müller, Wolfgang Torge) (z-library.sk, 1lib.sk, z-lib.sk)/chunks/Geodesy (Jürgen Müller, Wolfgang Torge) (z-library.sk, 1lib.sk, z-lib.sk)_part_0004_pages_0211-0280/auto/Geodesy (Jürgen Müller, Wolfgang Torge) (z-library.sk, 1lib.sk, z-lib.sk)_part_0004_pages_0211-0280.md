![](images/d2e04dcfab298633f90fa9f6307d529496245b11111ebd3117eaeaddf659339e.jpg)  
Fig. 5.73: Gravimetric Earth tide record, obtained with LaCoste and Romberg gravimeter G298, Institut für Erdmessung (IfE), University of Hannover.

![](images/affa2c0e7f5a3954f0197a65cf8b48bc362b61c0ff8588e8dde2d9e8a39832b2.jpg)  
Fig. 5.74: Superconducting gravimeter principle, after GWR-Instruments information.

![](images/7e7ac396689f6e7c1332c3f181b307a8a5c2cde4c20e5eb5fa592f4cf94008b3.jpg)  
Fig. 5.75: OSG Observatory Superconducting Gravimeter view, courtesy of GWR-Instruments Inc., San Diego, CA, U.S.A.

of $4 . 2 ~ \mathsf { K }$ . The superconducting cylinder provides a primary shielding from the Earth’s magnetic fi eld, supported by an additional $\mu { \cdot }$ -metal shield on the outside of the vacuum case. The measuring system is kept in an insulating dewar vessel (Fig. 5.75). An automatic leveling system (two orthogonally mounted tiltmeters and two levelers under the dewar) provides an alignment better than 1 μrad.

![](images/69041dea2b30cdf97007000990a4bb6ff3175ee506bd63634db4224265ae3d9e.jpg)  
Fig. 5.76: GWR superconducting gravimeter drift, with (top to bottom) raw gravimeter signal, Earth tides reduced signal, atmospheric pressure and gravity residuals after removal of Earth tides and atmospheric pressure effects, courtesy GWR-Instruments, Inc., San Diego, CA, U.S.A.

The instrumental drift of a superconducting gravimeter is very small (on the order of $1 0 \ \mathrm { n m s ^ { - 2 } / a } )$ , and may be modeled for the fi rst months of observation by an exponential function, followed by a linear trend (Van Camp and Francis, 2007), Fig. 5.76. Absolute gravity measurements can be used to control the drift at longer time intervals. From tidal analysis, a noise level of $< 0 . 0 1 \ \mathrm { n m s } ^ { - 2 }$ (frequency domain) and $< 1 \mathsf { n m s } ^ { - 2 }$ (time domain) has been found for superconducting gravimeter results (Hinderer et al., 2009; Neumeyer, 2010).

The superconducting gravimeter was introduced by Prothero and Goodkind (1968) and commercially manufactured since the 1980s by GWR Instruments. Systematic investigations at several institutions, e.g., at the Observatoire Royal de Belgique, Brussels, and the Bundesamt für Kartographie und Geodäsie, Frankfurt a.M. (Richter, 1987) led to continuous improvements. This includes the reduction of the instrument’s size, the increase of the time interval for helium refi lling (a closed cycle cooling system will make the refi lling practically superfl uous), and the development of a dual-sphere instrument in order to detect instrumental offsets (“tares”).

A global project of gravity recording with superconducting gravimeters (Global Geodynamics Project GGP) has been launched in 1991, and started operation in 1997. Today the net comprises about 20 stations, which continuously record gravity and provide the raw data decimated to 1 minute samples (Fig. 5.77). The results serve for improving Earth and ocean tidal models and for investigating a multitude of geodynamic phenomena, and are used as ground truth for gravimetric space missions, cf. [5.2.8], Crossley and Hinderer (2010). The GGP data are included in the data bank for tidal gravity measurements which is maintained at the International Centre for Earth Tides, it contains the tidal gravity data (hourly values) of about 360 stations (Melchior, 1994).

Calibration of a recording gravimeter is performed by relative and absolute methods. A relative calibration is realized by parallel registration with a “calibrated” gravimeter or by recording on a station with well-known tidal parameters. Absolute calibration procedures include the artifi cial periodic acceleration on a vertically moving platform, the controlled vertical displacement of large external masses, and the parallel registration with an absolute gravimeter. Concentrating now on the superconducting gravimeter, the latter method is often used now, achieving a calibration precision of about $0 . 0 5 \%$ (Tamura et al., 2005). An even better precision has been obtained at the moving platform calibration, while the accuracy of the relative methods is limited to a few $0 . 1 \%$ (Richter et al., 1995; Francis, 1997). The instrumental phase shift is determined by recording the gravimeter’s response to a defi ned impulse (step response method), Van Camp et al. (2000).

![](images/33974fc3c8a92ffcbd0df86ac33f40b87b5cec16d478fead58de7efc47ce889f.jpg)  
Fig. 5.77: Global Geodynamics Project: station distribution, status 2010 (Hinderer et al., 2009), courtesy GGP Website (http://www.eas.slu.edu/GGP/ggphome.html)

The gravity signal is strongly correlated with atmospheric pressure. A linear regression with local air pressure (between $- 2 . 5$ and $- 3 . 5 \ \mathrm { \ n m s ^ { - 2 } / h P a } )$ reduces the main part of this effect, see (5.81b), also Fig. 5.76. More refi ned models are available which also take the air pressure around the station and the elastic response of the Earth’s crust into account (Merriam, 1992; Gitlein and Timmen, 2007; Kroner et al., 2007). Variations of groundwater level and precipitation also affect the gravity record and may reach the order of some $1 0 \ \mathrm { n m s } ^ { - 2 }$ , but they are diffi cult to model (Virtanen, 2000), cf. also [8.3.1].

Longer (several months and more) gravity records can be subjected to a tidal analysis (Wang, 1997; Agnew, 2009). This dedicated analysis is already introduced here, as the tidal frequencies for a rigid Earth are extremely well known, cf. [3.5.2], in contrast to the majority of other geodynamic phenomena, cf. [8.3.6]. The analysis is based on the spectral decomposition of the observed signal into a number of partial tides. By comparing the observations (hourly samples, atmospheric pressure effects reduced) with the gravimetric tides for a rigid Earth, deviations in amplitude and phase are found, which depend on the Earth’s elastic response to the tidal forces (Earth and ocean tides). For the partial tide $i ,$ this is expressed by the amplitude factor (also gravimetric factor)

$$
\delta _ { i } = A _ { _ i } \left( \mathrm { o b s } \right) : A _ { _ i } \left( \mathrm { t h e o r } \right)
$$

and the phase shift

$$
\Delta \Phi _ { i } = \Phi _ { i } ( \mathrm { o b s } ) - \Phi _ { i } ( \mathrm { t h e o r } ) ,
$$

where $A _ { i }$ is the observed resp. calculated (solid Earth) amplitude, and $\Phi _ { _ i }$ the corresponding phase. The observation equation for a least-squares spectral analysis then reads

$$
I ( t ) = \sum _ { i = 1 } ^ { n } \delta _ { i } A _ { i } \left( \mathrm { t h e o r } \right) \cos { \left( \omega _ { i } t + \Phi _ { i } \left( \mathrm { t h e o r } \right) + \Delta \Phi _ { i } \right) } ,
$$

with $I ( t )$ being the recorded gravity value at time $t ,$ and $\Phi _ { _ i } = 2 \pi T _ { _ i }$ the circular frequency ( $T _ { _ i }$ is the period) for the partial tide $\boldsymbol { i }$ (Wenzel, 1976, 1997a). As a fi rst approximation, a gravimetric factor of $\delta \mathrm { = } 1 . 1 6$ and a phase lag of zero may be introduced for the reduction of gravity data, but more sophisticated gravimetric tidal models are available. This will be discussed in [8.3.6], together with the relation of the gravimetric factor to the Love numbers describing the reaction of the elastic Earth to tidal forces and loads.

Elastic spring gravimeters allow the determination of 10 to 20 partial tides (mainly diurnal, semi-diurnal, ter-diurnal), with an observation time of 4 to 6 months. Superconducting gravimeters can resolve up to 40 tides (including semi-annual and annual) by registration over several years. The gravimetric factor for polar motion has also been derived from long-term series. As an example, a 158 days registration with a LaCoste and Romberg feedback gravimeter at Hannover $\varphi = 5 2 . 3 8 7 ^ { \circ } \mathsf { N } ,$ $\lambda = 9 . 7 1 3 ^ { \circ } \mathsf { E } _ { \iota }$ , $H = 5 0 ~ \mathrm { m } )$ ) yielded for the lunar diurnal tide O1 (Timmen and Wenzel, 1994a):

$$
\delta ( \mathrm { O 1 } ) = 1 . 1 5 1 \pm 0 . 0 0 1 , \Delta \Phi ( \mathrm { O 1 } ) = 0 . 1 6 ^ { \circ } \pm 0 . 0 8 ^ { \circ }
$$

and for the semi-diurnal tide ${ \cal M } 2$

$$
\delta ( M 2 ) = 1 . 1 8 8 \pm 0 . 0 0 0 5 , \Delta \Phi ( M 2 ) = 1 . 7 0 ^ { \circ } \pm 0 . 0 3 ^ { \circ } .
$$

The factor for O1 is close to the observed global value 1.155, while the M2 result differs due to ocean load and attraction, cf. [8.3.6].

# 5.5 Terrestrial geodetic measurements

Terrestrial geodetic measurements determine the relative position of points on the Earth’s surface, and generally use electromagnetic waves for deriving geometric quantities between them. The majority of the observations refers to the local vertical, and thus delivers results orientated in local gravity related astronomic systems. The measurement of horizontal and zenith angles [5.5.1] and of distances [5.5.2] allows relative threedimensional positioning. Combined instruments (total stations) are now generally used, and even integrated with absolute GNSS positioning. Inertial surveying applies acceleration measurements, and seafl oor positioning uses acoustic waves, for positioning under special environmental conditions [5.5.3]. Precise height differences are provided by leveling, which again refers to the Earth’s gravity fi eld [5.5.4]. Strain and tilt measurements serve for detecting local changes of distances and inclination with time [5.5.5].

Due to the high accuracy and economy of satellite-based positioning techniques, terrestrial geodetic measurements are used primarily for interpolating satellite-derived results or in areas where satellite methods fail or need terrestrial support. This includes underground and underwater positioning, surveys in forests and in urban areas, engineering surveys, and monitoring of local geodynamic processes.

Terrestrial methods are treated in textbooks on surveying, e.g., Anderson and Mikhail (1998), Bannister et al. (1998), Johnson (2004), Kahmen (2006). Classical surveying instruments are described by Deumlich (1982), while a more recent state is dealt with in Deumlich and Staiger (2002) and Joeckel et al. (2008). Kahmen (1978) and Schlemmer (1996) concentrate on the fundamentals of electronics employed in geodetic instruments, and Brunner (1984b) deals with the effects of atmospheric refraction.

# 5.5.1 Horizontal and vertical angle measurements

The horizontal angle is defi ned as the angle measured in the horizontal plane of the local astronomic system between two vertical planes. It is formed by the difference in horizontal directions to the target points which defi ne the vertical planes. The vertical angle is the angle measured in the vertical plane between the horizontal plane and the direction to the target point. The zenith angle (also zenith distance), being the complement to $9 0 ^ { \circ } .$ , is often introduced instead of the vertical angle, cf. [2.5].

A theodolite is used for measuring horizontal and vertical angles. The principal components of this instrument are a horizontal and a vertical circle with graduation, a telescope capable of being rotated about the vertical and the horizontal axes, and a mechanism for reading the circles. In order to orientate the theodolite with respect to the plumb line direction, it is equipped with spirit or electronic levels.

Regarding the reading of the circle graduation, we distinguish between optical and electronic or digital theodolites.

Optical theodolites of highest precision were developed since the second half of the eighteenth century and were then used until the 1960s for fi rst order triangulation (with the Kern DKM3 and the Wild T3 theodolites being the latest developments) at station distances of 30 to $6 0 ~ \mathrm { k m }$ , cf. [7.1]. They were characterized by very stable construction and circle diameters of 100 to 250 mm. Circle graduation errors were less than $0 . 5 ^ { \prime \prime } ,$ and reading accuracy reached $0 . 1 ^ { \prime \prime }$ by using a coincidence microscope with micrometer screw. The lens aperture of the telescope was 60 to $7 0 ~ \mathrm { m m }$ , and the magnifi cation 30 to 40 or more. Standard deviations of $0 . 2 { ^ { \prime \prime } }$ to $0 . 4 ^ { \prime \prime }$ have been achieved for an adjusted horizontal direction

Today, horizontal and vertical angles are measured only over shorter distances reaching from a few meter to about one and eventually up to $1 0 \mathrm { k m } ,$ , at engineering projects, geodetic network densifi cation, and local geodynamic control. Electronic theodolites (lens aperture 30 to $4 5 \ \mathsf { m m }$ , magnifi cation of 30 or more) are employed for this purpose, they have superseded the optical analogue instruments. Generally, the electronic theodolite is combined with a distance meter to produce a total station, cf. [5.5.2], but “pure” theodolites still fi nd application at industrial surveys (Fig. 5.78).

The horizontal and vertical circles (circle diameter 60 to $7 0 \ \mathrm { m m }$ ) of an electronic theodolite are either coded (with code signals arranged on concentric circles) or carry an incremental graduation (bright/dark changes). Reading is microprocessor-controlled and performed by optical-electronic scanning and subsequent interpolation (electronic micrometer). Electronic levels are used as tilt sensors, they are based on the refl exion of light at the surface of a fl uid and measure the refl ected light point’s position by means of a CCD array. A dual-axes compensator serves for automatic leveling the instrument (measuring range about $5 ^ { \prime \prime }$ , precision $0 . 3 \dots 0 . 5 ^ { \prime \prime } )$ ; a residual tilt correction may also be applied automatically. Collimation and horizontal axis errors are either eliminated by measurement at both positions of the telescope or corrected internally. For the measurement of vertical angles, the theodolite is equipped with a reading index for the vertical circle. By leveling the index either manually (spirit level) or automatically (electronic level) the readings are referred to the local vertical, with an accuracy of a few $0 . 1 ^ { \prime \prime }$ . With electronic theodolites an accuracy of $0 . 5 ^ { \prime \prime }$ to $2 ^ { \prime \prime }$ is obtained for observed angles.

![](images/95f61d8a81c2e717c5cf411ce0e5bd3ecff44cba3d382d5979673a1636cb56e7.jpg)  
Fig. 5.78: Industrial Theodolite (Leica TM6100A), courtesy Leica Geosystems AG, Heerbrugg, Switzerland

![](images/c1419250b051a90e67bb3957b04584257680f93b6f427e6ea4a14fbc6955cc0b.jpg)  
Fig. 5.79: Gyrotheodolite (Gyromat 3000 with Leica TM5100 Theodolite), courtesy Deutsche Montan Technologie (DMT), Essen, Germany.

Gyrotheodolites have been developed for the determination of astronomic azimuths by combining a theodolite with a gyroscope. The principle of the gyroscope is based on the fact that a rapidly rotating gyro with horizontal spin axis swings into the north direction due to the combined effects of the gyro’s spin, the Earth’s gravity, and the Earth’s rotation. An accuracy of $3 ^ { \prime \prime }$ can be obtained by an automatic measurement procedure (20 individual measurements), within a time span of $1 0 \ \mathrm { m i n }$ . Gyrotheodolites are employed primarily for mining and tunnel surveys (Lienhart and Brunner, 2004), Fig. 5.79.

Ray bending by terrestrial refraction is an error source which may pose special problems, cf. [5.1]. The effect of lateral refraction on horizontal angles generally can be neglected, but may reach the arcsec order of magnitude under unfavorable circumstances, e.g., if the light ray is closely passing a hill. Extended classical triangulation networks partly suffer from this effect which is diffi cult to model. Further processing of vertical angles, on the other hand, always requires the consideration of errors due to vertical refraction.

The refraction angle depends on the coeffi cient of refraction and thereby on the meteorological conditions along the path of light, particularly the vertical gradient of temperature, cf. [5.1.2]. Generally, a traditional value for the refraction coeffi cient (e.g., $k = 0 . 1 3 ,$ ) is introduced in order to reduce the effect of vertical refraction, more actual values for the refraction coeffi cient can be derived from meteorological data taken at the endpoints of the observation line. These strategies easily may lead to a vertical angle error of a few arcsec and more. The effect of this error on the height difference increases with the square of the distance and thus reaches the order of a few decimeters already over a few km. The error of the observed zenith angle, on the other hand, only propagates with distance and thus remains at the order of a few cm. An approximately symmetric behavior of refraction is to be expected for simultaneous observations at the endpoints, especially with cloudy weather and prior to the isothermal conditions of the evening and if the light ray is more than 15 to $2 0 ~ \mathsf { m }$ above the ground. The uncertainty of the refraction angle then remains less than $1 ^ { \prime \prime }$ for distances below 10 to $2 5 ~ \mathrm { k m }$ . This has led to the method of observing reciprocal-simultaneous zenith angles, cf. [6.4.2].

For the direct determination of the refraction angle, attempts have been made to utilize the dispersion of the light, cf. [5.1.1]. Here, two different wavelengths are used for observation which causes a difference between the two angles of refraction at the target point. The dispersion angle is proportional to the refraction angle but about two orders of magnitude smaller which requires a measuring accuracy of a few $0 . 0 1 ^ { \prime \prime }$ . Corresponding experiments at distances less than $2 0 ~ \mathrm { k m }$ gave uncertainties of 1 to $2 ^ { \prime \prime }$ for the refraction angle (Williams and Kahmen, 1984).

# 5.5.2 Distance measurements, total stations

Terrestrial distance measurements have played and still play an important role for positioning. They provide geometric relations between neighboring control points, and they have also established the scale of classical geodetic networks.

Until about 1960, the scale of triangulation networks, constructed from angle measurements, was derived from baselines having lengths of 5 to $1 0 \mathrm { k m }$ . Measuring rods and, since about 1900, wires or tapes served to measure the base line length. With the Jäderin (1880) method, freely hanging invar (NiFe alloy) wires $2 4 ~ \mathsf { m }$ in length were used, characterized by a small coeffi cient of thermal expansion. The relative accuracy of the more recent base lines amounts to ${ { 1 0 } ^ { - 6 } } ,$ which corresponds to $1 ~ \mathrm { m m / k m }$ . For fi eld calibrations of wires and tapes, several international calibration lines were established by interferometric methods. Starting from the length of a standard meter, the Väisälä light interference comparator provided an optical multiplication up to base line lengths of $8 6 4 \mathrm { ~ m ~ }$ (relative accuracy $1 0 ^ { - 7 } )$ .

Electromagnetic distance measurements started at the end of the 1940s. They may either use light waves $\lambda = 0 . 4$ to $0 . 8 \mu \mathrm { m }$ ) and the near infrared (up to $\lambda = 1 ~ { \mu \mathrm { m } } )$ ) or microwaves $\lambda = 1$ to $1 0 ~ \mathrm { c m }$ ) as carriers of the measuring signal (Rueger, 1997; Joeckel et al., 2008). Microwaves are hardly absorbed by the atmosphere and allow the measurement of large distances ( $5 0 ~ \mathrm { k m }$ and more) even under unfavorable weather conditions. The effect of humidity on refraction, on the other hand, is big and may signifi cantly deteriorate the results. Distances measured by light waves are about one order of magnitude more accurate, but the measurement range depends on visibility, and is eventually strongly limited by disturbances through clouds, haze, or fog, cf. [5.1.2].

The travel time $\Delta t$ of the signal serves as a measure for the distance $S _ { \prime }$ according to the relation

$$
s = v \Delta t \mathrm { a n d } \ v = { \frac { c } { n ^ { \prime } } }
$$

with $V$ being the actual velocity of the electromagnetic waves, $C$ the velocity in vacuum, and $n$ the index of refraction, cf. [5.1.1]. Time measurement is performed by the pulse or the phase comparison method, where we have to distinguish between electro-optical and microwave distance meters.

For electro-optical distance measurements, the transmitting and the receiving unit are combined in one instrument, and a refl ector (prism) is posted on the target station (refl ectorless measurements are also possible over limited distances). At the pulse method, the transmitter emits a pulse which after refl ection is observed at the receiver. An electronic timer measures the time $\Delta t$ that the signal requires to travel forth and back along the distance $s$ leading to

$$
s = \frac { v } { 2 } \Delta t .
$$

If the uncertainty in distance is to remain less than $1 \ \mathrm { m m }$ , the time of propagation must be obtained to an accuracy better than 0.01 ns. This high accuracy demand can be fulfi lled by short (a few ns) laser pulses, electronic counting controlled by a reference oscillator, and averaging the results of a large amount of individual measurements.

A similar instrumental arrangement is used for the phase comparison method. A high-frequency carrier wave is produced by a laser diode, and modulated continuously (amplitude or frequency modulation), with modulation frequencies between about 10 and $1 0 0 ~ { \cal M } { \sf H } z$ . The corresponding half wavelength (because of the double distance traveled by the signal) serves as a “yard stick” (about 1 to $1 0 ~ \mathrm { m } )$ ) in surveying the distance. After transmission and refl ection, the phase shift $\Delta \varphi$ between the emitted and the received signal is measured by a phase meter (Fig. 5.80). It represents the residual part of the distance above an integral number $N$ of complete wavelengths, which is determined automatically by applying several slightly different modulation frequencies generated by frequency division. With a digital phase detector and a microprocessor, the measuring process can be fully automatized; the resolution achievable is ${ { 1 0 } ^ { - 3 } }$ to ${ \mathsf { 1 0 } } ^ { - 4 } ,$ , which corresponds to a $" \mathrm { m m } ^ { \prime \prime }$ -precision.

Travel time $\Delta t$ and phase shift $\Delta \varphi$ are related through

$$
\Delta t = \frac { N + \displaystyle \frac { \Delta \varphi } { 2 \pi } } { f } ,
$$

where $N$ is the number of complete periods, and the modulation frequency

$$
f = \frac { V } { \lambda } = \frac { C } { n \lambda } ,
$$

![](images/9a7578a02221accdc2cffa3862fb23f87137a8c85459d51bf970ec9d3309474d.jpg)  
Fig. 5.80: Phase comparison method principle (electro-optical distance measurement).

with the group refractive index $n$ (5.13) and the wavelength $\lambda .$ . Substituting (5.104) and (5.105) into (5.103b) delivers the distance

$$
s = \frac { \lambda } 2 \left( N + \frac { \Delta \varphi } { 2 \pi } \right) .
$$

With the residual part of a wavelength

$$
\Delta \lambda = \frac { \Delta \varphi } { 2 \pi } \lambda ,
$$

the distance can also be expressed by

$$
s = N \frac { \lambda } { 2 } + \frac { \Delta \lambda } { 2 } .
$$

Terrestrial microwave distance measurements differ from the optical method by the separate setting up of transmitter/receiver-units (combining master and remote function in one instrument) at the end points of the distance to be measured, both units are equipped with an antenna for sending and receiving the signals. The phase comparison method has been applied generally. Here, the emitted signal is received at the remote station, where it is demodulated and amplifi ed. After superimposing on the remote station’s carrier wave, the signal is sent back to the master station. Demodulation and comparison with a reference signal (phase measurement) delivers the phase shift, and again the use of different modulation frequencies allows a unique solution. At the pulse method the receiver has to include a correlator for measuring the travel time, while a one-way measurement would require precise clocks on both stations. The evaluation then would follow (5.103a), and apply modifi ed formulas (5.106) and (5.108).

The calibration of electronic distance meters includes the control of the modulation frequency by a temperature-stabilized frequency meter and the determination of the instrumental constants (zero point correction and possible cyclic errors) on a comparator or on a short (about $1 \ \mathrm { k m } ^ { \prime }$ ) calibration line. Calibration lines are usually partitioned into several sections and determined by laser interferometry or with a short-range distance meter of high precision.

Terrestrial microwave distance measurements started with the development of the tellurometer by T. L. Wadley (1956). Here, the master station emitted a modulated (modulation frequencies between 7.5 and $1 5 0 ~ \boldsymbol { M } \boldsymbol { \ H } \boldsymbol { z } )$ carrier wave $( \lambda = 8 ~ \mathrm { m m }$ to $1 0 \ \mathrm { c m } ,$ ), which was retransmitted from an active transponder (receiver and transmitter). Measurement of ranges up to $1 0 0 ~ \mathrm { k m }$ and more were obtained. The accuracy strongly depended on refraction uncertainties and could reach $1 0 \dots 1 5$ $\mathsf { m m } + 3$ ppm (ppm is relative to distance). Electro-optical distance measurements trace back to the fi rst geodimeter developed by E. Bergstrand (1948). Long-range distance meters used laser light (He-Ne gas laser) with modulation frequencies between 15 and $5 0 ~ \mathsf { M H z }$ and were able to measure distances up to $6 0 ~ \mathrm { k m }$ on clear days, with an accuracy of $1 \ldots 5 \ \mathrm { m m } + 1 \ldots 2 \ \mathrm { p p m }$ . Long-range microwave and electro-optical distance measurements have been carried out extensively from the 1950s to the 1980s. The measurements were primarily for establishing fi rst order control networks and for strengthening existing horizontal control, cf. [7.1].

Long-range distance measurements have become obsolete, as large-scale positioning is carried out nowadays almost exclusively by satellite methods; and terrestrial microwave distance measurements are no longer carried out at all. Microwave range and range rate measurements between satellites and ground stations, on the other hand, play an outstanding role for positioning and navigation on Earth and in space, cf. [5.2.5], [5.2.7].

Today, terrestrial distance measurements concentrate on distances less than one km, ranges of a few km are rarely exceeded. Visible light and near infrared are used, either in the pulse or in the phase comparison method. Separate distance meters have been available for special applications (partly suitable to be mounted on a theodolite), but generally electronic total stations are employed, providing distances, horizontal directions and zenith angles by combining a theodolite with a distance meter.

The measuring range of a distance measuring unit incorporated in a total station depends on the number of prisms posted on the target station. With one prism, distances up to $3 ~ \mathrm { k m }$ can be observed, and the measurement range can be extended to about $6 \mathrm { k m }$ (three prisms) and $9 ~ \mathrm { k m }$ (nine prisms), respectively. The error budget of the distance measurements contains a constant part that depends on uncertainties in timing or phase measurement and on the zero point stability. It is augmented by a distance dependent part which is determined by errors of the modulation frequency and by refraction effects. Generally, an accuracy of $3 \dots 5 \ : \mathrm { m m } + 1$ ppm can be achieved with electro-optical distance meters, within a measuring time of a few seconds. The refl ectorless mode allows ranging up to more than one km, with accuracies of $2 \ldots 1 0 \ : \mathrm { m m } + 2$ … 10 ppm, depending on material and structure of the refl ecting surface.

When integrated into a total station, the microprocessor-controlled operation in addition to distance measurement also provides automatic prism search, automatic leveling, and the measurement of horizontal directions and zenith angles. Further processing includes data storage in the internal memory, calibration, and application of refraction corrections with standard or actual meteorological data, as well as the transformation from local polar to Cartesian coordinates (Feist et al., 1998). High fl exibility is given through the control unit in connection with a graphic display, and especially by the interchange of individual modules. Of special importance is the modular connection or the integration of GNSS units (antenna and receiver). The latter strategy allows precise absolute positioning through real time kinematic methods, cf. [5. 2.5], and consequently the transformation of the local results to a global reference. Examples for total stations are given in Figs. 5.81 to 5.83.

While refraction effects have played an important role at long-range distance meas urements, they are of less importance at shorter distances usually observed today. Nevertheless, refraction corrections still have to be applied in order to achieve high accuracy at terrestrial distance measurements.

The meteorological parameters needed for modeling the corrections, cf. [5.1.2], generally are measured only at the instrument and at the target point, and the arithmetic mean is introduced with the refraction reduction. This value may not be representative for the entire distance, and thus a limiting factor for precise distance measurements is set (Iliffe and Dodson, 1987). It also must be noted that measurements conducted under the same atmospheric conditions may be highly correlated, but this correlation can be signifi cantly reduced if observations are carried out under different conditions.

![](images/8b222ac8c987f8d02c77f52740b9959c137ec4abb93bcc22b7acbcfb57061260.jpg)  
Fig. 5.81: Total station (Spectra Precision Focus 8), courtesy Spectra Precision, Westminster, CO, U.S.A.

![](images/5b029f6db12f2c78bdf61f8fcb4ae3cdf6feeefe08f3c6d8306bba3fa0ec3012.jpg)  
Fig. 5.82: Total station (Trimble S8), courtesy Trimble Navigation Ltd., Sunnyvale, CA, U.S.A.

![](images/63eeec647d72949deb9b0b406ea100faf9ad30a21a98f63830c3a5c50ab8a9da.jpg)  
Fig. 5.83: Total station with integrated GNSS (Leica Smartstation TPS1 $2 0 0 +$ ), courtesy Leica Geosystems AG, Heerbrugg, Switzerland.

The refraction corrections which have to be applied to the observed distances before further processing can be split up into three parts (Höpcke, 1966). The distance $\overline { { S } } _ { 0 }$ read on the instrument is based on a standard value $n _ { \mathrm { { o } } }$ for the refractive index calculated from standard temperature and air pressure (5.17). If a more realistic value $\overline { { n } }$ is available from local meteorological measurements, the relation

$$
\overline { { s } } \overline { { n } } = \overline { { s } } _ { \mathrm { o } } { n _ { \mathrm { o } } }
$$

provides a fi rst velocity correction

$$
k _ { _ n } = \overline { { s } } ( n _ { _ 0 } - \overline { { n } } ) .
$$

As seen from (5.20a), the radius of the light curve differs from the Earth’s radius $r \approx 8 ~ R$ ). Hence, the light passes through atmospheric layers with a larger refractive index than the mean value ${ \overline { { \boldsymbol { n } } } } ,$ , calculated from the endpoint data only. With (5.10) and the coeffi cient of refraction $k = 0 . 1 3$ , we obtain

$$
\frac { d n } { d h } = - \frac { k } { R } = - 2 0 \times 1 0 ^ { - 6 } / \mathrm { k m } ,
$$

which can be used to derive a second velocity correction

$$
k _ { { } _ { \Delta n } } = - ( k - k ^ { 2 } ) \frac { \overline { { s } } ^ { 3 } } { 1 2 R ^ { 2 } } .
$$

This correction is less than $1 \mathsf { m m }$ over a distance of $1 5 \mathrm { k m }$ and can be neglected generally. For three-dimensional computations, the chord distance $s$ is required. By assuming a spherical arc with radius $r$ we have

$$
s = 2 r \sin \frac { \bar { s } } { 2 r ^ { \prime } } ,
$$

or after a series expansion

$$
s = 2 r \left( \frac { \bar { s } } { 2 r } - \frac { 1 } { 6 } \left( \frac { \bar { s } } { 2 r } \right) ^ { 3 } + \ldots \right) .
$$

Introducing (5.10) yields the curvature reduction

$$
k _ { _ { r } } = - k ^ { 2 } \frac { \bar { s } ^ { 3 } } { 2 4 R ^ { 2 } } ,
$$

which is part of the reduction formula (5.6). This reduction is less than $0 . 1 \mathrm { \ m m }$ for a distance of $1 5 ~ \mathrm { k m }$ and can be neglected. By adding (5.110) to (5.112), we obtain the total reduction from the observed distance to the chord:

$$
s - \bar { s } _ { { } _ { 0 } } = \bar { s } ( n _ { { } _ { 0 } } - \bar { n } ) - \frac { 2 k - k ^ { 2 } } { 2 4 R ^ { 2 } } \bar { s } ^ { 3 } .
$$

The reduction from the chord distance to the length of the normal section and the geodesic on the ellipsoid will be given in [6.3.2].

Special distance meters have been developed in order to measure shorter distances with very high precision, as required for calibration lines and for geodetic surveying, and for monitoring related to engineering projects and to geodynamic control networks. These developments are based either on instrumental refi nements and better determination of the refraction effects or on the use of two or three different wavelengths.

The Kern Mekometer ME 5000 uses a He-Ne laser as a light source, with a polarization modulated wavelength of $0 . 6 ~ \textrm { m }$ (Meier and Löser, 1986), Fig. 5.84. The modulation frequency $( 5 0 0 ~ M { \sf H z } )$ is automatically adjusted by means of a cavity resonator compensated for temperature change, such that the distance becomes an integer number of wavelengths. Distances of a few km can be measured with instruments of this type, and an accuracy of $0 . 1 . . . 0 . 2 \ m \ m \ + \ 0 . 2$ ppm may be obtained, where residual refraction effects still play an essential role (Rueger and Cidder, 1987).

If the distance is measured with different wavelengths, the dispersive effect of air for visible light can be exploited, cf. [5.1.1]. The difference in the distances obtained with “blue” and “red” light particularly depends on the infl uence of temperature and atmospheric pressure on the index of refraction. If an additional microwave measurement is performed, the effect of humidity is refl ected in the difference between the microwave and the light results. From (5.14), (5.15), (5.17), and (5.18), a relation between the geometric length of the path and the light and microwave results can be established, where a resolution of a few $0 . 0 1 \ \mathrm { \ m m }$ is required. We mention the Terrameter as an realization of this strategy, which has been developed as a two-wave laser-instrument to measure distances up to $1 0 ~ \mathrm { k m }$ with a precision of better than $0 . 1 \mathrm { \ m m }$ , and which has been applied to measure crustal strain rates in California (Huggett, 1981).

![](images/72cadf8b3ab92479631ad2365346226f8f896d0be496b34c4e716834254638ee.jpg)  
Fig. 5.84: Distance meter Mekometer ME 5000, Leica Geosystems AG, Heerbrugg, Switzerland. IfE, Leibniz Universität Hannover.

# 5.5.3 Inertial surveying, underwater acoustic positioning

In the following we shortly describe two measurement methods which are not based on electromagnetic waves but use different physical signals for positioning: Inertial surveying and underwater acoustic positioning. The application of these methods is limited to areas where GNSS or classical terrestrial instruments fail or face severe problems, but GNSS techniques are generally integrated in order to strengthen the results and to connect them with the global geodetic reference frame.

Inertial positioning is based on measurements with an inertial navigation system (INS, also inertial survey system) carried on a vehicle moving in space (car, helicopter, ship, submarine, airplane, spacecraft). INSs have been originally developed for autonomous navigation in aviation and missile guidance, and found wide application in space and marine (especially submarine) navigation (Salychev, 1998; Jekeli, 2001a). An INS consists of two sensor sets mounted on a common platform (body frame) and a computer. The platform may be gyro-stabilized or body-fi xed (strap-down method). The sensors are the accelerometers measuring the (linear) velocity rates of the platform, and gyros providing the orientation of the accelerometers by monitoring the angular rates of the accelerometer frame with respect to the local level resp. inertial frame (cf. [4.1.3]); accelerometers and gyros are arranged at three mutually perpendicular axes.

The evaluation of the INS outputs is based on Newton’s second law of motion, extended by the effect of gravity. The fundamental observation equations (5.96) thus can be solved either for gravity or for position. Solving for gravity leads to kinematic gravi metry and presupposes an independent determination of the moving vehicle’s kinematic acceleration, e.g., by GNSS methods, cf. [5.4.4]. By introducing gravity values derived from a model (ellipsoidal normal gravity fi eld, global gravity fi eld model)

or from local gravity data, on the other hand, the observation equations can be solved for the platform’s acceleration. Starting from an initial point with known position and velocity, the updated position and velocity is then continuously computed by single resp. double integration with time. This method of inertial surveying thus offers the possibility of a nearly continuous positioning, which, in principle, works independently of an external reference (Cross, 1985; Schwarz, 1986). The simultaneous evaluation of the INS/DGNSS data streams for the vehicle’s trajectory and the gravity disturbance along its path may offer some advantage, but is generally avoided. This is due to the strongly different functional and stochastic (error) models to be applied for positioning and gravity determination (Schwarz, 2006), see below and [5.2.5].

Inertial surveying started in the 1970s, with a fi rst commercial geodetic inertial survey system developed by Litton Guidance and Control Systems. Other local-level or space-stabilized systems followed, and Kalman fi ltering was developed for an optimal processing of the INS survey data (Schwarz, 1983). The method has been used until recently for the establishment of geodetic control and for station densifi cation in existing networks, in order to accelerate mapping of vast undeveloped areas, e.g., in Canada and in Brazil.

A weakness of inertial positioning is the error propagation. INS errors are characterized by the time stability of the output’s bias (drift) and of the scale factor (calibration). There exists a wide accuracy range at these quantities, ranging at the bias stability from $0 . 0 0 0 1 ^ { \circ } / \mathrm { h }$ to $0 . 1 ^ { \circ } / \mathrm { h }$ for the gyro’s and $1 0 ^ { - 6 }$ to $1 0 ^ { - 2 }$ for the accelerometers, and 1 to 100 ppm for the scale factors. These errors increase with the square of time, due to the double integration from acceleration to position. This error behavior led to the zerovelocity-updating (ZUPT) procedure, where the INS results are controlled and corrected every few minutes either by a stationary measurement (at land vehicles with the condition of zero velocity) or by external information (e.g., from GPS positioning). Today, INS surveys are generally combined with GNSS, which provide control of INS error propagation and system synchronization through updating and relate the INS results to a global reference system (Fig. 5.85). The INS results (output rate 10 to $1 0 0 \ H z )$ ) on the other hand, supply high spatial resolution and serve for bridging gaps due to temporal loss of GNSS signals. Integrated positioning using INS and GNSS is usually done along a traverse connecting two points with known position, and traverses may be combined to an area network. Coordinates can be calculated already nearly real-time using Kalman fi lter techniques, but post-processing by least-squares adjustment delivers best results. With rapid updating, relative centimeter-accuracy can be achieved now, while INS networks with zero-velocity-updating every few minutes are characterized by an accuracy of 0.1 to $0 . 3 ~ \mathsf { m }$ over distances of $1 0 0 ~ \mathrm { k m }$ and more.

![](images/5b0bb3eb62eedb7da17a5d74ac6576aa190896f89510c09a7f379db7a1c7316a.jpg)  
Fig. 5.85: iMAR iNAV-RQH: Inertial Laser Gyro Navigation System, courtesy M. Becker, Institut für Physikalische Geodäsie (IPG), TU Darmstadt.

At most geodetic applications, inertial positioning cannot compete nowadays with GNSS methods, with respect to economy and accuracy. Nevertheless, there a number of useful applications, e.g., subterranean and submarine surveys. Continuous positioning and orientation based on integrated GNSS/INS instrumentation, on the other hand, is of high interest at kinematic applications using land, sea and air vehicles. The multitude of sensor results to be georeferenced especially includes photogrammetric, laser and radar mapping, and also gravity, magnetic and other geophysical surveys (Schwarz and El-Sheimy, 2004; Vennegeerts et al., 2008).

Acoustic waves are employed for positioning on, and mapping of the ocean fl oor and the bottom of rivers and lakes. This is due to the fact that sound waves propagate well in water, in contrast to electromagnetic waves which are attenuated rapidly with increasing frequency. The propagation of acoustic waves through water depends on the interdependent water properties temperature (main effect), salinity and density resp. pressure. Distances between points on the sea surface and on sea bottom are derived from acoustic signals emitted from a ship-borne transducer and either refl ected by the sea bottom (mapping of the ocean, lake or river fl oor), or sent back by a transponder established at sea fl oor (positioning). Acoustic sea fl oor mapping is nowadays carried out effi ciently and in a global scale by multibeam sonar systems, with GNSS positioning of the survey vessel Lurton (2002), it will not be discussed here further. Precise positioning, on the other hand, requires the installation of sea-bottom control points, with active transponders (acoustic beacons) transmitting the received signal to the transducer on board of the ship (Fig. 5.86), Chadwell et al. (1998).

The slant range between the transducer and the transponder is calculated from the propagation time of the signal traveling forth and back, according to the two-way pulse travel time relation (5.103b). Depending on the distance between the transponders (“baselines”), the frequency of the carrier waves varies between 5 to $2 0 \ \mathsf { k H z } ,$ for baseline lengths up to $1 0 ~ \mathrm { k m }$ and more; pulse lengths are between 5 and $1 5 ~ \mathsf { m s }$ . Signal travel time is measured with μs-accuracy, and refraction (pulse delay and ray bending) is taken into account by empirical formulas for the effects of temperature, salinity and pressure changes. Velocity values vary between 1470 and $1 5 4 0 ~ \mathrm { m / s }$ for sea water (mean value $1 5 0 0 \mathrm { m } / \mathrm { s } )$ , with large variations occurring within the uppermost $5 0 0 ~ \mathrm { m }$ . Baseline accuracy depends on the range and the network’s confi guration, and reaches the cm-order of magnitude. Relative positions of the sea fl oor control points are derived by spatial trilateration (Rinner, 1977), while the relation to the global reference system is established by GNSS-positioning on board of the surface vessel.

![](images/c7d17359b3f4603a780bea682763e5504a4e345cd20daa51a778842c3e9cc69e.jpg)  
Fig. 5.86: Acoustic positioning on the sea bottom (transponder T, transmitter S).

Geodetic underwater acoustic networks have been established locally for geodynamic investigations, e.g., for the observation of sea fl oor spreading at active ridge zones, and for monitoring crustal deformation at subduction zones (Spiess et al. (1998); Isshiki, 2000/2001/2004). Control points are usually arranged in arrays of three to four stations, with station separation of a few $\mathrm { k m }$ to $1 0 ~ \mathrm { k m }$ and more. The acoustic transponders are powered by batteries, with lifetime up to 5 years, or by nuclear energy sources. The connection to “stable” reference stations on land is realized through relay stations established at platforms on the sea surface (ship, buoy) or even inside the water.

# 5.5.4 Leveling

In geometric leveling (also spirit leveling or differential leveling), differences in height are determined using horizontal lines of sight between points in close proximity to each other. Leveling is conducted with a leveling instrument (level) and two vertically posted leveling rods (Fig. 5.87). The leveled height difference $\delta n$ between the rods is given by the difference between the backsight $( b )$ and the foresight $( f )$ reading:

$$
\delta n = b - f .
$$

The leveling instrument consists primarily of a measuring telescope capable of rotation about the vertical axis. The line of sight is brought into the horizontal either by a coincidence bubble in conjunction with a tilting screw or, for most modern instruments, automatically by a compensator that is comprised mainly of a gravity pendulum (fi rst introduced with the ZEISS Ni2 level in 1950). A setting accuracy of $0 . 2 { ^ { \prime \prime } }$ to $0 . 5 ^ { \prime \prime }$ is achieved by both methods. The use of a compensator increases the speed of leveling and reduces the sensitivity with respect to temperature variations. On the other hand, a spirit level is less sensitive with respect to high-frequency oscillations as produced by traffi c, machinery or wind. Thus it may still offer advantages at high precision industrial and engineering surveys, Fig. 5.88.

![](images/10330a7de4a698a2e00c507349dcbbd86870e42175b3c63a6bc84404f8d8f7ca.jpg)  
Fig. 5.87: Geometric leveling principle.

![](images/2273a18a0965eb560e9b9f6f640e74c33548bdfb563ee6461faf0b25fdddf314.jpg)  
Fig. 5.88: Bubble precision level NABON, courtesy Breithaupt, Kassel/Germany.

High-precision levels employ telescopes with an aperture of 40 to $5 0 \ \mathrm { m m }$ and a magnifi cation of 30 to 40 or more. Lines of sight (distance between the level and the rods) depend on leveling purpose and topography, and are kept within 30 to $5 0 ~ \mathsf { m }$ at precise leveling. Setting-up the instrument in the middle of two subsequent rod positions is usual, as it eliminates errors due to non-parallelism of the collimation and the bubble axes as well as symmetric refraction effects (see below). In the analog mode, the leveling rods carry two graduation lines on invar tape, displaced against each other and numbered differently in order to detect reading errors. The line of sight is adjusted to the closest graduation mark by means of a parallel plate mounted in front of the objective’s lens. The amount of the displacement is measured by a micrometer (Fig. 5.89).

Digital levels were introduced with the Wild NA 2000 (Ingensand, 1990). They are used in connection with invar staffs that carry a binary code (division e.g., $0 . 3 \mathrm { \ m m }$ ), Fig. 5.90. A code section around the horizontal sight is projected on a CCD sensor in the image plane of the telescope. A subsequent processing of the image by a microprocessor includes electronic scanning (A/D conversion) and correlation with a digital reference signal, whereby the automatically measured distance has to be taken into account. Special calibration procedures have been developed for digital levels and staffs (Rueger and Brunner, 2000).

![](images/cd5de6125e59299c3534f564240710b27af42f792f71d3ea3c984df81e07a2da.jpg)  
Fig. 5.89: Automatic level (Wild/Leica NA2), courtesy Leica Geosystems AG, Heerbrugg, Switzerland.

![](images/5857448d94ed50269d748008ea1924b4bda9726997d05668ebec174816c98e88.jpg)  
Fig. 5.90: Digital level (Trimble DiNi Level), courtesy Trimble Navigation Ltd., Sunnyvale, CA, U.S.A.

In order to transfer heights over larger distances, the individual leveled differences are summed. For one set-up, the non-parallelism of the level surfaces may be neglected (quasi-differential method). The observed difference $\delta n$ then corresponds to the height difference of the level surfaces passing through the rod sites. Summing the individual differences between two bench marks $P _ { \uparrow }$ and $P _ { _ 2 }$ yields the “raw” leveled height difference

$$
\Delta { n } _ { 1 , 2 } ^ { \mathrm { ~ ~ } } = \sum _ { 1 } ^ { 2 } \delta n .
$$

At longer distances, the effect of the non-parallelism may reach the cm-order of magnitude and more, cf. [3.2.1]. Hence $\Delta { } n$ depends on the path taken and does not provide a unique height. A unique height determination can only be achieved by considering gravity $g ,$ that is by referring to potential differences $\Delta W .$ According to (3.52) we have

$$
\Delta W _ { _ { 1 , 2 } } = W _ { _ { 2 } } - W _ { _ { 1 } } = - \intop _ { 1 } ^ { 2 } g d n \approx - \sumop _ { 1 } ^ { 2 } g \delta n .
$$

Thus potential differences can be determined without any hypothesis from leveling and surface gravity. In order to obtain height differences in any specific height system from the raw leveling results, gravity reductions have to be applied, cf. [6.4.1].

The accuracy of precise leveling depends on many effects. Some of the leveling errors behave in a random manner and propagate with the square root of the number of individual setups. Other errors are of systematic type and may propagate with distance in a less favorable way. Hence, particular attention must be afforded to reduce them, by instrumental measures and modeling or by employing dedicated measurement methods. We mention the main error sources (Kukkamäki, 1980):

Misleveling of the instrument is of random type and results in an error of a few $0 . 0 1 \mathrm { ~ m m }$ for an individual height difference. Residual adjustment errors at a bubble instrument cancel at “leveling from the middle”. An imperfect operation of the compensator causes an “obliquity of the horizon” which is eliminated by measuring in two opposite positions of the compensator. Magnetic effects on the compensator are kept small generally, but a regular control is advisable. Rod graduation errors include a “mean” scale error, errors of the individual graduation marks, and effects of thermal expansion. Routine calibrations deliver the corresponding corrections, with a remaining random part less than 5 to $1 0 \mu \mathrm { m }$ (Rueger and Brunner, 2000). Rod inclination errors can be kept suffi ciently small by properly adjusting the rod bubble and carefully holding the rod in the vertical position. Local vertical movements (0.01 to $0 . 1 \mathrm { \ m m }$ per station) of the rods may occur during the measuring process, depending on the stability of the ground. If proportional to time, they cancel by forward and backward leveling runs.

Vertical refraction, cf. [5.1.2], contains an irregular (shimmer) and a systematic part. The fi rst one acts as a random error, reaching $0 . 0 1 ~ \mathrm { \ m m }$ under cloudy skies. Systematic effects particularly affect observations made close to the ground or in terrain with steep slopes. These effects may reach 0.01 to $0 . 1 ~ \mathsf { m m }$ per $1 \textrm { \textrm { m } }$ height difference. They can be modeled in part by a refraction correction, with the vertical temperature gradient as a function of height, and eventually additional information about the environment (Angus-Leppan, 1984). The timevariable effect of the Earth tides plays a role at extended leveling networks, causing periodic inclinations of the line of sight. These can be modeled by the horizontal tidal component acting in the azimuth of the leveling line. Starting from (3.119) and taking the elasticity of the Earth into account, the tidal reduction for the moon reads

$$
\delta _ { _ { t ( m ) } } = 0 . 0 6 \sin 2 \psi _ { _ { m } } \cos ( \alpha _ { _ { m } } - \alpha ) s \mathrm { m m / k m } .
$$

Here, $\alpha _ { \mathrm { { m } } }$ and $\alpha$ are the azimuths of the moon and of the leveling line, and $\psi _ { \mathrm { { m } } }$ is the geocentric central angle between the directions to the moon and the computation point; $s$ is the length of the leveling line in km. The same equation is valid for the sun, with an effect of $4 6 \%$ of that for the moon (Kukkamaki, 1949).

In order to eliminate or reduce systematic errors, precise leveling is always carried out with equal back and foresights (“leveling from the middle”) at less than $5 0 ~ \mathsf { m }$ distance. Observations should be performed during cloudy weather, preferably in the morning and in the evening hours. Line of sights very close to the ground ( $_ { 0 . 5 \textrm { m } }$ or less) should be avoided. Leveling is generally conducted twice, in opposing directions and possibly under different meteorological conditions. For a $1 ~ \mathrm { k m }$ double-run leveling, one can attain an accuracy of 0.2 to $1 . 0 \mathrm { m m }$ .

The time needed for precise leveling can be signifi cantly reduced by motorized leveling, whereby the instrument and the rods are carried in and operated from an automobile. This mode also reduces time dependent errors and partially eliminates asymmetric refraction effects, as the line of sight is more remote from the ground (Peschel, 1974; Becker, 2002).

For leveling across broad waterways and inlets of the sea, several methods have been developed. In reciprocal leveling, approximately horizontal sights to specially designed targets are taken simultaneously with precise levels from both sides of the waterway. For longer series of observations including a change of the instruments, height differences over 1 to $2 ~ \mathrm { k m }$ can be determined with a precision of 1 to $2 \textrm { m m }$ (Kakkuri, 1966). Larger distances can be bridged by hydrostatic leveling based on the principle of communicating tubes. A hose fi lled with water (free of air bubbles, uniform temperature) is laid between the shores of the watercourse, and the water level at the vertical ends of the hose is observed, assuming that it represents the same level surface. In hydrodynamic leveling (geostrophic leveling), the height is transferred over the waterway utilizing water level records, which have to be reduced for the effects of sea surface topography, cf. [3.4.2]. This implies the use of a hydrodynamic model, which takes water velocity, wind drag, water depth and bottom friction, atmospheric pressure and water density into account, as well as gravity and Coriolis force.

Hydrostatic leveling has been applied for ranges up to $2 0 \mathrm { k m }$ (e.g., Fehmarn-Belt/Baltic Sea) and delivers mm-precision (Andersen, 1992). In the Netherlands, it was used in an operational mode for measurements off-shore and through rivers and canals (Waalewijn, 1964). Hydrodynamic leveling was employed, for instance, for a height transfer over the British channel $( 7 0 \mathrm { k m } )$ , with a precision of about $1 \ \mathrm { c m }$ (Cartwright and Crease, 1963).

# 5.5.5 Tilt and strain measurements

Tilt and strain observed on the surface of the Earth indicate the response of the Earth’s crust (crustal deformations) to external and internal forces such as Earth tides, tectonic processes, and seismic and volcanic activities. Tilt and strain are dimensionless quantities and are given in radian or arcsec and (relative) extension (positive sign) or compression per distance, respectively.

Over time intervals of years to decades, long-term tilt and strain can be determined from repeated observations of geodetic control networks, delivering relative displacements between the observation sites. Classical terrestrial techniques as triangulation, trilateration and leveling could only detect the integral deformation effect over large time spans (years to decades), while satellite techniques as GPS are now able to continuous recording of absolute site displacements, in horizontal position and height, cf. [8.3.3]. Tiltmeters and strainmeters (also called extensometers), on the other hand, have been developed in order to monitor continuously local deformations (Agnew, 1986; Zadro and Braitenberg, 1999).

Short-term (up to 1 day) tilt and strain is dominated by tidal deformations and is at the order of ${ { 1 0 } ^ { - 8 } }$ to ${ { 1 0 } ^ { - 7 } } ,$ , which correspond to inclinations of $0 . 0 0 2 ^ { \prime \prime }$ to $0 . 0 2 ^ { \prime \prime }$ and lengths changes of 0.01 to $0 . 1 ~ { \mu \mathrm { m / m } }$ . Long-term effects of tectonic origin generally are only at the order of a few ${ { 1 0 } ^ { - 7 } } .$ /year. Episodic effects related to seismic or volcanic events may reach the same order of magnitude and more over a few hours to a few weeks and months. Consequently, the instrumental sensitivity of tilt and strainmeters should be at least about $1 \dot { 0 } ^ { - 9 }$ to $\dot { 1 } 0 ^ { - 1 0 } ,$ and the stability with time should be better than ${ { 1 0 } ^ { - 7 } } .$ /year. A variety of tiltmeters and strainmeters has been developed over the past 50 years and operated underground in order to reduce the strong disturbances of atmospheric and hydrological origin. Instrumental noise was remarkably reduced at the transition from analogue to digital recording.

Tiltmeters measure the inclination of the Earth’s surface with respect to the local vertical. Two mutually perpendicular sensors are needed in order to completely determine the tilt, which are usually orientated in the NS and EW-directions. Tiltmeters have been designed as horizontal and vertical pendulums, electronic tiltmeters, and long water tubes (Zürn et al., 1986).

Horizontal pendulums consist of two nearly vertical threads that support an approximately horizontal beam with an attached mass (Zöllner suspension), Fig. 5.91. Because of the small inclination of the rotational axis with respect to the vertical, a tilt of the support (basis about $3 0 ~ \mathrm { c m }$ ) or a plumb line variation cause a strongly amplifi ed angular defl ection (astatization), which may be further enlarged optically. Fused quartz (Verbaandert-Melchior pendulum) or metallic alloys are used as pendulum material in order to keep thermal effects small. Calibration is performed by controlled tilting of the instrument (Van Ruymbeke, 1976). Among the vertical pendulums is the Askania borehole instrument (length $6 0 ~ \mathrm { c m }$ ) which may operate in depths of 20 to $6 0 \textrm { m }$ (Fig. 5.92). The pendulum’s suspension allows it to swing freely, and the defl ections are sensed by two three-plate capacitive transducers installed at right angles to each other. The pendulum is calibrated by displacing a small mass over a known distance (Flach, 1976). Short-base electronic tiltmeters (e.g., the Hughes tiltmeter) use electrodes as sensors to measure a bubble’s position, or record the fl oating of the sensing mass in a magnetic fi eld; these instruments are especially adapted for the installation in boreholes. Water-tube tiltmeters with lengths of several $1 0 0 \mathrm { m }$ have also been developed, and installed in cavities. Tilt is derived from the water level variations at the endpoints of the tube which are measured by capacitive or interferometric methods (Kääriäinen, 1979).

![](images/51a7099101889e27ed911d7203d61e9eb62e81aa5182098a39ba8b7ae4deb545.jpg)  
Fig. 5.91: Zöllner horizontal pendulum principle.

![](images/c49a25da6333dd9dada136a287b0b8d178bb20866292d80dc32a8bc8c58aa86f.jpg)  
Fig. 5.92: Vertical pendulum “Askania borehole tiltmeter”, Bodenseewerk Geosystem, Überlingen, Germany, after Flach (1976) and Agnew (1986).

Strainmeters measure relative displacements of the Earth’s crust (King and Bilham, 1973). For a complete determination of the strain tensor, which contains six independent components, a strain meter array should be arranged with orientation in different spatial directions, although in most cases only horizontal strainmeters have been installed. Strainmeter constructions use mechanical or laser length standards, with baseline lenghts from $_ { 0 . 1 \textrm { m } }$ to $1 ~ \mathrm { k m }$ .

Short-baseline strainmeters (baseline length 10 to $3 0 \textrm { m }$ and more) are represented by invar wires and fused quartz tube rods. One end of the instrument is fi xed to the rock, and the crustal displacement is measured at the other end by inductive or capacitive transducers (King and Bilham, 1973), Fig. 5.93. Borehole strainmeters were developed since the 1960s, including a hydraulic dilatometer (Myren et al., 2006) and a 3-component rod strainmeter of $_ { 0 . 1 \mathsf { m } }$ -baselength (Gladwin et al., 1987). Laser strainmeters apply the Michelson interfero meter principle. Operated in an evacuated tube, they can measure distances up to $1 ~ \mathrm { k m }$ with nm resolution and better (Berger and Levine, 1974; Takemoto et al., 2006).

Among the instrumental errors of tiltmeters and strainmeters are the uncertainties of the calibration (about 0.1 to $1 \%$ ) and the direct effects of temperature and air pressure variations, which are kept small by the selection of the material and appropriate shielding. Long-term drift effects are at the order of ${ { 1 0 } ^ { - 6 } }$ to ${ { 1 0 } ^ { - 7 } } .$ /year and to a large part are due to problems inherent with the sensor-rock coupling. Effects induced by atmospheric and hydrological variations (air temperature, air pressure, solar radiation, rainfall, groundwater) pose severe problems in interpreting the results, especially for tiltmeters. These disturbances pronounce daily and seasonal periods but also happen at other time scales, they severely obscure tidal, tectonic and other geodynamic signals. Modeling of these effects, with frequency bands including those of the Earth tides and the seismotectonic deformations, is still in its infancy. Consequently, their infl uence is reduced by installing the instruments below the Earth’s surface, in tunnels, mines, natural caves, and boreholes. Unfortunately, this strategy causes other problems to be discussed in the following.

![](images/a485a0b1b4c858baa4346cdad5b7ca37a8363f3cb0d93005e08aedd8acbc9e6b.jpg)  
Fig. 5.93: Invar wire strainmeter, courtesy Black Forest Observatory Schiltach.

When installing tiltmeters and strainmeters below the Earth’s surface, geologic, topographic, and cavity effects in most cases produce large local distortions of the tiltmeter and strainmeter data. This is due to variable rock properties including local fractures, rugged topography, and different cavity reactions to deformation. Local distortion may reach 10 to $1 5 \%$ and more, leading to non-representative results (Harrison, 1976). Attempts to model these effects have been only partly successful (Sato and Harrison, 1990; Kohl and Levine, 1995). Consequently, in addition to carefully selecting the observation site, preference now is given either to short-base tiltmeters and strainmeters operating in boreholes (if possible with depths of $1 0 0 \mathrm { ~ m ~ }$ or more) or to long-baseline instruments installed in tunnels or cavities. In the latter case, local effects are reduced by integrating over the large distance of some 10 to some $^ { 1 0 0 \mathrm { ~ m ~ } }$ .

Tilt and strain is measured continuously at underground observatories and dedicated networks, frequently in connection with GNSS observations and gravity recording. Extensive observations started with the “International Geophysical Year” (1957), and concentrate now on regions of seismotectonic and volcanic activity, as the western United States, Japan, China, and Italy. A strong impetus also for tilt and strain techniques came from national earthquake prediction programs, as e.g., established in Japan and China. Among the participating observatories we have the Piñon Flat Observatory/California (Institute of Geophysics and Planetary Physics, University of California, Wyatt et al., 1990), the observatories of the Research Center for earthquake Prediction/Disaster Prevention (Kyoto University, Japan) and other Japanese institutions, the observation sites and observatories under the responsibility of the China Seismological Bureau, and the Black Forest Observatory Schiltach (Karlsruhe Institute of Technology KIT and University of Stuttgart, Germany). Extended geodetic networks for monitoring surface displacements due to plate tectonics have been installed, among others, in Japan (Takemoto, 1995) and in the western United States. Here, the Earth Scope Plate Boundary Observatory (PBO) started operation in 2008. This National Science Foundation funded project now coordinates the operation of more than 1000 permanent GPS stations (with partly one Hertz or higher frequency and one second and less latency) and a number of borehole and laser strainmeters, located along the Pacifi c/ North-American plate boundary (Agnew, 2007). The strategy of obtaining “real-time” data for actual crustal movements is pursued also at the global differential GPS network (more than 100 stations) of JPL/NASA (Kechine et al., 2003). Tiltmeter networks have been established especially at active volcanoes, e.g., at the Kilauea/Hawaii and Mount Etna/Italy.

Tiltmeter and strainmeter results contribute to Earth tide research in the short-periodic part and to the detection of anomalous tilt and strain related to seismic and volcanic activity, cf. [8.3.4], [8.3.6].

# 6 Methods of Positioning and Gravity Field Modeling

Geodetic evaluation methods may be separated into positioning and gravity fi eld determination (the determination of the Earth’s rotation parameters is not pursued in the following, as it has been discussed in connection with global reference systems [2] and measuring techniques [5]). This separation is possible because positioning only requires an approximate knowledge of the gravity fi eld, and gravity fi eld modeling needs only approximate positions. The linearization of the gravity fi eld is essential in both cases, and it permits a statistical fi eld description [6.1]. Nowadays, positioning is based on three-dimensional models [6.2], while classical strategies distinguish between horizontal positioning [6.3] and height determination [6.4]. Gravity fi eld modeling utilizes all kind of gravity fi eld related observables, it can be formulated in the form of boundary-value problems of potential theory [6.5]. Global models are derived mainly from the results of space geodesy, with additional information from terrestrial observations [6.6]. Local gravity fi eld estimation, on the other hand, is primarily based on terrestrial gravity fi eld data, and generally supported by satellite results [6.7]. Least-squares collocation represents another effi cient method for transformation and combination of gravity fi eld quantities, and is now routinely applied for regional and local solutions [6.8].

The simultaneous determination of station coordinates and gravity fi eld quantities, together with other parameters of different kind, in one mathematical model has been designated as integrated or operational geodesy (Eeg and Krarup, 1973; Hein, 1986). Employing all relevant data and taking the errors of the data into account, functional modeling fi nally leads to least-squares adjustment. The combination strategy allows to more completely exhaust the information content of the data, and to improve the accuracy and reliability of the results. On the other hand, the large amount of data and unknown parameters (at least at global and regional dimensions) raises serious problems with respect to proper weighting of the observations, modeling of systematic effects, and data processing. Hence, the application of deterministic combination methods is restricted to a limited number of observations and unknown geometric and physical parameters, recent examples being the “satellite-only” Earth models calculated since the early days of satellite geodesy, cf. [6.6.2]. An alternative (and extended) approach to combined modeling of geometric and physical quantities is least-squares collocation with parameters (Moritz, 1980, p. 111 ff.), where again for practical reasons the geometric part of the problem is treated separately from the gravimetric part. The integration of geodetic techniques and the consistent combination for geometry, gravity fi eld and Earth rotation is a fundamental part of the Global Geodetic Observing System (GGOS) established by IAG, cf. [1.4.2], Plag and Pearlman (2009).

Geodetic evaluation methods are described in textbooks on geodesy, e.g., Bomford (1980), Moritz (1980), Vanicˇek and Krakiwsky (1986), Heck (2003a), Hofmann-Wellenhof and Moritz (2005). The theory of errors and adjustment methods applied to geodetic modeling are discussed in Koch (1999), Grafarend (2006), Niemeyer (2008) and Ghilani (2010), among others.

# 6.1 Residual gravity fi eld

The actual gravity fi eld can be suffi ciently well approximated by the normal gravity fi eld of the level ellipsoid, cf. [4.2.2], which results in linear relations between the residual observations and the unknown gravity fi eld parameters. The fundamental quantity of the residual gravity fi eld is the disturbing potential. It is closely related to the height anomaly and the geoid height [6.1.1]. The residual gravity vector generally is expressed by its scalar components, the gravity anomaly or the gravity disturbance and the defl ection of the vertical [6.1.2]. On certain assumptions, the residual gravity fi eld may be treated by statistical methods, which is of importance in gravity fi eld interpolation and modeling [6.1.3].

# 6.1.1 Disturbing potential, height anomaly, geoid height

Approximation of the Earth’s gravity potential $W ( 3 . 4 2 )$ by the normal gravity potential $U$ (4.37) leads to the disturbing potential (also anomalous potential) T defi ned at the point $P$ :

$$
T _ { \scriptscriptstyle P } = W _ { \scriptscriptstyle P } - U _ { \scriptscriptstyle P } .
$$

$W$ and $U$ contain a gravitational and a centrifugal part. As the centrifugal acceleration of the Earth is known with high accuracy, cf. [3.1.4], we may assume that the centrifugal parts of $W$ and $U$ are identical. The disturbing potential then is formed by the difference of the gravitation of the Earth and of the level ellipsoid, and thus is a harmonic function outside the Earth’s masses. Hence, it obeys Laplace’s differential equation (3.29)

$$
\Delta T = 0 ,
$$

where $\Delta$ stands for the Laplace operator. $T$ can be expanded into spherical harmonics, in analogy to the corresponding development for the gravitational potential (3.89) and (4.45). Expressed in spherical coordinates $r , \vartheta , \lambda ,$ the disturbing potential as a spatial function reads, in abbreviated form, see (3.88):

$$
T = T ( r , \ \vartheta , \ \lambda ) = \sum _ { I = 2 } ^ { \infty } \Bigl ( \frac { a } { r } \Bigr ) ^ { I + 1 } T _ { I } ( \vartheta , \lambda ) .
$$

In its full form this development reads as

$$
T = \frac { G M } { r } \sum _ { I = 2 } ^ { \infty } \Bigl ( \frac { a } { r } \Bigr ) ^ { I } \sum _ { m = 0 } ^ { I } \Bigl ( \Delta C _ { I m } \cos m \lambda + \Delta S _ { I m } \sin m \lambda \Bigr ) P _ { I m } ( \cos \vartheta ) ,
$$

where the $\Delta C _ { \scriptscriptstyle I m }$ and $\Delta S _ { _ { I m } }$ are the residual harmonic coeffi cients, being defi ned as differences between the coeffi cients of the actual and the normal gravity fi eld. Comparing (6.3) and (6.4) yields the surface spherical harmonics

$$
T _ { \jmath } = \frac { G M } { a } \sum _ { m = 0 } ^ { I } ( \Delta C _ { \jmath m } \cos m \lambda + \Delta S _ { \jmath m } \sin m \lambda ) P _ { \jmath m } ( \cos \vartheta ) .
$$

Due to the properties of $U ,$ only the even zonal residual coeffi cients differ from the actual gravity fi eld coeffi cients $C _ { I m ^ { \prime } }$ while all the other $\Delta C _ { \scriptscriptstyle I m }$ are identical with the actual gravity fi eld parameters, cf. [4.2.2]. The development of (6.3) and (6.4) starts at $I = 2$ since equality of the masses of the Earth and the ellipsoid is assumed, as is coincidence of the center of the Earth’s masses with the center of the ellipsoid, cf. [3.3.4].

The disturbing potential is closely related to the vertical distance between $P$ and the point $Q$ located on the spheroidal surface $U = U _ { Q ^ { \prime } }$ cf. [6.5.1]. $Q$ is associated with $P$ by the condition

$$
U _ { Q } = W _ { P ^ { \prime } } 
$$

cf. [4.2.3], Fig. 6.1. This distance is called height anomaly $\zeta .$ Geometrically, it is the difference between the ellipsoidal height $h$ and the normal height $H ^ { N } ( 3 . 1 0 7 )$ , (4.66):

$$
\zeta = h - H ^ { N } ,
$$

where we have neglected the slight curvature of the normal plumb line. The surface for which (6.6) holds at every point is called the telluroid (Hirvonen, 1960; Grafarend, 1978b). A corresponding relation holds at any point in the exterior space.

The telluroid represents an approximation to the physical surface of the Earth. By extending $H ^ { N }$ downward from $P$ we obtain the quasigeoid, which is often used as a zero height surface, cf. [3.4.3], [7.2]. The height anomaly $\zeta$ now becomes the distance between the level ellipsoid $U = U _ { 0 }$ and the quasigeoid, and is also called quasigeoid height.

If $P$ is located on the geoid, we obtain the geoid height $N$ (also called geoid undulation) as the vertical distance between the ellipsoid and the geoid. In analogy to (6.7), a geometric defi nition follows by differencing the ellipsoidal height $h$ and the orthometric height $H \left( 3 . 1 0 6 \right)$ :

$$
N = h - H ,
$$

where again the effect of the plumb line curvature has been neglected.

The difference between the geoid height and the height anomaly is equal to the difference between the normal height and the orthometric height and follows from (3.106) and (3.107):

$$
N - \zeta = H ^ { N } - H = \frac { \overline { { g } } - \overline { { \gamma } } } { \overline { { \gamma } } } H = \frac { \Delta g _ { _ B } } { \overline { { \gamma } } } H .
$$

![](images/b3ef93fecf845d2cc0da805b235727be63855ff0363bc15e9421a091fb61ba3c.jpg)  
Fig. 6.1: Ellipsoidal, normal and orthometric height.

The difference depends on the height and thus is zero on the oceans, if we neglect the small effect of sea surface topography, cf. [3.4.2]. It also depends on a “mean” gravity_ anomaly ${ \overline { { g } } } - { \bar { \gamma } } ,$ which (approximately) corresponds to the Bouguer anomaly $\Delta { g } _ { B ^ { \prime } }$ to be introduced in [6.5.3 ].

# 6.1.2 Gravity disturbance, gravity anomaly, defl ection of the vertical

The gravity vector $\mathbf { g }$ at $P$ can be approximated by the vector of normal gravity $\gamma ,$ which leads to the gravity disturbance

$$
\delta \mathbf { g } _ { P } = \mathbf { g } _ { P } - \boldsymbol { \eta } _ { P } ,
$$

see Fig. 6.2. Neglecting the small angle between the directions of $\pmb { \delta }$ and $\gamma$ (defl ection of the vertical), we obtain the magnitude of the gravity disturbance

$$
\delta g _ { _ P } = g _ { _ P } - \gamma _ { _ P } .
$$

$g$ can be measured on the Earth’s surface and in the exterior space. The calculation of $\gamma _ { _ { P } }$ presupposes the knowledge of the geodetic coordinates (ellipsoidal latitude and height) of $P .$ This is nowadays possible through geodetic space techniques (mainly GNSS methods), while classical geodesy had to consider the ellipsoidal coordinates as unknowns, cf. [6.3], [6.4]. This fact posed a serious problem with the height coordinate, as only normal or orthometric heights determined by leveling were available, cf. [3.4.3]. Consequently, gravity fi eld modelling, instead of the gravity disturbance, employed (and generally still employs today) the gravity anomaly

$$
\Delta \mathbf { g } _ { P } = \mathbf { g } _ { P } - \boldsymbol { \eta } _ { Q ^ { \prime } }
$$

with the magnitude

$$
\Delta g _ { _ P } = g _ { _ P } - \gamma _ { _ Q } .
$$

![](images/e32b8de4397adc24f88b7676e5516ddb65a46a6d12cc3c7311c6af83bb4af0b4.jpg)  
Fig. 6.2: Actual and normal gravity.

Again, $Q$ is related to $P$ by the condition (6.6). $\gamma _ { _ { Q } }$ can be calculated by (4.63), starting from normal gravity $\gamma _ { \mathrm { { 0 } } }$ on the ellipsoid (4.41) and replacing $h$ by $H ^ { N } ( 3 . 1 0 7 )$ . This free-air reduction is given by (4.61):

$$
\delta g _ { F } ^ { N } = - \frac { \partial \gamma } { \partial H ^ { N } } H ^ { N } .
$$

The free-air gravity anomaly, defi ned on and outside the Earth’s surface according to Molodensky, reads

$$
\Delta g _ { F } ^ { N } = g + \delta g _ { F } ^ { N } - \gamma _ { 0 } .
$$

In many applications, $\frac { \partial \gamma } { \partial H ^ { N } }$ is approximated by a mean value of $- 3 . 0 8 6 ~ \mu \mathrm { m } s ^ { - 2 } / \mathrm { m }$ .

The determination of the geoid requires that the gravity anomalies are given everywhere on that level surface. Furthermore, in order to apply the Laplace equation, the masses outside the geoid have to be removed. Several types of gravity reductions are available for this purpose. The methods differ by the manner in which the topographical masses are displaced, and gravity is reduced onto the geoid. The gravity anomaly on the geoid then is defi ned as the difference between the gravity on the geoid $g _ { 0 ^ { \prime } }$ and the normal gravity $\gamma _ { \mathrm { { 0 } } }$ on the ellipsoid (Fig. 6.2):

$$
\begin{array} { r } { \Delta g = g _ { \mathrm { 0 } } - \gamma _ { \mathrm { 0 } } . } \end{array}
$$

Dependent on the kind of reduction, different types of geoid related gravity anomalies have been defi ned, serving not only for the determination of the geoid but also for gravity fi eld interpolation and geophysical interpretation, cf. [6.5.3].

According to the previous defi nitions, gravity disturbance and gravity anomaly are vector quantities. Their directions are given through the difference between the direction of the actual plumb line and a reference direction defi ned in the normal gravity fi eld. This difference is called defl ection of the vertical (Fig. 6.3). With respect to the reference direction, we distinguish between three kinds of vertical defl ection, which differ only slightly (Jekeli, 1999):

• The defl ection of the vertical $\theta ^ { N }$ defi ned on the surface or the exterior of the Earth, with the direction of the normal plumb line at $Q$ as a reference (Molodensky defi nition). The reference direction practically coincides with the surface normal to $U = U _ { P }$ at $P .$

![](images/253fced10bfb7d4e41f885311b1905316dd395d20df47c42dd4cfad04a91554b.jpg)  
Fig. 6.3: Defl ection of the vertical according to a) Molodensky, b) Helmert, c) Pizetti.

• The defl ection of the vertical $\theta$ at the Earth’s surface, referring to the ellipsoidal normal at $P$ (Helmert defi nition). It differs from $\theta ^ { N }$ only by the slight curvature (effect of a few $0 . 1 ^ { \prime \prime }$ ) of the normal plumb line, cf. [4.2.3]. This defi nition is preferred generally, as the ellipsoidal normal is provided by the geodetic coordinates. The defl ection of the vertical $\theta _ { \mathrm { 0 } }$ defi ned on the geoid (Pizetti defi nition). It is given by the difference between the actual plumb line on the geoid and the ellipsoidal normal. It differs from the previous defi nitions by the curvature of the actual plumb line and is of importance for the determination of the geoid.

The defl ection of the vertical is expressed either by its magnitude $\theta$ and its azimuth $\alpha _ { \theta }$ or, more generally, by its components in the north-south and east-west directions. A geometric derivation follows from spherical trigonometry on the unit sphere around the calculation point (Fig. 6.4). Here, we assume that the minor axis of the reference ellipsoid is parallel to the $Z .$ -axis of the global reference system and that the ellipsoidal initial meridian is parallel to the $\chi$ -axis. These conditions are practically fulfi lled with modern reference systems and well approximated by classical geodetic systems, cf. [6.2.2]. After parallel displacement, we identify $N$ as the point of intersection of the $Z .$ -axis with the unit sphere and $Z _ { a }$ and $Z _ { g }$ as the directions to the astronomic and the geodetic zenith, respectively. The defl ection of the vertical represents the spherical distance between $Z _ { a }$ and $Z _ { \mathrm { g } ^ { \prime } }$ its azimuth is denoted by $\alpha _ { \theta ^ { \ast } }$ The defl ection is decomposed into the meridional component $\xi$ (positive when $Z _ { a }$ is north of $Z _ { g } )$ and the component in the prime vertical $\eta$ (positive when $Z _ { a }$ is east of $Z _ { g } )$ . Along the azimuth $\alpha$ to a target point $P _ { _ { j ^ { \prime } } }$ we have the vertical defl ection component $\varepsilon .$

From spherical trigonometry we get

$$
\sin \varphi = \cos \eta \sin ( \Phi - \xi ) , \quad \sin \eta = \cos \varphi \sin ( \Lambda - \lambda ) ,
$$

and with

$$
\cos \eta \approx 1 , \sin \eta \approx \eta , \sin ( \Lambda - \lambda ) \approx \Lambda - \lambda ,
$$

the components are given by (linear approximation)

$$
\xi = \Phi - \varphi , \quad \eta = ( \Lambda - \lambda ) \mathrm { c o s } \varphi .
$$

According to Fig. 6.4, the component $\varepsilon$ in the azimuth $\alpha$ is composed by two parts:

$$
\varepsilon = \xi \cos \alpha + \eta \sin \alpha .
$$

These relations can also be derived by subtracting (4.36) from (3.45), after corresponding linearization, cf. [6.2.2].

![](images/e5ed7c214c491d5aa3f7fbc36cf90d31089b10ac86eaf62d91956328085d772d.jpg)  
Fig. 6.4: Vertical defl ection components.

Equations (6.17) and (6.18) are valid for any defi nition of the defl ection of the vertical.

The residual gravity fi eld quantities (disturbing potential, height anomaly/geoid height, gravity disturbance/gravity anomaly, defl ection of the vertical and others) depend on the geodetic Earth model used for approximating the gravity fi eld and on its orientation with respect to the Earth, cf. [6.2.2]. If referred to a geocentric mean Earth ellipsoid, they are designated as absolute quantities, otherwise they are relative only. The root mean square variation of absolute height anomalies and geoid heights is $\pm 3 0 \mathrm { ~ m ~ }$ (maximum values about $1 0 0 ~ \mathrm { { m } }$ ). The free-air gravity anomalies vary by about $\pm 4 0 0 ~ { \mu \mathrm { m } } s ^ { - 2 }$ (maximum values of a few $1 0 0 0 ~ { \mu \mathrm { m s } } ^ { - 2 } ,$ ) and the defl ections of the vertical by $\pm 7 ^ { \prime \prime }$ (maximum $3 0 ^ { \prime \prime }$ to $1 ^ { \prime \prime }$ in the high mountains), cf. [6.1.3], [6.6.3].

# 6.1.3 Statistical description of the gravity fi eld, interpolation

The residual gravity fi eld can be viewed as a realization of a stochastic process and treated by statistical methods (Moritz, 1970; Tscherning, 1978). The gravity anomaly is used as a fundamental gravity fi eld parameter in this aspect, as gravity data are available with high resolution on the continents and on the oceans. Other type gravity fi eld observations are either restricted to the long-wave part of the gravity fi eld (satellite derived spherical harmonic coeffi cients) or to the oceanic (satellite altimetry) respectively continental (defl ections of the vertical) parts of the Earth’s surface.

We assume that the mean value of the gravity anomalies $\Delta g$ corresponding to the zero-degree term of the spherical harmonic expansion of $\Delta g$ over the Earth (spherical approximation) is zero, cf. [6.5.4]:

$$
M \{ \Delta g \} = \frac { 1 } { 4 \pi } \int \displaylimits _ { \sigma } ^ { \infty } \Delta g d \sigma = 0 ,
$$

where $M \{ \}$ is the mean value operator, and $\sigma$ represents the unit sphere with the area of $4 \pi .$ The surface element can be expressed in spherical coordinates $\vartheta , \lambda$ by

$$
d { \boldsymbol { \sigma } } = \sin { \vartheta } d { \vartheta } d \lambda .
$$

The further statistical behavior of $\Delta g$ is described by the covariance function

$$
C ( \boldsymbol { \psi } ) = \mathrm { c o v } _ { \boldsymbol { \psi } } \big ( \Delta g \big ) = M \big \{ \Delta g \Delta g ^ { \prime } \big \} _ { \boldsymbol { \psi } } .
$$

It is defi ned as the mean value of all products of gravity anomalies at the points $P ( \Delta g )$ and $P ^ { \prime } ( \Delta g ^ { \prime } )$ having constant spherical distance $\psi$ on the unit sphere. $C ( \psi )$ shall only depend on $\psi$ and neither depend on the position (homogeneity of the anomalous gravity fi eld) nor on the azimuth of the line $P P ^ { \prime }$ (isotropy), Grafarend (1976). The evaluation of (6.21a) leads to

$$
C ( \psi ) = \frac { 1 } { 2 \pi } \cdot \frac { 1 } { 4 \pi } \int \limits _ { \lambda = 0 } ^ { 2 \pi } \int \displaylimits _ { \vartheta = 0 } ^ { \pi } \int \displaylimits _ { \sigma = 0 } ^ { 2 \pi } \int \displaylimits _ { \vartheta } ^ { \vartheta } { \mathrm { d } \vartheta \mathrm { d } \vartheta } d \vartheta d \lambda d \alpha = \frac { 1 } { 4 \pi } \int \displaylimits _ { \sigma } ^ { \mathrm { \dj } } \int \mathrm { \ d } \Delta { \mathrm { g } } \Delta { \mathrm { g } } ^ { \prime } \big \rangle _ { \psi } d \sigma .
$$

$C ( \psi )$ describes the distance dependent correlation of the gravity anomalies, which decreases with increasing distance. For $\psi = 0$ , we have $\Delta g = \Delta g ^ { \prime } ,$ and the covariance transforms into the anomaly variance

$$
\sigma ^ { 2 } ( \Delta g ) = M \big \{ \Delta g ^ { 2 } \big \} = \frac { 1 } { 4 \pi } \int \int \Delta g ^ { 2 } d \sigma .
$$

From the theory of stochastic processes, the statistical properties should be derived from an infi nite number of process realizations. As only one realization of the gravity fi eld is available,

the hypothesis of ergodicity is necessary, which states that the statistical quantities may also be calculated from mean values over one realization only (Moritz, 1980, p. 269).

As shown in [6.6.1], $\Delta g$ as a functional of T can be expanded into spherical harmonics. On the Earth’s surface $( r = R )$ the abbreviated form of this expansion reads

$$
\Delta g ( \vartheta , \lambda ) = \sum _ { I = 2 } ^ { \infty } \Delta g _ { I } ( \vartheta , \lambda ) ,
$$

with $\Delta g _ { I }$ Laplace’s surface harmonics, cf. [3.3.2]. With the conventions of mass equality between the Earth and the reference ellipsoid, and geocentric position of the ellipsoid, the terms of degree 0 and 1 are missing again, cf. [6.1.1]. As a consequence of (6.23), $C ( \psi )$ can also be expanded into spherical harmonics in the defi nition range $0 \leq \psi \leq \pi$ :

$$
C ( \psi ) = \sum _ { I = 2 } ^ { \infty } C _ { I } P _ { I } \left( \cos \psi \right) ,
$$

with $P _ { \ / r }$ $( \cos \psi )$ Legendre polynomials. Because of isotropy, only zonal terms exist in (6.24a). As is well known from potential theory, the harmonic coeffi cients $C _ { I }$ can be derived by inversion, applying orthogonality relations:

$$
\begin{array} { l } { { \displaystyle c _ { I } = \frac { 2 I + 1 } { 4 \pi } \int \displaylimits _ { \alpha = 0 } ^ { 2 \pi } \int \displaylimits _ { \psi = 0 } ^ { \pi } ( \cos \psi ) \sin \psi d \psi d \alpha } } \\ { { \displaystyle \quad = \frac { 2 I + 1 } { 2 } \int C ( \psi ) P _ { I } ( \cos \psi ) \sin \psi d \psi . } } \end{array}
$$

Corresponding equations are valid for fully normalized spherical harmonics, cf. [3.3.2], with

$$
C ( \psi ) = \sum _ { I = 2 } ^ { \infty } \bar { C } _ { I } \overline { { P } } _ { I } ( \cos \psi )
$$

and

$$
\overline { { C } } _ { I } = \frac { C _ { I } } { \sqrt { 2 I + 1 } } .
$$

Equation (6.24b) can be solved for a known covariance function by numerical integration. By inserting (6.21) into (6.24b), and taking (6.23) into account, we fi nally obtain

$$
C _ { I } = M \{ \Delta g _ { I } ^ { 2 } \} = \sigma _ { I } ^ { 2 } ( \Delta g ) .
$$

Hence, the coeffi cients are given by the anomaly degree variances defi ned as mean values over the squares of $\Delta g _ { \scriptscriptstyle { I ^ { \prime } } }$ and related to the degree variances of the residual harmonic coeffi cients, cf. [6.6.1].

A good approximation to reality is provided by the Tscherning and Rapp (1974) – degree variance model and the related covariance function, both have been successfully applied to date. The Tscherning-Rapp-model is based on satellite-derived harmonic coeffi cients for the degrees 2 to 10 and a set of $1 ^ { \circ }$ equal area anomalies (approximately quadratic compartments with constant area $1 1 0 \mathrm { k m } \times 1 1 0 \mathrm { k m } )$ . The variance of the point anomalies is__ $\dot { \sigma } ^ { 2 } ( \Delta \mathrm { g } ) = \left( 4 2 4 \mu \mathrm { m } \mathrm { s } ^ { - 2 } \right) ^ { 2 }$ and that of the mean anomalies $\sigma ^ { 2 } ( \overline { { \Delta g } } ) _ { 1 ^ { \circ } } = \big ( 3 0 3 \mathrm { \dot { \mu } m s } ^ { - 2 } \big ) ^ { 2 } .$ . The transition from the variance/covariance of point to mean anomalies has been performed per degree by a smoothing factor, which depends on the cap radius of the mean anomaly block (here $1 ^ { \circ } \times 1 ^ { \circ } ,$ ). As seen from Fig. 6.5, the correlation of the $1 ^ { \circ } \times 1 ^ { \circ } ,$ -anomalies approaches zero at a spherical distance of about $3 0 ^ { \circ }$ to $4 0 ^ { \circ }$ .

![](images/75dc426e5c482c3e7ee93976794325a14b96d00665f58f022774ab6f79e4a8df.jpg)  
Fig. 6.5: Global covariance function of gravity anomalies, model Tscherning and Rapp (1974).

The anomaly degree variance model reads

$$
\sigma _ { _ { I } } ^ { 2 } ( \Delta g ) = \left\{ \begin{array} { l l } { 0 } & { \mathrm { ~ f o r ~ } I = 0 , 1 } \\ { 7 5 4 \mathrm { ( \mu m s ^ { - 2 } ) ^ { 2 } } } & { \mathrm { ~ f o r ~ } I = 2 } \\ { \displaystyle \frac { A ( I - 1 ) } { ( I - 2 ) ( I + B ) } \sigma _ { _ { 0 } } ^ { I + 2 } } & { \mathrm { ~ f o r ~ } I \geq 3 } \end{array} \right. ,
$$

with $A = 4 2 ~ 5 2 8$ and $B = 2 4$ . $\sigma _ { \scriptscriptstyle 0 } = { \bigl ( } R _ { \scriptscriptstyle B } / R { \bigr ) } ^ { 2 } = 0 . 9 9 9 6 1 7$ is the ratio between the radius of the Bjerhammar sphere (internal boundary surface for the harmonic development, cf. [3.3.2]), and the Earth’s radius, Fig. 6.6 shows the anomaly degree variances of the Tscherning-Rapp (1974) model and the more recent geopotential models EGM96 and EGM2008, cf. [6.6.2], where the latter one has been developed until degree and order 2159, see Arabelos and Tscherning (2010).

More details on the spherical harmonic development of different gravity fi eld quantities and their relation with degree variances and covariance functions will be given in [6.6.1] and [6.8.2].

![](images/5d6be73cb210585bddff0b42d216111ce433179ea518610c1bfcf587a15d83aa.jpg)  
Fig. 6.6: Anomaly degree variances, left: model Tscherning and Rapp (1974) and geopotential SPHERICAL HARMONIC DEGREE model EGM96 (after Lemoine et al., 1998); right: EGM96 (green), EIGEN-GL04C (blue) and EGM2008 (red) (after Arabelos and Tscherning, 2010).

![](images/c0e17007cab485fef105634336801bd11cd99f6a2b5cfd23df09b0ab7d4834e0.jpg)  
Fig. 6.7: Local covariance functions of trend-removed $6 ^ { \prime } \times 1 0 ^ { \prime }$ mean free air anomalies (Torge et al., 1984).

For regional applications, a covariance function may be derived by subtracting the long-wave part from the global function, which results in a decrease in the variance and a shortening of the correlation length. Local gravity fi eld interpolation is even possible by a plane covariance function, e.g., the Gauss function

$$
C ( \psi ) = C _ { 0 } e ^ { - A ^ { 2 } \psi ^ { 2 } } ,
$$

see Fig. 6.7.

It should be noted that covariance functions have to be positive defi nite. This condition is fulfi lled for (6.24), as all coeffi cients according to (6.26) are non-negative, as well as for (6.28).

An important application of the anomaly covariance function is the interpolation of gravity anomalies at points or areas not surveyed. Simple interpolation methods such as the manual construction of iso-anomaly maps or the geometric interpolation using adjacent data are not ideal and do not deliver optimum results. Least-squares prediction, on the other hand, utilizes the statistical information inherent in the covariance function and takes the errors of the observations into account.

In the usual linear prediction, the (unknown) gravity anomaly at the point $P$ is estimated by a linear function of the anomalies observed at the points $P _ { _ i } ( _ i = 1 , . . . , n )$ . We assume that, in addition to the covariance function of the anomalies, an error covariance function is also available, describing the statistical behavior of the data errors. It can be derived from a priori error and error correlation estimates, where the demands on homogeneity and isotropy have to be fulfi lled again. Generally the error covariances are unknown, and the error model has to be restricted onto the error variances. Among the rare examples of error covariance functions are the analytical approximations, based on overlapping data of different sea gravimetry surveys carried out around Europe (Weber and Wenzel, 1983).

Based on the statistical information on the gravity anomalies and their errors, the following covariances, for any distance $\psi ,$ can be calculated:

$C _ { { \scriptscriptstyle P } _ { i } } = M \{ \Delta g _ { { \scriptscriptstyle P } } \Delta g _ { { \scriptscriptstyle i } } \} ;$ : cross-covariance of $\Delta g _ { p }$ with the observation $\Delta { g } _ { i ^ { \prime } }$

$C _ { _ { i j } } = M \{ \Delta g _ { i } \Delta g _ { _ { j } } \}$ : auto-covariance of the observations,

$D _ { _ { i j } } = M \{ n _ { _ { i } } n _ { _ { j } } \}$ : auto-covariance of the observational errors (noise $n$ ), and combined into

$$
\mathbf { C } _ { p } ^ { \mathsf { T } } = \left( C _ { _ { P _ { \uparrow } } } . . . , C _ { _ { P _ { \uparrow } } } . . . , C _ { _ { P _ { \downarrow } } } \right)
$$

Now, the prediction error is introduced, being the difference between the true gravity anomaly and the predicted value $\Delta \hat { g } .$ The requirement of a minimum prediction error variance, in analogy to least-squares adjustment, leads to the predicted anomaly, as the result of least-squares prediction

$$
\Delta \hat { g } _ { P } = \mathbf { C } _ { P } ^ { \intercal } \overline { { \mathbf { C } } } ^ { - 1 } \Delta \mathbf { g } ,
$$

where the observed anomalies have been collected in the vector

$$
\begin{array} { r } { \Delta \mathbf { g } ^ { \intercal } = ( \Delta g _ { 1 } , \quad \ldots \quad \Delta g _ { i ^ { \prime } } \quad \ldots \quad \Delta g _ { n } ) . } \end{array}
$$

Under the (plausible) assumption that the gravity anomalies and their errors are not correlated, the corresponding matrices __ $\mathbf { C }$ and $\mathbf { D }$ can be added element by element, leading to the combined matrix $\bar { \mathbf { C } }$ appearing in (6.30):

$$
{ \overline { { \mathbf { C } } } } = \mathbf { C } + \mathbf { D } .
$$

The prediction of point free-air anomalies (based on a point anomaly covariance function) is successful only for very densely surveyed areas, as these anomalies strongly depend on height. A smoother gravity anomaly fi eld with improved possibility of interpolation is obtained by calculating mean anomalies over larger surface elements (e.g., $5 ^ { \prime } \times 5 ^ { \prime }$ , $3 0 ^ { \prime } \times 3 0 ^ { \prime }$ ). An effective smoothing is obtained by reducing the effect of the topographic masses, and eventually also geological mass anomalies, where Bouguer and isostatic anomalies are especially well suited for interpolation, cf. [6.5.3]. As well known from least-squares adjustment theory, the predicted values of the gravity anomalies are relatively independent from the choice of the covariance function, while the error estimates strongly depend on it. Realistic prediction results can be expected only within the correlation length defi ned by a covariance of ${ \frac { 1 } { 2 } } \sigma ^ { 2 } ( \Delta g )$ .

# 6.2 Three-dimensional positioning

Three-dimensional positioning is generally carried out in a Cartesian coordinate system; the use of ellipsoidal coordinates results in more complicated models [6.2.1]. The Geodetic Datum provides the orientation of the three-dimensional model with respect to the global geocentric system [6.2.2]. Three-dimensional modeling has been early proposed by Bruns (1878), and taken up, expanded and carefully investigated since the

1950s by Hotine (1969), Wolf (1963a, b), Grafarend (1978a), also Hofmann-Wellenhof and Moritz (2005, p. 208 ff.).

# 6.2.1 Observation equations

As usual, the observation equations relate the observed quantities to the unknown station coordinates and other parameters (functional model). By “observations” we mean geometric quantities that result from preprocessing of the original measurements, such as signal travel time, phase and frequency, and readings on graduated circles or staffs, see the corresponding sections on geodetic measurement methods in [5]. We also assume that instrumental corrections have been applied (e.g., calibration) and that effects from the atmosphere (refraction) and the gravity fi eld (Earth tides) have been taken into account. The observation equations are mostly non-linear. They have to be linearized for the subsequent least-squares adjustment, which also includes the treatment of the errors of the observations (stochastic model), see references given at the beginning of this chapter.

The “observations” used for three-dimensional positioning may be divided into space and terrestrial measurements.

Space observations include satellite related • space directions, cf. [5.2.4], ranges derived from GNSS (GPS and other satellite systems) and laser distance measurements, cf. [5.2.5], [5.2.6], range rates from Doppler measurements, cf. [5.2.4].

We add

• baseline vectors obtained from VLBI, cf. [5.3.4].

Global and regional satellite and VLBI networks are nowadays adjusted separately, and independent from terrestrial geodetic data. The results (Cartesian coordinates or coordinate differences) can be introduced later as “observed” parameters into combined adjustments, together with other satellite networks or with terrestrial measurements. Naturally, the correlations produced by the previous adjustments (variance-covariance matrix) have to be taken into account in that case, cf. [2.5], [7.3].

Satellite observations provide the components of the observation vector s directed from the station $P$ to the satellite $S$ (Fig. 6.8). The vector $\pmb { S }$ is related to the geocentric station vector $\boldsymbol { r } _ { \scriptscriptstyle P }$ and the radius vector $r _ { s }$ of the satellite by

$$
\boldsymbol { \mathsf { r } } _ { P } + \boldsymbol { \mathsf { s } } - \boldsymbol { \mathsf { r } } _ { S } = \mathbf { 0 } ,
$$

with

$$
\boldsymbol { \mathsf { r } } _ { P } = \left( \begin{array} { l } { X _ { P } } \\ { Y _ { P } } \\ { Z _ { P } } \end{array} \right) , \quad \boldsymbol { \mathsf { r } } _ { s } = \left( \begin{array} { l } { X } \\ { Y } \\ { Z } \end{array} \right) , \quad \boldsymbol { \mathsf { r } } _ { s } - \boldsymbol { \mathsf { r } } _ { P } = \left( \begin{array} { l } { \Delta X _ { P } ^ { S } } \\ { \Delta Y _ { P } ^ { S } } \\ { \Delta Z _ { P } ^ { S } } \end{array} \right) .
$$

The “observation” vector is formed by the distance and the spatial direction (as obtained by optical direction measurements) to the satellite given in the hour angle system

$$
{ \bf s } = s \left( \begin{array} { c } { \cos h _ { _ { G r } } \cos \delta } \\ { \sin h _ { _ { G r } } \cos \delta } \\ { \sin \delta } \end{array} \right) ,
$$

![](images/6b66362ee3c04450f83f9f73c56aeb2dd2c1ea7a2b79862417069981bbbdc11f.jpg)  
Fig. 6.8: Satellite tracking principle.

where $\delta$ is the declination and

$$
h _ { _ { G r } } = \mathrm { G A S T } - \alpha
$$

is the Greenwich hour angle, cf. [2.4.1]. For the reductions to be applied to the original topocentric observations in order to obtain declination and Greenwich hour angle see [5.3.3].

Inserting (6.34) into (6.33) and solving for the components of $\pmb { S }$ yields the observation equations

$$
\left. \begin{array} { l } { \displaystyle h _ { _ { G r } } = \arctan \frac { \Delta Y _ { _ { P } } ^ { s } } { \Delta X _ { _ { P } } ^ { s } } } \\ { \displaystyle \delta = \arctan \frac { \Delta Z _ { _ { P } } ^ { s } } { \sqrt { \Delta X _ { _ { P } } ^ { s ^ { 2 } } + \Delta Y _ { _ { P } } ^ { s ^ { 2 } } } } } \\ { \displaystyle s = \sqrt { \Delta X _ { _ { P } } ^ { s ^ { 2 } } + \Delta Y _ { _ { P } } ^ { s ^ { 2 } } + \Delta Z _ { _ { P } } ^ { s ^ { 2 } } } } \end{array} \right] .
$$

Range differences to the satellite positions________________ _____ $( i , j )$ are given by_______

$$
s _ { j } - s _ { i } = \sqrt { \Delta X _ { P } ^ { j ^ { 2 } } + \Delta Y _ { P } ^ { j ^ { 2 } } + \Delta Z _ { P } ^ { j ^ { 2 } } } - \sqrt { \Delta X _ { P } ^ { i ^ { 2 } } + \Delta Y _ { P } ^ { i ^ { 2 } } + \Delta Z _ { P } ^ { i ^ { 2 } } } ,
$$

with

$$
\Delta X _ { _ { P } } ^ { j } = X _ { _ { j } } - X _ { _ { P } } \mathrm { e t c . , } \quad \Delta X _ { _ { P } } ^ { i } = X _ { _ { i } } - X _ { _ { P ^ { \prime } } } \mathrm { e t c . }
$$

If the directions to the quasars are known, VLBI observations deliver the baseline vector between two terrestrial stations $P _ { \uparrow }$ and $P _ { _ 2 }$ :

$$
\begin{array} { r } { \mathbf { b } _ { 1 , 2 } = \mathbf { r } _ { 2 } - \mathbf { r } _ { 1 } = \left( \begin{array} { l } { X _ { 2 } - X _ { 1 } } \\ { Y _ { 2 } - Y _ { 1 } } \\ { Z _ { 2 } - Z _ { 1 } } \end{array} \right) . } \end{array}
$$

The relations of the original measurements to the “observations” introduced as geometrical quantities in (6.36) to (6.38) are given by (5.42) for Doppler counts, (5.43) and (5.45) for GNSS, (5.48) for satellite laser ranging, and (5.68) for VLBI.

The observation equations contain a large number of parameters in addition to the station coordinates, and the coordinates of the satellites (orbital parameters) and the quasars, respectively. Among them are the Earth orientation parameters, which relate the terrestrial to the celestial reference frame, cf. [2.4.1], parameters describing temporal variations of the ground stations (e.g., Earth tides and crustal deformation effects), as well as the coeffi cients of the gravitational fi eld and other “disturbing” forces entering through satellite orbit modeling. There are two strategies to handle the large amount of data and unknown parameters. The fi rst one consists in estimating most of the unknowns in one adjustment process and to adopt only a few parameters (e.g., the Earth orientation parameters) from other sources. This leads to “satellite-only” Earth models, which provide a global set of station coordinates, the harmonic coeffi cients of the gravitational fi eld, and other parameters. If only positioning is intended, the station coordinates are the most important adjustment unknowns. Numerical values for the other parameters are then taken from corresponding models (e.g. the high precision orbital parameters as provided by operational services for GNSS and laser satellites, geopotential models, tropospheric refraction models, and others, cf. [5.2], [5.3]. If necessary, small corrections to the model values can also be derived (corrections to the Keplerian elements for short arcs, introduction of a local tropospheric scale factor, clock corrections, etc.)

As already discussed for GNSS observations, cf. [5.2.5], we may distinguish between absolute and relative positioning when evaluating the observation equations. Absolute positioning utilizes the satellite’s orbit (coordinates of the satellite as a function of time) and delivers geocentric station coordinates, with an accuracy directly depending on the quality of the orbital data. Relative positioning is based on simultaneous observations on two or more stations. It leads to purely geometric solutions which contain datum defi ciencies of a different kind. At least one station has to be known in order to fi x the origin of the network. A pure triangulation network requires a minimum of one measured distance for defi ning the scale, and a trilateration net would need orientation through the spatial direction to stars or quasars.

By differencing simultaneous observations a number of errors are eliminated or greatly reduced which is due to the high error correlation between neighboring stations. This strategy has been developed especially for the parameter estimation in GPS/ GNSS networks by introducing differences or linear combinations of the observables (code and carrier phases) into the adjustment (Teunissen and Kleusberg, 1998b). Since the absolute orientation is lost with this strategy, the absolute coordinates of at least one station have to be included into the adjustment model.

As a standard, “single differences” $S _ { 1 } ^ { A } - S _ { 2 } ^ { A }$ between the distances measured simultaneously from two receivers $P _ { \mathrm { \uparrow ^ { \prime } } }$ $P _ { _ 2 }$ to the satellite $A$ at epoch $t _ { \scriptscriptstyle i }$ are formed (Fig. 6.9). Thereby, the satellite clock errors are eliminated and refraction and orbital errors are reduced. “Double differences” are formed by differencing two single differences taken to different satellites $A _ { \iota }$ , $B$ at the same epoch $t _ { i } \colon \left( s _ { 1 } ^ { A } - s _ { 2 } ^ { A } \right) - \left( s _ { 1 } ^ { B } - s _ { 2 } ^ { B } \right) .$ . With double difference, the receiver clock errors vanish and refraction and orbital errors are further reduced. “Triple differences” are constructed by differencing two double differences taken at the epochs $t _ { \scriptscriptstyle i }$ and $t _ { j } .$ The ambiguity which enters into carrier phase measurements cancels in the observation equation. Due to the loss of information, triple differences allow reduced-accuracy positioning only but are useful for the detection and correction of cycle slips.

![](images/f4e19a102f95e61768a8935809578766c3fc9159481394b2955963b7f1216cd0.jpg)  
Fig. 6.9: GPS single, double and triple differences.

Sophisticated software packages are available for the adjustment of satellite networks; for GNSS networks we mention Wübbena (1989), Webb and Zumberge (1997), King and Bock 2005 and Dach et al. (2007). The adjustment delivers the Cartesian coordinates or coordinate differences of the ground stations and their full variance-covariance matrix, which has to be taken into account for further processing, e.g., for the combination with other space techniques and/or terrestrial data. If the orientation of the networks to be combined is not identical, a corresponding transformation (datum shift) has to be included in the adjustment, cf. [6.2.2].

Terrestrial measurements include (traditionally, astronomic observations to fi xed stars are included here)

• Astronomic azimuths, latitudes, and longitudes, cf. [5.3.2],   
Horizontal directions (which can be regarded as azimuths without orientation) and horizontal angles (corresponding to differences of azimuths), cf. [5.5.1], Zenith angles, cf. [5.5.1], Distances, cf. [5.5.2], Leveled height differences, cf. [5.5.3].

Terrestrial measurements have been classically evaluated separately for horizontal position and for height, cf. [6.3], [6.4]. The resulting control networks are nowadays transformed to the global reference frame, provided by space methods. This is done by connection to the global network and (at least partial) remeasurement, with subsequent transformation. A joint evaluation of space and terrestrial observations is now restricted to local applications, with dimensions generally not exceeding a few kilometers. More details on the establishment and renewal of regional/local geodetic networks are given in [7.1] to [7.3].

By substituting (2.20) into (2.29) and taking (2.30) into account, we obtain the observation equations for azimuths A, zenith angles $Z ,$ and distances s:

$$
\left. \begin{array} { l } { { A = \arctan \displaystyle \frac { - \sin \Lambda \Delta X + \cos \Lambda \Delta Y } { - \sin \Phi \cos \Lambda \Delta X - \sin \Phi \sin \Lambda \Delta Y + \cos \Phi \Delta Z } } } \\ { { z = \operatorname { a r c c o s } \displaystyle \frac { \cos \Phi \cos \Lambda \Delta X + \cos \Phi \sin \Lambda \Delta Y + \sin \Phi \Delta Z } { \left( \Delta X ^ { 2 } + \Delta Y ^ { 2 } + \Delta Z ^ { 2 } \right) ^ { \frac { 1 } { 2 } } } } } \\ { { s = \left( \Delta X ^ { 2 } + \Delta Y ^ { 2 } + \Delta Z ^ { 2 } \right) ^ { \frac { 1 } { 2 } } } } \end{array} \right\} ,
$$

with

$$
\Delta X = X _ { 2 } - X _ { 1 } , \quad \Delta Y = Y _ { 2 } - Y _ { 1 } , \quad \Delta Z = Z _ { 2 } - Z _ { 1 } .
$$

Astronomic latitude $\Phi$ and astronomic longitude $\Lambda$ enter as orientation parameters in (6.39). They relate the local astronomic systems to the global geocentric system and are treated here as additional unknown parameters. If observed latitudes and longitudes are available, they may be introduced as observed parameters in the adjustment.

As mentioned previously, least-squares adjustment requires linear relations between the observations and the unknowns. Corresponding differential relations are derived by numerical or analytical differentiation of (6.39). Analytical expressions for the partial derivatives $\partial A / \partial X ,$ etc. are found in Wolf (1963b) and Hofmann-Wellenhof and Moritz (2005, p. 211 ff.).

Geometric leveling can be incorporated into three-dimensional computations after transformation of the leveled height difference $\delta n \approx d n$ (5.114) into the geocentric coordinate system. This is achieved by introducing the ellipsoidal height difference $d h ,$ as obtained by reducing dn for the effect of the (surface) defl ection of the vertical (Fig. 6.10). In the azimuth of the leveling line, the vertical defl ection component $\varepsilon ( 6 . 1 8 )$ is effective, which gives

$$
d h = d n - \varepsilon d s .
$$

The negative sign prefi xing e ds is based on the sign defi nitions inherent in (6.17) and (6.7) resp. (6.8). A differential relationship between the ellipsoidal height and $X , ~ Y , ~ Z$ is provided by (4.26a) and (4.27). With

$$
d { \bar { \mathbf { r } } } _ { Q } = \mathbf { 0 } ,
$$

and replacing $\varphi , \lambda$ with $\Phi , \Lambda ,$ we obtain

$$
d h = \bar { \bf n } ^ { \scriptscriptstyle \mathrm { I } } \cdot d { \bf r } = \cos \Phi \cos \Lambda \ d X + \cos \Phi \sin \Lambda \ d Y + \sin \Phi \ d Z .
$$

Again, we have assumed that the axes of the ellipsoidal and the geocentric system are parallel:

$$
d \overline { { { X } } } = d X , \quad d \overline { { { Y } } } = d Y , \quad d \overline { { { Z } } } = d Z .
$$

Integration of (6.40) yields the ellipsoidal height difference

$$
\Delta h _ { _ { 1 , 2 } } = h _ { _ { 2 } } - h _ { _ { 1 } } = \int _ { 1 } ^ { 2 } d n - \int _ { 1 } ^ { 2 } \varepsilon d s ,
$$

which can be included as an “observation” in three-dimensional computations: Geometric-astronomic leveling (Heitz, 1973). It is noted that both integrals in (6.42) have to be formed over the same path! The differential relation for (6.42) follows from differencing (6.41) for the points $P _ { \mathrm { \uparrow } }$ and $P _ { 2 }$ :

$$
d \big ( \Delta h _ { _ { 1 , 2 } } \big ) = d h _ { _ { 2 } } - d h _ { _ { 1 } } .
$$

![](images/6d1219afc70585324915ab04bf64f069e6f4694fc8cffb0aef11910654bdd18e.jpg)  
Fig. 6.10: Geometric-astronomic leveling.

The fi rst integral in (6.42) can easily be computed by summing the leveled height differences. The evaluation of the second integral poses diffi culties, as vertical defl ections (derived from geodetic astronomy) are generally only available at larger station distances (several $1 0 \mathrm { k m }$ in classical networks). This introduces the problem of the interpolation of defl ections of the vertical. In fl at and hilly areas, with an average distance of the vertical defl ection stations of 20 to $3 0 ~ \mathrm { k m } ,$ , an accuracy of about $0 . 1 ~ { \mathrm { m } } / 1 0 0 { \mathrm { k m } }$ can be achieved for the ellipsoidal height differences. If $^ { \prime \prime } { \mathrm { C } } { \sf m } ^ { \prime \prime }$ -accuracy is required, station distances of a few km and sophisticated interpolation methods are required (Torge, 1977; Hirt and Flury, 2008). By reducing the station distance to about $1 ~ \mathrm { k m }$ and taking into account topography, even $" \mathrm { m m } ^ { \prime \prime }$ -accuracy can be achieved over distances of a few km, cf. [6.7.4].

The three-dimensional concept based on terrestrial observations was already introduced by Villarceau (1868) and Bruns (1878). Bruns suggested a point-wise determination of the Earth’s surface by a spatial polyhedron constructed from terrestrial measurements and orientated by astronomical observations. The feasibility of this concept was demonstrated in some test networks (e.g., Torge and Wenzel, 1978), but large-scale application was prevented due to the uncertainties of trigonometrical height transfer over larger distances and the problems with reducing geometric leveling to ellipsoidal height differences.

Ellipsoidal coordinates $\varphi , \lambda ,$ and sometimes also $h$ are used for numerous applications in geodesy, geomatics and cartography, and navigation. They can easily be derived from the Cartesian coordinates by the transformation (4.28). However, network adjustments in the $\varphi , \lambda , h \mathrm { . }$ -system are more complicated than in the $X , ~ Y ,$ Z-system, and therefore restricted to special cases. Nevertheless, differential relations between the observations and the ellipsoidal coordinates are useful for solving dedicated problems, e.g., for deriving reductions onto the ellipsoid and for two-dimensional ellipsoidal calculations, cf. [6.3.2], [6.3.3].

Equations (4.27) provide the fundamental relations between the _ _ $\varphi , ~ \lambda , ~ h -$ and the $\bar { \bar { X } } , \ \bar { \bar { Y } } , \ \bar { \bar { Z } } .$ -systems. Differentiation yields

$$
{ \binom { d \overline { { X } } } { d \overline { { Y } } } } = \overline { { \mathbf { A } } } \left( \begin{array} { c } { { ( M + h ) d \varphi } } \\ { { ( N + h ) \cos \varphi d \lambda } } \\ { { d h } } \end{array} \right) ,
$$

where $\overline { { \bf A } }$ is given by (4.32). Again we assume parallelism of the ellipsoidal and the Cartesian coordinate systems. Equation (6.44) can immediately be used if satellite derived coordinates or coordinate differences are to be adjusted in the $\varphi , \lambda , h \cdot$ -system. Differential formulas for the terrestrial observations $A , \ z ,$ s are obtained by inserting (6.44) into the differential relations for Cartesian coordinates and reordering (Wolf, 1963b; Heiskanen and Moritz, 1967, p. 220 ff.), cf. [6.3.2].

We fi nally mention the straightforward transformation from the “natural” coordinates $\Phi , \Lambda ,$ and $H$ (orthometric height) or $H ^ { N }$ (normal height) to ellipsoidal coordinates $\varphi , \lambda ,$ $h ,$ where $H$ and $H ^ { N }$ are derived from the gravity potential $W$ by (3.106) and (3.107), respectively. According to (6.17), the defl ection of the vertical $( \xi , \eta )$ transforms from the plumb line direction to the ellipsoidal normal:

$$
\varphi = \Phi - \xi , \quad \lambda = \Lambda - \frac { \eta } { \cos \varphi } .
$$

If normal geodetic coordinates $\rho ^ { N } , \lambda ^ { N } ( 4 . 7 3 )$ are required, the curvature of the normal plumb line has to be taken into account by $\delta \varphi ^ { N } \left( 4 . 7 4 \right)$ :

$$
\varphi ^ { N } = \Phi - \left( \xi + \delta \varphi ^ { N } \right) = \Phi - \xi ^ { N } , \quad \lambda ^ { N } = \lambda = \Lambda - \frac { \eta } { \cos \varphi } .
$$

The relation between $h$ and $H$ respectively $H ^ { N }$ is given by, see Fig. 6.2:

$$
h = H + N = H ^ { N } + \zeta ,
$$

where we have neglected the small (sub-mm order of magnitude) effect of the plumb line curvature.

As shown in [6.7], gravimetric evaluation techniques allow the calculation of the defl ection of the vertical and the geoid height or the height anomaly from gravity fi eld data. Equations (6.45) and (6.46) thus would permit to establish a geocentric system of ellipsoidal coordinates. This led to the idea of establishing a world geodetic system from “natural” coordinates and gravimetric corrections, which was pursued since the 1950s, exploiting the (at that time) sparse gravity data available especially on the northern hemisphere (Heiskanen 1951). This strategy had to be abandoned with the success of satellite geodesy, taking also into account the fact that astronomical latitude and longitude generally can be determined only with an accuracy of $0 . 1 { ^ { \prime \prime } }$ (corresponding to $3 \textrm { m }$ in horizontal position) or less. The height transformation (6.46), on the other hand, has obtained high relevance, as it permits the connection of GNSS-derived ellipsoidal heights with heights determined by geometric leveling, cf. [6.4.3].

# 6.2.2 Geodetic datum

The geodetic datum describes the orientation of any geodetic coordinate system with respect to the Earth’s body, cf. [2.3.3]. It can be expressed by a parameter set of three translations, three rotations and a scale factor (Drewes, 2009c). Generally, ellipsoidal coordinates are used at geodetic reference systems, in addition to or instead of spatial Cartesian coordinates. This requires the inclusion of two geometric ellipsoid parameters (semi-major axis and fl attening) into the datum parameter set.

We distinguish between reference networks based on space methods (satellites, VLBI) and classical geodetic networks, established by terrestrial measurements and geodetic astronomy. The former networks are directly related to the geocenter and the Earth’s spin axis, and thus are very close to a geocentric reference system as the ITRS, cf. [2.4.2]. Classical networks, on the other hand, could be orientated only by astronomical observations (position) and connection to mean sea level (height). This resulted in large deviations of the network’s origin from the geocenter, while the axes could be made approximately parallel to the geocentric system. Another consequence was the separate treatment of horizontal and vertical control networks, with corresponding horizontal and vertical datum, see below and [6.3.3], [7.1], [7.2].

We start with the most general case, the transformation of a non-geocentric $\bar { \lambda } , \bar { Y } , \bar { Z }$ -system into the geocentric $X ,$ Y, $Z .$ -system. This strategy can be directly applied to satellite-based networks, and after corresponding transformation, see [4.1.3] and below, also to classical ellipsoidal systems. The relation between the two systems is given by a similarity transformation in space, i.e., by three translations, three rotations, and a change in scale (Fig. 6.11):

$$
\mathbf { r } = \mathbf { r } _ { \mathrm { 0 } } + ( 1 + m ) \mathbf { R } _ { \big ( } \varepsilon _ { \overline { { \chi } } \prime } \varepsilon _ { \overline { { \gamma } } \prime } \varepsilon _ { \overline { { Z } } \big ) } \overline { { \mathbf { r } } } .
$$

![](images/3cf97f0038a80b8c2397d45813401df6883fa0c387bd77b61aae04b2dd34dd7f.jpg)  
Fig. 6.11: Transformation between 3D-Cartesian coordinate systems.

Here, $\boldsymbol { \mathsf { r } } ^ { \mathsf { T } } = ( X , \ Y , Z )$ and $\overline { { \mathbf { r } } } ^ { \mathrm { T } } = \left( \overline { { X } } , \ \overline { { Y } } , \ \overline { { Z } } \right)$ are the position vectors in the two systems, __ and $\boldsymbol { \mathsf { r } } _ { 0 } ^ { \mathrm { { T } } } = \big ( X _ { 0 } , \ Y _ { 0 ^ { \prime } } \ Z _ { 0 } \big )$ contains the coordinates of the origin $\overline { O }$ of the $X , ~ Y , ~ Z .$ -system with respect to the geocenter $O _ { \ l }$ . We assume that the scale of the ${ \overline { { X } } } , { \overline { { Y } } } ,$ $\overline { Z }$ -system differs only slightly from the scale of the global reference system, and that the axes of the two systems are approximately parallel. Consequently, $m$ is a small scale correction, and the rotation matrix is composed of three small Eulerian angles; it takes the form

$$
\begin{array} { r } { \mathsf { R } ( \varepsilon _ { \bar { \chi } } , \varepsilon _ { \bar { \chi } } , \varepsilon _ { \bar { \gamma } } , \varepsilon _ { \bar { \zeta } } ) = \left( \begin{array} { l l l } { 1 } & { \varepsilon _ { \bar { \zeta } } - \varepsilon _ { \bar { \ Y } } } \\ { - \varepsilon _ { \bar { \zeta } } } & { 1 } & { \varepsilon _ { \bar { \chi } } } \\ { \varepsilon _ { \bar { \ Y } } } & { - \varepsilon _ { \bar { \chi } } } & { 1 } \end{array} \right) . } \end{array}
$$

In order to determine the seven parameters of the transformation (6.47), at least three points with seven coordinates given in both systems are required.

The parameters of a geodetic datum are provided indirectly by measurements carried out at control points located on the surface of the Earth. These data contain a multitude of time-variable effects, stemming from the gravity fi eld and tides, from atmosphere, hydrosphere and cryosphere, as well as from crustal motion and deformation. With present-day accuracies, a large part of these effects signifi cantly affects the results of geodetic networks, i.e. the coordinates of the reference frame’s control points, where temporal variations should be corrected by appropriate models. In this connection, a clear distinction should be made between the reference frame with stations moving with time and the geodetic datum, which should be fi xed over a longer time span (Drewes, 2009c). Here, the fi rst and second degree spherical harmonic coeffi cients of the gravitational fi eld play a special role, as they independently control shifts of the Earth’s center of mass and the (timevariable) axis of rotation, cf. [3.3.4].

After converting the Cartesian coordinates into ellipsoidal ones (6.47) can be expressed in ellipsoidal coordinates $\varphi , \lambda , h .$ . The datum parameters in that case also have to include the geometric parameters of the ellipsoid, i.e., the semi-major axis a and the fl attening $f .$ Of practical interest are the changes of the ellipsoidal coordinates that result from a datum transformation, i.e., from translation, rotation, change in scale, and change of the parameters of the ellipsoid. We insert (4.27) into (6.47) and take the total differential. As the real position of $P$ does not change, we have $d \mathbf { r } = \mathbf { 0 }$ . Neglecting the linear scale factor (which can be easily introduced again at all metric quantities) and substituting the differentials by (small) differences, a spherical approximation $( M + h = N + h = a$ , $f = 0$ ) yields (Merry and Vanicˇek, 1974):

$$
( \begin{array} { c } { a \delta \varphi } \\ { a \cos \varphi \delta \lambda } \\ { \delta h } \end{array} ) = - \overline { { \mathbf { A } } } ^ { - 1 } \delta \mathbf { r } _ { 0 } + \mathbf { C } \Bigg ( \begin{array} { c } { \delta \varepsilon _ { \overline { { X } } } } \\ { \delta \varepsilon _ { \overline { { Y } } } } \\ { \delta \varepsilon _ { \overline { { Z } } } } \end{array} ) + \mathbf { F } \Bigg ( \begin{array} { c } { \delta a } \\ { a } \end{array} \Bigg ) ,
$$

where $\mathbf { A } ^ { - 1 }$ is given by (4.34) and

$$
\mathbf { C } = a \left( \begin{array} { c c c } { \sin \lambda } & { - \cos \lambda } & { 0 } \\ { - \sin \varphi \cos \lambda - \sin \varphi \sin \lambda } & { \cos \varphi } \\ { 0 } & { 0 } & { 0 } \end{array} \right) , \quad \mathbf { F } = \left( \begin{array} { c c c } { 0 } & { \sin 2 \varphi } \\ { 0 } & { 0 } \\ { - 1 } & { \sin ^ { 2 } \varphi } \end{array} \right) .
$$

Equations (6.49) can be used for estimating the changes of the coordinates if the changes of the parameters of the geodetic datum are known. All differences are formed in the sense geocentric minus non-geocentric, e.g., $\delta \boldsymbol { a } = \boldsymbol { a } ( \mathrm { g e o c e n t r i c } ) - \boldsymbol { a } ($ (non-geocentric). Formulas which take the fl attening into account are given by Abd-Elmotaal and El-Tokhey (1995).

Classical geodetic networks, cf. [7.1], have been orientated by the ellipsoidal coordinates of an initial (or fundamental) point $P _ { _ { F } }$ and by condition equations for the parallelism of the axes with respect to the geocentric system: “local geodetic datum”, the distance to the geocenter remained unknown. If we apply (6.49) at a running point $P$ and at the fundamental point $P _ { { } _ { F ^ { \prime } } }$ the translation can be expressed in changes $\delta \varphi _ { _ { F } } , \delta \lambda _ { _ { \mathrm { F } ^ { \prime } } }$ $\delta h _ { _ { \mathtt { F } } }$ of the fundamental point. An equivalent relation can be derived by substituting the ellipsoidal coordinates through the (small) residual quantities defl ection of the vertical and geoid height, cf. [6.2.1]. By differentiating (6.45) and (6.46), and considering that because of $d \mathbf { r } = \mathbf { 0 }$ also $d \Phi = d \Lambda = d { \sf H } = 0$ , we obtain

$$
\delta \xi = - \delta \varphi , \quad \delta \eta = - \cos \varphi \delta \lambda , \quad d N = d h .
$$

Corresponding equations hold for the “normal” geodetic coordinates, cf. [4.2.3]. Hence, the coordinate changes at any point also can be expressed as changes of the defl ection of the vertical and the geoid height (or height anomaly), depending on the corresponding changes in the fundamental point (Vening-Meinesz, 1950). Spherical approximation yields (Heiskanen and Moritz, 1967, p. 208)

$$
\begin{array} { r l } & { d \tilde { c } ^ { 2 } = ( \cos \theta _ { e } \cos \phi + \sin \theta _ { e } \sin \phi - \sin \theta _ { e } \sin \phi - \sin \theta _ { e } \sin \phi ) d \xi , } \\ & { \qquad - \sin \theta _ { e } \sin \{ 2 - \tilde { \lambda } _ { e } \} d \eta _ { e } } \\ & { \qquad - ( \sin \theta _ { e } \cos \theta - \cos \theta _ { e } \sin \phi \cos ( 2 - \tilde { \lambda } _ { e } ) ) d \xi } \\ & { \qquad \times \{ \frac { d N _ { \Gamma } } { 2 } + \frac { d } { d \tau } + \sin \{ \eta ^ { 2 } \phi _ { e } d \} - 2 \cos \phi \{ \sin \theta - \sin \phi _ { e } \sin \{ d \} } \\ & { \qquad \quad + \eta ^ { 3 } \cos \{ \sin \theta _ { e } \sin ^ { 2 } \cdot \sin \theta _ { e } \sin \xi \} d \xi + \cos \{ \lambda - \tilde { \lambda } _ { e } \} d \eta _ { e } , } \\ & { \qquad \quad + \cos \theta _ { e } \sin \{ \lambda - \tilde { \lambda } _ { e } \} \{ \frac { d N _ { \Gamma } } { 2 } + \frac { d } { d \tau } + \sin \{ \theta _ { e } \sin ^ { 2 } \theta _ { e } d \} d \xi , } \\ & { \qquad \quad + \cos \{ \{ \cos \theta _ { e } \sin \phi - \sin \theta _ { e } \cos \phi \cos \{ 2 - \tilde { \lambda } _ { e } \} d \} d \xi _ { e } } \\ & { \qquad \quad - \alpha \cos \phi \sin \{ 2 - \tilde { \lambda } _ { e } \} d \eta _ { e } } \\ & { \qquad \quad + \{ \sin \theta _ { e } \sin \phi + \cos \phi _ { e } \cos \phi \cos \{ 2 - \tilde { \lambda } _ { e } \} \} } \\ & { \qquad \times ( d \sin \phi _ { e } + \sin \phi \cos \phi _ { e } \cos \phi - \sin \phi _ { e } ) } \\ & { \qquad \times ( d N _ { \Gamma } + d + \sin \phi _ { e } \sin \phi _ { e } d ) d \xi - d \alpha } \\ & { \qquad + \{ \sin \theta _ { e } \cos 2 \phi \sin \phi _ { e } \sin \phi \} d \xi , } \end{array}
$$

These relations have played a role in the optimum fi tting of horizontal control networks to the geoid, cf. [7.1].

We now investigate how the (approximate) parallelism of the axes of classical geo detic networks with respect to the geocentric system has been achieved.

We describe the deviation between the local astronomic_ _ _ $x ,$ y, z-system (2.20) and the local ellipsoidal_ ${ \overline { { x } } } , { \overline { { y } } } ,$ ${ \overline { { Z } } } .$ -system (4.29) by three (small) Eulerian angles, after refl ection of the $\gamma$ and $\overline { { y } }$ -axes (generating right-handed systems), Fig. 6.12:

$$
\mathbf { x } = \mathbf { R } ( \xi , \eta , \psi ) \overline { { \mathbf { x } } } ,
$$

with the rotation matrix

$$
\begin{array} { r } { \mathbf { R } ( \xi , \eta , \psi ) = \left( - { \psi \begin{array} { l } { 1 } \\ { - \psi \begin{array} { c } { 1 } \\ { \xi } \end{array} } { \eta } } \end{array} \right) . } \end{array}
$$

The Eulerian angles are the components of the defl ection of the vertical, cf. [6.1.2], in the meridian $( \xi ) ,$ in the prime vertical $( \eta ) ,$ , and in the horizontal plane $( \psi )$ . If the axes of the global $X , ~ Y , Z -$ and ${ \overline { { X } } } , { \dot { \overline { { Y } } } } ,$ ${ \overline { { Z } } } .$ -systems are not parallel, the following relations hold, according to (2.26), (4.29), (6.47), and (6.52):

$$
\Delta \mathbf { X } = \mathbf { A } \mathbf { x } = \mathbf { A } \mathbf { R } ( \xi , \eta , \psi ) \ \overline { { \mathbf { x } } } = \mathbf { R } _ { \left( \mathcal { E } _ { \overline { { X } } } , \mathcal { E } _ { \overline { { Y } } } , \mathcal { E } _ { \overline { { Z } } } \right) } \ \overline { { \mathbf { A } } } \overline { { \mathbf { x } } }
$$

or

$$
\begin{array} { r } { \pmb { \mathrm { R } } ( \mathcal { E } _ { \bar { \chi } } , \mathcal { E } _ { \bar { \chi } } , \mathcal { E } _ { \bar { Z } } ) \overline { { \mathbf { A } } } = \mathbf { A } \mathbf { R } ( \xi , \eta , \psi ) . } \end{array}
$$

After inserting $\bar { \bf A } ( 4 . 3 2 )$ and A (2.28), the evaluation of (6.54) results in nine equations. Three of the nine equations are independent from each other (orthogonality relations). After Taylor expansion of the trigonometrical functions of $\Phi , \Lambda$ inherent in (2.28) at the point $( \varphi , \lambda ) ,$ we obtain the components (linear approximation) of the defl ection of the vertical if the axes of the global systems are not parallel :

$$
\left. \begin{array} { l } { { \xi = \Phi - \varphi + \sin \lambda \varepsilon _ { \bar { \lambda } } - \cos \lambda \varepsilon _ { \bar { \lambda } } } } \\ { { \eta = \left( \Lambda - \lambda \right) \cos \varphi - \sin \varphi \left( \cos \lambda \varepsilon _ { \bar { \lambda } } + \sin \lambda \varepsilon _ { \bar { \gamma } } \right) + \cos \varphi \varepsilon _ { \bar { z } } } } \\ { { \psi = \left( \Lambda - \lambda \right) \sin \varphi + \cos \varphi \left( \cos \lambda \varepsilon _ { \bar { \lambda } } + \sin \lambda \varepsilon _ { \bar { \gamma } } \right) + \sin \varphi \varepsilon _ { \bar { z } } } } \end{array} \right. .
$$

![](images/7d17aec0b9dd24fd826706de5370bd0ea471503ea67bdbd5854db4ce547cbcf0.jpg)  
Fig. 6.12: Rotations between the local ellipsoidal and the local astronomic system.

We also generalize the equations for the azimuth and the zenith angle given in the local astronomic and the local ellipsoidal system. From (6.53) we have

$$
\begin{array} { r } { \mathbf { A } \mathbf { x } = \mathbf { R } \big ( \mathcal { E } _ { \overline { { X } } } , \mathcal { E } _ { \overline { { Y } } } , \mathcal { E } _ { \overline { { Z } } } \big ) \overline { { \mathbf { A } } } \overline { { \mathbf { x } } } . } \end{array}
$$

Inserting (2.20) and (4.29) yields, after linearization of the trigonometrical functions of $A , z$ at $\alpha , \zeta$ :

$$
\begin{array} { l } { { A - \alpha = ( \Lambda - \lambda ) \sin \varphi + ( ( \Phi - \varphi ) \mathrm { s i n } \alpha - \cos \varphi ( \Lambda - \lambda ) \mathrm { c o s } \alpha ) \mathrm { c o t } \zeta } } \\ { { \qquad + \cos \varphi \bigl ( \cos \lambda \varepsilon _ { \bar { X } } + \sin \lambda \varepsilon _ { \bar { Y } } \bigr ) + \sin \varphi \varepsilon _ { \bar { Z } } , } } \\ { { \ } } \\ { { z - \zeta = - ( ( \Phi - \varphi ) \cos \alpha + \cos \varphi ( \Lambda - \lambda ) \mathrm { s i n } \alpha ) } } \\ { { \qquad - ( \cos \alpha \sin \lambda - \sin \alpha \sin \varphi \cos \lambda ) \varepsilon _ { \bar { X } } } } \\ { { \qquad + ( \cos \alpha \cos \lambda + \sin \alpha \sin \varphi \sin \lambda ) \varepsilon _ { \bar { Y } } } } \\ { { \qquad - \cos \varphi \sin \alpha \varepsilon _ { \bar { Z } } . } } \end{array}
$$

We now require parallelism of the axes, setting

$$
\varepsilon _ { \bar { \chi } } = \varepsilon _ { \bar { \ Y } } = \varepsilon _ { \bar { Z } } = 0 .
$$

(6.55) and (6.56) then transform into condition equations for the parallelism of the axes of the global and the local system. This was already presupposed when introducing the defl ections of the vertical, in [6.1.2]. For the defl ection of the vertical these equations obtain the form

$$
\left. \begin{array} { c } { { \xi = \Phi - \varphi , \quad \eta = \left( \Lambda - \lambda \right) \cos \varphi } } \\ { { \psi = \left( \Lambda - \lambda \right) \sin \varphi } } \end{array} \right\} .
$$

The condition equations for the azimuth and the zenith angle now read as

$$
A - \alpha = \eta \tan \varphi + \left( \xi \sin \alpha - \eta \cos \alpha \right) \cot \zeta
$$

and

$$
Z - \zeta = - ( \xi \cos \alpha + \eta \sin \alpha ) .
$$

Equation (6.58) is known as Laplace’s equation of orientation, while (6.59) furnishes the component $\varepsilon$ of the defl ection of the vertical in the azimuth $\alpha \left( 6 . 1 8 \right) _$ , Vanicˇek and Wells (1974).

A geometric interpretation of the condition equations (6.58) and (6.59) reveals that they prevent rotations about the vertical and the horizontal axis of a theodolite. In addition, a rotation about the line of sight must be prevented in order to guarantee the parallelism of the global and the ellipsoidal system. This can be accomplished if, in addition to (6.58) and (6.59), another zenith angle equation is introduced at the fundamental point, possibly with an azimuth which differs by $9 0 ^ { \circ }$ . Due to the problems of vertical refraction, classical geodetic networks generally employed only the Laplace equation for orientation. A three-dimensional network then would need at least three Laplace azimuths at points well distributed over the network (Vincenty, 1985). In reality, only horizontal control networks were built up by reducing observed azimuths and horizontal directions onto the ellipsoid utilizing (6.58) for the reduction, cf. [6.3.2]. In order to achieve parallelism of the axes, at least one Laplace equation then had to be fulfi lled at this two-dimensional positioning, cf. [7.1.2]. The reduction (6.59), on the other hand, plays an important role for trigonometric height determination, cf. [6.4.2].

# 6.3 Horizontal positioning

In classical geodetic networks, horizontal positioning (with an ellipsoid as reference surface) has been separated from height determination (referring to the geoid), although a three-dimensional concept for geodetic modeling was early available (Bruns, 1878), cf. [1.3.4] and [6.2]. This is due to the fact that ellipsoidal height differences to be derived from geometric leveling or zenith angles were affected by large uncertainties, which entered through the necessary reductions of gravity fi eld related effects (geoid heights and defl ections of the vertical, respectively) and of vertical refraction. The separate treatment of horizontal and vertical coordinates was readily accepted by the users of geodetic products, especially because gravity fi eld related heights are generally required in practice. The possibility to directly compute ellipsoidal coordinates from GNSS-derived Cartesian coordinates, cf. [4.1.3], has strongly diminished the importance of horizontal positioning on the ellipsoid. In the following, we concentrate on some fundamentals of ellipsoidal geodesy, an extensive treatment is found in textbooks such as Grossmann (1976), Bomford (1980), and Heck (2003a).

With the ellipsoid as a reference surface, two-dimensional positioning requires ellipsoidal trigonometry [6.3.1] and reductions of the observed positional quantities onto the ellipsoid [6.3.2]. Ellipsoidal “observation” equations then allow the calculation of coordinates, after proper orientation of the ellipsoidal network with respect to the Earth’s body [6.3.3].

# 6.3.1 Ellipsoidal trigonometry

In order to carry out computations on the ellipsoidal surface, points on the ellipsoid are connected by surface curves. The arc of the normal section and the geodesic are primarily employed.

The normal section is defi ned by the curve of intersection of the vertical plane with the ellipsoid. Azimuths and distances, after being reduced to the ellipsoid, refer to normal sections. Since the surface normals of two points on the ellipsoid are in general skewed to each other, the reciprocal normal sections from $P _ { \mathrm { \uparrow } }$ to $P _ { \mathrm { { \gamma } } }$ and from $P _ { _ 2 }$ to $P _ { \mathrm { \uparrow } }$ do not coincide (Fig. 6.13). The differences in azimuth (less than $0 . 1 ^ { \bar { \prime } \prime }$ for $S = 1 0 \bar { 0 } \mathrm { k m } )$ ) and in distance (less than $1 ~ \mu \mathrm { m }$ for $S = 1 0 0 ~ \mathrm { k m } )$ are small and can be taken into account easily (Bowring, 1971).

![](images/f72024b59b27eb9100e9522de27968838e6c01fe1a6db175fdf15c2c30b80f5d.jpg)  
$S _ { n }$ $S _ { g } .$

Normally, because of its favorable properties, the geodesic is used for ellipsoidal calculations. It is uniquely defi ned as the shortest connection between two points and is generally bounded by the two normal sections. This defi nition is equal to the condition that the geodetic curvature (curvature of the normal projection of a surface curve onto the tangential plane) equals zero.

As known from differential geometry, the geodetic curvature $k _ { g }$ is represented by the triple scalar product

$$
k _ { g } = ( \mathbf { r } ^ { \prime } \times \mathbf { r } ^ { \prime \prime } ) \cdot \mathbf { n } .
$$

Here, $\mathbf { r } ^ { \prime } = d \mathbf { r } / d S$ is the tangent vector and $\mathbf { r } ^ { \prime \prime } = d ^ { 2 } \mathbf { r } / d S ^ { 2 }$ is the curvature vector. Also, $S$ arc length of the geodesic, and n designates the normal vector to the surface. With $k _ { _ { g } } = 0$ , we obtain a second-order vectorial differential equation for the geodesic :

$$
( { \bf r } ^ { \prime } \times { \bf r } ^ { \prime \prime } ) \cdot { \bf n } = 0 ,
$$

the local projection of the geodesic onto the tangential plane is a straight line. We now introduce the $\varphi , \lambda$ -system of ellipsoidal coordinates (Fig. 6.14) and express the geodesic by the function $\lambda = \lambda ( \varphi )$ . Corresponding evaluation of (6.61) yields the scalar differential equations

$$
\begin{array} { c } { { p ^ { 2 } \displaystyle \frac { d ^ { 2 } \lambda } { d \varphi ^ { 2 } } + 2 p \displaystyle \frac { d p } { d \varphi } \displaystyle \frac { d \lambda } { d \varphi } = 0 } } \\ { { M \displaystyle \frac { d M } { d \varphi } - p \displaystyle \frac { d p } { d \varphi } \displaystyle ( \displaystyle \frac { d \lambda } { d \varphi } ) ^ { 2 } = 0 } } \end{array} ) ,
$$

with $p = N \cos \varphi$ radius of the circle of latitude (4.6) and the principal radii of curvature $M$ and $N \left( 4 . 1 3 \right)$ , (4.15).

From Fig. 6.14, we take the relations

$$
\frac { d \varphi } { d S } = \frac { \cos \alpha } { M } , \quad \frac { d \lambda } { d S } = \frac { \sin \alpha } { N \cos \varphi }
$$

which are valid for any surface curve. We form $d \lambda / d \varphi$ and the second derivative and insert them into (6.62). Integration yields Clairaut’s equation

$$
N \cos \varphi \sin \alpha = { \cos \varphi } .
$$

The constant corresponds to the radius of the parallel circle at which the geodesic has an azimuth of $9 0 ^ { \circ }$ . By differentiation with respect to $S ,$ and taking (6.63) into account, (6.64) is transformed into the equivalent relation

$$
\frac { d \alpha } { d S } = \frac { \sin \alpha \tan \varphi } { N } .
$$

![](images/240e701f0c35cbe2129d806b76eb718e5a56d7750dd996d668d3a88fc7b5dc3f.jpg)  
Fig. 6.14: Ellipsoidal (geodetic) surface coordinates.

Equations (6.63) and (6.64) resp. (6.65) form a system of fi rst-order differential equations for the geodesic. The solution of this system leads to elliptic integrals which cannot be solved elementarily, cf. [6.3.3].

Two-dimensional positioning on the ellipsoid implies the solution of ellipsoidal triangles, bounded by geodesics. According to (4.18), the curvature of ellipsoidal surface curves depends on latitude and azimuth. As a consequence, the solution of a triangle not only requires three geometric elements (angles, distances) but also latitude and azimuth for orientation on the surface.

At point distances less than $1 0 0 ~ \mathrm { k m }$ (classical terrestrial networks) the ellipsoid may be approximated by the Gaussian osculating sphere (4.23), with the latitude calculated as an arithmetic mean of the latitudes of the triangle vertices. Closed spherical formulas then can be used for the solution of triangles, e.g., the spherical law of sines

$$
\frac { \sin \alpha } { \sin \beta } = \frac { \sin ( a / R ) } { \sin ( b / R ) } ,
$$

with the spherical angles $\alpha , \beta$ and sides a, $b ,$ $R$ is the radius of the Gaussian sphere. Errors due to the spherical approximation remain less than $0 . 0 0 2 ^ { \prime \prime }$ for the angles and less than $1 \textrm { m m }$ for the distances.

We fi nally mention the spherical excess which plays a role in spherical trigonometry. It is defi ned as the surplus over $1 8 0 ^ { \circ }$ of the angle sum of a spherical triangle. The excess is proportional to the area $F$ of the triangle:

$$
\varepsilon = \frac { F } { R ^ { 2 } } .
$$

For an equilateral triangle with $S = 5 0 ~ \mathrm { k m } _ { \it \ / }$ , the excess amounts to $5 . 4 8 ^ { \prime \prime }$

# 6.3.2 Reductions to the ellipsoid

In order to carry out a transfer of ellipsoidal coordinates on the ellipsoid, observed azimuths and distances have to be reduced to the ellipsoidal quantities $\alpha$ and $S ,$ which refer to the geodesic.

The reduction of the astronomic azimuth $A$ is composed of three parts. Laplace’s equation (6.58) takes the effect of the defl ection of the vertical into account. The corresponding reduction to the normal section reads

$$
\alpha - A = - \big ( \eta \tan \varphi + \big ( \xi \sin \alpha - \eta \cos \alpha \big ) \cot \zeta \big ) .
$$

The fi rst term in (6.68) is the azimuthal component of the defl ection of the vertical. It does not depend on the azimuth and corresponds to a twist in the observed directions; horizontal angles are not affected by this change of orientation. The second term can be viewed as an “error” in setting up the theodolite, by orientating it along the plumb line direction instead of the ellipsoidal normal. While the fi rst term reaches the order of magnitude of the vertical defl ections and more, a strong reduction takes place in the second term due to cot z. Hence, this direction-dependent term is of the order of a few $0 . 1 { ^ { \prime \prime } }$ in fl at areas only but may reach some arcsec in the mountains.

If the target point is not located on the ellipsoid but at a height $h _ { { } _ { 2 ^ { \prime } } }$ a further reduction has to be applied. Namely, the vertical plane formed by the ellipsoidal normal at $P _ { _ { 1 } }$ and the target point $P _ { _ { 2 ^ { \prime } } }$ in general, does not contain the ellipsoidal normal through $P _ { _ 2 }$ (Fig. 6.15). Therefore, the ensuing normal section does not pass through the footpoint $Q _ { { } _ { 2 ^ { \prime } } }$ but through

![](images/0d53322c6a09a4905322b254d1c6b4e260e96908c290764b7179aee55fae61a8.jpg)  
Fig. 6.15: Skew-normal reduction of the azimuth.

$Q _ { 2 } ^ { \prime } ,$ which requires a reduction by the angle ${ Q _ { 2 } ^ { \prime } } \ : P _ { 1 } { Q _ { 2 } }$ . This skew-normal reduction can be derived from the partial derivative $\partial A / \partial h _ { _ { 2 ^ { \prime } } }$ formed for the adjustment in the $\varphi , \lambda , h \mathrm { \ d { \cdot } }$ -system, cf. [6.2.1]; it reads

$$
\alpha _ { n } - \alpha _ { h _ { 2 } } = { \frac { e ^ { 2 } } { 2 b } } \cos ^ { 2 } \varphi \sin 2 \alpha h _ { 2 } ,
$$

where $e$ is the fi rst eccentricity and $b$ the semi-minor axis of the ellipsoid, cf. [4.1.1]. For $\varphi = 0 ^ { \circ }$ and $\alpha = 4 5 ^ { \circ } .$ , the reduction attains only $0 . 1 1 ^ { \prime \prime }$ at $h _ { _ 2 } = 1 0 0 0 \mathrm { m }$ .

Finally, the azimuth has to be reduced from the normal section to the geodesic:

$$
\alpha _ { g } - \alpha _ { n } = - \frac { e ^ { 2 } } { 1 2 a ^ { 2 } } \cos ^ { 2 } \varphi \sin 2 \alpha S ^ { 2 } .
$$

At $\varphi = 0 ^ { \circ }$ and $\alpha = 4 5$ , this reduction reaches only $0 . 0 2 8 ^ { \prime \prime }$ for $S = 1 0 0 ~ \mathrm { k m }$ .

The reduction of the chord distance $s$ to the ellipsoid is a purely geometric problem, as distances do not depend on the gravity fi eld (Höpcke, 1966). We assume that the effects of atmospheric refraction have been reduced beforehand, cf. [5.5.2]. From Fig. 6.16, we read

$$
\begin{array} { l } { { \displaystyle s ^ { 2 } = \left( R + h _ { \scriptscriptstyle 1 } \right) ^ { 2 } + \left( R + h _ { \scriptscriptstyle 2 } \right) ^ { 2 } - 2 \big ( R + h _ { \scriptscriptstyle 1 } \big ) \big ( R + h _ { \scriptscriptstyle 2 } \big ) \cos \psi , } } \\ { { \displaystyle s _ { \scriptscriptstyle 0 } = 2 R \sin \psi } , \quad { \displaystyle S = R \psi } , } \end{array}
$$

![](images/725307ccc80a7941160593b44c18a812d2b49f5ff49d736a93342db7ed36cd86.jpg)  
Fig. 6.16: Reduction of the spatial distance on the ellipsoid.

which gives closed formulas for the reduction to the normal section

$$
s _ { \mathrm { 0 } } = \sqrt { \frac { s ^ { 2 } - \left( h _ { \mathrm { 2 } } - h _ { \mathrm { 1 } } \right) ^ { 2 } } { \left( 1 \mathrm { ~ } + h _ { \mathrm { 1 } } / R \right) \left( 1 \mathrm { ~ } + h _ { \mathrm { 2 } } / R \right) } } , \quad S = 2 R \mathrm { a r c s i n } \frac { s _ { \mathrm { 0 } } } { 2 R ^ { \prime } }
$$

where $R$ is taken from Euler’s formula (4.18). After series expansion, the different contributions to the reduction become apparent:

$$
S - s = - \frac { h _ { 1 } + h _ { 2 } } { 2 R } s - \frac { \left( h _ { 2 } - h _ { 1 } \right) ^ { 2 } } { 2 s } + \frac { s _ { 0 } ^ { 3 } } { 2 4 R ^ { 2 } } .
$$

The fi rst term in (6.71b) corresponds to a reduction from the mean height to the ellipsoid. It reaches the meter-order of magnitude in the mountains at distances of several $\mathrm { k m }$ . The second term takes the inclination of the distance into account. It generally remains below the meterorder of magnitude in the lowland but may attain large values in the high mountains. The magnitude of these reduction terms does not allow substitution of the ellipsoidal heights by orthometric or normal heights, otherwise relative errors of $1 0 ^ { - 5 }$ have to be expected. The last term in (6.71b) provides the transition from the ellipsoidal chord to the normal section and reaches the cm-order only at larger distances.

The reduction from the normal section to the geodesic is given by

$$
S _ { g } - S _ { n } = - \frac { e ^ { 4 } } { 3 6 0 a ^ { 4 } } \cos ^ { 4 } \varphi \sin ^ { 2 } 2 \alpha S ^ { 5 } .
$$

The magnitude reaches the meter-order only at distances of several $1 0 0 0 ~ \mathrm { k m }$ and can be neglected in classical network computations.

# 6.3.3 Computations on the ellipsoid

As already mentioned, the relevance of ellipsoidal calculations has decreased, since the results of three-dimensional positioning in Cartesian coordinates can easily be transformed into ellipsoidal coordinates, see (4.28). Azimuths and distances derived from Cartesian coordinates, see (6.39), can be reduced to the ellipsoid according to [6.3.2]. Nevertheless, computations on the ellipsoid are still of signifi cance in navigation, and they have been the basis for the calculation of classical horizontal control networks, which are still in use today.

The geodetic datum of the classical two-dimensional geodetic systems has been established by the defl ection of the vertical and the geoid height at a fundamental point and the parameters of the reference ellipsoid, cf. [6.2.2]. Equation (6.57) then allows the transformation of observed astronomical latitude and longitude into the corresponding ellipsoidal quantities, and (6.46) provides the height relation between the geoid or quasigeoid and the ellipsoid. Having reduced the observed horizontal directions and the distances onto the ellipsoid, only one rotation about the ellipsoidal normal in the fundamental point is possible. This rotation is fi xed by applying the Laplace equation on the astronomic azimuth observed at the fundamental point. Equations (6.57) and (6.58) thus provide the parallelism of the axes of the ellipsoidal system with respect to the global geocentric system.

The accuracy of the parallelism of axes depends on the accuracy of the (nineteenth or early twentieth century) astronomical observations which entered into (6.57) and (6.58), and hence it is about 1 to 2 arcsec or even better. The origin of the classical systems, on the other hand, is far from being geocentric and may deviate by some $1 0 0 ~ \mathrm { { m } }$ and more from the geocenter. This results partly from the fact that 1 arcsec in astronomical positioning already corresponds to $3 0 ~ \mathsf { m }$ in horizontal position, but mainly from totally neglecting or only relative use of vertical defl ections and geoid heights, cf. [7.1].

Having fi xed the ellipsoidal coordinates and one geodetic azimuth at the fundamental point, ellipsoidal coordinate transfer can be carried out with the ellipsoidal “observations” referring to the geodesic. Here, it is assumed that the ellipsoidal network is error free; adjustment strategies are discussed in [7.1].

We distinguish between

• The direct problem, i.e., to compute the ellipsoidal coordinates $\varphi _ { { _ 2 ^ { \prime } } } \lambda _ { _ 2 }$ of the point $P _ { _ { 2 ^ { \prime } } }$ as well as the azimuth $\alpha _ { _ 2 ^ { \prime } }$ given the coordinates $\varphi _ { 1 } , \lambda _ { \mathfrak { r } }$ of point $P _ { \mathrm { { \uparrow } ^ { \prime } } }$ the azimuth $\alpha _ { _ { 1 ^ { \prime } } }$ and the distance $S _ { \cdot }$ . The inverse problem, i.e., to compute the azimuths $\alpha _ { _ 1 } , \alpha _ { _ 2 }$ and the distance $S ,$ given the coordinates $\varphi _ { 1 } , \lambda _ { \mathfrak { r } }$ and $\varphi _ { { _ 2 ^ { \prime } } } \lambda _ { _ 2 }$ of $P _ { \mathrm { \uparrow } }$ and $P _ { _ 2 }$ .

The direct and the inverse problem correspond to the solution of the ellipsoidal polar triangle $P _ { _ 1 } N P _ { _ 2 }$ (Fig. 6.17), Ehlert (1993). With the geodesic introduced as a surface curve connecting $P _ { _ { 1 } }$ and $P _ { _ { 2 ^ { \prime } } }$ elliptic integrals appear in the solutions, cf. [6.3.1]. Hence no closed solutions are available (Rösch and Kern, 2000). Dependent on the computing technique available, numerous solutions of the direct and the inverse problem have been developed over the past 200 years. They are based either on series expansions or on numerical integration, some examples follow.

A Taylor series expansion of latitude, longitude, and azimuth as a function of the arc length was given by Legendre already in 1806:

$$
\begin{array} { l } { { \displaystyle \varphi _ { _ 2 } - \varphi _ { _ 1 } = \left( \frac { d \varphi } { d S } \right) _ { 1 } S + \frac { 1 } { 2 } \left( \frac { d ^ { 2 } \varphi } { d S ^ { 2 } } \right) _ { 1 } S ^ { 2 } + . . . } } \\ { { \displaystyle \lambda _ { 2 } - \lambda _ { 1 } = \left( \frac { d \lambda } { d S } \right) _ { 1 } S + \frac { 1 } { 2 } \left( \frac { d ^ { 2 } \lambda } { d S ^ { 2 } } \right) _ { 1 } S ^ { 2 } + . . . } } \\ { { \displaystyle \alpha _ { _ 2 } - \alpha _ { _ 1 } = \left( \frac { d \alpha } { d S } \right) _ { 1 } S + \frac { 1 } { 2 } \left( \frac { d ^ { 2 } \alpha } { d S ^ { 2 } } \right) _ { 1 } S ^ { 2 } + . . . } } \end{array} ,
$$

![](images/a29e5ef6fc84547bddc6d2721c8775de9af8218de8b0d138eae39aaacb36f915.jpg)  
Fig. 6.17: Ellipsoidal polar triangle.

where the fi rst-order derivatives are provided by (6.63) and (6.65), and the equation of the geodesic enters through da /dS. The higher-order derivatives are calculated according to

$$
\frac { d ^ { 2 } \varphi } { d S ^ { 2 } } = \frac { \partial } { \partial \varphi } \left( \frac { d \varphi } { d S } \right) \frac { d \varphi } { d S } + \frac { \partial } { \partial \alpha } \left( \frac { d \varphi } { d S } \right) \frac { d \alpha } { d S } ,
$$

and so forth, with variable latitude and azimuth.

Since the Legendre series are expanded with respect to $S ,$ they converge slowly. An expansion to the fi fth order (for $\varphi , \lambda )$ and the fourth-order (fora ) is necessary at mid-latitudes in order to provide an accuracy of $0 . 0 0 0 1 ^ { \prime \prime }$ and $0 . 0 0 1 ^ { \prime \prime } ,$ respectively, at distances of $1 0 0 ~ \mathrm { k m }$ . Developments up to the tenth order are available (Krack, 1982), and modifi cations of (6.73) improve the convergence and allow an effi cient solution for lengths of several $1 0 0 ~ \mathrm { k m }$ and more.

Series expansions suitable for very long geodesics have been developed by Bessel (1826) and improved by Helmert (1880). For this method, the ellipsoidal polar triangle is projected onto a concentric sphere with radius a (Fig. 6.18). The latitude $\varphi$ is transformed to the reduced latitude $\beta ( 4 . 1 0 )$ .

Due to Clairaut’s equation (6.64), which now reads.

$$
\cos { \beta } \sin { \alpha } = \mathrm { c o n s t . } ,
$$

the ellipsoidal azimuths are preserved, if the azimuth $\alpha _ { _ 1 }$ is transferred to the sphere. The relation between the ellipsoidal distance $S$ and the spherical distance $\sigma ,$ as well as those between the ellipsoidal and the spherical longitude differences $\Delta \lambda$ and $\Delta \lambda ^ { \prime }$ , are given by differential formulas which correspond to (6.63):

$$
\frac { d \beta } { d \sigma } = \cos \alpha , ~ \frac { d \lambda ^ { \prime } } { d \sigma } = \frac { \sin \alpha } { \cos \beta } .
$$

By combination with (6.63), the following relations are obtained:

$$
d S = a \sqrt { 1 - e ^ { 2 } \mathrm { c o s } ^ { 2 } \beta } d \sigma , d \lambda = \sqrt { 1 - e ^ { 2 } \mathrm { c o s } ^ { 2 } \beta } d \lambda ^ { \prime } .
$$

The elliptic integrals resulting from (6.76) are solved either by expanding the square roots in series and subsequent integration term by term or by numerical methods. As the series expansions are controlled by the (small) numerical eccentricity, they converge rapidly. After projection onto the sphere, the coordinate transfer is carried out by strict formulas of spherical trigonometry, and the results are then transformed back to the ellipsoid by inverse relations. Computations around the globe are possible with mm accuracy (Klotz, 1993; Sjöberg, 2006).

![](images/dc0fe24d32cf8cde81a8bd67be4c7ddf97794d96630329ae5e146ae90ce3cdab.jpg)  
Fig. 6.18: Transfer of ellipsoidal coordinates: Bessel-Helmert solution.

![](images/b685cd80d39e2d501c28494a7a50ad50ce3d8cb58aec45a1d114dee4f515452b.jpg)  
Fig. 6.19: Transfer of ellipsoidal coordinates: numerical solution.

Numerical methods are based either on a polynomial approximation of the integrals and subsequent integration (methods of Newton, Gauss, Simpson and others) or on numerical integration (Schmidt, 1999). In the latter case, the length of the geodesic is subdivided into small increments (number $n$ ), which are calculated using the differential formulas (6.63) and (6.64), Fig. 6.19. Clairaut’s equation serves for keeping the increments on the direction of the geodesic. Summing the line elements provides a fi rst approximation. By iteration with smaller increments and comparison of the results, a given error limit can be obtained. With increments of $1 0 0 ~ \mathrm { { m } }$ length, sub-cm accuracy can be achieved with geodesics of $1 0 \ 0 0 0 \ \mathrm { k m }$ length.

By inversion, solutions of the inverse problem are available for all kind of methods. The adjustment of ellipsoidal networks would require differential relations da /dj, da /dl and dS/dj, dS/dl. These relations can be derived from the corresponding differentials of a three-dimensional model reduced to the ellipsoid or by differentiating the solutions of the inverse problem (Wolf, 1963b).

# 6.4 Height determination

Precise height determination is possible either with the relative methods of geometric leveling and trigonometric height transfer using zenith angles, or with GNSS (today still mainly GPS) heighting which may be applied in the absolute or in the relative mode. The results of these methods refer to the geoid (quasigeoid) or the ellipsoid, which requires corresponding reductions. Geometric leveling after applying small reductions provides height differences defi ned in the gravity fi eld [6.4.1]. Zenith angles also refer to the gravity fi eld. Trigonometric heighting thus delivers corresponding height differences, which may be transformed into ellipsoidal ones by taking the effect of the gravity fi eld (defl ections of the vertical) into account [6.4.2]. GPS heighting, on the other hand, immediately results in geometrically defi ned ellipsoidal heights or height differences, which for practical use generally have to be reduced to heights above the geoid (quasigeoid) [6.4.3].

As precise heighting is based on observed height differences, the defi nition and realization of a vertical reference surface (geoid) is of fundamental importance. This vertical datum problem is extensively discussed in [3.4.3], for practical realization see also [7.2].

# 6.4.1 Heights from geometric leveling

The raw results of geometric leveling $\delta n \approx d n$ are transformed into potential differences by taking surface gravity $g$ along the leveling line into account (5.116). If connected to the zero height surface (geoid or quasigeoid) geopotential numbers (3.104) are obtained:

$$
C = W _ { \scriptscriptstyle 0 } - W _ { \scriptscriptstyle P } = \intop _ { 0 } ^ { P } g d n .
$$

In principle, the evaluation of (6.77) requires a gravity value at each leveling point, i.e., at distances of $1 0 0 \mathrm { ~ m ~ }$ or less for precise leveling. This requirement can be diminished if we postulate the same relative accuracy for the effect of leveling and gravity on the geopotential differences:

$$
\frac { d g } { g } = \frac { d ( \Delta n ) } { \Delta n } .
$$

Assuming a leveling accuracy of $0 . 1 \mathrm { \ m m }$ , gravity would only be needed with an accuracy of $1 0 0 ~ { \mu \mathrm { m } } { \zeta } ^ { - 2 }$ for $\Delta n = 1 0 ~ \mathrm { m } ,$ , and $1 0 ~ { \mu \mathrm { m s } } ^ { - 2 }$ for $\Delta n = 1 0 0 \mathrm { ~ m ~ }$ . Consequently, gravity values required in (6.77) can be interpolated from gravity measurements carried out at station distances of 5 to $2 0 ~ \mathrm { k m }$ in fl at areas, and at 1 to $2 ~ \mathrm { k m }$ in the mountains. Preferably, gravity stations should be established at sites where the gravity changes depart from linearity (variations in slope or direction of the leveling line, gravity anomalies).

Precise leveling in fundamental networks is carried out in closed loops, cf. [7.2]. The calculation of heights is performed by adjusting potential differences, with the condition, cf. [3.2.3]:

$$
\oint d W = 0 .
$$

Subsequent transformation yields metric heights, cf. [3.4.3].

An alternative approach, used classically, is to fi rst convert the raw leveling results (with $\oint d n \neq 0 )$ ) into differences of the respective height system and then adjust height differences, where we distinguish again between dynamic, orthometric and normal heights.

Dynamic height differences are obtained by differencing (3.105):

$$
\Delta H _ { 1 , 2 } ^ { \mathrm { d y n } } = H _ { 2 } ^ { \mathrm { d y n } } - H _ { 1 } ^ { \mathrm { d y n } } = \Delta n _ { 1 , 2 } + E _ { 1 , 2 } ^ { \mathrm { d y n } } ,
$$

with the dynamic height reduction

$$
E _ { \ : 1 , 2 } ^ { \mathrm { d y n } } = \int _ { 1 } ^ { 2 } \frac { g - \gamma _ { \scriptscriptstyle 0 } ^ { 4 5 } } { \gamma _ { \scriptscriptstyle 0 } ^ { 4 5 } } d n .
$$

For orthometric heights, we expand (3.106) by dynamic heights:

$$
\Delta { H } _ { 1 , 2 } = H _ { 2 } - H _ { 1 } = \Delta H _ { 1 , 2 } ^ { \mathrm { d y n } } + \left( H _ { 2 } - H _ { 2 } ^ { \mathrm { d y n } } \right) - \bigl ( H _ { 1 } - H _ { 1 } ^ { \mathrm { d y n } } \bigr ) .
$$

This leads to

$$
\Delta H _ { _ { 1 , 2 } } = \Delta n _ { _ { 1 , 2 } } + E _ { _ { 1 , 2 ^ { \prime } } }
$$

with the orthometric height reduction

$$
E _ { _ { 1 , 2 } } ^ { { ^ 2 } } = \displaystyle \int _ { 1 } ^ { 2 } \frac { g - \gamma _ { _ 0 } ^ { 4 5 } } { \gamma _ { _ 0 } ^ { 4 5 } } d n + \frac { \overline { { g } } _ { 1 } - \gamma _ { _ 0 } ^ { 4 5 } } { \gamma _ { _ 0 } ^ { 4 5 } } H _ { _ 1 } - \frac { \overline { { g } } _ { 2 } - \gamma _ { _ 0 } ^ { 4 5 } } { \gamma _ { _ 0 } ^ { 4 5 } } H _ { _ 2 } .
$$

An analog equation is valid for the transformation of leveled height differences into normal height differences, where mean gravity along the plumb line $\overline { { g } }$ is replaced by mean normal gravity $\bar { \gamma } ,$ and orthometric height $H$ by normal height $\bar { H } ^ { N } ( 3 . 1 0 7 )$ . The normal height reduction then reads:

$$
E _ { 1 , 2 } ^ { \scriptscriptstyle N } = \int _ { 1 } ^ { 2 } \overline { { { g } } } ^ { \mathrm { ~ - ~ } } \gamma _ { 0 } ^ { 4 5 } d n + \frac { \overline { { { \gamma } } } _ { \scriptscriptstyle 1 } - \gamma _ { 0 } ^ { 4 5 } } { \gamma _ { 0 } ^ { 4 5 } } H _ { 1 } ^ { \scriptscriptstyle N } - \frac { \overline { { { \gamma } } } _ { \scriptscriptstyle 2 } - \gamma _ { 0 } ^ { 4 5 } } { \gamma _ { 0 } ^ { 4 5 } } H _ { 2 } ^ { \scriptscriptstyle N } .
$$

The dynamic height reduction only depends on gravity and height differences along the path. It attains values between a few $\mathsf { m m }$ (fl at terrain) and some cm to dm (mountains). Hence, it has to be taken into account even in local surveys if the vertical reference system is based on dynamic heights. The orthometric and the normal height reduction include the dynamic reduction, but, in addition, contain two terms with the mean gravity along the actual resp. normal plumb line at the end points of the leveling line. The different reduction terms substantially cancel each other, with the consequence that these reductions are below one mm in fl at areas and only reach a few cm in the mountains.

Mean normal gravity $\bar { \gamma }$ can be calculated by (4.67) with the spherical approximation

$$
\overline { { \gamma } } = \gamma _ { \scriptscriptstyle 0 } \bigg ( 1 - \frac { H ^ { N } } { R } \bigg ) .
$$

Mean actual gravity ${ \bar { g } } ,$ on the other hand, requires the knowledge of $g$ along the plumb line between the geoid and the Earth’s surface. At any point $P ^ { \prime }$ with height $H ^ { \prime }$ , we have

$$
g ^ { \prime } = g - \int _ { H ^ { \prime } } ^ { H } \frac { \partial g } { \partial H } d H ,
$$

where $g$ is the surface gravity at $P .$ The actual vertical gravity gradient is given by (3.71), where we may introduce (4.60) for the free-air part and $2 6 7 0 ~ \mathrm { k g / m ^ { 3 } }$ as a mean crustal density; this yields the approximation

$$
g ^ { \prime } = g + 0 . 8 4 8 \times 1 0 ^ { - 6 } ( H - H ^ { \prime } ) \mathrm { m } s ^ { - 2 } ,
$$

also called Poincaré-Prey reduction (Hofmann-Wellenhof and Moritz, 2005, p. 138 ff.). After inserting into (3.106) and integration between $H ^ { \prime } = 0$ and $H ^ { \prime } = H / 2$ , we obtain the frequently used formula

$$
\overline { { g } } = g + 0 . 4 2 4 \times 1 0 ^ { - 6 } H \mathrm { m } \mathrm { s } ^ { - 2 }
$$

for the mean actual gravity between the Earth’s surface and the geoid. Orthometric heights based on this estimate are called Helmert heights.

As shown in [6.5.3], the second term on the right side of (6.84) can be interpreted as a reduction of the surface gravity to actual gravity at $H / 2$ , with the Bouguer plate as a model of the topography. The effect of model errors remains small in fl at terrain, but improved

models that take topography and density into account are needed in the mountains (Tenzer et al., 2005).

# 6.4.2 Trigonometrical heights

Zenith angles can be used for a trigonometrical height transfer if refraction effects have been reduced suffi ciently, cf. [5.5.1], Fig. 6.20. The ellipsoidal zenith angle $\zeta$ is obtained from the observed quantity $Z ^ { \prime }$ by

$$
\zeta = z ^ { \prime } + \delta + \varepsilon = z + \varepsilon ,
$$

where $\delta$ is the angle of refraction (5.11) and $\varepsilon$ the vertical defl ection component in the azimuth of the line of sight (6.18). Using spherical trigonometry, the ellipsoidal height difference is given by (Kneissl, 1956, p. 358):

$$
\Delta h _ { _ { 1 , 2 } } = h _ { _ { 2 } } - h _ { _ { 1 } } = S \left( 1 + \frac { h _ { _ { m } } } { R } \right) \mathrm { c o t } \zeta _ { _ { 1 } } + \frac { S ^ { ^ { 2 } } } { 2 R \mathrm { s i n } ^ { 2 } \zeta _ { 1 } } .
$$

$S$ is the length of the ellipsoidal normal section, $R$ the radius of curvature (4.18), and $h _ { _ m } = \big ( h _ { _ 1 } + h _ { _ 2 } \big ) / 2$ represents a mean height.

m 1 2 The use of reciprocal zenith angles offers signifi cant advantages. With the central angle $\psi$

$$
\psi = \frac { S } { R } = \zeta _ { 1 } + \zeta _ { 2 } - \pi
$$

taken from Fig. 6.20, we apply the law of tangents on the triangle $P _ { \mathrm { 1 } } O P _ { \mathrm { 2 } }$ . In connection with (6.85), the height difference is obtained:

$$
\Delta h _ { _ { 1 , 2 } } = S \bigg ( 1 + \frac { h _ { _ { m } } } { R } + \frac { S ^ { 2 } } { 1 2 R ^ { 2 } } \bigg ) \tan \frac { 1 } { 2 } \big ( \big ( Z _ { _ { 2 } } ^ { \prime } + \delta _ { _ { 2 } } + \varepsilon _ { _ { 2 } } \big ) - \big ( Z _ { _ { 1 } } ^ { \prime } + \delta _ { _ { 1 } } + \varepsilon _ { _ { 1 } } \big ) \big ) .
$$

Here, only differences in $\delta$ and $\varepsilon$ appear. Symmetric refraction conditions may be expected with simultaneous observations, cf. [5.5.1], thus refraction effects will mostly cancel with the use of simultaneous reciprocal-zenith-angle measurements (Kuntz and Schmitt, 1995). They also offer a possibility to determine the coeffi cient of refraction. Combining (5.11), (6.85), and (6.87), and neglecting the defl ections of the vertical, yields

![](images/e2f65be48954f2db9602129426b37ebd7dbc8c7dd4fa2065d544db16920fc47e.jpg)  
Fig. 6.20: Trigonometrical height transfer.

$$
k = 1 - \frac { R } { S } \big ( Z _ { \uparrow } ^ { \prime } + Z _ { \uparrow } ^ { \prime } - \pi \big ) .
$$

From (6.89), an average value of $k = 0 . 1 3 \pm 0 . 0 4$ was obtained by Gauss at his arc measurement in the kingdom of Hannover. This value was confi rmed by other surveys for lines of sight with a large ground clearance, but close to the ground the coeffi cient of refraction may vary between $^ { - 1 }$ and $+ 1$ . Network adjustment models may be extended by introducing individual refraction coeffi cients for each station or for each line (Hradilek, 1984), and observed meteorological parameters may also contribute to the determination of more realistic values for $k ,$ cf. [5.1.2], [5.5.1]. In spite of these refi nements, refraction irregularities strongly limit the application of trigonometrical heighting. A cm-order of accuracy may be obtained over distances of a few km, but errors of the dm-order of magnitude and more have to be expected with larger distances.

Trigonometric leveling signifi cantly diminishes the errors of a trigonometrical height transfer, by reducing the lines of sight to 100 to $3 0 0 ~ \mathrm { { m } }$ (Rüeger and Brunner, 1982). At this method, height differences are determined by measuring zenith angles and slope distances with a total station, cf. [5.5.2]. Either simultaneous-reciprocal observations are carried out using two refl ector-equipped total stations or the method of leveling “from the middle” is applied, in analogy to geometric leveling, cf. [5.5.3]. Due to the short lines of sight running approximately parallel to the Earth’s surface, refraction errors remain small and obey a favorable error propagation even over larger distances; accuracies of 1 to $2 \textrm { m m }$ per km can be achieved. The effi ciency of the method can be increased by motorized procedures (Becker, 2002). Trigonometric leveling may be regarded as a special version of geometric leveling using inclined lines of sight. Hence, the results represent a good approximation to leveled height differences.

Trigonometric height determination with long lines played an important role in the establishment of classical horizontal networks by triangulation, as it simultaneously provided heights for reduction onto the ellipsoid and for the later construction of topographical maps. Today, it is restricted to special applications, e.g., to the height determination of inaccessible sites. Trigonometric leveling, on the other hand, has been employed successfully for surveying vertical control networks of large extension (Whalen, 1985).

# 6.4.3 Heights from GNSS (GPS)

GNSS and especially the Global Positioning System (GPS) provide global Cartesian coordinates with high accuracy, cf. [5.2.5], which can easily be transformed to ellipsoidal coordinates including the ellipsoidal height, see (4.28). While absolute heights above the reference ellipsoid can be derived with sub-cm accuracy only from global network observations, differential methods provide this accuracy already at observation times of a few hours or less, for distances of $1 0 0 ~ \mathrm { k m }$ and more. Main error sources stem from the geometry of the satellites’ constellation and the atmospheric refraction, cf. [5.2.5]. For distances of a few $1 0 ~ \mathrm { k m }$ , even sub-cm accuracy can be obtained. Consequently,

GPS heighting may support or substitute time-consuming geometric leveling, at least for distances larger than about $1 0 ~ \mathrm { k m }$ . This has led to the strategy of GPS leveling which requires that the reduction of ellipsoidal height differences to normal or orthometric height differences can be performed with corresponding accuracy (Dodson, 1995; Featherstone et al., 1998). According to (6.46), quasigeoid or geoid differences then provide the necessary reductions:

$$
\Delta H ^ { N } = \Delta h - \Delta \zeta , \quad \Delta H = \Delta h - \Delta N .
$$

We remark, that (6.90) may be evaluated for the determination of normal or orthometric height differences (“GPS leveling”), but also for deriving the quasigeoid or geoid, respectively. The latter problem presupposes the existence of a precise leveling network, well connected to the GPS derived heights, cf. [6.7]. Repeated GPS height determinations, on the other hand, may be directly evaluated with respect to temporal height changes, as correlated geoid variations only happen at large-scale mass shifts, and remain about one order of magnitude smaller. This fact can be exploited at the investigation of vertical crustal movements as well as for the detection of subsidence at tide gauges or at engineering projects, cf. [8.3.3], [8.3.4].

Today, global quasigeoid or geoid models have an accuracy of about $0 . 1 \textrm { m }$ , and regional models reach the cm accuracy, cf. [6.6], [6.7]. The use of these models for the reduction of GPS heights presupposes that the model contains the same reference surface as used as zero height surface for the height system, cf. [3.4.3]. This demand can be fulfi lled by fi tting the model to quasigeoid or geoid heights at control points where GPS and leveled heights are available. The fi tting also reduces long- and medium-wave model errors. Following the method of least-squares collocation, cf. [6.8.2], the discrepancies found at the control points can be modeled (for normal heights) as follows (Denker et al., 2000):

$$
h _ { g p s } - H ^ { N } - \zeta _ { \mathrm { m o d } } = t + s + n ,
$$

where $t$ describes a trend component, $s$ is a stochastic signal part, and $n$ represents the random noise of all types of observations involved (GPS, leveling, geopotential model). A simple trend function may consist of a three-parameter datum shift according to (6.41):

$$
t = \cos \varphi \cos \lambda \Delta X + \cos \varphi \sin \lambda \Delta Y + \sin \varphi \Delta Z .
$$

Equivalently, the trend function may consist of a change in the ellipsoidal coordinates of some initial point, which corresponds to a vertical shift and tilts in the NS- and the EW-direction. Presupposing a suffi cient number of control points, the signal part can be derived from an empirical covariance function of the de-trended residuals and modeled, e.g., by an exponential function, cf. [6.1.3].

Using trend reduction only, the r.m.s. discrepancies between local geoid/quasigeoid models and GPS/leveling control points have been reduced to the dm-order of magnitude over a few $1 0 0 0 ~ \mathrm { k m }$ and to a few centimetre over several $1 0 0 ~ \mathrm { k m }$ . By also including a signal part, cm-accuracy may be obtained over distances up to $1 0 0 0 ~ \mathrm { k m } ,$ , which corresponds to the accuracy of classical leveling networks (Denker, 1998). Large-scale GPS leveling is now an effi cient tool for improving or completely renewing national and continental height systems, cf. [7.2]. Local applications include, among others, the height transfer to islands (e.g., Seeber and Torge, 1997) or to high mountains such as Mount Everest (Chen et al., 2010). For local (several $1 0 ~ \mathrm { k m } )$ applications, gravity fi eld related heights may also be estimated by purely mathematical interpolation between GPS/leveling control points, employing, e.g., low-order surface polynomials or splines. If a dense net of control points is available, and if the gravity fi eld is suffi ciently smooth, cm-accuracy can be achieved (Collier and Croft, 1997). The interpolation accuracy rapidly decreases at rough topography, and a topographic reduction will be necessary then, cf. [6.5.3].

With the further improvement of global and regional quasigeoid/geoid models, GPS leveling will become even more important.

# 6.5 Fundamentals of gravity fi eld modeling

Gravity fi eld modeling is part of the geodetic boundary-value problem [6.5.1]. Topography plays an important role in the solution of this problem [6.5.2]. Gravity reductions serve for reducing observed gravity fi eld data onto the geoid and subsequent geoid computation, and also provide different kinds of gravity anomalies for fi eld interpolation and geophysical interpretation [6.5.3]. While the orientation of the gravimetrically derived geoid is uniquely defi ned, the scale remains unknown and has to be determined by distance measurements [6.5.4].

# 6.5.1 The geodetic boundary-value problem

The geodetic boundary-value problem comprises the determination of the surface of the Earth and of its external gravity fi eld from observations on or close to the Earth’s surface (Sansò and Rummel, 1997). The surface to be determined is either the geoid (Stokes problem) or the physical surface of the Earth and the quasigeoid (Molodensky problem), Sansò (1995).

We start from Green’s third identity (e.g., Jekeli, 2009, p. 19), applied here for a function $V ,$ being continuous and fi nite outside and on the surface $S ,$ with continuous and fi nite partial derivatives of the fi rst and second order there, and vanishing in infi nity (Heiskanen and Moritz, 1967, p. 11ff.). With $n$ being defi ned as the outer surface normal and $I$ the distance between the point of evaluation and the source point, cf. [3.1.1], we have

$$
\iiiint _ { V } { \frac { 1 } { I } } \Delta V d v = - p V - \int \int _ { S } \left( { \frac { 1 } { I } } { \frac { \partial V } { \partial n } } - V { \frac { \partial } { \partial n } } \left( { \frac { 1 } { I } } \right) \right) d S ,
$$

with $p = 4 \pi$ if $P$ is outside $S ,$ and $p = 2 \pi$ if $P$ is on $S .$ If we apply (6.92a) on the gravity potential $W \left( 3 . 4 2 \right)$ and take the generalized Laplace equation (3.49) into account, the fundamental boundary problem of physical geodesy may be formulated by a non-linear integral equation of the second kind in the gravity potential (Molodenski et al., 1962). The above substitutions fi nally lead to (Heiskanen and Moritz, 1968, p. 15):

$$
- 2 \pi W + \int \int _ { s } \left( W \frac { \partial } { \partial n _ { s } } \left( \frac { 1 } { I } \right) - \frac { 1 } { I } \frac { \partial W } { \partial n _ { s } } \right) d S + 2 \pi \omega ^ { 2 } \left( X ^ { 2 } + Y ^ { 2 } \right) + 2 \omega ^ { 2 } \left[ \int _ { \nu } \left[ \frac { d V } { I } = 0 . \right. \right.
$$

Now $n _ { s }$ S   is the outer surface normal to the Earth’s surface $S , \nu$ is the volume of the Earth and $\omega$ its rotational velocity, and $I$ denotes the distance between the source point (on the surface or the interior of the Earth) and the point of calculation. If $W$ and $\partial W / \partial n _ { s }$ (i.e., the gravity component normal to the surface) were known on $S ,$ then the geometry of the Earth’s surface would remain as the only unknown quantity. After the determination of $S ,$ an upward continuation of $W$ would deliver the external gravity fi eld .

This boundary-value problem can be linearized by approximating the Earth’s surface by the telluroid (with respect to the physical surface) or the ellipsoid (with respect to the geoid), and the actual gravity potential $W$ by the normal potential $U ,$ cf. [6.1.1]. As the centrifugal part is well known, (6.92b) then transforms into an integral equation for $T$

$$
- 2 \pi T + \int _ { \Sigma } \int \left( T \frac { \partial } { \partial n _ { _ \Sigma } } \left( \frac { 1 } { I } \right) - \frac { 1 } { I } \frac { \partial T } { \partial n _ { _ \Sigma } } \right) d \Sigma = 0 .
$$

For the physical surface, the integration is now performed over the known telluroid $\Sigma$ . As the surface normal $n _ { \scriptscriptstyle \Sigma }$ deviates from the direction of the plumb line, $\partial T / \partial n _ { _ { \Sigma } }$ not only depends on the gravity disturbance and gravity anomaly, respectively, but also on the defl ection of the vertical and the slope of the terrain, cf. [6.7.2]. If (6.93), on the other hand, is applied on the geoid as boundary surface, this dependence reduces to the gravity disturbance respectively gravity anomaly.

Instead of the integral equation (6.93), the geodetic boundary-value problem can also be formulated by Laplace‘s differential equation (6.2):

$$
\Delta T = 0 .
$$

The residual gravity fi eld parameters observed on the Earth’s surface, or reduced to the geoid, then enter into boundary conditions for the solution of (6.94). The primary “observables” are the height anomalies and the geoid heights, respectively, and the gravity disturbances or gravity anomalies. Defl ections of the vertical and gravity gradient components play a role only in local calculations.

A Taylor development of $U$ in the telluroid point $Q$ gives

$$
U _ { _ P } = U _ { _ Q } + \left( { \frac { \partial U } { \partial \overline { { { n } } } } } \right) _ { Q } \zeta _ { _ P } + . . . ,
$$

where $\overline { { n } }$ is the normal to $U = U _ { Q ^ { \prime } }$ and $\zeta _ { _ P }$ the height anomaly. Solving for $\zeta _ { _ P }$ and inserting into (6.1) yields

$$
\zeta _ { \ / P } = \frac { T _ { \ / P } - \left( W _ { \ / P } - U _ { \ / Q } \right) } { \gamma _ { \ / Q } } ,
$$

with the normal gravity

$$
\gamma _ { _ Q } = - \bigg ( \frac { \partial U } { \partial \bar { n } } \bigg ) _ { Q } .
$$

The condition $U _ { \boldsymbol { Q } } = W _ { p }$ (6.6) fi nally delivers

$$
\zeta _ { P } = \frac { T _ { _ P } } { \gamma _ { _ Q } } .
$$

If (6.96a) is applied to the geoid, we obtain the corresponding relation between the geoid height and the disturbing potential on the geoid:

$$
N = \frac { T - \left( W _ { \mathrm { 0 } } - U _ { \mathrm { 0 } } \right) } { \gamma _ { \mathrm { 0 } } } ,
$$

where $\gamma _ { \scriptscriptstyle 0 }$ is normal gravity on the ellipsoid (4.41). Under the condition $U _ { 0 } = W _ { 0 ^ { \prime } }$ (6.97a) reads

$$
N { = } \frac { T } { \gamma _ { \mathrm { 0 } } } .
$$

This simple relation between the geoid height (a geometric quantity) and the disturbing potential (a physical quantity) has been known as Bruns’ theorem. As demonstrated above, it is also valid at the Earth’s surface, and can be extended to the exterior space, cf. [6.7.3].

We now derive the relations between the disturbing potential and residual gravity (defl ection of the vertical, gravity disturbance/anomaly, cf. [6.1.2]). The defl ection of the vertical is the horizontal derivative of $\zeta$ resp. $N$ (Fig. 6.21). Taking (6.96) and (6.97) into account, the components in the direction of the meridian and the prime vertical are then given by

$$
\xi = - \frac { 1 } { \gamma ( M + h ) } \frac { \partial T } { \partial \varphi } , \quad \eta = - \frac { 1 } { \gamma ( N + h ) \cos \varphi } \frac { \partial T } { \partial \lambda } ,
$$

where the ellipsoidal arc elements are provided by (4.20). The negative sign follows from the sign conventions for the quasigeoid (geoid) and the vertical defl ection, see (6.40).

In spherical approximation we obtain

$$
\xi = - \frac { 1 } { \gamma r } \frac { \partial T } { \partial \varphi } , \quad \eta = - \frac { 1 } { \gamma r \cos \varphi } \frac { \partial T } { \partial \lambda } .
$$

The gravity disturbance (6.11) is related to $T$ by

$$
\delta g _ { \scriptscriptstyle P } = g _ { \scriptscriptstyle P } - \gamma _ { \scriptscriptstyle P } = - \bigg ( \frac { \partial W } { \partial n } \bigg ) _ { \scriptscriptstyle P } - \bigg ( - \frac { \partial U } { \partial \overline { { { n } } } } \bigg ) _ { \scriptscriptstyle P } = - \bigg ( \frac { \partial T } { \partial n } \bigg ) _ { \scriptscriptstyle P } ,
$$

where we have neglected the defl ection of the vertical. We now develop $\boldsymbol { \gamma } _ { \mathrm { { p } } }$ at the telluroid point $Q ,$ taking (6.96c) into account:

$$
\gamma _ { _ P } = \gamma _ { _ Q } + \ \left( { \frac { \partial \gamma } { \partial \overline { { { n } } } } } \right) _ { Q } \xi _ { _ P } + \ldots .
$$

Inserting into (6.99) and taking (6.96c) into account yields the gravity anomaly :

$$
\Delta g _ { P } = g _ { P } - \gamma _ { Q } = - \bigg ( \frac { \partial T } { \partial n } \bigg ) _ { P } + \frac { 1 } { \gamma _ { Q } } \bigg ( \frac { \partial \gamma } { \partial \bar { n } } \bigg ) _ { Q } T _ { P } .
$$

The important relation between gravity anomaly and gravity disturbance reads as

$$
\Delta g _ { \scriptscriptstyle P } = \delta g _ { \scriptscriptstyle P } + \frac { 1 } { \gamma _ { \scriptscriptstyle Q } } \left( \frac { \partial \gamma } { \partial \bar { n } } \right) _ { \scriptscriptstyle Q } T _ { \scriptscriptstyle P } .
$$

![](images/4edf3139cd306aaafca7172eb1cd7c6fd77ab94f446efb60cc2661f2f6d25393.jpg)  
Fig. 6.21: Defl ection of the vertical components and height anomaly.

With the spherical approximation cf. [4.2.2],

and (6.99a) to (6.101a) and (6.102) read as

$$
\begin{array} { l } { { \displaystyle \delta g _ { _ P } = - \frac { \partial T } { \partial r } } , } \\ { { \displaystyle \gamma _ { _ P } = \gamma _ { _ Q } - \frac { 2 } { r } T } , } \\ { { \displaystyle \Delta g = - \frac { \partial T } { \partial r } - \frac { 2 } { r } T = \delta g - \frac { 2 } { r } T } . } \end{array}
$$

Equations (6.99), (6.101) represent boundary conditions for the solution of the Laplace equation (6.94). Because of the importance of (6.101), this fi rst-order partial differential equation in $T$ is also known as the fundamental equation of physical geodesy.

High-resolution gravity-fi eld modeling (e.g., geoid determination with cm-accuracy) requires some refi nements in the formulation and solution of the geodetic boundaryvalue problem (Moritz, 1974; Heck, 1991). This includes the transition to an ellipsoidal approximation by developing the potential in ellipsoidal harmonics or by applying ellipsoidal corrections to the spherical approximation (Jekeli, 1988b; Wang, 1999). It should be remembered that the spherical approximation primarily stems from neglecting the ellipsoid’s fl attening, which is about $0 . 3 \%$ . This results in corresponding relative errors in the residual gravity fi eld quantities derived from the solution of the boundary value problem. As an example, with an r.m.s. geoid variation of about $3 0 ~ \mathrm { m } ,$ , a geoid calculation would thus be erroneous by $_ { 0 . 1 \mathrm { ~ m ~ } }$ . Furthermore, the mass of the atmosphere has to be taken into account by a corresponding reduction, cf. [4.3], and the topography has to be smoothed by a terrain correction, cf. [6.5.3].

The geodetic boundary-value problem resembles the third boundary-value problem of potential theory, namely to determine a harmonic function given a linear combination of the function and its normal derivative on a bounding surface. It differs from the classical problem, as the bounding surface is supposed to be unknown: free boundary-value problem. In addition, observed gravity data do not represent potential derivatives with respect to the physical surface of the Earth, but rather refer to the plumb line: free and oblique boundary-value problem (Grafarend and Niemeier, 1971). Finally, the horizontal components of the position vector cannot be determined with suffi cient accuracy from gravimetric data, cf. [6.2.1], consequently the geometric part of the problem is generally restricted to the determination of heights: scalar free gravimetric boundary-value problem (Heck, 1997).

With the rapid progress in satellite positioning and satellite altimetry, the geometry of the Earth’s surface now can be assumed to be known with still increasing accuracy; the only remaining unknown at the boundary value problem then is the external gravity potential. Hence, a fi xed boundary-value problem can be formulated according to (6.99) which employs gravity disturbances as boundary values (Koch and Pope, 1972; Bjerhammar and Svensson, 1983), cf. [6.7.1]. This corresponds to the second (Neumann) boundary-value problem of potential theory, which is to determine a harmonic function from its derivative given on the bounding surface. Finally, a mixed altimetric-gravimetric boundary-value problem may be set up, taking into account that – in addition to the harmonic coeffi cients derived from satellite orbit analysis or satellite gradiometry – altimetric geoid heights and gravity anomalies are the main data sets available on a global scale (Sansò and Rummel, 1997).

# 6.5.2 Gravitation of topography, digital elevation models

The short-wavelength part of the gravitational fi eld is dominated by the effect of the topographical masses. By removing this effect, the gravity fi eld is smoothed signifi - cantly, which simplifi es gravity fi eld interpolation and transformation procedures; a corresponding restoration of topography has to follow, cf. [6.7]. For the determination of the geoid, the topography has to be removed completely in order to establish this level surface as a boundary surface in the gravity fi eld (Forsberg and Tscherning, 1997). In addition, the knowledge of the topography is of relevance at forward gravity modeling, i.e., for the calculation of synthetic gravity models from the Earth masses. These statements are also valid for the Earth’s crust and upper mantle, where isostasy mainly governs the mass distribution and affects the gravity fi eld in the medium-wavelength part, cf. [8.2.2]. In the following, we concentrate on the calculation of the gravitation of topographic (and isostatic) mass distributions and the present state of knowledge of topography (height and density).

The effect of the topographic masses on gravity fi eld parameters is calculated by the law of gravitation. The evaluation of (3.10) and corresponding integrals for other parameters poses problems, as topography is rather irregular in geometry (heights) and, to a far lesser extent, also in density. Therefore, the topographic masses are subdivided into elementary bodies for which closed solutions of the mass integrals exist. Rectangular prisms of constant density are especially appropriate, as the heights of the topography nowadays are provided in gridded form by digital elevation models (see below), but spherical or ellipsoidal tesseroids and point masses may also be used (Heck and Seitz, 2007). Vertical cylindrical columns around the point of calculation, constructed from concentric circles and horizontal radii and with constant density and height, have been used extensively in the past, but require coordinate transformation.

Starting from a system of three-dimensional Cartesian coordinates, the gravitational potential of the topography is expressed by

$$
V _ { \mathrm { t o p } } = G \rho \Big \{ \int _ { \stackrel { V } { v } } \int \int \displaylimits _ { - } ^ { d v } = G \rho \int \displaylimits _ { \stackrel { X _ { 1 } } { X _ { 1 } } } ^ { \therefore \therefore y _ { 2 } } \int \displaylimits _ { \stackrel { V } { I } } ^ { 1 } d x d y d z ,
$$

with $I = \sqrt { x ^ { 2 } + y ^ { 2 } + z ^ { 2 } } .$ . The topographic effects on the defl ection of the vertical, the gravity disturbance, and the gravity anomaly follow from the relations (6.97), (6.98), (6.99), and (6.101). The integration over a rectangular prism (Fig. 6.22) with density $\rho$ delivers closed formulas for the potential and its derivatives (Nagy, 1966; Nagy et al., 2000, 2002; Denker, 2012, p. 57). As an example, for a point located at the origin of the local $x , \ y , z .$ -system, the potential is given by

$$
\begin{array} { l } { { \displaystyle V ^ { p r i s m } = G \rho \left\| \left| x \gamma \ln ( z + I ) + x z \ln ( y + I ) + y z \ln ( x + I ) - \frac { x ^ { 2 } } { 2 } \arctan \frac { y z } { x I } \right. \right. } } \\ { { \displaystyle \left. - \frac { y ^ { 2 } } { 2 } \arctan \frac { x z } { y I } - \frac { Z ^ { 2 } } { 2 } \arctan \frac { x y } { z I } \left| _ { x _ { 1 } } ^ { x _ { 2 } } \right| _ { y _ { 1 } } ^ { y _ { 2 } } \right. _ { z _ { 1 } } ^ { z _ { 2 } } } . }  \end{array}
$$

The vertical component of the gravitation reads as (Nagy, 1966)

$$
B _ { z } ^ { p r i s m } = G \rho \left. \left. \left. x \ln ( y + I ) + y \ln ( x + I ) - z \arctan \frac { x y } { Z I } \right. _ { x _ { 1 } } ^ { x _ { 2 } } \right. _ { y _ { 1 } } ^ { y _ { 2 } } \right. _ { z _ { 1 } } ^ { z _ { 2 } } .
$$

![](images/b8c9a05a8783ed2e326b5c5b72cc640a264d25bb1abbe67f259f01a4dc108e70.jpg)  
Fig. 6.22: Gravitation of topography: rectangular prism method.

The total effect of topography results from the sum over the gravitation of the individual elementary bodies:

$$
\delta g _ { \mathrm { t o p } } = \Sigma b _ { z } .
$$

For heights given in a regular grid (e.g., formed by ellipsoidal or plane coordinates). Fast Fourier Transform (FFT) techniques provide a powerful tool for the effi cient calculation of topographic effects (Schwarz et al., 1990).

Digital elevation models (DEM), also called digital terrain models, are nowadays available on a global and regional scale (Li et al., 2005). They provide gridded height values above the geoid, and depths below mean sea level (marine areas). The quality of a DEM depends on the sampling density and accuracy of the height measurement method, the grid resolution (ranging from about 1 arcsec to $5 ^ { \prime \prime }$ ) and the data interpolation method as well as on the roughness of the terrain. Until recently, DEMs have been derived from digitized topographic and bathymetric maps, generally containing height/depths information in the form of contour lines. The underlying measurement methods included all kind of ground-based surveying methods as well as airborne stereo-photogrammetry and LIDAR (LIght Detection And Ranging). Beginning in the 1980s, remote-sensing space techniques now dominate the development of DEMs. Among them is the space and airborne Interferometric Synthetic Aperture Radar (InSAR). This method uses a digital image correlation from two subsequent radar signals (intensity and phase) refl ected from one point on the surface of the Earth. The phase differences obtained by two separate antenna positions are used for topographic mapping, where either two antennas are installed on the same platform (single-pass mode) or one antenna is operated on exactly repeated tracks (repeat-pass mode). The images from the same scene but different antenna positions then allow to determine topography and surface deformations, cf. [8.3.4], Hanssen (2001). Satellite laser and radar altimetry serve for the height determination of the Greenland and Antarctica ice sheets, cf. [5.2.7]. Radar altimetry also provides bathymetric information, due to the high correlation (at wavelengths of a few 10 to a few $1 0 0 ~ \mathrm { k m } )$ ) between the ocean surface and the ocean bottom; ship depths soundings are effi ciently supported and densifi ed by this method (Sandwell and Smith, 2001).

With respect to the density of the topographic masses a special remark is necessary. In the uppermost layers of the Earth this quantity varies between 2000 and $3 0 0 0 \mathrm { k g / m ^ { 3 } }$ , a global model with high spatial resolution is not available, cf. [8.2.1]. Therefore, a mean density value of $2 6 7 0 ~ \mathrm { k g / m ^ { 3 } }$ (corresponding to the density of granite) generally is introduced in physical geodesy, for global and regional applications. More refi ned density models are used for local studies, where the density values are estimated from geological information, rock samples, and gravity profi les exploiting the densitydependent relation between gravity and height: Nettleton method (e.g., Torge, 1989).

Among the more recent global DEMs are the NOAA ETOPO5 $( 5 ^ { \prime } \times 5 ^ { \prime }$ gridded land and seafl oor elevations) and the GLOBE (GLObal land one-kilometer Base Elevation) model. GLOBE is given in a $3 0 ^ { \prime \prime } \times 3 0 ^ { \prime \prime }$ grid; the accuracy depends on the data quality and varies between $2 0 \textrm { m }$ and a few $1 0 0 ~ \mathrm { { m } }$ (Hastings et al., 2000), the U.S. Geological Survey model GTOPO30 has similar properties. The NASA/NIMA Shuttle Radar Topography Mission (SRTM, February 2000) collected a global (between $\pm 6 0 ^ { \circ }$ latitude) InSAR data set, with a resolution of 1 arcsec (for the area of the U.S.A.) and 3 arcsec, respectively, and an accuracy of 6 to $9 \mathsf { m }$ (Farr et al., 2007). The results have been used, in connection with ICESat laser altimetry and ocean bathymetry, for the $3 0 ^ { \prime \prime } \times 3 0 ^ { \prime \prime }$ DTM2006.0 (Digital Topographic Model) of the U.S. National Geospatial-Intelligence Agency (Becker et al., 2009). Fusing of SRTM data and satellite radar altimetry results (ERS, TOPEX, etc.) led to an improved global land digital elevation model (ACE2), Berry et al. (2010). Another high resolution $( 1 ^ { \prime \prime } / 0 . 3 ^ { \prime \prime } )$ and high accuracy $( 3 \mathrm { ~ m } / 1 0 \mathrm { ~ m } )$ ) Global Digital Elevation Model (GDEM) is available from the ASTER (Advanced Spaceborne Thermal Emission and Refl ection radiometer) instrument on-board the Terra satellite (1999, $i = 9 8 ^ { \circ } ,$ , $h \approx 6 7 0 ~ \mathrm { k m } )$ , within the frame of an $\cup . S . /$ Japan cooperation. The German (DLR) TanDEM-X mission (fully operational since 2010) employs two active radar satellites (TerraSAR-X) in nearly identical orbit confi guration (polar orbit, mutual distance of a few $1 0 0 \mathrm { ~ m ~ }$ , $h \approx 5 1 4 ~ \mathrm { k m } )$ . The absolute/relative accuracy of the resulting DEM amounts to $1 0 ~ \mathrm { m } / 2 ~ \mathrm { m }$ , and the (latitude dependent) resolution is between $1 2 ~ \mathsf { m }$ and $5 \textrm { m }$ (Zheng et al., 2010). Regional DEMs have been developed in many countries with resolutions down to 1 arcsec (Smith and Roman, 2000).

Global height information also has been used early for developing spherical harmonic models of the topography (and later also for isostasy). While Prey (1922) could only carry out a development to the $1 6 ^ { \mathrm { t h } }$ degree, more recent models benefi t from the rapid progress of DEMs. The degree of development orientates itself on the state of global gravity fi eld modeling, cf. [6.6], resulting in developments (heights and depths) until degree and order 360 (Pavlis and Rapp, 1990) and 2190 (Pavlis et al., 2008), cf. [6.6.3]. These topographic-isostatic models not only serve for reduction purposes, but may also be used for the prediction of gravity anomalies in unsurveyed areas, cf. [6.5.3].

# 6.5.3 Gravity reductions to the geoid

The determination of the geoid requires some special considerations. As the solution of this problem is based on the assumption that the geoid represents a boundary surface in the gravity fi eld, the topographic masses (masses above the geoid) have to be removed, and the observed gravity fi eld data (here we restrict ourselves to gravity values, for the reduction of defl ections of the vertical see [6.7.4]) have to be reduced to the geoid. This is done by gravity reductions, which provide gravity anomalies on the geoid.

Depending on how the topographic masses are displaced, different types of gravity anomalies are obtained. The topographic reduction is connected with a propagation of the topographic model errors (height and density errors) into the calculation of the geoid. This has to be taken into account, for example, in the calculation of orthometric heights (3.106), where the same topographic model has to be employed.

The displacement of the topographical masses changes the gravitational fi eld of the Earth, including the potential of the geoid: indirect effect of the gravity reductions. The level surface which possesses the geoid potential after the displacement is called the cogeoid.

The terminus “compensated geoid” was introduced by J. de Graaff-Hunter and G. Bomford in the 1930s, after removal of topography and isostatic compensation at geoid calculations for India. The more general expression cogeoid results from the discussions at the IAG General Assembly in Oslo 1948.

The following steps may be distinguished in the calculation of the geoid (Fig. 6.23):

Reduction of the direct effect of the topography on gravity and adding of the direct effect of the dislocated masses if necessary, both to be calculated by the law of gravitation, cf. [6.5.2],   
calculation of the primary indirect effect on the potential, caused by the removal of the topography and the dislocation of the topographic masses. The calculation is performed according to some rule of compensation:

$$
\delta V = { V } _ { _ { \mathrm { t o p } } } - { V } _ { C } ,
$$

with $V _ { \mathrm { t o p } }$ potential of the topography and $V _ { c }$ potential of the compensating masses,

• calculation of the vertical distance between the geoid and the cogeoid according to Bruns’ theorem (6.97b):

$$
\delta N = \frac { \delta V } { \gamma } ,
$$

• reduction of the gravity values from the geoid to the cogeoid: secondary indirect effect. Here, a free-air reduction (6.101) is suffi cient:

$$
\delta g _ { c } = 2 \frac { \gamma } { r } \delta N ,
$$

![](images/0aa74de154a3220d2539e7330bd532e847bd26be5e4676f74df6566b91c1370b.jpg)  
Fig. 6.23: Geoid and cogeoid.

• calculation of the heights $N _ { _ C }$ of the cogeoid above the ellipsoid, as the solution of a gravimetric boundary-value problem, cf. [6.6], [6.7],   
calculation of the geoid heights according to

$$
N = N _ { _ { C } } + \delta N .
$$

In principle, every kind of gravity reduction could serve for the calculation of the geoid according to this scheme. Naturally, the indirect effect should be small in order to avoid laborious and error susceptible computations. Other criteria for the selection of gravity reductions include the smoothness of the resulting gravity anomalies, which facilitates interpolation, and their geophysical signifi cance, which would allow a corresponding interpretation. Under these aspects, we may distinguish between the effects of a homogeneous topography, density anomalies within the topography and the Earth’s crust, and isostatic compensation masses (Martinec, 1998), cf. [8.2.2].

The free-air anomaly is generally used for the calculation of the geoid, with the assumption that no masses exist above the geoid. The free-air reduction

$$
\delta g _ { F } ^ { } = - \frac { \partial g } { \partial H } H ,
$$

with $H$ being the orthometric height, provides the reduction of the surface gravity to the geoid, and the simple free-air anomaly on the geoid is then given by

$$
\Delta g _ { \scriptscriptstyle F } = g + \delta g _ { \scriptscriptstyle F } - \gamma _ { \scriptscriptstyle 0 } ,
$$

where $\gamma _ { \scriptscriptstyle 0 }$ is normal gravity on the ellipsoid. The free-air anomaly on the geoid should be clearly distinguished from the free-air anomaly defi ned on the surface of the Earth (6.15) where the normal gravity gradient is used for reduction.

According to (6.110), the correct reduction to the geoid would require the knowledge of the real vertical gravity gradient. Splitting the gradient into a normal and an anomalous part gives

$$
\frac { \partial g } { \partial H } = \frac { \partial \gamma } { \partial H } + \frac { \partial ( \Delta g ) } { \partial H } .
$$

The real and the normal part may differ by $1 0 \%$ or more. The normal gravity gradient can be calculated by (4.61). The calculation of the anomalous part corresponds to the downward continuation of a harmonic function. It can be formulated by Poisson’s integral, which is a solution of the fi rst (Dirichlet) boundary-value problem of potential theory, and solved by an integration over the surface gravity anomalies, cf. [6.7.2]. If the gravity anomaly depends linearly on elevation, the anomalous gradient part of the free-air reduction corresponds to the terrain correction (Moritz, 1980, p. 421), see below. This is of importance at practical geoid calculations, cf. [6.7.1]. A discrete solution of this problem has been given by Bjerhammar (1985), which takes into account that gravity data are given only at discrete points. This solution satisfi es all given data and generates missing data, and it is harmonic down to an internal sphere, located close to the Earth’s surface (Bjerhammar sphere), cf. [3.3.2].

The terrain correction removes geometric irregularities of the topography. It creates a plate (spherical or planar) of constant thickness and (assumed to be) constant density by fi lling mass defi cits below $P$ and removing excess masses above the plate: Bouguer plate (Fig. 6.24). For planar approximation (Bouguer plate extending to infi nity), both measures increase gravity at $P ;$ the terrain correction then is always positive. It can be calculated from digital elevation models, cf. [6.5.2], and attains values of 1 to $1 0 \mu \mathrm { m } \mathsf { s } ^ { - 2 }$ in fl at areas, reaching several $1 0 0 ~ { \mu \mathrm { m s } } ^ { - 2 }$ in the mountains. From the evaluation of (6.103), we obtain for the terrain correction

![](images/8fa78e953847afbaf8672684af26f0078754d38ebeeb44aecc4e95f6b070a446.jpg)  
Fig. 6.24: Bouguer plate and terrain correction.

$$
\delta g _ { _ T } = G \rho \int \displaylimits _ { - \infty } ^ { + \infty } \int \displaylimits _ { - \infty } ^ { + \infty } \int \displaylimits _ { - \infty } ^ { { Z } - { H } } \frac { { Z } - { H } _ { { P } } } { { I } ^ { 3 } } d x d y d z .
$$

For small surface slopes, the distance

$$
I = \sqrt { \left( X - X _ { P } \right) ^ { 2 } + \left( Y - Y _ { P } \right) ^ { 2 } + \left( Z - Z _ { P } \right) ^ { 2 } }
$$

may be approximated by

$$
I _ { { } _ { 0 } } = \sqrt { ( x - x _ { { } _ { P } } ) ^ { 2 } + { ( y - y _ { { } _ { P } } ) } ^ { 2 } } .
$$

The linear approximation of the terrain correction then reads

$$
\delta g _ { T } = \frac { 1 } { 2 } G \rho \int _ { - \infty } ^ { + \infty } \int _ { - \infty } ^ { + \infty } \frac { ( H - H _ { P } ) ^ { 2 } } { I _ { 0 } ^ { 3 } } d x d y ,
$$

where $H$ and $H _ { { \scriptscriptstyle P } }$ are the orthometric heights of the (running) terrain point and the point of calculation (Forsberg and Tscherning, 1997).

By including the terrain correction into (6.111), we obtain the terrain-corrected freeair anomaly, also called Faye anomaly. The shift of the topographic masses now corresponds to a condensation of the Bouguer plate on the geoid (Helmert’s condensation method), Heck (2003b). Here, the surface density

$$
\mu = \frac { d m } { d s } = \rho \frac { d v } { d s } = \rho H
$$

replaces the volume density $\rho$ and takes the height of topography into account.

As the mass displacement is slight, the indirect effect of the free-air and the condensation reduction remains small. It reaches a few meters in the absolute sense at most, and is of the cm- to dm-order of magnitude for geoid differences. As the height-dependent effect of the topographic masses has not been removed, free-air anomalies are strongly correlated with height. Therefore, point free-air anomalies are not suited for interpolation and cannot be geophysically interpreted. For limited areas, the height-dependence generally can be described by linear regression, this smoothing of the anomaly fi eld corresponds to the application of the Bouguer plate reduction (see below).

By removing the effect of topography explicitly through a topographic reduction $\delta g _ { \mathrm { t o p ^ { \prime } } }$ we obtain the Bouguer gravity anomaly $\Delta g _ { B }$ (we use this term under the assumption of a strict topographic mass reduction, although Bouguer for practical reasons originally applied an approximation, see below). After the removal of the masses the surface gravity again is reduced to the geoid by the free-air reduction and compared with the normal gravity $\gamma _ { _ { 0 } }$ (Fig. 6.24):

$$
\Delta g _ { _ B } = g - \delta g _ { _ { \mathrm { t o p } } } + \delta g _ { _ F } - \gamma _ { _ 0 } .
$$

The topographic reduction can be calculated from digital elevation models, applying the law of gravitation on standard mass elements, cf. [6.5.2].

Traditionally (in order to simplify calculation), the topographic reduction is decomposed into the Bouguer plate reduction $\delta g _ { \scriptscriptstyle P }$ and the terrain correction $\delta g _ { r }$ The Bouguer plate reduction accounts for the gravitation of an infi nitely extended horizontal plate with constant density. Its thickness is given by the height of the computation point. The gravitational effect of the Bouguer plate is derived from the attraction of a circular cylinder on a point located on the cylinder axis (e.g., Torge, 1989). By extending the cylinder radius to infi nity, one obtains

$$
\delta g _ { P } = 2 \pi G \rho H = 0 . 0 0 0 ~ 4 1 9 ~ \rho H ~ \mu \mathrm { m s ^ { - 2 } } ,
$$

where $\rho$ is taken in $\mathrm { k g / m } ^ { 3 }$ and $H$ in m. Here we have assumed that the terrain correction has reduced the actual topography to the Bouguer plate (see above). After this decomposition of the topographic reduction the Bouguer anomaly reads

$$
\Delta g _ { \scriptscriptstyle B } = g - \delta g _ { \scriptscriptstyle P } + \delta g _ { \scriptscriptstyle T } + \delta g _ { \scriptscriptstyle F } - \gamma _ { \scriptscriptstyle 0 } .
$$

Due to the removal of the height-dependent part of topography, Bouguer anomalies display smooth long-wave variations only. Hence, they are well suited for interpolation. Revealing density anomalies below the geoid, the Bouguer anomalies are also of considerable signifi cance in geophysics and geology, cf. [8.2.4]. For regional and local applications (e.g., national gravimetric surveys), a spherical Bouguer plate and a corresponding terrain correction is used frequently, with a calculation extending $1 7 0 ~ \mathrm { k m }$ from the computation point and conventional density being $2 6 7 0 ~ \mathrm { k g / m } ^ { 3 }$ . On the other hand, since the topographic masses are completely removed and not restored (i.e., they are shifted to infi nity!), the indirect effect on the geoid is very large (up to several $1 0 0 \ \mathrm { m }$ ). Hence, Bouguer anomalies are not used for geoid computations.

The Bouguer plate model also allows a simple calculation of the mean gravity $\bar { g }$ along the plumb line required for the computation of the orthometric height $H \left( 3 . 1 0 6 \right) _ { \cdot }$ , (6.81). If we assume a linear change of $g$ along the vertical, $\bar { g }$ will be found at the height $H / 2$ . Hence it can be derived from surface gravity by removing a Bouguer plate of thickness $H / 2 ,$ a free-air reduction from $H$ to $H / 2$ , and a subsequent restoration of the Bouguer plate above $H / 2$ . Removing and restoring the Bouguer plate has the same (negative) effect on gravity; so we obtain

$$
\bar { g } = g - \delta g _ { { \scriptscriptstyle P } } ( { \cal H } ) + \delta g _ { { \scriptscriptstyle F } } \left( \frac { { \cal H } } { 2 } \right) .
$$

Evaluation with (6.116) and (6.110), and introducing the density value $2 6 7 0 ~ \mathrm { k g / m ^ { 3 } } ,$ leads to (6.84).

Equation (6.118) also provides an important interpretation of the difference between the heights of the geoid and the quasigeoid, and the normal and the orthometric height, respectively. We calculate the mean normal gravity

$$
\bar { \gamma } = \gamma _ { { \scriptscriptstyle 0 } } - \delta g _ { { \scriptscriptstyle F } } \big ( \frac { H } { 2 } \big )
$$

according to (6.118), and subtract it from $\bar { g }$ . The mean gravity anomaly introduced in (6.9) is then identifi ed as the “simple” Bouguer anomaly (terrain correction neglected)

$$
\begin{array} { r } { \textstyle \bar { g } - \bar { \gamma } = g - \delta g _ { P } ( H ) + \delta g _ { F } ( H ) - \gamma _ { 0 } = \Delta g _ { B } . } \end{array}
$$

This fact permits a simple transformation from the geoid to the quasigeoid and vice versa, e.g., Flury and Rummel (2009), cf. [6.7.2].

Isostatic anomalies are formed by not only removing the gravitational effect of topography but by also restoring compensation masses in the Earth’s crust below the geoid, according to some isostatic model (e.g., Martinec, 1993). In this way, the crust is regularized, obtaining constant thickness and density, cf. [8.2.2]. The gravitation of the compensating masses is taken into account by an isostatic reduction $\delta g _ { I }$ to be calculated from the isostatic model according to [6.5.2]. The isostatic anomaly then is given by

$$
\Delta g _ { I } = g - \delta g _ { \mathrm { t o p } } + \delta g _ { I } + \delta g _ { F } - \gamma _ { 0 } .
$$

The largest part of the Earth’s topography is isostatically compensated. Hence, isostatic anomalies are small and vary smoothly about zero, with the exception of uncompensated areas (tectonic plate boundaries, regions of postglacial land uplift, etc.). They may be successfully employed for gravity prediction, and they are of value for geophysical and geodynamic interpretation, cf. [8.2.4]. As the compensating masses are arranged more remote from topography than in the free-air reduction (see above), the indirect effect is larger and may reach the amount of $^ { 1 0 \textrm { m } }$ . Therefore, isostatic anomalies have been rarely used for geoid calculations.

# 6.5.4 Orientation and scale of gravity fi eld models

We now investigate the orientation and the scale of a gravimetrically derived geoid/ quasigeoid, i.e., the “gravimetric datum”, see Hofmann-Wellenhof and Moritz (2005, p. 109 ff.).

The following assumptions were made for the spherical harmonic expansion of the disturbing potential and the quasigeoid/geoid, respectively, cf. [6.1.1], [6.5.1]:

• The level ellipsoid and the Earth have the same mass: $M _ { \mathrm { { E } | | } } = M .$ (6.122) • Hence, no zero-degree term $T _ { _ { 0 } }$ appeared in the expansion (6.4). The center of the ellipsoid and the Earth’s center of mass (origin of the global coordinate system) coincide; no fi rst-degree term entered into (6.4), cf. also [3.3.4]. . The normal potential $U$ and the real potential $W$ are related by

$$
U _ { Q } = W _ { P } .
$$