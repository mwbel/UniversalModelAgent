Similarly,

$$
\mathbf { C } _ { i } ^ { \top } = \left( \Delta \mathbf { R } _ { i 1 } ^ { \top } \Delta \mathbf { R } _ { i 2 } ^ { \top } \Delta \mathbf { R } _ { i K } ^ { \top } \right) .
$$

Finally, taking into account that to each equation there corresponds different $\Delta \mathbf { P } _ { j k }$ and $\mathcal { M } _ { i k }$ , and that only the product of terms corresponding to the same $k$ are not zero, one has the summation over $j$ of

$$
\boldsymbol { B } _ { i j } ^ { \intercal } = \left( \boldsymbol { D } _ { i j 1 } ^ { \intercal } \quad \boldsymbol { D } _ { i j 2 } ^ { \intercal } \quad \ldots \quad \boldsymbol { D } _ { i j K } ^ { \intercal } \right) .
$$

with

$$
\begin{array} { r l } { \mathcal { D } _ { l j } = \mathcal { M } _ { i k } \ } & { \mathrm { ~ i f ~ } l = k \ \mathrm { a n d ~ } j = j _ { k } } \\ { = 0 } & { \mathrm { ~ o t h e r w i s e } . } \end{array}
$$

If the star is a reference star, the terms of Equation (14.16) are appended so that:

$$
\begin{array} { r l } & { \mathcal { A } _ { i } ^ { \top } = \left( \mathcal { U } _ { i 1 } ^ { \top } \ \mathcal { U } _ { i 2 } ^ { \top } \ \ldots \ \mathcal { U } _ { i K } ^ { \top } \ \mathcal { U } _ { i \mathrm { r } } ^ { \top } \right) , } \\ & { \mathcal { B } _ { i j } ^ { \top } = \left( \mathcal { D } _ { i j 1 } ^ { \top } \ \mathcal { D } _ { i j 2 } ^ { \top } \ \ldots \ \mathcal { D } _ { i j K } ^ { \top } 0 \right) , } \\ & { \mathbf { C } _ { i } ^ { \top } = \left( \Delta \mathbf { R } _ { i 1 } ^ { \top } \ \Delta \mathbf { R } _ { i 2 } ^ { \top } \ \ldots \ \Delta \mathbf { R } _ { i K } ^ { \top } \ \Delta \mathbf { R } _ { i \mathrm { r } } ^ { \top } \right) . } \end{array}
$$

# 14.5.2 Solution for all stars

Using the same convention for writing matrices as superposition of smaller matrices, the observational equations for all the $I$ stars can now be written as

$$
\mathcal { A } \times \Delta \mathbf { S } + \sum _ { j } \mathcal { B } _ { j } \times \Delta \mathbf { P } _ { j } = \mathbf { C } ,
$$

with

$$
\mathcal { A } = \left( \begin{array} { c c c c c c } { \mathcal { A } _ { 1 } } & { 0 } & { . } & { . } & { . } & { 0 } \\ { 0 } & { \mathcal { A } _ { 2 } } & { . } & { . } & { . } & { 0 } \\ { 0 } & { 0 } & { . } & { . } & { . } & { 0 } \\ { 0 } & { 0 } & { . } & { . } & { . } & { 0 } \\ { 0 } & { 0 } & { . } & { . } & { . } & { 0 } \\ { 0 } & { 0 } & { . } & { . } & { . } & { \mathcal { A } _ { I } } \end{array} \right)
$$

$$
\boldsymbol { B } _ { j } ^ { \intercal } = \left( \boldsymbol { B } _ { 1 j } ^ { \intercal } \boldsymbol { B } _ { 2 j } ^ { \intercal } \boldsymbol { \cdot } \boldsymbol { \cdot } \boldsymbol { B } _ { I j } ^ { \intercal } \right) ,
$$

$$
\mathbf { C } ^ { \top } = \left( \mathbf { C } _ { 1 } ^ { \top } \mathbf { C } _ { 2 } ^ { \top } \ldots \mathbf { C } _ { I } ^ { \top } \right) ,
$$

$$
\Delta \mathbf { S } ^ { \top } = \left( \Delta \mathbf { S } _ { 1 } ^ { \top } \Delta \mathbf { S } _ { 2 } ^ { \top } \dots \Delta \mathbf { S } _ { I } ^ { \top } \right) .
$$

Assuming there are $I$ stars and $M$ plates, the normal equations are

$$
\left( \begin{array} { c c c c c c c } { \mathcal { A } ^ { \top } \mathcal { A } } & { \mathcal { A } ^ { \top } \mathcal { B } _ { 1 } } & { \mathcal { A } ^ { \top } \mathcal { B } _ { 2 } } & { . } & { . } & { . } & { \mathcal { A } ^ { \top } \mathcal { B } _ { M } } \\ { \mathcal { B } _ { 1 } ^ { \top } \mathcal { A } } & { \mathcal { B } _ { 1 } ^ { \top } \mathcal { B } _ { 1 } } & { 0 } & { . } & { . } & { . } & { 0 } \\ { \mathcal { B } _ { 2 } ^ { \top } \mathcal { A } } & { 0 } & { \mathcal { B } _ { 2 } ^ { \top } \mathcal { B } _ { 2 } } & { . } & { . } & { . } & { 0 } \\ { . } & { . } & { . } & { . } & { . } & { . } & { 0 } \\ { . } & { . } & { . } & { . } & { . } & { . } & { 0 } \\ { \mathcal { B } _ { M } ^ { \top } \mathcal { A } } & { 0 } & { 0 } & { . } & { . } & { . } & { \mathcal { B } _ { M } ^ { \top } \mathcal { B } _ { M } } \end{array} \right) = \left( \begin{array} { c } { \Delta \mathbf { S } } \\ { \Delta \mathbf { P } _ { 1 } } \\ { \Delta \mathbf { P } _ { 2 } } \\ { . } \\ { . } \\ { . } \\ { \Delta \mathbf { P } _ { M } ^ { \top } \mathcal { \mathbf { A } } } \end{array} \right) \times \left( \begin{array} { c } { \mathcal { A } ^ { \top } \mathbf { C } } \\ { \mathcal { B } _ { 1 } ^ { \top } \mathbf { C } } \\ { \mathcal { B } _ { 2 } ^ { \top } \mathbf { C } } \\ { . } \\ { . } \\ { \mathcal { B } _ { M } ^ { \top } \mathbf { C } } \end{array} \right) .
$$

Advantage is taken of the fact that $\boldsymbol { B } _ { j } ^ { \intercal } \times \boldsymbol { B } _ { k } = 0$ , if $j \neq k$ . If the unknown vector of star coordinates $\Delta \mathbf { S }$ is now eliminated, the following system of reduced normal equations results:

$$
\left( \begin{array} { c c c c c c c } { \mathcal { F } _ { 1 1 } } & { \mathcal { F } _ { 1 2 } } & { . } & { . } & { . } & { \mathcal { F } _ { 1 M } } \\ { \mathcal { F } _ { 1 2 } ^ { \top } } & { \mathcal { F } _ { 2 2 } } & { . } & { . } & { . } & { \mathcal { F } _ { 2 M } } \\ & & & & & & \\ { . } & { . } & { . } & { . } & { . } & { . } & { . } \\ { . } & { . } & { . } & { . } & { . } & { . } & { . } \\ { \cdot } & { \cdot } & { . } & { . } & { . } & { . } & { \mathcal { F } _ { M M } } \end{array} \right) \times \left( \begin{array} { c } { \Delta \mathbf { P } _ { 1 } } \\ { \Delta \mathbf { P } _ { 2 } } \\ { . } \\ { . } \\ { . } \\ { \Delta \mathbf { P } _ { M } } \end{array} \right) = \left( \begin{array} { c } { \mathbf { G } _ { 1 } } \\ { \mathbf { G } _ { 2 } } \\ { . } \\ { . } \\ { . } \\ { \mathbf { G } _ { M } } \end{array} \right) ,
$$

with

$$
\begin{array} { r l } & { \mathcal { F } _ { j j } = \mathcal { B } _ { j } ^ { \top } \mathcal { B } _ { j } - \mathcal { B } _ { j } ^ { \top } \mathcal { A } ( \mathcal { A } ^ { \top } \mathcal { A } ) ^ { - 1 } \mathcal { A } ^ { \top } \mathcal { B } _ { j } , } \\ & { \mathcal { F } _ { j k } = - \mathcal { B } _ { j } ^ { \top } \mathcal { A } ( \mathcal { A } ^ { \top } \mathcal { A } ) ^ { - 1 } \mathcal { A } ^ { \top } \mathcal { B } _ { k } , \quad \mathrm { ~ f o r } \quad j \neq k , } \end{array}
$$

and

$$
\mathbf { G } _ { j } = \big ( \mathcal { B } _ { j } ^ { \top } - \mathcal { B } _ { j } ^ { \top } \mathcal { A } ( \mathcal { A } ^ { \top } \mathcal { A } ) ^ { - 1 } \mathcal { A } ^ { \top } \big ) \mathbf { C } .
$$

Because of the simple structure of $\mathcal { A }$ , one can write

$$
\begin{array} { r l } & { \mathcal { F } _ { j j } = \displaystyle \sum _ { i } \big ( \mathcal { B } _ { i j } ^ { \top } \mathcal { B } _ { i j } - \mathcal { B } _ { i j } ^ { \top } \mathcal { A } _ { i } \big ( \mathcal { A } _ { i } ^ { \top } \mathcal { A } _ { i } \big ) ^ { - 1 } \mathcal { A } _ { i } ^ { \top } \mathcal { B } _ { i j } \big ) , } \\ & { \mathcal { F } _ { j k } = - \displaystyle \sum _ { i } \big ( \mathcal { B } _ { i j } ^ { \top } \mathcal { A } _ { i } \big ( \mathcal { A } _ { i } ^ { \top } \mathcal { A } _ { i } \big ) ^ { - 1 } \mathcal { A } _ { i } ^ { \top } \mathcal { B } _ { i k } \big ) , \quad \mathrm { f o r } \quad j \ne k , } \\ & { \mathbf { G } _ { j } = \displaystyle \sum _ { i } \big ( \big ( \mathcal { B } _ { i j } ^ { \top } - \mathcal { B } _ { i j } ^ { \top } \mathcal { A } _ { i } \big ( \mathcal { A } _ { i } ^ { \top } \mathcal { A } _ { i } \big ) ^ { - 1 } \mathcal { A } _ { i } ^ { \top } \big ) \mathbf { C } _ { i } \big ) . } \end{array}
$$

The summations in these formulae are over all stars (i.e. the index $i$ ), but $B _ { i j }$ is zero if star $i$ does not appear on plate $j$ . Thus, the summation in (14.28) is taken over all stars which are common on plates $j$ and $k$ , and $\mathcal { F } _ { j k }$ is a zero matrix if there are no such stars. Since the matrices $B _ { i j }$ contain so many zeros, the matrix products in formulae (14.27) to (14.29) contain many trivial multiplications. These unnecessary computations can be avoided, if the following equations are used, as may be seen from Equations (14.19)–(14.23):

$$
\begin{array} { r l r } {  { \mathcal { B } _ { i j } ^ { \top } \mathcal { B } _ { i j } = \sum _ { k } \mathcal { M } _ { i k } ^ { \top } \mathcal { M } _ { i k } , } } \\ & { } & { \mathcal { A } _ { i } ^ { \top } \mathcal { B } _ { i j } = \sum _ { k } { \mathcal { U } _ { i k } ^ { \top } \mathcal { M } _ { i k } } , } \\ & { } & { \mathcal { B } _ { i j } ^ { \top } { \mathbf { C } } _ { i } = \sum _ { k } { \mathcal { M } _ { i k } ^ { \top } \mathbf { R } _ { i k } } , } \end{array}
$$

where the summations are over $k$ , representing the measurements of the $i$ th star made on the $j$ th plate. In addition, one has:

$$
\begin{array} { r l r } { \mathcal { A } _ { i } ^ { \top } \mathcal { A } _ { i } = \displaystyle \sum _ { k } \mathcal { U } _ { i j k } ^ { \top } \mathcal { U } _ { i j k } } & { } & { \mathrm { f o r ~ f i e l d ~ s t a r s } } \\ { = \displaystyle \sum _ { k } \mathcal { U } _ { i j k } ^ { \top } \mathcal { U } _ { i j k } + \mathcal { U } _ { i \mathrm { r } } ^ { \top } \mathcal { U } _ { i \mathrm { r } } } & { } & { \mathrm { f o r ~ r e f e r e n c e ~ s t a r s } , } \end{array}
$$

and

$$
\begin{array} { r l r } { \boldsymbol { \mathcal { A } } _ { i } ^ { \top } { \bf C } _ { i } = \displaystyle \sum _ { k } \boldsymbol { \mathcal { U } } _ { i j k } ^ { \top } \Delta { \bf R } _ { i j k } } & { \mathrm { ~ f o r ~ f i e l d ~ s t a r s } } \\ { \quad \quad \quad } & { = \displaystyle \sum _ { k } \boldsymbol { \mathcal { U } } _ { i j k } ^ { \top } \Delta { \bf R } _ { i j k } + \boldsymbol { \mathcal { U } } _ { i \mathrm { r } } ^ { \top } \Delta { \bf R } _ { i \mathrm { r } } } & { \mathrm { ~ f o r ~ r e f e r e n c e ~ s t a r s . } } \end{array}
$$

Once these matrices are calculated all the combinations needed for the summations in Equations (14.27)–(14.29) can be found by using arithmetic operating on small matrices.

For the solution of the plate constant normal equations for the overlap pattern, the component matrices $\mathcal { F } _ { j k }$ of the plate constant normal equations will be zero, whenever there are no stars common on the plates $j$ and $k$ , and there are no model constraints relating the constants of the two plates. If one neglects for the moment all constraints, then the plate constant normal equation coefficient matrix for a typical zonal pattern, in which every star appears on exactly two plates which overlap in right ascension only, assumes the form

$$
\left( \begin{array} { c c c c c c c } { \mathcal { F } _ { 1 1 } } & { \mathcal { F } _ { 1 2 } } & { 0 } & { . } & { . } & { . } & { \mathcal { F } _ { 1 M } } \\ { \mathcal { F } _ { 1 2 } ^ { \top } } & { \mathcal { F } _ { 2 2 } } & { \mathcal { F } _ { 2 3 } } & { . } & { . } & { . } & { 0 } \\ { 0 } & { \mathcal { F } _ { 2 3 } ^ { \top } } & { \mathcal { F } _ { 3 3 } } & { . } & { . } & { . } & { 0 } \\ { . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } \\ { . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } \\ { . } & { . } & { . } & { . } & { . } & { . } & { . } & { . } \\ { \mathcal { F } _ { 1 M } ^ { \top } } & { 0 } & { 0 } & { . } & { . } & { . } & { \mathcal { F } _ { M M } } \end{array} \right) .
$$

Only three non-zero submatrices appear in any row. Because of the symmetry, for computational purposes it is only necessary to store two sub-matrices per row. However, even with so many sub-matrices, the number of elements is considerable. For example, for 90 plates and 24 plate constants per plate, more than 100 000 elements require storage. So it is advantageous not to introduce any more non-trivial elements than absolutely necessary. Thus, it is desirable not to introduce constraints on plate constants of pairs of non-overlapping plates. Methods of introducing constraints on the plate constants are given in Googe et al. (1970). Once the corrections to the plate constants have been found, the corrections to the celestial coordinates are given by

$$
\Delta \mathbf { S } _ { i } = \left( \mathcal { A } _ { i } ^ { \top } \mathcal { A } _ { i } \right) ^ { - 1 } \left( \mathcal { A } _ { i } ^ { \top } \mathbf { C } _ { i } - \sum _ { j } \mathcal { A } _ { i } ^ { \top } \mathcal { B } _ { i j } \Delta \mathbf { P } _ { j } \right) .
$$

Then $A _ { i } , B _ { i }$ , and $\mathbf { C } _ { i }$ should be evaluated from Equations (14.19) and (14.21) for reference stars as well as field stars.

Modifications or improvements on the overlapping plate method have been given in terms of quaternions (Jefferys, 1987), orthogonal functions (Brosche et al., 1989), and a new principle of statistical estimation (Taff, 1988). The overlapping plate technique has also been suggested as a means of developing star catalogs from existing catalog material (Taff et al., 1990a,b).

The existence of many Schmidt plates taken as all sky surveys reaching as faint as 21st magnitude provided the opportunity to develop very large astrometric positional catalogs for such faint magnitudes (Monet, 1998; Russell et al., 1990). The challenge was how to obtain the best accuracy in the presence of the distortions of Schmidt plates. A number of techniques were developed and tested as part of the preparation of the Space Telescope Guide Star Catalog and the US Naval Observatory’s massive A and B, and smaller SA and SB catalogs. These methods might be called the filtering, mask, plate modeling, and infinitely overlapping circles approaches (Taff et al., 1990a,b; Lattanzi and Bucciarelli, 1991). The filtering and mask methods remove small-scale systematics, but the mask technique does not handle plate-to-plate variations. It also requires a large collection of plates that have been taken on the same telescope, same filter, same exposure and emulsion, and measured on the same measuring machine. Thus, the mask technique is best suited for reduction of large plate data bases. The filter technique requires a dense reference catalog. The plate model and mask technique give an indication of what is being modeled, and the plate model gives an estimate of the errors remaining. The combination of the mask and filter techniques can remove the systematics that are common to all the plates, while the mask method and the filter technique remove the smaller individual plate systematics (Morrison et al., 1998). It has been found that there is a coma-like term, which is a function of magnitude and radial distance from the plate center, in Schmidt plates (Morrison et al., 1996).

# 14.5.3 Global solutions

Global solutions, or block adjustments, techniques can be used to achieve wideangle astrometric results from differential narrow-field observations. Overlapping fields are required for this approach. Instead of solving for individual plate parameters, the reduction scheme solves for all plate parameters and star positions simultaneously using the fact that each star has one unique position in the sky as observed on all CCDs or plates.

This technique was developed in the 1960s, but not really applied until the 1970s owing to the computer capabilities required. The method is very sensitive to any systematic effects not included in the model, and can thus lead to results that are worse than traditional methods, if the technique is not properly applied.

The Hipparcos sphere reconstruction process is an example of global solutions. Hipparcos has the advantage of providing many observations of each star as well as simultaneous observations of widely separated fields. This leads to a better conditioned global solution than overlapping fields.

# 14.6 Radio observations

At the present time, Very Long Baseline Interferometry (VLBI) observations of distant radio sources give the most accurate astrometric positions. These positions determine the International Celestial Reference Frame (ICRF). Since the sources are very distant, there are no apparent proper motions of the sources. However, owing to the physics of the generating sources, they are subject to changes in the source structure which has the characteristic of temporal changes in the positions. The VLBI observations are made of many sources from multiple sites over a period of time. They are made from the rotating Earth, so they are subject to all the kinematics of the Earth including the moving equator. Solutions of radio-source positions must be made in conjunction with solutions for many other parameters, such as station locations, Earth orientation parameters, precession–nutation, atmospheric effects, etc. For details, see chapter 12 of Thompson et al. (1986).

# 14.7 Millisecond pulsars

Millisecond pulsars require precise reduction procedures in order to achieve the full accuracy possible from their observations. They provide, in turn, a variety of information and tests on the accuracies of astrometry, relativity, and time. If the millisecond pulsars maintained constant rates, they could serve as independent sources of accurate time, and thus verify the accuracies of atomic time standards on Earth. The reduction of millisecond pulsars to the barycenter of the Solar System requires accurate ephemerides and masses of the bodies of the Solar System. Periodic variations in the pulsar data can indicate the inaccuracies in the reduction procedure. The determinations of the positions of the pulsars can be used as calibrators of the accuracy of the reference system to which the positions have been referred. Also, the millisecond pulsars provide tests of the theory of relativity. So, in general, pulsars that have been “recycled” through a process of mass exchange in an evolving binary star are believed to be rapidly spinning, strongly magnetized neutron stars with energetics dominated by their spindown luminosities. Their evolution has been modified by an accretion episode in which mass and angular momentum were transferred from an orbiting companion star. While recycled pulsars comprise only a small fraction of pulsars, they are older, spin faster, and have smaller magnetic fields than ordinary pulsars. Thus, they are the most demanding on astrometric reduction procedures, but also the most fruitful for results (Backer and Hellings, 1986; Rawley et al., 1988; Taylor, 1992).

The timing of the arrival of a pulse requires proper handling of the polarization of the signal, accurate prediction of the true period and Doppler offset, averaging of the pulse profile, determination of a fiducial point of the pulse, and cross correlation of each average with a template of a high-sensitivity averages to produce the UTC time of arrival of a pulse at the observatory with an accuracy of about 0.001 period. The observatory UTC scale requires correction to a national standard UTC, then to TAI, and then to TCB (see Section 5.5), to achieve a uniform time as seen by an external observer. A correction for dispersion in the interstellar plasma is made by computing the total path delay at the barycentric observing frequency. The TCB times of arrival are related to the TCB times of emission by a model that includes the motion of the Earth, the motion of the pulsar, and the time of flight of the photons from the pulsar to the Earth.

The emission times $T _ { N }$ are modeled by the “pulsar spin equation”, which contains polynomial terms for the rotational phase $N _ { 0 }$ at time $T _ { 0 }$ , the spin rate $\varOmega$ , its acceleration $\dot { \varOmega }$ , as well as, in some cases, the second derivative $\ddot { \varOmega }$ . The equation is

$$
N ( T ) = N _ { 0 } + \varOmega ( T - T _ { 0 } ) + \frac 1 2 \dot { \varOmega } ( T - T _ { 0 } ) ^ { 2 } + \frac 1 6 \ddot { \varOmega } ( T - T _ { 0 } ) ^ { 3 } .
$$

The seven pulsar parameters are pulse epoch, rotation rate, rotation acceleration or spinup, right ascension, declination, proper motion in right ascension, and proper motion in declination. Additional parameters are required for binary pulsars. Pulsar spins are decelerated by electro-magnetic torque. The deterministic spin parameters are determined by iterative least squares analysis of arrival time data, leaving residuals characterized by random jitter, discontinuities, and slow variations, or noise. Some pulsars have better characteristics than others.

# 14.7.1 Times used

In the following treatment of the pulsar timing observations, we shall restrict ourselves to the following terms of the general relativity metric (5.22) reduced to its second-order terms in $c ^ { - 2 }$ :

$$
\begin{array} { l } { { \displaystyle g _ { 0 0 } = - 1 + \frac { 2 U } { c ^ { 2 } } + \mathrm { O } ( c ^ { - 4 } ) } } \\ { { \displaystyle g _ { i i } = 1 + 2 \frac { U } { c ^ { 2 } } + \mathrm { O } ( c ^ { - 4 } ) } } \\ { { \displaystyle g _ { 0 i } = \mathrm { O } ( c ^ { - 3 } ) , } } \end{array}
$$

where $c$ is the speed of light and $U$ is the gravitational potential, that we write assuming that the Sun and planets are point-like objects (Equation (5.17)):

$$
U = \sum _ { p } { \frac { G m _ { p } } { | \mathbf { r } - \mathbf { r } _ { p } | } }
$$

where $\mathbf { r } _ { p }$ is the coordinate of the $p$ th body, $\mathbf { r }$ is the coordinate of the field point, and the sum is over the Sun and planets of the Solar System. The origin of the coordinate system, chosen to be the Solar System barycenter, must be approximately at rest relative to the mean rest frame of its gravitational sources, for the higher-order terms of (14.34) to remain small. More terms are required in (14.34) to describe the dynamics of the Solar System to modern accuracies of observation (postlinear terms in $g _ { 0 0 }$ and $g _ { 0 i }$ are needed), but the form is sufficient to discuss the principle of relativistic timing effects. Other terms could be added at will, and actually are necessary for precise pulsar timing.

Equation (14.34) defines the physical significance of the time coordinate. It is the time of a clock infinitely far from the Solar System and at rest with respect to the Solar System. In practice, among possible equivalent time scales, the present choice is the Barycentric Coordinate Time (TCB), which describes the dynamics of pulsars, planets, and photons. The observations are made in a local time scale, which is linked to the TAI or the Terrestrial Time (TT), called here $\tau$ , which is kept by terrestrial clocks. These two times are related by Equation (5.25), the “proper time equation”,

$$
{ \frac { \mathrm { { d } } \tau } { \mathrm { { d } } t } } = { \sqrt { 1 - { \frac { 2 U } { c ^ { 2 } } } - { \frac { v ^ { 2 } } { c ^ { 2 } } } } } ,
$$

where $\mathbf { r } ( t )$ is the location of the clock on the surface of the Earth, ${ \bf v } = \dot { \bf r }$ is the coordinate velocity of the clock, and $U ( \mathbf { r } )$ is the instantaneous total gravitational potential at the clock’s location. The relation between TCB and TT is given by Equations (5.37) and (5.39).

For $\mathrm { P S R } 1 9 3 7 + 2 1$ , time transformation accuracy of the order of 100 ns over decades of observations is required. In (14.34) higher-order terms arising from the $c ^ { - 4 }$ term in $g _ { 0 0 }$ and $g _ { i i }$ , as well as from postlinear terms in $g _ { 0 i }$ as given by (5.22) are of order $1 0 ^ { - 1 6 }$ for terrestrial clocks and should be considered. It was developed by the BIPM/IAU Joint Committee on Relativity (Petit, 2000).

Millisecond and binary pulsars exhibit very stable spinning and/or orbital periods, so their rotational, or orbital, phases might be used as time references, generally named pulsar time scale (PT) and binary pulsar time scale (BPT). Theoretical and observational investigations of the stabilities of PT and BPT have been considered (Matsakis and Foster, 1996; Ilyasov et al., 1998). The PT is not ideally uniform, owing to variations of the phase of rotation, stochastic variations in the delay of signal through the interstellar medium, and errors in determining the relative position of the observer and the pulsar. In certain situations the scale of BPT is far more stable than PT; however, the accuracies are limited by the presence of noise (Deshpande et al., 1996). While pulsar timing data are improving by increased time periods of data and more accurate observations, terrestrial atomic time standards are also improving in accuracy. Pulsar data from the 1980s were probably degraded by the instabilities of the terrestrial time scales used at that time. Comparisons of real pulsar data and terrestrial time scales show that these two kinds of data currently have comparable stabilities (Matsakis et al., 1997; Kaspi et al., 1994).

Pulsar rates of rotation are determined by evolutionary circumstances, not by fundamental constants of nature such as control atomic clocks. Therefore, the second should not be defined by the pulsar frequencies. If a number of pulsars are observed regularly, an ensemble average pulsar time scale should be possible. It might have better long-term stability than existing time standards, and could establish relative instabilities of different realizations of terrestrial time.

# 14.7.2 Time arrival model

Once the terrestrial observations of pulse arrival times are transformed into the coordinate time of reception, a model is needed for determining the coordinate time of reception as a function of the coordinate time of emission of the pulse. Models of pulse arrival times have been published by Manchester and Taylor (1977), Downs and Reichley (1983), and Hellings (1986).

Assuming the pulsar is at $\mathbf { R } _ { 0 }$ at some time $T _ { 0 }$ and has a velocity $\mathbf { V } _ { 0 }$ , its position at the time of emission of the $N$ th pulse is

$$
\mathbf { R } _ { N } = \mathbf { R } _ { 0 } + \mathbf { V } _ { 0 } ( T _ { N } - T _ { 0 } ) .
$$

The vector $\mathbf { V } _ { 0 }$ includes both radial and transverse, or proper, motion components. The position of the receiving station on the Earth is $r _ { N }$ at time $t _ { N }$ when the $N$ th pulse is received. $\mathbf { r } _ { N }$ is the sum of two terms, $\mathbf { q } _ { N }$ , the position of the center of the Earth at time $\mathbf { t } _ { N }$ with respect to the barycenter of the Solar System, and $\mathbf { p } _ { N }$ , the intersection of the rotation axes of the antenna relative to the center of the Earth at the same time. $\mathbf q _ { N }$ is found from numerical integration of the equations of motion in ICRS, and ${ \bf p } _ { N }$ is found from known station coordinates and a known Earth rotation model.

The photons from the pulsar will follow null trajectories of the geometry. The first-order coordinate system with metric of (14.34) and (14.35) is used. Neglecting second-order terms introduces an error of less than 1 ns in absolute time of flight for crossing the Solar System. To first order the line element is

$$
\begin{array} { r } { \mathrm { d } \sigma ^ { 2 } = ( - 1 + 2 U ) c ^ { 2 } \mathrm { d } t ^ { 2 } + ( 1 + 2 U ) ( \mathrm { d } x ^ { 2 } + \mathrm { d } y ^ { 2 } + \mathrm { d } z ^ { 2 } ) = 0 . } \end{array}
$$

Considering that the signal path is not deviated by the gravitational field of the Sun, as a first approximation, introduces a maximum error of 36 ns. Assuming that the Sun and planets are at rest during the signal passage, causes an error in the time delay by each body by the factor of the ratio of its speed to $c$ . The expression for the time of flight of the $N$ th pulse from a pulsar at $\mathbf { R } _ { N }$ to the Earth at $\mathbf { r } _ { N }$ is determined by integrating (14.38) along the path from $( T _ { N } , { \bf R } _ { N } )$ to $( t _ { N } , { \bf r } _ { N } )$ , with the result being

$$
c ( t _ { N } - T _ { N } ) = | { \bf R } _ { N } - { \bf r } _ { N } | - 2 \sum _ { p } \frac { G m _ { p } } { c 2 } \ln \left[ \frac { \bf n \cdot r _ { \it p N } + r _ { \it p N } } { \bf n \cdot R _ { \it p N } + R _ { \it p N } } \right] ,
$$

where $\mathbf { r } _ { p N }$ is the position of the receiver relative to the $p$ th Solar System body at the time of closest approach of the photon to that body, and $\mathbf { R } _ { p N }$ is the pulsar’s position relative to body $p$ at time $T _ { N }$ . Vector $\mathbf { n }$ is a unit vector in the direction of the pulsar. The sum in (14.39) is over all bodies along the photon path from the pulsar to the Earth, including interstellar objects. Unless the pulsar’s line of sight lies close to some intervening object, the interstellar gravitational fields will be essentially constant over decades and need not be modeled. The delay due to the pulsar’s gravitational field will also be constant. It may be necessary to include the effects of the planets, because Jupiter’s gravitational field, for example, can cause a signal delay of as much as 200 ns.

Using (14.37) to expand the source position and assuming that the pulsar is very far away so that $V _ { 0 } ( T _ { N } - T _ { 0 } ) \ll R _ { 0 }$ and $\mathbf { n } \sim \mathbf { R } _ { 0 } / R _ { 0 }$ , then (14.39) becomes

$$
\begin{array} { l } { { \displaystyle c t _ { N } = c T _ { N } + [ ( { \bf n } \cdot { \bf V } _ { 0 } ) \Delta t _ { N } - ( { \bf n } \cdot { \bf r } _ { N } ) ] } \ ~ } \\ { { \displaystyle ~ - \ \frac { 1 } { R _ { 0 } } [ { \bf V } _ { 0 } \cdot { \bf r } _ { N } - ( { \bf n } \cdot { \bf V } _ { 0 } ) ( { \bf n } \cdot { \bf r } _ { N } ) ] \Delta t _ { N } } \ ~ } \\ { { \displaystyle ~ + \frac { 1 } { 2 R _ { 0 } } \big [ r _ { N } ^ { 2 } - ( { \bf n } \cdot { \bf r } _ { N } ) ^ { 2 } \big ] + \frac { 1 } { 2 R _ { 0 } } \big [ V _ { 0 } ^ { 2 } - ( { \bf n } \cdot { \bf V } _ { 0 } ) ^ { 2 } \big ] \Delta t _ { N } ^ { 2 } } \ ~ } \\ { { \displaystyle ~ - 2 \sum _ { p } \frac { G m _ { p } } { c ^ { 2 } } \ln \Big | \frac { { \bf n } \cdot { \bf r } _ { p N } + r _ { p N } } { 2 R _ { 0 } } \Big | } , \ ~ } \end{array}
$$

where the definition

$$
\Delta t _ { N } = t _ { N } - t _ { 0 } \sim T _ { N } - T _ { 0 }
$$

is introduced. The combination

$$
T _ { 0 } + \frac { R _ { 0 } } { c } + 2 \sum _ { p } \frac { G m _ { p } } { c ^ { 2 } } \ln ( 2 R _ { 0 } )
$$

is the zero-order time of arrival of the pulses at the Solar System. Defining this time as the Solar System time origin $t _ { 0 }$ , then (14.40) becomes

$$
\begin{array} { l } { { \displaystyle c ( t _ { N } - t _ { 0 } ) = c ( T _ { N } - T _ { 0 } ) + [ ( { \bf n } \cdot { \bf V } _ { 0 } ) \Delta t _ { N } - ( { \bf n } \cdot { \bf r } _ { N } ) ] } \ ~ } \\ { { \displaystyle ~ - \frac { 1 } { R _ { 0 } } [ { \bf V } _ { 0 } \cdot { \bf r } _ { N } - ( { \bf n } \cdot { \bf V } _ { 0 } ) ( { \bf n } \cdot { \bf r } _ { N } ) ] \Delta t _ { N } } \ ~ } \\ { { \displaystyle ~ + \frac { 1 } { 2 R _ { 0 } } \big [ r _ { N } ^ { 2 } - ( { \bf n } \cdot { \bf r } _ { N } ) ^ { 2 } \big ] + \frac { 1 } { 2 R _ { 0 } } \big [ V _ { 0 } ^ { 2 } - ( { \bf n } \cdot { \bf V } _ { 0 } ) ^ { 2 } \big ] \Delta t _ { N } ^ { 2 } } \ ~ } \\ { { \displaystyle ~ - 2 \sum _ { p } \frac { G m _ { p } } { c ^ { 2 } } \ln \vert { \bf n } \cdot { \bf r } _ { p N } + r _ { p N } \vert + \Delta t _ { D M } } . } \end{array}
$$

The first term on the right-hand side involves the model of the rotational dynamics of the pulsar, the second term is the first-order Doppler delay, the third term, which is proportional to $\Delta t _ { N }$ , comes from the pulsar’s proper motion, and the fourth term gives the effects of annual parallax. The $\Delta t _ { N } ^ { 2 }$ term arises from the increase in distance to the pulsar with time, if the pulsar has radial motion. The log term is the gravitational delay caused by space-time curvature and term $\Delta t _ { D M }$ represents the plasma delay.

The predicted time of arrival of the $N$ th pulse is explicitly a function of the constant parameters n, $\mathbf { V } _ { 0 }$ , and $\mathbf { R } _ { 0 }$ , but implicitly a function of all parameters in the numerical integration of planetary positions determining $\mathbf { r } _ { N }$ . All of these parameters may be adjusted in fitting the model to the observed arrival times. The term $T _ { N } - T _ { 0 }$ is modeled by assuming that the pulsar rotation is a simple polynomial in time (14.33) with parameters to be adjusted to fit the data. The timing data are the only source of information about these parameters.

The vector $\mathbf { n }$ gives the right ascension and declination of the pulsar at time $T _ { 0 }$ . The arrival time data can be analyzed to determine positions (Manchester and Taylor, 1977). Independently, positions of pulsars can be determined by radio interferometric techniques. The two techniques can lead to differences in the determined positions. The differences can be due to uncertainties in Solar System ephemerides, reference frames, instabilities in the reference time standards, uncompensated changes in the propagation medium, rotational instabilities in the pulsars, and cosmic background of low frequency gravitational waves. The two components of proper motion contained in $\mathbf { V } _ { 0 }$ are determined from the timing equation and by astrometry with interferometry. The accuracy of the proper motion solutions from pulsar arrival times is the result of slowly varying “noise” in pulsar arrival times. VLBI observations are able to determine parallaxes for nearby pulsars, and arrival time data can be used for determining parallaxes from (14.41) for some pulsars.

![](images/02258626437bcc88d1b08ca4814a13a5af6acf62d27d55875e38ee2e9f10b7ce.jpg)  
Fig. 14.3. Detail of a single impulse received from pulsar $0 9 5 0 + 0 8$ and the mean profile folded from 300 individual observations (adapted from Stinebring, 1982).

Individual radio profiles of a pulse are very irregular as shown in Fig. 14.3. Only after integration over a large number of periods can one obtain a smooth reproducible profile. The timing information is deduced from these integrated curves, which still show noise. There are many types of noise that may be present in the residuals. Taylor (1991) has proposed a dimensionless fractional instability, $\sigma _ { z }$ , which is an extension of the Allan variance (Section 4.5.3) This is a method to characterize the stability of pulsar time of arrivals.

However, the most common model is based on a mathematical description of several types of noise due to interstellar medium density fluctuations, the imperfections of planetary ephemerides and atomic clocks: random noise, white noise, frequency dependent noise, flicker noise, etc.

The usual premise for estimating pulsar parameters is that white noise dominates the time of arrival residuals. However, long-term monitoring of some pulsars has revealed the presence of a non-white component of noise that is of astrophysical origin (Kaspi et al., 1994; Deshpande et al., 1996). Such correlated noise is usually referred to as a colored Gaussian noise, or red noise, because its spectrum diverges at zero frequency. The red noise has a non-flat spectrum at low frequencies and can be represented by a single- or multiple-component power-law model. Although it is difficult to detect, the red noise contains information about the physical processes that take place in the neutron star interior, the interstellar medium, the early Universe, and terrestrial clocks. Thus, a rigorous method of treating red noise in the pulsar timing residuals has been of interest for a long while, and statistical procedures have been undertaken by Bertotti et al. (1983) and Blandford et al. (1984) to obtain unbiased estimates of pulsar parameters. There remains the need to improve statistical analysis of pulsar timing observational data in the presence of red noise as indicated by Bertotti et al. (1983), Blandford et al. (1984), and Kopeikin (1997, 1999).

The Solar System observations, including spacecraft, laser and radar ranging, VLBI, and optical, provide accurate means of determining the planetary ephemerides. However, the pulsar data become very precise tests of the motions of the planets and the Solar System barycenter, and should be used to indicate discrepancies in the Solar System ephemerides. In particular, the position of the Earth relative to the barycenter is not a well-determined quantity in the ephemerides. Variations in the barycenter in an absolute sense do not affect the relative motions of the planets, however, they can introduce periodicities in the Earth uncertainties. The effects of the uncertainties in masses of bodies in the asteroid belt and outer Solar System can affect the barycenter and pulsar timing data.

When the pulsar is a member of a binary system, then the pulse arrival time model is more complex. This is discussed, along with the relativistic description of the point mass binary, by Backer and Hellings (1986). Advanced developments of the motions of binary systems in general relativity are by Iyer and Will (1995), Jaranowski (1997), and Jaranowski and Shafer (1997).

Results of the applications of the above methods to pulsar observations are given, as examples, in Taylor and Weisberg (1989), Ryba and Taylor (1991a,b), and Kaspi et al. (1994).

# 14.8 Extrasolar planets

The discovery of planets around stars other than our Sun has been a goal for a long time. There have been many different methods pursued for this purpose. The efforts divide as a function of mass and period of the planet, with the size of the perturbations being a function of the planetary mass and the length of observations required being a function of the planetary period. The first planetary system discovered outside our Solar System was found around a neutron star, the $6 . 2 \mathrm { m s }$ pulsar PSR $1 2 5 7 + 1 2$ (Wolszczan and Frail, 1992). Other planets have been detected by means of the measurement of variations in the radial velocities of stars. The astrometric measurement of periodic motions of stars has, to date, detected double stars, but not bodies small enough to be called planets. The photometric detection of the reduction of light from a star owing to the transit of a planet in front of the star is another means of detecting planets. Microlensing is a means of detecting more-distant planets. Another, more difficult, means of finding planets is the direct observation of the planet next to a star. The large difference in the light from the two bodies requires that some technique be used to reduce the light from the star, but not from the nearby planet. Techniques such as optical nulling are required.

After many false claims in the past, current surveys are indicating that $5 \%$ of main-sequence stars have companions of 0.5–8 Jupiter masses within 3 AU. The future for planetary discovery using the techniques below should be very bright.

# 14.8.1 Doppler technique

A star wobbles around the system barycenter as a result of the perturbations of planets in the system. For the Sun, the wobble due to Jupiter is $1 2 . 5 \mathrm { m } / \mathrm { s }$ , and that due to Saturn is $2 . 7 ~ \mathrm { m } / \mathrm { s }$ . The general expression for the semi-amplitude, $K$ , of the wobble of the stellar radial velocity due to an orbiting companion is given by Equation (12.29b):

$$
K = { \frac { n a \sin i } { \sqrt { 1 - e ^ { 2 } } } } ,
$$

where $a$ is the semi-major axis, $n$ is the mean motion, $e$ is the eccentricity, of the relative orbit of the companion about the primary, and $i$ is the inclination of the orbit to the plane of measurement of $K$ . Introducing the orbital period $P = 2 \pi / n$ and Kepler’s third law,

$$
P ^ { 2 } = \frac { 4 \pi ^ { 2 } a ^ { 3 } } { G ( M _ { \star } + m _ { \mathrm { p } } ) } ,
$$

where $m _ { \mathrm { p } }$ is the mass of the planet and $M _ { \star }$ is the mass of the primary, one gets:

$$
K = \left( \frac { 2 \pi G } { P } \right) ^ { 1 / 3 } \frac { m _ { \mathrm { p } } \sin i } { \left( M _ { \star } + m _ { \mathrm { p } } \right) ^ { 2 / 3 } } \frac { 1 } { \sqrt { 1 - e ^ { 2 } } } .
$$

Thus, a Jupiter mass planet at 1 AU causes an amplitude of $2 8 . 0 \sin i \mathrm { m } / \mathrm { s }$ , which is now easily detectable. For a given amplitude, the detectability depends on the Doppler precision, the number of orbital cycles, and the number of observations per cycle. For orbital periods much shorter than the duration of observations, the use of Fourier analysis permits the detection of velocity amplitudes comparable to the Doppler errors. For orbital periods comparable to the observational history, detection requires amplitudes about four times the errors. As an example, Fig. 14.4 gives the graph of radial velocities that allowed Mayor and Queloz (1995) to report the first discovery of such an object around $5 1 \ \mathrm { P e g }$ . The distance of $5 1 \ \mathrm { P e g }$ as determined by Hipparcos is $1 3 . 5 ~ \mathrm { p c }$ . The discovered companion is a Jupiter-like planet. Because the inclination $i$ could not be determined, one obtained only

$M$ cos $i = 0 . 4 7$ Jupiter masses.

![](images/00f8e80c3765d68e36d1578dd1254bc8d819ebe3bec3e356a35e6f19cb2ab7af.jpg)  
Fig. 14.4. Observations during one year of the radial velocity of $5 1 \mathrm { P e g }$ with their uncertainties that led to the discovery of its planetary companion. Time in days is folded to the period of the system.

The period is 4.23 days, which means that the distance between the star and the planet is of the order of 0.09 AU, that is much closer than Mercury to the Sun. Now, every year, many new similar systems of a star accompanied by one or more close Jupiter-like planets are discovered by the Doppler method. In August 2000, at the General Assembly of the IAU, 48 extra-solar planets were known, and this number increases every month. In particular, three multi-planet systems had already been detected by that date.

The instrument designs, observational techniques, analysis methods, results, planet properties, and implications for Solar System formation are given in Serkowski (1976), Mayor and Queloz (1995), Marcy and Butler (1992, 1993, 1998, 1999, 2000), and Cummings, Marcy, and Butler (1999).

# 14.8.2 Astrometric technique

The angular wobble of a star due to a companion is proportional to both planet mass, $m _ { \mathrm { p } }$ , and orbital radius, $r$ in AU, and inversely proportional to the distance to the star, $D$ in parsecs, and its mass, $M _ { \star }$ . The masses are in solar masses. The

amplitude of the astrometric signal, $\theta$ , in arcseconds is given by

$$
\theta = \left( \frac { m _ { \mathrm { p } } } { M _ { \star } } \right) \left( \frac { r } { D } \right) = \left( \frac { m _ { \mathrm { p } } } { D } \right) \left( \frac { P } { M _ { \star } } \right) ^ { 2 / 3 } .
$$

Gatewood has formulated this, for stars of known parallax and mass, into a detection index, $I$ , which is given as

$$
I = \frac { A } { m P ^ { 2 / 3 } } = \frac { \varpi } { M ^ { 2 / 3 } } ,
$$

where $\varpi$ is the stellar parallax, $m$ and $M$ are masses of the companion and primary respectively, and $A$ is the semi-major axis of the stellar motion.

The observational equation (14.1) is the basis for the astrometric technique. After the observations are corrected for observational effects, such as aberration, refraction, and nutation as discussed in Chapters 6 and 8, the position, proper motion and parallax constants can be determined by least squares. Then the problem is detecting the planetary induced perturbations in the presence of the noise of observational errors. There are some possible practical problems separating the linear perturbation effect from the proper motion term and the perturbations from the annual parallax terms, if the periods are close.

To achieve the accuracy required for planetary detection by the astrometric technique, photoelectric techniques have been introduced into astrometry. The approaches divide into images on the detector surface, modulating the light before it reaches the detector’s surface, and interferometry. Gatewood (1987) has built the multichannel astrometric photometer with a Ronchi ruling and applied it on ground-based telescopes. Narrow-angle astrometry with long-baseline infrared interferometry can exploit the atmospheric turbulence properties over fields smaller than the baseline, and use phase referencing with a reference star in the isoplanatic patch. Using baselines $> 1 0 0 \mathrm { m }$ to minimize the photon-noise errors, and controlling systematic errors using laser metrology, accuracies of tens of microarcseconds per hour should be possible. The better approach is to observe from above the atmosphere, therefore missions such as FAME, SIM, and GAIA are well adapted for such investigation.

At present, only some heavy brown dwarfs have been discovered by this technique, precisions of the order of a milliarcsecond being insufficient to recognize slight nonlinearities of the proper motion of a star owing to the shift produced by the presence of small mass objects. Figure 14.5 illustrates this by showing what could be the apparent motion of the Sun as seen at $1 0 0 \ \mathrm { p c }$ perpendicularly to the plane of the ecliptic. This motion is essentially governed by the motion of the outer planets and would be observable only if accuracies of the order of $1 0 ~ \mu \mathrm { { a s } }$ were available. In addition, in order to detect the Earth or Venus, one should be able to recognize small periodic perturbations with periods of 1 and 0.6 years respectively and amplitudes smaller by a factor of about 2000 than the global amplitude shown in figure. So the recognition of terrestrial planets might be only marginally possible for the closest stars with microarcsecond astrometry.

![](images/e2cbe94f1b01a49aa30015d1a05e85864b0df05a32a095c911e64bdd28da85c5.jpg)  
Fig. 14.5. Apparent motion of the Sun as seen from $1 0 0 \mathrm { p c }$ .

Reviews of the astrometric approach to planet detection have been written by Black and Scargle (1982), Gatewood (1976, 1987), Gatewood et al. (1980), Colavita and Shao (1994), and Black (1995). The astrometric technique determines the mass and orbital inclination of a planet (see Sections 12.4.2 and 12.8).

# 14.8.3 Photometric technique

Planets may be detected as they transit in front of a star. The reduction in light from the star is the cross-sectional area of the planet multiplied by the surface brightness of the disk of the star. A Jupiter with a radius of $1 \ R _ { \mathrm { j } }$ will cause a solar type star to dim by $1 \%$ with a duration of hours, depending on the orbital radius (Hale and Doyle, 1994). Earth-size planets would cause $0 . 0 1 \%$ dimming. The dimming is distinguished in character as the transit includes a limb-darkened ingress and egress with a flat-bottomed mid-period. For a transit to occur, the orbital inclination, $i$ , must be close to $9 0 ^ { \circ }$ , tan $i > a / R$ , where $a$ is the planet semi-major axis and $R$ is the star’s radius. The probability, $P$ , of transits, for randomly oriented orbital planes, is based on $i$ between $9 0 ^ { \circ }$ and $i ^ { \prime }$ , and is

$$
P ( i ^ { \prime } { \mathrm { ~ t o ~ } } 9 0 ^ { \circ } ) = \cos i ^ { \prime } .
$$

If $4 . 7 \%$ of Jupiter-like satellites at 0.1 AU will transit and $4 \%$ of solar-type stars have such satellites (Marcy and Butler, 1999), then $0 . 1 9 \%$ of solar-type stars should exhibit transits. This estimate is subject to uncertainty owing to the small numbers involved. The detection of planetary transits can indicate the existence of planets which can be further observed. The radius of the planet can be determined from the dimming, the mass from Doppler measures, and thus the density can be computed. This technique can be pursued from the ground for Jupiter and larger-sized objects and from space missions, such as COROT and KEPLER, for Earth-size planets (Koch et al., 1999; L´eger et al., 1999). There is now one example of a planet, previously discovered by Doppler technique, which was also recorded photometrically (Charbonneau et al., 2000).

# 14.8.4 Microlensing observations

Gravitational microlensing of stars in the galactic bulge can reveal the presence of planets in orbit around the intervening lensing object (Section 6.4.4). Follow-up photometry of microlensing events can reveal the perturbations on the microlensing light curve by an attendant planet (Peale, 1997; Safizadeh et al., 1999). Microlensing is most sensitive to planets that are about an Einstein radius from the lensing star. This is about 3–6 AU for a typical galactic bulge microlensing event. The duration of the perturbation on the light curve is proportional to the square root of the mass of the planet. The unique ability of microlensing is its ability for groundbased observations to detect Earth-mass planets with several astronomical units semi-major axis orbits around main-sequence stars. This procedure would yield statistics on such planets, but would be hard to follow-up because of the target’s large distance and the uncertainties in identifying the lensing objects.

# 14.8.5 Direct detections

Direct detection of planets is difficult due to the small fluxes from the planets and the wings of the point spread functions (psf) of the star. In visible wavelengths, reflected light from a Jupiter will have a brightness of $\sim 1 0 ^ { - 9 }$ of the star, while in the thermal infrared the contrast would be $\sim 1 0 ^ { - 4 }$ . The biggest challenges to detecting planets become the atmospheric seeing and exozodiacal light. Coronographic adaptive optics reduce seeing effects. The dark regions between speckles of a stellar image may enable planet detection (Labeyrie, 1995). Ground-based interferometric imaging in the infrared in methane absorption bands, which appear in Jovian atmospheres, may be able to reveal gas-giant planets. Earth-like planets will require space-borne interferometers that can eliminate the glare from the star by nulling, or destructive optical interference (Beichman, 1998; Angel and Woolf, 1997). Both ESA and NASA are developing missions for this purpose.

# 14.8.6 Conclusion

Comparing the methods presented, one may say that the spectroscopic method has the considerable advantage of being independent of the distance of the star. Its limitation lies in the uncertainties of the determination of radial velocities which cannot be indefinitely improved because of the intrinsic width and shape of the spectral lines. On the other hand, astrometry has still a large range of improvement as described in Section 2.6, and should provide in the future most of the data on extrasolar planetary systems. Finally, surveys using photometric techniques have good prospects for discovering new systems, but the quantitative investigations will have to be performed by spectroscopy and astrometry.

# Appendix A

Examples

The examples in this appendix are given to provide specific examples of astronomical computations, to show the differences between old and new reference systems, and as verifications of computational methods. The sources of equations and detailed descriptions of the concepts from this book are cited. The textual material is not repeated in this appendix.

# Example 1 Stellar angle and sidereal time

This is to illustrate the difference between the use of the equinox, the CEO and GMST, and the stellar angle. The stellar angle is described in Section 10.4 and the equation is (10.23).

For November 7, 2002, at $0 8 . 0 0 \mathrm { U T 1 }$ , the Julian Date is 2 452 585.833 33. . .. The time difference $T _ { \mathrm { u } }$ in Julian centuries from J2000.0 $\langle J D = 2 4 5 1 5 4 5 . 0 \rangle$ is:

$$
T _ { \mathrm { u } } = ( 2 4 5 2 5 8 5 . 8 3 3 3 3 3 3 \dots - 2 4 5 1 5 4 5 . 0 ) = 1 0 4 0 . 8 3 3 3 3 3 \dots . . .
$$

The stellar angle $\theta$ , expressed in radians, is, following (10.19):

$$
\begin{array} { r l } & { \theta ( T _ { \mathrm { u } } ) = 2 \pi ( 0 . 7 7 9 0 5 7 2 7 3 2 6 4 0 + 1 . 0 0 2 7 3 7 8 1 1 9 1 1 3 5 4 4 8 T _ { \mathrm { u } } ) } \\ & { \qquad = [ 2 \pi ( 1 0 4 4 ) ] + 2 \pi ( 0 . 4 6 1 9 9 6 5 0 4 1 0 ) } \\ & { \qquad = 1 6 6 { } ^ { \circ } . 3 1 8 6 2 1 2 } \\ & { \qquad = 1 1 ^ { \mathrm { h } } { \ : } 5 ^ { \mathrm { m } } 1 6 { } ^ { \mathrm { s } } . 4 6 9 . } \end{array}
$$

GMST is discussed in Sections 10.5 and 8.7 and the equation is (10.21). The GMST is given by computing first $\tau _ { 0 } = \mathrm { G M S T 1 }$ of $0 ^ { \mathrm { h } }$ UT1.

$$
\tau _ { 0 } = 2 4 1 1 0 ^ { 5 } 5 4 8 4 1 + 8 6 4 0 1 8 4 ^ { \mathrm { s } } 8 1 2 8 6 6 T _ { \mathrm { u } } ^ { \prime } + 0 { \dot { \times } } 0 9 3 1 0 4 { T _ { \mathrm { u } } } ^ { \prime } - 6 . 2 \times 1 0 ^ { - 6 } { T _ { \mathrm { u } } } ^ { 3 } { \mathrm { s } } ,
$$

where,

$$
T _ { \mathrm { u } } ^ { \prime } = ( 2 4 5 2 5 8 5 . 5 - 2 4 5 1 5 4 5 . 0 ) / 3 6 5 2 5 = 0 . 0 2 8 4 8 7 3 3 7 4 ,
$$

so that,

$$
\tau _ { 0 } = 2 7 0 2 4 6 \small ^ { \mathrm { s } } 4 2 8 8 = 3 ^ { \mathrm { d } } 3 ^ { \mathrm { h } } 4 ^ { \mathrm { m } } 6 \small ^ { \mathrm { s } } 4 0 8 7 9 ,
$$

to which, one must add 8 hours at sidereal rate of 1.002 737 909 350 795 $8 ^ { \mathrm { h } } 1 ^ { \mathrm { m } } 1 8 ^ { \mathrm { s } } . 8 5 1 7 7$ .

Let us now apply the correction dGMST given by the equation (10.22)

$$
\mathrm { d } G M S T = ( - 1 8 3 3 0 . 2 6 6 T _ { \mathrm { u } } ^ { \prime } + 7 . 8 7 { T _ { \mathrm { u } } ^ { \prime } } ^ { 2 } + 1 . 2 7 { T _ { \mathrm { u } } ^ { \prime } } ^ { 4 } ) \vert \mathrm { u s } .
$$

One gets ${ \mathrm { d } G M S T } = - 5 2 2 . 1 7 { \mu \mathrm { s } }$ . So, GMST at 8.h0 UT1 on November 7, 2002, is $1 1 ^ { \mathrm { h } } 5 ^ { \mathrm { m } } 2 5 _ { \cdot } ^ { \mathrm { s } } 2 6 0 6$ .

# Example 2 Apparent geocentric positions of planets from ICRF positions

This is to illustrate the calculation of apparent geocentric positions, the difference in planetary positions due to the difference between the equinox and the Geocentric Celestial Reference System, and the time transformation from TCB to TCG.

The ICRF position of Saturn for November 7, 2002, $J D = 2 4 5 2 5 8 5 . 5$ , in equatorial rectangular coordinates in AU at 08.00 hour TCB is to be converted to apparent geocentric position in TCG in the old and new systems.

# 2a Time transformation

The time conversion to Geocentric Coordinate Time (TCG) from Barycentric Coordinate Time (TCB) is discussed in Section 5.5.1, Equations (5.40) and (5.41). There are secular and periodic terms, the principal periodic term is given below for the example. The difference, in seconds, is calculated from:

$$
\begin{array} { r l } & { ( \mathrm { T C B } - \mathrm { T C G } ) _ { \mathrm { s e c u l a r } } = L _ { c } ( J D - 2 4 4 3 1 4 4 . 5 ) \times 8 6 4 0 0 } \\ & { \qquad = 1 . 4 8 0 8 2 6 8 4 5 7 \times 1 0 ^ { - 8 } ( 2 4 5 2 5 8 5 . 8 3 3 } \\ & { \qquad \quad - 2 4 5 1 5 4 5 . 5 ) \times 8 6 4 0 0 } \\ & { \qquad = 1 . 3 3 1 0 3 8 2 4 8 \mathrm { s } , } \\ & { ( \mathrm { T C B } - \mathrm { T C G } ) _ { \mathrm { p e r i o d i c } } = 0 . 0 0 1 6 5 8 \sin g + 0 . 0 0 0 0 1 4 \sin 2 g , } \end{array}
$$

where

(TCB − TCG)periodic = −0.001 415 s and $( \mathrm { T C B } - \mathrm { T C G } ) _ { \mathrm { t o t a l } } = 1 . 3 2 9 6 2 4 \mathrm { s }$

# 2b Barycentric positions

(1) Determine the barycentric vectors to the Earth and Saturn and the geocentric vector to Saturn. The ICRF position, E, and velocity of the Earth, $\dot { \bf E }$ , at $J D 2 4 5 2 5 8 5 . 8 3 3 3 \mathrm { T C B }$ in AU and AU per day are

$$
\mathbf { E } = \left( \begin{array} { c } { 0 . 7 0 5 3 5 2 3 3 5 } \\ { 0 . 6 3 5 0 4 4 6 8 6 } \\ { 0 . 2 7 5 3 3 7 6 3 4 } \end{array} \right) \quad \mathrm { a n d } \quad \dot { \mathbf { E } } = \left( \begin{array} { c } { - 0 . 0 1 2 3 8 1 3 2 4 } \\ { 0 . 0 1 1 1 6 4 2 0 4 } \\ { 0 . 0 0 4 8 4 0 6 7 1 } \end{array} \right) .
$$

The ICRF position, $\mathbf { Q }$ , and velocity, $\dot { \bf Q }$ , of Saturn at J D2 452 585.8333 TCB in AU and AU per day are

$$
\mathbf { Q } = \left( \begin{array} { c } { 0 . 9 3 7 0 8 4 0 2 6 } \\ { 8 . 3 1 7 7 8 0 5 8 1 } \\ { 3 . 3 9 5 2 2 0 6 1 6 } \end{array} \right) \quad \mathrm { a n d } \quad \dot { \mathbf { Q } } = \left( \begin{array} { c } { - 0 . 0 0 5 8 4 5 3 1 2 } \\ { 0 . 0 0 0 4 3 1 0 2 1 } \\ { 0 . 0 0 0 4 2 9 6 7 7 } \end{array} \right) .
$$

(2) Determine iteratively the barycentric position, $\mathbf { Q }$ , and the geocentric position, P, of Saturn at time $( t - \tau )$ , where $\tau$ is the light time, so the light emitted from Saturn at $( t - \tau )$ arrives at the Earth at time $t$ . After iteration, the positions of Saturn are:

$$
\mathrm { i c } \ \mathbf { Q } = \left( \begin{array} { l } { 0 . 9 3 7 3 6 4 0 7 2 } \\ { 8 . 3 1 7 7 5 9 9 3 1 } \\ { 3 . 3 9 5 2 0 0 0 3 0 } \end{array} \right) , \quad \mathrm { g e o c e n t r i c } \ \mathbf { P } = \left( \begin{array} { l } { 0 . 2 3 2 0 1 1 7 3 7 } \\ { 7 . 6 8 2 7 1 5 2 4 5 } \\ { 3 . 1 1 9 8 6 2 3 9 6 } \end{array} \right) ,
$$

where light time $= 4 1 3 9 . 3 7 8 8 1 \mathrm { s } = 0 . 0 4 7 9 0 9 4 7 7 \mathrm { d } .$

The unit vectors corresponding to the above vectors are:

$$
\mathbf { e } = { \left( \begin{array} { l } { 0 . 7 1 3 7 4 7 3 8 2 } \\ { 0 . 6 4 2 6 0 2 9 3 7 } \\ { 0 . 2 7 8 6 1 4 6 8 0 } \end{array} \right) } \ \mathbf { q } = { \left( \begin{array} { l } { 0 . 1 0 3 7 4 2 5 8 8 } \\ { 0 . 9 2 0 8 4 3 8 7 5 } \\ { 0 . 3 7 5 8 7 7 6 8 5 } \end{array} \right) } \ \mathbf { p } = { \left( \begin{array} { l } { 0 . 0 2 7 9 6 9 1 6 4 } \\ { 0 . 9 2 6 1 5 6 2 7 5 } \\ { 0 . 3 7 6 1 0 1 4 2 3 } \end{array} \right) } .
$$

# 2c Correct for light deflection

Calculate the geocentric direction $\mathbf { p _ { 1 } }$ of the planet, correcting for light deflection, $\Delta \mathbf { p }$ , as discussed in Section 6.4.3, from

$$
\Delta { \bf p } = \left( { \frac { 2 \mu } { c ^ { 2 } E } } \right) \left( { \frac { ( { \bf p } \cdot { \bf q } ) { \bf e } - ( { \bf e } \cdot { \bf p } ) { \bf q } } { 1 + { \bf q } \cdot { \bf e } } } \right) .
$$

The vector $\bf { p } _ { 1 } = \bf { p } + \Delta \Delta \bf { p }$ is a unit vector to order $\mu / c ^ { 2 }$ . The scalar products are

$$
\begin{array} { l } { { { \bf p } \cdot { \bf q } = \cos \zeta = 0 . 9 9 7 1 1 5 0 5 8 , { \bf e } \cdot { \bf p } = - \cos \psi = 0 . 7 1 9 9 0 1 0 3 8 , } } \\ { { \mathrm { a n d } { \bf q } \cdot { \bf e } = \cos \lambda = 0 . 7 7 0 5 0 8 0 2 0 . } } \end{array}
$$

In this case, the Earth and Saturn are in the same side with respect to the Sun, the deflection is very small. So, to allow comparisons, we give $\Delta \mathbf { p }$ with more decimals than necessary:

$$
\Delta \mathbf { p } = \left( \begin{array} { l } { 7 . 1 8 7 \times 1 0 ^ { - 9 } } \\ { - 0 . 2 5 0 \times 1 0 ^ { - 9 } } \\ { 0 . 0 8 1 \times 1 0 ^ { - 9 } } \end{array} \right) \quad \mathrm { a n d } \quad \mathbf { p } _ { 1 } = \left( \begin{array} { l } { 0 . 0 2 7 9 6 9 1 7 1 } \\ { 0 . 9 2 6 1 5 3 2 7 5 } \\ { 0 . 3 7 6 1 0 1 4 2 3 } \end{array} \right) .
$$

# 2d Correct for aberration

Calculate the planetary direction in a geocentric fixed frame that is moving with the instantaneous velocity of the Earth as discussed in Section 6.3, from

$$
\mathbf { p } _ { 2 } = \frac { \gamma ^ { - 1 } \mathbf { p } _ { 1 } + ( 1 + ( \mathbf { p } _ { 1 } \mathbf { V } ) ) \mathbf { V } / ( 1 + \gamma ^ { - 1 } ) } { 1 + \mathbf { p } _ { 1 } \cdot \mathbf { V } } .
$$

In this formulation, $\mathbf { V } = \dot { \mathbf { E } } / c$ , $\gamma = { ( 1 - V ^ { 2 } ) } ^ { - 1 / 2 }$ ; the velocity is in units of the velocity of light. So

$$
\mathbf { V } = \left( \begin{array} { c } { { - 7 . 1 5 0 8 5 6 3 6 \times 1 0 ^ { - 5 } } } \\ { { 6 . 4 4 7 9 0 6 4 7 \times 1 0 ^ { - 5 } } } \\ { { 2 . 7 9 5 7 3 8 2 7 \times 1 0 ^ { - 5 } } } \end{array} \right)
$$

# 2e Precession–nutation correction (equinox system)

Apply precession and nutation as discussed in Section 8.4 by multiplying by the rotation matrix $\mathcal { R }$ as given in the Astronomical Almanac to obtain the apparent direction ${ \bf p } _ { 3 }$ from

$$
\mathbf { p } _ { 3 } = \mathcal { R } \times \mathbf { p } _ { 2 } .
$$

$\mathcal { R } = \left( \begin{array} { l } { 0 . 9 9 9 9 9 9 9 8 1 } \\ { 0 . 0 0 0 5 5 9 2 1 } \\ { 0 . 0 0 0 2 4 3 0 8 } \end{array} \right.$ 0.000 559 21 0.000 243 08   
The matrix 0.999 999 84 0.000 015 27   
0.000 015 13 0.999 999 97

Then,

$$
\mathbf { p } _ { 3 } = { \mathcal { R } } \times \mathbf { p } _ { 2 } = { \left( \begin{array} { l } { 0 . 0 2 7 3 2 8 1 6 1 } \\ { 0 . 9 2 6 1 0 3 0 2 4 } \\ { 0 . 3 7 6 0 9 7 9 3 3 } \end{array} \right) } .
$$

# 2f Precession–nutation correction (new system)

Apply precession and nutation as discussed in Section 10.4.1 by multiplying by the precession–nutation matrix $\mathcal { P N }$ described in Section 8.7.2 to obtain the apparent direction ${ \bf p } _ { 3 } ^ { \prime }$ from

$$
\mathbf { p } _ { 3 } ^ { \prime } = \mathcal { P N } \times \mathbf { p } _ { 2 } .
$$

0.999 999 970 483 0.000 000 014 937 $\begin{array} { r l } & { 0 . 0 0 0 2 4 2 9 6 7 9 1 5 } \\ & { 0 . 0 0 0 0 1 5 1 0 5 6 2 0 } \\ & { 0 . 9 9 9 9 9 9 9 9 7 0 3 6 9 } \end{array}$ The matrix  = 0.000 000 011 267 0.999 999 999 886 0.000 242 967 915 0.000 015 105 617

Then,

$$
\mathbf { p } _ { 3 } ^ { \prime } = \mathcal { P N } \times \mathbf { p } _ { 2 } = \left( \begin{array} { l } { 0 . 0 2 7 3 2 8 1 5 7 } \\ { 0 . 9 2 6 1 0 3 0 2 4 } \\ { 0 . 3 7 6 1 1 8 7 2 5 } \end{array} \right) .
$$

# $_ { 2 g }$ Convert to spherical coordinates

Calculate the right ascensions and declinations from vectors ${ \bf p } _ { 3 }$ . The results, for November 7, 2002, at $7 ^ { \mathrm { h } } 5 9 ^ { \mathrm { m } } 5 8 . 6 7 0 3 7 6 \mathrm { T C G }$ , are

equinox system: $\alpha = 5 ^ { \mathrm { h } } 5 3 ^ { \mathrm { m } } 1 4 _ { \cdot } ^ { \mathrm { s } } 3 4 3 0 , \delta = 2 2 ^ { \circ } 5 ^ { \prime } 3 7 _ { \cdot } ^ { \prime \prime } 6 0 0 ,$

new system : $\alpha = 5 ^ { \mathrm { h } } 5 3 ^ { \mathrm { m } } 6 5 6 5 2 5 , \delta = 2 2 ^ { \circ } 5 ^ { \prime } 3 7 ! 5 9 4 .$

The difference in δ corresponds to the difference between the nutation theories used. The difference in $\alpha$ corresponds to the motion of the equinox with respect to the CEO.

# Example 3 Astrometric positions of reference stars

This example illustrates how reference stars would be computed for a CCD observation of a program object at some observational date.

The observational program star is being observed on November 7, 2002, $J D 2 4 5 2 5 8 5 . 5$ , at 08.00 TT. Reference stars, three for the example, have been selected from the Hipparcos Catalogue, and their data are the following.

<table><tr><td rowspan="2">Number</td><td rowspan="2">Position</td><td rowspan="2">Parallax w (mas)</td><td colspan="2">Proper motion (mas/year)</td></tr><tr><td>μa</td><td>μ8</td></tr><tr><td>84392</td><td>α1 = 258:806244 73 δ = +30:301 25112</td><td>2.96</td><td>1.84</td><td>13.98</td></tr><tr><td>84341</td><td>α = 258:641307 01</td><td>9.84</td><td>-21.26</td><td>42.82</td></tr><tr><td></td><td>82 = +30:955 79299</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>84733</td><td>α = 259:765 901 84</td><td>3.61</td><td>-16.19</td><td>5.59</td></tr><tr><td></td><td>8 = +30:905 257 83</td><td></td><td></td><td></td></tr></table>

The positions are on the ICRF, but their epochs are those of the Hipparcos Catalogue, 1991.25, J D2 448 349.0625 TT. For astrometric positions, the proper motions from epoch to observed time and the parallax corrections must be calculated and applied. The star positions dependent on time are given in Equation (14.1) as

$$
\begin{array} { r } { \alpha _ { i } = \alpha _ { i 0 } + \mu _ { \alpha i } t _ { j } + \varpi _ { i } P _ { j } , } \\ { \delta _ { i } = \delta _ { i 0 } + \mu _ { \delta i } t _ { j } + \varpi _ { i } Q _ { j } , } \end{array}
$$

where the terms for nonlinear motion and observational errors have been omitted. The proper motion corrections are to be computed with

$t = 2 4 5 2 5 8 5 . 8 3 3 3 - 2 4 4 8 3 4 9 . 0 6 2 5 = 4 2 3 6 . 7 7 0 8 { \mathrm { d a y s } } = 1 1 . 6 0$ years,

The stellar parrallax corrections are given in (6.23) as

$$
\begin{array} { r } { \Delta \alpha \cos \delta = \varpi ( x \sin \alpha - y \cos \alpha ) , \qquad } \\ { \Delta \delta = \varpi [ ( x \cos \alpha + y \sin \alpha ) \sin \delta - z \cos \delta ] , } \end{array}
$$

where $x , y , z$ are the barycentric coordinates of the Earth which are for the date above

$$
\begin{array} { l } { x = + 0 . 7 0 9 4 6 7 9 2 4 } \\ { y = + 0 . 6 3 1 3 1 2 0 3 8 } \\ { z = + 0 . 2 7 3 7 1 9 1 9 8 . } \end{array}
$$

Then

$$
\begin{array} { c } { { \Delta \alpha _ { 1 } \cos \delta _ { 1 } = - 1 . 7 0 \mathrm { m a s } , \quad \Delta \delta _ { 1 } = - 1 . 8 3 \mathrm { m a s } } } \\ { { \Delta \alpha _ { 2 } \cos \delta _ { 2 } = - 5 . 6 2 \mathrm { m a s } , \quad \Delta \delta _ { 2 } = - 6 . 1 5 \mathrm { m a s } } } \\ { { \Delta \alpha _ { 3 } \cos \delta _ { 3 } = - 2 . 1 6 \mathrm { m a s } , \quad \Delta \delta _ { 3 } = - 2 . 2 3 \mathrm { m a s } . } } \end{array}
$$

The resulting positions for $J D 2 4 5 2 5 8 5 . 8 3 3$ are:

$$
{ \begin{array} { r l l l } { { \mathrm { f o r } } } & { 8 4 3 9 2 } & { \alpha _ { 1 } = 2 5 8 \cdot 8 0 6 2 3 8 2 6 } & { \delta _ { 1 } = + 3 0 \cdot 3 0 1 2 0 5 6 6 } \\ & { 8 4 3 4 1 } & { \alpha _ { 2 } = 2 5 8 \cdot 6 4 1 3 7 3 6 9 } & { \delta _ { 2 } = + 3 0 \cdot 9 5 5 6 5 3 3 1 } \\ & { 8 4 7 2 2 } & { \alpha _ { 3 } = 2 5 9 \cdot 7 6 5 9 5 3 3 2 } & { \delta _ { 3 } = + 3 0 \cdot 9 0 5 2 3 9 2 0 . } \end{array} }
$$

These are astrometric positions in the classical sense. Additional differential corrections for refraction, color, etc., can be introduced to reduce the size of the plate constants for the program object solution.

These positions can then be projected onto the plate, or CCD, by the gnomonic projection given in (3.52). Let $( \xi , \eta )$ be rectangular Cartesian coordinates measured from the position of $( \alpha _ { 0 } , \delta _ { 0 } )$ . Then, setting $\Delta \alpha = \alpha _ { i } - \alpha _ { 0 }$ ,

$$
\begin{array} { c } { { \xi = \frac { \cos \delta \sin \Delta \alpha } { \sin \delta _ { 0 } \sin \delta + \cos \delta _ { 0 } \cos \delta \cos \Delta \alpha } , } } \\ { { \eta = \frac { \cos \delta _ { 0 } \sin \delta - \sin \delta _ { 0 } \cos \delta \cos \Delta \alpha } { \sin \delta _ { 0 } \sin \delta + \cos \delta _ { 0 } \cos \delta \cos \Delta \alpha } . } } \end{array}
$$

If $\alpha _ { 0 } = 2 5 8 . 7$ and $\delta _ { 0 } = 3 0 _ { \cdot } ^ { \circ } 5$ , then

$$
\begin{array} { l l l } { { \xi _ { 1 } = 0 . 0 0 1 6 0 0 9 0 7 \quad } } & { { \mathrm { a n d } } } & { { \eta _ { 1 } = - 0 . 0 0 3 4 6 8 8 8 2 } } \\ { { \xi _ { 2 } = - 0 . 0 0 0 8 7 7 5 0 4 } } & { { } } & { { \eta _ { 2 } = 0 . 0 0 7 9 5 3 0 4 9 } } \\ { { \xi _ { 3 } = 0 . 0 1 5 9 6 4 4 2 7 } } & { { } } & { { \eta _ { 3 } = 0 . 0 0 7 1 4 9 1 5 5 . } } \end{array}
$$

There is the alternate approach which is the use of space coordinates and motion matrices, as discussed in Section 7.8, rather than spherical coordinates. This is particularly applicable for positions near the pole, where accuracy can be lost.

Taking two stars from the Hipparcos Catalogue in the same region of the sky, but near the pole to which we have added hypothetical radial velocities.

<table><tr><td>Number</td><td></td><td>Parallax</td><td colspan="2">Proper motion (mas/year)</td><td>Radial</td></tr><tr><td></td><td>Position</td><td>π (mas)</td><td>μa</td><td>μ8</td><td>velocity (km/s)</td></tr><tr><td>84525</td><td>α1 = 259:183 322 80 81 = +83:70027394</td><td>2.88</td><td>-7.85</td><td>22.31</td><td>30</td></tr><tr><td>84535</td><td>α2 = 259:238 585 72</td><td>3.72</td><td>-23.03</td><td>-3.07</td><td>40</td></tr></table>

Their position vectors, r, can be determined at the Hipparcos epoch, $t$ , from Equation (7.7) as

$$
\mathbf { r } = \left( \begin{array} { c } { r \cos \delta \cos \alpha } \\ { r \cos \delta \sin \alpha } \\ { r \sin \delta } \end{array} \right) .
$$

Note that $r$ is the barycentric distance to the star, which can be computed from the parallax, $\varpi$ , of the star. The additional problem here is the choice of the unit of length.

(1) If we take the astronomical unit (AU), then

$$
r = 1 / \sin \varpi ,
$$

by the more sophisticated approach described in Section 11.2.

So, for the stars above, the position vectors are

$$
\mathbf { r } _ { 1 } = { \left( \begin{array} { l } { - 1 4 7 4 8 3 9 } \\ { - 7 7 1 9 1 7 0 } \\ { 7 1 1 8 7 2 4 7 } \end{array} \right) } \quad { \mathrm { a n d } } \quad \mathbf { r } _ { 2 } = { \left( \begin{array} { l } { - 1 7 3 8 7 3 } \\ { - 9 1 4 8 2 3 } \\ { 5 5 4 3 9 7 0 8 } \end{array} \right) } .
$$

The space motion vector, r˙ can be given by

$$
\dot { \mathfrak { r } } = \left( \begin{array} { r r r } { p _ { x } } & { q _ { x } } & { r _ { x } } \\ { p _ { y } } & { q _ { y } } & { r _ { y } } \\ { p _ { z } } & { q _ { z } } & { r _ { z } } \end{array} \right) = \left( \begin{array} { c c c } { - \sin \alpha } & { - \sin \delta \cos \alpha } & { \cos \delta \cos \alpha } \\ { \cos \alpha } & { - \sin \delta \sin \alpha } & { \cos \delta \sin \alpha } \\ { 0 } & { \cos \delta } & { \sin \delta } \end{array} \right) \times \left( \begin{array} { c } { 1 5 s r \mu _ { \alpha } } \\ { s r \mu _ { \delta } } \\ { k \dot { r } } \end{array} \right) .
$$

The factors $s = 2 \pi / ( 3 6 0 \times 3 6 0 0 0 0 0 \times 3 6 5 . 2 5 )$ converts from milliarcseconds per year to radians per day and $k = 8 6 4 0 0 / ( 1 . 4 9 5 9 7 8 7 0 \times 1 0 ^ { 8 } )$ converts from $\mathrm { k m / s }$ to AU/day.

The values of r˙ for the two stars are

$$
\dot { \mathbf { r } } _ { 1 } = \left( \begin{array} { c c c } { - 0 0 3 } & { 7 3 0 } & { 5 8 4 } \\ { 0 . 0 2 0 } & { 2 3 6 } & { 2 4 9 } \\ { 0 . 0 1 9 } & { 5 4 9 } & { 0 6 0 } \end{array} \right) \quad \mathrm { a n d } \quad \dot { \mathbf { r } } _ { 2 } = \left( \begin{array} { c c c } { 0 . 0 1 7 } & { 0 1 5 } & { 4 0 6 } \\ { 0 . 0 0 1 } & { 3 2 9 } & { 3 2 6 } \\ { - 0 . 0 2 3 } & { 1 3 6 } & { 6 2 1 } \end{array} \right) .
$$

Then the positions of the stars for the epoch $t _ { 1 } = J D 2$ 452 585.8333, are determined from

$$
\dot { \mathbf { r } } _ { i } = \dot { \mathbf { r } } _ { i 1 } + ( t _ { 1 } - t ) \dot { \mathbf { r } } _ { i } ,
$$

and the results are

$$
\mathbf { r } _ { 1 } = { \left( \begin{array} { l } { - 1 4 7 4 8 5 5 } \\ { - 7 7 1 9 0 8 5 } \\ { 7 1 1 8 7 3 3 0 } \end{array} \right) } \quad { \mathrm { a n d } } \quad \mathbf { r } _ { 2 } = { \left( \begin{array} { l } { - 1 7 3 9 4 5 } \\ { - 9 1 4 8 1 6 } \\ { 5 5 4 3 9 6 1 0 } \end{array} \right) } ,
$$

giving

$$
\begin{array} { l l l } { { \alpha _ { 1 } = 2 5 9 { \mathrm { . } } 1 8 3 0 9 2 2 9 4 } } & { { \mathrm { a n d } } } & { { \delta _ { 1 } = 8 3 { \mathrm { . } } 7 0 0 3 4 5 8 2 5 } } \\ { { \alpha _ { 2 } = 2 5 9 { \mathrm { . } } 2 3 4 1 6 3 4 1 7 } } & { { \mathrm { a n d } } } & { { \delta _ { 2 } = 8 9 { \mathrm { . } } 0 3 7 7 0 5 5 6 5 . } } \end{array}
$$

(2) One may also choose parsecs. In this case, $\varpi$ being expressed in milliarcseconds, one has

$$
r = 1 / 1 0 0 0 \varpi .
$$

The coefficient $s$ remains the same, but $k$ is to be divided by $A = 2 0 6 2 6 4 . 8 0 6$ , which is a parsec expressed in AU. The distances in parsecs are, respectively,

$$
r _ { 1 } = 3 4 7 . 2 2 2 \ldots \ \mathrm { a n d } \quad r _ { 2 } = 2 6 8 . 8 1 7 2 \ldots ,
$$

and the position vectors are

$$
\mathbf { r } _ { 1 } = \left( \begin{array} { l } { - 7 . 1 5 0 2 2 2 7 6 } \\ { - 3 7 . 4 2 3 5 9 6 } \\ { 3 4 5 . 1 2 5 5 1 4 } \end{array} \right) \mathrm { ~ a n d ~ } \mathbf { r } _ { 2 } = \left( \begin{array} { l } { - 0 . 8 4 3 3 1 1 } \\ { - 4 . 4 3 5 1 8 5 } \\ { 2 6 8 . 7 7 8 8 1 7 } \end{array} \right) .
$$

The resulting ccordinates at the observation time are of course the same.

# Appendix B

Astronomical values

Preliminary remark. The numbers that are given in this appendix should not be considered as reference values. Although the present authors have tried to provide numbers that are as close as possible to what is estimated to be the best values, they do not guarantee either that they are the best possible, or that all are mutually consistent. In several cases, authorities that publish values of astronomical constants do not agree, and the choice of one or the other is necessarily subjective. Furthermore, as time goes on, better values will become available. For these reasons, we do not associate uncertainties to values, and one should consider these lists as providing orders of magnitude of the parameters and not as a basis for accurate and dependable calculations.

# IAU system of astronomical constants, best estimates

# SI units

The units meter (m), kilogram $( \mathrm { k g } )$ , and second (s) are the units of length, mass and time in the International System of Units (SI).

# Astronomical units

The astronomical unit of time is a time interval of one day $( D )$ of 86 400 seconds.   
An interval of 36 525 days is one Julian century.

The astronomical unit of mass is the mass of the Sun (S).

The astronomical unit of length (AU) is that length $( A )$ for which the Gaussian gravitational constant $( k )$ takes the value $0 . 0 1 7 2 0 2 0 9 8 9 5$ when the units of measurement are the astronomical units of length, mass and time. The dimensions of $k$ are those of the constant of gravitation $G \colon L ^ { 3 } / ( M \ : T ^ { 2 } )$ . The term “unit distance” is also used for the length $A$ .

# Defining constants

Gaussian gravitational constant: $k = 0 . 0 1 7 2 0 2 0 9 8 9 5$ Speed of light: $c = 2 9 9 7 9 2 4 5 8 { \mathrm { m / s } }$

# Primary constants

Light-time for unit distance: $\tau _ { A } = 4 9 9 . 0 0 4 7 8 3 8 0 6 1$ s Equatorial radius for Earth: $a _ { \mathrm { e } } = 6 3 7 8 1 4 0 \ \mathrm { m }$ IUGG value: $a _ { \mathrm { e } } = 6 3 7 8 1 3 6 . 6 \ : \mathrm { m }$ Dynamical form-factor for Earth: $J _ { 2 } = 0 . 0 0 1 0 8 2 6 3 5 9$ Geocentric gravitational constant: $G E = 3 . 9 8 6 0 0 4 4 1 8 \times 1 0 ^ { 1 4 } \mathrm { m ^ { 3 } / s ^ { 2 } }$ Constant of gravitation: $G = 6 . 6 7 3 \times 1 0 ^ { - 1 1 } \mathrm { m } ^ { 3 } / ( \mathrm { k g } \ \mathrm { s } ^ { 2 } )$ Ratio of mass of Moon to that of Earth: $\mu = 0 . 0 1 2 3 0 0 0 3 8 3$ General precession in longitude: $\rho = 5 0 2 8 . 7 9 0$ (per Julian century, at epoch J2000.0) Obliquity of the ecliptic: $\varepsilon = 2 3 ^ { \circ } 2 6 ^ { \prime } 2 1 . 4 0 5 9$ (at standard epoch J2000.0)

# Derived constants

${ \mathrm { U n i t  d i s t a n c e : } } c \tau _ { A } = A = 1 . 4 9 5 9 7 8 7 0 6 9 1 \times 1 0 ^ { 1 1 } { \mathrm { m } }$ Solar parallax: arcsi $1 ( a _ { \mathrm { e } } / A ) = \pi _ { \odot } = 8 . 7 9 4 1 4 4$ Constant of aberration $= \kappa _ { \odot } = 2 0 _ { : } ^ { \prime } 4 9 5 5 2$ (for standard epoch J2000.0)

Flattening factor for the Earth: $f = 0 . 0 0 3 3 5 2 8 1 = 1 / 2 9 8 . 2 5 7$

Heliocentric gravitational constant:

$$
A ^ { 3 } k ^ { 2 } / D ^ { 2 } = G S = 1 . 3 2 7 1 2 4 4 2 0 7 6 \times 1 0 ^ { 2 0 } { \mathrm { m } } ^ { 3 } / { \mathrm { s } } ^ { 2 }
$$

Ratio of mass of Sun to that of the Earth:

$$
( G S ) / ( G E ) = S / E = 3 3 2 9 4 6 . 0 5 0 8 9 5
$$

Ratio of mass of Sun to that of Earth + Moon:

$$
( S / E ) / ( l + \mu ) = 3 2 8 9 0 0 . 5 6 1 4 0 0
$$

Mass of the Sun: $( G S ) / G = S = 1 . 9 8 9 1 \times 1 0 ^ { 3 0 } \mathrm { k g }$

# Solar System values

# System of planetary masses

Ratios of mass of Sun to masses of the planets

Masses of minor planets   

<table><tr><td>Mercury</td><td>6023 600</td><td>Jupiter</td><td>1047.3486</td></tr><tr><td>Venus</td><td>408 523.71</td><td>Saturn</td><td>3 497.898</td></tr><tr><td>Earth+Moon</td><td>328 900.561 400</td><td>Uranus</td><td>22 902.98</td></tr><tr><td rowspan="2">Mars</td><td rowspan="2">3 098 708</td><td>Neptune</td><td>19 412.24</td></tr><tr><td>Pluto</td><td>135 200 000</td></tr></table>

Masses of satellites   

<table><tr><td>N° Minor planet</td><td>Mass in solar mass</td></tr><tr><td>(1) Ceres</td><td>4.7 ×10-10</td></tr><tr><td>(2) Pallas</td><td>1.0 ×10-10</td></tr><tr><td>(4) Vesta</td><td>1.3 × 10-10</td></tr><tr><td></td><td></td></tr></table>

Equatorial radii in km   

<table><tr><td>Planet</td><td>Satellite</td><td>Satellite /Planet</td></tr><tr><td rowspan="5">Jupiter</td><td>Io</td><td>4.70 × 10-5</td></tr><tr><td>Europa</td><td>2.56 × 10-5</td></tr><tr><td>Ganymede</td><td>7.84 × 10-5</td></tr><tr><td>Callisto</td><td>5.6×10-5</td></tr><tr><td>Titan</td><td>2.41×10-4</td></tr><tr><td>Saturn Neptune</td><td>Triton</td><td>2 ×10-3</td></tr></table>

<table><tr><td>Mercury</td><td>2439.76</td><td>Jupiter</td><td>71398</td></tr><tr><td>Venus</td><td>6052.3</td><td>Saturn</td><td>60000</td></tr><tr><td>Earth</td><td>6378.137</td><td>Uranus</td><td>25 400</td></tr><tr><td>Mars</td><td>3 397.515</td><td>Neptune</td><td>24300</td></tr><tr><td></td><td></td><td>Pluto</td><td>2500</td></tr><tr><td>Moon</td><td>1738</td><td>Sun</td><td>696000</td></tr></table>

Orbital elements of planets   

<table><tr><td>Name</td><td>Semimajor axis (AU)</td><td>Eccentricity</td><td>Inclination on ecliptic</td><td>Sidereal orbital period in days</td></tr><tr><td>Mercury</td><td>0.3871</td><td>0.206</td><td>7:00</td><td>87.969</td></tr><tr><td>Venus</td><td>0.7233</td><td>0.007</td><td>3.39</td><td>227.701</td></tr><tr><td>Earth</td><td>1.0000</td><td>0.017</td><td>一</td><td>365.256</td></tr><tr><td>Mars</td><td>1.5237</td><td>0.093</td><td>1:85</td><td>686.980</td></tr><tr><td>Jupiter</td><td>5.2026</td><td>0.048</td><td>1:31</td><td>4332.59</td></tr><tr><td>Saturn</td><td>9.5547</td><td>0.056</td><td>2.48</td><td>10759.2</td></tr><tr><td>Uranus</td><td>19.2181</td><td>0.046</td><td>0:77</td><td>30688.5</td></tr><tr><td>Neptune</td><td>30.1096</td><td>0.009</td><td>1:77</td><td>60182.3</td></tr><tr><td>Pluto</td><td>39.4387</td><td>0.250</td><td>17:14</td><td>90469.7</td></tr></table>

Gravity fields of planets   

<table><tr><td>Planet</td><td>J</td><td>J</td><td>J4</td></tr><tr><td>Earth</td><td>+0.001082 6359</td><td>-0.2533 × 10-5</td><td>-0.1616 × 10-5</td></tr><tr><td>Mars</td><td>+0.001964</td><td>+0.36 × 10-4</td><td>-0.58 × 10-3</td></tr><tr><td>Jupiter</td><td>+0.014 75</td><td></td><td></td></tr><tr><td>Saturn</td><td>+0.01645</td><td></td><td>-0.10 × 10-2</td></tr><tr><td>Uranus</td><td>+0.012</td><td></td><td></td></tr><tr><td>Neptune</td><td>+0.004</td><td></td><td></td></tr><tr><td>Mars:</td><td>C22 = -0.000055，</td><td>S22 = +0.000031, S31 = +0.000026</td><td></td></tr></table>

# Gravity field of the Moon

$$
{ \begin{array} { r l } { \gamma = ( B - A ) / C = 0 . 0 0 0 2 2 7 8 \quad } & { \beta = ( C - A ) / B = 0 . 0 0 0 6 3 1 3 } \\ { C / M R ^ { 2 } } & { = 0 . 3 9 2 } \end{array} } { \begin{array} { r l } { I = 5 5 5 2 { \mathrm { ' } } 7 = 1 { \mathrm { ' } } 3 2 { \mathrm { ' } } 3 2 { \mathrm { ' } } 7 } \end{array} }
$$

$C _ { 2 0 } = - 0 . 0 0 0 2 0 2 7$ $C _ { 3 0 } = - 0 . 0 0 0 0 0 6$ $C _ { 3 2 } = + 0 . 0 0 0 0 0 4 9$   
$C _ { 2 2 } = + 0 . 0 0 0 0 2 2 5$ $C _ { 3 1 } = + 0 . 0 0 0 0 3 0 8$ $S _ { 3 2 } = + 0 . 0 0 0 0 0 1 7$ $S _ { 3 1 } = + 0 . 0 0 0 0 0 4$ $C _ { 3 3 } = + 0 . 0 0 0 0 0 1 8$ $S _ { 3 3 } = - 0 . 0 0 0 0 0 0 3$

# Time scale factors

Average value of $d ( T C B ) / d ( ( T T ) - 1$ , Average value of $d ( T C B ) / d ( T C G ) - 1$ , Defining value of $d ( T C G ) / d ( T T ) - 1$ ,

$L _ { B } = 1 . 5 5 0 5 1 9 7 6 7 7 2 \times 1 0 ^ { - 8 }$ $L _ { C } = 1 . 4 8 0 8 2 6 8 6 7 4 1 \times 1 0 ^ { - 8 }$ LG 6.969 290 134  10−10

# Sun

<table><tr><td>Radius:</td><td>6.96 ×10m</td></tr><tr><td>Semidiameter at mean distance:</td><td>15&#x27;59.63 = 959.63</td></tr><tr><td>Mass:</td><td>1.9891 × 1030 kg</td></tr><tr><td>Mean density:</td><td>1.41 g/cm³</td></tr><tr><td>Surface gravity:</td><td>2.74 × 10² m/s² = 27.9 gal</td></tr><tr><td>Inclination of solar equator to ecliptic:</td><td>7°15&#x27;</td></tr><tr><td>Longitude of ascending node: (T in centuries from J2000.0)</td><td>75°46&#x27;+84&#x27;T</td></tr><tr><td>Period of synodic rotation (Φ = latitude): Period of sidereal rotation adopted for</td><td>26.90+5.2 sin²Φdays</td></tr><tr><td>heliographic longitudes:</td><td>25.38 days</td></tr><tr><td>Motion relative to nearby stars,apex:</td><td>α = 271，δ= +30°</td></tr><tr><td>Motion relative to nearby stars, speed:</td><td>1.94 × 104 m/s = 0.0112 AU/day</td></tr></table>

# Earth

# Rotation of the Earth

Period with respect to fixed stars

Annual rates of precession $_ T$ in centuries from J2000.0)

# Figure and gravity field of the Earth

Values in the IAU system and best estimates in 2001   

<table><tr><td></td><td>IAU system</td><td>Best estimate (2001)</td></tr><tr><td>Equatorial radius: Dynamical form factor:</td><td>a = 6378140m J = 0.001 082 63</td><td>637 8136.6m 0.001081 6359</td></tr><tr><td></td><td></td><td>-2.8×10-11 1year-1</td></tr><tr><td>Flattening: Polar radius:</td><td>f = 1/298.257 b= 6356755m</td><td>6356752 m</td></tr><tr><td>Mass of the Earth:</td><td>M = 5.9742 × 1024kg</td><td>5.9742 × 1024 kg</td></tr><tr><td>Mean density:</td><td>5.52 g/cm</td><td></td></tr><tr><td>Normal gravity:</td><td>gal = 9.80621</td><td></td></tr><tr><td></td><td>-0.02593 cos 2Φ</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>+0.00003 cos 4Φ m/s2</td><td></td></tr><tr><td>Geocentric gravitational</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>constant in 1014 m³/s²:</td><td>GM = 3.986005</td><td>3.98600418</td></tr></table>

Other constants (best values in 2001)

Mean equatorial gravity $( g _ { \mathrm { e } } )$ : $9 7 . 8 0 3 2 7 8 \mathrm { m } / \mathrm { s } ^ { 2 }$ Potential of the geoid $( W _ { 0 } )$ : $6 2 6 3 6 8 5 6 . 0 \mathrm { m } ^ { 2 } / \mathrm { s } ^ { 2 }$ Mean angular velocity of the Earth $( \omega )$ : $7 . 2 9 2 1 1 5 \times 1 0 ^ { - 5 } \mathrm { r a d / s }$ Geopotential scale factor $\left( R _ { 0 } = G M _ { \oplus } / W _ { 0 } \right)$ : $6 3 6 3 6 7 2 . 6  { \mathrm { m } }$

For a point on the spheroid of the IAU system at geodetic latitude $( \phi )$ :   
$1 ^ { \circ }$ of latitude: $1 1 { \overset { - } { 0 . 5 7 5 } } + 1 . 1 1 0 \sin ^ { 2 } \phi \operatorname { k m }$   
$1 ^ { \circ }$ of longitude: $( 1 1 1 . 3 2 0 + 0 . 3 7 3 \sin ^ { 2 } \phi ) \cos \phi \mathrm { k m }$   
Geodetic latitude $( \phi ) -$ geocentric latitude $( \phi ^ { \prime } ) : 6 9 2 ! 7 4 \sin 2 \phi - 1 ! 7 1 6 \sin 4 \phi$

Orbit of the Earth   

<table><tr><td></td><td>IAU System</td><td>Best estimate (2001)</td></tr><tr><td>Solar parallax:</td><td>8.794 148</td><td>8.794 144</td></tr><tr><td>Constant of aberration:</td><td>20&quot;.495 52(J2000.0)</td><td></td></tr><tr><td>Light-time for 1 AU:</td><td>499.004 782s</td><td>499.004 783 8061s</td></tr><tr><td>Astronomical unit of length:</td><td>1.495 978 70 × 101 m</td><td>1.495 978 70691 × 101 m</td></tr><tr><td>Mass ratio Sun/Earth:</td><td>332 946.0</td><td>332 946.050 895</td></tr><tr><td>Mass ratio Sun/Earth+ Moon:</td><td>328 900.5</td><td>328 900.561 400</td></tr><tr><td>Massratio Moon/Earth:</td><td>0.0123 002</td><td>0.012 300 0383</td></tr><tr><td>Mean eccentricity:</td><td>0.016 708 617</td><td></td></tr><tr><td>Mean obliquity of the ecliptic:</td><td>23°26&#x27;21&#x27;448</td><td>23° 26&#x27;21&#x27;4119</td></tr><tr><td>Annual rate of rotation on the ecliptic:</td><td>0.4704</td><td></td></tr><tr><td>Mean distance Earth-Sun:</td><td>1.000 0010178AU</td><td>1.000 001057266 65AU</td></tr><tr><td>Mean orbital speed:</td><td>29.7859 km/s</td><td>29.784 766 966km/s</td></tr><tr><td>Mean centripetal acceleration:</td><td>0.005 94 m/s²</td><td>5.930113 4387 × 10-³ m/s²</td></tr></table>

Moon Physical Moon   

<table><tr><td></td><td></td></tr><tr><td>Mean radius</td><td>1738 km</td></tr><tr><td>Semi-diameter at mean distance</td><td>15&#x27;32&#x27;6</td></tr><tr><td>Mass</td><td>7.3483 × 1022 kg</td></tr><tr><td>Mean density</td><td>3.34g/cm3</td></tr><tr><td>Surface gravity</td><td>1.62 m/s² = 0.17 gal</td></tr></table>

Orbit of the Moon about the Earth

<table><tr><td>Sidereal mean motion of Moon: Mean distance of Moon from Earth:</td><td>2.661 699 489 × 10-6 rad/s1 3.844 × 10 km = 60.27Earth radii = 0.002 570 AU</td></tr></table>

# Glossary

aberration: the angular displacement of the observed position of a celestial object from its geometric position, caused by the finite velocity of light in combination with the motions of the observer and of the observed object.

aberration, annual: the component of stellar aberration resulting from the motion of the Earth about the Sun.

aberration, diurnal: the component of stellar aberration resulting from the observer’s diurnal motion about the center of the Earth.

aberration, orbital: in space astrometry, the component of stellar aberration resulting from the spacecraft motion with respect to the center of the Earth.

aberration, planetary: the angular displacement of the observed position of a body of the Solar System produced by motion of the observer and the actual motion of the observed object in the Solar System.

aberration, secular: the component of stellar aberration resulting from the essentially uniform and rectilinear motion of the entire Solar System in space. Secular aberration is usually disregarded.

aberration, stellar: the angular displacement of the observed position of a celestial body resulting from the motion of the observer. Stellar aberration is divided into diurnal or orbital, annual, and secular components.

accuracy: evaluation of the uncertainty of a measurement due to the uncorrected systematic errors. With the precision, it is one of the two components of the uncertainty.

adaptive optics: active optics correctors that adjust the optics to compensate for the wavefront distortions due to changes in the inhomogeneity of the atmosphere as measured from close artificial or bright star measurements.

altitude: the angular distance of a celestial body above or below the horizon, measured along the great circle passing through the body and the zenith. Altitude is $9 0 ^ { \circ }$ minus zenith distance.

apparent place: the geocentric position in the CIRF (or GTRF) of a specific time determined by removing from the directly observed position of a celestial body the effects that depend on the topocentric location of the observer; i.e. refraction, diurnal aberration, geocentric (diurnal) parallax, polar motion, and Earth rotation. Thus, the position at which the object would actually be seen from the center of the Earth, displaced by the light bending and aberration, except the diurnal part (see aberration, planetary; aberration, stellar; aberration, diurnal), and referred to the true equator and the CEO or the equinox.

astrometric positions: observed positions with respect to GCRF reference stars at some epoch. Positions have not been corrected for annual or planetary aberration and light bending.

astronomical coordinates: the longitude and latitude of a point on Earth relative to the ITRF and the local vertical. These coordinates are influenced by local gravity anomalies.

astronomical unit (AU): the radius of a circular orbit in which a body of negligible mass, and free of perturbations, would revolve around the Sun in $2 \pi / k$ days, where $k$ is the Gaussian gravitational constant. This is slightly less than the semimajor axis of the Earth’s orbit. Its best estimate is $1 . 4 9 5 9 7 8 7 0 6 9 1 \times 1 0 ^ { 8 } \mathrm { m }$ .

azimuth: the angular distance measured clockwise along the horizon from a specified reference point (usually north) to the intersection with the great circle drawn from the zenith through a body on the celestial sphere.

barycenter: the center of mass of a system of bodies; e.g. the center of mass of the Solar System or the Earth–Moon system.

barycentric: with reference to, or pertaining to the barycenter of the Solar System. Otherwise, the mass system should be specified (e.g. the Earth–Moon system).

Barycentric Celestial Reference Frame (BCRF): the realization of the BCRS centered at the barycenter of the Solar System by extragalactic objects (kinematic BCRF) or coordinates and motions of planets (dynamical BCRF); specifically, a barycentric ICRF.

Barycentric Celestial Reference System (BCRS): a global space fixed coordinate system centered at the barycenter of the Solar System, defined by the metric tensor of the IAU 2000 resolutions. More specifically, it is a barycentric International Celestial Reference System (ICRS).

Barycentric Coordinate Time (TCB): the coordinate time for BCRS, a coordinate system at the barycenter of the Solar System, related to Geocentric Coordinate Time (TCG) and Terrestrial Time (TT) by relativistic transformations that include secular terms.

Barycentric Dynamical Time (TDB): an independent argument of ephemerides and equations of motion that are referred to the barycenter of the Solar System. A family of time scales results from the transformation by various theories and metrics of relativistic theories of Terrestrial Time (TT). TDB is a coordinate time, which differs from TT only by periodic variations. Since TT and TDB have the same rates, owing to the relativistic transformation of the space-time metrics, the implied units of distance are different.

Barycentric Ephemeris Time $( T _ { \mathrm { e p h } } )$ : an independent time argument of barycentric ephemerides. This time scale is a linear function of TCB. Each ephemeris defines its own version of $T _ { \mathrm { e p h } }$ . The linear drift between $T _ { \mathrm { e p h } }$ and TCB is chosen so that the rates of $T _ { \mathrm { e p h } }$ and TT are as close as possible for the time span covered by the particular ephemeris.

catalog equinox: the intersection of the hour circle of zero right ascension of a star catalog with the celestial equator.

catalog positions: positions on the ICRF.

Celestial Ephemeris Origin (CEO): origin for right ascensions on the true equator of date. Its motion has no component along the true instantaneous equator. Also called Celestial Intermediate Origin (CIO).

Celestial Ephemeris Pole (CEP): the reference pole for nutation and polar motion; the axis of figure for the mean surface of a model Earth in which the free motion has zero amplitude. This pole has no nearly-diurnal nutation with respect to a space-fixed or Earth-fixed coordinate system. (Used from 1984 to 2003 with the IAU 1980 Theory of Nutation.)

celestial equator: the plane perpendicular to the Celestial Ephemeris Pole or the Celestial Intermediate Pole. Colloquially, the projection onto the celestial sphere of the Earth’s equator.

celestial intermediate equator, or the true equator: equatorial plane through the center of the Earth and perpendicular to the Celestial Intermediate Pole (CIP) at some epoch.

Celestial Intermediate Origin (CIO): see CEO.

Celestial Intermediate Pole (CIP): Geocentric equatorial pole determined by the IAU 2000A precession–nutation model which provides the transformation from the ICRF to the GCRF.

Celestial Intermediate Reference Frame (CIRF): geocentric reference frame defined by the true equator, CIP, and CEO on a specific date. It is also called Geocentric True Reference Frame (GTRF).

celestial pole: either of the two points projected onto the celestial sphere by the extension of the Earth’s axis of rotation to infinity.

celestial sphere: an imaginary sphere of arbitrary radius, upon which celestial bodies may be considered to be located. As circumstances require, the celestial sphere may be centered at the observer, at the Earth’s center, or at any other location.

center of figure: that point so situated relative to the apparent figure of a body that any line drawn through it divides the figure into two parts having equal apparent areas. If the body is oddly shaped, the center of figure may lie outside the figure itself.

center of light: same as center of figure except referring to the illumination, each point being weighted by its intensity. It is also called photocenter.

collimation: alignment of an optical system.

coordinate time: the fourth component of the space-time metric in the Theory of Relativity. TCB and TCG are the coordinate times associated with the barycentric and the geocentric coordinate sytems.

Coordinated Universal Time (UTC): the time scale available from broadcast time signals. UTC differs from TAI (see International Atomic Time) by an integral number of seconds; it is maintained within $\pm 0 . 9 0$ second of UT1 (see Universal Time) by the introduction of one second steps (leap seconds).

correlation coefficient: a measure of the dependency between two variables.

covariance: the product of the standard deviations of two variables and their correlation coefficients.

datums: local geodetic coordinate systems.

declination: angular distance north or south of the celestial equator. It is measured along the hour circle passing through the celestial object. Declination is usually given in combination with right ascension or hour angle.

deflection of light: the angle by which the path of a photon is altered from a straight line by the gravitational field of a massive body. The path is deflected radially towards the mass. In the case of the Sun, it amounts up to $1 ^ { \prime \prime } 7 5$ at the Sun’s limb. Correction for this effect, which is independent of wavelength, is included in the reduction from CIRF to BCRF.

deflection of the vertical: the angle between the astronomical vertical, perpendicular to the local equipotential surface, and the geodetic vertical, perpendicular to the reference terrestrial spheroid.

delta T, $\Delta T$ : the difference between Terrestrial Time and Universal Time; specifically the difference between Terrestrial Time TT and UT1:

$$
\Delta T = \mathrm { T T } - \mathrm { U T 1 } .
$$

delta UT1, $\Delta \mathrm { U T 1 }$ (or $\Delta \mathrm { U T }$ ): the predicted value of the difference between UT1 (UT) and UTC, transmitted in code on broadcast time signals:

$$
\Delta \mathrm { U T 1 } = \mathrm { U T 1 } - \mathrm { U T C } .
$$

diurnal motion: the apparent daily motion caused by the Earth’s rotation, of celestial bodies across the sky from East to West.

dynamical equinox: the ascending node of the Earth’s mean orbit on the Earth’s true equator; i.e. the intersection of the ecliptic with the celestial equator at which the Sun’s declination is changing from South to North.

dynamical time: the family of time scales introduced in 1984 to replace ephemeris time as the independent argument of dynamical theories and ephemerides. Examples: Barycentric Dynamical Time and Terrestrial Time.

Earth orientation: the Earth’s orientation with respect to ICRF. It is the combination of the Earth’s rotation around the polar axis, the polar motion, and the precession–nutation.

Earth potential model: list of values of spherical harmonics that specify the potential of the Earth.

Earth rotation angle: another name for the stellar angle.

eclipse: the obscuration of a celestial body caused by its passage through the shadow cast by another body.

ecliptic: mean plane of the Earth’s orbit around the Sun as determined from and designated by an ephemeris of the Earth (e.g. ecliptic of DE 405).

ecliptic longitudes and latitudes: coordinates measured from the equinox with respect to the ecliptic, which can be of date, mean, or conventionally fixed. They can be apparent, true, or mean, geocentric or barycentric.

Einstein circle or ring: the circle or ring image of a star formed when a star and a gravitational lens are aligned so the light is deviated by the same amount in all directions.

Einstein distance: the angle between the true direction to the source of the light and the direction where the light is seen owing to the deviation by a gravitational lens.

Einstein radius: radius of the Einstein ring.

ephemeris hour angle: an hour angle referred to the ephemeris meridian.

ephemeris longitude: terrestrial longitude measured eastward from the ephemeris meridian.

ephemeris meridian: a fictitious meridian that rotates independently of the Earth at the uniform rate implicitly defined by Terrestrial Time (TT). The ephemeris meridian is $1 . 0 0 2 7 3 8 \Delta T$ east of the International (Greenwich) meridian, where $\Delta T = \mathrm { T T } - \mathrm { U T } 1$ .

Ephemeris Time (ET): the time scale used prior to 1984 as the independent variable in gravitational theories of the Solar System. In 1984, ET was replaced by dynamical time.

ephemeris transit: the passage of a celestial body or point across the ephemeris meridian.

epoch: an arbitrary fixed instant of time or date used as a chronological reference datum for calendars, celestial reference systems, star catalogs, or orbital motions.

equation of the equinoxes: the right ascension of the mean equinox referred to the true equator and equinox; alternatively apparent sidereal time minus mean sidereal time.

equation of time: the hour angle of the true Sun minus the hour angle of the fictitious mean sun; alternatively, apparent solar time minus mean solar time.

equator: the great circle on the surface of a body formed by the intersection of the surface with the plane passing through the center of the body perpendicular to the axis of rotation.

equinox: either of the two points at which the ecliptic intersects the celestial intermediate equator; also the time at which the Sun passes through either of these intersection points; i.e. when the apparent longitude of the Sun is $0 ^ { \circ }$ or $1 8 0 ^ { \circ }$ . When required, the equinox can be designated by the ephemeris of the Earth from which it is obtained (e.g. vernal equinox of DE 405).

equinox right ascensions: right ascensions that are measured from the equinox, instead of from the CEO or CIO.

fixed ecliptic: ecliptic for any ephemeris at epoch J2000.0. The ecliptic has a specified offset from the ICRS origin and the obliquity has a determined value.

Fizeau interferometer: interferometer whose two entry pupils are parts of a single telescope, not necessarily a complete mirror. The interferences are uniform all over the field of view of the instrument.

free core nutation: component of the nutation due to the free wobble of the Earth’s core. It is not modeled in the IAU 2000 precession–nutation formula and is provided by the IERS.

galactic coordinates: system of coordinates (galactic longitude and latitude) whose principal plane is the mean plane of the Galaxy and the origin near the galactic center. It is defined by its position in the ICRF.

Gaussian gravitational constant $( k = 0 . 0 1 7 2 0 2 0 9 8 9 5 )$ : the constant defining the astronomical system of units of length (astronomical unit), mass (solar mass) and time (day), by means of Kepler’s third law. The dimensions of $k ^ { 2 }$ are those of Newton’s constant of gravitation: $\mathrm { L } ^ { 3 } / ( \mathrm { M } ^ { 1 } \mathrm { T } ^ { 2 } )$ .

geocentric: with reference to, or pertaining to, the center of the Earth.

geocentric apparent right ascensions and declinations: positions measured in the GTRF of a specific time. The topocentric positions have been corrected for diurnal aberration and parallax, polar motion, UT1 irregularities, and TCG – TT. Geocentric apparent right ascensions and declinations may be thought as equivalent to previous designations of apparent right ascensions and declinations.

Geocentric Celestial Reference Frame (GCRF): the transformation of the Barycentric Celestial Reference Frame (BCRF) to the geocenter. It is also a realization of the GCRS, by extragalactic objects. More specifically, geocentric ICRF.

Geocentric Celestial Reference System (GCRS): a global direction fixed coordinate system centered at the geocenter, defined by the metric tensor of the IAU 2000 resolutions. It is defined such that its spatial coordinates are kinematically non-rotating with respect to the barycentric ones.

geocentric coordinates: the latitude and longitude or rectangular coordinates of a point on the Earth’s surface relative to the center of the Earth. Also, celestial coordinates given with respect to the center of the Earth.

Geocentric Coordinate Time (TCG): coordinate time for GCRS a coordinate system at the geocenter, related to Terrestrial Time (TT) by a relativistic linear transformation.

Geocentric True Reference Frame (GTRF): another name for the Celestial Intermediate Reference Frame (CIRF). Observed positions are corrected for aberration.

geocentric true right ascensions and declinations: coordinates measured in a geocentric true reference system at a specific time in TCG or TT. They are geocentric apparent positions corrected for deflection of light and annual aberration.

geodesic: the path with minimum length between two points in a mathematically defined $n$ -dimension space.

geodesic precession and nutation: the effect on a moving reference frame around a fixed reference frame when both frames have fixed coordinate directions. Specifically, the coordinate transformation between GCRS and BCRS. The geodesic precession is the secular rotational part of the transformation, and geodesic nutation is the periodic part.

geodetic coordinates: the latitude and longitude of a point on the Earth’s surface determined from the geodetic vertical (normal to the specified spheroid).

geoid: the equipotential surface on which the geopotential is $U _ { \mathrm { G } } =$ $6 2 6 3 6 8 5 6 \mathrm { m } ^ { 2 } / \mathrm { s } ^ { 2 }$ . It roughly coincides with mean sea level in the open ocean.

geometric positions: the positions of an object in a three dimensional reference frame that can be either topocentric, geocentric, or barycentric with the Oxyz axes parallel to the ICRF axes.

gnomonic projection: the geometric transform of the projection of an area of the celestial sphere onto a plane tangent to the celestial sphere. It transforms differential spherical coordinates into rectangular coordinates.

gravitational lens: a celestial body whose gravitational field bends light from a more distant source, so that one or several images of it are produced (see Einstein distance).

Greenwich sidereal date (GSD): the number of sidereal days and fraction of a day elapsed at the International meridian since the beginning of the Greenwich sidereal day that was in progress at Julian date 0.0.

Greenwich sidereal day number: the integral part of the Greenwich sidereal date.

Greenwich sidereal time (GST): the hour angle measure of the Terrestrial Ephemeris Origin (TEO), or TIO, meridian (Greenwich or International meridian) with respect to the ICRF.

height: elevation upwards from the geoid to a fixed point. More generally, distance upwards from a given level, particularly the geoid.

heliocentric: with reference to, or pertaining to, the center of the Sun.

horizon: a plane perpendicular to the line from an observer to the zenith. The great circle formed by the intersection of the celestial sphere with the horizon is called the astronomical horizon.

hour angle: angular distance measured westward along the celestial equator from the meridian to the hour circle that passes through a celestial object.

hour circle: a great circle on the celestial sphere that passes through the celestial poles and is therefore perpendicular to the celestial equator.

inclination: the angle between two planes or their poles; usually the angle between an orbital plane and a reference plane; one of the standard orbital elements that specifies the orientation of an orbit.

interferometry: astrometric technique producing interferences between two images of a celestial source for the derivation of geometric relations between the baseline of the instrument and the apparent direction of the source.

International Atomic Time (TAI): the continuous scale resulting from analyses by the Bureau International des Poids et Mesures (BIPM) of atomic time standards in many countries. The fundamental unit of TAI is the SI second (see second), and the epoch is 1958, January 1.0.

International Celestial Reference Frame (ICRF): radio sources realization of the barycentric, fixed, celestial reference system (ICRS), based on extragalactic sources. Other realizations have a specific name (e.g. HCRF: Hipparcos Celestial Reference Frame).

International Celestial Reference System (ICRS): a global direction fixed coordinate system, defined by the metric tensor of the IAU 2000 resolutions. It can be geocentric (GCRS) or barycentric (BCRS) in its restricted meaning.

International Terrestrial Reference Frame (ITRF): a realization of the ITRS by a set of coordinates and velocities of fiducial points on the Earth (e.g. ITRF 2000).

International Terrestrial Reference System (ITRS): the terrestrial reference system to which the positions on the Earth are referred. It is geocentric and has no global residual rotation with respect to horizontal motions at the Earth’s surface.

invariable plane: the plane through the center of mass of the Solar System perpendicular to the angular momentum vector of the Solar System.

isoplanatic patch: region of the sky within which the refraction effect is relatively uniform.

Julian date (JD): the interval of time in days and fraction of a day since 4713 BC January 1, Greenwich noon, Julian proleptic calendar. In precise work the time scale, TCB, TCG, TT, or Universal Time, should be specified.

Julian date, modified (MJD): the Julian date minus 2 400 000.5.   
Julian day number: the integral part of the Julian date.

Julian year: a period of 365.25 days. This period served as the basis for the Julian calendar, and is now used as a standard astronomical period.

latitude, celestial: angular distance on the celestial sphere measured North or South of the ecliptic along the great circle passing through the poles of the ecliptic and the celestial object.

latitude, terrestrial: angular distance on the Earth measured North or South of the equator along the meridian of a geographic location.

leap second: a second (see second) added between $6 0 \mathrm { s }$ and 0 s at announced times to keep UTC within $\pm 0 . 9 0 \mathrm { s }$ of UT1. Generally, leap seconds are added to UTC at the end of June or December.

light-time: the interval of time required for light to travel from a celestial body to the Earth. During this interval the motion of the body in space causes an angular displacement of its apparent place from its geometric place.

light-year: the distance that light traverses in a vacuum during one year.

limb darkening: reduction of brightness when approaching the limb of stars (or Sun).

local sidereal time: the local hour angle of a catalog equinox.

longitude, celestial: angular distance on the celestial sphere measured eastward along the ecliptic from the dynamical equinox to the great circle passing through the poles of the ecliptic and the celestial object.

longitude, terrestrial: angular distance measured along the Earth’s equator from the international (Greenwich) meridian or the TEO to the meridian of a geographic location.

Lorentz transformation: in special relativity, relationship between coordinates and time in one reference frame and those in another reference frame which is moving with respect to the first reference frame.

Love and Shida numbers: numbers that describe the proportionality of the local reaction of the deformable Earth to an external potential.

magnitude: a measure on a logarithmic scale of the brightness of a celestial object. There are many magnitude systems depending on the filters used (e.g. UBV or SLOAN).

magnitude, absolute: magnitude that a star would have if it were at a distance of ten parsecs from the Sun.

mean equator and equinox: the celestial reference system determined by ignoring short-period variations (nutation) in the motions of the celestial equator. Thus, the mean equator and equinox are affected only by precession. This requires using a separated precession expression and nutation theory.

mean place: the barycentric position, referred to the mean equator and equinox of a standard epoch, of an object on the celestial sphere. A mean place is determined by removing from the directly observed position the effects of refraction, geocentric and stellar parallax, diurnal and stellar aberration, deflection of light, and by referring the coordinates to the mean equator and equinox of a standard epoch. In compiling star catalogs it has been the practice not to remove the secular part of stellar aberration.

mean Sun: a fictitious body defined by Newcomb to define a mean solar time that averaged the Earth rotation. It was used to define the Besselian year until 1984.

meridian: a great circle passing through the celestial poles and through the zenith of a location on Earth. For planetary observations a meridian is half the great circle passing through the planet’s poles and through any location on the planet.

metric: in the theory of relativity, the expression representing the square of the four-dimensional distance of two close generalized events; it is noted $\mathrm { d } s ^ { 2 }$ .

Michelson interferometer: two identical telescopes point at a given star, the images are recombined forming interference patterns based on the differences in the phases of the two images.

moving celestial reference frame: celestial reference frame defined by the true equator and equinox or the CEO. The coordinates are right ascension and declination with the origin to be specified.

nadir: the point on the celestial sphere diametrically opposite to the zenith.

node: either of the points on the celestial sphere at which the plane of an orbit intersects a reference plane. The position of a node is one of the standard orbital elements used to specify the orientation of an orbit.

nutation: the oscillations in the motion of the pole of rotation of a freely rotating body that is undergoing torque from external gravitational forces. The secular part of the motion is called precession. For the Earth, terms with periods less than two days are included in the polar motion. Nutation of the Earth’s pole is discussed in terms of components in obliquity and longitude (see precession, polar motion).

obliquity: in general, the angle between the equatorial and orbital planes of a body or, equivalently, between the rotational and orbital poles. For the Earth the obliquity of the ecliptic is the angle between the planes of the equator and the ecliptic.

occultation: the obscuration of one celestial body by another of greater apparent diameter; especially the passage of the Moon in front of a star or planet, or the disappearance of a satellite behind the disk of its primary. If the primary source of illumination of a reflecting body is cut off by the occultation, the phenomenon is also called an eclipse. The occultation of the Sun by the Moon is a solar eclipse.

opposition: a configuration of the Sun, Earth and a planet in which the apparent geocentric longitude (see longitude, celestial) of the planet differs by $1 8 0 ^ { \circ }$ from the apparent geocentric longitude of the Sun.

orbit: the path in space followed by a celestial body.

parallactic correction: the difference in apparent direction of an object as seen from two different locations; conversely, the angle at the object that is subtended by the line joining two designated points.

parallax, annual: the difference between hypothetical geocentric and barycentric observations.

parallax, diurnal or geocentric: the difference in direction between a topocentric observation and a hypothetical geocentric observation.

parallax, horizontal: the difference between the topocentric and hypothetical geocentric observations of an object, when the object is on the astronomical horizon.

parallax, orbital: the difference in direction between an observation from a spacecraft and a hypothetical geocentric observation.

parallax, stellar: the angle subtended at the observed object by one astronomical unit.

parsec: the distance at which one astronomical unit subtends an angle of one second of arc; equivalently, the distance to an object having an annual parallax of one second of arc. A parsec is equal to 3.261 633 light-years.

period: the interval of time required to complete one revolution in an orbit or one cycle of a periodic phenomenon, such as the rotation of a body or a cycle of phases.

perturbations: deviations between the actual orbit of a celestial body and an assumed reference orbit; also, the forces that cause deviations between the actual and reference orbits. Perturbations, according to the first meaning, are usually calculated as quantities to be added to the coordinates of the reference orbit to obtain the precise coordinates.

phase: the ratio of the illuminated area of the apparent disk of a celestial body to the area of the entire apparent disk taken as a circle. For the Moon, phase designations are defined by specific configurations of the Sun, Earth and Moon. For eclipses, phase designations (total, partial, penumbral, etc.) provide general descriptions of the phenomena. More generally, for use with oddly shaped bodies, phase might be defined as $0 . 5 ( 1 + \cos$ (phase angle)).

phase angle: the angle measured at the center of an illuminated body between directions of the light source and the observer.

phase coefficient: expression for the observationally determined magnitude correction for variation in brilliancy of planets with phase angle.

photometry: a measurement of the intensity of light usually specified for a specific wavelength filter (see magnitude).

polar motion: the irregularly varying motion of the Celestial Intermediate Pole (CIP) with respect to the ITRF, including all periodic terms less than two days.

precession: the uniformly progressing motion of the pole of rotation of a freely rotating body undergoing torque from external gravitational forces. In the case of the Earth, the component of precession caused by the Sun and Moon acting on the Earth’s equatorial bulge is called luni-solar precession; the component caused by the action of the planets is called planetary precession. The sum of luni-solar and planetary precession is called general precession.

precession–nutation: the ensemble of effects of external torques on the motion of the CIP.

precision: evaluation of the uncertainty due to the random errors of a measurement.

With the accuracy, it is one of the two components of the uncertainty.

probability density function (pdf): a continuous function that takes on, for each possible value of a random variable, the associated probability.

proper motion: the projection onto the celestial sphere of the space motion of a star relative to the barycenter of the Solar System. Proper motion is usually tabulated in star catalogs as changes in right ascension and declination per year or century.

proper time: in the theory of relativity, the time linked to an object, which also applies to the local physics in a frame at rest with respect to the object.

pulsar: rapidly spinning bodies emitting very stable periodic pulses of radiowaves and often in other wavelengths.

radial velocity: the rate of change of the distance to an object.

reference frame: practical realization of a reference system, usually as a catalog of positions and proper motions of a certain number of fiducial points on the sky (stars or radio sources). For instance, ICRF is the realization of ICRS.

reference system: theoretical concept of a system of coordinates, including time and standards, necessary to specify the bases for representing the position and motion of bodies in space.

refraction, astronomical: the change in direction of travel (bending) of a light ray as it passes obliquely through the atmosphere. As a result of refraction the observed altitude of a celestial object is greater than its geometric altitude. The amount of refraction depends on the altitude of the object and on atmospheric conditions.

right ascension: angular distance measured eastward along the celestial equator from the CEO, or equinox, to the hour circle passing through the celestial object. Right ascension is given either in degrees, or in hours, minutes, and seconds.

right ascension $\alpha$ and declination δ: without qualification, right ascensions and declinations measured in ICRS. The epoch of the positions must be specified. By extension, catalog or mean position in a barycentric reference system from the catalog right ascension fiducial point and from the catalog equator, respectively. They are designated with the catalog reference system as necessary (e.g. Hipparcos right ascension and declination at epoch 1991.25 on TCB).

Roche limit: critical distance at which an approaching smaller body becomes structurally unstable and disintegrates.

second: the time unit in the Syst\`eme International d’Unit´es (SI). It is the duration of 9 192 631 770 cycles of radiation corresponding to the transition between two hyperfine levels of the ground state of cesium-133.

seeing: size of a smeared star from the short-period perturbations of the atmosphere during an observation.

selenocentric: with reference to, or pertaining to, the center of the Moon.

semidiameter: the angle at the observer subtended by the equatorial radius of the Sun, Moon or a planet.

Shida number: see Love and Shida numbers.

sidereal day: time necessary for sidereal time to increase by $3 6 0 ^ { \circ }$ .

sidereal hour angle: angular distance on the celestial sphere measured westward along the celestial equator from the catalog equinox to the hour circle passing through the celestial object. It is equal to $3 6 0 ^ { \circ }$ minus right ascension in degrees.

sidereal time: the measure of the angle defined by the apparent diurnal motion of the catalog equinox; hence, a measure of the rotation of the Earth with respect to the stars rather than the Sun. It is often expressed in hours, minutes, and seconds, one hour being equal to $1 5 ^ { \circ }$ .

solar time: the measure of time based on the diurnal motion of the Sun. The rate of diurnal motion undergoes seasonal variation because of the obliquity of the ecliptic and because of the eccentricity of the Earth’s orbit. Additional small variations result from irregularities in the rotation of the Earth on its axis.

solstice: either of the two points on the ecliptic at which the apparent longitude (see longitude, celestial) of the Sun is $9 0 ^ { \circ }$ or $2 7 0 ^ { \circ }$ ; also, the time at which the Sun is at either point.

space motion: three-dimensional velocity vector of a star, expressed in kilometers per second. Its components are the radial velocity and the transverse velocity derived from the proper motion and the parallax.

space-time coordinate system: a four-dimensional set of three space and one time coordinates, based on a specific metric, that specify an event in relativity theory.

speckles: irregular patterns at the focus of the telescope produced by light from a point source crossing atmosphere cells.

spectral types or classes: categorization of stars according to their spectra, primarily due to differing temperatures of the stellar atmosphere. From hottest to coolest, the main spectral types are O, B, A, F, G, K and M.

standard deviation: an evaluation of the precision of a measurement assuming a random (Gaussian) distribution of errors, with a level of confidence of $6 8 . 2 7 \%$ . It is the square root of the variance, which is the sum of the squares of the measurement residuals divided by the number of the measurements minus one.

standard epoch: a date and time that specifies the reference system to which celestial coordinates are referred. Prior to 1984, coordinates of star catalogs were commonly referred to the mean equator and equinox of the beginning of a Besselian year. Beginning with 1984 the Julian year has been used, as denoted by the prefix J, e.g. J2000.0.

stellar angle, or Earth rotation angle: angle measured along the true equator of the Celestial Intermediate Pole (CIP) between the Terrestrial Ephemeris Origin (TEO), or TIO, and the Celestial Ephemeris Origin (CEO), or CIO, positively in the retrograde direction. It is proportional to UT1.

synodic period: for planets, the mean interval of time between successive conjunctions of a pair of planets, as observed from the Sun; for satellites, the mean interval between successive conjunctions of a satellite with the Sun, as observed from the satellite’s primary.

synodic time: pertaining to successive conjunctions; successive returns of a planet to the same aspect as determined by Earth.

TAI: Temps Atomique International, see International Atomic Time

Terrestrial Ephemeris Origin (TEO): the origin of terrestrial longitudes of the International Terrestrial Reference System (ITRS) of date. Also called Terrestrial Intermediate Origin (TIO).

Terrestrial Intermediate Origin (TIO): see TEO.

Terrestrial Time (TT): the independent argument for apparent geocentric ephemerides, previously known as Terrestrial Dynamical Time (TDT). At 1977 January $1 ^ { \mathrm { d } } 0 0 ^ { \mathrm { h } } 0 0 ^ { \mathrm { m } } 0 0 ^ { \mathrm { s } }$ TAI, the value of TT was exactly 1977 January 1.000 3725 days. The unit of TT is the SI second or a day of 86 400 SI seconds at the geoid. One realization of TT is $\mathrm { T T } ( \mathrm { T A I } ) = \mathrm { T A I } + 3 2 . 1 8 4 \ \mathrm { s }$ . See Geocentric Coordinate Time (TCG).

time dilatation: the positive difference between a time interval measured in a moving frame and the same one measured in a frame fixed with respect to the events.

tip-tilt correction: two-dimensional corrections of the secondary mirror to compensate for the changes in the atmosphere during an observation.

topocentric: with reference to, or pertaining to, a point on the surface of the Earth.

topocentric position: the observed position corrected for refraction and instrumental parameters, on UTC or TT.

transit: the passage of the apparent center of the disk of a celestial object across a meridian; also, the passage of one celestial body in front of another of greater apparent diameter (e.g., the passage of Mercury or Venus across the Sun, or Jupiter’s satellites across its disk); however, the passage of the Moon in front of the larger apparent Sun is called an annular eclipse. The passage of a body’s shadow across another body is called a shadow transit; however, the passage of the Moon’s shadow across the Earth is called a solar eclipse.

true equator: another name of the Celestial Intermediate Equator; it is the equatorial plane through the center of the Earth and perpendicular to the CIP pole at some specific time.

true equator and equinox: the classical moving celestial coordinate frame determined by the instantaneous positions of the celestial equator and ecliptic. The motion of this system is due to the progressive effect of precession and of nutation.

true positions: ICRF positions that have been transformed to the CEO and celestial intermediate, or true, equator of a specific epoch by the application of precession–nutation and geodesic precession and nutation. The same name applies for positions in the equator–equinox reference frame (see moving celestial reference frame).

true value: value that would be obtained by a perfect measurement. True values are by nature indeterminate and an expected value is often used as a true value.

uncertainty: parameter, associated with the result of a measurement, that characterizes the dispersion that can be attributed to include the expected value of the measured quantity with some given probability. Its components are accuracy and precision. Also, estimation of the difference between the measurement and the true value.

Universal Time (UT): a measure of time that conforms, within a close approximation, to the mean diurnal motion of the Sun and serves as the basis of all civil timekeeping. It is determined from observations of the diurnal motions of the stars. It has several realizations: UT0, UT1, and UTC.

UT0: the Universal Time as determined directly from observations; it is slightly dependent on the place of observation.

UT1: time scale deduced from the UT0 corrected for the shift in longitude of the observing station caused by polar motion. It was related by a mathematical formula to the sidereal time in the moving reference frame, or to the stellar angle in the CIRF.

UTC: see Coordinated Universal Time.

vernal equinox: the ascending node of the ecliptic on the celestial equator; also, the time at which the apparent longitude (see longitude, celestial) of the Sun is $0 ^ { \circ }$ (see equinox).

vertical: the apparent direction of gravity at the point of observation (normal to the plane of a free level surface).

year: a period of time based on the revolution of the Earth around the Sun. The calendar year is an approximation to the tropical year (see year, tropical). The anomalistic year is the mean interval between successive passages of the Earth through perihelion. The sidereal year is the mean period of revolution with respect to the background stars.

year, Besselian: the period of one complete revolution in right ascension of the fictitious mean sun, as defined by Newcomb. The beginning of a Besselian year, traditionally used as a standard epoch, is denoted by the suffix “.0”. Since 1984 standard epochs have been defined by the Julian year rather than the Besselian year. For distinction, the beginning of the Besselian year is now identified by the prefix B (e.g., B1950.0).

year, tropical: the period of one complete revolution of the mean longitude of the Sun with respect to the dynamical equinox. The tropical year is longer than the Besselian year by $0 . 1 4 8 T$ s, where $T$ is centuries from B1900.0.

zenith: in general, the point directly overhead on the celestial sphere. The astronomical zenith is the extension to infinity of a plumb line. The geocentric zenith is defined by the line from the center of the Earth through the observer. The geodetic zenith is the normal to the geodetic ellipsoid at the observer’s location (see deflection of the vertical).

zenith distance: angular distance on the celestial sphere measured along the great circle from the zenith to the celestial object. Zenith distance is $9 0 ^ { \circ }$ minus altitude.

# References

Note: the chapters of this book where the references are cited are indicated in parentheses.

Adams, J. C., 1853, Phil. Trans. R. Soc. London, CXLIII, 397–406. (Ch. 1) Altamimi, Z., Sillard, P. and Boucher, C., 2002, J. Geophys. Res., 107 NB10, 2214, ETG2. (Ch. 9) Andersen, J., 1991, Astron. & Astrophys. Review, 3, 91–126. (Ch. 12) Andersen, J., 2001, Transactions of the IAU, vol. XXIV B. (Ch. 5) Anderson, J. and King, I. R., 1999, Publ. Astro. Soc. Pacific 111, 1095–1098. (Ch. 14) Angel, R. and Woolf, N., 1997, Astrophys. J., 475, 373–379. (Ch. 14) Aoki, S., Guinot, B., Kaplan, G. H., Kinoshita, H., McCarthy, D. D. and Seidelmann, P. K., 1982, Astron. & Astrophys., 105, 359–361. (Ch. 8, 10, 14) Aoki, S. and Kinoshita, H., 1983, Celest. Mech., 29, 335–360. (Ch. 10) Arias, E. F., Charlot, P., Feissel, M. and Lestrade, J.-F., 1995, Astron. & Astrophys., 303,   
604–608. (Ch. 7) Backer, D. C., 1993, in Galactic High-Energy Astrophysics, High Accuracy Timing and Positional Astronomy, J. van Paradijs and H. M. Maitzes (Eds.), Lecture Notes in Physics, 418, Springer Verlag, Berlin, Heidelberg, 193–253. (Ch. 12) Backer, D. C. and Hellings, R. W., 1986, Ann. Rev. Astron. Astrophys., 24, 537–575. (Ch. 14) Bastian, U., R¨oser, S. et al., 1993, PPM Star Catalogue, Spektrum Akademisher Verlag, Heidelberg, III and IV. (Ch. 11) Bastian, U., R¨oser, S., Høg, E. et al., 1996, Astron. Nachr., 317, 281–288. (Ch. 2) Battin, R. H., 1987, An Introduction to the Mathematics and Methods of Astrodynamics, American Institute of Aeronautics and Astronautics Inc., New York. (Ch. 3) Beichman, C. A., 1998, Proceed. SPIE, 3350, 719. (Ch. 14) Bertotti, B., Carr, B. J. and Rees, M. J., 1983, Monthly Not. RAS, 203, 945–951. (Ch. 14) Blaauw, A., Gum, C. S., Pawsey, J. L. and Westerhout, G., 1960, Monthly Not. RAS, 121,   
123–131. (Ch. 7) Black, D. C., 1995, Ann. Rev. Astron. Astrophys., 33, 359–380. (Ch. 14) Black, D. C. and Scargle, J. D., 1982, Astrophys. J., 263, 854–869. (Ch. 14) Blandford, R. and Teukolsky, S. A., 1976, Astrophys. J., 205, 580–591. (Ch. 14) Blandford, R., Romani, R. and Narayan, R., 1984, J. Astrophys. Astron., 5, 369–388. (Ch. 14) Borkowski, K. M., 1989, Bulletin Geod ´ esique ´ , 69, (1), 50–56. (Ch. 9) Boss, B., Albrecht, S., Jenkins, H. et al., 1937, General Catalogue of 33342 stars for the Epoch 1950, Carnegie Institution of Washington Publ., 5 volumes. (Ch. 11)   
Boss, L., 1910, Preliminary General Catalogue of 6188 Stars for Epoch 1900, Carnegie Institution of Washington, Washington. (Ch. 11)   
Boucher, C., 1990, in Variations in Earth Rotation, D. D. McCarthy and W. E. Carter (Eds.) , 197–201. (Ch. 9)   
Boucher, C., Altamimi, Z. and Sillard, P., 1999, The 1997 International Terrestrial Reference Frame (ITRF-97), IERS Technical note 27, May 1999, Observatoire de Paris. (Ch. 9)   
Bouill´e, F., Cazenave, A., Lemoine, J.-M. and Cr´etaux, J.-F., 2000, Geophys. J. Int., 143, 71–82. (Ch. 9)   
Brosche, P., Wildermann, E. and Geffert, M., 1989, Astron. & Astrophys., 211, 239–244. (Ch. 14)   
Brouwer, D. and Clemence, G.M., 1961, Methods of Celestial Mechanics, Academic Press, New York and London. (Ch. 8, 9)   
Brumberg, V. A., 1991a, Essential Relativistic Celestial Mechanics, Adam Hilger, Bristol, Philadelphia, New York. (Ch. 5, 7)   
Brumberg, V .A., 1991b, in Reference Systems, Proceedings of IAU Coll. 127, J. A. Hughes, C. A. Smith and G. H. Kaplan (Eds.), U.S. Naval Observatory, Washington D.C., 36–49. (Ch. 7)   
Brumberg, V. A. and Groten, E., 2001, Astron. & Astrophys., 367, 1070–1077. (Ch. 7)   
Brumberg, V. A. and Kopeikin, S. M., Celestial Mech. and Dynam. Astron., 48, 23–44. (Ch. 5)   
Buffett, B. A., Mathews, P. M. and Herring, T. A., 2002, J. Geophys. Res., 107 ETG 5-1-14. (Ch. 8)   
Capitaine, N., 1990, Celest. Mech. Dyn. Astron., 46, 127–143. (Ch. 8)   
Capitaine, N., Guinot, B. and Souchay, J., 1986, Celest. Mech., 39, 283–307. (Ch. 8)   
Capitaine, N., Chapront, J. Lambert S. and Wallace, P., 2002, Astron. & Astrophys., 400, 1145–1154. (Ch. 10)   
Capitaine, N. and Gontier, A.-M., 1993, Astron. & Astrophys., 275, 645–650. (Ch. 10)   
Capitaine, N., Guinot, B. and McCarthy, D. D., 2000, Astron. & Astrophys., 355, 398–405. (Ch. 10)   
Cazenave, A., Valette, J.-J. and Boucher, C., 1992, J. Geophys. Res., 97, 7109–7119. (Ch. 9)   
Chapront, J., Chapront-Touz´e, M. and Francou, G., 1999, Astron. & Astrophys., 343, 624–633. (Ch. 8)   
Chapront, J., Chapront-Touz´e, M. and Francou, G., 2002, Astron. & Astrophys., 387, 700–709. (Ch. 10)   
Chapront-Touz´e, M. and Chapront, J., 1988, Astron. & Astrophys., 190, 342–352. (Ch. 13)   
Charbonneau, D., Brown, T., Latham, D. and Mayor, M., 2000, Astrophys. J., 529, L45–48. (Ch. 12)   
Chen, J.L., Wilson, C.R., Eanes, R.J. and Tapley, B.D., 2000, J. Geophys. Res., 105, 16271–16277. (Ch. 9)   
Cheng, M. K. and Tapley, B. D., 1999, J. Geophys. Res., 104, 2661–2681. (Ch. 9)   
Cheng, M. K., Shum, C. K. and Tapley, B. D., 1997, J. Geophys. Res. 102, 22377–22390. (Ch. 9)   
Clausen, J. V., Gimenez, A. and Scarfe, C., 1986, Astron. & Astrophys., 167 287–296. (Ch. 12)   
Clemence, G. M., 1948, Astron. J., 53, 169–179. (Ch. 1)   
Colavita, M. M. and Shao, M., 1994, in Planetary Systems: Formation, Evolution, and Detection, B. F. Burke, J. H. Rahe, E. E.Roettger (Eds.), Kluwer Academic Publishers, Dordrecht, 385–390. (Ch. 11)   
Corbin, T., 1992, Transactions of the International Astronomical Union, Vol. XXIB, 1991, 149–150. (Ch. 11)   
Corbin, T. and Urban, S., 1988, in IAU Symposium No. 133, Mapping the Sky, S. Debarbat, J. A. Eddy, H. K. Eichhorn and A. P. Upgren (Eds.), Kluwer Academic Publishers, Dordrecht, 287–291. (Ch. 14)   
Cummings, A., Marcy, G. W. and Butler, R. P., 1999, Astrophys J., 526, 890–915. (Ch. 14)   
Danjon, A., 1929, L’Astronomie, XLIII, 13–22. (Ch. 1)   
Defraigne, P., Dehant, V. and Paquet, P., 1995, Celest. Mech. Dyn. Astron., 62, 363–376. (Ch. 8)   
Delaunay, C. E., 1865, Comptes Rendus des Seances de l’Acad ´ emie des Sciences ´ , 61, 1023–1032. (Ch. 1)   
DeMets, G., Gordon, R. G., Argus, D. F. and Stein, S., 1994, Geophys. Res. Lett., 21, 2191–2194. (Ch. 9)   
Derr, J., 1969, J. Geophys. Res., 74, 5202–5220. (Ch. 9)   
Deshpande, A. A., D’Allessandro, F. and McCulloch, P. M., 1996, J. Astrophys. Astron., 17, 7–16. (Ch. 14)   
de Sitter, W., 1927, Bull. of the Astron. Institutes of the Netherlands, IV, 21–38. (Ch. 1, 10)   
Dick, S. J., 1997, in History of Astronomy, An Encyclopedia, John Lankford (Ed.), Garland Publishing Inc., New York & London, 47–60. (Ch. 1)   
Dieckvoss, W., 1971, in Conference on Photographic Astrometric Techniques, H. Eichhorn (Ed.), NASA publication, 161–167. (Ch. 11)   
DMA, 1987, in Department. of Defense World Geodetic System 1984 (DMA TR 83502, Washington D.C.). (Ch. 9)   
Downs, G. S. and Reichley, P. E., 1983, Astrophys. J. Suppl., 53, 169–240. (Ch. 14)   
Duncombe, R. L., Jefferys, W. H., Shelus, P. J. et al., 1991, Advan. Space Res., 11–2, 87–96. (Ch. 2)   
Eckhardt, D. H., 1981, The Moon and the Planets, 3, 3–49. (Ch. 13)   
Eddington, A. S., 1922, The Mathematical Theory of Relativity, Cambridge University Press, Cambridge. (Ch. 5)   
Eichhorn, H., 1960, Astron. Nachr., 285, 233. (Ch. 11)   
Eichhorn, H., 1974, Astronomy of Star Positions, F. Ungar Publishing Co., New York. (Ch. 11)   
Eichhorn, H., 1988, Astrophys. J., 334, 465–469. (Ch. 14)   
Eichhorn, H. and Jeffreys, W. H., 1971, Publ. McCormick Obs., 16. (Ch. 14)   
Eichhorn, H. and Russell, J., 1976, Mothly Not. RAS, 174, 679–694. (Ch. 14)   
Eichhorn, H. and Williams, C. A., 1963, Astron. J., 68, 221–231. (Ch. 14)   
Eichhorn, H., Googe, W. D. and Gatewood, G., 1967, Astron. J., 72, 626–630. (Ch. 14)   
ESA, 1997, The Hipparcos and Tycho Catalogues, European Space Agency Publication, SP-1200, June 1997, 17 volumes. (Ch. 2, 7, 11)   
ESA, 2000, GAIA, Concept and Technology Report, European Space Agency Publication, ESA–SCI (2000) 4. (Ch. 2)   
Felli, M. and Spencer, R. E., 1989, Very Long Baseline Interferometry, Techniques and Applications, Kluwer Academic Publishers, Dordrecht. (Ch. 2)   
Ferrel, W., 1864, Proc. of the American Academy of Arts and Sciences, VI, 379–383. (Ch. 1)   
Fock, V., 1976, The Theory of Space Time and Gravitation, Pergamon Press, Oxford. (Ch. 5)   
Folker, W. M., Charlot, P., Finger, M. H. et al., 1994, Astron. & Astrophys. 287, 279–289. (Ch. 7)   
Fricke, W., 1982, Astron. & Astrophys., 107, L13–L16. (Ch. 11)   
Fricke, W., Kopff, A. et al., 1963, Veroff. des Astron. Rechen-Institut Heidelberg ¨ , 10. (Ch. 11)   
Fricke, W., Schwan, H., Lederle, T. et al., 1988, Veroff. des Astron. Rechen-Institut, ¨ Heidelberg, 32. (Ch. 11)   
Fricke, W., Schwan, H. and Corbin, T., 1991, Veroff. Astron. Rechen-Institut, Heidelberg ¨ , 33. (Ch. 11)   
Fricke, W., Schwan, H., Corbin, T. et al., 1994, Veroff. Astron. Rechen-Institut, ¨ Heidelberg, 34. (Ch. 11)   
Fukushima, T., 1991, Astron. & Astroph., 244, L11–L12. (Ch. 7, 8)   
Fukushima, T., 1995, Astron. & Astroph., 294, 895–906. (Ch. 5)   
Fukushima, T., 1999, J. of Geodesy, 73, 603–610. (Ch. 9)   
Fukushima, T., 2001, Report on Astronomical Constants, in Highlights of Astronomy, Proceedings of the XXIV-th IAU General Assembly, H. Rickman (Ed.), Astron. Soc. of the Pacific, 107–112. (Ch. 7, 8)   
Gai, M., Carollo, D., Delbo, M. et al., 2001, Astron. & Astrophys., 367, 362–370. (Ch. 14)   
Garfinkel, B., 1944, Astron. J., 50, 169–179. (Ch. 6)   
Gatewood, G. D., 1976, Icarus, 27, 1–12. (Ch. 14)   
Gatewood, G. D., Breakiron, L., Goebel, R. et al., 1980, Icarus, 41, 205–231. (Ch. 14)   
Gatewood, G. D., 1987, Astron. J., 94, 213–224. (Ch. 14)   
Gilbert, F. and Dziewonski, A. M., 1975, Phil. Trans. Roy. Soc. London., A278, 187–269. (Ch. 8)   
Gliese, W., 1963, Veroff. Astron. Rechen-Institut, Heidelberg ¨ , 12. (Ch. 11)   
Goad, C. C., 1980, J. Geophys. Res., 85, 2679–2683. (Ch. 9)   
Googe, W. D., Eichhorn, H. and Lukac, C. F., 1970, Monthly Not. RAS, 150, 35–44. (Ch. 14)   
Grafarend, E. W. and Ardalan, A. A., 1999, J. of Geodesy, 73, 611–623. (Ch. 9)   
Guinot, B., 1979, in Time and the Earth’s Rotation, IAU Symp. 82, D. D. McCarthy and J. D. H. Pilkington (Eds.), D. Reidel Publ. Co., Dordrecht, 7–18. (Ch. 8, 10)   
Guinot, B., 1997, Metrologia, 34, 261–290. (Ch. 5)   
Guseva, I. S., 1987, Proceedings of a Workshop on Refraction Determination, G. Teleki (Ed.) Publication of the Belgrad Observatory, 69–74. (Ch. 6)   
Hagihara,Y., 1970–76, Celestial Mechanics, MIT Press and the Japan Society for the Promotion of Science, 5 volumes. (Ch. 8)   
Hale, A. and Doyle, L.R., 1994, Astrophys. Space Science, 212, 335–342. (Ch. 14)   
Hamilton, Sir W. R., 1866, Elements of Quaternions, Longmans, Green and Co., London. (Ch. 3)   
Hartkopf, W. I., Mason, B. D. and Worley, C. E., 2001a, Astron. J., 122, 3472–3479. (Ch. 12)   
Hartkopf, W. I., Mc Allister, H. A. and Mason, B. D., 2001b, Astron. J., 122, 3480–3481. (Ch. 12)   
Hazard, C., Sutton, J., Argue, A. N. et al., 1971, Nature Phys. Sci., 233, 89–91. (Ch. 7)   
Heiskanen, W. A. and Moritz, H., 1967, Physical Geodesy, Freeman and Co., San Francisco, London. (Ch. 9)   
Hellings, R. W., 1986, Astron. J., 91, 650–659. (Ch. 14)   
Hemenway, P., 1980, Celest. Mech., 22, 89–109. (Ch. 14)   
Herring, T. A., 1996, Private communication. (Ch. 8)   
Herring, T. A., Mathews, P. M. and Buffett, B. A., 2002, J. Geophys. Res., 107, ETG 4-1-12. (Ch. 8)   
Hilton, J. L., 2002, Private communication. (Ch. 8)   
Hofmann-Wallenhof, B., Lichtenegger, H. and Colins, J., 1992, Global Positioning System, Theory and Practice, Springer Verlag, Wien, New-York. (Ch. 2, 10)   
Høg, E., 1997, in Hipparcos Venice’97, B. Batrick (Ed.), ESA Publ. SP-402, July 1997, Noordwijk, 25–30. (Ch. 11)   
Høg, E., Bastian, U., Egret, D. et al., 1992, Astron. & Astrophys., 258, 177–185. (Ch. 11)   
Høg, E., Fabricius, C., Makarov, V. V. et al., 2000a, Astron. & Astrophys., 355, L19–L22. (Ch. 11)   
Høg, E., Fabricius, C., Makarov, V. V., Bastian, U. et al., 2000b, Astron. & Astrophys., 357, 367–386. (Ch. 7, 11)   
IAG, 1980, The Geodetic Reference System 1980, Bulletin Geod ´ esique ´ , 54, 395–405. (Ch. 9)   
IAU, 1992, Proceedings of the XXI-st General Assembly, J. Bergeron (Ed.) IAU Transactions, Kluwer Academic Publishers, Dordrecht, 41–52. (Ch. 7)   
IAU, 1998, Proceedings of the XXIII-rd General Assembly, J. Andersen (Ed.) IAU Transactions, Kluwer Academic Publishers, Dordrecht 39–41. (Ch. 7)   
IAU, 2001, Proceedings of the XXIV-th General Assembly, H. Rickman (Ed.) IAU Transactions, Astro. Soc. of the Pacific, 33–59. (Ch. 7)   
IERS, 1996, IERS Conventions (1996), IERS Technical Note 21, D. D. McCarthy (Ed.), Observatoire de Paris. (Ch. 8)   
IERS, 2003, IERS Conventions 2000, International Earth Rotation Service. (Ch. 9, 10)   
Ilyasov, Y. P., Kopeikin, S. M. and Rodin, A. E., 1998, Astronomy Letters, 24, 228–236. (Ch. 14)   
IUGG, 1992, Bulletin Geod ´ esique ´ , 66, 128–129. (Ch. 9)   
Iyer, B. R. and Will, C. M., 1995, Phys. Rev., D 52, 6882–6893. (Ch. 14)   
Jaech, J. L., 1985, Statistical Analysis of Measurement Errors, An Exxon Monograph, John Wiley & Sons, New York. (Ch. 4)   
James, T. S. and Ivins, E. R., 1997, J. Geophys. Res., 102, 605–633. (Ch. 9)   
Jaranowski, P., 1997, in Mathematics of Gravitation, Part II, Gravitational Wave Detection, A. Krolak (Ed.), Banach Center Publications of Inst. Math., Polish Acad. Sci., 41, 55. (Ch. 14)   
Jaranowski, P. and Schafer, G., 1997, Phys. Rev., D 55, 4712–4722. (Ch. 14)   
Jefferys, W. H., 1963, Astron. J., 68, 111–113. (Ch. 14)   
Jefferys, W. H., 1979, Astron. J., 84, 1775–1777. (Ch. 14)   
Jefferys, W. H., 1987, Astron. J., 93, 755–759. (Ch. 14)   
Johnston, K. J., Fey, A. L., Zacharias, N. et al., 1995, Astron. J., 110, 880–915. (Ch. 7)   
Johnston, K. J. and de Vegt, C., 1999, Annual Rev. Astron. Astrophys., 37, 97–125. (Ch. 7)   
Kammeyer, P., 2000, Celestial Mechanics and Dynamical Astronomy, 77, 241–272. (Ch. 10)   
Kaplan, G. H., Josties, F. J., Angerhofer, P. E. et al., 1982, Astron. J., 87, 570–576. (Ch. 7)   
Kaspi, V. M., Taylor, J. H. and Ryba, M. F., 1994, Astrophys. J., 428, 713–728. (Ch. 14)   
Kinoshita, H., 1977, Celestial Mechanics, 15, 277–326. (Ch. 8)   
Kinoshita, H. and Kozai, H., 1989, Celestial Mechanics, 45, 231–244. (Ch. 9)   
Kinoshita, H. and Souchay, J., 1990, Celest. Mech. and Dyn. Astr., 48, 187–265. (Ch. 8)   
Klioner, S. A., 1993 , Astron. & Astrophys., 279, 273–277. (Ch. 7)   
Koch, D. G., Borucki, W., Webster, L. et al., 1999, in Space telescopes and Instruments V., P. Y. Bely and J. B. Breckinridge (Eds.), Proc. SPIE, 3356, 599–607. (Ch. 14)   
Kopeikin, S. M., 1997, Monthly Not. RAS, 288, 129–137. (Ch. 14)   
Kopeikin, S. M., 1999, Monthly Not. RAS, 305, 563–590. (Ch. 14)   
Kopeikin, S. M., 2001, in Reference Frames and Gravitomagnetism, Proceedings of the Spanish Relativity Meeting 2000, J.-F. Pascual-Sanchez (Ed.), World Science, Singapore. (Ch. 5)   
Kopeikin, S. M. and Gwinn, C. R., 2000, Towards Models and Constants for Sub-Microarcsecond Astrometry, K. J. Johnston, D. D. McCarthy, B. J. Luzum and G. H. Kaplan (Eds.), IAU Colloquium 180, Publ. U.S. Naval Observatory, Washington, 303–307. (Ch. 5)   
Kopeikin, S. M. and Ozenoy, L. M., 1999, Astrophys. J., 523, 771–785. (Ch. 12)   
Kopeikin, S. M. and Sch˝affer G., 1999, Phys. Review, D 60, 124002. (Ch. 5)   
Kopff, A., 1937, Veroff. Astron. Rechen-Institut, Heidelberg ¨ , 54. (Ch. 11)   
Korff, D., 1973, J. of Opt. Soc. of America, 63, 971–980. (Ch. 2)   
Kovalevsky, J., 1967, Introduction to Celestial Mechanics, D. Reidel Publ. Co., Dordrecht. (Ch. 8, 12)   
Kovalevsky, J., 2000, in Towards Models and Constants for Sub-Microarcsecond Astrometry, IAU Colloquium 180, K. J. Johnston, D. D. McCarthy, B. J. Luzum and G. H. Kaplan (Eds.), US Naval Observatory, Washington DC 3–9. (Ch. 7)   
Kovalevsky, J., 2002, Modern Astrometry, second edition, Springer-Verlag, Berlin, Heidelberg. (Ch. 2, 10, 11)   
Kovalevsky, J., 2003, Astron. & Astrophys., 404, 743–747. (Ch. 6)   
Kovalevsky, J., Falin, J.-L., Pieplu, J.-L. et al., 1992, Astron. & Astrophys., 258, 7–17. (Ch. 11)   
Kovalevsky, J., Lindegren, L. and Froeschl´e, M., 2000, in Journees 1999, Syst ´ emes de \` ref´ erence spatio-temporels ´ , M. Soffel and N. Capitaine (Eds.), Paris Observatory, 119–130. (Ch. 2)   
Kovalevsky, J., Lindegren, L., Perryman, M. A. C. et al., 1997, Astron. & Astrophys., 323, 620–633. (Ch. 7, 11)   
Kovalevsky, J. and McCarthy, D., 1998, in Highlights in Astronomy, J. Andersen (Ed.), 11A, 182–186. (Ch. 10)   
Kuimov, K. V., Sorokin, F. D., Kuz’min, A. V. and Barusheva, N. T., 2000, Astronomy Reports, 44, 474–480. (Ch. 14)   
Labeyrie, A., 1970, Astron. & Astrophys., 6, 85–87. (Ch. 2)   
Labeyrie, A., 1975, Astrophys. J. Letters, 196, L71–75. (Ch. 2)   
Labeyrie, A., 1995, Astron. & Astrophys., 298, 544–548. (Ch. 14)   
Lambeck, K., 1980, The Earth’s Variable Rotation: Geophysical Causes and Consequences, Cambridge University Press, Cambridge. (Ch. 10)   
Laskar, J., 1986, Astron. & Astrophys., 157, 59–70. (Ch. 13)   
Lattanzi, M. G. and Bucciarcelli, B., 1991, Astron. & Astrophys., 250, 565–572. (Ch. 14)   
L´eger, A., Rouan, D., Schneider, J. et al., 1999, in Bioastronomy 99: A new Era in Bioastronomy, Kohala Coast Meeting, Hawaii, August 2–6, 1999. (Ch. 14)   
L´ena, P., 1996, Astrophysique, Methodes physiques de l’observation ´ , CNRS Editions, Paris. (Ch. 2)   
Le Provost, C., Genco, M. L., Lyard, F. et al., 1994 J. Geophys. Res., 99, 24777–24797. (Ch. 9)   
Lestrade, J.-F., Jones, D. L., Preston, R. A. et al., 1995, Astron. & Astrophys., 304, 182–188. (Ch. 7)   
Liebelt, P. B., 1967, An Introduction to Optimal Estimation, Addison-Wesley Publ. Co., Reading (Mass). (Ch. 4)   
Lieske, J. H., 1979, Astron. & Astrophys., 73 282–284. (Ch. 8)   
Lieske, J. H., Lederle, T., Fricke, W. and Morando, B., 1977, Astron. & Astrophys., 58, 1–16. (Ch. 8, 11)   
Lindegren, L., Høg, E., van Leeuwen, F. et al., 1992, Astron. & Astrophys., 258, 18–30. (Ch. 11)   
Lindegren, L. and Kovalevsky, J., 1995, Astron. & Astrophys., 304, 189–201. (Ch. 7)   
Luri, X. and Arenou, F., 1997, in Hipparcos Venice’97, B. Batrick (Ed.), ESA Publ., SP-402, 449–452. (Ch. 11)   
Lutz, T. E. and Kelker, D. H., 1973, Publ. Astron. Soc. Pacific, 85, 573–578. (Ch. 11)   
Ma, C., Arias, E. F., Eubanks, T. M. et al., 1998, Astron. J., 116, 516–546. (Ch. 2, 7)   
Ma, C. and Feissel, M., 1997, Definition and Realization of the International Celestial Reference System by VLBI Astrometry of Extragalactic Objects, IERS Technical Note No 23, Observatoire de Paris. (Ch. 7)   
Manchester, R. N. and Taylor, J. H., 1977, Pulsars, Freeman, San Francisco. (Ch. 14)   
Marcy, G. W. and Butler, R. P., 1992, Publ. Astron. Soc. Pacific, 104, 270–277. (Ch. 14)   
Marcy, G. W. and Butler, R. P., 1993, Astron. Soc. of the Pacific Conference Series, 47, 175–182. (Ch. 14)   
Marcy, G. W. and Butler, R. P., 1998, Ann. Rev. Astron. Astrophys., 36, 57–97. (Ch. 14)   
Marcy, G. W. and Butler, R. P., 1999, in The Origin of Stars and Planetary Systems, C. J. Lada and N. D. Kylafis (Eds.), Kluwer Academic Publishers, Dordrecht, 681–708. (Ch. 14)   
Marcy, G. W. and Butler, R. P., 2000, Publ. Astron. Soc. Pacific, 112, 137–140. (Ch. 14)   
Marini, J. W. and Murray, C. W., 1973, Correction of the Laser Range Tracking Data for Atmospheric Refraction at Elevations above $1 0 ^ { \circ }$ , NASA-GSFC document X-591-73-35. (Ch. 6)   
Markowitz, W., Hall, R. G., Essen, L. and Perry, J. V. L., 1958, Phys. Rev. Letters, 1, 105. (Ch. 1)   
Martinez, P. and Klotz, A., 1999, A Practical Guide to CCD Astronomy, Cambridge University Press, Cambridge. (Ch. 2, 14)   
Mason, R. D., Wycoff, G. L., Hartkopf, W. I. et al. 2001, Astron. J., 122, 3466–3471. (Ch. 12)   
Mathews, P. M., Herring, T. A. and Buffett, B. A., 2002, J. Geophys. Res., 107, ETG 3-1-26. (Ch. 8)   
Matsakis, D. N. and Foster, R. S., 1996, in Amazing Light, A Festschrift for Charles Townes, R. Chiao (Ed.), Springer Verlag, Berlin, 445–462. (Ch. 14)   
Matsakis, D. N., Taylor, J. H. and Eubanks, T. M., 1997, Astron. & Astrophys., 326, 924–928. (Ch. 14)   
Mayor, M. and Queloz, D., 1995, Nature, 378 (6555), 355–359. (Ch. 12, 14)   
Mc Allister, H. A., 1996, Sky and Telescope, November 1996, 29–35. (Ch. 12)   
McCarthy, D. D. (Ed.), 1996, IERS Conventions, IERS Technical Note 21, Observatoire de Paris. (Ch. 6, 9, 10)   
McCarthy, D. D. (Ed.), 2003, IERS Conventions, (in press). (Ch. 6, 9, 10)   
McCarthy, D. D. and Babcock, A. K., 1986, Physics of the Earth and Planetary Interiors, 44, 281–292. (Ch. 10)   
McCarthy, D. D. and Luzum, B. J., 2003, Celest. Mech. and Dyn. Astron., 85, 37–49. (Ch. 8)   
McLean, B., Lasker, B. and Lattanzi, M., 1998, AAS Meeting, 192, 55.10. (Ch. 11)   
Melchior, P., 1966, The Earth Tides, Pergamon Press, Oxford, London. (Ch. 9)   
Mendenhall, W., Schaeffer, R. L. and Wackerly, D. D., 1986, Mathematical Statistics and Applications, 3rd edition, Duxbury Press, Boston. (Ch. 4)   
Mignard, F., Froeschl´e, M., Badiali, M. et al., 1992, Astron. & Astrophys., 258, 165–172. (Ch. 12)   
Mitrovica, J. X. and Peltier, W. R., 1993, J. Geophys. Res., 98, 4509–4526. (Ch. 9)   
Moller, O. and Kristensen, L. K., 1976, Trans. IAU., XVI B, 166. (Ch. 14)   
Monet, D. G., 1988, Ann. Review. Astron. Astrophys., 26, 413–440. (Ch. 2, 14)   
Monet, D. G. et al., 1998, USNO-A, US Naval Observatory, Washington D.C. (Ch. 14)   
Morgan, H. R., 1952, Astron. Papers Am. Ephemeris and Naut. Alm., 13, part 3. (Ch. 11)   
Moritz, H., 1980, Advanced Physical Geodesy, Abacus Press, Tunbridge Wells, Kent, UK. (Ch. 9)   
Morrison, J. E., R¨oser, S., Lasker, B. M. et al., 1996, Astron. J., 111, 1405–1410. (Ch. 14)   
Morrison, J. E., R¨oser, S., McLean, B. et al., 2001, Astron. J., 121, 1752–1763. (Ch. 11)   
Morrison, J. E., Smart, R. L. and Taff, L. G., 1998, Monthly Not. RAS, 296, 66–76. (Ch. 14)   
Mould, R. A., 1994, Basic Relativity, Springer-Verlag, New York, Berlin. (Ch. 3, 5)   
Murray, C. A., 1983, Vectorial Astrometry, Adam Hilger, Bristol, England. (Ch. 7)   
Murray, C. A., 1989, Astron. & Astrophys. 218, 325–329. (Ch. 7)   
Murray, C. D. and Dermott, S. F., 1999, Solar System Dynamics, Cambridge University Press, Cambridge, UK. (Ch. 8)   
Nelson, B. and Davis, W. D., 1972, Astrophys. J., 174, 617–628. (Ch. 12)   
Newcomb, S., 1878, Washington Observations for 1875. (Ch. 1)   
Newcomb, S., 1912, Astron. Papers Am. Ephemeris and Naut. Alm., IX, part I. (Ch. 1)   
Nordtvedt, K., 1970, Astrophys. J., 161, 1059–1067. (Ch. 5)   
Ohanian, H. C., 1980, Gravitation and Spacetime, second edition, W.W. Norton & Co., New York. (Ch. 5, 7)   
Owen, W. M. and Yeomans, D. K., 1994, Astron. J. 107, 2295–2298. (Ch. 14)   
Paczy´nski, B., 1996, Ann. Rev. Astron. Astrophys., 34, 419–459. (Ch. 6)   
Peale, S. J., 1997, Icarus, 127, 269–289. (Ch. 14)   
Peters, J., 1907, Veroff. des K ¨ onig. Astron. Rechen-Instituts zu Berlin ¨ , 33. (Ch. 11)   
Petit, G., 2000, in Towards Models and Constants for Sub-microarcsecond Astrometry, IAU Colloquium 180, K. J. Johnston, D. D. McCarthy, B. J. Luzum, and G. H. Kaplan (Eds.), US Naval Observatory, Washington DC, 275–282. (Ch. 14)   
Popper, D. M., 1984, Astron. J., 84, 132–144. (Ch. 12)   
Poveda, A., 1988, Astrophys. Space Science, 143, N1/2, 67–78. (Ch. 12)   
Pulkovo Observatory, 1985, Refraction Tables of Pulkovo Observatory, fifth edition, Pulkovo. (Ch. 6)   
Rawley, L. A., Taylor, J. H. and Davis, M. M., 1988, Astrophys. J., 326, 947–953. (Ch. 14)   
Rindler, W., 1977, Essential relativity, Springer-Verlag, New York, Heidelberg. (Ch. 5)   
Roddier, C. and Roddier, F., 1975, J. Opt. Soc. of America, 65, 664–667. (Ch. 2)   
R¨oser, S., 1999, in Review in Modern Astrometry, R. Schielicke (Ed.), Astronomische Geselschaft, Hamburg, 12, 97–106. (Ch. 2)   
R¨oser, S. and Bastian, U., 1991, PPM Star Catalogue, Spektrum Akademisher Verlag, Heidelberg, I and II. (Ch. 11)   
R¨oser, S. and Bastian, U., 1993, Bulletin d’Information du CDS, Observatoire de Strasbourg, 42, 11–16. (Ch. 11)   
R¨oser, S., Bastian, U. and Kuzmin, A., 1994, Astron. & Astrophys. Suppl., 105, 301–303. (Ch. 11)   
Russell, J. L., Lasker, B. M., McLean, B. J., Sturch, C. R. and Jenkner, H., 1990, Astron. J., 2059–2081. (Ch. 11)   
Ryba, M. F. and Taylor, J. H., 1991a, Astrophys J., 371, 739–748. (Ch. 14)   
Ryba, M. F. and Taylor, J. H., 1991b, Astrophys J., 380, 557–563. (Ch. 14)   
Safizadeh, N., Dalal, N. and Griest, K., 1999, Astrophys. J., 522, 512–517. (Ch. 14)   
SAO, 1966, Star Catalog positions and proper motions of 258 997 stars for the epoch and equinox of 1950.0, Publication of the Smithsonian Institution of Washington, n◦ 4562. (Ch. 11)   
Schneider, P., Ehlers, J. and Falco, E. E., 1992, Gravitational Lensing, Springer Verlag, Berlin. (Ch. 6)   
Seidelmann, P. K., 1982, Celest. Mech., 27, 79–106. (Ch. 8, 10)   
Seidelmann, P. K., 1991, Advan. Space Res., 11–2, 103–111. (Ch. 2)   
Seidelmann, P. K., (Ed.), 1992, Explanatory Supplement to the Astronomical Almanac, University Science Books, Mill Valley, California. (Ch. 6, 8, 9, 10, 13)   
Seidelmann, P. K., Abalakin, V. K., Bursa, M. et al., 2002, Celest. Mech., 82, 83–110. (Ch. 13)   
Seidelmann, P. K. and Kovalevsky, J., 2002, Astron. & Astrophys., 392, 341–351. (Ch. 8, 10)   
Serkowski, K., 1976, Icarus, 27, 13–24. (Ch. 14)   
Shaffer, D. B. and Marscher, A. P., 1987, in Superluminal radio-sources, J.-A. Zensus and T. J. Pearson (Eds.), Cambridge University Press, Cambridge, 67–71. (Ch. 7)   
Shao, M., Colavita, M. M., Hines, B. E. et al., 1988, Astron. & Astrophys., 193, 357–371. (Ch. 2)   
Silvey, S. D., 1991, Statistical Inference, Chapman and Hall, London, New York. (Ch. 4)   
Simon, J.-L., Bretagnon, P., Chapront, J. et al., 1994, Astron. & Astrophys., 282, 663–683. (Ch. 8)   
Simon, J.-L., Chapront-Touz´e, M., Morando, B. and Thuillot, W., 1996, Introduction aux eph ´ em´ erides astronomiques ´ , Editions de Physique, Paris. (Ch. 6)   
Skrutskie, M. F., 2001, AAS Meeting, 198, 33.01. (Ch. 11)   
Smith, E. K. Jr and Weintraub, S., 1953, Proceedings IRE, 41, 1035–1037. (Ch. 6)   
Smith, H., 1987, Astron. & Astrophys., 171, 336–341. (Ch. 11)   
Smith, H. Jr and Eichhorn, H., 1996, Monthly Not. RAS, 281, 211–218. (Ch. 11)   
S¨oderhjelm, S., Evans, D. W., van Leeuwen, F. and Lindegren, L., 1992, Astron. & Astrophys., 258, 157–164. (Ch. 12)   
Soffel, M. H., 1989, Relativity in Astrometry, Celestial Mechanics and Geodesy, A & A Library, Springer-Verlag, Berlin, New York. (Ch. 5, 6)   
Soffel, M. H., 2000, Towards Models and Constants for Sub-Microarcsecond Astrometry, K. J. Johnston, D. D. McCarthy, B. J. Luzum and G. H. Kaplan (Eds.), IAU Colloquium 180, Publ. U.S. Naval Observatory, Washington DC, 283–292. (Ch. 5, 7, 8)   
Souchay, J., Loysel, B., Kinoshita, H. and Folgeira, M., 1999, Astron. & Astroph. Supp. Series, 135, 111–131. (Ch. 8)   
Spencer Jones, H., 1939, Monthly Not. R.A.S., 99, 541. (Ch. 1, 10)   
Standish, E .M., Newhall, X. X., Williams, J. G. and Folkner, W. F., 1995, JPL Planetary and Lunar Ephemerides, JPL IOM 314, 10–127. (Ch. 7)   
Standish, E. M., 1998, JPL Interoffice Memorandum, IOM 312, F-98-048. (Ch. 8)   
Stark, H. and Woods, J. W., 1986, Probability, Random Processes, and Estimation Theory for Engineers, Prentice-Hall, Englewood Cliffs, New Jersey. (Ch. 4)   
Stephenson, F. R. and Lieske, J. H., 1988, Astron. & Astrophys., 200, 218–224. (Ch. 10)   
Stephenson, F. R. and Morrison, L. V., 1984, Phil. Trans. R. Soc. London, A313, 47–70. (Ch. 10)   
Stinebring, D. R., 1982, PhD thesis, Cornell University, Ithaca, N.Y. (Ch. 14)   
Stone, R. C. and Dahn, C. C., 1995, in Astronomical and Astrophysical Objectives of Sub-milliarcsecond Astrometry, IAU Symp. 166, E. Høg and P. K.Seidelmann (Eds.), Kluwer, Dordrecht, 3–8. (Ch. 7)   
Stoyko, N., 1937, Comptes-rendus de l’Academie des Sciences ´ , 250, 79–82. (Ch. 10)   
Taff, L. G., 1988, Astron. J., 96, 409–411. (Ch. 14)   
Taff, L. G., Lattanzi, M. G. and Bucciarelli, B., 1990a, Astrophys. J., 358, 359–369. (Ch. 14)   
Taff, L. G., Bucciarelli, B. and Lattanzi, M. G., 1990b, Astrophys. J., 361, 667–672. (Ch. 14)   
Taylor, G. E., 1955, J. British Astron. Ass., 65, 84. (Ch. 13)   
Taylor, J. H., 1991, Proc. IEEE, 79, 1054–1062. (Ch. 14)   
Taylor, J. H., 1992, Phil. Trans. R. Soc. London, B 341, 117–134. (Ch. 14)   
Taylor, J. H., 1993, Classical Quantum Gravity, 10, S135. (Ch. 12)   
Taylor, J. H. and Weisberg, J. M., 1989, Astrophys. J., 345, 434–450. (Ch. 5, 12, 14)   
Thomasson, P., 1986, Quarterly Jour. RAS, 27, 413–431. (Ch. 2)   
Thompson, A. R., Clark, B. G., Wade, C. M. and Napier, P. J., 1980, Astrophys. J. Supp., 44, 151–167. (Ch. 2)   
Thompson, A. R., Moran, J. M. and Swenson, G. W. Jr, 1986, Interferometry and synthesis in Radio Astronomy, John Wiley and Sons, New York. (Ch. 14)   
Triebes, K., Gilliam, L., Hilby, T. et al., 2000, in UV, Optical, and IR Space Telescopes and Instruments, Proc. SPIE 4013, 482–492. (Ch. 14)   
Turon, C., Cr´ez´e, M., Egret, D. et al., 1992a, The Hipparcos Input Catalogue, European Space Agency Publ., SP-1136, March 1992, 7 volumes (Ch. 2, 11)   
Turon, C., G´omez, A., Crifo, F. et al., 1992b, Astron. & Astrophys., 258, 74–81. (Ch. 11)   
Urban, S. E., Corbin, T. E. and Wycoff, G. L., 1998, Astron. J., 115, 2161–2166. (Ch. 11)   
Urban, S. E. and Corbin, T. E., 1998, Personnal communication and distributed CD-roms with the catalog. (Ch. 11)   
Urban, S. E., Corbin, T. E., Wycoff, G. L. and Mason, B. D., 2000, in Towards Models and Constants for Sub-Microarcsecond Astrometry, IAU Colloquium 180, K. J. Johnston, D. D. McCarthy, B. J. Luzum and G. H. Kaplan (Eds.), US Naval Observatory, Washington DC, 97–103. (Ch. 7)   
Urban, S. E., Seidelmann, P. K., Germain, M. et al., 2000, in Journees 1999, Syst ´ emes de \` ref´ erence spatio-temporels ´ , M. Soffel and N. Capitaine (Eds.), Paris Observatory, 131–135. (Ch. 2)   
Van Altena, W. F., 1983, Ann. Rev. Astron. Astrophys., 21, 131–164. (Ch. 14)   
van Dam, T. M. and Wahr, J. M., 1987, J. Geophys. Res., 92B, 1281–1286. (Ch. 9)   
van Dam, T. M. and Herring, T. A., 1994, J. Geophys. Res., 99B, 4505–4517. (Ch. 9)   
Van de Kamp, P., 1967, Principles of Astrometry, W. H. Freeman & Co., San Francisco. (Ch. 12)   
Vanivcek, P. and Krakiwsky, E., 1982, Geodesy: the concepts, North Holland Publ. Co., Amsterdam. (Ch. 9)   
Van Leeuwen, F., 1997, Space Sc. Rev., 81, 201–409. (Ch. 2)   
Vondrak, J. and Ron, C., 2000, in Towards Models and Constants for Sub-microarcsecond Astrometry, IAU Colloquium 180, K. J. Johnston, D. D. McCarthy, B. J. Luzum, and G. H. Kaplan (Eds.), U.S. Naval Observatory, Washington D.C., 248–253. (Ch. 10)   
Wahr, J. M., 1981, Geophys. J. R. Astron. Soc., 64, 705–727. (Ch. 8, 9)   
Wahr, J. M., 1985, J. Geophys. Res., 90B, 9363–9368. (Ch. 9)   
Walter, H. G. and Sovers, O. J., 2000, Astrometry of Fundamental Catalogues, Springer Verlag, Berlin, Heidelberg (Ch. 2, 10)   
Wertz, J., 1978, Spacecraft Attitude Determination and Control, Reidel Publ. Co., Dordrecht, Boston. (Ch. 3) Will, C. M., 1974, in Experimental Gravitation, B. Bertotti, (Ed.), Academic Press, New York, 1–110. (Ch. 8) Will, C. M., 1981, Theory and experiment in gravitational physics, Cambridge University Press, Cambridge. (Ch. 5, 6) Will. C. M. and Nordvedt, K., 1972, Astrophys. J., 177, 757–774. (Ch. 14) Wolszczan, A. and Frail, D. A., 1992, Nature, 355, 145–147. (Ch. 14) Woolard, E. W. and Clemence, G. M., 1966, Spherical Astronomy, Academic Press, New York. (Ch. 6, 11) Worley, C. E. and Douglass, G. G., 1997, Astron. & Astrophys. Suppl. Series, 125, 523. (Ch. 12) Zacharias, N., 1996, Proc. Astron. Soc. Pacific, 108, 1135–1138. (Ch. 14) Zacharias, N., 2001, Astrometry: telescopes and techniques, Encyclopedia of Astronomy and Astrophysics, Nature Publishing Group, Institute of Physics Publishing,   
111–120. (Ch. 14) Zacharias, N., de Vegt, C. and Murray, C. A., 1997, in Proc. ESA Symp. Hipparcos-Venice   
1997, B. Batrick (Ed.), ESA SP-402, 85–90. (Ch. 7) Zacharias, N., Urban, S. E., Zacharias, M. I. et al., 2000, Astron. J., 120, 2131–2147. (Ch. 11) Zarrouati, O., 1987, Trajectoires Spatiales, Cepadues-Editions, Toulouse, France. (Ch. 9) Zombeck, M. V., 1990, Handbook of Space Astronomy and Astrophysics, second edition, Cambridge University Press, Cambridge, 65. (Ch. 11)

Index

aberration 121, 135–42, 356, 371 annual 135, 138–40, 371 constant of 140, 363, 368 differential planetary 143–4 diurnal 135, 141–2, 371 elliptic 141 orbital 135, 141–2, 371 planetary 135, 142–4, 356, 371 relativistic 137–8 secular 135–6, 371 stellar 3, 135–7, 143, 371   
acceleration gravitational 106 in relativity 103 perspective 250 rotational inertial 106   
accuracy 2, 74, 82, 371   
AC 2000 271   
ACT Reference Catalog 271   
adaptive optics 371   
AGK3-R 264   
Airy diffraction disk 22   
Algol-type binary 298   
altitude 66, 201–2, 206, 371   
apparent geocentric position 354   
apparent orbit 281–2, 287–9   
apparent place 372   
apparent solar time 6   
Astrographic Catalog 4, 263–4, 271   
Astrographic Catalog Reference Stars 266   
Astrolabes 218   
astrometric position 328, 357, 359, 372   
astrometric techniques 5–6, 11–12, 221, 347   
Astrometry 1–2 History of 2–4 space 221–3   
astronomical constants 363–4   
astronomical phenomena 307–9   
astronomical unit (a.u.) 360, 363, 372   
atmosphere 122–3   
atmospheric angular momentum 218   
bandwidth 15   
barycenter 372   
Barycentric Celestial Reference Frame 166, 372   
Barycentric Celestial Reference System (BCRS) 108–9, 116, 158–9, 164, 171, 372   
Barycentric Coordinate Time (TCB) 7, 68, 116–17, 158, 165, 340, 354, 372   
Barycentric Ephemeris Time 372   
Barycentric Dynamical Time (TDB) 8, 68, 372   
barycentric positions 355   
Besselian elements 316   
binaries see double stars   
Bradley, James 3, 176   
brilliancy 313   
brown dwarfs 301   
calendar 308, 313, 319–21   
Cape Photographic Catalogue 265   
Carte du ciel 4, 263   
catalogs absolute 261 compilation 265–6 double stars 305–7 fundamental 261–3 observational 261 reference 263–5 relative 261   
catalog equinox 308, 373   
CCD 5, 11, 164, 325–7, 357   
Celestial Ephemeris Origin (CEO) 171, 175–6, 202, 223–7, 230, 236–7, 308, 324, 357, 373   
Celestial Ephemeris Pole 183, 235, 324, 373   
Celestial Intermediate Pole (CIP) 175–6, 185, 200, 202, 224, 228–9, 236, 324, 373   
Celestial Intermediate Frame 175, 373   
Celestial Intermediate Origin (CIO) 175, 373   
celestial pole 177, 200, 373   
celestial pole offsets 184–6   
celestial sphere 373   
center of figure   
center of light 373   
central fringe 15   
central limit theorem 78   
Centre de donn´ees stellaires (CDS) 305   
centrifugal potential 197   
cesium fountain clock 23   
CHARA 20, 306   
charge transfer efficiency (CTE) 325   
chi-square test 86, 88   
chromatic effect 127, 130   
COAST 19   
coherence length 14–15   
collimation 373   
conjunction 314   
Conventional Terrestrial Reference System (CTRS) 188   
coordinate time 100–1, 107, 114–15, 154, 340–1, 373   
Coordinated Universal Time (UTC) 7, 68, 234, 374   
coordinates astronomical 200, 201, 240, 251–53, 372 cartesian 41, 49 cylindrical 41 differential 61–2 ecliptic 167–8 equatorial 167, 203, 204, 240 galactic 163, 168–70, 376 geocentric 65, 193–5, 200, 205–6, 368, 376 geodetic 65, 193–5, 200, 204–5, 377 geographical 200 horizontal 203 harmonic 110–11 reference 64–8 space 63, 357 space fixed 158, 171 space-time 111, 118 spherical 41 standard 62–4 systems 49–50, 59–61 terrestrial 65, 187, 192–3, 199 topocentric 66, 201–3, 205, 384   
Coriolis effect 221   
correlation coefficients 71, 75, 79, 254, 374   
correlator, Mark III 25   
covariance 75–7, 86, 254, 374   
coverage factor 78, 79   
cross product 42   
data reduction 71–4, 118

datums 187, 374   
declination 66, 202, 240, 374, 376–7, 382   
defect of illumination 374   
deflection of the vertical 66, 200–1, 204, 210, 374   
degree of freedom 80–1, 87–8   
delay lines 19   
delta T 374   
delta UT1 374   
density function 78   
diurnal motion 274   
DIVA 35   
Doppler effect 248, 302, 346

DORIS 189   
dot product 41   
double stars 18, 88, 250, 269, 275 apparent orbit 281–2, 287–9 astrometric 289–91, 301–2, 347–9 catalogs 305–7 eclipsing 297–300, 306, 349–50 observation 285–6, 290, 292 orbital elements 282–5, 291–2, 294–6 spectroscopic 292–6, 346–7   
dynamical equinox 374   
dynamical form factor 196   
dynamical time 374   
Earth angular velocity 368 elasticity 213 equatorial radius 364, 368 flattening factor 364, 368 form factor 363, 368 gravitational field 195–7 orbit 368 orientation 8, 217–21, 228–9, 374 potential models 197, 216, 374 Rotation Angle 176, 230, 375, 384   
eccentric anomaly 280   
eccentricity 278   
eclipse 314–15, 375   
ecliptic 171, 174, 176, 178–80, 182, 375 longitude, latitude 168, 375   
Einstein circle 150–3, 350, 375   
Einstein distance 151–2, 375   
Einstein Time 153   
elastic deformation 220   
elements, orbital 282   
ellipse 278   
ellipsoid 187   
elongations 314   
energy momentum tensor 53   
ephemerides 164, 172–3   
ephemeris hour angle 375   
ephemeris longitude 375   
ephemeris meridian 375   
Ephemeris Time (ET) 7, 68, 234, 375   
ephemeris transit 375   
epoch 375   
epoch transformation 251–3   
equation of the equinoxes 176, 375   
equation of time 231–2, 375   
equations of condition 73, 83   
equator 171, 174, 178–80, 202, 217, 375   
equinox 164, 171, 174, 176, 223, 324, 354, 357, 375 dynamical 171   
equivalence principle 103, 106   
errors random 74 systematic 74, 81–2, 88   
Euclidian space 94, 106   
Euler angles 59   
Euler symmetric parameters 54–7

extragalactic reference frame 68   
extrasolar planets 301–2, 345–51   
FAME 35   
fiducial points 174–6   
fine guidance sensors 32   
fringe visibility 18   
FK5 162–4, 262   
flux 255, 256   
free core nutation (FCN) 177, 184–5, 220, 228, 376

GAIA 36–7   
galactic center 168   
galactic longitude 168   
galactic plane 69, 168   
galactic pole 168   
galactic rotation 262   
Gaussian probability density function 78–80, 89   
Gaussian gravitational constant 275, 363–4, 376   
Gauss–Markov theorem 84–5   
geocenter 215–16, 376   
geocentric coordinates 65, 193, 200, 205, 368, 376 latitude 65 longitude 65   
Geocentric Celestial Reference Frame (GCRF) 166, 376   
Geocentric Celestial Reference System (GCRS) 108–9, 115–16, 158–9, 164, 171, 184–5, 188, 224, 354, 376   
Geocentric Coordinate Time (TCG) 7, 68, 115, 117, 158–9, 165, 188, 192, 354, 376   
Geocentric True Reference Frame (GTRF) 376   
geodesic 104, 108, 112, 154, 164, 377   
geodesic precession and nutation 119, 121, 164–6, 177–8, 181, 184, 377   
geodetic coordinates 65, 193, 200, 204–5, 377 height 65, 193–4 latitude 65, 193–4, 200, 368 longitude 65, 200, 368 reference systems 187   
geoid 106, 115–16, 187, 197–8, 208, 368, 377   
geometric position 377   
geophysical model 183   
GI2T 20   
Global Positioning System (GPS) 23–4, 189, 218, 222   
global solutions 338   
global tectonics 188   
gnomonic projection 72, 328, 359, 377   
gnomonic transformations 62   
goodness of fit 87–8   
gradiant 45   
gravimetry 198   
gravitational constant 173, 195–6, 206, 364, 368 heliocentric 364   
gravitational field Earth 195–8, 216, 368 Moon 366 planets 366   
gravitational lens 150, 152–4, 377

gravitational potential 195, 340   
gravitational waves 119   
gravity, local 197–9, 208   
Greenwich Apparent Sidereal Time (GAST) 176, 203   
Greenwich Mean Sidereal Time (GMST) 175–6, 233,   
235, 324   
Greenwich meridian 65, 189   
Greenwich sidereal date (GSD) 377   
Greenwich sidereal day number 377   
Greenwich Sidereal Time 231, 235, 324, 354, 377   
Gregorian calendar 308   
Guide Star Catalog 264, 272, 337

Harmonics tesseral 105, 196 zonal 105, 196, 215–16   
height 377   
heliocentric 377   
Hipparchus 2, 176   
Hipparcos 5, 8, 29–32, 88, 158, 162–3, 285–6, 305, 338 Catalogue 245, 259, 267–9, 358–9   
horizon 66, 201, 377   
hour angle 66–8, 377   
hour circle 66–7, 377   
Hubble Space Telescope 32–3   
hyperbola 278   
illumination 14   
improved classical system 175–6, 324   
inclination 283, 378   
inertial frame 94   
infrared detectors 12   
interference fringes 14, 17–18   
interferometers 18–20   
interferometric double stars 306   
interferometry 5, 12–15, 378 Fizeau 21–2, 376 Michelson 16, 380 optical 18 space 34 speckle 22, 305 stellar 16–17   
intermediate axes 166   
intermediate reference system 175–6, 223   
International Atomic Time (TAI) 7, 23–4, 68, 116, 234, 378, 384   
International Celestial Reference Frame (ICRF) 8, 26–7, 65, 69, 159–62, 164–6, 171, 174–5, 186, 234, 267, 323, 358, 378   
International Celestial Reference System (ICRS) 157–8, 166, 168, 171, 267, 378   
International Earth Rotation Service (IERS) 26, 158, 166, 175, 177, 189, 219, 237   
International Hipparcos Reference Frame 162–3   
International meridian 65, 189   
International Reference Star Catalog 265   
International Terrestrial Reference Frame (ITRF) 27, 65, 189–93, 228, 234, 378   
International Terrestrial Reference System (ITRS) 166, 175, 188–9, 190, 223–4, 378

invariable plane 174, 378   
ionosphere 131   
IOTA 20   
irradiation 309   
ISI 20   
isoplanatic patch 17, 378   
Jacobian 77, 254   
Julian date (JD) 378   
Julian date, modified (MJD) 378   
Julian day number 378   
Julian year 308, 378   
Kepler’s equation 279–81   
Kepler’s laws 278–9   
KI 21

Laplace formula 124–7   
laser ranging 27–8, 155, 164, 189, 218, 222   
latitude, celestial 200, 378   
latitude, terrestrial 199, 379   
LBT 21   
leap second 234, 379   
least squares 73, 82, 84–6, 89 weighted 84–5   
length of day (LOD) 217–18, 220   
level of confidence 74   
librations 309   
Lick Northern Proper Motion Program 265   
light bending 119, 121 deflection 143–4, 147–54, 355–6, 374 paths 112–15, 121, 144–7, 155 retardation 154–5 time delays 119   
light-time 121, 143, 205, 355, 364, 368, 379   
light-year 379   
limb darkening 18, 300, 379   
linearization 73, 82, 83, 88–9   
loading atmospheric 213–14 ocean 211–13   
local hour angle 66, 202, 229   
local sidereal time 202, 229, 379   
local standard of rest 135   
longitude, celestial 200, 379   
longitude, terrestrial 199, 379   
longitude of periastron 283   
Lorentz transformation 97–8, 118, 158, 171, 3   
Love Numbers 209–11, 220, 379   
luminosity class 258, 260   
lunation 308   
MACHOS 154   
magnitudes 254–7, 260, 313, 379   
main sequence 259   
Martini and Murray formula 130   
masses Earth 368 in relativity 102 minor planets 365

Moon 368 planetary 365 satellites 365 solar 354, 368 stars 302–4 matrices 46–8 mean anomaly 280 mean equator and equinox 379 mean flattening 196 mean motion 279 mean place 379 mean sidereal time 229 mean solar time 231 mean Sun 380 meridian 380 Metonic cycle 312 metric 100, 107, 110, 112–13, 158, 171, 380 general relativity 106–8, 340 special relativity 99–100 microlensing 350 month 310 moonrise, moonset 310–12 Moon mass 364 mean motion 221 orbit 369 physical 366, 369 moving celestial reference frame 380 multiple star systems 4, 275, 300–1 mutual events 318

N30 263   
nadir 280   
Newtonian mechanics 94–5, 275–6   
node 282, 380   
noise Gaussian 344 red 344 white 344   
non-rigid Earth 218   
non-rotating origin 223–4, 227–8   
nutation 3, 174–7, 183–4, 228, 356, 380   
obliquity 167, 177–8, 181–2, 364, 368, 380   
occultation 315–17, 380   
optical path 13   
opposition 314, 380   
orbit 380   
orbital elements Earth 368 Moon 369 planets 366   
orthogonal 48–9   
overlapping plate solutions 329–38   
parabola 278   
paradox of twins 101   
parallax 3, 121–2, 131, 166–8, 239, 241–5, 358, 360, 380 annual 132, 241, 381 diurnal 132, 134–5, 205–6, 381 horizontal 381 orbital 132, 134–5, 381 solar 364, 368 stellar 3, 133–4, 381   
parametrized post Newtonian (PPN) 110, 173   
parsec 134, 361, 381   
periastron 280   
penumbra 315   
perihelion advance of 118   
period 308–9, 381   
permittivity, constant 131   
perspective acceleration 250   
perturbations 381   
phases 312–13, 381   
phase angle 313, 381   
phase coefficient 313, 381   
photometric binaries 297   
photometric technique 349   
photometry 270, 381   
physical ephemerides 318–19   
planetary radars 28   
planetocentric coordinates 318   
planetographic coordinates 319   
planets 365–6   
point spread function (psf) 327   
Poisson distribution 89–90   
Polar axis 179   
polar motion 3, 175, 210, 217–18, 223–4, 228–9, 235, 381   
pole tide 220   
Positions and Proper Motions Catalogue (PPM) 266   
post-glacial rebound 216, 220   
potential Earth 195–9, 216 in relativity 104–6, 115, 158 tidal 206–9   
precession 2, 174, 176–8, 182, 262, 356, 381 angles 179–83 constant of 177–8, 185, 364 general 177–9, 181, 367 lunisolar 176, 178, 367 matrix 180 planetary 176, 178, 367   
precession–nutation model 166, 175–7, 184–6, 217, 223–4, 233, 235–7, 324, 357, 382   
precision 2, 74, 82, 382   
probability density function (pdf) 78–9, 83, 241–2, 244, 382 chi-square 80, 86–87 gamma 80 Gaussian 78–80, 89, 245, 247 Lutz and Kelker 242–5 uniform 81   
proper motion 3, 165–7, 169, 174, 239–41, 246, 249–53, 358, 382   
proper time 100–2, 107, 154, 340, 382   
PTI 20   
Pulkovo Tables 126, 128   
pulsars 302, 345, 382 binary 302

millisecond 328–345   
spin equation 339   
timing 29, 108, 112, 119, 341

quaternions 54–7   
radar altimetry 198 planetary 28   
radial velocity 166, 239, 246–50, 292–4, 346, 38   
radii Moon 369 planetary 365 Sun 367   
random quantities 75–8   
red shifts 119   
reduction of observations 71–2, 327–9 relativistic 118   
reference frame 8, 112, 157, 174–76, 382 dynamical 163, 171, 173, 260, 262 extragalactic 68–9 galactic 136 planes 174 ties 108–109, 163–5, 234–7   
reference system 157, 235–6, 323–4, 382   
refraction atmospheric 121–9, 382 index of 12, 122–5 in distance 129–30 planar layers 122 radio waves 130–1 spherical model 123–4   
relativity 93–4 Galilean 94 general 94, 103–4, 106–8, 118–19 special 94, 99–103   
residuals 87   
right ascension 240, 376–7, 382   
rigid Earth 183–4   
robust estimations 90–1   
Roche limit 298, 382   
rotating axes 44–5   
rotation matrices 48 quaternions 56–7   
rotation of the Earth 6, 219–23, 315, 367

Saros 308, 312, 369   
satellite missions, astrometric 29–37   
Schmidt telescopes 4, 30, 327, 337   
Schwarzschild space-time 109, 113, 164   
second, Syst\`eme International (SI) 7, 68, 115, 234,   
382   
secular deceleration 217   
seeing 22, 383   
selenocentric 383   
semidiameter 383   
semimajor axis 278   
Shida numbers 209–11, 240, 379, 383   
sidereal day 383   
sidereal hour angle 383