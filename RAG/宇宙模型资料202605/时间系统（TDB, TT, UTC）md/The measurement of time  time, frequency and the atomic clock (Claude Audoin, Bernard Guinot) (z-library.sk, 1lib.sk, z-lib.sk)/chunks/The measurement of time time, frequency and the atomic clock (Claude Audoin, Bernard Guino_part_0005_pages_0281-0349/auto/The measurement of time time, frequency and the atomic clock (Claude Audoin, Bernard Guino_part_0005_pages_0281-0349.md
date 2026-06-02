# (b) Use of the equinox

Although the stellar angle $A _ { \mathrm { S } }$ is becoming more and more frequently used in practice,letusrecalltedevelopments based on the traditional origin in (C). This is the vernal equinox $\Upsilon$ ,the intersection between the equator and the ecliptic. The arc $\Omega \Upsilon$ is Greenwich Sidereal Time GST.It is related to UT1 in a much more complicated way than the stellar angle. It involves periodic terms that have to be subtracted to define the Greenwich mean sidereal time GMST. Then,according toan IAU decision [8.4,8.5], with the previous definition of $T _ { \mathrm { u } } ^ { \prime }$ and in seconds of hour angle, we find

$$
\begin{array} { r } { G M S T \mathrm { ~ \ a t ~ { ~ 0 ~ h ~ } ~ U T I } = 2 4 1 1 0 . 5 4 8 4 1 + 8 6 4 0 1 8 4 . 8 1 2 8 6 6 T _ { \mathrm { u } } ^ { \prime } } \\ { + 0 . 0 9 3 1 0 4 T _ { \mathrm { u } } ^ { \prime 2 } - 6 . 2 \times 1 0 ^ { - 6 } T _ { \mathrm { u } } ^ { \prime 3 } . } \end{array}
$$

The relation at arbitrary times is deduced in the same way as for $A _ { S }$

# 8.1.3 Other forms of Universal Time

It is sometimes necessary to estimate the Universal Time when the instantaneous position of the Earth's pole is not known. We then take $x = 0 = y$ at the time of estimate,and this leads to the form UTo.Thedifference $U T I - U T O$ is given by

$$
U T I - U T O = - ( x \sin L + y \cos L ) \tan \phi \ ,
$$

where $\phi$ and $L$ are the latitude and longitude (positive towards the east) of the observer,and $x$ and $y$ are the coordinates of the pole. At medium latitudes, this difference is less than a few hundrdths of a second.

There is also a regularised form of Universal Time, denoted UT2, which corrects for an annual irregularity.The difference $U T 2 - U T I$ varies between $\pm 3 0$ ms. UT2 does not represent the Earth's rotation any more than UTo does. Only UT1 has a physical meaning.

Also defined is UT1R,which is UT1 corrected for zonal tidal effectsafecting the polar moment of inertia and having periods less than 35 days. Corrections are less than $2 \mathrm { m s }$ Finally,U’ isorrectedfortheeectsofalltides, the main term having amplitude 0.16 s and period 18.6 years.

# 8.1.4 Measurement techniques

Until about 1970, our knowledge of the Earth's rotation was based entirely upon optical observation of the apparent motion of the stars relative to terrestrial reference directions. After a transition period of about ten years, this approach was superseded by methods using space geodesy techniques and interferometry.

Several of these new methods coexist. They provide complementary data for establishing the celestial and terrestrial reference frames and monitoring the five parameters that specify the Earth's rotation. But they are also competitive in certain domains where they lead to results of comparable quality. In the following brief review,we shall see that all these methods are based on time and frequency techniques.

# (a)Very long baseline radio interferometry (VLBI)

VLBI was first developed to study the structure of celestial radio sources. Around the beginning of the 198Os,it was used to measure the direction of these sources relative to a terrestrial baseline.

The measurement method involves receiving quasar radiation at centimetre and decimetre wavelengths using two antennas several hundred or several thousand kilometres apart. These antennas define the baseline. The characteristics of the radiation are recorded on magnetic tape as a function of the time given by clocks placed near the antennas.Let us assume that the clocks are synchronised. The magnetic tapes are compared and correlations sought between the signals received by the two antennas. The time lag between them can thus be found and.,if the distance between the antennas is known,the angle between the baseline and the source direction can also be determined (Figure 8.2).

When this method is implemented, clocks cannot be synchronised sufficiently accurately by external methods like the ones described in Chapter 5. They therefore remain independent and time comparisons have to be modelled, for example, by a second order polynomial in the time, throughout the period of the measurements to be treated in a single batch (often 24 hours). Model parameters, such as the coefficients of this polynomial. are left as unknowns to be deduced from the VLBI observations themselves. It is therefore essential to use clocks that are as stable in frequency as possible over sampling periods up to the duration of the relevant batch of observations,so that the model of their time difference involves a minimum of parameters. This explains why hydrogen masers are used,and indeed. this is one of their principal applications.

Likewise, the antenna coordinates are not known a priori. at least, not with suficient accuracy,and neither are the source positions. When observations of several sources are analysed globally using several baselines, the various unknown parameters can be fited. VLBI can supply allfive Earth rotation parameters and construct both celestial and terrestrial reference frames. However, the terrestrial frame is only obtained up to a translation. The centre of mass of the Earth is not located.

![](images/d8ca81df90b965456cb69471e83c6393be22b2a68815ddeec54603ac5bf6f35f.jpg)  
Fig.8.2. Astrometric use of VLBI. By measuring the geometrically produced time lag $\Delta t$ ,wecanfindtheorientationofthebasevector $B$ relative tothe sourcedirection.

The application of VLBI to astrometry and geodesy is coordinated by the International VLBI Service (IVS). We have already noted in Section 5.6.3c that clock comparisons could be a spin-off of VLBI if instrumental delays were measurable.

# (b) Dynamical methods

In VLBI, nature directly yields up the non-rotating celestial frame. The way is then open for geometry. For the methods considered here, observations refer to objects in orbit around the Earth,viz.,artificial satellites and the Moon. The non-rotating reference frame is realised by dynamical studies of the motion of such objects.Let us adopt a highly schematic approach in order to bring out the essential features of these so-called dynamical methods. We imagine that the Earth is spherical,homogeneousand isolated inspace,and thata satellite is deployed incircular orbit around it. The plane of the orbit has fixed orientation in space. In addition, the orbital period of the satellite is constant and can be measured with great accuracy by pursuing observations as long as necessary from various points on the Earth's surface. We can then identify fixed geocentric axes in the orbital plane and a non-rotating frame is thus established.

In practice,dynamical methods are extremely complex because significant perturbations have to be accounted for. These include the presence of neighbouring celestial bodies,irregularities in the shape and rotation of the geoid, residual friction effects,solar radiation pressure, and refraction in the Earth's atmosphere. All the corresponding problems have been resolved and dynamical methods now attain comparable accuracies to VLBI, wherever both approaches are applicable.

Dynamical methods can determine the Earth's polar motion, provide data concerning precession-nutation, and realise the terrestrial reference frame in relation to the centre of mass of the Earth (something VLBI cannot do). However, residual terms not included in corrections for the above-mentioned perturbations lead to a drift in UT1 values. This drift becomes more pronounced when perturbations to the satellite increase. It is very slow for the Moon,but not negligible. For this reason, these methods are well suited to studying short term variations in UT1. They can be categorised according to the object observedand the way it isobserved.

The coordinates of the pole were first obtained in 1967 by tracking satellites in the Navsat system using the Doppler effect. An improved version of this technique is the DORIS system developed by the Centre national d'études spatiales (CNES) in France and used to track Spot satellites, as well as the Franco-American TOPEX-POSEIDON oceanographic satelite.

For extremely precise applications, several spherical satellites were launched by France (Starlette,1975), the United States (Lageos,1976), then Japan and Russia. These are very dense in order to reduce the relative importance of non-gravitational perturbations and covered with retroreflectors. They are tracked by laser ranging and uncertainties in measured distances are of the order of one centimetre. Apart from their direct contribution to measuring the Earth's rotation and constructing the terrestrial frame, these satellites are of great importance in representing the geoid. This in turn is a major contribution to geophysics and al those techniques based upon precise orbitography of artificial satelites.It is unfortunate that laser telemetry is so expensive and sensitive to cloud conditions, because it is a very accurate method which can also be used for calibrations. An International Laser Ranging Service (ILRS) coordinates this activity.

The dynamical method which seems to be the most efficient involves tracking the twenty-four GPS satellites. Coordination and analysis of observations is the task of an International GPS Service (IGS) which produces outstanding results for the motion of the terrestrial pole and geodetic coordinates.

Three reflecting panels were deployed on the Moon from 1969 by Apollo astronauts, and two more (French made) by Soviet unmanned Lunakhod spacecraft. One was never relocated but the other four are used for laser ranging.This telemetry also achieves centimetre accuracy but remains a state-ofthe-art technique only mastered by two ground stations,in France and the United States, where observational data is regularly retrieved.For this reason, the method has not produced a global assessment of the Earth's rotation, only some useful values of UT1. It contributes rather to studies of the Earth-Moon system.

# (c) Coordination and results

Results obtained by each of these technical centres (IVS,DORIs,I,and IGS)are communicated to the IERS,where theyare combined.The IERS publishes,among other results,the final values for the five Earth rotation parameters,currently ona monthly and annual basis [8.6,8.7]. In 2ooO, uncertainties in the orientation of (I),on 5 day averages, were around $0 . 0 0 0 0 5 ^ { \prime \prime }$ relative to (T),i.e., $\pm 1 . 5 \ \mathrm { m m }$ for the position of the rotational pole at the surface of the Earth,and $0 . 0 0 0 2 ^ { \prime \prime }$ relative to (C). Uncertainties in $U T l - T A l$ ,also averaged over five days, were around $1 0 ~ \mu \mathrm { s }$

# 8.1.5 Irregularities in the Earth's rotation

If the Earth is treated as a rigid body, its rotational parameters are predictable once a very small number of initial conditions have been established by measurement. According to this hypothesis,the terrestrial pole would follow a circular motion with period 3o5 days,and its amplitude and phase would only need to be measured once. UT1 would vary linearly with time. Lunisolar precession-nutation, due to the effects of the Moon and Sun on the Earth's equatorial bulge,iscertainly a difficult theoretical problem inastronomybut it has been resolved with uncertainties well below those remaining in observations.Only one parameter would require observations, namely, the dynamical flattening of the Earth.

Discrepancies between observation and the theory of rotation of a rigid Earth arise from displacements in the fluid components of the planet,i.e.,atmosphere, oceans,and core, with respect to the lithosphere,and also elastic and viscous deformations of the so-called solid components. These displacements and deformations may cause rotational energy to be lost, as we shall see. In fact,certain irregularities are not yet well understood. Even when the basic mechanism has been ascertained, itis impossible to make quantitative predictions about their effects on the Earth's rotation. We shall restrict discussion to UT1. The reader interested in such geophysical phenomena should consult [8.8, 8.9].

# (a) Secular slowing of the Earth's rotation

The earliest available estimates of the length of day $D$ go back 400 million years.Various phenomena have recorded the diurnal, lunar and annual cycles. These phenomena are mainly the growth of corals and bivalves,and the laying down of sediments. The year is a duration that has remained practically unchanged,whereas variations in the lunation,expressed in uniform time,are fairly well known. By counting the number of days in the year and the lunation, it can be deduced that the length of one day has increased on average by about 2 ms per century.

This value agrees with what can be deduced from observations of eclipses in ancient times. The appearance of an eclipse is governed by orbital motions and therefore depends on the uniform Ephemeris Time (see Section 8.2). However, the place from which an eclipse is observed depends on the Earth's rotation. Since the size of this geographical shift is sometimes cause for surpise,we shall outline the way it is calculated.

For example, suppose that $D$ increases by $2 ~ \mathrm { m s }$ per century. From (8.5),

$$
\frac { \mathrm { d } \omega } { \mathrm { d } t } = - 5 . 3 5 \times 1 0 ^ { - 2 2 } \mathrm { r a d s } ^ { - 2 } .
$$

The integration in (8.2)iscarried outover thelast 2 years,puting $t \_ =$ $- 2 0 0 0$ yr, $t _ { 0 } = 0$ (the present),in two different ways.The first time we put $\omega = \omega _ { 0 }$ ,and the second,

$$
\omega = \omega _ { 0 } + \frac { \mathrm { d } \omega } { \mathrm { d } t } t \ .
$$

Taking the diference,it isobserved that thecumulated lag since the begining of Christianity is $4 . 1 \mathrm { ~ h ~ }$ The narrow band in which a solar eclipse would have been total at this epoch is thus shifted by $6 1 ^ { \circ }$ longitude towards the east, relative to what would have been calculated if UT1 had been uniform. Information about the Earth's rotation can thus be derived by studying the archives.

The secular slowing down of the Earth's rotation is mainly attributed to ocean tides. Rotational energy is lost in shallow seas. There is also energy transfer to the orbital motion of the Moon which,as aresult,is moving away from the Earth by about $4 \mathrm { c m }$ per year. Recent research has revealed significant dissipation in deep oceans [8.10].

# (b) Decennial fluctuations

The difference between UT1 and Ephemeris Time can be restituted over the past three centuries or so. Figure 8.3 shows the corresponding values of $D$ Fluctuationsare large enough to hide the secular variation.Thedetails of these fluctuations are becoming more and more clearly revealed. Since 1955,TAI has been available as a much better reference,but the period is too short to study variations with typical period of the order of ten years (inset in Figure 8.3). The origin of these fluctuations is still not well understood, but there is little doubt that they must be due to interaction between the Earth's fluid core and its rigid mantle. Another contribution may also arise from the oceans. They remain totally unpredictable. It is observed that they lead to relative fluctuations in $D$ ， and hence in the length of the UT1 second, with magnitude reaching about $1 0 ^ { - 7 }$

![](images/f2999ce165b4eb72b620f143b5ed5fb228db5e22207d6f6ef917c42edeca9ffa.jpg)  
Fig.8.3. Fluctuations in the length of day $D$ ,measured in seconds of Ephemeris Time upuntil1955 (from[8.11]),then inatomic seconds (inset). Thesloping straight line represents the secular slowing of the Earth's rotation.

# (c) Short term fluctuations

Figures 8.4 and 8.5 show fluctuations in UT2 and $D$ with the best temporal resolution that can be achieved. These fluctuations are essentially due to atmospheric motions, via angular momentum exchange with the solid Earth. An annual component is recognisable in Figure 8.5.For the main part, this component has been subtracted from the curve in Figure 8.4.

![](images/34081e36fdfc1427f5146e1c9abe6c6f5aecae1719dc8ab9a5f173f811e4b7dc.jpg)  
Fig.8.4. Observed values of Universal Time,after subtracting an annual variation, periodic terms due to tides and a linear function of time. The details are real fluctuations, not observational errors. (Figure kindly communicated by the IERS.)

# (d) Frequency instability of Universal Time

The frequency instability of Universal Time is shown in an approximate way in Figure 8.7,at the end of this chapter. In the very long term,it is dominated by secular slowdown of the Earth's rotation.

# 8.1.6 Use of Universal Time

UT1 is used to adjust Coordinated Universal Time, which requires very little precision. When the utmost accuracy is involved, one of its main uses is to provide a link between celestial and terrestrial frames as a function of TAI (see Section 3.3.2b). It is then used in combination with the other four Earth rotation parameters. These parameters also have an intrinsic value to geophysics. Although it is hardly satisfactory to isolate the factors contributing to a description of the Earth's rotation, we shalladd a few brief comments on each.

The non-rotating celestial frame serves to establish dynamical models of the motions of bodies in the Solar System, whether they be natural or artificial,using observations relative to this frame.This produces an ephemeris for the object in question, which allows its position to be predicted. Of course, the existence of this frame in the radio domain of VLBI is not always helpful, practically speaking.But it has been extended to the visible by fixing the angle and angular velocity of the frame formed by 10o ooO stars in the programme of the astrometric satelite HIPPARCOS [8.12,8.13,8.14, 8.15]. This wasachieved by observing stars that radiate in both the radio and visible regions of the spectrum. The ephemerides of the planets and their satellites,as well as space probe orbitography,are crucial to exploration of the Solar System. In addition,astrophysicists find it useful to know the proper (angular) motions of the stars relative to a non-rotating frame.

![](images/7b6c1434eb30157875c9634475b134f62d669ab867fcb8d00db2c00823c37891.jpg)  
Fig.8.5.Fluctuations in the length of day $D$ in (atomic)millseods,fterig fortheeffects of short term zonal tides.(Figure kindly communicatedby the IERS.)

A highly accurate, homogeneous terrestrial frame has only recently been established. In 1984,the Bureau international de I'heure undertook to publish the coordinates it had adopted for sites used to observe the Earth'srotation,thereby creating a first outline of what was to become the ITRF.National and regional geodetic networks, which may manifest differences of more than $1 0 0 ~ \mathrm { m }$ from one to another,are in the process of being fited to the ITRF.This unification is all the more useful in that the Global Positioning System is based upon a system very close to the ITRF (to within a decimetre) and hence supplies coordinates in this frame. The centimetre accuracy of the ITRF provides a reference in which tectonic deformations can be studied, whether they be large scale motions associated with the tectonic plates,or localised motions in critical regions.

As regards the terrestrial rotation parameters, their importance in geophysics is clear from their unpredictability. Their variations do not always lead unambiguously to a geophysical model. Conversely,however, they give constraints that can lead to rejection of models whose predictions fall too wide of the mark.These parameters also have geometrical importance when transforming coordinates between the celestial and terrestrial systems.For example, VLBI observation of a space probe yields its direction referred to the Earth. In order to organise a rendezvous with another planet, corrections must be made to its path,and this requires knowledge of its position relative to the celestial frame. In this example, the Earth's rotation parameters must be known in real time, which is only possible by prediction. The example shows why good values for these parameters are needed at short notice if the uncertainties of prediction are to be minimised. The IERS has a Rapid Service (in the USA),responsible for predicting the Earth rotation parameters.

# 8.2 Ephemeris Time

# 8.2.1 Definition

The conceptual definition of Ephemeris Time ET was given in Chapter 4. It is a form of classical dynamical time.The unit and origin of ETare conventionally defined by adopting a numerical expression for the geometric mean longitude of the Sun established by Newcombiz.,

$$
L = 2 7 9 ^ { \circ } 4 1 ^ { \prime } 4 8 . 0 4 ^ { \prime \prime } + 1 2 9 6 0 2 7 6 8 . 1 3 ^ { \prime \prime } T + 1 . 0 8 9 ^ { \prime \prime } T ^ { 2 } \ ,
$$

where $T$ is counted in Julian centuries of 36525 ephemeris days.The origin of $T$ is at the beginning of the year 1900,at the instant when the geometric mean longitude of the Sun took the value $2 7 9 ^ { \circ } 4 1 ^ { \prime } 4 8 . 0 4 ^ { \prime \prime }$ This instant of time is dated 1900 January O,12 h ET exactly (decision taken by the IAU in 1958).

For those readers unfamiliar with astronomical terminology, let us review briefly. The longitude of the Sun is measured along the ecliptic from the vernal equinox. The later is the intersection of the ecliptic and the equator and moves in space because of the motion of these two planes. Its motion in the ecliptic is traditionally described by two types of terms, namely, those represented by a polynomial function of time (secular terms),and those represented explicitly by periodic functions.The adjective ‘mean’ refers to the fact that periodic terms have been subtracted of. Likewise,the Sun’s motion in the ecliptic,as seen from the Earth, involves periodic components due to the eccentricity of the Earth's orbit together with perturbations from the other planets and the Moon,and a (very small)secular component. Only the secular terms remain in the mean longitude.

Concerning the adjective ‘geometric',this refers to the problem of aberration.We see the Sun in the position itoccupied about 8 minutes earlier, the time required for its light to reach us.This is its apparent position.The geometric position is corrected for this delay.

Expression (8.14) contains the definition of the second of Ephemeris Time which is in fact based upon the speed in longitude at $T = 0$ The official definition given in Section 4.3.3 was adopted to bring out a fraction of a duration, but it appeals to Ephemeris Time itself,and this is not defined.The value of this fraction is found by calculating the length of the tropical year in seconds from (8.14), as $L$ increases by $3 6 0 ^ { \circ }$ ,putting $T \simeq 0$ in the $T ^ { 2 }$ term.

# 8.2.2 Determining Ephemeris Time

Ephemeris Time was designed and used before atomic time had come into existence,oratleast,eore ithadbcome widelyccepted inheatronomical community. We must therefore place ourselves in this context.

Expression (8.14) can be viewed as the primary definition of ET. The corresponding determination consists in measuring the longitude of the Sun at an instant of time that the observer dates $\tau _ { \mathrm { C } }$ with his or her clock C.From the longitude measurement, ET is deduced using (8.14) and we thus obtain $E T - \tau _ { \mathrm { C } }$ As the uncertainties in UT1 were much smaller than those in ET, the result was given a universal character by specifying

$$
\Delta T = E T - U T I \mathrm { a t o b s e r v a t i o n d a t e } .
$$

The slowness in the variation and lack of precision in $\Delta t$ allowed a great deal of freedom in the choice of reference scale used to date the measure.

In order to measure its longitude, the Sun had to be situated relative to the stars on the sky background. Clearly, this could not be done directly.What was possible,however,was todate solar and stellar transits of the meridian in U1 and use the Earth's angular velocity to deduce the difference between their right ascensions.Measuring their zenithal distances during these transits gave differences of declination needed to evaluate the longitude of the Sun. Many corrections were needed. One was for aberration,as we have seen,but there was also a correction for parallax, since the longitude in (8.14) is geocentric, and corrections for yet other astronomical phenomena. In fact, this primary determination of ET is extremely difcult and also very imprecise. If we assume that the likely uncertainty in $L$ is $0 . 5 { ^ { \prime \prime } }$ ,the corresponding uncertainty in ET from observation of the Sun is $1 0 ~ \mathrm { s } .$ Ifwe hope to measure a time interval in ET by two observations of the Sun, with relative uncertainty of $1 0 ^ { - 8 }$ ,these observations must be made more than 50 years apart.

Other approaches had therefore to be explored. Astronomers who set up geocentric ephemerides, giving angular positions and distances of bodies in the Solar System, had to choose the unit and origin of their time parameter so that it satisfied the condition expressed by (8.14). Once this.was done,all such ephemerides had ET as their argument.In principle, observation of any of these bodies gave access to ET,with a possible gain in precision. The fact nevertheless remained that this way of finding ET depended on a sort of calibration via solar observations.

The faster the orbital motion of the observed body, the greater is the precision in ET. In this respect, the Moon is the most suitable object. Unfortunately, the motion of the Moon is perturbed by the Earth's rotation (see Section 8.1.5a). Its mean geocentric angular velocity (or mean motion) is gradually slowed down ina way that can only be ascertained by observation. Variations in the Moon's mean motion could only be obtained if ET was first determined via observations of the Sun and planets. After this delicate calibration exercise,which required decades of tedious work,the Moon could then be used as a practical way of obtaining ET. The Moon was a kind of secondary clock that allowed greater precision in readings, but at the risk of introducing systematic errors that would increase with time,stemming from some error in its calibration.

To guarantee a unique realisation of ET, the IAU recommended the use of a specific lunar ephemeris and the notation $\operatorname { E T } j$ , where the suffix $j$ indicates the one chosen. (From 1960 to 1984, $j = 0$ , 1, 2 were used.)

The Moon's motion against the star background was measured by observing occultations of stars by the Moon, or else by using photographic methods. Large scale observation campaigns were organised at the end of the 1950s. Despite the considerable effort put in, these techniques still gave uncertainties of several hundredths of a second in annual averages of $\Delta T j = E T j - U T I$ When TAI was set up,these determinations of ET came to an end, for it was simpler to adopt

$$
E T - T A I = 3 2 . 1 8 4 \mathrm { ~ s ~ } ,
$$

a conventional constant value based on observation.

# 8.2.3 Difficulties and current solutions

Apart from the uncertainties mentioned in Section 8.2.2,large systematic errors affected ET.It was very sensitive to the way thecelestial coordinate system was realised and also to the values adopted for various astronomical constants.

For example,catalogues giving positions and proper motions of stars,and realising anon-rotating geocentric frame (earlier forms of the frame (C) discussed in Section 8.1.1),hadtobe revised several times due to improved measurements and also because uncertainties in proper motions degrade accuracy as time goes by.Each revision caused ET to jump.To illustrate the part played by the astronomical constants, we may consider the aberation constant relating the mean longitude in (8.14) to the observed apparent longitude. The change in recommended value applied by the IAU in 1968 led toa jump of $0 . 6 s$ in ET.

In 1994, to overcome the diffculties inherent in defining ET by means of the solar longitude, the IAU simply recommended that the realisation of Terrestrial Time TTdefined in Section7.1.2 be extendedbackwards in time tothe periodbefore1955,via the dynamics of theSolar System.Indeed,theTTscale unit has duration equal to that of the atomic second on the rotating geoid and thelater was defined in such a way as to agree with the best available determination of the ephemeris second. Moreover, the origin of TT was chosen to give continuity with ET. Hence,replacing ETby TTdoes not lead toany great discontinuity in the construction of the ephemerides.

In this modern application of the Ephemeris Time concept, which allows for relativistic dynamics,the scale unit is fixed by the present atomic definition of the second, and the origin by relation to International Atomic Time. Each ephemeris $k$ nevertheless leads to a different approximation $\mathrm { T T } ( k )$ of TT that must be clearly stated (IAU Resolution C7,1994).

In Section 4.3.4, we mentioned the rather historical role played by ET. Figure 8.7 gives some idea of its frequency stability.

# 8.3 Pulsar Time

Pulsars were first observed in 1967 [8.16]. These objects send out radio pulses at regular intervals. It is thought that they are stars composed mainly of neutrons in a state of ultimate compression and emitting a beam of radiation in a fixed direction relative to the matter within them. The pulses of radiation received here on Earth are thus witness to their rotation.

All pulsars discovered between 1967 and 1982 have rotation periods of the order of one second. The frequency at which their pulses arrive on Earth is affected by changes in distance between the pulsar and the observer,and in particular, by the Earth's orbital motion. After correcting and referring to the atomic time scale, relative frequency instabilities for these pulses lie in the range $1 0 ^ { - 1 0 }$ to $1 0 ^ { - 1 1 }$ .However,in1982,astronomersaddedanother category of pulsars to their collection of celestial objects. These were the millisecond pulsars, with periods of a few milliseconds. The diameters of these objects are estimated at about $2 0 ~ \mathrm { k m }$ and their masses at around 1.4 times the mass of the Sun. The first was discovered by D.C. Backer and his team using a huge fixed radio antenna, $3 0 0 \mathrm { m }$ in diameter, at Arecibo in Puerto Rico [8.17]. This pulsar $\mathrm { P S R } 1 9 3 7 { + } 2 1$ has a period of $1 . 6 ~ \mathrm { m s }$ . The shape of its pulses is shown in Figure 8.6. It was soon realised that the arrival of pulses from PSR1937+21 could be dated relative to TAI with an uncertainty of a few tenths of a microsecond.In addition,once the gradual slowdown in its rotation had been taken into account, it had a long term frequency stability at least as good as that of the best atomic clocks running at the time (instabilities of $1 0 ^ { - 1 4 }$ or less over one year). Several dozen other millisecond pulsars were subsequently discovered, some of them being components of multiple star systems. An international programme was set up to time pulse arrivals. Observations were made at frequencies of the order of $1 \ \mathrm { G H z }$ , using large radio antennas. The power collected is very low,of the order of $1 0 ^ { - 1 6 }$ W with the largest antennas $^ \dagger$ This programme does not require continuous observation. The frequency stability of both the pulsars and TAI is such that observations may be interrupted for periods of a few weeks or months without risk of losing a single period.

![](images/8977c63ccf6d986e2bee9607b95f062b4c35ce5a87007b7b1658205b4c81a460.jpg)  
Fig. 8.6. Mean shape of pulses from the pulsar PSR1937+21. The presence of an intermediate pulse suggests that the magnetic axis of the pulsar is perpendicular to the axis of rotation.

Some have suggested that millisecond pulsars will bring time measurement back within the province of astronomy. However, this would be to forget the spin-down effect just mentioned, which rather limits the usefulness of measuring time by pulsar rotation. In the case of PSR1937+21, for example, the period $P$ increases by $1 0 . 5 \times 1 0 ^ { - 2 0 }$ s per second,sothatinrelative vlues

$$
\frac { 1 } { P } \frac { \mathrm { d } P } { \mathrm { d } t } = 7 \times 1 0 ^ { - 1 7 } ~ \mathrm { s } ^ { - 1 } ~ .
$$

This relative spin-down is ten times greater than the same for the Earth. Although it is thought that $\mathrm { d } P / \mathrm { d } t$ is constant,its value cannot be knownaiori with sufficient accuracy to rival the frequency accuracy of atomic clocks.There is afurther problem. The rotational phase of the pulsar must be transferred to Earth and uncertainties enter as a result of the relative motion of observer and source.For example,observations depend on the position of the pulsar,because of the orbital motion of the Earth,and its position cannot be determined accurately enough. In addition,pulsars have their own proper motion,and possibly orbital motion if they are in binary systems. There may also be fluctuations in propagation times if the signal crosses ionised media in space. For these reasons, pulsar rotation cannot be made the basis for defining a time unit,and nor can it be used as a clock to realise the time scales, e.g., TCG,used in the theory.

As a consequence of the slowing rotation and instabilities introduced when evaluating variations in the propagation time, we must reconsider what is meant by the frequency instability of a pulsar. In the following,the intrinsic instability will be taken to mean the hypothetical instability after making ideal corrections for the constant $\mathrm { d } P / \mathrm { d } t$ ,as it would be observed in a frame moving with the pulsar. It is this intrinsic instability that is considered to be smaller than the frequency instability of atomic clocks.

We may then imagine the possibility of calibrating pulsar clocks using atomic clocks,by determining their frequency drift over a time interval of duration $I$ .We might be able to use these to improve the frequency stability of TAI retrospectively for sampling periods shorter than $I$ ,by forming a mixed time scale [8.18]. Unfortunately, random uncertainties in pulse arrival times require $I$ to be very long. For example, if atomic time has a frequency instability of $1 0 ^ { - 1 4 }$ over one year, then with the help of the pulsar giving the most suitable pulses that can be dated to within $0 . 3 ~ \mu \mathrm { s }$ , we can only hope for better stability in the mixed scale when sampling times lie between one year and $I$ .Recent advances with atomic clocks would mean extending $I$ to several decades,which seems to spell the end for this idea. A Pulsar Time has nevertheless been envisaged. It would be constructed by means of an algorithm combining observations of a group of pulsars whose comparison with atomic time might in the long run lead to new discoveries [8.18].

A rather different contribution of millisecond pulsars to time measurement has also been studied. By measuring the Doppler effect, the timing of these pulsars provides the Earth's position on its orbit and hence leads to a new measure for Ephemeris Time. There is much greater precision in readings, compared with observations based upon the definition (8.14) of Ephemeris Time in terms of the Sun's longitude. Frequency stability is also improved for sampling periods less than six months. But in the long term, which is the most important, nothing is gained over traditional observation methods [8.18].

![](images/fab087dbe3bddca0b6adc049e2f7b61a7df90644c8419898dc39aa7f83bdb80c.jpg)  
Fig. 8.7. Instability of astronomical time scales and TAI: ET and $\operatorname { E T } j$ are ephemeris time scales set up by observing the Sun and Moon,respectively; UT is Universal Time; TP(PSR1937+21) is time based on the rotation of the named pulsar; TBP is time based on the orbital motion of a binary pulsar (optimal case). Concerning TAI, properties for 1998 are projected into the future. This figure is based upon elements from [8.18] and [8.21].

A third method for measuring time based on pulsars consists in monitoring the orbital motion of a pulsar with abinary companion,by observing the Doppler effct.The theory for such motions is exceedingly complex,because gravitational fields arevery strongand effects of gravitational waves are significant. However, it can be developed.The question remains as to whether a dynamical time scale based on this motion can rival atomic time. In the study [8.18],the authors reach the following conclusion.Thediscovery,observation and interpretation of binary pulsars might have occurred before the emergence of atomic clocks (since quartz clocks would have been sufficient for this purpose),and in this case, binary pulsar time would have been a good candidate for replacing Ephemeris Time. However, this measure of time cannot take the place of atomic time, which has greater accuracy and stability.

It thus seems likely that millisecond pulsars will provide neither a unit of time nor the time we read on our clocks. Notwithstanding, up until now, instabilities in International Atomic Time have to some extent limited the quality of scientific results that can be obtained by timing pulsars.Indeed,this is what justifies the retrospective calculation of more accurate and stable atomic time scales than TAI, as discussed in Section 7.4.3. New frequency standards may render the imperfections in atomic time negligible,but only time will tell.

Pulsar timing is the most demanding application of atomic time scales,with regard to their accuracy and their long term stability (over six months or more). It is bringing new results in astrometry,Solar System dynamics and the theory of gravitation itself. The timing of binary pulsars has indirectly confirmed the existence of gravitational waves,predicted by general relativityand it has thereby strengthened confidence in the theory [8.19, 8.2O]. This research was rewarded by the Nobel Prize for Physicsin 1993,attributed to R.A. Hulse and J.H. Taylor.

Frequency instabilities in times related to pulsars are illustrated in Figure 8.7.The figure gives a rather qualitative overview of the problem. For astronomical times,it gives only the likely orders of magnitude.For atomic time, it assumes that characteristics of standards will remain at the same level.

# 9

Ultraprecise time and frequency applications

Whether it concerns frequencies or times on clocks, time measurement is omnipresent today. An ordinary wristwatch used to organise our everyday activities is a precision instrument. Driven by a quartz crystal, its frequency instability over one day may be less than $1 0 ^ { - 7 }$ . Some watches are even servo controlled by time signals which are themselves linked to the best caesium standards.We may thus wear an instrument whose frequency remains accurate to a few parts in $1 0 ^ { - 1 4 }$ providedthatweveaeillonsofso own houses, we are surrounded by time and frequency sources: time switches, computer clocks,radio receiver oscillators, cordless phones,and so on. Many systems and services depend on time: telecommunications,television, electricity distritonig

It would be an interesting exercise tochoose a relative frequency inaccuracy, say $1 0 ^ { - 1 0 }$ ,and determine which activities would become impossible if no frequency standard were able to go beyond this limit. It is clear that the Global Positioning System and its host of applications could not exist. International Atomic Time would not exist either, since astronomy would have retained control over the world’s time scales. Space geodesy would not be precise enough to make a contribution to geophysics. The same exercise could be carried out at different levels of accuracy. Unfortunately, we must admit that we are unable to provide exhaustive consideration of the different cases. We can only invite the reader to reflect upon the historical evolution of techniques, particularly those concerned with space and telecommunications, where time measurement is a key element.

As an example, we shall examine several applications of time measurement using the best standards, either the most accurate ones, or the most stable for various sampling periods, or again those providing a good compromise between accuracy and stability on the one hand,and reliability on the other. Indeed, in a great many applications, we must accept a slight degradation with respect to the quality of laboratory standards if we are to obtain reliable and convenient instruments.For such applications,commercially manufactured rubidium and caesium clocks have been produced in their thousands,and even hydrogen masers are sometimes used.

What is the purpose of all these instruments? Their main use centres upon three different operations. The first is the measurement of time intervals and frequencies,for example, when measuring distances by radar or laser ranging. The second arises when systems are based on clock synchronism,as in the case of the Global Positioning System,oron equality of frequencies (syntonisation). The last occurs when a time scale is used to represent the time in some physical theory,for example when modelling the orbits of satellites and planets.However,this way of breaking time measurement down into different categories cannot serve as a basis for systematic presentation of the subject, for the categories tend to overlap.We shall therefore illustrate our discussion by selecting some practical and scientific themes which involve time measurement in characteristic ways.

# 9.1 Fundamental research

# 9.1.1 Metrology

The second is by far the best realised of the base units in the International System of Units (SI units). It is therefore quite natural to define the other base units in terms of the second using only the laws of physics and the fundamental constants they involve. By accepting the postulate that such constants do inded exist (i.e.,Einstein’s principle of equivalence),all the accuracy in the realisation of the second is thereby,in principle,carried over to the other units. This was the step taken in 1983,when the definition of the metre was based on the speed of light. Of the seven base units in the International System (see Appendix 3), there are now only three that remain independent, viz., the second, the kilogram and the kelvin. For example the definition of the ampere is based upon the notion of force in $[ \mathrm { m } \mathrm { k g } \mathrm { s } ^ { - 2 } ]$ and distance in [m] between two conductors. This definition refers in the end to the second and the kilogram.

A significant advance would be made if the kilogram could be defined in terms of the second. The present definition based upon the mass of a particular object,a cylinder of platinum-iridium alloy kept at the BIPM, gives rise to a relative uncertainty barely less than $1 0 ^ { - 8 }$ .It may be possible to achieve this via electromagnetic or electrostatic forces.All measures,apart from those appealing to thermodynamics,would then be related to the second.

This process whereby the measure of a quantity is transposed into a measure of time also applies to voltages using the Josephson effect, and to electrical resistances, via the quantum Hall effect. However, these quantum effects cannot serveas a basis for new definitions of the units used in electricity,at least, not for the moment,because the link with mechanical units would then be lost: the mechanical watt must remain equal to the electrical watt. For the time being, they are used to maintain the values of the volt and the ohm,with these values still being related to the definition of the ampere.

The Josephson effect occurs when two superconductors are separated by a very thin insulating barrier. When subjected to ultrahigh frequency radiation of frequency $\nu$ ,this junction exhibits a stair-shaped current-voltage characteristic,levelling out at specific values $V _ { n }$ of the applied potential difference. These are given theoretically by the relation

$$
V _ { n } = n \frac { h } { 2 e } \nu ~ ,
$$

where $n$ is a whole number, $h$ is Planck's constant and $e$ is the electron charge.

The uncertainty in the measurement of the ratio $h / 2 e$ afforded by the above equation is smaller than the uncertainty arising when $h$ and $e$ are found by separate experimental determinations. In 1988, following an international campaign of measurements,a conventional value denoted $K _ { \mathrm { J } }$ was adopted for $h / 2 e$ .This is given by

$$
K _ { \mathrm { J } } = 4 8 3 5 9 7 . 9 \mathrm { G H z V ^ { - 1 } } .
$$

This provides a stable reference for potential differences,tied to afrequency measurement.

The quantum Hall effect, aiso known as the von Klitzing effect, occurs when a thin semiconducting layer is cooled to about $1 \mathrm { \textrm { K } }$ and subjected to a magnetic field of the order of $1 5 \mathrm { T }$ perpendicular to the layer. The Hall voltage $V _ { \mathrm { { f } } }$ which is orthogonal to the direction of the applied current $I$ , behaves in such a way that the resistance $R = V _ { \mathrm { t } } / I$ is given theoretically by

$$
R = \frac { 1 } { n } \frac { h } { e ^ { 2 } } \ ,
$$

where $n$ is once again a whole number. Experimental determination of the quantum Hall resistance yields a value for $h / e ^ { 2 }$ that is more precise than can be obtained from separate determinations of $h$ and $e$ ,and in 1988, a conventional value $R _ { \mathrm { { K } } }$ was adopted for this ratio, viz.,

$$
R _ { \mathrm { K } } = 2 5 8 1 2 . 8 0 7 \Omega .
$$

Since the beginning of the 1990s,it has been possible to send electrons one by one through a potential barrier. It has therefore become feasible to create an electric current whose intensity would be determined by the frequency of the signal controlling the opening of the barrier.It would then be possible to check the mutual consistency of methods for determining the electrical units,since the intensity of a current is also related to the quantity frequency through the Josephson and quantum Hall effects.

The conventional values of $K _ { \mathrm { J } }$ and $R _ { \mathrm { { K } } }$ implicitly define electrical units that do notstrictly conform tooficial SIunits.However,they have the advantage of providing a uniform representation of the volt and the ohm with far greater reproducibility than can be had from absolute determinations based upon the definition of the ampere.

# 9.1.2 Measuring physical constants

Some constants can be determined simply by measuring the frequency of a physical phenomenon,and their values can therefore beobtained with very low uncertainty.

The Rydberg constant is an example. It has been ascertained to within $7 . 7 \times 1 0 ^ { - 1 2 }$ This resultis theoutcomeof work carred outby teams at theEcole normale supérieure in Paris (France)and the Max Planck Institute in Garching (Germany). Using methods of high resolution spectroscopy, they measured the frequency of several optical transitions in the hydrogen atom. The value obtained was [9.1]

$$
R _ { \infty } = 1 0 9 7 3 7 . 3 1 5 6 8 5 5 0 \mathrm { c m } ^ { - 1 } .
$$

The Landé factor $g$ for the electron,close to 2, has been measured at the University of Washington in Seattle by confining a single electron in a Penning trap. This is produced by superposing a uniform magnetic field on an inhomogeneous electric field. The value of $g$ is equal to twice the ratio of the electron's Larmor precession frequency to its cyclotron frequency. The value obtained is given by [9.2]

$$
{ \frac { g } { 2 } } = 1 . 0 0 1 1 5 9 6 5 2 1 8 8 \ ,
$$

with uncertainty of $4 \times 1 0 ^ { - 1 2 }$

Applying the same technique to a positron, the same value of $g$ was obtained, to within $2 \times 1 0 ^ { - 1 2 }$ .This result is currently the most accurate confirmation available of the hypothesis that antiparticles have the same properties as their corresponding particles.

By comparing the cyclotron frequencies of protons and antiprotons in a Penning trap,it has been shown that their inertial masses are equal, to within $4 \times 1 0 ^ { - 8 }$ [9.3]. Using a similar technique, the ratio of the proton and electron masses has been measured to within $3 \times 1 0 ^ { - 9 }$ [9.4].

As can be seen from (9.6), the value of the electron Landé factor differs from 2 by only a tiny amount. The deviation from this value depends on quantum electrodynamic (QED) effects and can be expressed in terms of the fine structure constant $\alpha$ . This is one of the most important constants in atomic and quantum physics. Recent theoretical progress has made it possible to use the measurement of $g$ to obtain [9.5]

$$
1 / \alpha = 1 3 7 . 0 3 5 9 9 9 4 4 ,
$$

to within $4 \times 1 0 ^ { - 9 }$

# 9.1.3 Impact on atomic physics

# (a) Checking linearity of quantum mechanics

The basic equation in quantum mechanics is the Schrodinger equation (6.27), which is linear. However, it has been shown theoretically that there may be a slight non-linearity [9.6]. The transition frequency between two energy levels would then depend on the population of these levels, making the transition slightly anharmonic. Experimental tests have been carried out, one with $\mathrm { B e ^ { + } }$ ions in a radiofrequency trap [9.7],and the other with hydrogen atoms in a hydrogen maser [9.8]. In both cases, the transition frequency between the relevant hyperfine sublevels was found not to depend on their populations, up to experimental uncertainties. Since these uncertainties were extremely low, thanks to the very low frequency instability of the devices used for the tests, we may conclude that anon-linear generalisation of the Schrodinger equation is unnecessary.

# (b) Understanding properties of atoms and molecules

The contribution here is important and varied and a detailed description would go beyond the scope of this book.

Techniques of high resolution spectroscopy developed and used in atomic or molecular frequency standards have made it posible to measure a great many transition frequencies with very low uncertainties. Examples are the hyperfine transition frequencies of hydrogen and its isotopes, rubidium isotopes of mass 85 and 87,and many ions with a single valence electron (Section 6.7). Likewise,atomic and molecular transition frequencies in the infrared and the visible are now known with uncertainties as low as a few times $1 0 ^ { - 1 2 }$

These determinations,together with investigations of electric and magnetic field effects,have greatly advanced our knowledge of atomic constants,such as the nuclearand electronic gyromagneticratios,and interatomic couplings in molecules.

A better understanding of the interatomic potential has been obtained by measuring the spin-exchange collision cross section and spin-exchange frequency shift cross section of the hydrogen atom in the range $1 - 3 7 3 \ \mathrm { K }$ Studies are underway to compare theoretical and experimental values of these cross sections for caesium and rubidium atoms with low relative velocities. These studies are motivated by the use of laser-cooled atoms in clocks.

An unexpected contribution to the shift in the hyperfine transition frequency of rubidium atoms has ben observed when they are subjected to a strong magnetic field of around $5 ~ \mathrm { T }$ [9.9]. The result implies that the magnetic interaction energy between the nucleus and the electron cloud is not suficiently well known and that further terms must be evaluated [9.1O]. These might well affect the value of the frequency shift due to the second order Zeeman effect,a value that must be taken into account in atomic time and frequency standards. This question could be investigated in experiments with a caesium beam frequency standard [9.11]. This standard would be unusual in that the transition

$$
F = 3 \ , m _ { F } = - 1 \quad \longleftrightarrow \quad F = 4 \ , m _ { F } = - 1
$$

is used as the reference transition. Its frequency has an extremum for an applied magnetic field close to $8 2 \mathrm { m T } .$ Precise measurement of the transition frequency, close to 8.901 GHz, should provide a way of checking that the Breit-Rabi formula (6.4) contains allthe terms needed to calculate the Zeeman frequency shift.

# 9.1.4 Spacetime structure and gravity

Most tests for models of spacetime structure and gravitation involve time measurements. An exhaustive discussion of the significance of these tests can be found in [9.12,9.13].We will consider a few examples of experiments in which atomic time standards play acritical role. Certain tests are based directly upon the stability or accuracy of time standards [9.14]. In other cases, these standards are essential auxiliary tools.

# (a)Direct use of atomic time standards

Several clock transportation experiments have been organised to check the predictions of general relativity.Inparticular, in1972,Hafele and Keating of the US Naval Observatory arranged for transportation of four caesium clocks around the world on commercial flights. In the westward journey, they observed a gain of $2 3 7 \pm 7$ ns, and in the eastward journey, a loss of $5 9 \pm 1 0 ~ \mathrm { n s }$ Theoretical predictions gave a gain of 275 ± 21 ns and a loss of 40 ± 23 ns, respectively, tainted by uncertainties arising from the poorly identified trajectories followed by the clocks [9.15]. This experiment was considered as a check on frequency shifts due to gravity, but it was not very informative,because Pound, Rebka and Snider had already made the same check to better accuracy using the Mossbauer effect [9.16, 9.17]. However, along with several analogous experiments,it was a convincing argument for treating time measurement within a relativistic framework.

A further measurement of the gravitational frequency shift was made by Vessot and Levine in 1976 [9.18]. A hydrogen maser was launched in a probe, up to an altitude of $1 0 0 0 0 ~ \mathrm { k m }$ . During the flight, its phase was continually compared with the phase of a ground-based hydrogen maser, using a threeway link to eliminate the Doppler effect. The observed frequency shift was found to agree with the predictions of general relativity, within the limits of experimental uncertainty, viz.,arelative uncertainty of $7 \times 1 0 ^ { - 5 }$ .More accurate experiments are planned along the same lines,either in satellites with highly elliptical orbits around the Earth,or on a space probe flying towards the Sun. These experiments are interpreted as tests of the Einstein Equivalence Principle (EEP) [9.12].

By comparing a caesium clock, based upon a hyperfine structure transition, with a magnesium clock,based upon a fine structure transition, operating side by side, Godone et al. [9.19] were able to place limits on the time evolution of the product $g _ { \mathrm { p } } ( m _ { \mathrm { e } } / m _ { \mathrm { p } } )$ ,where $g _ { \mathrm { p } }$ is the gyromagnetic ratio of the proton and $m _ { \mathrm { e } } , \ m _ { \mathrm { p } }$ are the electron and proton masses,respectively. This (relative) limit is equal to $5 . 4 \times 1 0 ^ { - 1 3 }$ per year. Combining withastrophysical data these authors have shown that the relative time variation of the fine structure constant $\alpha$ is less than $2 . 7 \times 1 0 ^ { - 1 3 }$ per year. During the same experiment, the clocks underwent an anual variation in the gravitational potential of the Sun, due to the eccentricity of the Earth's orbit. If EEP were violated,an annual variation would have been found in the frequency diference between the two clocks.This was not the case [9.2O]. In more recent work,comparison between a hydrogen maser and a trapped $\mathrm { H g ^ { + } }$ ion frequency standard gives the upper limit [9.21]

$$
{ \frac { 1 } { \alpha } } \left| { \frac { \mathrm { d } \alpha } { \mathrm { d } t } } \right| < 3 . 4 \times 1 0 ^ { - 1 4 } \ \mathrm { p e r \ y e a r } .
$$

Furthermore. taking advantage of the remarkable frequency stability of caesium and rubidium fountains, measurements spread over an interval of 24

months reduced the upper limit for the possible variation of $\alpha$ . We now have [6.23]

$$
{ \frac { 1 } { \alpha } } \left| { \frac { \mathrm { d } \alpha } { \mathrm { d } t } } \right| < 3 . 1 \times 1 0 ^ { - 1 5 } \ \mathrm { p e r \ y e a r } .
$$

These last two results are based upon the fact that the theoretical expression for the hyperfine transition of ground state alkali atoms (such as H, Rb, Cs, $\mathrm { H g } ^ { + } .$ ）contains correction terms depending on the product $\alpha Z$ ,where $Z$ is the atomic number of the element. Any time variation in $\alpha$ would induce different changes in the transition frequency under consideration.

One postulate of relativity theories is the constancy of the speed of light $c$ when measured locally. Let us note in passing that this constancy can only be checked experimentally if we have independent standards for time and length. For this purpose, we require material length standards,such as rulers,interferometer arms or a geodetic base. The constancy of $c$ is generally checked by a two-way propagation. This was the case in the famous Michelson-Morley experiment [9.22], which was unable to detect any effect due to the motion of the observer relative to a hypothetical ether. However, we should also check that the outwardvelocity is equal to the return velocity,or more generally, that the velocity is indeed isotropic.This was done at the Jet Propulsion Laboratory (USA) in 1990, using the frequency stability of two hydrogen masers placed $2 1 ~ \mathrm { k m }$ apart,compared by one-way transmissions in optical fibres [9.23]. Whilst the baseline of the two masers was displaced by the Earth's rotation, no anisotropy was revealed, within the limits of experimental uncertainty, so that $| \Delta c | / c \ < \ 3 . 5 \times 1 0 ^ { - 7 }$ .It has been proposed to repeat this experiment using a spaceborne maser [9.24]. This should reduce the relative uncertainty to $1 . 5 \times 1 0 ^ { - 9 }$ .In the same area of investigation,long term comparison of clocks on board GPS satellites with clocks in ground stations has led to the upper bound $| \Delta c | / c \ < \ 4 . 9 \times 1 0 ^ { - 9 }$ when all directions are considered and $| \Delta c | / c < 1 . 6 \times 1 0 ^ { - 9 }$ for the equatorial component [9.25].

# (b) Indirect use of atomic time standards

In other tests of relativity,the quality of time measurements is exploited for the purposes of highly accurate positioning. Radar telemetry has thus been applied to measure the advance of the perihelion of Mercury more precisely than was possible by optical astrometry using angle determinations [9.26]. The relative inaccuracy in this historic test of Einstein's theory has been reduced to $1 0 ^ { - 3 }$ .Laser ranging on lunar reflectors made it possible to seek a possible violation of the weak equivalence principle for massive bodies (equivalence of inertial and gravitational masses). This putative violation goes by the name of the Nordtvedt effect [9.27]. Other research has been carried out on possible time variations of the gravitational constant, based upon precise measurements of the distances of artificial satellites placed in orbit around Mercury.

As discussed in Section 8.1.4a. angular measurements can be made with great accuracy using VLBI. This method has been used to improve another classic test of general relativity, the deflection of light by matter. It has been possible to measure the bending of quasar light by the Sun,and even by Jupiter [9.28].

All these experiments require detailed models of orbital motions. To this end. the atomic time scale TAI is used to represent the time parameters of the theory,as defined in Section 7.1. Since observations are made from the rotating Earth, the parameters describing this rotation are also needed to very great accuracy. However.we have seen that these parameters are determined on the basis of time and frequency techniques.It is quite clear that time metrology is implicated in such work in an extremely complex manner.

One new form of test involves measuring the time delay of signals from a celestial object when they pass close by the Sun (the Shapiro time delay). Time enters through positioning (VLBI), the orbital model, stability of Earth-based and spaceborne clocks and by the method of radar ranging. This method has been applied to signals from a millisecond pulsar.

We should also record here research involving the timing of millisecond pulsars, discussed in Section 8.3.

# (c) Ultimate aims of these tests

Since the publication of Einstein’s general relativity,many other gravitational theories have been devised. In most of these theories, gravitation is viewed as in general relativity as a manifestation of the structure of spacetime itself, described mathematically by a metric. Yet other theories assume the existence of fields in addition to the metric, or even replacing it.

In weak gravitational fields and for small speeds relative to the speed of light, post-Newtonian metrics are used. e.g.,(3.14) at a low level of approximation. Following work by Nordtvedt [9.29] and Will[9.30]. the various competing theories have been encoded by introducing ten parameters known as the PPN parameters. where PPN stands for parametrised post-Newtonian formalism. These parameters are used to represent the post-Newtonian metrics in a single expression. but they take different values in the diferent theories. Observation then leads to estimates of their values. or the value of one of their combinations. For example, we have seen that the relative gravitational frequency shift is $\Delta U / c ^ { 2 }$ according to general relativity. Its PPN expression is $( 1 + \alpha ) \Delta U / c ^ { 2 }$ . The parameter $\alpha$ (not to be confused with the fine structure constant) is then a measurable quantity,which general relativity predicts to be zero. Vessot and Levine's experiment shows that $| \alpha | < 2 \times 1 0 ^ { - 4 }$

Up until now, tests carried out in the Solar System, for weak felds and low velocities,have led toPP parameters agreeing withgeneral relativitywithin the limits of experimental uncertainty. This only means that we have not yet been able to discriminate between theories whose consequences may differ when we model the Universe and its evolution.This is why tests must involve strong gravitational fields,such as those in the vicinity of binary pulsars.Likewise,observation and modelling of astronomical objects like black holes are of key importance in cosmology.

Cosmology is indeed the ultimate aim of allthese investigations.Here is one of the great human dreams,and are not such dreams the glory of humankind? In the same spirit,the search for a single unified theory covering all macroscopic phenomena as well as the world of elementary particle physics has not yet borne its fruits.A betterunderstanding of the structure of spacetime and gravity would be a significant advance.

For those who are not convinced of this claim, or for those who invest their time and money in the hope of a more immediate return,we may add that therelativistic theoretical framework has becomeanabsolutenecessity for applications. An example is ultraprecise positioning. In addition to its obvious use in transportation, it is crucial for measuring large scale deformations of the Earth's crust (relevant to earthquake prediction) and monitoring sea levels around the world as the climate evolves. A sound experimental basis for the theory is therefore of the utmost importance.

# 9.2 Positioning, geodesy and navigation

# 9.2.1 Principles of time and frequency methods

The idea of determining distances by measuring the two-way propagation time of a signal is widely used in astronomy and geodesy,using laser ranging and radar,not to mention many applications in other fields based on the same principle.A three-dimensional positioning method is then possible, provided that three targets are available and the observer is not situated in the same plane. This is the principle governing ultraprecise geodesy by laser ranging artificial satellites.

In satellite positioning systems, it is more convenient for an observer to use a one-way transmission from the satelite. This also requires much less powerful emissions. However,the inevitable absence of synchronisation between transmitter and receiver must somehow be compensated. Two solutions have been used for worldwide systems,and also for global geodesy. One is based on Doppler shifting of frequencies transmitted by the satellite. The other uses the pseudo-range calculated from the difference between the reception time as measured by the receiver clock and the transmission time as measured by the satellite clock. thereby including the synchronisation error.

In order to give a simple description of the Doppler method, let us assume that the frequency $1 ^ { \prime } ( \tau$ of the transmitter is known to the observer and that the latter is fixed relative to the Earth's surface. We shall not consider relativistic effects here, although in practice they should be taken into account. The observer measures the received frequency $\nu _ { 0 } \mathbf { \kappa }$ and calculates the difference $\Delta 1 ^ { \prime } = 1 ^ { \prime } ( ) \textrm { R } ^ { - } 1 ^ { \prime } ( ) .$ This difference is integrated over a time interval $\Delta t = t _ { 2 } - t _ { 1 }$ We then obtain the number $n$ of periods $P ~ = ~ \nu _ { 0 } ^ { - 1 }$ lost (when $n \ < \ 0$ or gained (when $n > 0$ ) at reception, depending on whether the satellite is moving away or approaching, respectively. The quantity $c n P$ is just the difference between the distances to the satellite at dates $t _ { 2 }$ and $t _ { \mathrm { l } }$ . If the positions of the satellite are known at these dates, in a frame fixed relative to the Earth, the observer's position must lie on a well-defined hyperboloid in this frame. As the satelite continues its orbit, measurements are repeated and the hyperboloids produced in this way have only one common point. which must be the position of the observer. However. in practice, observation of a single satellite can only lead to satisfactory precision if the altitude of the observer is known. Of course, this description has been simplified. Other factors must be included, such as a possible frequency offset, refraction, the observer's own motion.and so on. However, the basic features of the system are clear enough. Measurements involving a single satellite give the 'fix', but not in an instantaneous way, since the satellite must be observed over a portion of its orbit. The whole sct of directions is obtained allthe more quickly as the satellite orbit is lower. Global coverage of the Earth by low-orbiting satelites thus requires polar orbits.

The pseudo-range method involves several synchronised spaceborne or Earth-based transmitters whose positions are known in the terrestrial frame. When two transmiters simultaneously emit signals. the observer measures the difference between reception times and thereby deduces the difference in the distances to these transmiters. The observer is then located on a known hyperboloid. With four transmiters. the position is instantaneously determined. Geometrical constraints require the transmiters to be spaceborne. However, for air and sea navigation. when the altitude is known. Earth-based two-dimensional positioning systems are used. In both cases. redundant information from extra transmitters provides added precision and safety. Apart from the position. a time comparison between the observer's clock and the time base of the system is obtained as a kind of bonus. As we saw in Chapter 7,this by-product can be of great importance for the purposes of time dissemination.

The close relationship between the Doppler method and the pseudo-ranging method is worth noting,even though,inpractice,this relationship may be concealed by the way data is treated mathematically. Such methods,applied with the help of artificial satelites,require a precise description of satelite orbits in the terrestrial frame. This is achieved by setting up a network of tracking stations at known positions. Measurements are immediately transmitted to a control centre where they are processed in the shortest posible time,so that orbital models sent back to the satellites are kept asup-to-date as possible, ready for transmission to users.

We have already mentioned the Global Positioning System (GPS), based upon pseudo-range measurements,because it can be used to compare clocks, to disseminate time (Chapters 5and 7) and to measure the Earth's rotation (Chapter 8). There has been an almost explosive increase in the number of users of GPS in its normal positioning mode. In the next section,we hope to satisfy the reader's curiosity by describing this system in a litle more detail, although many specialised works are already devoted to the subject. In particular,reference [9.31] explains how it worksand describes its various modes of use in geodesy. We shall then go on to outline some other systems.

# 9.2.2 The Global Positioning System

# (a) The satellites and their messages

The Navstar system (Navigation Satellite Time and Ranging)， beter known today by the acronym GPS,stems from studies which began in 1965.Deployment was not completed until 1995,a development period that gives some idea of the magnitude of the undertaking. GPS results from a merger between US Navy and US Air Force projects (Timation and 621B, respectively).

The system uses twenty-four satellites in quasi-circular orbits at an altitude of about $2 0 0 0 0 ~ \mathrm { k m }$ distributed in six orbital planes at intervals of $6 0 ^ { \circ }$ longitude and inclined at $5 5 ^ { \circ }$ to the equator. The orbital period of these satellites is half the Earth's sidereal period. (The latter is $2 3 \mathrm { ~ h ~ } 5 6 \mathrm { ~ m ~ }$ and corresponds to an increase of $3 6 0 ^ { \circ }$ in the angle $A _ { \mathrm { S } }$ defined in Section 8.1.2.) Hence, a fixed observer on the Earth sees the same satellite following the same path across the sky,inazimuth and elevation,every $2 3 \mathrm { ~ h ~ } 5 6 \mathrm { ~ m ~ }$ .At least four satellites are always visible from any point on the Earth's surface (apart from a few very shortlived exceptions) in a configuration suitable for obtaining the observer's position.

The first eleven satellites in the system,known as block I, carried rubidium clocks for the very first, then caesium clocks,as well as reserve quartz clocks as a security measure. Block I satellites,launched from 1985,are each equipped with two caesium clocks and two rubidium clocks, backed up by quartz clocks. They have a lifetime of about eight years.

The basic principle behind GPS is synchronism of on-board clocks. In practice, the clocks are not physically synchronised, but the satellites transmit data which can be used to calculate the offset between their readings and the time base of the system, viz., GPs Time, with uncertainties of a few nanoseconds.

GPS signals are transmitted at two carrier frequencies common to all satellites in the system. These are Ll at $1 5 7 5 . 4 2 ~ \mathrm { M H z }$ and L2 at $1 2 2 7 . 6 0 ~ \mathrm { M H z }$ The information they transmit, called the message, is carried by $1 8 0 ^ { \circ }$ phase reversals in the carrier. It consists of the following components:

· a pseudo-random code C/A, a pseudo-random code P, · a message carrying the data.

The pseudo-random codes are different for each satellite and mutually orthogonal. The autocorrelation function of each code is almost zero, except for zero delay. Correlation functions between satellite codes are almost zero. This explains how receivers distinguish the different satellites,generating the code for each one, and how they measure the reception time of the signal from each satellite (maximal correlation) using their internal clock.

The C/A code (Coarse Acquisition or Clear Access) is only transmitted at frequency L1,phase shifted by $9 0 ^ { \circ }$ . It repeats with period $1 ~ \mathrm { m s }$ and comprises a 1023 bit sequence.

The Pcode (Precise or Protected) is transmitted at both L1 and L2. Its period of repetition is 267 days,but one week segments are transmited and changed every week. It can be encrypted to exclude unauthorised users.

The data message is transmitted at the low modulation speed of 50 bits $\mathrm { s } ^ { - 1 }$ It is made up of frames of 1500 bits (lasting 30 s),each divided into five subframes. The content of subframes 1 to 3 repeats from frame to frame (unless this contextis refreshed)and supplies informationabout the transmiting satellite,i.e.itsalthbtallemtsndientsfolulatingoo to the clock currently in use. Subframes 4 and 5 provide information concerning the system as a whole,i.e., models for calculating ionospheric delays,offset between UTC and GPS Time,rough ephemerides and state of health for the other satelltes in the system,and information about codes.Since all this information is too bulky to fit into two subframes.it is spread over subframes 4 and 5 of twenty-five consecutive frames.The whole set of information can thus only be obtained by tracking the satelite for a total of 12.5 minutes. This explains why tracking extends over 13 minute periods when very precise time measurement applications are at stake (see Section 5.6.3). At each of the frequencies L1 and L2,the transmitted signal is the product of modulations corresonding to the code and the message.Note that during the transmission of one message bit,i.e., $2 0 \mathrm { m s }$ ,the C/A code repeats twenty times.

# (b) Normal operation of the system

By ‘normal operation', we understand simple real-time positioning applications using ordinary GPS receivers.We shallnot discussthe many other modes of use for these receivers.

The determination of satellite orbits and calculation of clock corrections carried out at the master control station are based on tracking by five control stations. The geodetic coordinates of these stations are known with uncertainties as low as a few tens of centimetres relative to a reference system called WGS84.Every atempt is being made to bring the WGS84 system into line with the IERS frame known as ITRF, mentioned in Section 8.1.6. Deviations are now of the order of one decimetre. Orbital parameters are thus calculated and transmitted in the WGs84 system,in practice ITRF, and the same can therefore be said of the observer's coordinates.t

GPS Time is aligned on UTC (USNO) to within 100 ns, modulo 1 s. The latter follows UTC to within 100 ns.

Orbitsare described by means of six parameters similar to the Keplerian parameters,viz.,emi-major axis,ccentricity,inclinationto the equatoright ascension of the ascending node,argument of the perigee,and mean anomaly. However,the orbit of an artificial satellite is perturbed by iregularities in the Earth's gravitational field,solar radiation pressure,the lunisolar tidal potential and the residual atmosphere. According to the approach usually adopted by astronomers,orbital parametersare thus regarded as variables. Using their values at a given instant, we obtain an orbit very close to the true orbit over a range of neighbouring times. Their rates of change are broadcast and parameters should be changed every hour or so.

Position uncertainties for a moving observer may be as low as about $1 0 ~ \mathrm { m }$ when the P code is used at both frequencies.With the C/A code, they are around $3 0 ~ \mathrm { m }$ WhenSelective Availability (SA) wasapplied,until May2000, uncertainties were about $1 0 0 \mathrm { m }$ for unauthorised users.

# (c) Other applications

GPS can be used in differential mode to gain precision in a local positioning application. The position of the moving observer is referred to accurately known positions of nearby fixed stations simultaneously tracking the same satellites. Some errors are significantly reduced, including errors due to the ephemerides, satellite clock noise,refraction and SA when it was imposed. Uncertainties can be reduced to a few metres in real time. Differential positioning is also used to determine relative positions of timing receivers and thereby improve clock comparisons.Since these receivers are fixed, time averages can be taken and uncertainties in relative coordinates are of decimetre order [9.32].

For high precision applications, such as centimetre geodesy and study of the Earth's rotation, the phase of the carrier waves is followed. Modulation is removed by multiplying the received signal by itself. Since modulation is achieved by phase reversal, a pure double frequency is obtained. In this field,studies are coordinated by an international service known as the International GPS Service for Geodynamics (IGS).This service establishes precise ephemerides for GPS satellites,available one or two weeks after the event. They are useful,in particular,for reducing uncertainties in time comparisons when producing TAI.

# (d) Civilian complement to GPS

As far as civilian applications are concerned, GPS has been criticised for its lack of precision due to SA and also for the absence of real time warnings when one of its satelites fails. Since the number of satellites visible only just exceeds the minimum required number of four, such failure may lead to incorrect positioning with disastrous consequences. The question then arises as to whether a civilian system should be set up in parallel.

The complexity of GPS is partly due to its military role. A system operating along the same lines has been designed without satellite-borne clocks. The time provided by a single master clock on the ground is transmitted to satellite transponders. However, this kind of system does not satisfy the need of the armed forces for a completely self-suficient mode of operation,i.e., one in which no data need be injected by ground stations. Such autonomy,although its degrades quality, may be vital in time of conflict.

For the moment, two lines of development are under investigation. The first involves combined use of GPS and its Russian counterpart GLONASS, to be discussed shortly. The number of satelltes available may then rise to forty-eight, with a dozen or so simultaneously in view. The resulting redundancy means that an offending satelite can be detected and eliminated. Mixed

GPS/GLONASS receivers are already available. The other development involves seting upa civilian complement to GPS,in which transmiters would be carried by geostationary satelites and transmit with GPS codes [9.33].

# 9.2.3 Other positioning systems

GLONASS was developed by the USR,and subsequently by Russia, in paralel with GPS. It operates according to the same principles,although the satellites follow slightly different orbits at an altitudeof about $2 0 0 0 0 ~ \mathrm { k m }$ A fixed observer also sees a satelite move along the same apparent trajectory every $2 3 \mathrm { ~ h ~ } 5 6 \mathrm { ~ m ~ }$ ,but this satelliteisadiferent oneeachdaywithaone week cycle.Satelites are recognised by a range of frequencies. Orbital models are transmitted in the form of coordinates. In addition,the time base known as GLONAss Time is different,and not so closely synchronised with UTC. The geodetic frame is also different. This makes the construction of mixed GPS/GLONASS receivers a complicated task,although not impossible.

Before GPS and GLONASS came on the scene, the Doppler system Navsat was widely used for maritime navigation from 1964.The six satellites in polar orbits at altitude $1 1 0 0 ~ \mathrm { k m }$ transmitted frequencies $1 5 0 ~ \mathrm { M H z }$ and $4 0 0 ~ \mathrm { M H z }$ and also synchronisation markers. Messages providing orbital models were transmitted by phase modulation.

Another Doppler system known as DORIS was designed by the French Centre national d'études spatiales (CNES) for high precision positioning [9.34]. It uses the opposite approach to Navsat in the sense that frequencies are transmitted by the beacons tobelocalised and received by satelites.Both beacons and satellites are equipped with ultra-stable quartz oscillators.Frequencies are close to $4 0 0 \mathrm { M H z }$ and $2 \mathrm { G H z }$ .The frequency instability of beacon and satellite oscillators has to beless than $5 \times 1 0 ^ { - 1 3 }$ over the counting period (the interval $\Delta t$ defined in Section 9.2.1) and $1 0 ^ { - 1 2 }$ throughout the pass (e.g.,for a period of 10oo s). The on-board frequency is determined by comparing with a ground-based master clock adjusted to TAI. The uncertainty must be less than $1 0 ~ \mu \mathrm { s }$ .A basic network of forty to fifty fixed beacons on Earth serves to determine satellite orbits.The system was tried out on the Earth observation satellite Spot 2. It was subsequently adopted as one of the positioning systems for the TOPEX/POSEIDON oceanographic satellite, to be discussed below. In the latter case, it was shown that the uncertainty in the radial component of the satellite position is around $3 \mathrm { c m }$ .For the two other components,the uncertainty isabout $2 0 \mathrm { c m }$ .DORIS also provides the beacon positions, with uncertainty as lowas $2 \mathrm { c m }$ . This precision allowed DORIS to feature amongst the panoply of techniques used at the IERS for constructing ITRF and measuring the Earth's rotation.

The PRARE system (Precise Range and Range Rate Equipment) was originally designed in Germany for precise determination of artificial satellite orbits [9.35]. It also includes a satellite-borne space segment, a network of tracking stations and a processing centre. It combines pseudo-ranging and Doppler measurements on signals transmitted by the satellite at frequencies 2 GHz and 8 GHz. This system is used by the ESA's Earth Reconnaissance Satellites (ERS) in conjunction with GPS. It has the same order of precision as DORIS.

# 9.3 Very Long Baseline Interferometry (VLBI)

In Section 8.1.4, we discussed the part played by Very Long Baseline Interferometry (VLBI) in the measurement of Universal Time. In its applications to the study of the Earth's rotation and the construction of celestial and terrestrial reference frames, angular separations between sources should be as large and varied as possible,in order to separate the various quantities to be determined. We have already seen that this type of measurement takes advantage of the frequency stability of hydrogen masers.

VLBI was originally devised to study the structure of celestial sources with small angular dimensions emitting in the radio region of the spectrum. Resolution is improved when reception frequency increases and antennas are more widely spaced. At centimetre and decimetre wavelengths and using Earth-based antennas,angular resolutions of $0 . 0 0 1 ^ { \prime \prime }$ are achieved. Reception in the millimetre wavelengths, still under development, reaches resolutions of $0 . 0 0 0 1 ^ { \prime \prime }$ .VLBI projects involving one Earth-based and one spaceborne antenna would obtain resolutions down to a few tens of microseconds of arc [9.36].

VLBI is also used in differential mode to locate sources on the sky relative to the directions of compact extragalactic sources forming the primary reference frame. In this case nearby sources are the target and typical angular separations to be measured are of a few degrees.

This technique can be used in diferent ways to extend the celestial reference frame ICRFto the optical domain (see Section 3.3.2b). In particular. the space astrometry mission HIPPARCOS provided a catalogue of angular positions and proper motions of some 10o o00 stars with an internal consistency at the level of $0 . 0 0 1 ^ { \prime \prime }$ and $0 . 0 0 1 ^ { \prime \prime } / \mathrm { y r }$ respectively, but was unable to give an initial setting for the rotation and rotation rate of the whole catalogue [9.37]. The HIPPARCOS catalogue had to be aligned with the ICRF. One technique used for this purpose was VLBlobservation of afewdozenradio stars belonging to the HIPPARCOS catalogue. By combining the various methods,it is estimated that the fit is achieved to within $0 . 0 0 0 5 ^ { \prime \prime }$ at the mean date of the HIPPARCOS observations (1991).However,itdeterioratesatarateofabout $0 . 0 0 0 2 5 ^ { \prime \prime }$ per year through uncertainties in proper motions of the stars [9.38].

Differential VLBI is often used to track space probes, in order to situate them relative to ICRF,and also to locate artificial satelites placed inorbit around other planets.

# 9.4 The TOPEX/POSEIDON mission

As an example,we shalldiscuss the many time and frequency aspects of the TOPEX/POSEIDON mission.

Measurements of the vertical distance between an artificial satellite and the surface of the sea by means of an on-board radar altimeter were first attempted between 1975 and 1978 with the American Geos 3 satellite. They were continued using Seasat in 1978.Although the satellite failed afterafew months,it had already proven that these measurements were useful for studying the oceans and their interaction with the atmosphere,climatology and internal geophysics. Geosat confirmed this appraisal over 1985-1989.More ambitious programmes were subsequently devised, with the European Space Agency’s ERS and the TOPEX/POSEIDON collaboration between NASA and CNES (France). The satellite ERS1 was launched in June 1991 and followed by ERS2 in 1995. TOPEX/POSEIDON was launched on 10 August 1992.

The radar beam intersects a sufficiently large region of the sea surface to average out the effect of the waves.Altimetric measurements involve the various elements shown in Figure 9.1.

· The reference ellipsoid is a mathematical surface adopted by convention which approximately follows the sea surface. This removes the need to refer to the geocentre.   
The geoid is a surface of constant gravitational potential,after correcting for periodic terms introduced by the tidal potential. It would coincide with the mean sea surface if the waters of the oceans were homogeneous and at rest.   
The real sea surface is defined as the surface when wave effects have been averaged out.   
The satelite orbit is established ina geocentric frame.Its altitude is calculated above the reference ellipsoid.

Altimetric measurement gives the altitude of the satellite above the real sea surface.Knowing the satellite orbit,we then obtain the height ofthe sea surface above the reference ellipsoid.

![](images/c9f2f8c1636436fe19e306b8f5ab12b8512973e02cc46fd2922a1bdd95f7ab11.jpg)  
Fig. 9.1. Geometrical elements of altimetry above the oceans.

Two elements of great scientific importance are the height $h _ { 2 }$ of the geoid above the reference ellipsoid, which may be positive or negative,and atains values of a hundred metres or so,and the height $h _ { 1 }$ of the sea surface above the geoid, which may also be positive or negative,and attains values of around one metre. We note immediately that the measurement yields the sum of these two elements. This ambiguity is removed by their variability. Over several years, the geoid can be taken as invariable and the oceanic variation is obtained. If we assume that oceanic effects have zero time average, then the mean surface represents the spatial iregularities of the geoid.In the very long term, however, difficulties may remain here. For example, the melting of the polar ice caps affects both sea levels and the shape of the geoid.

The form of the radar echo is afected by conditions at sea. By analysing it, information is obtained about the waves,including their height and direction, quite apart from geometrical data concerning altitudes.

Sea levels areaetedbytemperaturedifferences,salinitytheatmsphre and dynamical effects such as those due to centrifugal and Coriolis forces. It is easy to see therefore that their study can reveal curents,eddies,and heat energy transfers generating climatic change. However, such efects amount to no more than a few decimetres. In order to study them,they must be measured with uncertainties at thecentimetre level.It is interesting to list the scientific themes mentioned in te callfor research proposals issued by the CNES when TOPEX/POSEIDON was still under preparation [9.39]:

· to conduct studies of the permanent and variable circulation of the ocean, and its interaction with the atmosphere,on global and basin scales, in order to contribute to our understanding of the climatic role played by the oceans;   
to develop an improved understanding of oceanic circulation on regional scales over periods of a few months;   
to obtain an improved understanding of heat transfer in the ocean;   
to conduct studies of tidal models;   
· to study the statistics of ocean variability;   
to improve knowledge of the gravity field and associated geoid;   
· to conduct studies of geophysics;   
· to study the physics of waves.

The TOPEX/POSEIDON satellite is in circular orbit at an altitude of about $1 3 0 0 ~ \mathrm { k m }$ ,inclined at $6 6 ^ { \circ }$ to the equator. It does not therefore cover the polar regions. The track of its orbit, that is,the vertical projection of the orbit on the Earth's surface, repeats every 1O days and the distance between tracks is $3 1 6 ~ \mathrm { k m }$ at the equator, decreasing at higher latitudes. The mission,initially planned until 1997,was still running in 20o0.Geophysical assessment of the mission and scientific results clearly show how successful it has been. This lis attested by the 1200 pages devoted to the subject in Vols. 99 and 100 of theJournal of Geophysical Research for 1994and 1995,and many other scientific papers published since then. In particular,uncertainty in the height of the sea surface above the ellipsoid is around $5 ~ \mathrm { c m }$ for a single pass. This includes uncertainties in the orbit and the altimetric measurement in almost equal parts. By taking a monthly average, the uncertainty can be reduced to $1 ~ \mathrm { c m }$ It has also been shown that the variation in the mean sea level can be measured to within $1 ~ \mathrm { m m } \mathrm { y r } ^ { - 1 }$ .This achievement, combined with the success of ERS1 and 2,has encouraged projects to launch further altimetric satellites. (ERS1and2 are complementary because they have different tracksand repeat in different ways.) Such projects would study long term effects,including long term variations in sea level, as well as providing continuous monitoring (Jason project).

Leaving aside the scientific results, which are not our main concern here,we shall now discuss the role played by time and frequency in the TOPEX/POSEIDON mission.

The altimeter is nothing other than a radar, measuring the time of flight of a signal. The inaccuracy of the altimeter clock must be less than $1 0 ^ { - 1 0 }$ if its contribution is to be negligible. Its frequency instability over the time of flight, roughly $1 0 \mathrm { m s }$ ,must also be less than this same value.Measurement dates must be expressed in TAI to the nearest $1 0 ~ \mu \mathrm { s }$

Time measurements are critical in determining the satelite orbit. The precision required for TOPEX/POSEIDON (an uncertainty of a few centimetres in the radial distance) went far beyond anything that had previously been achieved. Three main tracking systems were used, viz.,laser ranging via retroreflectors on the satellite,an on-board GPS receiver,and the DORIS system. These time/frequency systems have been discussed in Section 9.2. Knowledge of the Earth’s gravitational field is required to model the orbit. The model is based on trackings of a great many satellites in very different orbits. Such trackings also involve time/frequency positioning techniques. Moreover, in the present case, the model was improved by tracking TOPEX/POSEIDON itself. Such analyses require precise knowledge of Earth rotation parameters, because the orbit is described in a non-rotating system, whereas the satelite position must be given in the reference system that accompanies the Earth in its rotation. This rotation is now monitored solely by means of time/frequency techniques (see Section 8.1.4). The rotation parameters can be determined when DORIS tracks TOPEX/POSEIDON,but it is useful to combine the results with those stemming from other techniques. Among the later, VLBI requires the most stable clocks that can be built.

Finally, TAI is involved in various ways. It is the base for synchronisation (to within $1 ~ \mu \mathrm { s }$ in tracking stations),the reference for frequency accuracyand the time argument in dynamical theories used for orbital calculations.

# 9.5 Telecommunications

Telecommunications networks have a tree structure in which the ends of the branches are user terminals. Several hierarchical levels contain nodes at which messages are switched from one channel to another. In the analogue transmission mode, several messages are sent together through the same communication channel using single sideband amplitude modulation without transmission of the carrier. In order to correctly reconstitute the message,the frequencies of oscillators equipping modulation/demodulation centres must be tuned to the nearest $1 0 ^ { - 8 }$ [9.40].

Digital voice transmission represents a significant development. Voice frequencies,weenout $3 0 0 ~ \mathrm { H z }$ and $3 6 0 0 ~ \mathrm { H z }$ ,are sampled at a rate of 8000 times per second and coded in 8 bit words. It is then possible to blend messages together and transmit them simultaneously through the same channel, up to thirty at a time,ina process called multiplexing. In order to demultiplex,a frequency reference is needed at reception. However,a quite substantial shift can be tolerated between multiplexing and demultiplexing frequencies,since a time shift is not audible.

For the transmission of numerical data in which information loss due to time shifts cannotbe tolerated,aneedarisesfor goodsntonisation,i.e.,good fre quency tuning, over the whole network. This problem has led to the current development of the Synchronous Digital Hierarchy (SDH).Here,frequencies at nodes and terminals must be tuned to within $1 0 ^ { - 1 1 }$ on a daily average. In addition, the International Telecommunication Union stipulates that this frequency should be fixed relative to UTC frequency,and hence TAI frequency, to within $1 0 ^ { - 1 1 }$ in normalised value [9.41].

Within the context of the present work, the needs of telecommunications may appear modest. More sophisticated solutions are ruled out by the quest for lower costs.Nevertheless,caesium clocks are a necessity at the master node of the network. Nodes at other levels and user terminals are equipped with quartz oscillators servo controlled by the network itself. GPS can contribute to the control of frequencies at the master node or at high level nodes.

Despite its name, SDH is based upon syntonisation. The use of synchronisation in the proper sense has sometimes been advocated for the advantages lit would bring. There has even been some talk of a future need for real-time access to UTC to within 100 ns for telecommunications purposes [9.42]. This isno doubta project for the rather distant future,about which we have been unable to obtain further details.

# Appendix 1

# Acronyms for time laboratories

The following is a list of acronyms for laboratories $k$ maintaining an approximation $\mathrm { U T C } ( k )$ to UTC, or an independent local atomic time scale $\mathrm { T A } ( k )$ ， together with their name and location.

AMC Alternate Master Clock station, Colorado Springs, CO,USA   
AOS Astronomiczne Obserwatorium Szerokosciowe, Borowiec, Poland   
APL Appliedysicsaboratory,urel,,   
AUS Consortium of Australian laboratories   
BEV Bundesamt fur Eich- und Vermessungswesen, Vienna, Austria   
BIRM Beijing Institute of Radio Metrology and Measurement, Beijing,People's Republic of China   
CAO Cagliari Astronomical Observatory, Cagliari, Italy   
CH Consortium of Swiss laboratories   
CNM Centro Nacional deetrologia,exico ityeico   
CRL Communications Research Laboratory,Tokyo,Japan   
CSAO Shaanxi Astronomical Observatory,Lintong, People's Republic of China   
CSIR Council for Scientific and Industrial Research, Pretoria, South Africa   
DLR Deutsche Forschungsanstalt fur Luft- und Raumfahrt, Oberpfaffenhofen,Germany   
DTAG Deutsche Telekom AG,Darmstadt, Germany   
F Commission Nationale de 'Heure,Paris, France   
GUM Gl6wny Urzad Miar,Central Office of Measures, Warsaw, Poland   
ILN Isututo Eietrotecnico Nazionaie Gamieo Ferraris, Turin, Italy   
IFAG Bundesamt fuir Kartographie und Geodaesie Fundamentalstationll   
IGMA Instituto GeograficoMilitar,BuenosAires,rgentina   
INPL NationalicalboratoryJerusalemel   
IPQ Institute Portugues da Qualidade,Monte de Caparica, Portugal   
JATC Joint Atomic Time Commission,Lintong, People's Republic of China   
KRIS Korea Research Institute of Standards and Science,Taejon, Republic of Korea   
LDS The Universityof Leeds,Leeds,United Kingdom   
MSL Measurement StandardsLaboratory,Lower Hutt, New Zealand   
NAO National Atronomicalervatoryisuawa,   
NIM National Institute of Metrology, Beijing, People's Republic of China   
NIST National Instituteof tandards andechnologyoulder, Co, USa   
NPL National Physical Laboratory, Teddington, United Kindom   
NPLI National PhysicalLaboratory,New elhi,Idia   
NRC National Research Council, Ottawa, Canda   
NRLM National Research Lboratoryof MetrologyTsukuba,Japan   
OMH Orszagos eresugyivatal, dapst,Hugary   
ONBA Observatorio val, uenosres,rgetina   
ONRJ Observatoriocional,iodeJneirorail   
OP Observatoirede aris,aris,rce   
ORB Observatoire oyal de Belgique,Brussels,elgium   
PTB Physikalisch-Technische Bundesanstalt,Braunschweig, Germany   
ROA Real InstitutoyObservatorio de la Armada,San Fernando, Spain   
SCL Standards and Calibration Laboratory,Hong Kong, People's Republic of China   
SO Shanghai Observatory, hanghai,People's epublic of China   
SP Swedish National Testing and Research Institute, Boras, Sweden   
SU Institute of Metrology for Time and Space (IMPV), NPO‘VIIFI',endeleevo,oscow egion,ia   
TL Telecommunication Laboratories, Chung-Li, Taiwan

310

TP Institute of Radio Engineering and Electronics, Academy of Sciences,Czech Repblic   
UME Ulusai Metroloji Enstitusu, Marmara Research Centre, NationalMetrology Institute,Gebze-Kocaeli,urkey   
USNO USavalObservatory,Washington,,U   
VSLVan SwidenLaboratorium, Delft,Netherlands

# Appendix 2 Abbreviations

# Time scales

Abbreviations inbold type are official inall languages.

EAL Free (unsteered) atomic time scale   
ET Ephemeris Time   
GMST Greenwich Mean Sidereal Time   
GMT Greenwich Mean Time   
TA(k) Atomic time established by laboratory $k$   
TAI International Atomic Time   
TCB Barycentric Coordinate Time   
TCG Geocentric Coordinate Time   
TDB Barycentric Dynamical Time   
TDT Terrestrial Dynamical Time (became TT in 1991)   
TT Terrestrial Time   
UT Universal Time   
UTC Coordinated Universal Time   
UT1 Universal Time 1 (forms O and 2 also exist)

# Miscellaneous

BIH Bureau international de l'heure   
BIPM Bureau international des poids et mesures (International Bureau of Weights and Measures)   
CCDS Consultative Committee for the Definition of the Second (became CCTF in 1997)   
CCIR International Radio Consultative Committee   
CCTF Consultative Commitee for Time and Frequency   
CGPM Conférence générale des poids et mesures (General Conference on Weights and Measures)   
CIPM Comité international des poids et mesures (International Committee for Weights and Measures)   
CNES Centre national d'études spatiales,France   
GLONASS Global Navigation Satellite System   
GPS Global Positioning System   
IAU International Astronomical Union   
ICRF International Celestial Reference Frame   
IERS International Earth Rotation Service   
ITRF International Terrestrial Reference Frame   
ITU International Telecommunication Union   
IUGG International Union of Geodesy and Geophysics   
JD Julian Date   
LHA Laboratoire de l'horloge atomique,Orsay,France   
LPTF Laboratoire primaire du temps et des frequences,Paris   
MJD Modified Julian Date   
NASA National Aeronautics and Space Administration   
SI International System of Units   
TWSTFT Two-Way Satellite Time and Frequency Transfer   
URSI International Union of Radio Science   
VLBI Very Long Baseline Interferometry   
VLF Very Low Frequency   
WGS World Geodetic System

# Appendix 3

Definitions of base units in the SI system

# The metre [m]

The metre is the length of the path travelled by light in vacuum during a time interval of $1 / 2 9 9 7 9 2 4 5 8$ of asecond.(17thGeneralConferenceonWeights and Measures,1983.)

# The kilogram [kg]

The General Conference sanctions the prototype of the kilogram adopted by the International Committee. This prototype shall henceforth be considered to be the unit of mass. (1st CGP9.)

The kilogram is the unit of mass; it is equal to the mass of the international prototype of the kilogram. (3rd CGPM,1901.)

# The second [s]

The second is the duration of 9192 631 770 periods of te radiation corre.. sponding to the transition between the two hyperfine levels of the ground state of the cesium 133 atom. (13th CGPM,1967.)

# The ampere [A]

The ampere is that constant current which,if maintained in two straight parallel conductors of infinite length,of negligible circular cross-section,and placed 1 metre apart in vacuum, would produce between these conductors a force equal to $2 \times 1 0 ^ { - 7 }$ newton per metre of length. (9th CGPM,1948.)

# The kelvin [K]

The kelvin, unit of thermodynamic temperature,is the fraction 1/273.16 of the thermodynamic temperature of the triple point of water. (13th CGPM,1967.)

# The mole [mol]

(1) The mole is the amount of substance of a system which contains as many elementary entitiesas there are atoms in 0.012 kilogram ofcarbon12; its symbol is $\cdot _ { \mathrm { m o l } } \cdot$ ·

(2) When the mole is used, the elementary entities must be specified and may be atoms,molecules,ions, electrons, other particles,or specified groups of such particles. (14th CGPM,1971.)

# The candela [cd]

The candela is the luminous intensity,in a given direction, of a source that emits monochromatic radiation of frequency $5 4 0 \times 1 0 ^ { 1 2 }$ hertz and that has a radiant intensity in that direction of $1 / 6 8 3$ watt per steradian. (16th CGPM, 1979.)

# Appendix 4 International services

# Time

Bureau international des poids et mesures, Time Section, Pavillon de Breteuil,F-92312 Sevres Cedex (France).

Telephone BIPM Switchboard $+ 3 3 \ 1 \ 4 5 \ 0 7 \ 7 0 \ 7 0$   
Fax BIPM General $+ 3 3 \ 1 \ 4 5 \ 3 4 \ 2 0 \ 2 1$ BIPM Time Section $+ 3 3 \ 1 \ 4 5 \ 0 7 \ 7 0 \ 5 9$   
Internet http://www.bipm.fr or anonymous ftp 62.161.69.5 (subdirectory TAI)   
E-mail tai@bipm.fr

# Rotation of the Earth (Universal Time)

International Earth Rotation Service (IERS).

# Central Bureau

Bundesamt fuer Kartographie und Geodaesie (BKG), Richard Strauss Allee 11,D-60598Frankfurt-am-Main (Germany).

Telephone +49696333 273 Fax +49 69 6333 425 E-mail richter@ifag.de

Product Centre on Earth Orientation

Observatoire de Paris, Departement d'astronomie fondamentale, 61,avenue de l'Observatoire,75014 Paris (France).

Internet http://hpiers.obspm.fr or anonymous ftp hpiers.obspm.fr 145.238.100.28   
E-mail gambis@obspm.fr

Rapid Service and Predictions of Earth Rotation Parameters

US Naval ObservatoryEarthrientationertnt 3450 Massachusetts Avenue NW, Washington DC 20392-5420, USA.

Internet http://maia.usno.navy.mil or anonymous ftp maia.usno.navy.mil 192.5.41.22   
E-mail jimr@maia.usno.navy.mil

# References

# Chapter 2

[2.1] H. Poincaré (19o6). La valeur de la science (Flammarion,Paris).

# Chapter 3

[3.1] C.M.Will(1993). Theory and experiment in gravitational physics (revised edn.) (Cambridge University Press, Cambridge).   
[3.2] J.L.Anderson (1967).Principles of relativity physics (AcademicPress,New York).   
[3.3] B.Guinot (1997).Application of general relativity tometrology,Metrologia 34,261-290.   
[3.4] C.W.Miser,K..re,J.A.eeler(973).rvitation (Freenew York,San rancisco,odon).   
[3.5] International Astronomical Union (1991).IAU transactions,Vol. XXI B,ed. J.Bergero(r,drecht,oton,).   
[3.6] V.A.Brumberg (1991).Essential relativisticcelestial mechanics (AdamHilger, Bristol,hiladelphia,Nework).   
[3.7] International Earth Rotation Service(1996).Conventions,Technical note21, ed.D.D.McCarthy (Observatoire de Paris).   
[3.8] S.A.Klioner (1992).The problem of clock synchronisation:a relativistic approach,Celestial mechanicsanddynamical astronomy 83,81-109.   
[3.9] P.Wolf, G. Petit (1996).Relativistic theory for clock syntonization and the realization of geocentric coordinate times,Astron. Astrophys.304,653-661.   
[3.10] P.Willis (1991).IAG Newsletter,Bulletin geodesique 65,i89-208.

# Chapter 4

[4.1] G. Bigourdan (1914). Le jour et ses divisions,les fuseaux horaires et l'Association internationalede l'heure,Annuairedu Bureau des longitudes, notice B.   
[4.2] October 1884. International conference held in Washington for the adoption of asingle primemeridianandauniversal time,Proces-verbauxdes Seances (Gibson Bros.,Printers and Bookbinders, Washington).   
[4.3] J. Renaud (1917). L'avance de I'heure légale pendant I'eté 1916, Annuaire du Bureau des longitudes,notice B.   
[4.4] A.Lambert (194O).Le Bureau international'de I'heure, son role, son fonctionnement,Annuairedu ureau des longitudes.   
[4.5] B.Guinot (1992).LeBureau international del'heurede1911a1964:Le temps astronomique et la naissance du tempsatomique,in Le Bureauinternational de l'heure,75nsauservicedel'heureuniverselle,1-43(ObservatoireePris, Bureau des longitudes).   
[4.6] P.Paquet (1992).Le BIH de 1964 a 1987. Temps atomique et geodynamique globale, évolution et réorganisation, in $L e$ Bureau international de l'heure,75 ansau servicedel'heureuniverselle,45-57 (Observatoire de Paris,Bureau des longitudes).   
[4.7] D.Howse (198o).Greenwich time and the discovery of the longitude (Oxford UniversityPress,ord,ework,ronto,eoe).   
[4.8] W.de Sitter (1927). On the secular acceleration and fluctuation of the longitude of theounruryds,ulltro.t.th.v   
[4.9] A.Danjon (i929).Le temps,sa definition pratique,sa mesure,L'astronomie 43,13-22.   
[4.10] G.M. Clemence (1950). On revising the official system of astronomical constants,Constantesondamentalesdel'atronomie9-28(Cs).   
[4.11] A. Scheibe, U.Adelsberger (1936). Nachweiss von Schwankungen der astronomischer Tageslange mittels Quartzuhren,Phys.Zeitschrift 37,38.   
[4.12]N.Stoyko (1937).Sur laperiodicite dans l'iregularitede larotation de la Terre,C.R.Acad.Sci.Paris 250,79.   
[4.13]E.W.Woolard,G.M.Clemence(1966).Spherical astronomy (Academicrs, New York,London).   
[4.14] P.Forman (1985). Atomichron: The atomic clock from concept to commercial product, Proc. IEEE 73,118-1204.   
[4.15]R.E.Beehler(1967).Ahistoricalreview ofatomic frequency standards,Proc. IEEE 55,792-805.   
[4.16] R.L. Sydnor (1982). Distinguished scientist panel discussion,Proc. 14th AnnualPrecise Time and Time Interval Applications and Planning Meeting, 631-657 (Greenbelt, USA).   
[4.17] N.F.Ramsey (1983).History of atomicclocks,J.ofRes.National Bureau of Standards 88,301-320.   
[4.18] L. Essen, J.V.L. Parry (1957). The caesium resonator as a standard of frequencyandtime,Phil.Trans.R.Soc.LondonSer.A250,45-69.   
[4.19]P.Forman (1982). Atomic clocks.Preview of an exhibit at the Smithsonian, Proc.36thAnn.Freq.Contr.Symp.,220-222(Philadelphia,UA).   
[4.20]W.arowitz.G.Hall.senJ.VLrry958).reenc in terms of ephemeris time,Phys.Rev.Lett.1,-107.   
[4.21]B.Guinot(1967).FormationduneechellemoyennedetempsatomiqueBull. Astron.,Série 32,449-464.   
[4.22] J.McA. Steele, W. Markowitz, C.A. Lidback (1964). Telstar time synchronization,EEETrans.Instrum.eas.,Vol.I-13,No.4617.   
[4.23]G.Becker (1967).Lanouvelle definition de la secondeetles theories relativistes,Com.Cons.efinitionde laode, $4 ^ { e }$ session,78.   
[4.24]B.Gnot99).icatioofenraleativityetrolgy 34,261-290.   
[4.25]D.H.Sadler (1978).Meansolartme on the meridian ofGreenwich,Q. J.R. Astron. Soc.19,290-309.

# Chapter 5

[5.1] ISO(1993).International Vocabulary of Basic and General Terms in Metrology,2ndedn.(nteratioalOrgaiationfortadardiation,a).   
[5.2] IEEE(1988).IEEEStandarddefinitionsof physical quantitiesforfundamental frequencyand timemetrology(InstituteofElectricaland ElectronicEngineers Standard no.1139-1988,New York).   
[5.3] CCIR(1992).asurementsofrencyandtime (se),inIoal Telecommunications Union:Recommendation538-2of theInternationalRadid Consultative ommittee(CCIR,Geva).   
[5.4] IEEE(1984).Frequencystability:fundamentalsandmeasurement,ed.V.F. Kroupa (IEEE Press, New York).   
[5.5] NIST(199).aracterzatonfocksdocilatorsed..ullin D.W.Allan,D.A.HoweandF.L.Walls (NTechicalNote37).   
[5.6] P.Karta)ceecrs York,San Francisco).   
[5.7] J.A.Barnes,A.R.Chi,L.S.Cutler,D.J.Healey,D.B.Leeson,T.E.McGunigal, J.A.MullenJr.,WL.mith,R.L.nor,R.FC.VessotG...Wiler (1971).Characterizationoffrequencysability,IEEETrans.Intrum.Meas.20 105-120.   
[5.8] P. Lesage, C. Audoin (1979). Characterization and measurement of time and frequencyabilitydioci.14,9.   
[5.9] D.W.Allan (1987). Time and frequency (time domain) characterization, estimation,and prediction of precisionclocksand oscillators,IEEE Trans. Ultrason.,erroelec.,Freq.Contr.34,6   
[5.10] D.A. Howe,D.W.Allan,J.A.Barnes (1981).Propertiesofsignal sources and measurementmethods,Proc.35thAnnualFrequencyControlSymposium A1-A47 (Philadelphia, USA).   
[5.11] C.A. Greenhall(1991). Recipes for degrees of freedom of frequency stability estimators,IEEE Trans.Instrum.Meas.40,994-999.   
[5.12] L.-G. Bernier (1988). Linear prediction of the non-stationary clock error function,Proc.2ndEroeanFreuencyndTimeForum (Neuchatel, Switzerland).   
[5.13] D.W.Allan (1991).Time and frequency metrology: current status and future considerations,Proc.5th European Frequency and Time Forum,1-9 (Besangon,rce).   
[5.14]F.Boquet(1913).Surlorganisationduservice de1'heurealObservatoirede Paris,Buloc.Atronomiquedence,Jee   
[5.15]E.A.Gerber,A.Ballato (eds.) (1985).Precisionfrequencycontrol,2voumes (Academic Press, Orlando).   
[5.16]F.L.Walls,J.-J.Gagnepain (1992).Environmental sensitivities of quartzcrytal oscillators,Ens.Uron.,roelec.,q.ontr.3949   
[5.17] R.-J.esson(97).Anew electrodelessresonatoresignProc.3stnnual Frequency ControlSymposium,147-152(Atlantic City,UA).   
[5.18] B.Guinot (1997). Application of general relativity to metrology,Metrologia 34,261-290.   
[5.19] G.Petit,P.Wolf (1994).Relativistic theory for picosecond time transfer in the vicinity of the Earth,Astron. Astrophys.286,971-977.   
[5.20] P.Wolf,G.Petit (1995).Relativistic theory for clock syntonization and the realization of geocentric coordinate times,Astron. Astrophys.304,653-661.   
[5.21] P.Parcelier, G. Freon (1976). Comparaison d'horloges atomiques par reception designauxde television,Bull.InformationBur.Nat.deMetrologie23,32-39.   
[5.22] D.W. Allan, C. Thomas (1994). Technical directives for standardization of GPS time receiver software,Metrologia 31,69-79.   
[5.23] M. Brunet (1979). Synchronization of atomic clocks through the SYMPHONIE satellite,Radio Sci.14, 721-730.   
[5.24] B.S. Dudnik, B.L. Kashcheev, Y.A. Koval, S.F. Semenov, M:D. Sopelnikov, A.A.Tkachuk (1986). New equipment for comparison of time and frequency standardsusingmeteorite trails, Izm.Teknika4.   
[5.25] P.Friedelance (1994). L'experience LASSO,Doctoral thesis, University of Paris VI.

# Chapter 6

[6.1] P.Kartaschoff (1978). Frequency and time (Academic Press,London).   
[6.2] H.Hellwig (1985).Microwave frequency and time standards,in Precision frequency control,113-176,eds.E.A.Gerber,A.Ballato (Academic Press, Orlando).   
[6.3] C. Audoin (1991).Les étalons atomiques de frequence,in La mesure de la frequence eocillateurs,2176(ronos,asson,is).   
[6.4] J.Vanier,C.Audoin (1989).Thequantum physics of atomic frequency standards,2vols.(IOPPublishing,Bristol and Philadelphia).   
[6.5] B.Cagnac,J.C.Pebay-Payroula (1983).Physiqueatomique,2vols.(Dunod Universite,Paris).   
[6.6] N.F. Ramsey (1956). Molecular beams (Oxford University Press,London).   
[6.7] A. Kastler (195o). Quelques suggestions concernant la production optique et la detection optique d'une inégalite de population des niveaux de quantification spatiale desatomes.Applicationsa I'experience de Stern et Gerlach etala reésonance magnetique,J.Phys.Radium11,255-265.   
[6.8] R.H. Dicke (1953). The effect of collisions upon the Doppler width of spectral lines,Phys. Rev. 89,472-473.   
[6.9] A.de Marchi (1987). Understanding environmental sensitivity and ageing of cesium beam frequency standards,Proc. Ist European Frequency and Time Forum,288-293 (Besancon,France).   
[6.10] L.EssenJ.VL.arry(957).heesimresoatorasatad frequencyand time,Phil.Trans.R.Soc.LondonSer.A25o,45-69.   
[6.11]A.uch,K.orenwendt,B.isher,T.eindor,E..uller,R.choder (1987).CS2: The PTB's new primary clock,IEEE Trans. Instrum.Meas.36, 613-616.   
[6.12] K. Dorenwendt, B. Fisher,T. Heindorf(1990). The PTB’s primary time and frequencyaardsformaedcertintyica4   
[6.13]A.Bauch,T.Heindorf,R.Schroder,B.Fisher(1996).ThePTBprimaryclock CS3:Type B evaluation of its standard uncertainty.Metrologia 33.249-259.   
[6.14]A.Bauch,B.Fisher,T.Heindorff.R.Schroder(1998).Performanceof the PB reconstructed primary clock and an estimate of its current uncertainty, Metrologia 35,829-845.   
[6.15] M. Arditi,J.L. Picque (1980). A cesium beam atomic clock using laser optical pumping. Preliminary tests,J. Phys.Lett. 41,L379-L381.   
[6.16] L.L.Lewis,M.Feldman (1981).Optical pumpingbylasers inatomic frequencystadards,roc.Ann.Freq.Controlymposium62624 (Philadelphia, USA).   
[6.17] P.Cerez, G.Theobald, V.Giordano, N. Dimarcq,M.de Labachelerie (1991). Laser diode optically pumped cesium beam frequency standards investigations atL.H.A.,EEETans.Itrum.eas.407141.   
[6.18]A.issiJertet,E.eeq).ett determinationinanoticallypumpedcesiumbeamfrequencystandard,EE Trans.Uraon.,roec.e.Cotr46.   
[6.19]W.D,..ruirJ.H.yC.e.J L.O.Mullen,F.L.Wals,T.E.Parker,A.asegawa,K.Fukuda,N.otake,. Kajita,T.Morikawa(1999).Accuracyevauationsandfrequencycomparion ofNIST7andCRLO1rocjointmeetingEuropeanFrequencydme ForumandIEEEInt.FrequencyControlSymposium62-65(Besancon France).   
[6.20] C.lomon,J.albard,W.lips,A.aron,.Guellati (99). cooling of cesium atoms below $3 \mu \mathrm { K }$ Europhys.Lett.268.   
[6.21]A.Ciron,P.Lurent,G.tareli,.Geali..Lea,.Bouhara(995). Acesium fountainfrequencyandard:preliminarymeasurement,EEan. Instrum.Meas.44,128--131.   
[6.22]A.Ciron,.GealiG.ntareli,P.Lurent,E.mn..ea M.Bouhara,S.Weyrs,K.aec996).hepreaycac evaluatioydot FrequencyandTimeForum218-223(Brighton,UnitedKingdom).   
[6.23]A.Clairon (20oo).Private communication.Cold atom clocks,tobe published in Proc. ICAP 20OO (Florence,Italy).   
[6.24]N.F.Ramsey(199o).Experiments withseparatedoscillatoryfieldsand hydrogen masers,Nobellecture,Rev. od.Phys.62,541-551.   
[6.25] C.Cohen-Tannoudji,B.Diu,F.Laloe (1973).Mecanique quantique,2 volumes (Herman,Paris).   
[6.26] C.Audoin,N.imarcq,V.Giordano,J.Viennet (1992).Physical originof the frequency shifts incesium beam frequency standards,IEEE Trans. Instrum. Meas. 39, 412-421.   
[6.27] J.Rabian,P.Rochat (1988).Full-digital processing ina new commercial cesium standard,Proc.2nd European Frequencyand Time Forum461-468 (Neuchatel, witzrland).   
[6.28] L.S.Cutler,R.P.Giffard (1992). Architecture and algorithms for new cesium beamfrequency standardelectronics,Proc.IEEEFrequency Control Symposium 127-133 (Hershey,UA).   
[6.29] C. Audoin,F. Hamouda,L. Chassagne,R. Barillet (1999). Controlling the microwave amplitude in optically pumped cesium beam frequency standards, IEEETrans.Ultrason.,Ferroelec.,Freq.Contr.46,41.   
[6.30] A. de Marchi, G.D. Rovera, A. Premoli (1984). Puling by neighbouring transitions and its effect on the performances of cesium beam frequency standards,etrologia 20,37-47.   
[6.31] L.S.Cutler,C.A.Flory,R.P.Giard,A.de Marchi (1991).Frequencypulling by hyperfine $\sigma$ transitions in cesium beam atomic frequency standards,J. Appl. Phys.69,2780-2792.   
[6.32] Guidetotheexpressionofuncertaintyinmeasurement,Interational Organization for Standardization (Geneva, Switzerland).   
[6.33] C. Audoin (1992). Caesium beam frequency standards: classical and optically pumped,Metrologia29,113-134.   
[6.34] G.Theobald,N.Dimarcq,V.Giordano,P.Cerez (1989).Ground state Zeeman coherence effects in an optically pumped cesium beam, Opt. Comm.71, 256-261.   
[6.35] G.D. Rovera. E. de Clercq, A. Clairon (1994). An analysis of major frequency shifts in theLPTF optically pumped primary frequency standard,IEEETrans. Ultrason.,rrelec.,Fr.Cntr.49   
[6.36] N.imarcq,V.Giordano,C.Jacques,G.Theobald,P.Cere (1991). Experimental study of two-laser optical pumping in a cesium clock, Proc. 5th European Frequency and Time Forum 187-189 (Besancon,France).   
[6.37] A. Makdissi, J.-P. Berthet, E. de Clercq (1997). Improvement of the short term stability of the LPTF cesium beam frequency standard,Proc.1Ith European Frequencyand Time Forum564-566(Neuchatel,Switzerland).   
[6.38] F. Hamouda, G. Theobald, P.Cerez, C. Audoin (20oO). Analysis tools for the accurate evaluationofasmall frequencytandard,IEEErans.Utron., Ferroelec.,Freq.Contr.47,449-455.   
[6.39] S. Oshima,Y. Nakadan,T.Ikegami, Y. Koga (1991). Light shifts in an optically pumped Cs beam frequency standard,IEEE Trans.Instrum.Meas.40, 1003-1007.   
[6.40] D. Yang,J. Chen (1997).Light frequency shift in small optically pumped cesiumbamucyrds,n.ron.,roelec. Contr. 47,449-455.   
[6.41] P. Forman (1985). Atomichron: The atomic clock from concept to commercial product, Proc.IEEE 73,1181-1204.   
[6.42] A. Ashkin $( 1 9 . 0 )$ .Acceleration and trapping of particles by radiation pressure, Phys. Rev.Lett.24,156-159.   
[6.43]T.Hansch,A.Schawlow (1975).Cooling of gases bylaserradiation,Opt. Comm. 13,68-69.   
[6.44]D.Wineland,H.Dehmelt (1975).Proed $1 0 ^ { 1 4 } \Delta \nu < \nu$ laser fluorescence spectroscopy on $\mathrm { T l } ^ { + }$ mono-ionoscillatorI,Bull.Amer. Phys.Soc.67.   
[6.45]C.Cohen-Tannoudji,W.D.Phillips (199o).Newmechanisms forlasercooling， Phys.Today43,33-40.   
[6.46] A.Aspect,J.Dalibard (1994).Lerefroidissement desatomes par laser,La Recherche25,30-37.   
[6.47] S.Chu (1998). The manipulation of neutral particles,Nobel lecture,Rev. Mod. Phys. 70,685-706.   
[6.48] C.Cohen-Tannoudji (1998). Manipulating atoms with photons.Nobel lecture, Rev.Mod.Phys.70,707-719.   
[6.49] W.D.Phillps (1998).Laser coolingand trapping ofneutral atoms,Nobel lecture,Rev.Mod.Phys.70,72-741.   
[6.50] A.N. Luiten, A.G. Mann, M.E. Costa, D.G. Blair (1995). Power stabilized exceptionally high stability cryogenic sapphire resonator oscillator,IEEE Trans.Instrum.Meas.44,132-135.   
[6.51]E.Tiesinga,B.J.Verhaar,H.T.C.toof.DvanBragt(992).Spinge frequencyshift inacesiumatomic fountain,Phys.Rev. A45,R267-2673.   
[6.52]K.Gibble,S.Chu (1993).LasercooledCs frequencystandardanda measurement of the frequency shift due to ultracold collisions, Phys. Rev. Lett. 70, 1771-1774.   
[6.53] P.Luent,monde,E.moG.nareli,.iron,.cq, P.Petit,C.Audoin,C.alomon (1998).Acoldatomclock inabeeof gravity,Eur Phys.J.D3,201-204.   
[6.54] A.Jood,L.-G.Bernier,H.Schweda,G.Busca(998).TheSHcompact hydrogen maser forspace applications.Report onthePEM physics package designveriicaionrocthuropeanFeecydimeFum25 (Warsaw Poland)   
[0.55] C. Salomon, C. Veilet (T998). ACES: Atomic clock ensemble in space, Proc. lst symposiumon utilisation of the International Space Station SP-385, 295-297 (Darmstadt,Gerany).   
[6.56]H.G.oS..Jerts,..ullin,L.W.olrg,N. T.Heavner,J.H.irleyFL.Walls,R.E.rulinger(998).Deignsuiesor laser-cooledsacelock,roc.EEEInt.Fre.ControlSmosi4 (Pasadena, UA).   
[6.57]K.Ge998).Lerledmirogavitocksroc.tFre. Control Symposium41-45(Pasadena,UA).   
[6.58]B.Kokkelmans,B.Verhaar,K.Gibble,D.Heinzen(1997).Predictionsfor laser-cooledRbclocks,Phys.Rev.A56,43894392.   
[6.59] C.Fertig,K.Gibble (20o0).Measurementand cancellation of the cold collision shift in an $^ { 8 7 } \mathrm { R b }$ fountain clock,hs.Rev.Lett.85,162625.   
[6.60]YaiseC).o shifts in an $^ { 8 7 } \mathrm { R b }$ atomic fouains.ev.Lett851.   
[6.61]S.Bize,Y.ortais,M.S.Santos,C.Mandache,A.Clairon,C.Salomon (1999). High-accuracymeasurementofthe $^ { 8 7 } \mathrm { R b }$ ground-stateperfineslitga atomic fountain,Europhys.Lett.45,558-564.   
[6.62] J.P.Gordon,H.J.Zeiger,C.H.Townes (1994).The maser: Newtypeof microwaveamplifier,frequency standardand spectrometer,Phys.Rev.99, 1264-1274.   
[6.63] N.G. Basov, A.M. Prokhorov (1955). The theory of a molecular oscillator and a molecular power amplifier,Discuss.Faraday Soc.19,96-99.   
[6.64]D.Kleppner,H.M.Goldenberg,N.F.Ramsey(1962).Theoryof thehdrogen maser,Phys.Rev.126,603-615.   
[6.65]D.eper,H.C.Berg,S.B.Camton,N.F.amsey,R.F.C.sot, H.E.Peters,J.Vanier(1965).Hydrogen maserprinciplesand techniques,Phys. Rev.138,A972-A983.   
[6.66] N.Koshelyaevsky (1991).H-masers inthe USSR,Proc.5th European Time andFrequency Forum4i5-434 (Besancon,France).   
[6.67]R.F.C.Vessot,M.W.Levine,L.Mueller,M.Baker (1967).The design of an atomic hydrogen maser system for satelite experiments,Proc.21st Annual Frequency Control Symposium512-542(Atantic City,USA).   
[6.68]H.E.Peters,T.E.McGunigal,E.H.Joson(1968).Hydrogenstandardorkat GoddardSpaceFlightCenterProc.22ndAnnual FrequencyControl Symposium 464-492 (Atlantic City,UA).   
[6.69] H.E. Peters, B.H. Owings, T. Oakley, L. Beno (1987). Hydrogen maser for radioastronomy,Proc.41stAnnual FrequencyControlSymposium75-1 (Philadelphia, U).   
[6.70] B.A. Gaygerov,F.S. Rusin, V.P.Sysoev (1991).Portable atomic clock on the basisof anactive hydrogen maser,sapphire,Proc.5th European Time and FrequencyForum293-295(Besancon,Frce).   
[6.71] H.G. Andresen, E. Pannaci (1966). Servo controlled hydrogen maser cavity tuning,Proc.20th Annual Frequency Control Symposium 402-415(Atlantic City,USA).   
[6.72] N.A.Demidov,E.M.Ezhov,B.A.Sakharov,B.A.Ujanov,A.Bauch B.Fischer (1992). Investigation of the frequency instability of CH1-75 hydrogenmasers,Proc.6th European Timeand Frequency Forum409-414 (Noordwijk,Holland).   
[6.73] C. Audoin (1981).Fast cavity auto-tuning system for hydrogen maser, Rev. Phys. A16,125-130 and17,273.   
[6.74] N. Yahyabey, R. Barillet. J. Viennet, C. Audoin (1987). Accord automatique de lacavite resonnante d'horloges a hydrogene: résultats preliminaires,Proc. Ist European Time and Frequency Forum 334-338 (Besancon,France).   
[6.75] C. Audoin, J. Viennet,P. Lesage (1981). Hydrogen maser: active or passive?, J. Phys. 42 Suppl. 12, C8-159-C8-170.   
[6.76] D.A. Howe, F.L. Walls, H.E. Bell, H. Hellwig (1979). A small, passively operated hydrogen maser,Proc. 33rd Annual Frequency Control Symposium 554-562 (Atlantic City， USA).   
[6.77] E.M. Mattison, E.C. Blomberg, G.U. Nystrom, R.F.C Vessot (1979). Design, construction and testing of a small passive hydrogen maser,Proc.33rd Annual Frequencyontrol Symposium549-553(tlanticCityU).   
[6.78] H.E.Peters (1978). Small,very small and extremely small hydrogen masers, Proc.32nd Annual Frequency Control Symposium 469-476(Atlantic City, USA).   
[6.79] N.A. Demidov, A.A. Uljanov (199o). Design and industrial production of frequency standards inthe USSR,Proc.22nd Annual Precise Time and Time Interval Applications and Planning Meeting 187-208(Vienna,USA).   
[6.80] R.V.Pound (1947).Frequency stabilization of microwave oscillators,Proc. IRE 35,1405-1415.   
[6.81] G.Busca(1979).PassiveH-maser,Proc.33rd Annual Frequency Control Symposium 563-568 (Atlantic City，UA).   
[6.82]L.S.Cutler,C.L.Searle (1966).Some aspects of the theory and measurement of frequency fluctuations infrequency standards,Proc.IEEE 54,136-154.   
[6.83] D.A. Howe,F.L. Wals (1983). A compact hydrogen maser with exceptional long-termstability,IEEETrans.Instrum.Meas.32,218-223.   
[6.84]E.M.Mattison (1992).Physics of systematic frequency variations in hydrogen masers,IEEE Trans.Instrum.Meas.39,250-255.   
[6.85]R.F.C.Vessot,E..atison,R.L.Wasworth,I.F.ivera,H.P.Goid, C.C.Agosta (1987).A hydrogen maser at temperatures below 1 K, IEEE Trans.Instrum.Meas.36,588-593.   
[6.86] M.E. Hayden, M.D. Hurliman, W.N. Hardy (1996). Measurement of atomic-hydrogen spin-exchangeparameters at 0.5Kusing acryogenic hydrogenmaser,Phys.Rev.A53,589-1604.   
[6.87] M. Arditi (1958). L'influence des gaz tampons sur le deplacement de la frequenceetla largeur des raies des transitions hyperfines del'etat fondamentaldeatomesalcalins,J.hs.dium1980   
[6.88]M.Arditi, T.R.Carver (1961).Pressure,lightand temperature shiftsinoptical detection ofO-0hyperfine resonance ofalkali metals,Phys.Rev.124,800-809.   
[6.89]M.ArditiT.R.Carver(964).HyperfinerelaxationofopticallypumpedRb87 atoms in buffer gases,Phys. Rev.136A,643-649.   
[6.90]M.Arditi(96o).Agasellatomicclockasahigh-stabilityfrequency standard,ans.il.Electron.4.   
[6.91]R.J.peterE..atyP.der,.ito.toe(96). prototype rubidium vapor frequency standard, IRE Trans. Instrum.9,132-135.   
[6.92] M.E.Packard, B.E.Swartz (1962). The optically pumped rubidium vapour frequencydard,ns.rum.1.   
[6.93]M.Bloch,1.Pascaru,C.Stone,T.McClelland(1993).Subminiaturerubidium frequency standard for commercial applications.Proc.IEEE International FrequencyControlSympoium164177(SaltLakeCityU).   
[6.94] P.Rochat,H. Schweda.G. Mileti,G.Busca (1994).Miniaturized rubidium clocks for space and industrial applications,Proc.8th European Timeand   
[6.95] W.J.Riley (1992).The physics of the environmental sensitivityof rubidium gascellccsr Contr. 39,232-240.   
[6.96] J.C.Camparo, R.P. Frueholz (1986). Fundamental stability limit for the diode-laserdoiccyrd,Jp. 3313-3317.   
[6.97] Y.Saburi,T.Koga,S.Kinugawa,T.Imamura,H.Suga,Y.Ouch(994). Shorttermstabilityoflaser-pumpedrubidiumgascellfrequencystadard Electron.Lett.30,665.   
[6.98] G.Mileti, P.Thomann (1995). Study of the S/N performance of passive atomicclocksusingalaser pumpedvapour,Proc.9th European Timeand Frequency Forum27-276(Besancon,race).   
[6.99] M.Tetu,G.Busca,J.Vanier(973).hort-termfrequencytabilitythe $\mathrm { R b } ^ { 8 7 }$ maser,IEE   
[6.100]G.usca,R.roueau,J.anier(975).Longtermrequencyabty the $\mathrm { R b } ^ { 8 7 }$ maser,IEEs.um..24996   
[6.101]W.Paul(199o).Electromagnetictrapsforhargedandneutralparticles, Nobel lecture,Rev.od.Phys.62,31540   
[6.102]F.G.Major,G.Werth(1973).High-resolution magnetic hyperfineresonance in harmonicallybound ground-state $^ { 1 9 9 } \mathrm { H g }$ ions,Phys.RevLt.3, 1155-1158.   
[6.103] M.D.McGuire,R. Petsch,G. Werth (1978).Precision determinationof the groundstatepfiesepaatioin $^ { 1 9 9 } { \mathrm { H g } } ^ { + }$ usingteionstoragetechque Phys.Rev.A17,1999-2004.   
[6.104] .Jardino,.eainusien,R.Barillet,J.Viennet,P.Petit,C.oin (1981).Freqecystabilityofamercuryionreuecysadard,Al.. 24,107-112.   
[6.105] L.S.Cutler,R.P.Giffard,M.D.McGuire (1981).A trapped mercury199 ion frequencystandard,Proc.3thnnualPrecise TimeandTime Ieal Applications and Planning Meeting 563-578(Washington D.C.,USA).   
[6.106] L.S.Cutler,R.P.Giffard,M.D.McGuire (1985).Thermalizationof $^ { 1 9 9 } { \mathrm { H g } } ^ { + }$ ion macromotion by a light background gas in an RF quadrupole trap,Appl. Phys.B36,137-142.   
[6.107] J.D.Prestage,R.L.Tjoelker,G.J.Dick,L. aleki (1992). Ultra-stable $\mathrm { H g ^ { + } }$ trapped ion frequency standard, J. Mod.Opt.39,221-232.   
[6.108] R.L.Tjoelker,J.D.Prestage,G.J.Dick,L. Maleki (1993).Long termstability of $\mathrm { H g } ^ { \mp }$ trapped ionfrequencysandardsProc.EEEInternational Frequency Control Symposium 132-138(Salt Lake City,USA).   
[6.109] R.L.Tjoelker,J.D.Prestage,L.Maleki (1995).Record frequencystability withmercury inalineariontrapProc.FifthymposiumonFrequency Standardsandetrology33-38(Woods Hole,USA)ed.J.C.ergquist (World Sientific,ingre).   
[6.110]D.J.Berkeland,J.D.iler,J.C.Berquist,W..Itano(1998).Laser-ooled mercury ionfruencydard,hys.ev.Lett.92.   
[6.111] D.J.Berkeland,F.C.Cruz,J.C.Berquist (1997).Sum-frequency generatioof continuous-wave light at $1 9 4 ~ \mathrm { { n m } }$ ,Appl.Opt.36,4159-4162.   
[6.112] C. Tamm,D.Schnier, A.Bauch (1995). Radio-frequency laser double-resonance spectroscopy of trapped $^ { 1 7 1 } { \mathrm { Y b } } ^ { + }$ ions and determinationof line shifts of the ground-state hyperfine resonance,Appl. Phys.B60,19-29.   
[6.113] M.J. Sellars, P.T.H. Fisk,M.A. Lawn, C.Coles (1995). Further investigation of a prototype microwave frequency standard based on trapped $^ { 1 7 1 } { \mathrm { Y b } } ^ { + }$ ions. Proc.International Frequency Control Symposium 66-73(San Francisco USA).   
[6.114] D.J.Wineland,W..Itano (1987).Laser cooling,Phys.Today,June issue, 2-8.   
[6.115] D.J. Wineland, J.C. Bergquist, D. Berkeland, J.J. Bolinger, F.C. Cruz, W.M. Itano,B.M. Jelenkovic, B.E. King, D.M. Meekhof, J.D.Miller, C. Monroe, M.Rauner, J.N. Tan (1995). Application of laser cooled ions to frequency standardsandmetrology，Proc.Fifth Symposiumon Frequency Standardsand Metrology 11-19 (Woods Hole,USA) ed.J.C.Bergquist (World Scientific, Singapore).   
[6.116] J.J. Bollinger,D.J. Wineland, W.M. Itano (1995). Spin squeezing applied to frequency standards,Proc.FifthSymposium onFrequency Standards and Metrology 107-114(Woods Hole, USA) ed. J.C. Bergquist (World Scientific, Singapore).   
[6.117] A.Godone,E. Bava, C.Novero (1988).Mg beam frequency standard, Fourth Symposium on Frequency Standardsand Metrology78-83(Ancona,Italy)ed. A.de Marchi (Springer,Berlin).   
[6.118] C.Daussy,F.Ducos,G.D.Rovera,O.Acef (2oo0).Performanesof $\mathrm { O s O } _ { 4 }$ stabilized $\mathrm { C O } _ { 2 }$ lasersas optical frequency standards near 29 THz, IEEE Trans.Utraon.,erroelec.,req.ontr.47.   
[6.119] S..Bagayev,A.K.DmitriyevP.V.PokasovB.. vortsov(1995). $\mathrm { H e - N e / C H _ { 4 } }$ laser frequency standard for precise measurements,Proc.Fifth Symposium on Frequency Standardsand Metrology 289-296(Woods Hole, USA) ed. J.C.Bergquist (World Scientific,Singapore).   
[6.120] H.G.Dehmelt (1982).Mono-ion oscillator as potential ultimate laser frequency standard,EEE Trans.Instrum.Meas.31,3-87   
[6.121]E.Peik,G.Hollemann,H. Walther (1994).Laser cooling and quantum jumps of a single indium ion,Phys.Rev.A49,4048.   
[6.122] W.Nagourney,E.Burt,H.G.Dehmelt (1995).Optical frequencysadard using individual indium ions,Proc.Fifth SymposiumonFrequencyStandards and Metrology 341-346 (Woods Hole, USA) ed.J.C.Bergquist (World Scientific,Singapore).   
[6.123]R.J.Rafac,B.C.Yung,J..Beall,W..Itano,D.J.Wineland,J.C.r (2000).Sub-decahertzultravioletspectroscopyof $^ { 1 9 9 } { \mathrm { H g } } ^ { + }$ Phys.Rev.Lett. 85,2462-2465.   
[6.124] T.Udem,J. Reichert,R.Holzwarth,T.W.Hansh (1999). Absoluteoptical frequency measurement of the cesium D1 line with a mode-locked laser, Phys. Rev.Lett. 82,3568-3571.   
[6.125] S.A.Diddams,D.J.Jones,L.-S.Ma,S.T.CundiffJ.L.Hall (2o).Optical frequency measurement acrossa 104 THz gapwithafemtosecond laser frequency comb,Opt.Lett.25,.

# Chapter 7

[7.1]L.Fairhead,P.Bretagnon (199o). An analytical formula forthe time transformation TB-TT,Astron.Astrophys.229,240-247.   
[7.2] Bureau international del'heure (1994).Rapport annuel pour1973 (Observatoire de Paris).   
[7.3] B. Guinot, C. Thomas (1988). Establishment of International Atomic Time, Rapporteldelonuu1 France).   
[7.4] J. Azoubib,M.Granveaud,B.Guinot (1977).Estimation of thescaleunit durationof timescales,etrologia1393.   
[7.5] B.Guinot,M.essel,.Laclare(97).reauinteraioalehur (1970).Rapport annuel pour I969(ObservatoiredeParis).   
[7.6] F.Arias (2ooo).Private communication.   
[7.7] B.Guinot (1988).Atomic time scales for pulsar studies and other demanding applications,Astron.Astrophys.192,370373.

# Chapter 8

[8.1] B. Guinot (1979). Basic problems in the kinematics of the rotation of the Earth,Timeh'sel Boston, London).   
[8.2] N. Capitaine, B. Guinot,J. Souchay (1987). A non-rotating origin on the instantaneous equator: definition,properties and use,Celest. ech.39, 283-307.   
[8.3] N. Capitaine, B.Guinot,D.D.McCarthy (20oo). Definition of the Celestial Ephemeris Origin and of UT1in the International Celestial ReferenceFrame, Astron. Astrophys.355,398-405.   
[8.4] S.Aoki,B.Ginot,G..aplan,H.ioshita.arthy P.K.Seidelmann (1982).The new definition of Universal Time,Astron. Astrophys.105,359-361.   
[8.5] IERSConventions (1996).IERS Technical Note21,ed.D.D.McCarthy (Paris Observatory, France).   
[8.6] International Earth Rotation Service.Annual Report (Paris Observatory, France). See Appendix 4.   
[8.7] International Earth Rotation Service.Bulletin B(monthly edition,Paris Observatory, France). See Appendix 4.   
[8.8] K.Lambeck (1980).The Earth's variable rotation (Cambridge University Press,Cambridge).   
[8.9] A.Cazenave,K.Feigl(1994).Formes etmouvementsde la Terre (CNRS Editions,Paris).   
[8.10] G.D.Egbert,R.D.Rey (2ooo).Significant dissipation of tidal energy in the deep ocean inferred fromsatellitealimeterdata,Nature405,775-778.   
[8.11] F.R.Stephenson,L.V.Morrison(198o).Phil.Trans.R.Soc.Londoner.A 313,47.   
[8.12] F.Mignard (1994).Hipparcos: une mission dastrometrie spatiale,Bulletin Bur.Nat.Metrologie95,11-17.   
[8.13] J. Kovalevsky et al. (1992). The FAST Hipparcos data reduction consortium: overview of the reduction software,Astron. Astrophys.258,7-17.   
[8.14] J. Kovalevsky et al. (1995). Construction of the intermediate Hipparcos astrometriccatalogue,Astron.Astrophys.304,34-43.   
[8.15] D.Benest,C.Froeschle (eds.) (1992).HPPARcOS,une nouvelle donne pour l'astronomie(Observatoire de la Cote d’Azur et Societe francaise des specialistes d'astronomie,Goutelas).   
[8.16] A. Hewish,S.J.Bell, J.H. Pikington,P.F.Scot,R.A. Collins (1968). Observation of a rapidly pulsating radio source,Nature 217,709-713.   
[8.17] D.C. Backer,R.R. Kulkarni, C. Heiles,M.M. Davis,W.M. Goss (1982). A millisecond pulsar, Nature 300, 615-618.   
[8.18] G.Petit, P. Tavella(1996).Pulsars and time scales,Astron. Astrophys. 308, 290-298.   
[8.19] J.H. Taylor,A.Wolszczan,T. Damour, J.M. Weisberg (1992). Experimental constraints onstrong field relativistic gravity,Nature 355,132.   
[8.20] N. Mashall (1993). Des pulsars binaires aux ondes gravitationnelles,La Recherche 260,1390--1391.   
[8.21] B.Guinot (1989). General principles of the measure of time,astronomical time,in Reference frames inastronomyand geophysics,351-377,eds.J. Kovalevsky,I.I. Mueller,B.Kolaczec (KluwerAcademic Publishers, Dordrecht,oton,).

# Chapter 9

[9.1] B. de Beauvoir, C. Schwob, O. Acef,L. Josefowski, L. Hilico,F. Nez, L. Julien,A. Clairon, F. Biraben (1997). Metrology of the hydrogen and deuterium atoms: determination of the Rydberg constant and Lamb shifts, Eur.Phys.J.D12,61-93,and references therein.   
[9.2] H.Dehmelt (199O). Experiments with an isolated subatomic particle at rest, Nobellecture,Rev.Mod.Phys.62,525-530.   
[9.3] H.Gabrielse,X. Fei,L.A. Orozco,R.L. Tjoelker,J. Haas,H. Kalinowsky, T.A. Trainor, W.Kells (1990). Thousandfold improvement in the measured antiproton mass,Phys.Rev.Lett.65,1317-1320.   
[9.4] R.S. van Dick,D.L. Farnham,P.B.Schwinberg (1995). Proton-electron mass ratio and the electron's atomic mass,IEEE Trans. Instrum.Meas.44, 546-549.   
[9.5] T. Kinoshita (1995). New value of the $\alpha ^ { 3 }$ electron anomalous magnetic moment,Phys.Rev.Lett.75,4728-4731.   
[9.6] S.Weinberg (1989). Testing quantum mechanics,Ann. Phys.194,336-386.   
[9.7] J.J. Bollinger,D.J.Heinen,W.N.Itano,S.L.Glbert,D.J. Wineland (1989). Test of the linearity of quantum mechanics by rf spectroscopy of the $^ { 9 } \mathrm { { B e } ^ { + } }$ ground state,Phys. Rev.Lett.63,1031-1034.   
[9.8] R.L. Walworth,I.F. Silvera, E.M. Mattison, R.F.C. Vessot (199o). Test of the linearity of quantum mechanics in an atomic system with a hydrogen maser, Phys.Rev.Lett. 64,2599-2602.   
[9.9] G.D.Fletcher, S.J. Lipson, D.J. Larson (1987). Observation of a magnetic-field-dependent g-factorratio,Phys.Rev.Let 58,2535-2538.   
[9.10] N.Fortson(1987).New term inatomic Zemanenergy,hys.Rev.Let.59, 988-990.   
[9.11] A. de Marchi (1993). The high C-field concept for an accurate cesium beam resonator,Proc.7th European frequency and time forum 541-548 (Neuchatel Switzerland).   
[9.12] C.M.Will(1993).Theoryandexperiment ingravitational physics(revised edn.) (Cambridge University Press,Cambridge).   
[9.13] T.Damour (1994). Gravitation and quantizations,Proc. LVIith Les Houches summerolJu.aui Amsterdam).   
[9.14]P.Wolf (1997).Relativity and the metrologyof time,PhD.Thesis,Queen Mary and Westfield College,UniversityofLondon. (Also Monographie 97/1, BIPM,Sers,997.)   
[9.15] J.C.Hafele,R.E.Keating (1972).Around-the-worldatomicclocks: predicted relativistictedisiceticee 77,166-170.   
[9.16] R.V.Pound,G.A.RebkaJr.(96).Apparent weightofphotons,Ps.Rev. Lett. 4, 337-341.   
[9.17]R.V.Pound,G.A.RebkaJr.,J.L.Snider (1965).Effectof gravityonamma radiation,ys.evLett.4803.   
[9.18] R.F.C.Vessot,M.W.Levine (1979).Atest of theequivalence principleusing aspace-borneclock,J.Gen.Rel.Grav.10,181-204.(SeealsoR.F.C.Vesso et al.(1980).Phys.Rev.Lett.45,2081-2084.)   
[9.19] A.Godone,C.Novero,P.avella,K.ahimullah(1993).Nwexprital limitstothetimevariationsof $g _ { \mathrm { p } } ( m _ { \mathrm { e } } / m _ { \mathrm { p } } )$ and $\alpha$ ,Phys.Rev.Lett.71, 2364-2366.   
[9.20] A. Godone,C. Novero,P. Tavella (1995). Null gravitational redshift experiment withon-identicalatomicclocks,Phys.Rev.51,319-23.   
[9.21] J.D.Prestage,R.L. Tjoelker,L. Maleki (1995).Atomicclocks and variations of thefineucreots.evLett7414.   
[9.22] A.A.Micheson,E.W.Morley (1887).Am.J.Sci.34,333.   
[9.23] T.P. Krisher,L.Maleki,G.F.Lutes,L.E.Primas,R.T.Logan,JD.Adeon C.M.Will(1990).Test of the isotropy of theone-way speed of light using hydrogen-maser frequencystandards,Phys.Rev.D(apid Commun.)42,731.   
[9.24] P.Wolf(995).ooedatellitetstofsialelaivityysv5 5016-5018.   
[9.25] P. Wolf,G. Petit (1997). Satellite test of special relativity using the GPS, Phys.Rev.A56,4405-4409.   
[9.26] I.I.Shapiro (1990).General relativity and gravitation,313,eds.N.Ashby D.F.Bartltt,W.s(geesitys,e).   
[9.27] K.Nordtvedt Jr.(1973). Post-Newtonian gravitational effects in lunar laser ranging,Phys.Rev.D.7,2327-2356.   
[9.28] R.N. Treuhaft,S.T. Lowe (1991). A measurement of planetary relativistic deflection,Astron.J.102,1879-1888.   
[9.29] K.Nordtvedt Jr.(1968).Equivalence principle formassvebodies: IITheory Phys. Rev. 169,1017-1025.   
[9.30] C.M.Will (1971). Theoretical frameworks for testing relativistic gravity: II Parametrized post-Newtonian hydrodynamics and the Nordtvedt effect, Astrophys.J. 163,611-628.   
[9.31] Guide to GPS Positioning (1986).Ed.D.Wells (Canadian GPS Associates).   
[9.32] B.Guinot, W.Lewandowski (1989).Improvement of the GPS time comparisons by simultaneous relative positioning of the receiver antennas, Bull.Geodesique63,371-86.   
[9.33] B.Juompan,P.Uhrich,M. Brunet (1995). Aspects temps du complément europeen au Global Positioning System(CE-GPS): resultats experimentaux des phasescontinentales ettransatlaniques,Bull.Bureau Nat.Metrologie 101, 13-24.   
[9.34] M.Brunet (1992). DORIS precise orbit determination and location system, performance of ultra stable oscillators,Proc.6th European Frequency and Time Forum 125-136(Noordwijk,Holland).   
[9.35] W.Schafer, H. Wilmes (1986).Precise range and range-rate equipment (PRARE).System design and status of development,Workshop on advances in satelliteradiotracking (Austin,s).   
[9.36] R.T.Schilizi (1995). Current development in VLBI astronomy on the ground and in space,RadioSci.Bull.274,14-28.   
[9.37] D.Benest, C.Froeschle (eds.) (1992). HiPPARCOS,une nouvelle donne pour l'astronomie (Observatoire de la Coted'Azur et Societé francaise des spécialistesd'astronomie,Goutelas).   
[9.38] L.Lindegren, J. Kovalevsky (1995). Linking the Hipparcos catalogue to the extragalacticreferencesystem,Astron.Astrophys.304,189-201.   
[9.39] CNES (1986). Announcement of opportunity: altimetry research in ocean circulation,TOPEX/POSEIDON,a CNES/NASA oceanographic stellite.   
[9.40] B.Dubouis (1986). Temps frequences dans les telecommunications francaises,Bull.BureauNat.Metrologie63,58-67.   
[9.41] P.Kartaschoff (1991).Synchronization in digital communications networks, Proc.IEEE79,1019-1028.   
[9.42] CCDS(1993). Rapport de la 12eme session (see p. S17 and recommendation S5, p. S29).

# Index

absolute space,17,19 time,6,17   
absorption,116   
accuracy frequency,55,66,788 of TAI readings,252   
active clock,126   
algorithm for frequencystability,243-245 for TAI,241 for time scale,60,240-241   
Algos,247   
alkali atom, 110-116   
Allan variance definition, 74 estimator,76,78 modified, 80 practical calculation,76-79 systematic effects,79 variation,75   
apparent solar day,38 time,40   
astronomical unit of length,30   
atomic fountain,130,177-180   
atomic second,56,236   
atomic time integrated,56,57 local independent,258   
barycentric coordinate system,29   
Barycentric CoordinateTime(TCB),30,238   
Binary Pulsar Time (TBP),284   
Boltzmann'saw,20   
Breit-Rabi formula, 114,149   
caesium clock cold atom fountain,177 frequency shifts,147-159,168-169,181 inaccuracy,161,169,183 long termfrequencyinstability60,16 magneticallydeflectedbeam,30-162 medium term frequency instability,144 167,181 non-reproducibility,160,169 optically pumped beam,162-170   
cavity pulling,128   
celestial frame,276 pole,265 sphere,267   
Celestial Ephemeris Origin,268   
Celestial Ephemeris Pole (CEP),65   
Celestial IntermediatePole(),65   
chaos,7   
civil time,42   
clock active,126 comparison, 35 definition, 65 in space,183 master,247 passive,126,129,147 primary, 262 transition,115 transportation,93,291   
closing error,93   
common view method,99   
comparison of clocks,35 of frequencies,104-108 of times,59,90-104   
coolingatoms by Doppler efect,171 by Sisyphus effect,174 launching the atoms,176   
cooling ions collisional method,24 radiative method,29   
coordinate quantity,22,28 simultaneity, 35 synchronisation,35,37 time (definition),1,28,7   
coordinate system,17 barycentric,29 geocentric, 29   
CoordinatedUniversal Time,39,255-259   
cycling transition,122,166   
date,17,38   
day,lengthof,266   
definitive time,45   
Dickecondition,24,223   
Doppler cooling,171   
Doppler effect,23 Dicke condition,124,223 elimination,123-125 for positioning,301 for satellite tracking,272 frequency shift, second order,125,151   
DORIS,272,301,306   
double resonance method,211   
duration,7   
Earth Reconnaissance Satellites (ERS),302 303,305   
Earth rotation,264 irregularities,47,273-276 measurement,269-273 parameters,265,278   
Echelle atomique libre (EAL),242   
Einstein's equivalence principle,21,109   
ellipsoid,rerence,   
energy-timeuncertainty relation,118   
ephemeris,10,13,276   
Ephemeris Time,15,50-51 definition,278-279 determination,279-280   
equation of time,40,41   
equinox,269   
event,17   
excited state,110   
fine structure,110   
fluctuations model, 72-73 power spectral density, 71   
fluorescence,117   
frequency instantaneous,68 nominal, 57 normalised, 57   
frequency accuracy,55,66,7-88   
frequency comparison,104-108   
frequency instability definition,67 measurement, 70   
of atomic clocks,147 of TAI,254   
frequency noise,73   
frequency shift Doppler, 123 gravitatioal,,92 hydrogen maser,207 in caesium clock,147-159,168-169,181 in rubidium clock,215 mercury ion clock,228   
frequency standard characteristics,234 inaccuracy,234 magnesium beam,231 mercury ion,224-229 optical, 1 primary,129 primary and secondary, 65 single ionatrest,231 ytterbium ion, 229   
frequencysteering,243,246

Galilean relativity principle,19   
geocentric coordinate system,29   
Geocentric Coordinate Time (TCG),30,237   
geoid,31,03   
Global Positioningystem,60,98,297-301   
GLONASS,98,100,01   
GLONASS Time,262   
GMT,42   
GPS,60,98,297-301   
GPS Time,98,261   
gravitation,15,26,291   
gravitational   
frequency shift,32,292   
potential (terrestrial), 32   
Greenwich Mean Time,42   
ground state, 110

HIPPARCOS, 277,302   
hydrogen maser, 184-211 active,191-201 cavity tuning,192-195,199-201 cryogenic,210 frequency shifts,207 inaccuracy,209 induced magnetic moment,193 Iong term frequency instability,209 medium term frequency instability,206 oscillation condition,191 passive,201-206   
hyperfine filter,212 structure, 111-116   
ICRF,31,264,302   
inaccuracy,88 of caesium clock,161,169,183 of frequency standards,234 of hydrogen maser,209 of mercury ion clock,229 of TAI frequency,254   
induced emission17   
inertial system,19   
instability frequency, 67,70 time,67,69,81   
instantaneous axis of rotation,265 frequency,68 longitude origin, 267   
instrumental delay,90   
integrated atomic time,56,57 time scale,12   
International AtomicTime,60,237-239 accuracy of readings,252 algorithm,241 frequency inaccuracy,254 frequency instability,254 origin,237 scale unit, 106,237,260   
International Celestial Reference Frame,31, 264,302   
International GPS Service (IGS),272,300   
International Laser Ranging Service (ILRS), 272   
International Terrestrial Reference Frame,31, 264   
interval,22,25   
ion confinement micromotion, 221 Paul trap,218 restoring force,221 secular motion,222 three-d quadrupole field,219 two-d quadrupolefield,218   
ITRF,31,264

Josephson effect,288   
JulianDate (JD),39   
laser ranging,272,306   
LASSO,102   
leap second,256   
length of day,266   
Loran-C,59,97   
Lorentz transformation, 21   
lunar   
month,39   
reflecting panels,272   
lunation,39

Iunisolar precession-nutation265   
magnesium beam frequency standard,231   
magnetic deflection,120,13 shielding,125   
master clock,43,247   
mean solar time,40,46   
mercury ion clock frequency shift,28 inaccuracy,229 long term frequency instability,229 medium term frequency instability,228   
mercury ionfrequency standard,224229   
metric,22 tensor,25   
Minkowski metric, 22   
Modified Julian Date (MJD),39   
$N$ -sample variance,74   
Navsat,72,   
Newton’s firstlaw,18   
noise frequency,73 shot,144 thermal, 206   
nominal frequency,57   
non-rotating origin,268   
normalised frequency,57   
optical detection,122 frequencystandard,231 molasses,173 pumping,121   
origin instantaneous longitude,267 non-rotating,268   
passive clock,126,129,147   
Paul trap,218   
pendulum clock, 83   
physical constants,289   
piezoelectric effect,84   
pole celestial, 265 terrestrial,265   
power spectral density,71   
PPN formalism,294   
PRARE,302   
precession-nutation,lunisolar,265   
primary clock,262   
proper frequency,87,104 quantity,28 second,36 time,10,21,65,69,236

pulling   
cavity,128   
Rabi,157   
Ramsey,157   
pulsar spin-down,283   
Pulsar Time,64,281-285   
pumping   
optical, 121   
transition,122   
two-laser,166

quality factor of atomic resonance,118 resonant cavity,55   
quantum Hall effect, 288   
quartz oscillator,84,140-144,196-199,204, 228   
quasar,24,29,31,100,270   
Rabi frequency,189 pedestal, pulling,157   
Ramsey fringe,133 pulling,157   
Ramsey method by separated oscillating fields,131 Rabi pedestal,3 response curve, 135 time domain,227,230   
reference ellipsoid,03   
relative frequency offset,57,68   
relativity principle,Galilean,19   
reproducibility postulate,7   
resonance curve,133,35,141,151,165,179, 202,227   
resonant cavity quality factor, 155   
rise time,91   
rotation, 24 of the Earth,47,264,269-276   
rubidium clock,211-217 double resonance, 211 frequency shifts,215 hyperfine filter,212 long term frequency instability,216 medium term frequency instability,215   
Sagnac effect, 96   
scale unit,28,237 TAI, 106,237, 260   
second atomic,56.236 leap,256 of Ephemeris Time, 50 of mean time, 46 proper,36 unit of duration, 12   
selection rules, 116   
SelectiveAvailability (SA),99,99   
servo control of amplitude, 155 of frequency,143 of magnetic feld,5 of phase,198   
shot noise,144   
sidereal time,43,269   
signal transmission,92,95,100   
simultaneity,17 coordinate,35   
Sisyphus effect,174   
speed of light, 19   
spontaneous emission,117   
stabilityalgorithm,243-245   
standard frequency emissions,260   
Stark effect,116 second order,150   
state preparation,119   
steering,offrequency,243,246   
stellar angle,267   
stored ion clock,217-230   
synchronisation coordinate,35,37 Einstein convention,20   
TAI,60,237-239 accuracy of readings,252 algorithm, 241 frequency inaccuracy,254 frequency instability,254 origin,237 scale unit,106,237,260   
telecommunications,306   
terrestrial frame,276 pole,265   
Terrestrial EphemerisOrigin,268   
TerrestrialeT)   
thermal noise,206   
three-corner hat method, 83   
tidalel   
time absolute, 6,17 coordinate,11,28,37 proper,10,21,65,69,236   
time comparison methods. 90--104 need for, 59   
time instability characterisation, 81 definition, 67 measurement, 69   
time interval counter, 91   
time scale algorithm,60,240-241 integrated,12,57 notion,10   
time signal,6   
timestandard,pimry9   
time zone,41   
timekeeper,43   
TOPEX-POSEIDON,272,301,303-306   
transition clock,115 cycling,122,166 pumping,122   
tropical year,38   
two-laser pumping,166   
two-sample variance,74   
two-waytimetransfer,92,100   
uncertainty rela+ion,energy-time,118   
unit of proper time,22   
Universal Time,43,264-278 definition,264-266 measurement techniques,269-273 other forms,269 use,276   
UT1,266-269   
UTC,39,255-259

VLBI,270,302,06

WorldGeodetic System,99 worldline,

ytterbium ion frequency standard,229

Zeeman effect,114   
second order,148

![](images/b2429d60909f1f9e06f40c189d7353d63ec719789a7e14c814d0f51c49e513b1.jpg)

![](images/5e40e8ba84c17c67ccf798cdaed22b6a4e335549ae8fbd19b7e8ff37f1c9b1fd.jpg)

# TheMeasurementofTime

This book provides a comprehensive introduction to the physics of time and time measurement,from an historical perspective to the modern day.It discusses the stability and accuracy of atomic frequency standards,including different types of oscillatorsand atomic clocks,and covers the most recent developments and uses of these devices.The precision of atomic clocks and the atomic time scale are considered in the context of fundamental physical research,with relation to general relativityand searches for possible timevariation in the fundamental constants.The authors also discuss International Atomic Time and its relationship to Coordinated Universal Timeand thetime scales used inastronomyas well as applications such as the Global Positioning System (GPS).

The book will be ideal asan introduction for graduate students or researchersenteringthefieldsoftimeand frequencymetrology and precise astronomical observation.It willalso be useful asareference for scientists working in these and otherapplied areas,such as geophysics,atomic physics,astronomyand telecommunicaions. General readers witha background in science should also find this a fascinating book.