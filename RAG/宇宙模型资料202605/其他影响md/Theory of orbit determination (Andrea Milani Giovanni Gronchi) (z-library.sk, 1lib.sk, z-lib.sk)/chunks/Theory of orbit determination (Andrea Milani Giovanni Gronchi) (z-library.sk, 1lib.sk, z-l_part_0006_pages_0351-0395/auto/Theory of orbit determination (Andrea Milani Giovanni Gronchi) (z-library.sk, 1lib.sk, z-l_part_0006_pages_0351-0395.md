# 16.4 Resonant decomposition

To obtain the scientifically interesting results $\mathbf { g }$ , we need to compute $\Gamma _ { \bf g g } =$ $( C ^ { \bf g g } ) ^ { - 1 }$ , see eq. (15.4). To solve for coefficients up to a large degree, e.g., $\ell =$ 200, the matrix is still very large. Thus we want to decompose the problem into smaller ones; the solution of the normal equation (15.3) has to be found as the limit of a sequence of independent differential corrections for subsets of the $\mathbf { g }$ parameters. The simplest solution is solving for each coefficient independently of the others, that is approximating $C ^ { \mathrm { { g g } } }$ with a diagonal matrix: this would work if the observations were uniformly distributed on a sphere, so that the different harmonics would be orthogonal, see Section 13.3. This is not the case for any possible satellite orbit, as it is already clear from Figure 13.1: if the orbit has an inclination $I < 9 0 ^ { \circ }$ with respect to the equator, the polar caps with latitude $> I$ and $< - I$ are never overflown.10 It can be shown that indeed the spherical harmonics are not orthogonal over a latitude band (Albertella et al. 1999, Pail et al. 2001).

Colombo (1989) proposed that the normal matrix should be decomposed by the value of the harmonic order $m$ : the harmonics with the same $m$ share the same frequencies (13.37), thus they are more correlated. This could work, but something better is possible, by using the Kaula expansion of the geopotential perturbing function (Section 13.4) as a function of orbital elements. Let us suppose that the orbit of the gravimetric satellite is exactly resonant, in the sense of eq. (13.39), and that $e$ is small, thus we can neglect the $q \ne 0$ terms. Then the only frequencies in $U _ { \ell m }$ , as a function of time along the orbit, are: $\nu _ { \ell m p 0 } = \left[ \left( \ell - 2 p \right) j - m k \right] \mu$ . The same frequencies appear in all the partial derivatives of the potential, including the gradiometer observables; this follows from (13.24) and (13.25). Two harmonics $( \ell , m )$ and $( \ell ^ { \prime } , m ^ { \prime } )$ share some frequencies if and only if

$$
k m ^ { \prime } = \pm k m ( { \bmod { j } } ) ,
$$

a significant constraint, since for a low satellite $j$ is larger than $k$ by a factor $> 1 0$ . The signals from two harmonics with disjoint sets of frequencies are orthogonal over an infinite time span. Thus we can define a resonant decomposition: the harmonics are reordered by remainder class $r = \pm k m$ (mod $\jmath$ ), with $0 \leq r \leq j / 2$ , and the linear system (15.3) is

$$
( M - N ) \Delta \mathbf { g } = D \mathbf { g }
$$

where $M$ is the block diagonal part of $C ^ { \mathrm { { g g } } }$ , with off-diagonal terms only when row and column correspond to harmonics in the same remainder class. The blocks are larger than in the decomposition by $m$ , and still $M ^ { - 1 }$ can be computed block by block with acceptable computational load. In the assumptions (13.39), $e = 0$ , and an infinite observation time span, $N = { \bf 0 }$ . In practice, $N$ is not zero, because none of these assumptions applies exactly to a realistic case. If $N$ is smaller than $M$ , to solve the linear system (16.10) we can transform it into a fixed point problem (Bini et al. 1988, Section 5.2)

$$
M \Delta \mathbf { g } = N \Delta \mathbf { g } + D \mathbf { g } \Leftrightarrow \Delta \mathbf { g } = M ^ { - 1 } N \Delta \mathbf { g } + M ^ { - 1 } D \mathbf { g } = P \Delta \mathbf { g } + Q \mathbf { g }
$$

which can be solved by iteration

$$
\Delta ^ { ( 1 ) } { \bf g } = P \Delta ^ { ( 0 ) } { \bf g } + Q _ { \bf g } , ~ \Delta ^ { ( 2 ) } { \bf g } = P \Delta ^ { ( 1 ) } { \bf g } + Q _ { \bf g } , ~ \dots
$$

starting from an arbitrary initial guess $\Delta ^ { ( 0 ) } \mathbf { g }$ ; if, in some matrix norm, $| | P | | < 1$ , the sequence $\Delta ^ { ( k ) } \mathbf { g }$ converges to $\Delta ^ { * } \mathbf { g }$ solving the complete normal equation. For an initial guess $\Delta ^ { ( 0 ) } \mathbf { g } = \mathbf { 0 }$ , $\Delta ^ { ( 1 ) } \mathbf { g } = Q _ { \mathbf { g } } = M ^ { - 1 } D _ { \mathbf { g } }$ is the solution with approximate inversion, the first step of a convergent iteration.

For GOCE, the exact value of the semimajor axis was not yet known at the time of the simulation (ESA 1999, Section 6.2.4); it has been decided later, by selecting an optimal ground track repeat period $> 6 0$ days, thus a different resonant decomposition would be better. Anyway, a decomposition corresponding to a resonance not too close to the nominal one, that is $j =$ 31, $k = 2$ , has been used to test the robustness of the method. The upper part of Figure 16.2 shows the results for the gravity coefficients, and their covariance, for the remainder class $r = 1$ , which includes $m = 1 5 , 1 6 , \dots$ .

The norm of $P$ is small because the off-block correlations are small, but there is no quantitative estimate, thus we cannot predict how many iterations would be necessary for satisfactory convergence. In (Milani et al. 2005d) there is a numerical test of the second iteration $\Delta ^ { ( 2 ) } g$ : this is possible only after a complete first iteration, 16 separate differential corrections with $r = 0 , 1 , \ldots , 1 5$ , by performing a second iteration for some remainder class. The upper plot of Figure 16.2 shows both the result of the first and the second iteration, and the two curves are so close that most points are superimposed. Albertella and Migliaccio (1998, Section 3.5.2) report another numerical test computing explicitly, for the accelerometer mission case, the off-block correlations and showing that they are $< 0 . 0 1$ .

# 16.5 Polar gaps

In a solution for the geopotential coefficients up to a large degree $\ell _ { m a x }$ , after controlling the local–global correlations (with an appropriate minimum degree $\ell _ { m i n }$ ), and after decomposing the normal matrix of the global parameters $C ^ { \mathrm { { g g } } }$ (see the previous section), some diagonal blocks are still very badly conditioned. As an example, in Figure 16.2, lower panel, we show the results for the remainder class $r = 0$ in a solution for $2 5 \leq \ell \leq 2 0 0$ . The bulge in both the formal uncertainty, and in the actual error corresponds to very high correlations among the zonal spherical harmonics. The error/signal ratio reaches $\simeq 1$ around $\ell = 1 0 0$ , unlike the $r = 1$ case of the upper plot. The analogous figure for $\ell _ { m a x } = 9 0$ would show a much lower bulge.

![](images/3659a801e7d53ec52604764a76c6299e3f931b3b302b0f8039a76ad313b38821.jpg)  
Fig. 16.2. We plot as a function of the degree $\ell$ : the gravity field signal (Lemoine et al. 1998), the approximating Kaula rule, the formal uncertainty, and the actual error (estimate minus “true” value used in the data simulation). Above: for the remainder class $r = 1$ ; the actual error is shown for the first and the second iteration; the two curves are almost superimposed. Below: for the $r = 0$ class, including the zonals, there is a large bulge such that both the formal and the actual errors exceed the signal for degree $\ell > 1 0 0$ . Reproduced with permission of Springer from Milani et al. (2005d).

Large RMS (and actual errors) occur in this remainder class only for the zonals with $m \ = \ 0$ ; the other harmonics, with $m = { \ o { 3 1 } } , 6 2 , . . .$ , are determined with error/signal ratio well below 1 for all $\ell$ . The correlations are significant only among the zonals, e.g., the $\ell = 1 5 0$ zonal has significant correlations with all the even zonals, correlation 0.9999 with the $\ell = 1 4 8$ , and the $\ell = 1 5 2$ one. This is clear from the frequency analysis: for $m = 0$ , low $e$ , $\nu _ { l 0 p 0 } = ( \ell - 2 p ) ( n + \dot { \omega } )$ , hence the highly correlated zonals share the same frequencies, consecutive even (or odd) $\ell$ have only one frequency not in common; in any case zonal harmonics with the same parity have some frequencies in common, and are correlated.

Similar results are obtained for the remainder classes containing harmonics with low $m$ : e.g., for $r = 2$ , that is for $m = 1 , 2 9 , 3 3 , . . .$ the error-tosignal ratio reaches 1 around $\ell = 9 0$ . For $m = 7$ the formal and actual error curves still show the bulge at intermediate degrees, but the error-to-signal ratio is below 1. These difficulties with the low $m$ coefficients in GOCE were known, by the designers of the mission (Aguirre-Martinez and Sneeuw 2003, Figure 4), to be due to the polar gaps; the non-polar orbit of GOCE has ground tracks with latitude neither above $\simeq 8 3 . 5 ^ { \circ }$ nor below $- 8 3 . 5 ^ { \circ }$ .

# Principal components analysis

Given the covariance matrix $\Gamma _ { \mathbf { g } \mathbf { g } }$ , or at least one of the blocks $1 _ { \mathbf { g } \mathbf { g } } ^ { \scriptscriptstyle \prime }$ of the resonant decomposition, we can perform a principal components analysis. Let $\lambda _ { 1 } > \lambda _ { 2 } > \cdots > \lambda _ { s }$ be the square roots of the eigenvalues of $1 _ { \mathbf { g } \mathbf { g } } ^ { \prime \prime }$ .

The corresponding unit eigenvectors $V _ { j } , j = 1 , \ldots , s$ , contain harmonic coefficients and can be interpreted as gravity anomalies. For the $r = 0$ block $\lambda _ { 1 }$ , $\lambda _ { 2 }$ are not very different and significantly larger than $\lambda _ { 3 }$ ; in $V _ { 1 }$ , $V _ { 2 }$ the components corresponding to harmonics with $m \neq 0$ are very small $( < 1 0 ^ { - 4 }$ ), thus the harmonic functions with coefficients $\lambda _ { 1 } ~ V _ { 1 }$ and $\lambda _ { 2 } V _ { 2 }$ are essentially zonal harmonics, functions of latitude, e.g., in Figure 16.3 they are represented as anomalies of the geoid. The anomalies are concentrated on the two polar caps: $\lambda _ { 1 } \ : V _ { 1 }$ more pronounced on the South pole, $\lambda _ { 2 } V _ { 2 }$ on the North pole. The size of the anomalies is huge with respect to the target accuracy of GOCE, up to $\simeq 2 0 \textup { m }$ on the poles; to understand this, it is enough to compute one of the GOCE observables, e.g., the radial component of the gravity gradient, for the anomalies $\lambda _ { 1 } ~ V _ { 1 }$ and $\lambda _ { 2 } V _ { 2 }$ . Although the undetermined anomalies are not only on the polar caps, the signal for latitudes between $- 8 3 . 5 ^ { \circ }$ and $+ 8 3 . 5 ^ { \circ }$ is well below the noise of the GOCE measurements.

![](images/c6a43c2fbceda800cf268fb535ca57b4aaead3169147f84087af1b8c7b72188f.jpg)  
Fig. 16.3. The gravity anomalies corresponding to the two principal axes of the confidence ellipsoid (for $\sigma = 1$ ) represented by the corresponding geoid anomalies, as a function of latitude. The vertical lines bound the latitude band covered by GOCE, the horizontal line is at $1 ~ \mathrm { c m }$ . Reproduced with permission of Springer from Milani et al. (2005d).

# Symmetry and degeneration

Why are the undetermined anomalies as large as shown in Figure 16.3, and why does the situation become worse as the solution is pushed to higher $\ell$ ?

Typically, the origin of an approximate rank deficiency is due to a “nearby” exact rank deficiency, in turn connected to a number of exact symmetries, see Section 6.3. When the symmetries are broken, approximate symmetries remain, and they result in an approximate rank deficiency.

The case of a gradiometer mission is somewhat more complicated, because the symmetry group is an infinite dimensional subspace of harmonic functions. Its existence can be proven by selecting, on the sphere of radius $R _ { \oplus } + h$ , an arbitrary smooth $( C ^ { \infty } )$ function $\Phi$ with support in the polar caps (e.g., the function is exactly zero for $- 8 3 . 5 ^ { \circ } <$ < latitude $< 8 3 . 5 ^ { \circ }$ ). By the solution of the exterior Dirichlet problem given in Section 13.3, there is a harmonic function for geocenter distance $> R _ { \oplus } + h$ and coinciding with $\Phi$ on the sphere of radius $R _ { \oplus } + h$ . Such a function may not exist on the sphere of radius $R _ { \oplus }$ because the downward continuation may well be divergent; that is, it does not need to be a “realistic” gravity anomaly.

If we take the approximation that the satellite flies at an exactly constant altitude, then the gradiometer is measuring the second derivatives where $\Phi$ is zero. In this approximation there would be an exact symmetry. This symmetry is broken for two reasons: first, the altitude is not constant, although the eccentricity is small ( $e < 0 . 0 0 4 5$ for GOCE). Second, the harmonic function we are trying to fit to the gradiometer data is the sum of only a finite number of harmonics, with limited degree $\ell \leq \ell _ { m a x }$ . The cap function $\Phi$ cannot have a finite spherical harmonic expansion, because it is not an analytic function. If $\Phi$ is expanded in a series of spherical harmonics, the series is convergent on the sphere. When this series is truncated to degree $\ell _ { m a x }$ , the remainder is small on the latitude band where $\Phi$ is zero, with maximum $ 0$ for $\ell _ { m a x } \to + \infty$ . This is what is shown in Figure 16.3: the observable signal is not zero but very small. Thus as $\ell _ { m a x }$ increases the observable signal becomes smaller and smaller, and the bulge becomes more pronounced. At the limit for $\ell _ { m a x } \to + \infty$ the undetermined geoid anomaly on the sphere of radius $R _ { \oplus }$ might be arbitrarily large.

# Outside the polar caps

On a block of harmonics not including low $m$ ones the polar gaps have little effect: e.g., for $r = 1$ , Figure 16.2, above. The actual error is larger than the formal one, but the ratio does not exceed 4 (and is $\leq 2$ for most orders $\ell$ ). Both the formal and actual error are well below the signal up to $\ell _ { m a x } = 2 0 0$ , and it is possible to solve harmonics with signal-to-ratio $\geq 1$ up to $\ell _ { m a x } = 2 2 0 { - } 2 3 0$ . Figure 16.3 suggests a positive interpretation of the polar gaps effects: the undetermined gravity anomalies are concentrated on the polar caps, e.g., the geoid anomalies are at the mm level in the “overflown region”, the latitude band of the ground tracks. The harmonics up to $\ell _ { m a x } = 2 2 0$ cannot all be determined, but the gravity in the overflown region can be determined down to a spatial scale of $\pi R _ { \oplus } / 2 2 0 \simeq 9 1 { \mathrm { ~ k m } }$ .

Even in the overflown region the solution is reliable only provided there is no aliasing between spurious signals and the gravity signal. To detect such an aliasing, we analyze the specific harmonics where the largest actual/formal error ratio holds. For example, for the remainder class $r = 7$ (Figure 16.4) the actual error grows significantly for $\ell > 1 6 0$ . Among the harmonics in this block, those with $m = 1 6 7$ show a particularly high actual error. The spurious signal with frequency $f = 1 / 1 0 0 0 ~ \mathrm { H z }$ introduced in the simulation, and not removed by the calibration fit because $f > f _ { c }$ , is responsible for this behavior. Looking for gravity field signals with similar frequencies, we find, e.g., that for $l - 2 p = - 5 , m = 1 6 7$ the frequency $\nu _ { l m p 0 }$ corresponds to a period of 990 s; for $l - 2 p = - 1 9 , m = 1 6 7$ the frequency is negative, with a period of 957 s.

![](images/d8907c49863fb50c45a4795b384bad41ba3e49eed1fb40ad5534a19816c83954.jpg)  
Fig. 16.4. For the $r = 7$ remainder class the formal and actual errors are compared with the signal. The harmonics with $\ell > 1 6 0$ cannot be determined with a signal/error ratio $> 1$ . Reproduced with permission of Springer from Milani et al. (2005d).

# Limitations of gravimetry missions

The main general conclusion we can draw from this case study is that each gravimetry mission has some limitations, due to the performance of the instruments and to the orbit: in the case of GOCE, these limitations could be summarized as follows. First, if the orbit does not cover the entire surface with the ground track, then it is not possible to accurately solve for all the spherical harmonics up to some high degree. Nevertheless, in the overflown region the results can be accurate down to a short spatial scale.

Second, given the noise model, the formal error deduced from the covariance matrix $\Gamma _ { \mathbf { g } \mathbf { g } }$ sets an upper bound for the degree $\ell$ to be determined, where it exceeds the signal: for GOCE this occurs for $\ell \simeq 2 3 0$ . Since this value is obtained in the optimistic assumption that the systematic errors are zero, this upper bound does not depend upon the orbit determination method used, but only on the specifications for the measurement noise.

Third, if in the intermediate frequency band there are spurious systematic signals, they can alias with gravity signals. The period 1000 s for the spurious signal is arbitrary, but any period in that band would affect some harmonics. Sometimes a numerical simulation has to be used to convince the skeptics, even though a back of the envelope computation could be enough. The frequencies $\nu _ { \ell m p 0 }$ for $\ell \leq 2 0 0$ are $\simeq 4 0 0 0 0$ ; to invent some spurious signal without frequencies close to some harmonic would be a difficult task. Thus each spurious signal generates a wrong value for some harmonics, with an actual error significantly larger than the formal one, an illusory result limited to a few coefficients.

# 16.6 Satellite-to-satellite tracking

A satellite-to-satellite tracking mission uses two spacecraft, in low Earth orbits, and relative tracking data between the two, such as range and/or range-rate. The main choice in mission design is to decide the distance $d$ between the two, and how tightly to control it. For a target minimum spatial scale $L = \pi R _ { \oplus } / \ell _ { m a x }$ , at short distances $d \ll L$ the measurement has the same information content as a gradiometer (16.7), although the data processing is somewhat more complex (see below). The short distance allows us to use a relative tracking method sensitive to distance and insensitive to the atmospheric propagation disturbances, but requires a drag free system.

If $d \simeq L$ the orbit control requirement is weaker: this has been the choice of the NASA mission GRACE (Tapley et al. 2005), launched in 2002. The two spacecraft are allowed to decay because of drag, sporadic orbit maneuvers controlling the distance between $\simeq 1 2 0$ and $\simeq 2 7 0$ km. The difficulty is to model with the required accuracy the propagation of radio waves: GRACE has a complex multifrequency link between the two spacecraft.

In any case, for an Earth gravimetry mission, an accelerometer is required on both spacecraft: apparent forces and calibration are a problem as they are for an accelerometer mission. Around the Moon this is not necessarily the case. The MORO lunar mission study of the European Space Agency (Coradini et al. 1996) proposed to measure the range-rate to a simple lunar subsatellite released from the main polar orbiter (Milani et al. 1996). The sensitivity to the lunar gravity field can be good, down to a scale $\simeq 1 0 0$ km, with orbital height $h \simeq 1 0 0 ~ \mathrm { k m }$ , which can be maintained even without propulsion (Kneˇzevi´c and Milani, 1998). The problem of the sectorial weakness (see below) was discussed in the MORO study. The Japanese lunar mission KAGUYA, launched in 2007, has implemented another version of the subsatellite concept, using VLBI differential measurements from Earth.

# Laser Doppler interferometry for gravimetry

We shall use as an example of satellite-to-satellite tracking the LDIM study commissioned by the European Space Agency to Thales Alenia Spazio, for a long-duration Earth gravimetry mission (Cesare et al. 2005, Cesare et al. 2006). This study selects laser interferometry to generate extremely accurate measurements of changes in the distance between reference points on the two spacecraft, at a distance $d \simeq 1 0$ km. This distance gives good sensitivity to harmonics with degree up to $\ell _ { m a x } \simeq 2 0 0$ , because $d / L \simeq 1 / 1 0$ , where $L \simeq 1 0 0$ km is the spatial scale. An accelerometer with a measurement band between 1/1000 Hz and $1 / 1 0 0 \mathrm { H z }$ and noise spectral density $S ( f )$ comparable to the units on GOCE is assumed; for the accelerometer and interferometers performances in measuring differences of accelerations see (Cesare et al. 2006, Figure 2). The selected altitude $h = 3 2 5$ km is maintained with an ion thruster, providing drag free control and relative distance control. The two spacecraft maintain a constant attitude in the $( \hat { \mathbf { r } } , \hat { \mathbf { t } } , \hat { \mathbf { w } } )$ orbit frame of Section 14.1, and are separated in the $\hat { \mathbf { t } }$ direction.

Given the preliminary nature of such a study, only a simplified orbit determination simulation was included, $_ { 1 1 }$ for a six month mission segment, to assess how small changes in the geopotential, with periods $\geq 1$ year, can be measured. The observations were simulated as gradiometer measurements, an approximation with small parameter $d / r \simeq 1 . 5 \times 1 0 ^ { - 3 }$ .

The orbit inclination was constrained by the requirement of a Sun synchronous orbit (with period of the node equal to one year, to simplify the thermal control) to $I = 9 6 . 8 ^ { \circ }$ . As a consequence the polar gaps effects were comparable to those found for GOCE and discussed in Section 16.5: see (Cesare et al. 2005, Figures 4.2–5, 4.2–6). To summarize the results as a function of degree $\ell$ we have separated the harmonics with $m \le 1 5$ , for which there was a significant bulge, in Figure 16.5, which looks like the superposition of the two plots of Figure 16.2. This was the LDIM goal, to achieve results comparable to GOCE from a higher orbit, with two smaller spacecraft, which could avoid orbit decay for more than five years.

![](images/1028a53802293dea28f8ffbeb8af38ecd5b5326e44eb4579efbb9b6f9296d408.jpg)  
Fig. 16.5. Signal and different estimates of the error as a function of the harmonic degree $\ell$ . From top to bottom on the left: Kaula rule and actual signal (Lemoine et al. 1998); actual and formal error for $m \le 1 5$ , actual and formal error for $m > 1 5$ .

However, there is an interesting difference. If we show the results for each individual harmonic coefficient $C _ { \ell m }$ , $S _ { \ell m }$ in a representation with the low $m$ near the axes and low $\ell - m$ near the diagonal as in Figure 16.6, the two “ears” on the sides show the effects of the polar gaps, the ridge in the middle indicates the presence of another weakness of the solution, although not quite a rank deficiency; the increase in the noise for the sectorial spherical harmonics, with $\ell = m$ , is just by a factor $\simeq 1 0$ .

Still it is possible to find a nearby exact symmetry, because the only component of $\partial ^ { 2 } U / \partial \mathbf { x } ^ { 2 }$ which can be measured is the one in the direction $\hat { \mathbf { t } }$ . If the orbits were exactly polar, all the derivatives of the sectorial harmonics with respect to the latitude would be zero: $P _ { \ell \ell } = c o n s t$ . Since $\pi / 2 { - } I \simeq 1 / 1 0$ rad, the weakness is not important in the results. It is important to remind us that there is no ideal orbit allowing a perfect gravity field solution; if the orbit was closer to polar, the polar gap would be smaller and the bulge less pronounced, but the sectorial weakness could become a problem.

![](images/53e75ad739aec46852e2146899fc01340ca7e1f75a86ce99b4b382cc73dbdf00.jpg)  
Fig. 16.6. For each harmonic $\ell , \ m$ the smooth noise/signal computed as formal RMS divided by the value suggested by the Kaula rule. In the horizontal plane, the two coordinates are $( \ell , m )$ for $C _ { \ell m }$ and $( m , \ell )$ for $S _ { \ell m }$ .

# The numerical precision requirements

There is a specific additional problem in the satellite-to-satellite tracking missions, not fully addressed by the first LDIM study, namely the numerical precision of the orbit. With laser interferometry, the sensitivity $\Delta d$ to changes in the distance $d$ between the two spacecraft could be as small as $1 0 ^ { - 7 }$ cm. With $r \simeq 6 . 7 \times 1 0 ^ { 8 }$ cm, we have $\Delta d / r \simeq 1 . 5 \times 1 0 ^ { - 1 6 }$ . If the two orbits computed separately are $\mathbf { x } _ { 1 }$ and $\mathbf { x } _ { 2 }$ , in computing $d = | \mathbf { x } _ { 1 } - \mathbf { x } _ { 2 } |$ the components of the difference vector are differences between two large numbers. This implies that rounding off is a problem with current computers, supporting in hardware only a mantissa of 53 bits, thus with relative rounding off error $2 ^ { - 5 2 } = 2 . 2 \times 1 0 ^ { - 1 6 }$ . Extended precision is supported in software, but this significantly increases the computational load. There are ways to use extended precision only for some of the computations, not including the spherical harmonic expansion of the gravity fields and its derivatives.

# 17

# ORBITERS AROUND OTHER PLANETS

BepiColombo is a European Space Agency mission to be launched in 2014, with the goal of an in depth exploration of the planet Mercury. This chapter contains a case study: the orbit determination for this mission, including the techniques to be used for both the simulations and the real data processing. Some tools not yet described in this book will be developed, such as the light time and range-rate implicit equations, the equations for the rotation of the planet, etc. This chapter is based on our papers (Milani et al. 2001b, Milani et al. 2002) and on ongoing research.

# 17.1 Science goals for an orbiter around Mercury

In a first exploration of a planet, every piece of information which can be gathered is valuable, starting from the first close up images. Mercury was visited by the NASA Mariner 10 probe, with three flybys1 in 1974–1975. With these short visits, the orbit determination of Mariner 10 provided estimates of the harmonic coefficients $\overline { { C } } _ { 2 0 } \simeq - 2 . 6 8 { \times } 1 0 ^ { - 5 }$ , $\overline { { C } } _ { 2 2 } \simeq 1 . 5 5 { \times } 1 0 ^ { - 5 }$ (Anderson et al. 1987) and gave evidence of a bipolar magnetic field.

Further exploration of a planet needs to follow a very different logic. Scientists would like to define a set of science goals and then obtain from the space agencies the resources to achieve them, but this is not really possible. The science goals have to be limited to what is affordable, taking into account how expensive are the resources, such as the mass, the power, the data rate and the thermal control, when deployed around another planet. The experiments are limited by the available technology, also taking into account the need for extreme miniaturization.

A window of opportunity was opened for the BepiColombo mission with the proposal (Iess and Boscagli 2001) of including a two-frequency radio system, with transponders for both the X and the Ka band. With a five-way link between the spacecraft and the ground antenna it is possible to eliminate almost completely the uncertainty on the speed of the radio waves, which is lower than the speed of light because of the plasma content along their path. This is possible even for radio wave paths passing comparatively close to the Sun, down to a few Sun radii.

Then the question has to be reversed: which scientific goals can be achieved with such good quality of tracking data, and which are the additional requirements to fully exploit the extraordinary accuracy possible in the measurements of both range and range-rate to a Mercury orbiter. The possible fields of scientific interest are two. First, geophysics, with the study of the internal structure of the planet, including the core, the mantle, and the source of the bipolar magnetic field. Second, the theory of gravitation, since Mercury is a probe going into the gravity potential well of the Sun deeper than any other body large enough not to be affected significantly by non-gravitational perturbations (see Section 4.6).

# Geophysics of Mercury

It is possible to determine the gravity field of Mercury from the orbit determination of a satellite of that planet; the question is how far we can go with the degree and order of the spherical harmonics. The problem, as discussed in Section 13.2, is that the gravity field outside a planet, as represented in (exterior) spherical harmonics, does not uniquely constrain the internal mass distribution. In particular the degree 2 harmonics are five, and there is a linear relationship with the six coefficients of the inertia quadratic form, resulting in one free parameter which may be expressed as the concentration coefficient $C / ( M R ^ { 2 } )$ , where $C$ is the maximum moment of inertia. This makes it difficult to constrain the size of the core of Mercury by gravimetry.

Moreover, the static gravity field alone does not constrain the physical state of the interior layers, such as the outer core. On the Earth, the outer core is liquid (as established with seismic wave analysis) and it is believed to be the source of the Earth’s bipolar magnetic field, through a dynamo effect. If Mercury had no liquid layer the dynamo theory could be challenged.

Both the presence of a liquid layer and the size of the core can be investigated by constraining the rotation state of the planet. Also the timedependent part of the gravity field of Mercury, that is the response of the planet’s gravity to the tides raised by the Sun, can be used as a constraint.

The rotation state of the planet can be measured by comparing images of the same area on the planet taken at different times, see Section 17.4. The question is how accurately it is possible to measure the harmonic coefficients (as a function of the degree $\ell$ ), the tidal response of the planet, and the rotation state, given the technology practically available around Mercury.

# Theory of gravitation

The parametric post-Newtonian approach, outlined in Section 6.6, allows us to describe a number of theoretically interesting violations of the current theory of gravitation, namely general relativity, and other interesting astrophysical phenomena by a set of parameters such as $\gamma , \beta , \eta , \alpha _ { 1 } , \alpha _ { 2 } , \zeta , J _ { 2 \odot }$ . Of course these parameters can be determined only within an orbit determination procedure solving also for the initial conditions of Mercury and of the Earth. The question is how accurate can the solution be for the post-Newtonian parameters, given the accuracy and time distribution of the tracking data. If the constraints on the possible violations of general relativity can be significantly improved with respect to all the other available experimental constraints, this will become a very important experiment.2

# 17.2 Interplanetary tracking

The observables are the distance $r$ between the ground antenna and the spacecraft, and its time derivative $\dot { r }$ . They can be computed from solutions for the motion of five different state vectors

$$
r = \left| ( \mathbf { x } _ { s a t } + \mathbf { x } _ { M } ) - ( \mathbf { x } _ { E M } + \mathbf { x } _ { E } + \mathbf { x } _ { a n t } ) \right| + S ( \gamma )
$$

where $\mathbf { x } _ { s a t }$ is the Mercury-centric position of the orbiter, $\mathbf { x } _ { M }$ is the Solar System barycentric position of the center of mass of Mercury, $\mathbf { x } _ { E M }$ is the position of the Earth–Moon center of mass in the same reference system, $\mathbf { x } _ { E }$ is the vector from the Earth–Moon barycenter to the center of mass of the Earth, and ${ \bf x } _ { a n t }$ is the position of the ground antenna center of phase with respect to the center of mass of the Earth.

$S ( \gamma )$ is the Shapiro effect, the difference between distance in a flat space and the geodesic length in curved space-time, depending upon the post-Newtonian parameter $\gamma$ . Thus the distinction between dynamical and kinematical parameters, introduced in Chapter 1, is not sharp, because $\gamma$ appears in the observation equation (17.1) and also in the relativistic dynamics, see Section 6.6. If the distance is measured by light-time, the flat-space distance of two heliocentric vectors $\mathbf { r } _ { 1 } , \mathbf { r } _ { 2 }$ has to be corrected by (Moyer 2003)

$$
S ( \gamma ) = \frac { ( 1 + \gamma ) G m _ { 0 } } { c ^ { 2 } } \log \left[ \frac { r _ { 1 } + r _ { 2 } + r _ { 1 2 } } { r _ { 1 } + r _ { 2 } - r _ { 1 2 } } \right] ,
$$

where the vectors $\mathbf { r } _ { 1 }$ and $\mathbf { r } _ { 2 }$ correspond to the vectors ${ \bf x } _ { E M } + { \bf x } _ { E } + { \bf x } _ { a n t }$ and $\mathbf { x } _ { s a t } + \mathbf { x } _ { M }$ , but they have to be converted to a heliocentric frame, which is moving with the velocity $\dot { \mathbf { x } } _ { \odot }$ of the Sun, thus a relativistic coordinate transformation needs to be applied. The length $r _ { 1 2 }$ is similarly converted from the $r$ of eq. (17.1). This conversion introduces a number of small terms of post-Newtonian order $> 1$ which may be observable, given the very high signal-to-noise in the range. Other terms relevant for the level of accuracy of this experiment appear in the denominator inside the logarithm: when the radio waves are passing near the Sun, at just a few solar radii, even corrections of the order of $G M _ { \odot } / c ^ { 2 } \simeq 1 . 5 \mathrm { k m }$ have to be computed, although they introduce a correction to $S ( \gamma )$ which is of post-Newtonian order 2.

The five vectors of (17.1) have to be computed at the epoch of different events, e.g., $\mathbf { x } _ { a n t }$ , $\mathbf { x } _ { E M }$ , and $\mathbf { x } _ { E }$ are to be considered at both the antenna transmit time $t _ { t }$ and the receive time $t _ { r }$ of the signal. $\mathbf { x } _ { M }$ and $\mathbf { x } _ { s a t }$ are computed at the bounce time $t _ { b }$ , when the signal has arrived at the orbiter and is sent back, with corrections for the delay of the transponder. Thus there are two different light-times, the up-leg $\Delta t _ { u p } = t _ { b } - t _ { t }$ for the signal from the antenna to the orbiter, and the down-leg $\Delta t _ { d o } = t _ { r } - t _ { b }$ for the return signal. Given the down-leg and up-leg distances

$$
\begin{array} { l c l } { \mathbf { r } _ { d o } ( t _ { r } ) } & { = } & { \mathbf { x } _ { s a t } ( t _ { b } ) + \mathbf { x } _ { M } ( t _ { b } ) - \mathbf { x } _ { E M } ( t _ { r } ) - \mathbf { x } _ { E } ( t _ { r } ) - \mathbf { x } _ { a n t } ( t _ { r } ) } \\ { r _ { d o } ( t _ { r } ) } & { = } & { | \mathbf { r } _ { d o } ( t _ { r } ) | + S _ { d o } ( \gamma ) } \\ & & { } \\ { \mathbf { r } _ { u p } ( t _ { r } ) } & { = } & { \mathbf { x } _ { s a t } ( t _ { b } ) + \mathbf { x } _ { M } ( t _ { b } ) - \mathbf { x } _ { E M } ( t _ { t } ) - \mathbf { x } _ { E } ( t _ { t } ) - \mathbf { x } _ { a n t } ( t _ { t } ) } \\ { r _ { u p } ( t _ { r } ) } & { = } & { | \mathbf { r } _ { u p } ( t _ { r } ) | + S _ { u p } ( \gamma ) } \end{array}
$$

with somewhat different Shapiro effects $S _ { d o } , S _ { u p }$ ; by definition of distance in a relativistic space-time the light-times are $\Delta t _ { d o } = r _ { d o } / c$ and $\Delta t _ { u p } = r _ { u p } / c$ respectively. If the measurement is labeled with the receive time $t _ { r }$ , the iterative procedure needs to start from eq. (17.2) by computing the states $\mathbf { x } _ { E M }$ , $\mathbf { x } _ { E }$ , and $\mathbf { x } _ { a n t }$ at epoch $t _ { r }$ , then selecting a rough guess $t _ { b } ^ { 0 }$ for the bounce time.3 Then the states $\mathbf { x } _ { s a t }$ and $\mathbf { x } _ { M }$ are computed at $t _ { b } ^ { 0 }$ and a first guess $r _ { d o } ^ { 0 }$ is given by (17.2)eated computing This allows a better estimate , and so on until convergence, $t _ { b } ^ { \mathrm { l } } = t _ { r } - r _ { d o } ^ { \mathrm { 0 } } / c$ $r _ { d o } ^ { 1 }$ $r _ { d o } ^ { k } - r _ { d o } ^ { k - 1 }$ is smaller than the required accuracy.

After accepting the last value of $t _ { b }$ and $r _ { d o }$ we start with the states $\mathbf { x } _ { s a t }$ and $\mathbf { x } _ { M }$ at $t _ { b }$ and with a rough guess $t _ { t } ^ { 0 }$ for the transmit time.4 Then $\mathbf { x } _ { E M }$ , $\mathbf { x } _ { E }$ , and $\mathbf { x } _ { a n t }$ are computed at epoch $t _ { t } ^ { 0 }$ and $r _ { u p } ^ { 0 }$ is given by eq. (17.3); then $t _ { t } ^ { 1 } = t _ { b } - r _ { u p } ^ { 0 } / c$ and the same procedure is iterated to convergence, that is to achieve a small enough $r _ { u p } ^ { k } - r _ { u p } ^ { k - 1 }$ − rk−1up . Then the two-way range is just rup + rdo; a one-way range can be conventionally defined as $r ( t _ { r } ) = ( r _ { u p } + r _ { d o } ) / 2$ .

The iterative procedure above is also used for planetary radar to a natural body, such as an asteroid (Yeomans et al. 1992), in which case stateof-the-art accuracies can be $\simeq 5 0 ~ \mathrm { m }$ in range and $\simeq 4 ~ \mathrm { m m / s }$ in range-rate. With an active transponder, and using higher frequencies, the accuracies can now be $> 1 0 0$ times better, and this implies that also post-Newtonian corrections of order 1 need to be taken into account. Thus we need to add to (17.2) and (17.3) relativistic corrective terms $\Delta _ { d o } , \Delta _ { u p }$ accounting for the different time coordinates; see an example in the next section.

The instantaneous range-rate is computed with the unit vectors $\hat { \mathbf { r } } _ { u p }$ and $\hat { \mathbf { r } } _ { d o }$ , e.g. down-leg

$$
\dot { r } _ { d o } ( t _ { r } ) = \hat { \mathbf { r } } _ { d o } \cdot \dot { \mathbf { r } } _ { d o } + \dot { S } _ { d o } ( \gamma ) .
$$

The problem is the computation of $\dot { \mathbf { r } } _ { d o }$ . A first approximation can use the velocities for each of the five position vectors, at the same times $t _ { r }$ and $t _ { b } , t _ { t }$ obtained at convergence of the two light-time iterations

$$
\dot { \bf r } _ { d o } = ( \dot { \bf x } _ { s a t } + \dot { \bf x } _ { M } ) - ( \dot { \bf x } _ { E M } + \dot { \bf x } _ { E } + \dot { \bf x } _ { a n t } ) .
$$

However, this neglects the fact that $t _ { b } , t _ { t }$ depend on $t _ { r }$ also through $r _ { d o } , r _ { u p }$

$$
\frac { d t _ { b } } { d t _ { r } } = 1 - \frac { \dot { r } _ { d o } } { c } + \frac { d \Delta _ { d o } } { d t _ { b } } , \frac { d t _ { t } } { d t _ { r } } = 1 - \frac { \dot { r } _ { d o } } { c } - \frac { \dot { r } _ { u p } } { c } + \frac { d \Delta _ { d o } } { d t _ { b } } + \frac { d \Delta _ { u p } } { d t _ { b } }
$$

and the corresponding corrections to $\dot { \mathbf { r } } _ { d o }$

$$
\dot { \bf r } _ { d o } = \left( \dot { \bf x } _ { s a t } + \dot { \bf x } _ { M } \right) \left( 1 - \frac { \dot { r } _ { d o } } { c } + \frac { d \Delta _ { d o } } { d t _ { b } } \right) - \left( \dot { \bf x } _ { E M } + \dot { \bf x } _ { E } + \dot { \bf x } _ { a n t } \right)
$$

are large with respect to the Doppler measurement accuracy, the first term being $\mathcal { O } ( \dot { r } / c )$ ; the one due to $\Delta _ { d o } ( t c )$ is smaller, but still significant. Thus the improved value of $\dot { \mathbf { r } } _ { d o }$ has to be inserted in eq. (17.4), the correction (17.5) recomputed, and so on until convergence of the value $\dot { r } _ { d o }$ . Similarly, an iteration loop is necessary for $\dot { r } _ { u p } ( t _ { r } )$ . Note that also the computation of $\dot { S } _ { d o } ( \gamma ) , \dot { S } _ { u p } ( \gamma )$ requires corrections $\mathcal { O } ( \dot { r } / c )$ .

4 $t _ { t } ^ { 0 } = t _ { b } - ( t _ { r } - t _ { b } )$ is good enough.

Conventionally, $\dot { r } ( t _ { r } ) = ( \dot { r } _ { u p } ( t _ { r } ) + \dot { r } _ { d o } ( t _ { r } ) ) / 2$ is the instantaneous value. However, the measurement is not instantaneous: an accurate measure of the Doppler effect requires us to fit the difference in phase between carrier waves, the one generated at the station and the one returned from space, accumulated over some integration time $\Delta$ , typically between 10 and 1000 s. Thus the observable $\dot { r }$ is really obtained from a difference of ranges

$$
\frac { r ( t _ { b } + \Delta / 2 ) - r ( t _ { b } - \Delta / 2 ) } { \Delta } = \frac { 1 } { \Delta } \int _ { t _ { b } - \Delta / 2 } ^ { t _ { b } + \Delta / 2 } \dot { r } ( s ) d s
$$

or, equivalently, an averaged value of range-rate over the integration interval, which can be computed with a quadrature formula (see Appendix B).

The computation of the observables, as presented in this section, is already complex, but still the list of subtle technicalities is not complete. To understand the computational difficulty we need to take into account also the orders of magnitude. For state-of-the-art tracking systems, such as those using a multifrequency link in the X and Ka bands, the accuracy of the range measurements can be $\simeq 1 0$ cm and that of the range-rate $3 \times 1 0 ^ { - 4 }$ cm/s (over an integration time of 1000 s). Let us take an integration time $\Delta = 3 0$ s, which is adequate for measuring the gravity field of Mercury.5

The accuracy over 30 s of the range-rate measurement can be, by Gaussian statistics, $\simeq 3 \times 1 0 ^ { - 4 } ~ \sqrt { 1 0 0 0 / 3 0 } \simeq 1 7 \times 1 0 ^ { - 4 } ~ \mathrm { c m / s }$ , and the required accuracy in the computation of the difference $r ( t _ { b } + \Delta / 2 ) - r ( t _ { b } - \Delta / 2 )$ i s $\simeq 0 . 0 5$ cm. The distances can be as large as $\simeq 2 \times 1 0 ^ { 1 3 }$ cm, thus the relative accuracy in the difference needs to be $2 . 5 \times 1 0 ^ { - 1 5 }$ . This implies that rounding off is a problem with current computers, with relative rounding off error of $\varepsilon = 2 ^ { - 5 2 } = 2 . 2 \times 1 0 ^ { - 1 6 }$ ; extended precision is supported in software, but it has many limitations. The practical consequences are that the computer program processing the tracking observables, at this level of precision and over interplanetary distances, needs to be a mixture of ordinary and extended precision variables. Any imperfection may result in “banding”, that is residuals showing a discrete set of values, implying that some information corresponding to the real accuracy of the measurements has been lost in the digital processing. As an alternative, the use of a quadrature formula for the integral in eq. (17.6) can provide a numerically more stable result, because the S/N of the range-rate measurement is $\ll 1 / \varepsilon$ .

# Time-scales and science goals

Of the five state vectors used in eq. (17.1), $\mathbf { x } _ { a n t }$ and $\mathbf { x } _ { E }$ can be assumed known, that is their current knowledge (at the cm level) cannot be improved by ranging to a Mercury orbiter. To observe the orbit of the Moon it is more effective to measure the range to a point on the surface of the Moon, as it is done with lunar laser ranging. Both tracking navigation satellites and using very long baseline interferometry give, by far, more information on the position of the antenna and on the rotation of the Earth.

On the contrary, $\mathbf { x } _ { s a t }$ contains information on the gravity field of Mercury, $\mathbf { x } _ { M }$ , $\mathbf { x } _ { E M }$ , and $S ( \gamma )$ on the orbits of the planets and on the theory of gravitation. Of the underlying dynamics, that of $\mathbf { x } _ { s a t }$ has orbital periods of $\simeq 8 0 0 0$ s, the planetary orbits have periods starting at $\simeq 7 \times 1 0 ^ { 6 }$ s for $\mathbf { x } _ { M }$ . The Shapiro effect $S ( \gamma )$ during superior conjunction, when the Sun is close to the path of radio waves from the Earth to the spacecraft, changes over an intermediate time-scale of $\simeq 3 \times 1 0 ^ { 5 }$ s.

The distribution in time of the observations is tightly constrained by visibility conditions, e.g., Mercury has to be well above the horizon of the ground station, thus a pass observable by a given station lasts about eight hours, with seasonal variations (longer in summer, shorter in winter). The spacecraft must not be behind Mercury, thus for some relative orientations of the Mercury-centric orbit plane and the direction to the Earth the passes are interrupted by occultations. The radio waves must not meet the Sun in their path to the spacecraft, including not just the photosphere (the visible Sun) but also the inner solar corona, where the radio waves are too much disturbed by plasma turbulence. Overall, for a Mercury polar orbiter, tracking from a single station is possible only about $1 / 4$ of the time.

For the state-of-the-art tracking systems discussed above, the accuracy of the range-rate measurements is better than that of the range, when integrated over a time span $< 3 3 0 0 0$ s; the one in range is more accurate over longer times. It follows that over one pass the measurements of $\dot { r }$ provide the most accurate constraints on $\mathbf { x } _ { s a t }$ . On the contrary, the constraints to the planetary orbits $\mathbf { x } _ { M }$ and $\mathbf { x } _ { E M }$ are essentially from $r$ measurements. The determination of $\gamma$ from the Shapiro effect is possible by using $\dot { r }$ to constrain $\dot { S } ( \gamma )$ during a superior conjunction experiment (Bertotti et al. 2003a). Still, if $r$ measurements are available, they constrain the value of $\gamma$ even during a superior conjunction with an accuracy improved by about an order of magnitude with respect to the $\dot { r }$ measurements alone.

Thus it is possible to separate conceptually (although not in the data processing) a gravimetry experiment and a relativity experiment.

# 17.3 The gravimetry experiment

The orbit $\mathbf { x } _ { s a t } ( t )$ depends upon the gravity field of Mercury and is a function of the mass of Mercury, of the harmonic coefficients $\overline { { C } } _ { \ell m } , \overline { { S } } _ { \ell m }$ of its static field (in a frame rotating with Mercury), and of the coefficients of the tidal deformations affecting the potential (mostly the Love number $k _ { 2 }$ ).

The orbit also depends upon the coefficients describing the rotation of Mercury, including the obliquity $\epsilon _ { 1 }$ and the amplitude of the libration in longitude $\epsilon _ { 2 }$ (see the next section). However, the response of the orbit $\mathbf { x } _ { s a t } ( t )$ to $\epsilon _ { 1 }$ contains the coefficient $\overline { { C } } _ { 2 0 }$ and the response to $\epsilon _ { 2 }$ contains $\overline { { C } } _ { 2 2 }$ (Cical\`o 2007), of course there would be no effect of the rotation on the gravity field if the planet were spherically symmetric. Thus the sensitivity to $\epsilon _ { 1 } , \epsilon _ { 2 }$ is too weak for a robust orbit determination based on the orbit only.

Table 17.1. Accelerations acting on a spacecraft in orbit around Mercury, in a planetocentric reference frame, with $a = 3 0 0 0 ~ \mathrm { k m }$ , $A / M = 0 . 0 5 ~ \mathrm { c m ^ { 2 } / g }$ .   

<table><tr><td>Cause</td><td>Formula</td><td>Parameters</td><td> Value cm/s2</td></tr><tr><td>Mercury monopole</td><td>GM/r² = Fo</td><td>GM</td><td>2.4· 10²</td></tr><tr><td>Mercury oblateness</td><td>3FC0R/r2</td><td>C20</td><td>1.3· 10-2</td></tr><tr><td>Mercury triaxiality</td><td>3F0C22R/22</td><td>C22</td><td>7.8 . 10-3</td></tr><tr><td>Radiation pressure</td><td>CR FPR</td><td>CR</td><td>6.8.10-5</td></tr><tr><td>Thermal emission</td><td>4/9FpR ag△T/T</td><td>a,△T</td><td>3.10-5</td></tr><tr><td>Sun tide</td><td>2GMr/r</td><td>GM</td><td>2.3· 10-5</td></tr><tr><td>Effect of ∈1</td><td>(9/2)q1 FC20R/r²</td><td>1C20</td><td>1.9 · 10-5</td></tr><tr><td>Effect of ∈2</td><td>(9/2) ∈FC22R/r2</td><td>C22</td><td>3.3 · 10-6</td></tr><tr><td>Solid tide</td><td>3k2 GMR/rr</td><td>k2</td><td>2.8.10-6</td></tr><tr><td>Mercury albedo</td><td>CRFPR (1-α)R/(2r²)</td><td>a，CR</td><td>2.7· 10-6</td></tr><tr><td>Venus tide</td><td>2GMqT8</td><td>GMq</td><td>4.10-8</td></tr><tr><td>Relativistic Mercury</td><td>F0GM/(c²r)</td><td>GM</td><td>1.9 . 10-8</td></tr></table>

A list of the perturbations acting on the orbit $\mathbf { x } _ { s a t } ( t )$ with their orders of magnitude (Table 17.1) easily shows that non-gravitational perturbations, in the fiery radiation environment around Mercury, are large enough to mask the effect of Mercury’s gravity field, besides the lowest degree harmonics, and even these could not be determined with the needed accuracy. The direct radiation pressure from the Sun generates a perturbing acceleration of the order of 0.01 times the $\overline { { C } } _ { 2 2 }$ effect; note that the thermal emission from the planet is of the same order, also because the planetary albedo of Mercury

1  α is low. Thus the requirement for an accelerometer: it is in fact available on BepiColombo as the ISA instrument, a spring accelerometer (Iafolla and Nozzoli 2001, Lucchesi and Iafolla 2006).

# Accelerometer observables

As discussed in Section 16.1, an accelerometer directly measures the acceleration resulting from non-gravitational perturbations acting on the outer surface of the spacecraft, with a minus sign, see eq. (16.3). Apparent forces due to the displacement of the sensing heads with respect to the spacecraft center of mass (CoM) are also included in the measurement, but this does not introduce an error in the acceleration measurements if the reference point, for which an orbit is computed, is rigidly attached to the accelerometer rather than being the CoM, see eq. (16.5).

A more serious problem is the thermal perturbations on the accelerometer, resulting in time-variable accelerometer calibration parameters; if these variations were slow enough, the determination of constant calibration parameters separately for each observed arc would solve the problem, but if the temperature variations are large this fails. For an accelerometer without active thermal control the temperature changes are large. For example, over a time span of 22 days ( $1 / 4$ of Mercury orbit) the temperature could change by $\simeq 1 0 ^ { \circ }$ , and the resulting spurious signal would degrade the solution.

Full size simulations of the BepiColombo gravimetry experiment have been performed (Milani et al. 2001b, Milani et al. 2003) to assess the feasible accuracy in the determination of the Mercury gravity coefficients, static and tidal, and to define the requirements on the accelerometer a priori calibration. The results are summarized in Figure 17.1, showing the effects of temperature changes on the accelerometer body, assuming the temperature changes are either uncontrolled or reduced to $1 0 \%$ or to $1 \%$ of the value applicable to the spacecraft frame. In all cases the true error, the difference between the ground truth value used in the simulation and the nominal solution, is significantly larger than the formal accuracy as deduced from the covariance matrix. However, with temperature control reducing by 1–2 orders of magnitude the changes occurring along an orbit of Mercury around the Sun, the gravitational signal is still well above the error up to order and degree 25. This resulted in the definition of a requirement for the accelerometer unit, which was adopted in the design of the instrument.6

![](images/25142c0a9fd0920703b9f634c655522ec08fef94d4b90d8b848db5d32e669490.jpg)  
Fig. 17.1. Signal and error for three simulations with $1 0 0 \%$ , $1 0 \%$ , and $1 \%$ of spurious accelerometer signals resulting from thermal sensitivity. For each degree $\ell$ the results are expressed in terms of the gravity anomalies at the surface, in milliGal $\mathrm { { ( 1 0 ^ { - } 3 ~ c m / s ^ { 2 } } }$ ). The errors for each degree are accumulated as the RMS sum of the errors for all the degrees up to $\ell$ . The top curves are the simulated signal and Kaula rule, the bottom one is the formal uncertainty from the covariance matrix.

The best simulation, with temperature control at the $1 \%$ level, allowed us to solve for the Love number $k _ { 2 }$ , giving the elastic response of Mercury’s gravity to the degree 2 tidal potential of the Sun, with a true error of 0.004, the formal accuracy being one order of magnitude less.

# Relativity in Mercury-centric orbit

The Mercury-centric orbit of the spacecraft is coupled to the orbit of the planet, mostly through the difference between the acceleration from the Sun on the probe and that on the planet (the Sun’s tidal term). This coupling is weak because the Sun’s tide is just $1 0 ^ { - 7 }$ of the monopole acceleration from Mercury. The relativistic perturbations containing the mass of Mercury are small, as shown in the table, to the point that they are not measurable, being easily absorbed by the much larger accelerometer calibrations. Should we conclude that general relativity does not matter in the computation of the Mercury-centric orbit? The answer is negative, but the main relativistic effect does not appear in the equation of motion for $\mathbf { x } _ { s a t }$ .

In the equations for the range-rate observable (17.5) the term $d \Delta _ { d o } / d t _ { b }$ accounts for the difference in time coordinates. In fact, there are three different time coordinates to be considered. The dynamics of the planets, as described by the Lagrangian (6.18), is the solution of differential equations with as independent variable a time belonging to a space-time reference frame with origin in the Solar System barycenter (6.16). There can be different realizations of such a time coordinate; the currently published planetary ephemerides are provided in a time called TDB (for dynamic barycentric time).7 The observations are based on averages of clocks and frequency scales located on the Earth’s surface; this corresponds to another time coordinate called TT (for terrestrial time). Thus for each observation the times $t _ { t } , t _ { r }$ need to be converted from TT to TDB to find the corresponding positions of the planets, e.g., the Earth and the Moon, by combining information from the precomputed ephemerides and the output of the numerical integration for Mercury and the Earth–Moon barycenter. This time conversion step is necessary for the accurate processing of each set of interplanetary tracking data; the main term in the TT-TDB difference is periodic, with period 1 year and amplitude $\simeq 1 . 6 \times 1 0 ^ { - 3 }$ s, while there is essentially no linear trend, as a result of a suitable definition of the TDB.

The equation of motion of a Mercury-centric satellite can be approximated, to the required level of accuracy, by a Newtonian equation of motion provided the independent variable of the spacecraft equation of motion is the proper time of Mercury. Thus, for the BepiColombo radioscience experiment, it is necessary to define a new time coordinate TDM (dynamic Mercury time) containing terms of post-Newtonian order 1 depending mostly upon the distance from the Sun $r _ { 1 0 }$ and velocity $v _ { 1 }$ of Mercury. The relationship with the TDB scale, truncated to post-Newtonian order 1, is given by the differential equation

$$
{ \frac { d t _ { T D M } } { d t _ { T D B } } } = 1 - { \frac { v _ { 1 } ^ { 2 } } { 2 c ^ { 2 } } } - \sum _ { k \neq 1 } { \frac { G m _ { k } } { c ^ { 2 } r _ { 1 k } } }
$$

which can be solved by a quadrature formula (see Appendix B) once the orbits of Mercury, the Sun, and the other planets are known. Figure 17.2 plots the output of such a computation, showing a drift due to the non-zero average of the post-Newtonian term. The periodic term, with the period of Mercury’s orbit, is almost an order of magnitude larger than the difference TT-TDB. The time derivative of the periodic correction is $\simeq 1 0 ^ { - 8 }$ ; in (17.5) it is multiplied by the velocity of Mercury $\simeq 5 0 \mathrm { k m / s }$ , resulting in a change in range-rate by up to 0.05 cm/s, $\simeq 3 0$ times larger than the accuracy of the range-rate with an integration time of 30 s. The linear drift is relevant, although it could be removed by a change of scale, see Section 4.1, of the dynamic time and of the mass of Mercury. Caution must be used also in the space portion of the space-time coordinate change, used to refer the spacecraft orbit to the center of Mercury, see Appendix C.

![](images/fb8451d41642ca7abb29adf7d11070bf413229686fd8d805481e17a109b2205e.jpg)  
Fig. 17.2. Bottom: difference between the time coordinate TDM, in which the Mercury-centric orbit of the spacecraft is computed, and TDB, in which the planetary orbits are computed, as a function of TDB. Top: the same difference after removing a linear trend, showing the dependence upon the distance between Mercury and the Sun.

# 17.4 The rotation experiment

The rotation experiment will use correlation of images from the highresolution camera of BepiColombo to directly constrain the rotation state of the planet. The theory of the rotation of Mercury was established based on the early planetary radar data, which allowed us to measure the planet rotation frequency $\nu \simeq 3 / 2 n _ { 1 }$ , where $n _ { 1 }$ is the mean motion of the orbit of Mercury. Because of the significant eccentricity $e _ { 1 } \simeq 0 . 2$ of the orbit, the torque applied by the Sun’s tidal attraction on the long axis of the equator of Mercury forces a periodic perturbation of the uniform rotation. In a simplified model with Mercury in a Keplerian orbit and the rotation axis orthogonal to the orbit plane, coincident with the axis of maximum moment of inertia, the equation of motion for the rotation phase $\phi$ is (Colombo and Shapiro 1966)

$$
C \frac { d ^ { 2 } \phi } { d t ^ { 2 } } = \frac { 3 } { 2 } \frac { G M _ { \odot } \left( B - A \right) } { r ^ { 3 } } \sin ( v _ { 1 } - \phi )
$$

where $A , B , C$ are the principal moments of inertia (eigenvalues of the inertia quadratic form), $r$ is the distance to the Sun, and $v _ { 1 }$ the true anomaly of Mercury. From this equation it is possible to derive a first approximation solution

$$
\phi = \frac { 3 } { 2 } l _ { 1 } + \frac { 3 } { 2 } ~ \frac { B - A } { C } \sin l _ { 1 } + \cdot \cdot \cdot ,
$$

where $l _ { 1 }$ is the mean anomaly of Mercury, showing a libration of the rotation angle around the uniform rotation rate $\nu = 3 / 2 n _ { 1 }$ . The phase of this libration in longitude is 0 for $v _ { 1 } = 0$ , that is with Mercury at perihelion. However, if we assume that Mercury has a liquid layer separating a rigid outer shell from an inner core, the moment of inertia $C$ appearing in eqs. (17.7) and (17.8) should be replaced by $C _ { m }$ , the moment of inertia of the outer shell (Peale 1972). Then the amplitude of the libration in longitude would be larger by a factor $C / C _ { m }$ , which could be as large as $\simeq 2$ . The first goal of the rotation experiment is to estimate the amplitude $\epsilon _ { 2 }$ of this libration, thus constraining $( B - A ) / C _ { m }$ .

A complete theory of the rotation of Mercury, taking into account the secular perturbations to the orbit, should also take into account the Cassini laws, by which the rotation axis belongs to the plane spanned by the normal to the orbit plane and the axis of the orbital plane precession of Mercury (Colombo 1966). The obliquity, the angle $\epsilon _ { 1 }$ between the normal to the orbit plane and the rotation axis, is proportional to the concentration coefficient $C / ( M R ^ { 2 } )$ where $R$ is the mean radius of Mercury. Then (Peale 1988)

$$
\frac { C _ { m } } { C } = \frac { C _ { m } } { B - A } \frac { M R ^ { 2 } } { C } \frac { B - A } { M R ^ { 2 } } ,
$$

where the first two factors are measured by $\epsilon _ { 1 } , \epsilon _ { 2 }$ and the third by the harmonic coefficient $C _ { 2 2 }$ , see eq. (13.23). Thus it is possible, by measuring the rotation state of Mercury, in particular the parameters $\epsilon _ { 1 } , \epsilon _ { 2 }$ , and the gravity field, in particular $C _ { 2 2 }$ , to draw some conclusions about both the physical state and the size of the core of Mercury.

A more complete model of the rotation of Mercury would include planetary short periodic perturbations on the orbit, indirectly affecting the rotation state (Dufey et al. 2008). The main terms introduced in this way in the longitude libration (17.8) contain the anomalies of the planets, thus have periods of a few years. The largest term is due to Jupiter: it has period 11.86 y and amplitude $\simeq 1 3$ arcsec. This implies that the phase of the complete libration in longitude is not 0 at perihelion. If the duration of the mission in orbit around Mercury is small compared to the periods of the main planetary perturbation terms, the latter are approximately a constant shift in the rotation phase at perihelion. We assume that the expansion in spherical harmonics is done with spherical polar coordinates $( r , \theta , \lambda )$ with the origin of longitudes at the meridian of Mercury facing the Sun at some perihelion. Then the presence of a non-zero rotation phase implies that the axis of minimum inertia is at some angle $\delta _ { 2 2 }$ from the reference meridian. Then there is a non-zero $S _ { 2 2 }$ coefficient, which can be solved in the orbit determination and used to compute $\delta _ { 2 2 }$ by the equation $C _ { 2 2 } \cos ( 2 \lambda ) + S _ { 2 2 } \sin ( 2 \lambda ) = J _ { 2 2 } \cos ( 2 \lambda + 2 \delta _ { 2 2 } )$ . In conclusion the planetary perturbations generate effects which should be observable by the Bepi-Colombo radioscience experiment.

# The observing conditions

The peculiar rotation of Mercury in a $3 / 2$ resonance with the orbital motion results in sharp constraints on the possibility of observing multiple times the same portion of the surface from an orbiting spacecraft. A Mercury solar day is a time span ( $\simeq 1 7 6$ Earth days) in which the planet completes three sidereal rotations (the rotation phase $\phi$ is the curve F in Figure 17.3) and the Sun as seen from Mercury’s orbit revolves twice in the sky (the mean anomaly $l _ { 1 }$ of Mercury is the curve M). Thus the Sun, as seen from a point on the surface, makes a full revolution on the celestial sphere in one Mercury solar day. The solar time on Mercury is given by $\phi - v _ { 1 }$ (curve T); for a given meridian on Mercury’s surface the times in which there is sunlight are the continuous part of the curve, the dotted part corresponds to darkness. The phase of the torque from the solar tide acting on the $C _ { 2 2 }$ harmonic is $2 \phi - 2 v _ { 1 } = 3 l _ { 1 } - 2 v _ { 1 } + \mathcal { O } ( \epsilon _ { 1 } )$ (curve C), thus the forced libration in the longitudinal main term has the period of the orbit of Mercury, see (17.8).

For a polar orbit there are only six times per Mercury solar day when the spacecraft ground track passes in a given area (of the size of a highresolution image), as shown in Figure 17.3 by the intersections of the horizontal lines and the rotation phase, and three of these are in darkness, on average. Moreover, the illumination conditions and the spacecraft altitude are bound to be different in the two images to be compared. If the mission lasts one Earth year, the same cycle of observing conditions repeats twice, but the same longitude is observed again at the same value of the anomaly of

![](images/94c61714be722817264b983a26d3a54681cd45ebec8568541144223d2aa78b31.jpg)  
Fig. 17.3. The angles involved in the libration in longitude of Mercury over half a year. M is the mean anomaly of the orbit of Mercury. F is the phase of the planet spin. $_ \mathrm { T }$ is the local solar time in degrees; note that the Sun can go back in the sky as seen from Mercury near perihelion. C is the phase of the torque applied by the Sun on Mercury’s equatorial bulge: its period is the orbital period. The two horizontal lines represent one choice for the orbital plane of the spacecraft.

Mercury, thus the libration in longitude also has the same phase. As a result of these observational constraints, it is essential to take all the opportunities to record images of the same area, including times when the spacecraft is not being tracked by a ground station. It has been shown by the gravimetry experiment simulations that, with reduction to $1 \%$ of the accelerometer bias, the orbit $\mathbf { x } _ { s a t } ( t )$ is accurate enough to perform the rotation experiment by comparing images taken at arbitrary times during the mission. However, this implies constraints on the maneuvers, even attitude ones, performed between two tracking passes.

The measurements are direction angles to reference points on the surface, as seen from the spacecraft and referred to an inertial reference frame by using the knowledge of the attitude (from star mappers) and of the alignment of the camera with respect to the spacecraft-fixed reference frame. Thus the error budget for these measurements includes the spacecraft orbit error, the attitude error, the thermo-mechanical stability of the camera and star mapper alignments, and the error in correlating two images to find the relative displacement (Milani et al. 2001b).

# 17.5 The relativity experiment

To test the theory of gravitation, the orbit of Mercury has to be determined with unprecedented accuracy; some improvement is necessary also for the orbit of the Earth–Moon barycenter. The requirement is for a fully relativistic equation of motion, including the terms expressing the violations of general relativity with the post-Newtonian parameters, such as $\gamma , \beta , \zeta , J _ { \mathrm { 2 \odot } } , \eta , \alpha _ { 1 } , \alpha _ { 2 }$ . Moreover, the mass of the Sun and possibly of some of the planets has to be improved. With 12 initial conditions for Mercury and the Earth–Moon barycenter, there are $\simeq 2 0$ parameters to be solved.

If it is possible to separate this portion of the problem from the determination of the Mercury-centric orbit, then it is a comparatively small computation, suitable for running a large number of tests exploring the combined effect of random and systematic errors (Milani et al. 2002). The observations can be introduced as two normal points, representing the range and range-rate data, for each pass of Mercury above the horizon. This simplified approach is useful in simulations, to identify the main problems and to assess the possible performances, see below; this does not imply that such a partitioning of the problem should be used in the operational processing of the real data. Five main problems have been identified with this approach.

(i) The determination of the two planetary orbits and of the mass of the Sun results in an approximate rank deficiency of order 4.   
(ii) There is a strong correlation, in the covariance matrix of the solution, between $\beta$ and $J _ { 2 \odot }$ , degrading the marginal accuracy in the solution of both parameters.   
(iii) The parameter $\gamma$ appears also in the Shapiro effect, strongly dependent upon the minimum distance of the radio beam from the Sun. During a close superior conjunction, $\gamma$ generates a Shapiro signal larger than that on the orbit of Mercury.   
(iv) The parameter $\zeta$ describing $d ( G M _ { \odot } ) / d t$ is very sensitive to the presence of a time-dependent systematic effect in the range measurement.   
(v) The orbit of the Earth–Moon barycenter has to be determined with such an accuracy that perturbations from asteroids are relevant.

The origin of these problems, and some possible solutions, are as follows.

(i) After eliminating the Sun’s coordinates as dynamical variables by the use of barycentric planetary positions, eq. (6.17), there are still three exact symmetries obtained by rotation of all the planets, as discussed in Section 6.6. Even if the orbits of the other planets are not solved, but taken from the existing planetary ephemerides, because of the weak coupling with the orbits of Mercury and the Earth there is still an approximate symmetry. Moreover, a scale change is an approximate symmetry, provided the mass of the Sun is simultaneously changed according to eq. (4.7). Thus it is necessary to add four constraints, with the technique discussed in Section 6.1.

(ii) The main orbital effect of $\beta$ is a precession of the argument of perihelion, that is a displacement taking place in the plane of the orbit of Mercury; $J _ { 2 \odot }$ affects the precession of the longitude of the node, that is generates a displacement in the plane of the solar equator. The angle between these two planes is only $\epsilon = 3 . 3 ^ { \circ }$ and $\cos \epsilon = 0 . 9 9 8$ , thus it is easy to understand how the correlation between $\beta$ and $J _ { 2 \odot }$ can be 0.997. Short of using another test body, with an orbit plane much more inclined than that of Mercury, this correlation cannot be avoided. One possible way to mitigate this effect is to use the equation derived by Nordtvedt (1970) for a generic theory of gravitation under the assumption that it is a metric theory:

$$
\eta = 4 \beta - \gamma - 3 - \alpha _ { 1 } - \frac { 2 } { 3 } \alpha _ { 2 } .
$$

When the values of $\gamma , \eta$ and also of the preferred frame parameters (if included in the solution) are well determined, this equation acts essentially as a strong constraint on the value of $\beta$ , and as a result the variance of both $\beta$ and $J _ { 2 \odot }$ is sharply reduced, see (Milani et al. 2002, Figure 6).

(iii) Because of the different time-scale, a superior conjunction experiment with the specific purpose of strongly constraining the value of $\gamma$ cannot be simulated in the same way as the determination of the other post-Newtonian parameters: a combined solution for the Mercury-centric orbit, for a local correction to the orbit of Mercury and for $\gamma$ has to be used. The quality of the results, however, depends strongly on the assumptions. In every year there are three superior conjunctions of Mercury as seen from the Earth, but each individual superior conjunction produces a Shapiro S/N depending upon the circumstances: in some cases Mercury is occulted by the Sun, in others the radio waves are passing much farther from the Sun, thus the $\gamma$ signal contained in the Shapiro effect is much weaker. In (Milani et al. 2002) the assumption used for the simulations was that for a comparatively short time span (20 days) around the superior conjunction three ground stations were available, distributed in longitude in such a way as to provide continuous tracking; moreover, a conjunction in which Mercury was actually occulted by the Sun was used. In the real mission, these assumptions may not be satisfied. A possible alternative is to perform a superior conjunction experiment during the interplanetary cruise phase, as in (Bertotti et al. 2003a). As discussed in Section 14.5, the handling of the non-gravitational perturbations is easier, the accelerometer is not really needed (the same experiment can be used as long-term calibration of the accelerometer). An experiment under conditions comparable to the Cassini one, but with the BepiColombo instrument (capable of very accurate range measurements, not just range-rate) could give results on $\gamma$ more accurate by an order of magnitude. However, the conditions in the inner Solar System are more difficult for several reasons, including stronger radiation pressure and the need for a longer duration of the experiment.

(iv) The main effect of a change of either the universal gravitational constant $G$ or the mass of the Sun $M _ { \odot }$ by a fraction $1 0 ^ { - 1 3 }$ in one year is a quadratic perturbation along-track, growing to $\simeq 1 5$ cm after one year for Mercury. If the range measurements contain a time-dependent bias with a quadratic signature, this results in a systematic error in the nominal solution for $\zeta$ . This argument was used to upgrade the requirements for the instrument to be used in the BepiColombo radioscience experiment, which now includes an internal calibration loop to measure the transponder delay. The mass of the Sun changes by a fraction $\simeq 7 \times 1 0 ^ { - 1 4 }$ per year because of the mass shed as photons, and this contribution to $\zeta$ can be predicted with some accuracy. Less easy is to estimate accurately the mass shed by the Sun as charged particles, also because a large fraction of this phenomenon might occur near the poles of the Sun. Thus the determination of $\zeta$ from the orbit of Mercury is not a null experiment, but one in which there is a predicted value, although not a very accurate one. For estimated values of $\zeta$ of the order of a few parts in $1 0 ^ { - 1 3 }$ , to discriminate between a change in $G$ and the known change in $M _ { \odot }$ might be difficult.

(v) The perturbations by the asteroid Ceres on the orbit of the Earth can be estimated from the Roy–Walker parameters of Table 4.1: the short periodic perturbations on the Earth’s orbit should be $\simeq 2 . 2 \times 1 0 ^ { - 1 1 }$ AU 3 m. Not to degrade the accuracy of the results obtained with ranging from Earth accurate to $\simeq 1 0$ cm, the mass of Ceres needs to be known with a relative error of the order of 0.01, and this appears to be feasible by using the deflections of the orbits of other asteroids passing near Ceres. The problem is that there are $> 2 0$ asteroids with mass at least $1 / 1 0 0$ of that of Ceres, $\simeq 1 5 0$ with mass at least $1 / 1 0 0 0$ , and for many of them the mass is largely unknown. The combined effect of these poorly known perturbations could degrade the orbital determination for the Earth; the effect on Mercury is one order of magnitude smaller. This problem is connected to that of observation weighting discussed in Section 5.8, because the accurate orbit determination of closely approaching asteroids is strongly affected by the astrometric data quality (Baer et al. 2008). A solution of the problem could come from future asteroid mass determinations, obtained with higher accuracy astrometric surveys either from the ground or from space. 8

Table 17.2. The standard deviations and full errors (including systematic effects) in two simulations of the Relativity Experiment with BepiColombo. Experiments A and B differ only in that B uses the Nordtvedt equation (17.10) as a constraint.   

<table><tr><td>[0.5ex]</td><td colspan="2">Exp A (non-metric)</td><td colspan="2">Exp B (metric)</td></tr><tr><td>Parameter</td><td>RMS</td><td>True error</td><td>RMS</td><td>True error</td></tr><tr><td>β-1</td><td>6.7 ×10-5</td><td>2.2×10-4</td><td>7.5 ×10-7</td><td>2.0 ×10-6</td></tr><tr><td>n</td><td>4.4 × 10-6</td><td>1.5 ×10-5</td><td>3.0 ×10-6</td><td>7.9 × 10-6</td></tr><tr><td>s</td><td>4.0 × 10-14</td><td>5.2 × 10-13</td><td>3.9 ×10-14</td><td>5.3 × 10-13</td></tr><tr><td>△J</td><td>7.9 × 10-9</td><td>2.8 ×10-8</td><td>2.4 ×10-10</td><td>2.1 × 10-9</td></tr><tr><td>△M/M0</td><td>1.9 × 10-12</td><td>5.9 × 10-12</td><td>3.3 × 10-13</td><td>1.0 × 10-12</td></tr></table>

The results of two simulations performed by Milani et al. (2002) were as described in Table 17.2. The parameter $\gamma$ was considered to be known at the $2 \times 1 0 ^ { - 6 }$ level as a result of a superior conjunction experiment. The systematic effects included in the error model of the data simulation included a time-dependent bias with a nonlinear growth to 50 cm in one year, and this affected all the parameters, as shown by the significant difference between the formal error, computed from the covariance matrix, and the true error, obtained as the difference with the values actually used in the simulation. For $\zeta$ the ratio true error/formal RMS is particularly large, as expected. For $\beta$ , $J _ { 2 \odot }$ the marginal uncertainty is degraded by a factor $\simeq 1 0 0$ in the non-metric case A, with respect to the metric case B, in which eq. (17.10) is used as constraint. This is made possible by the good determination of $\gamma$ and $\eta$ , and also of $\alpha _ { 1 } , \alpha _ { 2 }$ as shown by other simulations including also these parameters. In conclusion, the results of these simplified simulations are encouraging, which does not mean that all the problems have been solved.

# 17.6 Global data processing

We have described, in the previous three sections, three aspects of the Bepi-Colombo radioscience experiment: the gravimetry, rotation, and relativity experiments. However, the main challenge of the BepiColombo orbit determination is to assemble all the observations and solve for all the relevant parameters, in a complete and self-consistent way. This results in a comparatively large least squares fit, although not as large as some of the examples in Chapter 16. With state-of-the-art computer hardware, neither the memory size nor the computational load are a problem. The difficult task is to ensure that all the equations, representing physically heterogeneous phenomena, are accurate and consistent at the required level. In this last section we discuss how this global data processing could be done.

# The local–global decomposition

The range and range-rate observations are naturally decomposed into arcs, one for each pass of Mercury above the horizon of the ground station(s). If there is only one ground station, this means one arc per day. Additionally, there are separate arcs of angular observations of the geodetic reference points, taken with the high-resolution camera.

The Mercury-centric orbit cannot be propagated in an accurate way for a very long time span, because of the poorly modeled non-gravitational perturbations during the interval between two passes, and also because of the possible attitude maneuvers. During a pass, the accelerometer calibration parameters are obtained from the fit of the observations (mostly the rangerate). A rough order of magnitude estimate could be as follows: over 1000 s with a measurement of range-rate accurate to $3 \times 1 0 ^ { - 4 }$ cm/s, a constant acceleration of $\simeq 3 \times 1 0 ^ { - 7 }$ can be determined. With only one ground station, in the interval of 14–16 hours between two passes the accelerometer will record uncalibrated accelerations. In the simulations (Milani et al. 2003), even assuming a priori calibration with $1 \%$ accuracy of the thermal signal (the best case considered in Section 17.3), the mean error in the spacecraft position propagated by one day was 3.8 m, a very substantial growth with respect to the mean error in the initial conditions, which was $< 1 0$ cm.

That is, any attempt to propagate in a deterministic way the orbit while it is not tracked results in an error which is far larger than the measurement accuracy. Thus to the Mercury-centric orbit determination we can apply the same argument used for the geocentric orbit of LAGEOS in Section 15.3, and a good choice could be to use a multi-arc strategy, in which an independent set of six initial conditions is solved for each arc.

Then we can find out which parameters are local to one arc, in the sense of eq. (15.1), and which ones are global. The arc initial conditions and three constant calibrations (one for each accelerometer sensitive axis) are local parameters, for a total of $\simeq 9 \times 3 6 5$ for a nominal one-year mission. The geodetic coordinates of the reference points used to find the shift between images are local to an arc containing only the camera observations.

The harmonic coefficients ( $3 1 ^ { 2 } - 4$ for degree and order up to 30), the planetary initial conditions with some masses and post-Newtonian parameters, the global range calibrations, the tidal coefficients, and Mercury’s rotation parameters are global parameters.

Following the algorithm described in Section 15.1, the problem can be solved by steps. First the local normal matrix is inverted arc by arc, see eq. (15.2), then the global variables are corrected, eq. (15.4), last the local variables are corrected by eq. (15.5). The problem in this approach appears in the first step: the local-only normal matrix has an approximate rank deficiency of order 1.

# Line of sight symmetry

The symmetry responsible for the weakness of the local only normal matrix is an approximate version of the exact symmetry found for extrasolar planets in Section 6.5. If the Mercury-centric orbit is rotated around an axis $\hat { \rho }$ in the direction from the Earth to the center of Mercury, then there would be an exact symmetry in the range and range-rate observations if $\hat { \rho }$ were constant. Given that $\hat { \rho }$ changes with time, the small parameter in the approximate symmetry is the angle by which $\hat { \rho }$ rotates (in an inertial reference system) during the arc time span (Bonanno and Milani 2002).

Different solutions can be adopted to stabilize the solution for the local parameters. A set of a priori observations weakly constraining the initial conditions (with an uncertainty of 3 m in position and 3 m/day in velocity) would be enough to stabilize the solution (Milani et al. 2001b). This is a simplified method used in a simulation; under operational conditions we would need to compute a lower accuracy long arc solution which does not contain the approximate symmetry (because the time span is comparable with the synodic period of Mercury and the Earth), and use it to weakly constrain the local initial conditions for a short arc. As an alternative approach, the initial conditions for two consecutive arcs could be weakly constrained together, by using a covariance matrix for the prediction at the next day enlarged $^ { 9 }$ with respect to the deterministic covariance propagation of Section 5.5. A final choice among the different options has not yet been done, but will be dictated by the results of new rounds of full-scale simulations.

# A complex experiment

We would like to conclude this discussion of the BepiColombo radioscience experiment with a few words on the context. Because of the expected extreme quality of the data, the BepiColombo tracking will contain an enormous amount of information, which could generate very interesting results on both the structure of Mercury and the theory of gravitation. However, we need to be well aware of what could go wrong, also because this is the only way to safeguard against this possibility.

As a matter of principle, unless there is available absolute a priori knowledge, with errors too small to significantly affect the measurements, all the parameters affecting the observations should be included in a global least squares fit. This avoids the risk of confusion between marginal and conditional uncertainty for correlated parameters of interest.

In practice some decomposition of the problem is unavoidable, in particular the one resulting from the fact that some data are acquired by other teams and transmitted with a not too complicated interface. For example, the ground station calibration parameters, the ground antenna motion, the spacecraft antenna position and motion, the tropospheric corrections, the spacecraft attitude, and the camera alignment will be measured by other teams. For most of these measurements the requirements for keeping up with the target accuracy of the BepiColombo data set are challenging.

In other words, the BepiColombo radioscience experiment is a system experiment, involving the performance of many spacecraft subsystems and of the ground station. The work of hundreds of specialists needs to be kept at a high level of quality. This chapter has given a short account of the work we have to do, but we need to be aware of the need to rely on the work of many others.

# Conclusions

We conclude this book with some words of caution: as already anticipated in the preface, we never had the intention of writing a complete reference for all methods which could be used in orbit determination problems. The goal was to present to the readers something new which they may use, mostly from the research we have conducted ourselves with many coworkers and in many years. Please let us know if we have succeeded in this.

# References

Aguirre-Martinez, M. and Sneeuw, N. (2003). Needs and tools for future gravity measuring missions, Space Sci. Rev. 108, 409–416.   
Aitken R. G. (1964). The Binary Stars (Dover Publication, New York).   
Aksnes, K. (1976). Short-period and long-period perturbations of a spherical satellite due to direct solar radiation, CMDA 13, 89–104.   
Albertella, A. (1993). Calcoli geodetici sulla sfera con la serie di Fourier, Politecnico di Torino, D. Phil. thesis.   
Albertella, A. and Migliaccio, F. (eds) (1998). SAGE, Satellite Accelerometry for Gravity Field Exploration: Phase A Final Report (International Geoid Service, Milano).   
Albertella, A., Sans\`o, F. and Sneeuw, N. (1999). Band-limited functions on a bounded spherical domain: the Slepian problem on the sphere, J. Geod. 73, 436–447.   
Anderson, J.D., Colombo, G., Esposito, P.B., Lau, E.L. and Trager, G.B. (1987). The mass, gravity field, and ephemeris of Mercury, Icarus 124, 337–349.   
Anselmo, L., Bertotti, B., Farinella, P., Milani, A. and Nobili, A. M. (1983a). Orbital perturbations due to radiation pressure for a spacecraft of complex shape, CMDA 29, 27–43.   
Anselmo, L., Farinella, P., Milani, A. and Nobili, A. M. (1983b). Effects of the Earth-reflected sunlight on the orbit of the LAGEOS satellite, Astron. Astrophys. 117, 3–8.   
Arnold, V. (1976). Mathematical Methods of Classical Mechanics (Springer, Berlin).   
Baer, J., Milani, A., Chesley, S.R. and Matson, R.D. (2008). An Observational Error Model, and Application to Asteroid Mass Determination, AAAS-DPS meeting 2008, abstract 52.09.   
Balmino, G., Barriot, J. P. and Val´es, N. (1990). Non-singular formulation of the gravity vector and gravity gradient tensor in spherical harmonics, Manuscripta Geodetica 15, 11–16.   
Bern, M. and Eppstein, D. (1992). Mesh generation and optimal triangulation. In Computing in Euclidean Geometry, eds. D.-Z. Du and F.K. Hwang (World Scientific), pp. 23–90.   
Bertotti, B. and Iess, L. (1991). The rotation of LAGEOS, J. Geophys. Res. 96, 2431–2440.   
Bertotti, B., Iess, L. and Tortora, P. (2003a). A test of general relativity using radio links with the Cassini spacecraft, Nature 425, 374–376.   
Bertotti, B., Farinella, P. and Vokrouhlick´y, D. (2003b). Physics of the Solar System (Kluwer, Dordrecht).   
Bini, D., Capovani, M. and Menchi, O. (1988). Metodi numerici per l’algebra lineare (Zanichelli, Bologna).   
Bini, D. A. (1997). Numerical computation of polynomial zeros by means of Aberth method, Numer. Algorithms 13, no. 3–4, 179–200.   
Boattini, A., D’Abramo, G., Forti and G. Gal, R. (2001). The Arcetri NEO Precovery Program, Astron. Astrophys. 375, 293–307.   
Bonanno, C. (2000). An analytical approximation for the MOID and its consequences, Astron. Astrophys. 360, 411–416.   
Bonanno, C. and Milani, A. (2002). Symmetries and rank deficiency in the orbit determination around another planet, CMDA 83, 17–33.   
Bowell, E. and Muinonen, K. (1994). Earth-crossing asteroids and comets: groundbased search strategies, in Hazards due to Comets and Asteroids, ed. T. Gehrels (University of Arizona Press, Tucson), pp. 149–197.   
Bowell, E., Hapke, B., Domingue, D., Lumme, K., Peltoniemi, J. and Harris, A.W. (1989). Application of photometric models to asteroids. In Asteroids II, eds. R. P. Binzel, T. Gehrels and M. S. Mathews (University of Arizona Press, Tucson), pp. 524–556.   
Broucke, R. A. and Cefola, P. J. (1972). On the equinoctial orbit elements, CMDA 5, 303–310.   
Carpino, M., Milani, A. and Chesley, S. R. (2003). Error statistics of asteroid optical astrometric observations, Icarus 166, 248–270.   
Celletti, A. and Pinzari, G. (2005). Four classical methods for determining planetary elliptic elements: A comparison, CMDA 93, 1–52.   
Celletti, A. and Pinzari, G. (2006). Dependence on the observational time intervals and domain of convergence of orbital determination methods, CMDA 95, 327– 344.   
Cesare, S. et al. (2005). Laser Doppler Interferometry Mission: Final Report, Alcatel Alenia Space Italia report No. SD-RP-AI-0445. 19 December 2005.   
Cesare, S., Sechi, G., Bonino, L., Sabadini, R., Marotta, M., Migliaccio, F., Reguzzoni, M., Sans\`o, F., Milani, A. and Pisani, M. (2006). Satellite-to-satellite laser tracking mission for gravity field measurement. In Gravity Field of The Earth, Proceedings of the First International Symposium of the International Gravity Field Service, Istambul, 28 August $^ { - 1 }$ September 2006.   
Charlier, C. V. L. (1910). On multiple solutions in the determination of orbits from three observations, MNRAS 71, 120–124.   
Charlier, C. V. L. (1911). Second note on multiple solutions in the determination of orbits from three observations, MNRAS 71, 454–459.   
Chesley, S.R. (2005). Very short arc orbit determination: the case of asteroid 2004 FU162. In Dynamics of Populations of Planetary Systems, eds. Z. Kneˇzevi´c, and A. Milani (Cambridge University Press), pp. 259–264.   
Chesley, S.R. (2006). Potential impact detection for near-Earth asteroids: the case of 99942 Apophis, in Asteroid, Comets, Meteors, eds. Lazzaro, D. et al. (Cambridge University Press), pp. 215–228.   
Chesley, S.R., Chodas, P.W., Milani, A., Valsecchi, G.B. and Yeomans, D.K. (2002). Quantifying the risk posed by potential Earth impacts, Icarus, 159, 423–432.   
Chesley, S. R., Ostro, S. J., Vokrouhlick´y, D., Capek, D., Giorgini, J. D., Nolan, ˇ M. C., Margot, J.-L., Hine, A. A., Benner, L. A. M. and Chamberlin, A. B. 6489 Golevka, Science 302, 1739–1742.   
Chesley, S.R., Vokrouhlick´y, D. and Matson, R.D. (2008). Orbital identification for asteroid 152563 (1992 BF) through the Yarkovsky effect, Astron. J 135, 2336–2340.   
Chodas, P.W. and Yeomans, D.K. (1996). The orbital motion and impact circumstances of Comet Shoemaker-Levy 9. In The Collision of Comet Shoemaker-Levy 9 and Jupiter, eds. K.S. Knoll et al. eds. (Kluwer, Dordrecht), pp. 1–30.   
Cical\`o, S. (2007). Determinazione dello stato di rotazione di Mercurio dallo studio del campo gravitazionale, University of Pisa, Master thesis.   
Colombo, G. (1966). Cassini’s second and third laws, Astron. J 71, 891–896.   
Colombo, O.L. (1989). Advanced techniques for high-resolution mapping of the gravitational field. In Theory of Satellite Geodesy and Gravity Field Determination, Lecture Notes in Earth Sciences 25, eds. F. Sans\`o and R. Rummel (Springer, Berlin), pp. 335–369.   
Colombo, G. and Shapiro, I.I. (1966). The rotation of the planet Mercury, Astrophys. J 145, 296–307.   
Conn, A.R., Gould, N.I.M. and Toint, Ph.L. (1992) LANCELOT: a Fortran package for large-scale nonlinear optimization (Springer, Berlin).   
Coradini, A. et al. (1996). MORO Moon ORbiting Observatory, ESA SCI (96) 1, March 1996.   
Cox, D. A., Little, J. B. and O’Shea, D. (1996). Ideals, Varieties and Algorithms (Springer, Berlin).   
Crawford, R. T., Leuschner, A. O. and Merton, G. (1930). Determination of Orbits of Comets and Asteroids (McGraw Hill, New York).   
Danby, J. M. A. (1988). Fundamentals of Celestial Mechanics, Second edition (Willmann Bell, Richmond VA).   
Delaunay, B. (1934). Sur la sphere vide, Izvestiya Akademii Nauk SSSR, Otdelenie Matematicheskii i Estestvennykh Nauk 7, 793–800.   
de’ Michieli Vitturi, M. (2004). Approximate gradient-based methods for optimum shape design in aerodynamic, University of Pisa, D. Phil. thesis.   
Dufey, J., Lemaitre, A. and Rambaux, N. (2008) Planetary perturbations on Mercury’s libration in longitude, CMDA 101, 141–157.   
Edmonds, A.R. (1957). Angular Momentum in Quantum Mechanics (Princeton University Press.)   
European Space Agency (1999). Gravity field and steady-state ocean circulation mission (GOCE), ESA SP-1233(1), July 1999.   
Evans, L. C. (1998). Partial Differential Equations (American Mathematical Society).   
Everhart, E. and Pitkin, E. T. (1983). Universal variables in the two-body problem, Am. J. Phys. 51/8 712–717.   
Farnocchia, D. (2008). Orbite preliminari di asteroidi e satelliti artificiali, University of Pisa, Master thesis.   
Ferraz-Mello, S. (1981). Estimation of periods from unequally spaced observations, Astron. Astrophys. 86, 619–624.   
Field, D.A. (1988). Laplacian smooting and Delaunay triangulations, Commun. Appl. Math 4, 709–712.   
Gauss, C. F. (1809). Theoria motus corporum coelestium in sectionis conicis solem ambientum, Hamburg; also in Werke, siebenter band, (1981, Olms Verlag, Hildesheim). aPP Icarus 198, 130–137.   
Granvik, K., Muinonen, K., Virtanen, J., Delb´o, M., Saba, L., De Sanctis, G., Morbidelli, R., Cellino, A. and Tedesco, E. (2005). Linking Very Large Telescope asteroid observations. In Dynamics of Populations of Planetary Systems, eds. Kneˇzevi´c, Z. and Milani, A. (Cambridge University Press), pp. 231–238.   
Greenberg, R., Carusi, A. and Valsecchi, G.B. (1988), Outcomes of planetary close encounters – A systematic comparison of methodologies, Icarus 75, 1–29.   
Gronchi, G. F. (2002). On the stationary points of the squared distance between two ellipses with a common focus, SIAM Journ. Sci. Comp. 24/1, 61–80.   
Gronchi, G. F. (2005). An algebraic method to compute the critical points of the distance function between two Keplerian orbits, CMDA 93, 297–332.   
Gronchi, G. F. (2009). Multiple solutions in preliminary orbit determination from three observations, CMDA 103, 301–326.   
Gronchi, G. F. and Tommei, G. (2006). On the uncertainty of the minimal distance between two confocal Keplerian orbits, DCDS-B 7/4, 755–778.   
Gronchi, G. F., Tommei, G. and Milani, A. (2007). Mutual geometry of confocal Keplerian orbits: uncertainty of the MOID and search for Virtual PHAs. In Near Earth Objects, our Celestial Neighbors: Opportunity and Risk, eds. Milani, A. Valsecchi, G. B. and Vokrouhlick´y, D. (Cambridge University Press), pp. 3–14.   
Gronchi, G. F., Dimare, L. and Milani, A. (2008). Orbit determination with the two-body integrals, submitted.   
Hartmann, P. (1964). Ordinary Differential Equations (John Whiley, Hoboken, NJ).   
Herrick, S. (1971). Astrodynamics, Vol. 1 (Van Nostrand Reinhold, London).   
Hobson, E. W. (1931). The Theory of Spherical and Ellipsoidal Harmonics (Cambridge University Press).   
Hoots, F. R. (1994). An analytical method to determine future close approaches between satellites, CMDA 33, 143–158.   
Iafolla, V. and Nozzoli, S. (2001). Italian spring accelerometer (ISA): a high sensitive accelerometer for BepiColombo ESA CORNERSTONE Plan. Space Sci. 49, 1609–1617.   
Iess, L. and Boscagli, G. (2001). Advanced radio science instrumentation for the mission bepiColombo to Mercury, Plan. Space Sci. 49, 1597–1608.   
Jazwinski, A. H. (1970). Stochastic Processes and Filtering Theory (Academic Press, New York).   
Jeffreys, B. (1965). Transformations of tesseral harmonics under rotation, Geophys. J. 10, 141–145.   
Kaula, W. M. (1966). Theory of Satellite Geodesy (Blaisdell, Whaltham).   
Kholshevnikov, K. V. and Vassiliev, N. (1999). On the distance function between two keplerian elliptic orbits, CMDA 75, 75–83.   
King-Hele, D. (1964). Theory of Satellite Orbits in an Atmosphere (Butterworths, London).   
Kinoshita, H., Hori, G. and Nakai, H. (1974). Modified Jacobi polynomial and its applications to expansions of disturbing functions, Ann. Tokyo Astron. Obs. (Sec. Ser.) 14, 14–35.   
Kneˇzevi´c, Z. and Milani, A. (1998). Orbit maintenance of a lunar polar orbiter, Planet. Space Sci. 46, 1605–1611.   
Knuth D.E. (1998). The Art of Computer Programming, Volume 3, Sorting and Searching (Addison-Wesley, Reading, Massachussets).   
Kristensen, L.K. (1995). Orbit determination by four observations, Astron. Nachr. 316/4, 261–266.   
Kubica, J., Denneau, L., Grav, T., Heasley, J., Jedicke, R., Masiero, J., Milani, A., Moore, A., Tholen and D., Wainscoat, R. J. (2007). Efficient intra- and inter-night linking of asteroid detections using kd-trees, Icarus 189, 151–168.   
Lemoine, F.G., Kenyon, S.C., Factor, J.K., Trimmer, R.G., Pavlis, N.K., Chinn, D.S., Cox, C.M., Klosko, S.M., Luthcke, S.B., Torrence, M.H., Wang, Y.M., Williamson, R.G., Pavlis, E.C., Rapp, R.H. and Olson, T.R. (1998). The Development of the Joint NASA GSFC and NIMA Geopotential Model EGM96, NASA/TP-1998-206861, (NASA Goddard Space Flight Center, Greenbelt, MD).   
Leuschner, A. O. (1913a). A short method of determining orbits from 3 observations, Publ. Lick Obs. 7, 3–20.   
Leuschner, A. O. (1913b). Short methods of determining orbits, second paper, Publ. Lick Obs. 7, 217–376.   
Lucchesi, D. and Iafolla, V. (2006). The non-gravitational perturbations impact on the BepiColombo radio science experiment and the key rˆole of the ISA accelerometer: direct solar radiation and albedo effects, CMDA 96, 99–127.   
Marchi, S., Momany, Y. and Bedin, L. R. (2004). Trails of solar system minor bodies on WFC/ACS images, New Astron. 9, 679–685.   
Mehrholz, D., Leushacke, L., Flury, W., Jehn, R., Klinkrad, H. and Landgraf, M. (2002). Detecting, tracking and imaging space debris, ESA Bulletin 109 128–134.   
Milani, A. (1999). The asteroid identification problem I: recovery of lost asteroids, Icarus 137, 269–292.   
Milani, A. (2002a). Introduzione ai sistemi dinamici (Editrice PLUS, Pisa).   
Milani, A. (2002b). Celestial mechanics and the real Solar System: measurements, models and tests. In Celestial Mechanics, St. Petersburg 2002, IAU Transactions no. 8 (Institute of Applied Astronomy, St. Petersburg), pp. 133–136.   
Milani, A. (2005). Virtual asteroids and virtual impactors. In Dynamics of Populations of Planetary Systems, eds. Z. Kneˇzevi´c, and A. Milani (Cambridge University Press), pp. 219–228.   
Milani, A. and Kneˇzevi\`c, Z. (1995). Selenocentric Proper Elements, A Tool for Lunar Satellite Mission Analysis, version 2.0. ESA, Final Report of Study 144506, G. Racca technical officer.   
Milani, A. and Melchioni, E. (1989). Determination of a local geodetic network by multi-arc processing of satellite laser ranges. In Theory of Satellite Geodesy and Gravity Field Determination, Lecture Notes in Earth Sciences, 25, eds. F. Sans\`o and R. Rummel (Springer-Verlag, Berlin), 417–445.   
Milani, A. and Nobili, A. M. (1983a). On topological stability in the general 3–body problem, CMDA 31, 213–240.   
Milani, A. and Nobili, A. M. (1983b). On the stability of hierarchical 4–body systems, CMDA 31, 241–291.   
Milani, A. and Valsecchi, G.B. (1999). The asteroid identification problem II: Target plane confidence boundaries. Icarus 140, 408–423.   
Milani, A., Nobili, A. M. and Farinella, P. (1987). Non Gravitational Perturbations and Satellite Geodesy (Adam Hilger, Liverpool).   
Milani, A., Carpino, M., Rossi, A., Catastini and G., Usai, S. (1995). Local geodesy by satellite laser ranging: a European solution, Manuscripta Geodetica 20, 123–138. of the ESA MORO mission, Planet Space Sci. 44, 1065–1076.   
Milani, A., Chesley, S.R., and Valsecchi, G.B. (1999). Close approaches of asteroid 1999 $A N _ { 1 0 }$ : Resonant and non-resonant returns. Astron. Astrophys. 346, L65– L68.   
Milani, A., La Spina, A., Sansaturio and M. E., Chesley, S. R. (2000a). The asteroid identification problem III. Proposing identifications, Icarus 144, 39–53.   
Milani, A., Chesley, S.R., and Valsecchi, G.B. (2000b). Asteroid close encounters with Earth: risk assessment. Planet Space Sci. 48, 945–954.   
Milani, A., Chesley, S.R., Boattini, A. and Valsecchi, G.B. (2000c). Virtual impactors: Search and destroy, Icarus 145, 12–24.   
Milani, A., Sansaturio, M. E. and Chesley, S. R. (2001a). The asteroid identification problem IV: Attributions, Icarus 151, 150–159.   
Milani, A., Rossi, A., Vockrouhlicky, D., Villani, D. and Bonanno, C. (2001b). Gravity field and rotation state of Mercury from the BepiColombo Radio Science Experiments, Planet. Space Sci. 49, 1579–1596.   
Milani, A, Vokrouhlick´y, D., Villani, D., Bonanno, C. and Rossi, A. (2002). Testing general relativity with the BepiColombo radio science experiment, Phys. Rev. $D$ 66, 082001.   
Milani, A., Rossi, A. and Villani, D. (2003). The BepiColombo radio science simulations, Report to ESA, Version 2, 11 April 2003.   
Milani, A., Gronchi, G. F., de’ Michieli Vitturi, M. and Kneˇzevi´c, Z. (2004). Orbit determination with very short arcs. I admissible regions, CMDA 90, 59–87.   
Milani, A., Gronchi, G. F., Kneˇzevi´c, Z., Sansaturio, M. E. and Arratia, O. (2005a). Orbit determination with very short arcs. II identifications, Icarus 79, 350–374.   
Milani, A., Chesley, S. R., Sansaturio, M. E., Tommei, G. and Valsecchi, G. (2005b). Nonlinear impact monitoring: line of variation searches for impactors, Icarus 173, 362–384.   
Milani, A., Sansaturio, M. E., Tommei, G., Arratia, O. and Chesley, S. R. (2005c). Multiple solutions for asteroid orbits: computational procedure and applications, Astron. Astrophys. 431, 729–746.   
Milani, A., Rossi, A. and Villani D. (2005d). A timewise kinematic method for satellite gradiometry: GOCE simulations, Earth Moon Planets 97, 37–68.   
Milani, A., Gronchi, G. F., Kneˇzevi´c, Z., Sansaturio, M. E., Arratia, O., Denneau, L., Grav, T., Heasley, J., Jedicke, R. and Kubica, J. (2006). Unbiased orbit determination for the next generation asteroid/comet surveys. In Asteroids Comets Meteors 2005, eds. D. Lazzaro et al. (Cambridge University Press), pp. 367–380.   
Milani, A., Gronchi, G. F. and Kneˇzevi´c, Z. (2007). New definition of discovery for Solar System objects, Earth Moon Planets 100, 83–116.   
Milani, A., Gronchi, G. F., Farnocchia, D., Kneˇzevi´c, Z., Jedicke, R., Dennau, L. and Pierfederici, F. (2008). Topocentric orbit determination: Algorithms for the next generation surveys, Icarus 195, 474–492.   
Mood, A.M., Graybill, F.A. and Boes, D.C. (1974). Introduction to Statistics, (McGraw-Hill, New York).   
Mossotti, O.F. (1816–1818). Nuova analisi del problema di determinare le orbite dei corpi celesti, in Mossotti, scritti (Domus Galileiana, Pisa).   
Moyer, T.D. (2003). Formulation for Observed and Computed Values of Deep Space Network Data Types for Navigation (Wiley-Interscience, Hoboken, NJ).   
Mussio, L. (1984). Il metodo della collocazione minimi quadrati e le sue applicazioni per l’analisi statistica dei risultati delle compensazioni. Ricerche di Geodesia, Topografia e Fotogrammetria 4, 305–338.   
Nordtvedt, K. (1970). Post-Newtonian metric for a general class of scalar-tensor gravitational theories and observational consequences, Astrophys. J. 161, 1059–1067.   
Olsen, Ø. (2007). The constancy of the Pioneer anomalous acceleration, Astron. Astrophys. 463, 393–397.   
Pail, R., Plank, G. and Schuh, W. D. (2001). Spatially restricted data distributions on the sphere: the method of orthonormalized functions and applications, J. Geod. 75, 44–56.   
Peale, S.J. (1972). Determination of parameters related to the interior of Mercury, Icarus 17, 168–173.   
Peale, S.J. (1988). The rotation dynamics of Mercury and the state of its core, in Mercury, eds. Vilas, F., Chapman, C.R. and Matthews, M.S. (University of Arizona Press, Tucson), pp. 461–493.   
Plummer, H. C. (1918). An Introductory Treatise on Dynamical Astronomy (Dover Publications, New York).   
Poincar´e, H. (1906). Sur la d´etermination des orbites par la m´ethode de Laplace, Bulletin astronomique 23, 161–187.   
Risler, J. J. (1991). M´ethodes mathematiques pour le CAO, Collection Recherche en mathematiques appliqu´ees, RMA 18, Masson.   
Rossi, A. (2005) Population models of space debris. In Dynamics of Populations of Planetary Systems, eds. Z. Kneˇzevi´c, and A. Milani (Cambridge University Press), pp. 427–438.   
Sansaturio, M. E., Milani, A. and Cattaneo, L. (1996). Nonlinear optimisation and the asteroid identification problem. In Dynamics, Ephemerides and Astrometry of the Solar System, eds. S. Ferraz Mello et al. (Kluwer, Dordrecht), pp. 193– 198.   
Simmons, J.F.L., McDonald, A.J.C. and Brown, J.C. (1985). The restricted 3-body problem with radiation pressure, CMDA 35, 145–187.   
Sitarski, G. (1968). Approaches of the parabolic comets to the outer planets, Acta Astron. 18/2, 171–195.   
Sneeuw (1991). Inclination functions: group theoretical background and a recursive algorithm. In Reports of the Faculty of Geodetic Engineering, 91.2 (Delft University of Technology, Delft).   
Taff, L. G. and Hall, D. L. (1977). The use of angles and angular rates. I – Initial orbit determination, CMDA 16, 481–488.   
Tapley, B., Ries, J., Bettadpur, S., Chambers, D., Cheng, M., Condi, F., Gunter, B., Kang, Z., Nagel, P., Pastor, R., Pekker, T., Poole, S. and Wang, F. (2005). GGM02 – An improved Earth gravity field model from GRACE, J. Geodesy 79, 467–478.   
Tommei, G. (2005). Nonlinear impact monitoring: 2-dimensional sampling, in Dynamics of Populations of Planetary Systems, eds. Z. Kneˇzevi´c, and A. Milani, (Cambridge University Press), pp. 259–264.   
Tommei, G. (2006a). Canonical elements for Opik theory, ¨ CMDA 94, 173–195.   
Tommei, G. (2006b). Impact monitoring of near-Earth objects: theoretical and computational results, University of Pisa, D. Phil. thesis.   
Tommei, G., Milani, A. and Rossi, A. (2007). Orbit determination of space debris: admissible regions, CMDA 97, 289–304.   
Valk, S. and Lemaitre, A. (2007). Semi-analytical investigations of high area-tomass ratio geosynchronous space debris including Earth’s shadowing effects, Adv. Space Res. 42, 1429–1443.   
Valk, S., Lemaitre, A. and Anselmo, L. (2007) Analytical and semi-analytical investigations of geosynchronous space debris with high area-to-mass ratios influenced by solar radiation pressure. Adv. Space Res. 41, 1077–1090.   
Valsecchi, G.B., Milani, A., Gronchi, G.F., and Chesley, S.R. (2003), Resonant returns to close approaches: analytical theory, Astron. Astrophys. 408, 1179– 1196.   
Virtanen, J., Muinonen, K. and Bowell, E. (2001). Statistical ranging of asteroid orbits, Icarus 154, 412–431.   
Vokrouhlick´y, D and Milani, A. (2000). Direct radiation pressure on the orbits of small near-Earth asteroids: observable effects?, Astron. Astrophys. 362, 746– 755.   
Vokrouhlick´y, D, Milani, A. and Chesley, S. R. (2000). Yarkovsky effect on small Near Earth asteroids: mathematical formulation and examples, Icarus 148, 118–138.   
Wagner, W. E. and Velez, C. E. (eds) (1972). Goddard Trajectory Determination Subsystem Mathematical Specifications (Goddard Space Flight Center, Greenbelt, MD).   
Walker, I.W., Gordon Emslie, A. and Roy, A.E. (1980). Stability criteria in manybody systems I, CMDA 22, 371–402.   
Wallin, J.F., Dixon, D.S. and Page, G.L. (2007). Testing gravity in the outer solar system: results from transneptunian objects, ApJ 666, 1296–1302.   
Wetherill, G. W. (1967). Collisions in the asteroid belt, J. Geophys. Res. 72, 2429– 2444.   
Whipple, A.L. (1995). Lyapunov times of the inner asteroids, Icarus 115, 347–353.   
Wigner, E.P. (1959). Group Theory and its Applications to the Quantum Mechanics of Atomic Spectra (Academic Press, New York).   
Will, C.M. (1981). Theory and Experiment in Gravitational Physics (Cambridge University Press).   
Winslow, A.M. (1964). An irregular triangle mesh generator, Report UCXRL-7880, National Technical Information Service, Springfield, VA.   
Yeomans, D.K., Chodas, P.W., Keesey, M.S., Ostro, S.J., Chandler, J.F. and Shapiro, I.I. (1992). Asteroid and comets orbits using radar data, Icarus 103, 303–317.

# Index

a posteriori calibration, 328, 330, 336   
a priori constraints, 90, 105, 321 observations, 89, 101, 337, 369 scaling, 97   
aberration, 148, 153, 161   
absolute calibration, 328   
absolute magnitude, 11, 143, 148, 218, 247   
absorption, 288, 299   
accelerometer, 303, 311, 325, 331, 357, 366, 368   
accuracy, 124, 221, 223, 228, 232   
admissible region, 144, 148, 151, 163, 205, 214, 224   
aerodynamic coefficient, 302   
aliasing, 97, 335, 343   
along-track acceleration, 172, 310 effect, 292, 304   
angle variable, 76, 91   
angular velocity, 326   
apparent acceleration, 326   
apparition, 113, 124   
approximate rank deficiency, 93, 197, 342, 364, 369   
approximate symmetry, 94, 342, 365, 369   
arc, 311, 336, 368 length parameter, 172 of type $N$ , 217   
area-to-mass ratio, 55, 290   
argument of pericenter, 39   
asteroid, 113, 137, 171   
astrometric observation, 130   
astronomical unit, 96, 105   
attitude, 289, 293   
attributable, 134, 137, 163, 205, 214, 216, 223 orbital elements, 148, 175, 209   
attribution, 114, 133, 165, 206, 224 penalty, 135, 156, 206   
axial symmetry, 267   
axial vector, 198

badly conditioned matrix, 64, 71   
barycentric coordinate, 40, 105   
BepiColombo, 9, 349   
bias, 80, 84   
bounce time, 352

calibration band, 336   
Cassini laws, 361 mission, 304   
center of mass, 35, 107, 239, 273, 309, 326, 357   
centrifugal, 320   
change of scale, 36, 105, 360   
Charlier theory, 185   
Cholewsky algorithm, 64, 67   
close approach, 142, 241 trace, 239   
collaborative orbit determination, 8   
collocation method, 337   
companion matrix, 150   
complete orthonormal sequence, 279   
compromise solution, 118, 129, 136   
computational complexity, 220   
concentration coefficient, 275, 350, 361   
conditional confidence ellipsoid, 69, 72 covariance matrix, 30, 150, 332 density function, 26, 78, 119 identification penalty, 129 normal matrix, 30, 149   
conditioning number, 64, 74, 97, 153, 197   
confidence ellipse, 76, 130, 155, 241, 251, 256 ellipsoid, 69, 73, 79, 85, 151, 152, 154, 198, 332 parameter, 6, 154, 241 prediction region, 130, 132 region, 6, 75, 151, 152, 154, 156, 248   
confirmed identification, 222   
consider parameters, 5, 69   
constrained triangulation, 145   
continuous random variable, 23   
Coriolis, 320   
correlation, 25, 61, 85, 163, 365 matrix, 85, 97   
covariance, 25, 61 matrix, 25, 60, 64, 87, 93, 116, 313, 321 propagation, 31, 73, 131, 153, 241, 369   
crossing, 243   
cycle slip, 129

Delaunay triangulation, 145, 206   
descoping, 88   
design matrix, 60, 62, 78, 83, 151   
differential corrections, 63, 114, 157, 203   
diffusion, 288   
direct perturbations, 42   
direct radiation pressure, 288   
discordant   
identifications, 226   
tracklets, 231   
discovery, 218   
distribution function, 23   
diurnal effect, 298   
divergence formula, 262   
Don Quixote, 306   
double binary hierarchy, 47   
drag coefficient, 302, 316   
drag free, 329   
dynamic   
barycentric time, 359   
Mercury time, 359   
dynamical equation, 174, 176, 179   
dynamical parameters, 3, 15, 351   
eccentricity, 39   
functions, 284   
effective cross-section, 289   
efficiency, 221, 223, 228, 232   
eigenvalues algorithm, 64, 67   
empirical acceleration, 316, 324   
ephemerides, 203   
equinoctial elements, 121   
equivalence principle, 109, 365, 367   
exact symmetry, 91, 309, 365, 369   
exterior Dirichlet problem, 279, 343   
external harmonics, 269   
extrasolar   
planetary system, 98, 103   
planets, 13, 98   
f and g series, 175   
first guess, 63, 114   
first integral, 34   
fit parameters, 59, 62   
fold, 254   
frequencywise method, 334, 346

Gaia, 183, 367   
Gauss divergence formula, 262 map, 177 method, 175, 177, 193   
Gaussian, 27, 29, 77, 85

general relativity, 106, 351, 358   
generic completion, 257   
geodesic curvature, 172   
geoid, 281, 341   
geometric equation, 174, 176   
geometric sampling, 248   
Gibbs formula, 176   
global fit parameters, 311, 368   
gradiometer, 281, 329, 333   
gravimeter, 264   
gravitational potential, 262   
gravity gradient acceleration, 327   
ground track, 286, 301, 345   
ground truth, 232, 357   
group of symmetries, 34, 91

harmonic coefficients, 276, 331, 336, 356 degree, 271, 332, 335, 347 function, 17, 264, 343 order, 271, 338   
heliocentric coordinates, 41, 52   
hierarchy, 50   
hyperbolic orbits, 90, 142, 206, 239   
identification, 10, 113, 163 management, 223, 226 normalization, 226 penalty, 117   
impact, 237, 239 cross-section, 240 monitoring, 12, 14, 202, 237 parameter, 239 probability, 238, 251   
inclination functions, 283   
independent identifications, 226 random variables, 26, 118   
indirect oblation, 316   
indirect perturbations, 42, 52   
inertia quadratic form, 275, 350, 361   
initial conditions, 3, 15   
integral flow, 4, 16   
integration time, 354   
internal harmonics, 269   
intersection problem, 160, 184   
isometry, 34

Jacobian coordinates, 43, 44, 47, 54   
joint probability density function, 24

Kaula expansion, 283, 323, 338 rule, 279, 332, 340, 348, 358   
Kepler problem, 38   
Keplerian distance function, 242   
kinematic method, 324, 334   
kinematical parameters, 4, 351   
kinetic method of deflection, 307   
kurtosis, 24, 84, 318   
Lagrange equation, 33, 37, 43, 110 function, 33, 37, 47 perturbative equations, 285   
Lagrangian, 33, 107, 109, 359   
Lambert law, 288   
Laplace equation, 264, 267 method, 174, 179, 188, 193   
Laplace–Beltrami operator, 267, 270   
Laplace–Lenz vector, 38   
Laplacian smoothing, 147   
least squares, 6, 59, 62, 90, 114, 149, 24 336, 368, 370   
Legendre associated function, 271 equation, 268 polynomials, 49, 269, 272   
libration in longitude, 356, 361   
Lie groups, 92   
limiting curve, 187, 194   
line of variations, 158, 200, 249   
linear momentum, 35, 107, 110   
linkage, 115, 156, 205   
local fit parameters, 311, 368   
local MOID, 243   
lost asteroid, 113   
Love number, 356, 358   
lunar laser ranging, 8, 355   
Lyapounov exponent, 20, 74 time, 20, 249   
maneuvers, 305, 363   
manifold dynamics, 250   
marginal confidence ellipsoid, 70 covariance matrix, 30, 121, 153, 332 density function, 26 normal matrix, 154   
Mariner, 349   
mass density function, 263   
matrix exponential, 22   
mean, 24, 25, 61   
mean anomaly, 102, 284   
measurement band, 335   
Mercury, 349 orbiter, 106, 350 solar day, 362   
merging identifications, 229   
minimum orbital intersection distance, 242   
minimum principle, 6   
mission analysis, 9   
modified target plane, 239   
Monte Carlo, 248   
Moore’s law, 219   
moving ob ject, 10, 134, 216, 221   
multiple solutions, 202   
mystery drag, 300, 316, 317

near-Earth asteroids, 11, 182, 216, 222, 237   
Newton’s method, 63, 75, 255   
Noether’s theorem, 34, 107, 110   
nominal solution, 6   
normal   
equation, 60, 89, 117, 199, 322, 331   
matrix, 25, 60, 63, 117, 197   
normal points, 11, 318, 364   
normalization of the residuals, 67   
normalized harmonics, 278   
normally distributed, 27, 29   
number density, 232   
Nyquist frequency, 335   
obliquity, 356, 361   
observation function, 4, 153   
oceanic loading, 318   
optimization interpretation, 6   
orbit distance, 242   
orbit identification, 114, 230   
outliers, 80   
Pan-STARRS, 219   
parametric post-Newtonian, 12, 107, 304, 351,   
364   
pass, 163, 314, 355, 364, 368   
penalty, 68, 116   
perturbing function, 48, 285   
photo-gravitational symmetry, 309   
Pioneer, 305   
planetary   
albedo, 299, 356   
ephemerides, 106, 359, 365   
hierarchy, 46   
radar, 11, 353   
systems, 12   
Poincar´e observer interpolation, 138, 161, 166,   
182   
Poisson equation, 264   
polar caps, 338   
population orbit determination, 10, 221   
possibility of an impact, 241   
potentially hazardous asteroid, 247   
precision orbit determination, 325   
precovery, 115, 155, 238   
prediction function, 4, 135, 152   
preferred frame, 110, 365, 367   
preliminary orbit, 114, 157, 171, 202, 223   
principal components analysis, 94, 341   
principle of the simplest geometry, 250, 253   
probabilistic interpretation, 6, 77   
probability density, 23, 77, 80, 118   
proper motion, 141, 172   
proposed identifications, 114, 222   
pseudo-inverse, 65, 87, 150   
quality control parameters, 202, 223   
radar attributable, 167   
radial velocity, 13, 137

radiation pressure force, 56, 289

range, 8, 137   
range-rate, 8, 137   
rank deficiency, 88, 105   
receive time, 167, 352   
recovery, 115, 155   
recursion formula, 275   
recursive attribution, 206, 222   
reduced dynamics orbit, 324   
reduced mass, 38, 43   
reflection, 288   
regression   
line, 29, 61, 70, 97, 134   
subspace, 70, 72, 121, 132   
regula falsi, 250, 255   
residual, 4, 59   
residual point, 194   
resonant decomposition, 332, 338   
resonant return, 254, 258, 349   
restricted identification, 121   
roots of a polynomial, 140, 161, 184   
rotation acceleration, 326   
rotation experiment, 360   
rounding off, 64, 88, 140, 348, 354   
Roy–Walker parameters, 47, 50, 366

saddle point of the target function, 66, 208   
satellite geodesy, 10 gravimetry, 261, 326 laser ranging, 8, 314 to-satellite tracking, 9, 345   
scale calibration, 328   
scale height, 164, 303, 324   
scaling, 96, 209   
scheduler, 231   
science goals, 349   
seasonal effect, 298   
sectorial spherical harmonic, 271, 281, 347   
secular perturbation, 285, 292   
self-residual point, 194   
semigroup property, 16, 73   
semilinear confidence boundary, 125, 133, 204 identification, 123 prediction, 76   
separation of variables, 267   
Shapiro effect, 106, 351   
short periodic perturbation, 292   
shower, 251   
signal-to-noise, 11, 80, 166, 220   
singleton, 251   
singular curve, 191   
space debris, 11, 163   
spacewise method, 333   
spatial scale, 323, 343   
spherical harmonic, 48, 271, 323, 334, 350   
spherical polar coordinates, 148, 266, 362   
spurious solution, 160, 185   
standard deviation, 24

state transition matrix, 18, 21, 72, 74, 248   
state vector, 3, 15   
statistical quality control, 221, 232   
stretching, 253, 257   
superior conjunction, 304, 355, 367   
superposition principle, 262   
surface of variations, 214, 249   
survey, 10, 219   
symmetry breaking, 95, 104   
target function, 5, 60, 198   
target plane, 239   
terminator plane, 295, 300, 307   
terrestrial time, 359   
tesseral spherical harmonic, 271   
thermal emission, 294   
thermal sensitivity, 328   
time coordinates, 353, 359   
time-dependent first integral, 35   
time-shift invariance, 16   
timewise method, 333, 336   
tiny object boundary, 143, 156, 222   
too short arc, 133, 216   
topocentric correction, 180   
total mass, 43, 263, 272   
trace of the close approach, 239, 250   
tracking, 8   
tracklet, 85, 163, 216, 221   
management, 223, 229, 231   
tracks, 222   
trail, 251   
transmit time, 352   
transponder, 8, 352   
transversal, 291, 293, 316   
triangulated ephemerides, 155   
triangulation, 145   
true anomaly, 39, 100, 361   
two-body integrals, 39, 158

undetermined coefficients, 268 uniformly Lipschitz-continuous, 16 universal gravitational constant, 33, 261, 366

variance, 24, 25, 61   
variational equation, 18, 64, 276   
virtual asteroid, 148, 152, 156, 165, 206, 224, 248 debris, 165, 169 hazardous asteroids, 247 impactor, 251 impactor representative, 256

weak direction, 65, 95, 198, 200, 208   
weight matrix, 66, 83, 86, 367   
width, 256, 257

Yarkovsky effect, 297

zero circle, 187, 188, 213   
zonal spherical harmonic, 48, 109, 170, 269, 295, 341