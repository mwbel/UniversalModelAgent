# CHAPTER 9

# DIFFERENTIAL TOPOLOGY

In analytic geometry,many relations which are independent of any frame must be expressed with respect to some particular frame.It is therefore preferable to devise new methods  
methods which lead directly to intrinsic properties without any mention of coordinates. The development of the topology of   
general spaces and of the objects which occur in them,as well as the development of the geometry of general metric spaces, are steps in this direction.

KARL MENGER，in Schilpp (1949)，p. 467.

# $\$ 9.1$ .GEOMETRIC OBJECTS IN METRIC-FREE, GEODESIC-FREE SPACETIME

Curved spacetime without metric or geodesics or parallel transport, i.e.,“differential topology,” is the subject of this easy chapter. It is easy because all the necessary geometric objects (event, curve,vector, l-form, tensor) are already familiar from flat spacetime. Yet it is also necessary, because one's viewpoint must be refined when one abandons the Lorentz metric of flat spacetime.

# Events

The primitive concept of an event $\mathscr { P }$ (Figure 1.2) needs no refinement. The essential property here is identifiability,which is not dependent on the Lorentz metric structure of spacetime.

This chapter is entirely Track 2. It depends on no preceding   
Track-2 material. It is needed as preparation   
for (1） Chapters 10-13 (differential geometry; Newtonian gravity). and (2) Box 30.1 (mixmaster cosmology). It will be helpful in (1）Chapter 14 (calculation of curvature) and in (2)Chapter 15(Bianchi identities).

Metric is abandoned

Geometric concepts must be refined

# Curves

Again no refinement.A“curve” $\mathcal { S } ( \lambda )$ is also too primitive to care whether spacetime has a metric-except that, with metric gone, there is no concept of “proper length" along the curve. This is in accord with Newton's theory of gravity,where one talks of the lengths of curves in “space,” but never in “spacetime."

# Vectors

Here refinement is needed.In special relativity one could dress primitive ("identifiable")events in enough algebraic plumage to talk of vectors as differences $\mathcal { P } - \mathcal { Q }$ between“algebraic” events. Now the plumage is gone,and the old bilocal("point for head and point for tail") version of a vector must be replaced by a purely local version $( \ S 9 . 2 )$ . Also vectors cannot be moved around; each vector must be attached to a specific event $\mathfrak { S 8 9 . 2 }$ and 9.3).

# 1-Forms

Almost no refinement needed, except that, with metric gone,there is no way to tell which l-form corresponds to a given vector (no way to raise and lower indices), and each 1-form must be atached to a specific event (89.4).

# Tensors

Again almost no refinement, except that each slot of a tensor is specific: if it accepts vectors, then it cannot accommodate l-forms,and conversely (no raising and lowering of indices); also, each tensor must be attached to a specific event (89.5).

# $\$ 9.2$ ."VECTOR" AND "DIRECTIONAL DERIVATIVE" REFINED INTO TANGENT VECTOR

Flat spacetime can accommodate several equivalent definitions of a vector (S2.3): a vector is an arrow reaching from an event $\mathcal { P } _ { 0 }$ to an event $\mathcal { Q } _ { 0 } ;$ it is the parameterized straight line, $\mathcal { P } ( \lambda ) = \mathcal { P } _ { 0 } + \lambda ( \mathcal { Z } _ { 0 } - \mathcal { P } _ { 0 } )$ extending from $\mathcal { P } _ { 0 }$ at $\lambda = 0$ to $\mathcal { Q } _ { 0 }$ at $\lambda = 1$ ； it is the rate of change of the point $\mathcal { P } ( \lambda )$ with increasing $\lambda .$ $d \mathcal { P } / d \lambda$

Old definitions of vector break down when metric is abandoned

With Lorentz metric gone, the“arrow” definition and the“parametrized-straight line”definition must break down.By what route is the arrow or line to be laid out between $\mathcal { P } _ { 0 }$ and $\boldsymbol { \mathcal { Q } } _ { 0 } \boldsymbol { ? }$ There is no concept of straightness; all routes are equally straight or bent.

Such fuzziness forces one to focus on the “rate-of-change-of-point-along-curve”

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/0e7c4b061b20f8a3b6dd3843bc64d9bfbec44d54539f0b136d47403bc099deb6.jpg)  
Box 9.1 TANGENT VECTORS AND TANGENT SPACE

A tangent vector $d \mathcal { P } / d \lambda$ is defined to be “the limit, when $N \longrightarrow \infty$ ，of $N$ times the displacement of $\mathcal { S }$ as $\lambda$ ranges from O to $1 / N$ ”One cannot think of this final displacement $d \mathcal { P } / d \lambda$ as lying in spacetime; fuzziness forbids (no concept of straightness). Instead,one visualizes $d \mathcal { P } / d \lambda$ as lying in a“tangent plane”or “tangent space,”which makes contact with spacetime only at ${ \mathcal { P } } ( 0 )$ ,the event where $d \mathcal { P } / d \lambda$ is evaluated. All other tangent vectors at ${ \mathcal { P } } ( 0 ) { - } \mathrm { e . g . } , d { \mathcal { P } } / d \rho , d { \mathcal { P } } / d \eta , d { \mathcal { P } } / d \xi .$ -lie in this same tangent space.

To make precise these concepts of tangent space and tangent vector,-one may regard spacetime as embedded in a flat space of more than four dimensions. One can then perform the limiting process that leads to $d \mathcal { P } / d \lambda ,$ ,using straight arrows in the flat embedding space.The result is a higherdimensional analog of the figure shown above.

But such a treatment is dangerous. It suggests, falsely，that the tangent vector $d \mathcal { P } / d \lambda$ and the tangent space at $\mathcal { P } _ { 0 }$ depend on how the embedding is done,or depend for their existence on the embedding process. They do not. And to make clear that they do not is one motivation for defining the directional derivative operator $" d / d \lambda "$ to be the tangent vector, rather than using Cartan's more pictorial concept $" d \mathcal { P } / d \lambda "$ 、

definition, $d \mathcal { P } / d \lambda$ . It, under the new name“tangent vector,”is explored briefly in $\ B \circ \mathbf { x } \ 9 . 1$ ,and in greater depth in the following paragraphs.

Even $" d \varphi / d \lambda "$ is a fuzzy definition of tangent vector, most mathematicians would argue.More acceptable,they suggest, is this definition: the tangent vector u to $\pmb { a }$ curve $\mathcal { P } ( \lambda )$ is the directional derivative operator along that curve

$$
\pmb { \upsilon } = \partial _ { \pmb { u } } = ( d / d \lambda ) _ { \mathrm { a l o n g c u r v e } } ,
$$

Best new definition:"'tangent vector equals directional derivative operator" $\pmb { u } = \pmb { d } / d \lambda$

Tangent vector equals directional derivative operator? Preposterous! A vector started out as a happy, irresponsible trip from $\mathcal { P } _ { 0 }$ to ${ \mathcal { Q } } _ { 0 }$ It ended up loaded with the social responsibility to tell how something else changes at $\mathcal { P } _ { 0 }$ At what point did the vector get saddled with this unexpected load? And did it really change its character all that much,as it seems to have done? For an answer, go back and try

Alternative definition, $\pmb { \upsilon } = d \hat { \mathscr { P } } / d \lambda$ ，requires embedding in flat space of higher dimensionality

to redo the “rate-of-change-of-point” definition, $d \mathcal { P } / d \lambda$ ,in the form of a limiting process:

0.Choose a curve $\mathcal { P } ( \lambda )$ whose tangent vector $d \mathscr { s p } / d \lambda$ at $\lambda = 0$ is desired. 1. Take the displacement of $\mathcal { P }$ as $\lambda$ ranges from O to l; that is not $d \mathscr { o } ^ { \flat } / d \lambda$ 、 2.Take twice the displacement of $\mathcal { S }$ as $\lambda$ ranges from 0 to $\scriptstyle { \frac { 1 } { 2 } } ;$ that is not $d ^ { \boldsymbol { o } \vec { p } } / d \lambda$ $N _ { \ast }$ Take $N$ times the displacement of $\mathscr { P }$ as $\lambda$ ranges from O to $1 / N ;$ that is not $d { \mathcal { P } } / d \lambda .$ $\infty$ . Take the limit of such displacements as $N \longrightarrow \infty$ ; that is $d ^ { \omega } / d \lambda$ 、

This definition has the virtue that $d \mathcal { P } / d \lambda$ describes the properties of the curve $\mathcal { P } ( \lambda )$ ， not over the huge range from $\lambda = 0$ to $\lambda = 1$ ,where the curve might be doing wild things,but only in an infinitesimal neighborhood of the point $\mathcal { P } _ { 0 } = \mathcal { P } ( 0 )$

The deficiency in this definition is that no meaning is assigned to steps $1 , 2 , \ldots$ $N , \ldots$ ， so there is nothing, yet, to take the limit of.To make each “displacement of ${ \mathcal { P } } ^ { * }$ a definite mathematical object in a space where “limit” has a meaning, one can imagine the original manifold to be a low-dimensional surface in some much higher-dimensional flat space.Then $\mathcal { P } ( 1 / N ) - \mathcal { P } ( 0 )$ is just a straight arrow connecting two points, i.e. a segment of a straight line,which,in general,will not lie in the surface itself-see Box 9.1.The resulting mental picture of a tangent vector makes its essential properties beautifully clear,but at the cost of some artifacts. The picture relies on a specific but arbitrary way of embedding the manifold of interest (metricfree spacetime) in an extraneous flat space.In using this picture,one must ignore everything that depends on the peculiarities of the embedding. One must think like the chemist, who uses tinkertoy molecular models to visualize many essential properties of a molecule clearly,but easily ignores artifacts of the model (colors of the atoms,diameters of the pegs, its tendency to collapse) that do not mimic quantummechanical reality.

Elie Cartan's approach to diferential geometry, including the $d \mathcal { P } / d \lambda$ idea of a tangent vector, suggests that he always thought of manifolds as embedded in flat spaces this way,and relied on insights that he did not always formalize to separate the essential geometry of these pictures from their embedding-dependent details. Acceptance of his methods of calculation came late.Mathematicians, who mistrusted their own ability to distinguish fact from artifact, exacted this price for acceptance: stop talking about the movement of the point itself,and start dealing only with concrete measurable changes that take place within the manifold, changes in any or all scalar functions $f$ as the point moves. The limiting process then reads:

0. Choose a curve $\mathcal { P } ( \lambda )$ whose tangent vector at $\lambda = 0$ is desired.   
1. Compute the number $f [ \mathcal { P } ( 1 ) ] - f [ \mathcal { P } ( 0 ) ] ,$ . which measures the change in $f$ as the point $\mathcal { P } ( \lambda )$ moves from $\mathcal { P } _ { 0 } = \mathcal { P } ( 0 )$ to $\mathcal { Q } _ { 0 } = \mathcal { P } ( 1 )$   
2. Compute $2 \{ f [ \mathcal { P } ( \vec { \mathfrak { g } } ) ] - f [ \mathcal { P } ( 0 ) ] \}$ , which is twice the change in $f$ as the point goes from ${ \mathcal { P } } ( 0 )$ to $\mathcal { P } ( \scriptstyle { \frac { 1 } { 2 } } )$   
N. Compute $N \{ f [ \mathcal { P } ( 1 / N ) ] - f [ \mathcal { P } ( 0 ) ] \}$ ，which is $N$ times the change in $f$ as the point goes from $\mathcal { P } ( 0 )$ to $\mathcal { P } ( 1 / N )$

$\infty$ 、 Same in the limit as $N \longrightarrow \infty$ : (change in $f ) = d f / d \lambda$

O. The vector is not itself the change in $f .$ It is instead the operation $d / d \lambda$ ,which, when applied to $f ,$ gives the change $d f / d \lambda$ Thus

$$
\mathsf { t a n g e n t \ v e c t o r = } d / d \lambda
$$

[cf. definition (9.1)].

The operation $d / d \lambda$ clearly involves nothing but the last steps $N \longrightarrow \infty$ in this limiting process, and only those aspects of these steps that are independent of $f .$ But this means it involves the infinitesimal displacements of the point $\mathcal { P }$ and nothing more.

One who wishes both to stay in touch with the present and to not abandon Cartan's deep geometric insight $( \mathbf { B o x } \ 9 . 1 )$ can seek to keep alive a distinction between:

(A） the tangent vector itself in the sense of Cartan, the displacement $d \mathcal { P } / d \lambda$ of a point;and   
(B) the “tangent vector operator,” or “directional derivative operator,” telling what happens to a function in this displacement: (tangent vector operator) $= d / d \lambda$

However,present practice drops (or, if one will,“slurs") the word“operator” in (B), and uses the phrase “tangent vector” itself for the operator,as will be the practice here from now on. The ideas (A) and (B) should also slur or coalesce in one's mind, so that when one visualizes an embedding diagram with arrows drawn tangent to the surface, one always realizes that the arrow characterizes an infinitesimal motion of a point $d \mathcal { P } / d \lambda$ that takes place purely within the surface,and when one thinks of a derivative operator $d / d \lambda$ , one always visualizes this same infinitesimal motion of a point in the manifold,a motion that must occur in constructing any derivative $d f ( \mathcal { P } ) / d \lambda$ 、 In this sense,one should regard a vector $d \mathcal { P } / d \lambda \equiv d / d \lambda$ as both“a displacement that carries attention from one point to another” and“a purely geometric object built on points and nothing but points.”

The hard-nosed physicist may still be inclined to say “Tangent vector equals directional derivative operator? Preposterous!” Perhaps he will be put at ease by another argument. He is asked to pick an event ${ \mathcal { P } } _ { 0 }$ 、At that event he chooses any set of four noncoplanar vectors (vectors defined in whatever way seems reasonable to him)；he names them $\pmb { e } _ { 0 } , \pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ ；and he uses them as a basis on which to expand all other vectors at $\mathcal { P } _ { 0 }$ ：

$$
u = u ^ { \alpha } e _ { \alpha } , \qquad v = v ^ { \alpha } e _ { \alpha } .
$$

He is asked to construct the four directional derivative operators $\partial _ { \alpha } \equiv \partial _ { \pmb { \alpha } _ { r } }$ along his four basis vectors.As in flat spacetime, so also here; the same expansion coeffcients that appear in $\pmb { u } = \pmb { u } ^ { \alpha } \pmb { \mathcal { e } } _ { \alpha }$ also appear in the expansion for the directional derivative:

lsomorphism between directional derivatives and vectors

$$
\partial _ { \pmb { \omega } } = u ^ { \pmb { \alpha } } \partial _ { \alpha } , \partial _ { \pmb { \nu } } = v ^ { \pmb { \alpha } } \partial _ { \alpha } ,
$$

Hence,every relation between specific vectors at ${ \mathcal { P } } _ { 0 }$ induces an identical relation between their differential operators:

$$
\begin{array} { c } { { \pmb u = a \pmb w + b \pmb v \Longleftrightarrow u ^ { \alpha } = a w ^ { \alpha } + b v ^ { \alpha } } } \\ { { \Longleftrightarrow \partial _ { \pmb u } = a \partial _ { \pmb w } + b \partial _ { \pmb v } . } } \end{array}
$$

Tangent space defined

There is a complete “isomorphism” between the vectors and the corresponding directional derivatives. So how can the hard-nosed physicist deny the hard-nosed mathematician the right to identify completely each tangent vector with its directional derivative? No harm is done; no answer to any computation can be affected.

This isomorphism extends to the concept “tangent space."Because linear relations (such as $\hat { \partial } _ { \pmb { u } } = a \hat { \partial } _ { \pmb { w } } + b \hat { \partial } _ { \pmb { v } } )$ among directional derivatives evaluated at one and the same point ${ \mathcal { P } } _ { 0 }$ are meaningful and obey the usual addition and multiplication rules, these derivative operators form an abstract (but finite-dimensional) vector space called the tangent space at $\mathcal { P } _ { 0 }$ 、In an embedding picture (Box 9.1).one uses these derivatives (as operators in the flat embedding space) to construct tangent vectors $\pmb { u } = \hat { o } _ { \pmb { u } ^ { \pmb { \imath } } } s ^ { \ p }$ ， $\pmb { v } = \hat { \partial } _ { \pmb { v } } \mathcal { s } ^ { \dagger }$ ,in the form of straight arrows. Thereby one identifies the abstract tangent space with the geometrically visualized tangent space.

Coordinate-induced basis defined

# $\$ 9.3$ .BASES,COMPONENTS,AND TRANSFORMATION LAWS FOR VECTORS

An especially useful basis in the tangent space at an event $\mathcal { P } _ { 0 }$ is induced by any coordinate system [four functions, $x ^ { 0 } ( { \mathcal { P } } ) , x ^ { 1 } ( { \mathcal { P } } ) , x ^ { 2 } ( { \mathcal { P } } ) , x ^ { 3 } ( { \mathcal { P } } ) ]$ ：

$$
\begin{array} { r } { \pmb { e _ { 0 } } \equiv \left( \frac { \partial } { \partial x ^ { 0 } } \right) _ { x ^ { 1 } , x ^ { 2 } , x ^ { 3 } } = \left( \overset { \mathrm { d i r e c t i o n a l ~ d e r i v a t i v e ~ a l o n g ~ t h e } } { \mathrm { c u r v e ~ w i t h ~ c o n s t a n t ~ } } ( x ^ { 1 } , x ^ { 2 } , x ^ { 3 } ) \right) _ { \mathrm { a t } \mathcal { P } _ { 0 } } , } \end{array}
$$

$$
{ \pmb e } _ { 1 } = \frac { \hat { \partial } } { \hat { \partial } x ^ { 1 } } , \qquad e _ { 2 } = \frac { \hat { \partial } } { \hat { \partial } x ^ { 2 } } , \qquad e _ { 3 } = \frac { \hat { \partial } } { \hat { \partial } x ^ { 3 } } .
$$

Changes of basis: transformation matrices defined

(See Figure 9.1.)

A transformation from one basis to another in the tangent space at $\mathcal { P } _ { 0 } ,$ , like any change of basis in any vector space, is produced by a nonsingular matrix,

$$
{ \pmb e } _ { \alpha ^ { \prime } } = { \pmb e } _ { \beta } L ^ { \beta } { } _ { \alpha ^ { \prime } } \mathrm { ; }
$$

and,as always (including the Lorentz frames of flat spacetime), the components of a vector must transform by the inverse matrix

$$
u ^ { \alpha ^ { \prime } } = L ^ { \alpha ^ { \prime } } { } _ { \beta } u ^ { \beta } ;
$$

$$
\begin{array} { r } { \vert \vert L ^ { \alpha ^ { \prime } } { } _ { \beta } \vert \vert = \vert \vert L ^ { \beta } \gamma ^ { \vert \vert - 1 } , \mathrm { i . e . , } \left\{ \begin{array} { l l } { L ^ { \alpha ^ { \prime } } { } _ { \beta } L ^ { \beta } { } _ { \gamma } = \delta ^ { \alpha ^ { \prime } } { } _ { \gamma } , } \\ { L ^ { \delta } { } _ { \alpha ^ { \prime } } L ^ { \alpha ^ { \prime } } { } _ { \beta } = \delta ^ { \delta } { } _ { \beta } . } \end{array} \right. } \end{array}
$$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/739f58fe0047b8197dcc869bd9801b1c076d1082ced40a0cb6fb7a6cd37e4a6d.jpg)  
Figure 9.1. The basis vectors induced,by a coordinate system,into the tangent space at each event.Here a truncated, two-dimensional spacetime is shown (two other dimensions suppressed),with coordinates $x ( \mathcal { P } )$ and ${ \dot { \psi } } ( { \mathcal { P } } )$ ，and with corresponding basis vectors $\partial / \partial x$ and $\partial / \partial \psi$

This “inverse” transformation law guarantees Compatibility between the expansions $\pmb { u } = \pmb { e } _ { \alpha ^ { \prime } } \pmb { u } ^ { \alpha ^ { \prime } }$ and $\pmb { \mu } = \pmb { \varrho } _ { \beta } \pmb { u } ^ { \beta }$ ：

$$
\begin{array} { r } { \pmb { u } = \pmb { e } _ { \alpha ^ { \prime } } u ^ { \alpha ^ { \prime } } = ( \pmb { e } _ { \gamma } L ^ { \gamma } { } _ { \alpha ^ { \prime } } ) ( L ^ { \alpha ^ { \prime } } { } _ { \beta } u ^ { \beta } ) = \pmb { e } _ { \gamma } \delta ^ { \gamma } { } _ { \beta } u ^ { \beta } } \\ { = \pmb { e } _ { \beta } u ^ { \beta } . \qquad } \end{array}
$$

In the special case of transformations between coordinate-induced bases, the transformation matrix has a simple form:

so

$$
{ \begin{array} { r } { { \frac { \partial } { \partial x ^ { \alpha ^ { \prime } } } } = { \frac { \partial x ^ { \beta } } { \partial x ^ { \alpha ^ { \prime } } } } { \frac { \partial } { \partial x ^ { \beta } } } ( { \mathrm { b y ~ u s u a l ~ r u l e s ~ o f ~ c a l c u l u s } } ) , } \\ { L ^ { \beta } _ { \alpha ^ { \prime } } = ( { \partial x ^ { \beta } } / { \partial x ^ { \alpha ^ { \prime } } } ) _ { \mathrm { a t e v e n t } { \mathcal { P } } _ { \mathrm { 0 } } { \mathrm { w h e r e } } \mathrm { t a n g e n t s p a c e l i e s } } . } \end{array} }
$$

(Note: this generalizes the Lorentz-transformation law $x ^ { \beta } = A ^ { \beta } { } _ { \alpha ^ { \prime } } x ^ { \alpha ^ { \prime } }$ ,which has the differential form $A ^ { \beta } { } _ { \alpha ^ { \prime } } = \partial x ^ { \beta } / \partial x ^ { \alpha ^ { \prime } }$ ; also,it provides a good way to remember the signs in the $\boldsymbol { A }$ matrices.)

# $\$ 9.4$ .1-FORMS

When the Lorentz metric is removed from spacetime, one must sharpen up the concept of a l-form $\pmb { \sigma }$ by insisting that it, like any tangent vector ${ \pmb u } .$ ，be attached to a specific event $\mathcal { P } _ { 0 }$ in spacetime. The family of surfaces representing $\pmb { \sigma }$ resides in the tangent space at $\mathcal { P } _ { 0 }$ ，not in spacetime itself. The piercing of surfaces of $\pmb { \sigma }$ by an arrow $\pmb { u }$ to produce the number $\langle \pmb { \sigma } , \pmb { u } \rangle$ ("bongs of bell"） occurs entirely in the tangent space.

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/06ff8084a06ccbc909e94440587c1fa25805a1acbfa28f6aef05f4fd79cfb873.jpg)  
Figure 9.2. The basis vectors ${ \pmb \theta } _ { \alpha }$ and dual basis l-forms $\pmb { \omega } ^ { \beta }$ in the tangent space of an event $\mathcal { G } _ { \mathfrak { o } } .$ The condition

$$
\langle { \pmb { \omega } } ^ { \beta } , { \pmb { \sigma } } _ { \alpha } \rangle = \delta _ { \alpha } ^ { \beta }
$$

dictates that the vectors $\pmb { e } _ { 2 }$ and ${ \pmb { \theta } } _ { 3 }$ lie parallel to the surfaces of $\pmb { \omega } ^ { 1 }$ ,and that $\pmb { \theta _ { 1 } }$ extend from one surface of $\pmb { \omega } ^ { 1 }$ to the next (precisely 1.0o surfaces pierced).

Notice that this picture could fit perfectly well into a book on $\mathbf { x }$ -raysand crystallography.There the vectors $\pmb { \theta _ { 1 } }$ ， $\pmb { e } _ { 2 }$ ， ${ \pmb \theta } _ { 3 }$ wouid be the edges of a unit cell of the crystal; and the surfaces of $\omega ^ { 1 } , \omega ^ { 2 }$ ， $\pmb { \omega } ^ { 3 }$ wouid be the surfaces of unit cells.Aiso,for an $\mathbf { x }$ -ray diffraction experiment,with waveiength of radiation and orientation of crystal appropriateiy adjusted, the successve surfaces of $\pmb { \omega } ^ { 1 }$ wouid produce Bragg reflection.For other choices of waveiength and orientation,the surfaces of $\scriptstyle { \pmb { \mu } } ^ { 2 }$ 0r $\pmb { \omega } ^ { 3 }$ wouid produce Bragg reflection.

Given any set of basis vectors $\{ \pmb { e } _ { 0 } , \pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 } \}$ at an event ${ \mathcal { P } } _ { 0 } ,$ one constructs the "dual basis"of 1-forms $\{ { \pmb { \omega } } ^ { 0 } , { \pmb { \omega } } ^ { 1 } , { \pmb { \omega } } ^ { 2 } , { \pmb { \omega } } ^ { 3 } \}$ by choosing the surfaces of $\pmb { \omega } ^ { \beta }$ such that that

$$
\langle { \pmb { \omega } } ^ { \beta } , { \pmb e } _ { \alpha } \rangle = \delta ^ { \beta } { } _ { \alpha } .
$$

See Figure 9.2. A marvelously simple formalism for calculating and manipulating components of tangent vectors and 1-forms then results:

Component-manipulation formulas

$$
\begin{array} { c } { { u = e _ { \alpha } u ^ { \alpha } } } \\ { { \ } } \\ { { \sigma = \sigma _ { \beta } \omega ^ { \beta } } } \\ { { \ } } \\ { { u ^ { \alpha } = \langle { \omega ^ { \alpha } , u } \rangle } } \\ { { \ } } \\ { { \sigma _ { \beta } = \langle { \sigma , e _ { \beta } } \rangle } } \\ { { \ } } \\ { { \mathrm { : } \ u \rangle = \sigma _ { \alpha } u ^ { \alpha } } } \end{array}
$$

$$
\omega ^ { \alpha ^ { \prime } } = L ^ { \alpha ^ { \prime } } { } _ { \beta } \omega ^ { \beta }
$$

$$
\sigma _ { \alpha ^ { \prime } } = \sigma _ { \beta } L ^ { \beta } { } _ { \alpha ^ { \prime } }
$$

(Exercise 9.1 below justifies these equations.)

In the absence of a metric, there is no way to pick a specific 1-form $\widetilde { \pmb { u } }$ at an event $\mathcal { P } _ { 0 }$ and say that it corresponds to a specific tangent vector $\pmb { u }$ at $\mathcal { P } _ { 0 }$ . The correspondence set up in flat spacetime,

Correspondence between vectors and 1-forms rubbed out

$$
\langle \widetilde { \pmb { u } } , \pmb { v } \rangle = \pmb { u } \cdot \pmb { v } \qquad \mathrm { f o r ~ a l l ~ } \pmb { v } ,
$$

was rubbed out when “.” was rubbed out. Restated in component language: the raising of an index, $u ^ { \alpha } = \eta ^ { \alpha \beta } u _ { \beta }$ ,is impossible because the $\eta ^ { \alpha \beta }$ do not exist; similarly, lowering of an index, $u _ { \beta } = \eta _ { \beta \alpha } u ^ { \alpha }$ ,is impossible.

The l-form gradient df was introduced in $\ S 2 . 6$ with absolutely no reference to metric.Consequently,it and its mathematical formalism are the same here,without metric,as there with metric,except that, like all other l-forms, ${ \pmb d } { \pmb f }$ now resides in the tangent space rather than in spacetime itself. For example, there is no change in the fundamental equation relating the projection of the gradient to the directional derivative:

$$
\begin{array} { r } { \langle d f , \pmb { u } \rangle = \partial _ { \pmb { u } } f = \pmb { u } [ f ] . \qquad } \\  \bigg [ \mathrm { o l d ~ n o t a t i o n ~ f o r } \bigg ] \mathscr { \bigg { T } } \begin{array} { r } { \underline { { \operatorname { i } } } _ { \mathrm { r e w ~ n o t a t i o n } ; } } \\ { \underline { { \operatorname { i r e c t i o n } a 1 \mathrm { ~ d e r i v a t i v e } } } \end{array} } \end{array}
$$

Gradient of a function

Similarly,there are no changes in the component equations,

$$
\begin{array} { l l } { d f = f _ { , \alpha } \boldsymbol { \omega } ^ { \alpha } } & { ( \mathrm { e x p a n s i o n ~ o f ~ } d f \mathrm { i n ~ a r b i t r a r y } } \\ & { \mathrm { b a s i s } ) , } \\ { f _ { , \alpha } = \partial _ { \alpha } f = e _ { \alpha } [ f ] } & { ( \mathrm { w a y ~ t o ~ c a l c u l a t e ~ c o m p o n e n t s } } \\ & { \mathrm { o f ~ } d f ) , } \\ { f _ { , \alpha } = \partial f / \partial x ^ { \alpha } } & { \mathrm { i f ~ } \{ e _ { \alpha } \} \mathrm { ~ i s ~ a ~ c o r d i n a t e ~ b a s i s } , } \end{array}
$$

except that they work in arbitrary bases, not just in Lorentz bases.And,as in Lorentz frames,so also in general: the one-form basis $\{ d x ^ { \alpha } \}$ and the tangent-vector basis $\{ \hat { \boldsymbol { d } } / \hat { \boldsymbol { o } } \boldsymbol { x } ^ { \alpha } \}$ ， which are induced into a tangent space by the same coordinate system, are the duals of each other,

$$
\langle d x ^ { \alpha } , \partial / \partial x ^ { \beta } \rangle = \delta ^ { \alpha } { } _ { \beta } .
$$

(See exercise 9.2 for proofs.) Also,most aspects of Cartan's “Exterior Calculus"(parts A,B, C of Box 4.1) are left unaffected by the removal of metric.

# $\$ 9.5$ .TENSORS

A tensor S,in the absence of Lorentz metric,differs from the tensors of flat, Lorentz spacetime in two ways.(l) $\pmb { s }$ must reside at a specific event $\mathcal { P } _ { 0 }$ ,just as any vector or l-form must.(2) Each slot of $\pmb { s }$ is specific; it will accept either vectors or l-forms, but not both, because it has no way to convert a 1-form $\widetilde { \pmb { u } }$ into a“corresponding

Specificity of tensor slots

vector” $\pmb { u }$ as it sends $\widetilde { \pmb { u } }$ through its linear machinery. Thus,if $\pmb { s }$ is a $\textstyle { { \binom { 1 } { 2 } } }$ tensor

s(... ...）, insert 1-form here insert vector here insert vector here

then it cannot be converted alternatively to a $\textstyle { { \binom { 2 } { 1 } } }$ tensor, or a $( _ { 0 } ^ { 3 } )$ tensor, or a $( \mathbf { _ { 3 } ^ { 0 } } )$ tensor by the procedure of $\ S 3 . 2$ . In component language, the indices of $\pmb { S }$ cannot be raised and lowered.

Except for these two restrictions (attachment to a specific event; specificity of slots), a tensor $\pmb { s }$ is the same linear machine as ever.And the algebra of component manipulations is the same:

$$
\begin{array} { c } { { { \stackrel {  } { \pmb S } } = S ^ { \alpha } { } _ { \beta \gamma } { \pmb e } _ { \alpha } \stackrel {  } { \otimes } \tilde { \pmb { \omega } ^ { \beta } } \otimes { } \tilde { \pmb { \omega } ^ { \gamma } } , } } \\ { { { \pmb S } ( \pmb \sigma , u , v ) = S ^ { \alpha } { } _ { \beta \gamma } \sigma _ { \alpha } u ^ { \beta } v ^ { \gamma } . } } \end{array}
$$

# Exercise 9.1. COMPONENT MANIPULATIONS

Derive equations (9.1lc) through (9.1lg) from (9.10), (9.1la,b),(9.6), (9.7),and (9.8).

# Exercise 9.2. COMPONENTS OF GRADIENT, AND DUALITY OF COORDINATE BASES

In an arbitrary basis, define $f _ { , \alpha }$ by the expansion (9.13a). Then combine equations (9.1ld) and (9.12) to obtain the method (9.13b) of computing $f _ { , \alpha }$ Finally,combine equations (9.12) and (9.13b) to show that the bases $\{ d x ^ { \alpha } \}$ and $\left\{ \partial / \partial x ^ { \beta } \right\}$ are the duals of each other.

# ExerCise 9.3. PRACTICE MANIPULATING TANGENT VECTORS

Let $\mathscr { s } _ { \mathbf { 0 } }$ be the point with coordinates $( x = 0 , y = 1 , z = 0 )$ in a three-dimensional space; and define three curves through $\mathscr { P } _ { \mathbf { 0 } }$ by

$$
\begin{array} { r l } & { \mathcal { P } ( \lambda ) = ( \lambda , 1 , \lambda ) , } \\ & { \mathcal { S } ( \xi ) = ( \sin \xi , \cos \xi , \xi ) , } \\ & { \mathcal { S } ( \rho ) = ( \sinh \rho , \cosh \rho , \rho + \rho ^ { 3 } ) . } \end{array}
$$

(a） Compute $( d / d \lambda ) f , ( d / d \xi ) f ,$ and $( d / d \rho ) f$ for the function $f = x ^ { 2 } - y ^ { 2 } + z ^ { 2 }$ at the point $\mathscr { P } _ { \mathbf { 0 } } .$ (b) Calculate the components of the tangent vectors $d / d \lambda , d / d \boldsymbol { \xi }$ and $d / d \rho$ at $\mathcal { P } _ { \mathbf { 0 } } .$ using the basis $\{ { \partial } / { \partial x } ,  \partial / { \partial y } , \partial / { \partial z }  \}$ ·

# ExerCise 9.4. MORE PRACTICE WITH TANGENT VECTORS

In a three-dimensional space with coordinates $( x , y , z )$ ,introduce the vector field $v = y ^ { 2 }$ $\partial / \partial x - x \partial / \partial z$ ， and the functions $f = x y , g = z ^ { 3 }$ . Compute

$$
\begin{array} { c c }   ( a )  \begin{array} { c c } { { { \pmb v } [ { f } ] \quad } } & { { ( c ) { \pmb v } [ { f g } ] \quad } } \\ { { ( b ) { \pmb v } [ { g } ] \quad } } & { { ( d ) { \begin{array} { c c } { { f { \pmb v } [ { g } ] \quad } } & { { ( e ) { \pmb v } [ { f } ^ { 2 } + g ^ { 2 } ] } } \\ { { f { \pmb v } [ { g } ] - g { \pmb v } [ { f } ] \quad } } & { { ( f ) { \pmb v } \{ { \pmb v } [ { f } ] \} } } \end{array} } } } \end{array} \end{array}
$$

ExerCise 9.5. PICTURE OF BASIS 1-FORMS INDUCED BY COORDINATES In the tangent space of Figure 9.l, draw the basis l-forms $\pmb { d } \pmb { \psi }$ and $\pmb { d } \chi$ induced by the $\psi$ ， $x ^ { \cdot }$ coordinate system.

# Exercise 9.6. PRACTICE WITH DUAL BASES

In a three-dimensional space with spherical coordinates $r , \theta , \phi ,$ ,one often likes to use,instead of the basis $\partial / \partial r , \partial / \partial \theta , \partial / \partial \phi .$ the basis

$$
\pmb { e } _ { \hat { r } } = \frac { \hat { \partial } } { \partial r } , \qquad \pmb { e } _ { \hat { \theta } } = \frac { 1 } { r } \frac { \hat { \partial } } { \partial \theta } , \qquad \pmb { e } _ { \hat { \phi } } = \frac { 1 } { r \sin \theta } \frac { \hat { \partial } } { \partial \phi } .
$$

(a)What is the l-form basis $\{ \pmb { \omega } ^ { \hat { \tau } } , \pmb { \omega } ^ { \hat { \theta } } , \pmb { \omega } ^ { \hat { \phi } } \}$ dual to this tangent-vector basis? (b) On the sphere $r = 1$ ，draw pictures of the bases $\left\{ { \partial } / { \partial r } , \right. \partial / { \partial \theta } , \left. { \partial } / { \partial \phi } \right\}$ ， $\{ \pmb { e } _ { \hat { r } } , \pmb { e } _ { \hat { \theta } } , \pmb { e } _ { \hat { \phi } } \}$ ， $\{ d r , d \theta , d \phi \}$ ， and $\{ \pmb { \omega } ^ { \hat { r } } , \pmb { \omega } ^ { \hat { \theta } } , \pmb { \omega } ^ { \hat { \phi } } \}$

# S9.6. COMMUTATORS AND PICTORIAL TECHNIQUES

A vector ${ \pmb u } _ { 0 }$ given only at one point $\mathcal { P } _ { 0 }$ suffices to compute the derivative $\pmb { u } _ { 0 } [ f ] \equiv$ $\partial _ { { \pmb u } _ { 0 } } f ,$ which is simply a number associated with the point $\scriptstyle { \mathfrak { s p } } _ { 0 }$ . In contrast, a vector field $\pmb { u }$ provides a vector ${ \pmb u } ( { \mathcal { P } } )$ -which is a differential operator $\widehat { \partial } _ { \pmb { \omega } ( \mathfrak { s p } ) }$ -at each point $\mathcal { P }$ in some region of spacetime. This vector field operates on a function $f$ to produce not just a number, but another function $\pmb { u } [ f ] \equiv \partial _ { \pmb { u } } f .$ A second vector field $\pmb { \nu }$ can perfectly well operate on this new function, to produce yet another function

$$
{ \pmb v } \{ { \pmb u } [ f ] \} = \hat { \partial } _ { \pmb v } ( \hat { \partial } _ { \pmb u } f ) .
$$

Does this function agree with the result of applying ${ \pmb v }$ first and then ${ \pmb u } \mathrm { ? }$ Equivalently, does the“commutator”

$$
[ { \pmb u } , { \pmb v } ] [ f ] \equiv { \pmb u } \{ { \pmb v } [ f ] \} - { \pmb v } \{ { \pmb u } [ f ] \}
$$

vanish?

The simplest special case is when $\pmb { u }$ and $\pmb { \nu }$ are basis vectors of a coordinate system, $\pmb { \mu } = \hat { \partial } / \hat { \partial } x ^ { \alpha }$ ， $\pmb { v } = \partial / \partial x ^ { \beta }$ . Then the commutator does vanish, because partial derivatives always commute:

$$
[ \partial / \partial x ^ { \alpha } , \partial / \partial x ^ { \beta } ] [ f ] = \partial ^ { 2 } f / \partial x ^ { \beta } \partial x ^ { \alpha } - \partial ^ { 2 } f / \partial x ^ { \alpha } \partial x ^ { \beta } = 0 .
$$

But in general the commutator is nonzero,as one sees from a coordinate-based calculation:

$$
\begin{array} { c } { { \displaystyle { [ { \pmb u } , { \pmb v } ] } f = u ^ { \alpha } \frac { \hat { \partial } } { \partial x ^ { \alpha } } \left( v ^ { \beta } \frac { \hat { \partial } f } { \partial x ^ { \beta } } \right) - v ^ { \alpha } \frac \hat { \partial } { \hat { \sigma } x ^ { \alpha } } \left( u ^ { \beta } \frac { \hat { \partial } f } { \partial x ^ { \beta } } \right) } } \\ { { = \left[ ( u ^ { \alpha } v ^ { \beta } { } _ { , \alpha } - v ^ { \alpha } { u ^ { \beta } } _ { , \alpha } ) \frac \hat { \partial } { \partial x ^ { \beta } } \right] f . } } \end{array}
$$

Commutator of two vector fields isa vector field

Notice however, that the commutator $[ { \pmb u } , { \pmb v } ]$ like ${ \pmb u }$ and $\pmb { \nu }$ themselves,isa vector field,i.e., a linear differential operator at each event:

Commutator asa “closer of curves"

$$
[ { \pmb u } , { \pmb v } ] = ( { \pmb u } [ { \pmb v } ^ { \beta } ] - { \pmb v } [ { \pmb u } ^ { \beta } ] ) \frac { \hat { \partial } } { \partial { \pmb x } ^ { \beta } } = ( { \pmb u } ^ { \alpha } { \pmb v } ^ { \beta } , _ { \alpha } - v ^ { \alpha } { \pmb u } ^ { \beta } , _ { \alpha } ) \frac { \hat { \partial } } { \partial { \pmb x } ^ { \beta } } .
$$

Such results should be familiar from quantum theory's formalism for angular momentum operators (exercise 9.8).

The three levels of geometry-pictorial, abstract, and component-yield three different insights into the commutator.(l） The abstract expresion $[ { \pmb u } , { \pmb v } ]$ suggests the close connection to quantum theory,and brings to mind the many tools developed there for handling operators. But recall that the operators of quantum theory need not be first-order differential operators. The kinetic energy is second order and the potential is zeroth order in the familiar Schrodinger equation. Only first-order operators are vectors.(2)The component expression $u ^ { \alpha } v ^ { \beta } { } _ { , \alpha } - v ^ { \alpha } u ^ { \beta } { } _ { , \alpha } ,$ valid in any coordinate basis,brings the commutator into the reaches of the powerful tools of index mechanics. (3） The pictorial representation of $[ \pmb { u } , \pmb { v } ]$ $( { \tt B o x } \ 9 . 2 )$ reveals its fundamental role as a “closer of curves”-a role that willbe important in Chapter 1l's analysis of curvature.

Commutators find application in the distinction between a coordinate-induced basis, $\{ \pmb { e } _ { \alpha } \} = \{ \hat { \sigma } / \hat { \sigma } x ^ { \alpha } \}$ ,and a noncoordinate basis. Because partial derivatives always commute,

# A. Pictorial Representation in Flat Spacetime

1. For ease of visualization, consider flat spacetime,so the two vector fields ${ \pmb u } ( { \mathcal { P } } )$ and ${ \pmb v } ( { \mathcal { P } } )$ can be laid out in spacetime itself.   
2. Choose an event ${ \mathfrak { s o } } _ { 0 }$ where the commutator $[ { \pmb u } , { \pmb v } ]$ is to be calculated.   
3. Give the names $\mathcal { P } _ { 1 } , \mathcal { P } _ { 2 } , \mathcal { P } _ { 3 } , \mathcal { P } _ { 4 }$ to the events pictured in the diagram.   
4. Then the vector $\mathcal { P } _ { 4 } - \mathcal { P } _ { 3 } ,$ which measures how much the four-legged curve fails to close, can be expressed in a coordinate basis as

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/8bf2c15d493349ec4b5a37ac9f8779bb55ba220e0c8bdb21f907097bd5797d4a.jpg)  
Box 9.2 THE COMMUTATOR AS A CLOSER OF QUADRILATERALS

$$
\begin{array} { r l } { \mathcal { S } _ { 4 } - \mathcal { S } _ { 3 } = [ \pmb { u } ( \mathcal { P } _ { 0 } ) + \pmb { v } ( \mathcal { P } _ { 1 } ) ] - [ \pmb { u } ( \mathcal { P } _ { 2 } ) + \pmb { v } ( \mathcal { P } _ { 0 } ) ] } & { } \\ { = [ \pmb { v } ( \mathcal { P } _ { 1 } ) - \pmb { v } ( \mathcal { P } _ { 0 } ) ] - [ \pmb { u } ( \mathcal { P } _ { 2 } ) - \pmb { u } ( \mathcal { P } _ { 0 } ) ] } & { } \\ { = ( v ^ { \beta } , \alpha ^ { u ^ { \alpha } } \pmb { e } _ { \beta } ) _ { \mathcal { S } _ { 0 } } - ( u ^ { \beta } , \alpha ^ { v ^ { \alpha } } \pmb { e } _ { \beta } ) _ { \mathcal { S } _ { 0 } } + \mathrm { ~ e r r o r s } } & { } \\ { = [ \pmb { u } , \pmb { v } ] _ { \mathcal { S } _ { 0 } } + \mathrm { ~ e r r o r s . } } & { } \\ { \qquad \quad \pmb { \mathrm { ~ \mathscr { L } _ { [ t e r m s ~ s u c h ~ a s ~ } } v ^ { \beta } } , _ { \mu ^ { \nu } } u ^ { \mu } u ^ { \nu } \pmb { e } _ { \beta } ] } \end{array}
$$

5. Notice that if u and v are halved everywhere, then [u,v] is cut down by a factor of 4, while the error terms in the above go down by a factor of 8. Thus, $[ \pmb { u } , \pmb { v } ]$ represents accurately the gap in the four-legged curve (“quadrilateral") in the limit where $\pmb { u }$ and $\pmb { \nu }$ are sufficiently short; i.e., $[ { \pmb u } , { \pmb v } ]$ "closes the quadrilateral”whose edges aie the vectors felds $\pmb { u }$ and $v .$

B. Pictorial Representation in Absence of Metric, or in Curved Spacetime with a Metric

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/489a97286ff6e8a1e68e5c7025d32b9260d64d497a702426ad238fe946ac211d.jpg)

1. The same picture must work, but now one dares not (at least initially)lay out the vector fields in spacetime itself. Instead one lays out two families of curves: the curves for which ${ \pmb u } ( { \mathcal { P } } )$ is the tangent vector; and the curves for which ${ \pmb v } ( \mathcal { P } )$ is the tangent vector.

2. The gap ${ } ^ { 6 6 } { \mathcal { P } } _ { 4 } - { \mathcal { P } } _ { 3 } { } ^ { \prime \prime }$ in the four-legged curve can be characterized by the difference $f ( \mathcal { P } _ { 4 } ) - f ( \mathcal { P } _ { 3 } )$ in the values of an arbitrary function at ${ \mathcal { P } } _ { 4 }$ and $\mathcal { P } _ { 3 }$ .That difference is,in a coordinate basis,

$$
\begin{array} { r c l } { { f ( \dot { \mathcal { S } } _ { 4 } ) - f ( \mathcal { S } _ { 3 } ) = \displaystyle \{ f ( \mathfrak { s } ^ { \rho } _ { 4 } ) - f ( \mathfrak { s } ^ { \rho } _ { 1 } ) \} } } & { { + } } & { { \displaystyle \{ f ( \mathfrak { s } ^ { \rho } _ { 1 } ) - f ( \mathfrak { s } ^ { \rho } _ { 0 } ) \} } } \\ { { \displaystyle \ } } & { { \displaystyle \left( f _ { , \alpha } \mathfrak { v } ^ { \alpha } + \frac { 1 } { 2 } f _ { , \alpha \beta } \mathfrak { v } ^ { \alpha } \mathfrak { v } ^ { \beta } \right) _ { \varphi _ { 1 } } } } & { { \displaystyle \ \left( f _ { , \alpha } \mathfrak { u } ^ { \alpha } + \frac { 1 } { 2 } f _ { , \alpha \beta } \mathfrak { u } ^ { \alpha } \mathfrak { u } ^ { \beta } \right) _ { \varphi _ { 0 } } } } \\ { { - \underbrace { [ f ( \mathfrak { s } ^ { \rho } _ { 2 } ) - f ( \mathfrak { s } ^ { \rho } _ { 0 } ) ] } _ { \displaystyle \left( f _ { , \alpha } \mathfrak { v } ^ { \alpha } + \frac { 1 } { 2 } f _ { , \alpha \beta } \mathfrak { v } ^ { \alpha } \mathfrak { v } ^ { \beta } \right) _ { \varphi _ { 0 } } } } } & { { - } } & { { \displaystyle \frac { [ f ( \mathfrak { s } ^ { \rho } _ { 3 } ) - f ( \mathfrak { s } ^ { \rho } _ { 2 } ) ] } { 2 } } } \end{array}
$$

$$
\begin{array} { r l } & { = [ ( u ^ { \beta } v ^ { \alpha } , _ { \beta } - v ^ { \beta } u ^ { \alpha } , _ { \beta } ) \partial f / \partial x ^ { \alpha } ] _ { \mathcal { S } _ { 0 } } + } \\ & { = \{ [ u , v \} [ f ] \} _ { \mathcal { S } _ { 0 } } + \cdots \mathrm { c u b i c ~ e r r o r s . } ^ { , , } } \end{array}
$$

Here “cubic errors” are cut down by a factor of 8,while $[ { \pmb u } , { \pmb v } ] f$ is cut down by one of 4,whenever ${ \pmb u }$ and $\pmb { \nu }$ are cut in half.

3.The result

$$
f ( \mathcal { P } _ { 4 } ) - f ( \mathcal { S } _ { 3 } ) = \{ { \boldsymbol { [ } \pmb { u } , \pmb { v } ] } [ f ] \} _ { \mathcal { S } _ { 0 } } + \mathrm { { ^ { * } c u b i c \ e r r o r s ^ { \prime } } }
$$

says that $[ { \pmb u } , { \pmb v } ]$ is a tangent vector at $\mathcal { P } _ { 0 }$ that describes the separation between the points $\mathcal { P } _ { 3 }$ and ${ \mathcal { P } } _ { 4 }$ .Its description gets arbitrarily accurate when $\pmb { u }$ and $\pmb { \nu }$ get arbitrarily short. Thus, $[ { \pmb u } , { \pmb v } ]$ closes the quadrilateral whose edges are the projections of $\pmb { u }$ and $\pmb { v }$ into spacetime.

# C． Philosophy of Pictures

1. Pictures are no substitute for computation. Rather, they are useful for (a) suggesting geometric relationships that were previously unsuspected and that one verifies subsequently by computation; (b) interpreting newly learned geometric results.

2.This usual noncomputational role of pictures permits one to be sloppy in drawing them. No essential new insight was gained in part B over part A, when one carefully moved the tangent vectors into their respective tangent spaces, and permitted only curves to lie in spacetime. Moreover, the original picture (part A) was clearer because of its greater simplicity.

3.This motivates one to draw “sloppy” pictures,with tangent vectors lying in spacetime itself-so long as one keeps those tangent vectors short and occasionally checks the scaling of errors when the lengths of the vectors are halved.

Conversely,if one is given a feld of basis vectors ("frame field") $\{ \pmb { e } _ { \alpha } ( \mathcal { P } ) \}$ ,but one does not know whether a coordinate system $\{ x ^ { \alpha } ( { \mathcal { P } } ) \}$ exists in which $\{ \pmb { e } _ { \alpha } \} = \{ \hat { \sigma } / \hat { \sigma } x ^ { \alpha } \}$ ， one can find out by a simple test: calculate all $( 4 \times 3 ) / 2 = 6$ commutators $[ e _ { \alpha } , e _ { \beta } ] ;$ if they al vanish,then there exists such a coordinate system. If not, there doesn't. Stated more briefly, $\{ \pmb { e } _ { \alpha } ( \mathcal { P } ) \}$ is a coordinate-induced basis if and only if $[ { \pmb e } _ { \alpha } , { \pmb e } _ { \beta } ] = 0$ for all ${ \pmb { e } } _ { \pmb { \alpha } }$ and $\pmb { e } _ { \beta }$ .(See exercise 9.9 for proof; see $\ S 1 1 . 5$ for an important application.) Coordinate-induced bases are sometimes called “holonomic.”In an “anholonomic basis” (noncoordinate basis), one defines the commutation coefficients ${ c _ { \mu \nu } } ^ { \alpha }$ by

Vanishing commutator:a test for coordinate bases

Commutation coefficients defined

$$
[ \pmb { e } _ { \mu } , \pmb { e } _ { \nu } ] = c _ { \mu \nu } ^ { \alpha } \pmb { e } _ { \alpha } .
$$

They enter into the component formula for the commutator of arbitrary vector felds ${ \pmb u }$ and $\pmb { \nu }$

$$
[ { \pmb u } , { \pmb v } ] = ( { \pmb u } [ { \pmb v } ^ { \beta } ] - { \pmb v } [ { \pmb u } ^ { \beta } ] + { \pmb u } ^ { \mu } { \pmb v } ^ { \nu } c _ { \mu \nu } ^ { \beta } ) { \pmb e } _ { \beta }
$$

(see exercise 9.10).

[Warning! In notation for functions and fields,mathematicians and physicists often use the same symbols to mean contradictory things. The physicist may write $\ell$ when considering the length of some critical component in an instrument he is designing, then switch to $\ell ( T )$ when he begins to analyze its response to temperature changes. Thus $\ell$ is a number, whereas $\ell ( T )$ is a function. The mathematician,in contrast, will write $f$ for a function that he may be considering as an element in some infinite-dimensional function space. Once the function is supplied with an argument, he then contemplates $f ( x )$ ,which is merely a number: the value of $f$ at the point $_ x$ .Caught between these antithetical rituals of the physics and mathematics sects, the authors have adopted a clear policy: vacilation. Usually physics-sect statements, like “On a curve $\mathcal { P } ( \lambda ) \ldots , \neg \ ,$ are used; and the reader can translate them himself into mathematically precise language: “Consider a curve $\mathcal { C }$ on which a typical point is ${ \mathcal { P } } = { \mathcal { C } } ( \lambda )$ ; on this curve ....” But on occasion the reader will encounter a pedantic-sounding paragraph written in mathematics-sect jargon (Example: Box 23.3). Such paragraphs deal with concepts and relationships so complex that standard physics usage would lead to extreme confusion. They also should prevent the reader from becoming so conditioned to physics usage that he is allergic to the mathematical literature,where great advantages of clarity and economy of thought are achieved by consistent reliance on wholly unambiguous notation.]

Physicists'notation vs. mathematicians'notation

# Exercise 9.7. PRACTICE WITH COMMUTATORS

Compute the commutator $[ e _ { \hat { \theta } } . e _ { \hat { \phi } } ]$ of the vector fields

$$
{ \pmb e } _ { \hat { \theta } } = \frac { 1 } { r } \frac { \partial } { \hat { c } \pmb \theta } , \qquad { \pmb e } _ { \hat { \phi } } = \frac { 1 } { r \sin \theta } \frac { \hat { c } } { \hat { c } \phi } .
$$

Express your result as a linear combination of $\pmb { \theta } _ { \pmb { \theta } }$ and $\pmb { e } _ { \hat { \phi } }$

# Exercise 9.8. ANGULAR MOMENTUM OPERATORS

In Cartesian coordinates of three-dimensional Euclidean space,one defines three “angularmomenium operalors"(vector fields) $\pmb { L _ { j } }$ by

$$
\pmb { L } _ { j } \equiv \epsilon _ { j k l } x ^ { k } ( \hat { c } / \hat { c } x ^ { l } ) .
$$

Draw a picture of these three vector fields. Calculate their commutators both pictorially and analytically.

# Exercise 9.9. COMMUTATORS AND COORDINATE-INDUCED BASES

Let $\pmb { u }$ and $\pmb { \nu }$ be vector fields in spacetime. Show that in some neighborhood of any given point there exists a coordinate system for which

$$
\pmb { \upsilon } = \hat { \varrho } / \hat { \varrho } x ^ { 1 } , \qquad \pmb { v } = \hat { \varrho } / \partial x ^ { 2 } ,
$$

if and only if $\pmb { u }$ and $\pmb { v }$ are linearly independent and commute:

$$
[ { \pmb u } , { \pmb v } ] = 0 .
$$

First make this result plausible from the second figure in $\tt B o x 9 . 2$ ； then prove it mathematically. Note: this result can be generalized to four arbitrary vector fields $e _ { 0 } , e _ { 1 } , e _ { 2 } ,$ $\pmb { e _ { 3 } }$ There exists a coordinate system in which $\pmb { e } _ { \alpha } = \hat { \partial } / \hat { \partial } x ^ { \alpha }$ if and only if $\pmb { e } _ { 0 } , \pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ are linearly independent and $[ { \pmb e } _ { \mu } , { \pmb e } _ { \nu } ] = 0$ for all pairs ${ \pmb \mathscr { e } } _ { \mu } , \pmb { \mathscr { e } } _ { \mathfrak { r } }$

# Exercise 9.1O. COMPONENTS OF COMMUTATOR IN NON-COORDINATE BASIS Derive equation (9.23).

# Exercise 9.11. LIE DERIVATIVE

The“Lie derivative” of a vector field ${ \pmb v } ( { \pmb \mathcal { P } } )$ along a vector field ${ \pmb u } ( { \pmb \mathcal { P } } )$ is defined by

$$
\pmb { \mathscr { L } } _ { \pmb { \mu } } \pmb { v } \equiv [ \pmb { u } , \pmb { v } ] .
$$

Draw a space-filling family of curves (a “congruence") on a sheet of paper. Draw an arbitrary vector $\pmb { v }$ at an arbitrary point $\mathcal { P } _ { \mathbf { 0 } }$ on the sheet. Transport that vector along the curve through $\scriptstyle { \mathcal { P } } _ { 0 }$ by means of the “Lie iransport law” $\pmb { \mathscr { L } _ { u } } \pmb { v } = 0$ ,where $\pmb { \mu } = d / d t$ is the tangent to the curve. Draw the resulting vector $\pmb { \nu }$ at various points $\mathcal { P } ( t )$ along the curve.

Exercise 9.12. A CHIP OFF THE OLD BLOCK (a) Prove the Jacobi identity

$$
[ { \pmb u } , [ { \pmb v } , { \pmb w } ] ] + [ { \pmb v } , [ { \pmb w } , { \pmb u } ] ] + [ { \pmb w } , [ { \pmb u } , { \pmb v } ] ] = 0
$$

by picking out all terms of the form $\hat { \partial } _ { \pmb { \mu } } \hat { \partial } _ { \pmb { \nu } } \hat { c } _ { \mathbf { w } } ,$ showing that they add to zero,and arguing from symmetry that all other terms, e.g., $\hat { c } _ { { \pmb w } } \hat { d } _ { \pmb { \mu } } \hat { d } _ { \pmb { v } }$ terms,must similarly cancel.

(b) State this identity in index form.   
(c) Draw a picture corresponding to this identity (see Box 9.2).

# $\$ 9.7$ .MANIFOLDS AND DIFFERENTIAL TOPOLOGY

Spacetime is not the only arena in which the ideas of this chapter can be applied. Points,curves,vectors, 1-forms,and tensors exist in any“differentiable manifold.”

Their use to study differentiable manifolds constitutes a branch of mathematics called "differential topology"-hence the title of this chapter.

The mathematician usually begins his development of differential topology by introducing some very primitive concepts, such as sets and topologies of sets, by building a fairly elaborate framework out of them,and by then using that framework to define the concept of a differentiable manifold. But most physicists are satisfied with a more fuzzy, intuitive definition of manifold: roughly speaking,an $\pmb { n }$ -dimensional differentiable manifold is a set of“points” tied together continuously and differentiably,so that the points in any sufficiently small region can be put into a one-to-one correspondence with an open set of points of $R ^ { n }$ · $[ R ^ { n }$ is the number space of $_ n$ dimensions,i.e., the space of ordered $\pmb { n }$ -tuples $( x ^ { 1 } , x ^ { 2 } , \ldots , x ^ { n } ) .$ ] That correspondence furnishes a coordinate system for the neighborhood.

Differentiable manifold "defined"

Examples of differentiable manifolds

A few examples will convey the concept better than this definition. Elementary examples (Euclidean 3-spaces,the surface of a sphere) bring to mind too many geometric ideas from richer levels of geometry; so one is forced to contemplate something more complicated.Let $R ^ { 3 }$ be a three-dimensional number space with the usual advanced-calculus ideas of continuity and differentiability. Points $\pmb { \xi }$ of $R ^ { 3 }$ are triples, $\pmb { \xi } = ( \xi _ { 1 } , \xi _ { 2 } , \xi _ { 3 } )$ ,of real numbers.Let a ray $\mathcal { P }$ in $R ^ { 3 }$ be any half-line from the origin consisting of all $\pmb { \xi }$ of the form $\pmb { \xi } = \lambda \pmb { \eta }$ for some fixed $\pmb { \eta } \neq 0$ and for all positive real numbers $\lambda > 0$ . (See Figure 9.3.) A good example of a differentiable manifold then is the set $S ^ { 2 }$ of all distinct rays. If $f$ is a real-valued function with a specific value $f ( { \mathcal { P } } )$ for any ray $\mathcal { P }$ [so one writes $f \colon S ^ { 2 } \longrightarrow R \colon \mathcal { P } \longrightarrow f ( \mathcal { P } ) ] ,$ it should be intuitively (or even demonstrably) clear that we can define what we mean by saying $f$ is continuous or differentiable. In this sense $S ^ { 2 }$ itself is continuous and differentiable. Thus $S ^ { 2 }$ is a manifold,and the rays $\mathcal { P }$ are the points of $S ^ { 2 }$ . There are many other manifolds that diferential topology finds indistinguishable from $S ^ { 2 }$ The simplest is the two-dimensional spherical surface (2-sphere),which is the standard representation of $S ^ { 2 }$ ; it is the set of points $\pmb { \xi }$ of $R ^ { 3 }$ satisfying $( \xi _ { 1 } ) ^ { 2 } + ( \xi _ { 2 } ) ^ { 2 } + ( \xi _ { 3 } ) ^ { 2 } = 1$ Clearly a different point $\mathcal { P }$ of $S ^ { 2 }$ (one ray in $R ^ { 3 }$ )intersects each point of this standard 2-sphere surface,and the correspondence is continuous and differentiable in either direction (ray to point; point to ray). The same is true for any ellipsoidal surface in $R ^ { 3 }$ enclosing the origin,and for any other surface enclosing the origin that has

The manifold ${ \mathcal { S } } ^ { 2 }$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/7989b22536dcf6f6cbc73db0c21e899b5f28e13ecccf284bf62bdfb6e03c3156.jpg)  
Figure 9.3. Three different representations of the differentiabie manifoid $S ^ { 2 }$ .The first is the set of ail rays emanating from the origin; the second is the sphere they intersect;the third is an oddshaped,closed surface that each ray intersects precisely once.

a different ray through each point of itself. They each embody the same global continuity and differentiability concepts. and represent the same abstract differentiable manifold $S ^ { 2 }$ ，the 2-sphere. They,and the bundle of rays we started with, all have the same geometric properties at this rudimentary level of geometry. A two-dimensional manifold that has a different geometric structure at this level (a different “differentiable structure") is the torus $T ^ { 2 }$ , the surface of a donut. There is no way to imbed this surface smoothly in $R ^ { 3 }$ so that a distinct ray $\mathcal { P } \in S ^ { 2 }$ intersects each of its points; there is no invertible and differentiable correspondence between $T ^ { 2 }$ and $S ^ { 2 }$

The manifold $\tau ^ { 2 }$

The manifold SO(3) (rotation group)

Another example of a manifold is the rotation group $S O ( 3 )$ , whose points $\mathcal { S }$ are all the $3 \times 3$ orthogonal matrices of unit determinant, s $0 \mathcal { P } = | | P _ { i j } | |$ with $\mathcal { P } ^ { \pmb { T } \ o \mathcal { O } } = 1$ and det $\langle { \boldsymbol { \mathsf { y } } } ^ { \flat } = { \boldsymbol { \mathsf { l } } }$ . This is a three-dimensional space (one often uses the three Eulerangle parameters in computations), where differential ideas (e.g., angular velocity) are employed; hence, it is a manifold. So is the Lorentz group.

The differentiability of a manifold (i.e., the possibility of defining differentiable functions on it) permits one to introduce coordinate systems locally, if not globally, and also curves, tangent spaces,tangent vectors,1-forms,and tensors, just as is done for spacetime.But the mere fact that a manifold is differentiable does not mean that such concepts as geodesics, parallel transport, curvature,metric, or length exist in it. These are additional layers of structure possessed by some manifolds, but not by all Roughly speaking, every manifold has smoothness properties and topology, but without additional structure it is shapeless and sizeless.

Affine geometry and Riemannian geometry defined

That branch of mathematics which adds geodesics, parallel transport, and curvature (shape) to a manifold is called affne geometry; that branch which adds a metric is called Riemannian geometry. They will be studied in- the next few chapters.

# EXERCISES

# EXERCISES ON THE ROTATION GROUP

As the exposition of differential geometry becomes more and more sophisticated in the following chapters,the exercises will return time and again to the rotation group as an example of a manifold.Then,in $\mathbf { B o x } ~ 3 0 . 1 $ ，the results developed in these exercises will beused to analyze the“Mixmaster universe,”which is a particularly important cosmological solution to Einstein's field equation.

Before working these exercises,the reader may wish to review the Euler-angle parametrization for rotation matrices,as treated, e.g., on pp.l07-lO9 of Goldstein (1959).

# Exercise 9.13. ROTATION GROUP:GENERATORS

Let $\mathcal { K } _ { \mathrm { ~ f ~ } }$ be three $3 \times 3$ matrices whose components are $( K _ { t } ) _ { m n } = \epsilon _ { t _ { m n } }$ (a）Display the matrices $\mathcal { F } _ { 1 } , ( \hat { \mathscr { h } _ { 1 } } ) ^ { 2 } , ( \hat { \mathscr { h } _ { 1 } } ) ^ { 3 } ,$ and $( \hat { \mathcal { R } } _ { 1 } ^ { \star } ) ^ { 4 }$ (b) Sum the series

$$
\mathcal { R } _ { z } ( \theta ) \equiv \exp ( \mathcal { K } _ { 1 } \theta ) = \sum _ { n = 0 } ^ { \infty } \frac { \theta ^ { n } } { n ! } ( \mathcal { K } _ { 1 } ) ^ { n } .
$$

Show that ${ \mathcal R } _ { \varepsilon } ( \theta )$ is a rotation matrix and that it produces a rotation through an angle $\pmb \theta$ about the $x \cdot$ -axis.

(c) Show similarly that $\mathcal { R } _ { z } ( \phi ) = \exp ( \mathcal { K } _ { 3 } \phi )$ and $\mathcal { R } _ { u } ( x ) = \exp ( \mathcal { K } _ { 2 } { \chi \smash [ t ] { \mathstrut } } )$ are rotation matrices, and that they produce rotations through angles $\phi$ and $x$ about the $z \cdot$ and y-axes, respectively.

(d) Explain why $\mathcal { P } = \mathcal { R } _ { z } ( \psi ) \mathcal { R } _ { z } ( \theta ) \mathcal { R } _ { z } ( \phi )$ defines the Euler-angle coordinates, $\psi , \theta , \phi$ for the generic element $\mathcal { P } \in S O ( 3 )$ of the rotation group.

(e) Let $\mathcal { C }$ be the curve $\mathscr { P } = \mathscr { R } _ { z } ( t )$ through the identity matrix, $\mathcal { C } ( 0 ) = \mathfrak { g } \in S O ( 3 )$ . Show that its tangent, $( d \mathcal { C } / d t ) ( 0 ) \equiv \dot { \mathcal { C } } ( 0 )$ does not vanish by computing $\dot { \mathcal { C } } ( 0 ) f _ { 1 2 }$ where $f _ { 1 2 }$ is the function $f _ { 1 2 } ( \mathcal { P } ) = P _ { 1 2 } ,$ whose value is the l2 matrix element of $\mathcal { P }$

(f) Define a vector field ${ \pmb { e } } _ { 3 }$ on $S O ( 3 )$ by letting $\pmb { \mathscr { e } } _ { 3 } ( \mathcal { P } )$ be the tangent (at $\scriptstyle { t = 0 }$ to the curve $\mathcal { C } ( t ) = \mathcal { R } _ { z } ( t ) \mathcal { P }$ through $\mathcal { P }$ . Show that $\pmb { \mathscr { e } } _ { 3 } ( \mathcal { P } )$ is nowhere zero. Note: $\pmb { e _ { 3 } } ( \mathcal { P } )$ is called the“generator of rotations about the $z \cdot$ -axis,"because it points from $\mathcal { P }$ toward neighboring rotations, $\mathcal { R } _ { z } ( t ) \mathcal { P }$ ,which differ from $\mathcal { P }$ by a rotation about the $z \cdot$ -axis.

(g） Show that $\pmb { e } _ { 3 } = ( \hat { \partial } / \hat { \partial } \psi ) _ { \pmb { \theta } \phi }$ (h) Derive the following formulas,valid for $t \ll 1$ ：

$$
\begin{array} { r l } & { \mathscr { R } _ { \boldsymbol { x } } ( t ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \psi } ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \theta } ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \phi } ) = \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \psi } - \boldsymbol { t } \sin \boldsymbol { \psi } \cot \boldsymbol { \theta } ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \theta } + \boldsymbol { t } \cos \boldsymbol { \psi } ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \phi } + \boldsymbol { t } \sin \boldsymbol { \psi } / \sin \boldsymbol { \theta } ) ; } \\ & { \mathscr { R } _ { \boldsymbol { y } } ( t ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \psi } ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \theta } ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \phi } ) = \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \psi } + \boldsymbol { t } \cos \boldsymbol { \psi } \cot \boldsymbol { \theta } ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \theta } + \boldsymbol { t } \sin \boldsymbol { \psi } ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \phi } - \boldsymbol { t } \cos \boldsymbol { \psi } / \sin \boldsymbol { \theta } ) . } \end{array}
$$

(i） Define $\pmb { e } _ { 1 } ( \pmb { \mathcal { P } } )$ and $\pmb { e } _ { 2 } ( \mathcal { P } )$ to be the tangent vectors (at $t = 0$ ）to the curves $\mathcal { C } ( t ) = \mathcal { R } _ { z } ( t ) \mathcal { P }$ and $\mathcal { C } ( t ) = \mathcal { R } _ { y } ( t ) \mathcal { P }$ ,respectively. Show that

$$
\begin{array} { r } { \pmb { e } _ { 1 } = \cos \psi \frac { \hat { \partial } } { \partial \theta } - \sin \psi \left( \cot \theta \frac { \hat { \partial } } { \partial \psi } - \frac { 1 } { \sin \theta } \frac { \hat { \partial } } { \partial \phi } \right) , } \\ { \pmb { e } _ { 2 } = \sin \psi \frac { \hat { \partial } } { \partial \theta } + \cos \psi \left( \cot \theta \frac { \hat { \partial } } { \partial \psi } - \frac { 1 } { \sin \theta } \frac { \hat { \partial } } { \partial \phi } \right) . } \end{array}
$$

$\pmb { e _ { 1 } }$ and $\pmb { e _ { 2 } }$ are the “generators of rotations about the $x \cdot$ and $y$ -axes.”

# ExerciSe 9.14. ROTATION GF:OUP: STRUCTURE CONSTANTS

Jse the three vector fields constructed in the last exercise,

$$
{ \begin{array} { r l } & { e _ { 1 } = \cos \psi { \frac { \partial } { \partial \theta } } - \sin \psi { \biggl ( } \cot \theta { \frac { \partial } { \partial \psi } } - { \frac { 1 } { \sin \theta } } { \frac { \partial } { \partial \phi } } { \biggr ) } , } \\ & { e _ { 2 } = \sin \psi { \frac { \partial } { \partial \theta } } + \cos \psi { \biggl ( } \cot \theta { \frac { \partial } { \partial \psi } } - { \frac { 1 } { \sin \theta } } { \frac { \partial } { \partial \phi } } { \biggr ) } , } \\ & { e _ { 3 } = { \frac { \partial } { \partial \psi } } , } \end{array} }
$$

as basis vectors for the manifold of the rotation group.The above equations express this “basis of generators”in terms of the Euler-angle basis.Show that the commutation coeffcients for this basis are

$$
{ c _ { \alpha \beta } } ^ { \gamma } = - \epsilon _ { \alpha \beta \gamma } ,
$$

independently of location $\mathcal { S }$ in the rotation group.These coefficients are also called the structure constants of the rotation group.
