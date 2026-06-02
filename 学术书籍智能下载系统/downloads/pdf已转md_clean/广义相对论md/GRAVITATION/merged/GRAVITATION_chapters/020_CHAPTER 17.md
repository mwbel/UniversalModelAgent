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
