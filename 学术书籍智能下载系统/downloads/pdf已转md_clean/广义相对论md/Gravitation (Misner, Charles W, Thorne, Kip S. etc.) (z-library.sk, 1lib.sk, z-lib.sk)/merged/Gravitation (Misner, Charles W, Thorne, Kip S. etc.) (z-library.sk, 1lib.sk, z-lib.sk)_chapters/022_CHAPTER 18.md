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

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0007_pages_0421-0490/auto/images/702ef4d9626c705a7fc3c251f18219baacac27092b4dbd3225218b73e535163f.jpg)  
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
