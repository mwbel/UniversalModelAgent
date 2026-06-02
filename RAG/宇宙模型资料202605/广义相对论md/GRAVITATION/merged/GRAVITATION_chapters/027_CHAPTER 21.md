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


<!-- chunk 0009: pages 561-630 -->
Turn from initial- and final-value data to the action integral that is determined by(l) these data and (2) the principle that the action be an extremum,

$$
I = I _ { \mathrm { e x t r e m u m } } = S .
$$

The action depends on the variables on the final hypersurface,according to the formula

Problem in assuring completeness and consistency of initial data

$$
S = S ( \varSigma , B )
$$

in electrodynamics, but according to the formula

$$
S = S ( ^ { ( 3 ) } \mathcal { Y } )
$$

in geometrodynamics. In each case, there are three numbers per spacepoint in the argument of the functional (one in $\pmb { \Sigma }$ ; two in a divergence-free magnetic field; three in $( 3 ) \textcircled { 8 }$

This mixing of the one many-fingered time and the two dynamic variables in a 3-geometry makes it harder in general relativity than in Maxwell theory to know when one has in hand appropriate initial value data. Give $\pmb { \Sigma }$ and give $\mathcal { B }$ and $\dot { \mathcal { B } }$ on $\pmb { \Sigma }$ : that was enough for electrodynamics. For geometrodynamics, to give the six $g _ { i j } ( x , y , z )$ and the six $\dot { g } _ { i j } ( x , y , z )$ is not necessarily enough. For example, let the time parameter $t$ be a fake, so that $d t$ , instead of leading forward from a given hypersurface $\pmb { \Sigma }$ to a new hypersurface $\pm \mathbf { \nabla } d \Sigma$ , merely recoordinatizes the present hypersurface:

$$
\begin{array} { c } { { x ^ { i } \longrightarrow x ^ { i } - \xi ^ { i } d t , \qquad \longrightarrow } } \\ { { g _ { i j } \longrightarrow g _ { i j } + ( \xi _ { i \mid j } + \xi _ { j \mid i } ) d t . } } \end{array}
$$

A first inspection may make one think that one has adequate data in the six $g _ { i j }$ and the six

$$
\dot { g } _ { i j } = \xi _ { i \vert j } + \xi _ { j \vert i } ,
$$

but in the end one sees that one has not both faces of the thin sandwich,as required, but only one. Thus one must reject, as improperly posed data in the generic problem of dynamics,any set of six $\dot { g } _ { i j }$ that let themselves be expressed in the form (21.131) [Belasco and Ohanian (1969)].

The “thin sandwich conjecture"

Similar diffculties occur when the two faces of the thin sandwich, instead of coinciding everywhere, coincide in a limited region,be it three-dimensional, twodimensional, or even one-dimensional ("crossover of one face from being earlier than the other to being later"). Thus it is enough to have (21.131) obtaining even on only a curved line in $\boldsymbol { \Sigma }$ to reject the six $g _ { i j }$ as inappropriate initial-value data.

That one can impose conditions on the $g _ { i j }$ and $\dot { g } _ { i j }$ which will guarantee existence and uniqueness of the solution $N ( x , y , z )$ ， $N _ { \mathfrak { i } } ( x , y , z )$ of the initial-value equations (21.126)and (21.127) is known as the“thin-sandwich conjecture,”a topic on which there has been much work by many investigators,but so far no decisive theorem.

To presuppose existence and uniqueness is to make the first step in giving mathematical content to Mach's principle that the distribution of massenergy throughout space determines inertia (821.12).

# \$21.10. THE TIME-SYMMETRIC AND TIME-ANTISYMMETRIC INITIAL-VALUE PROBLEMS

Turn from the general initial-value problem to two special initial-value problems that lend themselves to detailed treatment, one known as the time-symmetric initial-value problem,the other as the time-antisymmetric problem.

A 4-geometry is said to be time-symmetric when there exists a spacelike hypersurface $\pmb { \Sigma }$ at all points of which the extrinsic curvature vanishes.In this case the three initial value equations (21.127) are automatically satisfied,and the fourth reduces to a simple requirement on the three-dimensional scalar curvature invariant,

$$
R = 1 6 \pi \rho .
$$

Still further simplifications result when one limits attention to empty space. Simplest of all is the case of spherical symmetry in which (21.132) yields at once the full Schwarzschild geometry at the moment of time symmetry (two asymptotically flat spaces connected by a throat),as developed in exercise 21.20.

Consider a 3-geometry with metric

$$
d s _ { 1 } ^ { 2 } = g _ { ( 1 ) i k } d x ^ { i } d x ^ { k } .
$$

Call it a“base metric.” Consider another 3-geometry with metric

$$
d s _ { 2 } ^ { 2 } = \psi ^ { 4 } ( x ^ { i } ) d s _ { 1 } ^ { 2 } .
$$

Angles are identical in the two geometries. On this account they are said to be conformally equivalent. The scalar curvature invariants of the two 3-geometries are related by the formula [Eisenhart (1926)]

$$
{ \cal R } _ { 2 } = - 8 { \psi } ^ { - 5 } { \bf { \nabla } } { \bf { \overline { { { \psi } } } } } _ { 1 } ^ { 2 } \psi + { \psi } ^ { - 4 } { \cal R } _ { 1 } ,
$$

where

$$
\pmb { \nabla } _ { 1 } ^ { 2 } \psi = \psi _ { \mid i } ^ { \mid i } = g _ { 1 } ^ { \enspace - 1 / 2 } ( \partial / \partial x ^ { i } ) [ g _ { 1 } ^ { \enspace 1 / 2 } g ^ { i k } ( \partial \psi / \partial x ^ { k } ) ]
$$

Demand that the scalar curvature invariant $R _ { 2 }$ vanish,and arrive [Brill (1959)] at the “wave equation”

$$
\pmb { \nabla } _ { 1 } 2 \psi - ( R _ { 1 } / 8 ) \psi = 0
$$

for the conformal correction factor $\psi$ . Brill takes the base metric to have the form suggested by Bondi,

$$
d s _ { 1 } ^ { ~ 2 } = e ^ { 2 4 q _ { 1 } ( \rho , z ) } ( d z ^ { 2 } + d \rho ^ { 2 } ) + \rho ^ { 2 } d \phi ^ { 2 } ,
$$

and takes the conformal correction factor $\psi$ also to possess axial symmetry. In the application:

$q _ { 1 } ( \pmb { \rho } , z )$ measures the“distribution of gravitational wave amplitude,”assumed for simplicity.to vanish outside $r = ( \rho ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 } = a .$   
$\pmb { A }$ measures the “amplitude of the distribution of gravitational wave amplitude";   
$\psi ( \rho , z )$ is the conformal correction factor, which varies with position at large distances as $1 + ( m / 2 r )$ . The quantity $m ( \mathrm { c m } )$ is uniquely determined by the condition that the geometry be asymtotically flat. It measures the mass-energy of the distribution of gravitational radiation.

Wave amplitude determines mass-energy: $m = m ( A )$

The mass m of the gravitational radiation is proportional to $A ^ { 2 }$ for small values of the amplitude A. It is inversely proportional to the reduced wavelength $\lambda =$ (effective wavelength/ $^ { \prime } 2 \pi $ )that measures the scale of rapid variations in the gravitational wave amplitude $q _ { 1 } ( \pmb { \rho } , z )$ in the“active zone.”Thus the metric is dominated by wiggles, proportional in amplitude to $\pmb { A }$ ,in the active zone,and at larger distances dominated by something close to a Schwarzschild $( 1 + 2 m / r )$ factor in the metric.When the amplitude $\pmb { A }$ is increased,a critical value is attained, $A = A _ { \mathrm { c r i t } } ,$ at which $m$ goes to infinity and the geometry curves up into closure("universe closed by its own content of gravitational-wave energy"). Further analysis and examples will be found in Wheeler (1964a), pp.399-451, also in Wheeler (1964c).

Brill has carried out a similar analysis [Brill (l961)] for the vacuum case of what he calls time-antisymmetric initial-value conditions,sketched below as amended by York(1973).(l） The initial slice is maximal,T $\mathbf { \nabla } \cdot \kappa = 0 _ { : - } ( 2 )$ This slice is conformally flat,

$$
g _ { i j } = \psi ^ { 4 } \delta _ { i j } .
$$

(3) Work in the“base space" with metric $\delta _ { i j }$ and afterwards transform to the geometry (21.139). Three of the initial-value equations become

$$
K _ { \mathrm { b a s e , } j } ^ { i j } = 0 .
$$

To solve these equations, (l） take any localized trace-free symmetric tensor $B _ { k m }$ ； (2） solve the flat-space Laplace equation $\nabla ^ { 2 } A = ( 3 / 2 ) \partial ^ { 2 } B _ { k m } / \partial x ^ { k } \partial x ^ { m }$ for $\pmb { A }$ ； (3） define the six potentials $A _ { k m } = B _ { k m } + \frac { 1 } { 3 } A \ \delta _ { k m }$ and (4） calculate

$$
K _ { \mathrm { b a s e } } ^ { i j } = [ i k \ell ] [ j m n ] \partial ^ { 2 } A _ { k m } / \partial x ^ { \ell } \partial x ^ { n } ,
$$

that automaticallysatisfy (21.140)and give $\mathrm { T r } \kappa _ { \mathrm { b a s e } } = 0$ . Then $K ^ { i j } = \psi ^ { - 1 0 } K _ { \mathrm { b a s e } } ^ { i j } a l s o$ automatically satisfies these conditions,but now in the curved geometry (21.139). The final initial-value equation becomes a quasilinear elliptic equation, in the flat base space, for the conformal factor $\psi ,$

$$
8 \nabla _ { \mathrm { b a s e } } ^ { 2 } \psi + \psi ^ { - 7 } \sum _ { i , j } ( K _ { \mathrm { b a s e } i j } ) ^ { 2 } = 0 .
$$

The asymptotic form of $\psi$ reveals that the mass of the wave is positive.

In addition to the time-symmetric and time-antisymmetric cases, there are at least two further cases where the initial-value problem possess special simplicity. One is the case of a geometry endowed with a symmetry,as,for example,for the Friedmann universe of Chapter 27 or the mixmaster universe of Chapter 30 or cylindrical gravitational waves in the treatment of Kuchar (l97la). One starts with a spacelike slice on which the $g _ { i j }$ and $\pi ^ { i j }$ have a special symmetry, and makes allfuture spacelike slices in a way that preserves this symmetry. The geometry on any one of these simultaneities, though almost entirely governed by these symmetry considerations, still typically demands some countable number of parameters for its complete determination, such as the radius of the Friedmann universe, or the three principal radii of curvature of the mixmaster universe. These parameters and the momenta conjugate to them define a miniphase space. In this miniphase space, the dynamics runs its course as for any other problem of classcal dynamics [see,for example,Box 30.1 and Misner (1969) for the mixmaster universe; Kuchar (197la) and (l972) for waves endowed with cylindrical symmetry;and Gowdy (1973) for waves with spherical symmetry]. Even the evidence for the existence of many-fingered time, most characteristic feature of general relativity,is suppressed as the price for never having to give attention to any spacelike slice that departs from the prescribed symmetry.

Exercise 21.16. POOR MAN'S WAY TO DO COSMOLOGY Consider a spacetime with the metric

EXERCISES

$$
d s ^ { 2 } = \ - d t ^ { 2 } + \ a ^ { 2 } ( t ) [ d \chi ^ { 2 } + \sin ^ { 2 } \chi ( d \theta ^ { 2 } + \sin ^ { 2 } \theta \ d \phi ^ { 2 } ) ] ,
$$

corresponding to a 3-geometry- with the form of a sphere of radius $a ( t )$ changing with time. Show that the tensor of extrinsic curvature as expressed in a local Euclidean frame of reference is

$$
\pmb { K } = - \pmb { a } ^ { - 1 } ( d \pmb { a } / d t ) \pmb { \eta } ,
$$

where $\pmb { \eta }$ is the unit tensor. Show that the initial value equation (21.77) reduces to

$$
( 6 / a ^ { 2 } ) ( d a / d t ) ^ { 2 } + ( 6 / a ^ { 2 } ) = 1 6 \pi \rho ( a )
$$

[for the value of the second term on the left, see exercise l4.3 and Boxes l4.2 and 14.5], and explain why it is appropriate to write the term on the right as $6 a _ { 0 } / a ^ { 3 }$ for a“dust-filled model universe.” More generally,given any equation of state, $p = p ( \boldsymbol { \rho } )$ , explain how one can find $\rho = \rho ( a )$ from

$$
d ( \rho a ^ { 3 } ) = - p d ( a ^ { 3 } ) ;
$$

and how one can thus forecast the history of expansion and recontraction, $a = a ( t )$

# Exercise 21.17. THIN-SANDWICH VARIATIONAL PRINCIPLE FOR THE SCALAR POTENTIAL IN ELECTRODYNAMICS

(a) Choose the unknown $U ^ { m }$ in the expression

$$
\frac { 1 } { 8 \pi } g ^ { m n } \frac { \hat { c } \phi } { \hat { c } . { \bf x } ^ { m } } \frac { \hat { c } \phi } { \hat { c } . { \bf x } ^ { n } } + U ^ { m } \frac { \hat { c } \phi } { \hat { c } x ^ { n } }
$$

in such a way that this expression, multiplied by the volume element $g ^ { 1 / 2 } d ^ { 3 } x$ ,and integrated over the simultaneity $\pmb { \Sigma }$ , is extremized by a $\phi .$ ,and only by a $\phi$ 、that satisfies the initial-value equation (21.108) of electrodynamics.

(b) Show that the resulting variational principle,instead of having to be invented “out of the blue,”is none other than what follows directly from the action principle build on the Lagrangian density (21.l00) of electrodynamics (independent variation of $\phi$ and the three $A _ { i }$ everywhere between the two faces of a sandwich to extremize $\boldsymbol { I }$ ,subject only to the prior specification of the $A _ { i }$ on the two faces of the sandwich,in the limit where the thickness of the sandwich goes to zero).

# ExerciSe 21.18. THIN-SANDWICH VARIATIONAL PRINCIPLE FOR THE LAPSE AND SHIFT FUNCTIONS IN GEOMETRODYNAMICS

(a)Extremize the action integral

$$
\begin{array} { l } { { I _ { 3 } = \displaystyle \int \left\{ [ R - ( \mathrm { T r } K ) ^ { 2 } + \mathrm { T r } K ^ { 2 } - 2 T _ { n n } ^ { * } ] N \right. } } \\ { { \left. - 2 T _ { n } ^ { * k } N _ { k } \right\} g ^ { 1 / 2 } d ^ { 3 } x } } \end{array}
$$

with respect to the lapse and shift functions,and show that one arrives in this way at the four initial-value equations of geometrodynamics. It is understood that one has given the six $g _ { i j }$ and the six $\partial g _ { i j } / \partial t$ on the simultaneity where the analysis is being done. The extrinsic curvature is considered to be expressed as in (21.67) in terms of these quantities and the lapse and shift. The energy density and energy fow are referred to a unit normal vector $\pmb { n }$ and three arbitrary coordinate basis vectors ${ \pmb e } _ { i }$ within the simultaneity,as earlier in this chapter,and the asterisk is an abbreviation for an omitted factor of ${ \tt 8 \pi }$

(b) Derive this variational principle from the ADM variational principle by going to the limit of an infinitesimally thin sandwich [see derivation in Wheeler (1964)].

# Exercise 21.19. CONDENSED THIN-SANDWICH VARIATIONAL PRINCIPLE

(a）Extremize the action $I _ { 3 }$ of the preceding exercise with respect to the lapse function $N .$ (b) What is the relation between the result and the principle that $^ { 6 6 } 3$ -geometry is a carrier of information about time"? (c) By elimination of $N _ { \ast }$ ,arrive at a“condensed thin-sandwich variational principle”in which the only quantities to be varied are the three shift functions $N _ { i }$

# Exercise 21.20. POOR MAN'S WAY TO SCHWARZSCHILD GEOMETRY

On curved empty space evolving deterministically in time, impose the conditions (l） that it possess a moment of time-symmetry, a spacelike hypersurface, the extrinsic curvature of which,withespectenelopingspaceti,isvererezerond2)thattisscelike hypersurface be endowed with spherical symmetry. Write the metric of the 3-geometry in the form

$$
d s ^ { 2 } = \psi ^ { 4 } ( \overline { { { r } } } ) ( d \overline { { { r } } } ^ { 2 } + \overline { { { r } } } ^ { 2 } d \theta ^ { 2 } + \overline { { { r } } } ^ { 2 } \sin ^ { 2 } \theta d \phi ^ { 2 } ) .
$$

From the initial-value equation (21.127),show that the conformal factor $\psi$ up to a multiplicative factor must have the form $\psi = ( 1 + m / 2 \overline { { r } } )$ .Show that the proper circumference $2 \pi \overline { n } \ell ^ { 2 } ( \overline { r } )$ assumes a minimum value at a certain value of $\widetilde { \pmb { r } } ,$ thus defining the throat of the 3-geometry. Show that the 3-geometry is mirror-symmetric with respect to reflection in this throat in the sense that the metric is unchanged in form under the substitution $r ^ { \prime } = m ^ { 2 } / 4 \overline { { r } } .$ Find the transformation from the conformal coordinate $\widetilde { \pmb { r } }$ to the Schwarzschild coordinate $\boldsymbol { r } .$

# \$21.11. YORK'S "HANDLES" TO SPECIFY A 4-GEOMETRY

On a simultaneity-or on the simultaneity-of extremal proper volume, give the conformal part of the 3-geometry and give the two inequivalent components of the dynamically conjugate momentum in order (l） to have freely specifiable, but also complete,initial-value data and thus (2) to determine completely the whole generic four-dimensional spacetime manifold.This in brief is York's extension (1971,1972b) to the generic case of what Brill did for special cases (see the preceding section). York and Brill acknowledge earlier considerations of Lichnerowicz (1944)and Bruhat (1962 and earlier papers cited there on conformal geometry and the initial-value problem). But why conformal geometry,and why pick such a special spacelike hypersurface on which to give the four dynamic data per spacepoint?

Few solutions of Maxwell's equations are simpler than an infinite plane monochromatic wave in Minkowski's fat spacetime,and few look more complex when examined on a spacelike slice cut through that spacetime in an arbitrary way,with local wiggles and waves,larger-scale lumps and bumps,and still larger-scale general curvatures. No one who wants to explore electrodynamics in its evolution with many-fingered time can avoid these complexities；and no one will accept these complexities of many-fingered time who wants to see the degrees of freedom of the electromagnetic field in and by themselves exhibited in their neatest form.He will pick the simplest kind of timelike slice he can find. On that simultaneity, there are two and only two field coordinates, and two and only two feld momenta per spacepoint. Similarly in geometrodynamics.

When one wants to untangle the degrees of freedom of the geometry, as distinct from analyzing the dynamics of the geometry, one therefore retreats from the three items of information per-spacepoint that are contained in a 3-geometry [or in any other way of analyzing the geometrodynamics,as especially seen in the “extrinsic time” formulation of Kuchar (1971b and 1972)] and following York (l） picks the simultaneity to have maximal proper volume and (2) on this simultaneity specifies the two “coordinate degrees of freedom per spacepoint’ that are contained in the conformal part of the 3-geometry.

The degrees of freedom of the geometry in brief

An element of proper volume $g ^ { 1 / 2 } d ^ { 3 } x$ on the spacelike hypersurface $\pmb { \Sigma }$ undergoes, in the next unit interval of proper time as measured normal to the hypersurface, a fractional increase of proper volume [see Figure 21.3 and equations 21.59 and 21.66] given by

# Pick hypersurface of extremal proper volume

$$
- \mathrm { T r } { \pmb { K } } = - \frac 1 2 g ^ { - 1 / 2 } \mathrm { T r } { \pmb { \pi } } .
$$

For the volume to be extremal this quantity must vanish at every point of $\pmb { \Sigma }$ This condition is satisfed in a Friedmann universe (Chapter 27) and in a Taub universe (Chapter 3O) at that value of the natural time-coordinate $t$ at which the universe switches over from expansion to recontraction. It is remarkable that the same condition on the choice of simultaneity, $\pmb { \Sigma }$ ,lets itself be formulated in the same natural way,

$$
\mathrm { T r } { \cal K } = 0 ~ \mathrm { o r ~ T r } \pi = 0 ,
$$

for a closed universe altogether deprived of any symmetry whatsoever. Alternatively, one can deal with a spacetime that is topologically the product of an open 3-space by the real line (time). Then it is natural to think of specifying the location in it of a bounding spacelike 2-geometry $s$ with the topology of a 2-sphere. Then one has many ways to fil in the interior of $s$ with a spacelike 3-geometry $\pmb { \Sigma }$ ; but of all these $\pmb { \Sigma }$ 's,only the one that is extremal,or only the ones that are extremal,satisfy (21.144).

Who is going to specify this 2-geometry with the topology of a 2-sphere? The choice of that 2-geometry is not a matter of indifference. In a given 4-geometry, distinct choices for the bounding 2-geometry willordinarily give distinct results for the extremizing 3-geometry,and therefore different choices for the “initial-value simultaneity,” $\pmb { \Sigma }$ . No consideration immediately thrusts itself forward that would give preference to one choice of 2-geometry over another. However, no such infinity of options presents itself when one limits attention to a closed 3-geometry. Therefore it will give concreteness to the following analysis to consider it applied to a closed universe, even though the analysis surely lets itself be made well-defined in an open region by appropriate specification of boundary values on the closed 2-geometry that bounds that open region. In brief, by limiting attention to a closed 3-geometry, one lets the obvious condition of closure take the place of boundary conditions that are not obvious.

York's analysis remains simple when his extrinsic time

$$
\tau = \frac { 2 } { 3 } g ^ { - 1 / 2 } \operatorname { T r } \pmb { \eta } = \frac { 4 } { 3 } \operatorname { T r } \pmb { K }
$$

has any constant value on the hypersurface, not only the value $\tau = 0$ appropriate for the hypersurface of extremal proper volume.

On the simultaneity $\pmb { \Sigma }$ specified by the condition of constant extrinsic time, $\tau =$ constant, begin by giving the conformal 3-geometry,

$$
< = ^ { ( 3 ) } < = \left( \begin{array} { l } { { \mathrm { t h e ~ e q u i v a l e n c e ~ c l a s s ~ o f ~ a l l ~ t h o s e ~ p o s i t i v e ~ d e f i n i t e } } } \\ { { \mathrm { R i e m a n n i a n ~ t h r e e - d i m e n s i o n a l ~ m e t r i c s ~ t h a t ~ a r e } } } \\ { { \mathrm { e q u i v a l e n t ~ t o ~ e a c h ~ o t h e r ~ u n d e r ~ ( 1 ) ~ d i f f e o m o r p h i s m } } } \\ { { \mathrm { ( s m o o t h ~ s l i d i n g ~ o f ~ t h e ~ p o i n t s ~ o v e r ~ t h e ~ m a i n i f o l d ~ t o ) } } } \\ { { \mathrm { n e w ~ l o c a t i o n s ~ o r ~ ( 2 ) ~ c h a n g e s ~ o f ~ s c a l e ~ t h a t ~ v a r y } } } \\ { { \mathrm { s m o o t h y ~ f r o m ~ p o i n t ~ t o ~ p o i n t , ~ l e a s i n g ~ f i x e d ~ a l l } } } \\ { { \mathrm { l o c a l ~ a n g l e s ~ ( r a t i o s ~ o f ~ l o c a l ~ d i s t a n c e s ) , ~ b u t } } } \\ { { \mathrm { c h a n g i n g ~ l o c a l ~ d i s t a n c e s ~ t h e r w s ~ o r ~ ( 3 ) ~ b o t h } } } \end{array} \right)
$$

The conformal 3-geometry is a geometric object that lends itself to definition and interpretation quite apart from the specific choice of coordinate system and even without need to use any coordinates at all. The conformal 3-geometry (on the hypersurface $\pmb { \Sigma }$ where T= constant） may be regarded much as one regards the magnetic feld in electromagnetism. The case of conformally flat 3-geometry,

$$
d s ^ { 2 } = \psi ^ { 4 } ( x , y , z ) d s _ { \mathrm { b a s e } } ^ { 2 }
$$

(with $g _ { i j b a s e } = \delta _ { i j }$ , is analogous to those initial-value situations in electromagnetism where the magnetic feld is everywhere zero (the time-antisymmetric initial-value problemof Bril);utnow weconsider thecaseofgenral $d s _ { \mathrm { b a s e } } ^ { 2 }$

The six metric coefficients $g _ { i j }$ of the conformal 3-geometry, subject to being changed by change of the three coordinates $x ^ { i }$ ,and undetermined at any one point up to a common position-dependent multiplicative factor,carry $6 - 3 - 1 = 2$ pieces of information per spacepoint. In this respect, they are like the components of the divergenceless magnetic field $\boldsymbol { \mathcal { B } }$ The corresponding field momentum $\pi _ { E M } ^ { i } \propto \delta ^ { i }$ (Box 21.1, page 496) has its divergence specified by the charge density,and so also carries

two pieces of information (in addition to the prescribed information about the density of charge) per spacepoint. （

The comparison is a little faulty between the components of $\boldsymbol { \mathcal { B } }$ and the metric coefficients. They are more like potentials than like components of the physically relevant field.

The appropriate measure of the “field” in geometrodynamics is the curvature tensor; but how can one possibly define a curvature tensor for a geometry that is asrudimentary as a conformal 3-geometry? York (l97l) has raised and answered this question. The Weyl conformal-curvature tensor [equation (l3.50) and exercise 13.13] is independent [in the proper $\textstyle { { \binom { 2 } { 2 } } }$ representation], in spaces of higher dimensionality,of the position-dependent factor $\psi ^ { \pm }$ with which one multiplies the metric coeffcients,but vanishes identically in three-dimensional space (exercise 21.21). One arrives at a non-zero conformally invariant measure of the curvature only when one goes to one higher derivative (exercise 21.22). In this way,one comes to York's curvature ${ \widetilde { \beta } } ^ { a \delta }$ ,here called $Y ^ { a b }$ , a tensor density with these properties:

York's curvature tensor

$$
\begin{array} { c } { { Y ^ { a b } = Y ^ { b a } ( \mathrm { s y m m e t r i c } ) ; } } \\ { { { } } } \\ { { Y _ { a } ^ { a } = 0 ( \mathrm { t r a c e l e s s } ) ; } } \\ { { { } } } \\ { { Y ^ { a b } { } _ { | b } = 0 ( \mathrm { t r a n s v e r s e } ) ; } } \end{array}
$$

$Y ^ { a b }$ invariant with respect to position-dependent changes in the conformal scale factor;

$Y ^ { a b } = 0$ when and only when the 3-geometry is conformally fat

$Y ^ { a b }$ provides what York calls the pure spin-two representation of the 3-geometry intrinsic to $\pmb { \Sigma }$ .It is the analog of the field $\mathcal { B }$ of electrodynamics on the spacelike initial-value simultaneity.It directly carries physical information about the conformal 3-geometry.

In addition to the conformal geometry $^ { ( 3 ) } <$ ,specified by the“potentials” $g _ { i j } / g ^ { 1 / 3 }$ ， and measured -by the “field components” $\gamma ^ { i j }$ ，one must also specify on $\pmb { \Sigma }$ the corresponding conjugate momenta:

$$
\widetilde { \pi } ^ { a b } = \widetilde { \pi } ^ { a b } ( \mathrm { s y m m e t r i c } ) ; \widetilde { \pi } _ { a } ^ { a } = 0 ( \mathrm { t r a c e l e s s } ) ;
$$

$\widetilde { \overline { { { \tau } } } } ^ { a \delta } { } _ { \mathfrak { i } \mathfrak { b } } = 0$ (transverse)incase thereisnofowofnergy in space;otherwise

$$
\widetilde { \pi } \sp { a b } \sb { | b } = 8 \pi ( { \mathrm { d e n s i t y ~ o f ~ f i o w ~ o f ~ e n e r g y } } ) \sp a ;
$$

two pieces of information (in addition to the prescribed information about the flow of energy) per spacepoint.

It might appear to be essential to specify with respect to which of the 3-geometries, distinguished from one another by different values of the conformal factor one calculates the covariant derivatives of tensor densities of weight $5 / 3$ (see $\ S 2 1 . 2 )$ in (21.148)and (21.149). However, York has shown that the conditions (21.149) do not in any way depend on the value of the conformal factor $\psi ^ { \pm }$

These equations (21.149) for what York calls the “momentum density of weight $5 / 3$ ”

$$
{ \widetilde { \pi } } ^ { a b } = g ^ { 1 / 3 } \biggl ( \pi ^ { a b } - { \frac { 1 } { 3 } } g ^ { a b } \mathrm { T r } \pi \biggr ) ,
$$

are linear,and therefore lend themselves to analysis by standard methods. It is a great help in this enterprise that York (l973a,b) has provided a “conformally invariant orthogonal decomposition of symmetric tensors on Riemannian manifolds” that allows one to generate solutions of these requirements ("transverse traceless,”“conformal Killing,” and “trace” parts,respectively, measure deformation of conformal part of geometry,mere recoordinatization, and change of scale). It is a further assistance,as York notes,that one has the same $\widetilde { \tau } ^ { a b }$ for an entire conformal equivalence class of metrics; that is, for a given

$$
\tilde { g } _ { a b } = g ^ { - 1 / 3 } g _ { a b } ,
$$

no matter how different the $g _ { a b }$ and $\psi$ themselves may be.

The conformal 3-geometry and the “momentum density of weight $5 / 3 "$ once picked,the remaining initial-value equation (21.116） then becomes the “scale” equation,

$$
8 { \pmb \nabla } ^ { 2 } \psi - { \ O ^ { ( 3 ) } } R \psi + M \psi ^ { - 7 } + Q \psi ^ { - 3 } - \frac { 3 } { 8 } \tau ^ { 2 } \psi ^ { 5 } = 0 ,
$$

for the determination of the conformal factor $\psi$ Here ${ \pmb { \nabla } } ^ { 2 }$ stands for the Laplacian

$$
\nabla ^ { 2 } \psi \equiv g ^ { - 1 / 2 } ( \partial / \partial x ^ { a } ) g ^ { 1 / 2 } g ^ { a b } ( \partial \psi / \partial x ^ { b } ) .
$$

It, like $^ { ( 3 ) } R , M ,$ and $Q$ ,refers to the base space. It is interesting that

$$
\nabla ^ { 2 } - \frac { 1 } { 8 } { } ^ { ( 3 ) } R
$$

is a conformally invariant wave operator, whereas ${ \pmb { \nabla } } ^ { 2 }$ itself is not. The quantity $M$ in York's analysis is an abbreviation for

$$
M \equiv g ^ { - 5 / 3 } g _ { a c } g _ { b d } \widetilde { \overline { { { \pi } } } } { } ^ { a b } \widetilde { \overline { { { \pi } } } } { } ^ { c d } ,
$$

and

$$
Q \equiv 1 6 \pi \rho _ { \mathrm { b a s e } } ( = 1 6 \pi \psi ^ { 8 } \rho = 1 6 \pi \psi ^ { 8 } \rho _ { \mathrm { i n f i n a l 3 - g e o m e t r y } } ) .
$$

One seeks a solution $\psi$ that is continuous over the closed manifold and everywhere real and positive.When does such a solution $\psi$ of the elliptic equation (21.152) exist? When is it unique? Always (when $M > 0$ and $\tau \neq 0$ ),is the result of O'Murchadha and York (1973); see also earlier investigations of Choquet-Bruhat (l972). Some of the physical considerations that come into this kind of problem have been discussed by Wheeler (1964a,pp.370-381).

# \$21.12. MACH'S PRINCIPLE AND THE ORIGIN OF INERTIA

In my opinion the general theory of relativity can only solve this problem [of inertia] satisfactorily ifit regardsthe world as spatially self-enclosed.

ALBERT EINSTEIN(1934),p.52.

On June 25,1913,two years before he had discovered the geometrodynamic law that bears his name, Einstein (1913b) wrote to Ernst Mach (Figure 21.5) to express his appreciation for the inspiration that he had derived for his endeavors from Mach's ideas.In his great book,The Science of Mechanics,Mach [(l9l2), Chapter 2, section 6] had reasoned that it could not make sense to speak of the acceleration of a mass relative to absolute space.Anyone trying to clear physics of mystical ideas would do better,he reasoned, to speak of acceleration relative to the distant stars. But how can a star at a distance of $1 0 ^ { 9 }$ light-years contribute to inertia in the here and the now? To make a long story short, one can say at once that Einstein's theory (l) identifies gravitation as the mechanism by which matter there infuences inertia here;(2) says that this coupling takes place on a spacelike hypersurface [in what one,without a closer examination,might mistakenly think to be a violation of the principle of causality; see Fermi(l932) for a discussion and clarification of the similar apparent paradox in electrodynamics； see also Einstein (1934),p. 84:“Moreover I believed that I could show on general considerations a law of gravitation invariant in relation to any transformation of coordinates whatever was inconsistent with the principle of causation. These were errors of thought which cost me two years of excessively hard work,until I finally recognized them as such at the end of 1915"]; (3) supplies in the initial-value equations of geometrodynamics a mathematical tool to describe this coupling; (4) demands closure of the geometry in space [one conjectures; see Wheeler (1959,1964c) and Honl (l962)],as a boundary condition on the initial-value equations if they are to yield a well-determined [and,we know now, a uniquel 4-geometry; and (5) identifies the collection of local Lorentz frames near any point in this resulting spacetime as what one means quantitatively by speaking of inertia at that point. This is how one ends up with inertia here determined by density and flow of mass-energy there.

No violation of causality. despite appearances

There are many scores of papers in the literature on Mach's principle, including many-even one by Lenin (English translation,l927)-one could call anti-Mach-ian; and many of them make interesting points [see especially the delightful dialog by Weyl (1924a) on “inertia and the cosmos,”and the article (1957) and book (1961) of Sciama]. However, most of them were written before one had anything like the understanding of the initial-value problem that one possesses today. Therefore no (continued on page 546)

An enormous literature

4.25. 13

Tth remen Xu Rullcyt:

![](images/26ab03acd4b355449e778035c1f7d3ba6ce56404457e7e2a16087b9da9356cd0.jpg)  
Figure 21.5. Einstein's appreciation of Mach,writen to Ernst Mach June 25,1913,while Einstein was working hard atarriving at the final November l915 formulationof standard general relativity.Regarding confirmation at a forthcoming eclipse:“If so,then your happy investigations on the foundations of mechanics,Planck's unjustified criticism notwithstanding,willreceive brilliant confrmation.For it necessarily turns out that inertia originates in a kind of interaction between bodies.quite in the sense of your considerations on Newton's pail experiment. The first consequence is on p. 6 of my paper. The following additional points emerge:(1) If one accelerates a heavy shellof matter S. then a mass enclosed by that shell experiences an accelerative force.(2) If one rotates the shell relative to the fixed stars about an axis going through its center,a Coriolis force arises in the interior of the shell; that is,the plane of a Foucault pendulum is dragged around (with a practically unmeasurably small angular velocity).”Following the death of Mach,Einstein (l916a）wrote a tribute to the man and his work.Reprinted with the kind permission of the estate of Albert Einstein, Helen Dukas and Otto Nathan,executors.

hku ja， afelren Hu guuk Mntersuihungm aibn du gunidlayu lin Mulum.k-Dlnch's.mguechr. pitgtu Kutk ju.hot-mi glinywa sestitiyry.Oemy daes'du Liyhuit  unu tix Wehuelmivhmmg n Hirpu hum gy uhn Sinu -Vneuch.

1) Bemhlemmiyt e wu tnir Puyelrhel yx ufiht uach der Thesria etm t -

![](images/2dc9fd12fe698d2cf07fcb50b35791108343556cba85017ea3ee57c79b290063.jpg)

Mingeloysmur Kirpu Lui tieeilha.   
\~guude .Kraft   
21Rter su tllnl Y hm eiu clureh lru. Miteyumkt geluuu Ala   
(ulatrr r Yyutm du Eetru(rut   
iyetuu)，u eltlt r   
  
klu"gierhudryktt)y "lo ei uu 'eue yrrut Trud   
Hhu. da mtul m hiuu,   
ru! Jte Kth Dlahe m   
zhm imn hirli \~mgnuh!   
futyt uoclulua mu. Mit grisern Hrhuchluug guur   
Llue hnylicl Lkr ugelmu it.生te\~. Js duwh iIlve huyke i   
thmy huB

attempt will be made to summarize or analyze the literature, which would demand a book in itself. Moreover, Mach's principle as presented here is more sharply formulated than Einstein ever put it in the literature [except for his considerations arguing that the universe must.be closed; see Einstein's book (l950),Pp. 107-108]; and Mach would surely have disowned it,for he could never bring himself to accept general (or even special) relativity.Nevertheless,it is a fact that Mach's principlethat mater there governs inertia here--and Riemann's idea--that the geometry of space responds to physics and participates in physics-were the two great currents of thought which Einstein,by means of his powerful equivalence principle,brought together into the present-day geometric description of gravitation and motion.

"Specify everyhere thedistribution andfowofmas-energy and thereby determine the inertial properties of every test particle everywhere and at all times". Spelled out, this prescription demands (l) a way of speaking about “everywhere": a spacelike hypersurface $\pmb { \Sigma }$ .Let one insist-in conformity with Einstein-(2) that it be a closed 3-geometry, and for convenience, not out of necesity, (3) that $\boldsymbol { \tau }$ be independent of position on $\pmb { \Sigma }$ . (4) Specify this 3-geometry to the extent of giving the conformal metric; without the specification of at least this much 3-geometry, there would be no evident way to say “where” the mas-energy is to be located. (5） Give density $\rho _ { \tt b a s e }$ as a function of position in this conformal 3-geometry. (6) Recognize that giving the mass-energy only of fields other than gravity is an inadequate way to specify the distribution of mas-energy throughout space. Formalistically,to be sure, the gravitational felds does not and cannot make any contribution to the source term that stands on the righthand side of Einstein's field equation. However, the analysis of gravitational waves (Chapters 18 and 35) shows that perturbations in the geometry ofscale small compared to the scale of observation have to be regarded as carrying an effective content of mass-energy. Moreover, one has in a geon [Wheeler(1955); Brilland Hartle (1964); for more on gravitational-wave energy, see $\ S 3 5 . 1 4 ]$ an object built out of gravitational waves (or electromagnetic waves, or neutrinos,or any combination of the three) that holds itself together for a time that is long in·comparison to the characteristic period of vibration of the waves.It looks from a distance like any other mass,even though nowhere in its interior can one put a finger and say “here is mass.” Therefore it, like any other mass,must have “its infuence on inertia.”But to specify this mass,one must give enough information to characterize completely the gravitational waves on the simultaneity $\pmb { \Sigma }$ . For this,it is not enough merely to have given the two “wave-coordinates” per spacepoint that one possesses in $^ { ( 3 ) } <$ . One must give in addition (7) the two “wave-momenta" per spacepoint that appear in York's “momentum density ofweight $5 / 3 , \ " \approx \mathbf { a } \mathbf { b }$ ; and at the same time,as an inextricable part of this operation, one must (8) specify the density of flow of field energy. (9) Solve for the conformal factor $\psi .$ (10)Then one has complete initial-value data that satisfy the initial-value equations of general relativity. (ll） These data now known, the remaining, dynamic, components of the field equation determine the 4-geometry into the past and the future.(l2) In this way,the inertial properties of every test particle are determined everywhere and at all times,giving concrete realization to Mach's principle.

Much must still be done to spell out the physics behind these equations and to see this physics in action. Some significant progress had already been made in this direction before the present stage in one's understanding of the initial-value equations.Especially interesting are results of Thirring (1918)and (1921) and of Thiring and Lense (1918),discussed by Einstein (195O) in the third edition of his book, The Meaning of Relativity.

Consider a bit of solid ground near the geographic pole, and a support erected there,and from it hanging a pendulum. Though the sky is cloudy, the observer watches the track of the Foucault pendulum as it slowly turns through. $3 6 0 ^ { \circ }$ . Then the sky clears and, miracle of miracles, the pendulum is found to be swinging all the time on an arc fixed relative to the far-away stars.If“mass there governs inertia here,” as envisaged by Mach, how can this be?

The Foucault pendulum

Enlarge the question. By the democratic principle that equal masses are created equal, the mass of the earth must come into the bookkeeping of the Foucault pendulum. Its plane of rotation must be dragged around with a slight angular velocity, $\omega _ { \tt d r a g } ,$ relative to the so-called “fixed stars.” How much is $\omega _ { \mathrm { d r a g } } ?$ And how much would $\omega _ { \tt d r a g }$ be if the pendulum were surrounded by a rapidly spinning spherical shell of mass $M$ and radius $R _ { \mathrm { s h e l l } } ,$ turning at angular velocity $\omega _ { \mathrm { s h e l l } } ?$

Einstein's theory says that inertia is a manifestation of the geometry of spacetime. It also says that geometry is affected by the presence of mater to an extent proportional to the factor $G / c ^ { 2 } = 0 . 7 4 2 \times 1 0 ^ { - 2 8 } \mathrm { c m / g }$ Simple dimensional considerations leave no room except to say that the rate of drag is proportional to a expression of the form

The dragging of the inertial frame

$$
\omega _ { \mathrm { d r a g } } = k \frac { G } { c ^ { 2 } } \frac { m _ { \mathrm { s h e l l , c o n v } } } { R _ { \mathrm { s h e l l } } } \omega _ { \mathrm { s h e l l } } = k \frac { m _ { \mathrm { s h e l l } } } { R _ { \mathrm { s h e l l } } } \omega _ { \mathrm { s h e l l } } .
$$

Here $k$ is a numerical factor to be found only by detailed calculation. Lense and Thirring [(l918) and (l92l)], starting with a flat background spacetime manifold, calculated in the weak-field approximation of Chapter 18 the effect of the moving current of mass on the metric. Expressed in polar coordinates,the metric acquires a non-zero coefficient $g _ { \phi t }$ .Inserted into the equation of geodesic motion, this offdiagonal metric coefficient gives rise to a precession. This precession (defined here about an axis parallel to the axis of rotation, not about the local vertical) is given by an expression of the form (21.155),where the precession factor $k$ has the value

$$
k = 4 / 3 .
$$

There is a close parallelism between the magnetic component of the Maxwell field and the precession component of the Einstein field. In neither field does a source at rest produce the new kind of effect when acting on a test particle that is also at rest. One designs a circular current of charge to produce a magnetic feld; and a test charge,in order to respond to this magnetic field,must also be in motion. Similarly here: no pendulum vibration means no pendulum precession. Moreover, the direction of the precession depends on where the pendulum is,relative to the rotating shell of mass. The precession factor $k$ has the following values:

$k = 4 / 3$ for pendulum anywhere inside rotating shell of mass;

$k = 4 / 3$ for pendulum at North or South pole; $k = - 2 / 3$ for pendulum just outside the rotating shell at its equator.

This position-dependence of the drag, $\omega _ { \tt d r a g } ,$ makes still more apparent the analogy with magnetism,where the field of a rotating charged sphere points North at the center of the sphere,and North at both poles,but South at the equator.

Whether the Foucault pendulum is located in imagination at the center of the earth or in actuality at the North pole,the order of magnitude of the expected drag is

$$
\begin{array} { c l c r } { \omega _ { \mathrm { d r a g } } \sim \displaystyle \frac { m _ { \mathrm { e a r t h } } } { R _ { \mathrm { e a r t h } } } \omega _ { \mathrm { e a r t h } } \sim \frac { 0 . 4 4 \mathrm { c m } } { 6 \times 1 0 ^ { 8 } \mathrm { c m } } \frac { \mathrm { l } \mathrm { r a d i a n } } { 1 3 7 0 0 \mathrm { s e c } } } \\ { \sim 5 \times 1 0 ^ { - 1 4 } \mathrm { r a d / s e c } , } \end{array}
$$

too small to allow detection, let alone actual measurement, by any device so far built--but perhaps measurable by gyroscopes now under construction $( \ S 4 0 . 7 )$ .By contrast, near a rapidly spinning neutron star or near a black hole endowed with substantial angular momentum, the calculated drag effect is not merely detectable; it is even important (see Chapter 33 on the physics of a rotating black hole).

The distant stars must influence the natural plane of vibration of the Foucault pendulum as the nearby rotating shell of matter does,provided that the stars are not so far away ( $r \sim$ radius of universe) that the curvature of space begins to introduce substantial corrections into the calculation of Thirring and Lense.In other words,no reason is apparent why all masses should not be treated on the same footing,so that (21.158) more appropriately,if also somewhat symbolically,reads

$$
\omega _ { \mathrm { p l a n e o f } } \sim \frac { m _ { \mathrm { s h e l l } } } { R _ { \mathrm { s h e l l } } } \omega _ { \mathrm { s h e l l } } + \sum _ { \mathrm { f a r - a w a y } } \frac { m _ { \mathrm { * } _ { \mathrm { s t a r } } } , } { r _ { \mathrm { * } _ { \mathrm { s t a r } } } , } \omega _ { \mathrm { * } _ { \mathrm { s t a r } } } , .
$$

Moreover, when there is no nearby shell of matter,or when it has negligible effects, the plane of vibration of the pendulum,if experience is any guide, cannot turn with respect to the frame defined by the far-away “stars.” In this event $\omega _ { \mathtt { F o u c a u l t } }$ must be identical with $\omega _ { \tt s t a r s }$ or the“sum for inertia,”

$$
\sum _ { \mathrm { f a r - a w } \mathrm { a y } } \frac { m _ { \mathrm { * } } } { r _ { \mathrm { * } \mathrm { s t a r } ^ { \mathrm { s } } } } { \sim } \frac { m _ { \mathrm { u n i v e r s e } } } { r _ { \mathrm { u n i v e r s e } } } ,
$$

must be of the order of unity.Just such a relation of approximate identity between the mass content of the universe and its radius at the phase of maximum expansion is a characteristic feature of the Friedman model and other simple models of a closed universe (Chapters 27 and 30). In this respect, Einstein's theory of Mach's principle exhibits a satisfying degree of self-consistency.

At phases of the dynamics of the universe other than the stage of maximum expansion, $r _ { \mathrm { u n i v e r s e } }$ can become arbitrarily small compared to $m _ { \mathrm { u n i v e r s e } }$ . Then the ratio (21.160) can depart by powers of ten from unity. Regardless of this circumstance, one has no option but to understand that the effective value of the “sum for inertia” is still unity after all corrections have been made for the dynamics of contraction or expansion,for retardation, etc. Only so can $\omega _ { \mathbf { F o u c a u l t } }$ retain its inescap-able identity with $\omega _ { \tt f a r }$ away starg-Fortunately,one does not have to pursue the theology of the“sum for inertia”to the uttermost of these sophistications to have a proper account of inertia. Mach's idea that mass there determines inertia here has its complete mathematical account in Einstein's geometrodynamic law,as already speled out.For-the first strong-field analysis of the dragging of the inertial reference system in the context of relativistic cosmology, see Brill and Cohen (1966) and Cohen and Brill (1967)； see also $\ S 3 3 . 4$ for dragging by a rotating black hole.

Still another clarification is required of what Mach's principle means and how it is used.The inertial properties of a test particle are perfectly well-determined when that particle is moving in ideal Minkowski space.“Point out, please,” the anti-Machian critic says,“the masses that are responsible for this inertia.”In answer,recall that Einstein's theory includes not only the geometrodynamic law, but also, in Einstein's view,the boundary condition that the universe be closed.Thus the section of spacetime that is flat is to be viewed, not as infinite,but as part of a closed universe. (For a two-dimensional analog,fill a rubber balloon with water and set it on a glass tabletop and look at it from underneath). The part of the universe that is curved acquires its curvature by reason of its actual content of mass-energy or--if animated only by gravitational waves-by reason of its effective content of mass-energy. This mass-energy,real or effective,is to be viewed as responsible for the inertial properties of the test particle that at first sight looked all alone in the universe.

It in no way changes the qualitative character of the result to turn attention to a model universe where the region of Minkowski flatness,and all the other linear dimensions of the universe, have been augmented tenfold("ten times larger balloon; ten times larger face"). The curvature and density of the curved part of the model universe are down by a factor of 10o, the volume is up by a factor of 1,000,the mass is up by a factor of 1O;but the ratio of mass to radius, or the“sum for inertia” (the poor man's substitute for a complete initial-value calculation) is unchanged.

Einstein acknowledged a debt of parentage for his theory to Mach's principle (Figure 21.5). It is therefore only justice that Mach's principle should in return today owe its elucidation to Einstein's theory.

Minkowski geometry as limit of a closed 3-geometry

# Exercise 21.21. WHY THE WEYL CONFORMAL CURVATURE TENSOR VANISHES

# EXERCISES

How many independent components does the Riemann curvature tensor have in threedimensional space? How many does the Ricci curvature tensor have? Show that the two tensors are related by the formula

$$
\begin{array} { c } { { R ^ { d } { } _ { a b c } = \delta _ { b } ^ { d } R _ { a c } - \delta _ { c } ^ { d } R _ { a b } + g _ { a c } R ^ { d } { } _ { b } - g _ { a b } R _ { c } ^ { d } } } \\ { { { } } } \\ { { + \displaystyle { \frac { 1 } { 2 } R ( \delta _ { c } ^ { d } g _ { a b } - \delta _ { b } ^ { d } g _ { a c } ) } } } \end{array}
$$

with no need of any Weyl conformal-curvature tensor to specify (as in higher dimensions) the further details of the Riemann tensor. Show that the Weyl tensor, from an $\pmb { n }$ -dimensional modification of equation (l3.50) as in exercise l3.l3,vanishes for $n = 2$

# Exercise 21.22. YORK'S CURVATURE

[York (197l)]. (a) Define the tensor [Eisenhart (1926)]

$$
R _ { a b c } = R _ { a b \mid c } - R _ { a c \mid b } + { \frac { 1 } { 4 } } ( g _ { a e } R _ { \mid b } - g _ { \pi b } R _ { 1 \bar { c } } ) .
$$

(b) Show that a 3-geometry is conformall flat when and only when $R _ { a b c } = 0$

(c) Show that the following identities hold and reduce to five the number of independent components of $R _ { a b c }$ ：

$$
\begin{array} { c } { { R ^ { a } { } _ { a c } = g ^ { a b } R _ { b a c } = 0 ; } } \\ { { { } } } \\ { { R _ { a b c } + R _ { a c b } = 0 ; } } \\ { { { } } } \\ { { R _ { a b c } + R _ { c a b } + R _ { b c a } = 0 . } } \end{array}
$$

(d) Show that Yorks’ curvature

$$
\begin{array} { c } { { Y ^ { a b } = g ^ { 1 / 3 } [ a e f ] \left( R _ { t } ^ { \ b } - \frac 1 4 \delta _ { t } ^ { \ b } R \right) _ { | e } } } \\ { { { } } } \\ { { { } = - \frac 1 2 g ^ { 1 / 3 } [ a e f ] g ^ { b m } R _ { m e f } } } \end{array}
$$

is conformally invariant and has the properties listed in equations (21.148).

# Exercise 21.23. PULLING THE POYNTING FLUX VECTOR “OUT OF THE AIR"

From the condition that the Hamilton-Jacobi functional $S ( g _ { i j } , A _ { m } )$ (extremal of the action integral) for the combined Einstein and Maxwellfields,ostensibly dependent on the six metric coefficients $g _ { i j } ( x , y , z )$ and the three potentials $A _ { m } ( x , y , z )$ , shall actually depend only on the 3-geometry of the spacelike hypersurface and the distribution of magnetic field strength on this hypersurface,show that the geometrodynamic field momentum $\pi ^ { i j } = \delta S / \delta g _ { i j }$ satisfies a condition of the form

$$
\pi ^ { i j } { } _ { | j } = c [ i m n ] \mathcal { E } _ { m } \mathcal { B } _ { n } ,
$$

and evaluate the coefficient $\pmb { c }$ in this equation [Wheeler(l968b)). Hint: Note that the transformation

$$
x ^ { i } \longrightarrow x ^ { i } - \xi ^ { i } , g _ { i j } \longrightarrow g _ { i j } + \xi _ { i \mid j } + \xi _ { j \mid i }
$$

in no way changes the 3-geometry itself, and therefore the corresponding induced change in $s$ ，

$$
\delta S = \int \biggl [ \frac { \delta S } { \delta g _ { i j } } \delta g _ { i j } + \frac { \delta S } { \delta A _ { m } } \delta A _ { m } \biggr ] d ^ { 3 } x
$$

must vanish identically for arbitrary choice of the $\xi ^ { i } ( x , y , z )$ ，which measure the equivalent of the sliding of a ruled transparent rubber sheet over an automobile fender.

# Exercise 21.24. THE EXTREMAL ACTION ASSOCIATED WITH THE HILBERT ACTION PRINCIPLE DEPENDS ON CONFORMAL 3-GEOMETRY AND EXTRINSIC TIME [K. Kuchar (1972) and J. York (1972)]

Show that the data demanded by the Hilbert action principle $\delta \int ^ { ( 4 ) } R ( - { } ^ { ( 4 ) } g ) ^ { 1 / 2 } d ^ { 4 } x = 0$ on each of the two bounding spacelike hypersurfaces consist of (l) the conformal 3-geometry $^ { ( 3 ) } <$ of the hypersurface plus (2)the extrinsic time variable defined by

$$
\tau = \frac { 2 } { 3 } g ^ { - 1 / 2 } \operatorname { T r } \pmb { \pi } = \frac { 4 } { 3 } \operatorname { T r } \pmb { K } ,
$$

conveniently represented by the pictogram $\approx$ ，measured by one number per spacepoint, and independent of the conformai factor in the metric of the 3-geometry.This done, explain in a few words why in this formulation of geometrodynamics the Hamilton-Jacobi function $\hbar$ times the phase of the wave function in the semiclassical or JWKB approximation) is appropriately expressed in the form

$$
S = S ( ^ { ( 3 ) } < , \breve { \varkappa } ) .
$$

# \$21.13. JUNCTION CONDITIONS

The intrinsic and extrinsic curvatures of a hypersurface, which played such fundamental roles in the initial-value formalism,are also powerful tools in the analysis of “junction conditions.”

Recall the junction conditions of electrodynamics: across any surface (e.g.， a capacitor plate), the tangential part of the electric feld, $\pmb { { \cal E } } _ { | | } ,$ and the normal part of the magnetic field, $\pmb { B } _ { \perp }$ ，must be continuous; thus,

Junction conditions for electrodynamics

$$
\begin{array} { r l } & { [ E _ { | | } ] \equiv ( \mathrm { d i s c o n t i n u i t y ~ i n ~ } E _ { | | } ) } \\ & { ~ \equiv ( E _ { | | } \mathrm { ~ o n ~ } ^ { \omega _ { \mathrm { + } } } + ^ { , \prime } \mathrm { ~ s i d e ~ o f ~ s u r f a c e } ) - ( E _ { | | } \mathrm { ~ o n ~ } ^ { \omega _ { \mathrm { - } } } - ^ { , \prime } \mathrm { ~ s i d e ~ o f ~ } } \\ & { ~ \mathrm { s u r f a c e } ) } \\ & { ~ \equiv E _ { | | } ^ { + } - E _ { | | } ^ { - } = 0 , } \\ & { [ B _ { \perp } ] \equiv B _ { \perp } ^ { + } - B _ { \perp } ^ { - } = 0 ; } \end{array}
$$

while the“jump” in the parts $\pmb { E } _ { \bot }$ and $\pmb { { \cal B } } _ { | | }$ must be related to the charge density (charge per unit area) $\pmb { \sigma }$ ,the current density (current per unit area) $j ,$ and the unit normal to the surface $\pmb { n }$ by the formulas

$$
\begin{array} { c } { { [ E _ { \perp } ] = E _ { \perp } ^ { + } - E _ { \perp } ^ { - } = 4 \pi \sigma n , } } \\ { { { } } } \\ { { [ B _ { | | } ] = B _ { | | } ^ { + } - B _ { | | } ^ { - } = 4 \pi j \times n . } } \end{array}
$$

Recall also that one derives these junction conditions by integrating Maxwell's equations over a “pill box” that is centered on the surface.

Similar junction conditions,derivable in a similar manner,apply to the gravitational field (spacetime curvature),and to the stress-energy that generates it.\* Focus

![](images/c21f9e38ac294c33fc8cb79dab8c029b713af112c10ca04046de8f65b17cea33.jpg)  
Figure 21.6. Gaussian normal coordinates in the neighborhood of a 3-surface $\pmb { \Sigma }$ The metric in Gaussian normal coordinates has the form

$$
d s ^ { 2 } = ( { \pmb { n } } \cdot { \pmb { n } } ) ^ { - 1 } d n ^ { 2 } + g _ { i j } d x ^ { i } d x ^ { j }
$$

with ${ \pmb n } = \partial / \partial n$ ， $( { \pmb n } \cdot { \pmb n } ) = - 1$ if the surface is spacelike,and $( \pmb { n } \cdot \pmb { n } ) = 1$ if it is timelike.(See exercise 27.2.) The extrinsic curvature of the surfaces $\pmb { n } =$ constant is $K _ { i j } = - \textstyle { \frac { 1 } { 2 } } \hat { \sigma } g _ { i j } / \hat { \sigma } n$ ,and the Einstein field equations writen in $" 3 + 1 "$ form are (21.162).

Einstein equation in $3 + 1$ ： form

attention on a specific three-dimensional slice through spacetime-the 3-surface $\pmb { \Sigma }$ on Figure 21.6. Let the surface be either spacelike [unit normal $\pmb { n }$ timelike; $( \pmb { n } \cdot \pmb { n } ) = - 1 ]$ or timelike [n spacelike; $( \pmb { n } \cdot \pmb { n } ) = + 1 ]$ . The null case will be discussed later.As an aid in deriving junction conditions, introduce Gaussian normal coordinates in the neighborhood of $\pmb { \Sigma }$ [see the paragraph preceeding equation (21.82)]. In terms of the intrinsic and extrinsic curvatures of $\pmb { \Sigma }$ and of neighboring 3-surfaces $n =$ constant, the Einstein tensor and Einstein field equation have components

$$
\begin{array} { l } { { G ^ { n } { } _ { n } = \displaystyle - \frac { 1 } { 2 } { } ^ { ( 3 ) } R + \frac { 1 } { 2 } ( n \cdot n ) ^ { - 1 } \{ ( \mathrm { T r } K ) ^ { 2 } - \mathrm { T r } ( K ^ { 2 } ) \} = 8 \pi T ^ { n } { } _ { n } , } } \\ { { \displaystyle G ^ { n } { } _ { i } = - ( n \cdot n ) ^ { - 1 } \{ K _ { i } ^ { m } | _ { m } - ( \mathrm { T r } K ) _ { | i } \} = 8 \pi T ^ { n } { } _ { i } , } } \\ { { G ^ { i } { } _ { j } = { } ^ { ( 3 ) } G ^ { i } { } _ { j } + ( n \cdot n ) ^ { - 1 } \{ ( K ^ { i } { } _ { j } - \delta ^ { i } { } _ { j } \mathrm { T r } K ) _ { , n } } } \\ { { \displaystyle ~ - ( \mathrm { T r } K ) K _ { j } ^ { i } + \frac { 1 } { 2 } \delta ^ { i } { } _ { j } ( \mathrm { T r } K ) ^ { 2 } + \frac { 1 } { 2 } \delta ^ { i } { } _ { j } \mathrm { T r } ( K ^ { 2 } ) \} = 8 \pi T ^ { i } { } _ { j } . } } \end{array}
$$

Surface stress-energy tensor

[See equations (21.77), (21.81), (21.76),and (21.82).]

Suppose that the stress-energy tensor $T ^ { \alpha } { } _ { \beta }$ contains a “delta-function singularity” at $\pmb { \Sigma }$ i.e.,suppose that $\pmb { \Sigma }$ is the“world tube”of a two-dimensional surface with finite 4-momentum per unit area (analog of surface charge and surface current in electrodynamics). Then define the surface stress-energy tensor on $\pmb { \Sigma }$ to be the integral of $T ^ { \alpha } { } _ { \beta }$ with respect to proper distance $( n )$ ，measured perpendicularly through $\pmb { \Sigma }$ ：

$$
{ S ^ { \alpha } } _ { \beta } = \underset { \varepsilon  0 } { \mathrm { L i m } } \biggl [ \int _ { - \varepsilon } ^ { + \varepsilon } T _ { \beta } ^ { \alpha } d n \biggr ] .
$$

To discover the efect of this surface layer on the spacetime geometry, perform a "pil-box integration”of the Einstein field equation (21.162)

$$
\operatorname * { L i m } _ { \varepsilon \to 0 } \left[ \int _ { - \varepsilon } ^ { + \varepsilon } G ^ { \alpha } { } _ { \beta } d n \right] = 8 \pi S ^ { \alpha } { } _ { \beta } .
$$

Derivation of junction conditions

Examine the integral of $G ^ { \alpha } { } _ { \beta }$ If the 3-metric $g _ { i j }$ were to contain a delta function or a discontinuity at $\pmb { \Sigma }$ then $\pmb { \Sigma }$ would not have any well-defined 3-geometry-a physically inadmissble situation, even in the presence of surface layers. Absence of delta functions, $\delta ( { \pmb n } )$ ,in $g _ { i j }$ means absence of delta functions in $^ { ( 3 ) } R$ ； absence of discontinuities in $g _ { i j }$ means absence of delta functions in $K _ { i j } = - { \textstyle \frac { 1 } { 2 } } g _ { i j , n }$ Thus, equations (21.162) when integrated say

$$
\begin{array} { c } { { { \stackrel { . } { \int } } G _ { ~ n } ^ { n } d \stackrel { . } { n } = 0 = 8 \pi S _ { ~ n } ^ { n } , } } \\ { { { \stackrel { . } { \int } } G _ { ~ i } ^ { n } d n = 0 = 8 \pi S _ { ~ i } ^ { n } , } } \\ { { { \stackrel { . } { \int } } G _ { ~ j } ^ { i } \cdot d n = ( n \cdot n ) ( \gamma _ { ~ j } ^ { i } - \delta _ { ~ j } ^ { i } \mathrm { T r } \gamma ) = 8 \pi S _ { ~ j } ^ { i } , } } \end{array}
$$

where $\gamma _ { \ j } ^ { \ i }$ is the “jump” in the components of the extrinsic curvature

$$
\begin{array} { r l } & { \gamma \equiv [ K ] \equiv ( K \circ \mathfrak { n } \ ^ { \ast } n = + \varepsilon \ \mathrm { s i d e } ^ { \prime } \ \mathrm { o f } \ \mathcal { L } ) - ( K \circ \mathfrak { n } \ ^ { \ast } n = - \varepsilon \ \mathrm { s i d e } ^ { \prime } \ \mathrm { o f } \ \mathcal { L } ) } \\ & { \quad \equiv K ^ { + } - K ^ { - } . } \end{array}
$$

In the absence of a delta-function surface layer, the above junction conditions say,simply, that $\pmb { \gamma } \equiv [ \pmb { K } ] = 0$ . In words: if one examines how $\pmb { \Sigma }$ is embedded in the spacetime above its “upper"face,and how it is embedded in the spacetime below its “lower” face, one must discover identical embeddings--i.e., identical extrinsic curvatures K. Of course, the intrinsic curvature of $\pmb { \Sigma }$ must also be the same, whether viewed from above or below. More briefly:

$$
\mathrm { a b s e n c e ~ o f ~ s u r f a c e ~ l a y e r s ) } \overrightarrow { \longleftarrow } ( \mathrm { ^ * c o n t i n u i t y ^ { \prime \prime } ~ o f ~ } g _ { i j } \mathrm { ~ a n d ~ } K _ { i j } ) .
$$

Junction conditions in absence of surface layers

If a surface layer is present, then $\pmb { \Sigma }$ must be the world tube of a two-dimensional layer of mater, and the normal to $\pmb { \Sigma }$ must be spacelike, $( \pmb { n } \cdot \pmb { n } ) = + 1$ . The junction conditions (21.165a,b) then have the simple physical meaning

$$
\begin{array} { r } { \pmb { S } ( n , . . . ) = 0 \pm \operatorname* { m a x } _ { \mathbf { \lambda } } \left( \begin{array} { l } { \mathrm { t h e ~ m o m e n t u m ~ f l o w ~ i s ~ e n t i r e l y ~ i n ~ } E ; \mathrm { , } } \\ { \mathrm { i . e . , ~ n o ~ m o m e n t u m ~ a s s o c i a t e d ~ w i t h ~ t h e } } \\ { \mathrm { s u r f a c e ~ l a y e r ~ f l o w s ~ o u t ~ o f ~ } E ; \mathrm { i . e . , ~ } E } \\ { \mathrm { i s ~ t h e ~ w o r l d ~ t u b e ~ o f ~ t h e ~ s u r f a c e ~ l a y e r } } \end{array} \right) , } \end{array}
$$

which tells one nothing new. The junction condition (21.165c) says that the surface stress-energy generates a discontinuity in the extrinsic curvature (different embedding in spacetime “above” $\pmb { \Sigma }$ than “below” $\pmb { \Sigma }$ ), given by

$$
\gamma ^ { i } { } _ { j } - \delta ^ { i } { } _ { j } \operatorname { T r } \gamma = 8 \pi S ^ { i } { } _ { j } .
$$

Of course, the intrinsic geometry of $\pmb { \Sigma }$ must be the same as seen from above and below, $g _ { i j }$ continuous across $\pmb { \Sigma }$ (21.169)

Junction conditions for a surface layer

In analyzing surface layers, one uses not only the junction conditions (21.168a) to (21.169), but also the four-dimensional Einstein field equation applied on each side of the surface $\pmb { \Sigma }$ separately,and also an equation of motion for the surface stressenergy.The equation of motion is derived by examining the jump in the field equation $G _ { \ i } ^ { n } = 8 \pi T _ { \ i } ^ { n }$ (equation 21.162b)； thus $[ G ^ { n } { } _ { i } ] = 8 \pi [ T ^ { n } { } _ { i } ]$ says

$$
( { \gamma _ { i } } ^ { m } - { \delta _ { i } } ^ { m } \operatorname { T r } \gamma ) _ { | m } = - 8 \pi [ { T ^ { n } } _ { \mathrm { i } } ] ;
$$

and when reexpressed in terms of $S _ { i } ^ { { m } }$ by means of the junction condition (21.168b), it says

Equation of motion for a surface layer

$$
{ \cal S } ^ { i m } { } _ { | m } + [ T ^ { i n } ] = 0 .
$$

[For intuition into this equation of motion, see Exercises 21.25 and 21.26. For applications of the “surface-layer formalism”see exercise 21.27；also Israel (1966). Kuchar (1968), Papapetrou and Hamoui (1968).]

Gravitational-wave shock fronts

When one turns attention to junction conditions across a null surface $\pmb { \Sigma }$ ,one finds results rather different from those in the spacelike and timelike cases.A“pill-box” integration of the field equations reveals that even in vacuum the extrinsic curvature may be discontinuous.A discontinuity in $K _ { i j }$ across a null surface, without any stress-energy to produce it, is the geometric manifestation of a gravitational-wave shock front (analog of a shock-front in hydrodynamics). For quantitative details see, e.g.,Pirani (1957),Papapetrou and Treder (1959,1962), Treder (1962),and especially Choquet-Bruhat (1968b).

That a discontinuity in the curvature tensor can propagate with the speed of light is a reminder that all gravitational effects, like all electromagnetic effects, obey a causal law. The initial-value data on a spacelike initial-value hypersurface uniquely determine the resulting spacetime geometry [see the work of Cartan, Stellmacher, Lichnerowicz,and Bruhat (also under the names Foures-Bruhat and Choquet-Bruhat) and others cited and summarized in the article of Bruhat (l962)] but determine it in a way consistent with causality. Thus a change in these data throughout a limited region of the initial value 3-geometry makes itself felt on a slightly later hypersurface solely in a region that is also limited,and only a little larger than the original region.

When one turns from classical dynamics to quantum dynamics, one sees new reason to focus attention on a spacelike initial-value hypersurface: the observables at different points on such a hypersurface commute with one another; i.e., are in principle simultaneously observable.

Not every four-dimensional manifold admits a global singularity-free spacelike hypersurface. Those manifolds that do admit such a hypersurface have more to do with physics,it is possible to believe, than those that do not.

Even in a manifold that does admit a spacelike hypersurface, attention has been given sometimes, in the context of classical theory, to initial-value data on a hypersurface that is not spacelike but “characteristic,” in the sense that it accomodates null geodesics [see,for example,Sachs (l964) and references cited there].It is typical in such situations that one can predict the future but not the past, or predict the past but not the future.

Children of.light and children of darkness is the vision of physics that emerges from this chapter,as from other branches of physics.The children of light are the differential equations that predict the future from the present. The children of darkness are the factors that fix these initial conditions.

# Exercise 21.25. EQUATION OF MOTION FOR A SURFACE LAYER

# EXERCISES

(a) Let $\pmb { u }$ be the“mean 4-velocity”of the matter in a surface layer-so defined that an Observer moving with 4-velocity $\pmb { u }$ sees zero energy flux. Let $\pmb { \sigma }$ be the total mass-energy per unit proper surface area,as measured by such a“comoving observer.”Show that the surface stress-energy tensor can be expressed in the form

$$
\pmb { S } = \sigma \pmb { u } \otimes \pmb { u } + \pmb { t } , \mathrm { w h e r e } \ ( \pmb { t } \cdot \pmb { u } ) = 0 ,
$$

and where $\pmb { t }$ is a symmetric stress tensor.

(b) Show that the component along $\pmb { u }$ of the equation of motion (21.170) is

$$
d \sigma / d \tau = - \sigma u ^ { j } { } _ { | j } + u _ { j } t ^ { j k } { } _ { | k } + u _ { j } [ T ^ { j n } ] ,
$$

where $d / d \tau = \pmb { \mathscr { u } }$ Give a physical interpretation for each term.

(c)Let $a _ { j }$ be that part of the 4-acceleration of the comoving observer which lies in the surface layer $\pmb { \Sigma }$ .By projecting the equation of motion (21.170) perpendicular to ${ \pmb u }$ ，show that

$$
\sigma a _ { j } = - P _ { j a } \{ t ^ { a b } { } _ { | b } + [ T ^ { a n } ] \} ,
$$

where $P _ { j a }$ is the projection operator

$$
P _ { j a } = g _ { j a } + u _ { j } u _ { a } .
$$

Give a physical interpretation for each term of equation (21.182).

# Exercise 21.26. THIN SHELLS OF DUST

For a thin shell of dust surrounded by vacuum $( [ T ^ { j n } ] = 0$ ， $\pmb { t } = 0$ ，derive the following equations

$$
d \sigma / d \tau = - { \sigma } { u ^ { b } } _ { | b } ,
$$

$$
{ \pmb a } ^ { + } + { \pmb a } ^ { - } = 0 ,
$$

$$
a ^ { + } - a ^ { - } = ( 4 \pi \sigma ) n
$$

$$
\pmb { \gamma } = 8 \pi \sigma \bigg ( \pmb { u } \otimes \pmb { u } + \frac { 1 } { 2 } \pmb { g } \bigg ) .
$$

Here $\pmb { \hat { e } } ^ { + }$ and $\pmb { a } ^ { - }$ are the 4-accelerations as measured by accelerometers that are fastened onto the outer and inner sides of the shell,and $\pmb { \mathscr { g } }$ is the $^ 3$ -metric of the shell. Show that the first of these equations is the law of “conservation of rest mass.”

# Exercise 21.27. SPHERICAL SHELL OF DUST

Apply the formalism of exercise 21.25 to a collapsing spherical shell of dust [Israel (1967b)]. For the metric inside and outside the shell.take the flat-spacetime and vacuum Schwarzschild expressions (Chapter 23),

$$
d s ^ { 2 } = { } - \left( 1 - { \frac { 2 M } { r } } \right) d t ^ { 2 } + { \frac { d r ^ { 2 } } { 1 - 2 M / r } } + r ^ { 2 } ( d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } ) \ \mathrm { o u t s i d e } .
$$

Let the“radius” of the shell,as a function of proper time measured on the shell, be

$$
R \equiv { \frac { 1 } { 2 \pi } } \times ( { \mathrm { p r o p e r ~ c i r c u m f e r e n c e ~ o f ~ s h e l l } } ) = R ( \tau ) .
$$

Show that the shell's mass density varies with time as

$$
\sigma ( \tau ) = \mu / 4 \pi R ^ { 2 } ( \tau ) , ~ \mu = \mathrm { c o n s t a n t } = { } ^ { \cdot \circ } \mathrm { t o t a l ~ r e s t ~ m a s s ^ { \circ } ; }
$$

and derive and solve the equation of motion

$$
M = \mu \left\{ 1 + \left( { \frac { d R } { d \tau } } \right) ^ { 2 } \right\} ^ { 1 / 2 } - { \frac { \mu } { 2 R } } .
$$
