# EXERCISES

# Exercise 20.1. FLUX INTEGRAL FOR TOTAL MASS-ENERGY IN LINEARIZED THEORY

Show that the flux integral (20.6) for $P ^ { 0 }$ reduces to (20.7). Then show that, when applied to a nearly Newtonian source [line element (l8.15c)]. it reduces further to the familiar Newtonian fux integral (20.2).

# ExerCise 2O.2. FLUX INTEGRAL FOR ANGULAR MOMENTUM IN LINEARIZED THEORY

Derive the Gaussian flux integral (20.8) for $J ^ { \mu \nu }$ .[Hint: use the field equations (20.5) to show

$$
1 6 { \pi } { x } ^ { \mu } T ^ { \nu 0 } = ( { x } ^ { \mu } { H } ^ { \nu \alpha 0 k } { } _ { , \alpha } { ) } _ { , k } - { H } ^ { \nu j 0 \mu } { } _ { , j } - { H } ^ { \nu 0 0 \mu } { } _ { , 0 } ;
$$

and then use Gausss theorem to evaluate the volume integral of equation (20.8).

ExerCiSe 2O.3. FLUX INTEGRALS FOR AN ARBITRARY STATIONARY SOURCE (a) Use the flux integrals (20.9) to calculate $P ^ { \mu }$ and $J ^ { \mu \nu }$ for an arbitrary stationary source. For the asymptotically flat metric around the source, use (19.13), with the gravitational radiation terms set to zero.   
(b) Verify that the“auxiliary equations”(20.lO) to (20.l2) give the correct answer for this source's total mass-energy $M$ and intrinsic angular momentum $S ^ { \mu }$

# $\$ 20.3$ . VOLUME INTEGRALS FOR 4-MOMENTUM AND ANGULAR MOMENTUM

It is easy,in linearized theory,to convert the surface integrals for $P ^ { \mu }$ and $J ^ { \mu \nu }$ into volume integrals over the source; one can simply trace backward the steps that led to the surface integrals in the first place [equation (20.6)；exercise 20.2]. How, in full general relativity,can one similarly convert from the surface integrals to volume integrals? The answer is rather easy, if one thinks in the right direction. One need only put the full Einstein field equations into the form

The full Einstein field equations in terms of $H ^ { \mu \alpha \nu \beta }$

$$
H ^ { \mu \alpha \nu \beta } { } _ { , \alpha \beta } = 1 6 \pi T _ { \mathrm { e f f } } ^ { \mu \nu }
$$

analogous to equations (20.5) of linearized theory.Here $H ^ { \mu \alpha \nu \beta }$ is to be defined in terms of $h _ { \mu \nu } \equiv g _ { \mu \nu } - \eta _ { \mu \nu }$ by equation (20.3),even deep inside the source where $\lvert h _ { \mu \nu } \rvert$ might be ${ \gtrsim } 1$ .This form of the Einstein equations then permits a conversion of the Gaussian flux integrals into volume integrals, just as in linearized theory:

Volume integrals for 4-momentum and angular momentum in full general relativity

$$
\begin{array} { l } { { P ^ { \mu } = \displaystyle \frac { 1 } { 1 6 \pi } \oint H ^ { \mu \alpha 0 j } { } _ { , \alpha } d ^ { 2 } S _ { j } = \displaystyle \frac { 1 } { 1 6 \pi } \int H ^ { \mu \alpha 0 j } { } _ { , \alpha j } d ^ { 3 } x = \displaystyle \frac { 1 } { 1 6 \pi } \int H ^ { \mu \alpha 0 \beta } { } _ { , \alpha \beta } d ^ { 3 } x ~ } } \\ { { { } } } \\ { { \displaystyle ~ = \int T _ { \mathrm { e f f } } ^ { \mu 0 } d ^ { 3 } x . } } \end{array}
$$

Similarly,

$$
J ^ { \mu \nu } = \int \left( x ^ { \mu } T _ { \mathrm { e f f } } ^ { \nu 0 } - x ^ { \nu } T _ { \mathrm { e f f } } ^ { \mu 0 } \right) d ^ { 3 } x .
$$

[Crucial to the conversion is the use of partial derivatives rather than covariant derivatives in equations (20.14).] In these volume integrals, as throughout the preceeding discusson,thecoordinates must become asymptoticallyLorentz $( g _ { \mu \nu } \to \eta _ { \mu \nu } )$ far from the source.

The form of $T _ { \mathsf { e f f } } ^ { \mu \nu }$ canbecalculatedbyealighat $H ^ { \mu \alpha \nu \beta } { } _ { , \alpha \beta }$ is a linearized approximation to the Einstein curvature tensor (20.5). Define the nonlinear corrections by

$$
1 6 \pi t ^ { \mu \nu } \equiv H ^ { \mu \alpha \nu \beta } , \alpha \beta  - 2 G ^ { \mu \nu } .
$$

$t ^ { \mu \nu }$ ("stress-energy pseudotensor"' defined

(To calculate them in terms of $g _ { \mu \nu }$ or $h _ { \mu \nu } = g _ { \mu \nu } - \eta _ { \mu \nu }$ is straightforward but lengthy. The precise form of these corrections will never be needed in this book.） Then Einstein's equations read

$$
{ H ^ { \mu \alpha \nu \beta } } _ { , \alpha \beta } = 1 6 \pi t ^ { \mu \nu } + 2 G ^ { \mu \nu } = 1 6 \pi ( t ^ { \mu \nu } + T ^ { \mu \nu } ) ,
$$

so that

$$
T _ { \mathsf { e f f } } ^ { \mu \nu } = T ^ { \mu \nu } + t ^ { \mu \nu } .
$$

Te defined

The quantity $t ^ { \mu \nu }$ is sometimes called a“stress-energy pseudotensor for the gravitational field.”The Einstein field equations (20.14) imply, because $H ^ { \mu \alpha \nu \beta } { } _ { , \alpha \beta }$ is antisymmetric in $\pmb { \nu }$ and $\beta$ that

$$
T _ { \mathsf { e f f } , \nu } ^ { \mu \nu } = \left( T ^ { \mu \nu } + t ^ { \mu \nu } \right) _ { , \nu } = 0 .
$$

Conservation law for $T _ { \mathrm { e f f } } ^ { \mu \nu }$

These equations are equivalent to $T ^ { \mu \nu } { } _ { ; \nu } = 0$ ， but they are written with partial derivatives rather than covariant derivatives-a fact that permits conversions back and forth between volume integrals and surface integrals.

All the quantities $H ^ { \mu \alpha \nu \beta }$ ， $T _ { \mathrm { e f f } } ^ { \mu \nu }$ ,and $t ^ { \mu \nu }$ depend for their definition and existence on the choice of coordinates; they have no existence independent of coordinates; they are not components of tensors or of any other geometric object. Correspondingly,the equations (20.14) to (20.19) involving $T _ { \mathrm { e f f } } ^ { \mu \nu }$ and $t ^ { \mu \nu }$ have no geometric, coordinate-free significance; they are not “covariant tensor equations.”There is, nevertheless,adequate invariance under general coordinate transformations to give the values $P ^ { \mu }$ and $J ^ { \mu \nu }$ of the volume integrals (20.15) and (20.16) geometric, coordinate-free significance in the asymptotically flat region far outside the source. Although this invariance is hard to see in the volume integrals themselves,it is clear from the surface-integral forms (20.9) that no coordinate transformation which changes the coordinates only inside some spatially bounded region can influence the values of the integrals. For coordinate changes in the distant, asymptotically flat regions, linearized theory guarantees that under Lorentz transformations the integrals for $P ^ { \mu }$ and $\mathcal { T } ^ { \mu \nu }$ will transform like special relativistic tensors,and that under infinitesimal coordinate transformations (gauge changes） they will be invariant.

Because $t ^ { \mu \nu }$ are not tensor components, they can vanish at a point in one coordinate system but not in another. The resultant ambiguity in defining a localized energy density $t ^ { 0 0 }$ for the gravitational field has a counterpart in ambiguities that exist in

$H ^ { \mu \alpha \nu \beta }$ ： $t ^ { \mu \nu }$ and $\tau _ { \mathrm { e f f } } ^ { \mu \nu }$ are coordinate-dependent objects

Other,equally good versions of $H ^ { \mu \alpha \nu \beta }$ $t ^ { \mu \nu }$ $\tau _ { \mathrm { e f f } } ^ { \mu \nu }$

the formal definition of $t ^ { \mu \nu }$ . It is clear that any quantities $H _ { \mathbf { n e w } } ^ { \mu \alpha \nu \beta }$ which agree with the original $H ^ { \mu \alpha \nu \beta }$ in the asymptotic weak-field region will give the same values as $H ^ { \mu \alpha \nu \beta }$ does for the $P ^ { \mu }$ and $J ^ { \mu \nu }$ surface integrals (20.9). One especially convenient choice has been given by Landau and Lifshitz $( 1 9 6 2 ; \{ \ S 1 0 0 \}$ ,who define

(1） H

$$
H _ { \mathrm { L - L } } ^ { \mu \alpha \nu \beta } = { \mathfrak { g } } ^ { \mu \nu } { \mathfrak { g } } ^ { \alpha \beta } - { \mathfrak { g } } ^ { \alpha \nu } { \mathfrak { g } } ^ { \mu \beta } ,
$$

where ${ \mathfrak { g } } ^ { \mu \nu } \equiv ( - g ) ^ { 1 / 2 } g ^ { \mu \nu }$ . Landau and Lifshitz show that Einstein's equations can be written in the form

$$
H _ { \mathrm { L ^ { - } L } , \alpha \beta } ^ { \mu \alpha \nu , \beta } = 1 6 \pi ( - g ) ( T ^ { \mu \nu } + t _ { \mathrm { L ^ { - } L } } ^ { \mu \nu } ) ,
$$

(2)t

where the Landau-Lifshitz pseudotensor components

$$
\begin{array} { c } { { ( - g ) t _ { \mathrm { L - L } } ^ { \alpha \beta } = \displaystyle \frac { 1 } { 1 6 \pi } \bigg \{ \mathfrak { L } ^ { \alpha \beta } , \mathbb { \Phi } ^ { \lambda \mu } , _ { \mu } - \mathfrak { L } ^ { \alpha \lambda } , \mathbb { A } ^ { \beta \mu } , _ { \mu } + \displaystyle \frac { 1 } { 2 } g ^ { \alpha \beta } g _ { \lambda \mu } \mathbb { S } ^ { \lambda \nu } , _ { \rho } \mathbb { S } ^ { \rho \mu } , _ { \nu } } } \\ { { - \left( g ^ { \alpha \lambda } g _ { \mu \nu } \mathbb { S } ^ { \beta \nu } , _ { \rho } \mathbb { S } ^ { \mu \rho } , _ { \lambda } + g ^ { \beta \lambda } g _ { \mu \nu } \mathbb { S } ^ { \alpha \nu } , _ { \rho } \mathbb { S } ^ { \mu \rho } , _ { \lambda } \right) + g _ { \lambda \mu } g ^ { \nu \rho } \mathbb { S } ^ { \alpha \lambda } , _ { \nu } \mathbb { S } ^ { \beta \mu } , _ { \rho } } } \\ { { + \displaystyle \frac { 1 } { 8 } ( 2 g ^ { \alpha \lambda } g ^ { \beta \mu } - g ^ { \alpha \beta } g ^ { \lambda \mu } ) ( 2 g _ { \nu \rho } g _ { \sigma \tau } - g _ { \rho \sigma } g _ { \nu \tau } ) \mathbb { S } ^ { \nu \tau } , _ { \lambda } \mathbb { S } ^ { \rho \sigma } , _ { \mu } \bigg \} } } \end{array}
$$

are precisely quadratic in the first derivatives of the metric. (Einstein also gave a pseudotensor $t _ { E } { } ^ { \mu } { } _ { \nu }$ with this property, but it was not symmetric and so did not lead to an integral for $J ^ { \mu \nu }$ .) Because $H _ { \mathrm { L - L } } ^ { \mu \alpha \nu \beta }$ has the same symmetries as $H ^ { \mu \alpha \nu \beta }$ and equals $H ^ { \mu \alpha \nu \beta }$ far from the source (exercise 20.4),and because the field equations (20.21) in terms of $H _ { \mathrm { L - L } } ^ { \mu \alpha \nu \beta }$ have the same form as in terms of $H ^ { \mu \alpha \nu \beta }$ , it follows that

(3） TL-Left

$$
T _ { \mathrm { L ^ { - } L e f f } } ^ { \mu \nu } \equiv ( - g ) ( T ^ { \mu \nu } + t _ { \mathrm { L ^ { - } L } } ^ { \mu \nu } )
$$

has all the properties of the $T _ { \mathsf { e f f } } ^ { \mu \nu }$ introduced earlier in this section:

$$
T _ { \mathrm { L - L e f f } , \nu } ^ { \mu \nu } = 0 ,
$$

$$
P ^ { \mu } = \int T _ { \mathrm { L - L e f f } } ^ { \mu 0 } d ^ { 3 } x ,
$$

$$
J ^ { \mu \nu } = \int \left( x ^ { \mu } T _ { \mathrm { L - L e f f } } ^ { \nu 0 } - x ^ { \nu } T _ { \mathrm { L - L e f f } } ^ { \mu 0 } \right) d ^ { 3 } x .
$$

# EXERCISE

Exercise 20.4. FORM OF $H _ { \mathrm { L - L } } ^ { \mu \alpha \nu \beta }$ FAR FROM SOURCE   
Show that the entities $H _ { \mathrm { L - L } } ^ { \mu \alpha \nu \beta }$ of equations (20.20) reduce to $H ^ { \mu \alpha \nu \beta }$ (20.3) in the weak-field region far outside the source.

# $\mathfrak { S 2 0 . 4 }$ .WHY THE ENERGY OF THE GRAVITATIONAL FIELD CANNOT BE LOCALIZED

Consider an element of 3-volume $d \Sigma _ { \nu }$ and evaluate the contribution of the“gravitational field” in that element of 3-volume to the energy-momentum 4-vector, using

in the calculation either the pseudotensor $t ^ { \mu \nu }$ or the pseudotensor $t _ { \mathbf { L - L } } ^ { \mu \nu }$ discussed in the last section.Thereby obtain

$$
{ \pmb { p } } = { \pmb e } _ { \mu } t ^ { \mu \nu } d { \pmb { \Sigma } } _ { \nu }
$$

or

$$
\pmb { p } = \pmb { e } _ { \mu } t _ { \mathrm { L - L } } ^ { \mu \nu } d S _ { \nu } .
$$

Right? No,the question is wrong.The motivation is wrong. Theresult is wrong.   
The idea is wrong.

To ask for the amount of electromagnetic energy and momentum in an element of 3-volume makes sense. First, there is one and only one formula for this quantity. Second,and more important, this energy-momentum in principle “has weight.” It curves space. It serves as a source term on the righthand side of Einstein's field equations. It produces a relative geodesic deviation of two nearby world lines that pass through the region of space in question. It is observable. Not one of these properties does “local gravitational energy-momentum” possess. There is no unique formula for it, but a multitude of quite distinct formulas. The two cited are only two among an infinity. Moreover,“local gravitational energy-momentum” has no weight. It does not curve space.It does not serve as a source term on the righthand side of Einstein's field equations. It does not produce any relative geodesic deviation of two nearby world lines that pass through the region of space in question. It is not observable.

Anybody who looks for a magic formula for “local gravitational energy-momentum”is looking for the right answer to the wrong question. Unhappily, enormous time and effort were devoted in the past to trying to “answer this question” before investigators realized the futility of the enterprise.Toward the end,above all mathematical arguments, one came to appreciate the quiet but rock-like strength of Einstein's equivalence principle. One can always find in any given locality a frame ofreference in which all local "gravitational fields"(all Christoffel symbols; all $T ^ { \alpha } { } _ { \mu \nu } )$ disappear. No $\boldsymbol { r }$ 's means no“gravitational field”and no local gravitational field means no “local gravitational energy-momentum.”

Nobody can deny or wants to deny that gravitational forces make a contribution to the mass-energy of a gravitationally interacting system. The mass-energy of the Earth-moon system is less than the mass-energy that the system would have if the two objects were at infinite separation. The mass-energy of a neutron star is less than the mass-energy of the same number of baryons at infinite separation. Surrounding a region of empty space where there is a concentration of gravitational waves, there is a net attraction,betokening a positive net mass-energy in that region of space (see Chapter 35). At issue is not the existence of gravitational energy, but the localizability of gravitational energy. It is not localizable. The equivalence principle forbids.

Look at an old-fashioned potato, replete with warts and bumps. With an orange marking pen, mark on it a“North Pole” and an “equator".The length of the equator is very far from being equal to $\mathfrak { z } _ { \pi }$ times the distance from the North Pole to the

Why one cannot define a localized energy-momentum for the gravitational field

equator. The explanation,“curvature,” is simple, just as the explanation,“gravitation",for the deficit in mass of the earth-moon system (or deficit for the neutron star, or surplus for the region of space occupied by the gravitational waves) is simple. Yet it is not possible to ascribe the deficit in the length of the equator in the one case,or in mass in the other case,in any uniquely right way to different elements of the manifold (2-dimensional in the one case,3-dimensional in the other). Look at a small region on the surface of the potato. The geometry there is locally flat. Look at any small region of space in any of the three gravitating systems. In an appropriate coordinate system it is free of gravitational field. The over-all effect one is looking at is a global effect, not a local effect.That is what the mathematics cries out. That is the lesson of the nonuniqueness of the $t ^ { \mu \nu }$ ！

# \$20.5. CONSERVATION LAWS FOR TOTAL 4-MOMENTUM AND ANGULAR MOMENTUM

Consider a system such as our galaxy or the solar system, which is made up of many gravitating bodies. Some of the bodies may be highly relativistic (black holes; neutron stars),while others are not. However,insist that in the regions between the bodies spacetime be nearly flat (gravity be weak)-so flat, in fact, that one can cover the entire system with coordinates which are (almost) globally inertial, except in a small neighborhood of each body where gravity may be strong.-Such coordinates can exist only if the Newtonian gravitational potential, $\begin{array} { r } { \varPhi \approx \frac { 1 } { 2 } ( \eta _ { 0 0 } - g _ { 0 0 } ) } \end{array}$ ,in the interbody region is small:

$$
\phi _ { \mathrm { i n t e r b o d y } } \sim \mathrm { ( M a s s ~ o f ~ s y s t e m ) / ( r a d i u s ~ o f ~ s y s t e m ) } \ll 1 .
$$

The solar system certainly satisfies this condition $( \Phi _ { \mathrm { i n t e r b o d y } } \sim 1 0 ^ { - 7 } )$ ， as does the Galaxy $( \Phi _ { \mathrm { i n t e r b o d y } } \sim 1 0 ^ { - 6 } )$ ， as do clusters of galaxies $( \Phi _ { \mathrm { i n t e r b o d y } } \sim 1 0 ^ { - 6 } )$ ; but the universe as a whole does not $( \phi _ { \mathrm { i n t e r b o d y } } \sim 1 )$ ！

In evaluating volume integrals for the system's total 4-momentum, split its volume into a region containing each body (denoted $^ { 6 4 } A ^ { 9 9 }$ ）plus an interbody region； and neglect the pseudotensor contribution from the almost-flat interbody region:

Total 4-momentum and angular momentum for a system of gravitating bodies

$$
\begin{array} { r l } & { P _ { \mathrm { s y s t e m } } ^ { \mu } = \displaystyle \sum _ { A } \int _ { A } T _ { \mathrm { e f f } } ^ { \mu 0 } d ^ { 3 } x + \int _ { \mathrm { i n t e r b o d y } } T _ { \mathrm { e f f } } ^ { \mu 0 } d ^ { 3 } x } \\ & { \quad \quad \quad = \displaystyle \sum _ { A } P _ { A } ^ { \mu } + \int _ { \mathrm { i n t e r b o d y } } T ^ { \mu 0 } d ^ { 3 } x . } \end{array}
$$

Because spacetime is asymptotically flat around each body, $P _ { A } { } ^ { \mu }$ is the 4-momentum of body $\pmb { A }$ as measured gravitationally by an experimenter near it. The integral of $T ^ { \mu 0 }$ over the interbody region is the contribution of any gas, particles,or magnetic

fields out there to the total 4-momentum. A similar breakup of the angular momentum reads

$$
J _ { \mathrm { \tiny ~ s y s t e m } } ^ { \mu \nu } = \sum _ { \cal A } J _ { \cal A } ^ { \mu \nu } + \int _ { \mathrm { i n t e r b o d y } } \left( x ^ { \mu } { \cal T } ^ { \nu 0 } - x ^ { \nu } { \cal T } ^ { \mu 0 } \right) d ^ { 3 } x .
$$

In operational terms, these breakups show that the total $^ { 4 }$ momentum and angular momentum of the system, as measured gravitationally by an experimenter outside it, are sums of $P ^ { \mu }$ and $J ^ { \mu \nu }$ for each individual body， as measured gravitationally by an experimenter near it, plus contributions of the usual special-relativistic type from the interbody matter and felds.This is true even ifsome of the bodies are hurtling through the system with speeds near that of light; their gravitationally measured $P ^ { \mu }$ and $J ^ { \mu \nu }$ contribute,on an equal footing with anyone else's, to the system's total $P ^ { \mu }$ and $J ^ { \mu \nu }$

Surround this asymptotically flat system by a two-dimensional surface $\mathcal { S }$ that is at rest in some asymptotic Lorentz frame. Then the 4-momentum and angular momentum inside $\mathcal { S }$ change at a rate (as measured in $\mathcal { S } \mathbf { \hat { s } }$ rest frame) given by

$$
\begin{array} { l } { { \displaystyle { \frac { d P ^ { \mu } } { d t } = \frac { d } { d t } \int T _ { \mathrm { e f f } } ^ { \mu 0 } d ^ { 3 } x = \int T _ { \mathrm { e f f , 0 } } ^ { \mu 0 } d ^ { 3 } x = - \int T _ { \mathrm { e f f , j } } ^ { \mu j } d ^ { 3 } x } } } \\ { { \displaystyle ~ = - \oint T _ { \mathrm { e f f } } ^ { \mu j } d ^ { 2 } S _ { j } , } } \end{array}
$$

Rates of change of total 4-momentum and angular momentum:

(1)expressed as flux integrals ofT

and similarly

$$
{ \frac { d J ^ { \mu \nu } } { d t } } = - \oint _ { S _ { 2 } } ( x ^ { \mu } T _ { \mathrm { e f f } } ^ { \nu j } - x ^ { \nu } T _ { \mathrm { e f f } } ^ { \mu j } ) d ^ { 2 } S _ { j } .
$$

Although the pseudotensor $t ^ { \mu \nu }$ , in the interbody region and outside the system, contributes negligibly to the total 4-momentum and angular momentum (by assumption), its contribution via gravitational waves to the time derivatives $d P ^ { \mu } / d t$ and $d J ^ { \mu \nu } / d t$ can be important when added up over astronomical periods of time. Thus,one must not ignore it in the flux integrals (20.25), (20.26).

In evaluating these flux integrals, it is especially convenient to use the Landau-Lifshitz form of $T _ { \mathrm { e f f } } ^ { \mu \nu }$ , since that form contains no second derivatives of the metric. Thus set

$$
T _ { \mathrm { e f f } } ^ { \mu \nu } = ( - g ) ( T ^ { \mu \nu } + t _ { \mathrm { L \cdot L } } ^ { \mu \nu } ) \approx ( T ^ { \mu \nu } + t _ { \mathrm { L \cdot L } } ^ { \mu \nu } ) ,
$$

where $t _ { \mathrm { L - L } } ^ { \mu \nu }$ are given by equations (20.22). Only those portions of $t _ { \mathrm { L - L } } ^ { \mu \nu }$ that die out as $1 / r ^ { 2 }$ or $1 / r ^ { 3 }$ at large $r$ can contribute to the flux integrals (20.25), (20.26). For static solutions $[ \mathfrak { g } _ { \mu \nu } \sim \mathrm { c o n s t . } + O ( 1 / r ) ] . \ t _ { \mathrm { L } ^ { - } \mathrm { L } } ^ { \mu \nu }$ dies out as $1 / r ^ { 4 }$ . Hence,the only contributions come from dynamic parts of the metric. which,at these large distances, are entirely in the form of gravitational waves. The study of gravitational waves in Chapter 35 will reveal that when $t _ { \mathrm { L - L } } ^ { \mu \nu }$ is averaged over several wavelengths, it becomes a stress-energy tensor $T ^ { ( \mathbf { G W } ) \mu \nu }$ for the waves. which has all the properties one ever requires of any stress-energy tensor. (For example, via Einstein's equations

$G ^ { ( \mathrm { B } ) \mu \nu } = 8 \pi T ^ { ( \mathrm { G W } ) \mu \nu }$ , it contributes to the “background”curvature of the spacetime through which the waves propagate.） Moreover, averaging $t _ { \mathrm { L - L } } ^ { \mu \nu }$ over several wavelengths before evaluating the flux integrals (20.25), (20.26) cannot affect the values of the integrals. Therefore, one can freely make in these integrals the replacement

$$
T _ { \mathsf { e f f } } ^ { \mu \nu } = T ^ { \mu \nu } + T ^ { ( \mathrm { G W } ) \mu \nu } ,
$$

thereby obtaining

(2)expressed as flux integrals of Tuv+T(GW)uv

$$
- \frac { d P ^ { \mu } } { d t } = \oint _ { s } \ \left( T ^ { \mu j } + \ T ^ { ( \mathrm { G W } ) \mu j } \right) d ^ { 2 } S _ { j } ,
$$

$$
- \frac { d J ^ { \mu \nu } } { d t } = \oint _ { \cal { S } } ~ [ x ^ { \mu } ( T ^ { \nu j } + T ^ { ( { \bf G } { \bf W } ) \nu j } ) - x ^ { \nu } ( T ^ { \mu j } + T ^ { ( { \bf G } { \bf W } ) \mu j } ) ] ~ d ^ { 2 } S _ { j } .
$$

These are tensor equations in the asymptotically flat spacetime surrounding the system.All reference to pseudotensors and other nontensorial entities has disappeared.

Equations (20.27) and (20.28) say that the rate of loss of 4-momentum and angular momentum from the system, as measured gravitationally,is precisely equal to the rate at which matter, fields, and gravitational waves carry off 4-momentum and angular momentum.

This theorem is extremely useful in thought experiments where one imagines changing the 4-momentum or angular momentum of a highly relativistic body (e.g, a rotating neutron star) by throwing particles onto it from far away [see, e.g., Hartle (1970)].

# Exercise 2O.5. TOTAL MASS-ENERGY IN NEWTONIAN LIMIT

(a) Calculate $t _ { \mathbf { L } - \mathbf { L } } ^ { \alpha \beta }$ for the nearly Newtonian metric

$$
d s ^ { 2 } = - ( 1 + 2 \phi ) d t ^ { 2 } + ( 1 - 2 \phi ) \delta _ { j k } d x ^ { j } d x ^ { k }
$$

(see $\ S 1 8 . 4 )$ 、Assume the source is slowly changing,so that time derivatives of $\pmb { \phi }$ can be neglected compared to space derivatives. [Answer:

$$
\begin{array} { l } { { \displaystyle t _ { \mathrm { L - L } } ^ { 0 0 } = - \frac { 7 } { 8 \pi } \phi _ { , j } \phi _ { , j } , } } \\ { { } } \\ { { t _ { \mathrm { L - L } } ^ { 0 j } = 0 , } } \\ { { } } \\ { { t _ { \mathrm { L - L } } ^ { j k } = \displaystyle \frac { 1 } { 4 \pi } ( \phi _ { , j } \phi _ { , k } - \frac { 1 } { 2 } \delta _ { j k } \phi _ { , t } \phi _ { , \downarrow } ) . } } \end{array}
$$

(Note: $t _ { \mathrm { L } \cdot \mathrm { L } } ^ { j k }$ as given here is the“stress tensor for a Newtonian gravitational field"; $c f .$ exercises 39.5 and 39.6.)

(b) Let the source of the gravitational field be a perfect fluid with

$$
T ^ { \mu \nu } = ( \rho + p ) u ^ { \mu } u ^ { \nu } + p g ^ { \mu \nu } , \qquad p / \rho \sim \nu ^ { 2 } \equiv ( d x / d t ) ^ { 2 } \sim | \phi | .
$$

Let the Newtonian potential satisfy the source equation

$$
\Phi _ { , j j } = 4 \pi \rho .
$$

Show that the energy of the source is

$$
\begin{array} { r l } & { P ^ { 0 } = \displaystyle \int ( T ^ { 0 0 } + t ^ { 0 0 } ) ( - g ) d ^ { 3 } x } \\ & { \qquad = \displaystyle \int [ \rho / \underbrace { ( 1 - \nu ^ { 2 } ) ^ { 1 / 2 } } _ { \begin{array} { c } { { \Big \mathrm { [ } \mathrm { L i n e t i c } } } \\ { { \Big \mathrm { c o n t r a c t i o n } } } \end{array} } + \underbrace { \frac { 1 } { 2 } \rho \nu ^ { 2 } } _ { \begin{array} { c } { { \Big \mathrm { [ } \mathrm { k i n e t i c } } } \\ { { \Big \mathrm { c n e r g y } } } \end{array} } + \underbrace { \frac { 1 } { 2 } \rho \Phi } _ { \begin{array} { c } { { \Big [ } \mathrm { c r a t e n t i a l } } \\ { { \Big [ \mathrm { e n e r g y } } } \end{array} \Big ] } ^ { \displaystyle { ( g _ { z z } } } ] ^ { \displaystyle { ( g _ { y y } } g _ { z z } ) ^ { 1 / 2 } } d x ~ d y ~ d z \ } \\ { \qquad \displaystyle \Big ] \underset { \begin{array} { c } { { \Big [ } \mathrm { c r o n t i o n e } } \\ { { \Big \mathrm { c o n t r a c t i o n } } } \end{array} \Big ] } ^ { \displaystyle { \Big [ } \mathrm { k i n e t i c } } \Big ] ^ { \displaystyle { \Big ] } } } \end{array}
$$

(c) Show that the “equations of motion" $T _ { \mathrm { L - L e f f } , \nu } ^ { \mu \nu } = 0$ reduce to the standard equations (16.3)of Newtonian hydrodynamics.

# $\$ 20.6$ .EQUATIONS OF MOTION DERIVED FROM THE FIELD EQUATION

Consider the Einstein field equation

$$
{ \pmb { G } } = 8 \pi { \pmb { T } }
$$

under conditions where space is empty of everything except a source-free electromagnetic feld:

$$
T ^ { \mu \nu } = { \frac { 1 } { 4 \pi } } \Big ( F ^ { \mu \alpha } g _ { \alpha \beta } F ^ { \nu \beta } - { \frac { 1 } { 4 } } g ^ { \mu \nu } F _ { \sigma \tau } F ^ { \sigma \tau } \Big )
$$

(cf. the expression for stress-energy tensor of the electromagnetic field in $\ S 5 . 6 \}$ .To predict from (20.31) how the geometry changes with time,one has to know how the electromagnetic field changes with time.The field is expressed as the “exterior derivative” of the 4-potential,

$$
\pmb { F } = d \pmb { A } \ ( \mathrm { l a n g u a g e \ o f \ f o r m s } )
$$

or

$$
F _ { \mu \nu } = \frac { \partial A _ { \nu } } { \partial x ^ { \mu } } - \frac { \partial A _ { \mu } } { \partial x ^ { \nu } } \ ( \mathrm { l a n g u a g e \ o f \ c o m p o n e n t s } ) ,
$$

and the time rate of change of the field is governed by the Maxwellequation

$$
{ \pmb d } ^ { * } { \pmb F } = 0
$$

$$
F ^ { \mu \nu } { } _ { ; \nu } = 0 .
$$

If it seems a fair division of labor for the Maxwell equation to predict the development in time of the Maxwell field and the Einstein equation to do the same for the Einstein field,then it may come as a fresh surprise to discover that the Einstein equation (20.31), plus expression (20.32) for the Maxwell stress-energy, can do both jobs. One does not have to be given the Maxwell “equation of motion”(20.34). One can derive it fresh from (20.31) plus (20.32). The proof proceeds in five steps (see also exercise 3.18 and $\ S 5 . 1 0 )$ . Step one: The Bianchi identity ${ \pmb { \nabla } } \cdot { \pmb { G } } \equiv 0$ implies conservation of energy-momentum $\pmb { \nabla } \cdot \pmb { r } = 0$ ． Step two: Conservation expresses itself in the language of components in the form

$$
\begin{array} { c } { { 0 = 8 \pi ^ { \mu \nu } { } _ { ; \nu } = 2 F ^ { \mu \alpha } { } _ { ; \nu } g _ { \alpha \beta } F ^ { \nu \beta } + 2 F ^ { \mu \alpha } g _ { \alpha \beta } F ^ { \nu \beta } { } _ { ; \nu } } } \\ { { - g ^ { \mu \nu } F _ { \sigma \tau ; \nu } F ^ { \sigma \tau } . } } \end{array}
$$

Step three: Leaving the middle term unchanged,rearrange the first term so that, like the last term,it carries a factor $F _ { . } ^ { \sigma \tau }$ .Thus in that frst term let the indices $\nu \beta$ of $F ^ { \prime \prime \beta }$ be replaced in turn by $\sigma \tau$ and by $\boldsymbol { \tau } \sigma$ ,to subdivide that term into

$$
\begin{array} { r l } {  { F ^ { \mu \alpha } { } _ { ; \sigma } g _ { \alpha \tau } F ^ { \sigma \tau } + F ^ { \mu \alpha } { } _ { ; \tau } g _ { \alpha \sigma } F ^ { \tau \sigma } } } \\ & { = ( F ^ { \mu } { } _ { \tau ; \sigma } - F ^ { \mu } { } _ { \sigma ; \tau } ) F ^ { \sigma \tau } } \\ & { = g ^ { \mu \nu } ( F _ { \nu \tau ; \sigma } + F _ { \sigma \nu ; \tau } ) F ^ { \sigma \tau } . } \end{array}
$$

Step four: Combine the first and the last terms in (20.35) to give

$$
g ^ { \mu \nu } ( F _ { \nu \tau ; \sigma } + F _ { \sigma \nu ; \tau } + F _ { \tau \sigma ; \nu } ) F ^ { \sigma \tau } .
$$

The indices on the derivatives of the field quantities stand in cyclic order. This circumstanceanulsallthetes inthecoectiococients $\Gamma ^ { \alpha } { } _ { \beta \gamma }$ when one writes out the covariant derivatives explicitly.Thus one can replace the covariant derivatives by ordinary derivatives. Moreover, these three derivatives annul one another identically when one substitutes for the fields their expressions (20.33) in terms of the potentials. Consequently, nothing remains in the conservation law (20.35） except the middle term,giving rise to four statements $( \mu = 0 , 1 , 2 , 3 )$

$$
F ^ { \mu } { } _ { \beta } F ^ { \beta \nu } { } _ { ; \nu } = 0
$$

about the four quantities $( \beta = 0 , 1 , 2 , 3 )$

$$
F ^ { \beta \nu } { } _ { ; \nu } .
$$

Step five: The determinant of the coeffcients in the four equations (20.38) for the four unknowns (20.39) has the value

$$
\left| \begin{array} { l } { { F ^ { 0 } { } _ { 0 } F ^ { 0 } { } _ { 1 } F ^ { 0 } { } _ { 2 } F ^ { 0 } { } _ { 3 } } } \\ { { \ldots \ldots \ldots \ldots \ldots } } \\ { { \ldots \ldots \ldots \ldots \ldots } } \\ { { F ^ { 3 } { } _ { 0 } F ^ { 3 } { } _ { 1 } F ^ { 3 } { } _ { 2 } F ^ { 3 } { } _ { 3 } } } \end{array} \right| = - ( { \pmb E } \cdot { \pmb B } ) ^ { 2 }
$$

(see exercise 20.6, part i). In the generic case, this one function of the four variables $( t , x , y , z )$ vanishes on one or more hypersurfaces; but off any such hypersurface (i.e.,at “normal points”in spacetime) it differs from zero.At all normal points, the solution of the four linear equations (20.38) with their nonvanishing determinant gives identically zero for the four unknowns (20.39)； that is to say，Maxwell's “equations of motion”

$$
F ^ { \beta \nu } { } _ { ; \nu } = 0
$$

are fulfilled and must be fulfilled as a straight consequence of Einstein's field equation (20.31)-plus expression 20.32 for the stress-energy tensor. Special cases admit counterexamples (see exercise 20.8); but in the generic case one need not invoke Maxwel's equations of motion; one can deduce them from the Einstein field equation.

Turn from the dynamics of the Maxwell field itself to the dynamics of a charged particle moving under the influence of the Maxwell field. Make no more appeal to outside providence for the Lorentz equation of motion than for the Maxwell equation of motion. Instead, to generate the Lorentz equation call once more on the Einstein field equation or, more directly,on its consequence,the principle of the local conservation of energy-momentum.

Keep track of the world line of the particle from $t = t$ to $t = t + \Delta t$ (Figure 20.1). Generate a “world tube”around this world line. Thus,at each value of the time coordinate t, take the location of the particle as center; construct a sphere of radius e around this center; and note how the successive spheres sweep out the desired world tube. Construct“caps” on this tube at times $t$ and $t + \Delta t$ .The two caps, together with the world tube proper, bound a region of spacetime in which energy and momentum can be' neither created nor destroyed ("no creation of moment of rotation,” in the language of the Bianchi identities,Chapter 15).Therefore the energy-momentum emerging out of the “top” cap has to equal the energy-momen-tum entering the “bottom” cap, supplemented by the amount of energy-momentum carried in across the world-tube by the Maxwell field. Out of such an analysis, as performed in flat spacetime, one ends up with the Lorentz equation of motion in its elementary form (see Chapters 3 and 4),

Lorentz force equation derived from the Einstein field equation

![](images/8b058fc1bf1e50a716fab876294b79e4e81d0b1dee2ec9616b31402420d962cf.jpg)  
Figure 20.1. “World tube." The change in the 4-momentum of the particle is governed by the flow of 4-momentum across the boundary of the world tube.

$$
d \pmb { p } / d \tau = e \langle \pmb { F } , \pmb { u } \rangle
$$

(language of forms)

or in curved spacetime, the Lorentz equation of motion in covariant form,

$$
\nabla _ { u } p = m \nabla _ { u } u = e \langle F , u \rangle
$$

or

$$
m \biggl [ { \frac { d ^ { 2 } x ^ { \alpha } } { d \tau ^ { 2 } } } + \Gamma ^ { \alpha } { } _ { \mu \nu } { \frac { d x ^ { \mu } } { d \tau } } { \frac { d x ^ { \nu } } { d \tau } } \biggr ] = e F ^ { \alpha } { } _ { \beta } { \frac { d x ^ { \beta } } { d \tau } }
$$

A particle acted on by its own electromagnetic field ("radiation damping")

“One ends up with the Lorentz equation of motion”-but only after hurdling problems of principle along the way. One would understand what a particle is if one understood how to do the calculation of balance of energy-momentum with all rigor! Few calculations in all of physics have been done in so many ways by so many leading investigators, from Lorentz and his predecessors to Dirac and Rohrlich [see Teitelboim (1970,l971) for still further insights]. Among the issues that develop are two that never cease to compel attention. (l) The particle responds according to the Lorentz force law (20.41) to a field. This field is the sum of a contribution from external sources and from the particle itself. How is the field exerted by the particle on itself to be calculated? Insofar as it is not already included in its effects in the “experimental mass” $m$ in (20.41), this force is to be calculated as half the difference between the retarded field and the advanced field caused by that particle (see $\ S 3 6 . 1 1$ for a more detailed discussion of the corresponding point for an emitter of gravitational radiation). This difference is singularity-free. On the world line, it has the following simple value [valid in general for point particles; valid for finite-sized particles when and only when the particle changes its velocity negligibly compared to the speed of light during the light-travel time across itselfsee,e.g., Burke (1970)]

$$
{ \frac { 1 } { 2 } } ( F _ { \mathrm { r e t } } - F _ { \mathrm { a d v } } ) ^ { \mu \nu } = { \frac { 2 e } { 3 } } \bigg ( { \frac { d x ^ { \mu } } { d \tau } } { \frac { d ^ { 3 } x ^ { \nu } } { d \tau ^ { 3 } } } - { \frac { d ^ { 3 } x ^ { \mu } } { d \tau ^ { 3 } } } { \frac { d x ^ { \nu } } { d \tau } } \bigg ) .
$$

Infinite self-energy of a point particle

Every acceptable line of reasoning has always led to expression (20.42). It also represents the field required to reproduce the long-known and thoroughly tested law of radiation damping. (2)“Infinite self-energy.” Around a particle at rest, or close to a particle in an arbitrary state of motion, the field is $e / r ^ { 2 }$ and the field energy is

$$
( 1 / 8 \pi ) \int _ { \tau _ { \mathrm { m i n } } } ^ { \epsilon } ( e / r ^ { 2 } ) ^ { 2 } 4 \pi r ^ { 2 } d r = ( e ^ { 2 } / 2 ) ( r _ { \mathrm { m i n } } ^ { - 1 } - \epsilon ^ { - 1 } ) .
$$

This expression diverges as $r _ { \mathrm { m i n } }$ is allowed to go to zero. To hurdle this difficulty, one arranges the calculation of energy balance in such a way that there always appears the sum of this “self-energy”and the“bare mas.”The two terms individually are envisaged as “going to infinity"as $r _ { \mathrm { m i n } } \mathtt { g o e s }$ to zero; but the sum is identified with the“experimental mass”and is required to remain finite. Of course, no particle is a classical object.A proper calculation of the energy has to be conducted at the quantum level. There it is easier to hide from sight the separate infinities-but they are still present, and promise to remain until the structure of a particle is understood.

Before one turns from the Maxwell and Lorentz equations of motion to a final example (deriving the geodesic equations of motion for an uncharged particle), is it not time to object to the whole program of “deriving an equation of motion from Einstein's field equation"? First, is it not a pretensious parade of pomposity to say it comes “from Einstein's field equation”(and even more,“from Einstein's field equations") when it really comes from a principle so elementary and long established as the law of conservation of 4-momentum? It cannot be contested that this conservation principle,in historical fact, came before geometrodynamics, just as it came before electrodynamics and before the theories of all other established fields.However, in no theory but Einstein's is this principle incorporated as an identity. Only here does the conservation of energy-momentum appear as a fully automatic consequence of the inner working of the machinery of the world (energy density tied to moment of rotation, and moment of rotation automatically conserved; see Chapter 17). Out of Einstein's theory one can derive the equation of motion of a particle. Out of Maxwell's one cannot. Thus, nothing prevents one from acting on a charge with an “external” force, over and above the Lorentz force, nor from tailoring this force in such a way that the charge follows some prescribed world line ("enginedriven source"). It makes no difficulties whatsoever for Maxwel's equations that one has shifted attention from a world line that follows the Lorentz equation of motion to one that does not. Quite the contrary is true in general relativity. To shift from right world line (geodesic) to wrong world line makes the difference between satisfying Einstein's field equation in the vicinity of that world line and being unable to satisfy Einstein's field equation.

The Maxwell field equations are so constructed that they automatically fulfill and demand the conservation of charge; but not everything has charge. The Einstein field equation is so constructed that it automatically fulfills and demands the conser-vation of momentum-energy; and everything does have energy. The Maxwell field equations are indifferent to the interposition of an “external” force, because that force in no way threatens the principle of conservation of charge. The Einstein field equation cares about every force, because every force is a medium for the exchange of energy.

Electromagnetism has the motto,“I count all the electric charge that's here.” All that bears no charge escapes its gaze.

“I weigh allthat's here” is the motto of spacetime curvature. No physical entity escapes this surveillance.

Why, then, is the derivation of the geodesic equation of motion of an object said to be based on “Einstein's geometrodynamic field equation” rather than on “the principle of conservation of 4-momentum"? Because geometry responds by its curvature to mass-energy in every form. Most of all, because geometry outside tells about mass-energy inside,free of all concern about issues of internal structure (violent motions, unknown forces, tortuously curved and even multiply-connected geometry).

If one objection to the plan to derive the equation of motion of a particle “from the field equation”has been disposed of, then the moment has come to deal with

How one can avoid complexities of particle structure when deriving equations of motion: the "external viewpoint

the other natural objection: Is there not an inner contradiction in trying to apply to a“particle” (implying idealization to a point） a field equation that deals with the continuum? Answer: There is a contradiction in dealing with a point. Therefore do not deal with.a point. Do not deal with internal structure at all. Analyze the motion by looking at the geometry outside the object. That geometry provides all the handle one needs to follow the motion.

Already here one sees the difference from the derivation of the Lorentz equation of motion as sketched out above. There (l） no advantage was taken of geometry outside as indicator of motion inside; (2) a detailed bookkeeping was envisaged of the localization in space of the electromagnetic energy;and (3) this bookkeeping brought up the issue of the internal structure of the particle,which could not be satisfactorily resolved.

Derivation of geodesic motion from Einstein field equation:

(1）derivation in brief

Now begin the analysis in the new geometrodynamic spirit. Surrounding “the Schwarzschild zone of influence” of the object, mark out a “buffer zone”(Figure 20.2） that extends out to the region where the “background geometry” begins to depart substantially from flatness. Idealize the geometry in the buffer zone as that of an unchanging source merging asymptotically ("boundary $\boldsymbol { \mathcal { B } }$ of buffer zone") into flat space. It suffices to recall the properties of the spacetime geometry far outside an unchanging (i.e., nonradiating) source (exercise l9.3) to draw the key conclusion: relative to this flat spacetime and regardless of its internal structure,the object remains at rest, or continues to move in a straight line at uniform velocity (conservation of total 4-momentum; $\ S 2 0 . 5 )$ . In other words, it obeys the geodesic equation of motion. If this is the result in a flash, then it is appropriate to go back a step to review it, to find out what it means and what it demands.

(2) derivation with care

When the object is absent and the background geometry alone has to be considered, then the geodesic is a wel-defined mathematical construct. Moreover, Fermi-Walker transport along this geodesic gives a well-defined way to construct a comoving local inertial frame (see $\ S 1 3 . 6 )$ .Relative to this frame, the representative point of the geodesic remains for all time at rest at the origin.

Coupling of curvature to particle moments produces deviations from geodesic motion

In what way does the presence of the object change this picture? The object possesses an angular momentum, mass quadrupole moments,and higher multipole moments. They interact with the tide-producing accelerations (Riemann curvature) of the background geometry. Depending on the orientation in space of these moments, the interactions drive the object off its geodesic course in one direction or another (see $\ S 4 0 . 9 )$ .These anomalies in the motion go hand in hand with anomalies in the geometry. On and near the ideal mathematical geodesic the metric is Minkowskian. At a point removed from this geodesic by a displacement with Riemann normal coordinates $\xi ^ { 1 }$ ， $\xi ^ { 2 }$ ， $\xi ^ { 3 }$ (see $\ S 1 1 . 6 )$ ,the metric components differ from their canonical values $( - 1 , 1 , 1 , 1 )$ by amounts proportional (l） to the squares and products of the $\xi ^ { m }$ and (2） to the components of the Riemann curvature tensor (tide-producing acceleration) of the background geometry. These second-order terms produce departures from ideality in the buffer zone,departures that may be described symbolically as of order

$$
\delta ( \mathrm { m e t r i c } ) \sim r ^ { 2 } \cdot R \cdot ( \mathrm { s p h e r i c a l ~ h a r m o n i c ~ o f ~ o r d e r ~ t w o } ) .
$$

![](images/39c4e7080dd0fdc452cd52257442e7d448aaa8de56b829fa345bae78f39f7154.jpg)  
Figure 20.2. “Buffer zone": the shell of space between $\boldsymbol { \mathcal { Q } }$ and $\mathcal { B }$ ，where the geometry is appropriately idealized as the sphericall symmetric“Schwarzschild geometry”of a localized center of attraction (the object under study) in an asymptotically flat space. Inside $\boldsymbol { \mathcal { Q } }$ : the“zone of influence”of the object.In the general case where this object lacks all symmetry,the metric is found to depart more and more from ideal “Schwarzschild character”as the exploration of the geometry is carried inward from $\boldsymbol { \mathcal { Q } }$ (effect of angular momentum of the object on the metric; effect of quadrupole moment; effect of higher moments). Outside B: the“background geometry.”As this geometry is explored at greater and greater distances outside $\Finv$ ,it is found to depart more and more from flatness (effect of concentrations of mass,gravitational waves,and other geometrodynamics).

Here $r$ is the distance from the geodesic and $R$ is the magnitude of the significant components of the curvature tensor. The object produces not only the standard "Schwarzschild” departure from flatness,

which by itself (in a flat background) would bring about no departure from geodesic motion, but also correction terms which may be symbolized as

and

and higher-order terms.Here $S ( \mathsf { c m ^ { 2 } } )$ is a typical component of the angular momentum vector or “spin”; $\pm ( \mathsf { c m } ^ { 3 } )$ is a representative component of the moment of inertia or quadrupole tensor (see Chapter 36 for details),and higher terms have higher-order coefficients.

Coupling of spin to curvature

The tide-producing acceleration generated by the surroundings of the object ("background geometry") acts on the spin of the object with a force of order $R S$ and pulls it away from geodesic motion with an acceleration of the order

$$
\mathsf { a c c e l e r a t i o n ~ ( c m ^ { - 1 } ) } \sim \frac { R ( \mathsf { c m } ^ { - 2 } ) S ( \mathsf { c m } ^ { 2 } ) } { m ( \mathsf { c m } ) }
$$

(see exercise 40.8). Otherwise stated, the surrounding and the spin both put warps in the geometry,and these warps conspire together to push the object off track.

The sum of the relevant two perturbations in the metric is qualitatively of the form

$$
\delta g \sim r ^ { 2 } R + S / r ^ { 2 } .
$$

The sum is least where $r$ has a value of the order

$$
r \sim ( S / R ) ^ { 1 / 4 } ,
$$

and there it has the magnitude

$$
\begin{array} { r } { \delta g \sim ( S R ) ^ { 1 / 2 } . } \end{array}
$$

To “derive the geodesic equation of motion with some preassigned accuracy e" may be defined to mean that the metric in the buffer zone is Minkowskian within the latitude ε. In the ilustrative example, this means that $( S R ) ^ { 1 / 2 }$ is required to be of the order of ε or less Nothing can be done about the value of $\pmb R$ because the background curvature $R$ is a feature of the background geometry. One can meet the requirement only by imposing limits on the mass and moments of the object. In the example, where the dominating moment is the angular momentum,one must require that this parameter of the object be less in order of magnitude than the limit

$$
S \sim \epsilon ^ { 2 } / R . .
$$

Evidently this and similar conditions on the higher moments are most easily satisfied by demanding that the object have spherical symmetry $( S = 0 , \ t = 0$ higher

moments $= 0$ ). Then the perturbation in the metric,again disregarding angle factors and indices, is qualitatively of the form

$$
\delta g \sim r ^ { 2 } R + m / r ,
$$

and the buffer zone is best designed to bracket the minimizing value of $r _ { \star }$

$$
r _ { \bar { G } } \leq [ r \sim ( m / R ) ^ { 1 / 3 } ] \leq r _ { \mathscr { B } } .
$$

The departure of the metric from Minkowskian perfection in the buffer zone is of the order

$$
\begin{array} { r } { \delta g \sim ( m ^ { 2 } R ) ^ { 1 / 3 } . } \end{array}
$$

To achieve any preassigned accuracy $\pmb { \epsilon }$ for $\delta g$ ,one must demand that the mass be less than a limit of the order

$$
m \sim \epsilon ^ { 3 / 2 } / R ^ { 1 / 2 } .
$$

No object of finite mass moving under the influence of a complex background will admit a buffer zone where the geometry approaches Minkowskian values with arbitrary precision. Therefore it is incorrect to say that such an object follows a geodesic world line.It is meaningless to say that an object of finite rest mass follows a geodesic world line. World line of what? If the object is a black hole, there is no point inside its “horizon”(capture surface; one-way membrane； see Chapters 33 and 34) that is relevant to the physics going on outside. Geodesic world line within what background geometry? It has no sense to speak of a geometry that “lies behind" or is“background to”a black hole.

The sense in which no body can move on a geodesic of spacetime

Turn from one motion of one object in one spacetime to a continuous one-parameter family of spacetimes, with the mass m of the object being the parameter that distinguishes one of these solutions of Einstein's field equation from another. Go to the limit $m = 0$ . Then the size of the buffer zone shrinks to zero and the departure of the metric from Minkowskian perfection in the buffer zone also goes to zero. In this limit (test particle"),it makes sense to say that the object moves in a straight line with uniform velocity in the local inertial frame or,otherwise stated, it pursues a geodesic in the background geometry. Moreover, this background geometry is well-defined: it is the limit of the spacetime geometry as the parameter m goes to zero [see Infeld and Schild (l949)]. In this sense, the geodesic equation of motion follows as an inescapable consequence of Einstein's field equation.

The sense in which test particles do move on geodesics of a background geometry

The concept of “background” as limit of a one-parameter family of spacetimes extends itself to the case where the object bears charge as well as mass,and where the surrounding space is endowed with an electromagnetic field. This time the one-parameter family consists of solutions of the combined Einstein-Maxwell equations. The charge-to-mass ratio $e / m$ is fixed.The mass m is again the adjustable parameter.In the limit when $^ m$ goes to zero,one is left with（l） a background geometry,(2) a background electromagnetic field,and (3) a world line that obeys

Motion of a charged test particle in curved spacetime

the general-relativity version of the Lorentz equation of motion in this background as a consequence of the field equations [Chase (l954)]. In contrast,a so-called “unified field theory of gravitation and electromagnetism” that Einstein tentatively put forward at one stage of his thinking,as a conceivable alternative to the combination of his standard 1915 geometrodynamics with Maxwell's standard electrody-namics, has been shown [Callaway (l953)] to lead to the wrong equation of motion for a charged particle. It moves as if uncharged no matter how much charge is piled on its back.If that theory were correct, no cyclotron could operate,no atom could exist,and life itself would be impossible.

References on derivation of equations of motion from Einstein field equation

Thus the ability to yield the correct equation of motion of a particle has today become an added ace in the hand of general relativity. The idea for such a treatment dates back to Einstein and Grommer (1927). Corrections to the geodesic equation of motion arising from interaction between the spin of the object (when it has finite dimensions) and the curvature of the background geometry are treated by Papapetrou (l95l) and more completely by Pirani (l956) (see exercise 40.8). A book on the subject exists [Infeld and Plebanski(l960)]. Section 40.9 describes how corrections to geodesic motion affect lunar and planetary orbits. Some of the problems that arise when the object under study fragments or emits a directional stream of radia-tion,and unresolved issues of principle, are discussed by Wheeler (1961).

When one turns from the limit of infinitesimal mass to an object of finite mass, no simpler situation presents itself then a system of uncharged black holes (Chapter 33). Everything about the motion of these objects follows from an application of the source-free Einstein equation $\pmb { G } = 0$ to the region of spacetime outside the horizons (see Chapter 34) of the several objects. The theory of motion is then geometrodynamics and nothing but geometrodynamics.

Quantum mechanical limitations on the derivation

It has to be emphasized that all the considerations on motion in this section are carried out in the context of classical theory.In the real world of quantum physics, the geometry everywhere experiences unavoidable, natural, zero-point fluctuations (Chapter 43). The calculated local curvatures associated with these fluctuations at the Planck scale of distances $[ L = ( \hbar G / c ^ { 3 } ) ^ { 1 / 2 } = 1 . 6 \times 1 0 ^ { - 3 3 } \mathrm { c m } ]$ are enormous $[ R \sim 1 / L ^ { 2 } \sim 0 . 4 \times 1 0 ^ { 6 6 } \mathrm { c m } ^ { - 2 } ]$ compared to the curvature produced on much larger scales by any familiar object (electron or star).No detailed analysis of the interaction of these two curvatures has ever been made. Such an analysis would define a smoothed-out average of the geometry over regions larger than the local quantum fluctuations. With respect to this average geometry, the object will follow geodesic motion: this is the expectation that no one has ever seen any reason to question-but that no one has proved.

# EXERCISES

# Exercise 20.6. SIMPLE FEATURES OF THE ELECTROMAGNETIC FIELDAND ITS STRESS-ENERGY TENSOR

(a) Show that the “scalar”- $1 / 2 F _ { \alpha \beta } F ^ { \alpha \beta }$ (invariant with respect to coordinate transformations） and the “pseudoscalar” $1 / 4 F _ { \alpha \beta } { } ^ { * } F ^ { \alpha \beta }$ (reproduces itself under a coordinate transformation up to ${ \mathfrak { a } } \pm$ sign,according as the sign of the Jacobian of the transformation is positive

or negative) have in any local inertial frame the values $\pmb { { \cal E } } ^ { 2 } - \pmb { { \cal B } } ^ { 2 }$ and ${ \pmb E } \cdot { \pmb B } .$ ,respectively ("the two Lorentz invariants”of the electromagnetic field).

(b） Show that the Poynting flux $( { \pmb { { \cal E } } } \times { \pmb { { \cal B } } } ) / 4 \pi$ is less in magnitude than the energy density $( E ^ { 2 } + B ^ { 2 } ) / 8 \pi$ ,save for the exceptional case where both Lorentz invariants of the field vanish (case where the field is locally “null").

(c) A charged pith ball is located a small distance from the North Pole of a bar magnet. Draw the pattern of electric and magnetic lines offorce,indicating where the electromagnetic field is“null” in character. Is it legitimate to say that a“null field” is a “radiation field"?

(d) A plane wave is traveling in the $z$ direction. Show that the corresponding electromagnetic feld is everywhere null.

(e) Show that the superposition of two monochromatic plane waves traveling in different directions is null on at most a set of points of measure zero.

(f）In the“generic case”where the field $( E , B )$ at the point of interest is not null, show that the Poynting fux is reduced to zero by viewing the field from a local inertial frame that is traveling in the direction of ${ \pmb E } \times { \pmb B }$ with a velocity

$$
v = \operatorname { t a n h } \alpha ,
$$

where the velocity parameter $\pmb { \alpha }$ is given by the formula

$$
\operatorname { t a n h } 2 \alpha = { \frac { ( { \mathrm { P o y n t i n g ~ f l u x } } ) } { ( { \mathrm { e n e r g y ~ d e n s i t y } } ) } } = { \frac { 2 | E \times B | } { E ^ { 2 } + B ^ { 2 } } } .
$$

(g) Show that all components of the electric and magnetic field in this new frame can be taken to be zero except $E _ { z }$ and $B _ { z }$

(h) Show that the $4 \times 4$ determinant built out of the components of the field in mixed representation, $F _ { \alpha } ^ { \beta }$ ,is invariant with respect to general coordinate transformations. (Hint: Use the theorem that the determinant of the product of three matrices is equal to the product of the determinants of those three matrices.)

(i) Show that this determinant has the value - $( { \pmb { { \cal E } } } \cdot { \pmb { { \cal B } } } ) ^ { 2 }$ by evaluating it in the special local inertial frame of (f).

(j) Show that in this special frame the Maxwell stres-energy tensor has the form

$$
| | T ^ { \mu } { } _ { \nu } | | = \frac { E _ { z } { } ^ { 2 } + B _ { r } { } ^ { 2 } } { 8 \pi } \left| \left| \begin{array} { c c c c } { { - 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { - 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { + 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { + 1 } } \end{array} \right| \right|
$$

(Faraday tension along the lines of force; Faraday pressure at right angles to the lines of force).

$( \mathbf { k } )$ In the other case,where the field is locally null,show that one can always find a local inertial frame in which the feld has the form $\pmb { { \cal E } } = ( 0 , F , 0 ) , \pmb { { \cal B } } = ( 0 , 0 , F )$ and the stress-energy tensor has the value

$$
1 1 T ^ { \mu } { } _ { \nu } ! 1 = { \frac { F ^ { \ast } } { 4 \pi } } \left\| { \begin{array} { l l l l } { - 1 } & { 1 } & { 0 } & { 0 } \\ { - 1 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} } \right\| ( \mu { \mathrm { ~ f o r ~ r o w , ~ } } \nu { \mathrm { ~ f o r ~ c o l u m n } } ) .
$$

(l） Regardless of whether the electromagnetic feld is or is not null, show that the Maxwell stress-energy tensor has zero trace, $T ^ { \mu } { } _ { \mu } = 0$ 、and that its square is a multiple of the unit tensor,

$$
\begin{array} { r l r } & { } & { { T ^ { \mu } } _ { \alpha } T ^ { \alpha } { } _ { \nu } = { \frac { \delta ^ { \mu } { } _ { \nu } } { ( 8 \pi ) ^ { 2 } } } [ ( E ^ { 2 } - B ^ { : 2 } ) ^ { 2 } + ( 2 E \cdot B ) ^ { 2 } ] } \\ & { } & { = { \frac { \delta ^ { \mu } { } _ { \nu } } { ( 8 \pi ) ^ { 2 } } } [ ( E ^ { 2 } + B ^ { : 2 } ) ^ { 2 } - ( 2 E \times B ) ^ { 2 } ] . } \end{array}
$$

# ExerciSe 2O.7. THE STRESS-ENERGY TENSOR DETERMINES THE ELECTROMAGNETIC FIELD EXCEPT FOR ITS COMPLEXION

(a）Given a non-zero symmetric $4 \times 4$ tensor $T ^ { \mu \nu }$ which has zero trace $T ^ { \mu } { } _ { \mu } = 0$ and whose square is a multiple, $M ^ { + } / ( 8 \pi ) ^ { 2 }$ . of the unit matrix,show that, according as this multiple is zero("null case")or positive,the tensor can be transformed to the form (20.60)or (20.59) by a suitable rotation in 3-space or by a suitable choice of local inertial frame,respectively. (b) In the generic (non-null) case in the frame in question,show that $T ^ { \mu \nu }$ is the Maxwell tensor of the “extremal electromagnetic field" $\xi _ { \mu \nu }$ with components

$$
\begin{array} { l } { E ^ { \mathrm { ( e x t r e m a l ) } } = ( M , 0 , 0 ) , } \\ { B ^ { \mathrm { ( e x t r e m a l ) } } = ( 0 , 0 , 0 ) . } \end{array}
$$

Show that it is also the Maxwell tensorof the“dual extremal field" $\ast \xi _ { \mu \nu }$ with components

$$
\begin{array} { c } { { { } ^ { * } E ^ { ( \mathrm { e x t r e m a l } ) } = ( 0 , 0 , 0 ) , } } \\ { { . { } ^ { * } B ^ { ( \mathrm { e x t r e m a l } ) } = ( M , 0 , 0 ) . } } \end{array}
$$

(c) Recaling that the duality operation \*applied twice to an antisymmetric second-rank tensor (2-form) in four-dimensional space leads back to the negative of that tensor, show that the operator $e ^ { * \alpha }$ ("duality rotation") has the value

$$
e ^ { * _ { \alpha } } = ( \cos \alpha ) + ( \sin \alpha ) ^ { * } .
$$

(d) Show that the most general electromagnetic field which will reproduce the non-null tensor $T ^ { \mu \nu }$ in the frame in question, and therefore in any coordinate system,is

$$
F _ { \mu \nu } = e ^ { * _ { \alpha } } \xi _ { \mu \nu } .
$$

(e） Derive a corresponding result for the null case.[The field $F _ { \mu \nu }$ defined in the one frame and therefore in every coordinate system by (d) and (e) is known as the “Maxwell square root”of $T ^ { \mu \nu } \colon \xi _ { \mu \nu }$ is known as the “extremal Maxwell square root” of $T ^ { \mu \nu }$ ； and the angle $\pmb { \alpha }$ is called the “complexion of the electromagnetic field.” See Misner and Wheeler (1957); see also Boxes 20.1 and 20.2,adapted from that paper.]

Box 20.1 CONTRAST BETWEEN PROPER LORENTZ TRANSFORMATIONAND DUALITY ROTATION  

<table><tr><td>Quantity</td><td>General proper Lorentz transformation</td><td>Duality rotation</td></tr><tr><td>Components of the Maxwell stress-energy tensor or the“Maxwell square”of the field F</td><td>Transformed</td><td>Unchanged</td></tr><tr><td>The invariants E²- B² and (E·B)²</td><td>Unchanged</td><td>Transformed</td></tr><tr><td>The combination [(E²- B²)² + (2E·B)²]= [(E²+B²)²-(2E×B)²]</td><td>Unchanged</td><td>Unchanged</td></tr></table>

# Box 20.2 TRANSFORMATION OF THE GENERIC (NON-NULL) ELECTROMAGNETIC FIELD TENSOR $\pmb { F } = \{ \pmb { E } , \pmb { B } \}$ IN A LOCAL INERTIAL FRAME

<table><tr><td></td><td>Field values</td><td>At start</td><td>After simplifying dualityrotation</td></tr><tr><td>At start</td><td></td><td>E,B</td><td>Eand B perpendicular,and E greater than B</td></tr><tr><td>transformation</td><td>After simplifying Lorentz</td><td>E and B parallel to each other and- parallel to x-axis</td><td>E parallel to x-axis and B=0</td></tr></table>

# ExerciSe 2O.8. THE MAXWELL EQUATIONS CANNOT BE DERIVED FROM THE LAW OF CONSERVATION OF STRESS-ENERGY WHEN $\pmb { \left\{ E \cdot B \right\} } = \pmb { 0 }$ OVER AN EXTENDED REGION

Supply a counter-example to the idea that the Maxwell equations,

$$
F ^ { \mu \nu } { } _ { ; \nu } = 0 ,
$$

follow from the Einstein equation; or,more precisely,show that (l) the condition that the Maxwellstress-energy tensor should have a vanishing divergence plus (2) the condition that this Maxwell field is the curl of a 4-potential $A _ { \mu }$ can both be satisfied,while yet the stated Maxwell equations are violated. [Hint: It simplifies the analysis without obscuring the main point to consider the problem in the context of fat spacetime. Refer to the paper of Teitelboim (1970) for the decomposition of the retarded field of an arbitrarily accelerated charge into two parts,of which the second,there called $F ^ { \mu \nu } { } _ { I I } ,$ meets the stated requirements,and has everywhere off the worldline $( { \pmb { { \cal E } } } \cdot { \pmb { { \cal B } } } ) = 0$ ,but does not satisfy the cited Maxwell equations.]

# Exercise 20.9. EQUATION OF MOTION OF A SCALAR FIELD AS CONSEQUENCE OF THE EINSTEIN FIELD EQUATION

The stress-energy tensor of a massless scalar field is taken to be

$$
T _ { \mu \nu } = ( 1 / 4 \pi ) ( \phi _ { , \mu } \phi _ { , \nu } - 1 / 2 g _ { \mu \nu } \phi _ { , \alpha } \phi ^ { , \alpha } ) .
$$

Derive the equation of motion of this scalar field from Einstein's field equation.

# CHAPTER 21

# VARIATIONAL PRINCIPLE AND INITIAL-VALUE DATA

Whenever any action occurs in nature, the quantity of action employed by this change is the least possible.

PIERRE MOREAU DE MAUPERTUIS (1746)

In the theory of gravitation,as in all other branches of theoretical physics,a mathematically correct statement of a problem must be determinate to the extent allowed by the nature of the problem; if possible,it must ensure the uniqueness of its solution.

VLADIMIR ALEXANDROVITCH FOCK (1959)

Things are es they are because they were as they were. THOMAS GOLD (1972)

This chapter is entirely Track 2. No earlier Track-2 material is needed as preparation for it, but Chapters 9-11 and 13-15 will be helpful. It is needed as preparation for Box 30.1 (mixmaster universe) and for Chapters 42 and 43.

No plan for predicting the dynamics of geometry could be at the same time more mistaken and more right than this:“Give the distribution of mass-energy; then solve Einstein's second-order equation,

$$
\pmb { G } = 8 \pi \pmb { T } ,
$$

for the geometry.”Give the distribution of mass-energy in spacetime and solve for the spacetime geometry? No. Give the fields that generate mass-energy, and their time-rates of change, and give 3-geometry of space and its time-rate of change, all at one time,and solve for the 4-geometry of spacetime at that one time? Yes. And only then let one's equations for geometrodynamics and field dynamics go on to predict for all time, in and by themselves,needing no further prescriptions from outside (needing only work!), both the spacetime geometry and the flow of massenergy throughout this spacetime.This,in brief, is the built-in “plan”of geometrodynamics, the plan spelled out in more detail in this chapter.

Contest the plan. Point out that the art of solving any coupled set of equations lies in separating the unknowns from what is known or to be prescribed. Insist that this separation is already made in (21.l). On the right already stands the source of curvature. On the left already stands the receptacle of curvature in the form of what one wants to know,the metric coefficients, twice differentiated. Claim therefore that one has nothing to do except to go ahead and solve these equations for the metric coefficients. However, in analyzing the structure of the equations to greater depth [see Cartan (l922a) for the rationale of analyzing a coupled set of partial differential equations], one discovers that one can only make the split between “the source and the receptacle” in the right way when one has first recognized the still more important split between “the initial-value data and the future.” Thus-to summarize the results before doing the analysis-four of the ten components of Einstein's law connect the curvature of space here and now with the distribution of mass-energy here and now,and the other six equations tell how the geometry as thus determined then proceeds to evolve.

Give initial data,predict geometry

In determining what are appropriate initial-value data to give, one discovers no guide more useful than the Hilbert variational principle,

$$
I = \int { \mathcal { E } } d ^ { 4 } x = \int L ( - g ) ^ { 1 / 2 } d ^ { 4 } x = { \frac { \int L d ( { \mathrm { p r o p e r ~ } } 4 { \mathrm { - v o l u m e } } ) = \mathrm { e x t r e m u m } } { \left\{ { \mathrm { e x e r c i s e ~ } } 8 . 1 6 \right\} } }
$$

or the Arnowitt-Deser-Misner ("ADM") variant of it (S21.6) and generalizations thereof by Kuchar $( \ S 2 1 . 9 )$ .Out of this principle one can recognize most directly what one must hold fixed at the limits (on an initial spacelike hypersurface and on a final spacelike hypersurface) as one varies the geometry (S21.2) throughout the spacetime “filling of this sandwich,” if one is to have a well-defined extremum problem.

The Lagrange function $L$ (scalar function） or the Lagrangian density $\mathcal { L } =$ $( - g ) ^ { 1 / 2 } L$ (quantity to be integrated over coordinate volume) is built of geometry alone,when one deals with curved empty space,but normally fields are present as well,and contribute also to the Lagrangian; thus,

Four of ten components of Einstein equation are conditions on initial-value data

$$
\begin{array} { c } { { \mathcal { L } = \mathcal { L } _ { \mathrm { g e o m } } + \mathcal { L } _ { \mathrm { f i e l d } } = ( - g ) ^ { 1 / 2 } L ; } } \\ { { L = L _ { \mathrm { g e o m } } + L _ { \mathrm { f i e l d } } . } } \end{array}
$$

The variation of the field Lagrangian with respect to the typical metric coefficient proves to be, of all ways, the one most convenient for generating (that is, for calculating) the corresponding component of the symmetric stress-energy tensor of the field (821.3).

New view of stress-energy tensor

A computer, allowing for the efect of this field on the geometry and computing ahead from instant to instant the evolution of the metric with time,imposes its own ordering on the events of spacetime. In effect, it slices spacetime into a great number of spacelike_slices. It finds it most convenient (S2l.4) to do separate bookkeeping on (l) the 3-geometry of the individual slices and (2) the relation between one such slice and the next, as expressed in a “lapse function" $N$ and a 3-vector “shift function” $N _ { i }$

The 3-geometry internal to the individual slice or “simultaneity” defines in and by itself the three-dimensional Riemannian curvature intrinsic to this hypersurface; but for a complete account of this hypersurface one must know also the extrinsic curvature $( \ S 2 1 . 5 )$ teling how this hypersurface is curved with respect to the enveloping four-dimensional spacetime manifold.

In terms of the space-plus-time split of the 4-geometry, the action principle of Hilbert takes a simple and useful form (21.6).

In the most elementary example of the application of an action principle in mechanics, where one writes

$$
I = \int _ { \boldsymbol { x } ^ { \prime } , t ^ { \prime } } ^ { \boldsymbol { x } , t } L ( d \boldsymbol { x } / d t , \boldsymbol { x } , t ) d t
$$

and extremizes the integral, one already knows that the resultant “dynamic path length” or “dynamic phase” or“action,”

$$
S ( x , t ) = I _ { \mathrm { e x t r e m u m } } ,
$$

is an important quantity, not least because it gives (up to a factor $\hbar$ ）the phase of the quantum-mechanical wave function. Moreover, the rate of change of this action function with position is what one calls momentum,

$$
p = \partial S ( x , t ) / \partial x ;
$$

and the (negative of the) rate of change with time gives energy (Figure 21.l),

$$
E = - \partial S ( x , t ) / \partial t ;
$$

and the relation between these two features of a system of wave crests,

$$
E = H ( p , x ) ,
$$

callit “dispersion relation” orcall it what one will,is the central topic of mechanics.

When dealing with the dynamics of geometry in the Arnowitt-Deser-Misner formulation,\* one finds it convenient to think of the specified quantities as being

Figure 21.1.   
Momentum and (the negative of the) energy viewed as rate of change of“dynamic phase”or“action,”

$$
S ( x , t ) = I _ { \mathrm { e x t r e m u m } } ( x , t ) = { \binom { \mathrm { e x t r e m u m } } { \mathrm { v a l u e ~ o f ~ } } } \int _ { x ^ { \prime } , t ^ { \prime } } ^ { x , t } \ L ( x , \dot { x } , t ) \ d t ,
$$

with respect to position and time; thus,

$$
\delta S = p \delta x - E \delta t .
$$

The variation of the integral $\pmb { I }$ with respect to changes of the history along the way, $\delta \boldsymbol { x } ( t )$ ,is already zero by reason of the optimization of the history;so the only change that takes place is

$$
\begin{array} { r l } & { \delta S = \delta I _ { \mathrm { e x t r e m u m } } = L ( x , \dot { x } , t ) \delta t + \displaystyle \int _ { x ^ { \prime } , t ^ { \prime } } ^ { x + \frac { d x } { d t } , \delta } \delta L d t } \\ & { \quad = L \delta t + \displaystyle \int _ { x ^ { \prime } , t ^ { \prime } } ^ { x + \frac { d x } { d t } , t } \left( \frac { \partial L } { \partial \dot { x } } \delta \dot { x } + \frac { \partial L } { \partial x } \delta x \right) d t } \\ & { \quad = L \delta t + \displaystyle \frac { \partial L } { \partial \dot { x } } \varDelta x + \int _ { x ^ { \prime } , t ^ { \prime } } ^ { x + \frac { d x } { d t } , t } \underbrace { \left( \frac { \partial L } { \partial x } - \frac { d } { d t } \frac { \partial L } { \partial \dot { x } } \right) } _ { \mathrm { [ ] } } \delta x d t . } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \left[ \mathrm { z e r o ~ b y ~ r e a s o n ~ } \right] \mathcal { J } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \end{array}
$$

When one contemplates only a change ${ \pmb \delta x }$ in the coordinates $( x , t )$ of the end point (change of history from $\boldsymbol { \mathcal { O } } \boldsymbol { \mathcal { P } }$ to $\mathbf { \mathcal { O } } \boldsymbol { \mathcal { Q } }$ ), one has $\varDelta x = \delta x$ When one makes only a change ${ \delta } t$ in the end point (change of history from $\boldsymbol { \vartheta } \boldsymbol { \vartheta }$ to $\pmb { \mathcal { O } } \pmb { \mathcal { S } }$ ,one has $\pmb { \varDelta x } =$ (indicator of change from $\mathcal { P }$ to $\mathcal { R } ) =$ $- \dot { x } \delta t$ For the general variation of the final point,one thus has $\pmb { 4 } \pmb { x } = \delta \pmb { x } - \dot { \pmb { x } } \ \delta t$ and

![](images/ae4b924416d56411ddf6cdca896f85a9638987981e2ce59a0d55a111013a686d.jpg)

$$
\delta S = \frac { \partial L } { \partial \dot { x } } \delta x - \left( \dot { x } \frac { \partial L } { \partial \dot { x } } - L \right) \delta t .
$$

Oneconcludes that the “dispersion relation” is obtained bytakingtherelations [compare (2)and (4)

$$
{ \left( \begin{array} { l } { \operatorname { r a t e ~ o f ~ c h a n g e ~ o f } } \\ { \operatorname { d y n a m i c ~ p h a s e } } \\ { \operatorname { w i t h ~ p o s i t i o n } } \end{array} \right) } = ( { \mathrm { m o m e n u m } } ) = p = { \frac { { \hat { c } } L ( x , { \dot { x } } , t ) } { { \hat { \mathscr { r } } } { \dot { x } } } }
$$

and

$$
- \left( \mathop { \mathrm { r a t e ~ o f ~ c h a n g e ~ o f } } ^ { \mathrm { r a t e ~ o f ~ c h a n g e ~ o f } } \right) = ( \mathrm { e n e r g y } ) = E = \dot { x } \frac { \hat { c } L } { \hat { c } \hat { x } } - L .
$$

and eliminating $\dot { \boldsymbol { x } }$ from them [solve (5） for $\dot { x }$ and substitute that value of $\dot { x }$ into (6)}; thus

$$
E = H ( p , x , t )
$$

or

$$
- \frac { \partial S } { \partial t } = H \bigg ( \frac { \partial S } { \partial x } , x , t \bigg ) .
$$

Every feature of this elementary analysis has its analog in geometrodynamics.

the 3-geometry $( 3 ) \textcircled { \cdot }$ of the initial spacelike hypersurface and the 3-geometry $( 3 ) \textcircled { \cdot }$ of the final spacelike hypersurface. One envisages the action integral as extremized with respect to the choice of the spacetime that fills the “sandwich” between these two faces. If one has thus determined the spacetime, one has automatically by that very act determined the separation in proper time of the two hypersurfaces. There is no additional time-variable to be brought in or considered. The one concept $( 3 ) g$ thus takes the place in geometrodynamics of the two quantities $x , \ t$ of particle dynamics. The action $s$ that there depended on $x$ and $t$ here depends on the 3-geometry of the face of the sandwich; thus,

# Action viewed as dependent on 3-geometry

$$
S = S ( ^ { 3 ) } \mathcal { Y } ) .
$$

A change in the 3-geometry changes the action. The amount of the change in action per elementarychangein3-geometrydefines the“feld momentum" $\pi _ { \mathrm { t r u e } } ^ { i j }$ conjugate to the geometrodynamic field coordinate $g _ { i j } ,$ ，according to the formula

$$
\delta S = \int \pi _ { \mathrm { t r u e } } ^ { i j } \delta g _ { i j } d ^ { 3 } x .
$$

Comparing this equation out of the Arnowitt,Deser, and Misner (ADM) canonical formulation of geometrodynamics (S21.7) with the expression for change of action with change of endpoint in elementary mechanics,

$$
\delta S = p \delta x - E \delta t ,
$$

one might at first think that something is awry,there being no obvious reference to time in (21.lO). However, the 3-geometry is itself automatically the carrier of information about time; and (21.10) is complete. Moreover, with no“time” variable other than the information that $( 3 ) \textcircled { \times }$ itself already carries about time, there is also no “energy.” Thus the“dispersion relation” that connects the rates of change of action with respect to the several changes that one can make in the“field coordinates” or 3-geometry takes the form

$$
\mathcal { K } ( \pi ^ { i j } , g _ { m n } ) = 0 ,
$$

with the E-term of (21.8) equal to zero (details in $\ S 2 1 . 7 \AA$ . All the content of Einstein's general relativity can be extracted from this one Hamiltonian, or “super-Hamilton-ian,” to give it a more appropriate name [see DeWitt (l967a),pp. 1ll3-11l8, for an account of the contributions of Dirac,of Arnowitt, Deser, and Misner, and of others to the Hamiltonian formulation of geometrodynamics; and see $\ S 2 1 . 7$ and subsequent sections of this chapter for the meaning and payoffs of this formulation].

The difference between a Hamiltonian and a super-Hamiltonian [see,for example, Kramers (l957)] shows nowhere more clearly than in the problem of a charged particle moving in flat space under the influence of the field derived from the electromagnetic 4-potential, $A _ { \mu } ( x ^ { \alpha } )$ .The Hamiltonian treatment derives the equation of motion from the action principle,

$$
0 = \delta I = \delta \int \left[ p _ { i } { \frac { d x ^ { i } } { d t } } - H ( p _ { j } , x ^ { k } , t ) \right] d t
$$

with

$$
H = - { \frac { e } { c } } \phi + \biggl [ m ^ { 2 } + \eta ^ { i j } \biggl ( p _ { i } + { \frac { e } { c } } A _ { i } \biggr ) \biggr ( p _ { j } + { \frac { e } { c } } A _ { j } \biggr ) \biggr ] ^ { 1 / 2 } .
$$

The super-Hamiltonian analysis gets the equations of motion from the action principle

$$
0 = \delta I ^ { \prime } = \delta \int \stackrel { \mathfrak { \sigma } } { \textstyle \left[ p _ { \mu } \right]} \frac { d x ^ { \mu } } { d \lambda } - \mathcal { K } ( p _ { \alpha } , x ^ { \beta } )  d \lambda .
$$

Here the super-Hamiltonian is given by the expression

$$
{ \mathcal { K } } ( p _ { \alpha } , x ^ { \beta } ) = { \frac { 1 } { 2 } } \biggl [ m ^ { 2 } + \eta ^ { \mu \nu } \biggl ( p _ { \mu } + { \frac { e } { c } } A _ { \mu } \biggr ) \biggr ( p _ { \nu } + { \frac { e } { c } } A _ { \nu } \biggr ) \biggr ] .
$$

The variational principle gives Hamilton's equations for the rates of change

$$
d x ^ { \alpha } / d \lambda = \partial \mathcal { K } / \partial p _ { \alpha }
$$

and

$$
d p _ { \beta } / d \lambda = - \partial \mathcal { K } / \partial x ^ { \beta } .
$$

From these equations, one discovers that $\mathcal { K }$ itself must be a constant, independent of the time-like parameter $\lambda$ .The value of this constant has to be imposed as an initial condition, $\mathcal { H } = 0$ ("specification of particle mass"), thereafter maintained by the Hamiltonian equations themselves.This vanishing of $\mathcal { K }$ in no way kills the partial derivatives,

$$
\partial \mathcal { K } / \partial p _ { \alpha } \qquad \mathrm { a n d } \qquad - \partial \mathcal { K } / \partial x ^ { \beta } ,
$$

that enter Hamilton's equations for the rates of change,

$$
d x ^ { \alpha } / d \lambda \qquad \mathrm { a n d } \qquad d p _ { \beta } / d \lambda .
$$

Whether derived in the one formalism or the other,the equations of motion are equivalent, but the covariance shows more clearly in the formalism of the super-Hamiltonian, and similarly in general relativity.

Granted values of the “field coordinates” $g _ { i j } ( x , y , z ) ~ ( ^ { ( 3 ) } \mathcal { Y } )$ and field momenta $\pi _ { \mathrm { t r u e } } ^ { i j } ( x , y , z ) = \delta S / \delta g _ { i j }$ compatible with (21.12), one has what are called “compatible initial-value data on an initial spacelike hypersurface.” One can proceed as described in $\ S 2 1 . 8$ to integrate ahead in time step by step from one spacelike hypersurface to another and another, and construct the whole 4-geometry. Here one is dealing with what in mathematical terminology are hyperbolic differential equations that have the character of a wave equation.

In contrast, one deals with elliptic differential equations that have the character of a Poisson potential equation when one undertakes in the first place to construct the needed initial-value data (S21.9). In the analysis of these elliptic equations, it

Another choice of what to fix at boundary hypersurface: conformal part of 3-geometry plus extrinsic time

proves helpful to distinguish in the 3-geometry between (l） the part of the metric that determines relative lengths at a point, which is to say angles ("the conformal part of the metric") and (2) the common multiplicative factor that enters all the components of the $g _ { i j }$ at a point to determine the absolute scale of lengths at that point. This breakdown of the 3-geometry into two parts provides a particularly simple way to deal with two special initial-value problems known as the time-symmetric and time-antisymmetric initial-value problems (S21.10).

The ADM formalism is today in course of development as summarized in $\ S 2 1 . 1 1$ · In Wheeler's (l968a) “superspace" form, the ADM treatment takes the 3-geometry to be fixed on each of the bounding spacelike hypersurfaces. In contrast, York (821.11） goes back to the original Hilbert action principle,and discovers what it takes to be fixed on each of the bounding spacelike hypersurfaces.The appropriate data turn out to be the “conformal part of the 3-geometry” plus something closely related to what Kuchai (1971a and l972) calls the “extrinsic time.” The contrast between Wheeler's approach and the Kuchar-York approach shows particularly clearly when one(l) deals with a flat spacetime manifold, (2) takes a flat spacelike section through this spacetime,and then (3) introduces a slight bump on this slice, of height e. The 3-geometry intrinsic to this deformed slice differs from Euclidean geometry only to the second order in e. Therefore to read back from the full3-geometry to the time ("the forward advance of the bump"） requires in this case an operation something like extracting a square root. In contrast, the Kuchar-York treatment deals with the“extrinsic curvature” of the slice, something proportional to the first power of e,and therefore provides what is in some ways a more convenient measure of time [see especially Kuchar (197l) for the construction of “extrinsic time” for arbitrarily strong cylindrical gravitational waves; see also Box 30.1 on “time” as variously defined in “mixmaster cosmology"].York shows that the time-variable is most conveniently identified with the variable “dynamically conjugate to the conformal factor in the 3-geometry.”

The initial-value problem of geometrodynamics can be formulated either in the language of Wheeler or in the language of Kuchai and York. In either formulation (821.9 or $\ S 2 1 . 1 1 $ ） it throws light on what one ought properly today to understand by Mach's principle (S21.12). That principle meant to Mach that the“acceleration” dealt with in Newtonian mechanics could have a meaning only if it was acceleration with respect to the fixed stars or to something equally well-defined.It guided Einstein to general relativity. Today it is summarized in the principle that“mass-energy there governs inertia here,” and is given mathematical expression in the initial-value equations.

The analysis of the initial-value problem connected past and future across a spacelike hypersurface. In contrast, one encounters a hypersurface that accommodates a timelike vector when one deals (S21.13) with the junction conditions between one solution of Einstein's field equation (say,the Friedmann geometry interior to a spherical cloud of dust of uniform density) and another (say,the Schwarzschild geometry exterior to this cloud of dust). Section 21.13,and the chapter, terminate with notes on gravitational shock waves and the characteristic initial-value problem (the statement of initial-value data on a light cone,for example).

# \$21.2. THE HILBERT ACTION PRINCIPLE AND THE PALATINI METHOD OF VARIATION

Five days before Einstein presented his geometrodynamic law in its final and now standard form,Hilbert,animated by Einstein's earlier work, independently discovered (1915a) how to formulate this law as the consequence of the simplest action principle of the form (21.2-21.3) that one can imagine:

$$
{ \cal L } _ { \mathrm { g e o m } } = ( 1 / 1 6 \pi ) ^ { ( 4 ) } R .
$$

(Replace $1 / 1 6 \pi$ by $c ^ { 3 } / 1 6 \pi G$ when going from the present geometric units to conventional units;or divide by $\hbar \sim L ^ { * 2 }$ to convert from dynamic phase,with the units of action, to actual phase of a wave function, with the units of radians).Here $^ { ( 4 ) } R$ is the four-dimensional scalar curvature invariant, as spelled out in $\textstyle \mathbf { B o x } ~ 8 . 4$

This action principle contains second derivatives of the metric coefficients. In contrast, the action principle for mechanics contains only first derivatives of the dynamic variables;and similarly only derivatives of the type $\partial A _ { \alpha } ^ { . } / \partial x ^ { \beta }$ appear in the action principle for electrodynamics. Therefore one might also have expected only first derivatives,of the form $\partial g _ { \mu \nu } / \partial x ^ { \gamma }$ ,in the action principle here.However, no scalar invariant lets itself be constructed out of these first derivatives.Thus, to be an invariant, $L _ { \mathbf { g e o m } }$ has to have a value independent of the choice of coordinate system. But in the neighborhood of a point, one can always so choose a coordinate system that all frst derivatives of the $g _ { \mu \nu }$ vanish. Apart from a constant, there is no scalar invariant that can be built homogeneously out of the metric coefficients and their first derivatives.

When one turns from first derivatives to second derivatives, one has all twenty distinct components of the curvature tensor to work with. Expressed in a local inertial frame, these twenty components are arbitrary to the extent of the six parameters of a local Lorentz transformation. There are thus $2 0 - 6 = 1 4$ independent local features of the curvature ("curvature invariants") that are coordinate-independent, any one of which one could imagine employing in the action principle. However, $^ { ( 4 ) } R$ is the only one of these 14 quantities that is linear in the second derivatives of the metric coefficients. Any choice of invariant other than Hilbert's complicates the geometrodynamic law, and destroys the simple correspondence with the Newtonian theory of gravity (Chapter 17).

Scalar curvature invariant the only natural choice

Hilbert originally conceived of the independently adjustable functions of $x , y , z , t$ in the variational principle as being the ten distinct components of the metric tensor in contravariant representation, $g ^ { \mu \nu }$ .Later Palatini (l9l9) discovered a simpler and more instructive listing of the independently adjustable functions: not the ten $g ^ { \mu \nu }$ alone, but the ten $g ^ { \mu \nu }$ plus the forty $\Gamma _ { \mu \nu } ^ { \alpha }$ of the afine connection.

To give up the standard formula for the connection $\boldsymbol { r }$ in terms of the metric $g$ and let $\boldsymbol { r }$ “flap in the breeze” is not a new kind of enterprise in mathematical physics. Even in the simplest problem of mechanics, one can give up the standard formula for the momentum $p$ in terms of a time-derivative of the coordinate $x$ and also let $p$ “flap in the breeze.” Then $x ( t )$ and $p ( t )$ become two independently adjustable functions in a new variational principle,

$$
I = \int _ { x ^ { \prime } , t ^ { \prime } } ^ { x , t } \left[ p ( t ) \frac { d x ( t ) } { d t } - H ( p ( t ) , x ( t ) , t ) \right] d t = \mathrm { e x t r e m u m } .
$$

Happily,out of the extremization with respect to choice of the function $p ( t )$ ，one recovers the standard formula for the momentum in terms of the velocity. The extremization with respect to choice of the other function, $x ( t )$ ，gives the equation of motion just as does the more elementary variational analysis of Euler and Lagrange, where $x ( t )$ is the sole adjustable function.A further analysis of this equivalence between the two kinds of variational principles in particle mechanics appears in Box 21.1.In that box, one also sees the two kinds of variational principle as applied to electrodynamics.

To express the Hilbertvariational principle interms of the $\boldsymbol { \Gamma } _ { \mu \nu } ^ { \lambda }$ and $g ^ { \alpha \beta }$ regarded as the primordial functions of $t , x , y , z$ , note that the Lagrangian density is

$$
{ \cal L } _ { \mathrm { g e o m } } ( - g ) ^ { 1 / 2 } = ( 1 / 1 6 \pi ) ^ { ( 4 ) } R ( - g ) ^ { 1 / 2 } = ( 1 / 1 6 \pi ) g ^ { \alpha \beta } R _ { \alpha \beta } ( - g ) ^ { 1 / 2 } .
$$

Here,as in any spacetime manifold with an affine connection, one has (Chapter 14)

$$
R _ { \alpha \beta } = R ^ { \lambda } { } _ { \alpha \lambda \beta } ,
$$

where

$$
{ R ^ { \lambda } } _ { \alpha \mu \beta } = \partial { \Gamma ^ { \lambda } } _ { \alpha \beta } / \partial x ^ { \mu } - \partial { \Gamma ^ { \lambda } } _ { \alpha \mu } / \partial x ^ { \beta } + { \Gamma _ { \sigma \mu } ^ { \lambda } } { \Gamma _ { \alpha \beta } ^ { \sigma } } - { \Gamma _ { \sigma \beta } ^ { \lambda } } { \Gamma _ { \alpha \mu } ^ { \sigma } } ,
$$

and every $\boldsymbol { r }$ is given in advance (in a coordinate frame) as symmetric in its two lower indices. In order that the integral $\boldsymbol { I }$ of (21.2-21.3) should be an extremum, one requires that the variation in $\pmb { I }$ caused by changes both in the $g ^ { \mu \nu }$ and in the $\boldsymbol { r }$ 's should vanish; thus,

$$
0 = \delta I = ( 1 / 1 6 \pi ) \int \delta [ g ^ { \alpha \beta } R _ { \alpha \beta } ( - g ) ^ { 1 / 2 } ] d ^ { 4 } x + \int \delta [ { \cal L } _ { \mathrm { f i e l d } } ( - g ) ^ { 1 / 2 } ] d ^ { 4 } x .
$$

Consider now the variations of the individual factors in the first and second integrals in (21.18). The variation of the first factor is trivial, $\delta g ^ { \alpha \beta }$ . In the variation of the second factor, $R _ { \alpha \beta }$ , changes in the $g ^ { \alpha \beta }$ play no part; only changes in the $\boldsymbol { r }$ 's appear. Moreover, the variation $\delta { \cal T } _ { \alpha \beta } ^ { \lambda }$ is a tensor even though $\Gamma _ { \alpha \beta } ^ { \lambda }$ itself is not. Thus in the transformation formula

$$
\begin{array} { r } { { \cal { T } } ^ { \overline { { \gamma } } } _ { \overline { { \alpha } } \overline { { \beta } } } = \left[ { \cal { T } } _ { \sigma \tau } ^ { \lambda } \frac { \partial x ^ { \sigma } } { \partial x ^ { \overline { { \alpha } } } } \frac { \partial x ^ { \tau } } { \partial x ^ { \overline { { \beta } } } } + \frac { \partial ^ { 2 } x ^ { \lambda } } { \partial x ^ { \overline { { \alpha } } } \partial x ^ { \overline { { \beta } } } } \right] \frac { \partial x ^ { \widetilde { \gamma } } } { \partial x ^ { \lambda } } , } \end{array}
$$

the last term destroys the tensor character of any set of $\boldsymbol { { \cal T } } _ { \sigma \tau } ^ { \lambda }$ individually,but subtracts out in the difference $\delta { \cal { T } } _ { \pmb { \sigma } \tau } ^ { \lambda }$ between two alternative sets of $\boldsymbol { r }$ 's.Note that the variation $\delta R _ { \alpha \mu \beta } ^ { \lambda }$ of the typical component of the curvature tensor consists of two terms of (continued on page 500)

Box 21.1 RATE OF CHANGE OF ACTION WITH DYNAMIC COORDINATE $\mid =$ "MOMENTUM') AND WITH TIME，AND THE DISPERSION RELATION $\curlyeqsucc$ "HAMILTONIAN" THAT CONNECTS THEM IN PARTICLE MECHANICS AND IN ELECTRODYNAMICS

# A. PROLOG ON THE PARTICLE-MECHANICS ANALOG OF THE PALATINI METHOD

In particle mechanics,one considers the history $x = x ( t )$ to be adjustable between the end points $( x ^ { \prime } , t ^ { \prime } )$ and $( x , t )$ and varies it to extremize the integral $I =$ $\textstyle \int L ( x , { \dot { x } } , t ) d t$ taken between these two limits.

Expressed in terms of coordinates and momenta (see Figure 21.1), the integral has the form

$$
I = \int [ p \dot { x } - H ( p , x , t ) ] d t ,
$$

where $x ( t )$ is again the function to be varied and $p$ is only an abbreviation for a certain function of $x$ and $\dot { x }$ ；thus, $p = \widehat { \boldsymbol { \sigma } } L ( \boldsymbol { x } , \dot { \boldsymbol { x } } , t ) / \widehat { \boldsymbol { \partial } \boldsymbol { x } }$ .Viewed in this way, the variation, $\delta p ( t )$ ,of the momentum is governed by,and is only a reflection of,the variation $\delta x ( t )$

# 1. Momentum Treated as Independently Variable

![](images/d82fffdc6c36c6883011a3e2e7c3128c91331008b980ee79eb4de6909665b9b3.jpg)

There miraculously exists, however, quite another way to view the problem (see inset). One can regard $x ( t )$ and $p ( t )$ as two quite uncorrelated and independently adjustable functions.One abandons the formula $p = \widehat { \vartheta } L ( x , \dot { x } , t ) / \widehat { \vartheta } \dot { x }$ ,only to recover it, or the equivalent of it, from the new “independent-coordinate-and-momentum version” of the variation principle.

The variation of (l),as defined and calculated in this new way, becomes

$$
\delta I = p ~ \delta x ~ \Big | _ { x ^ { \prime } , t ^ { \prime } } ^ { x ^ { \prime \prime } , t ^ { \prime \prime } } + \int _ { x ^ { \prime } , t ^ { \prime } } ^ { x ^ { \prime \prime } , t ^ { \prime \prime } } \Big [ \Big ( \dot { x } - \frac { \partial H } { \partial p } \Big ) \delta p + \Big ( - \dot { p } - \frac { \partial H } { \partial x } \Big ) \delta x \Big ] d t .
$$

Demand that the coefficient of $\delta p$ vanish and have the sought-for new version,

$$
\dot { x } = \frac { \partial H ( p , x , t ) } { \partial p }
$$

of the old relation, $p = \widehat { \vartheta } L ( x , \dot { x } , t ) / \widehat { \vartheta } \dot { x }$ ,between momentum and velocity. The vanishing of the coefficient of $\delta x$ gives the other Hamilton equation,

$$
\dot { p } = - \frac { \partial H ( p , x , t ) } { \partial x } ,
$$

equivalent in content to the original Lagrange equation of motion,

$$
\frac { d } { d t } \frac { \partial L } { \partial \dot { x } } - \frac { \partial L } { \partial x } = 0 .
$$

That $p ( t )$ in this double variable conception is-before the extremization!-a function of time quite separate from and independent of the function $x ( t )$ shows nowhere more clearly than in the circumstance that $p ( t )$ has no end point conditions imposed on it,whereas $x '$ and $x ^ { \prime \prime }$ are specified. Thus not only is the shape of the history subject to adjustment in $x , p ;$ ,t space in the course of achieving the extremum, but even the end points are subject to being slid along the two indicated lines in the inset, like beads on a wire.

# 2. Action as Tool for Finding Dispersion Relation

Denote by $S ( x , t )$ the “action,” or extremal value of $\pmb { I }$ ,for the classical history that starts with $( x ^ { \prime } , t ^ { \prime } )$ and ends at $( x , t ) ( = \hbar$ times phase of de Broglie wave). To change the end points to $( x + \delta x , t )$ makes the change in action

$$
\delta S = p \delta x .
$$

Thus momentum is “rate of change of action with dynamic coordinate."

To change the end point to

$$
( x + \delta x , t + \delta t ) = ( [ x + \dot { x } \delta t ] + [ \delta x - \dot { x } \delta t ] , t + \delta t )
$$

makes the change in action

$$
\delta S = p [ \delta x - \dot { x } \delta t ] + L \delta t = p \delta x - H \delta t .
$$

Thus the Hamiltonian is the negative of “the rate of change of action with time.”

In'terms of the Hamiltonian $H = H ( p , x )$ ,the“dispersion relation” for de Broglie waves becomes

$$
- \ : \frac { \partial S } { \partial t } = H \biggl ( \frac { \partial S } { \partial x } , x \biggr ) .
$$

In the derivation of this dispersion relation, one can profitably short-cut all talk of $p ( t )$ and $x ( t )$ as independently variable quantities,and derive the result in hardly

more than one step from the definition $\textstyle I = \int L ( x , { \dot { x } } , t ) d t .$ Similarly in electrodynamics.

The remainder of this box best follows a first perusal of Chapter 21.

# B. ANALOG OF THE PALATINI METHOD IN ELECTRODYNAMICS

In source-free electrodynamics, one considers as given two spacelike hypersurfaces $s \prime$ and $S ^ { \prime \prime }$ ,and the magnetic fields-as-a-function-of-position in each, $B ^ { \prime }$ and $B ^ { \prime \prime }$ (this second field will later be written without the "superscript to simplify the notation). To be varied is an integral extended over the region of spacetime between the two hypersurfaces,

$$
I _ { \mathrm { M a x w e l l } } \equiv \int { \mathcal E } _ { \mathrm { M a x w e l l } } d ^ { 4 } x = - \frac { 1 } { 1 6 \pi } \int F ^ { \mu \nu } F _ { \mu \nu } ( - g ) ^ { 1 / 2 } d ^ { 4 } x .
$$

# 1. Variation of Field on Hypersurface and Variation of Location of Hypersurface are Cleanly Separated Concepts in Electromagnetism

The electromagnetic field $\pmb { F }$ is the physically relevant quantity in electromagnetism (compare the 3-geometry in geometrodynamics). By contrast, the 4-potential $\pmb { A }$ has no direct physical significance.A change of gauge in the potentials,

$$
{ \cal A } _ { \mu } = { \cal A } _ { \mu _ { \mathrm { n e w } } } + \partial \lambda / \widehat { o } x ^ { \mu }
$$

leaves unchanged the field components

$$
F _ { \mu \nu } = \partial A _ { \nu } / \partial x ^ { \mu } - \partial A _ { \mu } / \partial x ^ { \nu }
$$

(compare the coordinate transformation that changes the $g _ { \mu \nu }$ while leaving unchanged the $( 3 ) \textcircled { \cdot }$ .The variation of the fields within the body of the sandwich is nevertheless expressed most conveniently in terms of the effect of changes $\delta A _ { \mu }$ in the potentials.

One also wants to see how the action integral is influenced by changes in the location of the upper spacelike hypersurface ("many-fingered time"). Think of the point of the hypersurface that is presently endowed with coordinates $x , y , z , t ( x , y , z )$ as being displaced to $x , y , z , t + \delta t ( x , y , z )$ Now renounce this use of a privileged coordinate system. Describe the displacement of the simultaneity in terms of a 4-vector $\delta \pmb { n }$ (not a unit 4-vector) normal to the hypersurface $\pmb { \Sigma }$ The element of 4-volume $\delta \varOmega$ included between the original upper face of the sandwich and the new upper face, that had in the privileged coordinate system the form $( - g ) ^ { 1 / 2 } \delta t ( x , y , z ) d ^ { 3 } x ,$ ,in the notation of Chapter 20 becomes

$$
\delta \varOmega = \delta n ^ { \mu } d ^ { 3 } \varSigma _ { \mu } = ( \delta \pmb { n } \cdot d ^ { 3 } \pmb { \Sigma } ) ,
$$

where the element of surface $d ^ { 3 } \Sigma _ { \mu }$ already includes the previously listed factor $( - g ) ^ { 1 / 2 }$

Counting together the influence of changes in the field values on the upper hypersurface and changes in the location of that hypersurface, one has

$$
\begin{array} { r l r } & { } & { \delta S = \delta I _ { \mathrm { e x t r e m a l } } = - ( 1 / 1 6 \pi ) \displaystyle \int _ { \mathrm { u p p e r } } F ^ { \mu \nu } F _ { \mu \nu } ( \delta n \cdot d ^ { 3 } \Sigma ) \quad } \\ & { } & { + \ : ( 1 / 4 \pi ) \displaystyle \int _ { \mathrm { u p p e r } \atop \mathrm { r e p l a c e ~ b l a c e ~ b y } } F ^ { \mu \nu } \underbrace { A d _ { \mu } } _ { \displaystyle \mathrm { f } } d ^ { 3 } \Sigma _ { \nu } , } \end{array}
$$

Simplify this expresson by arranging the coordinates so that the hypersurface shall be a hypersurface of constant t,and so that lines of constant $x , y , z$ shall be normal to this $\cdot$ hypersurface. Then it follows that the element of volume on that hypersurface contains a single nonvanishing component, $d ^ { 3 } { \mathcal { Z } } _ { 0 } = ( - g ) ^ { 1 / 2 } d ^ { 3 } x$ The antisymmetry of the field quantity $F ^ { 0 \nu }$ in its two indices requires that ${ \pmb \nu }$ be a spacelike label, $i = 1$ ,2,3. The variation of the action becomes

$$
\delta S = \int \left[ \frac { ( - g ) ^ { 1 / 2 } F ^ { \mathrm { i 0 } } } { 4 \pi } \delta { \cal A } _ { i } - \left\{ \underbrace { ( - g ) ^ { 1 / 2 } F ^ { \mathrm { i 0 } } } _ { 4 \pi } { \cal A } _ { i ; 0 } - \mathcal { E } _ { \mathrm { { M a x w e l l } } } \right\} \delta t \right] d ^ { 3 } x .
$$

# 2. Meaning of Field "Momentum" in Electrodynamics

Identify this expression with the quantity

$$
\delta S = \int \pi _ { E M } ^ { i } \delta A _ { i } d ^ { 3 } x - \int \mathcal { K } \delta \varOmega ,
$$

where

$$
\pi _ { E M } ^ { \mathrm { i } } = { \frac { \delta S } { \delta A _ { \mathrm { i } } } } = { \binom { \mathrm { * d e n s i t y ~ o f ~ e l e c t r o m a g n e t i c } } { \mathrm { m o m e n t u m ~ d y n a m i c a l l y ~ c a n o n . } } } = { \frac { ( - g ) ^ { 1 / 2 } F ^ { \mathrm { i 0 } } } { 4 \pi } } = - { \frac { \delta ^ { \mathrm { i } } } { 4 \pi } }
$$

is a simple multiple of the electric field and where

$$
\begin{array} { r l } & { { \mathcal K } = - \frac { { \delta } S } { { \delta } \varOmega } = \left( { \begin{array} { l } { \mathrm { {  ~ \psi ~ } } _ { \mathrm { e l e c t r o m a g n e t i c } } ^ { \mathrm { { \tiny { s * } d e n s i t y ~ o f } } } } \\ { \mathrm { {  ~ \psi ~ } } _ { \mathrm { H a m i l t o n i a n } } ^ { \mathrm { o f } } , } \end{array} } \right) = ( 1 / 1 6 \pi ) [ F ^ { \mu \nu } F _ { \mu \nu } + 4 F ^ { i 0 } ( A _ { i ; 0 } - A _ { 0 ; i } ) ] } \\ & { ~ = ( 1 / 8 \pi ) ( E ^ { 2 } + B ^ { 2 } ) . } \end{array}
$$

The concept of dynamic Hamiltonian density agrees with the usual concept of density of electromagnetic energy，despite the very different context in which the two quantities are derived and used. However,the canonical momentum $\pi _ { E M } ^ { i }$ has nothing directly whatsoever to do with the density of electromagnetic momentum as defined, for example,by the Poynting vector,despite the confusing similarity in the standard names for the two quantities.Note that there is no term $\delta A _ { 0 }$ in (13); that is, $\pi _ { E M } ^ { 0 } \cong 0$

# 3．Bubble Differentiation

The “bubble differentiation” with respect to “many-fingered time”that appears in (l5) was first introduced by Tomonaga (1946). One thinks of a spacelike hypersurface $\Sigma _ { 1 } ,$ a magnetic field $\pmb { B }$ defined as a function of position on this hypersurface (by an observer on a world line normal to this hypersurface),and a prescription $s$ that carries one from this information to a single number, the action. (Divided by $\hbar .$ ，this action gives the phase of the“wave function”or“probability amplitude” for the occurrence of this particular distribution of field values over this particular hypersurface.) One goes to a second hypersurface $\Sigma _ { 2 }$ (see inset), which is identical with $\pmb { \Sigma } _ { 1 } .$ ,except in the immediate vicinity of a given point.Take a distribution of field values over $\Sigma _ { 2 }$ that is identical with the original distribution over $\pmb { \Sigma } _ { 1 }$ ，“identity of location” being defined by means of the normal. Evaluate the difference, $\delta S .$ ，in the value of the dynamic phase or action in the two cases.Divide this difference by the amount of proper 4-volume $\delta \varOmega =$ $\int ( \delta \pmb { n } \cdot d ^ { 3 } \pmb { \Sigma } )$ contained in the“bubble"between the two hypersurfaces. Take the quotient, evaluate it in the limit in which the size of the bubble goes to zero,and in this way get the “bubble-time derivative,” $\delta S / \delta \Omega$ ,of the action.

![](images/798857bb881a64935090d31346420ef456b000cff12ed229ac1926a9bb14de15.jpg)

# Box 21.1 (continued)

What does it mean to say that the action, $s ,$ besides depending on the hypersurface, $\pmb { \Sigma }$ ,depends also on the distribution of the magnetic field, $B .$ ,over that hypersurface? The action depends on the physical quantity, $\pmb { B } = \pmb { \nabla } \times \pmb { A }$ ,not on the prephysical quantity, $\pmb { A }$ .Thus a change in gauge $\delta A _ { i } = \partial \lambda / \partial x ^ { i }$ ,cannot make any change in S. On the other hand,the calculated value of the change in $s$ for this alteration in $\pmb { A }$ is

$$
\begin{array} { r l r } {  { \delta ( \mathrm { a c t i o n } ) = \delta S = \int \frac { \delta S } { \delta A _ { i } } \delta A _ { i } d ^ { 3 } x } } \\ & { } & { = \int \frac { \delta S } { \delta A _ { i } } \frac { \partial \lambda } { \partial x ^ { i } } d ^ { 3 } x = - \int ( \frac { \delta S } { \delta A _ { i } } ) _ { , i } \lambda ( x , y , z ) d ^ { 3 } x . } \end{array}
$$

In order that there shall be no dependence of action on gauge,it follows that this expression must vanish for arbitrary $\lambda ( x , y , z )$ ,a result only possible if $S ( \pmb { \cal { 2 } } , \pmb { \cal { B } } ) =$ S(hypersurface, field on hypersurface) satisfies the identity

$$
\left( \frac { \delta { \cal S } } { \delta A _ { \mathrm { i } } } \right) _ { , i } = \pi _ { E M , i } ^ { i } = - ( 1 / 4 \pi ) \delta ^ { i } { } _ { , i } = 0 .
$$

# 4.Hamilton-Jacobi "Propagation Law" for Electrodynamics

The“dispersion relation”or “Hamilton-Jacobi equation”_for_electromagnetism relates (l) the changes of the“dynamic phase”or “action” brought about by alterations in the dynamic variables $A _ { i }$ (the generalization of the $x$ of particle dynamics) with (2) the changes brought about by alterations in many-fingered time (the generalization of the single time $t$ of particle dynamics)； thus (l5） translates into

$$
- { \frac { \delta S } { \delta \varOmega } } = { \frac { ( 4 \pi ) ^ { 2 } } { 8 \pi } } \biggl ( { \frac { \delta S } { \delta A } } \biggr ) ^ { 2 } + { \frac { 1 } { ( 8 \pi ) } } ( \nabla \times { \boldsymbol { A } } ) ^ { 2 }
$$

# C.DISPERSION RELATIONS FOR GEOMETRODYNAMICS AND ELECTRODYNAMICS COMPARED AND CONTRASTED

Geometrodynamics possesses a direct analog of equation (17) ("action depends on no information carried by the vector potential A except the magnetic field $\pmb { { \cal B } } = \pmb { \nabla } \times \pmb { { \cal A } } ^ { * } ,$ ),in an equation that says the action depends on no information carried by the metric $g _ { i j }$ on the “upper face of the sandwich” except the 3-geometry there, $( 3 ) . 9 .$ It also possesses a direct analog of equation (18)("dynamic equation for the propagation of the action") with this one difference:in electrodynamics the field variable $\pmb { B }$ and the many-fingered time are distinct in character, whereas in geometrodynamics the “field”and the “many-fingered time” can be regarded as two aspects of one and the same $( 3 ) g$ ：

# D. ACTION PRINCIPLE AND DISPERSION RELATION AREROOTED IN THE QUANTUM PRINCIPLE; FEYNMAN'SPRINCIPLE OF THE DEMOCRATIC EQUALITYOF ALL HISTORIES

For more on action principles in physics, see for example Mercier (l953),Lanczos (1970),and Yourgrau and Mandelstam (1968).

Newton (1687) in the first page of the preface to the first edition of his Principia notes that “The description of right lines ...，upon which geometry is founded, belongs to mechanics.Geometry does not teach us to draw these lines,but requires them to be drawn.”

Newton's remark is also a question. Mechanics moves a particle along a straight line, but what is the machinery by which mechanics accomplishes this miracle? The quantum principle gives the answer. The particle moves along the straight line only by not moving along the straight line. In effect it “feels out” every conceivable world line that leads from the start, $( x ^ { \prime } , t ^ { \prime } )$ ,to the point of detection, $( x ^ { \prime \prime } , t ^ { \prime \prime } )$ ,"compares” one with another,and takes the extremal world line.How does it accomplish this miracle?

The particle is governed by a“probability amplitude to transit from $( x ^ { \prime } , t ^ { \prime } )$ to $( x ^ { \prime \prime } , t ^ { \prime \prime } )$ ”This amplitude or “propagator,” $\langle x ^ { \prime \prime } , t ^ { \prime \prime } | x ^ { \prime } , t ^ { \prime } \rangle$ ,is the democratic sum with equal weight of contributions from every world line that leads from start to finish; thus,

$$
\langle x ^ { \prime \prime } , t ^ { \prime \prime } | x ^ { \prime } , t ^ { \prime } \rangle = N \int e ^ { i I _ { H } / \hbar } \langle \vec { \jmath } x .
$$

Here $N$ is a normalization factor, the same for all histories.

$\boldsymbol { \mathbf { \ell } } _ { \mathcal { X } }$ is the “volume element” for the sum over histories. For a“skeleton history” defined by giving $x _ { n }$ at $t _ { n } = t _ { 0 } + n \varDelta t$ ,one has $\boldsymbol { \vartheta x }$ equal,up to a multiplicative constant, to $d x _ { 1 } d x _ { 2 } \ldots . d x _ { N } .$ When the history is defined by the Fourier coefficients in such an expression as

$$
x ( t ) = \frac { x ^ { \prime } ( t ^ { \prime \prime } - t ) + x ^ { \prime \prime } ( t - t ^ { \prime } ) } { ( t ^ { \prime \prime } - t ^ { \prime } ) } + \sum _ { n } a _ { n } \sin n \pi \frac { ( t - t ^ { \prime } ) } { ( t ^ { \prime \prime } - t ^ { \prime } ) } ,
$$

the volume element, again up to a multiplicative factor, is $d a _ { 1 } d a _ { 2 } . . . .$

Destructive interference in effect wipes out the contribution to the transition probability from histories that differ significantly from the “extremal history”or "classical history.”Histories that are near that extremal history,on the other hand, contribute constructively,and for a simple reason: a small departure of the first order from the classical history brings about a change in phase which is only of the second order in the departure.

In this elementary example, one sees illustrated why it is that extremal principles play such a large part in classical dynamics.They remind one that all classical physics rests on a foundation of quantum physics. The central ideas are (l） the principle

# Box 21.1 (continued)

of superposition of probability amplitudes,(2) constructive and destructive interference,(3) the “democracy of all histories,”and (4) the probability amplitude associated with a history $H$ is $e ^ { \mathrm { i } I _ { H } / \hbar }$ ,apart from a normalizing factor that is a multiplicative constant.

For more on the democracy of histories and the sum over histories see Feynman (1942,1948,1949,1951,and 1955),and the book of Feynman and Hibbs (1965); also Hibbs (1951), Morette (1951), Choquard (1955),Polkinghorne (1955),Fujiwara (1962),and the survey and literature references in Kursunoglu (1962);also reports of Dempster (l963) and Symanzik (1963). This outlook has been applied by many workers to discuss the quantum formulation of geometrodynamics, the first being Misner (l957) and one of the latest being Faddeev (1971).

the form $\delta { \cal T } _ { \alpha \beta , \mu } ^ { \lambda }$ and four terms of the form $r \delta { \cal T }$ (indices being dropped for simplicity). One coordinate system is as good as another in dealing with a tensor. Therefore pick a coordinate system in which all the $\boldsymbol { { \cal T } }$ 's vanish at the point under study. The terms $r \delta T$ drop out. In this coordinate system, the variation of the curvature is expressed in terms of first derivatives of quantities like $\delta { \cal T } _ { \alpha \beta } ^ { \lambda }$ . One then need only replace the ordinary derivatives by covariant derivatives to obtain a formula correct in any coordinate system,

$$
\delta R _ { \alpha \mu \beta } ^ { \lambda } = \delta r _ { \alpha \beta ; \mu } ^ { \lambda } - \delta r _ { \alpha \mu ; \beta } ^ { \lambda } ,
$$

along with its contraction,

$$
\delta R _ { \alpha \beta } = \delta T _ { \alpha \beta ; \lambda } ^ { \lambda } - \delta T _ { \alpha \lambda ; \beta } ^ { \lambda } .
$$

The third factor that appears in the variation principle is $( - g ) ^ { 1 / 2 }$ . Its variation (exercise 21.1) is

$$
\delta ( - g ) ^ { 1 / 2 } = - \frac { 1 } { 2 } ( - g ) ^ { 1 / 2 } g _ { \mu \nu } \delta g ^ { \mu \nu } .
$$

The other integrand, the Lagrange density $L _ { \mathrm { f i e l d } } ,$ will depend on the fields present and their derivatives, but will be assumed to contain the metric only as $g ^ { \mu \nu }$ itself, never in the form of any derivatives of $g ^ { \mu \nu }$

In order for an extremum to exist, the following expression has to vanish:

$$
\begin{array} { c } { { ( 1 / 1 6 \pi ) \displaystyle \int \left[ \left( R _ { \alpha \beta } - \frac { 1 } { 2 } g _ { \alpha \beta } R \right) \delta g ^ { \alpha \beta } + g ^ { \alpha \beta } ( \delta r _ { \alpha \beta ; \lambda } ^ { \lambda } - \delta r _ { \alpha \lambda ; \beta } ^ { \lambda } ) \right] ( - g ) ^ { 1 / 2 } d ^ { 4 } x } } \\ { { + \displaystyle \int \left( \frac { \delta { \cal L } _ { \mathtt { f i e l d } } } { \delta g ^ { \alpha \beta } } - \frac { 1 } { 2 } g _ { \alpha \beta } { \cal L } _ { \mathtt { f i e l d } } \right) \delta g ^ { \alpha \beta } ( - g ) ^ { 1 / 2 } d ^ { 4 } x = 0 } } \end{array}
$$

Focus attention on the term in (21.23) that contains the variations of $r$

$$
( 1 / 1 6 \pi ) \int g ^ { \alpha \beta } ( \delta { \cal { T } } _ { \alpha \beta ; \lambda } ^ { \lambda } - \delta { \cal { T } } _ { \alpha \lambda ; \beta } ^ { \lambda } ) ( - g ) ^ { 1 / 2 } d ^ { 4 } x ,
$$

and integrate by parts to eliminate the derivatives of the $\delta { \cal T }$ . To prepare the way for this integration,introduce the concept of tensor density,a notational device widely applied in general relativity.The concept of tensor density aims at economy. Without this concept,one will treat the tensor

$$
\epsilon _ { \mu \alpha \beta \gamma } = ( - g ) ^ { 1 / 2 } [ \mu \alpha \beta \gamma ]
$$

(see exercise 3.13) as having $4 ^ { 4 } = 2 5 6$ components,and its covariant derivative as having $4 ^ { 5 } = 1 { , } 0 2 4$ components,of which one is

$$
\begin{array} { r l } & { \epsilon _ { 0 1 2 3 ; \rho } = \partial ( - g ) ^ { 1 / 2 } / \partial x ^ { \rho } \epsilon _ { \{ 0 1 2 3 \} } - { \Gamma _ { 0 \rho } ^ { \sigma } \epsilon } _ { \sigma 1 2 3 } - { \Gamma _ { 1 \rho } ^ { \sigma } \epsilon } _ { 0 \sigma 2 3 } } \\ & { \quad \quad \quad \quad - { \Gamma _ { 2 \rho } ^ { \sigma } \epsilon } _ { 0 1 \sigma 3 } - { \Gamma _ { 3 \rho } ^ { \sigma } \epsilon } _ { 0 1 2 \sigma } } \\ & { \quad \quad \quad \quad = [ ( - g ) ^ { 1 / 2 } , \rho - { \Gamma _ { \sigma \rho } ^ { \sigma } ( - g ) ^ { 1 / 2 } ] [ 0 1 2 3 ] } . } \end{array}
$$

The symbol $[ \alpha \beta \gamma \delta ]$ ，with values $( 0 , - 1 , + 1 )$ ,introduces what is largely excess baggage,doing mere bookkeeping on alternating indices.Drop this unhandiness. Introduce instead the non-tensor $( - g ) ^ { 1 / 2 }$ and define for it the law of covariant differentiation,

$$
( - g ) ^ { 1 / 2 } { } _ { ; \rho } = ( - g ) ^ { 1 / 2 } { } _ { , \rho } - \Gamma _ { \sigma \rho } ^ { \sigma } ( - g ) ^ { 1 / 2 } .
$$

These four components take the place of the 1,024 components and communicate all the important information that was in them.

Associated with the vector $j _ { \mu }$ is the vector density

$$
\mathfrak { j } _ { \mu } = ( - g ) ^ { 1 / 2 } \dot { \jmath } _ { \mu } ;
$$

with the tensor $T _ { \mu \nu } .$ , the tensor density

$$
{ \mathfrak { T } } _ { \mu \nu } = ( - g ) ^ { 1 / 2 } T _ { \mu \nu } ;
$$

and so on; the German gothic letter is a standard indicator for the presence of the factor $( - g ) ^ { 1 / 2 }$ . On some occasions (see, for example, $\ S 2 1 . 1 1 \rangle$ it is convenient to multiply the components of a tensor with a power of $( - g ) ^ { 1 / 2 }$ other than 1. According to the value of the exponent, the resulting assemblage of components is then called a tensor density of this or that weight.

The law of differentiation of an ordinary or standard tensor density formed from a tensor of arbitrary order,

$$
{ \mathfrak { A } } _ { \cdot \cdot } ^ { \dots } = ( - g ) ^ { 1 / 2 } A _ { \cdot \cdot } ^ { \dots } ,
$$

is

The .covariant derivative of a product is the sum of two terms: the covariant deriva-

tive of the first, times the second,plus the first times the covariant derivative of the second.

Now return to the integral to be evaluated. Combine the factors $g ^ { \alpha \beta }$ and $( - g ) ^ { 1 / 2 }$ into the tensor density ${ \mathfrak { g } } ^ { \alpha \beta }$ . Integrate covariantly by parts,as justified by the rule for the covariant derivative of a product. Get a “term at limits,” plus the integral

$$
- ( 1 / 1 6 \pi ) \int { ( { \bf { g } } ^ { \alpha \beta } ; \lambda - \delta _ { \lambda } ^ { \beta } { \bf { g } } ^ { \alpha \gamma } } _ { ; \gamma } ) \delta { \cal { T } } _ { \alpha \beta } ^ { \lambda } d ^ { 4 } x .
$$

This integral is the only term in the action integral that contains the variations of the $\boldsymbol { r }$ 's at the“interior points”of interest here.For the integral to be an extremum, the symmetrized coefficient of $\delta { \cal { T } } _ { \alpha \beta } ^ { \lambda }$ must vanish,

$$
{ \mathfrak { g } } ^ { \alpha \beta } { } _ { ; \lambda } - { \frac { 1 } { 2 } } \delta _ { \lambda } ^ { \alpha } { \mathfrak { g } } ^ { \beta \gamma } { } _ { ; \gamma } - { \frac { 1 } { 2 } } \delta _ { \lambda } ^ { \beta } { \mathfrak { g } } ^ { \alpha \gamma } { } _ { ; \gamma } = 0 .
$$

This set of forty equations for the forty covariant derivative $\mathfrak { g } ^ { \alpha \beta } { } _ { ; \lambda }$ has only the zero solution,

$$
{ \mathfrak { g } } ^ { \alpha \beta } { } _ { ; \lambda } = 0 .
$$

Thus the“density formed from the reciprocal metric tensor" is covariantly constant.

This simple result (l) brings many simple results in its train: the covariant constancy of (2) $( - g ) ^ { 1 / 2 }$ ，（3） $g ^ { \alpha \beta }$ ，（4) $g _ { \alpha \beta }$ ,and (5) $\mathfrak { g } _ { \alpha \beta }$ . Of these,(4) is of special interest here,and (2) is needed in proving it,as follows.Take definition (21.24) for the covariant derivative of $( - g ) ^ { 1 / 2 }$ ,and calculate the ordinary derivative that appears in the first term from exercise 21.1. One encounters in this calculation terms of the form $\partial \pmb { \mathfrak { g } } ^ { \alpha \beta } / \partial \pmb { x } ^ { \lambda }$ .Use (21.25) to evaluate them,and end up with the result

$$
( - g ) ^ { 1 / 2 } { } _ { ; \lambda } = 0 .
$$

From this result it follows that the covariant derivative of the $\textstyle { \binom { 1 } { 1 } }$ -tensor density $( - g ) ^ { 1 / 2 } \delta _ { \gamma } ^ { \alpha }$ is also zero.But this tensor density is the product of the tensor density ${ \mathfrak { g } } ^ { \alpha \beta }$ by the ordinary metric tensor $g _ { \beta \gamma } .$ In the covariant derivative of this product by $x ^ { \lambda }$ ， one already knows that the derivative of the first factor is zero. Therefore the first factor times the derivative of the second must be zero,

$$
{ \mathfrak { g } } ^ { \alpha \beta } g _ { \beta \gamma ; \lambda } = 0 ,
$$

and from this it follows that

$$
g _ { \beta \gamma ; \lambda } = 0 ,
$$

as was to be proven;or, explicitly,

$$
{ \frac { \partial g _ { \beta \gamma } } { \partial x ^ { \lambda } } } - g _ { \gamma \sigma } { \cal T } _ { \beta \lambda } ^ { \sigma } - g _ { \beta \sigma } { \cal T } _ { \gamma \lambda } ^ { \sigma } = 0 .
$$

Solve these equations for the $T ^ { \ast } { \mathsf { s } } _ { \mathrm { { } } }$ ，which up to now have been independent of the $g _ { \beta \gamma } ,$ and end up with the standard equation for the connection coefficients,

$$
{ \cal { T } } _ { \mu \nu } ^ { \rho } = { \frac { 1 } { 2 } } g ^ { \rho \sigma } ( g _ { \mu \sigma , \nu } + g _ { \sigma \nu , \mu } - g _ { \mu \nu , \sigma } ) ,
$$

as required for Riemannian geometry.

Similarly,equate to zero the coefficient of $\delta g ^ { \alpha \beta }$ in the variation (21.23),and find all ten components of Einstein's field equation,in the form

$$
G _ { \alpha \beta } = 8 \pi \underbrace { \left( g _ { \alpha \beta } L _ { \mathrm { f i e l d } } - 2 \frac { \delta L _ { \mathrm { f i e l d } } } { \delta g ^ { \alpha \beta } } \right) } _ { \mathrm { L } \mathrm { [ i d e n t i f i e d ~ i n ~ \ S 2 1 . 3 ~ w i t h ~ } } )
$$

Among variations of the metric,oneof the simplest is the change

$$
g _ { \mathrm { n e w } \mu \nu } = g _ { \mu \nu } + \delta g _ { \mu \nu } = g _ { \mu \nu } + \xi _ { \mu ; \nu } + \xi _ { \nu ; \mu }
$$

brought about by the infinitesimal coordinate transformation

$$
x _ { \mathrm { n e w } } ^ { \mu } = x ^ { \mu } - \xi ^ { \mu } .
$$

Although the metric changes, the 3-geometry does not. It does not matter whether the spacetime geometry that one is dealing with extremizes the action principle or not,whether it is a solution of Einstein's equations or not; the action integral $I$ is a scalar invariant, a number,the value of which depends on the physics but not at all on the system of coordinates in which that physics is expressed.This invariance even obtains for both parts of the action principle indiviually $( I _ { \mathrm { g e o m } }$ and $I _ { \mathrm { f i e l d s } } )$ Therefore neither part will be affected in value by the variation (21.29).In other words, the quantity

$$
\begin{array} { l } { { \delta I _ { \mathrm { g e o m } } = ( 1 / 1 6 \pi ) \int G _ { \alpha \beta } ( \xi ^ { \alpha ; \beta } + \xi ^ { \beta ; \alpha } ) ( - g ) ^ { 1 / 2 } d ^ { 4 } x } } \\ { { \mathrm { ~ \ - ~ } \overline { { { \frac { 1 } { \cdot } } } } \overline { { { \cos \pi } } } ^ { \prime } ( 1 / 8 \pi ) \int G _ { \alpha \beta } { } ^ { ; \beta } \xi ^ { \alpha } ( - g ) ^ { 1 / 2 } d ^ { 4 } x } } \\ { { \mathrm { ~ \ ~ } \begin{array} { l } { { \begin{array} { r l } { { \mathrm { ~ \ } } } & { { } } \\ { { \mathrm { ~ \ } } } & { { } } \end{array} } } \end{array} } } \end{array}
$$

Action unaffected by mere change in coordinatization

must vanish whatever the 4-geometry and whatever the change $\xi ^ { \alpha }$ . In this way, one Sees from a new angle the contracted Bianchi identities of Chapter 15,

$$
G _ { \alpha \beta } { } ^ { ; \beta } = 0 .
$$

The “neutrality”of the action principle with respect to a mere coordinate transformation such as (21.29) shows once again that the variational principle-and with it Einstein's equation-cannot determine the coordinates or the metric,but only the 4-geometry itself.

# ExerciSe 21.1. VARIATION OF THE DETERMINANT OF THE METRIC TENSOR

Recalling thatthe change in the valueof any determinantis given by multiplying the change in each element of that determinant by its cofactor and adding the resulting products (exercise 5.5) prove that

# EXERCISE

$$
\delta ( - g ) ^ { 1 / 2 } = \frac { 1 } { 2 } ( - g ) ^ { 1 / 2 } g ^ { \mu \nu } \delta g _ { \mu \nu } \qquad \mathrm { a n d } \qquad \delta ( - g ) ^ { 1 / 2 } = - \frac { 1 } { 2 } ( - g ) ^ { 1 / 2 } g _ { \mu \nu } \delta g ^ { \mu \nu } .
$$

Also show that

$$
g = \mathsf { d e t } ! | | \bar { \mathbf { g } } ^ { \mu \nu } | | \qquad \mathrm { a n d } \qquad \delta ( - g ) ^ { 1 / 2 } = + \frac 1 2 g _ { \mu \nu } \delta \mathbf { g } ^ { \mu \nu } .
$$

# \$21.3. MATTER LAGRANGIAN AND STRESS-ENERGY TENSOR

The derivation of Einstein's geometrodynamic law from Hilbert's action principle puts on.the righthand side a source term that is derived from the field Lagrangian. In contrast, the derivation of Chapter 17 identified the source term with the stressenergy tensor of the field.Forthe two derivations to be compatible,the stress-energy tensor must be given by the expression

$$
T _ { \alpha \beta } = - 2 \frac { \delta L _ { \mathrm { f i e l d } } } { \delta g ^ { \alpha \beta } } + g _ { \alpha \beta } L _ { \mathrm { f i e l d } } ,
$$

or

$$
( - g ) ^ { 1 / 2 } T ^ { \alpha \beta } \equiv { \mathfrak { C } } ^ { \alpha \beta } = 2 { \frac { \delta { \mathcal { L } } _ { \mathrm { f i e l d } } ^ { \beta } } { \delta g _ { \alpha \beta } } } .
$$

What are the consequences of this identification?

By the term“Lagrange function of the field”as employed here,one means the Lagrange function of the classical theory as formulated in flat spacetime,with the flat-spacetime metric replaced wherever it appears by the actual metric, and with the“comma-goes-to-semicolon rule” of Chapter l6 applied to all derivatives.

Were one dealing with a general tensorial field, the comma-goes-to-semicolon rule would introduce,in addition to the derivative of the tensorial field with allits indices, a number of $\boldsymbol { r }$ 's equal to the number of indices. The presence of these $\boldsymbol { r }$ 's in the field Lagrangian would have unhappy consequences for the Palatini variational procedure described in $\ S 2 1 . 2$ . No longer would the $\boldsymbol { r }$ 's end up given in terms of the metric coefficients by the standard formula (21.27).No longer would the geometry,as derived from the Hilbert-Palatini variation principle, be Riemannian. Then what?

These troublesome issues do not arise in two wel-known simple cases,a scalar field and an electromagnetic field. In the one case,the field Lagrangian becomes

$$
L _ { \mathrm { f i e l d } } = ( 1 / 8 \pi ) [ - g ^ { \alpha \beta } ( \partial \phi / \partial x ^ { \alpha } ) ( \partial \phi / \partial x ^ { \beta } ) - m ^ { 2 } \phi ^ { 2 } ] .
$$

Electromagnetism as an example

No connection coefficient comes in; the quantity being differentiated is a scalar. In the other case,the field Lagrangian is built on first derivatives of the 4-potential $A _ { \mu }$ 、Therefore $\boldsymbol { { \cal T } }$ 's should appear,according to the standard rules for covariant differentiation $\left( \mathbf { B o x } ~ 8 . 4 \right)$ .However, the derivatives of the A's appear, never alone, but always in an antisymmetric combination where the $\boldsymbol { { \cal T } }$ 's cancel, making covariant derivatives equivalent to ordinary derivatives:

$$
F _ { \mu \nu } = A _ { \nu ; \mu } - A _ { \mu ; \nu } = A _ { \nu , \mu } - A _ { \mu , \nu } .
$$

Contrast to stress-energy tensor of"canonical fieid theory"

In both cases,the differentiations of (21.33) to generate the stress-energy tensor are easily carried out (exercises 21.2 and 21.3) and give the standard expressions already seen [(5.22) and (5.23)] for $T _ { \mu \nu }$ in one of these two cases in an earlier chapter.

Field theory provides a quite other method to generate a so-called canonical expression for the stress-energy tensor of a field [see, for example, Wentzel (1949)].

By the very manner of construction, such an expression is guaranteed also to satisfy the law of conservation of momentum and energy,and by this circumstance it too becomes useful in certain contexts.However, the canonical tensor is often not symmetric in its two indices,and in such cases violates the law of conservation of angular momentum (see discussion in $\ S 5 . 7 )$ .Even when symmetric,it may give a quite different localization of stress and energy than that given by (21.33). Field theory in and by itself is unable to decide between these different pictures of where the field energy is localized.However, direct measurements of the pull of gravitation provide in_principle [see,for_example, Feynman (l964)] a means to distinguish between alternative prescriptions for the localization of stress-energy, because gravitation responds directly to density of mass-energy and momentum. It is therefore a happy circumstance that the theory of gravity in the variational formulation gives a unique prescription for fixing the stress-energy tensor,a prescription that, besides being symmetric, also automatically satisfies the laws of conservation of momentum and energy (exercises 21.2 and 21.3).[For an early discussion of the symmetrization of the stress-energy tensor, see Rosenfeld (1940) and Belinfante (1940).A more extensive discussion is given by Corson (l953) and Davis (l97O),along with extensive references to the literature.]

When one deals with a spinor field,one finds it convenient to take as the quantities to be varied, not the metric coefficients themselves,but the components of a tetrad of orthonormal vectors defined as a tetrad field over all space [see Davis (l970) for discussion and references].

# Exercise 21.2. STRESS-ENERGY TENSOR FOR A SCALAR FIELD

# EXERCISES

Given the Lagrange function (21.34) of a scalar field,derive the stressenergy tensor for this field.Also write down the field equation for the scalar field that one derives from this Lagrange function (in the general case where the field executes its dynamics within the arena of a curved spacetime). Show that as a consequence of this field equation, the stress-energy tensor satisfies the conservation law, $T _ { \alpha \beta } { } ^ { ; \beta } = { \bar { 0 } }$

# Exercise 21.3. FARADAY-MAXWELL STRESS-ENERGY TENSOR

Given the Lagrangian density $- F _ { \mu \nu } F ^ { \mu \nu } / 1 6 \pi$ ,reexpress it in terms of the Variables $A _ { \mu }$ and $\dot { \boldsymbol { g } } ^ { \mu \nu }$ ,and by use of (2l.33) derive the stress-energy tensor as discussed in $\ S 5 . 6$ Also derive from the Lagrange Variation principle the field equation $F _ { \alpha \beta } { } ^ { ; \beta } = 0$ (curved spacetime, but--for simplicity-a charge-free region of space).As a consequence of this field equation, show that the Faraday-Maxwellstress-energy tensor satisfies the conservation law, $T _ { \alpha \beta } \dot { \ast } ^ { \beta } = 0$ For a more ambitious project, show that any stress-energy tensor derived from a field Lagrangian by the prescription of equation (21.33) will automatically satisfy the conservation law $T _ { \alpha \beta } { } ^ { \bar { ; } \beta } = \bar { 0 }$

# \$21.4. SPLITTING SPACETIME INTO SPACE AND TIME

There are many ways to “push forward" many-fingered time and explore spacetime faster here and slower there,or faster there and slower here. However,a computer is most effciently programmed only when it follows one definite prescription. The

# 2

![](images/1d3210aae419c4d6b723f2d78b5755b8870f40b75a1e66132f706ada7ccba598.jpg)  
Figure 21.2. Building two 3-geometries into a thin sandwich 4-geometry， by interposing perpendicular connectors between the two,with preassigned lengths and shifts.What would otherwise be flexible thereupon becomes rigid. The flagged point ilustrates equation (21.40).

Slice spacetime to compute spacetime

successive hypersurfaces on which it gives the geometry are most conveniently described by successive values of a time-parameter t. One treats on a different footing the 3-geometries of these hypersurfaces and the 4-geometry that fills in between these laminations.

The slicing of spacetime into a one-parameter family of spacelike hypersurfaces is called for, not only by the analysis of the dynamics along the way, but also by the boundary conditions as they pose themselves in any action principle of the form, “Give the 3-geometries on the two faces of a sandwich of spacetime,and adjust the 4-geometry in between to extremize the action.”

There is no simpler sandwich to consider than one of infinitesimal thickness (Figure 21.2). Choosing coordinates adapted to the $( 3 + 1 )$ -space-time split, designate the “lower”(earlier) hypersurface in the diagram as $t =$ constant and the“upper"(later) one as $t + d t =$ constant (names, only names； no direct measure whatsoever of proper time). Compare the two hypersurfaces with two ribbons of steel out of which one wants to construct a rigid structure. To give the geometry on the two ribbons by no means fixes this structure; for that purpose, one needs cross-connectors between the one ribbon and the other.It is not even enough (l) to specify that these connectors are to be welded on perpendicular to the lower ribbon; (2) to specify where each is to be welded; and (3) to give its length. One must in.addition tell where each connector joins the upper surface. If the proper distances between tops of the connectors are everywhere shorter than the distances between the bases of the connectors,the double ribbon will have the curve of the cable of asuspension bridge; if everywhere longer,the curve of the arch of a masonry bridge. The data necessary for the construction of the sandwich are thus (l） the metric of the 3-geometry of the lower hypersurface,

$$
g _ { i j } ( t , x , y , z ) d x ^ { i } d x ^ { j } ,
$$

telling the (distance)² between one point in that hypersurface and another; (2) the metric on the upper hypersurface,

$$
g _ { i j } ( t + d t , x , y , z ) d x ^ { i } d x ^ { j } ;
$$

(3)a formula for the proper length,

$$
\left( \begin{array} { l } { \ln \mathrm { p s e ~ o f } } \\ { \mathsf { p r o p e r ~ t i m e } } \\ { \mathsf { b e t w e e n ~ l o w e r } } \\ { \mathrm { a n d ~ u p p e r } } \\ { \mathsf { h y p e r s u r f a c e } } \end{array} \right) = \binom { \mathrm { * l a p s e } } { \mathrm { f u n c t i o n } ^ { \mathrm { , * } } } d t = N ( t , x , y , z ) d t ,
$$

of the connector that is based on the point $( x , y , z )$ of the lower hypersurface; and (4) a formula for the place on the upper hypersurface,

$$
x _ { \mathrm { u p p e r } } ^ { i } ( x ^ { m } ) = x ^ { i } - N ^ { i } ( t , x , y , z ) d t ,
$$

where this connector is to be welded. Omit part of this information,and find the structure deprived of rigidity.

The rigidity of the structure of the thin sandwich is most immediately revealed in the definiteness of the 4-geometry of the spacetime filling of the sandwich. Ask for the proper interval ds or $d \tau$ between $\boldsymbol { x } ^ { \alpha } = ( t , x ^ { i } )$ and $x ^ { \alpha } + d x ^ { \alpha } =$ $( t + d t , x ^ { i } + d x ^ { i } )$ .The Pythagorean theorem in its 4-dimensional form

Metric of 4-geometry depends on Iapse and shift of connectors of the two 3-geometries

$$
d s ^ { 2 } = { \binom { \mathrm { p r o p e r ~ d i s t a n c e } } { \mathrm { i n ~ b a s e ~ } 3 - \mathrm { g e o m e t r y } } } ^ { 2 } - \left( { \overset { \mathrm { p r o p e r ~ t i m e ~ f r o m } } { \underset { \mathrm { l o w e r ~ t o ~ u p p e r ~ } } { 3 - \mathrm { g e o m e t r y } } } } ^ { 2 } \right) ^ { 2 }
$$

yields the result (see Figure 21.2).

$$
d s ^ { 2 } = \bar { g _ { i j } } ( d x ^ { i } + N ^ { i } d t ) ( d x ^ { j } + N ^ { j } d t ) - ( N d t ) ^ { 2 }
$$

Here as in (21.36) the $g _ { i j }$ are the metric coeffcients of the 3-geometry, distinguished by their Latin labels from the Greek-indexed components of the 4-metric,

$$
d s ^ { 2 } = { ^ { ( 4 ) } } g _ { \alpha \beta } d x ^ { \alpha } d x ^ { \beta } ,
$$

labeled here with a sufix (4) to reduce the possibility of confusion. Comparing (21.41) and (21.4O), one arrives at the following construction of the 4-metric out of the 3-metric and the lapse and shift functions [Arnowitt, Deser,and Misner (1962)):

Details of the 4-geometry

$$
| \begin{array} { c c } { { | { } ^ { ( 4 ) } g _ { 0 0 } { } ^ { ( 4 ) } g _ { 0 k } | } } \\ { { } } & { { } } \\ { { | { } ^ { ( 4 ) } g _ { i 0 } { } ^ { ( 4 ) } g _ { i k } | } } \end{array} | = | \begin{array} { c c } { { | { } ( N _ { s } N ^ { s } - N ^ { 2 } ) } } & { { N _ { k } } } \\ { { } } & { { } } \\ { { N _ { i } } } & { { g _ { i k } } } \end{array} | .
$$

The welded connectors do the job!

In (21.42), the quantities $N ^ { m }$ are the components of the shift in its original primordial contravariant form, whereas the $N _ { \mathrm { i } } = g _ { i m } N ^ { m }$ are the covariant components, as calculated within the 3-geometry with the 3-metric.To invert this relation,

$$
N ^ { m } = g ^ { m s } N _ { s }
$$

is to deal with the reciprocal 3-metric,a quantity that has to be distinguished sharply from the reciprocal 4-metric. Thus,the reciprocal 4-metric is

$$
\begin{array} { r } { \left\| ^ { ( 4 ) } g ^ { 0 0 ~ } ^ { ( 4 ) } g ^ { 0 m } \right\| = \left\| ^ { - ( 1 / N ^ { 2 } ) } \begin{array} { c c } { ( N ^ { m } / N ^ { 2 } ) } \\ { ( 4 ) _ { g } k ^ { 0 } } & { ( 4 ) _ { g } k m } \end{array} \right\| , } \end{array}
$$

a result that one checks by calculating out the product

$$
{ ^ { ( 4 ) } { g _ { \alpha \beta } } } ^ { ( 4 ) } { g ^ { \beta } } ^ { \gamma } = { ^ { ( 4 ) } } \delta _ { \alpha } { ^ { \gamma } }
$$

according to the standard rules for matrix multiplication.

The volume element has the form

$$
( - ^ { ( 4 ) } g ) ^ { 1 / 2 } d x ^ { 0 } d x ^ { 1 } d x ^ { 2 } d x ^ { 3 } = N g ^ { 1 / 2 } d t d x ^ { 1 } d x ^ { 2 } d x ^ { 3 } .
$$

Welding the connectors to the two steel ribbons,or adding the lapse and shift functions to the 3-metric,by rigidifying the 4-metric,also automatically determines the components of the unit timelike normal vector $\pmb { n }$ .The condition of normalization on this 4-vector is most easily formulated by saying that there exists a l-form,also called $\pmb { n }$ for the sake of convenience,dual to $\pmb { n }$ ,and such that the product of this vector by this 1-form has the value

$$
\langle \pmb { n } , \pmb { n } \rangle = - 1 .
$$

This 1-form has the value

$$
\pmb { n } = n _ { \beta } \pmb { d } x ^ { \beta } = - N \pmb { d } t + 0 + 0 + 0 .
$$

Only so can this l-form, this structure of layered surfaces,automatically yield a value of unity,one bong of the bell, when pierced as in Figure 2.4 by a vector that represents an advance of one unit in proper time, regardless of what $x , y ;$ and $z$ displacements it also has. Thus the unit timelike normal vector in covariant l-form representation necessarily has the components

$$
\boldsymbol { n } _ { \beta } = ( - N , 0 , 0 , 0 )
$$

Raise the indices via (21.44) to obtain the contravariant components of the same normal, represented as a tangent vector; thus,

$$
n ^ { \alpha } = [ ( 1 / N ) , - ( N ^ { m } / N ) ] .
$$

This result receives a simple interpretation on inspection of Figure 21.2. Thus the typical“perpendicular connector"in the diagram can be said to have the components

$$
( d t , - N ^ { m } d t )
$$

and to have the proper length $d \tau = N d t$ ；so,ratioed down to a vector $\pmb { n }$ of unit proper length, the components are precisely those given by (21.49).

# $\$ 21.5$ .INTRINSIC AND EXTRINSIC CURVATURE

The central concept in Einstein's account of gravity is curvature, so it is appropriate to analyze curvature in the language of the $( 3 + 1 )$ -space-time split. The curvature intrinsic to the 3-geometry of a spacelike hypersurface may be defined and calculated by the same methods described and employed in the calculation of four-dimensional curvature in Chapter l4. Of all measures of the intrinsic curvature, one of the simplest is the Riemann scalar curvature invariant $^ { ( 3 ) } R$ (written for simplicity of notation in what follows without the prefix, as $R$ );and of all ways to define this invariant (see Chapter l4),one of the most compact uses the limit (see exercise 21.4)

$$
R ( { \begin{array} { l } { \mathbf { \rho } } \\ { \mathbf { u } \mathbf { \rho } } \end{array} } ) = { \underset { \varepsilon \to 0 } { \mathrm { L i m ~ } } } \ 1 8 \ { \xrightarrow { 4 \pi \varepsilon ^ { 2 } - ( { \begin{array} { l } { \mathbf { p r o p e r ~ a r e a ~ o f ~ a ~ s u r f a c e ~ ( a p p r o x i m a t e l y } ) } \\ { \mathbf { a } ~ 2 \cdot \mathbf { s p h e r e } } \end{array} } ) } } \ \mathbf { d e f i n e d ~ a s ~ t h e ~ l o c u s ~ o f ~ t h e ~ } )
$$

For a more detailed description of the curvature intrinsic to the 3-geometry, capitalize on differential geometry as already developed in Chapters 8 through 14, amending it only as required to distinguish what is three-dimensional from what is four-dimensional. Begin by considering a displacement

$$
{ \pmb d } \mathcal { P } = { \pmb e } _ { i } { \pmb d } x ^ { i }
$$

within the hypersurface.Here the $\pmb { e _ { i } }$ are the basis tangent vectors $\pmb { e } _ { i } = \partial / \partial x ^ { i }$ (in one notation） or $\pmb { e } _ { i } = \partial \mathcal { P } / \partial x ^ { i }$ (in another notation） dual to the three coordinate 1-forms $\pmb { d x ^ { i } }$ Any field of tangent vectors $\pmb { A }$ that happens to lie in the hypersurface lets itself be expressed in terms of the same basis vectors:

$$
{ \pmb { A } } = { \pmb { e } } _ { i } { \pmb { A } } ^ { i } .
$$

The scalar product of this vector with the base vector $\pmb { e } _ { j }$ is

$$
( { \pmb A } \cdot { \pmb e } _ { j } ) = A ^ { i } ( { \pmb e } _ { i } \cdot { \pmb e } _ { j } ) = A ^ { i } g _ { i j } = A _ { j } .
$$

Now turn attention from a vector at one point to the parallel transport of the vector to a nearby point.

A vector lying on the equator of the Earth and pointing toward the North Star, transported parallel to itself along a meridian to a point still on the Earth's surface, but $1 { , } 0 0 0 \ \mathrm { k m }$ to the north,will no longer lie in the 2-geometry of the surface of the Earth.A telescope located in the northern hemisphere has to raise its tube to see the North Star! The generalization toa three-dimensional hypersurface imbedded in a 4-geometry is immediate. Take vector A,lying in the hypersurface,and transport it along an elementary route lying in the hypersurface,and in the course of this transport displace it at each stage parallel to itself, where “parallel” means parallel with respect to the geometry of the enveloping 4-manifold. Then $\pmb { A }$ will ordinarily end up no longer lying in the hypersurface. Thus the “covariant derivative”of $\pmb { A }$ in the direction of the $i$ -th coordinate direction in the geometry of the enveloping spacetime (that is, the $\pmb { A }$ at the new point diminished by the transported $\pmb { A }$ ）has the form (see $\ S 1 0 . 4 )$

$$
{ } ^ { ( 4 ) } \nabla _ { e _ { i } } A = { } ^ { ( 4 ) } \nabla _ { i } A = { } ^ { ( 4 ) } \nabla _ { i } ( e _ { j } A ^ { j } ) = e _ { j } \frac { \partial A ^ { j } } { \partial x ^ { i } } + { } ^ { ( 4 ) } \Gamma _ { j i } ^ { \mu } e _ { \mu } ) A ^ { j } .
$$

A specialinstance of this formula is the equation for the covariantly measured change of the base vector $\pmb { e _ { m } }$ itself,

$$
{ } ^ { ( 4 ) } \nabla _ { i } e _ { m } = { } ^ { ( 4 ) } \Gamma _ { m i } ^ { \mu } e _ { \mu } .
$$

In both (21.54)and (21.55) the presence of the “out-of-the-hypersurface component"

$$
( A ^ { j ( 4 ) } \Gamma _ { j i } ^ { 0 } ) ( e _ { 0 } \cdot n )
$$

From parallel transport in 4-geometry to parallel transport in 3-geometry

is quite evident.Now kill this component.Project $( 4 ) \triangledown \triangledown A$ orthogonally onto the hypersurface. In this way arrive at a parallel transport and a covariant derivative that are intrinsic to the 3-geometry of the hypersurface.By rights this covariant derivative should be written $( 3 ) { \pmb { \sigma } }$ ； but for simplicity of notation it will be written as $\blacktriangledown$ in the rest of this chapter, except where ambiguity might arise. To get the value of the new covariant derivative, one has only to rewrite (21.54) with the suffix (4) replaced everywhere by a(3,or, better,dropped altogether and with the“dummy index” of summation $\mu = ( 0 , 1 , 2 , 3 )$ replaced by $m = ( 1 , 2 , 3 )$ . However, it is more convenient, following Israel (l966),to turn from an expression dealing with contravariant components $A ^ { i }$ of $\pmb { A }$ to one dealing with covariant components $A _ { i } = ( \pmb { A } \cdot \pmb { e } _ { i } )$ · Thus the covariant derivative of $\pmb { A }$ in the direction of the $\scriptstyle { i . }$ -th coordinate direction in the hypersurface, calculated with respect to the 3-geometry intrinsic to the hypersurface itself,has for its $h _ { \ l }$ -th covariant component the quantity [see equation (10.18)]

A new covariant derivative, taken with respect to the 3-geometry

$$
A _ { h \mid i } = e _ { h } \cdot ^ { ( 3 ) } \nabla _ { e _ { i } } A \equiv e _ { h } \cdot \nabla _ { i } A = \frac { \partial A _ { h } } { \partial x ^ { i } } - A ^ { m } \Gamma _ { m h i } ( = A _ { h ; i } \mathrm { ~ f o r ~ } A \mathrm { ~ i n ~ } \varSigma ) .
$$

Here the notation of the vertical stroke distinguishes this covariant derivative from the covariant derivative taken with respect to the 4-geometry,as, for example,in equations (10.17ff).The connection coefficients here for three dimensions, like those dealt with earlier for four dimensions [see the equations leading from (l4.14) through (l4.15)], allow themselves to be expressed in terms of the metric coefficients and their first derivatives,and have the interpretation

$$
{ } ^ { ( 3 ) } \Gamma _ { m h i } \equiv { \cal I } _ { m h i } = \boldsymbol { e } _ { m } \cdot \nabla _ { i } \boldsymbol { e } _ { h } .
$$

From the connection coefficients in turn,one calculates as in Chapter l4 the full Riemann curvature tensor $^ { ( 3 ) } { R ^ { \ell } } _ { j m n }$ of the3-geometry intrinsictothe hypersurface

Over and above the curvature intrinsic to the simultaneity,one now encounters a concept not covered in previous chapters (except fleetingly in Box l4.1),the extrinsic curvature of the 3-geometry. This idea has no meaning for a 3-geometry conceived in and by itself. It depends for its existence on this 3-geometry's being imbedded as a well-defined slice in a well-defined enveloping spacetime. It measures the curvature of this slice relative to that enveloping 4-geometry (Figure 21.3).

![](images/b9896f90591646521b8b1260507e9686cb39d3c6d1c5f4b9920994186a48bd1b.jpg)  
Figure 21.3. Extrinsic curvature measures the fractional shrinkage and deformation of a figure lying in the spacelike hypersurface $\pmb { \Sigma }$ that takes place when each point in the figure is carried forward a unit interval of proper time “normal" to the hypersurface out into the enveloping spacetime. (No enveloping spacetime? No extrinsic curvature!） The extrinsic curvature tensor is a positive multiple of the unit tensor when elementary displacements $\delta \mathcal { P }$ ,in whatever direction within the surface they point,all experience the same fractional_shrinkage.Thus the extrinsic curvature of the hypersurface illustrated in the figure is positive. The dashed arrow represents the normal vector $\pmb { n }$ at the fiducial point $\mathcal { P }$ after parallel transport to the nearby point $\mathcal { P } + \delta \mathcal { P }$

Take the normal that now stands at the point $\mathcal { P }$ and,“keeping its base in the hypersurface" $\pmb { \Sigma }$ , transport it parallel to itself as a“fducial vector” to the point $\mathcal { P } + \delta \mathcal { P }$ ,and there subtract it from the normal vector that already stands at that point. The difference, $\delta \pmb { n }$ ,may be regarded in the appropriate approximation as a “vector,” the value of which is governed by and depends linearly on the“vector" of displacement $\delta \mathcal { P }$

To obviate any appeal to the notion of approximation, go from the finite displacement $\delta \mathcal { P }$ to the limiting concept of the vector-valued“displacement 1-form" $\pmb { d } \mathcal { P }$ [see equation 15.13]. Also replace the finite but not rigorously defined vector $\delta \pmb { n }$ by the limiting concept of a vector-valued 1-form dn. This quantity, regarded as a vector, being the change in a vector $\pmb { n }$ that does not change in length,must represent a change in direction and thus stand perpendicular to $\pmb { n }$ .Therefore it can be regarded as lying in the hypersurface $\pmb { \Sigma }$ .Depending linearly on $\pmb { d } \mathcal { P }$ ,it can be represented in the form

$$
d n = - K ( d \mathcal { O } ) .
$$

Here the linear operator $\pmb { \kappa }$ is the extrinsic curvature presented as an abstract coordinate-independent geometric object. The sign of $\pmb { \kappa }$ as defined here is positive when the tips of the normals in Figure 21.3 are closer than their bases,as they are, for example,during the recontraction of a model universe, in agreement with the conventions employed by Eisenhart (l926), Schouten (l954),and Arnowitt Deser and Misner (l962),but opposite to the convention of Israel (1966).

Into the slots in the 1-forms that appear on the lefthand and righthand sides of (21.59), insert in place of the general tangent vector[which is to describe the general local displacement, so far left open,as in the discussion following (2.12a)] a very special tangent vector, the basis vector $\pmb { e _ { i } }$ ,for a displacement in the $\pmb { i }$ -th coordinate direction.Thus find (21.59） reading

$$
{ } ^ { ( 4 ) } \nabla _ { i } n = - K ( \pmb { e } _ { \mathrm { i } } ) = - K _ { i } { } ^ { j } \pmb { e } _ { \mathrm { j } } ,
$$

where the $K _ { i } ^ { j }$ are the components of the linear operator $\pmb { \kappa }$ in a coordinate representation. Take the scalar product of both sides of (21.60) with the basis vector ${ \pmb { e } } _ { m }$ Recall $( { \pmb e } _ { m } \cdot { \pmb n } ) = 0$ . Thus establish the symmetry of the tensor $K _ { i m }$ ，covariantly presented, in its two indices:

$$
\begin{array} { r l } & { K _ { i m } = K _ { i } ^ { j } g _ { j m } = K _ { i } ^ { j } ( \pmb { e } _ { j } \cdot \pmb { e } _ { m } ) = - \pmb { e } _ { m } \cdot ^ { ( 4 ) } \pmb { \nabla } _ { i } n = n \cdot ^ { ( 4 ) } \pmb { \nabla } _ { i } \pmb { e } _ { m } } \\ & { \qquad = ( n \cdot \pmb { e } _ { 0 } ) ^ { ( 4 ) } T _ { m \mathrm { i } } ^ { 0 } = \pmb { n } \cdot ^ { ( 4 ) } \pmb { \nabla } _ { m } \pmb { e } _ { i } = K _ { m \mathrm { i } } . } \\ & { \qquad \quad \sum _ { \left\{ \sec { \beta } ( 2 1 . 5 5 ) \right\} } } \end{array}
$$

A knowledge of the tensor $K _ { i j }$ of extrinsic curvature assists in revealing the changes of the four vectors n, e1, ${ \pmb { \theta } } _ { 2 } , { \pmb { \theta } } _ { 3 }$ under parallel transport. Equation (21.60) already tells how $\pmb { n }$ changes under parallel transport. The change of ${ \pmb { e _ { m } } }$ is to be read off from (21.55) as a vector. It is adequate identification of this vector to know its scalar product with each of four independent vectors: with the basis vectors $\pmb { \theta } _ { 1 } , \pmb { \theta } _ { 2 } ,$ and $\pmb { \theta } _ { 3 }$ ，or,more briefly,with ${ \pmb { e } } _ { s }$ ,in (21.58)；and with the normal vector $\pmb { n }$ in (21.61). Thus one arrives,following Israel (l966),at what are known as the equations of Gauss and Weingarten, in happy oversight of allchange of notation in the intervening century:

$$
^ { ( 4 ) } \nabla _ { i } e _ { j } = K _ { i j } \frac { n } { \pmb { n } \cdot \pmb { n } } + { } ^ { ( 3 ) } \Gamma _ { j i } ^ { h } \pmb { e } _ { h } . ^ { - }
$$

Knowing from this equation how each basis vector in $\pmb { \Sigma }$ changes,one also knows how to rewrite (21.54) for the change in any vector field $\pmb { A }$ that lies in $\pmb { \Sigma }$ . The change in both cases is expressed relative to a fiducial vector transported from a fiducial nearby point. By the term“parallel transport”one now means“parallel with respect to the geometry of the enveloping spacetime":

$$
{ } ^ { ( 4 ) } \nabla _ { i } { \pmb A } = A ^ { j } { } _ { | i } { \pmb e } _ { j } + K _ { i j } A ^ { j } \frac { \pmb n } { ( \pmb n \cdot \pmb n ) } .
$$

Of special importance is the evaluation of extrinsic curvature when spacetime is sliced up into spacelike slices according to the plan of Arnowitt,Deser,and Misner as described in $\ S 2 1 . 4$ .The 4-geometry of the thin sandwich illustrated in Figure 21.2,rudimentary though it is, is fully defined by the 3-metric on the two faces of the sandwich and by the lapse and shift functions $N$ and $N ^ { \widehat { \bullet } }$ .The normal in covariant representation according to (21.47) has the components

$$
( n _ { 0 } , n _ { 1 } , n _ { 2 } , n _ { 3 } ) = ( - N , 0 , 0 , 0 ) .
$$

The change in $\pmb { n }$ relative to $^ { 6 6 } _ { D }$ transported parallel to itself in the enveloping 4-geometry,” according to the definition of parallel transport, is

$$
\begin{array} { l } { ( d { \boldsymbol { n } } ) _ { \mathrm { i } } = n _ { i ; k } d x ^ { k } } \\ { = \left[ \displaystyle \frac { \partial n _ { \mathrm { i } } } { \partial x ^ { k } } - { } ^ { ( 4 ) } { \boldsymbol { T } } _ { \mathrm { i } k } ^ { \sigma } n _ { \sigma } \right] d x ^ { k } } \\ { = N ^ { ( 4 ) } { \boldsymbol { T } } _ { \mathrm { i } k } ^ { 0 } d x ^ { k } } \end{array}
$$

Compare to the same change as expressed in terms of the extrinsic curvature tensor,

$$
( d \pmb { { n } } ) _ { \mathrm { { i } } } = - K _ { i k } \ \pmb { { d } } x ^ { k } .
$$

Conelude that this tensor has the value

$$
K _ { i k } = - n _ { i ; k } = - N ^ { ( 4 ) } { \cal { T } } _ { i k } ^ { 0 } = - N [ { } ^ { ( 4 ) } g ^ { 0 0 ( 4 ) } { \cal { T } } _ { 0 i k } + { } ^ { ( 4 ) } g ^ { 0 p ( 4 ) } { \cal { T } } _ { p i k } ] ,
$$

or,with the help of equations (21.42) and (21.44),

$$
\begin{array} { l } { { \displaystyle K _ { i k } = ( 1 / N ) [ ^ { ( 4 ) } T _ { 0 i k } - N ^ { p ( 3 ) } T _ { p i k } ] } } \\ { { \displaystyle = \frac { 1 } { 2 N } \bigg [ \frac { \partial N _ { i } } { \partial x ^ { k } } + \frac { \partial N _ { k } } { \partial x ^ { i } } - \frac { \partial g _ { i k } } { \partial t } - 2 T _ { p i k } N ^ { p } \bigg ] } } \\ { { \displaystyle = \frac { 1 } { 2 N } \bigg [ N _ { i | k } + N _ { k | i } - \frac { \partial g _ { i k } } { \partial t } \bigg ] . } } \end{array}
$$

Extrinsic curvature in terms of shift and change of 3-metric

This is the extrinsic curvature expressed in terms of the ADM lapse and shift functions [Arnowit, Deser, and Misner (1962)].

As an example, let $\pmb { \Sigma }$ have the geometry of a 3-sphere

$$
d s ^ { 2 } = a ^ { 2 } [ d \chi ^ { 2 } + \sin ^ { 2 } \chi ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) ] .
$$

Extrinsic curvature of expanding 3-sphere

Let the nearby spacelike slice in the one-parameter family of slices,the slice with the label $t + d t$ (only a label!) have a 3-metric given by the same formula with the radius $^ { a }$ replaced by $a + d a$ 、The 4-geometry of the thin sandwich between these two slices is completely undetermined until one gives the lapse and shift functions. For simplicity,take the shift vector $N ^ { \pm }$ (see Figure 21.2) to be everywhere zero and the lapse function at every point on $\pmb { \Sigma }$ to have the same value $N .$ The separation in proper time between the two spheres is thus $d \tau = N d t$ Any geometric figure located in $\pmb { \Sigma }$ expands with time. The fractional increase of any length in this figure per unit of proper time is the same in whatever direction that length is oriented, and has the value

$$
{ \binom { \mathrm { f r a c t i o n a l { \ i n c r e a s e } } } { \mathrm { o f ~ l e n g t h ~ p e r ~ u n i t } } } = { \frac { 1 } { a } } { \frac { d a } { d \tau } } = { \frac { 1 } { 2 N } } { \frac { 1 } { a ^ { 2 } } } { \frac { d ( a ^ { 2 } ) } { d t } } .
$$

The negative of this quantity,multiplied by the $\textstyle { \binom { 1 } { 1 } }$ unit tensor, $\pmb { \eta } = \pmb { d } \mathscr { P }$ ，gives the extrinsic curvature tensor in $\mathbf { \Sigma } ( _ { 1 } ^ { 1 } )$ representation,

$$
\pmb { K } = - \frac { 1 } { 2 N } \frac { 1 } { a ^ { 2 } } \frac { d ( a ^ { 2 } ) } { d t } \pmb { \eta } .
$$

One confirms this result (exercise 21.5) by direct calculation of the components $K _ { i } ^ { j }$ using the ADM formula (21.67) as the starting point.

The Riemann curvature $R ^ { a } { } _ { b c d } = { } ^ { ( 3 ) } R ^ { a } { } _ { b c d }$ intrinsic to the hypersurface $\pmb { \Sigma }$ together with the extrinsic curvature $K _ { i j } ,$ give one information on the Riemann and Einstein curvatures of the 4-geometry. In the calculation,it is not convenient to use the coordinate basis,

$$
\begin{array} { c c } { { \pmb e } _ { 0 } = \hat { \sigma } _ { t } , } & { { } } & { ~ { \pmb d } t , } \\ { { \pmb e } _ { i } = \hat { \sigma } _ { i } , } & { { } } & { ~ { \pmb d } x ^ { i } , } \end{array}
$$

Basic forms for calculating 4-curvature

because ordinarily the basis vector ${ \pmb \theta } _ { 0 }$ does not stand perpendicular to the hypersurface (see Figure 21.2).Adopt a different basis but one that is still self-dual,

$$
\begin{array} { c c } { { { \pmb e } _ { n } \equiv { \pmb n } = N ^ { - 1 } ( \hat { \partial } _ { t } - N ^ { m } \hat { \partial } _ { m } ) , \ } } & { { { \pmb \omega } ^ { n } = N { \pmb d } t = ( { \pmb n } \cdot { \pmb n } ) { \pmb n } } } \\ { { { \pmb e } _ { \mathrm { i } } = \hat { \partial } _ { \pmb { i } } , \ } } & { { { \pmb \omega } ^ { i } \equiv { \pmb d } x ^ { i } + N ^ { i } { \pmb d } t . } } \end{array}
$$

Also use Greek labels $\overline { { \alpha } } = n , 1 , 2 , 3$ ,instead of Greek labels $\alpha = 0 , 1 , 2 , 3$ to list components.

Recall that curvature is measured by the change in a vector on transport around a closed route; or, from equation (14.23),

$$
\boldsymbol { \mathcal { R } } ( u , v ) \boldsymbol { w } = \nabla _ { u } \ \nabla _ { v } \boldsymbol { w } - \nabla _ { v } \ \nabla _ { u } \boldsymbol { w } - \nabla _ { \{ u , v \} } \boldsymbol { w } .
$$

Let the vector transported be $\pmb { e } _ { i }$ and let the route be defined by $\pmb { e _ { j } }$ and $\pmb { \theta } _ { k }$ The latter two vectors belong to a coordinate basis.Therefore the“route closes automatically", $[ { \pmb e } _ { j } , { \pmb e } _ { k } ] = 0$ , and the final term in (21.72) drops out of consideration. Call on (21.62) and (21.60) to find

$$
\begin{array} { r l } & { ^ { ( 4 ) } \pmb { \nabla _ { e _ { j } } } ^ { ( 4 ) } \pmb { \nabla _ { e _ { k } } } \pmb { e _ { \mathrm { i } } } = ^ { ( 4 ) } \pmb { \nabla _ { e _ { j } } } \bigg [ K _ { i k } \frac { \pmb { n } } { ( \pmb { n } \cdot \pmb { n } ) } + ^ { ( 3 ) } \varGamma _ { \mathrm { i } k } ^ { \ast } \pmb { e _ { m } } \bigg ] } \\ & { \qquad = K _ { i k , j } \frac { \pmb { n } } { ( \pmb { n } \cdot \pmb { n } ) } - K _ { i k } K _ { j } ^ { m } \pmb { e _ { m } } \frac { 1 } { ( \pmb { n } \cdot \pmb { n } ) } + ^ { ( 3 ) } \varGamma _ { i k , j } ^ { m } \pmb { e _ { m } } } \\ & { \qquad + ^ { ( 3 ) } \varGamma _ { \mathrm { i } k } ^ { m } \bigg [ K _ { m j } \frac { \pmb { n } } { ( \pmb { n } \cdot \pmb { n } ) } + ^ { ( 3 ) } \varGamma _ { m j } ^ { \ast } \pmb { e _ { s } } \bigg ] . } \end{array}
$$

Gauss-Codazzi: 4-curvature in terms of intrinsic 3-geometry and extrinsic curvature

Evaluate similarly the term with indices $j$ and $k$ reversed, subtract from (21.73), simplify, and find

$$
\begin{array} { r l } & { \boldsymbol { \mathcal { A } } ( \boldsymbol { e } _ { j } , \boldsymbol { e } _ { k } ) \boldsymbol { e } _ { i } = ( K _ { \mathrm { i } k | \mathrm { j } } - K _ { \mathrm { i } j | k } ) \frac { \boldsymbol { n } } { ( \boldsymbol { n } \cdot \boldsymbol { n } ) } } \\ & { \phantom { { = } } + [ ( \boldsymbol { n } \cdot \boldsymbol { n } ) ^ { - 1 } ( K _ { \mathrm { i } j } K _ { k } ^ { \prime \prime } - K _ { \mathrm { i } k } K _ { j } ^ { \prime \prime } ) + { } ^ { ( \mathrm { i } ) } R ^ { m } { } _ { i j k } ] \boldsymbol { e } _ { m } . } \end{array}
$$

The coefficients give directly the desired components of the curvature tensor

$$
{ } ^ { ( 4 ) } R ^ { m } { } _ { i j k } = { } ^ { ( 3 ) } R ^ { m } { } _ { i j k } + ( \pmb { n } \cdot \pmb { n } ) ^ { - 1 } ( K _ { i j } K _ { k } ^ { \ m } - K _ { i k } K _ { j } ^ { \ m } )
$$

and

$$
{ } ^ { ( 4 ) } R ^ { n } { } _ { i j k } = ( \pmb { n } \cdot \pmb { n } ) ^ { - 1 } { } ^ { ( 4 ) } R _ { n i j k } = - ( \pmb { n } \cdot \pmb { n } ) ^ { - 1 } ( K _ { i j | k } - K _ { i k | j } ) .
$$

Equations (21.75) and (21.76) are known as the equations of Gauss and Codazzi [for literature, see Eisenhart (1926)]. It follows from (21.75) that the components of the curvature of the 3-geometry will normally only then agree with the corresponding components of the curvature of the 4-geometry when the imbedding happens to be accomplished at the point under study with a hypersurface free of extrinsic curvature. The directly opposite situation is illustrated by the familiar example of a 2-sphere imbedded in a flat 3-space, where the lefthand side of (21.75) (with dimensions lowered by one unit throughout!) is zero,and the extrinsic and intrinsic curvature on the right exactly cancel.

Important components of the Einstein curvature let themselves be evaluated from the Gauss-Codazzi results. In doing the calculation,it is simplest to think of $\pmb { e } _ { i } , \pmb { e } _ { j }$ and $\pmb { e } _ { k }$ as being an orthonormal tetrad, $\pmb { n }$ being itself already normalized and orthogonal to every vector in the hypersurface. Then, employing (l4.7) and (21.75), one finds

Einstein curvature in terms of extrinsic curvature

$$
\begin{array} { l } { { \displaystyle - G _ { 0 } ^ { 0 } = { } ^ { ( 4 ) } R ^ { 1 2 } { } _ { 1 2 } + { } ^ { ( 4 ) } R ^ { 2 3 } { } _ { 2 3 } + { } ^ { ( 4 ) } R ^ { 3 1 } { } _ { 3 1 } } } \\ { { \displaystyle ~ = { } ^ { ( 3 ) } R ^ { 1 2 } { } _ { 1 2 } + { } ^ { ( 3 ) } R ^ { 2 3 } { } _ { 2 3 } + { } ^ { ( 3 ) } R ^ { 3 1 } { } _ { 3 1 } } } \\ { { \displaystyle ~ + ( n \cdot n ) ^ { - 1 } [ ( K _ { 1 } ^ { 2 } K _ { 2 } ^ { 1 } - K _ { 2 } ^ { 2 } K _ { 1 } ^ { 1 } ) + ( K _ { 2 } ^ { 3 } K _ { 3 } ^ { 2 } - K _ { 3 } ^ { 3 } K _ { 2 } ^ { 2 } ) } } \\ { { \displaystyle ~ + ( K _ { 3 } ^ { 1 } K _ { 1 } ^ { 3 } - K _ { 1 } ^ { 1 } K _ { 3 } ^ { 3 } ) ] } } \\ { { \displaystyle ~ = \frac { 1 } { 2 } R - \frac { 1 } { 2 } ( n \cdot n ) ^ { - 1 } [ ( \mathrm { T r } K ) ^ { 2 } - \mathrm { T r } ( K ^ { 2 } ) ] . } } \end{array}
$$

Here $R$ is the 3-dimensional scalar curvature invariant and Tr stands for “trace of"; thus,

$$
\mathrm { T r } K = g ^ { i j } K _ { i j } = g _ { i j } K ^ { i j } = K _ { j } ^ { j }
$$

and

$$
\mathrm { T r } K ^ { 2 } = ( K ^ { 2 } ) _ { j } ^ { j } = K _ { j } ^ { m } K _ { m } { } ^ { j } = g _ { j s } K ^ { s m } g _ { m i } K ^ { i j } .
$$

The result, though obtained in an orthonormal tetrad, plainly is covariant with respect to general coordinate transformations within the spacelike hypersurface; and it makes no explicit reference whatever to any time coordinate, in this respect providing a coordinate-free description of the Einstein curvature.

The Einstein field equation equates (21.77） to $8 \pi \rho$ where $\pmb { \rho }$ is the density of mass-energy.Expression (21.77) is the “measure of curvature that is independent of how curved one cuts a spacelike slice.”This measure of curvature is central to the derivation of Einstein's field equation that is sketched in Box l7.2, item 3, “Physics on a Spacelike Slice."

The other component of the Einstein curvature tensor that is easily evaluated by (14.7) from the results at hand has the form

$$
\begin{array} { l } { { G _ { 1 } ^ { n } = { } ^ { ( 4 ) } R ^ { n 2 } { } _ { 1 2 } + { } ^ { ( 4 ) } R ^ { n 3 } { } _ { 1 3 } } } \\ { { \ = - ( \pmb { n } \cdot \pmb { n } ) ^ { - 1 } ( K _ { 1 / 2 } ^ { 2 } - K _ { 2 / 1 } ^ { 2 } + K _ { 1 / 3 } ^ { 3 } - K _ { 3 / 1 } ^ { 3 } ) , } } \end{array}
$$

Equation (21.77) is the central Einstein equation, "mass-energy fixes curvature"

when referred to an orthonormal frame. One immediately translates to a form valid for any frame $\pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ in the hypersurface, orthonormal or not,

$$
G _ { i } ^ { n } = - ( { \pmb { n } } \cdot { \pmb { n } } ) ^ { - 1 } [ K _ { i | m } ^ { m } - ( \operatorname { T r } { \pmb { K } } ) _ { | i } ] .
$$

The other initial-value equation

The Einstein field equation equates this quantity to ${ 8 \pi }$ times the $i .$ -th covariant component of the density of momentum carried by matter and fields other than gravity.

The four components of the Einstein field equation so far written down will have a central place in what follows as “initial-value equations”of general relativity. The other six components will not be written out: (l) the dynamics lets itself be analyzed more simply by Hamiltonian methods;and (2) the calculation takes work.It demands that one evaluate the remaining type of object, $\mathcal { R } ( \pmb { e } _ { j } , \pmb { n } ) \pmb { e } _ { i }$ .One step towards that calculation will be found in exercise 21.7. Sachs does the calculation (l964,equation 10） but only after specializing to Gaussian normal coordinates. These coordinates presuppose a very special slicing of spacetime: (l） geodesics issuing normally from the spacelike hypersurface $n = 0$ cut all subsequent simultaneities ${ \pmb n } =$ constant normally; and (2) the $_ n$ coordinate directly measures lapse of proper time, or proper length,whichever is appropriate,\* along these geodesics. In coordinates so special it is not surprising that the answer looks simple:

$$
{ } ^ { ( 4 ) } R ^ { n } { } _ { i n k } = ( n \cdot n ) ^ { - 1 } \left( { \frac { \partial K _ { i k } } { \partial n } } + K _ { i m } K ^ { m } { } _ { k } \right) . \qquad { \Big ( } { \begin{array} { l } { { \mathrm { G a u s s i a n ~ n o r m a l } } } \\ { { \mathrm { c o o r d i n a t e s } } } \end{array} } { \Big ) }
$$

Additional terms come into (21.82) when one uses,instead of the Gaussian normal coordinate system, the coordinate system of Arnowitt, Deser,and Misner. The ADM coordinates are employed here because they allow one to analyze the dynamics as one wants to analyze the dynamics, with freedom to push the spacelike hypersurface ahead in time at different rates in different places ("many-fingered time"). Fischer (1971)shows how to evaluate and understand the geometric content of such formulas in a coordinate-free way by using the concept of Lie derivative of a tensor field, an introduction to which is provided by exercise 21.8.

# EXERCISES

Exercise 21.4. SCALAR CURVATURE INVARIANT IN TERMS OF AREA DEFICIT It being $1 0 , 0 0 0 ~ \mathrm { k m }$ from North Pole to equator, one would have $^ { 6 2 , 8 3 2 \mathrm { ~ k m } }$ for the length of the “equator” if the earth were flat, as contrasted to the actual ${ \sim } 4 0 , 0 0 0 ~ \mathrm { k m }$ ,a difference reflecting the fact that the surface is curved up into closure. Turn from this “pre-problem” to the actual problem,a 3-sphere

$$
d s ^ { 2 } = a ^ { 2 } [ d \chi ^ { 2 } + \sin ^ { 2 } \chi ( d \theta ^ { 2 } + \sin ^ { 2 } \theta \ d \phi ^ { 2 } ) ] .
$$

Measure off from $x = 0$ a 2-sphere of proper radius $\varepsilon = a x$ Determine the proper area of this 2-sphere as a function of $x$ .Verify that relation (21.5O) on the area deficit gives in the limit $\varepsilon \longrightarrow 0$ the correct result $R = 6 / a ^ { 2 }$ .For a more ambitious exercise: (l) take a general (smooth) 3-geometry; (2) express the metric near any chosen point in terms of Riemann's normal coordinates as given in $\ S 1 1 . 6$ ； (3) determine the locus of the set of points at the proper distance e to the lowest interesting power ofe in terms of the spherical polar angles $\pmb \theta$ and $\phi$ (direction of start of geodesic of length e); (4) determine to the lowest interesting power ofe the proper area of the figure defined by these points; and thereby establish (21.50) [for more on this topic see,for example, Cartan (1946), pp.252-256].

# Exercise 21.5. EXTRINSIC CURVATURE TENSOR FOR SLICE OF FRIEDMANN GEOMETRY

Confirm the result (21.7O) for the extrinsic curvature by direct calculation from formula (21.67).

# Exercise 21.6. EVALUATION OF $\mathcal { R } ( e _ { j } , ~ e _ { k } ) _ { n }$

Evaluate this quantity along the model of (21.74) or otherwise.How can it be foreseen that the coefficient of $\pmb { n }$ in the result must vanish identically? Comparing coeficients of $\pmb { e _ { m } } .$ find ${ } ^ { ( 4 ) } R _ { n j k } ^ { m }$ and test forequivalencetoequation(276).

# Exercise 21.7. EVALUATION OF THE COMMUTATOR $[ e _ { j } , n ]$

The evaluation of this commutator is a first step toward the calculation of a quantity like $\mathcal { R } ( \pmb { e } _ { j } , \pmb { n } ) \pmb { e } _ { i }$ Expressing $\pmb { e } _ { j }$ as the differential operator $\partial / \partial x ^ { j }$ ,use (21.49) to represent $\pmb { n }$ also as a differential operator. In this way,show that the commutator in question has the value $- ( N _ { \underline { { { j } } } } / N ) \pmb { \eta } - ( \underbrace { N ^ { m } } _ { ~ , j } / N ) \pmb { e } _ { m } , ~ .$

Exercise 21.8. LIE DERIVATIVE OF A TENSOR (exercise provided byJ.W.York, Jr.) Define the Lie derivative of a tensor field and explore some of its properties. The Lie derivative along a vector field $\pmb { n }$ is a differential operator that operates on tensor fields $\pmb { \tau }$ of type $( \underline { { \tau } } )$ ,converting them into tensors $\pmb { \mathcal { L } } _ { n } \pmb { \cal T } ,$ also of type (g). The Lie differentiation process obeys the usual chain rule and has additivity properties [compare equations (l0.2b,10.2c, 10.2d) for the covariant derivative]. For scalar functions $f ,$ one has ${ \pmb { \mathscr { L } } } _ { n } f { \equiv } { \pmb { n } } \{ f \} = f _ { , \mu } { \pmb { n } } ^ { \mu } .$ The Lie derivative of a vector feld $\pmb { u }$ along a vector field ${ \pmb v }$ was defined in exercise 9.11 by

$$
\pmb { \mathscr { L } } _ { \pmb { u } } \pmb { v } \equiv [ \pmb { u } , \pmb { v } ] .
$$

If the action of ${ \pmb { \mathscr { L } } } _ { \pmb { \mathscr { n } } }$ on l-forms is defined, the extension to tensors of general type will be simple, because the latter can always be decomposed into a sum of tensor products of vectors and 1-forms. If $\pmb { \sigma }$ is a l-form and ${ \pmb v }$ is a vector,then one defines $\pmb { \mathcal { L } _ { p } } \pmb { \sigma }$ to be that l-form satisfying

$$
\langle { \pmb { \mathscr { L } } } _ { n } \sigma , { \pmb v } \rangle = n [ \langle { \pmb { \sigma } } , { \pmb v } \rangle ] - \langle { \pmb { \sigma } } , [ { \pmb { n } } , { \pmb v } ] \rangle
$$

for arbitrary ${ \pmb v }$

(a) Show that in a coordinate basis

$$
\pmb { \mathcal { L } } _ { n } \pmb { \sigma } = ( \sigma _ { \alpha , \beta } n ^ { \beta } + \sigma _ { \beta } n _ { , \alpha } ^ { \beta } ) \pmb { d } x ^ { \alpha } .
$$

(b) Show that in a coordinate basis

$$
{ \pmb { \mathscr { L } } } _ { n } { \pmb { T } } = ( T _ { \alpha \beta , \mu } n ^ { \mu } + T _ { \mu \beta } n ^ { \mu } { } _ { , \alpha } + T _ { \alpha \mu } n ^ { \mu } { } _ { , \beta } ) d x ^ { \alpha } \otimes d x ^ { \beta }
$$

where $\pmb { \tau }$ is of type $( \mathbf { \small { \begin{array} { l } { 0 } \\ { 2 } \end{array} } } )$

(c) Show that in (a) and (b),all partial derivatives can be replaced by covariant derivatives. [Observe that Lie differentiation is defined independently of the existence of an affine connection.For more information, see,for example,Bishop and Goldberg (l968） and Schouten (1954)].

# Exercise 21.9. EXPRESSION FOR DYNAMIC COMPONENTS OF THE CURVATURE TENSOR (exercise provided by J.W. York, Jr.)

The Gauss-Codazzi equations can be viewed as giving l4 of the 20 algebraically independent components of the spacetime curvature tensor in terms of the intrinsic and extrinsic geometry of three-dimensional (non-null） hypersurfaces.In order to accomplish a space-plus-time splitting of the Hilbert Lagrangian ${ \sqrt { - g } } ^ { \left( + \right) } R$ ,one must express,in addition.the remaining

6 components of the curvature tensor in an analogous manner. It is convenient for this purpose to express all tensors as spacetime tensors.and to use Lie derivation in the direction of the timelike unit normal field of the spacelike hypersurfaces as a generalized notion of time differentiation. A number of preliminary results must be proven:

$$
{ \pmb { \mathscr { L } } } _ { u } g _ { \mu \nu } = u _ { \mu ; \nu } + u _ { \nu ; \mu } ,
$$

$$
\begin{array} { r } { \mathbf { \mathcal { L } } _ { u } ( g _ { \mu \nu } + u _ { \mu } u _ { \nu } ) \equiv \mathbf { \mathcal { L } } _ { u } ( \gamma _ { \mu \nu } ) \qquad } \\ { = u _ { \mu ; \nu } + u _ { \nu ; \mu } + u _ { \mu } a _ { \nu } + a _ { \mu } u _ { \nu } , } \end{array}
$$

where $\gamma _ { \mu \nu }$ is the metric of the spacelike hypersurface,expressed in the spacetime coordinate basis, and $a ^ { \mu } \equiv u ^ { \lambda } \Gamma _ { \lambda } u ^ { \mu }$ is the curvature vector (4-acceleration) of the timelike normal curves whose tangent field is $u ^ { \mu }$ .(Recall that $u _ { \mu } a ^ { \mu } = 0 .$ ）

(c) Prove that the extrinsic curvature tensor is given by

$$
K _ { \mu \nu } = - \frac { 1 } { 2 } \mathfrak { L } _ { u } \gamma _ { \mu \nu } .
$$

(d) The unit tensor of projection into the hypersurface is defined by

$$
\perp _ { \nu } ^ { \mu } \equiv \delta _ { \nu } ^ { \mu } + u ^ { \mu } u _ { \nu } .
$$

In terms of $\perp$ show that one can write

$$
u _ { \alpha ; \beta } \equiv - K _ { \alpha \beta } - \omega _ { \alpha \beta } - a _ { \alpha } u _ { \beta } ,
$$

where

$$
K _ { \alpha \beta } = - \perp _ { \alpha } ^ { \mu } \perp _ { \beta } ^ { \nu } u _ { ( \mu ; \nu ) }
$$

and

$$
\omega _ { \alpha \beta } = - \perp _ { \alpha } ^ { \mu } \perp _ { \beta } ^ { \nu } u _ { [ \mu ; \nu ] } .
$$

(e) From the fact that $u ^ { \mu }$ is the unit normal field for a family of spacelike hypersurfaces, show that $\omega _ { \alpha \beta } = 0$

(f）The needed tools are now on hand. To obtain the result: (i) Write down $\pmb { \mathscr { L } } _ { \pmb { \mu } } K _ { \pmb { \mu } \pmb { \mu } }$ (see exercise 21.8); (ii） Insert this expression into the Ricci identity in the form

$$
u ^ { \sigma } \nabla _ { \sigma } \nabla _ { \mu } u _ { \nu } = u ^ { \sigma } \nabla _ { \mu } \nabla _ { \sigma } u _ { \nu } + { } ^ { ( 4 ) } R _ { \rho \nu \mu \sigma } u ^ { \sigma } u ^ { \rho } ;
$$

(iii) Project the two remaining free indices into the hypersurface using $\perp$ , and show that one obtains

$$
\begin{array} { r } { \begin{array} { r l } & { \perp _ { \alpha } ^ { \mu } \perp _ { \beta } ^ { \rho ( 4 ) } R _ { \mu \nu \rho \sigma } u ^ { \nu } u ^ { \sigma } = \mathfrak { L } _ { u } K _ { \alpha \beta } + K _ { \alpha \gamma } K _ { \beta } ^ { \gamma } } \\ & { \qquad + \ ^ { ( 3 ) } \nabla _ { ( \alpha } a _ { \beta ) } + a _ { \alpha } a _ { \beta } , } \end{array} } \end{array}
$$

where $^ { ( 3 ) } \nabla _ { \alpha } a _ { \beta } \equiv \perp _ { \alpha } ^ { \mu } \perp _ { \beta } ^ { \nu } \nabla _ { \mu } a _ { \nu }$ can be shown to be the thre-dimensional covariant derivative of $a _ { \beta }$ . In Gaussian normal coordinates, show that one obtains from this result

$$
R _ { 0 i 0 j } = \frac { \partial } { \partial t } K _ { i j } + K _ { i k } K _ { j } ^ { k } .
$$

(g）Finally,in the construction of ${ } ^ { ( 4 ) } R ,$ one needs to show that

$$
\gamma ^ { \mu \nu } [ { } ^ { ( 3 ) } \nabla _ { ( \mu } a _ { \nu ) } + a _ { \mu } a _ { \nu } ] = g ^ { \mu \nu } [ { } ^ { ( 3 ) } \nabla _ { ( \mu } a _ { \nu ) } + a _ { \mu } a _ { \nu } ] = a _ { ; \lambda } ^ { \lambda } .
$$

# Exercise 21.10.EXPRESSION OF ${ ^ { ( 4 ) } { R ^ { i } } _ { n i n } }$ INTERMS OF EXTRINSIC CURVATURE，PLUS A COVARIANT DIVERGENCE (exercise provided by K. Kuchar)

Let $\pmb { \alpha } ^ { \prime }$ be an arbitrary smooth set of four coordinates, not necesarily coordinated in any way with the choice of the l-parameter family of hypersurfaces.

(a) Show that

$$
^ { ( 4 ) } { \cal R } ^ { i } { } _ { n i n } = g ^ { \alpha ^ { * } \gamma ^ { \prime } } n ^ { \beta ^ { \prime } } ( n _ { \alpha ^ { \prime } ; \beta ^ { \prime } \gamma ^ { \prime } } - n _ { \alpha ^ { \prime } ; \gamma ^ { \prime } \beta ^ { \prime } } ) .
$$

(b) Show that the covariant divergences

$$
( n ^ { \beta ^ { \prime } } n ^ { \gamma } { } _ { ; \beta ^ { \prime } } ) _ { ; \gamma ^ { \prime } }
$$

and

$$
- ( n ^ { \beta ^ { \prime } } n ^ { \gamma ^ { \prime } } { } _ { ; \gamma ^ { \prime } } ) _ { ; \beta ^ { \prime } }
$$

can be removed from this expresson in such a way that what is left behind contains only first derivatives of the unit normal vector $\pmb { n }$

(c) Noting that the basis vectors $\pmb { e _ { i } }$ and $\pmb { n }$ form a complete set, justify the formula

$$
g ^ { \beta ^ { \prime } \mu ^ { \prime } } = e _ { \mathrm { i } } ^ { \beta ^ { \prime } } \omega ^ { i \mu ^ { \prime } } + ( n \cdot n ) ^ { - 1 } n ^ { \beta ^ { \prime } } n ^ { \mu ^ { \prime } } ,
$$

where $\omega ^ { i }$ is the 1-form dual to $\pmb { e } _ { i }$

(d) Noting that $n _ { \alpha ^ { \prime } ; \beta ^ { \prime } } n ^ { \alpha ^ { \prime } } = 0$ and

$$
K _ { i j } = - e _ { i \alpha ^ { \prime } } n ^ { \alpha ^ { \prime } } { } _ { ; \beta ^ { \prime } } e _ { j } { } ^ { \beta ^ { \prime } } ,
$$

show that

# s21.6. THE HILBERT ACTION PRINCIPLE AND THE ARNOWITT-DESER-MISNER MODIFICATION THEREOF IN THE SPACE-PLUS-TIME SPLIT

For analyzing the dynamics, it happily proves unnecessary to possess the missing formula for ${ ^ { ( 4 ) } R ^ { n } } _ { i n k }$ . It is essential, however, to have the Lagrangian density,

$$
1 6 \pi \mathcal { L } _ { \mathrm { g e o m } } = ( - { ^ { ( 4 ) } g } ) ^ { 1 / 2 ( 4 ) } R ,
$$

in the Hilbert action principle as the heart of all the dynamic analysis. In the present ADM(l962） notation, this density has the form

$$
\begin{array} { r l } & { ( - ^ { ( 4 ) } g ) ^ { 1 / 2 ( 4 ) } R = ( - ^ { ( 4 ) } g ) ^ { 1 / 2 } [ ^ { ( 4 ) } R ^ { i } { } _ { i j } + 2 ^ { ( 4 ) } R ^ { i } { } _ { i n } ] } \\ & { \qquad = ( - ^ { ( 4 ) } g ) ^ { 1 / 2 } [ R + ( n \cdot n ) ( \mathrm { T r } K ^ { 2 } - ( \mathrm { T r } K ) ^ { 2 } ) + 2 ( n \cdot n ) ^ { ( 4 ) } R ^ { i } { } _ { n i n } ] . } \end{array}
$$

Kuchai (l971b;see also exercise 21.10) shows how to calculate a sufficient part of this quantity without calculating all of it. The difference between the “sufficient part” and the “whole” is a time derivative plus a divergence, a quantity of the form

Drop a complete derivative from the Hiibert action principle to get the ADM principle

$$
\lbrack ( - ^ { ( 4 ) } g ) ^ { 1 / 2 } A ^ { \alpha } ] _ { , \alpha } = ( - ^ { ( 4 ) } g ) ^ { 1 / 2 } A ^ { \alpha } { } _ { ; \alpha } .
$$

When one multiplies (21.83) by dt $d x ^ { 1 } \ d x ^ { 2 } \ d x ^ { 3 }$ and integrates to obtain the action integral, the term (21.85) integrates out to a surface term. Variations of the geometry interior to this surface make no difference in the value of this surface term.Therefore it has no influence on the equations of motion to drop the term (21.85). The result of the calculation (exercise 21.10) is simple: what is left over after dropping the divergence merely changes the sign of the terms in Tr $\pmb { K } ^ { 2 }$ and $( \operatorname { T r } \pmb { K } ) ^ { 2 }$ in (21.84). Thus the variation principle becomes

$$
\begin{array} { r l } & { \mathrm { ( e x t r e m u m ) } = I _ { \mathrm { m o d i f i e d } } = \displaystyle \int \mathcal E _ { \mathrm { m o d i f i e d } } d ^ { 4 } x } \\ & { \quad = ( 1 / 1 6 \pi ) \displaystyle \int [ R + ( { \pmb n } \cdot { \pmb n } ) ( ( \mathrm { T r } K ) ^ { 2 } - \mathrm { T r } K ^ { 2 } ) ] N g ^ { 1 / 2 } d t d ^ { 3 } x + \displaystyle \int \mathcal E _ { \mathrm { f i e l d s } } d ^ { 4 } x . } \end{array}
$$

This expression,rephrased, is the starting point for Arnowitt, Deser,and Misner's analysis of the dynamics of geometry.

Two supplements from a paper of York (1972b; see also exercise 21.9) enlarge one's geometric insight into what is going on in the foregoing analysis. First, the tensor of extrinsic curvature lets itself be defined [see also Fischer (l971)] most naturally in the form

$$
K = - \frac { 1 } { 2 } \pmb { \mathscr { z } } _ { n } \pmb { g } ,
$$

where $\pmb { g }$ is the metric tensor of the 3-geometry, $\pmb { n }$ is the timelike unit normal field, and $\pmb { \mathscr { k } }$ is the Lie derivative as defined in exercise 21.8.Second,the divergence (21.85), which has to be added to the Lagrangian of (21.86) to obtain the full Hilbert Lagrangian, is

$$
- 2 [ ( - ^ { ( 4 ) } g ) ^ { 1 / 2 } ( n ^ { \alpha ^ { \prime } } \mathrm { T r } K + a ^ { \alpha ^ { \prime } } ) ] _ { , \alpha ^ { \prime } } ,
$$

where the coordinates are general (see exercise 21.l0), and

$$
a ^ { \alpha ^ { \prime } } = n ^ { \alpha ^ { \prime } } { } _ { ; \beta ^ { \prime } } n ^ { \beta ^ { \prime } }
$$

is the 4-acceleration of an observer traveling along the timelike normal $\pmb { n }$ to the successive slices.

# $\$ 21.7$ ． THE ARNOWITT，DESER,AND MISNER FORMULATION OF THE DYNAMICS OF GEOMETRY

Dirac (1959,1964,and earlier references cited therein) formulated the dynamics of geometry in a $( 3 + 1 )$ -dimensional form,using generalizations of Poisson brackets and of Hamilton equations.Arnowitt, Deser,and Misner instead made the Hilbert-Palatini variational principle the foundation for this dynamics. Because of its simplicity, this ADM (l962) approach is followed here.The gravitational part of the integrand in the Hilbert-Palatini action principle is rewritten in the condensed but standard form (after inserting a $1 6 \pi$ that ADM avoid by other units) as

$$
\begin{array} { r } { { 1 } 6 \pi \mathcal { E } _ { \mathrm { g e o m t r u e } } = \mathcal { E } _ { \mathrm { g e o m A D M } } = - g _ { i j } \partial \pi ^ { i j } / \partial t - N \mathcal { K } - N _ { \mathrm { i } } \mathcal { K } ^ { i } } \\ { - 2 \left[ \pi ^ { i j } N _ { j } - \displaystyle \frac { 1 } { 2 } N ^ { i } \mathrm { T r } \pi + N ^ { | i } ( g ) ^ { 1 / 2 } \right] _ { \mathrm { , i } } . } \end{array}
$$

Here each item of abbreviation has its special meaning and willplay its special part, a part foreshadowed by the name now given it:

$$
\pi _ { \mathrm { t r u e } } ^ { \mathrm { i } j } = \frac { \delta ( \mathrm { a c t i o n } ) } { \delta g _ { i j } } = \left( \begin{array} { l } { \mathrm { ' g e o m e t r o d y n a m i c } } \\ { \mathrm { f i e l d ~ m o m e n t u m ' ~ d y n - } } \\ { \mathrm { a m i c a l l y ~ c o n j u g a t e ~ t o } } \\ { \mathrm { t h e ~ ' g e o m e t r o d y n a m i c } } \\ { \mathrm { f i e l d ~ c o o r d i n a t e ' ~ } g _ { \mathrm { i j } } } \end{array} \right) = \frac { \pi ^ { i j } } { 1 6 \pi } ; \pi ^ { i j } = g ^ { 1 / 2 } ( g ^ { \mathrm { i } j } \mathrm { T r } K - K ^ { i j } )
$$

(here the $\pi ^ { i j }$ of ADM is usually more convenient than $\pi _ { \mathrm { t r u e } } ^ { i j } )$ ; and

$$
\begin{array} { r l } & { \mathcal { K } _ { \mathrm { t r u e } } = \mathcal { K } ( \pi _ { \mathrm { t r u e } } ^ { \mathrm { i j } } , g _ { \mathrm { i j } } ) = ( ^ { \ast } \mathrm { s u p e r - H a m i l t o n i a n } ^ { \prime \ast } ) = \mathcal { K } / 1 6 \pi ; } \\ & { \mathcal { K } ( \pi ^ { i j } , g _ { \mathrm { i j } } ) = g ^ { - 1 / 2 } \left( \mathrm { T r } \pi ^ { 2 } - \displaystyle \frac { 1 } { 2 } ( \mathrm { T r } \pi ) ^ { 2 } \right) - g ^ { 1 / 2 } R ; } \end{array}
$$

and

$$
1 6 \pi \mathcal { K } _ { \mathrm { t r u e } } ^ { i } = \mathcal { K } ^ { i } = \mathcal { K } ^ { i } ( \pi ^ { i j } , g _ { i j } ) = ( ^ { \ast \ast } \mathrm { s u p e r m o m e n t u m } ^ { \ast } ) = - 2 \pi ^ { i k } | _ { k } \mathrm { . }
$$

Here the covariant derivative is formed treating $\pi ^ { i k }$ as a tensor density,as its definition in (21.91） shows it to be (see $\ S 2 1 . 2 )$ . The quantities to be varied to extremize the action are the coefficients in the metric of the 4-geometry,as follows: the six $g _ { i j }$ and the lapse function $N$ and shift function $N _ { i }$ ; and also the six “geometrodynamic momenta,” $\pi ^ { i j }$ .To vary these momenta as well as the metric is (l) to follow the patern of elementary Hamiltonian dynamics (Box 21.1), where, by taking the momentum $p$ to be as independently variable as the coordinate $x$ ,one arrives at two Hamilton equations of the first order instead of one Lagrange equation of the second order, and (2) to follow in some measure the lead of the Palatini variation principle of $\ S 2 1 . 2$ . There， however, one had 40 connection coeffcients to vary, whereas here one has come down to only six $\pi ^ { i j }$ .To know these momenta and the 3-metric is to know the extrinsic curvature. Before carrying out the variation, drop the divergence $- 2 [ \mathrm { ~ \textit ~ { ~ l ~ } ~ } , $ from (21.9O), since it gives rise only to surface integrals and therefore in no way affects the equations of motion that will come out of the variational principle. Also rewrite the first term in (21.9O) in the form

$$
- ( \partial / \partial t ) ( g _ { i j } \pi ^ { i j } ) + \pi ^ { i j } \partial g _ { i j } / \partial t ,
$$

and drop the complete time-derivative from the variation principle,again because it is irrelevant to the resulting equations of motion. The action principle now takes the form

$$
\begin{array} { r } { \mathrm { \ e x t r e m u m = } I _ { \mathrm { t r u e } } = I _ { \mathrm { A D M } } / 1 6 \pi \mathrm { \phantom { - } } } \\ { = ( 1 / 1 6 \pi ) \int [ \pi ^ { \mathrm { i } j } \partial g _ { \mathrm { i j } } / \partial t - N \mathcal { K } ( \pi ^ { \mathrm { i j } } , g _ { \mathrm { i j } } ) - N _ { \mathrm { i } } \mathcal { K } ^ { \mathrm { i } } ( \pi ^ { \mathrm { i j } } , g _ { \mathrm { i j } } ) ] d ^ { \mathrm { i } } x } \\ { + \int \mathcal { E } _ { \mathrm { f i e l d } } d ^ { \mathrm { i } } x . } \end{array}
$$

The action principle itself, here as always,tells one what must be fixed to make the action take on a well-defined value (if and when the action possesses an extremum). Apart from appropriate potentials having to do with fields other than geom-

Action principle says, fix 3-geometry on each face of sandwich

etry, the only quantities that have to be fixed appear at first sight to be the values of the six $g _ { i j }$ on the initial and final spacelike hypersurfaces.However,the ADM action principle is invariant with respect to any change of coordinates $x ^ { 1 }$ ， $x ^ { 2 }$ ， $x ^ { 3 }$ $ x ^ { \vec { 1 } }$ ， $x ^ { \frac { \overline { { 2 } } } { 2 } } ,$ $x ^ { \bar { 3 } }$ within the successive spacelike slices. Therefore the quantities that really have to be fixed on the two faces of the sandwich are the 3-geometries $( 3 ) \{ 9 ^ { \prime }$ (on the initial hypersurface) and $( 3 ) \textcircled { 8 }$ (on the final hypersurface) and nothing more.

What a 3-geometry is

In mathematical terms,a 3-geometry $( 3 ) \textcircled { 8 }$ is the“equivalence class” of a set of differentiable manifolds that are isometrically equivalent to each other under diffeomorphisms. In the terms of the everyday physicist,a 3-geometry is the equivalence class of 3-metrics $g _ { i j } ( x , y , z )$ that are equivalent to one another under coordinate transformations. In more homely terms, two automobile fenders have one and the same 2-geometry if they have the same shape,regardless of how much the coordinate rulings painted on the one may differ from the coordinate rulings painted on the other.

Electromagnetism gives example of momentum conjugate to “field coordinate"

To have in equation (21.95) an example of a field Lagrangian that is at the same time physically relevant and free of avoidable complications, take the case of a source-free electromagnetic field. It would be possible to take the field Lagrangian to have the standard Maxwell value,

$$
( 1 / 8 \pi ) ( E ^ { 2 } - B ^ { 2 } ) \longrightarrow - ( 1 / 1 6 \pi ) F _ { \mu \nu } F ^ { \mu \nu } ,
$$

with

$$
F _ { \mu \nu } = \partial A _ { \nu } / \partial x ^ { \mu } - \partial A _ { \mu } / \partial x ^ { \nu } .
$$

The variation of the Lagrangian with respect to the independent dynamic variables of the field, the four potentials $A _ { \alpha }$ ,would then immediately give the four second-order partial differential wave equations for these four potentials.However,to have instead a larger number of first-order equations is as convenient for electrodynamics as it is for geometrodynamics. One seeks for the analog of the Hamiltonian equations of particle dynamics,

$$
\begin{array} { r l } & { d x / d t = \partial H ( x , p ) / \partial p , } \\ & { } \\ & { d p / d t = - \partial H ( x , p ) / \partial x . } \end{array}
$$

One gets those equations by replacing the Lagrange integral $\textstyle \int L ( x , { \dot { x } } ) d t$ by the .Hamilton integral $\iiint p { \dot { \boldsymbol { x } } } - H ( { \boldsymbol { x } } , p ) ]$ dt.Likewise, here one replaces the action integrand of (21.96) by what in flat spacetime would be

$$
( 1 / 4 \pi ) \left[ A _ { \mu , \nu } F ^ { \mu \nu } + \frac { 1 } { 4 } F _ { \mu \nu } F ^ { \mu \nu } \right] .
$$

In actuality,spacetime is to be regarded as not only curved but also sliced up into spacelike hypersurfaces.This $( 3 + 1 )$ split of the geometry made it desirable to split the ten geometrodynamic potentials into the six $g _ { i j }$ and the four lapse and shift functions.Here one similarly splits the four $A _ { \mu }$ into the three components $A _ { i }$ of the vector potential and the scalar potential $A _ { 0 } = - \phi$ (with the sign so chosen that, in flat spacetime in a Minkowski coordinate system, $\phi = { \cal { A } } ^ { 0 }$ ).In this notation, the

Lagrange density function, including the standard density factor $( - ^ { ( 4 ) } g ) ^ { 1 / 2 }$ but dropping a complete time integral $( \partial / \partial t ) ( A _ { i } \delta ^ { i } )$ that has no influence on the equations of motion,is given by the formula

$$
\begin{array} { l } { { 4 \pi \mathcal { L } _ { \mathrm { f i e l d } } = - \mathcal { E } ^ { \mathrm { i } } \partial A _ { \mathrm { i } } / \partial t + \phi \mathcal { E } ^ { \mathrm { i } } { } _ { , \mathrm { i } } } } \\ { { \displaystyle ~ - \frac { 1 } { 2 } N g ^ { - 1 / 2 } g _ { \mathrm { i j } } ( \mathcal { E } ^ { \mathrm { i } } \mathcal { E } ^ { \mathrm { j } } + \mathcal { B } ^ { \mathrm { i } } \mathcal { B } ^ { \mathrm { j } } ) + N ^ { \mathrm { i } } [ \mathrm { i } j k ] \mathcal { E } ^ { \mathrm { j } } \mathcal { B } ^ { k } . } } \end{array}
$$

Lagrange density for electromagnetism

Here use is made of the alternating symbol $[ i j k ]$ ,defined as changing sign on the interchange of any two labels,and normalized so that $[ 1 2 3 ] = 1$ .Note that the 3-tensor $\varepsilon ^ { i j k }$ and the alternating symbol $[ i j k ]$ are related much as are the corresponding four-dimensional objects in equation (8.1O),so that one can write

$$
\mathcal { B } ^ { i } = \frac { 1 } { 2 } [ i j k ] ( A _ { k , j } - A _ { j , k } ) .
$$

The quantities ${ \mathcal { B } } ^ { i }$ are the components of the magnetic field in the spacelike slice. They are not regarded as independently variable. They are treated as fully fixed by the choice of the three potentials $A _ { i }$ .The converse is the case for the components $\delta ^ { \ i }$ of the electric field: they are treated like momenta,and as independently variable.

Extremizing the action with respect to the $\delta ^ { \dagger }$ (exercise 21.1l） gives the analog of the equation $d x / d t = p / m$ in particle mechanics,and the analog of the equation

$$
E _ { i } = - \partial A _ { i } / \partial t - \partial \phi / \partial x ^ { i }
$$

of flat-spacetime electrodynamics; namely,

$$
- \partial A _ { i } / \partial t - \phi _ { , i } - N g ^ { - 1 / 2 } g _ { i j } \xi ^ { j } - [ i j k ] N ^ { j } \xi \partial ^ { k } = 0 .
$$

The initial-value equation of electromagnetism

Here the last term containing the shift functions $N ^ { j }$ ,arises from the obliquity of the coordinate system. ADM give the follwing additional but equivalent ways to state the result (21.103):

$$
\begin{array} { l } { { \displaystyle { \mathcal { E } ^ { i } = \frac { 1 } { 2 } [ i j k ] ^ { * } F _ { j k } } } } \\ { { \displaystyle { } } } \\ { { \displaystyle { = \frac { 1 } { 2 } [ i j k ] \left\{ \frac { 1 } { 2 } [ j k \mu \nu ] ( - ^ { ( 4 ) } g ) ^ { 1 / 2 ( 4 ) } g ^ { \mu \alpha ( 4 ) } g ^ { \nu \beta } F _ { \alpha \beta } \right\} } . } } \end{array}
$$

They note that $\delta ^ { j }$ and ${ \dot { \mathfrak { B } } } ^ { j }$ are not directly the contravariant components of the felds in the simultaneity $\pmb { \Sigma }$ ，

$$
E = E ^ { j } \boldsymbol { e } _ { j } , B = B ^ { j } \boldsymbol { e } _ { j } ,
$$

but the contravariant densities,

$$
\xi ^ { j } = g ^ { 1 / 2 } E ^ { j } , \xi \beta ^ { j } = g ^ { 1 / 2 } B ^ { j } .
$$

Extremizing the action with respect to the three $A _ { i }$ (exercise 21.12） gives the curved-spacetime analog of the Maxwell equations,

$$
\partial E / \partial t = \nabla \times \pmb { B } .
$$

The remaining potential, $\phi$ ,enters the action principle at only one point. Extremizing with respect to it gives immediately the divergence relation of source-free electromagnetism.

$$
\mathcal { E } ^ { \ i } { } _ { , \ i } = 0 .
$$

Action principle tells what to fix at limits

If an action principle tells in and by itself what quantities are to be fixed at the limits,what lessons does (21.100) give on this score? One can go back to the example of particle mechanics in Hamiltonian form.as in Box 2l.1,and note that there the momentum $p$ could “flap in the breeze." Only the coordinate $x$ had to be fixed at the limits. Thus the variation of the action was

$$
\begin{array} { l } { \displaystyle \delta I = \delta \int [ p \dot { x } - H ( x , p ) ] d t } \\ { \displaystyle \quad = \int \{ [ \dot { x } - \partial H / \partial p ] \delta p + ( d / d t ) ( p \delta x ) + [ - \dot { p } - \partial H / \partial x ] \delta x \} d t . } \end{array}
$$

To arrive at a well-defined extremum of the action integral $I ,$ it was not enough to annul the coefficients,in square brackets, of $\delta p$ and $\delta x$ ; that is, to impose Hamilton's equations of motion. It was necessary in addition to annul the quantities at limits, $p \delta x$ ； that is, to specify $x$ at the start and at the end of the motion. Similarly here.The quantities $\phi$ and $\delta ^ { i }$ flap in the breeze,but the magnetic field has to be specified on the two faces of the sandwich to allow one to speak of a well-defined extremum of the action principle. Why the magnetic field, or the three quantities

At limits,fix not potentials but magnetic field itself

$$
\partial A _ { j } / \partial x ^ { i } - \partial A _ { i } / \partial x ^ { j } ;
$$

why not the three $A _ { i }$ themselves? When one varies (21.100) with respect to the $A _ { i }$ ， and integrates the variation of the first term by parts,as one must to arrive at the dynamic equations, one obtains a term at limits

$$
\int _ { { \cal { S } } _ { \mathrm { { i n i u a l } } } } \delta ^ { i } \delta A _ { i } d ^ { 3 } x - \int _ { { \cal { S } } _ { \mathrm { { i n a l } } } } \delta ^ { i } \delta A _ { i } d ^ { 3 } x .
$$

One demands that both these terms at limits must vanish in order to have a welldefined variational problem. Go from the given vector potential to another vector potential, $\boldsymbol { A } _ { i _ { \mathrm { n e w } } }$ ,by the gauge transformation

$$
A _ { \mathrm { i _ { n e w } } } = A _ { i } + \delta A _ { i } = A _ { i } + \partial \lambda / \partial x ^ { i } .
$$

The magnetic-field components given by the three $A _ { i _ { \mathrm { n e w } } }$ differ in no way from those listed in (21.110).Moreover the“variation at limits,”

$$
\int \mathcal { \delta } ^ { i } \delta A _ { i } d ^ { 3 } x = \int \mathcal { \delta } ^ { i } \partial \lambda / \partial x ^ { i } d ^ { 3 } x = - \int \lambda \mathcal { E } ^ { i } { } _ { , i } d ^ { 3 } x ,
$$

is automatically zero by virtue of the divergence condition (21.108),for any arbitrary choice of $\lambda$ .Therefore the quantities fixed at limits are not the three $A _ { i }$ themselves (mere potentials) but the physically significant quantities (21.11O),the components of the magnetic field. Moreover, the divergence condition $\mathcal { E } ^ { \ i } { } _ { , i } = 0$ now becomes the initial-value equation for the determination of the potential $\phi$

In the preceding paragraph one need only replace“the three $A _ { \mathbf { i } } ^ { \prime \prime }$ by “the six $g _ { i j } ^ { \quad \dag }$ and “the components of the magnetic field” by“the 3-geometry $( 3 ) \textcircled { \cdot } 5$ and “the potential $\phi ^ { \dag }$ by “the lapse and shift functions $N$ and $N ^ { i } { } ^ { * }$ to pass from electrodynamics to geometrodynamics.

With this parallelism in view, turn back to the variational principle (21.95) of general relativity in the ADM formulation.With the 3-geometry fixed on the two faces of the sandwich, vary conditions in between to extremize the action, varying in turn the $\pi ^ { i j }$ the $g _ { i j } ,$ 、and the lapse and shift functions.The geometrodynamic momenta appear everywhere only algebraically in the action principle,except in the term $- 2 N _ { \mathfrak { i } } \pi ^ { i j } { } _ { | j \cdot }$ Variation and integration by parts gives $2 N _ { \mathfrak { i } \mathfrak { j } } \delta \pi ^ { \mathfrak { i } \mathfrak { j } }$ .Collecting coefficients of $\delta \pi ^ { i j }$ and annuling the sum of these coeffcients, one arrives at one of the several conditions required for an extremum,

# ADM principle reproduces formula for geometrodynamic momentum

$$
\partial g _ { i j } / \partial t = 2 N g ^ { - 1 / 2 } \left( \pi _ { i j } - \frac { 1 } { 2 } g _ { i j } \mathrm { T r } \eta \right) + N _ { i | j } + N _ { j | i } .
$$

This result agrees with what one gets from equations (21.91) defining geometrodynamic momentum in terms of extrinsic curvature, together with expression (21.67) for extrinsic curvature in terms of lapse and shift. The result (21.i14) here is no less useful than the result

$$
d x / d t = \partial H ( x , p ) / \partial p = p / m
$$

in the most elementary problem in mechanics: it marks the first step in spliting a second-order equation or equations into twice as many first-order equations.

Now vary the action with respect to the $g _ { i j }$ and again, after appropriate integration by parts and rearrangement, find the remaining first-order dynamic equations of general relativity [simplified by use of equations (21.116) and (21.117)],

Dynamic and initial-value equations out of ADM formalism

$$
\begin{array} { l } { { \displaystyle \partial \pi ^ { i j } / \partial t = - N g ^ { 1 / 2 } ( R ^ { i j } - \frac { 1 } { 2 } g ^ { i j } R ) + \frac { 1 } { 2 } \ N g ^ { - 1 / 2 } g ^ { i j } ( \mathrm { T r } \pi ^ { 2 } - \frac { 1 } { 2 } ( \mathrm { T r } \pi ) ^ { 2 } ) } } \\ { ~ - ~ 2 N g ^ { - 1 / 2 } ( \pi ^ { i m } \pi _ { m } ^ { ~ j } - \frac { 1 } { 2 } \pi ^ { i j } \mathrm { T r } \pi ) }  \\ { { ~ + ~ g ^ { 1 / 2 } ( N ^ { | i j } - g ^ { \mathrm { i } j } N ^ { | m } | m ) ~ + ~ ( \pi ^ { \mathrm { i } j } N ^ { m } ) _ { | m } } } \\ { { ~ - ~ N _ { ^ { \prime } | m } ^ { \mathrm { i } } \pi ^ { m j } - N _ { ^ { \prime } | m } ^ { \mathrm { i } } \pi ^ { m i } + [ \mathrm { o t h e r ~ t h a n ~ g e o m e t r y , ~ o m i t e d ~ h e r e ~ \mathrm { f o r } ~ } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } } } \\   \displaystyle \mathrm { s i n g ~ l i c i t y } , ~ \mathrm { b u t ~ d i s c a s e } \mathrm { b e q u } \mathrm { ~ b y ~ A n d ~ \mathrm { \scriptsize ~ ( 1 ) } } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm { f o r } \mathrm  f o r  \end{array}
$$

Finally extremize the action (21.95） with respect to the lapse function $N$ and the shift functions $N _ { i }$ ，and find the four so-called initial-value equations of general relativity,equivalent to (21.77) and (21.81) or to $G _ { n } ^ { \alpha } = 8 \pi T _ { n } ^ { \alpha }$ ；thus,

$$
\begin{array} { r l } & { - ( 1 / 1 6 \pi ) \mathcal { V } ( \pi ^ { i j } , g _ { i j } ) = ( 1 / 8 \pi ) N g ^ { - 1 / 2 } g _ { i j } ( \mathcal { E } ^ { i } \mathcal { E } ^ { j } + \mathcal { B } ^ { i } \mathcal { B } ^ { j } ) , } \\ & { \qquad - ( 1 / 1 6 \pi ) \mathcal { V } ^ { i } ( \pi ^ { i j } , g _ { i j } ) = - ( 1 / 4 \pi ) [ i j k ] \mathcal { E } ^ { j } \mathcal { B } ^ { k } . } \end{array}
$$

# Exercise 21.11. FIRST EXPLOITATION OF THE ADM VARIATIONAL PRINCIPLE FOR THE ELECTROMAGNETIC FIELD

Extremize the action principle (21.100) with respect to the $\delta ^ { i }$ and derive the result (21.103).

Exercise 21.12. SECOND EXPLOITATION OF THE ADM VARIATIONAL PRINCIPLE FOR THE ELECTROMAGNETIC FIELD

Extremize (21.100) with respect to the $A _ { i }$ and verify that the resulting equations in any Minkowski-flat region are equivalent to (21.107).

# Exercise 21.13. FARADAY-MAXWELL SOURCE TERM IN THE DYNAMIC EQUATIONS OF GENERAL RELATIVITY

Evaluate the final indicated source terms in (21.l15) from the Lagrangian (21.100)of Maxwell electrodynamics, regarded as a function of the A and the gif

# Exercise 21.14. THE CHOICE OF $\phi$ DOESN'T MATTER

Prove the statement in the text that the dynamic development of the electric and magnetic fields themselves is independent of the choice made for the scalar potential $\phi ( t , x , y , z )$ in the analysis (a) in flat spacetime in Minkowski coordinates and (b) in general relativity, according to equations (21.l03),and (21.107) as generalized in exercise 21.12.

# Exercise 21.15. THE CHOICE OF SLICING OF SPACETIME DOESN'T MATTER

Given a metric ${ ^ { ( 3 ) } g _ { i j } ( x , y , z ) }$ and an extrinsic curvature $K ^ { i j } ( x , y , z )$ on a spacelike hypersurface $\pmb { \tau }$ ,and given that these quantities satisfy the initial-value equations (21.l16) and (21.117), and given two alternative choices for the lapse and shift functions $( N , N _ { \mathfrak { i } } )$ and $( N + \delta N _ { \cdot }$ 、 $N _ { \mathrm { i } } + \delta N _ { \mathrm { i } } )$ , show that the curvature itself (as distinguished from its components in these two distinct coordinate systems),as calculated at a point $\mathscr { P }$ a“little way”(first order of small quantities) off the hypersurface,by way of the dynamic equations (21.l14) and (21.115), is independent of this choice of lapse and shift.

# S21.8. INTEGRATING FORWARD IN TIME

In the Hamiltonian formalism of Arnowit, Deser, and Misner [see also the many papers by many workers on the quantization of general relativity-primarily puting Einstein's theory into Hamiltonian form-cited,for example, in references l and 2 of Wheeler (1968),the dynamics of geometry takes a form quite similar to the Hamiltonian dynamics of geometry. There one gives $x$ and $p$ at a starting time and integrates two first-order equations for $d x / d t$ and $d p / d t$ ahead in time to find these dynamically conjugate variables at allfuture times. Here one gives appropriate values of $g _ { i j }$ and $\pi ^ { i j }$ over an initial spacelike hypersurface and integrates the two first-order equations (21.114) and (21.1i5) ahead in time to find the geometry at future times. For example, one can rewrite the differential equations as difference equations according to the practice by now familiar in modern hydrodynamics,and then carry out the integration on an electronic digital computer of substantial memory capacity.

Time in general relativity has a many-fingered quality very different from the one-parameter nature of time in nonrelativistic particle mechanics [see, however, Dirac,Fock,and Podolsky (1932) for a many-time formalism for treating the relativistic dynamics of a system of many interacting particles]. He who is studying the geometry is free to push ahead the spacelike hypersurface faster at one place than another,so long as he keeps it spacelike.This freedom expresses itself in the lapse function $N ( t , x , y , z )$ at each stage,t, of the integration. Equations (21.114) and (21.115) are not a conduit to feed out information on $N$ to the analyst. They are a conduit for the analyst to feed in information on $N .$ The choice of $N$ is to be made, not by nature,but by man.The dynamic equations cannot begin to fulfill their purpose until this choice is made.The “time parameter” $t$ is only alabel to distinguish one spacelike hypersurface from another in a one-parameter family of hypersurface; but $N$ thus tells the spacing in proper time,as it varies from place to place, between the successive slices on which one chooses to record the time-evolution of the geometry. A cinema camera can record what happens only one frame at a time, but the operator can make a great difference in what that camera sees by his choice of angle for the flming of the scene. So here, with the choice of slicing.

Another choice is of concern to the analyst, especially one doing his analysis on a digital computer. He is in the course of determining,via (21.114-21.115) written as difference equations, what happens on a lattice work of points, typified by x = ...,73,74,75,76,77,...,etc. He finds that the curvatures are developing most strongly in a localized region in the range around $x = 8 3$ to $x = 8 9$ He wants to increase the density of coverage of his tracer points in this region. He does so by causing points at lesser and greater $x$ values to drift into this region moment by moment as $t$ increases: $t = \ldots , 1 2 2$ ,123,124,....He makes the tracer points at lesser $x$ -values start to move to the right $\mathrm { { \cal N } } _ { 1 }$ positive) and points at greater $x$ -values move to the left ( $\mathbf { \cal { N } } _ { 1 }$ negative). In other words, the choice of the three shift functions $N _ { \mathrm { i } } ( t , x , y , z )$ is just as much the responsibility of the analyst as is the choice of the lapse function $N .$ The equations will never tell him what to pick.He has to tell the equations.

These options,far from complicating dynamic equations (21.114-21.115),make them flexible and responsive to the wishes of the analyst in following the course of whatever geometrodynamic process is in his hands for study.

The freedom that exists in general relativity in the choice of the four functions $N , N _ { i } ,$ is illuminated from another side by comparing it with the freedom one has in electrodynamics to pick the one function $\phi ( t , x , y , z )$ ,the scalar potential. In no way do the dynamic Maxwell equations (21.103) and (21.107),as generalized in exercise 21.12 determine $\phi$ . Instead they demand that it be determined (by the analyst) as the price for predicting the time-development of the vector potential $A _ { i }$ An altered choice of $\phi ( t , x , y , z )$ in its dependence on position and time means altered results from the dynamic equations for the development of the three $A _ { i }$ in time and space.However, the physically significant quantities, the electric and magnetic fields themselves on successive hypersurfaces, come out the same (exercise 21.14) regardless of this choice of $\phi$ 、Similarly in geometrodynamics: an altered choice for the four

Lapse and shift chosen to. push forward the integration in time as one finds most convenient

![](images/3788a0f515426125cfa64c26557d55229f25c02b8f463c91412cdf2068105220.jpg)  
Figure 21.4. Some of the many ways to make distinct spacelike slices through one and the same $( 4 ) g$ the complete Schwarzschild 4-geometry.

functions $N , N _ { i }$ ,means (a) an altered laying down of coordinates in spacetime,and therefore (b)altered results for the intrinsic metric $^ { ( 3 ) } g _ { i j }$ and extrinsic curvature $K ^ { i j }$ of successive spacelike hypersurfaces, but yields the same 4-geometry $( 4 ) \log$ (Figure 21.4) regardless of this choice of coordinatization (exercise 21.15).

Initial-value data: what is freely disposable? and what is thereby fixed?

# S21.9. THE INITIAL-VALUE PROBLEM IN THE THIN-SANDWICH FORMULATION

Given appropriate initial-value data,one can integrate the dynamic equations ahead in time and determine the evolution of the geometry; but what are “appropriate initial-value data"? They are six functions $^ { ( 3 ) } g _ { i j } ( x , y , z )$ plus six more functions $\pi ^ { i j } ( x , y , z )$ or $K ^ { i j } ( x , y , z )$ that together satisfy the four initial-value equations (21.116) and (21.117). To be required to give coordinates and momenta accords with the familiar plan of Hamiltonian mechanics; but to have consistency conditions or “constraints” imposed on such data is less familiar.A particle moving in two-dimensional space is catalogued by coordinates $x , y ;$ and coordinates $p _ { z } , p _ { y } ,$ but a particle forced to remain on the circle $x ^ { 2 } + y ^ { 2 } = a ^ { 2 }$ satisfies the constraint $x p _ { z } + y p _ { y } = 0$ Thus the existence of a“constraint” is a signal that the system possesses fewer degrees of freedom than one would otherwise suppose. Fully to analyze the four “initialvalue”or “constraint” conditions (21.116) and (21.117) is thus to determine (l) how many dynamic degrees of freedom the geometry possesses and (2) what these degrees of freedom are; that is to say， precisely what “handles” one can freely adjust to govern completely the geometry and its evolution with time.The counting one can do today, with the conclusion that the geometry possesses the same count of true degrees of freedom as the electromagnetic field.The identification of the“handles,” or freely adjustable features of the dynamics, is less advanced for geometry than it is for electromagnetism $( \mathbf { B o x } 2 1 . 2 )$ , but most instructive so far as it goes.

Byrights the identification of the degrees of freedom of the field,whether that of Einstein or that of Faraday and Maxwell, requires nothing more than knowing what must be fixed on initial and final spacelike hypersurfaces to make the appropriate variation principle well-defined. One then has the option whether (l) to give that quantity on both hypersurfaces or (2) to give that quantity and its dynamic conjugate on one hypersurface or (3) to give the quantity on both hypersurfaces, as in (l),but go to the limit of an infinitely thin sandwich,so that one ends up specifying the quantity and its time rate of change on one hypersurface. This third “thin sandwich”procedure is simplest for a quick analysis of the initial-value problem in both electrodynamics and geometrodynamics. Take electrodynamics first, as an illustration.

Give the divergence-free magnetic field andits time-rate of change: on an arbitrary smooth spacelike hypersurface in curved spacetime in the general case; on the hypersurface $t = 0$ in Minkowski spacetime in the present illustrative treatment,

In electromagnetism,give magnetic field and its rate of change as initial data

$$
{ \mathcal B } ^ { i } ( 0 , x , y , z ) { \mathrm { ~ g i v e n } } ,
$$

$$
{ \dot { \mathcal { B } } } ^ { i } ( 0 , x , y , z ) = \left( { \frac { \partial { \mathcal { B } } ^ { i } } { \partial t } } \right) { \mathrm { a l s o ~ g i v e n . } }
$$

These quantities together contain four and only four independent data per space point. How is one now to obtain the momenta $\pi ^ { i } \sim - \mathcal { E } ^ { i }$ so that one can start integrating the dynamic equations (21.103) and (21.107) forward in time?(l） Find a set of three functions $A _ { i } ( 0 , x , y , z )$ such that their curl gives the three specified ${ \mathcal { B } } ^ { i }$ .That_this can be done at all is guaranteed by the vanishing of the divergence ${ \widehat { \mathcal { B } } } _ { , i } ^ { i } .$ However, the choice of the $A _ { i }$ is not unique. The new set of potentials $A _ { i n e w } =$ $\mathcal { A } _ { i } + \partial \lambda / \partial x ^ { i }$ with arbitrary smooth $\lambda$ ，provide just as good a solution as the original $A _ { i }$ .No matter.Pick one solution and stick to it.(2) Similarly, find a set of three $\dot { A } _ { i } ( 0 , x , y , z )$ such that their curl gives the specified $\dot { \mathcal { B } } ^ { i } ( 0 , x , y , z )$ ，and resolve all arbitrariness of choice by fiat.(3) Recall that the electric field (negative of the feld momentum） is given by

$$
\mathcal { E } _ { i } = - \dot { A } _ { i } - \partial \phi / \partial x ^ { i }
$$

(formula valid without amendment only in flat space).The initial-value or constraint equation $\mathcal { E } ^ { i } { } _ { , i } = 0$ translates to the form

$$
\begin{array} { r } { \nabla ^ { 2 } \phi = - \eta ^ { i j } \dot { A } _ { i , j } . } \end{array}
$$

# A. First Approach: Number of "Field Coordinates" per Spacepoint

Superficial tally of the degrees of freedom of the source-free electromagnetic field gives three field coordinates $A _ { i } ( x , y , z )$ per spacepoint on the initial simultaneity ,plus three field momenta rue $\pi ^ { i } / 4 \pi$ [with $\pi ^ { i } = - \mathcal { E } ^ { i } ( x , y , z ) ]$ per spacepoint.

Closer inspection reveals that the number of coordinate degrees of freedom per spacepoint is not three but two. Thus the change in vector potential $A _ { i } \longrightarrow A _ { i } + \hat { \partial } \lambda / \hat { c } x ^ { i }$ makes no change in the actual physics, the magnetic field components,

$$
B ^ { i } = \frac { 1 } { 2 } [ i j k ] ( \partial A _ { k } / \partial x ^ { j } - \partial A _ { j } / \partial x ^ { k } ) .
$$

Moreover, though those components are three in number, they satisfy one condition per spacepoint, $\mathcal { B } _ { \mathrm { ~ , ~ } i } ^ { i } = 0$ thusreducingheeffecivetnbr of coordinate degrees of freedom per spacepoint to two.

The momentum degrees of freedom per spacepoint are likewise reduced from three to two by the one condition per spacepoint $\mathcal { E } ^ { i } { } _ { , i } = 0$

In curved spacetime,Fourier analysis is a less convenient way of identifying the degrees of freedom of the electromagnetic field [for such a Fourier analysis, see Misner and Wheeler (l957),especially their Table X and following text] than direct analysis in space,as above.

# C. Another Alternative: Analyze "Deformation of Structure"

Still a third way to get a handle on the degrees of freedom of a divergence-free field,whether $\pmb { \mathcal { E } }$ or $\boldsymbol { \mathcal { B } }$ ,rests on the idea of deformation of structure [diagram from Wheeler (1964)). Represent the

![](images/e4308d8a0fda4e92335227f98975a40d7e292c2c0b2c8f47351af4e1dd2adb91.jpg)

# B． Alternative Approach: Count Fourier Coefficients

In textbooks on field theory [see,for example, Wentzel (l949)], attention focuses on flat spacetime. The electromagnetic field is decomposed by Fourier analysis into individual running waves. Instead of counting degrees of freedom per point in coordinate space， one does the equivalent: counts up degrees of freedom per point in wavenumber space. Thus for each $( k _ { z } , k _ { y } , k _ { z } )$ ,there are two independent states of polarization. Each state of polarization requires for its description an amplitude("coordinate") and time-rate of change of amplitude ("momentum") at the initial time, $t _ { 0 } ^ { \prime }$ Thus the number of degrees of freedom per point in wave-number space is two for coordinates and two for momenta, in accord with what one gets by carrying out the count in coordinate space.

magnetic field by Faraday's picture of lines of force (a) continuing through space without ever ending, automatic guarantee that ${ \mathcal B } _ { , i } ^ { i }$ is everywhere zero.Insert “knitting needles”(b) into the spaghetti-like structure of the lines of foree and move these needles as one will. Sliding the “knitting needles”along a line of force causes no movement of the line of force. (c) With the help of two knitting needles perpendicular to each other and to the line of force,one can give any given line of force any small displacement one pleases perpendicular to its length: again two degrees of freedom per spacepoint. Granted any non-zero field to begin with, no matter how small, one can build it up by a sequence of such small deformations to agree with any arbitrary field pattern of zero divergence,no matter what its complexity and strength may be.

Solve for $\phi$ 、Then (4) equation (21.120） gives the initial-value electric field,or electrodynamic field momentum $\pi ^ { i } \sim - \delta ^ { i }$ ,required (along with the field coordinate $A _ { i } )$ for starting the integration of the dynamic equations (21.103) and (21.107). [Misner and Wheeler (l957) deal with the additional features that come in when the space is multiply connected. Each wormhole or handle of the geometry is able to trap electric lines of force. The flux trapped in any one wormhole defines the classical electric charge $q _ { w }$ associated with that wormhole. One has to specify all these charges once and for allin addition to the data (21.118) and (21.119) in order to determine fully the dynamic evolution of the electromagnetic field. There is no geometrodynamic analog to electric charge, according to Unruh (l971).] (5) In this integration, the scalar potential $\phi$ at each subsequent time step is not to be calculated; it is to be chosen. Only when one has made this free choice definite do the dynamic equations come out with definite results for the $A _ { i }$ and the $\pi ^ { i }$ or $\delta ^ { i }$ at these successive steps.

Scalar potential: fixed at start;freely disposable later

In the thin-sandwich formulation of the initial-value problem of electrodynamics, to summarize,one gives ${ \mathcal { B } } ^ { i }$ and ${ \dot { \mathcal { B } } } ^ { i }$ (equivalent to $\pmb { \mathcal { B } }$ on two nearby hypersurfaces). One chooses the $A _ { i }$ and $\dot { A } _ { i }$ with much arbitrariness to represent these initial-value data. The arbitrariness having been seized on to give the initial $A _ { i }$ and $A _ { i }$ ,there is no arbitrariness left in the initial $\phi$ .However,at all subsequent times the situation is just the other way around.All the arbitrariness is sopped up in the choice of the $\phi$ ,leaving no arbitrariness whatever in the three $A _ { i }$ (as given by the integration of the dynamic equation).

The situation is quite similar in geometrodynamics. One gives the beginnings of a l-parameter family of spacelike hypersurfaces; namely,

In ADM treatment, give 3-geometry and its time-rate of change

$$
{ } ^ { ( 3 ) } \dot { \mathfrak { s } } ( 0 ) = \frac { \partial ^ { ( 3 ) } \mathfrak { s } } { \partial t } \mathfrak { g i v e n } ,
$$

Then (l) one picks a definite set of coordinates $x ^ { i } = ( x , y , z )$ and in terms of those coordinates finds the unique metric coefficients $g _ { i j } ( x , y , z )$ that describe that 3-geometry. The existence of a solution is guaranteed by the circumstance that $( 3 ) \textcircled { 8 }$ is a Riemannian geometry. However, one could have started with different coordinates and ended up with different metric coefficients for the description of the same 3-geometry. No matter. Pick one set of coordinates, take the resulting metric coeffcients,and stick to them as giving half the required initial-value data.(2) Similarly,to describe the 3-geometry $( 3 ) g + ( 3 ) g$ It at the value of the parameter $t + d t$ ， make use of coordinates $x ^ { i } + { \dot { x } } ^ { i } d t$ and arrive at the metric coefficients $g _ { i j } + \dot { g } _ { i j } d t$ The arbitrariness in the $x ^ { i }$ having thus been resolved by fat, and the $( 3 ) \textcircled { 8 }$ being given as definite initial physical data, the $g _ { i j }$ are thereby completely fixed. (3) Recall that the components of the extrinsic curvature $K _ { i j }$ or the momenta $\pi ^ { i j }$ are given in terms of the $g _ { i j }$ and $\dot { g } _ { i j }$ and the lapse and shift functions $N$ and $N _ { i }$ by (21.67) or by (21.67) plus (21.91) or by (21.114). The four initial-value or “constraint” equations (21.116) and (21.117) thus become four conditions for finding the four quantities $N , ~ N _ { \mathfrak { i } }$ . One can shorten the writing of these conditions by introducing the abbreviations

$$
y _ { i j } = \frac { 1 } { 2 } [ N _ { i | j } + N _ { j | i } - \partial g _ { i j } / \partial t ]
$$

and

$$
\gamma _ { 2 } = { \binom { \mathfrak { s } _ { \mathrm { s h i f t } } } { \mathrm { a n o m a l y } ^ { \prime \prime } } } = ( \mathrm { T r } \gamma ) ^ { 2 } - \mathrm { T r } \gamma ^ { 2 }
$$

(both for functions of $x , y , z$ on the initial simultaneity). Then one has

$$
^ { ( 3 ) } R + \gamma _ { 2 } / N ^ { 2 } = 1 6 \pi T _ { n n } = 1 6 \pi T ^ { n n }
$$

for the one initial-value equation; and for the other three,

Lapse and shift initially determinate; thereafter freely disposable

$$
\begin{array} { r } { \left[ \frac { \gamma _ { i } ^ { \ k } - \delta _ { i } ^ { \ k } \mathrm { T r } \gamma } { N } \right] _ { \parallel k } = - 8 \pi T _ { i } ^ { n } . } \end{array}
$$

In summary,one chooses the $g _ { i j }$ and $\dot { g } _ { i j }$ with much arbitrariness (because of the arbitrariness in the coordinates,not by reason of any arbitrariness in the physics) to represent the given initial-value data, $( 3 ) \textcircled { 8 }$ and $( 3 ) \dot { 8 }$ The arbitrariness at the initial time all having been soaked up in this way,one expects no arbitrariness to be left in the initial $N$ and $N _ { i }$ as obtained by solving (21.126) and (21.127).However,on all later spacelike slices, the award of the arbitrariness is reversed. The lapse and shift functions are freely disposable, but, with them once chosen, there is no arbitrariness whatever in the six $g _ { i j }$ (and the six $K ^ { i j }$ or $\pi ^ { i j }$ )-as given by the integration of the dynamic equations (21.114) and (21.115). The analogy with electrodynamics is clear. There the one“gauge-controlled” function $\phi$ was fixed at the start by the elliptic equation (21.l2l),but was thereafter free. Here the four lapse and shift functions are fixed at the start by the four equations (21.126)and (21.127),but are thereafter free.

Exercise 21.16 applies the initial-value equation (21.126) to analyze the whole evolution in time of any Friedmann universe in which one knows the equation $p = p ( \pmb { \rho } )$ connecting pressure with density. Exercise 21.17 looks for a variation principle on the spacelike hypersurface $\pmb { \Sigma }$ equivalent in content to the elliptic initial-value equation (21.121) for the scalar potential $\phi$ .Exercises 21.18 and 21.19 look for similar variation principles to determine the lapse and shift functions.

How many degrees of freedom,or how many“handles,’are there in the specification of the 4-geometry that one will obtain? The metric coefficients of the initial 3-geometry provided six numbers per space point. However, they were arbitrary to the extent of a coordinate transformation, specified by three functions of position,

$$
\begin{array} { r } { x = x ( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } ) , } \\ { y = y ( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } ) , } \\ { z = z ( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } ) . } \end{array}
$$

The net number of quantities per space point with any physical information was therefore $6 - 3 = 3$ .One can visualize these three functions as the three diagonal components of the metric in a coordinate system in which $g _ { i j }$ has been transformed to diagonal form. Ordinarily it is not useful to go further and actually spell out the analysis in any such narrowly circumscribed coordinate system.

Now think of the $( 3 ) \textcircled { 8 }$ in question as imbedded in the $( 4 ) \log$ that comes out of the integrations.Moreover, think of that $( 4 ) 8$ as endowed with the lumps, bumps, wiggles, and waves that distinguish it from other generic 4-geometries and that make Minkowski geometry and special cosmologies so unrepresentative. The $( 3 ) \textcircled { 8 }$ is a slice in that $( 4 ) g$ It partakes of the lumps, bumps, wiggles,and waves present in all those regions of the $( 4 ) g$ that it intersects. To the extent that the $( 4 ) \cdot 8$ is generic, it does not allow the $( 3 ) \textcircled { 8 }$ to be moved to another location without becoming a different $( 3 ) g$ . If one tries to push the $( 3 ) \textcircled { 8 }$ "forward in time”a litle in acertain locality,leaving it unchanged in location elsewhere, one necessarily changes the $( 3 ) \textcircled { 8 }$ By this circumstance,one sees that the $( 3 ) \textcircled { 8 }$ "carries information about time”[Sharp (196O); Baierlein,Sharp,and Wheeler (l962)]. Moreover, this “forward motion in time”demands for its description one number per space point. It is possble to think of this number in concrete terms by imagining an arbitrary coordinate system t,x,y, $\overline { z }$ laid down in the $( 4 ) 8$ ，Then the hypersurface can be conceived as defined by the value $\overline { { t } } =$ $\overline { { t } } ( \overline { { x } } , \overline { { y } } , \overline { { z } } )$ at which it cuts the typical line ${ \overline { { x } } } ,$ y, z. A forward movement carries it to $\overline { { t } } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) + \delta \overline { { t } } ( \overline { { x } } , \overline { { y } } , \overline { { z } } )$ ,and changes shape and metric coefficients on $( 3 ) \textcircled { 8 }$ accordingly. It is usually better not to tie one's thinking down to such a concrete model, but rather to recognize as a general point of principle (l） that the location of the $( 3 ) \textcircled { 8 }$ in spacetime demands for its specification one datum per spacepoint, and (2) that this datum is already willy-nilly present in the three data per spacepoint that mark any $( 3 ) \textcircled { 8 }$

In conclusion, there are only two data per spacepoint in a $( 3 ) \textcircled { 8 }$ that really tell anything about the $( 4 ) g$ in which it is imbedded,or to be imbedded (as distinguished from where the $( 3 ) \textcircled { 8 }$ slices through that $( 4 ) . 8$ ).Similarlyfor theother $( 3 ) \textcircled { 8 }$ that defines the other “face of the sandwich,”whether thick or thin. Thus one concludes that the specification of $( 3 ) \textcircled { 8 }$ and $( 3 ) \dot { 8 }$ actually gives four net pieces of dynamic information per spacepoint about the $( 4 ) \log$ (all the rest of the information being “many-fingered time,”telling where the 3-geometries are located in that $( 4 ) 8$ ).According to this line of reasoning,geometrodynamics has the same number of dynamic degrees of freedom as electrodynamics. One arrives at the same conclusion in quite another way through the weak-field analysis $( \ S 3 \ 5 . 3 )$ of gravitational waves on a flat spacetime background: the same ranges of possible wave numbers as for Maxwell waves; and for each wave number two states of polarization; and for each polarization one amplitude and one phase (the equivalent of one coordinate and one momentum).

In electrodynamics in a prescribed spacetime manifold,one has a clean separation between the one time-datum per spacepoint (when one deals with electromagnetism in the context of many-fingered time) and the two dynamic variables per spacepoint; but not so in the superspace formulation of geometrodynamics. There the two kinds of quantities are inextricably mixed together in the one concept of 3-geometry.

Four pieces of   
geometrodynamic information   
per space point on initial   
simultaneity