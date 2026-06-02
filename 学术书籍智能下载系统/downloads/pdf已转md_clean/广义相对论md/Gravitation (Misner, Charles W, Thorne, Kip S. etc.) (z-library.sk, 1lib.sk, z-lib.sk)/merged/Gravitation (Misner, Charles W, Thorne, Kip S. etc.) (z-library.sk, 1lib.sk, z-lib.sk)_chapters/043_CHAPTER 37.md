CHAPTER 37

# DETECTION OF GRAVITATIONAL WAVES

l often say that when you can measure what you are speaking about, and express it in numbers,you know something about it:but when you cannot measure it, when you cannot express it in numbers, your knowledge is of a meagre and unsatisfactory kind: it may be the beginning of knowledge, but you have scarcely. in your thoughts,advanced to the stage of science, whatever the matter may be.

WILLIAM THOMSON,LORD KELVIN [(1889).p.73]

Linearized description of gravitational waves propagating past Earth

# \$37.1. COORDINATE SYSTEMS AND IMPINGING WAVES

The detector is even easier to analyze than the generator or the transmission when one deals with gravitational waves within the framework of general relativity.Man's potential detectors all lie in the solar system, where gravity is so weak and spacetime so nearly flat that a plane gravitational wave coming in remains for all practical purposes a plane gravitational wave. (Angle of deflection of wave front passng limb of sun is only l'75.) Moreover, the nearest source of significant waves is so far away 'that, for all practical purposes,one can consider the waves as plane-fronted when they reach the Earth. Consequently,as they propagate in the $z$ -direction past a detector, they can be described to high accuracy by the following transverse-traceless linearized expressions

Metric perturbation: $\begin{array} { r } { h _ { x x } ^ { T T } = - h _ { y y } ^ { T T } = A _ { + } ( t - z ) , h _ { x y } ^ { T T } = h _ { y x } ^ { T T } = A _ { \times } ( t - z ) , } \end{array}$

$$
R _ { z 0 y 0 } = R _ { y 0 x 0 } = - \frac { 1 } { 2 } \ddot { A } _ { \times } ( t - z ) .
$$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0015_pages_0981-1050/auto/images/59cab684ab55c8ed4ab3901dc0b9d378827ec7564abe498b2fdb1b580a8d175c.jpg)  
Figure 37.1. The proper reference frame of a vibrating-bar detector. The bar hangs by'a wire from a cross beam,which is supported by vertical posts (not shown) that are embedded in the Earth.Consequently,the bar experiences a 4-acceleration given, at the moment when this diagram is drawn, by ${ \pmb a } = { \pmb g } ( \hat { \partial } / \hat { \partial } \hat { \pmb z } )$ ，where $\pmb { g }$ is the “local acceleration of gravity” $( g \sim 9 8 0 \ \mathsf { c m } / \mathsf { s e c } ^ { 2 } )$ .Later,the spatial axes will have rotated relative to the bar ("Foucoult-pendulum effect” produced by Earth's rotation),so the components of a but not its magnitude will have changed.

The proper reference frame relies on an imaginary clock and three imaginary gyroscopes located at the bar's center of mass (and shown above in a cut-away view).Coordinate time is equal toproper time as measured by the clock,and the directions of the spatial axes $\partial / \hat { c } x ^ { \hat { j } }$ are attached to the gyroscopes.The forces that prevent the gyroscopes from falling in the Earth's field must be applied at the centers of mass of the individual gyroscopes (no torque!).

(See exercise 37.1.)

To analyze most easily the response of the detector to these impinging waves, use not the $T T$ coordinate system $\{ x ^ { \alpha } \}$ (which is specially “tuned” to the waves), but rather use coordinates $\scriptstyle { \left\{ x ^ { \hat { \alpha } } \right\} }$ specially “tuned” to the experimenter and his detector.The detector might be a vibrating bar,or the vibrating Earth,or a loop of tubing flled with fluid (see Figures 37.l and 37.2). But whatever it is, it will have a center of mass.Attach the spatial origin, $x ^ { \hat { j } } = 0$ ,to this center of mass; and attach orthonormal spatial axes, $\partial / \partial { x } ^ { \hat { j } }$ ,to (possibly imaginary） gyroscopes located at this spatial origin (Figure 37.l). If the detector is accelerating (i.e., not faling freely), make the gyroscopes accelerate with it by applying the necessary forces at their centers of mass (no torque!). Use, as time coordinate,the proper time $x ^ { \hat { 0 } } = \tau$ measured by a clock at the spatial origin. Finally,extend these locally defined coordinates $\overrightharpoon { x ^ { \alpha } }$ throughout all spacetime in the “straightest” manner possible. (See

Proper reference frame of a detector

Track 2's $\ S 1 3 . 6$ for full details.) The metric in this “proper reference frame of the detector” will have the following form

$$
d s ^ { 2 } = - ( 1 + 2 a _ { \lambda } x ^ { \hat { j } } ) ( d x ^ { \hat { 0 } } ) ^ { 2 } + \delta _ { \hat { j } \hat { k } } d x ^ { \hat { j } } d x ^ { \hat { k } } + { \cal O } ( | x ^ { \hat { j } } | ^ { 2 } ) d x ^ { \hat { \alpha } } d x ^ { \hat { \beta } } .
$$

[equation (13.71) with $\omega ^ { \hat { \imath } } = 0 ]$ . Here $a _ { \hat { j } }$ are the spatial components of the detector's 4-acceleration.(Since a must be orthogonal to the detector's 4-velocity, $a _ { \hat { 0 } }$ vanishes.) Notice that, except for the acceleration term in $g _ { \hat { 0 } \hat { 0 } }$ ("gravitational redshift term”; see $\ S 3 8 . 5$ and exercise 6.6), this reference frame is locally Lorentz.

# EXERCISES

# ExerciSe 37.1. GENERAL PLANE WAVE IN TT GAUGE

Show that the most general linearized plane wave can be described in the transverse-traceless gauge of linearized theory by expressions (37.l).[Hint: Express the plane wave as a superposition (Fourier integral) of monochromatic plane waves,and describe each monochromatic planewave byexpressions (35.16).Useequations (35.0)and (3523)tocalcuate $R _ { \alpha \beta \gamma \delta }$ and $T _ { \mu \nu } ^ { ( \mathsf { G W } ) }$ j

# ExerCiSe 37.2. TEST-PARTICLE MOTION IN PROPER REFERENCE FRAME

Show that a slowly moving test particle, falling freely through the proper reference frame of equation (37.2), obeys the equation of motion (geodesic equation)

$$
d ^ { 2 } x ^ { \hat { j } } / d \hat { t } ^ { 2 } = - a _ { \hat { j } } + O ( | x ^ { \hat { k } } | ) .
$$

Thus, one can interpret $- a _ { \ 3 }$ as the “local acceleration of gravity” (see caption of Figure 37.1).

Equations of motion for a mechanical detector

# \$37.2. ACCELERATIONS IN MECHANICAL DETECTORS

The proper reference frame of equation (37.2) is the closest thing that exists to the reference frame a Newtonian physicist would use in analyzing the detector.In fact, it is so nearly Newtonian that (according to the analysis of Box 37.1) the equations ofmotion for a mechanical detector,when written in this proper reference frame,take their standard Newtonian form and can be viewed and dealt with in a fully Newtonian manner, with one exception: the gravitational waves produce a driving force of non-Newtonian origin, given by the familiar expression for geodesic deviation 9

$$
\left( \begin{array} { l } { { \mathrm { f o r c e ~ p e r ~ u n i t ~ m a s s ~ ( i . e . , ~ a c c e l e r a t i o n ) } } } \\ { { \mathrm { o f ~ a ~ p a r t i c l e ~ a t ~ } x ^ { \hat { j } } \mathrm { ~ r e l a t i v e ~ t o ~ d e t e c t o r ' s } } } \\ { { \mathrm { c e n t e r ~ o f ~ m a s s ~ a t ~ } x ^ { \hat { j } } = 0 } } \\ { { \qquad = \qquad - ( R _ { \hat { j } \hat { o } \hat { k } \hat { o } } ) _ { \mathrm { d u e t o ~ w a v e s } } x ^ { \hat { k } } . } } \end{array} \right) = \left( \begin{array} { l } { { d ^ { 2 } x ^ { \hat { j } } } } \\ { { \hat { d t } ^ { \hat { 2 } } } } \end{array} \right) _ { \mathrm { d u e ~ t o ~ w a v e s } }
$$

To use this equation, and to calculate detector cross sections later, one must know the components of the curvature tensor $R ^ { \hat { \alpha } } { } _ { \hat { \beta } \hat { \gamma } \hat { \delta } }$ ,and of the wavesstress-energy ensor, $T _ { \hat { \mu } \hat { \nu } } ^ { ( \mathrm { G W } ) }$ in the detectorsproperreferenceframe.Onecannot calculate $R ^ { \hat { \alpha } } { } _ { \hat { \beta } \hat { \gamma } \hat { \delta } }$ directly

# Box 37.1 DERIVATION OF EQUATIONS OF MOTION FOR A MECHANICAL DETECTOR

Consider a “mass element”in a mechanical detector (e.g., a cube of aluminum one millimeter on each edge if the detector is the bar of Figure 37.l； or an element of fluid with volume $1 \mathrm { m m } ^ { 3 }$ if the detector is the tube filled with fluid shown in part h of Figure 37.2). This mass element gets pushed and pulled by adjacent matter and electromagnetic fields,as the medium of the detector vibrates or flows or does whatever it is supposed to do.Let

$$
\pmb { \mathscr { r } } \equiv \left( { \begin{array} { l } { 4 . { \mathrm { f o r c e ~ p e r ~ u n i t ~ m a s s ~ e x e r t e d ~ o n ~ m a s s . } } { \mathrm { e l e m e n t } } } \\ { { \mathrm { b y ~ a d j a c e n t ~ m a t t e r ~ a n d ~ b y ~ e l e c t r o m a g n e t i c ~ f i e l d s } } } \end{array} } \right) .
$$

This 4-force per unit mass gives the mass element a 4-acceleration $\pmb { \check { \bigtriangledown } } _ { \pmb { \mu } } \pmb { \mu } = \pmb { \mathcal { t } }$ or, in terms of components in the detector's proper reference frame, ${ f ^ { \widehat { \jmath } } } = D u ^ { \widehat { \jmath } } / d \tau$ Assume that the mass element has a very small velocity $( v \ll 1 )$ in the detector's proper reference frame (i.e., relative to the detector's center of mas). Then,ignoring terms of $O ( v ^ { 2 } ) , O ( | x ^ { \hat { j } } | ^ { 2 } ) .$ and $O ( | x ^ { \hat { j } } | \upsilon )$ ,one has [see equation (37.2)]

$$
d \hat { t } / d \tau = u ^ { \hat { 0 } } = 1 - a _ { \hat { j } } x ^ { \hat { j } } \equiv 1 - a \cdot x ,
$$

and

$$
f ^ { \hat { j } } = d ^ { 2 } x ^ { \hat { j } } / d \tau ^ { 2 } + { \cal T } ^ { \hat { j } } { } _ { \hat { \alpha } \hat { \beta } } u ^ { \hat { \alpha } } u ^ { \hat { \beta } } = ( d ^ { 2 } x ^ { \hat { j } } / d \hat { t } ^ { 2 } + { \cal T } ^ { \hat { j } } { } _ { \hat { 0 } \hat { 0 } } ) ( 1 - 2 a \cdot x ) .
$$

Exercise 37.3 calculates ${ r ^ { \hat { j } } } _ { \hat { 0 } \hat { 0 } }$ to precision of $O ( | x ^ { \hat { j } } | )$ Inserting its result andrearranging terms,one finds that

$$
d ^ { 2 } x ^ { \hat { j } } / \hat { d t ^ { 2 } } = ( 1 + 2 a \cdot x ) f ^ { \hat { j } } - a ^ { \hat { j } } ( 1 + a \cdot x ) - R ^ { \hat { j } } { } _ { \hat { 0 } \hat { k } \hat { 0 } } x ^ { \hat { k } }
$$

("equation of motion for mass element").

Examine this equation,first from the viewpoint of an Einsteinian physicist, and then from the viewpoint of a Newtonian physicist.

The Einsteinian physicist recognizes $d ^ { 2 } x ^ { \hat { j } } / { \hat { d t } } ^ { 2 }$ as the“coordinate acceleration” of the mass element-but he keeps in mind that, to precision of $O ( | x ^ { \hat { j } } | ^ { 2 } )$ ，coordinate lengths and proper lengths are the same [see equation (37.2)]. The coordinate acceleration $\bar { d } ^ { 2 } x ^ { \hat { j } } / d \hat { t } ^ { 2 }$ has three causes: (l) the externally applied force,

$$
\begin{array} { r } { ( 1 + 2 a \cdot x ) f ^ { \hat { j } } = ( d ^ { 2 } x ^ { \hat { j } } / { \hat { d t } ^ { 2 } } ) _ { \mathrm { e x t e r n a l f o r c e } } } \\ { = ( 1 + 2 a \cdot x ) ( d ^ { 2 } x ^ { \hat { j } } / d \tau ^ { 2 } ) _ { \mathrm { e x t e r n a l f o r c e } } } \end{array}
$$

(the origin of the $\mathbf { \nabla } _ { \mathbf { a } } \cdot \mathbf { \nabla } _ { \mathbf { x } }$ correction is simply the conversion between coordinate time

and proper time); (2) the “inertial force” due to the acceleration of the reference frame,

$$
- a ^ { \hat { j } } ( 1 + a \cdot x ) = ( d ^ { 2 } x ^ { \hat { j } } / \hat { d t ^ { 2 } } ) _ { \mathrm { i n e r t a l f o r c e } }
$$

(see exercise 37.4 for explanation of the ${ \pmb a } \cdot { \pmb x }$ correction)；and (3） a“Riemann curvature force,”which will include Riemann curvature due to local, Newtonian gravitational fields (fields of Earth, sun, moon, etc.), plus Riemann curvature due to the impinging gravitational waves,

$$
- ( R ^ { \hat { j } } { } _ { \hat { 0 } \hat { k } \hat { 0 } } ) _ { \mathrm { w a v e s } } x ^ { \hat { k } } - ( R ^ { \hat { j } } { } _ { \hat { 0 } \hat { k } \hat { 0 } } ) _ { \mathrm { N e w t o n f i e l d s } } x ^ { \hat { k } } = ( d ^ { 2 } x ^ { \hat { j } } / d \hat { t } ^ { 2 } ) _ { \mathrm { c u r v a t u r e } }
$$

(linear superposition because all gravitational fields in the solar system are so weak). This “Riemann curvature force” is not, of course,“felt” by the mass element; it does not produce any 4-acceleration. Rather, like the inertial force,it originates in the choice of reference frame: The spatial coordinates $x ^ { \hat { j } }$ measure proper distance and direction away from the detector's center of mass; and Riemann curvature tries to change this proper distance and direction ("relative acceleration;”“geodesic deviation").

A Newtonian physicist views the equation of motion (4) in a rather different manner. Having been told that the spatial coordinates $x ^ { \hat { \mathfrak { j } } }$ measure proper distance and direction away from the detector's center of mass,he thinks of them as the standard Euclidean spatial coordinates of Newtonian theory. He then rewrites equation (4) in the form

$$
d ^ { 2 } x ^ { \hat { j } } / \hat { d t ^ { 2 } } = F ^ { \hat { j } } - ( R ^ { \hat { j } } { } _ { \hat { 0 } \hat { k } \hat { 0 } } ) _ { \mathrm { w a v e s } } x ^ { \hat { k } } ,
$$

where

$$
\begin{array} { r l } & { F ^ { j } \equiv \binom { \mathrm { N e w t o n i a n ~ f o r c e ~ p e r ~ u n i t ~ m a s s } } { \mathrm { a c t i n g ~ o n ~ m a s s ~ e l e m e n t } } } \\ & { ~ = ( 1 + 2 a \cdot x ) f ^ { j } - a ^ { \dot { \beta } } ( 1 + a \cdot x ) - ( R ^ { \hat { j } } \hat { 0 } \hat { \pmb { \mathscr { k } } } \hat { 0 } ) _ { \mathrm { N e w t o n ~ f i e l d s } } x ^ { \hat { \pmb { \mathscr { k } } } } . } \end{array}
$$

The Newtonian physicist is free to express $F ^ { \hat { j } }$ in a form more familiar than this. He can ignore the subtleties of the $\pmb { a } \cdot \pmb { x }$ "redshift effects” because (l) they are small

$$
| a ^ { \widehat { j } } ( a \cdot x ) | \sim | f ^ { \widehat { j } } ( a \cdot x ) | \lesssim | ( R ^ { \widehat { j } } { } _ { \widehat { 0 } \widehat { k } \widehat { 0 } } ) _ { \mathrm { w a v e s } } x ^ { \widehat { k } } | ;
$$

and (2) they are steady in time,and therefore-by contrast with the equally small wave-induced forces-they cannot excite resonant motions of the detector. Also,he can separate the “inertial acceleration $\vec { \bf \Phi } ^ { \prime } - a ^ { \hat { j } }$ ,into a contribution from the local acceleration of gravity at the detector's center of mass, $- ( \partial \Phi / \partial x ^ { \widehat { \ j } } ) _ { x ^ { \widehat { \ j } } = 0 }$ plus a contribution $- \tilde { a ^ { j } } _ { \mathrm { a b s o l u t e } }$ due to acceleration of the detector relative to the “absolute space”of Newtonian theory. Finally,he can rewrite the Riemann curvature due to Newtonian gravity in the familiar form $R ^ { \hat { j } } { } _ { \hat { 0 } \hat { k } \hat { 0 } } = \partial ^ { 2 } \varPhi / \partial x ^ { \hat { j } } \partial x ^ { \hat { k } }$ ，The net result is

$$
F ^ { \widehat { j } } =
$$

$$
{ \biggl [ } = - ( \partial \phi / \partial x ^ { \hat { \jmath } } ) _ { x ^ { \hat { \jmath } } = 0 } - ( \partial ^ { 2 } \phi / \partial x ^ { \hat { \jmath } } \partial x ^ { \hat { k } } ) x ^ { \hat { k } }  \\ { = { \mathrm { N e w t o n i a n ~ g r a v i t a t i o n a l ~ a c c e l e r a t i o n } } } { \biggr ] } .
$$

Conclusion: The equation of motion for a mass element of a mechanical detector, when written in the detector's proper reference frame, has the standard Newtonian form (6),with standard Newtonian driving forces (9), plus a driving force due to the gravitational waves given by

$$
( d ^ { 2 } x ^ { \hat { j } } / { d { \hat { t } } ^ { 2 } } ) _ { \mathrm { d u e t o w a v e s } } = - ( R ^ { \hat { j } } { } _ { \hat { 0 } \hat { k } \hat { 0 } } ) _ { \mathrm { w a v e s } } x ^ { \hat { k } } .
$$

from the metric coefficients $g _ { \hat { \alpha } \hat { \beta } }$ of expression (37.2); to do so one would need the unknown corrections of $O ( | x ^ { \hat { j } } | ^ { 2 } )$ . However, one can easily obtain $R ^ { \hat { \alpha } } { } _ { \hat { \beta } \hat { \gamma } \hat { \delta } }$ and $T _ { \hat { \mu } \hat { \nu } } ^ { ( \mathrm { G W } ) }$ from the corresponding components in the $T T$ coordinate frame [equations (37.1)] by applying the transformation matrix $\lvert \lvert \partial x ^ { \alpha } / \partial x ^ { \hat { \mu } } \rvert \rvert$ . To make the transformation trivial, orient the $T T$ coordinate frame so that, to a precision of $O ( | h _ { \mu \nu } | ) \ll 1$ ,it coincides with the detector's proper reference frame near the detector's center of mass at the moment of interest, $\overset { \cdot } { t } = \overset { \cdot } { t } = 0$ .Then the transformation matrix will be

$$
\begin{array} { r l r } & { ~ \partial x ^ { \alpha } / \partial x ^ { \hat { \mu } } = \delta _ { \mu } ^ { \alpha } + { \cal O } ( h _ { \mu \nu } ) + { \cal O } ( a _ { \hat { \mu } } x ^ { \hat { \eta } } ) + { \cal O } ( | a | \hat { t } ) . } & \\ & { ~ \cdot \mathrm { c o r r e c t i o n s ~ d u e ~ t o ~ } } & { \Bigg ] \int \left[ \mathrm { r e d s h i f t } \atop \mathrm { c o r r e c t i o n s } \right] ^ { \hat { \mu } } } & { \left[ \begin{array} { l } { \mathrm { r e c t i o n s ~ d u e ~ t i o n s ~ } \mathrm { d u } } \\ { \mathrm { v e l o c i n ~ s p a c e t i m e } } \end{array} \right] } \\ & { ~ \cdot \mathrm { c a u s e d ~ b y ~ w a v e s ~ } } & { } \end{array}
$$

The acceleration the detector experiences is typically

$$
| a | = \mathrm { o n e } ^ { \mathrm { * } } \mathrm { E a r t h ~ g r a v i t y } ^ { \mathrm { * } \mathrm { , * } } = 9 8 0 \mathrm { c m / s e c ^ { 2 } } \sim 1 / ( \mathrm { l i g h t \mathrm { - } y e a r } ) .
$$

Description of waves in frame of detector

Therefore to enormous precision $| | \hat { \partial } x ^ { \alpha } / \hat { \partial } x ^ { \hat { \mu } } | | = | | \delta _ { \mu } ^ { \alpha } | |$ ,and components of tensors are the same in the two reference frames:

$$
\mathrm { ~ . ~ } R _ { \hat { x } \hat { 0 } \hat { x } \hat { 0 } } = - R _ { \hat { y } \hat { 0 } \hat { y } \hat { 0 } } = - \frac { 1 } { 2 } \ddot { A } _ { + } , R _ { \hat { x } \hat { 0 } \hat { y } \hat { 0 } } = R _ { \hat { y } \hat { 0 } \hat { x } \hat { 0 } } = - \frac { 1 } { 2 } \ddot { A } _ { \times } ,
$$

$$
T _ { \hat { 0 } \hat { 0 } } ^ { \mathrm { ( G W ) } } = T _ { \hat { z } \hat { z } } ^ { \mathrm { ( G W ) } } = - T _ { \hat { 0 } \hat { z } } ^ { \mathrm { ( G W ) } } = \frac { 1 } { 1 6 \pi } \langle \dot { A } _ { + } ^ { 2 } + \dot { A } _ { \times } ^ { 2 } \rangle _ { \mathrm { t i m e a v g . } }
$$

[see equation (37.1)].

Combining equations (37.3） and (37.5)，one obtains for the wave-induced accelerations relative to the center of mass of the detector

Explicit form of accelerations due to waves

$$
\begin{array} { r l } & { \left( \frac { d ^ { 2 } \hat { x } } { d \hat { t } ^ { 2 } } \right) _ { \mathrm { d u e t o w a v e s } } = - R _ { \hat { x } \hat { 0 } \hat { x } \hat { 0 } } \hat { x } - R _ { \hat { x } \hat { 0 } \hat { y } \hat { 0 } } \hat { y } = \displaystyle \frac { 1 } { 2 } ( \ddot { A _ { + } } \hat { x } + \ddot { A } _ { \times } \hat { y } ) , } \\ & { \left( \frac { d ^ { 2 } \hat { y } } { d \hat { t } ^ { 2 } } \right) _ { \mathrm { d u e t o w a v e s } } = - R _ { \hat { y } \hat { 0 } \hat { y } \hat { 0 } } \hat { y } - R _ { \hat { y } \hat { 0 } \hat { x } \hat { 0 } } \hat { x } = \displaystyle \frac { 1 } { 2 } ( - \ddot { A _ { + } } \hat { y } + \ddot { A _ { \times } } \hat { x } ) , } \end{array}
$$

$$
\begin{array} { r } { \left( \frac { d ^ { 2 } \hat { z } } { d t ^ { 2 } } \right) _ { \bf d u e t o w a v e s } = 0 . } \end{array}
$$

This analysis is valid only for "small" detectors $( L \ll \lambda )$

These expressions,like the equation of geodesic deviation, are valid only over regions small compared to one wavelength. Second derivatives of the metric (i.e., the components of the Riemann tensor） give a poor measure of geodesic deviation and of wave-induced forces over regions of size $L \gtrsim \lambda$ .Thus,to analyze large detectors $( L \gtrsim \lambda )$ ， one must abandon the “local mathematics” of the curvature tensor and replace it by “global mathematics”-e.g.,an analysis in the $T T$ coordinate frame using the metric components $h _ { \mu \nu }$ .For an example, see exercise 37.6.

All detectors of high sensitivity that have been designed up until now (l973) are small compared to a wavelength,and therefore can be analyzed using the techniques of Newtonian physics and the driving forces of equations (37.6).

It is usefulto develop physical intuition for the driving forces, $- { R ^ { j } } _ { \hat { 0 } \hat { k } \hat { 0 } } x ^ { \hat { k } }$ , produced by waves of various polarizations.Figure 35.2 is one aid to such intuition; Box 37.2 is another.[The reader may find it interesting to examine,compare,and reconcile them!]

EXERCISES

# Exercise 37.3. CONNECTION COEFFICIENTS IN PROPER REFERENCE FRAME

(a） Calculate $\Gamma ^ { \hat { \alpha } } { } _ { \hat { \beta } \hat { \gamma } }$ for the metric (37.2),ignoring corrections of $O ( \{ x ^ { j } \} )$ . [Answer: Equations (13.69) with $\omega ^ { \downarrow } = \mathrm { 0 } . 1$

(b) Calculate $R ^ { \widehat { j } } { \widehat { \circ } } \widehat { \kappa } { \widehat { \boldsymbol { 0 } } }$ using the standard formula (8.44),and leaving spatial derivatives of the connection coeffcients unevaluated because of the unknown corrections of $O ( | x ^ { \hat { \mathbf { j } } } | )$ in $T ^ { \hat { \alpha } } { } _ { \hat { \beta } \hat { \gamma } } .$ [Answer: $R ^ { \hat { j } } { } _ { \hat { 0 } \hat { k } \hat { 0 } } = T ^ { \hat { j } } { } _ { \hat { 0 } \hat { 0 } , \hat { k } } - a ^ { \hat { j } } a ^ { \hat { k } } .$ 1

(c) Use the answer to part (b) to evaluate the $O ( \{ x ^ { \hat { j } } \} )$ corrections to $\Gamma ^ { \hat { j } } { } _ { \hat { 0 } \hat { 0 } } .$ [Answer:

$$
{ T ^ { \hat { j } } } _ { \hat { 0 } \hat { 0 } } = a ^ { \hat { j } } ( 1 + a _ { \hat { k } } x ^ { \hat { k } } ) + { R ^ { \hat { j } } } _ { \hat { 0 } \hat { k } \hat { 0 } } x ^ { \hat { k } } + O ( | x ^ { \hat { k } } | ^ { 2 } ) . ]
$$

# Box 37.2 LINES OF FORCE FOR GRAVITATIONAL-WAVE ACCELERATIONS

# A.Basic ldea

Consider a plane wave propagating in the $\hat { z }$ direction.Discuss it entirely in the proper reference frame of a detector.The relative accelerations due to the wave are entirely transverse. Relative to the center of mass of the detector (origin of spatial coordinates） they are

$$
\begin{array} { l } { { d ^ { 2 } \hat { x } / d \hat { t } ^ { 2 } = \displaystyle \frac { 1 } { 2 } ( \ddot { A } _ { + } \hat { x } + \ddot { A } _ { \times } \hat { y } ) , } } \\ { { } } \\ { { d ^ { 2 } \hat { y } / d \hat { t } ^ { 2 } = \displaystyle \frac { 1 } { 2 } ( - \ddot { A } _ { + } \hat { y } + \ddot { A } _ { \times } \hat { x } ) , } } \\ { { } } \\ { { d ^ { 2 } \hat { z } / \hat { d \hat { t } } ^ { 2 } = 0 . } } \end{array}
$$

Notice that these accelerations are divergence-free. Consequently they can be represented by “lines of force,” analogous to those of a vacuum electric field. At a value of $\hat { t } - \hat { z }$ where $\ddot { A } _ { \times } = 0$ (so polarization is entirely ${ \pmb e } _ { + }$ ),the lines of force are the hyperbolas shown here [sketch (a)]. The direction of the acceleration at any point is the direction of the arrow there; the magnitude of the acceleration is the density of force lines. Since acceleration is proportional to distance from center of mass, the force lines get twice as close together when one moves twice as far_away from the origin in a given direction. When $\ddot { A } _ { + }$ is positive,the arrows on the force lines are as shown in (a); when it is negative, they are reversed.As $| \ddot { A } _ { + } |$ increases,the force lines move in.toward the origin so their density goes up；as $| \ddot { A } _ { + } |$ decreases, they move out toward infinity so their density goes down.

For polarization ${ \pmb { e } } _ { \times }$ the force lines are rotated by $4 5 ^ { \circ }$ from the above diagram.For intermediate polarization (values of $\hat { t } - \check { z }$ where $\ddot { A } _ { + }$ and $\ddot { A } _ { \times }$ are both nonzero), the diagram is rotated by an intermediate angle [sketch (b)]

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0015_pages_0981-1050/auto/images/28514c3211e87fedbfd4d692d06106f47fd3a76fc9b456584ea22fc9ae2db059.jpg)

(a) Force lines for $\ddot { A } _ { \times } = 0 , \ddot { A } _ { + } > 0$

$$
\phi _ { 0 } = \frac { 1 } { 2 } \arctan { ( \ddot { A } _ { \times } / \ddot { A } _ { + } ) } .
$$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0015_pages_0981-1050/auto/images/ab2cb2e9a961150c6d4585e1968544ca226775d2d368b1f1e8c070286ccea520.jpg)

# Box 37.2 (continued)

# B. Three-Dimensional Diagram

At each value of $\hat { t } - \hat { z } ,$ ,the wave-produced accelerations have a specific polarization [orientation angle $\phi _ { 0 }$ of sketch (b)] and a specific amplitude (density of lines of force). Draw the lines of force in a three-dimensional $( \hat { x } , \hat { y } , \hat { z } )$ diagram for fixed $\hat { t } .$ Then as time passes the over-all diagram wil remain unchanged in form, but will propagate with the speed of light in the $\hat { z }$ direction.

Sketch (c) shows such a diagram for righthand circularly polarized waves of unchanging amplitude. Note: The authors are not aware of diagrams such as these [(a), (b),(c) above] and their use in analyzing detector response prior to William H. Press (1970).

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0015_pages_0981-1050/auto/images/a103d4f2c4eaa1d7e5737c40a45e4d2dd6da531ce0e23d0cb283cc8a8aebe703.jpg)  
Eight types of mechanical detectors:

# Exercise 37.4. WHY THE ${ \pmb a } \cdot { \pmb x } \mathbf { \nabla }$

Explain the origin of the ${ \pmb a } \cdot { \pmb x }$ correction in equation (5b) of Box 37.l. [Hint: Take the viewpoint of an observer at rest at the spatial origin who watches two freely falling particles respond to the inertial force.At time $\hat { \boldsymbol { t } } = 0$ ， put one particle at the origin and the other at ${ \dot { x } } ^ { \hat { j } } .$ As time passes,the separation of the particles in their common Lorentz frame remains fixed; so there develops a Lorentz contraction from the viewpoint of the observer at $x ^ { \hat { j } } = 0 . ]$

Exercise 37.5. ORIENTATION OF POLARIZATION DIAGRAM Derive equation (2) of Box 37.2.

# \$37.3. TYPES OF MECHANICAL DETECTORS

Figure 37.2 shows eight different types of mechanical detectors for gravitational waves.(By“mechanical detector”is meant a detector that relies on the relative

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0015_pages_0981-1050/auto/images/bd56d409472221078eb6dea083f523fabf3affb2ac3ef574e370728332b2e624.jpg)  
Figure 37.2. Various types of gravitational-wave detectors.

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0015_pages_0981-1050/auto/images/a0bd25ae95c72c643d92e01914c4a4e6b920c9db4e238f85a723c4ef0a8657d4.jpg)  
(b) Normal-mode vibrations of earth and moon [see Weber(1968)]

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0015_pages_0981-1050/auto/images/71aaca11f9d0c0e5952f5a99b75fb75324d57ce725814998f2786b05b3d89d22.jpg)  
(d) Normal-mode vibrations of an elastic bar [see Weber(1969）and references cited therein]

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0015_pages_0981-1050/auto/images/cc79391509bec3f30ab6fc0a8e48db932ba49a2d6960f6781a485baa9f694448.jpg)

(f） Angular accelerations of rotating bars[“Heterodyne detector":see Braginsky, Zel'dovich,and Rudenko (1969)]

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0015_pages_0981-1050/auto/images/31051635dd99aafeeba4d7e092f5842f8fa06f1fba4920e7bd0b25832a9ebd17.jpg)  
(h）Pumping of fluid in a rotating loop of pipe [Press (l970)].The pipe rotates with the same angular velocity as the waves: so the position of the pipe in the righthand polarized lines of force remains forever fixed

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0015_pages_0981-1050/auto/images/c41eef9214e6a3d489b94de09a399890cfd3e4fc63177ff0725a516999754319.jpg)

motions of matter. Nonmechanical detectors are described in $\ S 3 7 . 9$ ,near end of this chapter.) These eight detectors,and others,can be analyzed easily using the force-line diagrams of Box 37.2.A qualitative discussion of each of the eight detectors is given below.(A full quantitative analysis for each one would entail experimental technicalities for which general relativity is irrelevant, and which are beyond the scope of this book. However, some quantitative details are spelled out in $\ S \ S 3 7 . 5 \ – 3 7 . 8 . )$

# 1. The Relative Motions of Two Freely Falling Bodies

(1） freely falling bodies

As a gravitational wave passes two freely falling bodies, their proper separation oscillates (Figure 37.3). This produces corresponding oscillations in the redshift and round-trip travel times for electromagnetic signals propagating back and forth between the two bodies. Either effect,oscillating redshift or oscillating travel time, could be used in principle to detect the passage of the waves. Examples of such detectors are the Earth-Moon separation, as monitored by laser ranging [Fig. 37.2(a); Earth-spacecraft separations as monitored by radio ranging; and the separation between two test masses in an Earth-orbiting laboratory,as monitored by redshift measurements or by laser interferometry. Several features of such detectors are explored in exercises 37.6 and 37.7.As shown in exercise 37.7, such detectors have so low a sensitivity that they are of little experimental interest.

Figure 37.3.   
Time of round-trip travel between two geodesics responds to oscillations in the curvature of spacetime (diagram is schematic only;symbolic of a laser pulse sent from the Earth to a corner reflector on the Moon and back at a time when a very powerful, long-wavelength gravitational wave passes by；the wave would have to be powerful because a direct measure of distance to better than $1 0 \ \mathtt { c m }$ is difficult, and such precision produces a much less sensitive indicator of waves than the vibrations in length $1 0 ^ { - 1 4 }$ cm or less] of a Weber bar; see exercise 37.7).The geodesics are curved toward each other in regions where the relevant component of the Riemann curvature tensor, call it $R _ { \widehat { \pm } \widehat { 0 } \widehat { \pm } \widehat { 0 } } .$ has one sign,and curved away from each other in regions where it has the opposite sign.The diagram allows one to see at a glance the answer to an often expressed puzzlement: Is not any change in round-trip travel time mere trumpery flummery? The metric perturbation, $\delta h _ { \mu \nu } ^ { - } ,$ of the wave changes the scale of distances slightly but also correspondingly changes the scale of time.Therefore does not every possibility of any really meaningful and measurable effect cancel out? Answer:(l） The widened separation between the geodesics is not a local effect but a cumulative one.It does not arise from the local value of $\delta h _ { \mu \nu }$ directly or even from the local value of the curvature.It arises from an accumulation of the bending process over an entire half-period of the gravitational wave.(2) The change in separation of the geodesics is a true change in proper distance,and shows up in a true change in proper time (see“ticks”on the world line of one of the particles). See exercise 37.6.Note:When one investigates the separation between the geodesics,not over a single period,as here,but over a large number of periods,he finds a cumulative,systematic,net slow bending of the rapidly wiggling geodesics toward each other.This small,attractive acceleration is evidence in gravitation physics of the effective mass-energy carried by the gravitational waves (see Chapter 35).

# 2. Normal-Mode Vibrations of the Earth and Moon

(2) Earth and Moon

A gravitational wave sweeping over the Earth will excite its quadrupole modes of vibration, since the driving forces in the wave have quadrupole spatial distributions [see Fig.37.2(b)]. The fundamental quadrupole mode of the Earth has a period of 54 minutes,while that of the moon has a period of l5 minutes.Thus, the Earth and Moon should selectively pick out the 54-minute and 15-minute components of any passing wave train. Section 37.7 will analyze quantitatively the interaction between the wave and solid-body vibrations.By comparing that analysis with seismometer studies of the Earth's vibrations,Weber(l967) put the first observational limit ever on the cosmic flux of gravitational waves:

$$
I _ { \nu } \equiv \frac { d \mathrm { \ f u x } } { \ s \ t \ \mathrm { \ f r e q u e n c y } } < 3 \times 1 0 ^ { 7 } \ \mathrm { e r g \ c m ^ { - 2 } \ s e c ^ { - 1 } \ H z ^ { - 1 } \ a t \ } \nu = 3 . 1 \times 1 0 ^ { - 4 } \ \mathrm { H z } .
$$

# 3. Oscillations in the Earth's Crust

(3) Earth's crust

If the neutron star in a pulsar is slightly deformed from axial symmetry,its rotation will produce gravitational waves. The period of the waves is half the period of the pulsar (rotation of star through $1 8 0 ^ { \circ }$ produces one period of waves)-i.e., it should range from 0.017 sec for NP0532 (Crab Pulsar) to 1.87 sec. for NP0527. Such a wave train cannot excite the 54-minute quadrupole vibration or any of the other normal,low-frequency modes of vibration of the Earth.The kind of vibrations it can excite allow themselves in principle to be described in the language of normal modes.However, they are clearly and more conveniently envisaged as vibrations of localized regions of the Earth;or,more particularly,vibrations of the Earth's crust.

Dyson (l969) has analyzed the response of an elastic solid,such as the Earth, to an incident, off-resonance gravitational wave.He shows that the response depends on irregularities in the elastic modulus for shear waves,and that it is strongest at a free surface [Figure 37.2(c)). For the fraction of gravitational-wave energy crossing a flat surface that is converted into energy of elastic motion of the solid, he finds the expression

$$
\mathrm { ( f r a c t i o n ) } = ( 8 \pi G \rho / \omega ^ { 2 } ) ( s / c ) ^ { 3 } \times \sin ^ { 2 } \theta | \cos \theta | ^ { - 1 } [ 1 + \cos ^ { 2 } \theta + ( s / v ) \sin ^ { 2 } \theta ] .
$$

Here $\pmb { S }$ and $v$ are'the velocities of shear waves and compressive waves, respectively, and $\pmb \theta$ is the angle between the direction of propagation of the waves and the normal to the surface.Considering a flux of $2 \times 1 0 ^ { - 5 } ~ \mathrm { e r g / c m ^ { 2 } }$ sec (an optimistic but conceivable value for waves from a pulsar) incident horizontally $\left( \theta = \pi / 2 \right.$ ; "divergent” factor $| \cos \theta | ^ { - 1 }$ cancels out in calculation!),and taking $\pmb { s }$ to be $4 . 5 \times 1 0 ^ { 5 } \mathrm { c m } / \mathrm { s t }$ ec and $\pmb { \omega }$ to be 6 rad/sec, he calculates that the l-Hz horizontal displacement produced in the surface has an amplitude of $\xi _ { 0 } \sim 2 \times 1 0 ^ { - 1 7 } \mathrm { c m }$ ,too small by a factor of the order of $1 0 ^ { 5 }$ to be detected against background seismic noise. He points to the possibilities of improvements,especially via resonance (elastic waves reflected back and forth between two surfaces; Antarctic ice sheet).

# 4. Normal-Mode Vibrations of an Elastic Bar

As of l972,the most often-discussed type of detector is the aluminum bar invented by Joseph Weber (l960, l961) [see Figures 37.l and 37.2(d)].Weber's bars are cylindrical in shape, with length $1 5 3 \mathrm { c m }$ ，diameter $6 6 \mathrm { c m }$ and weight $1 . 4 \times 1 0 ^ { 6 } \mathrm { g }$ Each bar is suspended by a wire in vacuum and is mechanically decoupled from its surroundings. Around its middle are attached piezoelectric strain transducers, which couple into electronic circuits that are sensitive to the bar's fundamental end-to-end mode of oscillation (frequency $\nu = 1 , 6 6 0 \mathrm { H z } )$ . When a gravitational wave hits the bar broadside,as shown in Figure 37.2(d), the relative accelerations carried by the wave will excite the fundamental mode of the bar.As of 1972,Weber observes sudden,simultaneous excitations in two such bars,one at the University of Maryland, near Washington, D.C.; the other at Argonne National Laboratory, near Chicago [see Weber (l969,l970a,b)]. No one has yet come forward with a workable explanation for Weber's coincidences other than gravitational waves from outer space. However, the history of physics is rich with instances where supposedly new effects had to be attributed in the end to long familiar phenomena. Therefore it would seem diffcult to rate the observed events as“battle-tested.”To achieve that confidence rating would seem to require confirmation with different equipment, or under different circumstances,or both;experiments to provide that confirmation are now (l972) underway. If one makes this tentative assessment, one can be excused for expressing at the same time the greatest admiration for the experimental ingenuity, energy,and magnificent persistence that Joseph Weber has shown in his more than decade-long search for the most elusive radiation on the books of physics.

Mechanical detectors of the above four types represent systems on which measurements have been made; so practical difficulties and realizable noise levels can be estimated properly. In the continuing search for improved methods,more elaborate detectors are being studied,and in l972 one can list a number of interesting proposals,as below.For these it is hard to know how much development would be required in order to achieve the desired performance.

# 5. Normal-Mode Vibrations of Elastic Bodies of Other Shapes

(5)elastic bodies of other shapes

The“bar” of a Weber detector need not be cylindrical in shape. For a discussion of a detector with the shape of a hollow square,a hoop, or a tuning fork, see Douglass (1971); such a detector might allow its fundamental frequency to be adjusted for the most favorable response, with given mass,or given maximum dimension,or both. Sections 37.4 and 37.7 and exercises 37.9 to 37.12 analyze in detail the operation of a “vibrating-bar” detector of arbitrary shape. See also Douglass and Tyson (1971).

# 6. Angular Accelerations of Rotating Bars

(6)rotating bars ("heterodyne detector.")

All the potential detectors described thus far respond in the most obvious of manners to the tidal accelerations of a gravitational wave: relative distances oscillate in and out. But the tidal accelerations contain, in addition to a length-changing component, also a tangential, rotation-producing component. In picture (a) of Box 37.2, the length-changing component dominates near the $\hat { x }$ and $\hat { y }$ axes, whereas the rotation-producing component dominates half-way between the axes. Vladimir B. Braginsky was the first to propose a detector that responds to the rotation-producing accelerations [see Braginsky, Zel'dovich,and Rudenko (l969)； Braginsky and Nazarenko (1971)]. It consists of two metal rods,oriented perpendicular to each other,and rotating freely with angular velocity $\omega _ { 0 }$ in their common plane [see Fig. 37.2(f)]. (The rotation is relative to the gyroscopes of the proper reference frame of the detector; equivalently, it is relative to the Lorentz frame local to the detector.) Let monochromatic gravitational waves of angular frequency $\omega = 2 \omega _ { 0 }$ (change of phase per unit of time equals twice the angular velocity at which the pattern of lines of force turns) impinge broadside on the rotating rods. The righthand circularly polarized component of the waves will then rotate with the rods; so their orientation in its lines-of-force diagram wil remain forever fixed. With the orientation of Fig. 37.2(f),rod A will undergo angular acceleration,while rod B will decelerate. The experimenter can search for the constant relative angular acceleration of the two rods (constant so long as the angle between them does not depart significantly from $9 0 ^ { \circ }$ ).Beter yet, the experimenter can (all too easily) adjust the rotation rate $\omega _ { 0 }$ so it does not quite match the waves' frequency $\omega$ Then for $\frac { 1 } { 2 } \omega _ { 0 } / | \omega - 2 \omega _ { 0 } |$ rotations, rod A will accelerate and B will decelerate； then will follow $\frac { 1 } { 2 } \omega _ { 0 } / | \omega - 2 \omega _ { 0 } |$ rotations in which A decelerates and B accelerates,and so on (frequency beating). The experimenter can search for oscillations in the relative orientation of the rods. One need not worry about the lefthand polarized waves marring the experiment. Since they do not rotate with the rods, their angular accelerations average out over one cycle.

Such a device is called a “heterodyne detector”by Braginsky.He envisages that such detectors might be placed in free-fall orbits about the Earth late in the $1 9 7 0 ^ { \circ } { \mathsf { s } } .$ Heterodyne detectors would work most efficiently for long monochromatic wave trains such as those from pulsars; but even for short bursts of waves they may be more sensitive than vibrating bars [see Braginsky and Nazarenko (l971)].

# 7. Angular Accelerations of Driven Oscillators

Andrei D. Sakharov (l969) has proposed a different type of detector for the angular accelerations of a gravitational wave. Instead of two rotating bars, it consists of two identical, driven oscillators,initially parallel and nonrotating,but oscillating out of phase with each other. Each oscillator experiences angular accelerations in one direction at one phase of a passing wave,and in the opposite direction at the next phase,but the torques do not cancel out. When the oscilator is maximally distended, it experiences a greater torque (acceleration $\propto$ length; torque $\propto$ length²) than when it is maximally contracted. Consequently, if the driven oscillations have the same angular frequency as a passing, monochromatic wave, and if the phases are as shown in Figure 37.2(g), then oscillator A will receive an angular acceleration in the righthand direction,while B receives an angular acceleration in the lefthand direction.

(7）rotation of driven oscillators

# 8. Pumping of Fluid in a Rotating Loop of Pipe

A third type of detector that responds to angular accelerations has been described by William Press (l970). This detector would presumably be far less sensitive than others,and therefore not worth constructing; but it is intriguing in its novel design; and it illustrates features of gravitational waves ignored by other detectors. Press's detector consists of a loop of rotating pipe, containing a superfluid. The shape of the pipe and its constant rotation rate are chosen so that the gravitational waves will pump the fluid around inside the pipe. One conceivable pipe design (a bad one to build in practice,but an easy one to analyze) is shown in Fig. 37.2(h). Note that use is made of the variation in tidal acceleration along the direction of propagation of the wave as well as perpendicular to that direction. To analyze the response of the fluid to a righthand circularly polarized wave,one can mentally place the rotating pipe in the three-dimensional line-of-force diagram of Box 37.2(c).

# EXERCISES

# ExerciSe 37.6. RELATIVE MOTION OF FREELY FALLING BODIES AS A DETECTOR OF GRAVITATIONAL WAVES [see Figures 37.2(a) and 37.3.]

Consider two test bodies initially at rest with respect to each other in flat, empty spacetime. (The case where other, gravitating bodies are nearby can be treated without too much more diffculty; but this exercise concerns only the simplest example!) A plane, nearly monochromatic gravitational wave, with angular frequency $\pmb { \omega }$ and polarization $e _ { + }$ ,impinges on the bodies,coming from the $- z$ direction.As shown in exercise 35.5,the bodies remain forever at rest in those TT coordinates that constituted the bodies’ global inertial frame before the wave arrived. Calculate,for arbitrary separations $( \varDelta x , \varDelta y , \varDelta z )$ of the test bodies,the redshift and the round-trip travel time of photons going back and forth between them. Compare the answer, for large $\pmb { \mathscr { s } } \pmb { x }$ 4y,4z,with the answer one would have obtained by using (without justification!） the equation of geodesic deviation. Physically,why does the correct answer oscillate with increasing separation? Discuss the feasibility and the potential sensitivity of such a detector using current technology.

# Exercise 37.7. EARTH-MOON SEPARATION AS A GRAVITATIONAL-WAVE DETECTOR

In the early $1 9 7 0 ^ { \circ } { \mathsf { s } }$ One can monitor the Earth-moon separation using laser ranging to a precision of $1 0 \mathrm { c m }$ ,with successive observations separated by at least one round-trip travel time.Suppose that no oscillations in round-trip travel time are observed except those (of rather long periods) to be expected from the Earth-moon-sun-planets gravitational interaction. What limits can one then place on the energy fux of gravitational waves that pass the Earth? The mathematical formula for the answer should yield numerically 4

$$
\mathrm { F l u x } \lesssim 1 0 ^ { 1 8 } ~ \mathrm { e r g / c m ^ { 2 } ~ s e c ~ f o r } ~ 0 . 3 ~ \mathrm { c y c l e / s e c } \lesssim \nu \lesssim 1 ~ \mathrm { c y c l e / d a y } ,
$$

corresponding to a limit on the mass density in gravitational waves of

$$
\mathrm { D e n s i t y } \lesssim 1 0 ^ { - 1 3 } ~ \mathrm { g / c m } ^ { 3 } .
$$

Why is this an uninteresting limit?

# $\$ 37.4$ .VIBRATING，MECHANICAL DETECTORS: INTRODUCTORY REMARKS

Theremainder ofthis chapter (except for $\ S 3 7 . 9$ gives adetailed analysis of vibrating, mechanical detectors (Earth; Weber bar; “bars” with complex shapes; and so on).

The details of the analysis and its applications depend in a crucial way on the values of two dimensionless numbers: (l） the ratio $\pmb { \tau _ { \mathtt { G W } } } / \pmb { \tau _ { 0 } }$ ,where

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0015_pages_0981-1050/auto/images/c654d74ec270a9981ac060b28f2d78b5dd2902feff701ba972745996f3efeed4.jpg)

$$
\begin{array} { r l } & { \tau _ { \mathsf { G W } } \equiv \left( \begin{array} { l } { \mathrm { c h a r a c t e r i s t i c ~ t i m e ~ s c a l e ~ f o r ~ c h a n g e s ~ i n } } \\ { \mathrm { g r a v i t a t i o n a l - w a v e ~ a m p l i t u d e ~ a n d ~ s p e c t r u m } } \end{array} \right) , } \\ & { \tau _ { 0 } \equiv \left( \begin{array} { l } { e \mathrm { - f o l d i n g ~ t i m e ~ f o r ~ d e t e c t o r ~ v i b r a t i o n s ~ ( i n } } \\ { \mathrm { n o r m a l ~ m o d e ~ o f ~ i n t e r e s t } \ ) \ \mathrm { t o ~ d i e ~ o u t ~ a s } } \\ { a \mathrm { ~ r e s u l t ~ o f ~ i n t e r n a l ~ d a m p i n g } } \end{array} \right) ; } \end{array}
$$

The rest of this chapter is Track 2. No earlier track-2 material is needed as preparation for it, nor is it needed for any later chapter.

and (2) the ratio $\overline { { E } } _ { \mathrm { v i b r a t i o n } } / k T ,$ where

$$
\begin{array} { r } { \bar { E } _ { \mathrm { v i b r a t i o n } } \equiv \left( \begin{array} { l l } { \mathrm { m e a n ~ v a l u e ~ o f ~ d e t e c t o r ' s ~ v i b r a t i o n ~ e n e r g y ~ ( i n ) } } \\ { \mathrm { n o r m a l ~ m o d e ~ o f ~ i n t e r e s t ) ~ w h i l e ~ w a v e s ~ a r e } } \\ { \mathrm { p a s s i n g ~ a n d ~ d r i v i n g ~ d e t e c t o r } } \end{array} \right) , } \end{array}
$$

$$
\begin{array} { r l } & { k T { \equiv } \binom { \mathrm { B o l t z m a n ~ } ^ { \circ } } { \mathrm { c o n s t a n t } } \times \binom { \mathrm { d e t e c t o r } ^ { \circ } } { \mathrm { t e m p e r a t u r e } } } \\ & { ~ } \\ & { ~ { = } \binom { \mathrm { M e a n ~ e n e r g y ~ i n ~ n o r m a l ~ m o d e } } { \mathrm { o f ~ i n t e r e s t ~ w h e n ~ g r a v i t a t i o n a l } } . } \\ & { ~ { - } \quad \operatorname { w a v e s ~ a r e ~ n o t ~ e x c i t i n g ~ i t } } \end{array}
$$

When $\tau _ { \tt G W } \gg \tau _ { 0 }$ ,the detector views the radiation as having a“steady $\mu u x , ^ { \ast }$ and it responds with steady-state vibrations; when $\tau _ { \tt G W } \ll \tau _ { 0 }$ (short burst of waves), the waves deal a “hammer blow” to the detector. When $\overline { { E } } _ { \mathrm { v i b r a t i o n } } \gg k T ,$ the driving force of the waves dominates over the detector's random, internal, Brownian-noise forces ("wave-dominated detector"); when $\overline { { E } } _ { \mathrm { v i b r a t i o n } } \lesssim k T ,$ the driving force of the waves must compete with the detector's random,internal, Brownian-noise forces ("noisy detector").

Sections 37.5 to37.7 deal with wave-dominated detectors $( \overline { E } _ { \mathrm { v i b r a t i o n } } \gg k T )$ .The key results of those sections are summarized in Box 37.3,which appears here as a quick preview (though it may not be fully understandable in advance). Section 37.8 treats noisy detectors.

Definitions:"steady flux," "hammer-blow waves." "wave-dominated detector." "noisy detector"

Warning: Throughout the rest of this chapter prime attention focuses on the concept of cross section.This is fine for a first introduction to the theory of detectors. But cross section is not the entire story,especially when one wishes to study the detailed wave-form of the radiation. And sometimes (e.g., for the detector of Figure 37.2a),it is none of the story. A first-rate experimenter designing a new detector will not deal primarily in cross sections any more than a radio engineer will in designinga new radio telescope. Attention will also focus heavily on the bandwidth

(continued on page 1022)

Design of detectors requires much more than the concept of cross section

# Box 37.3 WAYS TO USE CROSS SECTION FOR WAVE-DOMINATED DETECTORS

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0015_pages_0981-1050/auto/images/14a6c1b47cd78759f1dfb8b18688464a6af637731cc689259111950949a34c52.jpg)

# B. To Calculate Total Energy Deposited in Detector by any Pessing Wave train

I.lf frequency distribution of radiation is arbitrary:

erg/cm Hz cm··.Hz.

2.1f frequency spread of radiation is small compared to line width of detector ("monochromatic waves"):

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0015_pages_0981-1050/auto/images/431b8febacc411ada683284bd14338262f3606d7c51c6e876e6719d3b8e00e76.jpg)

3. If frequency spread of radiation is large compared to line widthof detector (as it must be for hammer-blow radiation. where.. $\begin{array} { r l } & { \underbrace { \vphantom { \int _ { \theta _ { \theta } ( \phi _ { \theta } ) } } d \nu _ { \mathrm { s o u r c e } } \gtrsim 1 / \smash { \vphantom { \int _ { \theta } } 4 \overline { { \pi _ { \tau _ { \mathrm { G W } } } } } \gg 1 / 4 \pi \tau _ { 0 } } } _ { \mathrm { ( t o t a l ~ e n e r g ~ d e p o s i t e d ) } } = \delta _ { \mathrm { e l e t e c t o r } } } \\ & { \underbrace { \vphantom { \int _ { \theta _ { \theta } ( \phi _ { \theta } ) } } \langle \widetilde { \mathcal { G } } _ { \underline { { \nu } } } \rangle ^ { \prime } \delta _ { \mathrm { d e t e c t o r } } } _ { \mathrm { e r g / c m ^ { 2 } ~ H z } } \underbrace { \int _ { \sigma ( \nu ) } d \nu } _ { \mathrm { c m ^ { 2 } ~ H z } } } \end{array}$ "resonance integral"

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0015_pages_0981-1050/auto/images/b0a944e1e23e6fb1d7a8832e61f0776140d20be33a6912f169f5caa0f5f06bc8.jpg)

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0015_pages_0981-1050/auto/images/4c0b029eea2b76be79f28400805bff749e711864bef00119ae8f73adb6267fdc.jpg)  
Figure 37.4. An idealized detector (vibrator）responding to linearly polarized gravitational waves,

of the antenna,and on other,more detailed characteristics of its response,on coupling of the antenna to the displacement sensor, on response characteristics of the sensor, on antenna noise,on sensor noise,and so on. For an overview of these issues,and for discussions of detectors for which the concept of cross section is useless, see,e.g.,Press and Thorne (1972).

# \$37.5. IDEALIZED WAVE-DOMINATED DETECTOR, EXCITED BY STEADY FLUX OF MONOCHROMATIC WAVES

$^ { * } { }$

Idealized detector: oscillator driven bya steady flux of monochromatic waves:

(1）derivation of equation of motion

Begin with the case of a wave-dominated detector $( \overline { { E } } _ { \mathrm { v i b r a t i o n } } \gg k T )$ being driven by a steady flux of radiation $( \tau _ { \mathtt { G W } } \gg \tau _ { 0 } )$ . Deal at first, not with a solid bar of arbitrary shape, but rather with the idealized detector of Figure 37.4: an oscillator made of two masses $M$ on the ends of a spring of equilibrium length $2 L$ Let the detector have a natural frequency of vibration $\omega _ { 0 }$ and a damping time $\tau _ { 0 } \gg 1 / \omega _ { 0 } ,$ so that its equation of motion (in the detector's proper reference frame) is

$$
\ddot { \xi } + \dot { \xi } / \tau _ { 0 } + \omega _ { 0 } ^ { 2 } \xi = \mathrm { d r i v i n g ~ a c c e l e r a t i o n } .
$$

Let gravitational waves of polarization ${ \pmb { e } } _ { + }$ and angular frequency $\omega$ impinge on the detector from the $- \hat { z }$ direction; and let the polar angles of the detector relative to the wave-determined $\hat { x } , \hat { y } , \hat { z } \mathrm { . }$ -axes be $\pmb \theta$ and $\phi$

The incoming waves are described by equations (37.1) with the amplitude

$$
A _ { \times } = 0 , ~ A _ { + } = \mathcal { a } _ { + } e ^ { - i \omega ( t - z ) } .
$$

(Here and throughout one must take the real part of all complex expressions.)


<!-- chunk 0016: pages 1051-1120 -->
Assume that the detector is much smaller than a wavelength, so that one can set $z \approx \hat { z } = 0$ throughout it. Then the tidal accelerations produced by the wave

$$
\begin{array} { r l } & { \left( \frac { d ^ { 2 } \hat { x } } { d \hat { t } ^ { 2 } } \right) _ { \mathrm { d u e t o w a v e } } = - R _ { \hat { x } 0 \hat { y } 0 } x ^ { \hat { j } } = - \frac { 1 } { 2 } \omega ^ { 2 } \mathcal { A } _ { + } e ^ { - i \omega \hat { t } } \hat { x } , } \\ & { \left( \frac { d ^ { 2 } \hat { y } } { d \hat { t } ^ { 2 } } \right) _ { \mathrm { d u e t o w a v e } } = - R _ { \hat { y } 0 \hat { j } 0 } x ^ { \hat { j } } = + \frac { 1 } { 2 } \omega ^ { 2 } \mathcal { A } _ { + } e ^ { - i \omega \hat { t } } \hat { y } , } \end{array}
$$

have as their component along the oscillator

$$
\begin{array} { l } { { \displaystyle \frac { d ^ { 2 } \xi } { d t ^ { 2 } } = \frac { \hat { x } } { L } \frac { d ^ { 2 } \hat { x } } { d t ^ { 2 } } + \frac { \hat { y } } { L } \frac { d ^ { 2 } \hat { y } } { d t ^ { 2 } } + \frac { \hat { z } } { L } \frac { d ^ { 2 } \hat { z } } { d t ^ { 2 } } = - \frac { 1 } { 2 } \omega ^ { 2 } \mathcal { A } _ { + } L e ^ { - \mathrm { i } \omega \hat { t } } \frac { \hat { x } ^ { 2 } - \hat { y } ^ { 2 } } { L ^ { 2 } } } } \\ { { \displaystyle \quad = - \frac { 1 } { 2 } \omega ^ { 2 } \mathcal { A } _ { + } L e ^ { - \mathrm { i } \omega \hat { t } } \mathrm { s i n } ^ { 2 } \theta \mathrm { c o s } 2 \phi . } } \end{array}
$$

Consequently, the equation of motion for the oscillator is

$$
\ddot { \xi } + \dot { \xi } / \tau _ { 0 } + \omega _ { 0 } { } ^ { 2 } \xi = - \frac { 1 } { 2 } \omega ^ { 2 } \mathcal { Q } _ { + } L e ^ { - \mathrm { i } \omega \hat { t } } \sin ^ { 2 } \theta \cos 2 \phi .
$$

The driving force varies as cos $2 \phi$ because of the “spin- $z ^ { \dag }$ nature of gravitational waves: a rotation through $1 8 0 ^ { \circ }$ in the transverse plane leaves the waves unchanged; a rotation through $9 0 °$ reverses the phase.The $\sin ^ { 2 } \theta$ term results from the transverse nature of the waves [one factor of sin $\pmb \theta$ to account for projection onto the detector's direction], plus their tidal-force nature another factor of sin $\pmb \theta$ to account for (relative force) $\propto$ (distance in transverse plane)].

The straightforward steady-state solution of the equation of motion (37.15) is

$$
\xi = \frac { \frac { 1 } { 2 } \omega ^ { 2 } \mathcal { Q } _ { + } L \sin ^ { 2 } \theta \cos 2 \phi } { \omega ^ { 2 } - { \omega _ { 0 } } ^ { 2 } + i \omega / \tau _ { 0 } } e ^ { - i \omega \hat { t } } .
$$

(2)oscillator amplitudeas function of frequency and orientation

When the incoming waves are near resonance with the detector, $| \omega \pm \omega _ { 0 } | \lesssim 1 / \tau _ { 0 } ,$ the oscilltor is excited to large amplitude. Otherwise the excitation is small. Focus attention henceforth on near-resonance excitations; then equation (37.l6) can be simplified (note: $\omega _ { 0 }$ is positive, but $\omega$ may be negative or positive):

$$
\xi = \frac { \displaystyle \frac { 1 } { 4 } \omega _ { \scriptscriptstyle 0 } \mathcal { Q } _ { + } L \sin ^ { 2 } \theta \cos 2 \phi } { \displaystyle \vert \omega \vert - \omega _ { \scriptscriptstyle 0 } + \frac { 1 } { 2 } \mathrm { s g n } ( \omega ) i / \tau _ { \scriptscriptstyle 0 } } e ^ { - i \omega \hat { t } } .
$$

One measure of the detector's usefulness is its cross section for absorbing gravitational-wave energy.The steady-state vibrational energy in a detector with the above amplitude and with 2 masses $M$ is

$$
E _ { \mathrm { v 1 b r a t i o n } } = 2 \cdot { \frac { 1 } { 2 } } \cdot M \cdot ( { \dot { \xi } } ^ { 2 } ) _ { \mathrm { m a x } } = { \frac { { \frac { 1 } { 1 6 } } M L ^ { 2 } \omega _ { 0 } { } ^ { 4 } { \mathcal { Q } } _ { + } ^ { ~ 2 } \sin ^ { 4 } \theta \cos ^ { 2 } 2 \phi } { ( | \omega | - \omega _ { 0 } ) ^ { 2 } + ( 1 / 2 \tau _ { 0 } ) ^ { 2 } } } .
$$

This energy is being dissipated internally at a rate $E _ { \mathrm { v i b r a t i o n } } / \tau _ { 0 }$ . If one ignores reradiation of energy as gravitational waves (a negligible process!), one can equate the dissipation rate to the rate at which the detector absorbs energy from the incoming waves-which in turn equals the “cross section” $\pmb { \sigma }$ times the incoming flux:

$$
E _ { \mathrm { v i b r a t i o n } } / \tau _ { 0 } = - d E _ { \mathrm { w a v e s } } / d t = \sigma T ^ { 0 z ( \mathrm { G W } ) } = \frac { 1 } { 3 2 \pi } \sigma \omega ^ { 2 } \mathcal { d } _ { + } { ^ 2 } .
$$

(3) cross sections for polarized radiation

Consequently, near resonance $( | \omega \pm \omega _ { 0 } | \ll \omega _ { 0 } )$ ，the cross section for interception of gravitational-wave energy is

(4) cross sections for unpolarized radiation

$$
\sigma = \frac { 2 \pi M L ^ { 2 } ( { \omega _ { 0 } } ^ { 2 } / \tau _ { 0 } ) \sin ^ { 4 } \theta \cos ^ { 2 } 2 \phi } { ( | \omega | - \omega _ { 0 } ) ^ { 2 } + ( 1 / 2 \tau _ { 0 } ) ^ { 2 } } , ~ \mathrm { f o r ~ p o l a r i z e d ~ r a d i a t i o n } .
$$

This expression applies to monochromatic radiation. However, experience with many Other kinds of waves has taught that one often has to deal with a broad continuum of frequencies,with the“bandwidth”of the incident radiation far greater than the width of the detector resonance (see Box 37.3). Under these conditions, the relevant quantity is not the cross section itself, but the “resonance integral' of the cross section,

$$
\int _ { \mathrm { r e s o n a n c e } } \sigma d \nu = \int \sigma ( d \omega / 2 \pi ) = 2 \pi M L ^ { 2 } \omega _ { 0 } ^ { \ 2 } \sin ^ { 4 } \theta \cos ^ { 2 } 2 \phi ,
$$

for polarized radiation.

Before examining the magnitude of this cross section, scrutinize its directionality (the“antenna-beam pattern"). The factor of $\sin ^ { 4 } \theta \cos ^ { 2 } 2 \phi$ refers to linearly polarized, ${ \pmb { e } } _ { + }$ radiation (see Figure 37.4). For the orthogonal mode of polarization, ${ \pmb \theta } _ { \times }$ ， $\cos ^ { 2 } 2 \phi$ is to be replaced by $\sin ^ { 2 } 2 \phi$ ； and for unpolarized (incoherent mixture) radiation or circularly polarized radiation, the cross section is the average of these two expressions; thus

$$
\sigma = \frac { \pi M L ^ { 2 } ( { \omega _ { 0 } } ^ { 2 } / \tau _ { 0 } ) \sin ^ { 4 } \theta } { ( | \omega | - \omega _ { 0 } ) ^ { 2 } + ( 1 / 2 \tau _ { 0 } ) ^ { 2 } } \mathrm { f o r ~ u n p o l a r i z e d ~ r a d i a t i o n } .
$$

Notice that this unpolarized cross section is peaked,with half-width $3 3 ^ { \circ }$ ,about the equatorial plane of the detector. Averaged over all possble directions of incoming waves, the cross section is

$$
\begin{array} { r } { \langle \sigma \rangle _ { \mathrm { a l l d i r e c t i o n s } } = \displaystyle \frac { 1 } { 2 } \int _ { 0 } ^ { \pi } \sigma \sin \theta d \theta = \frac { 8 } { 1 5 } \sigma _ { \mathrm { m a x } } } \\ { = \displaystyle \frac { ( 8 \pi / 1 5 ) M L ^ { 2 } ( { \omega _ { 0 } } ^ { 2 } / \tau _ { 0 } ) } { ( | \omega | - \omega _ { 0 } ) ^ { 2 } + ( 1 / 2 \tau _ { 0 } ) ^ { 2 } } \mathrm { f o r } } \end{array}
$$

One can rewrite the above cross sections in several suggestive forms. For example, On resonance,the cross section (37.21） reads

$$
\langle \sigma \rangle _ { \mathrm { a l l d i r e c t i o n s } } = \frac { 4 \pi ^ { 2 } } { 1 5 } \frac { 4 M } { 2 \pi / \omega _ { 0 } } ( \omega _ { 0 } \tau _ { 0 } ) ( 2 L ) ^ { 2 } .
$$

Recall that $\omega _ { 0 } \tau _ { 0 }$ defines the $" Q '$ of a detector, $1 / Q \equiv$ (fraction of energy dissipated per radian of oscillation). Note that $2 \pi / \omega _ { 0 }$ is the wavelength $\lambda _ { 0 }$ of resonant radiation. Finally,denote by $r _ { g } = 4 M$ the gravitational radius of the detector.In terms of these three'familiar quantities, find for the cross section the formula

$$
\begin{array} { r } { \frac { \langle \sigma \rangle _ { \mathrm { a l l d i r e c t i o n s } } } { ( 2 L ) ^ { 2 } } = \frac { \left( \mathrm { c r o s s ~ s e c t i o n ~ f o r ~ a b s o r b i n g ~ w a v e s ~ o n ~ r e s o n a n c e } \right) } { ( ^ { \ast } \ g e o m e \mathrm { t r i c } ^ { \ast } ) _ { \mathrm { ~ c r o s s ~ s e c t i o n ~ o f ~ d e t e c t o r } } } } \\ { = ( 4 \pi ^ { 2 } / 1 5 ) ( r _ { g } / \lambda _ { 0 } ) Q \phantom { \frac { \mathrm { f o r ~ u n p o l a r i z e d ~ r a d i a t i o n } } { \mathrm { f o r ~ r e s o n a n c e } } } } \end{array}
$$

Magnitude of cross sections forany resonant detector

This relation holds in order of magnitude for any resonant detector. It shows starkly that gravitational-wave astronomy must be a diffcult enterprise.How large could you make the factor $r _ { g } / \lambda _ { 0 } ,$ given a reasonable budget? Weber's 1970 detectors have $2 L _ { \mathrm { e f f e c t i v e } } \approx 1$ meter, $r _ { g } \approx ( 0 . 7 4 \times 1 0 ^ { - 2 8 } \ \mathrm { c m / g } ) \times ( 1 0 ^ { 6 } \ \mathrm { g } ) \approx 1 0 ^ { - 2 2 } \ \mathrm { c m }$ ， $\nu _ { 0 } = \omega _ { 0 } / 2 \pi =$ $1 { , } 6 6 0 \ \mathrm { H z }$ $\lambda _ { 0 } \approx 2 0 0 \mathrm { k m }$ ， $r _ { g } / \lambda _ { 0 } \approx \frac { 1 } { 2 } \times 1 0 ^ { - 2 9 }$ ， $\tau _ { 0 } \approx 2 0$ sec, $Q \approx 2 \times 1 0 ^ { 5 }$ ； so that

What flux of gravitational-wave energy would have to be incident to excite a cold detector $( { \sim } 0 ^ { \circ } \mathrm { ~ K ) }$ into roughly steady-state vibrations with a vibration energy of (Boltzmann's constant) $\times$ (room temperature) $\sim 4 \times 1 0 ^ { - 1 4 }$ erg? The vibrator, if cooled enough to be wave-dominated, disspates its energy at the rate $E _ { \mathrm { v i b r a f i o n } } / \tau _ { 0 }$ $\sim 2 \times 1 0 ^ { - 1 5 }$ erg/sec. The incident flux has to make up this loss,at the rate

Flux required to excite a Weber-type detector

$$
T _ { 0 0 } ^ { ( \mathrm { G W ) } } \sigma \sim 2 \times 1 0 ^ { - 1 5 } \mathrm { e r g / s e c } ,
$$

implying an incident flux of the order of $2 \times 1 0 ^ { - 1 5 } / 3 \times 1 0 ^ { - 2 0 } \sim 1 0 ^ { 5 } ~ \mathrm { e r g / c m ^ { 2 } ~ s e c }$ Moreover, this flux has to be concentrated in the narrow range of resonance

$$
\nu \approx \nu _ { 0 } \pm 1 / 4 \pi \tau _ { 0 } = ( 1 6 6 0 \pm 0 . 0 0 4 ) \mathrm { H z } .
$$

By anybody's standards,this is a very high flux of gravitational radiation for such a small bandwidth $( \sim 1 0 ^ { 7 } ~ \mathrm { e r g / c m ^ { 2 } }$ sec $\mathbf { H } \mathbf { \mathfrak { z } }$ ，as compared to the flux of blackbody gravitational radiation, $8 \pi \nu ^ { 2 } k T / c ^ { 2 } = 3 \times 1 0 ^ { - 2 7 } \mathrm { ~ e r g / c m ^ { 2 } }$ sec $\mathbf { H } \mathbf { \mathfrak { z } } _ { \mathfrak { i } }$ ，that would corre-spond to Planck equilibrium at the same temperature; the large factor of difference is a direct reflection of the difference in rate of damping of the oscillator by friction and by gravitational radiation).

Equation (37.22) makes it seem that an optimal detector must have a large $Q$ This is not necessarily so. Recall that the bandwidth, $\scriptstyle 4 \omega \approx \omega _ { 0 } / Q$ ,over which the cross section is large, decreases with increasing $Q$ 、When an incoming steady flux of waves of bandwidth $\Delta \omega \gg \omega _ { 0 } / Q \equiv 1 / \tau _ { 0 }$ and of specific flux

A large $\pmb { \alpha }$ is not necessarily optimal

$$
F _ { \nu } ( { \mathrm { e r g / c m ^ { 2 } s e c H z } } )
$$

drives the detector, it deposits energy at the rate

$$
\binom { \mathrm { r a t e ~ o f ~ d e p o s i t } } { \mathrm { o f ~ e n e r g y } } = \frac { d E } { d t } = \int _ { \mathrm { \tiny ~ r e s o n a n c e } } F _ { \nu } \sigma d \nu = F _ { \nu } ( \nu _ { 0 } ) \int _ { \mathrm { \tiny ~ r e s o n a n c e } } \sigma d \nu .
$$

Consequently, the relevant measure of detector effectiveness will be the integral of the cross section over the resonance, $\int \sigma d \nu ( 3 7 . 1 9 )$ . (See next section.) This frequencyintegrated cross section is independent of the detector's $Q$ ,so one must use more sophisticated reasoning (e.g. signal-to-noise theory) in deciding whether a large $Q$ is desirable. (See $\ S 3 7 . 8 )$

# $\$ 37.6$ .IDEALIZED，WAVE-DOMINATED DETECTOR, EXCITED BY ARBITRARY FLUX OF RADIATION

Response of idealized detector to an arbitrary, non-monochromatic flux:

（1）derivation

Let plane-polarized waves of polarization ${ \pmb \ 6 } _ { + }$ but arbitrary spectrum [equation (37.1) with $A _ { \times } = 0 \dot { }$ impinge on the idealized detector of Figure 37.4. Then the equation of motion for the detector is the same as for monochromatic waves [equation (37.15)], but with $- \omega ^ { 2 } \mathcal { Q } _ { + } e ^ { - i \omega t }$ replaced by $\ddot { A } _ { + }$ ：

$$
\ddot { \xi } + \dot { \xi } / \tau _ { 0 } + \omega _ { 0 } { } ^ { 2 } \xi = \frac { 1 } { 2 } \ddot { A } _ { + } L \sin ^ { 2 } \theta \cos 2 \phi .
$$

[By now one is fully accustomed to the fact that all analyses of detectors (when the detector is much smaller than the wavelength of the waves) are performed in the proper reference frame, with coordinates $\hat { t , x , y , z } .$ Henceforth,for easeof eyesight, abandon the“hats” on these “proper coordinates,” and denote them as merely t, x, y，2]

Fourier-analyze the waves and the detector displacement,

$$
\begin{array} { c } { { A _ { + } ( t ) = ( 2 \pi ) ^ { - 1 / 2 } \displaystyle \int _ { - \infty } ^ { + \infty } \widetilde { \cal A } _ { + } ( \omega ) e ^ { - i \omega t } , } } \\ { { \xi ( t ) = ( 2 \pi ) ^ { - 1 / 2 } \displaystyle \int _ { - \infty } ^ { + \infty } \widetilde { \xi } ( \omega ) e ^ { - i \omega t } ; } } \end{array} .
$$

and conclude from equation (37.26) that

$$
\widetilde \xi = \frac { \displaystyle \frac { 1 } { 2 } \omega ^ { 2 } \widetilde A _ { + } L \sin ^ { 2 } \theta \cos 2 \phi } { \displaystyle \omega ^ { 2 } - \omega _ { 0 } ^ { 2 } + i \omega / \tau _ { 0 } } .
$$

This Fourier amplitude is negligible unless $| \omega \pm \omega _ { 0 } | \ll \omega _ { 0 } ;$ consequently,without loss of accuracy, one can rewrite it as

$$
\widetilde { \xi } = \frac { \displaystyle \frac { 1 } { 4 } \omega _ { 0 } \widetilde { A } _ { + } L \sin ^ { 2 } { \theta } \cos { 2 \phi } } { \displaystyle \vert \omega \vert - \omega _ { 0 } + \frac { 1 } { 2 } \operatorname { s g n } ( \omega ) i / \tau _ { 0 } } .
$$

[Compare with the steady-state amplitude (37.16).]

Ask how much total energy is deposited in the.detector by the gravitational waves. Do not seek an answer by examining the amplitude of the vibrations, $\xi ( t )$ directly; since that amplitude is governed by both inteinal damping and the driving force of the waves,it does not reflect directly the energy deposited.To get the total energy deposited,integrate over time the force acting on each mass multiplied by its velocity:

$$
\begin{array} { r } { \Bigl ( \underset { \mathrm { d e p o s i t e d } } { \mathrm { t o t a l ~ e n e r g y } } \Bigr ) = \int _ { - \infty } ^ { + \infty } 2 \left. \frac { 1 } { 2 } M \ddot { A _ { + } } L \sin ^ { 2 } \theta \cos 2 \phi \right. \dot { \xi } d t . } \\ { \dot { \mathrm { : } } \qquad [ 2 \mathrm { m a s s e s } ] } \end{array}
$$

Use Parseval's theorem (one of the most powerful tools of mathematical physics!) to replace the time integral by a frequency integral

$$
\binom { \mathrm { t o t a l ~ e n e r g y } } { \mathrm { d e p o s i t e d } } = \Re \int _ { - \infty } ^ { + \infty } ( M L \sin ^ { 2 } \theta \cos 2 \phi ) ( - \omega ^ { 2 } \widetilde { A } _ { + } ^ { * } ) ( - i \omega \widetilde { \xi } ) d \omega .
$$

Then use equation (37.28) to rewrite this entirely in terms of the wave amplitude

$$
\binom { \mathrm { t o t a l ~ e n e r g y } } { \mathrm { d e p o s i t e d } } = \int _ { - \infty } ^ { + \infty } \bigg [ \frac { 2 \pi ( \omega _ { 0 } ^ { ~ 2 } / \tau _ { 0 } ) M L ^ { 2 } \sin ^ { 4 } \theta \cos ^ { 2 } 2 \phi } { ( | \omega | - \omega _ { 0 } ) ^ { 2 } + ( 1 / 2 \tau _ { 0 } ) ^ { 2 } } \bigg ] \bigg [ \frac { \omega ^ { 2 } | \widetilde { A } _ { + } | ^ { 2 } } { 1 6 \pi } \bigg ] d \omega .
$$

The first term in this expression is precisely the cross section for monochromatic waves,derived in the last section (37.18). The second term has an equally simple interpretation: the total energy that the gravitational waves carry past a unit surface area of detector is

$$
\begin{array} { r } { \mathcal { F } ( \mathrm { e r g s } / \mathrm { c m } ^ { 2 } ) = \displaystyle \int T _ { 0 0 } ^ { ( \mathrm { G W } ) } d t = \int \frac { 1 } { 1 6 \pi } \dot { A _ { + } } ^ { 2 } d t } \\ { = \displaystyle \int \frac { \omega ^ { 2 } | \widetilde { A _ { + } } | ^ { 2 } } { 1 6 \pi } d \omega = \int \frac { \omega ^ { 2 } | \widetilde { A _ { + } } | ^ { 2 } } { 8 } d \nu } \end{array}
$$

(Parseval's theorem again!). Consequently, the energy per unit frequency interval, per unit area carried by the waves is

$$
\mathcal { F } _ { \nu } ( \mathrm { e r g s } / \mathrm { c m ^ { 2 } H z } ) = \frac { 1 } { 8 } \omega ^ { 2 } | \widetilde { A } _ { + } | ^ { 2 }
$$

[for $- \infty < \nu < + \infty$ ； double this for $0 < \nu < + \infty$ ,a convention we use for the rest of this chapter]. This is $\mathtt { 2 } \pi$ times the second term in (37.29).

Combining equations (37.18), (37.29),and (37.31),then,one finds

(2)answer-

$$
\binom { \mathrm { t o t a l ~ e n e r g y } } { \mathrm { d e p o s i t e d } } = \int \sigma ( \nu ) \mathcal { F } _ { \nu } ( \nu ) d \nu .
$$

$$
\left( \mathsf { \Pi } _ { \mathsf { d e p o s i t e d } } ^ { \mathsf { e n e r g y } } \right) = \int \sigma \mathcal { F } _ { \nu } d \nu
$$

This is the total energy deposited,regardlessofthe spectrum ofthe waves,and regardless of whether they come in a steady flux for a long time,or in a short burst,or in any other form. It is perfectly general-so long as the detector is wave-dominated $( E _ { \mathrm { v i b r a t i o n } } \gg k T )$ while the waves are driving it.

How can an experimenter measure the total energy deposited? He cannot measure it directly, in general, but he can measure a quantity equal to it: the total energy that goes into internal damping,i.e.,into“friction.”Energy is removed by“friction” at a rate $E _ { \mathrm { v i b r a t i o n } } / \tau _ { 0 } ,$ when the vibration energy is much greater than $k T$ (during period of wave-dominance). Therefore,the experimenter can measure

$$
\begin{array} { l } { { \displaystyle \left( \mathrm { \ t o t a l \ e n e r g y } \right) = \frac { 1 } { \tau _ { 0 } } \int E _ { \mathrm { v i b r a t i o n } } \ d t , \quad \mathrm { ~ i n ~ g e n e r a l . } \quad } } \\ { { \displaystyle \left. \left( \mathrm { \ t i n t e g r a t e \ o v e r \ t h e \ p e r i o d \ t h a t \ } E _ { \mathrm { v i b r a t i o n } } \geqslant k T \right] \right. } } \end{array}
$$

In the special case of “hammer-blow waves”( $\mathbf { \tau _ { G w } = }$ duration of $\mathrm { w a v e s } \ll \tau _ { 0 } )$ ，the vibrationenegisdrieninstateoro ${ \sim } k T$ to a peak value, $E$ peatio $\gg k T ,$ and then decays exponentially back to ${ \sim } k T$ thus

$$
{ \binom { \mathrm { t o t a l ~ e n e r g y } } { \mathrm { d e p o s i t e d } } } = { \frac { 1 } { \tau _ { 0 } } } \int _ { 0 } ^ { \infty } E _ { \mathrm { v i b r a t i o n } } ^ { \mathrm { p e a k } } e ^ { - t / \tau _ { 0 } } d t = E _ { \mathrm { v i b r a t i o n } } ^ { \mathrm { p e a k } }
$$

for hammer-blow waves.

When the waves are steady for a long period of time $( \tau _ { \tt G W } \gg \tau _ { 0 } )$ , with specific flux

$$
{ \cal F } _ { \nu } = { \mathcal G } _ { \nu } / \tau _ { \mathrm { G W } } \qquad ( \mathrm { e r g s / c m ^ { 2 } ~ s e c ~ H z } ) ,
$$

then the energy will be deposited at a constant rate

$$
( d E / d t ) = ( \mathrm { t o t a l \ e n e r g y \ d e p o s i t e d } ) / \tau _ { \mathrm { G W } } ;
$$

and equation (37.32) can be rewritten

$$
\binom { \mathrm { r a t e ~ o f ~ d e } \mathrm { p o s i t } } { \mathrm { o f ~ e n e r g y } } = \int \sigma ( \nu ) F _ { \nu } d \nu , \qquad \mathrm { f o r ~ s t e a d y ~ w a v e s ~ } ( \tau _ { \mathrm { G W } } \gg \tau _ { 0 } ) .
$$

Equations (37.32) and (37.35) are the key equations for application of the concept of cross section to realistic situations.They are applicable not only to polarized radiation, but also to unpolarized radiation and to radiation coming in from all directions, if one merely makes sure to use the appropriate cross section [equation (37.20) or (37.21) instead of (37.18)]. For examples of their application,see Box 37.3.

# \$37.7. GENERAL WAVE-DOMINATED DETECTOR, EXCITED BY ARBITRARY FLUX OF RADIATION

The cross sections of the idealized spring-plus-mass detector can be put into a form more elegant than equations (37.18)to (37.21)-a form that makes contact with many

branches of physics,and is valid for any vibrating resonant detector whatsoever.

Introduce the“Einstein $\pmb { A }$ -coefficients,”which describe the rate at which a unit amount of detector energy is lost to internal damping and to reradiation of gravitational waves:

$$
A _ { \mathrm { d i s s } } \equiv \left( \frac { \mathrm { r a t e ~ a t ~ w h i c h ~ e n e r g y ~ i s ~ d i s s i p a t e d ~ i n t e r n a l l y } } { \mathrm { e n e r g y ~ i n ~ o s c i l l a t i o n s ~ o f ~ d e t e c t o r } } \right) = \frac { 1 } { \tau _ { 0 } } ,
$$

$$
A _ { \tt G W } \equiv \left( \frac { \mathrm { r a t e ~ a t ~ w h i c h ~ e n e r g y ~ i s ~ r e r a d i a t e d } } { \tt e n e r g y ~ i n ~ o s c i l l a t i o n s } \right) .
$$

For the idealized detector of Figure 37.4,the standard formula (36.1) for the emission of gravitational waves yields

$$
( \mathsf { p o w e r \ r e r a d i a t e d } ) = \frac { 3 2 } { 1 5 } \omega ^ { 6 } M ^ { 2 } L ^ { 2 } \langle \xi ^ { 2 } \rangle _ { \mathrm { t m e a v g . } }
$$

(see exercise 37.8). Consequently

$$
A _ { \tt G W } = { \frac { 1 6 } { 1 5 } } M L ^ { 2 } \omega ^ { 4 } .
$$

Onecan use these relations to rewrite the detector cross sections in terms of $A _ { \mathrm { d i s s } } ,$ $A _ { \tt G W }$ , and the reduced wavelength

$$
\lambda \equiv 1 / \omega
$$

of the radiation. For example,the cross section (37.21)--now with $\omega \ge 0$ is

$$
\left. \sigma \right. _ { \mathrm { a l l d i r e c t i o n s } } = \frac { 1 } { 2 } \pi \lambda ^ { 2 } \frac { A _ { \mathrm { G W } } A _ { \mathrm { d i s s } } } { ( \omega - \omega _ { 0 } ) ^ { 2 } + ( A _ { \mathrm { d i s s } } / 2 ) ^ { 2 } }
$$

(recall the assumption $| \omega - \omega _ { 0 } | \ll \omega _ { 0 }$ in all cross-section formulas) and the corresponding integral over the resonance is

$$
\int \left. \sigma \right. _ { \mathrm { a l l d i r e c t i o n s } } d \nu = \frac { 1 } { 2 } \pi { \lambda _ { 0 } } ^ { 2 } A _ { \mathrm { G W } } \mathrm { \ f o r \ p o l a r i z e d \ r a d i a t i o n } .
$$

These expressions for the cross section are comprehensive in their application. They apply to any vibrating, resonant, gravitational-wave detector whatsoever, as one sees from the “detailed balance” calculation of exercise 37.9,and from the dynamic calculations of exercise 37.10. They also apply,with obvious changes in statistical factors and notation, to compound-nucleus reactions in nuclear physics (“Breit-Wigner formula"; see Blattand Weisskopf, pp.392-94,408-10,555-59),to the absorption of photons by atoms and molecules,to reception of electromagnetic waves by a television antenna,etc. Equation (37.41) says in effect,“Calculate the rate at which the oscillator is damped by emission of gravitational radiation; multiply that rate by the geometric factor familiar in all work with antennas, ${ \scriptstyle { \frac { 1 } { 2 } } } \pi { \hat { \lambda } _ { 0 } } ^ { 2 }$ ,and immediately obtain the resonance integral of the cross section. The result is expressed in geometric

Generality of the $\pmb { A }$ -coefficient formalism

units (cm). To get the resonance integral in conventional units, multiply by the conversion factor $c = 3 \times 1 0 ^ { 1 0 } \ { \mathrm { c m } } \ { \mathrm { H z } } .$

The‘dynamic analysis’of the idealized masses-on-spring detector,as developed in the last section,is readily extended to a vibrating detector of arbitrary shape (Earth; Weber's bar; an automobile fender; and so on). The extension is carried out in exercise 37.10 and its main results are summarized in Box 37.4.

# Scattering of radiation by detector

Part of the energy that goes into a detector is reradiated as scattered gravitational radiation. For any detector of laboratory dimensions with laboratory damping coefficients,this fraction is fantastically small.However, in principle one can envisage a larger system and conditions where the reradiation is not at all negligible.In such an instance one is dealing with scattering. No attempt is made here to analyze such scattering processes. For a simple order-of-magnitude treatment, one can use the same type of Breit-Wigner scattering formula that one employs to calculate the scattering of neutrons at a nuclear resonance or photons at an optical resonance.A still more detailed account will analyze the correlation between the polarization of the scattered radiation and the polarization of the incident radiation.The kind of formalism useful here for gravitational radiation with its tensor character will be very much like that now used to treat polarization of radiation with a spin-1 character. Here notice especially the “Madison Convention”[Barschall and Haeberli (1971)] developed by the collaborative efforts of many workers after experience during many years with a variety of conflicting notations. Considering the way in which the best notation that is available today for spin-l radiation was evolved, one can only feel that it is too early to canonize any one notation for describing the scattering parameters for an object that is scattering gravitational radiation.

# EXERCISES

# Exercise 37.8. POWER RERADIATED

The idealized gravitational wave detector of Figure $3 7 . 4 \cdot$ vibrates with angular frequency ω. Show that the power it radiates as gravitational waves is given by equation (37.37).

# Exercise 37.9. CROSS SECTIONS CALCULATED BY DETAILED BALANCE

Use the principle of detailed balance to derive the cross sections (37.41) for a vibrating, resonant detector of any size,shape, or mass(e.g.,for the vibrating Earth,or Weber's vibrating cylinder, or the idealized detector of Figure 37.4).[Hints: Let the detector be in thermal equilibrium with a bath of blackbody gravitational waves. Then it must be losing energy by reradiation as rapidly as it is absorbing it from the waves. (Internal damping can be ignored because,in true thermal equilibrium, energy loss by internal damping will match energy gain from random internal Brownian forces.） In detail, the balance of energy in and out reads [with $I _ { \nu } =$ "specific intensity,” equation (22.48)]

$$
{ \begin{array} { r l } & { [ 4 \pi I _ { \nu } ( \nu = \nu _ { 0 } ) ] _ { \mathrm { b l a c k b o d y } } \times \int \langle \sigma \rangle _ { \mathrm { a l l d i r e c t i o n s } } d \nu } \\ & { \qquad = A _ { \mathrm { G W } } \times ( { \mathrm { E n e r g y i n n o r m a l ~ m o d e ~ o f ~ d e t e c t o r } } ) . } \end{array} }
$$

Solve for $\int \langle \pmb { \sigma } \rangle d \pmb { \nu }$ ,using the familiar form of the Planck spectrum and the fact that gravitational waves have two independent states of polarization.] Note: Because detailed balance

# Box 37.4 VIBRATING, RESONANT DETECTOR OF ARBITRARY SHAPE

# A.Physical Characteristics of Detector

1. Detector is a solid object (Earth, Weber bar, automobile fender,.. .) with density distribution $\pmb \rho ( \pmb x )$ and total mass $\begin{array} { r } { M = \int \rho \ d ^ { 3 } x } \end{array}$

2.Detector has normal modes of vibration. The nth normal mode is characterized by:

$$
\begin{array} { r l } & { \omega _ { n } = \mathrm { a n g u l a r f r e q u e n c y } ; } \\ & { \tau _ { n } = \Big ( \mathrm { e } \mathrm { - } \mathrm { f o l d i n g ~ t i m e ~ f o r ~ v i b r a t i o n ~ e n e r g y } } \\ & { \tau _ { n } = \Big ( \mathrm { t o ~ d e c a y ~ a s ~ r e s u l t ~ o f ~ i n t e r n a l ~ d a m p i n g } \Big ) \gg 1 / \omega _ { n } ; } \\ & { \mathbf { \Phi } _ { n } ( \mathbf { x } ) = \mathrm { e i g e n f u n c t i o n ~ ( d e f i n e d ~ h e r e ~ t o ~ b e ~ d i m e n s i o n l e s s ~ a i r ~ \omega ~ } } \end{array}
$$

The eigenfunctions ${ \pmb u } _ { \pmb n }$ are orthonormalized, so that

$$
\int \rho u _ { n } \cdot u _ { m } \ d ^ { 3 } x = M \delta _ { n m } .
$$

3.During a normal-mode vibration with $E _ { \mathsf { v i b r a t i o n } } \gg k T ,$ a mass element originally at $\hat { x }$ receives the displacement

$$
\begin{array} { r } { \delta \boldsymbol { x } = \boldsymbol { \xi } = \boldsymbol { u } _ { n } ( \boldsymbol { x } ) \mathcal { B } _ { n } e ^ { - i \omega _ { n } t - t / \tau _ { n } } , } \\ { \hat { \mathrm { L } } _ { [ \mathrm { c o n s t a n t a r } ] } } \end{array}
$$

the density at fixed $\pmb { x }$ changes by

$$
\delta \rho = - \nabla \cdot ( \rho \pmb { u } _ { n } ) \mathcal { B } _ { n } e ^ { - i \omega _ { n } t - t / \tau _ { n } } ,
$$

and the moment of inertia tensor oscilates

$$
\delta I _ { j k } = I _ { ( n ) j k } \mathcal { B } _ { n } e ^ { - i \omega _ { n } t - t / \tau _ { n } } .
$$

Here $I _ { ( n ) j k }$ is the“moment of inertia factor for the nth normal mode":

$$
\begin{array} { c } { { I _ { ( n ) j k } \equiv \displaystyle \int - ^ { \cdot } ( \rho u _ { n } { } ^ { t } ) _ { , i } x ^ { j } x ^ { k } d ^ { 3 } x } } \\ { { = \displaystyle \int \rho ( u _ { n } { } ^ { j } x ^ { k } + u _ { n } { } ^ { k } x ^ { j } ) d ^ { 3 } x } } \end{array}
$$

[dimensions: mass X length, multiply by Bn (length) to get Ijk]. The corresponding“reduced quadrupole factor for the nth normal mode” is

$$
\tilde { \cal t } _ { ( n ) j k } \equiv { \cal I } _ { ( n ) j k } - \frac { 1 } { 3 } { \cal I } _ { ( n ) t l } \delta _ { j k } .
$$

# B. Cross. Sections for Detector (exercise 37.10)

1. For polarized radiation with propagation direction $\pmb { n }$ and polarization tensor e:

$$
h _ { j k } = A ( t - \pmb { n } \cdot \pmb { x } ) e _ { j k } ,
$$

$$
e _ { j k } n _ { k } = 0 , e _ { j j } = 0 , e _ { j k } e _ { j k } = 2 ;
$$

$$
\sigma _ { n } ( \nu ) = \sigma _ { n } ( \omega / 2 \pi ) = \frac { \pi } { 4 } \frac { | { \cal f } _ { ( n ) j k } e _ { j k } | ^ { 2 } } { M } \frac { { \omega _ { n } } ^ { 2 } / \tau _ { n } } { ( | \omega | - \omega _ { n } ) ^ { 2 } + ( 1 / 2 \tau _ { n } ) ^ { 2 } } ,
$$

$$
\int _ { \mathrm { r e s o i a n c e } } \sigma _ { n } d \nu = \frac { \pi } { 4 } \frac { | \mathcal { I } _ { ( n ) j k } e _ { j k } | ^ { 2 } } { M } { \omega _ { n } } ^ { 2 } .
$$

2.For unpolarized radiation (random mixture of polarizations) with propagation direction $\pmb { n }$ ，cross sections are

$$
\begin{array} { c } { \displaystyle \sigma _ { n } ( \nu ) = \sigma _ { n } ( \omega / 2 \pi ) = \frac { \pi } { 4 } \frac { ( { f _ { ( n ) j k } ^ { \mathrm { T T } } } ) ^ { 2 } } { M } \frac { { \omega _ { n } } ^ { 2 } / \tau _ { n } } { ( | \omega | - \omega _ { n } ) ^ { 2 } + ( 1 / 2 \tau _ { n } ) ^ { 2 } } , } \\ { \displaystyle \int _ { \mathrm { r e s o n a n c e } } \sigma _ { n } ~ d \nu = \frac { \pi } { 4 } \frac { ( { f _ { ( n ) j k } ^ { \mathrm { T T } } } ) ^ { 2 } } { M } \omega _ { n } ^ { 2 } . } \end{array}
$$

Here $\mathcal { \pm } _ { ( n ) j k } ^ { \mathrm { T T } }$ is the transverse-tracelesspartof $\dot { f } _ { ( n ) j k }$ (transverse and traceless relative to the propagation direction $\pmb { n }$ ：

$$
\mathcal { F } _ { ( n ) } ^ { \mathrm { T T } } = P \mathcal { F } _ { ( n ) } P - \frac { 1 } { 2 } P \mathrm { t r a c e } ( P \mathcal { F } _ { ( n ) } ) , \qquad P _ { j k } \equiv \delta _ { j k } - n _ { j } n _ { k } .
$$

(See Box 35.1)

3. Cross sections for unpolarized radiation, averaged over all directions, are

$$
\langle \sigma _ { n } ( \nu ) \rangle _ { \mathrm { a l l d i r e c t i o n s } } = \frac { 1 } { 2 } \pi \lambda ^ { 2 } \frac { A _ { \mathrm { G W } } A _ { \mathrm { d i s s } } } { ( | \omega | - \omega _ { n } ) ^ { 2 } + ( A _ { \mathrm { d i s s } } / 2 ) ^ { 2 } } ,
$$

$$
\int _ { \mathrm { r e s o n a n c e } } \left. \sigma _ { n } \right. _ { \mathrm { a l l d i r e c t i o n s } } d \nu = \frac { 1 } { 2 } \pi \lambda ^ { 2 } A _ { \mathrm { G W } } ,
$$

where the Einstein $\pmb { A }$ coefficients are

$$
A _ { \mathrm { d i s s } } = 1 / \tau _ { n } ,
$$

$$
A _ { \mathrm { G W } } = \frac { 1 } { 5 } \frac { ( \mathcal { F } _ { ( n ) j k } ) ^ { 2 } } { M } { \omega _ { n } } ^ { 4 } .
$$

# C. Spectrum Radiated by an Aperiodic Source (exercise 37.11)

It is instructive to compare these formulas with expressions for the radiation emitted by an aperiodic source.

1. Fourier-analyze the reduced quadrupole factor of the source

$$
\mathcal { I } _ { j k } ( t ) = ( 2 \pi ) ^ { - 1 / 2 } \int _ { - \infty } ^ { + \infty } \widetilde { \mathcal { I } } _ { j k } ( \omega ) e ^ { - i \omega t } d \omega .
$$

2. Then the total energy per unit frequency $( \nu \geq 0 )$ radiated over all time, into a unit solid angle about the direction $\pmb { n }$ ,and with polarization tensor $\pmb { e }$ ,is

$$
\frac { d E } { d \nu d \Omega } = \frac { 1 } { 8 } \sum _ { \omega = \pm 2 \pi \nu } | \widetilde { \mathcal { F } } _ { j k } e _ { j k } | ^ { 2 } \omega ^ { 6 }
$$

[compare with equations (7)]. Summed over polarizations, this is

$$
\frac { d E } { d \nu \ d \Omega } = \frac { 1 } { 2 } \sum _ { j , k } | \widetilde { \pmb { f } } _ { j k } ^ { \mathrm { \tiny ~ T T } } | ^ { 2 } \omega ^ { 6 }
$$

[compare with equations (8)]. Here $\nu \geq 0$

3. The total energy radiated per unit frequency, integrated over al directions, still with $\nu \geq 0$ ,is

$$
d E / d \nu = \frac { 4 \pi } { 5 } \sum _ { j , k } | \widetilde { \boldsymbol { \tau } } _ { j k } | ^ { 2 } \omega ^ { 6 }
$$

[compare with equations (10)-(12)].

can be applied to any kind of resonant system in interaction with any kind of thermal bath of radiation or particles, equations (37.40) and (37.41), with appropriate changes of statistical factors, have wide generality.

# Exercise 37.10. NORMAL-MODE ANALYSIS OF VIBRATING, RESONANT DETECTORS

Derive all the results for vibrating,resonant detectors quoted in Box 37.4. Patern the derivation after the treatment of the idealized detector in $\ S 3 7 . 6$ .[Guidelines: (a) Let the detector be driven by the polarized waves of equation(6), Box 37.4;and let it be wave-dominated $( E _ { \mathrm { v i b r a t i o n } } \gg k T )$ . Show that the displacements $\delta { \pmb x } = { \pmb \xi } ( { \pmb x } , t )$ of its mass elements are described by

$$
\pmb { \xi } = \sum _ { n } \pmb { B } _ { n } ( t ) \pmb { u } _ { n } ( \cdot \cdot ) ,
$$

where the time-dependent amplitude for the nth mode satisfies the driven-oscillator equation

$$
\ddot { B } _ { n } + \dot { B } _ { n } / \tau _ { n } + \omega _ { n } { } ^ { 2 } B _ { n } = R _ { n } ( t ) ,
$$

and where the curvature-induced driving term is

$$
\begin{array} { l } { { \displaystyle R _ { n } ( t ) = - R _ { \hat { \jmath } \hat { 0 } \hat { k } \hat { 0 } } \int \left( \rho / M \right) u _ { n } ^ { \ j } \ d x ^ { k } d ^ { 3 } x } } \\ { { \displaystyle ~ = \frac { 1 } { 4 } \ddot { A } ( \mathcal { I } _ { ( n ) j k } e _ { j k } ) / M . } } \end{array}
$$

(See Box 37.4 for notation.)

(b) Fourier-analyze the amplitudes of the detector and waves,

$$
\begin{array} { r l r } & { } & { \displaystyle { B _ { n } ( t ) = ( 2 \pi ) ^ { - 1 / 2 } \int _ { - \infty } ^ { + \infty } \widetilde { B } _ { n } ( \omega ) e ^ { - i \omega t } d \omega , } } \\ & { } & { \displaystyle { A ( t ) = ( 2 \pi ) ^ { - 1 / 2 } \int _ { - \infty } ^ { + \infty } \widetilde { A } ( \omega ) e ^ { - i \omega t } d \omega , } } \end{array}
$$

and solve the equation of motion (37.42b,c) to obtain,in the neighborhood of resonance,

$$
\widetilde { B } _ { n } = \frac { \displaystyle \frac { 1 } { 8 } \omega _ { n } \widetilde { A } ( { f } _ { ( n ) j k } e _ { j k } ) / M } { | \omega | - \omega _ { n } + \displaystyle \frac { 1 } { 2 } i / \tau _ { n } } \qquad \mathrm { f o r ~ } | \omega \pm \omega _ { n } | \ll \omega _ { n } .
$$

(c) Calculate the total energy deposited in the detector by integrating

$$
\binom { \mathrm { e n e r g y } } { \mathrm { d e p o s i t e d } } = \int \left( { \mathrm { F o r c e ~ p e r ~ u n i t ~ v o l u m e } } \right) \cdot \left( { \mathrm { V e l o c i t y } } \right) d ^ { 3 } x d t .
$$

Thereby obtain

$$
\binom { \mathrm { e n e r g y ~ d e p o s i t e d ~ i n } } { n \mathrm { t h ~ n o r m a l ~ m o d e } } = \frac { 1 } { 4 } ( I _ { ( n ) j k } e _ { j k } ) \int \ddot { A } \dot { B } _ { n } \ : d t .
$$

(d) Apply Parseval's theorem and combine with expression (37.42f) to obtain

$$
\binom { \mathrm { e n e r g y ~ d e p o s i t e d ~ i n } } { n \mathrm { t h ~ n o r m a l ~ m o d e } } = \int \sigma _ { n } ( \nu ) \mathcal { F } _ { \nu } ( \nu ) d \nu ,
$$

where ${ \pmb { \sigma } } _ { \pmb { n } }$ is given by equation (7a)of Box 37.4,and (for $- \infty < \omega < + \infty ;$

$$
\mathcal { F } _ { \nu } ( \nu ) = \mathcal { F } _ { \nu } ( \omega / 2 \pi ) = \frac { 1 } { 8 } \omega ^ { 2 } | \widetilde { A } | ^ { 2 } .
$$

(e） Show that ${ \mathfrak { F } } _ { \nu } ( \nu )$ is the total energy per unit area per unit frequency carried by the waves past the detector.

(f） Obtain all the remaining cross sections quoted in Box 37.4 by appropriate manipulations of this cross section. Use the mathematical tools for projecting out and integrating “transverse-traceless parts,” which were developed in $\mathbf { B o x } 3 5 . 1$ and exercise 36.9.

# Exercise 37.11. SPECTRUM OF ENERGY RADIATED BY A SOURCE

Derive the results quoted in the last section of Box 37.4.

# Exercise 37.12. PATTERNS OF EMISSION AND ABSORPTION

The elementary dumbbell oscillator of Figure 37.4, initially unexcited, has a cross section for absorption of unpolarized gravitational radiation proportional to $\sin ^ { 4 } \theta$ ,and when excited radiates with an intensity also proportional to $\sin ^ { 4 } \theta$ (Chapter 36).The patterns of emission and absorption are identical. Any other dumbbell oscillator gives the same pattern, apart from a possible difference of orientation. Consider a nonrotating oscillator of general shape undergoing free vibrations in a single nondegenerate (and therefore nonrotatory） mode,or excited from outside by unpolarized radiation.

(a) Show that its pattern of emission is identical with its pattern of absorption.[Hint: Make the comparisons suggested in the last few parts of Box 37.4.1 (b) Show that this emission pattern $\risingdotseq$ absorption pattern), apart from three Euler angles that describe the orientation of this pattern in space,and apart from a fourth parameter that determines total intensity, is uniquely fixed by a single (“fifth") parameter. (c) Construct diagrams for the pattern of intensity for the two extreme values of this parameter and for a natural choice of parameter intermediate between these two extremes. (d):Define the parameter in question in terms of a certain dimensionless combination of the principal moments of the reduced quadrupole tensor.

# Exercise 37.13. MULTIMODE DETECTOR

Consider a cylindrical bar of length very long compared to its diameter. Designate the fundamental mode of end-to-end vibration of the bar as $" n = 1$ ,” and call the mode with $n - 1$ nodes in its eigenfunction the “nth mode.” Show that the cross section for the interception of unpolarized gravitational waves at the nth resonance,integrated over that resonance,and averaged over direction, is given by the formula [Rufini and Wheeler (1971b)]

$$
\int _ { \stackrel { \scriptstyle \mathrm { { r t h } } } { \mathrm { { r e s o n a n c e } ; } } } \sigma ( \nu ) d \nu = \frac { 3 2 } { 1 5 \pi } \frac { v ^ { 2 } } { c ^ { 2 } } \frac { M } { n ^ { 2 } } \mathrm { { ~ f o r ~ } } n \mathrm { { ~ o d d ~ } } ( \mathrm { z e r o ~ f o r ~ e v e n ~ } n ) ,
$$

where $v$ is the speed of sound in the bar expressed in the same units as the speed of light, $c$ ； and $M$ is the mass of.the-bar (geometric units;multiply the righthand side by the factor $G / c = 2 . 2 2 \times 1 0 ^ { - 1 8 } \mathrm { c m ^ { 2 } H z / g }$ when employing conventional units). Show that this expresion gives $\mathrm { f } \sigma \ d \nu = 1 . 0 \times 1 0 ^ { - 2 1 } \mathrm { c m ^ { 2 } \ H z }$ for the lowest mode of Weber's bar. Multimode detectors are (i973） under construction by William Fairbank and William Hamilton, and by David Douglass and John A. Tyson.

# Exercise 37.14. CROSS SECTION OF IDEALIZED MODEL OF EARTH FOR ABSORPTION OF GRAVITATIONAL RADIATION

The observed period of quadrupole vibration of the earth is 54 minutes [see, e.g., Bolt (1964) or Press (l965) for survey and bibliography]. To analyze that mode of vibration,with all due allowance for elasticity and the variation of density in the earth, is a major enterprise. Therefore,for a first estimate of the cross section of the earth for the absorption of quadrupole radiation,treat it as a globe of fuid of uniform density held in the shape of a sphere by gravitational forces alone (zero rigidity).Let the surface be displaced from $r = a$ to

$$
r = a + a \alpha P _ { 2 } ( \cos \theta ) ,
$$

where $\pmb \theta$ is polar angle measured from the North Pole and $\pmb { \alpha }$ is the fractional elongation of the principal axis. The motion of lowest energy compatible with this change of shape is described by the velocity field

$$
\xi ^ { x } = - \frac 1 2 \alpha x , \qquad \xi ^ { y } = - \frac 1 2 \alpha y , \qquad \xi ^ { z } = \alpha z
$$

(zero divergence、 zero curl).

(a) Show that the sum of the kinetic energy and the gravitational potential energy is

$$
E \textbf { x } - ( 3 / 5 ) ( M ^ { 2 } / a ) ( 1 - \alpha ^ { 2 } / 5 ) + ( 3 / 2 0 ) M a ^ { 2 } \dot { \alpha } ^ { 2 } .
$$

. (b) Show that the angular frequency of the free quadrupole vibration is

$$
\begin{array} { r } { \omega = ( 1 6 \pi / 1 5 ) ^ { 1 / 2 } \rho ^ { 1 / 2 } . } \end{array}
$$

(c) Show that the reduced quadrupole moments are

$$
\dot { \mathcal { I } } _ { z z } = \dot { \mathcal { I } } _ { y y } = - M a ^ { 2 } \alpha / 5 , \qquad \dot { \mathcal { I } } _ { z z } = 2 M a ^ { 2 } \alpha / 5 .
$$

(d) Show that the rate of emission of vibrational energy,averaged over a period, is

$$
- \langle d E / d t \rangle = ( 3 / 1 2 5 ) M ^ { 2 } { a ^ { 4 } \omega ^ { 6 } \alpha _ { \mathrm { p e a k } } } ^ { 2 } .
$$

(e) Show that the exponential rate of decay of energy by reason of gravitational wave damping, or “gravitational radiation line broadening,”is

$$
A _ { \tt G W } = ( 4 / 2 5 ) M a ^ { 2 } \omega ^ { 4 } .
$$

(f） Show that the resonance integral of the absorption cross section for radiation incident from random directions with random polarization is

$$
\int _ { \mathrm { r e s o n a n c e } } \langle \sigma ( \nu ) \rangle d \nu = ( \pi / 2 ) \lambda ^ { 2 } A _ { \mathrm { G W } } = ( 2 \pi / 2 5 ) M a ^ { 2 } / { \lambda ^ { 2 } } .
$$

(g) Evaluate this resonance integral. Note: This model of a globe of fluid of uniform density would imply for the earth, with average density $5 . 5 1 7 \ \mathsf { g } / \mathsf { c m } ^ { 3 }$ ,a quadrupole vibration period of $9 4 ~ \mathrm { m i n }$ ,as compared to the observed $5 4 ~ \mathrm { { m i n } }$ ； and a moment of inertia $( 2 / 5 ) M a ^ { 2 }$ as compared to the observed $0 . 3 3 M a ^ { 2 }$ .Ruffini and Wheeler(l971b) have estimated correction factors for both effects and give for the final resonance integral ${ \sim } 5 ~ \mathrm { c m ^ { 2 } ~ H z }$

# \$37.8. NOISY DETECTORS

When the bandwidth of the incoming waves is large compared to the resonance width of the detector, the waves deposit a total energy in the detector given by

$$
\begin{array} { r l r } & { } & { \mathrm { ( t o t a l ~ e n e r g y ~ d e p o s i t e d ) } = \displaystyle \int \sigma \mathcal { F } _ { \nu } ~ d \nu = \mathcal { F } _ { \nu } ( \nu = \nu _ { 0 } ) \int \sigma ~ d \nu . } \\ & { } & { \mathrm { [ e r g s i . } \int \mathrm { ~ } } \end{array}
$$

Extraction of small signal from large noise--general remarks

At least, this is so if the detector is wave-dominated (i.e., if $E _ { \mathrm { v i b r a t i o n } } \gg k \mathcal { T }$ while waves act; i.e., if initial amplitude of oscillation, produced by Brownian forces,is too small to interfere constructively or destructively with the amplitude due to waves).

Unfortunately,all experiments today (1973) are faced with noisy detectors.Nobody has yet found waves so strong, or constructed a detector so sensitive, that the detector is wave-dominated. Consequently,a key experimental task today is to pick a small signal out of large noise. Many techniques for doing this have been developed and used in a variety of fields of physics, as well as in astronomy， psychology and engineering [see, e.g., Davenport and Root (1958), Blackman and Tukey (1959),and

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0016_pages_1051-1120/auto/images/809050c589cf1cdc2245c834f6e0d2fbde93a05731c722a0a80113d123853dd3.jpg)  
Figure 37.5. Detection of hammer-blow gravitational waves with a noisy detector.Detection of even a weak pulse is possible if the time of the pulse is short enough.The amplitude ${ \mathcal { B } } _ { n }$ of the detector's vibrations changes by an amount $\sim \mathcal { B } _ { n } ^ { \mathrm { r m s } }$ $( \varDelta t / \tau _ { n } ) ^ { 1 / 2 }$ during a time interval $\pmb { \mathscr { s t } }$ ,due to thermal fluctuations (random-walk,Brownian-noise forces). Depicted in the inset is a change in amplitude produced by a burst of waves of duration $\tau _ { \tt G W }$ arriving out of phase with the detector's thermal motions (energy extracted by waves!).The waves are detectable because

$$
\begin{array} { r } { \varDelta | \mathcal { B } _ { n } | _ { \mathrm { d u e t o w a v e s } } \gg \mathcal { B } _ { n } ^ { \mathrm { r m s } } ( \tau _ { \mathrm { G W } } / \tau _ { n } ) ^ { 1 / 2 } , } \end{array}
$$

even though $\Delta | \mathcal { B } _ { n } | \ll \mathcal { B } _ { n } ^ { \mathrm { r m s } }$

references given there]. The key point is always to find some feature of the signal that is statistically more prominent than the same feature of the noise, plus a correlation to show that it arises from the expected signal source and not from elsewhere ("protection from systematic error"). Thus to detect steady gravitational waves from a pulsar, one might seek to define very precisely two numbers $\langle N ^ { 2 } \rangle$ and $\langle ( N + S ) ^ { 2 } \rangle = \langle \bar { N } ^ { 2 } \rangle + \langle S ^ { 2 } \rangle$ ,where $N$ and $s$ are the noise and signal amplitudes respectively. A long series of observations (with the pulsar out of the antenna beam) gives one value of $\langle N ^ { 2 } \rangle$ . Another equally long series of observations, interspersed with the first series, will be expected in zeroth approximation to give the same value of $\langle N ^ { 2 } \rangle$ . In the next approximation one recognizes and calculates the influence of normal statistical fluctuations. In an illustrative example, theory, confirmed by statistical tests of other parameters drawn from the same data, guarantees that the fluctuations are less than $1 0 ^ { - 5 } \langle N ^ { 2 } \rangle$ with 95 per cent confidence (only 5 per cent chance of exceeding $1 0 ^ { - 5 } \langle N ^ { 2 } \rangle$ ; this limit is set by time and money, not by absolute limitations of physics).Let the second series of observations be carried out only at times when the pulsar is in the antenna beam. Let it give

$$
\begin{array} { r } { \left\{ \langle N ^ { 2 } \rangle + \langle S ^ { 2 } \rangle \right\} _ { \mathrm { 2 d } \mathrm { s e r i e s } } = ( 1 + 7 . 3 \times 1 0 ^ { - 5 } ) \{ \langle N ^ { 2 } \rangle \} _ { \mathrm { 1 s t s e r i e s } } . } \end{array}
$$

.Then in first approximation one can say that $\langle S ^ { 2 } \rangle$ lies with 95 per cent confidence in the limits $( 7 . 3 \pm 1 . 0 ) \times 1 0 ^ { - 5 } \langle N ^ { 2 } \rangle$

Many conceivable sources of gravitational radiation produce bursts rather than a steady signal strength (Figure 37.5). Thus one is led to ask in what features “hammer-blow radiation” $( \tau _ { \mathtt { G W } } \ll \tau _ { 0 } )$ differs from noise. The“Brownian motion” noise in the detector may be thought of as arising from large numbers of small

Rate-of-change of detector amplitude as a tool for extracting burst signals from thermal noise

(molecular) energy exchanges with a heat bath. The calculations below estimate the typical rate of change of amplitude that a series of such molecular “knocks” can produce in a detector,and compare it with the rapid amplitude change produced by a“hammer-blow” pulse of radiation.The calculations show that sudden thermally induced changes,even of very small amplitude, are rare. Thus sudden changes are a suitable feature for the observations to focus on. The actual detection of pulses requires a more extended analysis, however, which goes beyond the estimates made below. Such an analysis would calculate the probabilities that rare events (sudden changes in amplitude) occur by chance (i.e., due to thermal fluctuations) in specified periods of time,the still smaller probabilities that they occur in coincidence between two or more detectors,and the correlations with postulated sources.

Consider a realistic detector of the type described in Box 37.4.But examine it at a time when it is not radiation-dominated. Then its motions are being driven by internal Brownian forces (thermal fluctuations),and perhaps also by an occasional burst of gravitational waves. Focus attention on a particular normal mode (mode $^ { \ast } n ^ { \ast } )$ , and describe that mode's contribution to the vibration of the detector by the vector field

$$
\delta \mathbf { x } = \pmb { \xi } = \mathcal { B } _ { n } ( t ) e ^ { - i \omega _ { n } t } \pmb { u } _ { n } ( \mathbf { x } ) .
$$

Since ${ \pmb u } _ { \pmb { n } }$ is dimensionless with mean value unity $\begin{array} { r } { ( \small { \mathscr { f } \mathscr { p } u _ { n } } ^ { 2 } d ^ { 3 } x = M ) } \end{array}$ ，the complex number $\mathcal { B } _ { n } ( t )$ is the mass-weighted average of the amplitudes of motion of the detector's mass elements. This amplitude changes slowly with time (rate $\ll \omega _ { n }$ as a result of driving by Brownian forces; but averaged over time it has a magnitude corresponding to a vibration energy of $k T$ ：

$$
\langle E _ { \mathrm { v i b r a t i o n } } \rangle = 2 \left. { \frac { 1 } { 2 } } \int \rho { \dot { \xi } } ^ { 2 } d ^ { 3 } x \right. = { \frac { 1 } { 2 } } M \omega _ { n } { } ^ { 2 } \langle | { \mathcal { B } } _ { n } | ^ { 2 } \rangle = k T ;
$$

$$
\mathcal { B } _ { n } ^ { \mathrm { r m s } } \equiv \langle | \mathcal { B } _ { n } | ^ { 2 } \rangle ^ { 1 / 2 } = ( 2 k T / M \omega _ { n } ^ { ~ 2 } ) ^ { 1 / 2 } .
$$

Example: for Weber's detector $( M \sim 1 0 ^ { 3 } \mathrm { k g }$ ， $\omega _ { 0 } \sim 1 0 ^ { 4 } / \mathsf { s e c } )$ , the fundamental mode at room temperature has

$$
\mathcal { B } _ { 0 } ^ { \mathrm { r m s } } = \left( \frac { 2 \times 1 . 3 8 \times 1 0 ^ { - 1 6 } \times 3 0 0 ~ \mathrm { e r g } } { 1 0 ^ { 6 } ~ \mathrm { g } \times 1 0 ^ { 8 } ~ \mathrm { s e c } ^ { - 2 } } \right) ^ { 1 / 2 } = 3 \times 1 0 ^ { - 1 4 } ~ \mathrm { c m } .
$$

One's hope for detecting weak hammer-blow radiation lies not in an examination of the detector's vibration amplitude (or energy), but in an examination of its rate of change (Figure 37.5). The time-scale for large Brownian fluctuations in amplitude $( | \boldsymbol { \varDelta } \mathcal { B } _ { n } | \sim \mathcal { B } _ { n } ^ { \mathrm { r m s } } )$ , when the detector is noisy,is the same as the time scale $\tau _ { n }$ for internal forces to damp the detector,when it is driven to $E _ { \mathrm { v i b r a t i o n } } \gg k T .$ Thus, the amplitude ${ \mathcal { B } } _ { n }$ does a“random walk” under the influence of Brownian forces, with the mean time for"large walks” $( | \boldsymbol { \varDelta } \mathcal { B } _ { n } | \sim \mathcal { B } _ { n } ^ { \mathrm { r m s } } )$ being $\varDelta t \approx \tau _ { n }$ . The change in ${ \mathcal { B } } _ { n }$ over shorter times $\pmb { \varDelta t }$ is smaller by the ${ } ^ { 6 6 } 1 / { \sqrt { N } }$ factor,” which always enters into random-walk processes:

$$
{ \sqrt { N } } = \left( { \frac { \mathrm { n u m b e r ~ o f ~ v i b r a t i o n ~ c y c l e s ~ i n ~ t i m e ~ } \tau _ { n } } { \mathrm { n u m b e r ~ o f ~ v i b r a t i o n ~ c y c l e s ~ i n ~ t i m e ~ } \tilde { A } t } } \right) ^ { 1 / 2 } = \left( { \frac { \tau _ { n } } { \varDelta t } } \right) ^ { 1 / 2 } ;
$$

$$
\langle | \varDelta \mathcal { B } _ { n } ^ { ( \mathrm { t h e r m a l } ) } | \rangle \approx \mathcal { B } _ { 0 } ^ { \mathrm { r m s } } \left( \frac { \varDelta t } { \tau _ { n } } \right) ^ { 1 / 2 } = \left( \frac { 2 k T } { M \omega _ { n } ^ { 2 } } \right) ^ { 1 / 2 } \left( \frac { \varDelta t } { \tau _ { n } } \right) ^ { 1 / 2 } \mathrm { d u r i n g } _ { \ : } .
$$

Now suppose that “hammer-blow” radiation (burst of duration $\varDelta t = \tau _ { \mathrm { G W } } \ll \tau _ { n } )$ strikes the detector, producing a change $\varDelta \mathcal { B } _ { n } ^ { ( \mathrm { G w } ) }$ in the detector's amplitude. This change in amplitude, because it comes so quickly, (l) superposes linearly on any change in amplitude produced in the same time interval by the action of Brownianmotion forces; and (2) is therefore independent in value of the presence or absence of Brownian-motion forces, i.e., independent of all thermal agitation. Therefore $\varDelta \mathcal { B } _ { n } ^ { ( \mathrm { G W } ) }$ (a quantity with both magnitude and phasel) is identical to what it would have been if the detector were at zero temperature:

$$
\underbrace { \frac { 1 } { 2 } M \omega _ { n } ^ { 2 } | A B _ { n } ^ { \mathrm { ( G W ) } } | ^ { 2 } } _ { \begin{array} { c } { { \mathrm { 1 } } } \\ { { \mathrm { 1 } } } \\ { { \mathrm { 2 } } } \end{array} } = \int \sigma _ { n } ( \nu ) \mathcal { F } _ { \nu } ( \nu ) d \nu = \mathcal { F } _ { \nu } ( \omega _ { n } / 2 \pi ) \int \sigma _ { n } ( \nu ) d \nu ;
$$

Effect of a burst of waves on a noisy. resonant detector

energy that would be deposited if detector were at zero temperature

'For hammer-blow radiation,bandwidth of radiation is always $\gg$ bandwidth of detector; see Box 37.4

$$
| \varDelta \phi _ { n } ^ { ( \mathrm { G W } ) } | = \biggl ( \frac { 2 \mathcal { F } _ { \nu } ( \omega _ { n } / 2 \pi ) \int \sigma _ { n } d \nu } { M { \omega _ { n } } ^ { 2 } } \biggr ) ^ { 1 / 2 } .
$$

· This wave-induced change in amplitude willbe distinguishable from thermal changes only if it is significantly bigger than the thermal changes (37.52) expected during the same length of time $\tau _ { \tt G W }$ ：

Criteria for detectability of burst

$$
\begin{array} { r l } & { | \mathcal { A } \mathcal { B } _ { n } ^ { ( \mathrm { G W } ) } | \gg \langle | \mathcal { A } \mathcal { B } _ { n } ^ { ( \mathrm { t h e r m a l } ) } | \rangle \mathrm { ~ d u r i n g ~ t i m e ~ } \tau _ { \mathtt { G W } } } \\ & { \mathrm { e q u i v a l e n t l y } ; F _ { \nu } ( \omega _ { n } / 2 \pi ) \gg \left( \frac { k T } { \displaystyle \int \sigma _ { n } \ : d \nu } \right) \left( \frac { \tau _ { \mathtt { G W } } } { \tau _ { n } } \right) \left\{ \mathrm { d e t e c t a b i l i t y } \right. } \end{array}
$$

Of course, if one is equipped only to measure the magnitude of the detector's amplitude or energy,and not its phase, these criteria for detectability are not quite sufficient. The wave-induced change in squared amplitude (proportional to change in energy) will depend on the relative phases of the initial amplitude and amplitude change

$$
\begin{array} { r l } {  { \begin{array} { l l } { { \varDelta } | ^ { \varepsilon } \vartheta _ { n } | ^ { 2 } = | \mathcal { P } _ { n } ^ { ( \mathrm { i n i t i a l } ) } + { \varDelta } \mathcal { B } _ { n } ^ { ( \mathrm { G W } ) } | ^ { 2 } - | { \varepsilon } \mathcal { P } _ { n } ^ { ( \mathrm { i n i t i a l } ) } | ^ { 2 } } \end{array} } } \\ & { \begin{array} { r l } & { \approx 2 | \mathfrak { H } _ { n } ^ { ( \mathrm { i n i t i a l } ) } | | { \varDelta } \mathfrak { e } \mathcal { P } _ { n } ^ { ( \mathrm { G W } ) } | \qquad \mathrm { ~ i f ~ i n ~ p h a s e } } \\ & { \approx 0 } \\ { . \qquad \approx - 2 | \mathcal { H } _ { n } ^ { ( \mathrm { i n i t i a l } ) } | | { \varDelta } \mathfrak { e } \mathcal { B } ^ { ( \mathrm { G W } ) } | \qquad } & { \mathrm { i f ~ p h a s e ~ d i f f e r e n c e ~ i s ~ } { \pm \pi } / 2 } \end{array} } \\ & { . \qquad \approx - 2 | \mathcal { H } _ { n } ^ { ( \mathrm { i n i t i a l } ) } | | { \varDelta } \mathfrak { e } \mathcal { B } _ { n } ^ { ( \mathrm { G W } ) } | \qquad \mathrm { i f ~ p h a s e ~ d i f f e r e n c e ~ i s ~ } \pi . } \end{array}
$$

Ways to improve sensitivity of detector

Thus,only a burst that arrives in phase with the initial motion of the detector or with reversed phase will be measurable. But for such a burst, the criteria (37.54) are sufficient.

Equations (37.54) make it clear that there are three ways to improve the sensitivity ofvibratory detectors to hammer-blow radiation: $( I )$ increase the detector's integrated cross-section [which can be done only by increasing the rate $A _ { \tt G W }$ at which it reradiates gravitational waves; see equations (lOb) and $( l I b )$ of Box 37.4]; (2) cool the detector; (3) increase the detector's damping time.

Box 37.5 applies the above detectability criteria to some detectors that seem feasible in the $1 9 7 0 ^ { \circ } { \mathsf { s } } ,$ and to some bursts of waves predicted by theory. The conclusions of that comparison give one hope!

To be complete, the above discussion should have analyzed not only noise in the detector, but also the noise in the sensor which one uses to measure the amplitude of the detector's displacements. However, the theory of displacement sensrs is beyond the scope of this book.For a brief discussion and for references, see Press and Thorne (1972).

Non-mechanical detectors

# \$37.9. NON-MECHANICAL DETECTORS

When gravitational waves flow through matter, they excite it into motion. Such excitations are the basis for all detectors described thus far. But gravitational waves interact not only with matter; they also interact with electromagnetic fields; and those interactions can also be exploited in detectors. One of the most promising detectors that may be built in the future, one designed by Braginsky and Menski (1971),relies on a resonant interaction between gravitational waves and electromagnetic waves.It is described in Box 37.6.

The future of gravitational-wave astronomy

# \$37.10. LOOKING TOWARD THE FUTURE

As this book is being written, it is not at all clear whether the experimental results of Joseph Weber constitute a genuine detection of gravitational waves. (See $\ S 3 7 . 4$ part 4.) But whether they do or not, gravitational-wave astronomy has begyn, and seems to have a bright future. The technology of 1973 appears sufficient for the construction of detectors that will register waves from a star that collapses to form a black hole anywhere in our galaxy (Box 37.5); and detectors of the late 1970's and early 1980's may well register waves from pulsars and from supernovae in other galaxies. The technical difficulties to be surmounted in constructing such detectors are enormous.But physicists are ingenious; and with the impetus provided by Joseph Weber's pioneering work,and with the support of a broad lay public sincerely interested in pioneering in science, al obstacles will surely be overcome.

Box 37.5 DETECTABILITY OF HAMMER-BLOW WAVES FROM ASTROPHYSICAL SOURCES: TWO EXAMPLES (The following calculations are accurate only to within an order of magnitude or so)

A. Waves from a Star of Ten Solar Masses Collapsing to Form a Black Hole; 1972 Detector with 1975 (?) Sensor

1. Predicted characteristics of radiation:

$( \mathrm { i n t e n s i t y ~ a t ~ E a r t h } ) = \mathcal { F } _ { \nu } \sim \frac { M _ { \odot } } { 4 \pi ( \mathrm { d i s t a n c e } ) ^ { 2 } \nu }$ $\sim ( 2 \times 1 0 ^ { 5 } ~ \mathrm { e r g s / c m ^ { 2 } ~ H z ) }$ [(distance to center of galaxy)/(distance)]²,   
$( { \mathrm { f r e q u e n c y ~ o f ~ w a v e s } } ) = \nu \sim 1 0 ^ { 3 } { \mathrm { ~ H z } } ,$   
(bandwidth of waves ${ \mathrm { \Omega } } ^ { \prime } = { \varDelta } { \nu } \sim 1 0 ^ { 3 } { \mathrm { ~ H z } } ,$   
(duration of burst) $= \tau _ { \tt G W } \sim 1 0 ^ { - 3 }$ sec to $1 0 ^ { - 1 }$ sec.

2. Detector properties: A Weber bar, vibrating in its fundamental mode, with

$$
M = 1 0 ^ { 6 } ~ \mathrm { g } , ~ \int \sigma ~ d \nu = 1 0 ^ { - 2 1 } ~ \mathrm { c m ^ { 2 } ~ H z ~ ( e x e r c i s e ~ 3 7 . 1 3 ) } ,
$$

$$
\mathit { \Pi } _ { \vartheta _ { 0 } ^ { \mathrm { r m s } } } ^ { \mathrm { { \sc } } s \mathrm { { r m s } } } = \left( \frac { 2 \times 1 . 3 7 \times 1 0 ^ { - 1 6 } \times 3 \mathrm { ~ e r g } } { 1 0 ^ { 6 } \mathrm { ~ g } \times 1 0 ^ { 8 } \mathrm { ~ s e c } ^ { - 2 } } \right) ^ { 1 / 2 } = 3 \times 1 0 ^ { - 1 5 } \mathrm { { \ c m } , }
$$

$$
| \varDelta \mathcal { P } _ { 0 } ^ { ( \mathrm { t h e r m a l } ) } | = ( 3 \times 1 0 ^ { - 1 5 } \mathrm { c m } ) ( 1 0 ^ { - 3 } / 2 0 ) ^ { 1 / 2 } = 2 \times 1 0 ^ { - 1 7 } \mathrm { c m } ,
$$

3. Effect of waves [equation (37.53):

$$
\begin{array} { r l r } & { \left| { \mathcal { A } } { \mathfrak { s } } _ { 0 } ^ { ( \mathbb { G W } ) } \right| = \left( \frac { 2 \times 2 \times 1 0 ^ { \bar { \mathfrak { s } } } \times 1 0 ^ { - 2 1 } \mathrm { ~ e r g s } } { 1 0 ^ { 6 } \times 1 0 ^ { 8 } \mathrm { ~ s e c } ^ { - 2 } } \right) ^ { 1 / 2 } \left( \frac { \mathrm { c e n t e r ~ o f ~ G a l a x y } } { \mathrm { d i s t a n c e } } \right) } \\ & { } & { \mathrm { d i s t a n c e ~ t o } } \\ & { } & { = 2 \times 1 0 ^ { - 1 5 } \mathrm { ~ c m ~ } \left( \frac { \mathrm { c e n t e r ~ o f ~ G a l a x y } } { \mathrm { d i s t a n c e } } \right) . } \end{array}
$$

4.Conclusion: Gravitational waves from a massive star collapsing to form a black hole anywhere in our galaxy are readily detectable, $i f$ one can construct a “sensor” to measure changes in vibration amplitudes of magnitude $\lesssim 1 0 ^ { - 1 5 }$ cm on time scales $< 0 . 1$ seconds. This does appear to be feasible with l972 technology; see Press and Thorne (l972).

# B. Waves from a Supernova Explosion in the Virgo Cluster of Galaxies; a Detector that might be constructable by late $1 9 7 0 ^ { \prime } { \mathsf { s } }$ or early 1980's

1. Predicted characteristics of radiation:

$$
\begin{array} { r l } & { \mathrm { ( i n t e n s i t y ~ a t ~ E a r t h ) } = F _ { \nu } \sim \frac { 0 . 0 3 M _ { \odot } } { 4 \pi ( 1 1 ~ \mathrm { m e } \mathrm { g a p a r s e c s } ) ^ { 2 _ { \nu } } } } \\ & { \qquad \sim 4 \times 1 0 ^ { - * } \mathrm { e r g s } / \mathrm { c m ^ { 2 } ~ H z } , } \\ & { \mathrm { ( f r e q u e n c y ~ o f ~ w a v e s ) } = \nu \sim 1 0 ^ { 3 } \mathrm { ~ H z } , } \\ & { \mathrm { ( b a n d w i d t h ~ o f ~ w a v e s ) } \sim \nu \sim 1 0 ^ { 3 } \mathrm { ~ H z } , } \\ & { \mathrm { ( d u r a t i o n ~ o f ~ b u r s t ) } = \tau _ { \mathrm { G W } } \sim 0 . 3 \mathrm { ~ s e c , ~ o r ~ } \tau _ { \mathrm { G W } } \sim 2 \times 1 0 ^ { - 3 } \mathrm { ~ s e c ~ } } \end{array}
$$

2. Detector: A Weber-type bar made not of metal, but of a $1 { , } 0 0 0 { \cdot } \mathbf { k g }$ monocrystal of quartz, cooled to a temperature of $3 \times 1 0 ^ { - 3 } \mathrm { ~ K ~ }$ (For such a monocrystal, it is thought that the damping time would increase in inverse proportion to temperature, $\tau _ { 0 } \propto 1 / T .$ Estimated properties of such a detector:

$M \sim 1 0 ^ { 6 } ~ \mathrm { g } , ~ \int \sigma ~ d \nu = 1 0 ^ { - 2 1 } ~ \mathrm { c m } ^ { 2 } ~ \mathrm { H z }$ (same as for Weber bar),

$$
\begin{array} { r l } & { \nu _ { 0 } = \omega _ { 0 } / 2 \pi \sim 1 . 5 0 0 \ \mathrm { H z } , \qquad T = 3 \times 1 0 ^ { - 3 } \ \mathrm { K } ; \mathit { \Omega } ^ { - } } \\ & { \tau _ { 0 } \sim 1 0 ^ { 6 } \ \mathrm { s e c } , } \end{array}
$$

$$
{ \mathcal { B } } _ { 0 } ^ { \mathrm { r m s } } = \left( { \frac { 2 \times 1 . 3 7 \times 1 0 ^ { - 1 6 } \times 3 \times 1 0 ^ { - 3 } ~ { \mathrm { e r g } } } { 1 0 ^ { 6 } ~ { \mathrm { g } } \times 1 0 ^ { 8 } ~ { \mathrm { s e c } } ^ { - 2 } } } \right) ^ { 1 / 2 } = 1 \times 1 0 ^ { - 1 6 } ~ { \mathrm { c m } } ,
$$

$$
| \mathbf { \Delta } 4 8 \mathbf { \% } \mathbf { e } \mathbf { r } \mathbf { m } \mathbf { a } \mathbf { b } | = ( 1 \times 1 0 ^ { - 1 6 } \mathbf { \Delta } \mathrm { c m } ) \left( { \frac { 0 . 3 \mathrm { ~ o r ~ } 2 \times 1 0 ^ { - 3 } } { 1 0 ^ { 6 } } } \right) ^ { 1 / 2 } = \left\{ \begin{array} { l l } { 6 \times 1 0 ^ { - 2 0 } \mathrm { ~ c m } , } \\ { \qquad \mathrm { o r } } \\ { 5 \times 1 0 ^ { - 2 1 } \mathrm { ~ c m } . } \end{array} \right.
$$

3. Effect of waves [equation (37.53)):

$$
| \varDelta \mathfrak { s } \mathfrak { s } _ { 0 } ^ { ( \mathfrak { G } \mathfrak { w } ) } | = \left( \frac { 2 \times 4 \times 1 0 ^ { - 3 } \times 1 0 ^ { - 2 1 } \mathrm { \ e r g s } } { 1 0 ^ { 6 } \times 1 0 ^ { 8 } \mathrm { \ s e c } ^ { - 2 } } \right) ^ { 1 / 2 } = 3 \times 1 0 ^ { - 1 9 } \mathrm { \ c m } .
$$

4. Conclusion: Gravitational waves are detectable from a supernova in the Virgo cluster,if one can construct a sensor to measure changes in vibration amplitudes of magnitude $\lesssim 1 0 ^ { - 1 9 } ~ { \mathsf { c m } }$ on time scales of $\lesssim 0 . 1$ seconds； and if one can construct a detector with the above characteristics.

# Box 37.6 A NONMECHANICAL DETECTOR OF GRAVITATIONAL WAVES [Braginsky and Menskii (1971)]

The Idea in Brief (see diagram at right)

A toroidal waveguide contains a monochromatic train of electromagnetic waves, traveling around and around it. Gravitational waves propagate per-pendicular to the plane of the torus.If the circuit time for the EM waves is twice the period of the gravitational waves, then one circularly polarized component of the gravitational waves will stay always in phase with the traveling EM waves. Result: a resonance develops. In one region of the EM wave train, gravitational tidal forces always "push”the waves forward (blue shift!) in another region the tidal forces “push”backward (red shift!). An EM frequency difference builds up linearly with time; a phase difference builds up quadratically.

# Outline of Quantitative Analysis

1. Let waveguide fall freely in an Earth orbit. Orient axes of waveguide's proper reference frame (= local Lorentz frame） so (l） waveguide lies in $\hat { x } , \hat { y } \cdot$ -plane,and (2） gravitational waves propagate in $\hat { z }$ direction.

2. Let gravitational waves have amplitudes

$$
A _ { + } - i A _ { \times } = \mathcal { Q } e ^ { - i \omega ( t - z ) }
$$

[Recall: $\hat { t } \approx t , \hat { z } \approx z$ ； i.e., proper frame and TT coordinates almost agree.] Then in plane of waveguide $( z = 0 )$ ，

$$
\begin{array} { r l } & { \underbrace { R _ { \hat { x } \hat { 0 } \hat { x } \hat { 0 } } = - R _ { \hat { y } \hat { 0 } \hat { y } \hat { 0 } } } _ { \begin{array} { l } { R _ { \hat { x } \hat { 0 } \hat { y } \hat { 0 } } = R _ { \hat { y } \hat { 0 } \hat { x } \hat { 0 } } = \frac { 1 } { 2 } \omega ^ { 2 } \mathcal { Q } \sin { ( \omega t ) } } } \end{array} } \end{array} ,
$$

3.Consider two neighboring parts of the EM wave, one at $\phi = \alpha + { \textstyle { \frac { 1 } { 2 } } } \omega t$ ； the other at $\phi = \alpha + \delta \alpha + { \textstyle { \frac { 1 } { 2 } } } \omega t$ Treat them as photons. Each moves along a null geodesic, except for $\omega =$ (angular freq uency of gravitational waves) (rate of change of phase of waves with time) (two times angular velocity with which pattern of “lines of force” rotates)

$r =$ (radius of torus),is adjusted so the speed of propagation of EM waves in waveguide is $v = { \frac { 1 } { 2 } } \omega r$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0016_pages_1051-1120/auto/images/2a8c4b6a64d7bd0b292fc60bdb99d281a94df76b5dc64a8b8bc08bad44fee69a.jpg)

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0016_pages_1051-1120/auto/images/9015c98eea99f4630ce85fe21ba19cc1c8fdc8ff5621cdf3a6cb64b3020b72e6.jpg)

[EM waves propagate counterclockwise；gravitational line-of-force diagram rotates counterclockwise; they stay in phase.]

the deflective guidance of the wave guide. Thus, their wave vectors $\pmb { k }$ satisfy

$$
\begin{array} { r } { \nabla _ { \boldsymbol { k } } k = \binom { \mathrm { d e f l e c t i v e \ ^ { * } a c c e l e r a t i o n " } } { \mathrm { o f \ w a v e g u i d e } } ; } \end{array}
$$

and the difference $\delta k = \nabla _ { \eta } k$ between the wave vectors of the two parts of the wave (difference measured via parallel transport） satisfies the equation

$$
\begin{array} { r } { \pmb { \nabla } _ { k } \delta k = \pmb { \nabla } _ { k } \pmb { \nabla } _ { n } k = [ \pmb { \nabla } _ { k } , \pmb { \nabla } _ { n } ] k + \pmb { \nabla } _ { n } \pmb { \nabla } _ { k } k } \\ { = R i e m a n \pmb { n } ( . . , k , k , n ) + \pmb { \nabla } _ { n } \underbrace { \pmb { \nabla } _ { k } k } _ { \pmb { \downarrow } } } \\ { \mathrm { d e f l e c t i v e ~ a c c e l e r a t i o n ~ o f ~ w a v e ~ g u i d e ] } \dagger } \end{array}
$$

The waveguide influences the direction of propagation of the waves, but not their frequency. Thus only Riemann enters into the 0 component of the above equation:

$$
\begin{array} { r } { k ^ { \hat { \alpha } } \delta k ^ { \hat { 0 } } { } _ { , \hat { \alpha } } = R ^ { \hat { 0 } } { } _ { \hat { \alpha } \hat { \beta } \hat { \gamma } } k ^ { \hat { \alpha } } k ^ { \hat { \beta } } n ^ { \hat { \gamma } } . } \end{array}
$$

4. Let k = ωe be the angular frequency of the electromagnetic wave: The direction of the space component $\pmb { k }$ of the propagation 4-vector is along the purely spatial vector $\pmb { n }$ ; so

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0016_pages_1051-1120/auto/images/1fa513f027a17f02b0c027a8af69747aae65b875e7b7c515511a2bdd9b829d99.jpg)  
Box 37.6 (continued)

$$
k ^ { \hat { 0 } } = \omega _ { e } , ~ k = ( v \omega _ { e } / r \hat { \delta } \alpha ) n , ~ n ^ { \hat { 0 } } = 0 .
$$

Use these relations to rewrite equation (5） as

$$
\begin{array} { r l } & { ( d \delta \omega _ { e } / d \hat { t } ) _ { \mathrm { m o v i n g w i t h p h o t o n s } } } \\ & { \qquad = ( v \omega _ { e } / r \hat { \delta } \alpha ) R _ { \hat { \ i } \hat { 0 } \hat { j } } ^ { \hat { 0 } } n ^ { \hat { \ i } } n ^ { \hat { j } } . } \end{array}
$$

5. Combine the expression for n in the spacetime diagram with equations (2) and (7), and with the world line \$= α + ωt for the photons, to obtain

$$
\begin{array} { r l r } {  { ( d \delta \omega _ { e } / d \hat { t } ) _ { \mathrm { m o v i n g w i t h p h o t o n s } } } } \\ & { } & { = - \frac { 1 } { 2 } v \omega _ { e } \omega ^ { 2 } \mathcal { \vec { G } } r ( \cos 2 \alpha ) \delta \alpha . } \end{array}
$$

6. Integrate over time and over $\pmb { \alpha }$ to obtain

Spacetime   
diagram Photon“a” Photon "a + δ” 8k   
n= (vector coneting） = rδa(-sinΦe, + cosΦey)

$$
\omega _ { e } = \omega _ { e o } \Big [ 1 - \frac { 1 } { 4 } \mathcal { { O } } v ( \sin { 2 \alpha } ) ( \omega r ) ( \omega \hat { t } ) \Big ] .
$$

# PART IX

# EXPERIMENTAL TESTSOF GENERAL RELATIVITY

Wherein the reader is tempted by a harem of charming gravitation theories (and some not so charming),is saved from   
his foolish passions by an army of experiments,cleaves unto his   
faithful spouse,Geometrodynamics,vows to lead an honest life hereafter,and becomes a True Believer.
