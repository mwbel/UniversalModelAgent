# CHAPTER 12

# NEWTONIAN GRAVITY IN THE LANGUAGE OF CURVED SPACETIME

The longest period of time for which a modern painting has hung upside down in a public gallery unnoticed is 47 days.This   
occurred to Le Bateau by Matisse in the Museum of Modern Art, New York City. In this time 116.000 people had passed through the gallery.

McWHIRTER AND MCWHIRTER (1971)

# $\$ 12.1$ .NEWTONIAN GRAVITY IN BRIEF

The equivalence principle is not unique to Einstein's description of the facts of gravity. What is unique to Einstein is the combination of the equivalence principle and local Lorentz geometry. To return to the world of Newton, forget everything discovered in the last century about special relativity,light cones,the limiting speed of light, and proper time. Return to the“universal time” $t$ of earlier centuries. In terms of that universal time,and of rectangular,“Galilean” space coordinates, Newtonian theory gives for the trajectories of neutral test particles

This chapter is entirely Track 2. Chapters 9-11 are necessary preparation for it.

It is not needed for any later chapter,but it will be helpful in (1）Chapter 17 (Einstein field equations) and (2) Chapters 38 and 39 (experimental tests and other theories of gravity).

$$
\begin{array} { r } { \frac { d ^ { 2 } x ^ { j } } { d t ^ { 2 } } + \frac { \partial \phi } { \partial x ^ { j } } = 0 ; } \end{array}
$$

Newtonian gravity:original formulation

Customarily one interprets these equations as describing the“curved paths" $x ^ { j } ( t )$ along which test particles fall in Euclidean space (not spacetime). These curved paths include circular orbits about the Earth and the parabolic trajectory of a baseball. Cartan (l923,1924) asks one to abandon this viewpoint. Instead, he says, regard these trajectories as geodesics $[ t ( \lambda ) , x ^ { j } ( \lambda ) ]$ in curved spacetime.(This change of viewpoint was embodied in Figures B and C of Box 1.6.) Since the “affinely ticking"

Newtonian gravity: translation into language of curved spacetime

Newtonian clocks carried by test particles read universal time (or some multiple, $\lambda = a t + b$ , thereof), the equation of motion (l2.1) can be rewritten

$$
\frac { d ^ { 2 } t } { d \lambda ^ { 2 } } = 0 , \qquad \frac { d ^ { 2 } x ^ { j } } { d \lambda ^ { 2 } } + \frac { \partial \phi } { \partial x ^ { j } } \left( \frac { d t } { d \lambda } \right) ^ { 2 } = 0 .
$$

By comparing with the geodesic equation

$$
d ^ { 2 } x ^ { \alpha } / d \lambda ^ { 2 } + { \cal { T } } ^ { \alpha } { } _ { \beta \gamma } ( d x ^ { \beta } / d \lambda ) ( d x ^ { \gamma } / d \lambda ) = 0 ,
$$

one can read off the values of the connection coefficients:

$$
{ \cal T } _ { 0 0 } ^ { j } = \partial \phi / \partial x ^ { j } ; \qquad \mathrm { a l l ~ o t h e r } \ { \cal T } _ { \phantom { \alpha } \beta \gamma } ^ { \alpha } \ \mathrm { v a n i s h } .
$$

And by inserting these into the standard equation (l1.l2) for the components of the Riemann tensor, one learns (exercise l2.1)

$$
{ R ^ { j } } _ { 0 k 0 } = - { R ^ { j } } _ { 0 0 k } = { \frac { \hat { \sigma } ^ { 2 } \phi } { \hat { \sigma } x ^ { j } \hat { \sigma } x ^ { k } } } ; ~ \mathrm { a l l ~ o t h e r } ~ { R ^ { \alpha } } _ { \beta \gamma \delta } \mathrm { v a n i s h } .
$$

Finally, the source equation for the Newtonian potential

$$
\nabla ^ { 2 } \phi \equiv \sum _ { j } \phi _ { , j j } = 4 \pi \rho
$$

one can rewrite with the help of the “Ricci curvature tensor”

$$
R _ { \alpha \beta } \equiv R _ { \alpha \mu \beta } ^ { \mu } \ ( \mathrm { c o n t r a c t i o n \ o f } \ R i e m a n n )
$$

in the geometric form (exercise 12.2)

$$
R _ { 0 0 } = 4 \pi \rho ; \qquad \mathrm { a l l ~ o t h e r } ~ R _ { \alpha \beta } ~ \mathrm { v a n i s h } .
$$

Equation (12.4) for $\Gamma ^ { \alpha } { } _ { \beta \gamma } ,$ equation (12.5) for $R ^ { \alpha } { } _ { \beta \gamma \delta }$ , equation (12.8) for $R _ { \alpha \beta }$ ,plus the law of geodesic motion are the full content of Newtonian gravity,rewritten in geometric language.

It is one thing to pass quickly through these component manipulations. It is quite another to understand fully,in abstract and pictorial terms,the meanings of these equations and the structure of Newtonian spacetime. To produce such understanding, and to compare Newtonian spacetime with Einsteinian spacetime, are the goals of this chapter,which is based on the work of Cartan (l923,1924), Trautman (1965), and Misner (1969a).

# EXERCISES

# Exercise 12.1. RIEMANN CURVATURE OF NEWTONIAN SPACETIME

Derive equation (12.5） for $R ^ { \alpha } { } _ { \beta \gamma \delta }$ from equation (12.4) for $\varGamma ^ { \alpha } { } _ { \beta \gamma } .$

Exercise 12.2. NEWTONIAN FIELD EQUATION Derive the geometric form (12.8) of the Newtonian field equation from (12.5) through (12.7).

# $\$ 12.2$ . STRATIFICATION OF NEWTONIAN SPACETIME

Galileo and Newton spoke of a flat, Euclidean“absolute space”and of an “absolute time,”two concepts distinct and unlinked.In absolute space Newtonian physics took place; and as it took place,absolute time marched on. No hint was there that space and time might be two aspects ofa single entity,a curved “spacetime”-until Einstein made the unification in relativity physics,and Cartan (l923) followed suit in Newtonian physics in order to provide clearer insight into Einstein's ideas.

How do the absolute space of Galileo and Newton,and their absolute time, fit into Cartan's “Newtonian spacetime"? The key to the fit is stratification; stratification produced by the universal time coordinate t.

The geometry of Newtonian spacetime:

Regard t as a function (scalar field) defined once and for all in Newtonian spacetime

"Universal time" as a scalar field

$$
t = t ( { \mathcal { P } } ) .
$$

Without it, spacetime could not be Newtonian, for $" t "$ is every bit as intrinsic to Newtonian spacetime as the metric $" g \prime$ is to Lorentz spacetime. The layers of spacetime are the slices of constant t-the “space slices"-each of which has an identical geometric structure: the old “absolute space.”

Adopting Cartan's viewpoint, ask what kind of geometry is induced onto each space slice by the surrounding geometry of spacetime. A given space slice is endowed, by the Galilean coordinates of $\ S 1 2 . 1$ , with basis vectors $\pmb { e } _ { j } = \partial / \partial x ^ { j }$ ；and this basis has vanishing connection coefficients, $T ^ { j } { } _ { \kappa \ell } = 0$ [cf. equation (12.4)]. Consequently, the geometry of each space slice is completely flat.

“Absolute space” is Euclidean in its geometry, according to the old viewpoint, and the Galilean coordinates are Cartesian. Translated into Cartan's language, this says: not only is each space slice ( $( t =$ constant) flat,and not only do its Galilean coordinates have vanishing connection coefficients, but also each space slice is endowed with a three-dimensional metric,andits Galilean coordinate basis is orthonormal,

Space slices with Euclidean geometry

$$
\begin{array} { r } { \pmb { e } _ { i } \cdot \pmb { e } _ { j } = ( \hat { \partial } / \hat { \partial } \pmb { x } ^ { i } ) \cdot ( \hat { \partial } / \hat { \partial } \pmb { x } ^ { j } ) = \delta _ { i j } . } \end{array}
$$

If the space slices are really so flat, where do curvature and geodesic deviation enter in? They are properties of spacetime. Parallel transport a vector around a closed curve lying entirely in a space slice; it will return to its starting point unchanged.. But transport it forward in time by $\pmb { \varDelta t }$ , northerly in space by $\pmb { \varDelta x ^ { k } }$ , back in time by $- \Delta t$ ,and southerly by $- \varDelta x ^ { k }$ to its starting point; it will return changed by

Curvature acts in spacetime, not in space slices

$$
\begin{array} { r } { \delta \pmb { A } = - \mathcal { R } \bigg ( \Delta t \frac { \partial } { \partial t } , \pmb { A x } ^ { k } \frac { \partial } { \partial { \pmb x } ^ { k } } \bigg ) \pmb { A } ; } \end{array}
$$

i.e.,

$$
\begin{array} { r } { \delta A ^ { 0 } = 0 , \delta A ^ { j } = \leavevmode { - R ^ { j } \mathstrut _ { 0 0 k } A ^ { 0 } ( \varDelta t ) ( \varDelta x ^ { k } ) } = \frac { \vec { c } ^ { 2 } \phi } { \partial x ^ { j } \partial x ^ { k } } A ^ { 0 } ( \varDelta t ) ( \varDelta x ^ { k } ) . } \end{array}
$$

Geodesics of a space slice (Euclid's straight lines) that are initially parallel remain

always parallel. But geodesics of spacetime (trajectories of freely falling particles) initially parallel get pried apart or pushed together by spacetime curvature,

$$
\pmb { \nabla } _ { \pmb { u } } \pmb { \nabla } _ { \pmb { u } } \pmb { n } + \mathcal { R } ( \pmb { n } , \pmb { u } ) \pmb { u } = 0 ,
$$

or equivalently in Galilean coordinates:

$$
\frac { d ^ { 2 } n ^ { j } } { d t ^ { 2 } } + \frac { \partial ^ { 2 } \phi } { \partial x ^ { j } \partial x ^ { k } } n ^ { k } = 0
$$

(see Box l2.1 and exercise 12.3).

# EXERCISE

# Exercise 12.3. GEODESIC DEVIATION DERIVED

Produce a third column for Box l1.4, one that carries out the “geometric analysis” in component notation using the Galilean connection coefficients (l2.4) of Newtonian spacetime. Thereby achieve a deeper understanding of how the geometric analysis parallels the old Newtonian analysis.

# $\$ 123$ . GALILEAN COORDINATE SYSTEMS

The Lorentz spacetime of special relativity has an existence and structure completely independent of any coordinate system. But a special property of its geometry (zero curvature) allows the introduction of a special class of coordinates (Lorentz coordinates), which cling to spacetime in a special way

By studying these special coordinate systems and the relationships between them (Lorentz transformations), one learns much about the structure of spacetime itself (breakdown in simultaneity; Lorentz contraction； time dilatation; ...).

Galilean coordinates defined

Similarly for Newtonian spacetime. Special properties of its geometry (explored in abstract later; Box 12.4) permit the introduction of special coordinates (Galilean coordiates), which cling to spacetime in a special way

$$
x ^ { 0 } ( { \mathcal { P } } ) = t ( { \mathcal { P } } ) ;
$$

$$
( \partial / \partial x ^ { j } ) \cdot ( \partial / \partial x ^ { k } ) = \delta _ { j k } ;
$$

$T ^ { j } { } _ { 0 0 } = \Phi _ { , j }$ for some scalar field $\pmb { \bar { p } }$ , and all other $\Gamma ^ { \alpha } { } _ { \beta \gamma }$ vanish.

To understand Newtonian spacetime more deeply, study the relations between these Galilean coordinate systems.

Coordinate system for calculation: Galilean space coordinates $x ^ { j }$ and universal time coordinate $t ,$ General component form of equation:

$$
{ \frac { D ^ { 2 } n ^ { \alpha } } { d \lambda ^ { 2 } } } + R ^ { \alpha } { } _ { \beta \gamma \delta } { \frac { d x ^ { \beta } } { d \lambda } } n ^ { \gamma } { \frac { d x ^ { \delta } } { d \lambda } } = 0 .
$$

Special conditions for this calculation: let the particles'clocks (afine parameters) all be normalized to read universal time, $\lambda = t$ 、This means that the separation vector

$$
n ^ { \alpha } = (  { \partial } x ^ { \alpha } /  { \partial } n ) _ { \lambda }
$$

between geodesics has zero time component, $n ^ { 0 } = 0$ ; i.e., in abstract language,

$$
\langle d t , n \rangle = t _ { , \alpha } n ^ { \alpha } = n ^ { 0 } = 0 ;
$$

i.e., in geometric language, $\pmb { n }$ lies in a space slice (surface of constant $t$ ）.

Evaluation of covariant derivative:

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/5be2b9c2f4e5455c6fd9d26ae474abeedcd91ad47e50d31953c0eecd05f08281.jpg)

$\begin{array} { r } { \frac { D n ^ { \alpha } } { D \lambda } = \frac { d n ^ { \alpha } } { d \lambda } + \underbrace { { \Gamma ^ { \alpha } } _ { \beta \mu } } _ { \lambda } n ^ { \beta } \frac { d x ^ { \mu } } { d \lambda } = \frac { d n ^ { \alpha } } { d \lambda } , } \\  { [ 0 \mathrm { ~ u n l e s s ~ } \beta = 0 ] } ^ { \qquad } \enspace \enspace \middle [ \enspace . \vphantom { \int ^ { \alpha } } \end{array}$ a space index $( n ^ { 0 } = 0 )$ ] ${ \begin{array} { l } { { \frac { D ^ { 2 } n ^ { \alpha } } { d \lambda ^ { 2 } } } = { \frac { d ( D n ^ { \alpha } / d \lambda ) } { d \lambda } } + \underbrace { { \Gamma ^ { \alpha } } _ { \beta \mu } } _ { \mathrm { \normalfont ~ d } } { \frac { d n ^ { \beta } } { d \lambda } } { \frac { d x ^ { \mu } } { d \lambda } } = { \frac { d ( D n ^ { \alpha } / d \lambda ) } { d \lambda } } = { \frac { d ^ { 2 } n ^ { \alpha } } { d \lambda ^ { 2 } } } = { \frac { d ^ { 2 } n ^ { \alpha } } { \mathrm { \normalfont ~ d } } } . } \\ { \left[ 0 { \mathrm { ~ u n l e s s ~ } } \beta = 0 \right] { \cfrac { d n ^ { \beta } } { \mathrm { \normalfont ~ / } 0 { \mathrm { ~ u n l e s s ~ } } \beta { \mathrm { ~ i s ~ s p a c e ~ i n d e x } } | } } } \end{array} }$

Evaluation of tidal accelerations:

RBy8 nydx8 =0 since $R _ { 0 k 0 } ^ { j }$ and $R _ { ~ 0 0 k } ^ { j }$ are only nonzero components. d

$$
\begin{array} { l } { { \underbrace { R ^ { j } { } _ { \beta \gamma \delta } } _ { \mathrm { \normalfont ~ \displaystyle \{ ~ \int ~ } } d \lambda \begin{array} { l } { { d x ^ { \beta } } } \\ { { d \lambda } } \end{array}  \{ \begin{array} { l l } { { d x ^ { \delta } } } \\ { { d \lambda } } \end{array} = R ^ { j } { } _ { 0 k 0 } \frac { d t } { d \lambda } n ^ { k } \frac { d t } { d \lambda } = R ^ { j } { } _ { 0 k 0 } n ^ { k } = \frac { { \hat { c } } ^ { 2 } \phi } { \hat { c } x ^ { j } \partial x ^ { k } } n ^ { k } . } } \\ { { \mathrm { \normalfont ~ \{ ~ \begin{array} { l l } { { ~ 0 \ u n l e s s ~ } \gamma ~ i s ~ s p a c e ~ i n d e x \} ~ } } \\ { { \mathrm { \normalfont ~ \{ ~ f o r ~ } \gamma ~ a ~ s p a c e ~ i n d e x ; ~ 0 ~ u n l e s s ~ } \beta = \delta = 0 \} } } \end{array} } \end{array}
$$

Resultant equation of geodesic deviation:

$$
\frac { d ^ { 2 } n ^ { 0 } } { d t ^ { 2 } } = 0
$$

Point of principle: how can one write down the laws of gravity and properties of spacetime in Galilean coordinates first $( \ S 1 2 . 1 )$ ,and only afterward (here) come to grip with the nature of the coordinate system and its nonuniqueness? Answer: (a quotation from $\ S 3 . 1$ ， slightly modified):“Here and elsewhere in science,as emphasized not least by Henri Poincaré,that view is out of date which used to say \*Define your terms before you proceed.' All the laws and theories of physics, including Newton's laws of gravity, have this deep and subtle character, that they both define the concepts they use (here Galilean coordinates) and make statements about these concepts."

The Newtonian laws of gravity, writen in a Galilean coordinate system

$$
x ^ { 0 } = t , \qquad ( \partial / \partial x ^ { j } ) \cdot ( \partial / \partial x ^ { k } ) = \delta _ { j k }
$$

make the statement ${ } ^ { \mathrm { * } } T ^ { j } { } _ { 0 0 } = \Phi _ { , j }$ and all other $T ^ { \alpha } { } _ { \beta \gamma } = 0 ^ { , \gamma }$ about the geometry of spacetime. This statement in turn gives information about the relationships between different Galilean systems. Let one Galilean system $\{ x ^ { \alpha } ( { \mathcal { P } } ) \}$ be given,and seek the most general coordinate transformation leading to another, $\{ x ^ { \alpha ^ { \prime } } ( { \mathcal { P } } ) \}$ . The following constraints exist:(l) $x ^ { 0 ^ { \prime } } = x ^ { 0 } = t$ (both time coordinates must be universal.time); (2) at fixed $t$ (i.e.,in a fixed space slice) both sets of space coordinates must be Euclidean, so they must be related by a rotation and a translation:

$$
\begin{array} { l } { { x ^ { j ^ { \prime } } = A _ { j ^ { \prime } k } x ^ { k } + a ^ { j ^ { \prime } } } } \\ { { \mathrm { ~ } } } \\ { { \mathrm { ~ } } } \\ { { \scriptstyle \qquad \bigcup _ { \{ \mathrm { { r o t a t i o n ~ m a t r i x , ~ i . e . , ~ } } A _ { j ^ { \prime } L } A _ { k ^ { \prime } l } = \delta _ { j ^ { \prime } k ^ { \prime } } \} } } } \\ { { \scriptstyle x ^ { k } = A _ { j ^ { \prime } k } x ^ { j ^ { \prime } } - a ^ { k } , \mathrm { ~ w i t h ~ } a ^ { k } \equiv A _ { j ^ { \prime } k } a ^ { j ^ { \prime } } . } } \end{array}
$$

The rotation and translation might, a priori, be different on different slices, $A _ { j ^ { \prime } k } =$ $A _ { j ^ { \prime } k } ( t )$ and $a ^ { j } = a ^ { j } ( t )$ ； but (3) they must be constrained by the required special form of the connection coefficients. Calculate the connection coefficients in the new coordinate system, given their form in the old. The result (exercise l2.4) is:

$$
\begin{array} { l } { { { \cal T } ^ { j ^ { \prime } } { } _ { 0 ^ { \prime } k ^ { \prime } } = { \cal T } ^ { j ^ { \prime } } { } _ { k ^ { \prime } 0 ^ { \prime } } = A _ { j ^ { \prime } \mathrm { t } } \dot { A } _ { k ^ { \prime } \mathrm { t } } \qquad \mathrm { ( p r o d u c e s ~ ^ { * * } C o r i o l i s ~ f o r c e s ^ { * } ) } ; } } \\ { { \cal T } ^ { j ^ { \prime } } { } _ { 0 ^ { \prime } 0 ^ { \prime } } = \displaystyle \frac { \partial \phi } { \partial x ^ { j } } + A _ { j ^ { \prime } k } ( \ddot { A } _ { \mathit { t } ^ { \prime } k } x ^ { \mathit { t } ^ { \prime } } - \ddot { a } ^ { k } ) ; } \\ { { \cal T } ^ { * * } \mathrm { c e n t r i f u g a l ~ f o r c e s ^ { \prime } ) } . } \end{array}
$$

("Euclidean” index conventions; repeated space indices to be summed even if both are down; dot denotes time derivative). These have the standard Galilean form (l2.4) if and only if

$$
\begin{array} { c } { { \dot { A } _ { j ^ { \prime } k } = 0 , \phi ^ { \prime } = \phi - \ddot { a } ^ { k } x ^ { k } + \mathrm { c o n s t a n t . } } } \\ { { \left[ \begin{array} { l } { { \mathrm { N e w t o n i a n ~ p o t e n t i a l ~ i n } } } \\ { { \mathrm { n e w ~ c o o r d i n a t e ~ s y s t e m } } } \end{array} \right] ^ { \mathrm { ~ \dagger ~ } } \begin{array} { l } { { \dot { \mathrm { ~ L } } \mathord { \left[ \mathrm { N e w t o n i a n ~ p o t e n t i a l ~ i n } \right]}  } } \\ { { \mathrm { ~ \left[ \mathrm { o l d ~ c o o r d i n a t e ~ s y s t e m } ~ \right] ~ } } } \end{array} } } \end{array}
$$

These results can be restated in words: any two Galilean coordinate systems are related by(l) a time-independent rotation of the space grid (same rotation on each space slice), and (2) a time-dependent translation of the space grid (translation possibly different on different slices)

$$
\begin{array} { c } { { x ^ { j ^ { \prime } } = A _ { j ^ { \prime } k } x ^ { k } + a ^ { j ^ { \prime } } ( t ) . } } \\ { { \mathrm { [ c o n s t a n t ] } } } \end{array}
$$

Transformations linking Galilean coordinate systems

The Newtonian potential is not a function defined in spacetime with existence independent of allcoordinate systems. (There is no coordinate-free way to measure it.) Rather,it depends for its existence on a particular choice of Galilean coordinates; and if the choice is changed via equation (l2.16), then $\pmb { \phi }$ is changed:

$$
\phi ^ { \prime } = \phi - \ddot { a } ^ { k } x ^ { k } .
$$

(By contrast, an existence independent of all coordinates is granted to the universal time $t ( { \mathcal { P } } )$ and the covariant derivative ${ \pmb v } .$ ）

Newtonian potential depends on choice of Galilean coordinate system

Were all the matter in the universe concentrated'in a finite region of space and surrounded by emptiness (island universe")， then one could impose the global boundary condition

Absolute Galilean coordinates defined

$$
\phi \longrightarrow 0 \mathrm { \ a s \ } r \equiv ( x ^ { k } x ^ { k } ) ^ { 1 / 2 } \longrightarrow \infty .
$$

This would single out a subclass of Galilean coordinates ("absolute" Galilean coordinates), with a unique, common Newtonian potential. The transformation from one absolute Galilean coordinate system to any other would be

Transformations linking absolute Galilean coordinate systems

x=Ajκxk +a³+u"t   
[constant] [constant]   
rotation velocity] constant displacement

("Galilean transformation"). But. (l） by no local measurements could one ever distinguish these absolute Galilean coordinate systems from the broader class of Galilean systems (to distinguish, one must integrate the locally measurable quantity $\boldsymbol { \phi } _ { , j } = \boldsymbol { \Gamma ^ { j } } _ { 0 0 }$ out to infinity);and (2) astronomical data deny that the real universe is an island of matter surrounded by emptiness.

It is instructive to compare Galilean coordinates and Newtonian spacetime as described above with Lorentz coordinates and the Minkowskii spacetime of special relativity,and with the general coordinates and Einstein spacetime of general relativity;see Boxes l2.2 and 12.3.

(continued on page 298)

Box 12.2 NEWTONIAN SPACETIME，MINKOWSKIIAN SPACETIME，AND EINSTEINIAN SPACETIME: COMPARISON AND CONTRAST   

<table><tr><td>Query</td><td>Newtonian spacetime</td><td>Minkowskiian spacetime (special relativity)</td><td>Einsteinian spacetime (general relativity)</td></tr><tr><td>What a priori geometric structures does spacetime possess?</td><td>(l）Universal time function / (2) Covariant derivative (3) Spatial metric “&quot;; but spacetime metric can not be defined (exercise 12.10)</td><td>A spacetime metric that is fat (vanishing Riemann curvature)</td><td>A spacetime metric</td></tr><tr><td>What preferred coordinate systems are present?</td><td>(I）Galilean coordinates in general (2)Absolule Galilean coordinates in an island universe (this case nol considered here)</td><td>Lorentz coordinates</td><td>In general, every coordinate system is equally preferred (though in special cases with symmetry there are special preferred coordinates)</td></tr><tr><td>What is required to select out a particular preferred coordinate system?</td><td>(l）A single spatial orientation, the same throughout all spacetime (three Euler angles) (2)The arbitrary world line of the origin of space coordinates (three functions of time)</td><td>(I）A single spatial orientation, the same throughout all spacetime (three Euler angles) (2） The location of the origin of coordinates (four numbers) (3）The velocity of the origin of</td><td>All four functions of position x&quot;(s)</td></tr><tr><td>Under what conditions is“g and 2 are simultaneous”well-defined?</td><td>In general; it is a coordinate-free geometric concept</td><td>space coordinates (three numbers) Only after a choice of Lorentz frame has been made;“simultaneity”depends on the frame&#x27;s velocity</td><td>Only after arbitrary choice of time coordinate has been made</td></tr><tr><td>Under what conditions is“9 and 2 occur at same point in spaee”well- defined?</td><td>Only after choice of Galilean coordinates has been made</td><td>Only after choice of Lorentz coordinates has been made</td><td>Only after arbitrary choice of space Coordinates has been made</td></tr><tr><td>Under what conditions is“u and v, at different events,point in same direction&quot;well-defined?</td><td>Only if u and v are both spatial veciors((dt,u&gt;=(dt,v&gt;=0）；or if they lie in the same space slice and are arbitrary vectors; or if there exists a preferred route connecting their locations,along which to compare them by parallel.</td><td>Always</td><td>Only if u andv lie at events infinitesimally close together:or if there exists a preferred route (e.g.,a unique geodesic) connecting their locations,along which to compare them by parallel transport</td></tr><tr><td>Under what conditions is “the invariant distance between  and 2&quot; well-defined?</td><td>transport Only if gand  lie in the same space slice</td><td>Always</td><td>Only if and &amp;are sufliciently close together;or if there exists a unique preferred world line (e.g., a geodesic） linking them,along</td></tr></table>

Box 12.3 NEWTONIAN GRAVITY A_LA CARTAN,AND EINSTEINIAN GRAVITY: COMPARISON AND CONTRAST   

<table><tr><td>Property</td><td>Newton-Cartan</td><td>Einstein</td></tr><tr><td>Idea in brief (formulations of the equivalence principle of very different scope)</td><td>Laws of motion of free parti- cles in a local, freely falling,nonrotating frame are identical to Newton&#x27;s laws of motion as expressed in a gravity-free Galilean frame</td><td>Laws of physics in a local, freely falling,nonrotating frame are identical with the laws of physics as formulated in special relativity ina Lorentz frame</td></tr><tr><td>Idea even more briefly stated</td><td>Point mechanics simple in a local inertial frame</td><td>Everything simple ina local inertial frame</td></tr><tr><td>Consequence (tested to one part in 1011 by Roll-Krotkov- Dicke experiment)</td><td>Test particles of diverse composition started with same initial position and same initial velocity follow the sameworld line(&quot;definition of geodesic&quot;)</td><td>Test particles of diverse composition started with same initial position and same initial velocity follow the same world line(&quot;definition of geodesic&quot;)</td></tr><tr><td>Another consequence</td><td>In every local region,there existsa local frame(&quot;freely falling frame&quot;) in which all geodesics appear straight (all r =0）</td><td>In every local region there existsa local frame(freely falling frame&quot;) in which all geodesics appear straight (all ra =0）</td></tr><tr><td>Consequence of way light rays travel in real physical world?</td><td>Disregarded or evaded.All light rays have same velocity? Speed depend on motion of source? Speed depend on motion of observer? Possible to move fast enough to catch up with a light ray?No satisfactory position on any of these</td><td>Spacetime always and every- where has local Lorentz character</td></tr><tr><td>Summary of spacetime structure</td><td>Stratified into spacelike slices;geometry in each slice Euclidean;each slice charac- terized by value of universal time(geodesic parameter); displacement of one slice with respect to another not spec- ified;no such thing as a</td><td>No stratification.Well- defined interval between every event and every nearby event; spacetime has everywhere local Lorentz character,with one local frame (specific space and time axes) as good as another (other space and time axes);“homogeneous”rather</td></tr><tr><td>This structure expressed in mathematical language</td><td>rαu&#x27;s. yes: spacetime metric Surno: 冲 r&#x27;00= (i = 1,2.3); 2x</td><td>existence;all derived from （gB rauv = gaB 1 2 axu</td></tr></table>

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/fa987383bc8e4548c43742fcaa2166350e1ea9e828f2d8140066566b0532a3a0.jpg)  
Figure 12.1. The coordinate system carried by an orbital laboratory as it moves in a circular orbit about the Earth,

# Exercise 12.4. CONNECTION COEFFICIENTS FOR ROTATING, ACCELERATING COORDINATES

Beginning with equation (12.4) for the connection coeffcients of a Galilean coordinate system $\{ x ^ { \alpha } ( { \mathcal { P } } ) \}$ ，derive the connection coeffcients （12.14） of the coordinate system $\left\{ x ^ { \alpha ^ { \prime } } ( { \mathcal { P } } ) \right\}$ of equations (l2.l3). From this, verify that (l2.15) are necessary and suffcient for $\left\{ x ^ { \alpha ^ { \prime } } ( { \mathcal { P } } ) \right\}$ to be Galilean.

# Exercise 12.5. EINSTEIN'S ELEVATOR

Use the formalism of this chapter to discuss “Einstein's elevator"-i.e., the equivalence of “gravity” to an acceleration of one's reference frame.Which aspects of"gravity”are equivalent to an acceleration, and which are not?

# Exercise 12.6. GEODESIC DEVIATION ABOVE THE EARTH

A manned orbital laboratory is put into a circular orbit about the Earth [radius of orbit $\mathit { \Theta } = { \mathfrak { r } } _ { 0 } .$ angular velocity $\backsimeq \omega = ( M / { r _ { 0 } } ^ { 3 } ) ^ { 1 / 2 }$ -why?]. An astronaut jetisons a bag of garbage and watches it move along its geodesic path. He observes its motion relative to (non-Galilean) space coordinates $\{ x ^ { j ^ { \prime } } ( \mathcal { P } ) \}$ which-see Figure l2.1-(l) are Euclidean at each moment of universal time $[ ( \partial / \partial x ^ { j ^ { \prime } } ) \cdot ( \partial / \partial x ^ { k ^ { \prime } } ) = \delta _ { j k } ] ,$ (2) have origin at the laboratory's center,(3) have $\partial / \partial x ^ { \prime }$ pointing away from the Earth,(4） have $\hat { \boldsymbol { d } } / \hat { \boldsymbol { d } } \boldsymbol { x } ^ { \prime }$ and $\partial / \partial y ^ { \prime }$ in the plane of orbit. Use the equation of geodesic deviation to calculate the motion of the garbage bag in this coordinate system. Verify the answer by examining the Keplerian orbits of laboratory and garbage. Hints: (1) Calculate $R ^ { \alpha ^ { \prime } } { } _ { \beta ^ { \prime } \gamma ^ { \prime } \delta ^ { \prime } }$ in this coordinate system by atrivialtransformation of tensorial components. (2) Use equation (12.14) to calculate $\boldsymbol { T ^ { \alpha ^ { \prime } } } _ { \beta ^ { \prime } \gamma ^ { \prime } }$ at the center of the laboratory (i.e, on the fiducial geodesic).

# $\$ 123$ .GEOMETRIC, COORDINATE-FREE FORMULATION OF NEWTONIAN GRAVITY

To restate Newton's theory of gravity in coordinate-independent, geometric language is the principal goal of this chapter. It has been achieved,thus far,with extensive assistance from a special class of coordinate systems, the Galilean coordinates.To climb out of Galilean coordinates and into completely coordinate-free language is straightforward in principle. One merely passes from index notation to abstract notation.

ExmpleRe ${ \varGamma ^ { 0 } } _ { \alpha \beta } = 0$ of Galilean coordinates.

Solution: Write ${ \Gamma ^ { 0 } } _ { \alpha \beta } = - \langle \nabla _ { \beta } d t , \pmb { e } _ { \alpha } \rangle$ the vanishingof this forall $\pmb { \alpha }$ means $\pmb { \nabla } _ { \beta } \pmb { d t } = 0$ for all $\beta$ ,which in turn means $\pmb { \nabla _ { u } } \pmb { d t } = 0$ for all $\pmb { u }$ In words: the gradient of universal time is covariantly constant.

By this process one can construct a set of coordinate-free statements about Newtonian spacetime $\left( \mathbf { B 0 X } \ 1 2 . 4 \right)$ that are completely equivalent to the standard, non-geometric version of Newton's gravitation theory. From standard Newtonian theory, one can deduce these geometric statements (exercise l2.7); from these geometric statements, regarded as axioms, one can deduce standard Newtonian theory (exercise 12.8).

Coordinate-free，geometric axioms for Newton's theory of gravity

# Exercise 12.7. FROM NEWTON TO CARTAN

From the standard axioms of Newtonian theory (last part of Box l2.4) derive the geometric axioms (first part of Box l2.4). Suggested procedure:Verify each of the geometric axioms by a calculation in the Galilean coordinate system. Make free use of the calculations and results in $\ S 1 2 . 1$

# EXERCISES

# Exercise 12.8. FROM CARTAN TO NEWTON

From the geometric axioms of Newtonian theory (first part of Box l2.4) derive the standard axioms (last part of Box l2.4). Suggested procedure: (l) Pick three orthonormal, spatial basis vectors $( \pmb { \mathscr { e } } _ { j }$ with $\begin{array} { r } { \pmb { e } _ { j } \cdot \pmb { e } _ { k } = \delta _ { j k } } \end{array} .$ at some event ${ \mathcal { P } } _ { 0 }$ Parallel transport each of them by arbitrary routes to all other events in spacetime.

(2）Use the condition $\mathcal { R } ( \pmb { u } , \pmb { n } ) \pmb { e } _ { j } = 0$ for all $\pmb { u }$ and $\pmb { n }$ [axiom (3)] and an argument like that in $\ S 1 1 . 5$ to conclude: (a) the resultant vector fields $\pmb { e _ { j } }$ are independent of the arbitrary transport routes.(b) $\pmb { \nabla _ { \pmb { e } _ { j } } } = 0$ for the resultant fields,and (c) $[ { \pmb e } _ { j } , { \pmb e } _ { k } ] = 0$

(3)Pick an arbitrary“time line”,which passes through each space slice (slice of constant $t )$ once and only once.Parametrize it by $t$ and select its tangent vector as the basis vector ${ \pmb { e } } _ { 0 }$ at each event along it. Parallel transport each of these ${ \pmb { e } } _ { 0 }$ 's throughout its respective space slice by arbitrary routes.

(4) From axiom (4) conclude that the resultant field is independent of the transport routes; also show that the above construction process guarantees $\pmb { \nabla } _ { j } \pmb { e } _ { 0 } = \pmb { \nabla } _ { 0 } \pmb { e } _ { j } = 0$

(5)Show that $[ { \pmb e } _ { \alpha } , { \pmb e } _ { \beta } ] = 0$ for all pairs of the four basis-vector fields,and conclude from this that there exists a coordinate system("Galilean coordinates") in which $\pmb { e } _ { \alpha } = \partial / \partial x ^ { \alpha }$ (see $\ S 1 1 . 5$ and exercise 9.9).

(6) Show that in this coordinate system $\pmb { e } _ { j } \cdot \pmb { e } _ { k } = \delta _ { j k }$ everywhere (space coordinates are Euclidean). and the only nonzero components of the connection coeficient are $T ^ { j } { _ { 0 0 } }$ ；here axioms (6) and (2） will be helpful.

(7)From the self-adjoint property of the Jacobi curvature operator (axiom 7) show that $R _ { 0 k 0 } ^ { j } = R _ { 0 j 0 } ^ { k }$ showatisos ${ T ^ { j } } _ { 0 0 , k } = { T ^ { k } } _ { 0 0 , j }$ and from this conclude that there exists a potential such that $T ^ { j } { } _ { 0 0 } = \Phi _ { . j } .$

(8) Show that the geometric field equation (axiom 5） reduces to Poisson's equation ²Φ = 4mp.

(9) Show that the geodesic equation for free fall (axiom 8) reduces to the Newtonian equation of motion $d ^ { 2 } x ^ { j } / d t ^ { 2 } + \dot { \phi } _ { { \scriptsize ; } } = 0$

(continued on page 302)

# Box 12.4 NEWTONIAN GRAVITY: GEOMETRIC FORMULATION CONTRASTED WITH STANDARD FORMULATION

# Geometric Formulation

Newton's theory of gravity and the properties of Newtonian spacetime can be derived from the following axioms. (For derivation see exercise 12.8.)

(l） There exists a function $t$ called“universal time",and a symmetric covariant derivative $\blacktriangledown$ (with associated geodesics, parallel transport law, curvature operator, etc.).

(2) The 1-form $\pmb { d t }$ is covariantly constant; ie.,

$$
\pmb { \nabla } _ { \pmb { u } } \pmb { d t } = 0 \mathrm { ~ f o r ~ a l l ~ } \pmb { u } .
$$

[Consequence: if $\pmb { w }$ is a spatial vector field (i.e., $\pmb { w }$ lies everywhere in a surface of constant $t$ i.e. $\langle d t , { \pmb w } \rangle = 0$ everywhere), then $\yen 12$ is also spatial for every $\pmb { u }$

$$
\begin{array} { r } { \langle d t , \nabla _ { u } w \rangle = \nabla _ { u } \langle \underbrace { d t , w } _ { \begin{array} { l } { \begin{array} { l } { \begin{array} { r } { \cdot } \end{array} } \end{array} } } - \langle \underbrace { \nabla _ { u } \ : d t } _ { \begin{array} { l } { \vert } \\ { \begin{array} { l } { \cdot } \end{array} } } , w \rangle = 0 . ] } \\ { \left[ 0 \mathrm { ~ a l w a y s } \right] } \end{array} \end{array} \end{array}
$$

(3） Spatial vectors are unchanged by parallel transport around infinitesimal closed curves; i.e.,

(4) All vectors are unchanged by parallel transport around infinitesimal, spatial, closed curves; i.e.,

(5）The Ricci curvature tensor, $R _ { \alpha \beta } \equiv R _ { \alpha \mu \beta } ^ { \mu }$ , has the form

$$
R i c c i = 4 \pi \rho \ d t \otimes \ d t ,
$$

where $\pmb { \rho }$ is the density of mass.

(6) There exists a metric“.”defined on spatial vectors only，which is compatible with the covariant derivative in this sense: for any spatial $\boldsymbol { \mathsf { \Sigma } }$ and $\pmb { v } ,$ and for any $\pmb { u }$ whatsoever,

$$
\nabla _ { \boldsymbol { u } } ( \boldsymbol { w } \cdot \boldsymbol { v } ) = ( \nabla _ { \boldsymbol { u } } \boldsymbol { w } ) \cdot \boldsymbol { v } + \boldsymbol { w } \cdot ( \nabla _ { \boldsymbol { u } } \boldsymbol { v } ) .
$$

[Note: axioms (l), (2),and (3) guarantee that such a spatial metric can exist; see exercise 12.9.]

(7）The Jacobi curvature operator $\mathcal { f } \left( \pmb { u } , \pmb { n } \right)$ , defined for any vectors ${ \pmb u } , { \pmb n } , { \pmb p }$ by

$$
\mathscr { f } ( u , n )  { \boldsymbol { p } } = \frac { 1 } { 2 } [ \mathscr { R } (  { \boldsymbol { p } } , \pmb { n } )  { \boldsymbol { u } } + \mathscr { R } (  { \boldsymbol { p } } , \pmb { u } )  { \boldsymbol { n } } ] ,
$$

is “self-adjoint” when operating on spatial vectors; i.e., (8)“Ideal rods” measure the lengths that are calculated with the spatial metric; "ideal clocks” measure universal time $t$ (or some multiple thereof); and “freely falling particles” move along geodesics of $\pmb { \triangledown }$ [Note: this can be regarded as a definition of “ideal rods,”“ideal clocks,” and “freely falling particles.”A more complete theory (e.g.，general relativity； see $\ S 1 6 . 4 )$ would predict in advance whether a given physical rod or clock is ideal, and whether a given real particle is freely falling.]

Note: For an alternative but equivalent set of axioms,see pp. lO6-lO7 of Trautman (1965).

# Standard Formulation

The following standard axioms are equivalent to the above.

(l） There exist a universal time $t .$ ，a set of Cartesian space coordinates $x ^ { j }$ (called “Galilean coordinates"),and a Newtonian gravitational potential $\pmb { \phi }$

(2） The density of mass $\rho$ generates the Newtonian potential by Poisson's equation,

$$
\nabla ^ { 2 } \Phi \equiv \frac { \partial ^ { 2 } \phi } { \partial _ { \cdot } x ^ { j } \partial x ^ { j } } = 4 \pi \rho .
$$

(3） The equation of motion for a freely fallng particle is

$$
\begin{array} { r } { \frac { d ^ { 2 } . { \bf \vec { r } } ^ { j } } { d t ^ { 2 } } + \frac { \partial \phi } { \partial x ^ { j } } = 0 . } \end{array}
$$

(4）“Ideal rods” measure the Galilean coordinate lengths:“ideal clocks”measure universal time.

# ExerciSe 12.9. SPATIAL METRIC ALLOWED BY OTHER AXIOMS

Show that the geometric axioms (1),(2),and (3) of Box 12.4 permit one to introduce a spatial metric satisfying axiom (6). Hint:Pick an arbitrary spatial basis $\{ \pmb { e } _ { i } \}$ at some event. Define it to be orthonormal. $\pmb { e } _ { \dag } \cdot \pmb { e } _ { \ b { k } } \equiv \delta _ { j k }$ .Extend this basis through all spacetime by the method used in (1) of exercise 12.8. Define $\pmb { e } _ { j } \cdot \pmb { e } _ { k } \equiv \delta _ { j k }$ everywhere in spacetime for this basis. Then prove that the resulting metric satisfies the compatibility condition of axiom (6).

# Exercise 12.10. SPACETIME METRIC FORBIDDEN BY OTHER AXIOMS

Show that in Newtonian spacetime it is impossible to construct a nondegenerate spacetime metric ${ \pmb g }$ .defined on all vectors,that is compatible with the covariant derivative in the sense that

$$
\nabla _ { \boldsymbol { u } } g ( \boldsymbol { n } , \boldsymbol { p } ) = g ( \nabla _ { \boldsymbol { u } } \boldsymbol { n } , \boldsymbol { p } ) + g ( \boldsymbol { n } , \nabla _ { \boldsymbol { u } } \boldsymbol { p } ) .
$$

Note: to prove this requires mastery of the material in Chapter 8 or 13; so study either 8 or 13 before tackling it. Hint: Assume that such a $\pmb { \mathscr { g } }$ exists. Show,by the methods of exercise 12.8,that in a Galilean coordinate system the spatial components $g _ { j k }$ are independent of position in spacetime. Then use this and the form of $R ^ { \alpha } { } _ { \beta \gamma \delta }$ in Galilean coordinates to prove $R _ { \mathrm { i 0 } k 0 }$ and $- R _ { 0 i k 0 }$ are not identical, a result that conflicts with the symmetries of the Riemann tensor [eq.(8.45)] in a manifold with compatible metric and covariant derivative.

# $\$ 12.5$ . THE GEOMETRIC VIEW OF PHYSICS: A CRITIQUE

The principle of general covariance has no forcible content

An important digression is in order.

“Every physical quantity must be describable by a (coordinate-free） geometric object,and the laws of physics must all be expressble as geometric relationships between these geometric objects.” This view of physics, sometimes known as the "principle of general covariance," pervades twentieth-century thinking. But does it have any forcible content? No, not at all, according to one viewpoint that dates back to Kretschmann(1917). Any physical theory originally written in a special coordinate system can be recast in geometric,coordinate-free language. Newtonian theory is a good example, with its equivalent geometric and standard formulations (Box l2.4). Hence,as a sieve for separating viable theories from nonviable theories, the principle of general covariance is useless.

Twentieth-century viewpoint judges a theory by simplicity of its geometric formulation

Einstein's theory of gravity is simple: Newton's is complex

But another viewpoint is cogent. It constructs a powerful sieve in the form of a slightly altered and slightly more nebulous principle:“Nature likes theories that are simple when stated in coordinate-free, geometric language."\* According to this principle, Nature must love general relativity,and it must hate Newtonian theory. Of all theories ever conceived by physicists, general relativity has the simplest, most elegant geometric foundation [three axioms: (l) there is a metric;(2) the metric is governed by the Einstein field equation ${ \pmb { G } } = 8 \pi { \pmb { T } } .$ ：(3）all special relativistic laws of physics are valid in local Lorentz frames of metric]. By contrast, what diabolically clever physicist would ever foist on man a theory with such-a complicated geometric foundation as Newtonian theory?

Of course,from the nineteenth-century viewpoint, the roles are reversed. It judged simplicity of theories by examining their coordinate formulations. In Galilean coordinates,Newtonian theory is beautifully simple.Expressed as differential equations for the metric coefficients in a specific coordinate system,Einstein's field 'equations (ten of them now!) are horrendously complex.

The geometric, twentieth-century view prevails because it accords best with experimental data (see Chapters 38-40). In Chapter l7 it will be applied ruthlessly to make Einstein's field equation seem compelling.
