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


<!-- chunk 0008: pages 491-560 -->
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
