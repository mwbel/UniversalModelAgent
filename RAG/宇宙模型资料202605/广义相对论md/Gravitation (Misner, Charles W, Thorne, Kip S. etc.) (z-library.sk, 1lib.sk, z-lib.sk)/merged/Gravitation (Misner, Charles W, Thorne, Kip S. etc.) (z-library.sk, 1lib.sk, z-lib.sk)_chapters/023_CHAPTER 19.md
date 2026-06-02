CHAPTER 19

# MASS AND ANGULAR MOMENTUM OF A GRAVITATING SYSTEM

# S19.1. EXTERNAL FIELD OF A WEAKLY GRAVITATING SOURCE

Metric far from a weakly gravitating system,as a power series in $1 / r \colon$

Consider an isolated system with gravity so weak that in calculating its structure and motion one can completely ignore self-gravitational effects. (This is true of an asteroid,and of a nebula with high-energy electrons and protons spiraling in a magnetic field; it is not true of the Earth or the sun.) Assume nothing else about the system--for example,by contrast with Newtonian theory,allow velocities to be arbitrarily close to the speed of light, and allow stresses $T ^ { j k }$ and momentum densities $T ^ { 0 j }$ to be comparable to the mass-energy density $T ^ { 0 0 }$

(1） derivation

Calculate the weak gravitational field,

$$
\begin{array} { c } { { g _ { \mu \nu } = \eta _ { \mu \nu } + h _ { \mu \nu } , } } \\ { { { \overline { { { h } } } } _ { \mu \nu } \equiv h _ { \mu \nu } = \displaystyle \int \frac { 4 \overline { { { T } } } _ { \mu \nu } ( t - | x - x ^ { \prime } | , x ^ { \prime } ) } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } } \end{array}
$$

produced by such a system [see “baired” version of equation (l8.14)]. Restrict attention to the spacetime region far outside the system, and expand $h _ { \mu \nu }$ in powers of ${ \pmb x } ^ { \prime } / r \equiv { \pmb x } ^ { \prime } / | { \pmb x } |$ ,using the relations

$$
\overline { { T } } _ { \mu \nu } ( t - \vert x - x ^ { \prime } \vert , x ^ { \prime } ) = \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } \biggl [ \frac { \partial ^ { n } } { \partial t ^ { n } } \ : \overline { { T } } _ { \mu \nu } ( t - \ r , x ^ { \prime } ) \biggr ] ( r - \vert x - x ^ { \prime } \vert ) ^ { n } ,
$$

$$
r - | x - x ^ { \prime } | = x ^ { j } \left( { \frac { x ^ { j ^ { \prime } } } { r } } \right) + { \frac { 1 } { 2 } } { \frac { x ^ { j } x ^ { k } } { r } } \left( { \frac { x ^ { j ^ { \prime } } x ^ { k ^ { \prime } } - r ^ { \prime 2 } \delta _ { j k } } { r ^ { 2 } } } \right) + \cdot \cdot \cdot ,
$$

$$
{ \frac { 1 } { | x - x ^ { \prime } | } } = { \frac { 1 } { r } } + { \frac { x ^ { j } } { r ^ { 2 } } } { \frac { x ^ { j ^ { \prime } } } { r } } + { \frac { 1 } { 2 } } { \frac { x ^ { j } x ^ { k } } { r ^ { 3 } } } { \frac { ( 3 x ^ { j ^ { \prime } } x ^ { k ^ { \prime } } - r ^ { \prime 2 } \delta _ { j k } ) } { r ^ { 2 } } } + \cdot \cdot \cdot .
$$

Perform the calculation in the system's rest frame, where

$$
P ^ { j } \equiv \int { \cal T } ^ { 0 j } d ^ { 3 } x = 0 ,
$$

with origin of coordinates at the system's center of mass

$$
\int x ^ { j } T ^ { 0 0 } d ^ { 3 } x = 0 .
$$

The result, after a change of gauge to simplify $h _ { 0 0 }$ and $h _ { 0 j } ,$ is

$$
\begin{array} { l } { { d s ^ { 2 } = - \left[ 1 - \frac { 2 M } { r } + 0 \left( \frac 1 { r ^ { 3 } } \right) \right] d t ^ { 2 } - \left[ 4 \epsilon _ { j k l } S ^ { \star } \frac { x ^ { t } } { r ^ { 3 } } + 0 \left( \frac 1 { r ^ { 3 } } \right) \right] d t d x ^ { j } } } \\ { { \mathrm { ~ \ ~ \ } + \left[ \left( 1 + \frac { 2 M } { r } \right) \delta _ { j k } + \left( _ { \mathrm { t h a t \ d i e \ o u t \ a s \ 0 ( l / r ) } } ^ { \mathrm { g r a v i t a t i o n \ } } \mathrm { t e r m s } \right) \right] d x ^ { j } d x ^ { k } . } } \end{array}
$$

(2）result

(see exercise 19.1 for derivation.) Here $M$ and $S ^ { k }$ are the body's mass and intrinsic angular momentum.

$$
\begin{array} { l } { { \displaystyle M = \int T ^ { 0 0 } d ^ { 3 } x , } } \\ { { \displaystyle S _ { k } = \int \epsilon _ { k l m } x ^ { \ell } T ^ { m 0 } d ^ { 3 } x . } } \end{array}
$$

The corresponding Newtonian potential is

$$
\phi = - \frac { 1 } { 2 } ( g _ { 0 0 } - \eta _ { 0 0 } ) = - \frac { M } { r } + 0 \left( \frac { 1 } { r ^ { 3 } } \right) .
$$

Conclusion: With an appropriate choice of gauge, $\pmb { \phi }$ and $g _ { 0 0 }$ far from any weak source are time-independent and are determined uniquely by the source's mass $M ;$ $g _ { 0 j }$ is time-independent and is fixed by the source's intrinsic angular momentum $S ^ { j }$ but $g _ { j \pmb { k } }$ has time-dependent terms (gravitational waves!) of $0 ( 1 / r )$

The rest of this chapter focuses on the “imprints” of the mass and angular momentum in the gravitational field; the gravitational waves will be ignored, or almost so, until Chapter 35.

How metric depends on system's mass $M$ and angular momentum $\pmb { S }$

# Exercise 19.1. DERIVATION OF METRIC FAR OUTSIDE A WEAKLY GRAVITATING BODY

(a) Derive equation (l9.5).[Hints: (l) Follow the procedure outlined in the text. (2) When calculating $h _ { 0 0 }$ ,write out explicitly the $n = 0$ and $n = 1$ terms of (19.2), to precision $0 ( 1 / r ^ { 2 } )$ ， and simplify the $n = 0$ term using the identities

$$
\begin{array} { l } { { \displaystyle T ^ { j k } = \frac { 1 } { 2 } ( T ^ { 0 0 } x ^ { j } x ^ { k } ) _ { , 0 0 } + ( T ^ { i j } x ^ { k } + T ^ { t k } x ^ { j } ) _ { , t } - \frac { 1 } { 2 } ( T ^ { t m } x ^ { j } x ^ { k } ) _ { , t m } } , } \\ { { \displaystyle T ^ { t t } x ^ { m } = \bigg ( T ^ { 0 t } x ^ { t } x ^ { m } - \frac { 1 } { 2 } T ^ { 0 m } r ^ { 2 } \bigg ) _ { , 0 } + \bigg ( T ^ { t k } x ^ { k } x ^ { m } - \frac { 1 } { 2 } T ^ { t m } r ^ { 2 } \bigg ) _ { , t } . } } \end{array}
$$

(Verify that these identities follow from $T ^ { \alpha \beta } { } _ { , \beta } = 0 .$ ）(3）When calculating $h _ { 0 m }$ ，write out explicitly the $n = 0$ term of (19.2),to precision $0 ( 1 / r ^ { 2 } )$ ,and simplify it using the identity

$$
T ^ { 0 k } x ^ { j } + T ^ { 0 j } x ^ { k } = ( T ^ { 0 0 } x ^ { j } x ^ { k } ) _ { , 0 } + ( T ^ { 0 \ell } x ^ { j } x ^ { k } ) _ { , \ell } .
$$

(Verify that this follows from $T ^ { \alpha \beta } { } _ { , \beta } = 0 .$ ) (4) Simplify $h _ { 0 0 }$ and $h _ { 0 m }$ by the gauge transformation generated by

$$
\begin{array} { r l } & { \xi _ { 0 } = \frac { 1 } { 2 r ^ { 3 } } \frac { \partial } { \partial t } \int T ^ { \infty } r ^ { \prime \prime } d ^ { 3 \nu } + \frac { x ^ { \prime } } { r ^ { 3 } } \int ( T ^ { \infty } x ^ { \star } x ^ { \star } x ^ { \prime \prime } - \frac { 1 } { 2 } T ^ { \nu } r ^ { \prime \prime } ) d ^ { 3 } x ^ { \prime } } \\ & { \qquad + \int ( T _ { 0 ^ { \prime } } + T _ { t } ) [ \frac { x ^ { \prime } x ^ { \prime \prime } } { r ^ { 2 } } + \frac { ( 3 x ^ { \prime } x ^ { \star } x ^ { \prime \prime } - r ^ { 2 } \delta ) \sigma ^ { \star } x ^ { \prime \prime } } { 2 r ^ { 4 } } ] d ^ { 3 } x ^ { \prime } } \\ & { \qquad + \underbrace { \frac { \dot { x } } { r } } _ { \mathrm { s = 2 } } \frac { 1 } { x ^ { 1 } } \frac { \tilde { \sigma } ^ { n - 1 } } { \partial t ^ { n - 1 } } \int ( T _ { 0 ^ { \prime } } + T _ { \star \star } ) \frac { ( r - | x - x ^ { \prime } | ) ^ { \alpha } } { | x - x ^ { \prime } | } d x _ { x ^ { \prime } } , } \\ & { \dot { \varepsilon } _ { \mathrm { n } } = - \frac { 2 x ^ { \prime } } { r ^ { 3 } } \int T _ { 0 ^ { \prime } } \mathrm { s } \mathrm { e } ^ { x ^ { \prime } x ^ { \prime \prime } } d ^ { 3 x ^ { \prime } } + 4 \frac { \dot { x } } { r ^ { 3 } } \frac { 1 } { x ^ { 1 } } \frac { \tilde { \sigma } ^ { n - 1 } } { | \dot { x } ^ { n - 1 } | } \int _ { 0 ^ { \prime } } \frac { ( r - | x - x ^ { \prime } | ) ^ { \alpha } } { | x - x ^ { \prime } | } d ^ { 3 \nu ^ { \prime } } } \\ &  \qquad + \frac { x ^ { \prime \prime } } { r } \delta _ { 0 ^ { - 1 } } - \frac { 1 } { 2 } ( \frac { 1 } { r ^ { 2 } } ) _ { m } \int T _ { 0 ^ { \prime } } r ^ { \prime \prime } d ^ { 3 } x ^ { \prime } - ( \frac { x ^ { \prime } } { r ^ { 2 } } ) _ { \mathrm { o r } } \int ( T ^ { \infty } x ^  \ \end{array}
$$

Here $T _ { \mu \nu } ^ { \quad \prime }$ denotes $T _ { \mu \nu } ( t - r , x ^ { \prime } ) . ]$

(b) Prove that the system's mass and angular momentum are conserved. [Note: Because $T ^ { \alpha \beta } { } _ { , \beta } = 0$ (selfgraviyegibee)eoste spacetime (Chapter 5).]

# $\$ 19.2$ .MEASUREMENT OF THE MASS AND ANGULAR MOMENTUM

For a weakly gravitating system:

(1） total mass $M$ can be measured by applying Kepler's $" 1 - 2 - 3 "$ law to orbiting particles

The values of a system's mass and angular momentum can be measured by probing the imprint they leave in its external gravitational field. Of all tools one might use to probe, the simplest is a test particle in a gravitationally bound orbit. If the particle is sufficiently far from the source, its motion is affected hardly at all by the source's angular momentum or by the gravitational waves; only the spherical, Newtonian part of the gravitational field has a significant influence. Hence, the particle moves in an ellptical Keplerian orbit. To determine the source's mass $M _ { i }$ one need only apply Kepler's third law (perhaps better called “Kepler's $1 - 2 - 3 \ \mathrm { i a w } ^ { \ast \ast } ,$ ：

$$
M = \left( { \frac { 2 \pi } { \mathrm { \ o r b i t a l \ p e r i o d } } } \right) ^ { 2 } \left( { \mathrm { S e m i . m a j o r \ a x i s } } \right) ^ { 3 } ; \qquad { \mathrm { i . e . , } } ~ M ^ { 1 } = \omega ^ { 2 } a ^ { 3 } .
$$

The source's angular momentum is not measured quite so easily. One must use a probe that is insensitive to Newtonian gravitational effects,but “feels” the offdiagonal term,

$$
\displaystyle g _ { 0 j } = - 2 \epsilon ^ { j k \ell } S ^ { k } x ^ { \ell } / r ^ { 3 } ,
$$

in the metric (19.5). One such probe is the precession of the perihelion of a corevolving satellite, relative to the precession for a counterrevolving satelite. A gyroscope is another such probe. Place a gyroscope at rest in the source's gravitational field. By a force applied to its center of mass, prevent it from falling. As time passes, the $g _ { 0 j }$ term in the metric will force the gyroscope to precess relative to the basis vectors $\partial / \partial x ^ { j }$ ； and since these basis vectors are “tied”to the coordinate system, which in turn is tied to the Lorentz frames at infinity, which in turn are tied to the “fixed stars"(cf. $\ S 3 9 . 1 2 \rangle$ , the precession is relative to the “fixed stars.” The angular velocity of precession,as derived in exercise 19.2, is

(2) total angular momentum $\pmb { S }$ can be measured by examining the precession of gyroscopes

$$
\Omega = \frac { 1 } { r ^ { 3 } } \biggl [ - S + \frac { 3 ( S \cdot x ) x } { r ^ { 2 } } \biggr ] ,
$$

One sometimes says that the source's rotation “drags the inertial frames near the source," thereby forcing the gyroscope to precess.For further discussion, see $\ S 8 2 1 . 1 2$ ， 40.7,and 33.4.

# Exercise 19.2. GYROSCOPE PRECESSION

EXERCISE

Derive equation (19.10) for the angular velocity of gyroscope precession. [Hints: Place an orthonormal tetrad at the gyroscope's center of mass. Tie the tetrad rigidly to the coordinate system,and hence to the “fixed stars”;more particularly,choose the tetrad to be that basis $\left\{ e _ { \hat { \alpha } } \right\}$ which is dual to the following l-form basis:

$$
\begin{array} { r } { \pmb { \omega } ^ { i } = [ 1 - ( 2 M / r ) ] ^ { 1 / 2 } d t + 2 \epsilon _ { j k l } S ^ { k } ( x ^ { i } / r ^ { 3 } ) d x ^ { j } , \qquad \pmb { \omega } ^ { j } = [ 1 + ( 2 M / r ) ] ^ { 1 / 2 } d x ^ { j } . } \end{array}
$$

The spatial legs of the tetrad, $\pmb { e _ { \hat { j } } } ,$ ，rotate relative to the gyroscope with an angular velocity $\pmb { \omega }$ given by [see equation (13.69)]

$$
- \epsilon _ { i \hat { j } \hat { k } } \omega ^ { \hat { k } } = { \cal T } _ { \hat { i } \hat { j } \hat { 0 } } .
$$

Consequently, the gyroscope's angular momentum vector $\pmb { L }$ precesses relative to the tetrad with angular velocity $\Omega = - \omega$

$$
\frac { d L ^ { j } } { d \hat { t } } = \epsilon _ { \vdots \hat { k } \hat { \imath } } \varOmega ^ { \hat { k } } L ^ { \hat { \jmath } } , \qquad \epsilon _ { \vdots \hat { \jmath } \hat { k } } \varOmega ^ { \hat { k } } = { \cal T } _ { \hat { \imath } \hat { \jmath } \hat { \imath } } .
$$

Calculate $T _ { \hat { i } \hat { j } \hat { 0 } }$ for the given orthonormal frame,and thereby obtain equation (l9.10) for $\pmb { \Omega }$ ]

# $\$ 19.3$ .MASS AND ANGULAR MOMENTUM OF FULLY RELATIVISTIC SOURCES

Abandon, now, the restriction to weakly gravitating sources. Consider an isolated, gravitating system inside which spacetime may or may not be highly curved-a black hole,a neutron star, the Sun,... But refuse,for now,to analyze the system's interior or the“strong-field region” near the system. Instead, restrict attention to the weak gravitational field far from the source,and analyze it using linearized theory in vacuum. Expand $h _ { \mu \nu }$ in multipole moments and powers of $1 / r ;$ and adjust the gauge, the Lorentz frame,and the origin of coordinates to simplify the resulting metric. .The outcome of such a calculation is a gravitational field identical to that for a weak. source [equation (l9.5)j (Details of the calculation are not spelled out here because of their length; but see exercise 19.3.)

But before accepting this as the distant field of an arbitrary source, one should examine the nonlinear effects in the vacuum field equations. Two types of nonlinearities turn out to be important far from the source: (l） nonlinearities in the static, Newtonian part of the metric, which generate metric corrections

$$
\delta g _ { 0 0 } = - 2 M ^ { 2 } / r ^ { 2 } , ~ \delta g _ { j k } = \frac { 3 } { 2 } ( M ^ { 2 } / r ^ { 2 } ) \delta _ { j k } ,
$$

Metric far from any gravitating system,as a power series in $1 / r$

(see exercise 19.3 and $\ S 3 9 . 8 \}$ , thereby putting the metric into the form

$$
\begin{array} { l } { { d s ^ { 2 } = - \left[ 1 - \displaystyle \frac { 2 M } { r } + \displaystyle \frac { 2 M ^ { 2 } } { r ^ { 2 } } + 0 \left( \displaystyle \frac { 1 } { r ^ { 3 } } \right) \right] d t ^ { 2 } - \left[ 4 \epsilon _ { j k \ell } S ^ { k } \displaystyle \frac { x ^ { \ell } } { r ^ { 3 } } + 0 \left( \displaystyle \frac { 1 } { r ^ { 3 } } \right) \right] d t d x ^ { j } } } \\ { { \mathrm { ~ } + \left[ \left( 1 + \displaystyle \frac { 2 M } { r } + \displaystyle \frac { 3 M ^ { 2 } } { 2 r ^ { 2 } } \right) \delta _ { j k } + \left( \displaystyle \frac { \mathrm { g r a v i t a t i o n a l ~ r a d i a t i o n ~ t e r m s } } { \mathrm { t h a t ~ d i e ~ o u t ~ a s ~ } 0 ( 1 / r ) } \right) \right] d x ^ { j } d x ^ { k } ; } } \end{array}
$$

(2) a gradual decrease in the source's mass, gradual changes in its angular momentum,and gradual changes in its:“rest frame” to compensate for the mass, angular momentum,and linear momentum carried off by gravitational waves (see Box 19.1, which is best read only after finishing this section).

Failure of volume integrals for $M$ and $s$ when source has strong internal gravity

By measuring the distant spacetime geometry (l9.13) of a given source,one cannot discover whether that source has strong internal gravity,or weak.But when one expresses the constants $M$ and $S _ { j } ,$ which determine $g _ { 0 0 }$ and $g _ { 0 j } ,$ as integrals over the interior of the source,one discovers a crucial difference: if the internal gravity is weak, then linearized theory is valid throughout the source, and

$$
M = \int T _ { 0 0 } d ^ { 3 } x , S _ { j } = \int \epsilon _ { j k l } x ^ { k } T ^ { l 0 } d ^ { 3 } x ;
$$

but if the gravity is strong, these formulas fail. Does this failure prevent one, for strong gravity, from identifying the constants $M$ and $S _ { j }$ of the metric (19.13）as the source's mass and angular momentum? Not at all, according to the following argument.

Consider, first, the mass of the sun. For the sun one expects Newtonian theory to be highly accurate (fractional errors $\sim M _ { \odot } / R _ { \odot } \sim 1 0 ^ { - 6 } )$ ；so one can assert that the constant $M$ appearing in the line element (l9.13) is, indeed

$$
M = \int \rho d ^ { 3 } x = \int T _ { 0 0 } d ^ { 3 } x = \mathrm { t o t a l \ m a s s } .
$$

But might this assertion be wrong? To gain greater confidence and insight, adopt the viewpoint of "controlled ignorance"; i.e., do not pretend to know more than what is needed. (This style of physical argument goes back to Newton's famous “Hypotheses non fingo,”i.e.“I do not feign hypotheses.") In evaluating the volume integral of $T _ { 0 0 }$ (usual Newtonian definition of $M$ ),one needs a theory of the internal structure of the sun. For example, one must know that the visible surface layers of the sun do not hide a massive central core,so dense and large that relativistic gravitational fields $| \phi | \sim 1$ exist there. Ifone makes use in the analysis of a fluid-type stres-energy tensor $T ^ { \mu \nu }$ , one needs to know equations of state, opacities, and theories of energy generation and transport. One needs to justify the fluid description as an adequate approximation to the atomic constitution of matter. One needs to assume that an ultimate theory of matter explaining the rest masses of protons and electrons will not assign an important fraction of this mass to strong (nonlinear) gravitational fields on a submicroscopic scale. It is plausible that one could do all this, but it is also obvious that this is not the way the mass of the sun is,in fact, determined by astronomers! Theories of stellar structure are adjusted to give the observed mass; they are not constructed to let one deduce the mass from nongravitational observations.The mass of the sun is measured in practice by studying the orbits of planets in its external gravitational field,a procedure equivalent to reading the mass $M$ off the line element (l9.l3),rather than evaluating the volume integral $\int T ^ { 0 0 } d ^ { 3 } x$

To avoid all the above uncertainties,and to make theory correspond as closely as possible to experiment, one defines the “total mass-energy” M of the sun or any other body to be the constant that appears in the line element (19.13) for its distant external spacetime geometry. Similarly, one defines the body's intrinsic angular momentum as the constant 3-vector S appearing in its line element (19.13). Operationally, the total mass-energy $M$ is measured via Kepler's third law; the angular momentum $s$ is measured via its influence on the precession of a gyroscope or a planetary orbit. This is as true when the body is a black hole or a neutron star as when it is the sun.

Definition of "total mass-energy" $M$ and "angular momentum" $\pmb { S }$ in terms of external gravitational field

What kind of a geometric object is the intrinsic angular momentum S? It is defined by measurements made far from the source, where, with receding distance, spacetime is becoming flatter and flatter (asymptotically flat). Thus, it can be regarded as a 3-vector in the“asymptotically flat spacetime"that surrounds the source. But in what Lorentz frame is $s$ a 3-vector? Clearly, in the asymptotic Lorentz frame where the line element (19.13) is valid; i.e.,in the asymptotic Lorentz frame where the source's distant“coulomb” $( ^ { 6 6 } M / r ^ { 3 3 } )$ field is static; i.e., in the “asymptotic rest frame”of the source. Alternatively, one can regard $s$ as a 4-vector, $\pmb { S } _ { \mathrm { i } }$ ，which is purely spatial $( S ^ { 0 } = 0 )$ in the asymptotic rest frame.If one denotes the 4-velocity of the asymptotic rest frame by $\pmb { U }$ ,then the fact that $\pmb { s }$ is purely spatial can be restated geometrically as $\pmb { S } \cdot \pmb { U } = 0$ ，or

# $\pmb { S }$ as a geometric object in an asymptotically flat region far outside source

"Asymptotic rest frame" and "total 4-momentum"

$$
\begin{array} { r } { \pmb { S } \cdot \pmb { P } = 0 , } \end{array}
$$

where

$$
\pmb { P } \equiv M \pmb { U } \equiv \mathrm { " t o t a l ~ } 4 \mathrm { - m o m e n t u m ~ o f ~ s o u r c e " }
$$

is still another vector residing in the asymptotically flat region of spacetime.

The total 4-momentum $\pmb { P }$ and intrinsic angular momentum $\pmb { s }$ satisfy conservation laws that are summarized in $\mathbf { B o x } \ 1 9 . 1 $ . These conservation laws are valuable tools in gravitation theory and relativistic astrophysics,but the derivation of these laws (Chapter 2O) does not compare in priority to topics such as neutron stars and basic cosmology; so most readers will wish to skip it on a first reading of this book.

(continued on page 456)

Conservation laws for total 4-momentum and angular momentum

# Box 19.1 TOTAL MASS-ENERGY, 4-MOMENTUM,AND ANGULAR MOMENTUM OF AN ISOLATED SYSTEM

A. Spacetime is divided into (l） the source's interior;which is surrounded by (2）a strong-field vacuum region; which in turn is surrounded by (3)a weak-field, asymptotically flat, near-zone region;which in turn is surrounded by (4) a weakfield,asymptotically flat, radiation-zone region. This box and this chapter treat only the asymptotically flat regions. The interior and strong-field regions are treated in the next chapter.

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0007_pages_0421-0490/auto/images/e1f9d00071049e96ce67bc7504d49d6b636dd1246c46ceafe34b60d8a83231b9.jpg)

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0007_pages_0421-0490/auto/images/b0e09a5f194ea80bc13687429e2238f5e673afed7cbecbc0d2bef0be1e4a3da9.jpg)

B.The asymptotic rest frame of the source is that global, asymptotically Lorentz frame (coordinates $t , x , y , z )$ in which the distant,“coulomb”part of the source's field is at rest (see diagram). The asymptotic rest frame does not extend into the strong-field region; any such extension of it would necessarily be forced by the curvature into a highly non-Lorentz, curvilinear form. The spatial origin of the asymptotic rest frame is so adjusted that the source is centered on it-i.e., that the distant Newtonian potential is $\phi = - M / ( x ^ { 2 } + y ^ { 2 } +$ $z ^ { 2 } ) ^ { 1 / 2 } + 0 ( 1 / r ^ { 3 } )$ ； i.e., that $\pmb { \phi }$ has no dipole term, $\pmb { D } \cdot \pmb { x } / r ^ { 3 }$ ， such as would originate from an offset of the coordinates.

C. To the source one can attribute a total mass-energy $M ,$ a 4-velocity $\pmb { U }$ a total 4-momentum $\pmb { P } ,$ .and an intrinsic angular momentum vector, S.The 4-vectors $\theta , P ,$ and $\pmb { s }$ reside in the asymptotically flat region of spacetime and can be moved about freely there (negligible curvature $\Longrightarrow$ parallel transport around closed curves does not change $\theta , P ,$ or $\pmb { s }$ ). The source's 4-velocity $\pmb { U }$ is defined to equal the 4-velocity of the asymptotic rest frame ( $U ^ { 0 } = 1$ ， $U = 0$ in rest frame). The total mass-energy $M$ is measured via Kepler's third (“1-2-3") law [equation (l9.8)]. The total 4-momentum is defined by $\pmb { P } \equiv M \pmb { U }$ .The intrinsic angular momentum $\pmb { S }$ is orthogonal to the 4-velocity $\pmb { U }$ ， $\pmb { S } \cdot \pmb { U } = 0$ (so $S ^ { 0 } = 0$ ； $s \neq 0$ in general in asymptotic rest frame); $s$ is measured via gyroscope precession or differential perihelion precession $( \ S ^ { 1 9 . 2 ) }$

In the asymptotic rest frame, with an appropriate choice of gauge (i.e., of ripples in the coordinates),the slight deviations from flat-spacetime geometry are described by the line element

$$
\begin{array} { l } { { d s ^ { 2 } = - \left[ 1 - \displaystyle \frac { 2 M } { r } + \displaystyle \frac { 2 M ^ { 2 } } { r ^ { 2 } } + 0 \left( \displaystyle \frac { 1 } { r ^ { 3 } } \right) \right] d t ^ { 2 } - \left[ 4 \epsilon _ { j k l } S ^ { k } \displaystyle \frac { x ^ { l } } { r ^ { 3 } } + 0 \left( \displaystyle \frac { 1 } { r ^ { 3 } } \right) \right] d t d x ^ { j } } } \\ { { + \left[ \left( 1 + \displaystyle \frac { 2 M } { r } + \displaystyle \frac { 3 M ^ { 2 } } { 2 r ^ { 2 } } \right) \delta _ { j k } + \mathrm { ( g r a v i t a t i o n a l ~ r a d i a t i o n ~ t e r m s ) } \right] d x ^ { j } d x ^ { k } . } } \end{array} \mathrm { ( ) }
$$

D. Conservation of 4-momentum and angular momentum: Suppose that particles fall into a source or are ejected from it; suppose that electromagnetic waves flow in and out; suppose the source emits gravitational waves. All such processes break the source's isolation and can change its total 4- momentum $\pmb { P } ,$ ,its intrinsic angular momentum S, and its asymptotic rest frame. Surround the source with a spherical shell $\textstyle { \mathcal { S } } _ { i }$ ，which is far enough out to be in the asymptotically flat region. Keep this shell always at rest in the source's momentary asymptotic rest frame. By probing the source's gravitational field near $s$ ，measure its 4-momentum $\pmb { P }$ and intrinsic angular momentum $\pmb { s }$ as functions of the shel's proper time $\boldsymbol { \mathsf { \tau } } .$ An analysis given in the next chapter reveals that the 4-momentum is conserved, in the sense that

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0007_pages_0421-0490/auto/images/6bb9d1ea1c003ac1c3941467c4862a80ff9ffbe01b21b83e8a13160f57826325.jpg)  
Interstellar debris falls into a black hole, and gravitational waves emerge.

$$
{ \frac { d P ^ { \alpha } } { d \tau } } = - \int _ { s ^ { - } } T _ { - } ^ { \alpha j } n _ { j } d ( \mathrm { a r e a } ) = { \binom { \mathrm { r a t e ~ a t ~ w h i c h ~ 4 \mathrm { - } m o m e n t u m } } { \mathrm { f l o w s ~ i n w a r d ~ t h r o u g h ~ s h e l l } } } ,
$$

where $\pmb { n }$ is the unit outward normal to $s$ and the integral is performed in the shell's momentary rest frame. In words: the rate at which $^ { 4 }$ -momentum flows through the shell,as measured in the standard special relativistic manner,equals the rate of change ofthe source's gravitationally measured $^ { 4 }$ -momentum. Similarly,the angular momentum is conserved in the sense that

$$
\frac { d S _ { i } } { d \tau } = \mathrm { ~ - ~ } \int _ { S } { ( \epsilon _ { i j k } x ^ { j } T ^ { k t } ) n _ { t } d ( \mathrm { a r e a } ) } = \left( \begin{array} { l } { \mathrm { r a t e ~ a t ~ w h i c h ~ a n g u l a r } } \\ { \mathrm { m o m e n t u m ~ f l o w s ~ i n w a r d } } \\ { \mathrm { t h r o u g h ~ t h e ~ s h e l l } } \end{array} \right) ,
$$

$$
\frac { d S _ { 0 } } { d \tau } = - \frac { d U ^ { \alpha } } { d \tau } S _ { \alpha } = \Big ( { \mathop { \mathrm { c h a n g e ~ r e q u i r e d ~ t o ~ k e e p ~ } } ^ { \mathrm { c h a n g e } } } _ { \mathrm { c } ^ { \prime } \mathrm { e r m i - W a l k e r - t r a n s p o r t ~ l a w } ^ { \mathrm { * } } \mathrm { ; ~ c f . ~ } 8 8 6 \mathrm { . } 5 , ~ 1 3 . 6 } \Big ) .
$$

In these conservation laws $T ^ { \alpha \beta }$ is the total stress-energy tensor at the shell, including contributions from matter, electromagnetic fields, and gravitational waves. The gravitational-wave contribution, called $T ^ { ( G W ) _ { \alpha \beta } }$ , is treated in Chapter 35.

Note: The conservation laws in the form stated above contain fractional errors of order $M / r$ (contributions from “gravitational potential energy” of infalling material),but such errors go to zero in the limit of a very large shell $( r \longrightarrow \infty )$

Note: The formulation of these conservation laws given in the next chapter is moie precise and more rigorous, but less physically enlightening than the one here.

# ExerCiSe 19.3. GRAVITATIONAL FIELD FAR FROM A STATIONARY, FULLY RELATIVISTIC SOURCE

Derive the line element (l9.l3) for the special case of a source that is time-independent $( g _ { \mu \nu , t } = 0 )$ .This can be a difficult problem,if one does not proceed carefully along the following outlined route.(l) lnitially ignore all nonlinearities in the Einstein field equations. The field is weak far from the source.These nonlinearities will be absent from the dominant terms. (2) Calculate the dominant terms using linearized theory in the Lorentz gauge [equations (l8.8)]. (3)ln particular, write the general solution to the vacuum,time-independent wave equation (l8.8b) in the following form involving $n ^ { j } \equiv x ^ { j } / r \equiv$ (unit vector in radial direction):

$$
\begin{array} { r l } & { \overline { { h } } _ { 0 0 } = \frac { A ^ { 0 } } { r } + \frac { B ^ { j } n ^ { j } } { r ^ { 2 } } + 0 \left( \frac { 1 } { r ^ { 3 } } \right) , } \\ & { \overline { { h } } _ { 0 j } = \frac { A ^ { j } } { r } + \frac { B ^ { j k } n ^ { k } } { r ^ { 2 } } + 0 \left( \frac { 1 } { r ^ { 3 } } \right) , } \\ & { \overline { { h } } _ { j k } = \frac { A ^ { j k } } { r } + \frac { B ^ { j k } n ^ { t } } { r ^ { 2 } } + 0 \left( \frac { 1 } { r ^ { 3 } } \right) , } \\ & { A ^ { j k } = A ^ { ( j k ) } , \qquad B ^ { j k i } = B ^ { ( j k ) t } . } \end{array}
$$

(Round brackets denote symmetrization.） (4) Then impose the Lorentz gauge conditions $\overline { { h } } _ { \alpha } { } ^ { \beta } { } _ { , \beta } = 0$ onthis generalsolutionteebyeaing

$$
\begin{array} { c c } { { A ^ { j } = 0 , } } & { { A ^ { j k } = 0 , } } \\ { { } } & { { } } \\ { { B ^ { j k } ( \delta ^ { j k } - 3 n ^ { j } n ^ { k } ) = 0 , } } \\ { { } } & { { } } \\ { { B ^ { j k t } ( \delta ^ { k t } - 3 n ^ { k } n ^ { t } ) = 0 . } } \end{array}
$$

(5）Write $B ^ { j k }$ as the sum of its trace $3 B$ ,its traceless symmetric part $S ^ { j k }$ , and its traceless antisymmetric part (these are its “irreducible parts"):

$$
B ^ { j k } = B \delta ^ { j k } + S ^ { j k } + \epsilon ^ { j k } F ^ { i } , \qquad S ^ { j j } = \cdot 0 ,
$$

Show that any tensor $B ^ { j k }$ can be put into such a form. Then show that the gauge conditions (19.18) imply $S ^ { j k } = 0$ ：(6) Similarly show that any tensor $B ^ { j k \ell }$ that is symmetric on its first two indices can be put into the form

$$
B ^ { j k l } = \delta ^ { j k } { \cal { A } } ^ { \ell } + C ^ { ( j } \delta ^ { k ) \ell } + \epsilon ^ { m \ell ( j } E ^ { k ) m } + S ^ { j k \ell } ,
$$

$$
E ^ { k m } = E ^ { ( k m ) } , \qquad E ^ { k k } = 0 ,
$$

$$
S ^ { j k l } = S ^ { ( j k l ) }
$$

$$
S ^ { j j l } = S ^ { j k k } = S ^ { j k j } = 0 .
$$

Then show that the gauge conditions (l9.18） imply $C ^ { j } = - 2 A ^ { j }$ and $E ^ { k m } = S ^ { j k l } = 0$ (7) Combining all these results,conclude that

$$
\begin{array} { r l } & { \overline { { h } } _ { 0 0 } = \frac { A ^ { 0 } } { r } + \frac { B ^ { j } n ^ { j } } { r ^ { 2 } } + 0 \left( \frac { 1 } { r ^ { 3 } } \right) , } \\ & { \overline { { h } } _ { 0 j } = \frac { \epsilon ^ { j k } n ^ { k } F ^ { i } } { r ^ { 2 } } + \frac { B n ^ { j } } { r ^ { 2 } } + 0 \left( \frac { 1 } { r ^ { 3 } } \right) , } \\ & { \overline { { h } } _ { j k } = \frac { \delta ^ { j k } A ^ { t } n ^ { t } - A ^ { j } n ^ { k } - A ^ { k } n ^ { j } } { r ^ { 2 } } + 0 \left( \frac { 1 } { r ^ { 3 } } \right) . } \end{array}
$$

Then use gauge transformations, which stay within Lorentz gauge, to eliminate $\pmb { B }$ and $A ^ { j }$ from $\overline { { h } } _ { 0 j }$ and $\bar { \bar { h } } _ { j k }$ ；so

$$
\begin{array} { l } { \overline { { h } } _ { 0 0 } = \displaystyle \frac { A ^ { 0 } } { r } + \frac { ( B ^ { j } + A ^ { j } ) n ^ { j } } { r ^ { 2 } } + 0 \left( \frac { 1 } { r ^ { 3 } } \right) , } \\ { \overline { { h } } _ { 0 j } = \frac { \epsilon ^ { j k t } n ^ { k } F ^ { t } } { r ^ { 2 } } + 0 \left( \frac { 1 } { r ^ { 3 } } \right) , } \\ { \overline { { h } } _ { j k } = 0 \left( \frac { 1 } { r ^ { 3 } } \right) . } \end{array}
$$

(8)Translate the origin of coordinates so $x ^ { j } { } _ { \mathrm { n e w } } = x ^ { j } { } _ { \mathrm { o l d } } - ( B ^ { j } + A ^ { j } ) / A ^ { 0 }$ in the new coordinate system $\overline { { h } } _ { \alpha \beta }$ has the same form as (l9.22), but with $B ^ { j } + A ^ { j }$ removed. From the resultant $\check { \overline { { h } } } _ { \alpha \beta }$ ,construct the metric and redefine the constants $A ^ { 0 }$ and $F ^ { t }$ to agree with equation (19.13). (9)All linear terms in the metric are now accounted for. The dominant nonlinear terms must be proportional to the square, $( M / r ) ^ { 2 }$ ,of the dominant linear term. The easiest way to get the proportionality constant is to take the Schwarzschild geometry for a fuly relativistic, static,spherical source [equation (31.l)], by a change of coordinates put it in the form

$$
d s ^ { 2 } = \mathrm { } - \left( \frac { 1 - M / 2 r } { 1 + M / 2 r } \right) ^ { 2 } d t ^ { 2 } + \left( 1 + \frac { M } { 2 r } \right) ^ { 4 } ( d x ^ { 2 } + d y ^ { 2 } + d z ^ { 2 } )
$$

(exercise 25.8), and expand it in powers of $M / r$

# $\$ 19.4$ . MASS AND ANGULAR MOMENTUM OF A CLOSED UNIVERSE

"There are no snakes in Ireland."

Statement of St. Patrick after driving the snakes out of Ireland (legend")

There is no such thing as “the energy (or angular momentum,or charge) of a closed universe,”according to general relativity,and this for a simple reason. To weigh something one needs a platform on which to stand to do the weighing.

To weigh the sun, one measures the periods and semimajor axes of planetary orbits, and applies Kepler's $^ { 6 6 } 1 - 2 - 3 ^ { 3 }$ law, $M = \omega ^ { 2 } a ^ { 3 }$ .To measure the angular momentum, $s ,$ ,of the sun (a task for space technology in the $1 9 7 0 ^ { \circ } { \mathsf { s } }$ or $1 9 8 0 ^ { \circ } { \mathsf { s ! } } )$ , one measures the precession of a gyroscope in a near orbit about the sun, or one examines some other aspect of the “dragging of inertial frames.”To determine the electric charge

For a closed universe the total mass-energy $M$ and angular momentum $\pmb { S }$ are undefined and undefinable

of a body,one surrounds it by a large sphere,evaluates the electric field normal to the surface at each point on this sphere, integrates over the sphere,and applies the theorem of Gauss. But within any closed model universe with the topology of a 3-sphere,a Gaussian 2-sphere that is expanded widely enough from one point finds itself collapsing to nothingness at the antipodal point. Also collapsed to nothingness is the attempt to acquire useful information about the “charge of the universe": the charge is trivially zero.By the same token,every“surface integral" (see details in Chapter 20) to determine mass-energy or angular momentum collapses to nothingness.To make the same point in another way: around a closed universe there is no place to put a test object or gyroscope into Keplerian orbit to determine either any so-called “total mass”or“rest frame”or“4-momentum”or “angular momentum” of the system. These terms are undefined and undefinable.Words, yes; meaning, no.

Not having a defined 4-momentum for a closed universe may seem at first sight disturbing; but it would be far more disturbing to be given four numbers and to be told authoritatively that they represent the components of some purported “total energy-momentum 4-vector of the universe." Components with respect to what local Lorentz frame? At what point? And what about the change in this vector on parallel transport around a closed path leading back to that strangely preferred point? It is a happy salvation from these embarrassments that the issue does not and cannot arise!

Imagine a fan:astically precise measurement of the energy of a $\boldsymbol { \gamma }$ -ray. The experi-menter wishes to know how much this $\gamma$ ray contributes to the total mass-energy of the universe. Having measured its energy in the laboratory,he then corrects it for the negative gravitational energy by which it is bound to the Earth. The result,

$$
E _ { \mathrm { c o r r e c t e d } } = h \nu ( 1 - M _ { \oplus } / R _ { \oplus } ) ,
$$

Asymptotic flatness as the key to the definability of $M$ and $s$

is the energy the photon will have after it climbs out of the Earth's gravitational field.But this is only the first in a long chain ofcorrections for energy losses (redshifts) as the photon climbs out of the gravitational fields of the solar system, the galaxy, the local cluster of galaxies,the supercluster, and then what? These corrections show no sign of converging, unless to $E _ { \mathrm { c o r r e c t e d } } = 0$

Quite in contrast to the charge-energy-angular-momentum facelessness of a closed universe are the atractive possibilities of defining and measuring allthree quantities in any space that is asymptotically flat. One does not have to revolutionize presentday views of cosmology to talk of asymptotically flat space. It is enough to note how smallis the departure from flatness,as measured by the departure of $( - g _ { 0 0 } ) ^ { 1 / 2 }$ from unity,in cases of astronomical or astrophysical interest $( \mathbf { B o x } 1 9 . 2 )$ . Surrounding a region where any dynamics, however complicated, is going on, whenever the geometry is asymptotically flat to some specified degree of precision, then to that degree of precision it makes sense to speak of the total energy-momentum 4-vector of the dynamic region, $\pmb { P } ,$ and its total intrinsic angular momentum, S. Parallel transport of either around any closed curve in the flat region brings it back to its starting point unchanged. Moreover, it makes no difference how enormous are the departures from flatness in the dynamic region (black holes, collapsing stars,intense gravitational waves, etc.); far away the curvature will be weak, and the 4-momentum and angular momentum will reveal themselves by their imprints on the spacetime geometry.

Box 19.2 METRIC CORRECTION TERM NEAR SELECTED HEAVENLY BODIES   

<table><tr><td></td><td>m m</td><td>r</td><td>m =1-(-900)1/2 r</td></tr><tr><td>At shoulder of Venus de Milo</td><td>2 × 10g = 1.5 × 10-23cm</td><td>30cm</td><td>5×10-25</td></tr><tr><td>At surface of Earth</td><td>6× 10²g = 4× 10-1cm</td><td>6.4 × 108cm</td><td>6×10-10</td></tr><tr><td>At Earth&#x27;s distance from sun</td><td>2 × 1033g = 1.5× 10 cm</td><td>1.5 × 1013 cm</td><td>1×10-8</td></tr><tr><td>At sun&#x27;s distance from center of galaxy</td><td>2 × 10+4g = 1.5 × 1016cm</td><td>2.5 × 1022 cm</td><td>6×10-7</td></tr><tr><td>At distance of galaxy from center of Virgo cluster of galaxies</td><td>6×10+7g = 4× 1019 cm</td><td>3 ×1025cm</td><td>1×10-6</td></tr></table>
