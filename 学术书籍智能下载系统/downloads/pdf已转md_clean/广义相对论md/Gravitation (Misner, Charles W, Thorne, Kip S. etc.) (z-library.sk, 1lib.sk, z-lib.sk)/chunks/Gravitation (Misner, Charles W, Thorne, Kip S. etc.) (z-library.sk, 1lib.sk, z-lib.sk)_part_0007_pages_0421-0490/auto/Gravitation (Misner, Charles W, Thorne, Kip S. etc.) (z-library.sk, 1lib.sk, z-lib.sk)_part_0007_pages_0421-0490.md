# Box 16.2 PROOF THAT A PENDULUM CLOCK AT REST ON THE EARTH'S SURFACE IS IDEAL

That is, a proof that it measures the interval $d \tau = ( - g _ { \alpha \beta } d x ^ { \alpha } d x ^ { \beta } ) ^ { 1 / 2 }$

# A. Constraint on the Pendulum

It must be so small that it cannot couple to the spacetime curvature-i.e., so small that the Earth's gravitational field looks uniform in its neighborhood—and that the velocity of its ball is totally negligible compared to the speed of light.

# B. Coordinate System and Metric

(l） General coordinate system: because the Earth's field is nearly Newtonian, one can introduce the coordinates of “linearized theory” $( \ S 1 8 . 4$ ；one must take this on faith until one reaches that point) in which

$$
d s ^ { 2 } = - ( 1 + 2 \varPhi ) d t ^ { \prime 2 } + ( \mathrm { I } - 2 \varPhi ) ( d x ^ { \prime 2 } + d y ^ { \prime 2 } + d z ^ { \prime 2 } ) ,
$$

where $\pmb { \phi }$ is the Newtonian potential.

![](images/fa84a4f2db43d091f9214e0e842d64408d905d9025131151800e45fe02a2729c.jpg)

(2）Put the origin of coordinates at the pendulum's equilibrium position, and orient the $x ^ { \prime } , z ^ { \prime } .$ -plane so the pendulum swings in it.

(3) Renormalize the coordinates so they measure proper length and proper time at the equilibrium position

$$
t = [ 1 + 2 \phi ( 0 ) ] ^ { 1 / 2 } t ^ { \prime } , \qquad x ^ { j } = [ 1 - 2 \phi ( 0 ) ] ^ { 1 / 2 } x ^ { j ^ { \prime } } .
$$

Then near the pendulum (inhomogeneities in the field neglected!)

$$
\phi = \phi ( 0 ) + g z , \qquad g = \mathrm { ^ { * } a c c e l e r a t i o n ~ o f ~ g r a v i t y , ^ { * } }
$$

$$
d s ^ { 2 } = { } - ( 1 + 2 g z ) d t ^ { 2 } + ( 1 - 2 g z ) ( d x ^ { 2 } + d y ^ { 2 } + d z ^ { 2 } ) .
$$

# C. Analysis of Pendulum Motion

(l） Put the total mass $m$ of the pendulum in its ball (negligible mass in its rod). Let its rod have proper length $l .$

(2) Calculate the 4-acceleration $\pmb { a } = \pmb { \nabla } _ { \pmb { u } } \pmb { u }$ of the pendulum's ball in terms of $d ^ { 2 } x ^ { \alpha } / d t ^ { 2 }$ ，using the velocity condition $v < < < 1$ and $d t / d \tau \approx 1$ ：

$$
\begin{array} { r l } & { a ^ { z } = d ^ { 2 } x / d \tau ^ { 2 } + \Gamma ^ { z } { } _ { 0 0 } ( d t / d \tau ) ^ { 2 } = d ^ { 2 } x / d t ^ { 2 } + \Gamma ^ { z } { } _ { 0 0 } = d ^ { 2 } x / d t ^ { 2 } , } \\ & { a ^ { z } = d ^ { 2 } z / d \tau ^ { 2 } + \Gamma ^ { z } { } _ { 0 0 } ( d t / d \tau ) ^ { 2 } = d ^ { 2 } z / d t ^ { 2 } + \Gamma ^ { z } { } _ { 0 0 } = d ^ { 2 } z / d t ^ { 2 } + g . } \end{array}
$$

(3）This 4-acceleration must be produced by the forces in the rod,and must be directed up the rod so that (for $x \ll l \ s _ { 0 } \ g \gg d ^ { 2 } z / d t ^ { 2 } )$

$$
d ^ { 2 } x / d t ^ { 2 } = a ^ { x } = - ( x / l ) a ^ { z } = - ( g / l ) x .
$$

(4） Solve this differential equation to obtain

$$
x = x _ { 0 } \cos { ( t \sqrt { g / l } ) } .
$$

(5) Thus conclude that the pendulum is periodic in $t$ ，which is proper time at the ball's equilibrium position (see equation 2).This means that the pendulum isan ideal clock when it is at rest on the Earth's surface.

Note: The above analysis ignores the Earth's rotation; for an alternative analysis including rotation,one can perform a similar calculation at the origin of the pendulum's“proper reference frame”[S13.6; line element (13.71)]. The answer is the same; but now $" g "$ is a superposition of the“gravitational acceleration,”and the “centrifugal acceleration produced by Earth's rotation.”

Consider an atomic clock with frequency stabilized by some atomic or molecular process-for exam-ple, fixed by the“umbrella vibrations” of ammonia molecules [see Feynman et. al. (l964)]. When subjected to suficiently strong accelerations or tidal forces,such a clock will cease to measure proper time with its normal precision. Two types of effects could lead to such departures from "ideality":

A. Infuence of the acceleration or tidal force on the atomic process that provides the frequency stability. Example: If tidal forces are significant over distances of a few angstroms (e.g., near a spacetime “singularity” terminating gravitational collapse), then they can and will deform an ammonia molecule and destroy the regularity of its umbrella vibrations, thereby making useless any ammonia atomic clock,no matter how constructed. Similarly,if an ammonia molecule is subjected to accelerations of magnitude comparable to its internal atomicaccelerations $( a \sim \mathrm { 1 0 ^ { 1 2 \cdots } } g ^ { \cdots } \sim 1 0 ^ { 1 5 } \mathrm { c m / }$ $\mathsf { s e c } ^ { 2 } )$ ，which change in times of the order of the “umbrella”vibration period,then it must cease to vibrate regularly,and any clock based on its vibrations must fail. Such limits of principle on the ideality of a clock will vary from one atomic proc-ess to another. However, they are far from being a limiting factor on clock construction in 1973. Much more important today is:

B. Influence of the acceleration or tidal force on the macroscopic structure of the clock-a structure dictated by current technology. The crystal oscillator, which produces the periodic signal output, must be locked to the regulating atomic process in some way. The lock will be disturbed by moderate accelerations. The toughest task for the manufacturer of aircraft clocks is to guarantee that precise locking will be maintained,even when the aircraft is maneuvering desperately to avoid collision with another aircraft or with a missile.In 1972 a solidly built rubidium clock will maintain its lock,with no apparent degradation of stability

$[ \Delta t / t \sim 1 0 ^ { - 1 2 } ( 1 ~ \mathrm { s e c } / t ) ^ { 1 / 2 }$ for 1 sec ≤t ≤ 10³ sec] under steady-state accelerations up to $5 0 ~ \ " g ^ { \prime \prime }$ or more.But, because of the finite bandwidth of the lock loop (typically $\varDelta \nu \sim 2 0$ to $5 0 \ \mathrm { H z }$ ，sudden changes in acceleration will temporarily break the lock,degrading the clock stability to that of the unlocked crystal oscillator-for which an acceleration $\pmb { a }$ produces a change in frequency of about $( a / \mathrm { I } \ ^ {  } g ^ { , - } ) \times \mathrm { I 0 ^ { - 9 } }$ . But the lock to the rubidium standard is restored quickly $( \delta t \sim 1 / \Delta \nu )$ ，bringing the clock back to its normal highly stable performance.\*

Tidal forces are so small in the solar system that the clock manufacturer can ignore them. However, a 1973 atomic clock, subjected to the tidal accelerations near a spacetime singularity,should break the “lock” to its atomic process long before the tidal forces become strong enough to influence the atomic process itself.

Ideal rods and clocks constructed from geodesic world lines

as governed by the metric-though,of course,it is also tied to other things, such as cigarette smoking.

In principle,one can build ideal rods and clocks from the geodesic world lines of freely falling test particles and photons. (See Box l6.4.) In other words,spacetime has its own rods and clocks built into itself,even when matter and nongravitational fields are absent!

# Box 16.4 IDEAL RODS AND CLOCKS BUILT FROM GEODESIC WORLD' LINES\*

The Standard Interual. A specific timelike interval-the interval between two particular neighboring events $\boldsymbol { \mathcal { a } }$ and $\mathcal { B }$ -is chosen as the standard interval,and is assigned unit length. It is used to calibrate a huge set of geodesic clocks that pass through $\boldsymbol { \mathcal { a } }$

![](images/1ca4a14cf1a108252139859bc4fa67f91ae8ba487abc5839e9952826e3cd57bc.jpg)

Each geodesic clock is constructed and calibrated as follows:

(l） A timelike geodesic $\boldsymbol { \mathcal { a } } \boldsymbol { \mathcal { e } }$ (path of freely falling particle） passes through $\boldsymbol { \mathcal { a } }$   
(2)A neighboring world line, everywhere parallel to $\boldsymbol { \mathcal { a } } \boldsymbol { \mathcal { e } }$ (and thus not a geodesic),is constructed by the method of Schild's ladder (Box 10.2), which relies only on geodesics.   
(3）Light rays (null geodesics） bounce back and forth between these parallel world lines; each round trip constitutes one “tick.”   
(4) The proper time lapse, $\tau _ { 0 }$ ，between ticks is related to the interval $\boldsymbol { \mathcal { a B } }$ by $\begin{array} { r } { - 1 \equiv ( \mathscr { Q } ^ { \varsigma \beta } ) ^ { 2 } = - ( N _ { 1 } \tau _ { 0 } ) ( N _ { 2 } \tau _ { 0 } ) , } \end{array}$ where $N _ { \imath }$ and $N _ { 2 }$ are the number of ticks between the events shown in the diagrams. [Proof: see diagram at right.]

to point $\mathcal { E }$

![](images/18904a7adc7e5a5e3d072638f8b3e34d4d760b247fa25aedc55fd0fc6119b7b8.jpg)

Spacetime is filled with such geodesic clocks. Those that pass through $\boldsymbol { \mathcal { a } }$ are calibrated as above against the standard interval $\mathcal { Q } \mathfrak { s } \beta$ ，and are used subsequently to calibrate all other clocks they meet.

In local Lorentz rest frame of geodesic clock:

$$
\begin{array} { c } { { ( N _ { 1 } \tau _ { 0 } ) ( N _ { 2 } \tau _ { 0 } ) = ( t - x ) ( t + x ) } } \\ { { = t ^ { 2 } - x ^ { 2 } = - ( d \llap / \llap / \llap / } } \end{array}
$$

Any interval $\mathcal { P T }$ along the world line of a geodesic clock can be measured by the same method as was used in calibration.The interval $\mathcal { P Q }$ can be timelike, spacelike, or null; its squared length in all three cases will be

$$
( \mathcal { P Q } ) ^ { 2 } = - ( N _ { 3 } \tau _ { 0 } ) ( N _ { 4 } \tau _ { 0 } )
$$

To achieve a precision of measurement good to one part in $N _ { \bullet }$ where $N$ is some large number, take two precautions:

(1） Demand that the intervals $\boldsymbol { \mathcal { Q } } \boldsymbol { \mathcal { B } }$ and $\mathcal { P Q }$ be sufficiently small compared to the scale of curvature of spacetime; or specifically,

$$
R ^ { ( A B ) } ( { \mathcal { Q B } } ) ^ { 2 } \leqslant 1 / N
$$

and

$$
R ^ { ( P Q ) } ( { \mathcal P } \mathscr { Q } ) ^ { 2 } \leqslant 1 / N ,
$$

where R4B) and RPQ are the largest relevant components of the curvature tensor in the two regions in question.

(2) Demand that the time scale, $\tau _ { 0 }$ , of the geodesic clocks employed be small compared to $\boldsymbol { \mathcal { a B } }$ and $\mathcal { P } \mathcal { Q }$ individually; thus,

$$
\begin{array} { r } { \tau _ { 0 } \ll \mathcal { Q B } / N , } \\ { \tau _ { 0 } \ll \mathcal { P Q } / N . } \end{array}
$$

The Einstein principle that spacetime is described by Riemannian geometry exposes itself to destruction by a “thousand” tests.Thus,from the fiducial interval, $\mathcal { Q B }$ ,to the interval under measurement, $\mathcal { P D }$ ,there are a “score”of routes of intercomparison, all of which must give the same value for the ratio ${ \mathcal { P Q } } / { \mathcal { Q B } }$ Moreover, one can easily select out “fifty” intervals $\mathcal { P Q }$ to which the same kind of test can be applied. Such tests are not all items for the future.

Some $5 \times 1 0 ^ { 9 }$ years ago, electrons arrived by different routes at a common location,a given atom of iron in the core of the earth. This iron atom does not collapse. The Pauli principle of exclusion keeps the electrons from allfalling into the K-orbit. The Pauli principle would not apply if the electrons were not identical or nearly so. From this circumstance it would appear possible to draw an important conclusion (Marzke and Wheeler).With each electron is associated a standard length, its Compton wavelength, $\hbar / m c$ If these lengths had started different, or changed by different amounts along the different routes, and if the resulting difference in properties were as great as one part in

![](images/c5de79a66445d1f60d689935392bcbb32953ce5eff52238853cb16ce920b13ce.jpg)

$$
\begin{array} { r } { \sim ( 5 \times 1 0 ^ { 9 } ~ \mathrm { y r } ) \times ( 3 \times 1 0 ^ { 7 } ~ \mathrm { s e c / y r } ) ~ } \\ { \times ( 5 \times 1 0 ^ { 1 8 } ~ \mathrm { r e v / s e c } ) \sim 1 0 ^ { 3 6 } , } \end{array}
$$

by now this difference would have shown up, the varied electrons would have fallen into the ${ \bf K } \cdot { \bf \Omega }$ orbit,and the earth would have collapsed,contrary to observation.

The Marzke-Wheeler construction expresses an arbitrary small interval $\mathcal { P Q }$ ， anywhere in spacetime,in terms of the fiducial interval $\smash { \mathcal { Q } \mathfrak { G } _ { 3 } } ^ { }$ aninterval which itself may be taken for definiteness to be the“geometrodynamic standard centimeter" of $\ S 1 . 5$ . This construction thus gives a vivid meaning to the idea of Riemannian geometry.

The M-W construction makes no appeal whatsoever to rods and clocks of atomic constitution. This circumstance is significant for the following reasons. The length of the usual platinum meter stick is some multiple, $N _ { 1 } ( \hbar ^ { 2 } / m e ^ { \bar { 2 } } )$ ，of the Bohr atomic radius. Similarly, the wavelength of the $\mathbf { K r ^ { 8 6 } }$ line is some multiple, $N _ { 2 } ( \hbar c / e ^ { 2 } ) ( \hbar ^ { 2 } / m e ^ { 2 } ) .$ of a second basic length that depends on the atomic constants in quite a different way. Thus,if there is any change with time in the dimensionless ratio $\hbar c / e ^ { 2 } = 1 3 7 . 0 3 8$ ,one or the other or both of these atomic standards of length must get out of kilter with the geometrodynamic standard centimeter. In this case, general relativity says,“Stick to the geometrodynamic standard centimeter.”

Hermann Weyl at first thought that one could carry out the comparison of lengths by light rays alone,but H. A. Lorentz pointed out that one can dispense with the geodesics neither of test particles nor of light rays in the measurement process, the construction for which,however, neither Weyl nor Lorentz supplied [literature in Marzke and Wheeler (1964)). Ehlers,Pirani,and Schild (1972) have given a deeper analysis of the separate parts played in the measurement process by the affine connection, by the conformal part of the metric, and by the full metric.

# $\$ 16.5$ . THE MEASUREMENT OF THE GRAVITATIONAL FIELD

“I know how to measure the electromagnetic field using test charges; what is the analogous procedure for measuring the gravitational field?” This question has,at the same time,many answers and none.

It has no answers because nowhere has a precise definition of the term“gravitational field" been given-nor will one be given.Many different mathematical entities are associated with gravitation: the metric, the Riemann curvature tensor, the Ricci curvature tensor, the curvature scalar, the covariant derivative, the connection coefficients,etc. Each of these plays an important role in gravitation theory,and none is so much more central than the others that it deserves the name “gravitational field.”Thus it is that throughout this book the terms “gravitational field”and “gravity” refer in a Vague, collective sort of way to all of these entities. Another, equivalent term used for them is the“geometry of spacetime.”

The many faces of gravity, and how one measures them

To“measure the gravitational feld,” then, means to “explore experimentally various properties of the spacetime geometry.” One makes different kinds of measurements, depending on which geometric property of spacetime one is interested in.However,all such measurements must involve a scrutiny of the effects of the spacetime geometry (i.e., of gravity) on particles,on matter, or on nongravitational fields.

For example, to “measure” the metric near a given event, one typically lays out a latticework of rods and clocks (local orthonormal frame,small enough that curva-ture effects are negligible), and uses it to determine the interval between neighboring events. To measure the Riemann curvature tensor near an event, one typically studies the geodesic deviation (relative accelerations) that curvature' produces between the world lines of a variety of neighboring test particles; alternatively, one makes measurements with a“gravity gradiometer” (Box l6.5) if the curvature is static or slowly varying; or with a gravitational wave antenna (Chapter 37) if the curvature fluctuates rapidly. To study the large-scale curvature of spacetime, one examines large-scale effects of gravity,such as the orbits of planets and satellites,or the bending of light by the sun's gravitational field.

But whatever aspect of gravity one measures,and however one measures it, one is studying the geometry of spacetime.

# Exercise 16.5. GRAVITY GRADIOMETER

The gravity gradiometer of Box l6.5 moves through curved spacetime along an accelerated world line. Calculate the amplitude and phase of oscillation of one arm of the gradiometer relative to the other. [Hint: Perform the calculation in the gradiometer's“proper reference frame" $( \ S 1 3 . 6 )$ ,with Fermi-Walker-transported basis vectors. Use,as the equation for the relative angular acceleration of the two arms,

$$
2 m \hat { L } ^ { 2 } ( \ddot { \alpha } + \dot { \alpha } / \tau _ { 0 } + { \omega _ { 0 } } ^ { 2 } \alpha ) = \binom { \mathrm { D r i v i n g ~ t o r q u e ~ p r o d u c e d ~ b y } } { \mathrm { R i e m a n n ~ c u r v a t u r e } } ,
$$

where

$$
{ \begin{array} { r l } { { 2 } m \mathbb { L } ^ { 2 } = ( { \mathrm { m o m e n t ~ o f ~ i n e r i a ~ o f ~ o n e ~ a r m } } ) , } & \\ & { \qquad \alpha = ( { \mathrm { a n g u l a r ~ d i s p l a c e m e n t ~ o f ~ o n e ~ a r m ~ f r o m ~ e q u i l i b r i u m } } ) , } \\ { { \frac { \pi } { 2 } } + 2 \alpha = ( { \mathrm { a n g u l a r ~ s e p a r a t i o n ~ o f ~ t h e ~ t w o ~ a r m s } } ) , } \\ { 2 m \mathbb { L } ^ { 2 } { \omega _ { 0 } } ^ { 2 } = ( { \mathrm { t o r s i o n a l ~ s p r i n g ~ c o n s t a n t } } ) , } \\ & { \qquad \omega _ { 0 } = ( { \mathrm { a n g u l a r ~ f r e q u e n c y ~ o f ~ f r e e ~ v i b r a t i o n s } } ) , } \\ & { \qquad \tau _ { 0 } = ( { \mathrm { d e c a y ~ t i m e ~ f o r ~ f r e e ~ v i b r a t i o n s ~ t o ~ d a m p ~ o u t ~ d u e ~ t o } } } \\ & { \qquad { \mathrm { i n t e r m a l ~ f r i c t i o n a l ~ f o r e s } } ) . } \end{array} }
$$

If $\pmb { \xi }$ is the vector from the center of mass of the gradiometer to mass 1,then one has

$$
\begin{array} { r } { \cdot \left( \begin{array} { l } { \mathrm { c u r v a t u r e - p r o d u c e d } } \\ { \mathrm { a c c e l e r a t i o n ~ o f ~ m a s s ~ } 1 } \\ { \mathrm { r e l a t i v e ~ t o ~ c e n t e r ~ o f } } \\ { \mathrm { g r a d i o m e t e r } } \end{array} \right) _ { \hat { k } } = \left( \frac { D ^ { 2 } \xi _ { \hat { k } } } { d \tau ^ { 2 } } \right) _ { \mathrm { g e o d e s i o n } } = - R _ { \hat { k } \hat { 0 } \hat { 1 } \hat { 0 } } \xi _ { \hat { l } } ; } \end{array}
$$

(continued on page 403)

# Box 16.5 GRAVITY GRADIOMETER FOR MEASURING THE RIEMANN CURVATURE OF SPACETIME

![](images/dd881ac6bff8d0b6d58768b7e3209b1e0e505255181767a00e506951532ae64e.jpg)

This gravity gradiometer was designed and built by Robert M.Forward and his colleagues at Hughes Research Laboratories, Malibu, California. It measures the Riemann curvature of spacetime produced by nearby masses. By flying a more advanced version of such a gradiometer in an airplane above the Earth's surface, one should be able to measure subsurface mass variations due to varying geological structure. In an Earth-orbiting satellite, such a gradiometer could measure the gravitational multipole moments of the Earth. Technical details of the gradiometer are spelled out in the papers of Forward (1972),and Bell, Forward,and Williams (1970). The principles of its operation are outlined below.

The gradiometer consists of two orthogonal arms with masses m on their ends,connected at their centers by a torsional spring. When the arms are twisted out of orthogonal alignment, they oscillate. A piezoelectric strain transducer is used to measure the oscillation amplitude.

![](images/c1a3e68b03150c9f2ddd7759b55a0b5fd1adfd7aeac0fd2adeb5a775b52308ea.jpg)

When placed near an external mass, $M _ { i }$ the gradiometer experiences a torque: because of the gradient in the gravitational field of $M$ (i.e., because of the spacetime curvature produced by $M _ { j }$ ，the Newtonian forces $F _ { 1 }$ and $F _ { 2 }$ are greater than $F _ { 3 }$ and $F _ { 4 }$ ； so a net torque pulls masses 1 and 2 toward each other, and 3 and 4 toward each other. [Note: the forces $F _ { 1 } , F _ { 2 } , F _ { 3 } , F _ { 4 }$ depend on whether the gradiometer is in free fall (geodesic motion; $\pmb { \nabla } _ { \pmb { u } } \pmb { u } = 0 ;$ or is moving on an accelerated world line. But the net torque is unaffected by acceleration; acceleration produces equal Newtonian forces on al four masses, with zero net torque.]

![](images/72cc91443e8a8021485f403e24fda546f6ee196d0364a9b04136d4adcc4badf6.jpg)  
Box 16.5 (continued)

![](images/55d397fe487bafd2cd35b72d6568949e163d0fdf22e97ac5e1df6660a7a85b2f.jpg)

When in operation the gradiometer rotates with angular velocity $\omega$ about its center. As it rotates, the torques on its arms oscillate:

at $\omega t = 0$ net torque pushes 1 and 2 toward each other;   
at $\omega t = \pi / 4$ net torque is zero;   
at $\omega t = \pi / 2$ net torque pushes l and 2 away from each other.

The angular frequency of the oscillating torque is $2 \omega$ If $\mathtt { 2 \omega }$ is set equal to $\omega _ { 0 } \equiv$ (natural oscillation frequency of the arms)， the oscillating torque drives the arms into resonant oscillation. The resulting oscillation amplitude,in the1970 prototype of the gradiometer, was easily detectable for gravity gradients (Riemann curvatures) of magnitude

$$
\begin{array} { r l r } {  { \gtrsim 0 . 0 0 0 2 [ \frac { 2 ( \mathrm { m a s s ~ o f ~ e a r t h } ) } { ( \mathrm { r a d i u s ~ o f ~ e a r t h } ) ^ { 3 } } ] } } \\ & { } & { \sim 1 \times 1 0 ^ { - 3 0 } \mathrm { c m } ^ { - 2 } \sim . 0 1 \mathrm { g } / \mathrm { c m } ^ { 3 } } \end{array}
$$

[Riemann curvature produced by a two-kilometer high mountain,idealized as a two-kilometer high cube,at a distance of 15 kilometers.(Neglected in this idealization are isostacy and any lowering of density of Earth's crust in regions of mountain Luplift.)

For a mathematical analysis of the gradiometer, see exercise 16.5.

$$
\begin{array} { r l } & { \left( \begin{array} { l } { \mathrm { t o r q u e ~ a c t i n g ~ o n ~ m a s s ~ } 1 } \\ { \mathrm { r e l a t i v e ~ t o ~ c e n t e r ~ o f } } \\ { \mathrm { g r a d i o m e t e r } } \end{array} \right) _ { \mathrm { i } } = \epsilon _ { i j k } \xi _ { j } ( - m R _ { k \widehat { 0 } l { 0 } } \xi _ { l } ) . } \end{array}
$$

The torque on mass 4 is identical to this (replace $\pmb { \xi }$ by $- \pmb { \xi } )$ ， so the total torque on arm 1-4 is twice this. The components $R _ { \hat { k } \hat { 0 } \hat { l } \hat { 0 } }$ of Riemann can be regarded as components of a $3 \times 3$ symmetric matrix.By appropriate orientation of the reference frame's spatial axes (orientation along“principal axes” of $R _ { \hat { k } \hat { 0 } \hat { l } \hat { 0 } } )$ , one can make $R _ { \hat { k } \hat { 0 } \hat { 1 } \hat { 0 } }$ diagonal at some initial moment of time

$$
R _ { \hat { x } \hat { 0 } \hat { z } \hat { 0 } } \neq 0 , R _ { \hat { y } \hat { 0 } \hat { y } \hat { 0 } } \neq 0 , R _ { \hat { z } \hat { 0 } \hat { z } \hat { 0 } } \neq 0 , \mathrm { a l l ~ o t h e r s ~ v a n i s h } .
$$

Assume that Riemann changes suffciently slowly along the gradiometer's world line that throughout the experiment $R _ { \widehat { j } \widehat { 0 } \widehat { k } \widehat { 0 } }$ remains diagonal and constant. For simplicity， place the gradiometer in the $\hat { x } , \hat { y }$ plane, so it rotates about the $\hat { z }$ axis with angular velocity $\omega \approx _ { \mathrm { 2 } } ^ { \mathrm { 1 } } \omega _ { 0 } \mathrm { , }$ ：

$$
{ \binom { \mathrm { \bf A n g l e ~ o f ~ a r m ~ } 1 . 4 } { \mathrm { \bf r e l a t i v e ~ t o ~ } \hat { x } ~ a x i s } } = \omega t .
$$

Show that the resultant equation of oscillation is

$$
\ddot { \alpha } + \dot { \alpha } / \tau _ { 0 } + { \omega _ { 0 } } ^ { 2 } \alpha = \frac { 1 } { 2 } ( R _ { \hat { x } \hat { 0 } \hat { x } \hat { 0 } } - R _ { \hat { y } \hat { 0 } \hat { y } \hat { 0 } } ) \sin 2 \omega t ;
$$

and that the steady-state oscillations are

$$
\alpha = I m \left\{ \frac { \frac { 1 } { 2 } ( R _ { \hat { x } \hat { 0 } \hat { x } \hat { 0 } } - R _ { \hat { y } \hat { 0 } \hat { y } \hat { 0 } } ) } { 2 \omega _ { 0 } ( \omega _ { 0 } - 2 \omega + i / 2 \tau _ { 0 } ) } e ^ { \mathsf { i } 2 \omega t } \right\} .
$$

Thus,for fixed $\pmb { \omega }$ (e.g., $2 \omega = \omega _ { 0 } )$ ,by measuring the amplitude and phase of the oscillations, one can learn the magnitude and sign of $R _ { \hat { z } \hat { 0 } \hat { z } \hat { 0 } } - R _ { \hat { y } \hat { 0 } \hat { y } \hat { 0 } }$ The other differences, $R _ { \hat { y } \hat { 0 } \hat { y } \hat { 0 } } -$ $R _ { \hat { z } \hat { 0 } \hat { z } \hat { 0 } }$ and $R _ { \hat { z } \hat { 0 } \hat { z } \hat { 0 } } - R _ { \hat { z } \hat { 0 } \hat { z } \hat { 0 } }$ can be measured by placing the gradiometer's rotation axis along the $\hat { x }$ and $\hat { y }$ axes,respectively.]

# CHAPTER 17

# HOW MASS-ENERGY GENERATES CURVATURE

The physical world is represented as a four-dimensional continuum、If in this 丨 adopt a Riemannian metric,and look for the simplest laws which such a metric can satisfy, I arrive at the relativistic gravitation theory of empty space. If 丨 adopt in this space a vector field,or the antisymmetrical tensor field derived from it,and if l look for the simplest laws which such a field can satisfy, I arrive at the Maxwell equations for free space. ...at any given moment, out of all conceivable constructions, a single one has always proved itself absolutely superior to all the rest...

ALBERT EINSTEIN (1934，p.18)

This section derives the "Einstein field equation"

# $\$ 17.1$ . AUTOMATIC CONSERVATION OF THE SOURCE AS THE CENTRAL IDEA IN THE FORMULATION OF THE FIELD EQUATION

Turn now from the response of matter to geometry (motion of a neutral test particle on a geodesic; “comma-goes-to-semicolon rule” for the dynamics of matter and fields),and analyze the response of geometry to matter.

Mass is the source of gravity. The density of massenergy as measured by any observer with 4-velocity $\pmb { u }$ is

$$
\rho = { \pmb u } \cdot { \pmb T } \cdot { \pmb u } = u ^ { \alpha } T _ { \alpha \beta } u ^ { \beta } .
$$

Therefore the stress-energy tensor $\pmb { \tau }$ is the frame-independent “geometric object” that must act as the source of gravity.

This source, this geometric object, is not an arbitrary symmetric tensor. It must have zero divergence

$$
\begin{array} { r } { \pmb { \nabla } \cdot \pmb { T } = 0 , } \end{array}
$$

because only so can the law of conservation of momentum-energy be upheld.

Place this source, $\tau ,$ on the righthand side of the equation for the generation of gravity. On the lefthand side willstand a geometric object that characterizes gravity. That object, like $\tau ,$ must be a symmetric, divergence-free tensor;and if it is to characterize gravity,it must be built out of the geometry of spacetime and nothing but that geometry. Give this object the name “Einstein tensor” and denote it by $\pmb { G }$ ，so that the equation for the generation of gravity reads

Equation describing how matter generates gravity must have form $\pmb { G } = \kappa \pmb { T } ,$ where $\pmb { \tau }$ is stress-energy tensor

$$
\begin{array} { l } { \pmb { G } = \kappa \pmb { \tau } . } \\ { \qquad \sum _ { \left[ \mathbb { P } ^ { \mathrm { r o p o r t i o n a l i t y ~ f a c t o r } ;  } } } \en\right]d{array} \end{array}
$$

(Do not assume that $\pmb { G }$ is the same Einstein tensor as was encountered in Chapters 8,13,14,and 15; that will be proved below!)

The vanishing of the divergence $\mathbf { \nabla } \textbf { \textrm { w } } \mathbf { \hat { s } }$ is not to be regarded as a consequence of $\pmb { \nabla } \cdot \pmb { \tau } = 0$ .Rather,the obedience of all matter and fields to the conservation law $\pmb { \nabla } \pmb { \cdot } \pmb { \tau } = 0$ is to be regarded (l) as a consequence of the way [equation (17.3)] they are wired into the geometry of spacetime,and therefore (2) as required and enforced by an automatic conservation law,or identity, that holds for any smooth Riemannian spacetime whatsoever,physical or not: ${ \pmb { \nabla } } \pmb { \cdot } { \pmb { G } } \equiv 0$ (See Chapter 15 for a fuller discussion and $\ S 1 7 . 2$ below for a fuller justification.) Accordingly,look for a symmetric tensor $\pmb { G }$ that is an “automatically conserved measure of the curvature of spacetime” in the following sense:

(1) $\pmb { G }$ vanishes when spacetime is flat.   
(2) $\pmb { G }$ is constructed from the Riemann curvature tensor and the metric,and from nothing else.   
(3） $\pmb { G }$ is distinguished from other tensors which can be built from Riemann and $\pmb { \mathscr { g } }$ by the demands (i) that it be linear in Riemann, as befits any natural measure of curvature; (ii) that, like $\tau ,$ it be symmetric and of second rank; and (ii) that it have an automatically vanishing divergence,

Properties that the tensor $\pmb { G }$ must have

$$
{ \pmb { \nabla } } \cdot { \pmb { G } } \equiv 0 .
$$

Apart from a multiplicative constant, there is only one tensor (exercise 17.l） that satisfies these requirements of being an automatically conserved, second-rank tensor, linear in the curvature,and of vanishing when spacetime is flat. It is the Einstein curvature tensor, $\pmb { G }$ ,expressed in Chapter 8 in terms of the Ricci curvature tensor:

Proof that $\pmb { G }$ must be the Einstein curvature tensor of Chapter 8

$$
\begin{array} { l } { { R _ { \mu \nu } = { R ^ { \alpha } } _ { \mu \alpha \nu } , } } \\ { { { \displaystyle G _ { \mu \nu } = R _ { \mu \nu } - \frac { 1 } { 2 } g _ { \mu \nu } R . } } } \end{array}
$$

This quantity was given vivid meaning in Chapter 15 as the“moment of rotation of the curvature” or, more simply,the “moment of rotation,” constructed by taking the double-dual

$$
G = { ^ { \ast } R i e m a n n ^ { \ast } }
$$

of the Riemann curvature tensor, and then contracting this double dual,

$$
G _ { \mu \nu } = { \mathcal { G } } ^ { \alpha } { } _ { \mu \alpha \nu } .
$$

Evaluation of $\kappa$ (in $\pmb { G } = \kappa \pmb { T } .$ by comparing with Newtonian theory of gravity

In Chapter 15 the vanishing of $\mathbf { v } \cdot \mathbf { G }$ was shown to follow as a consequence of the elementary principle of topology that “the boundary of a boundary is zero.”

To evaluate the proportionality constant $\kappa$ in the “Einstein field equation” $\pmb { G } = \kappa \pmb { T } ,$ one can compare with the well-tested Newtonian theory of gravity. To facilitate the comparison, examine the relative acceleration (geodesic deviation) of particles that fall down a pipe inserted into an idealized Earth of uniform density $\pmb { \rho }$ (Figure 1.12). According to Newton,the relative acceleration is governed by the density; according to Einstein,it is governed by the Riemann curvature of spacetime. Direct comparison of the Newtonian and Einstein predictions using Newtonian coordinates (where $g _ { \mu \nu } \approx \eta _ { \mu \nu } )$ reveals the relation

$$
R _ { 0 0 } \equiv { R ^ { \alpha } } _ { 0 \alpha 0 } = 4 \pi \rho .
$$

(See $\ S 1 . 7$ for details of the derivation; see Chapter l2 for extensive discussion of Newtonian gravity using this equation.） When applied to the Earth's interior, the Einstein field equation $\pmb { G } = \kappa \pmb { T }$ must thus reduce to $R _ { 0 0 } = 4 \pi \rho$ . In component form, the Einstein field equation reads

$$
G _ { \mu \nu } = R _ { \mu \nu } - \frac { 1 } { 2 } g _ { \mu \nu } R = \kappa T _ { \mu \nu } .
$$

Its trace reads

$$
- R = R - 2 R = { \kappa } T .
$$

In consequence, it predicts

$$
\begin{array} { l } { { \displaystyle R _ { 0 0 } = \frac { 1 } { 2 } g _ { 0 0 } R + \kappa T _ { 0 0 } = \frac { 1 } { 2 } \kappa ( 2 T _ { 0 0 } - \underbrace { g _ { 0 0 } } _ { \displaystyle - 1 } T ) } } \\ { ~ . } \\ { { \displaystyle ~ = \frac { 1 } { 2 } \kappa [ 2 T _ { 0 0 } + ( T ^ { 0 } _ { 0 } + T ^ { j } _ { j } ) ] } } \\ { ~ } \\ { { \displaystyle ~ = \frac { 1 } { 2 } \kappa ( T _ { 0 0 } + T ^ { j } _ { j } ) } , } \end{array}
$$

which reduces to

$$
R _ { 0 0 } = \frac { 1 } { 2 } \kappa \rho
$$

when one recals that for the Earth-as for any nearly Newtonian system-the stresses $T _ { j k }$ are very small compared to the density of mass-energy $T _ { 0 0 } = \rho$ ：

$$
\frac { | T _ { j k } | } { T _ { 0 0 } } \sim \frac { \mathrm { p r e s s u r e } } { \mathrm { d e n s i t y } } \sim \frac { d p } { d \rho } \sim ( \mathrm { v e l o c i t y ~ o f ~ s o u n d } ) ^ { 2 } \ll 1 .
$$

The equation $R _ { 0 0 } = 4 \pi \rho$ (derived by comparing relative accelerations in the Newton and Einstein theories)and the equation $R _ { 0 0 } = \textstyle { \frac { 1 } { 2 } } \kappa \rho$ (derived directly from the Einstein field equation) can agree only if the proportionality constant $\kappa$ is ${ 8 \pi }$

Thus,the Einstein field equation, describing the generation of curvature by mass-energy,must read

Result:"Einstein field equation" $\pmb { G } = 8 \pi \pmb { T }$

$$
{ \pmb { G } } = 8 \pi { \pmb { T } } .
$$

The lefthand side ("curvature") has units $\mathtt { c m } ^ { - 2 }$ ，since a curvature tensor is a linear machine into which one inserts a displacement (units: cm) and from which one gets a relative acceleration (units: $\mathsf { c m / s e c ^ { 2 } } \sim \mathsf { c m / c m ^ { 2 } } \sim \mathsf { c m ^ { - 1 } } ,$ .The right-hand side also has dimensions $\mathtt { c m } ^ { - 2 }$ , since it is a linear machine into which one inserts 4-velocity (dimensionless) and from which one gets mass density [units: $g / \mathrm { c m } ^ { 3 } \sim \mathrm { c m } / \mathrm { c m } ^ { 3 } \sim$ $\mathtt { c m } ^ { - 2 }$ ； recall from equation (1.12) and Box 1.8 that $1 \mathbf { g } = ( 1 \mathbf { g } ) \times ( G / c ^ { 2 } ) = ( 1 \mathbf { g } ) \times $ $( 0 . 7 4 2 \times 1 0 ^ { - 2 8 } ~ \mathrm { c m / g } ) = 0 . 7 4 2 \times 1 0 ^ { - 2 8 } ~ \mathrm { c m }$

This concludes the simplest derivation of Einstein's field equation that has come to hand, and establishes its correspondence with the Newtonian theory of gravity under Newtonian conditions. That correspondence had to be worked out to determine the factor $\kappa = 8 \pi$ on the righthand side of (17.9).Apart from this factor, the central point in the derivation was the demand for,and the existence of,a unique tensorial measure of curvature $\pmb { G }$ with an identically vanishing divergence.

# Exercise 17.1. UNIQUENESS OF THE EINSTEIN TENSOR

# EXERCISES

(a) Show that the most general second-rank, symmetric tensor constructable from Riemann and $\pmb { g }$ ,and linear in Riemann,is

$$
{ \begin{array} { r l } { a R _ { \alpha \beta } + b R g _ { \alpha \beta } + A g _ { \alpha \beta } } & { } \\ { = a R ^ { \mu } { } _ { \alpha \mu \beta } + b R ^ { \mu \nu } { } _ { \mu \nu } g _ { \alpha \beta } + A g _ { \alpha \beta } , } \end{array} }
$$

where $a , b ,$ and $\pmb { \varLambda }$ are constants.

(b) Show that this tensor has an automatically vanishing divergence if and only if $\begin{array} { r } { b = - \frac { 1 } { 2 } a . } \end{array}$

(c) Show that,in addition,this tensor vanishes in flat spacetime,if and only if $\varLambda = 0$ i.e., if and only if it is a multiple of the Einstein tensor $G _ { \alpha \beta } = R _ { \alpha \beta } - { \scriptstyle { \frac { 1 } { 2 } } } R g _ { \alpha \beta }$ (Do not bother to prove that ${ \pmb { \check { \bigtriangledown } } } \cdot { \pmb { \ 6 } } \equiv 0$ ； assume it as a result from Chapter l3.)

# Exercise 17.2. NO TENSOR CONSTRUCTABLE FROM FIRST DERIVATIVES OF METRIC

Show that there exists no tensor with components constructable from the ten metric coefcients $g _ { \alpha \beta }$ and their 40 first derivatives $g _ { \alpha \beta , \mu }$ except the metric tensor $\pmb { \mathscr { g } }$ , and products of it with itself; e.g, ${ \pmb g } \otimes { \pmb g }$ [Hint:Assume there exists some other such tensor,and examine its hypothesized components in a local inertial frame.]

# Exercise 17.3. RIEMANN AS THE ONLY TENSOR CONSTRUCTABLE FROM、AND LINEAR IN SECOND DERIVATIVES OF METRIC

Show that (l) Riemann, (2) $\pmb { \mathscr { g } }$ ，and (3) tensors (e.g.， Ricci） formed from Riemann and $\pmb { g }$ but linear in Riemann,are theonly tensors that (a)areconstructable fromthe ten $g _ { \alpha \beta \colon \_ }$ the $4 0 \ g _ { \alpha \beta , \mu }$ and the $1 0 0 \ g _ { \alpha \beta , \mu \nu } ,$ ,and (b) are linear in the $g _ { \alpha \beta , \mu \nu } .$ [Hint: Assume there exists some other such tensor, and examine its hypothesized components in an orthonormal, Riemann-normal coordinate system. Use equations (l1.30) to (1.32).]

# Exercise 17.4. UNIQUENESS OF THE EINSTEIN TENSOR

(a) Show that the Einstein tensor, ${ \cal G } _ { \alpha \beta } = { \cal R } _ { \alpha \beta } - { \scriptstyle \frac { 1 } { 2 } } { \cal R } g _ { \alpha \beta }$ , is the only second-rank,symmetric tensor that (1) has components constructable solely from $g _ { \alpha \beta } , g _ { \alpha \beta , \mu } , g _ { \alpha \beta , \mu \nu } ,$ (2) has components linear in $g _ { \alpha \beta , \mu \nu }$ (3)has an automatically vanishing divergence, $\pmb { \nabla } \pmb { \cdot } \pmb { G } = 0$ ; and (4) vanishes in flat spacetime. This provides added motivation for choosing the Einstein tensor as the left side of the field equation $\pmb { G } = 8 \pi \pmb { T } .$

(b） Show that, when condition (4) is dropped,the most general tensor is ${ \pmb { G } } + \varLambda { \pmb { g } }$ where A is a constant. (See $\ S 1 7 . 3$ for the significance of this.)

Einstein field equation governs the evolution of spacetime geometry

# $\$ 12$ . AUTOMATIC CONSERVATION OF THE SOURCE: A DYNAMIC NECESSITY

The answer $\pmb { G } = 8 \pi \pmb { T }$ is now on hand; but what is the question? An equation has been derived that connects the Einstein-Cartan“moment-of rotation”G with the stress-energy tensor $\pmb { \tau } ,$ but what is the purpose for which one wants this equation in the first place? If geometry tells matter how to move,and matter tells geometry how to curve,does one not have in one's hands a Gordian knot? And how then can one ever untie it?

The story is no different in character for the dynamics of geometry than it is for other branches of dynamics. To predict the future, one must first specify, on an "initial" hypersurface of "simultaneity,” the position and velocity of every particle, and the amplitude and time-rate of change of every field that obeys a second-order wave equation. One can then evolve the particles and fields forward in time by means of their dynamic equations. Similarly,one must give information about the geometry and its first time-rate of change on the “initial” hypersurface if the Einstein field equation is to be able to predict completely and deterministically the future timedevelopment of the entire system, particles plus fields plus geometry. (See Chapter 21 for details.)

If a prediction is to be made of the geometry, how much information has to be supplied for this purpose? The geometry of spacetime is described by the metric

$$
d s ^ { 2 } = g _ { \alpha \beta } ( \mathcal { P } ) d x ^ { \alpha } d x ^ { \beta } ;
$$

that is,by the ten functions $g _ { \alpha \beta }$ of location $\mathscr { P }$ in spacetime. It might then seem that ten functions must be predicted; and, if so, that one would need for the task ten

equations.Not so. Introduce a new set of coordinates $x ^ { \overline { { \mu } } }$ by way of the coordinate transformations

$$
x ^ { \alpha } = x ^ { \alpha } ( x ^ { \overline { { \mu } } } ) ,
$$

and find the same spacetime geometry, with all the same bumps, rils, and waves, described by an entirely new set of metric coefficients $g _ { \overline { { \alpha } } \overline { { \beta } } } ( \mathcal { P } )$

It would transgress the power as wellas the duty of Einstein's “geometrodynamic law" ${ \pmb { G } } = 8 \pi { \pmb { T } }$ if, out of the appropriate data on the “initial-value hypersurface,” it were to provide a way to calculate, on out into the future, values for all ten functions $g _ { \alpha \beta } ( \mathcal { P } )$ .To predict all ten functions would presuppose a choice of the coordinates; and to make a choice among coordinate systems is exactly what the geometrodynamic law cannot and must not have the power to do. That choice resides of necessity in the man who studies the geometry, not in the Nature that makes the geometry. The geometry in and by itself,like an automobile fender in and by itself, is free of coordinates. The coordinates are the work of man.

It follows that the ten components $G _ { \alpha \beta } = 8 \pi T _ { \alpha \beta }$ of the field equation must not determine completely and uniquely all ten components $g _ { \mu \nu }$ of the metric. On the contrary, $G _ { \alpha \beta } = 8 \pi T _ { \alpha \beta }$ must place only six independent constraints on the ten $g _ { \mu \nu } ( \mathcal { P } )$ leaving four arbitrary functions to be adjusted by man's specialization of the four coordinate functions $x ^ { \alpha } ( { \mathcal { P } } )$

$\pmb { G } = 8 \pi \pmb { T }$ must determine only six metric components: the other four are adjustable by changes of.coordinates

How can this be so? How can the ten equations $G _ { \alpha \beta } = 8 \pi T _ { \alpha \beta }$ be in reality only six? Answer: by virtue of the “automatic conservation of the source.” More specifically,the identity $G ^ { \alpha \beta } { } _ { ; \beta } \equiv 0$ guaranees that thetenequations $G _ { \alpha \beta } = 8 \pi T _ { \alpha \beta }$ contain the four"conservationlaws” $T ^ { \alpha \beta } { } _ { ; \beta } = 0$ Thesfourconservationlawsalongwith other equations-govern the evolution of the source. They do not constrain in any way the evolution of the geometry. The geometry is constrained only by the six remaining, independent equations in $G _ { \alpha \beta } = 8 \pi T _ { \alpha \beta }$

When viewed in this way,the “automatic conservation of the source”is not merely a philosophically attractive principle. It is, in fact, an absolute dynamic necessity. Without “automatic conservation of the source,” the ten $G _ { \alpha \beta } = 8 \pi T _ { \alpha \beta }$ would place ten constraints on the ten $g _ { \alpha \beta }$ ，thus fixing the coordinate system as well as the geometry. With “automatic conservation,” the ten $G _ { \alpha \beta } = 8 \pi T _ { \alpha \beta }$ place four constraints (local conservation of energy and momentum) on the source,and six constraints on the ten $g _ { \alpha \beta }$ , leaving four of the $g _ { \alpha \beta }$ to be adjusted by adjustment of the coordinate system.

$\pmb { G } = \pmb { 8 } \pi \pmb { T }$ leaves four   
components of metric free   
because it satisfies four   
identities   
$0 \equiv \pmb { \nabla } \cdot \pmb { G } = 8 \pi \pmb { \nabla } \cdot \pmb { \tau }$   
("automatic conservation of   
source\`\`)

# $\$ 123$ . COSMOLOGICAL CONSTANT

In l915,when Einstein developed his general relativity theory, the permanence of the universe was a fixed item of belief in Western philosophy.“The heavens endure from everlasting to everlasting.”Thus,it disturbed Einstein greatly to discover (Chapter 27) that his geometrodynamic law $\pmb { G } = 8 \pi \pmb { T }$ predicts a nonpermanent universe; a dynamic universe; a universe that originated in a “big-bang” explosion,

Einstein's motivation for introducinga cosmological constant

or will be destroyed eventually by contraction to infinite density, or both. Faced with this contradiction between his theory and the firm philosophical beliefs of the day,Einstein weakened;he modified his theory.

The only conceivable modification that does not alter vastly the structure of the theory is to change the lefthand side of the geometrodynamic law ${ \pmb { G } } = 8 \pi { \pmb { T } } .$ Recall that the lefthand side is frced to be the Einstein tensor, ${ \cal G } _ { \alpha \beta } = { \cal R } _ { \alpha \beta } - { \scriptstyle \frac { 1 } { 2 } } { \cal R } g _ { \alpha \beta } .$ by three assumptions:

(1) $\pmb { G }$ vanishes when spacetime is fat.   
(2) $\pmb { G }$ is constructed from the Riemann curvature tensor and the metric and nothing else.   
(3) $\pmb { G }$ is distinguished from other tensors that can be built from Riemann and $\pmb { \mathscr { g } }$ by the demands (l） that it be linear in Riemann,as befits any natural measure of curvature; (2) that, like $\pmb { \tau } ,$ it be symmetric and of second rank; and (3) that it have an automatically vanishing divergence, $\pmb { \nabla } \cdot \pmb { G } \equiv 0$

Denote a new,modified lefthand side by $" G "$ ，with quotation marks to avoid confusion with the standard Einstein tensor. To abandon ${ \pmb { \bigtriangledown } } \cdot \mathbf { \partial } ^ { * } { \pmb { G } } ^ { * } \equiv 0$ is impossible on dynamic grounds (see $\ S 1 7 . 2 )$ . To change the symmetry or rank of $" G ^ { \prime \prime }$ is impossible on mathematical grounds, since $" G "$ must be equated to $\pmb { \tau } .$ To let $\ " \pmb { G } ^ { \prime \prime }$ be nonlinear in Riemann would vastly complicate the theory. To construct $" G "$ from anything except Riemann and $\pmb { \mathscr { g } }$ would make “ ${ \bf \ddot { \sigma } } _ { \bf \vec { \sigma } }$ no longer a measure of spacetime geometry and would thus violate the spirit of the theory. After much anguish, one concludes that the assumption which one might drop with least damage to the beauty and spirit of the theory is assumption (l), that $\because G ^ { , }$ .vanish when spacetime is flat. But even dropping this assumption is painful: (l） although $" G "$ might still be in Some sense a measure of geometry,it can no longer be a measure of curvature; and (2) flat, empty spacetime will no longer be compatible with the geometrodynamic law ( $\ b \mathscr { G } \neq 0$ in flat, empty space, where $\pmb { \tau } = 0 \mathrm { \hbar }$ ).Nevertheless, these consequences were less painful to Einstein than a dynamic universe.

The only tensor that satisfies conditions (2) and (3) {with (l） abandoned] is the Einstein tensor plus a multiple of the metric:

$$
^ { \ast } G _ { \alpha \beta } { } ^ { , \ast } = R _ { \alpha \beta } - \frac { 1 } { 2 } g _ { \alpha \beta } R + A g _ { \alpha \beta } = G _ { \alpha \beta } + A g _ { \alpha \beta }
$$

Einstein's field equation with the cosmological constant

(exercise l7.1; see also exercise 17.4). Thus was Einstein (l917) led to his modified field equation

$$
{ \pmb { G } } + \varLambda { \pmb { g } } = 8 \pi { \pmb { T } } .
$$

Why Einstein abandoned the cosmological constant

The constant $\pmb { A }$ he called.the “cosmological constant"; it has dimensions $\mathsf { c m } ^ { - 2 }$

The modified field equation, by contrast with the original,admits a static, unchanging universe as one particular solution (see Box 27.5).For this reason, Einstein in l917 was inclined to place his faith in the modified equation. But thirteen years later Hubble discovered the expansion of the universe. No longer was the cosmological constant necessary. Einstein, calling the cosmological constant “the biggest blunder of my life,”abandoned it and returned to his original geometrodynamic law, ${ \pmb { G } } = 8 \pi { \pmb { T } }$ [Einstein (1970)].

A great mistake $\pmb { \varLambda }$ was indeed!-not least because, had Einstein stuck by his original equation, he could have claimed the expansion of the universe as the most triumphant prediction of his theory of gravity.

A mischievous genie,once let out of a bottle, is not easily reconfined. Many workers in cosmology are unwilling to abandon the cosmological constant. They insist that it be abandoned only after cosmological observations reveal it to be negligibly small.As a modern-day motivation for retaining the cosmological constant, one sometimes rewrites the modified field equation in the form

A modern-day motivation for the cosmological constant: vacuum polarization

$$
\begin{array} { r } { \pmb { G } = 8 \pi [ \pmb { T } + \pmb { T } ^ { \mathrm { ( V A C ) } } ] , } \\ { \pmb { T } ^ { \mathrm { ( V A C ) } } \equiv - ( A / 8 \pi ) \pmb { g } } \end{array}
$$

and interprets ${ \pmb T } ^ { ( \nabla \mathbf { A } \mathbf { C } ) }$ as a stress-energy tensor associated with the vacuum. This viewpoint speculates [Zel'dovich (l967)] that the vacuum polarization of quantum field theory endows the vacuum with the nonzero stress-energy tensor (17.12b), which is completely unobservable except by its gravitational effects. Unfortunately, today's quantum field theory is too primitive to allow a calculation of $\pmb { T } ^ { \mathrm { ( v \mathbf { A C } ) } }$ from first principles. (See, however,exercise 17.5.)

The mass-energy density that the cosmological constant attributes to the vacuum is

$$
\rho ^ { ( \mathrm { V A C } ) } = { \cal T } _ { \hat { 0 } \hat { 0 } } ^ { ( \mathrm { V A C } ) } = + { \cal A } / 8 \pi .
$$

f $\varLambda \neq 0$ ,it must at least be so small that $\pmb { \rho } ^ { ( \mathbf { V } \mathbf { A C } ) }$ has negligible gravitational effects $\{ | \rho ^ { \mathrm { ( v A C ) } } | < \rho ^ { \mathrm { ( M A T T E R ) } } \}$ wherever Newton's theory of gravity gives a successful account ofobservations.The systems of lowest density to which one applies Newtonian theory with some (though not great) success are smal clusters of galaxies. Hence, one can place the limit

Observational limit on the cosmological constant

$$
| \rho ^ { \mathrm { ( V A C ) } } | = | A | / 8 \pi \lesssim \rho ^ { \mathrm { ( C L U S T E R ) } } \sim 1 0 ^ { - 2 9 } \mathrm { g / c m } ^ { 3 } \sim 1 0 ^ { - 5 7 } \mathrm { c m } ^ { - 2 }
$$

on the value of the cosmological constant.Evidently,even if $\varLambda \neq 0$ ， $\pmb { \varLambda }$ is so small that it is totally unimportant on the scale of a galaxy or a star or a planet or a man or an atom. Consequently it is reasonable to stick with Einstein's original geometrodynamic law $( \pmb { G } = 8 \pi \pmb { T } ;$ $\varLambda = 0$ ）everywhere，except occasionally when discussing cosmology (Chapters 27-30).

Why one ignores the cosmological constant everywhere except in cosmology

(a) What is the order of magnitude of the influence of the cosmological constant on the celestial mechanics of the solar system if $\varLambda \sim 1 0 ^ { - 5 7 } \ : \mathrm { c m ^ { - 2 } } \ :$

(b) Show that the mass-energy density of the vacuum $\rho ^ { \mathrm { ( V A C ) } } = A / 8 \pi \sim 1 0 ^ { - 2 9 } \ : \mathrm { g / c m ^ { 3 } } ,$ corresponding to the maximum possible value of $\pmb { \varLambda }$ ,agrees in very rough magnitude with

$$
= \frac { m } { ( \hbar / m ) ^ { 3 } } \frac { m ^ { 2 } } { \hbar } = \frac { m ^ { 6 } } { \hbar ^ { 4 } }
$$

[Zel'dovich (l967,1968)]. This numerology is suggestive, but has not led to any believable derivation of a stress-energy tensor for the vacuum.

# $\$ 17.4$ .THE NEWTONIAN LIMIT

Just as quantum mechanics reduces to classical mechanics in the “correspondence limit”of large actions, $I \gg \hbar$ ，so general relativity reduces to Newtonian theory in the “correspondence limit” of weak gravity and low velocities. (On“correspondence limits,”see Box 17.1.) This section elucidates, in some mathematical detail, the correspondence between general relativity and Newtonian theory. It begins with “passive” aspects of gravitation (response of matter to gravity) and then turns to “active” aspects (generation of gravity by matter).

Consider an isolated system-e.g., the solar system-in which Newtonian theory is highly accurate. In order that special relativistic effects not be noticeable,all

# Box 17.1 CORRESPONDENCE PRINCIPLES

# A. General Remarks and Specific Examples

1. As physics develops and expands, its unity is maintained by a network of correspondence principles, through which simpler theories maintain their vitality by links to more sophisticated but more accurate ones.

a.Physical optics,with all the new diffraction and interference phenomena for which it accounted, nevertheless also had to account, and did account, for the old,elementary, geometric optics of mirrors and lenses. Geometric optics is recovered from physical optics in the mathematical "correspondence principle limit”in which the wavelength is made indefinitely small in comparison with all other relevant dimensions of the physical system.

b. Newtonian mechanics is recovered from the mechanics of special relativity in the mathematical “correspondence principle limit”in which all relevant velocities are negligibly small compared to the speed of light.

c. Thermodynamics is recovered from its successor theory,statistical mechanics,in the mathematical “correspondenceprinciple limit” in which so many particles are taken into account that fluctuations in pressure, particle number,and other physical quantities are negligible compared to the average values of these parameters of the system.

d. Classical mechanics is recovered from quantum mechanics in the“correspondence principle limit” in which the quantum numbers of the quantum states in question are so large,or the quantities of action that come into play are so great compared to $\hbar$ that wave and diffraction phenomena make negligible changes in the predictions of standard deterministic classical mechanics.Niels Bohr formulated and took advantage of this correspondence principle even before any proper quantum theory existed.He used it to predict approximate values of atomic energy levels and of intensities of spectral lines. He also expounded it as a guide to all physicists, first in searching for a proper version of the quantum theory,and then in elucidating the content of this theory after it was found.

2.In all these examples and others, the newer, more sophisticated theory is “better” than its predecessor because it gives a good description of a more extended domain of physics,or a more accurate description of the same domain, or both.

3. The correspondence between the newer theory and its predecessor (a） gives one the power to recover the older theory from the newer; (b) can be exhibited by straightforward mathematics; and (c), according to the historical record,often guided the development of the newer theory.

# B. Correspondence Structure of General Relativity

1. Einstein's theory of gravity has as distinct limiting cases (a） special relativity;(b) the“linearized theory of gravity"; (c) Newton's theory of gravity; and (d) the post-Newtonian theory of gravity. Thus,it has a particularly rich correspondence structure.

a. Correspondence with special relativity: General relativity has two distinct kinds of correspondence with special relativity. The first is the limit of vanishing gravitational field everywhere (vanishing curvature)；in this limit one can introduce a global inertial frame, set $g _ { \mu \nu } = \eta _ { \mu \nu }$ ,and recover completely and precisely the theory of special relativity. The second is local rather than global; it is the demand ("correspondence principle"; "equivalence principle") that in a local inertial frame all the laws of physics take on their special relativistic forms. As was seen in Chapter l6,this puts no restrictions on the metric (except that $g _ { \mu \nu } = \eta _ { \mu \nu }$ and $g _ { \mu \nu , \alpha } = 0$ in local inertial frames);but it places severe constraints on the behavior of matter and fields in the presence of gravity.

b. Correspondence with Newtonian theory: In the limit of weak gravitational fields, low velocities, and small pressures, general relativity reduces to Newton's theory of gravity. The correspondence structure is explored mathematically in the text of $\ S 1 7 . 4$

c. Correspondence with post-Newtonian theory: When Newtonian theory is nearly valid, but "first-order relativistic corrections”might be important, one often uses the “post-Newtonian theory of gravity.” Chapter 39 expounds the post-Newtonian theory and its correspondence with both general relativity and Newtonian theory.

d. Correspondence with linearized theory: In the limit of weak gravitational fields, but possibly large velocities and pressures $( v \sim 1$ ， $T _ { j k } \sim T _ { 0 0 } )$ general relativity reduces to the "linearized theory of gravity". This correspondence is explored in Chapter l8.

Conditions which a system must satisfy for Newton's theory of gravity to be accurate

velocities in the system, relative to its center of mass and also relative to the Newtonian coordinates, must be small compared to the speed of light

$$
v \ll 1 .
$$

As a particle fals from the outer region of the system to the inner region, gravity accelerates it to a kinetic energy ${ \bf \tau } _ { 2 } ^ { 1 } m v ^ { 2 } \sim \left| m \mathbf { \hat { \phi } } \right| _ { \operatorname* { m a x } } .$ [Here $\Phi < 0$ is Newton's gravitational potential, so normalized that $\dot { \pmb { \phi } } ( \infty ) = 0 .$ ] The resulting velocity will be small only if

$$
| \phi | \leqslant 1 .
$$

Internal stresses in the system also produce motion-e.g., sound waves. Such waves have characteristic velocities of the order of $| T ^ { i j } / T ^ { 0 0 } | ^ { 1 / 2 }$ -for example, the speed of sound in a perfect fluid is

$$
v = ( d p / d \rho ) ^ { 1 / 2 } \sim ( p / \rho ) ^ { 1 / 2 } \sim | T ^ { i j } / T ^ { 0 0 } | ^ { 1 / 2 } .
$$

In order that these velocities be small compared to the speed of light, all stresses must be smallcompared to the density of mass-nergy

$$
| T ^ { i j } | / T ^ { 0 0 } = | T ^ { i j } | / \rho \ll 1 .
$$

When,and only when conditions (17.15) hold,one can expect Newtonian theory to describe accurately the system being studied. Correspondence of general relativity with Newtonian theory for gravity in a passive role then demands that the geodesic world lines of freely falling particles reduce to the Newtonian world lines

$$
d ^ { 2 } x ^ { i } / d t ^ { 2 } = - \partial \varPhi / \partial x ^ { i } .
$$

Moreover, they must reduce to this form in any relativistic coordinate system where the source and test particles have low velocities $v \not \ll 1$ ,and where coordinate lengths and times agree very nearly with the lengths and times of the Newtonian coordinates--which in turn are proper lengths and times as measured by rods and clocks. Thus,the relevant coordinates (called“Galilean” or “Newtonian” coordinates) are ones in which

$$
g _ { \mu \nu } = \eta _ { \mu \nu } + h _ { \mu \nu } , ~ | h _ { \mu \nu } | \ll 1 , ~ | v ^ { j } | = | d x ^ { j } / d t | \ll 1
$$

(weak gravitational field； nearly inertial coordinates; low velocities). In such a coordinate system, the geodesic world lines of test particles have the form

$$
\begin{array} { r l r } { \frac { d ^ { 2 } x ^ { i } } { d t ^ { 2 } } = \frac { d ^ { 2 } x ^ { i } } { d \tau ^ { 2 } } } & { ( \mathrm { s i n c e ~ } d / d \tau \approx 1 \mathrm { ~ w h e n ~ } | h _ { \rho \rho } | \leqslant 1 \mathrm { ~ a n d ~ } | v | \leqslant 1 ) } \\ { } & { = - { \cal T } _ { \circ \rho } ^ { i } \frac { d x ^ { \alpha } } { d \tau } \frac { d x ^ { \beta } } { d \tau } } & { ( \mathrm { g e o d e s i c ~ e q u a t i o n } ) } \\ { } & { = - { \cal T } _ { \circ \rho } ^ { i } } & { ( \mathrm { s i n c e ~ } d / d \tau \approx 1 \mathrm { ~ a n d ~ } | d x ^ { j } / d \tau | \leqslant 1 ) } \\ { } & { = - { \cal T } _ { \circ \rho } } & { ( \mathrm { s i n c e ~ } g _ { \mu \rho } \approx \eta _ { \rho \rho } ) } \\ { } & { = \frac { 1 } { 2 } h _ { \circ 0 , i } - h _ { 0 , \circ } } & { ( \mathrm { e q u a t i o n ~ f o r ~ } { \cal T } _ { \circ \beta } \mathrm { ~ i n ~ t e r m s ~ o f ~ } g _ { \alpha \beta , \nu } ) } \\ { } & { } & { = \frac { 1 } { 2 } h _ { \circ 0 , i } \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { } & { = - \frac { 1 } { 2 } h _ { \circ 0 , i } \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { } & { = - \frac { 1 } { 2 } h _ { \circ 0 , i } \quad \quad } & { ( \mathrm { a l l ~ v e l o c i t i e s ~ s m a l l ~ c o m p a r e d ~ t o ~ c i n p l i e s ~ t i m e } ) } \\ { } & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { } & { = - \frac { 1 } { 2 } h _ { \circ 0 , i } \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \end{array}
$$

These geodesic world lines do,indeed,reduce to those of Newtonian theory [equation (17.16)] if one makes the identification

$$
\bar { \Gamma ^ { i } } _ { 0 0 } = - \frac { 1 } { 2 } h _ { 0 0 , i } = \varPhi _ { , i } .
$$

Together with the boundary conditions $\phi ( r = \infty ) = 0$ and $h _ { \mu \nu } ( r = \infty ) = 0$ (coordinates Lorentz far from the source),this identification implies $h _ { 0 0 } = - 2 \phi$ ;i.e., $g _ { 0 0 } = - 1 - 2 \Phi$ for nearly Newtonian systems in Newtonian coordinates.

Note that the correspondence tells one the form of $h _ { 0 0 }$ for nearly Newtonian systems, but not the forms of the other components of the metric perturbation. In fact, the other $h _ { \mu \nu }$ could perfectly well be of the same order of magnitude as $h _ { 0 0 } \sim \Phi$ ， without infuencing the world lines of slowly moving particles, because they always enter the geodesic equation multiplied by the small numbers $v$ or $v ^ { 2 }$ ,or differentiated by $t$ rather than by $x ^ { i }$ . The forms of the other $h _ { \mu \nu }$ and their small corrections to the Newtonian motion will be explored in Chapters 18,39,and 40.

Einstein gravity reduces to Newton gravity only if,in Newtonian coordinates, $g _ { 0 0 } = - 1 - 2 \Phi$

The relation $g _ { \scriptscriptstyle 0 0 } = - l - 2 \Phi$ is the mathematical embodiment of the correspondence between general relativity theory and Newtonian theory for passve aspects of gravity. Together with the “validity conditions”(17.15,17.17), it is a foundation from which one can derive allother aspects of the correspondence for “passive gravity," including the relation +

$$
R _ { ~ 0 j 0 } ^ { i } = \hat { \sigma } ^ { 2 } \varPhi / \hat { \sigma } x ^ { i } \hat { \sigma } x ^ { j }
$$

(exercise l7.6). Alternatively. all other aspects of this correspondence can be derived bydirect comparison of Newton's predictions with Einstein's.For example, to derive equation(l7.20), examine the relative acceleration of two test particles,one at xi + i and the other at $x ^ { i }$ . According to Newton

$$
\begin{array} { r l r } { \left. { \frac { d ^ { 2 } \xi ^ { i } } { d t ^ { 2 } } = \frac { d ^ { 2 } ( x ^ { i } + \xi ^ { i } ) } { d t ^ { 2 } } - \frac { d ^ { 2 } x ^ { i } } { d t ^ { 2 } } } } \\ & { } & { = \left. - \frac { \partial \phi } { \partial x ^ { i } } \right| _ { \mathrm { a t } x ^ { j } + \xi ^ { j } } + \frac { \partial \phi } { \partial x ^ { i } } \right| _ { \mathrm { a t } x ^ { j } } = \frac { - \hat { \sigma } ^ { 2 } \phi } { \hat { \sigma } x ^ { i } \hat { \sigma } x ^ { j } } \xi ^ { j } . } \end{array}
$$

For comparison, Einstein predicts (equation of geodesic deviation)

$$
\frac { D ^ { 2 } \xi ^ { i } } { d \tau ^ { 2 } } = \frac { d ^ { 2 } \xi ^ { \mathrm { i } } } { d t ^ { 2 } } = - R ^ { i } { } _ { 0 { \mathrm { j 0 } } } \xi ^ { \mathrm { j } } .
$$

Direct comparison gives relation (17.20).

The correspondence between Einstein theory and Newton theory for all"passive' aspects of gravity

Turn now from correspondence for passive aspects of gravity to correspondence for active aspects. According to Einstein, mass generates gravity (spacetime curvature) by the geometrodynamic law $\pmb { G } = 8 \pi \pmb { T } .$ Apply this law to a nearly Newtonian system,and by the chain of reasoning that preceeds equation (l7.8） derive the relation

$$
R _ { 0 0 } = 4 \pi \rho .
$$

The Newtonian limit of the Einstein field equation is $\pmb { \nabla } ^ { 2 } \pmb { \phi } = 4 \pi \rho$

Combine with the contraction of (17.20),

$$
\begin{array} { r } { R _ { 0 0 } = R _ { \ 0 i 0 } ^ { i } + R _ { \ 0 0 0 } ^ { 0 } = \partial ^ { 2 } \phi / \partial x ^ { i } \partial x ^ { i } = \nabla ^ { 2 } \phi , } \\ { \uparrow . . \qquad \quad \uparrow . } \\ { 0 \qquad \quad \mathrm { ~ } } \end{array}
$$

and thereby obtain Newton's equation for the generation of gravity by mass

$$
\nabla ^ { 2 } \Phi = 4 \pi \rho .
$$

Thus,Einstein's field equation reduces to Newton's field equation in the Newtonian limit.

The correspondence between Newton and Einstein, although clear and straightforward as outlined above, is even more clear and straightforward when Newton's theory of gravity is rewritten in Einstein's language of curved spacetime (Chapter 12; exercise 17.7).

# EXERCISES

# ExerCise 17.6. RAMIFICATIONS OF CORRESPONDENCE FOR GRAVITY IN A PASSIVE ROLE

From the correspondence relation $g _ { \scriptscriptstyle 0 0 } = - 1 - 2 \varPhi$ ,and from conditions (17.15) and (17.17) for Newtonian physics,derive the correspondence relations

$$
{ T ^ { \ i } } _ { _ { 0 0 } } = \partial \phi / \partial x ^ { \ i } , { R ^ { \ i } } _ { _ { 0 j 0 } } = \partial ^ { 2 } \phi / \partial x ^ { \ i } \partial x ^ { j } .
$$

# Exercise 17.7. CORRESPONDENCE IN THE LANGUAGE OF CURVED SPACETIME [Track 2]

Exhibit the correspondence between the Einstein theory and Cartan's curved-spacetime formulation of Newtonian theory (Chapter 12).

# $\$ 17.5$ :AXIOMATIZE EINSTEIN'S THEORY?

Find the most compact and reasonable axiomatic structure one can for general relativity? Then from the axioms derive Einstein's field equation,

$$
{ \pmb { G } } = 8 \pi { \pmb { T } } \ ?
$$

That approach would follow tradition. However, it may be out of date today. More than half a century has gone by since November 25,1915. For all that time the equation has stood unchanged,if one ignores Einstein's temporary “aberration”of adding the cosmological constant. In contrast the derivations have evolved and become more numerous and more varied.In the beginning axioms told what equation is acceptable. By now the equation tells what axioms are acceptable. Box 17.2 sketches a variety of sets of axioms,and the resulting derivations of Einstein's equation.

There are many ways (Box 17.2) to derive the Einstein field equation

(continued on page 429)

# Box 17.2 SIX ROUTES TO EINSTEIN'S GEOMETRODYNAMIC LAW OF THE EQUALITY OF CURVATURE AND ENERGY DENSITY ("'EINSTEIN'S FIELD EQUATION")

[Recommended to the attention of Track-l readers are only route l (automatic conservation of the source, plus correspondence with Newtonian theory） and route 2 (Hilbert's variational principle)；and even Track-2 readers are advised to finish the rest of this chapter before they study route 3 (physics on a spacelike slice), route 4 (going from superspace to Einstein's equation),route 5 (field of spin 2 in an “unobservable flat spacetime” background),and route 6 (gravitation as an elasticity of space that arises from particle physics).]

1. Model geometrodynamics after electrodynamics and treat “automatic conservation of the source” and correspondence with the Newtonian theory of gravity as the central considerations.

a.Particle responds in electrodynamics tofield; ingeneralrelativity,togeometry.

b. The potential for the electromagnetic field is the 4-vector $\pmb { A }$ (components $A _ { \mu . }$ ） The potential for the geometry is the metric tensor $\pmb { g }$ (components $g _ { \mu \nu } )$

c. The electromagnetic potential satisfies a wave equation with source term (4-current) on the right,

$$
\left( \frac { \widehat { \circ } A _ { \nu } } { \widehat { \sigma } x ^ { \mu } } - \frac { \widehat { \circ } A _ { \mu } } { \widehat { \circ } x ^ { \nu } } \right) ^ { ; \nu } = 4 \pi j _ { \mu } ,
$$

so constructed that conservation of the source, $j _ { \mu } ^ { \mu } { } ^ { ; \mu } = 0$ ,is automatic (consequence of an identity fulfilled by the lefthand side). By analogy, the geometrodynamic potential must also satisfy a wave equation with source term (stressenergy tensor) on the right,

$$
G _ { \mu \nu } = 8 \pi T _ { \mu \nu } ,
$$

so constructed that conservation of the source, $T _ { \mu \nu } { } ^ { ; \nu } = 0$ (Chapter 16） is “automatic.” This conservation is automatic here because the lefthand side of the equation is a tensor (the Einstein tensor; see $\mathtt { B o x } 8 . 6$ or Chapter 15), built from the metric components and their second derivatives,that fulfills the identity $G _ { \mu \nu } { } ^ { ; \nu } \equiv 0$

d. No other tensor which (l） is linear in the second derivatives of the metric components,(2) is free of higher derivatives,and (3) vanishes in flat spacetime, satisfies such an identity.

e. The constant of proportionality $( 8 \pi )$ is fixed by the choice of units [here geometric; see Box l.8] and by the requirement ("correspondence with Newtonian theory"） that a test particle shall oscillate back and forth through a collection of matter of density $\pmb \rho$ ，or revolve in circular orbit around that collection of matter, at a circular frequency given by $\omega ^ { 2 } = ( 4 \pi / 3 ) \rho$ (Figure

# Box 17.2 (continued)

1.12). The foregoing oversimplifies, and omits Einstein's temporary false-turns, but otherwise summarizes the reasoning he pursued in arriving at his field equation. This reasoning is spelled out in more detail in the text of Chapter 17.

2. Take variational principle as central.

a. Construct out of the metric components the only scalar that exists that (l) is linear in the second derivatives of the metric tensor,(2) contains no higher derivatives,and (3) vanishes in flat spacetime: namely, the Riemann scalar curvature invariant, $R .$

b. Construct the invariant integral,

$$
I = \frac { 1 } { 1 6 \pi } \int _ { \itOmega } R ( - g ) ^ { 1 / 2 } d ^ { 4 } x .
$$

c. Make small variations, $\delta g ^ { \mu \nu }$ ,in the metric coefficients $g ^ { \mu \nu }$ in the interior of the four-dimensional region $\pmb { \mathcal { Q } }$ ，and find that this integral changes by the amount

$$
\delta I = \frac { 1 } { 1 6 \pi } \int _ { \it Q } G _ { \mu \nu } \delta g ^ { \mu \nu } ( - g ) ^ { 1 / 2 } d ^ { 4 } x .
$$

d. Demand that $I$ should be an extremum with respect to the choice of geometry in the region interior to $\pmb { \mathcal { Q } }$ $\delta I = 0$ for arbitrary $\delta g ^ { \mu \nu }$ ； "principle of extremal action").

e. Thus arrive at the Einstein field equation for empty space,

$$
G _ { \mu \nu } = 0 .
$$

f. The continuation of the reasoning leads to the identity

$$
G _ { \mu \nu } { } ^ { ; \nu } = 0 .
$$

Chapter 21,on the variational principle, gives more detail and takes up the additional term that appears on the righthand side of(5) when matter or fields or both are present.

g. This approach goes back to David Hilbert (l915). No route to the field equations is quicker.Moreover, it connects immediately (see the following section here,2') with the quantum principle of the “democracy of all histories” [Feynman (l942); Feynman and Hibbs (l965). The variational principle is speled out in more detail in Chapter 21.

2'.An aside on the meaning of the classical action integral for the real world of quantum physics.

a.A“history of geometry,” $H ,$ is a spacetime, that is to say,a four-dimensional manifold with four-dimensional $- + + +$ Riemann metric that (l) reduces on one spacelike hypersurface ("hypersurface of simultaneity"） to a specified "initial value 3-geometry,” $\pmb { A } ,$ ,with positive definite metric and (2) reduces on another spacelike hypersurface to a specified “final value 3-geometry,” $\pmb { B }$ ,also with positive definite metric.

b. The classical variational principle of Hilbert, as reformulated by Arnowitt, Deser,and Misner, provides a prescription for the dynamical path length, $I _ { H } ,$ of any conceivable history $H ,$ classically allowed or not, that connects $\pmb { A }$ and $\pmb { B }$ (see Chapter 21 for a fuller statement for what can and must be specified on the initial hypersurface of simultaneity,and on the final one,and for alternative choices of the integrand in the action principle).

c. Classical physics says that a history $\pmb { H }$ is allowed only if it extremizes the dynamic path length $I$ as compared to all nearby histories. Quantum physics says that all histories occur with equal probability amplitude, in the following sense.The probability amplitude for “the dynamic geometry of space to transit from $\pmb { A }$ to $B ^ { \prime \prime }$ by way of the history $\pmb { H }$ with action integral ${ \cal I } _ { H } ,$ and by way of histories that lie within a specified infinitesimal range, ${ \mathcal { O H } } ,$ of the history $H ,$ is given by the expression

$$
\left( \begin{array} { l } { \mathrm { p r o b a b i l i t y ~ a m p l i t u d e } } \\ { \mathrm { t o ~ t r a n s i t ~ f r o m ~ } A \mathrm { ~ t o } } \\ { B \mathrm { ~ b y ~ w a y ~ o f ~ h i s t o r y ~ } H } \\ { \mathrm { a n d ~ h i s t o r i e s ~ l y i n g } } \\ { \mathrm { w i t h i n ~ t h e ~ r a n g e ~ } \mathcal { D } H } \\ { \mathrm { a b o u t ~ } H } \end{array} \right) \sim \exp { ( i I _ { H } / \hbar ) } N \mathcal { O } { H } .
$$

Here the normalization factor, $N ,$ is the same for all conceivable histories $H ,$ allowed or not, that lead from $\pmb { A }$ to $\pmb { B }$ ("principle of democracy of histories"). The quantum of angular momentum, $\hbar = h / 2 \pi$ ,expressed in geometric units, has the value

The rest of this chapter is Track 2. No previous track-2 material is needed as preparation for it, nor is it necessary preparation for any later chapter, but it will be helpful in Chapter21 (initialvalue equations and variational principle) and in Chapter 39 (other theories of gravity).

$$
\hbar = \hbar _ { \mathrm { c o n v } } G / c ^ { 3 } = ( L ^ { * } ) ^ { 2 } ,
$$

where $L ^ { * }$ is the Planck length, $L ^ { * } = 1 . 6 \times 1 0 ^ { - 3 3 } \mathrm { c m } .$

d. The classically allowed history receives “preference without preference.” That history, and histories $\pmb { H }$ that differ from it so little that $\delta I = I _ { H } - I _ { c l a s s }$ is only of the order $\hbar$ and less, give contributions to the probability amplitude that interfere constructively. In contrast, destructive interference effectively wipes out the contribution (to the probability amplitude for a transition) that comes from histories that differ more from the classically allowed history.Thus there are quantum fluctuations in the geometry, but they are fluctuations of limited magnitude. The smallness of $\hbar$ ensures that the scale of these fluctuations is unnoticeable at everyday distances (see the further discussion in Chapters 43 and 44). In this sense classical geometrodynamics is a good approximation to the geometrodynamics of the real world of quantum physics.

3. “Physics on a spacelike slice or hypersurface of simultaneity,” again with electromagnetism as the model.

a. Say over and over “lines of magnetic force never end’and come out with half of Maxwell's equations. Say over and over “lines of electric force end only on charge” and arrive at the other half of Maxwel's equations. Similarly, say over and over

$$
{ \left( \begin{array} { l } { \mathrm { i n t r i n s i c } } \\ { \mathrm { c u r v a t u r e } } \\ { \mathrm { s c a l a r } } \end{array} \right) } + { \left( \begin{array} { l } { \mathrm { e x t r i n s i c } } \\ { \mathrm { c u r v a t u r e } } \\ { \mathrm { s c a l a r } } \end{array} \right) } = 1 6 \pi \left( { \begin{array} { l } { \mathrm { l o c a l ~ d e n s i t y } } \\ { \mathrm { o f ~ m a s s - } } \\ { \mathrm { e n e r g y } } \end{array} } \right)
$$

and end up with all ten components of Einstein's equation. To “say over and over" is an abbreviation for demanding that the stated principles hold on every spacelike slice through every event of spacetime.

b. Spell out explicitly this “spacelike-slice formulation” of the equations of Maxwell and Einstein. Consider an arbitrary point of spacetime, $\mathcal { P }$ ("event"), and an arbitrary “simultaneity” $s$ through $\mathcal { P }$ (hypersurface of simultaneity; spacelike slice through spacetime). Magnetic lines of force run about throughout $s$ ,but nowhere is even a single one of them permitted to end. Recall (83.4) that the demand “lines of magnetic force never end,” when imposed on all reference frames at $\mathcal { P }$ (for all choices of the “simultaneity" $s$ )， guarantees not only $\pmb { \nabla } \pmb { \cdot } \pmb { B } = 0$ but also $\pmb { \nabla } \times \pmb { E } + \partial \pmb { B } / \partial t = 0$ Similarly $( \ S 3 . 4 )$ the demand that “electric lines of force never end except on electric charge,” $\pmb { \nabla } \cdot \pmb { E } = 4 \pi J ^ { 0 }$ ， when imposed on all “simultaneities” through $\mathcal { P }$ ， guarantees the remaining Maxwell equation $\pmb { \nabla } \times \pmb { B } = \partial \pmb { E } / \partial t + 4 \pi \pmb { J } .$

c. Each simultaneity $s$ through $\mathcal { P }$ has its own slope and curvature. The possibility of different slopes (different local Lorentz frames at $\mathcal { P }$ ）is essential for deriving all of Maxwel's equations from the requirements of conservation of flux. Relevant though the slope thus is, the curvature of the hypersurface $s$ never matters for the analysis of electromagnetism. It does matter, however, for any analysis of gravitation modeled on the foregoing treatment of electromagnetism.

![](images/a88aed4dbd75aae4b67888ac23e381e725564f0dfd2ff1d4179ad10a86fb0611.jpg)

“Simultaneity” S (spacelike hypersurface or “slice through spacetime") that cuts through event $\mathcal { P }$ The “simultaneity”may be considered to be defined by a set of “observers” $\mathsf { a } , \mathsf { b } , \mathsf { c } ,$ ....Their world lines cross the simultaneity orthogonally, and their clocks all read the same proper time at the instant of crossing. Another simultaneity through $\mathcal { P }$ may have at $\mathcal { P }$ a different curvature or a different slope or both; and it is defined by a different band of observers,with other wrist watches.

d.“Mass-energy curves space” is the central principle of gravitation. To spell out this principle requires one to examine in succession the terms “space” and “curvature of space” and “density of mass-energy in a given region of space.” “Space” means spacelike hypersurface; or, more specifically, a hypersurface of simultaneity $s$ that includes the point $\mathcal { P }$ where the physics is under examination.

e. Denote by $\pmb { u }$ the 4-vector normal to $s$ at $\mathcal { P }$ . Then the density of mass-energy in the spacelike hypersurface $\mathcal { S }$ at $\mathcal { P }$ is

$$
\rho = u ^ { \alpha } T _ { \alpha \beta } u ^ { \beta } ,
$$

in accordance with the definition of the stress-energy tensor given in Chapter 5.

f. This density is a single number,dependent on the inclination of the slice one cuts through spacetime, but independent of how curved one cuts this slice. If it is to be equated to “curvature of space,” that curvature must also be independent of how curved one cuts the slice.

g. Conclude that the geometric quantity,“curvature of space,” must (l) be a single number (a scalar) that (2) depends on the inclination ${ \pmb u }$ of the cut one makes through spacetime at $\mathcal { P }$ in constructing the hypersurface $s$ ,but (3） must be unaffected by how one curves his cut. The demand made here appears paradoxical. One seems to be asking for a measure of curvature that is independent of curvature!

h.A closer look discloses that three distinct ideas come into consideration here. One is the scalar curvature invariant $^ { ( 3 ) } R$ of the 3-geometry intrinsic to the hypersurface $s$ at $\mathcal { P }$ : “intrinsic” in the sense that it is defined by,and depends exclusively on,measurements of distance made within the hypersurface.The second is the “extrinsic curvature”of this 3-geometry relative to the 4-geometry of the enveloping spacetime ("how curved one cuts his slice"; see Box 14.1 for more on the distinction between extrinsic and intrinsic curvature). The third is the curvature of the four-dimensional spacetime itself, “normal to u,”in some sense yet to be more closely defined. This is the quantity that is independent of how curved one cuts his slice. It is the quantity that is to be identified,up to a factor that depends on the choice of units,with the density of mass-energy.

# Box 17.2 (continued)

i. These three quantities are related in the folowing way:

/a correction term that (a) depends only on the “extrinsic curvature” $K _ { \alpha \beta }$ (Box 14.l and Chapter 21) of the hypersurface relative to   
/scalar curvature invariant,   
(3 R, of the 3-geometry the four-dimensional geometry in which it is imbedded,and   
intrinsic to the spacelike + (b) is so calculated (a   
hypersurface S, a quantity   
dependent onho curved lation)termimths correction term and $^ { ( 3 ) } R$ is independent of “how curved one cuts his slice,” and (c) has the precise value $\big \langle \mathrm { T r } K \big \rangle ^ { 2 } - \mathrm { T r } K ^ { 2 } \equiv ( K _ { \alpha } ^ { \alpha } ) ^ { 2 } - K _ { \alpha \beta } K ^ { \alpha \beta } \big \Big \rangle$ /a measure of the curvature of spacetime that depends /a scalar quantity that on the 4-gemetry of (a) is completely defined the spacetime and on by what has just been the inclination $\pmb { u }$ of the said and (b) can therespacelike slice S cut fore be calculated in all through spacetime, but is completeness by standard independent, by construc- differential geometry tion, of “how curved one (details in Chapter 21) cuts the slice” a quantity interpreted in Track 2, Chapter 15,as the $\int 2 u ^ { \alpha } G _ { \alpha \beta } u ^ { \beta }$ where $G _ { \alpha \beta }$ is "moment of rotation” assothe Einstein curvature =2 ciated with a unit element tensor of equation 8.49 of 3-volume located at $\mathcal { P }$ and Box 8.6 in the hypersurface orthogonal to u (10)

j.Conclude that the central principle,“mass-energy curves space,”translates to the formula

$$
{ } ^ { ( 3 ) } R + ( \mathrm { T r } K ) ^ { 2 } - \mathrm { T r } K ^ { 2 } = 1 6 \pi \rho ,
$$

or, in shorthand form,

$$
\binom { \mathrm { m o m e n t ~ o f } } { \mathrm { r o t a t i o n } } = \binom { \mathrm { i n t r i n s i c } } { \mathrm { c u r v a t u r e } } + \binom { \mathrm { e x t r i n s i c } } { \mathrm { c u r v a t u r e } } = \binom { \mathrm { d e n s i t y ~ o f } } { \mathrm { m a s s - e n e r g y } } ,
$$

valid for every spacelike slice through spacetime at any arbitrary point $\mathcal { P }$ $\mathbf { k } .$ All of Einstein's geometrodynamics is contained in this statement as truly as all of Maxwell's electrodynamics is contained in the statement that the number of lines of force that end in an element of volume is equal to $4 \pi$ times the amount of charge in that element of volume. The factor $1 6 \pi$ is appropriate for the geometric system of units in use in this book (density $\pmb \rho$ in $\mathsf { c m } ^ { - 2 }$ given by $G / c ^ { 2 } = 0 . 7 4 2 \times 1 0 ^ { - 2 8 } { \mathrm { c m / g } }$ multiplied by the density $\pmb { \rho } _ { \mathtt { c o n v } }$ expressed in the conventional units of $\mathsf { g } / \mathsf { c m } ^ { 3 } ,$ .

1. Reexpress the principle that “mass-energy curves space” in the form

$$
2 u ^ { \alpha } G _ { \alpha \beta } u ^ { \beta } = 1 6 \pi u ^ { \alpha } T _ { \alpha \beta } u ^ { \beta } .
$$

Demand that this equation should hold for every simultaneity that cuts through $\mathcal { P }$ ，whatever its“inclination” ${ \pmb u }$

m. Conclude that the coeffcients on the two sides of (l3) must agree; thus,

$$
G _ { \alpha \beta } = 8 \pi T _ { \alpha \beta } ,
$$

Einstein's equation in the language of components; or, in the language of abstract geometric quantities,

$$
{ \pmb { G } } = 8 \pi { \pmb { T } } .
$$

4. Going from superspace to Einstein's equation rather than from Einstein's equation to superspace.

a. A fourth route to Einstein's equation starts with the advanced view of geometrodynamics that is spelled out in Chapter 43.One notes there that the dynamics of geometry unfolds in superspace. Superspace has an infinite number of dimensions. Any one point in superspace describes a complete 3-geometry, $( 3 ) g$ ， with all its bumps and curvatures. The dynamics of geometry leads from point to point in superspace.

b.Like the dynamics of a particle, the dynamics of geometry lends itself to distinct but equivalent mathematical formulations, associated with the names of Lagrange, of Hamilton,and of Hamilton and Jacobi. Of these the most convenient for the present analysis is the last $( ^ { 6 6 } \mathrm { H - J ^ { 3 } } )$

c. In the problem of one particle moving in one dimension under the influence of a potential $V ( x )$ ，the H-J equation reads

It has the solution

$$
S _ { E } ( x , t ) = - E t + \int ^ { x } [ 2 m ( E - V ) ] ^ { 1 / 2 } d x .
$$

Out of this solution one reads the motion by applying the “condition of constructive interference,”

$$
\frac { \partial S _ { E } ( x , t ) } { \partial E } = 0
$$

(one equation connecting the two quantities $x$ and $t$ ；for more on the condition of constructive interference and the H-J method in general, see Boxes 25.3 and 25.4).

d. In the corresponding equation for the dynamics of geometry,one deals with a function $S = S ( ^ { ( 3 ) } \mathfrak { s } )$ of the 3-geometry. It depends on the 3-geometry itself, and not on the vagaries of one's choice of coordinates or on the corresponding vagaries in the metric coeffcients of the 3-geometry,

$$
d s ^ { 2 } = { } ^ { ( 3 ) } g _ { m n } d x ^ { m } d x ^ { n }
$$

(3 to indicate 3-geometryomited hereafter for simplicity).This function obeys the H-J equation [the analog of (l6)]

$$
- ( 1 6 \pi ) ^ { 2 } \frac { 1 } { 2 g } ( g _ { i m } g _ { j n } + g _ { i n } g _ { j m } - g _ { i j } g _ { m n } ) \frac { \delta S } { \delta g _ { i j } } \frac { \delta S } { \delta g _ { m n } } + ^ { ( 3 ) } R = 1 6 \pi \rho .
$$

e. Out of this equation for the dynamics of geometry in superspace one can deduce the Einstein field equation by reasoning similar to that employed in going from (17) to (18) (Gerlach 1969).

f. It would appear that one must break new ground,and establish new foundations, if one is to find out how to regard the “Einstein-Hamilton-Jacobi equation"(2O)as more basic than the Einstein field equation that one derives from it. [Since done,by Hojman, Kuchar, and Teitelboim (l973 preprint).]

5.Einstein's geometrodynamics viewed as the standard field theory for a field of spin 2 in an “unobservable flat spacetime” background.

a. This approach to Einstein's field equation has a long history,references to which will be found in $\ S 7 . 1$ and $\ S 1 8 . 1$ . (Further discussion of this approach will be found in those two sections and in Box 7.1,exercise 7.3,and Box 18.1). b. The following summary is quoted from Deser (l970): “We wish to give a simple physical derivation of the nonlinearity...，using a now familiar argument :.. leading from the linear,massless,spin-2 field to the full Einstein equations....

c. “The Einstein equations may be derived nongeometrically by noting that the free, massless, spin-2 field equations,

$$
\begin{array} { r l } & { R ^ { L } { } _ { \mu \nu } ( \phi ) - \displaystyle \frac 1 2 R ^ { L } { } _ { \alpha \alpha } ( \phi ) \eta _ { \mu \nu } \equiv G ^ { L } { } _ { \mu \nu } ( \phi ) \equiv [ ( \eta _ { \mu \alpha } \eta _ { \nu \beta } - \eta _ { \mu \nu } \eta _ { \alpha \beta } ) \bigtriangledown } \\ & { \qquad + \ \eta _ { \mu \nu } \partial _ { \alpha } \partial _ { \beta } + \eta _ { \alpha \beta } \partial _ { \mu } \partial _ { \nu } - \eta _ { \mu \alpha } \partial _ { \nu } \partial _ { \beta } - \eta _ { \nu \beta } \partial _ { \mu } \partial _ { \alpha } ] \phi _ { \alpha \beta } = 0 , } \end{array}
$$

whose source is the matter stress-tensor $T _ { \mu \nu }$ , must actually be coupled to the total stress-tensor,including that of the $\phi$ -field itself.That is, while the free-field equations (21) are of course quite consistent as they stand,[they are not] when there is a dynamic system's $T _ { \mu \nu }$ as a source. For then the left side,which is identically divergenceless, is inconsistent with the right, since the coupling implies that $T ^ { \mu \nu } { } _ { , \nu }$ , as computed from the mater equations of motion, is no longer conserved.

d.“To remedy this [violation of the principle of conservation of momentum and energyl, the stress tensor ${ ^ { ( 2 ) } \theta } _ { \mu \nu }$ arising from the quadratic Lagrangian $^ { ( 2 ) } L$ responsible for equation (21) is then inserted on the right.

e.“But the Lagrangian $^ { ( 3 ) } L$ leading to these modified equations is then cubic, and itself contributes a cubic ${ ^ { ( 3 ) } \theta } _ { \mu \nu }$

f. “This series continues indefinitely,and sums (if properly derived!) to the full nonlinear Einstein equations, $G _ { \mu \nu }$ ([calculated from] $\eta _ { \alpha \beta } + \phi _ { \alpha \beta } ) = - \kappa T _ { \mu \nu }$ $[ + 8 \pi T _ { \mu \nu }$ in the geometric units and sign conventions of this book], which are an infinite series in the deviation $\phi _ { \mu \nu }$ of the metric $g _ { \mu \nu }$ from its Minkowskian value $\eta _ { \mu \nu }$

g. Once the iteration is begun (whether or not a $T _ { \mu \nu }$ is actually present), it must be continued to all orders, since conservation only holds for the full series $\sum _ { n = 2 } ^ { \infty } \ O ^ { ( n ) } \theta _ { \mu \nu }$ Te

form (21),or it must be an infinite series.”

h. For details, see Deser (l97O); the paper goes on (l) to take advantage of a well-chosen formalism (2) to rearrange the calculation,and thus (3) to “derive the full Einstein equations,on the basis of the same self-coupling requirement, but with the advantages that the full theory emerges in closed form with just one added (cubic) term,rather than as an infinite series.”

i. Deser summarizes the analysis at the end thus:“Consistency has therefore led us to universal coupling, which implies the equivalence principle. It is at this point that the geometric interpretation of general relativity arises, since all matter now moves in an effective Riemann space of metric ${ \mathfrak { g } } ^ { \mu \nu } \equiv \eta ^ { \mu \nu } + h ^ { \mu \nu }$ ...[The] initial flat ‘background’ space is no longer observable.” In other words, this approach to Einstein's field equation can be summarized as “curvature without curvature” or-equally well-as “flat spacetime without flat spacetime"!

6. Sakharov's view of gravitation as an elasticity of space that arises from particle physics.

a.The resistance of a homogeneous isotropic solid to deformation is described by two elastic constants, Young's modulus and Poisson's ratio.

b. The resistance of space to deformation is described by one elastic constant, the Newtonian constant of gravity. It makes its appearance in the action principle of Hilbert

$$
\begin{array} { r l } & { I = \frac { 1 } { 1 6 \pi G } \displaystyle \int { } ^ { ( 4 ) } R ( - g ) ^ { 1 / 2 } d ^ { 4 } x } \\ & { \qquad + \displaystyle \int { ( L _ { \mathrm { m a t t e r } } + L _ { \mathrm { f i e l d s } } ) ( - g ) ^ { 1 / 2 } d ^ { 4 } x } = \mathrm { e x t r e m u m } . } \end{array}
$$

c. According to the historical records, it was first learned how many elastic constants it takes to describe a solid from microscopic molecular models of matter (Newton,Laplace, Navier, Cauchy,Poisson, Voigt, Kelvin, Born), not from macroscopic considerations of symmetry and invariance. Thus,count the energy stored up in molecular bonds that are deformed from natural length or natural angle or both.Arrive at an expression for the energy of deformation per unit volume of the elastic material of the form

$$
e = A ( \operatorname { T r } s ) ^ { 2 } + B \operatorname { T r } ( s ^ { 2 } ) .
$$

Here the strain tensor

$$
s _ { m n } = \frac { 1 } { 2 } \biggl ( \frac { \partial \xi _ { m } } { \partial x ^ { n } } + \frac { \partial \xi _ { n } } { \partial x ^ { m } } \biggr )
$$

measures the strain produced in the elastic medium by motion of the typical point that was at the location $x ^ { m }$ to the location $x ^ { m } + \xi ^ { m } ( x )$ .The constants $\pmb { A }$ and $\pmb { B }$ are derived out of microscopic physics. They fix the values of the two elastic constants of the macroscopic theory of elasticity.

d. Andrei Sakharov (l967) (the Andrei Sakharov) has proposed a similar microscopic foundation for gravitation or,as he calls it, the “metric elasticity of space.”He identifies the action term of Einstein's geometrodynamics [the first term in (22)] “with the change in the action of quantum fluctuations of the vacuum [associated with the physics of particles and fields and brought about] when space is curved."

e. Sakharov notes that present-day quantum field theory“gets rid by a renormalization process” of an energy density in the vacuum that would formally be infinite if not removed by this renormalization. Thus, in the standard analysis of the degrees of freedom of the electromagnetic field in flat space, one counts the number of modes of vibration per unit volume in the range of circular wave numbers from $k$ to $k + d k$ as $( 2 \cdot 4 \pi / 8 \pi ^ { 3 } ) k ^ { 2 } d k$ Each mode of oscillation, even at the absolute zero of temperature, has an absolute irreducible minimum of"zero-point energy of oscillation,” ${ \scriptstyle { \frac { 1 } { 2 } } } h \nu = { \frac { 1 } { 2 } } \hbar c k$ [the fluctuating electric field associated with which is among the most firmly established of all physical effects. It acts on the electron in the hydrogen atom in supplement to the electric field caused by the proton alone,and thereby produces most of the famous Lamb-Retherford shift in the energy levels of the hydrogen atom,as made especially clear by Welton (l948) and Dyson (l954)). The totalized density of zero-point energy of the electromagnetic field per unit volume of spacetime (units: $\mathsf { c m } ^ { 4 } ,$ formally diverges as

$$
( \hbar / 2 \pi ^ { 2 } ) \int _ { 0 } ^ { \infty } k ^ { 3 } d k .
$$

Equally formally this divergence is “removed”by “renormalization”[for more on renormalization see, for example, Hepp (1969)].

f. Similar divergences appear when one counts up formally the energy associated with other fields and with vacuum fluctuations in number of pairs of electrons, $\mu$ -mesons, and other particles in the limit of quantum energies large in comparison with the rest mass of any of these particles. Again these divergences in formal calculations are “removed by renormalization.”

g. Removed by renormalization is a contribution not only to the energy density, and therefore to the stress-energy tensor,but also to the total Lagrange function $\mathcal { L }$ of the variational principle for al these fields and particles,

$$
I = \int { \mathcal { E } } d ^ { 4 } x = { \mathrm { e x t r e m u m } } .
$$

h. Curving spacetime alters all these energies, Sakharov points out, extending an argument of Zel'dovich (1967). Therefore the process of “renormalization" or “subtraction”no longer gives zero. Instead, the contribution of zero-point energies to the Lagrangian, expanded as a power series in powers of the curvature, with numerical coefficients $A , B , \ldots$ of the order of magnitude of unity,takes a form simplified by Ruzmaikina and Ruzmaikin (l969) to the following:

$$
\begin{array} { l } { { \displaystyle { \mathcal E } ( R ) = A \hbar \int k ^ { 3 } d k + B \hbar ^ { ( 4 ) } R \int k d k } } \\ { { \displaystyle ~ + ~ \hbar [ C ( ^ { ( 4 ) } R ) ^ { 2 } + D R ^ { \alpha \beta } R _ { \alpha \beta } ] \int k ^ { - 1 } d k } } \\ { { \displaystyle ~ + ~ ( \mathrm { { h i g h e r - o r d e r ~ t e r m s } } ) . } } \end{array}
$$

[For the alteration in the number of standing waves per unit frequency in a curved manifold, see also Berger (l966), Sakharov (l967),Hill in De Witt (1967c),Polievktov-Nikoladze (l969),and Berger, Gauduchon,and Mazet (1971).]

i. Renormalization physics argues that the first term in (27) is to be dropped. The second term,Sakharov notes,is identical in form to the Hilbert action principle,equation (3） above,with the exception that there the constant that multiplies the Riemann scalar curvature invariant is $- c ^ { 3 } / 1 6 \pi G$ (in conventional units), whereas here it is $B \hbar \int k \ d k$ (in the same conventional units).

The higher order terms in (27) lead to what Sakharov cals “corrections .. . to Einstein's equations.”

j. Overlooking these corrections,one evidently obtains the action principle of Einstein's theory when one insists on the equality

$$
G = { \binom { \mathrm { N e w t o n i a n } } { \mathrm { c o n s t a n t ~ o f ~ g r a v i t y } } } = { \frac { c ^ { 3 } } { 1 6 \pi B \hbar \int k d k } } .
$$

With $\pmb { B }$ a dimensionless numerical factor of the order of unity,it follows, Sakharov argues, that the effective upper limit or “cutoff” in the formally divergent integral in (28) is to be taken to be of the order of magnitude of the reciprocal Planck length [see equation (7)],

$$
k _ { \mathrm { c u t o f f } } \sim ( c ^ { 3 } / \hbar G ) ^ { 1 / 2 } = 1 / L ^ { * } = 1 / 1 . 6 \times 1 0 ^ { - 3 3 } \mathrm { c m } .
$$

In effect Sakharov is saying (l） that field physics suffers a sea change into something new and strange for wavelengths less than the Planck length,and for quantum energies of the order of $\hbar c k _ { \mathrm { c u t o f f } } \sim 1 0 ^ { 2 8 } \mathrm { e V }$ or $1 0 ^ { - 5 } \ \mathsf { g }$ or more; (2) that in consequence the integral $\int k d k$ is cut off; and (3) that the value of this cutoff, arising purely out of the physics of fields and particles, governs the value of the Newtonian constant of gravity, $G$

k. In this sense, Sakharov's analysis suggests that gravitation is to particle physics as elasticity is to chemical physics: merely a statistical measure of residual energies.In the one case, molecular bindings depend on departures of molecule-molecule bond lengths from standard values. In the other case, particle energies are affected by curvatures of the geometry.

1. Elasticity,which looks simple,gets its explanation from molecular bindings, which are complicated; but molecular bindings, which are complicated,receive their explanation in terms of Schrodinger's wave equation and Coulomb's law of force between charged point-masses, which are even simpler than elasticity.

m.Einstein's geometrodynamics, which looks simple, is interpreted by Sakharov as a correction term in particle physics, which is complicated. Is particle physics, which is complicated,destined some day in its turn to unravel into something simple—something far deper and far simpler than geometry ("pregeometry"; Chapter 44)?

# $\$ 123$ ."NO PRIOR GEOMETRY": A FEATURE DISTINGUISHING EINSTEIN'S THEORY FROM OTHER THEORIES OF GRAVITY

Whereas Einstein's theory of gravity is exceedingly compelling,one can readily construct less compelling and less elegant alternative theories. The physics literature is replete with examples [see Ni (l972),and Thorne, Ni,and Will (197l) for reviews]. However, when placed among its competitors, Einstein's theory stands out sharp and clear: it agrees with experiment; most of its competitors do not (Chapters 38-40). It describes gravity entirely in terms of geometry; most of its competitors do not. It is free of any“prior geometry”;most of its competitors are not.

Einstein's theory compared with other theories of gravity

Set aside,until Chapter 38, the issue of agreement with experiment. Einstein's theory remains unique. Every other theory either introduces auxiliary gravitational fields [e.g.,the scalar field of Brans and Dicke (l96l)], or involves “prior geometry," or both. Thus,every other theory is more complicated conceptually than Einstein's theory. Every other theory contains elements of complexity for which there is no experimental motivation.

All other theories introduce auxiliary gravitational fields or prior geometry

The concept of “prior geometry” requires elucidation, not least because the rejection of prior geometry played a key role in the reasoning that originally led Einstein to his geometrodynamic equation ${ \pmb { G } } = 8 \pi { \pmb { T } } .$ By“prior geometry” one means any aspect of the geometry of spacetime that is fixed immutably, i.e., that cannot be changed by changing the distribution of gravitating sources. Thus, prior geometry is not generated by or affected by matter; it is not dynamic. Example: Nordstrom(1913) formulated a theory in which the physical metric of spacetime $\pmb { \mathscr { g } }$ (the metric that enters into the equivalence principle) is generated by a “background” flat-spacetime metric $\pmb { \eta }$ ,and by a scalar gravitational field $\phi$ ：

$$
\begin{array} { r l } { \eta ^ { \alpha \beta } \phi _ { , \alpha \beta } = - 4 \pi \phi \eta ^ { \alpha \beta } T _ { \alpha \beta } \quad } & { \Bigl ( \begin{array} { c } { \mathrm { g e n e r a t i o n ~ o f ~ \phi \ b y } } \\ { \mathrm { s t r e s s - e n e r g y } } \end{array} \Bigr ) , } \\ { g _ { \alpha \beta } = \phi ^ { 2 } \eta _ { \alpha \beta } \quad } & { \Bigl ( \begin{array} { c } { \mathrm { c o n s t r u c t i o n ~ o f ~ } g } \\ { \mathrm { f r o m ~ } \phi \mathrm { ~ a n d ~ } \eta } \end{array} \Bigr ) . } \end{array}
$$

In this theory, the physical metric $\pmb { g }$ (governor of rods and clocks and of test-particle motion) has but one changeable degree of freedom-the freedom in $\phi$ The rest of $\pmb { g }$ is fixed by the flat spacetime metric ("prior geometry") $\pmb { \eta }$ .One does not remove the prior geometry by rewriting Nordstrom's equations (l7.23) in a form

$$
\begin{array} { r l } & { \qquad R = 2 4 \pi T , \qquad C ^ { \alpha \beta } _ { \mu \nu } = 0 } \\ & { \Bigl [ \mathrm { c u r v a t u c t e ~ s c a l a r } } \\ & { \Bigl [ \mathrm { c o n s t r u c t e d ~ f r o m } g \Bigr ] ^ { \mathrm { ~ \scriptscriptstyle ~ \int ~ } } \qquad \Bigl [ \underbrace { \vphantom { \biggl [ \sum _ { \alpha } \beta _ { n } \eta _ { \alpha \beta } ^ { \alpha \beta } } } _ { \bigl [ g ^ { \alpha \beta } T _ { \alpha \beta } \bigr ] } } & { \Bigl [ \mathrm { W e y l ~ t e n s o r } } \\ & { \qquad \mathrm { c o n s t r u c t e d ~ f r o m } g \Bigr ] } \end{array}
$$

devoid of reference to $\pmb { \eta }$ and $\phi$ [Einstein and Fokker (l914); exercise 17.8]. Mass can still infuence only one degree of freedom in the spacetime geometry. The other degrees of freedom are fixed $\dot { a }$ priori-they are prior geometry.And this prior geometry can perfectly well(in principle) be detected by physical experiments that make no reference to any equations (Box 17.3).

"Prior geometry" defined

Nordstrom's theory as an illustration of prior geometry

# Box 17.3 AN EXPERIMENT TO DETECT OR EXCLUDE CERTAIN TYPES OF PRIOR GEOMETRY (Based on December 197O discussions between Alfred Schild and Charles W.Misner)

Choose a momentarily static universe populated with a large supply of suitable pulsars. The pulsars should be absolutely regular, periodically emitting characteristic pulses of both gravitational and electromagnetic waves.

Two fleets of spaceships containing receivers are sent out “on station” to collect the experimental data.Admiral Weber's fleet carries gravitational-wave receivers; Admiral Hertz's fleet, electromagnetic receivers. The captain of each spaceship holds himself “on station” by monitoring three suitably chosen pulsars (of identical frequency) and maneuvering so that their pulses always arrive in coincidence.The experimental data he collects consist of the pulses received from all other pulsars, which he is not using for station keeping, each registered as coincident with or interlaced among the reference (stationary) pulses. [For display purposes, the pattern produced by any single pulsar can be converted to acoustic form. The reference pulses can be played acoustically (by the dataprocessing computer) on one drum at a fixed rate, and the pulses from other pulsars can be played on a second drum.A pattern of rythmic beats will result.]

When the data fleet is checked out and tuned up,each captain reports stationary patterns. Now the experiment begins. One or more massive stars are towed in among the fleet. The fleet reacts to stay on station, and reports changes in the data patterns. The spaceships on the outside edges of the fleet verify that no detectable changes occur at their stations; so the incident radiation from the distant pulsars can be regarded as unaffected by the newly placed stars. Data stations nearer the movable stars report the interesting data.

What are the results?

In a universe governed by the laws of special relativity (spacetime always flat)， no patterns change. (Weber's fleet was unable to get checked out in the first place,as no gravitational waves were ever detected from the pulsars). Neither stars, nor anything else,can produce gravitational fields. All aspects of the spacetime geometry are fixed a priori (complete prior geometry!). There is no gravity; and no light deflection takes place to make Hertz's captains adjust their positions.

In a universe governed by Nordstrom's theory of gravity (see text) both fleets get checked outi.e.,both see waves. But neither fleet sees any changes in the rhythmic pattern of beats. The stars being towed about have no influence on either gravitational waves or electromagnetic waves. The prior geometry (n) present in the theory precludes any light deflection or any gravitational-wave deflection.

In a universe governed by Whitehead's (1922) theory of gravity [see Will (l971b) and references cited therein], radio waves propagate along geodesics of the“physical metric” $\pmb { g } ,$ and get deflected by the gravitational fields of the stars. But gravitational waves propagate along geodesics of a flat background metric $\pmb { \eta }$ ,and are thus unaffected by the stars. Consequently, Hertz's captains must maneuver to keep on station; and they hear a chang-ing beat pattern between the reference pulsars and the other pulsars.But Weber's fleet remains on station and records no changes in the beat pattern. The prior geometry $( \pmb { \eta } )$ shows itself clearly in the experimental result.

In a universe governed by Einstein's theory, both fleets see effects (no sign of prior geometry because Einstein's theory has no prior geometry). Moreover, if the fleets were originally paired,one Weber ship and one Hertz at each station, they remain paired. No differences exist between the propagation of high-frequency light waves and high-frequency gravitational waves. Both propagate along geodesics of $\pmb { g }$

Mathematics was not suffciently refined in l917 to cleave apart the demands for “no prior geometry” and for a “geometric,coordinate-independent formulation of physics.”Einstein described both demands by a single phrase,“general covariance.” The “no-prior-geometry” demand actually fathered general relativity,but by doing so anonymously, disguised as “general covariance,” it also fathered half a century of confusion. [See, e.g., Kretschmann (1917).]

.A systematic treatment of the distinction between prior geometry ("absolute objects") and dynamic fields ("dynamic objects") is a notable feature of Anderson's (1967) relativity text.

"No prior geometry" as a part of Einstein's principle of "'general covariance"

# Exercise 17.8. EINSTEIN-FOKKER REDUCES TO NORDSTR0M

The vanishing of the Weyl tensor [equation (l3.5O)] for a spacetime metric $\pmb { g }$ guarantees that the metric is conformally flat-i.e.,that there exists a scalar field $\phi$ such that ${ \pmb g } = \phi ^ { 2 } { \pmb \eta }$ ， where $\pmb { \eta }$ is a flat-spacetime metric. [See, e.g.,Schouten (l954) for proof.] Thus,the Einstein-Fokker equation (17.24), $C ^ { \alpha \beta } { } _ { \mu \nu } = 0$ ,is equivalent tothe Nordstrom equation (17.23b).With this fact in hand,show that the Einstein-Fokker field equation $\scriptstyle R = 2 4 \pi T$ reduces to the Nordstrom field equation (17.23a).

# \$17.7. A TASTE OF THE HISTORY OF EINSTEIN'S EQUATION

Nothing shows better what an idea is and means today than the battles and changes it has undergone on its way to its present form. A complete history of general relativity would demand a book. Here let a few key quotes from a few of the great Papers give a little taste of what a proper history might encompass.

Einstein (l908):“We...will therefore in the following assume the complete physical equivalence of a gravitational field and of a corresponding acceleration of the reference system....the clock at a point $\pmb { P }$ for an observer anywhere in space runs $( 1 + \phi / c ^ { 2 } )$ times faster than the clock at the coordinate origin....it follows that light rays are curved by the gravitational field....an amount of energy $E$ has a mass $\scriptstyle { E / c ^ { 2 } }$ ”

Einstein and Grossmann (l9l3):“The theory described here originates from the conviction that the proportionality between the inertial and the gravitational mass of a body is an exact law of nature that must be expressed as a foundation principle of theoretical physics....An observer enclosed in an elevator has no way to decide whether the elevator is at rest in a static gravitational field or whether the elevator is located in gravitation-free space in an accelerated motion that is maintained by forces acting on the elevator (equivalence hypothesis)....In the decay of radium，for example, that decrease [of mass] amounts to l/lo,0o0 of the total mass.If those changes in inertial mass did not correspond to changes in gravitational mass, then deviations of inertial from gravitational masses would arise that are far larger than the Eotvos experiments allow. It must therefore be considered as very probable that the identity of gravitational and inertial mass is exact.

# EXERCISE

“The sought for generalization will surely be of the form

$$
\bar { \cal T } _ { \mu \nu } = \kappa T _ { \mu \nu } .
$$

where $\kappa$ is a constant and $\Gamma _ { \mu \nu }$ is a contravariant tensor of the second rank that arises. out of the fundamental tensor $g _ { \mu \nu }$ through differential operations.... it proved impossible to find a differential expression for $\Gamma _ { \mu \nu }$ that is a generalization of[Poisson's] $\varDelta \phi$ ,and that is a tensor with respect to arbitrary transformations....It seems most natural to demand that the system of equations should be covariant against arbitrary transformations. That stands in conflict with the result that the equations of the gravitational field do not possess this property."

Einstein and Grossman (l9l4): “In a l9l3 treatment ... we could not show general covariance for these gravitational equations. [Origin of their difficulty: part of the two-index curvature tensor was put on the left,to constitute the second-order part of the field equation,and part was put on the right with $T _ { \mu \nu }$ and was called gravitational stress-energy.It was asked that lefthand and righthand sides transform as tensors,which they cannot do under general coordinate transformations.]

Einstein (l9l5a):“In recent years I had been trying to found a general theory of relativity on the assumption of the relativity even of nonuniform motions.I believed in fact that I had found the only law of gravitation that corresponds to a reasonably formulated postulate of general relativity,and I sought to establish the necessity of exactly this solution in a paper that appeared last year in these proceedings.

“A renewed analysis showed me that that necessity absolutely was not shown in the approach adopted there; that it nevertheless appeared to be shown rested on an error.

“For these reasons,I lost all confidence in the field equations I had set up,and I sought for an approach that would limit the possibilities in a natural way.In this way I was led back to the demand for the general covariance of the field equations, from which I had departed three years ago,while working with my friend Grossmann, only with a heavy heart.In fact we had already at that time come quite near to the solution of the problem that is given in what follows.

“According to what has been said,it is natural to postulate the field equations of gravitation in the form

$$
R _ { \mu \nu } = - \kappa T _ { \mu \nu } ,
$$

since we already know that these equations are covariant with respect to arbitrary transformations of determinant l. In fact, these equations satisfy all-conditions.that.. we have to impose on them. [Here $R _ { \mu \nu }$ is a piece of the Ricci tensor that Einstein regarded as covariant.]...

“Equations (22a) give in the first approximation

$$
\frac { \partial ^ { 2 } g ^ { \alpha \beta } } { \partial x ^ { \alpha } \partial x ^ { \beta } } = 0 .
$$

By this [condition] the coordinate system is still not determined,in the sense that for this determination four equations are necessary."(Session of Nov.4,l9l5,published Nov. 11.)

Einstein (l915b):“In a recently published investigation,I have shown how a theory of the gravitational field can be founded on Riemann's covariant theory of many-dimensional manifolds.Here it will now be proved that, by introducing a surely bold additional hypothesis on the structure of matter,a still tighter logical structure of the theory can be achieved....it may very well be possible that in the matter to which the given expression refers,gravitational fields play an essential part. Then $T ^ { \mu } { } _ { \mu }$ can appear to be positive for the entire structure,although in reality only $T ^ { \mu } { } _ { \mu } + t ^ { \mu } { } _ { \mu }$ is positive,and $T ^ { \mu } { } _ { \mu }$ vanishes everywhere.We assume in the following that in fact the condition $T ^ { \mu } { } _ { \mu } = 0$ is fulfilled [quite] generally.

“Whoever does not from the beginning reject the hypothesis that molecular [smalscalel gravitational fields constitute an essential part of matter willsee in the following a strong support for this point of view.

“Our hypothesis makes it possble ... to give the field equations of gravitation in a generally covariant form ...

$$
G _ { \mu \nu } = - \kappa T _ { \mu \nu }
$$

[where $G _ { \mu \nu }$ is the Ricci tensor].”(Session of Nov.l1,1915; published Nov.18.)

Einstein (l9l5c):“I have shown that no objection of principle stands in the way of this hypothesis [the field equations],by which space and time are deprived of the last trace of objective reality.In the present work I find an important confirmation of this most radical theory of relativity: it turns out that it explains qualitatively and quantitatively the secular precession of the orbit of Mercury in the direction of the orbital motion,as discovered by Leverrier, which amounts to about $4 5 ^ { \prime \prime }$ per century, without calling on any special hypothesis whatsoever.”

Einstein (1915d; session of Nov.25,1915;published Dec.2):“More recently I have found that one can proceed without hypotheses about the energy tensor of matter when one introduces the energy tensor of matter in a somewhat different way than was done in my two earlier communications.The field equations for the motion of the perihelion of Mercury are undisturbed by this modification....

"Let us put

$$
G _ { i m } = \mathrm { ~ - } \kappa \left( T _ { i m } - \frac { 1 } { 2 } g _ { i m } T \right)
$$

[where $G _ { i m }$ is the Ricci tensor].”...

...these equations, in contrast to (9),contain no new condition, so that no other assumption has to be made about the energy tensor of matter than obedience to the energy-momentum [conservation] laws.

“With this step,general relativity is finally completed as a logical structure. The postulate of relativity in its most general formulation,which makes the spacetime coordinates into physically meaningless parameters,leads compelingly to a completely determinate theory of gravitation that explains the perihelion motion of Mercury. In contrast, the general-relativity postulate is able to open up to us nothing about the nature of the other processes of nature that special relativity has not already taught. The opinion on this point that I recently expressed in these proceedings was erroneous. Every physical theory compatible with special relativity can be aligned into the system of general relativity by means of the absolute differential calculus,without [general relativity] supplying any criterion for the acceptability of that theory.”

Hilbert (l9l5):“Axiom I [notation changed to conform to usage in this book]. The law of physical events is determined through a world function [Mie's terminology; better known today as “Lagrangian"] $L$ ,that contains the following arguments:

$$
\begin{array} { c } { { g _ { \mu \nu } , { \displaystyle \frac { \partial g _ { \mu \nu } } { \partial x ^ { \alpha } } } , { \displaystyle \frac { \partial ^ { 2 } g _ { \mu \nu } } { \partial x ^ { \alpha } \partial x ^ { \beta } } } , } } \\ { { { \cal A } _ { \sigma } , { \displaystyle \frac { \partial A _ { \sigma } } { \partial x ^ { \tau } } } , } } \end{array}
$$

and specifically the variation of the integral

$$
\int L ( - g ) ^ { 1 / 2 } d ^ { 4 } x
$$

must vanish for[changesin]every oneof the 14 potentials $g _ { \sigma \nu } , A _ { \sigma } . \ . \ . \ .$

“Axiom II (axiom of general invariance). The world function $\pmb { L }$ is invariant with respect to arbitrary transformations of the world parameters [coordinates] $x ^ { \alpha }$ ..

“For the world function $\cal L$ ， still further axioms are needed to make its choice unambiguous. If the gravitation equations are to contain only second derivatives of the potentials $g ^ { \sigma \nu }$ ，then $L$ must have the form

$$
L = R + L _ { \mathrm { e l e c } } ,
$$

where $R$ is the invariant built from the Riemann tensor (curvature of the four-dimensional manifold.”(Session of Nov.20,1915.)

Einstein (1916c): “Recently $\mathbf { H }$ A.Lorentz and D. Hilbert have succeeded in giving general relativity an especially transparent form in deriving its equations from a single variation principle.This will be done also in the following treatment. There it is my aim to present the basic relations as transparently as possble and in a way as general as general relativity allows.”

Einstein (l9l6b):“From this it follows,first of all,that gravitational fields spread Out with the speed of light....[plane] waves transport energy....One thus gets... the radiation of the system per unit time....

$$
\frac { G } { 2 4 \pi } \sum _ { \alpha , \beta } \bigg ( \frac { \partial ^ { 3 } J _ { \alpha \beta } } { \partial t ^ { 3 } } \bigg ) ^ { 2 } \cdot ^ { , }
$$

Hilbert (l9l7):“As for the principle of causality, the physical quantities and their time-rates of change may be known at the present time in any given coordinate system; a prediction will then have a physical meaning only when it is invariant with respect to all those transformations for which exactly those coordinates used for the present time remain unchanged.I declare that predictions of this kind for the future are all uniquely determined; that is,that the causality principle holds in this formulation:

“From the knowledge of the l4 physical potentials $g _ { \mu \nu } , \ A _ { \sigma } ,$ in the present, all predictions about the same quantities in the future folow necessarily and uniquely insofar as they have physical meaning.”

# CHAPTER 18

# WEAK GRAVITATIONAL FIELDS

The way that can be walked on is not the perfect way. The word that can be said is not the perfect word.

LAO-TZU (\~3rd century B.C.)

# $\$ 123,1$ . THE LINEARIZED THEORY OF GRAVITY

Because of the geometric language and abbreviations used in writing them, Einstein's field equations, $G _ { \mu \nu } = 8 \pi T _ { \mu \nu }$ ,hardly seem to be differential equations at all, much less ones with many familiar properties.The best way to see that they are is to apply them to weak-field situations

"Linearized theory of gravity":

(1）as weak-field limit of general relativity

$$
g _ { \mu \nu } = \eta _ { \mu \nu } + h _ { \mu \nu } , \qquad | h _ { \mu \nu } | \ll 1 ,
$$

e.g., to the solar system, where $| h _ { \mu \nu } | \sim | \varPhi | \lesssim M _ { \odot } / R _ { \odot } \sim 1 0 ^ { - 6 }$ or to a weak gravitational wave propagating through interstellar space.

In a weak-field situation, one can expand the feld equations in powers of $h _ { \mu \nu } ,$ using a coordinate frame where (l8.1) holds; and without much loss of accuracy, one can keep only linear terms.The resulting formalism is often called “the linearized theory of gravity,”because it is an important theory in its own right. In fact, it is precisely this “linearized theory” that one obtains when one asks for the classical field corresponding to quantum-mechanical particles of (l） zero rest mass and (2) spin two in (3) flat spacetime [see Fierz and Pauli (l939)]. Track-2 readers have already explored linearized theory somewhat in $\ S 7 . 1$ ,exercise 7.3,and Box 7.1.There it went under the alternative name,“tensor-feld theory of gravity in flat spacetime.”

(2)as standard "field-theory" description of gravity in ‘flat spacetime"

(3)as a foundation for "deriving" general relativity

Just as one can“descend” from general relativity to linearized theory by linearizing about flat spacetime (see below), so one can “bootstrap” one's way back up from linearized theory to general relativity by imposing consistency between the linearized field equations and the.equations of motion. or. equivalently,by asking about: (l) the stress-energy carried by the linearized gravitational field $h _ { \mu \nu }$ ； (2) the influence of this stress-energy acting as a source for corrections $h ^ { ( 1 ) } { } _ { \mu \nu }$ to the field; (3) the stress-energy carried by the corrections ${ h ^ { ( 1 ) } } _ { \mu \nu }$ ; (4)the influence of this stress-energy acting as a source for corrections ${ h ^ { ( 2 ) } } _ { \mu \nu }$ to the corretions $h ^ { ( 1 ) } { } _ { \mu \nu }$ (5) the stress-energy carried by the corrections to the corrections; and so on. This alternative way to derive general relativity has been developed and explored by Gupta (l954,l957,1962), Kraichnan (l955), Thirring (196l), Feynman (1963a), Weinberg (l965),and Deser (1970).But because the outlook is far from geometric (see Box l8.l), the details of the derivation are not presented here.(But see part 5 of Box 17.2.)

Details of linearized theory:

Here attention focuses on deriving linearized theory from general relativity. Adopt the form (18.l） for the metric components. The resulting connection coeffcients [equations (8.24b)], when linearized in the metric perturbation $h _ { \mu \nu } ,$ read

(1）connection coefficients

$$
\begin{array} { r l } { { \displaystyle { \cal T } _ { \alpha \beta } ^ { \mu } = \frac { 1 } { 2 } \eta ^ { \mu \nu } ( h _ { \alpha \nu , \beta } + h _ { \beta \nu , \alpha } - h _ { \alpha \beta , \nu } ) } } & { { } } \\ { { \displaystyle \equiv \frac { 1 } { 2 } ( h _ { \alpha } { } ^ { \mu } { } _ { , \beta } + h _ { \beta } { } ^ { \mu } { } _ { , \alpha } - h _ { \alpha \beta } { } ^ { , \mu } ) } . } \end{array}
$$

The second line here introduces the convention, used routinely whenever one expands in powers of $h _ { \mu \nu }$ ，that indices of $h _ { \mu \nu }$ are raised and lowered using $\eta ^ { \mu \nu }$ and $\eta _ { \mu \nu } , n o t g ^ { \mu \nu }$ and $g _ { \mu \nu }$ .A similar linearization of the Ricci tensor [equation (8.47)l yields

$$
\begin{array} { l } { { R _ { \mu \nu } = { \Gamma ^ { \alpha } } _ { \mu \nu , \alpha } - { \Gamma ^ { \alpha } } _ { \mu \alpha , \nu } } } \\ { { \displaystyle \quad = \frac { 1 } { 2 } ( { h _ { \mu } } ^ { \alpha } { } _ { , \nu \alpha } + { h _ { \nu } } ^ { \alpha } { } _ { , \mu \alpha } - { h _ { \mu \nu , \alpha } } ^ { \alpha } - { h _ { , \mu \nu } } ) } , } \end{array}
$$

where

$$
h \equiv h _ { \alpha } ^ { \alpha } = \eta ^ { \alpha \beta } h _ { \alpha \beta } .
$$

After a further contraction to form $R \equiv g ^ { \mu \nu } R _ { \mu \nu } \stackrel { \cdot } { \approx } \eta ^ { \mu \nu } R _ { \mu \nu } ;$ ,one finds that the Einstein equations, $2 G _ { \mu \nu } = 1 6 \pi T _ { \mu \nu } $ read

$$
\begin{array} { r l } & { h _ { \mu \alpha , \nu } ^ { \alpha } + h _ { \nu \alpha , \mu } ^ { \alpha } - h _ { \mu \nu , \alpha } ^ { \alpha } - h _ { , \mu \nu } } \\ & { \qquad - \eta _ { \mu \nu } ( h _ { \alpha \beta } , ^ { \alpha \beta } - h _ { , \beta } ^ { \beta } ) = 1 6 \pi T _ { \mu \nu } . } \end{array}
$$

The numberof terms has increased in passing from $R _ { \mu \nu }$ (18.3) to $G _ { \mu \nu } = R _ { \mu \nu } - { \textstyle \frac { 1 } { 2 } } g _ { \mu \nu } R$ (18.5), but this annoyance can be counteracted by defining

(2)"gravitational potentials" h

$$
\overline { { h } } _ { \mu \nu } \equiv h _ { \mu \nu } - \frac { 1 } { 2 } \eta _ { \mu \nu } h
$$

and using a bar to imply a corresponding operation on any other symmetric tensor.

Box 18.1 DERIVATIONS OF GENERAL RELATIVITY FROM GEOMETRIC VIEWPOINTAND FROM SPIN-TWO VIEWPOINT,COMPARED AND CONTRASTED   

<table><tr><td colspan="2">Einstein derivation</td><td>Spin.2 derivation</td></tr><tr><td>Nature of primordial spacetime1 geometry?</td><td>Not primordial; geometry is a dynamic participant in physics</td><td>“God-given” flat Lorentz spacetime manifold</td></tr><tr><td>Topology (multiple connected- ness） of spacetime?</td><td>Laws of physics are local; they do not specify the topology</td><td>Simply connected Euclidean topology</td></tr><tr><td>Vision of physics?</td><td>Dynamic geometry is the “master field”of physics</td><td>This field,that field,and the other field all execute theirdynamics in a flat- spacetime manifold</td></tr><tr><td rowspan="2">Starting points for this deri- vation of general relativity</td><td>1.Equivalence principle (world lines of photons and test particles are geo- desics of the spacetime geometry)</td><td>1.Begin with field of spin two and zero rest mass in flat spacetime. 2.Stress-energy tensor built from this field serves as a</td></tr><tr><td>2.That tensorial conserved quantity which is derived from the curvature (Cartan&#x27;s moment of rotation） is to be identified with the tensor of stress-momentum-energy</td><td>source for this field.</td></tr><tr><td>Resulting equations</td><td>(see Chapter 15). Einstein&#x27;s field equations</td><td>Einstein&#x27;s field equations</td></tr><tr><td>Resulting assessment of the spacetime geometry from which pant in physics derivation started</td><td>Fundamental dynamic partici-</td><td>None.Resulting theory eradi- cates original flat geometry from all equations,showing it to be unobservable</td></tr><tr><td>View about the greatest single crisis of physics to emerge from these equations: complete universe gravitational collapse</td><td>Central to understanding the nature of matter and the</td><td>Unimportant or at most peripheral</td></tr></table>

Thus $G _ { \mu \nu } = \bar { R } _ { \mu \nu }$ to first order in the $h _ { \mu \nu } ,$ and $\overline { { { \bar { h } } } } _ { \mu \nu } = h _ { \mu \nu }$ i.e., $h _ { _ { \mu \nu } } = \bar { h } _ { _ { \mu \nu } } - { \scriptstyle \frac { 1 } { 2 } } \eta _ { _ { \mu \nu } } \bar { h }$ With this notation the linearized feld equations become

$$
- \overline { { h } } _ { \mu \nu , \alpha } ^ { \quad \alpha } - \eta _ { \mu \nu } \overline { { h } } _ { \alpha \beta , } ^ { \quad \alpha \beta } + \overline { { h } } _ { \mu \alpha , \enskip \nu } ^ { \quad \alpha } + \overline { { h } } _ { \nu \alpha , \enskip \mu } ^ { \quad \alpha } = 1 6 \pi T _ { \mu \nu } .
$$

The first term in these linearized equations is the usual flat-space d'Alembertian, and the other terms serve merely to keep the equations“gauge-invariant” (see Box

18.2). In $\mathbf { B o x } \ 1 8 . 2$ it is shown that, without loss of generality, one can impose the “gauge conditions”

(4）gauge conditions

$$
{ \overline { { h } } } { \mu } { \alpha } _ { , \alpha } = 0 .
$$

These gauge conditions are the tensor analog of the Lorentz gauge $A ^ { \alpha } { } _ { , \alpha } = 0$ of electromagnetic theory. The field equations (18.7) then become

(5) field equations and metric in Lorentz gauge

$$
- \overline { { h } } _ { \mu \nu , \alpha } { } ^ { \alpha } = 1 6 \pi T _ { \mu \nu } .
$$

The gauge conditions $( l 8 . 8 a )$ ,the field equations (18.8b),and the definition of the metric

$$
g _ { \mu \nu } = \eta _ { \mu \nu } + h _ { \mu \nu } = \eta _ { \mu \nu } + \overline { { h } } _ { \mu \nu } - \frac { 1 } { 2 } \eta _ { \mu \nu } \overline { { h } }
$$

are the fundamental equations of the linearized theory of gravity written in Lorentz gauge.

# EXERCISES

# Exercise 18.1. GAUGE INVARIANCE OF THE RIEMANN CURVATURE

Show that in linearized theory the components of the Riemann tensor are

$$
R _ { \alpha \mu \beta \nu } = \frac { 1 } { 2 } ( h _ { \alpha \nu , \mu \beta } + h _ { \mu \beta , \nu \alpha } - h _ { \mu \nu , \alpha \beta } - h _ { \alpha \beta , \mu \nu } ) .
$$

Then show that these components are left unchanged by a gauge transformation of the form discussed in Box l8.2 [equation (4b)). Since the Einstein tensor is a contraction of the Riemann tensor,this shows that it is also gauge-invariant.

# Exercise 18.2. JUSTIFICATION OF LORENTZ GAUGE

Let a particular solution to the field equations (8.7) of linearized theory be given, in an arbitrary gauge. Show that there necessarily exist four generating functions $\xi _ { \mu } ( t , x ^ { j } )$ whose gauge transformation [Box l8.2,eq. (4b)] makes

$$
{ \bar { h } } ^ { \operatorname { n e w } \mu \alpha } , _ { \alpha } = 0 \qquad \mathrm { ( L o r e n t z ~ g a u g e ) . }
$$

Also show that a subsequent gauge transformation leaves this Lorentz gauge condition unaffected if and only if its generating functions satisfy the sourceless wave equation

$$
\xi ^ { \alpha , \beta } { } _ { \beta } = 0 .
$$

# Exercise 18.3. EXTERNAL FIELD OF A STATIC, SPHERICAL BODY

Consider the external gravitational feld of a static spherical body,as described in the body's (nearly) Lorentz frame-i.e.,in a nearly rectangular coordinate system $\{ h _ { \mu \nu } | \ll 1$ ,in which the body is located at $x = y = z = 0$ for all $t .$ By fiat, adopt Lorentz gauge.

(a) Show that the field equations (l8.8b) and gauge conditions (18.8a) imply

$$
\begin{array} { r l r l } & { \overline { { h } } _ { 0 0 } = 4 M / ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 } , } & & { \overline { { h } } _ { 0 j } = \overline { { h } } _ { j k } = 0 , } \\ & { h _ { 0 0 } = h _ { x x } = h _ { y y } = h _ { z z } = 2 M / ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 } , } & & { h _ { \alpha \beta } = 0 \mathrm { ~ i f ~ } \alpha \neq \beta , } \end{array}
$$

where $M$ is a constant (the mass of the body; see $\ S 1 9 . 3 )$

# B0x 18.2 GAUGE TRANSFORMATIONS AND COORDINATE TRANSFORMATIONS IN LINEARIZED THEORY

A. The Basic Equations of Linearized Theory, written in any coordinate system that is nearly globally Lorentz, are (18.l) and (18.7):

$$
\begin{array} { c } { { g _ { \mu \nu } = \eta _ { \mu \nu } + h _ { \mu \nu } , \qquad | h _ { \mu \nu } | \ll 1 ; } } \\ { { - \overline { { { h } } } _ { \mu \nu , \alpha } \alpha _ { \alpha } - \eta _ { \mu \nu } \overline { { { h } } } _ { \alpha \beta } { } ^ { , \alpha \beta } + \overline { { { h } } } _ { \mu \alpha } { } ^ { , \alpha } { } _ { \nu } + \overline { { { h } } } _ { \nu \alpha } { } ^ { , \alpha } { } _ { \mu } = 1 6 \pi T _ { \mu \nu } . } } \end{array}
$$

Two different types of coordinate transformations connect nearly globally Lorentz systems to each other: global Lorentz transformations, and infinitesimal coordinate transformations.

1. Global Lorentz Transformations:

$$
x ^ { \mu } = { A ^ { \mu } } _ { \alpha ^ { \prime } } x ^ { \alpha ^ { \prime } } , \qquad { A ^ { \mu } } _ { \alpha ^ { \prime } } { A ^ { \dot { \nu } } } _ { \beta } { \cdot } \eta _ { \mu \nu } = \eta _ { \alpha ^ { \prime } \beta ^ { \prime } } .
$$

These transform the metric coefficients via

$$
\begin{array} { c } { { \eta _ { \alpha ^ { \prime } \beta ^ { \prime } } + h _ { \alpha ^ { \prime } \beta ^ { \prime } } = g _ { \alpha ^ { \prime } \beta ^ { \prime } } = \frac { \partial x ^ { \mu } } { \partial x ^ { \alpha ^ { \prime } } } \frac { \partial x ^ { \nu } } { \partial x ^ { \beta ^ { \prime } } } g _ { \mu \nu } = { A ^ { \mu } } _ { \alpha ^ { \prime } } { A ^ { \nu } } _ { \beta ^ { \prime } } ( \eta _ { \mu \nu } + h _ { \mu \nu } ) } } \\ { { = \eta _ { \alpha ^ { \prime } \beta ^ { \prime } } + { A ^ { \mu } } _ { \alpha ^ { \prime } } \ { A ^ { \nu } } _ { \beta ^ { \ast } } h _ { \mu \nu } . } } \end{array}
$$

Thus, $h _ { \mu \nu }$ -and likewise $\overline { { h } } _ { \mu \nu }$ -transform like components of a tensor in flat spacetime

$$
h _ { \alpha ^ { \prime } \beta ^ { \prime } } = A ^ { \mu } { } _ { \alpha ^ { \prime } } A ^ { \nu } { } _ { \beta ^ { \prime } } h _ { \mu \nu } .
$$

2. Infinitesimal Coordinate Transformations (creation of “ripples” in the coordinate system):

$$
x ^ { \mu ^ { \prime } } ( \mathcal { O } \bar { \mathcal { P } } ) = x ^ { \mu } ( \mathcal { P } ) + \xi ^ { \mu } ( \mathcal { P } ) ,
$$

where $\xi ^ { \mu } ( { \mathcal { P } } )$ are four arbitrary functions small enough to leave $| h _ { \mu ^ { \prime } \nu ^ { \prime } } | \ll 1$ Infinitesimal transformations of this sort make tiny changes in the functional forms of all scalar, vector,and tensor fields. Example: the temperature $T$ is a unique function of position, $T ( { \mathcal { P } } )$ ; so when written as a function of coordinates it changes

$$
\begin{array} { c } { { T ( x ^ { \mu ^ { * } } = a ^ { \mu } ) = T ( x ^ { \mu } + \xi ^ { \mu } = a ^ { \mu } ) = T ( x ^ { \mu } = a ^ { \mu } - \xi ^ { \mu } ) } } \\ { { { } } } \\ { { { } = T ( x ^ { \mu } = a ^ { \mu } ) - T _ { , \mu } \xi ^ { \mu } ; } } \end{array}
$$

i.e., if $\xi ^ { 0 } = 0 . 0 0 1 \ \sin ( x ^ { 1 } )$ ,and if $T = \cos ^ { 2 } ( x ^ { 0 } )$ ,then

$$
T = \cos ^ { 2 } ( x ^ { 0 ^ { \prime } } ) + 0 . 0 0 2 \sin ( x ^ { 1 ^ { \prime } } ) \cos ( x ^ { 0 ^ { \prime } } ) \sin ( x ^ { 0 ^ { \prime } } ) .
$$

# Box 18.2 (continued)

These tiny changes can be ignored in all quantities except the metric, where tiny deviations from $\eta _ { \mu \nu }$ contain all the information about gravity. The usual tensor transformation law for the metric

$$
g _ { \rho ^ { \prime } \sigma ^ { \prime } } [ x ^ { \alpha ^ { \prime } } ( \mathcal { P } ) ] = g _ { \mu \nu } [ x ^ { \alpha } ( \mathcal { S } ^ { \rho } ) ] \frac { \hat { \partial } x ^ { \mu } } { \hat { \partial } x ^ { \rho ^ { \prime } } } \frac { \hat { \partial } x ^ { \nu } } { \hat { \partial } x ^ { \rho ^ { \prime } } } ,
$$

when combined with the transformation law (4a) and with

$$
g _ { \mu \nu } [ x ^ { \alpha } ( \mathcal { P } ) ] = \eta _ { \mu \nu } + h _ { \mu \nu } [ x ^ { \alpha } ( \mathcal { S } ) ] ,
$$

reveals that

$$
\begin{array} { r } { g _ { \rho ^ { \prime } \sigma ^ { \prime } } ( x ^ { \alpha ^ { \prime } } = a ^ { \alpha } ) = \eta _ { \rho \sigma } + h _ { \rho \sigma } ( x ^ { \alpha } = a ^ { \alpha } ) - \xi _ { \rho , \sigma } - \xi _ { \sigma , \rho } \mathrm { } } \\ { + \mathrm { \ n e g l i g i b l e \ c o r r e c t i o n s } \sim h _ { \rho \sigma , \alpha } \xi ^ { \alpha } \mathrm { \ a n d } \sim h _ { \rho \alpha } { \xi ^ { \alpha } } _ { , \sigma } . } \end{array}
$$

Hence,the metric perturbation functions in the new $( x ^ { \mu ^ { \prime } } )$ and old $( x ^ { \mu } )$ coordinate systems are related by

$$
h _ { \mu \nu } ^ { \mathrm { n e w } } = h _ { \mu \nu } ^ { \mathrm { o l d } } - \xi _ { \mu , \nu } - \xi _ { \nu , \mu } ,
$$

whereas the functionalforms ofallother scalars,vectors,and tensors are unaltered, to within the precision of linearized theory.

B. Gauge Transformations and Gauge Invariance. In linearized theory one usually regards equation (4b) as gauge transformations, analogous to those

$$
{ \cal A } _ { \mu } ^ { \mathrm { n e w } } = { \cal A } _ { \mu } ^ { \mathrm { o l d } } + \Psi _ { , \mu }
$$

of electromagnetic theory. The fact that gravitational gauge transformations do not affect the functional forms of scalars,vectors, or tensors (i.e.,observables) is called "gauge invariance.” Just as a straightforward calculation reveals the gauge invariance of the electromagnetic field,

$$
F _ { \mu \nu } ^ { \mathrm { n e w } } = A _ { \nu , \mu } ^ { \mathrm { n e w } } - A _ { \mu , \nu } ^ { \mathrm { n e w } } = A _ { \nu , \mu } ^ { \mathrm { o l d } } + \varPsi _ { , \nu \mu } - A _ { \mu , \nu } ^ { \mathrm { o l d } } - \varPsi _ { , \mu \nu } = F _ { \mu \nu } ^ { \mathrm { o l d } } ,
$$

so a straightforward calculation (exercise 18.1) reveals the gauge invariance of the Riemann tensor

$$
R _ { \mu \nu \alpha \beta } ^ { \mathrm { n e w } } = R _ { \mu \nu \alpha \beta } ^ { \mathrm { o l d } } .
$$

Such gauge invariance was already guaranteed by the fact that $R _ { \mu \nu \alpha \beta }$ are the components of a tensor, and are thus essentially the same whether calculated in an orthonormal frame $g _ { \hat { \mu } \hat { \nu } } = \eta _ { \mu \nu } ,$ in the old coordinates where $g _ { \mu \nu } = \eta _ { \mu \nu } ^ { \cdot } + h _ { \mu \nu } ^ { \scriptscriptstyle 0 1 0 }$ 0r in the new coordinates where $g _ { \mu \nu } = \eta _ { \mu \nu } + h _ { \mu \nu } ^ { \mathrm { n e w } }$

Like the Riemann tensor, the Einstein tensor and the stress-energy tensor are unaffected by gauge transformations. Hence, ifone knows a specific solution $\overline { { h } } _ { \mu \nu }$ t0 the linearized field equations (2) for a given $T ^ { \mu \nu }$ ,one can obtain another solution that describes precisely the samephysical situation (allobseruables unchanged)bythe change of gauge (4), in which $\xi _ { \mu }$ are four arbitrary but small functions.

C. Lorentz Gauge. One can show (exercise 18.2) that for any physical situation, one can specialize the gauge (i.e., the coordinates) so that ${ \overline { { h } } } { } ^ { \mu \alpha } { } _ { , \alpha } = 0$ This is the Lorentz gauge introduced in $\ S 1 8 . 1$ .The Lorentz gauge is not fixed uniquely. The gauge condition $\overline { { { h } } } { ^ { \mu \alpha } } { _ { , \alpha } } = 0$ is left unafected by any gauge transformation for which

$$
\xi ^ { \alpha , \beta } { } _ { \beta } = 0 .
$$

(See exercise 18.2.)

D. Curvilinear Coordinate Systems. Once the gauge has been fixed by fiat for a given system (e.g., the solar system), one can regard $h _ { \mu \nu }$ and $\overline { { h } } _ { \mu \nu }$ as components of tensors in flat spacetime; and one can regard the field equations (2) and the chosen gauge conditions as geometric, coordinate-independent equations in flat spacetime. This viewpoint allows one to use curvilinear coordinates (e.g., spherical coordinates centered on the sun),if one wishes. But in doing so, one must everywhere replace theLorentzcompoentsofthemetric,ythemetricsompoet in the flat-spacetime curvilinear coordinate system; and one must replace all ordinary derivatives ("commas") in the field equations and gauge conditions by covariant derivatives whoseconnection coeffcientscomefrom gunat See exercise 18.3 for an example.

(b)Adopt spherical polar coordinates,

$$
x = r \sin \theta \cos \phi , \qquad y = r \sin \theta \sin \phi , \qquad z = r \cos \theta .
$$

By regarding $h _ { \mu \nu }$ and $\overline { { h } } _ { \mu \nu }$ as components of tensors in fat spacetime (see end of Box 18.2), and by using the usual tensor transformation laws, put the solution found in (a) into the form

$$
\begin{array} { r } { \overline { { h } } _ { 0 0 } = 4 M / r , \qquad \overline { { h } } _ { 0 j } = \widetilde { h } _ { j k } = 0 , } \end{array}
$$

$$
h _ { 0 0 } = { \frac { 2 M } { r } } , \qquad h _ { 0 j } = 0 , \qquad h _ { j k } = { \frac { 2 M } { r } } g _ { j k } \qquad 
$$

where gαβ flat are the components of the flat-spacetime metric in the spherical coordinate system

$$
\begin{array} { r l r } & { } & { g _ { \scriptscriptstyle { 0 0 } } _ { \Pi \mathrm { a t } } = - 1 , \qquad g _ { \scriptscriptstyle { r \tau _ { \mathrm { f l a t } } } } = 1 , \qquad g _ { \scriptscriptstyle { \theta \theta } _ { \mathrm { f l a t } } } = r ^ { 2 } . } \\ & { } & { g _ { \scriptscriptstyle { \phi \phi } _ { \mathrm { f l a t } } } = r ^ { 2 } \sin ^ { 2 } \theta . \qquad \quad g _ { \alpha \beta _ { \mathrm { f l a t } } } = 0 \mathrm { ~ w h e n ~ } \alpha \neq \beta . } \end{array}
$$

Thereby conclude that the general relativistic line element,accurate to linearized order, is

$$
d s ^ { 2 } = { } - ( 1 - 2 M / r ) d t ^ { 2 } + ( 1 + 2 M / r ) ( d r ^ { 2 } + r ^ { 2 } d \theta ^ { 2 } + r ^ { 2 } \sin ^ { 2 } \theta d \phi ^ { 2 } ) .
$$

：(c) Derive this general, static,spherically symmetric,Lorentz-gauge,vacuum solution to the linearized field equations from scratch,working entirely in spherical coordinates.[Hint: Asdiseusedateendofoiqan8c)stbeeplacedy and in the field equations and gauge conditions (l8.8a,b),all commas (partial derivatives) must be replaced by covariant derivatives, whose connection coeffcients come from $g _ { \mu \nu \mathrm { \ n a t } } ]$ (d) Calculate the Riemann curvature tensor for this gravitational feld. The answer should agree with equation (1.14).

# $\$ 18.2$ .GRAVITATIONAL WAVES

# Linearized theory and electromagnetic theory compared

The gauge conditions and field equations (l8.8a,b) of linearized theory bear a close resemblance to the equations of electromagnetic theory in Lorentz gauge and flat spacetime,

$$
\begin{array} { c } { { A ^ { \alpha } { } _ { , \alpha } = 0 , } } \\ { { - A ^ { \mu } { } _ { , \alpha } { } ^ { \alpha } = 4 \pi J ^ { \mu } . } } \end{array}
$$

They differ only in the added index( $h ^ { \mu \nu }$ versus $A ^ { \mu }$ ， $T ^ { \mu \nu }$ versus $J ^ { \mu }$ ). Consequently, from past experience with electromagnetic theory, one can infer much about linearized gravitation theory.

For example, the field equations (18.8b) must have gravitational-wave solutions. The analog of the electromagnetic plane wave

$$
A ^ { \varepsilon } = A ^ { \varepsilon } ( t - z ) , A ^ { y } = A ^ { y } ( t - z ) , A ^ { z } = 0 , A ^ { 0 } = 0 ,
$$

Plane gravitational waves

will be the gravitational plane wave

$$
\begin{array} { r l } & { \overline { { h } } ^ { x x } = \overline { { h } } ^ { x x } ( t - z ) , \qquad \overline { { h } } ^ { x y } = \overline { { h } } ^ { x y } ( t - z ) , \qquad \overline { { h } } ^ { y y } = \overline { { h } } ^ { y y } ( t - z ) , } \\ & { \qquad \overline { { h } } ^ { \mu 0 } = \overline { { h } } ^ { \mu z } = 0 \mathrm { ~ f o r ~ a l l ~ } \mu . } \end{array}
$$

Although a detailed study of such waves will be delayed until Chapters 35-37, some properties of these waves are explored in the exercises at the end of the next section.

# £18.3. EFFECT OF GRAVITY ON MATTER

How to analyze effects of weak gravity on matter

The effects of weak gravitational fields on matter can be computed by using the linearized metric (18.1) and Christoffel symbols (18.2) in the appropriate equations of motion--i.e.,in the geodesic equation (for the motion of particles or light rays), in the hydrodynamic equations (for fluid matter), in Maxwel's equations (for electromagnetic waves), or in the equation $\pmb { \nabla } \cdot \pmb { \tau } = 0$ for the total stress-energy tensor of whatever fields and matter may be present. Exercises 18.5,18.6 and 18.7 provide examples,as do the Newtonian-limit calculations in exercises l6.l and 16.4, and in $\ S 1 7 . 4$ . If, however, the lowest-order (linearized） gravitational “forces”(Christoffel-symbol terms) have a significant influence on the motion of the sources of the gravitational field,one finds that the linearized field equation (18.7)is inadequate, and better approximations to Einstein's equations must be considered.[Thus emission of gravitational waves by a mechanically or electrically driven oscillator falls within the scope of linearized theory,but emission by a double-star system, or by stellar Oscillations that gravitational forces maintain,will require discussion of nonlinear terms (gravitational “stress-energy") in the Einstein equations; see $\ S \ S 3 6 . 9$ to 36.11.]

The above conclusions follow from a consideration of conservation laws associated with the linearized field equation. Just as the electromagnetic equations (l8.10a,b) guarantee charge conservation

$$
J ^ { \mu } { } _ { , \mu } = 0 , \int _ { \mathrm { a l l s p a c e } } J ^ { 0 } ( t , x ) d x d y d z \equiv Q = \mathrm { c o n s t } ,
$$

so the gravitational equations (18.8a,b) guarantee conservation of the total 4-momentum and angular momentum of any body bounded by vacuum:

$$
T ^ { \mu \nu } { } _ { , \nu } = 0 ,
$$

$$
\int _ { \mathrm { b o d y } } T ^ { \mu 0 } ( t , x ) d x d y d z \equiv P ^ { \mu } = \mathrm { c o n s t } ;
$$

$$
( x ^ { \alpha } T ^ { \beta \mu } - x ^ { \beta } T ^ { \alpha \mu } ) _ { , \mu } = 0 ,
$$

$$
\int _ { \mathrm { b o d y } } \left( x ^ { \alpha } { \cal T } ^ { \beta 0 } - x ^ { \beta } { \cal T } ^ { \alpha 0 } \right) d x d y d z \equiv { \cal J } ^ { \alpha \beta } = \mathrm { c o n s t . }
$$

(See $\ S 5 . 1 1$ for the basic properties of angular momentum in special relativity. The angular momentum here is calculated relative to the origin of the coordinate system.) Now it is important that the stress-energy components $T ^ { \mu \nu }$ ，which appear in the linearized field equations (18.7) and in these conservation laws, are precisely the components one would calculate using special relativity (with $g _ { \mu \nu } = \eta _ { \mu \nu } )$ . As a result, the energy-momentum conservation formulated here contains no contributions or effects of gravity!From this one sees that linearized theory assumes that gravitational forces do no significant work. For example,energy losses due to gravitational radiation-damping forces are neglected by linearized theory. Similarly, conservation -of 4-momentum $^ { - } P ^ { \  \alpha }$ for each of the bodies acting as sources of $h _ { \mu \nu }$ means that each body moves along a geodesic of $\eta _ { \mu \nu }$ (straight lines in the nearly Lorentz coordinate system) rather than along a geodesic of $g _ { \mu \nu } = \eta _ { \mu \nu } + h _ { \mu \nu }$ Thus, linearized theory can be used to calculate the motion of test particles and felds, using $g _ { \mu \nu } = \eta _ { \mu \nu } + h _ { \mu \nu } ;$ but to include gravitational corrections to the motion of the sources themselves-to allow them to satisfy $T ^ { \mu \nu } { } _ { ; \nu } = 0$ rather than $T ^ { \mu \nu } { } _ { , \nu } = 0$ -one must reinsert into the field equations the nonlinear terms that linearized theory discards. (See,e.g. Chapter 20 on conservation laws; $\ S 8 3 6 . 9 \substack { - 3 6 . 1 1 }$ on the generation of gravitational waves and radiation reaction; and Chapter 39 on the post-Newtonian approximation.)

Limit on validity of linearized theory: gravity must not affect motions of sources significantly

The energy, momentum, and angular momentum radiated by gravitational waves in linearized theory can be calculated by special-relativistic methods analogous to those used in electromagnetic theory for electromagnetic waves [Fiertz and Pauli (1939)], but it will be more informative and powerful to use a fully gravitational approach (Chapters 35 and 36).

# Exercise 18.4. SPACETIME CURVATURE FOR A PLANE GRAVITATIONAL WAVE

Calculate the components of the Riemann curvature tensor [equations (18.9)] for the gravitational plane wave (18.ll). [Answer:

$$
\begin{array} { l } { { R _ { x 0 x 0 } = - R _ { y 0 y 0 } = - R _ { x 0 x z } = + R _ { y 0 y z } = + R _ { x z x z } = - R _ { y z y z } = - \frac { 1 } { 4 } ( \overline { { h } } _ { x x } - \overline { { h } } _ { y y } ) _ { , t t } ; } } \\ { { \ } } \\ { { R _ { x 0 y 0 } = - R _ { x 0 y z } = + R _ { z y z } = - R _ { x z y 0 } = - \frac { 1 } { 2 } \overline { { h } } _ { x y , t i } ; } } \end{array}
$$

all other components vanish except those obtainable from the above by the symmetries ${ \cal R } _ { \alpha \beta \gamma \delta } = { \cal R } _ { [ \alpha \beta ] [ \gamma \delta ] } = { \cal R } _ { \gamma \delta \alpha \beta } .$

# Exercise 18.5. A PRIMITIVE GRAVITATIONAL-WAVE DETECTOR (see Figure 18.1)

Two beads slide almost freely on a smooth stick; only slight friction impedes their sliding. The stick falls freely through spacetime,with its center moving along a geodesic and its ends attached to gyroscopes,so they do not rotate.The beads are positioned equidistant (distance $\textstyle { \frac { 1 } { 2 } } \left( { \mathfrak { L } } \right)$ from the stick's center. Plane gravitational waves [equation (l8.ll) and exercise 18.4]. impinging on the stick,push the beads back and forth("geodesic deviation”;“tidal gravitational forces").The resultant friction of beads on stick heats the stick;and the passage of the waves is detected by measuring the rise in stick temperature.\*(Of course,this is not the best of all conceivable designs!) Neglecting the effect of friction on the beads’ motion, calculate the proper distance separating them as a function of time. [Hints: Let $\pmb { \xi }$ be the separation between the beads; and let $\pmb { \mathscr { n } } = \pmb { \xi } / | \pmb { \xi } |$ be a unit vector that points along the stick in the stick's own rest frame.Then their separation has magnitude $i = \xi \cdot n$ The fact that the stick is nonrotating is embodied in a parallel-transport law for n. $\pmb { \bigtriangledown _ { \pmb { u } } } \pmb { n } = 0$ ("Fermi-Walker transport”of $\ S 8 6 . 5 , 6 . 6$ ,and l3.6 reduces to parallel transport,because the stick moves along a geodesic with $\begin{array} { r } { \pmb { a } = \pmb { \nabla } _ { \pmb { u } } \pmb { u } = 0 . } \end{array}$ )Thus,

$$
\begin{array} { r l } & { ~ d \ell / d \tau = \nabla _ { \boldsymbol { u } } ( \xi \cdot \boldsymbol { n } ) = ( \nabla _ { \boldsymbol { u } } \xi ) \cdot \boldsymbol { n } _ { \cdot - } } \\ & { ~ d ^ { 2 } \ell / d \tau ^ { 2 } = \nabla _ { \boldsymbol { u } } \nabla _ { \boldsymbol { u } } ( \xi \cdot \boldsymbol { n } ) = ( \nabla _ { \boldsymbol { u } } \nabla _ { \boldsymbol { u } } \xi ) \cdot \boldsymbol { n } , } \end{array}
$$

where $\tau$ is the stick's proper time. But $\yen 92$ is produced by the Riemann curvature of the wave (geodesic deviation):

$$
\nabla _ { u } \nabla _ { u } \xi = \mathrm { p r o j e c t i o n ~ a l o n g } \ n \ \mathrm { o f } \ [ - R i e m a n n \ ( . . . , u , \xi , u ) ] .
$$

(The geodesic-deviation forces perpendicular to the stick,i.e., perpendicular to $\pmb { n }$ ,are coun-

![](images/702ef4d9626c705a7fc3c251f18219baacac27092b4dbd3225218b73e535163f.jpg)  
Figure 18.1. A primitive detector for gravitational waves,consisting of a beaded stick with gyroscopes on its ends [Bondi (1957)].See exercise 18.5 for discussion.

terbalanced by_the stick's pushing back on the beads to stop them from passing through it-no penetration of matter by matter!） Thus,

$$
d ^ { 2 } \ell / d \tau ^ { 2 } = { } - R i e m a n n \ ( . . . , u , \xi , u ) \cdot n = { } - R i e m a n n \ ( n , u , \xi , u ) .
$$

Evaluate this acceleration in the stick's local Lorentz frame. Orient the coordinates so the waves propagate in the $\pmb { z }$ -direction and the stick's direction has components $n ^ { z } = \cos \theta$ ， $n ^ { x } = \sin \theta \cos \phi , n ^ { y } = \sin \theta \sin \phi .$ Solve the resulting differential equation for $\ell ( \tau ) . ]$ [Answer:

$$
\small  \{  =  \ell _ { 0 } [ 1 + \frac { 1 } { 4 } ( \overline { { h } } _ { x x } - \overline { { h } } _ { y y } ) \sin ^ { 2 } \theta \cos 2 \phi + \frac { 1 } { 2 } \overline { { h } } _ { x y } \sin ^ { 2 } \theta \sin 2 \phi ] , 
$$

where $\overline { { h } } _ { j k }$ are evaluated on the stick's world line $( x = y = z = 0$ ).Notice that,if the stick is oriented along the direction of wave propagation (if $\theta = 0$ ),the beads do not move.In this sense,the effect of the waves (geodesic deviation) is purely transverse.For further discussion, see $\ S 8 3 5 . 4$ to 35.6.]

# $\$ 18.4$ . NEARLY NEWTONIAN GRAVITATIONAL FIELDS

The general solution to the linearized field equations in Lorentz gauge [equations (18.8a,b)] lends itself to expression as a retarded integral of the form familiar from electromagnetic theory:

$$
\widetilde { h } _ { \mu \nu } ( t , x ) = \int \frac { 4 T _ { \mu \nu } ( t - | x - x ^ { \prime } | , x ^ { \prime } ) } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } .
$$

Retarded-integral solution of linearized field equation

The gravitational-wave aspects of this solution will be studied in Chapter 36. Here focus attention on a nearly Newtonian source: $T _ { 0 0 } \gg | T _ { 0 j } |$ ， $T _ { \mathrm { 0 0 } } \gg | T _ { j \star } |$ , and velocities slow enough that retardation is negligible. ln this case,(l8.14) reduces to

Newtonian gravity as a limit of linearized theory

$$
\begin{array} { r l r } { \overline { { h } } _ { 0 0 } = - 4 \phi , } & { { } } & { \widetilde { h } _ { 0 j } = \overline { { h } } _ { j k } = 0 . } \end{array}
$$

$$
\phi ( t , x ) = - \int { \frac { T _ { 0 0 } ( t , x ^ { \prime } ) } { | x - x ^ { \prime } | } } d ^ { 3 } x ^ { \prime } = \mathrm { { N e w t o n i a n } \ p o t e n t i a l } .
$$

The corresponding metric (18.8c) is

$$
\begin{array} { c } { { d s ^ { 2 } = - ( 1 + 2 \phi ) d t ^ { 2 } + ( 1 - 2 \phi ) ( d x ^ { 2 } + d \nu ^ { 2 } + d z ^ { 2 } ) } } \\ { { \approx - ( 1 - 2 M / r ) d t ^ { 2 } + ( 1 + 2 M / r ) ( d x ^ { 2 } + d y ^ { 2 } + d z ^ { 2 } ) } } \end{array}
$$

The errors in this metric are: (l) missing corrections of order $\varPhi ^ { 2 }$ due to nonlinearities of which linearized theory is oblivious; (2) missng corrections due to setting $\overline { { h } } _ { 0 j } = 0$ (these are of order $\overline { { h } } _ { 0 j } \sim \Phi v$ where $v \sim | T _ { 0 j } | / T _ { 0 0 }$ is a typical velocity in the source); (3) missing corrections due to seting $\overline { { h } } _ { j k } = \mathrm { ~ 0 ~ }$ [these are of order $\overline { { h } } _ { j k } \sim \varPhi ( | T _ { j k } | / T _ { 0 0 } ) ]$ In the solar system all these errors are $\sim 1 0 ^ { - 1 2 }$ ，whereas $\phi \sim 1 0 ^ { - 6 }$

Bending of light and gravitational redshift predicted by linearized theory

Passive correspondence with Newtonian theory demanded only that $g _ { 0 0 } =$ $- ( 1 + 2 \phi )$ ； see equation (l7.19). However, linearized theory determines all the metric coefficients,up to errors of ${ \sim } \phi v , { \sim } \phi ^ { 2 }$ ,and ${ \sim } \Phi ( | T _ { j k } | / T _ { 0 0 } )$ 、This is sufficient accuracy to predict correctly (fractional errors $\sim 1 0 ^ { - 6 }$ ）the bending of light and the gravitational redshift in the solar system,but not perihelion shifts.

# EXERCISES

# Exercise 18.6. BENDING OF LIGHT BY THE SUN

To high precision,the sun is static and spherical,so its external line element is (18.l5c) with $\dot { \pmb { \phi } } = - \pmb { M } / r$ i.e.,

$$
d s ^ { 2 } = { } - ( 1 - 2 M / r ) d t ^ { 2 } + ( 1 + 2 M / r ) ( d x ^ { 2 } + d y ^ { 2 } + d z ^ { 2 } )
$$

A photon moving in the equatorial plane $( z = 0$ ）of this curved spacetime gets deflected very slightly from the world line

$$
x = t , \qquad y = b \equiv \overleftarrow { \mathrm { * } } \mathrm { i m p a c t } \mathrm { p a r a m e t e r } , \mathrm { * } \qquad z = 0 .
$$

Calculate the amount of deflection as follows.

(a) Write down the geodesic equation (l6.4a) for the photon's world line,

$$
{ \frac { d p ^ { \alpha } } { d \lambda ^ { * } } } + { \Gamma ^ { \alpha } } _ { \beta \gamma } p ^ { \beta } p ^ { \gamma } = 0 .
$$

[Here $p = d / d \lambda ^ { * } = ( 4$ -momentum of photon) $\asymp$ (tangent vector to photon's null geodesic).] (b) By evaluating the connection coeffcients in the equatorial plane,and by using the approximate values, $| p ^ { y } | \ll p ^ { 0 } \approx p ^ { x }$ ,of the 4-momentum components corresponding to the approximate world line (l8.l7), show that

$$
{ \frac { d p ^ { \nu } } { d \lambda ^ { * } } } = { \frac { - 2 M b } { ( x ^ { 2 } + b ^ { 2 } ) ^ { 3 / 2 } } } p ^ { z } { \frac { d x } { d \lambda ^ { * } } } , \qquad p ^ { z } = p ^ { 0 } \biggl [ 1 + { \cal O } \left( { \frac { M } { b } } \right) \biggr ] = \mathrm { c o n s t } \biggl [ 1 + { \cal O } \left( { \frac { M } { b } } \right) \biggr ] .
$$

(c) Integrate this equation for $p ^ { \pmb { \nu } }$ assuming $p ^ { y } = 0$ at $x = - \infty$ (photon moving precisely in $_ { x }$ direction initially)； thereby obtain

$$
p ^ { \pmb { \nu } } ( x = + \infty ) = - \frac { 4 M } { b } p ^ { x } .
$$

(d) Show that this corresponds to deflection of light through the angle

$$
\begin{array} { r } { \Delta \phi = 4 M / b = 1 ^ { \prime \prime } . 7 5 ( R _ { \odot } / b ) , } \end{array}
$$

where $\scriptstyle R _ { \odot }$ is the radius of the sun. For a comparison of this prediction with experiment, see Box 40.1.

# Exercise 18.7. GRAVITATIONAL REDSHIFT

(a) Use the geodesic equation for a photon, written in the form

$$
d p _ { \mu } / d \lambda ^ { \ast } - { \Gamma ^ { \alpha } } _ { \mu \beta } p _ { \alpha } p ^ { \beta } = 0 ,
$$

to prove that any photon moving freely in the sun's gravitational field [line element (l8.16)] has $d p _ { \alpha } / d \lambda ^ { * } = 0$ ；ie.,

$$
p _ { 0 } = \mathrm { c o n s t a n t ~ a l o n g ~ p h o t o n } ^ { \prime } s \mathrm { w o r l d ~ l i n e } .
$$

(b) An atom at rest on the sun's surface emits a photon of wavelength $\lambda _ { e } .$ as seen in its orthonormal frame. [Note:

$$
h \nu _ { e } = h / \lambda _ { e } = ( \mathrm { e n e r g y ~ a t o m ~ m e a s u r e s } ) = - p \cdot u _ { e } ,
$$

where $\pmb { p }$ is the photon's 4-momentum and ${ \pmb u } _ { e }$ is the emitter's 4-velocity.] An atom at rest far from the sun receives the photon, and measures its wavelength to be $\lambda _ { r }$ [Note: $h / \lambda _ { r } =$ $- \pmb { p } \cdot \pmb { u } _ { r } ]$ Show that the photon is redshifted by the amount

$$
z \equiv \frac { \lambda _ { r } - \lambda _ { e } } { \lambda _ { e } } = \frac { M _ { \odot } } { R _ { \odot } } = 2 \times 1 0 ^ { - 6 } .
$$

$[ H i n t : { \pmb u } _ { r } = \hat { \sigma } / \hat { \sigma } t ; { \pmb u } _ { e } = ( 1 - 2 M / r ) ^ { - 1 / 2 } \hat { \sigma } / \hat { \sigma } t .$ Why?] For further discussion of the gravitational redshift and experimental results, see $\ S \ S 7 . 4$ and 38.5；also Figures 38.l and 38.2.

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

![](images/e1f9d00071049e96ce67bc7504d49d6b636dd1246c46ceafe34b60d8a83231b9.jpg)

![](images/b0e09a5f194ea80bc13687429e2238f5e673afed7cbecbc0d2bef0be1e4a3da9.jpg)

B.The asymptotic rest frame of the source is that global, asymptotically Lorentz frame (coordinates $t , x , y , z )$ in which the distant,“coulomb”part of the source's field is at rest (see diagram). The asymptotic rest frame does not extend into the strong-field region; any such extension of it would necessarily be forced by the curvature into a highly non-Lorentz, curvilinear form. The spatial origin of the asymptotic rest frame is so adjusted that the source is centered on it-i.e., that the distant Newtonian potential is $\phi = - M / ( x ^ { 2 } + y ^ { 2 } +$ $z ^ { 2 } ) ^ { 1 / 2 } + 0 ( 1 / r ^ { 3 } )$ ； i.e., that $\pmb { \phi }$ has no dipole term, $\pmb { D } \cdot \pmb { x } / r ^ { 3 }$ ， such as would originate from an offset of the coordinates.

C. To the source one can attribute a total mass-energy $M ,$ a 4-velocity $\pmb { U }$ a total 4-momentum $\pmb { P } ,$ .and an intrinsic angular momentum vector, S.The 4-vectors $\theta , P ,$ and $\pmb { s }$ reside in the asymptotically flat region of spacetime and can be moved about freely there (negligible curvature $\Longrightarrow$ parallel transport around closed curves does not change $\theta , P ,$ or $\pmb { s }$ ). The source's 4-velocity $\pmb { U }$ is defined to equal the 4-velocity of the asymptotic rest frame ( $U ^ { 0 } = 1$ ， $U = 0$ in rest frame). The total mass-energy $M$ is measured via Kepler's third (“1-2-3") law [equation (l9.8)]. The total 4-momentum is defined by $\pmb { P } \equiv M \pmb { U }$ .The intrinsic angular momentum $\pmb { S }$ is orthogonal to the 4-velocity $\pmb { U }$ ， $\pmb { S } \cdot \pmb { U } = 0$ (so $S ^ { 0 } = 0$ ； $s \neq 0$ in general in asymptotic rest frame); $s$ is measured via gyroscope precession or differential perihelion precession $( \ S ^ { 1 9 . 2 ) }$

In the asymptotic rest frame, with an appropriate choice of gauge (i.e., of ripples in the coordinates),the slight deviations from flat-spacetime geometry are described by the line element

$$
\begin{array} { l } { { d s ^ { 2 } = - \left[ 1 - \displaystyle \frac { 2 M } { r } + \displaystyle \frac { 2 M ^ { 2 } } { r ^ { 2 } } + 0 \left( \displaystyle \frac { 1 } { r ^ { 3 } } \right) \right] d t ^ { 2 } - \left[ 4 \epsilon _ { j k l } S ^ { k } \displaystyle \frac { x ^ { l } } { r ^ { 3 } } + 0 \left( \displaystyle \frac { 1 } { r ^ { 3 } } \right) \right] d t d x ^ { j } } } \\ { { + \left[ \left( 1 + \displaystyle \frac { 2 M } { r } + \displaystyle \frac { 3 M ^ { 2 } } { 2 r ^ { 2 } } \right) \delta _ { j k } + \mathrm { ( g r a v i t a t i o n a l ~ r a d i a t i o n ~ t e r m s ) } \right] d x ^ { j } d x ^ { k } . } } \end{array} \mathrm { ( ) }
$$

D. Conservation of 4-momentum and angular momentum: Suppose that particles fall into a source or are ejected from it; suppose that electromagnetic waves flow in and out; suppose the source emits gravitational waves. All such processes break the source's isolation and can change its total 4- momentum $\pmb { P } ,$ ,its intrinsic angular momentum S, and its asymptotic rest frame. Surround the source with a spherical shell $\textstyle { \mathcal { S } } _ { i }$ ，which is far enough out to be in the asymptotically flat region. Keep this shell always at rest in the source's momentary asymptotic rest frame. By probing the source's gravitational field near $s$ ，measure its 4-momentum $\pmb { P }$ and intrinsic angular momentum $\pmb { s }$ as functions of the shel's proper time $\boldsymbol { \mathsf { \tau } } .$ An analysis given in the next chapter reveals that the 4-momentum is conserved, in the sense that

![](images/6bb9d1ea1c003ac1c3941467c4862a80ff9ffbe01b21b83e8a13160f57826325.jpg)  
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

CHAPTER 20

# CONSERVATION LAWS FOR 4-MOMENTUM AND ANGULAR MOMENTUM

We denote as energy of a material system in a certain state the contribution of all effects (measured in mechanical units of work) produced outside the system when it passes in an arbitrary manner from its stete to e reference state which has been defined ad hoc.

WILLIAM THOMPSON (later Lord Kelvin). as quoted by Max von Laue in Schiipp (1949),p.514.

All forms of energy possess inertia.

Chapter 5 (stress-energy tensor) is needed as preparation for this chapter, which in turn is needed as preparation for the Track-2 portion of Chapter 36 (generation of gravitational waves) and will be useful in understanding Chapter 35 (propagation of gravitational waves).

# \$20.1.OVERVIEW

Chapter 19 expounded the key features of total 4-momentum $\pmb { P }$ and total angular momentum S for an arbitrary,gravitating system. But one crucial feature was left unproved: the conservation laws for $\pmb { P }$ and $\pmb { \mathsf { S } } \left( \pmb { \mathrm { B o x } } 1 9 . 1 \right)$ . To prove those conservation laws is the chief purpose of this chapter. But other interesting, if less important, aspects of $\pmb { P }$ and $\pmb { s }$ will be encountered along the route to the proof-Gaussian flux integrals for 4-momentum and angular momentum; a stress-energy “pseudotensor” for the gravitational field,which is a tool in constructing volume integrals for $\pmb { P }$ and S;and the nonlocalizability of the energy of the gravitational field.

# $\mathfrak { s } 2 0 . 2$ .GAUSSIAN FLUX INTEGRALS FOR 4-MOMENTUM AND ANGULAR MOMENTUM

In electromagnetic theory one can determine the conserved total charge of a source by adding up the number of electric field lines emanating from it-i.e., by performing a Gaussian flux integral over a closed 2-surface surrounding it:

Gaussian flux integrals for charge and Newtonian mass

$$
Q = \frac { 1 } { 4 \pi } \oint E ^ { j } d ^ { 2 } S _ { j } = \frac { 1 } { 4 \pi } \oint F ^ { 0 j } d ^ { 2 } S _ { j } .
$$

Similarly,in Newtonian theory one can determine the mass ofasource by evaluating the Gaussian flux integral

$$
M = \frac { 1 } { 4 \pi } \oint \phi _ { , j } d ^ { 2 } S _ { j } .
$$

These flux integrals work because the charge and mass of a source place indelible imprints on the electromagnetic and gravitational fields that envelop it.

The external gravitational field (spacetime geometry) in general relativity possesses similar imprints,imprints not only of the source's total mass-energy $M ,$ ,but also of its total 4-momentum $\pmb { P }$ and its intrinsic angular momentum $\pmb { s }$ (see Box 19.1).Hence, it is reasonable to search for Gaussian flux integrals that represent the 4-momentum and angular momentum of the source.

To simplify the search,carry it out initially in linearized theory,and use Maxwell electrodynamics as a guide. In electrodynamics the Gaussan flux integral for charge follows from Maxwell's equations $F ^ { \mu \nu } { } _ { , \nu } = 4 \pi J ^ { \mu }$ ，plus the crucial fact that $F ^ { \mu \nu }$ is antisymmetric, so that $F ^ { 0 \mu } { } _ { , \mu } = F ^ { 0 j } { } _ { , j }$

$$
\begin{array} { c } { { Q = \displaystyle { \int J ^ { 0 } d ^ { 3 } x = \frac { 1 } { 4 \pi } \int F ^ { 0 \nu } } , { d ^ { 3 } x = \displaystyle { \frac { 1 } { 4 \pi } \int F ^ { 0 j } } } } } \\ { { { } } } \\ { { \displaystyle { [ G \mathrm { a u s s } ^ { \prime } s \mathrm { ~ t h e o r e m } ] } } } \end{array} \nonumber
$$

To find analogous flux integrals in linearized theory,rewrite the linearized field equations (18.7) in an analogous form involving an entity with analogous crucial symmetries. The entity needed turns out to be

$$
H ^ { \mu \alpha \nu \beta } \equiv - ( \bar { h } ^ { \mu \nu } \eta ^ { \alpha \beta } + \eta ^ { \mu \nu } \overline { { { h } } } ^ { \alpha \beta } - \overline { { { h } } } ^ { \alpha \nu } \eta ^ { \mu \beta } - \overline { { { h } } } ^ { \mu \beta } \eta ^ { \alpha \nu } ) .
$$

As one readily verifies from this expression, it has the.same symmetries as the Riemann tensor

$$
\begin{array} { c } { { H ^ { \mu \alpha \nu \beta } = H ^ { \nu \beta \mu \alpha } = H ^ { \left[ \mu \alpha \right] \left\{ \nu \beta \right\} } , } } \\ { { H ^ { \mu \left[ \alpha \nu \beta \right] } = 0 . } } \end{array}
$$

This entity, like $\overline { { h } } ^ { \mu \nu }$ ，transforms as a tensor under the Lorentz transformations of linearized theory;but it is not gauge-invariant, so it is not a tensor in the general relativistic sense.

Linearized field equations in terms of $H ^ { \mu \alpha r \beta }$

In terms of $H ^ { \mu \alpha \nu \beta }$ ,the linearized field equations (18.7) take on the much simplified form

$$
2 G ^ { \mu \nu } = H ^ { \mu \alpha \nu \beta } { } _ { , \alpha \beta } = 1 6 \pi T ^ { \mu \nu } ;
$$

and from these, by antisymmetry of $H ^ { \mu \alpha \nu \beta }$ in $\pmb { \nu }$ and $\beta$ ,follow the source conservation laws of linearized theory,

$$
T ^ { \mu \nu } { } _ { , \nu } = \frac { 1 } { 1 6 \pi } H ^ { \mu \alpha \nu \beta } { } _ { , \alpha \beta \nu } = 0 ,
$$

Gaussian flux integrals in linearized theory: (1） for 4-momentum

which were discussed back in $\ S 1 8 . 3$ .The same antisymmetry as yields these equations of motion also produces a Gaussian flux integral for the source's total 4-momentum:

$$
{ \begin{array} { l } { { P ^ { \mu } = \displaystyle \int T ^ { \mu 0 } d ^ { 3 } x = \frac { 1 } { 1 6 \pi } \int H ^ { \mu \alpha 0 \beta } , \alpha \beta \ d ^ { 3 } x = \frac { 1 } { 1 6 \pi } \int H ^ { \mu \alpha 0 \beta } , _ { \alpha j } d ^ { 3 } x } } \\ { { } } \\ { { \frac { \displaystyle = \frac { 1 } { \displaystyle 1 6 \pi } \oint _ { \scriptstyle \mathscr { S } } H ^ { \mu \alpha 0 j } , \alpha \ d ^ { 2 } S _ { j } . } } } \\ { { \mathrm { ~ : ~ } } } \\ { { \mathrm { ~ : ~ } } } \end{array} }
$$

Here the closed 2-surface of integration $\mathcal { S }$ must completely surround the source and must lie in a 3-surface of constant time $x ^ { 0 }$ .The integral (20.6) for the source's energy $P ^ { 0 }$ ,which is used more frequently than the integrals for $P ^ { j }$ , reduces to an especially simple form in terms of $g _ { \alpha \beta } = \eta _ { \alpha \beta } + h _ { \alpha \beta }$

$$
P ^ { 0 } = \frac { 1 } { 1 6 \pi } \int _ { s } \left( g _ { j k , k } - g _ { k k , j } \right) d ^ { 2 } S _ { j }
$$

(2) for angular momentum

(see exercise 20.1).

A calculation similar to (20.6),but more lengthy (exercise 20.2)，yields a flux integral for total angular momentum about the origin of coordinates:

$$
\begin{array} { l } { { J ^ { \mu \nu } = \displaystyle \int \left( x ^ { \mu } T ^ { \nu 0 } - x ^ { \nu } T ^ { \mu 0 } \right) d ^ { 3 } x } } \\ { { \displaystyle \quad = \frac { 1 } { 1 6 \pi } \oint _ { s } \left( x ^ { \mu } H ^ { \nu \alpha 0 j } { } _ { , \alpha } - x ^ { \nu } H ^ { \mu \alpha 0 j } { } _ { , \alpha } + H ^ { \mu j 0 \nu } - H ^ { \nu j 0 \mu } \right) d ^ { 2 } S _ { j } . } } \end{array}
$$

Generalization of Gaussian flux integrals to full general relativity

To evaluate the flux integrals in (20.6) to (20.8) (by contrast with the volume integrals),one need utilize only the gravitational field far outside the source. Since that gravitational field has the same form in full general relativity for strong sources as in linearized theory for weak sources,the flux integrals can be used to calculate $P ^ { \mu }$ and $J ^ { \mu \nu }$ for any isolated source whatsoever, weak or strong:

$$
\left. \begin{array} { c } { { P ^ { \mu } = \displaystyle \frac { 1 } { 1 6 \pi } \oint _ { s } H ^ { \mu \alpha 0 { \boldsymbol { j } } } , \alpha ^ { d 2 } S _ { \boldsymbol { j } } , } } \\ { { { } } } \\ { { P ^ { 0 } = \displaystyle \frac { 1 } { 1 6 \pi } \oint _ { s } \left( g _ { { \boldsymbol j } h , k } - g _ { { \boldsymbol k } h , { \boldsymbol j } } \right) d ^ { 2 } S _ { \boldsymbol { j } } , } } \\ { { { } } } \\ { { J ^ { \mu \nu } = \displaystyle \frac { 1 } { 1 6 \pi } \oint _ { s } \left( x ^ { \mu } H ^ { \nu \alpha 0 { \boldsymbol { j } } } , \alpha - x ^ { \nu } H ^ { \mu \alpha 0 { \boldsymbol { j } } } , \alpha \right. } } \\ { { { } } } \\ { { \left. \qquad + \ H ^ { \mu { \boldsymbol j } 0 \nu } - H ^ { \nu { \boldsymbol j } 0 } \right) d ^ { 2 } S _ { \boldsymbol { j } } . } } \end{array} \right\}
$$

in full general relativity theory,for any isolated source, when the closed surface of integration $\mathcal { S }$ is in the asymptotically flat region surrounding the source,and when asymptotically Minkowskian coordinates are used.

Knowing $P ^ { \mu }$ and $J ^ { \mu \nu }$ ,one can calculate the source's total mass-energy $M$ and intrinsic angular momentum $S ^ { \mu }$ by the standard procedure of $\mathtt { B o x } 5 . 6$ ：

$$
M = ( - P ^ { \mu } P _ { \mu } ) ^ { 1 / 2 } ,
$$

$$
S _ { \rho } = \frac { 1 } { 2 } \epsilon _ { \mu \nu \sigma \rho } ( J ^ { \mu \nu } - Y ^ { \mu } P ^ { \nu } + Y ^ { \nu } P ^ { \mu } ) P ^ { \sigma } / M .
$$

Note especially that the integrands of the flux integrals (20.9) are not gauge-invariant. In any local inertial frame at an event ${ \mathcal { P } } _ { 0 } \left[ g _ { \mu \nu } ( { \mathcal { P } } _ { 0 } ) = \eta _ { \mu \nu } , g _ { \mu \nu , \alpha } ( { \mathcal { P } } _ { 0 } ) = 0 \right]$ they vanish, since

$$
g _ { \mu \nu , \alpha } = h _ { \mu \nu , \alpha } = 0 \Longrightarrow H ^ { \mu \nu \alpha \beta } { } _ { , \alpha } = 0 ; \qquad g _ { \mu \nu } = \eta _ { \mu \nu } \Longrightarrow H ^ { \mu \nu \alpha \beta } = 0 .
$$

This is reasonable behavior;their Newtonian analog,the integrand $\varPhi _ { , j } =$ (gravitational acceleration) of the Newtonian flux integral (20.2),similarly vanishes in local inertial frames.

Although the integrands of the flux integrals are not gauge-invariant, the total integrals $P ^ { \mu }$ (4-momentum) and $J ^ { \mu \nu }$ (angular momentum) most assuredly are! They have meaning and significance independent of any coordinate system and gauge. They are tensors in the asymptotically flat region surrounding the source.

The spacetime must be asymptotically flat if there is to be any possibility of defining energy and angular momentum. Only then can linearized theory be applied; and only on the principle that linearized theory applies far away can one justify using the flux integrals (20.9) in the full nonlinear theory. Nobody can compel a physicist to move in close to define'energy and angular momentum. He has no need to move in close; and he may have compelling motives not to: the internal structure of the sources may be inaccessible, incomprehensible, uninteresting，dangerous, expensively distant,or frightening. This requirement for far-away flatness is a remarkable feature of the flux integrals (20.9); it is also a decisive feature.Even the coordinates must be asymptotically Minkowskian; otherwise most formulas in this chapter fail or require modification.In particular,when evaluating the 4-momentum and angular momentum of a localized system, one must apply the flux integrals (20.9)only in asymptotically Minkowskian coordinates.If such coordinates do not exist (spacetime not flat at infinity), one must completely abandon the flux integrals,and the quantities that rely on them for definition: the total mass,momentum,and angular momentum of the gravitating source.In this connection, recall the discussion of $\ S 1 9 . 4$ It described,in physical terms,why “total mass-energy” is a limited concept, useful only when one adopts a limited viewpoint that ignores cosmology.(Compare “light ray" or “particle," concepts of enormous value, but concepts that break down when wave optics or wave mechanics enter significantly.)

Gaussian flux integrals valid only in asymptotically flat region of spacetime and in asymptotically Minkowskian coordinates

Summary: Attempts to use formulas (20.9) in ways that lose sight of the Minkowski boundary conditions (and especially simply adopting them unmodified in curvilinear coordinates） easily and unavoidably produce nonsense.