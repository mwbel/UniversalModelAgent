CHAPTER 15

# BIANCHI IDENTITIES AND THE BOUNDARY OF A BOUNDARY

This chapter is entirely Track 2. As preparation,one needs to have covered(1) Chapter 4 (differential forms) and (2) Chapter 14 (computation of curvature).

In reading it,one will be helped by Chapters g-11 and 13.

It is not needed as preparation for any later chapter,but it will be helpful in Chapter 17 (Einstein field equations).

Identities and conservation of the source: electromagnetism and gravitation compared:

# S15.1. BIANCHI IDENTITIES IN BRIEF

Geometry gives instructions to matter, but how does matter manage to give instructions to geometry? Geometry conveys its instructions to matter by a simple handle: "pursue a world line of extremal lapse of proper time (geodesic)."What is the handle by which matter can act back on geometry? How can one identify the right handle when the metric geometry of Riemann and Einstein has scores of interesting features? Physics tels one what to look for: a machinery of coupling between gravitation (spacetime curvature) and source (matter; stress-energy tnsor $\pmb { \tau }$ ）that will guarantee the automatic conservation of the source ( $\begin{array} { r }  \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla \nabla } \mathbf { \nabla } \mathbf { \nabla } \nabla \mathbf { \nabla } \mathbf { \nabla } \nabla \mathbf { \nabla } \mathbf { \nabla \nabla } \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \nabla \mathbf { \nabla } \nabla \nabla \mathbf { \nabla } \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \end{array}$ ).Physics therefore asks_mathe-matics: “What tensor-like feature of the geometry is automatically conserved?” Mathematics comes back with the answer: “The Einstein tensor.” Physics queries, “How does this conservation come about?” Mathematics, in the person of Elie Cartan,replies,“Through the principle that ‘the boundary of a boundary is zero'” (Box 15.1).

Actually, two features of the curvature are automatically conserved; or, otherwise stated,the curvature satisfies two Bianchi identities,the subject of this chapter. Both features of the curvature, both “geometric objects,"lend themselves to representation in diagrams, moreover,diagrams that show in action the principle that“the boundary of a boundary is zero.”In this respect, the geometry of spacetime shows a striking analogy to the field of Maxwell electrodynamics.

In electrodynamics there are four potentials that are united in the 1-form ${ \pmb A } \equiv$ $A _ { \mu } \pmb { d } x ^ { \mu }$ . Out of this quantity by differentiation follows the Faraday, ${ \pmb F } = \pmb { d A }$ . This feld satisfies the identity $\pmb { d } \pmb { F } = 0$ (identity,yes; identity lending itself to the definition $\pmb { d } \pmb { F } \equiv 0$ of a conserved source, no).

In gravitation there are ten potentials (metric coefficients $g _ { \mu \nu , \ l }$ ）that are united in the metric tensor ${ \pmb g } = \pmb { g } _ { \mu \nu } { \pmb d } x ^ { \mu } \otimes { \pmb d } x ^ { \nu }$ .Out of this quantity by two differentiations follows the curvature operator

$$
{ \mathcal R } = \frac { 1 } { 4 } { \pmb e } _ { \mu } \wedge { \pmb e } _ { \nu } R ^ { \mu \nu } { } _ { \alpha \beta } d x ^ { \alpha } \wedge d x ^ { \beta } .
$$

This curvature operator satisfies the Bianchi identity ${ \pmb d } \mathcal { R } = 0$ ，where now $" d "$ is a generalization of Cartan's exterior derivative, described more fully in Chapter 14 (again an identity, but again one that does not lend itself to the definition of a conserved source).

${ \pmb d } { \pmb d } ^ { * } { \pmb F } \equiv 0$ plus Maxwell equations $\implies { \bf { \Theta } } ^ { * } J = 0$

In electromagnetism,one has to go to the dual, $" _ { F , }$ to have any feature of the field that offers a handle to the source, $d ^ { * } F = 4 \pi ^ { * } J .$ The conservation of the source, ${ \pmb d } ^ { * } { \pmb J } = 0$ ，appears as a consequence of the identity $d d ^ { * } F = 0$ ；or,by a rewording of the reasoning $\mathbf { ( B o x ~ 1 5 . 1 ) }$ ，as a consequence of the vanishing of the boundary of a boundary.

(continued on page 370)

# A. The Idea in Its 1-2-3-Dimensional Form

Begin with an oriented cube or approximation to a cube (3-dimensional).

Its boundary is composed of six oriented faces, each two-dimensional. Orientation of each face is indicated by an arrow.

Boundary of any one oriented face consists of four oriented edges or arrows,each one-dimensional.

Every edge unites one face with another. No edge stands by itself in isolation.

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/addc80e273f7698ef68af483b4ff20c213c9eeae5482dff25e44efa64e0b59d9.jpg)  
Box 15.1 THE BOUNDARY OF A BOUNDARY IS ZERO

“Sum” over all these edges, with due regard to sign. Find that any given edge is counted twice, once going one way, once going the other.

Conclude that the one-dimensional boundary of the two-dimensional boundary of the three-dimensional cube is identically zero.

# B. The Idea in Its 2-3-4-Dimensional Form

Begin with an oriented four-dimensional cube or approximation thereto. The coordinates of the typical corner of the four-cube may be taken to be $( t _ { 0 } \pm \frac { 1 } { 2 } \Delta t$ $x _ { 0 } \pm { \textstyle { \frac { 1 } { 2 } } } \Delta x$ $y _ { 0 } \pm { \textstyle { \frac { 1 } { 2 } } } \Delta y$ ， $z _ { 0 } \pm { \scriptstyle { \frac { 1 } { 2 } } } \Delta z )$ ； and,accordingly,a sample corner itself,in an obvious abbreviation, is conveniently abbreviated $+ -- + .$ .There are l6 of these corners. Less complicated in appearance than the 4-cube itself are its three-dimensional faces,which are “exploded off of it’ into the surrounding area of the diagram, where they can be inspected in detail.

The boundary of the 4-cube is composed of eight oriented hyperfaces,each of them three-dimensional (top hyperface with extension $\Delta x \ \Delta y \Delta z .$ for example;a “front” hyperface with extension △t △y Az; etc.)

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/917973ea52723b8d1f122f58b80528eee21b3a82ee7cf913da19c29991cfaf1e.jpg)

Boundary of any one hyperface ("cube") consists of six oriented faces,each :wo-dimensional.

Every face (for example, the hatched face $\varDelta x \varDelta y$ in the lower lefthand corner) unites one hypersurface with another (the $^ { * 3 }$ -cube side face”At Ax Ay in the lower lefthand corner with the“3-cube top face" $\ 4 x \ 4 y \ 4 z$ ,in this example).No face stands by itself in isolation. The three-dimensional boundary of the 4-cube exposes no 2-surface to the outside world. It is faceless.

“Sum”over al these faces, with due regard to orientation. Find any given face is counted twice,once with one orientation, once with the opposite orientation.

Conclude that the two-dimensional boundary of the three-dimensional boundary of the four-dimensional cube is identically zero.

# C. The ldea in Its General Abstract Form

$\partial \hat { \boldsymbol { \partial } } = 0$ (the boundary of a boundary is zero).

# D. Idea Behind Application to Gravitation and Electromagnetism

The one central point is a law of conservation (conservation of charge; conservation of momentum-energy).

The other central point is“automatic fulfillment” of this conservation law.

“Automatic conservation” requires that source not be an agent free to vary arbitrarily from place to place and instant to instant.

Source needs a tie to something that, while having degrees of freedom of its own, will cut down the otherwise arbitrary degrees of freedom of the source suffciently to guarantee that the source automatically fulfills the conservation law. Give the name “field” to this something.

Define this feld and “wire it up”to the source in such a way that the conservation of the source shallbe an automatic consequence of the “zero boundary ofa boundary.” Or, more explicitly: Conservation demands no creation or destruction of source inside thefour-dimensional cube shown in the diagram. Equivalently, integral of "creation events” (integral of $\pmb { d } ^ { \ast } \pmb { J }$ for electric charge; integral of $\pmb { d } ^ { \ast } \pmb { \tau }$ for energy-momentum) over this four-dimensional region is required to be zero.

Integral of creation over this four-dimensional region translates into integral of source density-current ( $^ { \ast , \prime }$ or ${ } ^ { * } { \pmb { T } }$ ）over three-dimensional boundary of this region. This boundary consists of eight hyperfaces, each taken with due regard to orientation. Integral over upper hyperface $( ^ { * } \varDelta x \varDelta y \varDelta z ) ^ { * }$ gives amount of source present at later moment; over lower hyperface gives amount of souce present at earlier moment; over such hyperfaces as $\ " { \Delta t } { \Delta x } { \Delta y } \ "$ gives outflow of source over intervening period of time. Conservation demands that sum of these eight three-dimensional integrals shall be zero (details in Chapter 5).

Vanishing of this sum of three-dimensional integrals states the conservation requirement, but does not provide the machinery for “automatically”(or,in mathematical terms,“identically"） meeting this requirement. For that, turn to principle that“boundary of a boundary is zero.”

Demand that integral of source density-current over any oriented hyperface $\mathcal { V }$ (three-dimensional region;“cube"） shall equal integral of field over faces of this “cube”(each face being taken with the appropriate orientation and the cube being infinitesimal):

$$
4 \pi \int _ { \tau ^ { \prime } } { } ^ { \ast } J = \int _ { \partial \tau ^ { \prime } } { } ^ { \ast } F ; \qquad 8 \pi \int _ { \tau ^ { \prime } } { } ^ { \ast } { \pmb { r } } = \int _ { \partial \tau ^ { \prime } } { \binom { \mathrm { m o m e n t ~ o f } } { \mathrm { r o t a t i o n } } } .
$$

Sum over the six faces of this cube and continue summing until the faces of all eight cubes are covered. Find that any given face (as,for example, the hatched face in the diagram) is counted twice, once with one orientation, once with the other ("boundary of a boundary is zero"). Thus is guaranteed the conservation of source: integral of source density-current over three-dimensional boundary of four-dimensional region is automatically zero, making integral of creation over interior of that four-dimensional region also identically zero.

Repeat calculation with boundary of that four-dimensional region slightly displaced in one locality [the“bubble differentiation”of Tomonaga (l946) and Schwinger (l948), and conclude that conservation is guaranteed, not.oniy in the four-dimensional region as a whole,but at every point within it,and, by extension, everywhere in spacetime.

# E. Relation of Source to Field

One view: Source is primary. Field may have other duties, but its prime duty is to serve as “slave" of source. Conservation of source comes first; field has to adjust itself accordingly.

Alternative view: Field is primary. Field takes the responsibility of seeing to it that the source obeys the conservation law. Source would not know what to do in absence of the field,and would not even exist. Source is “built” from feld. Conservation of source is consequence of this construction.

One model illustrating this view in an elementary context: Concept of “classical" electric charge as nothing but “electric lines of force trapped in the topology of a multiply connected space” [Weyl (l924b)；Wheeler (1955)；Misner and Wheeler (1957)

On any view: Integral of source density-current over any three-dimensional region (a “cube” in simplified analysis above) equals integral of field over boundary of this region (the six faces of the cube above). No one has ever found any other way to understand the correlation between field law and conservation law.

# F. Electromagnetism as a Model: How to “Wire Up" Source to Field to Give Automatic Conservation of Source Via ${ } ^ { 6 6 } \partial \hat { \partial } = 0 { } ^ { 3 }$ in Its 2-3-4-Dimensional Form

Conservation means zero creation of charge (zero creation in four-dimensional region $\pmb { \mathcal { a } }$ ）

Conservation therefore demands zero value for integral of charge density-current over three-dimensional boundary of this volume; thus,

$$
0 = \int _ { \Omega } { \frac { \partial J ^ { \mu } } { \partial x ^ { \mu } } } d ^ { + } \Omega = \int _ { \partial \Omega } J ^ { \mu } d ^ { 3 } { \cal { \Sigma } } _ { \mu }
$$

in the Track-l language of Chapters 3 and 5.Equivalently, in the coordinate-free abstract language of $\ S \ S 4 . 3 \ – 4 . 6$ ,one has

$$
0 = \int _ { \Omega } d ^ { \ast } J = \int _ { \partial \Omega } { ^ \ast } J ,
$$

where

$$
\begin{array} { l } { { { } ^ { * } J = { } ^ { * } J _ { 1 2 3 } \ d x ^ { 1 } \wedge \ d x ^ { 2 } \wedge \ d x ^ { 3 } + { } ^ { * } J _ { 0 2 3 } \ d x ^ { 0 } \wedge \ d x ^ { 2 } \wedge \ d x ^ { 3 } } } \\ { { \qquad + { } ^ { * } J _ { 0 3 1 } \ d x ^ { 0 } \wedge \ d x ^ { 3 } \wedge \ d x ^ { 1 } + { } ^ { * } J _ { 0 1 2 } \ d x ^ { 0 } \wedge \ d x ^ { 1 } \wedge \ d x ^ { 2 } } } \end{array}
$$

("eggcrate-like structure” of the 3-form of charge-density and current-density).

Fulfill this conservation requirement automatically ("identically"） through the principle that“the boundary of a boundary is zero” by writing $4 \pi ^ { * } J = d ^ { * } F$ ;thus,

$$
4 \pi \int _ { \partial \mathcal { Q } } { ^ { \ast } J } = \int _ { \partial \mathcal { Q } } d ^ { \ast } F = \int _ { \partial \partial \mathcal { Q } ( { \mathrm { z e r o } } \mathfrak { t } ) } { ^ { \ast } F } \equiv 0
$$

or, in Track-1language, write $4 \pi J ^ { \mu } = { \cal F } ^ { \mu \nu } { } _ { ; \nu }$ and have

$$
4 \pi \int _ { \partial \mathcal { Q } } J ^ { \mu } d ^ { 3 } \Sigma _ { \mu } = \int _ { \partial \mathcal { Q } } F ^ { \mu \nu } { } _ { ; \nu } d ^ { 3 } \Sigma _ { \mu } = \int _ { \partial \ni \mathcal { Q } ( { \bf z e r o } ; ) } F ^ { \mu \alpha } d ^ { 2 } \Sigma _ { \mu \alpha } \equiv 0 .
$$

In other words, half of Maxwel's equations in their familiar flat-space form,

$$
\operatorname { d i v } { \cal E } = \nabla \cdot { \cal E } = 4 \pi \rho , \operatorname { c u r l } { \cal B } = \nabla \times { \cal B } = \dot { \cal E } + 4 \pi { \cal J } ,
$$

“wire up" the source to the field in such a way that the law of conservation of source follows directly from ${ } ^ { 6 6 } \partial \widehat { \partial } \varDelta 2 = 0$ ”

# G. Electromagnetism Also Employs ${ } ^ { \bullet } \widehat { \sf d } \widehat { \sf d } = 0 ^ { \bullet }$ in its 1-2-3-Dimensional Form ("No Magnetic Charge')

Magnetic charge is linked with feld via $4 \pi J _ { \mathrm { m a g } } = d F$ (see point F above for translation of this compact Track-2 language into equivalent Track-l terms). Absence of

any magnetic charge says that integral of $J _ { \tt m a g }$ over any 3-volume $\Im ^ { * }$ is necessarily zero;or ("integration by parts,” generalized Stokes theorem)

$$
0 = \int _ { \mathcal { F } } d \pmb { F } = \int _ { \partial \mathcal { V } } \pmb { F } = \bigg ( \mathrm { \Pi } _ { \mathrm { e x i t i n g ~ t h r o u g h ~ } \hat { \sigma } \mathcal { V } } ^ { \mathrm { t o t a l ~ m a g n e t i c ~ f l u x } } \bigg ) .
$$

In order to satisfy this requirement “automatically,” via principle that “the boundary of a boundary is zero,’write ${ \pmb F } = { \pmb d } { \pmb A }$ ("expression of field in terms of 4-potential"), and have

$$
\int _ { \partial \mathcal { V } } \pmb { F } = \int _ { \partial \mathcal { V } } \pmb { d } \pmb { A } = \int _ { \partial \partial \mathcal { V } ( \mathrm { \pmb { z e r o } } ! ) } \pmb { A } \equiv 0 .
$$

# H. Structure of Electrodynamics in Outline Form

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/0222e8c5537e326f02a67bd820ad763530a939472429ee0c5cd7be796c14afb9.jpg)

In gravitation physics,one has to go to the“double dual"(two pairs of alternating indices,two places to take the dual) $\pmb { G } = { ^ \ast } \pmb { R } ^ { \ast }$ of Riemann to have a feature of the field that offers a handle to the source:

$$
\pmb { G } = \mathrm { T r } \pmb { G } = \pmb { E } i n s t e i n = 8 \pi \pmb { T } = 8 \pi \times (
$$

The conservation of the source $\pmb { T } \equiv \pmb { e } _ { \mu } T ^ { \mu } { } _ { \nu } \pmb { \omega } ^ { \nu }$ can be stated $\pmb { \bigtriangledown } \cdot \pmb { \tau } = 0$ .But better suited for the present purpose is the form (see Chapter l4 and exercise 14.18)

# I. Structure of Geometrodynamics in Outline Form

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/f4e4a03d78b8cb9572c0c15877d4c8f4696af1b79db768cb5830e310c79b2a86.jpg)

where

$$
{ \pmb { d } } ^ { * } { \pmb { T } } = 0 ,
$$

${ \pmb { d } } ^ { * } { \pmb { G } } \equiv 0$ plus Einstein field equation $\implies d ^ { * } \tau = 0$

$$
{ } ^ { * } T \equiv e _ { \mu } T ^ { \mu } { } _ { \nu } ( { } ^ { * } \omega ^ { \nu } ) = e _ { \mu } T ^ { \mu \nu } d ^ { 3 } \Sigma _ { \nu } .
$$

This conservation law arises as a consequence of the “contracted Bianchi identity”, ${ \pmb { d } } ^ { * } { \pmb { G } } = 0$ ， again interpretable in terms of the vanishing of the boundary of a boundary.

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/c5b9435e17976dc13311d1bcb3a4b7b41494700c316f79ad90c1ab997f61ebae.jpg)  
Figure 15.1. Combine rotations associated with each of the six faces of the illustrated 3-volume and end up with zero net rotation ("full Bianchi identity").Reason:Contribution of any face is measured by change ina test vector A carried in parallel transport around the perimeter of that face.Combine contributions of all faces and end up with each edge traversed twice,once in one direction,once in the other direction [boundary (here one-dimensional) of boundary (two-dimensional) of indicated three-dimensional figure is zero].Detail: The vector $\pmb { A }$ ， residing at the indicated site, is transported parallel to itself over to the indicated face,then carried around the perimeter of that face by parallel transport,experiencing in the process a rotation measured by the spacetime curvature associated with that face,then transported parallel to itself back to the original site.To the lowest relevant order of small quantities one can write

$$
( \mathrm { c h a n g e ~ i n } \ \pmb { A } ) = - \pmb { A } \gamma \ \pmb { A } z \ \mathcal { A } ( \pmb { e } _ { \nu } , \ \pmb { e } _ { z } ) \ \pmb { A }
$$

in operator notation;or in coordinate language,

$$
- \delta A ^ { \alpha } = R ^ { \alpha } { } _ { \beta \upsilon z } ( \mathrm { a t } x + A x ) A ^ { \beta } A y A z .
$$

Bianchi identity, $\pmb { d } \mathcal { R } \equiv 0$ ， interpreted in terms of parallel transport around the six faces of a cube.

# $\$ 15.2$ .BIANCHI IDENTITY ${ \pmb d } \mathcal { R } = { \bf 0 }$ AS A MANIFESTATION OF "BOUNDARY OF BOUNDARY $\mathbf { \mu } = \mathbf { 0 } ^ { \prime \prime }$

Such is the story of the two Bianchi identities in outline form; it is now appropriate to fill in the details.Figure l5.1 illustrates the full Bianchi identity, $\pmb { d } \mathcal { R } = 0$ (see exercise l4.l7),saying in brief,“The sum of the curvature-induced rotations associated with the six faces of any elementary cube is zero.”The change in a vector $\pmb { A }$ associated with transport around the perimeter of the indicated face evaluated to the lowest relevant order of small quantities is given by

$$
- \delta A ^ { \alpha } = { R ^ { \alpha } } _ { \beta y z } ( { \mathrm { a t ~ } } x + A x ) A ^ { \beta } A y A z .
$$

The opposite face gives a similar contribution, except that now the sign is reversed and the evaluation takes place at $x$ rather than at $x + 4 x$ .The combination of the contributions from the two faces gives

$$
{ \frac { \partial { R ^ { \alpha } } _ { \beta y z } } { \partial x } } A ^ { \beta } \varDelta x \varDelta y \varDelta z ,
$$

when Riemann normal coordinates are in use. In such coordinates, the vanishing of the total $- \delta A ^ { \alpha }$ contributed by all six faces implies

$$
{ R ^ { \alpha } } _ { \beta y z ; x } + { R ^ { \alpha } } _ { \beta z x ; y } + { R ^ { \alpha } } _ { \beta x y ; z } = 0 .
$$

Here semicolons (covariant derivatives) can be and have been inserted instead of commas (ordinary derivatives), because the two are identical in the context of Riemann normal coordinates； and the covariant version (l5.3） generalizes itself to arbitrary curvilinear coordinates. Turn from an xyz cube to a cube defined by any set of coordinate axes,and write Bianchi's identity in the form

$$
{ R ^ { \alpha } } _ { \beta [ \lambda _ { \mu } ; \nu ] } = 0 .
$$

(See exercise l4.17 for one reexpression of this identity in the abstract coordinateindependent form, ${ \pmb d } \mathcal { R } = 0$ ,and $\ S 1 5 . 3$ for another.) This identity occupies much the same place in gravitation physics as that occupied by the identity $d F = d d A \equiv 0$ in electromagnetism:

$$
F _ { [ \lambda _ { \mu } , \nu ] } = F _ { [ \lambda _ { \mu } ; \nu ] } = 0 .
$$

# $\$ 15.3$ . MOMENT OF ROTATION: KEY TO CONTRACTED BIANCHI IDENTITY

The contracted Bianchi identity,the identity that offers a “handle to couple to the source,”was shown by Elie Cartan to deal with “moments of rotation” [Cartan (1928)；Wheeler (l964b); Misner and Wheeler (1972)].Moments are familiar in elementary mechanics.A rigid body willnot remain at rest unless allthe forces acting on it sum to zero:

$$
\sum _ { i } F ^ { ( i ) } = 0 .
$$

Although necessary,this condition is not sufficient. The sum of the moments of these forces about some point $\mathcal { P }$ must also be zero:

$$
\sum _ { i } \left( { \mathcal { P } } ^ { ( i ) } - { \mathcal { P } } \right) \wedge F ^ { ( i ) } = 0 .
$$

Exactly what point these moments are taken about happily does not matter, and this for a simple reason. The arbitrary point in the vector product (l5.7) has for coefficient the quantity $\pmb { \mathcal { Z } } _ { i } \pmb { F } ^ { ( i ) }$ ，which already has been required to vanish. The situation is similar in the elementary cube of Figure l5.1.Here the rotation associated with a given face is the analog of the force $F ^ { ( i ) }$ in mechanics. That the sum of these rotations vanishes when extended over allsix faces of the cube is the analog of the vanishing of the sum of the forces $F ^ { ( i ) }$

What is the analog for curvature of the moment of the force that one encounters in mechanics? It is the moment of the rotation associated with a given face of the

Net moment of rotation over all six faces of a cube:

(1）described

cube.The value of any individual moment depends on the reference point $\mathcal { S }$ However, the sum of these moments taken over all six faces of the cube will have a value independent of the reference point $\mathcal { P }$ ,for the same reason as in mechanics. Therefore $\mathcal { P }$ can be taken where one pleases, inside the elementary cube or outside it. Moreover, the cube may be viewed as a bit of a hypersurface sliced through spacetime. Therefore $\mathcal { S }$ can as well be off the slice as on it.It is only required that all distances involved be short enough that one obtains the required precision by calculating the moments and the sum of moments in a local Riemann-normal coordinate system. One thus arrives at a $\mathcal { P }$ -independent totalized moment of rotation (not necessarily zero; gravitation is not mechanics!） associated with the cube in question.

(2)equated to integral of source, $\textstyle \int ^ { * \tau }$ Over interior of cube

Now comes the magic of“the boundary of the boundary is zero.” Identify this net moment of rotation of the cube, evaluated by summing individual moments of rotation associated with individual faces,with the integral of the source densitycurrent (energy-momentum tensor ${ } ^ { \ast } \mathbf { r }$ ）over the interior of the 3-cube.Make this identification not only for the one 3-cube,but for all eight 3-cubes (hyperfaces) that bound the four-dimensional cube in Box 15.1. Sum the integrated source densitycurrent ${ \ast } _ { \pmb { T } }$ not only for the one hyperface of the 4-cube, but for all eight hyperfaces. Thus have

$$
\begin{array}{c} \int _ { \pm \mathrm {  ~ \scriptstyle ( \begin{array} { c } { { \scriptstyle ( \mathrm { { e x a t i o n } }  } } \\ { { \scriptstyle ( \mathrm { e x a t i o n }  } } \\ { { \scriptstyle (  d ^ { * } \mathrm {  { \scriptstyle ( \Lambda \Lambda ) } ) } } } \end{array} ) } \ = \ \int _ { \begin{array} { c } { { \scriptstyle ( \mathrm { s o u r c e } \atop { \scriptstyle ( d \mathrm { { e n d t i o n } } ) }  } } \\ { { \scriptstyle ( \mathrm { s o u r c e } \atop { \scriptstyle ( d \mathrm { { e n d t i o n } } ) }  } } \\ { { \scriptstyle ( \mathrm { n o t e a r c e } \atop { \scriptstyle ( d \mathrm { e n d } ) }  } } \end{array} ( \begin{array} { l } { { \scriptstyle \mathrm { s o u r c e } \ \ \mathrm { c u r c e } } } \\ { { \scriptstyle ( \mathrm { n o t e a r c e } ) } } \\ { { \scriptstyle ( \mathrm { n o t e a r c e } ) } } \end{array} ) } \end{array} \ }  \\ { = \ \sum _ { \begin{array} { c } { { \scriptstyle ( \mathrm { n o t e a l i o n } \atop { \scriptstyle \mathrm { { e n d e a t i o n } } ) } } } \\ { { \scriptstyle ( \mathrm { n o t e a r c e } ) } } \end{array} \ ( \begin{array} { l } { { \scriptstyle \mathrm { n o t e } \ \ \mathrm { n o m e n t \ q r o \ c i t i o n } } } \\ { { \scriptstyle ( \mathrm { n o t e a r c e } ) } } \end{array} ) } } \\  = \ \sum _  \begin{array} { c } { { \scriptstyle ( \mathrm { n o m e n t \ q r o \ c i t i o n } \atop { \scriptstyle \mathrm { { e n d e a t i o n } } \atop { \scriptstyle \mathrm { { e n d e a t i o n } } \atop { \scriptstyle \mathrm { { e n d e a t i o n } } \atop { \scriptstyle \mathrm { { e n d e a t i o n } } \atop { \scriptstyle \mathrm { { e n d e a t i o n } } \atop { \scriptstyle \mathrm { { e n o m e n t e } } \ } } } } } ) } } \end{array} } ( \begin{array} { l } { { \scriptstyle \mathrm { n o m e n t \ q r o \ c u i o n } } } \\ { { \scriptstyle \mathrm { n o s c o i a t e d \ w i t h \ s p e c i s i e d } } } \\ { { \scriptstyle ( \mathrm { n o t e a r c e } \ ) } } \end{array} ) .
$$

Let the moments of rotation, not only for the six faces of one cube,but for all the faces of all the cubes, be taken with respect to one and the same point $\mathscr { P }$ Recall $( \mathbf { B o x } \ 1 5 . 1 )$ that any given face joins two cubes or hyperfaces. It therefore appears twice in the count of faces,once with one orientation ("sense of circumnavigation in parallel transport to evaluate rotation") and once with the opposite orientation. Therefore the double sum vanishes identically (boundary of a boundary is zero!) This identity establishes existence of a new geometric object, a feature of the curvature, that is conserved,and therefore provides a handle to which to couple a source. The desired result has been achieved. Now to translate it into standard mathematics!

# $\$ 15.4$ . CALCULATION OF THE MOMENT OF ROTATION

It remains to find the tensorial character and value of this conserved Cartan moment of rotation that appertains to any elementary 3-volume. The rotation associated with the front face Ay $\Delta z e _ { y } \wedge e _ { z }$ of the cube in Figure 15.l will be represented by the bivector

$$
{ \binom { \mathrm { r o t a t i o n ~ a s s o c i a t e d } } { \mathrm { w i t h ~ f r o n t ~ } { \cal A } y { \cal A } z \ \mathrm { f a c e } } } = e _ { _ { \lambda } } \wedge e _ { _ { \mu } } R ^ { | { \lambda } \mu | } { } _ { y z } { \cal A } y { \cal A } z
$$

located at $\begin{array} { r } { \overline { { \varphi } } _ { \mathrm { f r o n t } } = ( t - \frac { 1 } { 2 } \bar { A } t , x + A x , y + \frac { 1 } { 2 } \varDelta y , z + \frac { 1 } { 2 } \varDelta z ) . } \end{array}$ This equation uses Riemann normal coordinates; indices enclosed by strokes,as in $| \lambda \mu |$ ,are summed with the restriction $\lambda < \mu$ . The moment of this rotation with respect to the point $\mathcal { P }$ will be represented by the trivector

$$
\left( \begin{array} { l } { \mathrm { m o m e n t ~ o f ~ r o t a t i o n } } \\ { \mathrm { a s s o c i a t e d ~ w i t h } } \\ { \mathrm { f r o n t ~ } A y \ A z \ \mathrm { f a c e } } \end{array} \right) = ( \begin{array} { l } { \mathcal { P } _ { \mathrm { c e n t e r } } } \\ { \underset { \mathrm { f a c e } } { \operatorname { e \% } } } \end{array} - \begin{array} { l } { \mathcal { P } } ) \wedge \pmb { \mathscr { e } } _ { \lambda } \wedge \pmb { e } _ { \mu } R ^ { { \mathrm { i } } \lambda \mu } \underset { y z } { A } y \ A z . \end{array}
$$

Here neither $\mathcal { P } _ { \mathrm { c e n t e r f r o n t } }$ nor $\mathcal { P }$ has any well-defined meaning whatsoever as a vector, but their difference is a vector in the limit of infinitesimal separation, $\varDelta \mathcal { P } =$ $\mathcal { P } _ { \mathrm { c e n t e r f r o n t } } - \mathcal { P }$ .With the back face a similar moment of rotation is assciated, with the opposite sign, and with $\mathcal { P } _ { \mathrm { c e n t e r f r o a t } }$ replaced by $\mathcal { P } _ { \mathtt { c e n t e r b a c k } }$ . In the difference between the two terms, the factor $\mathcal { P }$ is of no interest, because one is already assured it will cancel out [Bianchi identity (15.4)； analog of $\Sigma F ^ { ( i ) } = 0$ in mechanics]. The difference ${ \mathcal { P } } _ { \cdot }$ cente front $- \mathcal { P } _ { \mathrm { c e n t e r b a c k } }$ has the value $\pmb { \varDelta x e } _ { x }$ Summing over allsix faces, one has

$$
\begin{array} { r } { \left( \begin{array} { l } { \mathrm { n e t ~ m o m e n t ~ o f } } \\ { \mathrm { r o t a t i o n ~ a s s o c i a t e d } } \\ { \mathrm { w i t h ~ c u b e ~ o r ~ h y p e r } } \\ { \mathrm { f a c e ~ } A x ~ A y ~ A z } \\ { \hphantom { n e t } \hphantom { n e t } \hphantom { n e t } \hphantom { n e t } \hphantom { n e t } e _ { z } \wedge e _ { \mu } R ^ { \mathrm { i } \mu } \underset { y z } { A x } ~ A y ~ A z ~ ( \mathrm { f r o n t ~ a n d ~ b a c k } ) } \\ { \hphantom { n e t } \longrightarrow ~ - \hphantom { n e t } \hphantom { n e t } \hphantom { n e t } \cdots ~ + \hphantom { n e t } e _ { y } \wedge e _ { \mu } R ^ { \mathrm { i } \mu } \underset { z y } { A x } ~ A z ~ A x ~ ( \mathrm { s i d e s } ) } \\ { \hphantom { n e t } \qquad \quad + \hphantom { n e t } \rho _ { z } \wedge e _ { \lambda } \wedge e _ { \mu } R ^ { \mathrm { i } \mu } \underset { z y } { A z } ~ A x ~ A y ~ ( \mathrm { t o p ~ a n d ~ b o t t o m } ) . } \end{array} \right. } \end{array}
$$

This sum one recognizes as the value (on the volume element $e _ { x } \wedge e _ { y } \wedge e _ { z } \varDelta x$ $\boldsymbol { \mathsf { \Delta } } \boldsymbol { y } \boldsymbol { \mathsf { \Delta } } \boldsymbol { \mathsf { \Delta } } \boldsymbol { z } )$ of the 3-form

$$
{ \pmb e } _ { \nu } \wedge { \pmb e } _ { \lambda } \wedge { \pmb e } _ { \mu } R ^ { | \lambda \mu | } { } _ { | \alpha \beta | } d x ^ { \nu } \wedge d x ^ { \alpha } \wedge d x ^ { \beta } .
$$

Moreover this 3-form is defined,and precisely defined, at a point, whereas (15.11), applying as it does to an extended region, does not lend itself to an analysis that is at the same time brief and precise. Therefore forego (l5.11) in favor of the 3-form. Only remember, when it comes down to interpretation, that this 3-form is to be evaluated for the“cube” ${ \pmb e } _ { x } \wedge { \pmb e } _ { y } \wedge { \pmb e } _ { z } A x A y A z$ . Now note that the “trivectorvalued moment-of-rotation 3-form” can also be written as

(5) abstracted to give $\pmb { d } \mathcal { P }$ >

$$
\binom { \mathrm { m o m e n t ~ o f } } { \mathrm { r o t a t i o n } } = d \mathcal { P } \wedge \hat { \mathcal { R } } = e _ { \nu } \wedge e _ { \lambda } \wedge e _ { \mu } R ^ { | \lambda \mu | } | _ { \alpha \beta ! } d x ^ { \nu } \wedge d x ^ { \alpha } \wedge d x ^ { \beta } .
$$

Here

$$
d \mathscr { P } = \mathscr { e } _ { \sigma } d x ^ { \sigma }
$$

is Cartan's $\textstyle { \binom { 1 } { 1 } }$ unit tensor. Also $\mathcal { R }$ is the curvature operator, treated as a bivectorvalued 2-form:

$$
{ \mathcal R } = \pmb { \mathscr { e } } _ { \lambda } \wedge \pmb { \mathscr { e } } _ { \mu } R ^ { | \lambda \mu | } | _ { \alpha \beta | } d x ^ { \alpha } \wedge d x ^ { \beta } .
$$

Using the language of components as in (15.1l), or the abstract language introduced in (15.l2),one finds oneself dealing with a trivector.A trivector can be left a trivector, as, in quite another context, an element of 3-volume on a hypersurface in 4-space can be left as a trivector. However, there it is more convenient to take the dual representation, and speak of the element of volume as a vector. Denote by $\star$ a duality operation that acts only on contravariant vectors, trivectors, etc. (but not on forms). Then in a Lorentz frame one has ${ \star ( { \pmb e } _ { 1 } \wedge { \pmb e } _ { 2 } \wedge { \pmb e } _ { 3 } ) = { \pmb e } _ { 0 } }$ ；but $\star ( d x ^ { 3 } ) = d x ^ { 3 }$ . More generally,

$$
\star ( \pmb { \mathscr { e } } _ { \nu } \wedge \pmb { \mathscr { e } } _ { \lambda } \wedge \pmb { \mathscr { e } } _ { \mu } ) = \varepsilon _ { \nu \lambda \mu } ^ { \quad \sigma } \pmb { \mathscr { e } } _ { \sigma } .
$$

(6)abstracted to give $\star ( d \mathcal { P } \wedge \mathcal { R } ) = \varrho _ { \sigma } G ^ { \sigma \tau } d ^ { 3 } \varSigma _ { \tau }$

In this notation, the“vector-valued moment-of-rotation 3-form” is

$$
{ \begin{array} { r l } & { { \binom { \mathrm { m o m e n t } } { \mathrm { o f ~ r o t a t i o n } } } = \star ( d { \mathcal { P } } \wedge { \mathcal { R } } ) = e _ { \sigma } \varepsilon _ { \nu \lambda \mu } ^ { \quad \sigma } R ^ { \left. \lambda \mu \right. } \vert _ { \alpha \beta ! } d x ^ { \nu } \wedge d x ^ { \alpha } \wedge d x ^ { \beta } } \\ & { \qquad = e _ { \sigma } ( ^ { \ast } R ) _ { \nu } ^ { \sigma } \vert _ { \alpha \beta \vert } d x ^ { \nu } \wedge d x ^ { \alpha } \wedge d x ^ { \beta } , } \end{array} }
$$

or, in one more step,

$$
\binom { \mathrm { m o m e n t } } { \mathrm { o f ~ r o t a t i o n } } = \star ( d \mathcal { P } \wedge \mathcal { R } ) = \pmb { e } _ { \sigma } ( ^ { * } R ^ { * } ) _ { \nu } ^ { \sigma \nu \tau } d ^ { 3 } \mathcal { \Sigma } _ { \tau } .
$$

Here $d ^ { 3 } \pmb { \Sigma } _ { \tau }$ is a notation for basis 3-forms,as in Box 5.4; thus,

$$
d x ^ { \nu } \wedge d x ^ { \alpha } \wedge d x ^ { \beta } = \varepsilon ^ { \nu \alpha \beta \tau } d ^ { 3 } \varSigma _ { \tau } .
$$

(In a local Lorentz frame, $d x ^ { 1 } \wedge d x ^ { 2 } \wedge d x ^ { 3 } = d ^ { 3 } \varSigma _ { 0 } . \qquad $

Nothing is more central to the analysis of curvature than the formula (15.16). It starts with an element of 3-volume and ends up giving the moment of rotation in that 3-volume.The tensor that connects the starting volume with the final moment, the “contracted double-dual” of Riemann, is so important that it deserves and receives a name of its own, $\pmb { G } \equiv$ Einstein; thus

$$
( \mathrm { E i n s t e i n } ) ^ { \sigma \tau } \equiv G ^ { \sigma \tau } = { \mathcal { G } } _ { \nu } ^ { \ \sigma \nu \tau } = ( { ^ * R ^ { * } } ) _ { \nu } ^ { \ \sigma \nu \tau } .
$$

This tensor received attention in $\ S \ S 1 3 . 5$ and l4.2,and also in the examples at the

end of Chapter l4. In terms of Einstein, the connection between element of 3-volume and “vector-valued moment of rotation” is

$$
\binom { \mathrm { m o m e n t } } { \mathrm { o f ~ r o t a t i o n } } = \star ( d \mathcal { P } \wedge \mathcal { R } ) = e _ { \sigma } G ^ { \sigma \tau } d ^ { 3 } \varSigma _ { \tau } .
$$

The amount of “vector-valued moment of rotation” contained in the element of 3-volume $d ^ { 3 } \pmb { \Sigma } _ { \mu }$ is identified by general relativity with the amount of energy-momentum contained in that 3-volume.However, defer this identification for now. Concentrate instead on the conservation properties of this moment of rotation. See them once in the formulation of integral calculus, as a consequence of the principle ${ } ^ { 6 6 } \partial \partial \equiv 0$ ." See them then a second time,in differential formulation,as a consequence of $\mathbf { \hat { \Sigma } } ^ { * } \mathbf { \Sigma } \mathbf { \hat { d } } \mathbf { d } \equiv 0$ ”

# S15.5. CONSERVATION OF MOMENT OF ROTATION SEEN FROM "BOUNDARY OF A BOUNDARY IS ZERO"

The moment of rotation defines an automatically conserved quantity.In other words, the value of the moment of rotation for an elementary 3-volume $\ 4 x \ 4 y \ : \Delta z$ after the lapse of a time $\pmb { \varDelta t }$ is equal to the value of the moment of rotation for the same 3-volume at the beginning of that time, corrected by the inflow of moment of rotation over the six faces of the 3-volume in that time interval (quantities proportional to $\Delta y \Delta z \Delta t$ , etc.） Now verify this conservation of moment of rotation in the language of "the boundary of a boundary."Follow the pattern of equation (l5.8), but translate the words into formulas, item by item. Evaluate the amount of moment of rotation created in the elementary 4-cube $\pmb { \mathcal { Q } }$ ,and find

Conservation of net moment of rotation:

(1） derived from $\because \partial \partial = 0 ^ { \prime \prime }$

$$
\mathrm { } ^ { \ast } \mathrm { c r e a t i o n } ^ { \prime \prime } \equiv \int \left( \begin{array} { l } { { \mathrm { } ^ { \ast \ast } \mathrm { c r e a t i o n ~ o f ~ m o m e n t ~ o f ~ \ast ~ } } } \\ { { \mathrm { } \mathrm { r o t a t i o n } ^ { \prime \prime } \mathrm { ~ i n ~ t h e ~ e l e m e n t a r y } } } \\ { { \mathrm { } 4 \mathrm { - c u b e ~ o f ~ s p a c e t i m e ~ } \varOmega } } \end{array} \right) \equiv \int _ { \varOmega } d ^ { \ast } G ;
$$

$$
\int _ { \Omega } d ^ { * } G = \int _ { \Omega } { } ^ { * } G = \int _ { \Omega } { } ^ { * } G = \int _ { \Omega } { } ^ { * } G ( d \varphi ^ { \mathcal { P } } \wedge \mathcal { R } ) = \sum _ { \mathbf { \Omega } _ { \beta } ^ { * } \in \mathbb { N } ^ { 6 } \Omega \cap \mathbb { R } ^ { 6 } } \star \left( \int _ { \mathbf { \Omega } _ { 3 - \mathrm { c u b e } } ^ { * } ( d \varepsilon ^ { \mathcal { P } } } ^ { \mathrm { m o m e n t ~ o f ~ r o t a t i o n } } \right) = \int _ { \mathbf { \Omega } _ { 3 - \mathrm { c u b e } } ^ { * } ( d \varepsilon ^ { \mathcal { P } } ) \wedge \mathbf { \Omega } _ { \beta } ^ { * } } ^ { \mathbf { m o m e n t } ( d \omega ) } \left( \begin{array} { l } { h \to \omega \mathrm { m i t } } \\ { h \to \omega \mathrm { m i t } } \\ { h \to \omega \mathrm { m i t } } \\ { s \mathrm { p e c i f i e d } 3 - \omega \mathrm { t e p } } \end{array} \right)  ; \qquad \mathrm { s t e p } \qquad \left| { \begin{array} { l } { h \to \omega \mathrm { m i t } } \\ { h \to \omega \mathrm { m i t } } \\ { h \to \omega \mathrm { m i t } } \\ { s \mathrm { t e p } 3 } \end{array} } \right| = \left| { \begin{array} { l } { h \to \omega \mathbf { \Omega } _ { \beta } } \\ { h \to \omega \mathrm { m i t } } \\ { h \to \omega \mathrm { m i t } } \\ { s \mathrm { t e p } 4 } \end{array} } \right| = 0 ,
$$

$$
\Bigg ) \equiv 0 . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg \quad . \Bigg . \Bigg . \Bigg . \Bigg . \Bigg \downarrow \Bigg . \Bigg . \Bigg . \Bigg . \Bigg \downarrow \Bigg . \Bigg . \Bigg . \Bigg . \Bigg \downarrow \Bigg . \Bigg . \Bigg . \Bigg \downarrow \Bigg . \Bigg . \Bigg . \Bigg \downarrow \Bigg . \Bigg . \Bigg . \Bigg \downarrow \Bigg . \Bigg . \Bigg \downarrow \Bigg . \Bigg . \Bigg . \Bigg \downarrow \Bigg . \Bigg . \Bigg \downarrow \Bigg . \Bigg . \Bigg \downarrow \Bigg . \Bigg . \Bigg \downarrow \Bigg . \Bigg . \Bigg \downarrow \Bigg . \Bigg . \Bigg \downarrow \Bigg . \Bigg . \Bigg \Bigg . \Bigg \downarrow \Bigg . \Bigg \downarrow \Bigg .
$$

Here step l is the theorem of Stokes.Step 2 is the identification established by(l5.19) between the Einstein tensor and the moment of rotation. Step 3 breaks down the integral over the entire boundary $\partial \Omega$ into integrals over the individual 3-cubes that constitute this boundary. Moreover,in all these integrals, the star $\star$ is treated as a constant and taken outside the sign of integration. The reason for such treatment is simple: the duality operation $\star$ involves only the metric,and the metric is locally constant throughout the infinitesimal 4-cube over the boundary of which the integration extends.Step 4 uses the formula

$$
d ( \mathscr { s } ^ { \flat } \wedge \mathscr { s } \mathscr { k } ) = d \mathscr { s } ^ { \flat } \wedge \mathscr { s } \mathscr { k } + \mathscr { s } ^ { \flat } \wedge d \mathscr { R } = d \mathscr { s } ^ { \flat } \wedge \mathscr { R }
$$

and the theorem of Stokes to express each 3-cube integral as an integral of $\mathcal { P } \wedge \mathcal { R }$ over the two-dimensional boundary of that cube.The culminating step is 5. It has nothing to do with the integrand. It depends solely on the principle $\partial \partial \equiv 0$

In brief, the conservation of moment of rotation follows from two circumstances. (l)The moment of rotation associated with any elementary 3-cube is by definition a net value, obtained by adding the six moments of rotation associated with the six faces of that cube. (2) When one sums these net values for all eight 3-cubes in (l5.20),which are the boundary of the elementary 4-cube $\pmb { \mathcal { Q } }$ ，one counts the contribution of a given 2-face twice,once with one sign and once with the opposite sign.In virtue of the principle that “the boundary of a boundary is zero,” the conservation of moment of rotation is thus an identity.

# $\$ 15.6$ .CONSERVATION OF MOMENT OF ROTATION EXPRESSED IN DIFFERENTIAL FORM

Every conservation law stated in integral form lends itself to restatement in differential form,and conservation of moment of rotation is no exception. The calculation is brief.Evaluate the generalized exterior derivative of the moment of rotation in three steps,and find that it vanishes; thus:

$$
\begin{array} { r l } & { d ^ { * } G = d [ \star ( d \mathcal { P } \wedge \mathcal { R } ) ] } \\ & { \qquad = \star [ d ( d \mathcal { P } \wedge \mathcal { R } ) ] } \\ & { \qquad = \star [ d ^ { 2 } \mathcal { P } \wedge \mathcal { R } - d \mathcal { P } \wedge d \mathcal { R } ] \left\{ \begin{array} { l l } { \mathrm { s t e p ~ 1 } } \\ { \mathrm { s t e p ~ 2 } } \end{array} \right. } \\ & { \qquad = 0 } \end{array}
$$

Step l uses the relation $d \star = \star d .$ The star duality and the generalized exterior derivative commute because when $\pmb { d }$ is applied to a contravariant vector, it acts as a covariant derivative,and when $\star$ is applied to a covariant vector or l-form,it is without effect. Step 2 applies the standard rule for the action of $\pmb { d }$ on a product of tensor-valued forms [see equation (l4.13b)]. Step 3 deals with two terms.The first term vanishes because the first factor in it vanishes; thus, $\pmb { d } ^ { 2 \mathcal { O } } = 0$ [Cartan's equation of structure;expresses the“vanishing torsion”of the covariant derivative; see equation (l4.26)]. The second term also vanishes, in this case, because the second factor in it vanishes; thus, $\mathbf { d } \mathcal { R } = 0$ (the full Bianchi identity).Thus briefly is conservation of moment of rotation established.

Box 15.2 THE SOURCE OF GRAVITATION AND THE MOMENT OF ROTATION: THE TWO KEY QUANTITIES AND THE MOST USEFUL MATHEMATICA REPRESENTATIONS FOR THEM   

<table><tr><td colspan="3">REPRESENTATIONSFORTHEM</td></tr><tr><td></td><td>Energy-momentum as source of gravitation (curvature of space- time)</td><td>Moment of rotation as automati- cally conserved feature of the geometry</td></tr><tr><td>Representation as a vector-valued 3-form,a coordinate-independent geometric object</td><td>Machine to tell how much energy- momentum is contained in an elementary 3-volume: *T = e,ToT d3∑, (&quot;dual of stress-energy tensor&quot;)</td><td>Machine to tell how much net moment of rotation-expressed as a vector-is obtained by add- ing the six moments of rotation associated with the six faces of the elementary 3-cube: ★（dP△）=*G=eGd∑, (&quot;dual of Einstein&quot;)</td></tr><tr><td>Representation as a()-tensor (alsoa coordinate independent geometric object)</td><td>Stress-energy tensor itself: T = eToe,</td><td>Einstein itself: G = eGoe.</td></tr><tr><td>Representation in language of components (values depend on choice of coordinate system)</td><td>T07</td><td>G</td></tr><tr><td>Conservation law in language of components</td><td>ToT., = 0</td><td>GoT.,=0</td></tr><tr><td>Conservation in abstract lan- guage.for the()-tensor</td><td>v·T=0</td><td>V·G=0</td></tr><tr><td>Conservation in abstract lan- guage,as translated into exterior derivative of the dual tensor (vec- tor-valued 3-form)</td><td>d*T = 0</td><td>d*G=0or d（d&gt;）三0</td></tr><tr><td>Same conservation law expressed in integral form for an element of 4-volume Ω</td><td>T *T=0 Ja</td><td>*G=00r ， a *f(dp&gt;）=0or an ★ （9&gt;）=0 aan</td></tr></table>

# $\$ 15.7$ .FROM CONSERVATION OF MOMENT OF ROTATION TO EINSTEIN'S GEOMETRODYNAMICS: A PREVIEW

Mass,or mass-energy, is the source of gravitation. Mass-energy is one component of the energy-momentum 4-vector. Energy and momentum are conserved.The amount of energy-momentum in the element of 3-volume $d ^ { 3 } \pmb { \Sigma }$ is

Einstein field equation "derived" from demand that (conservation of net moment of rotation) $\Longrightarrow$ (conservation of source)

$$
{ ^ { * } } \pmb { \tau } = \pmb { e } _ { \sigma } T ^ { \sigma \tau } d ^ { 3 } \pmb { \Sigma } _ { \tau }
$$

(see Box 15.2). Conservation of energy-momentum for an elementary 4-cube $\pmb { \mathcal { Q } }$ expresses itself in the form

$$
\int _ { \partial \Omega } \ast \pmb { \tau } = 0 .
$$

This conservation is not an accident. According to Einstein and Cartan, it is “automatic";and automatic, moreover, as a consequence of exact equality between energy-momentum and an automatically conserved feature of the geometry. What is this feature? It is the moment of rotation,which satisfes the law of automatic conservation,

$$
\int _ { \partial \Omega } \ast \pmb { G } = 0 .
$$

In other words, the conservation of momentum-energy is to be made geometric in character and automatic in action by the following prescription: Identify the stressenergy tensor (up to a factor ${ 8 \pi } .$ or $8 \pi G / c ^ { 4 }$ ,or other factor that depends on choice of units) with the moment of rotation; thus,

$$
{ } ^ { \star } ( d ^ { \varrho } \wedge { \mathcal { R } } ) = { } ^ { \ast } G = 8 \pi ^ { \ast } T ;
$$

or equivalently (stillin the language of vector-valued 3-forms)

$$
{ \binom { \mathrm { m o m e n t ~ o f } } { \mathrm { r o t a t i o n } } } = \star ( d ^ { \mathcal { P } } \wedge \mathscr { R } ) = e _ { \sigma } G ^ { \sigma \tau } d ^ { 3 } \Sigma _ { \tau } = 8 \pi e _ { \sigma } T ^ { \sigma \tau } d ^ { 3 } \Sigma _ { \tau } ;
$$

Or, in the language of tensors,

$$
{ \pmb G } = { \pmb e } _ { \sigma } G ^ { \sigma \tau } { \pmb e } _ { \tau } = 8 \pi { \pmb e } _ { \sigma } T ^ { \sigma \tau } { \pmb e } _ { \tau } = 8 \pi { \pmb T } ;
$$

or, in the language of components,

$$
G ^ { \sigma \tau } = 8 \pi T ^ { \sigma \tau }
$$

(Einstein's field equation; more detail,and more on the question of uniqueness, wili be found in Chapter 17; see also Box 15.3). Thus simply is all of general relativity tied to the principle that the boundary of a boundary is zero. No one has ever discovered a more compelling foundation for the principle of conservation of momentum and energy. No one has ever seen more deeply into that action of matter on space,and space on matter, which one calls gravitation.

In summary,the Einstein theory realizes the conservation of energy-momentum as the identity,“the boundary of a boundary is zero.”

# EXERCISES

# ExerciSe 15.1. THE BOUNDARY OF THE BOUNDARY OF A 4-SIMPLEX

In the analysis of the development in time of a geometry lacking all symmetry, when one is compelled to resort to a computer,one can, as one option, break up the 4-geometry into simplexes [four-dimensional analog of two-dimensional triangle, three-dimensional tetrahedron;vertices of“central simplex”conveniently considered to be at $( t , x , y , z ) = ( 0 , 1 , 1 , 1 ) ;$ $( 0 , 1 , - 1 , - 1 )$ ， $( 0 , - 1 , 1 , - 1 )$ ， $( 0 , - 1 , - 1 , 1 )$ ， $( 5 ^ { 1 / 2 } , 0 , 0 , 0 )$ , for example], suffciently numerous,and each sufficiently small, that the geometry inside each can be idealized as flat (Lorentzian), with all the curvature concentrated at the join between simplices (see discussion of dynamics of geometry via Regge calculus in Chapter 42). Determine ("give a mathematical

# Box 15.3 OTHER IDENTITIES SATISFIED BY THE CURVATURE

(l) The source of gravitation is energy-momentum. (2)Energy-momentum is expressed by stressenergy tensor (or by its dual) as a vector-valued 3-form ("energy-momentum per unit 3-volume"). (3)This source is conserved (no creation in an elementary spacetime 4-cube).

These principles form the background for the probein this chapter of the Bianchi identities.That is why two otherwise most interesting identities [Allendoerfer and Weil (1943); Chern (1955,1962)] are dropped from attention. One deals with the 4-form

spacetime geometry interior to that surface (provided that these changes neither abandon the continuity nor change the connectivity of the 4-geometry in that region). Property (l） kils any possibility of identifying the integral,a scalar, with energy-momentum,a 4-vector. Property (2） kils it for the purpose of a conservation law, because it implies a non-zero creation in $\pmb { \mathcal { a } }$

Also omitted here is the Bel-Robinson tensor (see exercise l5.2), built bilinearly out of the curvature tensor, and other tensors for which see, e.g., Synge (1962).

$$
\Pi = \frac { 1 } { 2 4 \pi ^ { 2 } } g ^ { \alpha \gamma } g ^ { \beta \delta } \mathcal { R } _ { \alpha \beta } \wedge \mathcal { R } _ { \gamma \delta } ,
$$

and the other with the 4-form

$$
\begin{array} { r l r } & { } & { = \frac { 1 } { 8 \pi ^ { 2 } | \operatorname* { d e t } g _ { \mu \nu } | ^ { 1 / 2 } } ( \mathcal { R } _ { 1 2 } \wedge \mathcal { R } _ { 3 0 } + \mathcal { R } _ { 1 3 } \wedge \mathcal { R } _ { 0 2 } } \\ & { } & { \qquad \quad + \mathcal { R } _ { 1 0 } \wedge \mathcal { R } _ { 2 3 } ) . } \end{array}
$$

One or all of these quantities may be found someday to have important physical content.

The integral of the 4-form $\boldsymbol { r }$ of equation (2) over the entire manifold gives a number,an integer,the so-called Euler-Poincaré characteristic of the manifold,whenever the integral and the integer are well-defined.This result is the four-dimen-sional generalization of the Gauss-Bonnet integral, widely known in the context of two-dimensional geometry:

Both quantities are built from the tensorial “curvature 2-forms"

$$
{ \mathcal R } _ { \alpha \gamma } = \frac { 1 } { 2 } R _ { \alpha \gamma \beta \delta } d x ^ { \beta } \wedge d x ^ { \delta } .
$$

The four-dimensional integral of either quantity over a four-dimensional region $\pmb { \mathcal { a } }$ has a value that (l) is a scalar, (2) is not identically equal to zero, (3) depends on the boundary of the region of spacetime over which the integral is extended, but (4） is independent of any changes made in the

$$
\int \left( \begin{array} { l } { { \mathrm { R i e m a n n i a n ~ s c a l a r ~ c u r v a t u r e } } } \\ { { \mathrm { i n v a r i a n t ~ ( v a l u e ~ } 2 / a ^ { 2 } } } \\ { { \mathrm { f o r ~ a ~ s p h e r e ~ o f ~ r a d i u s ~ } a ) } } \end{array} \right) g ^ { 1 / 2 } d ^ { 2 } x .
$$

This integral has the value ${ 8 \pi }$ for any closed, oriented,two-dimensional manifold with the topology of a 2-sphere,no matter how badly distorted;and the value O for any 2-torus,again no matter how rippled and twisted; and other equally specific values for other topologies.

description of") the boundary (three-dimensional) of such a simplex. Take one piece of this boundary and determine its boundary (two-dimensional).For one piece of this two-dimensional boundary.verify that there is at exactly one other place,and no more,in the bookkeeping on the boundary of a boundary,another two-dimensional piece that cancels it ("facelessness"of the 3-boundary of the simplex).

Exercise 15.2. THE BEL-ROBINSON TENSOR [Bel (1958,1959.1962). Robinson (1959b). Sejnowski (1973): see also Pirani (1957) and Lichnerowicz (1962)].

Define the Bel-Robinson tensor by

$$
T _ { \alpha \beta \gamma \delta } = R _ { \alpha \rho \gamma \sigma } R _ { \beta } { } ^ { \rho } { } _ { \delta } { } ^ { \sigma } + { } ^ { * } R _ { \alpha \rho \gamma \sigma } { } ^ { * } R _ { \beta } { } ^ { \rho } { } _ { \delta } { } ^ { \sigma } .
$$

Show that in empty spacetime this tensor can be rewritten as

$$
T _ { \alpha \beta \gamma \delta } = R _ { \alpha \rho \gamma \sigma } R _ { \beta } { } ^ { \rho } { } _ { \delta } { } ^ { \sigma } + R _ { \alpha \rho \delta \sigma } R _ { \beta } { } ^ { \rho } { } _ { \gamma } { } ^ { \sigma } - \frac { 1 } { 8 } g _ { \alpha \beta } g _ { \gamma \delta } R _ { \rho \sigma \lambda \mu } R ^ { \rho \sigma \lambda \mu } .
$$

Show also that in empty spacetime

$$
T ^ { \alpha } { } _ { \beta \gamma \delta : \alpha } = 0 ,
$$

$T _ { \alpha \beta \gamma \delta }$ is symmetric and traceless on all pairs of indices.

Discussion: It turns out that Einstein's "canonical energy-momentum pseudotensor" $( \ S 2 0 . 3 )$ for the gravitational field in empty spacetime has a second derivative which,in a Riemannnormal coordinate system,is

$$
t _ { { \tt E } \alpha \beta , \gamma \delta } = - \frac { 4 } { 9 } \Big ( T _ { \alpha \beta \gamma \delta } - \frac { 1 } { 4 } S _ { \alpha \beta \gamma \delta } \Big ) .
$$

Here $T _ { \alpha \beta \gamma \delta }$ is the completely symmetric Bel-Robinson tensor, and $S _ { \alpha \beta \gamma \delta }$ is defined by

$$
S _ { \alpha \beta \gamma \delta } \equiv R _ { \alpha \delta \rho \sigma } R _ { \beta \gamma } { } ^ { \rho \sigma } + R _ { \alpha \gamma \rho \sigma } R _ { \beta \delta } { } ^ { \rho \sigma } + \frac { 1 } { 4 } g _ { \alpha \beta } g _ { \gamma \delta } R _ { \mu \nu \rho \sigma } R ^ { \mu \nu \rho \sigma } .
$$

$S _ { \alpha \beta \gamma \delta }$ appears in the empty-space covariant wave equation

$$
\begin{array} { r } { { A } R _ { \alpha \beta \gamma \delta } \equiv - R _ { \alpha \beta \gamma \delta ; \mu } { } ^ { ; \mu } + R _ { \alpha \beta \rho \sigma } R _ { \gamma \delta } { } ^ { \rho \sigma } + 2 ( R _ { \alpha \rho \gamma \sigma } R _ { \beta } { } ^ { \rho } { } _ { \delta } { } ^ { \sigma } - R _ { \alpha \rho \delta \sigma } R _ { \beta } { } ^ { \rho } { } _ { \gamma } { } ^ { \sigma } ) = 0 , } \end{array}
$$

where $\pmb { \varDelta }$ is a variant of the Lichnerowicz-de Rham wave operator [Lichnerowicz (1964)], when one rewrites this wave equation as

$$
\Pi { R _ { \alpha \beta } } ^ { \gamma \delta } \equiv R _ { \alpha \beta } { } ^ { \gamma \delta } { } _ { ; \mu } { } ^ { ; \mu } = 2 S _ { [ \alpha } { } ^ { \{ \gamma } _ { \beta ] } { } ^ { \delta ] }  .
$$

# PART IV

# EINSTEIN'S GEOMETRIC THEORY OF GRAVITY

Wherein the reader is seduced into marriage with the most elegant temptress of all-Geometrodynamics--and learns from her the magic potions and incantations that control the universe.
