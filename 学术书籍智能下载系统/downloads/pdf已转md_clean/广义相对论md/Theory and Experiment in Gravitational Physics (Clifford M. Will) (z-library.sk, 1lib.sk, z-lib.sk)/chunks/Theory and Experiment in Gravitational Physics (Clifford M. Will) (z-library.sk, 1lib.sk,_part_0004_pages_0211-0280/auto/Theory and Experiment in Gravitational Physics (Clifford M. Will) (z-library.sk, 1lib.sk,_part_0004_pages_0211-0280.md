fixed bearing on the Earth’s surface. Detailed observation of the orientation of the rotors during such “resonant jumps” showed just such loxodromic behavior. In the end, every jump of every rotor could be identified by its “mode number,” the integer relating its polhode period to the spacecraft roll period.

The original goal of GPB was to measure the frame-dragging precession with an accuracy of one percent, but the problems discovered over the course of the mission dashed the initial optimism that this would be possible. Although the GPB team were able to model the effects of the patches, they had to pay the price of the increase in error that comes from using a model with so many parameters. The experiment uncertainty quoted in the final result—roughly 20 percent for frame dragging—is almost totally dominated by those errors (Table 9.1). Nevertheless, after the model was applied to each rotor, all four gyros showed consistent Lense-Thirring precessions. Gyro 2 was particularly “unlucky”—it had the largest uncertainties because it suffered the most resonant jumps. Numerous cross-checks were carried out, including estimating the relativity effect during different segments of the 12-month science phase (various events, including computer reboots and a massive solar storm in January 2005, caused brief interruptions in data taking), increasing and decreasing the number of parameters in the torque model, and so on.

When GPB was first conceived in the early 1960s, tests of general relativity were few and far between, and most were of limited precision. But during the ensuing decades, there was enormous progress in experimental gravity in the solar system and in binary pulsars. By the middle 1970s, some argued that the PPN parameters $\gamma$ and $\alpha _ { 1 }$ were already known to better accuracy than GPB could ever achieve. Given its projected high cost, critics argued for the cancellation of the GPB mission. The counterargument was that all such assertions involved theoretical assumptions about the class of theories encompassed by the PPN approach, and that all existing bounds on the post-Newtonian parameters involved phenomena entirely different from the precession of a gyroscope. All these issues were debated, for example, in the 1994 National Academy review of GPB that recommended its continuation.

Disclosure: The author was a member of the 1994 NAS panel that recommended completion of GPB, and served as Chair of an external NASA Science Advisory Committee for Gravity Probe B from 1998 to 2011.

strategy, and the one adopted by GPB, is to put the gyros into a polar orbit, so that $\hat { \pmb { h } } { \cdot } \pmb { S } _ { 2 } = 0$ . This reduces the amplitude by a half, but with $\pmb { S } _ { 1 }$ lying in the orbital plane to maximize the geodetic effect, the frame-dragging precession will now be perpendicular to the orbital plane. By separately measuring the north-south (geodetic) precession and the east-west (frame-dragging) precession, one can make a clean measurement of both effects, at least in principle. Dividing Eq. (9.3) by the orbital period $P = 2 \pi ( a ^ { 3 } / m ) ^ { 1 / 2 }$ , we obtain the rate of angular precession in the two directions given by

$$
\frac { d \hat { \pmb S } _ { 1 } } { d t } = \Omega _ { [ \mathrm { G e o } ] } \pmb { e } _ { \mathrm { N S } } + \Omega _ { [ \mathrm { F D } ] } \pmb { e } _ { \mathrm { E W } } ,
$$

where

$$
\begin{array} { c } { { \Omega _ { \mathrm { [ G e o ] } } = \displaystyle \frac { 1 } { 2 } ( 2 \gamma + 1 ) \frac { m _ { \oplus } ^ { 3 / 2 } } { a ^ { 5 / 2 } } ( 1 - e ^ { 2 } ) ^ { - 1 } } } \\ { { = \displaystyle \frac { 1 } { 3 } ( 2 \gamma + 1 ) 6 6 3 8 \mathrm { m a s ~ \ y r } ^ { - 1 } , } } \end{array}
$$

$$
\begin{array} { l } { { \Omega _ { \mathrm { [ F D ] } } = \displaystyle \frac { 1 } { 1 6 } \left( 4 \gamma + 4 + \alpha _ { 1 } \right) \frac { J _ { \oplus } } { a ^ { 3 } } ( 1 - e ^ { 2 } ) ^ { - 3 / 2 } \sin \psi } } \\ { { \displaystyle ~ = \frac { 1 } { 8 } \left( 4 \gamma + 4 + \alpha _ { 1 } \right) 3 9 . 2 \mathrm { m a s ~ \ y r } ^ { - 1 } , } } \end{array}
$$

where $a$ and $e$ are the semimajor axis and eccentricity of the orbit, and $\psi$ is the angle between the spin axes of the gyroscope and of the Earth. In obtaining the numerical values for GPB, we used the fact that the satellite was in a circular orbit at $6 4 2 ~ \mathrm { k m }$ altitude $( a = 7 0 1 3 \mathrm { k m }$ ). The angular momentum of the Earth is known from combining data from the luni-solar precession of the Earth’s axis and from the multipole moments of the Earth, and is given by $J _ { \oplus } = 0 . 3 3 0 7 m _ { \oplus } R _ { \oplus } ^ { 2 } \omega _ { \oplus }$ , where $R _ { \oplus } = 6 3 7 1 { \mathrm { ~ k m } }$ is the Earth’s mean radius, and $\omega _ { \oplus } = 7 . 2 9 2 1 \times 1 0 ^ { - 5 } \mathrm { s } ^ { - 1 }$ is the Earth’s rotational angular velocity. In a perfect world, the angle $\psi$ would be chosen to be $9 0 ^ { \circ }$ , but in fact it was about $7 3 ^ { \circ }$ . This is because the precessions of the gyroscopes had to be compared with directions in inertial space, as established to high precision, for example, by the distant quasars. To make that comparison, an on-board telescope was oriented toward a “guide” star, and the spin directions were aligned to be parallel to the optical axis of the telescope. This alignment was operationally necessary because the spacecraft itself rotated about that same axis in order to average out numerous environmentally induced torques on the gyros. Many candidate guide stars were considered, but in the end the star IM Pegasi (HR 8703) was selected, in part because it was optically bright and relatively isolated in the sky, and in part because it was bright in the radio, so that its own proper motion relative to the quasars could be measured using VLBI to an accuracy better than the goal for measuring the gyro precessions. IM Peg lies at a distance of $9 6 \ \mathrm { p c }$ , and at a declination of $1 6 . 8 3 ^ { \circ }$ , thus $\psi ~ = ~ 7 3 . 2 ^ { \circ }$ . In fact, VLBI measurements of IM Peg made before, during and after the GPB mission gave a proper motion $3 4 . 3 \pm 0 . 1$ mas $\mathrm { y r } ^ { - 1 }$ , well within the error requirements for GPB (Bartel et al., 2015).

Two additional relativistic geodetic precessions had to be accounted for, one induced by the quadrupole moment of the Earth $( \sim \mathrm { 7 { m a s } \ y r ^ { - 1 } ) }$ , and the other induced by the gyroscopes’ orbital motion around the Sun $( \sim 2 0 \mathrm { m a s ~ \ y r ^ { - 1 } } )$ ). The final results for the GPB experiment are shown in Table 9.1; the GPB saga is told in Box 9.1. The complete technical details of GPB can be found in a special issue of Classical and Quantum Gravity, Vol. 32, 2015.

Another example of relativistic spin precession is in binary pulsars. In this case, the masses of the two bodies are comparable, and using the fact that each mass is given by $m _ { i } = m ( 1 \pm \sqrt { 1 - 4 \eta } ) / 2$ , we can express the two precession rates as

<table><tr><td colspan="3">Table 9.1 Final results of Gravity Probe B.</td></tr><tr><td></td><td>Measured</td><td>Predicted</td></tr><tr><td>Geodetic Precession (mas)</td><td>6602 ± 18</td><td>6606</td></tr><tr><td>Frame-dragging (mas)</td><td>37.2 ± 7.2</td><td>39.2</td></tr></table>

$$
\begin{array} { r l } & { \Omega _ { \mathrm { [ G e o ] } } = 5 . 8 \times 1 0 ^ { - 2 } \mathrm { d e g ~ } \mathrm { y r } ^ { - 1 } \left( \frac { m } { m _ { \odot } } \right) ^ { 2 / 3 } \left( \frac { 1 \mathrm { d a y } } { P _ { \mathrm { b } } } \right) ^ { 5 / 3 } \frac { \alpha } { 1 - e ^ { 2 } } , } \\ & { \Omega _ { \mathrm { [ F D ] } } = 3 . 3 \times 1 0 ^ { - 5 } \mathrm { d e g ~ } \mathrm { y r } ^ { - 1 } \frac { m _ { 2 } } { m } \left( \frac { R _ { 2 } } { 1 0 \mathrm { k m } } \right) ^ { 2 } \left( \frac { 1 \mathrm { d a y } } { P _ { \mathrm { b } } } \right) ^ { 2 } \left( \frac { \nu _ { p } } { 1 \mathrm { m H z } } \right) \frac { \beta } { ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } , } \end{array}
$$

where $\nu _ { p }$ is the spin frequency of the spinning companion, $P _ { \mathrm { { b } } }$ is the orbital period, $\beta = I _ { 2 } / m _ { 2 } R _ { 2 } ^ { 2 }$ is the moment-of-inertia factor, and

$$
\alpha \equiv \frac { 6 } { 7 } \left( 1 + \frac { 2 } { 3 } \eta \pm \sqrt { 1 - 4 \eta } \right) = \left\{ \begin{array} { c c } { { 1 2 / 7 } } & { { : } } & { { m _ { 2 } \gg m _ { 1 } } } \\ { { 1 } } & { { : } } & { { m _ { 2 } = m _ { 1 } } } \\ { { 1 6 \eta / 7 } } & { { : } } & { { m _ { 2 } \ll m _ { 1 } } } \end{array} \right.
$$

For simplicity we have set $\gamma = 1$ and $\alpha _ { 1 } = 0$ .

It is clear that the frame dragging precession is negligible in binary pulsar systems, whereas the geodetic effect could be measurable. Indeed, the first binary pulsar $\mathrm { B } 1 9 1 3 + 1 6$ provided the first evidence of this effect (see Section 12.1 for details about binary pulsars). Observations (Kramer, 1998; Weisberg and Taylor, 2002) indicated that the pulse profile is varying with time, which suggested that the pulsar is undergoing geodetic precession on a 300-year timescale. The amount was consistent with GR, assuming that the pulsar’s spin is suitably misaligned with the orbital angular momentum. Unfortunately, the evidence also suggested that the pulsar beam may precess out of our line of sight by 2025.

A better test was provided by the “double pulsar system,” J0737–3039, discovered in 2003 (see Section 12.1.2). Because the orbit is seen to be almost edge-on, the radio signal from the primary pulsar A is partially eclipsed by the magnetosphere of pulsar B. By monitoring the long-term evolution of the amplitude variations of pulsar A’s signal during eclipses and building a simple model of the magnetosphere of pulsar B, Breton et al. (2008) were able to measure the orientation of both the spin and magnetic axes of pulsar B relative to the orbital plane, as well as the rate of precession of the spin axis. Since both masses are known along with the orbital period and eccentricity (see Table 12.2), we can use Eq. (9.11a) to predict a value $\Omega _ { \mathrm { { [ G e o ] } } } = 5 . 0 7 \mathrm { d e g } \ \mathrm { y r } ^ { - 1 }$ . The value inferred from the model was $4 . 7 \pm 0 . 7 \ : \mathrm { d e g } \ : \ : \mathrm { y r } ^ { - 1 }$ , a $1 3 \%$ test in agreement with general relativity. In fact the precession is so significant that in 2008 the radio beam of pulsar B went out of sight.

# 9.1.3 Tests of spin effects on orbits

In Section 9.1.1, we saw that spin-orbit and spin-spin interactions can induce precessions of orbital planes and of orbital pericenters. In the solar system, the effect of the spin of the Sun on most orbits is too small to be detectable; the best hope might be Mercury, where the additional contribution to the perihelion advance due to the Sun’s spin is $\sim 3 \times 1 0 ^ { - 3 }$ arcseconds per century, of the same order as the current measurement uncertainties.

On the other hand, the effect has been measured using an array of Earth-orbiting satellites, tracked to high precision using laser ranging. For a satellite with negligible mass and spin, $\sigma = 0$ , so the vector $c$ that appears in Eq. (9.7) is given by

$$
{ \pmb { C } } = \frac { 1 } { 2 } \left( 4 \gamma + 4 + \alpha _ { 1 } \right) { \pmb S } _ { \oplus } .
$$

In a reference system in which $S _ { \oplus }$ points in the $z$ -direction, $C _ { \Omega } = 0$ , $\boldsymbol { C } _ { \perp } = \boldsymbol { C } \sin \iota$ and $C _ { \mathrm { h } } = C \cos { \iota } .$ . Thus from Eq. (9.6), the inclination of the orbit relative to the Earth’s spin axis stays unchanged, while the line of nodes and the pericenter advance at the rates

$$
\begin{array} { l } { { \left( \displaystyle \frac { d \Omega } { d t } \right) _ { \mathrm { F D } } = \displaystyle \frac { 1 } { 4 } \left( 4 \gamma + 4 + \alpha _ { 1 } \right) \displaystyle \frac { S _ { \oplus } } { a ^ { 3 } \left( 1 - e ^ { 2 } \right) ^ { 3 / 2 } } } } \\ { { = \displaystyle \frac { 1 } { 8 } \left( 4 \gamma + 4 + \alpha _ { 1 } \right) \left( \displaystyle \frac { R _ { \oplus } } { a } \right) ^ { 3 } \displaystyle \frac { 0 . 2 1 8 } { \left( 1 - e ^ { 2 } \right) ^ { 3 / 2 } } \mathrm { a s ~ \ y r ^ { - 1 } ~ } } } \\ { { \left( \displaystyle \frac { d \omega } { d t } \right) _ { \mathrm { F D } } = - \displaystyle \frac { 1 } { 8 } \left( 4 \gamma + 4 + \alpha _ { 1 } \right) \displaystyle \frac { S _ { \oplus } } { a ^ { 3 } \left( 1 - e ^ { 2 } \right) ^ { 3 / 2 } } \mathrm { c o s } \iota } } \\ { { = - \displaystyle \frac { 1 } { 8 } \left( 4 \gamma + 4 + \alpha _ { 1 } \right) \left( \displaystyle \frac { R _ { \oplus } } { a } \right) ^ { 3 } \displaystyle \frac { 0 . 6 5 5 } { \left( 1 - e ^ { 2 } \right) ^ { 3 / 2 } } \mathrm { a s ~ \ y r ^ { - 1 } ~ } } , } \end{array}
$$

where we use the fact that $\dot { \omega } = \dot { \varpi } - \dot { \Omega } \mathfrak { c }$ cos $\iota$ . Unfortunately, these effects are tiny compared to the effects of the Newtonian multipole moments of the Earth, given by

$$
\begin{array} { r l } & { \left( \frac { d \Omega } { d t } \right) _ { \mathrm { \tiny ~ N } } = - \frac { 3 } { 2 } J _ { 2 } \frac { m _ { \oplus } ^ { 1 / 2 } R _ { \oplus } ^ { 2 } } { a ^ { 7 / 2 } ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } \cos \iota } \\ & { \qquad = - 3 6 4 5 \left( \frac { R _ { \oplus } } { a } \right) ^ { 7 / 2 } \frac { \cos \iota } { ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } \mathrm { d e g ~ \ y r ^ { - 1 } , } } \\ & { \left( \frac { d \omega } { d t } \right) _ { \mathrm { \tiny ~ N } } = 3 J _ { 2 } \frac { m _ { \oplus } ^ { 1 / 2 } R _ { \oplus } ^ { 2 } } { a ^ { 7 / 2 } ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } \left( 1 - \frac { 5 } { 4 } \sin ^ { 2 } \iota \right) } \\ & { \qquad = 7 2 9 1 \left( \frac { R _ { \oplus } } { a } \right) ^ { 7 / 2 } \frac { 1 } { ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } \left( 1 - \frac { 5 } { 4 } \sin ^ { 2 } \iota \right) \mathrm { d e g ~ \ y r ^ { - 1 } , } } \end{array}
$$

where $J _ { 2 }$ is the quadrupole moment coefficient of the Earth, given by $J _ { 2 } = 1 . 0 8 6 4 \times 1 0 ^ { - 3 }$ . Notice that the Newtonian nodal advance rate is proportional to $\scriptstyle \mathrm { c o s } \iota$ , hence it vanishes for a polar orbit; for two orbits with the same orbital elements but with supplementary inclinations $( \iota _ { 2 } = \pi - \iota _ { 1 } )$ ), the nodal advances are equal and opposite. This dependence is true for all the even multipole moments $J _ { 4 } , J _ { 6 }$ and so on. Thus in order to measure the relativistic precession, one has to measure or suppress the Newtonian effect to extremely high accuracy.

Van Patten and Everitt (1976) proposed measuring the frame dragging effect using two satellites in counter-rotating polar orbits. The Newtonian nodal precession would be suppressed, at least up to the effects of the errors $\Delta \iota _ { 1 }$ and $\Delta \iota _ { 2 }$ involved in achieving true polar orbits, and those errors could be measured to sufficient precision by having the satellites track each other as they passed one another over the poles. Ground tracking would measure the nodal precession, and the contribution of the Newtonian precession could be subtracted. This proposal never came to fruition.

The 1976 launch of the “Laser Geodynamics Satellite” (LAGEOS) and of a second LAGEOS in 1992 changed the situation. These satellites are massive spheres, $6 0 ~ \mathrm { c m }$ in diameter and weighing about $4 0 0 ~ \mathrm { k g }$ , placed in nearly circular orbits with semimajor axes approximately equal to $2 R _ { \oplus }$ (the precise orbital elements are listed in Table 9.2). The spheres are covered with laser retroreflectors, similar to those used for lunar laser ranging.

<table><tr><td colspan="5">Table 9.2 Orbital elements of laser-ranged satellites.</td></tr><tr><td> Satellite</td><td>Semimajor axis (km)</td><td>Orbital period (min)</td><td>Eccentricity</td><td>Inclination to equator (°)</td></tr><tr><td>LAGEOS I</td><td>12,257</td><td>225</td><td>0.0045</td><td>109.84</td></tr><tr><td>LAGEOS II</td><td>12,168</td><td>223</td><td>0.0135</td><td>52.64</td></tr><tr><td>LARES</td><td>7,821</td><td>115</td><td>0.0007</td><td>69.5</td></tr></table>

Because of their large mass-to-area ratio, the spheres are less affected by atmospheric drag than other satellites at similar altitudes. This, combined with the high precision of laser ranging (which routinely achieves millimeter-level precision), means that their orbits can be determined extremely precisely. The LAGEOS satellites were launched primarily to carry out studies in geodesy and geodynamics, but it was soon recognized that they were potentially capable of measuring the relativistic nodal advance, which for the values for LAGEOS I shown in Table 9.2 amounts to approximately 30.7 mas/yr.

Indeed, Ciufolini (1986) pointed out that if a second LAGEOS satellite were to have an inclination supplementary to that of LAGEOS I, then the Newtonian advance would be equal and opposite for the two satellites, so that if one measured the nodal advance of both satellites simultaneously and added them together, the large Newtonian effect would cancel out, up to the contributions of errors in achieving the precise orbital inclinations.

Ciufolini and other relativists campaigned vigorously to have LAGEOS II launched with $\iota _ { 2 } = 7 0 . 1 6 ^ { \circ }$ , but other considerations prevailed in the end. LAGEOS II was launched with $\iota _ { 2 } = 5 2 . 6 4 ^ { \circ }$ , mainly to optimize coverage by the world’s network of laser tracking stations, which was important for geophysics and geodynamics research. The fall-back option was then to combine the data from the two satellites as they were. One could still eliminate the largest Newtonian contribution coming from $J _ { 2 }$ with a suitable linear combination of the two measured nodal advances, thereby revealing the relativistic contribution and those coming from higher-order multipole moments. The uncertainties in the values of those moments would contribute to the error made in measuring the relativistic effect. For a time, Ciufolini and collaborators tried to include a third piece of data, the perigee advance of LAGEOS II (which has a small eccentricity), as a way to also eliminate $J _ { 4 }$ , but this turned out to be plagued with systematic errors that were large and hard to control (Ciufolini et al., 1997, 1998; Ciufolini, 2000).

The turning point came with CHAMP and GRACE. Europe’s CHAMP (Challenging Minisatellite Payload) and NASA’s GRACE (Gravity Recovery and Climate Experiment) missions, launched in 2000 and 2002, respectively, use precision tracking of spacecraft to measure variations in the Earth’s gravity on scales as small as several hundred kilometers, with unprecedented accuracies. GRACE consists of a pair of satellites flying in close formation (200 kilometers apart) on polar orbits. Each satellite carries an on-board accelerometer to measure nongravitational perturbations, a satellite to satellite K-band radar link to measure variations in the Earth’s gravity gradient on short scales, and a GPS tracking unit to measure larger scale variations. With the dramatic improvements on $J _ { \ell }$ obtained by CHAMP and GRACE, Ciufolini and his colleagues could now treat $J _ { 4 }$ and higher multipole moments as known, and use the two LAGEOS nodal advances to determine $J _ { 2 }$ and the relativistic contribution. The final outcome was a successful test of the relativistic prediction at the level of 10 percent (Ciufolini et al., 2011).

On February 13, 2012, a third laser-ranged satellite, known as LARES (Laser Relativity Satellite) was launched by the Italian Space Agency. Its inclination was $6 9 . 5 ^ { \circ }$ , very close to the required supplementary angle relative to LAGEOS I, and its eccentricity was very nearly zero (see Table 9.2). However, the launch failed to achieve the same semimajor axis as that of the two LAGEOS satellites, again preventing a perfect cancellation of the Newtonian effect. Nevertheless, combining data from all three satellites with continually improving Earth data from GRACE, the LARES team reported a test of frame-dragging at the 5 percent level (Ciufolini et al., 2016).

# 9.2 De Sitter Precession

This effect, an advance of the line of nodes of the Earth–Moon orbit, was first calculated by de Sitter (1916) as a consequence of the post-Newtonian perturbations of the lunar orbit induced by the gravitational potential of the Sun and by the orbital motion of the Earth– Moon system around the Sun (for details of the derivation in general relativity in modern language, see section 10.1.6 of PW). However, it can equally well be regarded as a geodetic precession of the Earth–Moon system’s angular momentum vector (its “spin”) about the angular momentum vector of the Earth-Sun orbit. From the geodetic term in Eq. (9.3), the change in $\pmb { S } _ { \mathrm { E M } }$ , the Earth–Moon’s spin, over one orbit around the Sun is given by

$$
\Delta S _ { \mathrm { E M } } = \pi ( 2 \gamma + 1 ) \frac { m _ { \odot } } { p } \hat { \pmb { h } } \times { \pmb { S } } _ { \mathrm { E M } } ,
$$

where we have approximated $m _ { 1 } = m _ { \oplus } + m _ { \ ? } \ll m$ , and $m _ { 2 } = m _ { \odot } \simeq m$ . This precession leads directly to an advance of the lunar node, given by

$$
\frac { d \Omega } { d t } = \frac { 1 } { 2 } ( 2 \gamma + 1 ) \frac { m _ { \odot } ^ { 3 / 2 } } { a ^ { 5 / 2 } } \frac { 1 } { 1 - e ^ { 2 } } = 1 . 9 1 7 \mathrm { a s / c e n t u r y } ,
$$

where $a$ and $e$ are the semimajor axis and eccentricity of the Earth–Moon barycenter orbit around the Sun. This effect has been measured to about 0.6 percent using lunar laser ranging data (Dickey et al., 1994; Williams et al., 2004a, 2004b).

# 9.3 Tests of Post-Newtonian Conservation Laws

Here we discuss tests of the “conservation law” PPN parameters $\zeta _ { 1 }$ , $\zeta _ { 2 }$ , $\zeta _ { 3 }$ , $\zeta _ { 4 }$ , and $\alpha _ { 3 }$ . We have already seen in Section 8.4 that, by virtue of its additional role as a preferred-frame parameter, $\alpha _ { 3 }$ has been constrained to vanish to a few parts in $1 0 ^ { 2 0 }$ using data from widebinary millisecond pulsars.

In addition, there is strong theoretical evidence that $\zeta _ { 4 }$ , which is related to the gravity generated by fluid pressure, is not really an independent parameter. In any reasonable theory of gravity there should be a connection between the gravity produced by kinetic energy $( \rho \nu ^ { 2 } )$ , internal energy $( \rho \Pi )$ , and pressure $( p )$ . The idea is to consider an alternative PPN metric generated by a system of charged point masses, with gravitational potentials generated by masses, microscopic velocities, charges, and so on. Under suitable coarse graining as used in thermodynamics, this metric should transform smoothly to the hydrodynamic PPN metric. From such considerations, there follows (Will, 1976b) the additional theoretical constraint

$$
6 \zeta _ { 4 } = 3 \alpha _ { 3 } + 2 \zeta _ { 1 } - 3 \zeta _ { 3 } .
$$

In addition the ratio of active to passive mass for such a bound system of point charges should take the form

$$
\frac { m _ { \mathrm { A } } } { m _ { \mathrm { P } } } = 1 + \frac { 1 } { 2 } \zeta _ { 3 } \frac { E _ { e } } { m _ { \mathrm { P } } } ,
$$

where $E _ { e }$ is the electrostatic energy of the system of point charges.

A nonzero value for $\zeta _ { 3 }$ would result in a violation of conservation of momentum, or of Newton’s third law in gravitating systems, based on differences in chemical composition.

A classic test of Newton’s third law for gravitating systems was carried out by Kreuzer (1968), in which the gravitational attraction of fluorine and bromine were compared. Kreuzer’s experiment used a Cavendish balance to compare the Newtonian gravitational force generated by a cylinder of Teflon (76 percent fluorine by weight) with the force generated by that amount of a liquid mixture of trichloroethylene and dibromomethane (74 percent bromine by weight) that had the same passive gravitational mass as the cylinder, namely the amount of liquid displaced by the cylinder at neutral buoyancy. In the actual experiment, the Teflon cylinder was moved back and forth in a container of the liquid, with the Cavendish balance placed near the container. Had the active masses of Teflon and displaced liquid differed at neutral buoyancy, a periodic torque would have been experienced by the balance. The absence of such a torque led to the conclusion that the ratios of active to passive mass for fluorine and bromine are the same to 5 parts in $1 0 ^ { 5 }$ . Using the semi-empirical mass formula for nuclear electrostatic energies (which are the dominant contribution in this case), $E _ { e } / m \simeq 7 . 6 \times 1 0 ^ { - 4 } Z ( Z - 1 ) A ^ { - 4 / 3 }$ , where $Z$ and $A$ are the atomic number and mass number, respectively, we obtain the bound $\left| \zeta _ { 3 } \right| < 0 . 0 6$ .

An improved bound was reported by Bartlett and van Buren (1986). They noted that current understanding of the structure of the Moon involves an iron-rich, aluminum-poor mantle whose center of mass is offset about $1 0 \mathrm { k m }$ from the center of mass of an aluminumrich, iron-poor crust. The direction of offset is toward the Earth, about $1 4 ^ { \circ }$ to the east of the Earth–Moon line. Such a model accounts for the basaltic maria that face the Earth, and the aluminum-rich highlands on the Moon’s far side, and for a $2 ~ \mathrm { k m }$ offset between the observed center of mass and center of figure for the Moon. Because of this asymmetry, a violation of Newton’s third law for aluminum and iron would result in a momentum nonconserving self-force on the Moon, whose component along the orbital direction would contribute to the secular acceleration of the lunar orbit. Improved knowledge of the lunar orbit through lunar laser ranging, and a better understanding of tidal effects in the Earth–Moon system (which also contribute to the secular acceleration) through satellite data, severely limit any anomalous secular acceleration, with the resulting limit of $4 \times 1 0 ^ { - 1 2 }$ on the difference between the active-to-passive mass ratios for aluminum and iron. This leads to the bound $\left| \zeta _ { 3 } \right| < 1 0 ^ { - 8 }$ . Nordtvedt (2001) examined whether this bound could be improved by considering the asymmetric distribution of ocean water on Earth; the self-acceleration of the Earth in the polar direction would then lead to an effect in the Earth–Moon orbit that could be tested by lunar laser ranging.

Another test of PPN conservation laws involves an effect first pointed out, incorrectly, by Levi-Civita (1937). The effect is the secular acceleration of the center of mass of a binary system. Levi-Civita pointed out that general relativity predicted a secular acceleration in the direction of the periastron of the orbit, and found a binary system candidate in which he felt the effect might one day be observable. Eddington and Clark (1938) repeated the calculation using the $N .$ -body equations of motion of de Sitter (1916). After first finding a secular acceleration of opposite sign to that of Levi-Civita, they then discovered an error in de Sitter’s equations of motion, and concluded finally that the secular acceleration was zero. Robertson (1938) independently reached the same conclusion using the Einstein-Infeld-Hoffmann equations of motion, and Levi-Civita later verified that result.

In fact, the center-of-mass acceleration does exist, but only in nonconservative theories of gravity (Will, 1976a). The simplest way to derive this result is to treat the two-body system as a single composite “body” in otherwise empty space, and to focus on the self acceleration terms in the equation of motion (6.46a). Setting $\alpha _ { 3 } = 0$ , dropping the fluid terms $\mathcal { E } ^ { j }$ and $\mathcal { P } ^ { j }$ , specializing the remaining terms to two bodies and then averaging over one orbit, we obtain

$$
{ \pmb a } _ { \mathrm { C M } } = - \frac { 1 } { 2 } \zeta _ { 2 } \frac { m ^ { 2 } } { a ^ { 3 } } \eta \Delta \frac { e } { ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } { \pmb e } _ { \mathrm { P } } ,
$$

where $e _ { \mathrm { P } }$ is a unit vector in the direction of the pericenter of body 1, $\eta = m _ { 1 } m _ { 2 } / ( m _ { 1 } + m _ { 2 } ) ^ { 2 }$ and $\Delta = ( m _ { 2 } - m _ { 1 } ) / ( m _ { 1 } + m _ { 2 } )$ . A consequence of this acceleration would be non-vanishing values for $d ^ { 2 } P / d t ^ { 2 }$ , where $P$ denotes the period of any intrinsic process in the system (orbital period, spectral frequencies, pulsar periods). The observed upper limit on $d ^ { 2 } P _ { \mathrm { p } } / d t ^ { 2 }$ of the binary pulsar $\mathrm { B } 1 9 1 3 + 1 6$ places a strong constraint on such an effect, resulting in the bound $\left| \zeta _ { 2 } \right| < 4 \times 1 0 ^ { - 5 }$ (Will, 1992b).

No feasible experiment or observation has ever been proposed that would set a direct limit on the PPN parameters $\zeta _ { 1 }$ or $\zeta _ { 4 }$ . Note, however, that these parameters do appear in combination with other PPN parameters in observable effects, for example, $\zeta _ { 1 }$ in the Nordtvedt effect (see Section 8.1).

The landscape for testing gravitational theory underwent a dramatic upheaval in September 1974, with the discovery by Hulse and Taylor of the Binary Pulsar (see Section 12.1 for an account of the discovery). Until then, all tests of relativistic gravitation were carried out under conditions of weak gravitational fields and slow motions, and were well described by the PPN framework of Chapter 4. Tests involving the orbits of bodies, such as those of Mercury and other planets around the Sun, could be safely studied by treating the planets as test bodies and calculating their geodesic motion; the notable exception to this was the Nordtvedt effect in lunar motion. And no tests prior to 1974 even remotely involved gravitational radiation.

The discovery of the binary pulsar $\mathrm { B } 1 9 1 3 + 1 6$ changed all that. Here was a system consisting of a neutron star and a compact companion star of almost equal mass; each star moves in a curved spacetime generated both by the companion star and by itself, and both stars are moving at substantial speeds. Neutron stars are not weak-field objects; the selfgravitational binding energy of a neutron star can be as much as 20 percent of its rest mass. Thus the PPN framework no longer applies, or at least must be applied with great caution. And within a few weeks of the announcement of the discovery, it was realized that, with orbital velocities of order $2 0 0  { \mathrm { k m } } \ \mathrm { s } ^ { - 1 }$ , the system was so relativistic that the dissipative effects on its orbit resulting from the emission of gravitational radiation might eventually be detectable. And indeed, by 1979, the inspiral of the orbit had been measured in an amount that agreed with the prediction of general relativity, providing the first evidence of the existence of gravitational radiation.

In this chapter and the two chapters that follow, we will focus on this new landscape for testing relativistic gravity. This chapter will deal with the structure and motion of bodies with strong internal gravity, such as neutron stars and black holes; “compact body” has become the standard term for such astronomical objects. This is known as the “strongfield” regime of gravity since the spacetime geometry inside and near such objects is characterized by $m / r \sim 1$ , as compared with $1 0 ^ { - 6 }$ near the solar surface. Chapter 11 will treat gravitational radiation in general relativity and alternative theories of gravity. This is frequently termed the “dynamical” regime of gravity, where motions are sufficiently rapid that the gravitational waves generated can be significant, both for direct detection, and for the back-reaction on the evolution of the system. Using the basic frameworks developed in these two chapters, we will describe in Chapter 12 specific strong-field and dynamical tests of relativistic gravity, including tests involving binary pulsars, tests using gravitational waves from inspiralling binaries of compact bodies, such as the waves detected by the LIGO/Virgo observatories beginning in 2015, and tests involving orbits of stars and matter outside black holes.

We will begin by discussing the structure of neutron stars and black holes in general relativity and in a range of alternative theories in Sections 10.1 and 10.2, and then will turn to their motion in Section 10.3.

# 10.1 Structure of Neutron Stars

Neutron stars were first suggested as theoretical possibilities in the 1930s (Baade and Zwicky, 1934). They are highly condensed stars where gravitational forces are sufficiently strong to crush atomic electrons together with the nuclear protons to form neutrons, to raise the density of matter above nuclear density $( \rho \geq 3 \times 1 0 ^ { 1 4 } \mathrm { ~ g ~ c m } ^ { - 3 } )$ , and to cause the neutrons to be quantum-mechanically degenerate. At such high densities, exotic phenomena can occur, including superfluidity, strange quark matter, and quark-gluon plasmas. A typical neutron-star model has a mass between 0.7 and $2 . 5 M _ { \odot }$ , and a radius of order $1 0 \mathrm { k m }$ . However, they remained just theoretical possibilities until the discovery of pulsars in 1967 (Hewish et al., 1968) and their subsequent interpretation as rotating neutron stars. There followed significant progress in calculating the structure of neutron stars using different nuclear equations of state, in obtaining firm estimates for the maximum mass of neutron stars, and in developing robust methods for modelling rapidly rotating neutron stars.

Today, with over 2300 pulsars known (Lorimer and Kramer, 2012), neutron stars are fully accepted as members of the astronomical zoo, and indeed comprise a number of different classes. There is the class of mostly isolated pulsars of periods between 0.1 and $1 0 ~ \mathrm { s } .$ , representing the bulk of the population. The class of “recycled” pulsars with periods between one and 100 milliseconds, found mostly in binary systems, includes objects whose spin periods are so stable that they rival the best Earth-bound atomic clocks, yielding methods both for testing general relativity and for detecting gravitational waves. The class of accreting, X-ray emitting neutron stars has provided laboratories for studing the behavior of matter and magnetic fields under extreme conditions. The statistics of neutron stars also provide constraints on models of supernovae and on the evolution of binary systems containing massive stellar progenitors. Pulsars are regarded as important laboratories for testing theories of the equation of state of matter at ultrahigh densities. They could also be useful for testing alternative theories of gravity, and this section is devoted to discussing the structure of these objects in a range of theories.

In Newtonian gravitation theory, the equations of stellar structure for a static, spherically symmetric star composed of matter at zero temperature are given by

$$
\begin{array} { c } { { \displaystyle \frac { d p } { d r } = \rho \frac { d U } { d r } , \quad \mathrm { [ H y d r o s t a t i c ~ e q u i l i b r i u m ] } , } } \\ { { p = p ( \rho ) , \qquad \mathrm { [ E q u a t i o n ~ o f ~ s t a t e ] } , } } \\ { { \displaystyle \frac { d } { d r } \left( r ^ { 2 } \frac { d U } { d r } \right) = - 4 \pi r ^ { 2 } \rho , \quad \mathrm { [ F i e l d ~ e q u a t i o n ] } , } } \end{array}
$$

where $p ( r )$ is the pressure, $\rho ( r )$ is the density and $U ( r )$ is the Newtonian gravitational potential. Note that $T = 0$ (more precisely, $T \ll$ the Fermi temperature of the degenerate matter in the star) is an adequate approximation for neutron-star matter for all but newly formed hot neutron stars; this results in the simple equation of state $p ( \rho )$ .

In any metric theory of gravity, it is simple to write down the equations corresponding to the first two of these three equations because they follow from the Einstein Equivalence Principle (Chapter 2), which states that in local freely falling frames the nongravitational laws of physics are those of special relativity, $T ^ { \mu \nu } { } _ { , \nu } = 0 , p = p ( \rho )$ . Thus, we have in any basis,

$$
T ^ { \mu \nu } { } _ { ; \nu } = 0 , \quad p = p ( \rho ) .
$$

For a perfect fluid, $T ^ { \mu \nu } = ( \rho + p ) u ^ { \mu } u ^ { \nu } + p g ^ { \mu \nu }$ , where we have lumped the internal energy $\rho \Pi$ into $\rho$ (compare Eq. (3.77)).

It is useful to rewrite these equations in a form that parallels the first two parts of Eq. (10.1). For a static, spherically symmetric spacetime, there exists a coordinate system in which the metric has the form

$$
d s ^ { 2 } = - e ^ { 2 \Phi ( r ) } d t ^ { 2 } + e ^ { 2 \Lambda ( r ) } d r ^ { 2 } + e ^ { 2 \mu ( r ) } r ^ { 2 } d \Omega ^ { 2 } ,
$$

where $d \Omega ^ { 2 } = d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 }$ is the element of the two-sphere. For theories of gravity with a preferred frame, established by an auxiliary vector or tensor field, for example, the assumption of spherical symmetry is only valid for stars at rest with respect to the preferred frame. There exists the freedom to change the coordinate $r$ by $r ~ = ~ g ( \tilde { r } )$ . If the radial coordinate is chosen so that $\mu ( r ) = 0$ , the coordinates are called “curvature coordinates.” In such coordinates, $2 \pi r$ measures the proper circumference of circles of constant $r$ . In general relativity, they are known as Schwarzschild coordinates. If the radial coordinate is chosen so that $\mu ( r ) = \Lambda ( r )$ , the coordinates are called “isotropic coordinates.”

Now, for hydrostatic equilibrium, the equations of motion $T ^ { \mu \nu } { } _ { ; \nu } = 0$ may be written in the form

$$
p _ { { , j } } = - ( \rho + p ) u ^ { \nu } u _ { { j } ; \nu } ,
$$

where $j$ runs over $r , \ \theta$ , and $\phi$ . For spherical symmetry only the $j ~ = ~ r$ component is nontrivial, and using the fact that $\pmb { u } = ( e ^ { - \Phi ( r ) } , 0 , 0 , 0 )$ , we obtain

$$
\frac { d p } { d r } = - ( \rho + p ) \frac { d \Phi } { d r } , \qquad p = p ( \rho ) .
$$

Notice that in the Newtonian limit, $p \ll \rho$ , $\Phi \simeq - U$ and we recover the first two of Eqs. (10.1). Eq. (10.5) are valid independently of the theory of gravity, assuming static spherical symmetry. The field equations for $\Phi , \Lambda$ , and $\mu$ , along with field equations for any auxiliary fields, will depend upon the theory.

In constructing a stellar model, boundary conditions must be imposed. One set imposes a continuity condition for the matter, and defines the stellar surface at radius $R$ :

$$
\left. \frac { d p } { d r } \right| _ { r = 0 } = 0 , \qquad p ( R ) = 0 .
$$

Assuming that the spacetime far from the neutron star can be approximated as asymptotically flat, the metric functions are constrained to behave as $r  \infty$ according to [see Eq. (5.6)]

$$
\begin{array} { l } { { e ^ { 2 \Phi ( r ) } \to c _ { 0 } - 2 c _ { 0 } c _ { 1 } \displaystyle \frac { m } { r } , } } \\ { { e ^ { 2 \Lambda ( r ) } \to c _ { 1 } , } } \\ { { e ^ { 2 \mu ( r ) } \to c _ { 1 } . } } \end{array}
$$

These conditions guarantee that after transforming to asymptotically Lorentz coordinates, and converting to geometrized units ( $G _ { \mathrm { t o d a y } } = 1 $ ), the metric will have the form

$$
g _ { 0 0 }  - 1 + \frac { 2 m } { r } , \quad g _ { 0 j }  0 , \quad g _ { j k }  \delta _ { j k } ,
$$

and thus that the Kepler-measured mass of the star will be $m$ . The asymptotic boundary conditions on the auxiliary fields of the theory are assumed to take the form, as $r  \infty$ , and in the preferred rest frame (if any):

$$
\begin{array} { r c l } { { } } & { { } } & { { \phi ( r )  \phi _ { 0 } , } } \\ { { } } & { { } } & { { K ^ { \mu } ( r )  ( K , 0 , 0 , 0 ) , } } \\ { { } } & { { } } & { { B ^ { \mu \nu } ( r )  \mathrm { d i a g } ( b _ { 0 } , b _ { 1 } , b _ { 2 } r ^ { 2 } , b _ { 2 } r ^ { 2 } \sin ^ { 2 } \theta ) . } } \end{array}
$$

These boundary values $\phi _ { 0 } , K , b _ { i }$ could depend on time through cosmological evolution, or they could depend on the presence of nearby matter, such as a companion star in a binary system. The presence of nearby matter could affect the internal structure of the neutron star because of violations of the strong equivalence principle (see Section 3.3 for discussion). If the timescale over which these parameters change is long compared to the internal dynamical timescale of the neutron star, one can still approximate the star’s structure as quasistatic, with its structure evolving adiabatically as the external parameters vary. If the timescales are comparable, such as near the end of an inspiral of two compact bodies, then one must resort to a fully dynamical calculation.

Another problem that must be confronted in building neutron star models in alternative theories of gravity is that real neutron stars are in motion because of the motion of the host galaxy relative to the cosmic background radiation, and in some cases because of orbital motion around a companion. This means that in theories of gravity with auxiliary vector or tensor fields, one cannot automatically assume spherical symmetry, since these fields will single out a preferred direction in space from the point of view of the neutron star’s rest frame. Depending on the theory, it may be possible to treat these nonspherical effects as small perturbations of an underlying spherical model.

For a range of nuclear equations of state, one then can determine such important quantities as the mass-radius relation, the maximum mass, the surface gravitational redshift, the innermost stable circular orbit, and, for rotating neutron stars, the moment of inertia, the quadrupole moment and the Love numbers. These astrophysically relevant parameters could then be compared with available data in order to place constraints on the alternative theory (as well as on the equation of state).

Another important set of parameters, known as “sensitivities,” encodes the degree to which such quantities as the mass, radius and moment of inertia vary when the parameters $\phi _ { 0 } , K ,$ , and $b _ { i }$ vary. These quantities will play an important role in the equations of motion for compact bodies in alternative theories of gravity (see Section 10.3).

Unfortunately, this exhausts the generic features of the equations of relativistic stellar structure, so we must now turn to specific theories. Here we describe neutron stars in only a sampling of theories of gravity. Berti et al. (2015) give a more thorough review, covering a wide range of alternative theories.

# General relativity

In curvature coordinates $\mathbf { \bar { \rho } } _ { \mu } ( r ) \equiv 0$ ), and in units where $G = 1$ , the field equations (5.13) take the form

$$
\begin{array} { c } { { \displaystyle \frac { d } { d r } \left[ r ( 1 - e ^ { - 2 \Lambda } \right] = 8 \pi r ^ { 2 } \rho , } } \\ { { \displaystyle \frac { d \Phi } { d r } = \frac { m ( r ) + 4 \pi r ^ { 3 } p } { r ( r - 2 m ( r ) ) } . } } \end{array}
$$

The first equation has the solution

$$
e ^ { 2 \Lambda } = \left( 1 - \frac { 2 m ( r ) } { r } \right) ^ { - 1 } ,
$$

where

$$
m ( r ) = 4 \pi \int _ { 0 } ^ { r } r ^ { \prime 2 } \rho ( r ^ { \prime } ) d r ^ { \prime } .
$$

These equations, together with Eq. (10.5) and the boundary conditions (10.7) (with $c _ { 0 } = c _ { 1 } = 1$ ), are sufficient to calculate neutron-star models. Called the TOV (Tolman, Oppenheimer, Volkoff) equations for hydrostatic equilibrium, they are the standard tool for the study of nonrotating neutron stars within general relativity. For reviews, including models of rotating neutron stars, see Arnett and Bowers (1977), Baym and Pethick (1979), Salgado et al. (1994), Cook et al. (1994), Stergioulas (2003) and Lattimer and Prakash (2007). The maximum masses of neutron star models range from around $1 . 4 M _ { \odot }$ for soft equations of state to $2 . 7 M _ { \odot }$ for stiff equations of state. The discovery of pulsars with masses in excess of $2 M _ { \odot }$ , coupled with the assumption that general relativity is correct, has made it possible to rule out a number of soft equations of state.

# Scalar-tensor theories

Using curvature coordinates $\mathbf { \boldsymbol { \mu } } ( r ) \equiv 0$ ), and defining

$$
e ^ { 2 \Lambda } \equiv \left[ 1 - { \frac { 2 m ( r ) } { r } } \right] ^ { - 1 } ,
$$

we can put the field equations (5.35) for scalar-tensor theories into the form

$$
\begin{array} { l } { \displaystyle \frac { d m } { d r } = \frac { 4 \pi G r ^ { 2 } } { \phi } \left[ \rho - \frac { \rho - 3 p } { 3 + 2 \omega } - \frac { 1 } { 8 \pi G } \left( 1 - \frac { 2 m } { r } \right) \left\{ \Phi _ { , r } \phi _ { , r } - \frac { \phi _ { , r } ^ { 2 } } { 2 \phi } \left( \omega - \frac { 2 \omega ^ { \prime } \phi } { 3 + 2 \omega } \right) \right\} \right] , } \\ { \displaystyle \frac { d \Phi } { d r } = \frac { 1 } { \left( 1 + r \phi _ { , r } / 2 \phi \right) } \left[ \frac { m + 4 \pi G r ^ { 3 } p / \phi } { r \left( r - 2 m \right) } + \frac { \omega r \phi _ { , r } ^ { 2 } } { 4 \phi ^ { 2 } } - \frac { \phi _ { , r } } { \phi } \right] , } \\ { \displaystyle \frac { d } { d r } \left( r ^ { 2 } e ^ { \Phi - \mathrm { A } } \frac { d \phi } { d r } \right) = - \frac { r ^ { 2 } e ^ { \Phi - \mathrm { A } } } { 3 + 2 \omega } \left[ \frac { 8 \pi G r \left( \rho - 3 p \right) } { r - 2 m } + \omega ^ { \prime } \phi _ { , r } ^ { 2 } \right] , } \end{array}
$$

where $G$ is the gravitational coupling constant, and $\omega ^ { \prime } \equiv d \omega / d \phi$ . The present value of $G$ is related to the asymptotic value of $\phi$ by (see Eq. (5.54)) by

$$
G _ { \mathrm { t o d a y } } \equiv \frac { G } { \phi _ { 0 } } \left( \frac { 4 + 2 \omega ( \phi _ { 0 } ) } { 3 + 2 \omega ( \phi _ { 0 } ) } \right) = 1 .
$$

For the special case of Brans-Dicke theory ( $\omega =$ constant), neutron star models differ only slightly from those of general relativity for almost all values of $\omega > 0$ (Salmona, 1967; Hillebrandt and Heintzmann, 1974). For general scalar-tensor theories with $\omega ^ { \prime }$ positive and with relatively large values of $\omega _ { 0 }$ , the differences are typically of order $1 / \omega _ { 0 }$ (Zaglauer, 1992). However, within a class of scalar-tensor theories for which $A ( \varphi ) = e ^ { \beta _ { 0 } \varphi ^ { 2 } / 2 }$ [see Eq. (5.38)], and for negative values $\beta _ { 0 } = 2 \omega _ { 0 } ^ { \prime } \phi _ { 0 } / ( 3 + 2 \omega _ { 0 } ) ^ { 2 } < - 4 . 8 5$ , a phenomenon known as “spontaneous scalarization” can occur, whereby nonlinear interactions between gravity and the scalar field can lead to large deviations of the scalar field inside the star from its values outside, resulting in dramatically different neutron-star structure (Damour and Esposito-Farese, 1993, 1996, 1998). For a semi-analytic analysis of neutron-star structure \` in scalar-tensor theories, along with an extensive bibliography, see Horbatsch and Burgess (2011).

Neutron star models have also been studied in various versions of $f ( R )$ and chameleon scalar-tensor theories (Kobayashi and Maeda, 2008; Upadhye and Hu, 2009; Babichev and Langlois, 2009, 2010; Cooney et al., 2010; Jaime et al., 2011).

# Vector-Tensor Theories

Neutron-star models in Einstein-Æther theory were studied by Eling et al. (2007), extending earlier work by Eling and Jacobson (2006). The star was assumed to be isolated in an asymptotically flat spacetime and at rest relative to the preferred frame induced by the vector field. They first imposed the constraints of Eq. (5.65), so that $\alpha _ { 1 } = \alpha _ { 2 } = 0$ . They restricted the parameters further by requiring that propagating modes of gravitational waves be stable, carry positive energy and have speeds $\geq 1$ . They assumed that the vector field had only a time component ${ { K } _ { r } } = 0$ ). This is not strictly required by the assumption of a static system, so it may be overly restrictive. Since the vector field in Einstein-Æther theory has unit norm, this implies that $K ^ { 0 } ( r ) = e ^ { - \Phi ( r ) }$ . In static spherical symmetry with $K _ { r }$ forced to vanish, it turns out that the constants $c _ { 2 }$ and $c _ { 3 }$ play no role, and that the only relevant parameter is $c _ { 4 }$ , or equivalently the combination $c _ { 1 4 }$ . Recall from Chapter 5 that $0 < c _ { 1 4 } < 2$ . Eling et al. (2007) found, for example that the maximum mass was in general a monotonically decreasing function of $c _ { 1 4 }$ , ranging from about $2 . 4 M _ { \odot }$ for $c _ { 1 4 } ~ = ~ 0$ to about $1 . 8 M _ { \odot }$ for $c _ { 1 4 } = 1 . 9$ for a stiff hadronic equation of state, and from $2 . 2 M _ { \odot }$ to about $1 . 7 M _ { \odot }$ for a medium hadronic equation of state. For any MIT bag model equation of state with strange quarks, and for a soft hadronic equation of state, the maximum mass was less than $2 M _ { \odot }$ for all values of $c _ { 1 4 }$ . The observation of neutron stars with masses $\geq 2 M _ { \odot }$ thus constrains both the equation of state and the parameter $c _ { 1 4 }$ . Yagi et al. (2014a) extended this to a broad range of equations of state compatible with $2 M _ { \odot }$ neutron stars, and also studied models in Khronometric theory.

# Tensor-Vector-Scalar Theories

Neutron stars in TeVeS were first studied by Lasky et al. (2008). While that analysis used the original flawed version of TeVes (Skordis, 2008), Lasky (2009) showed that, for static spherical symmetry, with the constraint $K _ { r } = 0$ , the equations used are equivalent to those obtained from the improved TeVeS theory, as described in Section 5.5. The models depend on the asymptotic value $\phi _ { 0 }$ of the scalar field $0 \leq \phi _ { 0 } \ll 1$ ), on the vector coupling constant $c _ { 1 4 }$ , and on the scalar coupling constant $k \sim 0 . 0 3$ . They used a polytropic equation of state with $\Gamma = 2 . 4 6$ , which leads to a maximum mass in general relativity of only $1 . 6 5 M _ { \odot }$ (this was before the discovery of a $2 M _ { \odot }$ neutron star). As in Einstein-Æther theory, the maximum mass was found to be a decreasing function of $c _ { 1 4 }$ , holding $k$ and $\phi _ { 0 }$ fixed. For $c _ { 1 4 } = 0 . 5$ and $\phi _ { 0 } = 0 . 0 0 3$ , the maximum mass decreased slightly with increasing $k .$ . In the limit of small values of the three parameters $c _ { 1 4 }$ , $k$ and $\phi _ { 0 }$ , the models approached their general relativistic counterparts.

# Quadratic gravity theories

Pani et al. (2011) studied neutron star models in a class of quadratic theories described by the action

$$
\begin{array} { r c l } { { } } & { { } } & { { I = \displaystyle \int \Biggl [ f _ { 0 } ( | \phi | ) R + f _ { 1 } ( | \phi | ) R _ { \mathrm { G B } } ^ { 2 } + f _ { 4 } ( | \phi | ) ^ { * } R R } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - \gamma ( | \phi | ) g ^ { \mu \nu } \partial _ { \mu } \phi ^ { * } \partial _ { \nu } \phi - V ( \phi ) \Biggr ] ( - g ) ^ { 1 / 2 } d ^ { 4 } x } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + I _ { \mathrm { N G } } ( q _ { A } , A ^ { 2 } ( | \phi | ) g _ { \mu \nu } ) , } } \end{array}
$$

where $R _ { \mathrm { G B } } ^ { 2 }$ is the Gauss-Bonnet invariant, given by

$$
R _ { \mathrm { G B } } ^ { 2 } = R ^ { 2 } - 4 R _ { \alpha \beta } R ^ { \alpha \beta } + R _ { \alpha \beta \gamma \delta } R ^ { \alpha \beta \gamma \delta } ,
$$

and $\phi$ is potentially a complex scalar field. The use of $R _ { \mathrm { G B } } ^ { 2 }$ in the action (10.16) guarantees that the field equations contain no more than two derivatives of the metric (compare with Eq. (5.77)). They then specialized to Einstein-Dilaton-Gauss-Bonnet gravity, with $\phi$ real, $f _ { 0 } = ( 1 6 \pi G ) ^ { - 1 }$ , and $V ( \phi ) = 0$ . In spherical symmetry, the Chern-Simons term $^ { * } R R$ makes no contribution, $\mathrm { s o } f _ { 4 }$ can be set equal to zero. Finally, they used a parametrization $f _ { 1 } ( \phi ) =$ $( \alpha / 1 6 \pi ) e ^ { \beta \phi }$ where $\alpha$ and $\beta$ are constants, with $\alpha$ having dimensions of (length)2. They chose boundary conditions in which the metric was asymptotically flat, and in which $\phi  0$ as $r \to \infty$ . They found that $\phi \ll 1$ throughout the neutron star, and that the maximum mass was a decreasing function of the product $\alpha \beta$ . For a reasonably stiff equation of state, the maximum mass ranged from $2 . 4 M _ { \odot }$ for small values of $\alpha \beta$ , corresponding to the general relativistic limit, to $0 . 6 M _ { \odot }$ for $\alpha \beta ~ = ~ 1 0 0 M _ { \odot } ^ { 2 }$ . Recall that the “natural” scale for $\alpha$ is $M _ { \mathrm { P l a n c k } } ^ { 2 } = 1 0 ^ { - 7 6 } M _ { \odot } ^ { 2 }$ .

While spherical neutron stars are not affected by the Chern-Simons term, rotating neutron stars are. Slowly rotating neutron star models in dynamical Chern-Simons theory were constructed by Yunes et al. (2010), Ali-Ha¨ımoud and Chen (2011), and Yagi et al. (2013). Unfortunately, modifications to the maximum mass were found to be degenerate with the equation of state. The stars develop a “dipole scalar charge” that can affect orbital motions in binary pulsars, but the effects were found to be too small to provide meaningful constraints on the theory (Yagi et al., 2013).

# 10.2 Structure of Black Holes

In a certain sense, black hole theory has a longer history than neutron-star theory, as it dates back to a suggestion by the Reverend John Michell (1784) that, according to Newtonian gravity, objects might exist in which the escape velocity from the surface could exceed the speed of light. Laplace made the same suggestion independently in 1796 (Laplace, 1808, 1799). Remarkably, Michell went on argue that such a body, though invisible, could be detected by measuring the motion of a companion star that might be in orbit around it. Michell had already used a sophisticated statistical analysis of William Herschel’s data on close associations of stellar pairs and triples to conclude that some of them must be selfgravitating systems. It would take 20 more years for Herschel to confirm the existence of binary stars. For a history of the ideas of Michell and Laplace concerning black holes, see Montgomery et al. (2009).

Within general relativity, two key events in the history of black holes were the discovery of the Schwarzschild metric (Schwarzschild, 1916) and the analysis of gravitational collapse across the Schwarzschild horizon (Oppenheimer and Snyder, 1939). However, theoretical black hole physics really came into its own with the discovery of the true nature of the “event horizon” of Schwarzschild’s solution (Finkelstein, 1958; Kruskal, 1960) and the discovery in 1963 of the Kerr metric (Kerr, 1963), now known to be the unique solution for a stationary, vacuum, rotating black hole (with the Schwarzschild metric being the limiting case corresponding to no rotation). Other important developments in the theory of black holes include the full understanding of event horizons as nonsingular, causal boundaries between an exterior spacetime and an interior from which there is no escape, the establishment of black-hole uniqueness and stability, the formulation of singularity theorems, the development of black-hole accretion theory, and the discovery of black-hole thermodynamics and Hawking radiation. For a history, see Israel (1987).

It was the discovery in 1971 of the rapid variations of the X-ray source Cygnus X-1 by telescopes aboard the UHURU satellite that took black holes out of the realm of pure theory (Bolton, 1972; Webster and Murdin, 1972). The source of X-rays was observed to be in a binary system with the companion star HDE 226868; analysis of the nature of the companion and of its orbit around the X-ray source, and detailed study of the X-rays, led to the conclusion that the unseen body was a compact object with a mass exceeding $9 M _ { \odot }$ . Since the maximum masses of white dwarfs and neutron stars are approximately $1 . 4 M _ { \odot }$ and $\sim 3 M _ { \odot }$ , respectively, the simplest conclusion was that the object was a black hole. The source of the X-rays was believed to be the hot, inner regions of an accretion disk around the black hole, formed by gas stripped from the atmosphere of the companion star. Since 1971, many black hole candidates in X-ray binary systems have been found (Celotti et al., 1999).

Studies of the central regions of quasars, galaxies and globular clusters have indicated that supermassive black holes may be ubiquitous (see Kormendy and Richstone (1995) for an early review); indeed, every massive spiral galaxy appears to contain a central massive black hole. There is even a $4 . 3 \times 1 0 ^ { 6 } M _ { \odot }$ black hole in the center of the Milky Way, the precise measurement of its mass being made possible by observations of stars in orbit around it (Eckart and Genzel, 1996; Ghez et al., 1998). Although the masses of such black holes are trivial compared to the total mass of their host galaxies, their apparent ability to generate extraordinary mass and energy outflow from accreting matter can have important feedback effects on the structure of the galaxy, including such phenomena as star formation.

The capstone to the remarkable history of black holes is the September 14, 2015 detection by LIGO of gravitational waves from the inspiral and merger of two black holes of masses 29 and $3 6 M _ { \odot }$ (Abbott et al., 2016c).

General relativity predicts the existence of black holes. Black holes are the end products of catastrophic gravitational collapse in which the collapsing matter crosses an event horizon, a surface whose radius depends upon the mass and angular momentum of matter that has fallen across it, and which is a one-way membrane for timelike or null world lines. Such world lines can cross the horizon moving inward but not outward. The interior of the black hole is causally disconnected from the exterior spacetime. There is considerable evidence to support the claim that any gravitational collapse involving sufficient mass, whether spherically symmetric or not, with zero net charge and zero net angular momentum, results in a black hole whose metric (at late times after the black hole has become stationary) is the Schwarzschild metric, given by

$$
d s ^ { 2 } = - \left( 1 - \frac { 2 M } { r } \right) d t ^ { 2 } + \left( 1 - \frac { 2 M } { r } \right) ^ { - 1 } d r ^ { 2 } + r ^ { 2 } \left( d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } \right) ,
$$

where $M$ is the mass of the black hole. If the collapsing body has net rotation, the black hole is described by the Kerr metric.

While curved spacetime is essential to the existence of event horizons as one-way membranes for the physical interactions, the existence of black holes is not an automatic byproduct of curved spacetime, but depends on the specific theory of gravity.

The general approach for finding black hole solutions in a given theory is the same as for neutron stars, except that one assumes vacuum everywhere. In general relativity, solving Eqs. (10.10) with $\rho = p = 0$ leads immediately to Eq. (10.18). To see if a particular vacuum solution corresponds to a black hole, one must check whether a non-singular event horizon exists, and whether any true physical singularities in the spacetime are safely hidden behind the event horizon. In some theories, different fundamental speeds or “null cones” may be associated with different fields (see Section 11.3), and thus there may be more than one “event” horizon.

Once again, we provide a mere sampling of black hole structure in alternative theories of gravity; see Berti et al. (2015) for a more thorough review, including various attempts to “parametrize” black holes in a manner similar to the PPN formalism.

# Scalar-tensor theories

As one might expect, scalar-tensor theories, being in some sense the least violent modification of general relativity, predict black holes. However, what is unexpected is that they predict black holes whose geometry is identical to the Schwarzschild geometry of general relativity. Roger Penrose was probably the first to conjecture this, in a 1970 talk at the Fifth Texas Symposium on Relativistic Astrophysics. Motivated by this remark, Thorne and Dykla (1971) showed that during gravitational collapse to form a black hole, the Brans-Dicke scalar field is radiated away, leaving only its constant asymptotic value and a Schwarzschild black hole. Hawking (1972) argued on general grounds that the scalar field $\phi$ must be constant throughout the exterior of the horizon, given by its asymptotic cosmological value $\phi _ { 0 }$ . Thus, the vacuum field equation (5.35a) for the metric is Einstein’s vacuum field equation, and the solution is the Schwarzschild solution. The scalar field has no effect other than to determine the value of the gravitational constant $G _ { \mathrm { l o c a l } }$ . (This result also holds for rotating and charged black holes.)

In Brans-Dicke theory for instance, the most direct way to verify this (Hawking, 1972) is to use the vacuum field equation for $\varphi \equiv \phi - \phi _ { 0 }$ , $\bigtriangledown \varphi = 0$ , and to integrate the quantity $\varphi \sqcup \varphi$ over the exterior of the horizon between two spacelike hypersurfaces at different values of coordinate time. After an integration by parts, we obtain

$$
\int \varphi , \alpha \varphi ^ { , \alpha } \sqrt { - g } d ^ { 4 } x - \frac { 1 } { 2 } \int \left( \varphi ^ { 2 } \right) ^ { , \alpha } d \Sigma _ { \alpha } = 0 .
$$

Now the surface integrals over the spacelike hypersurfaces cancel because the situation is stationary. The integral over the hypersurface at infinity vanishes because $\varphi \sim r ^ { - 1 }$ asymptotically. The integral over the horizon vanishes because $d \Sigma _ { \alpha }$ is parallel to the generators of the horizon and is thus in a direction generated by the symmetry transformations of the black hole (Killing direction) whereas $\left( \varphi ^ { 2 } \right) _ { , \alpha }$ vanishes along that symmetry direction. Thus

$$
\int \varphi , _ { \alpha } \varphi ^ { , \alpha } { \sqrt { - g } } d ^ { 4 } x = 0 .
$$

But $\varphi _ { , \alpha }$ is spacelike since $\varphi$ is stationary, so $\varphi , _ { \alpha } \varphi ^ { , \alpha } \ \geq \ 0$ everywhere. Equation (10.20) thus implies that $\varphi _ { , \alpha } = 0$ . Sotiriou and Faraoni (2012) extended Hawking’s theorem to the class of $f ( R )$ theories that can be transformed into generalized scalar-tensor theories.

These theorems can be evaded, for example, if the scalar field is time dependent (e.g., because of cosmic evolution) or complex, or if it is massive and the black hole is rotating (see Berti et al. (2015) for a review).

# Vector-tensor theories

Black-hole solutions have been studied extensively in Einstein-Æther theory and Hoˇrava gravity (Eling and Jacobson, 2006; Tamaki and Miyamoto, 2008; Barausse et al., 2011; Barausse and Sotiriou, 2013a). Barausse et al. (2011) obtained numerical black hole solutions for a range of values of the two parameters $c _ { + }$ and $c _ { - }$ between zero and unity (the equations are so complicated that no analytic solutions were found). They evaluated such observable or invariant quantities as the angular velocity of a particle at the innermost stable circular orbit (ISCO), the angular velocity of the circular photon orbit, the maximum redshift of a photon emitted by a particle on the ISCO, and the proper circumference of the outer event horizon in units of the black hole mass. For $c _ { + } = c _ { - } = 0$ , the solutions were numerically equivalent to the Schwarzschild solution, as expected. These invariant quantities were insensitive to the value of $c _ { - }$ , and depended fairly weakly on $c _ { + }$ , deviating from the general relativistic values by between five and 15 percent for $c _ { + } \sim 0 . 6$ , reaching deviations of 50 percent for $c _ { + } \sim 0 . 9$ . In Hoˇrava gravity, the deviations from general relativity were consistently smaller in most of the parameter space. Slowly rotating black hole solutions have also been analyzed (Barausse and Sotiriou, 2013b; Barausse et al., 2016).

# Tensor-vector-scalar theories

Black-hole solutions in TeVeS were studied by Giannios (2005) and Lasky (2009). For a black hole at rest in the preferred frame, and for the restricted case in which the vector field has only a time component, the physical metric turns out to be identical to the Schwarzschild metric; in the unrestricted case $( K _ { r } \neq 0 )$ ) only the asymptotic properties of the metric and fields were studied.

# Quadratic gravity theories

Non-rotating black hole solutions in a range of quadratic gravity theories were studied with a view toward possible observational signatures by Pani and Cardoso (2009), Yunes and Stein (2011) and Kleihaus et al. (2011); for a brief review, see Blazquez-Salcedo et al.´ (2017). In Chern-Simons theory, spherically symmetric black holes are identical to their general relativistic counterparts, but rotating black holes are not. Slowly rotating black hole models were analysed by Yunes and Pretorius (2009), Konno et al. (2009) and Yagi et al. (2012).

# 10.3 The Motion of Compact Objects

In Chapter 6, we derived the $N .$ -body equations of motion for massive, self-gravitating bodies within the PPN framework [see Eqs. (6.45) and (6.46)]. A key assumption that went into that analysis was that the weak-field, slow-motion limit of gravitational theory applied everywhere, in the interiors of the bodies as well as between them. This assumption restricted the applicability of the equations of motion to systems such as the solar system. However, when dealing with systems containing a neutron star or a black hole with highly relativistic spacetimes near or inside them, one can no longer apply the assumptions of the post-Newtonian limit everywhere, except possibly in the interbody region between the relativistic bodies. Instead, one must employ a method for deriving equations of motion for compact objects that, within a chosen theory of gravity, involves (a) solving the full, relativistic equations for the regions inside and near each body, (b) solving the post-Newtonian equations in the interbody region, and (c) matching these solutions in an appropriate way in a “matching region” surrounding each body. This matching presumably leads to constraints on the motions of the bodies (as characterized by suitably defined centers of mass); these constraints would be the sought-after equations of motion. Such a procedure amounts to a generalization of the Einstein-Infeld-Hoffmann (EIH) approach (Einstein et al., 1938).

Let us first ask what would be expected from such an approach within general relativity. In the fully weak-field post-Newtonian limit, we found that the motion of post-Newtonian bodies is independent of their internal structure, that is, there is no Nordtvedt effect. Each body moves on a geodesic of the post-Newtonian interbody metric generated by the other bodies, with proper allowance for post-Newtonian terms contributed by its own interbody field. This is the EIH result.

It turns out however, that this structure independence seems to be valid even when the bodies are highly compact (neutron stars or black holes). The only restriction is that they be quasistatic, nearly spherical, and sufficiently small compared to their separations that tidal interactions may be neglected. This would be a bad approximation for a neutron star about to spiral into a stellar-mass black hole, for example, but is a good approximation for binary pulsars or for the inspiral of a binary system of compact bodies before the last few orbits.

Although this conclusion has not been proven rigorously, a strong argument for its plausibility can be presented by considering in more detail the matching procedure discussed earlier. We first note that the solution for the relativistic structure and gravitational field of each body is independent of the interbody gravitational field, since we can always choose a coordinate system for each body that is freely falling and approximately Minkowskian in the matching region and in which the body is at rest. Thus, there is no way for the external fields to influence the body or its field, provided that we can neglect tidal effects due to inhomogeneities of the interbody field across the interior of the matching region. Only the velocity and acceleration of the body are affected. Now, if the body is static and spherically symmetric to sufficient accuracy, its external gravitational field is characterized only by its Kepler-measured mass $m$ and is independent of its internal structure; the field is given essentially by the Schwarzschild metric. Thus, the matching procedure described above must yield the same result, whether the body is a black hole of mass $m$ or a post-Newtonian body of mass m. In the latter case, the result is the EIH equations of motion (see Section 6.2), so those equations must be valid in all cases. A slightly different way to see this is to note that because the local field of the body in the freely falling frame is spherically symmetric, depends only on the constant mass $m$ , and is unaffected by the external geometry, the acceleration of the body in the freely falling frame must vanish, so its trajectory must be a geodesic of some metric. The metric to be used is a post-Newtonian interbody metric that includes post-Newtonian terms contributed by the body itself, but that excludes self-fields. This was shown for nonrotating black holes in a seminal paper by D’Eath (1975), and was extended to a variety of contexts by Rudolph and Borner (1978a,b), ¨ Kates (1980), Thorne and Hartle (1985), Anderson (1987), Itoh et al. (2000), and Taylor and Poisson (2008). This structure independence was also verified explicitly to 2PN order for self-gravitating fluid bodies by Mitchell and Will (2007). For a pedagogical treatment of this approach at 1PN order, see PW, section 9.4.

A key element of these derivations is the validity of the Strong Equivalence Principle within general relativity (see Chapter 3 for discussion), which guarantees that the structure of each body is independent of the surrounding gravitational environment. By contrast, most alternative theories of gravity possess additional gravitational fields, whose values in the matching region can influence the structure of each body, and thereby can affect its motion. Consider as a simple example a theory with an additional scalar field (scalartensor theory). In the local freely falling coordinates, although the interbody metric is Minkowskian up to tidal terms, the scalar field has a value $\phi _ { 0 } ( t )$ . In a solution for the structure of the body, this boundary value of $\phi _ { 0 } ( t )$ could influence the resulting mass, for example, by controlling the locally measured value of $G$ , thus turning the mass into a function $m ( \phi _ { 0 } )$ of the scalar field. Thus, the asymptotic metric of the body in the matching region may depend upon its internal structure via the dependence of $m$ on $\phi _ { 0 }$ (essentially, the matching conditions will depend upon $m , d m / d \phi , \ldots )$ . Furthermore, the acceleration of the body in the freely falling frame need not be zero, as we saw in Sections 2.4 and 3.3. If the mass-energy of a body varies as a result of a variation in an external parameter, we found, using cyclic gedanken experiments that assumed only conservation of energy, that (see Eqs. (3.97) and (3.99))

$$
a - a _ { \mathrm { g e o d e s i c } } \sim \frac { 1 } { m } \nabla E _ { \mathrm { B } } ( X , V ) \sim \frac { \partial \ln m } { \partial \phi } \nabla \phi .
$$

Thus, the bodies need not follow geodesics of any metric, rather their motion may depend on their internal structure.

In practice, the matching procedure described above is very cumbersome (D’Eath, 1975). Within general relativity, a simpler method for obtaining the EIH equations of motion is to treat each body as a “point” mass of inertial mass $m _ { a }$ and to solve Einstein’s equations using a point-mass matter action or energy-momentum tensor, with proper care to neglect or regularize infinite “self” fields. In the action for general relativity, we thus write

$$
I = \frac { 1 } { 1 6 \pi G } \int R \sqrt { - g } d ^ { 4 } x - \sum _ { a } m _ { a } \int d \tau _ { a } ,
$$

where $\tau _ { a }$ is proper time along the world line of the ath body. By solving the field equations to 1PN order, it is then possible to derive straightforwardly from the matter action an $N .$ - body EIH action in the form

$$
I _ { \mathrm { E I H } } = \int L ( \pmb { x } _ { 1 } , . . . . \pmb { x } _ { N } , \pmb { \nu } _ { 1 } , . . . \pmb { \nu } _ { N } ) d t ,
$$

with a Lagrangian $L$ written purely in terms of the variables $( \boldsymbol { x } _ { a } , \boldsymbol { \nu } _ { a } )$ of the bodies. The result is Eq. (6.81), with the PPN parameters set to their general relativistic values. The $N$ -body EIH equations of motion are then given by

$$
\frac { d } { d t } \frac { \partial L } { \partial \nu _ { a } ^ { j } } - \frac { \partial L } { \partial x _ { a } ^ { j } } = 0 , \quad a = 1 , \dots N .
$$

In alternative theories of gravity, we assume that the only difference is the possible dependence of the mass on the boundary values of the auxiliary fields. In the quasi-Newtonian limit (Sections 2.4 and 3.3), this was sufficient to yield the complete quasi-Newtonian acceleration of composite bodies including modifications (Nordtvedt effect) due to their internal structure. Thus, following the suggestion of Eardley (1975), we merely replace the constant inertial mass $m _ { a }$ in the matter action with the variable inertial mass $m _ { a } ( \psi _ { A } )$ , where $\psi _ { A }$ represents the values of the external auxiliary fields, evaluated at the body (we neglect their variation across the interior of the matching region), with infinite self-field contributions excluded. The functional dependence of $m _ { a }$ upon the variable $\psi _ { A }$ will depend on the nature and structure of the body. Thus, we write the action of the alternative theory in the form

$$
I = I _ { G } - \sum _ { a } \int m _ { a } \left( \psi _ { A } [ { \pmb x } _ { a } ( \tau _ { a } ) ] \right) d \tau _ { a } ,
$$

where $I _ { G }$ is the action for the metric and auxiliary fields $\psi _ { A }$ . In varying the action with respect to the fields $g _ { \mu \nu }$ and $\psi _ { A }$ , the variation of $m _ { a }$ must now be taken into account. In the post-Newtonian limit, where the fields $\psi _ { A }$ are expanded about asymptotic values $\psi _ { A } ^ { ( 0 ) }$ according to $\psi _ { A } = \psi _ { A } ^ { ( 0 ) } + \delta \psi _ { A }$ , it is generally sufficient to expand $m _ { a } ( \psi _ { A } )$ in the form

$$
m _ { a } ( \psi _ { A } ) = m _ { a } ( \psi _ { A } ^ { ( 0 ) } ) + \sum _ { A } \frac { \partial m _ { a } } { \partial \psi _ { A } ^ { ( 0 ) } } \delta \psi _ { A } + \frac { 1 } { 2 } \sum _ { A , B } \frac { \partial ^ { 2 } m _ { a } } { \partial \psi _ { A } ^ { ( 0 ) } \partial \psi _ { B } ^ { ( 0 ) } } \delta \psi _ { A } \delta \psi _ { B } + \ldots .
$$

Thus, the final form of the metric and of the $N -$ -body Lagrangian will depend on $m _ { a } \equiv$ $m _ { a } ( \psi _ { A } ^ { ( 0 ) } )$ and on the parameters $\partial m _ { a } / \partial \psi _ { A } ^ { ( 0 ) }$ , and so on. We will use the term “sensitivities” to describe these parameters, since they measure the sensitivity of the inertial mass to changes in the fields $\psi _ { A }$ . Thus, we define

$$
\begin{array} { c } { { s _ { a } ^ { ( A ) } \equiv \displaystyle \frac { \partial \ln m _ { a } } { \partial \ln \psi _ { A } ^ { ( 0 ) } } , } } \\ { { s _ { a } ^ { \prime } { } ^ { ( A B ) } \equiv \displaystyle \frac { \partial ^ { 2 } \ln m _ { a } } { \partial \ln \psi _ { A } ^ { ( 0 ) } \partial \ln \psi _ { B } ^ { ( 0 ) } } , } } \end{array}
$$

and so on, where the derivatives are typically taken holding the total baryon number of the body fixed, for bodies made of matter. For black holes, some other method must be used to identify the sensitivities. Similar sensitivities can be defined for the radius and moment of inertia of the compact body. The final result is a “modified EIH formalism.”

Gralla (2010, 2013) developed a more general theory of the motion of “small” bodies characterized by such parameters as mass, spin and charge in an environment of external fields, and argued that Eardley’s ansatz is a special case of that general framework.

# 10.3.1 A modified EIH formalism

By analogy with the PPN formalism, a general EIH formalism can be constructed using arbitrary parameters whose values depend both on the theory under study and on the nature of the bodies in the system. However, to keep the resulting formalism simple, we will make some restrictions. First, we restrict attention to semiconservative theories of gravity; every Lagrangian-based metric theory of gravity falls into this class. We will also restrict attention to theories of gravity that have no Whitehead term in the post-Newtonian limit; all of the currently viable theories described in Chapter 5 satisfy this constraint. This generalizes the formalism presented in the first edition of this book, which made a restriction to fully conservative theories. Nordtvedt (1985) discussed a similar formalism for compact-body dynamics.

Each body is characterized by an inertial mass $m _ { a }$ , defined to be the quantity that appears in the conservation laws for energy and momentum that emerge from the EIH Lagrangian. We then write for the metric, valid in the interbody region and far from the system,

$$
\begin{array} { l } { { \displaystyle g _ { 0 0 } = - 1 + 2 \sum _ { a } \alpha _ { a } ^ { * } \frac { m _ { a } } { | { \bf x } - { \bf x } _ { a } | } + O ( \epsilon ^ { 2 } ) , } } \\ { { \displaystyle g _ { 0 j } = O ( \epsilon ^ { 3 / 2 } ) , } } \\ { { \displaystyle g _ { j k } = \left( 1 + 2 \sum _ { a } \gamma _ { a } ^ { * } \frac { m _ { a } } { | { \bf x } - { \bf x } _ { a } | } \right) \delta _ { j k } + O ( \epsilon ^ { 2 } ) , } } \end{array}
$$

where $\alpha _ { a } ^ { * }$ and $\gamma _ { a } ^ { * }$ are functions of the parameters of the theory and of the structure of the ath body. For test-body geodesics in this metric, the quantities $\alpha _ { a } ^ { * } m _ { a }$ , and $\sum _ { a } \alpha _ { a } ^ { * } m _ { a }$ are the Kepler-measured active gravitational masses of the individual bodies and of the system as a whole. In general relativity, $\alpha _ { a } ^ { * } \equiv \gamma _ { a } ^ { * } \equiv 1$ .

To obtain the modified EIH Lagrangian, we first generalize the post-Newtonian semiconservative $N .$ -body Lagrangian, Eq. (6.81), in a natural way, to obtain

$$
\begin{array} { c } { { { \displaystyle { \cal L } _ { \mathrm { E H } } = - \sum _ { a } m _ { a } \left[ 1 - \frac { 1 } { 2 } \nu _ { a } ^ { 2 } - \frac { 1 } { 8 } \left( 1 + { \mathcal A } _ { a } \right) \nu _ { a } ^ { 4 } \right] } } } \\ { { + \displaystyle { \frac { 1 } { 2 } \sum _ { a } \sum _ { b \neq a } \frac { m _ { a } m _ { b } } { r _ { a b } } \left[ { \mathcal G } _ { a b } + 3 { \mathcal B } _ { a b } \nu _ { a } ^ { 2 } - \frac { 1 } { 2 } \left( { \mathcal G } _ { a b } + 6 { \mathcal B } _ { ( a b ) } + { \mathcal G } _ { a b } \right) \nu _ { a } \cdot \nu _ { b } \right. } } } \\ { { \displaystyle { \left. \mathrm { ~ \ ~ \ - \frac { 1 } { 2 } \left( { \mathcal G } _ { a b } + { \mathcal E } _ { a b } \right) \left( \nu _ { a } \cdot n _ { a b } \right) \left( \nu _ { b } \cdot n _ { a b } \right) } \right] } } } \\ { { - \displaystyle { \frac { 1 } { 2 } \sum _ { a } \sum _ { b \neq a } \sum _ { c \neq a } \mathcal D _ { a b c } \frac { m _ { a } m _ { b } } { r _ { a b } } \frac { m _ { c } } { r _ { a c } } } , } } \end{array}
$$

where ${ \pmb n } _ { a b } = { \pmb x } _ { a b } / r _ { a b }$ . Notice that we did not introduce a parameter in front of the $\nu _ { a } ^ { 2 }$ term in Eq. (10.29). Any such parameter can always be absorbed into a new definition of the inertial mass $m _ { a } ^ { \prime }$ of body $a$ . We are then free to change the constant term $- \sum _ { a } m _ { a }$ to be the sum of the new inertial masses $- \sum a ^ { \prime }$ . This has no effect on the equations of motion, but does allow the Hamiltonian derived from $L _ { \mathrm { E I H } }$ to be the sum of the new inertial masses at lowest order. We also did not include a term of the form $( m _ { a } m _ { b } / r _ { a b } ) ( { \bf { v } } _ { b } \cdot { \bf { n } } _ { a b } ) ^ { 2 }$ ; such a term can be associated (via a total time derivative in the Lagrangian) with the Whitehead term in Eq. (6.81), which we have chosen to reject.

The quantities $\mathbf { \mathcal { A } } _ { a }$ , $\mathcal { G } _ { a b }$ , $\mathcal { B } _ { a b }$ , $\mathcal { C } _ { a b }$ , ${ \mathcal { E } } _ { a b }$ and $\mathcal { D } _ { a b c }$ are functions of the parameters of the theory and of the structure of each body, and satisfy

$$
\mathcal { G } _ { a b } = \mathcal { G } _ { ( a b ) } , \quad \mathcal { C } _ { a b } = \mathcal { C } _ { ( a b ) } , \quad \mathcal { E } _ { a b } = \mathcal { E } _ { ( a b ) } , \quad \mathcal { D } _ { a b c } = \mathcal { D } _ { a ( b c ) } .
$$

Note that $\mathcal { B } _ { a b }$ has no special symmetry, in general.

In general relativity, $\mathcal { G } _ { a b } = \mathcal { B } _ { a b } = \mathcal { D } _ { a b c } = 1$ , while $\mathcal { A } _ { a } = \mathcal { C } _ { a b } = \mathcal { E } _ { a b } = 0$ . In the post-Newtonian limit of semiconservative theories (with $\xi = 0$ ), for structureless masses (no self-gravity), the parameters have the values [compare Eq. (6.81)]

$$
\begin{array} { c l } { { \mathcal { G } _ { a b } = 1 , } } & { { \mathcal { B } _ { a b } = \displaystyle \frac { 1 } { 3 } ( 2 \gamma + 1 ) , \quad \mathcal { D } _ { a b c } = 2 \beta - 1 , } } \\ { { \mathcal { A } _ { a } = 0 , \quad \mathcal { C } _ { a b } = \alpha _ { 1 } - \alpha _ { 2 } , \quad \mathcal { E } _ { a b } = \alpha _ { 2 } . } } \end{array}
$$

In the fully conservative case, including contributions of the self-gravitational binding energies of the bodies, the parameters have the values

$$
\begin{array} { l } { { \displaystyle \mathcal G _ { a b } = 1 + ( 4 \beta - \gamma - 3 ) \left( \frac { \Omega _ { a } } { m _ { a } } + \frac { \Omega _ { b } } { m _ { b } } \right) , } } \\ { { \displaystyle \mathcal B _ { a b } = \frac { 1 } { 3 } ( 2 \gamma + 1 ) , \quad \mathcal D _ { a b c } = 2 \beta - 1 , } } \\ { { \displaystyle \mathcal A _ { a } = \mathcal C _ { a b } = \mathcal E _ { a b } = 0 , } } \end{array}
$$

where $\Omega _ { a }$ is the self-gravitational energy of the ath body.

In a theory of gravity that singles out a preferred frame, such as the Einstein-Æther theory, the Lagrangian (10.29) must be understood to be defined in that frame. To obtain the Lagrangian in a moving frame, we must carry out a post-Galilean transformation of the Lagrangian (see Section 4.3 for discussion). We make a low-velocity Lorentz transformation (post-Galilean transformation) from $( t , x )$ to $( \tau , \xi )$ coordinates, given by

$$
\begin{array} { l } { { { \displaystyle { \pmb x } = { \pmb \xi } + \left( 1 + \frac { 1 } { 2 } w ^ { 2 } \right) { \pmb w } \tau + \frac { 1 } { 2 } ( { \pmb \xi } \cdot { \pmb w } ) { \pmb w } + { \boldsymbol \xi } \times { \cal O } ( \epsilon ^ { 2 } ) } , \ ~ } } \\ { { { \displaystyle t = \tau \left( 1 + \frac { 1 } { 2 } w ^ { 2 } + \frac { 3 } { 8 } w ^ { 4 } \right) + \left( 1 + \frac { 1 } { 2 } w ^ { 2 } \right) { \pmb \xi } \cdot { \pmb w } + \tau \times { \cal O } ( \epsilon ^ { 3 } ) } . \ } } \end{array}
$$

From the transformation (10.33), we have

$$
\begin{array} { l } { { { \displaystyle { \nu } _ { a } = \nu _ { a } + w - \frac { d \nu _ { a } } { d \tau } ( { \pmb \xi } _ { a } \cdot { \pmb w } ) - \frac { 1 } { 2 } w ^ { 2 } \nu _ { a } - ( { \pmb \nu } _ { a } \cdot { \pmb w } ) \left( \nu _ { a } + \frac { 1 } { 2 } { \pmb w } \right) } \ , } } \\ { { \displaystyle \frac { 1 } { r _ { a b } } = \frac { 1 } { \xi _ { a b } } \left[ 1 + \frac { 1 } { 2 } ( { \pmb w } \cdot { \pmb n } _ { a b } ^ { \prime } ) ^ { 2 } + \frac { 1 } { \xi _ { a b } } ( ( { \pmb w } \cdot { \pmb \xi } _ { a } ) ( { \pmb \nu } _ { a } \cdot { \pmb n } _ { a b } ^ { \prime } ) - ( { \pmb w } \cdot { \pmb \xi } _ { b } ) ( { \pmb \nu } _ { b } \cdot { \pmb n } _ { a b } ^ { \prime } ) ) \right] \ / , } } \end{array}
$$

where $\xi _ { a } , \xi _ { b }$ and $\pmb { \nu } _ { a } \equiv d \pmb { \xi } _ { a } / d \tau$ are to be evaluated at the same time, given by a clock at the spatial origin $( \xi = 0$ ) of the moving coordinate system, and ${ \pmb n } _ { a b } ^ { \prime } \equiv { \pmb \xi } _ { a b } / \xi _ { a b }$ . The new Lagrangian is given by

$$
L ( \pmb \xi , \tau ) = L ( \pmb x , t ) \frac { d t } { d \tau } - \frac { d f } { d \tau } ,
$$

where $d t / d \tau$ is evaluated at $\xi = 0$ , and where we are free to subtract a total time derivative of a function $f$ to simplify the new Lagrangian. Substituting these results into Eqs. (10.29) and (10.35), dropping constants and total time derivatives, and replacing $\xi _ { a b }$ and $\nu _ { a }$ with $r _ { a b }$ and $\nu _ { a }$ , we obtain the Lagrangian in the moving frame

$$
\begin{array} { l } { { \displaystyle { \cal L } = { \cal L } _ { \mathrm { E I H } } + \displaystyle \frac { 1 } { 4 } \sum _ { a } m _ { a } { \cal A } _ { a } \left[ \nu _ { a } ^ { 2 } w ^ { 2 } + 2 \nu _ { a } ^ { 2 } ( \nu _ { a } \cdot w ) + 2 ( \nu _ { a } \cdot w ) ^ { 2 } \right] } } \\ { ~ } \\ { { \displaystyle ~ - \frac { 1 } { 4 } \sum _ { a \neq b } \frac { m _ { a } m _ { b } } { r _ { a b } } \left\{ \mathcal { C } _ { a b } w ^ { 2 } - 2 \left( 6 \mathcal { B } _ { [ a b ] } - \mathcal { C } _ { a b } \right) ( \nu _ { a } \cdot w ) \right. } } \\ { { \displaystyle ~ \left. + \mathcal { E } _ { a b } \left[ ( w \cdot n _ { a b } ) ^ { 2 } + 2 ( w \cdot n _ { a b } ) ( \nu _ { a } \cdot n _ { a b } ) \right] \right\} . } } \end{array}
$$

Notice that the Lagrangian is post-Galilean invariant if and only if

$$
\mathcal { A } _ { a } \equiv { \mathcal { B } } _ { [ a b ] } \equiv \mathcal { C } _ { a b } \equiv \mathcal { E } _ { a b } \equiv 0 .
$$

These quantities are the preferred-frame parameters of our modified EIH formalism.

Since our ultimate goal is to apply this formalism to binary systems containing compact objects, let us now restrict attention to two-body systems. We obtain from $L$ the two-body equations of motion

$$
\begin{array} { r l } { a _ { 1 } = - \frac { 8 a _ { 1 } \theta } { c ^ { 2 } } \Bigg [ a _ { 1 } - 1 . 9 8 a _ { 1 } b _ { 2 } - 2 . 9 8 \Bigg ] \frac { \theta _ { 1 } } { c ^ { 2 } } } \\ { - \frac { 1 } { 2 } ( 5 a _ { 2 } ^ { 2 } - 6 b _ { 3 } c _ { 3 } - 1 2 . 9 8 ) + \mathcal { O } ( \epsilon a _ { 1 } c _ { 3 } + \mathcal { O } ( \epsilon a _ { 2 } + \mathcal { O } ( \epsilon a _ { 3 } ) ) ) \frac { \theta _ { 1 } } { c ^ { 3 } } } \\ { - \frac { 1 } { 2 } ( 5 a _ { 3 } ^ { 2 } - 6 a _ { 2 } c _ { 1 } ( 1 + A _ { 3 } ) ) \eta _ { 1 } ^ { 2 } + \frac { 1 } { 2 } ( 3 a _ { 3 } + \mathcal { O } ( \epsilon a _ { 2 } - \mathcal { O } ( \epsilon a _ { 3 } ) ) ) \frac { \theta _ { 1 } } { c ^ { 3 } } } \\ { + \frac { 1 } { 2 } ( 5 a _ { 3 } - 7 a _ { 2 } c _ { 1 } ( 1 + A _ { 3 } ) ) \eta _ { 2 } ^ { 3 } + \frac { 1 } { 2 } ( 3 a _ { 3 } + \mathcal { O } ( \epsilon a _ { 2 } - \mathcal { O } ( \epsilon a _ { 3 } ) ) ) } \\ { - \frac { 1 } { 2 } ( 6 a _ { 3 } + 3 \theta _ { 1 } c _ { 3 } + 2 9 a _ { 1 } + 5 a _ { 2 } ( 1 + A _ { 3 } ) ) \eta _ { 3 } ^ { 2 } - \frac { 1 } { 2 } ( 5 a _ { 2 } + 5 a _ { 1 } ^ { 2 } ) \eta _ { 3 } ^ { 2 } } \\ { + \frac { 1 } { 2 } ( 6 \epsilon a _ { 3 } + \epsilon a _ { 3 } ) \eta _ { 3 } ^ { 2 } + \frac { 1 } { 2 } ( 5 a _ { 2 } - 6 a _ { 1 } ( 1 - c _ { 3 } ) - 2 6 a _ { 2 } ( 1 + A _ { 3 } ) ) \eta _ { 3 } + \mathcal { O } ( \epsilon a _ { 1 } c _ { 3 } ) } \\ { + \frac { 1 } { 2 } ( 5 a _ { 2 } - 6 a _ { 1 } - 5 a _ { 2 } ( 1 + A _ { 3 } ) ) \eta _ { 3 } } \\  + \frac { 1 } { 2 } ( 5 a _ { 3 } ^ { 2 } - 6 a _  \end{array}
$$

where $\pmb { a } _ { a } \equiv d \pmb { \nu } _ { a } / d t$ , ${ \pmb x } \equiv { \pmb x } _ { 1 } - { \pmb x } _ { 2 }$ , $r \equiv | { \boldsymbol { x } } |$ , and ${ \pmb n } \equiv { \pmb x } / r$ . If the conditions of Eq. (10.37) hold, then the preferred-frame terms vanish.

To Newtonian order, the center of mass $X ~ = ~ ( m _ { 1 } x _ { 1 } + m _ { 2 } x _ { 2 } ) / m$ of the system is unaccelerated, thus, to sufficient accuracy in the post-Newtonian terms, we can set $\boldsymbol { X } =$ ${ \dot { X } } = 0$ and write

$$
\begin{array} { l } { { \displaystyle x _ { 1 } = \left[ \frac { m _ { 2 } } { m } + O ( \epsilon ) \right] x , } } \\ { { \displaystyle x _ { 2 } = - \left[ \frac { m _ { 1 } } { m } + O ( \epsilon ) \right] x . } } \end{array}
$$

As in Section 6.4.1, we define

$$
\begin{array} { l } { { \pmb { \nu } \equiv \pmb { \nu } _ { 1 } - \pmb { \nu } _ { 2 } , \quad { \pmb { a } } \equiv { \pmb { a } } _ { 1 } - { \pmb { a } } _ { 2 } , } } \\ { { \pmb { m } \equiv m _ { 1 } + m _ { 2 } , \quad \eta \equiv \displaystyle \frac { m _ { 1 } m _ { 2 } } { m ^ { 2 } } , \quad \Delta = \displaystyle \frac { m _ { 2 } - m _ { 1 } } { m } . } } \end{array}
$$

We also define the coefficients

$$
\begin{array} { r l } & { \mathcal { G } \equiv \mathcal { G } _ { 1 2 } , \quad \mathcal { B } _ { + } \equiv \mathcal { B } _ { ( 1 2 ) } , \quad \mathcal { B } _ { - } \equiv \mathcal { B } _ { [ 1 2 ] } , \quad \mathcal { D } \equiv \cfrac { m _ { 2 } } { m } \mathcal { D } _ { 1 2 2 } + \cfrac { m _ { 1 } } { m } \mathcal { D } _ { 2 1 1 } , } \\ & { \mathcal { C } \equiv \mathcal { C } _ { 1 2 } , \quad \mathcal { E } \equiv \mathcal { E } _ { 1 2 } , \quad \mathcal { A } ^ { ( n ) } \equiv \left( \cfrac { m _ { 2 } } { m } \right) ^ { n } \mathcal { A } _ { 1 } - \left( - \cfrac { m _ { 1 } } { m } \right) ^ { n } \mathcal { A } _ { 2 } . } \end{array}
$$

Then the equation of motion for the relative orbit takes the form

$$
\pmb { a } = \pmb { a } _ { \mathrm { L } } + \pmb { a } _ { \mathrm { P F } } ,
$$

where the purely two-body, or “local” contributions have the form (we use “hats” to denote parameters associated with compact bodies)

$$
{ a _ { \mathrm { L } } } = - \frac { \mathcal { G } m n } { { { r ^ { 2 } } } } + \frac { m } { { { r ^ { 2 } } } } \left[ { n \left( { \hat { A } _ { 1 } } { \nu ^ { 2 } } + { \hat { A } _ { 2 } } { \dot { r } } ^ { 2 } + { \hat { A } _ { 3 } } \frac { m } { r } \right) + \dot { r } { \nu } { \hat { B } _ { 1 } } } \right] ,
$$

where

$$
\begin{array} { l } { \displaystyle \hat { A } _ { 1 } = \frac 1 2 \left\{ \mathcal { G } \left( 1 - 6 \eta \right) - 3 \mathcal { B } _ { + } - 3 \Delta \mathcal { B } _ { - } - \eta ( \mathcal { C } + 2 \mathcal { E } ) + \mathcal { G } A ^ { ( 3 ) } \right\} , } \\ { \displaystyle \hat { A } _ { 2 } = \frac 3 2 \eta ( \mathcal { G } + \mathcal { E } ) , } \\ { \displaystyle \hat { A } _ { 3 } = \mathcal { G } \left[ 2 \eta \mathcal { G } + 3 \mathcal { B } _ { + } + \eta \left( \mathcal { C } + \mathcal { E } \right) + 3 \Delta \mathcal { B } _ { - } \right] + \mathcal { D } , } \\ { \displaystyle \hat { B } _ { 1 } = \mathcal { G } ( 1 - 2 \eta ) + 3 \mathcal { B } _ { + } + 3 \Delta \mathcal { B } _ { - } + \eta \mathcal { C } + \mathcal { G } A ^ { ( 3 ) } , } \end{array}
$$

and the preferred-frame contributions have the form

$$
\begin{array} { l } { \displaystyle { \boldsymbol { a } } _ { \mathrm { P F } } = + \frac { m } { r ^ { 2 } } \left\{ n \left[ \left( \frac { 1 } { 2 } \hat { \alpha } _ { 1 } + 2 \mathcal { G } \mathcal { A } ^ { ( 2 ) } \right) ( w \cdot v ) + \frac { 3 } { 2 } \left( \hat { \alpha } _ { 2 } + \mathcal { G } \mathcal { A } ^ { ( 1 ) } \right) ( w \cdot n ) ^ { 2 } \right] \right. } \\ { \displaystyle \left. - w \left[ \frac { 1 } { 2 } \hat { \alpha } _ { 1 } ( n \cdot v ) + \hat { \alpha } _ { 2 } ( n \cdot w ) \right] + \mathcal { G } \mathcal { A } ^ { ( 2 ) } \nu ( n \cdot w ) \right\} , } \end{array}
$$

where

$$
\begin{array} { r l } & { \hat { \alpha } _ { 1 } = \Delta \left( \mathcal { C } + \mathcal { E } \right) - 6 \mathcal { B } _ { - } - 2 \mathcal { G } \mathcal { A } ^ { ( 2 ) } , } \\ & { } \\ & { \hat { \alpha } _ { 2 } = \mathcal { E } - \mathcal { G } \mathcal { A } ^ { ( 1 ) } . } \end{array}
$$

These two parameters play the role of compact-body analogues of the PPN parameters $\alpha _ { 1 }$ and $\alpha _ { 2 }$ in the context of binary systems.

In the Newtonian limit of the orbital motion, we have $\pmb { a } = \mathcal { G } m \pmb { x } / r ^ { 3 }$ , with Keplerian orbit solutions given by Eq. (6.73), but with $m$ replaced by $\mathcal { G } m$ . The post-Newtonian terms in Eq. (10.43) can be inserted into the Lagrange planetary equations (6.74). Using the methods outlined in Section 6.4.2, we find that the pericenter advance per orbit is given by

$$
\Delta \omega = \frac { 6 \pi m } { p } { \mathcal P } \mathcal { G } ^ { - 1 } ,
$$

where $p = a ( 1 - e ^ { 2 } )$ , and where

$$
\boldsymbol { \mathcal { P } } = \mathcal { G } \mathcal { B } _ { + } + \frac { 1 } { 6 } \left( \mathcal { G } ^ { 2 } - \mathcal { D } \right) + \frac { 1 } { 6 } \mathcal { G } \left[ 6 \Delta \mathcal { B } _ { - } + \eta \mathcal { G } ( 2 \mathcal { C } + \mathcal { E } ) + \mathcal { G } \mathcal { A } ^ { ( 3 ) } \right] .
$$

This is the only secular perturbation produced by the post-Newtonian terms in Eq. (10.43).   
In the PPN limit, this result agrees with Eq. (6.78) for semiconservative theories.

We can convert $\Delta \omega$ to a rate by dividing by the orbital period and can use $P _ { \mathrm { { b } } } ~ =$ $2 \pi ( a ^ { 3 } / \mathcal { G } m ) ^ { 1 / 2 }$ , to eliminate $a$ to obtain

$$
\langle \dot { \omega } \rangle = \frac { 6 \pi } { P _ { \mathrm { b } } ( 1 - e ^ { 2 } ) } \left( \frac { 2 \pi m } { P _ { \mathrm { b } } } \right) ^ { 2 / 3 } \mathcal { P } \mathcal { G } ^ { - 4 / 3 } .
$$

This expression will be useful for discussing binary pulsar measurements.

We can also use the preferred-frame contributions to the equations of motion $\pmb { a } _ { \mathrm { P F } }$ to work out the secular perturbations of the orbit elements of a binary system, extending the analysis of Section 8.2 to systems with compact bodies. The results are identical to Eqs. (8.2), (8.33), (8.35), and (8.37), with $\xi = 0$ , and with $\hat { \alpha } _ { 1 }$ and $\hat { \alpha } _ { 2 }$ replacing $\alpha _ { 1 }$ and $\alpha _ { 2 }$ , respectively.

Returning to the full $N .$ -body Lagrangian (10.29), and working at quasi-Newtonian order, we can derive the leading effects in a hierarchical three-body system, such as the pulsar triple $J 0 3 3 7 \substack { + 1 7 1 5 }$ , including the Nordtvedt effect. The resulting equation of motion for the inner binary is given by Eqs. (8.10)–(8.12), with

$$
\begin{array} { c } { { m ^ { * } = \mathcal { G } _ { 1 2 } m , } } \\ { { { } } } \\ { { \displaystyle \alpha = \frac 1 2 \left( \mathcal { G } _ { 1 3 } + \mathcal { G } _ { 2 3 } \right) , } } \\ { { { } } } \\ { { \displaystyle \delta = \mathcal { G } _ { 1 3 } - \mathcal { G } _ { 2 3 } . } } \end{array}
$$

As an illustration of this modified EIH framework for compact bodies, we will again focus on specific theories where calculations have been carried out. As we have already discussed, a variety of approaches have shown that the EIH equations of motion for compact objects within general relativity are identical to those of the post-Newtonian limit with weak fields everywhere. In other words, in general relativity, $\mathcal { G } _ { a b } \equiv B _ { a b } \equiv \mathcal { D } _ { a b c } \equiv 1$ , and the remaining coefficients vanish, independently of the nature of the bodies.

# 10.3.2 Scalar-tensor theories

The modified EIH formalism was first developed by Eardley (1975) for application to Brans-Dicke theory. It makes use of the fact that only the scalar fleld $\phi$ produces an external influence on the structure of each compact body via its boundary values in the matching region. This boundary value of $\phi$ is related to the local value of the gravitational constant as felt by the compact body by

$$
G _ { \mathrm { l o c a l } } = \frac { G } { \phi } \left( \frac { 4 + 2 \omega } { 3 + 2 \omega } \right) ,
$$

where $G$ is the fundamental gravitational coupling constant. Thus we will treat the inertial mass $m _ { a }$ of each body as a being a function of $\phi$ . Then, by defining the deviation of $\phi$ from its asymptotic value $\phi _ { 0 }$ as in Section 5.3.2, $\phi \equiv \phi _ { 0 } ( 1 + \Psi )$ , we can write down the expansion

$$
m _ { a } ( \phi ) = m _ { a } \left[ 1 + s _ { a } \Psi + \frac { 1 } { 2 } ( s _ { a } ^ { 2 } + s _ { a } ^ { \prime } - s _ { a } ) \Psi ^ { 2 } + O ( \Psi ^ { 3 } ) \right] ,
$$

where $m _ { a } \equiv m _ { a } ( \phi _ { 0 } )$ , and we define the dimensionless sensitivities

$$
\begin{array} { l } { { \displaystyle s _ { a } \equiv \left( \frac { d \ln m _ { a } ( \phi ) } { d \ln \phi } \right) _ { 0 } \mathrm { , } } } \\ { { \displaystyle s _ { a } ^ { \prime } \equiv \left( \frac { d ^ { 2 } \ln m _ { a } ( \phi ) } { d ( \ln \phi ) ^ { 2 } } \right) _ { 0 } . } } \end{array}
$$

The action for the theory is then written

$$
I = \frac { 1 } { 1 6 \pi G } \int \left[ \phi R - \frac { \omega ( \phi ) } { \phi } g ^ { \mu \nu } \phi _ { , \mu } \phi _ { , \nu } \right] \sqrt { - g } d ^ { 4 } x - \sum _ { a } \int m _ { a } ( \phi ) d \tau _ { a } ,
$$

where the integrals over proper time $\tau _ { a }$ are to be taken along the world line of each body $a$ . We have dropped the scalar self-interaction potential $U ( \phi )$ . It is straightforward to vary the action with respect to $g _ { \mu \nu }$ and $\phi$ to obtain the field equations,

$$
\begin{array} { l } { { G _ { \mu \nu } = \displaystyle \frac { 8 \pi G } { \phi } T _ { \mu \nu } + \frac { \omega ( \phi ) } { \phi ^ { 2 } } \left( \phi _ { , \mu } \phi _ { , \nu } - \frac { 1 } { 2 } g _ { \mu \nu } \phi _ { , \lambda } \phi ^ { , \lambda } \right) } } \\ { { { } } } \\ { { { } + \displaystyle \frac { 1 } { \phi } \left( \phi _ { ; \mu \nu } - g _ { \mu \nu } \Pi _ { g } \phi \right) , } } \\ { { { } } } \\ { { \Pi _ { g } \phi = \displaystyle \frac { 1 } { 3 + 2 \omega ( \phi ) } \left( 8 \pi G T - 1 6 \pi G \phi \frac { \partial T } { \partial \phi } - \frac { d \omega } { d \phi } \phi _ { , \lambda } \phi ^ { , \lambda } \right) , } } \end{array}
$$

where

$$
T ^ { \mu \nu } = ( - g ) ^ { - 1 / 2 } \sum _ { a } m _ { a } ( \phi ) u _ { a } ^ { \mu } u _ { a } ^ { \nu } ( u _ { a } ^ { 0 } ) ^ { - 1 } \delta ^ { 3 } ( { \bf x } - { \bf x } _ { a } ) ,
$$

where $u _ { a } ^ { \mu }$ is the four-velocity of body $a$ . The equations of motion take the form

$$
T ^ { \mu \nu } { } _ { ; \nu } - \frac { \partial T } { \partial \phi } \phi ^ { , \nu } = 0 .
$$

In harmonic gauge, the relaxed field equations for $\tilde { h } ^ { \alpha \beta }$ are given by Eqs. (5.43), while for the scalar field, the relaxed field equation is given by Eqs. (5.45) and (5.46), but with the replacement

$$
\tilde { T }  \frac { \phi _ { 0 } ^ { 2 } } { \phi ^ { 2 } } ( T - 2 \phi \frac { \partial T } { \partial \phi } ) .
$$

where $T = T ^ { \mu \nu } g _ { \mu \nu }$

Repeating the post-Newtonian calculation using the relaxed field equations, as described in Section 5.3.2, we obtain, to lowest order

$$
\begin{array} { l } { { \displaystyle \Psi = 2 \zeta \sum _ { b } \frac { m _ { b } } { r _ { b } } \left( 1 - 2 s _ { b } \right) + O \left( \epsilon ^ { 2 } \right) } , }  \\ { { \displaystyle g _ { 0 0 } = - 1 + 2 \sum _ { b } \frac { m _ { b } } { r _ { b } } \left( 1 - 2 \zeta s _ { b } \right) + O \left( \epsilon ^ { 2 } \right) } , }  \\ { { \displaystyle g _ { 0 j } = - 4 ( 1 - \zeta ) \sum _ { b } \frac { m _ { b } \nu _ { b } ^ { j } } { r _ { b } } + O ( \epsilon ^ { 5 / 2 } ) } , }  \\ { { \displaystyle g _ { j k } = \delta _ { j k } \left[ 1 + 2 \sum _ { b } \frac { m _ { b } } { r _ { b } } \left( 1 - 2 \zeta + 2 \zeta s _ { b } \right) \right] , } } \end{array}
$$

where $\zeta = 1 / ( 4 + 2 \omega _ { 0 } )$ , $r _ { b } = | { \pmb x } - { \pmb x } _ { b } |$ , and we have chosen units in which $G _ { \mathrm { l o c a l } } = 1$ . For the explicit $O ( \epsilon ^ { 2 } )$ terms in $g _ { 0 0 }$ and $\Psi$ , see Mirshekari and Will (2013). Notice that the

active gravitational mass as measured by test-body Keplerian orbits far from each body is given by

$$
( m _ { \mathrm { A } } ) _ { a } = m _ { a } ( 1 - 2 \zeta s _ { a } ) .
$$

To compare with the post-Newtonian limit, we must connect the sensitivity $s _ { a }$ to the self-gravitational energy $\Omega _ { a }$ , defined in $\mathrm { B o x } 6 . 2$ . The gravitational energy is actually proportional to $G _ { \mathrm { l o c a l } }$ . Thus if the total inertial mass of a weak-field, gravitationally bound body is $m = m _ { 0 } + T + G _ { \mathrm { l o c a l } } \Omega + E _ { \mathrm { i n t } } ,$ , where $\tau$ and $E _ { \mathrm { i n t } }$ are the kinetic and internal energies, respectively, then $\Omega = d m / d G _ { \mathrm { l o c a l } }$ . We can then express the sensitivity $s$ for a given body in the form

$$
\begin{array} { l } { { \displaystyle s _ { a } = \left( \frac { d \ln m _ { a } ( \phi ) } { d \ln G _ { \mathrm { l o c a l } } } \right) _ { 0 } \left( \frac { d \ln G _ { \mathrm { l o c a l } } } { d \ln \phi } \right) _ { 0 } , } } \\ { { \displaystyle ~ = - \left( 1 + 2 \lambda \right) \frac { \Omega _ { a } } { m _ { a } } , } } \end{array}
$$

where we used Eq. (10.51), including the fact that $\omega$ also depends on $\phi$ , and used the definition (see Eq. (5.55)),

$$
\lambda \equiv { \frac { \phi _ { 0 } \omega _ { 0 } ^ { \prime } } { ( 3 + 2 \omega _ { 0 } ) ( 4 + 2 \omega _ { 0 } ) } } .
$$

The active mass in the weak field limit is then given by

$$
( m _ { \mathrm { A } } ) _ { a } = m _ { a } \left[ 1 + 2 \zeta ( 1 + 2 \lambda ) \frac { \Omega _ { a } } { m _ { a } } \right] ,
$$

in agreement with Eq. (6.59).

From the complete post-Newtonian solution for $g _ { \mu \nu }$ and $\Psi$ , we can obtain the matter action for the ath body, given by

$$
I _ { a } = - \int m _ { a } ( \phi ) \left( - g _ { 0 0 } - 2 g _ { 0 j } \nu _ { a } ^ { j } - g _ { j k } \nu _ { a } ^ { j } \nu _ { a } ^ { k } \right) ^ { 1 / 2 } d t .
$$

To obtain an $N -$ -body action in the form of Eq. (10.23), we first make the gravitational terms in $I _ { a }$ , manifestly symmetric under interchange of all pairs of particles, then take one of each such term generated in $I _ { a }$ , and sum the result over $a$ . The resulting $N$ -body Lagrangian then has the form of Eq. (10.29) with

$$
\begin{array} { r l } & { \mathcal { G } _ { a b } = 1 - 2 \zeta \left( s _ { a } + s _ { b } - 2 s _ { a } s _ { b } \right) , } \\ & { \mathcal { B } _ { a b } = \cfrac { 1 } { 3 } \left[ \mathcal { G } _ { a b } + 2 ( 1 - \zeta ) \right] , } \\ & { \mathcal { D } _ { a b c } = \mathcal { G } _ { a b } \mathcal { G } _ { a c } + 2 \zeta ( 1 - 2 s _ { b } ) ( 1 - 2 s _ { c } ) \left[ \lambda ( 1 - 2 s _ { a } ) + 2 \zeta s _ { a } ^ { \prime } \right] , } \\ & { \mathcal { A } _ { a } = \mathcal { B } _ { [ a b ] } = \mathcal { C } _ { a b } = \mathcal { E } _ { a b } = 0 . } \end{array}
$$

The quasi-Newtonian equations of motion obtained from the EIH Lagrangian are

$$
{ \pmb a } _ { a } = - \sum _ { b \neq a } \frac { m _ { b } { \pmb x } _ { a b } } { r _ { a b } ^ { 3 } } \left[ 1 - 2 \zeta \left( s _ { a } + s _ { b } - 2 s _ { a } s _ { b } \right) \right] .
$$

For bodies with weak internal fields the product term $s _ { a } s _ { b }$ may be neglected, and the acceleration may be written

$$
{ \pmb a } _ { a } = - \frac { ( m _ { \mathrm { P } } ) _ { a } } { m _ { a } } \sum _ { b \not = a } \frac { ( m _ { \mathrm { A } } ) _ { b } { \pmb x } _ { a b } } { r _ { a b } ^ { 3 } } ,
$$

where $\left( m _ { \mathrm { A } } \right) _ { b }$ is given by Eq. (10.60) and where

$$
( m _ { \mathrm { P } } ) _ { a } = m _ { a } ( 1 - 2 \zeta s _ { a } ) ,
$$

in agreement with our results of Section 6.3, Eq. (6.59). However, if the bodies are sufficiently compact that $s _ { a } ~ \sim ~ s _ { b } ~ \sim ~ 1$ , then because of the product term $s _ { a } s _ { b }$ , it is impossible to describe the quasi-Newtonian equations simply in terms of active and passive masses of individual bodies.

Mirshekari and Will (2013) extended this analysis to higher post-Newtonian orders, obtaining the equations of motion for compact binary systems through $2 . 5 \mathrm { P N }$ order. At 1PN order, the equations have the form

$$
\frac { d ^ { 2 } { \bf x } } { d t ^ { 2 } } = - \frac { \mathcal { G } m } { r ^ { 2 } } \left[ { \pmb n } \left( 1 - A _ { \mathrm { P N } } \right) - \dot { r } \pmb { \nu } B _ { \mathrm { P N } } \right] ,
$$

where

$$
\begin{array} { l } { { A _ { \mathrm { P N } } = - \displaystyle ( 1 + 3 \eta + \bar { \gamma } ) \nu ^ { 2 } + \frac { 3 } { 2 } \eta \dot { r } ^ { 2 } + 2 ( 2 + \eta + \bar { \gamma } + \bar { \beta } _ { + } + \Delta \bar { \beta } _ { - } ) \frac { \displaystyle \mathcal { G } m } { r } , } } \\ { { B _ { \mathrm { P N } } = 2 ( 2 - \eta + \bar { \gamma } ) , } } \end{array}
$$

where the coefficients $\bar { \gamma }$ , $\bar { \beta } _ { + }$ , and $\bar { \beta } _ { - }$ are defined by

$$
\begin{array} { r c l } { { } } & { { } } & { { \bar { \gamma } \equiv - 2 { \mathcal G } ^ { - 1 } \zeta ( 1 - 2 s _ { 1 } ) ( 1 - 2 s _ { 2 } ) , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \bar { \beta } _ { \pm } \equiv \displaystyle \frac { 1 } { 2 } \left( \bar { \beta } _ { 1 } \pm \bar { \beta } _ { 2 } \right) , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \bar { \beta } _ { 1 } \equiv { \mathcal G } ^ { - 2 } \zeta ( 1 - 2 s _ { 2 } ) ^ { 2 } \left[ \lambda ( 1 - 2 s _ { 1 } ) + 2 \zeta s _ { 1 } ^ { \prime } \right] , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \bar { \beta } _ { 2 } \equiv { \mathcal G } ^ { - 2 } \zeta ( 1 - 2 s _ { 1 } ) ^ { 2 } \left[ \lambda ( 1 - 2 s _ { 2 } ) + 2 \zeta s _ { 2 } ^ { \prime } \right] . } } \end{array}
$$

Roughly speaking, the sensitivity $s \sim$ [self-gravitational binding energy]/[mass], so $s _ { \oplus } \sim 1 0 ^ { - 1 0 }$ , $s _ { \odot } \sim 1 0 ^ { - 6 }$ , $s _ { \mathrm { w h i t e \ d w a r f } } \sim 1 0 ^ { - 4 }$ . For neutron stars, whose equation of state is of the form $p = p ( \rho )$ , a model is uniquely determined (for a given function $\omega ( \phi ) .$ ) by the local value of $\phi _ { 0 }$ (or $G _ { \mathrm { l o c a l , } }$ ) and by the central density $\rho _ { c }$ , in other words $m = m ( G , \rho _ { c } )$ and $N = N ( G , \rho _ { c } )$ , where $N$ is the total baryon number. The sensitivity can be expressed in terms of $G$ as

$$
s _ { \mathrm { N S } } = - ( 1 + 2 \lambda ) \left( \frac { \partial \ln m } { \partial \ln G } \right) _ { N } .
$$

However, in any theory of gravity in which the local gravitational structure depends upon a single external parameter whose role is that of a gravitational “constant,” it can be shown that

$$
\left( \frac { \partial \ln m } { \partial \ln G } \right) _ { N } = - \left( \frac { \partial \ln m } { \partial \ln G } \right) _ { \rho _ { c } } + \left( \frac { \partial \ln m } { \partial \ln N } \right) _ { G } \left( \frac { \partial \ln N } { \partial \ln G } \right) _ { \rho _ { c } } .
$$

For fixed central density and fixed equation of state, a simple scaling argument reveals that $m$ and $N$ scale as $G ^ { - 3 / 2 }$ , so that

$$
s _ { \mathrm { N S } } = \frac { 3 } { 2 } ( 1 + 2 \lambda ) \left[ 1 - \left( \frac { \partial \ln m } { \partial \ln N } \right) _ { G } \right] .
$$

Note that $( \partial m / \partial N ) _ { G }$ is the injection energy per baryon.

For the special case of Brans-Dicke theory, Salmona (1967) showed that neutron star models differed very little from their general relativistic counterparts, for values of $\omega$ as small as 2.5. Using general relativistic neutron star models Eardley (1975) obtained sensitivities ranging from 0.07 to 0.39 for masses ranging from $0 . 5 M _ { \odot }$ to $1 . 4 1 M _ { \odot }$ (the maximum mass for the 1975-era equation of state used). Zaglauer (1992) obtained sensitivities for neutron stars with masses between about $1 . 1 M _ { \odot }$ and $1 . 4 6 M _ { \odot }$ for the B, O and M equations of state tabulated by Arnett and Bowers (1977). The sensitivities ranged from 0.19 to 0.30 for the soft B equation of state, and from 0.08 to 0.12 for the stiff M equation of state.

Similar results hold for general scalar-tensor theories with $\omega _ { 0 } ^ { \prime }$ positive (corresponding to positive values of the Damour-Esposito-Farese parameter \` $\beta _ { 0 }$ ). However, when $\omega _ { 0 } ^ { \prime }$ is sufficiently negative (corresponding to $\beta _ { 0 } ~ < ~ - 4 )$ , spontaneous scalarization can occur, leading to neutron star models whose structure is very different from those in general relativity, with dramatically different values of the sensitivities (Damour and Esposito-Farese, 1993, 1996). In the DEF approach (see Section 5.3), the relevant parameter is \` $\alpha ^ { 2 } \sim ( 1 - 2 s ) / ( 4 + 2 \omega _ { 0 } )$ . For example, for a theory corresponding to a value $\beta _ { 0 } = - 6$ , with asymptotic conditions on the theory chosen to agree with the 1993 solar-system bound of $\omega _ { 0 } ~ > ~ 1 5 0 0$ , they found $\alpha ^ { 2 } \sim 0 . 4$ , corresponding to $s \ \sim \ - 6 0 0 !$ As we will see in Chapter 12, binary pulsar observations make it possible to place very tight bounds on this regime of scalar-tensor theories.

For black holes, we found in Section 10.2 that the scalar field is constant in the exterior of the black hole. Thus from Eq. (10.59) we must have $s _ { \mathrm { B H } } = 1 / 2$ . Another way to see this is to note that, because all information about the matter that formed the black hole has vanished behind the event horizon, the only scale on which the mass of the hole can depend is the Planck scale, $m _ { \mathrm { P l a n c k } } = ( \hbar c / G ) ^ { 1 / 2 }$ , and thus $m _ { \mathrm { B H } } \propto m _ { \mathrm { P l a n c k } } \propto G ^ { - 1 / 2 } \propto \phi ^ { 1 / 2 }$ , and hence $s _ { \mathrm { B H } } ~ = ~ 1 / 2$ . Substituting $s _ { a } = s _ { b } = s _ { c } = 1 / 2$ in Eqs. (10.65), we obtain $\mathcal { G } _ { a b } = B _ { a b } = 1 - \zeta$ and $\mathcal { D } _ { a b c } = ( 1 - \zeta ) ^ { 2 }$ . Then it is straightforward to see that if we replace each mass in the Lagrangian (10.29) by $m / ( 1 - \zeta ) = m ( 4 + 2 \omega _ { 0 } ) / ( 3 + 2 \omega _ { 0 } )$ , then apart from a meaningless overall mutiplicative factor of $( 1 - \zeta ) ^ { - 1 }$ , the Lagrangian is identical to that for general relativity. Since black-hole masses cannot be measured by any means other than via their orbital dynamics, this implies that, at 1PN order, the motion of a system of black holes in scalar-tensor theory is indistinguishable from the motion in general relativity. In fact, Mirshekari and Will (2013) showed that this is valid through $2 . 5 \mathrm { P N }$ order.

For binary systems containing one black hole, the equations are again identical to those of general relativity through 1PN order. However, at $1 . 5 \mathrm { P N }$ order (where dipole radiation reaction begins) and beyond, the equations differ from those of general relativity by terms that depend on the single parameter $Q = \zeta ( 1 - \zeta ) ^ { - 1 } ( 1 - 2 s _ { 1 } ) ^ { 2 }$ , where $s _ { 1 }$ is the sensitivity of the companion to the black hole (see Mirshekari and Will (2013) for details).

# 10.3.3 Constrained vector-tensor theories

Because the norm of the vector field in Einstein-Æther and Khronometric theories is constrained to be $^ { - 1 }$ , the structure of a spherically symmetric compact body at rest with rest to the preferred rest frame does not depend on it. However it could depend on the time component $K ^ { 0 }$ , or more properly on the invariant quantity $\pmb { K } \cdot \pmb { u }$ , where $\pmb { u }$ is the body’s four-velocity. (The structure of a rotating body could also depend on the projection of $\pmb { K }$ along the body’s spin axis, but here we will focus on non-rotating bodies.) We define for a body with four-velocity $\pmb { u }$ ,

$$
\gamma \equiv - K ^ { \mu } u _ { \mu } \equiv 1 + \Psi ,
$$

where we assume that far from the system, for a test body at rest, $\pmb { K } \cdot \pmb { u } = - 1$ . We define the sensitivities

$$
\begin{array} { l } { { s _ { a } \equiv \left( \displaystyle \frac { d \ln m _ { a } ( \gamma ) } { d \ln \gamma } \right) _ { \gamma = 1 } , } } \\ { { s _ { a } ^ { \prime } \equiv \left( \displaystyle \frac { d ^ { 2 } \ln m _ { a } ( \gamma ) } { d ( \ln \gamma ) ^ { 2 } } \right) _ { \gamma = 1 } , } } \end{array}
$$

where the derivatives are to be taken holding baryon number fixed. Then in terms of $\Psi$ , we can expand

$$
m _ { a } ( \gamma ) = m _ { a } \left[ 1 + s _ { a } \Psi + \frac { 1 } { 2 } \left( s _ { a } ^ { 2 } + s _ { a } ^ { \prime } - s _ { a } \right) \Psi ^ { 2 } + O ( \Psi ^ { 3 } ) \right] .
$$

With this assumption, Foster (2007) and Yagi et al. (2014a) derived the metric and equations of motion to post-Newtonian order for systems of compact bodies in Einstein-Æther theory. The metric is given by

$$
\begin{array} { l } { { g _ { 0 0 } = - 1 + 2 U - 2 U ^ { 2 } - 2 \Phi _ { 2 } + 3 \Phi _ { 1 s } + O ( \epsilon ^ { 3 } ) , } } \\ { { g _ { 0 j } = g ^ { j } + O ( \epsilon ^ { 5 / 2 } ) , } } \\ { { g _ { j k } = ( 1 + 2 U ) \delta _ { j k } + O ( \epsilon ^ { 2 } ) , } } \end{array}
$$

and the vector field is given by

$$
\begin{array} { l } { { { \cal K } ^ { 0 } = ( - g _ { 0 0 } ) ^ { - 1 / 2 } + { \cal O } ( \epsilon ^ { 3 } ) , } } \\ { { { \cal K } ^ { j } = k ^ { j } + { \cal O } ( \epsilon ^ { 5 / 2 } ) , } } \end{array}
$$

where

$$
\begin{array} { l } { { \displaystyle U = \sum _ { b } \frac { G _ { N } m _ { b } } { r _ { b } } , \quad \Phi _ { 2 } = \sum _ { b , c } \frac { G _ { N } ^ { 2 } m _ { b } m _ { c } } { r _ { b } r _ { b c } } , \quad \Phi _ { 1 s } = \sum _ { b } \frac { G _ { N } m _ { b } } { r _ { b } } \nu _ { b } ^ { 2 } ( 1 - s _ { b } ) , } } \\ { { \displaystyle g ^ { j } = \sum _ { b } \frac { G _ { N } m _ { b } } { r _ { b } } \left[ B _ { b } ^ { - } \nu _ { b } ^ { j } + B _ { b } ^ { + } n _ { b } ^ { j } ( n _ { b } \cdot \nu _ { b } ) \right] , } } \end{array}
$$

$$
k ^ { j } = \sum _ { b } \frac { G _ { N } m _ { b } } { r _ { b } } \left[ C _ { b } ^ { - } \nu _ { b } ^ { j } + C _ { b } ^ { + } n _ { b } ^ { j } ( \pmb { n } _ { b } \cdot \pmb { \nu } _ { b } ) \right] ,
$$

where $G _ { N } = 2 G / ( 2 - c _ { 1 4 } )$ and $c _ { 1 4 } = c _ { 1 } + c _ { 4 }$ . The quantities $B _ { b } ^ { \pm }$ and $C _ { b } ^ { \pm }$ are complicated expressions involving the constants $c _ { 1 } , c _ { 2 } , c _ { 3 }$ , and $c _ { 4 }$ of Einstein-Æther theory and the sensitivities $s _ { b }$ (see Eqs. (23) and (29) of Foster (2007)).

From Eqs. (10.78) and (10.79), we obtain

$$
\Psi ( { \pmb x } _ { a } ) = \frac { 1 } { 2 } \nu _ { a } ^ { 2 } + \frac { 3 } { 8 } \nu _ { a } ^ { 4 } + 2 \nu _ { a } ^ { 2 } U ( { \pmb x } _ { a } ) - \nu _ { a } ^ { j } k ^ { j } ( { \pmb x } _ { a } ) + O ( \epsilon ^ { 3 } ) .
$$

Note that, when $\nu _ { a } ^ { j } = 0$ , $\Psi = 0$ , resulting in no dependence of the inertial mass on the vector field. Writing the action for the ath body as

$$
I _ { a } = - \int m _ { a } ( \Psi ) \left( - g _ { 0 0 } - 2 g _ { 0 j } \nu _ { a } ^ { j } - g _ { j k } \nu _ { a } ^ { j } \nu _ { a } ^ { k } \right) ^ { 1 / 2 } d t ,
$$

we expand to post-Newtonian order, make the action manifestly symmetric under interchange of all pairs of particles, select one of each term, and sum over $a$ . After rescaling each mass by $m _ { a } \to m _ { a } / ( 1 - s _ { a } )$ and replacing the constant term in the Lagrangian by the sum of the rescaled masses, we obtain the modified EIH Lagrangian in the form of Eq. (10.29), with

$$
\begin{array} { r l } & { { { \mathcal G } _ { a b } } = \displaystyle \frac { G _ { N } } { ( 1 - s _ { a } ) ( 1 - s _ { b } ) } \ : , } \\ & { \displaystyle B _ { a b } = { { \mathcal G } _ { a b } } ( 1 - s _ { a } ) \ : , } \\ & { \displaystyle D _ { a b c } = { { \mathcal G } _ { a b } } { { \mathcal G } _ { a c } } ( 1 - s _ { a } ) \ : , } \\ & { \displaystyle A _ { a } = s _ { a } - \frac { s _ { a } ^ { \prime } } { 1 - s _ { a } } \ : , } \\ & { { { \mathcal C } _ { a b } } = { { \mathcal G } _ { a b } } \left[ { \alpha _ { 1 } } - { \alpha _ { 2 } } + 3 \left( { s _ { a } } + { s _ { b } } \right) - { { \mathcal Q } _ { a b } } - { { \mathcal R } _ { a b } } \right] \ : , } \\ & { { { \mathcal E } _ { a b } } = { { \mathcal G } _ { a b } } \left[ { \alpha _ { 2 } } + { { \mathcal Q } _ { a b } } - { { \mathcal R } _ { a b } } \right] \ : , } \end{array}
$$

where

$$
\begin{array} { l } { { \displaystyle { \mathcal { Q } } _ { a b } = \frac { 1 } { 2 } \left( \frac { 2 - c _ { 1 4 } } { 2 c _ { + } - c _ { 1 4 } } \right) ( \alpha _ { 1 } - 2 \alpha _ { 2 } ) ( s _ { a } + s _ { b } ) + \frac { 2 - c _ { 1 4 } } { c _ { 1 2 3 } } s _ { a } s _ { b } , } } \\ { { \displaystyle { \mathcal { R } } _ { a b } = \frac { 8 + \alpha _ { 1 } } { 4 c _ { 1 } } \left[ c _ { - } ( s _ { a } + s _ { b } ) + ( 1 - c _ { - } ) s _ { a } s _ { b } \right] . } } \end{array}
$$

Here $\alpha _ { 1 }$ and $\alpha _ { 2 }$ are the PPN parameters of Einstein-Æther theory, given by Eqs. (5.63), $c _ { \pm } = c _ { 1 } \pm c _ { 3 }$ , and $c _ { 1 2 3 } = c _ { 1 } + c _ { 2 } + c _ { 3 }$ . The two-body equations of motion that follow from the Lagrangian with these coefficients agree with Eq. (33) of Foster (2007) (after correcting a sign and a parenthesis in Eqs. (34) and (35) of that paper).

Note that the Lagrangian is in general not Lorentz invariant, and therefore will exhibit preferred-frame effects. Even when the parameters $c _ { i }$ are constrained so as to enforce $\alpha _ { 1 } =$ $\alpha _ { 2 } = 0$ , making the dynamics Lorentz invariant in the fully weak field post-Newtonian limit, the dynamics of compact bodies will still be dependent on the overall motion of the system via the motion-induced sensitivities of the bodies.

The corresponding equations in Khronometric theory can be obtained from these by setting $c _ { 1 } = - \epsilon$ , $c _ { 2 } = \lambda _ { K }$ , $c _ { 3 } = \beta _ { K } + \epsilon$ , and $c _ { 4 } = \alpha _ { K } + \epsilon$ , and taking the limit $\epsilon  \infty$ (see Yagi et al. (2014a)). The parameters of the modified EIH Lagrangian are given by Eq. (10.83), but now with $G _ { N } = 2 G / ( 2 - \alpha _ { K } )$ , and

$$
\begin{array} { l } { { \displaystyle \mathcal { Q } _ { a b } = \frac { 1 } { \beta _ { K } + \lambda _ { K } } \left[ ( \alpha _ { K } + \beta _ { K } + 3 \lambda _ { K } ) ( s _ { a } + s _ { b } ) + ( 2 - \alpha _ { K } ) s _ { a } s _ { b } \right] , } } \\ { { \displaystyle \mathcal { R } _ { a b } = \frac { 1 } { 2 } ( 8 + \alpha _ { 1 } ) \left[ s _ { a } + s _ { b } - s _ { a } s _ { b } \right] , } } \end{array}
$$

where $\alpha _ { 1 }$ is the PPN parameter of Khronometric theory, given by Eq. (5.68).

Yagi et al. (2014a) calculated neutron star sensitivities in both Einstein-Æther and Khronometric theories. In order to do so, it was necessary to construct models for neutron stars moving uniformly relative to the preferred frame. From Eqs. (10.77) and (10.81), assuming uniform motion with no external bodies ( $U = k ^ { j } = 0$ ), the sensitivity is given by $s = \nu ^ { - 1 } d \ln m / d \nu$ . They chose the coefficients $c _ { 2 }$ and $c _ { 4 }$ so that the PPN parameters $\alpha _ { 1 }$ and $\alpha _ { 2 }$ saturate the bounds from solar-system measurements, and obtained fitting formulae for the sensitivities as a function of $c _ { + }$ , $c _ { - }$ and the compactness $M / R$ of the neutron star.

In this chapter, we develop the tools needed to treat gravitational radiation in general relativity and alternative theories of gravity. This is the “dynamical” regime of relativistic gravity, and since gravitational waves are intimately linked to the motion of masses, we begin (Section 11.1) with a brief history of the “problem of motion and radiation” in general relativity. This history has been at times muddled, at times controversial. We follow this (Section 11.2) with a short account of the status of today’s gravitationalwave detectors. We then turn to the theory of gravitational waves in general relativity and alternative theories, treating their speed (Section 11.3), polarization (Section 11.4) and generation, mainly by binary systems (Section 11.5).

# 11.1 The Problem of Motion and Radiation

At the most primitive level, the problem of motion in general relativity is relatively straightforward, and was an integral part of the theory as proposed by Einstein.1 This is geodesic motion, the motion of a test particle in a fixed spacetime provided by some distribution of matter, for example, that of a spherically symmetric star. The motion of a test particle does not generate gravitational waves, of course. The first attempts to treat the motions of multiple bodies, each with a finite mass and thus each contributing to the spacetime geometry, were made by de Sitter (1916) and Droste (1917) (see also Lorentz and Droste (1917)). They derived the metric and equations of motion for a system of $N$ bodies, in what today would be called the first post-Newtonian approximation of general relativity (de Sitter’s equations turned out to contain some important errors, however).

Einstein (1916, 1918) studied gravitational radiation, using the linearized approximation of his theory to derive the energy emitted by a body such as a rotating rod or dumbbell, held together by nongravitational forces. The first paper was marred by rather egregious errors; the second paper was correct, apart from a trivial numerical error, later spotted and corrected by Eddington (1922). The underlying conclusion that dynamical systems would radiate gravitational waves was correct.

However, there was ongoing confusion over whether gravitational waves are real or are artifacts of general covariance. Although Eddington (1922) clearly elucidated the difference between the physical, coordinate independent modes and modes that were purely coordinate artifacts, he made the unfortunate remark that some gravitational waves propagate “with the speed of thought.” He was referring to the coordinate modes, but the understanding of the role of coordinates at the time was sufficiently poor that the remark cast a pall of doubt over the entire subject.

For example, in 1936, in a paper submitted to The Physical Review, Einstein and Rosen claimed to prove that gravitational waves could not exist. However, the anonymous referee of their paper found that they had made an error. He pointed out that the singularity in their solution that caused them offer their negative conclusion was actually a harmless coordinate singularity. Upset that the journal had sent his paper to a referee (a newly instituted practice), Einstein withdrew the paper and refused to publish in The Physical Review again. Einstein became duly convinced that the referee was right, however, and a corrected paper showing that gravitational waves do exist – cylindrical waves in this case – was published elsewhere (Einstein and Rosen, 1937). Fifty years later it was revealed that the anonymous referee had been H. P. Robertson (Kennefick, 2005).

The next significant advance in the problem of motion came a few years later. In 1938, Einstein, Infeld, and Hoffman published the now legendary EIH paper, a calculation of the $N .$ -body equations of motion using only the vacuum field equations of general relativity (Einstein et al., 1938). They treated each body in the system as a spherically symmetric object whose nearby vacuum exterior geometry approximated that of the Schwarzschild metric of a static spherical star. They then solved the vacuum field equations for the metric between each body in the system in a weak field, slow-motion approximation, equivalent to the post-Newtonian approximation. Then, using a version of what today would be called “matched asymptotic expansions” they showed that, in order for the nearby metric of each body to match smoothly to the interbody metric at each order in the expansion, certain conditions on the motion of each body had to be met. This is essentially the matching procedure described in Chapter 10. Together, these conditions turned out to be equivalent to the Droste–Lorentz $N .$ -body equations of motion. The internal structure of each body was irrelevant, apart from the requirement that its nearby field be approximately spherically symmetric.2

During the 1960s, Fock in the Soviet Union and Chandrasekhar in the United States independently developed and systematized the post-Newtonian approximation in a form that laid the foundation for modern post-Newtonian theory (Fock, 1964; Chandrasekhar, 1965). They developed a full post-Newtonian hydrodynamics, with the ability to treat realistic, self-gravitating bodies of fluid, such as stars and planets. In a suitable limit of “point” particles, or bodies whose size is small enough compared to the interbody separations that finite-size effects such as spin and tidal interactions can be ignored, their equations of motion could be shown to be equivalent to the EIH and the Droste-Lorentz equations of motion.3

Meanwhile, Pirani, Bondi, and others had demonstrated rigorously that gravitational waves were physically real, that they propagate with the speed of light and that they carry energy. At the same time, Joseph Weber began to build detectors for gravitational waves, based on suspended massive cylinders of aluminum that would vibrate in a resonant manner if a gravitational wave of the appropriate frequency passed them. In 1969 and 1970, Weber made the stunning announcement that he had detected gravitational waves, most likely coming from the central regions of the Milky Way. The strength of the signals and rate of the detections were orders of magnitude higher than could be explained by reasonable astrophysical sources, and numerous follow-up investigations by physicists who built their own detectors failed to confirm Weber’s claims. By 1980, a consensus had emerged that Weber had not detected gravitational waves. Despite this negative outcome, Weber’s work had the positive effect of putting gravitational wave theory and detection on the scientific map, and of bringing into the field distinguished experimentalists from other branches of physics, such as Vladimir Braginsky, William Fairbank, Heinz Billing, Edoardo Amaldi, Ronald Drever, and Rainer Weiss. These scientists helped change the field from one dominated by theorists to one characterized by a healthy interplay between theory and experiment. Some of them began to work on a new type of gravitational-wave detection, based on laser interferometry.

The discovery of the binary pulsar in 1974 revealed an inconvenient truth about the “problem of motion,” however. As J¨urgen Ehlers and colleagues pointed out in an influential 1976 paper (Ehlers et al., 1976), the general relativistic theory of motion and radiation, as it was understood at the time, was full of holes large enough to drive trucks through. They pointed out that most treatments of the problem used “delta functions” as a way to approximate the bodies in the system as point masses. As a consequence, the “self-field”, the gravitational field of the body evaluated at its own location, becomes infinite. While this is not a major issue in Newtonian gravity or classical electrodynamics, the non-linear nature of general relativity requires that this infinite self-field contribute to gravity. In the past, such infinities had been simply swept under the rug. Similarly, because gravitational energy itself produces gravity, it thus acts as a source throughout spacetime. This means that, when calculating radiative fields, integrals of the multipole moments of the source that are so useful in treating electromagnetic radiation begin to diverge in the case of gravity. These divergent integrals had also been routinely swept under the rug. Ehlers et al. further pointed out that the true boundary condition for any problem involving radiation by an isolated system should be one of “no incoming radiation” from the past. Connecting this boundary condition with the routine use of retarded solutions of wave equations was not a trivial matter in general relativity. The response of the source to the emitted flux of radiation was usually calculated by assuming that the flux of energy and angular momentum was balanced by an equal loss of those quantities in the motion of the source. While this balance assumption made sense, Ehlers et al. argued that there was no actual proof that it was valid. Finally, they pointed out that there was no evidence that the post-Newtonian approximation, so central to the problem of motion, was a convergent or even asymptotic sequence. Nor had the approximation been carried out to high enough order to make credible error estimates.

During this time, some authors even argued that the “quadrupole formula” for the gravitational energy emitted by a system (see Section 11.5.2), while correct for a rotating dumbbell as calculated by Einstein in the linearized approximation, was actually wrong for a binary system moving under its own gravity. The discovery in 1979 that the rate of decay of the orbit of the binary pulsar was in agreement with the standard quadrupole formula made some of these arguments moot. Yet the question raised by Ehlers et al. was still relevant: Is the quadrupole formula for binary systems an actual prediction of general relativity?

Motivated by the Ehlers et al. critique, numerous workers began to address the holes in the problem of motion, and by the late 1990s most of the criticisms had been answered, particularly those related to divergences. For a detailed history of the ups and downs of the subject of motion and gravitational waves, see Kennefick (2007).

Additional motivation for this theoretical work came in the early 1990s from the experimentalists. By this time, proposals to construct large-scale laser interferometric gravitational wave observatories were well advanced, eventually culminating in the LIGO interferometers in the United States, and Virgo and GEO600 in Europe. A leading candidate source of waves detectable by these devices is the inspiral, driven by gravitational radiation damping, of a binary system of compact objects (neutron stars or black holes) (for a review of sources of gravitational waves, see Sathyaprakash and Schutz (2009)). It was realized that the analysis of signals from such systems would require theoretical predictions from general relativity that are extremely accurate, well beyond the leadingorder prediction of Newtonian or even post-Newtonian gravity for the orbits, and well beyond the leading-order quadrupole formula for gravitational waves (Cutler et al., 1993).

This presented a substantial theoretical challenge: to calculate the motion and radiation of systems of compact objects to very high post-Newtonian order, a formidable algebraic task, while addressing the issues of principle raised by Ehlers et al. sufficiently well to ensure that the results were physically meaningful. This challenge was largely met, and a post-Newtonian description of the inspiral orbit and gravitational wave signal is now in hand, approaching the fourth post-Newtonian (4PN) order beyond the approximation used to account for the binary pulsar (Blanchet, 2014).

Meanwhile another major approach to the problem of motion, known as numerical relativity, finally began to bear fruit. This is the method whereby one solves Einstein’s equations for complex problems, such as the evolution of the orbit of two compact bodies and the gravitational waves emitted, by purely numerical means. The effort began with the pioneering work by Hahn and Lindquist (1964) and Smarr et al. (1976, 1977), focused on the head-on collision of two black holes. Subsequent progress was slow, however, as researchers struggled to find formulations of Einstein’s equations that were better suited to stable numerical analysis, to learn how to treat the coordinate freedom inherent in the theory, and to find schemes to deal with the event horizons of the black holes. Progress was also limited by the available computer speed, power and memory. The first full numerical solution for the head on collision of two nonspinning black holes was achieved in 1993 (Anninos et al., 1993; Matzner et al., 1995). The more complicated problem of two orbiting and inspiralling black holes proved very challenging, until major breakthroughs occurred in 2005, paving the way for rapid progress (Pretorius, 2005; Baker et al., 2006; Campanelli et al., 2006). Baumgarte and Shapiro (2010) provide a pedagogical review of the field.

Today it is common to see published gravitational waveforms from black-hole inspirals and mergers that cover many orbits, that include a range of mass ratios, that incorporate black-hole spins together with the complex precessions of both the spins and the orbital angular momentum, and that give accurate results for the merger of the two black holes and the quasi-normal mode “ringdown” of the final black hole. Remarkably, there is a substantial region of overlap where post-Newtonian theory and numerical relativity are in “unreasonably” good agreement. This has permitted the development of phenomenological approaches that yield accurate analytic formulae that match post-Newtonian theory at early stages in the inspiral, and numerical relativity at the final stage. One of the most prominent of these is the “effective one-body” (EOB) approach, pioneered by Buonanno and Damour (1999). These formulae played a crucial role in the recent detections of gravitational waves by LIGO and Virgo (Abbott et al., 2016b, 2016c, 2017b, 2017c).

At the same time, there has been significant progress in applying numerical relativity to systems containing matter, such as neutron stars. Here one must deal with the uncertainties in the equation of state of nuclear matter, the effects of shock waves and of magnetic fields, and microphysical processes such as radiation and neutrino transport (see Shibata and Taniguchi (2011) and Faber and Rasio (2012) for reviews). These advances became particularly relevant with the 2017 detection of a binary neutron star inspiral and merger by LIGO and Virgo, together with observations of the accompanying electromagnetic signals by numerous observatories on the ground and in space (Abbott et al., 2017d, 2017e).

Needless to say, the “problem of motion” in general relativity looks quite different today than it did in 1974!

# 11.2 Gravitational Wave Detectors

The attempts to detect gravitational waves, from Weber’s pioneering yet flawed experiments to the present international effort involving laser interferometry, pulsar timing, and cosmic microwave background observations, is a story rich in sociology, history, technological development, and big-science politics. That story, and the details of the methods of gravitational-wave detection are beyond the scope of this book. Readers should consult the books by Saulson (1994), Maggiore (2007), and Creighton and Anderson (2011) for those details.

The resonant bar detectors used by Weber and others have been almost completely phased out, in favor of kilometer-scale laser interferometer observatories. The US Laser Interferometer Gravitational-Wave Observatory (LIGO) was constructed between 1994 and 1999, operated between 2002 and 2010 without making any detections, and then after a major upgrade to “advanced LIGO” with higher sensitivity, resumed operations in September 2015. LIGO consists of two interferometers, one in Hanford, Washington, and the other $3 0 0 0 \mathrm { k m }$ away in Livingston, Louisiana, each with arms four kilometers long. The Virgo observatory, operated by a European consortium is in Cascina, Italy, near Pisa, with three-kilometer long arms. It operated between 2003 and 2011, was upgraded, and resumed operation as advanced Virgo in August 2017. A smaller interferometer, GEO600, located in Hannover, Germany, is operated by a German-UK consortium; because its 600-meter arms mean lower sensitivity, GEO600 is today used mainly as a test-bed for advanced technologies for future detectors, for specialized searches for gravitational waves, and as a backup when the other observatories are off-line for maintenance or upgrading. The Kamioka Gravitational-wave detector (KAGRA), an underground three-kilometer interferometer in Japan, is nearing completion. Plans are well advanced for LIGO-India, a four-kilometer interferometer to be located in Maharashtra state, using interferometer and laser instrumentation that was built, but not used, in the final advanced LIGO observatory in Hanford. LIGO-India may join the other interferometers around 2024. These groundbased detectors are sensitive to gravitational waves in the frequency band between about $1 0 \mathrm { H z }$ , where seismic and gravity-gradient noise dominate the detector response, and about ${ 5 0 0 } \mathrm { H z }$ , where photon-counting or “shot” noise dominates.

In addition, plans are being developed for the Laser Interferometer Space Antenna (LISA). Consisting of three spacecraft orbiting the Sun in a triangular formation separated from each other by 2.5 million km, LISA will be sensitive primarily to waves in the low frequency band between $1 0 ^ { - 4 }$ and $1 0 ^ { - 1 }$ Hz. Following the success of LISA Pathfinder, a mission designed to test and demonstrate some of the key technologies needed for the ambitious mission (Armano et al., 2016), LISA was formally selected in June 2017 by the European Space Agency for a launch around 2034, with NASA participating as a junior partner.

In its most schematic realization, a laser interferometric gravitational-wave detector works just like the interferometer used by Michelson in the late 1800s to measure the speed of light and search for evidence of an “aether.” The real-life interferometers are much more complex than this, but this simple model is adequate and captures the essential physics.

A laser interferometer consists of a laser source, a beam splitter, and two end mirrors mounted on test masses imagined to be freely moving in spacetime (although in reality they are suspended by thin wires). The arms of the interferometers are taken to be perpendicular to each other, although this is not essential (in LISA they make angles of $6 0 ^ { \circ }$ ). The laser beam is divided in two at the beam splitter, and each beam travels along one arm of the interferometer, reflects off the test mass, and returns to the beam splitter to be recombined with the other beam. The relative phase of the beams determines whether they produce a bright or dark spot when the recombined beam is measured by a photon detector. Since the initial phases at the beam splitter are identical, the phase difference depends on the difference in travel time along the two arms. If a passing gravitational wave induces a displacement $\Delta L$ that changes the relative lengths of the two arms, it will induce a varying interference pattern. The ground-based advanced LIGO and Virgo are sensitive to strains $\Delta L / L$ at the level of $1 0 ^ { - 2 2 }$ at $1 0 0 \mathrm { H z }$ .

In LISA, the multimillion-kilometer long arms make reflection of the laser signal impractical. Instead each spacecraft is equipped with an optical system that records the phase of each incoming and outgoing laser signal referenced to the location of a freely floating test mass inside the spacecraft. By combining the phase information from these six laser links (three in each direction) in a technique known as time-delay interferometry, one can measure the relative displacements of each pair of spacecraft. LISA’s peak strain sensitivity is expected to be of order $1 0 ^ { - 2 1 }$ at about a millihertz frequency (Amaro-Seoane et al., 2012).

The pulsar timing array (PTA) technique is another variant on the interferometry method. Here, an array of very stable millisecond pulsars distributed around the sky provides the analogue of the laser signal. The phases of the pulsed radio signals are measured as they arrive at Earth and monitored over multiyear timescales. Gravitational waves passing through the galaxy will induce phase variations in the pulsar signals that are sufficiently coherent that they can be distinguished from intrinsic pulsar noise, atomic clock noise on Earth and dispersion from the interstellar medium. This technique is sensitive to gravitational waves with frequencies of order the inverse of the multiyear observation time, or in the nanoHertz regime (for a review, see Manchester (2015)).

Finally, gravitational waves of frequencies of the order of the inverse Hubble time can be probed by looking for a specific class of fluctuations (so-called “B-modes”) in the polarization of the cosmic background radiation.

We now turn to a study of gravitational waves in metric theories of gravity.

# 11.3 Speed of Gravitational Waves

The Einstein Equivalence Principle demands that in every local, freely falling frame, the speed of light must be the same – unity, if one works in geometrized units. The speed of propagation of all zero-rest-mass, nongravitational fields must also be the same as that of light. However, EEP demands nothing about the speed of gravitational waves. That speed is determined by the detailed structure of the field equations of each metric theory of gravity. Some theories of gravity predict that weak, short-wavelength gravitational waves propagate with exactly the same speed as light. By weak, we mean that the dimensionless amplitude $h _ { \mu \nu }$ that characterizes the waves is in some sense small compared to the metric of the background spacetime through which the wave propagates. that is,

$$
| h _ { \mu \nu } | / | g _ { \mu \nu } ^ { ( \mathrm { B } ) } | \ll 1 ,
$$

and by short wavelength, we mean that the wavelength $\lambda$ is small compared to the typical radius of curvature $\mathcal { R }$ of the background spacetime, that is,

$$
\left| \lambda / \mathcal { R } \right| \ll 1 .
$$

This is equivalent to the geometrical optics limit, discussed in Chapter 3 for electromagnetic radiation. In the case of general relativity, for example, one can show (see MTW, exercise 35.15) that the gravitational wave vector $\ell$ is tangent to a null geodesic with respect to the “background” spacetime, that is,

$$
\ell ^ { \mu } \ell ^ { \nu } g _ { \mu \nu } ^ { ( \mathrm { B } ) } = 0 , \ell ^ { \nu } \ell ^ { \mu } { } _ { | \nu } = 0 ,
$$

where “|” denotes a covariant derivative with respect to the background metric. In a local, freely falling frame, where $g _ { \mu \nu } ^ { ( \mathrm { B ) } } = \eta _ { \mu \nu }$ , the speed of the radiation is thus the same as that of light. Gravitational radiation propagates along the “light cones” of electromagnetic radiation.

# General relativity

A simple method to derive this result in general relativity, which can then be applied to other metric theories, is to solve the vacuum field equations, linearized about a background metric chosen locally to be the Minkowski metric. Physically, this is tantamount to solving the propagation equations for the radiation in a local Lorentz frame. As long as the wavelength is short compared to the radius of curvature of the background spacetime, this method will yield the same results as a full geometrical-optics computation. Referring to Section 5.2.2, where we defined the potential $h ^ { \alpha \beta }$ in Eq. (5.18), we see that the linearized vacuum field equation (5.19) in harmonic coordinates takes the form

$$
\begin{array} { r } { \boxed { \ d } h ^ { \alpha \beta } = 0 , } \end{array}
$$

where $\sqsubset$ denotes the flat-spacetime d’Alembertian. The plane-wave solutions of this equation are

$$
h ^ { \alpha \beta } = \mathcal { A } ^ { \alpha \beta } e ^ { i \ell _ { \mu } x ^ { \mu } } , \quad \ell _ { \mu } \ell _ { \nu } \eta ^ { \mu \nu } = 0 ,
$$

where $\mathcal { A } ^ { \alpha \beta }$ and $\ell _ { \mu }$ are the constant amplitude tensor and wave vector, respectively. Thus, the electromagnetic and gravitational light cones coincide, that is, the gravitational waves are null.

# Scalar-tensor theories

Here the linearized vacuum field equations in harmonic gauge, Eqs. (5.43) and (5.45), take the form

$$
\begin{array} { r } { \boxed { \ d } \tilde { h } ^ { \alpha \beta } = 0 , \quad \sqcup \phi = 0 . } \end{array}
$$

where $\tilde { h } ^ { \alpha \beta }$ is the potential related to the auxiliary gothic inverse metric by $\widetilde { h } ^ { \alpha \beta } \equiv$ $\eta ^ { \alpha \beta } - \tilde { \mathfrak { g } } ^ { \alpha \beta }$ . Writing $\phi = \phi _ { 0 } ( 1 + \Psi )$ , where $\phi _ { 0 }$ is the asymptotic value of $\phi$ far from the system, we obtain the plane wave solutions

$$
\begin{array} { c } { { { \tilde { h } } ^ { \alpha \beta } = A ^ { \alpha \beta } e ^ { i \ell _ { \mu } x ^ { \mu } } , \quad \ell _ { \mu } \ell _ { \nu } \eta ^ { \mu \nu } = 0 , } } \\ { { \Psi = { \mathcal B } e ^ { i \ell _ { \mu } ^ { \prime } x ^ { \mu } } , \quad \ell _ { \mu } ^ { \prime } \ell _ { \nu } ^ { \prime } \eta ^ { \mu \nu } = 0 , } } \end{array}
$$

where $\boldsymbol { B }$ is a constant amplitude. Recalling that $\tilde { g } _ { \mu \nu } \equiv ( \phi / \phi _ { 0 } ) g _ { \mu \nu }$ , we see that $\tilde { h } ^ { \alpha \beta }$ is related to the gothic metric potential $h ^ { \alpha \beta }$ to linear order by

$$
\tilde { h } ^ { \alpha \beta } = h ^ { \alpha \beta } - \Psi \eta ^ { \alpha \beta } .
$$

Although the tensor and scalar waves do not necessarily have the same wave vector (depending on the source, $\ell _ { \nu }$ need not be the same as $\ell _ { \nu } ^ { \prime }$ ), both types of wave are null.

This will no longer be true if the scalar field has a potential $V ( \phi )$ . If, for example, $V ( \phi ) \sim m ^ { 2 } \phi ^ { 2 }$ , then the scalar field will propagate like a massive field with a speed less than that of light, while the waves of the field $\tilde { h } ^ { \alpha \beta }$ will remain null.

# Vector-tensor and TeVeS theories

In vector-tensor theories the linearized field equations are much more complex than in the scalar-tensor case, with the propagation of linearized metric perturbations being strongly influenced by the background cosmological value of the vector field $\pmb { K }$ . In general there are ten different wave modes (six for the metric, four for the vector field), each with its own characteristic speed and polarization, although various gauge symmetries within a specific theory may reduce this number. For example, in the Einstein-Æther theory (see Section 5.4.1), there are five modes: two pure metric modes (no vector waves), with speed $( 1 - c _ { + } ) ^ { - 1 / 2 }$ , where $c _ { + } = c _ { 1 } + c _ { 3 }$ and three mixed metric-vector modes, with speeds that are complicated functions of the parameters $c _ { 1 } \ldots c _ { 4 }$ of the theory (Jacobson and Mattingly, 2004).

TeVeS theories have the same general vector-tensor structure as the general vector-tensor theories (see Section 5.5), and as a result, they predict the same modes with the same speeds. At linearized order, the scalar modes decouple from the tensor and vector modes, but because of the nature of the interpolating function $\mathcal { F } ( k \ell ^ { 2 } h ^ { \mu \nu } \phi _ { , \mu } \phi _ { , \nu } )$ that appears in the TeVeS action (5.69), the speed of the scalar waves is generally much lower than the speed of light (Sagi, 2010).

# Massive gravity

Many massive gravity theories (Section 5.7) are motivated by a desire to have the metric, linearized about a flat spacetime background, obey a massive vacuum wave equation, of the form

$$
\sqcap h ^ { \alpha \beta } - \left( \frac { m _ { g } } { \hbar } \right) ^ { 2 } h ^ { \alpha \beta } = 0 ,
$$

where $m _ { g }$ is the mass associated with the field. Substituting the ansatz $\begin{array} { r l } { h ^ { \alpha \beta } } & { { } = } \end{array}$ $\mathcal { A } ^ { \alpha \beta } \mathrm { e x p } ( i \ell _ { \mu } x ^ { \mu } )$ , we obtain $\eta _ { \mu \nu } \ell ^ { \mu } \ell ^ { \nu } = - ( m _ { g } / \hbar ) ^ { 2 }$ . With $\ell ^ { 0 } \equiv \omega$ and $\ell ^ { j } \equiv k ^ { j }$ , we obtain the dispersion relation $\omega ^ { 2 } - | \boldsymbol { k } | ^ { 2 } = ( m _ { g } / \hbar ) ^ { 2 }$ . With $E = \hbar \omega$ and $p = \hbar k$ , this is equivalent to $E ^ { 2 } - p ^ { 2 } = m _ { g } ^ { 2 }$ . Then it is straightforward to show that the propagation speed of the wave, $\nu _ { g } \equiv d \omega / d k$ is given by

$$
\nu _ { g } = \left( 1 - \frac { m _ { g } ^ { 2 } } { E ^ { 2 } } \right) ^ { 1 / 2 } = \left( 1 - \frac { \lambda ^ { 2 } } { \lambda _ { g } ^ { 2 } } \right) ^ { 1 / 2 } ,
$$

where $\lambda _ { g } ~ = ~ h / m _ { g }$ is the “graviton” Compton wavelength, and $\lambda$ is the wavelength of the gravitational waves. This wavelength-dependent propagation speed is analogous to the dispersion experience by an electromagnetic wave propagating through a tenuous plasma, a phenomenon well-known to radio astronomers. In Section 12.2.3, we will see how the gravitational-wave signals detected by LIGO in 2015 and 2017 were used to place a bound on the Compton wavelength $\lambda _ { g }$ .

# 11.4 Polarization of Gravitational Waves

# 11.4.1 The $E ( 2 )$ framework

General relativity predicts that weak gravitational radiation has two independent states of polarization, conventionally called the $\cdot + ^ { \dag }$ and “ $\mathbf { \nabla } \times \mathbf { \vec { \mu } } ^ { \mathbf { 5 } }$ modes, or the $+ 2$ and $^ { - 2 }$ helicity states, to use the language of quantum field theory. However, general relativity is probably unique in that prediction; every other known, viable metric theory of gravity predicts more than two polarizations for the generic gravitational wave. In fact, the most general weak gravitational wave that a theory may predict is composed of six modes of polarization, expressible in terms of the six “electric” components of the Riemann tensor $R _ { 0 j 0 k }$ , that govern the driving forces in a detector (Eardley et al., 1973a,b).

Consider an observer in a local freely falling frame. In the neighborhood of a chosen fiducial event $\mathcal { P }$ along a world line $\gamma$ , construct a locally Lorentz orthonormal coordinate system $( \tau , \xi ^ { j } )$ with $\tau$ as proper time along the world line and $\mathcal { P }$ as spatial origin (“Fermi normal coordinates”). The metric has the form (PW, section 5.2.5)

$$
\begin{array} { l } { { g _ { 0 0 } = - 1 - R _ { 0 p 0 q } ( \gamma ) \xi ^ { p } \xi ^ { q } + { \cal O } ( \xi ^ { 3 } ) , } } \\ { { \displaystyle g _ { 0 j } = \frac { 2 } { 3 } R _ { j p q 0 } ( \gamma ) \xi ^ { p } \xi ^ { q } + { \cal O } ( \xi ^ { 3 } ) , } } \\ { { \displaystyle g _ { j k } = \delta _ { j k } - \frac { 1 } { 3 } R _ { j p k q } ( \gamma ) \xi ^ { p } \xi ^ { q } + { \cal O } ( \xi ^ { 3 } ) . } } \end{array}
$$

For a test particle with spatial coordinates $\xi ^ { j }$ , momentarily at rest in the frame, the acceleration relative to the origin is

$$
\frac { d ^ { 2 } \xi _ { j } } { d t ^ { 2 } } = \frac { 1 } { 2 } g _ { 0 0 , j } = - R _ { 0 j 0 q } ( \gamma ) \xi ^ { q } .
$$

Note that despite the possible presence of auxiliary gravitational fields in a given metric theory of gravity, the acceleration is sensitive only to the Riemann tensor. This is not necessarily true if the body has self-gravitational energy (Lee, 1974).

Thus, a gravitational wave may be completely described in terms of the Riemann tensor it produces. We characterize a weak, plane, nearly null gravitational wave in any metric theory (Eardley et al., 1973b), as observed in some local Lorentz frame, by a linearized Riemann tensor with components that depend only on a retarded time $\tilde { u }$ , that is,

$$
R _ { \alpha \beta \gamma \delta } \equiv R _ { \alpha \beta \gamma \delta } ( \tilde { u } ) .
$$

The “wave vector” $\tilde { \ell } _ { \mu }$ defined by

$$
\tilde { \ell } _ { \mu } \equiv - \tilde { u } _ { , \mu } ,
$$

is normal to surfaces of constant $\tilde { u }$ and is almost null with respect to the local Lorentz metric, that is,

$$
\eta ^ { \mu \nu } \tilde { \ell } _ { \mu } \tilde { \ell } _ { \nu } \equiv \epsilon , \quad | \epsilon | \ll 1 ,
$$

where $\epsilon$ is related to the difference in speed, as measured in a local Lorentz frame at rest in the universal rest frame, between light and the propagating gravitational wave, that is,

$$
\epsilon = \left( \frac { c } { \nu _ { g } } \right) ^ { 2 } - 1 .
$$

We now wish to analyze the general properties of the Riemann tensor for a weak, plane, nearly null gravitational wave. To do this, it is useful to introduce a locally null basis instead of the local Lorentz frame’s Fermi normal basis $( \tau , \xi ^ { j } )$ . Consider a null plane wave (light, for instance) propagating in the $+ Z$ direction in the local Lorentz frame. The wave is described by functions of retarded time $u$ , where $u = t - Z$ . (we use units in which the locally measured speed of light is unity). A similar wave propagating in the $- Z$ direction would be described by functions of advanced time $\nu$ , where $\nu = t + Z$ . We now define the four-vector fields $\ell \equiv \ell ^ { \mu } e _ { \mu }$ and ${ \pmb n } \equiv n ^ { \mu } { \pmb e } _ { \mu }$ , where

$$
\ell _ { \mu } = - u _ { , \mu } , \quad n _ { \mu } = - \frac { 1 } { 2 } \nu _ { , \mu } .
$$

These vectors are tangent to the propagation directions of the two null plane waves. In the $( \tau , \xi ^ { j } )$ basis they have the form

$$
\ell ^ { \mu } = ( 1 , 0 , 0 , 1 ) , \quad n ^ { \mu } = \frac { 1 } { 2 } ( 1 , 0 , 0 , - 1 ) ,
$$

and are null with respect to $\eta$ , that is, $\ell ^ { \mu } \ell ^ { \nu } \eta _ { \mu \nu } = n ^ { \mu } n ^ { \nu } \eta _ { \mu \nu } = 0$ ; note that $\ell ^ { \mu } n ^ { \nu } \eta _ { \mu \nu } = - 1$ . We also introduce the complex null vectors ${ \pmb m } \equiv m ^ { \mu } { \pmb e } _ { \mu }$ and $\bar { \pmb { m } } \equiv \bar { m } ^ { \mu } \pmb { e } _ { \mu }$ , where the bar denotes complex conjugation, and where

$$
m ^ { \mu } = \frac { 1 } { \sqrt { 2 } } ( 0 , 1 , i , 0 ) , ~ \bar { m } ^ { \mu } = \frac { 1 } { \sqrt { 2 } } ( 0 , 1 , - i , 0 ) .
$$

These vectors are also null, since $m ^ { \mu } m ^ { \nu } \eta _ { \mu \nu } = 0$ , and ${ \bar { m } } ^ { \mu } { \bar { m } } ^ { \nu } \eta _ { \mu \nu } = 0$ ; note that $m ^ { \mu } \bar { m } ^ { \nu } \eta _ { \mu \nu } = 1$ . These orthogonality relations imply that

$$
\eta ^ { \mu \nu } = - 2 \ell ^ { ( \mu } n ^ { \nu ) } + 2 m ^ { ( \mu } { \bar { m } } ^ { \nu ) } .
$$

For the remainder of this section, we will use Roman subscripts (excluding the usual spatial indices $i , j , k )$ to denote components of tensors with respect to the null tetrad basis $\ell , n , m$ , $\bar { m }$ , that is, $P _ { a p b \ldots } \equiv P _ { \alpha \beta \gamma \ldots } a ^ { \alpha } p ^ { \beta } b ^ { \gamma } \ldots , \ldots ,$ where $a , b , c , \ldots$ run over $\ell , n , m$ , and $\bar { m }$ , while $p$ , $q , r , \ldots$ run over only $\ell$ , $\pmb { m }$ , and $\bar { m }$ .

Because the null tetrad $\ell$ , ${ \pmb n } , { \pmb m }$ , and $\bar { m }$ is a complete set of basis vectors, we may expand the gravitational wave vector $\tilde { \ell }$ terms of them. But since the gravitational wave is not exactly null, this expansion will depend in general upon the velocity of the observer’s local frame relative to the universe rest frame. Choose a “preferred” observer, whose frame is at rest in the universe, and let $\tilde { \ell } ^ { \mu }$ in this frame have the form

$$
\tilde { \ell } ^ { \mu } = \ell ^ { \mu } ( 1 + \epsilon _ { \ell } ) + \epsilon _ { n } n ^ { \mu } + \epsilon _ { m } m ^ { \mu } + \bar { \epsilon } _ { m } \bar { m } ^ { \mu } ,
$$

where $\{ \epsilon _ { \ell } , \epsilon _ { n } , \epsilon _ { m } \} \sim O ( \epsilon )$ . However, this observer is free (i) to orient his spatial basis so that the gravitational wave and his null wave are parallel, so that $\tilde { \ell } ^ { j } \propto \ell ^ { j }$ , and (ii) to choose

the frequency of his positively propagating null wave to be equal to that of the gravitational wave, so that $\tilde { \ell } ^ { 0 } = \ell ^ { 0 }$ . This implies that $\epsilon _ { m } = 0$ , $\epsilon _ { \ell } = - \epsilon _ { n } / 2$ , and

$$
\tilde { \ell } ^ { \mu } = \ell ^ { \mu } - \epsilon _ { n } \left( \frac { 1 } { 2 } \ell ^ { \mu } - n ^ { \mu } \right) .
$$

Now, because the Riemann tensor is a function of retarded time $\tilde { u }$ alone, we have that

$$
R _ { \alpha \beta \gamma \delta , \mu } \equiv - \tilde { \ell } _ { \mu } \frac { \partial R _ { \alpha \beta \gamma \delta } } { \partial \tilde { u } } \equiv - \tilde { \ell } _ { \mu } \dot { R } _ { \alpha \beta \gamma \delta } .
$$

This, together with the orthogonality relations among the null tetrad vectors, implies that

$$
\begin{array} { l } { { R _ { \alpha \beta \gamma \delta , \ell } = \epsilon _ { n } \dot { R } _ { \alpha \beta \gamma \delta } , } } \\ { { { } } } \\ { { R _ { \alpha \beta \gamma \delta , n } = \left( 1 - \displaystyle \frac { 1 } { 2 } \epsilon _ { n } \right) \dot { R } _ { \alpha \beta \gamma \delta } , } } \\ { { { } } } \\ { { R _ { \alpha \beta \gamma \delta , m } = 0 . } } \end{array}
$$

The linearized Bianchi identities $R _ { a b [ c d , e ] } = 0$ then yield

$$
R _ { a b p q , n } = O ( \epsilon _ { n } \dot { R } ) ,
$$

which, except for a trivial nonwavelike constant, implies that

$$
R _ { a b p q } = R _ { p q a b } = O ( \epsilon _ { n } R ) .
$$

Thus the only components of the Riemann tensor that are not $O ( \epsilon _ { n } )$ are of the form $R _ { n p n q }$ . There are only six such components, and all other components of the Riemann tensor can be expressed in terms of them. They can be related to particular tetrad components of the irreducible parts of the Riemann tensor known as Newman-Penrose quantities (Newman and Penrose, 1962), specifically the Weyl tensor $\Psi _ { A }$ and the tracefree Ricci tensor $\Phi _ { A B }$ (see MTW section 13.5 for definitions). For our nearly null plane wave in the preferred tetrad, they have the form

$$
\begin{array} { l } { { \Psi _ { 2 } = - \displaystyle \frac { 1 } { 6 } R _ { n \ell n \ell } + { \cal O } \left( \epsilon _ { n } R \right) , } } \\ { { \displaystyle \Psi _ { 3 } = - \displaystyle \frac { 1 } { 2 } R _ { n \ell n \bar { m } } + { \cal O } \left( \epsilon _ { n } R \right) , } } \\ { { \Psi _ { 4 } = - R _ { n \bar { m } n \bar { m } } , } } \\ { { \Phi _ { 2 2 } = - R _ { n m n \bar { m } } , } } \end{array}
$$

( $\Psi _ { 3 }$ and $\Psi _ { 4 }$ are complex). These results are valid for a gravitational wave as detected by the preferred observer. Now, in order to discuss the polarization properties of the waves, we must consider the behavior of these components as observed in local Lorentz frames related to the preferred frame by boosts and rotations. However, we must restrict attention to observers who agree with the preferred observer on the frequency of the gravitational wave and on its direction; such “standard” observers can most readily analyze the intrinsic polarization properties of the waves. The Lorentz frames of these standard observers are related by a subgroup of the group of Lorentz transformations that leave $\tilde { \ell }$ unchanged. The most general such transformation is given by

$$
\begin{array} { r l } & { \ell ^ { \prime } = \left( 1 - \alpha \bar { \alpha } \epsilon _ { n } \right) \ell - \epsilon _ { n } \left( \bar { \alpha } m + \alpha \bar { m } \right) + O ( \epsilon _ { n } ^ { 2 } ) , } \\ & { n ^ { \prime } = \left( 1 - \alpha \bar { \alpha } \epsilon _ { n } \right) \left( n + \alpha \bar { \alpha } \ell + \bar { \alpha } m + \alpha \bar { m } \right) + O ( \epsilon _ { n } ^ { 2 } ) , } \\ & { m ^ { \prime } = \left( 1 - \alpha \bar { \alpha } \epsilon _ { n } \right) e ^ { \mathrm { i } \phi } \left( m + \alpha \ell \right) - \epsilon _ { n } \alpha e ^ { \mathrm { i } \phi } \left( n + \alpha \bar { m } \right) + O ( \epsilon _ { n } ^ { 2 } ) , } \\ & { \bar { m } ^ { \prime } = \left( 1 - \alpha \bar { \alpha } \epsilon _ { n } \right) e ^ { - \mathrm { i } \phi } \left( \bar { m } + \bar { \alpha } \ell \right) - \epsilon _ { n } \bar { \alpha } e ^ { - \mathrm { i } \phi } \left( n + \bar { \alpha } m \right) + O ( \epsilon _ { n } ^ { 2 } ) , } \end{array}
$$

where $\alpha$ is a complex number that produces null rotations (combinations of boosts and rotations) and $\phi$ is an arbitrary real phase $0 \leq \phi \leq 2 \pi$ ) that produces a rotation about $e _ { Z }$ . The parameter $\alpha$ is arbitrary except for the restriction $\alpha \bar { \alpha } \ll \epsilon _ { n } ^ { - 1 }$ . This expresses the fact that our results are valid as long as the velocity $w$ of the frame is not too close to the speed either of light or of the gravitational wave, whichever is less; note that for nearly null waves $\epsilon _ { n } ^ { - 1 } \gg 1$ , and almost any velocity that is not infinitesimally close to unity is permitted, since $\alpha \bar { \alpha } \sim w ^ { 2 } / ( 1 - w ^ { 2 } )$ . For exactly null waves, $\epsilon _ { n } = 0$ and arbitrary velocities $w < 1$ are permitted.

Under this set of transformations, the amplitudes of the gravitational wave change according to

$$
\begin{array} { l } { { \Psi _ { 2 } ^ { \prime } = \Psi _ { 2 } + { \cal O } ( \epsilon _ { n } R ) , } } \\ { { \Psi _ { 3 } ^ { \prime } = e ^ { - \mathrm { i } \phi } \left( \Psi _ { 3 } + 3 \bar { \alpha } \Psi _ { 2 } \right) + { \cal O } ( \epsilon _ { n } R ) , } } \\ { { \Psi _ { 4 } ^ { \prime } = e ^ { - 2 \mathrm { i } \phi } \left( \Psi _ { 4 } + 4 \bar { \alpha } \Psi _ { 3 } + 6 \bar { \alpha } ^ { 2 } \Psi _ { 2 } \right) + { \cal O } ( \epsilon _ { n } R ) , } } \\ { { \Phi _ { 2 2 } ^ { \prime } = \Phi _ { 2 2 } + 2 \alpha \Psi _ { 3 } + 2 \bar { \alpha } \bar { \Psi } _ { 3 } + 6 \alpha \bar { \alpha } \Psi _ { 2 } + { \cal O } ( \epsilon _ { n } R ) . } } \end{array}
$$

Consider a set of observers related to each other by pure rotations about the direction of propagation of the wave $\mathit { \Pi } _ { \mathcal { ( } \alpha \mathrm { ~ = ~ } 0 }$ ). A quantity that transforms under rotations by a multiplicative factor $e ^ { \mathrm { i } s \phi }$ is said to have helicity $s$ as seen by these observers. Thus, ignoring the correction terms of $O ( \epsilon _ { n } R )$ , we see that the amplitudes $\Psi _ { 2 }$ ${ } _ { 2 } , \ \Psi _ { 3 } , \ \Psi$ and $\Phi _ { 2 2 }$ have helicities

$$
\begin{array} { l l l } { { \Psi _ { 2 } : } } & { { s = 0 , } } & { { \Phi _ { 2 2 } : \mathrm {  ~ \sigma ~ } s = 0 , } } \\ { { \Psi _ { 3 } : } } & { { s = - 1 , } } & { { \bar { \Psi } _ { 3 } : \mathrm {  ~ \sigma ~ } s = + 1 , } } \\ { { \Psi _ { 4 } : } } & { { s = - 2 , } } & { { \bar { \Psi } _ { 4 } : \mathrm {  ~ \sigma ~ } s = + 2 . } } \end{array}
$$

However, these amplitudes are not observer-independent quantities, as can be seen from Eq. (11.29). For example, if in one frame $\Psi _ { 4 } \neq 0$ but $\Psi _ { 2 } \neq 0$ , then there exists a frame in which $\Psi _ { 4 } ^ { \prime } = 0$ . Thus, the presence or absence of the components of various helicities depends upon the frame. Nevertheless, certain frame-invariant statements can be made about the amplitudes, within the small corrections of $O ( \epsilon _ { n } R )$ . These statements comprise a set of quasi-Lorentz invariant classes of gravitational waves. Each class is labeled by the Petrov type of its nonvanishing Weyl tensor and the maximum number of nonvanishing amplitudes as seen by any observer. These labels are independent of observer. For exactly null waves ${ { \epsilon } _ { n } } = 0$ ), the classes are:

• Class $I I _ { 6 }$ : $\Psi _ { 2 } \neq 0$ . All standard observers measure the same value for $\Psi _ { 2 }$ , but disagree on the presence or absence of all other modes. • Class $I I I _ { 5 }$ : $\Psi _ { 2 } = 0$ , $\Psi _ { 3 } \neq 0$ . All standard observers agree on the absence of $\Psi _ { 2 }$ and on the presence of $\Psi _ { 3 }$ , but disagree on the presence or absence of $\Psi _ { 4 }$ and $\Phi _ { 2 2 }$ .

• Class $N _ { 3 } \colon \Psi _ { 2 } = 0$ , $\Psi _ { 3 } ~ = ~ 0$ , $\Phi _ { 2 2 } \neq 0$ , $\Psi _ { 4 } \neq 0$ . Presence or absence of all modes is observer-independent.

• Class $N _ { 2 }$ : $\Psi _ { 2 } = 0$ , $\Psi _ { 3 } = 0$ , $\Phi _ { 2 2 } = 0$ , $\Psi _ { 4 } \neq 0$ . Independent of observer.   
• Class $O _ { 1 }$ $) _ { 1 } \colon \Psi _ { 2 } = 0$ , $\Psi _ { 3 } = 0$ , $\Phi _ { 2 2 } \neq 0$ , $\Psi _ { 4 } = 0$ . Independent of observer.   
• Class $O _ { 0 }$ : $\Psi _ { 2 } = \Psi _ { 3 } = \Phi _ { 2 2 } = \Psi _ { 4 } = 0$ . Independent of observer: No wave.

For nearly null waves, simply replace the vanishing of modes $( = ~ 0$ ) with the nearly vanishing of modes $[ \simeq \ : O ( \epsilon _ { n } R ) ]$ . This scheme, developed by Eardley et al. (1973b), is known as the $E ( 2 )$ classification for gravitational waves, since in the case of exactly null plane waves $( \epsilon _ { n } = 0$ ), the transformation equations (11.28), are the “little group” $E ( 2 )$ of transformations, a subgroup of the Lorentz group. The $E ( 2 )$ class of a particular metric theory is defined to be the class of its most general wave.

Although we have confined our attention to plane gravitational waves, one can show straightforwardly (Eardley et al., 1973b) that these results also apply to spherical waves far from an isolated source provided one considers the dominant $1 / R$ part of the outgoing waves, where $R$ is the distance from the source.

# 11.4.2 E(2) class of specific metric theories

To determine the $E ( 2 )$ class of a particular theory, it is sufficient to examine the linearized vacuum field equations of the theory in the limit of plane waves (observer far from source of waves). Here we present some examples. Some useful identities that can be obtained from Eqs. (11.20) and (11.26) are

$$
\begin{array} { r } { R _ { n \ell } = R _ { n \ell n \ell } + O ( \epsilon _ { n } R ) , \qquad } \\ { R _ { n n } = 2 R _ { n m n \bar { m } } + O ( \epsilon _ { n } R ) , } \\ { R _ { n m } = R _ { n \ell n m } + O ( \epsilon _ { n } R ) , \qquad } \\ { R = - 2 R _ { n \ell } + O ( \epsilon _ { n } R ) . \qquad } \end{array}
$$

If the Riemann tensor is computed from a linearized metric perturbation $p _ { \mu \nu } ( \tilde { u } )$ , then

$$
\begin{array} { l } { { R _ { \mu \nu \alpha \beta } = \displaystyle \frac { 1 } { 2 } \left( p _ { \mu \beta , \alpha \nu } - p _ { \mu \alpha , \beta \nu } + p _ { \nu \alpha , \beta \mu } - p _ { \nu \beta , \alpha \mu } \right) } } \\ { { = \displaystyle \frac { 1 } { 2 } \left( \tilde { \ell } _ { \alpha } \tilde { \ell } _ { \nu } \ddot { p } _ { \mu \beta } - \tilde { \ell } _ { \beta } \tilde { \ell } _ { \nu } \ddot { p } _ { \mu \alpha } + \tilde { \ell } _ { \beta } \tilde { \ell } _ { \mu } \ddot { p } _ { \nu \alpha } - \tilde { \ell } _ { \alpha } \tilde { \ell } _ { \mu } \ddot { p } _ { \nu \beta } \right) , } } \end{array}
$$

and

$$
\begin{array} { l } { \displaystyle \Psi _ { 2 } = \frac 1 { 1 2 } \ddot { p } \varepsilon \ d + O \left( \epsilon _ { n } R \right) , } \\ { \displaystyle \Psi _ { 3 } = \frac 1 4 \ddot { p } \varepsilon \dot { m } + O \left( \epsilon _ { n } R \right) , } \\ { \displaystyle \Psi _ { 4 } = \frac 1 2 \ddot { p } \frac { } { m \bar { m } } + O \left( \epsilon _ { n } R \right) , } \\ { \displaystyle \Phi _ { 2 2 } = \frac 1 2 \ddot { p } _ { m \bar { m } } + O \left( \epsilon _ { n } R \right) . } \end{array}
$$

# General relativity

The vacuum field equations are $R _ { \mu \nu } = 0$ . The waves are null $( \epsilon _ { n } = 0$ ). Eq. (11.31) then implies that

$$
R _ { n \ell n \ell } = R _ { n m n \bar { m } } = R _ { n \ell n m } = 0 ,
$$

and thus that

$$
\Psi _ { 2 } = \Psi _ { 3 } = \Phi _ { 2 2 } = 0 .
$$

The only unconstrained mode is $\Psi _ { 4 } \neq 0$ , so general relativity is of $E ( 2 )$ class $N _ { 2 }$ . There are only two polarization modes, of helicity $\pm 2$ .

# Scalar-tensor theories

In the massless scalar case, the linearized vacuum field equations (5.35a) and (5.35b) take the form

$$
\begin{array} { c } { { \displaystyle \sqcup _ { \eta } \phi = 0 , } } \\ { { { } } } \\ { { R _ { \mu \nu } - \displaystyle \frac { 1 } { 2 } \eta _ { \mu \nu } R = \displaystyle \frac { 1 } { \phi _ { 0 } } \left( \phi _ { , \mu \nu } - \eta _ { \mu \nu } \Pi _ { \eta } \phi \right) , } } \\ { { { } } } \\ { { R = { \cal O } ( { \phi _ { , \mu } } ^ { 2 } ) , } } \end{array}
$$

where $\phi _ { 0 }$ is the cosmological boundary value of the scalar field $\phi$ . The solution to the first of Eqs. (11.36) for a plane wave is

$$
\phi = \phi _ { 0 } B e ^ { i \ell _ { \mu } x ^ { \mu } } ,
$$

where $\eta _ { \mu \nu } \ell ^ { \mu } \ell ^ { \nu } = 0$ . Then from the remaining two of Eq. (11.36),

$$
R _ { \mu \nu } = - B e ^ { i \ell _ { \mu } x ^ { \mu } } \ell _ { \mu } \ell _ { \nu } .
$$

Thus $R _ { n \ell } = R _ { n m } = 0$ , but $R _ { n n } \neq 0$ , thus

$$
\Psi _ { 2 } = \Psi _ { 3 } = 0 , \quad \Phi _ { 2 2 } \neq 0 , \Psi _ { 4 } \neq 0 ,
$$

and scalar-tensor theories are of class $N _ { 3 }$

# Einstein-Æther theory

Depending on how the source excites waves in the vector field, there are three different modes of gravitational wave in Einstein-Æther theory (Jacobson and Mattingly, 2004). In one mode, the vector field is unexcited, leaving a pure gravity mode of class $N _ { 2 }$ ( $\Psi _ { 2 } =$ $\Psi _ { 3 } = \Phi _ { 2 2 } = 0 $ ) exactly as in general relativity. A second mode has tranverse excitations of the vector field, producing gravitational waves of class $I I I _ { 5 }$ $\Psi _ { 2 } = 0$ ). The third mode has longitudinal excitations of the vector field, producing waves of the most general class, $I I _ { 6 }$ . Each mode has a different gravitational wave speed. The modes and their speeds are summarized in Table 11.1.

<table><tr><td colspan="3">Table11.1 Gravitational-wave polarizationsand speeds in Einstein-Ather theory</td></tr><tr><td>Mode</td><td>v and small ci limit</td><td>E(2) class</td></tr><tr><td>Pure metric</td><td>1 →1 1-c13 2c1-c²+c²</td><td>N2</td></tr><tr><td>Transverse vector</td><td>2c14(1-c13) 𝐶14 2-C14</td><td>II15 C123</td></tr><tr><td>Longitudinal vector</td><td>𝐶123 C14 2(1+c2)²-c123(1+c2+C123) →</td><td>16 c14</td></tr></table>

# 11.4.3 Measurement of gravitational-wave polarizations

Consider an idealized experiment in which an observer uses an array of devices to determine via Eq. (11.12) the six components $R _ { 0 j 0 k }$ of the Riemann tensor for an incident wave. These are generally referred to as the “electric” components, by analogy with the electric field components $F ^ { 0 j }$ of the electromagnetic field tensor. Let us suppose that the waves come from a single localized source with spatial wave vector $\pmb { k }$ chosen to be in the $Z$ direction. Basis vectors $e _ { X }$ and $e _ { Y }$ are chosen to be perpendicular to the $Z$ direction, and therefore to lie in the plane of the sky, with the orientation chosen to reflect some characteristic of the source (for example, the line of the ascending node of an orbit inclined with respect to the plane of the sky). If the observer expresses her data on the displacements $\xi ^ { k }$ as a $3 \times 3$ symmetric matrix, defined by

$$
R _ { 0 j 0 k } \equiv - \frac { 1 } { 2 R } \frac { d ^ { 2 } } { d t ^ { 2 } } A _ { j k } ( t ) ,
$$

where $R$ is the distance to the source, then, to first order in the small displacement $\xi ^ { k }$ Eq. (11.12) gives

$$
\xi ^ { j } ( t ) = \xi ^ { j } ( 0 ) + \frac { 1 } { 2 R } A _ { j k } ( t ) \xi ^ { k } ( 0 ) ,
$$

where $A _ { j k }$ can be written in the form

$$
A _ { j k } = \left( \begin{array} { c c c } { { A _ { + } + A _ { \mathrm { S } } } } & { { A _ { \times } } } & { { A _ { \mathrm { V } 1 } } } \\ { { A _ { \times } } } & { { - A _ { + } + A _ { \mathrm { S } } } } & { { A _ { \mathrm { V } 2 } } } \\ { { A _ { \mathrm { V } 1 } } } & { { A _ { \mathrm { V } 2 } } } & { { A _ { \mathrm { L } } } } \end{array} \right) .
$$

The standard $X Y Z$ orientation of the matrix elements is assumed. From Eqs. (11.18), (11.19), and (11.27), the amplitudes in $A _ { j k }$ are related to the Newman-Penrose quantities by

$$
\begin{array} { l c r } { { \mathrm { R e } \Psi _ { 4 } = \displaystyle \frac { 1 } { 2 R } \ddot { \cal A } _ { + } , } } & { { \mathrm { I m } \Psi _ { 4 } = - \displaystyle \frac { 1 } { 2 R } \ddot { \cal A } _ { \times } , } } \\ { { \mathrm { R e } \Psi _ { 3 } = \displaystyle \frac { 1 } { 4 \sqrt { 2 } R } \ddot { \cal A } _ { \mathrm { V 1 } } , } } & { { \mathrm { I m } \Psi _ { 3 } = - \displaystyle \frac { 1 } { 4 \sqrt { 2 } R } \ddot { \cal A } _ { \mathrm { V 2 } } , } } \\ { { \Phi _ { 2 2 } = \displaystyle \frac { 1 } { 2 R } \ddot { \cal A } _ { \mathrm { S } } , } } & { { \Psi _ { 2 } = \displaystyle \frac { 1 } { 1 2 R } \ddot { \cal A } _ { \mathrm { L } } . } } \end{array}
$$

For each polarization mode, Eq. (11.41) produces a specific distortion of, say, a sphere of freely moving particles, as displayed in Figure 11.1.

![](images/aea02117443d596827433ad4ab6b9fc473365ba7bcbe4321eac1e09ac5e8b929.jpg)  
Displacements induced on a sphere of free particles by each polarization mode of a plane gravitational wave permitted in any metric theory of gravity. The wave propagates in the $+ Z$ direction and has a sinusoidal time dependence. The solid and dashed lines are snapshots at $\omega t = 0$ and $\pi$ , respectively. There are no displacements perpendicular to the plane of the figure. In (a), (b) and (c), the wave propagates out of the page; in (d), (e), and (f ), the wave propagates in the direction of the arrow.

Now, if the observer knows the direction $\pmb { k }$ a priori, either by associating the wave with an electromagnetic counterpart, such as a gamma-ray burst, or by triangulating the direction using the arrival times of signals detected at widely spaced antennas, then by choosing the $Z$ -axis parallel to $\pmb { k }$ , she can determine uniquely the amplitudes as given in Eq. (11.42), and thereby obtain the class of the incident wave. Because a specific source need not emit the most general wave possible, the $E ( 2 )$ class determined by this method would be the least general class permitted by any metric theory of gravity.

![](images/8400785b52421f918bb3e183d830d4ec02f2f4aeedbd4aee8a721ad95e503bea.jpg)  
Fig. 11.2 Relation between the detector basis $( e _ { 1 } , e _ { 2 } , e _ { 3 } )$ and the source basis $( e _ { \boldsymbol { \chi } } , e _ { \boldsymbol { \ Y } } , e _ { Z } = - e _ { 3 } ^ { \prime } )$

However, if the observer does not know the direction a priori, it is not possible to determine the $E ( 2 )$ class uniquely, since there are eight unknowns (six amplitudes and two direction angles) and only six observables $A _ { j k }$ . In particular, any observed $A _ { j k }$ can be fit by an appropriate wave of class $I I _ { 6 }$ and an appropriate direction. However, for certain observed $A _ { j k }$ , the $E ( 2 )$ class may be limited in such a way as to provide a test of gravitational theory. For example, if the driving forces remain in a fixed plane and are pure quadrupole, that is, if there is a fixed coordinate system in which

$$
A _ { j k } = \left( \begin{array} { c c c } { { \lambda } } & { { \mu } } & { { 0 } } \\ { { \mu } } & { { - \lambda } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) ,
$$

then the wave may be either $I I _ { 6 }$ (unknown direction), or $N _ { 2 }$ , (direction parallel to the $z$ -axis of new coordinate system). If this condition is not fulfilled, however, the class cannot be $N _ { 2 }$ . Such a result would be evidence against general relativity. Eardley et al. (1973b) provide a detailed enumeration of other possible outcomes of such idealized polarization measurements.

We must now link this idealized description of the polarization modes to measurements made by realistic gravitational wave detectors, for which the natural basis is defined by the detector, not the source.

For an Earth-bound laser interferometer, the natural basis is one where the directions of the two arms $e _ { 1 }$ and $e _ { 2 }$ define the $x$ and $y$ axes, and $e _ { 3 }$ , perpendicular to the Earth’s surface, defines the $z$ axis (see Figure 11.2). The source direction is then characterized by the polar angles $\theta$ and $\phi$ , and the orientation of the source basis relative to the rotated detector basis (the primed basis in Figure 11.2) is characterized by a phase $\psi$ (note that $\begin{array} { r } { \hat { \pmb { k } } = \pmb { e } _ { Z } = - \pmb { e } _ { 3 } ^ { \prime } } \end{array}$ ).

In addition, the detector response is somewhat more complicated than our ideal measurement, because it involves finding the difference in displacements of two free bodies (suspended mirrors) at the ends of the perpendicular arms of the interferometer. It is straightforward to show (see, e.g., PW, section 11.5) that the phase difference between the two laser beams when they are recombined after travelling along each arm is given by

$$
\Delta \Phi = \frac { 4 \pi \nu L _ { 0 } } { R } S ( t ) ,
$$

where $\nu$ is the laser frequency, $L _ { 0 }$ is the fiducial length of the arms, and the interferometer’s “response function” $S ( t )$ is given by

$$
S ( t ) = \frac { 1 } { 2 } \left( e _ { 1 } ^ { j } e _ { 1 } ^ { k } - e _ { 2 } ^ { j } e _ { 2 } ^ { k } \right) A ^ { j k } ( t ) .
$$

Taking into account the rotations between the detector basis and the source basis that defines $A ^ { j k }$ , we obtain

$$
S ( t ) = F _ { \mathrm { + } } A _ { \mathrm { + } } ^ { \prime } + F _ { \mathrm { \times } } A _ { \mathrm { \times } } ^ { \prime } + F _ { \mathrm { 5 } } A _ { \mathrm { 5 } } + F _ { \mathrm { \nabla 1 } } A _ { \mathrm { V 1 } } ^ { \prime } + F _ { \mathrm { V 2 } } A _ { \mathrm { V 2 } } ^ { \prime } + F _ { \mathrm { L } } A _ { \mathrm { L } } ,
$$

where the “angular pattern functions” $F _ { \mathrm { A } }$ are given by

$$
\begin{array} { r l } & { F _ { + } = \displaystyle \frac { 1 } { 2 } ( 1 + \cos ^ { 2 } \theta ) \cos 2 \phi , } \\ & { F _ { \times } = - \cos \theta \sin 2 \phi , } \\ & { F _ { \mathrm { S } } = - \displaystyle \frac { 1 } { 2 } \sin ^ { 2 } \theta \cos 2 \phi , } \\ & { F _ { \mathrm { V I } } = - \sin \theta \cos \theta \cos 2 \phi , } \\ & { F _ { \mathrm { V 2 } } = \sin \theta \sin 2 \phi , } \\ & { F _ { \mathrm { L } } = \displaystyle \frac { 1 } { 2 } \sin ^ { 2 } \theta \cos 2 \phi , } \end{array}
$$

and where

$$
\begin{array} { r c l } { { } } & { { } } & { { A _ { + } ^ { \prime } \equiv A _ { + } \cos 2 \psi + A _ { \times } \sin 2 \psi , } } \\ { { } } & { { } } & { { A _ { \times } ^ { \prime } \equiv A _ { + } \sin 2 \psi - A _ { \times } \cos 2 \psi , } } \\ { { } } & { { } } & { { A _ { \mathrm { V 1 } } ^ { \prime } \equiv A _ { \mathrm { V 1 } } \cos \psi + A _ { \mathrm { V 2 } } \sin \psi , } } \\ { { } } & { { } } & { { A _ { \mathrm { V 2 } } ^ { \prime } \equiv A _ { \mathrm { V 1 } } \sin \psi - A _ { \mathrm { V 2 } } \cos \psi . } } \end{array}
$$

Notice that the $A _ { A } ^ { \prime }$ amplitudes are simply the original amplitudes in the source basis projected onto the basis vectors $e _ { 1 } ^ { \prime }$ and $e _ { 2 } ^ { \prime }$ , with the factor $2 \psi$ in $A _ { + } ^ { \prime }$ and $A _ { \times } ^ { \prime }$ arising because those modes have helicity 2. Also notice that, since $F _ { \mathrm { S } } = - F _ { \mathrm { L } }$ , measurements using laser interferometers cannot measure the scalar and longitudinal modes separately, but can only measure the difference $A _ { \mathrm { S } } - A _ { \mathrm { L } }$ . If the direction to the source is known, then a suitable array of five interferometers with distinct orientations, leading to five distinct values of $\theta , \phi$ , can in principle measure the five amplitudes $A _ { + } ^ { \prime } , A _ { \times } ^ { \prime } , A _ { \mathrm { V 1 } } ^ { \prime } , A _ { \mathrm { V 2 } } ^ { \prime }$ , and $A _ { \mathrm { S } } - A _ { \mathrm { L } }$ . One can also show that, for an interferometer whose arms make an angle $\chi$ relative to each other, the angular pattern functions of Eqs. (11.48) are simply multiplied by a factor $\sin \chi$ (Cutler, 1998).

One might be tempted to imagine that, when the full network of kilometer-scale interferometers consisting of the two LIGO devices and Virgo, plus KAGRA and LIGO-India are online, such tests of polarization might become routine. However, the arms of the two LIGO interferometers in Hanford and Livingston are actually parallel to each other, apart from a small relative angle of about $2 7 ^ { \circ }$ induced by the curvature of the Earth’s surface and a relative rotation of $9 0 ^ { \circ }$ . As a result, $e _ { 1 } ^ { \mathrm { H } } \approx e _ { 2 } ^ { \mathrm { L } }$ , $e _ { 2 } ^ { \mathrm { H } } \approx - e _ { 1 } ^ { \mathrm { L } }$ , and $S ^ { \mathrm { H } } ( t ) \approx - S ^ { \mathrm { L } } ( t )$ . This alignment is the result of a decision made early in the development of LIGO to forgo any sensitivity to multiple polarizations in favor of the redundancy provided by almost identical responses to any given signal. This decision was validated in the initial detection of GW150914, where one can see by eye in the almost raw data (mildly band-pass filtered to suppress low-frequency and high-frequency noise) that the chirp signals recorded in the Hanford and Livingston detectors are the precise negatives of each other.

Thus to carry out polarization tests, it will be necessary either to add an interferometer to the network, to combine data from sources of similar type (such as binary black hole mergers), or to focus on restricted classes of theories, such as $N _ { 3 } , N _ { 4 }$ or $O _ { 1 }$ . For specific analyses, see Wagoner and Kalligas (1997), Brunetti et al. (1999), Gasperini (1999), Magueijo (2003), Wen and Schutz (2005), and Nishizawa et al. (2009). By combining signals from various interferometers into a kind of “null channel” one can test for the existence of modes beyond the $^ +$ and $\times$ modes in a model-independent manner (Chatziioannou et al., 2012).

The space-based interferometer LISA can also measure polarizations. In this case, because the arm lengths $( \sim 2 \times 1 0 ^ { 6 } \ \mathrm { k m }$ ) may be comparable to or longer than the gravitational wavelength, our analysis based on local Fermi normal coordinates is no longer appropriate. Instead one uses an approach called “time delay interferometry” (TDI) (Armstrong et al., 1999), in which one determines the effect of the gravitational wave on each of the six laser beams propagating between the three spacecraft at the moment of emission and the moment of reception. The result is six “Doppler response functions,” two for each spacecraft. Certain linear combinations of these functions completely suppress the contributions of laser noise, for example. Because the orientation of the spacecraft triangle changes as the constellation orbits the Sun, the response to the incoming gravitational wave varies continuously, permitting both localization of the source and measurement of the polarization modes (Tinto and Alves, 2010; Nishizawa et al., 2010). Gravitational-wave polarization can also be studied using pulsar timing arrays (Lee et al., 2008; Alves and Tinto, 2011; Chamberlin and Siemens, 2012).

# 11.5 Generation of Gravitational Waves

It is common knowledge that general relativity predicts that the lowest multipole emitted in gravitational radiation is quadrupole, in the sense that, if a multipole analysis of the gravitational field in the radiation zone far from an isolated system is performed in terms of tensor spherical harmonics, then only the harmonics with $\ell \geq 2$ are present (see Thorne (1980) for a thorough discussion of multipole-moment formalisms). For material sources, this statement can be reworded in terms of appropriately defined multipole moments of the matter and gravitational-field distribution within the near-zone surrounding the source: the lowest source multipole that generates radiation is quadrupole. For slow-motion, weak-field sources, such as binary star systems, quadrupole radiation is in fact the dominant multipole. The result is a gravitational waveform in the radiation zone given, to leading post-Newtonian order, by

$$
h ^ { j k } ( t ) = \frac { 2 } { R } \ddot { I } ^ { j k } ( \tau ) ,
$$

where $h ^ { j k }$ is defined by Eq. (5.18), $R$ is the distance from the source, $\tau \equiv t - R$ is retarded time, dots denote time derivatives, and $I ^ { j k }$ is the quadrupole moment tensor of the source, given by

$$
I ^ { j k } \equiv \int \rho ^ { * } x ^ { j } x ^ { k } d ^ { 3 } x ,
$$

where $\rho ^ { * }$ is the conserved density. The waveform $h ^ { j k }$ can be related to the measured electric components of the Riemann tensor by Eq. (11.33),

$$
R _ { n \bar { m } n \bar { m } } = - \Psi _ { 4 } = - { \frac { 1 } { 2 } } \ddot { h } _ { \bar { m } \bar { m } } .
$$

The rate of change of energy of the system resulting from the flux of energy carried by the waves to infinity is given by

$$
\frac { d E } { d t } = - \frac { 1 } { 5 } \dddot { I } ^ { \langle j k \rangle } \dddot { I } ^ { \langle j k \rangle } ,
$$

where $I ^ { \langle j k \rangle } \equiv I ^ { j k } - \textstyle { \frac { 1 } { 3 } } \delta ^ { j k } I$ is the tracefree quadrupole moment tensor.

Eqs. (11.50) and (11.53) are collectively referred to as the “quadrupole formulae” for gravitational radiation. It has also become the accepted convention to refer to Eqs. (11.50) and (11.53) as the “Newtonian” waveform and energy flux. Even though Newtonian theory does not admit gravitational radiation because the interactions are considered to be instantaneous, the term “Newtonian” establishes these expressions as the lowest order terms in a post-Newtonian sequence of contributions, according to general relativity. Thus one can talk about $0 . 5 \mathrm { P N } .$ , 1PN, 2PN corrections to these expressions.

For a binary system with total mass $m \ = \ m _ { 1 } + m _ { 2 }$ , reduced mass parameter $\eta =$ $m _ { 1 } m _ { 2 } / m ^ { 2 }$ , orbital separation $r$ and relative velocity $\nu$ , we obtain the waveform

$$
h ^ { j k } = 4 \eta \frac { m } { R } \left( \nu ^ { j } \nu ^ { k } - \frac { m } { r } n ^ { j } n ^ { k } \right) ,
$$

and the energy loss rate

$$
\frac { d E } { d t } = - \frac { 8 } { 1 5 } \eta ^ { 2 } \left( \frac { m } { r } \right) ^ { 4 } \left( 1 2 \nu ^ { 2 } - 1 1 \dot { r } ^ { 2 } \right) ,
$$

where $\dot { \boldsymbol { r } } = d \boldsymbol { r } / d t$ (Peters and Mathews, 1963). This loss of energy results in a decrease of the orbital period $P$ at a rate given, to lowest PN order, by $\dot { P } / P = - \frac { 3 } { 2 } \dot { E } / E$ .

These comments apply to the asymptotic properties of the outgoing radiation field. However, if we are interested in the response of the source itself to the emission of the radiation we must deal with the field within the near zone at a level of approximation that incorporates the effects of gravitational radiation back reaction. A variety of computations in general relativity have yielded a local radiation-reaction force that, in a particular gauge, takes the form

$$
F _ { \mathrm { R e a c t } } ^ { j } = - \frac { 2 } { 5 } \overline { { { I } } } ^ { ( j k ) } x _ { k } ,
$$

where the superscript (5) denotes five time derivatives. In the equations of motion, this represents a correction to Newtonian gravity at $2 . 5 \mathrm { P N }$ order. This leads to a loss of mechanical or orbital energy by the system that agrees with Eq. (11.53).

Quadrupole radiation also leads to a decrease of the orbital angular momentum and to a corresponding decrease of the orbital eccentricity.

Unlike general relativity, however, nearly every alternative metric theory of gravity predicts the presence of lower multipoles – monopole and dipole – in gravitational radiation, in addition to the quadrupole and higher multipole contributions (Eardley, 1975; Will and Eardley, 1977; Will, 1977). At zeroth PN order, the monopole moment is just the total rest mass of the system, which is conserved. Thus two time derivatives of the leading contribution to the monopole moment will vanish. At the first PN order, there are contributions to the monopole moment of order $m \nu ^ { 2 }$ , which is of the same order as two time derivatives of the quadrupole moment, and so these contributions to the monopole moment serve mainly to modify the radiation at quadrupole order. At zeroth PN order, the dipole moment is proportional to the center of rest mass of the system, which at lowest order moves at constant velocity; thus two time derivatives of that quantity will vanish, by virtue of the Newtonian equations of motion. However, post-Newtonian corrections to the dipole moment need not share this property, and thus there could be dipole contributions to the radiation.

By contrast, in general relativity, the monopole moment turns out to be the total mass of the system, which is constant by virtue of the full equations of motion, at least up to the $2 . 5 \mathrm { P N }$ order at which the loss of mass to the flux of gravitational waves must be incorporated. Similarly, the dipole moment turns out to be the full dipole moment, or center of mass of the system, which is a linear function of time by virtue of the full equations of motion, at least up to the order at which the system experiences a recoil due to the emission of linear momentum in gravitational waves. These properties, which are a result of the remarkable adherence of general relativity to the Strong Equivalence Principle, account for the fact that quadrupole radiation leads the multipolar contributions to gravitational waves in general relativity.

In many alternative theories, the most important contribution to dipole radiation comes from a 1PN-order, residual dipole moment of gravitational energy, schematically of the form $\begin{array} { r } { D ^ { j } \sim \int \rho ^ { * } U x ^ { j } d ^ { 3 } x . } \end{array}$ . Focusing on the part of $U$ that is the internal gravitational potential of each body, we can express the dipole moment in the form $\begin{array} { r } { D ^ { j } \sim \sum _ { a } \Omega _ { a } x _ { a } ^ { j } } \end{array}$ , where $\begin{array} { r } { \Omega _ { a } = - \frac { 1 } { 2 } \int _ { a } \rho ^ { * } U d ^ { 3 } x . } \end{array}$ . For a binary system with its center of mass placed at the origin of coordinates, we have to lowest PN order, ${ \pmb x } _ { 1 } = ( m _ { 2 } / m ) { \pmb x }$ and $\pmb { x } _ { 2 } = - ( m _ { 1 } / m ) \pmb { x }$ , and we have that

$$
\boldsymbol { D } ^ { j } \sim \eta \boldsymbol { m } \boldsymbol { S } \boldsymbol { x } ^ { j } ,
$$

where

$$
{ \mathcal { S } } \equiv { \frac { \Omega _ { 1 } } { m _ { 1 } } } - { \frac { \Omega _ { 2 } } { m _ { 2 } } }
$$

is the difference in self-gravitational energy per unit mass between the two bodies. For compact bodies, $\boldsymbol { \mathcal { S } }$ typically is related to the difference $s _ { 1 } - s _ { 2 }$ between the sensitivities of the two bodies, as defined in Section 10.3. This varying dipole moment can thus contribute both to the gravitational waveform and to the fluxes of energy and angular momentum. Furthermore, if the bodies are compact bodies, such as neutron stars, where $\Omega / m$ could be as large as 0.3 or even black holes, where the analogue of $\Omega / m$ could be as large as unity, the contributions of dipole radiation could be larger than expected. In some theories, the flux of energy due to dipole radiation is similar to that in electromagnetism, namely $d E / d t \sim \ddot { D } \cdot \ddot { D } \sim \eta ^ { 2 } ( m / r ) ^ { 4 } S ^ { 2 }$ .

Generalizing the quadrupole energy flux of general relativity, Eq. (11.55) and adding the dipole energy flux, we can write down a parametrized formula for the leading energy loss rate from binary systems in a class of alternative theories, given by

$$
\frac { d E } { d t } = - \eta ^ { 2 } \mathcal { G } ^ { - 1 } \left( \frac { \mathcal { G } m } { r } \right) ^ { 4 } \left[ \frac { 8 } { 1 5 } \left( \kappa _ { 1 } \nu ^ { 2 } - \kappa _ { 2 } \dot { r } ^ { 2 } \right) + \frac { 1 } { 3 } \kappa _ { D } S ^ { 2 } \right] ,
$$

where $\mathcal { G } = \mathcal { G } _ { 1 2 }$ is defined by Eq. (10.29), $\kappa _ { 1 } , \kappa _ { 2 }$ and $\kappa _ { D }$ are parameters that vary from theory to theory. In general relativity, $\mathcal { G } = 1$ , $\kappa _ { 1 } = 1 2$ , $\kappa _ { 2 } = 1 1$ and $\kappa _ { D } = 0$ .

The foregoing remarks are rather broad and qualitative. In the end, one must treat each theory in turn and calculate its gravitational waveform and fluxes of energy, angular momentum and linear momentum to the PN order needed. The next section attempts to provide a “recipe,” largely based on experience with general relativity and scalar-tensor theories, for carrying out such calculations.

# 11.5.1 Calculating gravitational waves in alternative theories

In this section we will outline a general approach for calculating gravitational waves using a formalism developed for general relativity by Epstein and Wagoner (1975) and Wagoner and Will (1976), and extended by Will and Wiseman (1996) and Pati and Will (2000, 2002). This approach is closely related to the “post-Minkowskian” framework of Blanchet, Damour, and Iyer (for a thorough review, see Blanchet (2014)). Another approach, inspired by quantum field theory, is “Effective Field Theory” framework pioneered by Goldberger and Rothstein (2006) (for a review, see Foffa and Sturani (2014)).

We will focus our attention on gravitational waves from $N .$ -body systems (with $N = 2$ being the most important case), assuming that the bodies are small compared to their separations. The two-body case is relevant for binary pulsar observations and for the first detections of gravitational radiation from compact binary inspiral.

Other potential sources of gravitational radiation, such as core collapse in supernovae, spinning deformed neutron stars, collisions of cosmic strings, and cosmological gravitational waves, involve very different assumptions, considerable input from nongravitational physics, and substantial numerical computation; these are beyond the scope of this book.

Because of the complexity of many alternative theories of gravitation beyond the post-Newtonian approximation, it has proven impossible to devise a formalism analogous to the PPN framework for describing gravitational radiation from dynamical sources. But we can provide a general description of the method used to arrive at the gravitational waveform and the energy and angular momentum fluxes within a chosen theory of gravity, emphasizing those features that are common to many currently viable theories, such as those described in Chapter 5. Later, we will treat specific theories. The method proceeds as follows:

Step 1: Select a theory, identify the variables and set the cosmological boundary conditions (follow Steps 1–3 in Section 5.1). Restrict the adjustable constants and cosmological matching parameters to values that give close agreement with solar-system tests.

Step 2: Working in the universal rest frame, expand the metric and any scalar, vector or tensor fields about their asymptotic values:

$$
\begin{array} { c } { { g _ { \mu \nu } = g _ { \mu \nu } ^ { ( 0 ) } + p _ { \mu \nu } , } } \\ { { \phi = \phi _ { 0 } \bigl ( 1 + { \Psi } \bigr ) , } } \\ { { K ^ { \mu } = \bigl ( K + k ^ { 0 } , k ^ { 1 } , k ^ { 2 } , k ^ { 3 } \bigr ) , } } \\ { { B _ { \mu \nu } = B _ { \mu \nu } ^ { ( 0 ) } + b _ { \mu \nu } . } } \end{array}
$$

We assume that the vector field is timelike, so that, in the universal rest frame far from the source, it has only a time component. All current theories with vector fields make this assumption. In theories with fields that single out a preferred rest frame, it may actually be advantageous to transform to the rest frame of the system under study at the beginning of the calculation, rather than at the end, as we did for the post-Newtonian limits of such theories.

Step 3: Derive the “relaxed field equations.” Using any gauge freedom available, express the field equations in the form

$$
\begin{array} { r } { \boxed { \ d } \psi ^ { A } = - 1 6 \pi \tau ^ { A } , } \end{array}
$$

where $\psi ^ { A }$ is one of the fields $p _ { \mu \nu }$ , $\Psi$ , and so on, or possibly a linear combination of fields, and the “source” $\tau ^ { A }$ typically consists of matter and nongravitational field stress-energies, and of “gravitational” stress-energies consisting of terms quadratic and higher in the fields. The operator $\sqsubset$ is given by

$$
\boldsymbol { \Xi } \equiv - \frac { 1 } { \nu _ { g A } ^ { 2 } } \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } + \boldsymbol { \nabla } ^ { 2 } ,
$$

where the wave speed $\nu _ { g A }$ is a function of adjustible constants and matching parameters of the theory, and could be different for different $\psi ^ { A }$ .

Because we will be dealing only with Lagrangian-based metric theories, we know that each theory admits a pseudotensorial object $\tau ^ { \mu \nu }$ that reduces to the matter energymomentum tensor $T ^ { \mu \nu }$ in the absence of gravity, and that satisfies the equation

$$
\tau ^ { \mu \nu } { } _ { , \nu } = 0 ,
$$

(see Lee et al. (1974) and the discussion of Section 4.4). The system of Eqs. (11.61) and (11.63) is sometimes referred to as “relaxed” field equations, because one can solve Eq. (11.61) formally using the Green function for the operator $\sqsubset$ as a functional of the matter variables, without specifying the behavior of the matter (this is the “relaxed” aspect of the procedure). Then one can use Eq. (11.63) to obtain the matter behavior as a function of time and thereby obtain the full solution for the fields of the theory (see PW section 6.2 for further discussion).

# Box 11.1

# Iterating the relaxed field equations

If one assumes that the fields are weak, so that $\psi ^ { A } \ll 1$ , then it is natural to approximate solutions to Eq.   
(11.61) by a process of iteration. First substitute $\psi ^ { A } = 0$ in the right-hand-side of (11.61), so that $\tau ^ { A }$ consists   
of only matter contributions, and obtain the first iterationright-hand side of (11.61), and obtain the second iterated $\psi _ { ( 1 ) } ^ { A }$ substitute those solutions back into the. Continue the process until the desired $\psi _ { ( 2 ) } ^ { A }$   
accuracy is reached.

There is a persistent legend that, in order to obtain the gravitational wave signal and energy flux in general relativity at the leading quadrupole order, one only needs to obtain the first iterated field, which corresponds to linearized theory. While this is correct for the radiation from a source governed internally by nongravitational forces, such as an object in the laboratory, it is incorrect for a self-gravitating source, such as a binary star system. This is because the equations of motion that follow from the first iteration are given by $\tau _ { ( 0 ) , \nu } ^ { \mu \nu } = 0 ,$ , which do not contain gravitational interactions. A second iteration of the fields is required in order to arrive at a solution for gravitationally interacting systems that is compatible with the equations of motion $\tau _ { ( 1 ) , \nu } ^ { \mu \nu } = 0 ,$ which now contain Newtonian gravity at leading order. The fact that the final answer, the so-called “quadrupole formula”(11.50), is formally the same for binary systems as for laboratory sources is both coincidental and misleading. The difference is in the meaning of the two time derivatives: for binary systems, one inserts the Newtonian equation of motion for the acceleration generated by two time derivatives, while for a laboratory system one inserts equations of motion appropriate for a system with only nongravitational interactions, such as a dumbell governed by internal atomic forces. The underlying reason for this formal coincidence is the Strong Equivalence Principle, which asserts that certain behaviors of systems, such as their motion or the waves they generate, are not sensitive to the internal structure of the bodies or systems, so that the leading-order waves generated by either a dumbell or a binary system depend only on the mass quadrupole moment.

This coincidence cannot be expected to hold in alternative theories of gravity, which generically violate SEP. Thus one cannot rely upon the linearized approximation to yield sensible results, but instead must carefully consider the structure of the relaxed field equations (11.61) and (11.63) in the theory and determine the number of iterations required to obtain solutions for the field and the equations of motion that are compatible with each other. For a detailed discussion within general relativity of this iteration process and of how to determine the number of iterations needed for a given situation, see PW, section 6.2.3.

Step 4: Obtain the formal solutions in the wave zone. The solution of Eq. (11.61) that has outward propagating disturbances at infinity is

$$
\psi ^ { A } ( t , \pmb { x } ) = 4 \int \frac { \tau ^ { A } ( t - | \pmb { x } - \pmb { x } ^ { \prime } | / \nu _ { g d } , \pmb { x } ^ { \prime } ) } { | \pmb { x } - \pmb { x } ^ { \prime } | } d ^ { 3 } \pmb { x } ^ { \prime } .
$$

The integration is to be carried out over the past “null cone” $\mathcal C ( x )$ of the field point $( t , x )$ , that is, over those points $( t ^ { \prime } , x ^ { \prime } )$ such that $t ^ { \prime } = t - | \pmb { x } - \pmb { x } ^ { \prime } | / \nu _ { g A }$ (see Figure 11.3). In dealing with slow-motion sources, it is conventional to divide the spatial domain into a near zone, with $r < \mathcal { R }$ and a far zone or wave zone, with $r > \mathcal { R }$ , where $\mathcal { R } \sim \lambda _ { c } \sim t _ { c }$ , where $t _ { c }$ and $\lambda _ { c }$ are the characteristic timescale of the source and the characteristic wavelength of the radiation, respectively. The vertical world tube $\mathcal { D }$ in Figure 11.3 is the interior region $r < \mathcal { R }$ projected in spacetime. The hypersurface $\mathcal { N } ( x )$ is that piece of the null cone $\mathcal { C }$ within the near zone $\mathcal { D }$ , and the hypersurface $\mathcal { W } ( x )$ is the rest of the null cone. Thus the integral for the field $\psi ^ { A }$ can be written as an integral over $\mathcal { N } ( x )$ plus an integral over $\mathcal { W } ( x )$ , that is,

![](images/62dfb0940f5be91ba8696962bbf2646b40c154723c39e25d68b4d4996ef90a4a.jpg)  
Integration domains for the retarded solution (11.64) of the wave equation (11.61) with the field point in the wave zone: $\mathcal C (  { \boldsymbol { { x } } } )$ is the past “null” cone (with speed $V _ { g A } )$ of the field point $x ; \mathcal { D }$ is the world tube of the near zone of radius $\mathcal { R } ; \mathcal { N } ( \boldsymbol { \chi } )$ is the intersection of $\mathcal { D }$ with $\mathcal C (  { \boldsymbol { { x } } } )$ and ${ \mathcal { W } } ( x )$ is the rest of the null cone; $\mathcal { M } ( \boldsymbol { x } )$ is a constant retarded-time hypersurface used for calculating multipole moments.

$$
\psi ^ { A } ( t , \pmb { x } ) = \psi _ { \mathcal { N } } ^ { A } ( t , \pmb { x } ) + \psi _ { \mathcal { W } } ^ { A } ( t , \pmb { x } ) .
$$

To obtain the gravitational waveform and the energy flux, we want to evaluate the fields in the far wave zone, and retain only the leading contributions in powers of $1 / R$ , where $R$ is the distance to the source. In the integral $\psi _ { \mathcal { N } } ^ { A }$ , $\left| x ^ { \prime } \right| < \mathcal { R }$ , while $R \gg \mathcal { R }$ , so we can expand $\vert x - x ^ { \prime } \vert$ in powers of $x ^ { \prime } / R$ to obtain

$$
\psi _ { \mathcal { N } } ^ { A } = \frac { 4 } { R } \int _ { \mathcal { N } } \boldsymbol { \tau } ^ { A } \left( t - \frac { R } { \nu _ { g A } } + \frac { \boldsymbol { N } \cdot \boldsymbol { x } ^ { \prime } } { \nu _ { g A } } , \boldsymbol { x } ^ { \prime } \right) d ^ { 3 } \boldsymbol { x } ^ { \prime } + O ( R ^ { - 2 } ) ,
$$

where $N \equiv x / R$ . For dynamical sources, $t _ { c } \sim r _ { c } / \nu _ { c }$ , where $r _ { c }$ is a characteristic scale of the material source and $\nu _ { c }$ is a characteristic velocity within the source, and thus for slowmotion sources $( \nu _ { c } \ll 1 )$ ), $\mathcal { R } \sim t _ { c } \gg r _ { c }$ , so the matter source is confined to a region deep within the near zone, and $\partial / \partial t \sim \nu _ { c } / r _ { c }$ . Thus we can expand the retardation in Eq. (11.66) in the form

$$
\psi _ { \mathcal { N } } ^ { 4 } = \frac { 4 } { R } \sum _ { m = 0 } ^ { \infty } \frac { 1 } { m ! \left( \nu _ { g A } \right) ^ { m } } \left( \frac { \partial } { \partial t } \right) ^ { m } \int _ { \mathcal { M } } \tau ^ { A } \left( t - \frac { R } { \nu _ { g A } } , x ^ { \prime } \right) \left( N \cdot x ^ { \prime } \right) ^ { m } d ^ { 3 } x ^ { \prime } + O ( R ^ { - 2 } ) ,
$$

where the integration is now over the constant retarded-time hypersurface $\mathcal { M }$ (see Figure 11.4). Note that

$$
\psi _ { \mathcal { N } , j } ^ { A } = - ( \nu _ { g A } ) ^ { - 1 } N _ { j } \dot { \psi } _ { \mathcal { N } } ^ { A } + O ( R ^ { - 2 } ) .
$$

The source $\tau ^ { A }$ will contain contributions proportional to the matter variables $\rho ^ { * } , p , \Pi , \nu _ $ , and so on, which have “compact support,” that is, are nonzero only in finite spatial regions where the matter resides. However, at the second iteration and beyond, $\tau ^ { A }$ will also contain contributions proportional to products of fields and their derivatives. These contributions extend over all spacetime, although they generally decrease with distance from the source. Thus in integrating the multipole moments of $\tau ^ { A }$ over the hypersurface $\mathcal { M }$ , the integrations must be extended all the way to the boundary of the near zone, at $\mathcal { R }$ .

![](images/afc14d4b9582aba859fbaeaeafd401bb950eaf4d05f5b85dab08653bdede2a46.jpg)  
Integration domains for the retarded solution (11.64) of the wave equation (11.61) with the field point in the near zone: here $\mathcal { M } ( \boldsymbol { x } )$ is a constant time hypersurface at time t within the near zone.

Because of these field contributions to $\tau ^ { A }$ , one must also include the integral $\psi _ { \mathcal { W } } ^ { A } ( t , \boldsymbol { x } )$ over the rest of the past null cone, beyond the near zone. It turns out that this integration can best be done by changing variables from $d ^ { 3 } x ^ { \prime } = r ^ { \prime 2 } d r ^ { \prime } d \Omega ^ { \prime }$ , where $d \Omega ^ { \prime }$ is the element of solid angle, to a null-type variable $u ^ { \prime } \equiv \nu _ { g A } t - r ^ { \prime } - | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } |$ , and $d ^ { 3 } x ^ { \prime } = r ^ { \prime } ( u ^ { \prime } , \theta ^ { \prime } , \phi ^ { \prime } ) ^ { 2 } d u ^ { \prime } d \Omega ^ { \prime }$ (Wiseman and Will, 1991). This change is motivated by the fact that the fields that make up $\tau ^ { A }$ in the far zone are themselves retarded fields. Both the inner and the outer integrals will depend in general on the radius $\mathcal { R }$ where they terminate, but since that radius is chosen arbitrarily, the final result cannot depend on $\mathcal { R }$ . This realization then provides a procedure for identifying and retaining in $\psi _ { \mathcal { N } } ^ { A } ( t , \boldsymbol { x } )$ and in $\psi _ { \mathcal { W } } ^ { A } ( t , x )$ only contributions that do not depend on $\mathcal { R }$ , and throwing away contributions that depend on $\mathcal { R }$ . In fact it was shown explicitly that all $\mathcal { R }$ -dependent contributions actually cancel each other in the sum $\psi _ { \mathcal { N } } ^ { A } + \psi _ { \mathcal { W } } ^ { A }$ (Pati and Will, 2000). In general relativity, it turns out that the contributions of $\psi _ { \mathcal { W } } ^ { A }$ first occur $1 . 5 \mathrm { P N }$ orders beyond the leading quadrupole approximation; they are known as gravitationalwave “tails.” While it is likely that, in an alternative theory of gravity, these outer integrals will contribute at a similar PN order, they must be carefully examined to determine the precise order at which they will contribute. In fact, in theories of gravity with dipole radiation, dipole “tails” from $\psi _ { \mathcal { W } } ^ { A }$ can occur in the waveform at 1PN order, instead of $1 . 5 \mathrm { P N }$ order.

Step 5: Obtain a post-Newtonian expansion of the source $\tau ^ { A }$ . This will be needed both for evaluation of the multipole moments of $\tau ^ { A }$ in Eq. (11.67) to the required order, and for obtaining the equations of motion to the required order. For this purpose, we need the near-zone solution for the fields $\psi ^ { A }$ . For $| x - x ^ { \prime } | \ll \mathcal { R }$ , we can carry out the expansion of the inner integral $\psi _ { \mathcal { N } } ^ { A }$ in the form

$$
\begin{array} { l } { { \displaystyle \psi _ { \mathcal { N } } ^ { A } = 4 \sum _ { m = 0 } ^ { \infty } \frac { ( - 1 ) ^ { m } } { m ! ( \nu _ { g A } ) ^ { m } } \int _ { \mathcal { M } } \tau ^ { A } ( t , x ^ { \prime } ) | x - x ^ { \prime } | ^ { m - 1 } d ^ { 3 } x ^ { \prime } , } } \\ { { \displaystyle \quad = 4 \int _ { \mathcal { M } } \frac { \tau ^ { A } ( t , x ^ { \prime } ) } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } - \frac { 4 } { \nu _ { g A } } \frac { \partial } { \partial t } \int _ { \mathcal { M } } \tau ^ { A } ( t , x ^ { \prime } ) d ^ { 3 } x ^ { \prime } } } \\ { { \displaystyle \quad \quad + \frac { 2 } { \nu _ { g A } ^ { 2 } } \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } \int _ { \mathcal { M } } \tau ^ { A } ( t , x ^ { \prime } ) | x - x ^ { \prime } | d ^ { 3 } x ^ { \prime } + \ldots . } } \end{array}
$$

The first term is an instantaneous solution of Poisson’s equation with the source $\tau ^ { A }$ (called a Poisson potential), and, because $\partial / \partial t \sim \nu / r$ , subsequent terms are of $0 . 5 \mathrm { P N }$ order, 1PN order, and so on. One must also evaluate the outer integral $\psi _ { \mathcal { W } } ^ { A }$ for fields points in the near zone, although generally speaking, this integral begins to contribute only at very high post-Newtonian order (4PN in the case of general relativity).

Depending on the tensorial nature of $\tau ^ { A }$ , in the near zone it will typically be made up of terms of the form

$$
\tau ^ { A } \sim \left\{ \begin{array} { l l } { \rho ^ { * } , \rho ^ { * } \nu ^ { 2 } , p , \rho ^ { * } U , ( \nabla U ) ^ { 2 } , U _ { j } U _ { k } , \dots } & { \mathrm { s c a l a r , t e n s o r } } \\ { \rho ^ { * } \nu ^ { j } , \rho ^ { * } \nu ^ { 2 } \nu ^ { j } , \rho ^ { * } U \nu ^ { j } , p \nu ^ { j } , \nabla V ^ { j } \cdot \nabla U , \dots } & { \mathrm { v e c t o r } , } \end{array} \right.
$$

if the source is modeled as a fluid with weak internal gravitational fields, or

$$
\tau ^ { A } \sim \left\{ \begin{array} { l l } { m _ { a } ( \psi _ { A } ) , m _ { a } ( \psi _ { A } ) \nu ^ { 2 } , m _ { a } ( \psi _ { A } ) U , ( \nabla U ) ^ { 2 } , U _ { , j } U _ { , k } , \ldots } & { \mathrm { s c a l a r , t e n s o r } } \\ { m _ { a } ( \psi _ { A } ) \nu ^ { j } , m _ { a } ( \psi _ { A } ) \nu ^ { 2 } \nu ^ { j } , m _ { a } ( \psi _ { A } ) U \nu ^ { j } , \nabla V ^ { j } \cdot \nabla U , \ldots } & { \mathrm { v e c t o r } , } \end{array} \right.
$$

if the source is modeled as a system of compact objects with masses dependent upon fields $\Psi _ { A }$ with appropriately defined “sensitivities” (see Section 10.3). In the compact-body case, each mass is accompanied by a delta function, augmented by a suitable prescription for regularizing infinite self-fields effects. Here “scalar” or “tensor” refers to quantities such $\mathrm { a s } p _ { 0 0 } , p _ { j k } , \Psi , k ^ { 0 }$ , and so on, while “vector” refers to quantities such as $p _ { 0 j } , k ^ { j }$ , and so on. The wave-zone field is then determined by multipole moments of the source $\tau ^ { A }$ (Eq. (11.67)).

Various post-Newtonian conservation laws can often be used to simplify the multipole moments of $\tau ^ { A }$ in Eq. (11.67). For example, the monopole moment $\int _ { \mathcal { M } } \rho ^ { * } d ^ { 3 } x$ is constant because of the conservation of baryon number of the system. If a collection of terms in a multipole moment can be combined to yield a component of the pseudotensorial quantity $\tau ^ { \mu \nu }$ , then one can exploit a number of identities that follow from $\tau ^ { \mu \nu } { } _ { , \nu } = 0$ to simplify or transform expressions. These identities include

$$
\begin{array} { c } { { \tau ^ { 0 j } = \left( \tau ^ { 0 0 } x ^ { j } \right) _ { , 0 } + \left( \tau ^ { 0 k } x ^ { j } \right) _ { , k } , } } \\ { { \displaystyle \tau ^ { ( j k ) } = \frac { 1 } { 2 } \left( \tau ^ { 0 0 } x ^ { j } x ^ { k } \right) _ { , 0 0 } + \left( \tau ^ { ( p j ) } x ^ { k } + \tau ^ { ( p k ) } x ^ { j } \right) _ { , p } - \frac { 1 } { 2 } \big ( \tau ^ { p q } x ^ { j } x ^ { k } \big ) _ { , p q } } } \\ { { \displaystyle + \left[ ( \tau ^ { [ 0 p ] } x ^ { j } x ^ { k } ) _ { , p } - \tau ^ { [ 0 j ] } x ^ { k } - \tau ^ { [ 0 k ] } x ^ { j } \right] _ { , 0 } , } } \\ { { \displaystyle \tau ^ { 0 j } x ^ { k } = \frac { 1 } { 2 } \left( \tau ^ { 0 0 } x ^ { j } x ^ { k } \right) _ { , 0 } + \tau ^ { 0 [ j } x ^ { k ] } + \frac { 1 } { 2 } \left( \tau ^ { 0 p } x ^ { j } x ^ { k } \right) _ { , p } . } } \end{array}
$$

Note that, because we are dealing with semiconservative theories of gravity, $\tau ^ { \mu \nu }$ is not necessarily symmetric, so we have retained contributions of the antisymmetric parts of $\tau ^ { \mu \nu }$ where necessary.

Step 6: Determine the energy, momentum and angular momentum loss rate in terms of $\psi$ . Generally speaking, this involves using the pseudotensorial quantity $\tau ^ { \mu \nu }$ and its associated conservation law $\tau ^ { \mu \nu } { } _ { , \nu } = 0$ . If one defines a quantity $P ^ { 0 }$ according to

$$
P ^ { \mu } \equiv \int \tau ^ { \mu 0 } d ^ { 3 } x ,
$$

then it is straightforward to show that

$$
\frac { d P ^ { \mu } } { d t } = - \oint \tau ^ { \mu j } d ^ { 2 } S _ { j } ,
$$

where the surface integral is to be carried out in the far wave zone. Since the matter energymomentum tensor $T ^ { \mu \nu }$ has compact support, it will vanish in the far zone, and thus only the contributions from the fields $\psi _ { A }$ to $\tau ^ { \mu j }$ will be needed. And because $d ^ { 2 } S _ { j } = R ^ { 2 } n ^ { j } d \Omega$ and we wish to take the limit as $R \to \infty$ , only the $R ^ { - 2 }$ contributions to $\tau ^ { \mu j }$ are relevant. Making use of the far-zone behavior of Eq. (11.68), one can express the rate of change of $P ^ { 0 }$ and $P ^ { j }$ in the generic form

$$
\begin{array} { l } { \displaystyle \frac { d P ^ { 0 } } { d t } = - \frac { R ^ { 2 } } { 3 2 \pi } \sum _ { A B } \oint N ^ { L } \delta ^ { M } \dot { \psi } _ { A } \dot { \psi } _ { B } d \Omega , } \\ { \displaystyle \frac { d P ^ { j } } { d t } = - \frac { R ^ { 2 } } { 3 2 \pi } \sum _ { A B } \oint N ^ { L } \delta ^ { M } \dot { \psi } _ { A } \dot { \psi } _ { B } N ^ { j } d \Omega , } \end{array}
$$

where $N ^ { L }$ denotes a product of $L$ unit vectors, and $\delta ^ { M }$ denotes a product of $M$ Kronecker deltas. The $L$ and $M$ indices are suitably contracted with indices on the $\psi _ { A } \mathbf { s }$ . In integrating over solid angles, one makes use of the identities

$$
\oint N ^ { L } d \Omega = \left\{ \begin{array} { l l } { \frac { 4 \pi } { ( \ell + 1 ) ! ! } \left[ \delta ^ { L / 2 } + \mathrm { s y m } ( q ) \right] } & { L \mathrm { e v e n } , } \\ { 0 } & { L \mathrm { o d d } , } \end{array} \right.
$$

where $\operatorname { s y m } ( q )$ denotes all distinct terms obtained by permuting indices on the Kronecker deltas, with $q = ( \ell - 1 ) ! !$ ! denoting the total number of terms.

Similarly one can define an angular-momentum quantity, given by

$$
J ^ { j k } \equiv 2 \int x ^ { [ j } \tau ^ { k ] 0 } d ^ { 3 } x ,
$$

whose rate of change is given by

$$
\frac { d J ^ { j k } } { d t } = - 2 \int \tau ^ { [ j k ] } d ^ { 3 } x - 2 \oint x ^ { [ j } \tau ^ { k ] m } d ^ { 2 } S _ { m } .
$$

The first term in Eq. (11.78) is not related to gravitational radiation; it is the result of the fact that some theories of gravity are only semi conservative (see Section 4.4 and Eq. (4.70)). For the surface term, the presence of the factor $x ^ { j } \propto R$ means that one must calculate the subleading $R ^ { - 3 }$ terms in $\tau ^ { k ] m }$ in order to find a nontrivial result (the $R ^ { - 2 }$ contributions give zero because of an odd number of unit vectors). This means obtaining the subleading $R ^ { - 2 }$ terms in the $\psi _ { A }$ . Section 12.2.4 of PW gives a detailed derivation within general relativity.

In some theories of gravity, $\tau _ { \mu \nu }$ is not unique; scalar-tensor theories are examples (Lee, 1974). Therefore one must determine the physical meaning of the quantity $P ^ { 0 }$ . In general relativity, it is known to be the Kepler measured mass, or the Bondi mass of the system (when evaluated at spacelike infinity, it is also the Arnowitt-Deser-Misner (ADM) mass). In scalar-tensor theories, different choices for $\tau _ { \mu \nu }$ lead to different masses: tensor mass, scalar mass or active (Kepler) mass. In the end, it is not so important which type of “mass” is represented by $P ^ { 0 }$ , but rather what changes in observable parameters are induced by the change $d P ^ { 0 } / d t$ . Therefore one must carefully calculate $P ^ { 0 }$ to an appropriate PN order in order to relate it to quantities such as orbital period, which are measurable.

Step 7: Apply to binary systems. We consider a system made of two bodies that are small compared to their separations $( d \ll r )$ ; that is, we ignore all tidal interactions between them. We may thus treat each body’s structure as static and spherical in its own rest frame. We then follow the procedure of Section 6.3: for a given element of matter in body a, we write ${ \pmb x } \equiv { \pmb X } _ { a } + { \bar { \pmb x } }$ and $\nu \equiv \nu _ { a }$ , where

$$
\begin{array} { l } { \displaystyle { X _ { a } \equiv \frac { 1 } { m _ { a } } \int _ { a } \rho ^ { * } \left( 1 + \Pi - \frac { 1 } { 2 } \bar { U } \right) x d ^ { 3 } x , } } \\ { \displaystyle { m _ { a } \equiv \int _ { a } \rho ^ { * } \left( 1 + \Pi - \frac { 1 } { 2 } \bar { U } \right) d ^ { 3 } x , } } \\ { \displaystyle { \quad \nu \equiv \frac { d X } { d t } , } } \\ { \displaystyle { \quad \bar { U } \equiv \int _ { a } \frac { \rho ^ { * } } { | x - x _ { a } | } d ^ { 3 } x . } } \end{array}
$$

We note that $m _ { a }$ is conserved to post-Newtonian order, as long as tidal forces are neglected. The full Newtonian potential $U$ for spherical bodies is given by

$$
\begin{array} { r l r } & { } & { U ( { \pmb x } , t ) = \bar { U } + \displaystyle \sum _ { b \neq a } \frac { m _ { b } } { | { \pmb x } - { \pmb X } _ { b } | } , \quad { \pmb x } \mathrm { i n s i d e b o d y } a } \\ & { } & { \qquad = \displaystyle \sum _ { b } \frac { m _ { b } } { | { \pmb x } - { \pmb X } _ { b } | } , \qquad { \pmb x } \mathrm { o u t s i d e b o d y } a . } \end{array}
$$

In the compact-body approach, each body is located at the singularity of the delta function, internal gravitational fields are regularized appropriately and the masses are expanded in terms of sensitivities. Only the external potential is present, where now $m _ { a } \equiv \stackrel { - } { m } _ { a } ( \psi _ { A } ^ { ( 0 ) } )$ , where $\psi _ { A } ^ { ( 0 ) }$ represents the asymptotic values of the relevant auxiliary fields.

Step 8: Apply balance equations to obtain the orbital evolution. Let us suppose that $\tau ^ { \mu \nu }$ has been chosen so that, to the appropriate orders, $P ^ { 0 }$ and $J ^ { j } = ( 1 / 2 ) \epsilon ^ { j p q } J ^ { p q }$ , are given by

$$
\begin{array} { l } { { P ^ { 0 } = \displaystyle \sum _ { a } \Biggl [ m _ { a } + \frac { 1 } { 2 } m _ { a } \nu _ { a } ^ { 2 } - \frac { 1 } { 2 } \sum _ { b \neq a } \frac { \mathcal { G } m _ { a } m _ { b } } { r _ { a b } } + O \bigl ( m _ { a } \epsilon ^ { 2 } \bigr ) \Biggr ] , } } \\ { { J = \displaystyle \sum _ { a } m _ { a } \pmb x _ { a } \times \pmb \nu _ { a } \bigl [ 1 + O ( \epsilon ) \bigr ] , } } \end{array}
$$

where $r _ { a b } \equiv | \pmb { x } _ { a } - \pmb { x } _ { b } |$ and where $\mathcal { G } \equiv \mathcal { G } _ { 1 2 }$ is the parameter defined in the modified EIH Lagrangian, Eq. (10.29). It depends in general on the parameters of the theory and on the sensitivities.

For a binary system we may evaluate the orbital terms in Eq. (11.81) using the appropriate Keplerian equations, with the result

$$
\begin{array} { c } { { P ^ { 0 } = m - \eta \displaystyle \frac { \mathcal { G } m ^ { 2 } } { 2 a } + O ( m \epsilon ^ { 2 } ) , } } \\ { { J = \eta m \sqrt { \mathcal { G } m p } \hat { \pmb { h } } [ 1 + O ( \epsilon ) ] , } } \end{array}
$$

where $m = m _ { 1 } + m _ { 2 }$ , $\eta = m _ { 1 } m _ { 2 } / m ^ { 2 }$ , $a$ is the semimajor axis, related to the binary orbital period by $( P _ { \mathrm { b } } / 2 \pi ) ^ { 2 } = a ^ { 3 } / \mathcal { G } m$ , and $p = a ( 1 - e ^ { 2 } )$ .

In the emission of gravitational radiation whose source is the orbital motion, we will treat the quantities $m _ { 1 }$ and $m _ { 2 }$ as constant because of our neglect of tidal forces and internal motions. Then one can obtain a direct relation between $d P ^ { 0 } / d t$ and $d J / d t$ and variations in $a , e _ { \mathrm { { : } } }$ , and $P$ . Thus, for example, if the resulting energy loss rate for a binary system is given by Eq. (11.59), then one can average over an orbit to obtain

$$
\frac { d P ^ { 0 } } { d t } = - \frac { 3 2 } { 5 } \eta ^ { 2 } \mathcal { G } ^ { - 1 } \left( \frac { \mathcal { G } m } { a } \right) ^ { 5 } F ( e ) - \frac { 1 } { 3 } \kappa _ { D } \eta ^ { 2 } \mathcal { S } ^ { 2 } \mathcal { G } ^ { - 1 } \left( \frac { \mathcal { G } m } { a } \right) ^ { 4 } G ( e ) ,
$$

where

$$
\begin{array} { l } { { F ( e ) = \displaystyle \frac { 1 } { 1 2 } ( 1 - e ^ { 2 } ) ^ { - 7 / 2 } \left[ \kappa _ { 1 } \left( 1 + \frac { 7 } { 2 } e ^ { 2 } + \frac { 1 } { 4 } e ^ { 4 } \right) - \frac { 1 } { 2 } \kappa _ { 2 } e ^ { 2 } \left( 1 + \frac { 1 } { 2 } e ^ { 2 } \right) \right] , } } \\ { { G ( e ) = ( 1 - e ^ { 2 } ) ^ { - 5 / 2 } \left( 1 + \frac { 1 } { 2 } e ^ { 2 } \right) . } } \end{array}
$$

Combining Eqs. (11.82) and (11.83) with the relation between orbital period $P _ { \mathrm { b } }$ and semimajor axis $a$ , we can obtain an expression for the time-derivative $\dot { P } _ { \mathrm { { b } } }$ ,

$$
\dot { P } _ { \mathrm { b } } = - \frac { 1 9 2 \pi } { 5 } \left( \frac { 2 \pi \mathcal { G } \mathcal { M } } { P _ { \mathrm { b } } } \right) ^ { 5 / 3 } F ( e ) - 2 \pi \kappa _ { D } \eta S ^ { 2 } \left( \frac { 2 \pi \mathcal { G } m } { P _ { \mathrm { b } } } \right) G ( e ) ,
$$

where $\mathcal { M }$ is called the “chirp mass,” given by

$$
\mathcal { M } \equiv \eta ^ { 5 / 3 } m .
$$

If one has calculated $d P ^ { 0 } / d t$ and $d J / d t$ to higher PN orders, then it will be necessary to evaluate $P ^ { 0 }$ and $\pmb { J }$ to a corresponding PN order.

Although the use of energy and angular momentum balance to infer the behavior of the source from flux formulae in the far zone was specifically criticized by Ehlers et al. (1976), it has actually been validated within general relativity and scalar-tensor theories to modest PN orders beyond the quadrupole formula via first-principles calculations of the radiationreaction forces (Pati and Will, 2002; Will, 2005; Mirshekari and Will, 2013). Unfortunately, to reach a given PN order beyond the quadrupole formula, it is much easier to obtain flux results than it is to obtain radiation-reaction results. Therefore, in order to work at the high-PN orders required to analyze the inspiral of compact binaries, one is forced to adopt the balance assumption.

This completes our recipe for analyzing the generation of gravitational waves. To illustrate the method, we will now focus on two metric theories, general relativity and scalar-tensor theories where gravitational radiation from compact binaries has been analized in considerable detail. Partial results are also known for some of the alternative theories discussed in Chapter 5.

# 11.5.2 General relativity

In Section 5.2.2 we described the post-Minkowskian approach to solving Einstein’s equations iteratively, using the Landau-Lifshitz formulation of the equations. We write the wave equation for the field $h ^ { \alpha \beta }$ , Eq. (5.19) in the form

$$
\begin{array} { r } { \boxed { \ d \Xi h ^ { \alpha \beta } } = - 1 6 \pi \tau ^ { \alpha \beta } , } \end{array}
$$

where τ αβ = (−g)(Tαβ + t αβLL + t αβH ), and where we have set G = 1. Note that, because of the harmonic gauge condition $h ^ { \alpha \beta } { } _ { , \beta } = 0$ , we have that $\tau ^ { \alpha \beta } { } _ { , \beta } = 0$ . Using Eq. (11.67), and recalling that $\nu _ { g } = 1$ in general relativity, we obtain the multipole expansion in the far wave zone,

$$
h _ { \mathcal { N } } ^ { \alpha \beta } = \frac { 4 } { R } \sum _ { m = 0 } ^ { \infty } \frac { 1 } { m ! } \left( \frac { \partial } { \partial t } \right) ^ { m } \int _ { \mathcal { M } } \tau ^ { \alpha \beta } \left( t - R , \pmb { x } ^ { \prime } \right) \left( \pmb { N } \cdot \pmb { x } ^ { \prime } \right) ^ { m } d ^ { 3 } \pmb { x } ^ { \prime } + O ( R ^ { - 2 } ) .
$$

Because of the harmonic gauge condition combined with Eq. (11.68), we can show that

$$
\begin{array} { r l } & { h _ { \mathcal { N } } ^ { j 0 } = N _ { k } h _ { \mathcal { N } } ^ { j k } + O ( R ^ { - 2 } ) \left[ \mathrm { m o d u l o ~ a ~ \ c o n s t a n t } \right] , } \\ & { h _ { \mathcal { N } } ^ { 0 0 } = N _ { j } N _ { k } h _ { \mathcal { N } } ^ { j k } + O ( R ^ { - 2 } ) \left[ \mathrm { m o d u l o ~ a ~ \ c o n s t a n t } \right] , } \end{array}
$$

therefore, we need to determine only the jk components.

For the first iteration $h _ { 1 } ^ { j k }$ , the source $\tau _ { 0 } ^ { j k }$ is the special relativistic stress tensor for matter $T _ { 0 } ^ { j k } \sim \rho ^ { * } \nu ^ { j } \nu ^ { k }$ . However, the equation of motion that is compatible with the gauge condition at the first iteration is Tαβ0 $T _ { 0 } ^ { \alpha \beta } { } _ { , \beta } ~ = ~ 0$ , which implies no gravitational interaction between the two bodies. Furthermore, an inspection of the Landau-Lifshitz pseudotensor $t _ { \mathrm { L L } } ^ { \alpha \beta }$ reveals that it contributes terms to vitational potential; these terms are o $\tau ^ { j k }$ of the form e same order $U _ { j } U _ { , k }$ , where  purely $U$ is the near zetic terms in $T _ { 0 } ^ { j k }$ and therefore they must be included. This is why $t w o$ iterations of the relaxed equations are essential. However, it turns out that these details can be averted by exploiting the identity in Eq. (11.72b). At the lowest multipole order, we have that

$$
\begin{array} { c } { { h _ { \mathcal { N } } ^ { j k } = \displaystyle \frac { 4 } { R } \int _ { \mathcal { M } } \tau ^ { j k } \left( t - R , { \pmb x } ^ { \prime } \right) d ^ { 3 } x ^ { \prime } } } \\ { { \displaystyle = \frac { 2 } { R } \frac { d ^ { 2 } } { d t ^ { 2 } } \int _ { \mathcal { M } } \tau ^ { 0 0 } \left( t - R , { \pmb x } ^ { \prime } \right) x ^ { \prime j } x ^ { \prime k } d ^ { 3 } x ^ { \prime } } . }  \end{array}
$$

In converting the divergence terms in Eq. (11.72b) to surface integrals at the boundary of $\mathcal { M }$ , we must verify that there are no $\mathcal { R }$ -independent contributions. Any $\mathcal { R }$ -dependent contributions can be discarded, as we know that they will be cancelled by corresponding contributions from the outer integral $h _ { \mathcal { W } } ^ { k j }$ . To lowest PN order, $\tau ^ { 0 0 } = \rho ^ { * }$ , thus we obtain

$$
\begin{array} { l } { { \displaystyle h _ { \mathcal { N } } ^ { j k } = \frac { 2 } { R } \frac { d ^ { 2 } } { d t ^ { 2 } } \int _ { \mathcal { M } } \rho ^ { \ast } \left( t - R , \pmb { x } ^ { \prime } \right) x ^ { \prime j } x ^ { \prime k } d ^ { 3 } x ^ { \prime } \left[ 1 + O ( \epsilon ) \right] } } \\ { { \displaystyle ~ = \frac { 2 } { R } \ddot { I } ^ { j k } ( t - R ) , } } \end{array}
$$

where $\begin{array} { r } { I ^ { j k } \equiv \sum _ { a } m _ { a } x _ { a } ^ { j } x _ { a } ^ { k } } \end{array}$ is the quadrupole moment tensor of the source. This is the wellknown quadrupole formula for the gravitational waveform. To complete the solution we must add the term $h _ { \mathcal { W } } ^ { j k }$ from the integration over the rest of the past null cone, however this is known not to contribute until $1 . 5 \mathrm { P N }$ order beyond the leading quadrupole term.

It can be demonstrated that the total mass-energy of an isolated system is given by

$$
{ \cal E } \equiv P ^ { 0 } = \int \tau ^ { 0 0 } d ^ { 3 } x .
$$

Then, because of the condition $\tau ^ { \alpha \beta } { } _ { , \beta } = 0$ , we find that

$$
\frac { d E } { d t } = \int \tau ^ { 0 0 } { } _ { , 0 } d ^ { 3 } x = - \int \tau ^ { 0 j } { } _ { , j } d ^ { 3 } x = - \oint \tau ^ { 0 j } N _ { j } R ^ { 2 } d \Omega ,
$$

where $d \Omega$ is the element of solid angle. By examining carefully the structure of the Landau-Lifshitz and harmonic pseudotensors of Eqs. (5.16) and (5.20) in the far wave zone, and taking Eqs. (11.68) and (11.89) into account, we obtain the energy loss rate

$$
\frac { d E } { d t } = - \frac { R ^ { 2 } } { 3 2 \pi } \oint \dot { h } _ { \mathrm { T T } } ^ { j k } \dot { h } _ { \mathrm { T T } } ^ { j k } d \Omega ,
$$

where the subscript TT denotes the “transverse tracefree” part of $h ^ { j k }$ , given by

$$
h _ { \mathrm { T T } } ^ { j k } \equiv \left( P _ { m } ^ { j } P _ { n } ^ { k } - \frac { 1 } { 2 } P ^ { j k } P _ { m n } \right) h ^ { m n } ,
$$

where $P ^ { j k }$ is the “projection tensor” given by

$$
P ^ { j k } \equiv \delta ^ { j k } - N ^ { j } N ^ { k } .
$$

We substitute Eq. (11.91) into (11.94) and integrate over solid angles, making use of the identities (11.76). The result is the quadrupole formula for the energy loss rate, Eq. (11.53). Substituting the quadrupole moment tensor for a binary system, $I ^ { j k } = \mu x ^ { j } x ^ { k } + m X ^ { j } X ^ { k }$ , taking the time derivatives, and using the Newtonian equation of motion $d \pmb { \nu } / d t = - m \pmb { x } / r ^ { 3 }$ , yields Eq. (11.54) for the waveform and Eq. (11.55) for the energy loss rate. Thus, for general relativity, $\kappa _ { 1 } = 1 2$ , $\kappa _ { 2 } = 1 1$ , and $\kappa _ { D } = 0$ .

Analogous formulae for the angular momentum loss rate and the rate of change of linear momentum of the source can be obtained:

$$
\begin{array} { l } { { \displaystyle \frac { d J ^ { k } } { d t } = - \frac { R ^ { 2 } } { 1 6 \pi } \epsilon ^ { k m n } \oint \left[ h _ { \mathrm { T T } } ^ { m p } \dot { h } _ { \mathrm { T T } } ^ { n p } - \frac { 1 } { 2 } \dot { h } _ { \mathrm { T T } } ^ { p q } x ^ { m } \frac { \partial } { \partial x ^ { n } } h _ { \mathrm { T T } } ^ { p q } \right] d \Omega } } \\ { { \displaystyle \quad = \frac { 2 } { 5 } \epsilon ^ { k m n } \ddot { T } ^ { ( m p ) } \ddot { T } ^ { ( n p ) } } , } \\ { { \displaystyle \frac { d P ^ { k } } { d t } = - \frac { R ^ { 2 } } { 3 2 \pi } \oint \dot { h } _ { \mathrm { T T } } ^ { m n } \dot { h } _ { \mathrm { T T } } ^ { m n } N ^ { k } d \Omega } } \\  { \displaystyle \quad = \frac { 2 } { 6 3 } ( { \mathrm { \it { l } } } ^ { ( 4 ) } { \it { l } } ^ { ( k m n ) } \ddot { T } ^ { m n } - \frac { 1 6 } { 4 5 } \epsilon ^ { k m n } \dot { T } ^ { m p } \ddot { T } ^ { m p } , } \end{array}
$$

where $I ^ { k m n }$ and $J ^ { m p }$ are the mass octupole and current quadrupole moments, given to lowest PN order by

$$
\begin{array} { l } { { \displaystyle I ^ { k m n } \equiv \int \rho ^ { * } x ^ { k } x ^ { m } x ^ { n } d ^ { 3 } x , } } \\ { { \displaystyle J ^ { m p } \equiv \epsilon ^ { m a b } \int \rho ^ { * } x ^ { a } \nu ^ { b } x ^ { p } d ^ { 3 } x . } } \end{array}
$$

Note that, at purely quadrupole order, the linear momentum change vanishes, because the number of unit vectors $N ^ { j }$ in the angular integral will always be odd. To get the final expression in Eq. (11.97b) it is necessary to compute the $0 . 5 \mathrm { P N }$ corrections to the waveform $h ^ { j k }$ , resulting in the appearance of the higher-order multipole moments of Eq. (11.98). For a binary system at lowest PN order, these loss rates become

$$
\begin{array} { l } { \displaystyle \frac { d J } { d t } = - \frac { 8 } { 5 } \eta ^ { 2 } \left( \frac { m } { r } \right) ^ { 3 } h \left( 2 \nu ^ { 2 } - 3 \dot { r } ^ { 2 } + 2 \frac { m } { r } \right) , } \\ { \displaystyle \frac { d P } { d t } = \frac { 8 } { 1 0 5 } \eta ^ { 2 } \Delta \left( \frac { m } { r } \right) ^ { 4 } \left[ \nu \left( 5 0 \nu ^ { 2 } - 3 8 \dot { r } ^ { 2 } + 8 \frac { m } { r } \right) - \dot { r } n \left( 5 5 \nu ^ { 2 } - 4 5 \dot { r } ^ { 2 } + 1 2 \frac { m } { r } \right) \right] , } \end{array}
$$

where $\pmb { h } = \pmb { x } \times \pmb { \nu }$ and $\Delta = ( m _ { 2 } - m _ { 1 } ) / m$

Substituting Keplerian formulae for the orbital variables and averaging over an orbit, we can obtain the orbit-averaged $d E / d t$ and $d J / d t$ . Recalling that for the orbit, $E = - \eta m ^ { 2 } / 2 a$ and $J = \eta m \sqrt { m p }$ , where $p ~ = ~ a ( 1 ~ - ~ e ^ { 2 } )$ , we obtain the rate of change of $a$ and $e$ . The results are

$$
\begin{array} { l } { { \displaystyle \frac { d E } { d t } = - \frac { 3 2 } { 5 } \eta ^ { 2 } \left( \frac { m } { a } \right) ^ { 5 } F ( e ) , } } \\ { { \displaystyle \frac { d J } { d t } = - \frac { 3 2 } { 1 5 } \eta ^ { 2 } m \left( \frac { m } { a } \right) ^ { 7 / 2 } G ( e ) . } } \\ { { \displaystyle \frac { d a } { d t } = - \frac { 6 4 } { 5 } \eta \left( \frac { m } { a } \right) ^ { 3 } F ( e ) , } } \\ { { \displaystyle \frac { d e } { d t } = - \frac { 3 0 4 } { 1 5 } \eta _ { a } ^ { - } \left( \frac { m } { a } \right) ^ { 3 } H ( e ) , } } \end{array}
$$

where

$$
\begin{array} { l } { { F ( e ) = ( 1 - e ^ { 2 } ) ^ { - 7 / 2 } \left( 1 + \displaystyle \frac { 7 3 } { 2 4 } e ^ { 2 } + \displaystyle \frac { 3 7 } { 9 6 } e ^ { 4 } \right) , } } \\ { { \displaystyle G ( e ) = ( 1 - e ^ { 2 } ) ^ { - 2 } \left( 1 + \displaystyle \frac { 7 } { 8 } e ^ { 2 } \right) , } } \\ { { \displaystyle H ( e ) = ( 1 - e ^ { 2 } ) ^ { - 5 / 2 } \left( 1 + \displaystyle \frac { 1 2 1 } { 3 0 4 } e ^ { 2 } \right) . } } \end{array}
$$

These equations for $d a / d t$ and $d e / d t$ can be combined and integrated to yield

$$
\frac { a } { a _ { 0 } } = \left( \frac { e } { e _ { 0 } } \right) ^ { 1 2 / 1 9 } \left( \frac { 1 - e _ { 0 } ^ { 2 } } { 1 - e ^ { 2 } } \right) \left( \frac { 1 + 1 2 1 e ^ { 2 } / 3 0 4 } { 1 + 1 2 1 e _ { 0 } ^ { 2 } / 3 0 4 } \right) ^ { 8 7 0 / 2 2 9 9 } ,
$$

where $a _ { 0 }$ and $e _ { 0 }$ are the initial values. Note that gravitational radiation causes the orbit to both shrink and circularize. For $e _ { 0 } ~ \ll ~ 1$ , the evolution is given approximately by $e \simeq e _ { 0 } ( a / a _ { 0 } ) ^ { 1 9 / 1 2 }$ . From $d a / d t$ we can obtain an expression for the rate of change of $P _ { \mathrm { { b } } }$ , given by

$$
\dot { P } _ { \mathrm { b } } = - \frac { 1 9 2 \pi } { 5 } \left( \frac { 2 \pi \mathcal { M } } { P _ { \mathrm { b } } } \right) ^ { 5 / 3 } F ( e ) ,
$$

where $\mathcal { M }$ is the chirp mass given by Eq. (11.86). Notice that by making precise measurements of the phase $\begin{array} { r } { \Phi ( t ) = 2 \pi \int ^ { t } f ( t ^ { \prime } ) d t ^ { \prime } } \end{array}$ of either the orbit or the gravitational waves (for which $f = 2 f _ { \mathrm { b } } ^ { \mathrm { ~ } } = 2 / P _ { \mathrm { b } } ^ { \mathrm { ~ } }$ for the dominant component) as a function of the frequency, one in effect measures the chirp mass of the system. The frequency of the orbit and of any emitted gravitational waves increases with time, varying as $f _ { \mathrm { b } } \sim ( t - t _ { 0 } ) ^ { - 3 / 8 }$ for circular orbits, where $t _ { 0 }$ is the merger time when the binary separation vanishes. The semimajor axis shrinks according to $a \sim ( t - t _ { 0 } ) ^ { 1 / 4 }$ , and thus the waveform amplitude increases as $h \sim a ^ { - 1 } \sim ( t - t _ { 0 } ) ^ { - 1 / 4 }$ . In acoustics, a signal of increasing amplitude and frequency is known as a “chirp”, hence the name “chirp mass” for the quantity $\mathcal { M }$ that controls the process.

From Eq. (11.91), the gravitational waveform for a binary system is given, to lowest PN order by (we drop the subscript $\mathcal { N }$ )

$$
\begin{array} { c } { { h ^ { j k } = \displaystyle \frac { 4 \eta m } { R } ( \nu ^ { j } \nu ^ { k } - \displaystyle \frac { m } { r } n ^ { j } n ^ { k } ) , } } \\ { { \displaystyle  \frac { 4 \eta m ^ { 2 } } { R r } ( \lambda ^ { j } \lambda ^ { k } - n ^ { j } n ^ { k } ) , } } \end{array}
$$

where the second line is the circular orbit limit, and where $r \ \nu , \ n$ and $\lambda$ are given by Eqs. (6.73). We now choose the basis in Figure 6.1 so that the $X$ axis is along the line of nodes and also choose $\omega = 0$ for the pericenter angle. Using the fact that, for $N$ in the $Z$ direction, the projection tensor can be written $P ^ { j k } = e _ { X } ^ { j } e _ { X } ^ { k } + e _ { Y } ^ { j } e _ { Y } ^ { k }$ , we can show that the transverse tracefree components $h _ { \mathrm { T T } } ^ { j k }$ , Eq. (11.95) become

$$
h _ { \mathrm { T T } } ^ { j k } = \left( e _ { X } ^ { j } e _ { X } ^ { k } - e _ { Y } ^ { j } e _ { Y } ^ { k } \right) h _ { + } + \left( e _ { X } ^ { j } e _ { Y } ^ { k } + e _ { Y } ^ { j } e _ { X } ^ { k } \right) h _ { \times } ,
$$

where

$$
\begin{array} { l } { { \displaystyle h _ { + } = \frac { 2 \eta m } { R } \frac { m } { r } \left[ ( \lambda \cdot e _ { X } ) ^ { 2 } - ( \lambda \cdot e _ { Y } ) ^ { 2 } - ( n \cdot e _ { X } ) ^ { 2 } + ( n \cdot e _ { Y } ) ^ { 2 } \right] } } \\ { { \displaystyle \quad = - \frac { 2 \eta m } { R } \frac { m } { r } ( 1 + \cos ^ { 2 } \iota ) \cos 2 \phi , } } \\ { { \displaystyle h _ { \times } = \frac { 4 \eta m } { R } \frac { m } { r } \left[ ( \lambda \cdot e _ { X } ) ( \lambda \cdot e _ { Y } ) - ( n \cdot e _ { X } ) ( n \cdot e _ { Y } ) \right] } } \\ { { \displaystyle \quad = - \frac { 4 \eta m } { R } \frac { m } { r } \cos \iota \sin 2 \phi . } } \end{array}
$$

It can also be shown that

$$
R _ { 0 j 0 k } = - \frac { 1 } { 2 } \frac { d ^ { 2 } } { d t ^ { 2 } } h _ { \mathrm { T T } } ^ { j k } ,
$$

and thus the amplitudes in Eqs. (11.42) and (11.48) are given by

$$
\begin{array} { l } { { \displaystyle { \cal A } _ { + } = - \frac { 2 \eta m ^ { 2 } } { r } ( 1 + \cos ^ { 2 } \iota ) \cos 2 \phi , } } \\ { { \displaystyle { \cal A } _ { \times } = - \frac { 4 \eta m ^ { 2 } } { r } \cos \iota \sin 2 \phi . } } \end{array}
$$

with $A _ { \mathrm { S } } = A _ { \mathrm { V } 1 } = A _ { \mathrm { V } 2 } = A _ { \mathrm { L } } = 0$ .

The foregoing discussion has been for the Newtonian waveforms and fluxes, but results are now known to many post-Newtonian orders beyond these lowest order formula. As an illustration, we show the rate of change of energy for a circular orbit through 2PN order:

$$
\begin{array} { c } { { \displaystyle \displaystyle \frac { d E } { d t } = - \frac { 3 2 } { 5 } \eta ^ { 2 } \left( \frac { m } { a } \right) ^ { 5 } \left[ 1 - \frac { m } { a } \left( \frac { 2 9 2 7 } { 3 3 6 } + \frac { 5 } { 4 } \eta \right) + 4 \pi \left( \frac { m } { a } \right) ^ { 3 / 2 } \right. } } \\ { { \displaystyle \left. + \left( \frac { m } { a } \right) ^ { 2 } \left( \frac { 2 9 3 3 8 3 } { 9 0 7 2 } + \frac { 3 8 0 } { 9 } \eta \right) \right] . } } \end{array}
$$

The 1PN corrections to the waveform and energy flux were calculated by Wagoner and Will (1976). The $1 . 5 \mathrm { P N }$ term $4 \pi ( m / a ) ^ { 3 / 2 }$ is the contribution of tails, the result of scattering of the outgoing gravitational wave off the background curved spacetime produced by the source. This and the 2PN terms were calculated by Blanchet et al. (1995a, 1995b) and Will and Wiseman (1996). Through pioneering work by Blanchet and collaborators, these results are now known through $3 . 5 \mathrm { P N }$ order (see Blanchet (2014) for an up-to-date review). The leading effects of spins of the bodies on the waveform and fluxes were first calculated by Kidder et al. (1993) and Kidder (1995) (see Section 6.7 for the leading contributions to the equations of motion). Numerous higher-order spin contributions have also been calculated (see Blanchet (2014) for a review and references).

# 11.5.3 Scalar-tensor theories

Because we are interested in gravitational waves from systems containing compact bodies, we will combine the “relaxed” or Landau-Lifshitz formulation of the scalar-tensor field equations developed in Section 5.3.2 with the modified EIH formalism described in Section 10.3.2.

The wave equation for the field $\tilde { h } ^ { \alpha \beta }$ in harmonic gauge has a form parallel to that of Eq. (11.87),

$$
\begin{array} { r } { \Pi \tilde { h } ^ { \alpha \beta } = - 1 6 \pi \tilde { G } \tilde { \tau } ^ { \alpha \beta } , } \end{array}
$$

where $\tilde { \tau } ^ { \alpha \beta } \ = \ ( - \tilde { g } ) ( \tilde { T } ^ { \alpha \beta } + \tilde { t } _ { \phi } ^ { \alpha \beta } + \tilde { t } _ { \mathrm { L L } } ^ { \alpha \beta } + \tilde { t } _ { \mathrm { H } } ^ { \alpha \beta } )$ and $\tilde { { \textbf { \textit { G } } } } = \ G / \phi _ { 0 }$ (see Section 5.3.2 for definitions). Recall that quantities with tildes are defined using the conformally transformed metric $\tilde { g } _ { \mu \nu } = ( \phi / \phi _ { 0 } ) g _ { \mu \nu } .$ . Because $\tilde { \tau } _ { , \beta } ^ { \alpha \beta } = 0$ by virtue of the gauge condition on $\tilde { h } ^ { \alpha \beta }$ , we can follow the same steps as for general relativity, Eqs. (11.88)–(11.90) to find, in the far zone, that

$$
\tilde { h } ^ { j k } = \frac { 2 \tilde { G } } { R } \frac { d ^ { 2 } } { d t ^ { 2 } } \int _ { \mathcal { M } } \tilde { \tau } ^ { 0 0 } \left( t - R , \pmb { x } ^ { \prime } \right) x ^ { \prime j } x ^ { \prime k } d ^ { 3 } x ^ { \prime } .
$$

To lowest PN order, $\begin{array} { r } { \tilde { \tau } ^ { 0 0 } = \rho ^ { * } = \sum _ { a } m _ { a } \delta ^ { 3 } ( { \pmb x } - { \pmb x } _ { a } ) } \end{array}$ , where $m _ { a }$ is the mass of each body evaluated for the asymptotic value $\phi _ { 0 }$ of the scalar field, and we obtain

$$
\tilde { h } ^ { j k } = \frac { 2 ( 1 - \zeta ) } { R } \ddot { I } ^ { j k } ( t - R ) ,
$$

where $I ^ { j k }$ is the quadrupole moment tensor of the source (see Eq. (11.91)), and we have used units in which $G _ { \mathrm { t o d a y } } = \tilde { G } / ( 1 - \zeta ) = 1$ . We now turn to the scalar wave equation in its relaxed, compact body form, Eq. (10.55b). To lowest PN order, it is straightforward