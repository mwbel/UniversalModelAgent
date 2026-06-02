Herget,P.(1948).ComputationofOrbits.Willmann-Bell,Inc.,Richmond,VA:Published privatelyby the author.   
Hilton,J.L.,N.Capitaine,J.Chapront,etal. (2Oo6).Report of the International Astronomical Union DivisionI Working Group onPrecessionand the Ecliptic.Celestial Mechanicsand Dynamical Astronomy 94,351-367.   
IAU(1992).InJ.Bergeron (Ed.),Transactionsof theInternationalAstronomicalUnion,Volume XXIB,Dordrecht,pp.41.Kluwer.Proc.21st General Assembly,BeunosAires,1991.   
IAU(1999).InJ.Andersen (Ed.),Transactionsof theInternational Astronomical Union,Volume XXIII B,Dordrecht,pp.40.Kluwer.Proc.23rd GeneralAssembly,Kyoto,1997.   
IAU(2001).InH.Rickman(Ed.),Transactionsof theInternational AstronomicalUnion,Volume XXIVB,San Francisco.Astronomical Society of the Pacific.Proc.24th General Assembly, Manchester,2000.   
IAU(2007).InO.Engvold (Ed.),Transactionsofthe InternationalAstronomical Union,Volume XXVB,San Francisco.Astronomical Society of the Pacific.Proc.25th General Assembly, Sydney,2003.   
IAU(2008).In K.A.vander Hucht (Ed.),Transactions of the International Astronomical Union, VolumeXXVIB,Cambridge.Cambridge UniversityPress.Proc.26th General Assembly,Prague, 2006.   
IERS(2OO4).Conventions(2Oo3).Technical Note32,International EarthRotation Service,Frankfurt amMain.Verlag des Bundsesants fur Kartographie und Geodesie,D.D.McCarthy and G.Petit (Eds.).   
IERS (2009).The Second Realizationof the International Celestial Reference Frame By VeryLong Baseline Interferometry.TechnicalNote35,International EarthRotationService,Frankfurtam Main. Verlag des Bundsesants fur Kartographie und Geodesie,A.Fey and D.Gordon (Eds.).   
IUGG(1994).Bulletin Geodesique 66,128-129.   
Kaplan, G.H. (2oo5).The IAUResolutions on Astronomical Reference Systems,Time Scales,and EarthRotation Models.Circular179,U.S.Naval Observatory,Washington,DC.   
Kovalevsky,J.,L.Lindegren,M. A.C.Perryman,etal. (1997).TheHIPPARCOScatalogue asa realisationof theextragalacticreference system.AstronomyandAstrophysics323,620-633.   
Kovalevsky,J.andP.K.Seidelmann (2004).Fundamentals ofAstrometry.Cambridge:Cambridge University Press.   
Meeus,J.(1989).Transits.Richmond,VA.:Willman-Bell,Inc.   
Mueller,I.I. (1969).Spherical andPractical AstronomyasApplied to Geodesy.NewYork: Ungar.   
Nautical Almanac OfficesofUKandUSA(1961).Explanatory Supplement toTheAstronomical EphemerisandTheAmerican EphemerisandNauticalAlmanac.London:HerMajesty's Stationery Office.   
Seidelmann,P.K.(Ed.) (1992).Explanatory Supplement toTheAstronomicalAlmanac.Mill Valley, CA:University Science Books.   
Seidelmann,P.K.and J. Kovalevsky (2O02).Application of the new concepts and definitions (ICRS, CIP,and CEO) in fundamental astronomy.Astronomy and Astrophysics392,341-351.   
Woolard,E.W.and G.M. Clemence (1966).Spherical Astronomy.New York and London: Academic Press.

# Relativity for Astrometry, Celestial Mechanics and Metrology

M.SOFFEL&S.KLIONER

# 2.1 Introduction

Mosthigh precision astronomical techniques have passed the threshold wherea Newtonian formulationisno longer sufficientand Einstein's theoryof gravity(General RelativityTheory, GRT)has to be employed as the basis.

Thispoint is especially obvious in the field of astrometry.It iswell known that the gravitational light-deflection at the limb of the Sun amounts to $1 ^ { \prime \prime } 7 5$ and decreasesas $1 / r$ with increasingimpact parameter $r$ ofalight rayto the solarcenter.Thus,for light raysincident at about $9 0 ^ { \circ }$ from the Sun,the angle of light-deflection still amounts to 4 milliarcseconds (mas).To describe the accuracy of astrometric measurements it is useful to make use of the parameter $\gamma$ of the parametrized post-Newtonian (PPN) formalism.In the PPN formalism, theangle of light-deflectionisproportional to $( \gamma + 1 ) / 2$ ,sothatastrometricmeasurements can be used fora precise determination of the parametery.An advanced processing of VLBI data provided the estimates $\gamma = 0 . 9 9 9 6 \pm 0 . 0 0 1 7$ (Lebach etal.1995) and $\gamma = 0 . 9 9 9 9 4 \pm$ 0.00031(Eubanks et al.1997).Current accuracy of modernoptical astrometry,as represented bytheHipparcoscatalog,isabout1 mas,which gavea determination of $\gamma$ at the level of $0 . 9 9 7 \pm 0 . 0 0 3$ (Froeschlé,Mignard,and Arenou1997).Finally,in2003 the accuracy for $\gamma$ was improved by the CASSINIDoppler experiment (Bertotti,Iess,and Tortora 2O03) which gave $\gamma = 1 + ( - 2 . 1 \pm 2 . 3 ) \times 1 0 ^ { - 5 } .$ Future astrometric missions such as GAIA will push the accuracy even belowthis limit.The accuracy of such future missionswill beat the level of a few microarcseconds $( \mu \mathrm { a s } )$ ,where the light-deflection caused by the oblateness of the Jupiter or the post-post Newtonian light-deflection near the limb of the Sun will become measurable.

Relativity crucially enters the problem of time measurement,time dissemination,and timescales.The main reason for that is the improvement of frequency oscillators (atomic clocks）and the fact that relativistic effects are most pronounced in the time domain. Cesium fountain clocks achieve stabilities of better than one part in $1 0 ^ { 1 5 }$ when averagedovera day.Meanwhile,optical clocks with frequencies approaching $1 0 ^ { 1 5 } \mathrm { H z }$ are stable to almost one part in $1 0 ^ { 1 5 }$ simply by averaging over a few seconds. Such stable clocks allow highly accurate use of various space techniques like Very Long Baseline Interferometry (VLBI),GPS,SateliteLaser Ranging (SLR) or Lunar Laser Ranging (LLR).The precision of these techniques is so high that relativity has to be taken into account to fully exploit their observational potential (Muller,Soffel,and Klioner 2008). Note,that relativistic effectsproduced by the gravity field of the Earth itself are of order

$U _ { E } / c ^ { 2 } \simeq 7 \times 1 0 ^ { - 1 0 }$ in the vicinity of its surface.At present several clock experiments in terrestrial orbit are planned,such as the Atomic Clock Ensemble in Space project (ACES,Lemonde et al.2Oo1) that requiresa detailed account of many subtle relativistic effects.

Finally we would like to mention the problem of geodesic precession-nutation (a relativistic effect that is discussed in more detail below,e.g.,Misner,Thorne,andWheeler1973; Soffel1989)and the description of Earth's rotation in a suitably chosen Geocentric Celestial Reference System(GCRS).Geodesic precession amounts to $1 \%$ per century and geodesic nutationisdominatedbyanannual termwithamplitude $0 . 1 5 \mathrm { m a s }$ Since the GCRS ischosen to be kinematically non-rotating,geodesic precession-nutation should be contained in the model describing the relation between the GCRSand the International Terrestrial Reference System (ITRS).According to the International Astronomical Union (IAU) 2Ooo Resolution B1.6 this relativistic precesson-nutation is indeed contained in the present IAU precession-nutation model (IAU2001;URL[2]).

These examples show clearly that high-precision modern astronomical observations can no longer be described by Newtoniantheory,butrequire Einstein's theory of gravity.

# 2.2 Newtonian Formalism

Aremarkable feature of Newton's theory of gravity is the absolute character of space and time.Space is Euclidean while the time measured by an observer flows independently of the observer's position,velocity or acceleration,or from the matter and physical fields.In Newton'stheorythereexistCartesian inertialcoordinatesystems $( t , \mathbf { x } )$ that cover the entire Newtonian universe in which dynamical equations of motion show no inertial forces.Such inertialsystemsare relatedbyGalileantransformations.Such inertial coordinates inNewton's theory are unique up to the choice of origin,scales,the orientationof spatial axes,and a constant velocity of origin.If the origin ofan inertial system $\Sigma _ { m }$ with coordinates $( T , \mathbf { X } )$ moveswith constant velocity $\mathbf { v }$ withrespect to the inertial system $\Sigma _ { r }$ with coordinates $( t , \mathbf { x } )$ , then in the simplest case of parallel spatial axes we have

$$
T = t , \qquad { \bf X } = { \bf x } - { \bf v } t .
$$

In astronomy such inertial systems play afundamental role formany purposes.With the origin in the barycenter of the solar system one introduces a (Newtonian) Barycentric Celestial Reference System (BCRS) with coordinates $( t , \mathbf { x } )$ .The transformation (Eq.2.1) with ${ \bf x } _ { E } ( t )$ replacingvt defines the (Newtonian) Geocentric Celestial Reference System (GCRS) with coordinates $( T , \mathbf { X } )$ .Thisgeocentric celestial systemmightbe called quasi-inertial,since thespatial axes are non-rotating in the Newtonian absolute sense whereas the geocenter is accelerated.

The barycentric celestial systemis used for solar systemephemerides,for concepts such as an ecliptic,for interplanetary spacecraft navigation,etc.The positions ofremote astronomical objects such as distant stars or quasars canbe definedin that system.The barycentric celestial system presents the fundamental astrometric system,where concepts such as stellar position, radial velocity,or proper motion can be defined. On the other hand the GCRS is employed for the descriptionof physical processes in the vicinity of the Earth,for satellite theory,the dynamics of the Earth including Earth's rotation,etc.Itis also used for the introduction of concepts like equator and the International Terrestrial Reference System (ITRS).

In Newton's theory inertial coordinates are physically preferredin the sense that they have direct physical meaningand observables can be derived from them directly.Considera light raywith parametrization inBCRScoordinates

$$
{ \bf x } _ { \gamma } ( t ) = { \bf x } _ { 0 } + c { \bf n } ( t - t _ { 0 } )
$$

and a second one given by $\mathbf { x } _ { \gamma } ^ { \prime } ( t ) = \mathbf { x } _ { 0 } ^ { \prime } + c \mathbf { n } ^ { \prime } ( t - t _ { 0 } ) .$ If the observer is at rest with respect to the BCRS,the observed angle $\varphi$ between the two incident lightrays is given by cos $\varphi = \mathbf { n } \cdot \mathbf { n } ^ { \prime }$ , where the dot indicates the usual Euclidean scalar product.Next we consider the same situation but the observer movingwith velocity $\mathbf { \Delta V }$ intheBCRS.For each of the two incident light rays we can associate a Euclidean unit vector of the form ${ \bf { m } } = \alpha ( { \bf { n } } - { \bf { \nabla } } \beta )$ with ${ \boldsymbol { \beta } } = \mathbf { v } / c$ The normalization constant $\alpha$ to first order in $\beta$ is givenby $\alpha \simeq 1 + \mathbf { n } \cdot \beta .$ From these quantities one derives the observed angle $\varphi$ between the two rays according to

$$
\cos \varphi = \mathbf { m } \cdot \mathbf { m } ^ { \prime } = \mathbf { n } \cdot \mathbf { n } ^ { \prime } + ( \mathbf { n } \cdot \mathbf { n } ^ { \prime } - 1 ) ( ( \mathbf { n } + \mathbf { n } ^ { \prime } ) \cdot { \boldsymbol { \beta } } ) + { \mathcal { O } } ( { \boldsymbol { \beta } } ^ { 2 } )
$$

including first-order aberration terms.

InNewton'stheory of gravity the gravitational interactionis described by one single scalar potential $U ( t , \mathbf { x } )$ ,theNewtonian gravitational potential,that in any inertial reference system satisfies the Poisson equation

$$
\Delta U = - 4 \pi G \rho .
$$

Here, $^ { G }$ is the gravitational constant and $\rho$ is the matter density that acts asa gravitational source.In the BCRS we usually assume the Newtonian potential to vanish at spatial infinity, so that the desired solution ofEq.2.4 takes the form

$$
U ( t , { \bf x } ) = G \int d ^ { 3 } x ^ { \prime } \frac { \rho ( t , { \bf x } ^ { \prime } ) } { | { \bf x } - { \bf x } ^ { \prime } | } .
$$

Note that the Poisson equation (Eq.2.4) is linear,i.e.,in the gravitational $N$ -bodyproblem $U$ is given bya sum over the individual bodies $A$ of the form

$$
U = \sum _ { A } U _ { A }
$$

where $U _ { A }$ is givenbyEq.2.5with the integral taken over body $A$ only. Usually in astronomy the explicit expression of the gravitational potential in terms of the matter density,however, is not needed.In astronomy one is usually not interested in the gravitational field inside of the astronomical bodies.In the outer vicinity of some astronomical body, $A$ ,the gravitational potential $U _ { A }$ will admit a convergent power series expansion in terms of the inverse distance to the body's center by means of suitable mass multipole moments (potential coefficients). The usual Newtonian multipole expansion of the Earth in the GCRS reads

$$
U _ { E } ( T , { \bf X } ) = \frac { G M _ { E } } { R } \left[ 1 + \sum _ { l = 2 } ^ { \infty } \sum _ { m = 0 } ^ { l } \left( \frac { R _ { E } } { R } \right) ^ { l } P _ { l m } ( \cos \theta ) ( C _ { l m } \cos m \phi + S _ { l m } \sin m \phi ) \right] .
$$

Here, $M _ { E }$ istheNewtonian mass of the Earth, $R _ { E }$ somesuitablychosenEarth’sradiusand $( R , \theta , \phi )$ are the usual polar coordinates of $\mathbf { X }$ .Expression 2.7 assumes that the origin of the GCRScoincides with the Earth's center of mass,so that the mass dipole moments (the $l = 1$ termsin the spherical harmonics expansion) vanish.

In the gravitational $N$ -body problem the BCRS acceleration $\mathbf { a } _ { A }$ of body $A$ is determined by the external gravitational potential

$$
U _ { \mathrm { e x t } } ( t , { \bf x } ) = \sum _ { B \ne A } U _ { B } ( t , { \bf x } ) .
$$

If the gravitational field of body $A$ can be neglected or if $A$ is spherically symmetric (a mass monopole),then

$$
\mathbf { a } _ { A } = \nabla U _ { \mathrm { e x t } } .
$$

For a system of mass monopoles we then have

$$
\mathbf { a } _ { A } = - \sum _ { B \neq A } { \frac { G M _ { B } } { r _ { A B } ^ { 2 } } } \mathbf { n } _ { A B }
$$

where $r _ { A B } \equiv | \mathbf { x } _ { A } ( t ) - \mathbf { x } _ { B } ( t ) |$ and ${ \bf n } _ { A B } = [ { \bf x } _ { A } ( t ) - { \bf x } _ { B } ( t ) ] / r _ { A B }$

Because of the weak equivalence principle (all uncharged test bodies in some external gravitational field fall atthe same rate) in the GCRS,the external gravitational potential $\boldsymbol { U } _ { \mathrm { e x t } }$ differs from the barycentric $U _ { \mathrm { e x t } }$ ：

$$
\mathcal { U } _ { \mathrm { e x t } } = \mathcal { U } _ { \mathrm { t i d a l } } + \mathcal { U } _ { \mathrm { i n e r } } .
$$

Here the Newtonian tidal potential $\mathcal { U } _ { \mathrm { t i d a l } }$ is given by

$$
\mathcal { U } _ { \mathrm { t i d a l } } ( \mathbf { X } ) = U _ { \mathrm { e x t } } ( \mathbf { x } _ { E } + \mathbf { X } ) - U _ { \mathrm { e x t } } ( \mathbf { x } _ { E } ) - \mathbf { X } \cdot \nabla U _ { \mathrm { e x t } } ( \mathbf { x } _ { E } ) .
$$

The inertial potential $\boldsymbol { U } _ { \mathrm { i n e r } }$ results from the coupling of the Earth's higher mass multipole moments to the external potential and vanishes fora purely spherical Earth.Mathematically it is given by

$$
\mathcal { U } _ { \mathrm { i n e r } } = ( \nabla U _ { \mathrm { e x t } } - \mathbf { a } _ { E } ) \cdot \mathbf { X } .
$$

# 2.3Special Relativity and the Metric Tensor

Specialrelativity theory(SRT) is basedupon certain principles.The principleofthe constancy ofthe velocityof light says that thevelocity of light in vacuumis independent of themotion of the source and of frequency,intensity and polarization (note that this has nothing to do with the motion of the observer relative to some“medium”in which electromagnetic waves propagate).

No signal can propagate in the vacuum faster than light; massless particles move with the speed of light $c$ ；massive particles always have a speed less than $c$

If the unit of length isdefined (asin the old days)by some meter stick or as the 1650763,73 multiple of the wavelength of the orange line( $( 5 d _ { 5 }  2 p _ { 1 0 } )$ of $^ { 8 6 } \mathrm { K r }$ thenthe numerical value for $c$ can be measured. It then turns out that it does not depend upon the speed of the observer and the direction in space (the result of the famous Michelson and Morley experiment).As is well known,this result was historically the starting point for the developmentof the SRT.Taking this resultfor granted during the 17th conference on measures and weights in 1983,a new definition of the meter was given:

Themeteris the lengthof thepath traveledby light invacuumduringatimeintervalof 1/299 792 458 of a second.

This new definition of the meter has important consequences:i) the numerical value for $c$ cannolonger be measured and ii) theMichelson-Morley(and related) experiments have to beinterpreted ina different manner(e.g.,the length of ameter stick in some inertial frame does not depend upon its orientation in space).

We now come to the next important principle ofSRT,Einstein's relativity principle:with respect to all (non-gravitational) laws of physics two inertial frames $\Sigma _ { r } [ x ^ { \mu } = ( c t , \mathbf { x } ) ]$ and $\Sigma _ { m } [ X ^ { \alpha } = \left( c T , \mathbf { X } \right) ]$ are completely indistinguishable.This implies that bymeans of physical experiments itis impossible to tell in which inertial system one is located.

These principles imply thatin each inertial frame with Cartesian coordinates $( t , \mathbf { x } )$ the electromagneticwave equation takes the form

$$
\left( - \frac { 1 } { c ^ { 2 } } \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } + \Delta \right) u = 0
$$

if $u$ is the wave amplitude and $c$ isthesame for each inertial frame.Especially for the propagation of a spherical wave originating from the origin of an inertial frame we can write $( \Delta \mathbf { x } ) ^ { 2 } = c ^ { 2 } ( \Delta t ) ^ { 2 }$ Because of this we can introduce a spacetime metric $g _ { \mu \nu }$ with

$$
d s ^ { 2 } = g _ { \mu \nu } d x ^ { \mu } d x ^ { \nu }
$$

(according to Einstein's summation convention over equal indices a summation is automatically caried out) such thatin each inertial Cartesian(or pseudo-Cartesian) coordinate system $x ^ { \mu } = ( c t , x , y , z )$ (note that we are now including a factor of $c$ in the definition of $x ^ { 0 } = c t$ ; then all four coordinates have the same dimension of a length)

$$
g _ { \mu \nu } = \eta _ { \mu \nu } \equiv { \mathrm { d i a g } } ( - 1 , + 1 , + 1 , + 1 )
$$

or, equivalently,

$$
g _ { 0 0 } = - 1 , g _ { 0 i } = 0 , g _ { i j } = \delta _ { i j } .
$$

Equation 2.15 together with 2.16 gives

$$
d s ^ { 2 } = - c ^ { 2 } d t ^ { 2 } + d { \bf x } ^ { 2 } .
$$

Hence,we have introduced a spacetime metric that has the first important property: light rays are geodesic curves with $d s ^ { 2 } = 0$ .In the absence of gravity theyare straight lines with

$$
d s ^ { 2 } = 0 = - c ^ { 2 } d t ^ { 2 } + d { \bf x } ^ { 2 } .
$$

InSRTthe metric tensor in every inertial system is givenbyEq.2.16.This invariance determines the relation between the corresponding coordinates.If the origin of an inertial system $\Sigma _ { m }$ with coordinates $( c T , \mathbf { X } )$ moves with constant velocity $\mathbf { v }$ with respect to the inertial system $\Sigma _ { r }$ with coordinates $( c t , \mathbf { x } )$ ,then for the case of parallel spatial axes the Lorentz transformation reads:

$$
T = \Gamma \left( t - { \frac { \mathbf { v } \cdot \mathbf { x } } { c ^ { 2 } } } \right) , \qquad \mathbf { X } = \mathbf { x } - \Gamma \mathbf { v } t + { \frac { ( \Gamma - 1 ) } { v ^ { 2 } } } ( \mathbf { v } \cdot \mathbf { x } ) \mathbf { v } \ ,
$$

where

$$
\Gamma \equiv \left( 1 - \frac { \mathbf { v } \cdot \mathbf { v } } { c ^ { 2 } } \right) ^ { - 1 / 2 } .
$$

Note,that even in the absence of gravitational fieldsand the acceleration of the geocenter because of Special Relativity,the BCRS and the GCRS coordinateswould be related by aLorentz transformation,a 4-dimensional spacetime transformation that generalizes the Galilean transformation of Eq. 2.1.

Propertime $\tau$ of an observer is the time measured by an (ideal) clock moving together with that observer.If insome inertial systemaclock isat rest( $d \mathbf { x } = 0$ ),thetime indicated by this clock coincides with the coordinate time $t$ .If theclock is moving with respect to the inertialsystem,this willno longerbe the case.Each observable has,mathematically speaking, to be a scalar,because the clock and the observerdo not care what coordinates someone is using to describe the situation.In the general case,proper time, $\tau$ ,asindicatedby someclock is directly related with the spacetime metric according to

$$
d s ^ { 2 } = - c ^ { 2 } d \tau ^ { 2 }
$$

where $d s$ is takenalong the clock's worldline.This constitutes the second important property of the spacetime metric.

Finally,we would like to note that not only the observed proper time,but alsoany other kind of observable,mathematically has to be presented by some coordinate-independent, scalar quantity.We will come back to this point below.

# 2.4 Einstein's Theoryof Gravity

The equivalence principle presents one of the cornerstones of Einstein's theory of gravity. Einstein's equivalence principle says(Weinberg1972,Section3.1) thatat every spacetime pointinanarbitrary gravitational field it is possble to choose a“locally inertial coordinate system”such that,within asufficient small spacetime region of the point inquestion, the laws of nature take the same form as in inertial reference frames of Special Relativity.

This form of the equivalence principle has the consequence that gravity can be described bya metric theory(Will1993),i.e.,byatleasta $g _ { \mu \nu }$ -fieldandpossiblyby“other gravitational fields.”At each point in spacetime there exists a bundle of local freely fallingsystems (Einstein elevators) in which the spacetime metric $g _ { \mu \nu }$ reduces to the flat spacetime metric $\eta _ { \mu \nu }$ .Theworld lines of test bodieswith vanishing own gravitational fieldsare geodesicsof $g _ { \mu \nu }$ .This follows from the fact that these world lines are straight lines in the local freely falling system,i..,geodesics with respect to the flat spacetime metric.Hence,they must be geodesics with respect to the spacetime metric $g _ { \mu \nu }$ .This is the third important property of the metric.

Einstein's theory is the simplest of all metric theoriesof gravity.In Einstein's theory there are no other gravitational fields,but only one spacetime metric that also describes the gravitational interaction and satisfiesEinstein’s field equations

$$
E _ { \mu \nu } ( g , \partial g , \partial ^ { 2 } g ) = \kappa T _ { \mu \nu } .
$$

The left-hand side ofEq.2.22,the Einstein tensor,contains $g _ { \mu \nu }$ and its first and second partial derivatives with respect to the spacetime coordinates.On the right-hand side the energymomentum tensor, $T _ { \mu \nu }$ ,describes the field-generating sources;it generalizes the density $\rho$ of thePoisson equation (Eq.2.4).Inrelativity,energy,density,pressure,and stressesallact as sources of the gravitational field.The energy-momentum tensorcontains theNewtonian matter density, $\rho$ ,inits time-time component

$$
T _ { 0 0 } = \rho c ^ { 2 } + \ldots .
$$

The corresponding field equation to lowest order in $1 / c$ reads

$$
\Delta g _ { 0 0 } = - \kappa ~ T _ { 0 0 } = - \kappa ~ \rho c ^ { 2 } .
$$

If we write

$$
g _ { 0 0 } = - 1 + \frac { 2 U } { c ^ { 2 } } + \mathcal { O } ( c ^ { - 3 } )
$$

the potential $U$ satisfies the Poisson equation (2.4) and the coupling constant $\kappa = 8 \pi G / c ^ { 4 }$ . In this way we see how gravity enters the spacetime metric:in our coordinate system the Newtonian potential iscontained in the $1 / c ^ { 2 }$ term of $g _ { 0 0 }$

Einstein’s equations forma complicated set of ten partial differential equations of second order.Because both sides of the Einstein field equations have zero divergence (due to the conservation of energy and momentum), these ten equations are not independent,only six of them are independent (because of four additional relations).Hence,the equations determine only six out of ten degrees of freedom of the metric tensor $g _ { \mu \nu }$ .Fourdegreesof freedom for the metric tensor remain,expressing the freedom in the choice of the four spacetime coordinates.Ofcourse the field equations cannot tell what coordinates should be used; instead the coordinates can be fixed by four (more or less)arbitrary conditions for the metric tensor. Thisisthe coordinate or gauge freedom of the theory.This gauge freedom is one of the mostimportant differences to the classicalNewtonian theory of gravity.Physically preferred coordinates usually do not exist and observables have to be constructed as scalar quantities.

However,the situation is simpler for isolated systems with anasymptotically flat spacetime.E.g.,the solar systemmightbe idealizedin this manner:we forgetabout distant masses (distant depends upon the problem;for pulsar timing now the masses of our galaxy have to betaken into account)and think of the solar system as being isolated.Then,far from the solar system the gravitational fields will become weaker,with increasing distance spacetime asymptotically will approach the flat spacetime from SRT in thisidealized picture.In the asymptotic region preferred (inertial and e.g., Cartesian) coordinates exist such that there $g _ { \mu \nu }  \eta _ { \mu \nu } .$ If,however,we get closer to the gravitatingmasses,preferred coordinates cease to exist;i.e.,many different coordinates have equal rights.

One might deal with that gauge problem in different ways.One way to avoid confusion is to define certain relevant reference systems,such as the BCRS and the GCRS,by completely specifying their metric tensors as was done by the IAU 2Ooo Resolution B1.3 (IAU 2001; URL[2]).Note that even for that case the observables have to be constructed as coordinateindependent quantities.

# 2.5 The Problem of Observables

Usually coordinatesin Einstein's theory of gravity have no direct physical meaning. To relate the theory with measured quantities (observables)one has to proceed as follows.First onechooses a coordinate system (reference system） that covers the spacetime region of interest.Allrelevant elements of the system such as extended bodies,light rays,physical fields,etc.,have to be described in this coordinate picture.The coordinate dynamics of thesystem follows from fundamental lawsofphysics suchasEinstein's field equations. In such a coordinatepicture light raysand observers are described by means of curves or world lines.The astronomical observables have to be constructed as coordinate-independent quantities.Usually the coordinate picture contains a lot of parameters such as initial positions ofastronomical bodies,their masses,etc.,that canbe fitted to observations by means of leastsquares methods.

# 2.5.1 The Ranging Observable

Letus consider a typical astronomical measurement in the solar system: lunar laser ranging (LLR).Here laser pulses are emitted from LLR stations on the Earth to retro-reflectors on thelunar surface.Typically asingle photonper several pulses finds itsway back into the receiving telescope of the station and one measures the total travel time of a pulse from the stationto theMoon and back.This situationis depicted inFig.2.1.Inthe right part of the figure we see the world line of the clock with the two events $E$ :emission of the pulse and $R$ ： reception of the pulse.The observed time interval between $E$ and $R$ is given by

$$
\Delta \tau = \int _ { E } ^ { R } d \tau
$$

where

$$
d \tau ^ { 2 } = - { \frac { 1 } { c ^ { 2 } } } d s ^ { 2 } .
$$

In practice this indicated time interval $\Delta \tau$ can be related with a corresponding interval of some other timescale.The same sort of observable is used in SLR and radio ranging.

# 2.5.2 The Spectroscopic Observable

We now consider the following problem:one observer emits some monochromatic electromagnetic wave of frequency $f _ { E }$ .Another observer receives this signal and measures the frequency $f _ { R }$ and we ask about the relation between the two frequencies.If we concentrate upon one single light ray propagating from the emitter to the receiver,the situation is shown in Fig.2.2.Here $\gamma _ { E }$ is the world line of the emitter, $\gamma _ { R }$ that of the receiver, $\gamma _ { L }$ that of the light ray.We consider tangent vectors to these three world lines.A tangent vector $u ^ { \mu }$ to the world line of the emitter or observer iscalled 4-velocity and given by $u ^ { \mu } = d x ^ { \mu } / d \tau$ , if $\tau$ indicates proper time along the corresponding world line.The 4-velocity is,obviously, normalized according to

![](images/7a0351313bb74ae8863d5e67d150f711e07b86fa3551350ae23cf9f1fa6342da.jpg)  
Figure 2.1 Left:The ranging observable is a propagation time interval between emission and reception of some electromagnetic pulse.In Lunar LaserRangingitisa laserpulse thattravelsfrom someLLR station on the Earth to some retro-reflector on the lunar surface and back to the ground station. Right:the observableis the proper time interval that has elapsed between the instant of emission and the instant of reception of an electromagnetic pulse.

![](images/b5cec8ebe8c3349897e40f64c6238a3d37e8077a9f7d898770d82183cdba9a1b.jpg)  
Figure 2.2 The spectroscopic observable is the frequency ratio $f _ { R } / f _ { E }$ .Some observer (emitter) emits some electromagnetic signal offrequency $f _ { E }$ .This signal is observed by another observer (receiver) who measures the frequency $f _ { R }$ (see text).

$$
g _ { \mu \nu } u ^ { \mu } u ^ { \nu } = - c ^ { 2 } .
$$

A tangent vector toa light ray will be denoted by $k ^ { \mu }$ .If $\lambda$ is asuitable curve parameter $k ^ { \mu } = d x ^ { \mu } / d \lambda$ .Because of the first metric property

$$
g _ { \mu \nu } k ^ { \mu } k ^ { \nu } = 0
$$

and,therefore,light raysare called null geodesics (geodesics of zero length).Let $u _ { E } ^ { \mu }$ be the 4-velocity of the emitter at the point of emission,and $u _ { R } ^ { \mu }$ be that of the receiver at the point of reception. Let $k ^ { \mu }$ be the tangent vector onto $\gamma _ { L }$ ,thenthe frequency ratio is given by

$$
{ \frac { f _ { R } } { f _ { E } } } = { \frac { ( g _ { \mu \nu } k ^ { \mu } u ^ { \nu } ) _ { R } } { ( g _ { \mu \nu } k ^ { \mu } u ^ { \nu } ) _ { E } } } .
$$

If in the absence of gravitational fields we consider the receiver atrest at the point of reception and the emitter moving with coordinate velocity $\mathbf { v }$ at the point of emission, then

$$
f _ { R } = f _ { E } { \frac { \sqrt { 1 - \beta ^ { 2 } } } { 1 - \beta \cdot \mathbf { n } } }
$$

where $\mathbf { n }$ is the direction of light propagation,so that $k ^ { \mu } \propto ( 1 , { \bf n } )$ .This is the well-known formula for the Doppler effect in Special Relativity.

# 2.5.3Astrometric Observables

In astrometry one principle observable is the observed angle between two incident light rays. This situation is depicted in Fig.2.3.Here $\gamma _ { \mathrm { o b s } }$ is the world line of the observer, $\gamma _ { * }$ and $\gamma _ { * } ^ { \prime }$ are two light rays from two different astronomical sources that are simultaneously observed by the observer in some event $o$ .Let $u ^ { \mu }$ be the4-velocity of the observer in $o$ ， $k ^ { \mu }$ and $k ^ { \prime \mu }$ be the wave vectors of the two incident light rays.Then

$$
P _ { \nu } ^ { \mu } \equiv \delta _ { \nu } ^ { \mu } + \frac { 1 } { c ^ { 2 } } u ^ { \mu } u _ { \nu }
$$

is a projection tensor that projects vectors into their components perpendicular to $u ^ { \mu }$ ,i.e.,

$$
P _ { \nu } ^ { \mu } u ^ { \nu } = u ^ { \mu } + { \frac { 1 } { c ^ { 2 } } } u ^ { \mu } u _ { \nu } u ^ { \nu } = 0
$$

in virtue of the normalization condition Eq.2.27.In a certain sense $u ^ { \mu }$ points into the timedirection of the observer and the projection operator points into the space “experienced”by the observer. Now $k ^ { \mu }$ isa vector obeyingEq.2.28,but

$$
\bar { k } ^ { \mu } = P _ { \nu } ^ { \mu } k ^ { \nu }
$$

is a vectorofnon-vanishing length.The observedangle $\varphi$ between two incidentlight rays $\gamma _ { * }$ and $\gamma _ { * } ^ { \prime }$ is generally given by

$$
\cos \varphi = \frac { g _ { \mu \nu } \bar { k } ^ { \mu } \bar { k } ^ { \prime \nu } } { \vert \bar { k } ^ { \mu } \vert \vert \bar { k } ^ { \prime \mu } \vert }
$$

![](images/c4b257e0d348ab40c57b0e4e1ea4e315a5cc135755e014628aa130e5599a84ed.jpg)  
Figure2.3 The astrometric observable: the observed angle $\varphi$ between two incident light rays $\gamma _ { * }$ and $\gamma _ { * } ^ { \prime }$ as seen by an observer moving along the world line $\gamma _ { \mathrm { o b s } }$

where $\mid A ^ { \mu } \mid = ( g _ { \mu \nu } A ^ { \mu } A ^ { \nu } ) ^ { \frac { 1 } { 2 } } .$ In theabsenceofgravityfieldsfromthis weget

$$
\cos \varphi = \frac { \mathbf { n } \cdot \mathbf { n } ^ { \prime } - 1 + \Gamma ^ { 2 } ( 1 - { \boldsymbol { \beta } } \cdot \mathbf { n } ) ( 1 - { \boldsymbol { \beta } } \cdot \mathbf { n } ^ { \prime } ) } { \Gamma ^ { 2 } ( 1 - { \boldsymbol { \beta } } \cdot \mathbf { n } ) ( 1 - { \boldsymbol { \beta } } \cdot \mathbf { n } ^ { \prime } ) }
$$

where $\beta = { \bf v } / c$ .This is the aberration formula of Special Relativity.A Taylor expansion in terms of $c ^ { - 1 }$ yields

$$
\begin{array} { c } { \cos \varphi = \mathbf { n } \cdot \mathbf { n } ^ { \prime } + ( \mathbf { n } \cdot \mathbf { n } ^ { \prime } - 1 ) \left[ ( \mathbf { n } + \mathbf { n } ^ { \prime } ) \cdot { \boldsymbol { \beta } } + ( \mathbf { n } \cdot { \boldsymbol { \beta } } ) ^ { 2 } \right. } \\ { \left. + ( \mathbf { n } ^ { \prime } \cdot { \boldsymbol { \beta } } ) ^ { 2 } + ( \mathbf { n } \cdot { \boldsymbol { \beta } } ) ( \mathbf { n } ^ { \prime } \cdot { \boldsymbol { \beta } } ) - { \boldsymbol { \beta } } ^ { 2 } \right] + { \mathcal { O } } ( c ^ { - 3 } ) } \end{array}
$$

generalizing Eq.2.3.

In future high-precision astrometric missions different observables might play arole, e.g.,the observed angles between incident light rays and certain reference directions in aspacecraft.In that case these reference directions have to be introduced explicitly into the theory.If one of such reference directionsisrepresented by a reference vector $e ^ { \mu }$ ,the corresponding directional cosine can be obtained from

$$
\cos \theta = \frac { g _ { \mu \nu } \bar { k } ^ { \mu } e ^ { \nu } } { \vert \bar { k } ^ { \mu } \vert \ \vert e ^ { \nu } \vert } .
$$

# 2.6The Post-Newtonian Framework1

The full Einstein equations form a complicated set of non-linear equations.Many exact solutions of Einstein's equations are in fact known,but most of them apply only to the vacuum case for highly symmetric situations.Apart from the well-known Schwarzschild solution (the spherically symmetric vacuum solution) most known exact solutions have little or nothing todo with reality.Forthat reason forapplications in the solar system the so-called post-Newtonian approximation to Einstein's theory is used.The idea of the post-Newtonian theoryis to employ the fact that in the solar systemvelocities of astrophysical bodies are small and gravitational fieldsareweak.The post-Newtonian theory isa slow motion,weak fieldapproximation.Thepost-NewtonianapproximationtoEinstein'stheoryisdetermined with respect to equations of motion. One starts with Newtonian equations of motion for the massive bodies in our solar system and approximates terms in Einstein's theory such that next higher order terms in $1 / c$ are considered explicitly.

# 2.6.1 Coordinate Timescales and Proper Time

Wehave already made it clear that in Einstein's theory of gravity one has first to choosea coordinate system or reference systemto create a coordinate picture of the system of interest. For the construction of a barycentric ephemeris the Barycentric Celestial Reference System (BCRS) with coordinate $x ^ { \mu } = \left( c t , \mathbf { x } \right)$ is a necessary starting point. One component of such a referencesystemisatimecoordinate that definesatimescale thatattributesavalueof time forany event covered by theunderlyingcoordinate system.Forthe BCRS the timescale is $t = \mathrm { T C B }$ (Barycentric Coordinate Time).Since the BCRS covers at least the solar system, any event in the solar system is associated with a TCB value.Another basic reference system of importance is the GCRS (Geocentric Celestial Reference System) whose time coordinate is TCG(Geocentric Coordinate Time).Although the GCRS is physically adequate for the physical phenomenaina vicinity of the Earth (say,within the geostationary orbit),the GCRSalso covers the whole solar system.Therefore,any event in the solar system can be alternatively labelled by TCG and the spatial coordinates of the GCRS.Fromthese two basic timescales,TCBand TCG,additional oneshave been introduced for practical reasons:TDB, TTand TAI; these will be discussed below.

The relation between areference system and the real worldis established via observational data.For theproblem of timescales the readings of certain atomic clocks,defining TAI (International AtomicTime),are employed.Mathematically,areferencesystemisdefinedby the form of the corresponding metric tensor. The readings of an idealized atomic clock can be derived fromEq.2.21by meansof the metric tensor.Hence,whereas‘proper times'refer to theindication of certain individual clocks,coordinate times represent mathematical models andrefer toany event coveredby thereference system.Theypresent anecessary basis for the coordinate picture of an astronomical system.

Moreover, coordinate times present the crucial tool for the synchronization of clocks at different locations.Note,that the concept of simultaneity is an indispensable part of any clock comparison algorithm.The coordinate simultaneity is the only logical possbility of saving the concept of simultaneity in General Relativity (Klioner 1992;Wolf and Petit 1995): two eventsare called simultaneous if and only if the corresponding coordinate times have the same value for both of them.

# 2.6.2The Barycentric Celestial Reference System

IAU200O Resolution B1.3 (IAU 2OO1;URL[2]) concerns the definition of Barycentric Celestial Reference System (BCRS) and the Geocentric Celestial Reference System(GCRS). The BCRS is defined with coordinates $( c t , x ^ { i } ) = x ^ { \mu }$ where $t = \mathrm { T C B }$ (Barycentric Coordinate Time).The BCRS is a particular version of the barycentric reference system of the solar system.The Resolution recommends to write the metric tensor of the BCRS in the form

$$
\begin{array} { l } { { g _ { 0 0 } { } = { } - 1 + \displaystyle \frac { 2 w } { c ^ { 2 } } - \displaystyle \frac { 2 w ^ { 2 } } { c ^ { 4 } } + \mathcal { O } ( c ^ { - 5 } ) } } \\ { { \displaystyle g _ { 0 i } { } = - \displaystyle \frac { 4 } { c ^ { 3 } } w ^ { i } + \mathcal { O } ( c ^ { - 5 } ) } } \\ { { \displaystyle g _ { i j } { } = \delta _ { i j } \left( 1 + \displaystyle \frac { 2 } { c ^ { 2 } } w \right) + \mathcal { O } ( c ^ { - 4 } ) . } } \end{array}
$$

A comparison reveals that this form of the metric presents an extension of the flat metric fromSRT,Eq.2.16,andof the‘Newtonianlimit'Eq.2.25 for $g _ { 0 0 }$ .Whereasthe‘Newtonian limit'of the metric contains only the Newtonian potential, $U$ ,thenew one containsa scalar potential, $w$ ,andavectorpotential, $w ^ { i }$ .

Actually the equations for $g _ { 0 0 }$ and $g _ { 0 i }$ from Eq.2.38 without the order symbols $\mathcal { O } ( c ^ { - 5 } )$ are always correct and can be simply considered as definitions of $w$ and $w ^ { i }$ in terms of $g _ { 0 0 }$ and $g _ { 0 i }$ To specify the post-Newtonian metric we have added order symbols inEq.2.38.E.g., for $g _ { 0 0 }$ the order symbol indicates that terms of order $c ^ { - 5 }$ will systematically be neglected. With these forms for $g _ { 0 0 }$ and $g _ { 0 i }$ one finds that spatially isotropic coordinates $x ^ { i }$ exist such that $g _ { i j }$ from Eq.2.38with the potential $w$ from $g _ { 0 0 }$ solves Einstein's field equations to the first post-Newtonian order.Note that the form ofEq.2.38 implies that the barycentric spatial coordinates $x ^ { i }$ satisfy the harmonic gauge condition (see e.g.,Brumberg and Kopeikin 1989; Damour,Soffel,and $\mathrm { { X u ~ } } 1 9 9 1$ ).Atthispoint,because of the freedomin the timecoordinate, many different‘time gauge conditions'are stillpossible.IAU 2ooo Resolution B1.3 proceeds byrecommending a specific kind of space and time harmonic gauge (IAU 2oo1;URL[2]). Tremendous work on General Relativity has been done with the harmonic gauge that was found to bea useful and simplifying gauge for many kinds of applications.The harmonic gauge condition (e.g.,Weinberg 1972;Fock 1959)

$$
g ^ { \mu \nu } \Gamma _ { \mu \nu } ^ { \lambda } = 0
$$

where $\Gamma _ { \mu \nu } ^ { \lambda }$ are the Christoffel symbols of the metric tensor,is not restricted to some post-Newtonian approximation,but can be defined in Einstein's theory of gravity without any approximations.With the harmonic gauge condition the post-Newtonian Einstein field equationstakethe form

$$
\begin{array} { r } { \left( - \frac { 1 } { c ^ { 2 } } \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } + \Delta \right) w = - 4 \pi G \sigma + \mathcal { O } ( c ^ { - 4 } ) } \\ { \Delta w ^ { i } = - 4 \pi G \sigma ^ { i } + \mathcal { O } ( c ^ { - 2 } ) . } \end{array}
$$

Here $o$ and $\sigma ^ { i }$ are the gravitational mass and mass current density related to the energymomentum tensor $T ^ { \mu \nu }$ by

$$
\sigma = \frac { 1 } { c ^ { 2 } } \left( T ^ { 0 0 } + T ^ { s s } \right) , \quad \sigma ^ { i } = \frac { 1 } { c } T ^ { 0 i } .
$$

In practice,however,the energy-momentum tensor will usually not appear explicitly.This is because the gravitational potentials $w$ and $w ^ { i }$ from Eqs.2.40-2.41 are completely determined by $\sigma$ and $\sigma ^ { i }$ which can be considered as primary quantities.If we deal with problems where gravitational fields playaroleonlyoutsideofastronomical bodiesand admitauseful convergent expansion in terms of multipole moments (potential coeficients),only corresponding integral characteristics of the bodies like masses,quadrupole moments,etc.,show up explicitly,which are defined in terms of $\sigma$ and $\sigma ^ { i }$ and whose numerical values will be fixed by observations.Because of Eq.2.41, $w ^ { i }$ issometimes called the gravitomagnetic potential, since it results from mass currents (moving or rotating masses) just as the electromagnetic vector potential results from electric currents in Maxwell's theory of electromagnetism.

Equation 2.40 generalizes the Poisson equation (Eq.2.4),and,hence,the scalar potential $w$ presents a relativistic generalization of the Newtonian potential $U$ .Because of problems related with homogeneous solutions and boundary conditions mathematically,it is clear that these differential equations do not fix the harmonic solutions uniquely.Assuming spacetime to be asymptotically flat (no gravitational fields far from the system),i.e.,

$$
\operatorname* { l i m } _ { r \to \infty } g _ { \mu \nu } = \eta _ { \mu \nu }
$$

the solution reads

$$
\begin{array} { l } { { \displaystyle w ( t , { \bf x } ) = G \int d ^ { 3 } x ^ { \prime } \frac { \sigma ( t , { \bf x } ^ { \prime } ) } { | { \bf x } - { \bf x } ^ { \prime } | } + \frac { 1 } { 2 c ^ { 2 } } G \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } \int d ^ { 3 } x ^ { \prime } \sigma ( t , { \bf x } ^ { \prime } ) | { \bf x } - { \bf x } ^ { \prime } | } } \\ { { \displaystyle w ^ { i } ( t , { \bf x } ) = G \int d ^ { 3 } x ^ { \prime } \frac { \sigma ^ { i } ( t , { \bf x } ^ { \prime } ) } { | { \bf x } - { \bf x } ^ { \prime } | } . } } \end{array}
$$

Comparing our form of the metric tensor with other forms that can be found in the literature (e.g.,Will 1993),one might get the erroneous impression that something is missing in Eq.2.38and Eqs.2.44-2.45,which is not the case.If matter is described by some fluid model,then formally $( w , w ^ { i } )$ might be split into the various pieces resulting from kinetic energy,gravitational potential energy,specificinternal energy density,pressure,etc.,and the equivalence of our form of the metric tensor,e.g.,with that given in Will(1993) can be shown (Soffel et al. 2003).

Thepoint,however, is that asplitof $( \sigma , \sigma ^ { i } )$ of our metric potentials $( w , w ^ { i } )$ ,or of the metric tensor itself into various pieces is usually unnecessary.If only gravitational fields outside therelevant bodiesplaya role (as is typically the case in celestial mechanics and astrometry),itisadvantageous to keep such pieces together,since it will be the sum that determines the observables.One might argue $U$ isthe‘Newtonian potential’and the rest can be identified as‘relativistic corrections'.This way of thinking,however,can be very misleading and presents a source of errors.As has been shown in the literature (e.g.,Damour, Soffel,and Xu1991,1993),suitably defined potential coeffcients based upon $w$ (not $U$ )and $w ^ { i }$ canbe introduced that can be determined from satellite data.From a more theoretical point of view the introduction of $( w , w ^ { i } )$ has the advantage that the field equations 2.40-2.41 areformally linear,although the corresponding metric is not (because of the $w ^ { 2 }$ -term).We used theword ‘formally'since $o$ dependsupon $w$ implicitly.Thislinearity impliesthat for anensembleof $N$ -bodies

$$
w \left( t , \mathbf { x } \right) = \sum _ { A = 1 } ^ { N } w _ { A } ( t , \mathbf { x } ) , \qquad w ^ { i } ( t , \mathbf { x } ) = \sum _ { A = 1 } ^ { N } w _ { A } ^ { i } ( t , \mathbf { x } )
$$

where the index $A$ indicates the contribution related with body $A$ where the integrals have to be taken over body $A$ only.This linearity,however,does notimplythat body-body interaction

terms have been neglected.Ifwritten explicitly, $w _ { A }$ will in general contain contributions from bodies $B \neq A$

# 2.6.3 BCRS versus ICRS

BCRS is a dynamical concept. The statement“we use BCRS”in General Relativity is analogousto the statement“weuse barycentric inertial coordinates”in Newtonianphysics. The mathematicallanguage and physical content ofGeneral Relativity make it indispensable tofully fix the metric tensor of the BCRS to make the choice of coordinates unique.On the basis of the metric tensor of the BCRS,one derives the dynamical equations of motion ofcelestial bodiesand light rays,and finally constructsrelativistic models of observable quantities.

ICRS is a kinematical concept.From the physical point of view the idea of the ICRS is the cosmological assumption that distant quasars do not rotate with respect to asymptotically flat reference systems like BCRS (orwith respect to inertial coordinatesin the Newtonian framework).In principle such an assumption could and should be checked by testing if the motion of solar system bodies is compatible with the equations of motion,with no Coriolis and centrifugal forces.Up to now no contradictions have been noticed here.

The BCRS as defined by the IAU 2Ooo Resolution has no specific orientation.IAU 2006 Resolution 2completes the definition of the BCRS by adding that unless otherwise stated, theBCRS is assumed to be oriented according to the ICRS axes (IAU 20O7;URL[2]). One can say that the BCRS providesa way to prolong coordinate lines of the ICRS from distance quasars to any point of the solar system.

# 2.6.4The Geocentric Celestial Reference System

IAU 2O0o Resolution B1.3 continues to define the GCRS which represents aparticular version of thelocal geocentric reference system for the Earth.The coordinates $( T , X ^ { a } )$ of the GCRS have two remarkable properties:

(a) Thegravitational field of external bodies is represented only inthe form of tidal terms, thatare at least quadratic in the spatial coordinatesand coincides with theNewtonian tidal potential in the Newtonian limit.   
(b)The internal gravitational field of the central body coincides with the gravitational field of the corresponding isolated source provided that the tidal field of external masses is neglected.

The fact that these two properties can be satisfied simultaneously is a direct consequence of the so-called Strong EquivalencePrinciple that is satisfied in General Relativity(but not necessarily in alternative theories of gravity).

Spatial coordinates $X ^ { a }$ of the GCRS are kinematically non-rotating with respect to the barycentric ones (see e.g.,Brumberg and Kopeikin 1989；Klioner and Soffel1998).The geocentric coordinates are denoted by $( T , \mathbf { X } )$ ,where $T = \mathrm { T C G }$ .In therelationbetween $x ^ { i }$ and $X ^ { a }$ fromIAU 2Ooo Resolution B1.3 let us replace the unit matrix $\delta _ { a i }$ bya general rotation matrix $R _ { a i }$

$$
X ^ { a } = R _ { a i } \left[ r _ { E } ^ { i } + \frac { 1 } { c ^ { 2 } } \left( \ldots \right) \right] + \mathcal { O } ( c ^ { - 4 } )
$$

where $\mathbf { r } _ { E } = \mathbf { x } - \mathbf { x } _ { E }$ .If the two sets of spatial coordinatesare aligned forall times,i.e., if $R _ { a i } = \delta _ { a i }$ as is the case for the GCRS spatial coordinates, then $X ^ { a }$ is defined to be kinematically non-rotating with respect to the barycentric spatial coordinates $x ^ { i }$ .Themetric tensor of the GCRS in the same formas the barycentric one,but with potentials $W ( T , { \bf X } )$ and $W ^ { a } ( T , { \bf X } )$ ：

$$
\begin{array} { l } { { G _ { 0 0 } { } = { } - 1 + { } \displaystyle \frac { 2 W } { c ^ { 2 } } - \displaystyle \frac { 2 W ^ { 2 } } { c ^ { 4 } } + \mathcal { O } ( c ^ { - 5 } ) } } \\ { { { } } } \\ { { G _ { 0 a } { } = - { } \displaystyle \frac { 4 } { c ^ { 3 } } W ^ { a } + \mathcal { O } ( c ^ { - 5 } ) } } \\ { { { } } } \\ { { G _ { a b } { } = \delta _ { a b } \left( 1 + { } \displaystyle \frac { 2 } { c ^ { 2 } } W \right) { } + \mathcal { O } ( c ^ { - 4 } ) } } \end{array}
$$

and the geocentric field equations formally look the same as the barycentric ones (Eqs.2.40- 2.41),but with all variables referred to the GCRS.Again one decisive advantage of this form of the GCRS is the formal linearity of the field equations.This linearity admitsaunique split ofthe geocentric metric into apartcoming fromthe Earth itself and aremaining part resulting frominertial and tidalforces.Therefore,the potentials $W$ and $W ^ { a }$ can be split according to

$$
\begin{array} { r } { W ( T , { \mathbf { X } } ) = W _ { E } ( T , { \mathbf { X } } ) + W _ { \mathrm { e x t } } ( T , { \mathbf { X } } ) } \\ { W ^ { a } ( T , { \mathbf { X } } ) = W _ { E } ^ { a } ( T , { \mathbf { X } } ) + W _ { \mathrm { e x t } } ^ { a } ( T , { \mathbf { X } } ) . } \end{array}
$$

The Earth's potentials $w _ { E }$ and $W _ { E } ^ { u }$ are defined in the same way as $w _ { E }$ and $w _ { E } ^ { u }$ ,(i.e.,Eqs.2.44 2.45with integrals taken over the volume of the whole Earth) but with quantities calculated in the GCRS.Outside the Earth the potentials（W, $W ^ { a }$ ）admit a power series expansion in terms of $R \equiv | \mathbf { X } |$ and all negative powers of $R$ are contained in $W _ { E }$ and $W _ { E } ^ { u }$ .For that reason theEarth'spotentials admit multipole expansions that look very similar to the Newtonian ones.

Itisusefutosliteteeas $W _ { \mathrm { e x t } }$ and $W _ { \mathrm { e x t } } ^ { a }$ further.Theycanbe writen in the form

$$
W _ { \mathrm { e x t } } = W _ { \mathrm { t i d a l } } + W _ { \mathrm { i n e r } } , \qquad W _ { \mathrm { e x t } } ^ { a } = W _ { \mathrm { t i d a l } } ^ { a } + W _ { \mathrm { i n e r } } ^ { a }
$$

where the tidal terms are at least quadratic in $X ^ { a }$ and the inertialcontributions $W _ { \mathrm { i n e r } }$ and $W _ { \mathrm { i n e r } } ^ { a }$ are just linear in $X ^ { a }$ .Explicitly,

$$
\begin{array} { l } { { W _ { \mathrm { i n e r } } = Q _ { a } ~ X ^ { a } } } \\ { { \displaystyle W _ { \mathrm { i n e r } } ^ { a } = - \frac { 1 } { 4 } ~ c ^ { 2 } \epsilon _ { a b c } \Omega _ { \mathrm { i n e r } } ^ { b } X ^ { c } . } } \end{array}
$$

Mathematically the $Q _ { a }$ termis related with the 4-acceleration of the geocenterin the external gravitational field,aquantity that vanishes forapurely spherical and non-rotating Earth (for a mass monopole,more precisely) that moves along a geodesic in the external gravitational field. The $Q _ { a }$ term therefore results from the coupling of higher order multipole moments of theEarth to the external tidal gravitational fields (to the external curvature tensorof spacetime inmathematical language).Further detailson the definition of $Q _ { a }$ and its properties can be found in Soffel etal.(2Oo3).Here we note that for the GCRS $| Q _ { a } | < 4 \times 1 0 ^ { - 1 1 } \mathrm { m } / \mathrm { s } ^ { - 2 }$ .

The term $W _ { \mathrm { i n e r } } ^ { a }$ describes arelativisticCoriolis force duetotherotationof the GCRS with respect to a dynamically non-rotating geocentric reference system.Such a rotation has several components,the dominant of which is called geodesic precession

$$
{ \pmb \Omega } _ { \mathrm { i n e r } } \simeq { \pmb \Omega } _ { \mathrm { G P } }
$$

with

$$
\Omega _ { \mathrm { G P } } = - \frac { 3 } { 2 c ^ { 2 } } \mathbf { v } _ { E } \times \nabla w _ { \mathrm { e x t } } ( \mathbf { x } _ { E } )
$$

where

$$
w _ { \mathrm { e x t } } ( t , { \bf x } ) = \sum _ { A \ne E } w _ { A } ( t , { \bf x } ) .
$$

The orderof magnitude is given by $| \Omega _ { \mathrm { G P } } | { \sim } 3 \times 1 0 ^ { - 1 5 } \mathrm { s } ^ { - 1 } \sim 2 ^ { \prime \prime }$ /century.

The definition of the GCRS implies that the spatial GCRS coordinates $\mathbf { X }$ are kinematically non-rotating with respect to the BCRS ones, $\mathbf { X }$ (as indicated by the $\delta _ { a i }$ -term in ResolutionB1.3).Because of geodesic precession,locally inertial coordinates precess with respect to the GCRS by an amount of $| \pmb { \Omega } _ { \mathrm { i n e r } } | = 1 . ^ { \prime \prime } 9 1 9 8$ /century (Brumberg,Bretagnon,and Francou 1992).Let us forget about the mass of the Earth and imagine a torque free gyroscope at the geocenter,moving along the actual trajectory of the geocenter. It will precess by this amount in our GCRS.Since the GCRS does not present a locally inertial reference system, Coriolis forces caused by geodesic precession-nutation appear in every GCRS dynamical equation of motion,e.g.,of Earth's satelites.Asrecommended by the IERS (2oo4) these additional forces should be taken into account.Moreover,geodesic precession-nutation has to be considered in the precession-nutation model formulated in the GCRS.As long as observations of Earth's orientation parametersare referred to the GCRS they will contain geodesic precession-nutation automatically.Because of the eccentricity of the Earth orbit the leading termin $\Omega _ { \mathrm { { i n e r } } }$ has an annual and asemi-annual part that leads to geodesic nutation in longitude with

$$
\Delta \psi _ { \mathrm { G P } } = 0 . 1 5 3 \sin l ^ { \prime } + 0 . 0 0 2 \sin 2 l ^ { \prime }
$$

where the amplitudes are in mas and $l ^ { \prime }$ is the mean anomaly of the Earth-Moon barycenter (Fukushima 1991; Brumberg etal.1992; Bois and Vokrouhlicky 1995).

$W _ { \mathrm { t i d a l } }$ is a generalization of the Newtonian tidal potential ${ \mathcal { U } } _ { \mathrm { t i d a l } }$ of Eq. 2.12. Full post-Newtonian expressions for $W _ { \mathrm { f i d a l } }$ and $W _ { \mathrm { t i d a l } } ^ { a }$ can be found inDamour,Soffel,and Xu (1992). There $W _ { \mathrm { e x t } }$ is denoted by $\overline { W }$ and a tidal expansion in powers of local spatial coordinates by means of suitably defined tidal momentsis given inEq.4.15of Damour,Soffel,and Xu (1992).Expressions for $W _ { \mathrm { f i d a l } }$ and $W _ { \mathrm { t i d a l } } ^ { a }$ in closed form are given in Klioner and Voinov (1993) (see also Klioner and Soffel 2000).

Finally,the local gravitational potentials $W _ { E }$ and $W _ { E } ^ { a }$ of the Earth are related to the barycentric gravitational potentials $w _ { E }$ and $w _ { E } ^ { i }$ by $\delta _ { i } ^ { a } = \delta _ { a } ^ { i } = \delta _ { a i }$ ）

$$
\begin{array} { l } { { w _ { E } ( t , { \bf { x } } ) = W _ { E } ( T , { \bf { X } } ) \left( { 1 + \frac { 2 } { { { c ^ { 2 } } } } { v _ { E } ^ { 2 } } } \right) + \frac { 4 } { { { c ^ { 2 } } } } { { \delta _ { i a } } { v _ { E } ^ { i } } W _ { E } ^ { a } ( T , { \bf { X } } ) + \mathcal { O } ( { c ^ { - 4 } } ) } } } \\ { { { \displaystyle { w _ { E } ^ { i } ( t , { \bf { x } } ) = { \delta _ { a } ^ { i } } W _ { E } ^ { a } ( T , { \bf { X } } ) + v _ { E } ^ { i } } W _ { E } ( T , { \bf { X } } ) + \mathcal { O } ( { c ^ { - 2 } } ) } . } } \end{array}
$$

The relations between the geocentric gravitational potentials $W$ and $W ^ { a }$ ,and the barycentric ones $w$ and $w ^ { i }$ follow from the coordinate transformations between the BCRS and GCRS discussed below.

# 2.6.5 Coordinate Transformations

The metric tensors of the BCRS and GCRS allow one to derive the rules for the transformations between the BCRS coordinates, $x ^ { \mu }$ ,and the GCRSones, $X ^ { \alpha }$ .It is obvious that these transformations can be written in two equivalent forms:i) as $x ^ { \mu } ( T , X ^ { a } )$ orii)as $X ^ { \alpha } ( t , x ^ { i } )$ . Both forms can be found in the literature.It should be pointed out that the transformation from one version to the other is not so trivial,because of the barycentric coordinate position of the geocenter that appears in the first form as a function of Geocentric Coordinate Time (TCG)and as a function of Barycentric Coordinate Time (TCB) in the second one.Here $T = \mathrm { T C G }$ and $X ^ { a }$ are presented as functions of $t = \mathrm { T C B }$ and $x ^ { i }$ .Theexplicit form of this transformation can be found in Soffel etal. (2OO3)and inResolutionB1.3 itself (URL[2]). For the time transformation one finds

$$
T = t - \frac { 1 } { c ^ { 2 } } [ A ( t ) + v _ { E } ^ { i } r _ { E } ^ { i } ] + \mathcal { O } ( c ^ { - 4 } )
$$

where $( \mathbf { r } _ { E } = \mathbf { x } - \mathbf { x } _ { E } )$

$$
\frac { d } { d t } A ( t ) = \frac { 1 } { 2 } v _ { E } ^ { 2 } + w _ { \mathrm { e x t } } ( \mathbf { x _ { E } } ) .
$$

Here $x _ { E } ^ { i }$ and $v _ { E } ^ { i }$ are the barycentric position and velocity vectors of the Earth,and the external potential, $w _ { \mathrm { e x t } }$ ,is given by Eq.2.53.

# 2.6.6 Relativistic Potential Coefficients

Formany problems itis advantageous to present the local gravitational potentials of the Earth as multipole series that usually converge everywhere outside the Earth.To this end one hasto introducea certain setof multipolemomentsorpotential coefficientsfor the Earth. Acertain set of potential coefficients,called Blanchet-Damour (BD) moments (Blanchet and Damour 1989;Damour, Soffel,and $\mathrm { { X u ~ 1 9 9 1 } }$ )defined to first post-Newtonian order has especially attractive features.Moreover,by using such Blanchet-Damour moments we get a very simple formof the multipole expansion of the post-Newtonian potentials.Basically two sets of BD moments occur in the formalism: mass multipole moments and spin multipole moments.Theoretically these moments can be derived from the distribution of mass and mattercurrents inside the body (Blanchetand Damour1989;Damour,Soffel,and Xu 1991), butfor an observer they simply present parameters which can be directly estimated from observations.

In Soffel et al.(2oo3) it is shown that the metric potential $W _ { E } ( T , { \bf X } )$ outside the Earth can be written as

$$
W _ { E } ( T , { \bf X } ) = \frac { G M _ { E } } { R } \left[ 1 + \sum _ { l = 2 } ^ { \infty } \sum _ { m = 0 } ^ { l } \left( \frac { R _ { E } } { R } \right) ^ { l } P _ { l m } ( \cos \theta ) ( C _ { l m } \cos m \phi + S _ { l m } \sin m \phi ) \right] .
$$

Here, $M _ { E }$ isthe mass of the Earth,definedtopost-Newtonianorder, $R _ { E }$ some suitably chosen Earth's radius and ( $C _ { l m }$ , $S _ { l m } )$ arethe post-Newtonian Blanchet-Damour potentialcoeficients of the Earth.The $l = 1$ termis missing in Eq.(2.58)because the origin of the GCRS is assumed to coincide with the Earth's center of mass.To derive this relation certain approximations related with the shape of the Earth have been made that are explained in Soffel etal.(2003), but,nevertheless,itis valid to post-Newtonian accuracy.Note that formally this expression for $W _ { E }$ inEq.2.58 agreeswith that for the Newtonian potential of the Earth in Eq. 2.7, showing the great simplicity of the formalismin virtue of theway of writing themetric tensorand of using the Blanchet-Damour multipole moments.In Soffel etal.(2Oo3) it was also demonstrated that the gravitomagnetic vector potential resulting from the motion of the variousmaterial elements of the Earth in the GCRS can be written inthe form

$$
{ \cal W } _ { E } ^ { a } ( T , { \bf X } ) = - \frac { G } { 2 } \frac { ( { \bf X } \times { \bf S } _ { E } ) ^ { a } } { R ^ { 3 } }
$$

where $\mathbf { S } _ { E }$ is the total angular momentum vector of the Earth,that here is needed only to Newtonian accuracy.Higher order spin moments of the Earth have been neglected in this expression that can be found in many standard textbooks on GRT(Weinberg 1972;Will 1993). $W _ { E } ^ { a }$ is usually related withLense-Thirring effects resulting from the Earth's rotational motion.

# 2.7 Applications

# 2.7.1 Other Versions of the Geocentric Celestial Reference System

The technique developed to construct the GCRS can be directly applied for other purposes if otherbodiesare takenascentral bodiesinstead of theEarth.

If the whole solar system is considered as such a central body and if the gravitational field of other bodies in the Galaxy are taken into account,the technique used in the GCRS allows one to construct areference system forthe whole solar system(a version of the BCRS) with external gravitational fields explicitly taken into account.Aswas discussed above,in thiscase the external gravitational fields due to the Galaxy are tidal fields.One can estimate the magnitude of accelerations and other effects due to these tidal forces and find them to be negligible for the current levelof accuracy.It is,therefore,one more argument for the BCRS in the form discussed above.

AGCRS-like reference system can be constructed not only for the Earth,but for any other body of the solar system.Such areference system for the Moon is used to model the rotational motion of the Moonaswell as to model theLLR data. One can expect that GCRS-like reference systems forMarsand Mercury willbe used soon to study the rotational motionand physics of these planets.Also for other bodies such reference systems will be of importance.For example,the gravitational fields ofall bodies are definedbyEq.2.58 defined in the corresponding reference system.

Finally,consideringan observer as the central body fora GCRS-likereference system one immediately getsareference system which can be directly used for modelling of any sort of observables as seen by the observer or to study the local physical phenomena in the immediate vicinity of that observer (e.g.,atttude of a spacecraft). Usually,one can neglect themassof theobserverand this simplifies the formulae for theGCRS-likemetric tensor since the internal potentials (denoted by $W _ { E }$ and $W _ { E } ^ { a }$ in theGCRS） vanish.On the other side the inertial potentials (Eq.2.5O)may become much larger than for the GCRS.For example,for an observer on the surface of the Earth one has $\vert Q _ { a } \vert \approx 9 . 8 1 \mathrm { m } / \mathrm { s } ^ { 2 } .$ At the origin ofthe GCRS-likereference system of an observer,itscoordinate time coincideswith the proper time of that observer.Moreover,the coordinate basis of the GCRS-like system at itsorigin representsa kinematically non-rotating tetrad.The latter is the standard tool to convert coordinate-dependent quantities into coordinate-independent observables in General Relativity;seeKlioner(2oo4) fora detailed discussion.

Let us also note that the BCRS and GCRS are givenby the IAU Resolutions in the framework of General Relativity.Variants of thesereference systems in the framework of the PPN formalism are discussed in Will(1993); Klioner and Soffel (20o0); Klioner (2004); Kopeikin and Vlasov (2004).

# 2.7.2 Rotating Reference Systems

Another important variant of a GCRS-likereference system isa local reference system rotating with respect to the corresponding celestial (i.e.,non-rotating) reference system. Such a rotating reference system with coordinates $( \overline { { T } } , \overline { { X } } ^ { u } )$ is defined from the GCRS-like (kinematically non-rotating) reference system by the following transformations:

$$
\begin{array} { c } { { \overline { { { T } } } = T } } \\ { { \overline { { { X } } } ^ { b } = P ^ { a b } ( T ) X ^ { b } } } \end{array}
$$

where $P ^ { a b } ( T )$ is anarbitrary time-dependentorthogonal matrix.Matrix $P ^ { a b }$ defines arotation of spatial coordinates ${ \overline { { X } } } ^ { u }$ with respect to the kinematically non-rotating coordinates $X ^ { a }$ .Such rotating reference systemscan be used to separate the dynamics of thecentral body into a rotationandadeformation.Thus,for the Earth therotatingcoordinatesof this kind provide arelativistic model for ITRS/ITRF.The matrix in thiscase represents therotation between GCRSand ITRS and describes precession,nutation,and polar motion.The same sort of coordinates can be used for other planetsand for,e.g.,spacecrafts.Inall cases the matrices $P$ represent arelativistically meaningful way to describe the atitude of the central body with respect to the kinematically non-rotating GCRS-like coordinates.

# 2.7.3The Einstein-lnfeld-Hoffmann Equations of Motion

Inthe gravitationalN-body problem the potential coefficients ofabody $A$ are defined in its corresponding local reference system (analogous to the GCRS for the Earth).For many applications it is sufficient to keep only the mass monopoles of the solar system bodies.If we go into the local system of body $A$ with coordinates $X _ { A } ^ { \alpha } = ( c T _ { A } , \mathbf { X } _ { A } )$ ,

$$
W _ { A } = \frac { G M _ { A } } { R } , W _ { A } ^ { a } = 0
$$

where $R = | \mathbf { X } _ { A } |$ Note that this expression for $W _ { A }$ looks perfectly Newtonian though $M _ { A }$ is defined to post-Newtonian order.

From the transformation rules for the metric potentials of Eq.2.55,and formula2.46,one derives the metric in the barycentric coordinate systemin the form ofEq.2.38with

$$
w = \sum _ { A } \frac { G M _ { A } } { r _ { A } } - \frac { 1 } { c ^ { 2 } } \sum _ { A } \Delta _ { A } ( t , { \bf x } )
$$

with $\mathbf { r } _ { B A } = \mathbf { x } _ { B } - \mathbf { x } _ { A }$ and $\mathbf { a } _ { A } = d \mathbf { v } _ { A } / d t$ ）

$$
\begin{array} { l } { { \displaystyle \Delta _ { A } ( t , { \bf x } ) = \frac { G M _ { A } } { r _ { A } } \left( - \frac { 3 } { 2 } v _ { A } ^ { 2 } + \sum _ { B \ne A } \frac { G M _ { B } } { r _ { B A } } \right) - \frac { 1 } { 2 } G M _ { A } r _ { A , t t } } } \\ { { \displaystyle \qquad = \frac { G M _ { A } } { r _ { A } } \left[ - 2 v _ { A } ^ { 2 } + \sum _ { B \ne A } \frac { G M _ { B } } { r _ { B A } } + \frac { 1 } { 2 } \left( \frac { ( r _ { A } ^ { k } v _ { A } ^ { k } ) ^ { 2 } } { r _ { A } ^ { 2 } } + r _ { A } ^ { k } a _ { A } ^ { k } \right) \right] . } } \end{array}
$$

Furthermore,in our approximation

$$
w ^ { i } ( t , { \bf x } ) = \sum _ { A } \frac { G M _ { A } } { r _ { A } } v _ { A } ^ { i } .
$$

Note the remarkable fact that the post-Newtonian BCRS mass monopole metric with potentials given inEqs.2.62and2.64 hasbeen derived from the $G M _ { A } / R$ potentials in the local system of body $A$ bymeans of the transformation rules of Eq.2.55.

From this metric the well-known Einstein-Infeld-Hoffmann equations of motion can be derived.In Damour,Soffel,and $\mathrm { X u }$ (1991) it is shown that to post-Newtonian order every spherically symmetric body $A$ follows a geodesic in the external metric given by $w _ { \mathrm { e x t } }$ and $w _ { \mathrm { e x t } } ^ { i }$ described by formula2.46where the potentials due to body $A$ are excluded from the sums.These geodesic equations,the Einstein-Infeld-Hoffmann(EIH) equations,finally read:

$$
\begin{array} { l } { { { \displaystyle { \ddot { \bf x } } _ { A } = - \sum _ { B \ne A } \frac { G M _ { B } } { r _ { A B } ^ { 2 } } { \bf n } _ { A B } \Biggl [ 1 + \frac { 1 } { c ^ { 2 } } \left( { \bf v } _ { A } ^ { 2 } + 2 { \bf v } _ { B } ^ { 2 } - 4 { \bf v } _ { A } \cdot { \bf v } _ { B } - \frac { 3 } { 2 } ( { \bf n } _ { A B } \cdot { \bf v } _ { B } ) ^ { 2 } \right) } } \ ~ } \\ { { \displaystyle ~ - 4 \sum _ { C \ne A } \frac { G M _ { C } } { c ^ { 2 } r _ { A C } } - \sum _ { C \ne B } \frac { G M _ { C } } { c ^ { 2 } r _ { B C } } \biggl [ 1 + \frac { 1 } { 2 } \frac { { r } _ { A B } } { { r } _ { B C } } { \bf n } _ { A B } \cdot { \bf n } _ { C B } \biggr ] \Biggr ] } } \\ { { \displaystyle ~ - \frac { 7 } { 2 } \sum _ { B \ne A } \sum _ { C \ne B } { \bf n } _ { B C } \frac { G ^ { 2 } M _ { B } M _ { C } } { c ^ { 2 } r _ { A B } r _ { B C } ^ { 2 } } \ ~ } } \\ { { \displaystyle ~ + \sum _ { B \ne A } ( { \bf v } _ { A } - { \bf v } _ { B } ) \frac { G M _ { B } } { c ^ { 2 } r _ { A B } ^ { 2 } } ( 4 { \bf n } _ { A B } \cdot { \bf v } _ { A } - 3 { \bf n } _ { A B } \cdot { \bf v } _ { B } ) } . } \end{array}
$$

These EIH equations of motion are used to model the motion of our solar system and to form the basis of modern solar system ephemerides.They are also used for high-accuracy calculations ofasteroid orbits.

# 2.7.4 Equations of Motion in the GCRS

The motionof artificial satellites isusuallydescribed in the GCRSwith TCGor terrestrial time TT(see below) as the timescale.In the GCRS the equation of motion of asatellite is given bythe geodesicequation in theGCRS metric,Eq.2.47.The dominant relativistic acceleration resultsfrom the mass of the Earth.For this post-Newtonian Schwarzschild acceleration one considers

$$
W _ { E } ( T , { \bf X } ) = \frac { G M _ { E } } { R } .
$$

Without external contributions to the metric tensor (tidal and inertial terms) the geodesic equation takes the form

$$
{ \frac { d ^ { 2 } X ^ { a } } { d T ^ { 2 } } } = - { \frac { G M _ { E } X ^ { a } } { R ^ { 3 } } } + { \frac { G M _ { E } } { c ^ { 2 } R ^ { 3 } } } \left[ \left( 4 { \frac { G M _ { E } } { R } } - \mathbf { V } ^ { 2 } \right) X ^ { a } + 4 ( \mathbf { X } \cdot \mathbf { V } ) V ^ { a } \right]
$$

where $\mathbf { X }$ and $\mathbf { V }$ are the satellite position and velocity in GCRS coordinates.Other effects that should be taken into account in practical calculations are geodesic andLense-Thirring precessions.The corresponding terms can be easily derived from the second equation in Eqs.2.50 and2.59,respectively.Detailed theoretical discussions of the equations of motion of Earth's satelites in the GCRScanbe found in Damour,Soffel,and Xu (1994);Brumberg (1991); Klioner and Soffel (20oo). Section 10.2of IERS (2004) contains a practical approximation to these equations.

# 2.7.5Astrometry

As indicated above the relativistic description of astrometric measurements proceeds intwo steps: first one formulates a coordinate picture of the astrometric situation including the light source,the observer,andthe light rays that propagate through the cosmos under the influence ofvariousgravitational fields.Ina second step the observables have to be calculated as explained in $\ S \ 2 . 5$ .If the solarsystemisconsidered tobe isolated,one forgetsabout the large-scale structure of the universe which for cosmological questions clearly is not justified. For cosmological problems one might use some metric averaged over a large cosmological volume so that it becomes homogeneous and isotropic like the Friedman-Robertson-Walker metric(e.g.,Weinberg 1972) on large scales.However,the matching of such a cosmological metric to our BCRS metric still presents serious difficultiesand this work is still in progress (Klioner and Soffel 2005).

For an isolated gravitational $N$ -body system,the formulation of relativistic astrometry has evolved to $\mu$ as precision.We will only consider the simplest case here.

As we have seen earlier light rays are null geodesics,i.e.,curves $x ^ { \mu } ( \lambda )$ satisfying the geodesic equation and the condition

$$
g _ { \mu \nu } { \frac { d x ^ { \mu } } { d \lambda } } { \frac { d x ^ { \nu } } { d \lambda } } = 0 .
$$

If the metric tensor $g _ { \mu \nu }$ is fully specified,these equations can be solved for a mathematical description oflight rays in the form ${ \bf x } _ { \gamma } ( t )$ where coordinate time $t$ serves as curve parameter. In the first post-Newtonian approximation one usually writes

$$
\begin{array} { r } { \mathbf { x } _ { \gamma } ( t ) = \mathbf { x } _ { N } + \Delta \mathbf { x } _ { \gamma } \quad } \\ { \mathbf { x } _ { N } = \mathbf { x } _ { 0 } + \pmb { \sigma } c ( t - t _ { 0 } ) . } \end{array}
$$

Here, $\mathbf { x } _ { N }$ represents the unperturbed (Newtonian) trajectory of the light ray.We now consider the gravitational potential $w$ to begenerated by some‘roughly spherical’matter distribution. I.e., outside the matter we consider only the mass monopole $M$ situated at the origin of our coordinates and write $w = G M / r$ ,where $r = | \mathbf { x } |$ .Thento first post-Newtonianorder the light ray equations are solved by

$$
\Delta { \bf x } _ { \gamma } ( t ) = - 2 m \left[ \sigma \ln \left( { \frac { x _ { N } + { \bf x } _ { N } \cdot \sigma } { x _ { 0 } + { \bf x } _ { 0 } \cdot \sigma } } \right) + { \frac { \bf d } { d ^ { 2 } } } [ r _ { N } - r _ { 0 } + c ( t - t _ { 0 } ) ] \right]
$$

where $x _ { N } = | \mathbf { x } _ { N } | , x _ { 0 } = | \mathbf { x } _ { 0 } |$

$$
m \equiv { \frac { G M } { c ^ { 2 } } }
$$

and $\mathbf { d }$ is the vector joining the center of the gravitating body and the point of closest approach of theunperturbed ray (Will 1993),and $d = | \mathbf { d } |$ .The logarithmic termisin the direction of the unperturbed light ray; it describes the so-called gravitational time delay.Finally the last part,proportionally to $\mathbf { d }$ ,describes the gravitational light-deflection.

Let $\mathbf { n }$ be the unit coordinate direction of light propagation at the point of observation: $\mathbf { n } = \dot { \mathbf { x } } _ { \gamma } / | \dot { \mathbf { x } } _ { \gamma } |$ .Then at the position $\mathbf { x _ { \mathrm { o b s } } }$ of observation one has (Klioner 2003):

$$
{ \bf n } = \sigma - 2 m \frac { { \bf d } } { d ^ { 2 } } \left( 1 + \sigma \cdot \frac { { \bf x } _ { \mathrm { { o b s } } } } { | { \bf x } _ { \mathrm { { o b s } } } | } \right) .
$$

These formulae give the main relativistic effect of light-deflection.The gravitational lightdeflection due to the Sun amounts to $1 \% 7 5$ fora grazing ray,and attains4 mas if the angular distance between the source and the Sun is $9 0 ^ { \circ }$ .The deflection due to Jupiter can be as large as 16 mas.Other effects include the influence of the quadrupole gravitational fields of giant planets (up to $2 4 0 \mu$ as)and higher-order Schwarzschild effects (upto about $1 6 \mu$ as). Furthermore,it is important to know that the motionof the deflecting body in the BCRS must also be taken into account,and that the position of the gravitating body should be calculated attheretarded moment $t ^ { * }$ defined as

$$
t ^ { * } = t _ { \mathrm { o b s } } - \frac { 1 } { c } | \mathbf { x } _ { \gamma } ( t _ { \mathrm { o b s } } ) - \mathbf { x } _ { A } ( t ^ { * } ) |
$$

where ${ \bf x } _ { A } ( t )$ is the BCRS position of the gravitating body as a function of time $t$ (Kopeikin and Schäfer 1999).For a more exhaustive discussion of relativistic astrometry the reader is referred to Klioner(2003).

Currently in The Astronomical Almanac,geocentric positions (apparent places) are computed using deflection of light from the mass of the Sun,Jupiter,and Saturn.If the observer is notat the geocenter(e.g.,for topocentric positionswhich may be availablevia The Astronomical AlmanacOnline),light-deflectionduetotheEarthisalso included.

Let usconsidera light ray propagating from point $\mathbf { x } _ { 0 }$ topoint $\mathbf { x } _ { 1 }$ .In the presence of a gravitational field the travel time $t _ { 1 } - t _ { 0 }$ between these two points is slightly larger than the distance $R = | \mathbf { x } _ { 1 } - \mathbf { x } _ { 0 } |$ divided by $c$ .In the spherically symmetric gravitational fieldof amass monopole one has

$$
c \left( t _ { 1 } - t _ { 0 } \right) = R + 2 m \ \ln { \frac { x _ { 1 } + x _ { 0 } + R } { x _ { 1 } + x _ { 0 } - R } } .
$$

This additional retardation in light propagation is called the Shapiro delay and can amount to 240 microseconds for observations of Venus in superior conjunction with the Sun.

# 2.7.6 VLBl Observations

The model of VLBI observations is one of the most complicated relativistic models.This model naturally combines quantities and parameters defined in the BCRS and the GCRS. The positions of observing stations and the corresponding baseline vectors are defined in the GCRS.Also in the GCRS one describes the rotational motion of the Earth.The coordinate transformation between BCRS and GCRS,as wellthe BCRS position of the geocenter,are then used to calculate the positions of observing station in the BCRS.The positions of the quasars are defined in the BCRS.Considering the light propagation between a given quasar and two observing stations,one calculates the difference in propagation time between these two light rays incoordinate time TCB.Then the derived coordinate time difference can be converted inany other coordinate time (e.g.,TT).The details of the derivation of this model are rathercomplicated.A detailed practical summary is given in Section11.1ofIERS (2004).

# 2.8Relativistic Timescales, their Definitions and Units

# 2.8.1Practical Transformations of Timescales

Sofar we have extensively discussed Geocentric Coordinate Time (TCG) and Barycentric Coordinate Time (TCB)as timescalesofthe GCRSand the BCRS,respectively.To sufficient accuracy therelation between these two timescalesis given inIAU 2Ooo Resolution B1.5 (IAU20O1; URL[2]).This Resolution contains a slightly simplified version of the coordinate transformations between TCG and TCB that are given inResolutionB1.3.The transformation between TCGand TCB evaluated atthe geocentercan becalculatedby anumericalintegration of the corresponding equations using a solar system ephemeris.

The relation between proper time $\tau$ of some observer with coordinates $\mathbf { x } _ { \mathrm { o b s } } ( t )$ and $t = \mathrm { T C B }$ may be written in the form (Soffel etal.2003)

$$
\begin{array} { r l r } {  { \frac { d \tau } { d \mathrm { T C B } } = 1 - \frac { 1 } { c ^ { 2 } } ( w _ { 0 } + w _ { L } + \frac { v ^ { 2 } } { 2 } ) } } \\ & { } & { \qquad + \frac { 1 } { c ^ { 4 } } ( - \frac { 1 } { 8 } v ^ { 4 } - \frac { 3 } { 2 } v ^ { 2 } w _ { 0 } + 4 v ^ { i } w ^ { i } + \frac { 1 } { 2 } w _ { 0 } ^ { 2 } + \Delta ) } \end{array}
$$

where $v ^ { i }$ is the BCRS coordinate velocity of the observer,

$$
w _ { 0 } = \sum _ { A } \frac { G M _ { A } } { | \mathbf { x } _ { \mathrm { o b s } } - \mathbf { x } _ { A } | }
$$

$w _ { L }$ containscontributionsfrom higherpotentialcoefficients,and $\Delta \equiv \sum _ { A } \Delta _ { A }$ with $\Delta _ { A }$ being given byEq.2.63.The uncertainty of relations inResolutionB1.5and Eq.2.72is less than $5 \times 1 0 ^ { - 1 8 }$ in rate.

For some clock in the vicinity of the Earth the relation between its proper time $\tau$ and TCG canbe obtained fromEq.2.21and theGCRS metric Eq.2.47.At the indicated level of accuracy the contributions from $W ^ { 2 }$ , $W ^ { a }$ ,and $W _ { \mathrm { i n e r } }$ can be neglected (Soffel et al.2003).

# 2.8.2 Scaled Coordinate Timescales

ResolutionsIAU1991 A4and IAU $2 0 0 0 \ \mathrm { B } 1 . 3$ havedefinedTCBand TCGasthe time coordinatesof theBCRSandGCRS,respectively,andIAUResolutionB3(Note6)has encouragedthe use ofTCB for solar system ephemerides.Fromthe considerations of practical convenience one often uses two additional timescales,TTand TDB.The reasons for and the mathematical detailsof the relativistic scalingof BCRSand GCRS,and in particular their coordinate times,are summarized,e.g.,byKlioner (2Oo8).TT and TDB are conventional linearfunctions of TCG and TCB,respectively.The definition of TTis givenby IAU2000 ResolutionB1.9and IAU1991Resolution A4as

$$
\mathrm { T T } = F _ { G } \mathrm { T C G }
$$

where $F _ { G } = 1 - L _ { G }$ ,and $L _ { G } = 6 . 9 6 9 2 9 0 1 3 4 \times 1 0 ^ { - 1 0 }$ is adefining constant.TDB is defined inIAU 20o6Resolution 3by itsconventional relation to TCB:

$$
\mathrm { T D B } = F _ { B } \ \mathrm { T C B } + \mathrm { T D B } _ { 0 }
$$

where $\boldsymbol { F } _ { B } = 1 - \boldsymbol { L } _ { B }$ ,and $L _ { B } = 1 . 5 5 0 5 1 9 7 6 8 \times 1 0 ^ { - 8 }$ and $\mathrm { T D B } _ { 0 } = - 6 . 5 5 \times 1 0 ^ { - 5 }$ saredefining constants.In Eqs.2.74 and $2 . 7 5 \ \mathrm { T T }$ ,TCG,TCB and TDB should be expressed by the corresponding Julian dates reckoned from $\mathrm { T } _ { 0 } = 2 4 4 3 1 4 4 . 5 0 0 3 7 2$ that stands for the event 1977 January $1 0 0 \mathrm { { h } 0 0 \mathrm { { m } 0 0 \mathrm { { s } } } }$ TAI at the geocenter. Many of the defining constants,including $L _ { B }$ and $L _ { G }$ ,aregiven annually in SectionK(Tables and Data)of The Astronomical Almanac.

The slopes $F _ { G }$ and $F _ { B }$ of both linear functions have the same purpose: both TTand TDB should show no linear drift with respect to proper times of observers situated on the rotating geoid. Since this requirement depends on our model of the solar system (i.e.,on a planetary ephemeris and on a number of astronomical and geodesic constants), it cannot be satisfied exactly.Therefore,some conventional constants have beenchosen in the definitions ofTTand TDB so that the requirement is satisfied approximately,but with an accuracy totally sufficient for practical purposes.Similarly,the constant $\mathrm { T D B _ { 0 } }$ was chosen merely to keep TDB-TT approximately centered on zero.

International Atomic Time(TAI) isaphysical realizationofTTwithashiftof $- 3 2 . 1 8 4$ s forhistorical reasons.Therefore,TAI isarealizationof coordinate time“ $\Gamma \Gamma - 3 2 . 1 8 4 \mathrm { ~ s } ^ { \prime \prime }$ . The difference between TAI and an ideal realization of $ { { } ^ { * } \mathrm { T T } } - 3 2 . 1 8 4 \  { { \mathrm { s } } ^ { \prime \ } }$ is only due to imperfections of the participating clocks and the clock synchronization procedures.

Finally,the timescale $T _ { \mathrm { e p h } }$ has been introduced by Standish (1998)to mean the time coordinate used in Jet Propulsion Laboratory'sDE/LE ephemerides (for more,see Chapter 8 of this publication).Although $T _ { \mathrm { e p h } }$ is defined as a linear function of TCB,with the slope depending on the ephemeris,in practice $T _ { \mathrm { e p h } }$ was defined bya fixed relation to TT(by the formulae of Moyer (1981) or Fairhead and Bretagnon (199O).For practical purposes TDB, asdefined byEq.2.75 for the JPL ephemerisDE405,agrees with $T _ { \mathrm { e p h } }$ . In the near future each new solar system ephemeris will include the TDB-TT transformation at the geocenter,thus becoming4-dimensionalas itisnaturallyrequired by the theoryof relativity(Fienga et al. 2009).

# 2.8.3 Units of Timescales

There has been a long debate of the question of time units.The basic unit is the SI second:

thesecondis the duration of9192631770 periods of the radiationcorrespondingto the transition between thetwo hyperfinelevelsof theground state of thecesiumatom.

This definition contains no indication of any specificlocation, gravitational potential,or state of motion of the observer realizing the SI second.Thus,this definition is merely arecipe for how some observercanrealize the SI second.The SI second is the natural unitfor proper time. Viathe theoretical relation between proper time of some (idealized)clock andthe coordinates ofa reference system,the unit for proper time (the SI second) is naturally induced as a canonical unit forany other timescale,as longas there is a direct relation to proper time and no explicit rescaling of units.

From the metrological point of view,the theoretical relations between proper time and the coordinate times are relations between quantities and are independent of the choice of units.The sameis true for the theoretical relations between different coordinate timescales themselves.Thismeans that basicallyanyunitscan beused to convert these quantities into numerical values.The SI second is the canonical unit for proper time of some observer. If a theoretical formula relating the proper time and a coordinate time is used to compute the values of the corresponding coordinate time starting from the values of proper time inSI seconds,the resulting values of coordinate time will also be expressed in terms of SI seconds.

If one consider the timescales TTand TDB,two standpoints might be taken.One posble standpoint is that using TTand TDB is nothing but arescaling of the TCGorTCB time unit, respectively.However,this standpoint easily leads to confusionsand possible mistakes.For example,in this case one cannot consider TAIand TTas expressed in the seconds of SI.For these reasons it is logical to avoid notations such as“TDB units”(TDB seconds/meters"), “TTunits”(“TT seconds/meters"),and avoid contrasting these terms with“SI units”("SI seconds/meters").Itis straightforward to interpret TTand TDBas beingevolved froma coordinate transformationofTCGand TCB,respectively.In thisway,the SI second is the onlyunit for any timescale.IfTTorTDB are used as basic timescales indynamical equations, then either the conversion parameters $F _ { G }$ and $F _ { B }$ have to be included in the equations of motion explicitly,orTT-compatibleand TDB-compatible values for dimensional quantities (e.g.,mass parameters $\mu = G M$ ofcelestial bodies) have to beconsidered.In general,all quantities intended for use with timescale xxx should be called xxx-compatible (xxx being TT,TDB,TCG or TCB).Moreover,numerical values of all such quantities(called xxxcompatible values) should be considered to be expressed in the usual units of the SI.More details on this subject and formal nomenclature can be found in Klioner(2Oo8)and Klioner et al. (2009).

# REFERENCES

1.The Astronomical Almanac Online: http://asa.usno.navy.mil orhttp://asa.hmnao.com.   
2.IAUResolutions Adopted by the General Assemblies: http://www.iau.org/administration/resolutions/general_assemblies/.   
Bertott,B.,L.Iess,andP.Tortora (2Oo3).A test of general relativity using radio links with theCassin spacecraft.Nature425,374-376.   
Blanchet,L.and T.Damour (1989).Post-Newtonian generation of gravitational waves.Annales de L'InstitutHenri PoincareSectionPhysiqueTheorique50,377-408.   
Bois,E.andD.Vokrouhlicky(1995).Relativistic spin effects in the Earth-Moonsystem.Astronomy and Astrophysics 300,559.   
Brumberg,V.A.(1991).EssentialRelativisticCelestialMechanics.Bristol:A.Hilder.   
Brumberg,V.A.,P.Bretagnon,andG.Francou(1992).Analytical algorithms of relativisticreductior ofastronomical observations.InN.Capitaine (Ed.),LesJournées199l,pp.141-148.Paris: Observatoire de Paris.   
Brumberg,V.A.and S.M.Kopeikin (1989).Relativistic Theoryof Celestial ReferenceFrames.In J.Kovalevsky etal. (Eds.),ReferenceFrames,pp.115.Dordrecht,Holland:Kluwer.   
Damour,T.,M.Soffel,and C.Xu (1991).General-relativistic celestial mechanics.I.Method and definition of reference systems.Physcial ReviewD43(10),3273-3307.   
Damour,T.,M.Sofel,and C.Xu (1992).General-relativistic celestial mechanics.II.Translational equations of motion.Physcial ReviewD 45(4),1017-1044.   
Damour,T.,M. Soffel,and C.Xu (1993).General-relativistic celestial mechanics.II.Rotational equations of motion.Physcial ReviewD47(8),3124-3135.   
Damour,T.,M.Soffel,andC.Xu(1994).General-relativisticcelestial mechanics.IV.Theoryof satellite motion.PhyscialReviewD49(2),618-635.   
Eubanks,T.M.,D.N.Matsakis,J.O.Martin,B.A.Archinal,D.D.McCarthy,S.A.Klioner, S.Shapiro,and I. I Shapiro (1997).Advances in Solar System Tests of Gravity.APS Meeting Abstracts,K11.05.   
Fairhead,L.andP.Bretagnon (199O).Ananalytical formula for the time transformation TB-TT. Astronomy and Astrophysics 229,240-247.   
Fienga,A.,J.Laskar,T.Morley,H.Manche,P.Kuchynka,C.LePoncin-Lafitte,F.Budnik, M.Gastineau,andL.Somenzi (2Oo9).INPOPO8,a4-Dplanetary ephemeris:Fromasteroid and time-scale computations to ESA Mars Express and Venus Expresscontributions.Astronomy and Astrophysics 507,1675-1686.   
Fock,V.A.(1959).TheTheoryof Space,Time andGravitation.Oxford:Pergamon.Translated into English fromTeoriyaprostranstvavremeniityagoteniya,955,Fizmazgiz,oscow.   
Froeschlé,M.,FMignard,andF.Arenou (1997).Determination of thePPN Parametery with the HipparcosData.InProceedingsofthe ESASymposium“Hipparcos-Venice97",13-16May 1997 Venice,Italy,VolumeSP-402,pp.49.ESA.   
Fukushima,T.(1991).Geodesic nutation.Astronomy and Astrophysics244,L11.   
IAU(20o1).InH.Rickman (Ed.),Transactions of theInternational Astronomical Union,Volume XXIVB,San Francisco.Astronomical Society of the Pacific.Proc.24th General Assembly, Manchester,2000.   
IAU(2007).In O.Engvold (Ed.),Transactions of the International Astronomical Union,Volume XXVB,San Francisco.Astronomical Society of the Pacific.Proc.25th General Assembly, Sydney,2003.   
IERS(20O4).Conventions (2Oo3).Technical Note32,International EarthRotation Service,Frankfurt amMain.VerlagdesBundsesamts fuirKartographieund Geodäsie,D.D.McCarthyandG.Petit (Eds.).   
Klioner,S.,N.Capitaine,W.Folkner,B.Guinot,T.Y.Huang,S.Kopeikin,G.Petit,E.Pitjeva,P.K. Seidelmann,andM.Soffel(2Oo9).UnitsofRelativistic Time Scalesand Associated Quantities.In S.Kioner,P.K.Sidelmann,andM.Sofel (Eds.),ProceedingsofIAUSymposium261.Ratiity inFundamentalstronomy:DyamicsReferenceFramesndataAnalysis,.79.Cmbdge University Press.   
Klioner,S.A.(1992).The problem of clock synchronization-A relativisticapproach.Celestial MechanicsandDynamicalAstronomy53,81-109.   
Klioner,S.A.(2oo3).A Practical Relativistic Model forMicroarcsecond Astrometry in Space. Astronomical Journal 125,1580-1597.   
Klioner,S.A.(2O04).Physically adequate proper reference system of a test observer and relativistic descriptionof theGAIAattitude.Physcial ReviewD69(12),124001.   
Klioner,S.A.(2oo8).Relativistic scaling of astronomical quantities and the system of astronomical units.Astronomy and Astrophysics 478(3),951-958.   
Klioner,S.A.andM.Soffel(1998).Nonrotating astronomical relativistic reference frames.Astronomy and Astrophysics334,1123-1135.   
Klioner,S.A.and M.Sofel (2ooo).Relativistic celestial mechanics with PPN parameters.Physcial Review D 62(2),ID 024019.   
Klioner,S.A.andM.Soffel(2Oo5).Refining theRelativistic ModelforGaia:Cosmological Effects in theBCRS.InC.Turon,K.S.O'Flaherty,andM.A.C.Perryman (Eds.),TheThree-Dimensional Universewith Gaia:ProceedingsoftheGAIA meeting4-7October2004,Paris,VolumeSP-576, Pp.305.ESA.   
Klioner,S.A.andA.V.Voinov(1993).Relativistic theory ofastronomical reference systems inclosed form.PhyscialReviewD48,1451-1461.   
Kopeikin,S.M.and G.Schäfer(1999).Lorentz covariant theoryof light propagation ingravitational fields of arbitrary-movingbodies.Physcial ReviewD60(12),124002.   
Kopeikin,S.M.and I.Vlasov (2Oo4).Parametrized post-Newtonian theory of reference frames, multipolar expansions and equations of motion in the N-body problem.Physics Reports 400(4-6), 209-318.   
Lebach,D.E.,B.E.Corey,S.I.I.,M.I.Ratner,J.C.Webber,A.E.E.Rogers,J.L.Davis,and T.A.Herring(1995).Measurementof theSolarGravitationalDeflectionof Radio Waves Using Very-Long-BaselineInterferometry.Physical Review Letters75(8),1439-1442.   
Lemonde,P.,P.Laurent,G.Santarelli,M.Abgrall,Y.Sortais,S.Bize,C.Nicolas,S.Zhang,A.Clairon, N.Dimarcq,P.Petit,A.G.Mann,A.N.Luiten,S.Chang,and C.Salomon (2001).Cold-Atom ClocksonEarthndiSace.IA.N.uiten(Ed.)FrequencyMeasurementandCotrolp 131-153. Springer.   
Misner,C.,K. Thorne,andJ.A.Wheeler(1973).Gravitation.San Francisco: Freeman.   
Moyer,T.D.(1981).Transformation fromProper Time on Earth to Coordinate Timein Solar System Barycentric Space-TimeFrameofReference,PartsIandII.Celestial Mechanicsand Dynamical Astronomy23(1),33&68.   
Muler,J.,M.Soffel,andS.A.Klioner(2oo8).Geodesyandrelativity.JournalofGeodesy82,33-145.   
Soffel,M.(1989).Relativity inAstrometry,Celestial MechanicsandGeodesy.Berlin:Springer.   
Soffel,M.,S.A.Klioner,G.Petit,P.Wolf,S.M.Kopeikin,P.Bretagnon,V.A.Brumberg,N.Capitaine, T.Damour,T.Fukushima,B.Guinot,T.Huang,L.Lindegren,C.Ma,K.Nordtvedt,J.C.Ries, P.K.Seidelmann,D.Vokrouhlicky,C.M.Will,andC.Xu (2003).The IAU200o Resolutions forAstrometry,Celestial Mechanics,andMetrologyin theRelativistic Framework:Explanatory Supplement.Astronomical Journal126,2687-2706.   
Standish,M.(1998).Time scales in the JPLand CfA ephemerides.Astronomy and Astrophysics336, 381-384.   
Weinberg,S.(1972).Gravitationand Cosmology:Principlesand ApplicationsoftheGeneral Theory ofRelativity.NewYork:J.Wiley&Sons.   
Will,C.M.(1993).Theoryand ExperimentinGravitationalPhysics.Cambridge:Cambridge University Press.   
Wolf,P.and G.Petit (1995).Relativistic theory forclock syntonizationand therealizationof geocentric coordinate times.Astronomy and Astrophysics304,653-661.

# Time

D.McCARTHY&B.GUINOT

# 3.1 Introduction

Measurement of time requires knowledge of an observable,repeatable phenomenon and a conventional reference by which the changes in the repeatable phenomenon can be described. The rotation of the Earth,for example,has been used throughout history as a convenient measure of time where the repeatable phenomenon is the daily repetition of sunrise or sunset. A number of conventional dating and timing systems have been used to distinguish epochs depending on cultural preferences.

Common civil or technical timescales in modern times have made use of three types of repeatablephenomena.These are(1） the Earth's rotation,(2) therevolution of the Earth around the Sun,and (3) atomic energy level transitions.Each of these processes has provided avariety of timescales that have been used to meet particular user applications.The conventional units of time (i.e.,days,hours,minutes,seconds) are defined in each of these systems, but because the underlying phenomena are not equivalent,each of these units is of different length.The length of the second currently accepted as the international standard in the International SystemofUnits (SI) is defined as the duration of 9192631770 periodsof the radiation corresponding to the transition between the two hyperfine levels of the ground state of the caesium133 atom,and isreferred to as the SI second (BIPM2006).Units of time in this chapter correspond to the SI definition of the second unless otherwise stated.The historicaldevelopmentof timekeepingis outlinedin Explanatory SupplementtotheAstronomical Almanac (1992).More information on Time is givenin McCarthy and Seidelmann (2009).

# 3.1.1Absolute (or Newtonian) Time

Absolute time is conceptually a unique uniform time valid for the whole universe to be used in the expresson of the laws of physicsand in particular of Newtonian mechanics. Theincreasing accuracy of measurements led progressively,during the 2Oth century,to the adoption of Special Relativityand General Relativity,and to the introductionof the notions of proper time and coordinate time (see $\ S 3 . 1 . 2$ and $\ S \ 3 . 1 . 3 $ ).Therelativistic theoriesare applied in such a way that the Newtonian theory remains a good approximation,but Newtonian time is not used in The Astronomical Almanac.

# 3.1.2 Proper Time

In the theory of General Relativity,proper time is the time measured along the trajectory of an observer in space-time (world line).Proper time is invariant in any coordinate change.In practice,itismeasured byaphysical clock accompanying theobserver.Thisclock should be insensitive to environmental conditions,including gravity or other types of acceleration. These conditionsare fulfilled to a high level of accuracy by atomic clocks.The use of proper time keeps the laws of local physicsand the physical constants involved invariant.Proper time,whichmayalsobecalledclock timeorprocesstime (although this terminologyisnot used in The Astronomical Almanac),cannotbe used for modelingphenomena in extended domains such as those encountered in astronomy.In these domains the time dimension is describedbycoordinate time.

# 3.1.3 Coordinate Time

In the context of General Relativity,a four-dimensional space-time reference system is described by four coordinates among which three are the spatial coordinates and the other is $x _ { 0 } = c t$ ,where $c$ isthevelocity of light in vacuumand $t$ isthecoordinate timein this reference system. Coordinate time provides an unambiguous way of dating events in a specified reference system.Itis the time basis (or coordinate)to be used in the theory of motion referred to this system.The relation of the proper time of an observerto the coordinate time is provided by a metric,which takes into account the observer's motion in space-time and the surrounding masses and energy.

# 3.2 Time and the Earth's Rotation

The rotation of the Earth has long served as the basis for timekeeping.Practical measurement of time using the Earth's rotation depends ondetermining the relationship between areference directiondefinedina rotating terrestrial reference system with respectto areference direction defined in the celestial reference system.

The transformation from the terrestrial reference system(TRS)to the celestial reference system(CRS) at epoch $t$ can be written as

$$
[ \mathbf { C R S } ] = \mathbf { Q } \left( t \right) \mathbf { R } \left( t \right) \mathbf { W } ( t ) \left[ \mathbf { T R S } \right]
$$

where $\mathbf { Q } ( t )$ , $\mathbf { R } ( t )$ ,and $\mathbf { W } ( t )$ are the transformation matrices arising from the motion of the celestial pole in the celestial system,the rotation of the Earth,and the motion of the pole in the terrestrial system,respectively.

Two equivalent procedures were provided in IERS (1996) to transform from the TRS to the CRS.The equinox-based procedure,described as option 1,makes use of the equinox to realize the intermediate reference frame of epoch $t$ .Greenwich Sidereal Time(GST) isused in the transformation matrix $\mathbf { R } ( t )$ and the classical precession and nutation parametersin the transformation matrix $\mathbf { Q } ( t )$ .The second procedure,described as option 2,makes use of the Earth Rotation Angle (0) between the non-rotating origins (Guinot 1979;Capitaine 2000) defining the Celestial Intermediate Origin(CIO)andthe TerrestrialIntermediate Origin (TIO) to realize the intermediate reference frame of epoch $t$ .In this procedure the transformation matrix $\mathbf { R } ( t )$ is

$$
\mathbf { R } ( t ) = \mathbf { R } _ { 3 } ( - \theta )
$$

where $\mathbf { R } _ { 3 }$ represents a rotation about the $\mathbf { Z }$ -axis.

Onlythe second procedure complieswith Resolution B1.8,adopted by the XXIVth GeneralAssembly of the International Astronomical Union (IAU 20O1；URL[6]),which recommends the use of the non-rotating origin both in the CRS and the TRS as well as the position of the Celestial Intermediate Pole (CIP) in the CRS and in the TRS(IERS 2004). In practice,both methodswill give equal results.The CIO-based method was implemented in The Astronomical Almanac beginning with the 20o6 edition.

The Earth's rotation can be described either with respect to the Sun or with respect to a reference frame defined by directions to celestial objects.The two are not equivalent since the orbital motion of the Earth causes the apparent direction to the Sun to move with respect to the celestial reference frame. Time reckoned with respect to the Sun is now designated byasetof timescales and called Universal Time.Time reckoned with respect to the celestial reference frame attached to the equinox iscalled sidereal time.Because the Earth's rotational speed is not constant,the units of timescales based on the Earth's rotation vary with time.

There are three general kinds of variation in the Earth'srotation (Nelsonetal.2Oo1).These are(1)a steady deceleration,(2) random fluctuations,and (3) periodic changes.Analyses of solar eclipses (Stephensonand Morrison 1984,1995) show that the long-term average rate of increase in the length of the day isabout 1.7mspercentury.Energy dissipation by tidal friction correspondsto arateofincreaseinthelength of day of $2 . 3 \mathrm { m s }$ percentury.Toaccount forthe observed deceleration,there must also be a component in the opposite direction acting to decrease the length of day by about O.6 ms per century,which is possibly associated with changes in the figure of the Earth caused by post-glacial rebound(Yoder etal.1983)or with deep ocean dissipation (Egbert and Ray 2000).

Inaddition to this steady decrease in the rotational velocity,the Earth's rotation is subject to apparently random changes (Jones 1949;Brouwer 1952).These were first observed directly using atomic clocks in the mid-195Os (Essen et al.1958).They generate fluctuations in time ofafew seconds over periods of a few decades.These changes are probably due to the interaction of the core and mantle of the Earth.There are also periodic seasonal variations caused principally by meteorological effects and periodic variationscaused by luni-solar tides.The seasonal variation in the length of the day is of the order of $0 . 5 ~ \mathrm { m s }$ (Munk and MacDonald 1975;Lambeck 1980).

# 3.2.1 Sidereal Time

Until the introduction ofthe CIO-based system(IAU 2001) by theIAU in 2000,sidereal time was primarily used to compute hour angles.Now hour angles can be obtained by use of the Earth Rotation Angle $\theta$ ,as shown in $\ S \ 3 . 2 . 1 . 3$ .Sidereal Time has been defined previously in the Explanatory Supplement (1992),p.3 in the equinox-based systemas“the hour angle of the catalog equinox.”Onp.48 it is defined:

“In general terms,sidereal time is the hour angle of the vernal equinox,which is also known as the first point of Aries.”

It goes on to distinguish

“The sidereal time measured by the hour angle of the true equinox—i.e.,the intersection of the true equator of date with the ecliptic of date-isapparent sidereal time."

and

“The time measured by the diurnal motion of the mean equinox of date,which is affected by onlythe secular inequalities due to the precession of the axis,ismean sidereal time.Apparent sidereal time minus mean sidereal time is the equation of the equinoxes.”

Despite possible confusion about “catalog”versus“vernal equinox”these definitions represent the traditionally accepted definitions of sidereal time.

The sidereal day is the time interval between successive transits of the equinox implicitly defined by the conventionally adopted precession-nutation model; it is approximately equal to 86164.O905 SI seconds.It represents the Earth's rotation with respect to the Celestial IntermediateReference System,i.e.,the geocentric reference systemrelated to the Geocentric Celestial Reference System bya time-dependent rotation taking precession-nutation into account.Because of precession,the sidereal day is not equivalent to the period of rotation of the Earth in inertial space.It isabout O.Oo84s shorter than the actual rotation period,which isapproximately 86164.0989 mean solar seconds.

3.2.1.1Calculating Sidereal Time with IAU 2000A Nutationand IAU 2006 Precession The relationship between Greenwich Sidereal Time (GST)and the Earth Rotation Angle (θ) isdescribed in IERS(2Oo4).The term Greenwich Sidereal Time refers to the sidereal time measuredatthose locations with terrestriallongitudeof $0 ^ { \circ }$ .Theselocationsmaybe considered to be on the Greenwich meridian but this term is loosely defined.The numerical expression consistent with theIAU 2000A nutation (IAU 2001,res.B1.6;URL[6]) and IAU2006 precession models (IAU 2oo8,res.B1; URL[6]) was obtained following a procedure ensuring consistency at the microarcsecond level with the previous expression as wellas continuity in UT1at the date of change on1January 2OO3 (Capitaine,Wallace,and McCarthy 2003).The numerical expression for Greenwich Sidereal Time can be split into two components.

The first component is the Earth Rotation Angle defined by its relationship to $\mathrm { U T 1 = }$ $\mathrm { U T C } + ( \mathrm { U T 1 } - \mathrm { U T C } )$ ，,

$$
\theta ( t _ { U } ) = 2 \pi ( 0 . 7 7 9 0 5 7 2 7 3 2 6 4 0 + 1 . 0 0 2 7 3 7 8 1 1 9 1 1 3 5 4 4 8 t _ { U } )
$$

where $t _ { U }$ is the Julian UT1 date-2451545.0.The second component is the equation of the origins, $E _ { 0 }$ ,which equals the accumulated precession-nutation of the equinox in right ascension.It is made up oftwo subcomponents: aportion, $E _ { \mathrm { p r e c } }$ ,representing the accumulated precession,and the equation of the equinoxes, $E _ { e } ( t )$ ,representing the accumulated nutation. Thus, $E _ { 0 } ( t ) = E _ { \mathrm { p r e c } } ( t ) - E _ { e } ( t ) .$ The precession portion is given in units of arcseconds by

$$
\begin{array} { r l } & { E _ { \mathrm { p r e c } } ( t ) = - 0 . {  { \stackrel { \prime } { \operatorname { \prime } } } } 0 1 4 5 0 6 - 4 6 1 2 {  { \stackrel { \prime \prime } { \operatorname { \prime } } } } 1 5 6 5 3 4 t - 1 {  { \stackrel { \prime \prime } { \operatorname { \prime } } } } 3 9 1 5 8 1 7 t ^ { 2 } } \\ & { \qquad + 0 . {  { \stackrel { \prime \prime } { \operatorname { \prime } } } } 0 0 0 0 0 4 4 t ^ { 3 } + 0 {  { \stackrel { \prime \prime } { \operatorname { \prime } } } } 0 0 0 0 2 9 9 5 6 t ^ { 4 } } \end{array}
$$

where $t$ ismeasured in the terrestrial timescale (TT; see $\ S \ 3 . 4 . 2 $ ,inJuliancenturiesof 36525 days,from JD2451545.0at12hTT.The equationof the equinoxes,inarcseconds,is given by

where $\Delta \psi$ is the nutation in longitude, $\varepsilon _ { A }$ isthe obliquity referred to the eclipticof date, $F$ $_ { D }$ ,and $\Omega$ are fundamental luni-solar arguments. Greenwich Sidereal Time is then given by

$$
\mathrm { G S T } ( t _ { U } , t ) = \theta ( t _ { U } ) - E _ { 0 } ( t ) .
$$

This is often referred to as Greenwich Apparent Sidereal Time (GAST).Greenwich Mean Sidereal Time (GMST),then,is givenby

$$
\mathrm { G M S T } ( t _ { U } , t ) = \theta ( t _ { U } ) - E _ { \mathrm { p r e c } } ( t ) .
$$

So that

$$
\mathrm { G S T } ( t _ { U } , t ) = \mathrm { G M S T } ( t _ { U } ) + E _ { e } ( t ) .
$$

Daily tabulations of Greenwich mean and apparent sidereal time, nutation in longitude, and obliquity referred to the ecliptic are provided in The Astronomical Almanac;also included are examples ofcomputing local sidereal time.The expressions for GSTand GMST distinguish between $\theta$ ,expressed asa functionof Universal Time,and the accumulated precession-nutation in rightascension,which isexpressedasafunctionof Terrestrial Time (TT) (see $\ S \ 3 . 4 . 2$ ).Theexpression forGreenwichMean Sidereal Time(GMST) ofAoki et al.(1982) thatwasadopted previously used only Universal Time (UT1),giving rise to an additional difference dGMSTof(TT-UT1) multiplied by the speed of precession in right ascension. If $\mathrm { T T - T A I } = 3 2 . 1 8 4$ s (see $\ S \ 3 . 4 . 2 )$ ,this is given by:

$$
d \mathrm { G M S T } = 4 7 \mu \mathrm { a s } + 1 . 5 \mu \mathrm { a s } \left( \mathrm { T A I } - \mathrm { U T 1 } \right)
$$

where TAI-UT1isinseconds.

A convenient expression for GMST in time units is given by

$$
\mathbf { G M S T } ( t _ { U } , t ) = 8 6 4 0 0 \mathrm { s } ( 0 . 7 7 9 0 5 7 2 7 3 2 6 4 0 + 1 . 0 0 2 7 3 7 8 1 1 9 1 1 3 5 4 4 8 t _ { U } )
$$

$$
\begin{array} { r l } & { + 0 . 0 0 0 9 6 7 0 7 \mathrm { s } + 3 0 7 . 4 7 7 1 0 2 2 7 \mathrm { s } t + 0 . 0 9 2 7 7 2 1 1 3 \mathrm { s } t ^ { 2 } } \\ & { - 0 . 0 0 0 0 0 0 0 2 9 \mathrm { s } t ^ { 3 } - 0 . 0 0 0 0 0 0 1 9 9 7 \mathrm { s } t ^ { 4 } . } \end{array}
$$

Toenumerate successive sidereal days,the concepts of Greenwich sidereal date and Greenwich sidereal day number have sometimes beenused.The Greenwich sidereal date is definedas the intervalin sidereal days elapsedon the Greenwich meridian since the beginning of the sidereal day thatwas inprogressat JulianDate O.O (See $\ S 3 . 7$ fora discussion of Julian

Date).The integral part ofthe Greenwich sidereal date is the Greenwich sidereal day number, whichistabulateddailyin TheAstronomical Almanac.

# 3.2.1.2Calculating Hour Angles in the Equinox-based System

he equinox-based system,sidereal time is used to calculate hour angle using the relations:

(See $\ S 7 . 1 . 3$ for a discussion of apparent right ascension).

# 3.2.1.3Calculating Hour Angles in the ClO-based System

In the CIO-based system,using the linear expression for Earth Rotation Angle $\theta ( t _ { U } )$ (see Eq.3.3) the calculation of hour angles is simpler than using sidereal time.

$$
\begin{array} { r l } & { \mathrm { l o c a l ~ h o u r ~ a n g l e = E a t t h ~ R o t a t i o n ~ A n g l e - i n t e r m e d i a t e ~ r i g h t ~ a s c e n s i o n } } \\ & { \qquad + \mathrm { e a s t ~ l o n g i t u d e , ~ o r } } \\ & { \mathrm { l o c a l ~ h o u r ~ a n g l e = G A S T + e q u a t i o n ~ o f ~ t h e ~ o r i g i n s } } \\ & { \qquad - \mathrm { i n t e r m e d i a t e ~ r i g h t ~ a s c e n s i o n + e a s t ~ l o n g i t u d e } , } \end{array}
$$

where the intermediate right ascension is computed using the IAU 2OoO recommendations. Calculating hour angles using either the equinox-based system or the CIO-based system will provide identical results.Note that the Earth Rotation Angle is (nearly) the Greenwich Hour Angle of the right ascension origin of the International Celestial Reference System,a convenience formental arithmetic.

# 3.2.2 UT1

UT1 isa measure of the Earth's rotation angle expressedin time units and treated conventionally as an astronomical timescale defined by the rotation of the Earth with respect to the Sun. In practice,Universal Time Was defined until1January 2Oo3 by means of conventional formulae defining sidereal time.Resolution B1.8 adopted by the XXIVth General Assembly of the International Astronomical Union (IAU 2Oo1;URL[6]) recommended the use of the nonrotating origin(Guinot1979) both in the Geocentric Celestial Reference System(GCRS)and theInternational Terrestrial Reference System (ITRS).These origins are designated as the Celestial Intermediate Origin(CIO) and the Terrestrial Intermediate Origin (TIO) in these systems,respectively.The EarthRotationAngleisdefinedas theanglemeasuredalong the equatorof the Celestial Intermediate Pole between the CIO and the TIO.This resolution also recommended that UT1be linearly proportional to the Earth Rotation Angle,and that the transformation between the ITRS and GCRS be specified using the Earth Rotation Angle.

The Earth Rotation Angle, $\theta$ ,is linked to UT1by the conventional relationshipas given byCapitaine (2OoO) (Eq.3.3).This definition of UT1 based on the CIO is insensitive at the microarcsecond level to the precession-nutation model and to the observed celestial pole offsets.UT1is observed using Very Long Baseline Interferometry(VLBI) measurements of selected radio point sources,mostly quasars and interpolated by trackingofGPSsatellites. Strictly speaking,because of the motion of satelite orbital nodes in space,VLBI provides the only rigorous determination of UT1.

The ratio of mean sidereal time to UT1 is

$$
\boldsymbol { r } ^ { \prime } = 1 . 0 0 2 7 3 7 3 7 9 0 9 3 5 0 7 9 5 + 5 . 9 0 0 6 \times 1 0 ^ { - 1 1 } t - 5 . 9 \times 1 0 ^ { - 1 5 } t ^ { 2 } .
$$

The ratio of UT1 to mean sidereal time is

$$
1 / r ^ { \prime } = 0 . 9 9 7 2 6 9 5 6 6 3 2 9 0 8 4 - 5 . 8 6 8 4 \times 1 0 ^ { - 1 1 } t + 5 . 9 \times 1 0 ^ { - 1 5 } t ^ { 2 } .
$$

In both Eqs.3.17 and 3.18, $t$ represents the number of Julian centuries elapsed since J2000.0.

UT1 is considered to be nominally equivalent to mean solar time reckoned from midnight on the meridian of Greenwich.The mean solar day is the time interval between successive transits of a conventionally defined direction in the celestial reference system.The mean solarsecond,is1/86400 ofa mean solar day (Kovalevsky1965;McCarthy1991).Before theadoption of the Aoki etal.(1982) expresson for siderealtime asa function of solar time, this conventional point was called the fictitious mean Sun,which was Simon Newcomb's expression for a fictitious point whose motion in the celestial reference system corresponds to the average motion of the Sunin the sky.Apparent solar time,the time determinedby using asundial orbymeasuring thealtitudeof the Sun,is defined bythe motionof the observed Sun.However,the day measured by the time interval between successive passes of the actual Sun over the local meridian varies because the Earth'saxis is tilted in spaceand because the Earth's orbit is not circular.The difference between mean and apparent solar time iscalled the equation of time.The maximum amount by which apparent noon precedes mean noon is about16.5 minutes around 3 November,while the maximum amount by which mean noon precedes apparent noon isabout 14.5 minutes around 12 February (Nelson etal.2001).

UTO,a designation no longerin common use,is UT1 corrupted by the effect of the motion of the pole of the Earth's rotational axis with respect to the terrestrial reference frame.The difference between the two is of the order of a few tens of milliseconds (Guinot 1989).

UT2 isa timescale,rarely used in practice,resulting from a conventional correction to UT1 accounting forthe seasonal variation in the Earth's rotation.The correction accounts for the fact that the Earth rotates slower by about $3 0 ~ \mathrm { m s }$ in Mayand fasterbyasimilar amount in November. The difference between UT2 and UT1 is a conventional expression given in McCarthy (1991).

$$
\mathrm { U T 2 } = \mathrm { U T 1 } + 0 . 0 2 2 \mathrm { s } \sin 2 \pi t _ { B } - 0 . 0 1 2 \mathrm { s } \cos 2 \pi t _ { B } - 0 . 0 0 6 \mathrm { s } \sin 4 \pi t _ { B } + 0 . 0 0 7 \mathrm { s } \cos 4 \pi t _ { B }
$$

where $t _ { B }$ is the fractionof the Besselian year and given by

$$
t _ { B } = \mathrm { m o d } \left[ 2 0 0 0 + \frac { \left( \mathrm { J u l i a n ~ D a t e } - 2 4 5 1 5 4 4 . 5 3 3 \right) } { 3 6 5 . 2 4 2 2 } , 1 \right] .
$$

# 3.3Dynamical Time

A timescale based on the dynamics of the motions of solar system bodies was originally conceived as an answer to the need fora more uniform,astronomically-based timescale.

Ephemeris Time,which came into use in the195Os,was based on ephemerides that assumed Newtonian mechanics.Since that time,aseries of dynamical timescales have been developed toaccount for evolving developments in modeling the effects of general relativity.In current practice,dynamical timescales are used to provide the independent variable of the equations of motion of the bodies in the solar system.

# 3.3.1 Ephemeris Time

Ephemeris Time (ET) refers to the timescale suggested by G.M.Clemence (1948).He proposed a timescale based on the period of the revolution of the Earth around the Sun,as represented by Newcomb'sTablesof the Sunpublished in1895.ETisdefined practically through the use of Newcomb's formula for the geometric mean longitude of the Sun (Newcomb 1895):

$$
L = 2 7 9 ^ { \circ } 4 1 ^ { \prime } 4 8 ^ { \prime \prime } 0 4 + 1 2 9 6 0 2 7 6 8 ^ { \prime \prime } 1 3 T + 1 ^ { \prime \prime } 0 8 9 T ^ { 2 }
$$

where $T$ isthe time reckoned in Julian centuries of 36 525 days since January O,1900,12h UT.TheIAU adopted this proposalin 1952 at its 8th General Assembly inRome (IAU1954).

Newcomb's formula implies that,ifwe use the motion of the Sun at $T = 0$ ，thatis $\delta L / \delta T = 1 2 9 6 0 2 7 . ^ { \prime \prime } 6 8 1 3$ per year,we would expect the year to contain

$$
3 6 5 . 2 5 \mathrm { d a y s } \times 8 6 4 0 0 \mathrm { s } / \mathrm { d a y } \times ( 3 6 0 \times 6 0 \times 6 0 ^ { \prime \prime } / \mathrm { r e v . } ) / ( \delta L / \delta T ) = 3 1 5 5 6 9 2 5 . 9 7 4 7 \mathrm { s } .
$$

The 10th General Conferenceon Weightsand Measures (CGPM) in1954,therefore,proposed the definition of the second,‘The second is the fraction 1/31 556 925.975 of the length of the tropical year for19oo.0.’Consequently the International Committee forWeights and Measures(CIPM) in1956,defined the second of ephemeris time to be “the fraction1/31556 925.9747of the tropical year for19oo JanuaryOat12 hours ephemeris time.”This definition wasratified by the11th CGPMin1960 (BIPM1956;BIPM2006,p.148).In1958,the International Astronomical Union General Assembly defined the epochofETby (IAU1960): “Ephemeris Time(ET),or Tempsdes Ephémérides (TE),isreckoned from the instant,near the beginning of the calendar year A.D.19oo,when the geometric mean longitude of the Sun was $2 7 9 ^ { \circ } 4 1 ^ { \prime } 4 8 . ^ { \prime \prime } 0 4$ ,at which instant the measure of Ephemeris Time was 19Oo January $0 ^ { \mathrm { d } }$ $1 2 ^ { \mathrm { h } }$ precisely."

AsNewcomb's formula (Eq.3.21) was mostly based on observations made during the 19th century and referred to mean solar time,the duration of the ephemeris second represents approximately the mean duration of the second of mean solar time during this century.

AlthoughETwasdefined using Newcomb's expression, it was realized using observations of the positionof the Moon with respectto thecelestialreference frame.These observed lunar positions were used together with conventional lunar ephemerides to derive estimates of ET. This led to asetof realizations ofETbased on the actual ephemeris used that were denoted ETO,ET1 and ET2 (Guinot 1989).

ET was determined in practice using the expression

$$
\mathrm { E T } = \mathrm { U T 1 } + \Delta T
$$

where $\Delta T$ was determined from astronomical observations.

Although astronomical ephemeridesadoptedETasthe independentvariable,itwas inconvenient to obtain accuratereal-time estimates of ET,and it did not includerelativistic effects,nor did it distinguish between properand coordinate time.

# 3.3.2 TDT/TDB

The 16th IAU General Assemblyin 1976 defined time-like arguments,consistent with the general theory of relativity,that distinguish coordinate systemswith origins at the center of theEarth and the center of the solar system (IAU1977).The recommendations for the definition of dynamical time adopted at the IAU General Assembly of 1976 were:

(a)At the instant 1977 January $0 1 ^ { \mathrm { d } } \ 0 0 ^ { \mathrm { h } } \ 0 0 ^ { \mathrm { m } } \ 0 0 ^ { \mathrm { s } }$ TAI,the value of the new timescale forapparent geocentric ephemerideswillbe 1977 January1d.oo0 3725（ $1 ^ { \mathrm { d } } 0 0 ^ { \mathrm { h } } 0 0 ^ { \mathrm { m } }$ 32184) exactly.   
(b) The unit of this timescale willbe a day of 86 4Oo SI seconds at mean sea level.   
(c）The timescales for equations of motion referred to the barycenter of the solar system will be such that there will be only periodic variations between these timescales and those of the apparent geocentric ephemerides.

These were given the names Terrestrial Dynamical Time (TDT)and Barycentric Dynamical Time (TDB),respectively,in 1979 (IAU 1980).

The epoch of TDT is referred to International Atomic Time(TAI) on1 January 1977 $0 ^ { \mathrm { h } }$ , as shown in(a) above (see $\ S \ 3 . 4$ fora discussion of TAI).Its basic unit is the SI second,and it maintains continuity with ET.The reason for the selection of the epoch in January 1977 is that atthis time,arate correction of $- 1 0 \times 1 0 ^ { - 1 3 }$ was applied to TAI to bring the unit of TAI more closely into accord with the SI second (IAU 1977,p.66; Seidelmann 1992,p. 85).For years prior to1955,when atomic time was not available,TDTmustbe extrapolated backward,using dynamical theory fit to observations.

During the 198Os,the definition of TDB was found to be ambiguous.In particular, the form of the relativistic metric was not made explicit.This led to improvements in 1991,2000, and 2006 (see $\ S \ S . 6 \ O$ . $\mathrm { T _ { e p h } }$ (see $\ S \ 3 . 6 . 1$ )is now essentially equivalent to TDB.

# 3.4 Atomic Time

In1955,L.EssenandJ.V.L.Parryof theNational PhysicalLaboratory(NPL)calibrated the resonance frequency of the laboratory'scaesium standard with respect to the UT2 second of that epoch (Essen and Parry 1955).Together with $\scriptstyle \mathrm { W m }$ .Markowitz and R.G.Hallat theU. S.Naval Observatory (USNO),they later calibrated the frequency in terms of the ET second using observations made with the USNO dual-rate Moon camera over the period 1955.50 to 1958.25.The measured caesium frequency was9192 631 770 Hz with an uncertainty of $\pm 2 0$ Hz,mostly due to the measurement of ET (Markowitz et al.1958).

In1967the 13th CGPMadopted the atomic second as the unit of time in the International System of Units.It was definedas“the duration of9192 63177O periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the