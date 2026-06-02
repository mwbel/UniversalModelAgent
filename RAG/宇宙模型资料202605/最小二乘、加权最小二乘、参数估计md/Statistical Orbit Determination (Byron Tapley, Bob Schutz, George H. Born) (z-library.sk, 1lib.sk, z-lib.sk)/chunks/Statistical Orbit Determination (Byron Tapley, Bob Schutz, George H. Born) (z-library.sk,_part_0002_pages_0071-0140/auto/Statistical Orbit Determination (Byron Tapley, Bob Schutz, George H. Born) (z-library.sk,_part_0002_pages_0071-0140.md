include the Coriolis, centripetal, tangential, and relative acceleration terms. Alternatively, expressing ¨r in the nonrotating expression is simpler. Since the gradient of $U$ given by Eq. (2.3.18) provides force components in spherical coordinates, a coordinate transformation matrix $T _ { r \phi \lambda } ^ { x y z }$ is required to rotate the $\left( \mathbf { u } _ { r } , \mathbf { u } _ { \phi } , \mathbf { u } _ { \lambda } \right)$ components of $\mathbf { f }$ into $( x , y , z )$ components, as follows:

$$
T _ { r \phi \lambda } ^ { x y z } = \left[ \begin{array} { c c c } { \cos \phi \cos \lambda } & { - \sin \phi \cos \lambda } & { - \sin \lambda } \\ { \cos \phi \sin \lambda } & { - \sin \phi \sin \lambda } & { \cos \lambda } \\ { \sin \phi } & { \cos \phi } & { 0 } \end{array} \right]
$$

where the latitude $\phi$ and longitude $\lambda$ are related to $( x , y , z )$ through Eq. (2.2.36). In addition, if $\ddot { \mathbf { r } }$ is expressed in the nonrotating system, then a further transformation, $T _ { x y z } ^ { X Y Z }$ , is needed between the rotating axes $( x , y , z )$ and the nonrotating axes $( X , Y , Z )$ . The details of this transformation are dependent on variations in both the magnitude and direction of the angular velocity vector of the rotating axes. For simplicity in this discussion, if the $( x , y , z )$ axes rotate about the $Z$ axis and the $z$ axis is coincident with the $Z$ axis, it follows that the transformation is

$$
T _ { x y z } ^ { X Y Z } = \left[ \begin{array} { c c c } { \cos \alpha } & { - \sin \alpha } & { 0 } \\ { \sin \alpha } & { \cos \alpha } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right]
$$

where $\alpha$ represents the angle of rotation.

If the $( x , y , z )$ axes are fix ed in the Earth, with the $x$ axis coinciding with the intersection between the Greenwich meridian and the equator and the $X$ axis coincides with the vernal equinox, the angle $\alpha$ corresponds to $\alpha _ { G }$ , described in Section 2.2.3. Thus, the contribution of the mass distribution of the central body to the perturbing force in Eq. (2.3.3) is expressed by

$$
{ \bf f } _ { N S } = T _ { x y z } ^ { X Y Z } T _ { r \phi \lambda } ^ { x y z } \nabla U ^ { \prime }
$$

assuming $\mathbf { r }$ is expressed in the nonrotating system $( X , Y , Z )$ in the equations of motion. Hence, Eq. (2.3.17) becomes

$$
\ddot { \mathbf { r } } = - \frac { \mu } { r ^ { 3 } } \mathbf { r } + T _ { x y z } ^ { X Y Z } \ : T _ { r \phi \lambda } ^ { x y z } \ : \nabla U ^ { \prime } .
$$

The alternate expression for the equations of motion use the rotating system to express $\mathbf { r }$ . In this case,

$$
\begin{array} { c c l } { \ddot { \mathbf { r } } _ { \mathrm { R e l } } } & { = } & { - \boldsymbol { \omega } _ { c } \times \left( \boldsymbol { \omega } _ { c } \times \mathbf { r } \right) - 2 \boldsymbol { \omega } _ { c } \times \dot { \mathbf { r } } _ { \mathrm { R e l } } - \dot { \boldsymbol { \omega } } _ { c } \times \mathbf { r } } \\ & & { - \displaystyle \frac { \mu \mathbf { r } } { r ^ { 3 } } + T _ { r \phi \lambda } ^ { x y z } \nabla U ^ { \prime } } \end{array}
$$

where $\omega _ { c }$ represents the angular velocity vector of $( x , y , z )$ with respect to $( X , Y$ , $Z$ ), the position vector $\mathbf { r }$ is expressed in terms of $( x , y , z )$ components, and “Rel” means that the time derivative does not include derivatives of the unit vectors.

If $\omega _ { c }$ is constant such that $\omega _ { c } = \omega _ { c } \mathbf { u } _ { z }$ , it can be shown that an energy-like integral exists, known as the Jacobi Integral:

$$
\frac { v ^ { 2 } } { 2 } - \frac { \omega _ { c } ^ { 2 } ( x ^ { 2 } + y ^ { 2 } ) } { 2 } - \frac { \mu } { r } - U ^ { \prime } = K
$$

where $K$ is the Jacobi Constant and $v$ is the speed of the satellite with respect to the rotating system $( x , y , z )$ . Another form of this integral is given by Bond and Allman (1996), which is suitable for the nonrotating formulation:

$$
\frac { V ^ { 2 } } { 2 } - { \omega _ { c } } \cdot { \bf h } - \frac { \mu } { r } - U ^ { \prime } = K
$$

where $V$ is the ECI speed, $\omega _ { c }$ and $\mathbf { h }$ are also expressed in the ECI coordinate system. The relation between ECI velocity $( \mathbf { V } _ { \mathbf { \Omega } }$ ) and ECF velocity $( \mathbf { v } )$ i s

$$
\mathbf { V } = \mathbf { v } + \omega _ { c } \times \mathbf { r }
$$

For the same $U ^ { \prime }$ and the same assumptions about reference frames, the various differential equations (Eqs. (2.3.22), (2.3.23)) and the equations in Appendix C for orbit elements give equivalent results. In practice, the solution method applied to the respective equations may produce a different error spectrum. The nonrotating coordinate system and the equations represented by Eq. (2.3.22) are widely used in precision orbit determination software.

# 2.3.4 GRAVITATIONAL PERTURBATIONS: OBLATENESS AND OTHER EFFECTS

Consider an ellipsoid of revolution with constant mass density. It is apparent that $C _ { \ell m }$ and $S _ { \ell m }$ will be zero for all nonzero $m$ because there is no longitudinal dependency of the mass distribution. Furthermore, it can readily be shown that because of symmetry with respect to the equator there will be no odd-degree zonal harmonics. Hence, the gravitational potential of such a body will be represented by only the even-degree zonal harmonics. Furthermore, for a body like the Earth, more than $9 5 \%$ of the gravitational force (other than $\mu / r ^ { 2 }$ ) will be derived from the degree-2 term, $J _ { 2 }$ .

Assuming that the entire gravitational potential for the ellipsoid of revolution can be represented by the $J _ { 2 }$ term, it follows from Eq. (2.3.12) that

$$
U ^ { \prime } = - \frac { \mu } { r } \left( \frac { a _ { e } } { r } \right) ^ { 2 } J _ { 2 } P _ { 2 } ( \sin \phi )
$$

Table 2.3.2: Node Motion as a Function of i $\left( J _ { 2 } > 0 \right)$ )   

<table><tr><td>Inclination</td><td>Ss</td><td>Terminology</td></tr><tr><td>Posigrade</td><td>Negative</td><td>Regression of Nodes</td></tr><tr><td>Retrograde</td><td>Positive</td><td>Progression of Nodes</td></tr><tr><td>Polar</td><td>Zero</td><td></td></tr></table>

where $\mu ^ { * } = \mu$ and $P _ { 2 } ( \sin \phi ) = ( 3 \sin ^ { 2 } \phi - 1 ) / 2$ .

Noting that $\sin \phi = \sin i \sin ( \omega + f )$ from spherical trigonometry, it can be shown that the gravitational potential can be expressed in terms of orbit elements with the help of the expansions in eccentricity given in Eq. (2.2.26). By ignoring terms of order $e$ and higher, it follows that

$$
\begin{array} { l l l } { { U ^ { \prime } } } & { { = } } & { { \displaystyle - \frac { \mu } { a } \left( \frac { a _ { e } } { a } \right) ^ { 2 } J _ { 2 } \{ 3 / 4 \sin ^ { 2 } i [ 1 - \cos ( 2 \omega + 2 M ) ] - 1 / 2 \} } } \\ { { } } & { { + } } & { { \mathrm { h i g h e r ~ o r d e r ~ t e r m s } . } } \end{array}
$$

To a first order approximation, the orbit elements have a small variation with time, except $M$ , which is dominated by $n t$ . If $U ^ { \prime }$ is separated into

$$
U ^ { \prime } = U _ { s } + U _ { p }
$$

where

$$
\begin{array} { l c l } { { U _ { s } } } & { { = } } & { { \displaystyle - \frac { G M } { a } \left( \frac { a _ { e } } { a } \right) ^ { 2 } J _ { 2 } ( 3 / 4 \sin ^ { 2 } i - 1 / 2 ) } } \\ { { } } & { { } } & { { } } \\ { { U _ { p } } } & { { = } } & { { \displaystyle \frac { G M } { a } \left( \frac { a _ { e } } { a } \right) ^ { 2 } J _ { 2 } \left( 3 / 4 \sin ^ { 2 } i \cos ( 2 \omega + 2 M ) \right) } } \end{array}
$$

it can be shown from Eq. (2.3.6) that

$$
\dot { \Omega } _ { s } \cong - \frac { 3 } { 2 } J _ { 2 } n \left( \frac { a _ { e } } { a } \right) ^ { 2 } \cos i
$$

if the disturbing function $D$ is taken to be $U _ { s }$ and terms with $e$ are ignored. For convenience the notation $\dot { \Omega } _ { s }$ has been introduced to identify the node rate caused by $U _ { s }$ . It can be further shown using $U _ { s }$ that $a , ~ e$ , and $i$ do not change with time. Hence, for a given set of $a , e$ , and $i$ , $\dot { \Omega } _ { s }$ will be constant, referred to as the secular node rate. Furthermore, it is evident that the sign of $\dot { \Omega } _ { s }$ is determined by the inclination. Specifically , if $J _ { 2 }$ is positive (oblate spheroid, such as Earth), then Table 2.3.2 summarizes the characteristics and terminology associated with various inclinations.

From $\dot { \Omega } _ { s } = \mathrm { c o n s t a n t }$ , it is evident that the ascending node location changes linearly with time at a constant rate, referred to as a secular perturbation. Similarly, the term $U _ { p }$ is responsible for periodic perturbations. It is evident from Eq. (2.3.30) that the magnitude of the node rate for a given inclination will increase as the altitude decreases.

An important application of the secular perturbation in the node is the solarsynchronous satellite. As the name implies, such a satellite is synchronized with the Sun, such that the line of nodes remains aligned with the Earth-Sun direction. This orbit design is adopted for various reasons; for example, lighting conditions on the Earth’s surfaces. For a solar-synchronous satellite $\dot { \Omega _ { s } } = \bar { 3 6 0 ^ { \circ } } / \bar { 3 6 5 } . 2 5$ days $\cong 1 ^ { \circ }$ /day. For a near-circular orbit with a semimajor axis of about $7 0 0 0 { \mathrm { k m } }$ , the inclination would be about $9 8 ^ { \circ }$ .

A more complete expression with no eccentricity truncation for the expansion of the potential as a function of orbit elements can be found in Kaula (1966). This expansion enables the following expressions for the secular rates of $\Omega , \omega$ , and $M$ to be readily obtained:

$$
\begin{array} { r c l } { { \dot { \Omega } _ { s } } } & { { = } } & { { \displaystyle - \frac { 3 } { 2 } J _ { 2 } \frac { n } { ( 1 - e ^ { 2 } ) ^ { 2 } } \left( \frac { a _ { e } } { a } \right) ^ { 2 } \cos i } } \\ { { \dot { \omega } _ { s } } } & { { = } } & { { \displaystyle \frac { 3 } { 4 } J _ { 2 } \frac { n } { ( 1 - e ^ { 2 } ) ^ { 2 } } \left( \frac { a _ { e } } { a } \right) ^ { 2 } ( 5 \cos ^ { 2 } i - 1 ) } } \\ { { \dot { M } _ { s } } } & { { = } } & { { \displaystyle \bar { n } + \frac { 3 } { 4 } J _ { 2 } \frac { n } { ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } \left( \frac { a _ { e } } { a } \right) ^ { 2 } ( 3 \cos ^ { 2 } i - 1 ) . } } \end{array}
$$

The values of $a , e$ , and $i$ in these expressions represent the mean elements; that is, the elements with periodic variations averaged out. In Eq. (2.3.33), $\bar { n } \ =$ $\mu ^ { 1 / 2 } / \bar { a } ^ { 3 / 2 }$ , where $\bar { a }$ is the mean value. Table 2.3.3 provides the characteristics and motion expressed by $\dot { \omega } _ { s }$ . As shown in this table, two inclinations exist where $\dot { \omega } _ { s } = 0$ , referred to as the critical inclinations.

Considering only the effect of $U _ { s }$ , the following orbit elements exhibit linear variations with time: $\Omega , \omega , M$ . It can be shown that $a , e$ , and $i$ do not exhibit such change. As a consequence, a simple model of the perturbed motion is a secularly precessing ellipse (SPE). In this model, $a , e$ , and $i$ are constant, and $\Omega , \omega$ , and $M$ change linearly with time at the rates derived from $U _ { s }$ . With the SPE as a reference, the effect of $U _ { p }$ , Eq. (2.3.29), can be introduced to show that, to first order,

$$
a ( t ) = \overline { { a } } + 3 \bar { n } \bar { a } J _ { 2 } \left( \frac { a _ { e } } { \overline { { a } } } \right) ^ { 2 } \sin ^ { 2 } \overline { { i } } \frac { \cos ( 2 \omega + 2 M ) } { 2 \dot { \omega } _ { s } + 2 \dot { M } _ { s } }
$$

Table 2.3.3: Perigee Motion as a Function of Inclination $\left( J _ { 2 } > 0 \right)$ )   

<table><tr><td>Inclination i</td><td>Ws</td><td>Terminology</td></tr><tr><td>i&lt; 63.435°</td><td>Positive</td><td>Progression of perigee</td></tr><tr><td>i = 63.435°</td><td>Zero</td><td>Critical inclination</td></tr><tr><td>63.435°&lt;i&lt;116.656°</td><td>Negative</td><td>Regression of perigee</td></tr><tr><td>i= 116.565°</td><td>Zero</td><td>Critical inclination</td></tr><tr><td>i &gt; 116.565</td><td>Positive</td><td>Progression of perigee</td></tr></table>

where $( ^ { - } )$ denotes the mean value of the element. Recall that this expression is approximate since terms with order $e ^ { 1 }$ and higher powers, as well as $J _ { 2 } ^ { 2 }$ , have been ignored. If the eccentricity is small, this expression is a good approximation. It should also be noted that mean elements can be replaced by osculating elements, except in the computation of $\overline { { n } }$ in the first term of $\dot { M }$ , since terms of $J _ { 2 } ^ { 2 }$ are ignored. Note that $\overline { { n } } = \mu ^ { 1 / 2 } / \overline { { a } } ^ { 3 / 2 }$ . If $J _ { 2 } ^ { 2 }$ terms are ignored, $\bar { a }$ may be computed from Eq. (2.3.34) by using an osculating value for $a ( t )$ and in the second term for $\bar { a }$ .

The preceding discussion illustrates the concepts of general perturbations; that is, an analytical solution of Lagranges planetary equations. A well-known solution for all the orbit elements is given by Brouwer for the $J _ { 2 }$ problem (Appendix E). The equations in this appendix have truncated Brouwer’s solution so that terms of order $e J _ { 2 }$ are ignored.

The linear solution of Kaula (1966) is an example of a solution that enables categorization of the influence of all gravity coefficients on the orbit perturbation. As shown by Kaula, the general frequency of a perturbation is given by

$$
\dot { \psi } _ { l m p q } = ( l - 2 p ) \dot { \omega } _ { s } + ( l - 2 p + q ) \dot { M } _ { s } + m ( \dot { \Omega } _ { s } - \omega _ { e } )
$$

where $p$ is an index that ranges from 0 to $l , q$ is an index associated with a function that is dependent on the orbit eccentricity, and $\omega _ { e }$ is the rotation rate of the primary body. The orbit element change with time is dependent on eccentricity and inclination functions. The eccentricity-dependent function has a leading term that is dependent on $e ^ { | q | }$ ; thus, for small eccentricity orbits, $q$ is usually considered to range between $- 2$ and $+ 2$ . The characteristics of the orbit perturbations caused by individual degree and order terms in the gravity field are summarized in Table 2.3.4, where the categories are defined by the nature of $\dot { \psi } _ { l m p q }$ . Note that the period of the perturbation is $2 \pi / \dot { \psi } _ { l m p q }$ . An example of resonance is the geostationary satellite, where $\dot { M } = \omega _ { e }$ .

Table 2.3.4:   
Perturbation Categories and Sources   

<table><tr><td>Category</td><td>Source</td><td>Comments</td></tr><tr><td>Secular</td><td>Even-degree zonals</td><td>l-2p=0;l-2p+q=0;m=0</td></tr><tr><td>Long period</td><td>Odd-degree zonals</td><td>l-2p≠0;l-2p+q=0;m=0</td></tr><tr><td>Short period</td><td>All gravity coeffci ents</td><td>l-2p+q≠0</td></tr><tr><td>m-daily</td><td>Order m terms</td><td>l-2p=0;l-2p+q=0;m≠0</td></tr><tr><td>Resonance</td><td>Order m terms</td><td>(l-2p)u+(l-2p+q)M≌-m(Ω-ωe)</td></tr></table>

A special class of perturbed orbits, known as frozen orbits, have proven useful for some applications. For these orbits, even though the inclination is not critical, $J _ { 2 }$ and $J _ { 3 }$ interact to produce $\dot { \omega } _ { s } = 0$ (Cook, 1966; Born et al., 1987) and the mean perigee remains fixed at about $9 0 °$ or $2 7 0 ^ { \circ }$ in an average sense. Frozen orbits are useful in applications where it is desired that the mean altitude have small variations for a given latitude. They are required if it is necessary to have an exactly repeating ground track. Otherwise, the time to go between two latitudes will vary as the perigee rotates, and the ground tracks will not repeat.

The nodal period is the time required for a satellite to complete successive equatorial crossings, such as ascending node to ascending node. The nodal period, $P _ { n }$ , is

$$
P _ { n } = \frac { 2 \pi } { \dot { \omega } _ { s } + \dot { M } _ { s } }
$$

or

$$
P _ { n } = \frac { 2 \pi } { \bar { n } } \left[ 1 - 3 / 2 J _ { 2 } \left( \frac { a _ { e } } { \overline { { { a } } } } \right) ^ { 2 } \left( 4 \cos ^ { 2 } i - 1 \right) \right]
$$

which is obtained using Eqs. (2.3.31) and (2.3.32). Using osculating elements, the nodal period for a near-circular orbit is

$$
\begin{array} { l c l } { { P _ { n } } } & { { = } } & { { \displaystyle \frac { 2 \pi } { n } \bigg [ 1 - 3 / 4 ~ J _ { 2 } \left( \frac { a _ { e } } { a } \right) } } \\ { { } } & { { } } & { { \displaystyle \left\{ 1 + 5 \cos ^ { 2 } i - 6 \sin ^ { 2 } i \sin ^ { 2 } \left( \omega + M \right) \right\} \bigg ] . } } \end{array}
$$

Note that either mean or osculating elements can be used in any term that is multiplied by $J _ { 2 }$ , since the approximation used in the analytic theory is accurate only to order $J _ { 2 }$ . However, unless a mean value of semimajor axis is used in Eq. (2.3.37), an error of order $J _ { 2 }$ will be introduced in the lead term of the nodal period equation. Note also that Eq. (2.3.38) requires an osculating value for $a$ to compute $n$ .

Another useful concept in mission design is that of the nodal day, which is the time required for the Earth to make one revolution relative to the satellite’s line of nodes. It is given by

$$
D _ { n } = \frac { 2 \Pi } { \dot { \Omega } _ { s } + \omega _ { e } } .
$$

Hence, a nodal day will be greater than a siderial day for retrograde orbits and less than a siderial day for posigrade orbits.

# Example 2.3.1

For the Space Shuttle example, Example 2.2.4.1, use the state vector as initial conditions for the numerical integration of the equations of motion given by Eqs. (2.3.17) and (2.3.26). For the Earth, $J _ { 2 } = 0 . 0 0 1 0 8 2 6 3 6$ (the normalized value $C _ { 2 , 0 } = - 0 . 0 0 0 4 8 4 1 6 9 5 )$ . The position-velocity ephemeris, converted into orbit elements, produces the results shown in Fig. 2.3.5 for $a , e , i , \Omega$ , and $\omega$ for a one-day interval. Evaluation of Eq. (2.3.31) for $\dot { \Omega } _ { s }$ with the approximate mean orbit elements $( a = 6 8 2 7 \mathrm { k m }$ , $e = 0 . 0 0 8$ , $i = 2 8 . 4 5 5$ ) gives $- 6 . 9 1 ^ { \circ } / \mathrm { d a y }$ . The approximate slope of $\Omega$ in Fig. 2.3.5 is $- 6 . 9 3 ^ { \circ } / \mathrm { d a y }$ . Note that $a$ and $i$ exhibit no secular rate (as expected), only a dominant twice-per-revolution change, as suggested by Eq. (2.3.34) for semimajor axis. Note that $e$ exhibits no secular variation, although its periodic variations includes a combination of frequencies (see Appendix E).

# 2.3.5 GRAVITATIONAL PERTURBATIONS: THIRD-BODY EFFECTS

An artificial satellite of the Earth experiences the gravitational attraction of the Sun, the Moon, and to a lesser extent the planets and other bodies in the solar system. Equation (2.3.1), which was derived for the perturbed lunar motion based on the gravitational problem of three bodies, can be adapted to represent the gravitational effect of celestial bodies on the motion of a satellite. Since the description is based on the problem of three bodies, the perturbation is often referred to as the third-body effect, even when more than three bodies are considered. In some literature, the terminology $n$ -body effects may be used to accommodate the case when many perturbing bodies are included. With the third-body effects, it can be shown that the perturbing force contribution to the equations of motion, Eq. (2.3.3), is

![](images/5293a6e480e9127c6889632a7c519b62f8847a56860bad0948f657468a79da37.jpg)  
Figure 2.3.5: Orbit element variations produced by Earth oblateness, $J _ { 2 }$ . The mean anomaly is not shown since it is a straight line with a slope approximately equal to $n$ . The ascending node and the argument of perigee exhibit significant linear variation, whereas $a , ~ e$ , and $i$ do not. These results were obtained from numerical integration of the equations of motion.

$$
\mathbf { f } _ { 3 B } = \sum _ { j = 1 } ^ { n _ { p } } \mu _ { j } \left( \frac { \Delta _ { j } } { \Delta _ { j } ^ { 3 } } - \frac { \mathbf { r } _ { j } } { r _ { j } ^ { 3 } } \right)
$$

where $n _ { p }$ is the number of additional bodies, $j$ represents a specific body (Sun, Moon, or planet), $\mu _ { j } = G M _ { j }$ is the gravitational parameter of body $j , \Delta _ { j }$ is the position vector of $M _ { j }$ with respect to the satellite, and $\mathbf { r } _ { j }$ is the position vector of $M _ { j }$ with respect to the Earth (see Fig. 2.3.1). The first term $( \Delta _ { j } / \Delta _ { j } ^ { 3 } )$ of the thirdbody perturbation is known as the direct effect and the second term $( \mathbf { r } _ { j } / r _ { j } ^ { 3 } )$ is the indirect effect. The notation for the latter term arises from the observation that it is independent of the artificial satellite coordinates. Since Eq. (2.3.39) describes the satellite motion with respect to the Earth center of mass, which is a noninertial point, the indirect term accounts for the inertial acceleration of the geocenter.

The third-body terms in Eq. (2.3.39) are based on the assumption that the satellite, Earth, and perturbing body $( M _ { j } )$ are point masses (or spheres of constant density). In reality, the Moon and Sun should be represented by a gravitational potential, such as Eq. (2.3.12). The satellite equations of motion will be complicated by the inclusion of these terms, but the accuracy required for most applications does not warrant such modeling of the luni-solar gravitational fields. For some high-accuracy applications, the dominant contribution is the interaction of the third body with the Earth oblateness through the indirect term, sometimes referred to as the indirect oblateness.

The nature of the third-body perturbation is similar to the Earth oblateness effect; namely, the Sun and Moon produce a secular variation in the satellite node, argument of perigee, and mean anomaly. Expressing the third-body perturbation with a gravitational potential and following a treatment similar to the approach used in Section 2.3.4, it can be shown that the secular node rate for an Earth satellite is

$$
{ \dot { \Omega } } _ { \mathrm { s e c } } = { \frac { 3 } { 4 } } { \frac { \mu _ { j } } { a _ { j } ^ { 3 } } } { \frac { \cos i } { n } } \left( { \frac { 3 } { 2 } } \sin ^ { 2 } \epsilon - 1 \right)
$$

where the $5 ^ { \circ }$ inclination of the Moon’s orbit with respect to the ecliptic has been ignored, the subscript $j$ identifies the Moon or the Sun, and $\epsilon$ is the obliquity of the ecliptic.

It is evident from Eq. (2.3.40) that the third-body effect on the nodal motion increases as the altitude increases, since $n$ gets smaller with increasing semimajor axis. This characteristic is consistent with the expectation that the effect would increase as the satellite altitude approaches the source of the perturbation. Note the dependency of $\dot { \Omega } _ { \mathrm { s e c } }$ on $\cos i$ , which is similar to the $J _ { 2 }$ effect. Since the quantity in parentheses is negative, $\dot { \Omega } _ { \mathrm { s e c } }$ is retrograde for a posigrade orbit, for example.

In addition to the secular effect contributed by the Moon and Sun, significant periodic effects exist. The largest periodic effects have periods of 183 days and 14 days, caused by the Sun and Moon, respectively. The semiannual solar effects are greater than the lunar semimonthly effects. The coordinates of the Sun, Moon, and planets required for the third-body perturbation are available in numerical form (e.g., Standish et al., 1997). These coordinates are expressed in the J2000.0 system.

# 2.3.6 GRAVITATIONAL PERTURBATIONS: TEMPORAL CHANGES IN GRAVITY

If the mass distribution within a body is constant over time in an appropriate coordinate system that is fix ed in the body, the mass property coeffici ents, $C _ { l m }$ and $S _ { l m }$ , will be constant. Such is the case if the body is perfectly rigid. However, all celestial bodies deform at some level and this deformation redistributes mass so that the mass property coefficients vary with time. The ocean tides are well known and familiar mass-redistribution phenomena, but the solid Earth also responds to the same luni-solar gravitational forces that are responsible for the ocean tides. The previous formulation for the gravitational potential, Eq. (2.3.12), is valid even if the $C _ { l m }$ and $S _ { l m }$ coefficients are time dependent. The detailed formulation for the temporal changes in these coefficients produced by solid Earth and ocean tides is given by McCarthy (1996). Further discussion of the topic is given by Lambeck (1988).

The dominant tide effect appears in temporal changes of the degree two coefficients ; namely,

$$
\begin{array} { l r c l r c l } { { \Delta J _ { 2 } } } & { { = } } & { { - K _ { T } \ q _ { 2 , 0 } } } & { { } } & { { } } & { { } } & { { } } \\ { { \Delta C _ { 2 , 1 } } } & { { = } } & { { K _ { T } \ q _ { 2 , 1 } } } & { { \Delta S _ { 2 , 1 } } } & { { = } } & { { K _ { T } \ u _ { 2 , 1 } \nonumber } } \\ { { \Delta C _ { 2 , 2 } } } & { { = } } & { { K _ { T } \ q _ { 2 , 2 } } } & { { \Delta S _ { 2 , 2 } } } & { { = } } & { { K _ { T } \ u _ { 2 , 2 } } } \end{array}
$$

$$
K _ { T } = k _ { 2 } \frac { a _ { e } ^ { 3 } } { \mu } .
$$

Here, $k _ { 2 } =$ second-degree Love Number (dependent on elastic properties of the Earth, with an approximate value of 0.3), thus:

$$
\begin{array} { c c l } { { q _ { 2 , 0 } } } & { { = } } & { { \displaystyle \sum _ { j } C _ { T } P _ { 2 , 0 } ( \sin \phi _ { j } ) } } \\ { { } } & { { } } & { { } } \\ { { q _ { 2 , 1 } } } & { { = } } & { { \frac { 1 } { 3 } \displaystyle \sum _ { j } C _ { T } P _ { 2 , 1 } ( \sin \phi _ { j } ) \cos \lambda _ { j } } } \end{array}
$$

$$
\begin{array} { l c l } { { q _ { 2 , 2 } } } & { { = } } & { { \frac { 1 } { 1 2 } \displaystyle \sum _ { j } C _ { T } P _ { 2 , 2 } ( \sin \phi _ { j } ) \cos 2 \lambda _ { j } } } \\ { { } } & { { } } & { { } } \\ { { u _ { 2 , 1 } } } & { { = } } & { { \frac { 1 } { 3 } \displaystyle \sum _ { j } C _ { T } P _ { 2 , 1 } ( \sin \phi _ { j } ) \sin \lambda _ { j } } } \\ { { } } & { { } } & { { } } \\ { { u _ { 2 , 2 } } } & { { = } } & { { \frac { 1 } { 1 2 } \displaystyle \sum _ { j } C _ { T } P _ { 2 , 2 } ( \sin \phi _ { j } ) \sin 2 \lambda _ { j } } } \\ { { } } & { { } } & { { } } \\ { { C _ { T } } } & { { = } } & { { \frac { \mu _ { j } } { r _ { j } ^ { 3 } } } } \end{array}
$$

where

$j$ is determined by the Moon or Sun,

$r _ { j }$ is the distance from the geocenter to the center of mass of the Moon or Sun, and

$\phi _ { j } \lambda _ { j }$ are the geocentric latitude and longitude of the Moon and Sun, respectively.

The magnitude of $\Delta J _ { 2 }$ is about $1 0 ^ { - 8 }$ , compared to the $J _ { 2 }$ magnitude of $1 0 ^ { - 3 }$ . Care should be taken with applying $\Delta J _ { 2 }$ , since the average value produced by Eq. (2.3.41) is nonzero and this average may already be accommodated into $J _ { 2 }$ .

Other phenomena contribute to temporal changes in gravity. Among these are meteorologically driven redistributions of atmospheric mass as well as redistribution of solid Earth and ocean mass in response to changes in the magnitude and direction of the Earth’s angular velocity vector. The latter phenomena are referred to as pole tides.

# 2.3.7 GRAVITATIONAL PERTURBATIONS: GENERAL RELATIVITY

Although the preceding developments are well served by the foundations of Newtonian mechanics, some high-accuracy applications will require additional terms introduced by relativistic effects (Einstein, 1905; Huang et al. 1990; Ries et al., 1991). The dominant dynamical effect from general relativity is a small, but observable, advance in the argument of perigee (Ries et al., 1991). For example, a satellite such as BE-C $( a = 7 5 0 0 \mathrm { k m }$ , $e = 0 . 0 2 5$ , $i = 4 1 . 2 ^ { \circ }$ ) experiences an advance of 11 arcsec/yr in the location of perigee. The relativistic term that should be included in the equations of motion is

$$
{ \bf f } _ { g } = \frac { \mu } { c ^ { 2 } r ^ { 3 } } \left\{ \left[ 2 ( \beta + \gamma ) \frac { \mu } { r } - \gamma ( \dot { \bf r } \cdot \dot { \bf r } ) \right] { \bf r } + 2 ( 1 + \gamma ) ( { \bf r } \cdot \dot { \bf r } ) \dot { \bf r } \right\}
$$

where

$c$ is the speed of light,

$\mathbf { r } , \dot { \mathbf { r } }$ are the position and velocity vectors of the satellite in geocentric nonrotating coordinates,

$\beta , \gamma$ are parameters in the isotropic Parameterized Post-Newtonian metric, which are exactly equal to one in General Relativity.

As previously noted, the dominant effect of this contribution is a secular motion of perigee.

# 2.3.8 NONGRAVITATIONAL PERTURBATIONS: ATMOSPHERIC RESISTANCE

For a low-altitude Earth satellite, atmospheric drag can be a dominant perturbing force. The drag force is derived from aerodynamic considerations and the representation of the drag force on an orbiting vehicle is the same as an atmospheric fli ght vehicle:

$$
\mathbf { F } _ { \mathrm { D r a g } } = - 1 / 2 \rho C _ { D } A V _ { r } \mathbf { V } _ { r }
$$

where $\rho$ is the atmospheric density, $C _ { D }$ is the drag coefficient, ${ \mathbf V } _ { r }$ is the vehicle velocity relative to the atmosphere, $A$ is the satellite cross-sectional area and the minus sign denotes the direction opposite to ${ \mathbf V } _ { r }$ . When this force is included in the derivation of the equations of satellite motion with respect to the geocenter, the following perturbing force per unit mass results, which will be added to the other forces in Eq. (2.3.3):

$$
{ \bf f } _ { \mathrm { D r a g } } = - 1 / 2 \rho \left( \frac { C _ { D } A } { m } \right) V _ { r } { \bf V } _ { r }
$$

where the satellite mass, $m$ , now appears as a divisor in the drag term. A commonly used parameter in the drag term is $( C _ { D } A / m )$ , sometimes referred to as the ballistic coefficient . At low altitudes, such as those where the Space Shuttle operates $( \sim 3 5 0 \mathrm { k m } )$ ), the atmospheric density is about $1 0 ^ { - 1 1 }$ that of sea level density. Such low densities have mean molecular distances measured in meters. Nevertheless, atmospheric drag removes energy from the orbit and produces a secular decay in semimajor axis and eccentricity. This decay eventually brings the satellite into the higher density regions of the atmosphere, and it may be destroyed by the heating produced from atmospheric friction generated by the high orbital speeds. Some satellites have been designed to accommodate the high heat loads produced by atmospheric entry, such as Space Shuttle, but most satellites will not survive intact.

The drag term in Eq. (2.3.43) is dependent on several factors. Most notably, the atmospheric density exhibits an approximately exponential reduction with increasing altitude, $\rho = \rho _ { 0 } e ^ { - \beta ( h - h _ { 0 } ) }$ , where $\rho _ { 0 }$ is the density at a reference altitude $h _ { 0 }$ , $h$ is the altitude of interest, and $\beta$ is a scale parameter. But the specific density at any location will be influe nced by the day-night cycle and the location of the subsolar point, solar activity (e.g., solar storms), geomagnetic activity, and seasonal variations. A satellite at a constant altitude can experience an order of magnitude change in density over an orbital revolution. Acting over many orbital revolutions, the decay in semimajor axis will determine the lifetime of a satellite. A very low-altitude satellite with a high ballistic coefficient will have a short lifetime, perhaps a few weeks or a few months in duration. Prediction of satellite lifetime is a challenging problem, but it is made particularly difficul t by uncertainties in predicting atmospheric density and other factors. Various models of atmospheric density exist, such as those developed by Barlier, et al. (1978) and Jacchia (1977).

To account for the variations in drag produced by changes in atmospheric density, as well as the area-to-mass ratio $\left( A / m \right)$ , other parameterizations are introduced. These parameterizations may include piecewise constant values of $C _ { D }$ , which are defined over specific intervals of time, or more complex representations of $C _ { D }$ .

Some satellites have been designed to reduce the effects of atmospheric drag. Most notably, these are satellites where high-accuracy knowledge of the orbital position is required and it is desirable to minimize the influence of forces with significa nt uncertainty such as drag. The French Starlette satellite, launched in 1975, is spherical with a diameter of $1 4 ~ \mathrm { c m }$ , but it contains a core of depleted uranium to increase the mass. The area-to-mass ratio for Starlette is $0 . 0 0 1 \mathrm { ~ m } ^ { 2 } / \mathrm { k g }$ . By contrast, the Echo balloon satellite had an $\mathrm { A } / \mathrm { m }$ of about $1 0 \mathrm { m } ^ { 2 } / \mathrm { k g }$ . It is obvious that the balloon satellite will have a much shorter lifetime than Starlette at the same altitude.

If it is assumed that $V _ { r } = V$ , it can be shown (Danby, 1988) that

$$
\frac { d a } { d t } = - \left( \frac { C _ { D } A } { m } \right) \frac { \rho a ^ { 2 } } { \mu } V ^ { 3 } .
$$

Since $V _ { r }$ is almost entirely in the orbit plane, drag has only a very small out-ofplane force and, hence, there is no significant drag effect on the orbit node or

inclination. In addition to the secular change in semimajor axis, $e$ and $\omega$ also exhibit secular change because of drag.

# 2.3.9 NONGRAVITATIONAL PERTURBATIONS: RADIATION PRESSURE

For an Earth satellite, the Sun is the source for perturbations referred to as solar radiation pressure. This force results from the transfer of momentum through impact, reflection, absorption, and re-emission of photons. The Earth is an additional perturbation source, through both reflected solar radiation and emitted radiation, both of which exhibit considerable variation over an orbital revolution. The solar radiation pressure force contribution $( \mathbf { f } _ { S R P } )$ to Eq. (2.3.3) is given by

$$
\mathbf { f } _ { S R P } = - P \frac { \nu A } { m } C _ { R } \mathbf { u }
$$

where $P$ is the momentum flux from the Sun at the satellite location, $A$ is the cross-sectional area of the satellite normal to the Sun, $\mathbf { u }$ is the unit vector pointing from the satellite to the Sun, $C _ { R }$ is the reflec tivity coefficient with a value of approximately one, and $\nu$ is an eclipse factor such that $\nu = 0$ if the satellite is in the Earth’s shadow (umbra), $\nu = 1$ if the satellite is in sunlight, and $0 < \nu < 1$ if the satellite is in partial shadow or penumbra. The passage of the satellite from sunlight to shadow is not abrupt, but the interval of time spent in partial shadow will be very brief for near-Earth satellites. In the vicinity of Earth, $P$ is approximately $4 . 5 6 \times 1 0 ^ { - 6 }$ Newtons $/ \mathrm { m ^ { 2 } }$ .

The modeling of the Earth radiation components is commonly performed with spherical harmonics to represent latitudinal and longitudinal variations of Earth albedo and emissivity. This force can be expressed using Eq. (2.3.45), except the momentum flux parameter would account for the albedo and emissivity and u would be directed toward the Earth. It is known from observations that the simple model given by Eq. (2.3.45) is inadequate for applications with high accuracy requirements. Alternate models for GPS are described by Fliegel et al. (1992) and Beutler et al. (1994).

# 2.3.10 NONGRAVITATIONAL PERTURBATIONS: OTHER

Other nongravitational forces exist that may influence the orbit in complex ways. Aside from forces that involve the magnetic fiel d of the planet (e.g., if the satellite has a charge), there are other forces that have been studied because of their anomalous nature.

In addition to solar radiation pressure modeled by Eq. (2.3.45), heating of satellite components by the Sun and the Earth, as well as internal heat sources, will produce an unsymmetrical thermal distribution. Such a thermal imbalance will generate a thermal force, which may produce drag-like characteristics. The modeling of a spacecraft with more complex shapes, such as TOPEX/Poseidon and GPS, has required analysis by finite element methods for high-accuracy applications. A review of nongravitational force modeling is given by Ries et al. (1993). For purposes of this book, these forces will be covered by the term fOther in the satellite equations of motion.

Satellite-dependent models have been developed to represent some nongravitational components. The GPS satellites experience a force parallel to the solar panel rotation axis, referred to as the y-bias force, thought to result from solar panel misalignment and/or thermal force effects (Vigue, et al., 1994). index[aut]Schutz, B. E.

Additional forces exist, usually with short time duration, associated with mass expulsion from a spacecraft. The resulting force, or thrust, may be difficult to model because the time at which the expulsion occurred and magnitude of the event may be unknown.

For some applications, empirical forces are included in the equations of motion to accommodate forces of unknown origin or errors that result from mismodeling of forces. As described in this chapter, a typical error signature has a periodicity approximately equal to the orbit period; that is, a once per revolution characteristic. A convenient modeling takes the form of $A \cos n t + B \sin n t + C$ , where $n$ is the mean motion and $A$ , $B$ , $C$ are empirical parameters to be estimated in the orbit determination process. The empirical model may be applied to the radial, transverse, and/or normal components.

# 2.3.11 PERTURBED EQUATIONS OF MOTION: SUMMARY

Based on Eq. (2.3.3), the satellite equations of motion are

$$
{ \ddot { \mathbf { r } } } = - { \frac { \mu \mathbf { r } } { r ^ { 3 } } } + \mathbf { f }
$$

where $\mathbf { r }$ is the position vector of the satellite center of mass in an appropriate reference frame. The perturbing force f consists of the following

$$
\mathbf { f } = \mathbf { f } _ { N S } + \mathbf { f } _ { 3 B } + \mathbf { f } _ { g } + \mathbf { f } _ { \mathrm { D r a g } } + \mathbf { f } _ { \mathrm { S R P } } + \mathbf { f } _ { \mathrm { E R P } } + \mathbf { f } _ { \mathrm { O t h e r } }
$$

where

$\mathbf { f } _ { N S }$ is given by Eq. (2.3.21), including the tide contribution in Eq. (2.3.41),   
$\mathbf { f } _ { 3 B }$ is given by Eq. (2.3.39),   
$\mathbf { f } _ { g }$ represents the contributions of general relativity, Eq. (2.3.42),   
$\mathbf { f } _ { \mathrm { D r a g } }$ is given by Eq. (2.3.43),

fSRP is given by Eq. (2.3.45), fERP is Earth radiation pressure,

fOther represents other forces, such as thermal effects, magnetically induced forces, and so on.

The various contributions to the equations of motion must use a consistent coordinate system. If, for example, the acceleration ¨r is expressed in J2000, all individual components of f must be expressed in the same system. As a result, some of these components may require coordinate transformations similar to those given in Eq. (2.3.21) for the nonspherical mass distribution effects. Advanced aspects of the relevant transformation between, for example, Earth-fix ed and J2000 are discussed in the next section.

As noted previously, Eq. (2.3.46) can be solved with the use of a numerical method or through analytical approaches. Both introduce different levels of approximation. Various high-accuracy numerical programs have been developed in the community based on different numerical methods (single-step integrators, multistep integrators, etc.).

The advantage of speed offered by analytical techniques may be traded for force model accuracy (see Section 2.5). In these cases, a simplified geopotential consisting of a few zonal harmonics plus the effects of luni-solar gravity and drag may be used. NORAD, for example, has adopted such a general perturbation method, based on Brouwer’s Theory (see Appendix E).

# Example 2.3.11.1

The node rate of the GPS satellite known as PRN-5 was observed to have a dominant secular rate of $- 0 . 0 4 1 0 9 ~ \mathrm { d e g / d a y }$ during 1995 and 1996. We wish to determine the most significant factors that contribute to this rate. The following mean elements for the satellite also were observed:

$$
\begin{array} { l c l } { { a } } & { { = } } & { { 2 6 5 6 0 . 5 \mathrm { k m } } } \\ { { e } } & { { = } } & { { 0 . 0 0 1 5 } } \\ { { i } } & { { = } } & { { 5 4 . 5 \mathrm { d e g } . } } \end{array}
$$

The following contributions can readily be obtained:

$J _ { 2 }$ Eq. (2.3.31) −0.03927 deg/day Moon Eq. (2.3.40) −0.00097 Sun Eq. (2.3.40) −0.00045

Total −0.04069 deg/day

The difference between the observed value and this total is $0 . 0 0 0 4 ~ \mathrm { d e g / d a y }$ , or $1 \%$ , caused mainly by secular contributions from the other even-degree zonal harmonics and $J _ { 2 } ^ { 2 }$ .

# 2.4 COORDINATE SYSTEMS AND TIME:INTRODUCTION

Time and coordinate systems are an inherent component of the orbit determination problem. As described in Chapter 3, measurements of some aspect of a satellite’s position or motion must be indexed in time. The time index of the measurements must be related to the time used in the equations of motion, Eq. (2.3.46), but different time systems are used, all of which attempt to represent the concept of Newtonian time. The relation between the various time systems must be known.

Measurements collected by some instrumentation located on the Earth’s surface suggest the use of coordinate systems attached to the Earth at the location of the instrument. Such topocentric coordinate systems rotate since they are fix ed to the planet’s surface. On the other hand, the equations of motion use an inertial system. It is evident that transformation equations between the various coordinate systems are required.

The coordinate description given in Section 2.2.3, based on the problem of two bodies, assumed that the bodies were rigid spheres with constant density. In this model, the equinoxes remained fix ed in direction, and the angular velocity vectors of the rotating bodies maintain the same direction in space. The following sections relax these conditions and examine the effects resulting from more realistic models of the celestial bodies. The resulting transformations and relationships are essential in the modern orbit determination problem. More complete discussions of the characteristics of the rotation of the Earth are given by Lambeck (1980) and Moritz and Mueller (1987).

# 2.4.1 PRECESSION AND NUTATION

Consider the motion of a spherical Moon orbiting the nonspherical Earth. Based on the discussion in Section 2.3, the gradient of the gravitational potential given by Eq. (2.3.12), multiplied by the mass of the Moon, yields the gravitational force experienced by the Moon. By Newton’s Third Law, the Earth will experience an equal and opposite force; however, this force will not, in general, be directed through the center of mass of the Earth. As a consequence, the Earth will experience a gravitational torque, $\mathbf { T }$ , given by

$$
\mathbf { T } = - \mathbf { r } _ { p } \times M _ { P } \pmb { \nabla } _ { P } U ^ { \prime }
$$

![](images/2195bbb3aefa6fd7f2879c7cc3aae991874debf49482f41746ac834c5412a069.jpg)  
Figure 2.4.1: Precession and nutation. The Sun and Moon interact with the oblateness of the Earth to produce a westward motion of the vernal equinox along the ecliptic $( \Psi )$ and oscillations of the obliquity of the ecliptic $( \epsilon )$ .

where $U ^ { \prime }$ is the Earth’s gravitational potential, $\nabla _ { P }$ is the gradient operator with respect to the coordinates of the Moon $( \mathbf { r } _ { p } )$ , and $M _ { P }$ is the mass of the Moon. The torque acting on the Earth produces changes in the inertial orientation of the Earth.

In the case of the Earth, both the Moon and the Sun are significant contributors to this gravitational torque. A dominant characteristic of the changes in inertial orientation is a conical motion of the Earth’s angular velocity vector in inertial space, referred to as precession. Superimposed on this conical motion are small oscillations, referred to as nutation.

Consider the two angles in Fig. 2.4.1, $\Psi$ and $\epsilon$ . The angle $\Psi$ is measured in the ecliptic from a fix ed direction in space, $X ^ { \ast }$ , to the instantaneous intersection of the Earth’s equator and the ecliptic. As discussed in Section 2.2.3, the intersection between the equator and the ecliptic where the Sun crosses the equator from the southern hemisphere into the northern hemisphere is the vernal equinox. For this discussion, the ecliptic is assumed to maintain a fix ed orientation in space, although this is not precisely the case because of gravitational perturbations from the planets. The angle $\epsilon$ represents the angle between the angular velocity vector and an axis $Z _ { e c }$ , which is perpendicular to the ecliptic. The gravitational interaction between the Earth’s mass distribution, predominantly represented by the oblateness term, $J _ { 2 }$ , and the Sun or Moon produces a change in $\Psi$ , which can be shown to be

$$
\dot { \Psi } = - { \frac { 3 } { 2 } } \left( { \frac { \mu J _ { 2 } a _ { e } ^ { 2 } } { C \omega _ { e } } } \right) { \frac { M _ { p } } { a _ { p } ^ { 3 } } } \cos \bar { \epsilon }
$$

where the subscript $p$ represents the Sun or the Moon, the parameters in the parentheses refer to Earth, $C$ is the polar moment of inertia of Earth, and $\bar { \epsilon }$ is the mean obliquity of the ecliptic. This motion, known as the precession of the equinoxes, has been known since antiquity. The combined effect of the Sun and the Moon produce $\dot { \Psi } = - 5 0$ arcsec/yr; that is, a westward motion of the vernal equinox amounting to $1 . 4 ^ { \circ }$ in a century. Thus, the conical motion of $\omega _ { e }$ about $Z _ { e c }$ requires about 26,000 years for one revolution.

The obliquity of the ecliptic, $\epsilon$ , is $\epsilon = \bar { \epsilon } + \Delta \epsilon$ , where $\bar { \epsilon }$ represents the mean value, approximately $2 3 . 5 ^ { \circ }$ . The nutations are represented by $\Delta \epsilon$ , which exhibits periodicities of about 14 days (half the lunar period, or semimonthly) and 183 days (half the solar period, or semiannual), plus other long period variations. The $5 ^ { \circ }$ inclination of the Moon’s orbit with respect to the ecliptic, $i _ { M }$ , produces a long period nutation given by:

$$
\Delta \epsilon = \frac { 3 } { 2 } \left( \frac { \mu J _ { 2 } a _ { e } ^ { 2 } } { C \omega _ { e } } \right) \frac { M _ { M } } { a _ { M } ^ { 3 } } \cos i _ { M } \sin i _ { M } \cos \epsilon \frac { \cos ( \Omega _ { M } - \Psi ) } { ( \dot { \Omega } _ { M } - \dot { \Psi } ) }
$$

where the subscript $M$ refers to the Moon, and the amplitude of the coefficient of $\cos ( \Omega _ { M } - \Psi )$ in Eq. (2.4.3) is about 9 arcsec with a period of 18.6 years. The 9 arcsec amplitude of this term is known as the constant of nutation. The amplitudes of the semimonthly and semiannual terms are smaller than the constant of nutation, but all are important for high-precision applications.

The precession/nutation series for a rigid body model of the Earth, including the ecliptic variations, were derived by Woolard (1953). Extensions that include the effects of nonrigidity have been developed. Nevertheless, small discrepancies between observation and theory exist, believed to be associated with geophysical effects in the Earth’s interior (Herring et al., 1991; Wahr, 1981). Such observational evidence will lead, in time, to the adoption of new series representing the precession and nutation. The current 1980 International Astronomical Union (IAU) series are available with the lunar, solar, and planetary ephemerides in an efficient numerical form based on results generated by the Jet Propulsion Laboratory (Standish et al., 1997).

As described in Section 2.2.3, the J2000.0 mean equator and equinox specifies a specific point on the celestial sphere on January 1, 2000, 12 hrs. The true of date (TOD) designation identifies the true equator and equinox at a specified date. The J2000.0 equinox is fix ed in space, but the location of the TOD equinox changes with time.

# 2.4.2 EARTH ROTATION AND TIME

In the simplified model of Earth rotation described in Section 2.2.3, the angular velocity vector, $\omega _ { e }$ , is fix ed in direction and magnitude. It has been known since the late 1800s that the direction of this vector does not remain fixed in direction with respect to an Earth-fix ed frame of reference (Seidelmann, 1992). The vector describes a conical counter-clockwise motion, making a complete revolution in about 430 days (known as the Chandler period), but exhibiting an annual variation as well. The combination of Chandler and annual periods results in a six-year variation. Over a decadal time scale, this polar motion is confined to a region around the $z$ axis with a diameter of less than 0.6 arcsec (or $1 8 . 5 \mathrm { ~ m ~ }$ at the Earth’s surface). The components of the angular velocity vector in the $( x , y )$ plane are usually expressed in terms of angular components $( x _ { p } , y _ { p } )$ using a left-handed coordinate system. The $x$ axis of this system is directed along the Greenwich meridian and the $y$ axis is directed toward $9 0 °$ west. These components $( x _ { p } , y _ { p } )$ provide the direction of $\omega _ { e }$ but they cannot be predicted accurately over long periods of time, so they are determined from modern observational techniques (see Chapter 3) and reported by the International Earth Rotation Service (IERS).

In addition to changes that take place in the direction of $\omega _ { e }$ , the magnitude of the vector changes with time. These changes in the magnitude are caused by transfer of angular momentum from atmospheric winds to the solid Earth and by tidal deformations that produce changes in the Earth’s moments of inertia. A change in the angular velocity vector produces a corresponding change in the length of day (LOD), the period required for a complete revolution of the Earth with respect to the stars (but not the Sun). This change in LOD usually is expressed with a parameter using units of time, a form of Universal Time known as $\Delta ( \mathrm { U T } 1 )$ . The variations in LOD, as well as $\Delta ( \mathrm { U T } 1 )$ , are difficult to predict so they are observed regularly and reported by the IERS. In cases that rely on the use of satellite observations, the quantities $x _ { p }$ , $y _ { p }$ , and LOD may be estimated simultanelously with the satellite state.

Although $\Delta ( \mathrm { U T } 1 )$ can, in principle, be estimated with polar motion and satellite state, the separation of $\Delta ( \mathrm { U T } 1 )$ from the orbit node, $\Omega$ , complicates such estimation. Although satellite observations from satellites such as GPS and Lageos have been used to determine both $\Delta ( \mathrm { U T } 1 )$ and $\Omega$ over time scales of a few days, it should be noted that errors in modeling $\Omega$ will be absorbed in the estimation of $\Delta ( \mathrm { U T } 1 )$ . Since modeling the satellite $\Omega$ over very long periods, such as semiannual and longer, is complicated by force model errors from, for example, radiation pressure, artificial satellite observations cannot provide reliable longterm estimates of $\Delta ( \mathrm { U T } 1 )$ .

Time is expressed in different ways. An event can uniquely be identified by the calendar date and time of day, expressed in local time or Universal Time (discussed in a later paragraph). For example, the epoch $J 2 0 O O . O$ is January 1, 2000, 12 hours. The event may be identified by the Julian Date (JD), which is measured from 4713 b.c., but the day begins at noon. The epoch J2000.0 is represented by JD2451545.0. However, January 1, 2000, 0 hours (midnight) is JD 2451544.5. A modified Julian date (MJD) is represented by the JD minus 2400000.5 and the Julian day number is the integral part of the Julian date. Another commonly used expression of time is the day of year (DOY), in which January 1, 2000, would be day 1 of 2000 and February 1, 2000, would be day 32. The general format for the system is DOY followed by hours, minutes, and seconds past midnight.

Time is the independent variable of the equations of motion, Eq. (2.3.46), and the ability to relate the time tag associated with some observation of an aspect of satellite motion to the independent variable is essential for the problem of orbit determination. Observations such as the distance from an instrument to a satellite are described in Chapter 3, but each observation will be time tagged using a reference clock at the tracking station.

A clock requires the repeated recurrence of an event with a known interval. Up until the early part of the twentieth century, the rotation of the Earth served as a clock, but this use was abandoned when evidence mounted that the rotation rate was not uniform. In the modern context, clocks are a particular application of devices that oscillate with specific frequencies. By counting the number of cycles completed over a specified time interval, the oscillator becomes a clock. For example, crystal oscillators abound in modern life (e.g., wristwatches, computers, etc.) The reference frequency of crystal oscillators will change with temperature, for example. Hence, the frequency will exhibit temporal characteristics, usually represented by an offset from “true” time, a drift term and perhaps higher order terms, including stochastic components.

Modern atomic frequency standards, also used as clocks, are classified as rubidium, cesium, and hydrogen maser, given in the order of increasing accuracy and cost. In the case of a cesium frequency standard, a tunable quartz oscillator is used to excite the cesium at the natural frequency of 9,192,631,770 Hz. This frequency is used to define the System International (SI) second. Cesium clocks exhibit high stability, losing about 1 second in 1.5 million years. Hydrogen maser clocks exhibit about an order of magnitude even higher stability.

Various time systems are in use. For Earth satellite applications, the Terrestrial

Table 2.4.1: Difference Between GPS-Time and UTCa   

<table><tr><td colspan="2">Date</td><td>(GPS-T) minus UTC</td></tr><tr><td>(00:00:01 UTC)</td><td></td><td>seconds</td></tr><tr><td>July July 1,</td><td>1, 1981</td><td>1</td></tr><tr><td>July 1,</td><td>1982</td><td>2</td></tr><tr><td>July</td><td>1983</td><td>3</td></tr><tr><td></td><td>1, 1985</td><td>4</td></tr><tr><td> January</td><td>1, 1988</td><td>5</td></tr><tr><td>January</td><td>1, 1990</td><td>6</td></tr><tr><td> January</td><td>1, 1991</td><td>7</td></tr><tr><td>July</td><td>1, 1992</td><td>8</td></tr><tr><td>July July</td><td>1, 1993</td><td>9</td></tr><tr><td></td><td>1, 1994</td><td>10</td></tr><tr><td> January</td><td>1, 1996</td><td>11</td></tr><tr><td>July</td><td>1, 1997</td><td>12</td></tr><tr><td>January</td><td>1, 1999</td><td>13</td></tr></table>

aDates shown are leap second adjustments.

Dynamical Time (TDT) is used as the independent variable in the equations of motion, although Barycentric Dynamical Time (TDB) is used for solar system applications. Both TDT and TDB were related to International Atomic Time (TAI) at a specified epoch. TAI is a time scale based on cesium atomic clocks operated by numerous international agencies. In principle, by averaging over numerous atomic clocks, stochastic variations can be diminished and TAI will be a close approximation of a uniform time scale. TDT has come to be known as Terrestrial Time (TT).

Universal Time is the measure of time that is the theoretical basis for all civil time-keeping. Aside from the previously defined $\Delta ( \mathrm { U T } 1 )$ , Coordinated Universal Time (UTC) is derived from TAI, where $\mathbf { U T 1 } = \mathbf { U T C } + \Delta ( \mathbf { U T 1 } )$ . UTC is maintained by the atomic clocks of various agencies, such as the National Institute of Standards and Time (NIST) and the U.S. Naval Observatory (USNO). The specific time systems are designated UTC(NIST) or UTC(USNO), for example. UTC(USNO) and TAI are based on the ensemble average of several cesium oscillators and hydrogen masers (about 30 cesium and 5–10 hydrogen masers in early 2000). The primary difference between UTC and TAI is the introduction of leap seconds to maintain synchronization between UTC and $\Delta ( \mathrm { U T } 1 )$ to within $\pm 0 . 9$ seconds.

The difference between TAI and TT is, by definition, a constant. The transformation is given by

$$
\mathrm { T T - T A I } = 3 2 . 1 8 4 \mathrm { s e c } .
$$

The transformation between TDB and $\mathrm { T T }$ is a purely periodic function of the position and velocity of the Earth, Moon, planets, and Sun, a relativistic effect. The largest term in this transformation is an annual term with an amplitude of 1.658 milliseconds.

With the introduction of the Global Positioning System (GPS), another time system was introduced. To avoid discontinuities that occur with UTC, GPS-Time (GPS-T) is related to atomic time (maintained by USNO), but the leap second adjustments applied to UTC are not introduced in GPS-T. One of the hydrogen maser clocks at the USNO is used to provide the physical realization of both UTC(USNO) and GPS-T, which is determined from the ensemble average. This clock is steered to UTC(USNO) and is referred to as the Master Clock (MC). The MC is used for both UTC(USNO) and GPS-T. The offsets between GPS-T and UTC are shown in Table 2.4.1. As of January 1, 1999, and until the next leap second, TAI-UTC $= 3 2$ seconds.

In GPS operations, time is measured by GPS-week and time within the week, measured from Sunday midnight. The GPS-week is an integer with the initial week assigned a value of zero, corresponding to January 6, 1980. Since 10 bits were allocated in the GPS broadcast message to the GPS-week, the week number is limited to 1023, which occurred the week of August 15, 1999. After reaching the value of 1023, the week “rolled over” to zero for the week of August 22. Although an ambiguity exists with the uniqueness of the GPS-week as the result of the rollover, resolution of this ambiguity is not a problem for most applications.

References containing more detailed information include Seidelmann (1992) and McCarthy (1996). The latter reference documents the definitions, algorithms, models and constants adopted by the IERS. The document on the “IERS Conventions” is updated every few years.

# 2.4.3 EARTH-FIXED AND TOPOCENTRIC SYSTEMS

Since the Earth is not a rigid body, the concept of an Earth-fix ed reference frame is not precisely defined. As previously noted, the Earth deforms in response to luni-solar gravity, which produces a redistribution of mass. The deformations associated with this redistribution, or tides, produce not only changes in gravity but changes in the coordinates of points on the Earth’s surface. In addition, the Earth’s crust consists of several moving tectonic plates. As a consequence, a relative motion exists between points on different plates. With these considerations, a true Earth-fix ed reference frame does not exist. The selected reference frame must be consistent with the description of the Earth’s rotational characteristics and deformation.

A Terrestrial Reference Frame (TRF) for precision orbit determination is “attached” to the Earth with an origin that is coincident with the center of mass. The $( x , y , z )$ axes are orthogonal and the $z$ axis of this coordinate system is approximately coincident with $\omega _ { e }$ , but it cannot remain coincident because of polar motion. The $x$ axis is usually chosen to be approximately coincident with the Greenwich meridian and the $y$ axis is mutually perpendicular. Specific realizations of the TRF include the IERS TRF, or $I T R F$ , and the TRF commonly used with many GPS applications, referred to as the WGS-84 (World Geodetic System) system. WGS-84 is closely aligned with the ITRF.

With the ITRF, for example, velocities of the observing sites are determined to account for plate motion, including local crustal deformations. To maintain a consistent TRF, these site velocities are determined within a process that defines the ITRF as well as the Earth rotation parameters. ITRF-97 (Boucher et al., 1999) provides the coordinates and velocities for stations participating in the International Space Geodetic Network. The IERS Conventions (McCarthy, 1996) are a useful source of information for the effects of tides on station coordinates.

As defined in Section 2.3.3, spherical coordinates are used to describe the planetary gravitational potential. These spherical coordinates are related to the $( x , y , z )$ coordinates by the following relations:

$$
\begin{array} { r c l } { x } & { = } & { r \cos \phi \cos \lambda } \\ { y } & { = } & { r \cos \phi \sin \lambda } \\ { z } & { = } & { r \sin \phi . } \end{array}
$$

Here the angle $\phi$ is the geocentric latitude, $\lambda$ is the longitude, and $r$ is the magnitude of the position vector, $\mathbf { r }$ . Since an ellipsoid of revolution is a better approximation to the physical topography of the Earth than a sphere, an alternate set of coordinates is used to describe positions on the surface of the ellipsoid, as illustrated in Fig. 2.4.2. This alternate set uses a geodetic latitude, $\phi ^ { \prime }$ , longitude, $\lambda$ , and height above the ellipsoid, $h$ . The relationships between these coordinates and $( x , y , z )$ are

$$
\begin{array} { r c l } { { x } } & { { = } } & { { { \left( N _ { h } + h \right) \cos \phi ^ { \prime } \cos \lambda } } } \\ { { y } } & { { = } } & { { { \left( N _ { h } + h \right) \cos \phi ^ { \prime } \sin \lambda } } } \end{array}
$$

![](images/e016a2c5ca3d1d5db55ccef22cdd26223524d5e925dfafeab28aa33724949ce9.jpg)  
Figure 2.4.2: Geodetic coordinates. Coordinates on the surface of the Earth are usually defined in terms of geodetic latitude, $\phi ^ { \prime }$ , which differs from geocentric latitude, $\phi$ .

$$
\begin{array} { l l l } { z } & { = } & { \left( N _ { h } + h - { \tilde { e } } ^ { 2 } N _ { h } \right) \sin { \phi ^ { \prime } } } \end{array}
$$

where eccentricity of the elliptical cross-section of the ellipsoid is

$$
\begin{array} { c } { { \tilde { e } ^ { 2 } = \tilde { f } ( 2 - \tilde { f } ) , } } \\ { { { } } } \\ { { N _ { h } = \displaystyle \frac { R _ { e } } { ( 1 - \tilde { e } ^ { 2 } \sin ^ { 2 } \phi ^ { \prime } ) ^ { 1 / 2 } } } } \end{array}
$$

and $\tilde { f }$ represents the flattening parameter. The parameter $\tilde { f }$ is defined by

$$
\tilde { f } = \frac { R _ { e } - R _ { p } } { R _ { e } } ,
$$

where $R _ { e }$ is the equatorial radius of the ellipsoid, and $R _ { p }$ is its polar radius. Another useful equation for the ellipsoid is

$$
x ^ { 2 } + y ^ { 2 } + \left( { \frac { R _ { e } } { R _ { p } } } \right) ^ { 2 } z ^ { 2 } = R _ { e } ^ { 2 }
$$

where $( x , y , z )$ are coordinates of a point on the ellipsoid surface. Further geodetic details can be found in Torge (1980). This equation can be a useful constraint to determine the location, for example, of the point where a space-borne instrument boresight pierces the ellipsoid for a specified spacecraft orientation in the ECF.

![](images/739a7da8f44be59da069f8433ea01419172f58d2324e1c094a5340652f584814.jpg)  
Figure 2.4.3: Topocentric coordinates. A useful description of satellite position can be made with topocentric coordinates. The origin is an observer’s position on the surface of the Earth and the topocentric coordinates are defined with $x _ { t }$ directed eastward, $y _ { t }$ northward, and $z _ { t }$ is radial.

For some applications, a coordinate system attached to a point on the surface of the Earth is useful in the description of satellite motion from a ground-based observer’s viewpoint. A topocentric coordinate system can be defined such that $z _ { t }$ is along the local vertical, $x _ { t }$ is eastward, and $y _ { t }$ is northward, as illustrated in Fig. 2.4.3. The position vector of a satellite, for example, in an Earth-fix ed system, $\mathbf { r }$ , can be expressed in the topocentric system as $\mathbf { r } _ { t }$ :

$$
{ \bf r } _ { t } = T _ { t } ( { \bf r } - { \bf r } _ { s } ) = T _ { t } \rho
$$

$$
T _ { t } = \left[ \begin{array} { c c c } { { - \sin \lambda } } & { { \cos \lambda } } & { { 0 } } \\ { { - \sin \phi \cos \lambda } } & { { - \sin \phi \sin \lambda } } & { { \cos \phi } } \\ { { \cos \phi \cos \lambda } } & { { \cos \phi \sin \lambda } } & { { \sin \phi } } \end{array} \right] .
$$

![](images/901fd1e4d995be1be6bcaba359a50ae5643599ca393785dbcf10c5dfb8b04ca5.jpg)  
Figure 2.4.4: Azimuth and elevation. These angles are defined in a topocentric system with azimuth measured eastward from north and elevation measured above the plane tangent to the Earth at the observer’s location.

Where geocentric latitude has been used for simplicity, $\mathbf { r }$ and $\mathbf { r } _ { s }$ are the position vectors of the satellite, and the observer is expressed in the Earth-fix ed system. With the components of satellite position expressed in the topocentric system, $( x , y , z ) _ { t }$ , two commonly used angles can be introduced: azimuth (Az) and elevation (El). These angles are illustrated in Fig. 2.4.4 and can be determined from

$$
\begin{array} { r l r } & { \sin ( \mathrm { E l } ) = \displaystyle \frac { z _ { t } } { r _ { t } } \qquad } & { - 9 0 ^ { \circ } \leq \mathrm { E l } \leq 9 0 ^ { \circ } } \\ & { \sin ( \mathrm { A z } ) = \displaystyle \frac { x _ { t } } { r _ { x y } } } \\ & { \cos ( \mathrm { A z } ) = \displaystyle \frac { y _ { t } } { r _ { x y } } } \end{array}
$$

Where $( \mathbf { A } \mathbf { z } )$ is measured from North in an eastward direction, (El) is measured above (or below) the $( x , y ) _ { t }$ plane (that is, the local tangent plane), and $r _ { x y } =$ $[ x _ { t } ^ { 2 } + y _ { t } ^ { 2 } ] ^ { 1 / 2 }$ . Both sin (Az) and cos (Az) are needed to determine the correct quadrant.

# 2.4.4 TRANSFORMATION BETWEEN ECF AND ECI

If the equations of motion given by Eqs. (2.3.46) and (2.3.47) are expressed in an ECI system, such as the J2000 system, the gravitational force given by Eq. (2.3.18) must be transformed from the Earth-fix ed system used to describe the potential into the J2000 system. For the simplified case of simple ECF rotation about the body-fix ed $z$ axis, the necessary transformation was given in Eq. (2.3.20). In reality, with consideration given to precession, nutation, polar motion, and UT1, the transformation is considerably more complex. If T xyzXY Z represents the transformation matrix from J2000 coordinates to Earth-fix ed, then

$$
\left[ \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right] _ { E C F } = T _ { X Y Z } ^ { x y z } \left[ \begin{array} { l } { X } \\ { Y } \\ { Z } \end{array} \right] _ { E C I }
$$

where the vector components $( X , Y , Z ) _ { E C I }$ represent Earth-centered inertial coordinates (e.g., J2000) and $( x , y , z ) _ { E C F }$ represents the Earth-fix ed components (e.g., ITRF). The transformation matrix can be further decomposed into

$$
T _ { X Y Z } ^ { x y z } = W S ^ { \prime } N P
$$

where the specific components of these matrices and additional details are given in Appendix H. The general purpose of these matrices is

P: applies precession, from a specified epoch to the current time,   
N: applies nutation at the current time,   
$S ^ { \prime }$ : applies the rotation to account for true sidereal time,   
W: applies polar motion to align the $z$ axis (true pole) with the pole of the ECF system.

# 2.5 ORBIT ACCURACY

Different conditions and considerations must be applied to a discussion about orbit accuracy. The term orbit accuracy may refer to the accuracy of the solution of the equations of motion with specified parameters in the model of the forces acting on the satellite. In this case, little consideration is given to the accuracy of the parameters in the equations of motion. Instead the focus is simply on the accuracy of the technique used to solve the nonlinear ordinary differential equations given by Eqs. (2.3.46) and (2.3.47). If a general perturbation technique is used, the concern is usually with the small parameters, such as eccentricity, that are used to expand the forces and facilitate the solution. On the other hand, if a special perturbation technique is used, the concern will be with the step size of the numerical method chosen to solve the equations of motion. In either case, the solution technique is an approximation and will always introduce some error in the solution. To clarify this aspect, the terminology solution technique accuracy refers to the error introduced in the solution of the equations of motion by the solution technique, with no consideration given to the accuracy of the parameters in the equations. The solution technique accuracy can be controlled at different levels. For example, a numerical integration technique can be controlled by the step size and order of the technique.

Since the errors introduced by the solution technique can be controlled at some level, they are seldom the dominant error source. The parameters in the force models as well as the modeling of the forces are usually the most significant error sources. For example, all parameters in the force model have been determined by some means, usually as part of the orbit determination process. As a consequence, all parameters in the equations of motion contain some level of error. Such errors are crucial in the comparison of the solution to the equations of motion to physical measurements of some characteristics of the motion. In some cases, the error source may be embedded in the force modeling. In other words, the force model may be incorrect or incomplete. These errors will be described by the terminology force model accuracy.

In some cases, intentional mismodeling may be introduced to simplify the equations of motion. For example, the simple evaluation of the spherical harmonic terms in the gravitational force will require significantly greater computation time if the representation includes terms to degree and order 180 compared to degree and order 8. In this case, it may be acceptable to introduce a level of spherical harmonic truncation to reduce the computation time, though some error will be introduced into the solution by the omitted terms.

The most important consideration for the orbit accuracy is the specification of a requirement for the accuracy in each application. The requirement may be motivated by a wide variety of considerations, such as sensor accuracy, but the requirement will determine the selection of parameters for the solution technique, the accuracy of the force model parameters, the selection of force models, and the selection of a solution technique. The equations of motion are distinctly different if the orbit of a satellite must be known (and hence determined) with centimeter accuracy versus kilometer accuracy. Depending on these requirements, intentional model simplificat ions may be introduced. Identification of the accuracy to which the orbit must be determined is a vital aspect of the orbit determination problem.

# 2.6 REFERENCES

Barlier, F., C. Berger, J. Falin, G. Kockarts, and G. Thuiller, “A thermospheric model based on satellite drag data,” Annales de Geophysique ´ , Vol. 34, No. 1, pp. 9–24, 1978.

Battin, R., An Introduction to the Mathematics and Methods of Astrodynamics, American Institute of Aeronautics and Astronautics, Reston, VA, 1999.

Beutler, G., E. Brockmann, W. Gurtner, U. Hugentobler, L. Mervart, M. Rothacher, and A. Verdun, “Extended orbit modeling techniques at the CODE Processing Center of the International GPS Service for Geodynamics (IGS): theory and initial results,” Manuscripta Geodaetica, Vol. 19, No. 6, pp. 367–385, April 1994.

Bond, V., and M. Allman, Modern Astrodynamics, Princeton University Press, Princeton, NJ, 1996.

Born, G., J. Mitchell, and G. Hegler, “GEOSAT ERM – mission design,” J. Astronaut. Sci., Vol. 35, No. 2, pp. 119–134, April–June 1987.

Boucher, C., Z. Altamini, and P. Sillard, The International Terrestrial Reference Frame (ITRF97), IERS Technical Note 27, International Earth Rotation Service, Observatoire de Paris, May 1999.

Brouwer, D., “Solutions of the problem of artificial satellite theory without drag,” Astron. J., Vol. 64, No. 9, pp. 378–397, November 1959.

Brouwer, D., and G. Clemence, Methods of Celestial Mechanics, Academic Press, New York, 1961.

Chobotov, V. (ed.), Orbital Mechanics, American Institute of Aeronautics and Astronautics, Inc., Reston, VA, 1996.

Cook, G. E., “Perturba tions of near-circular orbits by the Earth’s gravitational potential,” Planetary and Space Science, Vol. 14, No. 5, pp. 433–444, May 1966.

Danby, J. M. A., Fundamentals of Celestial Mechanics, Willmann-Bell, Inc., Richmond, VA, 1988.

Einstein, A., “Zur Elektrodynamik bewegter Korper,” ¨ Annalen der Physik, Vol. 17, No. 10, pp. 891–921, 1905 (translated to English: Perrett, W., and G. Jeffery, The Principle of Relativity, Methuen and Co., 1923; republished by Dover, New York).

El´Yasberg, P. E., Introduction to the Theory of Flight of Artificial Earth Satellites, translated from Russian, Israel Program for Scientific Translations, 1967.

Fliegel, H., T. Gallini, and E. Swift, “Global Positioning System radiation force models for geodetic applications,” J. Geophys. Res., Vol. 97, No. B1, 559– 568, January 10, 1992.

Goodyear, W. H., “Complet ely general closed form solution for coordinates and partial derivatives of the two-body problem,” Astron. J., Vol. 70, No. 3, pp. 189–192, April 1965.

Heiskanen, W., and H. Moritz, Physical Geodesy, W. H. Freeman and Co., San Francisco, 1967.

Herring, T., B. Buffett, P. Mathews, and I. Shapiro, “Free nutations of the Earth: influence of inner core dynamics,” J. Geophys. Res., Vol. 96, No. B5, pp. 8259–8273, May 10, 1991.

Huang, C., J. C. Ries, B. Tapley, and M. Watkins, “Rel ativistic effects for near-Earth satellite orbit determination,” Celest. Mech., Vol. 48, No. 2, pp. 167– 185, 1990.

Jacchia, L., Thermospheric temperature, density and composition: new models, Special Report 375, Smithsonian Astrophysical Observatory, Cambridge, MA, 1977.

Kaula, W. M., Theory of Satellite Geodesy, Blaisdell Publishing Co., Waltham, 1966 (republished by Dover, New York, 2000).

Kovalevsky, J., I. Mueller, and B. Kolaczek (eds.), Reference Frames in Astronomy and Geophysics, Kluwer Academic Publishers, Dordrecht, 1989.

Lambeck, K., The Earth’s Variable Rotation, Cambridge University Press, Cambridge, 1980.

Lambeck, K., Geophysical Geodesy, Clarendon Press, Oxford, 1988.

Lundberg, J., and B. Schutz, “Recursion formulas of Legendre functions for use with nonsingular geopotential models,” J. Guid. Cont. Dyn., Vol. 11, No. 1, pp. 31–38, January–Februar y 1988.

McCarthy, D. (ed.), IERS Conventions (1996), IERS Technical Note 21, International Earth Rotation Service, Observatoire de Paris, July 1996.

Moritz, H., and I. Mueller, Earth Rotation: Theory and Observation, Ungar Publishing Company, New York, 1987.

Moulton, F. R., An Introduction to Celestial Mechanics, MacMillan Co., New York, 1914.

Newton, I., Philosophiae Naturalis Principia Mathematica, 1687 (translated into English: A. Motte, 1729; revised by F. Cajori, University of California Press, 1962).

Pines, S., “Uniform representation of the gravitational potential and its derivatives,” AIAA J., Vol. 11, No. 11, pp. 1508–1511, November 1973.

Plummer, H. C., An Introductory Treatise on Dynamical Astronomy, Cambridge University Press, 1918 (republished by Dover Publications, New York, 1966).

Pollard, H., Mathematical Introduction to Celestial Mechanics, Prentice-Hall, Englewood Cliffs, NJ, 1966.

Press, W., B. Flannery, S. Teukolsky, and W. Vetterling, Numerical Recipes, Cambridge University Press, Cambridge, 1986.

Prussing, J., and B. Conway, Orbit Mechanics, Oxford University Press, New York, 1993.

Ries, J. C., C. K. Shum, and B. Tapley, “Surf ace force modeling for precision orbit determination,” Geophysical Monograph Series, Vol. 73, A. Jones (ed.), American Geophysical Union, Washington, DC, 1993.

Ries, J. C., C. Huang, M. M. Watkins, and B. D. Tapley, “Orbit determination in the relativistic geocentric reference frame,” J. Astronaut. Sci., Vol. 39, No. 2, pp. 173–181, April–June 1991.

Roy, A. E., Orbital Motion, John Wiley & Sons Inc., New York, 1988.

Schaub, H., and J. Junkins, Analytical Mechanics of Space Systems, American Institute of Aeronautics and Astronautics, Reston, VA, 2003.

Seidelmann, P. K. (ed.), Explanatory Supplement to the Astronomical Almanac, University Science Books, Mill Valley, CA, 1992.

Shampine, L., and M. Gordon, Computer Solution of Ordinary Differential Equations, The Initial Value Problem, W. H. Freeman and Co., San Francisco, 1975.

Smart, W. M., Celestial Mechanics, John Wiley & Sons Inc., New York, 1961.

Standish, E. M., X. Newhall, J. Williams, and W. Folkner, JPL Planetary and Lunar Ephemerides (CD-ROM), Willmann-Bell, Inc., Richmond, VA, 1997.

Szebehely, V., Theory of Orbits, Academic Press, New York, 1967.   
Szebehely, V., and H. Mark, Adventures in Celestial Mechanics, John Wiley & Sons, Inc., New York, 1998.   
Torge, W., Geodesy, Walter de Gruyter, Berlin, 1980 (translated to English: Jekeli, C.).   
Vallado, D., Fundamentals of Astrodynamics and Applications, Space Technology Library, Microcosm Press, El Segundo, CA, 2001.   
Vigue, Y., B. Schutz, and P. Abusali, “Thermal force modeling for the Global Positioning System satellites using the finite element method,” J. Spacecr. Rockets, Vol. 31, No. 5, pp. 866–859, 1994.   
Wahr, J. M., “The forced nutations of an elliptical, rotating, elastic, and oceanless Earth,” Geophys. J. of Royal Astronom. Soc., 64, pp. 705–727, 1981.   
Westfall, R., Never at Rest: A Biography of Isaac Newton, Cambridge University Press, Cambridge, 1980.   
Woolard, E., Theory of the rotation of the Earth around its center of mass, Astronomical Papers—American Ephemeris and Nautical Almanac, Vol. XV, Part I, U.S. Naval Observatory, Washington, DC, 1953.

# 2.7 EXERCISES

1. By differentiating ${ \mathbf { r } } = r { \mathbf { u } } _ { r }$ , derive Eqs. (2.2.8) and (2.2.9). Recall that the derivative of a unit vector in a rotating frame is given by $\dot { \mathbf { u } } = \boldsymbol { \omega } \times \mathbf { u }$ , where $\omega$ is the angular velocity of the rotating frame. In this case, $\omega = { \dot { \theta } } \mathbf { u } _ { h }$ .

2. Determine the orbital period of the following satellites:

(a) Shuttle: $a = 6 , 7 7 8 \mathrm { k m }$ (b) Earth-observing platform (EOS/Terra): $a = 7 , 0 8 3 \mathrm { k m }$ (c) Geodetic satellite (Lageos): $a = 1 2 , 3 0 0 \mathrm { k m }$

3. Determine the semimajor axis from the period for the following:

(a) Geosynchronous $( T = 8 6 , 1 6 4 \mathrm { s e c }$ ) (b) GPS $( T = 8 6 , 1 6 4 / 2$ sec)

4. Given the following position and velocity of a satellite expressed in a nonrotating, geocentric coordinate system:

<table><tr><td></td><td>Position (m)</td><td>Velocity (m/sec)</td></tr><tr><td>X</td><td>7088580.789</td><td>-10.20544809</td></tr><tr><td>Y</td><td>-64.326</td><td>-522.85385193</td></tr><tr><td>Z</td><td>920.514</td><td>7482.07514112</td></tr></table>

Determine the six orbit elements (a, e, i, $\Omega , \omega , \mathbf { M } _ { 0 } ,$ ). Express the angles in degrees.

5. Given the position and velocity in Exercise 4 at $t = 0$ , predict the position and velocity of the satellite at $t = 3 , 0 0 0$ sec, assuming two-body motion. Determine the radial and horizontal components of velocity and the flight path angle at $t = 3 , 0 0 0$ sec. The flight path angle is the angle in the orbit plane between the normal to the position vector and the velocity vector.

6. Determine the latitude and longitude of the subsatellite point for $t = 3 , 0 0 0$ sec in Exercise 5 if $\alpha _ { G }$ at $t = 0$ is zero. Assume the $Z$ axis of the nonrotating system is coincident with the $z$ axis of the rotating system.

7. Determine the node rate and perigee rate due to $J _ { 2 }$ of the Earth for the following satellites:

<table><tr><td>Satellite</td><td>Altitude</td><td>Eccentricity</td><td>Inclination</td></tr><tr><td>Mir</td><td>400 km</td><td>0</td><td>51 deg</td></tr><tr><td>EOS/AM</td><td>705 km</td><td>0</td><td>98 deg</td></tr><tr><td>GPS</td><td>20,000 km</td><td>0</td><td>55 deg</td></tr><tr><td>Geosync</td><td>36,000 km</td><td>0.1</td><td>63 deg</td></tr></table>

(Assume semimajor axis is altitude $^ +$ mean radius of Earth.)

8. Determine the inclination required for a “solar -synchronous” satellite with an altitude of $6 0 0 { \mathrm { k m } }$ (add Earth radius to obtain semimajor axis) and zero eccentricity.

9. Determine the node rate caused by the Sun and Moon for the set of satellites in Exercise 7. Determine the individual luni-solar contributions and the combined effect.

10. In November, 1996, a payload known as Wakeshield (WSF-03) was deployed from Columbia on STS-80. This payload carried a GPS receiver. Using an on-board navigation method, the receiver measurements were processed into position in an Earth-centered, Earth-fix ed coordinate system. The GPS-determined positions for selected times follow.

<table><tr><td colspan="2">WSF-O3 Earth-fx ed Position Determined by GPS WGS-84 Positions in Meters November 24,1996</td><td rowspan="2">00:00:03.000000</td></tr><tr><td>GPS-T (hrs:min:sec)</td><td>00:00:0.000000</td></tr><tr><td>x</td><td>3325396.441</td><td>3309747.175</td></tr><tr><td>y</td><td>5472597.483</td><td>5485240.159</td></tr><tr><td>2</td><td>-2057129.050</td><td>-2048664.333</td></tr><tr><td></td><td></td><td></td></tr><tr><td colspan="3">November 25,1996</td></tr><tr><td>GPS-T (hrs:min:sec)</td><td>00:00:0.000000</td><td>00:00:03.000000</td></tr><tr><td>x</td><td>4389882.255</td><td>4402505.030</td></tr><tr><td>y</td><td>-4444406.953</td><td>-4428002.728</td></tr><tr><td>2</td><td>-2508462.520</td><td>-2515303.456</td></tr></table>

(a) Use these positions to demonstrate that the WSF-03 node location is not fixed in space and determine an approximate rate of node change (degrees/day) from these positions. Compare the node rate with the value predicted by Eq. (2.3.31). (Hint: Determine the node location in the first 3 sec and the last 3 sec. Also, recall that for two-body dynamics, the position vectors at two times will define the orbit plane.)

(b) Determine the inclination of WSF-03 during the first 3-sec interval and the last 3-sec interval. (Hint: Assume two-body dynamics applies during these respective 3-sec intervals.)

Comment: The position vectors determined by GPS in this case are influenced at the 100-meter level by Selective Ability, but the error does not significantly affect this problem.

11. Assuming an Earth satellite is influenced by $J _ { 2 }$ only, derive the equations of motion in nonrotating coordinates. Assume the nonrotating $Z$ axis coincides with the Earth-fix ed $z$ axis.

12. Using the result of Exercise 11, numerically integrate the equations of motion for one day with the following initial conditions for a high-alititude, GLONASS-like satellite:

a 25500.0 km e 0.0015 i 63 deg $\Omega$ −60 deg $\omega$ 0 deg ${ { \bf { M } } _ { 0 } }$ 0 deg

(a) During the integration, compute the Jacobi constant and the $Z$ component of the angular momentum. Are these quantities constant?   
(b) Plot the six orbit elements as a function of time.   
(c) Identify features that are similar to and different from Fig. 2.3.5 for the Shuttle.   
(d) Compare the node rate predicted by Eq. (2.3.31) with a value estimated from (b).   
(e) Compare the amplitude of the semimajor axis periodic term with Eq. (2.3.34).   
(f) Plot the ground track. Does the ground track repeat after one day?

13. Using Fig. 2.3.5, estimate the mean values of $a , e$ , and $i$ and the linear rates of node and perigee change. Compare the estimated node and perigee rates with the rates predicted by Eqs. (2.3.31) and (2.3.32).

14. For the orbit of the TOPEX/Poseidon, assume the ECF frame rotates with a constant rate $\omega _ { e }$ about the $z$ axis and the initial osculating elements are:

$$
\begin{array} { l l l } { { a } } & { { } } & { { 7 7 1 2 \mathrm { k m } } } \\ { { e } } & { { } } & { { 0 . 0 0 0 1 } } \\ { { i } } & { { } } & { { 6 3 . 4 ^ { \circ } } } \\ { { \Omega } } & { { } } & { { 1 3 5 ^ { \circ } } } \\ { { \omega } } & { { } } & { { 9 0 ^ { \circ } } } \\ { { M _ { 0 } } } & { { 0 } } & { { } } \end{array}
$$

(a) Use the $J _ { 2 }$ result of Exercise 11 to numerically integrate the equations of motion for one day.   
(b) Compare the numerical results with results from the analytical theory in Appendix E. Note that errors in the analytical theory are of the order $e J _ { 2 }$ and $J _ { 2 } ^ { 2 }$ .

15. Using the gravitational potential in Eq. (2.3.12), derive

$$
{ \frac { \partial U } { \partial r } } , \quad { \frac { \partial U } { \partial \phi } } , \quad \mathrm { a n d } \ { \frac { \partial U } { \partial \lambda } } .
$$

Derive a recursive relation for

$$
\frac { \partial P _ { \ell m } } { \partial \phi } .
$$

16. With the initial conditions from Exercise 12 or 14, derive the equations of motion in both the ECF and ECI with all gravity coefficient s through degree and order 3. Numerically integrate for 10 days both ECF (Eq. 2.3.22) and ECI (Eq. 2.3.23) and compute the Jacobi integral for both cases. Assume the Earth rotates with constant angular velocity (neglect polar motion, $\Delta$ (LOD), precession, and nutation). Assume the Greenwich meridian coincides with the vernal equinox at $t = 0$ .

(a) Assess the numerical integration accuracy from the Jacobi integral. (b) Compare the ECF and ECI position results by applying an appropriate transformation into a common coordinate system.

17. Determine the contributions from the Moon and the Sun to the precession of the equinoxes using Eq. 2.4.2. Compare the combined luni-solar rate with the observed rate of $- 5 0 . 2 5$ arcsec/yr. Note that the polar moment of inertia of the Earth is $8 . 1 2 \times 1 0 ^ { 4 4 } ~ \mathrm { g ~ c m ^ { 2 } }$ , the semimajor axis of the Moon’s orbit is $3 8 4 , 0 0 0 \ \mathrm { k m }$ , and for the Sun $a = 1 4 9 , 5 9 9 , 0 0 0 { \mathrm { k m } }$ $\sim 1$ Astronomical Unit).

18. Determine the secular change in semimajor axis (in m per day) for a balloonlike satellite $( A / m = 1 0 ~ \mathrm { m ^ { 2 } ~ k g ^ { - 1 } } ,$ ) at an altitude of $6 0 0 ~ \mathrm { k m }$ , with atmospheric density $\rho = 5 \times 1 0 ^ { - 1 3 } \mathrm { k g \ m ^ { - 3 } }$ . Compare the result to a geodetic satellite with $A / m = 0 . 0 0 1 { \mathrm { m } } ^ { 2 } { \mathrm { k g } } ^ { - 1 }$ . Assume $C _ { D } = 2$ for both cases.

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

![](images/a25f4487347f1aff2165dd7c6b986bd7ef863a77d2595be3cc7e257ec5a9a8fe.jpg)  
Figure 3.2.1: Portion of shuttle ground track from Fig. 2.2.6. The two orbital revolutions in the vicinity of simulated tracking stations at EI (Easter Island) and FZ (Fortaleza) produce two passes that are within view of the stations. However, the satellite in Pass 1 at Fortaleza rises above the horizon by less than $5 ^ { \circ }$ in elevation.

If the initial conditions in Example 2.2.6.2 represent the true initial conditions, and the set given by Example 2.2.4.1 are used as a nominal or reference set, a residual can be formed as the observed minus computed, or $o$ minus $C \left( O - C \right)$ . Within the context of orbit determination applications, the true initial conditions are unknown, but the observations represented by the ranges in Fig. 3.2.2 are the result of the true state and the measuring instrument characteristics. Usually, a nominal set of initial conditions are available but they deviate from the true values. Nevertheless, based on the nominal initial conditions, a computed range can be formed. The resulting residuals for the three passes are shown in Fig.

![](images/408ea2474097e6bb85dc8e5ea4a157c1cc5f45aa909c1a9f95c2368321ac06ad.jpg)

![](images/372ca48e8124fc9b289ff4c6a9ad5ce1a3c60c158ba9e3f9614dec1324540602.jpg)  
Figure 3.2.2: Simulated range vs time. These plots show the geometric range vs time measured by the two sites, Easter Island and Fortaleza, shown in Fig. 3.2.1.   
Figure 3.2.3: Simulated range-rate vs time.

3.2.5. It has been assumed that all ranges are instantaneous and no atmospheric delays have been included in these simulations. In essence, the residuals in Fig. 3.2.5 illustrate how the orbit differences of Fig. 2.2.9 are exhibited in terms of range residuals from ground-based stations.

Consider the residual, $O - C$ , for the second pass from Easter Island. As shown in the sky plot for this pass in Fig. 3.2.4, the satellite passes nearly overhead, with a maximum elevation of about $7 8 ^ { \circ }$ . When the satellite rises above the Easter Island horizon in the west, the measured range re ects a signi cant component in the along-track direction. As described in Section 2.2.6.2, the position on the true orbit trails the position on the nominal orbit in the along-track direction. It follows that the true range will be longer than the range to the reference position. As a consequence, the orbit differences shown in Fig. 2.2.9 will result in $( O - C ) > 0$ at satellite rise, but $( O - C ) < 0$ when the satellite sets at the observing station’s horizon. At some point during the pass over the station, the satellite motion will be perpendicular to the observer’s viewing direction, so none of the along-track differences will be seen ; that is, $O$ goes to zero. If the pass has a lower elevation, the basic characteristics are the same, as shown for the low-elevation Fortaleza pass in Fig. 3.2.5.

# 3.3 CONCEPTUAL MEASUREMENT SYSTEMS

# 3.3.1 RANGE

All measurements of range are based on the time-of- ight principle. Simply stated, an instrument transmits a signal, usually with some appropriate time duration, which is re ected by a passive target or retransmitted by an active target. A two-way range may originate with an instrument located on the surface of the Earth, or ground-based instrument, and the signal will travel to the satellite and back to the transmitting site. One example of a two-way instrument is the satellite laser ranging (SLR) hardware, which is described in Section 3.5.2. In the SLR measurement, a laser pulse travels on an uplink path to the satellite, where it is re ected. The downlink path takes the signal from the satellite back to the transmitting site. The uplink and downlink paths constitute the two-way measurement. Some two-way range measurements may be transmitted and received at the same location by essentially the same instrumentation, but others may use a transmitter at one location and a receiver at another. This latter case is sometimes referred to as a three-way measurement, in spite of only uplink and downlink paths in the measurement. In some communities, the term $b i$ -static measurement may be used.

The one-way range is based on the transmittal of a signal by a satellite or a ground-based transmitter that is received by separate instrumentation. If the transmit source is within the satellite, the signal may travel only a downlink path.

![](images/7c6c8c4cd498f671e36612336a6dee067fcaed4380c818ab6bb8d790dc26bf7f.jpg)  
Figure 3.2.4: Sky plots. These plots illustrate the azimuth and elevation for the three passes shown in the ground track of Fig. 3.2.1. The circles represent increments of $3 0 ^ { \circ }$ elevation, with the outermost circle at $0 ^ { \circ }$ elevation and the center of the circles at $9 0 °$ elevation. Azimuth is measured clockwise from north.

Alternatively, the transmitter could be ground-based, and the signal might be received by satellite-borne instrumentation on the uplink path. An important example of the satellite-borne transmitter is the Global Positioning System (GPS), discussed in Section 3.5.1. Even in the case of GPS, the receiver could be located on a satellite, rather than being ground-based.

# One-Way Range

Assume a signal of very short duration is transmitted with a specific electromagnetic frequency at time $t _ { T }$ . The transmitted signal propagates along a path and arrives at a point instrumented to receive the transmitted signal. The signal arrives at the receiver at time $t _ { R }$ . Since the signal travels at the speed of light, denoted by $c$ , the signal has traveled a one-way distance given by

![](images/eace288fb7a75e6e220f4b36cc78f7307369e7e3fa1732a3d9e08edc277f78b7.jpg)  
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

![](images/f04dced259776fa4a516bc7fd41f8bc464c2d07e3ea340befbf656b31a0eeb59.jpg)  
Figure 3.5.1: Block II GPS satellite. The satellite solar panels rotate about the axis mounted perpendicular to the main body (spacecraft bus) and the transmit antenna array, shown with the helical windings in the center, is directed toward the Earth’s center. The antenna transmit pattern encompasses the visible Earth. A body-fix ed set of axes includes a $y$ axis coincident with the solar panel axes and a $z$ axis directed toward the Earth’s center. The spacecraft can present the maximum cross-sectional area of the solar panels to the Sun by rotating the bus about the $z$ axis (yaw) and rotating the solar panels about the $y$ axis.

The PRN codes currently transmitted by the GPS satellites are:

• C/A (Coarse Acquisition): This code uses 1023 bits and repeats every 1 ms. The algorithm for generating the sequence is described in detail by Hofmann-Wellenhof et al. (1997). Each bit requires about 1 microsec for transmission or about 300 meters in distance. One major purpose of this code is to facilitate acquisition of the P-code, which is a much longer bit sequence. Since the C/A code repeats every millisecond, an ambiguity exists between each millisecond interval. In other words, there is no information about absolute time within the C/A code. Resolving this ambiguity to determine the correct time interval requires additional information (e.g., information broadcast by the GPS satellites about their position).

• P (Precise): This code has a much longer duration of 37 weeks before it repeats. But this long repeat interval is divided into one week segments and each segment is assigned to a specific GPS satellite. Each satellite, in turn, repeats its assigned code each week. The duration for each bit is the equivalent of 30 meters in distance, corresponding to a transmission rate of $1 0 . 2 3 \times 1 0 ^ { 6 }$ bits per sec. All information about the P-code is readily available. Most receivers use the C/A code for initial acquisition, then transition to the P-code. Since the P-code within each satellite does not repeat for one week, direct cross-correlation without use of the C/A code is challenging. Direct P-code acquisition is easier if the receiver has an accurate clock.

• Y: This code is generated from the P-code, but a classified code (W-code) is used to mix with the P-code. This mixing produces an encrypted P-code. When the Y-code is being transmitted, it is said that Anti-Spoofing (AS) has been invoked. The terminology arises from the military consideration that an adversary could transmit false P-code signals to confuse, or spoof, a receiver. When AS is used, the classified Y-code avoids this possibility.

In the GPS satellites known as Block II, including Block IIA and Block IIR, the $\mathrm { C } / \mathrm { A }$ code is transmitted only on $L _ { 1 }$ and the P/Y codes are transmitted on both $L _ { 1 }$ and $L _ { 2 }$ . As a consequence, receivers capable of operating with only C/A are single-frequency receivers. Without the second frequency, the ionosphere correction cannot be made as accurately as measurements obtained with two frequencies, since it must rely on less accurate ionosphere models. Modern dualfrequency receivers are available that may be capable of correlating directly with the Y-code or they may use signal processing techniques, such as cross-correlation of the Y-code on the two frequencies to obtain the ionosphere delay. The method based on advanced signal processing effectively provides a dual-frequency measurement without knowledge of the Y-code. A pseudo-measurement usually is created by adding the measured ionosphere delay to the C/A pseudorange.

![](images/219f5f8760d6d4a9606583b3290c918faf0b628b345a6bf8639209d2c16acb3e.jpg)  
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