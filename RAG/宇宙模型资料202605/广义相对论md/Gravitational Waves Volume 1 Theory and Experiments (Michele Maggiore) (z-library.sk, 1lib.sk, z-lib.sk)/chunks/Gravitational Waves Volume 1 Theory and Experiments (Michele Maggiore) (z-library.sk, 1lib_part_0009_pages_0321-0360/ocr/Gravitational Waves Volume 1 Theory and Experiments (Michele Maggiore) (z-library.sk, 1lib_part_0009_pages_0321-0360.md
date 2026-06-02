precision is so good that it is possible to assign unambiguously a puls number to each pulse,even after long periods in which observations hav not been made; in particular, the Arecibo telescope was closed,for majd upgrades,for various years in the mid 199Os,and still we know exactl how many pulses elapsed during that time,until observations resumed This is quite remarkable if we consider that,with a rotation period d $5 9 ~ \mathrm { m s }$ ，in one year there are about $5 \times 1 0 ^ { 8 }$ pulses! It is this stability d the integrated profile that allows pulsars to be extraordinarily accurat clocks.

Even if a pulsars were,intririsically,a perfect clock,the TOAs of th pulses in a earthbound laboratory will still be modulated by a numbe of time-dependent factors,due to the motion of the Earth around th Sun (and of the Sun around the solar system barycenter) and also b general-relativistic effects due to the gravitational field of the solar sys tem.Furthermore,if a pulsar isa member of a binary system,the pulse will be similarly modulated bythe motion of the pulsar around its com panion,and by the strong gravitational fields of the two stars.Thes timing residuals,i.e. these modulations of the TOAs with respect to perfectly periodic pattern,are & rich source of information,because they can be computed and depend dn parameters of the binary system,sucl as the masses of the two stars,and therefore the measurement of th timing residual can allow us todetermine these parameters. In the nex subsections we will see how td compute this “timing formula",whicl takes into account all relevant corrections.

![](images/3656b5ea307ae28c00f5d6e9683fc922496032be0473ebe9ab555c729282685b.jpg)  
Fig.6.3 The $( x , y )$ plane is the plane of the orbit of the Earth around the Sun.The angle $\lambda$ isthe ecliptic longitude of the pulsar.

# 6.2.2 Roemer,Shapirb and Einstein time delays

We consider a pulsar that emitsa sequence of pulses,and we discuss frs how the time of arrival of these pulses is modified by the motion of th Earth,and by the effect of the gravitational field of the solar system o electromagnetic waves.We will then see how these time of arrivals an affected if the pulsar is member of a binary system.Following a nomen clature originally introduced by Damour and Deruelle,we will split th corrections into three separate contributions,the Roemer,Shapiro and Einstein time delays.

# Roemer time delay

Since light takes about 50O s totravel from the Sun to the Earth,therei an annual modulation of the tine of arrivals.For instance,for a pulsal which is lying in the plane of the ecliptic,at ecliptic longitude $\lambda$ W see from Fig.6.3 that this modulation is $\Delta _ { R , \odot } = t _ { 0 } \cos ( \Omega t - \lambda )$ where $\Omega$ is the angular velocity of the Earth around the Sun, $t _ { 0 }$ is the trave time from the Sun to the Earth,and for simplicity we assumed a circular orbit.So,when the Earth is in the direction of the pulsar, $\Omega t - \lambda = 0$ the pulse arrives earlier,by an amount $t _ { 0 }$ ，and when it is on the opposite side of the orbit, $\Omega t - \lambda = \pi ,$ it arrives later by an amount $t _ { 0 }$ with respect to the arrival time at the Sun. This is called the Roemer tim delay.4 The subscript $R$ in $\Delta _ { R , \odot }$ stands for Roemer,while $\odot$ reminds that this is a correction due to the motion of the observer,in the Solar System,and not to the intrinsic motion of the source.

If, rather than lying on the plane of the ecliptic,the pulsar has an ecliptic latitude $\beta$ ,the modulation is instead

$$
\begin{array} { r } { \Delta _ { R , \odot } = t _ { 0 } \cos ( \Omega t - \lambda ) \cos \beta . } \end{array}
$$

Its amplitude is maximum for pulsarslin the ecliptic plane, $\cos { \beta } = 0$ ， and vanishes for pulsars in the direction of the poles of the ecliptic. A variation $\delta \lambda , \delta \beta$ in the angles induces a variation of $\Delta _ { R , \odot }$ ，given by

$$
\delta ( \Delta _ { R , \odot } ) = t _ { 0 } \delta \lambda \sin ( \Omega t - \lambda ) \cos \beta + t _ { 0 } \delta \beta \cos ( \Omega t - \lambda ) \sin \beta .
$$

With a resolution $\delta t = 0 . 2 \ : \mathrm { m s }$ on the artival times of the pulses,and taking for definiteness an average angle $\beta \sim 4 5 ^ { 0 }$ ,s0 $\sin \beta = \cos \beta = 1 / \sqrt { 2 }$ ， we get an accuracy on the angles of order $\delta \lambda \sim \delta \beta \sim \sqrt { 2 } \delta t / t _ { 0 } \sim$ $5 . 6 \times 1 0 ^ { - 7 } \mathrm { r a d } \simeq 0 . 1$ arcsec. Such an acceuracy can be suffcient to search for an optical counterpart. This is an example of the fact that the modulation of the originally periodic signal contains very useful information.

Actually,for pulsar timing we will need in general a better precision, so the orbit of the Earth cannot be approximated as circular.We must also take into account the rotation of the Earth around its axis,which for an Earth-bound laboratory introduces a daily modulation with an amplitude $R _ { \oplus } / c \simeq 2 1$ ms,and we must even include the motion of the Sun around the solar system barycenter (which is determined primarily by the influence of Jupiter on the Sun,\$o that the solar system barycenter lies just outside the surface of the $\mathbb { S } \mathrm { u n } \backslash$ 1.The most practical way to take into account these corrections is to refer allarrival times to the solar system barycenter (SSB). Let $\mathbf { r } _ { \mathrm { { o e } } }$ be the vector from the observer to the center of the Earth, $\mathbf { r } _ { \mathrm { e s } }$ from the center of the Earth to the center of the Sun,and $\mathbf { r } _ { \mathrm { s b } }$ from the center of the Sun to the SSB.Then the distance from the observer to the SSB is ${ \bf r } _ { \mathrm { o b } } = { \bf r } _ { \mathrm { 0 e } } + { \bf r } _ { \mathrm { e s } } + { \bf r } _ { \mathrm { s b } }$ and,to obtain the barycentric times of arrival,we must add to the times observed in the laboratory the quantity

$$
\Delta _ { R , \odot } = - \mathbf { r } _ { \mathrm { o b } } \cdot \hat { \mathbf { n } } / c ,
$$

where $\hat { \bf n }$ is the unit vector from the $\mathrm { S S B }$ to the pulsar. The vectors $\mathbf { r } _ { \mathrm { o e } }$ ， $\tilde { \tau } _ { \mathrm { e s } }$ and $\mathbf { r } _ { \mathrm { s b } }$ are known with suffcient aceuracy (for $\mathbf { r } _ { \mathrm { e s } }$ it is also necessary to include the motion of the barycenter of the Earth-Moon system),so we can get $\hat { \bf n }$ from a measure of $\Delta _ { R , \odot }$ ·

It should be remarked that the barycentric time of arrival so obtained are just a useful, but fictitious,intermediate quantity in our computation. The real time of arrival of the pulses at the SSB is also affected by other effects,such as the propagation f light in the gravitational feld of the solar system and its interaction with the interstellar medium,as we will discuss below.

4 After the Danish astronomer Ole Roemer who,in 1675,from the observation of Jupiter's moons,formulated the hypothesis that light travels at a finite speed. At that time the four largest moons of Jupiter were first observed when Jupiter is“in opposition”,i.e. when the Earth passes between Jupiter and the Sun,since then Jupiter is high in the night sky and therefore easier to observe,and the times of the eclipses and passages (i.e. the passings of the moons behind and in front of Jupiter) could be predicted precisely. Later the moons of Jupiter were observed when the Earth was on the opposite side of the Sun from Jupiter,and it was found that the eclipses were consistently late by about 20 minutes.This led Roemer to the hypothesis that light propagates at a finite speed.His estimate for the speed of light was $2 1 4 ~ 0 0 0 ~ \mathrm { k m / s }$

# Shapiro time delay

The above computation of the Roemer delay neglected the genera relativistic effects of the gravitational field of the solar system on tl propagation of light. To take it into account we recall,from eq. (5.1l that the space-time interval geherated by a weak and nearly static New tonian source can be written,to linear order in the metric perturbatid $\phi$ ，as

$$
d s ^ { 2 } = - [ 1 + 2 \phi ( { \bf x } ) ] c ^ { 2 } d t ^ { 2 } + [ 1 - 2 \phi ( { \bf x } ) ] d { \bf x } ^ { 2 } .
$$

In the solar system, $| \phi ( \mathbf { x } ) |$ is at most of order $1 0 ^ { - 6 }$ ,and the weak-fell approximation is excellent.Photons travel along the light-like geodesi $d s ^ { 2 } = 0$ ,so to lowest order in $\dot { \phi }$ ，

$$
c d t = \pm [ 1 - 2 \phi ( { \bf x } ) ] | d { \bf x } | .
$$

If we denote by $\mathbf { r } _ { p }$ the (fixed) position of the pulsar,and by $\mathbf { r } _ { \mathrm { { o b s } } }$ th position of the observer at the arrival time $t _ { \mathrm { o b s } }$ ，then the coordinatl time difference,between the arrival time $t _ { \mathrm { o b s } }$ at the observer and th emission time at the pulsar $t _ { e }$ is

$$
\begin{array} { l } { { \displaystyle c \big ( t _ { \mathrm { o b s } } - t _ { e } \big ) = \int _ { \mathbf { r } _ { \mathrm { o b s } } } ^ { \mathbf { r } _ { p } } \big \vert d \mathbf { x } \big \vert \left[ 1 - 2 \phi ( \mathbf { x } ) \right] } \ ~ } \\ { { \displaystyle ~ = \vert \mathbf { r } _ { p } - \mathbf { r } _ { \mathrm { o b s } } \vert - 2 \int _ { \mathbf { r } _ { \mathrm { o b s } } } ^ { \mathbf { r } _ { p } } \big \vert d \mathbf { x } \big \vert \phi ( \mathbf { x } ) } . } \end{array}
$$

We write

$$
\begin{array} { r l } { \left| \mathbf { r } _ { p } - \mathbf { r } _ { \mathrm { { o b s } } } \right| = \left| ( \mathbf { r } _ { p } - \mathbf { r } _ { b } ) + ( \mathbf { r } _ { b } - \mathbf { r } _ { \mathrm { { o b s } } } ) \right| } & { } \\ { \simeq \left| \mathbf { r } _ { p } - \mathbf { r } _ { b } \right| + ( \mathbf { r } _ { b } - \mathbf { r } _ { \mathrm { { o b s } } } ) \cdot \hat { \mathbf { n } } , } & { } \end{array}
$$

where $\mathbf { r } _ { b }$ is the position of the SSB, $\hat { \bf n }$ is the unit vector from the SSB to the pulsar, i.e. $\hat { \mathbf { n } } = ( \mathbf { r } _ { p } - \left| \mathbf { r } _ { b } \right. / \left| \mathbf { r } _ { p } - \mathbf { r } _ { b } \right|$ ， and the expansion in th second line is valid because $\left| \mathbf { r } _ { p } - \mathbf { r } _ { b } \right| \gg \left| \mathbf { r } _ { b } - \mathbf { r } _ { \mathrm { { o b s } } } \right|$ .Therefore,denoting $\mathbf { r } _ { b } - \mathbf { r } _ { \mathrm { { o b s } } } \equiv \mathbf { r } _ { \mathrm { { o b } } } ,$

$$
t _ { \mathrm { o b s } } \simeq \left( t _ { e } + \frac { 1 } { c } | \mathbf { r } _ { p } - \mathbf { r } _ { b } | \right) + \frac { 1 } { c } \mathbf { r } _ { \mathrm { o b } } \cdot \hat { \mathbf { n } } - \frac { 2 } { c } \int _ { \mathbf { r } _ { \mathrm { o b s } } } ^ { \mathbf { r } _ { p } } | d \mathbf { x } | \phi ( \mathbf { x } ) .
$$

The term $t _ { e } + | { \bf r } _ { p } - { \bf r } _ { b } | / c$ is thebarycentric time of arrival, $t _ { \mathrm { S S B } }$ ,defined as the (fictitious) time at which the pulse would arrive at the SSB i there were no effect of the gravity of the solar system. Then we get

$$
t _ { \mathrm { S S B } } = t _ { \mathrm { o b s } } - \frac { 1 } { c } { \bf r } _ { \mathrm { { o b } } } \cdot \hat { \bf n } + \frac { 2 } { c } \int _ { { \bf r } _ { \mathrm { o b s } } } ^ { { \bf r } _ { p } } \left| d { \bf x } \right| \phi ( { \bf x } ) .
$$

The first correction is just the Roemer time delay that we already found in eq.(6.8)． The second term,which takes into account the effect om light propagation due to the gravitational potential of the solar system is called (minus) the solar system Shapiro time delay,

$$
\Delta _ { S , \odot } = - \frac { 2 } { c } \int _ { { \bf r } _ { \mathrm { o b s } } } ^ { { \bf r } _ { p } } \left. d { \bf x } \right. \phi ( { \bf x } ) ,
$$

s0

$$
t _ { \mathrm { S S B } } = t _ { \mathrm { o b s } } + \Delta _ { R , \odot } - \Delta _ { S , \odot } .
$$

The Shapiro time delay is dominated by the gravitational field of the Sun.To compute it,we consider a photon emitted by the pulsar,which reaches the observer on the Earth when the pulsar-Sun-Earth angle has the value $\theta$ ,see Fig.6.4.Let $P$ be a generic point on the straight-line trajectory made by the photon,and denote by $\rho$ the distance of $P$ from the Earth and by $r$ its distance from the Sun.If $r _ { \mathrm { e s } } ~ = ~ 1$ au is the distance between the Earth and the Sun,we see from the figure that

ie.

$$
\begin{array} { r l } & { r ^ { 2 } = ( r _ { \mathrm { e s } } + \rho \cos \theta ) ^ { 2 } \bigg + ( \rho \sin \theta ) ^ { 2 } , } \\ & { } \\ & { r = r _ { \mathrm { e s } } ( u ^ { 2 } + 1 + 2 u \cos \theta ) ^ { 1 / 2 } , } \\ & { \vdots _ { \mathrm { m o n } ~ \not \sim ~ ( 1 ~ / \alpha ^ { 2 } ) / ~ \mathrm { C } } \kappa u ~ , } \end{array}
$$

where $u = \rho / r _ { \mathrm { e s } }$ Since $\phi = ( 1 / c ^ { 2 } ) ( - G { \cal M } _ { \odot } / r )$ ,we have

$$
\begin{array} { l } { \displaystyle \Delta _ { S , \odot } = \frac { 2 G M _ { \odot } } { c ^ { 3 } } \int _ { 0 } ^ { d } \frac { d \rho } { r } } \\ { = \frac { 2 G M _ { \odot } } { c ^ { 3 } } \int _ { 0 } ^ { \bar { u } } \frac { d u } { ( u ^ { 2 } + 1 + 2 u \cos \theta ) ^ { 1 / 2 } } , } \end{array}
$$

where $\bar { u } = d / r _ { \mathrm { e s } }$ ,and $d$ is the Earth-pulsar distance.It is convenient to add and subtract the delay at a given angle,say when $\cos \theta = 0$ ，S0

$$
\begin{array} { l } { \displaystyle \Delta _ { S , \odot } = \frac { 2 G M _ { \odot } } { c ^ { 3 } } \int _ { 0 } ^ { \bar { u } } \frac { d u } { ( u ^ { 2 } + 1 ) ^ { 1 / 2 } } \eqno ( 6 . } \\ { \displaystyle \qquad + \frac { 2 G M _ { \odot } } { c ^ { 3 } } \int _ { 0 } ^ { \bar { u } } d u \left[ \frac { 1 } { ( u ^ { 2 } + 1 + | 2 u \cos \theta ) ^ { 1 / 2 } } - \frac { 1 } { ( u ^ { 2 } + 1 ) ^ { 1 / 2 } } \right] . } \end{array}
$$

The term in thefirst lineis a fixed quantity which, for $d / r _ { \mathrm { e s } }$ large, grows logarithmically,

$$
\begin{array} { r } { \frac { 2 G M _ { \odot } } { c ^ { 3 } } \displaystyle \int _ { 0 } ^ { \bar { u } } \frac { d u } { ( u ^ { 2 } + 1 ) ^ { 1 / 2 } } = \frac { 2 G M _ { \odot } } { c ^ { 3 } } \mathrm { a r c s i n h } ( \bar { u } ) } \\ { \simeq \frac { 2 G M _ { \odot } } { c ^ { 3 } } \log ( 2 d / r _ { \mathrm { e s } } ) . } \end{array}
$$

This is a constant shift that simply adds up to the total travel time from the pulsar to the SSB. The term in the second line is more interesting from our purposes,since it depends on $\lvert \theta$ ,and therefore on the position f the Earth in its orbit around the SSB.In the integral in the second line of eq.(6.2O) we can take the limit $\bar { u } = d / r _ { \mathrm { e s } } \to \infty$ .The integral converges and gives

$$
\int _ { 0 } ^ { \infty } d u \left[ \frac { 1 } { ( u ^ { 2 } + 1 + 2 u \cos \theta ) ^ { 1 / 2 } } - \frac { 1 } { ( u _ { \scriptscriptstyle } ^ { 2 } + 1 ) ^ { 1 / 2 } } \right] = - \log ( 1 + \cos \theta ) .
$$

Thus, we get

$$
\Delta _ { S , \odot } = { \frac { 2 G M _ { \odot } } { c ^ { 3 } } } \log \left( { \frac { 2 d } { r _ { \mathrm { e s } } } } \right) - { \frac { 2 G M _ { \odot } } { c ^ { 3 } } } \log ( 1 + \cos \theta ) .
$$

![](images/50fa950d718047f809640912f38750f2d966680ff2160566c0d85bfce5fa49ef.jpg)  
Fig.6.4 The geometry for the computation of the Shapiro delay discussed in the text.

![](images/b20c2bb2fe253b9a82a5e6549c53c8bb8d70da58439e6047f29d863cdfc5dbd4.jpg)  
Fig.6.5 The function $f ( \theta )$ = $- \log ( 1 + \cos \theta )$ ,against $\theta$

A plot of the function $- \log ( 1 + \cos \theta )$ is shown in Fig. 6.5. Observe th $\Delta _ { S , \odot }$ formally divergeswhen $\theta = \pi$ ，that is,when the signal crosses t center of the Sun before reaching the Earth.However,of course, divergence is fictitious,first of all because in this case the signal is simp absorbed by the Sun and second,because the Newtonian potential the Sun is $- G M / r$ only outside the Sun,so the result is valid onlyi photons that at most graze the surface of the Sun.

Recalling that $2 G M _ { \odot } / c ^ { 2 } \equiv | R _ { S , \odot } \simeq 3 $ km is the Schwarzschild radm of the Sun,we see that the time-scale of the solar system Shapiro deli is given by the time that light takes to go across a distance $R _ { S , \odot }$ is,about $1 0 \mu \mathrm { s }$ ,which howeverismultiplied by large logarithmic facton In particular,for a pulse which is just grazing the surface of the $\ S _ { \parallel }$ $\theta = \theta _ { \mathrm { g r a z i n g } } \simeq \pi - ( R _ { \odot } / r _ { \mathrm { e s } } )$ ，sc $1 + \cos \theta \simeq ( 1 / 2 ) ( R _ { \odot } / r _ { \mathrm { e s } } ) ^ { 2 }$ .Then th maximum modulation induced by the Shapiro delay,i.e.the differem between its value for a pulse which is just grazing the Sun and its vali at $\theta = 0$ is

$$
\begin{array} { r } { \Delta _ { S , \odot } ( \theta = \theta _ { \mathrm { g r a z i n g } } ) - \boxed { \Delta _ { S , \odot } ( \theta = 0 ) = \frac { 4 G M _ { \odot } } { c ^ { 3 } } \log \frac { 2 r _ { \mathrm { e s } } } { R _ { \odot } } } } \\ { \simeq 1 1 9 . 5 \mu s . } \end{array}
$$

It is also useful to rewrite eq.(6.23) as

$$
\Delta _ { S , \odot } = \frac { 2 G M _ { \odot } } { c ^ { 3 } } \left[ \log \left( \frac { d } { r _ { \mathrm { e s } } } \right) - \log \left( \frac { 1 + \cos \theta } { 2 } \right) \right] ,
$$

which stresses that $\Delta _ { S , \odot }$ is the sum of two positive terms,given tha $0 \leqslant ( 1 + \cos \theta ) / 2 \leqslant 1$ ,and therefore its logarithm is negative.Therefor $\Delta _ { S , \odot } > 0$ for all values of $\theta$ .Since eq.(6.16) gives $t _ { \mathrm { o b s } } = ( t _ { \mathrm { S S B } } - \Delta _ { R , \odot } ) .$ $\Delta _ { S , \odot }$ ,we see that a positive $\Delta _ { S , \odot }$ produces a delay in the time at whir the pulse arrives at the observer (or at the SSB).This is physicall correct,since the radio wave is delayed by the fact that it goes into tl “potential well” in space-time generated by the presence of the Sun.

# Einstein time delay

The Roemer and Shapiro time delays that we have computed are shifl in the coordinate time $t$ .However,this is not the same as the tim recorded by a clock in a laboratory.A laboratory clock located at position $\mathbf { x } _ { \mathrm { o b s } }$ rather measures its own proper time $\tau$ ,which in the metri (6.9) is related to $t$ by

$$
c ^ { 2 } d \tau ^ { 2 } = [ 1 + 2 \phi (  { \mathbf { x } } _ { \mathrm { 0 b s } } ) ] \mathrm { e } ^ { 2 } d t ^ { 2 } - [ 1 - 2 \phi (  { \mathbf { x } } _ { \mathrm { 0 b s } } ) ] d  { \mathbf { x } } _ { \mathrm { 0 b s } } ^ { 2 } ,
$$

so,to first order in the small parameters $\phi ( \mathbf { x } _ { \mathrm { o b s } } )$ and ${ \bf v } _ { \mathrm { o b s } } = d { \bf x } _ { \mathrm { o b s } } / \mathrm { d }$ we have

$$
\frac { d \tau } { d t } \simeq 1 \Big | + \phi \big ( \mathbf { x } _ { \mathrm { \scriptscriptstyle 0 b s } } \big ) - \frac { v _ { \mathrm { \scriptscriptstyle 0 b s } } ^ { 2 } } { 2 c ^ { 2 } } .
$$

Physically, the term $( - 1 / 2 ) v _ { \mathrm { o b s } } ^ { 2 } / c ^ { 2 }$ gives the transverse Doppler shif while $\phi$ gives the gravitational redshift. Integrating,we get

$$
\tau \simeq t + \int ^ { t } d t ^ { \prime } \left[ \phi ( \mathbf { x } _ { \mathrm { o b s } } ( t ^ { \prime } ) ) - \frac { v _ { \mathrm { o b s } } ^ { 2 } ( t ^ { \prime } ) } { 2 c ^ { 2 } } \right] ,
$$

where the lower limit of the integral is arbitrary,since it corresponds to an arbitrary constant shift in the origin of T.We can rewrite this as

$$
\begin{array} { r } { \hat { \mathbf { \sigma } } _ { t \simeq \tau + \Delta _ { E \odot } } , } \end{array}
$$

where

$$
\Delta _ { E \odot } = \int ^ { t } d t ^ { \prime } \left[ \frac { v _ { \mathrm { { o b s } } } ^ { 2 } ( t ^ { \prime } ) } { 2 c ^ { 2 } } - \phi ( \mathbf { x } _ { \mathrm { o b s } } ( t ^ { \prime } ) ) \right] .
$$

This is called the Einstein time delay.The dominant effect on $v _ { \mathrm { o b s } }$ comes from the motion of the Earth around the Sun,with velocity $v _ { \oplus }$ ,and the rotation of the Earth around its axis gives a small correction,so we write Vobs \~ U@.We take the Earth in anlelliptic orbit around the Sun, with semimajor axis α.Recall from eq.(4.53) that in a Keplerian orbit the total kinetic plus potential energy of the Earth-Sun system is related to the semimajor axis $a$ by

$$
E = - { \frac { G M \mu } { 2 a } } ,
$$

where $\mu$ is the reduced mass of the|Earth-Sun system (i.e.the Earth mass,with excellent accuracy） and $M$ the total mass (i.e. $M \simeq M _ { \odot }$ ， with excellent accuracy).Since,on the other hand,

$$
E = { \frac { 1 } { 2 } } \mu v _ { \oplus } ^ { 2 } - { \frac { G M \mu } { r } } ,
$$

we have

$$
\frac { 1 } { 2 } v _ { \oplus } ^ { 2 } = \frac { G M _ { \odot } } { r } - \frac { G M _ { \odot } } { 2 a } ,
$$

and

$$
\begin{array} { l } { \displaystyle \frac { d \Delta _ { E \odot } } { d t } \simeq \frac { v _ { \oplus } ^ { 2 } } { 2 c ^ { 2 } } - \phi } \\ { \displaystyle = \frac { 2 G M _ { \odot } } { c ^ { 2 } } \left( \frac { 1 } { r } - \frac { 1 } { 4 a } \right) . } \end{array}
$$

A constant part in this expresson is incorporated in the definition of atomic time,which is defined as the time measured byanatomic clock at a fixed distance $a$ from the Sun.The dependence on $r$ however introduces a modulation,due to the ellipticity of the Earth orbit.

# Dispersion in the interstellar medium

Beside the Roemer,Shapiro and Einstein delays,which are due to the motion of the observer and to the gravitational field of the solar system, there is also a correction to the arrival times which is due to the propagation of the radio waves throughi the ionized interstellar gas,which effctively acts as a medium witha refraction index appreciably different from unity,and with an important frequency dependence.As a result,the component of the radio pulse with frequency v travels with a group velocity $v _ { g }$ given by

$$
v _ { g } \simeq c \left( 1 - \frac { n _ { e } e ^ { 2 } } { 2 \pi m _ { e } } \frac { 1 } { \nu ^ { 2 } } \right) ,
$$

where $e$ and $m _ { e }$ are the charge and the mass of the electron, and n is the electron number density. The travel time over a distance $L$ i5 therefore

$$
\int _ { 0 } ^ { L } \frac { d l } { v _ { g } } \simeq \frac { L } { c } + \frac { 1 } { \nu ^ { 2 } } \left( \frac { e ^ { 2 } } { 2 \pi m _ { e } c } \right) \int _ { 0 } ^ { L } n _ { e } d l .
$$

The quantity

$$
\mathrm { D M } \equiv \int _ { 0 } ^ { L } { n _ { e } d l }
$$

is called the dispersion measure,and is typically quoted in $\mathrm { c m } ^ { - 3 }$ D Measuring the TOAs at different frequencies,we can get the dispersiot measure,and we can correct for this effect. This procedure, known as de dispersion,is performed separating the useful bandwidth of the receive into many channels,such that in each channel the effect of dispersion i negligible.The output of the channels operating at different frequencie is then automatically corrected and superimposed,in order to enhanc the signal-to-noise ratio.

To have an idea of the size of the effect,we observe that the Hulse Taylor binary pulsar has a (relatively large) dispersion measure DM $\simeq 1 6 9 \mathrm { c m } ^ { - 3 }$ pc.The measurements at Arecibo which led to its discovery were performed near $4 3 0 ~ \mathrm { M H z }$ In the typical 4 MHz bandwidth around $4 3 0 ~ \mathrm { M H z }$ ,this value of DM produces a spreading of the pulse of abou $7 0 \mathrm { m s }$ ,which is larger than the iitrinsic period of the pulsar of 59 ms,and the signal would then be unobservable. Thus,de-dispersion is a crucia part of pulsar observations.If one is performing a search for unknown pulsars,the value of DM is an unknown parameter,and the data are de dispersed with various possible values of DM within a plausible range i.e.DM becomes one of the dimensions of the parameter space in which data analysis is performed.

# Relation to the intrinsic pulsar signal

We can now put together all these corrections. Since they are small, we can simply add them up linearly (e.g. the effect of the Einstein time delay on the Shapiro delay is totally negligible).Equation (6.30) shows that the time $\tau _ { \mathrm { { o b s } } }$ actually measured bya clock in a laboratory (i.e. it proper time)is related to the cdordinate time $t _ { \mathrm { o b s } }$ by $t _ { \mathrm { { o b s } } } = \tau _ { \mathrm { { o b s } } } + \Delta _ { E \odot }$ , which,combined with eq.(6.16),gives

$$
t _ { \mathrm { S S B } } = \tau _ { \mathrm { o b s } } + \left| \Delta _ { E \odot } + \Delta _ { R , \odot } - \Delta _ { S , \odot } . \right.
$$

From this,we must stillsubtract the time delay due to the interaction with the interstellar medium,given in eq. (6.36),so we write

where

$$
\begin{array} { c } { { t _ { \mathrm { S S B } } = \tau _ { \mathrm { { o b s } } } - \displaystyle \frac { D } { \nu ^ { 2 } } \big ( { \mit \Delta } _ { E \odot } + \Delta _ { R , \odot } - \Delta _ { S , \odot } , \ : } } \\ { { { } } } \\ { { D = \displaystyle \left( \frac { e ^ { 2 } } { 2 \pi m _ { e } c } \right) \mathrm { D M } . } } \end{array}
$$

The quantity tssB so obtained is the coordinate time at which the signal recorded by our laboratory clock at $\tau _ { \mathrm { { \phi } ^ { b s } } }$ would have arrived at a fixed point in space such as the solar system barycenter,if there were no effect due to the gravitational potential of the solar system,and no interaction with the interstellar medium.It therefore depends only on the intrinsic properties of the source.

The emission mechanism of the pulsar is not yet completely understood,but in any case is believed tobe related to some “hot spot” corotating with the pulsar.If we denote by $\Phi$ the accumulated phase of the spinning pulsar,and we neglect for the moment any proper motion of the pulsar,we seea pulse whenever the phase $\Phi$ goes back to the same value $\Phi _ { 0 }$ mod $2 \pi$ ,at which the radiated beam sweeps across the Earth. If we denote by $T$ the proper time in the pulsar frame,fora perfectly periodic pulsar,spinning with frequency v,we would have Φ = 2πvT. Actually, $\nu$ cannot be exactly constant.In particular,the pulsar must spin down because the energy of the beam is ultimately taken from its rotational energy (and also,because aiy deviation of axisymmetry leads to a production of gravitational wave\$,as we saw in Section 4.2). We can model phenomenologically the evolution of the pulsar frequency performing a Taylor expansion around some reference value To = O of the pulsar proper time,

$$
\nu ( T ) = \nu _ { 0 } + \dot { \nu } _ { 0 } T + \frac { 1 } { 2 } \ddot { \nu } _ { 0 } T ^ { 2 } + \ldots ,
$$

where $\dot { \nu } _ { 0 } , \ddot { \nu } _ { 0 }$ ,etc.are generically called the spindown parameters.Then the accumulated phase is given by

$$
\begin{array} { c } { { \displaystyle \frac { 1 } { 2 \pi } \Phi ( T ) = \int _ { 0 } ^ { T } d \tau \nu ( \tau ) } } \\ { { = \nu _ { 0 } T + \displaystyle \frac { 1 } { 2 } \dot { \nu } _ { 0 } T ^ { 2 } + \displaystyle \frac { 1 } { 6 } \ddot { \nu } _ { 0 } T ^ { 3 } + \dots . } } \end{array}
$$

Emission will take place at the proper times $T _ { n }$ such that $\Phi ( T _ { n } ) =$ $\Phi _ { 0 } + 2 \pi n$ .Then the emission proper times $T _ { n }$ are given by

$$
\nu _ { 0 } T _ { n } + \frac { 1 } { 2 } \dot { \nu } _ { 0 } T _ { n } ^ { 2 } + \frac { 1 } { 6 } \ddot { \nu } _ { 0 } T _ { n } ^ { 3 } + \ldots = n + \frac { \Phi _ { 0 } } { 2 \pi } ,
$$

so .the spindown parameters produce deviations from the exact periodicity $T _ { n } = ( \Phi _ { 0 } / 2 \pi \nu _ { 0 } ) + ( 1 / \nu _ { 0 } ) n$ .The typical dissipation mechanisms in pulsars produce a power-like behavior v \~ Cvn,with C a constant and $n \sim 2 - 3$ (or at most $n = 5$ for damping due to GW emission,see eq.(4.228)).This gives i \~ Cnvn-1 = nv²/v. For the Hulse-Taylor pulsar, $\nu _ { 0 } \simeq 1 6 . 9 { \mathrm { s } } ^ { - 1 }$ and $\dot { \nu } _ { 0 } \simeq - 2 . 5 \times 1 0 ^ { - 1 5 } \mathrm { s } ^ { - 2 }$ ,so one expects a value of the second derivative of order $\ddot { \nu } _ { 0 } \simeq \mathfrak { s } \times 1 0 ^ { - 3 1 } \mathrm { s } ^ { - 3 }$ ,which over the time span of the observation is unobservably small. Thus,in this case it is sufficient to keep only $\dot { \nu } _ { 0 }$ in eq. (6.41)

This model assumes that the evolution of the pulsar frequency is smooth.Actually,most pulsars exhibit“glitches”,i.e.sudden jumps in heirrotational periods,related to some form of rearrangement of their internal structure.For instande,the Vela pulsar typically has glitches al intervals of about three years,where the period sudden decreases up to 200 ns (for comparison,the normal rate of change of the period of the Vela pulsar is an increase by about $1 0 ~ \mathrm { { n s / d a y } }$ .However,the Hulse Taylor pulsar has shown a remarkable stability,and no glitches,over the 30 years period that is has been observed.

The final step is to connect the pulsar proper time $T$ with the coordinate time $t$ .This will give the values of coordinate time at emission $t _ { \mathrm { e m } , n } = t ( T _ { n } )$ ; apart from corrections due to the pulsar proper motion, te be discussed below,we can then trivially compute the barycentric time of arrivals $t _ { \mathrm { S S B } , n }$ ,i.e.the fctitious values of coordinate time at which these signals would arrive at the solar system barycenter in the absence of dispersion and of Shapiro delay: these are simply $t _ { \mathrm { S S B } , n } = t _ { \mathrm { e m } , n } + d / c$ where $d$ is the distance between the barycenter of the pulsar-companion system and the SSB.Thus,onee we compute the relation between proper time $T$ and the coordinate time $t$ ，which we will do in the next subsec tion,both the time of arrivals measured by our laboratory clock and the timing predicted by this pulsar model have been expressed in terms ol the same variable, $t _ { \mathrm { S S B } }$ ,and can be compared.

5It should be observed that the splitting of the various contribution to the timing formula into Einstein,Roemer and Shapiro time delays,aberration delays,etc.discussed below, is not invariant under general coordinate transformations,so it really refers to the harmonic coordinate system,in which the interval has the form (6.9).

# 6.2.3 Relativistic corrections for binary pulsars

For a pulsar in a binary system we can proceed similarly to what we have done for the Earth-Sun system,and perform the transformation from the pulsar proper time to the coordinate time of the pulsar-companiom barycenter. We therefore have also Roemer,Shapiro and Einstein de lays associated to the pulsar-gompanion system. The crucial difference however,with respect to the solar system corrections,is that the binary pulsar is a fairly relativistic system,with strong gravitational fields,and therefore general-relativistic effects are much more important. This is a blessing,since it is just this fact that allows us to measure general relativistic effects in such systems, such as the emission of gravitational radiation,but it also implies that the computation is technically more difcult,sincea full general-relativistic treatment of the two-body dynamics becomes necessary. We discuss the various relevant effects in turn.5

# Einstein time delay

For this term,the Newtonian equation of the trajectory gives a suffcient accuracy. The computaton is therefore similar to what we did on page 310,except that in the expressions for the reduced and total mass of the system we must use the masses $m _ { p }$ and $m _ { c }$ of the pulsar and of its companion. There is however a subtle conceptual point.The beam is radiated by some“hot spot”ata position $\mathbf { x }$ on the surface of the pulsar. The Newtonian expression for $\phi$ at the location $\mathbf { x }$ is

$$
\phi ( { \bf x } ) = - \frac { | G m _ { p } } { c ^ { 2 } | { \bf x } - { \bf x } _ { p } | } - \frac { G m _ { c } } { c ^ { 2 } | { \bf x } - { \bf x } _ { c } | } ,
$$

where xp is the position of the center of the pulsar and $\mathbf { x } _ { c }$ is the position of the companion．Using the numerical values in eqs.(6.1） and (6.2),the second term is of order $G m _ { c } / ( c ^ { 2 } a ) \sim 1 0 ^ { - 6 }$ and therefore is small.For this term，therefore,the|weak-field approximation is legitimate. The self-gravity of the pulsar however is strong on its surface. For a typical neutron star radius $r _ { N S } \simeq 1 0 ~ \mathrm { k m }$ and $m _ { p } \simeq 1 . 4 M _ { \odot }$ we have $G m _ { p } / ( c ^ { 2 } r _ { N S } ) \simeq 0 . 2$ .Howeverthis term (as well as its generalization in full general relativity） does not change along the trajectory of the pulsar in orbit around its companion,so it does not introduce a modulation of the time of arrivals.Its effect is simply reabsorbed in a constant rescaling of proper time $T$ ,which is not observable. Thus,the time-dependent part of the Einstein time delay can be computed simply using

$$
\phi ( \mathbf { x } ) = - { \frac { G m _ { c } } { c ^ { 2 } | \mathbf { x } - \mathbf { x } _ { c } | } } ,
$$

and the weak field approximation. Then,eq. (6.27) gives

$$
\frac { d T } { d t } = 1 - \frac { G m _ { c } } { c ^ { 2 } | { \bf x } _ { p } - { \bf x } _ { c } | } - \frac { v _ { p } ^ { 2 } } { 2 c ^ { 2 } } ,
$$

where $\mathbf { x } _ { p }$ is the pulsar position and $v _ { p }$ is its velocity. The latter is obtained from

$$
v _ { p } = \frac { \not m _ { c } } { m _ { p } + m _ { c } } v ,
$$

where $v$ is the relative velocity in the center of mass system,given by (compare with eq. (6.33))

$^ 6 \mathrm { A }$ more detailed discussion on this point can be found in Will (1984).

$$
\frac { 1 } { 2 } v ^ { 2 } - \frac { G ( m _ { p } + m _ { c } ) } { r } \sp { + } = - \frac { G ( m _ { p } + m _ { c } ) } { 2 a } ,
$$

Thus,

$$
\frac { d T } { d t } = 1 - \frac { G } { c ^ { 2 } } \left[ \frac { m _ { c } ( m _ { p } + 2 m _ { c } ) } { m _ { p } + m _ { c } } \frac { 1 } { r } - \frac { m _ { c } ^ { 2 } } { m _ { p } + m _ { c } } \frac { 1 } { 2 a } \right] .
$$

We use the parametrization of the Keplerian orbit in terms of the eccentric anomaly $u$ ,given in eqs.(4.56)and (4.57),with $u$ related to the time $t$ by Kepler equation (4.58),

$$
u - e \sin u = \frac { 2 \pi } { P _ { b } } \left( t - t _ { 0 } \right) ,
$$

where $t _ { 0 }$ is a reference time of periastron passage.Differentiating,we have

$$
\frac { d u } { d t } \left( 1 - e \cos u \right) = \frac { 2 \pi } { P _ { b } } ,
$$

d therefore,

$$
\frac { d T } { d t } = \frac { d u } { d t } \frac { d T } { d u } = \frac { 2 \pi } { P _ { b } } \frac { 1 } { 1 - e \cos u } \frac { d T } { d u } .
$$

Plugging this into eq. (6.49) and using eq. (4.56) we get

$$
\begin{array} { l }   \displaystyle { \frac { 2 \pi } { P _ { b } } \frac { d T } { d u } = \left( 1 - \frac { G } { c ^ { 2 } } \frac { 2 m _ { c } m _ { p } + \} { 2 a ( m _ { p } + m _ { c } ) }  - e \cos u \left( 1 + \frac { G } { c ^ { 2 } } \frac { m _ { c } ^ { 2 } } { 2 a ( m _ { p } + m _ { c } ) } \right) } } \\ { \right){ \mathrm { \simeq \left( 1 - \frac { \it G } { c ^ { 2 } } \frac { 2 m _ { c } m _ { p } + 3 m _ { c } ^ { 2 } } { 2 a ( m _ { p } + m _ { c } ) } \right) } } } \\ { { \mathrm { \quad \quad } \times \left[ 1 - e \cos u \left( 1 + \left| { \frac { G } { c ^ { 2 } } \frac { m _ { c } ( m _ { p } + 2 m _ { c } ) } { a ( m _ { p } + m _ { c } ) } } \right. \right) \right] \ : , } } \end{array}
$$

where in the second line we retained only terms of first order in G.The overallfactor is a constant multiplicative rescaling of the pulsar proper time $T$ .Such a factor is unobservable,since it relates the (unobservable)proper time that the pulsar would have in the presence of only its own gravitational feld,to its actual proper time that includes the gravitational effect of the companion and the pulsar orbital velocity. Instead,the correction proportional to $\cos u$ produces a modulation along the orbit and is therefore observable.We can therefore reabsorb the multiplicative factor into the definition of proper time,rescaling

$$
T  ( 1 - \frac { G } {  { \mathrm { k } } ^ { 2 } } \frac { 2 m _ { c } m _ { p } + 3 m _ { c } ^ { 2 } } { 2 a ( m _ { p } + m _ { c } ) } ) T ,
$$

and eq.(6.53) becomes

$$
\frac { d T } { d u } = \frac { P _ { b } } { 2 \pi } \left\{ 1 - e \cos u \right\} - \gamma \cos u
$$

where the Einstein parameter $ { \uparrow }$ is given by

$$
\begin{array} { l } { { \gamma = e \left( \frac { P _ { b } } { 2 \pi } \right) \frac { G } { c ^ { 2 } } \frac { m _ { c } ( m _ { p } + 2 m _ { c } ) } { a ( m _ { p } + m _ { c } ) } } } \\ { { \mathrm { } = e \left( \frac { P _ { b } } { 2 \pi } \right) ^ { 1 / 3 } \frac { G ^ { 2 / 3 } } { c ^ { 2 } } \frac { m _ { c } ( m _ { p } + 2 m _ { c } ) } { ( m _ { p } + m _ { c } ) ^ { 4 / 3 } } , } } \end{array}
$$

and in the second line we used Kepler's law, $G ( m _ { p } + m _ { c } ) / a ^ { 3 } = ( 2 \pi / P _ { b } ) ^ { 2 }$ to eliminate $a$ Writing $T = t - \Delta _ { E }$ ,and observing,fromeq. (6.50),thal $( 2 \pi / P _ { b } ) d t / d u = 1 - e \cos u$ we see that

$$
\frac { d \Delta _ { E } } { d \hbar } = \gamma \cos u .
$$

Then, we obtains for the Einstein delay

$$
\Delta _ { E } = \gamma \sin u .
$$

Inserting the numerical values of $e$ and $P _ { b }$ of the Hulse-Taylor pulsar eq.(6.56) gives

$$
\gamma = 2 . 9 3 6 9 6 \mathrm { m s } \left( \frac { m _ { c } } { M _ { \odot } } \right) \left( \frac { | m _ { p } + 2 m _ { c } } { M _ { \odot } } \right) \left( \frac { m _ { p } + m _ { c } } { M _ { \odot } } \right) ^ { - 4 / 3 } .
$$

# Roemer time delay and the post-Newtonian orbit

Referring the emission time to the barycenter of the pulsar-companion system，we encounter the Roemer and Shapiro time delays,similarly to what we found for the solar system corrections.In the geometry of Fig.6.1, the Roemer delay is given by $\Delta _ { R } = \hat { { \bf z } } { \cdot } { \bf x } _ { 1 } ( t ) / c$ ，where $\mathbf { x } _ { 1 }$ is the distance of the pulsar from the center-of-mass of the pulsar-companion system.We therefore need the explicit form of the orbit, ${ \bf x } _ { 1 } ( t )$

We first consider a Keplerian orbit,neglecting general-relativistic corrections.Using polar coordinates $( r _ { 1 } , \psi )$ in the plane of the orbit,the Keplerian equation of motion is given in parametric form,in terms of the eccentric anomaly $u$ ，by

$$
\begin{array} { c } { r _ { 1 } ( u ) = a _ { \mathrm { i } } [ 1 - e \cos u ] , } \\ { \displaystyle \cos \psi ( u ) = \frac { \cos u - e } { 1 - e \cos u } } \end{array}
$$

(compare with eqs. (4.56) and (4.57)),where $a _ { 1 }$ is the semimajor axis of the pulsar orbit.Observe that $r _ { 1 }$ reaches its minimum value at $u = 0$ ,in which case $\psi = 0$ .Therefore the angle $\psi$ is measured from periastron, and the angle measured from the line of nodes is $\omega + \psi ( u )$ ,see Fig. 6.1. From the geometry of Fig.6.1 we then see that the Roemer delay is

$$
\Delta _ { R } = r _ { 1 } ( u ) \sin \iota \sin [ \omega + \psi ( u ) ] .
$$

We now expand $\sin ( \omega + \psi ) = \cos \psi$ sin $\omega { + } \sin \psi \cos \omega$ and we use eq. (6.61) for $\cos \psi$ ,together with the corresponding expression for $\sin \psi$ ，

$$
\sin \psi ( u ) = ( 1 - e ^ { 2 } ) ^ { 1 / 2 } \frac { \sin u } { 1 - e \cos u } ,
$$

and we get

$$
\begin{array} { l } { \displaystyle \Delta _ { R } = \frac { r _ { 1 } ( u ) } { 1 - e \cos u } \sin \upsilon \iota [ ( \cos u - e ) \sin \omega + ( 1 - e ^ { 2 } ) ^ { 1 / 2 } \sin u \cos \omega ] } \\ { = a _ { 1 } \sin \iota [ ( \cos u - e ) \sin \omega + ( 1 - e ^ { 2 } ) ^ { 1 / 2 } \sin u \cos \omega ] . \qquad ( 6 } \end{array}
$$

This is the result at the Keplerian level. However, numerically the effect is quite large,and it is necessary tq go beyond the Keplerian orbit,and include the post-Newtonian corrections to 1PN order.This computation has been performed by Damour andDeruelle (1985,1986),and we sketch the main steps. The equations of motion at 1PN level can be derived from the Lagrangian (5.54).Defining the variable

$$
{ \bf X } = \frac { m _ { 1 } ^ { * } { \bf x } _ { 1 } + m _ { 2 } ^ { * } { \bf x } _ { 2 } } { m _ { 1 } ^ { * } + m _ { 2 } ^ { * } } ,
$$

where

$$
m _ { A } ^ { * } = m _ { A } + \frac { m _ { A } ^ { } v _ { A } ^ { 2 } } { 2 c ^ { 2 } } - \frac { G m _ { 1 } ^ { } m _ { 2 } ^ { } } { 2 r c ^ { 2 } } ,
$$

the equations of motion give $d ^ { 2 } \mathbf { X } / d t ^ { 2 } = 0$ ，In the non-relativistic limit this is the statement that the center-of-mass is non accelerated. In fact, because of the corrections $O ( v ^ { 2 } / c ^ { 2 } )$ ， $\mathbf { X }$ is rather a“center-of-energy”.

Invariance under time translations and rotations leads to the conser vation of energy and angular momentum.Because of conservation angular momentum,the equatibn for the relative coordinate r describe a motion in a plane,just as in the Newtonian case,and there are two conserved quantities,the total energy $E$ and the total angular momer tum J.We use the usual notations $m$ for the total mass, $m = m _ { 1 } + m _ { 2 }$ $\mu$ for the reduced mass $\mu = m _ { 1 } m _ { 2 } / m$ and,as in Chapter 5,we use th symmetric mass ratio $\nu = \mu / ( m _ { 1 } + m _ { 2 } ) = m _ { 1 } m _ { 2 } / ( m _ { 1 } + m _ { 2 } ) ^ { 2 }$ (observ that $0 \leqslant \nu \leqslant 1 / 4$ ).It is also convenient to introduce the energy an angular momentum per unit value of $\mu$ ， $\varepsilon = E / \mu , \mathbf { j } = \mathbf { J } / \mu$ Applying the Noether theorem to the Lagrangian (5.54),one finds the explici expression of the conserved quantities,

$$
\varepsilon = { \frac { 1 } { 2 } } v ^ { 2 } - { \frac { G m } { r } } + { \frac { 3 } { 8 } } ( 1 - 3 \nu ) { \frac { v ^ { 4 } } { c ^ { 2 } } } + { \frac { G m } { 2 r c ^ { 2 } } } \left[ ( 3 + \nu ) v ^ { 2 } + \nu ( { \hat { \mathbf { r } } } \cdot \mathbf { v } ) ^ { 2 } - { \frac { G m } { r } } \right] .
$$

and

$$
\mathbf { j } = \left[ 1 + { \frac { 1 } { 2 } } ( 1 - 3 \nu ) { \frac { v ^ { 2 } } { c ^ { 2 } } } + ( 3 + \nu ) { \frac { G m } { r c ^ { 2 } } } \right] \mathbf { r } \times \mathbf { v } ,
$$

where $v$ is the relative velocity and $\hat { \mathbf { r } } = \mathbf { r } / r$ .Using polar coordinate $( r , \psi )$ in the plane of the orbit these first integrals of the equations d motion give

$$
\begin{array} { c } { { { \displaystyle \left( \frac { d r } { d t } \right) ^ { 2 } = A + \frac { 2 B } { r } + \frac { { \cal C } } { r ^ { 2 } } + \frac { { \cal D } } { r ^ { 3 } } } , } } \\ { { { \displaystyle \frac { d \psi } { d t } = \frac { { \cal H } } { r ^ { 2 } } + \frac { { \cal I } } { r ^ { 3 } } } , } } \end{array}
$$

where $A , \ldots , I$ are polynomials in $\varepsilon$ and $j$

$$
\begin{array} { r l } & { { A = 2 \varepsilon \left[ 1 + \frac { 3 } { 2 } ( 3 \nu + 1 ) { { \frac { \varepsilon } { c ^ { 2 } } } } \right] , } } \\ & { { B = G m \left[ 1 + ( 7 \nu + 6 ) { { \frac { \varepsilon } { c ^ { 2 } } } } \right] , } } \\ &  { C = - { { \vec { r } } ^ { 2 } } \left[ 1 + 2 ( 3 \nu - 1 ) { { \frac { \varepsilon } { c ^ { 2 } } } } \right] + { { \left( 5 \nu - 1 0 \right) } { { \frac { G ^ { 2 } m ^ { 2 } } { c ^ { 2 } } } } } , } \\ & { { D = { \left( 8 - 3 \nu \right) } { \frac { G M { { \vec { j } } ^ { 2 } } } { c ^ { 2 } } } , } } \\ & { { H = { \left( \mu \right) } \left[ 1 + { \left( 3 \nu - 1 \right) { { \frac { \varepsilon } { c ^ { 2 } } } } } \right] , } } \\ & { { I = { \left( 2 \nu - 4 \right) } { \frac { G M { { \vec { j } } ^ { 2 } } } { c ^ { 2 } } } . } } \end{array}
$$

In the limit $c \to \infty$ we have $D | = I = 0$ ，while the other coefficients re duce to their Newtonian values.Observe that in the Newtonian case th equation for $( d r / d t ) ^ { 2 }$ contains terms up to $1 / r ^ { 2 }$ ，while at the 1PN leve there is also a $1 / r ^ { 3 }$ term,that in principle could make the integratiol of the equation of motion very complicated．However,as observed b Damour and Deruelle,we can introduce a new radial variable $\bar { r }$ ，

$$
\bar { r } \equiv r + \frac { D } { 2 j ^ { 2 } } ,
$$

and in terms of this variable eq.(6.69) becomes

$$
\left( \frac { d \bar { r } } { d t } \right) ^ { 2 } = A + \frac { 2 B } { \bar { r } } + \frac { \bar { C } } { \bar { r } ^ { 2 } } + O ( v ^ { 4 } / c ^ { 4 } ) ,
$$

with $\bar { C } = C + ( B D / j ^ { 2 } )$ .Since the terms $O ( v ^ { 4 } / c ^ { 4 } )$ are consistently neglected at this order,this equation still has the form of a Newtonian-like radialequation of motion,with suitably redefined parameters. Similarly, defining $\tilde { r } = r - I / ( 2 H )$ ,the angular equation (6.7O) becomes

$$
\frac { d \psi } { d t } \sp \frac { H } { \widetilde { r } ^ { 2 } } .
$$

As a result,the equations of motion|to 1PN order can be integrated analytically,and the solution can be put in a form similar to the Keplerian orbit discussed in Section 4.1.2. In particular,eqs. (4.56) and (4.58) become

$$
u - e _ { t } \sin \mu = \frac { 2 \pi } { P _ { b } } t ,
$$

and

$$
r = a _ { r } [ 1 - e _ { r } \cos u ] ,
$$

where

$$
\begin{array} { l } { { a _ { r } = - \displaystyle \frac { G m } { 2 \varepsilon } \left[ 1 - ( \nu - 7 ) \frac { \varepsilon } { 2 c ^ { 2 } } \right] \bigg \vert , } } \\ { { e _ { r } ^ { 2 } = 1 + \displaystyle \frac { 2 \varepsilon } { G ^ { 2 } m ^ { 2 } } \left[ 1 + ( 5 \nu - 1 5 ) \frac { \varepsilon } { 2 c ^ { 2 } } \right] \left[ j ^ { 2 } + ( \nu - 6 ) \frac { G ^ { 2 } m ^ { 2 } } { c ^ { 2 } } \right] , \hfill } } \\ { { e _ { t } ^ { 2 } = 1 + \displaystyle \frac { 2 \varepsilon } { G ^ { 2 } m ^ { 2 } } \left[ 1 + ( 1 7 - \nu \nu ) \frac { \varepsilon } { 2 c ^ { 2 } } \right] \left[ j ^ { 2 } + ( 2 - 2 \nu ) \frac { G ^ { 2 } m ^ { 2 } } { c ^ { 2 } } \right] , \hfill } } \\ { { \displaystyle \frac { 2 \pi } { P _ { b } } = \frac { ( - 2 \varepsilon ) ^ { 3 / 2 } } { G m } \left[ 1 - ( \nu - 1 9 ) \frac { \varepsilon } { 4 c ^ { 2 } } \right] . \hfill } } \end{array}
$$

In other words,the eccentricity $e$ of the Keplerian solution is now split into a“radial eccentricity” $e _ { r }$ and $\mathrm { a }$ “time eccentricity” $e _ { t }$ .Similarly, the solution for $\psi ( u )$ is writen in terms of an“angular eccentricity" $e _ { \theta }$ ，

$$
\psi = \omega _ { 0 } + ( 1 + k ) A _ { e _ { \theta } } ( u ) ,
$$

where7

$$
k = { \frac { 3 G m } { c ^ { 2 } a ( 1 - e ^ { 2 } ) } } .
$$

The function $A _ { e _ { \theta } } ( u )$ is the same as in eq. (4.61),with $e \to e _ { \theta }$ ,and

$$
e _ { \theta } ^ { 2 } = 1 + \frac { 2 \varepsilon } { G ^ { 2 } m ^ { 2 } } \left[ 1 + \left( \nu - 1 5 \right) \frac { \varepsilon } { 2 c ^ { 2 } } \right] \left[ j ^ { 2 } - 6 \frac { G ^ { 2 } m ^ { 2 } } { c ^ { 2 } } \right] .
$$

Observe that, when $c  \infty$ ， $e _ { \theta } ^ { 2 } , e _ { r } ^ { 2 }$ and $e _ { t } ^ { 2 }$ reduce to the Keplerian quantity $e ^ { 2 }$ given in eq. (4.5O).We therefore have a parametric “quasi-Newtonian” (i.e. Newtonian plus the precession due to a non-vanishing tineq. (6.86)) representation of the orbit accurate to 1PN order.8 Using

7Observe that， since $k$ is already a correction，to the order at which we are working it is irrelevant whether in eq.(6.87) we write the Keplerian major semiaxis $~ a ~ = ~ - G m / ( 2 \varepsilon )$ rather than $a _ { r }$ ,and similarly we can use $e$ or any other eccentricity such as $e _ { T }$

$^ { 8 } \mathrm { A t }$ the same time,the equation of motion (6.80) can be rewritten in terms of the proper time $T$ of the pulsar,rather than in terms of coordinate time $t _ { i }$ as

$$
u - e _ { T } \sin u = { \frac { 2 \pi } { P _ { b } } } T ,
$$

where $e _ { T }$ is another time eccentricity. It is crucial to carefully distinguish between these time eccentricities to get the correct 1PN result. See Damour and Deruelle(1985,1986) for details.

this expression for the orbit,eq.(6.64)is replaced by

$$
\Delta _ { R } = a _ { 1 } \sin \iota [ ( \cos \boldsymbol { u } - e _ { r } ) \sin \omega + ( 1 - e _ { \theta } ^ { 2 } ) ^ { 1 / 2 } \sin \boldsymbol { u } \cos \omega ] .
$$

Writing $e _ { r } = ( 1 + \delta _ { r } ) e$ and $e _ { \theta } \ = \ ( 1 + \delta _ { \theta } ) e$ ，where $e$ is the Keplerian eccentricity given by eq. (4.50),the parameters $\delta _ { r }$ and $\delta _ { \theta }$ have the values

$$
\begin{array} { l } { { \delta _ { r } = \displaystyle \frac { G } { c ^ { 2 } } \frac { 3 m _ { p } ^ { 2 } + | 6 m _ { p } m _ { c } + 2 m _ { c } ^ { 2 } } { a ( m _ { p } + m _ { c } ) } \ : , } } \\ { { \delta _ { \theta } = \displaystyle \frac { G } { c ^ { 2 } } \frac { ( 7 / 2 ) m _ { p } ^ { 2 } + 6 m _ { p } m _ { c } + 2 m _ { c } ^ { 2 } } { a ( m _ { p } + m _ { c } ) } \ : , } } \end{array}
$$

$^ { 9 } \mathrm { { I n } }$ all these equations we have assumed the correctness of general relativity. Alternatively, quantities such as $\delta _ { r }$ and $\delta _ { \theta }$ can be treated as free parameters, to be determined directly from the data,and their measure allows us to compare general relativity to alternative theories of gravitation.

where we wrote $m _ { 1 } = m _ { p } , m _ { 2 } = m _ { c }$ for the masses of the pulsar and the companion.9 Finally, we observe from eq. (6.81) that the periastron passages (i.e. the minima of $r$ ）arereached for $u = u _ { n } \equiv 2 \pi n$ with $\pi$ integer. Since $A _ { e _ { \theta } } ( u _ { n } ) = 2 \pi n$ ，we see from eq.(6.86) that $2 \pi k$ isthe angle of periastron precession per orbit. Observe that, in the complete general-relativistic solution, the advance of the periastron is not uniform along the orbit,but is a function of $u$ ．Since the position $\omega$ ofthe periastron advances by $2 \pi k$ over one period, the derivative of $\omega$ ,averaged over the orbit,is

$$
\begin{array} { l } { \displaystyle { \langle \dot { \omega } \rangle = \frac { 2 \pi } { P _ { b } } k } } \\ { \displaystyle { = \frac { 3 } { c ^ { 2 } } [ G ( m _ { p } + m _ { c } ) ] ^ { 2 / 3 } \left( \frac { 2 \pi } { P _ { b } } \right) ^ { 5 / 3 } \frac { 1 } { 1 - e ^ { 2 } } } , } \end{array}
$$

where in the second line we used eq. (6.87),and we eliminated $a$ using Kepler's law. Using the known values of $e$ and $P _ { b }$ for the Hulse-Taylor binary pulsar, this gives

$$
\left. \dot { \omega } \right. = 2 . 1 1 3 5 3 \left( \frac { m _ { p } + m _ { c } } { M _ { \odot } } \right) ^ { 2 / 3 } \mathrm { d e g / y r } .
$$

The comparison with the experimental value therefore gives the total mass of the binary system.

# Shapiro time delay

The Shapiro delay is due to the effect of the gravitational field of the companion on the pulsar signal (observe that the gravitational field of the pulsar itself enters instead in the relation between the pulsar proper time and coordinate time, just as the Earth's gravitational field when we computed the solar system corrections). The computation is analogous to what we did on pages 308-310. Using the Keplerian equation of the orbit given in eqs. (4.56) and (4.57)，and taking into account its orientation with respect to the observer,given by the periastron angle $\omega$ and by the inclination angle $\iota$ ,one obtains

$$
\Delta _ { S } = - 2 r \log \Big \{ \big ( 1 - e \cos u \big ) - s [ \sin \omega ( \cos u - e ) + \sqrt { 1 - e ^ { 2 } } \cos \omega \sin u ] \Big \} ,
$$

where $r \equiv G m _ { c } / c ^ { 3 }$ (not to be confused with a distance) and $s \equiv \sin \iota$ are called the range and shape of the Shapiro delay,respectively,and we omitted an overall constant (i.e.,a $u ^ { \flat }$ -independent term),which grows logarithmically with the distance to the pulsar. This constant term simply adds up to the total travel time,but it does not show up as a modulation in $u$ ,and is therefore unobservable.

# Secular changes due to GW emission

The timing formula also includes secular changes in the Keplerian parameters of the orbit,induced by GW emission,whose extraction is in fact our final aim.In particular we already saw that,because of GW emission,the orbital period has a non-vanishing time derivative given by eq. (6.4).10

This secular change modifies the Keplerian relation (6.50) between the eccentric anomaly $u$ and the proper time $T$ of the pulsar,which becomes

$$
u - e \sin u = 2 \pi \left[ \frac { T - T _ { 0 } } { P _ { b } } - \frac { 1 } { 2 } \dot { P } _ { b } \left( \frac { T - T _ { 0 } } { P _ { b } } \right) ^ { 2 } \right] ,
$$

where $T _ { 0 }$ is a reference value of proper time,and $P _ { b }$ is defined as the value of the orbital periodat this reference time.The factor $- 1 / 2$ comes from integrating the instantaneous orbital frequency $[ P _ { b } + \dot { P } _ { b } ( T - T _ { 0 } ) ] ^ { - 1 }$ to obtain the orbital phase.

Observe that，in order of magnitude,the velocity $v$ of the binary system is given by $v ^ { 2 } \sim G M / a$ ,where $M = m _ { p } + m _ { c }$ is the total mass. Using Kepler's law to eliminate $a$ in favor of $P _ { b }$ ,this can be rewritten as $P _ { b } / ( 2 \pi ) \sim G M / v ^ { 3 }$ . Substituting this into the expression for $\dot { P } _ { b }$ ，given ineq. (6.4),we see that

$$
\dot { P } _ { b } = O \left( \frac { v ^ { 5 } } { c ^ { 5 } } \right) .
$$

It is quite remarkable that an effect of order $( \boldsymbol { v } / c ) ^ { 5 }$ can be measured, and this is due to the combination of the extreme precision of the timing measurements,and to the fact that the Hulse-Taylor binary system is quite relativistic,with $v \sim 1 0 ^ { - 3 } c$

# Aberration correction and Doppler shift

Another ingredient of the full timing formula is an aberration correction lue to the fact that,because of the orbital motion of the pulsar around its companion, the direction from which the observer receives the pulse liffers from the direction in which it was emitted in the pulsar frame. This produces a delay

$$
\Delta _ { A } = A \{ \sin [ \omega + A _ { e } ( u ) ] + e \sin \omega \} + B \{ \cos [ \omega + A _ { e } ( u ) ] + e \cos \omega \} ,
$$

where $A$ and $B$ are two known constants.Finally, there is a longitudinal Doppler shift,due to the fact that there is in general a proper motion of

10 Actually， also $x ~ = ~ ( 1 / c ) a \sin \iota$ and the eccentricity $e$ have secular changes, see eqs.(4.116)and (4.117),which however are smaller,and not detectable with the present precision for the Hulse-Taylor pulsar.

the solar system barycenter with respect to the barycenter of the pulsar companion system,with a radial component of the velocity. Thus,the relation between the intrinsic and the observed orbital periods is given by

$$
P _ { b } ^ { \mathrm { i n t r } } = D P _ { b } ^ { \mathrm { o b s } } ,
$$

and the Dopper factor $D$ is given by

$$
D = \left( 1 - { \frac { \mathbf { v } \cdot { \hat { \mathbf { n } } } } { c } } \right) ,
$$

where $\mathbf { v }$ is the velocity of the pulsar-companion barycenter with respec to the SSB,and $\hat { \bf n }$ is the unit vector from the SSB toward the pulsar From eq.(6.99) we get

$$
\frac { \dot { P } _ { b } ^ { \mathrm { o b s } } } { P _ { b } ^ { \mathrm { o b s } } } = \frac { \dot { P } _ { b } ^ { \mathrm { i n t r } } } { P _ { b } ^ { \mathrm { i n t r } } } - \frac { \dot { D } } { D } .
$$

If the Doppler factor $D$ werea constant in time,the additional term $\dot { D } / D$ would vanish, that is, $\mathcal { D }$ would be simply reabsorbed into the definition of $P _ { b }$ ,and would be unobservable.However,there is a relativw acceleration of the SSB and oflthe pulsar-companion system,induced by the differential rotation of the Galaxy,as well as proper motion effects and therefore $\dot { D }$ is non-vanishing and produces an observable correcticn to $\dot { P } _ { b } / P _ { b }$ .To lowest order in the radial velocity $\mathbf { v } { \cdot } \hat { \mathbf { n } }$ we have $\dot { D } / D \simeq \dot { D }$ and

$$
{ \begin{array} { r l } & { \displaystyle - { \dot { D } } = { \frac { d } { d t } } { \frac { \mathbf { v } \cdot { \hat { \mathbf { n } } } } { c } } } \\ & { \displaystyle = { \frac { \mathbf { a } \cdot { \hat { \mathbf { n } } } } { c } } + { \frac { \mathbf { v } } { c } } \cdot { \frac { d { \hat { \mathbf { n } } } } { d t } } . } \end{array} }
$$

If the pulsar has a transverse velocity $v _ { T }$ with respect to the SSB,and as usual $d$ is the distance to the pulsar,in a time $d t$ the unit vector n acquires a component $v _ { T } d t / d$ in the transverse direction,and therefore ${ \bf v } { \cdot } d \hat { \bf n } / d t = v _ { T } ^ { 2 } / d$ ，Thus,there is a Doppler correction

$$
\left( \frac { \dot { P } _ { b } } { P _ { b } } \right) ^ { \mathrm { o b s } } = \left( \frac { \dot { P } _ { b } } { P _ { b } } \right) ^ { \mathrm { i n t r i n s i c } } + \left( \frac { \dot { P } _ { b } } { P _ { b } } \right) ^ { \mathrm { g a l } } ,
$$

where $( \dot { P } _ { b } / P _ { b } ) ^ { \mathrm { g a l } }$ is the value of $- \dot { D } / D$ due to the galactic acceleration and to proper motion

$$
\left( \frac { \dot { P } _ { b } } { P _ { b } } \right) ^ { \mathrm { g a l } } = \frac { \mathbf { a } \cdot \hat { \mathbf { n } } } { c } + \frac { v _ { T } ^ { 2 } } { c d } .
$$

The term $v _ { T } ^ { 2 } / ( c d )$ is also known as the Shklovsky effect due to the orbital motion.Fora pulsar in the galactic plane,eq.(6.1O4) can be rewriten as

$$
\left( \frac { \dot { P } _ { b } } { P _ { b } } \right) ^ { \mathrm { \tiny ~ g a l } } = - \frac { v _ { 0 } ^ { 2 } } { c \dot { R } _ { 0 } } \cos l - \frac { v _ { 1 } ^ { 2 } } { c R _ { 1 } } \cos \lambda + \frac { v _ { T } ^ { 2 } } { c d } ,
$$

where $v _ { 0 }$ is the galactic circular velocity at the Sun position, $R _ { 0 }$ the distance from the galactic center to the Sun, $v _ { 1 }$ and $R _ { 1 }$ are respectively the galactic circular velocity and the distance to the galactic center at the pulsar position, $l$ is the galactic latitude of the pulsar and $\lambda$ the Sun-pulsar-galactic center angle.11

We see from eq. (6.37) that,if we have a model of the electron distribution in the Galaxy,we can get the distance of a pulsar from us from the observed value of its dispersion measure. For the Hulse-Taylor pulsar this gives

$$
d = 8 . 3 \pm 1 . 4 \mathrm { k p c } .
$$

At this relatively large distance,the last term in eq. (6.105) is small, since it is proportional to $1 / d$ .However,the difference between the acceleration at the Earth and pulsar location,due to the differential rotation of the Galaxy,is quite importaht.Furthermore,this correction is sensitive to the values of $v _ { 0 }$ and $R _ { 0 } ,$ which are not very accurately known.Indeed,for the Hulse-Taylor the uncertainty in the first two terms in eq.(6.1O5) is the limiting factor in the comparison between the experimental results and the general relativity prediction.

# Fit to the full timing formula

At this point,one can compare these corrections with the observed timing residual and extract, from a fit,the parameters that enter in the timing formula. These parameters can be grouped as follows.

·Parameters characterizing the pulsar itself: the right ascension $\alpha$ and declination $\delta$ ,its proper motion,the initial pulse phase $\Phi _ { 0 }$ ,its frequency $\nu$ and the spindown parameters.In practice,among the spindown parameters it suffices to keep only $\dot { \nu } _ { 0 }$ ，as we saw below eq. (6.41).

· The five Keplerian parameters

which parametrize (at the level of Newtonian mechanics) the orbital motion of the pulsar. Here $T _ { 0 }$ is a time of passage at periastron,used as a reference time,and the quantities $P _ { b } , x \ =$ $( a / c ) \sin \iota , e , \omega$ ,which all have secular variations,are evaluated at $T = T _ { 0 }$

· The eight independently measurable post-Keplerian parameters

$$
\left\{ \dot { \omega } , \gamma , \dot { P } _ { b } , r , \vartheta , \delta _ { \theta } , \dot { e } , \dot { x } \right\} ,
$$

which characterize the relativistic corrections to the orbital motion.

Instead, the parameters $A$ and $B$ which enter in the aberration formula, as well as $\delta _ { r }$ ,in practice are not separately measurable,since their efect turns out to be degenerate with that of other parameters.

$^ { 1 1 } \mathrm { F } _ { 0 \mathrm { r } }$ a pulsar outside the galactic plane,there is also a (usually smaller) effect due to the vertical acceleration in the galactic potential. All these acceleration corrections are discussed in detail in Damour and Taylor (1991).

![](images/c4a69aa511f88f91f5c0d38c8864bf820e1530c2c2b2fe0be65eaeff39fc9004.jpg)  
Fig.6.6 Constraints on the pulsar and companion mass from $\langle \dot { \omega } \rangle$ and $\gamma$ Theuncertainties in $\langle \dot { \omega } \rangle$ and $\gamma$ are smaller than the displayed linewidths.From Weisberg and Taylor(2Oo2).The values of the masses have been updated in Weisberg and Taylor (2004),see Table 6.1.

If we assume the validity of general relativity,all the post-Keplerian parameters are predicted once we know the value of the Keplerian para meters,and the masses of the pulsar and of the companion, $m _ { p }$ and $m _ { c }$ Therefore,if from the fit of the observed time residuals to the timing formula we can extract the five Keplerian parameters plus any two of the post-Keplerian parameters,we can get the masses $m _ { p }$ and $m _ { c }$ , this point,any further post-Keplerian parameter which can be extracted from the fit to the experimental data provides a test of general relativity, since it can be compared to the value predicted by general relativity with no more free parameter at our disposal.

In particular,for the HulseTaylor binary pulsar it is possible to extract,from the comparison with the timing formula,all Keplerian para meters and the three post-Keplerian quantities $\langle \dot { \omega } \rangle , \gamma$ and $\dot { P } _ { b }$ From the values of $\langle \dot { \omega } \rangle$ and $\gamma$ one obtains $m _ { p }$ and $m _ { c }$ ,see eq. (6.1) and Fig.6.6. Concerning $\dot { P } _ { b }$ ,the observed value is (see Table 6.1 on page 303)

$$
\dot { P } _ { b } ^ { \mathrm { o b s } } = - 2 . 4 1 8 4 ( 9 ) \times 1 0 ^ { - 1 2 } .
$$

Using the known values of the accelerations in the galactic potential, one finds $\dot { P } _ { b } ^ { \mathrm { g a l } } = - 0 . 0 1 2 8 ( 5 0 ) \times 1 0 ^ { - 1 2 }$ Correciisi to eq.(6.103) we therefore haye

$$
\dot { P } _ { b } ^ { \mathrm { i n t r i n s i c } } = \dot { P } _ { b } ^ { \mathrm { o b s } } - \dot { P } _ { b } ^ { \mathrm { g a l } } = - 2 . 4 0 5 6 ( 5 1 ) \times 1 0 ^ { - 1 2 } .
$$

Since the masses and have been fixed from $\langle \dot { \omega } \rangle$ and ,the value ol

![](images/0c464f01362f6a9f1012f9c85e4b696b26abed65d5fd49cfd14af409eae85f70.jpg)  
Fig.6.7 Orbital decay of PSR $\mathrm { B } 1 9 1 3 + \mathrm { 1 6 }$ ，The data points indicate the observed change in the epoch of periastron with date,while the parabola is the general relativity prediction for a system emitting gravitational radiation.From Weisberg,Taylor and Nice (in preparation).The years in the late l99Os with no data corresponds to a period when the Arecibo telescope was closed for major upgrades.

due to GW emission,eq. (6.4), which is

$$
\dot { P } _ { b } ^ { \mathrm { G R } } = - 2 . 4 0 2 4 2 ( 2 ) \times 1 0 ^ { - 1 2 } .
$$

The agreement is therefore at the $( 0 . 1 3 \pm 0 . 2 1 ) \%$ level. A vivid way to show this agreement is to plot the cumulative shift of periastron time as a function of the observation time. Similarly to what we did in eq. (6.42) for the cumulative phase of the rotation of the pulsar around its axis, we can write the accumulated orbital phase $\phi _ { b }$ as

$$
\frac { 1 } { 2 \pi } \phi _ { b } ( T ) = \nu _ { b } T + \frac { 1 } { 2 } \dot { \nu } _ { b } T ^ { 2 } + \ldots ,
$$

where $\nu _ { b } = 1 / P _ { b }$ is the orbital frequency,and we have chosen the origin of $T$ so that a periastron passage $T _ { 0 }$ isat $\phi _ { b } = 0$ .For the Hulse--Taylor pulsar,the terms proportional to $\ddot { \nu } _ { b }$ and higher are negligible.The $n$ -th time of periastron passage, $T _ { n }$ ,takes place when $\phi _ { b } ( T _ { n } ) = 2 \pi n$ ,i.e.

$$
\nu _ { b } T _ { n } + \frac 1 2 \dot { \nu } _ { b } T _ { n } ^ { 2 } = n .
$$

Thus, the cumulative diference between the periastron passages $T _ { n }$ and the values $n / \nu _ { b }$ is given by

$$
T _ { n } - \frac { n } { \nu _ { b } } = - \frac { \dot { \nu } _ { b } } { 2 \nu _ { b } } T _ { n } ^ { 2 } ,
$$

or, in terms of $P _ { b } = 1 / \nu _ { b }$ ，

$$
T _ { n } - \biggl | P _ { b } n = \frac { \dot { P } _ { b } } { 2 P _ { b } } T _ { n } ^ { 2 } .
$$

This is a parabola with coefficjent given by $( \dot { P } _ { b } ) / ( 2 P _ { b } ) < 0$ and,as we see in Fig.6.7,the agreement between the data and the theory is extremely good,and remarkably stable along the years.Observe that the uncertainty in the galactic acceleration (the first term in eq. (6.104) dominates the experimental error,and is the limiting factor in the comparison with general relativity.

Finally,we mention that recent observations indicate a variation of tle pulse profile of the Hulse-Taylpr binary pulsar.This is consistent witl the fact that the pulsar is undergoing geodetic precession (a general relativistic effect due to the spin-orbit coupling). The period of this geodetic precession is about 30O yr,and the data suggest that the pusar's beam will no longer intersect our line of sight after the year 2025. so the pulsar will become unobservable.

# 6.3The double pulsar,and more compact binaries

Double NS systems are rare.Even if the original binary star system survived the first supernova explosion,it will typically be disrupted by the second supernova explosioh．Furthermore,in pulsar surveys there are selection effects against NS-NS systems,because the modulation ol the period of the pulsar due to its orbital motion makes the detection more difficult.Still,after the discovery of the Hulse-Taylor pulsar,PSR $\mathrm { B } 1 9 1 3 { + } 1 6$ ，anumber of other NS-NS binaries have been discovered Presently (2007) there are five system whose identification with Ns NS binaries is considered certain, because the masses of the two stars have been measured,and found to be very close to the value $\simeq 1 . 3 M _ { \odot }$ expected fora NS.These are shown in Table 6.2. Furthermore,there are at least three more binary systems (PSR J1518+4904,J1811-1736 and $\mathrm { J 1 8 2 9 + 2 4 5 6 }$ ）whose identification with NS-NS binaries is very likely although the two separate masses have not yet been measured with comparable precision. Besides,a number of white dwarf/NS binaries are known.We discuss here the most interesting systems.

# The double pulsar, PSR J0737-3039

This is a very remarkable system,which is already a truly spectaculai laboratory for general relativity,and will become even more so in the next few years. The pulsar PSR J0737-3039,with a period 22.8 ms, was discovered in April 2003 (Burghy et al. 2003),in a survey of the southern sky made with the Parkes 64-m radio telescope in Australia. It was soon found to be a member of the most relativistic binary system evel discovered,with an orbital period $P _ { b }$ bf just $2 . 4 { \mathrm { ~ h r } }$ ：Thus,relativistic effects are even more important than in the Hulse-Taylor pulsar. For instance,its periastron advance is abdut $1 7 ~ \mathrm { d e g / y r }$ ，four times larger than for the Hulse-Taylor pulsar,and could be measured already after a few days of observations.Its coalescence time,of only about $8 6 ~ \mathrm { M y r }$ is the shortest among all NS-NS systems known,see Table 6.2.12 Furthermore,its large flux density and it\$ narrow pulse make possible to have a high timing precision. These features would have already made this system exceptionally interesting.Then,in October 2003,even its companion was detected as a pulsar (Lyne et al. 2oo4),making it the first observed NS-NS system where both neutron stars are pulsars whose beams intersect our line of sight.The pulsar discovered first,labeled as A,is amillisecond pulsar,while the other(B)hasa period of about $2 . 7 \ : \mathrm { s }$ (see Table 6.2). It turned out that the pulses of B change significantly along the orbital phase,probably because of the influence of the energy fux ofA on its magnetosphere,so the beam from B is clearly visible only for two short periods of about 10 min each during its orbital motion (which is the reason why B was not detected initially).

Table 6.2 The five confirmed NS-NS binaries; $\tau$ is the time to coalescence because of GW emission,computed from eqs.(4.136)and (4.140) (setting $G ( e ) = 1 { \ : }$ .For PSR J1756-2251 we assumed $m _ { \mathrm { c } } = 1 . 2 M _ { \odot }$   

<table><tr><td>psr</td><td>P (ms)</td><td>P (hr)</td><td>e</td><td>(a/c)sint (s)</td><td>mp(Mo)</td><td>mc(Mo)</td><td>T (Myr)</td></tr><tr><td>J0737-3039A</td><td>22.7</td><td>2.45</td><td>0.088</td><td>1.42</td><td>1.3381(7)</td><td></td><td>86</td></tr><tr><td>B</td><td>2773.6</td><td></td><td></td><td></td><td></td><td>1.2489(7)</td><td></td></tr><tr><td>B1534+12</td><td>37.9</td><td>10.1</td><td>0.27</td><td>3.73</td><td>1.3332(10)</td><td>1.3452(10)</td><td>2783</td></tr><tr><td>J1756-2251</td><td>28.5</td><td>7.67</td><td>018</td><td>2.76</td><td>2.574(3)-mc</td><td>&lt;1.25</td><td>1660</td></tr><tr><td>B1913+16</td><td>59.0</td><td>7.75</td><td>0617</td><td>2.34</td><td>1.4414(2)</td><td>1.3867(2)</td><td>306</td></tr><tr><td>B2127+11C</td><td>30.5</td><td>8.05</td><td>0.681</td><td>2.52</td><td>1.350(40)</td><td>1.363(40)</td><td>218</td></tr></table>

The fact that we observe both beams allows us to measure separately $x _ { A } = ( 1 / c ) a _ { A } \sin \iota$ and $x _ { B } = ( 1 / c ) a _ { B } | \sin \iota$ ，where $a _ { A }$ and $a _ { B }$ are the major semiaxes of the orbits of the A and B pulsars,respectively. Then, from Kepler's third law,we get their mass ratio,13

$$
R \equiv { \frac { m _ { A } } { m _ { B } } } = \left| { \frac { x _ { B } } { x _ { A } } } \right. ,
$$

while,as usual, once the Keplerian parameters have been measured, from the periastron advance we get the total mass (see eq.(6.93)). Thus, after only two anda half years of obseryations,we already havea rather precise determination of the masses of the two pulsars,see Table 6.2.

Given the importance of relativistic leffects in this system, it has already been possible to extract,from tlie ft to the timing formula,five post-Keplerianparameters,reported in Table6.3.Observe in particular that $\sin \iota = 0 . 9 9 9 7 4$ ,with an error $( - 3 9 , + 1 6 )$ on the last two digits,i.e.

12This also had the effectof increasing by almost one order of magnitude the expected coalescence rate of NS-NS systems,with very important consequences for GW detectors.We will come back to these issues in Vol.2.

$^ { 1 3 } \mathrm { { I t } }$ is also important toobserve that eq.(6.116) is expected to hold not only in general relativity,but in any realistic theory of gravity,at least to 1PN order. Furthermore,this relation is also independent of strong-field effects,which is not the case for the post-Keplerian parameters.

the orbit is seen nearly edge-on, so it is ideally oriented for measuringtl Shapiro delay.Finally,we can add to the list of virtues of this binar system that the timing result\$ indicate that its proper motion is su prisingly small,so the proper motion corrections discussed on page 32 are small. The distance to the pulsar is estimated, from its dispersio measure,to be $d \sim 5 0 0$ pc.

Having fixed the masses using $\langle \dot { \omega } \rangle$ and the mass ratio $R$ ，we are let with four predictions from general relativity,for the four measured quan tities $\dot { P _ { b } } , \dot { \gamma } , r , s$ .Better yet,one can plot the six quantities $\{ R , \dot { \omega } , \dot { P } _ { b } , \gamma ,$ $s \}$ in the plane $( m _ { A } , m _ { B } )$ ,and one finds that all six curves meet at on common point.As shown in Fig.6.8,the agrcement is very remarkabl In particular,for the shape of the Shapiro time dclay, $s$ ，the agreemen between theory and observation is

Table 6.3 The measuredpost-KeplerianparametersforPSR J0737-3039; $s \ = \ \sin \iota$ and $\boldsymbol { r }$ are the shape and range of Shapiro delay, respectively.From Krameret $a l$ (2006).   

<table><tr><td>parameter</td><td>value</td></tr><tr><td>(ω)(deg/yr)</td><td>16.89947(68)</td></tr><tr><td>Y(ms)</td><td>0.3856(26)</td></tr><tr><td>P</td><td>--1.252(17) × 10-12</td></tr><tr><td>S</td><td>0.99974(-39,+16)</td></tr><tr><td>r(μs)</td><td>6.21(33)</td></tr></table>

$$
\frac { s ^ { \mathrm { G R } } } { s ^ { \mathrm { o b s } } } = 0 . 9 9 9 8 7 ( 5 0 )
$$

and we see that general relativity passes this test at the $0 . 0 5 \%$ level This is by far the best available test of general relativity in strong fields even better than the test based on the observed $\dot { P } _ { b }$ for the Hulse-Taylo binary pulsar with a 3O-year data span, compare with eq. (6.5).

Concerning the measure of $\dot { P } _ { b }$ ,the precision obtained after 2.5 years observations is given in Table 6.3. Given that the measured uncertainti in $\dot { P } _ { b }$ decreases approximately as $T ^ { - 2 . 5 }$ ，where $T$ is the data span, expect that in about five years it should be measured at the level $0 . 1 \%$ or better. As we mentioned,the proper motion correction to thi double binary system are quite small, as well as the corrections due t differential acceleration in the galactic potential. This suggests that fo this system one could eventually arrive to a measure of $\dot { P } _ { b }$ at the leve of $0 . 0 2 \%$

Observe that,in Fig.6.8,only the white part of the plot is allowed and the shaded part is excluded.This follows from the fact that,i this binary system，we can measure separately $x _ { A } = ( 1 / c ) a _ { A } \sin \iota$ and $x _ { B } = ( 1 / c ) a _ { B } \sin \iota$ ，where $a _ { A , \dot { B } }$ are the semimajor axes of the orbits o the stars A and B,respectively. From the measure of $x _ { A }$ , together with the orbital period $P _ { b }$ ,one can form the mass function

$$
f _ { A } ( \boldsymbol { m } _ { A } , \boldsymbol { m } _ { B } ) = \left( \frac { 2 \pi } { P _ { b } } \right) ^ { 2 } x _ { A } ^ { 3 } .
$$

Using $a _ { A } = ( m _ { B } / m ) a$ ，where $\begin{array} { r } { m = m _ { A } + m _ { B } } \end{array}$ is the total mass, and $a$ is the semimajor axis of the relative orbit in the CM,and making use $0 1$ Kepler's law $a ^ { 3 } = G m ( P _ { b } / 2 \pi ) ^ { 2 }$ ,the mass function can be written as

$$
f _ { A } ( m _ { A } , m _ { B } ) = \frac { G } { c ^ { 3 } } \frac { ( m _ { B } \sin \iota ) ^ { 3 } } { ( m _ { A } + m _ { B } ) ^ { 2 } } .
$$

Similarly, from $x _ { B }$ and $P _ { b }$ we can form the mass function $f _ { B } ( m _ { A } , m _ { B } )$ Given the measured values of $f _ { A }$ and $f _ { B }$ ,the condition $\sin \iota \leqslant 1$ restricts the allowed region in the $( m _ { A } , m _ { B } )$ plane to the white, wedge-shaped part.The fact that sin $\iota ,$ turns out to be very close to one is reflected in the fact that the intersection between the various curves is very close to the cusp of the wedge-shaped region.

![](images/16b4fe8250eb6f1291fd36b883b8480538892fbad9ce23586cdd8248e6b9f244.jpg)  
Fig.6.8 The mass-mass diagram for the double pulsar system J0737-3039. Inset is an enlarged view of the small square where the various constraints intersect.From Kramer et al. (2006).

With more observation time,the accuracy of these data will increase further,and it is expected that one will soon have to use post-Newtonian corrections to the orbit of higher order than $( v / c ) ^ { 2 }$ .Potentially, this could allow the observation of corrections that depend on the moment of inertia of the neutron stars,and therefore to obtain a direct measure of the NS radius. This will be of great interest, since the mass-radius relation of a NS is characteristic of its equation of state,as we will discuss in Vol. 2.

# PSR B1534+12

Together with the Hulse-Taylor pulsar and the double pulsar, this is the other system in which to date has been possible to measure the decrease in orbital period due to GW emission．It was discovered in 1991 with the Arecibo telescope.It is significantly brighter than the Hulse-Taylor pulsar,and its pulse has a narrow peak,allowing precise liming measurement.Furthermore,the orbit is nearly edge-on,which facilitates the measure of the range $r$ and shape s of the Shapiro delay. As a result,after ten years of data, the five post-Keplerian $\{ \dot { \omega } , \gamma , \dot { P } _ { b } , r , s \}$ parameters have been measured.As discussed above,this in principle llows us to have three independent tests of general relativity,since these five parameters are fixed in terms of the two masses $m _ { p }$ and $m _ { c }$ We see from Fig. 6.9 that the three curves corresponding to $\dot { \omega } , \gamma$ and $s$ meet indeed at a single point in the $( m _ { p } , m _ { c } )$ plane,providing an agreemem between theory and experiment at a level of about $1 \%$ .The value ol $r$ is only measured with a precision of about $2 0 \%$ ，but still its value is centered on the general relativity prediction.There is instead a small discrepancy for $\bar { \dot { P } } _ { b }$ .However,the value of $\dot { P } _ { b }$ is quite sensitive to the correction $v _ { T } ^ { 2 } / d$ in eq. (6.104)，since the pulsar has a significant proper motion and is at a close distance from us.If one estimates the distance $d$ from the dispersion measure,one finds $d \simeq 0 . 7$ kpc.However,this estimate implies a model for the electron distribution in the galaxy (the quantity $n _ { e }$ which enters in eq. (6.37)).This model,due to Cordes and Taylor,has mostly a statistical significance,and can be in error for a single pulsar. After correcting for galactic acceleration and proper motion using eq.(6.104) with $d \simeq \mathrm { 0 . 7 ~ k p c }$ ,one finds

![](images/56f476655821f6318cc2125c664cedfcd964ac2c13cc378541a7ff209c8d0922.jpg)  
Fig.6.9 The mass-mass diagram for PSR B1534+12.From Stairs et al.(2002).

$$
\dot { P } _ { b } ^ { \mathrm { o b s } } - \dot { P } _ { b } ^ { \mathrm { g a l } } = ( - 0 . 1 7 4 \pm 0 . 0 1 1 ) \times 1 0 ^ { - 1 2 } ,
$$

to be compared with the prediction of general relativity

$$
\begin{array} { r } { \dot { P } _ { b } ^ { \mathrm { G R } } = - 0 . 1 9 2 \times 1 0 ^ { - 1 2 } , } \end{array}
$$

so the measured value differs from this prediction by about 1.7 standard deviations. We can however reverse the logic,and assume the correctness of the prediction of general relativity for $\dot { P } _ { b }$ ，which，at this level of precision,is by now established beyond any doubt from the Hulse Taylor pulsar and from the double pulsar,and we can use the measured value of Pb to obtain a better estimate lof the distance d to the pulsar. This method yields $d = 1 . 0 2 \pm 0 . 0 5 ~ \mathrm { k p c }$ 1

# Further reading

· For a general introduction to pulsars, see Lyne and Graham-Smith (2005) and Lorimer (2005).For a catalogue of pulsars see the ATNF catalogue,at www.atnf.csiro.au/research/pulsar/psrcat.

·For the discovery of PSR B1913+l6,see Hulse and Taylor (1975),and the Nobel lectures of Hulse (1994)and of Taylor (1994)．The pbservation of gravitational radiation from PSR B1913+16 is discussed in Taylor,Fowler and McCulldch (1979) and in Taylor and Weisberg (1982,1989)An update of the results is given in Weisberg and Taylor (2002, 2004).

·Pulsar timing is reviewed in Backer and Hellings (1986)and in Stairs (2003). See also the textbooks Will (1993),Straumann (2004) and Lyne and Graham-Smith (2005).A review of the comparison with experiments of general relativistic effects such as Shapiro delay,etc.is given in Will (2006).

·An approximate timing formula was developed by Blanford and Teukolsky (1976)，Epstein (1977, 1979)and Haugan (1985)，and was adequate to describe the earlier data of the Hulse-Taylor pulsar,and to find evidence for GW emission，see Taylor and Weisberg (1982).With improved experimental accuracy it became necessary a full general-relativistic treatment,which was given by Damour and Deruelle (1985,1986).Furthermore, in Damour and Deruelle (1986)it is shown how to parametrize the timing effects in a way common to a wide class of alternative theories of gravitations,performing a theory-independent analysis of the timing data,and therefore comparing general relativity to alternative theories.A comparison of different timing models is given in Taylor and Weisberg (l989).For further discussions of the full general-relativistic treatment see also Damour (1983)and Damour and Taylor (1991,1992).

·The 1PN corrections to $\dot { P } _ { b }$ are computed in Blanchet and Schäfer (1989).This corrections has the effect of multiplying $\dot { P } _ { b }$ bya factor $\left( 1 + X _ { 1 \mathrm { P N } } \right)$ where,for the Hulse-Taylor binary pulsar, $X _ { \tt { 1 P N } } \simeq$ $2 . 1 5 \times 1 0 ^ { - 5 }$ ，far below the accuracy of eq.(6.5). This correction is however larger,and potentially more important，for the double pulsar．Higherorder post-Newtonian corrections,which depend also on the moment of inertia of the star,can be important in the measurement of other relativistic parameters,such as the periastron advance,and are discussed in Damour and Schäfer (1988).

· The discovery of the pulsar PSR JO737-3039A is reported in Burgay et al.(2003) and the detection of the companion as a pulsar in Lyne et al. (2004).The resulting tests of general relativity,including orbital decay because of GW emission,are discussed in Kramer et al. (2005),and updated in Kramer et al. (2006).

·The discovery of PSR B1534+12 is reported in Wolszczan (1991),and updated measurements of its orbital decay and other post-Keplerian parameters arereported in Stairs,Thorsett,Taylor and Wolszczan (2002).

<table><tr><td>Part II Gravitational-wave</td><td>experiments</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>

# Data analysis techniques

In this chapter we begin our study of GW experiments. The functioning principles and the sensitivities of existing or planned detectors will be examined in great detail in the subsequent chapters.In this chapter we rather introduce a number of general qoncepts which characterize any GW detector,and we discuss the cruclal problem of how to extract a GW signal from the (typically much larger) detector noise.

In Section 7.1 we will see how the various noise generated inside a the detector can be conveniently treated referring them to the detector input,and are characterized by a spectral strain sensitivity,which has dimensions $1 / \sqrt { \mathrm { { H z } } }$ ：In Section 7.2 we introduce the pattern functions that encode the detector angular sensitivity. We will then discuss in Section 7.3 the optimum filtering techniques that must be applied to the detector output.The importance of this procedure stems from the fact that,with existing detectors and with reasonable estimates of the GW signal,we expect that the GW signal will be buried into a much larger noise.The fact that we try to extract asmall signal from noisy detectors is certainly not a new situation in physics. Rather on the contrary,it is a typical problem in many fields,e.g.in radio engineering where it has been much studied in connections with radars,or in radio astronomy for application to pulsar searches,and standard filtering techniques have been developed. We will see how these techniques are adapted to the problem of GW detection.The prqper interpretation of the results obtained with matched filtering relies on notions of probability and statistics,that we discuss in Section 7.4.Here,after an introduction to the frequentist and the Bayesian frameworks,we discuss how to reconstruct the parameters of the source and how to examine the statistical significance of the observation of an event with a given signal-to-noise ratio.Then,in Sections 7.5-7.8,we will examine the application of these concepts to various classes of GW signals,i.e. bursts,periodic signals, coalescing binaries and stochastic backgrounds.

# 7.1The noise spectral density

The output of any GW detector is a time series,which describes for instance the oscillation state of a resonant mass,or the phase shift of thelight recombined after traveling in the two arms of an interferometer. This output will bea combination of a true GW signal (hopefully） and of noise.To understand how signal and noise combine, it is useful to tlink of a GW detector as a linear system.At its input there is the GW

7.1 Noise spectral density 335   
7.2 Pattern functions 339   
7.3 Matched filtering 343   
7.4 Probability and statistics 346   
7.5 Bursts 361   
7.6 Periodic sources 371   
7.7 Coalescences 387   
7.8 Stochastic backgrounds 392

signal that we want to detect.More precisely,the input and output the detector are scalar quantities,while the GW is described bya tenso $h _ { i j }$ . So,in general,the input of the detector will have the form

$$
h ( t ) = D ^ { i j } h _ { i j } ( t ) ,
$$

where $D ^ { i j }$ is a constant tensor which depends on the detector geometr and is known as the detector tensor.For example,fora detector which i driven only by the $( x , x )$ component of $h _ { i j }$ (which,as we will see, is th case for a resonant bar oriented along the $x$ axis), $D ^ { i j } = 1$ if $i = j =$ and $D ^ { i j } = 0$ otherwise.We will later compute the explicit form of $D$ for interferometers and for resdnant masses.

For a linear system,the output of the detector is a linear functiom in frequency space,of the input $h ( t )$ ,that is,the output $h _ { \tt o u t } ( t )$ ofthe detector (in the absence of noise) is related to the input $h ( t )$ by

$$
\tilde { h } _ { \mathrm { o u t } } ( f ) = T ( f ) \tilde { h } ( f ) ,
$$

where $T ( f )$ is known as the transfer function of the system. However in the output of any real detecior there will also be noise,so the outpu $s _ { \mathrm { o u t } } ( t )$ will be rather given by

$$
s _ { \mathrm { o u t } } ( t ) =  { h _ { \mathrm { o u t } } } ( t ) + n _ { \mathrm { o u t } } ( t ) .
$$

More precisely,a detector can be modeled as a linear system with mam stages,labeled by $i = 1 , \ldots , N ,$ each one with its own transfer function $T _ { i } ( f )$ ,so the total transfer function is $\begin{array} { r } { T ( f ) = \prod _ { i } T _ { i } ( f ) } \end{array}$ .For example we will see in Chapter 8 that resonant-bar detectors are composed a heavy aluminum cylinder which is set into oscillation by an incoming GW；its energy is then transferred to a lighter mechanical oscillator coupled to the heavy bar,which works as a mechanical amplifier, then it is transformed into an electric signal by an LC circuit coupled to the light oscillator,and then this electric signal is further amplifed by on or more SQUIDs,and recorded.Clearly,noise can be generated at each of these stages.Each noise will propagate to the output with a transfer function which depends on the point of the linear system at which i first appeared,see Fig.7.1,and will contribute to total noise $n _ { \tt o u t } ( t ) { \mathrm { ~ a ~ t ~ } }$ the output. It is convenient tp refer each noise to the detector input. defining the quantity $n ( t )$ from

![](images/a93ddba4ebcb53759ce2bd72c39f23b58bd5a0e7596e1b649d1cd4afc7b6ebb8.jpg)  
Fig.7.1 A schematic representation of a detector as a linear system. The full transfer function $T ( f )$ is the product of the separate transfer function. Here $T ( f ) = T _ { 1 } ( f ) T _ { 2 } ( f )$ ， and $\tilde { n } _ { \mathrm { o u t } } ( f ) ~ = ~ T _ { 1 } ( f ) T _ { 2 } ( f ) n _ { a } ( f ) ~ +$ $T _ { 2 } ( f ) n _ { b } ( f )$

$$
\tilde { n } ( f ) = T ^ { - 1 } ( f ) \tilde { n } _ { \mathrm { o u t } } ( f ) ,
$$

where $n _ { \mathrm { o u t } } ( t )$ is the total noise measured at the output. That is, $n ( t )$ is a fictitious noise that,if it were injected at the detector input,and if there were no other noise inside the detector,would produce at the output the noise $n _ { \mathrm { o u t } } ( t )$ thatis actually observed.It is therefore the quantity that we can compare directly with $h ( t )$ ,i.e.to the effect due to the GW.We then define

$$
s ( t ) = h ( t ) + n ( t ) ,
$$

and we can simply think of the detectoras if $s ( t )$ were its output, composed of a noise $n ( t )$ and a GW signal $h ( t )$ ,1 and the detection problem is how to distinguish $h ( t )$ from $n ( t )$ . In the following,when we speak of the detector output, we will always refer to $s ( t )$ .2 If one has a theoretical model for a given source of noise $n _ { i } ( t )$ ,which appears at a given stage of the linear system,we can compare it with $h ( t )$ simply multiplying it by the inverse of the appropriate trapsfer function,in order to refer this noise to the detector input.Equivalently,of course,one could refer both the noise and the signal to the true detector output,and compare $n _ { \mathrm { o u t } } ( t )$ to the quantity $h _ { \mathrm { o u t } } ( t )$ whose Fourier transform is given by eq.(7.2). However,the great advantage pf referring everything to the input is that $n ( t )$ gives a measure of the minimum value of $h ( t )$ that can be detected and $h ( t )$ ,apart from the geometrical factor $D ^ { i j }$ which is always of order one,depends only on the incoming GW.In contrast, $h _ { \mathrm { o u t } } ( t )$ depends on the transfer function of the system,and different detectors can have transfer functions which differ by many orders of magnitude. Thus, the use of $n _ { \mathrm { o u t } } ( t )$ and $h _ { \mathrm { 0 u t } } ( t )$ would be very unpractical when we want to compare the performances of different detectors.

So,in the above sense, we take $n ( t )$ to be the detector's noise. If the Ioise is stationary,as we assume for the moment,the different Fourier components are uncorrelated,and therefore the ensemble average³ of the Fourier components of the noise is of the form

$$
\langle \tilde { n } ^ { * } ( f ) \tilde { n } ( f ^ { \prime } ) \rangle = \delta ( f - \biggl | f ^ { \prime } ) \frac { 1 } { 2 } S _ { n } ( f ) .
$$

The above equation defines the functibn $S _ { n } ( f )$ Since $n ( t )$ isreal, $\tilde { n } ( - f ) = \tilde { n } ^ { * } ( f )$ and therefore $S _ { n } ( - f ) \ne S _ { n } ( f )$ If $n ( t )$ is dimensionless, as we will assume, $S _ { n } ( f )$ has dimensions $\mathrm { H z ^ { - 1 } }$ Without loss of generality,we can also assume that

$$
\langle n ( t ) \rangle = 0 | .
$$

Observe that， for $f ~ = ~ f ^ { \prime }$ ，the right-hand side of eq.(7.6) diverges. However, in any real experiment we have a finite value of the time T used to measure $\tilde { n } ( f )$ ，see Note 3.Restricting the time interval to $- T / 2 < t < T / 2$ we have

$$
\delta ( f = 0 )   [ \int _ { - T / 2 } ^ { T / 2 } d t e ^ { i \ell \pi f t } ] | _ { f = 0 } = T .
$$

Then, from eq. （7.6) with $f = f ^ { \prime }$ ,we get

$$
\left. \left| \tilde { n } ( f ) \right| ^ { 2 } \right. = \frac { 1 } { 2 } S _ { n } ( f ) T .
$$

Fora function defined on the interval $[ - T / 2 , T / 2 ]$ , the Fourier modes ave discrete frequencies $f _ { n } = n / T$ ，sothe resolution in frequency is iven by

1One often multiplies the detector output by $T ^ { - 1 } ( f )$ already at the level of data acquisition,so in this sense $s ( t )$ is really the output of the data acquisition system.

$$
\Delta f = { \frac { 1 } { T } } .
$$

2Some more nomenclature:we willalways use the word “event”to indicate that in the detector happened something，which deserves further scrutiny. At this stage,it could be due to a GW or(much more likely）to noise.An event which is already assumed to have been generated by a GW will be called a “GW signal". The letter $s$ conventionally used to denote the detector output $s ( t ) = h ( t ) + n ( t )$ does not stand for “signal" (the signal in this nomenclature is $h ( t ) )$ . It can rather be taken to denote the“strain amplitude”of the detector.

3The ensemble average is the average over many possible “realizations"of the system．In practice we have only one physical system,our detector,but we can follow it in time,so the ensemble average is replaced by a time average (this implicitly assumes that the system is ergodic). Then the ensemble average is computed measuring the noise $n ( t )$ over a given time interval $T$ and considering this asa“realization”of the system.From this we obtain $\tilde { n } ( f )$ (with a resolution in frequency $\Delta f = 1 / T$ We then repeat the procedures over a subsequent time stretch,again of duration $T$ and separated by a sufficient time shift from the first realization, so that the correlation between the noise $n ( t )$ in the two stretches can be neglected,and we define this as a second independent realization of the system. Finally, we average $\tilde { n } ( f )$ over many independent realizations.It is useful to keep in mind that a time-scale $T$ is implicit in this procedure,and will indeed appear in the equations below.

We can then write eq. (7.9) also in the form

$$
\frac { 1 } { 2 } S _ { n } ( f ) = \left. | \tilde { n } ( f ) | ^ { 2 } \right. \Delta f .
$$

The factor $1 / 2$ is conventionally inserted in the definition (7.6)of $S _ { n }$ (f so that $\langle n ^ { 2 } ( t ) \rangle$ is obtained integrating $S _ { n } ( f )$ over the physical rang $0 \leqslant f < \infty$ ,rather than from $- \infty$ to $\infty$ ，

$$
\begin{array} { l } { { \displaystyle \langle n ^ { 2 } ( t ) \rangle = \langle n ^ { 2 } ( t = 0 ) \rangle } } \\ { { \displaystyle = \int _ { | - \infty } ^ { \infty } d f d f ^ { \prime } \langle n ^ { * } ( f ) n ( f ^ { \prime } ) \rangle } } \\ { { \displaystyle = \frac { 1 } { 2 } \int _ { - \infty } ^ { \infty } d f S _ { n } ( f ) } } \\ { { \displaystyle = \int _ { 0 } ^ { \infty } d f S _ { n } ( f ) . } } \end{array}
$$

The function $S _ { n } ( f )$ is known as the noise spectral density (or the nois spectral sensitivity,or the noise power spectrum).More precisely, it i called a single-sided spectral density,to emphasize that $\langle n ^ { 2 } ( t ) \rangle$ isob tained from it integrating only over the physical range of frequencie $f > 0$ .Alternatively,we can write

$$
\langle n ^ { 2 } ( t ) \rangle = \int _ { - \infty } ^ { \infty } d f S _ { n } ^ { \mathrm { d o u b l e  s i d e d } } ( f ) ,
$$

with $S _ { n } ^ { \mathrm { d o u b l e ~ s i d e d } } ( f ) = ( 1 / 2 ) S _ { n } ( f )$ . Throughout this book, when we wil use the term spectral density or power spectrum,we will always refer to the single-sided quantity.

Equivalently,the noise of a detector can be characterized by $\sqrt { S _ { n } ( f ) }$ which is called the spectral strain sensitivity,or spectral amplitude,am has dimensions $\mathrm { H z ^ { - 1 / 2 } }$ . Note that,if the noise increases by a factor X $n ( t )  \lambda n ( t )$ ，then $S _ { n } ( f ) \to \lambda ^ { 2 } S _ { n } ( f )$ while the strain sensitivity scale linearly.

Actually the definition (7.6),even if rather intuitive,is not mathe matically rigorous,because the function $n ( t )$ in general does not satisfy the conditions necessary for having a well-defined Fourier transform; fol instance,on the interval $- \infty < t < \infty$ ， $n ( t )$ does not necessarily go to zeroat $t \to \pm \infty$ ,s0 $\tilde { n } ( f )$ in general does not exist.A more precise definition of the spectral density is obtained considering the auto-correlation function of the noise,

$$
R ( \tau ) \equiv \langle n ( t + \tau ) n ( t ) \rangle
$$

A Gaussian stochastic process $n ( t )$ is characterized uniquely by its average value $\langle n ( t ) \rangle$ ,that for a stationary noise is a constant and can be set to zero with a constant shift of $n ( t )$ ，and by its auto-correlation function.Typically, the knowledge of the noise at time $t$ gives us very little information on the value of the noise at a subsequent time $t + \tau$ with $\tilde { 1 }$ sufficiently large,that is,for $| \tau |  \infty$ ， $R ( \tau )$ goes to zero quite fast, e.g exponentially, $R ( \tau ) \sim \exp \{ - | \tau | / \tau _ { c } \}$ . The limiting case is white noise,in which the noise at time $t$ and at any subsequent time $t + \tau$ are totally uncorrelated, so for $\tau \neq 0$ we have $\langle \bar { n } ( t + \tau ) \bar { n } ( t ) \rangle = \langle n ( t + \tau ) \rangle \langle n ( t ) \rangle = 0$ and $R ( \tau ) \sim \delta ( \tau )$

The auto-correlation function therefore goes to zero very fast as $\tau $ $\pm \infty$ ,and it satisfies the requirements for performing the Fourier trans-$S _ { n } ( f )$

$$
\frac { 1 } { 2 } S _ { n } ( f ) \equiv \int _ { - \infty } ^ { \infty } d \tau \ : \bar { R } ( \tau ) \ : e ^ { i 2 \pi f \tau } .
$$

The reality of $R ( \tau )$ implies $S _ { n } ( - f ) = S _ { n } ^ { * } ( f )$ ， while invariance under time translations gives $R ( - \tau ) = \langle n ( t - \tau ) n ( t ) \rangle = \langle n ( t ) n ( t + \tau ) \rangle = R ( \tau )$ ， which implies $S _ { n } ( - f ) = S _ { n } ( f )$ .Inverting eq. (7.15),

$$
\begin{array} { l } { { \displaystyle R ( \tau ) \equiv \langle n ( t + \tau ) n ( t ) \rangle } } \\ { { \displaystyle \quad = \frac { 1 } { 2 } \int _ { - \infty } ^ { \infty } d f S _ { n } ( f ) e ^ { - i 2 \pi f \tau } , } } \end{array}
$$

and in particular

$$
\begin{array} { l } { { \displaystyle R ( 0 ) = \langle n ^ { 2 } ( t ) \rangle } } \\ { { \displaystyle ~ = \frac { 1 } { 2 } \int _ { - \infty } ^ { \infty } d f S _ { n } ( f ) } } \\ { { \displaystyle ~ = \int _ { 0 } ^ { \infty } d f S _ { n } ( f ) . } } \end{array}
$$

Comparing this result with eq.(7.12)|we see that, when $\tilde { n } ( f )$ exists, cqs. (7.6) and (7.15) are equivalent definitions of $S _ { n }$ .Otherwise,only eq. (7.15)applies. Equation (7.15) is known as the Wiener-Khintchin relation.

f $R ( \tau ) \sim \delta ( \tau )$ ,we see from eq.(7.15) that $S _ { n } ( f )$ is independent of frequency and therefore we have white noise. If instead $S _ { n } ( f )$ depends $_ { \mathrm { ~ \tiny ~ o n ~ } f }$ ,one speaks generically of colored noise.A typical example is $1 / f$ noise,which is a generic denomination for a noise where $S _ { n } ( f )$ hasa power-law behavior, $S _ { n } ( f ) \sim 1 / f ^ { \gamma }$ ,over many decades in frequency.

# 7.2 Pattern functions and angular sensitivity

Fromeq. (1.58), we know that a GW with a given propagation direction I can be written as

$$
h _ { i j } ( t , { \bf x } ) = \sum _ { A = + , \times } e _ { i j } ^ { A } ( \hat { \bf n } ) \int _ { - \infty } ^ { \infty } d f \ : \tilde { h } _ { A } ( f ) \ : e ^ { - 2 \pi i f ( t - \hat { \bf n } \cdot { \bf x } / c ) } ,
$$

where $e _ { i j } ^ { A }$ are the polarization tensors given in eq. (1.54). We take $\mathbf { x } = 0$ Sthe location of the detector.For a detector which is sensitive only GWs with a reduced wavelength much larger than its size,such as resonant masses and ground-based interferometers,we have $2 \pi f { \hat { \mathbf { n } } } \cdot \mathbf { x } =$ $\hat { \mathbf { n } } \cdot \mathbf { x } / \dot { \bar { \lambda } } \ll 1$ over the whole detector,and we can neglect the spati dependence of $h _ { a b } ( t , \mathbf { x } )$ . So,to study the interaction of GWs with sud detectors we can write simply

$$
\begin{array} { l } { { \displaystyle h _ { i j } ( t ) = \sum _ { A = + , \times } \epsilon _ { i j } ^ { A } ( \hat { \bf n } ) \int _ { - \infty } ^ { \infty } d f \tilde { h } _ { A } ( f ) e ^ { - 2 \pi i f t } } } \\ { { \displaystyle ~ = \sum _ { A = + , \times } \epsilon _ { i j } ^ { A } ( \hat { \bf n } ) h _ { A } ( t ) . } } \end{array}
$$

Combining this with eq. (7.1)we see that the contribution of GWs t the scalar output of the detector can be written as

$$
h ( t ) = \sum _ { A = + , \times } D ^ { i j } e _ { i j } ^ { A } ( \hat { \bf n } ) h _ { A } ( t ) .
$$

It is then convenient to definelthe detector pattern functions $F _ { A } ( \hat { \mathbf { n } } )$

The pattern functions depend bn the direction $\hat { \bf n } = ( \theta , \phi )$ of propagatiol of the wave,and in terms of them eq.(7.20) becomes

$$
\boxed { \begin{array} { r l } & { h ( t ) = h _ { + } ( t ) F _ { + } ( \not \theta , \phi ) + h _ { \times } ( t ) F _ { \times } ( \theta , \phi ) . } \end{array} }
$$

The above equations assume that we have chosen a system of axes (u,v in the plane orthogonal to the propagation direction $\hat { \bf n }$ of the wave, witl respect to which the polarizations $h _ { + }$ and $h _ { \times }$ are defined. It is interestin to see what happens if we change this system of axes，performing rotation by an angle $\psi$ in the transverse plane. Then the axes $( \hat { \mathbf { u } } , \hat { \mathbf { v } } )$ are rotated to new axes $( \hat { \mathbf { u } } ^ { \prime } , \hat { \mathbf { v } } ^ { \prime } )$ given by

$$
\begin{array} { r } { \hat { \mathbf { u } } ^ { \prime } = \hat { \mathbf { u } } \cos \psi - \hat { \mathbf { v } } \sin \psi , } \\ { \hat { \mathbf { v } } ^ { \prime } = \hat { \mathbf { u } } \sin \psi + \hat { \mathbf { v } } \cos \psi , } \end{array}
$$

where we used the same conventions on the sign of $\psi$ as in eqs. (2.188) and (2.194).With respect to the $( \hat { \mathbf { u } } , \hat { \mathbf { v } } )$ axes,the amplitudes of the plus and cross polarizations have values $h _ { + }$ and $h _ { \times }$ ，while with respect to the $( \hat { \mathbf { u } } ^ { \prime } , \hat { \mathbf { v } } ^ { \prime } )$ axes,they have the values $h _ { + } ^ { \prime }$ and $h _ { \times } ^ { \prime }$ .Equations (1.49)and (1.50) show that $h _ { + } ^ { \prime }$ and $h _ { \times } ^ { \prime }$ are related to $h _ { + }$ and $h _ { \times }$ by

$$
\begin{array} { r } { h _ { + } ^ { \prime } = h _ { + } \cos 2 \psi - h _ { \times } \sin 2 \psi , } \\ { h _ { \times } ^ { \prime } = h _ { + } \sin 2 \psi + h _ { \times } \cos 2 \psi . } \end{array}
$$

In the new frame,the definition (1.54) states that the polarization ten sors are given by

$$
( e _ { i j } ^ { + } ) ^ { \prime } ( \hat { \bf n } ) = \hat { \bf u } _ { i } ^ { \prime } \hat { \bf u } _ { j } ^ { \prime } - \hat { \bf v } _ { i } ^ { \prime } \hat { \bf v } _ { j } ^ { \prime } | , ~ ( e _ { i j } ^ { \times } ) ^ { \prime } ( \hat { \bf n } ) = \hat { \bf u } _ { i } ^ { \prime } \hat { \bf v } _ { j } ^ { \prime } + \hat { \bf v } _ { i } ^ { \prime } \hat { \bf u } _ { j } ^ { \prime } .
$$

Then,using eq.(7.23), we find

$$
\begin{array} { r l } & { ( e _ { i j } ^ { + } ) ^ { \prime } ( \hat { \bf n } ) = e _ { i j } ^ { + } ( \hat { \bf n } ) \cos 2 \psi - e _ { i j } ^ { \times } \sin 2 \psi , } \\ & { ( e _ { i j } ^ { \times } ) ^ { \prime } ( \hat { \bf n } ) = e _ { i j } ^ { + } ( \hat { \bf n } ) \sin 2 \psi + e _ { i j } ^ { \times } \cos 2 \psi . } \end{array}
$$

The pattern functions $F _ { A }$ depends on the polarization tensors $e _ { i j } ^ { A }$ through eq. (7.21). Since the detector tensor is a fixed quantity, independent of $\psi$ ,we find that in the new frame

$$
\begin{array} { r } { F _ { + } ^ { \prime } ( \hat { \mathbf { n } } ) = F _ { + } ( \hat { \mathbf { n } } ) \cos 2 \psi - F _ { \times } ( \hat { \mathbf { n } } ) \sin 2 \psi , } \\ { F _ { \times } ^ { \prime } ( \hat { \mathbf { n } } ) = F _ { + } ( \hat { \mathbf { n } } ) \sin 2 \psi + F _ { \times } ( \hat { \mathbf { n } } ) \cos 2 \psi . } \end{array}
$$

Combining this transformation of the pattern functions with the transformation of $h _ { + } , h _ { \times }$ given in eqs. (7.24) and (7.25), we see that $h ( t )$ in eq. (7.22) is independent of $\psi$

Of course,once a choice of the axes $( \hat { \mathbf { \mu } } , \hat { \mathbf { v } } )$ used to define the polarization is made, then the pattern functions $F _ { A }$ depends on $\theta$ and $\phi$ only. However,it is sometime useful to keep generic the definition of the $( \hat { \mathbf { u } } , \hat { \mathbf { v } } )$ axes in the transverse plane,and to paiametrize the possible choices by the angle $\psi$ .In this case,the pattern finctions depend also on $\psi$ ，and

$$
\begin{array} { r l } & { F _ { + } ( \hat { \bf n } ; \psi ) = F _ { + } ( \hat { \bf n } ; 0 ) \cos 2 \psi - F _ { \times } ( \hat { \bf n } ; 0 ) \sin 2 \psi , } \\ & { F _ { \times } ( \hat { \bf n } ; \psi ) = F _ { + } ( \hat { \bf n } ; 0 ) \sin 2 \psi + F _ { \times } ( \hat { \bf n } ; 0 ) \cos 2 \psi . } \end{array}
$$

A useful identity satisfed by the pattern functions,independently of the specifc form of the detector tensor $D _ { i j }$ ,is4

$$
\int \frac { d ^ { 2 } \hat { { \bf n } } } { 4 \pi } F _ { + } ( \hat { { \bf n } } ) F _ { \times } ( \hat { { \bf n } } ) = 0 ,
$$

where as usual $d ^ { 2 } { \hat { \mathbf { n } } } = d \cos \theta d \phi$ is the ihtegral over the solid angle.As for the integral over $d ^ { 2 } { \hat { \mathbf { n } } }$ of $F _ { + } ^ { 2 }$ and of $F _ { \times } ^ { 2 }$ ,with a generic choice of the angle $\psi$ they are different.We will see for instance that one can choose $\psi \ : \mathrm { s } 0$ that $F _ { \times }$ vanishes while $F _ { + }$ is non-zero,or viceversa．However,if we average over the angle $\psi$ ,we find

$$
\int _ { 0 } ^ { 2 \pi } \frac { d \psi } { 2 \pi } F _ { + } ^ { 2 } ( \hat { \mathbf { n } } ; \psi ) = \int _ { 0 } ^ { 2 \pi } \frac { d \psi } { 2 \pi } F _ { \times } ^ { 2 } ( \hat { \mathbf { n } } ; \psi ) .
$$

In fact,inserting eqs. (7.31) and (7.32) into eq. (7.34)，the equality follows from $\begin{array} { r } { \int d \psi \sin 2 \psi \cos 2 \psi = 0 } \end{array}$ and $\textstyle { \int d \psi \sin ^ { 2 } \psi = \int d \psi \cos ^ { 2 } \psi }$ From this,italso trivially follows that

where

$$
\begin{array} { l } { { \displaystyle \langle F _ { + } ^ { 2 } \big ( \hat { \mathbf { n } } ; \psi \big ) \rangle = \langle F _ { \times } ^ { 2 } \big ( \hat { \mathbf { n } } ; \psi \big ) \rangle , } } \\ { { \displaystyle \langle \dots \rangle \equiv \int _ { 0 } ^ { 2 \pi } \frac { d \psi } { 2 \pi } \int \left. \frac { d ^ { 2 } \hat { \mathbf { n } } } { 4 \pi } ( \dots ) \right. . } } \end{array}
$$

For later use we also define the angular efficiency factor

$$
F = \langle F _ { + } ^ { 2 } \rangle + \langle F _ { \times } ^ { 2 } \rangle = 2 \langle F _ { + } ^ { 2 } \rangle .
$$

4Equation (7.33)can be shown in full generality writing

$$
\begin{array} { l } { { \displaystyle \int d ^ { 2 } { \hat { \bf n } } F _ { + } ( { \hat { \bf n } } ) F _ { \times } ( { \hat { \bf n } } ) } } \\ { { \displaystyle = D _ { a b } D _ { c d } \int d ^ { 2 } { \hat { \bf n } } e _ { a b } ^ { + } ( { \hat { \bf n } } ) e _ { c d } ^ { \times } ( { \hat { \bf n } } ) , } } \end{array}
$$

$e _ { a b } ^ { + } ( \hat { \mathbf { n } } ) e _ { c d } ^ { \times } ( \hat { \mathbf { n } } )$   
$\hat { \mathbf { u } } _ { a } \hat { \mathbf { u } } _ { b } \hat { \mathbf { u } } _ { c } \hat { \mathbf { v } } _ { d }$   
and one factor $\hat { \mathbf { v } }$ ,and of similar terms with $\hat { \mathbf { u } }  \hat { \mathbf { v } }$ ：A simple way to see that the integral over $d ^ { 2 } { \hat { \mathbf { n } } }$ vanishes is then to observe that,when we integrate over all possible values of $\hat { \bf n }$ ，for each term $\hat { \mathbf { u } } _ { a } \hat { \mathbf { u } } _ { b } \hat { \mathbf { u } } _ { c } \hat { \mathbf { v } } _ { d }$ there is also a corresponding term obtained with $\hat { \mathbf { u } }  - \hat { \mathbf { u } }$ and $\hat { \mathbf { v } } $ $+ \hat { \mathbf { v } }$ ，which cancels it.

<table><tr><td colspan="2">Detector</td><td colspan="3"></td></tr><tr><td></td><td>F+(0,$;=0）</td><td></td><td>Fx（0,Φ;=0）F</td><td></td></tr><tr><td>interferometers</td><td></td><td>1(1+cos²0)cos 2Φ</td><td>cos0 sin 2Φ</td><td>2/5</td></tr><tr><td>cylindrical bars</td><td>sin²0</td><td>0</td><td></td><td>8/15</td></tr><tr><td>resonant spheres</td><td></td><td></td><td></td><td></td></tr><tr><td>m=0</td><td>(√3/2)sin² 0</td><td></td><td>0</td><td>2/5</td></tr><tr><td>m=1s</td><td>-sinθ co θ sinΦ</td><td></td><td>sinθ cos</td><td>2/5</td></tr><tr><td>m=lc</td><td>sin0coscos</td><td></td><td>sinθsin</td><td>2/5</td></tr><tr><td>m=2s</td><td></td><td>-1(1+cos²0)sin 2Φ</td><td>cos0 cos 2Φ</td><td>2/5</td></tr><tr><td>m=2c</td><td></td><td>(1+cos²0）cos2Φ</td><td>cos0 sin 2Φ</td><td>2/5</td></tr></table>

We will compute the explicit forms of $F _ { + , \times } ( \theta , \phi ; \psi )$ for bars and interferometers,in their respective chapters.We find useful to collect here the result that we will find for interferometers,cylindrical bars and resonant spheres;in Table 7.1 we give the value of $F ( \theta , \phi ; \psi = 0 )$ (with appropriate definitions of the angles,discussed in the table caption and,in more detail,in their respective chapters),and the values of the angular efficiency factor $F$

As we see from the above table,the pattern functions are relatively smooth functions of the position of the source in the sky. On the one hand,this has the positive consequence that GW detectors have a large sky coverage,of almost $4 \pi$ ,except for some blind directions. This is very different from conventional astronomy, where a telescope must point the source very precisely to detect it.The reverse of the coin,however,is that with a single GW detector we cannot determine the position of the source in the sky.A single detector has an output $h ( t )$ that,according to eq.(7.22),depends on four unknown: the two functions $h _ { + , \times } ( t )$ and the angles $( \theta , \phi )$ that give the source position. To disentangle these quantities we need a coincident observation by a network of detectors.With two detectors we have at our disposal their two outputs $h _ { 1 } ( t )$ and $h _ { 2 } ( t )$ and the delay time $\tau _ { 1 2 }$ between these two signals. These three quantities are not yet sufficient to solve for the four unknown $h _ { + } ( t ) , h _ { \times } ( t ) , \theta$ and $\phi$

However,with three interferometers we have five measured quantities, the three functions $h _ { i } ( t )$ ， $i = 1 , 2 , 3$ ，and two independent delay times, so we can solve for $h _ { + } ( t ) , h _ { \times } ( t ) , \theta$ and $\phi .$ The actual accuracy of the reconstruction depends on the signal-to-npise ratio.For typical expected signals,at first-generation interferometers the angular resolution could be of order one square degree.

# 7.3 Matched filtering

We have seen above that the detector output will be of the general form $s ( t ) = h ( t ) + n ( t )$ .Naively,one might then think that we can detect a GW signal only when $| h ( t ) |$ islarger than $| n ( t ) |$ .This would be very unfortunate since we will see that,with plausible estimates of tle expected GW signals bathing the Earth,and with the sensitivity of the present generation of detectors,we will rather be in the situation $| h ( t ) | \ll | n ( t ) |$

The fundamental question that we ask in this section is then how can we dig out the GW signal from a much larger noise.This is a classical problem in many fields of physics or in radio engineering,and the answer is that we can detect values of $h ( t )$ much smaller than the floor of the noise if we know,at least to some level of accuracy, the form of $h ( t )$ .5 To understand the basic idea,we can first illustrate a simple version of this “filtering”procedure,before moving to optimal filtering.Suppose that $s ( t ) = h ( t ) + n ( t )$ ,and that we know the form of the GW signal $h ( t )$ that we are hunting for. Then we can multiply the output $s ( t )$ by $h ( t )$ ,integrate over an observation time $T$ ,and divide by $T$ ，

$$
\frac { 1 } { T } \int _ { 0 } ^ { T } d t s ( t ) h ( t ) = \frac { 1 } { T } \int _ { 0 } ^ { T } d t h ^ { 2 } ( t ) + \frac { 1 } { T } \int _ { 0 } ^ { T } d t n ( t ) h ( t ) .
$$

The crucial point now is that $h ( t )$ and $n ( t )$ ,separately,are oscillating functions.However,the integrand of the first integral on the right-hand side is definite positive; it might be for instance the integral of something like $\cos ^ { 2 } \omega t$ ,times a slowly varying function of time;this integral then grows,for large T,as T. Its value averaged over a time T is therefore of order one in $T$ ，

$$
\frac { 1 } { T } \int _ { 0 } ^ { T } d t h ^ { 2 } ( t ) \ d t \sim h _ { 0 } ^ { 2 } ,
$$

where $h _ { 0 }$ is the characteristic amplitude of the oscillating function $h ( t )$ In contrast,since the noise $n ( t )$ and our chosen function $h ( t )$ are uncorrelated, the quantity $n ( t ) h ( t )$ is oscillating,and its integral will grow onlyas $T ^ { 1 / 2 }$ for large $T$ (as is typical df systems performing a random walk), s0

$$
\frac { 1 } { T } \int _ { 0 } ^ { T } d t n ( t ) h ( t ) \sim \Big ( \frac { \tau _ { 0 } } { T } \Big ) ^ { 1 / 2 } n _ { 0 } h _ { 0 } ,
$$

where $n _ { 0 }$ is the characteristic amplitude of the oscillating function $n ( t )$ ， and $\tau _ { 0 }$ a typical characteristic time,e.g.the period of the oscillating

5 More precisely，we must know $h ( t )$ and have an idea of the typical scales of variations of the noise,in order to exploit their different behaviors.

6We limit ourselves to linear filters,i.e. filters in which $\hat { s }$ is linear in $s ( t )$ ,asin eq. (7.41).

function $h ( t )$ .Thus,in the limit $T \to \infty$ ,the second term on the right hand side of eq.(7.38) averages to zero,and we have “filtered out” th contribution of the noise from the output. Of course,in practice we can not sent $T$ to infinity,either because the signal $h ( t )$ itself has a limited temporal duration or because we are limited by the total available ob servation time.Still we see that,to detect the signal given in eq. (7.39) against the background of eq. (7.40),it is not necessary to have $h _ { 0 } > n _ { 0 } ,$ but it suffices to have $h _ { 0 } > ( \tau _ { 0 } / T ) ^ { 1 / 2 } n _ { 0 }$ . For example, for a periodic sig nal with a period $\tau _ { 0 } \sim 1$ ms,such as a millisecond pulsar,observed for $T = 1$ yr, we have $( \tau _ { 0 } / T ) ^ { 1 / 2 } \sim 1 0 ^ { - 5 }$ .Wecanthereforedig verydeepl into the noise floor.

After having discussed the intuitive idea,let us see how the above procedure can be made more precise mathematically,and optimized in order to obtain the highest possible value of the signal-to-noise ratio We define

$$
\hat { s } = \int _ { - \infty } ^ { \infty } d t s ( t ) K ( t ) ,
$$

where $K ( t )$ is called the filter function. We assume that we know whal GW signal we are looking for,i.e. we know the form of $h ( t )$ We then ask what is the filter function that maximizes the signal-to-noise ratio for such a signal. Since the filter function is chosen so to“match”the signal that we are looking for,the technique is called matched filtering.

The signal-to-noise ratio (in|amplitude) is defined as $S / N$ ，where $s$ is the expected value of $\hat { s }$ when the signal is present,and $N$ is the rms value of $\hat { s }$ when the signal is absent. Since $\langle n ( t ) \rangle = 0$ ,we have

$$
\begin{array} { l } { S = \displaystyle \int _ { - \infty } ^ { \infty } d t \langle s ( t ) \rangle K ( t ) } \\ { \displaystyle = \int _ { - \infty } ^ { \infty } d t h ( t ) K ( t ) } \\ { \displaystyle = \int _ { - \infty } ^ { \infty } d f \tilde { h } ( f ) \tilde { K } ^ { * } ( f ) , } \end{array}
$$

while

$$
\begin{array} { l } { { \displaystyle N ^ { 2 } = \left[ \langle \hat { s } ^ { 2 } ( t ) \rangle - \langle \hat { s } ( t ) \rangle ^ { 2 } \right] _ { h = 0 } } } \\ { { \displaystyle ~ = \langle \hat { s } ^ { 2 } ( t ) \rangle _ { h = 0 } } } \\ { { \displaystyle ~ = \int _ { - \infty } ^ { \infty } d t d t ^ { \prime } K ( t ) K ( t ^ { \prime } ) \langle n ( t ) n ( t ^ { \prime } ) \rangle } } \\ { { \displaystyle ~ = \int _ { - \infty } ^ { \infty } d t d t ^ { \prime } K ( t ) K ( t ^ { \prime } ) \int _ { - \infty } ^ { \infty } d f d f ^ { \prime } e ^ { 2 \pi i f t - 2 \pi i f ^ { \prime } t ^ { \prime } } \langle \tilde { n } ^ { * } ( f ) \tilde { n } ( f ^ { \prime } ) \rangle . } } \end{array}
$$

Using eq.（7.6) we obtain

$$
N ^ { 2 } = \int _ { - \infty } ^ { \infty } d f \frac { 1 } { 2 } S _ { n } ( f ) | \tilde { K } ( f ) | ^ { 2 } ,
$$

and therefore

$$
\frac { S } { N } = \frac { \int _ { - \infty } ^ { \infty } d f \tilde { h } ( f ) \tilde { K } ^ { * } ( f ) } { \left[ \int _ { - \infty } ^ { \infty } d f ( 1 / 2 ) S _ { n } ( f ) | \tilde { K } ( f ) | ^ { 2 } \right] ^ { 1 / 2 } } .
$$

We now ask what is the filter $K ( t )$ that maximizes $S / N$ ，for a given $h ( t )$ .This variational problem is elegantly solved by defining the scalar product between two real functions $\overset { \smile } { A } ( t )$ and $B ( t )$ ,by

$$
\begin{array} { r l r } & { } & { ( A | B ) = \mathrm { { R e } } \int _ { - \infty } ^ { \infty } d f \frac { \tilde { A } ^ { * } ( f ) \tilde { B } ( f ) } { \left( 1 / 2 \right) S _ { n } ( f ) } \ } \\ & { } & { = 4 { \mathrm { R e } } \int _ { 0 } ^ { \infty } d f \frac { \tilde { A } ^ { * } ( f ) \tilde { B } ( f ) } { S _ { n } ( f ) } , } \end{array}
$$

where Re denotes the real part,and the second line holds because we take $A ( t )$ and $B ( t )$ to be real functions,so that $\tilde { A } ( - f ) = \tilde { A } ^ { * } ( f )$ (recall also that $S _ { n } ( - f ) \ : = \ : S _ { n } ( f ) )$ Since $S _ { n } ( f ) > 0$ ，this scalar product is positive definite.Then eq.(7.45) can be written as

$$
\frac { S } { N } = \frac { ( u | h ) } { ( u | u ) ^ { 1 / 2 } } .
$$

where $u ( t )$ is the function whose Fourier transform is

$$
\tilde { u } ( f ) = \frac { 1 } { 2 } S _ { n } ( f ) \tilde { K } ( f ) .
$$

In this form,the solution is clear.We are searching for the“vector” of unit norm $\hat { n } = u / ( u | u ) ^ { 1 / 2 }$ ，such that its scalar product with the "vector” $h$ is maximum.This is obtained choosing $\hat { n }$ and $h$ parallel, i.e. $\tilde { u } ( f )$ proportional to $\tilde { h } ( f )$ ,so we get

$$
\tilde { K } ( f ) = \mathrm { c o n s t . } \frac { \sqrt { \tilde { h } ( f ) } } { S _ { n } ( f ) } .
$$

The constant is arbitrary, since rescaling $\hat { s }$ by an overall factor does not change its signal-to-noise ratio. Equation (7.49) defines the matched filter (or Wiener filter).7In particular,if we are looking for a signal $h ( t )$ embedded into white noise,so that ${ \tilde { S } } _ { n } ( f )$ is a constant,then the best filteris provided by the signal itself,which is the fltering discussed in eq.(7.38). However,when $\tilde { S } _ { n } ( f )$ is not fat,eq.(7.49) tells us that we must weight less the frequency region where the detector is more noisy, a very natural result.

Inserting the solution (7.49) into eql(7.48) we get $\tilde { u } = \mathrm { c o n s t . } \times \tilde { h }$ Plugging this into eq. (7.47),the overall constant cancels and we get the optimal value of $S / N$ ，

$$
\left( \frac { S } { N } \right) = ( h | h ) ^ { 1 / 2 } ,
$$

that is

$$
\overline { { { \left( \frac { S } { N } \right) } } } ^ { 2 } = 4 \int _ { 0 } ^ { \infty } d f \frac { | \tilde { h } ( f ) | ^ { 2 } } { S _ { n } ( f ) } ,
$$

which is the optimal value of the signal-to-noise ratio.8 The above equations are completely general,and independent of the form of $\tilde { h } ( f )$ In Sections 7.5-7.8 we will apply them to some specific signals.

$^ 7 \mathrm { { I t } }$ is also common in the Jiterature to write eq.(7.4l) in the form $\begin{array} { r l } { \hat { s } } & { { } = } \end{array}$ $\textstyle \int _ { - \infty } ^ { \infty } d t s ( t ) G ( - t )$ and to call $G ( t )$ the filter function. So $G ( t ) = K ( - t )$ and $\tilde { G } ( f ) \sim \tilde { h } ^ { * } ( f ) / S _ { n } ( f )$

$^ { 8 } \mathrm { R e c a l l }$ from Section 7.1 that our $S _ { n } ( f )$ is single-sided．In terms of the double-sided spectral density,defined after eq. (7.13),we have $\begin{array} { l } { \displaystyle { \ddot { ( S / N ) ^ { 2 } } = } } \end{array}$ $\begin{array} { r } { \int _ { - \infty } ^ { \infty } d f | \tilde { h } ( f ) | ^ { 2 } \big / S _ { n } ^ { \mathrm { d o u b l e ~ s i d e d } } ( f ) } \end{array}$