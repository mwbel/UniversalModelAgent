# Chapter 3

# Observations

# 3.1 INTRODUCTION

In the late 1950s, a ground-based tracking system known as Minitrack was installed to track the Vanguard satellites. This system, which was based on radio interferometry, provided a single set of angle observations when the satellite passed above an instrumented station’s horizon. These angle measurements, collected from a global network of stations over several years, were used to show that the Earth had a pear-shape. They also provided the means to investigate the nature of forces acting on Vanguard and their role in the multiyear orbit evolution of the satellite.

A variety of observations are now available to support the determination of a satellite orbit. For the most part, these observations are collected by instrumentation that measures some scalar quantity related to the satellite’s position or velocity. Modern systems such as the Global Positioning System (GPS) provide the position of a GPS receiver, but even GPS requires the use of scalar measurements to determine the orbits of the individual satellites that comprise the GPS constellation. The dependence of scalar measurements on the satellite state (position and velocity) is a key element in the orbit determination process.

Section 3.2 describes an ideal representation of the commonly used measurements. This ideal representation not only serves as an introduction to the measurement type, it also can be used for simulations and other analyses of the orbit determination process. A more realistic description of those measurements is provided in Section 3.3, but from a conceptual viewpoint. The hardware realization of the measurements is discussed in Section 3.4, including other effects, such as those associated with propagation of signals through the atmosphere. The hardware realization must be modeled in terms of the orbit parameters to be determined; hence, this modeling produces a computed observation, which is an essential part of the orbit determination process. Examples of measurements obtained by selected instrumentation are discussed in Section 3.5. The use of differenced measurements to remove errors with speci c characteristics is discussed in Section 3.6. The use of a satellite ephemeris and angles are discussed in the nal sections of this chapter. Supplementary material can be found in Montenbruck and Gill (2001) and Seeber (1993).

# 3.2 OBSERVATIONS

# 3.2.1 IDEAL RANGE

A common measurement in orbit determination is the distance between an Earth-based instrument performing the measurement and the satellite. If the position vector of an instrument is $\mathbf { r } _ { I }$ and the position vector of the satellite is $\mathbf { r }$ , the ideal range $\rho$ is the scalar magnitude of the position vector of the satellite with respect to the instrument,

$$
\rho = [ ( \mathbf { r } - \mathbf { r } _ { I } ) \cdot ( \mathbf { r } - \mathbf { r } _ { I } ) ] ^ { 1 / 2 } .
$$

In this ideal representation, the range should be more precisely described as the geometric range or instantaneous range, since it represents the instantaneous, geometric distance between the measuring instrument and the satellite. This ideal representation has ignored subtle issues, such as the nite speed of light and the fact that $\rho$ is the distance between a speci c point within the instrument and a speci c point on the satellite. Furthermore, if $\rho _ { \mathrm { o b s } }$ represents the measured range at time $t$ , $\mathbf { r }$ and $\mathbf { r } _ { I }$ represent the true position vectors at this time, then $\rho$ and $\rho _ { \mathrm { o b s } }$ are related by

$$
\rho _ { \mathrm { o b s } } = \rho + \epsilon
$$

where $\epsilon$ represents instrumental errors and propagation delays. Note also that if the position vectors $\mathbf { r }$ and $\mathbf { r } _ { I }$ are in error, then $\epsilon$ must contain terms that would be necessary to make Eq. (3.2.2) an equality.

The geometric range, $\rho$ , is invariant under rotation of axes used to describe r and $\mathbf { r } _ { I }$ . That is, if $( X , Y , Z )$ represents an inertial system and $( x , y , z )$ represents an Earth- $\mathbf { X }$ ed system, the geometric range can be expressed as

$$
\rho = [ ( X - X _ { I } ) ^ { 2 } + ( Y - Y _ { I } ) ^ { 2 } + ( Z - Z _ { I } ) ^ { 2 } ] ^ { 1 / 2 }
$$

or

$$
\rho = [ ( x - x _ { I } ) ^ { 2 } + ( y - y _ { I } ) ^ { 2 } + ( z - z _ { I } ) ^ { 2 } ] ^ { 1 / 2 }
$$

where $\rho$ is identical for both representations.

# 3.2.2 IDEAL RANGE RATE

In some cases, the time rate of change of the range, or range-rate, may be the measured quantity. From the expression of range in the $( X , Y , Z )$ nonrotating system, Eq. (3.2.3), differentiation with respect to time yields

$$
\begin{array} { r c l } { \dot { \rho } } & { = } & { \Big [ ( X - X _ { I } ) ( \dot { X } - \dot { X } _ { I } ) + ( Y - Y _ { I } ) ( \dot { Y } - \dot { Y } _ { I } ) } \\ & & { + ( Z - Z _ { I } ) ( \dot { Z } - \dot { Z } _ { I } ) \Big ] \Big / \rho } \end{array}
$$

or

$$
{ \dot { \rho } } = { \frac { \rho \cdot { \dot { \rho } } } { \rho } }
$$

where $\rho = ( X - X _ { I } ) \mathbf { u } _ { X } + ( Y - Y _ { I } ) \mathbf { u } _ { Y } + ( Z - Z _ { I } ) \mathbf { u } _ { Z }$ , the position vector of the satellite with respect to the instrument. The relative velocity is

$$
{ \dot { \boldsymbol { \rho } } } = ( { \dot { X } } - { \dot { X } } _ { I } ) \mathbf { u } _ { X } + ( { \dot { Y } } - { \dot { Y } } _ { I } ) \mathbf { u } _ { Y } + ( { \dot { Z } } - { \dot { Z } } _ { I } ) \mathbf { u } _ { Z } .
$$

Note that the position and velocity of a ground-based instrument expressed in the nonrotating $( X , Y , Z )$ system will be dependent on the rotation of the Earth.

Equation (3.2.6) can readily be interpreted as the component of the relative velocity in the direction de ned by the relative position vector, $\rho$ . In other words, the range-rate is the component of the relative velocity between the observing instrument and the satellite in the line-of-sight direction t he direction de ned by $\rho$ . As described in the preceding section, if $\dot { \rho } _ { \mathrm { o b s } }$ is the observed parameter, then $\dot { \rho } _ { \mathrm { o b s } }$ is equal to $\dot { \rho }$ plus the inclusion of instrumental, media, and other errors.

# 3.2.3 IDEAL AZIMUTH AND ELEVATION ANGLES

A topocentric system was de ned in Section 2.4.3. If the relative position vector, $\rho$ , is expressed in this system, then the angles, azimuth and elevation, can be de ned, as noted in Section 2.4.3. The angles are illustrated in Fig. 2.4.4.

# 3.2.4 EXAMPLES: IDEAL OBSERVATIONS

In Example 2.2.4.1, the initial conditions for a Shuttle-like orbit were given and the state was predicted forward in time with Example 2.2.5. This ephemeris was transformed into Earth- x ed coordinates and the ground track can be found in Fig. 2.2.7. If the initial conditions differ by 1 meter in the radial component with respect to those in Example 2.2.4.1, the difference between the two ephemerides is illustrated in Fig. 2.2.9 for about two orbital revolutions. If the perturbed initial conditions in Example 2.2.6.1 are assumed to represent the trut h, then a set of simulated observations can be generated. For this discussion, simulated observations are represented by geometric ranges (Section 3.2.1) and range-rate (Section 3.2.2). Simulated observations are useful to characterize different error sources in a controlled experiment.

Table 3.2.1: Coordinates of Simulated Ranging Instruments   

<table><tr><td colspan="4">Earth-Fixed Coordinates</td><td colspan="3">Geocentric</td></tr><tr><td>Site</td><td>x (m)</td><td>y(m)</td><td>z(m)</td><td></td><td>Latitude</td><td>Longitude</td></tr><tr><td>FZ</td><td>4985447.872</td><td>2-3955045.423</td><td>-428435.301</td><td>3.8516°S</td><td></td><td>38.4256°W</td></tr><tr><td>EI</td><td></td><td>-1886260.450 -5361224.413 -2894810.165</td><td></td><td></td><td>26.9919°S</td><td>109.3836W</td></tr></table>

FZ: Fortaleza EI: Easter Island Note: x,y,z computed from latitude, longitude, and a spherical Earth with radius $6 3 7 8 1 3 7 . 0 \ \mathrm { m }$

Consider two hypothetical sites capable of making range measurements: Easter Island and Fortaleza, Brazil. Assume the true coordinates of these two sites are given in Table 3.2.1. The ground tracks of the orbit in the vicinity of these sites are illustrated in Fig. 3.2.1, extracted from the global ground tracks shown in Fig. 2.2.6. The interval while the satellite is above the station’s horizon is termed a pass. In some cases, the measurements below a speci ed elevation may be ignored, usually referred to as the elevation mask. The rst candidate pass from Fortaleza rises less than $1 ^ { \circ }$ in elevation, so with a $5 ^ { \circ }$ elevation mask, for example, this pass would be ignored. An elevation mask usually is adopted to edit lowelevation passes because of poor signal-to-noise ratios, excessive atmospheric refraction, or multipath effects. For the case shown in Fig. 3.2.1, two passes are observed from Easter Island and one pass from Fortaleza, ignoring the very lowelevation pass at Fortaleza.

The geometric ranges to the satellite observed by each station over three passes are shown in Fig. 3.2.2, where time is measured from the time of the initial state given in Example 2.2.4.1. The minimum range point in each plot is the point of closest approach of the satellite to the station. If the ranging instrument had a measurement noise at the one meter level, it is clear that this characteristic would not be visually obvious in Fig. 3.2.2.

The range-rates observed from Easter Island are shown in Fig. 3.2.3. Since range-rate is the time derivative of range, the point of minimum range corresponds to zero range-rate.

A sky plot is a useful way to visualize the geometry of a satellite pass above an observing station’s horizon. The sky plot for each of the three passes illustrated in Fig. 3.2.2 is shown in Fig. 3.2.4. The concentric circles represent an elevation increment of $3 0 ^ { \circ }$ , where the outermost circle is the station’s horizon $0 ^ { \circ }$ elevation), and the center point is $9 0 ^ { \circ }$ elevation (directly overhead the station). The plot shows the azimuth, measured eastward from north. For example, for Pass 1 from Easter Island, the satellite rises above the station horizon at an azimuth of $- 5 9 ^ { \circ }$ (i.e., $5 9 ^ { \circ }$ west of north) and sets at $9 6 ^ { \circ }$ azimuth $9 6 ^ { \circ }$ east of north). The highest elevation for this pass is about $4 0 ^ { \circ }$ at an azimuth of $2 3 ^ { \circ }$ .

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0002_pages_0071-0140/auto/images/a25f4487347f1aff2165dd7c6b986bd7ef863a77d2595be3cc7e257ec5a9a8fe.jpg)  
Figure 3.2.1: Portion of shuttle ground track from Fig. 2.2.6. The two orbital revolutions in the vicinity of simulated tracking stations at EI (Easter Island) and FZ (Fortaleza) produce two passes that are within view of the stations. However, the satellite in Pass 1 at Fortaleza rises above the horizon by less than $5 ^ { \circ }$ in elevation.

If the initial conditions in Example 2.2.6.2 represent the true initial conditions, and the set given by Example 2.2.4.1 are used as a nominal or reference set, a residual can be formed as the observed minus computed, or $o$ minus $C \left( O - C \right)$ . Within the context of orbit determination applications, the true initial conditions are unknown, but the observations represented by the ranges in Fig. 3.2.2 are the result of the true state and the measuring instrument characteristics. Usually, a nominal set of initial conditions are available but they deviate from the true values. Nevertheless, based on the nominal initial conditions, a computed range can be formed. The resulting residuals for the three passes are shown in Fig.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0002_pages_0071-0140/auto/images/408ea2474097e6bb85dc8e5ea4a157c1cc5f45aa909c1a9f95c2368321ac06ad.jpg)

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0002_pages_0071-0140/auto/images/372ca48e8124fc9b289ff4c6a9ad5ce1a3c60c158ba9e3f9614dec1324540602.jpg)  
Figure 3.2.2: Simulated range vs time. These plots show the geometric range vs time measured by the two sites, Easter Island and Fortaleza, shown in Fig. 3.2.1.   
Figure 3.2.3: Simulated range-rate vs time.

3.2.5. It has been assumed that all ranges are instantaneous and no atmospheric delays have been included in these simulations. In essence, the residuals in Fig. 3.2.5 illustrate how the orbit differences of Fig. 2.2.9 are exhibited in terms of range residuals from ground-based stations.

Consider the residual, $O - C$ , for the second pass from Easter Island. As shown in the sky plot for this pass in Fig. 3.2.4, the satellite passes nearly overhead, with a maximum elevation of about $7 8 ^ { \circ }$ . When the satellite rises above the Easter Island horizon in the west, the measured range re ects a signi cant component in the along-track direction. As described in Section 2.2.6.2, the position on the true orbit trails the position on the nominal orbit in the along-track direction. It follows that the true range will be longer than the range to the reference position. As a consequence, the orbit differences shown in Fig. 2.2.9 will result in $( O - C ) > 0$ at satellite rise, but $( O - C ) < 0$ when the satellite sets at the observing station’s horizon. At some point during the pass over the station, the satellite motion will be perpendicular to the observer’s viewing direction, so none of the along-track differences will be seen ; that is, $O$ goes to zero. If the pass has a lower elevation, the basic characteristics are the same, as shown for the low-elevation Fortaleza pass in Fig. 3.2.5.

# 3.3 CONCEPTUAL MEASUREMENT SYSTEMS

# 3.3.1 RANGE

All measurements of range are based on the time-of- ight principle. Simply stated, an instrument transmits a signal, usually with some appropriate time duration, which is re ected by a passive target or retransmitted by an active target. A two-way range may originate with an instrument located on the surface of the Earth, or ground-based instrument, and the signal will travel to the satellite and back to the transmitting site. One example of a two-way instrument is the satellite laser ranging (SLR) hardware, which is described in Section 3.5.2. In the SLR measurement, a laser pulse travels on an uplink path to the satellite, where it is re ected. The downlink path takes the signal from the satellite back to the transmitting site. The uplink and downlink paths constitute the two-way measurement. Some two-way range measurements may be transmitted and received at the same location by essentially the same instrumentation, but others may use a transmitter at one location and a receiver at another. This latter case is sometimes referred to as a three-way measurement, in spite of only uplink and downlink paths in the measurement. In some communities, the term $b i$ -static measurement may be used.

The one-way range is based on the transmittal of a signal by a satellite or a ground-based transmitter that is received by separate instrumentation. If the transmit source is within the satellite, the signal may travel only a downlink path.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0002_pages_0071-0140/auto/images/7c6c8c4cd498f671e36612336a6dee067fcaed4380c818ab6bb8d790dc26bf7f.jpg)  
Figure 3.2.4: Sky plots. These plots illustrate the azimuth and elevation for the three passes shown in the ground track of Fig. 3.2.1. The circles represent increments of $3 0 ^ { \circ }$ elevation, with the outermost circle at $0 ^ { \circ }$ elevation and the center of the circles at $9 0 °$ elevation. Azimuth is measured clockwise from north.

Alternatively, the transmitter could be ground-based, and the signal might be received by satellite-borne instrumentation on the uplink path. An important example of the satellite-borne transmitter is the Global Positioning System (GPS), discussed in Section 3.5.1. Even in the case of GPS, the receiver could be located on a satellite, rather than being ground-based.

# One-Way Range

Assume a signal of very short duration is transmitted with a specific electromagnetic frequency at time $t _ { T }$ . The transmitted signal propagates along a path and arrives at a point instrumented to receive the transmitted signal. The signal arrives at the receiver at time $t _ { R }$ . Since the signal travels at the speed of light, denoted by $c$ , the signal has traveled a one-way distance given by

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0002_pages_0071-0140/auto/images/eace288fb7a75e6e220f4b36cc78f7307369e7e3fa1732a3d9e08edc277f78b7.jpg)  
Figure 3.2.5: Range residuals vs time. The range residuals, $( O - C )$ , for the three passes illustrate the effect of the orbit error shown in Fig. 2.2.9 on range residuals. The orbit used to generate $O$ is Example 2.2.6.1 and the orbit used to generate $C$ is Example 2.2.4.1.

$$
\tilde { \rho } = c ( t _ { R } - t _ { T } ) .
$$

Different clocks are used to register the respective times, $t _ { R }$ and $t _ { T }$ . If the clocks used to record $t _ { R }$ and $t _ { T }$ are precisely synchronized, then $\tilde { \rho }$ represents the true range, aside from other effects such as atmospheric delays of the signal propagation. For the discussion in this section, $c$ will represent the speed of light in a vacuum. Unfortunately, the clocks used are generally not well-synchronized. In fact, if the clock used to determine the transmit time is running significant ly faster than the receiver clock, the quantity $\tilde { \rho }$ could be negative! With the synchronization aspect in mind, the quantity $\tilde { \rho }$ generally will not represent the true range, but it is related to the true range. As a consequence, $\tilde { \rho }$ is designated the pseudorange.

Using the GPS case as an example, a signal with special characteristics is transmitted. The time when this signal is transmitted is predetermined, but the actual time when the signal is emitted will be controlled by the satellite clock. The time of signal arrival at a reception site is measured by an independent clock. Let $t$ represent clock time—tim e as registered by a clock—b ut let $T$ represent true time. Everyday experience suggests that a reasonable model for the relation between clock time and true time is the linear relation

$$
\begin{array} { r } { t = T + a + b ( T - T _ { 0 } ) + \epsilon ^ { \prime } } \end{array}
$$

where $a$ represents a constant offset of clock time from true time, $b$ represents a linear clock drift, $T _ { 0 }$ is a reference time, and $\epsilon ^ { \prime }$ represents other errors, such as nonlinear terms and stochastic components. In essence, the linear clock model is assumed to be valid over the interval from $T _ { 0 }$ to $T$ . Applying Eq. (3.3.2) to both the transmitter clock and the receiver clock, the pseudorange becomes

$$
{ \tilde { \rho } } = c ( T _ { R } - T _ { T } ) + c ( a _ { R } - a _ { T } ) + c ( b _ { R } - b _ { T } ) ( T - T _ { 0 } ) + \epsilon
$$

where the subscript $T$ refers to the transmitter clock, $R$ denotes the receiver clock, and $\epsilon$ is the difference between the other error sources. Since the term $c ( T _ { R } - T _ { T } )$ is the true range, it is evident that

$$
\tilde { \rho } = \rho ( T _ { T } , T _ { R } ) + c ( a _ { R } - a _ { T } ) + c ( b _ { R } - b _ { T } ) ( T - T _ { 0 } ) + \epsilon
$$

where $\rho ( T _ { T } , T _ { R } )$ is the distance between the transmit point at time $T _ { T }$ and the receive point at $T _ { R }$ ; that is, the true range. Recall that the true range is distinctly different from the ideal range, which does not account for the finite speed of light. It is further evident that pseudorange differs from true range by the clock-related terms. Furthermore, if the time interval $( T - T _ { 0 } )$ and the difference in drift terms are suffici ently small, then

$$
\tilde { \rho } = \rho + c ( a _ { R } - a _ { T } ) + \epsilon
$$

which illustrates that pseudorange is a biased range; the pseudorange differs from true range by a “constant” term (plus noise). Letting $\rho _ { b }$ represent $c ( a _ { R } - a _ { T } )$ , a range bias, it follows that

$$
\tilde { \rho } = \rho + \rho _ { b } + \epsilon .
$$

This discussion has ignored the influence of other delays that contribute to the signal arrival time. In particular, atmospheric refraction will delay the signal (see Section 3.4.2) and contribute an additional term, $\delta \rho _ { \mathrm { a t m } }$ , to Eq. 3.3.5 to yield

$$
\tilde { \rho } = \rho + \rho _ { b } + \delta \rho _ { \mathrm { a t m } } + \epsilon .
$$

The one-way range instrumentation measures $\tilde { \rho }$ by determining $t _ { T }$ and $t _ { R }$ . Equation (3.3.7) shows that the measured quantity is a biased range. A useful alternate form of Eq. (3.3.7) is

$$
\tilde { \rho } = \rho + c \delta t _ { R } - c \delta t _ { T } + \delta \rho _ { \mathrm { a t m } } + \epsilon
$$

where $\delta t _ { R }$ is the receiver clock correction and $\delta t _ { T }$ is the transmitter clock correction. For example, from Eq. (3.3.4), $\delta t _ { R } = a _ { R } + b _ { R } ( T - T _ { 0 } )$ plus higher order and random components.

From Eq. (3.3.7) the measured quantity, $\tilde { \rho }$ , is related to the satellite position at time $T _ { T }$ and the receiver position at time $T _ { R }$ , or

$$
\tilde { \rho } = [ ( X - X _ { I } ) ^ { 2 } + ( Y - Y _ { I } ) ^ { 2 } + ( Z - Z _ { I } ) ^ { 2 } ] ^ { 1 / 2 } + \rho _ { b } + \delta \rho _ { \mathrm { a t m } } + \epsilon
$$

where $( X , Y , Z )$ represents the true position of the satellite at time $T _ { T }$ and the true instrument components $( X , Y , Z ) _ { I }$ are determined at $T _ { R }$ .

A computed pseudorange, $\tilde { \rho } _ { c }$ , would be formed with an assumed, or nominal, ephemeris for the satellite and coordinates of the instrument and other parameters in Eq. (3.3.9). A residual would be obtained from the difference, $\tilde { \rho } - \tilde { \rho } _ { c }$ . Such a residual is required in orbit determination.

It is significant to note that the true range, $\rho$ , is formed as the magnitude of the difference between two position vectors, each of which has a different time attached to it. As a consequence, these two vectors must be expressed in the same reference frame. If the reference frame is nonrotating, the resulting path is simply the straight line distance between the two vectors. If an Earth-fix ed frame is used, for example, the path appears to be curved and it will be necessary to account for this curvature. Unless otherwise stated, it will be assumed that $\rho ( T _ { T } , T _ { R } )$ will be formed using a nonrotating reference frame.

Table 3.3.1 shows the quantity $\langle \delta T = T _ { R } - T _ { T } \rangle$ for transmitting satellites at different altitudes, assuming the satellite is at the zenith of a ground-based receiver. With $c = 2 9 9 , 7 9 2 . 4 5 8 \mathrm { k m / s e c }$ , the GPS case is $2 0 , 0 0 0 \div c = 0 . 0 8 6 7 3$ sec.

# Two-Way Range

The two-way range includes both an uplink and a downlink path, where the order will be dependent on the transmitter source. For this discussion, assume the transmitter to be located on the Earth’s surface and the same instrumentation will be used to receive the return signal. For simplicity, assume no time delay exists when the signal arrives at the satellite and is retransmitted. This description matches the ground-based satellite laser ranging (SLR) instrumentation, where the transmitted laser pulse is refle cted by the satellite back to the transmitting station. Another important example is a satellite altimeter, where the satellite-borne altimeter emits a pulse in the satellite nadir direction and the pulse is reflected by the Earth’s surface (e.g., the ocean) back to the satellite. For simplicity, assume the transmitted pulse has a Gaussian shape. A commonly used point on the pulse for determination of $t _ { T }$ is the centroid, but other points may be used that are determined by the hardware characteristics. The return pulse is usually characterized by lower energy, but if the return pulse is also Gaussian, the receive time, $t _ { R }$ , can be determined for the centroid. In the SLR case, the instrumentation records the time when the laser pulse was transmitted by the ground-based hardware, $t _ { T }$ , and the time, $t _ { R }$ , represents the time when some portion of that pulse returns to the transmitting site after being reflect ed by the satellite. Hence, the round-trip distance traversed by the pulse is

Table 3.3.1: One-Way $\delta T = T _ { R } - T _ { T }$ at Ground Observer Zenith   

<table><tr><td>Transmitter</td><td>Altitude (km)</td><td>δT (millisec)</td></tr><tr><td>Shuttle</td><td>400</td><td>1.33</td></tr><tr><td>ERS-1</td><td>700</td><td>2.33</td></tr><tr><td>TOPEX/Poseidon</td><td>1336</td><td>4.46</td></tr><tr><td>GPS</td><td>20,000</td><td>86.73</td></tr><tr><td>Geosynchronous</td><td>36,000</td><td>140.10</td></tr></table>

$$
\rho _ { r t } = c ( t _ { R } - t _ { T } )
$$

where the transmit and receive times are measured by the same clock, denoted by clock time, $t$ . Since the path length is the round-trip distance, the two-way ranges corresponding to the examples in Table 3.3.1 will be double those shown.

As in the one-way example, assume the instrumentation clock can be characterized by a linear clock model, Eq. (3.3.2). It follows that

$$
\rho _ { r t } = c ( T _ { R } - T _ { T } ) + b ( T _ { R } - T _ { T } ) + \epsilon
$$

where the offset term, $a$ , has cancelled since it is assumed to be based on the same clock. If the clock drift is sufficiently small over the round-trip time interval and other clock error terms plus atmospheric delays can be ignored, then the round-trip range is essentially the true round trip distance. The removal of the major clock term, $a$ , in the two-way range is a significant advantage for this measurement type.

As in the one-way range case, atmospheric delays must be considered. Assuming the drift term can be ignored, it follows that a more accurate representation of Eq. (3.3.11) is

$$
\rho _ { r t } = c ( T _ { R } - T _ { T } ) + \delta \rho _ { \mathrm { a t m } } + \epsilon
$$

where $\delta \rho _ { \mathrm { a t m } }$ is the atmospheric delay contribution.

The orbit determination process will compare the measured range, $\rho _ { r t }$ , to a computed value based on $t _ { T }$ and $t _ { R }$ , a nominal satellite ephemeris and nominal ground station coordinates, plus modeled atmospheric contributions and other effects. A computed value of $\rho _ { r t }$ with this information is not straightforward, since the computation requires the time when the signal arrives at the satellite, but this parameter is not directly measured.

An iterative process can be invoked for the computed two-way range to determine the unknown time of arrival of the signal at the satellite. Two sets of iterations are required. For this discussion, assume that errors in clock time, $t$ , are insignificant. Further assume that an ECI nominal satellite ephemeris is available and that an appropriate procedure is available to evaluate the ephemeris for any arbitrary time. It is also assumed that nominal coordinates of a ground-based ranging station are given in ECF, but the transformation between ECF and ECI is known. The following description of the iteration assumes that the signal propagates in a straight line path in the ECI frame (e.g., a very narrow laser beam); hence the description of the procedure is based on ECI.

If the measured signal transmit time, $t _ { T }$ , is taken as the starting point, then the computed two-way range can be determined as follows:

1. Determine the instantaneous range, $\rho$ , between the station and the satellite at $t _ { T }$ using Eq. (3.2.3). This step requires evaluation of the ephemeris at $t _ { T }$ and the station coordinates in ECI, so the ECF coordinates are transformed into ECI using the ECF-to-ECI transformation matrix, Eq. (2.4.11).   
2. Compute the approximate signal arrival time at the satellite as $t _ { a } = t _ { T } +$ $\rho / c$ .   
3. Evaluate the ephemeris at ta and compute the corresponding range, ρnew, between the ECI satellite position at $t _ { a }$ and the ECI position of the station at $t _ { T }$ .   
4. Compare $\rho$ and $\rho _ { \mathrm { n e w } }$ ; if the difference is less than some specifie d criteria, such as 1 micrometer, then the process has converged and no more iterations are required. Otherwise, rename $\rho _ { \mathrm { n e w } }$ to be $\rho$ and go to step 2.

After converging on the computed signal arrival time, $t _ { a }$ , and the corresponding uplink range, $\rho$ , the next set of computations determine the downlink range and time of arrival at the station based on the models. A procedure similar to the one given earlier can be followed. In this case, the arrival time at the satellite will be assumed to be known from the first iteration, and the arrival time at the station is unknown. This arrival time will most likely differ from the measured arrival time because of errors in the nominal orbit, errors in the station coordinates, and mismodeling of the media corrections.

It turns out, however, that the preceding iterative process can be remarkably simplified. From the measured round-trip range, $\rho _ { r t }$ , the average range can be determined as $\rho _ { \mathrm { a v g } } = \rho _ { r t } / 2$ and the approximate pulse arrival time at the satellite is $\rho _ { r t } / ( 2 c ) = \delta \tau$ . It follows that the satellite pulse arrival time is $t _ { a } = t _ { T } + \delta \tau$ . If the instantaneous range is computed at $t _ { a }$ (evaluate the ephemeris and the ECI station coordinates at this $t _ { a }$ ), this range is approximately equal to $\rho _ { \mathrm { a v g } }$ , at least to the submillimeter level. As a consequence, the measured round-trip range can be modeled by the instantaneous range (one-way) determined at the time $t _ { a }$ .

In the case of a satellite-borne altimeter, the two-way measurement originates with an instrument in the satellite, but the signal propagation is earthward, usually in the nadir direction defined by either the local geodetic vertical or the radial direction to the geocenter. In the altimeter case, the signal is reflected by the Earth’s surface (e.g., the ocean). The preceding discussion in this section for the ground-based instrument applies as well to the altimeter. Let $h _ { r t }$ represent the round-trip altitude, and

$$
h _ { r t } = c ( t _ { R } - t _ { T } )
$$

where $t _ { R }$ is the signal transmit time and $t _ { T }$ is the receive time. Note that the measurement consists of a downlink path (satellite to surface) and an uplink path for the echo (surface to satellite). Even in the ECI coordinate system, the motion of the Earth has a small contribution to $h _ { r t }$ during the round-trip interval.

As in the case of the previous two-way range, the computed altitude requires an iterative process to determine the surface time of arrival. In the general case that allows for an off-nadir pointed altimeter, the process is similar to the preceding discussion for the ground-based two-way ranging station. The average altitude is

$$
h _ { \mathrm { a v g } } = h _ { r t } / 2
$$

and the average time is

$$
t _ { \mathrm { a v g } } = t _ { T } + h _ { \mathrm { a v g } } / c .
$$

As in the preceding case, $h _ { \mathrm { a v g } }$ is a good approximation (submillimeter) to the instantaneous altitude formed at $t _ { \mathrm { a v g } }$ . The time of signal arrival at the surface is closely represented by $t _ { \mathrm { a v g } }$ .

# Example

Consider a satellite in an equatorial posigrade, circular orbit with an altitude of $6 0 0 { \mathrm { k m } }$ above a spherical Earth. Assume the satellite is $2 0 ^ { \circ }$ in true anomaly past the zenith direction of a two-way ranging station, which places the satellite at $4 . 3 ^ { \circ }$ elevation with respect to the station. Assume a signal is transmitted by the station at $t = 0$ . The uplink iteration to determine the computed range gives 2393433.99356 meters, with signal arrival at the satellite 0.007983636445 sec after transmission. The downlink iteration gives 2393426.58799 meters and a signal arrival at the ground station 0.015967248187 sec $( \delta \tau )$ after transmission. The average range (sum of uplink and downlink, divided by two) is 2393430.290775 meters. Determination of the instantaneous range at $\delta \tau / 2$ (0.007983624094 sec) gives 2393430.290689 meters.

# 3.3.2 RANGE-RATE

Most range-rate systems in current use are based on a single propagation path, either uplink or downlink. The following discussion treats the problem from two viewpoints: an instrument transmitting a short duration pulse at a known interval and a beacon that transmits a signal with a known frequency.

# Repeated Pulse Transmission

Assume a satellite-borne instrument transmits a pulse at a specified and fix ed interval, $\delta t _ { T }$ . Hence, the pulses are transmitted at a sequence of times (e.g., $t _ { T 1 } , t _ { T 2 }$ , etc). The transmitted pulses are received by a ground-based instrument and the arrival times are recorded as $t _ { R 1 } , t _ { R 2 }$ , and so on, where $t _ { R 1 }$ is the arrival of the pulse transmitted at $t _ { T 1 }$ . The transmit and receive times are related by

$$
\begin{array} { r c l } { { t _ { R 1 } } } & { { = } } & { { { t _ { T 1 } } + \rho _ { 1 } / c } } \\ { { t _ { R 2 } } } & { { = } } & { { { t _ { T 2 } } + \rho _ { 2 } / c , } } \end{array}
$$

and so on, where the relation to Eq. (3.3.1) is obvious. If $t _ { R 1 }$ is subtracted from $t _ { R 2 }$ , it follows that

$$
t _ { R 2 } - t _ { R 1 } = \delta t _ { T } + ( \rho _ { 2 } - \rho _ { 1 } ) / c
$$

or

$$
\delta t = \delta t _ { T } + \delta \rho / c
$$

where $\delta t = t _ { R 2 } - t _ { R 1 }$ and $\delta \rho$ represents the range change between $t _ { T 2 }$ and $t _ { T 1 }$ . Consider the following cases:

• If $\rho _ { 2 } > \rho _ { 1 }$ : the length of the path traversed by the signal is getting longer (the transmitter and receiver are getting farther apart), then $\delta t > \delta t _ { T }$ . In other words, the time between successive pulse arrivals is longer than the fix ed interval between their transmission, $\delta t _ { T }$ .

• If $\rho _ { 2 } < \rho _ { 1 }$ : the length of the signal path is getting shorter (the transmitter and receiver are moving toward each other), then $\delta t < \delta t _ { T }$ . In this case, the time between successive pulse arrivals is shorter than $\delta t _ { T }$ .

• If $\rho _ { 2 } = \rho _ { 1 }$ : there is no change in the signal path length and the pulse arrival interval equals the pulse transmit interval.

Equation (3.3.18) can be rewritten as

$$
\delta t = \delta t _ { T } ( 1 + ( \delta \rho / \delta t _ { T } ) / c )
$$

where $( \delta \rho )$ is the range change in the time interval $\delta t _ { T }$ . Hence, $\delta \rho / \delta t _ { T }$ is a form of range-rate. If the ground-based instrument measures $\delta t$ , it is evident that this measured quantity is dependent on the range change during the interval $\delta t _ { T }$ . Note that the measured quantity is not the instantaneous range-rate, although the shorter the interval $\delta t _ { T }$ , the closer the measured quantity will be to the instantaneous range-rate. In a sense, the previous description is a form of measurement differences, which is discussed later in this chapter. Since the same clock is used to determine the pulse transmit times and a separate clock is used to measure the pulse receive times, the quantities $\delta t$ and $\delta t _ { T }$ are time differences based on the time recorded by separate clocks. As in the case of two-way ranging, the dominant clock model term, $a$ , will cancel in the differencing process while the drift and higher order clock effects will remain at some level.

# Transmitter Beacon

Assume a satellite contains a radio beacon that transmits a signal with a known frequency, $f _ { T }$ . The transmitted signal arrives at a ground-based site with an apparent frequency $f _ { R }$ , but this arrival signal is usually mixed with a reference frequency standard at the site. The arriving signal is multiplied with the reference frequency, $f _ { G }$ , which yields a signal that contains frequencies of $\left( f _ { G } + f _ { R } \right)$ and $\left( f _ { G } - f _ { R } \right)$ . The sum of frequencies is filtered and if $f _ { G }$ is essentially $f _ { T }$ , the resulting $\left( f _ { G } - f _ { R } \right)$ signal represents the apparent change in transmitted frequency. The receiver is designed to count the number of cycles at this frequency between two times, $t _ { R _ { 1 } }$ and $t _ { R _ { 2 } }$ , thus

$$
N _ { 1 , 2 } = \int _ { t _ { R _ { 1 } } } ^ { t _ { R _ { 2 } } } ( f _ { G } - f _ { R } ) d t
$$

where $N _ { 1 , 2 }$ represents the number of integer cycles plus the fractional part of a cycle in the measured frequency $\left( f _ { G } - f _ { R } \right)$ during the time interval between $t _ { R _ { 1 } }$ and $t _ { R _ { 2 } }$ . Let

$$
t _ { R _ { 1 } } = t _ { T _ { 1 } } + \Delta t _ { 1 }
$$

and

$$
t _ { R _ { 2 } } = t _ { T _ { 2 } } + \Delta t _ { 2 }
$$

where $\Delta t _ { 1 } { = } \rho _ { 1 } / c$ and $\rho _ { 1 }$ is the distance from the transmit point to the receive point at $t _ { R _ { 1 } }$ . Assuming that $f _ { G }$ is constant,

$$
N _ { 1 , 2 } = f _ { G } \left[ t _ { T _ { 2 } } - t _ { T _ { 1 } } + ( \rho _ { 2 } - \rho _ { 1 } ) / c \right] - \int _ { t _ { R _ { 1 } } } ^ { t _ { R _ { 2 } } } f _ { R } d t .
$$

However, the last integral is

$$
\int _ { t _ { R _ { 1 } } } ^ { t _ { R _ { 2 } } } f _ { R } d t = \int _ { t _ { T _ { 1 } } } ^ { t _ { T _ { 2 } } } f _ { T } d t = f _ { T } \left[ t _ { T _ { 2 } } - t _ { T _ { 1 } } \right] .
$$

Thus,

$$
N _ { 1 , 2 } = ( f _ { G } - f _ { T } ) ( t _ { T _ { 2 } } - t _ { T _ { 1 } } ) + f _ { G } ( \rho _ { 2 } - \rho _ { 1 } ) / c .
$$

Let $\delta t = t _ { T _ { 2 } } - t _ { T _ { 1 } } , \delta \rho = \rho _ { 2 } - \rho _ { 1 }$ , and $f _ { G }$ equal $f _ { T }$ , then

$$
N _ { 1 , 2 } / \delta t = ( f _ { T } / c ) ( \delta \rho / \delta t ) .
$$

It follows that

$$
f _ { R } = f _ { T } - N _ { 1 , 2 } / \delta t ,
$$

so the apparent received frequency is $f _ { T } ( 1 - ( \delta \rho / \delta t ) / c )$ , and it is evident that this frequency depends on the range-rate. In other words, Eq. (3.3.25) illustrates the Doppler effect. If the relative motion between the transmitter and receiver is positive (the two are moving apart), then $f _ { T } - f _ { R }$ is less than $f _ { T }$ ; that is, the apparent frequency of the transmitter beacon is lower than the actual frequency. But if the relative motion is negative, the apparent frequency of the transmitter beacon is higher than $f _ { T }$ . These results are consistent with those in the preceding section for the repeated pulse transmission, as they should be since both cases are based on the Doppler effect. An important element of the preceding discussion is the fact that instantaneous range-rate cannot be measured. Instead, the measured quantity $( N _ { 1 , 2 } )$ is related to the range change $( \delta \rho )$ in a specified interval of time $( \delta t )$ . Depending on the realization of the previously described concept, the instrument design may measure $N _ { 1 , 2 }$ by allowing the zero crossings of $\left( f _ { G } - f _ { T } \right)$ to increment a counter, thereby generating an integer count, or Doppler count. In some designs, the counter may reset at the end of the count interval $\left( t _ { R _ { 2 } } \right.$ in the previous discussion), or it may simply record the content of the counter at the interval end. In the continuous count case, the count is made with respect to some interval when the signal from the transmitter first appeared, where the start count may be nonzero.

Another interpretation of $N _ { 1 , 2 }$ can be obtained by rearranging the terms in Eq. (3.3.23) to give

$$
\rho _ { 2 } = \rho _ { 1 } + N _ { 1 , 2 } ~ c / f _ { G } - c / f _ { G } ( f _ { G } - f _ { T } ) ( t _ { T _ { 2 } } - t _ { T _ { 1 } } ) ,
$$

which suggests that a range measurement can be formed from the measured $N _ { 1 , 2 }$ . In this representation, $\rho _ { 1 }$ is not known so $\rho _ { 2 }$ can be regarded to be a biased range, similar to the previously described pseudorange. If $t _ { 2 }$ is any time after $t _ { 1 }$ , Eq. (3.3.26) demonstrates that $N _ { 1 , 2 }$ exhibits a range-like variation with time. For these applications, $N _ { 1 , 2 }$ is usually the accumulated integer cycles plus the fractional part of the cycle. Although the fractional part is the phase, the term is commonly used to describe the sum of the integer cycles plus the fractional part. In the case when $f _ { G } = f _ { T }$ , it follows that Eq. (3.3.26) can be written as

$$
\rho _ { 2 } = \rho _ { 1 } + \tilde { \rho } _ { { } _ { P H } }
$$

where $\tilde { \rho } _ { { } _ { P H } } = \lambda N _ { 1 , 2 }$ , $\lambda = c / f _ { T }$ , the signal wavelength. The quantity $\tilde { \rho } _ { { } _ { P H } }$ is a pseudorange formed from the phase, phase pseudorange.

# 3.4 REALIZATION OF MEASUREMENTS

# 3.4.1 CONSIDERATIONS

The preceding section provided a conceptual discussion of the commonly used observations with little consideration given to the actual instrumentation applied to the realization of those observations. Although the discussion referred to the transmission of signals, the characteristics of those signals and the effects of the atmosphere were not treated. All signals are transmitted using a region of the electromagnetic spectrum, spanning from radio frequencies to visible regions of the spectrum. The commonly used regions of the spectrum are identified using terminology established during the 1940s global conflict and are shown in Table 3.4.1. Depending on their frequency, the signals will be influenced differently by the atmosphere, as discussed in the next section. Current technologies used in orbit determination are summarized in the following sections.

# 3.4.2 ATMOSPHERIC EFFECTS

Measurements used for orbit determination that propagate through the Earth’s atmosphere will experience refractive effects. These effects delay the signals and, for example, lengthen the apparent range. Account must be taken of these delays in most cases, though the overall effect is unimportant in cases with coarse accuracy requirements (e.g., km-level). Since the atmosphere consists of distinctive layers, the propagation effects can be discussed within the context of the two most influentia l layers: troposphere and ionosphere.

Table 3.4.1: Electromagnetic Spectrum Regions for Satellite Transmissions   

<table><tr><td>Band Category</td><td>Approx. Frequency Range (MHz)</td><td>Wavelength Range (approx. cm)</td></tr><tr><td>L-Band</td><td>1000-2000</td><td>30-15</td></tr><tr><td>S-Ba nd</td><td>2000-4000</td><td>15-.5</td></tr><tr><td>C-Ba nd</td><td>4000-8000</td><td>7.5-3.75</td></tr><tr><td>X-Band</td><td>8000-12500</td><td>3.75-2.4</td></tr><tr><td>K-Band</td><td>12500-40000</td><td>2.4-0.75</td></tr><tr><td>Infrared</td><td>3 ×108</td><td>0.00010</td></tr><tr><td>Green</td><td>5.6 × 108</td><td>0.0000532</td></tr></table>

(Skolnik, 1990)

# Troposphere

The troposphere, which extends from the surface to about $1 0 \mathrm { k m }$ , is the region of the atmosphere where most meteorological effects that influence the surface take place. A transition region known as the tropopause lies between the troposphere and the next layer, the stratosphere. The dominant refractive contributions from these regions are associated with the troposphere, so the effect is referred to as the tropospheric delay, even though the stratosphere accounts for about $2 0 \%$ of the total. For radio frequencies, the troposphere and stratosphere are electrically neutral, or a nondispersive medium. The propagation delay, $\delta \rho$ , is

$$
\delta \rho = 1 0 ^ { - 6 } \int N d s
$$

where $d s$ is a differential length along the path, $N$ is the refractivity

$$
N = ( n - 1 ) 1 0 ^ { 6 }
$$

and $n$ is the index of refraction. The refractivity is usually written as the sum of the two components

$$
N = N _ { \mathrm { d } } + N _ { \mathrm { w } }
$$

where the subscripts denote dry (d) and wet (w) components. The dry component, or hydrostatic component, accounts for about $9 0 \%$ of the total effect. It assumes the atmosphere behaves consistently with the ideal gas law and that it is in hydrostatic equilibrium so that only the surface pressure needs to be known. Modeling of the wet component is more difficult because of variability in the partial water vapor pressure, so this correction is estimated from the tracking data or may be obtained from other instrumentation, such as water vapor radiometers. A commonly applied expression for frequencies less than about $3 0 \ : \mathrm { G H z }$ was given by Smith and Weintraub (1953)

$$
\begin{array} { c c l } { N _ { \mathrm { d } } } & { = } & { 7 7 . 6 ( P / T ) } \\ { N _ { \mathrm { w } } } & { = } & { 3 . 7 3 \times 1 0 ^ { 5 } ( \tilde { e } / T ^ { 2 } ) } \end{array}
$$

where $P$ is pressure in millibars $\mathrm { ( m b ) }$ ), $T$ is temperature in degrees Kelvin, and partial water vapor pressure, $\tilde { e }$ , is in mb, all measured at the surface. Evaluation of Eq. (3.4.1) has been treated by Saastamoinen (1972).

In the zenith direction, the tropospheric delay is about 2 meters at sea level, but the effect is dependent on the elevation angle of the viewing direction through the atmosphere. For example, at $1 0 ^ { \circ }$ elevation, the delay is about 12 meters. Mapping functions are usually adopted to map the zenith effect to any elevation angle. These mapping functions are fundamentally dependent on the cosecant of the elevation angle, but the complexity of the mapping functions varies.

Various methods are used to generate the propagation delay, including raytracing. The signal delay is predominantly dependent on the cosecant of the satellite elevation seen at the station. A frequently used expression for the tropospheric delay, $\Delta \rho _ { t }$ , is

$$
\Delta \rho _ { t } ( E l ) = \tau _ { d } m _ { d } ( E l ) + \tau _ { w } m _ { w } ( E l )
$$

where $\tau$ represents the zenith delay, $m ( E l )$ represents a mapping function with elevation dependency and the subscript $d$ is the dry component and $w$ is the wet component. The simplest mapping function is

$$
m ( E l ) = 1 / ( \sin ( E l ) ) .
$$

For optical wavelengths, such as those used with lasers, the troposphere behaves dispersively. As a consequence, the delay is dependent on the wavelength of the signal. For laser ranging systems, a commonly used correction for troposphere delay is given by Marini and Murray (1973):

$$
\Delta \rho _ { t } = \frac { f ( \lambda ) } { f ( \phi , H ) } \frac { A + B } { \sin ( E l ) + \frac { B / ( A + B ) } { \sin ( E l ) + 0 . 0 1 } }
$$

where

$$
\begin{array} { r c l } { A } & { = } & { 0 . 0 0 2 3 5 7 P _ { 0 } + 0 . 0 0 0 1 4 1 e _ { 0 } } \end{array}
$$

$$
\begin{array} { r c l } { { \cal B } } & { { = } } & { { ( 1 . 0 8 4 \times 1 0 ^ { - 8 } ) P _ { 0 } T _ { 0 } K + ( 4 . 7 3 4 \times 1 0 ^ { - 8 } ) \frac { P _ { 0 } ^ { 2 } } { T _ { 0 } } ~ \frac { 2 } { ( 3 - 1 / K ) } } } \\ { { f ( \phi , H ) } } & { { = } } & { { 1 - 0 . 0 0 2 6 \cos 2 \phi - 0 . 0 0 0 3 1 H } } \\ { { K } } & { { = } } & { { 1 . 1 6 3 - 0 . 0 0 9 6 8 \cos ( 2 \phi ) - 0 . 0 0 1 0 4 T _ { 0 } + 0 . 0 0 0 0 1 4 3 5 P _ { 0 } } } \\ { { e _ { 0 } } } & { { = } } & { { \displaystyle \frac { R _ { h } } { 1 0 0 } \times 6 . 1 1 \times 1 0 ^ { a } } } \\ { { a } } & { { = } } & { { \displaystyle \frac { 7 . 5 ( T _ { 0 } - 2 7 3 . 1 5 ) } { 2 3 7 . 3 + ( T _ { 0 } - 2 7 3 . 1 5 ) } . } } \end{array}
$$

$E l$ is the true elevation, $P _ { 0 }$ is the atmospheric pressure at the laser site $\mathrm { ( m b ) }$ ), $T _ { 0 }$ is the atmospheric temperature at the laser site (degrees Kelvin), $e _ { 0 }$ is the water vapor pressure at the site (millibars), $R _ { h }$ is relative humidity $( \% )$ , $\phi$ is the site geodetic latitude, and $H$ is the height of the site above the ellipsoid (km). Note that $f ( \lambda )$ is

$$
f ( \lambda ) = 0 . 9 6 5 0 + { \frac { 0 . 0 1 6 4 } { \lambda ^ { 2 } } } + { \frac { 0 . 0 0 0 2 2 8 } { \lambda ^ { 4 } } }
$$

where $\lambda$ is the laser wavelength in microns. For example, a ruby laser has a wavelength of 0.6943 microns and $f ( \lambda )$ is 1.0000, whereas a green laser $\lambda =$ 0.532 microns) has $f ( \lambda ) = 1 . 0 2 5 7 9$ . At optical wavelengths, the wet component is small and usually ignored.

Other mapping functions have been developed for radio frequency measurements. For example, the MIT Thermospheric mapping function, known as MTT, has close functional similarity to the Marini-Murray function (Herring et al., 1992):

$$
m ( E l ) = \frac { 1 + \frac { a } { 1 + \frac { b } { 1 + c } } } { \sin ( E l ) + \frac { a } { \sin ( E l ) + \frac { b } { \sin ( E l ) + \frac { b } { \sin ( E l ) + \frac { b } { \sin ( E l ) + c } } } } }
$$

where the coefficients for the dry part, $m _ { d }$ , are

$$
\begin{array} { l l l } { a } & { = } & { [ 1 . 2 3 2 0 + 0 . 0 1 3 0 \cos \phi - 0 . 0 2 0 9 H _ { s } } \\ & & { + 0 . 0 0 2 1 5 ( T _ { s } - T _ { 0 } ) ] \times 1 0 ^ { - 3 } } \\ { b } & { = } & { [ 3 . 1 6 1 2 - 0 . 1 6 0 0 \cos \phi - 0 . 0 3 3 1 H _ { s } } \\ & & { + 0 . 0 0 2 0 6 ( T _ { s } - T _ { 0 } ) ] \times 1 0 ^ { - 3 } } \\ { c } & { = } & { [ 7 1 . 2 4 4 - 4 . 2 9 3 \cos \phi - 0 . 1 4 9 H _ { s } } \\ & & { - 0 . 0 0 2 1 ( T _ { s } - T _ { 0 } ) ] \times 1 0 ^ { - 3 } } \end{array}
$$

where $T _ { s }$ is surface temperature in $^ \circ \mathrm { C }$ , $T _ { 0 } = 1 0 ^ { \circ } \mathrm { C }$ , $\phi$ is the site geodetic latitude, and $H _ { s }$ is the height of the site above the reference ellipsoid. The coeffici ents for the wet part, $m _ { w }$ , are

$$
\begin{array} { l c l } { { a } } & { { = } } & { { [ 0 . 5 8 3 - 0 . 0 1 1 \cos \phi - 0 . 0 5 2 H _ { s } } } \\ { { } } & { { } } & { { + 0 . 0 0 1 4 ( T _ { s } - T _ { 0 } ) ] \times 1 0 ^ { - 3 } } } \\ { { b } } & { { = } } & { { [ 1 . 4 0 2 + 0 . 1 0 2 \cos \phi - 0 . 1 0 1 H _ { s } } } \\ { { } } & { { } } & { { + 0 . 0 0 2 0 ( T _ { s } - T _ { 0 } ) ] \times 1 0 ^ { - 3 } } } \\ { { c } } & { { = } } & { { [ 4 5 . 8 5 - 1 . 9 1 \cos \phi - 1 . 2 9 H _ { s } } } \\ { { } } & { { } } & { { + 0 . 0 1 5 ( T _ { s } - T _ { 0 } ) ] \times 1 0 ^ { - 3 } } } \end{array}
$$

In very high-accuracy cases, azimuthal dependencies should be accounted for in the mapping function or measured with water vapor radiometers.

# Ionosphere

The ionosphere is the portion of the atmosphere that is characterized by the presence of ions and free electrons. The ionosphere is most distinctive at altitudes above $8 0 ~ \mathrm { k m }$ and consists of several layers, but not all of the layers are completely distinct. The ionosphere has no significant effect on signals with optical wavelengths (e.g., lasers). For radio frequencies, the ionosphere is dispersive and the signal time delay is dependent on the frequency, as well as the electron content along the signal path. Thus, the time delay $\delta t$ at a frequency $f$ is, to order $1 / f ^ { 3 }$ ,

$$
\delta t = \frac { \alpha } { f ^ { 2 } }
$$

where $\alpha$ is related to the TEC (total electron content) along the path. The term $\alpha$ is positive for group delays (e.g., pseudorange) and negative for carrier phase. Since the ionospheric delay is dependent on frequency, transmission of signals at different frequencies allows removal of the ionosphere, at least to an acceptable level for orbit determination applications. Given a ranging code transmitted at two different frequencies, $f _ { 1 }$ and $f _ { 2 }$ , this equation can be used to eliminate the TEC and obtain an ionosphere-free range, $\rho _ { c }$ . Using the linear combination of range measurements made with $f _ { 1 }$ and $f _ { 2 } , \rho _ { c }$ can be shown to be

$$
\rho _ { c } = \gamma _ { 1 } \rho _ { 1 } - \gamma _ { 2 } \rho _ { 2 }
$$

where $\rho _ { 1 }$ is the range measurement from $f _ { 1 }$ and $\rho _ { 2 }$ is the measurement from $f _ { 2 }$ , and

$$
\begin{array} { r l r } { \gamma _ { 1 } } & { = } & { \displaystyle \frac { f _ { 1 } ^ { 2 } } { f _ { 1 } ^ { 2 } - f _ { 2 } ^ { 2 } } } \\ { \gamma _ { 2 } } & { = } & { \displaystyle \frac { f _ { 2 } ^ { 2 } } { f _ { 1 } ^ { 2 } - f _ { 2 } ^ { 2 } } . } \end{array}
$$

Significant changes in total electron content take place both spatially and temporally. Predictive ionosphere models may be used to correct single-frequency ranging data, but the highest accuracy is achieved with dual-frequency measurements. For measurement systems that operate in the L-band of the frequency spectrum (e.g., GPS with $f _ { 1 } ~ = ~ 1 5 7 5 . 4 2 ~ \mathrm { M H z }$ and $f _ { 2 } \ = \ 1 2 2 7 . 6 0 ~ \mathrm { M H z } )$ , the ionosphere delay can be meter-level to tens of meters, depending on the TEC. Although the linear combination increases the measurement noise compared to the single-frequency measurement, the removal of the systematic effects associated with ionospheric variability is essential for high-accuracy applications. Appropriate estimation techniques can aid in smoothing the increased measurement noise produced by the linear combination.

# 3.4.3 GENERAL RELATIVITY

As noted in Chapter 2, an Earth orbiter experiences a small relativistic precession of the perigee. In this section, the relativistic effects associated with various measurements (e.g., range or time delay) are described. These effects include the constancy of the speed of light, time dilation, gravitational frequency shifts, and the Sagnac effect. Further details for GPS are given by Ashby (2002).

Depending on the altitude, a clock (oscillator) in a circular orbit may beat fractionally faster or slower than a clock with identical characteristics on the surface of the Earth. This effect applies to systems such as GPS, Transit, and DORIS. In the case of GPS, this relativistic effect is usually accounted for by slightly lowering the satellite oscillator frequency to 10.229999999543 MHz to achieve the effective frequency of $1 0 . 2 3 ~ \mathrm { M H z }$ when the satellite is in orbit. It is evident that this effect does not apply to passive satellites, such as Lageos, with no on-board oscillators.

If the clock’s orbit is not perfectly circular, the clock will vary about the mean frequency with the same period as the orbit. For a GPS satellite with an orbital eccentricity of 0.01, for example, this could lead to a navigation error of up to 7 m. The correction to the time offset is easily calculated from knowledge of the GPS satellite position and velocity from

$$
\Delta t _ { r } = { \frac { 2 \mathbf { r } \cdot \mathbf { v } } { c ^ { 2 } } } .
$$

In a system of several massive bodies, the gravitational fiel ds of these bodies will influence the arrival time of a signal traveling at the speed of light from a source. For Earth orbiters, a nonrotating inertial reference system tied to the center of mass of the Earth usually is used, and the relativistic effect of the Earth’s mass is the only contributor. If the signal is transmitted from a position at a distance $r _ { 1 }$ from the geocenter and received at a position that is a distance $r _ { 2 }$ , and $\rho$ is the distance between transmitter and receiver, then the relativistic correction to the

time delay caused by the Earth is:

$$
\Delta t _ { \mathrm { d e l a y } } = { \frac { 2 G M } { c ^ { 3 } } } \ln \left[ { \frac { r _ { 1 } + r _ { 2 } + \rho } { r _ { 1 } + r _ { 2 } - \rho } } \right] .
$$

For low-altitude Earth satellites, the contribution from other celestial bodies is negligible. In the case of GPS, this correction is a few $\mathrm { c m }$ , but the effect mostly cancels in differenced measurements (see Section 3.6).

An additional relativistic effect is known as the Sagnac effect. When working in the ECI frame, the Sagnac effect is not applicable; the iteration to calculate the light-time accounts for the motion of the receiver clock during the time of propagation. The Sagnac effect is generally a concern only for high-precision time transfer between ground-based clocks via a satellite. Ries et al. (1991) describe the relativistic effects for orbit determination.

# 3.5 MEASUREMENT SYSTEMS

# 3.5.1 ONE-WAY RANGE

# GPS

The basic concept of a one-way range was described in Section 3.3.1. As noted in that description, the one-way range is based on the time required for a signal to travel from a transmitter to a receiver. The wide use of GPS makes it a suitable example of the one-way ranging technique. Further details of GPS are given by Hofmann-Wellenhof et al. (1997) and Leick (2003).

The GPS consists of a constellation of satellites, developed by the U.S. Department of Defense. Each satellite broadcasts signals to support one-way ranging at radio frequencies using the following basic elements: a radio transmitter, a computer, a frequency standard (provides both time and frequency reference for radio transmissions), a transmit antenna, and a power source. The characteristics of the constellation in January 2000 are summarized in Table 3.5.1. The GPS satellites are organized into six orbit planes $( i = 5 5 ^ { \circ }$ ) with four or five satellites in each plane. Each satellite has an orbital period of 11 hours 58 minutes.

All GPS satellites use the same frequencies in the L-band: $1 5 7 5 . 4 2 ~ \mathrm { M H z }$ (known as $L _ { 1 }$ ) and 1227.60 (known as $L _ { 2 }$ ). These frequencies are termed the carrier frequencies, which are $1 5 4 ~ f _ { 0 }$ and $1 2 0 ~ f _ { 0 }$ , where $f _ { 0 } = 1 0 . 2 3 ~ \mathrm { M H z }$ , the GPS fundamental frequency. A third civil frequency (known as $L _ { 5 }$ at 1176.45 MHz) is being planned for future GPS satellites starting with Block IIF. A thorough discussion of the GPS signals can be found in Parkinson et al. (1996).

Table 3.5.1 GPSConstellationStatus:1January 200o00:00:00.0o0GPS-Time   

<table><tr><td rowspan="2">Orb./Plane &amp;Position</td><td colspan="3">S/C</td><td rowspan="2">a</td><td rowspan="2">e</td><td rowspan="2">i (deg.）</td><td rowspan="2">Ω</td><td rowspan="2">W (deg.）</td><td rowspan="2">w+M (deg.）</td><td colspan="2">AN(deg.)</td></tr><tr><td>PRN</td><td>type Clock</td><td>(km)</td><td>(deg.)</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>A-1</td><td>09</td><td>IIA</td><td>Cs</td><td>26559.3</td><td>0.0098</td><td>54.0</td><td>175.7</td><td>32.3</td><td>103.0</td><td>127.0</td><td>-53.0</td></tr><tr><td>A-2</td><td>25</td><td>IIA</td><td>Cs</td><td>26561.7</td><td>0.0078</td><td>53.6</td><td>173.5</td><td>232.9</td><td>356.0</td><td>71.9</td><td>-108.1</td></tr><tr><td>A-3</td><td>27</td><td>IIA</td><td>Cs</td><td>26559.9</td><td>0.0137</td><td>53.9</td><td>174.7</td><td>198.3</td><td>212.2</td><td>1.1</td><td>-178.9</td></tr><tr><td>A-4</td><td>19</td><td>II</td><td>Rb</td><td>26560.0</td><td>0.0053</td><td>53.1</td><td>172.4</td><td>203.6</td><td>238.8</td><td>12.0</td><td>-168.0</td></tr><tr><td>A-5</td><td>08</td><td>IIA</td><td>Rb</td><td>26539.7</td><td>0.0086</td><td>54.8</td><td>178.2</td><td>102.1</td><td>148.2</td><td>152.2</td><td>-28.0</td></tr><tr><td>B-1</td><td>22</td><td>IIA</td><td>Rb</td><td>26559.9</td><td>0.0129</td><td>53.5</td><td>233.7</td><td>30.5</td><td>278.4</td><td>92.6</td><td>-87.4</td></tr><tr><td>B-2</td><td>30</td><td>IIA</td><td>Cs</td><td>26562.8</td><td>0.0056</td><td>54.1</td><td>235.7</td><td>83.8</td><td>3.5</td><td>137.2</td><td>-42.8</td></tr><tr><td>B-3</td><td>02</td><td>II</td><td>Cs</td><td>26561.3</td><td>0.0194</td><td>53.6</td><td>232.9</td><td>236.7</td><td>140.7</td><td>24.3</td><td>-155.7</td></tr><tr><td>B-4</td><td>05</td><td>IIA</td><td>Cs</td><td>26562.0</td><td>0.0019</td><td>53.7</td><td>234.0</td><td>9.5</td><td>38.6</td><td>153.3</td><td>-26.7</td></tr><tr><td>C-1</td><td>06</td><td>IIA</td><td>Cs</td><td>26558.9</td><td>0.0068</td><td>54.5</td><td>297.2</td><td>222.1</td><td>306.4</td><td>170.8</td><td>-9.2</td></tr><tr><td>C-2</td><td>03</td><td>IIA</td><td>Cs</td><td>26561.2</td><td>0.0010</td><td>54.1</td><td>294.8</td><td>72.8</td><td>207.5</td><td>118.6</td><td>-61.4</td></tr><tr><td>C-3</td><td>31</td><td>IIA</td><td>Cs</td><td>26561.7</td><td>0.0092</td><td>54.6</td><td>295.4</td><td>45.7</td><td>175.0</td><td>102.7</td><td>-77.3</td></tr><tr><td>C-4</td><td>07</td><td>IIA</td><td>Cs</td><td>26559.5</td><td>0.0109</td><td>54.6</td><td>295.4</td><td>239.7</td><td>75.1</td><td>53.6</td><td>-126.4</td></tr><tr><td>D-1</td><td>24</td><td>IIA</td><td>Rb</td><td>26561.1</td><td>0.0090</td><td>56.5</td><td>358.4</td><td>261.4</td><td>325.4</td><td>61.7</td><td>-118.3</td></tr><tr><td>D-2</td><td>15</td><td>II</td><td>Cs</td><td>26555.5</td><td>0.0073</td><td>56.3</td><td>0.2</td><td>85.8</td><td>118.6</td><td>139.2</td><td>-40.7</td></tr><tr><td>D-3</td><td>17</td><td>II</td><td>Cs</td><td>26558.9</td><td>0.0113</td><td>56.4</td><td>2.5</td><td>167.5</td><td>224.5</td><td>14.7</td><td>-165.3</td></tr><tr><td>D-4</td><td>04</td><td>IIA</td><td>Rb</td><td>26562.0</td><td>0.0053</td><td>56.0</td><td>357.8</td><td>323.0</td><td>0.5</td><td>78.4</td><td>-101.6</td></tr><tr><td>D-5</td><td>11</td><td>IIR</td><td>Cs</td><td>26559.3</td><td>0.0029</td><td>53.0</td><td>355.2</td><td>189.8</td><td>101.0</td><td>125.8</td><td>-54.2</td></tr><tr><td>E-1</td><td>14</td><td>II</td><td>Cs</td><td>26562.4</td><td>0.0005</td><td>56.1</td><td>59.3</td><td>129.5</td><td>31.4</td><td>155.0</td><td>-25.0</td></tr><tr><td>E-2</td><td>21</td><td>II</td><td>Cs</td><td>26559.9</td><td>0.0160</td><td>55.7</td><td>56.9</td><td>211.5</td><td>130.0</td><td>22.5</td><td>-157.5</td></tr><tr><td>E-3</td><td>10</td><td>IIA</td><td>Cs</td><td>26557.3</td><td>0.0038</td><td>55.8</td><td>56.5</td><td>353.0</td><td>256.6</td><td>84.7</td><td>-95.3</td></tr><tr><td>E-4</td><td>23</td><td>IIA</td><td>Cs</td><td>26562.3</td><td>0.0145</td><td>55.9</td><td>59.2</td><td>249.3</td><td>163.6</td><td>41.8</td><td>-138.2</td></tr><tr><td>E-5</td><td>16</td><td>II</td><td>Cs</td><td>26562.3</td><td>0.0044</td><td>55.9</td><td>59.5</td><td>19.6</td><td>355.5</td><td>137.2</td><td>-42.8</td></tr><tr><td>F-1</td><td>01</td><td>IIA</td><td>Cs</td><td>26568.4</td><td>0.0048</td><td>55.0</td><td>117.9</td><td>258.8</td><td>335.0</td><td>5.7</td><td>-174.4</td></tr><tr><td>F-2</td><td>26</td><td>IIA</td><td>Rb</td><td>26562.3</td><td>0.0116</td><td>55.2</td><td>116.9</td><td>2.1</td><td>180.0</td><td>106.9</td><td>-73.1</td></tr><tr><td>F-3</td><td>18</td><td>II</td><td>Cs</td><td>26559.2</td><td>0.0076</td><td>54.4</td><td>114.0</td><td>107.0</td><td>117.9</td><td>162.7</td><td>-17.4</td></tr><tr><td>F-4</td><td>29</td><td>IIA</td><td>Rb</td><td>26558.6</td><td>0.0073</td><td>55.0</td><td>115.3</td><td>248.2</td><td>81.0</td><td>56.3</td><td>-123.7</td></tr><tr><td>F-5</td><td>13</td><td>IIR</td><td>Rb</td><td>26558.7</td><td>0.0022</td><td>55.2</td><td>116.5</td><td>322.6</td><td>244.1</td><td>138.7</td><td>-41.3</td></tr></table>

Theosculating orbit elements are expressed in J20，PRN is the GPS identifer，Cs denotes cesium andRbis rubidium,S/CTypeidentifiesthesatelitedesigntype,and $\lambda _ { \mathrm { A N } }$ islongitude of the ascending node.

The discussion in this section also applies to the current Russian navigation satellite system, known as GLONASS (Global Navigation Satellite System) and the future European Space Agency GALILEO (planned for operation by 2008).

Both satellite constellations use three orbital planes with about 10 satellites (including spares) in each plane (GALILEO). The GLONASS satellites use a $6 3 ^ { \circ }$ inclination and orbit periods of 11 hours 15 minutes. GALILEO satellites are expected to use a $5 6 ^ { \circ }$ inclination with an orbit period of 14 hours 22 minutes. Each GLONASS satellite broadcasts on a different frequency in the L-band, but GALILEO will have broadcast characteristics similar to GPS.

A Block II GPS satellite is illustrated in Fig. 3.5.1. The transmit antenna is the array shown on the main body of the spacecraft with the helical windings. The large panels on both sides are the solar panels used to generate power. Each satellite carries standard quartz frequency standards, as well as multiple atomic frequency standards (two cesium and two rubidium). In fact, a tunable quartz standard is used to excite the cesium standard, for example, at the natural frequency of $9 , 1 9 2 , 6 3 1 , 7 7 0 ~ \mathrm { H z }$ . It is this frequency that, in fact, defines the SI second.

The carrier frequencies are derived from the frequency standard in use (cesium, rubidium, or quartz), but additional information is superimposed. A simple analogy can be drawn with a common radio where a carrier frequency is used (e.g., ${ 1 0 0 } \mathrm { M H z }$ ) to carry the audio $( < 2 0 , 0 0 0 \mathrm { H z } )$ . In this example, the transmitter superimposes audio on the carrier, and the receiver extracts the audio signal when the radio is properly tuned to the carrier frequency. In the case of GPS (or GLONASS), the information superimposed on the carrier includes ranging codes and other data necessary to perform the navigation function offered by the satellite constellation.

GPS uses several ranging codes, though they have many similarities. In concept, the ranging codes are generated as pseudo-random noise (PRN). Consider the PRN code to be a series of binary digits (bits)—001101011100—for example, superimposed on the carrier. Each bit, known in GPS terminology as a chip, has a specific time duration depending on the code. The PRN bit sequence is determined by a documented algorithm. Each bit in the sequence will be transmitted by the satellite at a specific time determined by the satellite clock (which is derived from the frequency standard). Hence, as the receiver extracts the bit sequence from the carrier, it will assign receive times to each bit based on its own clock. With the ability to replicate the PRN code, the receiver will cross-correlate, or align, the received bit sequence with the sequence it is able to generate. Since each bit has a known transmit time, the difference between receive time and transmit time is obtained by this cross-correlation; that is, the quantity $t _ { R } - t _ { T }$ in Eq. (3.3.1) is determined, as well as the individual times, $t _ { R }$ and $t _ { T }$ . Note that the time when each bit in the code is transmitted is determined by the satellite clock, so the time $t _ { T }$ is based on the satellite clock. Similarly, the time when the bit is received, $t _ { R }$ , is determined by the clock in the receiver.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0002_pages_0071-0140/auto/images/f04dced259776fa4a516bc7fd41f8bc464c2d07e3ea340befbf656b31a0eeb59.jpg)  
Figure 3.5.1: Block II GPS satellite. The satellite solar panels rotate about the axis mounted perpendicular to the main body (spacecraft bus) and the transmit antenna array, shown with the helical windings in the center, is directed toward the Earth’s center. The antenna transmit pattern encompasses the visible Earth. A body-fix ed set of axes includes a $y$ axis coincident with the solar panel axes and a $z$ axis directed toward the Earth’s center. The spacecraft can present the maximum cross-sectional area of the solar panels to the Sun by rotating the bus about the $z$ axis (yaw) and rotating the solar panels about the $y$ axis.

The PRN codes currently transmitted by the GPS satellites are:

• C/A (Coarse Acquisition): This code uses 1023 bits and repeats every 1 ms. The algorithm for generating the sequence is described in detail by Hofmann-Wellenhof et al. (1997). Each bit requires about 1 microsec for transmission or about 300 meters in distance. One major purpose of this code is to facilitate acquisition of the P-code, which is a much longer bit sequence. Since the C/A code repeats every millisecond, an ambiguity exists between each millisecond interval. In other words, there is no information about absolute time within the C/A code. Resolving this ambiguity to determine the correct time interval requires additional information (e.g., information broadcast by the GPS satellites about their position).

• P (Precise): This code has a much longer duration of 37 weeks before it repeats. But this long repeat interval is divided into one week segments and each segment is assigned to a specific GPS satellite. Each satellite, in turn, repeats its assigned code each week. The duration for each bit is the equivalent of 30 meters in distance, corresponding to a transmission rate of $1 0 . 2 3 \times 1 0 ^ { 6 }$ bits per sec. All information about the P-code is readily available. Most receivers use the C/A code for initial acquisition, then transition to the P-code. Since the P-code within each satellite does not repeat for one week, direct cross-correlation without use of the C/A code is challenging. Direct P-code acquisition is easier if the receiver has an accurate clock.

• Y: This code is generated from the P-code, but a classified code (W-code) is used to mix with the P-code. This mixing produces an encrypted P-code. When the Y-code is being transmitted, it is said that Anti-Spoofing (AS) has been invoked. The terminology arises from the military consideration that an adversary could transmit false P-code signals to confuse, or spoof, a receiver. When AS is used, the classified Y-code avoids this possibility.

In the GPS satellites known as Block II, including Block IIA and Block IIR, the $\mathrm { C } / \mathrm { A }$ code is transmitted only on $L _ { 1 }$ and the P/Y codes are transmitted on both $L _ { 1 }$ and $L _ { 2 }$ . As a consequence, receivers capable of operating with only C/A are single-frequency receivers. Without the second frequency, the ionosphere correction cannot be made as accurately as measurements obtained with two frequencies, since it must rely on less accurate ionosphere models. Modern dualfrequency receivers are available that may be capable of correlating directly with the Y-code or they may use signal processing techniques, such as cross-correlation of the Y-code on the two frequencies to obtain the ionosphere delay. The method based on advanced signal processing effectively provides a dual-frequency measurement without knowledge of the Y-code. A pseudo-measurement usually is created by adding the measured ionosphere delay to the C/A pseudorange.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0002_pages_0071-0140/auto/images/219f5f8760d6d4a9606583b3290c918faf0b628b345a6bf8639209d2c16acb3e.jpg)  
Figure 3.5.2: Typical GPS antenna setup. A choke-ring antenna is shown on the left and the antenna set up with a tripod over a geodetic marker is shown on the right. The height of the antenna reference point (ARP) above the geodetic marker is usually made to high accuracy with a geodetic-quality graduated ruler. The antenna phase center locations, denoted by L1 and L2, are separately calibrated.

A typical GPS receiver antenna installation is shown in Fig. 3.5.2, which shows a choke-ring antenna on the left. The choke ring is designed to reduce the effects of multipath, a phenomenon that occurs when the incoming GPS signal is reflected from nearby objects, such as buildings for a ground receiver. The reflected signal travels a longer path to the antenna, thereby introducing another error source into the measured signal. The choke-ring antenna is used for both ground-based and space-borne installations.

The relationship between the measured ranges and the satellite state requires the specific ation, or estimation, of the receiver antenna location. For precision orbit determination, the coordinates of the antenna shown in Fig. 3.5.2 must be known or determined in an appropriate reference frame. Furthermore, the reference point to which those coordinates refer and the specific point to which the range measurements are made are required. The antenna usually is described with a phase center, the point to which range measurements refer. This phase center usually is obtained by empirical testing, including testing in anechoic chambers. Such testing determines the phase center pattern for a particular antenna. Experience has shown that such patterns are common to a particular antenna type so that the test results of a subset may be applied to other nontested antennas.

For some antennas, the phase center pattern may be azimuthally symmetric, but may exhibit change as a function of elevation. For precision applications, the characteristics of the phase center variation must be known, as well as the location of the phase center even if it is invariant. Furthermore, in some cases, the coordinates published for a particular antenna may refer to a specific point other than the phase center, usually referred to as the antenna reference point (ARP). In these cases, the correction to the phase center must be separately applied. It is important that the specific point where a priori coordinates for the antenna should be applied is understood. To further complicate matters, the phase center for $L _ { 1 }$ is usually different from the location for $L _ { 2 }$ . As shown in Fig. 3.5.2, the location for the $L _ { 1 }$ phase center is $\delta _ { 1 }$ with respect to the ARP and the location of the $L _ { 2 }$ phase center is $\delta _ { 2 }$ .

The precision of GPS pseudorange measurements is receiver dependent, but most modern receivers are at the level of about 1 meter for P-code pseudorange. Note that the combination of two measurements made at different frequencies to remove ionosphere effects will produce a noisier measurement (Eq. 3.4.14). Although the precision of the pseudorange is meter level, the accuracy of the measurement is usually not comparable. For example, pseudorange measurements may be negative because of unsynchronized clocks, a clear indication that a measurement may be precise, but not accurate. Nevertheless, the correction for clock errors can be determined through appropriate estimation strategies and the corrections obtained from them will render the measurement accurate, as well as precise. As a means to control the accuracy of pseudorange measurements, the GPS satellite clocks may be dithered. This dithering produces clock errors that cannot be accounted for without access to Department of Defense classified information. When clock dithering is activated, it is said that Selective Availability (SA) has been invoked. Unclassified techniques to remove SA will be described in Section 3.6, but SA was deactivated in May, 2000.

The pseudorange measurement given by Eq. (3.3.9) can be expanded for either $L _ { 1 }$ or $L _ { 2 }$ to give

$$
\tilde { \rho } = \rho + c ( \delta t _ { R } - \delta t _ { T } ) + \delta \rho _ { \mathrm { t r o p } } + \delta \rho _ { \mathrm { i o n } } + \epsilon
$$

where

$\tilde { \rho }$ is the measured pseudorange,

$\rho$ is the true range between the true transmit time and the true receive time, $\delta t _ { R }$ is the receiver clock difference with true time, $\delta t _ { T }$ is the transmitter clock difference with true time, $\delta \rho _ { \mathrm { t r o p } }$ is the troposphere delay, $\delta \rho _ { \mathrm { i o n } }$ is the ionosphere contribution, and $\epsilon$ represents remaining errors, such as instrument noise.

Computation of the true range, $\rho$ , would require knowledge of the true GPS satellite position and the true receiver antenna coordinates, as well as the true transmit and receive times. In practice, these quantities may not be known with high accuracy. In the orbit determination problem, for example, the satellite position may be known a priori with an accuracy of several meters. In this instance, the error term $\epsilon$ will represent the error between the true range and the computed range formed from the a priori known position. The receiver ability to measure pseudorange is characterized by the instrument’s precision, usually at the meter level.

A more precise GPS measurement is based on the carrier phase. With the previously described atmospheric effects, the usual form of the phase, expressed as range and similar to Eq. (3.5.1), can be obtained from Eq. (3.3.26). For either $L _ { 1 }$ or $L _ { 2 }$ , it can be shown that

$$
\Phi = \rho + c ( \delta t _ { R } - \delta t _ { T } ) + \lambda \widetilde { N } + \delta \rho _ { \mathrm { t r o p } } - \delta \rho _ { \mathrm { i o n } } + \epsilon
$$

where

$\Phi$ is the measured phase range for the specified frequency,

$\lambda$ is the wavelength of the signal $\scriptstyle { \mathrm { { L } } } _ { 1 }$ or $L _ { 2 }$ ),

$\widetilde N$ is the integer phase ambiguity,

and the other terms were defined with Eq. (3.5.1).

Note that the raw phase measurement, $\phi$ , provided by a receiver consists of the accumulated integer cycles since a reference time, plus the fractional part of a cycle. The measured phase range is

$$
\Phi = \lambda \phi
$$

but in some receivers the expression may require $\Phi = - \lambda \phi$ .

For comparison with pseudorange, the precision of phase range is usually characterized at the several millimeter level. If the GPS receiver is carried on a satellite, the term $\delta \rho _ { \mathrm { t r o p } }$ is zero and $\delta \rho _ { \mathrm { i o n } }$ may be sufficiently small to neglect. Even at $1 0 0 0 ~ \mathrm { k m }$ altitude, the ionosphere contribution is at the decimeter level. The phase range from $L _ { 1 }$ and $L _ { 2 }$ can be combined to remove the ionosphere contribution using the same approach applied to pseudorange (Hofmann-Wellenhof et al., 1997).

In applications of GPS measurements to the determination of an orbit of a low Earth orbiter (LEO), such as described in Section 3.7, the positions of the GPS satellites must be known or determined. One option is to apply the techniques of estimation described in the following chapters to the determination of the orbits of the GPS satellites using a network of ground stations. In some cases, the GPS satellite orbits may be determined simultaneously with the orbit of a LEO, but in others the GPS satellite orbits may be fix ed to orbits determined by other sources.

The GPS ephemerides can be recreated using information broadcast by the satellites in near real time. These broadcast ephemerides can be generated from 16 parameters (navigation message or ephemeris parameters) based on Keplerian orbit elements and coefficients of terms that represent time dependency (see Hofmann-Wellenhof et al., 1997) . The set of broadcast parameters applies to a specific interval of time, typically two hours, and new sets of parameters are broadcast automatically by a GPS satellite as the applicable time interval changes. The accuracy of the broadcast ephemerides generally is regarded to be at the 10-meter level. The primary intent is for the broadcast ephemerides to support real-time or near real-time applications. The information used to create the parameters broadcast by the GPS satellites is based on determination of the GPS satellite orbits by the Department of Defense using a set of six monitor stations. These monitor stations record pseudorange and carrier phase measurements between the ground-based receiver and the GPS satellite, which are then used to determine the orbits through a process that makes use of the methodologies in the following chapters. The orbits determined by this process are then extrapolated forward in time and the extrapolated ephemerides are approximated with a model based on the 16 ephemeris parameters. The ephemeris parameters are uploaded to the GPS satellites for broadcast during the appropriate time interval.

Precise GPS ephemerides are available with a latency of about one day or longer. These ephemerides are intended to support applications with high accuracy requirements, such as those related to space geodesy. Depending on the application, the position accuracy of a satellite carrying a GPS receiver may approach the centimeter level, while other applications may require an accuracy of ten meters. Two sources of ephemerides are available: National Imagery and Mapping Agency (NIMA) and the International GPS Service (IGS). In both cases, the respective agency operates a ground network of GPS receivers to support the determination of the GPS orbits. In the case of the IGS, an international collaboration of agencies supports a ground network of 200 receivers, somewhat uniformly distributed around the Earth. Seven Analysis Centers of the IGS use a subset of measurements from these receivers to determine GPS ephemerides and the IGS combines these products into a single official IGS product. The IGS final product is available with a latency of two to three weeks with an accuracy expected to be at the decimeter level, but a rapid product is available with a one-day latency.


<!-- chunk 0003: pages 141-210 -->
# Satellite-to-Satellite Tracking (SST)

Various forms of satellite-to-satellite tracking (SST) are in use. This terminology usually applies to measurements collected between a pair of satellites, but the common terminology enables identification of the respective satellite altitude. If a GPS receiver is carried on a LEO satellite, then the previously described GPS measurements would be categorized as high-low SST measurements. For some GPS satellites, an inter-satellite range measurement is made, known as cross-link ranging, that would be a high-high SST measurement.

A recent example of low-low SST measurements is represented by the Gravity Recovery And Climate Experiment (GRACE). The SST measurements are primarily used to detect components of the Earth’s gravitational field and especially gravity variations associated with redistribution of mass. Two low-altitude satellites are used and each satellite transmits signals at two frequencies in the K-band ${ ( 2 4 \mathrm { G H z } ) }$ and Ka-band $( 3 2 \mathrm { G H z } $ ), but the actual frequencies used by each satellite are not identical. The satellites have approximately the same $5 0 0 \mathrm { - k m }$ altitude and are in the same orbit plane, but separated in the along-track direction by about $2 0 0 \mathrm { k m }$ . Each satellite carries a GPS receiver, but these receivers have been modified to track both the GPS signals and the K-band signals transmitted by the other GRACE satellite.

The GRACE SST measurements in the K-band are similar to GPS one-way measurements of carrier phase made in the L-band. Two K-band measurements are made at different frequencies on each satellite to enable a correction for the ionosphere using the technique discussed in Section 3.4.2. The measurements made and recorded by each GRACE satellite are a form of one-way carrier phase similar to GPS. Each GRACE satellite carries an ultra-stable oscillator as the frequency reference $\mathrm { ( { \sim } 4 . 8 M H z }$ ) that is used to generate the transmitted signal and to mix with the signal that arrives from the other satellite. Simply stated, each satellite measures the carrier phase signal it receives from the other satellite relative to the signal that it transmits. In an approach similar to measurement differencing (Section 3.6), the measurements collected on each satellite can be added to obtain a measurement that is proportional to the range between the satellites, while at the same time removing long-term oscillator instability. This form of SST measurement has been termed dual-one-way-ranging. The measurement and instrumentation has been described by Dunn et al. (2003).

# 3.5.2 TWO-WAY RANGE

# SLR

The basic concept of a two-way range was described in Section 3.3.1. Examples of this measurement type include ground-based satellite laser ranging (SLR) systems and satellite-borne altimeters. SLR was applied for the first time by

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0003_pages_0141-0210/auto/images/4cade39067ab2c869d7f6132206044b360fa8590687093fd918aa1f46c94ef9c.jpg)  
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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0003_pages_0141-0210/auto/images/03d3b8c0c558fcfaeb4a6a9def463fcca846015cce97222c981629ac813f970b.jpg)  
Figure 3.5.4: The ICESat SLR array. The circular components on each fla t face contain a cube corner with the optical property of reflecting incoming light back to the source. There are nine corner cubes, each with a diameter of $3 . 2 \mathrm { c m }$ . (Photo courtesy of ITE, Inc.)

# Altimeter

A radar altimeter, such as those carried on TOPEX/Poseidon (T/P), operates similarly to the SLR system as a two-way measurement. The altimeter sends a chirp and measures the round-trip time. The TOPEX altimeter (U.S.) operates with two frequencies to enable a correction for the ionosphere, whereas the Poseidon altimeter (France) uses a single frequency and relies on other data to provide the ionosphere correction. The TOPEX frequencies are $1 3 . 6 \ : \mathrm { G H z }$ and 5.3 GHz, and the Poseidon frequency is $1 3 . 6 5 \ : \mathrm { G H z }$ . The altimeters share a common antenna, but only one altimeter is operated at a time. The TOPEX ionosphere correction can be obtained from Eq. (3.4.12), and the antenna is shown in Fig. 3.5.5. As shown, TOPEX carried several tracking systems that supported determination of the TOPEX orbit.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0003_pages_0141-0210/auto/images/452677711303e29510ab1416d21a1886f861f1a331e8e51f79803328b970e9ee.jpg)  
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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0003_pages_0141-0210/auto/images/17965033e8ee4a77f66b806e74b281b8ba4f0d8fd65c5808b05a62641004a101.jpg)  
Figure 3.5.6: McDonald Observatory (MDO1) L1 pseudorange from PRN-6 on 19 June 1999. The uncorrected pseudorange as recorded by the receiver at a 30 second interval is shown. No pseudoranges were recorded for 200 seconds at about 67000 seconds.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0003_pages_0141-0210/auto/images/e9f7caf7ac1d949f252583ddc77e3b23f147bc6bb07b91551c8ec1b1edfc3129.jpg)  
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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0003_pages_0141-0210/auto/images/4c0805c462d4e592e6c9737810f265a1c26eb90a21de427d502ec337215283ee.jpg)  
Figure 3.5.8: MDO1 $L _ { 1 }$ pseudorange residuals (O-C) from 19 June 1998 for PRN6. The computed pseudorange (C) was obtained from the geometric range at signal receive time with no corrections. The one meter measurement noise is not evident at this scale since the O-C characteristics are dominated by an overall drift and high-frequency variations.

After SA, the next dominant characteristics in the residuals are the nonzero mean and the linear slope that remains after “remo val” of the mean and the periodic variations. Both the nonzero mean and the linear slope are caused by uncorrected clock errors, with some contribution from the generation of the computed range using the geometric range.

With the expectation that the receiver coordinates and the IGS ephemerides for the GPS satellites have errors at the decimeter level (see Table 3.5.4), the plots for (O-C) would show only random noise at the $5 0 \mathrm { - c m }$ level if the one-way range were properly computed from the available information, the clock errors were corrected, and the atmospheric delays were accounted for. The two receivers used in this example record pseudorange and carrier phase at a 30-second interval.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0003_pages_0141-0210/auto/images/dccf087e48f6de634dd851ba8fe1f3be2cbf0bb38f628aabf9647cdfd2b1cddd.jpg)  
Figure 3.5.9: PIE1 $L - 1$ pseudorange residuals (O-C) for PRN6 from 19 June 1998. These residuals were formed with the same procedure used in Fig. 3.5.8. The high-frequency variations have a high correlation with those observed for the same time period at MDO1; therefore, these variations are not produced by the receiver. The variations are associated with Selective Availability.

If carrier phase is converted to range, the plots for (O-C) would be dominated by a very large bias: the phase ambiguity term. However, removal of the ambiguity results in residual plots with characteristics very similar to Figs. 3.5.8 and 3.5.9. Since phase-range noise is usually a few millimeters, removal of the effects described in the preceding paragraph would illustrate the low noise level. The instrument noise statistics are usually used to describe the measurement precision.

# DORIS

An example of DORIS measurements obtained from TOPEX/Poseidon is shown in Fig. 3.5.10. The data in this figure are based on a DORIS beacon located at Fairbanks, Alaska. Both DORIS frequencies were used to remove the ionosphere, but there would be no noticeable difference on the scale shown if the plot had been made using a single-frequency measurement.

# Altimeter

As previously described, the altimeter measurement is based on two-way time of flight. The altimeter antenna is directed toward the nadir and a one-way range (altitude) is formed by dividing the round-trip time-of-flight by two. The TOPEX altimeter data collected during a long pass over the Pacific (TOPEX/Poseidon Repeat Cycle 303) are shown in Fig. 3.5.11. For this example, the dual-frequency correction for the ionosphere was made, along with other corrections, at the meter level. The T/P orbit is frozen (see Chapter 2) with argument of perigee at $9 0 ^ { \circ }$ , which occurs just past 35500 seconds. As illustrated, the minimum altitude occurs near 34500 seconds, approximately corresponding to a latitude of $0 ^ { \circ }$ . The apparent contradiction of the perigee location and the minimum altitude is explained by the ellipsoidal character of the Earth, which plays a dominant role in Fig. 3.5.11, since the eccentricity of the T/P orbit is small $( < 0 . 0 0 1 )$ ).

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0003_pages_0141-0210/auto/images/6aed504863288061a89f304507bd2bec53f60fb0e58d9be08167fb847f572903.jpg)  
Figure 3.5.10: DORIS Range-rate from TOPEX/Poseidon on June 8, 1999.

Using an ephemeris of high accuracy for T/P, a computed altitude $( C )$ to the Earth ellipsoid can be formed. The altitude residual, O-C, can be generated and is shown in Fig. 3.5.12, using satelllite geodetic latitude for the abscissa. The geodetic latitude at $- 6 5 . 7 ^ { \circ }$ corresponds to the initial time of 32759 seconds. The residuals illustrate the profile of the ocean surface, expressed with respect to a reference ellipsoid, since this pass crosses mostly ocean.

# 3.6 DIFFERENCED MEASUREMENTS

In some cases, the measurements made by a particular technique are differenced in special ways. The differencing of the measurements removes or dimin-

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0003_pages_0141-0210/auto/images/9545143a923bcad3cc794435709b4268b39714af9e2590722a68371c6395356e.jpg)  
Figure 3.5.11: The TOPEX altimeter data collected during a long pass over the Pacific (TOPEX/Poseidon Repeat Cycle 303) are shown here.

ishes one or more error sources. The most common use of such differencing is with GPS pseudorange and carrier phase measurements and with altimeter measurements.

# 3.6.1 DIFFERENCED GPS MEASUREMENTS

Figures 3.5.8 and 3.5.9 show a very clear correlation in high-frequency variations in the PRN-6 pseudorange residuals collected with two receivers separated by $5 5 0 \mathrm { k m }$ , as discussed in Section 3.5.4. These variations are caused by Selective Availability (SA), an intentional dithering of the broadcasting satellite clock. SA was turned off in May 2000, but provides an excellent example of the application of differenced data. An obvious approach to removing this effect is to difference the residuals (or the measurements) shown in Figs. 3.5.8 and 3.5.9, which is referred to as a single difference $( S D )$ . In this case, the pseudorange measurements (or carrier phase) from a specific GPS satellite recorded at two different receivers can be differenced to produce:

$$
S D _ { j k } ^ { i } = \rho _ { j } ^ { i } - \rho _ { k } ^ { i }
$$

where $i$ identifies the GPS satellite, $j$ identifies one receiver, and $k$ identifies the other receiver. Alternatively, the single difference could be formed using mea-

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0003_pages_0141-0210/auto/images/406ea1b6541b1ed8eb2f70fa1bcc0cc6ae43af040b3f07aa93dcbb4430f39e99.jpg)  
Figure 3.5.12: The geodetic altitude residual, O-C, can be illustrated using satellite geodetic latitude for the abscissa, as shown here. The O-C is generated from the observed geodetic altitude (Fig. 3.5.11) and a computed altitude formed from a TOPEX ephemeris determined form DORIS and SLR. The residual illustrates the along-track ocean surface profile with respect to the reference ellipsoid.

surements collected by one receiver and two different satellites.

An SD residual can be formed from the a priori receiver coordinates and the given coordinates for the broadcasting satellites to generate the computed $S D$ . Hence, the SD residual is

$$
S D ( O - C ) _ { j k } ^ { i } = ( O - C ) _ { j } ^ { i } - ( O - C ) _ { k } ^ { i } ,
$$

where $O$ can be either pseudorange or carrier phase and $\mathrm { S D } ( O - C )$ represents the single difference residual using satellite $i$ and receivers $j$ and $k$ . Using Eq. (3.6.2), if the residuals shown in Fig. 3.5.8 are differenced with those in Fig. 3.5.9, the result is shown in Fig. 3.6.1, where it is evident that the SA high-frequency variations have been removed.

The single-difference residuals formed using a different satellite, PRN-30, are shown in Fig. 3.6.2. Although they are not shown, the residuals formed in the same way as Fig. 3.5.8 or 3.5.9, but using PRN-30 instead of PRN-6, exhibit similar high-frequency variations. Since the SA effect is satellite-dependent, the difference in the specific characteristics of the high-frequency variations is expected.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0003_pages_0141-0210/auto/images/5f426bf954c27a54291fcbac7d75fbbd3f98137aabb3fdc989bb84c47ed6ee90.jpg)  
Figure 3.6.1: Single difference L1 pseudorange residuals formed with PRN-6, MDO1, and PIE1.

The SD behavior shown in Figs. 3.6.1 and 3.6.2 warrants further discussion. The formation of the SD has removed most of the high-frequency variations that are evident in Figs. 3.5.8 and 3.5.9. The remaining SD residuals exhibit a linear slope, a discontinuity at about 67000 sec, and some very small amplitude variations with an apparent high frequency. The remaining linear slope suggests that the effect is caused by sources that are not common in the data collected by the two receivers. Such effects include errors in the respective receiver clocks, errors contributed by atmosphere delays, and errors in the approximation of the computed range by the geometric range. Although the receiver separation of $5 5 0 \mathrm { k m }$ perhaps seems large, it is not when compared to the GPS orbit radius of 26000 km. Since both PRN-6 and PRN-30 are within view of each receiver, the lineof-sight to each satellite from the respective receiver is similar, which means that the atmospheric delays will be very similar and some portion (but not all) of the atmospheric delay will be removed in the SD formation. Errors associated with use of geometric range will partially cancel in the SD as well. However, the clock behavior of each receiver will be different and cannot be expected to cancel. As a consequence, receiver clock errors are expected to be the dominant error source that produces the linear variation in SD residuals shown in Figs. 3.6.1 and 3.6.2.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0003_pages_0141-0210/auto/images/2abd23e9c2559bf9e358051de79ed1e53eb414f8cf2429bbb5cb78308b650e42.jpg)  
Figure 3.6.2: Single difference L1 pseudorange residuals formed with PRN-30, MDO1, and PIE1.

The discontinuity in Figs. 3.6.1 and 3.6.2 is another matter. This discontinuity occurs when the MDO1 receiver did not record data, but the PIE1 receiver does not show a gap in the data record. Although the precise cause of the discontinuity is not known, it appears to be associated with some event at MDO1, such as a clock anomaly related to the data gap.

The third characteristic evident in the SD residuals is an apparently small amplitude variation, which exhibits larger amplitude at the endpoints. These endpoints correlate with satellite rise and satellite set of one or both satellites. Clearly, SD measurements require that data from two satellites be available, so the difference between satellites requires that both satellites are located above the receiver horizon. The nature of these apparent high-frequency variations will become clearer in the following discussion.

The single differences for PRN-6 and PRN-30 can be further differenced to remove additional common errors. The resulting double difference (DD) is

$$
D D _ { j k } ^ { i m } = S D _ { j } ^ { i } - S D _ { k } ^ { m }
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0003_pages_0141-0210/auto/images/98e25d19d87833d5b59641974ffda9a481a324c9d1daa3af63f0c168600738b3.jpg)  
Figure 3.6.3: Double difference L1 pseudorange residuals formed from PRN-6, PRN-30, MDO1, and PIE1.

where DD represents the DD residual, formed between satellites $i$ and $m$ , and receivers $j$ and $k$ . The DD residual can be formed by differencing the single difference residuals, for example.

Double difference residuals can be formed by differencing the data used to create the plots of Figs. 3.6.1 and 3.6.2. The corresponding pseudorange DD residuals are shown in Fig. 3.6.4. It is evident that the dominant characteristics observed in the SD residuals have disappeared and the residuals are now scattered near zero. These residuals now exhibit a more random character and the only systematic characteristic is a slight linear slope. The fact that the Fig. 3.6.4 residuals are near zero demonstrates that the coordinates of the receivers given in Table 3.5.3 and the IGS ephemerides are quite accurate. If the receiver coordinates or the satellite ephemerides contained significant errors, the resulting DD residuals would reflect those errors, though not necessarily in a one-to-one ratio.

Note these additional points from Fig. 3.6.4. The obvious scatter is referred to as a measurement noise or measurement precision. The scatter seems to increase near the initial times and the final times, which is likely caused by low elevation effects at one or both receivers where the signal-to-noise ratio is degraded.

If the SD residuals had been computed using carrier phase (converted to phase range) and if the computations had been performed in the same way as those for pseudorange described earlier, the residuals would have a large bias caused by the phase ambiguity. Without any correction for this ambiguity, the ambiguities in each of the phase range measurements would combine to produce a constant bias in the phase range DD residuals. Determination of the respective phase ambiguities is referred to as ambiguity resolution. In many cases the ambiguity may be estimated with other parameters in the estimation process. Once the phase ambiguity has been removed, either in the individual receiver/satellite measurements or as a combined term in the DD, the residuals formed after ambiguity removal would exhibit characteristics similar to Fig. 3.6.4, with the major exception that the residuals would be at the level of a few millimeters instead of the meter level evident in Fig. 3.6.4.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0003_pages_0141-0210/auto/images/2051e990bcd024d9d89eb8fd1e385bf0efde8e3de2d28c97c0ee61bcb4bb18bb.jpg)  
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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0003_pages_0141-0210/auto/images/03348afeac62a904729c993877ee66c9d871afa5f4312c4105a3fdbafa53ce6c.jpg)

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


<!-- chunk 0004: pages 211-280 -->
Here $t _ { 0 }$ is an arbitrary epoch and all quantities in Eq. (4.6.1) are assumed to have been mapped to this epoch using the appropriate state transition matrices as illustrated in Eqs. (4.3.15) and (4.3.16). Because we are dealing with a linearized system, Eq. (4.6.1) generally is iterated to convergence; that is, until $\hat { \mathbf { x } } _ { 0 }$ no longer changes. Note that the two matrices in Eq. (4.6.1) that must be accumulated are $H ^ { T } R ^ { - 1 } H$ and $H ^ { T } R ^ { - 1 } \mathbf { y }$ . If $R$ is a block diagonal matrix—the observations are uncorrelated in time although correlations between the observations at any given time may exist—these matrices simply may be accumulated as follows:

$$
H ^ { T } R ^ { - 1 } H = \sum _ { i = 1 } ^ { \ell } \left[ \widetilde { H } _ { i } \Phi ( t _ { i } , t _ { 0 } ) \right] ^ { T } R _ { i } ^ { - 1 } \widetilde { H } _ { i } \Phi ( t _ { i } , t _ { 0 } )
$$

$$
\boldsymbol { H } ^ { T } \boldsymbol { R } ^ { - 1 } \mathbf { y } = \sum _ { i = 1 } ^ { \ell } [ \widetilde { H } _ { i } \Phi ( t _ { i } , t _ { 0 } ) ] ^ { T } R _ { i } ^ { - 1 } \mathbf { y } _ { i } .
$$

In general $\mathbf { X } ^ { * } ( t _ { 0 } )$ would be chosen so that $\bar { \bf x } _ { 0 } = 0$ , and $\overline { { P } } _ { 0 }$ would reflect the relative accuracy of the elements of the initial condition vector $\mathbf { X } ^ { * } ( t _ { 0 } )$ . In theory $\bar { \bf x } _ { 0 }$ and $\bar { P } _ { 0 }$ represent information and should be treated as data that are merged with the observation data, as indicated by Eq. (4.6.1). Consequently, the value of $\mathbf { X } _ { 0 } ^ { * } + \bar { \mathbf { x } } _ { 0 }$ should be held constant for the beginning of each iteration. Since the initial condition vector $\mathbf { X } _ { 0 } ^ { * }$ is augmented by the value of $\hat { \mathbf { x } } _ { 0 }$ after each iteration, that is, $( \mathbf { X } _ { 0 } ^ { * } ) _ { n } \ = \ ( \mathbf { X } _ { 0 } ^ { * } ) _ { n - 1 } + ( \hat { \mathbf { x } } _ { 0 } ) _ { n }$ , holding $\mathbf { X } _ { 0 } ^ { * } + \bar { \mathbf { x } } _ { 0 }$ constant results in the following expression for $\left( \bar { \mathbf { x } } _ { 0 } \right) _ { n }$

$$
\begin{array} { r l } & { \mathbf { X } _ { 0 } ^ { * } + \bar { \mathbf { x } } _ { 0 } = ( \mathbf { X } _ { 0 } ^ { * } ) _ { n - 1 } + ( \bar { \mathbf { x } } _ { 0 } ) _ { n - 1 } } \\ & { \qquad = ( \mathbf { X } _ { 0 } ^ { * } ) _ { n } + ( \bar { \mathbf { x } } _ { 0 } ) _ { n } } \\ & { \qquad = ( \mathbf { X } _ { 0 } ^ { * } ) _ { n - 1 } + ( \bar { \mathbf { x } } _ { 0 } ) _ { n - 1 } + ( \bar { \mathbf { x } } _ { 0 } ) _ { n } } \end{array}
$$

or

$$
( \bar { \bf x } _ { 0 } ) _ { n } = ( \bar { \bf x } _ { 0 } ) _ { n - 1 } - ( \hat { \bf x } _ { 0 } ) _ { n - 1 } .
$$

Recall from Section 4.2 that the state transition matrix is obtained by integrating

$$
{ \dot { \Phi } } ( t , t _ { k } ) = A ( t ) \Phi ( t , t _ { k } )
$$

subject to the initial conditions

$$
\Phi ( t _ { k } , t _ { k } ) = I
$$

along with the nonlinear equations, $\dot { \mathbf { X } } ^ { * } = F ( \mathbf { X } ^ { * } , t )$ , which define the nominal trajectory, $\mathbf { X } ^ { * } ( t )$ . The matrix $A ( t )$ is evaluated on the reference trajectory,

$$
A ( t ) = \frac { \partial F ( \mathbf { X } ^ { * } , t ) } { \partial \mathbf { X } }
$$

(A) Initialize for this iteration:

Set $i = 1$ . Set $t _ { i - 1 } = t _ { 0 }$ , $\mathbf { X } ^ { * } ( t _ { i - 1 } ) = \mathbf { X } _ { 0 } ^ { * }$ , $\Phi ( t _ { i - 1 } , t _ { 0 } ) = \Phi ( t _ { 0 } , t _ { 0 } ) = I$ .   
If there is an a priori estimate, set $\Lambda = \overline { { P } } _ { 0 } ^ { - 1 }$ and set $N = \overline { { P } } _ { 0 } ^ { - 1 } \bar { \mathbf { x } } _ { 0 }$ .   
If there is no a priori estimate, set $\Lambda = 0$ and set $N = 0$ .

(B) Read the next observation: $t _ { i } , \mathbf { Y } _ { i } , R _ { i }$ .

Integrate reference trajectory and state transition matrix from $t _ { i - 1 }$ to $t _ { i }$ . $\dot { \mathbf { X } } ^ { * } = F ( \mathbf { X } ^ { * } ( t ) , t )$ with initial conditions $\mathbf { X } ^ { * } ( t _ { i - 1 } )$   
$A ( t ) = [ \partial F ( \mathbf { X } , t ) / \partial \mathbf { X } ] ^ { * }$ , where ∗ means evaluated on the nominal trajectory.   
${ \dot { \Phi } } ( t , t _ { 0 } ) = A ( t ) \Phi ( t , t _ { 0 } )$ with initial conditions $\Phi ( t _ { i - 1 } , t _ { 0 } )$ .   
This gives $\mathbf { X } ^ { * } ( t _ { i } ) , \Phi ( t _ { i } , t _ { 0 } )$ .

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/bbcad0286f942247b57137958751a396aa9376a3de23756296757d126bc15411.jpg)

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/71112c9f3e2517bc85ad0e8ffad047b0a127e31db172bccc12760bb993fd6621.jpg)

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/33ba23dc10add28bf439865c9184ba2e310c90a5095f513e145e96d80c038aa9.jpg)  
Figure 4.6.1: Batch processing algorithm flo w chart.

where $F ( \mathbf { X } ^ { * } , t )$ is the time derivative of the state vector in the differential equations governing the time evolution of the system. The observation-state mapping matrix is given by

$$
\widetilde { H } _ { i } = \frac { \partial G ( \mathbf { X } _ { i } ^ { * } , t _ { i } ) } { \partial \mathbf { X } }
$$

where $G ( \mathbf { X } _ { i } ^ { * } , t _ { i } )$ are the observation-state relationships evaluated on the nominal or reference trajectory.

Notice that the solution for $\hat { \mathbf { x } } _ { 0 }$ involved inversion of the information matrix, $\Lambda _ { 0 }$ , where

$$
\Lambda _ { 0 } = H ^ { T } R ^ { - 1 } H + \overline { { { \cal P } } } _ { 0 } ^ { - 1 } .
$$

Generally the normal equation would not be solved by a direct inversion of $\Lambda _ { 0 }$ but rather would be solved by an indirect but more accurate technique, such as the Cholesky decomposition described in Chapter 5, Section 5.2. The sequence of operations required to implement the batch estimation process is outlined in Fig. 4.6.1. Note that the algorithm in Fig. 4.6.1 assumes that there are no observations at $t _ { 0 }$ . If observations exist at $t _ { 0 }$ , set $\overline { { \Lambda } } = \overline { { P } } _ { 0 } ^ { - 1 } + H _ { 0 } ^ { T } R _ { 0 } ^ { - 1 } H _ { 0 }$ and $N = H _ { 0 } ^ { T } R _ { 0 } ^ { - 1 } \mathbf { y } _ { 0 }$ in the initialization box, A. As previously stated, the entire sequence of computations are repeated until the estimation process has converged. If there are observations at $t _ { 0 }$ , the state transition matrix for processing these observations is the identity matrix.

This procedure yields a minimum value of the performance index (see Eq. (4.3.24))

$$
J ( x ) = ( \hat { \mathbf { x } } _ { 0 } - \bar { \mathbf { x } } _ { 0 } ) ^ { T } \overline { { P } } _ { 0 } ^ { - 1 } ( \hat { \mathbf { x } } _ { 0 } - \bar { \mathbf { x } } _ { 0 } ) + \sum _ { i = 1 } ^ { \ell } \hat { \epsilon } _ { i } ^ { T } R _ { i } ^ { - 1 } \hat { \epsilon } _ { i }
$$

where

$$
\hat { \mathbf { \epsilon } } _ { i } = \mathbf { y } _ { i } - H _ { i } \hat { \mathbf { x } } _ { 0 }
$$

and $\hat { \epsilon } _ { i }$ is the best estimate of the observation error.

In practice, $\overline { { P } } _ { 0 }$ is generally not a realistic representation of the accuracy of $\bar { \bf x } _ { 0 }$ and it is used only to better condition the estimation error covariance matrix, $P$ . In this case, $\bar { \bf x } _ { 0 }$ usually is set to zero for each iteration and ${ \overline { { P } } } _ { 0 }$ is chosen to be a diagonal matrix with large diagonal values. Hence, the firs t term in Eq. (4.6.8) will be very small and the tracking data residuals will determine the value of $J ( x )$ . The RMS of the observation residuals generally is computed and may be used as a measure of convergence; when the RMS no longer changes the solution is assumed to be converged. The RMS is computed from

$$
\mathrm { R M S } = \left\{ \frac { \displaystyle \sum _ { i = 1 } ^ { \ell } \hat { \epsilon } _ { i } ^ { T } R _ { i } ^ { - 1 } \hat { \mathbf { \epsilon } } _ { i } } { m } \right\} ^ { 1 / 2 } .
$$

$\hat { \epsilon } _ { i }$ is a p-vector and $m = \ell \times p$ . Hence, $m$ is the total number of observations. Eq. (4.6.10) is referred to as the weighted RMS. If the RMS is computed without including the weighting matrix, $R _ { i } ^ { - 1 }$ , it may be referred to as the unweighted RMS or just the RMS.

# 4.7 THE SEQUENTIAL ESTIMATION ALGORITHM

In this section, an alternate approach to the batch processor is discussed in which the observations are processed as soon as they are received. An advantage of this approach, referred to as the sequential processing algorithm, is that the matrix to be inverted will be of the same dimension as the observation vector. Hence, if the observations are processed individually, only scalar divisions will be required to obtain the estimate of $\mathbf { x } _ { k }$ . The algorithm was developed originally by Swerling (1959), but the treatment that received more popular acclaim is due to Kalman (1960). In fact, the sequential estimation algorithm discussed here often is referred to as the Kalman filter . A number of papers and textbooks have been written describing and providing variations of the Kalman fil ter. The collection of papers edited by Sorenson (1985) contains many of the pioneering papers in this area. Also, the treatments by Bierman (1977), Liebelt (1967), Tapley (1973), Gelb (1974), Maybeck (1979), Grewal and Andrews (1993), and Montenbruck and Gill (2000) are other references.

Recall that an estimate $\hat { \mathbf { x } } _ { j }$ and a covariance matrix $P _ { j }$ can be propagated forward to a time $t _ { k }$ by the relations

$$
\begin{array} { r l } & { \overline { { \mathbf { x } } } _ { k } = \Phi ( t _ { k } , t _ { j } ) \hat { \mathbf { x } } _ { j } } \\ & { \overline { { P } } _ { k } = \Phi ( t _ { k } , t _ { j } ) P _ { j } \Phi ^ { T } ( t _ { k } , t _ { j } ) . } \end{array}
$$

Assume that we have an additional observation at $t _ { k }$ (see Eq. (4.2.6)),

$$
\mathbf { y } _ { k } = \widetilde { H } _ { k } \mathbf { x } _ { k } + \boldsymbol { \epsilon } _ { k }
$$

where $E [ \epsilon _ { k } ] = 0$ and $E [ \epsilon _ { k } \epsilon _ { j } ^ { T } ] = R _ { k } \delta _ { k j }$ , where $\delta _ { k j }$ is the Kronicker delta. We wish to process $\mathbf { y } _ { k }$ in order to determine $\hat { \mathbf { x } } _ { k }$ . The best estimate of $\mathbf { x } _ { k }$ is obtained in Eq. (4.4.29) as

$$
\begin{array} { r } { \hat { \mathbf { x } } _ { k } = \big ( \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } + \overline { { P } } _ { k } ^ { - 1 } ) ^ { - 1 } \big ( \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \mathbf { y } _ { k } + \overline { { P } } _ { k } ^ { - 1 } \overline { { \mathbf { x } } } _ { k } \big ) . } \end{array}
$$

The primary computational problems are associated with computing the $( n \times n )$ matrix inverse in Eq. (4.7.3). Recall that in the original derivation it was shown that the quantity to be inverted is the information matrix $\Lambda _ { k }$ , which yields the covariance matrix $P _ { k }$ associated with estimate $\hat { \mathbf { x } } _ { k }$ (see Eq. (4.4.30)),

$$
P _ { k } = \Lambda _ { k } ^ { - 1 } = ( \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } + \overline { { P } } _ { k } ^ { \ - 1 } ) ^ { - 1 } .
$$

From Eq. (4.7.4), it follows that

$$
\begin{array} { r } { P _ { k } ^ { - 1 } = \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } + \overline { { P } } _ { k } ^ { - 1 } . } \end{array}
$$

Premultiplying each side of Eq. (4.7.5) by $P _ { k }$ and then postmultiplying by $\overline { { P } } _ { k }$ leads to the following expressions:

$$
\overline { { P } } _ { k } = P _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } \overline { { P } } _ { k } + P _ { k }
$$

or

$$
P _ { k } = \overline { { P } } _ { k } - P _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } \overline { { P } } _ { k } .
$$

Now if Eq. (4.7.6) is postmultiplied by the quantity $H _ { k } ^ { T } { \cal R } _ { k } ^ { - 1 }$ , the following expression is obtained:

$$
\begin{array} { r l } & { \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } = P _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } [ \widetilde { H } _ { k } \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } + I ] } \\ & { \qquad = P _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } [ \widetilde { H } _ { k } \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } + R _ { k } ] R _ { k } ^ { - 1 } . } \end{array}
$$

Solving for the quantity $P _ { k } \widetilde { H } _ { k } ^ { T } { R _ { k } ^ { - 1 } }$ leads to

$$
\begin{array} { r } { P _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } = \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } [ \widetilde { H } _ { k } \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } + R _ { k } ] ^ { - 1 } . } \end{array}
$$

This relates the a priori covariance matrix $\overline { { P } } _ { k }$ to the $a$ posteriori covariance matrix $P _ { k }$ . If Eq. (4.7.9) is used to eliminate $P _ { k } \widetilde { H } _ { k } ^ { T } { R _ { k } ^ { - 1 } }$ in Eq. (4.7.7), the following result is obtained:

$$
\begin{array} { r } { P _ { k } = \overline { { P } } _ { k } - \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } [ \widetilde { H } _ { k } \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } + R _ { k } ] ^ { - 1 } \widetilde { H } _ { k } \overline { { P } } _ { k } . } \end{array}
$$

Equation (4.7.10) also can be derived by using the Schur identity (Theorem 4 of Appendix B). Note that Eq. (4.7.10) is an alternate way of computing the inverse in Eq. (4.7.4). In Eq. (4.7.10), the matrix to be inverted is of dimension $p \times p$ , the same dimensions as the observation error covariance matrix. If the observations are processed as scalars (i.e., one at a time), only a scalar division is required. If the weighting matrix, $K _ { k }$ (sometimes referred to as the Kalman gain or simply gain matrix), is defined as

$$
\begin{array} { r } { K _ { k } \equiv \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } [ \widetilde { H } _ { k } \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } + R _ { k } ] ^ { - 1 } , } \end{array}
$$

then Eq. (4.7.10) can be expressed in the compact form

$$
P _ { k } = [ I - K _ { k } { \widetilde { H } } _ { k } ] { \overline { { P } } } _ { k } .
$$

If Eq. (4.7.4) is substituted into Eq. (4.7.3), the sequential form for computing $\hat { \mathbf { x } } _ { k }$ can be written as

$$
\hat { \mathbf { x } } _ { k } = P _ { k } [ \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \mathbf { y } _ { k } + \overline { { P } } _ { k } ^ { - 1 } \overline { { \mathbf { x } } } _ { k } ]
$$

$$
\mathbf { \Sigma } = P _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \mathbf { y } _ { k } + P _ { k } \overline { { P } } _ { k } ^ { - 1 } \overline { { \mathbf { x } } } _ { k } .
$$

But from Eqs. (4.7.9) and (4.7.11)

$$
K _ { k } = P _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } .
$$

Using the preceding and Eq. (4.7.12), Eq. (4.7.13) becomes

$$
\hat { \mathbf { x } } _ { k } = K _ { k } \mathbf { y } _ { k } + [ I - K _ { k } \widetilde { H } _ { k } ] \overline { { P } } _ { k } \overline { { P } } _ { k } ^ { - 1 } \overline { { \mathbf { x } } } _ { k } .
$$

Collecting terms yields

$$
\hat { \mathbf { x } } _ { k } = \overline { { \mathbf { x } } } _ { k } + K _ { k } [ \mathbf { y } _ { k } - \widetilde { H } _ { k } \overline { { \mathbf { x } } } _ { k } ] .
$$

Equation (4.7.16), with Eqs. (4.7.1), (4.7.11), and (4.7.12), can be used in a recursive fashion to compute the estimate of $\hat { \mathbf { x } } _ { k }$ , incorporating the observation $\mathbf { y } _ { k }$ .

# 4.7.1 THE SEQUENTIAL COMPUTATIONAL ALGORITHM

The algorithm for computing the estimate sequentially is summarized as

Given: $\hat { \mathbf { x } } _ { k - 1 }$ , $P _ { k - 1 }$ , $\mathbf { X } _ { k - 1 } ^ { * }$ , and $R _ { k }$ , and the observation ${ \bf Y } _ { k }$ , at $t _ { k }$ (at the initial time $t _ { 0 }$ , these would be $\mathbf { X } _ { 0 } ^ { * }$ , $\hat { \mathbf { x } } _ { 0 }$ , and $P _ { 0 }$ ).

(1) Integrate from $t _ { k - 1 }$ to $t _ { k }$ ,

$$
\begin{array} { l l } { { { \dot { \bf X } } ^ { * } = F ( { \bf X } ^ { * } , t ) , } } & { { \qquad { \bf X } ^ { * } ( t _ { k - 1 } ) = { \bf X } _ { k - 1 } ^ { * } } } \\ { { { \dot { \Phi } } ( t , t _ { k - 1 } ) = A ( t ) \Phi ( t , t _ { k - 1 } ) , } } & { { \qquad \Phi ( t _ { k - 1 } , t _ { k - 1 } ) = I . } } \end{array}
$$

(2) Compute

$$
\begin{array} { r } { \overline { { \mathbf { x } } } _ { k } = \Phi ( t _ { k } , t _ { k - 1 } ) \widehat { \mathbf { x } } _ { k - 1 } \quad \overline { { P } } _ { k } = \Phi ( t _ { k } , t _ { k - 1 } ) P _ { k - 1 } \Phi ^ { T } ( t _ { k } , t _ { k - 1 } ) . } \end{array}
$$

(3) Compute

$$
\begin{array} { r } { \mathbf { y } _ { k } = \mathbf { Y } _ { k } - G ( \mathbf { X } _ { k } ^ { * } , t _ { k } ) \qquad { \widetilde { H } } _ { k } = { \frac { \partial G ( \mathbf { X } _ { k } ^ { * } , t _ { k } ) } { \partial \mathbf { X } } } . } \end{array}
$$

(4) Compute the measurement update

$$
\begin{array} { r l } & { K _ { k } = \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } [ \widetilde { H } _ { k } \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } + R _ { k } ] ^ { - 1 } } \\ & { \hat { \mathbf { x } } _ { k } = \overline { { \mathbf { x } } } _ { k } + K _ { k } [ \mathbf { y } _ { k } - \widetilde { H } _ { k } \overline { { \mathbf { x } } } _ { k } ] } \\ & { P _ { k } = [ I - K _ { k } \widetilde { H } _ { k } ] \overline { { P } } _ { k } . } \end{array}
$$

(5) Replace $k$ with $k + 1$ and return to (1).

Equation (4.7.1) is known as the time update and Eq. (4.7.18) is called the measurement update equation. The flow chart for the sequential computational algorithm is given in Fig. 4.7.1. If there is an observation at $t _ { 0 }$ , a time update is not performed but a measurement update is performed.

Note that we do not multiply $\widetilde { H } _ { k }$ by the state transition matrix, since the observation at $\mathbf { y } _ { k }$ is not accumulated at another time epoch, as is the case for the batch processor. Also, note that the differential equations for the state transition matrix are reinitialized at each observation epoch. Therefore, the state transition matrix is reinitialized at each observation epoch. If there is more than one observation at each epoch and we are processing them as scalars, we would set $\Phi ( t _ { i } , t _ { i } ) = I$ after processing the first observation at each epoch; $P$ and $\hat { \bf x }$ are not time updated until we move to the next observation epoch. The estimate of the state of the nonlinear system at $t _ { k }$ is given by $\hat { \mathbf { X } } _ { k } = \mathbf { \bar { X } } _ { k } ^ { * } + \hat { \mathbf { x } } _ { k }$ .

One disadvantage of both the batch and sequential algorithm lies in the fact that if the true state and the reference state are not close together then the linearization assumption leading to Eq. (4.2.6) may not be valid and the estimation process may diverge. The extended sequential filter algorithm (see Section 4.7.3) is often used to overcome problems with the linearity assumption.

A second unfavorable characteristic of the sequential estimation algorithm is that the state estimation error covariance matrix may approach zero as the number of observations becomes large. The sketch in Fig. 4.7.2 illustrates the behavior of the trace of the state estimation error covariance matrix as discrete observations are processed. As illustrated in this sketch, the trace grows between observations and is reduced by the amount, trace $( K \widetilde { H } \overline { { P } } )$ , after each observation. Hence, the magnitude of the covariance matrix elements will decrease depending on the density, information content, and accuracy of the observations.

Examination of the estimation algorithm shows that as $P _ { k } \to 0$ the gain approaches zero, and the estimation procedure will become insensitive to the observations. Consequently, the estimate will diverge due to either errors introduced in the linearization procedure, computational errors, or errors due to an incomplete mathematical model. To overcome this problem, process noise often is added to the state propagation equations (see Section 4.9).

In addition to these two problems, the Kalman filter may diverge because of numerical difficultie s associated with the covariance measurement update, given by Eq. (4.7.12). This problem is described in the next section.

# Numerical Considerations

The conventional Kalman filte r, which uses the covariance update, (4.7.12), can sometimes fail due to numerical problems with this equation. The covariance

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/60d483baad66a3a0c5aeaff6c324403706079b6ca401638d9485d7d69f86669f.jpg)

<table><tr><td>↓ Time Update</td></tr><tr><td>Xi=Φ(ti,ti-1)xi-1</td></tr><tr><td>Pi=Φ(ti,ti-1)Pi-1ΦT(ti,ti-1)</td></tr><tr><td>↓</td></tr></table>

Compute: observation deviation, observation-state matrix, gain matrix

$$
\begin{array} { r l } & { \mathbf { y } _ { i } = \mathbf { Y } _ { i } - G ( \mathbf { X } _ { i } ^ { * } , t _ { i } ) } \\ & { { \widetilde { H } } _ { i } = [ \partial G ( \mathbf { X } , t _ { i } ) / \partial \mathbf { X } ] ^ { * } } \\ & { K _ { i } = { \overline { { P } } } _ { i } { \widetilde { H } } _ { i } ^ { T } ( { \widetilde { H } } _ { i } { \overline { { P } } } _ { i } { \widetilde { H } } _ { i } ^ { T } + R _ { i } ) ^ { - 1 } } \end{array}
$$

Measurement Update

$$
\begin{array} { r l } & { \hat { \mathbf { x } } _ { i } = \bar { \mathbf { x } } _ { i } + K _ { i } [ \mathbf { y } _ { i } - \widetilde { H } _ { i } \bar { \mathbf { x } } _ { i } ] } \\ & { P _ { i } = ( I - K _ { i } \widetilde { H } _ { i } ) \overline { { P } } _ { i } } \\ & { \quad i = i + 1 . } \end{array}
$$

Thus: $t _ { i }$ becomes $t _ { i - 1 }$ , $\mathbf { X } ^ { * } ( t _ { i } )$ becomes $\mathbf { X } ^ { * } ( t _ { i - 1 } )$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/a76d23720b91a2b81fbaf7bba57968bb92e54ec95491cae1f999e9fe198616a4.jpg)  
Figure 4.7.1: Sequential processing algorithm flo w chart.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/299625b25f1bd7c3ae75b1409a6bd181cb5611d29252f027e0825fa15f560299.jpg)  
Figure 4.7.2: Illustration of the behavior of the trace of the state estimation error covariance matrix.

matrix may lose its properties of symmetry and become nonpositive definite when the computations are carried out with the finite digit arithmetic of the computer. In particular, this equation can fail to yield a symmetric positive definite result when a large a priori covariance is reduced by the incorporation of very accurate observation data.

In order to prevent these problems, several alternate algorithms have been suggested. A common alternative is to use the form of the equation given by Bucy and Joseph (1968):

$$
P _ { k } = ( I - K _ { k } \widetilde { H } _ { k } ) \overline { { P } } _ { k } ( I - K _ { k } \widetilde { H } _ { k } ) ^ { T } + K _ { k } R _ { k } K _ { k } ^ { T } .
$$

Note that this formulation will always yield a symmetric result for $P _ { k }$ , although it may lose its positive definite quality for a poorly observed system.

The most common solution to numerical problems with the covariance update is to use a square root formulation to update the covariance matrix. The square root algorithms are discussed in Chapter 5.

An example of a poorly conditioned system taken from Bierman (1977, p. 96, Example V.2) illustrates the numerical instability problem. Consider the problem of estimating $x _ { 1 }$ and $x _ { 2 }$ from scalar measurements $z _ { 1 }$ and $z _ { 2 }$ , where

$$
\begin{array} { l } { { z _ { 1 } = x _ { 1 } + \epsilon x _ { 2 } + v _ { 1 } } } \\ { { \ } } \\ { { z _ { 2 } = x _ { 1 } + x _ { 2 } + v _ { 2 } . } } \end{array}
$$

We assume that the observation noise $v _ { 1 }$ and $v _ { 2 }$ are uncorrelated, zero mean random variables with unit variance. If $v _ { 1 }$ and $v _ { 2 }$ do not have unit variance or are correlated, we can perform a simple whitening transformation so that their covariance matrix is the identity matrix (Bierman, 1977, or see Section 5.7.1). In matrix form,

$$
{ \Big [ } z _ { 1 } { \Big ] } = { \Big [ } { 1 \ \epsilon { \Big ] } } \left[ { x _ { 1 } { \Big ] } } + { \Big [ } v _ { 1 } { \Big ] } \right. .
$$

Assume that the $a$ priori covariance associated with our knowledge of $[ x _ { 1 } \ x _ { 2 } ]$ is given by

$$
{ \overline { { P } } } _ { 1 } = \sigma ^ { 2 } I
$$

where $\sigma = 1 / \epsilon$ and $0 < \epsilon \ll 1$ . The quantity $\epsilon$ is assumed to be small enough such that computer round-off produces

$$
\begin{array} { c } { { 1 + \epsilon ^ { 2 } = 1 , } } \\ { { \mathrm { a n d } } } \\ { { 1 + \epsilon \neq 1 ; } } \end{array}
$$

that is, $1 + \epsilon ^ { 2 }$ rounds to 1 and $1 + \epsilon$ does not. Note that $\sigma = 1 / \epsilon$ is large; hence, this is an illustration of the problem where accurate data is being combined with a large a priori covariance.

This estimation problem is well posed. The observation $z _ { 1 }$ provides an estimate of $x _ { 1 }$ which, when combined with $z _ { 2 }$ , should determine $x _ { 2 }$ . However, the conventional Kalman update to $P$ given by Eq. (4.7.12) will result in failure of the filte r.

The observations will be processed one at a time. Let the gain and estimation error covariance associated with $z _ { 1 }$ be denoted as $K _ { 1 }$ and $P _ { 1 }$ , respectively. Similar definitions apply for $z _ { 2 }$ .

The exact solution yields

$$
K _ { 1 } = \frac { 1 } { 1 + 2 \epsilon ^ { 2 } } \left[ { 1 \atop \epsilon } \right] .
$$

The estimation error covariance associated with processing $z _ { 1 }$ is

$$
P _ { 1 } = \frac { 1 } { 1 + 2 \epsilon ^ { 2 } } \left[ \begin{array} { c c } { { 2 } } & { { - \sigma } } \\ { { - \sigma } } & { { \sigma ^ { 2 } + 1 } } \end{array} \right] .
$$

After processing $z _ { 2 }$ it can be shown that the exact solution for the estimation error covariance is

$$
P _ { 2 } = \frac { 1 } { \beta } \left[ \begin{array} { c c } { 1 + 2 \epsilon ^ { 2 } } & { - ( 1 + \epsilon ) } \\ { - ( 1 + \epsilon ) } & { 2 + \epsilon ^ { 2 } } \end{array} \right] ,
$$

where

$$
\beta = 1 - 2 \epsilon + 2 \epsilon ^ { 2 } ( 2 + \epsilon ^ { 2 } )
$$

and we see that both $P _ { 1 }$ and $P _ { 2 }$ are symmetric and positive definite.

The conventional Kalman filter, subject to Eq. (4.7.21), yields

$$
K _ { 1 } = { \left[ \begin{array} { l } { 1 } \\ { \epsilon } \end{array} \right] }
$$

and

$$
P _ { 1 } = \left[ \begin{array} { c c } { { 0 } } & { { - \sigma } } \\ { { - \sigma } } & { { \sigma ^ { 2 } } } \end{array} \right] .
$$

Note that $P _ { 1 }$ is no longer positive definite and the filter will not produce correct results. If $z _ { 2 }$ is processed, the conventional Kalman filter yields

$$
P _ { 2 } = \frac { 1 } { 1 - 2 \epsilon } \left[ \begin{array} { r r } { - 1 } & { 1 } \\ { 1 } & { - 1 } \end{array} \right] .
$$

Note that $P _ { 2 }$ does not have positive terms on the diagonal and $| P _ { 2 } | = 0$ . Hence, the conventional Kalman filter has failed.

By way of comparison, the Joseph formulation yields

$$
\begin{array} { l } { P _ { 1 } = \left[ \begin{array} { c c } { 2 } & { - \sigma } \\ { - \sigma } & { \sigma ^ { 2 } } \end{array} \right] } \\ { P _ { 2 } = \left[ \begin{array} { c c } { 1 + 2 \epsilon } & { - ( 1 + 3 \epsilon ) } \\ { - ( 1 + 3 \epsilon ) } & { ( 2 + \epsilon ) } \end{array} \right] } \end{array}
$$

which are symmetric and positive definite and agree with the exact solution to $O ( \epsilon )$ .

It should be pointed out that the batch processor for this problem, under the same assumption that $1 + \epsilon ^ { 2 } = 1 $ , yields

$$
P _ { 2 } = \left[ \begin{array} { c c } { { 1 + 2 \epsilon } } & { { - ( 1 + 3 \epsilon ) } } \\ { { - ( 1 + 3 \epsilon ) } } & { { 2 ( 1 + 2 \epsilon ) } } \end{array} \right] .
$$

This agrees to $O ( \epsilon )$ with the exact solution for $P _ { 2 }$ . The batch solution is not as sensitive as the conventional Kalman filt er to computer round-off errors. An intuitive understanding of this can be had by examining the equations for $P$ .

For the batch processor

$$
P = ( \overline { { P } } _ { 0 } ^ { \ - 1 } + \sum _ { i = 1 } ^ { \ell } H _ { i } ^ { T } R ^ { - 1 } H _ { i } ) ^ { - 1 } ,
$$

and for the sequential processor

$$
P = ( I - \overline { { P } } \widetilde { H } ^ { T } ( \widetilde { H } \overline { { P } } \widetilde { H } ^ { T } + R ) ^ { - 1 } \widetilde { H } ) \overline { { P } } .
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/fd86a46bed129bb97d07da78bff502948dec04c255142bc17d00ddb43fb70d17.jpg)  
Figure 4.7.3: Difference of the exact trace of $P _ { 2 }$ and that for various algorithms versus the value of $\epsilon$ on the abscissa.

Hence, if very accurate tracking data (small values for the elements of $R$ ) are combined with a large a priori (large values for the elements of $\overline { { P } }$ ), the sequential algorithm will ignore the data contribution, $R$ , when it adds $\widetilde { H } \overline { { P } } \widetilde { H } ^ { T } + R$ ; whereas the batch processor will tend to ignore $\overline { { P } } _ { 0 } ^ { - 1 }$ and base its solution on the strength of the data when it computes $( \Sigma H ^ { T } R ^ { - 1 } H + \overline { { P } } _ { 0 } ^ { - 1 } )$ . It is emphasized that for sequential processing of the data the preferred solution to this problem is to use one of the square root formulations for propagating the covariance or information matrix discussed in Chapter 5.

Figure 4.7.3 shows the difference between the exact value of the trace of $P _ { 2 }$ and the trace computed using various algorithms on a 16-digit machine. Notice that the conventional Kalman update yields an error of O(1) for $\epsilon \simeq 1 0 ^ { - 8 }$ , whereas the Joseph and Potter algorithms approach this value for $\epsilon = 1 0 ^ { - 1 5 }$ . Also, the Givens and Householder algorithms, which are introduced in Chapter 5, and the batch algorithm are all highly accurate.

# 4.7.2 THE EXTENDED SEQUENTIAL ESTIMATION ALGORITHM

To minimize the effects of errors due to the neglect of higher order terms in the linearization procedure leading to Eq. (4.2.6), the extended form of the sequential estimation algorithm is sometimes used. This algorithm is often referred to as the Extended Kalman Filter (EKF). The primary difference between the sequential and the extended sequential algorithm is that the reference trajectory for the extended sequential algorithm is updated after each observation to reflect the best estimate of the true trajectory. For example, after processing the $k ^ { \mathrm { t h } }$ observation, the best estimate of the state vector at $t _ { k }$ is used to provide new initial conditions for the reference trajectory,

$$
( \mathbf { X } _ { k } ^ { * } ) _ { \mathrm { n e w } } = \hat { \mathbf { X } } _ { k } = \mathbf { X } _ { k } ^ { * } + \hat { \mathbf { x } } _ { k } .
$$

Using $\hat { \mathbf { X } } _ { k }$ for the reference trajectory leads to $\hat { \mathbf { x } } _ { k } = 0$ , which will result in $\bar { \bf x } _ { k + 1 } =$ 0. The integration for the reference trajectory and the state transition matrix is reinitialized at each observation epoch, and the equations are integrated forward from $t _ { k }$ to $t _ { k + 1 }$ . The estimate for $\hat { \mathbf { x } } _ { k + 1 }$ is then computed from

$$
\hat { \mathbf { x } } _ { k + 1 } = K _ { k + 1 } \mathbf { y } _ { k + 1 }
$$

where $K _ { k + 1 }$ and $\mathbf { y } _ { k + 1 }$ are computed based on the new reference orbit. Then, the reference orbit is updated at time $t _ { k + 1 }$ by incorporating $\hat { \mathbf { x } } _ { k + 1 }$ and the process proceeds to $t _ { k + 2 }$ . The process of incorporating the estimate at each observation point into the reference trajectory for propagating to the next observation epoch leads to the reference trajectory being the prediction of the estimate of the nonlinear state; for example, $\mathbf { X } ^ { * } ( t ) = \dot { \mathbf { X } } ( t )$ .

In actual practice, it is not a good idea to update the reference trajectory using the first observations. This is particularly true if the observations contain significant noise. After a few observations have been processed, the estimates of $\hat { \bf x }$ will stabilize, and the trajectory update can be initiated.

The advantage of the extended sequential algorithm is that convergence to the best estimate will be more rapid because errors introduced in the linearization process are reduced. In addition, because the state estimate deviation, $\hat { { \bf x } } ( t )$ , need not be mapped between observations, it is not necessary to compute the state transition matrix. The estimation error covariance matrix, $P ( t )$ , can be mapped by integrating the matrix differential equation (4.9.35) discussed in Section 4.9.

The major disadvantage of the extended sequential algorithm is that the differential equations for the reference trajectory must be reinitialized after each observation is processed.

# 4.7.3 THE EXTENDED SEQUENTIAL COMPUTATIONAL ALGORITHM

The algorithm for computing the extended sequential estimate can be summarized as follows:

Given: $P _ { k - 1 }$ , $\hat { \mathbf X } _ { k - 1 }$ and ${ \bf Y } _ { k } , R _ { k }$

(1) Integrate from $t _ { k - 1 }$ to $t _ { k }$

$$
\begin{array} { l } { \dot { \mathbf { X } } ^ { * } = F ( \mathbf { X } ^ { * } , t ) , \qquad \mathbf { X } ^ { * } ( t _ { k - 1 } ) \mathbf { \Omega } = \hat { \mathbf { X } } _ { k - 1 } } \\ { \dot { \Phi } ( t , t _ { k - 1 } ) = A ( t ) \Phi ( t , t _ { k - 1 } ) , \Phi ( t _ { k - 1 } , t _ { k - 1 } ) = I . } \end{array}
$$

(2) Compute

$$
\begin{array} { r l } & { \overline { { P } } _ { k } = \Phi ( t _ { k } , t _ { k - 1 } ) P _ { k - 1 } \Phi ^ { T } ( t _ { k } , t _ { k - 1 } ) } \\ & { \mathbf { y } _ { k } = \mathbf { Y } _ { k } - G ( \mathbf { X } _ { k } ^ { * } , t _ { k } ) } \\ & { \widetilde { H } _ { k } = \partial G ( \mathbf { X } _ { k } ^ { * } , t _ { k } ) / \partial \mathbf { X } _ { k } . } \end{array}
$$

(3) Compute

$$
\begin{array} { r l } & { K _ { k } = \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } [ \widetilde { H } _ { k } \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } + R _ { k } ] ^ { - 1 } } \\ & { \hat { \mathbf { X } } _ { k } = \mathbf { X } _ { k } ^ { * } + K _ { k } \mathbf { y } _ { k } } \\ & { P _ { k } = [ I - K _ { k } \widetilde { H } _ { k } ] \overline { { P } } _ { k } . } \end{array}
$$

(4) Replace $k$ with $k + 1$ and return to (1).

The flo w chart for the extended sequential computational algorithm is given in Fig. 4.7.4.

# 4.7.4 THE PREDICTION RESIDUAL

It is of interest to examine the variance of the predicted residuals, which are sometimes referred to as the innovation, or new information, which comes from each measurement. The predicted residual, or innovation, is the observation residual based on the a priori or predicted state , $\bar { \mathbf { x } } _ { k }$ , at the observation time, $t _ { k }$ , and is defined as

$$
\beta _ { k } = \mathbf { y } _ { k } - \widetilde { H } _ { k } \overline { { \mathbf { x } } } _ { k } .
$$

As noted previously,

$$
\begin{array} { r } { \overline { { \mathbf { x } } } _ { k } = \mathbf { x } _ { k } + \pmb { \eta } _ { k } } \\ { \mathbf { y } _ { k } = \widetilde { H } _ { k } \mathbf { x } _ { k } + \epsilon _ { k } } \end{array}
$$

where $\mathbf { x } _ { k }$ is the true value of the state deviation vector and $\eta _ { k }$ is the error in $\bar { \bf x } _ { k }$ Also,

$$
E [ \pmb { \eta } _ { k } ] = 0 , E [ \pmb { \eta } _ { k } \pmb { \eta } _ { k } ^ { T } ] = \overline { { P } } _ { k }
$$

and

$$
\begin{array} { c } { E [ \epsilon _ { k } ] = 0 , E [ \epsilon _ { k } \epsilon _ { k } ^ { T } ] = R _ { k } } \\ { E [ \epsilon _ { k } \eta _ { k } ^ { T } ] = 0 . } \end{array}
$$

From these conditions it follows that $\beta _ { k }$ has mean

$$
\begin{array} { l } { { \displaystyle E [ \beta _ { k } ] \equiv \overline { { \beta } } _ { k } = E \big ( \widetilde { H } _ { k } \mathbf { x } _ { k } + \epsilon _ { k } - \widetilde { H } _ { k } \overline { { \mathbf { x } } } _ { k } \big ) } } \\ { ~ = E \big ( \epsilon _ { k } - \widetilde { H } \pmb { \eta } _ { k } \big ) = 0 } \end{array}
$$

and variance-covariance

$$
\begin{array} { r l } & { P _ { \beta _ { k } } = E [ ( \beta _ { k } - \widetilde { \beta } _ { k } ) ( \beta _ { k } - \widetilde { \beta } _ { k } ) ^ { T } ] = E [ \beta _ { k } \beta _ { k } ^ { T } ] } \\ & { \quad \quad = E [ ( \mathbf { y } _ { k } - \widetilde { H } _ { k } \overline { { \mathbf { x } } } _ { k } ) ( \mathbf { y } _ { k } - \widetilde { H } _ { k } \overline { { \mathbf { x } } } _ { k } ) ^ { T } ] } \\ & { \quad \quad = E [ ( \epsilon _ { k } - \widetilde { H } _ { k } \eta _ { k } ) ( \epsilon _ { k } - \widetilde { H } _ { k } \eta _ { k } ) ^ { T } ] } \\ & { P _ { \beta _ { k } } = R _ { k } + \widetilde { H } _ { k } \widetilde { P } _ { k } \widetilde { H } _ { k } ^ { T } . } \end{array}
$$

Hence, for a large prediction residual variance-covariance, the Kalman gain

$$
K _ { k } = \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } P _ { \beta _ { k } } ^ { - 1 }
$$

will be small, and the observation will have little influence on the estimate of the state. Also, large values of the prediction residual relative to the prediction residual standard deviation may be an indication of bad tracking data and hence may be used to edit data from the solution.

# 4.8 EXAMPLE PROBLEMS

This section provides several examples that involve processing observations with the batch and sequential processors.

# 4.8.1 LINEAR SYSTEM

Given: A system described by

$$
\mathbf { x } ( t _ { i + 1 } ) = { \left[ \begin{array} { l } { x _ { 1 } ( t _ { i + 1 } ) } \\ { x _ { 2 } ( t _ { i + 1 } ) } \end{array} \right] } = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } ( t _ { i } ) } \\ { x _ { 2 } ( t _ { i } ) } \end{array} \right] }
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/8dabb60293eb43d2a585e8a97a8069b690434857bb41fd3ecd327dc40f6fbc7b.jpg)  
Figure 4.8.1: Extended sequential processing algorithm flo w chart.

and observation-state relationship

$$
\left[ \begin{array} { c } { y _ { 1 } ( t _ { i } ) } \\ { y _ { 2 } ( t _ { i } ) } \end{array} \right] = \left[ \begin{array} { c c } { 0 } & { 1 } \\ { 1 / 2 } & { 1 / 2 } \end{array} \right] \left[ \begin{array} { c } { x _ { 1 } ( t _ { i } ) } \\ { x _ { 2 } ( t _ { i } ) } \end{array} \right] + \left[ \begin{array} { c } { \epsilon _ { 1 } } \\ { \epsilon _ { 2 } } \end{array} \right]
$$

with a priori information

$$
\overline { { \mathbf { x } } } _ { 0 } = \overline { { \mathbf { x } } } ( t _ { 0 } ) = \left[ \begin{array} { l } { \overline { { x } } _ { 1 } ( t _ { 0 } ) } \\ { \overline { { x } } _ { 2 } ( t _ { 0 } ) } \end{array} \right] = \left[ \begin{array} { l } { 3 } \\ { 2 } \end{array} \right] , \overline { { P } } _ { 0 } = \overline { { P } } ( t _ { 0 } ) = \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right]
$$

$$
W ^ { - 1 } = R = E \left\{ \left[ \epsilon _ { 1 } \atop \epsilon _ { 2 } \right] \left[ \epsilon _ { 1 } \epsilon _ { 2 } \right] \right\} = \left[ \begin{array} { l l } { { 2 } } & { { 0 } } \\ { { 0 } } & { { 3 / 4 } } \end{array} \right]
$$

and observations at $t _ { 1 }$ given by

$$
{ \left[ \begin{array} { l } { y _ { 1 } ( t _ { 1 } ) } \\ { y _ { 2 } ( t _ { 1 } ) } \end{array} \right] } = { \left[ \begin{array} { l } { 6 } \\ { 4 } \end{array} \right] } .
$$

(1) Using the batch processor algorithm, determine the best estimate of $\mathbf { x } ( t _ { 0 } )$ based on observations $y _ { 1 } ( t _ { 1 } )$ and $y _ { 2 } ( t _ { 1 } ) , \overline { { \mathbf { x } } } ( t _ { 0 } ) , \overline { { P } } ( t _ { 0 } )$ , and $R$ .

(2) Using the sequential algorithm and the information given, determine $\hat { \mathbf { x } } ( t _ { 1 } )$ the best estimate of $\mathbf { x } ( t _ { 1 } )$ .

(3) Show that $\hat { \mathbf { x } } ( t _ { 0 } )$ obtained in (1), when mapped forward to $t _ { 1 }$ is equal to $\hat { \mathbf { x } } ( t _ { 1 } )$ obtained in (2). Show that $P _ { 0 }$ from the batch processor mapped forward to $t _ { 1 }$ agrees with $P _ { 1 }$ from the sequential processor.

(1) Batch Processor

$$
\begin{array} { r l } & { \Phi ( t _ { i + 1 } , t _ { i } ) = \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } \\ & { \qquad \widetilde { H } = \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 1 / 2 } & { 1 / 2 } \end{array} \right] , \quad \overline { { P } } _ { o } = \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] , \quad \overline { { \mathbf { x } } } _ { o } = \left[ \begin{array} { l } { 3 } \\ { 2 } \end{array} \right] } \\ & { W ^ { - 1 } = R = \left[ \begin{array} { l l } { 2 } & { 0 } \\ { 0 } & { 3 / 4 } \end{array} \right] } \\ & { \qquad \mathbf { y } = \left[ \begin{array} { l } { y _ { 1 } ( t _ { 1 } ) } \\ { y _ { 2 } ( t _ { 1 } ) } \end{array} \right] = \left[ \begin{array} { l } { 6 } \\ { 4 } \end{array} \right] . } \end{array}
$$

The computational algorithm for the batch processor is given in Section 4.6.

$$
\begin{array} { r l } & { \hat { \mathbf { x } } _ { 0 } = ( \overline { { P } } _ { 0 } ^ { - 1 } + H _ { 1 } ^ { T } W H _ { 1 } ) ^ { - 1 } ( H _ { 1 } ^ { T } W \mathbf { y } + \overline { { P } } _ { 0 } ^ { - 1 } \overline { { \mathbf { x } } } _ { 0 } ) } \\ & { H _ { 1 } = \widetilde { H } _ { 1 } \Phi ( t _ { 1 } , t _ { 0 } ) = \left[ \begin{array} { c c } { 0 } & { 1 } \\ { 1 / 2 } & { 1 / 2 } \end{array} \right] \left[ \begin{array} { c c } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] = \left[ \begin{array} { c c } { 0 } & { 1 } \\ { 1 / 2 } & { 1 } \end{array} \right] } \end{array}
$$

$$
\begin{array} { r l } & { \tilde { \mathbf { x } } _ { 0 } = \left\{ \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] + \left[ \begin{array} { l l } { 0 } & { 1 / 2 } \\ { 1 } & { 1 } \end{array} \right] \left[ \begin{array} { l l } { 1 / 2 } & { 0 } \\ { 0 } & { 4 / 3 } \end{array} \right] \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 1 / 2 } & { 1 } \end{array} \right] \right\} ^ { - 1 } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \left\{ \left[ \begin{array} { l l } { 0 } & { 1 / 2 } \\ { 1 } & { 1 } \end{array} \right] \left[ \begin{array} { l l } { 1 / 2 } & { 0 } \\ { 0 } & { 4 / 3 } \end{array} \right] \left[ \begin{array} { l } { 6 } \\ { 4 } \end{array} \right] + \left[ \frac { 3 2 } { 2 } \right] \right\}  \\ & { \quad \quad \quad \quad \tilde { \mathbf { x } } _ { o } = \left[ \begin{array} { l l } { 4 / 3 } & { 2 / 3 } \\ { 2 / 3 } & { 1 7 / 6 } \end{array} \right] ^ { - 1 } \left[ \begin{array} { l } { 1 7 / 3 } \\ { 3 1 / 3 } \end{array} \right] } \\ & { \quad \quad \quad \tilde { \mathbf { x } } _ { o } = \left[ \begin{array} { l l } { 1 7 / 2 0 } & { - 1 / 5 } \\ { - 1 / 5 } & { 2 / 5 } \end{array} \right] \left[ \begin{array} { l } { 1 7 / 3 } \\ { 3 1 / 3 } \end{array} \right] } \\ & { \quad \quad \quad \quad \quad \tilde { \mathbf { x } } _ { 0 } = \left[ \begin{array} { l l } { 2 / 3 } & { - 1 / 5 } \end{array} \right] \left[ \begin{array} { l } { 1 7 / 3 } \\ { 3 1 / 3 } \end{array} \right] } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \tilde { \mathbf { x } } _ { 0 } = \left[ \begin{array} { l } { 2 / 3 } \\ { 3 } \end{array} \right] } \end{array}
$$

Note that

$$
P _ { 0 } = \left[ \begin{array} { c c } { { \ 1 7 / 2 0 } } & { { \ - 1 / 5 } } \\ { { - 1 / 5 } } & { { \ 2 / 5 } } \end{array} \right] .
$$

The correlation matrix, computed from $P _ { 0 }$ , has standard deviations on the diagonal and correlation coefficient s for the lower off-diagonal terms,

$$
\left[ \begin{array} { c } { \sigma _ { x _ { 1 } } } \\ { \rho _ { x _ { 1 } x _ { 2 } } \sigma _ { x _ { 2 } } } \end{array} \right] = \left[ \begin{array} { c c } { \phantom { - } . 9 2 2 } \\ { - . 3 4 3 } & { . 6 3 2 } \end{array} \right] .
$$

(2) Sequential Processor

$$
\begin{array} { r l } & { \hat { \mathbf { x } } _ { 1 } = \overline { { \mathbf { x } } } _ { 1 } + \overline { { P } } _ { 1 } \widetilde { H } _ { 1 } ^ { T } ( W _ { 1 } ^ { - 1 } + \widetilde { H } _ { 1 } \overline { { P } } _ { 1 } \widetilde { H } _ { 1 } ^ { T } ) ^ { - 1 } \big ( \mathbf { y } _ { 1 } - \widetilde { H } _ { 1 } \overline { { \mathbf { x } } } _ { 1 } \big ) } \\ & { \qquad = \overline { { \mathbf { x } } } _ { 1 } + K _ { 1 } \big ( \mathbf { y } _ { 1 } - \widetilde { H } _ { 1 } \overline { { \mathbf { x } } } _ { 1 } \big ) } \end{array}
$$

From the problem definition

$$
{ \begin{array} { l } { { \overline { { \mathbf { x } } } } _ { 1 } = \Phi ( t _ { 1 } , t _ { 0 } ) { \overline { { \mathbf { x } } } } _ { o } } \\ { = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { 3 } \\ { 2 } \end{array} \right] } = { \left[ \begin{array} { l } { 5 } \\ { 2 } \end{array} \right] } } \end{array} }
$$

$$
{ \begin{array} { r l } & { { \overline { { P } } } _ { 1 } = \Phi ( t _ { 1 } , t _ { 0 } ) { \overline { { P } } } _ { o } \Phi ^ { T } ( t _ { 1 } , t _ { 0 } ) } \\ & { \quad = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 1 } & { 1 } \end{array} \right] } = { \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 1 } \end{array} \right] } } \end{array} }
$$

$$
\overline { { P } } _ { 1 } \widetilde { H } _ { 1 } ^ { T } = \left[ \begin{array} { c c } { 2 } & { 1 } \\ { 1 } & { 1 } \end{array} \right] \left[ \begin{array} { c c } { 0 } & { 1 / 2 } \\ { 1 } & { 1 / 2 } \end{array} \right] = \left[ \begin{array} { c c } { 1 3 / 2 } \\ { 1 } & { 1 } \end{array} \right]
$$

$$
\widetilde { H } _ { 1 } \overline { { { P } } } _ { 1 } \widetilde { H } _ { 1 } ^ { T } = \left[ \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { 1 / 2 } } & { { 1 / 2 } } \end{array} \right] \left[ \begin{array} { c c } { { 1 } } & { { 3 / 2 } } \\ { { 1 } } & { { 1 } } \end{array} \right] = \left[ \begin{array} { c c } { { 1 } } & { { 1 } } \\ { { 1 } } & { { 5 / 4 } } \end{array} \right]
$$

$$
\begin{array} { r l } & { ( W _ { 1 } ^ { - 1 } + \widetilde { H } _ { 1 } \overline { { P } } _ { 1 } \widetilde { H } _ { 1 } ^ { T } ) ^ { - 1 } = \left[ \left( \begin{array} { c c } { 2 } & { 0 } \\ { 0 } & { 3 / 4 } \end{array} \right) + \left( \begin{array} { c c } { 1 } & { 1 } \\ { 1 } & { 5 / 4 } \end{array} \right) \right] ^ { - 1 } } \\ & { \qquad = \left[ \begin{array} { c c } { 2 / 5 } & { - 1 / 5 } \\ { - 1 / 5 } & { 3 / 5 } \end{array} \right] } \end{array}
$$

$$
\begin{array} { r l } & { K _ { 1 } = \overline { { P } } _ { 1 } \widetilde { H } _ { 1 } ^ { T } ( W _ { 1 } ^ { - 1 } + \widetilde { H } _ { 1 } \overline { { P } } _ { 1 } \widetilde { H } _ { 1 } ^ { T } ) ^ { - 1 } } \\ & { \quad = \left[ 1 3 / 2 \right] \left[ \begin{array} { c c } { 2 / 5 } & { - 1 / 5 } \\ { - 1 / 5 } & { 3 / 5 } \end{array} \right] = \left[ \begin{array} { c c } { 1 / 1 0 } & { 7 / 1 0 } \\ { 1 / 5 } & { 2 / 5 } \end{array} \right] . } \end{array}
$$

With these results,

$$
\begin{array} { r l } &  \hat { \mathbf { x } } _ { 1 } = \left[ \begin{array} { l } { 5 } \\ { 2 } \end{array} \right] + \left[ \begin{array} { l l } { 1 / 1 0 } & { 7 / 1 0 } \\ { 1 / 5 } & { 2 / 5 } \end{array} \right] \left\{ \begin{array} { l } { \left[ 6 \right] - \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 1 / 2 } & { 1 / 2 } \end{array} \right] \left[ \begin{array} { l } { 5 } \\ { 2 } \end{array} \right] \right\} } \\ & { \quad = \left[ \begin{array} { l l } { 5 } \\ { 2 } \end{array} \right] + \left[ \begin{array} { l l } { 1 / 1 0 } & { 7 / 1 0 } \\ { 1 / 5 } & { 2 / 5 } \end{array} \right] \left[ \begin{array} { l } { 4 } \\ { 1 / 2 } \end{array} \right] } \\ & { \quad \hat { \mathbf { x } } _ { 1 } = \left[ \begin{array} { l } { 5 \frac { 3 } { 4 } } \\ { 3 } \end{array} \right] } \\ & { \quad P _ { 1 } = \left( I - K _ { 1 } \widetilde { H } _ { 1 } \right) \overline { { P } } _ { 1 } } \\ & { \quad = \left\{ \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] - \left[ \begin{array} { l l } { 7 / 2 0 } & { 9 / 2 0 } \\ { 1 / 5 } & { 2 / 5 } \end{array} \right] \right\} \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 1 } \end{array} \right] } \\ & { \quad P _ { 1 } = \left[ \begin{array} { l l } { 1 7 / 2 0 } & { 1 / 5 } \\ { 1 / 5 } & { 2 / 5 } \end{array} \right] . } \end{array} \end{array}
$$

(3) Map $\hat { \mathbf { x } } _ { o }$ obtained with the batch processor to $t _ { 1 }$ .

$$
{ \begin{array} { r l } & { { \hat { \mathbf { x } } } _ { 1 } = \Phi ( t _ { 1 } , t _ { 0 } ) { \hat { \mathbf { x } } } _ { 0 } } \\ & { \quad = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { 2 { \frac { 3 } { 4 } } } \\ { 3 } \end{array} \right] } } \\ & { \quad = { \left[ \begin{array} { l } { 5 { \frac { 3 } { 4 } } } \\ { 3 } \end{array} \right] } } \end{array} }
$$

Hence, the batch and sequential estimates and covariances at $t _ { 1 }$ agree.

Note that $P _ { 0 }$ from the batch processor may be mapped to $t _ { 1 }$ by

$$
\begin{array} { c } { P _ { 1 } = \Phi ( t _ { 1 } , t _ { 0 } ) P _ { 0 } \Phi ^ { T } ( t _ { 1 } , t _ { 0 } ) } \\ { = \left[ \begin{array} { c c } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { c c } { 1 7 / 2 0 } & { - 1 / 5 } \\ { - 1 / 5 } & { 2 / 5 } \end{array} \right] \left[ \begin{array} { c c } { 1 } & { 0 } \\ { 1 } & { 1 } \end{array} \right] } \end{array}
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/f8cccd098e2cbecc543102d68a35cd22304a95c277c639fbe667d37a2bad0de8.jpg)  
Figure 4.8.2: Spring-mass system.

$$
P _ { 1 } = \left[ { \begin{array} { r r } { 1 7 / 2 0 } & { 1 / 5 } \\ { 1 / 5 } & { 2 / 5 } \end{array} } \right] ,
$$

which agrees with the sequential processor results.

# 4.8.2 SPRING-MASS PROBLEM

A block of mass $m$ is attached to two parallel vertical walls by two springs as shown in Fig. 4.8.2. $k _ { 1 }$ and $k _ { 2 }$ are the spring constants. $h$ is the height of the position $P$ on one of the walls, from which the distance, $\rho$ , and the rate of change of distance of the block from $P$ , $\dot { \rho }$ , can be observed.

Let the horizontal distances be measured with respect to the point $O$ where the line $O P$ , the lengths of the springs, and the center of mass of the block are all assumed to be in the same vertical plane. Then, if $\bar { x }$ denotes the position of the block at static equilibrium, the equation of motion of the block is given by

$$
{ \ddot { x } } \equiv { \dot { v } } = - ( k _ { 1 } + k _ { 2 } ) ( x - { \bar { x } } ) / m .
$$

Let

$$
\omega ^ { 2 } = ( k _ { 1 } + k _ { 2 } ) / m .
$$

Since $\bar { x }$ is an arbitrary constant we have set it to zero so that Eq. (4.8.1) can be

written as

$$
\dot { v } + \omega ^ { 2 } x = 0 .
$$

Consider the problem of estimating the position and the velocity of the block with respect to the reference point $O$ , by using the range and range-rate measurements of the block from the point, $P$ . In order to formulate this problem mathematically, the estimation state vector is taken as ${ \bf X } ^ { T } = [ x \textbf { } v ]$ . Then the system dynamics are represented by

$$
{ \dot { \bf X } } = F ( { \bf X } , t ) = \left[ { \dot { x } } \right] = \left[ { v \atop - \omega ^ { 2 } x } \right] = \left[ \begin{array} { c c } { 0 } & { 1 } \\ { - \omega ^ { 2 } } & { 0 } \end{array} \right] \ \left[ \begin{array} { c } { x } \\ { v } \end{array} \right] \ .
$$

The observation vector is

$$
\mathbf { Y } ( t ) = \left[ \rho \atop \dot { \rho } \right] .
$$

Also,

$$
G ( \mathbf { X } ^ { * } , t ) = \left[ \rho \atop \dot { \rho } \right] ^ { * } = \left[ \sqrt { x ^ { 2 } + h ^ { 2 } } \right] ^ { * } .
$$

The system parameters are $m , k _ { 1 } , k _ { 2 }$ (from dynamics), and $h$ (from geometry).

Note that the state propagation equation, Eq. (4.8.3), is linear in the state variables $\mathbf { x }$ and $v$ . However, the observation-state equation, Eq. (4.8.4), is nonlinear. Hence, the system must be linearized about a reference solution. Accordingly, let

$$
\delta \mathbf { X } ( t ) = { \bigg [ } x ( t ) - x ^ { * } ( t ) { \bigg ] }
$$

and we will solve for $\delta \hat { \mathbf X } ( t _ { 0 } ) \equiv \delta \hat { \mathbf X } _ { 0 }$ and

$$
\begin{array} { c } { \delta \dot { \mathbf { X } } ( t ) = A ( t ) \delta \mathbf { X } ( t ) } \\ { \mathbf { y } ( t ) = \widetilde { H } \delta \mathbf { X } ( t ) } \end{array}
$$

where

$$
\mathbf { y } ( t ) = \mathbf { Y } ( t ) - G ( \mathbf { X } ^ { * } , t )
$$

$$
\begin{array} { r l } & { \boldsymbol { A } ( t ) = \left[ \begin{array} { c c } { 0 } & { 1 } \\ { - \omega ^ { 2 } } & { 0 } \end{array} \right] } \\ & { \boldsymbol { \widetilde { H } } = \left[ \begin{array} { c c } { \frac { \boldsymbol { x } } { \rho } } & { 0 } \\ { \left( \frac { \boldsymbol { v } } { \rho } - \frac { \boldsymbol { x } ^ { 2 } { \boldsymbol { v } } } { \rho ^ { 3 } } \right) } & { \frac { \boldsymbol { x } } { \rho } } \end{array} \right] . } \end{array}
$$

The solution to Eq. (4.8.3) is given by (assuming $t _ { 0 } = 0$ )

$$
\begin{array} { r l } & { x ( t ) = x _ { 0 } \cos \omega t + \frac { v _ { 0 } } { \omega } \sin \omega t } \\ & { v ( t ) = v _ { 0 } \cos \omega t - x _ { 0 } \omega \sin \omega t . } \end{array}
$$

Hence, we could determine the state transition matrix by differentiating Eq. (4.8.5),

$$
\Phi ( t , 0 ) = \frac { \partial { \bf X } ( t ) } { \partial { \bf X } ( t _ { 0 } ) } .
$$

Alternatively, the solution to the variational equation

$$
{ \dot { \Phi } } ( t , 0 ) = A ( t ) \Phi ( t , 0 ) , \quad \Phi ( 0 , 0 ) = I
$$

is given by

$$
\begin{array} { r } { \Phi ( t , 0 ) = \left[ \begin{array} { c c } { \cos \omega t } & { \frac { 1 } { \omega } \sin \omega t } \\ { - \omega \sin \omega t } & { \cos \omega t } \end{array} \right] } \end{array}
$$

hence,

$$
\begin{array} { r } { \delta \mathbf { X } ( t ) = \Phi ( t , 0 ) \delta \mathbf { X } ( t _ { 0 } ) . } \end{array}
$$

Also,

$$
H _ { i } = \widetilde { H } _ { i } \Phi ( t _ { i } , 0 ) .
$$

Perfect observations were simulated for a period of 10 seconds at one-second intervals (see Table 4.8.1), assuming the following values for the system parameters and the initial condition for the state parameters:

Table 4.8.1: Observation Data   

<table><tr><td>Time (s)</td><td>p(m)</td><td>p(m/s)</td></tr><tr><td></td><td></td><td></td></tr><tr><td>0.00</td><td>6.1773780845922</td><td>0</td></tr><tr><td>1.00</td><td>5.56327661282686</td><td>1.31285863495514</td></tr><tr><td>2.00</td><td>5.69420161397342</td><td>-1.54488114381612</td></tr><tr><td>3.00</td><td>6.15294262127432</td><td>0.534923988815733</td></tr><tr><td>4.00</td><td>5.46251322092491</td><td>0.884698415328368</td></tr><tr><td>5.00</td><td>5.83638064328625</td><td>-1.56123248918054</td></tr><tr><td>6.00</td><td>6.08236452736002</td><td>1.00979943157547</td></tr><tr><td>7.00</td><td>5.40737619817037</td><td>0.31705117039215</td></tr><tr><td>8.00</td><td>5.97065615746125</td><td>-1.37453070975606</td></tr><tr><td>9.00</td><td>5.97369258835895</td><td>1.36768169443236</td></tr><tr><td>10.00</td><td>5.40669060248179</td><td>-0.302111588503166</td></tr></table>

$$
\begin{array} { r l } & { k _ { 1 } = 2 . 5 ~ \mathrm { N / m } } \\ & { k _ { 2 } = 3 . 7 ~ \mathrm { N / m } } \\ & { m = 1 . 5 ~ \mathrm { k g } } \\ & { ~ h = 5 . 4 ~ \mathrm { m } } \\ & { x _ { 0 } = 3 . 0 ~ \mathrm { m } } \\ & { v _ { 0 } = 0 . 0 ~ \mathrm { m / s } . } \end{array}
$$

The 11 perfect observations were processed using the batch processor with the following a priori values:

$$
\mathbf { X } _ { 0 } ^ { * } = \left[ \begin{array} { c } { 4 . 0 } \\ { 0 . 2 } \end{array} \right] , \overline { { { P } } } _ { 0 } = \left[ \begin{array} { c c } { 1 0 0 0 } & { 0 } \\ { 0 } & { 1 0 0 } \end{array} \right] , \mathrm { a n d } \delta \overline { { \mathbf { X } } } _ { 0 } = \left[ \begin{array} { c } { 0 } \\ { 0 } \end{array} \right] .
$$

The computed observations were calculated with the exact values of $k _ { 1 } , k _ { 2 }$ , $m$ , and $h$ from Eq. (4.8.6); $\mathbf { X } _ { 0 } ^ { * }$ was used for the values of $x _ { 0 } ^ { * }$ and $v _ { 0 } ^ { * }$ .

The least squares solution for $\delta { \bf X } _ { 0 }$ is given by (assuming that $W _ { i } ^ { - 1 } = R _ { i } = I )$

$$
\delta { \hat { \mathbf { X } } } _ { 0 } = \left( \sum _ { i = 0 } ^ { 1 0 } H _ { i } ^ { T } H _ { i } + { \overline { { P } } } _ { 0 } ^ { - 1 } \right) ^ { - 1 } \left( \sum _ { i = 0 } ^ { 1 0 } H _ { i } ^ { T } y _ { i } + { \overline { { P } } } _ { 0 } ^ { - 1 } \delta { \overline { { \mathbf { X } } } } _ { 0 } \right)
$$

and the best estimate of the initial state is

$$
\hat { \mathbf { X } } _ { 0 } = \mathbf { X } _ { 0 } ^ { * } + \delta \hat { \mathbf { X } } _ { 0 } .
$$

After each iteration shift the a priori state deviation vector so that

$$
( \delta { \bar { \mathbf { X } } } _ { 0 } ) _ { n } = ( \delta { \bar { \mathbf { X } } } _ { 0 } ) _ { n - 1 } - ( \delta { \hat { \mathbf { X } } } _ { 0 } ) _ { n - 1 }
$$

following Eq. (4.6.4) and Fig. 4.6.1.

After four iterations the estimate for the state at $t = 0$ is

$$
\left[ \hat { \bf X } _ { 0 } \right] = \left[ \begin{array} { l } { \hat { x } _ { 0 } } \\ { \hat { v } _ { 0 } } \end{array} \right] = \left[ \begin{array} { l } { 3 . 0 0 0 1 9 \mathrm { m } } \\ { 1 . 1 8 1 8 1 \times 1 0 ^ { - 3 } \mathrm { m } / \mathrm { s } } \end{array} \right] .
$$

The computed standard deviations and correlation coefficient are

$$
\sigma _ { x _ { 0 } } = 0 . 4 1 1 \mathrm { ~ m } , \sigma _ { v _ { 0 } } = 0 . 7 6 5 \mathrm { ~ m } / \mathrm { s } , \mathrm { a n d } \rho _ { x _ { 0 } v _ { 0 } } = 0 . 0 4 0 6 . \mathrm { ~ }
$$

The mean of the residuals is $\rho _ { \mathrm { m e a n } } = - 4 . 3 0 \times 1 0 ^ { - 5 } \mathrm { m }$ , $\dot { \rho } _ { \mathrm { m e a n } } = - 1 . 7 6 \times 1 0 ^ { - 6 }$ $\mathrm { m } / \mathrm { s }$ . The RMS of residuals is $\rho _ { R M S } = 1 . 1 6 \times 1 0 ^ { - 4 } \mathrm { m } , \dot { \rho } _ { \mathrm { R M S } } = 4 . 6 6 \times 1 0 ^ { - 4 } \mathrm { m } / \mathrm { s }$ .

# 4.9 STATE NOISE COMPENSATION ALGORITHM

In addition to the effects of the nonlinearities, the effects of errors in the dynamical model can lead to divergence in the estimate. See, for example, the discussion in Schlee et al., (1967) . As pointed out previously, for a sufficiently large number of observations the elements of the covariance matrix $P _ { k }$ will asymptotically approach zero and the estimation algorithm will be insensitive to any further observations. This condition can lead to filter divergence. One approach to preventing this divergence is to recognize that the linearized equations for propagating the estimate of the state are in error and to compensate for this by assuming that the error in the linearized dynamics can be approximated by process noise.

The state dynamics of a linear system under the influence of process noise are described by

$$
{ \dot { \mathbf { x } } } ( t ) = A ( t ) \mathbf { x } ( t ) + B ( t ) \mathbf { u } ( t )
$$

where $A ( t )$ and $B ( t )$ are known functions of time. The vector ${ \bf \delta u } ( t )$ is dimension $m \times 1$ , and $B ( t )$ is an $n \times m$ matrix. The functional form of ${ \bf \delta u } ( t )$ can include a number of processes, including constant, piecewise constant, correlated, or white noise. In the following discussion, the function ${ \bf \delta u } ( t )$ (called state or process noise) is assumed to be a white noise process with

$$
\begin{array} { c } { E [ { \mathbf { u } ( t ) } ] = 0 } \\ { E [ { \mathbf { u } ( t ) \mathbf { u } ^ { T } ( \tau ) } ] = Q ( t ) \delta ( t - \tau ) } \end{array}
$$

where $\delta ( t - \tau )$ is the Dirac Delta, and $Q$ is called the process noise covariance matrix.

The algorithm that results from the assumption that ${ \bf \delta u } ( t )$ is white noise with known covariance is known as State Noise Compensation (SNC). The use of more sophisticated models such as the process to compensate for state and/or measurement model errors generally is referred to as Dynamic Model Compensation (DMC). In the case of DMC, process noise parameters are often included in the state vector to be estimated. Appendix F provides more details on SNC and DMC.

The solution of Eq. (4.9.1) can be obtained by the method of variation of parameters. The homogeneous equation is given by

$$
\dot { \mathbf { x } } ( t ) = A ( t ) \mathbf { x } ( t )
$$

which, as previously noted, has a solution of the form

$$
\begin{array} { r } { { \bf x } ( t ) = \Phi ( t , t _ { 0 } ) { \bf C } _ { 0 } . } \end{array}
$$

The method of variation of parameters selects $\mathbf { C } _ { 0 }$ as a function of time so that

$$
\mathbf { x } ( t ) = \Phi ( t , t _ { 0 } ) \mathbf { C } ( t ) .
$$

It follows then that

$$
\dot { { \mathbf x } } ( t ) = \dot { \Phi } ( t , t _ { 0 } ) { \mathbf C } ( t ) + \Phi ( t , t _ { 0 } ) \dot { { \mathbf C } } ( t ) .
$$

Substituting Eq. (4.9.6) into Eq. (4.9.1) yields

$$
{ \dot { \Phi } } ( t , t _ { 0 } ) \mathbf { C } ( t ) + \Phi ( t , t _ { 0 } ) { \dot { \mathbf { C } } } ( t ) = A ( t ) \mathbf { x } ( t ) + B ( t ) \mathbf { u } ( t ) .
$$

Recall that

$$
\dot { \Phi } ( t , t _ { 0 } ) = A ( t ) \Phi ( t , t _ { 0 } ) .
$$

Substituting Eq. (4.9.8) into Eq. (4.9.7) and using Eq. (4.9.5) reduces Eq. (4.9.7) to

$$
\Phi ( t , t _ { 0 } ) \dot { \mathbf { C } } ( t ) = B ( t ) \mathbf { u } ( t ) .
$$

Hence,

$$
\dot { { \bf C } } ( t ) = \Phi ^ { - 1 } ( t , t _ { 0 } ) B ( t ) { \bf u } ( t ) .
$$

Integrating Eq. (4.9.10) yields

$$
\mathbf { C } ( t ) = \mathbf { C } _ { 0 } + \int _ { t _ { 0 } } ^ { t } \Phi ^ { - 1 } ( \tau , t _ { 0 } ) B ( \tau ) \mathbf { u } ( \tau ) d \tau .
$$

Substituting Eq. (4.9.11) into Eq. (4.9.5) results in

$$
\mathbf { x } ( t ) = \Phi ( t , t _ { 0 } ) \mathbf { C } _ { 0 } + \int _ { t _ { 0 } } ^ { t } \Phi ( t , t _ { 0 } ) \Phi ^ { - 1 } ( \tau , t _ { 0 } ) B ( \tau ) \mathbf { u } ( \tau ) d \tau .
$$

Using the properties of the transition matrix, we may write

$$
\Phi ( t , t _ { 0 } ) \Phi ^ { - 1 } ( \tau , t _ { 0 } ) = \Phi ( t , t _ { 0 } ) \Phi ( t _ { 0 } , \tau ) = \Phi ( t , \tau ) .
$$

At $t = t _ { 0 }$ , $\mathbf { x } ( t _ { 0 } ) = \mathbf { x } _ { 0 }$ ; hence, Eq. (4.9.12) can be used to determine that ${ \bf C } _ { 0 } = { }$ $\mathbf { x } _ { \mathrm { 0 } }$ . With these results, Eq. (4.9.12) can be written as

$$
{ \bf x } ( t ) = \Phi ( t , t _ { 0 } ) { \bf x } _ { 0 } + \int _ { t _ { 0 } } ^ { t } \Phi ( t , \tau ) B ( \tau ) { \bf u } ( \tau ) d \tau .
$$

Equation (4.9.14) is the general solution for the inhomogeneous Eq. (4.9.1) and indicates how the true state propagates under the influence of process noise.

The equations for propagating the state estimate $\hat { \mathbf { x } } ( t _ { k - 1 } )$ to the next observation time, $t _ { k }$ , are obtained by recalling that

$$
\begin{array} { r } { \overline { { \mathbf { x } } } ( t ) = E [ \mathbf { x } ( t ) | \mathbf { y } _ { k - 1 } ] \quad \mathrm { f o r } \quad t \geq t _ { k - 1 } ; } \end{array}
$$

that is, the expected value of ${ \bf x } ( t )$ given observations through $t _ { k - 1 }$ . Also, because we have observations through $t _ { k - 1 }$

$$
\overline { { \mathbf { x } } } ( t _ { k - 1 } ) = \hat { \mathbf { x } } ( t _ { k - 1 } ) .
$$

Differentiating Eq. (4.9.15) and using Eq. (4.9.1) gives

$$
\begin{array} { r l } & { \dot { \overline { { \mathbf { x } } } } ( t ) = E \left[ \dot { \mathbf { x } } ( t ) | \mathbf { y } _ { k - 1 } \right] } \\ & { \qquad = E \left[ \left\{ A ( t ) \mathbf { x } ( t ) + B ( t ) \mathbf { u } ( t ) \right\} | \mathbf { y } _ { k - 1 } \right] } \\ & { \qquad = A ( t ) E \left[ \mathbf { x } ( t ) | \mathbf { y } _ { k - 1 } \right] . } \end{array}
$$

Since $E [ \mathbf { u } ( t ) ] = 0$ , it follows then that

$$
\dot { \mathbf { x } } ( t ) = \boldsymbol { A } ( t ) \overline { { \mathbf { x } } } ( t )
$$

with initial conditions $\overline { { \mathbf { x } } } ( t _ { k - 1 } ) = \hat { \mathbf { x } } ( t _ { k - 1 } )$ . In Eq. (4.9.17), the assumption has been made that the state noise ${ \bf \delta u } ( t )$ has zero mean and is independent of the observations,

$$
E [ { \bf u } ( t ) | { \bf y } _ { k - 1 } ] = E [ { \bf u } ( t ) ] = 0 .
$$

Hence, if the mean of the process noise is zero, $\begin{array} { r } { ( E [ \mathbf { u } ( t ) ] = 0 , } \end{array}$ ), then the equation for propagating the state estimate is the same as without process noise,

$$
\overline { { \mathbf { x } } } ( t ) = \Phi ( t , t _ { k - 1 } ) \hat { \mathbf { x } } _ { k - 1 } .
$$

One could derive a solution for the case where the mean is nonzero. In the case where $E [ \mathbf { u } ( t ) ] = \overline { { \mathbf { u } } }$ , the solution would be obtained by applying the expectation operator to Eq. (4.9.14) to yield

$$
\overline { { { \bf x } } } ( t ) = \boldsymbol \Phi ( t , t _ { k - 1 } ) \hat { \bf x } _ { k - 1 } + \Gamma ( t _ { k } , t _ { k - 1 } ) \overline { { { \bf u } } }
$$

where $\Gamma ( t _ { k } , t _ { k - 1 } )$ is defined by Eq. (4.9.47).

The equation for propagation of the estimation error covariance matrix is obtained by using the definition for $\overline { { P } } ( t )$ , given by

$$
\overline { { P } } ( t ) = E [ ( \bar { \mathbf { x } } ( t ) - \mathbf { x } ( t ) ) ( \overline { { \mathbf { x } } } ( t ) - \mathbf { x } ( t ) ) ^ { T } | \mathbf { y } _ { k - 1 } ] \ t \geq t _ { k - 1 } .
$$

Let

$$
\Delta \mathbf { x } ( t ) \equiv \overline { { \mathbf { x } } } ( t ) - \mathbf { x } ( t ) .
$$

Then

$$
\overline { { P } } ( t ) = E [ \Delta \mathbf x \Delta \mathbf x ^ { T } | \mathbf y _ { k - 1 } ]
$$

and differentiating $\overline { { P } } ( t )$ yields

$$
\begin{array} { l } { \displaystyle { \dot { \overline { { P } } } ( t ) = E \left[ \frac { d } { d t } \Delta \mathbf { x } \Delta \mathbf { x } ^ { T } | \mathbf { y } _ { k - 1 } \right] } } \\ { \displaystyle { ~ = E \left[ \Delta \dot { \mathbf { x } } \Delta \mathbf { x } ^ { T } + \Delta \mathbf { x } \Delta \dot { \mathbf { x } } ^ { T } | \mathbf { y } _ { k - 1 } \right] . } } \end{array}
$$

From Eqs. (4.9.1) and (4.9.17)

$$
\begin{array} { l } { \Delta \dot { \mathbf { x } } ( t ) = \dot { \bar { \mathbf { x } } } ( t ) - \dot { \mathbf { x } } ( t ) } \\ { = A ( t ) \bar { \mathbf { x } } ( t ) - A ( t ) \mathbf { x } ( t ) - B ( t ) \mathbf { u } ( t ) . } \end{array}
$$

Hence,

$$
\Delta \dot { \mathbf { x } } ( t ) = A ( t ) \Delta \mathbf { x } ( t ) - B ( t ) \mathbf { u } ( t ) .
$$

Substituting Eq. (4.9.23) into Eq. (4.9.22) yields

$$
\begin{array} { r l } & { \dot { \overline { { P } } } ( t ) = E \left[ \left\{ ( A ( t ) \Delta \mathbf { x } - B ( t ) \mathbf { u } ( t ) ) \Delta \mathbf { x } ^ { T } + \Delta \mathbf { x } ( A ( t ) \Delta \mathbf { x } - B ( t ) \mathbf { u } ( t ) ) ^ { T } \right\} | \mathbf { y } _ { k - 1 } \right] } \\ & { \quad \quad = A ( t ) E \left[ \Delta \mathbf { x } \Delta \mathbf { x } ^ { T } | \mathbf { y } _ { k - 1 } \right] - B ( t ) E \left[ \mathbf { u } ( t ) \Delta \mathbf { x } ^ { T } | \mathbf { y } _ { k - 1 } \right] } \\ & { \quad \quad \quad + E \left[ \Delta \mathbf { x } \Delta \mathbf { x } ^ { T } | \mathbf { y } _ { k - 1 } \right] A ^ { T } ( t ) - E \left[ \Delta \mathbf { x } \mathbf { u } ^ { T } ( t ) | \mathbf { y } _ { k - 1 } \right] B ^ { T } ( t ) } \end{array}
$$

and using Eq. (4.9.21)

$$
\begin{array} { r l } & { \dot { \overline { { P } } } ( t ) = A ( t ) \overline { { P } } ( t ) + \overline { { P } } ( t ) A ^ { T } ( t ) - B ( t ) E \left[ \mathbf { u } ( t ) \Delta \mathbf { x } ^ { T } | \mathbf { y } _ { k - 1 } \right] } \\ & { ~ - E \left[ \Delta \mathbf { x } \mathbf { u } ^ { T } ( t ) | \mathbf { y } _ { k - 1 } \right] B ^ { T } ( t ) . } \end{array}
$$

The solution for $\Delta { \bf x } ( t )$ now is needed to substitute into Eq. (4.9.24). Note that the solution for Eq. (4.9.23) is identical in form to the solution of Eq. (4.9.1) given by Eq. (4.9.14). Substituting Eq. (4.9.14) with appropriate subscripts into the last term of Eq. (4.9.24) yields

$$
\begin{array} { r l r } {  { E [ \Delta \mathbf { x } ( t ) \mathbf { u } ^ { T } ( t ) | \mathbf { y } _ { k - 1 } ] = E [ \Phi ( t , t _ { k - 1 } ) \Delta \mathbf { x } _ { k - 1 } \mathbf { u } ^ { T } ( t ) | \mathbf { y } _ { k - 1 } ] } } & { ( 4 . } & \\ & { } & { - E [ \int _ { t _ { k - 1 } } ^ { t } \Phi ( t , \tau ) B ( \tau ) \mathbf { u } ( \tau ) \mathbf { u } ^ { T } ( t ) d \tau | \mathbf { y } _ { k - 1 } ] } \end{array}
$$

where $t \geq t _ { k - 1 }$ . However,

$$
E \left[ \Delta \mathbf { x } _ { k - 1 } \mathbf { u } ^ { T } ( t ) | \mathbf { y } _ { k - 1 } \right] = 0
$$

since the forcing function ${ \bf \delta u } ( t )$ cannot influe nce the state at a time $t _ { k - 1 }$ for $t \geq$

$t _ { k - 1 }$ . Hence,

$$
E \left[ \Delta \mathbf { x } ( t ) \mathbf { u } ^ { T } ( t ) | \mathbf { y } _ { k - 1 } \right] = - \int _ { t _ { k - 1 } } ^ { t } \Phi ( t , \tau ) B ( \tau ) E \left[ \mathbf { u } ( \tau ) \mathbf { u } ^ { T } ( t ) d \tau | \mathbf { y } _ { k - 1 } \right] .
$$

From Eq. (4.9.2)

$$
E \left[ \mathbf { u } ( \tau ) \mathbf { u } ^ { T } ( t ) \right] = Q ( t ) \delta ( t - \tau )
$$

where $\delta ( t - \tau )$ is the Dirac delta function, which is defined to be zero everywhere except at $\tau = t$ , where it is infinite in such a way that the integral of $\delta ( t - \tau )$ across the singularity is unity; the Dirac delta function is defined by

$$
\delta ( t ) = \operatorname* { l i m } _ { \epsilon \to 0 } \delta _ { \epsilon } ( t )
$$

where

$$
\delta _ { \epsilon } ( t ) = \left\{ \begin{array} { l } { { 0 \left| t \right| > \frac { \epsilon } { 2 } } } \\ { { \frac { 1 } { \epsilon } \left| t \right| < \frac { \epsilon } { 2 } } } \end{array} . \right.
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/c0656d5fbbc52304c452e3c22d7a859b207d7912805973d710659946a122f91f.jpg)

This definit ion implies that

$$
\int _ { t _ { 1 } } ^ { t _ { 2 } } \delta ( t - \tau ) d \tau = \int _ { t - \epsilon / 2 } ^ { t + \epsilon / 2 } \delta ( t - \tau ) d \tau = 1 .
$$

Substituting Eq. (4.9.27) into Eq. (4.9.26) gives

$$
E \left[ \Delta \mathbf { x u } ^ { T } ( t ) | \mathbf { y } _ { k - 1 } \right] = - \int _ { t _ { k - 1 } } ^ { t } \Phi ( t , \tau ) B ( \tau ) Q ( t ) \delta ( t - \tau ) d \tau .
$$

Now

$$
\int _ { - \infty } ^ { \infty } \delta ( t - \tau ) d \tau = \operatorname* { l i m } _ { \epsilon \to 0 } \left[ \int _ { - \infty } ^ { t - \epsilon / 2 } 0 d \tau + \int _ { t - \epsilon / 2 } ^ { t + \epsilon / 2 } \frac 1 \epsilon d \tau + \int _ { t + \epsilon / 2 } ^ { \infty } 0 d \tau \right] .
$$

Hence, Eq. (4.9.28) becomes

$$
E \left[ \Delta \mathbf { x } ( t ) \mathbf { u } ^ { T } ( t ) | \mathbf { y } _ { k - 1 } \right] =
$$

$$
- \operatorname* { l i m } _ { \epsilon \to 0 } \left[ \int _ { t _ { k - 1 } } ^ { t - \epsilon / 2 } \ d 0 \ d d \tau + \int _ { t - \epsilon / 2 } ^ { t } \Phi ( t , \tau ) B ( \tau ) Q ( t ) ( \frac { 1 } { \epsilon } ) \ d { d \tau } \right] .
$$

Since $\epsilon$ is small, $\Phi ( t , \tau )$ and $B ( \tau )$ can be expanded in a Taylor series about $\Phi ( t , t )$ and $B ( t )$ , respectively. To this end, let

$$
\Phi ( t , \tau ) = \Phi ( t , t ) - \dot { \Phi } ( t , t ) ( t - \tau ) + O ( t - \tau ) ^ { 2 } .
$$

The second term of this equation is negative, since $t \geq \tau$ . Using the fact that $\Phi ( t , t ) = I$ and ${ \dot { \Phi } } ( t , t ) = { \bar { A } } ( t ) \Phi ( t , t )$ , we can write

$$
\Phi ( t , \tau ) = I - A ( t ) ( t - \tau ) + O ( t - \tau ) ^ { 2 } .
$$

Similarly we can expand $B ( \tau )$ :

$$
B ( \tau ) = B ( t ) - \frac { d } { d t } B ( t ) ( t - \tau ) + O ( t - \tau ) ^ { 2 } .
$$

Substituting Eqs. (4.9.31) and (4.9.32) into Eq. (4.9.29) yields

$$
\begin{array} { l } { { E \left[ \Delta { \mathbf { x u } } ^ { T } ( t ) | { \mathbf { y } } _ { k - 1 } \right] = - \displaystyle \operatorname* { l i m } _ { \epsilon \to 0 } \frac { 1 } { \epsilon } \int _ { t - \epsilon / 2 } ^ { t } \Bigg [ [ I - A ( t ) ( t - \tau ) ] [ B ( t ) Q ( t ) } } \\ { { \begin{array} { l } { { - \frac { d } { d t } B ( t ) Q ( t ) ( t - \tau ) ] + O ( t - \tau ) ^ { 2 } \Bigg ] d \tau } } \\ { { - \frac { \operatorname* { l i m } } { \epsilon \to 0 } \int _ { t - \epsilon / 2 } ^ { t } \left[ B ( t ) Q ( t ) - \frac { d } { d t } B ( t ) Q ( t ) ( t - \tau ) \right. } } \\ { { \left. - A ( t ) B ( t ) Q ( t ) ( t - \tau ) \right. } } \\ { { \left. + A ( t ) \frac { d } { d t } B ( t ) Q ( t ) ( t - \tau ) ^ { 2 } \right. } } \\ { { \left. + O ( t - \tau ) ^ { 2 } \right] \frac { d \tau } { \epsilon } . } } \end{array} } } \end{array}
$$

Ignoring higher order terms $( O ( t - \tau ) ^ { 2 } )$ in Eq. (4.9.33) results in

$$
\begin{array} { l } { { \displaystyle E [ \Delta { \bf x } ( t ) { \bf u } ^ { T } ( t ) | { \bf y } _ { k - 1 } ] = - \operatorname* { l i m } _ { \epsilon  0 } \frac { 1 } { \epsilon } \int _ { t - \epsilon / 2 } ^ { t } \Bigg \{ B ( t ) Q ( t ) - [ A ( t ) B ( t ) Q ( t )  } } \\ { { \displaystyle  + \frac { d } { d t }  B ( t ) Q ( t ) ] ( t - \tau ) \} d \tau } . } \end{array}
$$

Defining $\begin{array} { r } { K ( t ) = A ( t ) B ( t ) Q ( t ) + \frac { d } { d t } B ( t ) Q ( t ) } \end{array}$ and carrying out the integration

$$
\begin{array} { l } { { E [ \Delta { \bf x u } ^ { T } ( t ) | { \bf y } _ { k - 1 } ] = - \operatorname* { l i m } _ { \epsilon  0 } \frac 1 { \epsilon } [ B ( t ) Q ( t ) \tau - K ( t ) ( t \tau - \frac { \tau ^ { 2 } } { 2 } ) ] _ { t - \frac { \epsilon } { 2 } } ^ { t } } } \\ { { \mathrm { ~ } = - \operatorname* { l i m } _ { \epsilon  0 } \frac 1 { \epsilon } [ B ( t ) Q ( t ) \frac { \epsilon } { 2 } - K ( t ) ( \frac { \epsilon ^ { 2 } } { 8 } ) ] } } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle = - \operatorname* { l i m } _ { \epsilon  0 } [ \frac { B ( t ) Q ( t ) } 2 - \frac { K ( t ) } 8 \epsilon ] } } \\ { { \mathrm { } } } \\ { { \displaystyle = - \frac { B ( t ) Q ( t ) } 2 . } } \end{array}
$$

Substituting (4.9.34) and its transpose into (4.9.24) leads to

$$
\dot { \overline { { P } } } ( t ) = A ( t ) \overline { { P } } ( t ) + \overline { { P } } ( t ) A ^ { T } ( t ) + B ( t ) Q ( t ) B ^ { T } ( t ) .
$$

Equation (4.9.35) is an $n \times n$ matrix differential equation whose solution may be obtained by integrating with the initial conditions $\overline { { P } } ( t _ { k } ) = P _ { k }$ ; that is, the measurement update of the estimation error covariance matrix at $t _ { k }$ .

Equation (4.9.35) also can be expressed in integral form by using the method of variation of parameters. The homogeneous differential equation is given by

$$
\dot { \overline { { { P } } } } ( t ) = A ( t ) \overline { { { P } } } ( t ) + \overline { { { P } } } ( t ) A ^ { T } ( t ) ,
$$

which has the solution

$$
\overline { { P } } ( t ) = \Phi ( t , t _ { 0 } ) P _ { 0 } \Phi ^ { T } ( t , t _ { 0 } ) ,
$$

where for convenience, $t _ { k - 1 }$ has been replaced by $t _ { 0 }$ . Letting $P _ { 0 }$ become a function of time, Eq. (4.9.37) becomes

$$
\begin{array} { r l } & { \dot { \overline { { P } } } ( t ) = \dot { \Phi } ( t , t _ { 0 } ) P _ { 0 } { \Phi } ^ { T } ( t , t _ { 0 } ) } \\ & { \qquad + { \Phi } ( t , t _ { 0 } ) P _ { 0 } \dot { \Phi } ^ { T } ( t , t _ { 0 } ) + { \Phi } ( t , t _ { 0 } ) \dot { P } _ { 0 } { \Phi } ^ { T } ( t , t _ { 0 } ) . } \end{array}
$$

Equating Eqs. (4.9.35) and (4.9.38)

$$
\begin{array} { r l } & { A ( t ) \overline { { P } } ( t ) + \overline { { P } } ( t ) A ^ { T } ( t ) + B ( t ) Q ( t ) B ^ { T } ( t ) = \dot { \Phi } ( t , t _ { 0 } ) P _ { 0 } { \Phi } ^ { T } ( t , t _ { 0 } ) } \\ & { \qquad + \ \Phi ( t , t _ { 0 } ) P _ { 0 } \dot { \Phi } ^ { T } ( t , t _ { 0 } ) + \Phi ( t , t _ { 0 } ) \dot { P } _ { 0 } { \Phi } ^ { T } ( t , t _ { 0 } ) . \qquad ( } \end{array}
$$

However, from Eqs. (4.9.36) and (4.9.37)

$$
\begin{array} { r } { A ( t ) \overline { { P } } ( t ) + \overline { { P } } ( t ) A ^ { T } ( t ) = \dot { \Phi } ( t , t _ { 0 } ) P _ { 0 } { \Phi } ^ { T } ( t , t _ { 0 } ) } \\ { + \Phi ( t , t _ { 0 } ) P _ { 0 } \dot { \Phi } ^ { T } ( t , t _ { 0 } ) . } \end{array}
$$

Using Eq. (4.9.40), Eq. (4.9.39) reduces to

$$
\Phi ( t , t _ { 0 } ) \dot { P } _ { 0 } \Phi ^ { T } ( t , t _ { 0 } ) = B ( t ) Q ( t ) B ^ { T } ( t ) ,
$$

or

$$
\dot { P } _ { o } = \Phi ^ { - 1 } ( t , t _ { 0 } ) B ( t ) Q ( t ) B ^ { T } ( t ) \Phi ^ { - T } ( t , t _ { 0 } ) .
$$

Integrating Eq. (4.9.41) results in

$$
P _ { 0 } ( t ) - P _ { 0 } = \int _ { t _ { 0 } } ^ { t } \Phi ( t _ { 0 } , \tau ) B ( \tau ) Q ( \tau ) B ^ { T } ( \tau ) \Phi ^ { T } ( t _ { 0 } , \tau ) d \tau .
$$

Substituting Eq. (4.9.42) into (4.9.37)

$$
\begin{array} { r l r } {  { \overline { { P } } ( t ) = \Phi ( t , t _ { 0 } ) [ P _ { 0 } + \int _ { t _ { 0 } } ^ { t } \Phi ( t _ { 0 } \tau ) B ( \tau ) Q ( \tau ) B ^ { T } ( \tau ) \Phi ^ { T } ( t _ { 0 } , \tau ) d \tau ] \Phi ^ { T } ( t , t _ { 0 } ) } } \\ & { } & { \qquad = \Phi ( t , t _ { 0 } ) P _ { 0 } \Phi ^ { T } ( t , t _ { 0 } ) + \int _ { t _ { 0 } } ^ { t } \Phi ( t , t _ { 0 } ) \Phi ( t _ { 0 } , \tau ) B ( \tau ) Q ( \tau ) B ^ { T } ( \tau ) } \\ & { } & { \qquad \times \Phi ^ { T } ( t _ { 0 } , \tau ) \Phi ^ { T } ( t , t _ { 0 } ) d \tau . } \end{array}
$$

If we use

$$
\Phi ( t , t _ { 0 } ) \Phi ( t _ { 0 } \tau ) = \Phi ( t , \tau ) ,
$$

and

$$
\Phi ^ { T } ( t _ { 0 } , \tau ) \Phi ^ { T } ( t , t _ { 0 } ) = [ \Phi ( t , t _ { 0 } ) \Phi ( t _ { 0 } , \tau ) ] ^ { T } = \Phi ^ { T } ( t , \tau ) ,
$$

then after letting $t _ { 0 } = t _ { k - 1 }$ , Eq. (4.9.43) becomes

$$
\begin{array} { l } { \displaystyle \overline { { P } } ( t ) = \Phi ( t , t _ { k - 1 } ) P _ { k - 1 } \Phi ^ { T } ( t , t _ { k - 1 } ) } \\ { \displaystyle \qquad + \int _ { t _ { k - 1 } } ^ { t } \Phi ( t , \tau ) B ( \tau ) Q ( \tau ) B ^ { T } ( \tau ) \Phi ^ { T } ( t , \tau ) d \tau . } \end{array}
$$

Equations (4.9.19) and (4.9.44) are the equations for propagating the estimate of the state and the covariance for a continuous system. Since the orbit determination problem generally consists of a continuous system (the trajectory) subjected to discrete observations, it is convenient to use Eq. (4.9.19) to propagate the state estimate and to discretize Eq. (4.9.44). This can be accomplished by replacing $t$ with $t _ { k + 1 }$ and assuming that $\mathbf { u } ( \tau )$ is a white random sequence rather than a process. Thus, as indicated in Fig. 4.9.1, ${ \bf \delta u } ( t )$ is considered to be a piecewise constant function with covariance

$$
E [ \mathbf { u } ( t _ { i } ) \mathbf { u } ^ { T } ( t _ { j } ) ] = Q _ { i } \delta _ { i j } \delta _ { i j } = \left\{ { 1 i = j \atop 0 i \neq j } \right.
$$

where the Dirac delta function has been replaced by its analog for the discrete case, the Kroneker delta function. In the discrete case, Eq. (4.9.14) becomes

$$
\mathbf { x } ( t _ { k + 1 } ) \equiv \mathbf { x } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) \mathbf { x } _ { k } \ + \Gamma ( t _ { k + 1 } , t _ { k } ) \mathbf { u } _ { k }
$$

where

$$
\Gamma ( t _ { k + 1 } , t _ { k } ) = \int _ { t _ { k } } ^ { t _ { k + 1 } } \Phi ( t _ { k + 1 } , \tau ) B ( \tau ) d \tau .
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/4dc9b7c24b54776aee43014d19a293d6d283bb12da83d90b52f1355bc73fa07b.jpg)  
Figure 4.9.1: A white random sequence.

$\Gamma ( t _ { k + 1 } , t _ { k } )$ is referred to as the process noise transition matrix, and Eq. (4.9.47) is an $n \times m$ quadrature since $\Phi ( t _ { k + 1 } , \tau )$ and $B ( \tau )$ are known functions. Using the definit ion of the estimation error covariance matrix

$$
\overline { { P } } _ { k + 1 } = E [ ( \overline { { \mathbf { x } } } _ { k + 1 } - { \mathbf { x } } _ { k + 1 } ) ( \overline { { \mathbf { x } } } _ { k + 1 } - { \mathbf { x } } _ { k + 1 } ) ^ { T } ]
$$

and substituting Eqs. (4.9.46) and (4.9.19) into (4.9.48) leads to

$$
\begin{array} { r } { \overline { { P } } _ { k + 1 } = E \Bigg \{ \left[ \Phi ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { x } } _ { k } - \Phi ( t _ { k + 1 } , t _ { k } ) \mathbf { x } _ { k } - \Gamma ( t _ { k + 1 } , t _ { k } ) \mathbf { u } _ { k } \right] } \\ { \times \left[ \Phi ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { x } } _ { k } - \Phi ( t _ { k + 1 } , t _ { k } ) \mathbf { x } _ { k } - \Gamma ( t _ { k + 1 } , t _ { k } ) \mathbf { u } _ { k } \right] ^ { T } \Bigg \} . } \end{array}
$$

Note that $E [ ( \widehat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ) \mathbf { u } _ { k } ^ { T } ] = 0$ ; that is, $\mathbf { u } _ { k }$ cannot affect the estimation error at $t _ { k }$ since a finite time must evolve for $\mathbf { u } _ { k }$ to affect the state. Finally, carrying out the expectation operation in Eq. (4.9.49) yields

$$
\overline { { P } } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) P _ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) + \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) .
$$

The estimation error covariance matrix $\overline { { P } } _ { k + 1 }$ can be obtained by integrating the differential equation for $\dot { \overline { P } }$ given by Eq. (4.9.35), or $\overline { { P } } _ { k + 1 }$ may be obtained by using the state and process noise transition matrices as indicated in Eq. (4.9.50). A comparison of Eq. (4.9.35) and Eq. (4.9.50) indicates the following:

1. Since $P ( t )$ is symmetric, only $n ( n + 1 ) / 2$ of the $n \times n$ system of equations represented by Eq. (4.9.35) must be integrated. However, the $n ( n + 1 ) / 2$ equations are coupled and must be integrated as a single first-order system of dimension $n ( n + 1 ) / 2$ .

2. The $n \times n$ system represented by Eq. (4.9.50) can be separated into an $n \times n$ system of differential equations for $\Phi$ and an $n \times m$ quadrature for

Γ. Furthermore, the $n \times n$ system of equations represented by the solution for $\Phi ( t _ { k + 1 } , t _ { k } )$ can be integrated as a sequence of $n \times 1$ column vectors.

The comparison between the two methods indicates that integration of fewer equations is required to obtain the solution for $\overline { { P } } ( t )$ with Eq. (4.9.35). However, the integration of these equations may be more difficult than the integration associated with the larger system represented by Eq. (4.9.50) since they are coupled.

The equations for determining $\hat { \bf x }$ using the sequential processing algorithm are unchanged whenever a zero-mean process noise is included. However, as has been shown, the equations that propagate the estimation error covariance matrix do change; that is, the first of Eq. (4.7.31) is replaced by Eq. (4.9.50). Generally, the batch processing algorithm is not used with process noise because mapping of the process noise effects from the observation times to the epoch time is cumbersome. It further results in a normal matrix with an observation weighting matrix that will be nondiagonal and whose dimension is equal to $m \times m$ , where $m$ is the total number of observations. Computation of the inverse of the normal matrix will be so cumbersome that the normal equation solution involving process noise in the data accumulation interval is impractical. For example, a one-day tracking period for the TOPEX/Poseidon satellite by the French tracking system, DORIS, typically yields 5000–7000 doppler observations.

The advantage of using the process noise compensated sequential estimation algorithm lies in the fact that the asymptotic value of $\overline { { P } } ( t )$ will approach a nonzero value determined by the magnitude of $Q ( t )$ . That is, for certain values of $Q ( t )$ , the increase in the state error covariance matrix $\overline { { P } } ( t )$ during the interval between observations will balance the decrease in the covariance matrix that occurs at the observation point. In this situation, the estimation procedure will always be sensitive to new observations.

The question of how to choose the process noise covariance matrix, $Q ( t )$ , is complex. In practice, it is often chosen as a simple diagonal matrix and its elements are determined by trial and error. Although this method can be effective for a particular estimation scenario, such a process noise matrix is not generally applicable to other scenarios. The dynamic evolution of the true states of parameters estimated in a filter typically is affected by stochastic processes that are not modeled in the filte r’s deterministic dynamic model. The process noise model is a characterization of these stochastic processes, and the process noise covariance matrix should be determined by this process noise model. Development of the process noise model will not be presented in depth here; however, extensive discussions are given by Cruickshank (1998), Ingram (1970), and Lichten (1990).

The Gauss-Markov process is used as a process noise model and will be introduced here. It is computationally well suited for describing unmodeled forces since it obeys Gaussian probability laws and is exponentially correlated in time.

# 4.9.1 THE GAUSS-MARKOV PROCESS

A first-or der Gauss-Markov process is often used for dynamic model compensation in orbit determination problems to account for unmodeled or inaccurately modeled accelerations acting on a spacecraft. A Gauss-Markov process is one that obeys a Gaussian probability law and displays the Markov property. The Markov property means that the probability density function at $t _ { n }$ given its past history at $t _ { n - 1 }$ , $t _ { n - 2 } , \ldots$ is equal to its probability density function at $t _ { n }$ given its value at $t _ { n - 1 }$ .

A Gauss-Markov process obeys a differential equation (often referred to as a Langevin equation) of the form

$$
\dot { \eta } ( t ) = - \beta \eta ( t ) + u ( t )
$$

where $u ( t )$ is white Gaussian noise with

$$
\begin{array} { c } { { E ( u ) = 0 } } \\ { { E \left[ u ( t ) u ( \tau ) \right] = \sigma ^ { 2 } \delta ( t - \tau ) } } \end{array}
$$

and

$$
\beta = \frac { 1 } { \tau } ,
$$

where $\tau$ is the time constant or correlation time (not the same as $\tau$ in Eq. (4.9.52)).

Equation (4.9.51) can be solved by the method of variation of parameters to yield

$$
\eta ( t ) = \eta ( t _ { 0 } ) e ^ { - \beta ( t - t _ { 0 } ) } + \int _ { t _ { 0 } } ^ { t } e ^ { - \beta ( t - \tau ) } u ( \tau ) d \tau .
$$

Hence, $\eta ( t )$ consists of a deterministic part and a random part. The autocorrelation function is (Maybeck, 1979)

$$
\begin{array} { l } { E \left[ { \eta ( t _ { j } ) \eta ( t _ { i } ) } \right] = e ^ { - \beta ( t _ { j } - t _ { i } ) } E \left[ { \eta ( t _ { i } ) \eta ( t _ { i } ) } \right] } \\ { \displaystyle ~ + E \left[ \left( \int _ { t _ { i } } ^ { t _ { j } } e ^ { - \beta ( t _ { j } - \tau ) } u ( \tau ) d \tau \right) \eta ( t _ { i } ) \right] } \\ { \displaystyle = e ^ { - \beta ( t _ { j } - t _ { i } ) } E \left[ \eta ( t _ { i } ) \eta ( t _ { i } ) \right] } \end{array}
$$

since the stochastic process represented by the integral consists of independent increments. The remaining expectation is the autocorrelation of $\eta ( t )$ at $t _ { i }$ :

$$
\begin{array} { l } { { \displaystyle E \left[ \eta ( t _ { i } ) \eta ( t _ { i } ) \right] \equiv \Psi ( t _ { i } , t _ { i } ) } } \\ { { \displaystyle \qquad = \eta ^ { 2 } ( t _ { 0 } ) e ^ { - 2 \beta ( t _ { i } - t _ { 0 } ) } + \frac { \sigma ^ { 2 } } { 2 \beta } \left( 1 - e ^ { - 2 \beta ( t _ { i } - t _ { 0 } ) } \right) } } \end{array}
$$

where $\sigma ^ { 2 }$ is the variance (strength) of the driving noise in Eq. (4.9.51). Using Eq. (4.9.55), equation (4.9.54) can then be written as

$$
E \left[ \eta ( t _ { j } ) \eta ( t _ { i } ) \right] = \Psi ( t _ { i } , t _ { i } ) e ^ { - \beta ( t _ { j } - t _ { i } ) } .
$$

This is important because it points out one of the salient characteristics of the first-order Gauss-Markov process; that is, its autocorrelation fades exponentially with the rate of the fade governed by the time constant, $\tau = 1 / \beta$ .

Equation (4.9.53) contains a stochastic integral that cannot, in general, be evaluated except in a statistical sense. The mean of the stochastic integral is zero since $E [ \mathbf { u } ( t ) ] = 0$ . Its variance can be shown to be (Myers, 1973)

$$
\frac { \sigma ^ { 2 } } { 2 \beta } \big ( 1 - e ^ { - 2 \beta ( t _ { j } - t _ { i } ) } \big ) .
$$

Because the stochastic integral is a Gaussian process it is uniquely defined by its mean and variance. Hence, if a function can be found with the same mean and variance it will be an equivalent process. Such a discrete process is given by

$$
L _ { k } \equiv u _ { k } \sqrt { \frac { \sigma ^ { 2 } } { 2 \beta } ( 1 - e ^ { - 2 \beta ( t _ { j } - t _ { i } ) } ) }
$$

where $u _ { k }$ is a discrete, Gaussian random sequence with mean and variance

$$
\begin{array} { r } { E [ u _ { k } ] = 0 , \ E [ u _ { k _ { i } } u _ { k _ { j } } ] = \delta _ { i j } . } \end{array}
$$

It is evident that $L _ { k }$ has the same mean and variance as the stochastic integral in Eq. (4.9.53); hence, the solution for $\eta ( t )$ is given by

$$
\begin{array} { l } { { \eta ( t _ { j } ) = e ^ { - \beta ( t _ { j } - t _ { i } ) } \eta ( t _ { i } ) } } \\ { { \qquad + u _ { k } ( t _ { i } ) \sqrt { \frac { \sigma ^ { 2 } } { 2 \beta } ( 1 - e ^ { - 2 \beta ( t _ { j } - t _ { i } ) } ) } } } \end{array}
$$

where $u _ { k } ( t _ { i } )$ is a random number chosen by sampling from a Gaussian density function with a mean of zero and variance of 1.

The degree of correlation of the random process $\eta ( t )$ is determined by the choice of $\sigma$ and $\beta$ . For a finite value of $\beta$ and $\sigma ^ { 2 } \simeq 0$ , Eq. (4.9.60) yields

$$
\eta ( t _ { j } ) = e ^ { - \beta ( t _ { j } - t _ { i } ) } \eta ( t _ { i } )
$$

and as $\beta$ becomes small, $\eta ( t _ { j } )  \eta ( t _ { i } )$ , a constant. For a finit e value of $\sigma$ and $\beta \simeq 0$ , Eq. (4.9.60) yields

$$
\eta ( t _ { j } ) = \eta ( t _ { i } ) + u _ { k } ( t _ { i } ) \sigma \sqrt { t _ { j } - t _ { i } } ;
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/1e527882dc4ed6d738db5dcc88362cb83daf4510e232655975fe7350dc462175.jpg)  
Figure 4.9.2: Gauss-Markov process for three time constants.

that is, a random walk process.

The term $\textstyle { \frac { \sigma ^ { 2 } } { 2 \beta } }$ represents the steady-state variance of $\eta ( t )$ , the variance after a large enough time so that any transients in $\eta ( t )$ have died out and it is in steady state.

With the proper choice of $\sigma$ and $\beta$ any number of time-correlated random functions can be generated. Figure 4.9.2 illustrates three histories of $\eta ( t )$ for $\beta = 0 . 0 0 1$ , 0.1, 1.0, and $\sigma = 1 . 0$ . Note that for $\beta = 1 0 ^ { - 3 }$ , $\eta ( t )$ is essentially constant. The shape of this curve can be varied by changing $\sigma$ or $\beta$ or both.

To use the Gauss-Markov process to account for unmodeled accelerations in the orbit determination procedure we may formulate the problem as follows. The equations of motion are

$$
{ \begin{array} { r l } { { \dot { \mathbf { r } } } = \mathbf { v } } & { } \\ { { \dot { \mathbf { v } } } } & { = \mathbf { \nabla } - { \frac { \mu \mathbf { r } } { r ^ { 3 } } } + \mathbf { f } ( t ) + \pmb { \eta } ( t ) } \\ { { \dot { \pmb { \eta } } } ( t ) } & { = \mathbf { \nabla } - \beta \pmb { \eta } ( t ) + \mathbf { u } ( t ) , } \end{array} }
$$

where $\begin{array} { r l r } { \textrm { -- } \frac { \mu \mathbf { r } } { r ^ { 3 } } + \mathbf { f } ( t ) } \end{array}$ represents the known accelerations and $\pmb { \eta } ( t )$ is a $3 \times 1$ vector of unknown accelerations. The procedure is to estimate the deterministic portion of $\pmb { \eta } ( t )$ and perhaps the associated time constants as part of the state vector. The random portion of $\pmb { \eta } ( t )$ contributes to the process noise covariance matrix $Q$ . For details on implementing this algorithm see Tapley and Ingram (1973), Ingram and Tapley (1974), Cruickshank (1998), Lichten (1990), or Goldstein et al. (2001).

An example of the use of process noise for SNC and DMC for a simple problem is given in Appendix F.

# 4.10 INFORMATION FILTER

A sequential estimation algorithm can be developed by propagating the information matrix, $\Lambda \equiv P ^ { - 1 }$ (Maybeck, 1979). This form of the filter offers some numerical properties with better characteristics than the covariance filter . Writing Eq. (4.7.3) in terms of the information matrix gives

$$
\begin{array} { r } { \{ \overline { { \Lambda } } _ { k } + \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } \} \hat { \mathbf { x } } _ { k } = \overline { { \Lambda } } _ { k } \overline { { \mathbf { x } } } _ { k } + \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \mathbf { y } _ { k } } \end{array}
$$

or

$$
\Lambda _ { k } \hat { \mathbf { x } } _ { k } = \overline { { \Lambda } } _ { k } \overline { { \mathbf { x } } } _ { k } + \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \mathbf { y } _ { k } .
$$

Recall that $\overline { { P } } _ { k + 1 }$ is expressed in terms of $P _ { k }$ by Eq. (4.9.50) and $\overline { { \mathbf { x } } } _ { k }$ is obtained by propagating $\hat { \mathbf { x } } _ { k - 1 }$ according to Eq. (4.9.19). The Schur identity is given by (see Appendix B)

$$
( A + B C ) ^ { - 1 } = A ^ { - 1 } - A ^ { - 1 } B ( I + C A ^ { - 1 } B ) ^ { - 1 } C A ^ { - 1 } .
$$

In Eq. (4.9.50) let

$$
\begin{array} { l } { A = \Phi \left( t _ { k + 1 } , t _ { k } \right) P _ { k } \Phi ^ { T } \left( t _ { k + 1 } , t _ { k } \right) } \\ { B = \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } } \\ { C = \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) . } \end{array}
$$

Then, for $Q _ { k }$ nonsingular, the Schur identity yields

$$
\begin{array} { r l } & { \overline { { \Lambda } } _ { k + 1 } = \overline { { P } } _ { k + 1 } ^ { - 1 } = M ( t _ { k + 1 } ) - M ( t _ { k + 1 } ) \Gamma ( t _ { k + 1 } , t _ { k } ) } \\ & { \qquad \times \left[ \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) M ( t _ { k + 1 } ) \Gamma ( t _ { k + 1 } , t _ { k } ) + Q _ { k } ^ { - 1 } \right] ^ { - 1 } } \\ & { \qquad \times \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) M ( t _ { k + 1 } ) } \end{array}
$$

where

$$
M ( t _ { k + 1 } ) = A ^ { - 1 } = \Phi ^ { T } ( t _ { k } , t _ { k + 1 } ) P _ { k } ^ { - 1 } \Phi ( t _ { k } , t _ { k + 1 } ) .
$$

If there is no process noise, Eq. (4.10.4) reduces to

$$
\overline { { \Lambda } } _ { k + 1 } = \overline { { P } } _ { k + 1 } ^ { - 1 } = M ( t _ { k + 1 } ) .
$$

Define

$$
\begin{array} { l } { L _ { k + 1 } \equiv M ( t _ { k + 1 } ) \Gamma ( t _ { k + 1 } , t _ { k } ) \qquad } \\ { \qquad \times \left[ \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) M ( t _ { k + 1 } ) \Gamma ( t _ { k + 1 } , t _ { k } ) + Q _ { k } ^ { - 1 } \right] ^ { - 1 } . } \end{array}
$$

In terms of $L _ { k + 1 }$ , Eq. (4.10.4) becomes

$$
\begin{array} { r } { \overline { { \Lambda } } _ { k + 1 } = M ( t _ { k + 1 } ) - L _ { k + 1 } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) M ( t _ { k + 1 } ) . } \end{array}
$$

The measurement update for $\Lambda _ { k + 1 }$ is obtained by inverting Eq. (4.7.4); that is,

$$
\Lambda _ { k + 1 } = \overline { { { \Lambda } } } _ { k + 1 } + \widetilde { H } _ { k + 1 } ^ { T } R _ { k + 1 } ^ { - 1 } \widetilde { H } _ { k + 1 } .
$$

Define the following quantities:

$$
\begin{array} { r l } & { \overline { { \mathbf { D } } } _ { k } \equiv \overline { { \Lambda } } _ { k } \overline { { \mathbf { x } } } _ { k } } \\ & { \hat { \mathbf { D } } _ { k } \equiv \Lambda _ { k } \hat { \mathbf { x } } _ { k } . } \end{array}
$$

The recursion relations for $\mathbf { D }$ are given by

$$
\overline { { \mathbf { D } } } _ { k + 1 } = \overline { { \Lambda } } _ { k + 1 } \overline { { \mathbf { x } } } _ { k + 1 } .
$$

Using Eq. (4.10.7),

$$
\begin{array} { r l } & { \mathbf { \overline { { D } } } _ { k + 1 } = \{ I - L _ { k + 1 } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) \} } \\ & { \qquad \times \ : \Phi ^ { T } ( t _ { k } , t _ { k + 1 } ) P _ { k } ^ { - 1 } \Phi ( t _ { k } , t _ { k + 1 } ) \mathbf { \overline { { x } } } _ { k + 1 } } \end{array}
$$

but $\hat { \mathbf { x } } _ { k } = \Phi ( t _ { k } , t _ { k + 1 } ) \overline { { \mathbf { x } } } _ { k + 1 }$ and $\hat { \mathbf { D } } _ { k } = P _ { k } ^ { - 1 } \hat { \mathbf { x } } _ { k }$ . Hence,

$$
\begin{array} { r } { \overline { { \mathbf { D } } } _ { k + 1 } = \left\{ I - L _ { k + 1 } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) \right\} \Phi ^ { T } ( t _ { k } , t _ { k + 1 } ) \hat { \mathbf { D } } _ { k } . } \end{array}
$$

Also, from Eq. (4.10.9) and the second of Eq. (4.10.1),

$$
\begin{array} { r } { \hat { \mathbf { D } } _ { k + 1 } = \Lambda _ { k + 1 } \hat { \mathbf { x } } _ { k + 1 } = \overline { { \mathbf { D } } } _ { k + 1 } + \widetilde { H } _ { k + 1 } ^ { T } R _ { k + 1 } ^ { - 1 } \mathbf { y } _ { k + 1 } . } \end{array}
$$

The procedure starts with $a$ priori values $\overline { { P } } _ { 0 }$ and $\overline { { \mathbf { x } } } _ { \mathrm { 0 } }$ . From these compute

$$
\begin{array} { r l } & { \overline { { \Lambda } } _ { 0 } = \overline { { P } } _ { 0 } ^ { - 1 } } \\ & { \overline { { \mathbf { D } } } _ { 0 } = \overline { { \Lambda } } _ { 0 } \overline { { \mathbf { x } } } _ { 0 } . } \end{array}
$$

Next compute $M _ { 1 } , L _ { 1 } , \overline { { { \Lambda } } } _ { 1 } , \overline { { { \bf D } } } _ { 1 } , \hat { \bf D } _ { 1 }$ , and $\Lambda _ { 1 }$ from Eqs. (4.10.5), (4.10.6), (4.10.7), (4.10.13), (4.10.14), and (4.10.8). Once $\Lambda _ { k }$ becomes nonsingular, its inverse can

be computed to obtain $P _ { k }$ and the optimal estimate of $\mathbf { x }$ can be computed from Eq. (4.10.10); that is,

$$
\hat { \mathbf { x } } _ { k } = P _ { k } \hat { \mathbf { D } } _ { k } .
$$

Time updates are given by Eqs. (4.10.5), (4.10.6), (4.10.7), and (4.10.13), with initial conditions given by Eq. (4.10.15). The measurement update is accomplished using Eqs. (4.10.8) and (4.10.14).

In summary, the covariance filter and the information filt er time and measurement updates are given by

Time Update— $\epsilon$ ovariance Filter

$$
\begin{array} { r l } & { \overline { { \mathbf { x } } } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) \widehat { \mathbf { x } } _ { k } } \\ & { \overline { { P } } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) P _ { k } \Phi ^ { T } \left( t _ { k + 1 } , t _ { k } \right) } \\ & { \qquad + \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) . } \end{array}
$$

Measurement Update— $\epsilon o$ variance Filter

$$
\begin{array} { r l } & { K _ { k + 1 } = \overline { { P } } _ { k + 1 } \widetilde { H } _ { k + 1 } ^ { T } ( R _ { k + 1 } + \widetilde { H } _ { k + 1 } \overline { { P } } _ { k + 1 } \widetilde { H } _ { k + 1 } ^ { T } ) ^ { - 1 } } \\ & { \widehat { \mathbf { x } } _ { k + 1 } = \overline { { \mathbf { x } } } _ { k + 1 } + K _ { k + 1 } ( \mathbf { y } _ { k + 1 } - \widetilde { H } _ { k + 1 } \overline { { \mathbf { x } } } _ { k + 1 } ) } \\ & { P _ { k + 1 } = ( I - K _ { k + 1 } \widetilde { H } _ { k + 1 } ) \overline { { P } } _ { k + 1 } . } \end{array}
$$

# Time Update—Inf ormation Filter

$$
\begin{array} { r l } & { M ( t _ { k + 1 } ) = \Phi ^ { T } ( t _ { k } , t _ { k + 1 } ) \Lambda _ { k } \Phi ( t _ { k } , t _ { k + 1 } ) } \\ & { \qquad L _ { k + 1 } = M ( t _ { k + 1 } ) \Gamma ( t _ { k + 1 } , t _ { k } ) } \\ & { \qquad \times [ \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) M ( t _ { k + 1 } ) \Gamma ( t _ { k + 1 } , t _ { k } ) } \\ & { \qquad + Q _ { k } ^ { - 1 } ] ^ { - 1 } } \\ & { \qquad { \overline { { \mathbf { D } } } _ { k + 1 } } = \left\{ I - L _ { k + 1 } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) \right\} } \\ & { \qquad \times \Phi ^ { T } ( t _ { k } , t _ { k + 1 } ) { \overline { { \mathbf { D } } } _ { k } } } \\ &  { \qquad { \overline { { \Lambda } } _ { k + 1 } } = { \overline { { P } } _ { k + 1 } ^ { - 1 } } = \left[ I - L _ { k + 1 } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) \right] } \\ & { \qquad \times M ( t _ { k + 1 } ) . } \end{array}
$$

Measurement Update—Information Filter

$$
\begin{array} { r l } & { \hat { \mathbf { D } } _ { k + 1 } = \overline { { \mathbf { D } } } _ { k + 1 } + \widetilde { H } _ { k + 1 } ^ { T } R _ { k + 1 } ^ { - 1 } \mathbf { y } _ { k + 1 } } \\ & { P _ { k + 1 } ^ { - 1 } = \Lambda _ { k + 1 } = \overline { { \Lambda } } _ { k + 1 } + \widetilde { H } _ { k + 1 } ^ { T } R _ { k + 1 } ^ { - 1 } \widetilde { H } _ { k + 1 } } \\ & { \hat { \mathbf { x } } _ { k + 1 } = \Lambda _ { k + 1 } ^ { - 1 } \hat { \mathbf { D } } _ { k + 1 } . } \end{array}
$$

We can initialize the information fil ter with $P _ { 0 } = \infty$ or with $P _ { 0 }$ singular, and obtain valid results for $\hat { \bf x }$ once $P _ { k }$ becomes nonsingular. The Cholesky Algorithm of Chapter 5 may be used to solve for $\hat { \bf x }$ . However, the solution for $\hat { \bf x }$ is not required by the algorithm and needs to be computed only when desired. The conventional sequential estimation algorithm fails in these cases. Also, as indicated in Section 4.7.1, the conventional sequential estimator can fail in the case where very accurate measurements are processed, which rapidly reduce the estimation error covariance matrix. This can be mitigated with the information filter.

Consider the example discussed in Section 4.7.1,

$$
\overline { { { P } } } _ { 0 } = \sigma ^ { 2 } I , \quad \sigma = 1 / \epsilon , \quad \widetilde { H } _ { 1 } = \big [ 1 \ \vdots \ \epsilon \big ] , \quad R = I
$$

where $\epsilon \ll 1$ and we assume that our computer word length is such that

$$
\begin{array} { c } { { 1 + \epsilon \neq 1 } } \\ { { 1 + \epsilon ^ { 2 } = 1 . } } \end{array}
$$

The objective is to find $P _ { 1 }$ ; that is, the estimation error covariance matrix after processing one observation using the information filt er. The information filter yields

$$
\begin{array} { r l } & { M _ { 1 } = \epsilon ^ { 2 } I } \\ & { \overline { { \Lambda } } _ { 1 } = M _ { 1 } } \\ & { \Lambda _ { 1 } = \overline { { \Lambda } } _ { 1 } + \widetilde { H } _ { 1 } ^ { T } R ^ { - 1 } \widetilde { H } _ { 1 } } \\ & { \quad = \epsilon ^ { 2 } I + \left[ \begin{array} { c c } { 1 } & { \epsilon } \\ { \epsilon } & { \epsilon ^ { 2 } } \end{array} \right] } \\ & { \Lambda _ { 1 } = P _ { 1 } ^ { - 1 } = \left[ \begin{array} { c c } { 1 } & { \epsilon } \\ { \epsilon } & { 2 \epsilon ^ { 2 } } \end{array} \right] } \end{array}
$$

and

$$
P _ { 1 } = \left[ { \begin{array} { c c } { 2 } & { - \sigma } \\ { - \sigma } & { \sigma ^ { 2 } } \end{array} } \right] .
$$

This is the same symmetric, positive definite result obtained from the batch processor and agrees with the exact solution to $O ( \epsilon )$ . Because we are accumulating the information matrix at each stage, the accuracy of the information filter should be comparable to that of the batch processor. Hence, the conventional covariance filter fails for this example, but the information filt er does not.

# 4.11 BATCH AND SEQUENTIAL ESTIMATION

As described in previous sections, two general categories of estimators are used, the batch processor and the sequential processor, both with distinct advantages and disadvantages. The batch formulation provides an estimate of the state at some chosen epoch using an entire batch or set of data. This estimate and its associated covariance matrix can then be mapped to other times. The sequential processor, on the other hand, provides an estimate of the state at each observation time based on observations up to that time. This solution and its associated covariance also can be mapped to another time.

In the sequential formulation without process noise, a mathematical equivalence can be shown between the batch and sequential algorithms; given the same data set, both algorithms produce the same estimates when the estimates are mapped to the same times. In the extended form of the sequential algorithm, where the reference orbit is updated at each observation time, the algorithms are not equivalent, but numerical experiments have shown a very close agreement.

Normally, the batch and sequential algorithm will need to be iterated to convergence, whereas the extended sequential will obtain near convergence in a single iteration. The sequential algorithm, unlike the batch, requires restarting a numerical integrator at each observation time. In general, the sequential processor is used in real-time applications supporting control or other decision functions and it is appropriate to incorporate some representation of the state noise to ensure that divergence does not occur. This implementation provides a means of compensating for various error sources in the processing of ground-based or onboard data. As indicated previously, inclusion of process noise in the batch algorithm substantially complicates the solution of the normal equations by increasing the dimensions of the normal matrix from $n$ (the number of state parameters) to $m$ (the number of observations).

# 4.12 OBSERVABILITY

The property of observability refers to the ability to apply an estimator to a particular system and obtain a unique estimate for all components of the state vector. As applied to orbital mechanics, the observability property refers to the ability to obtain a unique estimate of the spacecraft state as opposed to whether the satellite can be physically observed. Cases of unobservability rarely occur for properly formulated problems. However, these cases illustrate clearly the caution that must be exercised in applying an estimation algorithm to a particular problem. An unobservable parameter can best be illustrated by the following example.

Consider a satellite moving in an orbit about a perfectly spherical planet with a homogeneous mass distribution. Assuming no forces other than the gravitational attraction of the planet, which can be represented by a point mass, the orbit will be a conic section. Suppose a laser or radar range system exists on the surface of the planet capable of measuring to infinite precision the distance between the instrument and the satellite. Assuming the planet does not rotate and only a single range measuring system exists, the previously described estimators can be applied to the problem of estimating the state of the spacecraft at some appropriate time. Consider a single pass of the satellite over the station as shown in Fig. 4.11.1, where $\mathbf { R } _ { \mathbf { S } }$ is the station position vector, assumed known. Given a sequence of range measurements, $\rho _ { i }$ , as shown, an orbit could be determined from which the computed ranges match the measured values. However, a subtle problem exists because there is no change in the location of the tracking station relative to the orbit plane; hence, multiple solutions are possible—the same range history occurs for each orbit as we rotate the orbit’s angular momentum vector about $\mathbf { R } _ { \mathbf { S } }$ keeping $\alpha$ constant. This results in an infinite number of solutions that could have the same range measurement sequence. This circumstance leads to an ambiguity in the inclination, $i$ , and longitude of the ascending node, $\Omega$ . The difficulty is not alleviated by using multiple passes, since each pass would have the same geometry relative to the station. The possible multiple solutions will be manifested by a singular normal matrix $( H ^ { T } H )$ in the ordinary least squares formulation, regardless of the number of observations used.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/4d2d4efa4c3deb36c29797fc5cec87f74bdd410c22eecdba0ee4965cb056174d.jpg)  
Figure 4.11.1: Single-station range geometry.

A unique solution can be obtained if (1) $i$ or $\Omega$ is known and not estimated, resulting in five elements being estimated, or (2) an $a$ priori covariance matrix is assigned to the state indicative of knowledge of $i$ or $\Omega$ . The problem can be avoided by other techniques as well; for example, using angular data such as azimuth and elevation or by using a second ranging station. However, this difficulty is not altered by varying the accuracy of the range measurements, or if range-rate is used instead of, or in addition to, range.

In practice, in a single pass the earth rotates slightly, resulting in a change in the station-orbit geometry. However, the resulting least squares system is frequently ill conditioned; that is, nearly singular. Numerous other examples of nonobservability exist, particularly in the recovery of spherical harmonic coefficients of the earth’s gravity field from inadequate amounts and distributions of tracking data.

The mathematical conditions for parameter observability can be derived from the observability criterion for a linear dynamical system.

Theorem: For the linear system and linear observation set,

$$
\begin{array} { r l } & { { \mathbf { x } } _ { i } = \boldsymbol { \Phi } ( t _ { i } , t _ { k } ) { \mathbf { x } } _ { k } } \\ & { { \mathbf { y } } _ { i } = \widetilde { H } _ { i } { \mathbf { x } } _ { i } + \epsilon _ { i } ; \qquad i = 1 , \dots , \ell } \end{array}
$$

complete observability of the $n \times 1$ state vector, at the general time, $t _ { k }$ , requires satisfying the condition

$$
\delta \mathbf { x } _ { k } ^ { T } \Lambda \delta \mathbf { x } _ { k } > 0
$$

for all arbitrary real vectors, $\delta \mathbf { x } _ { k }$ , where the $n \times n$ information matrix, $\Lambda$ , is defined as

$$
\Lambda = \sum _ { i = 1 } ^ { \ell } \Phi ^ { T } ( t _ { i } , t _ { k } ) \widetilde { H } _ { i } ^ { T } R _ { i } ^ { - 1 } \widetilde { H } _ { i } \Phi ( t _ { i } , t _ { k } ) = H ^ { T } R ^ { - 1 } H
$$

and $H$ is defined by Eq. (4.2.38). Hence, complete observability of the state with the data in the batch accumulated from the observation set $\mathbf { y } _ { i } ; i = 1 , \ldots , \ell$ requires that the symmetric information matrix, $\Lambda$ , be positive definite. Note that in order for $\Lambda$ to be positive definite, $H$ must be full rank.

In addition to the constraints placed on the data as a necessary criterion for observability, care in the mathematical formulation of the problem must be exercised to ensure that only a minimal set of parameters is estimated. If spurious or unnecessary parameters are included in the problem formulation, the solution will be nonobservable regardless of the data characteristics. As an example, the expression for the acceleration on a satellite due to effects of atmospheric drag can be written as

$$
\mathbf { D } = - \frac { 1 } { 2 } \frac { C _ { D } A } { m } \rho ( h ) | \mathbf { V } _ { r e l } | \mathbf { V } _ { r e l }
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/bd694add0d6b9bf1bfee64c3f6644efbe01e6a64f80ed2364a94c20544bcb9dd.jpg)  
Figure 4.12.1: Range vs time from ground-based station.

where ${ \bf V } _ { r e l } = { \bf V } - \omega _ { e } \times { \bf r }$ , $\mathbf { V }$ is the inertial satellite velocity, $\omega _ { e }$ is the rotational velocity of the atmosphere (which is assumed to be the same as the earth’s rotational velocity), $C _ { D }$ is the satellite drag coefficient, $A$ is the satellite projected cross-sectional area, $m$ is the satellite mass, and $\rho ( h )$ is the atmospheric density at the satellite altitude, $h$ . In many applications, $C _ { D }$ , $A$ , and $m$ will be sufficiently uncertain that the errors in their a priori values may degrade the estimate of the satellite state. However, if any two or all three of these parameters are added to the state vector, a singular or nonobservable state vector will result, no matter how dense or how complete the observation set is. In this case, the $H$ matrix will have two rows that are identical except for a scalar mutiplication factor. This condition will cause $H$ to be non-full-rank and $H ^ { T } H$ to be nonpositive defini te. The single scalar parameter,

$$
\beta = \frac { C _ { D } A } { m }
$$

can be included as a state variable, and a well-posed estimation problem will occur. Two constants, say $C _ { 1 }$ and $C _ { 2 }$ , that do not appear separately in other force functions cannot be observed. Rather the product $C _ { 3 } = C _ { 1 } C _ { 2 }$ may be observed. Any state variables that are linearly related to one another cannot be uniquely determined (see Exercise 2 of Chapter 1). In general, the observability criterion tests not only the completeness of the data set in both the spatial and temporal sense, but it also tests the validity of the problem formulation.

# 4.13 ERROR SOURCES

In the application of an estimation procedure to a satellite or trajectory problem, measurements are obtained by various ground-based or on-board instruments. For example, a ground-based ranging system may make the measurements shown in Fig. 4.13.1 with time measured in minutes since the first measurement. Based on a mathematical model of the dynamical system and the measurement system, a predicted or computed measurement could be generated and compared with the actual measurement. If, in fact, the models are quite accurate, the difference (or residual) between the actual and predicted (or computed) measurements (O-C) will exhibit the random component in the measurement system as in Fig. 4.13.3. On the other hand, as is usually the case, the model has some inaccuracies associated with it, and the residual pattern will exhibit the character shown in Fig. 4.13.2. By using a polynomial function of time, the systematic component in Fig. 4.13.2 can be removed to determine the noise-only components. The data editing functions to eliminate the spurious or erroneous measurements are applied to these residuals. Finally, the edited data in Fig. 4.13.2 are used by the estimators to improve the state and the force and measurement models.

In the ideal case, the nonzero difference between the actual measurement and the predicted value should be due to the noise and biasing that occur in making the measurement. In practice, however, the mathematical models that describe the satellite force environment and those that describe the instrument performing some measurement are not completely accurate, or certain approximations are made for the benefit of computer storage and/or computer execution time, which introduce some discrepancy or error in the data processing. It is frequently necessary to ascribe the source of an error to a phenomenon in the physical world or to an approximation made in the model of the real world. Knowledge of various parameters in the mathematical models, such as the mass of the Earth or the coefficients that describe the inhomogeneous mass distribution within the Earth, have been obtained through various experiments or through use of many measurements and are only approximately known.

Typical error sources are as follows.

# • SATELLITE FORCE MODEL:

# Gravitation parameters

– Mass of the earth (GM) – Geopotential coefficients, ( $C _ { l m }$ and $S _ { l m }$ ) – Solid earth and ocean tide perturbations – Mass and position of the moon and planets – General relativistic perturbation

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/9d75685a1d681065aa66a3503f0a6d91584cdbb3eab8f9070fc655c74025e348.jpg)  
Figure 4.13.1: O-C, random and systematic component.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/707216c84961410275f5af087c7c725e3c471c0de1dd425a92ff29417b8068a1.jpg)  
Figure 4.13.2: Random component.

# Nongravitational parameters

– Drag ( $C _ { D }$ , atmospheric density)   
– Solar and earth radiation pressure   
– Thrust (including venting and momentum dumping)   
– Other (magnetic origin, etc.)

• MEASUREMENT MODEL:

# Inertial and terrestrial coordinate systems

– Precession and nutation – Polar motion

# Ground-based measurements

– Coordinates of tracking station   
– Atmospheric effects (tropospheric and ionospheric refraction)   
– Instrument modeling   
– Clock accuracy   
– Tectonic plate motion

The error sources are dependent on the satellite under consideration, that is, satellite configuration, the orbit altitude and inclination, and measurement systems. Some of these error sources have distinct signatures in the data, and others may be very similar, thus producing aliasing between these components and making it difficult or impossible to separate their effects into individual components.

As a consequence, one constantly attempts to improve the model of the satellite environment. However, this improvement is normally done outside the operations aspect in which state estimates may be needed for an ongoing mission. To improve the gravitational model, for example, observations of various types such as range, range-rate, and angular data from different satellites would be used in a large parameter least squares solution. These large parameter solutions, in which the number of parameters may be 5000 or more, consume large amounts of computer time and, consequently, can be performed only infrequently. A family of such solutions has been generated since 1972 at the Goddard Space Flight Center and the Center for Space Research, and in several international centers. The models start with the Goddard Earth Model, GEM-1, and progress through the recent JGM-3 model (Tapley et al., 1996) developed for the TOPEX/Poseidon mission. In the case of JGM-3, a full degree-70 and order-70 solution was produced. Other solutions have been obtained at the Smithsonian Astrophysical Observatory (SAO), the Department of Defense, and by foreign institutions, including GFZ in Germany and GRGS in France.

Implicit in all of these solutions is the time standard used in solving Newton’s Equations, as well as time tagging the observations by various instruments. In the case of Newton’s Laws, a uniform time scale is inherent, and we attempt to provide such a system in time tagging the measurements. Uniform time scales are provided by atomic clocks, aside from small relativistic effects, and an operational problem exists to ensure that all clocks used in making measurements are adequately synchronized. For ground-based systems, station clocks are usually synchronized to a national standard. Clearly, in the event that a station is out of synchronization with the other stations, the measurements made at that station will produce residuals that are somewhat larger than the others.

# 4.14 ORBIT ACCURACY

In general, the orbit accuracy is dependent on the following factors:

1. Truncation error in the application of an approximating algorithm to a mathematical process;   
2. Round-off error in the application of a fini te computational precision;   
3. Mathematical model simplifications;   
4. Errors in the parameters used in the mathematical model of the physical system or the instrument model;   
5. Amount, type, and accuracy of tracking data.

For missions with high orbit-accuracy requirements, the limitation on the accuracy usually is imposed by the accuracy of the dynamical model, particularly the geopotential. But even the geopotential errors are dependent on the particular orbit; for example, an orbit at an altitude of one earth radius will be less affected by those errors than a satellite at an altitude of $8 0 0 { \mathrm { k m } }$ . The accuracy of the models is reflected in the current ability to determine an orbit for TOPEX/Poseidon (1334 km altitude) of ten days duration, which yields $1 \mathrm { c m }$ root mean square (RMS) of the laser range residuals (Tapley et al., 1994). This RMS reflects an overall orbit accuracy of about $8 \mathrm { c m }$ .

Determining the true accuracy of an orbit determination solution based on actual tracking data is difficult because the true trajectory is never known. Furthermore, the estimation error covariance matrix for a given solution is generally overly optimistic depending on the weights assigned to the tracking data. If realistic process noise has been included, the estimation error covariance matrix may be a good indicator of orbit accuracy but it is difficult to determine the level of process noise needed to properly scale the covariance matrix. This is best done through simulation studies, but these require quantitative knowledge of the error sources. Covariance analysis, described in Chapter 6, may also aid in accuracy assessment assuming statistical knowledge of the error sources is available.

A few quantitative indicators of accuracy can be examined depending on what tracking information is available. If solutions derived from different independent tracking systems are available they can be compared. The locations of most laser tracking sites are known to the centimeter level and the measurements themselves are accurate to this level. Therefore, if the satellite is tracked by lasers as it flies at high elevation over a site, the laser residuals will be a good indication of radial orbit accuracy. Furthermore, the estimation error covariance matrix can be mapped to these times, rotated to radial, along-track and cross-track directions and the radial standard deviation compared with the RMS of laser residuals. This comparison will provide a calibration of the radial component of the covariance matrix. The RMS of tracking data residuals is also an indicator of accuracy. However, small tracking residuals do not guarantee an accurate orbit because there may be a component of the satellite’s position that is insensitive to the particular tracking data type (see Section 4.12).

Another measure of accuracy is the RMS of orbit solution overlaps. For example, five days of contiguous tracking data may be fit as two arcs of three days length with one day of overlap. The RMS of the three components of overlapping position is an indicator of orbit accuracy. However, any error common to a given coordinate during the overlap period will not be evident in the RMS. Finally, orbit solutions for satellites that make any kind of metric measurements (radar altimeters, laser altimeters, SAR, etc.) can be evaluated by examining the quality of parameters based on these measurements themselves. For example, for laser or radar altimeter satellites the RMS of crossover residuals discussed in Chapter 3 are an indicator of orbit accuracy.

The accuracy just described relates to the estimation accuracy. Another important accuracy consideration occurs in the problem of prediction. Given some estimate of the satellite state, how well can the state of the spacecraft be predicted at some future time? Such prediction accuracy is important for (1) predicting and scheduling events at ground-based stations, including antenna or telescope pointing, and (2) scheduling events for future orbital maneuvers. The prediction accuracy is influenced by the same effects that influence the estimation accuracy; however, it is also dependent on the estimation accuracy itself. If, for instance, a perfect physical model was known but the state estimate used to initiate the prediction was in error, this error would grow during the prediction interval. As an example of prediction accuracy, the position of Lageos can be predicted to about 200 meters after two months. For the TOPEX/Poseidon Mission, the orbit can be predicted to about $0 . 5 \mathrm { k m }$ after a week based on tracking with laser ranging or the Global Positioning System.

# 4.15 SMOOTHING

It is often desirable to perform a smoothing operation when using a sequential filter . In this case, we are searching for the best estimate of the state at some time $t _ { k }$ based on all observations through time $t _ { \ell }$ where $\ell > k$ . For the case where there is no random component to the dynamical equation of state—for example, the no-process noise case—the batch estimation algorithm along with the prediction equation, Eqs. (4.4.19) and (4.4.22), will give the smoothed solution. However, as noted, the batch estimation approach has difficul ty including the effects of process noise. The smoothing algorithms have been developed to overcome this difficulty. Following Jazwinski (1970), the smoothing algorithm can be derived using a Bayesian approach of maximizing the density function of the state conditioned on knowledge of the observations through time, $t _ { \ell }$ . Our system is described in Section 4.9 (see Eq. (4.9.46)).

$$
\begin{array} { r } { \mathbf { x } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) \mathbf { x } _ { k } + \Gamma ( t _ { k + 1 } , t _ { k } ) \mathbf { u } _ { k } } \\ { \mathbf { y } _ { k } = \widetilde { H } _ { k } \mathbf { x } _ { k } + \boldsymbol { \epsilon } _ { k } . \qquad } \end{array}
$$

We will use the notation $\hat { \mathbf { x } } _ { k } ^ { \ell }$ to indicate the best estimate of $\mathbf { x }$ at $t _ { k }$ based on observations through $t _ { \ell }$ , where in general $\ell > k$ . Following the Maximum Likelihood philosophy, we wish to find a recursive expression for $\hat { \mathbf { x } } _ { k } ^ { \ell }$ in terms of $\hat { \mathbf { x } } _ { k + 1 } ^ { \ell }$ , which maximizes the conditional density function

$$
p ( \mathbf { x } _ { k } , \mathbf { x } _ { k + 1 } / \mathbf { Y } _ { \ell } ) , \quad { \mathrm { w h e r e } } \quad \mathbf { Y } _ { \ell } = \mathbf { y } _ { 1 } , \mathbf { y } _ { 2 } \cdot \cdot \cdot \mathbf { y } _ { k } \cdot \cdot \cdot \mathbf { y } _ { \ell } .
$$

From Bayes Rule

$$
\begin{array} { l } { { p \left( { { \bf { x } } _ { k } } , { { \bf { x } } _ { k + 1 } } / { \bf { Y } } _ { \ell } \right) } = \displaystyle \frac { { p \left( { { { \bf { x } } _ { k } } , { { \bf { x } } _ { k + 1 } } , { \bf { Y } } _ { \ell } } \right) } } { { p \left( { { \bf { Y } } _ { \ell } } \right) } } = \displaystyle \frac { { p \left( { { { \bf { x } } _ { k } } , { { \bf { x } } _ { k + 1 } } , { \bf { Y } } _ { k } , { { \bf { y } } _ { k + 1 } } \ldots { \bf { y } } _ { \ell } } \right) } } { { p \left( { { \bf { Y } } _ { \ell } } \right) } } } \\ { ~ \displaystyle ~ = \frac { { p \left( { { { \bf { Y } } } _ { k } } \right) } } { { p \left( { { \bf { Y } } _ { \ell } } \right) } } p \left( { { { \bf { x } } _ { k } } , { { \bf { x } } _ { k + 1 } } , { { \bf { y } } _ { k + 1 } } \ldots { { \bf { y } } _ { \ell } } / { \bf { Y } } _ { k } } \right) ~ ( 4 . 1 5 ) } \\ { ~ \displaystyle ~ = \frac { { p \left( { { \bf { Y } } _ { k } } \right) } } { { p \left( { { \bf { Y } } _ { \ell } } \right) } } p \left( { { { \bf { y } } _ { k + 1 } } \ldots { \bf { y } } _ { \ell } } / { { \bf { x } } _ { k } } , { { \bf { x } } _ { k + 1 } } , { { \bf { Y } } _ { k } } \right) } \\ { ~ \displaystyle ~ \times { p \left( { { { \bf { x } } } _ { k } } , { { \bf { x } } _ { k + 1 } } / { { \bf { Y } } _ { k } } \right) } . } \end{array}
$$

Notice that

$$
p \left( \mathbf { y } _ { k + 1 } \ldots \mathbf { y } _ { \ell } / \mathbf { x } _ { k } , \mathbf { x } _ { k + 1 } , \mathbf { Y } _ { k } \right) = p \left( \mathbf { y } _ { k + 1 } \ldots \mathbf { y } _ { \ell } / \mathbf { x } _ { k + 1 } \right) ,
$$

and

$$
\begin{array} { r l } & { p \left( \mathbf { x } _ { k } , \mathbf { x } _ { k + 1 } / \mathbf { Y } _ { k } \right) = p \left( \mathbf { x } _ { k + 1 } / \mathbf { x } _ { k } , \mathbf { Y } _ { k } \right) p \left( \mathbf { x } _ { k } / \mathbf { Y } _ { k } \right) } \\ & { \qquad = p \left( \mathbf { x } _ { k + 1 } / \mathbf { x } _ { k } \right) p \left( \mathbf { x } _ { k } / \mathbf { Y } _ { k } \right) , } \end{array}
$$

since knowledge of $\mathbf { x } _ { k }$ and ${ \bf Y } _ { k }$ is redundant. Using Eqs. (4.15.3) and (4.15.4), Eq. (4.15.2) may be written

$$
\begin{array} { r l r } {  { p ( \mathbf { x } _ { k } , \mathbf { x } _ { k + 1 } / \mathbf { Y } _ { \ell } ) = \frac { p ( \mathbf { Y } _ { k } ) } { p ( \mathbf { Y } _ { \ell } ) } p ( \mathbf { y } _ { k + 1 } \ldots \mathbf { y } _ { \ell } / \mathbf { x } _ { k + 1 } ) } } \\ & { } & { \times p ( \mathbf { x } _ { k + 1 } / \mathbf { x } _ { k } ) p ( \mathbf { x } _ { k } / \mathbf { Y } _ { k } ) . } \end{array}
$$

The first three density functions on the right-hand side of Eq. (4.15.5) are independent of $\mathbf { x } _ { k }$ ; hence, we need to be concerned only with $p ( \mathbf { x } _ { k + 1 } / \mathbf { x } _ { k } )$ and $p ( \mathbf { x } _ { k } / \mathbf { Y } _ { k } )$ . Assuming that these are Gaussian and that the process noise is zero mean, it is easily shown that

$$
\begin{array} { r l } & { p ( { \mathbf x } _ { k + 1 } / { \mathbf x } _ { k } ) \sim N \big ( \Phi ( t _ { k + 1 } , t _ { k } ) { \mathbf x } _ { k } , \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) \big ) } \\ & { p ( { \mathbf x } _ { k } / { \mathbf Y } _ { k } ) \sim N ( \hat { \mathbf x } _ { k } , P _ { k } ) . } \end{array}
$$

It may seem like the covariance of $p ( \mathbf { x } _ { k + 1 } / \mathbf { x } _ { k } )$ should be

$$
\Phi ( t _ { k + 1 } , t _ { k } ) P _ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) + \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) .
$$

However, notice that this is the density function of $\mathbf { x } _ { k + 1 }$ conditioned on knowledge of $\mathbf { x } _ { k }$ . Since $P _ { k }$ describes the error in $\hat { \mathbf { x } } _ { k }$ and $\mathbf { x } _ { k }$ has occurred and is known, $P _ { k }$ must be a null matrix.

In order to maximize the conditional probability density function given in Eq. (4.15.5), we may maximize the logarithm of $p \left( \mathbf { x } _ { k + 1 } / \mathbf { x } _ { k } \right) p \left( \mathbf { x } _ { k } / \mathbf { Y } _ { k } \right)$ ,

$$
\begin{array} { l } { { \displaystyle \ln { \cal L } = - \frac { 1 } { 2 } [ { \bf x } _ { k + 1 } - \Phi \left( t _ { k + 1 } , t _ { k } \right) { \bf x } _ { k } ] ^ { T } [ \Gamma \left( t _ { k + 1 } , t _ { k } \right) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) ] ^ { - 1 } } } \\ { { \displaystyle ~ \times \left[ { \bf x } _ { k + 1 } - \Phi \left( t _ { k + 1 } , t _ { k } \right) { \bf x } _ { k } \right] - \frac { 1 } { 2 } \left[ { \bf x } _ { k } - \hat { \bf x } _ { k } \right] ^ { T } P _ { k } ^ { - 1 } \left[ { \bf x } _ { k } - \hat { \bf x } _ { k } \right] . \quad ( 4 . } } \end{array}
$$

Suppose that $\hat { \mathbf { x } } _ { k + 1 } ^ { \ell }$ , the maximizing value of $\mathbf { x } _ { k + 1 }$ based on observations through $t _ { \ell }$ , is available. We wish to find the value of $\hat { \mathbf { x } } _ { k } ^ { \ell }$ that maximizes $\ln { \cal L }$ . Differentiating $\ln { \cal L }$ with respect to $\mathbf { x } _ { k }$ and setting this to zero yields (for simplicity we have dropped time identifiers on $\Phi ( t _ { k + 1 } , t _ { k } )$ and $\Gamma ( t _ { k + 1 } , t _ { k } ) ,$ )

$$
\begin{array} { r l } & { \hat { \mathbf { x } } _ { k } ^ { \ell } = [ ( P _ { k } ^ { k } ) ^ { - 1 } + \Phi ^ { T } ( \Gamma Q \Gamma ^ { T } ) ^ { - 1 } \Phi ] ^ { - 1 } } \\ & { \quad \times [ ( P _ { k } ^ { k } ) ^ { - 1 } \hat { \mathbf { x } } _ { k } ^ { k } + \Phi ^ { T } ( \Gamma Q \Gamma ^ { T } ) ^ { - 1 } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } ] , } \end{array}
$$

using our current notation,

$$
\begin{array} { l } { P _ { k } ^ { k } \equiv P _ { k } } \\ { \hat { \mathbf { x } } _ { k } ^ { k } \equiv \hat { \mathbf { x } } _ { k } . } \end{array}
$$

Applying the Schur identity we can write this in a more conventional form

$$
\hat { \mathbf { x } } _ { k } ^ { \ell } = \hat { \mathbf { x } } _ { k } ^ { k } + S _ { k } \left( \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } - \Phi ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { x } } _ { k } ^ { k } \right)
$$

where

$$
\begin{array} { r l } & { S _ { k } = P _ { k } ^ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) [ \Phi ( t _ { k + 1 } , t _ { k } ) P _ { k } ^ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) } \\ & { ~ + \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) ] ^ { - 1 } } \\ & { = P _ { k } ^ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) ( P _ { k + 1 } ^ { k } ) ^ { - 1 } . } \end{array}
$$

Eq. (4.15.9) is the smoothing algorithm. Computation goes backward in index $k$ , with $\hat { \mathbf { x } } _ { \ell } ^ { \ell }$ , the filt er solution, as initial conditions. Note that the filter solutions for $\hat { \mathbf { x } } _ { k } ^ { k }$ , $P _ { k } ^ { k }$ , $\Phi ( t _ { k + 1 } , t _ { k } )$ , and $\Gamma ( t _ { k + 1 } , t _ { k } )$ are required and should be stored in the filtering process. The time update of the covariance matrix, $P _ { k + 1 } ^ { k }$ , may be stored or recomputed.

The equation for propagating the smoothed covariance is derived next (Jazwinski, 1970; Rausch et al., 1965) . It can easily be shown from Eq. (4.15.9) that $\hat { \mathbf { x } } _ { k } ^ { \ell }$ is unbiased; hence, the smoothed covariance is defined by

$$
P _ { k } ^ { \ell } = E \left[ ( \hat { \mathbf { x } } _ { k } ^ { \ell } - \mathbf { x } _ { k } ) ( \hat { \mathbf { x } } _ { k } ^ { \ell } - \mathbf { x } _ { k } ) ^ { T } \right] .
$$

Subtracting $\mathbf { x } _ { k }$ from both sides of Eq. (4.15.9) and moving all terms involving smoothed quantities to the LHS yields:

$$
\tilde { \mathbf { x } } _ { k } ^ { \ell } - S _ { k } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } = \tilde { \mathbf { x } } _ { k } ^ { k } - S _ { k } \Phi ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { x } } _ { k } ^ { k }
$$

where

$$
\begin{array} { r } { \tilde { \mathbf { x } } _ { k } ^ { \ell } \equiv \hat { \mathbf { x } } _ { k } ^ { \ell } - \mathbf { x } _ { k } , \tilde { \mathbf { x } } _ { k } ^ { k } \equiv \hat { \mathbf { x } } _ { k } ^ { k } - \mathbf { x } _ { k } . } \end{array}
$$

Multiplying both sides of Eq. (4.15.12) by their respective transpose and taking the expected value yields

$$
\begin{array} { r l r } { \quad } & { } & { E \left( \tilde { \mathbf { x } } _ { k } ^ { \ell } \tilde { \mathbf { x } } _ { k } ^ { \ell ^ { T } } \right) + S _ { k } E \left( \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } \right) S _ { k } ^ { T } = } & { ( 4 . 1 \boldsymbol { : } \medskip } \\ { \quad } & { } & { E \left( \tilde { \mathbf { x } } _ { k } ^ { k } \tilde { \mathbf { x } } _ { k } ^ { k ^ { T } } \right) + S _ { k } \Phi ( t _ { k + 1 } , t _ { k } ) E \left( \hat { \mathbf { x } } _ { k } ^ { k } \hat { \mathbf { x } } _ { k } ^ { k ^ { T } } \right) \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) S _ { k } ^ { T } . } \end{array}
$$

By definiti on

$$
P _ { k } ^ { \ell } \equiv E \left[ \tilde { \mathbf { x } } _ { k } ^ { \ell } \tilde { \mathbf { x } } _ { k } ^ { \ell ^ { T } } \right]
$$

and

$$
P _ { k } ^ { k } \equiv E \left[ \tilde { \mathbf { x } } _ { k } ^ { k } \tilde { \mathbf { x } } _ { k } ^ { k ^ { T } } \right] .
$$

The cross product terms that have been dropped in Eq. (4.15.13) can be shown to be null matrices,

$$
\begin{array} { r l } & { E \left( \tilde { \mathbf { x } } _ { k } ^ { \ell } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } \right) = E \left( \hat { \mathbf { x } } _ { k } ^ { \ell } - \mathbf { x } _ { k } \right) \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } } \\ & { \qquad = E \left( \hat { \mathbf { x } } _ { k } ^ { \ell } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } \right) - E \left( \mathbf { x } _ { k } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } \right) } \\ & { \qquad = \hat { \mathbf { x } } _ { k } ^ { \ell } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } - E \left( \mathbf { x } _ { k } / \mathbf { y } _ { \ell } \right) \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } = 0 . } \end{array}
$$

Here $\hat { \bf x }$ is the conditional mean of the appropriate conditional density function and is not a random variable; hence,

$$
E \left[ \mathbf { x } _ { k } / \mathbf { y } _ { \ell } \right] \equiv \hat { \mathbf { x } } _ { k } ^ { \ell } .
$$

Likewise, for the filter results,

$$
\begin{array} { r l } & { E \left( \tilde { \mathbf { x } } _ { k } ^ { k } \hat { \mathbf { x } } _ { k } ^ { k ^ { \prime } } \right) = E \left( \hat { \mathbf { x } } _ { k } ^ { k } - \mathbf { x } _ { k } \right) \hat { \mathbf { x } } _ { k } ^ { k ^ { \prime } } } \\ & { \qquad = \hat { \mathbf { x } } _ { k } ^ { k } \hat { \mathbf { x } } _ { k } ^ { k ^ { \prime } } - E \left( \mathbf { x } _ { k } / \mathbf { y } _ { k } \right) \hat { \mathbf { x } } _ { k } ^ { k ^ { \prime } } = 0 . } \end{array}
$$

Hence, Eq. (4.15.13) becomes

$$
P _ { k } ^ { \ell } + S _ { k } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } S _ { k } ^ { T } = P _ { k } ^ { k } + S _ { k } \Phi ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { x } } _ { k } ^ { k } \hat { \mathbf { x } } _ { k } ^ { k ^ { T } } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) S _ { k } ^ { T } .
$$

Now,

$$
\begin{array} { r l } & { P _ { k + 1 } ^ { \ell } \equiv E \left\{ \left( \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } - \mathbf { x } _ { k + 1 } \right) \left( \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } - \mathbf { x } _ { k + 1 } \right) ^ { T } / \mathbf { y } _ { \ell } \right\} } \\ & { \qquad = - \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } + E \left( \mathbf { x } _ { k + 1 } \mathbf { x } _ { k + 1 } ^ { T } \right) } \end{array}
$$

or

$$
\begin{array} { r } { \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } = E ( \mathbf { x } _ { k + 1 } \mathbf { x } _ { k + 1 } ^ { T } ) - P _ { k + 1 } ^ { \ell } . } \end{array}
$$

Also, in terms of $\mathbf { x } _ { k }$ (let $G = \Phi ( t _ { k + 1 } , t _ { k } ) \mathbf { x } _ { k } + \Gamma ( t _ { k + 1 } , t _ { k } ) \mathbf { u } _ { k } )$

$$
\begin{array} { r l } & { E ( \mathbf { x } _ { k + 1 } \mathbf { x } _ { k + 1 } ^ { T } ) = E \left[ G G ^ { T } \right] } \\ & { \qquad = \Phi ( t _ { k + 1 } , t _ { k } ) E ( x _ { k } , x _ { k } ^ { T } ) \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) } \\ & { \qquad + \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) } \end{array}
$$

and

$$
\begin{array} { r l } & { P _ { k } ^ { k } = E \left\{ \left( \hat { \mathbf { x } } _ { k } ^ { k } - \mathbf { x } _ { k } \right) \left( \hat { \mathbf { x } } _ { k } ^ { k } - \mathbf { x } _ { k } \right) ^ { T } / \mathbf { y } _ { k } \right\} } \\ & { \quad \quad = - \hat { \mathbf { x } } _ { k } ^ { k } \hat { \mathbf { x } } _ { k } ^ { k ^ { T } } + E ( \mathbf { x } _ { k } \mathbf { x } _ { k } ^ { T } ) } \end{array}
$$

or

$$
\begin{array} { r } { \hat { \mathbf { x } } _ { k } ^ { k } \hat { \mathbf { x } } _ { k } ^ { k ^ { T } } = E \left( \mathbf { x } _ { k } \mathbf { x } _ { k } ^ { T } \right) - P _ { k } ^ { k } . } \end{array}
$$

Substituting Eqs. (4.15.20), (4.15.21), and (4.15.22) into (4.15.19) yields

$$
\begin{array} { r } { P _ { k } ^ { \ell } + S _ { k } \left[ - P _ { k + 1 } ^ { \ell } + \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) \right] S _ { k } ^ { T } } \\ { = P _ { k } ^ { k } - S _ { k } \Phi ( t _ { k + 1 } , t _ { k } ) P _ { k } ^ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) S _ { k } ^ { T } . } \end{array}
$$

Finally,

$$
\begin{array} { r } { P _ { k } ^ { \ell } = P _ { k } ^ { k } + S _ { k } \left( P _ { k + 1 } ^ { \ell } - P _ { k + 1 } ^ { k } \right) S _ { k } ^ { T } . } \end{array}
$$

Note that neither the smoothed covariance nor the observation data appear explicitly in the smoothing algorithm. The algorithm derived previously is identical to the Rauch, Tung, and Striebel smoother (1965).

Suppose there is no process noise (i.e., $Q = 0$ ), then the smoothing algorithm reduces to

$$
S _ { k } = \Phi ^ { - 1 } ( t _ { k + 1 } , t _ { k } ) ,
$$

and

$$
\begin{array} { r l } & { \hat { \mathbf { x } } _ { k } ^ { \ell } = \Phi ^ { - 1 } \bigl ( t _ { k + 1 } , t _ { k } \bigr ) \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } } \\ & { \qquad = \Phi \left( t _ { k } , t _ { k + 1 } \right) \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } } \\ & { \qquad = \Phi \bigl ( t _ { k } , t _ { \ell } \bigr ) \hat { \mathbf { x } } _ { \ell } ^ { \ell } . } \end{array}
$$

Also,

$$
\begin{array} { r l } & { P _ { k } ^ { \ell } = \Phi ^ { - 1 } ( t _ { k + 1 } , t _ { k } ) P _ { k + 1 } ^ { \ell } \Phi ^ { - T } ( t _ { k + 1 } , t _ { k } ) } \\ & { \quad = \Phi \left( t _ { k } , t _ { k + 1 } \right) P _ { k + 1 } ^ { \ell } \Phi ^ { T } ( t _ { k } , t _ { k + 1 } ) } \\ & { \quad = \Phi ( t _ { k } , t _ { \ell } ) P _ { \ell } ^ { \ell } \Phi ^ { T } ( t _ { k } , t _ { \ell } ) . } \end{array}
$$

Hence, with no process noise the smoothing algorithm simply maps the final filter state estimate and covariance matrix to earlier epochs.

# 4.15.1 COMPUTATIONAL ALGORITHM FOR SMOOTHER

Given (from the filtering algorithm)

$$
\hat { \bf x } _ { \ell } ^ { \ell } , \ \hat { \bf x } _ { \ell - 1 } ^ { \ell - 1 } , \ P _ { \ell } ^ { \ell - 1 } , \ P _ { \ell - 1 } ^ { \ell - 1 } , \ \Phi ( t _ { \ell } , t _ { \ell - 1 } ) ;
$$

set $k = \ell - 1$

$$
\begin{array} { r l } & { S _ { \ell - 1 } = P _ { \ell - 1 } ^ { \ell - 1 } ~ \boldsymbol \Phi ^ { T } ( t _ { \ell } , t _ { \ell - 1 } ) ~ ( P _ { \ell } ^ { \ell - 1 } ) ^ { - 1 } } \\ & { \hat { \mathbf { x } } _ { \ell - 1 } ^ { \ell } = \hat { \mathbf { x } } _ { \ell - 1 } ^ { \ell - 1 } + S _ { \ell - 1 } ( \hat { \mathbf { x } } _ { \ell } ^ { \ell } - \boldsymbol \Phi ( t _ { \ell } , t _ { \ell - 1 } ) \hat { \mathbf { x } } _ { \ell - 1 } ^ { \ell - 1 } ) . } \end{array}
$$

Given (from the filtering algorithm and the previous step of the smoothing algorithm)

$$
{ \hat { \mathbf { x } } } _ { \ell - 2 } ^ { \ell - 2 } , \ P _ { \ell - 1 } ^ { \ell - 2 } , \ P _ { \ell - 2 } ^ { \ell - 2 } , \ { \hat { \mathbf { x } } } _ { \ell - 1 } ^ { \ell } , \ \Phi ( t _ { \ell - 1 } , t _ { \ell - 2 } ) ;
$$

set $k = \ell - 2$ , and compute

$$
\begin{array} { r l } & { S _ { \ell - 2 } = P _ { \ell - 2 } ^ { \ell - 2 } \Phi ^ { T } \left( t _ { \ell - 1 } , t _ { \ell - 2 } \right) ( P _ { \ell - 1 } ^ { \ell - 2 } ) ^ { - 1 } } \\ & { \hat { \mathbf { x } } _ { \ell - 2 } ^ { \ell } = \hat { \mathbf { x } } _ { \ell - 2 } ^ { \ell - 2 } + S _ { \ell - 2 } \left( \hat { \mathbf { x } } _ { \ell - 1 } ^ { \ell } - \Phi \left( t _ { \ell - 1 } , t _ { \ell - 2 } \right) \hat { \mathbf { x } } _ { \ell - 2 } ^ { \ell - 2 } \right) } \\ & { \qquad \vdots } \end{array}
$$

# 4.16 THE PROBABILITY ELLIPSOID

Given a normally distributed random vector, $\mathbf { x }$ , with mean $\overline { { \mathbf { x } } }$ , and variancecovariance $P$ , the function

$$
( { \bf x } - { \overline { { \bf x } } } ) ^ { T } P ^ { - 1 } ( { \bf x } - { \overline { { \bf x } } } ) = \ell ^ { 2 }
$$

is a positive definite quadratic form representing a family of hyperellipsoids of constant probability density (Mikhail, 1976; Bryson and Ho, 1975). The 3D case is important because we often are interested in the 3D ellipsoids associated with the position uncertainty of a satellite. For example, in the case of interplanetary missions, we are interested in the probability ellipsoid of the spacecraft as it impacts the plane that contains the center of gravity of the target planet and that is normal to the asymptote of the spacecraft trajectory relative to the planet. This plane, shown in Fig. 4.16.1 and referred to as the B-plane (Dorroh and Thornton, 1970), is the reference plane used in interplanetary navigation applications. The associated coordinate system has two orthogonal axes in this plane and one normal to it. The axes of the ellipsoid in the B-plane give information on the uncertainty of the nearest approach distance to the planet that is needed to give assurance that the spacecraft will not impact the planet. The out-of-plane axis relates to the accuracy of the encounter time. If the spacecraft is to be placed in orbit about the target planet, information from the covariance matrix used to generate the probability ellipsoid is used to design the capture maneuver, and to compute the a priori uncertainty of the resulting orbit parameters. Construction of the probability ellipsoid is most easily accomplished relative to the principal axes. To this end, we introduce the following theorem (Kreyszig, 1993).

Theorem: If $\mathbf { u } _ { 1 } , \mathbf { u } _ { 2 } , \ldots , \mathbf { u } _ { n }$ is an orthonormal system of eigenvectors associated, respectively, with the eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ of an $n \times n$ symmetric positive definite matrix, $P$ , and if

$$
U = [ \mathbf { u } _ { 1 } , \mathbf { u } _ { 2 } , \ldots , \mathbf { u } _ { n } ] _ { n \times n } ,
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/ab9ec1b9314e283bee860db46b770896ccb2dd95cd88c8301b12624b0345c7a9.jpg)  
Figure 4.16.1: Probability ellipse on the B-plane.

then

$$
U ^ { T } P U = \left[ \begin{array} { l } { \lambda _ { 1 } \ 0 \ \cdots \ 0 } \\ { 0 \ \lambda _ { 2 } \cdots \ 0 } \\ { \vdots \qquad \ddots \ \vdots } \\ { 0 \ 0 \ \cdots \ \lambda _ { n } } \end{array} \right] = D \left[ \lambda _ { 1 } , \ \lambda _ { 2 } , \ldots , \ \lambda _ { n } \right] ;
$$

that is, $U ^ { T } P U$ is a diagonal matrix containing the eigenvalues of P. The normalized vectors $\mathbf { u } _ { 1 } , \mathbf { u } _ { 2 } , \ldots , \mathbf { u } _ { n }$ are called principal axes of $P$ , and the transformation matrix $U ^ { T }$ used to diagonalize $P$ is called a principal axes transformation. The matrix $U ^ { T }$ is the matrix of normalized eigenvectors and is orthogonal. For the random vector $\mathbf { x }$ with mean $\overline { { \mathbf { x } } }$ and variance-covariance, $P$ , the principal axes, $\mathbf { x } ^ { \prime }$ , are given by

$$
\mathbf { x } ^ { \prime } = U ^ { T } \mathbf { x } .
$$

The variance-covariance matrix, $P ^ { \prime }$ , associated with the principal axes is given by

$$
\begin{array} { r l } & { P ^ { \prime } \equiv E [ ( \mathbf { x } ^ { \prime } - \overline { { \mathbf { x } } } ^ { \prime } ) ( \mathbf { x } ^ { \prime } - \overline { { \mathbf { x } } } ^ { \prime } ) ^ { T } ] } \\ & { \quad = U ^ { T } E [ ( \mathbf { x } - \overline { { \mathbf { x } } } ) ( \mathbf { x } - \overline { { \mathbf { x } } } ) ^ { T } ] U } \\ & { \quad = U ^ { T } P U = D [ \lambda _ { 1 } \ldots \lambda _ { n } ] . } \end{array}
$$

In our case, $\Delta \mathbf { x }$ represents the estimation error vector defined by

$$
\Delta { \bf x } \equiv \hat { \bf x } - { \bf x } \equiv [ \tilde { x } \tilde { y } \tilde { z } ] ^ { T } ,
$$

with zero mean and variance-covariance given by

$$
P = E [ \Delta \mathbf { x } \Delta \mathbf { x } ^ { T } ] .
$$

Although this restriction is unnecessary, we will simplify matters and deal only with the three position coordinates of $\Delta \mathbf { x }$ and the associated $3 \times 3$ portion of the estimation error covariance matrix.

In this case, the equation for the probability ellipsoid is

$$
[ \tilde { x } \tilde { y } \tilde { z } ] P ^ { - 1 } \left[ \begin{array} { l } { \tilde { x } } \\ { \tilde { y } } \\ { \tilde { z } } \end{array} \right] = \ell ^ { 2 } .
$$

The ellipsoids for $\ell = 1 , 2$ , and 3 are called the $1 \sigma , 2 \sigma$ , and $3 \sigma$ error ellipsoids. The probability of the state estimate error falling inside these ellipsoids, assuming a trivariate Gaussian density function, is 0.200, 0.739, and 0.971, respectively.

To obtain the principal axes, we use the theorem just introduced and determine the matrix of normalized eigenvectors, $U$ , and the eigenvalues $\lambda _ { i }$ , $i = { 1 , 2 , 3 }$ of $P$ . The principal axes are given by

$$
\left[ \stackrel { \tilde { x } ^ { \prime } } { \tilde { y } ^ { \prime } } \right] = \boldsymbol { U } ^ { T } \left[ \stackrel { \tilde { x } } { \tilde { y } } \right] ,
$$

and the associated covariance matrix is

$$
P ^ { \prime } = U ^ { T } P U .
$$

The probability ellipsoids are given by

$$
\left[ { \tilde { x } } ^ { \prime } { \tilde { y } } ^ { \prime } { \tilde { z } } ^ { \prime } \right] { \left[ \begin{array} { l } { 1 / \lambda _ { 1 } } \\ { \qquad 1 / \lambda _ { 2 } } \\ { \qquad 1 / \lambda _ { 3 } } \end{array} \right] } { \left[ \begin{array} { l } { { \tilde { x } } ^ { \prime } } \\ { { \tilde { y } } ^ { \prime } } \\ { { \tilde { z } } ^ { \prime } } \end{array} \right] } = \ell ^ { 2 } ,
$$

or

$$
{ \frac { \tilde { x } ^ { \prime } ^ { 2 } } { \lambda _ { 1 } } } + { \frac { \tilde { y } ^ { \prime } ^ { 2 } } { \lambda _ { 2 } } } + { \frac { \tilde { z } ^ { \prime } ^ { 2 } } { \lambda _ { 3 } } } = \ell ^ { 2 } .
$$

It is convenient to arrange the eigenvectors so that $\lambda _ { 1 } > \lambda _ { 2 } > \lambda _ { 3 }$ (i.e., in order of descending values of $\lambda _ { i }$ ). The axes of the $1 \sigma$ ellipsoid are given by solving Eq.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/a13172c3131df9ec303c2f907d13f523bbb7db98bbad7d74a359521d8a7953d5.jpg)  
Figure 4.16.2: Euler angles defined.

(4.16.9) for $\ell = 1$ and sequentially setting two of the coordinate values to zero; that is, to obtain the semimajor axis, $a$ , set $\tilde { x } ^ { \prime } = a$ and $\tilde { y } ^ { \prime } = \tilde { z } ^ { \prime } = 0$ . This yields

$$
a ^ { 2 } = \lambda _ { 1 } , b ^ { 2 } = \lambda _ { 2 } , c ^ { 2 } = \lambda _ { 3 } .
$$

The orientation of the ellipse relative to the original axis system is obtained by solving for the three Euler angles given by the transformation matrix, $U$ . It is convenient to choose the sign of the normalized eigenvectors so that $U$ defines a right-hand triad. This can be accomplished by requiring that ${ \bf u } _ { 1 } \times { \bf u } _ { 2 } = { \bf u } _ { 3 }$ .

The Euler angles are defined in Fig. 4.16.2. The first rotation is about the $z$ axis through the angle $\phi$ and takes the unprimed frame into the $\left( \begin{array} { l l } { \mathbf { \Phi } } & { \mathbf { \Phi } } \end{array} \right) ^ { \prime \prime \prime }$ frame. The second rotation is about the $x ^ { \prime \prime \prime }$ axis through the angle $\theta$ to the $( \mathrm { ~  ~ \sigma ~ } ) ^ { \prime \prime }$ frame, and the final rotation is about the $z ^ { \prime \prime }$ axis through the angle $\psi$ to the $( \quad ) ^ { \prime }$ or principal axes frame (Reddy and Rasmussen, 1990). This transformation is analogous to that of transforming Earth-centered, Earth-fix ed coordinates into orbital plane coordinates with the $x ^ { \prime }$ axis through perigee, the $z ^ { \prime }$ axis along the angular momentum vector, and the $y ^ { \prime }$ axis completing the right-hand triad. The transpose of the transformation matrix that accomplishes this is the matrix we have identified as $U$ ; that is, $\mathbf { x } ^ { \prime } = U ^ { T } \mathbf { x }$ where

$$
U = \left[ \begin{array} { c c c } { { C _ { \phi } C _ { \psi } - C _ { \theta } S _ { \phi } S _ { \psi } } } & { { - C _ { \phi } S _ { \psi } - C _ { \theta } S _ { \phi } C _ { \psi } } } & { { S _ { \theta } S _ { \phi } } } \\ { { S _ { \phi } C _ { \psi } + C _ { \theta } C _ { \phi } S _ { \psi } } } & { { - S _ { \phi } S _ { \psi } + C _ { \theta } C _ { \phi } C _ { \psi } } } & { { - S _ { \theta } C _ { \phi } } } \\ { { S _ { \theta } S _ { \psi } } } & { { S _ { \theta } C _ { \psi } } } & { { C _ { \theta } } } \end{array} \right] ,
$$

and where $C$ and $S$ represent cosine and sine, respectively. The Euler angles are given by

$$
\begin{array} { r l } & { \phi = \mathrm { a t a n 2 } \left[ \cfrac { U _ { 1 3 } } { - U _ { 2 3 } } \right] , 0 \leq \phi \leq 2 \pi } \\ & { \theta = \mathrm { a c o s } \left[ U _ { 3 3 } \right] , 0 \leq \theta \leq \pi } \\ & { \psi = \mathrm { a t a n 2 } \left[ \cfrac { U _ { 3 1 } } { U _ { 3 2 } } \right] , 0 \leq \psi \leq 2 \pi . } \end{array}
$$

Example: Consider a normally distributed 2D random vector, $\mathbf { x }$ , where

$$
\mathbf { x } \sim N ( 0 , P ) ,
$$

and

$$
P = \left[ { \begin{array} { l l } { 4 } & { 2 } \\ { 2 } & { 2 } \end{array} } \right] .
$$

Sketch the 1-, 2-, and $3 { - } \sigma$ probability ellipses.

The eigenvalues are given by the polynomial

$$
| P - \lambda I | = 0 ,
$$

or

$$
\begin{array} { r } { \left| \begin{array} { c c } { 4 - \lambda } & { 2 } \\ { 2 } & { 2 - \lambda } \end{array} \right| = 0 ; } \end{array}
$$

hence,

$$
\lambda ^ { 2 } - 6 \lambda + 4 = 0 ,
$$

and

$$
\lambda _ { 1 } = 5 . 2 3 6 , \quad \lambda _ { 2 } = 0 . 7 6 4 .
$$

The corresponding eigenvectors are given by

$$
[ P - \lambda _ { i } I ] { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \end{array} \right] } = 0 , \quad i = 1 , 2 .
$$

The normalized eigenvectors are given by

$$
U = \left[ \begin{array} { c c } { { . 8 5 1 } } & { { - . 5 2 6 } } \\ { { . 5 2 6 } } & { { . 8 5 1 } } \end{array} \right] .
$$

The angle between the principal and original axes system is obtained by recognizing that the coordinate transformation matrix is given by (this can be determined by setting $\theta = \psi = 0$ in Eq. (4.16.11))

$$
U = \left[ \begin{array} { l l } { { \cos \phi } } & { { - \sin \phi } } \\ { { \sin \phi } } & { { \phantom { - } \cos \phi } } \end{array} \right] .
$$

Hence,

$$
\phi = \tan ^ { - 1 } { \frac { \sin \phi } { \cos \phi } } = 3 1 . 7 ^ { \circ }
$$

where $\phi$ is the angle between the $x _ { 1 }$ and $x _ { 1 } ^ { \prime }$ axes.

The semimajor axes $a _ { i }$ and minor axes $b _ { i }$ are given by

$$
\begin{array} { l } { { a _ { i } = \sqrt { \ell _ { i } ^ { 2 } \lambda \left( \mathrm { M a x } \right) } \ ~ } } \\ { { \ ~ } } \\ { { b _ { i } = \sqrt { \ell _ { i } ^ { 2 } \lambda ( \mathrm { M i n } ) } \ } } \end{array} { } i = 1 , 2 , 3 ; \ \ell _ { 1 } = 1 , \ \ell _ { 2 } = 2 , \ \ell _ { 3 } = 3
$$

with numerical values,

$$
\begin{array} { l l l } { { a _ { 1 } = 2 . 2 9 , } } & { { a _ { 2 } = 4 . 5 8 , } } & { { a _ { 3 } = 6 . 8 6 } } \\ { { b _ { 1 } = 0 . 8 7 , } } & { { b _ { 2 } = 1 . 7 5 , } } & { { b _ { 3 } = 2 . 6 2 } } \end{array} .
$$

The error ellipses can now be constructed:

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0004_pages_0211-0280/auto/images/168c0417dcfebcac5191cd0692ce8a9b9b1754b12b6bf5c86131c1d9a8531660.jpg)

# 4.16.1 TRANSFORMATION OF THE COVARIANCE MATRIX BETWEEN COORDINATE SYSTEMS

Sometimes it is desirable to transform the state vector and the estimation error covariance into alternate coordinate systems. For example, it may be of interest to view these quantities in a radial, transverse, and normal (RTN) system. Here the transverse direction is normal to the radius vector and the normal direction lies along the instantaneous angular momentum vector. RTN forms a right-hand triad.

The general transformation between any two coordinate frames (say prime to unprime) for a position vector is given by

$$
\mathbf { r } = \gamma \mathbf { r } ^ { \prime } + \mathbf { a } ,
$$

where $\gamma$ is an orthogonal transformation matrix, $\mathbf { r }$ is the vector in the unprimed frame, and a is the vector offset of the origin of the two systems expressed in the unprimed frame. Generally a will be zero unless, for example, we are transforming from a geocentric to a topocentric frame.

The velocity transforms according to

$$
\dot { \mathbf { r } } = \gamma \dot { \mathbf { r } } ^ { \prime } + \dot { \gamma } \mathbf { r } ^ { \prime } .
$$

Generally $\dot { \gamma }$ will be zero unless we are transforming from a rotating to a nonrotating frame or vice versa; for example, Earth-centered-Earth-fix ed to Earthcentered inertial (ECEF to ECI ). Let the unprimed system be the inertial, nonrotating frame. It can be shown (Wiesel, 1997) that ${ \dot { \gamma } } \mathbf { r } ^ { \prime } = { \boldsymbol { \omega } } \times \mathbf { r }$ , where $\omega$ is the angular velocity vector of the rotating frame expressed in the nonrotating frame coordinate system.

The transformation we want is ECI to RTN. We assume that the RTN frame is fix ed to the osculating orbit at each point in time; hence, $\dot { \gamma } = 0$ and

$$
\left[ \begin{array} { l } { \mathbf { r } } \\ { \mathbf { v } } \\ { \mathbf { V } } \end{array} \right] _ { \mathrm { R T N } } = \left[ \begin{array} { l l } { \gamma } & { \mathrm { ~  ~ 0 ~ } } \\ { \mathrm { ~  ~ 0 ~ } } & { \gamma } \end{array} \right] \left[ \begin{array} { l } { \mathbf { r } } \\ { \mathbf { v } } \\ { \mathbf { E C I } } \end{array} \right] _ { \mathrm { E C I } } .
$$

The covariance of the estimation error is transformed as follows:

$$
[ \hat { \bf x } - { \bf x } ] _ { \mathrm { R T N } } = \psi [ \hat { \bf x } - { \bf x } ] _ { \mathrm { E C I } } ,
$$

where

$$
\psi = \left[ \begin{array} { c c c } { \gamma } & { 0 } & { 0 } \\ { 0 } & { \gamma } & { 0 } \\ { 0 } & { 0 } & { I } \end{array} \right] \mathrm { ~ a n d ~ } \left[ \hat { \mathbf { x } } - \mathbf { x } \right] = \left[ \begin{array} { c c c } { \hat { \mathbf { r } } - \mathbf { r } } \\ { \hat { \mathbf { v } } - \mathbf { v } } \\ { \hat { \boldsymbol { \beta } } - \boldsymbol { \beta } } \end{array} \right] ,
$$

and r, $\mathbf { v }$ , and $\beta$ represent the true values of the position, velocity, and all other quantities in the state vector, respectively. It is assumed that none of the elements of $\beta$ are affected by the coordinate transformation. The desired covariance is given by

$$
\begin{array} { r l } & { P _ { \mathrm { R T N } } = E \left[ ( \hat { \mathbf { x } } - \mathbf { x } ) ( \hat { \mathbf { x } } - \mathbf { x } ) ^ { T } \right] _ { \mathrm { R T N } } } \\ & { \qquad = \psi E \left[ ( \hat { \mathbf { x } } - \mathbf { x } ) ( \hat { \mathbf { x } } - \mathbf { x } ) ^ { T } \right] _ { \mathrm { E C I } } \psi ^ { T } . } \end{array}
$$

The elements of $\gamma$ for the ECI to RTN transformation are given by

$$
\begin{array} { r l } & { \mathbf { u } _ { \mathrm { R } } = \frac { \mathbf { r } ^ { * } } { | \mathbf { r } ^ { * } | } = \epsilon _ { X } \mathbf { i } + \epsilon _ { Y } \mathbf { j } + \epsilon _ { Z } \mathbf { k } } \\ & { \mathbf { u } _ { \mathrm { T } } = \mathbf { u } _ { N } \times \mathbf { u } _ { R } = \delta _ { X } \mathbf { i } + \delta _ { Y } \mathbf { j } + \delta _ { Z } \mathbf { k } } \\ & { \mathbf { u } _ { N } = \frac { \mathbf { r } ^ { * } \times \mathbf { v } ^ { * } } { | \mathbf { r } ^ { * } \times \mathbf { v } ^ { * } | } = \alpha _ { X } \mathbf { i } + \alpha _ { Y } \mathbf { j } + \alpha _ { Z } \mathbf { k } , } \end{array}
$$

where $\mathbf { u } _ { \mathrm { R } }$ , uT, $\mathbf { u } _ { \mathrm { N } }$ are unit vectors in the RTN frame, i, j, and $\mathbf { k }$ are unit vectors in the ECI frame, and $\mathbf { r } ^ { * }$ and $\mathbf { v } ^ { * }$ are the position and velocity vectors of the reference orbit.

Equation (4.16.20) may be written

$$
\left[ \begin{array} { l } { \mathbf { u } _ { \mathrm { R } } } \\ { \mathbf { u } _ { \mathrm { T } } } \\ { \mathbf { u } _ { \mathrm { N } } } \end{array} \right] = \left[ \begin{array} { l l l } { \epsilon _ { X } ~ \epsilon _ { Y } ~ \epsilon _ { Z } } \\ { \delta _ { X } ~ \delta _ { Y } ~ \delta _ { Z } } \\ { \alpha _ { X } ~ \alpha _ { Y } ~ \alpha _ { Z } } \end{array} \right] \left[ \begin{array} { l } { \mathbf { i } } \\ { \mathbf { j } } \\ { \mathbf { k } } \end{array} \right] .
$$

Hence, the transformation matrix relating the RTN and ECI frame is

$$
\gamma = \left[ \begin{array} { l l l } { \epsilon _ { X } } & { \epsilon _ { Y } } & { \epsilon _ { Z } } \\ { \delta _ { X } } & { \delta _ { Y } } & { \delta _ { Z } } \\ { \alpha _ { X } } & { \alpha _ { Y } } & { \alpha _ { Z } } \end{array} \right] .
$$

# 4.17 COMBINING ESTIMATES

Assume we are given two unbiased and uncorrelated estimates $\hat { \mathbf { x } } _ { 1 }$ and $\hat { \mathbf { x } } _ { 2 }$ for the $n$ -vector $\mathbf { x }$ . Assume that the associated estimation errors $\pmb { \eta } _ { 1 }$ and $\eta _ { 2 }$ are Gaussian with covariance matrices $P _ { 1 }$ and $P _ { 2 }$ . Our objective is to establish a performance index and determine the combination of $\hat { \mathbf { x } } _ { 1 }$ and $\hat { \mathbf { x } } _ { 2 }$ that is an optimal, unbiased $\left( E [ \hat { \mathbf { x } } ] = \mathbf { x } \right)$ ) estimate of $\mathbf { x }$ .

Using the fact that the errors in $\hat { \mathbf { x } } _ { 1 }$ and $\hat { \mathbf { x } } _ { 2 }$ are zero mean and uncorrelated (hence, being Gaussian, they are independent), the joint density function for the

estimation errors, $\pmb { \eta } _ { 1 }$ and $\eta _ { 2 }$ , where

$$
\begin{array} { r } { \pmb { \eta } _ { 1 } = \hat { \bf x } _ { 1 } - { \bf x } } \\ { \pmb { \eta } _ { 2 } = \hat { \bf x } _ { 2 } - { \bf x } , } \end{array}
$$

is given by

$$
f ( \pmb { \eta } _ { 1 } , \pmb { \eta } _ { 2 } ) = f ( \pmb { \eta } _ { 1 } ) f ( \pmb { \eta } _ { 2 } )
$$

$$
\begin{array} { l } { { = \displaystyle \frac { 1 } { ( 2 \pi ) ^ { n / 2 } } \frac { 1 } { | P _ { 1 } | ^ { \frac { 1 } { 2 } } } e ^ { - \frac { 1 } { 2 } ( \pmb { \eta } _ { 1 } ^ { T } P _ { 1 } ^ { - 1 } \pmb { \eta } _ { 1 } ) } } } \\ { { \times \displaystyle \frac { 1 } { ( 2 \pi ) ^ { n / 2 } | P _ { 2 } | ^ { \frac { 1 } { 2 } } } e ^ { - \frac { 1 } { 2 } ( \pmb { \eta } _ { 2 } ^ { T } P _ { 2 } ^ { - 1 } \pmb { \eta } _ { 2 } ) } . } } \end{array}
$$

The method of Maximum Likelihood selects the value of $\mathbf { x }$ that maximizes the likelihood function $L = f ( \eta _ { 1 } , \eta _ { 2 } )$ . Because the density functions involved are Gaussian, all classical estimation techniques, Bayesian, Minimum Variance, or Maximum Likelihood, will yield the same results.

Maximizing the logarithm of $L$ is equivalent to maximizing $L$ . Hence, we wish to maximize

$$
\begin{array} { r l } & { \ln { L } = K - 1 / 2 \big [ \pmb { \eta } _ { 1 } ^ { T } P _ { 1 } ^ { - 1 } \pmb { \eta } _ { 1 } + \pmb { \eta } _ { 2 } ^ { T } P _ { 2 } ^ { - 1 } \pmb { \eta } \big ] } \\ & { \qquad = K - 1 / 2 \big [ ( \hat { \bf x } _ { 1 } - { \bf x } ) ^ { T } P _ { 1 } ^ { - 1 } ( \hat { \bf x } _ { 1 } - { \bf x } ) } \\ & { \qquad + ( \hat { \bf x } _ { 2 } - { \bf x } ) ^ { T } P _ { 2 } ^ { - 1 } ( \hat { \bf x } _ { 2 } - { \bf x } ) \big ] } \end{array}
$$

where

$$
K = \ln \left( \frac { 1 } { ( 2 \pi ) ^ { \eta / 2 } } \frac { 1 } { | P _ { 1 } | ^ { 1 / 2 } } \right) + \ln \left( \frac { 1 } { ( 2 \pi ) ^ { \eta / 2 } } \frac { 1 } { | P _ { 2 } | ^ { 1 / 2 } } \right) .
$$

Using Eq. (B.7.3) of Appendix B, for a maximum of $\ln { \cal L }$ , it is necessary that

$$
\frac { d \ln { \cal L } } { d { \bf x } } = - \frac { 1 } { 2 } \left[ - 2 P _ { 1 } ^ { - 1 } ( \hat { \bf x } _ { 1 } - { \bf x } ) - 2 P _ { 2 } ^ { - 1 } ( \hat { \bf x } _ { 2 } - { \bf x } ) \right] = 0 .
$$

Hence,

$$
P _ { 1 } ^ { - 1 } ( \hat { \bf x } _ { 1 } - \hat { \bf x } ) + P _ { 2 } ^ { - 1 } \left( \hat { \bf x } _ { 2 } - \hat { \bf x } \right) = 0
$$

and

$$
{ \hat { \mathbf { x } } } = ( P _ { 1 } ^ { - 1 } + P _ { 2 } ^ { - 1 } ) ^ { - 1 } [ P _ { 1 } ^ { - 1 } { \hat { \mathbf { x } } } _ { 1 } + P _ { 2 } ^ { - 1 } { \hat { \mathbf { x } } } _ { 2 } ] .
$$

Also,

$$
\frac { d ^ { 2 } \ln L } { d \mathbf { x } ^ { 2 } } = - ( P _ { 1 } ^ { - 1 } + P _ { 2 } ^ { - 1 } ) 
$$

which is negative definite; therefore, this is a maximum of $\ln { \cal L }$ .

It is easily shown that $\hat { \bf x }$ is unbiased,

$$
\begin{array} { r l } & { E \left[ \hat { \mathbf { x } } \right] = ( P _ { 1 } + P _ { 2 } ) ^ { - 1 } [ P _ { 1 } ^ { - 1 } E \left( \hat { \mathbf { x } } _ { 1 } \right) + P _ { 2 } ^ { - 1 } E \left( \hat { \mathbf { x } } _ { 2 } \right) ] } \\ & { \qquad = \mathbf { x } , } \end{array}
$$

since $E ( \hat { \mathbf { x } } _ { 1 } ) = E ( \hat { \mathbf { x } } _ { 2 } ) = \mathbf { x }$ .

The estimation error covariance, $P$ , associated with $\hat { \bf x }$ is given by

$$
P = E [ ( \hat { \mathbf { x } } - \mathbf { x } ) ( \hat { \mathbf { x } } - \mathbf { x } ) ^ { T } ] ,
$$

where

$$
\hat { \mathbf { x } } = \gamma [ P _ { 1 } ^ { - 1 } \hat { \mathbf { x } } _ { 1 } + P _ { 2 } ^ { - 1 } \hat { \mathbf { x } } _ { 2 } ] ,
$$

and

$$
\gamma \equiv ( P _ { 1 } ^ { - 1 } + P _ { 2 } ^ { - 1 } ) ^ { - 1 } .
$$

Using Eqs. (4.17.1) and the fact that

$$
E \left[ \pmb { \eta } _ { 1 } \right] = E \left[ \pmb { \eta } _ { 2 } \right] = 0 ,
$$

$$
E \left[ \pmb { \eta } _ { 1 } \pmb { \eta } _ { 1 } ^ { T } \right] = P _ { 1 } , E \left[ \pmb { \eta } _ { 2 } \pmb { \eta } _ { 2 } ^ { T } \right] = P _ { 2 } , E \left[ \pmb { \eta } _ { 1 } \pmb { \eta } _ { 2 } ^ { T } \right] = 0 ,
$$

we can write

$$
{ \hat { \bf x } } = \gamma [ P _ { 1 } ^ { - 1 } ( { \bf x } + \pmb { \eta } _ { 1 } ) + P _ { 2 } ^ { - 1 } ( { \bf x } + \pmb { \eta } _ { 2 } ) ] .
$$

Hence,

$$
\begin{array} { r } { \hat { \mathbf { x } } - \mathbf { x } = \gamma [ P _ { 1 } ^ { - 1 } \pmb { \eta } _ { 1 } + P _ { 2 } ^ { - 1 } \pmb { \eta } _ { 2 } ] , } \end{array}
$$

therefore,

$$
\begin{array} { r l } & { P = \gamma E \left\{ [ P _ { 1 } ^ { - 1 } \pmb { \eta } _ { 1 } + P _ { 2 } ^ { - 1 } \pmb { \eta } _ { 2 } ] [ P _ { 1 } ^ { - 1 } \pmb { \eta } _ { 1 } + P _ { 2 } ^ { - 1 } \pmb { \eta } _ { 2 } ] ^ { T } \right\} \gamma } \\ & { \quad = \gamma [ P _ { 1 } ^ { - 1 } P _ { 1 } P _ { 1 } ^ { - 1 } + P _ { 2 } ^ { - 1 } P _ { 2 } P _ { 2 } ^ { - 1 } ] \gamma } \\ & { \quad = \gamma } \\ & { \quad = ( P _ { 1 } ^ { - 1 } + P _ { 2 } ^ { - 1 } ) ^ { - 1 } . } \end{array}
$$

It is not necessary to assume that the errors in $\hat { \mathbf { x } } _ { 1 }$ and $\hat { \mathbf { x } } _ { 2 }$ are Gaussian. Knowing that the two estimates $\hat { \mathbf { x } } _ { 1 }$ and $\hat { \mathbf { x } } _ { 2 }$ are unbiased and uncorrelated, we could have simply chosen to minimize a performance index that yields a value of $\mathbf { x }$ that minimizes the weighted sum of squares of the estimation errors for $\hat { \bf x } _ { 1 }$ and $\hat { \mathbf { x } } _ { 2 }$ ,

$$
Q = \frac { 1 } { 2 } \left[ ( \hat { \bf x } _ { 1 } - { \bf x } ) ^ { T } P _ { 1 } ^ { - 1 } ( \hat { \bf x } _ { 1 } - { \bf x } ) + ( \hat { \bf x } _ { 2 } - { \bf x } ) ^ { T } P _ { 2 } ^ { - 1 } ( \hat { \bf x } _ { 2 } - { \bf x } ) \right] .
$$

Choosing $\mathbf { x }$ to minimize $Q$ will yield the result given by Eq. (4.17.4).

If there are $n$ independent solutions to combine, it is easily shown that

$$
\hat { \mathbf { x } } = \left( \sum _ { i = 1 } ^ { n } P _ { i } ^ { - 1 } \right) ^ { - 1 } \sum _ { i = 1 } ^ { n } P _ { i } ^ { - 1 } \hat { \mathbf { x } } _ { i } .
$$

# 4.18 REFERENCES

Battin, R., An Introduction to the Mathematics and Methods of Astrodynamics, American Institute of Aeronautics and Astronautics, Reston, VA, 1999.

Bertiger, W., Y. Bar-Sever, E. Christensen, E. Davis, J. Guinn, B. Haines, R. Ibanez-Meier, J. Jee, S. Lichten, W. Melbourne, R. Muellerschoen, T. Munson, Y. Vigue, S. Wu, T. Yunck, B. Schutz, P. Abusali, H. Rim, W. Watkins, and P. Willis , “GPS precise tracking of TOPEX/Poseidon: Results and implications,” J. Geophys. Res., Vol. 99, No. C12, pp. 24,449–24,462, December 15, 1995.

Bierman, G. J., Factorization Methods for Discrete Sequential Estimation, Academic Press, New York, 1977.

Bjorck, A., ¨ Numerical Methods for Least Squares Problems, SIAM, Philadelphia, PA, 1996.

Bryson, A. E., and Y. C. Ho, Applied Optimal Control, Hemisphere Publishing Corp., Washington, DC, 1975.

Bucy, R., and P. Joseph, Filtering for Stochastic Processes, John Wiley & Sons, Inc., New York, 1968.

Cruickshank, D. R., Genetic Model Compensation: Theory and Applications, Ph. D. Dissertation, The University of Colorado at Boulder, 1998.

Dahlquist, G., and A. Bjorck, ¨ Numerical Methods, Prentice-Hall, Englewood Cliffs, NJ, 1974 (translated to English: N. Anderson).

Desai, S. D., and B. J. Haines, “N ear real-time GPS-based orbit determination and sea surface height observations from the Jason-1 mission,” Marine Geodesy, Vol. 26, No. 3–4, pp. 187–199, 2003.

Deutsch, R., Estimation Theory, Prentice-Hall, Inc., Englewood Cliffs, NJ, 1965.

Dorroh, W. E., and T. H. Thornton, “Strate gies and systems for navigation corrections,” Astronautics and Aeronautics, Vol. 8, No. 5, pp. 50–55, May 1970.

Fisher, R. A., “On an absolute criteria for fitti ng frequency curves,” Mess. Math., Vol. 41, pp. 155–160, 1912.

Gauss, K. F., Theoria Motus Corporum Coelestium, 1809 (Translated into English: Davis, C. H., Theory of the Motion of the Heavenly Bodies Moving about the Sun in Conic Sections, Dover, New York, 1963).

Gelb, A. (ed.), Applied Optimal Estimation, MIT Press, Cambridge, MA, 1974.

Goldstein, D. B., G. H. Born, and P. Axelrad, “Real-ti me, autonomous, precise orbit determination using GPS,” J. ION, Vol. 48, No. 3, pp. 169–179, Fall 2001.

Grewal, M. S., and A. P. Andrews, Kalman Filtering: Theory and Practice, Prentice Hall, 1993.

Ingram, D. S., Orbit determination in the presence of unmodeled accelerations, Ph.D. Dissertation, The University of Texas at Austin, 1970.

Ingram, D. S., and B. D. Tapley, “Lunar orbit determination in the presence of unmodeled accelerations,” Celest. Mech., Vol. 9, No. 2, pp. 191–211, 1974.

Jazwinski, A. H., Stochastic Process and Filtering Theory, Academic Press, New York, 1970.

Kalman, R. E., “A New Approach to Linear Filtering and Prediction Theory,” J. Basic Eng., Vol. 82, Series E, No. 1, pp. 35–45, March, 1960.

Kreyszig, E., Advanced Engineering Mathematics, John Wiley & Sons, Inc., New York, 1993.

Lawson, C. L., and R. J. Hanson, Solving Least Squares Problems, Prentice-Hall, Inc. Englewood Cliffs, NJ, 1974 (republished by SIAM, Philadelphia, PA, 1995).

Lichten, S. M., “Estima tion and filteri ng for high precision GPS positioning applications,” Manuscripta Geodaetica, Vol. 15, pp. 159–176, 1990.

Liebelt, P. B., An Introduction to Optimal Estimation, Addison-Wesley, Reading, MA, 1967.

Lutchke, S. B., N. P. Zelenski, D. D. Rowlands, F. G. Lemoine, and T. A. Williams, “The 1-centimeter orbit: Jason-1 precision orbit determination using GPS, SLR, DORIS and altimeter data,” Marine Geodesy, Vol. 26, No. 3-4, pp. 399–421, 2003.

Marshall, J. A., N. P. Zelensky, S. M. Klosko, D. S. Chinn, S. B. Luthcke, K. E. Rachlin, and R. G. Williamson, “The temporal and spatial characteristics of TOPEX/Poseidon radial orbit error,” J. Geophys. Res., Vol. 99, No. C12, pp. 25,331–25,352, December 15, 1995.

Maybeck, P. S., Stochastic Models, Estimation and Control, Vol. 1, Academic Press, 1979.

Mikhail, E. M., Observations and Least Squares, University Press of America, Lanham, MD, 1976.

Moler, C., and C. Van Loan, “Ninetee n dubious ways to compute the exponential of a matrix,” SIAM Review, Vol. 20, No. 4, pp. 801–836, October 1978.

Montenbruck, O., and E. Gill, Satellite Orbits: Models, Methods and Applications, Springer, 2001.

Myers, K. A., Filtering theory methods and applications to the orbit determination problem for near-Earth satellites, Ph.D. Dissertation, The University of Texas at Austin, November 1973.1973.

Rausch, H. E., F. Tung, and C. T. Striebel, “M aximum likelihood estimates of linear dynamic systems,” AIAA J., Vol. 3, No. 7, pp. 1445–1450, August 1965.

Reddy, J. N., and M. L. Rasmussen, Advanced Engineering Analysis, Robert E. Krieger Publishing Co., Malabar, Florida, 1990.

Schlee, F. H., C. J. Standish, and N. F. Toda, “Di vergence in the Kalman filter ,” AIAA J., Vol. 5, No. 6, pp. 1114–1120, June 1967.

Schutz, B., B. D. Tapley, P. Abusali, H. Rim, “Dynamic orbit determination using GPS measurements from TOPEX/Poseidon,” Geophys. Res. Ltrs., Vol. 21, No. 19, pp. 2179–2182, 1994.

Sorenson, H. W. (ed.), Kalman Filtering: Theory and Applications, IEEE Press, 1985.

Swerling, P., “First order error propagation in a stagewise differential smoothing procedure for satellite observations,” J. Astronaut. Sci., Vol. 6, pp. 46–52, 1959.

Tapley, B. D., “Statist ical orbit determination theory,” in Recent Advances in Dynamical Astronomy, B. D. Tapley and V. Szebehely (eds.), D. Reidel, pp. 396–425, 1973.

Tapley, B. D.,“ Fundamentals of orbit determination”, in Theory of Satellite Geodesy and Gravity Field Determination, Vol. 25, pp. 235-260, Springer-Verlag, 1989.

Tapley, B. D., and D. S. Ingram, “O rbit determination in the presence of unmodeled accelerations”, Trans. Auto. Cont., Vol. AC-18, No. 4, pp. 369–373, August, 1973.

Tapley, B. D., J. Ries, G. Davis, R. Eanes, B. Schutz, C. Shum, M. Watkins, J. Marshall, R. Nerem, B. Putney, S. Klosko, S. Luthcke, D. Pavlis, R. Williamson, and N. P. Zelensky, “Preci sion orbit determination for TOPEX/ Poseidon,” J. Geophys. Res., Vol. 99, No. C12, pp. 24,383–24,404, December 15, 1994.

Tapley, B. D., M. Watkins, J. Ries, G. Davis, R. Eanes, S. Poole, H. Rim, B. Schutz, C. Shum, R. Nerem, F. Lerch, J. Marshall, S. Klosko, N. Pavlis, and R. Williamson, “The Joint Gravity Model 3”, J. Geophys. Res., Vol. 101, No. B12, pp. 28,029–28,049, December 10, 1996.

Walpole, R. E., R. H. Myers, S. L. Myers, and Y. Keying, Probability and Statistics for Engineers and Scientists, Prentice Hall, Englewood Cliffs, NJ, 2002.

Wiesel, W. E., Spaceflight Dynamics, McGraw-Hill, 1997.

# 4.19 EXERCISES

(1) A dynamical system is described by

$$
\dot { \mathbf { X } } ( t ) = \boldsymbol { A } \mathbf { X } ( t ) .
$$

Given that the state transition matrix for this system is

$$
\Phi = \left[ { \begin{array} { l } { e ^ { - 2 a t } 0 } \\ { 0 } \end{array} } \right] ,
$$

determine the matrix $A$ .

(2) Given the solution to the differential equation

$$
\dot { \mathbf { x } } ( t _ { i } ) = A ( t _ { i } ) \mathbf { x } ( t _ { i } )
$$

is

$$
\mathbf { x } ( t _ { i } ) = \boldsymbol \Phi ( t _ { i } , t _ { k } ) \mathbf { x } ( t _ { k } )
$$


<!-- chunk 0005: pages 281-350 -->
where

$$
\Phi ( t _ { k } , t _ { k } ) = I ,
$$

show that

$$
\begin{array} { r l } & { \dot { \Phi } ( t _ { i } , t _ { k } ) = A ( t _ { i } ) \Phi ( t _ { i } , t _ { k } ) } \\ & { \Phi ( t _ { i } , t _ { j } ) = \Phi ( t _ { i } , t _ { k } ) \Phi ( t _ { k } , t _ { j } ) } \\ & { \Phi ^ { - 1 } ( t _ { i } , t _ { k } ) = \Phi ( t _ { k } , t _ { i } ) } \\ & { \dot { \Phi } ^ { - 1 } ( t _ { i } , t _ { k } ) = - \Phi ^ { - 1 } ( t _ { i } , t _ { k } ) A ( t _ { i } ) . } \end{array}
$$

(3) Given a vector of observations, $\mathbf { y } = H \mathbf { x } + \epsilon$ with weighting matrix $W$ , and $a$ priori information, $( \overline { { \mathbf { x } } } , \overline { { W } } )$ , determine the least squares estimate for $\hat { \bf x }$ . (Note that $W$ corresponds to $R ^ { - 1 }$ and $\overline { W }$ to $\bar { P } _ { 0 } ^ { - 1 }$ in the case where we have statistical information on $\epsilon$ and $\bar { \bf x }$ .) Let the performance index be

$$
J ( x ) = 1 / 2 ~ \epsilon ^ { T } W \epsilon + 1 / 2 ~ \overline { { { \eta } } } ^ { T } \overline { { { W } } } \overline { { { \eta } } }
$$

where $\overline { { \eta } }$ is the error in the $a$ priori estimate $\overline { { \mathbf { x } } }$ ,

$$
\overline { { \pmb { \eta } } } = \overline { { \bf x } } - { \bf x } .
$$

Answer: $\hat { \mathbf { x } } = ( H ^ { T } W H + \overline { { W } } ) ^ { - 1 } ( H ^ { T } W \mathbf { y } + \overline { { W } } \overline { { \mathbf { x } } } )$

(4) Determine the state transition matrix associated with the matrix

$$
A = \left[ \begin{array} { c c } { { a } } & { { 0 } } \\ { { b } } & { { g } } \end{array} \right] , a \neq g , \mathrm { a n d } \dot { \Phi } = A \Phi , \Phi \left( t _ { 0 } , t _ { 0 } \right) = I .
$$

(5) Express the linear system of equations

$$
{ \ddot { x } } = - a b x
$$

in the matrix form

$$
{ \dot { \mathbf { x } } } = A \mathbf { x } ,
$$

where

$$
\mathbf { x } = { \left[ \begin{array} { l } { x } \\ { \dot { x } } \end{array} \right] } .
$$

Find the state transition matrix for this system.

(6) Show that the matrix

$$
\Phi \left( t , t _ { 0 } \right) = { \left[ \begin{array} { l l } { 3 e ^ { a t } } & { 0 } \\ { 0 } & { 2 e ^ { - b t } } \end{array} \right] }
$$

satisfies the relation

$$
{ \dot { \Phi } } = A \Phi
$$

but that $\Phi ( t , t _ { 0 } )$ is not a transition matrix. (Assume $t _ { 0 } = 0$ .)

(7) Show that whenever $\Phi ( t , t _ { k } )$ satisfies Eq. (4.2.22), it is symplectic; that is, $\Phi ( t , t _ { k } ) ^ { T } J \phi ( t , t _ { k } ) = J$ .

(8) The displacement of a particle, under the influence of a constant acceleration $\ddot { x } _ { 0 }$ , can be expressed as

$$
x ( t ) = x _ { 0 } + \dot { x } _ { 0 } t + \frac { 1 } { 2 } \ddot { x } _ { 0 } t ^ { 2 } ,
$$

where $x _ { 0 }$ is the initial displacement, ${ \dot { x } } _ { 0 }$ is the initial velocity, and $\ddot { x } _ { 0 }$ is the acceleration at the initial time, $t _ { 0 } = 0$ .

(a) By successive differentiation of this expression, show that the linear system

$$
{ \dot { \mathbf { x } } } = A \mathbf { x }
$$

describes the motion, where

$$
\mathbf { x } = { \left[ \begin{array} { l } { x } \\ { \dot { x } } \\ { \ddot { x } } \end{array} \right] } \ ; A = { \left[ \begin{array} { l } { 0 1 0 } \\ { 0 0 1 } \\ { 0 0 0 } \end{array} \right] } \ .
$$

(b) Prove that the transition matrix $\Phi ( t , t _ { 0 } )$ of the system in (a) is

$$
\Phi ( t , t _ { 0 } ) = \left[ \begin{array} { c c c } { { 1 } } & { { ( t - t _ { 0 } ) } } & { { ( t - t _ { 0 } ) ^ { 2 } / 2 } } \\ { { 0 } } & { { 1 } } & { { ( t - t _ { 0 } ) } } \\ { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right]
$$

first by differentiating $\Phi$ and showing that $\dot { \Phi } ( t , t _ { 0 } ) = A \Phi ( t , t _ { 0 } )$ where $\Phi ( t _ { 0 } , t _ { 0 } ) = I$ , and then by integrating this system of differential equations.

(c) Show that $\Phi ( t , t _ { 0 } )$ can be represented as

$$
\begin{array} { l } { \displaystyle \Phi ( t , t _ { 0 } ) = e ^ { A ( t - t _ { 0 } ) } } \\ { \displaystyle = I + \sum _ { n = 1 } ^ { \infty } \frac { 1 } { n ! } A ^ { n } ( t - t _ { 0 } ) ^ { n } . } \end{array}
$$

(d) Calculate $\Phi \left( t _ { 0 } , t \right)$ by direct inversion.

(e) Let $\Phi ^ { - 1 } ( t , t _ { 0 } ) = \Theta ( t , t _ { 0 } )$ and show that

$$
\dot { \Theta } ( t , t _ { 0 } ) = - \Theta ( t , t _ { 0 } ) A , \Theta \left( t _ { 0 } , t _ { 0 } \right) = I
$$

by integration and comparison with the results of $d$ .

(f) Calculate $\Phi \left( t _ { 2 } , t _ { 1 } \right)$ by finding the product $\Phi \left( t _ { 2 } , t _ { 0 } \right) \Phi \left( t _ { 0 } , t _ { 1 } \right)$ .

(g) Compare this result with the result obtained by integrating the equation

$$
\dot { \Phi } \left( t , t _ { 1 } \right) = A \Phi \left( t , t _ { 1 } \right) ,
$$

with the condition $\Phi \left( t _ { 1 } , t _ { 1 } \right) = I$ .

(h) Show that

$$
\frac { \partial \mathbf { x } } { \partial \mathbf { x } _ { 0 } } = \Phi \left( t , t _ { 0 } \right) ,
$$

where ${ \bf x } ^ { T } = ( x \dot { x } \ddot { x } )$ and $\mathbf { x } _ { 0 } ^ { T } = \left( x _ { 0 } \ \dot { x } _ { 0 } \ \ddot { x } _ { 0 } \right)$ .

(9) The equations of motion for a satellite moving in the vicinity of a body with a homogeneous mass distribution can be expressed as

$$
{ \ddot { \mathbf { r } } } = - { \frac { \mu \mathbf { r } } { r ^ { 3 } } }
$$

where $\mathbf { r }$ is the position vector, $\ddot { \mathbf { r } }$ is the acceleration vector, and where $r =$ $| \mathbf { r } |$ . Let ${ \textbf { v } } = { \dot { \textbf { r } } }$ denote the velocity vector, and express the equations in first-order form as

$$
\left[ \dot { \bar { \mathbf { r } } } \right] = \left[ \begin{array} { c } { \mathbf { v } } \\ { \dot { \mathbf { v } } } \end{array} \right] .
$$

(a) The relations that define the deviations from a given reference orbit due to deviations in $\mathbf { r }$ and $\mathbf { v }$ and $\mu$ at a given time $t _ { 0 }$ can be used to analyze the trajectory sensitivity. Show that

$$
{ \frac { d } { d t } } \left[ \delta \mathbf { r } \right] = { \left[ \begin{array} { l l } { ~ 0 } & { I } \\ { { \frac { \partial \mathbf { f } } { \partial \mathbf { r } } } } & { ~ 0 } \end{array} \right] } \left[ { \begin{array} { l } { \delta \mathbf { r } } \\ { \delta \mathbf { v } } \end{array} } \right] - \left[ { \begin{array} { l } { 0 } \\ { \mathbf { r } } \\ { r ^ { 3 } } \end{array} } \right] \delta \mu ,
$$

where

$$
\mathbf { f } = - { \frac { \mu \mathbf { r } } { r ^ { 3 } } }
$$

$$
- \frac { \partial \mathbf { f } } { \partial \mathbf { r } } = \left[ \begin{array} { c c c c } { \frac { \mu } { r ^ { 3 } } - 3 \mu \frac { x _ { 1 } ^ { 2 } } { r ^ { 5 } } } & { - 3 \mu \frac { x _ { 1 } x _ { 2 } } { r ^ { 5 } } } & { - 3 \mu \frac { x _ { 1 } x _ { 3 } } { r ^ { 5 } } } \\ { - 3 \mu \frac { x _ { 1 } x _ { 2 } } { r ^ { 5 } } } & { \frac { \mu } { r ^ { 3 } } - 3 \mu \frac { x _ { 2 } ^ { 2 } } { r ^ { 5 } } } & { - 3 \mu \frac { x _ { 2 } x _ { 3 } } { r ^ { 5 } } } \\ { - 3 \mu \frac { x _ { 1 } x _ { 3 } } { r ^ { 5 } } } & { - 3 \mu \frac { x _ { 2 } x _ { 3 } } { r ^ { 5 } } } & { \frac { \mu } { r ^ { 3 } } - 3 \mu \frac { x _ { 3 } ^ { 2 } } { r ^ { 5 } } } \end{array} \right] .
$$

Note that $\partial \mathbf { f } / \partial \mathbf { r }$ is symmetric.

(b) The constant $\mu$ is a physical constant and $\delta \mu$ represents the error in the knowledge of $\mu$ . Show that the error in $\mathbf { r } ( t )$ and $\mathbf { v } ( t )$ can be related to the error in $\mu$ by the following expression (Hint: Use the solution for $x ( t )$ given by Eq. (4.9.14).):

$$
{ \bigg [ } \delta \mathbf { r } ( t ) { \bigg ] } = \Phi ( t , t _ { 0 } ) { \bigg [ } { \delta \mathbf { r } _ { 0 } } { \bigg ] } - \delta \mu \int _ { t _ { 0 } } ^ { t } \Phi ( t , \tau ) { \left[ \begin{array} { l } { 0 } \\ { \mathbf { r } } \\ { r ^ { 3 } } \end{array} \right] } d \tau .
$$

(10) Assume an orbit plane coordinate system for Exercise 9 with $\mu = 1$ .

(a) Generate a “true” solution by numerically integrating the resulting differential equations

$$
\begin{array} { c } { \ddot { x } = - \displaystyle \frac { x } { r ^ { 3 } } } \\ { \ddot { y } = - \displaystyle \frac { y } { r ^ { 3 } } } \\ { r ^ { 2 } = x ^ { 2 } + y ^ { 2 } } \end{array}
$$

for the initial conditions

$$
\begin{array} { r } { \mathbf { X } ( t _ { 0 } ) = \left( \begin{array} { l } { x } \\ { y } \\ { \dot { x } } \\ { \dot { y } } \end{array} \right) _ { t = t _ { 0 } } = \left( \begin{array} { l } { 1 . 0 } \\ { 0 . 0 } \\ { 0 . 0 } \\ { 1 . 0 } \end{array} \right) . } \end{array}
$$

Save the values of the state vector $\mathbf { X } ( t _ { i } )$ for $t _ { i } = i * 1 0 . ; i = 0 , \ldots , 1 0$

(b) Perturb the previous set of initial conditions by an amount

$$
\mathbf { X } ^ { * } ( t _ { 0 } ) = \mathbf { X } ( t _ { 0 } ) - \delta \mathbf { X } ( t _ { 0 } )
$$

where

$$
\delta { \bf X } ( t _ { 0 } ) = \left( \begin{array} { c } { { 1 \times 1 0 ^ { - 6 } } } \\ { { - 1 \times 1 0 ^ { - 6 } } } \\ { { 1 \times 1 0 ^ { - 6 } } } \\ { { 1 \times 1 0 ^ { - 6 } } } \end{array} \right)
$$

and numerically integrate this “nomina l” trajectory along with the associated state transition matrix to find $\mathbf { X } ^ { * } ( t _ { i } )$ and $\Phi ( t _ { i } , t _ { 0 } )$ at $t _ { i } =$ $i * 1 0 . ; i = 0 , \dots , 1 0$ .

(c) For this problem, $\Phi ( t _ { i } , t _ { 0 } )$ is symplectic. Demonstrate this for $\Phi ( t _ { 1 0 0 } , t _ { 0 } )$ by multiplying it by $\Phi ^ { - 1 } ( t _ { 1 0 0 } , t _ { 0 } )$ , given by Eq. (4.2.22), and showing that the result is the identity matrix.

(d) Calculate the perturbation vector, $\delta { \bf X } ( t _ { i } )$ , by the following two methods:

$$
\begin{array} { r c l } { \delta \mathbf { X } ( t _ { i } ) = \mathbf { X } ( t _ { i } ) - \mathbf { X } ^ { * } ( t _ { i } ) } \\ { \delta \mathbf { X } ( t _ { i } ) = \Phi ( t _ { i } , t _ { 0 } ) \delta \mathbf { X } ( t _ { 0 } ) } \end{array}
$$

and compare the results of (1) and (2). A program such as Matlab works well for this problem.

(11) Show that if the acceleration on a spacecraft is derivable from a potential function,

$$
\ddot { \mathbf { r } } = \nabla U
$$

then the state transition matrix is symplectic; that is, Eq. (4.2.13) is true under the assumption that the state vector is

$$
\mathbf { x } = { \left[ \begin{array} { l } { \mathbf { r } } \\ { \mathbf { v } } \end{array} \right] } .
$$

(12) Given the spring-mass system, as shown,

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0005_pages_0281-0350/auto/images/748b6c26ef474be8c79cd7ffda227ab4229baebc628be89b83c37ffac827ff47.jpg)

$$
m { \ddot { x } } + c { \dot { x } } + k x + F \sin \omega t = 0 .
$$

Assume that we wish to estimate $x , \dot { x } , F , c$ , and $h$ using observations $\rho$ .   
Derive the $A$ and $\widetilde { H }$ matrix for this state vector.

(13) Given a point mass falling under the acceleration of gravity and being observed by range observations, $\rho$ , as shown. Determine the state transition matrix, and the $\widetilde { H }$ and $H$ matrices. Assume the state vector is to be estimated at $t _ { 0 } = 0$ .

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0005_pages_0281-0350/auto/images/96f2a59c0c4e37b50ed9365cbeb259df85732dbf9a966a661ab37f5045d21f35.jpg)

$$
\begin{array} { r } { \operatorname { l e t } { \mathbf { X } } = \left[ \begin{array} { l } { \begin{array} { l } { x } \\ { y } \\ { \dot { x } } \\ { \dot { y } } \\ { g } \\ { \dot { y } } \end{array} } \right] , \qquad \stackrel { \circledast } { \begin{array} { l } { ( } 0 . ~ t _ { 0 } ) } \\ { x = x _ { 0 } } \\ { \dot { x } = \dot { x } _ { 0 } } \\ { { y } = y _ { 0 } } \\ { \dot { y } = \dot { y } _ { 0 } } \end{array} }  \end{array} \end{array}
$$

(14) Given a simple pendulum with range observations $| \rho |$ , from a fix ed point, as shown in the figure.

(a) Write the equations of motion and form the observation-state matrix $\widetilde { \boldsymbol { H } } )$ and the state propagation matrix $( A )$ . Assume the state vector is

$$
\mathbf { X } = \left[ { \stackrel { \ominus } { \ominus } } \right] .
$$

(b) Assume small oscillations; that is, $\sin \Theta \approx \Theta$ , $\cos \Theta \approx 1$ . Solve the equations of motion and derive expressions for the state transition matrix.

(c) How does the assumption that $\Theta$ is small differ from a linearized formulation of this problem?

$$
\sum _ { \rho } ^ { | \star  } \sum _ { i = \pmb { \mathscr { S } } _ { 0 } } ^ { | \star  } x _ { 0 } \frac {  1 } {    } \sum _ { l } ^ { | \star  } {  \mathrm { a t } \ : t = t _ { 0 } , \Theta = \Theta _ { 0 } , \dot { \Theta } = \dot { \Theta } _ { 0 } \vphantom { | \star | } }
$$

(d) Write a computer program to process range observations of the pendulum mass using both a batch processor and a sequential filt er.   
(e) Generate a set of observations and process these observations using both the batch and sequential estimation algorithms. Use both perfect observations and observations with random noise.

(15) Write a computer program to process range and range-rate data for the spring-mass system of Section 4.8.2. Use the following data set (or create your own), which has Gaussian noise with mean zero and $\sigma _ { \rho } = 0 . 2 5 \mathrm { m }$ and $\sigma _ { \dot { \rho } } = 0 . 1 0 \mathrm { m / s }$ added. Use the same initial conditions given in Example 4.8.2. Use a weighting matrix, $W$ , that reflects the noise on the data,

$$
E [ \epsilon \epsilon ^ { T } ] = R = \left[ \begin{array} { c c } { \sigma _ { \rho } ^ { 2 } } & { 0 } \\ { 0 } & { \sigma _ { \dot { \rho } } ^ { 2 } } \end{array} \right] = \left[ \begin{array} { c c } { . 0 6 2 5 } & { 0 } \\ { 0 } & { . 0 1 } \end{array} \right] = W ^ { - 1 } .
$$

Observation Data   

<table><tr><td>Time</td><td>p(m)</td><td>p(m/s)</td></tr><tr><td>0.00</td><td>6.37687486186586</td><td>-0.00317546143535849</td></tr><tr><td>1.00</td><td>5.50318198665912</td><td>1.17587430814596</td></tr><tr><td>2.00</td><td>5.94513302809067</td><td>-1.47058865193489</td></tr><tr><td>3.00</td><td>6.30210798411686</td><td>0.489030779000695</td></tr><tr><td>4.00</td><td>5.19084347133671</td><td>0.993054430595876</td></tr><tr><td>5.00</td><td>6.31368240334678</td><td>-1.40470245576321</td></tr><tr><td>6.00</td><td>5.80399842220377</td><td>0.939807575607138</td></tr><tr><td>7.00</td><td>5.45115048359871</td><td>0.425908088320457</td></tr><tr><td>8.00</td><td>5.91089305965839</td><td>-1.47604467619908</td></tr><tr><td>9.00</td><td>5.6769731201352</td><td>1.42173765213734</td></tr><tr><td>10.00</td><td>5.25263404969825</td><td>-0.12082311844776</td></tr></table>

Answer after three iterations:

$$
\begin{array} { r l } & { x _ { 0 } = 2 . 9 5 7 1 m , \quad v _ { 0 } = - 0 . 1 2 6 0 m / s } \\ & { \rho _ { \mathrm { R M S } } = 0 . 2 4 7 m , \dot { \rho } _ { \mathrm { R M S } } = 0 . 0 8 7 5 m / s } \\ & { \sigma _ { x _ { 0 } } = 0 . 0 4 5 0 m , \sigma _ { v _ { 0 } } = 0 . 0 7 9 4 m / s , \rho _ { x _ { 0 } v _ { 0 } } = 0 . 0 4 2 6 } \end{array}
$$

(16) Repeat Exercise 15, except program the sequential processor algorithm. Use the same initial conditions. Solve for the state at each observation time. Map the state estimate and covariance matrix from the final time to the initial time and show that they agree with the batch results.

(17) Given: The equation of motion of a particle moving in a uniform gravity field influence d by a resistive drag force; for example,

$$
m { \ddot { \mathbf { r } } } = - m g \mathbf { j } - m \mathbf { D }
$$

where

$$
\mathbf { D } = { \frac { 1 } { 2 } } \rho \beta { \dot { r } } { \dot { \mathbf { r } } } ,
$$

and the sequence of observations

$$
\rho _ { i } = \sqrt { ( x - x _ { s } ) _ { i } ^ { 2 } + ( y - y _ { s } ) _ { i } ^ { 2 } } i = 1 , \ldots , m .
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0005_pages_0281-0350/auto/images/6c5144d08f24c3208f3a974288775c80304639643aea455b8cccee83040c7753.jpg)

Set up the necessary equations to estimate the initial position and velocity of the particle assuming that $\beta$ and $x _ { s }$ , $y _ { s }$ are unknown but constant forcemodel and measurement-model parameters to be estimated. Discuss the conditions necessary to ensure complete parameter observability.

(18) Given the following dynamic system

$$
\begin{array} { l } { \ddot { x } = - k x - \beta x ^ { 2 } + c \sin \omega t } \\ { \rho _ { i } = \sqrt { d ^ { 2 } + ( \ell + x _ { i } ) ^ { 2 } } + \epsilon _ { i } ; i = 1 , \dots , m . } \end{array}
$$

$$
E [ \epsilon _ { i } ] = 0 , ~ E [ \epsilon _ { i } \epsilon _ { j } ] = \sigma _ { i } ^ { 2 } \delta _ { i j }
$$

Set up all necessary equations for sequentially estimating the position and velocity of the system from observations $( \rho _ { i } )$ . Assume that $[ d , \ell , k , \beta , c ]$ are unknowns to be estimated. State clearly all information that must be given as input information beyond what is given in the problem statement.

(19) Given the observation-state relation

$$
y ( t ) = \sum _ { i = 1 } ^ { 3 } ( t ) ^ { i } x _ { i } ,
$$

and the observation sequence at $t = 1$ , $y \left( 1 \right) = 2$ , and at $t = 2 , \ y ( 2 ) = 1$ .

Find the “bes t” estimate of $\mathbf { x } _ { i }$ , $i = 1$ , 2, 3. (Hint: There are fewer observations than unknowns, so use the minimum norm solution.)

(20) Given the observation state relation ${ \bf y } = H \boldsymbol { x } + \epsilon$ , where $x$ is a scalar and given that

$$
\begin{array} { r l } & { \mathbf { y } = \left[ \mathbf { 1 } \right] , } \\ & { \mathbf { y } = \left[ \mathbf { 2 } \right] , \mathrm { ~ a n d ~ } E [ \epsilon ] = 0 , } \\ & { \mathbf { R } = E \left[ \epsilon \epsilon ^ { T } \right] = \left[ \begin{array} { l l l } { \frac { 1 } { 2 } } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] , H = \left[ \begin{array} { l } { 1 } \\ { 1 } \\ { 1 } \end{array} \right] } \end{array}
$$

with a priori information, ${ \overline { { x } } } = 2$ and $\begin{array} { r } { \sigma ^ { 2 } ( \overline { { x } } ) = \frac { 1 } { 2 } } \end{array}$ .

(a) Using $R ^ { - 1 }$ as the weighting matrix, find $\hat { x }$ using the batch processing algorithm.   
(b) What is the standard deviation of the estimation error associated with ${ \hat { x } } ?$   
(c) What is the best estimate of the observation error, ˆ-?

(21) Given the system

$$
\begin{array} { l } { { \displaystyle x ( t ) = x _ { 0 } + \dot { x } _ { 0 } t + \frac { 1 } { 2 } \ddot { x } _ { 0 } t ^ { 2 } ; t _ { 0 } = 0 \nonumber } } \\ { { \dot { x } ( t ) = \dot { x } _ { 0 } + \ddot { x } _ { 0 } t } } \\ { { \ddot { x } ( t ) = \ddot { x } _ { 0 } } } \end{array}
$$

with

$$
\mathbf { X } ( t ) = \left[ \begin{array} { l } { x } \\ { \dot { x } } \\ { \ddot { x } } \end{array} \right] , \overline { { P } } _ { 0 } = \left[ \begin{array} { l l l } { 4 } & { 0 } & { 0 } \\ { 0 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] , \overline { { \mathbf { X } } } ( t _ { 0 } ) = \left[ \begin{array} { l } { 1 } \\ { 1 } \\ { 1 } \end{array} \right] .
$$

At $t _ { 1 } = 1$ , an observation of $x ( t )$ is made; that is, $Y ( t _ { 1 } ) = x ( t _ { 1 } ) = 2$ . The variance of the error in $Y ( t _ { 1 } )$ is $\sigma ^ { 2 } ( \epsilon _ { Y } ) = 1$ .

(a) Compute $\hat { \mathbf X } ( t _ { 0 } )$ using the batch processing algorithm. Answer:

$$
\hat { \mathbf { X } } ( t _ { 0 } ) = \left[ \begin{array} { l } { 2 1 / 2 9 } \\ { 2 5 / 2 9 } \\ { 2 8 / 2 9 } \end{array} \right]
$$

(b) Using the sequential processing algorithm, determine $\hat { \mathbf X } ( t _ { 0 } )$ . Remember you are to solve for $\hat { \mathbf X } ( t _ { 0 } )$ , not $\hat { \mathbf X } ( t _ { 1 } )$ . You should get identical results to part a.

(c) Compute $\hat { \mathbf X } ( t _ { 1 } )$ using the sequential algorithm, then map $\hat { \mathbf X } ( t _ { 1 } )$ to $t _ { 0 }$ using the state transition matrix. You should get the same value of $\hat { \mathbf { X } } ( t _ { 0 } )$ as you computed in parts a and b.

Answer:

$$
\begin{array} { r } { \hat { \mathbf { X } } ( t _ { 1 } ) = \left[ \begin{array} { l } { 6 0 / 2 9 } \\ { 5 3 / 2 9 } \\ { 2 8 / 2 9 } \end{array} \right] } \end{array}
$$

(22) Assume a vehicle is moving along a rectilinear path with a constant acceleration. The generic equation of motion is

$$
x ( t ) = x _ { 0 } \ + v _ { 0 } t + \frac { 1 } { 2 } a t ^ { 2 } .
$$

At discrete constant intervals of time $t = t _ { i } , i = 0 , 1 , 2 , 3 \ldots 1 0$ the position and velocity of the vehicle are observed.

(a) Set up a flo w chart for the batch and sequential estimation algorithm to estimate a state vector consisting of the position, velocity, and acceleration. For the batch algorithm estimate the state at $t _ { 0 }$ , and for the sequential estimate the state at $t _ { i }$ .   
(b) Write a program (using Matlab or a similar software package) to solve for the state vector using the batch processor. Include an a priori covariance matrix and a measurement weighting matrix and the capability to map the state estimate and the estimation error covariance matrix from the epoch to any desired time. Generate a sequence of simulated observations to which random noise is added. Solve for the state vector and associated covariance matrix at $t _ { 0 }$ . Map these quantities to the final time for comparison with results from the sequential processor in part c.   
(c) Repeat part b for the sequential processor and estimate the state at $t _ { i }$ , $i = 1 \dots 1 0$ . Compare results at the final measurement time with the mapped results of the batch solution of part b.   
(d) Experiment with your program by changing the a priori covariance and weighting matrix. Write a brief report describing your results.

(23) For the problem posed in Section 4.7.1:

(a) Show that the exact value for $P _ { 2 }$ is given by Eq. (4.7.24).

(b) Under the assumption that $1 + \epsilon ^ { 2 } = 1$ , show that the conventional Kalman filt er yields

$$
P _ { 2 } = \frac { 1 } { 1 - 2 \epsilon } \left[ \begin{array} { r r } { - 1 } & { 1 } \\ { 1 } & { - 1 } \end{array} \right] .
$$

(c) Under the assumption that $1 + \epsilon ^ { 2 } = 1 $ , show that the batch processor yields

$$
P _ { 2 } = \frac { 1 } { 1 - 2 \epsilon } \left[ \begin{array} { c c } { { 1 } } & { { - ( 1 + \epsilon ) } } \\ { { - ( 1 + \epsilon ) } } & { { 2 } } \end{array} \right] = \left[ \begin{array} { c c } { { 1 + 2 \epsilon } } & { { - ( 1 + 3 \epsilon ) } } \\ { { - ( 1 + 3 \epsilon ) } } & { { 2 ( 1 + 2 \epsilon ) } } \end{array} \right] ,
$$

which agrees with the exact result to $O ( \epsilon )$ , thus illustrating the improved numerical behavior of the batch over the sequential processor.

(24) Two observations are taken of the parameter $x$ ,

$$
y _ { 1 } = x + \epsilon _ { 1 } , y _ { 2 } = x + \epsilon _ { 2 } ,
$$

where $\epsilon _ { 1 }$ and $\epsilon _ { 2 }$ are zero mean random noise. It is known that the variance of $\epsilon _ { 2 }$ is twice the variance of $\epsilon _ { 1 }$ . Determine the weighted least squares estimate of $x$ .

(25) Derive the following two equations for the estimation error covariance matrix:

(a) Beginning with Eq. (4.4.29), derive the expression for the estimation error covariance matrix given by Eq. (4.4.30). Assume that

$$
E \left[ ( \bar { \bf x } - { \bf x } ) \epsilon ^ { T } \right] = 0 .
$$

(b) Beginning with the equation for $\hat { \bf x }$ (Eq. 4.7.16), derive the Joseph formulation for the measurement update of the estimation error covariance matrix given by Eq. (4.7.19).

(c) Show that the Joseph formulation for the measurement update of $P$ is equivalent to the conventional Kalman update given by Eq. (4.7.18),

$$
P = ( I - K { \widetilde { H } } ) { \overline { { P } } } .
$$

(26) For the joint density function given by Eq. (4.5.4),

(a) Determine the MLE of $\sigma$ .

(b) Show that the MLE of $\alpha$ given by Eq. (4.5.8) is unbiased.

(27) Let $\mathbf { X } = [ x _ { 1 } x _ { 2 } \dots x _ { n } ] ^ { T }$ have a multivariate Gaussian distribution with each component of $\mathbf { X }$ having the same (unknown) mean $\alpha$ ,

$$
f \left( \mathbf { X } ; \alpha \right) = \frac { 1 } { ( 2 \pi ) ^ { n / 2 } | P | ^ { \frac { 1 } { 2 } } } \exp [ - \frac { 1 } { 2 } ( \mathbf { X } - A \alpha ) ^ { T } P ^ { - 1 } ( \mathbf { X } - A \alpha ) ]
$$

with

$$
A = { \left( \begin{array} { l } { 1 } \\ { 1 } \\ { \vdots } \\ { 1 } \end{array} \right) } ~ .
$$

(a) Identify the likelihood function and show that the expression for the maximum likelihood estimate of $\alpha$ is ${ \hat { \alpha } } = ( A ^ { T } P ^ { - 1 } { \bar { A ) } } ^ { - 1 } A ^ { T } P ^ { - 1 } \mathbf { X }$ . (b) Show that $\hat { \alpha }$ is an unbiased estimator of $\alpha$ .

(28) Given the estimator ${ \hat { \mathbf { x } } } = { \overline { { \mathbf { x } } } } + K \left( \mathbf { y } - H { \overline { { \mathbf { x } } } } \right)$ , state all necessary conditions on $\overline { { \mathbf { x } } }$ and $\mathbf { y }$ for $\hat { \bf x }$ to be an unbiased estimate of $\mathbf { x }$ .

(29) Given: Random variables $X$ and $Y$ and

$$
Y = a \pm b X
$$

where $a$ and $b$ are constants. Show that the correlation coeffic ient $\rho \left( X , Y \right)$ has the value

$$
\rho \left( X , Y \right) = \pm 1 .
$$

(30) Given that $\mathbf { x }$ is an $n \times 1$ vector of random variables with mean $\overline { { \mathbf { x } } }$ and covariance $P$ . Let $\mathbf { y }$ be an $m \times 1$ vector of random variables related to $\mathbf { x }$ by

$$
\mathbf { y } = H \mathbf { x } + \epsilon
$$

where $\epsilon$ is zero mean with covariance $R$ and is independent of $\mathbf { x }$ .

(a) Find the mean of y.

(b) Show that the variance-covariance of y is given by

$$
\begin{array} { c } { { P _ { y } = E \left[ ( { \bf y } - \overline { { { \bf y } } } ) ( { \bf y } - \overline { { { \bf y } } } ) ^ { T } \right] } } \\ { { { \bf \phi } = H P H ^ { T } + R . } } \end{array}
$$

(c) Show that the covariance of $\mathbf { x }$ and $\mathbf { y }$ is

$$
P _ { \bf x y } \equiv E [ ( { \bf x } - \overline { { \bf x } } ) ( { \bf y } - \overline { { \bf y } } ) ^ { T } ] = P H ^ { T } .
$$

(31) An estimate, $\hat { \bf x }$ is made of $\mathbf { x }$ (an $n \times 1$ vector), based on $m$ observations $\mathbf { y }$ $\mathbf { \chi } _ { m } > n \mathbf { \chi } ,$ ), where

$$
\mathbf { y } = H \mathbf { x } + \epsilon
$$

and

$$
\epsilon \mathrm { i s } N ( \overline { { \epsilon } } , R ) .
$$

An a priori value of $\mathbf { x }$ is given:

$$
{ \overline { { \mathbf { x } } } } = \mathbf { x } + \mathbf { e }
$$

where $\mathbf { e }$ is $N \left( 0 , { \overline { { P } } } \right)$ . Assume $E \left[ \mathbf { e } \epsilon ^ { T } \right] = 0$ .

The estimate is

$$
\hat { \mathbf { x } } = \overline { { \mathbf { x } } } + K ( \mathbf { y } - H \overline { { \mathbf { x } } } ) .
$$

(a) What is the bias for this estimator?

(b) What is the variance-covariance associated with the estimation error for $\hat { \mathbf { x } } ?$ Note that $\hat { \bf x }$ is biased so use the definition of $P$ given in the answer.

(c) Show that by redefining the noise vector to be $\epsilon = \overline { { \epsilon } } + \epsilon ^ { \prime }$ , and by including $\overline { { \epsilon } }$ in the state vector, an unbiased estimator may be formed. Assume that an a priori estimate of $\overline { { \epsilon } }$ with covariance $P _ { \overline { { \epsilon } } }$ is available.

# Answer:

(a) $E [ \hat { \mathbf { x } } ] = \mathbf { x } + K \overline { { \epsilon } } , \mathrm { b i a s } = K \bar { \epsilon }$ (b) $P = ( I - K H ) \overline { { P } } ( I - K H ) ^ { T } + K R K ^ { T }$ where

$$
R = E \left[ ( \epsilon - \overline { { \epsilon } } ) ( \epsilon - \overline { { \epsilon } } ) ^ { T } \right]
$$

and

$$
\begin{array} { l } { P \equiv E \left[ ( \tilde { \mathbf { e } } - E ( \tilde { \mathbf { e } } ) ) ( \tilde { \mathbf { e } } - E ( \tilde { \mathbf { e } } ) ) ^ { T } \right] } \\ { \tilde { \mathbf { e } } \equiv \hat { \mathbf { x } } - \mathbf { x } , E ( \tilde { \mathbf { e } } ) = K \overline { { \epsilon } } } \end{array}
$$

(32) Assuming we are given no $a$ priori information on $\hat { \bf x }$ ,

(a) show that there is no correlation between the residual observation error, $\hat { \mathbf { y } } - \mathbf { y } = \hat { \pmb { \epsilon } }$ , and the estimation error, $\hat { \mathbf { x } } - \mathbf { x }$ , that

$$
E \left[ \widehat { \epsilon } ( \widehat { \mathbf { x } } - \mathbf { x } ) ^ { T } \right] = 0 .
$$

If this were not zero, it would mean that we had not extracted all of the available information from the observations.

Hint: Use

$$
\begin{array} { r l } & { \hat { \mathbf { \epsilon } } = \mathbf { y } - H \hat { \mathbf { x } } } \\ & { \hat { \mathbf { x } } = ( H ^ { T } R ^ { - 1 } H ) ^ { - 1 } H ^ { T } R ^ { - 1 } \mathbf { y } } \\ & { \mathbf { y } = H \mathbf { x } + \mathbf { \epsilon } , \quad E [ \mathbf { \epsilon } ] = 0 , \quad E [ \mathbf { \epsilon } \mathbf { \epsilon } ^ { T } ] = R . } \end{array}
$$

(b) Assuming that a priori information is given; that is, $\bar { \mathbf { x } } = \mathbf { x } + \pmb { \eta }$ where $E [ \pmb { \eta } ] = 0 , E [ \pmb { \eta } \pmb { \eta } ^ { T } ] = \overline { { P } }$ and $E [ \epsilon \eta ^ { T } ] = 0$ . Show that $E [ \hat { \epsilon } ( \hat { \mathbf { x } } - \mathbf { x } ) ^ { T } ] =$ 0 is still true.

(33) Occasionally a priori information, $\overline { { \mathbf { x } } }$ and $\overline { { P } }$ , used to initiate a batch filter is obtained from processing an earlier batch of data so that the errors in $\overline { { \mathbf { x } } }$ and the observation error, $\epsilon$ , are correlated. Derive the expression for the covariance matrix of the estimation error, $P$ , assuming

$$
\begin{array} { r l } & { P = E \left[ ( \hat { \mathbf { x } } - \mathbf { x } ) ( \hat { \mathbf { x } } - \mathbf { x } ) ^ { T } \right] } \\ & { \hat { \mathbf { x } } = ( \overline { { P } } ^ { - 1 } + H ^ { T } R ^ { - 1 } H ) ^ { - 1 } ( \overline { { P } } ^ { - 1 } \overline { { \mathbf { x } } } + H ^ { T } R ^ { - 1 } \mathbf { y } ) , } \end{array}
$$

$$
\begin{array} { r l } & { \overline { { \mathbf { x } } } = \mathbf { x } + \epsilon _ { \overline { { \mathbf { x } } } } , ~ E ( \epsilon _ { \overline { { \mathbf { x } } } } ) = 0 , ~ E ( \epsilon _ { \overline { { \mathbf { x } } } } \epsilon _ { \overline { { \mathbf { x } } } } ^ { T } ) = \overline { { P } } , } \\ & { \mathbf { y } = H \mathbf { x } + \epsilon , E \left[ \epsilon \right] = 0 , ~ E \left[ \epsilon \epsilon ^ { T } \right] = R , } \\ & { ~ E \left[ \epsilon \epsilon _ { \overline { { \mathbf { x } } } } ^ { T } \right] = M . } \end{array}
$$

Answer:

$$
\begin{array} { r l } & { P = ( \overline { { P } } ^ { - 1 } + H ^ { T } R ^ { - 1 } H ) ^ { - 1 } + ( \overline { { P } } ^ { - 1 } + H ^ { T } R ^ { - 1 } H ) ^ { - 1 } } \\ & { \quad \times [ H ^ { T } R ^ { - 1 } M \overline { { P } } ^ { - 1 } + \overline { { P } } ^ { - 1 } M ^ { T } R ^ { - 1 } H ] ( \overline { { P } } ^ { - 1 } + H ^ { T } R ^ { - 1 } H ) ^ { - 1 } . } \end{array}
$$

(34) Given that

$$
\begin{array} { c } { \hat { \mathbf { x } } _ { k } = \mathbf { x } _ { k } + \pmb { \eta } _ { k } } \\ { \hat { \mathbf { x } } _ { k + 1 } = \mathbf { x } _ { k + 1 } + \pmb { \eta } _ { k + 1 } } \end{array}
$$

and

$$
\mathbf { x } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) \mathbf { x } _ { k } + \Gamma ( t _ { k + 1 } , t _ { k } ) \mathbf { u } _ { k } ,
$$

where

$$
E [ \pmb { \eta } _ { k } ] = E [ \pmb { \eta } _ { k + 1 } ] = 0
$$

and $\mathbf { x } _ { k }$ and $\mathbf { x } _ { k + 1 }$ are the true values, show that

$$
P \eta _ { k } \eta _ { k + 1 } = E [ \eta _ { k } \eta _ { k + 1 } ^ { T } ] = P _ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) ( I - K _ { k + 1 } H _ { k + 1 } ) ^ { T } .
$$

(35) Consider the linear system define d in Exercise 21. Assume $t _ { 0 } = 0$ ; otherwise replace $t$ with $( t - t _ { 0 } )$ .

$$
\Phi ( t , t _ { 0 } ) = { \frac { \partial X ( t ) } { \partial X ( t _ { 0 } ) } } = { \left[ 0 t \ \frac { t ^ { 2 } } { 2 } \right] } 
$$

and

$$
\overline { { P } } _ { 0 } = \left[ \begin{array} { c c c } { 4 0 0 } \\ { 0 2 0 } \\ { 0 0 1 } \end{array} \right] .
$$

(a) Show that the time update for $P$ at the first measurement time, $t _ { 1 }$ , obtained by integrating the differential equation for $\dot { \overline { { P } } }$ (Eq. 4.9.36) with initial conditions $\overline { { P } } _ { 0 }$ is given by

$$
\overline { { { \cal P } } } ( t _ { 1 } ) = \left[ \begin{array} { l l l l l l l } { { } } & { { 4 + 2 t _ { 1 } + \frac { t _ { 1 } ^ { 4 } } { 4 } } } & { { } } & { { } } & { { 2 t _ { 1 } + \frac { t _ { 1 } ^ { 3 } } { 3 } } } & { { } } & { { \frac { t _ { 1 } ^ { 2 } } { 2 } \nonumber } } & { { } } \\ { { } } & { { 2 t _ { 1 } + \frac { t _ { 1 } ^ { 3 } } { 3 } } } & { { } } & { { } } & { { 2 + t _ { 1 } ^ { 2 } } } & { { } } & { { t _ { 1 } \nonumber } } & { { } } \\ { { } } & { { \frac { t _ { 1 } ^ { 2 } } { 2 } } } & { { } } & { { } } & { { t _ { 1 } } } & { { } } & { { 1 } } & { { } } \end{array} \right] .
$$

(b) Show that this agrees with the conventional time update given by

$$
\overline { { \boldsymbol { P } } } ( t _ { 1 } ) = \Phi ( t _ { 1 } , t _ { 0 } ) \overline { { \boldsymbol { P } } } _ { 0 } \Phi ^ { T } ( t _ { 1 } , t _ { 0 } ) .
$$

(36) Given the information matrix

$$
\Lambda = \left[ \begin{array} { r r r } { { 1 3 } } & { { 2 } } & { { 6 } } \\ { { 2 } } & { { 2 } } & { { 6 } } \\ { { 6 } } & { { 6 } } & { { 1 8 } } \end{array} \right] .
$$

Are all three elements of the state vector observable? Why or why not?

(37) In Example 4.2.1 the state vector includes $X , Y , X _ { s }$ , and $Y _ { s }$ . Are all of these quantities observable? Why or why not?

(38) Given a 2D state vector, $\mathbf { X }$ , with

$$
\begin{array} { r } { E [ \mathbf { X } ] = 0 , \quad E [ \mathbf { X } \mathbf { X } ^ { T } ] = P = \left[ \begin{array} { l l } { 4 } & { 1 } \\ { 1 } & { 2 } \end{array} \right] . } \end{array}
$$

Sketch the $2 \sigma$ probability ellipse.

(39) For the transformation of coordinates

$$
\left[ { x ^ { \prime } } \right] = \left[ \begin{array} { r r } { \cos \theta } & { \sin \theta } \\ { - \sin \theta } & { \cos \theta } \end{array} \right] \left[ \begin{array} { r } { x + 2 } \\ { y + 2 } \end{array} \right] ,
$$

determine $\overline { { x } } ^ { \prime } , \overline { { y } } ^ { \prime }$ , and $P ^ { \prime }$ where $\bar { x } ^ { \prime } = E ( x ^ { \prime } ) , \bar { y } ^ { \prime } = E ( y ^ { \prime } )$ and

$$
P ^ { \prime } = \left[ \begin{array} { l l l } { \begin{array} { l } { \sigma ^ { 2 } ( x ^ { \prime } ) } \end{array} } & { \begin{array} { l } { \mu _ { 1 1 } ( x ^ { \prime } y ^ { \prime } ) } \end{array} } \\ { \begin{array} { l } { \mu _ { 1 1 } ( x ^ { \prime } y ^ { \prime } ) } \end{array} } & { \begin{array} { l } { \sigma ^ { 2 } ( y ^ { \prime } ) } \end{array} } \end{array} \right] .
$$

(40) The differential equation for the Ornstein-Uhlenbeck process, a first-order Gauss-Markov process, is

$$
\dot { \eta } ( t ) + \beta \eta ( t ) = u ( t )
$$

with initial conditions $\eta = \eta \left( t _ { 0 } \right)$ , at $t = t _ { 0 }$ where $u \left( t \right)$ is a Gaussian white noise process with mean zero. Show that the solution is given by

$$
\eta \left( t \right) = \eta \left( t _ { 0 } \right) e ^ { - \beta \left( t - t _ { 0 } \right) } + \int _ { t _ { 0 } } ^ { t } e ^ { - \beta \left( t - \tau \right) } u \left( \tau \right) d \tau .
$$

(41) Generate 1000 equally spaced observations of one cycle of a sine wave with amplitude 1 and period 10. Add Gaussian random noise with zero mean and variance $= 0 . 2 5$ . Set up a sequential estimation procedure to estimate the amplitude of the sine wave as a function of time using the noisy raw data. Model the sine wave as a Gauss-Markov process as given by Eq. (4.9.60),

$$
\eta _ { i + 1 } = m _ { i + 1 } \eta _ { i } + \Gamma _ { i + 1 } u _ { i }
$$

where

$$
u _ { i } = N ( 0 , 1 )
$$

$$
\begin{array} { l } { { m _ { i + 1 } = e ^ { - \beta ( t _ { i + 1 } - t _ { i } ) } } } \\ { { \ ~ } } \\ { { \Gamma _ { i + 1 } = \sqrt { \displaystyle \frac { \sigma ^ { 2 } } { 2 \beta } ( 1 - m _ { i + 1 } ^ { 2 } ) } } } \\ { { \ ~ \beta = \displaystyle \frac { 1 } { \tau } } } \end{array}
$$

and $\tau$ is the time constant. The sequential algorithm is given by

$$
\begin{array} { r l } & { \bar { \eta } _ { i } = \Phi ( t _ { i } , t _ { i - 1 } ) \hat { \eta } _ { i - 1 } \quad ( i = 1 , 2 \dots 1 0 0 0 ) } \\ & { \Phi ( t _ { i } , t _ { i - 1 } ) = m _ { i } = e ^ { - \beta ( t _ { i } - t _ { i - 1 } ) } } \\ & { \overline { { P } } _ { i } = \Phi ( t _ { i } , t _ { i - 1 } ) P _ { i - 1 } \Phi ^ { T } ( t _ { i } , t _ { i - 1 } ) + \Gamma _ { i } Q _ { i - 1 } \Gamma _ { i } ^ { T } } \end{array}
$$

Note that $P , \Phi , Q$ , and $\Gamma$ are scalars

$$
\begin{array} { r l } & { K _ { i } = \overline { { P } } _ { i } \widetilde { H } _ { i } ^ { T } ( \widetilde { H } _ { i } \overline { { P } } _ { i } \widetilde { H } _ { i } ^ { T } + R _ { i } ) ^ { - 1 } = \frac { \overline { { P } } _ { i } } { \overline { { P } } _ { i } + 1 } } \\ & { \widehat { \eta } _ { i } = \overline { { \eta } } _ { i } + K _ { i } ( Y _ { i } - \widetilde { H } _ { i } \overline { { \eta } } _ { i } ) = \overline { { \eta } } _ { i } + K _ { i } ( Y _ { i } - \overline { { \eta } } _ { i } ) , ( Y _ { i } \mathrm { i s t } } \\ & { \mathrm { d a t a } ) } \\ & { P _ { i } = ( I - K _ { i } \widetilde { H } _ { i } ) \overline { { P } } _ { i } = K _ { i } } \\ & { \mathrm { x t ~ } i } \end{array}
$$

he observation

Ne

Plot your observations, the truth data, and $\hat { \eta }$ versus time. You will need to guess initial values for $\sigma$ and $\beta$ . Try several values to see which gives you the best results (i.e., the smallest RMS of estimation errors).

$$
\mathrm { R M S } = \left\{ \sum _ { i = 1 } ^ { N } \frac { ( T _ { i } - \hat { \eta } _ { i } ) ^ { 2 } } { N } \right\} ^ { 1 / 2 } ,
$$

where $T _ { i }$ is the true amplitude of the sine wave and $N = 1 0 0 0$ . Fig. 4.19.1 illustrates the truth, the raw data, and one example of the filtered results (not necessarily the optimal) for the indicated values of $\sigma$ and $\beta$ . The truth is the smooth curve. You may also plot a histogram of the post-fit residuals to see if they conform to a Gaussian distribution.

(42) Using the optimum values of $\sigma$ and $\tau$ determined in Exercise 41, solve for the smoothed history of $\hat { \eta } ( t )$ using the algorithm of Section 4.15.1. Plot the true values of $\eta$ , the fil ter values determined in Exercise 41, and the smoothed values. Compute the RMS of the smoothed fit. You should find the RMS from the smoothed solution somewhat smaller than the fil ter result. Fig. 4.19.2 is an example of the truth, the filter , and the smoothed results for the case illustrated in Fig. 4.19.1. Is the histogram of residuals

# Process Noise / Sine Wave Recovery

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0005_pages_0281-0350/auto/images/32d910aeebc3eff5c581e213ce4af266f7449ffa16bc9c849f8a6a4b36ffa97b.jpg)  
Figure 4.19.1: Process noise/sine wave recovery showing truth, raw data (truth plus noise) and the filtered solution. $\bar { \eta } _ { 0 } = 0$ , $\sigma = 2 . 4 9$ , $\beta = . 0 4 5$ .

for the smoothed solution more nearly Gaussian than those from the filter in Exercise 41?

(43) Given a system described by

$$
\mathbf { X } ( t _ { i + 1 } ) = { \left[ \begin{array} { l } { x _ { 1 } ( t _ { i + 1 } ) } \\ { x _ { 2 } ( t _ { i + 1 } ) } \end{array} \right] } = { \left[ \begin{array} { l } { 1 1 } \\ { 0 1 } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } \left( t _ { i } \right) } \\ { x _ { 2 } \left( t _ { i } \right) } \end{array} \right] } + { \left[ \begin{array} { l } { 1 1 } \\ { 1 0 } \end{array} \right] } { \left[ \begin{array} { l } { u _ { 1 } ( t _ { i } ) } \\ { u _ { 2 } ( t _ { i } ) } \end{array} \right] }
$$

$$
{ \left[ \begin{array} { l } { y _ { 1 } ( t _ { i } ) } \\ { y _ { 2 } ( t _ { i } ) } \end{array} \right] } = { \left[ \begin{array} { l } { 0 1 / 2 } \\ { 1 1 / 2 } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } \left( t _ { i } \right) } \\ { x _ { 2 } \left( t _ { i } \right) } \end{array} \right] } + { \left[ \epsilon _ { 1 } \right] }
$$

$$
\begin{array} { r } { \overline { { \mathbf { X } } } ( t _ { 0 } ) = [ \overline { { x } } _ { 1 } ( t _ { 0 } ) ] = [ 2 ] , \overline { { P } } ( t _ { 0 } ) = [ 0 ] } \\ { \overline { { x } } _ { 2 } ( t _ { 0 } ) \mathbf { . } ] } \end{array}
$$

$$
R = E \left\{ \left[ { \epsilon } _ { 1 } \right] \left[ \epsilon _ { 1 } \epsilon _ { 2 } \right] \right\} = \left[ 0 \atop 0 2 \right] ,
$$

$$
E [ u _ { 1 } ( t _ { i } ) ] = E [ u _ { 2 } ( t _ { i } ) ] = 0
$$

# Process Noise / Sine Wave Recovery

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0005_pages_0281-0350/auto/images/fff4443c03d7d1a2cbaacfd605f8a0a49743e46c66ef35a64a650cb11b90c022.jpg)  
Figure 4.19.2: Process noise/sine wave recovery showing the truth, the filtered, and the smoothed solution. $\bar { \eta } _ { 0 } = 0$ , $\sigma = 2 . 4 9$ , $\beta = . 0 4 5$ .

$$
E \left\{ \left[ u _ { 1 } ( t _ { i } ) \right] \left[ u _ { 1 } ( t _ { j } ) u _ { 2 } ( t _ { j } ) \right] \right\} = I \delta _ { i j } .
$$

Observations at $t _ { 1 }$ are given by

$$
\begin{array} { r } { \left[ y _ { 1 } ( t _ { 1 } ) \right] = \left[ \begin{array} { l } { 3 } \\ { 2 } \end{array} \right] . } \end{array}
$$

(a) Using the sequential estimation algorithm, determine the optimal estimate of $\mathbf { X } ( t _ { 1 } )$ and $P ( t _ { 1 } )$ .   
(b) What is the smoothed estimate of ${ \bf X } ( t _ { 0 } ) \} \mathrm { ~ }$ ？   
(c) What is the optimal estimate of $\mathbf X ( t _ { 1 } )$ if no process noise were present?

(44) Use the information fil ter to determine the optimal estimate of $\mathbf X ( t _ { 1 } )$ and $P ( t _ { 1 } )$ for Exercise $4 3 \mathrm { a }$ .

# Square Root Solution Methods for the Orbit Determination Problem

# 5.1 INTRODUCTION

In the previous chapter, the solution to the least squares estimation problem including $a$ priori information, $\overline { { P } }$ and $\overline { { \mathbf { x } } }$ , is represented in the normal equation form as

$$
( H ^ { T } W H + \overline { { P } } ^ { - 1 } ) \hat { \mathbf { x } } = H ^ { T } W y + \overline { { P } } ^ { - 1 } \overline { { \mathbf { x } } }
$$

which can be expressed as

$$
M \hat { \mathbf { x } } = N .
$$

The solution for $\hat { \bf x }$ is obtained by computing the inverse of $M$ . In practice, computational problems are encountered in forming and inverting the matrix $M =$ $H ^ { T } W H + \overline { { P } } ^ { - 1 }$ . An orthogonal transformation approach can be used to write Eq. (5.1.2) in the form

$$
R \hat { \mathbf x } = b
$$

where $R$ is an $n \times n$ upper triangular matrix ( $R$ is not the observation error covariance matrix). Then $\hat { \bf x }$ can be obtained by backward substitution. This approach has the advantage that increased numerical accuracy is achieved over conventional matrix inversion methods for solving Eq. (5.1.2). Using the orthogonal transformation approach, accuracy can be achieved with a single-precision computation that is equal to the accuracy obtained by inverting $M$ with the normal equation approach using double-precision computations.

The normal equation approach has several operational and conceptual advantages that have led to the widespread adoption of this technique for many operational orbit determination systems. Both the normal equation and orthogonal transformation approaches are described in the subsequent sections.

The solution of the linear system

$$
M \hat { \mathbf { x } } = \mathbf { N }
$$

is expressed as

$$
\hat { \mathbf { x } } = M ^ { - 1 } \mathbf { N }
$$

where the operation $M ^ { - 1 }$ implies that the inverse of the $( n \times n )$ matrix $M$ is computed and then postmultiplied by the column vector $\mathbf { N }$ . A solution based on the Cholesky decomposition of $M$ is more efficient and, in most cases, more accurate. The Cholesky decomposition is applicable only if $M$ is symmetric and positive definite, a condition satisfied for the case considered here. The following discussion first outlines the Cholesky decomposition, and describes this approach to solving the normal equations. Then a discussion of solutions based on orthogonal transformations is presented in subsequent sections.

# 5.2 CHOLESKY DECOMPOSITION

Let $M$ be a symmetric positive definite matrix, and let $R$ be an upper triangular matrix computed such that

$$
R ^ { T } R = M .
$$

(Note that $R$ is not the observation error covariance matrix.) Then Eq. (5.1.4) can be expressed as

$$
R ^ { T } R \hat { \mathbf { x } } = \mathbf { N } .
$$

If the definit ion

$$
{ \bf z } = R \hat { \bf x }
$$

is used, Eq. (5.2.2) can be written as

$$
R ^ { T } { \bf z } = { \bf N }
$$

where $R ^ { T }$ is lower triangular. The components of $\mathbf { z }$ can be determined using a forward recursion relation. Then, Eq. (5.2.3) can be solved using a backward recursion to obtain the elements of $\hat { \bf x }$ .

The elements of the error covariance matrix, $P = ( H ^ { T } W H + \overline { { { P } } } ^ { - 1 } ) ^ { - 1 } =$ $M ^ { - 1 }$ , can be obtained from the condition

$$
P = M ^ { - 1 } = ( R ^ { T } R ) ^ { - 1 } = R ^ { - 1 } R ^ { - T } = S S ^ { T }
$$

where $S$ , the inverse of the upper triangular matrix, $R$ , can be computed by an efficient backward recursion.

Equation (5.2.1) represents a set of $( n ^ { 2 } + n ) / 2$ equations for the $( n ^ { 2 } + n ) / 2$ unknown elements of the upper triangular matrix, $R$ . The expression for the Cholesky decomposition of $M$ is obtained by expanding Eq. (5.2.1) and solving term by term for the elements of $R$ (e.g., $R _ { i j }$ is determined in terms of the elements of $M$ ).

Given the elements of the $n \times n$ positive definit e matrix $M$ and the $n \times 1$ column vector $\mathbf { N }$ , the following Cholesky algorithm will yield a solution for the elements of $R , \mathbf { z } , { \hat { \mathbf { x } } }$ and the upper triangular matrix, $S$ . Step 1 of the following algorithm determines the elements of $R$ and the vector $\mathbf { z }$ . Steps 2 and 3 perform a backward recursion to form $\hat { \bf x }$ and the elements of the matrix $S = R ^ { - 1 }$ .

# 5.2.1 THE CHOLESKY ALGORITHM

The Cholesky algorithm for $R$ is derived easily by equating the elements of $R ^ { T } R$ to the elements of $M$ that are known. For example, from expanding $R ^ { T } R$ it is shown that $r _ { 1 1 } = \sqrt { M _ { 1 1 } }$ .

1) For $i = 1 , 2 , \dots , n$

$$
\begin{array} { l } { { \displaystyle r _ { i i } = \left( M _ { i i } - \sum _ { k = 1 } ^ { i - 1 } r _ { k i } ^ { 2 } \right) ^ { 1 / 2 } } } \\ { { \displaystyle r _ { i j } = \left( M _ { i j } - \sum _ { k = 1 } ^ { i - 1 } r _ { k i } r _ { k j } \right) / r _ { i i } ; \quad j = i + 1 , \dots , n . } } \end{array}
$$

The elements of $\mathbf { z }$ are obtained from an expansion of Eq. (5.2.4):

$$
z _ { i } = \left( N _ { i } - \sum _ { j = 1 } ^ { i - 1 } r _ { j i } z _ { j } \right) / r _ { i i }
$$

2) For $i = n , n - 1 , \ldots , 1$

$$
{ \hat { x } } _ { i } = \left( z _ { i } - \sum _ { j = i + 1 } ^ { n } r _ { i j } { \hat { x } } _ { j } \right) / r _ { i i } .
$$

The elements of $S$ are obtained from an expansion of $S R = I$ .

3) For $i = 1 , 2 \dots , n$

$$
\begin{array} { l } { { s _ { i i } = \displaystyle \frac { 1 } { r _ { i i } } } } \\ { { s _ { i j } = - s _ { j j } \left[ \displaystyle \sum _ { k = i } ^ { j - 1 } r _ { k j } s _ { i k } \right] ; \quad j = i + 1 , \ldots , n . } } \end{array}
$$

Examples of the application of this algorithm are given in Sections 5.6.1 and 5.6.5.

This Cholesky algorithm is a nonblock algorithm. That is, it does not use matrix multiplication. Because matrix multiplication is much faster in terms of floating point operations per second than matrix-vector operations on modern computers, a block Cholesky algorithm often will be faster than a nonblock version. In fact, the increase in speed may be a factor of three or more. See Golub and Van Loan (1996) for examples of a block Cholesky algorithm.

# 5.2.2 THE SQUARE ROOT FREE CHOLESKY ALGORITHM

Notice that calculation of the diagonal elements of $R$ requires that $n$ square roots be taken. Computationally the square root operation is expensive compared to multiplication, division, addition, or subtraction; hence, it is desirable to avoid square roots if possible. A square root free Cholesky algorithm may be developed by defining

$$
M = U D U ^ { T }
$$

where $U$ is unit upper triangular (i.e., has ones on the diagonal), and $D$ is a diagonal matrix. As in the previous section, Eq. (5.2.10) represents the $( n ^ { 2 } + n ) / 2$ equation in the $( n ^ { 2 } + n ) / 2$ unknown elements of $U$ and $D$ . The algorithm for the elements of $U$ and $D$ is obtained by expanding Eq. (5.2.10) and is given by

$$
D _ { j } U _ { i j } = M _ { i j } - \sum _ { k = j + 1 } ^ { n } M _ { j k } ^ { \prime } U _ { i k } \equiv M _ { i j } ^ { \prime } j = n , \dots , 1
$$

$$
D _ { j } = M _ { j j } - \sum _ { k = j + 1 } ^ { n } M _ { j k } ^ { \prime } U _ { j k } .
$$

The procedure is to set $j = n$ and cycle through the algorithm for $i = 1 \dots n - 1$ , solving for $D _ { n }$ and the elements of $U _ { i n }$ (i.e., the last column of $U$ ). Then set $j = n - 1$ and cycle through for $i = 1 \dots n - 2$ , solving for $D _ { n - 1 }$ and the $n - 1$ column of $U$ . Repeat this procedure for the remaining values of $j$ .

Knowing $U$ and $D$ , it is possible to solve for $\hat { \bf x }$ from Eq. (5.1.2) and Eq. (5.2.10) as follows. Note that

$$
U D U ^ { T } \hat { \mathbf { x } } = \mathbf { N }
$$

and let

$$
{ \bf z } = D U ^ { T } \hat { \bf x } .
$$

Then

$$
U \mathbf { z } = \mathbf { N } .
$$

The intermediate vector $\mathbf { z }$ can be determined from Eq. (5.2.15). The solution is a backward substitution (i.e., we solve for $z _ { n }$ , $z _ { n - 1 } \ldots z _ { 1 } ,$ ):

$$
\begin{array} { l } { { z _ { n } = N _ { n } } } \\ { { z _ { i } = N _ { i } - \displaystyle \sum _ { j = i + 1 } ^ { n } U _ { i j } z _ { j } ~ i = n - 1 , \ldots , 1 . } } \end{array}
$$

Then the elements of $\hat { \bf x }$ can be determined from Eq. (5.2.14) by using a forward substitution, as

$$
\hat { x } _ { i } = \frac { z _ { i } } { D _ { i i } } - \sum _ { j = 1 } ^ { i - 1 } U _ { j i } \hat { x } _ { j } i = 1 , 2 , \ldots n .
$$

The associated estimation error covariance is obtained from

$$
\begin{array} { c } { P = ( U D U ^ { T } ) ^ { - 1 } } \\ { = U ^ { - T } D ^ { - 1 } U ^ { - 1 } } \end{array}
$$

where

$$
\begin{array} { l l } { { \displaystyle { D _ { i i } ^ { - 1 } = 1 / D _ { i i } } \qquad i = 1 , \dots n } } \\ { { \qquad \quad j = i + 1 , \dots \cdot n } } \\ { { \displaystyle { U _ { i j } ^ { - 1 } = - \sum _ { k = i } ^ { j - 1 } U _ { i k } ^ { - 1 } U _ { k j } } } } \\ { { \qquad \quad U _ { i j } ^ { - 1 } = 0 \qquad i > j } } \\ { { \displaystyle { D _ { i j } ^ { - 1 } = 0 \qquad i \neq j . } } } \end{array}
$$

Note that none of the algorithms required to compute $\hat { \bf x }$ involve the calculation of a square root.

# 5.3 LEAST SQUARES SOLUTION VIA ORTHOGONAL TRANSFORMATION

An alternate approach that avoids some of the numerical problems encountered in the normal equation approach is described in the following discussion. The method obtains the solution by applying successive orthogonal transformations to the information array, $( H , \mathbf { y } )$ . Enhanced numerical accuracy is obtained by this approach. Consider the quadratic performance index, $J ( \mathbf { x } )$ , which minimizes the weighted sum of squares of the observation errors, $\boldsymbol { \epsilon } = \mathbf { y } - H \mathbf { x }$ (for the moment we will assume no a priori information; i.e., $\overline { { P } } ^ { - 1 } = 0$ , $\mathbf { \overline { { x } } = 0 }$ ):

$$
J ( { \bf x } ) = \epsilon ^ { T } W \epsilon = \left\| { W ^ { \frac { 1 } { 2 } } ( H { \bf x } - { \bf y } ) } \right\| ^ { 2 } = ( H { \bf x } - { \bf y } ) ^ { T } W ( H { \bf x } - { \bf y } ) .
$$

If $W$ is not diagonal, $W ^ { 1 / 2 }$ can be computed by the Cholesky decomposition. Or the prewhitening transformation described at the end of Section 5.7.1 can be applied so that $W = I$ . For notational convenience we are using $- \epsilon$ in Eq. (5.3.1).

The solution to the least squares estimation problem (as well as the minimum variance and the maximum likelihood estimation problem, under certain restrictions) is obtained by finding the value $\hat { \bf x }$ that minimizes the performance index $J ( \mathbf { x } )$ . To achieve the minimum value of $J ( \mathbf { x } )$ , we introduce the $m \times m$ orthogonal matrix, $Q$ . An orthogonal matrix has the following properties:

1. $Q Q ^ { T } = I$

2. $Q ^ { - 1 } = Q ^ { T }$ hence $Q ^ { T } Q = I$ .

3. If $Q _ { 1 }$ and $Q _ { 2 }$ are orthogonal matrices, then so is $Q _ { 1 } Q _ { 2 }$ .

4. For any vector $\mathbf { x }$

$$
\left\| Q \mathbf { x } \right\| = \left\| \mathbf { x } \right\| = ( \mathbf { x } ^ { T } \mathbf { x } ) ^ { \frac { 1 } { 2 } } .
$$

Multiplying by $Q$ does not change the Euclidean norm of a vector.

5. If $\epsilon$ is an $m$ vector of random variables with $\epsilon \sim ( O , I )$ (i.e., $E ( \epsilon ) = 0$ and $E ( \epsilon \epsilon ^ { T } ) = I )$ ), then $\overline { { \epsilon } } = Q \epsilon$ has the same properties,

$$
E ( \overline { { \epsilon } } ) = Q E ( \epsilon ) = 0 , E ( \overline { { \epsilon } } \overline { { \epsilon } } ^ { T } ) = Q E ( \epsilon \epsilon ^ { T } ) Q ^ { T } = I .
$$

It follows then that (5.3.1) can be expressed as

$$
\begin{array} { l } { { \displaystyle J ( { \bf x } ) = \left\| Q W ^ { \frac { 1 } { 2 } } ( H { \bf x } - { \bf y } ) \right\| ^ { 2 } } } \\ { { \displaystyle ~ = \left( H { \bf x } - { \bf y } \right) ^ { T } W ^ { \frac { 1 } { 2 } } Q ^ { T } Q W ^ { \frac { 1 } { 2 } } \Big ( H { \bf x } - { \bf y } \Big ) . } } \end{array}
$$

Select $Q$ such that

$$
Q W ^ { \frac { 1 } { 2 } } H = { \Biggl [ } R { \Biggr ] } { \mathrm { a n d d e f i n e ~ } } Q W ^ { \frac { 1 } { 2 } } \mathbf { y } \equiv { \Biggl [ } \mathbf { b } { \Biggr ] }
$$

where

$R$ is a $n \times n$ upper-triangular matrix of rank $n$

$O$ is a $( m - n ) \times n$ null matrix $\mathbf { b }$ is a $n \times 1$ column vector $\mathbf { e }$ is a $( m - n ) \times 1$ column vector.

The results given by Eq. (5.3.6) assume that $m > n$ and $H$ is of rank $n$ . Using Eq. (5.3.6), Eq. (5.3.5) can be written as

$$
J ( \mathbf { x } ) = | [ { \binom { R } { O } } \mathbf { x } - [ \mathbf { b } ] | ^ { 2 } .
$$

Expanding leads to

$$
J ( \mathbf { x } ) = \Big \| R \mathbf { x } - \mathbf { b } \Big \| ^ { 2 } + \Big \| \mathbf { e } \Big \| ^ { 2 } .
$$

Only the first term in Eq. (5.3.8) is a function of $\mathbf { x }$ , so the value of $\mathbf { x }$ that minimizes $J ( \mathbf { x } )$ is obtained by requiring that

$$
R \hat { \mathbf x } = \mathbf b
$$

and the minimum value of the performance index becomes (equating $J ( \hat { x } )$ in Eq. (5.3.1) and Eq. (5.3.8))

$$
J ( \hat { \mathbf { x } } ) = \left\| \mathbf { e } \right\| ^ { 2 } = \left\| W ^ { \frac { 1 } { 2 } } ( H \hat { \mathbf { x } } - \mathbf { y } ) \right\| ^ { 2 } .
$$

That is, $\lVert \mathbf e \rVert$ is the norm of the observation residual vector, which for a linear system will be equal to the weighted sum of the squares of observation residuals determined by using $\hat { \bf x }$ in Eq. (5.3.10).

# 5.4 GIVENS TRANSFORMATIONS

The procedure described in the previous section is direct and for implementation requires only that a convenient procedure for computing $Q$ be obtained. One such procedure can be developed based on the Givens plane rotation (Givens, 1958). Let $\mathbf { x }$ be a $2 \times 1$ vector having components $\mathbf { x } ^ { T } = \left[ x _ { 1 } x _ { 2 } \right]$ and let $G$ be a $2 \times 2$ orthogonal matrix associated with the plane rotation through the angle $\theta$ . Then select $G$ such that

$$
G \mathbf { x } = \mathbf { x } ^ { \prime } = { \binom { x _ { 1 } ^ { \prime } } { 0 } } .
$$

To this end, consider the transformation

$$
{ \Bigg [ } x _ { 1 } ^ { \prime } { \Bigg ] } = { \Bigg [ } { \cos \theta \sin \theta } { \Bigg ] } { \Bigg [ } x _ { 1 } { \Bigg ] }
$$

or

$$
\begin{array} { r l } & { x _ { 1 } ^ { \prime } = \quad \cos \theta x _ { 1 } + \sin \theta x _ { 2 } } \\ & { x _ { 2 } ^ { \prime } = - \sin \theta x _ { 1 } + \cos \theta x _ { 2 } . } \end{array}
$$

Equations (5.4.3) represent a system of two equations in three unknowns; that is, $x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime }$ , and $\theta$ . The Givens rotation is defined by selecting the rotation $\theta$ such that $x _ { 2 } ^ { \prime } = 0$ . That is, let

$$
\begin{array} { r } { x _ { 1 } ^ { \prime } = \quad \cos \theta x _ { 1 } + \sin \theta x _ { 2 } } \\ { 0 = - \sin \theta x _ { 1 } + \cos \theta x _ { 2 } . } \end{array}
$$

From Eq. (5.4.5), it follows that

$$
\tan \theta = \frac { x _ { 2 } } { x _ { 1 } } , \sin \theta = \frac { x _ { 2 } } { \sqrt { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } } } , \cos \theta = \frac { x _ { 1 } } { \sqrt { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } } } .
$$

The positive value associated with the square root operation is selected for the following discussion. Substituting the expression for $\sin \theta$ and $\cos \theta$ into Eq. (5.4.4) leads to

$$
x _ { 1 } ^ { \prime } = \frac { x _ { 1 } ^ { 2 } } { \sqrt { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } } } + \frac { x _ { 2 } ^ { 2 } } { \sqrt { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } } } = \sqrt { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } } .
$$

Consider the application of the transformation

$$
G ( \theta ) = \left[ \begin{array} { r } { { \cos \theta \sin \theta } } \\ { { - \sin \theta \cos \theta } } \end{array} \right]
$$

to two general row vectors $\mathbf { h } _ { i }$ and $\mathbf { h } _ { k }$ ; for example,

$$
G \left[ \begin{array} { l } { h _ { i i } \ h _ { i i + 1 } \ . . . h _ { i n } } \\ { h _ { k i } h _ { k i + 1 } \ . . . h _ { k n } } \end{array} \right] = \left[ \begin{array} { l } { h _ { i i } ^ { \prime } h _ { i i + 1 } ^ { \prime } \ . . . h _ { i n } ^ { \prime } } \\ { 0 \ h _ { k i + 1 } ^ { \prime } \cdot . . . h _ { k n } ^ { \prime } } \end{array} \right] .
$$

That is, for any two general row vectors, $\mathbf { h } _ { i }$ and $\mathbf { h } _ { k }$ , the transformation is applied to the first column so as to null $h _ { k i }$ . The transformation that accomplishes this is applied to each remaining column to obtain the transformed matrix. Hence,

$$
\begin{array} { r } { \left[ \begin{array} { l } { \cos \theta \sin \theta } \\ { - \sin \theta \cos \theta } \end{array} \right] \left[ h _ { i i } \right] = \left[ \begin{array} { l } { h _ { i i } ^ { \prime } } \\ { h _ { k i } } \end{array} \right] } \end{array}
$$

or

$$
\begin{array} { r c l } { { } } & { { } } & { { \sin \theta = h _ { k i } / \sqrt { h _ { i i } ^ { 2 } + h _ { k i } ^ { 2 } } = h _ { k i } / h _ { i i } ^ { \prime } } } \\ { { } } & { { } } & { { \cos \theta = h _ { i i } / \sqrt { h _ { i i } ^ { 2 } + h _ { k i } ^ { 2 } } = h _ { i i } / h _ { i i } ^ { \prime } } } \\ { { } } & { { } } & { { h _ { i i } ^ { \prime } = \sqrt { h _ { i i } ^ { 2 } + h _ { k i } ^ { 2 } } . } } \end{array}
$$

Then for all other columns,

$$
\begin{array} { c } { { h _ { i j } ^ { \prime } = h _ { i j } \cos \theta + h _ { k j } \sin \theta } } \\ { { { } } } \\ { { j = i + 1 , \ldots , n } } \\ { { { } h _ { k j } ^ { \prime } = - h _ { i j } \sin \theta + h _ { k j } \cos \theta . } } \end{array}
$$

By using this transformation repetitively as $k$ goes from $i + 1$ to $m$ , the remaining elements of the $i ^ { \mathrm { t h } }$ column can be nulled. Then by moving down the diagonal and applying the transformation to successive columns whose first element lies on the diagonal, a rank $n$ matrix can be reduced to an upper triangular $n \times n$ matrix with a lower $( m - n ) \times n$ null matrix. If the element to be nulled already has a value of zero, the transformation matrix will be the identity matrix and the corresponding transformation may be skipped.

As an example, the transformation to null the fourth element in the third column is shown as follows:

$$
\begin{array} { r } { \left[ \begin{array} { l } { 1 } \\ { 1 } \\ { 1 } \\ { C ^ { 4 , 3 } S ^ { 4 , 3 } } \\ { - S ^ { 4 , 3 } C ^ { 4 , 3 } } \\ { 1 } \\ { 1 } \\ { 1 } \\ { \ddots } \\ { 1 } \\ { 0 } \end{array} \right] \left[ \begin{array} { l l l l } { h _ { 1 1 } ~ h _ { 1 2 } ~ h _ { 1 3 } \cdots ~ h _ { 1 n } ~ y _ { 1 } } \\ { 0 } & { h _ { 2 2 } ~ h _ { 2 3 } \cdots ~ h _ { 2 n } ~ y _ { 2 } } \\ { 0 } & { 0 } & { h _ { 3 3 } \cdots ~ h _ { 3 n } ~ y _ { 3 } } \\ { 0 } & { 0 } & { h _ { 4 3 } \cdots ~ h _ { 4 n } ~ y _ { 4 } } \\ { 0 } & { 0 } & { h _ { 5 3 } \cdots ~ h _ { 5 n } ~ y _ { 5 } } \\ { 0 } & { 0 } & { h _ { 6 3 } \cdots ~ h _ { 6 n } ~ y _ { 6 } } \\ { \vdots } & { \vdots } & { \vdots } \\ { ~ 0 } & { 0 } & { h _ { m 3 } \cdots ~ h _ { m } ~ y _ { m } } \end{array} \right] } \end{array}
$$

$$
\begin{array} { r } { \left[ \begin{array} { c c c c c } { h _ { 1 1 } h _ { 1 2 } h _ { 1 3 } \cdots h _ { 1 n } \ y _ { 1 } } \\ { 0 } & { h _ { 2 2 } h _ { 2 3 } \cdots h _ { 2 n } \ y _ { 2 } } \\ { 0 } & { 0 } & { h _ { 3 3 } ^ { \prime \prime } \cdots h _ { 3 n } ^ { \prime \prime } \ y _ { 3 } ^ { \prime } } \\ { 0 } & { 0 } & { 0 } & { \cdots h _ { d n } ^ { \prime \prime } \ y _ { 4 } ^ { \prime \prime } } \\ { 0 } & { 0 } & { h _ { 5 3 } \cdots h _ { 5 n } \ y _ { 5 } } \\ { 0 } & { 0 } & { h _ { 6 3 } \cdots h _ { 6 n } \ y _ { 6 } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { h _ { m 3 } \cdots h _ { m n } \ y _ { m } } \end{array} \right] . } \end{array}
$$

The prime superscript identifies the two rows that are affected by this transformation (rows three and four). Notice that the location of $- \sin \theta$ in the Givens transformation matrix corresponds to the location of the element to be nulled in the $H$ matrix. For example, in the previous example both are element (4,3).

By using the transformation

$$
\begin{array} { r } { Q ^ { 5 , 3 } = \left[ \begin{array} { c } { 1 } \\ { 1 } \\ { C ^ { 5 , 3 } \ 0 S ^ { 5 , 3 } } \\ { 0 \phantom { - } 1 \ 0 } \\ { - S ^ { 5 , 3 } \ 0 C ^ { 5 , 3 } } \\ { 1 } \\ { 1 } \\ { 1 } \\ { \ddots } \\ { 1 } \end{array} \right] , } \end{array}
$$

the third and fifth rows will be transformed so that the term $h _ { 5 3 }$ will be zero.

# 5.4.1 A PRIORI INFORMATION AND INITIALIZATION

The formulation given earlier does not specifically address the question of $a$ priori information. Assume a priori information, $\overline { { \mathbf { x } } }$ and $\overline { { P } }$ , are available. The procedure is initialized by writing the a priori information in the form of a data equation; that is, in the form of $\mathbf { y } = H \mathbf { x } + \epsilon$ . This is accomplished by writing

$$
\overline { { \mathbf { x } } } = \mathbf { x } + \boldsymbol { \eta }
$$

where $\mathbf { x }$ is the true value and $\eta$ is the error in $\overline { { \mathbf { x } } }$ . We assume that

$$
E [ \pmb { \eta } ] = 0 , E [ \pmb { \eta } \pmb { \eta } ^ { T } ] = \overline { { P } } .
$$

Compute $\overline { S }$ , the upper triangular square root of $\overline { { P } }$ ,

$$
\overline { { { P } } } = \overline { { { S } } } \overline { { { S } } } ^ { T } .
$$

If $\overline { { P } }$ is not diagonal, the Cholesky decomposition may be used to accomplish this. Next compute $\overline { { R } }$ , the square root of the a priori information matrix, $\overline { { \Lambda } }$ ,

$$
\overline { { { \Lambda } } } = \overline { { { P } } } ^ { - 1 } = \overline { { { S } } } ^ { - T } \overline { { { S } } } ^ { - 1 } = \overline { { { R } } } ^ { T } \overline { { { R } } }
$$

hence,

$$
\overline { { { R } } } = \overline { { { S } } } ^ { - 1 } .
$$

Multiplying Eq. (5.4.15) by $\overline { { R } }$ yields

$$
\begin{array} { r } { \overline { { R } } \overline { { \mathbf { x } } } = \overline { { R } } \mathbf { x } + \overline { { R } } \eta . } \end{array}
$$

Define

$$
\begin{array} { r } { \overline { { \mathbf { b } } } \equiv \overline { { R } } \overline { { \mathbf { x } } } , \overline { { \eta } } \equiv \overline { { R } } \eta , } \end{array}
$$

then

$$
\overline { { \mathbf { b } } } = \overline { { R } } \mathbf { x } + \overline { { \eta } }
$$

where $\overline { { \eta } } \sim ( O , I )$ . Note that Eq. (5.4.22) expresses the a priori information in the form of the data equation, $\mathbf { y } = H \mathbf { x } + \epsilon$ . Hence, the equations we wish to solve for $\hat { \bf x }$ , using orthogonal transformations, are

$$
\begin{array} { r } { \overline { { \mathbf { b } } } = \overline { { R } } \mathbf { x } + \overline { { \eta } } } \\ { \mathbf { y } = H \mathbf { x } + \epsilon } \end{array}
$$

where $\mathbf { x }$ is an $n$ vector and $\mathbf { y }$ is an $m$ vector.

The least squares solution for $\mathbf { x }$ in Eq. (5.4.23) is found by minimizing the performance index (we assume that $\epsilon$ has been prewhitened so that $\epsilon \sim ( O , I )$ ; if not, replace $\epsilon$ with $W ^ { 1 / 2 } \epsilon$ in $J$ )

$$
\begin{array} { r l } & { J = \| \overline { { \boldsymbol { \eta } } } \| ^ { 2 } + \| \epsilon \| ^ { 2 } } \\ & { \quad = \| \overline { { R } } \mathbf { x } - \overline { { \mathbf { b } } } \| ^ { 2 } + \| H \mathbf { x } - \mathbf { y } \| ^ { 2 } } \\ & { \quad = \left\| \begin{array} { l } { \left[ \overline { { R } } \right] \mathbf { x } - \left[ \overline { { \mathbf { b } } } \right] } \\ { H } \end{array} \right\| ^ { 2 } . } \end{array}
$$

After multiplying by an orthogonal transformation, $Q$ , Eq. (5.4.24) may be written as

$$
J = \left\{ \left[ { \overline { { R } } } \right] \mathbf { x } - \left[ { \overline { { \mathbf { b } } } } \right] \right\} ^ { T } Q ^ { T } Q \left\{ \left[ { \overline { { R } } } \right] \mathbf { x } - \left[ { \overline { { \mathbf { b } } } } \right] \right\} .
$$

Choose $Q$ so that

$$
Q \left[ { \frac { \overline { { R } } } { H } } \right] = { \binom { R } { O } } , { \mathrm { a n d d e f i n e } } Q \left[ { \overline { { \mathbf { b } } } } \right] \equiv { \left[ \begin{array} { l } { \mathbf { b } } \\ { \mathbf { e } } \end{array} \right] }
$$

where $R$ is upper triangular. Eq. (5.4.24) can now be written as

$$
J = \| [ { \binom { R } { O } } \mathbf { x } - [ \mathbf { b } ] \| ^ { 2 }
$$

or

$$
J = \left\| R \mathbf { x } - \mathbf { b } \right\| ^ { 2 } + \left\| \mathbf { e } \right\| ^ { 2 }
$$

as noted before. The minimum value of $J$ is found by choosing $\hat { \bf x }$ so that

$$
R \hat { \mathbf { x } } - \mathbf { b } = 0 .
$$

The vector $\hat { \bf x }$ is obtained by the backward substitution described by Eq. (5.2.8), where $z$ and $r$ are replaced by $b$ and $R$ , respectively. Observe that $\hat { \bf x }$ usually would be determined after processing all observations. However, intermediate values of $\hat { \bf x }$ could be determined at any point in the process.

The minimum value of $J$ is given by substituting $\hat { \bf x }$ into Eq. (5.4.24):

$$
J = \left\| \mathbf { e } \right\| ^ { 2 } = \sum _ { i = 1 } ^ { m } e _ { i } ^ { 2 } = \left\| { \overline { { R } } } { \hat { \mathbf { x } } } - { \overline { { \mathbf { b } } } } \right\| ^ { 2 } + \sum _ { i = 1 } ^ { m } \left( H _ { i } { \hat { \mathbf { x } } } - y _ { i } \right) ^ { 2 } .
$$

Note that the first term on the right-hand side of Eq. (5.4.30) corresponds to the norm of the error in the a priori value for $\mathbf { x }$ multiplied by the square root of the inverse of the a priori covariance matrix,

$$
\| \overline { { R } } \hat { \mathbf { x } } - \overline { { \mathbf { b } } } \| ^ { 2 } = \| \overline { { R } } ( \hat { \mathbf { x } } - \overline { { \mathbf { x } } } ) \| ^ { 2 }
$$

which also can be expressed as

$$
\left\| \overline { { R } } ( \widehat { \mathbf { x } } - \overline { { \mathbf { x } } } ) \right\| ^ { 2 } = ( \widehat { \mathbf { x } } - \overline { { \mathbf { x } } } ) ^ { T } \overline { { P } } ^ { - 1 } ( \widehat { \mathbf { x } } - \overline { { \mathbf { x } } } ) .
$$

From Eqs. (5.4.30) and (5.4.31) it is seen that

$$
\sum _ { i = 1 } ^ { m } e _ { i } ^ { 2 } = \| \overline { { R } } ( \hat { \mathbf { x } } - \overline { { \mathbf { x } } } ) \| ^ { 2 } + \sum _ { i = 1 } ^ { m } \left( H _ { i } \hat { \mathbf { x } } - y _ { i } \right) ^ { 2 }
$$

or

$$
\begin{array} { c } { \displaystyle \sum _ { i = 1 } ^ { m } e _ { i } ^ { 2 } = \| \overline { { R } } \hat { \pmb { \eta } } \| ^ { 2 } + \displaystyle \sum _ { i = 1 } ^ { m } \hat { \epsilon } _ { i } ^ { 2 } } \\ { \displaystyle = \hat { \pmb { \eta } } ^ { T } \overline { { R } } ^ { T } \overline { { R } } \hat { \pmb { \eta } } + \displaystyle \sum _ { i = 1 } ^ { m } \hat { \epsilon } _ { i } ^ { 2 } , } \end{array}
$$

where

$$
\hat { \pmb { \eta } } = \hat { \bf x } - \overline { { { \bf x } } } , \hat { \epsilon } _ { i } = y _ { i } - H _ { i } \hat { \bf x } .
$$

Consequently, $e _ { i } \neq \hat { \epsilon } _ { i }$ ; that is, the elements of the error vector $[ \mathbf { e } ] _ { m \times 1 }$ contain a contribution from errors in the $a$ priori information as well as the observation residuals. The RMS of the observation residuals, $\boldsymbol { \hat { \epsilon } } _ { i }$ , is given by

$$
\mathrm { R M S } = \sqrt { \frac { 1 } { m } \sum _ { i = 1 } ^ { m } \hat { \epsilon } _ { i } ^ { 2 } }
$$

and from Eq. (5.4.33)

$$
\sum _ { i = 1 } ^ { m } \hat { \epsilon } _ { i } ^ { 2 } = \sum _ { i = 1 } ^ { m } e _ { i } ^ { 2 } - \hat { \eta } ^ { T } \overline { { { R } } } ^ { T } \overline { { { R } } } \hat { \eta } .
$$

If the procedure is initialized with $n$ observations in place of $a$ priori information, $\overline { { \mathbf { x } } }$ and $\overline { { P } }$ , Eq. (5.4.33) becomes

$$
\sum _ { i = 1 } ^ { m - n } e _ { i } ^ { 2 } = \sum _ { i = 1 } ^ { m } \hat { \epsilon } _ { i } ^ { 2 }
$$

and again $e _ { i } \neq \hat { \epsilon } _ { i }$ because the first $n$ observations serve the same function as $a$ priori values of $\overline { { \mathbf { x } } }$ and $\overline { { P } }$ . Here we have assumed that the weighting matrix is the identity matrix. If not, $( H _ { i } { \hat { \mathbf { x } } } - y _ { i } ) ^ { 2 }$ in Eq. (5.4.30) and subsequent equations should be replaced by $W _ { i } ( H _ { i } \hat { \mathbf { x } } - y _ { i } ) ^ { 2 }$ .

An advantage of the orthogonal transformation approach, in addition to improved accuracy, is that the sum of squares of the residuals, $e _ { i }$ , based on the final value of $\hat { \bf x }$ is computed automatically as part of the solution procedure. To obtain this result with the conventional batch processor, one would have to go through the additional computation of evaluating Eq. (5.4.30) after solving the normal equations for $\hat { \bf x }$ .

This procedure of solving the least squares problem using orthogonal transformations can be described as a square root information batch processor. If the state vector is independent of time, it could be thought of as a filter because the best estimate of $\mathbf { x }$ could be generated after processing each observation. If the state vector is a function of time, the $H$ matrix must be combined with the state transition matrix to map the state to an epoch time as described in Chapter 4. As formulated here, it could not be implemented as a $\mathbf { f }$ ter without mapping the square root information matrix, $R$ , and the state estimate, $\hat { \bf x }$ , to the appropriate time for each observation. The square root information filter with time-dependent effects is described in Section 5.10.1.

In summary, given a priori information $\overline { { R } }$ and $\overline { { \mathbf { b } } }$ and observations

$$
y _ { i } = H _ { i } \mathbf { x } + \epsilon _ { i } , i = 1 , \ldots , m ,
$$

the matrix we wish to reduce to upper triangular form is

$$
[ \begin{array} { c c } { { { \overline { { { R } } } } } } & { { { \bf { \overline { { { b } } } } } } } \\ { { { \cal H } _ { 1 } } } & { { y _ { 1 } } } \\ { { { \cal H } _ { 2 } } } & { { y _ { 2 } } } \\ { { \vdots } } & { { \vdots } } \\ { { { \cal H } _ { m } } } & { { y _ { m } } } \end{array} ] \ \{ \begin{array} { c c }  { \scriptstyle \mathrm { ~ \} n } } \\ { { \bf \sigma } } \\ { { \bf \sigma } } \end{array} 
$$

where $\overline { { R } }$ is upper triangular.

# 5.4.2 GIVENS COMPUTATIONAL ALGORITHM

For purposes of the computational algorithm we will write Eq. (5.4.38) as

$$
\begin{array} { r l r } & { \overbrace { \left[ \begin{array} { l l } { \overline { { R } } } & { \begin{array} { l } { \overline { { \mathbf { b } } } } \\ { H } & { \begin{array} { l } { \mathbf { y } } \end{array} } } \end{array} \right] } ^ { n } } &  \} \end{array} \overbrace { \begin{array} { l } { \} { n + 1 } \end{array} } } & { } \\ & { \left[ \begin{array} { l } { \begin{array} { l } { \overline { { R } } } \\ { H } \end{array} } \end{array} \right] \} n } &  \} &  \} \end{array}
$$

Lowercase $r$ and $h$ in the following algorithm represent the elements of $\widetilde { R }$ and $\widetilde { H }$ respectively, in Eq. (5.4.39).

The algorithm using the Givens rotation for reducing the $( m + n ) \times ( n + 1 )$ matrix of Eq. (5.4.39) to upper triangular form can be expressed as follows:

$\mathrm { S u m } = 0 .$ 1. Do $k = 1 , . . . , m$

2. Do $i = 1 , \ldots , n$ If ( $h _ { k i } = 0 \mathrm { ~ , ~ }$ ) Go to 2

$$
\begin{array} { r l } & { r _ { i i } ^ { \prime } = \sqrt { r _ { i i } ^ { 2 } + h _ { k i } ^ { 2 } } } \\ & { S _ { i k } = h _ { k i } / r _ { i i } ^ { \prime } } \\ & { C _ { i k } = r _ { i i } / r _ { i i } ^ { \prime } } \\ & { h _ { k i } = 0 } \\ & { r _ { i i } = r _ { i i } ^ { \prime } } \end{array}
$$

3. Do $j = i + 1 , \ldots , n + 1$

$$
\begin{array} { r l } & { r _ { i j } ^ { \prime } = C _ { i k } r _ { i j } + S _ { i k } h _ { k j } } \\ & { h _ { k j } = - S _ { i k } r _ { i j } + C _ { i k } h _ { k j } } \\ & { r _ { i j } = r _ { i j } ^ { \prime } } \end{array}
$$

Next $j$   
Next $i$   
$\begin{array} { l } { e _ { k } = h _ { k j } } \\ { \mathrm { S u m } = \mathrm { S u m } + e _ { k } ^ { 2 } } \\ { \mathrm { N e x t } \ : k } \end{array}$

After application of this algorithm, the $( n + m ) \times ( n + 1 )$ matrix will appear

as

$$
Q [ { \begin{array} { l } { { \overline { { R } } } \colon { \overline { { \mathbf { b } } } } } \\ { H \colon \mathbf { y } } \end{array} } ] = { \pmod { \overbrace { R } } } \quad { \overbrace { \mathbf { b } } } ^ { n } ] \} n
$$

which is the required form for solution of the least squares estimation problem as given by Eq. (5.3.6). Note that $r _ { i , n + 1 } ( i = 1 , \dots , n )$ and $h _ { k , n + 1 } ( k = 1 , \ldots , m )$ given by the algorithm represent $\mathbf { b }$ and $\mathbf { e }$ , respectively, in Eq. (5.4.41). Also, $\begin{array} { r } { \mathrm { S u m } = \sum _ { k = 1 } ^ { m } e _ { k } ^ { 2 } } \end{array}$ .

Once the array has been reduced to the form given by Eq. (5.4.41), subsequent observations can be included by considering the following array:

$$
\left[ \begin{array} { c } { { R \mathbf b } } \\ { { H _ { m + 1 } y _ { m + 1 } } } \\ { { 0 \mathbf \Lambda } } \end{array} \right] =
$$

$$
\left[ \begin{array} { c c c c c } { R _ { 1 1 } } & { R _ { 1 2 } } & { \cdots } & { R _ { 1 n } } & { b _ { 1 } } \\ { 0 } & { R _ { 2 2 } } & { \cdots } & { R _ { 2 n } } & { b _ { 2 } } \\ { 0 } & { 0 } & { \cdots } & { R _ { 3 n } } & { b _ { 3 } } \\ { \vdots } & { } & { } & { } & { } \\ { 0 } & { 0 } & { \cdots } & { R _ { n n } } & { b _ { n } } \\ { H _ { m + 1 , 1 } H _ { m + 1 , 2 } \cdots H _ { m + 1 , n } y _ { m + 1 } } & { } & { } \\ { 0 } & { 0 } & { \cdots } & { 0 } & { e ^ { 2 } } \end{array} \right]
$$

where

$$
e ^ { 2 } = \sum _ { k = 1 } ^ { m } e _ { k } ^ { 2 } = \mathrm { S u m } .
$$

Then by application of a Givens rotation to rows 1 and $n + 1$ , $H _ { m + 1 , 1 }$ can be nulled. Successive applications moving down the main diagonal can be used to null the remaining $n - 1$ elements of the $n + 1 ^ { \mathrm { s t } }$ row and reduce the array to upper triangular form:

$$
\left[ \begin{array} { l l } { R ^ { \prime } } & { \mathbf { b } ^ { \prime } } \\ { 0 } & { e _ { m + 1 } } \\ { 0 } & { e ^ { 2 } } \end{array} \right] .
$$

Next $e ^ { 2 }$ is replaced by $e ^ { 2 } + e _ { m + 1 } ^ { 2 }$ and the procedure is repeated with the next observation, and so on. It is also obvious that a group of $m ^ { \prime }$ observations could be included by replacing the array $\left( H _ { m + 1 } , y _ { m + 1 } \right)$ with an array in which $H _ { m + 1 }$ has dimension $( m ^ { \prime } \times n )$ and $\mathbf { y } _ { m + 1 }$ has dimension $m ^ { \prime }$ . The Givens rotation would be used as before to reduce the augmented array to upper triangular form. Note that Sum is set to zero only before processing the first observation or batch of observations. Also note that if there are different observation types, e.g., range and range rate, the values of $e$ for each observation type should be stored in separate arrays.

The Givens algorithm operates on an individual row (i.e., observation) until it is in the proper form and then moves to the next row of the matrix. The algorithm can also be applied so that it operates column by column simply by interchanging the $k$ and $i$ loops. The same procedure just described for processing a new observation or batch of observations still applies. The following Givens algorithm operates on the successive columns.

$\mathrm { S u m } = 0 .$ 1. Do $i = 1 , \ldots , n$ 2. Do $k = 1 , \ldots , m$

If ( $h _ { k i } = 0 \mathrm { ~ , ~ }$ ) Go to 2

$$
\begin{array} { r l } & { r _ { i i } ^ { \prime } = \sqrt { r _ { i i } ^ { 2 } + h _ { k i } ^ { 2 } } } \\ & { S _ { i k } = h _ { k i } / r _ { i i } ^ { \prime } } \\ & { C _ { i k } = r _ { i i } / r _ { i i } ^ { \prime } } \\ & { h _ { k i } = 0 } \\ & { r _ { i i } = r _ { i i } ^ { \prime } } \end{array}
$$

3. Do $j = i + 1 , \ldots , n + 1$

$$
\begin{array} { r l } & { r _ { i j } ^ { \prime } = C _ { i k } r _ { i j } + S _ { i k } h _ { k j } } \\ & { h _ { k j } = - S _ { i k } r _ { i j } + C _ { i k } h _ { k j } } \\ & { r _ { i j } = r _ { i j } ^ { \prime } } \end{array}
$$

Next $j$

Next $k$

Next $i$

Do $\ell = 1 , \ldots , m$

$$
\mathrm { S u m } = \mathrm { S u m } + h _ { \ell , n + 1 } ^ { 2 }
$$

Next 

# 5.4.3 SQUARE ROOT FREE GIVENS TRANSFORMATION

The original Givens transformation requires the formation of square roots, which are more complex to compute than divisions or multiplications. The following procedure leads to a square root free algorithm.

Rather than seek the orthogonal transformation $Q$ , which leads to $Q W ^ { 1 / 2 } H =$ $[ R ^ { T } : 0 ] ^ { T }$ , we seek a factorization of $R$ of the form

$$
R = D ^ { \frac { 1 } { 2 } } U
$$

where $D$ is an $n \times n$ diagonal matrix and $U$ is $n \times n$ unit upper triangular matrix,

i.e.

$$
\begin{array} { r } { D ^ { 1 / 2 } = \left[ \begin{array} { l } { d _ { 1 } ^ { 1 / 2 } \qquad 0 } \\ { \quad d _ { 2 } ^ { 1 / 2 } \qquad } \\ { \cdot \qquad \cdot } \\ { 0 \qquad \quad d _ { n } ^ { 1 / 2 } } \end{array} \right] , U = \left[ \begin{array} { l l l l l } { 1 } & { U _ { 1 2 } } & { \cdot \cdot } & { U _ { 1 n } } \\ { 0 } & { 1 } & { U _ { 2 3 } } & { \cdot \cdot } & { U _ { 2 n } } \\ { \vdots } & & & { \vdots } \\ { 0 } & { \cdot \cdot } & { \cdot \cdot } & { \cdot \cdot } & { 1 } \end{array} \right] . } \end{array}
$$

Following Eq. (5.3.6) select the orthogonal matrix $Q$ , such that

$$
\begin{array} { r } { Q W ^ { \frac { 1 } { 2 } } H = \left[ \begin{array} { c } { D ^ { \frac { 1 } { 2 } } U } \\ { 0 } \end{array} \right] = \left[ \begin{array} { c c c c } { D ^ { \frac { 1 } { 2 } } \vdots } & { 0 } \\ { \cdots } & { \cdots } \\ { 0 } & { \vdots } & { 0 } \end{array} \right] \left[ \begin{array} { c } { U } \\ { \cdots } \\ { 0 } \end{array} \right] } \end{array}
$$

and

$$
Q W ^ { \frac { 1 } { 2 } } \mathbf { y } = \left[ \mathbf { b } \right] .
$$

Let

$$
{ \bf b } = D ^ { \frac { 1 } { 2 } } \widetilde { { \bf b } } .
$$

It follows from Eq. (5.3.7) that the least squares performance index can be expressed as

$$
J ( \mathbf { x } ) = \left\| \left[ { \cal D } ^ { \frac { 1 } { 2 } } U \right] \mathbf { x } - \left[ { \cal D } ^ { \frac { 1 } { 2 } } \widetilde { \mathbf { b } } \right] \right\| ^ { 2 }
$$

which for a minimum requires

$$
D ^ { \frac { 1 } { 2 } } U \hat { \mathbf { x } } = D ^ { \frac { 1 } { 2 } } \widetilde { \mathbf { b } } .
$$

Since $D ^ { 1 / 2 }$ is common to both sides of Eq. (5.4.48), the solution is

$$
U \hat { \mathbf { x } } = \widetilde { \mathbf { b } }
$$

and $\hat { \bf x }$ is obtained by backward recursion. Because the diagonals of $U$ are unitary, division by the $n$ diagonal elements is eliminated.

Consider now the use of the square root free Givens transformation to obtain the orthogonal decomposition (Gentleman, 1973). The product $W ^ { 1 / 2 } H$ can be

expressed in component form as

$$
W ^ { \frac { 1 } { 2 } } H = \left[ { \begin{array} { c c c } { \sigma _ { 1 } h _ { 1 1 } } & { \sigma _ { 1 } h _ { 1 2 } } & { \cdots } & { \sigma _ { 1 } h _ { 1 n } } \\ { \sigma _ { 2 } h _ { 2 1 } } & { \sigma _ { 2 } h _ { 2 2 } } & { \cdots } & { \sigma _ { 2 } h _ { 2 n } } \\ { \vdots } \\ { \sigma _ { m } h _ { m 1 } \sigma _ { m } h _ { m 2 } } & { \cdots } & { \sigma _ { m } h _ { m n } } \end{array} } \right]
$$

where

$$
\sigma _ { i } = W _ { i i } ^ { \frac { 1 } { 2 } } , W _ { i j } ^ { \frac { 1 } { 2 } } = 0 , i \neq j .
$$

Now consider the application of the Givens rotation, where any two rows of Eq. (5.4.19) are expressed in the form

$$
\begin{array} { r l r } & { } & { G \left[ \sqrt { d _ { i } } \qquad \sqrt { d _ { i } } \ l _ { i , i + 1 } \ \cdots \sqrt { d _ { i } } \ l _ { i n } \ \right] } \\ & { } & { \qquad \sqrt { \delta _ { k } } \ h _ { k i } \ \sqrt { \delta _ { k } } \ h _ { k , i + 1 } \cdot \cdot \cdot \sqrt { \delta _ { k } } \ h _ { k n } \ \biggr ] } \\ & { } & { = \left[ \sqrt { d _ { i } ^ { \prime } } \ \sqrt { d _ { i } ^ { \prime } } \ l _ { i , i + 1 } ^ { \prime } \ \cdots \sqrt { d _ { i } ^ { \prime } } \ l _ { i n } ^ { \prime } \ \right] . } \\ & { } & \end{array}
$$

From Eq. (5.4.50), it follows that

$$
\begin{array} { c } { \sqrt { d _ { i } } = \sigma _ { i } h _ { i i } } \\ { \ } \\ { l _ { i j } = \sigma _ { i } h _ { i j } / \sigma _ { i } h _ { i i } , j = i + 1 , \ldots , , n } \\ { \sqrt { \delta _ { k } } = \sigma _ { k } . } \end{array}
$$

Then from Eq. (5.4.51), the Givens transformation, Eq. (5.4.2), applied to the first column leads to

$$
\begin{array} { c } { { \sqrt { d ^ { \prime } } = \cos \theta \sqrt { d _ { i } } + \sin \theta \sqrt { \delta _ { k } } h _ { k i } } } \\ { { 0 = - \sin \theta \sqrt { d _ { i } } + \cos \theta \sqrt { \delta _ { k } } h _ { k i } . } } \end{array}
$$

The second of Eq. (5.4.53) can be used to obtain

$$
\tan \theta = \frac { \sin \theta } { \cos \theta } = \frac { \sqrt { \delta _ { k } } h _ { k i } } { \sqrt { d _ { i } } }
$$

and hence

$$
\sin \theta = \sqrt { \delta _ { k } } h _ { k i } \bigg / \sqrt { d _ { i } + \delta _ { k } h _ { k i } ^ { 2 } }
$$

$$
\cos \theta = \sqrt { d _ { i } } \bigg / \sqrt { d _ { i } + \delta _ { k } h _ { k i } ^ { 2 } } .
$$

Substituting (5.4.54) into (5.4.53) leads to

$$
\sqrt { d _ { i } ^ { \prime } } = \sqrt { d _ { i } + \delta _ { k } h _ { k i } ^ { 2 } } .
$$

Hence, Eq. (5.4.54) becomes

$$
\sin \theta = \sqrt { \delta _ { k } } \ h _ { k i } / \sqrt { d _ { i } ^ { \prime } } ; \cos \theta = \sqrt { d _ { i } } / \sqrt { d _ { i } ^ { \prime } } .
$$

Then for the general transformation, the $i j ^ { \mathrm { t h } }$ element of the first row is

$$
\begin{array} { r l r } & { } & { \sqrt { d _ { i } ^ { \prime } } \ell _ { i j } ^ { \prime } = \cos \theta \sqrt { d _ { i } } \ell _ { i j } + \sin \theta \sqrt { \delta _ { k } } h _ { k j } } \\ & { } & { \quad = \frac { \sqrt { d _ { i } } \sqrt { d _ { i } } } { \sqrt { d _ { i } ^ { \prime } } } \ell _ { i j } + \frac { \sqrt { \delta _ { k } } h _ { k i } \sqrt { \delta _ { k } } } { \sqrt { d _ { i } ^ { \prime } } } h _ { k j } . } \end{array}
$$

Now, dividing by $\sqrt { d _ { i } ^ { \prime } }$ , yields

$$
\ell _ { i j } ^ { \prime } = \frac { d _ { i } } { d _ { i } ^ { \prime } } \ell _ { i j } + \frac { \delta _ { k } } { d _ { i } ^ { \prime } } h _ { k i } h _ { k j } .
$$

Using the definitions

$$
\overline { { C _ { i } } } = d _ { i } / d _ { i } ^ { \prime } , \overline { { S } } _ { i } = \delta _ { k } h _ { k i } / d _ { i } ^ { \prime }
$$

Eq. (5.4.57) becomes

$$
\ell _ { i j } ^ { \prime } = \overline { { C } } _ { i } \ell _ { i j } + \overline { { S } } _ { i } h _ { k j } .
$$

Similarly, the $k j ^ { \mathrm { t h } }$ element of the $k ^ { \mathrm { t h } }$ row is

$$
\sqrt { \delta _ { k } ^ { \prime } } h _ { k j } ^ { \prime } = - \sin \theta \sqrt { d _ { i } } \ell _ { i j } + \cos \theta \sqrt { \delta _ { k } } h _ { k j } .
$$

Then, using Eq. (5.4.56) results in

$$
\sqrt { \delta _ { k } ^ { \prime } } h _ { k j } ^ { \prime } = \frac { - \sqrt { \delta _ { k } } h _ { k i } } { \sqrt { d _ { i } ^ { \prime } } } \sqrt { d _ { i } } \ l _ { i j } + \frac { \sqrt { d _ { i } } } { \sqrt { d _ { i } ^ { \prime } } } \sqrt { \delta _ { k } } h _ { k j } .
$$

Dividing by $\sqrt { \delta _ { k } ^ { \prime } }$ leads to

$$
h _ { k j } ^ { \prime } = \frac { \sqrt { d _ { i } } } { \sqrt { d _ { i } ^ { \prime } } } \frac { \sqrt { \delta _ { k } } } { \sqrt { \delta _ { k } ^ { \prime } } } h _ { k j } - \frac { \sqrt { \delta _ { k } } \sqrt { d _ { i } } } { \sqrt { d _ { i } ^ { \prime } } \sqrt { \delta _ { k } ^ { \prime } } } h _ { k i } l _ { i j } .
$$

Because $\sqrt { \delta _ { k } ^ { \prime } }$ is an arbitrary scaling factor for each element of the $k ^ { \mathrm { t h } }$ row, it is convenient to let

$$
\sqrt { \delta _ { k } ^ { \prime } } = \sqrt { \delta _ { k } } \times \frac { \sqrt { d _ { i } } } { \sqrt { d _ { i } ^ { \prime } } } .
$$

It then follows that Eq. (5.4.60) can be expressed as

$$
\begin{array} { r } { h _ { k j } ^ { \prime } = h _ { k j } - h _ { k i } l _ { i j } . } \end{array}
$$

The final values of $l _ { i j } ^ { \prime }$ become the elements of $U _ { i j }$ and $\tilde { b } _ { i }$ , and $h _ { k j } ^ { \prime }$ are the interim elements of the $_ \mathrm { H }$ matrix. The final value of $h _ { k j } ^ { \prime }$ in each row is the observation error. This will become clear from the examples of Section 5.6.

# 5.4.4 SQUARE ROOT FREE GIVENS COMPUTATIONAL ALGORITHM

If a priori information, $\overline { { \mathbf { x } } }$ and $\overline { { P } }$ , are available the algorithm is initialized by computing $\overline { S }$ and $\overline { { R } }$ where

$$
\overline { { P } } = \overline { { S } } \overline { { S } } ^ { T }
$$

and

$$
\overline { { { R } } } = \overline { { { S } } } ^ { - 1 } .
$$

The a priori information we need is ${ \overline { { D } } } , { \overline { { U } } }$ , and $\widetilde { \mathbf { b } }$ , where

$$
{ \overline { { R } } } = { \overline { { D } } } ^ { \frac { 1 } { 2 } } { \overline { { U } } } .
$$

Hence,

$$
\overline { { d } } _ { i } = \overline { { R } } _ { i i } ^ { 2 } \ i = 1 \dots n
$$

and

$$
\overline { { U } } = \left[ \begin{array} { l l l l } { 1 \overline { { U } } _ { 1 2 } \cdots \cdots \cdots \overline { { U } } _ { 1 n } } \\ { 0 \quad 1 \overline { { U } } _ { 2 3 } \cdots \overline { { U } } _ { 2 n } } \\ { 0 \quad 0 \quad 1 } & { \vdots } \\ { \vdots } & { \ddots } & { \vdots } \\ { 0 \quad \cdots \cdots \cdots \cdots } & { 1 } \end{array} \right] ,
$$

where $\overline { { d } } _ { i }$ are the square of the diagonal elements of $\overline { { R } }$ ; for example, $d _ { i } = R _ { i i } ^ { 2 }$ , $i = 1 , \ldots , n$ , and $\overline { { U } } _ { i j } = \overline { { R } } _ { i j } / \overline { { R } } _ { i i } ; i = 1 , \dots n ; j = i + 1 , n$ . Also, recall from Eq. (5.4.21) that

$$
\overline { { { \bf b } } } = \overline { { R } } \overline { { \bf x } }
$$

and the a priori value of $\widetilde { \mathbf { b } } \equiv \overline { { \widetilde { \mathbf { b } } } }$ is

$$
\overline { { \widetilde { { \bf b } } } } = \overline { { \cal D } } ^ { - \frac { 1 } { 2 } } \overline { { { \bf b } } } .
$$

Given observations $y _ { i }$ and $i = 1 \dots m$ , we now have the necessary information to execute the algorithm; that is, we wish to apply a series of orthogonal transformations, $G$ , so that

$$
\begin{array} { r l r } { G } &  { } [ \begin{array} { c c c c c } { \stackrel { n } { \longrightarrow } } & { \stackrel {  } { \longrightarrow } } & { \quad } & { \stackrel { n } { \longrightarrow } } & { \stackrel {  } { \longrightarrow } } \\ { \overline { { U } } } & { \stackrel {  } { \tilde { \textbf { b } } } } \\ { \hfill ~ [ \begin{array} { c c c c c } { y _ { 1 } } & { \frac { \pi } { \tilde { \textbf { b } } } } \\ { y _ { 1 } } & { \frac { \pi } { y _ { 1 } } } \\ { \vdots } & { \vdots } \\ { H _ { m } } & { y _ { m } } \end{array} ] \} ^ { h } } & { { } = } & { { } [ \begin{array} { c c c c c } { \overbrace { U } } & { \stackrel {  } { \tilde { \textbf { b } } } } \\ { 0 } & { \stackrel { e _ { 1 } } { e _ { 1 } } } \\ { 0 } & { \vdots } \\ { e _ { m } } \end{array} ] \Bigg \} _ { m } ^ { h } \ . } \end{array} \end{array}
$$

The computational algorithm for operating on the data one row, or one observation, at a time is as follows:

$$
\begin{array} { l l } { { \mathrm { S u m } = 0 } } \\ { { \qquad } } \\ { { U _ { i i } = 1 } } & { { \qquad i = 1 , \dots , n } } \end{array}
$$

1. Do $k = 1 , \ldots , m$

$$
\delta _ { k } = 1
$$

2. Do $i = 1 , \ldots , n$

If $h _ { k i } = 0$ ) Go to 2

$$
\begin{array} { l } { { d _ { i } ^ { \prime } = d _ { i } + \delta _ { k } h _ { k i } ^ { 2 } } } \\ { { \overline { { C } } = d _ { i } / d _ { i } ^ { \prime } } } \\ { { \overline { { S } } = \delta _ { k } h _ { k i } / d _ { i } ^ { \prime } } } \\ { { y _ { k } ^ { \prime } = y _ { k } - \bar { b } _ { i } h _ { k i } } } \\ { { \tilde { b } _ { i } - \tilde { b } _ { i } \overline { { C } } + y _ { k } \overline { { S } } } } \\ { { y _ { k } = y _ { k } ^ { \prime } } } \\ { { \delta _ { k } = \delta _ { k } \overline { { C } } } } \\ { { d _ { i } = d _ { i } ^ { \prime } } } \end{array}
$$

3. Do $j = i + 1 , \dotsc , n$

$$
\begin{array} { l } { { { h } _ { k j } ^ { \prime } = { h } _ { k j } - { U } _ { i j } { h } _ { k i } } } \\ { { { U } _ { i j } = { U } _ { i j } \overline { { C } } + { h } _ { k j } \overline { { S } } } } \\ { { { h } _ { k j } = { h } _ { k j } ^ { \prime } } } \end{array}
$$

$$
\begin{array} { l } { \operatorname { N e x t } ~ j } \\ { \operatorname { N e x t } ~ i } \\ { e _ { k } = \sqrt { \delta _ { k } } y _ { k } } \\ { \operatorname { S u m } = \operatorname { S u m } + e _ { k } ^ { 2 } } \end{array}
$$

Next k

The diagonal elements of $D$ are given by $d _ { i } ( i = 1 , \ldots , n )$ , the upper triangular elements of $U$ are given by $U _ { i j } ( i = 1 , \ldots , n , \ j = i + 1 , \ldots , n + 1 )$ , the elements of $\widetilde { \mathbf { b } }$ are given by $\tilde { b } _ { i }$ $( i = 1 , \ldots , n )$ and the elements of $\mathbf { e }$ are given by $e _ { k } ( k = 1 , \ldots , m )$ . The same procedure described for the Givens algorithm at the end of Section 5.4.2 can be used to handle multiple batches of observation data. Note that Sum and $\delta _ { k }$ are set to zero and one, respectively, only for the fir st batch of observations.

The vector $\hat { \bf x }$ is obtained from $U$ and $\widetilde { \mathbf { b } }$ by performing a back substitution using Eq. (5.4.49). Note that $D$ is not needed to compute $\hat { \bf x }$ but is needed to compute the estimation error covariance matrix, $P = U ^ { - 1 } D ^ { - 1 } U ^ { - T }$ (see Eq. (5.4.80)).

# 5.4.5 A SIMPLIFIED SQUARE ROOT FREE GIVENS TRANSFORMATION

The square root free Givens algorithm can be simplified further (Gentleman, 1973) by noting that we may write

$$
\begin{array} { r } { y _ { k } ^ { \prime } = y _ { k } - \tilde { b } _ { i } h _ { k i } } \\ { \tilde { b } _ { i } ^ { \prime } = \tilde { b } _ { i } \overline { { C } } + y _ { k } \overline { { S } } } \end{array}
$$

and

$$
\begin{array} { l } { { h _ { k j } ^ { \prime } = h _ { k j } - U _ { i j } h _ { k i } } } \\ { { U _ { i j } ^ { \prime } = U _ { i j } \overline { { C } } + h _ { k j } \overline { { S } } } } \end{array}
$$

as

$$
\begin{array} { l } { { y _ { k } ^ { \prime } = y _ { k } - \tilde { b } _ { i } h _ { k i } } } \\ { { \tilde { b } _ { i } ^ { \prime } = \tilde { b } _ { i } + y _ { k } ^ { \prime } \overline { { { S } } } } } \end{array}
$$

and

$$
\begin{array} { l } { { h _ { k j } ^ { \prime } = h _ { k j } - U _ { i j } ~ h _ { k i } } } \\ { { U _ { i j } ^ { \prime } = U _ { i j } + h _ { k j } ^ { \prime } ~ \overline { { { S } } } } } \end{array}
$$

by noting that

$$
\overline { { C } } = 1 - \overline { { S } } h _ { k i } .
$$

Hence, the algorithm may be simplified by eliminating the need to compute $\overline { { C } }$ explicitly. The computational algorithm becomes

$$
\mathrm { S u m } = 0 .
$$

1. Do $k = 1 , \ldots , m$

$$
\delta _ { k } = 1
$$

2. Do $i = 1 , \ldots , n$

If $h _ { k i } = 0$ ) go to 2

$$
\begin{array} { r l } & { d _ { i } ^ { \prime } = d _ { i } + \delta _ { k } \ h _ { k i } ^ { 2 } } \\ & { \overline { { S } } = \delta _ { k } \ h _ { k i } / d _ { i } ^ { \prime } } \\ & { y _ { k } ^ { \prime } = y _ { k } - \tilde { b } _ { i } \ h _ { k i } } \\ & { \tilde { b } _ { i } = \tilde { b } _ { i } + y _ { k } ^ { \prime } \ \overline { { S } } } \\ & { y _ { k } = y _ { k } ^ { \prime } } \\ & { \delta _ { k } = \delta _ { k } \ d _ { i } / d _ { i } ^ { \prime } } \\ & { d _ { i } = d _ { i } ^ { \prime } } \end{array}
$$

3. Do $j = i + 1 , \dotsc , n$

$$
\begin{array} { l } { { h _ { k j } ^ { \prime } = h _ { k j } - U _ { i j } \ : h _ { k i } } } \\ { { \ : U _ { i j } = U _ { i j } + h _ { k j } ^ { \prime } \ : \overline { { S } } } } \\ { { h _ { k j } = h _ { k j } ^ { \prime } } } \end{array}
$$

$$
\begin{array} { c } { { e _ { k } = \sqrt { \delta _ { k } } y _ { k } } } \\ { { \mathrm { S u m = S u m + } e _ { k } ^ { 2 } } } \end{array}
$$

This version of the square root free Givens algorithm is preferred because it involves fewer operations than that of Eq. (5.4.70).

# 5.4.6 IMPLEMENTATION CONSIDERATIONS

The following observations on the square root free algorithm are given:

1. Note that no square roots are required.

2. The algorithm assumes that a priori information ${ \overline { { D } } } , { \overline { { U } } } .$ , and $\overline { { \widetilde { \mathbf { b } } } }$ computed from $\overline { { P } }$ and $\bar { \bf x }$ is available. These are computed using Eqs. (5.4.63) through (5.4.68):

$$
\begin{array} { l } { \overline { { P } } = \overline { { S } } \overline { { S } } ^ { T } } \\ { \overline { { R } } = \overline { { S } } ^ { - 1 } } \\ { \bar { d } _ { i } = \overline { { R } } _ { i i } ^ { 2 } , i = 1 \ldots n } \\ { \overline { { U } } = \overline { { D } } ^ { - 1 / 2 } \overline { { R } } } \\ { \overline { { \tilde { \mathbf { b } } } } = \overline { { D } } ^ { - 1 / 2 } \overline { { R } } \bar { \mathbf { x } } = \overline { { U } } \bar { \mathbf { x } } } \end{array}
$$

3. If no a priori information is given the algorithm may be initialized using

$$
\begin{array} { l } { \overline { { D } } = 1 0 ^ { - 1 6 \ddag } } \\ { \overline { { U } } = I } \\ { \overline { { \widetilde { \mathbf { b } } } } = 0 . } \end{array}
$$

4. When an unprimed variable appears on both sides of an equation, this is taken to represent a replacement.

5. Remember that an orthogonal transformation does not change the norm or Euclidian length of each column of the original matrix.

6. Each of the Givens algorithms (Eqs. (5.4.40), (5.4.70), and (5.4.76)) operates on the subject matrix row by row. They can be modifie d to operate column by column by interchanging the $k$ and $i$ loops.

The value of $\hat { \bf x }$ is computed from Eq. (5.4.49),

$$
U \hat { \mathbf { x } } = \widetilde { \mathbf { b } }
$$

by using the back substitution algorithm obtained by a slight modification of Eq. (5.2.8):

$$
\begin{array} { c } { { i = n , ~ n - 1 , \ldots , 1 } } \\ { { \nonumber } } \\ { { \hat { x } _ { i } = \tilde { b } _ { i } - \displaystyle \sum _ { j = i + 1 } ^ { n } U _ { i j } \hat { x } _ { j } . } } \end{array}
$$

The estimation error covariance is computed from

$$
\begin{array} { l } { P = R ^ { - 1 } ~ R ^ { - T } } \\ { \ = ( D ^ { \frac { 1 } { 2 } } ~ U ) ^ { - 1 } ( U ^ { T } D ^ { \frac { 1 } { 2 } } ) ^ { - 1 } } \\ { \ = U ^ { - 1 } D ^ { - \frac { 1 } { 2 } } ~ D ^ { - \frac { 1 } { 2 } } U ^ { - T } } \\ { \ = U ^ { - 1 } D ^ { - 1 } U ^ { - T } } \end{array}
$$

where $U ^ { - 1 }$ may be computed by using Eq. (5.2.20).

# 5.5 THE HOUSEHOLDER TRANSFORMATION

An alternate computational approach can be developed by using orthogonal reflections rather than the planar rotations used in the previous discussions. Such transformations, which are referred to as Householder transformations (Householder, 1958), have the advantage of nulling a complete column in a single operation. Consider the following matrix

$$
\boldsymbol { T } = \boldsymbol { I } - 2 \hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T }
$$

where $\hat { \mathbf { u } } ^ { T } \hat { \mathbf { u } } = 1$ . The matrix $T$ satisfies the following conditions:

1) $T$ is symmetric.   
2) $T$ is idempotent: $T ^ { 2 } = I$ .   
3) $T$ is orthogonal: $T T ^ { T } = I$ .

Proof: The first condition follows from the definition. Then, since $\hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T }$ is symmetric and $\hat { \mathbf { u } } ^ { T } \hat { \mathbf { u } } = 1$ ,

$$
\begin{array} { r l } & { T ^ { 2 } = ( I - 2 \hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T } ) ( I - 2 \hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T } ) = I - 4 \hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T } + 4 \hat { \mathbf { u } } ( \hat { \mathbf { u } } ^ { T } \hat { \mathbf { u } } ) \hat { \mathbf { u } } ^ { T } } \\ & { \quad \quad = I - 4 \hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T } + 4 \hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T } = I . } \end{array}
$$

From Properties 1 and 2, it follows that

$$
T ^ { 2 } = T T ^ { T } = I .
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0005_pages_0281-0350/auto/images/47f3d7354e489691be705ec54ecc2f0e6c243cc8c10a56ade4ac0d50fac3c542.jpg)  
Figure 5.5.1: An elementary reflec tion.

Matrices of the form $T$ are called elementary Hermitian matrices, elementary reflectors , or Householder transformations. The geometric notion of a reflection is shown in Fig. 5.5.1 and can be developed as follows. Let $u _ { n }$ be the plane perpendicular to $\mathbf { u }$ . Let

$$
\hat { \mathbf { u } } = \mathbf { u } \big / \lVert \mathbf { u } \rVert
$$

and let ${ \boldsymbol { T } } \mathbf { z }$ be the reflection of $\mathbf { z }$ in the plane $u _ { n }$ —the mirror image of $\mathbf { z }$ where the plane $u _ { n }$ represents the mirror. That is,

$$
\mathbf { z } = ( \mathbf { z } ^ { T } \hat { \mathbf { u } } ) \hat { \mathbf { u } } + \mathbf { v }
$$

and

$$
\begin{array} { r } { T \mathbf { z } = - ( \mathbf { z } ^ { T } \hat { \mathbf { u } } ) \hat { \mathbf { u } } + \mathbf { v } . } \end{array}
$$

Eliminating $\mathbf { v }$ leads to

$$
- T \mathbf { z } + \mathbf { z } = 2 ( \mathbf { z } ^ { T } \hat { \mathbf { u } } ) \hat { \mathbf { u } } .
$$

Therefore,

$$
\begin{array} { r } { T \mathbf { z } = \mathbf { z } - 2 ( \mathbf { z } ^ { T } \hat { \mathbf { u } } ) \hat { \mathbf { u } } } \\ { = \mathbf { z } - 2 \hat { \mathbf { u } } ( \hat { \mathbf { u } } ^ { T } \mathbf { z } ) } \\ { = \mathbf { z } - 2 \hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T } \mathbf { z } } \end{array}
$$

where we have used the fact that $\mathbf { z } ^ { T } \hat { \mathbf { u } } = \hat { \mathbf { u } } ^ { T } \mathbf { z }$ because this quantity is a scalar. Finally,

$$
T \mathbf { z } = [ I - 2 \hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T } ] \mathbf { z } .
$$

Hence,

$$
\begin{array} { r } { T = I - 2 \frac { \mathbf { u } \mathbf { u } ^ { T } } { \mathbf { u } ^ { T } \mathbf { u } } } \\ { = I - \beta \mathbf { u } \mathbf { u } ^ { T } } \end{array}
$$

where

$$
\displaystyle \beta = 2 / \mathbf { u } ^ { T } \mathbf { u } = 2 \Big / \| \mathbf { u } \| ^ { 2 } .
$$

The following additional properties are of use:

4) If $u _ { j }$ , the $j ^ { t h }$ component of $\mathbf { u }$ , is zero, then $( T \mathbf { z } ) _ { j } = z _ { j }$ . That is, if the $j ^ { t h }$ component of $\mathbf { u }$ is zero, then the transformation $T$ leaves the $j ^ { t h }$ component of $\mathbf { z }$ unchanged.

Proof: This can be verified by writing down the product $\mathbf { u } \mathbf { u } ^ { T }$ and noting that the $j ^ { t h }$ row and $j ^ { t h }$ column vanish if $u _ { j }$ is zero.

5) If $\mathbf { u }$ is perpendicular to $\mathbf { z }$ , then $T \mathbf { z } = \mathbf { z }$ .

Proof: Since $T \mathbf { z } = [ I - \beta \mathbf { u } \mathbf { u } ^ { T } ] \mathbf { z } = \mathbf { z } - \beta \mathbf { u } ( \mathbf { u } ^ { T } \mathbf { z } )$ , it follows that $\mathbf { u } ^ { T } \mathbf { z } = 0$ if $\mathbf { u }$ is perpendicular to $\mathbf { z }$ and hence that $T \mathbf { z } = \mathbf { z }$ .

$$
T \mathbf { z } = \mathbf { z } - \gamma \mathbf { u } , { \mathrm { w h e r e ~ } } \ \gamma = 2 \mathbf { z } ^ { T } \mathbf { u } / \mathbf { u } ^ { T } \mathbf { u } .
$$

Proof:

$$
\begin{array} { c } { { T \mathbf { z } = \left[ I - \frac { 2 \mathbf { u } \mathbf { u } ^ { T } } { \mathbf { u } ^ { T } \mathbf { u } } \right] \mathbf { z } = \mathbf { z } - 2 \mathbf { u } \mathbf { u } ^ { T } \mathbf { z } / \mathbf { u } ^ { T } \mathbf { u } } } \\ { { \mathrm { ~ } } } \\ { { \displaystyle = \mathbf { z } - \frac { 2 \left( \mathbf { z } ^ { T } \mathbf { u } \right) \mathbf { u } } { \mathbf { u } ^ { T } \mathbf { u } } = \mathbf { z } - 2 \left( \frac { \mathbf { z } ^ { T } \mathbf { u } } { \mathbf { u } ^ { T } \mathbf { u } } \right) \mathbf { u } } } \\ { { \mathrm { ~ } } } \\ { { \displaystyle = \mathbf { z } - \gamma \mathbf { u } . } } \end{array}
$$

Here we use the fact that $\mathbf { u } ^ { T } \mathbf { z }$ is a scalar; hence, $\mathbf { u } ^ { T } \mathbf { z } = \mathbf { z } ^ { T } \mathbf { u }$ . Note that the computation of $T$ requires significantly more computation than the computation of ${ \boldsymbol { T } } \mathbf { z }$ , if property 6 is used. Furthermore, using property 6, it is not necessary that $T$ be stored; only the elements of ${ \boldsymbol { T } } \mathbf { z }$ need to be stored.

The feature of the Householder transformation, $T$ , that is of crucial interest in this discussion is that $T$ can be used to introduce zeros into any column vector, $\mathbf { z }$ . One can always find an orthogonal matrix, $T$ , such that $T \mathbf { z } = - \sigma \mathbf { e } _ { 1 }$ where $\sigma$ is a scalar and $\mathbf { e } _ { 1 }$ is a unit vector in the direction of $z _ { 1 }$ , the first component of the column vector $\mathbf { z }$ . The constant $\sigma$ can be determined up to a sign by the fact that $T$ is orthogonal. That is,

$$
\| T \mathbf { z } \| ^ { 2 } = \| - \sigma \mathbf { e } _ { 1 } \| ^ { 2 } = \sigma ^ { 2 } = \| \mathbf { z } \| ^ { 2 } = \mathbf { z } ^ { T } \mathbf { z } .
$$

Therefore,

$$
\boldsymbol { \sigma } = \pm \| \mathbf { z } \| .
$$

To obtain the specific transformation, $T$ , which accomplishes this reduction, the vector, u, must be determined. If we define u as

$$
\mathbf { u } = \mathbf { z } + \sigma \mathbf { e } = { \left[ \begin{array} { l } { z _ { 1 } } \\ { z _ { 2 } } \\ { \vdots } \\ { z _ { n } } \end{array} \right] } + { \left[ \begin{array} { l } { \sigma } \\ { 0 } \\ { \vdots } \\ { 0 _ { n } } \end{array} \right] }
$$

where

$$
\begin{array} { c } { { \mathbf { e } = [ 1 0 0 0 \cdots \cdot 0 ] ^ { T } \mathrm { i s } \mathrm { a n } n \mathrm { v e c t c } } } \\ { { \phantom { e } } } \\ { { \sigma = \mathrm { s i g n } ( z _ { 1 } ) ( \mathbf { z } ^ { T } \mathbf { z } ) ^ { \frac { 1 } { 2 } } \phantom { e } } } \end{array}
$$

then the orthogonal transformation $T = I - \beta \mathbf { u } \mathbf { u } ^ { T }$ is an elementary refle ctor and

$$
T \mathbf { z } = - \sigma \mathbf { e }
$$

where

$$
\beta = \frac { 2 } { { \bf u } ^ { T } { \bf u } } .
$$

Proof: Writing the expression for ${ \boldsymbol { T } } \mathbf { z }$ yields

$$
\begin{array} { r l } & { T \mathbf { z } = \mathbf { z } - \beta \mathbf { u } \mathbf { u } ^ { T } \mathbf { z } } \\ & { \qquad = \mathbf { z } - \beta ( \mathbf { u } ^ { T } \mathbf { z } ) \mathbf { u } } \\ & { \qquad = \mathbf { z } - \beta ( \mathbf { z } ^ { T } \mathbf { z } + \sigma \mathbf { e } ^ { T } \mathbf { z } ) \mathbf { u } } \\ & { \qquad = \mathbf { z } - \beta ( \sigma ^ { 2 } + \sigma \mathbf { e } ^ { T } \mathbf { z } ) \mathbf { u } . } \end{array}
$$

However,

$$
\begin{array} { l } { \displaystyle \beta = \frac { 2 } { \mathbf { u } ^ { T } \mathbf { u } } = 2 / ( \mathbf { z } ^ { T } \mathbf { z } + 2 \sigma \mathbf { e } ^ { T } \mathbf { z } + \sigma ^ { 2 } ) } \\ { \displaystyle = 1 / ( \sigma ^ { 2 } + \sigma \mathbf { e } ^ { T } \mathbf { z } ) } \end{array}
$$

or

$$
\beta = \frac { 1 } { \sigma u _ { 1 } }
$$

where $u _ { 1 }$ is the first element of $\mathbf { u }$ .

Substituting Eq. (5.5.16) into (5.5.15) yields

$$
{ \begin{array} { r } { T \mathbf { z } = \mathbf { z } - \mathbf { u } } \\ { = - \sigma \mathbf { e } . } \end{array} }
$$

From Eq. (5.5.14) and (5.5.17) note that

$$
\mathbf { u } ^ { T } \mathbf { u } = 2 \sigma u _ { 1 } .
$$

Also, from Eq. (5.5.9) we may write

$$
\gamma = \beta \mathbf { z } ^ { T } \mathbf { u }
$$

or

$$
\gamma = \beta \mathbf { u } ^ { T } \mathbf { z } .
$$

For each application of $T$ to a given matrix, we zero out all elements below the main diagonal of the first column. In this operation all elements will be multiplied by $\beta$ . Hence, we want to choose the sign of $\sigma$ to maximize $\lVert u _ { 1 } \rVert$ . Because $u _ { 1 } =$ $z _ { 1 } + \sigma$ , we choose the sign of $\sigma$ to be the same as that of $z _ { 1 }$ , the first element of $\mathbf { z }$ .

In summary, the Householder equations to achieve the desired transformation are

$$
\begin{array} { r l } & { \sigma = \mathrm { s i g n } \ ( z _ { 1 } ) ( \mathbf { z } ^ { T } \mathbf { z } ) ^ { 1 / 2 } } \\ & { z _ { i } ^ { \prime } = - \sigma } \\ & { u _ { 1 } = z _ { 1 } + \sigma } \\ & { u _ { i } = z _ { i } , z _ { i } ^ { \prime } = 0 , i = 2 , . . . \mathrm { n u m b e r ~ o f ~ r o w s } } \\ & { \beta = 1 / ( \sigma u _ { 1 } ) . } \end{array}
$$

The remaining columns also must have $T$ applied. From Eq. (5.5.20)

$$
\gamma _ { j } = \beta \mathbf { u } ^ { T } \mathbf { z } _ { j } , \quad j = 2 , \ldots { \mathrm { n u m b e r ~ o f ~ c o l u m n s } }
$$

where $\gamma _ { j }$ is a scalar and $\mathbf { z } _ { j }$ is the $j ^ { \mathrm { t h } }$ column of the matrix being transformed. The transformed columns, $\mathbf { z } _ { j } ^ { \prime }$ , are computed using Eq. (5.5.9):

$$
\mathbf { z } _ { j } ^ { \prime } = \mathbf { z } _ { j } - \gamma _ { j } \mathbf { u } .
$$

A more detailed algorithm is given in Section 5.5.2.

# 5.5.1 APPLICATION TO THE SOLUTION OF THE LEAST SQUARES PROBLEM

Our goal is to upper triangularize an $( n + m ) \times ( n + 1 )$ matrix using the Householder transformation:

$$
\begin{array} { r l r } { \stackrel { n } {  } 1 } & { { } \stackrel { n } {  } 1 } & { \stackrel { n } {  } 1 } \\ { T _ { n } T _ { n - 1 } \ldots T _ { 1 } } & { { } [ \begin{array} { l l } { \overline { { R } } } & { \overline { { \mathbf { b } } } } \\ { H } & { \mathbf { y } } \end{array} ] \Bigr \} n } & { { } = } & { [ \begin{array} { l l } { R } & { \mathbf { b } } \\ { 0 } & { \mathbf { e } } \end{array} ] \Bigr \} n . } \end{array}
$$

The procedure for accomplishing this is as follows. Let

$$
A \equiv \left[ \begin{array} { l l } { \overline { { R } } } & { \overline { { \mathbf { b } } } } \\ { H } & { \mathbf { y } } \end{array} \right] .
$$

The first transformation $T _ { 1 } A$ will zero all elements of the fir st column except for the first element, which will have the opposite sign of $\overline { { R } } _ { 1 1 }$ and magnitude equal to the Euclidian norm of the first column,

$$
T _ { 1 } A = \hbar - 1 \{ \begin{array} { l l } { \displaystyle \overbrace { - \sigma _ { 1 } | \tilde { a } _ { 1 1 } \tilde { a } _ { 1 2 } \cdots \tilde { a } _ { 1 n } } ^ { 1 } } \\ { \quad 0 } \\ { \quad \vdots } \\ { \quad 0 } \end{array}  \} \{ \begin{array} { l } { \displaystyle { n } } \\ { \displaystyle { \vphantom { \bigg | } } } \\ { \displaystyle { \vphantom { \bigg | } } } \\ { \displaystyle { \vphantom { \bigg | } } } \end{array}  ( 5 . 5 . )  \\  m + n - 1 \{ \begin{array} { l } { \displaystyle \overbrace { [ \begin{array} { l } { \begin{array} { r } { \begin{array} { r } { \begin{array} { r } { \begin{array} { r } { \begin{array} { r } { \end{array} } } \end{array} } \end{array} ] } { \tilde { a } _ { 1 1 } } \cdots \tilde { a } _ { 1 n } } } \\ { \displaystyle { 0 } } \\ { \quad \vdots } \\ { \displaystyle } } \\ { \quad { 0 } \end{array} }  } \end{array}  , \end{array} \end{array}
$$

The next transformation operates on $\widetilde { A } _ { 1 }$ and does not change the first row or column.

This procedure is continued, zeroing elements below the diagonal until the upper $n \times n$ portion of $A$ is upper triangular.

# 5.5.2 HOUSEHOLDER COMPUTATIONAL ALGORITHM

The computational algorithm for applying the Householder transformation is given by Bierman (1977). A few steps have been added here to aid in implementing the algorithm.

Given:

$$
\begin{array} { l l } { \bigcap _ { \mathbf { \lambda } } ^ { n } } & { \bigcap } \\ { \prod _ { \mathbf { \lambda } } ^ { n } } & { \mathbf { \lambda } ^ { \mathbf { \lambda } } } \\ { \prod _ { \mathbf { \lambda } } ^ { n } } & { \mathbf { \lambda } ^ { \mathbf { \lambda } } \mathbf { \tilde { b } } } \\ { H } & { \mathbf { \lambda } ^ { \mathbf { \lambda } } \mathbf { \tilde { y } } } \end{array} \biggr ] \} \ n  &  \equiv [ A ] _ { ( m + n ) \times ( n + 1 ) }
$$

Do $k = 1$ , $n$

$$
\begin{array} { r c l } { { \displaystyle \sigma ~ = ~ \mathrm { s i g n } ( A _ { k k } ) ~ { \Biggl ( } \sum _ { i = k } ^ { m + n } [ A _ { i k } ] ^ { 2 } { \Biggr ) } ^ { 1 / 2 } } } \\ { { \displaystyle u _ { k } ~ = ~ A _ { k k } + \sigma } } \\ { { A _ { k k } ~ = ~ - \sigma } } \\ { { u _ { i } ~ = ~ A _ { i k } ~ i ~ = k + 1 , \ldots , m + n } } \\ { { \beta ~ = ~ { \frac { 1 } { \sigma u _ { k } } } } } \end{array}
$$

Do $j = k + 1 , \dots , n + 1$

$$
\begin{array} { r c l } { { } } & { { } } & { { } } \\ { { \displaystyle \gamma } } & { { = } } & { { \beta \displaystyle \sum _ { i = k } ^ { m + n } u _ { i } A _ { i j } } } \\ { { } } & { { } } & { { } } \\ { { { \cal A } _ { i j } } } & { { = } } & { { { \cal A } _ { i j } - \gamma u _ { i } ~ i = k , \ldots , m + n } } \end{array}
$$

Next $j$

Next $k$

$$
A _ { i k } = 0 \quad i = k + 1 , \ldots , m + n
$$

$$
\mathrm { S u m } = \sum _ { i = 1 } ^ { m } [ A _ { n + i , n + 1 } ] ^ { 2 }
$$

Upon completion, the elements of $A$ represent $R , b$ , and $e$ , respectively:

$$
\overset { n } { \underset { A = \left[ \begin{array} { l l } { R } & { \mathbf { b } } \\ { 0 } & { \mathbf { e } } \end{array} \right] } { \mathrm { \Sigma } } } \mathfrak { j } _ { m }
$$

and

$$
\mathrm { S u m } = \sum _ { i = 1 } ^ { m } e _ { i } ^ { 2 } .
$$

The algorithm can be initialized with $a$ priori $\overline { { R } }$ and $\overline { { \mathbf { b } } }$ . If no $a$ priori is available it can be initialized with $\overline { { R } } = 0 , \overline { { \mathbf { b } } } = 0$ . Alternatively we may define $A$ as

$$
\lim \limits _ { A _ { m \times ( n + 1 ) } } \overbrace { \int \limits _ { \mathrm { ~ } H } \mathrm { ~ } \overbrace { i \mathrm { ~ } \textbf { y } } } ^ { n }
$$

and the operations with index $i$ range to $m$ instead of $m + n$ . In this case the final result is

$$
\begin{array} { r l } { A = } & { { } \left[ \begin{array} { l l } { \overbrace { R } ^ { n } } & { \overbrace { \mathbf { \Gamma } \mathbf { b } } ^ { 1 } } \\ { 0 } & { \mathbf { e } } \end{array} \right] \ m \} ^ { n } } \end{array}
$$

Recall from the discussion on Givens transformation in Section 5.4.1 that

$$
\sum _ { i = 1 } ^ { m } e _ { i } ^ { 2 } = \| \overline { { R } } ( \hat { \bf x } - \overline { { \bf x } } ) \| ^ { 2 } + \sum _ { i = 1 } ^ { m } \hat { \epsilon } _ { i } ^ { 2 }
$$

where

$$
\hat { \epsilon } _ { i } = y _ { i } - H _ { i } \hat { \mathbf { x } } .
$$

If the initialization procedure of Eq. (5.5.31) is used, Eq. (5.5.33) becomes

$$
\sum _ { i = 1 } ^ { m - n } e _ { i } ^ { 2 } = \sum _ { i = 1 } ^ { m } \hat { \epsilon } _ { i } ^ { 2 } .
$$

As with the Givens transformation, the value of $\hat { \bf x }$ is obtained by a backward substitution using Eq. (5.2.8); that is, $R \hat { \mathbf { x } } = \mathbf { b }$ and

$$
\hat { x } _ { i } = \left( b _ { i } - \sum _ { j = i + 1 } ^ { n } R _ { i j } \hat { x } _ { j } \right) \bigg / R _ { i i } \quad i = n , \ldots , 1
$$

and the estimation error covariance is obtained from

$$
\begin{array} { c } { P = \Lambda ^ { - 1 } = ( R ^ { T } R ) ^ { - 1 } } \\ { = R ^ { - 1 } R ^ { - T } } \\ { = S S ^ { T } } \end{array}
$$

where $S$ is obtained from Eq. (5.2.9):

$$
\begin{array} { l } { { \displaystyle i = 1 , \ldots , n } } \\ { { \displaystyle S _ { i i } = \frac { 1 } { R _ { i i } } } } \\ { { \displaystyle S _ { i j } = - S _ { j j } \left[ \sum _ { k = i } ^ { j - 1 } R _ { k j } S _ { i k } \right] ; \quad j = i + 1 , \ldots , n . } } \end{array}
$$

# 5.6 NUMERICAL EXAMPLES

First consider a case with no a priori information. Assume we are given the observation-state matrix, $H$ , and the observation vector, $\mathbf { y }$ , as follows:

$$
\mathbf { y } = H \mathbf { x } + \epsilon
$$

where

$$
\mathbf { y } = { \left[ \begin{array} { l } { - 1 } \\ { 1 } \\ { 2 } \end{array} \right] } , H = { \left[ \begin{array} { l } { 1 - 2 } \\ { 2 - 1 } \\ { 1 } \end{array} \right] } , \mathbf { x } = { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \end{array} \right] } .
$$

Assume that the prewhitening transformation described in Section 5.7.1 has been applied so that $\epsilon \sim ( O , I )$ ; that is, $W = I$ . Use the Cholesky decomposition algorithm and the Givens and Householder transformations to solve for $\hat { \bf x }$ .

# 5.6.1 CHOLESKY DECOMPOSITION

The basic equations are

$$
H ^ { T } H \mathbf { x } = H ^ { T } \mathbf { y } , \qquad M \mathbf { x } = \mathbf { N }
$$

$$
M = H ^ { T } H = { \left[ \begin{array} { l l l } { 1 } & { 2 } & { 1 } \\ { - 2 } & { - 1 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { 1 - 2 } \\ { 2 - 1 } \\ { 1 } & { 1 } \end{array} \right] } = { \left[ \begin{array} { l l } { 6 - 3 } \\ { - 3 } & { 6 } \end{array} \right] }
$$

$$
\mathbf { N } = H ^ { T } \mathbf { y } = \left[ { \ k _ { 1 } \ \mathrm { ~ 2 ~ } \mathbf { \Omega } } 1 \right] \left[ { \ k _ { 1 } \atop \mathrm { ~ 2 } } \right] = \left[ { \ k _ { 3 } \atop \mathrm { ~ 3 } } \right] .
$$

Find $R$ such that

$$
R ^ { T } R = M , \mathrm { w h e r e } \ R \mathrm { i s \ u p p e r \ t r i a n g u l a r \ ( U T }
$$

Using the Cholesky algorithm given by Eq. (5.2.6),

$$
i = 1 , \ldots , n , j = i + 1 , \ldots , n
$$

$$
\begin{array} { l } { { r _ { i i } = \left( M _ { i i } - \displaystyle \sum _ { k = 1 } ^ { i - 1 } r _ { k i } ^ { 2 } \right) ^ { 1 / 2 } } } \\ { { r _ { i j } = \left( M _ { i j } - \displaystyle \sum _ { k = 1 } ^ { i - 1 } r _ { k i } r _ { k j } \right) / r _ { i i } , } } \end{array}
$$

the following results are obtained:

$$
i = 1 , 2 , \mathrm { a n d } j = 2 \ ( \mathrm { f o r  t h i s e x a m p l e } )
$$

$$
r _ { 1 1 } = \sqrt { 6 } , r _ { 1 2 } = - 3 / \sqrt { 6 } , r _ { 2 2 } = 3 / \sqrt { 2 }
$$

$$
R = \left[ \begin{array} { c c c c } { { \sqrt { 6 } - 3 / \sqrt { 6 } } } \\ { { 0 } } & { { 3 / \sqrt { 2 } } } \end{array} \right]
$$

$$
{ \cal R } ^ { T } { \bf z } = { \cal H } ^ { T } { \bf y }
$$

$$
\begin{array} { r } { \left[ { \begin{array} { c c } { \sqrt { 6 } \quad } & { 0 } \\ { - 3 / \sqrt { 6 } \quad } & { 3 / \sqrt { 2 } } \end{array} } \right] \left[ \begin{array} { l } { z _ { 1 } } \\ { z _ { 2 } } \end{array} \right] = \left[ \begin{array} { c } { 3 } \\ { 3 } \end{array} \right] } \end{array}
$$

$$
\mathbf { z } = { \left[ \begin{array} { l } { 3 / { \sqrt { 6 } } } \\ { 3 / { \sqrt { 2 } } } \end{array} \right] }
$$

$$
R \hat { \mathbf x } = \mathbf z
$$

$$
{ \begin{array} { r } { \left[ { \sqrt { 6 } } - 3 / { \sqrt { 6 } } \right] } \\ { 0 \quad 3 / { \sqrt { 2 } } } \end{array} } { \left[ } { \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \end{array} } { \right] } = { \frac { \left[ 3 / { \sqrt { 6 } } \right] } { 3 / { \sqrt { 2 } } } }
$$

$$
{ \hat { \mathbf { x } } } = { \left[ \begin{array} { l } { 1 } \\ { 1 } \end{array} \right] } .
$$

If this were a more complex problem, we would use Eqs. (5.2.7) and (5.2.8) to compute $\mathbf { z }$ and $\hat { \bf x }$ , respectively.

# 5.6.2 GIVENS TRANSFORMATION

For this example,

$$
G [ H : \mathbf { y } ] = { [ \begin{array} { l } { \operatorname { w h e r e } R \equiv 2 \times 2 \ { \mathrm { U T } } , } \\ { \operatorname { \rho } \operatorname { \rho } \phi \equiv 1 \times 2 \ \operatorname { n u l l } \ \operatorname* { m a t r i x } } \\ { \phi \vdots \it { e } ] } { \mathrm { , ~ i t ~ f o l l o w s ~ t h e n ~ t h a t } } \ b \equiv 2 \ \times 1 } \\ { \operatorname { a n d } e \equiv 1 \ \times 1 . } \end{array}  
$$

$G$ is computed directly here using Eq. (5.4.8).

Operating on rows 1 and 2 $( i = 1 , k = 2$ ) yields

$$
\left[ { \begin{array} { c c c } { \cos \theta } & { \sin \theta } & { 0 } \\ { - \sin \theta } & { \cos \theta } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} } \right] \left[ { \begin{array} { c c c } { 1 - 2 \div - 1 } \\ { 2 - 1 \vdots } & { 1 } \\ { 1 } & { 1 \vdots } & { 2 } \end{array} } \right]
$$

$$
h _ { i i } ^ { \prime } = \sqrt { h _ { i i } ^ { 2 } + h _ { k i } ^ { 2 } } , ~ h _ { 1 1 } ^ { \prime } = \sqrt { 1 + 4 } = \sqrt { 5 }
$$

$$
\begin{array} { c } { { \sin \theta = S = h _ { k i } / h _ { i i } ^ { \prime } = 2 / \sqrt { 5 } } } \\ { { \cos \theta = C = h _ { i i } / h _ { i i } ^ { \prime } = 1 / \sqrt { 5 } } } \end{array}
$$

$$
\begin{array} { r l r } & { } & { \left[ \begin{array} { r r r r } { 1 / \sqrt { 5 } } & { 2 / \sqrt { 5 } } & { 0 } \\ { - 2 / \sqrt { 5 } } & { 1 / \sqrt { 5 } } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { r r r r } { 1 } & { - 2 } & { - 1 } \\ { 2 } & { - 1 } & { 1 } \\ { 1 } & { 1 } & { 2 } \end{array} \right] = } \\ & { } & { \left[ \begin{array} { r r r r } { \sqrt { 5 } } & { - 4 / \sqrt { 5 } } & { 1 / \sqrt { 5 } } \\ { 0 } & { 3 / \sqrt { 5 } } & { 3 / \sqrt { 5 } } \\ { 1 } & { 1 } & { 2 } \end{array} \right] . } \end{array}
$$

Operating on rows 1 and 3 $( i = 1 , k = 3$ ) yields

$$
h _ { 1 1 } ^ { \prime } = \sqrt { 6 }
$$

$$
S = h _ { 3 1 } / h _ { 1 1 } ^ { \prime } = 1 / \sqrt { 6 } , C = h _ { 1 1 } / h _ { 1 1 } ^ { \prime } = \sqrt { 5 } / \sqrt { 6 }
$$

$$
{ \begin{array} { r l } & { { \left[ \begin{array} { l l l } { { \sqrt { 5 } } / { \sqrt { 6 } } } & { 0 } & { 1 / { \sqrt { 6 } } } \\ { 0 } & { 1 } & { 0 } \\ { - 1 / { \sqrt { 6 } } } & { 0 } & { { \sqrt { 5 } } / { \sqrt { 6 } } } \end{array} \right] } { \left[ \begin{array} { l l l } { { \sqrt { 5 } } } & { - 4 / { \sqrt { 5 } } } & { 1 / { \sqrt { 5 } } } \\ { 0 } & { 3 / { \sqrt { 5 } } } & { 3 / { \sqrt { 5 } } } \\ { 1 } & { 1 } & { 2 } \end{array} \right] } } \\ & { = { \left[ \begin{array} { l l l } { { \sqrt { 6 } } } & { - 3 / { \sqrt { 6 } } } & { 3 / { \sqrt { 6 } } } \\ { 0 } & { 3 / { \sqrt { 5 } } } & { 3 / { \sqrt { 5 } } } \\ { 0 } & { 9 / { \sqrt { 3 0 } } } & { 9 / { \sqrt { 3 0 } } } \end{array} \right] } . } \end{array} }
$$

The final operation is on rows 2 and 3 $( i = 2 , k = 3 )$ ), which results in

$$
\begin{array} { r c l } { { } } & { { } } & { { h _ { 2 2 } ^ { \prime } = \sqrt { 9 / 5 \ + \ 8 1 / 3 0 } = \sqrt { 1 3 5 / 3 0 } } } \\ { { } } & { { } } & { { S = h _ { 3 2 } / h _ { 2 2 } ^ { \prime } = 9 / \sqrt { 1 3 5 } } } \\ { { } } & { { } } & { { C = h _ { 2 2 } / h _ { 2 2 } ^ { \prime } = 3 \sqrt { 6 } / \sqrt { 1 3 5 } } } \end{array}
$$

$$
\left[ \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { 3 \sqrt { 6 } / \sqrt { 1 3 5 } } & { 9 / \sqrt { 1 3 5 } } \\ { 0 } & { - 9 / \sqrt { 1 3 5 } } & { 3 \sqrt { 6 } / \sqrt { 1 3 5 } } \end{array} \right] \left[ \begin{array} { c c c } { \sqrt { 6 } } & { - 3 / \sqrt { 6 } } & { 3 / \sqrt { 6 } } \\ { 0 } & { 3 / \sqrt { 5 } } & { 3 / \sqrt { 5 } } \\ { 0 } & { 9 / \sqrt { 3 0 } } & { 9 / \sqrt { 3 0 } } \end{array} \right]
$$

$$
= \left[ \begin{array} { c c c c } { { \sqrt { 6 } } } & { { - 3 / \sqrt { 6 } } } & { { \vdots } } & { { 3 / \sqrt { 6 } } } \\ { { 0 } } & { { 3 / \sqrt { 2 } } } & { { \vdots } } & { { 3 / \sqrt { 2 } } } \\ { { 0 } } & { { 0 } } & { { \vdots } } & { { 0 } } \end{array} \right] .
$$

We now have the necessary information to solve for $\hat { \bf x }$ . Using

$$
R \hat { \mathbf x } = \mathbf b
$$

yields

$$
\left[ \begin{array} { c c } { { \sqrt { 6 } } } & { { - 3 / \sqrt { 6 } } } \\ { { 0 } } & { { 3 / \sqrt { 2 } } } \end{array} \right] \left[ \begin{array} { c } { { \hat { x } _ { 1 } } } \\ { { \hat { x } _ { 2 } } } \end{array} \right] = \left[ 3 / \sqrt { 6 } \right] .
$$

Solving for $\hat { \bf x }$ by a backward recursion yields

$$
{ \hat { \mathbf { x } } } = { \left[ \begin{array} { l } { 1 } \\ { 1 } \end{array} \right] } .
$$

The associated covariance matrix is

$$
P = ( H ^ { T } H ) ^ { - 1 } = ( H ^ { T } G ^ { T } G H ) ^ { - 1 } = R ^ { - 1 } R ^ { - T }
$$

$$
\begin{array} { r } { P = \left[ \begin{array} { l l } { 2 / 9 } & { \mathrm { ~ } 1 / 9 } \\ { 1 / 9 } & { \mathrm { ~ } 2 / 9 } \end{array} \right] . } \end{array}
$$

Note that in this example the observation residual, $e$ , has a value of zero. This is because the three observations were perfect, from Eq. (5.5.34):

$$
\hat { \epsilon } = \mathbf { y } - H \hat { \mathbf { x } } = 0 .
$$

# 5.6.3 HOUSEHOLDER TRANSFORMATION

This algorithm is given by Eq. (5.5.29). Because there is no a priori information, we use the initialization procedure of Eq. (5.5.31).

For this example,

$$
[ H : { \bf y } ] = A = \left[ \begin{array} { r c c c } { { 1 } } & { { - 2 } } & { { - 1 } } \\ { { 2 } } & { { - 1 } } & { { 1 } } \\ { { 1 } } & { { 1 } } & { { 2 } } \end{array} \right] .
$$

Each transformation, $T$ , results in

$$
T A = \left[ \begin{array} { r r } { - \sigma } & { \cdots } \\ { \vdots } & { \widetilde { A } } \\ { 0 } & { } \end{array} \right] .
$$

Note that the algorithm given by Eq. (5.5.29) does not use the array, $\widetilde { A }$ . It simply redefines the elements of $A$ , thereby requiring less computer storage. Beginning with

$$
k = 1
$$

$$
\begin{array} { c c } { \sigma = + \sqrt { 1 + 2 ^ { 2 } + 1 } = \sqrt { 6 } } \\ { A _ { 1 1 } = - \sigma = - \sqrt { 6 } } \\ { u _ { 1 } = A _ { 1 1 } + \sigma = 1 + \sqrt { 6 } = 3 . 4 4 9 5 } \\ { u _ { 2 } = A _ { 2 1 } = 2 } \\ { u _ { 3 } = A _ { 3 1 } = 1 } \\ { \beta = \frac { 1 } { \sigma u _ { 1 } } = \frac { 1 } { \sqrt { 6 } + 6 } = 0 . 1 1 8 3 5 } \end{array}
$$

$$
j = 2
$$

$$
\begin{array} { l } { { \displaystyle \gamma = \beta \sum _ { i = 1 } ^ { 3 } u _ { i } A _ { i j } } } \\ { { \displaystyle ~ = 0 . 1 1 8 3 5 \left[ 3 . 4 4 9 5 \left( - 2 \right) ~ + ~ 2 \left( - 1 \right) ~ + ~ 1 \right] } } \\ { { \displaystyle = - 0 . 9 3 4 8 } } \end{array}
$$

$$
j = 3
$$

$$
\gamma = 0 . 1 1 8 3 5 \left[ 3 . 4 4 9 5 ( - 1 ) + 2 + 2 \right]
$$

$$
\begin{array} { c } { { A _ { 1 3 } = - 1 - . 0 6 5 1 5 \left( 3 . 4 4 9 5 \right) } } \\ { { = - 1 . 2 2 4 7 } } \end{array}
$$

$$
\begin{array} { c } { A _ { 2 3 } = 1 - 0 . 0 6 5 1 5 \left( 2 \right. } \\ { \left. = 0 . 8 6 9 7 \right. } \end{array}
$$

$$
\begin{array} { c } { { A _ { 3 3 } = A _ { 3 3 } + \gamma u _ { 3 } } } \\ { { { } } } \\ { { = 2 - 0 . 0 6 5 1 5 } } \\ { { { } } } \\ { { { } = 1 . 9 3 4 8 . } } \end{array}
$$

Hence,

$$
\left[ \begin{array} { l } { \sigma \cdots } \\ { \vdots } \\ { 0 } \end{array} \right] = \left[ \begin{array} { l l l } { - 2 . 4 4 9 5 \vdots 1 . 2 2 4 7 - 1 . 2 2 4 7 } \\ { \ldots \ldots } & { \vdots } \\ { \phantom { - } \ldots \ldots } & { \vdots } \\ { \phantom { - } 0 } & { \vdots } \\ { \phantom { - } 0 } & { \vdots } \end{array} \ldots \ldots \right]
$$

$$
k = 2
$$

$$
\begin{array} { r l } & { \sigma = \sqrt { ( 0 . 8 6 9 7 ) ^ { 2 } + ( 1 . 9 3 4 8 ) ^ { 2 } } } \\ & { \quad = 2 . 1 2 1 2 } \\ & { \widetilde { A } _ { 1 1 } = - 2 . 1 2 1 2 } \\ & { \quad u _ { 2 } = A _ { 2 2 } + \sigma = 0 . 8 6 9 7 + 2 . 1 2 1 2 } \\ & { \quad \quad = 2 . 9 9 1 } \\ & { u _ { 3 } = A _ { 3 2 } = 1 . 9 3 4 8 } \end{array}
$$

$$
\beta = { \frac { 1 } { \sigma u _ { 2 } } } = { \frac { 1 } { ( 2 . 1 2 1 2 ) ( 2 . 9 9 1 ) } } = 0 . 1 5 7 6
$$

$$
j = 3
$$

$$
\begin{array} { r l } { \gamma = \beta [ u _ { 2 } u _ { 3 } ] \left[ \begin{array} { l } { A _ { 2 2 } } \\ { A _ { 3 2 } } \end{array} \right] } & { { } } \\ { = 0 . 1 5 7 6 \left[ 2 . 9 9 1 1 . 9 3 4 8 \right] \left[ \begin{array} { l } { 0 . 8 6 9 7 } \\ { 1 . 9 3 4 8 } \end{array} \right] } & { { } } \end{array}
$$

$$
\gamma = 1
$$

$$
\begin{array} { c } { { \widetilde { A } _ { i j } = A _ { i j } - \gamma u _ { i } , j = 3 , i = 2 , 3 } } \\ { { \widetilde { A } = \left[ { 0 . 8 6 9 7 } \atop { 1 . 9 3 4 8 } \right]}  - \left[ { 2 . 9 9 1 } { \atop { 1 . 9 3 4 8 } } \right] = \left[ { - 2 . 1 2 1 2 } \atop { 0 } \right] }  \end{array}
$$

so that the final result is

$$
T A = \left[ \begin{array} { r r r } { - 2 . 4 4 9 5 } & { { 1 . 2 2 4 7 - 1 . 2 2 4 7 } } \\ { 0 - 2 . 1 2 1 2 - 2 . 1 2 1 2 } \\ { 0 } & { 0 } & { 0 } \end{array} \right]
$$

which agrees with the Givens result except for the sign, which has no effect on $\hat { \bf x }$ or $P$ . Note that, as in the case for the Givens transformation, the observation residual is zero, implying that the observations were perfect.

# 5.6.4 A MORE ILLUSTRATIVE EXAMPLE

For this example we will include a priori information and observation errors. This will illustrate how to initialize the least squares procedure with a priori information using the Cholesky decomposition and orthogonal transformations and

will also demonstrate the feature of computing the sum of squares of the observation residuals.

Assume that we are given observations

$$
\mathbf { y } = H \mathbf { x } + \epsilon
$$

and that we have prewhitened the observation errors so that $\epsilon \sim ( O , I )$ . Values for $\mathbf { y }$ and $H$ are

$$
\mathbf { y } = { \left[ \begin{array} { l } { - 1 . 1 } \\ { 1 . 2 } \\ { 1 . 8 } \end{array} \right] } , \quad H = { \left[ \begin{array} { l } { 1 - 2 } \\ { 2 - 1 } \\ { 1 } \end{array} \right] } ,
$$

with assumed a priori information

$$
\overline { { { \cal P } } } = \left[ \begin{array} { r r } { { 1 0 0 } } & { { 0 } } \\ { { 0 } } & { { 1 0 0 } } \end{array} \right] , \overline { { { \bf x } } } = \left[ \begin{array} { l } { { 2 } } \\ { { 2 } } \end{array} \right] .
$$

Our objective is to determine the best estimate, $\hat { \bf x }$ , of the constant vector $\mathbf { x }$ using the Cholesky decomposition, the Givens square root free, and Householder algorithms. We also wish to find the estimation error covariance matrix and the sum of squares of the observation residuals.

# 5.6.5 CHOLESKY DECOMPOSITION

If the observations are given unit weight, for example, $W = I$ , the normal equations are

$$
( H ^ { T } H + \overline { { P } } ^ { - 1 } ) { \bf x } = H ^ { T } { \bf y } + \overline { { P } } ^ { - 1 } \overline { { { \bf x } } }
$$

or

$$
M \mathbf { x } = \mathbf { N }
$$

where

$$
\begin{array} { l } { { \displaystyle M = H ^ { T } H + \overline { { { \cal P } } } ^ { - 1 } } } \\ { { \displaystyle { \bf N } = H ^ { T } { \bf y } + \overline { { { \cal P } } } ^ { - 1 } \overline { { { \bf x } } } . } } \end{array}
$$

Substituting $H , { \overline { { P } } } , \mathbf { y }$ , and $\overline { { \mathbf { x } } }$ into Eqs. (5.6.13) and (5.6.14) yields

$$
M = \left[ \begin{array} { c c } { { 6 . 0 1 } } & { { \mathrm { ~  ~ \omega ~ } - 3 } } \\ { { \mathrm { ~  ~ \omega ~ } - 3 } } & { { \mathrm { ~  ~ \omega ~ } 6 . 0 1 } } \end{array} \right] , \ : \ : \ : \ : \mathbf { N } = \left[ \begin{array} { c c } { { 3 . 1 2 } } \\ { { 2 . 8 2 } } \end{array} \right] .
$$

Using the Cholesky algorithm given by Eq. (5.2.6) to compute $R$ , where $M =$ $R ^ { T } ~ R$ , yields

$$
\begin{array} { r } { R = \left[ \begin{array} { c c } { 2 . 4 5 2 } & { - 1 . 2 2 4 } \\ { 0 } & { 2 . 1 2 4 } \end{array} \right] . } \end{array}
$$

From Eq. (5.2.4)

$$
R ^ { T } { \bf z } = { \bf N } ,
$$

from Eq. (5.2.7)

$$
\mathbf { z } = { \left[ \begin{array} { l } { 1 . 2 7 3 } \\ { 2 . 0 6 0 9 } \end{array} \right] } ,
$$

and from Eq. (5.2.8)

$$
\hat { \mathbf { x } } = \left[ \begin{array} { c } { 1 . 0 0 3 } \\ { . 9 7 0 } \end{array} \right] .
$$

The covariance of the estimation error is given by Eq. (5.2.5),

$$
P = E ( \hat { \mathbf { x } } - \mathbf { x } ) ( \hat { \mathbf { x } } - \mathbf { x } ) ^ { T } = R ^ { - 1 } R ^ { - T } = S S ^ { T } .
$$

$S$ is given by Eq. (5.2.9)

$$
\begin{array} { r } { S = \left[ \begin{array} { r r } { . 4 0 8 } & { { } . 2 3 5 } \\ { 0 } & { . 4 7 1 } \end{array} \right] . } \end{array}
$$

Hence,

$$
P = \left[ \begin{array} { l l } { { . 2 2 2 } } & { { . 1 1 1 } } \\ { { . 1 1 1 } } & { { . 2 2 2 } } \end{array} \right] .
$$

The sum of squares of the observation errors, including errors in the $a$ priori information, is given by

$$
\begin{array} { l } { { \displaystyle e ^ { 2 } = ( \hat { \mathbf { x } } - \overline { { \mathbf { x } } } ) ^ { T } \overline { { P } } ^ { - 1 } ( \hat { \mathbf { x } } - \overline { { \mathbf { x } } } ) + \sum _ { i = 1 } ^ { 3 } ( y _ { i } - H _ { i } \hat { \mathbf { x } } ) ^ { 2 } } } \\ { { \displaystyle ~ = . 0 2 0 5 + . 0 2 6 6 + . 0 2 6 9 + . 0 2 9 9 } } \\ { { \displaystyle e ^ { 2 } = . 1 0 3 9 . } } \end{array}
$$

# 5.6.6 SQUARE ROOT FREE GIVENS TRANSFORMATION

The initialization procedure for the orthogonal transformation algorithms is described in Section 5.4.1. This involves computing the square root of the a priori

information matrix, $\overline { { R } }$ , and $\overline { { { \bf b } } } = \overline { { R } } \overline { { \bf x } }$ . Recall that $\overline { { \boldsymbol { P } } } = \overline { { \boldsymbol { S } } } \overline { { \boldsymbol { S } } } ^ { T }$ and $\overline { { R } } = \overline { { S } } ^ { - 1 }$ . For this example

$$
\overline { { { R } } } = \left[ \begin{array} { c c } { { 0 . 1 } } & { { 0 } } \\ { { 0 } } & { { 0 . 1 } } \end{array} \right] , \quad \overline { { { \bf b } } } = \left[ \begin{array} { c } { { 0 . 2 } } \\ { { 0 . 2 } } \end{array} \right] .
$$

We will use the square root free Givens rotation given by Eq. (5.4.70). For this we need $\overline { { D } }$ and $\overline { U }$ , where $\overline { { { R } } } = \overline { { { D } } } ^ { \frac { 1 } { 2 } } \overline { { { U } } }$ . Hence,

$$
\begin{array} { r } { \overline { { D } } = \left[ \begin{array} { c c } { . 0 1 } & { 0 } \\ { 0 } & { . 0 1 } \end{array} \right] , \quad \overline { { U } } = \left[ \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] . } \end{array}
$$

The $a$ priori value of $\widetilde { \mathbf { b } }$ is given by

$$
\begin{array} { c } { { \overline { { \widetilde { \mathbf { b } } } } = \overline { { D } } ^ { - \frac { 1 } { 2 } } \overline { { \mathbf { b } } } = \overline { { D } } ^ { - \frac { 1 } { 2 } } \overline { { R } } \overline { { \mathbf { x } } } } } \\ { { = \overline { { U } } \ \overline { { \mathbf { x } } } , } } \end{array}
$$

so

$$
\overline { { \widetilde { { \bf b } } } } = \left[ \begin{array} { l } { 2 } \\ { 2 } \end{array} \right] .
$$

The matrix we wish to compress is

$$
\left[ \begin{array} { l l } { \overline { { U } } } & { \overline { { \tilde { \mathbf { b } } } } } \\ { H } & { \mathbf { y } } \end{array} \right] = \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} 2 \right] .
$$

Recall that Givens algorithm as defined by Eq. (5.4.70) operates on the matrix one row at a time. After processing the first observation we have

$$
D = \left[ \begin{array} { c c } { { \ 1 . 0 1 0 0 } } & { { \ 0 } } \\ { { \ 0 } } & { { \ 0 . 0 4 9 6 } } \end{array} \right] , \quad U = \left[ \begin{array} { c c } { { \ 1 . 0 0 } } & { { \ - 1 . 9 8 0 2 } } \\ { { \ 0 } } & { { \ 1 . 0 0 } } \end{array} \right]
$$

$$
\widetilde { \mathbf { b } } = \left[ \begin{array} { c } { - 1 . 0 6 9 3 } \\ { 1 . 6 4 0 7 } \end{array} \right] , \quad e = 0 . 0 4 0 2 .
$$

Processing the second observation results in

$$
D = \left[ \begin{array} { c c } { { 5 . 0 1 0 0 } } & { { 0 } } \\ { { 0 } } & { { 1 . 8 1 6 4 } } \end{array} \right] , \quad U = \left[ \begin{array} { c c } { { 1 . 0 ~ } } & { { - 0 . 7 9 8 4 } } \\ { { 0 } } & { { 1 . 0 } } \end{array} \right]
$$

$$
\widetilde { \mathbf { b } } = \left[ \begin{array} { l } { 0 . 2 6 3 5 } \\ { 1 . 1 4 1 8 } \end{array} \right] , \quad e = - 0 . 1 1 2 7 .
$$

After processing the third observation,

$$
\begin{array} { r l } { D = \left[ { 6 . 0 1 0 \quad 0 } \atop { 0 \quad 4 . 5 1 2 5 } \right] , U = \left[ { 1 . 0 - 0 . 4 9 9 2 } \atop { 0 \quad 1 . 0 \atop { 1 \cdots 0 } } \right] } & { { } } \\ { \tilde { \mathbf { b } } = \left[ { 0 . 5 1 9 1 } \atop { 0 . 9 7 0 1 } \right] , } & { { } e = - 0 . 2 9 9 4 . } \end{array}
$$

To compare with the Householder results we must multiply by $D ^ { 1 / 2 }$ :

$$
\left[ { \begin{array} { l } { R \mathbf { b } } \\ { 0 \ \mathbf { e } } \end{array} } \right] = \left[ { \begin{array} { c c } { D ^ { \frac { 1 } { 2 } } U } & { D ^ { \frac { 1 } { 2 } } \widetilde { \mathbf { b } } } \\ { 0 } & { \mathbf { e } } \end{array} } \right] \ \} 3
$$

$$
\mathbf { \Sigma } = \left[ \begin{array} { r r r r r } { { 2 . 4 5 1 5 } } & { { - 1 . 2 2 3 7 } } & { { 1 . 2 7 2 7 } } \\ { { 0 } } & { { 2 . 1 2 4 3 } } & { { 2 . 0 6 0 7 } } \\ { { 0 } } & { { 0 } } & { { 0 . 0 4 0 2 } } \\ { { 0 } } & { { 0 } } & { { - 0 . 1 1 2 7 } } \\ { { 0 } } & { { 0 } } & { { - 0 . 2 9 9 4 } } \end{array} \right] .
$$

In actual practice, to conserve computer storage, we would read and process the observations one at a time and store the observations residuals as

$$
e ^ { 2 } = \sum _ { i = 1 } ^ { m } e _ { i } ^ { 2 } .
$$

$\hat { \bf x }$ is computed using Eq. (5.4.49),

$$
U \hat { \mathbf { x } } = \widetilde { \mathbf { b } }
$$

or

$$
\begin{array} { r } { \Big [ 1 . 0 0 - 0 . 4 9 9 2 \Big ] \Big [ \hat { x } _ { 1 } \Big ] = \Big [ 0 . 5 1 9 1 \Big ] } \\ { 0 \qquad 1 . 0 0 \Big ] \Big [ \hat { x } _ { 2 } \Big ] = \Big [ 0 . 9 7 0 1 \Big ] } \end{array}
$$

and

$$
\begin{array} { r } { \Big [ \hat { x } _ { 1 } \Big ] = \Big [ 1 . 0 0 3 4 \Big ] . } \\ { \Big [ \hat { x } _ { 2 } \Big ] } \end{array}
$$

The sum of squares of observation residuals is given by

$$
e ^ { 2 } = \sum _ { i = 1 } ^ { 3 } e _ { i } ^ { 2 } = ( 0 . 0 4 0 2 ) ^ { 2 } + ( - 0 . 1 1 2 7 ) ^ { 2 } + ( - 0 . 2 9 9 4 ) ^ { 2 }
$$

The covariance of the estimation error is given by Eq. (5.4.80), $P = U ^ { - 1 } D ^ { - 1 } U ^ { - T ^ { \prime } }$ Equation (5.2.20) may be used to compute $U ^ { - 1 }$ ,

$$
U ^ { - 1 } = \left[ { \begin{array} { l } { 1 . 0 0 . 4 9 9 2 } \\ { 0 \quad 1 . 0 } \end{array} } \right]
$$

and

$$
{ \begin{array} { r l } & { P = { \left[ \begin{array} { l l } { 1 . 0 } & { 0 . 4 9 9 2 } \\ { 0 } & { 1 . 0 } \end{array} \right] } { \left[ \begin{array} { l l } { . 1 6 6 4 } & { 0 } \\ { 0 } & { . 2 2 1 6 } \end{array} \right] } { \left[ \begin{array} { l l } { 1 . 0 } & { 0 } \\ { 0 . 4 9 9 2 } & { 1 . 0 } \end{array} \right] } } \\ & { \quad = { \left[ \begin{array} { l l } { . 2 2 1 6 } & { . 1 1 0 6 } \\ { . 1 1 0 6 } & { . 2 2 1 6 } \end{array} \right] } . } \end{array} }
$$

Notice that the results for $\hat { \mathbf { x } } , P$ , and $e ^ { 2 }$ agree with the Cholesky results.

# 5.6.7 THE HOUSEHOLDER TRANSFORMATION

The matrix we wish to transform is given by Eq. (5.6.25). In terms of $\overline { { R } }$ and $\overline { { \mathbf { b } } }$ the matrix is given by

$$
\left[ \begin{array} { l l } { { \overline { { R } } } } & { { \overline { { \mathbf { b } } } } } \\ { { \overline { { H } } } } & { { \mathbf { y } } } \end{array} \right] = \left[ \begin{array} { l l l } { 0 . 1 } & { 0 } & { 0 . 2 } \\ { 0 } & { 0 . 1 } & { 0 . 2 } \\ { 1 } & { - 2 } & { - 1 . 1 } \\ { 2 } & { - 1 } & { 1 . 2 } \\ { 1 } & { 1 } & { 1 . 8 } \end{array} \right] .
$$

The Householder transformation algorithm given by Eq. (5.5.29) nulls the elements of each column below the main diagonal. The first transformation yields

The second transformation results in

Several points should be noted:

1. The Householder values of $R$ and $b$ are identical to the Givens results. Hence, the solution for $\hat { \bf x }$ and $P$ will be identical.   
2. Although the individual values of $e _ { i }$ differ, both algorithms yield identical values of $e ^ { 2 } = 0 . 1 0 3 9$ . This also agrees with the Cholesky result.   
3. The Euclidean norm of each column is preserved by an orthogonal transformation.   
4. The square root free Givens algorithm as derived here operates on the matrix row by row, whereas the Householder algorithm transforms column by column. The Givens algorithm can be modifie d to operate column by column (see Section 5.4.2).   
5. The orthogonal transformations do not require the formation of $H ^ { T } H$ . Hence, they will generally be more accurate than Cholesky decomposition.

# 5.7 SQUARE ROOT FILTER ALGORITHMS

Although the sequential estimation algorithms have had wide use in autonomous navigation and control applications, there has been a reluctance to adopt the sequential estimation algorithm for real-time orbit determination mission support.

The primary reason for this reluctance is due to the phenomenon of filter divergence, during which the estimate of the state can depart in an unbounded manner from the true value of the state. There are two fundamental reasons for filt er divergence. The first of these is due to inaccuracies in the mathematical model used to describe the dynamic process or in the model used to relate the observations to the state.

A second factor that can cause filter divergence is associated with the errors that occur in the measurement update of the state error covariance matrix. In particular, this matrix can become nonpositive definite, a situation that is a theoretical impossibility due to the effects of using fini te word length arithmetic to compute the update of the state error covariance matrix at the point where an observation is incorporated. Since this type of divergence is related to errors introduced during the computational procedure, it should be possible to reformulate the computational process to minimize the effects of such errors.

To accomplish this objective, several filter modificat ions, referred to as square root covariance filters, have been proposed in which the state error covariance matrix is replaced by its square root. The state error covariance matrix is obtained by multiplying the square root matrix by its transpose and will always be symmetric and positive semidefinite. Note that the algorithms presented in the remainder of this chapter are designed to accommodate scalar observations.

The motivation for considering the square root measurement update algorithms stems from the loss of significant digits that occurs in computing the measurement update of the state error covariance matrix at the observation epoch (Kaminski et al., 1971) . When the eigenvalues have a wide spread, the error introduced in the computational process can destroy the symmetry and positive definite character of the covariance matrix and filte r divergence may occur. The square root measurement update philosophy, which has been proposed to alleviate this condition, can be expressed as follows.

Define $W$ , the state error covariance matrix square root such that

$$
P = W W ^ { T } .
$$

Note that $P$ , if computed using Eq. (5.7.1), can never be nonpositive definite even in the presence of round-off or truncation errors. Furthermore, since $P$ is symmetric and positive definite, there will exist an orthogonal matrix $M$ such that

$$
P ^ { * } = { M ^ { T } } P M ,
$$

where $P ^ { * }$ is a diagonal matrix whose elements are the eigenvalues of $P$ and $M$ is the corresponding matrix of eigenvectors (Graybill, 1961). Define $W ^ { * }$ as the matrix whose diagonal elements are equal to the square root of the diagonal elements of $P ^ { * }$ :

$$
W _ { i i } ^ { * } = \sqrt { P _ { i i } ^ { * } } i = 1 , . . . , n
$$

where $P _ { i i } ^ { * } > 0$ . Then note that

$$
\begin{array} { r } { W ^ { * } W ^ { * T } = P ^ { * } = M ^ { T } P M = M ^ { T } W W ^ { T } M . } \end{array}
$$

Hence, $W ^ { * } = M ^ { T } W$ and, since $M$ is an orthogonal matrix, it follows that

$$
\begin{array} { r } { W = M W ^ { * } . } \end{array}
$$

If the matrix is symmetrical and positive definit e, there are other methods of computing the square root matrix. For example, see the Cholesky decomposition discussed in Section 5.2.

The numerical conditioning of $W$ is generally much better than that of $P$ . The conditioning number $C ( P )$ of $P$ can be defined as (Lawson and Hanson, 1974)

$$
C ( P ) = \gamma _ { \mathrm { m a x } } / \gamma _ { \mathrm { m i n } } ,
$$

where $\gamma _ { m a x }$ is the maximum eigenvalue of $P$ and $\gamma _ { m i n }$ is the minimum eigenvalue. In base 10 arithmetic with $p$ significant digits, numerical difficul ties with matrix inversion and the precision of $\hat { \bf x }$ may be encountered as $C ( P ) \to 1 0 ^ { p }$ . However, for $W$ ,

$$
C ( W ) = { \sqrt { C ( P ) } } .
$$

Hence, numerical difficulties should not be encountered until

$$
C ( W ) = 1 0 ^ { p }
$$

or

$$
C ( P ) = 1 0 ^ { 2 p } .
$$

# 5.7.1 THE SQUARE ROOT MEASUREMENT UPDATE ALGORITHMS

Using these ideas, the covariance measurement update equation, Eq. (4.7.10), can be expressed in square root form as follows:

$$
P = \overline { { P } } - \overline { { P } } H ^ { T } \left[ H \overline { { P } } H ^ { T } + R \right] ^ { - 1 } H \overline { { P } } .
$$

Now, let $P = W W ^ { T }$ and make this substitution in Eq. (5.7.6) to obtain

$$
W W ^ { T } = \overline { { { W } } } \overline { { { W } } } ^ { T } - \overline { { { W } } } \overline { { { W } } } ^ { T } H ^ { T } \left[ H \overline { { { W } } } \overline { { { W } } } ^ { T } H ^ { T } + R \right] ^ { - 1 } H \overline { { { W } } } \overline { { { W } } } ^ { T } .
$$

Using the following definitions

$$
\widetilde { F } = \overline { { { W } } } ^ { T } H ^ { T } , \alpha = ( \widetilde { F } ^ { T } \widetilde { F } + R ) ^ { - 1 } ,
$$

Eq. (5.7.7) can be expressed as

$$
\boldsymbol { W } \boldsymbol { W } ^ { T } = \overline { { \boldsymbol { W } } } [ \boldsymbol { I } - \widetilde { F } \alpha \widetilde { F } ^ { T } ] \overline { { \boldsymbol { W } } } ^ { T } .
$$

If a matrix $\widetilde { A }$ can be found such that

$$
\tilde { A } \tilde { A } ^ { T } = I - \tilde { F } \alpha \tilde { F } ^ { T } ,
$$

then Eq. (5.7.9) can be expressed as

$$
\boldsymbol { W } \boldsymbol { W } ^ { T } = \overline { { W } } \widetilde { \boldsymbol { A } } \widetilde { \boldsymbol { A } } ^ { T } \overline { { \boldsymbol { W } } } ^ { T } .
$$

Hence,

$$
W = { \overline { { W } } } \widetilde { A } .
$$

The square root measurement update algorithm can be expressed as follows:

$$
\begin{array} { l } { { \widetilde F = \overline { { W } } ^ { T } H ^ { T } } } \\ { { \alpha = ( R + \widetilde F ^ { T } \widetilde F ) ^ { - 1 } } } \\ { { K = \overline { { W } } \widetilde F \alpha } } \\ { { W = \overline { { W } } \widetilde A } } \\ { { \hat { \mathbf { x } } = \overline { { \mathbf { x } } } + K ( \mathbf { y } - H \overline { { \mathbf { x } } } ) } } \end{array}
$$

where $\widetilde { A } = [ I ~ - { \widetilde { F } } \alpha { \widetilde { F } } ^ { T } ] ^ { 1 / 2 }$ . The primary differences in the various algorithms for computing the measurement update in square root form lie in the manner in which the matrix $\widetilde { A }$ is computed. The method first used in practice is that given by Potter (Battin, 1999).

# The Potter Square Root Update

If attention is restricted to processing a single scalar observation, $\alpha$ will be a scalar. For this application, Potter considered the problem of finding the matrix $\widetilde { A }$ such that

$$
\widetilde { A } \widetilde { A } ^ { T } = [ I - \alpha \widetilde { F } \widetilde { F } ^ { T } ] = [ I - \gamma \alpha \widetilde { F } \widetilde { F } ^ { T } ] [ I - \gamma \alpha \widetilde { F } \widetilde { F } ^ { T } ] ^ { T } ,
$$

where $\gamma$ is an unspecified scalar parameter whose value is to be selected to satisfy Eq. (5.7.13). Expanding the right-hand side of Eq. (5.7.13) yields

$$
I - \alpha \widetilde { F } \widetilde { F } ^ { T } = I - 2 \alpha \gamma \widetilde { F } \widetilde { F } ^ { T } + \alpha ^ { 2 } \gamma ^ { 2 } ( \widetilde { F } \widetilde { F } ^ { T } ) ( \widetilde { F } \widetilde { F } ^ { T } ) .
$$

Canceling the identity and factoring $\widetilde { F } \widetilde { F } ^ { T }$ after noting that $\widetilde { F } ^ { T } \widetilde { F }$ is a scalar leads to

$$
( 1 - 2 \gamma + \alpha \gamma ^ { 2 } \widetilde { F } ^ { T } \widetilde { F } ) \alpha \widetilde { F } \widetilde { F } ^ { T } = 0 .
$$

The solution, $\widetilde { F } \widetilde { F } ^ { T } = 0$ , is trivial. Hence, the solution of Eq. (5.7.14) leads to the following condition:

$$
1 - 2 \gamma + \gamma ^ { 2 } \alpha \widetilde { F } ^ { T } \widetilde { F } = 0 .
$$

From Eq. (5.7.15), it follows that $\gamma$ must satisfy the following relation

$$
\gamma = \frac { 2 \pm \sqrt { 4 - 4 \alpha \widetilde { F } ^ { T } \widetilde { F } } } { 2 \alpha \widetilde { F } ^ { T } \widetilde { F } } .
$$

After some algebra, this can be simplified to

$$
\gamma = \frac { 1 } { 1 \pm \sqrt { R \alpha } } ,
$$

where the $^ +$ sign is chosen to ensure that a singular value, $\gamma = \infty$ , does not occur.

Using Eq. (5.7.16) the computational algorithm, based on the sequential estimation algorithm discussed in Chapter 4, can be expressed as follows:

Given $\overline { W }$ , H , R, x and y

Compute:

$$
\begin{array} { r l } & { \widetilde { F } = \overline { { W } } ^ { T } H ^ { T } } \\ & { \alpha = ( \widetilde { F } ^ { T } \widetilde { F } + R ) ^ { - 1 } } \\ & { \gamma = 1 / ( 1 + \sqrt { R \alpha } ) } \\ & { K = \alpha \overline { { W } } \widetilde { F } } \\ & { \widehat { \mathbf { x } } = \overline { { \mathbf { x } } } + K ( \mathbf { y } - H \overline { { \mathbf { x } } } ) } \\ & { W = \overline { { W } } - \gamma K \widetilde { F } ^ { T } . } \end{array}
$$

Note that even if $\overline { W }$ is triangular, the computation involved in Eq. (5.7.17) will result in a nontriangular form for $W$ . Also the computation of Eq. (5.7.17) involves two divisions and a square root that are not involved in the conventional Kalman algorithm. Consequently, Eq. (5.7.17) will be slower than the conventional algorithm; however, it will be more accurate. If $\overline { { P } }$ is given instead of $\overline { W }$ , a Cholesky decomposition may be used to compute $\overline { W }$ in order to initialize the algorithm.

The time update for the state error covariance square root at time $t _ { k }$ for the Potter algorithm follows directly from the time update of the state error covariance. In the general case where there is process noise


<!-- chunk 0006: pages 351-420 -->
$$
\begin{array} { r l } & { \overline { { P } } _ { k } = \Phi ( t _ { k } , t _ { k - 1 } ) W _ { k - 1 } W _ { k - 1 } ^ { T } \Phi ^ { T } ( t _ { k } , t _ { k - 1 } ) } \\ & { ~ + \Gamma ( t _ { k } , t _ { k - 1 } ) V _ { k } V _ { k } ^ { T } \Gamma ^ { T } ( t _ { k } , t _ { k - 1 } ) } \\ & { ~ = \overline { { W } } _ { k } \overline { { W } } _ { k } ^ { T } } \end{array}
$$

where

$$
Q _ { k } = V _ { k } V _ { k } ^ { T } .
$$

A Givens algorithm to compute an upper (or lower) triangular matrix, $\overline { { W } } _ { k }$ , is given in Section 5.8, Eqs. (5.8.6) through (5.8.13). If there is no process noise, set $V _ { k } = 0$ in this algorithm. Methods for maintaining the measurement update in triangular form are discussed next.

# Triangular Square Root Measurement Update

The algorithm for performing the measurement update on the state error covariance matrix square root, $\overline { W }$ , can be expressed as

$$
W = { \overline { { W } } } \widetilde { A } .
$$

If $\overline { W }$ is lower triangular and if $\widetilde { A }$ is lower triangular, then $W$ will be lower triangular, and the computational process expressed in Eq. (5.7.19) will be conducted in a more efficient manner. Choose $\widetilde { A }$ as the solution to

$$
\widetilde { A } \widetilde { A } ^ { T } = [ I - \alpha \widetilde { F } \widetilde { F } ^ { T } ] ,
$$

and require that $\widetilde { A }$ be lower triangular. $\widetilde { A }$ will contain $( n ^ { 2 } + n ) / 2$ unknowns. Since the right-hand side is symmetric, Eq. (5.7.20) contains $( n ^ { 2 } + n ) / 2$ unique equations for the $( n ^ { 2 } + n ) / 2$ unknowns. By analytically expanding the results we can determine the expressions for $\tilde { a } _ { i j }$ , the elements of $\widetilde { A }$ . The procedure used is as follows.

If $\overline { W }$ is lower triangular, the equation

$$
\widetilde { \boldsymbol { F } } = \overline { { \boldsymbol { W } } } ^ { T } \boldsymbol { H } ^ { T }
$$

can be expressed as

$$
\left[ \begin{array} { c } { \widetilde F _ { 1 } } \\ { \vdots } \\ { \widetilde F _ { n } } \end{array} \right] = \left[ \begin{array} { c c c c } { \overline { { W } } _ { 1 1 } } & { \cdots \cdots \cdots \bullet } & { \overline { { W } } _ { n 1 } } \\ { \overline { { W } } _ { 2 2 } \cdots \cdots \cdots \bullet } & { \overline { { W } } _ { n 2 } } \\ { \ddots } & { \vdots } \\ { \cal O } & { \overbrace { W } _ { n n } } \end{array} \right] \left[ \begin{array} { c } { H _ { 1 } } \\ { \vdots } \\ { H _ { n } } \end{array} \right]
$$

$$
= \left[ \begin{array} { l } { \displaystyle { \sum _ { j = 1 } ^ { n } \overline { { W } } _ { j 1 } H _ { j } } } \\ { \quad } \\ { \quad } \\ { \overline { { W } } _ { n n } H _ { n } } \end{array} \right]
$$

or, for the general $i ^ { \mathrm { t h } }$ element,

$$
\widetilde { F } _ { i } = \sum _ { j = i } ^ { n } \overline { { { W } } } _ { j i } H _ { j } , \quad i = 1 , \ldots , n .
$$

From Eq. (5.7.20), the matrix $B$ can be defined as

$$
B = \widetilde { A } \widetilde { A } ^ { T } = I - \alpha \widetilde { F } \widetilde { F } ^ { T } .
$$

The general $i j$ element of the product matrix in Eq. (5.7.23) can be expressed as

$$
B _ { i j } = \sum _ { k = 1 } ^ { j } a _ { i k } a _ { j k } = \delta _ { i j } - \alpha \widetilde { F } _ { i } \widetilde { F } _ { j } , i = 1 , \dots , n ; j = 1 , \dots , i .
$$

From Eq. (5.7.24), it follows that

$$
\begin{array} { r l } & { B _ { 1 1 } = a _ { 1 1 } ^ { 2 } = 1 - ( \tilde { F } _ { 1 } ^ { 2 } \alpha ) } \\ & { B _ { 2 1 } = a _ { 2 1 } a _ { 1 1 } = - ( \tilde { F } _ { 2 } \tilde { F } _ { 1 } \alpha ) } \\ & { B _ { 2 2 } = a _ { 2 1 } ^ { 2 } + a _ { 2 2 } ^ { 2 } = 1 - ( \tilde { F } _ { 2 } ^ { 2 } \alpha ) } \\ & { B _ { 3 1 } = a _ { 3 1 } a _ { 1 1 } = - ( \tilde { F } _ { 3 } \tilde { F } _ { 1 } \alpha ) } \\ & { B _ { 3 2 } = a _ { 3 1 } a _ { 2 1 } + a _ { 3 2 } a _ { 2 2 } = - ( \tilde { F } _ { 3 } \tilde { F } _ { 2 } \alpha ) } \\ & { B _ { 3 3 } = a _ { 3 1 } ^ { 2 } + a _ { 3 2 } ^ { 2 } + a _ { 3 3 } ^ { 2 } = 1 - ( \tilde { F } _ { 3 } ^ { 2 } \alpha ) } \\ & { B _ { 4 1 } = a _ { 4 1 } a _ { 1 1 } = - ( F _ { 4 } F _ { 1 } \alpha ) . } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \end{array}
$$

If the definit ion

$$
\beta _ { i } = \frac { 1 } { \alpha } - \sum _ { j = 1 } ^ { i - 1 } \widetilde { F } _ { j } ^ { 2 } = R + \sum _ { j = i } ^ { n } \widetilde { F } _ { j } ^ { 2 } ,
$$

where

$$
\frac { 1 } { \alpha } = R + \sum _ { j = 1 } ^ { n } \widetilde { F } _ { j } ^ { 2 }
$$

is used, then

$$
\beta _ { i - 1 } = \beta _ { i } + \widetilde { F } _ { i - 1 } ^ { 2 } i = n + 1 , \ldots , 2
$$

where $\beta _ { i }$ satisfies the conditions

$$
\begin{array} { r } { \beta _ { n + 1 } = R , \beta _ { 1 } = \frac { 1 } { \alpha } . } \end{array}
$$

If Eq. (5.7.25) are solved recursively, starting with $a _ { 1 1 }$ , the solution can be expressed as

$$
a _ { i i } = \sqrt { \beta _ { i + 1 } / \beta _ { i } }
$$

$$
a _ { i j } = - \widetilde { F } _ { i } \widetilde { F } _ { j } / \sqrt { \beta _ { j + 1 } \beta _ { j } } \qquad \begin{array} { l l } { i = 1 , \dots , n } \\ { j = 1 , \dots , i - 1 . } \end{array}
$$

Once the elements of $\widetilde { A }$ have been computed, the elements of Eq. (5.7.19) can be expressed as follows:

$$
W _ { i j } = \sum _ { k = j } ^ { i } \overline { { { W } } } _ { i k } a _ { k j } \begin{array} { l } { i = 1 , \ldots , n } \\ { j = 1 , \ldots , i . } \end{array}
$$

The algorithm for the state estimate with a lower triangular square root covariance update is:

Given: $\overline { { W } } , H , R , \overline { { \mathbf { x } } }$ , and $y$ , where $\overline { W }$ is lower triangular Compute:

$$
\begin{array} { l } { { \displaystyle { 1 . \widetilde { F } _ { i } = \sum _ { j = 1 } ^ { n } \overline { { { W } } } _ { j i } H _ { j } } \qquad i = 1 , \ldots , n } } \\ { { \mathrm { } } } \\ { { \displaystyle { 2 . \beta _ { n + 1 } = R } } } \\ { { \beta _ { j } = \beta _ { j + 1 } + \widetilde { F } _ { j } ^ { 2 } \qquad j = n , \ldots , 1 } } \\ { { \beta _ { 1 } = 1 / \tilde { \alpha } } } \end{array}
$$

$$
\begin{array} { c c } { { 3 . d _ { i } = 1 / \sqrt { \beta _ { i + 1 } \beta _ { i } } \qquad } } & { { i = 1 , \ldots , n } } \\ { { a _ { i i } = \beta _ { i + 1 } d _ { i } \qquad } } & { { } } \\ { { a _ { i j } = - \widetilde { F } _ { i } \widetilde { F } _ { j } d _ { j } \qquad } } & { { j = 1 , \ldots , i - 1 } } \end{array}
$$

$$
4 . W _ { i j } = \sum _ { k = j } ^ { i } { \overline { { W } } } _ { i k } a _ { k j } \qquad i = 1 , \dots , n
$$

$$
5 . K _ { i } = \alpha ( \sum _ { j = 1 } ^ { i } \overline { { { W } } } _ { i j } \widetilde { F } _ { j } ) i = 1 , \ldots , n
$$

$$
6 . { \hat { \mathbf { x } } } _ { i } = { \overline { { \mathbf { x } } } } + K ( y - H { \overline { { \mathbf { x } } } } ) .
$$

If $\mathbf { y }$ is a vector of observations, this procedure must be repeated for each element of $\mathbf { y }$ .

The previous algorithm yields a lower triangular square root factorization of the measurement update error covariance matrix. An upper triangularization also can be used. The algorithm for this was developed by Carlson (1973). The version presented here is due to Bierman (1977) and is a slightly modified version of Carlson’s algorithm to enhance accuracy.

Given: $\overline { W }$ , $H , R , { \overline { { \mathbf { x } } } }$ , and $y$ , where $\overline { W }$ is upper triangular

Compute:

$$
\begin{array} { r l } & { 1 . \widetilde { F } = \overline { { W } } ^ { T } H ^ { T } } \\ & { \beta _ { o } = R , K _ { 2 } ^ { T } = \left[ \overline { { W } } _ { 1 1 } \widetilde { F } _ { 1 } , \overbrace { 0 , 0 , . . . 0 } ^ { n - 1 } \right] } \end{array}
$$

$$
\begin{array} { r l } & { 2 . \beta _ { j } = \beta _ { j - 1 } + \widetilde { F } _ { j } ^ { 2 } } \\ & { 3 . d _ { j } = ( \beta _ { j - 1 } / \beta _ { j } ) ^ { 1 / 2 } } \\ & { 4 . \gamma _ { j } = \widetilde { F } _ { j } / ( \beta _ { j } d _ { j } ) } \\ & { 5 . W _ { j j } = \overline { { W } } _ { j j } d _ { j } } \\ & { 6 . W _ { i j } = \overline { { W } } _ { i j } d _ { j } - \gamma _ { j } K _ { j } ( i ) } \\ & { 7 . K _ { j + 1 } ( i ) = K _ { j } ( i ) + \widetilde { F } _ { j } \widetilde { W } _ { i j } } \\ & { 8 . K = K _ { n + 1 } / \beta _ { n } } \\ & { 9 . \tilde { \kappa } = \overline { { \mathbf { X } } } + K ( y - H \mathbf { X } ) . } \end{array}
$$

$$
\begin{array} { l } { i = 1 , \dots j - 1 } \\ { \qquad } \\ { i = 1 , \dots j } \end{array}
$$

Although at first glance it does not seem to matter whether one uses an upper or lower triangular form for $W$ , Carlson (1973) points out that the time update for the upper triangular form is computationally more efficient. This can be seen by partitioning the state vector such that

$$
\begin{array} { r } { \mathbf { x } = \left[ \begin{array} { l } { \mathbf { x } _ { 1 } } \\ { \mathbf { x } _ { 2 } } \end{array} \right] , } \end{array}
$$

where $\mathbf { x } _ { 1 }$ contains the dynamical parameters such as position and velocity and $\mathbf { x } _ { 2 }$ contains constants such as gravity coefficients or time-varying quantities such as gas leaks that affect the elements of $\mathbf { x } _ { 1 }$ but are not affected by $\mathbf { x } _ { 1 }$ . Hence, the state transition matrix for $\mathbf { x }$ can be partitioned as

$$
\Phi = \left[ { \Phi _ { 1 1 } } \Phi _ { 1 2 } \right] ,
$$

where $\Phi _ { 1 1 }$ is a dense matrix, $\Phi _ { 1 2 }$ may contain some zeros, and $\Phi _ { 2 2 }$ is typically diagonal. When performing the time update, if $W$ is upper triangular, only the upper left partition of the product $\overline { { W } } = \Phi W$ becomes nontriangular and requires retriangularization.

Recall that these algorithms are designed to process the observations (acutally observation deviations) as scalars. Hence, if $\mathbf { y }$ is a vector the elements of $\mathbf { y }$ must be processed one at a time. We assume that the observations are uncorrelated so that $R$ is a diagonal matrix.

If $R$ is not a diagonal matrix, that is, the observation errors are correlated, we can perform a whitening and decorrelation transformation given by Bierman (1977), and described next.

Given a set of observations

$$
\mathbf { y } - H \mathbf { x } = { \boldsymbol { \epsilon } } ,
$$

where

$$
\begin{array} { r } { E [ \epsilon ] = 0 } \\ { E [ \epsilon \epsilon ^ { T } ] = R } \end{array}
$$

and $R$ is not diagonal but is positive definit e. Compute the triangular square root of $R$

$$
R = V V ^ { T } .
$$

The Cholesky algorithm may be used to ensure that $V$ is triangular. Next multiply Eq. (5.7.34) by $V ^ { - 1 }$

$$
V ^ { - 1 } \mathbf { y } = V ^ { - 1 } H \mathbf { x } + V ^ { - 1 } \boldsymbol \epsilon
$$

let

$$
\tilde { \mathbf { y } } = V ^ { - 1 } \mathbf { y } , \tilde { H } = V ^ { - 1 } H , \tilde { \epsilon } = V ^ { - 1 } \epsilon
$$

then

$$
\tilde { \mathbf { y } } = \widetilde { H } x + \tilde { \mathbf { \epsilon } }
$$

It is easily shown that $\widetilde { \epsilon }$ has zero mean and unit variance,

$$
\begin{array} { r } { \boldsymbol { E } [ \tilde { \epsilon } ] = V ^ { - 1 } \boldsymbol { E } [ \epsilon ] = 0 \qquad } \\ { E [ \tilde { \epsilon } \tilde { \epsilon } ^ { T } ] = V ^ { - 1 } \boldsymbol { E } [ \epsilon \epsilon ^ { T } ] V ^ { - T } = V ^ { - 1 } R V ^ { - T } = I } \end{array}
$$

Hence, we would process the observations, $\tilde { \mathbf { y } }$ , instead of $\mathbf { y }$ .

# 5.7.2 SQUARE ROOT FREE MEASUREMENT UPDATE ALGORITHMS

The square root operations in the Potter and Triangular algorithms shown earlier lead to increased computational load. Square root free equivalents of these algorithms can be used to obtain enhanced computational performance. A comprehensive discussion of these square root free algorithms is given by Thornton (1976) and Bierman (1977).

A square root free algorithm, known as the $U \mathcal { D }$ covariance factorization, developed by Bierman and Thornton is described next. Let

$$
{ \cal P } = U { \cal D } U ^ { T }
$$

where $U$ is unit upper triangular and $D$ is diagonal. Substituting Eq. (5.7.39) into the expression for the covariance matrix update

$$
P = [ I - K H ] \overline { { P } }
$$

and restricting attention to the scalar observation case leads to the following expression:

$$
U D U ^ { T } = \overline { { { U } } } \overline { { { D } } } \overline { { { U } } } ^ { T } ~ - \overline { { { U } } } \overline { { { D } } } \overline { { { U } } } ^ { T } H ^ { T } \alpha H \overline { { { U } } } \overline { { { D } } } \overline { { { U } } } ^ { T }
$$

where

$$
\alpha = ( H \overline { { { P } } } H ^ { T } + R ) ^ { - 1 } = \big ( H \overline { { { U } } } \overline { { { D } } } \overline { { { U } } } ^ { T } H ^ { T } + R \big ) ^ { - 1 } .
$$

Now, by factoring, Eq. (5.7.41) can be expressed as follows:

$$
\boldsymbol { U } \boldsymbol { D } \boldsymbol { U } ^ { T } = \overline { { \boldsymbol { U } } } \left[ \overline { { \boldsymbol { D } } } - \overline { { \boldsymbol { D } } } \overline { { \boldsymbol { U } } } ^ { T } \boldsymbol { H } ^ { T } \alpha \boldsymbol { H } \overline { { \boldsymbol { U } } } \overline { { \boldsymbol { D } } } \right] \overline { { \boldsymbol { U } } } ^ { T } .
$$

Let

$$
\boldsymbol { F } = \overline { { \boldsymbol { U } } } ^ { T } \boldsymbol { H } ^ { T } , \boldsymbol { V } = \overline { { \boldsymbol { D } } } \boldsymbol { F } ,
$$

then Eq. (5.7.43) can be expressed as

$$
P = U D U ^ { T } = \overline { { U } } \left[ \overline { { D } } - V \alpha V ^ { T } \right] \overline { { U } } ^ { T } ,
$$

where

$$
\overline { { { U } } } = \left[ \begin{array} { c c c c c c } { { 1 \overline { { { U } } } _ { 1 2 } \cdots } } & { { \overline { { { U } } } _ { 1 n } } } \\ { { } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { \ddots } } \\ { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { 1 } } \end{array} \right] ; \overline { { { D } } } = \left[ \begin{array} { c c c c c c c } { { \overline { { { d } } } _ { 1 } } } & { { 0 } } & { { } } \\ { { \overline { { { d } } } _ { 2 } } } & { { } } \\ { { } } & { { \ddots } } \\ { { } } & { { } } & { { \overline { { { d } } } _ { n } } } \end{array} \right] .
$$

$$
\boldsymbol { F } = \left[ \begin{array} { l } { \overline { { d } } _ { 1 } F _ { 1 } } \\ { \vdots } \\ { F _ { n } } \end{array} \right] = \overline { { \boldsymbol { U } } } ^ { T } \boldsymbol { H } ^ { T } ; \boldsymbol { V } = \overline { { D } } \boldsymbol { F } = \left[ \begin{array} { l } { \overline { { d } } _ { 1 } F _ { 1 } } \\ { \overline { { d } } _ { 2 } F _ { 2 } } \\ { \vdots } \\ { \overline { { d } } _ { n } F _ { n } } \end{array} \right] .
$$

Now let $\widetilde { U }$ and $\widetilde { D }$ be the factors of $[ \overline { { D } } - V \alpha V ^ { T } ]$ . Then Eq. (5.7.45) can be written as

$$
U D U ^ { T } = \overline { { { U } } } \widetilde { U } \widetilde { D } \widetilde { U } ^ { T } \overline { { { U } } } ^ { T } .
$$

Since $\overline { U }$ and $\widetilde { U }$ are upper triangular, their product will be upper triangular, and can be expressed as

$$
\begin{array} { l } { { U = \overline { { U } } \widetilde { U } } } \\ { { D = \widetilde { D } . } } \end{array}
$$

Hence, the problem of factoring the covariance measurement update for $P$ has been reduced to factoring the symmetric matrix $[ \overline { { \cal D } } - V \alpha V ^ { T } ]$ into $\widetilde { U }$ and $\widetilde { D }$ . This can be done using the square root free Cholesky decomposition or using the more computationally efficient algorithm presented in Thornton (1976) or Bierman (1977). This algorithm together with an example also appears in Maybeck (1979).

The computational algorithm for the measurement update of $P$ can be summarized then as follows:

Given: $\overline { { U } } , \overline { { D } } , H , R , \overline { { \mathbf { x } } }$ , and $y$

Compute:

1. $F = \overline { { U } } ^ { T } H ^ { T }$   
2. $V _ { i } = \overline { { d } } _ { i } F _ { i }$ , $i = 1 , \ldots , n$   
3. $\alpha _ { 1 } = \left( R + V _ { 1 } F _ { 1 } \right)$ d = d1R b1 = V1   
4. $\alpha _ { j } = \alpha _ { j - 1 } + F _ { j } V _ { j }$ $\left\{ { \begin{array} { l } { \qquad } \\ { j = 2 , \ldots , n } \\ { \qquad } \\ { \qquad \left. \right.} \\ { \qquad j = 2 , \ldots , n } \\ { \qquad } \\ { i = 1 , \ldots , j - } \end{array} }  \right.$ dj = dj αj−1 / αj bj = Vj pj = −Fj / αj−1   
5. $U _ { i j } = \overline { { U } } _ { i j } + b _ { i } p _ { j }$ bi = bi + U ij Vj 1   
6. K = b / αn   
$7 . { \hat { \mathbf { x } } } = { \overline { { \mathbf { x } } } } + K ( y - H { \overline { { \mathbf { x } } } } ) .$

Note that $\mathbf { b }$ is an $n$ vector, $[ b _ { 1 } , b _ { 2 } \dots b _ { n } ] ^ { T }$ . If the estimation error covariance matrix is needed, it may be calculated by using Eq. (5.7.39).

Thus far, with the exception of the Potter Algorithm, we have not addressed the time update of the estimation error covariance matrix. This will be addressed in Sections 5.8 and 5.9.

# 5.8 TIME UPDATE OF THE ESTIMATION ERROR COVARIANCE MATRIX

Section 5.7 deals primarily with the measurement update of the estimation error covariance matrix, $P$ . Various discrete algorithms have been developed for the time update. The most obvious approach for the time update would be to map $W W ^ { T }$ or $U D U ^ { T }$ using the conventional measurement update equation given in Chapter 4, for $W _ { k }$ and $V _ { k }$ ,

$$
\begin{array} { r l } & { \overline { { P } } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) P _ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) + \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) } \\ & { \qquad = \Phi ( t _ { k + 1 } , t _ { k } ) W _ { k } W _ { k } ^ { T } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) } \\ & { \qquad + \Gamma ( t _ { k + 1 } , t _ { k } ) V _ { k } V _ { k } ^ { T } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) } \end{array}
$$

where

$$
Q _ { k } = V _ { k } V _ { k } ^ { T } .
$$

$\overline { { P } } _ { k + 1 }$ may then be triangularized using a Cholesky transformation. After this, the measurement update is applied to process the next vector of observations.

Although this approach is computationally efficient, it is not as accurate as an orthogonal transformation approach that does not require the formation of the covariance matrix with the attendant numerical problems. A more accurate approach would be to find a propagation equation for the square root of $\overline { { P } }$ . This can be accomplished by noting that the right-hand side of Eq. (5.8.1) may be written as

$$
\overline { { P } } _ { k + 1 } = B _ { k + 1 } B _ { k + 1 } ^ { T }
$$

where

$$
B _ { k + 1 } = \left[ \Phi ( t _ { k + 1 } , t _ { k } ) W _ { k } \colon \Gamma ( t _ { k + 1 } , t _ { k } ) V _ { k } \right] .
$$

Note, however, that $B _ { k + 1 }$ would not be a square matrix but would be of dimension $n \times ( n { + } m )$ , where $n$ is the dimension of the state vector and $m$ is the dimension of the process noise vector. Various methods for converting Eq. (5.8.3) into an $n \times n$ triangular matrix are described by Bierman (1977), Thornton (1976), Maybeck (1979), Dyer and McReynolds (1969), and Kaminski (1971). The key to the triangularization of Eq. (5.8.3) is to note that an $( n + m ) \times ( n + m )$ orthogonal transformation, $T$ , can be applied to Eq. (5.8.2) so that (recall that $T T ^ { T } = I$ )

$$
B _ { k + 1 } T T ^ { T } B _ { k + 1 } ^ { T } = \tilde { W } _ { k + 1 } \tilde { W } _ { k + 1 } ^ { T }
$$

where

$$
\tilde { W } _ { k + 1 } = B _ { k + 1 } T = \left[ \phi : \overline { { W } } _ { k + 1 } \right]
$$

and where $\overline { { W } } _ { k + 1 }$ is now an $n \times n$ upper triangular matrix and $\phi$ is an $n \times m$ null matrix. Various methods that may be used to accomplish the triangularization are the Gram-Schmidt orthogonalization (Bierman, 1977), the Householder transformation, or the Givens transformation (Thornton, 1976).

The following Givens square root factorization algorithm is taken from Thornton (1976), and yields an $n \times n$ upper triangularization for $\overline { W }$ and an $n \times m$ null matrix, $\phi$ .

Let $B$ be a full rank $n \times ( n { + } m )$ matrix with column vectors $B _ { i }$ , $i = 1 \ldots , n +$ $m$ . The following algorithm yields an $n \times n$ upper triangular factor $\overline { W }$ such that $\overline { { W } } \ : \overline { { W } } ^ { T } = B B ^ { T }$ . For $j = n , \ldots , 1$ , cycle through Eqs. (5.8.6) through (5.8.12).

$$
k = m + j .
$$

For $i = k - 1 , \ldots 1$ evaluate recursively Eqs. (5.8.7) through (5.8.12).

$$
\begin{array} { c } { { B _ { k } ^ { \prime } ( j ) = \sqrt { ( B _ { i } ( j ) ) ^ { 2 } + ( B _ { k } ( j ) ) ^ { 2 } } } } \\ { { { } } } \\ { { C = B _ { k } ( j ) / B _ { k } ^ { \prime } ( j ) } } \\ { { S = B _ { i } ( j ) / B _ { k } ^ { \prime } ( j ) } } \\ { { { } } } \\ { { { \cal V } = B _ { i } } } \\ { { B _ { i } = C B _ { i } - S B _ { k } } } \\ { { B _ { k } = S V + C B _ { k } . } } \end{array}
$$

When completed this algorithm yields

$$
\begin{array} { c } { { \stackrel { m } { \longleftrightarrow } } } \\ { { B = \ \left[ \phi \ \stackrel { : } { : } \ \stackrel { n } { W } \ \right] \ \} n } } \end{array}
$$

where $\overline { W }$ is upper triangular.

As pointed out by Thornton (1976), a lower triangular factor $\overline { W }$ may be obtained from Eqs (5.8.6) through (5.8.12) if the indicies $i$ and $j$ are reordered so that $j = 1 , \dotsc , n$ and $i = j + 1 , \ldots , k$ . At the conclusion of this algorithm $B$ has the form

$$
\begin{array} { c } { { \stackrel { n } { \longleftrightarrow } } } \\ { { B = \ \left[ \overline { { { W } } } \ \stackrel { . } { : } \ \stackrel { m } { \phi } \ \right] \ \} n } } \end{array}
$$

where $\overline { W }$ is lower triangular.

The previous algorithms yield $\overline { W }$ as either upper or lower triangular. For the $U - D$ factorization we need $\overline { U }$ and $\overline { { D } }$ in order to perform the time update for $P$ ,

$$
\overline { { P } } = \overline { { U } } \overline { { D } } \overline { { U } } ^ { T }
$$

The following algorithm employs a generalized Gram-Schmidt orthogonalization to preserve numerical accuracy and was developed by Thornton and Bierman (1975), and it also appears in Maybeck (1979). The measurement update for $P$ at the $k ^ { \mathrm { t h } }$ stage is given by

$$
P _ { k } = U _ { k } D _ { k } U _ { k } ^ { T } .
$$

Let

$$
\begin{array} { l } { { Y _ { k + 1 } = [ \Phi ( t _ { k + 1 } , t _ { k } ) U _ { k } : \Gamma ( t _ { k + 1 } , t _ { k } ) ] } } \\ { { \widetilde D _ { k + 1 } = \left[ \begin{array} { l l } { { D _ { k } } } & { { 0 } } \\ { { 0 } } & { { Q _ { k } } } \end{array} \right] . } } \end{array}
$$

Then it can be seen that $Y _ { k + 1 } \widetilde { D } _ { k + 1 } Y _ { k + 1 } ^ { T }$ satisfies Eq. (5.8.1). We may now apply the following algorithm to obtain $\overline { U }$ and $\overline { { D } }$ , the time updated values of $U$ and $D$ . Let

$$
Y _ { k + 1 } ^ { T } = [ \mathbf { \_ { a } } _ { 1 } : \mathbf { a } _ { 2 } : \dots : \mathbf { a } _ { n } ]
$$

Where each vector ${ \bf a } _ { i }$ is of dimension $n + m$ . Again $n$ is the dimension of the state vector and $m$ is the dimension of the process noise vector.

$$
\begin{array} { l } { { \mathrm { F o r } \ell = n , n - 1 , \ldots , 1 : } } \\ { { \ } } \\ { { { \bf C } _ { \ell } = \widetilde D { \bf a } _ { \ell } \quad \mathrm { ( i . e . , } C _ { \ell j } = \widetilde D _ { j j } a _ { \ell j } , j = 1 , 2 , \ldots , n + m ) } } \\ { { \ } } \\ { { \overline { { { D } } } _ { \ell \ell } = { \bf a } _ { \ell } ^ { T } { \bf C } _ { \ell } \quad \quad \quad } } \\ { { \ } } \\ { { { \bf \overline { { U } } } _ { j \ell } = { \bf a } _ { j } / D _ { \ell \ell } \quad \quad \quad } } \\ { { \ } } \\ { { { \bf a } _ { j }  { \bf a } _ { j } - { \bf \overline { { U } } } _ { j \ell } { \bf a } _ { \ell } \quad \quad \quad } } \end{array}
$$

where $\longleftarrow$ denotes replacement; that is, write over the old variable to reduce storage requirements. For the final iteration, $\ell = 1$ and only $\mathbf { C } _ { 1 }$ and $D _ { 1 1 }$ are computed.

# 5.9 CONTINUOUS STATE ERROR COVARIANCE PROPAGATION

In this section a method that allows the integration of the continuous state error covariance differential equations in square root form is described. The derivation follows the approach used in Tapley and Choe (1976) and Tapley and Peters (1980), but the results are based on the $P \equiv U D U ^ { T }$ decomposition. This algorithm can be combined with a triangular measurement update algorithm to obtain a complete square root estimation algorithm for which square root operations are avoided. In addition, the effects of state process noise are included without approximation.

The differential equation for propagation of the state error covariance matrix can be expressed as

$$
{ \dot { \overline { { P } } } } ( t ) = A ( t ) { \overline { { P } } } ( t ) + { \overline { { P } } } ( t ) A ^ { T } ( t ) + Q ( t ) ,
$$

where $\overline { { P } } ( t )$ is the $a$ priori state error covariance matrix, $A ( t )$ is the $n \times n$ linearized dynamics matrix, and $Q ( t )$ is the process noise covariance matrix. Each of the matrices in Eq. (5.9.1) is time dependent in the general case. However, for simplicity, the time dependence will not be noted specifically in the following discussion.

If the following definitions are used,

$$
\overline { { { P } } } \equiv \overline { { { U } } } \overline { { { D } } } \overline { { { U } } } ^ { T } , \overline { { { Q } } } \equiv Q / 2 \ ,
$$

and if the first part of Eq. (5.9.2) is differentiated with respect to time and substituted into Eq. (5.9.1), the results can be rearranged to form

$$
\begin{array} { r l } & { ( \dot { \overline { { U } } } \overline { { D } } + \overline { { U } } \dot { \overline { { D } } } / 2 - \overline { { Q } } \overline { { U } } ^ { - T } - A \overline { { U } } \overline { { D } } ) \overline { { U } } ^ { T } } \\ & { + \overline { { U } } ( \overline { { D } } \dot { \overline { { U } } } ^ { T } + \dot { \overline { { D } } } \overline { { U } } ^ { T } / 2 - \overline { { U } } ^ { - 1 } \overline { { Q } } ^ { T } - \overline { { D } } \overline { { U } } ^ { T } A ^ { T } ) = 0 . } \end{array}
$$

Noting that the first term of Eq. (5.9.3) is the transpose of the second term, and making the following definition

$$
{ \cal C } ( t ) \equiv ( \dot { \overline { { U } } } \overline { { { D } } } + \overline { { { U } } } \dot { \overline { { { D } } } } / 2 - \overline { { { Q } } } \overline { { { U } } } ^ { - T } - A \overline { { { U } } } \overline { { { D } } } ) \overline { { { U } } } ^ { T }
$$

one obtains

$$
C ( t ) + C ^ { T } ( t ) = 0 .
$$

Relation (5.9.5) requires that $C ( t )$ be either the null matrix or, more generally, skew symmetric.

Equation (5.9.4) can be simplified by selectively carrying out the multiplication of the $- Q \overline { { U } } ^ { - T }$ term by $\overline { { U } } ^ { \bar { T } }$ to yield, after terms are arranged

$$
( \dot { \overline { { U } } } \overline { { D } } + \overline { { U } } \dot { \overline { { D } } } / 2 - A \overline { { U } } \overline { { D } } ) \overline { { U } } ^ { T } = \overline { { Q } } + C ( t ) \equiv \tilde { C } ( t ) .
$$

Equation (5.9.6) defines the differential equations for $\overline { U }$ and $\overline { { D } }$ to the degree of uncertainty in $C ( t )$ . Since the unknown matrix $C ( t )$ is skew symmetric, there exist $n ( n { - } 1 ) / 2$ unknown scalar quantities in Eq. (5.9.6). The problem considered here is one of specifying the elements of $C ( t )$ so that $\overline { U }$ is maintained in triangular form during the integration of Eq. (5.9.6). (The derivation pursued here assumes that $\overline { U }$ is lower triangular and $\overline { { D } }$ is diagonal, although an algorithm for an upper triangular $\overline { U }$ can be obtained as easily.) The following definiti ons are made to facilitate the solution to the problem posed:

$$
T \equiv A \overline { { { U } } } \overline { { { D } } } \quad M \equiv \dot { \overline { { { U } } } } \overline { { { D } } } + \overline { { { U } } } \dot { \overline { { { D } } } } / 2 - T .
$$

With these definitions, Eq. (5.9.6) is expressed as

$$
\boldsymbol { M } \boldsymbol { \overline { { U } } } ^ { T } = \boldsymbol { \widetilde { C } } ( t ) = \boldsymbol { \overline { { Q } } } + \boldsymbol { C } ( t ) \mathrm { ~ . ~ }
$$

Since $\overline { U }$ and $\dot { \overline { { U } } }$ in Eq. (5.9.6) are lower triangular, and since from Eq. (5.9.5) $C ( t )$ is skew symmetric, several observations can be made regarding Eq. (5.9.8). There are $n ( n - 1 ) / 2$ unknown elements in $\tilde { C }$ . The products $\dot { \overline { { U } } } \overline { { D } }$ and $\overline { { U } } \dot { \overline { { D } } }$ are lower triangular, creating $n ( n + 1 ) / 2$ unknowns. Therefore, the $n \times n$ system of equations in Eq. (5.9.8) has $\left[ n ( n - 1 ) / 2 + n ( n + 1 ) / 2 \right] = n \times n$ unknowns that can be determined uniquely.

An expansion of Eq. (5.9.8) into matrix elements indicates the method of solution

$$
\begin{array} { r l r } & { } & { \left[ { \cal M } _ { 1 1 } - { \cal T } _ { 1 2 } \cdot \cdot \cdot - { \cal T } _ { 1 n } \right] \left[ \begin{array} { l } { 1 \overline { { { \cal U } } } _ { 2 1 } \cdot \cdot \cdot \cdot \overline { { { \cal U } } } _ { n 1 } } \\ { M _ { 2 1 } \ M _ { 2 2 } \ \cdot \cdot \cdot \cdot - { \cal T } _ { 2 n } } \\ { \vdots \ \cdot \ 1 \ \cdot \ \cdot \cdot \overline { { { \cal U } } } _ { n 2 } } \\ { \vdots \ \vdots \ \cdot \ \ddots \ \vdots } \\ { M _ { n 1 } \ M _ { n 2 } \cdot \cdot \cdot \cdot \ M _ { n n } } \end{array} \right] \left[ \begin{array} { l } { 1 \overline { { { \cal U } } } _ { 2 1 } \cdot \cdot \cdot \cdot \overline { { { \cal U } } } _ { n 1 } } \\ { \vdots \ } \\ { \vdots \ } \\ { \vdots \ \vdots \ \cdot \ \ddots \ \vdots } \\ { 0 \ \vdots \ \ \vdots \ \ \ddots \ 1 } \end{array} \right] } \end{array}
$$

$$
= \left[ \begin{array} { c c c c } { \overline { { q } } _ { 1 1 } - C _ { 2 1 } \cdot \cdot \cdot - C _ { n 1 } } \\ { C _ { 2 1 } } & { \overline { { q } } _ { 2 2 } } & { \cdot \cdot \cdot - C _ { n 2 } } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { C _ { n 1 } } & { C _ { n 2 } } & { \cdot \cdot \cdot } & { \overline { { q } } _ { m n } } \end{array} \right] .
$$

In Eq. (5.9.9), $\overline { { Q } }$ is assumed to be a diagonal matrix with elements $\overline { { q } } _ { i i } = q _ { i i } / 2$ $( i = 1 , \ldots , n )$ . (This assumption can be generalized to allow other nonzero terms in the $\overline { { Q } }$ matrix with only a slight increase in algebraic complexity.) Each row of the upper triangular portion of the $\widetilde { C }$ matrix in Eq. (5.9.9) is determined as the product of the corresponding row of the $M$ matrix with the appropriate column of the $\overline { { U } } ^ { T }$ matrix. After an upper triangular row of $\widetilde { C }$ is determined, the condition from Eq. (5.9.5) that $\begin{array} { r } { \ddot { C } _ { i j } = - \ddot { C } _ { j i } ( i = 1 , \dotsc , n ; j = 1 , \dotsc , i - 1 ) } \end{array}$ is invoked to evaluate the corresponding lower triangular column of $\widetilde { C }$ . Then, a column of the lower triangular elements of $M$ can be evaluated. Once the elements of the $M$ matrix are determined, the new row of the upper triangular $\widetilde { C }$ elements can be computed along with a column of the $\dot { \overline { { U } } }$ and $\dot { \overline { { D } } }$ elements. This process is repeated until all $\dot { \overline { { U } } }$ and $\dot { \overline { { D } } }$ values are determined. The implementation of this approach proceeds as follows. From Eqs. (5.9.6) and (5.9.7) one can write

$$
M + T = \dot { \overline { { U } } } \overline { { D } } + \overline { { U } } \dot { \overline { { D } } } / 2 .
$$

The expansion of Eq. (5.9.10) in summation notation gives

$$
M _ { i j } + T _ { i j } = \sum _ { k = 1 } ^ { n } { \dot { \overline { { U } } } } _ { i k } { \overline { { d } } } _ { k j } + \sum _ { k = 1 } ^ { n } { \overline { { U } } } _ { i k } { \dot { \overline { { d } } } } _ { k j }
$$

$$
\left( i = 1 , \ldots , n ; j = 1 , \ldots , i \right) .
$$

But, since $\overline { { D } }$ is diagonal, Eq. (5.9.11) becomes

$$
\begin{array} { c } { { M _ { i j } + T _ { i j } = \dot { \overline { { U } } } _ { i j } \overline { { d } } _ { j j } + \overline { { U } } _ { i j } \dot { \overline { { d } } } _ { j j } / 2 } } \\ { { \nonumber } } \\ { { ( i = 1 , \ldots , n ; j = 1 , \ldots , i ) } } \end{array}
$$

for $i = j , \overline { { U } } _ { i j } \equiv 1$ , and $\dot { \overline { { U } } } _ { i j } \equiv 0$ . Therefore, Eq. (5.9.12) becomes

$$
\dot { \overline { d } } _ { i i } = 2 \left( M _ { i i } + T _ { i i } \right) ( i = 1 , \ldots , n ) .
$$

For $i > j$ , Eq. (5.9.12) is rearranged to obtain the differential equation

$$
\begin{array} { r l r } & { } & { \dot { \overline { { U } } } _ { i j } = ( M _ { i j } + T _ { i j } - \overline { { U } } _ { i j } \dot { \overline { { d } } } _ { j j } / 2 ) / \overline { { d } } _ { j j } } \\ & { } & \\ & { } & { ( i = 2 , . . . , n ; ~ j = 1 , . . . , ~ i - 1 ) . } \end{array}
$$

Equations (5.9.13) and (5.9.14) are the forms of the differential equations to be employed in the derivative routine of a numerical integrator. The elements of $T _ { i j }$ and $M _ { i j }$ are computed as define d in Eq. (5.9.7). The pertinent equations can be combined to obtain the following algorithm.

# 5.9.1 TRIANGULAR SQUARE ROOT ALGORITHM

# Measurement Update

If the Extended Sequential Filter algorithm (for which the reference trajectory is updated at each observation point) is adopted, the measurement update algorithm for the $U D U ^ { T }$ factorization has the following form. Using the observation $Y _ { k + 1 } = G ( \mathbf { X } _ { k + 1 } , t _ { k + 1 } )$ , calculate

$$
H _ { k + 1 } = \left[ \partial G \left( \overline { { \mathbf { X } } } _ { k + 1 } , t _ { k + 1 } \right) / \partial \overline { { \mathbf { X } } } _ { k + 1 } \right] .
$$

For $i = 1 , \ldots , n$

$$
\overline { { F } } _ { i } = H _ { i } + \sum _ { k = i + 1 } ^ { n } H _ { k } \overline { { U } } _ { k i }
$$

$$
V _ { i } = \overline { { { d } } } _ { i } \overline { { { F } } } _ { i } .
$$

Set $\beta _ { n + 1 } = R _ { k + 1 }$ (where $R _ { k + 1 }$ is the variance of the measurement noise at the $k + 1 ^ { \mathrm { s t } }$ observation epoch) and calculate

$$
\beta _ { i } = \beta _ { i + 1 } + V _ { i } \overline { { F } } _ { i } \quad ( i = n , . . . , 1 ) .
$$

Calculate diagonal covariance elements

$$
\begin{array} { c } { { d _ { i } = \overline { { { d } } } _ { i } \beta _ { i + 1 } / \beta _ { i } ( i = 1 , \ldots , n ) } } \\ { { { } } } \\ { { \alpha = \beta _ { 1 } . } } \end{array}
$$

For $i = 2 , \ldots , n$ and $j = 1 , \dots , i - 1$ , calculate

$$
P _ { j } = \overline { { F } } _ { j } / \beta _ { j + 1 }
$$

$$
B _ { i j } = V _ { i } + \sum _ { k = j + 1 } ^ { i - 1 } { \overline { { U } } } _ { i k } V _ { k }
$$

$$
U _ { i j } = \overline { { { U } } } _ { i j } - B _ { i j } P _ { j } \quad ( i = 2 , \ldots n ; \quad j = 1 , \ldots , i - 1 ) .
$$

Compute the observation residual

$$
y _ { k + 1 } = Y _ { k + 1 } - G \left( \overline { { \mathbf { X } } } _ { k + 1 } , t _ { k + 1 } \right) .
$$

Calculate gain, and update the state using

$$
\begin{array} { l } { { \displaystyle { \overline { { K } } } _ { i } = V _ { i } + \sum _ { j = 1 } ^ { i - 1 } \overline { { U } } _ { i j } V _ { j } \quad ( i = 1 , \dots , n ) } } \\ { { \displaystyle \hat { \bf X } _ { i } = \overline { { \bf X } } _ { i } + \overline { { K } } _ { i } y _ { k + 1 } / \alpha \quad ( i = 1 , \dots , n ) . } } \end{array}
$$

# Propagation

Given the elements of the square root state error covariance in lower triangular $\overline { { U } } \overline { { D } } \overline { { U } } ^ { T }$ form, $\overline { { Q } } \equiv Q / 2$ and $A ( t )$ , the differential equations $\dot { \overline { { U } } } _ { i j }$ and $\dot { \overline { { d } } } _ { i i }$ can be computed as follows:

$$
\begin{array} { r l r } & { } & { \mathcal { T } _ { 3 \zeta } - \displaystyle \sum _ { j = 0 } ^ { \infty } \mathcal { A } _ { j , j } \mathbb { E } _ { j , j } \mathcal { A } _ { j , j } \left\{ \ell - 1 , \dots , n _ { k } \right\} } \\ & { } & { \mathcal { D } _ { j , 1 \ell } } \\ & { } & { \mathcal { E } _ { i \ell } = \displaystyle \sum _ { k = 1 } ^ { \ell } \lambda _ { i \ell } \widetilde { U } _ { j , k } - \displaystyle \sum _ { k = 1 + 1 } ^ { \ell } \mathcal { D } _ { k \ell } \widetilde { U } _ { \ell } \left( \ell - 1 , \dots , n _ { k } \right) } \\ & { } & { \mathcal { D } _ { j \ell } - \displaystyle \sum _ { k = 1 } ^ { \ell } \lambda _ { \ell } \widetilde { U } _ { \ell } \left( \ell + 1 , \dots , n _ { k } \right) } \\ & { } & { \mathcal { D } _ { i , j } = \widetilde { \mathcal { D } } _ { i , j } \frac { \ell - 1 } { \lambda _ { \ell } } \mathcal { D } _ { k \ell } \left( \ell - 1 , \dots , n _ { k } \right) } \\ & { } & { \mathcal { M } _ { i , j } = \widetilde { U } _ { i , j } \frac { \ell - 1 } { \lambda _ { \ell } } \mathcal { M } _ { j , \ell } \mathcal { D } _ { \ell } \left( \ell - 1 , \dots , n _ { k } \right) } \\ & { } & { \mathcal { H } _ { i , j } = \widetilde { U } _ { i , j } \frac { \ell } { \lambda _ { \ell } } \mathcal { D } _ { j , 1 } \left( \ell - 1 , \dots , n _ { k } \right) } \\ & { } & { \mathcal { D } _ { i , j } = \widetilde { \mathcal { D } } _ { i , j } \frac { \ell - 1 } { \lambda _ { \ell } } \mathcal { D } _ { j , 1 } \left( \ell - 1 , \dots , n _ { k } \right) } \\ & { } & { \mathcal { D } _ { i , j } = \left( \lambda _ { i \ell } \right) _ { i \ell } \frac { \ell } { \lambda _ { \ell } } \mathcal { D } _ { j , 2 } \left( \ell - 1 , \dots , n _ { k } \right) } \\ & { } & { \mathcal { D } _ { i , j } = \left( \lambda _ { i \ell } \right) _ { i \ell } \frac { \ell } { \lambda _ { \ell } } \mathcal { D } _ { j , 1 } \left( \ell - 1 , \dots , n _ { k } \right) } \\ & { } &  \end{array}
$$

The algorithm summarized in Eqs. (5.9.15) through (5.9.32) defines a complete sequential estimation algorithm in which the covariance matrices $P$ and $\bar { \overline { { P } } }$ are replaced by the factors $( U , D )$ and $( \overline { { U } } , \overline { { D } } )$ , respectively. The algorithm given here assumes that only a single scalar observation is processed at each observation epoch; however, the algorithm is applicable to the case of multiple observations at a given epoch if the observation errors are uncorrelated. To obtain

$$
A ( t ) = \frac { F ( { \bf X } , t ) } { \partial { \bf X } } ,
$$

the additional integration of the system of nonlinear differential equations, ${ \dot { \bf X } } = { }$ $F ( \mathbf { X } , t )$ , is required. At the initial point, the starting conditions $\dot { \overline { { \mathbf { X } } } } _ { k } = \hat { \mathbf { X } } _ { k }$ are used.

# 5.10 THE SQUARE ROOT INFORMATION FILTER

In Sections 5.7, 5.8, and 5.9, attention has been directed to the problem of developing estimation algorithms based on the square root of the covariance matrix. Both measurement incorporation and time propagation algorithms were considered. In this section, we consider algorithms derived from the information equations, referred to as the normal equations in Chapter 4. Specificall y, we consider algorithms that deal with factoring the information matrix. In general such an algorithm is referred to as a square root information fil ter or SRIF.

We will first consider the case where the state vector, $\mathbf { x }$ , is independent of time; that is, a constant. Assume that $a$ priori information $[ \overline { { \mathbf { x } } } , \overline { { \Lambda } } ]$ is given, where x is the a priori value of x and Λ is the a priori information matrix, Λ = P −1 . The $a$ priori information can be written in the form of a data equation by noting that

$$
\begin{array} { r } { \overline { { \mathbf { x } } } = \mathbf { x } + \boldsymbol { \eta } , } \end{array}
$$

where $\eta$ is the error in $\overline { { \mathbf { x } } }$ and is assumed to have the following characteristics

$$
E [ \pmb { \eta } ] = 0 , E [ \pmb { \eta } \pmb { \eta } ^ { T } ] = \overline { { P } } = \overline { { \Lambda } } ^ { - 1 } .
$$

Factoring the information matrix yields

$$
\overline { { { \Lambda } } } = \overline { { { R } } } ^ { T } \overline { { { R } } } .
$$

Multiplying Eq. (5.10.1) by $\overline { { R } }$ yields

$$
\overline { { R } } \overline { { \mathbf { x } } } = \overline { { R } } \mathbf { x } + \overline { { R } } \boldsymbol { \eta } .
$$

Define

$$
\begin{array} { r } { \overline { { { \bf b } } } = \overline { { R } } \overline { { \bf x } } \quad \mathrm { a n d } \quad \overline { { \eta } } = \overline { { R } } \eta . } \end{array}
$$

Then Eq. (5.10.4) assumes the standard form of the data equation

$$
\overline { { \mathbf { b } } } = \overline { { R } } \mathbf { x } + \overline { { \eta } } .
$$

Note that the error $\overline { { \eta } }$ still has zero mean but now has unit variance,

$$
\begin{array} { r l } & { E [ \overline { { \eta } } ] = \overline { { R } } E [ \pmb { \eta } ] = 0 } \\ & { E [ \pmb { \eta } \pmb { \eta } ^ { T } ] = \overline { { R } } E [ \pmb { \eta } \pmb { \eta } ^ { T } ] \overline { { R } } ^ { T } = \overline { { R } } \overline { { P } } \overline { { R } } ^ { T } = I . } \end{array}
$$

We now seek to determine the “best” estimate of $\mathbf { x }$ given the a priori information in the form of Eq. (5.10.6), and additional observation data

$$
\mathbf { y } = H \mathbf { x } + \epsilon ,
$$

where $\epsilon \sim ( O , I )$ ; the observations have been prewhitened as described in Section 5.7.1. This value of $\mathbf { x }$ will be defined as that which minimizes the least squares performance index,

$$
\begin{array} { r l } & { J ( \mathbf { x } ) = \| \boldsymbol { \epsilon } \| ^ { 2 } + \| \overline { { \eta } } \| ^ { 2 } } \\ & { \qquad = \| H \mathbf { x } - \mathbf { y } \| ^ { 2 } + \| \overline { { R } } \mathbf { x } - \overline { { \mathbf { b } } } \| ^ { 2 } } \\ & { \qquad = \left\| \left[ \begin{array} { l } { \overline { { R } } } \\ { H } \end{array} \right] \mathbf { x } - \left[ \overline { { \mathbf { b } } } \right] \right\| ^ { 2 } . } \end{array}
$$

Following the procedure of Section 5.4, we apply a series of orthogonal transformations to Eq. (5.10.9) such that

$$
T \left[ { \frac { { \overline { { R } } } { \bar { \mathbf { b } } } } { H { \mathbf { y } } } } \right] = { \left[ { R \mathbf { b } } \right] }
$$

and the performance index becomes

$$
{ \begin{array} { r } { J ( \mathbf { x } ) = \left\| \left[ { \boldsymbol { R } } \right] \mathbf { x } - \left[ \mathbf { b } \right] \right\| ^ { 2 } } \\ { = \| { \boldsymbol { R } } \mathbf { x } - \mathbf { b } \| ^ { 2 } + \| \mathbf { e } \| ^ { 2 } . } \end{array} }
$$

The value of the $\mathbf { x }$ that minimizes the performance index is

$$
\hat { \mathbf { x } } = R ^ { - 1 } \mathbf { b } .
$$

Equation (5.10.12) is most easily solved by a backward substitution given by Eq. (5.2.8),

$$
\hat { x } _ { i } = \left( b _ { i } - \sum _ { j = i + 1 } ^ { n } R _ { i j } \hat { x } _ { j } \right) / R _ { i i } , i = n \ldots 1 .
$$

The data processing algorithm based on the orthogonal transformation can be summarized as follows. Assume we are given the $a$ priori information $\overline { { \cal R } } , \overline { { \bf b } }$ and the measurements $y _ { j } = H _ { j } { \bf x } + \epsilon _ { j } , j = 1 , \ldots , \ell$ , where each $y _ { j }$ is a scalar and where $\epsilon _ { j } \sim ( O , 1 )$ . Then the least squares estimate can be generated recursively as follows:

(a) Compute

$$
T _ { j } \left[ { \begin{array} { l } { { \overline { { R } } } { \bar { \mathbf { \Delta b } } } } \\ { { H _ { j } y _ { j } } } \end{array} } \right] = \left[ { R _ { j } \mathbf { \Delta b } _ { j } } \right] .
$$

(b) $R _ { j } { \hat { \mathbf { x } } } _ { j } = \mathbf { b } _ { j } .$

Solve for $\hat { \mathbf { x } } _ { j }$ by a backward substitution as given by Eq. (5.10.13) at each stage $j$ . If the estimation error covariance matrix is desired at any stage, it is computed from

$$
P _ { j } = R _ { j } ^ { - 1 } R _ { j } ^ { - T } .
$$

(c) $R _ { j }$ and $\mathbf { b } _ { j }$ become the a priori for the next stage.

(d) Repeat this process for $j = 1 , \dots , \ell$ .

Note that the residual sum of squares of the $a$ priori errors plus observation errors based on $\ell$ measurements is

$$
J ( \widehat { \mathbf { x } } _ { \ell } ) = \sum _ { i = 1 } ^ { \ell } \left( y _ { i } - H _ { i } \widehat { \mathbf { x } } _ { \ell } \right) ^ { 2 } + ( \widehat { \mathbf { x } } _ { \ell } - \overline { { \mathbf { x } } } ) ^ { T } \overline { { R } } ^ { T } \overline { { R } } ( \widehat { \mathbf { x } } _ { \ell } - \overline { { \mathbf { x } } } ) = \sum _ { i = 1 } ^ { \ell } e _ { i } ^ { 2 } .
$$

# 5.10.1 THE SQUARE ROOT INFORMATION FILTER WITH TIME-DEPENDENT EFFECTS

Consider the dynamic model of Eq. (4.9.46),

$$
\mathbf { x } _ { k } = \boldsymbol \Phi ( t _ { k } , t _ { j } ) \mathbf { x } _ { j } + \Gamma ( t _ { k } , t _ { j } ) \mathbf { u } _ { j }
$$

where

$$
E [ \mathbf { u } _ { j } ] = \overline { { \mathbf { u } } } , ~ E [ ( \mathbf { u } _ { j } - \overline { { \mathbf { u } } } ) ( \mathbf { u } _ { k } - \overline { { \mathbf { u } } } ) ^ { T } ] = Q \delta _ { j k } .
$$

Generally we assume that $\mathbf { \overline { { u } } = 0 }$ , but for this discussion we will assume that the random sequence $\mathbf { u } _ { j }$ has a known mean, u. $Q$ is assumed to be positive definite, and may vary with time, but we will assume that both $Q$ and $\mathbf { \overline { { u } } }$ are constant here.

Assume that a sequence of scalar observation, $y _ { i }$ , is given such that

$$
y _ { i } = H _ { i } \mathbf { x } _ { i } + \epsilon _ { i } , \quad i = 1 , \ldots , \ell
$$

and the observations have been prewhitened so that

$$
E [ \epsilon _ { i } ] = 0 , ~ E ( \epsilon _ { i } ^ { 2 } ) = 1 .
$$

Assume that at the initial time, say $t _ { 0 }$ , there is $a$ priori information given in the form of the information array $[ \overline { { R } } _ { 0 } , \overline { { \mathbf { b } } } _ { 0 } ]$ from which $\overline { { \mathbf { x } } } _ { 0 }$ and $\overline { { P } } _ { 0 }$ are determined as (the a priori information may be $\overline { { \mathbf { x } } } _ { \mathrm { 0 } }$ and $\overline { { P } } _ { 0 }$ from which $[ \overline { { R } } _ { 0 } , \overline { { \mathbf { b } } } _ { 0 } ]$ are computed)

$$
{ \bf { \overline { { x } } } } _ { 0 } = { \overline { { R } } } _ { 0 } ^ { - 1 } { \bf { \overline { { b } } } } _ { 0 } \quad { \bf { \overline { { P } } } } _ { 0 } = { \overline { { R } } } _ { 0 } ^ { - 1 } { \overline { { R } } } _ { 0 } ^ { - T } .
$$

Because $E [ \mathbf { u } ( t _ { 0 } ) ] = \overline { { \mathbf { u } } }$ , the a priori quantities are mapped to $t _ { 1 }$ by

$$
\begin{array} { r l } & { \overline { { \mathbf { x } } } _ { 1 } = \Phi ( t _ { 1 } , t _ { 0 } ) \overline { { \mathbf { x } } } _ { 0 } + \Gamma ( t _ { 1 } , t _ { 0 } ) \overline { { \mathbf { u } } } } \\ & { \mathbf { x } _ { 1 } = \Phi ( t _ { 1 } , t _ { 0 } ) \mathbf { x } _ { 0 } + \Gamma ( t _ { 1 } , t _ { 0 } ) \mathbf { u } _ { 0 } } \\ & { \overline { { P } } _ { 1 } = E [ ( \overline { { \mathbf { x } } } _ { 1 } - \mathbf { x } _ { 1 } ) ( \overline { { \mathbf { x } } } _ { 1 } - \mathbf { x } _ { 1 } ) ^ { T } ] } \\ & { \quad \mathbf { \Phi } = \Phi ( t _ { 1 } , t _ { 0 } ) \overline { { P } } _ { 0 } \Phi ^ { T } ( t _ { 1 } , t _ { 0 } ) + \Gamma ( t _ { 1 } , t _ { 0 } ) Q \Gamma ^ { T } ( t _ { 1 } , t _ { 0 } ) . } \end{array}
$$

For the case where there is no process noise, $Q$ is assumed to be zero, as is $\mathbf { u } _ { j }$ , and the following solution is applicable.

# Process Noise Absent

In this case both $Q$ and $\mathbf { \overline { { u } } }$ are assumed to be zero and

$$
\overline { { { P } } } _ { k } = \Phi ( t _ { k } , t _ { j } ) P _ { j } \Phi ^ { T } ( t _ { k } , t _ { j } ) .
$$

In terms of square root notation

$$
\overline { { { P } } } _ { k } = \overline { { { R } } } _ { k } ^ { - 1 } \overline { { { R } } } _ { k } ^ { - T } = \Phi ( t _ { k } , t _ { j } ) R _ { j } ^ { - 1 } R _ { j } ^ { - T } \Phi ^ { T } ( t _ { k } , t _ { j } ) .
$$

Hence,

$$
\overline { { R } } _ { k } ^ { - 1 } = \Phi ( t _ { k } , t _ { j } ) R _ { j } ^ { - 1 }
$$

and

$$
\overline { { { R } } } _ { k } = R _ { j } \Phi ^ { - 1 } ( t _ { k } , t _ { j } ) .
$$

It follows then that the mapping relations are

$$
\begin{array} { l } { { { \overline { { \bf x } } } _ { k } = \Phi ( t _ { k } , t _ { j } ) { \hat { \bf x } } _ { j } } } \\ { { { \overline { { R } } } _ { k } = R _ { j } \Phi ^ { - 1 } ( t _ { k } , t _ { j } ) . } } \end{array}
$$

Note also that the compressed observation can be obtained as

$$
\begin{array} { r l } & { \mathbf { \overline { { b } } } _ { k } = \overline { { R } } _ { k } \mathbf { \overline { { x } } } _ { k } = R _ { j } \Phi ^ { - 1 } ( t _ { k } , t _ { j } ) \Phi ( t _ { k } , t _ { j } ) \hat { \mathbf { x } } _ { j } } \\ & { \quad \mathbf { \overline { { \Lambda } } } = R _ { j } \hat { \mathbf { x } } _ { j } = \mathbf { b } _ { j } . } \end{array}
$$

With these mapping equations we can set up the equations for the SRIF algorithm. Assume that at time, $t _ { j }$ , we have a priori information

$$
\overline { { \mathbf { b } } } _ { j } = \overline { { R } } _ { j } \overline { { \mathbf { x } } } _ { j }
$$

where

$$
\overline { { \mathbf { x } } } _ { j } = \mathbf { x } _ { j } + \boldsymbol { \eta } _ { j }
$$

and

$$
\begin{array} { r } { E [ \pmb { \eta } _ { j } ] = 0 \qquad } \\ { E [ \pmb { \eta } _ { j } \pmb { \eta } _ { j } ^ { T } ] = \overline { { P } } _ { j } = \overline { { R } } _ { j } ^ { - 1 } \ \overline { { R } } _ { j } ^ { - T } . } \end{array}
$$

By multiplying Eq. (5.10.27) by $\overline { { R } } _ { j }$ , we obtain

$$
\overline { { \mathbf { b } } } _ { j } = \overline { { R } } _ { j } \mathbf { x } _ { j } + \overline { { \pmb { \eta } } } _ { j }
$$

where $\overline { { \pmb { \eta } } } _ { j } = \overline { { \pmb { R } } } _ { j } \pmb { \eta } _ { j }$ . Further, $\overline { { \pmb { \eta } } } _ { j }$ satisfies the condition $E ( \overline { { \eta } } _ { j } ) = 0$ and it is easily demonstrated that $E ( \overline { { \eta } } _ { j } \overline { { \eta } } _ { j } ^ { T } ) = I$ . Now assume that we have the new observation, $y _ { j }$ , where

$$
y _ { j } = H _ { j } \mathbf { x } _ { j } + \epsilon _ { j }
$$

and $\epsilon _ { j }$ satisfies the conditions given in Eq. (5.10.18). To obtain a best estimate of $\mathbf { x } _ { j }$ , the least squares performance index to be minimized is

$$
J ( \mathbf { x } _ { j } ) = \| \overline { { \pmb { \eta } } } _ { j } \| ^ { 2 } + \epsilon _ { j } ^ { 2 } ,
$$

or

$$
J ( \mathbf { x } _ { j } ) = \| \overline { { R } } _ { j } \mathbf { x } _ { j } - \overline { { \mathbf { b } } } _ { j } \| ^ { 2 } + \left( H _ { j } \mathbf { x } _ { j } - y _ { j } \right) ^ { 2 } .
$$

Following the procedure discussed in the previous section, $J ( \mathbf { x } _ { j } )$ can be written as

$$
J ( \mathbf { x } _ { j } ) = \left\| \left[ \overline { { R } } _ { j } \right] \mathbf { x } _ { j } - \left[ \overline { { \mathbf { b } } } _ { j } \right] \right\| ^ { 2 } .
$$

Multiplying by an orthogonal transformation, $T$ , yields

$$
J ( \mathbf { x } _ { j } ) = [ \begin{array} { l } { [ \overline { { R } } _ { j } ] } \\ { H _ { j } } \end{array} ] \mathbf { x } _ { j } - [ \overline { { \mathbf { b } } } _ { j } ] ] ^ { T } T ^ { T } T [ \begin{array} { l } { [ \overline { { R } } _ { j } ] } \\ { H _ { j } } \end{array} ] \mathbf { x } _ { j } - [ \overline { { \mathbf { b } } } _ { j } ] ] .
$$

We select $T$ so that

$$
T \left[ { \overline { { R } } } _ { j } \right] = { \bigg [ } R _ { j } { \bigg ] } , T \left[ { \overline { { \mathbf { b } } } } _ { j } \right] = { \bigg [ } { \mathbf { b } } _ { j } { \bigg ] }
$$

where $R _ { j }$ is upper triangular. Eq. (5.10.30) can be expressed then as

$$
J ( \mathbf { x } _ { j } ) = \left\| \left[ \binom { R _ { j } } { 0 } \mathbf { x } _ { j } - \left[ \mathbf { b } _ { j } \right] \right] ^ { 2 } \right\| ^ { 2 }
$$

or

$$
J ( \mathbf { x } _ { j } ) = ( e _ { j } ) ^ { 2 } + \| R _ { j } \mathbf { x } _ { j } - \mathbf { b } _ { j } \| ^ { 2 } .
$$

It follows that to minimize $J ( \mathbf { x } _ { j } )$ ,

$$
\hat { \mathbf { x } } _ { j } = R _ { j } ^ { - 1 } \mathbf { b } _ { j } , P _ { j } = R _ { j } ^ { - 1 } R _ { j } ^ { - T } , J ( \hat { \mathbf { x } } _ { j } ) \ : = \ : e _ { j } ^ { 2 } .
$$

where the elements of the vector $\hat { \mathbf { x } } _ { j }$ are obtained by evaluating Eq. (5.10.13). The previous steps are equivalent to the measurement update for the Kalman filter. The time update is obtained by mapping $\hat { \mathbf { x } } _ { j }$ and $R _ { j }$ forward to time $t _ { k }$ as follows

$$
\begin{array} { r l } & { \overline { { \mathbf { x } } } _ { k } = \Phi ( t _ { k } , t _ { j } ) \hat { \mathbf { x } } _ { j } } \\ & { \overline { { R } } _ { k } = R _ { j } \Phi ^ { - 1 } ( t _ { k } , t _ { j } ) } \\ & { \overline { { \mathbf { b } } } _ { k } = \overline { { R } } _ { k } \overline { { \mathbf { x } } } _ { k } = \mathbf { b } _ { j } } \end{array}
$$

and the measurement update process is repeated to obtain $\hat { \mathbf { x } } _ { k }$ . Note that the sum of squares of the estimation errors would be stored as (assuming we have processed $k$ scalar observations)1

$$
J ( \mathbf { x } _ { k } ) = \sum _ { i = 1 } ^ { k } e _ { i } ^ { 2 } .
$$

An alternate equation to Eq. (5.10.23) can be obtained by noting that for any $t$ ,

and

$$
\begin{array} { r } { \overline { { R } } ( t ) = R _ { j } \Phi ^ { - 1 } ( t , t _ { j } ) } \\ { \qquad } \\ { \dot { \overline { { R } } } ( t ) = R _ { j } \dot { \Phi } ^ { - 1 } ( t , t _ { j } ) . } \end{array}
$$

Substituting for $\dot { \Phi } ^ { - 1 } ( t , t _ { j } )$ leads to

$$
\dot { \overline { { { R } } } } ( t ) = - R _ { j } \Phi ^ { - 1 } ( t , t _ { j } ) A ( t ) = - \overline { { { R } } } ( t ) A ( t ) .
$$

Hence, as an alternate to Eq. (5.10.23) one can integrate the equation

$$
{ \dot { \overline { { R } } } } ( t ) = - { \overline { { R } } } A ( t ) .
$$

with initial conditions

$$
\begin{array} { r } { \overline { { R } } ( t _ { j } ) = R _ { j } . } \end{array}
$$

The propagation can be accomplished either by using Eq. (5.10.37) or by integrating Eq. (5.10.38) while propagating the state by integrating

$$
\dot { \overline { { \mathbf { x } } } } = A ( t ) \overline { { \mathbf { x } } } ,
$$

with the initial conditions $\overline { { \mathbf { x } } } _ { j } = \hat { \mathbf { x } } _ { j }$ . However, because $\overline { { \mathbf { b } } } _ { k } = \mathbf { b } _ { j }$ there is no need to map $\overline { { \mathbf { x } } } _ { j }$ . The $a$ priori covariance $\overline { { P } } _ { k }$ at $t _ { k }$ is obtained, in either case, as

$$
\overline { { P } } _ { k } = \overline { { R } } _ { k } ^ { - 1 } \overline { { R } } _ { k } ^ { - T } .
$$

If needed, a differential equation for $\overline { { R } } ^ { - 1 }$ is easily developed. From Eq. (5.10.37)

$$
\overline { { R } } _ { k } ^ { - 1 } = \Phi ( t _ { k } , t _ { j } ) R _ { j } ^ { - 1 }
$$

and

$$
\begin{array} { r l } & { \dot { \overline { { R } } } ^ { - 1 } ( t ) = \dot { \Phi } ( t , t _ { j } ) R _ { j } ^ { - 1 } } \\ & { \qquad = A ( t ) \Phi ( t , t _ { j } ) R _ { j } ^ { - 1 } } \\ & { \dot { \overline { { R } } } ^ { - 1 } ( t ) = A ( t ) \overline { { R } } ^ { - 1 } ( t ) , \mathrm { w i t h ~ I . c . ~ } \overline { { R } } ^ { - 1 } ( t _ { j } ) = R _ { j } ^ { - 1 } . } \end{array}
$$

Finally, note that even though $R _ { j }$ is upper triangular, the propagated information matrix $\overline { { R } } _ { k }$ will not be. An upper triangular time update for $\overline { { R } } _ { k }$ can be developed by noting that

$$
\overline { { { \Lambda } } } _ { k } = \overline { { { P } } } _ { k } ^ { - 1 } = \overline { { { R } } } _ { k } ^ { T } \overline { { { R } } } _ { k } .
$$

From Eq. (5.10.37)

$$
\overline { { \Lambda } } _ { k } = \Phi ^ { - T } ( t _ { k } , t _ { j } ) R _ { j } ^ { T } R _ { j } \Phi ^ { - 1 } ( t _ { k } , t _ { j } )
$$

multiplying by an orthogonal transformation yields

$$
\overline { { \Lambda } } _ { k } = \Phi ^ { - T } ( t _ { k } , t _ { j } ) R _ { j } ^ { T } T ^ { T } T R _ { j } \Phi ^ { - 1 } ( t _ { k } , t _ { j } ) = \overline { { R } } _ { k } ^ { T } \overline { { R } } _ { k }
$$

where $T$ is chosen so that

$$
\overline { { R } } _ { k } = T R _ { j } \Phi ^ { - 1 } ( t _ { k } , t _ { j } )
$$

is upper triangular. A Householder or Givens transformation may be used to accomplish this.

# 5.10.2 THE DYNAMIC CASE WITH PROCESS NOISE

The technique for including process noise in both the Potter and SRIF algorithms was developed by Dyer and McReynolds (1969). The state propagation equation for the case with process noise is given by Eq. (5.10.16),

$$
\mathbf { x } _ { k } = \Phi ( t _ { k } , t _ { k - 1 } ) \mathbf { x } _ { k - 1 } + \Gamma ( t _ { k } , t _ { k - 1 } ) \mathbf { u } _ { k - 1 } .
$$

The SRIF for this case can be formulated as follows. Assume that at $t _ { k - 1 }$ a priori information in the form of an information array $[ \overline { { R } } _ { k - 1 } \overline { { \mathbf { b } } } _ { k - 1 } ]$ or equivalently $[ \overline { { P } } _ { k - 1 } \overline { { \mathbf { x } } } _ { k - 1 } ]$ is available,

$$
\overline { { \mathbf { b } } } _ { k - 1 } = \overline { { R } } _ { k - 1 } \overline { { \mathbf { x } } } _ { k - 1 }
$$

but

$$
\overline { { \mathbf { x } } } _ { k - 1 } = \mathbf { x } _ { k - 1 } + \boldsymbol { \eta } _ { k - 1 }
$$

where $\mathbf x _ { k - 1 }$ is the true value. Also,

$$
E [ \pmb { \eta } _ { k - 1 } ] = 0 , E [ \pmb { \eta } _ { k - 1 } \pmb { \eta } _ { k - 1 } ^ { T } ] = \overline { { P } } _ { k - 1 } = \overline { { R } } _ { k - 1 } ^ { - 1 } \overline { { R } } _ { k - 1 } ^ { - T } .
$$

Substituting Eq. (5.10.47) into (5.10.46) yields the data equation for the $a$ priori information

$$
\overline { { \mathbf { b } } } _ { k - 1 } = \overline { { R } } _ { k - 1 } \mathbf { x } _ { k - 1 } + \overline { { \pmb { \eta } } } _ { k - 1 }
$$

where

$$
\begin{array} { c } { { E [ \overline { { { \pmb { \eta } } } } _ { k - 1 } ] = \overline { { { \cal R } } } _ { k - 1 } E [ \pmb { \eta } _ { k - 1 } ] = 0 } } \\ { { E [ \overline { { { \pmb { \eta } } } } _ { k - 1 } \overline { { { \pmb { \eta } } } } _ { k - 1 } ^ { T } ] = \overline { { { \cal R } } } _ { k - 1 } \overline { { { \cal P } } } _ { k - 1 } \overline { { { \cal R } } } _ { k - 1 } ^ { T } = I . } } \end{array}
$$

A scalar observation is given at $t _ { k - 1 }$

$$
y _ { k - 1 } = H _ { k - 1 } \mathbf { x } _ { k - 1 } + \epsilon _ { k - 1 }
$$

where we assume that the observations have been prewhitened so that $\epsilon _ { k - 1 } \sim$ [0, 1].

A priori information on $\mathbf { u } _ { k - 1 }$ is given by covariance $Q$ and by $\overline { { \mathbf { u } } } _ { k - 1 }$ , the mean value of $\mathbf { u }$ . Generally it is assumed that $\mathbf { u }$ is a zero mean process so that the $a$ priori value $\overline { { \mathbf { u } } } = 0$ at each stage. This information also may be written in the form of a data equation by noting that

$$
\begin{array} { c } { { \overline { { \mathbf { u } } } = \overline { { \mathbf { u } } } _ { k - 1 } } } \\ { { \mathbf { \Pi } } } \\ { { \mathbf { \Pi } = \mathbf { u } _ { k - 1 } + \alpha _ { k - 1 } } } \end{array}
$$

where $\overline { { \mathbf { u } } } _ { k - 1 }$ is the a priori value and $\mathbf { u } _ { k - 1 }$ is the true value. The error, $\pmb { \alpha } _ { k - 1 }$ , has the properties

$$
\begin{array} { r } { E [ \pmb { \alpha } _ { k - 1 } ] = 0 , } \\ { E [ \pmb { \alpha } _ { k - 1 } \pmb { \alpha } _ { k - 1 } ^ { T } ] = Q . } \end{array}
$$

We will assume that the process noise is uncorrelated in time; that is, $E [ \pmb { \alpha } _ { i } \pmb { \alpha } _ { j } ^ { T } ] =$ 0 for $i \neq j$ . Although it is not necessary, we will assume that both $\mathbf { u }$ and $Q$ are constant in time. Factor $Q$ such that

$$
\begin{array} { r } { R _ { u } ^ { - 1 } R _ { u } ^ { - T } = Q . } \end{array}
$$

After multiplying Eq. (5.10.53) by $R _ { u }$ , we may write the data equation for $\overline { { \mathbf { u } } } _ { k - 1 }$ as

$$
\begin{array} { r l } {  { R _ { u } \overline { { \mathbf { u } } } _ { k - 1 } \equiv \overline { { \mathbf { b } } } _ { u _ { k - 1 } } } } \\ & { = R _ { u } \mathbf { u } _ { k - 1 } + \overline { { \mathbf { \alpha } } } \overline { { \mathbf { \alpha } } } _ { k - 1 } } \end{array}
$$

where

$$
\begin{array} { r } { \overline { { \alpha } } _ { k - 1 } \sim [ O , I ] . } \end{array}
$$

Now define a performance index for the measurement update at $t _ { k - 1 }$ . We choose as our least squares performance index the sum of the squared errors given by Eqs (5.10.49), (5.10.52), and (5.10.56),

$$
\hat { J } _ { k - 1 } = \| \overline { { \eta } } _ { k - 1 } \| ^ { 2 } + ( \epsilon _ { k - 1 } ) ^ { 2 } + \| \overline { { \alpha } } _ { k - 1 } \| ^ { 2 } .
$$

Note that including $\| \overline { { \alpha } } \| ^ { 2 }$ in the performance index allows us to estimate $\mathbf { u }$ at each stage. The values of $\mathbf x _ { k - 1 }$ that minimizes $\hat { J } _ { k - 1 }$ is the filter value, $\hat { \mathbf { x } } _ { k - 1 }$ . At this point the value of $\mathbf { u } _ { k - 1 }$ that minimizes $\hat { J } _ { k - 1 }$ is just the $a$ priori value, $\overline { { \mathbf { u } } } _ { k - 1 }$ . After we perform a time and measurement update at $t _ { k }$ we will have the necessary information to compute $\hat { \mathbf { u } } _ { k - 1 }$ . Use the defining equations for the errors to write $\hat { J } _ { k - 1 }$ as

$$
\begin{array} { r l } & { \hat { J } _ { k - 1 } = \Vert \overline { { R } } _ { k - 1 } \mathbf { x } _ { k - 1 } - \overline { { \mathbf { b } } } _ { k - 1 } \Vert ^ { 2 } + ( H _ { k - 1 } \mathbf { x } _ { k - 1 } - y _ { k - 1 } ) ^ { 2 } } \\ & { \qquad + \Vert R _ { u } \mathbf { u } _ { k - 1 } - \overline { { \mathbf { b } } } _ { u _ { k - 1 } } \Vert ^ { 2 } . } \end{array}
$$

Because $\mathbf x _ { k - 1 }$ is independent of $\mathbf { u } _ { k - 1 }$ it is convenient to write this as

$$
\hat { J } _ { k - 1 } = \left\| \left[ \begin{array} { l } { \overline { { R } } _ { k - 1 } } \\ { H _ { k - 1 } } \end{array} \right] \mathbf { x } _ { k - 1 } - \left[ \overline { { \mathbf { b } } } _ { k - 1 } \right] \right\| ^ { 2 } + \| R _ { u } \mathbf { u } _ { k - 1 } - \overline { { \mathbf { b } } } _ { u _ { k - 1 } } \| ^ { 2 } .
$$

Applying a series of orthogonal transformations to the first term of Eq. (5.10.59) results in

$$
\hat { J } _ { k - 1 } = \left\| \begin{array} { l } { \left[ \begin{array} { l } { \hat { R } _ { k - 1 } } \\ { 0 } \end{array} \right] \mathbf { x } _ { k - 1 } - \left[ \begin{array} { l } { \hat { \mathbf { b } } _ { k - 1 } } \\ { e _ { k - 1 } } \end{array} \right] } \end{array} \right\| ^ { 2 } + \| R _ { u } \mathbf { u } _ { k - 1 } - \overline { { \mathbf { b } } } _ { u _ { k - 1 } } \| ^ { 2 }
$$

or

$$
\hat { J } _ { k - 1 } = ( e _ { k - 1 } ) ^ { 2 } + \| \hat { R } _ { k - 1 } { \bf x } _ { k - 1 } - \hat { \bf b } _ { k - 1 } \| ^ { 2 } + \| R _ { u } { \bf u } _ { k - 1 } - \overline { { { \bf b } } } _ { u _ { k - 1 } } \| ^ { 2 } .
$$

The minimum value of $\hat { J } _ { k - 1 }$ is found by setting

$$
\begin{array} { r } { \hat { R } _ { k - 1 } \hat { \mathbf { x } } _ { k - 1 } = \hat { \mathbf { b } } _ { k - 1 } } \\ { R _ { u } \overline { { \mathbf { u } } } _ { k - 1 } = \overline { { \mathbf { b } } } _ { u _ { k - 1 } } . } \end{array}
$$

As stated earlier, Eq. (5.10.63) returns the $a$ priori value, $\overline { { \mathbf { u } } } _ { k - 1 }$ . The minimum value of $\hat { J } _ { k - 1 }$ is given by

$$
\begin{array} { r } { \hat { J } _ { k - 1 } = \left( e _ { k - 1 } \right) ^ { 2 } . } \end{array}
$$

Also,

$$
P _ { k - 1 } = \hat { R } _ { k - 1 } ^ { - 1 } \hat { R } _ { k - 1 } ^ { - T } .
$$

Having completed the measurement update at $t _ { k - 1 }$ , we are ready to do the time update to $t _ { k }$ . In order to time update the performance index $\hat { J } _ { k - 1 } ^ { - }$ , we need to write Eq. (5.10.61) in terms of $\mathbf { x } _ { k }$ . Because $\mathbf { u } _ { k - 1 }$ is not time dependent, the update of $\mathbf { u }$ to $t _ { k }$ will be handled in the measurement update. From Eq. (5.10.45) we may write $\mathbf x _ { k - 1 }$ in terms of $\mathbf { x } _ { k }$ ,

$$
{ \bf x } _ { k - 1 } = \Phi ^ { - 1 } ( t _ { k } , t _ { k - 1 } ) ( { \bf x } _ { k } - \Gamma ( t _ { k } , t _ { k - 1 } ) { \bf u } _ { k - 1 } ) .
$$

Substituting Eq. (5.10.66) into Eq. (5.10.61) yields the time update

$$
\begin{array} { r l r } & { } & { \overline { { J } } _ { k } = ( e _ { k - 1 } ) ^ { 2 } + \Vert \hat { R } _ { k - 1 } \Phi ^ { - 1 } ( t _ { k } , t _ { k - 1 } ) ( { \bf x } _ { k } - \Gamma ( t _ { k } , t _ { k - 1 } ) { \bf u } _ { k - 1 } ) - \hat { { \bf b } } _ { k - 1 } \Vert ^ { 2 } } \\ & { } & { + \Vert { R } _ { u } { \bf u } _ { k - 1 } - \overline { { { \bf b } } } _ { u _ { k - 1 } } \Vert ^ { 2 } , \qquad ( { \boldsymbol 5 } . 1 0 . } \end{array}
$$

which may be written as

$$
\begin{array} { r l } & { \overline { { \boldsymbol J } } _ { k } = ( \boldsymbol e _ { k - 1 } ) ^ { 2 } + } \\ & { \left\| \left[ \begin{array} { l } { \boldsymbol R _ { u } } \\ { - \tilde { \boldsymbol R } _ { k } \boldsymbol \Gamma ( t _ { k } , t _ { k - 1 } ) ~ \tilde { \boldsymbol R } _ { k } } \end{array} \right] \left[ \begin{array} { l } { \mathbf u _ { k - 1 } } \\ { \mathbf x _ { k } } \end{array} \right] - \left[ \overline { { \mathbf b } } _ { u _ { k - 1 } } \right] \right\| ^ { 2 } } \end{array}
$$

where

$$
\tilde { R } _ { k } \equiv \hat { R } _ { k - 1 } \Phi ^ { - 1 } ( t _ { k } , t _ { k - 1 } ) .
$$

We now apply a series of $q$ orthogonal transformations to the second term of Eq. (5.10.68), where $q$ is the dimension of $\mathbf { u } _ { k - 1 }$ . This will partly upper triangularize Eq. (5.10.68) (for $q < n$ ) and will eliminate the explicit dependence of $\mathbf { x } _ { k }$ on $\mathbf { u } _ { k - 1 }$ , i.e.

$$
\begin{array} { r } { \overline { { T } } _ { k } \left[ \begin{array} { c c } { R _ { u } } & { 0 } & { \overline { { \mathbf { b } } } _ { u _ { k - 1 } } } \\ { - \tilde { R } _ { k } \Gamma ( t _ { k } , t _ { k - 1 } ) } & { \tilde { R } _ { k } } & { \hat { \mathbf { b } } _ { k - 1 } } \end{array} \right] = \left[ \begin{array} { c c } { \overline { { R } } _ { u _ { k } } } & { \overline { { R } } _ { u x _ { k } } } & { \widetilde { \mathbf { b } } _ { u _ { k } } } \\ { 0 } & { \overline { { R } } _ { k } } & { \overline { { \mathbf { b } } } _ { k } } \end{array} \right] . } \end{array}
$$

Then,

$$
\begin{array} { r } { \overline { { \boldsymbol { J } } } _ { k } = ( e _ { k - 1 } ) ^ { 2 } + \left\| \left[ \begin{array} { l l } { \overline { { R } } _ { u _ { k } } } & { \overline { { R } } _ { u x _ { k } } } \\ { 0 } & { \overline { { R } } _ { k } } \end{array} \right] \left[ \begin{array} { l } { \mathbf { u } _ { k - 1 } } \\ { \mathbf { x } _ { k } } \end{array} \right] - \left[ \begin{array} { l } { \widetilde { \mathbf { b } } _ { u _ { k } } } \\ { \overline { { \mathbf { b } } } _ { k } } \end{array} \right] \right\| ^ { 2 } . } \end{array}
$$

The minimum value of $J$ is obtained by setting

$$
\begin{array} { r } { \overline { { R } } _ { u _ { k } } \mathbf { u } _ { k - 1 } + \overline { { R } } _ { u x _ { k } } \mathbf { x } _ { k } = \widetilde { \mathbf { b } } _ { u _ { k } } } \\ { \overline { { R } } _ { k } \mathbf { x } _ { k } = \overline { { \mathbf { b } } } _ { k } . } \end{array}
$$

Therefore,

$$
\begin{array} { r } { \overline { { \mathbf { x } } } _ { k } = \overline { { R } } _ { k } ^ { - 1 } \overline { { \mathbf { b } } } _ { k } . } \end{array}
$$

Because $\overline { { R } } _ { u k }$ is nonsingular we can find a value of $\mathbf { u } _ { k - 1 }$ to satisfy Eq. (5.10.72) for any value of $\mathbf { x } _ { k }$ . We know that the value of $\overline { { \mathbf { x } } } _ { k }$ that results from Eq. (5.10.74) is given by

$$
\overline { { \mathbf { x } } } _ { k } = \Phi ( t _ { k } , t _ { k - 1 } ) \hat { \mathbf { x } } _ { k - 1 } + \Gamma ( t _ { k } , t _ { k - 1 } ) \overline { { \mathbf { u } } } _ { k - 1 }
$$

where $\overline { { \mathbf { u } } } _ { k - 1 }$ is the mean or $a$ priori value. Using this value of $\overline { { \mathbf { x } } } _ { k }$ in Eq. (5.10.72) will yield $\overline { { \mathbf { u } } } _ { k - 1 }$ . This is to be expected since we get no information on $\overline { { \mathbf { u } } } _ { k - 1 }$ until we process an observation at $t _ { k }$ .

Recall that the error covariance associated with $\bar { \bf x } _ { k }$ is

$$
\begin{array} { r l } & { \overline { { P } } _ { k } = E [ ( \overline { { \mathbf { x } } } _ { k } - \mathbf { x } _ { k } ) ( \overline { { \mathbf { x } } } _ { k } - \mathbf { x } _ { k } ) ^ { T } ] = \overline { { R } } _ { k } ^ { - 1 } \overline { { R } } _ { k } ^ { - T } } \\ & { \quad = \Phi ( t _ { k } , t _ { k - 1 } ) P _ { k - 1 } \Phi ^ { T } ( t _ { k } , t _ { k - 1 } ) } \\ & { \quad + \Gamma ( t _ { k } , t _ { k - 1 } ) Q \Gamma ^ { T } ( t _ { k } , t _ { k - 1 } ) . } \end{array}
$$

Equation (5.10.71) may be written as

$$
\begin{array} { r l } & { \overline { { J } } _ { k } = ( e _ { k - 1 } ) ^ { 2 } + \| \overline { { R } } _ { u _ { k } } \mathbf { u } _ { k - 1 } + \overline { { R } } _ { u x _ { k } } \mathbf { x } _ { k } - \widetilde { \mathbf { b } } _ { u _ { k } } \| ^ { 2 } } \\ & { \quad ~ + \| \overline { { R } } _ { k } \mathbf { x } _ { k } - \overline { { \mathbf { b } } } _ { k } \| ^ { 2 } . } \end{array}
$$

We may now do the measurement update at $t _ { k }$ . The least squares performance index for the measurement update is

$$
\begin{array} { r l } & { \hat { J } _ { k } = \overline { { J } } _ { k } + ( \epsilon _ { k } ) ^ { 2 } + \| \overline { { \alpha } } _ { k } \| ^ { 2 } } \\ & { \quad = \overline { { J } } _ { k } + ( H _ { k } \mathbf { x } _ { k } - y _ { k } ) ^ { 2 } + \| R _ { u } \mathbf { u } _ { k } - \overline { { \mathbf { b } } } _ { u _ { k } } \| ^ { 2 } . } \end{array}
$$

This may be written as

$$
\begin{array} { r } { \hat { J } _ { k } = ( e _ { k - 1 } ) ^ { 2 } + \| \overline { { R } } _ { u _ { k } } \mathbf { u } _ { k - 1 } + \overline { { R } } _ { u x _ { k } } \mathbf { x } _ { k } - \widetilde { \mathbf { b } } _ { u _ { k } } \| ^ { 2 } } \\ { + \left\| \left[ \overline { { R } } _ { k } \right] \mathbf { x } _ { k } - \left[ \overline { { \mathbf { b } } } _ { k } \right] \right\| ^ { 2 } + \| R _ { u } \mathbf { u } _ { k } - \overline { { \mathbf { b } } } _ { u _ { k } } \| ^ { 2 } . } \end{array}
$$

Applying orthogonal transformations to the third term yields

$$
\begin{array} { r l } & { \hat { J } _ { k } = ( e _ { k - 1 } ) ^ { 2 } + \| \overline { { R } } _ { u _ { k } } \mathbf { u } _ { k - 1 } + \overline { { R } } _ { u x _ { k } } \mathbf { x } _ { k } - \tilde { \mathbf { b } } _ { u _ { k } } \| ^ { 2 } } \\ & { \quad + \| \hat { R } _ { k } \mathbf { x } _ { k } - \hat { \mathbf { b } } _ { k } \| ^ { 2 } + ( e _ { k } ) ^ { 2 } + \| R _ { u } \mathbf { u } _ { k } - \overline { { \mathbf { b } } } _ { u _ { k } } \| ^ { 2 } . } \end{array}
$$

Once again $\mathbf { u } _ { k - 1 }$ , $\mathbf { u } _ { k }$ , and $\mathbf { x } _ { k }$ may be chosen to null all but the $( e ) ^ { 2 }$ terms. Hence, the minimum value of $\hat { J } _ { k }$ is

$$
\hat { J } _ { k } = ( e _ { k - 1 } ) ^ { 2 } + ( e _ { k } ) ^ { 2 } .
$$

The time update to obtain $\overline { { J } } _ { k + 1 }$ may now be obtained by substituting

$$
\mathbf { x } _ { k } = \Phi ^ { - 1 } \bigl ( t _ { k + 1 } , t _ { k } \bigr ) \bigl ( \mathbf { x } _ { k + 1 } - \Gamma \bigl ( t _ { k + 1 } , t _ { k } \bigr ) \mathbf { u } _ { k } \bigr )
$$

for $\mathbf { x } _ { k }$ in the term $\| \hat { R } _ { k } \mathbf { x } _ { k } - \hat { \mathbf { b } } _ { k } \| ^ { 2 }$ . Hence, the general expression for the time update at $t _ { m }$ after processing $m - 1$ observations is

$$
\begin{array} { r l r } {  { \overline { { J } } _ { m } = \sum _ { i = 1 } ^ { m - 1 } ( e _ { i } ) ^ { 2 } + \sum _ { i = 1 } ^ { m - 1 } \| \overline { { R } } _ { u _ { i } } \mathbf { u } _ { i - 1 } + \overline { { R } } _ { u x _ { i } } \mathbf { x } _ { i } - \widetilde { \mathbf { b } } _ { u _ { i } } \| ^ { 2 } } } \\ & { } & { + \| [ \begin{array} { l } { R _ { u } } \\ { - \widetilde { R } _ { m } \Gamma ( t _ { m } , t _ { m - 1 } ) \widetilde { R } _ { m } } \end{array} ] [ \begin{array} { l } { \mathbf { u } _ { m - 1 } } \\ { \mathbf { x } _ { m } } \end{array} ] - [ \overline { { \mathbf { b } } } _ { u _ { m - 1 } } ] \| ^ { 2 } } \end{array}
$$

and the corresponding measurement update for processing $m$ observations is obtained by upper triangularizing the third term of Eq. (5.10.82) and adding the data equations for the $m ^ { t h }$ observation,

$$
\begin{array} { r l r } {  { \hat { J } _ { m } = \overline { { J } } _ { m } + ( \epsilon _ { m } ) ^ { 2 } + \| \overline { { \boldsymbol { \alpha } } } _ { m } \| ^ { 2 } } } \\ & { } & { = \displaystyle \sum _ { i = 1 } ^ { m - 1 } ( e _ { i } ) ^ { 2 } + \sum _ { i = 1 } ^ { m } \| \overline { { R } } _ { u _ { i } } \mathbf { u } _ { i - 1 } + \overline { { R } } _ { u x _ { i } } \mathbf { x } _ { i } - \widetilde { \mathbf { b } } _ { u _ { i } } \| ^ { 2 } + \| R _ { u } \mathbf { u } _ { m } - \overline { { \mathbf { b } } } _ { u _ { m } } \| ^ { 2 } } \\ & { } & { + \| [ \overline { { R } } _ { m } ] \mathbf { x } _ { m } - [ \overline { { \mathbf { b } } } _ { m } ] \| ^ { 2 } . \quad \quad \quad \quad ( 5 . 1 0 . } \end{array}
$$

An orthogonal transformation is then applied to the last term of Eq. (5.10.83).

Finally, continuing the time and measurement update through stage $m$ yields

$$
\begin{array} { l } { { \displaystyle \hat { J } _ { m } = \sum _ { i = 1 } ^ { m } ( e _ { i } ) ^ { 2 } + \sum _ { i = 1 } ^ { m } \| \overline { { R } } _ { u _ { i } } { \bf u } _ { i - 1 } + \overline { { R } } _ { u x _ { i } } { \bf x } _ { i } - \widetilde { { \bf b } } _ { u _ { i } } \| ^ { 2 } } } \\ { { \displaystyle ~ + \| R _ { u } { \bf u } _ { m } - \overline { { { \bf b } } } _ { u _ { m } } \| ^ { 2 } + \| \hat { R } _ { m } { \bf x } _ { m } - \hat { { \bf b } } _ { m } \| ^ { 2 } } , } \end{array}
$$

so that for the filtering problem ${ \hat { J } } _ { m } $ is minimized by choosing

$$
\hat { \mathbf { x } } _ { m } = \hat { R } _ { m } ^ { - 1 } \hat { \mathbf { b } } _ { m }
$$

and

$$
\overline { { { R } } } _ { u _ { i } } \hat { \mathbf { u } } _ { i - 1 } = \widetilde { \mathbf { b } } _ { u _ { i } } - \overline { { { R } } } _ { u x _ { i } } \hat { \mathbf { x } } _ { i } ; i = m , m - 1 \ldots 1 .
$$

Notice that the third term in Eq. (5.10.84) is simply the addition of a priori information on $\mathbf { u } _ { m }$ and does not affect the performance index until we perform a time and measurement update at $t _ { m + 1 }$ . Then it yields the estimate for $\hat { \mathbf { u } } _ { m }$ given by Eq. (5.10.86) with $i = m + 1$ .

If we were performing only a filtering operation and had a need for a filtered value of $\hat { \bf { u } }$ , we would calculate it at each stage and not save the quantities $\overline { { R } } _ { u }$ , $\overline { { { \bf b } } } _ { u }$ , and $\overline { { R } } _ { u x }$ needed to compute it. However, if we wish to perform smoothing, these quantities should be saved as described in Section 5.10.4.

# 5.10.3 SRIF COMPUTATIONAL ALGORITHM

The SRIF computational algorithm is summarized as follows. Assuming we have processed the observations at the $k - 1 ^ { s t }$ stage, the time update for $t _ { k }$ is obtained by applying a series of orthogonal transformations, $\overline { { T } } _ { k }$ , to

$$
\begin{array} { r l } { \overrightarrow { T } _ { k } } &  \left[ \overbrace { \frac { R _ { u } } { - \tilde { R } _ { k } \Gamma ( t _ { k } , t _ { k - 1 } ) \left| \ \tilde { R } _ { k } \right| \ \hat { \mathbf { b } } _ { k - 1 } } } ^ { q } \right] \mathbf { \} \mathbf { \Sigma } _ { \left. n \right. } } \\ &  = \left[ \begin{array} { c c c c } { \overbrace { \tilde { R } _ { u _ { k } } } ^ { \mathrm { ~ ~ \it ~ n ~ } } } & { \overbrace { \tilde { R } _ { u _ { k } u _ { k } } } ^ { \mathrm { ~ \it ~ n ~ } } } & { \overbrace { \tilde { \mathbf { b } } _ { u _ { k } } } ^ { \mathrm { ~ \it ~ 1 ~ } } } & { } \\ { 0 } & { \overbrace { \tilde { R } _ { k } \mathrm { ~ \it ~ \hat { \textbf { b } } } _ { k } } ^ { \mathrm { ~ \it ~ 1 ~ } } } & { \right] \mathbf { \Sigma } _ { \left. n \right. } } \end{array} \end{array}
$$

where $\tilde { R } _ { k }$ is defined by Eq. (5.10.69) and $q$ and $n$ are the dimensions of the process noise and state vector, respectively. From Eqs. (5.10.70) and (5.10.71) we can write

$$
\left[ \begin{array} { c } { { \overline { { { R } } } _ { u _ { k } } \overline { { { R } } } _ { u x _ { k } } } } \\ { 0 \overline { { { R } } } _ { k } } \end{array} \right] \left[ \begin{array} { c } { { \widetilde { \mathbf { u } } _ { k - 1 } } } \\ { { \overline { { \mathbf { x } } } _ { k } } } \end{array} \right] = \left[ \begin{array} { c } { { \widetilde { \mathbf { b } } _ { u _ { k } } } } \\ { { \overline { { \mathbf { b } } } _ { k } } } \end{array} \right]
$$

from which $\tilde { \mathbf { u } } _ { k - 1 }$ , $\overline { { \mathbf { x } } } _ { k }$ and $\overline { { P } } _ { k }$ may be computed if desired. It is not necessary to compute these quantities. However, the quantities in the first row of Eq. (5.10.87) should be stored if smoothing is to take place.

The measurement update at $t _ { k }$ is obtained by applying a series of orthogonal transformations, $\hat { T } _ { k }$ , to

$$
\hat { T } _ { k } \stackrel { n } { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { \widehat { R } _ { k } } & { \widehat { \mathbf { b } } _ { k } } \\ { H _ { k } } & { y _ { k } } \end{array} \right] } \} n = \left[ \hat { R } _ { k } \hat { \mathbf { b } } _ { k } \right]
$$

and

$$
\begin{array} { r } { \hat { R } _ { k } \hat { \mathbf x } _ { k } = \hat { \mathbf b } _ { k } \quad } \\ { P _ { k } = \hat { R } _ { k } ^ { - 1 } \ \hat { R } _ { k } ^ { - T } } \\ { e = e + e _ { k } ^ { 2 } \ \quad } \end{array}
$$

where $e$ is the sum of squares of the observation residuals.

We can compute the filter value, $\hat { \mathbf { u } } _ { k - 1 }$ , by substituting $\hat { \mathbf { x } } _ { k }$ into Eq. (5.10.86),

$$
\hat { \mathbf { u } } _ { k - 1 } = \overline { { R } } _ { u _ { k } } ^ { - 1 } \big ( \widetilde { \mathbf { b } } _ { u _ { k } } - \overline { { R } } _ { u x _ { k } } \hat { \mathbf { x } } _ { k } \big ) .
$$

The time update at $t _ { k + 1 }$ may now be computed from Eq. (5.10.87) and the measurement update from Eq. (5.10.89) after changing the index from $k$ to $k + 1$ . The procedure is continued until all observations have been processed.

# 5.10.4 SMOOTHING WITH THE SRIF

There are two approaches that may be taken to perform smoothing with the SRIF (Kaminski, 1971). The first of these uses the performance index given by Eq. (5.10.84). This performance index must be satisfied by the smooth states as well as the filter states. Hence, the equations needed for smoothing are Eqs. (5.10.85), (5.10.86), and (5.10.66). These are repeated using smoothing notation:

$$
\begin{array} { r } { \hat { R } _ { m } \hat { \mathbf { x } } _ { m } ^ { m } = \hat { \mathbf { b } } _ { m } } \\ { \overline { { R } } _ { u _ { i } } \hat { \mathbf { u } } _ { i - 1 } ^ { m } = \widetilde { \mathbf { b } } _ { u _ { i } } - \overline { { R } } _ { u x _ { i } } \hat { \mathbf { x } } _ { i } ^ { m } \quad i = m , m - 1 , \ldots , 1 . } \\ { \hat { \mathbf { x } } _ { i - 1 } ^ { m } = \Phi ^ { - 1 } ( t _ { i } , t _ { i - 1 } ) ( \hat { \mathbf { x } } _ { i } ^ { m } - \Gamma ( t _ { i } , t _ { i - 1 } ) \hat { \mathbf { u } } _ { i - 1 } ^ { m } ) } \end{array}
$$

where the notation $( ) _ { i } ^ { m }$ means the smoothed value of the quantity at $t _ { i }$ based on $m$ observations. Note that this is the same notation used for the conventional smoother in Section 4.15.

Starting with $\hat { \mathbf { x } } _ { m } ^ { m }$ from Eq. (5.10.94), then $\hat { \mathbf { u } } _ { m - 1 } ^ { m }$ is computed from Eq. (5.10.95) and $\hat { \mathbf { x } } _ { m - 1 } ^ { m }$ is determined from Eq. (5.10.96). With this value of $\hat { \mathbf { x } } _ { m - 1 } ^ { m }$ , compute $\hat {  { \mathbf { u } } } _ { m - 2 } ^ { m }$ from Eq. (5.10.95) and $\hat { \mathbf { x } } _ { m - 2 } ^ { m }$ from Eq. (5.10.96), and so on.

This backward sweep strategy may be shown to be equivalent to the smoother described in Section 4.15, and hence it is also equivalent to the Rauch, Tung, and Striebel smoother (1995).

This equivalence may be used to derive an expression for the smoothed covariance for $\hat { \mathbf { x } } _ { k } ^ { m }$ using the filt er time update equation

$$
\overline { { \mathbf { x } } } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { x } } _ { k } + \Gamma ( t _ { k + 1 } , t _ { k } ) \overline { { \mathbf { u } } } _ { k } .
$$

The smoothed solution must also satisfy this equation; hence

$$
\hat { \mathbf { x } } _ { k + 1 } ^ { m } = \Phi ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { x } } _ { k } ^ { m } + \Gamma ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { u } } _ { k } ^ { m } .
$$

Using Eqs. (5.10.97) and (5.10.98) we may write

$$
\begin{array} { r l } & { \hat { \mathbf { x } } _ { k } ^ { m } - \hat { \mathbf { x } } _ { k } = \Phi ^ { - 1 } ( t _ { k + 1 } , t _ { k } ) \left[ \hat { \mathbf { x } } _ { k + 1 } ^ { m } - \overline { { \mathbf { x } } } _ { k + 1 } \right] } \\ & { \qquad + \Phi ^ { - 1 } ( t _ { k + 1 } , t _ { k } ) \Gamma ( t _ { k + 1 } , t _ { k } ) \left[ \overline { { \mathbf { u } } } _ { k } - \hat { \mathbf { u } } _ { k } ^ { m } \right] . } \end{array}
$$

From Eq. (5.10.95)

$$
\hat { \mathbf { u } } _ { k } ^ { m } = \overline { { R } } _ { u _ { k + 1 } } ^ { - 1 } \big ( \widetilde { \mathbf { b } } _ { u _ { k + 1 } } - \overline { { R } } _ { u x _ { k + 1 } } \hat { \mathbf { x } } _ { k + 1 } ^ { m } \big ) .
$$

This equation also yields the fil ter value of $\overline { { \mathbf { u } } } _ { k }$

$$
\overline { { \mathbf { u } } } _ { k } = \overline { { R } } _ { u _ { k + 1 } } ^ { - 1 } \big ( \widetilde { \mathbf { b } } _ { u _ { k + 1 } } - \overline { { R } } _ { u x _ { k + 1 } } \overline { { \mathbf { x } } } _ { k + 1 } \big ) .
$$

From Eq. (5.10.100) and (5.10.101) we may write

$$
\overline { { \mathbf { u } } } _ { k } - \hat { \mathbf { u } } _ { k } ^ { m } = \overline { { R } } _ { u _ { k + 1 } } ^ { - 1 } \overline { { R } } _ { u x _ { k + 1 } } ( \hat { \mathbf { x } } _ { k + 1 } ^ { m } - \overline { { \mathbf { x } } } _ { k + 1 } ) .
$$

Substituting Eq. (5.10.102) into (5.10.99) results in

$$
\begin{array} { r } { \hat { \mathbf { x } } _ { k } ^ { m } = \hat { \mathbf { x } } _ { k } + \Phi ^ { - 1 } ( t _ { k + 1 } , t _ { k } ) \left[ I + \Gamma ( t _ { k + 1 } , t _ { k } ) \overline { { R } } _ { u _ { k + 1 } } ^ { - 1 } \overline { { R } } _ { u x _ { k + 1 } } \right] } \\ { \times \left[ \hat { \mathbf { x } } _ { k + 1 } ^ { m } - \overline { { \mathbf { x } } } _ { k + 1 } \right] . \qquad } \end{array}
$$

Comparing Eq. (5.10.103) with Eqs. (4.15.9) and (4.15.10) yields the identity

$$
\begin{array} { r l } & { S _ { k } = P _ { k } ^ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) \left( P _ { k + 1 } ^ { k } \right) ^ { - 1 } } \\ & { \quad = \Phi ^ { - 1 } ( t _ { k + 1 } , t _ { k } ) \left[ I + \Gamma ( t _ { k + 1 } , t _ { k } ) \overline { { R } } _ { u _ { k + 1 } } ^ { - 1 } \overline { { R } } _ { u x _ { k + 1 } } \right] . } \end{array}
$$

Recall that $\mathbf { \overline { { x } } } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { x } } _ { k } ^ { k }$ in Eq. (4.15.9) since $\overline { { \mathbf { u } } } _ { k } = 0$ by assumption. Hence, the smoothed covariance for the estimation error in $\hat { \mathbf { x } } _ { k } ^ { m }$ may be obtained

from Eq. (4.15.24),

$$
P _ { k } ^ { m } = P _ { k } ^ { k } + S _ { k } ( P _ { k + 1 } ^ { m } - P _ { k + 1 } ^ { k } ) S _ { k } ^ { T }
$$

where $P _ { k } ^ { k }$ is the measurement update of the filter covariance at $t _ { k }$ and $P _ { k + 1 } ^ { k }$ is the time-updated value of $P _ { k } ^ { k }$ at $t _ { k + 1 }$ .

Note that this approach requires storage of the time and measurement update of the filter covariance. The time update is given by Eq. (5.10.75), where ${ \overline { { \overline { { P } } } } } \equiv$ $P _ { k + 1 } ^ { k }$ . The measurement update is given by Eq. (5.10.91), where $P _ { k } \equiv P _ { k } ^ { k }$ .

The smoothing operation also may be carried out, as described by Kaminski (1971), using an approach that yields the smoothed covariance directly and does not require storage of the filter covariance. Use Eq. (5.10.66) in Eq. (5.10.84) to eliminate $\mathbf { x } _ { m }$ . Then the performance index in terms of $\mathbf { x } _ { m - 1 } ^ { m }$ and $\mathbf { u } _ { m - 1 } ^ { m }$ becomes

$$
\begin{array} { r l r } {  { \hat { J } _ { m - 1 } ^ { m } = e _ { m } + \sum _ { m - 1 } + \Vert \overline { { R } } _ { u _ { m } } ^ { m } \mathbf { u } _ { m - 1 } ^ { m } + \overline { { R } } _ { u x _ { m } } [ \Phi ( t _ { m } , t _ { m - 1 } ) \mathbf { x } _ { m - 1 } ^ { m }  } } \\ & { } & { +  \Gamma ( t _ { m } , t _ { m - 1 } ) \mathbf { u } _ { m - 1 } ^ { m } ] - \widetilde { \mathbf { b } } _ { u _ { m } }  ^ { 2 } + \Vert \hat { R } _ { m } [ \Phi ( t _ { m } , t _ { m - 1 } ) \mathbf { x } _ { m - 1 } ^ { m }   } \\ & { } & {   + \Gamma ( t _ { m } , t _ { m - 1 } ) \mathbf { u } _ { m - 1 } ^ { m } ] - \hat { \mathbf { b } } _ { m } \Vert ^ { 2 } . } \end{array}
$$

The term $\| R _ { u } \mathbf { u } _ { m } - \overline { { \mathbf { b } } } _ { u _ { m } } \| ^ { 2 }$ has been dropped since its value is zero by definition; hence, it does not effect the value of $\hat { J } _ { m - 1 } ^ { m }$ . Also,

$$
\begin{array} { l } { { \displaystyle e _ { m } \equiv \sum _ { i = 1 } ^ { m } ( e _ { i } ) ^ { 2 } } \ ~ } \\ { { \displaystyle \sum _ { m - 1 } \equiv \sum _ { i = 1 } ^ { m - 1 } \left\| \overline { { R } } _ { u _ { i } } { \bf u } _ { i - 1 } + \overline { { R } } _ { u x _ { i } } { \bf x } _ { i } - \widetilde { { \bf b } } _ { u _ { i } } \right\| ^ { 2 } } \ . } \end{array}
$$

Equation (5.10.106) may be written as

$$
\begin{array} { r } { \hat { J } _ { m - 1 } ^ { m } =  [ \begin{array} { l } { [ \begin{array} { l } { \overline { { R } } _ { u _ { m } } + \overline { { R } } _ { u x _ { m } } \Gamma ( t _ { m } , t _ { m - 1 } ) } \end{array} ] \begin{array} { l } { \overline { { R } } _ { u x _ { m } } \Phi ( t _ { m } , t _ { m - 1 } ) } \\ { \hat { R } _ { m } \hat { \Phi } ( t _ { m } , t _ { m - 1 } ) } \end{array} ] } \\ { [ \begin{array} { l } { \mathbf { u } _ { m - 1 } ^ { m } } \\ { \mathbf { x } _ { m - 1 } ^ { m } } \end{array} ] - [ \begin{array} { l } { \widetilde { \mathbf { b } } _ { u _ { m } } } \\ { \hat { \mathbf { b } } _ { m } } \end{array} ]  ^ { 2 } + e _ { m } + \boldsymbol { \Sigma } _ { m - 1 } . } \end{array}  ~ ( 5 . 1 } \end{array}
$$

A series of orthogonal transformation is used to upper triangularize the first term of Eq. (5.10.109),

$$
\begin{array} { r l } { T _ { m - 1 } ^ { * } } &  { } \left[ \frac { \phantom { \frac { 1 } { 2 } } \overline { { R } } _ { u _ { m } } + \overline { { R } } _ { u x _ { m } } \Gamma ( t _ { m } , t _ { m - 1 } ) \phantom { \frac { 1 } { 2 } } \phantom { \frac { 1 } { 2 } } \left| \begin{array} { c } { \overline { { R } } _ { u x _ { m } } \Phi ( t _ { m } , t _ { m - 1 } ) } \end{array} \right. \right] } \\ { \phantom { \frac { 1 } { 2 } } \left. \qquad \hat { R } _ { m } \Gamma ( t _ { m } , t _ { m - 1 } ) \phantom { \frac { 1 } { 2 } } \qquad \hat { R } _ { m } \Phi ( t _ { m } , t _ { m - 1 } ) \phantom { \frac { 1 } { 2 } } \phantom { \frac { 1 } { 2 } } \right] } \end{array}
$$

$$
\mathbf { \Phi } = \left[ \begin{array} { c } { R _ { u _ { m - 1 } } ^ { * } } \\ { 0 } \end{array} \right] \begin{array} { c } { R _ { u x _ { m - 1 } } ^ { * } } \\ { R _ { m - 1 } ^ { * } } \end{array} \left[ \begin{array} { c } { \mathbf { b } _ { u _ { m - 1 } } ^ { * } } \\ { \ \mathbf { b } _ { m - 1 } ^ { * } } \end{array} \right] .
$$

Hence,

$$
\begin{array} { r } { \hat { J } _ { m - 1 } ^ { m } = \left\| \boldsymbol { R } _ { u _ { m - 1 } } ^ { * } \mathbf { u } _ { m - 1 } ^ { m } + { \cal R } _ { u x _ { m - 1 } } ^ { * } \mathbf { x } _ { m - 1 } ^ { m } - \mathbf { b } _ { u _ { m - 1 } } ^ { * } \right\| ^ { 2 } } \\ { + \left\| { \cal R } _ { m - 1 } ^ { * } \mathbf { x } _ { m - 1 } ^ { m } - \mathbf { b } _ { m - 1 } ^ { * } \right\| ^ { 2 } + e _ { m } + \Sigma _ { m - 1 } . } \end{array}
$$

To minimize $\hat { J } _ { m - 1 } ^ { m }$ , choose

$$
\begin{array} { r l } & { R _ { u _ { m - 1 } } ^ { * } \hat { \mathbf { u } } _ { m - 1 } ^ { m } = \mathbf { b } _ { u _ { m - 1 } } ^ { * } - R _ { u x _ { m - 1 } } ^ { * } \hat { \mathbf { x } } _ { m - 1 } ^ { m } } \\ & { \quad R _ { m - 1 } ^ { * } \hat { \mathbf { x } } _ { m - 1 } ^ { m } = \mathbf { b } _ { m - 1 } ^ { * } . } \end{array}
$$

The elements of $\Sigma _ { m - 1 }$ can be nulled by the proper selection of $\mathbf { u } _ { m - 2 } . . . . \mathbf { u } _ { 0 }$ . Therefore, we do not need to consider this term. The covariance for the estimation error in $\hat { \mathbf { u } } _ { m - 1 } ^ { m }$ and $\hat { \mathbf { x } } _ { m - 1 } ^ { m }$ is given by

$$
\begin{array} { r l } & { P _ { m - 1 } ^ { m } \equiv \left[ \begin{array} { c } { P _ { u } \ P _ { u x } } \\ { P _ { x u } \ P _ { x } } \end{array} \right] _ { m - 1 } ^ { m } } \\ & { \qquad = \left[ \begin{array} { c } { R _ { u _ { m - 1 } } ^ { * } \ R _ { u x _ { m - 1 } } ^ { * } } \\ { 0 \ R _ { m - 1 } ^ { * } } \end{array} \right] ^ { - 1 } \left[ R _ { u _ { m - 1 } } ^ { * } R _ { u x _ { m - 1 } } ^ { * } \right] ^ { - T } . } \end{array}
$$

Solving the equation

$$
\left[ \begin{array} { c c } { R _ { u _ { m - 1 } } ^ { * } } & { R _ { u x _ { m - 1 } } ^ { * } } \\ { 0 } & { R _ { m - 1 } ^ { * } } \end{array} \right] \left[ \begin{array} { c c } { A } & { B } \\ { 0 } & { C } \end{array} \right] = \left[ \begin{array} { c c } { I } & { 0 } \\ { 0 } & { I } \end{array} \right]
$$

for the matrices $A , B$ , and $C$ yields the inverse necessary to solve for $P _ { m - 1 } ^ { m }$ Substituting the result into Eq. (5.10.114) results in

$$
\begin{array} { r l } & { P _ { u _ { m - 1 } } ^ { m } = R _ { u _ { m - 1 } } ^ { * - 1 } R _ { u _ { m - 1 } } ^ { * - T } } \\ & { \qquad + R _ { u _ { m - 1 } } ^ { * - 1 } R _ { u x _ { m - 1 } } ^ { * } R _ { m - 1 } ^ { * - 1 } R _ { m - 1 } ^ { * - T } R _ { u x _ { m - 1 } } ^ { * T } R _ { u _ { m - 1 } } ^ { * - T } } \\ & { P _ { u x _ { m - 1 } } ^ { m } = - R _ { u _ { m - 1 } } ^ { * - 1 } R _ { u x _ { m - 1 } } ^ { * } R _ { m - 1 } ^ { * - 1 } R _ { m - 1 } ^ { * - T } } \\ & { \qquad P _ { x _ { m - 1 } } ^ { m } = R _ { m - 1 } ^ { * - 1 } R _ { m - 1 } ^ { * - T } . } \end{array}
$$

We are now ready to write $J _ { m - 1 } ^ { m }$ in terms of $ { \mathbf { x } } _ { m - 2 } ^ { m }$ and $ { \mathbf { u } } _ { m - 2 } ^ { m }$ . Because $\mathbf { u } _ { m - 1 } ^ { m }$ is independent of either of these quantities and we have already chosen its value

to null the fir st term in Eq. (5.10.111), we may drop this term when writing $J _ { m - 2 } ^ { m }$ hence,

$$
\begin{array} { r l } & { \hat { J } _ { m - 2 } ^ { m } = \hphantom { \eta } \| R _ { m - 1 } ^ { * } \mathbf x _ { m - 1 } - \mathbf b _ { m - 1 } ^ { * } \| ^ { 2 } + \| \overline { { R } } _ { u _ { m - 1 } } \mathbf u _ { m - 2 } } \\ & { \qquad + \overline { { R } } _ { u x _ { m - 1 } } \mathbf x _ { m - 1 } - \widetilde { \mathbf b } _ { u _ { m - 1 } } \| ^ { 2 } + e _ { m } + \Sigma _ { m - 2 } . } \end{array}
$$

Now use Eq. (5.10.45) to write $\mathbf x _ { m - 1 }$ in Eq. (5.10.118) in terms of $\mathbf { x } _ { m - 2 }$ ,

$$
\begin{array}{c} \begin{array} { r l r } {  { \hat { f } _ { m - 2 } ^ { m } = \| R _ { m - 1 } ^ { * } [ \Phi ( t _ { m - 2 } , t _ { m - 1 } ) \mathbf { x } _ { m - 2 } + \Gamma ( t _ { m - 2 } , t _ { m - 1 } ) \mathbf { u } _ { m - 2 } ] - \mathbf { b } _ { m - 1 } ^ { * } \| ^ { 2 } } } \\ & { } & { + \| \overline { { R } } _ { u _ { m - 1 } } \mathbf { u } _ { m - 2 } + \overline { { R } } _ { u x _ { m - 1 } } [ \Phi ( t _ { m - 2 } , t _ { m - 1 } ) \mathbf { x } _ { m - 2 }   } \\ & { } & {   + \Gamma ( t _ { m - 2 } , t _ { m - 1 } ) \mathbf { u } _ { m - 2 } ] - \widetilde { \mathbf { b } } _ { u _ { m - 1 } } \| ^ { 2 } + e _ { m } + \sum _ { m - 2 } } \\ & { } & { = \| [ \begin{array} { l l } { \overline { { R } } _ { u _ { m - 1 } } + \overline { { R } } _ { u x _ { m - 1 } } \Gamma ( t _ { m - 2 } , t _ { m - 1 } ) } & { | \overline { { R } } _ { u x _ { m - 1 } } \Phi ( t _ { m - 2 } , t _ { m - 1 } )  } \\ {   R _ { m - 1 } ^ { * } \Gamma ( t _ { m - 2 } , t _ { m - 1 } )   } & {   R _ { m - 1 } ^ { * } \Phi ( t _ { m - 2 } , t _ { m - 1 } ) ] } \end{array} ] } \\ & { } & { [ \begin{array} { l } { \mathbf { u } _ { m - 2 } } \\ { \mathbf { x } _ { m - 2 } } \end{array} ] - [ \widetilde { \mathbf { b } } _ { u _ { m - 1 } } } \\ { \mathbf { b } _ { m - 1 } ^ { * } } \end{array} ] \| ^ { 2 } + e _ { m } + \Sigma _ { m - 2 } .  \end{array}
$$

Next a series of orthogonal tranformations is applied to Eq. (5.10.119). This yields the solution for $\hat { \mathbf { x } } _ { m - 2 } ^ { m }$ and $\hat {  { \mathbf { u } } } _ { m - 2 } ^ { m }$ and the associated covariance matrices. This procedure is repeated until the initial stage is reached.

Hence, the procedure is continued recursively by applying orthogonal transformations so that

$$
\begin{array} { r l r } { T _ { k - 1 } ^ { * } } &  \left[ \begin{array} { l } { \overline { { R } } _ { u _ { k } } \overline { { R } } _ { u x _ { k } } \Gamma ( t _ { k } , t _ { k - 1 } ) } \\ { \overline { { R _ { k } ^ { * } \Gamma ( t _ { k } , t _ { k - 1 } ) } } \quad \left| \begin{array} { l } { \overline { { R } } _ { u x _ { k } } \Phi ( t _ { k } , t _ { k - 1 } ) } \\ { \boldsymbol { R } _ { k } ^ { * } \Phi ( t _ { k } , t _ { k - 1 } ) } \end{array} \right| \begin{array} { l } { \widetilde { \mathbf { b } } _ { u _ { k } } } \\ { \mathbf { b } _ { k } ^ { * } } \end{array} \right] } & \\ & { = \left[ \begin{array} { l l } { R _ { u _ { k - 1 } } ^ { * } R _ { u x _ { k - 1 } } ^ { * } \mathbf { b } _ { u _ { k - 1 } } ^ { * } } \\ { 0 \qquad R _ { k - 1 } ^ { * } \mathbf { b } _ { k - 1 } ^ { * } } \end{array} \right] } & { ( 5 . } \end{array} \end{array}
$$

where R∗uk−1 and $R _ { k - 1 } ^ { * }$ are upper triangular. The smoothed solution is given by

$$
\begin{array} { r l } & { \quad R _ { k - 1 } ^ { * } \hat { \mathbf { x } } _ { k - 1 } ^ { m } = \mathbf { b } _ { k - 1 } ^ { * } } \\ & { \quad R _ { u _ { k - 1 } } ^ { * } \hat { \mathbf { u } } _ { k - 1 } ^ { m } = \mathbf { b } _ { u _ { k - 1 } } ^ { * } - R _ { u x _ { k - 1 } } ^ { * } \hat { \mathbf { x } } _ { k - 1 } ^ { m } . } \end{array}
$$

The smoothed covariance is given by

$$
\begin{array} { r l } & { P _ { x _ { k - 1 } } ^ { m } = R _ { k - 1 } ^ { * } - 1 \ R _ { k - 1 } ^ { * - T } } \\ & { P _ { u _ { k - 1 } } ^ { m } = R _ { u _ { k - 1 } } ^ { * - 1 } R _ { u _ { k - 1 } } ^ { * - T } } \\ & { \quad \quad \quad + R _ { u _ { k - 1 } } ^ { * - 1 } R _ { u x _ { k - 1 } } ^ { * } R _ { k - 1 } ^ { * - 1 } R _ { k - 1 } ^ { * - T } R _ { u x _ { k - 1 } } ^ { * T } R _ { u _ { k - 1 } } ^ { * - T } } \end{array}
$$

$$
P _ { u x _ { k - 1 } } ^ { m } = - R _ { u _ { k - 1 } } ^ { * - 1 } R _ { u x _ { k - 1 } } ^ { * } R _ { k - 1 } ^ { * - 1 } R _ { k - 1 } ^ { * - T } .
$$

The first row of the left-hand side of Eq. (5.10.120) is saved from the filtering solution and the second row is computed as part of the smoothing procedure.

# 5.11 PROCESS NOISE PARAMETER FILTERING/ SMOOTHING USING A SRIF

Along with the dynamic state parameters, it is often advantageous to include some other types of parameters in filtering satellite data to improve the solution. In this section we expand the results of the previous section to include in the state vector, bias parameters, and exponentially correlated process noise parameters. These additional parameters will be defined as

c : Bias parameters (constant acceleration parameters, ephemeris corrections, station coordinates, etc.)   
p : Correlated process noise parameters; many random or unmodeled phenomena can be approximated quite well with fir st order exponentially correlated process noise, also referred to as a Gauss-Markov Process and sometimes as colored noise. Variables that commonly are modeled as a Gauss-Markov Process include

Solar radiation pressure Mismodeled drag effects Leaky attitude control systems Moving station positions Polar motion parameters Clock errors Atmospheric path delays Earth rotation parameters

The recursive equation for mapping a discrete first order exponentially correlated process is (Tapley and Ingram, 1973; Bierman, 1977)

$$
\mathbf { p } _ { k + 1 } = M _ { k + 1 } \mathbf { p } _ { k } + \mathbf { w } _ { k } .
$$

$M$ is the process noise parameter transition matrix and is assumed diagonal, with diagonals, $m$ , given by

$$
m = e ^ { - ( t _ { k + 1 } - t _ { k } ) / \tau }
$$

where $\tau$ is the time constant of the process and represents how correlated a process noise parameter is from one time step to the next. The extremes for $\tau$ are related to $m$ as follows:

$$
{ \begin{array} { r l r l r l } { \tau  0 } & { ~  ~ } & { m  0 } & & { ~ { \mathrm { ~ W h i t e ~ n o i s e } } } \\ & { } & & { } & & { ( { \mathrm { n o t ~ c o r r e l a t e d ~ a t ~ a l l ~ i n ~ t i m e } } ) } \\ { \tau  \infty } & { ~  ~ } & { m  1 } & & { ~ { \mathrm { R a n d o m ~ w a l k ~ ( n o ~ s t e a d y ~ s t a t e , ~ } } } \end{array} }
$$

w is called the process noise (not the same as $\mathbf { p }$ ) with

$$
E \left[ \mathbf { w } _ { j } \right] = \overline { { \mathbf { w } } } _ { j } .
$$

In almost all applications, the $a$ priori estimate of $\overline { { \mathbf { w } } } _ { j }$ is zero, but this is not a necessary assumption for this development.

Next

$$
E [ ( \mathbf { w } _ { j } - \overline { { \mathbf { w } } } _ { j } ) ( \mathbf { w } _ { k } - \overline { { \mathbf { w } } } _ { k } ) ^ { T } ] = Q \delta _ { j k }
$$

and

$$
Q = R _ { w } ^ { - 1 } R _ { w } ^ { - T }
$$

where $Q$ is the process noise covariance and is diagonal with elements

$$
q _ { i } = ( 1 - m _ { i } ^ { 2 } ) \sigma _ { i } ^ { 2 } .
$$

The variance corresponding to the particular process noise parameter $p _ { i }$ is $\sigma _ { i } ^ { 2 }$ . The SRIF formulation of Section 5.10 can be adapted to handle bias parameters and first order exponentially correlated noise (Bierman, 1977). The state propogation equations are represented by

$$
\begin{array}{c} \begin{array} { r } { \mathbf { \tilde { \rho } } { \bf \Xi } } \\ { \mathbf { x } } \\ { \mathbf { c } { \bf \Xi } } \\ { { \bf \Xi } { \bf { c } } { \bf \Xi } } \end{array} = \left[ \begin{array} { l l l } { M } & { 0 } & { 0 } \\ { \Phi _ { p } \Phi _ { x } \Phi _ { c } } \\ { 0 } & { 0 } & { I } \end{array} \right] _ { k + 1 } \left[ \begin{array} { l } { \mathbf { p } } \\ { \mathbf { x } } \\ { \mathbf { c } } \end{array} \right] _ { k } + \left[ \begin{array} { l } { \mathbf { w } _ { k } } \\ { 0 } \\ { 0 } \end{array} \right]  \end{array}
$$

where $\Phi _ { p } , \Phi _ { x }$ , and $\Phi _ { c }$ are state transition matrices that map perturbations in $\mathbf { p } , \mathbf { x }$ , and $\mathbf { c }$ at $t _ { k }$ into perturbations in $\mathbf { x }$ at $t _ { k + 1 }$ . If we define

$$
\mathbf { X } _ { k + 1 } \equiv { \left[ \begin{array} { l } { \mathbf { p } } \\ { \mathbf { x } } \\ { \mathbf { c } } \end{array} \right] } _ { k + 1 }
$$

$$
\Phi ( t _ { k + 1 } , t _ { k } ) \equiv \left[ { \begin{array} { c c c } { M \ 0 } & { 0 } \\ { \Phi _ { p } \ \Phi _ { x } \ \Phi _ { c } } \\ { 0 } & { 0 } & { I } \end{array} } \right] _ { k + 1 }
$$

$$
\Gamma ( t _ { k + 1 } , t _ { k } ) \equiv { \Bigg [ } { \begin{array} { l } { I } \\ { 0 } \\ { 0 } \end{array} } { \Bigg ] } ~ ,
$$

Eq. (5.11.7) may be written as

$$
{ \bf X } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) { \bf X } _ { k } + \Gamma ( t _ { k + 1 } , t _ { k } ) { \bf w } _ { k }
$$

which is identical to Eq. (5.10.45). Hence the algorithms of Section 5.10.2 may be applied directly to this problem. In actual practice, however, it is customary to reduce computations by taking advantage of the fact that some parameters are constant and the process noise parameters are modeled as a Gauss-Markov Process (Bierman, 1977).

# 5.11.1 EXPONENTIALLY CORRELATED PROCESS NOISE SRIF

Recall that for a SRIF, $R$ (the square root of the information matrix, $\Lambda$ ) is operated on for the measurement and time update rather than the covariance matrix, $P$ , where

$$
P = \Lambda ^ { - 1 } = R ^ { - 1 } R ^ { - T } .
$$

By keeping $R$ upper triangular through orthogonal transformations, the state deviation estimate, $\hat { \bf x }$ , in a standard SRIF is found by simple back substitution and is given by

$$
\hat { \mathbf { x } } = R ^ { - 1 } \mathbf { b } .
$$

We will derive the filter/s moother equations for the SRIF with bias parameters and process noise parameters shown explicitly. This will be accomplished by deriving and minimizing a least squares performance index.

As shown by Eq. (5.11.1), the recursive equation for a first-order exponentially correlated process is

$$
\mathbf { p } _ { k } = M _ { k } \mathbf { p } _ { k - 1 } + \mathbf { w } _ { k - 1 } .
$$

Assume that $a$ priori information for $\mathbf { w } _ { k - 1 }$ is given by $\overline { { \mathbf { w } } } _ { k - 1 }$ . Generally it is assumed that $\overline { { \bf w } } = 0$ at each stage. Assume that the error in $\overline { { \mathbf { w } } } _ { k - 1 }$ has zero mean (i.e., $\overline { { \mathbf { w } } } _ { k - 1 }$ is the mean value of $\mathbf { w } _ { k - 1 }$ ) and covariance $Q$ . Thus,

$$
\overline { { \mathbf { w } } } _ { k - 1 } = \mathbf { w } _ { k - 1 } + \boldsymbol { \gamma } _ { k - 1 }
$$

where $\mathbf { w } _ { k - 1 }$ is the true value and $\gamma _ { k - 1 }$ is the error in $\overline { { \mathbf { w } } } _ { k - 1 }$ . Hence,

$$
E [ \gamma _ { k - 1 } ] = 0 , E [ \gamma _ { k - 1 } \gamma _ { k - 1 } ^ { T } ] = Q .
$$

We will assume that $\gamma$ is uncorrelated in time so that

$$
E [ \gamma _ { k } \gamma _ { j } ^ { T } ] = Q \delta _ { k j } .
$$

As stated in Eq. (5.11.5), define the square root of $Q$ as

$$
\begin{array} { r } { R _ { w } ^ { - 1 } R _ { w } ^ { - T } = Q . } \end{array}
$$

Substituting $\mathbf { w } _ { k - 1 }$ from Eq. (5.11.13) into Eq. (5.11.14) and multiplying by $R _ { w }$ yields a data equation for $\mathbf { w } _ { k - 1 }$ ,

$$
R _ { w } \overline { { \mathbf { w } } } _ { k - 1 } \equiv \overline { { \mathbf { b } } } _ { w _ { k - 1 } } = R _ { w } \big ( \mathbf { p } _ { k } - M _ { k } \mathbf { p } _ { k - 1 } \big ) + R _ { w } \gamma _ { k - 1 }
$$

or

$$
\overline { { { \bf b } } } _ { w _ { k - 1 } } = R _ { w } ( { \bf p } _ { k } - M _ { k } { \bf p } _ { k - 1 } ) + \overline { { \gamma } } _ { k - 1 }
$$

where

$$
E \left[ \overline { { \gamma } } _ { k - 1 } \right] = R _ { w } E \left[ \gamma _ { k - 1 } \right] = 0 \mathrm { a n d } E \left[ \overline { { \gamma } } _ { k - 1 } \overline { { \gamma } } _ { k - 1 } ^ { T } \right] = I .
$$

Assume further that at $t _ { k - 1 }$ we have a priori information arrays $[ \overline { { R } } _ { p } \ \overline { { \mathbf { b } } } _ { p } ] _ { k - 1 }$ , $[ \overline { { { R } } } _ { x } \ \overline { { { \bf b } } } _ { x } ] _ { k - 1 }$ , and $[ \overline { { R } } _ { c } \ \overline { { \mathbf { b } } } _ { c } ] _ { k - 1 }$ for $\mathbf { p } , \mathbf { x }$ , and $\mathbf { c }$ , respectively. Assume that an observation is available at $t _ { k - 1 }$ given by

$$
y _ { k - 1 } = [ H _ { p } H _ { x } H _ { c } ] _ { k - 1 } \left[ \mathbf { x } \right] _ { k - 1 } + \epsilon _ { k - 1 }
$$

where the observations have been prewhitened so that $\epsilon$ has zero means and unit variance.

Recall that the a priori information on $\mathbf { p } , \mathbf { x }$ , and c may be written in the form of a data equation. For example, the $a$ priori value, $\overline { { \mathbf { p } } } _ { k - 1 }$ , may be written in terms of the true value, $\mathbf { p } _ { k - 1 }$ , and the error, $\eta _ { p _ { k - 1 } }$ , as

$$
\overline { { \mathbf { p } } } _ { k - 1 } = \mathbf { p } _ { k - 1 } + \boldsymbol { \eta } _ { p _ { k - 1 } }
$$

where

$$
E \left[ \pmb { \eta } _ { p _ { k - 1 } } \right] = 0 \mathrm { a n d } E \left[ \pmb { \eta } _ { p } \pmb { \eta } _ { p } ^ { T } \right] _ { k - 1 } = \overline { { P } } _ { p _ { k - 1 } }
$$

and

$$
\overline { { { P } } } _ { p _ { k - 1 } } = ( \overline { { { R } } } _ { p } ^ { - 1 } \overline { { { R } } } _ { p } ^ { - T } ) _ { k - 1 } .
$$

Then the desired data equation is given by multiplying Eq. (5.11.21) by $\overline { { R } } _ { p _ { k - 1 } }$

$$
\left( \overline { { { R } } } _ { p } \ \overline { { { \bf p } } } \right) _ { k - 1 } \equiv \overline { { { \bf b } } } _ { p _ { k - 1 } } = \left( \overline { { { R } } } _ { p } \ { \bf p } \right) _ { k - 1 } + \overline { { { \eta } } } _ { p _ { k - 1 } }
$$

where $\overline { { \eta } } _ { p _ { k - 1 } }$ has zero mean and unit covariance. Similar data equations can be written to represent the a priori information for $\mathbf { x }$ and $\mathbf { c }$ at $t _ { k - 1 }$ .

Given the a priori information and the observation at $t _ { k - 1 }$ we wish to determine the corresponding filter values of $\mathbf { p } , \mathbf { x }$ , and c. The desired algorithm can be developed by minimizing the least squares performance index given by

$$
\hat { J } _ { k - 1 } \equiv \left\| \overline { { \eta } } _ { p _ { k - 1 } } \right\| ^ { 2 } + \left\| \overline { { \eta } } _ { x _ { k - 1 } } \right\| ^ { 2 } + \left\| \overline { { \eta } } _ { c _ { k - 1 } } \right\| ^ { 2 } + \left\| \overline { { \gamma } } _ { k - 1 } \right\| ^ { 2 } + \left( \epsilon _ { k - 1 } \right) ^ { 2 } .
$$

Equation (5.11.25), which corresponds to the measurement update at $t _ { k - 1 }$ , may be written as (see Eqs. (5.11.18), (5.11.20), (5.11.24))

$$
\begin{array} { r l r } & { } & { \hat { J } _ { k - 1 } = \left\| \overline { { R } } _ { p } \mathbf { p } - \overline { { \mathbf { b } } } _ { p } \right\| _ { k - 1 } ^ { 2 } + \left\| \overline { { R } } _ { x } \mathbf { x } - \overline { { \mathbf { b } } } _ { x } \right\| _ { k - 1 } ^ { 2 } + \left\| \overline { { R } } _ { c } \mathbf { c } - \overline { { \mathbf { b } } } _ { c } \right\| _ { k - 1 } ^ { 2 } } \\ & { } & { + \left\| { R } _ { w } ( \mathbf { p } _ { k } - M _ { k } \mathbf { p } _ { k - 1 } ) - \overline { { \mathbf { b } } } _ { w _ { k - 1 } } \right\| ^ { 2 } } \\ & { } & { + \left( \left[ H _ { p } \ H _ { x } \ H _ { x } \right] \left[ \mathbf { p } \right] _ { k } - y \right) _ { k - 1 } ^ { 2 } . } \end{array}
$$

Because we may choose $\mathbf { p } _ { k }$ to zero the next-to-last term in Eq. (5.11.26), we do not have to deal with it until we do the time update to $t _ { k }$ . We may write $\hat { J } _ { k - 1 }$ as

$$
\begin{array} { r } { \hat { J } _ { k - 1 } = \left. \left[ \begin{array} { l l l } { \overline { { R } } _ { p } } & { 0 } & { 0 } \\ { 0 } & { \overline { { R } } _ { x } } & { 0 } \\ { 0 } & { 0 } & { \overline { { R } } _ { c } } \\ { H _ { p } } & { H _ { x } } & { H _ { c } } \end{array} \right] \left[ \begin{array} { l } { \mathbf { p } } \\ { \mathbf { x } } \\ { \mathbf { c } } \end{array} \right] - \left[ \begin{array} { l } { \mathbf { \overline { { b } } } _ { p } } \\ { \mathbf { \overline { { b } } } _ { x } } \\ { \mathbf { \overline { { b } } } _ { c } } \\ { y } \end{array} \right] \right. _ { k - 1 } ^ { 2 } } \\ { + \left. R _ { w } ( \mathbf { p } _ { k } - M _ { k } \mathbf { \textbf { p } } _ { k - 1 } ) - \mathbf { \overline { { b } } } _ { w _ { k - 1 } } \right. ^ { 2 } . } \end{array}
$$

Applying a series of orthogonal transformations to the first term of Eq. (5.11.27) yields

$$
T _ { k - 1 } \left[ \begin{array} { c c c c } { \overline { { { R } } } _ { p } } & { 0 } & { 0 } & { \overline { { { \mathbf b } } } _ { p } } \\ { 0 } & { \overline { { { R } } } _ { x } } & { 0 } & { \overline { { { \mathbf b } } } _ { x } } \\ { 0 } & { 0 } & { \overline { { { R } } } _ { c } } & { \overline { { { \mathbf b } } } _ { c } } \\ { H _ { p } } & { H _ { x } } & { H _ { c } } & { y } \end{array} \right] _ { k - 1 } = \left[ \begin{array} { c c c c } { \hat { R } _ { p } } & { \hat { R } _ { p x } } & { \hat { R } _ { p c } } & { \hat { \mathbf b } _ { p } } \\ { 0 } & { \hat { R } _ { x } } & { \hat { R } _ { x c } } & { \hat { \mathbf b } _ { x } } \\ { 0 } & { 0 } & { \hat { R } _ { c } } & { \hat { \mathbf b } _ { c } } \\ { 0 } & { 0 } & { 0 } & { e } \end{array} \right] _ { k - 1 }
$$

and Eq. (5.11.27) becomes

$$
\begin{array} { r l } & { \hat { J } _ { k - 1 } = \left\| \left[ \begin{array} { l l l } { \hat { R } _ { p } } & { \hat { R } _ { p x } } & { \hat { R } _ { p c } } \\ { 0 } & { \hat { R } _ { x } } & { \hat { R } _ { x c } } \\ { 0 } & { 0 } & { \hat { R } _ { c } } \end{array} \right] \left[ \begin{array} { l } { \mathbf { p } } \\ { \mathbf { x } } \\ { \mathbf { c } } \end{array} \right] - \left[ \begin{array} { l } { \hat { \mathbf { b } } _ { p } } \\ { \hat { \mathbf { b } } _ { x } } \\ { \hat { \mathbf { b } } _ { c } } \end{array} \right] \right\| _ { k - 1 } ^ { 2 } } \\ & { + \left\| R _ { w } \big ( \mathbf { p } _ { k } - M _ { k } \mathbf { \ p } _ { k - 1 } \big ) - \overline { { \mathbf { b } } } _ { w _ { k - 1 } } \right\| ^ { 2 } + ( e ) _ { k - 1 } ^ { 2 } . } \end{array}
$$

From Eq. (5.11.29) we could solve for $\hat { \mathbf { c } } , \hat { \mathbf { x } }$ , and $\hat { \bf p }$ at the $k - 1 ^ { \mathrm { t h } }$ stage.

We now perform the time update of $\hat { J } _ { k - 1 }$ in order to obtain $\overline { { J } } _ { k }$ . To accomplish this we need to replace $\mathbf { x } _ { k - 1 }$ with $\mathbf { x } _ { k }$ . Notice that our performance index already contains $\mathbf { p } _ { k }$ and we will leave $\mathbf { p } _ { k - 1 }$ in the performance index. This will conveniently yield the smoothed value of $\mathbf { p } _ { k - 1 }$ .

From Eq. (5.11.7)

$$
\mathbf { x } _ { k } = \Phi _ { p } ( k ) \mathbf { p } _ { k - 1 } + \Phi _ { x } ( k ) \mathbf { x } _ { k - 1 } + \Phi _ { c } ( k ) \mathbf { c } _ { k - 1 }
$$

or

$$
\mathbf { x } _ { k - 1 } = \Phi _ { x } ^ { - 1 } ( k ) \left[ \mathbf { x } _ { k } - \Phi _ { p } ( k ) \mathbf { p } _ { k - 1 } - \Phi _ { c } ( k ) \mathbf { c } _ { k - 1 } \right]
$$

where

$$
\Phi ( k ) \equiv \Phi ( t _ { k } , t _ { k - 1 } ) .
$$

Also, ${ \bf c } _ { k - 1 } ~ = ~ { \bf c } _ { k }$ , since $\mathbf { c }$ is a constant. Substituting Eq. (5.11.31) into Eq. (5.11.29) yields the following equations

$$
\hat { R } _ { p } \mathbf { p } _ { k - 1 } + \overline { { R } } _ { p x } \left[ { \bf x } _ { k } - \Phi _ { p } ( k ) \mathbf { p } _ { k - 1 } - \Phi _ { c } ( k ) \mathbf { c } _ { k - 1 } \right] + \hat { R } _ { p c } \mathbf { c } _ { k - 1 } = \hat { \mathbf { b } } _ { p _ { k - 1 } }
$$

$$
\overline { { { R } } } _ { x } \left[ \mathbf { x } _ { k } - \boldsymbol { \Phi } _ { p } ( k ) \mathbf { p } _ { k - 1 } - \boldsymbol { \Phi } _ { c } ( k ) \mathbf { c } _ { k - 1 } \right] + \hat { R } _ { x c } \mathbf { c } _ { k - 1 } = \hat { \mathbf { b } } _ { x _ { k - 1 } }
$$

$$
\hat { R } _ { c } \mathbf { c } _ { k - 1 } = \hat { \mathbf { b } } _ { c _ { k - 1 } } .
$$

Also,

$$
R _ { w } ( { \bf p } _ { k } - M _ { k } \mathrm { \bf ~ p } _ { k - 1 } ) = \overline { { { \bf b } } } _ { w _ { k - 1 } }
$$

where

$$
\begin{array} { r } { \overline { { R } } _ { p x } \equiv \hat { R } _ { p x } \Phi _ { x } ^ { - 1 } ( k ) } \\ { \overline { { R } } _ { x } \equiv \hat { R } _ { x } \Phi _ { x } ^ { - 1 } ( k ) . } \end{array}
$$

By regrouping and writing in matrix form (while noting that $\mathbf { c } _ { k - 1 } = \mathbf { c } _ { k }$ ), we may write Eq. (5.11.29) as

$$
\hat { J } _ { k - 1 } = \| [ \begin{array} { c c c c c } { - R _ { w } M _ { k } } & { R _ { w } } & { 0 } & { 0 } \\ { ( \hat { R } _ { p } - \overline { { R } } _ { p x } \Phi _ { p } ( k ) ) } & { 0 } & { \overline { { R } } _ { p x } } & { ( \hat { R } _ { p c } - \overline { { R } } _ { p x } \Phi _ { c } ( k ) ) } \\ { - \overline { { R } } _ { x } \Phi _ { p } ( k ) } & { 0 } & { \overline { { R } } _ { x } } & { ( \hat { R } _ { x c } - \overline { { R } } _ { x } \Phi _ { c } ( k ) ) } \\ { 0 } & { 0 } & { 0 } & { \hat { R } _ { c } } \end{array} ] _ { k - 1 }
$$

$$
\begin{array} { r l } & { [ \mathbf { p } _ { k - 1 } ] } \\ & { [ \begin{array} { l } { \mathbf { p } _ { k } } \\ { \mathbf { x } _ { k } } \\ { \mathbf { c } _ { k } } \end{array} ] - [ \begin{array} { l } { \overline { { \mathbf { b } } } _ { w } } \\ { \hat { \mathbf { b } } _ { p } } \\ { \hat { \mathbf { b } } _ { x } } \\ { \hat { \mathbf { b } } _ { c } } \end{array} ] _ { k - 1 }  ^ { 2 } + ( e ) _ { k - 1 } ^ { 2 } . } \end{array}
$$

Applying a series of orthogonal transformations to upper triangularize the first term in Eq. (5.11.33) yields the time update

$$
\begin{array} { r l } & { \overline { { J } } _ { k } = \left. \left[ \begin{array} { c c c c } { R _ { p } ^ { * } } & { R _ { p p } ^ { * } } & { R _ { p x } ^ { * } } & { R _ { p c } ^ { * } } \\ { 0 } & { \overline { { R } } _ { p p } ^ { * } } & { \overline { { R } } _ { p x } } & { \overline { { R } } _ { p c } ^ { * } } \\ { 0 } & { 0 } & { \overline { { R } } _ { x } } & { \overline { { R } } _ { x c } } \\ { 0 } & { 0 } & { 0 } & { \overline { { R } } _ { c } } \end{array} \right] _ { k } \left[ \begin{array} { c } { \mathbf { p } _ { k - 1 } } \\ { \mathbf { p } _ { k } } \\ { \mathbf { x } _ { k } } \\ { \mathbf { c } _ { k } } \end{array} \right] } \\ & { \qquad - \left[ \begin{array} { c } { \mathbf { b } _ { p } ^ { * } } \\ { \mathbf { \overline { { b } } } _ { p } ^ { * } } \\ { \mathbf { \overline { { b } } } _ { x } } \\ { \mathbf { \overline { { b } } } _ { c } } \end{array} \right] _ { k } \right. ^ { 2 } + ( e ) _ { k - 1 } ^ { 2 } . } \end{array}
$$

The $( ) ^ { * }$ quantities are not used for filtering but are necessary if smoothing is to be done following the filter ing. Hence, these quantities must be saved at each stage in the forward (filtering) sweep. Also, because c is a constant, it is unaffected by the mapping from $t _ { k - 1 }$ to $t _ { k }$ and need not be included in the time update procedure,

$$
\left[ \hat { R } _ { c } \hat { \mathbf { b } } _ { c } \right] _ { k - 1 } = \left[ \overline { { R } } _ { c } \overline { { \mathbf { b } } } _ { c } \right] _ { k } .
$$

We may now perform the measurement update on $\overline { { J } } _ { k }$ to obtain $\hat { J } _ { k }$ . This is accomplished by adding $\| \overline { \gamma } _ { k } \| ^ { 2 }$ (see Eq. (5.11.18)) and $( \epsilon _ { k } ) ^ { 2 }$ to $\overline { { J } } _ { k }$ given by Eq.

(5.11.34). Hence,

$$
\begin{array} { r } { \hat { J } _ { k } = \left\| \left[ \begin{array} { l l l } { \overline { { R } } _ { p } } & { \overline { { R } } _ { p x } } & { \overline { { R } } _ { p c } } \\ { 0 } & { \overline { { R } } _ { x } } & { \overline { { R } } _ { x c } } \\ { 0 } & { 0 } & { \overline { { R } } _ { c } } \\ { H _ { p } } & { H _ { x } } & { H _ { c } } \end{array} \right] _ { k } \left[ \begin{array} { l } { \mathbf { p } } \\ { \mathbf { x } } \\ { \mathbf { c } } \end{array} \right] _ { k } - \left[ \begin{array} { l } { \mathbf { \overline { { b } } } _ { p } } \\ { \mathbf { \overline { { b } } } _ { x } } \\ { \mathbf { \overline { { b } } } _ { c } } \\ { y } \end{array} \right] _ { k } \right\| ^ { 2 } } \\ { + \left\| \boldsymbol { R } _ { p _ { k } } ^ { * } \mathbf { p } _ { k - 1 } + \boldsymbol { R } _ { p p _ { k } } ^ { * } \mathbf { p } _ { k } + \boldsymbol { R } _ { p x _ { k } } ^ { * } \mathbf { x } _ { k } + \boldsymbol { R } _ { p c _ { k } } ^ { * } \mathbf { c } _ { k } - \mathbf { b } _ { p _ { k } } ^ { * } \right\| ^ { 2 } } \\ { + \left\| \boldsymbol { R } _ { w } ( \mathbf { p } _ { k + 1 } - \boldsymbol { M } _ { k + 1 } \mathbf { p } _ { k } ) - \mathbf { \overline { { b } } } _ { w _ { k } } \right\| ^ { 2 } + ( e ) _ { k - 1 } ^ { 2 } . } \end{array}
$$

Once again we can null the third term, $\| \overline { \gamma } _ { k } \|$ , by proper choice of $\mathbf { p } _ { k + 1 }$ ; hence, we do not have to deal with this term until we perform the time update to $t _ { k + 1 }$ . Notice that we can choose $\mathbf { p } _ { k - 1 }$ to null the second term. Later we will see that this is the smoothed value of $\mathbf { p } _ { k - 1 }$ .

A series of orthogonal transformations is now applied to Eq. (5.11.36) to yield

$$
\begin{array} { r l } & { { \hat { J } } _ { k } = \| [ \begin{array} { l l } { { \hat { R } } _ { p } \ { \hat { R } } _ { p x } \ { \hat { R } } _ { p c } } \\ { 0 \ } & { { \hat { R } } _ { x } \ { \hat { R } } _ { x c } } \\ { 0 \ } & { 0 \ } & { { \hat { R } } _ { c } } \end{array} ] [ \mathbf { c } ] - [ \begin{array} { l } { \mathbf { \hat { b } } _ { p } } \\ { \mathbf { \hat { b } } _ { x } } \\ { \mathbf { \hat { b } } _ { c } } \end{array} ] \| _ { k } ^ { 2 } } \\ & { \quad \quad \quad + \| R _ { p _ { k } } ^ { * } \mathbf { p } _ { k - 1 } + R _ { p p _ { k } } ^ { * } \mathbf { p } _ { k } + R _ { p x _ { k } } ^ { * } \mathbf { x } _ { k } + R _ { p c _ { k } } ^ { * } \mathbf { c } _ { k } - \mathbf { b } _ { p _ { k } } ^ { * } \| ^ { 2 } } \\ & { \quad \quad + \| R _ { w } ( \mathbf { p } _ { k + 1 } - M _ { k + 1 } \mathbf { p } _ { k } ) - \mathbf { \bar { b } } _ { w _ { k } } \| ^ { 2 } + ( e ) _ { k - 1 } ^ { 2 } + ( e ) _ { k } ^ { 2 } . } \end{array}
$$

This procedure of time and measurement updates is carried out until the desired number of observations has been processed.

After the $N ^ { \mathrm { t h } }$ measurement update the performance index is given by

$$
\begin{array}{c} \begin{array} { l } { { \hat { J } } _ { N } = \Sigma _ { N - 1 } + \left\| { \boldsymbol { R } } _ { p _ { N } } ^ { * } { \bf { p } } _ { N - 1 } + { \boldsymbol { R } } _ { p p _ { N } } ^ { * } { \bf { p } } _ { N } + { \boldsymbol { R } } _ { p x _ { N } } ^ { * } { \bf { x } } _ { N } + { \boldsymbol { R } } _ { p c _ { N } } ^ { * } { \bf { c } } _ { N } - { \bf { b } } _ { p _ { N } } ^ { * } \right\| ^ { 2 } } \\ { + \left\| \left[ \begin{array} { l } { { \hat { \boldsymbol { R } } } _ { p } \hat { \boldsymbol { R } } _ { p x } \hat { \boldsymbol { R } } _ { p c } } \\ { 0 \hat { \boldsymbol { R } } _ { x } \hat { \boldsymbol { R } } _ { x c } } \\ { 0 \ } & { \hat { \boldsymbol { R } } _ { c } } \end{array} \right] _ { N } \left[ { \bf { s } } _ { N } \right] - \left[ \hat { \bf { b } } _ { x }  \right\right\} \\ { { \bf { \hat { b } } } _ { c } } \end{array}] _ { N } | ^ { 2 }  \\ { + \displaystyle \sum _ { i = 1 } ^ { N } ( e _ { i } ) ^ { 2 } } \end{array}
$$

where

$$
\Sigma _ { N - 1 } \equiv \sum _ { i = 1 } ^ { N - 1 } \| R _ { p _ { i } } ^ { * } \mathbf { p } _ { i - 1 } + R _ { p p _ { i } } ^ { * } \mathbf { p } _ { i } + R _ { p x _ { i } } ^ { * } \mathbf { x } _ { i } + R _ { p c _ { i } } ^ { * } \mathbf { c } _ { i } - \mathbf { b } _ { p _ { i } } ^ { * } \| ^ { 2 } .
$$

The best estimate of the state at $t _ { N }$ is obtained from

$$
\hat { \mathbf { X } } _ { N } = \hat { R } _ { N } ^ { - 1 } \hat { \mathbf { b } } _ { N }
$$

where

$$
\begin{array} { r l } & { \hat { \mathbf { X } } _ { N } \equiv \left[ \hat { \mathbf { p } } \right] } \\ & { ~ \hat { \mathbf { X } } _ { N } \equiv \left[ \begin{array} { l } { \hat { \mathbf { p } } } \\ { \hat { \mathbf { x } } } \\ { \hat { \mathbf { c } } } \end{array} \right] _ { N } , ~ \hat { R } _ { N } \equiv \left[ \begin{array} { l l } { \hat { R } _ { p } \hat { R } _ { p x } \hat { R } _ { p c } } \\ { 0 } & { \hat { R } _ { x } \hat { R } _ { x c } } \\ { 0 } & { 0 } & { \hat { R } _ { c } } \end{array} \right] _ { N } } \\ & { ~ \hat { \mathbf { b } } _ { N } \equiv \left[ \begin{array} { l } { \hat { \mathbf { b } } _ { p } } \\ { \hat { \mathbf { b } } _ { x } } \\ { \hat { \mathbf { b } } _ { c } } \end{array} \right] _ { N } . } \end{array}
$$

The filter covariance is given by

$$
\begin{array} { r } { P _ { N } = R _ { N } ^ { - 1 } \ R _ { N } ^ { - T } . } \end{array}
$$

Since $\hat { R } _ { N }$ is upper triangular, $\hat { \mathbf { X } } _ { N }$ is obtained directly from a back substitution described by Eq. (5.2.8). If $\hat { P } _ { N } , \hat { \mathbf { x } } _ { N }$ , and $\hat { \mathbf { c } } _ { N }$ are used in the second term of Eq. (5.11.38), the smoothed value of $P _ { N - 1 }$ may be obtained. Note that it is not necessary to retain the first two terms of ${ \hat { J } } _ { N } $ if smoothing is not used.

# 5.11.2 SMOOTHING WITH A SRIF

Smoothing can now be done using Eq. (5.11.38) and the values of $\hat { \mathbf { X } } _ { N }$ given by Eq. (5.11.40). From the second term of Eq. (5.11.38) we have the smoothed value of $\mathbf { p } _ { N - 1 }$ based on $N$ measurements

$$
\hat { \mathbf { p } } _ { N - 1 } ^ { N } = { R _ { p } ^ { * } } _ { N } ^ { - 1 } \left[ \mathbf { b } _ { p } ^ { * } - { R _ { p } ^ { * } } _ { p } \hat { \mathbf { p } } _ { N } - { R _ { p x } ^ { * } } _ { N } - { R _ { p c } ^ { * } } _ { c _ { N } } \hat { \mathbf { c } } _ { N } \right] _ { N } .
$$

The smoothed value of $\mathbf { x } _ { N - 1 }$ is obtained from Eq. (5.11.31)

$$
\hat { \mathbf { x } } _ { N - 1 } ^ { N } = \Phi _ { x } ^ { - 1 } ( N ) \left[ \hat { \mathbf { x } } _ { N } - \Phi _ { p } ( N ) \hat { \mathbf { p } } _ { N - 1 } ^ { N } - \Phi _ { c } ( N ) \hat { \mathbf { c } } _ { N - 1 } ^ { N } \right]
$$

and c smooths as a constant,

$$
\hat { \mathbf { c } } _ { N } = \hat { \mathbf { c } } _ { N - 1 } ^ { N } = \hat { \mathbf { c } } _ { i } ^ { N } i = 1 , \ldots , N .
$$

Hence, the general expression for smoothing is given by

$$
\begin{array} { c } { \hat { \mathbf { p } } _ { i } ^ { N } = R _ { p i + 1 } ^ { * } \left[ \mathbf { b } _ { p } ^ { * } - R _ { p p } ^ { * } \hat { \mathbf { p } } _ { i + 1 } ^ { N } - R _ { p x } ^ { * } \hat { \mathbf { x } } _ { i + 1 } ^ { N } - R _ { p c } ^ { * } \hat { \mathbf { c } } _ { N } \right] _ { i + 1 } } \\ { { \phantom { \frac { 1 } { 2 } } } i = N - 1 , \dots , 1 \qquad } \end{array}
$$

where the $( \quad ) ^ { * }$ quantities have been saved at each value of $t _ { i }$ during the fil tering process. Also,

$$
\begin{array} { c } { { \hat { \mathbf { x } } _ { i } ^ { N } = \Phi _ { x } ^ { - 1 } ( i + 1 ) \left[ \hat { \mathbf { x } } _ { i + 1 } ^ { N } - \Phi _ { p } ( i + 1 ) \hat { \mathbf { p } } _ { i } ^ { N } - \Phi _ { c } ( i + 1 ) \hat { \mathbf { c } } _ { N } \right] } } \\ { { { } } } \\ { { i = N - 1 , \ldots , 1 . } } \end{array}
$$

The state transition matrices also are saved during filtering.

Although the procedure just outlined yields the smoothed solutions, it does not yield a smoothed covariance. To obtain the covariance we use the procedure for the filter time update and substitute for $\mathbf { x } _ { N }$ in terms of parameters at the $N - 1 ^ { \mathrm { s t } }$ stage; from Eq. (5.11.30),

$$
\begin{array} { r } { { \bf x } _ { N } = \Phi _ { x } ( N ) { \bf x } _ { N - 1 } + \Phi _ { p } ( N ) { \bf p } _ { N - 1 } + \Phi _ { c } ( N ) { \bf c } _ { N - 1 } . } \end{array}
$$

There is no need to substitute for $\mathbf { p } _ { N }$ because we already have $\mathbf { p } _ { N - 1 }$ available in Eq. (5.11.38) through the use of the data equation for the process noise parameters in the filt er sweep.

Substituting Eq. (5.11.48) into Eq. (5.11.38) yields

$$
\begin{array} { r l } { \hat { J } _ { N _ { 1 } } ^ { N } = } & { \displaystyle { \sum _ { i = 1 } ^ { N } ( e _ { i } ^ { \hbar } ) ^ { \prime } + \sum _ { k = 1 } ^ { N } } } \\ & { + [ [ \begin{array} { l l l } { \displaystyle { R _ { \mathrm { p } } ^ { k } } } & { \displaystyle { R _ { \mathrm { p } } ^ { k } + R _ { \mathrm { p } , i } ^ { \prime } \Phi _ { \mathrm { p } } ( N ) } } & { \displaystyle { R _ { \mathrm { p } , i } ^ { \prime } \Phi _ { \mathrm { x } } ( N ) } } & { \displaystyle { R _ { \mathrm { s p } } ^ { k } \Phi _ { \mathrm { c } } ( N ) + R _ { \mathrm { i s c } } ^ { \ast } } } \\ { \displaystyle { \hat { R } _ { \mathrm { p } } ^ { k } } } & { \displaystyle { \hat { R } _ { \mathrm { s p } } ^ { k } \Phi _ { \mathrm { p } } ( N ) } } & { \displaystyle { \hat { T } _ { \mathrm { p } , i } \Phi _ { \mathrm { x p } } ( N ) } } & { \displaystyle { \hat { T } _ { \mathrm { s p } } ^ { k } \Phi _ { \mathrm { x p } } ( N ) + \hat { T } _ { \mathrm { p } , i } } } \\ { \displaystyle { 0 } } & { \displaystyle { \hat { T } _ { \mathrm { s p } } ^ { k } \Phi _ { \mathrm { p } } ( N ) } } & { \displaystyle { \hat { T } _ { \mathrm { s p } } ^ { k } \Phi _ { \mathrm { x } } ( N ) } } & { \displaystyle { \hat { T } _ { \mathrm { s p } , i } \Phi _ { \mathrm { x c } } ( N ) + \hat { T } _ { \mathrm { s c } } } } \\ { \displaystyle { 0 } } & { 0 } & { \displaystyle { 0 } } & { \hat { R } _ { \mathrm { c } } } \end{array} ] } \\ &  \displaystyle  [ \begin{array} { l } { \displaystyle { \mathbb { P } _ { N } } } \\ { \displaystyle { \mathbb { P } _ { N - 1 } ^ { N } } } \\ { \displaystyle { \mathbb { R } _ { N - 1 } ^ { N } } } \\ { \displaystyle { \mathbb { C } _ { N - 1 } ^ { N } } } \end{array} ] - [ \begin{array} { l } { \displaystyle { \mathbb { P } _ { N _ { 1 } } ^ { k } } } \\ { \displaystyle { \mathbb { S } _ { P _ { 1 } } ^ { N } } } \\ { \displaystyle { \mathbb { S } _ { P _ { 1 } } ^ { N } } } \\  \displaystyle  \mathbb  S \end{array} \end{array}
$$

Because the smoothed value of c maps as a constant, we may drop the last row in the preceding matrix and use $\hat { R } _ { c }$ and $\hat { \mathbf { c } } _ { N }$ when needed. Applying a series of orthogonal transformations to the third term yields

$$
\begin{array} { c } { { \displaystyle \hat { J } _ { N - 1 } ^ { N } = \sum _ { i = 1 } ^ { N } ( e _ { i } ) ^ { 2 } + \Sigma _ { N - 1 } } } & { { \mathrm { ( S ~ ) } } } \\ { { \displaystyle ~ + \left\| \left[ \begin{array} { l l l } { { \displaystyle { R _ { p p } ^ { \prime } R _ { p } ^ { \prime } R _ { p x } ^ { \prime } R _ { p x } ^ { \prime } R _ { p c } ^ { \prime } } } } & { { \displaystyle { R _ { N - 1 } ^ { \prime } } } } \\ { { \displaystyle { R _ { p } \tilde { R } _ { p x } \tilde { R } _ { p x } \tilde { R } _ { p c } } } } & { { \displaystyle { R _ { N - 1 } \left[ \begin{array} { l } { { \hat { \bf x } _ { N } ^ { N } } } \\ { { \hat { \bf x } _ { N } } } \end{array} \right] } } } & { { \displaystyle { \left[ \begin{array} { l } { { \hat { \bf b } ^ { * \prime } } } \\ { { \bf { b } _ { p } ^ { \prime } } } \\ { { \hat { \bf b } _ { p } } } \\ { { \hat { \bf x } _ { N - 1 } ^ { N } } } \end{array} \right] } } } \end{array} \right] \right\| _ { { \displaystyle \hat { \cal T } _ { N - 1 } } } ^ { 2 } } }  \end{array}
$$

Solving for the state vector that minimizes $\hat { J } _ { N - 1 } ^ { N }$ yields the smoothes solution for the state. We may ignore the $( ) ^ { \prime }$ quantities because we already know the value of $\hat { \mathbf { p } } _ { N } ^ { N } = \hat { \mathbf { p } } _ { N }$ . The desired solution is

$$
\tilde { R } _ { N - 1 } \hat { \mathbf { X } } _ { N - 1 } ^ { N } = \widetilde { \mathbf { b } } _ { N - 1 }
$$

where

$$
\tilde { R } _ { N - 1 } = \left[ \begin{array} { l l l } { \tilde { R } _ { p } \tilde { R } _ { p x } \tilde { R } _ { p c } } \\ { 0 } & { \tilde { R } _ { x } } & { \tilde { R } _ { x c } } \\ { 0 } & { 0 } & { \hat { R } _ { c } } \end{array} \right]
$$

$$
\begin{array} { r } { \hat { \mathbf { X } } _ { N - 1 } ^ { N } = \left[ \hat { \mathbf { p } } _ { N - 1 } ^ { N } \right] , \qquad \hat { \mathbf { b } } _ { N - 1 } = \left[ \overset { \mathbf { \sim } } { \mathbf { b } } _ { p } ^ { \prime } \right] . } \\ { \hat { \mathbf { x } } _ { N - 1 } ^ { N } = \left[ \hat { \mathbf { x } } _ { N - 1 } ^ { N } \right] , \qquad \hat { \mathbf { b } } _ { N - 1 } = \left[ \overset { \mathbf { \sim } } { \mathbf { b } } _ { p } ^ { \prime } \right] . } \end{array}
$$

The smoothed covariance at $t _ { N - 1 }$ is given by

$$
P _ { N - 1 } ^ { N } = \tilde { R } _ { N - 1 } ^ { - 1 } \tilde { R } _ { N - 1 } ^ { - T } .
$$

Recall that the smoothed value of c never changes and is always the final filter value. Because the smoothed value of the state must also satisfy Eq. (5.11.48), we may substitute this into Eq. (5.11.50) in order to determine the smoothed state at $t _ { N - 2 }$ . Keep in mind that while we drop the $( ) ^ { \prime }$ terms, we must now deal with the $N - 1 ^ { \mathrm { s t } }$ term in $\Sigma _ { N - 1 }$ because it depends on the state at $t _ { N - 1 }$ and contains $\mathbf { p } _ { N - 2 }$ . Hence, the performance index $\hat { J } _ { N - 2 } ^ { N }$ becomes

$$
\begin{array} { r l } & { \hat { J } _ { N - 2 } ^ { N } = \Sigma _ { N - 2 } + \left\| \left[ \begin{array} { l l l } { R _ { p } ^ { * } R _ { p p } ^ { * } R _ { p x } ^ { * } R _ { p e } ^ { * } } \\ { 0 } & { \tilde { R } _ { p } } & { \tilde { R } _ { p x } \tilde { R } _ { p e } } \\ { 0 } & { 0 } & { \hat { R } _ { x } } \end{array} \right] _ { N - 1 } \right\| \mathbf { y } _ { N - 1 } } \\ & { \qquad - \left\| \mathbf { b } _ { p } ^ { * } \right\| _ { N } } \\ & { \qquad - \left\| \hat { \mathbf { b } } _ { p } \right\| _ { N - 1 } } \\ & { \qquad \left\| \mathbf { \tilde { b } } _ { x } \right\| _ { N - 1 } } \end{array}
$$

Substituting

$$
{ \bf x } _ { N - 1 } = \Phi _ { x } ( N - 1 ) { \bf x } _ { N - 2 } + \Phi _ { p } ( N - 1 ) { \bf p } _ { N - 2 } + \Phi _ { c } ( N - 1 ) { \bf c } _ { N }
$$

into Eq. (5.11.54) we obtain the $N - 2 ^ { \mathrm { n d } }$ stage of Eq. (5.11.49). Next we apply a series of orthogonal transformations to this equation to obtain the $N - 2 ^ { \mathrm { n d } }$ stage of Eq. (5.11.50). From this we obtain $\hat { \mathbf { X } } _ { N - 2 } ^ { N }$ and the associated covariance matrix. This procedure is repeated until the initial stage is reached. Notice that we have dropped the term

$$
\sum _ { i = 1 } ^ { N } ( e _ { i } ) ^ { 2 }
$$

in Eq. (5.11.54). This is the sum of squares of residuals from the filter sweep and is not affected by smoothing. We do not obtain a smoothed sum of squares of residuals during the backward sweep.

# 5.12 REFERENCES

Battin, R., An Introduction to the Mathematics and Methods of Astrodynamics, American Institute of Aeronautics and Astronautics, Reston, VA, 1999.

Bierman, G. J., Factorization Methods for Discrete Sequential Estimation, Academic Press, New York, 1977.

Carlson, N. A., “F ast triangular formulation of the square root filter”, AIAA J., Vol. 11, No. 9, pp. 1239–1265, September 1973.

Dyer, P., and S. McReynolds, “Extension of square-root fil tering to include process noise”, J. Optim. Theory Appl., Vol. 3, No. 6, pp. 444–458, 1969.

Gentleman, W. M., “Least squares computations by Givens transformations without square roots”, J. Inst. Math. Applic., Vol. 12, pp. 329–336, 1973.

Givens, W., “Computation of plane unitary rotations transforming a general matrix to triangular form,” J. Appl. Math., Vol. 6, pp. 26–50, 1958.

Golub, G. H., and C. F. Van Loan, Matrix Computations, Johns Hopkins University Press, 1996.

Graybill, F. A., An Introduction to Linear Statistical Models , Volume I, McGraw-Hill Series in Probability and Statistics, McGraw-Hill, New York, 1961.

Householder, A. S., “Unitary triangularization of a nonsymmetric matrix,” J. Assoc. Comput. Mach., Vol. 5, No. 4, pp. 339–342, October 1958.

Kaminski, P. G., A. E. Bryson, and S. F. Schmidt, “Discrete square root fil tering: A survey of current techniques”, Trans. Auto. Cont., Vol. AC-16, No. 6, pp. 727–735, 1971.

Lawson, C. L., and R. J. Hanson, Solving Least Squares Problems, Prentice-Hall, Inc. Englewood Cliffs, NJ, 1974 (republished by SIAM, Philadelphia, PA, 1995).

Tapley, B. D., and C. Y. Choe, “An algorithm for propagating the square root covariance matrix in triangular form,” Trans. Auto. Cont., Vol. AC-21, pp. 122–123, 1976.

Tapley, B. D., and D. S. Ingram, “O rbit determination in the presence of unmodeled accelerations,” Trans. Auto. Cont., Vol. AC-18, No. 4, pp. 369–373, August, 1973.

Tapley, B. D., and J. G. Peters, “A sequential estimation algorithm using a continuous $U D U ^ { T }$ covariance factorization,” J. Guid. Cont., Vol. 3, No. 4, pp. 326–331, July–August 1980.

Thornton, Thornton, C. L., Triangular covariance factorizations for Kalman filtering, Technical Memorandum, 33–798, Jet Propulsion Laboratory, Pasadena, CA, October 15, 1976.

# 5.13 EXERCISES

1. In Section 5.2 the algorithm for $\hat { x }$ is derived assuming the factorization

$$
M = R ^ { T } R
$$

(a) Rederive the algorithm assuming the factorization

$$
M = R R ^ { T }
$$

where $R$ is $n \times n$ upper triangular and

$$
\begin{array} { c } { M \hat { x } = N } \\ { R R ^ { T } \hat { x } = N } \\ { z \equiv R ^ { T } \hat { x } } \\ { R z = N . } \end{array}
$$

Answer:

$$
\begin{array} { r l } & { z _ { i } = \frac { \displaystyle ( N _ { i } - \sum _ { j = i + 1 } ^ { n } R _ { i j } z _ { j } } { R _ { i i } } \quad i = n , n - 1 . . . 1 } \\ & { \displaystyle \hat { x } _ { i } = \frac { \displaystyle ( z _ { i } - \sum _ { j = 1 } ^ { i - 1 } R _ { j i } \hat { x } _ { j } ) } { R _ { i i } } \quad } \\ & { \hat { x } _ { i } = \frac { R _ { i i } } { R _ { i i } } \quad i = 1 , 2 . . . n . } \end{array}
$$

2. Verify that the algorithm for $R$ in Exercise 1 is given by

$$
\begin{array} { l } { { \displaystyle R _ { j j } = \left( M _ { j j } - \sum _ { k = j + 1 } ^ { n } R _ { j k } ^ { 2 } \right) ^ { 1 / 2 } ~ j = n , n - 1 , \ldots 1 } } \\ { { \displaystyle R _ { i j } = \frac { \left( M _ { i j } - \sum _ { k = j + 1 } ^ { n } R _ { i k } R _ { j k } \right) } { R _ { j j } } ~ i = j - 1 , \ldots 1 } } \end{array}
$$

3. Using Eq. (5.2.6), find $R$ for

(a) The matrix $M$ given by

$$
M = \left[ { \begin{array} { r r r } { 1 } & { 2 } & { 3 } \\ { 2 } & { 8 } & { 2 } \\ { 3 } & { 2 } & { 1 4 } \end{array} } \right] .
$$

(b) Compute $R$ using the algorithm derived in Exercise 2. Note that these will be different matrices, thus illustrating the nonuniqueness of the matrix square root.

Answers:

Part (a)

$$
R = { \left[ 0 2 - 2 \right] }
$$

Part (b)

$$
R = \left[ \begin{array} { c c c } { { \displaystyle \frac { 1 } { 3 \sqrt { 3 } } \frac { 1 1 } { 3 \sqrt { 4 2 } } \frac { 3 } { \sqrt { 1 4 } } } } \\ { { 0 } } & { { 3 \sqrt { \frac { 6 } { 7 } } \frac { 2 } { \sqrt { 1 4 } } } } \\ { { 0 } } & { { 0 } } & { { \sqrt { 1 4 } } } \end{array} \right]
$$

4. Use the square root free Cholesky algorithm (Eqs. (5.2.11) and (5.2.12)) to determine the $U$ and $D$ factors of $M$ for problem 3,

$$
M = U D U ^ { T } .
$$

Answer:

$$
U = { \left[ \begin{array} { l l } { 1 { \frac { 1 1 } { 5 4 } } { \frac { 3 } { 1 4 } } } \\ { 0 \ 1 } & { { \frac { 1 } { 7 } } } \\ { 0 \ 0 } & { 1 } \end{array} \right] }
$$

$$
D = { \left[ \begin{array} { l l l } { { \frac { 1 } { 2 7 } } } & { 0 } & { 0 } \\ { 0 } & { { \frac { 5 4 } { 7 } } } & { 0 } \\ { 0 } & { 0 } & { 1 4 } \end{array} \right] }
$$

5. Given the function

$$
f ( t ) = \sum _ { i = 0 } ^ { 4 } a _ { i } t ^ { i } + \sum _ { i = 1 } ^ { 4 } A _ { i } \cos ( \omega _ { i } t ) + B _ { i } \sin ( \omega _ { i } t )
$$

where

$$
\begin{array} { r } { \omega _ { 1 } = \frac { 2 \pi } { 7 0 9 } , \quad \omega _ { 2 } = \frac { 2 \pi } { 3 8 3 } , \quad \omega _ { 3 } = \frac { 2 \pi } { 1 0 7 } , \quad \omega _ { 4 } = \frac { 2 \pi } { 1 3 } } \end{array}
$$

and given measurements of $f$ for $t = 0 , 1 , 2 , \ldots , 1 0 0 0$ , do the following:

(a) Estimate the constants $a _ { 0 }$ , and $a _ { i } , A _ { i } , B _ { i }$ for $i = { 1 , 2 , 3 , 4 }$ (b) Compare execution times and accuracy of the following four algorithms.

i. Cholesky decomposition ii. Givens transformation iii. Givens square root free transformation iv. Householder transformation

Generate your own perfect observations using the coefficients given:

Exact Coefficients:

$$
{ \begin{array} { l l l } { a _ { 0 } = - 5 0 } & & { a _ { 1 } = - 5 0 } \\ { a _ { 1 } = 0 . 2 5 } & & { A _ { 1 } = - 5 0 } & { B _ { 1 } = 1 0 1 } \\ { a _ { 2 } = - 0 . 6 2 5 \times 1 0 ^ { - 3 } } & & { A _ { 2 } = 1 } & { B _ { 2 } = - 0 . 5 } \\ { a _ { 3 } = - 0 . 4 \times 1 0 ^ { - 6 } } & & { A _ { 3 } = - 2 7 } & { B _ { 3 } = - 2 7 } \\ { a _ { 4 } = 0 . 9 \times 1 0 ^ { - 9 } } & & { A _ { 4 } = 4 } & { B _ { 4 } = - 3 } \end{array} }
$$

(c) Redo (a) after adding Gaussian random noise with mean zero and variance $= 2$ to the data.

6. From Eq. (5.10.120), derive Eqs. (5.10.123), (5.10.124), and (5.10.125), which define the covariance for the smoothed solution including process noise. (Hint: see Eqs. (5.10.114) through Eq. (5.10.117)).

7. Generate one cycle of a sine wave with an amplitude of unity. Add white noise, $N ( 0 , 0 . 0 5 )$ . Generate observation data by sampling the noisy sine wave 1000 times at equal intervals.

Using one process noise parameter, recover the sine wave using a SRIF both as a filter and a smoother. Try various combinations of $\tau$ and $\sigma$ in Eqs. (5.11.2) and (5.11.6). For example try a large $\tau$ and small $\sigma$ and estimate the amplitude as a constant (case 1). Try $\tau = 0$ and a very large $\sigma$ to simulate the sine wave as a white noise process (case 2). Try a random walk process to describe the process noise parameter (i.e., $m = 1$ , choose $q$ (case 3)). Finally find a value of $\tau$ and $\sigma$ that does a good job of replicating the sine wave (e.g., one for which the RMS of fit is near to the RMS of the noise on the data (case 4)). Assume a priori information, $\bar { p } = 0$ and $\overline { { P } } _ { 0 } = \infty$ and that the process noise, $\overline { { w } } = 0$ , at each stage. Use the algorithms described in Sections 5.11.1 and 5.11.2 for filtering and smoothing, respectively.

Generate the following figures for these four cases:

(a) Plot the observations and the filter solutions. Compute the RMS difference.   
(b) Plot the observations and the smoothed solutions. Compute the RMS difference.   
(c) Compute the RMS differences between the true sine wave (without noise) and the filter and smoothed solutions.   
(d) Plot the observations minus the smoothed solution.   
(e) Plot $w$ , the process noise.

For the optimal $\tau$ and $\sigma$ , the plots in (d) and (e) should look similar. The optimal $\tau$ and $\sigma$ result in the correlated signal in the observations being absorbed by $p$ and the random noise by $w$ .

\* Solution hints for Exercise 7.

The measurement update at the $i ^ { \mathrm { t h } }$ stage is given by performing an orthogonal transformation (Householder or Givens),

$$
T _ { i } \left[ \begin{array} { l } { \overline { { { R } } } _ { p _ { i } } \bar { b } _ { p _ { i } } } \\ { H \quad y _ { i } } \\ { 2 \times 2 } \end{array} \right] _ { 2 \times 2 } = \left[ \begin{array} { l } { \hat { R } _ { p _ { i } } \hat { b } _ { p _ { i } } } \\ { 0 \quad e _ { i } } \end{array} \right] _ { 2 \times 2 }
$$

where the equation number refers to the corresponding equation in the text.   
At the epoch time $\overline { { R } } _ { p _ { 0 } } = 0$ and $\bar { b } _ { p _ { 0 } } = 0$ are given.

Next, a time update to the $i + 1 ^ { \mathrm { s t } }$ stage results from a series of orthogonal transformations on

$$
T _ { i + 1 } \left[ \begin{array} { c c c } { - R _ { w } m } & { R _ { w } } & { \bar { b } _ { w _ { i } } } \\ { \hat { R } _ { p _ { i } } } & { 0 } & { \hat { b } _ { p _ { i } } } \end{array} \right] _ { 2 \times 3 } = \left[ \begin{array} { c c c } { R _ { p _ { i } } ^ { * } } & { R _ { p _ { i + 1 } } ^ { * } } & { b _ { p _ { i } } ^ { * } } \\ { 0 } & { \overline { { R } } _ { p _ { i + 1 } } } & { \bar { b } _ { p _ { i + 1 } } } \end{array} \right] _ { 2 \times 3 . }
$$

The $( \quad ) ^ { * }$ values must be saved for smoothing. Also,

$$
\begin{array} { l } { { \displaystyle R _ { w } = \frac { 1 } { \sqrt { q } } } } \\ { { \displaystyle m = e ^ { - ( t _ { i + 1 } - t _ { i } ) / \tau } } } \\ { { \displaystyle q = ( 1 - m ^ { 2 } ) \sigma ^ { 2 } } } \\ { { \displaystyle H = 1 ~ \mathrm { ( t h e ~ o b s e r v a t i o n ~ i s ~ } p ) } } \\ { { \displaystyle \overline { { P } } _ { 0 } = \infty } ; } \end{array}
$$

hence, $\overline { { R } } _ { p _ { 0 } } = 0$ and $\bar { b } _ { p _ { 0 } } = \overline { { R } } _ { p _ { 0 } } \bar { p } _ { 0 } = 0 .$ . The filter value of $p$ at each stage is

computed from

$$
\hat { p } _ { i } = \frac { \hat { b } _ { p _ { i } } } { \hat { R } _ { p _ { i } } } .
$$

After the final data point has been processed we may begin smoothing. The first smoothed value of $p$ is given by (assuming $N$ data points)

$$
p _ { N - 1 } ^ { N } = \frac { b _ { p _ { N } } ^ { * } - R _ { p _ { N } } ^ { * } \hat { p } _ { N } } { R _ { p _ { N - 1 } } ^ { * } } .
$$

The smoothed value of $p$ at the $i ^ { \mathrm { t h } }$ stage is given by

$$
p _ { i } ^ { N } = \frac { b _ { p _ { i + 1 } } ^ { * } - R _ { p _ { i + 1 } } ^ { * } \hat { P } _ { i + 1 } ^ { N } } { R _ { p _ { i } } ^ { * } }
$$

A value of $\hat { w } _ { i } ^ { N }$ may be determined from Eq. (5.11.13) by using the smoothed values of $p$ ,

$$
\hat { w } _ { i } ^ { N } = p _ { i + 1 } ^ { N } - m p _ { i } ^ { N } i = N - 1 , N - 2 , \ldots 0 .
$$

8. Work Example 4.8.2, the spring mass problem, using the square root free Givens method to solve for $\hat { \mathbf { x } } _ { 0 }$ and the associated estimation error covariance matrix. You should get results almost identical to those given in Example 4.8.2.
