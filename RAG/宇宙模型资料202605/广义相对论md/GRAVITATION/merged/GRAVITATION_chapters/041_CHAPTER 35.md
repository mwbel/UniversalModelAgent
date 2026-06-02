# CHAPTER 35

# PROPAGATION OF GRAVITATIONAL WAVES

Born: "/ should like to put to Herr Einstein a question, namely. how quickly the action of gravitation is propagated in your theory. That it happens with the speed of light does not elucidate it to me. There must be a very complicated connection between these ideas."

Einstein: “It is extremely simple to write down the equations for the case when the perturbations that one introduces in the field are infinitely small. Then the g's differ only infinitesimally from those that would be present without the perturbation. The perturbations then propagate with the same velocity as light."

Born: "But for great perturbations things are surely very complicated?" Einstein:“Yes, it is a mathematically complicated problem. It is especially difficult to find exact solutions of the equations. as the equations are nonlinear."

# $\$ 35.1$ .VIEWPOINTS

Study one idealization after another. Build a catalog of idealizations,of their properties,of techniques for analyzing them. This is the only way to come to grips with so complicated a subject as general relativity!

Spherical symmetry is the idealization that has dominated most of the last 12 chapters. Together with the idealization of matter as a perfect fluid, and of the universe as homogeneous,it has yielded insight into stars, into cosmology,into gravitational collapse.

Turn attention now to an idealization of an entirely different type,one independent of any symmetry considerations at all: the idealization of a“gravitational wave.”

Just as one identifies as “water waves” small ripples rolling across the ocean, so one gives the name “gravitational waves” to small ripples rolling across spacetime.

Gravitational waves compared to water waves on ocean:

(1） approximate nature of awave

Ripples of what? Ripples in the shape of the ocean's surface; ripples in the shape (i.e.,curvature) of spacetime. Both types of waves are idealizations. One cannot, with infinite accuracy, delineate at any moment which drops of water are in the waves and which are in the underlying ocean: Similarly,one cannot delineate precisely which parts of the spacetime curvature are in the ripples and which are in the cosmological background. But one can almost do so; otherwise one would not speak of“waves"!

(2) local viewpoint vs. large-scale viewpoint

Look at the ocean from a rowboat. Waves dominate the seascape. Changes in angle and level of the surface occur every 30 feet or less. These changes propagate. They obey a simple wave equation

$$
\begin{array} { r } { \left( \frac { 1 } { g ^ { 2 } } \frac { \hat { \sigma } ^ { 4 } } { \partial t ^ { 4 } } + \frac { \hat { \sigma } ^ { 2 } } { \hat { \sigma } y ^ { 2 } } + \frac { \hat { \sigma } ^ { 2 } } { \hat { \sigma } x ^ { 2 } } \right) ( \mathrm { h e i g h t ~ o f ~ s u r f a c e } ) = 0 . } \end{array}
$$

Now get more sophisticated. Notice from a spaceship the large-scale curvature of the ocean's surface-curvature because the Earth is round, curvature because the sun and the moon pull on the water. As waves propagate long distances,this curvature bends their fronts and changes slightly their simple wave equation. Also important over large distance are nonlinear interactions between waves, interaction with the wind, Coriolis forces due to the Earth's rotation, etc.

Spacetime is similar. Propagating through the universe,according to Einstein's theory, must be a complex pattern of small-scale ripples in the spacetime curvature, ripples produced by binary stars,by supernovae, by gravitational colapse， by explosions in galactic nuclei. Locally ("rowboat viewpoint"） one can ignore the interaction of these ripples with the large-scale curvature of spacetime and their nonlinear interaction with each other. One can pretend the waves propagate in flat spacetime; and one can write down a simple wave equation for them. But globally one cannot. The large-scale curvature due to quiescent stars and galaxies will produce redshifts and will deform wave fronts; and the energy carried by the waves themselves will help to produce the large-scale curvature. This chapter treats both viewpoints,the local (ss35.2-6), and the global (Sg35.7-15).

# \$35.2. REVIEW OF "LINEARIZED THEORY" IN VACUUM

Linearized theory of gravitational waves:

Idealize, for awhile, the gravitational waves of our universe as propagating through flat, empty spacetime (local viewpoint). Then they can be analyzed using the “linearized theory of gravity,”which was introduced in Chapter 18.

Linearized theory,one recals, is a weak-field approximation to general relativity. The equations of linearized theory are written and solved as though spacetime were flat (special-relativity viewpoint); but the connection to experiment is made through the curved-space formalism of general relativity.

More specifically, linearized theory describes gravity by a symmetric,second-rank tensor field $\overline { { h } } _ { \mu \nu }$ . In the standard ("Lorentz,”or Hilbert） gauge, this field satisfies the“gauge”or “subsidiary” conditions (coordinate conditions)

$$
{ \overline { { h } } } { ^ { \mu \alpha } } { } _ { , \alpha } = 0 .
$$

(Here,and throughout linearized theory,indices of $\overline { { h } } _ { \mu \nu }$ are raised and lowered with the Minkowski metric $\eta _ { \alpha \beta }$ ） In this gauge the propagation equations for vacuum gravitational fields are the familiar wave equations

$$
\Pi _ { \mu \nu } \equiv \overline { { { h } } } _ { \mu \nu , \alpha } { } ^ { \alpha } = 0 .
$$

(2） propagation equation

Spacetime is really curved in linearized theory， although equations (35.l） are written and solved as though it were not. The global inertial frames of equations (35.1)are only almost inertial. In them the metric components are actually

$$
g _ { \mu \nu } = \eta _ { \mu \nu } + h _ { \mu \nu } + O ( [ h _ { \mu \nu } ] ^ { 2 } ) ;
$$

(3) metric

and the “metric perturbation" $h _ { \mu \nu }$ is related tothe“gravitationalfeld” $\overline { { h } } _ { \mu \nu }$ by

$$
\begin{array} { c } { { h _ { \mu \nu } = \overline { { { h } } } _ { \mu \nu } - \displaystyle \frac { 1 } { 2 } \overline { { { h } } } \eta _ { \mu \nu } , \qquad \overline { { { h } } } _ { \mu \nu } = h _ { \mu \nu } - \frac { 1 } { 2 } h \eta _ { \mu \nu } , } } \\ { { { } } } \\ { { h \equiv h _ { \alpha } { } ^ { \alpha } = - \overline { { { h } } } = - \overline { { { h } } } _ { \alpha } { } ^ { \alpha } . } } \end{array}
$$

The metric (35.2a) governs the motion of test particles, the propagation of light, etc., in the usual general-relativistic manner.

Recall the origin of the equations (35.1) that govern $\widehat { h } _ { \mu \nu }$ .The subsidiary conditions $\bar { h } _ { \mu } ^ { \alpha } { } _ { , \alpha } = 0$ wereosed equations in vacuum then reduced to $\bar { \bigtriangledown } \overline { { h } } _ { \mu \nu } = 0$

Actually,as was shown in Box 18.2,the coordinates of linearized theory are not fullyfixed bytheconditions $\overline { { h } } _ { \mu } { } ^ { \alpha } { } _ { , \alpha } = 0$ Thereremainsanambiguitybodiedin further “gauge changes” (infinitesimal coordinate transformations), $\xi _ { \mu } ,$ which satisfy a restrictive condition

(4)residual gauge, freedom

$$
\xi _ { \mu , \alpha } ^ { \alpha } = 0
$$

in order to preserve conditions (35.la). Then

$$
x ^ { \mu } { } _ { \mathrm { n e w } } = x ^ { \mu } { } _ { \mathrm { o l d } } + \xi ^ { \mu }
$$

is the coordinate transformation and

$$
\overline { { h } } _ { \mu \nu \mathrm { n e w } } = \overline { { h } } _ { \mu \nu \mathrm { o l d } } - \xi _ { \mu , \nu } - \xi _ { \nu , \mu } + \eta _ { \mu \nu } \xi ^ { \alpha } { } _ { , \alpha }
$$

is the gauge change. All this was derived and discussed in Chapter 18.

# $\$ 35.3$ . PLANE-WAVE SOLUTIONS IN LINEARIZED THEORY

The simplest of all solutions to the linearized equations $\overline { { { h } } } _ { \mu \nu , \alpha } { } ^ { \alpha } = \overline { { { h } } } _ { \mu , \alpha } { } ^ { \alpha } = 0$ is the monochromatic, plane-wave solution,

Monochromatic， plane wave

$$
\begin{array} { r } { \overline { { h } } _ { \mu \nu } = \Re [ A _ { \mu \nu } \exp { ( i k _ { \alpha } x ^ { \alpha } ) } ] . } \end{array}
$$

Here R[. ... .] means that one must take the real part of the expression in brackets; while $A _ { \mu \nu }$ (amplitude) and $k _ { \mu }$ (wave vector) are constants satisfying

$$
\begin{array} { r l } { k _ { \alpha } k ^ { \alpha } = 0 } & { { } \quad ( k \mathrm { ~ a ~ n u l l ~ v e c t o r } ) , } \\ { A _ { \mu \alpha } k ^ { \alpha } = 0 } & { { } \quad ( A \mathrm { ~ o r t h o g o n a l ~ t o ~ } k ) } \end{array}
$$

[consequences of $\overline { { h } } _ { \mu \nu , \alpha } { } ^ { \alpha } = 0$ and $\overline { { h } } _ { \mu , \alpha } ^ { \alpha } = 0$ respectivelyo physics associated with this wave,the curvature tensor]. Clearly, this solution describes a wave with frequency

$$
\omega \equiv k ^ { 0 } = ( k _ { x } ^ { ~ 2 } + k _ { y } ^ { ~ 2 } + k _ { z } ^ { ~ 2 } ) ^ { 1 / 2 } ,
$$

Plane wave has two degrees of freedom in amplitude (two polarizations)

which propagates with the speed of light in the direction $( 1 / k ^ { 0 } ) ( k _ { x } , k _ { y } , k _ { z } )$

At first sight the amplitude $A _ { \mu \nu }$ of this plane wave appears to have six independent components (ten,less the four orthogonality constraints $A _ { \mu \alpha } k ^ { \alpha } = 0 ) ,$ .But this cannot be right! As Track-2 readers have learned in Chapter 21, the gravitational field in general relativity has two dynamic degrees of freedom, not six. Where has the analysis gone astray?

One went astray by forgeting the arbitrariness tied up in the gauge freedom (35.3). The plane-wave vector

$$
\xi ^ { \mu } \equiv - i C ^ { \mu } \exp { ( i k _ { \alpha } x ^ { \alpha } ) } ,
$$

with four arbitrary constants $C ^ { \mu }$ , generates a gauge transformation that can change arbitrarily four of the six independent components of $A _ { \mu \nu }$ .One gets rid of this arbitrariness by choosing a specific gauge.

Transverse-traceless (TT) gauge:

(1) for plane wave

# $\$ 35.4$ .THE TRANSVERSE TRACELESS (TT) GAUGE

Select a 4-velocity $\pmb { u }$ --not at just one event,but the same $\pmb { u }$ throughout all of spacetime (special-relativistic viewpoint!). By.a specific gauge transformation (exercise 35.1),impose the conditions

$$
A _ { \mu \nu } u ^ { \nu } = 0 .
$$

These are only three constraints on $A _ { \mu \nu } { : }$ ,not four,because one of them- $k ^ { \mu } ( A _ { \mu \nu } u ^ { \nu } )$ $= 0$ -is already satisfied (35.4c). As a fourth constraint, use a gauge transformation (exercise 35.1) to set

$$
{ A ^ { \mu } } _ { \mu } = 0 .
$$

One now has eight constraints in all, $A _ { \mu \alpha } u ^ { \alpha } = A _ { \mu \alpha } k ^ { \alpha } = A _ { \alpha } { } ^ { \alpha } = 0 .$ ，on the ten components of the amplitude; and the coordinate system (gauge) is now fixed rigidly. Thus,the two remaining free components of $A _ { \mu \nu }$ represent the two degrees of freedom (two polarizations) in the plane gravitational wave.

It is useful to restate the eight constraints $A _ { \mu \alpha } u ^ { \alpha } = A _ { \mu \alpha } k ^ { \alpha } = A ^ { \mu } { } _ { \dot { \mu } } = 0$ in a Lorentz frame where $\smash { u ^ { 0 } = 1 }$ ， $u ^ { j } = 0$ ,and in a form where $k ^ { \alpha }$ does not appear explicitly:

$$
h _ { \mu 0 } = 0 ,
$$

$$
h _ { k j , j } = 0 ,
$$

$$
h _ { k k } = 0 ,
$$

(Here and henceforth repeated spatial indices are to be summed, even if both are down; e.g., $h _ { k k } \equiv \Sigma _ { k = 1 } ^ { 3 } h _ { k k } .$ ） Notice that, since $h = h _ { \mu } { } ^ { \mu } = h _ { k k } = 0$ ，there is no distinction between $h _ { \mu \nu }$ and $\overline { { h } } _ { \mu \nu }$ in this gauge.

Turn attention now away from plane waves to arbitrary gravitational waves in linearized theory. Any electromagnetic wave can be resolved into a superposition of plane waves,and so can any gravitational wave. For each plane wave in the superposition, introduce the special gauge (35.8). Note that the gauge conditions are all linear in $h _ { \mu \nu } .$ .Therefore the arbitrary wave will also satisfy conditions (35.8). Thus arises the theorem: Pick a specific global Lorentz frame of linearized theory (i.e., pick a specific 4-velocity $\pmb { u }$ ).Inthat frame (where $u ^ { \alpha } = \delta _ { \mathrm { ~ 0 ~ } } ^ { \alpha }$ ,examine a specific gravitational wave of arbitrary form. One can always find a gauge in which $h _ { \mu \nu }$ satisfies the constraints (35.8). Moreover, in this gauge only the $h _ { j k }$ are nonzero. Therefore, one need only impose the six wave equations

(2) for any wave

$$
\begin{array} { r } { \boxed { \ d } h _ { j k } = h _ { j k , \alpha ^ { ' } } \ d ^ { \alpha } = 0 . } \end{array}
$$

Any symmetric tensor satisfying constraints (35.8) [but not necessarily the wave equations (35.9)] is called a transverse-traceless $( T T )$ tensor—transverse because it is purely spatial $( h _ { 0 \mu } = 0 )$ and, if thought of as a wave,is transverse to its own direction of propagation $( h _ { i j , j } = h _ { i j } k _ { j } = 0 )$ ; traceless because $h _ { k k } = 0$ The most general purely spatial tensor $S _ { i j }$ can be decomposed [see Arnowitt, Deser,and Misner (1962) or Box 35.1] into a part $S _ { i j } ^ { T T }$ ，which is “transverse and traceless”； a part $S _ { i j } ^ { T } = \frac { 1 } { 2 } ( \delta _ { i j } f _ { , k k } - f _ { , i j } )$ , which is "transverse” $( S _ { i j , j } ^ { T } = 0 )$ but is determined entirely by one function $f$ giving the trace of $S \left( S _ { k k } ^ { T } = \nabla ^ { 2 } f \right)$ ; and a part $S _ { i j } ^ { L } = S _ { i , j } ^ { L } + S _ { j , i } ^ { L }$ , which is "longitudinal” and is determined by the vector field $S _ { i } ^ { L }$ In linearized theory $h _ { i j } ^ { L }$ is a purely gauge part of $h _ { \mu \nu }$ ，whereas $h _ { \mathrm { i } j } ^ { T }$ and $h _ { i j } ^ { T T }$ are gauge-invariant parts of $h _ { \mu \nu }$ The special gauge in which $h _ { \mu \nu }$ reduces to its transverse-traceless part is called the $_ { T T }$ or transverse-traceless gauge. The conditions (35.8) defining this gauge can be summarized as

Decomposition of spatial tensors

$$
h _ { \mu \nu } = h _ { \mu \nu } ^ { T T } .
$$

As exercise 35.2 illustrates,only pure waves (and not more general solutions of the linearized field equations with source, $\begin{array} { r } { \boxed { \ d h _ { \mu \nu } } = - 1 6 \pi T _ { \mu \nu } ) } \end{array}$ can be reduced to $_ { T T }$ gauge.

Curvature tensor in TT gauge

In the $T T$ gauge, the time-space components

$$
R _ { j 0 k 0 } = R _ { 0 j 0 k } = - R _ { j 0 0 k } = - R _ { 0 j k 0 }
$$

of the Riemann curvature tensor have an especially simple form [see equation (18.9) and exercise 18.4]:

$$
R _ { j 0 k 0 } = - \frac { 1 } { 2 } h _ { j k , 0 0 } ^ { T T } .
$$

Recall that the curvature tensor is gauge-invariant (exercise 18.1). It follows that $h _ { \mu \nu }$ cannot be reduced to still fewer components than it has in the $\mathit { T T }$ gauge.

$\mathbf { B o x } \ 3 5 . 1$ describes methods to calculate $h _ { \mu \nu } ^ { T T }$ from a knowledge of $h _ { \mu \nu }$ in some other gauge.

Problem: Let a gravitational wave $h _ { \mu \nu } ( t , x ^ { j } )$ in an arbitrary gauge of linearized theory be known. How can one calculate the metric perturbation $h _ { \mu \nu } ^ { T T } ( t , x ^ { j } )$ for this wave in the transverse-traceless gauge?

Solution $l$ (valid only for waves; i.e., when $\bigtriangledown \overline { { h } } _ { \mu \nu } = 0 \big$ Calculate the components $R _ { j 0 k 0 }$ of Riemann in the initial gauge; then integrate equation (35.10)

$$
h _ { j k , 0 0 } ^ { T T } = - 2 R _ { j 0 k 0 }
$$

to obtain $h _ { j k } ^ { T T }$ When the wave is monochromatic, $h _ { \mu \nu } = h _ { \mu \nu } ( \dot { x ^ { i } } ) e ^ { - i \omega t }$ ; then the solution of(l) has the simple form

$$
h _ { j k } ^ { T T } = 2 \omega ^ { - 2 } R _ { j 0 k 0 } .
$$

Solution 2 (valid only for plane waves).“Project out” the $T T$ components in an algebraic manner using the operator

$$
P _ { j k } = \delta _ { j k } - n _ { j } n _ { k } .
$$

Here

$$
n _ { k } = k _ { k } / | k |
$$

is the unit vector in the direction of propagation. Verify that $P _ { j k }$ is a projection operator onto the transverse plane:

$$
P _ { j \ell } P _ { \ell k } = P _ { j k } , \qquad P _ { j k } n _ { k } = 0 , \qquad P _ { k k } = 2 .
$$

Then the transverse part of $h _ { j k }$ is $P _ { j \ell } h _ { \ell m } P _ { m k }$ (or in matrix notation, $P h P$ )；and the $T T$ part is this quantity diminished by its trace:

$$
h _ { j k } ^ { T T } = P _ { j \ell } P _ { m k } h _ { i m } - \frac { 1 } { 2 } P _ { j k } ( P _ { m \ell } h _ { i m } )
$$

$$
\begin{array} { r } { h ^ { T T } = P \dot { R } P - \frac { 1 } { 2 } P \operatorname { T r } \left( P h \right) } \\ { ( \mathrm { m a t r i x ~ n o t a t i o n } ) . } \end{array}
$$

The sequence of operations that gives $h _ { \mathrm { i } j } ^ { T T }$ cuts two parts out of $h _ { i j } .$ The first part cut out is

$$
h _ { j k } ^ { T } = \frac { 1 } { 2 } { \cal P } _ { j k } ( { \cal P } _ { i m } h _ { \ell m } ) ,
$$

which is transverse but is built from its own trace,

$$
h ^ { T } \equiv \operatorname { T r } \left( P h P \right) = \operatorname { T r } \left( P h \right) = P _ { i m } h _ { m l } .
$$

# Exercise 35.1. TRANSFORMATION OF PLANE WAVE TO TT GAUGE

# EXERCISES

Let a plane wave of the form (35.4) be given, in some arbitrary gauge of linearized theory. Exhibit explicitly the transformation that puts it into the $_ { T T }$ gauge.[Hint:Work in a Lorentz frame where the 4-velocity $u ^ { \mu }$ of the $_ { T T }$ gauge is $u ^ { 0 } = 1$ ， ${ \pmb u } ^ { { \pmb j } } = { \pmb 0 }$ .Solve for the four constants $C ^ { \mu }$ of the generating function (35.6) by demanding that $\overline { { h } } _ { \mu \nu }$ satisfy the $_ { T T }$ constraints (35.7).]

# Exercise 35.2. LIMITATION ON EXISTENCE OF TT GAUGE

Although the metric perturbation $h _ { \mu \nu }$ for any gravitational wave in linearized theory can be put into the $_ { T T }$ form (35.8), nonradiative $h _ { \mu \nu } \mathrm { } ^ { \ast }$ cannot. Consider,for example,the external feld of a rotating,spherical star, which cannot be written as a superposition of plane waves:

The second part cut out of $h _ { i j }$ is the longitudinal part

$$
\begin{array} { r l } & { h ^ { L } { } _ { j k } = h _ { j k } - P _ { j \ell } P _ { m k } h _ { \ell m } } \\ & { \qquad = n _ { t } n _ { k } h _ { j l } + n _ { j } n _ { l } h _ { l k } - n _ { j } n _ { k } ( n _ { l } n _ { m } h _ { l m } ) ; } \end{array}
$$

or

$$
h ^ { L } = h - P h P
$$

Solution $^ 3$ (general case). Fourier analyze any symmetric array $h _ { i j } = \mathcal { I } h _ { i j } ( k , t )$ exp $( i k _ { m } x ^ { m } ) d ^ { 3 } k ,$ and apply the formulas (4) from solution 2 to each Fourier component individually. But note that in this case one can write the projection operator in the direction-independent form :

$$
P _ { j k } = \delta _ { j k } - { \frac { 1 } { \nabla ^ { 2 } } } \widehat { \partial } _ { j } \widehat { \partial } _ { k }
$$

or

$$
n _ { i } n _ { m } = \frac { 1 } { \bar { \Gamma } ^ { 2 } } \hat { v } _ { i } \hat { v } _ { m }
$$

(provided the formulas are written with all h's standing on the right),since $\widehat { \boldsymbol { o } } _ { \mathfrak { t } } = i \boldsymbol { k } _ { \mathfrak { t } }$ under the Fourier integral. Ofcourse the operation $1 / \nabla ^ { 2 }$ can be evaluated by other methods,e.g.,by Green's functions,as well as by Fourier analysis. [The quantity $\psi \equiv \nabla ^ { - 2 } f$ stands for the solution $\psi$ of the Poisson equation $\nabla ^ { 2 } \psi = f ]$ The advantage of this method is its power in certain analytic computations (see,e.g.,below).

Gauge Transformations. The change in $h _ { \mu \nu }$ due to a gauge transformation is

$$
\delta h _ { \mu \nu } = - ( \widehat { \sigma } _ { \nu } \xi _ { \mu } + \widehat { \sigma } _ { \mu } \xi _ { \nu } ) .
$$

The transverse part of this change is

$$
P _ { j l } P _ { k m } ( \delta h _ { i m } ) = - P _ { j l } P _ { k m } ( \hat { o } _ { l } \xi _ { m } + \hat { o } _ { m } \xi _ { l } ) = 0 .
$$

To verify this formula for a plane wave (solution 2), note that $\hat { v } _ { \ell } = i | k | n _ { \ell }$ and $P _ { j i } n _ { i } = 0$ . To verify the same result in general, use equation (7) to give the result

$$
P _ { j \pmb { \imath } } \partial _ { \pmb { \imath } } = 0 .
$$

Thus both $h _ { i j } ^ { T T }$ of equation (4), and $h _ { i j } ^ { T }$ of equation (5） are gauge-invariant:

$$
\delta h _ { i j } ^ { T T } = \delta h _ { i j } ^ { T } = 0 .
$$

In empty space ( $\mathbf { \nabla } _ { T _ { \mu \nu } } = 0 \mathbf { \nabla } _ { \mathbf { \mu } _ { \nu } }$ ，both $h _ { i j } ^ { T }$ and another gauge-invariant quantity $\widetilde { h } _ { 0 k }$ (discussed in exercise 35.4) vanish,by virtue of the field equations.

$$
\begin{array} { l } { \displaystyle h _ { 0 0 } = \frac { 2 M } { r } , \qquad h _ { j k } = \frac { 2 M } { r } \delta _ { j k } , \qquad h _ { 0 k } = - 2 \epsilon _ { k t m } \frac { S ^ { \displaystyle t } x ^ { \displaystyle m } } { r ^ { 3 } } , } \\ { \displaystyle r = ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 } } \end{array}
$$

[see equation (l9.5)].Here $M$ is the star's mass and $s$ is its angular momentum. Show that this cannot be put into $T T$ gauge. [Hint: Calculate $R _ { j 0 k 0 }$ and from it,by means of (35.10), infer $h _ { j k } ^ { T T }$ .Then calculate $R _ { 0 x y z }$ in both the original gauge and the new gauge,and discover that they disagree-not only by virtue of the mass term,but also by virtue of the angularmomentum term.]

# Exercise 35.3. A CYLINDRICAL GRAVITATIONAL WAVE

To restore one's faith,which may have been shaken by exercise 35.2,one can consider the radiative solution whose only nonvanishing component $h _ { \mu \nu }$ is

$$
\overline { { h } } _ { z z } = 4 A \cos { ( \omega t ) } J _ { 0 } ( \omega \sqrt { x ^ { 2 } + y ^ { 2 } } ) ,
$$

where $J _ { 0 }$ is the Bessel function.This solution represents a superposition of ingoing and Outgoing cylindrical gravitational waves.For this gravitational field calculate $R _ { j 0 k 0 } { : }$ and from it infer $h _ { j k } ^ { T T }$ Then calculate several other components of $R _ { \alpha \beta \gamma \delta }$ (e.g., $R _ { z y z y } )$ in the original gauge and in $T T$ gauge,and verify that the answers are the same.

# Exercise 35.4. NON-TT PARTS OF METRIC PERTURBATION [Track 2]

From $\mathbf { B o x } 3 5 . 1$ establish the formula $h ^ { T } = \bar { \Gamma } ^ { - 2 } ( h _ { \boldsymbol { k } \boldsymbol { k } , t \boldsymbol { \ell } } - h _ { \boldsymbol { k } \boldsymbol { t } , \boldsymbol { k } \boldsymbol { \ell } } )$ ； then verify the gauge invariance of $h ^ { T }$ directly,by showing that $h _ { k k , i \lambda } - h _ { k \ell , k \ell }$ is gauge-invariant. Use $\delta h _ { i j } = \xi _ { i , j } + \xi _ { j , i }$ Show similarly that the quantities $\widetilde { h } _ { 0 k }$ defined by

$$
\widetilde { h } _ { 0 k } = \overline { { h } } _ { 0 k } - \nabla ^ { - 2 } ( \overline { { h } } _ { 0 , \mu k } ^ { \mu } + \overline { { h } } _ { k \ell , \ell 0 } )
$$

are gauge-invariant. Show from the gauge-invariant linearized field equations (l8.5) that

$$
\begin{array} { r } { \nabla ^ { 2 } h ^ { T } = - 1 6 \pi T ^ { 0 0 } , } \\ { \nabla ^ { 2 } \widetilde { h } _ { 0 k } = - 1 6 \pi T _ { 0 k } , } \end{array}
$$

so $h ^ { T }$ and $\widetilde { h } _ { 0 k }$ must vanish for waves in empty space.

# \$35.5. GEODESIC DEVIATION IN A LINEARIZED GRAVITATIONAL WAVE

# Action of a gravitational wave on separation of two test particles

The oscillating curvature tensor of a gravitational wave produces oscillations in the separation between two neighboring test particles, $\pmb { A }$ and $\pmb { B }$ .Examine the oscillations from the viewpoint of $\pmb { A }$ .Use a coordinate system (“proper reference frame of $A ^ { \mathfrak { s } }$ ）， with spatial origin $x ^ { \hat { j } } = 0$ ,attached to A's world line (comoving coordinates)； with coordinate time equal to A's proper time ( $( x ^ { \hat { 0 } } = \tau$ on world line $x ^ { \widehat { j } } = 0 .$ )；and with orthonormal spatial axes attached to gyroscopes carried by $\pmb { A }$ ("nonrotating frame"). This coordinate system,appropriately specialized, is a local Lorentz frame not just at one event $\scriptstyle { \mathcal { P } } _ { 0 }$ on $\pmb { A } ^ { * } \pmb { \ s }$ geodesic world line,but all along A's world line:

$$
d s ^ { 2 } = - d x ^ { \hat { 0 } ^ { 2 } } + \delta _ { \hat { j } \hat { k } } ~ d x ^ { \hat { j } } d x ^ { \hat { k } } + ~ { \cal O } ( | x ^ { \hat { j } } | ^ { 2 } ) d x ^ { \hat { \alpha } } d x ^ { \hat { \beta } } .
$$

[Proof: such a “proper reference frame”was set up for accelerated particles in Track $2 ^ { \circ } { \ s \ } \ S 1 3 . 6$ . The line element (13.71) derived there, when specialized to particle $\pmb { A }$ $( a _ { \hat { j } } = 0$ because $\pmb { A }$ falls freely; $\omega ^ { \updownarrow } = 0$ because the spatial axes are attached to gyroscopes) reduces to the above form, as in equation (l3.73).]

As the gravitational wave passes, it produces an oscillating curvature tensor, which wiggles the separation vector $\pmb { n }$ reaching from particle $\pmb { A }$ to particle $\pmb { B }$ ：

$$
D ^ { 2 } n ^ { \hat { j } } / d \tau ^ { 2 } = - R ^ { \hat { j } } { } _ { \hat { 0 } \hat { k } \hat { 0 } } n ^ { \hat { k } } = - R _ { \hat { j } \hat { 0 } \hat { k } \hat { 0 } } n ^ { \hat { k } } .
$$

The components of the separation vector are nothing but the coordinates of particle $\pmb { B }$ , since particle $\pmb { A }$ is at the origin of its own proper reference frame; thus,

$$
n ^ { \widehat { j } } = x _ { B } ^ { ~ \widehat { j } } - x _ { A } ^ { ~ \widehat { j } } = x _ { B } ^ { ~ \widehat { j } } .
$$

Moreover, at $x ^ { \hat { \jmath } } = 0$ [where the calculation (35.12)isbeing perfored], the $T ^ { \hat { \mu } } { } _ { \hat { \alpha } \hat { \beta } }$ vanish for all $x ^ { \hat { 0 } }$ ; so $d { T ^ { \hat { \mu } } } _ { \hat { \alpha } \hat { \beta } } / d \tau$ also vanish. This eliminates all Christoffel-symbol corrections in $D ^ { 2 } n ^ { \hat { j } } / D \tau ^ { 2 }$ .Hence,equation (35.12) reduces to

$$
d ^ { 2 } x _ { B } ^ { \ \hat { j } } / d \tau ^ { 2 } = - R _ { \hat { j } \hat { 0 } \hat { k } \hat { 0 } } x _ { B } ^ { \ \hat { k } } .
$$

There is a $_ { T T }$ Coordinatesystemthat,tofrst order inthe metricperturbation $h _ { j k } ^ { T T }$ moves with particle $\pmb { A }$ andwithitsproerreferenceframeTostoderin $h _ { j k } ^ { T T }$ the $_ { T T }$ coordinate time $t$ is the same as proper time $\pmb { \tau }$ and $R _ { j 0 k 0 } ^ { T T } = R _ { \hat { j } \hat { 0 } \hat { k } \hat { 0 } }$ . Hence, equation (35.13) can be rewritten

$$
d ^ { 2 } x _ { B } ^ { \hat { j } } / d t ^ { 2 } = - R _ { j 0 k 0 } ^ { T T } { x _ { B } ^ { \hat { k } } } = { \frac { 1 } { 2 } } ( { \hat { \sigma } } ^ { 2 } h _ { j k } ^ { T T } / { \hat { \sigma } } t ^ { 2 } ) { x _ { B } ^ { \hat { k } } } .
$$

Suppose,for concreteness, that the particles are at rest relative to each other before the wave arrives $( x _ { B } ^ { \hat { j } } = x _ { B ( 0 ) } ^ { \hat { j } }$ when $h _ { j k } ^ { T T } = 0 .$ ). Then the equation of motion (35.14) can be integrated to yield

$$
x _ { B } { } ^ { \hat { j } } ( \tau ) = x _ { B ( 0 ) } { } ^ { \hat { k } } \bigg [ \delta _ { j k } + \frac { 1 } { 2 } h _ { j k } ^ { T T } \bigg ] _ { \mathrm { a t p o s i t i o n o f } A }
$$

This equation describes the wave-induced oscillations of $\pmb { B }$ 's location, as measured in the proper reference frame of $\pmb { A }$

Turn to the special case of a plane wave. Suppose the test-particle separation lies in the direction of propagation of the wave. Then the wave cannot affect the separation; there is no oscillation:

Transverse character of relative accelerations

$$
h _ { j k } ^ { T T } x _ { B ( 0 ) } { } ^ { \hat { k } } \propto h _ { j k } ^ { T T } k _ { k } = 0 .
$$

Only separations in the transverse direction oscillate; the wave is transverse not only in its mathematical description $( h _ { j k } ^ { T T } )$ ,but also in its physical effects (geodesic deviation)!

# EXERCISE

# ExerciSe 35.5. ALTERNATIVE CALCULATION OF RELATIVE OSCILLATIONS

Introduce a TT coordinate system in which,at time $t = 0$ ,the two particles are both at rest. Use the-geodesic equation to show that subsequently they both always remain at rest in the TTcoordinates. despite the action of the wave.This means that the contravariant components of the separation vector are always constant in the $T T$ coordinate frame:

$$
n ^ { j } = { x _ { B } } ^ { j } - { x _ { A } } ^ { j } = \mathrm { c o n s t . }
$$

Call this constant ${ { x } _ { B ( 0 ) } } ^ { j }$ .Transform these components to the comoving orthonormal frame;   
the answer should be equation (35.15).

# $\$ 35.6$ .POLARIZATION OF A PLANE WAVE

Polarization of gravitational waves:

(1）States of linear polarization,"+" and“×"

Geodesic deviation in the transverse direction provides a means for studying and characterizing the polarizations of plane waves.

Consider a plane, monochromatic wave propagating in the $\pmb { z }$ direction. In the $T T$ gauge the constraints $h _ { 0 \mu } ^ { T T } = 0 , h _ { i j , j } ^ { T T } \equiv i k _ { j } h _ { i j } ^ { \bar { T } T } = 0$ and $h _ { k k } ^ { T T } = 0$ reveal that the only nonvanishing components of $h _ { \mu \nu } ^ { T T }$ 'are

$$
\begin{array} { l } { h _ { x x } ^ { T T } = - h _ { y y } ^ { T T } = \Re \big \{ A _ { + } e ^ { - i \omega ( t - z ) } \big \} , } \\ { h _ { x y } ^ { T T } = h _ { y x } ^ { T T } = \Re \big \{ A _ { \times } e ^ { - i \omega ( t - z ) } \big \} . } \end{array}
$$

The amplitudes $A _ { + }$ and $A _ { \times }$ represent two independent modes of polarization.

As for electromagnetic plane waves (Figure 35.1), so also for gravitational plane waves (Figure 35.2), one can resolve a given wave into two linearly polarized components, or,alternatively, into two circularly polarized components.

<table><tr><td rowspan="2">w(t-z)</td><td colspan="4">Displacement, δx,for polarization</td></tr><tr><td>e</td><td>ey</td><td>eR</td><td>eL</td></tr><tr><td>2nm</td><td></td><td></td><td>！</td><td>?</td></tr><tr><td>(2n +)）</td><td></td><td>：</td><td>Λ</td><td>↑</td></tr><tr><td>（(2n + 1）m</td><td></td><td></td><td>?</td><td>绿</td></tr><tr><td>（2n+2）</td><td>1</td><td>！</td><td>1</td><td>+</td></tr></table>

$$
\pmb { A } = \Re \left[ A _ { 0 } e ^ { - \mathrm { i } \omega ( t - z ) } e _ { P } \right]
$$

Acceleration of a test charge:

$$
\begin{array} { c } { { { \pmb a } = ( q / m ) { \pmb E } = ( q / m ) ( - \hat { \alpha } { \pmb A } / \hat { \alpha } t ) } } \\ { { = \Re [ i \omega ( q / m ) A _ { 0 } e ^ { - \mathrm { i } \omega ( t - z ) } e _ { P } ] } } \end{array}
$$

Displacement of charge relative to inertial frame:

$$
\delta \mathbf { x } = \Re \left[ \frac { q / m } { i \omega } A _ { 0 } e ^ { - i \omega ( t - z ) } e _ { P } \right]
$$

For linearly polarized waves, the unit polarization vectors of electromagnetic theory are $e _ { x }$ and $\pmb { e } _ { \pmb { y } } .$ A test charge hit by a plane wave with polarization vector $\pmb { e } _ { \pmb { x } }$ oscillates in the x-direction relative to an inertial frame; and similarly for ey. By analogy, the unit linear-polarization tensors for gravitational waves are

$$
\begin{array} { r } { \pmb { e } _ { + } \equiv \pmb { e } _ { x } \otimes \pmb { e } _ { x } - \pmb { e } _ { y } \otimes \pmb { e } _ { y } , } \\ { \pmb { e } _ { \times } \equiv \pmb { e } _ { x } \otimes \pmb { e } _ { y } + \pmb { e } _ { y } \otimes \pmb { e } _ { x } . } \end{array}
$$

The plane wave (35.16), when $A _ { \times } = 0$ ,has polarization ${ \pmb e } _ { + }$ and can be rewritten

$$
h _ { j k } = \Re \{ A _ { + } e ^ { - i \omega ( t - z ) } e _ { + j k } \} .
$$

Its effect in altering the geodesic separation between two test particles depends on the direction of their separation. To see the effect in all directions at once, consider a circular ring of test particles in the transverse $( x , y )$ plane,surrounding a central particle (Figure 35.2). As the plane wave (35.18) (polarization ${ \pmb { e } } _ { + }$ ）passes,it deforms what was a ring as measured in the proper reference frame of the central particle into an ellipse with axes in the $x$ and $y$ directions that pulsate in and out:

$$
\textsf { O o o o o 0 0 0 0 0 0 0 } \textsf { O o o o o o 0 0 0 0 }
$$

etc. By contrast (Figure 35.2), a wave of polarization ${ \pmb e } _ { \times }$ deforms the ring at a 45-degree angle to the $x$ and $y$ directions: $\textsf { O O O O O O S O O O }$ etc.

For circularly polarized waves, the unit polarization vectors of electromagnetic theory are

(2) States of circular polarization

$$
e _ { R } = \frac { 1 } { \sqrt { 2 } } ( e _ { x } + i e _ { y } ) , e _ { L } = \frac { 1 } { \sqrt { 2 } } ( e _ { x } - i e _ { y } )
$$

$\pmb { e } _ { P }$

Metric perturbation:

$$
h _ { j k } = \Re \left[ A _ { 0 } e ^ { - i \omega ( t - z ) } e _ { P j k } \right]
$$

Tidal acceleration between two test particles:

<table><tr><td>w(t-z) e+</td><td colspan="3">Deformation of a ring of test particles ex eR eL</td></tr><tr><td>2nm</td><td></td><td></td><td></td><td></td></tr><tr><td>（2n+）</td><td></td><td></td><td></td><td></td></tr><tr><td>(2n + 1)</td><td></td><td></td><td></td><td></td></tr><tr><td>（2n+2）</td><td></td><td></td><td></td><td></td></tr></table>

$$
\begin{array} { c } { { \displaystyle \frac { D ^ { 2 } n _ { j } } { D \tau ^ { 2 } } = - R _ { j 0 k 0 } n _ { \hat { k } } = \frac { 1 } { 2 } \frac { \partial ^ { 2 } h _ { j k } } { \partial t ^ { 2 } } n _ { k } } } \\ { { = \Re \bigg [ - \frac { 1 } { 2 } \omega ^ { 2 } A _ { 0 } e ^ { - \mathrm { i } \omega ( t - z ) } e _ { P j k } n _ { \hat { k } } \bigg ] } } \end{array}
$$

Separation between two test particles:

$$
n _ { \mathrm { 3 } } = n _ { j } ^ { \mathrm { ( 0 ) } } + \Re \left[ \frac { 1 } { 2 } A _ { \mathrm { 0 } } e ^ { - \mathrm { i } \omega ( t - z ) } e _ { P j k } { n _ { \vec { k } } } ^ { \mathrm { ( 0 ) } } \right]
$$

Position of test particle $\pmb { B }$ in proper reference frame of test particle $\pmb { A }$ (In drawing, $\pmb { A }$ is the central particle and $\pmb { B }$ is any peripheral particle):

$$
{ x _ { B } } ^ { j } = { x _ { B ( 0 ) } } ^ { j } + \Re \left[ { \frac { 1 } { 2 } } { A _ { 0 } } e ^ { - i \omega ( t - z ) } { e _ { P j k } } { x _ { B ( 0 ) } } ^ { k } \right]
$$


<!-- chunk 0015: pages 981-1050 -->
Similarly, the unit circular polarization tensors of gravitation theory are

$$
{ \pmb e } _ { R } = \frac { 1 } { \sqrt { 2 } } ( { \pmb e } _ { + } + i { \pmb e } _ { \times } ) , \qquad e _ { L } = \frac { 1 } { \sqrt { 2 } } ( { \pmb e } _ { + } - i { \pmb e } _ { \times } ) .
$$

A test charge hit by an electromagnetic wave of polarization $\boldsymbol { e } _ { R }$ moves around and around in a circle in the righthanded direction (counterclockwise for a wave propagating toward the reader)； for $e _ { L }$ it circles in the lefthanded (clockwise) direction (see Figure 35.1). Similarly (Figure 35.2), a gravitational wave of polarization ${ \pmb { e } } _ { R }$ rotates the deformation of a test-particle ring in the righthanded direction,

$$
\circ \circ \ \mathcal { O } \ \mathrm { ~ 0 ~ } \ \circ \ \circ \ \circ \ \mathcal { O }
$$

while a wave of ${ \pmb { e } } _ { L }$ rotates it in the lefthanded direction.The individual test particles in the ring rotate in small circles relative to the central particle. However, just as the drops in an ocean wave do not move along with the wave, so the particles on the ring do not move around the central particle with the rotating ellipse.

Notice from Figure 35.2 that, at any moment of time, a gravitational wave is invariant under a rotation of $1 8 0 ^ { \circ }$ about its direction of propagation. The analogous angle for electromagnetic waves (Figure 35.1） is $3 6 0 ^ { \circ }$ ，and for neutrino waves it is $7 2 0 ^ { \circ }$ . This behavior is intimately related to the spin of the zero-mass particles associated with the quantum-mechanical versions of these waves: gravitons have spin 2,photons spin 1,and neutrinos spin $1 / 2$ . The classical radiation field of a spin- $s$ particle is always invariant under a rotation of $3 6 0 ^ { \circ } / S$ about its propagation direction.

A radiation field of any spin $s$ has precisely two orthogonal states of linear polarization. They are inclined to each other at an angle of $9 0 ^ { \circ } / S$ ；thus, for a neutrino field, with $\begin{array} { r } { S = \frac { 1 } { 2 } , } \end{array}$ the two states are distinguished as $1 + >$ and $| \downarrow >$ (spin up and spin down; $1 8 0 ^ { \circ }$ angle). For an electromagnetic wave $s = 1$ and two orthogonal states of polarization are $e _ { x }$ and $e _ { y }$ $9 0 ^ { \circ }$ angle). For a gravitational wave $s = 2$ ， and two orthogonal states are $\pmb { e } _ { + }$ and ${ \pmb { e } } _ { \times }$ $4 5 ^ { \circ }$ angle).

# EXERCISES

# ExerciSe 35.6. ROTATIONAL TRANSFORMATIONS FOR POLARIZATION STATES

Consider two Lorentz coordinate systems, one rotated by an angle $\pmb \theta$ about the $z$ direction relative to the other:

$$
t ^ { \prime } = t , \qquad x ^ { \prime } = x \cos \theta + y \sin \theta , \qquad y ^ { \prime } = y \cos \theta - x \sin \theta , \qquad z ^ { \prime } = z .
$$

Let $1 \nmid >$ and $| \downarrow >$ be quantum-mechanical states of a neutrino with spin-up and spin-down relative to the $x$ direction;and similarly for $1 4 ^ { \prime } >$ and $| \downarrow ^ { \prime } >$ . Let $e _ { z } , e _ { y } , e _ { z ^ { \prime } } , e _ { y ^ { \prime } }$ be the unit polarization vectors in the two coordinate systems for an electromagnetic wave traveling in the $_ { z }$ direction; and similarly ${ \pmb { e } } _ { + } , { \pmb { e } } _ { \times } , { \pmb { e } } _ { + } , { \pmb { e } } _ { \times } ,$ for a gravitational wave in linearized theory. Derive the following transformation laws:

$$
| \dagger \rangle = | \dagger > \cos \frac { 1 } { 2 } \theta + | \dagger > \sin \frac { 1 } { 2 } \theta ; \qquad | \dagger > = - | \dagger > \sin \frac { 1 } { 2 } \theta + | \dagger > \cos \frac { 1 } { 2 } \theta ;
$$

$$
e _ { x ^ { \prime } } = e _ { x } \cos \theta + e _ { y } \sin \theta ; \qquad e _ { y ^ { \prime } } = - e _ { x } \sin \theta + e _ { y } \cos \theta ;
$$

$$
\begin{array} { r } { \pmb { \varrho } _ { + ^ { \prime } } = \pmb { \varrho } _ { + } \cos 2 \theta + \pmb { \varrho } _ { \times } \sin 2 \theta ; \qquad \pmb { \varrho } _ { \times ^ { \prime } } = - \pmb { \varrho } _ { + } \sin 2 \theta + \pmb { \varrho } _ { \times } \cos 2 \theta . } \end{array}
$$

What is the generalization to the linear-polarization basis states for a radiation field of arbitrary spin S?

# Exercise 35.7. ELLIPTICAL POLARIZATION

Discuss elliptically polarized gravitational waves in a manner analogous to the discussion of linearly and circularly polarized waves in Figure 35.2.

# $\$ 35.7$ . THE STRESS-ENERGY CARRIED BY A GRAVITATIONAL WAVE

Exercise 18.5 showed that in principle one can build detectors which extract energy from gravitational waves. Hence, it is clear that the waves must carry energy.

Unfortunately, to derive and justify an expression for their energy requires a somewhat more sophisticated viewpoint than linearized theory. Such a viewpoint will be developed later in this chapter ( $\lbrace \ S \ S 3 5 . 1 3$ and 35.15).But for the benefit of Track-l readers, the key result is stated here.

Approximate localization of energy in a gravitational wave

In accordance with the discussions in $\ S \ S 1 9 . 4$ and 20.4, the stress-energy carried by gravitational waves cannot be localized inside a wavelength. One cannot say whether the energy is carried by the crest of a wave, by its trough, or by its “walls." However,one can say that a certain amount of stress-energy is contained in a given “macroscopic” region (region of several wavelengths’ size), and one can thus talk about a tensor for an effective smeared-out stress-energy of gravitational waves, $T _ { \mu \nu } ^ { ( \mathsf { G W } ) }$ Ina(nearlyineralframeoflinearized theory $\ddot { T } _ { \mu \nu } ^ { ( \mathrm { G W } ) }$ is given by

Effective stress-energy tensor for gravitational waves:

$$
\begin{array} { r l } { \cdots } & { { } T _ { \mu \nu } ^ { ( \mathrm { G W } ) } = \frac { 1 } { 3 2 \pi } \langle h _ { j k , \mu } ^ { T T } h _ { j k , \nu } ^ { T T } \rangle , } \end{array}
$$

(1)expressed in terms of metric perturbations

where $\langle ~ \rangle$ denotes an average over several wavelengths and $h _ { j k } ^ { T T }$ means the (gaugeinvariant) transverse-traceless part of $h _ { \mu \nu }$ ，which is simply $h _ { j k }$ in the $T T$ gauge. Another formula for $T _ { \mu \nu } ^ { ( \mathsf { G W } ) }$ valid in anyarbitrary gauge,with $\widehat { \bar { h } } \not = 0 , \overline { { { h } } } _ { \mu } { } _ { , \alpha } ^ { \alpha } \not = 0$ and $\overline { { h } } _ { 0 \mu } \neq 0$ is

$$
T _ { \mu \nu } ^ { ( \mathrm { G W } ) } = \frac { 1 } { 3 2 \pi } \left. \bar { h } _ { \alpha \beta , \mu } \bar { h } ^ { \alpha \beta } { } _ { , \nu } - \frac { 1 } { 2 } \bar { h } _ { , \mu } \bar { h } _ { , \nu } - \bar { h } ^ { \alpha \beta } { } _ { , \beta } \bar { h } _ { \alpha \mu , \nu } - \bar { h } ^ { \alpha \beta } { } _ { , \beta } \bar { h } _ { \alpha \nu , \mu } \right.
$$

This stress-energy tensor, like any other, is divergence-free in vacuum

$$
T ^ { ( { \tt G W } ) } { } _ { \mu } { } ^ { \nu } { } _ { , \nu } = 0 ;
$$

(2) subject to conservation law

and it contributes to the large-scale background curvature (which linearized theory ignores) just as any other stress-energy does:

$$
G _ { \mu \nu } ^ { ( \mathrm { B } ) } = 8 \pi ( T _ { \mu \nu } ^ { ( \mathrm { G W } ) } + T _ { \mu \nu } ^ { ( \mathrm { m a t t e r } ) } + T _ { \mu \nu } ^ { ( \mathrm { o t h e r f i e l d s } ) } ) .
$$

(3)role as source of background curvature

In writing here the term $T _ { \mu \nu } ^ { ( \mathsf { G W } ) }$ for the effective smeared-out energy density of the gravitational wave, one is foregoing any further insertion of the gravitational wave into the Einstein equation. Otherwise one might end up counting twice over the

(4) for a plane, monochromatic wave

contribution of the same wave to the background curvature of space, even though expressed in very different formalisms.

According to equation (35.23), the stress-energy tensor for the plane wave,

$$
h _ { \mu \nu } = \Re \big \{ ( A _ { + } e _ { + \mu \nu } + A _ { \times } e _ { \times \mu \nu } ) e ^ { - i \omega ( t - z ) } \big \} ,
$$

is

$$
T _ { t t } ^ { ( \mathrm { G W } ) } = T _ { z z } ^ { ( \mathrm { G W } ) } = - T _ { t z } ^ { ( \mathrm { G W } ) } = \frac { 1 } { 3 2 \pi } \omega ^ { 2 } ( | A _ { + } | ^ { 2 } + | A _ { \times } | ^ { 2 } ) .
$$

Notice that the background radius of curvature ${ \mathcal R }$ (ignored by linearized theory), and the mean reduced wavelength $\lambda$ （ ${ } = { }$ wavelength/ $2 \pi$ ）and amplitude $\boldsymbol { \mathcal { Q } }$ of the gravitational waves satisfy

Consequently,the dimensionlessnumbers $\boldsymbol { \mathcal { Q } }$ and $\pmb { \lambda } / \mathcal { R }$ are related by

$$
{ \mathcal { Q } } \lesssim \hbar / { \mathcal { R } } .
$$

Conditions for validity of gravitational-wave formalism

Thus,the whole concept of a small-scale ripple propagating in a background of large-scale curvature breaks down, and the whole formalism of this chapter becomes meaningless,if the dimensionless amplitude of the wave approaches unity. One must always have $\mathcal { Q } \ll l$ as well as $\lambda \ll \mathcal { R }$ if the concept of a gravitational wave is to make any sense!

# \$35.8. GRAVITATIONAL WAVES IN THE FULL THEORY OF GENERAL RELATIVITY

Nonlinear effects in gravitational waves:

Curving up of the background spacetime by the energy of the waves is but one of many new effects that enter, when one passes from linearized theory to the full, nonlinear general theory of relativity.

(1） radiation damping

In linearized theory one can consider a localized source of gravitational waves (e.g., a vibrating bar) in steady oscillation,radiating a strictly periodic wave. But the exact theory insists that the energy of the source decrease secularly,to counterbalance the energy carried off by the radiation (energy conservation; gravitational radiation damping； see $\ S \ S 3 6 . 8$ and 36.11). This makes an exactly periodic wave impossible, though a very nearly periodic one can certainly be emitted [Papapetrou (1958); Arnowitt, Deser,and Misner as reported by Misner (1964b)].

(2）refraction

In the real universe there are spacetime curvatures due not only to the energy of gravitational waves, but also, and more importantly, to the material content of the universe (planets, stars, gas, galaxies). As a gravitational wave propagates through these curvatures,its wave fronts change shape ("refraction"),its wavelength changes (gravitational redshift),and it backscatters off the curvatures to some extent. If the wave is a pulse, the backscatter will cause its shape and polarization to keep changing and will produce “tails” that spread out behind the moving pulse, traveling slower than light [see exercise 32.10; also Riesz (1949),DeWitt and Brehme (1960),DeWitt and DeWit (1964a), Kundt and Newman (1968), Couch et. al. (1968)j. However, so long as $\mathcal { Q } \ll 1$ and $\lambda / \mathcal { R } \ll 1$ ,these effects will be extremely small locally. They can only build up over distances of the order of $\mathcal { R }$ -and sometimes not even then.Thus, locally, linearized theory will remain highly accurate.

(3）redshift(4）backscatter(5） tails

Even in an idealized universe containing nothing but gravitational waves, backscatter and tails are produced by the interaction of the waves with the background curvature that they themselves produce.

If the reduced wavelength $\lambda = \lambda / 2 \pi$ and the mass-energy m of a pulse of waves satisfy $\lambda \leqslant m$ ,it is possible (in principle) to focus the pulse into a region of size $r < m$ ，whereupon a part of the energy of the pulse will undergo gravitational collapse to a singularity,leaving behind a black hole [see Ruffini and Wheeler (1970), and pp.7-24 of Christodoulou (1971)]. Short of a certain critical strength, no part of the pulse undergoes such a collapse.But it does undergo a time delay before reexpanding.This time delay is definable and measurable in the asymptotically flat space,far from the domain where the energy a litle earlier underwent temporary focusing into dimensions of order $\pmb { \lambda }$

All these effects can be analyzed in general relativity theory using approximation schemes which,in first order,are similar to or identical to linearized theory. Later in this chapter (Sg35.13-35.15), one such approximation scheme will be developed. But first it is helpful to study an exact solution that exhibits some of these effects.

(6) self-gravitational attraction

![](images/e7ddc8225e1778ce9525a791ba0db7512d71d024535b658475d1265068a0a4a3.jpg)

# $\$ 35.9$ . AN EXACT PLANE-WAVE SOLUTION

Any exact gravitational-wave solution that can be given in closed mathematical form must be highly idealized; otherwise it could not begin to cope with the complexities outlined above. Consequently,mathematically exact solutions are useful for pedagogical purposes only. However, pedogogy should not be condemned: it is needed not only by students,but also by veteran workers in the field of relativity,who even today are only beginning to develop intuition into the nonlinear regime of geometrodynamics!

The rest of this chapter is Track 2.No earlier Track-2 material is needed as preparation for it, but Chapter 20 (conservation laws) and $\$ 22.5$ (geometric optics) will be found to be helpful.It is not needed as preparation for any later chapter.

From the extensive literature on exact solutions, we have chosen, as a compromise between realism and complexity,the following plane wave[Bondi et.al.(1959), Ehlers and Kundt (1962)):

$$
\begin{array} { c } { { d s ^ { 2 } = L ^ { 2 } ( e ^ { 2 \beta } d x ^ { 2 } + e ^ { - 2 \beta } d y ^ { 2 } ) + d z ^ { 2 } - d t ^ { 2 } } } \\ { { = L ^ { 2 } ( e ^ { 2 \beta } d x ^ { 2 } + e ^ { - 2 \beta } d y ^ { 2 } ) - d u d v . } } \end{array}
$$

Exact plane-wave solution of vacuum field equation:

(1） form of metric

Here

$$
u = t - z , ~ v = t + z , ~ L = L ( u ) , ~ \beta = \beta ( u ) .
$$

The forms that the functions $L ( u )$ ("background factor") and $\beta ( u )$ ("wave factor") can take are determined by the vacuum field equations.In the null coordinate system $u , v . x , y ,$ the only component of the Ricci tensor that does not vanish identically is (see Box 14.4.allowing for the diference in coordinates. $2 v _ { \mathrm { t h e r e } } = v _ { \mathrm { h e r e } } )$

$$
{ \cal R } _ { u u } = - 2 L ^ { - 1 } [ L ^ { \prime \prime } + ( \beta ^ { \prime } ) ^ { 2 } L ] .
$$

(2） generation of"background factor" $\iota$ by"wave factor" $\beta$

where the prime denotes $d / d u$ .Thus, Einstein's equations in vacuum read

$$
L ^ { \prime \prime } + ( \beta ^ { \prime } ) ^ { 2 } L = 0 .
$$

(3)linearized limit

("effect of wave factor on background factor")

The linearized version of this equation is $L ^ { \prime \prime } = 0$ since $( \beta ^ { \prime } ) ^ { 2 }$ is a second-order quantity. Therefore the solution corresponding to linearized theory is

$$
L = 1 , \qquad \beta ( u ) \ \mathrm { a r b i t r a r y \ b u t \ s m a l l } .
$$

(4) special case:a plane-wave pulse

The corresponding metric is

$$
d s ^ { 2 } = ( 1 + 2 \beta ) d x ^ { 2 } + ( 1 - 2 \beta ) d y ^ { 2 } + d z ^ { 2 } - d t ^ { 2 } , ~ \beta = \beta ( t - z ) .
$$

Notice that this is a plane wave of polarization $\pmb { e } _ { + }$ propagating in the $z \cdot$ direction. (See exercise 35.10 at end of $\ S 3 5 . 1 2$ for the extension to a wave possessing both polarizations, ${ \pmb { e } } _ { + }$ and ${ \pmb { e } } _ { \times }$ ）

Return attention to the exact plane wave, and focus on the case where the“wave factor" $\beta ( u )$ is a pulse of duration $2 T ,$ and $| \beta ^ { \prime } | \ll 1 / T$ throughout the pulse. Then the exact solution (Figure 35.3) is: (1） for $u < - T$ (flat spacetime; pulse has not yet arrived),

$$
\beta = 0 , \qquad L = 1 ;
$$

(2) for $- T < u < + T$ (interior of pulse),

$\beta = \beta ( u )$ is arbitrary, except that $| \beta ^ { \prime } | \ll 1 / T ,$

$$
{ \cal L } ( u ) = 1 - \int _ { - T } ^ { u } \biggl \{ \int _ { - T } ^ { \overline { { { u } } } } [ \beta ^ { \prime } ( \overline { { { u } } } ) ] ^ { 2 } d \overline { { { u } } } \biggr \} d \overline { { { u } } } + { \cal O } ( [ \beta ^ { \prime } T ] ^ { 4 } ) ;
$$

(3) for $u \geq T$ (after the pulse has passed),

$$
\beta = 0 , \qquad L = 1 - \frac { u } { a } , \qquad a \equiv \frac { 1 } { \int _ { - T } ^ { T } ( \beta ^ { \prime } ) ^ { 2 } d u } + \frac { O ( [ \beta ^ { \prime } T ] ^ { 2 } ) } { \int _ { - T } ^ { T } ( \beta ^ { \prime } ) ^ { 2 } d u } .
$$

Before discussing the physical interpretation of this exact solution, one must come to grips with the singularity in the metric coefficients at $u = a \gg T .$ (There $L = 0$ ， so $g _ { x x } = g _ { y y } = 0 .$ ）Is this a physical singularity like the region $r = 0$ of the Schwarzschild geometry,or is it merely a coordinate singularity as $r = 2 M$ is in Schwarzschild coordinates (Chapters 31, 32,and 33)? The only nonzero components of the Riemann tensor for the metric (35.29) are (see Box l4.4)

![](images/32bd6d0ca996d9b57616dd91bbb139969d7a569628c2da7546e5999c351f7cdf.jpg)  
Figure 35.3. Spacetime diagram and pulse profile for an exact plane-wave solution to Einstein's vacuum feld equations. The metric has the form

$$
d s ^ { 2 } = L ^ { 2 } ( e ^ { 2 \beta } d x ^ { 2 } + e ^ { - 2 \beta } d y ^ { 2 } ) + d z ^ { 2 } - d t ^ { 2 } .
$$

The“wave factor” $\beta ( u ) \equiv \beta ( t - z )$ (short-scale ripples） and the“background factor” $L ( u ) \equiv L ( t - z )$ (large-scale bending of the background geometry by the effective mass-energy of the“ripply gravitational wave) are shown in the drawing and are given analytically by equations (35.33).

$$
\begin{array} { l } { { \displaystyle R ^ { x } { } _ { u x u } = \frac 1 2 R _ { u u } - \beta ^ { \prime \prime } - 2 ( L ^ { \prime } / L ) \beta ^ { \prime } , } } \\ { { \displaystyle R ^ { y } { } _ { u y u } = \frac 1 2 R _ { u u } + \beta ^ { \prime \prime } + 2 ( L ^ { \prime } / L ) \beta ^ { \prime } . } } \end{array}
$$

Moreover, these components both vanish in any extended region where $\beta = 0$ .Thus, spacetime is completely flat in regions where the “wave factor’ vanishes-which is everywhere outside the pulse！ In particular, spacetime is flat near $u = a$ so the singularity there must be a coordinate singularity，not a physical singularity. To eliminate this singularity,one can perform the coordinate transformation

$$
\cdot x = { \frac { X } { 1 - U / a } } , \qquad y = { \frac { Y } { 1 - U / a } } , \qquad u = U , \qquad v = V + { \frac { X ^ { 2 } + Y ^ { 2 } } { a - U } }
$$

throughout the region to the future of the pulse $( u > T )$ ， where

(5) spacetime is flat outside the pulse

$$
d s ^ { 2 } = ( 1 - u / a ) ^ { 2 } ( d x ^ { 2 } + d y ^ { 2 } ) - d u d v .
$$

In the new $X , Y , U , V .$ coordinates the metric has the explicitly flat form

$$
d s ^ { 2 } = d X ^ { 2 } + d Y ^ { 2 } - d U d V \qquad { \mathrm { f o r ~ } } U = u > T .
$$

# EXERCISES

# ExerciSe 35.8. GLOBALLY WELL-BEHAVED COORDINATES FOR PLANE WAVE [based on Ehlers and Kundt (1962)]

Find a coordinate transformation similar to (35.35), which puts the exact plane-wave solutior (35.29a), (35.31),into the form

$$
d s ^ { 2 } = d X ^ { 2 } + d Y ^ { 2 } - d U d V + ( X ^ { 2 } - Y ^ { 2 } ) F d U ^ { 2 } ,
$$

This coordinate system has the advantage of no coordinate singularities anywhere; while the original coordinate system has the advantages of an easy transition to linearized theory, and easy interpretation of the action of the wave on test particles.

# ExerciSe 35.9. GEODESIC COMPLETENESS FOR PLANE-WAVE MANIFOLD [based on Ehlers and Kundt (1962)]

Prove that the coordinate system $( X , Y , U , V )$ of exercise 35.8 completely covers its spacetime manifold. More specifically,show that every geodesic can be extended in both directions for an arbitrarily large affine-parameter length without leaving the $X , Y , U , V$ coordinate system.(This property is called geodesic completeness.) [Hint: Choose an arbitrary event and an arbitrary tangent vector $d / d \lambda$ there.They determine an arbitrary geodesic.Perform a coordinate transformation that leaves the form of the metric unchanged and puts $d / d \lambda$ either in the $( \widetilde { U } , \widetilde { V } ) =$ constant 2-surface, or in the $\widetilde { X } , \widetilde { Y } ) =$ constant 2-surface. Verify that the two coordinate systems cover the same region of spacetime.Then analyze completeness of $d / d \lambda ^ { \prime } s$ geodesic in $( \widetilde { X } , \widetilde { Y } , \widetilde { U } , \widetilde { V } )$ coordinates.]

# S35.10. PHYSICAL PROPERTIES OF THE EXACT PLANE WAVE

Spacetime is completely flat both before the arrival of the plane-wave pulse $( u < - T )$ and after it has passed $( u > T )$ . This is the message of the last paragraph.

Flatness outside   
gravitational-wave pulses is   
unusual

Complete flatness outside the pulse is very atypical for gravitational waves in the full, nonlinear general theory of relativity. It occurs in this example only because the wave fronts (surfaces of constant $\pmb { u }$ and $v$ ,i.e., constant $_ z$ and $t$ ）are perfectly flat 2-surfaces. If the wave fronts were bent (e.g., spherical), the energy carried by the pulse would produce spacetime curvature outside it.

Action of exact   
gravitational-wave pulse on   
test particles:

To see nonlinear effects in action, turn from the fat geometry outside the pulse to the action of the pulse on freely falling test particles. Consider a family of particles that are all at rest in the original $t , x , y , z$ coordinate system (world lines: $[ x , y , z ]$ $=$ constant) before the pulse arrives.Then even while the pulse is passing, and after it has gone, the particles remain at rest in the coordinate system.(This is true for any metric,such as (35.29a), with $g _ { 0 \mu } = - \delta ^ { 0 } { } _ { \mu }$ ，for then $T ^ { \mu } { } _ { 0 0 } = 0$ ，so $x ^ { \mu } = \delta ^ { \mu } { } _ { 0 } \tau +$ const. satisfies the geodesic equation.)

Two particles whose separation is in the direction of propagation of the pulse $z$ -direction) have not only constant coordinate separation, $\varDelta x = \varDelta y = 0$ and $\varDelta z \neq 0$ ； they also have constant proper separation, $\Delta s = { g _ { z z } } ^ { 1 / 2 } \ : { \cal { \Delta } } z = { \cal { \Delta } } z$ Hence, the exact plane wave is completely transverse, like a plane wave of linearized theory.

Neighboring particles transverse to the propagation direction, $( \pmb { \mathscr { s } } \neq 0 , \pmb { \mathscr { s } } \neq 0 ,$ $\begin{array} { r } { { \varDelta } z = 0 } \end{array}$ ) have a proper separation that wiggles as the pulse passes:

$$
\begin{array} { l } { { A s = L ( t - z ) [ e ^ { 2 \beta ( t - z ) } ( A x ) ^ { 2 } + e ^ { - 2 \beta ( t - z ) } ( A y ) ^ { 2 } ] ^ { 1 / 2 } } } \\ { { \ \approx L [ ( 1 + 2 \beta ) ( A x ) ^ { 2 } + ( 1 - 2 \beta ) ( A y ) ^ { 2 } ] ^ { 1 / 2 } . } } \end{array}
$$

(1）transverse character of reiative accelerations

Superimposed on the usual linearized-theory type of wiggling,due to the “wave factor" $\beta$ , is a very small net acceleration of the particles toward each other, due to the “background factor” $L$ [note the form of $L ( u )$ in Figure 35.3].This is an acceleration of almost Newtonian type, caused by the gravitational attraction of the energy that the gravitational wave carries between the two particles.The total effect of all the energy that passes is to convert the particles from an initial state of relative rest, to a final state of relative motion with speed

$$
v _ { \mathrm { f i n a l } } = d A s / d t = d ( L A s _ { i } ) / d t = - A s _ { i } / a ,
$$

(2）gravitational attraction due to energy in puise

where

$$
A s _ { i } = [ ( A x ) ^ { 2 } \stackrel { * } { + } ( A y ) ^ { 2 } ] ^ { 1 / 2 } = ( \mathrm { i n i t i a l ~ p a r t i c l e ~ s e p a r a t i o n } ) .
$$

[Recall: $L _ { \mathrm { i n i t i a l } } = 1$ ， $L _ { \mathrm { t i n a l } } = 1 - u / a = 1 - ( t - z ) / a ;$ equation (35.33).]

Precisely the same efect can be produced by a pulse of electromagnetic waves (835.11).

# $\$ 35.11$ . COMPARISON OF AN EXACT ELECTROMAGNETIC PLANE WAVE WITH THE GRAVITATIONAL PLANE WAVE

Consider the metric

$$
d s ^ { 2 } = L ^ { 2 } ( u ) ( d x ^ { 2 } + d y ^ { 2 } ) - d u d v , \qquad \left\{ { u = t - z \atop v = t + z } \right\} ,
$$

which is always flat if it satisfies the vacuum Einstein equations $( R _ { \mu \nu } = 0$ or $L ^ { \prime \prime } = 0$ ）， and therefore cannot represent a gravitational wave.In this metric the electromagnetic potential

An electromagnetic plane-wave pulse

$$
A = A _ { \mu } d x ^ { \mu } = { \mathcal { A } } ( u ) d x
$$

satisfies Maxwel's equations for arbitrary $\mathcal { A } ( u )$ . It represents an electromagnetic plane wave analogous to the gravitational plane wave of the last few sections. The only nonzero field components of this wave are

$$
F _ { u x } = \mathcal { A } ^ { \prime } , \mathrm { i . e . , } F _ { t x } = - F _ { z x } = \mathcal { A } ^ { \prime } ;
$$

so the electric vector oscillates back and forth in the $x$ direction, the magnetic vector oscillates in the $y \mathrm { \cdot }$ -direction,and the wave propagates in the $z \cdot$ direction. The stressenergy tensor in $x , y , u , v .$ ，coordinates has only

$$
T _ { u u } = ( 4 \pi L ^ { 2 } ) ^ { - 1 } ( \mathcal { A } ^ { \prime } ) ^ { 2 }
$$

Electromagnetic plane wave and gravitational plane wave produce same gravitational attractions

nonzero.

The Maxwell equations are already satisfied by the potential (35.41) in the background metric (35.40),as the reader can verify. In order to make that metric itself equally acceptable, one need only impose the Einstein equations $G _ { \mu \nu } = 8 \pi T _ { \mu \nu }$ . They read [see equation (35.30) with $\beta = 0$

$$
L ^ { \prime \prime } + ( 4 \pi T _ { u u } ) L = 0 .
$$

This has exactly the form of the equation $L ^ { \prime \prime } + ( \beta ^ { \prime } ) ^ { 2 } L = 0$ for the gravitational plane wave. Consequently, the relative motions of uncharged test particles produced by the “background factor” $L ( u )$ are the same whether $L ( u ) \neq 1$ is produced by the stress-energy of an electromagnetic wave, or by a corresponding gravitational wave with

$$
[ ( \beta ^ { \prime } ) ^ { 2 } / 4 \pi ] _ { \mathrm { g r a v w a v e } } = [ T _ { u u } ] _ { \mathrm { e m w a v e } } = ( \mathcal { A } ^ { \prime } ) ^ { 2 } / 4 \pi L ^ { 2 } .
$$

The analogy can be made even closer. Decrease the wavelength of the waves, while holding $( \beta ^ { \prime } ) ^ { 2 } / 4 \pi$ and $( \mathcal { A } ^ { \prime } ) ^ { 2 } / 4 \pi L ^ { 2 }$ fixed:

$$
\langle ( \beta ^ { \prime } ) ^ { 2 } / 4 \pi \rangle = \langle ( \mathcal { A } ^ { \prime } ) ^ { 2 } / 4 \pi L ^ { 2 } \rangle = \mathrm { c o n s t } ; \qquad \lambda \longrightarrow 0 .
$$

In the limit of very small wavelength (i.e., from a viewpoint whose characteristic length is $\gg \pmb { \chi }$ ),the two solutions are completely indistinguishable.Their metrics are identical ( $\dot { x } \longrightarrow 0$ and $\langle { ( \beta ^ { \prime } ) ^ { 2 } } \rangle =$ const. imply $\beta \longrightarrow 0 \mathrm { \large ~ . ~ }$ ),and their jigglings of test particles are too small to be seen. Only their curving up of spacetime $( L \neq 1 )$ and the associated gravitational pull of their energy are detectable.

Exact gravitational plane waves reexamined in the language of \`short-wave approximation":

(1） ripples vs.background

# \$35.12. A NEW VIEWPOINT ON THE EXACT PLANE WAVE

The above comparison suggests a viewpoint that was sketched briefly in the introduction to this chapter and in $\ S 3 5 . 8$ . Think of the exact gravitational plane-wave solution [Figure 35.3；equations (35.29) and (35.33)] as ripples in the spacetime curvature, described by $\beta ( u )$ ，propagating on a very slightly curved background spacetime,characterized by $\boldsymbol { L } ( u )$ .The most striking difference between the background and the ripples is not in the magnitude of their spacetime curvatures,but in their characteristic lengths.The ripples have characteristic length

$$
\lambda \equiv ( \mathrm { t y p i c a l ~ r e d u c e d ~ w a v e l e n g t h } , \lambda / 2 \pi , \mathrm { o f ~ w a v e s } ) ;
$$

the background has characteristic length ("radius of curvature of background geometry")

$$
{ \mathcal R } \sim | L / L ^ { \prime \prime } | ^ { 1 / 2 } _ { \mathrm { i n s i d e w a v e } } \sim 1 / | \beta ^ { \prime } | .
$$

Recall that $\pmb { \lambda }$ is somewhat smaller than the pulse length, $2 T .$ Recall also that $| \beta ^ { \prime } T | \ll 1$ . Conclude that the characteristic lengths of the“wave factor” and the “background factor” differ greatly:

$$
\lambda \ll \mathcal { R } .
$$

This difference in scales enables one to separate out the background from the ripples.

The ripples are very much smaller in scale $( \lambda \ll \mathcal { R } )$ than the background. Nevertheless the local curvature in a ripple is correspondingly larger than the background curvature [equations (35.30), (35.34); thu,

$$
( R ^ { x } { } _ { u x u } ) _ { \mathrm { b a c k g r o u n d } } = ( R ^ { y } { } _ { u y u } ) _ { \mathrm { b a c k g r o u n d } } = - L ^ { \prime \prime } / L \sim 1 / \mathcal { R } ^ { 2 } ,
$$

$$
\begin{array} { r } { ( R ^ { x } { } _ { u x u } ) _ { \mathrm { w a v e s } } = - ( R ^ { y } { } _ { u y u } ) _ { \mathrm { w a v e s } } = - \beta ^ { \prime \prime } \sim | \beta ^ { \prime } | / \lambda \sim 1 / ( \lambda \mathcal { R } ) } \\ { \sim ( \mathcal { R } / \lambda ) ( R ^ { x } { } _ { u x u } ) _ { \mathrm { b a c k g r o u n d } } . } \end{array}
$$

One is reminded of the motted surface of an orange!

The metric for the background of the gravitational plane wave is the same as for the electromagnetic one [equation (35.40):

$$
d s ^ { 2 } = g _ { \mu \nu } ^ { ( \mathrm { \scriptsize { B } } ) } d x ^ { \mu } d x ^ { \nu } = L ^ { 2 } ( d x ^ { 2 } + d y ^ { 2 } ) - d u d v .
$$

By comparison with equation (35.29a),one sees that the metric for the fullspacetime （background plus ripple） is

$$
d s ^ { 2 } = ( g _ { \mu \nu } ^ { ( \mathtt { B } ) } + h _ { \mu \nu } ) d x ^ { \mu } d x ^ { \nu } ,
$$

$$
h _ { x x } = - h _ { y y } = 2 \beta , \mathrm { a l l ~ o t h e r } \ h _ { \mu \nu } = 0 .
$$

(Recall, in the region where $\beta \neq 0$ ， $L$ is very nearly 1.) One can think of the ripples as a transverse,traceless,symmetric tensor field $h _ { \mu \nu }$ analogous to the electromagnetic field $A _ { \mu } { , }$ propagating in the background geometry. Just as the electromagnetic field produces the background curvature via

(2)propagation of ripples in background

$$
G _ { u u } = - 2 L ^ { \prime \prime } / L = 8 \pi T _ { u u } ,
$$

so the gravitational-wave ripples $h _ { \mu \nu }$ produce the background curvature via equation (35.31),which one can rewrite as

$$
G _ { u u } ^ { \left( \mathrm { B } \right) } = - 2 L ^ { \prime \prime } / L = 8 \pi T _ { u u } ^ { \left( \mathrm { E F F } \right) } .
$$

Here

$$
T _ { u u } ^ { \mathrm { ( E F F ) } } \equiv \frac { 1 } { 4 \pi } ( \beta ^ { \prime } ) ^ { 2 } = \frac { 1 } { 3 2 \pi } h _ { j k , u } h _ { j k , u }
$$

(3) effective stress-energy tensor for ripples

is the “effective stress-energy tensor"for the gravitational waves. Notice that it agrees, except for averaging,with the expression (35.23） that was written down without justification in $\ S 3 5 . 7$

# ExerCise 35.1O. PLANE WAVE WITH TWO POLARIZATIONS PRESENT

The exact plane-wave solution (35.29） has polarization $\pmb { e } _ { + }$ Construct a similar solution. containing two arbitrary amplitudes, $\beta ( u )$ and $\gamma ( u )$ ,for polarizations ${ \pmb e } _ { + }$ and ${ \pmb e } _ { \times }$ .Extend the discussions of $\ S \ S 3 5 . 9 \mathrm { - } 3 5 . 1 2$ to this solution.

# $\$ 35,13$ .THE SHORTWAVE APPROXIMATION

The remainder of this chapter extends the above viewpoint in a rigorous manner to very general gravitational-wave solutions. This extension is called the “shortwave formalism"; it was largely devised by Isaacson (l968a,b), though it was built on foundations laid by Wheeler (l964a) and by Brill and Hartle (l964). Versions that are even more rigorous have been given in the W.K.B. or geometric-optics limit by Choquet-Bruhat (l969),and by MacCallum and Taub (1973).

Foundations for shortwave formalism:

Consider gravitational waves propagating through a vacuum background spacetime. As in $\ S 3 5 . 7$ ,let $\mathcal { R }$ be the typical radius of curvature of the background; let $\pmb { \lambda }$ and $\boldsymbol { \mathcal { a } }$ be the typical reduced wavelength $( \lambda / 2 \pi )$ and amplitude of the waves; and demand both $\mathcal { Q } \ll 1$ and $\lambda / \mathcal { R } \ll 1$ .The background curvature might be due entirely to the waves, or partly to waves and partly to nearby matter and nongravitational fields.

(1) ${ \mathcal { R } } , { \lambda }$ and $\mathcal { Q }$ defined   
(2) demand that $\mathcal { Q } \ll 1$ and $\lambda / \mathcal { R } \ll 1$   
(3) split of metric into background plus perturbation:"'steady coordinates"

The analysis uses a coordinate system closely “tuned” to spacetime in the sense that the metric coefficients can be split into "background"coeficients plus perturbations

$$
g _ { \mu \nu } = g _ { \mu \nu } ^ { ( \mathtt { B } ) } + h _ { \mu \nu }
$$

with these properties: (l) the amplitude of the perturbation is $\boldsymbol { \mathcal { a } }$

$$
h _ { \mu \nu } \lesssim \mathrm { ( t y p i c a l ~ v a l u e ~ o f ~ } g _ { \mu \nu } ^ { ( B ) } \big ) \cdot \mathcal { Q } ;
$$

(2) the scale on which $g _ { \mu \nu } ^ { ( \mathtt { B } ) }$ varies is $\gtrsim \mathcal { R }$

$$
g _ { \mu \nu , \alpha } ^ { ( \mathbf { B } ) } \lesssim ( \mathrm { t y p i c a l ~ v a l u e ~ o f ~ } g _ { \mu \nu } ^ { ( \mathbf { B } ) } ) / \mathcal { R } ;
$$

(3) the scale on which $h _ { \mu \nu }$ varies is\~

$$
h _ { \mu \nu , \alpha } \sim ( \mathrm { t y p i c a l ~ v a l u e ~ o f ~ } h _ { \mu \nu } ) / \lambda .
$$

Such coordinates are called“steady."

(4) Split of Ricci curvature tensor

A rather long computation (exercise 35.Il) shows that the Ricci tensor for an expanded metric of the form (35.55) is

$$
R _ { \mu \nu } = R _ { \mu \nu } ^ { ( \mathrm { B } ) } + R _ { \mu \nu } ^ { ( 1 ) } ( h ) + R _ { \mu \nu } ^ { ( 2 ) } ( h ) + \mathrm { e r r o r } .
$$

$$
? \qquad \mathcal { Q } / \lambda ^ { 2 } \qquad \mathcal { Q } ^ { 2 } / \lambda ^ { 2 } \qquad \mathcal { Q } ^ { 3 } / \lambda ^ { 2 }
$$

Here a marker $( \mathcal { a } / \dot { x } ^ { 2 }$ ，etc.）has been placed under each term to show its typical order of magnitude; $R _ { \mu \nu } ^ { ( \mathbf { B } ) }$ is theRiccitesorforthebackgrondmetric $g _ { \mu \nu } ^ { ( \mathtt { B } ) }$ ; and $R _ { \mu \nu } ^ { ( 1 ) }$ and $R _ { \mu \nu } ^ { ( 2 ) }$ are expressions defined by

$$
R _ { \mu \nu } ^ { ( 1 ) } ( h ) \equiv \frac { 1 } { 2 } ( - h _ { 1 \mu \nu } - h _ { \mu \nu \mid \alpha } { } ^ { \alpha } + h _ { \alpha \mu \mid \nu } { } ^ { \alpha } + h _ { \alpha \nu \mid \mu } { } ^ { \alpha } ) ,
$$

$$
\begin{array} { l } { { { \cal R } _ { \mu \nu } ^ { ( 2 ) } ( h ) \equiv \displaystyle \frac { 1 } { 2 } \biggl [ \frac { 1 } { 2 } h _ { \alpha \beta \mid \mu } h ^ { \alpha \beta } { } _ { \mid \nu } + h ^ { \alpha \beta } ( h _ { \alpha \beta \mid \mu \nu } + h _ { \mu \nu \mid \alpha \beta } - h _ { \alpha \mu \mid \nu \beta } - h _ { \alpha \nu \mid \mu \beta } ) } } \\ { { + h _ { \nu } ^ { \alpha \mid \beta } ( h _ { \alpha \mu \mid \beta } - h _ { \beta \mu \mid \alpha } ) - \biggl ( h ^ { \alpha \beta } { } _ { \mid \beta } - \displaystyle \frac { 1 } { 2 } h ^ { \mid \alpha } \biggr ) ( h _ { \alpha \mu \mid \nu } + h _ { \alpha \nu \mid \mu } - h _ { \mu \nu \mid \alpha } ) \biggr ] . } } \end{array}
$$

Intheseexpressdeveeoicedi $g _ { \mu \nu } ^ { ( \mathtt { B } ) }$ andanuprightline denotes acovariant derivative with respect to $g _ { \mu \nu } ^ { ( \mathtt { B } ) }$ (whereas in Chapter 21 it denoted covariant derivative with respect to.3-geometry).

At the heart of the shortwave formalism is its method for solving the vacuum field equations $R _ { \mu \nu } = 0$ . One begins by selecting out of expression (35.57) the part linear in the amplitude of the wave $\boldsymbol { \mathcal { q } }$ ,and setting it equal to zero. The action of the waves to curve up the background is a nonlinear phenomenon (linearized theory shows no sign of it)； so $R _ { \mu \nu } ^ { ( \mathbf { B } ) }$ cannot be linear in $\boldsymbol { \mathcal { Q } }$ Hence,in expression (35.57), $R _ { \mu \nu } ^ { ( 1 ) } ( h )$ is the only linear term, and it must vanish by itself

Split of vacuum field  
equations into ‘wave part"$( \propto \mathcal { Q } )$ plus"coarse-grain  
part" $( \propto \mathcal { Q } ^ { 2 }$ and smooth onscale $\pmb { \lambda }$ ）plus“fluctuationalcorrections" $( \propto \mathcal { Q } ^ { 2 }$ and ripplyon scale $\lambda$ ）

$$
R _ { \mu \nu } ^ { ( 1 ) } ( h ) = 0 .
$$

[Of course $h _ { \mu \nu }$ may contain nonlinear correction terms-call them $j _ { \mu \nu }$ -of order $\mathcal { Q } ^ { 2 }$ ， which must not be constrained by this linear equation. They will be determined by (35.59c), below.]

One next splits the remainder of $R _ { \mu \nu }$ into a part that is free of ripples-i.e., that varies only on scales far larger than $\pmb { \lambda }$ ("coarse-grain viewpoint"), and a second part that contains the fluctuations. This split can be accomplished by averaging over several wavelengths (see exercise 35.14 for a precise treatment of the averaging process,also see Choquet-Bruhat (l969)for a class of solutions where such averaging is not required):

$$
\begin{array}{c} \begin{array} { c } { { R _ { \mu \nu } ^ { ( B ) } + < R _ { \mu \nu } ^ { ( 2 ) } ( h ) > + \mathrm { e r r o r } = 0 \begin{array} { l } { { \Bigl [ \mathrm { s m o o t h } \Bigr ] } } \\ { { \Bigl [ \mathrm { p a r t } \Bigr ] } } \end{array} } } \\ { { \begin{array} { r l } { { \qquad \quad } } & { { \qquad \quad \mathcal { U } ^ { 3 } / \lambda ^ { 2 } } } \end{array} } } \\ { { R _ { \mu \nu } ^ { ( 1 ) } ( j ) + R _ { \mu \nu } ^ { ( 2 ) } ( h ) - < R _ { \mu \nu } ^ { ( 2 ) } ( h ) > + \mathrm { e r r o r } = 0 \begin{array} { l } { { \Bigl [ \mathrm { f l u c t u a t i n g } \Bigr ] } } \\ { { \Bigl [ \mathrm { s a r b } ^ { 2 } / \lambda ^ { 2 } } } \end{array} } } \\ { { \mathcal { M } ^ { 2 } / \lambda ^ { 3 } \Bigl [ \begin{array} { l } { { \mathrm { n o n l i n e a r ~ c o r r } - 1 } } \\ { { \Bigl [ \mathrm { r e c t i o n ~ t o ~ } h } } \end{array} \Bigr ] } } \end{array}   \end{array}
$$

That's allthere is to it!-except for reducing the equations to manageable form, and a fuller interpretation of the physics.

Begin with the interpretation.

Physical interpretation of the three parts of field equations:

(1） propagation of waves

Equation (35.59a) is an equation for the propagation of the gravitational waves $h _ { \mu \nu }$

(2) production of background curvature by energy of waves; $T _ { \mu \nu } ^ { ( \mathsf { G W } ^ { * } ) }$ defined

Equation (35.59b)shows how the stressenergy in the waves creates the background curvature. It can be rewritten in the more suggestive form

$$
{ \cal G } _ { \mu \nu } ^ { ( \mathrm { B } ) } \equiv R _ { \mu \nu } ^ { ( \mathrm { B } ) } - \frac { 1 } { 2 } R ^ { ( \mathrm { B } ) } g _ { \mu \nu } ^ { ( \mathrm { B } ) } = 8 { \pi } { } ^ { ( \mathrm { G W ) } } \mathrm { ~ i n ~ v a c u u m } ,
$$

where

$$
T _ { \mu \nu } ^ { \mathrm { ( G W ) } } \equiv - \frac { 1 } { 8 \pi } \biggl \{ \langle R _ { \mu \nu } ^ { \scriptscriptstyle ( 2 ) } ( h ) \rangle - \frac { 1 } { 2 } g _ { \mu \nu } ^ { \scriptscriptstyle ( 8 ) } \langle R ^ { \scriptscriptstyle ( 2 ) } ( h ) \rangle \biggr \}
$$

is the stress-energy tensor for the gravitational waves. Now one sees the origin of the statement in $\ S 3 5 . 7$ ,that the stress-energy of gravitational waves is well-defined only in a smeared-out sense.

(3) nonlinear self-interaction of waves

Finally,equation (35.59c) shows how the gravitational waves $\pmb { h }$ generate nonlinear corrections $j$ to themselves (wave-wave scattering,harmonics of the fundamental frequency, etc.). These higher-order effects will not be investigated in this chapter.

# EXERCISE

# Exercise 35.11. CONNECTION COEFFICIENTS AND CURVATURE TENSORS FOR A PERTURBED METRIC

Ina specific coordinate frame of an arbitrary spacetime,write the metric coefficients in covariant representation in the form

$$
g _ { \mu \nu } = g _ { \mu \nu } ^ { ( \mathrm { B } ) } + h _ { \mu \nu } .
$$

(At the end of the calculation, one can split $h _ { \mu \nu }$ into two parts, $h _ { \mu \nu } \longrightarrow h _ { \mu \nu } + j _ { \mu \nu } ;$ and out of this split obtain the formulas used in the text.） Assume that the typical components of $h _ { \mu \nu }$ are much lssthan those of $g _ { \mu \nu } ^ { ( \mathbf { B } ) }$ soonecanexpandChristofelsymbolsandcurvature tensors in $h _ { \mu \nu }$ Raise and lower indices of $h _ { \mu \nu }$ with $g _ { \mu \nu } ^ { ( \mathtt { B } ) }$ and denote by a $i ^ { 3 3 }$ covariant derivatives relative to $g _ { \mu \nu } ^ { ( \mathtt { B } ) }$ and byaoviatit $g _ { \mu \nu }$

(a）Here $g _ { \mu \nu }$ and $g _ { \mu \nu } ^ { ( \mathbf { B } ) }$ can bethoughtofastwodiferentmetricscoexistigintespaceime manifold. Show that the difference between the corresponding covariant derivatives, $\yen -$ ${ \pmb { \nabla } } ^ { ( \mathbf { B } ) } \equiv { \pmb { s } } .$ -indeed, the difference between any two covariant derivatives!-is a tensor with components

$$
S ^ { \mu } { } _ { \beta \gamma } = { T ^ { \mu } } _ { \beta \gamma } - { T ^ { ( \ B ) \mu } } _ { \beta \gamma }
$$

[Hint: See part B of Box 10.3.]

(b）Show that

$$
g ^ { \mu \nu } = g ^ { ( \mathsf { B } ) \mu \nu } - h ^ { \mu \nu } + h ^ { \mu \alpha } h _ { \alpha } ^ { \nu } - h ^ { \mu \alpha } h _ { \alpha } ^ { \beta } h _ { \beta } ^ { \nu } + \cdot \cdot \cdot ,
$$

and also that

$$
g ^ { \mu \nu } = g ^ { ( \mathsf { B } ) \mu \nu } - h ^ { \mu \nu } + h ^ { \mu \alpha } h _ { \alpha } ^ { \nu } - h ^ { \mu \alpha } h _ { \alpha } ^ { \beta } h _ { \beta \gamma } g ^ { \gamma \nu } .
$$

(c) By calculatingina local Lorentzframeof $g _ { \mu \nu } ^ { ( \mathbf { B } ) }$ and then transforming back to the original frame,show that

$$
\begin{array} { c } { { S ^ { \mu } { } _ { \beta \gamma } = \displaystyle \frac { 1 } { 2 } g ^ { \mu \alpha } ( h _ { \alpha \beta \mid \gamma } + h _ { \alpha \gamma \mid \beta } - h _ { \beta \gamma \mid \alpha } ) , } } \\ { { R ^ { \alpha } { } _ { \beta \gamma \delta } - R ^ { { ( \mathtt { B } ) } \alpha } { } _ { \beta \gamma \delta } = S ^ { \alpha } { } _ { \beta \delta \mid \gamma } - S ^ { \alpha } { } _ { \beta \gamma \mid \delta } + S ^ { \alpha } { } _ { \mu \gamma } S ^ { \mu } { } _ { \beta \delta } - S ^ { \alpha } { } _ { \mu \delta } S ^ { \mu } { } _ { \beta \gamma } , } } \\ { { R _ { \beta \delta } - R ^ { \mathtt { G } } { } _ { \beta \delta } = S ^ { \alpha } { } _ { \beta \delta \mid \alpha } - S ^ { \alpha } { } _ { \beta \alpha \mid \delta } + S ^ { \alpha } { } _ { \mu \alpha } S ^ { \mu } { } _ { \beta \delta } - S ^ { \alpha } { } _ { \mu \delta } S ^ { \mu } { } _ { \beta \alpha } . } } \end{array}
$$

(d） Show that expression (35.62f) reduces to

$$
R _ { \beta \delta } = R _ { \beta \delta } ^ { ( \mathrm { B } ) } + R _ { \beta \delta } ^ { ( 1 ) } ( h ) + R _ { \beta \delta } ^ { ( 2 ) } ( h ) + \cdot \cdot \cdot
$$

where $R ^ { ( 1 ) }$ and $R ^ { ( 2 ) }$ are defined by equations (35.58).

# \$35.14. EFFECT OF BACKGROUND CURVATURE ON WAVE PROPAGATION

Focus attention on the propagation equation $R _ { \mu \nu } ^ { ( 1 ) } ( h ) = 0$ . As in linearized theory, so also here,the propagation is studied more simply in terms of

$$
\overline { { { h } } } _ { \mu \nu } \equiv h _ { \mu \nu } - \frac { 1 } { 2 } h g _ { \mu \nu } ^ { ( \mathtt { B } ) } ,
$$

$\overline { { h } } _ { \mu \nu }$ defined

than in terms of $h _ { \mu \nu }$ . Rewritten in terms of $\overline { { h } } _ { \mu \nu } , R _ { \mu \nu } ^ { ( 1 ) } ( h ) = 0$ says

$$
\overline { { { h } } } _ { \mu \nu \mid \alpha } { } ^ { \alpha } + g _ { \mu \nu } ^ { ( \mathtt { B } ) } \overline { { { h } } } { } ^ { \alpha \beta } { } _ { \perp \beta \alpha } - 2 \overline { { { h } } } _ { \alpha ( \mu \mid } { } ^ { \alpha } { } _ { \nu ) } + 2 R _ { \alpha \mu \beta } ^ { ( \mathtt { B } ) } \overline { { { h } } } { } ^ { \alpha \beta } - 2 R _ { \alpha ( \mu } ^ { \mathtt { B } ) } \overline { { { h } } } _ { \nu ) } { } ^ { \alpha } = 0 .
$$

Propagation equation for waves on curved background

[To obtain this,invert equation (35.63)obtaining $h _ { \mu \nu } = \overline { { h } } _ { \mu \nu } - { \textstyle \frac { 1 } { 2 } } g _ { \mu \nu } ^ { ( \mathbf { B } ) } \overline { { h } }$ insert this into (35.58a) and equate to zero; then commute covariant derivatives using the identity (16.6b)； finally contract to obtain an expression for $\overline { { h } } _ { \vert \alpha } \alpha$ and substitute that back in.]

The propagation equation (35.64) can be simplified by a special choice of gauge. An infinitesimal coordinate transformation

Specialization to "Lorentz gauge"

$$
x _ { \mathrm { \tiny ~ n e w } } ^ { \mu } ( \mathcal { P } ) = x _ { \mathrm { \tiny ~ o l d } } ^ { \mu } ( \mathcal { P } ) + \xi ^ { u } ( \mathcal { P } )
$$

induces a first-order change in the functional forms of the metric coeficients given by

$$
h _ { \mu \nu \mathrm { n e w } } ( x _ { \mathrm { \ n e w } } ^ { \alpha } ) = h _ { \mu \nu \mathrm { o l d } } ( x _ { \mathrm { \ n e w } } ^ { \alpha } ) - 2 \xi _ { ( \mu | \nu ) }
$$

[analog of the gauge transformation of linearized theory,equation (35.3c)； see exercise 35.12]. By an appropriate choice of the four functions $\xi ^ { \mu }$ ,one can enforce the four “Lorentz gauge conditions"

$$
\overline { { h } } _ { \mu } { } ^ { \alpha } { } _ { | \alpha } = 0
$$

Coupling of waves to Ricci tensor can be ignored

Propagation equation in Lorentz gauge and its realm of validity

Lists of effects absent from and contained in propagation equation

in the new coordinate system (exercise 35.13). This choice of gauge is analogous to that of linearized theory. It makes the second and third terms in the propagation equation vanish. (For additional gauge conditions of the “TT” type. see exercise 35.13.)

The lasttermofthepropagationequation. $- 2 R _ { \alpha ( \mu } ^ { \mathrm { ( B ) } } \overline { { h } } _ { \nu ) } { } ^ { \alpha }$ . vanishes to within the precision of the analysis, for this reason: attention has been confined to vacuum; so the only source of a nonvanishing Ricci tensor is the stress-energy carried by the gravitational waves themselves [equation (35.60); hence $R _ { \alpha \beta } ^ { ( \mathbf { B } ) } \sim \mathcal { Q } ^ { 2 } / \lambda ^ { 2 }$ and

$$
R ^ { \mathrm { ( B ) } } { } _ { \alpha ( \mu } \overline { { { h } } } _ { \nu ) } { } ^ { a } \sim \bar { q } ^ { 3 } / \bar { \lambda } ^ { 2 } .
$$

This is of the same order as $R _ { \mu \nu } ^ { ( 3 ) } ( h )$ 、the third-order correction to the Ricci tensor, which is far below the precision of the analysis. For consistency in the analysis it will therefore be neglected.

Summaryofthissectionthusfar:bychosinga gauge where $\overline { { h } } _ { \mu } { } ^ { a } { } _ { | \alpha } = 0$ and by discarding terms of higher order than the precision of the analysis,one obtains the vacuum propagation equation

$$
\overline { { { h } } } _ { \mu \nu \mid \alpha } { } ^ { \alpha } + 2 R _ { \alpha \mu \beta \nu } ^ { \mathrm { ( B ) } } \overline { { { h } } } { } ^ { \alpha \beta } = 0 ,
$$

subject to the Lorentz gauge condition

$$
\overline { { h } } _ { \mu \alpha } { } ^ { | \alpha } = 0 .
$$

Equation (35.68） is accurate to first order in the amplitude [corrections $\propto \mathcal { Q } ^ { 2 }$ are embodied in equation (35.59c)]; and its accuracy is independent of the ratio $\pmb { \lambda } / \mathcal { R }$ ， as one sees from equations (35.59). Thus,it can be applied whenever the waves are weak,even if the wavelength is large!

All nonlinear interactions of the wave with itself are neglected in this first-order propagation equation. Absent is the mechanism for waves to scatter off each other and off the background curvature that they themselves produce. Also absent are any hints of a change in shape of pulse due to self-interaction as a pulse of waves propagates. There are no signs of the gravitational collapse that one knows must occur when a mass-energy $m$ of gravitational waves gets compressed into a region of size $\lesssim m$ . To see all these effects, one must turn to corrections of second order in $\mathcal { Q }$ and higher [e.g., equations (35.59c) and (35.60)].

Actually contained in the propagation equation are all effects due to the linear action of the background curvature on the propagating wave. These effects are explored, for short wavelengths $( \pmb { \chi } / \mathcal { R } \ll 1 )$ and for nearly flat wave fronts, in exercises 35.15-35.17 at the end of the chapter. The effects considered include a gravitational redshift of gravitational radiation and gravitational deflection of the direction of propagation of gravitational radiation, identical to those for light; and also a rotation of the polarization tensor. When the wavelength is not small $( \hbar / \mathcal { R }$ not $\ll 1$ ), the propagation equation includes a back-scatter of the gravitational waves off the background curvature and a resultant pattern of wave “tails” analogous to that explored in exercise 32.10 [see, e.g., Couch et al. (1968),Price (l97la), Bardeen and Press (1972), Unt and Keres (1972)).

# Exercise 35.12. GAUGE TRANSFORMATIONS IN A CURVED BACKGROUND

(a) Show that the infinitesimal coordinate transformation (35.65a) induces the change   
(35.65b) in the functional form of the metric perturbation. (b) Discuss the relationship between this gauge transformation and the concept of a Killing   
vector $( \ S 2 5 . 2 )$ ，

# ExerciSe 35.13. TRANSVERSE-TRACELESS GAUGE FOR GRAVITATIONALWAVES PROPAGATING IN A CURVED BACKGROUND

(a)Showthaticedckgodspacitegi $\overline { { { h } } } _ { \mu } \alpha _ { \{ \alpha }  = 0$ is preserved by transformations whose generator satisfies the wave equation $\xi _ { \mu } { } ^ { \mid \alpha } { } _ { \alpha } = 0$

(b) Locally (over distances much smaller than $\mathcal { R }$ )linearized theory is applicable;so there exists such a transformation which makes [see equations (35.7b) and (35.8a)]

$$
\begin{array} { r } { \overline { { h } } = 0 + \mathrm { e r r o r } , \qquad \overline { { h } } _ { \mu \alpha } u ^ { \alpha } = 0 + \mathrm { e r r o r } . } \end{array}
$$

Here $u ^ { \alpha }$ is a vector field that is as nearly covariantly constant as possible $( u ^ { \alpha } { } _ { 1 \beta } = 0 )$ ;i.e., it is a constant vector in the inertial coordinates of linearized theory;and the errors are small over distances much less than $\mathcal { R }$ . Show that $\overline { { h } } = 0$ can be imposed globally along with $\overline { { h } } _ { \mu \alpha } { } ^ { 1 \alpha } = 0$ ; ie.,show that,if itisimposedonaninitialhypesuface,the propagaionequation (35.68) preserves it.

(c) Show that in general, the background curvature prevents any vector field from being covariantly constant $( u ^ { \hat { \alpha } } { } _ { 1 \hat { \beta } } \sim u ^ { \hat { \alpha } } / \mathcal { R }$ at best)；and from this show that $\overline { { h } } _ { \mu \alpha } u ^ { \alpha } = 0$ cannot be imposed globally alongwith $\overline { { { h } } } _ { \mu } { } ^ { \alpha } { } _ { \{ \alpha }  = 0$

# $\$ 35.15$ .STRESS-ENERGY TENSOR FOR GRAVITATIONAL WAVES

Turn now to an evaluation of the effective stress-energy tensor $T _ { \mu \nu } ^ { ( \mathrm { G W ) } }$ of equation (35.61). The evaluation requires averaging various quantities over several wavelengths. Useful rules for manipulating quantities inside the averaging brackets $\langle \quad \rangle$ are the following (see exercise 35.l4 for justification).

The averaging process involved in"coarse-grain" viewpoint

(l） Covariant derivatives commute; e.g., $\langle h h _ { \mu \nu | \alpha \beta } \rangle = \langle h h _ { \mu \nu | \beta \alpha } \rangle$ The fractional errors made by freely commuting are ${ \sim } ( \lambda / \mathcal { R } ) ^ { 2 }$ ，well below the inaccuracy of the computation.

(2) Gradients average out to zero; e.g., $\langle ( h _ { | \alpha } h _ { \mu \nu } ) _ { | \beta } \rangle = 0$ Fractional errors made here are $\lesssim \hbar / \mathcal { R }$

(3） As a corollary,one can freely integrate by parts,flipping derivatives from one $h$ to the other; e.g., $\langle h h _ { \mu \nu | \alpha \beta } \rangle = \langle - h _ { 1 \beta } h _ { \mu \nu | \alpha } \rangle$

A straightforward but long calculation using these rules, using equation (35.58b) for $R _ { \mu \nu } ^ { ( 2 ) } ( h )$ ,using definition (35.63）of $\overline { { h } } _ { \mu \nu }$ ,using the propagation equation (35.64), andusingthedeiition5.61)of $T _ { \mu \nu } ^ { ( \mathrm { G W ) } }$ yields $\langle R ^ { ( 2 ) } ( h ) \rangle = 0$ and

Evaluation of effective stress-energy tensor for gravitational waves， TGw)

$$
T _ { \mu \nu } ^ { ( \mathrm { G W ) } } = \frac { 1 } { 3 2 \pi } \langle \overline { { { h } } } _ { \alpha \beta | \mu } \overline { { { h } } } { } ^ { \alpha \beta } { } _ { | \nu } - \frac { 1 } { 2 } \overline { { { h } } } _ { | \mu } \overline { { { h } } } _ { | \nu } - 2 \overline { { { h } } } { } ^ { \alpha \beta } { } _ { | \beta } \overline { { { h } } } _ { \alpha ( \mu | \nu ) } \rangle .
$$

This is the result quoted in equation (35.23'), except that there one used an inertial coordinate system of linearized theory,where covariant derivatives and ordinary derivatives arethesame.Inagauge where $\widehat { h } _ { \mu } { } ^ { \alpha } { } _ { | \alpha } = 0$ the last term vanishes.When, in addition, $\overline { { h } } _ { \mu \nu }$ is traceless (see exercise 35.l3), the second term vanishes; and there remains only

$$
T _ { \mu \nu } ^ { ( { \mathrm { G W } } ) } = { \frac { 1 } { 3 2 \pi } } \langle \overline { { h } } _ { \alpha \beta \mid \mu } \overline { { h } } ^ { \alpha \beta } { } _ { \mid \nu } \rangle \qquad \mathrm { i f ~ } \overline { { h } } _ { \mu } { } _ { \mid \alpha } ^ { \alpha } = \overline { { h } } = 0 .
$$

Accuracy of expression for T(Gw

These expressions for the effective stress-energy of a gravitational wave have fractional errors of order $\boldsymbol { \mathcal { a } }$ ，due to the neglect of second-order corrections to $h _ { \mu \nu }$ they also have fractional errors of order $\pmb { \dot { \lambda } } / \Im \mathbf { \hat { \eta } }$ ，due to the averaging process, which makes no sense when $\pmb { \lambda }$ approaches $\mathcal { R }$ in magnitude. Since ${ \mathcal { Q } } \lesssim \hbar / { \mathcal { R } }$ (35.28), the dominant errors in $T _ { \mu \nu } ^ { ( \mathrm { G W ) } }$ are ${ \sim } \hbar / \mathcal { R }$

Properties of $T _ { \mu \nu } ^ { \mathrm { ( G W ) } }$

To this accuracy, the stress-energy tensor for gravitational waves is on an equal footing with any other stress-energy tensor. It plays the same role in producing background curvature; and it enters into conservation laws in the same way.For example,one can show,either by direct calculation or from the identity ${ \cal G } ^ { ( { \bf B } ) \mu \nu } { } _ { | \nu } = 0$ ， that

$$
T ^ { \mathrm { ( G W ) } \mu \nu } { } _ { \vert \nu } = 0 + \mathrm { e r r o r } ,
$$

where the error ${ \sim } ( \lambda / \mathcal { R } ) ( T ^ { ( \mathrm { G W } ) \mu \nu } / \mathcal { R } )$ is negligible in the shortwave approximation. Some of the properties of $T _ { \mu \nu } ^ { ( \mathrm { G W ) } }$ have already been explored in $\ S 3 5 . 7$ .Further properties are explored in exercises 35.18 and 35.19.

# EXERCISES

# Exercise 35.14. BRILL-HARTLE AVERAGE

Isaacson (1968b) introduces the following averaging scheme, which he names “Brill-Hartle averaging.”

(a) In the small region,of size several times $\pmb { \lambda }$ ，where the averaging occurs,there wil be a unique geodesic of $g _ { \mu \nu } ^ { ( \mathtt { B } ) }$ connecting any two points ${ \mathcal { S } } ^ { \prime }$ and $\mathcal { P }$ ; so given a tensor $\pmb { \cal E } ( \mathcal { P } ^ { \prime } )$ at ${ \mathcal { P } } ^ { \prime }$ , one can parallel transport it along this geodesic to $\mathcal { P }$ ， getting there a tensor ${ \pmb E } ( \mathcal { P } ^ { \prime } ) _ {  \mathcal { P } }$ (b) Let $f ( { \mathcal { P } } ^ { \prime } , { \mathcal { P } } )$ be a weighting function that falls smoothly to zero when ${ \mathcal { P } } ^ { \prime }$ and $\mathcal { P }$ are separated by many wavelengths,and such that

$$
\int f ( \mathcal { P } ^ { \prime } , \mathcal { P } ) \sqrt { - g ^ { ( \mathsf { B } ) } ( \mathcal { P } ^ { \prime } ) } \ d ^ { 4 } x ^ { \prime } = 1 .
$$

(c) Then the average of the tensor feld $\pmb { \cal E } ( \mathcal { P } ^ { \prime } )$ over several wavelengths about the point $\mathcal { P }$ is

$$
\langle { \pmb E } \rangle _ { \mathcal { S } } \equiv \int { \pmb E } ( \mathcal { P } ^ { \prime } ) _ {  \mathcal { S } } f ( \mathcal { P } ^ { \prime } , \mathcal { P } ) \sqrt { - g ^ { ( { \pmb { \mathrm { B } } } ) } ( \mathcal { P } ^ { \prime } ) } \ d ^ { 4 } x ^ { \prime } .
$$

(i)Shothatthereexistsaneity $g _ { \mu } ^ { ( \mathbf { B } ) \alpha ^ { \prime } } ( \mathcal { P } , \mathcal { P } ^ { \prime } )$ ,whoseprimedindextransformsasatesor at ${ \mathcal { P } } ^ { \prime }$ and whose unprimed index transforms as a tensor at $\mathscr { P }$ ,such that (for $\pmb { \cal E }$ second rank)

$$
E _ { \alpha \beta } ( \mathcal { P } ^ { \prime } ) _ {  \mathcal { S } } = g _ { \alpha } ^ { \mathrm { ( B ) } \mu ^ { \prime } } g _ { \beta } ^ { \mathrm { ( B ) } \nu ^ { \prime } } E _ { \mu ^ { \prime } \nu ^ { \prime } } ( \mathcal { P } ^ { \prime } ) .
$$

This entity is called the “bivector of geodesic parallel displacement”; see DeWitt and Brehme (1960) or Synge (1960a).

(ii) Rewriting expression (35.73) in coordinate language as

$$
\langle E _ { \alpha \beta } ( x ) \rangle = \int g _ { \alpha } ^ { ( \mathbb { B } ) \mu ^ { \prime } } ( x , x ^ { \prime } ) g _ { \beta } ^ { ( \mathbb { B } ) \nu ^ { \prime } } ( x , x ^ { \prime } ) E _ { \mu ^ { \prime } \nu ^ { \prime } } ( x ^ { \prime } ) f ( x , x ^ { \prime } ) \sqrt { - g ^ { ( \mathbb { B } ) } ( x ^ { \prime } ) } d ^ { 4 } x ^ { \prime } ,
$$

derive the three averaging rules cited at the beginning of $\ S 3 5 . 1 5$ .[For solution, see Appendix of Isaacson (1968b).]

# Exercise 35.15. GEOMETRIC OPTICS

Develop geometric optics for gravitational waves of small amplitude propagating in a curved background. Pattern the analysis after geometric optics for electromagnetic waves (S22.5). In particular, let $\overline { { h } } _ { \mu \nu }$ have an amplitude that varies slowly (on a scale $\pmb { \mathscr { t } } \leq \pmb { \mathcal { R } } )$ and a phase $\pmb \theta$ that varies rapidly $( \pmb { \theta } _ { , \hat { \alpha } } \sim 1 / \pmb { \chi } )$ . Expand the amplitude in powers of $\pmb { \lambda } / \bar { \pmb { \lambda } }$ ,so that

$$
\overline { { { h } } } _ { \mu \nu } = \Re \{ A _ { \mu \nu } + \epsilon B _ { \mu \nu } + \epsilon ^ { 2 } C _ { \mu \nu } + \cdot \cdot \cdot \} e ^ { \mathrm { i } \theta / \epsilon } .
$$

Here $\pmb { \epsilon }$ is a formal expansion parameter,actually equal to unity,which reminds one that the terms attached to ${ \pmb \epsilon } ^ { \pmb n }$ are proportional to $( \pmb { \lambda } / \mathcal { R } ) ^ { \pmb { n } }$ Define the following quantities (with $\pmb { A } _ { \pmb { \mu } \pmb { \nu } } ^ { * }$ denoting the complex conjugate of $A _ { \mu \nu } )$ ：

$$
\begin{array} { r l } & { \quad \mathrm { ~ \forall ~ \ " e ~ s e c t o r " : ~ } k _ { \alpha } \equiv \theta _ { , \alpha } } \\ & { \quad \mathrm { ~ } } \\ & { \quad \mathrm { ~ \cdots ~ s c a l a r ~ a m p l i t u d e " : ~ } { \mathcal A } \equiv \left( \frac { 1 } { 2 } A _ { \mu \nu } ^ { * } A ^ { \mu \nu } \right) ^ { 1 / 2 } } \\ & { \quad \mathrm { ~ \ " ~ } \mathrm { ~ } } \\ & { \quad \mathrm { ~ \cdots ~ } \mathrm { ~ } \mathrm { ~ p o l a r i z a t i o n " : ~ } e _ { \mu \nu } \equiv A _ { \mu \nu } / A . } \end{array}
$$

By inserting expression (35.75) into the gauge condition (35.66) and the propagation equation (35.68),derive the fundamental equations of geometrical optics as follows.

(a) The rays (curves perpendicular to surfaces of constant phase) are null geodesics; i.e.

$$
\begin{array} { c c } { { } } & { { k _ { \alpha } k ^ { \alpha } = 0 , } } \\ { { . . . . . } } & { { . . . . } } \end{array}
$$

(b) The polarization is orthogonal to the rays and is parallel transported along them;

$$
\begin{array} { r } { e _ { \mu \alpha } k ^ { \alpha } = 0 , } \\ { e _ { \mu \nu \mid \alpha } k ^ { \alpha } = 0 . } \end{array}
$$

(c) The scalar amplitude decreases as the rays diverge away from each other in accordance with

$$
{ \mathcal A } _ { , \alpha } k ^ { \alpha } = - \frac { 1 } { 2 } k ^ { \alpha } { } _ { 1 \alpha } { \mathcal A } .
$$

i.e.,

$$
( \ \mathcal { A } ^ { 2 } k ^ { \alpha } ) _ { \mid \alpha } = 0 \ ( \mathrm { ^ { * * } c o n s e r v a t i o n \ o f \ g r a v i t o n s ^ { \prime * } } ) .
$$

(d） The correction $\pmb { { \cal B } } _ { \mu \nu }$ to the amplitude obeys

$$
B _ { \mu \alpha } k ^ { \alpha } = i A _ { \mu \alpha } { } ^ { \mathrm { i } \alpha } ,
$$

$$
B _ { \mu \nu \mid \alpha } k ^ { \alpha } = { } - \frac { 1 } { 2 } k ^ { \alpha } { } _ { \mid \alpha } B _ { \mu \nu } + \frac { 1 } { 2 } i A _ { \mu \nu \mid \alpha } { } ^ { \alpha } + i R _ { \alpha \mu \beta \nu } ^ { ( \mathrm { B } ) } A ^ { \alpha \beta } .
$$

In accordance with exercise 35.13, specialize the gauge so that $\bar { h } = 0$ ,i.e.,

$$
{ e _ { \alpha } ^ { \alpha } } \displaystyle = 0 .
$$

Then show that the stress-energy tensor (35.70') for ihe waves is

$$
T _ { \mu \nu } ^ { \mathrm { ( G W ) } } = \frac { 1 } { 3 2 \pi } \mathcal { A } ^ { 2 } k _ { \mu } k _ { \nu } .
$$

This has the same form as the stress-energy tensor for a beam of particles with zero rest mass(see $\ S 5 . 4 )$ .Show explicitly that $T ^ { \mathrm { ( G W ) } \tilde { \mu } \nu } { } _ { \{ \nu } ^ { } = 0 $

# Exercise 35.16. GRAVITONS

Show that geometric optics, as developed in the preceding exercise, is equivalent to the following: $^ { 6 6 } \mathsf { A }$ graviton is postulated to be a particle of zero rest mass and 4-momentum $\pmb { p }$ ,which moves along a null geodesic $\mathbf { \nabla } \mathbf { p } _ { } \mathbf { \pmb { \rho } } = 0 ;$ . It parallel transports with iself $( \pmb { \nabla _ { p } } \pmb { e } = 0 )$ a transverse $( \pmb { \theta } \cdot \pmb { p } = 0 )$ traceless $( e _ { \alpha } ^ { \ \alpha } = 0 )$ ）polarization tensor e. Geometric optics is the theory of a stream of such gravitons moving through spacetime.”Exhibit the relationship between the quantities in this version of geometric optics and the quantities in the preceding version (e.g., $\pmb { p } = \hbar \pmb { k }$ ,where $\hbar$ is Planck's reduced constant $h / 2 \pi$ ).

# Exercise 35.17. GRAVITATIONAL DEFLECTION OF GRAVITATIONAL WAVES

Show that gravitational waves of short wavelength passing through the solar system experience the same redshift and gravitational deflection as does light. (One should be able to infer this directly from exercise 35.15.)

# Exercise 35.18. GAUGE INVARIANCE OF $T _ { \mu \nu } ^ { ( \mathrm { G W } ) }$

owthst $T _ { \mu \nu } ^ { ( \mathsf { G W } ) }$

# Exercise 35.19. $T _ { \mu \nu } ^ { ( \mathsf { G W } ) }$ EXPRESSED AS THE AVERAGE OF A STRESS-ENERGY PSEUDOTENSOR

Calculate the average over several wavelengths of the Landau-Lifshitz stress-energy pseudotensor [equation (20.22)] for gravitational waves with $\lambda / { \mathcal { R } } \ll 1 ,$ The result should be equal 10 $T _ { \mu \nu } ^ { ( \mathsf { G W } ) }$ Hint: Work in a gauge where $\overline { { { h } } } _ { \mu } { } ^ { \alpha } { } _ { | \alpha } = \overline { { { h } } } = 0$ tosimplifythecalculation.

# Exercise 35.20. SHORTWAVE APPROXIMATION FROM A VARIATIONAL VIEWPOINT

Readers who have studied the variational approach to gravitation theory in Chapter 2l may find attractive the following derivation of the basic equations of the shortwave approximation. It was devised,independently,by Sandor Kovacs and Bernard Schutz,and by Bryce DeWitt (unpublished, 1971).MacCallum and Taub (l973） give a“non-Palatini”version.

(a) Define

$$
\begin{array} { l c r } { { g _ { \mu \nu } \equiv g _ { \mu \nu } ^ { ( \mathbf { B } ) } + h _ { \mu \nu } , \qquad \bar { h } _ { \mu \nu } \equiv h _ { \mu \nu } - \displaystyle \frac { 1 } { 2 } g _ { \mu \nu } ^ { ( \mathbf { B } ) } h , } } \\ { { \qquad \nonumber } } \\ { { W ^ { \mu } { } _ { \beta \gamma } \equiv \displaystyle \frac { 1 } { 2 } g _ { ( \mathbf { B } ) } ^ { \mu \alpha } ( h _ { \alpha \beta \mid \gamma } + h _ { \alpha \gamma \mid \beta } - h _ { \beta \gamma \mid \alpha } ) . } } \end{array}
$$

Raise and lower indices on $h _ { \mu \nu }$ and $W ^ { \mu } { } _ { \beta \gamma }$ with the background metric. Using the results of exercise 35.11,derive the following expression for the Lagrangian of the gravitational field:

$$
\mathcal { E } \equiv \frac { 1 } { 1 6 \pi } ( - g ) ^ { 1 / 2 } R = \mathcal { E } ^ { \prime } + \left( \begin{array} { l } { \mathrm { p e r f e c t ~ d i v e r g e n c e } } \\ { \mathrm { o f ~ f o r m ~ } \partial \mathcal { Q } ^ { \alpha } / \hat { x } x ^ { \alpha } } \end{array} \right) + \left( \begin{array} { l } { \mathrm { c o r r e c t i o n s ~ o f ~ o r d e r } } \\ { d ^ { 3 } / \hat { x } ^ { 2 } , R _ { \mu \nu } ^ { \mathrm { ( B ) } } \mathcal { Q } , \mathrm { ~ a n d ~ s m a l l e r } } \end{array} \right) ,
$$

where

$$
\begin{array} { l } { { \displaystyle { \mathcal E } ^ { \prime } \equiv \frac { 1 } { 1 6 \pi } ( - g ^ { ( \mathbf { B } ) } ) ^ { 1 / 2 } [ R ^ { ( \mathbf { B } ) } - \overline { { h } } ^ { \mu \nu } ( W _ { ~ \mu \nu | \alpha } ^ { \alpha } - W _ { ~ \mu \alpha | \nu } ^ { \alpha } ) } } \\ { { \displaystyle ~ + ~ g ^ { ( \mathbf { B } ) \mu \nu } ( W _ { ~ \beta \alpha } ^ { \alpha } W ^ { \beta } _ { \mu \nu } - W _ { ~ \beta \nu } ^ { \alpha } W _ { ~ \mu \alpha } ^ { \beta } ) ] . } } \end{array}
$$

[Hint:recall that

$$
( - g ^ { ( \mathsf { B } ) } ) ^ { 1 / 2 } B ^ { \alpha } { } _ { \mid \alpha } = \partial [ ( - g ^ { ( \mathsf { B } ) } ) ^ { 1 / 2 } B ^ { \alpha } ] / \partial x ^ { \alpha }
$$

for any $B ^ { \alpha }$ .] Drop the corrections of order ${ \mathcal { Q } } ^ { 3 } / { \dot { \lambda } } ^ { 2 }$ from $\mathcal { L }$ ；and,knowing in advance that the field equations will demand $R _ { \mu \nu } ^ { ( \mathbf { B } ) } \sim \mathcal { a } ^ { 2 } / \lambda ^ { 2 }$ ,drop also the corrections of order $R _ { \mu \nu } ^ { ( \mathbf { B } ) } \mathcal { Q }$ Knowing that a perfect divergence contributes nothing in an extremization calculation, drop the divergence term from $\mathcal { E }$ Then $\mathcal { E } ^ { \prime }$ is the only remaining part of $\mathcal { L }$

(b） Extremize $I \equiv \int \mathcal { E } ^ { \prime } d ^ { 4 } x$ by the Palatini method (S21.2); i.e.,abandon (temporarily) definition (35.78b) of $\underline { W } ^ { \mu } { } _ { \beta \gamma } ,$ and extremize $\pmb { I }$ with respect to independent variations of ${ { W ^ { \mu } } } _ { \beta \gamma } = W ^ { \mu } { } _ { \gamma \beta }$ ， $\overline { { { h } } } ^ { \mu \nu } = \overline { { { h } } } ^ { \nu \mu }$ and $g _ { ( \mathbf { B } ) } ^ { \mu \nu } = g _ { ( \mathbf { B } ) } ^ { \nu \mu }$ Show that extremization with respect to $W ^ { \mu } { } _ { \beta \gamma }$ leads back to equation (35.78b) for $W ^ { \mu } { } _ { \beta \gamma }$ in terms of $h _ { \mu \nu }$ .Show that extremization with respect t0 $\overline { { h } } ^ { \mu \nu }$ ,when combined with equations $( 3 5 . 7 8 \mathsf { a } , \mathsf { b } )$ ,leads to the propagation equation for gravitational waves (35.64). Show that extremization with respect to $g ^ { ( \mathbf { B } ) \mu \nu }$ ，when combined with equations $( 3 5 . 7 8 \mathbf { a } , \mathbf { b } )$ and with the propagation equation (35.64),and when averaged over several wavelengths, leads to

$$
G _ { \mu \nu } ^ { ( \mathrm { B } ) } = 8 \pi T _ { \mu \nu } ^ { ( \mathrm { G W ) } } ,
$$

whe $T _ { \mu \nu } ^ { ( \mathsf { G W } ) }$ sromce $\overline { { h } } = \overline { { h } } _ { \alpha } { } ^ { \beta } { } _ { 1 \beta } = 0$ outset.]
