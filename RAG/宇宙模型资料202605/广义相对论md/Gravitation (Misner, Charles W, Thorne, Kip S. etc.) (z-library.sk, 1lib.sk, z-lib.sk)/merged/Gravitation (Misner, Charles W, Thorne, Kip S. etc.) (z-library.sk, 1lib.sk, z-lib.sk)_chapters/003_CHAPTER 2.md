# CHAPTER 2

# FOUNDATIONS OF SPECIAL RELATIVITY

In geometric and physical applications,it always turns out that a quantity is characterized not only by its tensor order, but also by symmetry.

HERMAN WEYL (1925)

Undoubtedly the most striking development of geometry during the last 2,Ooo years is the continual expansion of the concept   
"geometric object." This concept began by comprising only the few curves and surfaces of Greek synthetic geometry; it was   
stretched,during the Renaissance,to cover the whole domain of   
those objects definedby analytic geometry;more recently,it has been extended to cover the boundless universe treated by point-set theory.

KARL MENGER.IN SCHILPP(1949)，P.466.

# \$2.1.OVERVIEW

Curvature in geometry manifests itself as gravitation. Gravitation works on the separation of nearby particle world lines. In turn, particles and other sources of mass-energy cause curvature in the geometry. How does one break into this closed loop of the action of geometry on matter and the reaction of matter on geometry? One can begin no better than by analyzing the motion of particles and the dynamics of fields in a region of spacetime so limited that it can be regarded as flat. (See “Test for Flatness,” Box 1.5).

Background assumed of reader

Chapters 2-6 develop this flat-spacetime viewpoint (special relativity). The reader, it is assumed.is already somewhat familiar with special relativity:\* 4-vectors in general: the energy-momentum 4-vector; elementary Lorentz transformations: the Lorentz law for the force on a charged particle;at least one look at one equation in one book that refers to the electromagnetic field tensor $F _ { \mu \nu }$ ; and the qualitative features of spacetime diagrams, including such points as (l） future and past light cones,(2) causal relationships ("past of,”“future of.”“neutral,”or “in a spacelike relationship to"),(3) Lorentz contraction.(4) time dilation,(5) absence of a universal concept of simultaneity,and (6） the fact that the $\overline { { t } }$ and $\overline { { z } }$ axes in $\tt B o X 2 . 4$ are orthogonal even though they do not look so. If the reader finds anything new in these chapters,it willbe: (i) a new viewpoint on special relativity,one emphasizing coordinate-free concepts and notation that generalize readily to curved spacetime ("geometric objects,” tensors viewed as machines-treated in Chapters 2-4); or (ii) unfamiliar topics in special relativity,topics crucial to the later exposition of gravitation theory ("stress-energy tensor and conservation laws,” Chapter 5；"accelerated observers,” Chapter 6).

# $\ S 2 . 2$ .GEOMETRIC OBJECTS

Every physical quantity can be described by a geometric object

Everything that goes on in spacetime has its geometric description, and almost every one of these descriptions lends itself to ready generalization from flat spacetime to curved spacetime. The greatest of the differences between one geometric object and another is its scope: the individual object (vector) for the momentum of a certain particle at a certain phase in its history,as contrasted to the extended geometric object that describes an electromagnetic field defined throughout space and time ("antisymmetric second-rank tensor field”or, more briefly,“field of 2-forms"). The idea that every physical quantity must be describable by a geometric object, and that the laws of physics must all be expressble as geometric relationships between these geometric objects, had its intellectual beginnings in the Erlanger program of Felix Klein (1872),came closer to physics in Einstein's“principle of general covariance”and in the writings of Hermann Weyl (l925),seems to have first been formu-lated clearly by Veblen and Whitehead (1932),and today pervades relativity theory, both special and general.

All laws of physics can be expressed geometrically

A. Nijenhuis (1952)and S.-S.Chern (l960,l966,197l) have expounded the mathematical theory of geometric objects. But to understand or do research in geometrodynamics, one need not master this elegant and beautiful subject. One need only know that geometric objects in spacetime are entities that exist independently of coordinate systems or reference frames.A point in spacetime ("event") is a geometric object. The arrow linking two neighboring events("vector") is a geometric object in flat spacetime, and its generalization, the“tangent vector,” is a geometric object even when spacetime is curved. The“metric”(machine for producing the squared length of any vector; see Box l.3) is a geometric object. No coordinates are needed to define any of these concepts.

The next few sections willintroduce several geometric objects, and show the roles they play as representatives of physical quantities in flat spacetime.

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/bda4cbe2b7cd631c0773942046f1054654e573f47869778ed790683755025bd7.jpg)  
Figure 2.1. From vector as connector of two points to vector as derivative ("tangent vector";a local rather than a bilocal concept).

# \$2.3. VECTORS

Begin with the simplest idea of a vector (Figure 2.1B): an arrow extending from one spacetime event $\boldsymbol { \mathcal { Q } }$ ("tail")） to another event $\mathcal { B }$ ("tip"). Write this vector as

Ways of defining vector: As arrow

$$
\pmb { v } _ { \vec { d } ^ { 2 } \ B } = \mathcal { B } - \vec { d } \ ( \mathrm { o r } \ \vec { d } ^ { \ c \beta } ) .
$$

For many purposes (including later generalization to curved spacetime) other completely equivalent ways to think of this vector are more convenient. Represent the arrow by the parametrized straight line $\mathcal { P } ( \lambda ) = \mathcal { Q } + \lambda ( \mathcal { B } - \mathcal { Q } )$ with $\lambda = 0$ the tail of the arrow, and $\lambda = 1$ its tip.Form the derivative of this simple linear expression for $\mathcal { P } ( \lambda )$ ：

As parametrized straightline

$$
( d / d \lambda ) [ \mathscr { Q } + \lambda ( \mathscr { B } - \mathscr { Q } ) ] = \mathscr { B } - \mathscr { Q } = \mathscr { P } ( 1 ) - \mathscr { P } ( 0 ) \equiv ( \mathrm { { t i p } ) - ( \mathrm { { t a i l } ) } \equiv \pmb { v } } _ { \mathscr { Q } \circ } .
$$

This result allows one to replace the idea of a vector as a 2-point object ("bilocal") by the concept of a vector as a l-point object ("tangent vector"; local):

$$
\pmb { v } _ { \mathcal { Q B } } = ( d \mathcal { P } / d \lambda ) _ { \lambda = 0 } .
$$

As derivative of point along curve

Example: if $\mathcal { P } ( \tau )$ is the straight world line of a free particle, parametrized by its proper time,then the displacement that occurs in a proper time interval of one second gives an arrow $\pmb { \upsilon } = \mathcal { P } ( 1 ) - \mathcal { P } ( 0 )$ .This arrow is easily drawn on a spacetime diagram. It accurately shows the 4-velocity of the particle.However, the derivative formula $\pmb { \upsilon } = d \mathcal { P } / d \tau$ for computing the same displacement （l） is more suggestive of the velocity concept and (2) lends itself to the case of accelerated motion. Thus,given a world line $\mathcal { P } ( \tau )$ that is not straight,as in Figure 2.2,one must first form $d \mathcal { P } / d \tau$ and only thereafter draw the straight line $\mathcal { P } ( 0 ) + \lambda ( d \mathcal { P } / d \tau ) _ { 0 }$ of the arrow $\pmb { \upsilon } = d \mathcal { P } / d \tau$ to display the 4-velocity ${ \pmb u }$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/fa6acd7a2964ab7f9e7587a250ad111cddb28594150282706fd8faa5eec59c36.jpg)  
Figure 2.2. Same tangent vector derived from two very different curves.That parametrized straight line is also drawn which best fits the two curves at ${ \vartheta } _ { 0 }$ The tangent vector reaches from O to l on this straight line.

The reader may be unfamiliar with this viewpoint. More familiar may be the components of the 4-velocity in a specific Lorentz reference frame:

$$
u ^ { 0 } = { \frac { d t } { d \tau } } = { \frac { 1 } { \sqrt { 1 - { \bf \nabla } \nu ^ { 2 } } } } , \qquad u ^ { j } = { \frac { d x ^ { j } } { d \tau } } = { \frac { v ^ { j } } { \sqrt { 1 - { \bf \nabla } \nu ^ { 2 } } } } ,
$$

where

$$
\begin{array} { l } { { v ^ { j } = d x ^ { j } / d t = \mathrm { c o m p o n e n t s ~ o f ~ } ^ { \ast \ast } \mathrm { o r d i n a r y ~ v e l o c i t y , } ^ { \ast } } } \\ { { \nu ^ { 2 } = ( v ^ { x } ) ^ { 2 } + ( v ^ { y } ) ^ { 2 } + ( v ^ { z } ) ^ { 2 } . } } \end{array}
$$

Even the components (2.2) of 4-velocity may seem slightly unfamiliar if the reader is accustomed to having the fourth component of a vector be multiplied by a factor $i = { \sqrt { - 1 } } .$ If so,he must adjust himself to new notation. (See “Farewell to ‘ict,'” Box 2.1.)

More fundamental than the components of a vector is the vector itself. It is a geometric object with a meaning independent of all coordinates. Thus a particle has a world line ${ \mathcal { P } } ( \tau ) ,$ ,and a 4-velocity $\pmb { \upsilon } = d \mathcal { P } / d \tau$ ，that have nothing to do with any coordinates. Coordinates enter the picture when analysis on a computer is required (rejects vectors; accepts numbers). For this purpose one adopts a Lorentz frame with orthonormal basis vectors (Figure 2.3) $\mathbf { e } _ { 0 } , \mathbf { e } _ { 1 } , \mathbf { e } _ { 2 }$ and ${ \pmb { e } } _ { 3 }$ Relative to the origin $\pmb { \mathcal { O } }$ of this frame, the world line has a coordinate description

$$
\mathcal { P } ( \tau ) - \mathcal { O } = x ^ { 0 } ( \tau ) \pmb { e } _ { 0 } + x ^ { 1 } ( \tau ) \pmb { e } _ { 1 } + x ^ { 2 } ( \tau ) \pmb { e } _ { 2 } + x ^ { 3 } ( \tau ) \pmb { e } _ { 3 } = x ^ { \mu } ( \tau ) \pmb { e } _ { \mu } .
$$

Expressed relative to the same Lorentz frame, the 4-velocity of the particle is

$$
\pmb { u } = d \pmb { \mathcal { P } } / d \tau = ( d x ^ { \mu } / d \tau ) \pmb { e _ { \mu } } = u ^ { 0 } \pmb { e _ { 0 } } + u ^ { 1 } \pmb { e _ { 1 } } + u ^ { 2 } \pmb { e _ { 2 } } + u ^ { 3 } \pmb { e _ { 3 } } .
$$

# Box 2.1 FAREWELL TO “ict"

One sometime participant in special relativity will have to be put to the sword: ${ } ^ {  } x ^ { 4 } = i c t . { } ^ {  }$ This imaginary coordinate was invented to make the geometry of spacetime look formally as little different as possible from the geometry of Euclidean space; to make a Lorentz transformation look on paper like a rotation; and to spare one the distinction that one otherwise is forced to make between quantities with upper indices (such as the components $p ^ { \mu }$ of the energy-momentum vector) and quantities with lower indices (such as the components $p _ { \mu }$ of the energy-momentum 1-form). However,it is no kindness to be spared this latter distinction. Without it, one cannot know whether a vector (S2.3) is meant or the very different geometric object that is a l-form (S2.5). Moreover, there is a significant difference between an angle on which everything depends periodically (a rotation)and a parameter the increase of which gives rise to ever-growing momentum differences (the “velocity parameter” of a Lorentz transformation; ${ \tt B o x } 2 . 4 )$ . If the imaginary time-coordinate hides from view the character of the geometric object being dealt with and the nature of the parameter in a transformation, it also does something even more serious: it hides the completely different metric structure $( \ S 2 . 4 )$ of $+ + +$ geometry and $- + + +$ geometry. In Euclidean geometry,when the distance between two points is zero, the two points must be the same point. In Lorentz-Minkowski geometry,when the interval between two events is zero,one event may be on Earth and the other on a supernova in the galaxy M31, but their separation must be a null ray (piece of a light cone).The backward-pointing light cone at a given event contains all the events by which that event can be influenced. The forward-pointing light cone contains all events that it can influence. The multitude of double light cones taking off from all the events of spacetime forms an interlocking causal structure. This structure makes the machinery of the physical world function as it does (further comments on this structure in Wheeler and Feynman l945 and 1949 and in Zeeman l964). If in a region where spacetime is flat, one can hide this structure from view by writing

$$
( A s ) ^ { 2 } = ( A x ^ { 1 } ) ^ { 2 } + ( A x ^ { 2 } ) ^ { 2 } + ( A x ^ { 3 } ) ^ { 2 } + ( A x ^ { 4 } ) ^ { 2 } ,
$$

with $x ^ { 4 } = i c t$ ，no one has discovered a way to make an imaginary coordinate work in the general curved spacetime manifold. If $^ { 6 6 } x ^ { 4 } = i c t ^ { 3 }$ cannot be used there,it will not be used here. In this chapter and hereafter,as throughout the literature of general relativity,a real time coordinate is used, $x ^ { 0 } = t = c t _ { \mathrm { c o n v } }$ (superscript O rather than 4 to avoid any possibility of confusion with the imaginary time coordinate).

The components $w ^ { \alpha }$ of any other vector $\pmb { \nu }$ in this frame are similarly defined as the coefficients in such an expansion,

Expansion of vector in terms of basis

$$
\begin{array} { r } { \pmb { w } = \pmb { w } ^ { \alpha } \pmb { e } _ { \alpha } . } \end{array}
$$

Notice: the subscript $\pmb { \alpha }$ on ${ \pmb e } _ { \alpha }$ tells which vector, not which component!

# \$2.4. THE METRIC TENSOR

The metric tensor, one recalls from part IV of Box 1.3,is a machine for calculating the squared length of a single vector,or the scalar product of two different vectors.

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/5296ca3ecf0a02d17be716cc860f9bea50c5fd9c10e9afa664ccbf11dc9ed2f0.jpg)  
Figure 2.3. The 4-velocity of a particle in flat spacetime.The 4-velocity $\pmb { u }$ is the unit vector (arrow) tangent to the particle's world line-one tangent vector for each event on the world line.In a specific Lorentz coordinate system,there are basis vectors of unit length,which point along the four coordinate axes: $\pmb { e } _ { 0 } , \pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ The 4-velocity, like any vector,can be expressed as a sum of components along the basis vectors:

$$
u = u ^ { 0 } e _ { 0 } + u ^ { 1 } e _ { 1 } + u ^ { 2 } e _ { 2 } + u ^ { 3 } e _ { 3 } = u ^ { \alpha } e _ { \alpha } .
$$

Metric defined as machine for computing scalar products of vectors

More precisely, the metric tensor $\pmb { \mathscr { g } }$ is a machine with two slots for inserting vectors

$$
\begin{array} { r } { \underset { \pmb { \mathscr { g } } ( \mathbf { \mathscr { G } } ) } { \mathrm { s l o t ~ l } } ~ \mathrm { s l o t } ~ 2 } \\ { \pmb { \mathscr { G } } ( \mathbf { \mathscr { G } } , \mathbf { \mathscr { f } } ) . } \end{array}
$$

Upon insertion, the machine spews out a real number:

$$
\begin{array} { r l } & { g ( u , v ) = \mathrm { ^ { * } s c a l a r ~ p r o d u c t ~ o f ~ } u \mathrm { ~ a n d ~ } v , \mathrm { ^ { * } ~ a l s o ~ d e n o t e d ~ } u \cdot v . } \\ & { g ( u , u ) = \mathrm { ^ { * } s q u a r e d ~ l e n g t h ~ o f ~ } u , \mathrm { ^ { * } ~ a l s o ~ d e n o t e d ~ } u ^ { 2 } . } \end{array}
$$

Moreover, this number is independent of the order in which the vectors are inserted ("symmetry of metric tensor"),

$$
\begin{array} { r } { \pmb { g } ( \pmb { u } , \pmb { v } ) = \pmb { g } ( \pmb { v } , \pmb { u } ) ; } \end{array}
$$

and it is linear in the vectors inserted

$$
g ( a u \ + \ b v , w ) = g ( w , a u \ + \ b v ) = a g ( u , w ) + b g ( v , w ) .
$$

Because the metric“machine"is inear,one can calculate its output,for any input,

as follows, if one kiows only what it does to the basis vectors ${ \pmb { e } } _ { \pmb { \alpha } }$ of a Lorentz frame. (l)Define the symbols ("metric coefficients") $\eta _ { \alpha \beta }$ by

$$
\eta _ { \alpha \beta } \equiv g ( e _ { \alpha } , e _ { \beta } ) = e _ { \alpha } \cdot e _ { \beta } .
$$

(2)Calculate their numerical values from the known squared length of the separation vector $\xi = \varDelta x ^ { \alpha } \pmb { \mathscr { e } } _ { \alpha }$ between two events:

$$
{ \begin{array} { r l } & { ( \Delta { s } ) ^ { 2 } = - ( \Delta { x ^ { 0 } } ) ^ { 2 } + ( \Delta { x ^ { 1 } } ) ^ { 2 } + ( \Delta { x ^ { 2 } } ) ^ { 2 } + ( \Delta { x ^ { 3 } } ) ^ { 2 } } \\ & { \qquad = g ( \Delta { x ^ { \alpha } } { e _ { \alpha } } , \Delta { x ^ { \beta } } { e _ { \beta } } ) = \Delta { x ^ { \alpha } } \Delta { x ^ { \beta } } g ( { e _ { \alpha } } , { e _ { \beta } } ) } \\ & { \qquad = \Delta { x ^ { \alpha } } \Delta { x ^ { \beta } } { \eta _ { \alpha \beta } } \qquad { \mathrm { f o r ~ e v e r y ~ c h o i c e ~ o f ~ } } \Delta { x ^ { \alpha } } } \end{array} }
$$

$$
\implies | | \eta _ { \alpha \beta } | | \equiv \left. \begin{array} { c c c c } { { - 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right. \mathrm { i n ~ a n y ~ L o r e n t z ~ f r a m e . }
$$

Metric coefficients

(3) Calculate the scalar product of any two vectors ${ \pmb u }$ and $\pmb { v }$ from

$$
\begin{array} { r l } & { \pmb { u } \cdot \pmb { v } = \pmb { g } ( \pmb { u } , \pmb { v } ) = \pmb { g } ( \mathscr { u } ^ { \alpha } \pmb { e } _ { \alpha } , \mathscr { v } ^ { \beta } \pmb { e } _ { \beta } ) = \mathscr { u } ^ { \alpha } \mathscr { v } ^ { \beta } \pmb { g } ( \pmb { e } _ { \alpha } , \pmb { e } _ { \beta } ) ; } \\ & { \pmb { u } \cdot \pmb { v } = \mathscr { u } ^ { \alpha } \mathscr { v } ^ { \beta } \eta _ { \alpha \beta } = - \mathscr { u } ^ { 0 } \mathscr { v } ^ { 0 } + \mathscr { u } ^ { 1 } \mathscr { v } ^ { 1 } + \mathscr { u } ^ { 2 } \mathscr { v } ^ { 2 } + \mathscr { u } ^ { 3 } \mathscr { v } ^ { 3 } . } \end{array}
$$

Scalar products computed from components of vectors

That one can classify directions and vectors in spacetime into “timelike"(negative squared length),“spacelike"(positive squared length),and “null"or “lightlike"(zero squared length) is made possible by the negative sign on the metric coefficient $\eta _ { 0 0 }$

Box 2.2 shows applications of the above ideas and notation to two elementary problems in special relativity theory.

# \$2.5.DIFFERENTIAL FORMS

Vectors and the metric tensor are geometric objects that are already familiar from Chapter l and from elementary courses in special relativity. Not so familiar, yet equally important, is a third geometric object: the“differential form”or“1-form.”

Consider the 4-momentum $\pmb { p }$ of a particle,an electron, for example. To spell out one concept of momentum，start with the 4-velocity, $\pmb { \mu } = d \mathcal { P } / d \tau$ ，of this electron ("spacetime displacement per unit of proper time along a straightline approximation of the world line").This is a vector of unit length.Multiply by the mass $m$ of the particle to obtain the momentum vector

$$
\begin{array} { r } { p = m \mathbf { \delta } u . } \end{array}
$$

But physics gives also quite another idea of momentum. It associates a de Broglie wave with each particle. Moreover,this wave has the most direct possible physical significance. Diffract this wave from a crystal lattice.From the pattern of diffraction, one can determine not merely the length of the de Broglie waves,but also the pattern in space made by surfaces of equal, integral phase $\phi = 7$ ， $\phi = 8$ ， $\phi = 9$ ,.... This

The 1-form illustrated by de Broglie waves

# Box 2.2 WORKED EXERCISES USING THE METRIC

Exercise: Show that the squared length of a test particle's 4-velocity $\pmb { u }$ is $^ { - 1 }$ Solution: In any Lorentz frame. using the components (2.2), one calculates as follows

$$
\begin{array} { l } { { { \pmb u } ^ { 2 } = g ( { \pmb u } , { \pmb u } ) = u ^ { \alpha } u ^ { \beta } \eta _ { \alpha \beta } = - ( u ^ { 0 } ) ^ { 2 } + ( u ^ { 1 } ) ^ { 2 } + ( u ^ { 2 } ) ^ { 2 } + ( u ^ { 3 } ) ^ { 2 } } } \\ { { \mathrm { ~ } } } \\ { { \mathrm { ~ } = - \displaystyle \frac { 1 } { 1 - { \bf r } ^ { 2 } } + \displaystyle \frac { { \bf r } ^ { 2 } } { 1 - { \bf r } ^ { 2 } } = - 1 . } } \end{array}
$$

Exercise: Show that the rest mass of a particle is related to its energy and momentum by the famous equation

$$
( m c ^ { 2 } ) ^ { 2 } = E ^ { 2 } - ( p c ) ^ { 2 }
$$

or,equivalently (geometrized units!),

$$
m ^ { 2 } = E ^ { 2 } - p ^ { 2 } .
$$

First Solution: The 4-momentum is defined by $\beta = m \pmb { u }$ where $\pmb { u }$ is the 4-velocity and $^ { m }$ is the rest mass. Consequently,its squared length is

$$
{ \bf \nabla } { p } ^ { 2 } = m ^ { 2 } u ^ { 2 } = - m ^ { 2 } \nonumber
$$

Second Solution: In the frame of the observer,where $E$ and $\pmb { p }$ are measured, the 4-momentum splits into time and space parts as

$$
p ^ { 0 } = E , ~ p ^ { 1 } \pmb { e } _ { 1 } + p ^ { 2 } \pmb { e } _ { 2 } + p ^ { 3 } \pmb { e } _ { 3 } = p ;
$$

hence, its squared length is

$$
p ^ { 2 } = - E ^ { 2 } + p ^ { 2 } .
$$

But in the particle's rest frame, $\pmb { p }$ splits as

$$
p ^ { 0 } = m , ~ p ^ { 1 } = p ^ { 2 } = p ^ { 3 } = 0 ;
$$

hence,its squared length is $p ^ { 2 } = - m ^ { 2 }$ .But the squared length is a geometric object defined independently of any coordinate system; so it must be the same by whatever means one calculates it:

$$
- p ^ { 2 } = m ^ { 2 } = E ^ { 2 } - p ^ { 2 } .
$$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/cc133f198b849d21d21b3abfa1861d701d878f04e65207684ee997476bbf7cd6.jpg)  
Figure 2.4. The vector separation $\pmb { \nu } = \pmb { \mathcal { P } } - \pmb { \mathcal { P } _ { 0 } }$ between two neighboring events $\mathcal { P } _ { 0 }$ and $\pmb { \mathcal { S } }$ ；a1-form $\pmb { \sigma }$ ；and the piercing of $\pmb { \sigma }$ by $\pmb { \nu }$ to give the number

$$
\langle \sigma , \pmb { v } \rangle = ( { \mathrm { n u m b e r ~ o f ~ s u r f a c e s ~ p i e r c e d } } ) = 4 . 4
$$

(4.4 “bongs of bell").When $\pmb { \sigma }$ is made of surfaces of constant phase, $\phi = 1 7$ ， $\phi = 1 8$ ， $\phi = 1 9$ .... of the de Broglie wave for an electron, then $\langle \pmb { \sigma } , \pmb { v } \rangle$ is the phase difference between the events $\scriptstyle { \mathcal { P } } _ { 0 }$ and $\mathcal { P }$ .Note that $\pmb { \sigma }$ is not fully specified by its surfaces;an orientation is also necessary.Which direction from surface to surface is“positive";i.e., in which direction does $\phi$ increase?

pattern of surfaces, given a name $\mathbf { \mu } ^ { \mathbf { * } \mathbf { * } } \widetilde { \pmb { k } }$ ” provides the simplest illustration one can easily find for a l-form.

The pattern of surfaces in spacetime made by such a l-form: what is it good for? Take two nearby points in spacetime, $\mathcal { P }$ and $\mathcal { P } _ { 0 } .$ Run an arrow $\pmb { v } = \mathcal { P } - \mathcal { P } _ { 0 }$ from $\mathcal { P } _ { 0 }$ to ${ \mathcal { P } } .$ . It will pierce a certain number of the de Broglie wave's surfaces of integral phase,with a bong of an imaginary bell at each piercing. The number of surfaces pierced (number of “bongs of bell") is denoted

$\langle \widetilde { \pmb { k } } , \pmb { v } \rangle ;$ 1-form pierced - dLvector tat pierces in this example it equals the phase difference between tail $( \mathcal { P } _ { 0 } )$ and tip $( \mathcal { P } )$ of $\pmb { v } ,$

$$
\begin{array} { r } { \langle \widetilde { \pmb { k } } , \pmb { v } \rangle = \phi ( \mathcal { P } ) - \phi ( \mathcal { P } _ { 0 } ) . } \end{array}
$$

See Figure 2.4.

Normally neither $\mathcal { P } _ { 0 }$ nor $\mathcal { P }$ will lie at a point of integral phase.Therefore one can and will imagine,as uniformly interpolated between the surfaces of integral phase,an infinitude of surfaces with all the intermediate phase values.With their aid, the precise value of $\langle \widetilde { \pmb { k } } , \pmb { v } \rangle = \phi ( \mathcal { P } ) - \phi ( \mathcal { P } _ { 0 } )$ can be determined.

To make the mathematics simple, regard $\widetilde { \pmb { k } }$ not as the global pattern of dé Brogliewave surfaces, but as a local pattern near a specific point in spacetime. Just as the vector $\pmb { \upsilon } = d \mathcal { P } / d \tau$ represents the local behavior of a particle's world line (linear approximation to curved line in general), so the l-form $\widetilde { \pmb { k } }$ represents the local form

The 1-form viewed as family of flat,equally spaced surfaces

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/c20ad1a64f8ae382644105cc718b2782f8000e55b17f455aaab35feb3a5dd768.jpg)  
Figure 2.5. This is a dual-purpose figure. (a) It ilustrates the de Broglie wave 1-form $\widetilde { \pmb { k } }$ at an event $\mathcal { P } _ { 0 }$ (family of equally spaced,flat surfaces,or “hyperplanes”approximating the surfaces of constant phase). (b) It illustrates the gradient $\pmb { d } \phi$ of the function $\phi$ (concept defined in $\ S 2 . 6 )$ ,which is the same oriented family of fat surfaces   
The 1-form viewed as linear function of vectors

$$
\widetilde { \pmb { k } } = \pmb { d } \pmb { \phi } .
$$

At different events, $\widetilde { \pmb { k } } = \pmb { d } \phi$ is different-different orientation of surfaces and different spacing. The change in $\phi$ between the tail and tip of the very short vector $\pmb { \nu }$ is equal to the number of surfaces of $\mathbf { \delta } \mathbf { \ d } \phi$ pierced by $\pmb { v } , \langle \pmb { d } \phi , \pmb { v } \rangle$ ; it equals $\mathord { \sim } 0 . 5$ in this figure.

of the de Broglie wave's surfaces (linear approximation; surfaces flat and equally spaced;see Figure 2.5).

Regard the l-form $\widetilde { \pmb { k } }$ as a machine into which vectors are inserted,and from which numbers emerge. Insertion of $\pmb { v }$ produces as output $\langle \widetilde { \pmb { k } } , \pmb { v } \rangle$ . Since the surfaces of $\widetilde { \pmb { k } }$ are flat and equally spaced, the output is a linear function of the input:

$$
\langle \widetilde { \pmb { k } } , a \pmb { u } + b \pmb { v } \rangle = a \langle \widetilde { \pmb { k } } , \pmb { u } \rangle + b \langle \widetilde { \pmb { k } } , \pmb { v } \rangle .
$$

This,in fact, is the mathematical definition of a 1-form: a $\boldsymbol { I }$ -form isa linear, realvalued function of vectors; i.e.,a linear machine that takes in a vector and puts out a number. Given the machine ${ \widetilde { \pmb { k } } } ,$ ,it is straightforward to draw the corresponding surfaces in spacetime. Pick a point $\mathcal { P } _ { 0 }$ at which the machine is to reside.The surface of $\widetilde { \pmb { k } }$ that passes through $\mathcal { P } _ { 0 }$ contains points $\mathcal { P }$ for which $\langle \widetilde { \pmb { k } } , \mathcal { P } - \mathcal { P } _ { 0 } \rangle = 0$ (no bongs of bell). The other surfaces contain points with $\langle \widetilde { \pmb { k } } , \mathcal { P } - \mathcal { P } _ { 0 } \rangle = \pm 1$ ，±2，±3,....

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/bdbf862fe0a425855daa22fbac0be6e31febfc1208cdff0ba92554d0db10d92a.jpg)  
Figure 2.6. The addition of two 1-forms, $\pmb { \alpha }$ and $\pmb { \beta }$ ,to produce the 1-form $\pmb { \sigma }$ Required is a pictorial construction that starts from the surfaces of $\pmb { \alpha }$ and $\pmb { \beta }$ ,e.g., $\langle \pmb { \alpha } , \mathcal { S } - \mathcal { S } _ { 0 } \rangle = \ \cdots - 1 , 0 , 1 , 2 , \ldots$ and constructs those of $\pmb { \sigma } = \pmb { \alpha } + \pmb { \beta }$ 、Sucha construction,based on linearity (2.12b) of the addition process,is as follows. (l) Pick several vectors ${ \pmb u } , { \pmb v } , \ldots$ that lie parallel to the surfaces of $\pmb { \beta }$ (no piercing!), but pierce precisely 3 surfaces of $\pmb { \alpha }$ ； each of these must then pierce precisely 3 surfaces of $\pmb { \sigma }$ ：

$$
\langle \sigma , u \rangle = \langle \alpha + \beta , u \rangle = \langle \alpha , u \rangle = 3 .
$$

(2）Pick several other vectors $w , . . .$ that lie parallel to the surfaces of $\pmb { \alpha }$ but pierce precisely 3 surfaces of $\pmb { \beta }$ ：these will also pierce precisely 3surfaces of $\pmb { \sigma }$ (3)Construct that unique family of equally spaced surfaces in which $\pmb { u } , \pmb { v } , \dots , \pmb { w } , \dots .$ all have their tails on one surface and their tips on the third succeeding surface.

Sometimes l-forms are denoted by boldface, sans-serif Latin letters with tildes over them, e.g., $\widetilde { \pmb { k } }$ ;but more often by boldface Greek letters,e.g., ${ \pmb \alpha } , { \pmb \beta } , { \pmb \sigma } .$ The output of a 1-form $\pmb { \sigma } .$ ,when a vector ${ \pmb u }$ is inserted,is called “the value of $\pmb { \sigma }$ on ${ \pmb u } ^ { * }$ or “the contraction of $\pmb { \sigma }$ with $\pmb { u }$ ”

Addition of 1-forms

Also,l-forms,like any other kind of function,can be added.The 1-form $a \alpha + b \beta$ is that machine (family of surfaces) which puts out the following number when a vector $\pmb { u }$ is put in:

$$
\langle a \pmb { \alpha } + b \pmb { \beta } , \pmb { u } \rangle = a \langle \pmb { \alpha } , \pmb { u } \rangle + b \langle \pmb { \beta } , \pmb { u } \rangle .
$$

Figure 2.6 depicts this addition in terms of surfaces.

One can verify that the set of all l-forms at a given event is a“vector space" in the abstract, algebraic sense of the term.

Return to a particle and its de Broglie wave. Just as the arrow $\pmb { p } = m d \pmb { \mathcal { P } } / d \tau$ represents the best linear approximation to the particle's actual world line near $\mathcal { P } _ { 0 } .$ so the flat surfaces of the l-form $\widetilde { \pmb { k } }$ provide the best linear approximation to the curved surfaces of the particle's de Broglie wave, and $\widetilde { \pmb { k } }$ itself is the linear function that best approximates the de Broglie phase $\phi$ near $\mathcal { P } _ { 0 }$ ：

$$
\begin{array} { r } { \phi ( \mathcal { P } ) = \phi ( \mathcal { P } _ { 0 } ) + \langle \widetilde { \pmb { k } } , \mathcal { P } - \mathcal { S } _ { 0 } \rangle } \\ { + \mathrm { ~ t e r m s ~ o f ~ h i g l } } \end{array}
$$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/8f2823837841d223b5bbb14cb2475cac136095849ea4b308b1c1c013d23ea225.jpg)  
Figure 2.7. Several vectors,A,B,C,D, E,and corresponding l-forms A, B,C,D,E. The process of drawing $\tilde { \pmb { U } }$ corresponding to a given vector $\pmb { U }$ is quite simple.(l) Orient the surfaces of $\tilde { \pmb { \upsilon } }$ orihogonal to the vector $\pmb { U }$ (Why? Because any vector $\pmb { \nu }$ that is perpendicular to $\pmb { U }$ must pierce no surfaces of $\tilde { \pmb { U } }$ $( 0 = { \pmb U } \cdot \overset { \cdot } { \pmb v } = \langle \widetilde { { \pmb u } } , { \pmb v } \rangle )$ and must therefore lie in a surface of $\tilde { \pmb { U } }$ ）(2）Space the surfaces of $\tilde { \pmb { v } }$ so that the number of surfaces pierced by some arbitrary vector $\pmb { \gamma }$ (e.g., $\pmb { \gamma } = \pmb { U }$ is equal to $\pmb { \gamma } \cdot \pmb { U }$

Physical correspondence between 1-forms and vectors

Note that in the figure the surfaces of $\widetilde { \pmb { B } }$ are,indeed,orthogonal to $\pmb {8 }$ ; those of $\bar { \pmb { c } }$ are, indeed,orthogonal to $\pmb { c }$ ,etc. If they do not look so,that is because the reader is attributing Euclidean geometry,not Lorentz geometry,to the spacetime diagram.He should recall,for example,that because $\pmb { c }$ is a null vector, it is orthogonal to itself $( { \pmb { c } } \cdot { \pmb { c } } = 0 )$ ,so it must itself lie in a surface of the l-formC.Confused readers mayreview spacetime diagrams in a more elementary text,e.g.,Taylor and Wheeler (1966).

Actually，,the de Broglie l-form $\widetilde { \pmb { k } }$ and the momentum vector $\pmb { p }$ contain precisely the same information, both physically (via quantum theory) and mathematically. To see their relationship. relabel the surfaces of $\widetilde { \pmb { k } }$ by $\hbar \times$ phase, thereby obtaining the“momentum $\widetilde { \pmb { I } } \widetilde { \pmb { J } } ^ { 0 r m ^ { 3 3 } } \widetilde { \pmb { p } }$ Pierce this 1-form with any vector $\pmb { v }$ ,and find the result (exercise 2.1) that

$$
\pmb { p } \cdot \pmb { v } = \langle \widetilde { \pmb { p } } , \pmb { v } \rangle .
$$

Mathematical correspondence between 1-forms and vectors

In words: the projection of $\pmb { v }$ on the 4-momentum vector $\pmb { p }$ equals the number of surfaces it pierces in the 4-momentum l-form $\tilde { \pmb { p } }$ Examples: Vectors $\pmb { v }$ lying in a surface of $\tilde { \pmb { p } }$ (no piercing) are perpendicular to $\pmb { p }$ (no projection); $\pmb { p }$ itself pierces $p ^ { 2 } = - m ^ { 2 }$ surfaces of $\widetilde { \pmb { p } }$

Corresponding to any vector $\pmb { p }$ there exists a unique l-form (linear function of vectors) $\tilde { \pmb { p } }$ defined by equation (2.l4). And corresponding to any l-form $\widetilde { \pmb { p } }$ ,there exists a unique vector $\pmb { p }$ defined by its projections on all other vectors,by equation (2.14): Figure 2.7 shows several vectors and their corresponding 1-forms.

A single physical quantity can be described equally well by a vector $\pmb { \rho }$ or by the corresponding l-form $\widetilde { \pmb { p } }$ .Sometimes the vector description is the simplest and most natural; sometimes the l-form description is nicer. Example: Consider a 1-form representing the march of Lorentz coordinate time toward the future-surfaces $x ^ { 0 } = \ldots , 7 , 8 , 9 , \ldots .$ The corresponding vector points toward the past [see Figure 2.7 or equation (2.14)}; its description of the forward march of time is not so nice!

One often omits the tilde from the l-form $\widetilde { \pmb { p } }$ corresponding to a vector $\pmb { p }$ ，and uses the same symbol $\pmb { p }$ for both. Such practice is justified by the unique correspondence (both mathematical and physical) between $\widetilde { \pmb { p } }$ and $\pmb { p }$

# Exercise 2.1.

# EXERCISE

Show that equation (2.14) is in accord with the quantum-mechanical properties of a de Broglie wave,

$$
\psi = e ^ { i \phi } = \exp { [ i ( k : x - \omega t ) ] } .
$$

# $\$ 2.6$ .GRADIENTS AND DIRECTIONAL DERIVATIVES

There is no simpler l-form than the gradient,“df,” of a functionf.Gradient a 1-form? How so? Hasn't one always known the gradient as a vector? Yes,indeed, but only because one was not familiar with the more appropriate l-form concept. The more familiar gradient is the vector corresponding,via equation (2.l4),to the 1-form gradient. The hyperplanes representing df at a point ${ \vartheta } _ { 0 }$ are just the level surfaces offitself, except for flattening and adjustment to equal spacing (Figure 2.5; identify $f$ here with $\phi$ there). More precisely,they are the level surfaces of the linear function that approximates $f$ in an infinitesimal neighborhood of ${ \mathcal { P } } _ { 0 }$

Why the name “gradient”? Because df describes the first order changes in $f$ in the neighborhood of $\scriptstyle { \mathcal { P } } _ { 0 }$ ：

$$
f ( \mathcal { P } ) = f ( \mathcal { P } _ { 0 } ) + \langle d f , \mathcal { S } ^ { \rho } - \mathcal { S } _ { 0 } \rangle + ( \mathrm { n o n l i n e a r ~ t e r m s } ) .
$$

[Compare the fundamental idea of “derivative” of something as “best linear approximation to that something at a point”-an idea that works even for functions whose values and arguments are infinite dimensional vectors! See, e.g.,Dieudonné (1960).]

Gradient of a function as a 1-form

Take any vector $\pmb { v }$ ； construct the curve $\mathcal { S } ( \lambda )$ defined by $\mathcal { P } ( \lambda ) - \mathcal { P } _ { 0 } \overset { \cdot } { = } \lambda \pmb { v }$ ; and differentiate the function $f$ along this curve:

$$
\hat { \sigma } _ { \pmb { v } } f = ( d / d \lambda ) _ { \lambda = 0 } f [ \mathcal { P } ( \lambda ) ] = ( d f / d \lambda ) _ { \hat { \sigma } _ { 0 } } .
$$

The“differential operator,”

$$
\begin{array} { r } { \hat { \mathcal { O } } _ { \pmb { v } } = ( d / d \lambda ) _ { \mathrm { a t } \lambda = 0 , \mathrm { a l o n g ~ c u r v e } \ : \forall \lambda ) - \ : \forall _ { 0 } = \lambda \pmb { v } } . } \end{array}
$$

which does this differentiating,is called the “directional derivative operator along the vector ${ \pmb v }$ ”The directional derivative $\partial _ { v } f$ and the gradient df are intimately related,as one sees by applying $\hat { \boldsymbol { { \sigma } } } _ { \pmb { { v } } }$ to equation (2.l5) and evaluating the result at the point $\scriptstyle { \mathcal { P } } _ { 0 }$ ：

$$
\hat { \sigma } _ { \pmb { v } } f = \langle \pmb { d } f , d \pmb { \mathcal { S } } / d \lambda \rangle = \langle \pmb { d } f , \pmb { v } \rangle .
$$

This result, expressed in words, is: df is a linear machine for computing the rate of change of $f$ along any desired vector $\pmb { v } .$ Insert $\pmb { v }$ into $d f ,$ the output ("number of surfaces pierced; number of bongs of bell") is $\partial { \mathbf { } } _ { v } f .$ -which,for sufficiently small $\pmb { v } ,$ is simply the difference in $f$ between tip and tail of ${ \pmb v }$

# $\ S 2 . 7$ ． COORDINATE REPRESENTATION OF GEOMETRIC OBJECTS

In flat spacetime,special attention focuses on Lorentz frames. The coordinates $x ^ { 0 } ( { \mathcal { P } } )$ ， $x ^ { 1 } ( { \mathcal { P } } ) , x ^ { 2 } ( { \mathcal { P } } ) , x ^ { 3 } ( { \mathcal { P } } )$ of a Lorentz frame are functions; so their gradients can be calculated. Each of the resulting“basis l-forms,”

$$
\omega ^ { \alpha } = d x ^ { \alpha } ,
$$

has as its hyperplanes the coordinate surfaces $x ^ { \alpha } =$ const; see Figure 2.8. Consequently the basis vector ${ \pmb { e } } _ { \pmb { \alpha } }$ pierces precisely one surface of the basis 1-form $\pmb { \omega } ^ { \alpha }$ ，

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/27a09c597786b4c1d54e65152fdf0fd3cea8f865b26d3499b31c1a80417ec986.jpg)  
Figure 2.8. The basis vectors and l-forms of a particular Lorentz coordinate frame.The basis l-forms are so laid out that

$$
\langle { \pmb { \omega } } ^ { \alpha } , { \pmb { \sigma } } _ { \beta } \rangle = \delta ^ { \alpha } { } _ { \beta } .
$$

while the other three basis vectors lie paralel to the surfaces of $\pmb { \omega } ^ { \alpha }$ and thus pierce none:

$$
\langle { \pmb { \omega } } ^ { \alpha } , { \pmb { \sigma } } _ { \beta } \rangle = \delta ^ { \alpha } { } _ { \beta } .
$$

(One says that the set of basis l-forms $\{ { \pmb { \omega } } ^ { \alpha } \}$ and the set of basis vectors $\big \{ \pmb { e } _ { \beta } \big \}$ are the “duals” of each other if they have this property.)

Just as arbitrary vectors can be expanded in terms of the basis $\begin{array} { r } { \pmb { e } _ { \alpha } , \pmb { v } = { v } ^ { \alpha } \pmb { e } _ { \alpha } , } \end{array}$ so arbitrary l-forms can be expanded in terms of $\pmb { \omega } ^ { \beta }$ ：

Expansion of 1-form in terms of basis

$$
\sigma = \sigma _ { \beta } \omega ^ { \beta } .
$$

The expansion coefficients $\sigma _ { \beta }$ are called “the components of $\pmb { \sigma }$ on the basis $\omega ^ { \beta }$ ”

These definitions produce an elegant computational formalism, thus: Calculate how many surfaces of $\pmb { \sigma }$ are pierced by the basis vector ${ \pmb e } _ { \pmb { \alpha } }$ ； equations (2.19) and (2.20) give the answer:

Calculation and manipulation of vector and 1-form components

$$
\langle \sigma , e _ { \alpha } \rangle = \langle \sigma _ { \beta } \omega ^ { \beta } , e _ { \alpha } \rangle = \sigma _ { \beta } \langle \omega ^ { \beta } , e _ { \alpha } \rangle = \sigma _ { \beta } \delta ^ { \beta } { } _ { \alpha } ;
$$

i.e.,

$$
\langle \pmb { \sigma } , \pmb { e } _ { \alpha } \rangle = \sigma _ { \alpha } .
$$

Similarly, calculate $\langle { \pmb u } ^ { \alpha } , { \pmb v } \rangle$ for any vector ${ \pmb v } = { \pmb e } _ { \beta } v ^ { \beta }$ ; the result is

$$
\langle { \pmb { \omega } } ^ { \alpha } , { \pmb v } \rangle = { \pmb v } ^ { \alpha } .
$$

Multiply equation (2.21a) by $v ^ { \alpha }$ and sum, or multiply (2.21b) by $\sigma _ { \alpha }$ and sum; the result in either case is

$$
\langle \pmb { \sigma } , \pmb { v } \rangle = \sigma _ { \alpha } v ^ { \alpha } .
$$

This provides a way, using components, to calculate the coordinate-independent value of $\langle \pmb { \sigma } , \pmb { v } \rangle$

Each Lorentz frame gives a coordinate-dependent representation of any geometric object or relation: $\pmb { v }$ is represented by its components $v ^ { \alpha . } , \sigma$ , by its components $\sigma _ { \alpha }$ a point $\mathcal { P }$ ,by its coordinates $x ^ { \alpha }$ ；the relation $\langle { \pmb \sigma } , { \pmb v } \rangle = 1 7 . 3$ by $\sigma _ { \alpha } v ^ { \alpha } = 1 7 . 3$

To find the coordinate representation of the directional derivative operator $\partial _ { v } ,$ rewrite equation (2.l6b) using elementary calculus

$$
\hat { \boldsymbol { \sigma } } _ { \pmb { v } } = \left( \frac { d } { d \lambda } \right) _ { \mathcal { S } _ { 0 } } = \underbrace { \left( \frac { d x ^ { \alpha } } { d \lambda } \right) _ { \mathrm { \pmb { a t } } \mathcal { S } _ { 0 } \mathrm { \ a l o n g \mathcal { S ( \lambda ) } - \mathcal { S } _ { 0 } = \lambda } \nu } \left( \frac { \partial } { \partial x ^ { \alpha } } \right) } _ { \mathrm { \normalfont ~ a t \mathcal { S } _ 0 \ a l o n g \mathcal { S ( \lambda ) } - \mathcal { S } _ 0 = \lambda } \nu } ;
$$

the result is

$$
\hat { v } _ { v } = v ^ { \alpha } \hat { v } / \hat { v } x ^ { \alpha } .
$$

Directional derivative in terms of coordinates

In particular,the directional derivative along a basis vector ${ \pmb { e } } _ { \pmb { \alpha } }$ (components $[ { \pmb e } _ { \alpha } ] ^ { \beta } = \langle { \pmb \omega } ^ { \beta } , { \pmb e } _ { \alpha } \rangle = \delta ^ { \beta } { } _ { \alpha } )$ is

$$
\hat { v } _ { \pmb { \alpha } } \equiv \hat { v } _ { { \pmb e } _ { \alpha } } = \hat { v } / \hat { v } x ^ { \pmb { \alpha } } .
$$

This should also be obvious from Figure 2.8.

The components of the gradient l-form df. which are denoted $f _ { , a }$

$$
{ d f } = f _ { , \alpha } \omega ^ { \alpha } , \textrm { -- }
$$

are calculated -easily using the above formulas:

$f _ { , \mathrm { a } } = \langle \pmb { d } f , \pmb { e } _ { \mathrm { a } } \rangle$ [standard way to calculate components; equation (2.2la)] $= \hat { c } _ { \alpha } f$ [by relation (2.17) between directional derivative and gradient] $= \hat { v } f / \hat { c } x ^ { \alpha }$ [by equation (2.24)].

Thus,in agreement with the elementary calculus idea of gradient, the components of df are just the partial derivatives along the coordinate axes:

$$
\begin{array} { r l r } { f _ { , \alpha } = \hat { c } f / \hat { c } x ^ { \alpha } ; } & { { } } & { \mathrm { i . e . , } d f = ( \hat { \sigma } f / \hat { c } x ^ { \alpha } ) \pmb { d } . \mathrm { r } ^ { \alpha } . } \end{array}
$$

(Recall: $\pmb { \omega } ^ { \alpha } = \pmb { d } \boldsymbol { x } ^ { \alpha } .$ ）The formula ${ \pmb d } f = \left( \hat { \sigma } f / \hat { \sigma } . x ^ { a } \right) { \pmb d } x ^ { \alpha }$ suggests, correctly, that ${ \pmb d } f$ is a rigorous version of the “differential” of elementary calculus; see $\mathtt { B o x } 2 . 3$

Other important coordinate representations for geometric relations are explored in the following exercises.

Derive the following computationally useful formulas:

# Exercise 2.2. LOWERING INDEX TO GET THE 1-FORM CORRESPONDING TO A VECTOR

The components $u _ { \alpha }$ of the 1-form $\widetilde { \pmb { u } }$ that corresponds to a vector $\pmb { u }$ can be obtained by "lowering an index” withthe metric coeffcients $\eta _ { \alpha \beta }$ ：

$$
u _ { \alpha } = \eta _ { \alpha \beta } u ^ { \beta } ; \mathrm { i . e . . } \qquad u _ { 0 } = - u ^ { 0 } , u _ { k } = u ^ { k } .
$$

Exercise 2.3. RAISING INDEX TO RECOVER THE VECTOR

One can return to the components of $\pmb { u }$ by raising indices.

$$
u ^ { \alpha } = \eta ^ { \alpha \beta } u _ { \beta } ;
$$

the matrix $| | \eta ^ { \alpha \beta } | |$ is defined as the inverse of $| | \eta _ { \alpha \beta } | |$ ， and happens to equal $| | \eta _ { \alpha \beta } | |$ ：

$$
\eta ^ { \alpha \beta } \eta _ { \beta \gamma } \equiv \delta ^ { \alpha } { } _ { \gamma } ; \qquad \eta ^ { \alpha \beta } = \eta _ { \alpha \beta } \mathrm { ~ f o r ~ a l l ~ } \alpha , \beta .
$$

Exercise 2.4. VARIED ROUTES TO THE SCALAR PRODUCT

The scalar product of $\pmb { u }$ with ${ \pmb v }$ can be calculated in any of the following ways:

$$
\pmb { u } \cdot \pmb { v } = \pmb { g } ( \pmb { u } , \pmb { v } ) = u ^ { \alpha } v ^ { \beta } \eta _ { \alpha \beta } = u ^ { \alpha } v _ { \alpha } = u _ { \alpha } v _ { \beta } \eta ^ { \alpha \beta } .
$$

# Box 2.3 DIFFERENTIALS

The “exterior derivative”or “gradient” df of a function $f$ is a more rigorous version of the elementary concept of “differential."

In elementary textbooks,one is presented with the differential df as representing“an infinitesimal change in the function $f ( \mathcal { P } ) ^ { \dag }$ associated with some infinitesimal displacement of the point $\mathcal { P }$ ; but one will recall that the displacement of $\mathcal { P }$ is left arbitrary,albeit infinitesimal. Thus df represents a change in $f$ in some unspecified direction.

But this is precisely what the exterior derivative df represents. Choose a particular, infinitesimally long displacement $\pmb { v }$ of the point $\mathcal { P }$ . Let the displacement vector $\pmb { v }$ pierce ${ \pmb d } f$ to give the number $\langle \pmb { d } f , \pmb { v } \rangle = \hat { \sigma } _ { \pmb { v } } f .$ That number is the change of $f$ in going from the tail of $\pmb { v }$ to its tip.Thusdf,before it has been pierced to give a number,represents the change of $f$ in an unspecified direction. The act of piercing df with $\pmb { v }$ is the act of making explicit the direction in which the change is to be measured. The only failing of the textbook presentation,then,was its suggestion that df was a scalar or a number; the explicit recognition of the need for specifying a direction $\pmb { v }$ to reduce df to a number $\langle \pmb { d } f , \pmb { v } \rangle$ shows that in fact ${ \pmb d } f$ is a 1-form, the gradient of $f .$

# S2.8.THE CENTRIFUGE AND THE PHOTON

Vectors,metric,l-forms,functions,gradients,directional derivatives: all these geometric objects and more are used in flat spacetime to represent physical quantities; and all the laws of physics must be expressible in terms of such geometric objects.

Asan example,consider a high-precision redshift experiment that uses the Mossbauer effect (Figure 2.9). The emitter and the absorber of photons are attached to

Geometric objects in action: example of centrifuge and photon

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/29122a10614e631c7977857f0150769dc6c4604724d58a3b61383fc2ccacf1b1.jpg)  
Figure 2.g. The centrifuge and the photon.

the rim of a centrifuge at points separated by an angle $\pmb { \alpha }$ ,as measured in the inertial laboratory.The emitter and absorber are at radius $r$ as measured in the laboratory, and the centrifuge rotates with angular velocity $\boldsymbol { \omega }$ .PROBLEM:What is the redshift measured,

$$
z = ( \lambda _ { \mathrm { a b s o r b e d } } - \lambda _ { \mathrm { e m i t t e d } } ) / \lambda _ { \mathrm { e m i t t e d } } ,
$$

in terms of $\omega , r ,$ and $\pmb { \alpha }$ ？

SOLUTION: Let ${ \pmb u } _ { e }$ be the 4-velocity of the emitter at the event of emission of a given photon; let $\pmb { u } _ { \pmb { a } }$ be the 4-velocity of the absorber at the event of absorption; and let $\pmb { p }$ be the 4-momentum of the photon. All three quantities are vectors defined without reference to coordinates. Equally coordinate-free are the photon energies $E _ { e }$ and $E _ { a }$ measured by emitter and absorber.No coordinates are needed to describe the fact that a specific emitter emitting a specific photon atributes to it the energy $E _ { e }$ ；and no coordinates are required in the geometric formula

$$
E _ { e } = - \pmb { p } \cdot \pmb { u } _ { e }
$$

for $E _ { e }$ ：[That this formula works can be readily verified by recalling that, in the emitter's frame, ${ u _ { e } } ^ { 0 } = 1$ and $u _ { e } ^ { ~ j } = 0$ ； so

$$
E _ { e } = - p _ { \alpha } u _ { e } { } ^ { \alpha } = - p _ { 0 } = + p ^ { 0 }
$$

in accordance with the identification “(time component of 4-momentum) $=$ (energy."] Analogous to equation (2.29) is the purely geometric formula

$$
E _ { a } = - \pmb { p } \cdot \pmb { u } _ { a }
$$

for the absorbed energy.

The ratio of absorbed wavelength to emitted wavelength is the inverse of the energy ratio (since $E = h \nu = h c / \lambda$ ：

$$
\frac { \lambda _ { a } } { \lambda _ { e } } = \frac { E _ { e } } { E _ { a } } = \frac { - \pmb { p } \cdot \pmb { u } _ { e } } { - \pmb { p } \cdot \pmb { u } _ { a } } .
$$

This ratio is most readily calculated in the inertial laboratory frame

$$
{ \frac { \lambda _ { a } } { \lambda _ { e } } } = { \frac { p ^ { 0 } u _ { e } ^ { ~ 0 } - p ^ { j } u _ { e } ^ { ~ j } } { p ^ { 0 } u _ { a } ^ { ~ 0 } - p ^ { j } u _ { a } ^ { ~ j } } } \equiv { \frac { p ^ { 0 } u _ { e } ^ { ~ 0 } - p \cdot u _ { e } } { p ^ { 0 } u _ { a } ^ { ~ 0 } - p \cdot u _ { a } } } .
$$

(Here and throughout we use boldface Latin letters for three-dimensional vectors in a given Lorentz frame; and we use the usual notation and formalism of threedimensional, Euclidean vector analysis to manipulate them.) Because the magnitude of the ordinary velocity of the rim of the centrifuge, $v = \omega r$ , is unchanging in time, ${ u _ { e } } ^ { 0 }$ and ${ u _ { a } } ^ { 0 }$ are equal, and the magnitudes-but not the directions-of ${ \pmb u } _ { e }$ and ${ \pmb u } _ { \pmb { a } }$ are equal:

$$
u _ { e } \sp { 0 } = u _ { a } \sp { 0 } = ( 1 - v \sp { 2 } ) \sp { - 1 / 2 } , | u _ { e } | = | u _ { a } | = v / ( 1 - v \sp { 2 } ) \sp { 1 / 2 } .
$$

From the geometry of Figure 2.9, one sees that ${ \pmb u } _ { e }$ makes the same angle with $\pmb { p }$ as does ${ \pmb u } _ { \pmb { a } }$ Consequently, $\pmb { p } \cdot \pmb { u } _ { e } = \pmb { p } \cdot \pmb { u } _ { a }$ ，and $\lambda _ { \mathrm { a b s o r b e d } } / \lambda _ { \mathrm { e m i t t e d } } = 1$ . There is no redshift!

Notice that this solution made no reference whatsoever to Lorentz transformations—they have not even been discussed yet in this book! The power of the geometric, coordinate-free viewpoint is evident!

One must have a variety of coordinate-free contacts between theory and experiment in order to use the geometric viewpoint. One such contact is the equation $\pmb { { \cal E } } = - \pmb { \rho } \cdot \pmb { u }$ for the energy of a photon with 4-momentum $\pmb { p }$ ,as measured by an observer with 4-velocity $\pmb { u }$ Verify the following other points of contact.

# Exercise 2.5. ENERGY AND VELOCITY FROM 4-MOMENTUM

A particle of rest mass $^ { \pmb { m } }$ and 4-momentum $\pmb { p }$ is examined by an observer with 4-velocity u. Show that just as (a) the energy he measures is

$$
\pmb { { \cal E } } = - \pmb { \mathsf { p } } \cdot \pmb { \mathsf { u } } ;
$$

so (b) the rest mass he attributes to the particle is

$$
m ^ { 2 } = - p ^ { 2 } ;
$$

(c) the momentum he measures has magnitude

$$
| { \pmb p } | = [ ( { \pmb p } \cdot { \pmb u } ) ^ { 2 } + ( { \pmb p } \cdot { \pmb p } ) ] ^ { 1 / 2 } ;
$$

(d） the ordinary velocity $\pmb { \nu }$ he measures has magnitude

$$
| { \pmb v } | = \frac { | { \pmb p } | } { E } ,
$$

where $| p |$ and $E$ are as given above；and (e） the 4-vector $\pmb { v }$ ，whose components in the observer's Lorentz frame are

$$
v ^ { 0 } = 0 , \qquad v ^ { j } = ( d x ^ { j } / d t ) _ { \mathrm { f o r p a r t i c l e } } = \mathrm { o r d i n a r y ~ v e l o c i t y } ,
$$

is given by

$$
\pmb { v } = \frac { \pmb { p } + ( \pmb { p } \cdot \pmb { u } ) \pmb { u } } { - \pmb { p } \cdot \pmb { u } } .
$$

# Exercise 2.6. TEMPERATURE GRADIENT

To each event $\mathcal { Q }$ inside the sun one attributes a temperature $T ( \mathcal { Q } )$ ,the temperature measured by a thermometer at rest in the hot gas there.Then $T ( \mathcal { Q } )$ is a function; no coordinates are required for its definition and discussion.A cosmic ray from outer space flies through the sun with 4-velocity ${ \pmb u }$ 、Show that, as measured by the cosmic ray's clock,the time derivative of temperature in its vicinity is

$$
d T / d \tau = \hat { v } _ { u } T = \langle { \pmb d T } , { \pmb u } \rangle .
$$

In a local Lorentz frame inside the sun,this equation can be written

$$
\frac { d T } { d \tau } = u ^ { \alpha } \frac { \partial T } { \partial x ^ { \alpha } } = \frac { 1 } { \sqrt { 1 - \nu ^ { 2 } } } \frac { \partial T } { \partial t } + \frac { v ^ { j } } { \sqrt { 1 - \nu ^ { 2 } } } \frac { \partial T } { \partial x ^ { j } } .
$$

Why is this result reasonable?

# \$2.9. LORENTZ TRANSFORMATIONS

Lorentz transformations: of coordinates

To sinplify computations,one often works with the components of vectors and 1-forms, rather than with coordinate-free language. Such component manipulations sometimes involve transformations from one Lorentz frame to another. The reader is already familiar with such Lorentz transformations;but the short review in Box 2.4 will refresh his memory and acquaint him with the notation used in this book.

The key entities in the Lorentz transformation are the matrices $1 1 A ^ { \alpha ^ { \prime } } { } _ { \beta } | 1$ and $| | A ^ { \beta } { } _ { \alpha ^ { \prime } } \mathbb { 1 } |$ the first transforms coordinates from an unprimed frame to a primed frame,while the second goes from primed to unprimed

$$
x ^ { \alpha ^ { \prime } } = { A ^ { \alpha ^ { \prime } } } _ { \beta } x ^ { \beta } , \qquad x ^ { \beta } = { A ^ { \beta } } _ { \alpha ^ { \prime } } x ^ { \alpha ^ { \prime } } .
$$

Since they go in opposite directions,each of the two matrices must be the inverse of the other:

$$
A ^ { \alpha ^ { \prime } } { } _ { \beta } A ^ { \beta } { } _ { \gamma ^ { \prime } } = \delta ^ { \alpha ^ { \prime } } { } _ { \gamma ^ { \prime } } ; \qquad A ^ { \beta } { } _ { \alpha ^ { \prime } } A ^ { \alpha ^ { \prime } } { } _ { \gamma } = \delta ^ { \beta } { } _ { \gamma } .
$$

Of basis vectors

From the coordinate-independent nature of 4-velocity, $\pmb { u } = ( d x ^ { \alpha } / d \tau ) \pmb { e } _ { \alpha }$ , one readily derives the expressions

$$
{ \pmb e } _ { \alpha ^ { \prime } } = { \pmb e } _ { \beta } A ^ { \beta } { } _ { \alpha ^ { \prime } } , \qquad { \pmb e } _ { \beta } = { \pmb e } _ { \alpha ^ { \prime } } A ^ { \alpha ^ { \prime } } { } _ { \beta }
$$

for the basis vectors of one frame in terms of those of the other; and from other geometric equations, such as

$$
\begin{array} { c } { { { \pmb v } = { \pmb e } _ { \alpha } { \pmb v } ^ { \alpha } = { \pmb e } _ { \beta } { \pmb v } ^ { \beta ^ { \prime } } , } } \\ { { \langle { \pmb \sigma } , { \pmb v } \rangle = \sigma _ { \alpha } { \pmb v } ^ { \alpha } = \sigma _ { \beta ^ { \prime } } v ^ { \beta ^ { \prime } } , } } \\ { { { \pmb \sigma } = \sigma _ { \alpha } { \pmb \omega } ^ { \alpha } = \sigma _ { \beta ^ { \prime } } { \pmb \omega } ^ { \beta ^ { \prime } } , } } \end{array}
$$

Of basis 1-forms

one derives transformation laws

Of components

$$
\begin{array} { c c } { { { \pmb \omega } ^ { \alpha ^ { \prime } } = A ^ { \alpha ^ { \prime } } { } _ { \beta } { \pmb \omega } ^ { \beta } , } } & { { { \pmb \omega } ^ { \beta } = A ^ { \beta } { } _ { \alpha ^ { \prime } } { \pmb \omega } ^ { \alpha ^ { \prime } } ; } } \\ { { } } & { { } } \\ { { v ^ { \alpha ^ { \prime } } = A ^ { \alpha ^ { \prime } } { } _ { \beta } v ^ { \beta } , } } & { { \quad v ^ { \beta } = A ^ { \beta } { } _ { \alpha ^ { \prime } } v ^ { \alpha ^ { \prime } } ; } } \\ { { } } & { { } } \\ { { { \sigma } _ { \alpha ^ { \prime } } = { \sigma } _ { \beta } A ^ { \beta } { } _ { \alpha ^ { \prime } } , } } & { { { \sigma } _ { \beta } = { \sigma } _ { \alpha ^ { \prime } } A ^ { \alpha ^ { \prime } } { } _ { \beta } . } } \end{array}
$$

.One need never memorize the index positions in these transformation laws. One need only line the indices up so that (l) free indices on each side of the equation are in the same position; and (2） summed indices appear once up and once down.Then all will be correct! (Note: the indices on $\varLambda$ always run “northwest to southeast.")

# Box 2.4 LORENTZ TRANSFORMATIONS

Rotation of Frame of Reference by Angle $\pmb { \theta }$ in $x - y$ Plane

$$
\cos \theta = \frac { 1 } { ( 1 + s ^ { 2 } ) ^ { 1 / 2 } }
$$

t=   
x=xcos0-ysinθ y=xsinθ+ycosθ = T=t   
x= x cosθ +ysinθ y=-x sinθ+ycosθ =z

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/a163a1245320ec2f0078b05b1647415b27b2c713b79a0aa063c229f0ece37027.jpg)

All signs follow from sign of this term. Positive by inspection of point $\mathcal { P }$

# Combination of Two Such Rotations

$$
s = { \frac { s _ { 1 } + s _ { 2 } } { 1 - s _ { 1 } s _ { 2 } } } \quad \quad { \mathrm { o r } } \quad \quad \theta = \theta _ { 1 } + \theta _ { 2 }
$$

# Boost of Frame of Reference by Velocity Parameter $\pmb { \alpha }$ in ${ { \pmb z } } { \pmb t }$ Plane

$$
{ \mathrm { V e l o c i t y ~ } } \beta = { \mathrm { t a n h ~ } } \alpha ; \sinh \alpha = { \frac { \beta } { ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 } } } ; \cosh \alpha = { \frac { 1 } { ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 } } } = { } ^ { \alpha } \gamma ^ { \prime \prime }
$$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/64d5f881393fe755663e62de9bdc707031249bd07202ba20accaf2b30ec82ba4.jpg)

tan $\pmb \theta =$ velocity $\beta$ $\Bumpeq$ tanh $\pmb { \alpha }$

$\begin{array} { l r } {  { t = \overline { { t } } \cosh \alpha + \overline { { z } } \sinh \alpha } } \\ { x = \overline { { x } } } \\ { y = \overline { { y } } } \\ { z = \underbrace { \overline { { t } } \sinh \alpha } _ { \qquad \mathrm { ~ . ~ } } + \overline { { z } } \cosh \alpha } \end{array}$ $\begin{array} { l } { { \overline { { t } } = t \cosh \alpha - z \sinh \alpha } } \\ { { \overline { { x } } = x } } \\ { { \overline { { y } } = y } } \\ { { \overline { { z } } = - t \sinh \alpha + z \cosh \alpha } } \end{array}$ All'signs follow from sign of this term. Positive because object at rest at $\overline { { z } } = 0$ in rocket frame moves in direction of increasing z in lab frame.

Matrix notation: $x ^ { \mu } = { \cal A } ^ { \mu } _ { \bar { \nu } } x ^ { \bar { \nu } } , ~ x ^ { \bar { \nu } } = { \cal A } ^ { \bar { \nu } } { } _ { \mu } x ^ { \mu }$

$$
| | A ^ { \mu } _ { \vec { \nu } } | | = \left\| \begin{array} { c c c c } { { \cosh \alpha } } & { { 0 } } & { { 0 } } & { { \sinh \alpha } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } \\ { { \sinh \alpha } } & { { 0 } } & { { 0 } } & { { \cosh \alpha } } \end{array} \right\| , | | A ^ { \vec { \nu } } _ { \mu } | | = \left\| \begin{array} { c c c c } { { \cosh \alpha } } & { { 0 } } & { { 0 } } & { { - \sinh \alpha } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } \\ { { - \sinh \alpha } } & { { 0 } } & { { 0 } } & { { \cosh \alpha } } \end{array} \right\|
$$

# Box 2.4 (continued)

Energy-momentum 4-vector Charge density-current 4-vector $\begin{array} { c } { { E = \overline { { { E } } } \cosh \alpha + p ^ { \overline { { { z } } } } \sinh \alpha } } \\ { { p ^ { z } = p ^ { \overline { { { x } } } } } } \\ { { p ^ { \upsilon } = p ^ { \overline { { { \upsilon } } } } } } \\ { { p ^ { z } = \overline { { { E } } } \sinh \alpha + p ^ { \overline { { { z } } } } \cosh \alpha } } \end{array}$ $\begin{array} { l } { \rho = \overline { { \rho } } \cosh \alpha ^ { ' } + j ^ { \overline { { z } } } \sinh \alpha } \\ { j ^ { z } = j ^ { \overline { { z } } } } \\ { j ^ { y } = j ^ { \overline { { y } } } } \\ { j ^ { z } = \overline { { \rho } } \sinh \alpha + j ^ { \overline { { z } } } \cosh \alpha } \end{array}$

Aberration, incoming photon:

$$
\begin{array} { l l } { { \sin \theta = \displaystyle \frac { - p _ { \perp } } { E } = \displaystyle \frac { ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 } \sin \bar { \theta } } { 1 - \beta \cos \bar { \theta } } \qquad } } & { { \sin \bar { \theta } = \displaystyle \frac { - \overline { { { p } } } _ { \perp } } { \overline { { { E } } } } = \displaystyle \frac { ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 } \sin \theta } { 1 + \beta \cos \theta } } } \\ { { \cos \theta = \displaystyle \frac { - p ^ { z } } { E } = \displaystyle \frac { \cos \bar { \theta } - \beta } { 1 - \beta \cos \bar { \theta } } \qquad } } & { { \cos \bar { \theta } = \displaystyle \frac { - \overline { { { p } } } ^ { \bar { z } } } { \overline { { { E } } } } = \displaystyle \frac { \cos \theta + \beta } { 1 + \beta \cos \theta } } } \end{array}
$$

# Combination of Two Boosts in Same Direction

$$
\beta = \frac { \beta _ { 1 } + \beta _ { 2 } } { 1 + \beta _ { 1 } \beta _ { 2 } } \qquad \mathrm { o r } \qquad \alpha = \alpha _ { 1 } + \alpha _ { 2 } .
$$

# General Combinations of Boosts and Rotations

Spinor formalism of Chapter 41

# Poincaré Transformation

$$
x ^ { \mu } = { \cal A } _ { \alpha ^ { \prime } } ^ { \mu } x ^ { \alpha ^ { \prime } } + a ^ { \mu } .
$$

Condition on the Lorentz part of this transformation:

$$
d s ^ { \prime 2 } = \eta _ { \alpha ^ { \prime } \beta ^ { \prime } } d x ^ { \alpha ^ { \prime } } d x ^ { \beta ^ { \prime } } = d s ^ { 2 } = \eta _ { \mu \nu } { \cal A } _ { \alpha ^ { \prime } } ^ { \mu } { \cal A } _ { \beta ^ { \prime } } ^ { \nu } d x ^ { \alpha ^ { \prime } } d x ^ { \beta ^ { \prime } }
$$

or $A ^ { \eta } \eta A = \eta$ (matrix equation, with $T$ indicating “transposed,”or rows and columns interchanged).

Effect of transformation on other quantities:

$\begin{array} { r l } & { u ^ { \mu } = A ^ { \mu } { } _ { \alpha ^ { \prime } } u ^ { \alpha ^ { \prime } } } \\ & { p ^ { \mu } = A ^ { \mu } { } _ { \alpha ^ { \prime } } p ^ { \alpha ^ { \prime } } } \\ & { F ^ { \mu \nu } = A ^ { \mu } { } _ { \alpha ^ { \prime } } A ^ { \nu } { } _ { \beta ^ { \prime } } F ^ { \alpha ^ { \prime } \beta ^ { \prime } } } \\ & { \pmb { e } _ { \alpha ^ { \prime } } = \pmb { e } _ { \mu } A ^ { \mu } { } _ { \alpha ^ { \prime } } } \\ & { \pmb { \omega } ^ { \alpha ^ { \prime } } = A ^ { \alpha ^ { \prime } } { } _ { \mu } \pmb { \omega } ^ { \mu } } \\ & { \quad u = \pmb { e } _ { \alpha ^ { \prime } } u ^ { \alpha ^ { \prime } } = \pmb { e } _ { \mu } u ^ { \mu } = \pmb { u } } \end{array}$ (4-velocity) (4-momentum) $\begin{array} { c } { { u _ { \alpha ^ { \prime } } = u _ { \mu } { \cal A } _ { \alpha ^ { \prime } } ^ { \mu } ; } } \\ { { p _ { \alpha ^ { \prime } } = p _ { \mu } { \cal A } _ { \alpha ^ { \prime } } ^ { \mu } ; } } \\ { { F _ { \alpha ^ { \prime } { \beta } ^ { \prime } } = F _ { \mu \nu } { \cal A } _ { \alpha ^ { \prime } } ^ { \mu } { \cal A } _ { \beta ^ { \prime } } ^ { \nu } ; } } \end{array}$ (electromagnetic field) (basis vectors); (basis 1-forms); (the 4-velocity vector).

# Exercise 2.7. BOOST IN AN ARBITRARY DIRECTION

An especially useful Lorentz transformation has the matrix components

$$
\begin{array} { r l } & { A ^ { 0 ^ { \prime } } \circ = \gamma \equiv \frac { 1 } { \sqrt { 1 - \beta ^ { 2 } } } , } \\ & { A ^ { 0 ^ { \prime } } \sb { j } = A ^ { j ^ { \prime } } \circ = - \beta \gamma n ^ { j } , } \\ & { A ^ { j ^ { \prime } } \sb k = A ^ { k ^ { \prime } } \sb j = ( \gamma - 1 ) n ^ { j } n ^ { k } + \delta ^ { j k } \sb { \textnormal { \tiny { e p l a } } } } \\ & { A ^ { \mu } \sb { \textnormal { \tiny { \varepsilon } } ^ { \prime } } = ( \mathrm { s a m e \textnormal { a s } } A ^ { \nu ^ { \prime } } \sb k \mathrm { \ u t \ w i t h \ } \beta \mathrm { \ r e p l a } } \end{array}
$$

EXERCISE

where $\beta , n ^ { 1 } , n ^ { 2 }$ ,and $n ^ { 3 }$ are parameters, and $n ^ { 2 } \equiv ( n ^ { 1 } ) ^ { 2 } + ( n ^ { 2 } ) ^ { 2 } + ( n ^ { 3 } ) ^ { 2 } = 1$ Show (a) that this does satisfy the condition $A ^ { \eta } \eta A = \eta$ required of a Lorentz transformation (see Box 2.4); (b) that the primed frame moves with ordinary velocity $\beta \pmb { n }$ as seen in the unprimed frame; (c) that the unprimed frame moves with ordinary velocity $- \beta \pmb { n }$ (i.e., $v ^ { 1 ^ { \prime } } = - \beta \bar { n ^ { \dot { 1 } } } , v ^ { 2 ^ { \prime } } = - \beta n ^ { 2 }$ $v ^ { 3 ^ { \prime } } = - \beta n ^ { 3 } )$ as seen in the primed frame;and (d) that for motion in the $z$ direction, the transformation matrices reduce to the familiar form

$$
1 | \boldsymbol { A } ^ { \nu ^ { \prime } } { } _ { \mu } | | = \left\| \begin{array} { c c c c } { \gamma } & { 0 } & { 0 } & { - \beta \gamma } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { - \beta \gamma } & { 0 } & { 0 } & { \gamma } \end{array} \right\| , \qquad | | \boldsymbol { A } ^ { \mu } { } _ { \nu ^ { \prime } } | | = \left\| \begin{array} { c c c c } { \gamma } & { 0 } & { 0 } & { \beta \gamma } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { \beta \gamma } & { 0 } & { 0 } & { \gamma } \end{array} \right\| .
$$

# \$2.10. COLLISIONS

Whatever the physical entity,whether it is an individual mass in motion, or a torrent of fluid, or a field of force, or the geometry of space itself, it is described in classical general relativity as a geometric object of its own characteristic kind.Each such object is built directly or by abstraction from identifiable points,and needs no coordinates forits representation. It has been seen how this coordinate-free description translates into,and how it can be translated out of, the language of coordinates and components,and how components in a local Lorentz frame transform under a Lorentz transformation. Turn now to two elementary applications of this mathematical machinery to a mass in motion. One has to do with short-range forces (collisions, this section); the other, with the long-range electromagnetic force (Lorentz force law, next chapter).

In a collision, all the change in momentum is concentrated in a time that is short compared to the time of observation. Moreover, the target is typically so small and quantum mechanics so dominating, that a probabilistic description is the right one. A quantity

Scattering of particles

$$
d \sigma = \left( { \frac { d \sigma } { d \varOmega } } \right) _ { \theta } d \varOmega
$$

gives the cross section $( \mathsf { c m } ^ { 2 } )$ for scattering into the element of solid angle $d \Omega$ at the deflection angle $\pmb \theta$ ； a more complicated expression gives the probability that the original particle will enter the aperture $d \Omega$ at a given polar angle $\pmb \theta$ and azimuth $\phi$ and with energy $E$ to $E + d E$ ，while simultaneously products of reaction also emerge into specified energy intervals and into specified angular apertures. It would be out of place here to enter into the calculation of such cross sections,though it is a fascinating branch of atomic physics. It is enough to note that the cross section is an area oriented perpendicular to the line of travel of the incident particle. Therefore it is unaffected by any boost of the observer in that direction, provided of course that energies and angles of emergence of the particles are transformed in accordance with the magnitude of that boost ("same events seen in an altered reference system").

Conservation of energy-momentum in a collision

Over and above any such detailed account of the encounter as follows from the local dynamic analysis,there stands the law of conservation of energy-momentum:

$$
\sum \pmb { p } _ { J } = \sum \pmb { p } _ { K } \ .
$$

Out of this relation, one wins without further analysis such simple results as the following. (l) A photon traveling as a plane wave through empty space cannot split (not true for a focused photon!).(2) When a high-energy electron strikes an electron at rest in an elastic encounter, and the two happen to come offsharing the energy equally,then the angle between their directions of travel is less than the Newtonian value of $9 0 ^ { \circ }$ ,and the deficit gives a simple measure of the energy of the primary. (3) When an electron makes a head-on elastic encounter with a proton,the formula for the fraction of kinetic energy transferred has three rather different limiting forms, according to whether the energy of the electron is nonrelativistic,relativistic,or extreme-relativistic.(4) The threshold for the production of an $( e ^ { + } , e ^ { - } )$ pair by a photon in the field of force of a massive nucleus is $2 m _ { e }$ .(5）The threshold for the production of an $( e ^ { + } , e ^ { - } )$ pair by a photon in an encounter with an electron at rest is $4 m _ { e }$ (or $4 m _ { e } - \epsilon$ when account is taken of the binding of the $e ^ { + } e ^ { - } e ^ { - }$ system in a very light “molecule"). All these results (topics for independent projects!) and more can be read out of the law of conservation of energy-momentum.For more on this topic,see Blaton(195O), Hagedorn(1964),and Chapter 4 and the last part of Chapter 5 of Sard (1970).
