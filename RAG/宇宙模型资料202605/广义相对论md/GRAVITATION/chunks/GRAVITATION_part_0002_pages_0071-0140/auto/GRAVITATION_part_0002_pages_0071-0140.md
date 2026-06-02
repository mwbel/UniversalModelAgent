# Exercise 1.1. CURVATURE OF A CYLINDER

Show that the Gaussian curvature $R$ of the surface of a cylinder is zero by showing that geodesics on that surface (unroll!) suffer no geodesic deviation. Give an independent argument for the same conclusion by employing the formula $R = 1 / \rho _ { 1 } \rho _ { 2 } .$ where $\pmb { \rho _ { 1 } }$ and $\pmb { \rho _ { 2 } }$ are the principal radii of curvature at the point in question with respect to the enveloping Euclidean three-dimensional space.

# Exercise 1.2. SPRING TIDE VS.NEAP TIDE

Evaluate (l) in conventional units and (2) in geometrized units the magnitude of the Newtonian tide-producing_acceleration $R ^ { \prime } { } _ { 0 n 0 } ( m , n = 1 , 2 , 3 )$ generated at the Earth by (l） the moon $( \dot { m _ { \mathrm { c o n v } } } = 7 . \bar { 3 } 5 \times 1 0 ^ { 2 5 } \mathrm { g } , r = 3 . 8 4 \times 1 0 ^ { 1 0 } \mathrm { c m } )$ and (2) the sun $( m _ { \mathrm { c o n v } } = 1 . 9 8 9 ^ { \cdot } \times 1 0 ^ { 3 3 } \ : \mathrm { g } ,$ $r = 1 . 4 9 6 \times 1 0 ^ { 1 3 } \mathrm { c m } ,$ . By what factor do you expect spring tides to exceed neap tides?

# Exercise 1.3. KEPLER ENCAPSULATED

A small satellite has a circular frequency $\omega ( \mathsf { c m } ^ { - 1 } )$ in an orbit of radius $r$ about a central object of mass $m ( \mathsf { c m } )$ .From the known value of $\pmb { \omega }$ ，show that it is possible to determine neither $r$ nor $^ m$ individually,but only the effective“Kepler density”of the object as averaged over a sphere of the same radius as the orbit. Give the formula for $\omega ^ { 2 }$ in terms of this Kepler density.

It is a reminder of the continuity of history that Kepler and Galileo $( \mathtt { B o x } 1 . 9 )$ wrote back and forth,and that the year that witnessed the death of Galileo saw the birth of Newton (Box 1.l0). After Newton the first dramatically new synthesis of the laws of gravitation came from Einstein $( \mathsf { B o x } \ 1 . 1 1 )$ ，

# And what the dead had no speech for,when living, They can tell you,being dead; the communication Of the dead is tongued with fire beyond the language of the living.

T. S.ELIOT, in LITTLE GIDDING (1942)

I measured the skies Now the shadows Imeasure Skybound was the mind Earthbound the body rests

JOHANNES KEPLER,d.November 15，1630. He wrote his epitaph in Latin; it is translated by Coleman (1967),p. 109.

# PART

# PHYSICS IN FLAT SPACETIME

Wherein the readermeets an old friend, Special Relativity, outfitted in new,mod attire,and becomes more intimately acquainted with hercharms.

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

![](images/bda4cbe2b7cd631c0773942046f1054654e573f47869778ed790683755025bd7.jpg)  
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

![](images/fa6acd7a2964ab7f9e7587a250ad111cddb28594150282706fd8faa5eec59c36.jpg)  
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

![](images/5296ca3ecf0a02d17be716cc860f9bea50c5fd9c10e9afa664ccbf11dc9ed2f0.jpg)  
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

![](images/cc133f198b849d21d21b3abfa1861d701d878f04e65207684ee997476bbf7cd6.jpg)  
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

![](images/c20ad1a64f8ae382644105cc718b2782f8000e55b17f455aaab35feb3a5dd768.jpg)  
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

![](images/bdbf862fe0a425855daa22fbac0be6e31febfc1208cdff0ba92554d0db10d92a.jpg)  
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

![](images/8f2823837841d223b5bbb14cb2475cac136095849ea4b308b1c1c013d23ea225.jpg)  
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

![](images/27a09c597786b4c1d54e65152fdf0fd3cea8f865b26d3499b31c1a80417ec986.jpg)  
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

![](images/29122a10614e631c7977857f0150769dc6c4604724d58a3b61383fc2ccacf1b1.jpg)  
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

![](images/a163a1245320ec2f0078b05b1647415b27b2c713b79a0aa063c229f0ece37027.jpg)

All signs follow from sign of this term. Positive by inspection of point $\mathcal { P }$

# Combination of Two Such Rotations

$$
s = { \frac { s _ { 1 } + s _ { 2 } } { 1 - s _ { 1 } s _ { 2 } } } \quad \quad { \mathrm { o r } } \quad \quad \theta = \theta _ { 1 } + \theta _ { 2 }
$$

# Boost of Frame of Reference by Velocity Parameter $\pmb { \alpha }$ in ${ { \pmb z } } { \pmb t }$ Plane

$$
{ \mathrm { V e l o c i t y ~ } } \beta = { \mathrm { t a n h ~ } } \alpha ; \sinh \alpha = { \frac { \beta } { ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 } } } ; \cosh \alpha = { \frac { 1 } { ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 } } } = { } ^ { \alpha } \gamma ^ { \prime \prime }
$$

![](images/64d5f881393fe755663e62de9bdc707031249bd07202ba20accaf2b30ec82ba4.jpg)

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

# CHAPTER 3

# THE ELECTROMAGNETIC FIELD

The rotating armatures of every generator and every motor in this age of electricity are steadily proclaiming the truth of the relativity theory to all who have ears to hear.

LEIGH PAGE (1941)

# $\pmb { \ S 3 . 1 }$ .THE LORENTZ FORCE AND THE ELECTROMAGNETIC FIELD TENSOR

At the opposite extreme from an impulsive change of momentum in a collision (the last topic of Chapter 2) is the gradual change in the momentum of a charged particle under the action of electric and magnetic forces (the topic treated here).

Let electric and magnetic fields act on a system of charged particles. The accelerations of the particles reveal the electric and magnetic field strengths.In other words, the Lorentz force law, plus measurements on the components of acceleration of test particles,can be viewed as defining the components of the electric and magnetic fields.Once the field components are known from the accelerations of a few test particles,they can be used to predict the accelerations of other test particles (Box 3.1).Thus the Lorentz force law does double service (l) as definer of fields and (2) as predicter of motions.

Lorentz force as definer of fields and predicter of motions

Here and elsewhere in science,as stressed not least by Henri Poincaré, that view is out of date which used to say,“Defne your terms before you proceed."Al the laws and theories of physics,including the Lorentz force law, have this deep and subtle character,that they both define the concepts they use (here $\pmb { B }$ and $\pmb { \cal E }$ ）and make statements about these concepts. Contrariwise, the absence of some body of theory, law,and principle deprives one of the means properly to define or even to use concepts. Any forward step in human knowledge is truly creative in this sense: that theory, concept, law,and method of measurement-forever inseparable-are born into the world in union.

# Box 3.1 LORENTZ FORCE LAW AS BOTH DEFINER OF FIELDS AND PREDICTER OF MOTIONS

How one goes about determining the components of the field from measurements of accelerations is not different in principle for electromagnetism and for gravitation. Compare the equations in the two cases:

$$
{ \frac { d ^ { 2 } x ^ { \alpha } } { d \tau ^ { 2 } } } = { \frac { e } { m } } F _ { ~ \beta } ^ { \alpha } u ^ { \beta } \mathrm { ~ i n ~ a ~ L o r e n t z ~ f r a m e } ,
$$

and

of reference parallel to the direction of motion of this second particle,which will then respond to and measure the components $\pmb { { \cal B } } _ { y }$ and $B _ { z }$ of the magnetic field. Not so $B _ { x }$ ！ The acceleration in the $x$ -direction merely remeasures the already once measured $E _ { z }$ .To evaluate $B _ { x } ,$ a third test particle is required,but it then gives duplicate information about the other field components.The alternative? Use all $N$ particles simultaneously and on the same democratic footing,both in the evaluation of the six $\underset { \bullet } { F } _ { \alpha \beta }$ and in the testing of the Lorentz force, by applying the method of least squares. Thus, write the discrepancy between predicted and observed acceleration of the Kth particle in the form

To make explicit the simpler procedure for electromagnetism will indicate in broad outline how one similarly determines all the components of $R ^ { \alpha } { } _ { \beta \gamma \delta }$ for gravity. Begin by asking how many test particles one needs to determine the three components of $\pmb { B }$ and the three components of $\pmb { { \cal E } }$ in the neighborhood under study.For one particle, three components of acceleration are measurable; for a second particle, three more. Enough? No! The information from the one duplicates in part the information from the other. The proof? Whatever the state of motion of the first test particle,pick one's Lorentz frame to be moving the same way. Having zero velocity in this frame,the particle has a zero response to any magnetic field. The electric field alone acts on the particle. The three components of its acceleration give directly the three components $E _ { x } , ~ E _ { y } , ~ E _ { z }$ of the electric field. The second test particle cannot be at rest if it is to do more than duplicate the information provided by the first test particle. Orient the $x$ -axis of the frame

$$
\dot { u } _ { \alpha } { } ^ { \kappa } - \frac { e } { m } F _ { \alpha \beta } u ^ { \beta , \kappa } = \delta a _ { \alpha } { } ^ { \kappa } .
$$

Take the squared magnitude of this discrepancy and sum over all the particles

$$
S = \sum _ { k } \eta ^ { \alpha \beta } \delta a _ { \alpha } { } ^ { K } \delta a ^ { K } { } _ { \beta } .
$$

In this expression, everything is regarded as known except the six $F _ { \alpha \beta }$ .Minimize with respect to these six unknowns. In this way,arrive at six equations for the components of $\pmb { B }$ and $\pmb { { \cal E } }$ These equations once solved,one goes back to (3) to test the Lorentz force law.

The $6 \times 6$ determinant of the coefficients in the equation for the $F _ { \alpha \beta }$ automatically vanishes when there are only two test particles. The same line of reasoning permits one to determine the minimum number of test particles required to determine all the components of the Riemann curvature tensor.

The Lorentz force law,written in familiar three-dimensional notation, with ${ \pmb { E } } =$ electric field, ${ \pmb B } =$ magnetic feld, ${ \pmb v } =$ ordinary velocity of particle, $p =$ momentum of particle, $e =$ charge of particle, reads

$$
( d { \pmb p } / d t ) = e ( { \pmb E } + { \pmb v } \times { \pmb B } ) .
$$

The three-dimensional version of the Lorentz force law

Useful though this version of the equation may be,it is far from the geometric spirit of Einstein. A fully geometric equation will involve the test particle's energy-momentum 4-vector, ${ \pmb \rho } _ { ; }$ ，not just the spatial part $\pmb { p }$ as measured in a specific Lorentz frame;and it will ask for the rate of change of momentum not as measured by a specific Lorentz observer $( d / d t )$ ,but as measured by the only clock present $\dot { \pmb { a } }$ priori in the problem: the test particle's own clock $( d / d \tau )$ . Thus, the lefthand side of a fully geometric equation will read

$$
\begin{array} { r } { d \pmb { p } / d \tau = . } \end{array}
$$

The righthand side, the Lorentz 4-force,must also be a frame-independent object. It will be linear in the particle's 4-velocity $\pmb { u }$ , since the frame-dependent expression

$$
{ \frac { d p } { d \tau } } = { \frac { 1 } { \sqrt { 1 - { \nu ^ { 2 } } } } } { \frac { d p } { d t } } = { \frac { e } { \sqrt { 1 - { \nu ^ { 2 } } } } } ( E + \nu \times B ) = e ( u ^ { 0 } E + u \times B )
$$

is linear in the components of ${ \pmb u }$ Consequently, there must be a linear machine named Faraday, or $\pmb { F } ,$ or“electromagnetic field tensor,”with a slot into which one inserts the 4-velocity of a test particle. The output of this machine, multiplied by the particle's charge,must be the electromagnetic 4-force that it feels:

Electromagnetic field tensor defined

Geometrical version ofLorentz force law、

$$
\begin{array} { r } { d \pmb { p } / d \tau = e \pmb { F } ( \pmb { u } ) . } \end{array}
$$

By comparing this geometric equation with the original Lorentz force law (equation 3.2a),and with the companion energy-change law

$$
\frac { d p ^ { 0 } } { d \tau } = \frac { 1 } { \sqrt { 1 - \nu ^ { 2 } } } \frac { d E } { d t } = \frac { 1 } { \sqrt { 1 - \nu ^ { 2 } } } e E \cdot \nu = e E \cdot u ,
$$

one can read off the components of $\pmb { F }$ in a specific Lorentz frame. The components of $d _ { P } / d _ { T }$ are $d p ^ { \alpha } / d \tau$ , and the components of $e \pmb { F } ( \pmb { u } )$ can be written (definition of $F ^ { \alpha } { } _ { \beta } ! )$ $e F ^ { \alpha } { } _ { \beta } u ^ { \beta }$ . Consequently

$$
d p ^ { \alpha } / d \tau = e F ^ { \alpha } { } _ { \beta } u ^ { \beta }
$$

must reduce to equations (3.2a,b). Indeed it does if one makes the identification

$$
\begin{array} { r } { { \beta = 0 \quad \beta = 1 \quad \beta = 2 \quad \beta = 3 } } \\ { { \alpha = 0 \quad \left\| \begin{array} { c c c c } { { 0 } } & { { E _ { x } } } & { { E _ { y } } } & { { E _ { z } } } \\ { { E _ { x } } } & { { 0 } } & { { B _ { z } } } & { { - B _ { y } } } \\ { { E _ { y } } } & { { - B _ { z } } } & { { 0 } } & { { B _ { x } } } \\ { { E _ { z } } } & { { B _ { y } } } & { { - B _ { z } } } & { { 0 } } \end{array} \right\| . } } \end{array}
$$

Components of electromagnetic field tensor

More often seen in the literature are the“covariant components,” obtained by lowering an index with the metric components:

$$
F _ { \alpha \beta } = \eta _ { \alpha \gamma } F ^ { \gamma } { } _ { \beta } ;
$$

$$
| | F _ { \alpha \beta } | | = \left. \begin{array} { c c c c } { { 0 } } & { { - E _ { x } } } & { { - E _ { y } } } & { { - E _ { z } | } } \\ { { E _ { x } } } & { { 0 } } & { { B _ { z } } } & { { - B } } \\ { { E _ { y } } } & { { - B _ { z } } } & { { 0 } } & { { B _ { x } } } \\ { { E _ { z } } } & { { B _ { y } } } & { { - B _ { x } } } & { { 0 } } \end{array} \right.
$$

This matrix equation demonstrates the unity of the electric and magnetic felds. Neither one by itself, $\pmb { { \cal E } }$ or $\pmb { B }$ ,is a frame-independent, geometric entity. But merged together into a single entity, $\pmb { F } =$ Faraday, they acquire a meaning and significance that transcends coordinates and reference frames.

# EXERCISE

# Exercise 3.1.

Derive equations (3.5) and (3.7) for the components of Faraday by comparing (3.4) with (3.2a,b),and by using definition (3.6).

# \$3.2. TENSORS IN ALL GENERALITY

Examples of tensors

A digression is in order. Now on the scene are several different tensors: the metric tensor $\pmb { g }$ (S2.4), the Riemann curvature tensor Riemann (S1.6), the electromagnetic field tensor Faraday (S3.1). Each has been defined as a linear machine with input slots for vectors,and with an output that is either a real number, e.g., ${ \pmb g } ( { \pmb u } , { \pmb v } )$ ,or a vector, e.g., Riemann $( \pmb { u } , \pmb { v } , \pmb { w } )$ and Faraday $( { \pmb u } )$

Should one make a distinction between tensors whose outputs are scalars,and tensors whose outputs are vectors? No! A tensor whose output is a vector can be reinterpreted trivially as one whose output is a scalar. Take, for example,Fara-$d a \gamma = F .$ Add a new slot for the insertion of an arbitrary 1-form $\pmb { \sigma }$ ,and gears and wheels that guarantee the output

$$
\pmb { F } ( \pmb { \sigma } , \pmb { u } ) = \langle \pmb { \sigma } , \pmb { F } ( \pmb { u } ) \rangle = \mathrm { r e a l ~ n u m b e r } .
$$

Then permit the user to choose whether he inserts only a vector, and gets out the vector $\pmb { F } ( . . . , \pmb { u } ) = \pmb { F } ( \pmb { u } )$ ,or whether he inserts a form and a vector,and gets out the number ${ \pmb F } ( { \pmb \sigma } , { \pmb u } )$ .The same machine will do both jobs.Moreover,in terms of components in a given Lorentz frame, both jobs are achieved very simply:

By analogy, one defines the most general tensor $\pmb { H }$ and its rank $\textstyle { \binom { n } { m } }$ as follows: $\pmb { H }$ is a linear machine with $\pmb { n }$ input slots for $\pmb { n }$ 1-forms,and $m$ input slots for $m$ vectors; given the requested input, it puts out a real number denoted

Definition of tensor as linear machine that converts vectors and 1-forms into numbers

$$
H ( \underbrace { \sigma , \boldsymbol { A } , \ldots , \boldsymbol { \beta } } _ { n \mathrm { ~ l - f o r m s } } , \underbrace { \pmb { u } , \pmb { v } , \ldots , \pmb { w } } _ { m \mathrm { ~ v e c t o r s } } ) .
$$

For most tensors the output changes when two input vectors are interchanged,

$$
R i e m a n n ( \sigma , u , v , w ) \neq R i e m a n n ( \sigma , v , u , w ) ,
$$

or when two input 1-forms are interchanged.

Choose a specific tensor $\pmb { S }$ of rank $( _ { 1 } ^ { 2 } )$ for explicitness. Into the slots of $\pmb { s }$ insert the basis vectors and 1-forms of a specific Lorentz coordinate frame. The output is a“component of $\pmb { s }$ in that frame":

$$
S ^ { \alpha \beta } { } _ { \gamma } \equiv { } \pmb { S } ( \pmb { \omega } ^ { \alpha } , \pmb { \omega } ^ { \beta } , \pmb { e } _ { \gamma } ) .
$$

Components of a tensor

This defines components. Knowing the components in a specific frame,one can easily calculate the output produced from any input forms and vectors:

$$
\begin{array} { l } { { { \pmb S } ( \sigma , \rho , \pmb v ) = { \pmb S } ( \sigma _ { \alpha } \pmb \omega ^ { \alpha } , \rho _ { \beta } \pmb \omega ^ { \beta } , v ^ { \gamma } { \pmb e } _ { \gamma } ) = \sigma _ { \alpha } \rho _ { \beta } v ^ { \gamma } { \pmb S } ( \pmb \omega ^ { \alpha } , \pmb \omega ^ { \beta } , \pmb e _ { \gamma } ) } } \\ { { = { \pmb S } ^ { \alpha \beta } { \gamma } ^ { \sigma _ { \alpha } \rho } { _ \beta } v ^ { \gamma } . } } \end{array}
$$

Tensor's machine action expressed in terms of components

And knowing the components of $\pmb { s }$ in one Lorentz frame (unprimed),plus the Lorentz transformation matrices $| | A ^ { \alpha ^ { \prime } } { } _ { \beta } | |$ and $1 | A ^ { \beta } { } _ { \alpha ^ { \prime } } | |$ which link that frame with another (primed),one can calculate the components in the new (primed) frame. As shown in exercise 3.2,one need only apply a matrix to each index of $\pmb { s }$ , lining up the matrix indices in the logical manner

$$
S ^ { \mu ^ { \prime } \nu ^ { \prime } } { } _ { \lambda ^ { \prime } } = S ^ { \alpha \beta } { } _ { \gamma } A ^ { \mu ^ { \prime } } { } _ { \alpha } A ^ { \nu ^ { \prime } } { } _ { \beta } A ^ { \gamma } { } _ { \lambda ^ { \prime } } .
$$

Lorentz transformation of components

A slight change of the internal gears and wheels inside the tensor enables one of its l-form slots to accept a vector.Allthat is necessary is a mechanism to convert an input vector $\pmb { n }$ into its corresponding l-form $\widetilde { \pmb { n } }$ and then to put that 1-form into the old machinery. Thus,denoting the modified tensor by the same symbol $\pmb { s }$ as was used for the original tensor, one demands

$$
\pmb { S } ( \sigma , n , \pmb { v } ) = \pmb { S } ( \sigma , \widetilde { \pmb { n } } , \pmb { v } ) ;
$$

Modifying a tensor to accept eitheravectorora1-form into each slot

or, in component notation

$$
S ^ { \alpha } { } _ { \beta \gamma } \sigma _ { \alpha } n ^ { \beta } v ^ { \gamma } = S ^ { \alpha \beta } { } _ { \gamma } \sigma _ { \alpha } n _ { \beta } v ^ { \gamma } .
$$

This is achieved if one raises and lowers the indices of $\pmb { s }$ using the components of the metric:

$$
S ^ { \alpha } { } _ { \beta \gamma } = \eta _ { \beta \mu } S ^ { \alpha \mu } { } _ { \gamma } , \qquad S ^ { \alpha \mu } { } _ { \gamma } = \eta ^ { \mu \beta } S ^ { \alpha } { } _ { \beta \gamma } .
$$

(See exercise 3.3 below.) By using the same symbol $\pmb { s }$ for the original tensor and the modified tensor, one allows each slot to accept either a 1-form or a vector, so one loses sight of whether $\pmb { s }$ is a $\mathbf { \Sigma } ( _ { 1 } ^ { 2 } )$ tensor, or a $\textstyle { { \binom { 1 } { 2 } } }$ tensor, or a $\textstyle { \binom { 3 } { 0 } }$ tensor, or a $( \small { \begin{array} { l } { 0 } \\ { 3 } \end{array} } )$ tensor;one only distinguishes its total rank,3. Terminology:an“upstairs index”is calledcontravantdowsair”inexisalldcotsin $S ^ { \alpha } { } _ { \beta \gamma ^ { * } }$ $" \alpha '$ is a contravariant index,while $^ { \bullet \bullet } { \bar { \beta } } ^ { \bullet }$ and“Y’are covariant indices.

Because tensors are nothing but functions,they can be added (if they have the same rank!) and multiplied by numbers in the usual way: the output of the rank-3 tensor $a \pm b \pmb { \mathscr { a } }$ ,when vectors u, v,w are put in, is

$$
( a \pmb { S } + b \pmb { \Omega } ) ( \pmb { u } , \pmb { v } , \pmb { w } ) \equiv a \pmb { S } ( \pmb { u } , \pmb { v } , \pmb { w } ) + b \pmb { \Omega } ( \pmb { u } , \pmb { v } , \pmb { w } ) .
$$

Several other important operations on tensors are explored in the following exercises.   
They and the results of the exercises will be used freely in the material that follows.

# EXERCISES

Exercise 3.2. TRANSFORMATION LAW FOR COMPONENTS OF A TENSOR From the transformation laws for components of vectors and 1-forms,derive the transformation law (3.14).

# Exercise 3.3. RAISING AND LOWERING INDICES

Derive equations (3.16) from equation (3.15'） plus the law ${ \pmb { n } } _ { \alpha } = { \pmb { \eta } } _ { \alpha \beta } { \pmb { n } } ^ { \beta }$ for getting the components of the 1-form n from the components of its corresponding vector $\pmb { n }$

# Exercise 3.4. TENSOR PRODUCT

Given any two vectors $\pmb { u }$ and $\pmb { \nu } _ { \pmb { \imath } }$ ,one defines the second-rank tensor $\pmb { \nu } \otimes \pmb { \nu }$ ("tensor product of $\pmb { u }$ with $\pmb { v } ^ { \prime \prime }$ ）to be a machine,with two input slots,whose output is the number

$$
( \pmb { \mathscr { u } } \otimes \pmb { \mathscr { v } } ) ( \pmb { \sigma } , \pmb { \lambda } ) = \langle \pmb { \sigma } , \pmb { \mathscr { u } } \rangle \langle \pmb { \lambda } , \pmb { \mathscr { v } } \rangle
$$

when 1-forms $\pmb { \sigma }$ and $\pmb { \lambda }$ are inserted. Show that the components of ${ \pmb { \tau } } = { \pmb { \upsilon } } \otimes { \pmb { \ v } }$ are the products of the components of $\pmb { u }$ and $\pmb { v } \mathrm { : }$

$$
T ^ { \alpha \beta } = u ^ { \alpha } v ^ { \beta } , \qquad T _ { \alpha } { } ^ { \beta } = u _ { \alpha } v ^ { \beta } , \qquad T _ { \alpha \beta } = u _ { \alpha } v _ { \beta } .
$$

Extend the definition to several vectors and forms,

$$
( \pmb { u } \otimes \pmb { v } \otimes \pmb { \beta } \otimes \pmb { w } ) ( \pmb { \sigma } , \pmb { A } , \pmb { n } , \pmb { \zeta } ) = \langle \pmb { \sigma } , \pmb { u } \rangle \langle \pmb { A } , \pmb { v } \rangle \langle \pmb { \beta } , \pmb { n } \rangle \langle \pmb { \zeta } , \pmb { w } \rangle ,
$$

and show that the product rule for components still holds:

$$
\begin{array} { c } { { \pmb S = \pmb u \otimes \pmb v \otimes \pmb \beta \otimes \pmb w \mathrm { \mathrm { \bf ~ h a s ~ c o m p o n e n t s } } } } \\ { { \pmb S ^ { \mu \nu } { } _ { \lambda } { } ^ { \sharp } = u ^ { \mu } v ^ { \nu } \beta _ { \lambda } w ^ { \xi } . } } \end{array}
$$

# Exercise 3.5. BASIS TENSORS

Show that a tensor $\pmb { M }$ with components $M ^ { \alpha \beta } { } _ { \gamma } { } ^ { \delta }$ in a given Lorentz frame can be reconstructed from its components and from the basis 1-forms and vectors of that frame as follows:

$$
{ \bf \partial } ^ { \cdot } M = M ^ { \alpha \beta } { } _ { \gamma } { } ^ { \delta } e _ { \alpha } \otimes e _ { \beta } \otimes \omega ^ { \gamma } \otimes e _ { \delta } .
$$

(For a special case of this, see Box 3.2.)

# Box 3.2 THE METRIC IN DIFFERENT LANGUAGES

# A. Geometric Language

$\pmb { \mathscr { g } }$ is a linear,symmetric machine with two slots for insertion of vectors. When vectors ${ \pmb u }$ and $\pmb { v }$ are inserted, the output of $\pmb { g }$ is their scalar product:

$$
\begin{array} { r } { \pmb { g } ( \pmb { u } , \pmb { v } ) = \pmb { u } \cdot \pmb { v } . } \end{array}
$$

# B. Component Language

$\eta _ { \mu \nu }$ are the metric components. They are used to calculate the scalar product of two vectors from components in a specific Lorentz frame:

$$
u \cdot v = \eta _ { \mu \nu } u ^ { \mu } v ^ { \nu } .
$$

# C. Coordinate-Based Geometric Language

The metric $\pmb { g }$ can be writen,in terms of basis 1-forms of a specific Lorentz fram, as

$$
g = \eta _ { \mu \nu } \varpi ^ { \mu } \otimes \varpi ^ { \nu } = \eta _ { \mu \nu } \ / d x ^ { \mu } \otimes d x ^ { \nu }
$$

[see equations (2.18) and (3.2).

# D. Connection to the Elementary Concept of Line Element

$\tt B o x 2 . 3$ demonstrated the correspondence between the gradient df of a function, and the elementary concept df of a differential change of $f$ in some unspecified direction. There is a similar correspondence between the metric, writen as $\eta _ { \mu } , d x ^ { \mu }$ $\otimes \ d x ^ { \nu }$ ,and the elementary concept of “line element,” written as $d s ^ { 2 } = \eta _ { \mu \nu } d x ^ { \mu } d x ^ { \nu }$ This elementary line element,as expounded in many special relativity texts,represents the squared length of the displacement $\ " d x \mu \ v { r } { }$ in an unspecified direction. The metric $\eta _ { \mu \nu } d x ^ { \mu } \otimes d x ^ { \nu }$ does the same. Pick a specific infinitesimal displacement vector $\pmb { \xi }$ ,and insert it into the slots of $\eta _ { \mu \nu } d x ^ { \mu } \otimes d x ^ { \nu }$ . The output will be $\xi ^ { 2 } = \eta _ { \mu \nu } \xi ^ { \mu } \xi ^ { \nu }$ ， the squared length of the displacement. Before $\pmb { \xi }$ is inserted, $\eta _ { \mu \nu } d x ^ { \mu } \otimes d x ^ { \nu }$ has the potential to tell the squared length of any vector; the insertion of $\pmb { \xi }$ converts potentiality into actuality: the numerical value of $\xi ^ { 2 }$

Because the metric $\eta _ { \mu \nu } d x ^ { \mu } \otimes d x ^ { \nu }$ and the line element $d s ^ { 2 } = \eta _ { \mu \nu } d x ^ { \mu } d x ^ { \nu }$ perform this same function of representing the squared length of an unspecified infinitesimal displacement, there is no conceptual distinction between them. One sometimes uses the symbols $\mathbf { d } s ^ { 2 }$ to denote the metric; one sometimes gets pressed and writes it as $d s ^ { 2 } = \eta _ { \mu \nu } d x ^ { \mu } d x ^ { \nu }$ ,omitting the $" \otimes "$ ； and one sometimes even gets so pressed as to use nonbold characters,so that no notational distinction remains at all between metric and elementary line element:

$$
g = d s ^ { 2 } = d s ^ { 2 } = \eta _ { \mu \nu } d x ^ { \mu } d x ^ { \nu } .
$$

# Exercise 3.6. Faraday MACHINERY AT WORK

An observer with 4-velocity $\pmb { u }$ picks out three directions in spacetime that are orthogonal and purely spatial (no time part) as seen in his frame. Let $\pmb { e } _ { \hat { 1 } }$ ， ${ \pmb e } _ { \hat { \bf 2 } } , { \pmb e } _ { \hat { \bf 3 } }$ be unit vectors in those directions and let them be oriented in a righthanded way $( \pmb { e } _ { \hat { 1 } } \cdot \pmb { e } _ { \hat { 2 } } \times \pmb { e } _ { \hat { 3 } } = + 1$ in three-dimensional language).Why do the following relations hold?

$$
{ \pmb e } _ { j } \cdot { \pmb u } = 0 , \qquad { \pmb e } _ { j } \cdot { \pmb e } _ { \hat { k } } = \delta _ { j k } .
$$

What vectors are to be inserted in the two slots of the electromagnetic field tensor Faraday if one wants to get out the electric field along $\pmb { e } _ { j }$ as measured by this observer? What vectors must be inserted to get the magnetic field he measures along ${ \pmb e } _ { j } { \pmb \mathrm { : \theta } }$

# \$3.3. THREE-PLUS-ONE VIEW VERSUS GEOMETRIC VIEW

The power of the geometric view of physics

Great computational and conceptual power resides in Einstein's geometric view of physics. Ideas that seem complex when viewed in the everyday “space-plus-time” or $" 3 + 1 "$ manner become elegant and simple when viewed as relations between geometric objects in four-dimensional spacetime. Derivations that are difficult in $3 + 1$ language simplify in geometric language.

Example of electromagnetism

The electromagnetic field is a good example. In geometric language, it is described by a second-rank,antisymmetric tensor ("2-form") $\pmb { F } _ { i }$ ，which requires no coordinates for its definition. This tensor produces a 4-force on any charged particle given by

$$
\begin{array} { r } { d \pmb { p } / d \tau = e \pmb { F } ( \pmb { u } ) . } \end{array}
$$

It is all so simple!

By contrast, consider the $" 3 + 1 "$ viewpoint. In a given Lorentz frame, there is an electric field $\pmb { { \cal E } }$ and a magnetic field $\pmb { B }$ They push on a particle in accordance with

Transformation law for electric and magnetic fields

$$
d { p } / d t = e ( { \cal E } + \nu \times { \cal B } ) .
$$

But the values of $\underline { { \boldsymbol { p } } } , \pmb { \cal E } , \pmb { \nu } ,$ and $\pmb { B }$ all change when one passes from the given Lorentz frame to a new one. For example, the electric and magnetic fields viewed from a rocket ship ("barred” frame) are related to those viewed in the laboratory ("unbarred” frame) by

$$
\begin{array} { r l r } & { \boldsymbol { \bar { E } } _ { \parallel } = \boldsymbol { E } _ { \parallel } , \quad } & { \boldsymbol { \bar { E } } _ { \perp } = \frac { 1 } { \sqrt { 1 - \beta ^ { 2 } } } ( \boldsymbol { E } _ { \perp } + \boldsymbol { \beta } \times \boldsymbol { B } _ { \perp } ) , } \\ & { \boldsymbol { \bar { B } } _ { \parallel } = \boldsymbol { B } _ { \parallel } , \quad } & { \boldsymbol { \bar { B } } _ { \perp } = \frac { 1 } { \sqrt { 1 - \beta ^ { 2 } } } ( \boldsymbol { B } _ { \perp } - \boldsymbol { \beta } \times \boldsymbol { E } _ { \perp } ) . } \end{array}
$$

(Here“ll" means component along direction of rocket's motion;“⊥"means perpendicular component; and $\beta ^ { j } = d x _ { \mathrm { ~ r o c k e t } } ^ { j } / d t$ is the rocket's ordinary velocity.） The analogous transformation laws for the particle's momentum $\pmb { p }$ and ordinary velocity $\pmb { \nu }$ ，and for the coordinate time $t$ ,all conspire-as if by magic, it seems,from the $3 + 1$ viewpoint-to maintain the validity of the Lorentz force law in all frames.

Not only is the geometric view far simpler than the $3 + 1$ view, it can even derive the $3 + 1$ equations with greater ease than can the $3 + 1$ view itself. Consider,for example,the transformation law (3.23） for the electric and magnetic fields.The geometric view derives it as follows: (l) Orient the axes of the two frames so their relative motion is in the $z$ -direction. (2） Perform a simple Lorentz transformation (equation 2.45) on the components of the electromagnetic field tensor:

$$
\begin{array} { r l } & { \bar { E } _ { 1 1 } = \bar { E } _ { z } = F _ { \overline { { 3 0 } } } = A ^ { \alpha } _ { \overline { { 3 } } } A ^ { \beta } _ { \overline { { 0 } } } F _ { \alpha \beta } = \gamma ^ { 2 } F _ { 3 0 } + \beta ^ { 2 } \gamma ^ { 2 } F _ { 0 3 } } \\ & { \quad = ( 1 - \beta ^ { 2 } ) \gamma ^ { 2 } F _ { 3 0 } = F _ { 3 0 } = E _ { z } = E _ { 1 \mid } , } \\ & { \bar { E } _ { x } = F _ { \overline { { 1 0 } } } = A ^ { \alpha } _ { \overline { { 1 } } } A ^ { \beta } _ { \overline { { 0 } } } F _ { \alpha \beta } = \gamma F _ { 1 0 } + \beta \gamma F _ { 1 3 } = \gamma ( E _ { x } - \beta B _ { y } ) , } \end{array}
$$

By contrast, the $3 + 1$ view shows much more work.A standard approach is based on the Lorentz force law and energy-change law (3.2a,b), written in the slightly modified form

$$
m \frac { d ^ { 2 } \overline { { x } } } { d \tau ^ { 2 } } = e \bigg ( \bar { E } _ { x } \frac { d \overline { { t } } } { d \tau } + 0 \frac { d \overline { { x } } } { d \tau } + \bar { B } _ { z } \frac { d \overline { { y } } } { d \tau } - \bar { B } _ { y } \frac { d \overline { { z } } } { d \tau } \bigg ) ,
$$

... (three additional equations)....

It proceeds as follows (details omitted because of their great length!):

(1） Substitute for the $d ^ { 2 } \overline { { x } } / d \tau ^ { 2 }$ , etc.,the expression for these quantities in terms of the $d ^ { 2 } x / d \tau ^ { 2 }$ ... (Lorentz transformation).   
(2） Substitute for the $d ^ { 2 } x / d \tau ^ { 2 }$ ,... the expression for these accelerations in terms of the laboratory $\pmb { { \cal E } }$ and $\pmb { B }$ (Lorentz force law).   
(3） In these expressions,wherever the components $d x / d \tau$ of the 4-velocity in the laboratory frame appear, substitute expressions in terms of the 4-velocities in the rocket frame (inverse Lorentz transformation).   
(4) In (3.25) as thus transformed, demand equality of left and right sides for all values of the $d \overline { { x } } / d \tau$ ,etc.(validity for all test particles).   
(5)In this way arrive at the expressions (3.23) for the $\bar { E }$ and $\bar { \pmb { B } }$ in terms of the $\pmb { { \cal E } }$ and $\pmb { B }$

The contrast in difficulty is obvious!

# $\ S 3 . 4$ .MAXWELL'S EQUATIONS

Turn now from the action of the field on a charge,and ask about the action of a charge on the field,or, more generally,ask about the dynamics of the electromagnetic

# Magnetodynamics derived from magnetostatics

feld, charge or no charge.Begin with the simplest of Maxwel's equations in a specific Lorentz frame, the one that says there are no free magnetic poles:

$$
\nabla \cdot B \equiv \mathrm { d i v } \ : B = \frac { \partial B _ { x } } { \partial x } + \frac { \partial B _ { y } } { \partial y } + \frac { \partial B _ { z } } { \partial z } = 0 .
$$

This statement has to be true in all Lorentz frames. It is therefore true in the rocket frame:

$$
\frac { \partial \overline { { B } } _ { z } } { \partial \overline { { x } } } + \frac { \partial \overline { { B } } _ { y } } { \partial \overline { { y } } } + \frac { \partial \overline { { B } } _ { z } } { \partial \overline { { z } } } = 0 .
$$

For an infinitesimal Lorentz transformation in the $x$ -direction (nonrelativistic velocity $\beta$ ),one has (see Box 2.4 and equations 3.23)

$$
\begin{array} { r l r } & { \overline { { B } } _ { x } = B _ { x } , \qquad \overline { { B } } _ { y } = B _ { y } + \beta E _ { z } , \qquad \overline { { B } } _ { z } = B _ { z } - \beta E _ { y } ; } & \\ & { \frac { \partial } { \partial \overline { { x } } } = \frac { \partial } { \partial x } + \beta \frac { \partial } { \partial t } , \qquad \frac { \partial } { \partial \overline { { y } } } = \frac { \partial } { \partial y } , \qquad \frac { \partial } { \partial \overline { { z } } } = \frac { \partial } { \partial z } . } & \end{array}
$$

Substitute into the condition of zero divergence in the rocket frame. Recover the original condition of zero divergence in the laboratory frame, plus the following additional information (requirement for the vanishing of the coefficient of the arbitrary small velocity $\beta$ ：

$$
\frac { \partial B _ { z } } { \partial t } + \frac { \partial E _ { z } } { \partial y } - \frac { \partial E _ { y } } { \partial z } = 0 .
$$

Had the velocity of transformation been directed in the y- or $z$ directions,a similar equation would have been obtained for $\partial B _ { y } / \partial t$ or $\partial B _ { z } / \partial t$ In the language of threedimensional vectors, these three equations reduce to the one equation

$$
\begin{array} { r } { \frac { \partial \boldsymbol { B } } { \partial t } + \boldsymbol { \nabla } \times \boldsymbol { E } \equiv \frac { \partial \boldsymbol { B } } { \partial t } + \operatorname { c u r l } \boldsymbol { E } = \boldsymbol { 0 } . } \end{array}
$$

Magnetodynamicsand magnetostatics unified in one geometric law

How beautiful that (1) the principle of covariance (laws of physics are the same in every Lorentz reference system, which is equivalent to the geometric view of physics） plus (2） the principle that magnetic tubes of force never end,gives (3) Maxwel's dynamic law for the time-rate of change of the magnetic field! This suggests that the magnetostatic law $\pmb { \nabla } \cdot \pmb { B } = 0$ and the magnetodynamic law $\partial { \pmb B } / \partial t + \pmb { \nabla } \times { \pmb E } = 0$ must be wrapped up together in a single frame-independent, geometric law.In terms of components of the field tensor $\pmb { F } ,$ that geometric law must read

$$
F _ { \alpha \beta , \gamma } + F _ { \beta \gamma , \alpha } + F _ { \gamma \alpha , \beta } = 0 ,
$$

since this reduces to $\pmb { \nabla } \cdot \pmb { B } = 0$ when one takes $\alpha = 1 , \beta = 2 , \gamma = 3$ and it reduces to $\partial { \pmb B } / \partial t + \pmb { \nabla } \times { \pmb E } = 0$ when one sets any index, e.g., $\pmb { \alpha }$ , equal to zero (see exercise 3.7 below). In frame-independent geometric language, this law is written (see $\ S 3 . 5$ ， exercise 3.l4,and Chapter 4 for notation)

and it says,“Take the electromagnetic 2-form $\pmb { F }$ (a geometric object defined even in absence of coordinates); from it construct a new geometric object dF (called the “exterior derivative of $\pmb { F } ^ { \prime }$ ）； $\pmb { d } \pmb { F }$ must vanish. The details of this coordinate-free process will be spelled out in exercise 3.15 and in $\ S 4 . 5$ (track 2).

Two of Maxwell's equations remain: the electrostatic equation

$$
\begin{array} { r } { \pmb { \nabla } \cdot \pmb { E } = 4 \pi \pmb { \rho } , } \end{array}
$$

and the electrodynamic equation

$$
\partial { \pmb { E } } / \partial t - { \pmb { \nabla } } \times { \pmb { B } } = - 4 \pi { \pmb { J } } .
$$

They, like the magnetostatic and magnetodynamic equations, are actually two different parts of a single geometric law. Written in terms of feld components, that law says

Electrodynamics and electrostatics unified in one geometric law

$$
F ^ { \alpha \beta } { } _ { , \beta } = 4 \pi J ^ { \alpha } { } ,
$$

where the components of the “4-current" $\pmb { J }$ are

$$
\begin{array} { c } { { J ^ { 0 } = \rho = \mathrm { c h a r g e ~ d e n s i t y } , } } \\ { { ( J ^ { 1 } , J ^ { 2 } , J ^ { 3 } ) = \mathrm { c o m p o n e n t s ~ o f ~ c u r r e n t ~ d e n s i t y } . } } \end{array}
$$

Writen in coordinate-free, geometric language, this electrodynamic law says

$$
{ \pmb d } ^ { * } { \pmb F } = 4 \pi ^ { * } { \pmb J } \mathrm { o r } , \mathrm { e q u i v a l e n t l y } , \pmb \nabla \cdot { \pmb F } = 4 \pi { \pmb J } .
$$

(For full discussion, see exercise 3.15 and $\ S 4 . 5$ ，which is on Track 2.)

# Exercise 3.7. MAXWELL'S EQUATIONS

Show, by explicit examination of components,that the geometric laws

EXERCISE

$$
F _ { \alpha \beta , \gamma } + F _ { \beta \gamma , \alpha } + F _ { \gamma \alpha , \beta } = 0 , \qquad F ^ { \alpha \beta } { } _ { , \beta } = 4 \pi J ^ { \alpha } ,
$$

do reduce to Maxwel's equations (3.26), (3.31), (3.34), (3.35),as claimed above.

# $\$ 3.5$ WORKING WITH TENSORS

Another mathematical digression is needed. Given an arbitrary tensor field,S,of arbitrary rank (choose rank $= 3$ for concreteness)， one can construct new tensor fields by a variety of operations.

One operation is the gradient $\blacktriangledown$ . (The symbol $\pmb { d }$ is reserved for gradients of scalars, in which case $\mathbf { v } f \equiv \mathbf { d } f$ and for“exterior derivatives of differential forms;”a Track-2

Ways to produce new tensors from old:

Gradient

concept, on which see $\ S 4 . 5 .$ ）Like S,VS is a machine. It has four slots,whereas $\pmb { s }$ has three. It describes how $\pmb { s }$ changes from point to point. Specifically, if one desires to know how the number $\pmb { S } ( \pmb { u } , \pmb { v } , \pmb { w } )$ for fixed $\pmb { u }$ ， $\pmb { \nu } ,$ w changes under a displacement $\pmb { \xi }$ ，one inserts ${ \pmb u } , { \pmb v } , { \pmb w } , { \pmb \xi }$ into the four slots of $\pmb { \triangledown } \pmb { \cal S }$

$$
\begin{array} { r l } & { \nabla S ( u , v , w , \xi ) \equiv \widehat { \circ } _ { \xi } S ( u , v , w ) \mathrm { ~ w i t h ~ } u , v , w \mathrm { ~ f i x e d ~ } } \\ & { \qquad \simeq + \mathrm { ~ } \{ \mathrm { v a l u e ~ o f ~ } S ( u , v , w ) \mathrm { ~ a t ~ t i p ~ o f ~ } \xi \} } \\ & { \qquad - \mathrm { ~ } \{ \mathrm { v a l u e ~ o f ~ } S ( u , v , w ) \mathrm { ~ a t ~ t a i l ~ o f ~ } \xi \} . } \end{array}
$$

In component notation in a Lorentz frame, this says

$$
\begin{array} { l } { { \nabla S ( u , v , w , \xi ) \equiv \hat { \sigma } _ { \xi } ( S _ { \alpha \beta \gamma } u ^ { \alpha } v ^ { \beta } w ^ { \gamma } ) = \left( \frac { \hat { \partial } S _ { \alpha \beta \gamma } } { \partial x ^ { \delta } } \xi ^ { \delta } \right) u ^ { \alpha } v ^ { \beta } w ^ { \gamma } } } \\ { { \mathrm { } } } \\ { { \mathrm { } = S _ { \alpha \beta \gamma , \delta } u ^ { \alpha } v ^ { \beta } w ^ { \gamma } \xi ^ { \delta } . } } \end{array}
$$

Thus, the Lorentz-frame components of VS are nothing but the partial derivatives of the components of $\pmb { s }$ . Notice that the gradient raises the rank of a tensor by l (from 3 to 4 for $\pmb { s }$ ）.

Contraction

Contraction is another process that produces a new tensor from an old one. It seals off ("contracts") two of the old tensor's slots, thereby reducing the rank by two. Specifically, if $\pmb R$ is a fourth-rank tensor and $\pmb { \mathscr { M } }$ is obtained by contracting the first and third slots of $\pmb R$ ,then the output of M is given by (definition!)

$$
M ( u , v ) = \sum _ { \alpha = 0 } ^ { 3 } \bar { R } ( e _ { \alpha } , u , \omega ^ { \alpha } , v ) .
$$

Here ${ \pmb { e } } _ { \alpha }$ and ${ \pmb { \omega } } ^ { \alpha }$ are the basis vectors and l-forms of a specific but arbitrary Lorentz coordinate frame.It makes no difference which frame is chosen; the result willalways be the same (exercise 3.8 below). In terms of components in any Lorentz frame, equation (3.40) says (exercise 3.8)

$$
M ( u , v ) = M _ { \mu \nu } u ^ { \mu } v ^ { \nu } = R _ { \alpha \mu } { } ^ { \alpha } { } _ { \nu } u ^ { \mu } v ^ { \nu } ,
$$

so that

$$
M _ { \mu \nu } = { R _ { \alpha \mu } } _ { \nu } ^ { \alpha } .
$$

Thus, in terms of components, contraction amounts to putting one index up and the other down,and then summing on them.

Divergence is a third process for creating new tensors from old.It is accomplished by taking the gradient, then contracting the gradient's slot with one of the original slots:

(divergence of $\pmb { s }$ on first $\mathbf { \sigma } _ { \mathrm { { s l o t } } } ) \equiv \mathbf { \boldsymbol { v } } \cdot \mathbf { \boldsymbol { s } }$ is a machine such that

$$
\begin{array} { r } { \pmb { \nabla } \cdot \pmb { S } ( \pmb { u } , \pmb { \dot { v } } ) = \pmb { \nabla } \pmb { S } ( \pmb { \omega } ^ { \alpha } , \pmb { u } , \pmb { v } , \pmb { e } _ { \alpha } ) = { S } ^ { \alpha } { } _ { \beta \gamma , \alpha } \pmb { u } ^ { \beta } \pmb { v } ^ { \gamma } ; } \end{array}
$$

i.e. $\pmb { \bigtriangledown } \cdot \pmb { S }$ has components $S ^ { \alpha } { } _ { \beta \gamma , \alpha ^ { . } }$

Transpose is a fourth, rather trivial process for creating'new tensors. It merely interchanges two slots:

Transpose

N obtained by transposing second and third slots of $\pmb { S } \Longrightarrow$

$$
\pmb { N } ( \pmb { u } , \pmb { v } , \pmb { w } ) = \pmb { S } ( \pmb { u } , \pmb { w } , \pmb { v } ) .
$$

Symmetrization and antisymmetrization are fth and sixth processes for producing new tensors from old.A tensor is completely symmetric if its output is unaffected by an interchange of two input vectors or l-forms:

$$
\mathcal { S } ( u , v , w ) = \mathcal { S } ( v , u , w ) = \mathcal { S } ( v , w , u ) = \cdot \cdot \cdot .
$$

Symmetrization and antisymmetrization

It is completely antisymmetric if it reverses sign on each interchange of input

$$
\mathcal S ( u , v , w ) = - \mathcal S ( v , u , w ) = + \mathcal S ( v , w , u ) = \cdot \cdot \cdot .
$$

Any tensor can be symmetrized or antisymmetrized by constructing an appropriate linear combination of it and its transposes; see exercise 3.12.

Wedge product is a seventh process for producing new tensors from old. It is merely an antisymmetrized tensor product: given two vectors ${ \pmb u }$ and $\pmb { v } ,$ ,their wedge product, the “bivector" $\mu \wedge v ,$ is defined by

Wedge product

Bivector

$$
\pmb { \iota } \wedge \pmb { v } \equiv \pmb { \iota } \otimes \pmb { v } - \pmb { v } \otimes \pmb { u } ;
$$

similarly,the“2-form” $\alpha \wedge \beta$ constructed from two l-forms is

2-form

$$
\alpha \wedge \beta \equiv \alpha \otimes \beta - \beta \otimes \alpha .
$$

From three vectors $\psi , v ,$ w one constructs the “triuector”

Trivector

$$
{ \begin{array} { r l } { u \wedge v \wedge w \equiv ( u \wedge v ) \wedge w \equiv u \wedge ( v \wedge w ) } \\ & { \qquad = u \otimes v \otimes w + { \mathrm { t e r m s ~ t h a t ~ g u a r a n t e e ~ c o m p l e t e } } } \\ & { \qquad = u \otimes v \otimes w + v \otimes w \otimes u + w \otimes u \otimes v } \\ & { \qquad - v \otimes u \otimes w - u \otimes w \otimes v - w \otimes v \otimes u . } \end{array} }
$$

From 1-forms $\pmb { \alpha } , \pmb { \beta } , \pmb { \gamma }$ one similarly constructs the“3-forms" $\alpha \wedge \beta \wedge \gamma$ .The wedge product gives a simple way to test for coplanarity (linear dependence) of vectors: if ${ \pmb u }$ and $\pmb { \nu }$ are collinear, so ${ \bf \nabla } \cdot { \bf u } = a { \bf v } _ { \mathrm { : } }$ then

$$
u \wedge v = a v \wedge v = 0 ( { \mathfrak { b } } \mathrm { y } \mathrm { ~ a n t i s y m m e t r y ~ o f ~ } ^ { \ast \ast } \wedge ^ { \prime \ast } ) .
$$

f $\boldsymbol { \mathsf { w } }$ is coplanar with $\pmb { u }$ and $\pmb { v } \ s _ { 0 } \ \pmb { w } = a \pmb { u } + b \pmb { v }$ ("collapsed box"), then

$$
\pmb { w } \wedge \pmb { u } \wedge \pmb { v } = a \pmb { u } \wedge \pmb { u } \wedge \pmb { v } + b \pmb { v } \wedge \pmb { u } \wedge \pmb { v } = 0 .
$$

The symbol $" \wedge "$ is called a“hat” or “wedge”or“exterior product sign."Its properties are investigated in Chapter 4.

Taking the dual is an eighth process for constructing new tensors. It plays aDual fundamental role in Track 2 of this book,but since it is not needed for Track 1, its defnition and properties are treated only in the exercises (3.14 and 3.15).

Because the frame-independent geometric notation is somewhat ambiguous (which slots are being contracted? on which slot is the divergence taken? which slots are being transposed?), one often uses component notation to express coordinate-inde-pendent, geometric relations between geometric objects. For example,

$$
J _ { \beta \gamma } = S ^ { \alpha } { } _ { \beta \gamma , \alpha }
$$

means $\blacktriangleleft$ is a tensor obtained by taking the divergence on the first slot of the tensor $\pmb { S } ^ { \prime \prime }$ Also,

$$
v ^ { \gamma } = ( F _ { \mu \nu } F ^ { \mu \nu } ) ^ { , \gamma } \equiv ( F _ { \mu \nu } F ^ { \mu \nu } ) _ { , \beta } \eta ^ { \beta \gamma }
$$

means $\cdots$ is a vector obtained by(l） constructing the tensor product ${ \pmb F } \otimes { \pmb F }$ of $\pmb { F }$ with itself, (2） contracting ${ \pmb F } \otimes { \pmb F }$ on its first and third slots,and also on its second and fourth,(3) taking the gradient of the resultant scalar function, (4) converting that gradient, which is a l-form, into the corresponding vector."

Index gymnastics

“Index gymnastics,” the technique of extracting the content from geometric equations by working in component notation and rearranging indices as required, must be mastered if one wishes to do diffcult calculations in relativity,special or general. Box 3.3 expounds some of the short cuts in index gymnastics,and exercises 3.8-3.18 offer practice.

# EXERCISES

# Exercise 3.8. CONTRACTION IS FRAME-INDEPENDENT

Show that contraction,as defined in equation (3.40),does not depend on which Lorentz frame ${ \pmb e } _ { \pmb { \alpha } }$ and $\pmb { \omega } ^ { \alpha }$ are taken from.Also show that equation (3.40) implies

$$
{ \pmb M } ( { \pmb u } , { \pmb v } ) = R _ { \alpha \mu } { } ^ { \alpha } { } _ { \nu } u ^ { \mu } v ^ { \nu } .
$$

# Exercise 3.9. DIFFERENTIATION

(a)Justify the formula

$$
d ( u _ { \mu } v ^ { \nu } ) / d \tau = ( d u _ { \mu } / d \tau ) v ^ { \nu } + u _ { \mu } ( d v ^ { \nu } / d \tau ) .
$$

by considering the special case $\mu = 0 , \nu = 1$

(b) Explain why

$$
( T ^ { \alpha \beta } v _ { \beta } ) _ { , \mu } = T ^ { \alpha \beta } { } _ { , \mu } v _ { \beta } + T ^ { \alpha \beta } v _ { \beta , \mu } .
$$

# Exercise 3.10. MORE DIFFERENTIATION

(a) Justify the formula,

$$
d ( u ^ { \mu } u _ { \mu } ) / d \tau = 2 u _ { \mu } ( d u ^ { \mu } / d \tau ) ,
$$

by writing out the summation $u ^ { \mu } u _ { \mu } \equiv \eta _ { \mu \nu } u ^ { \mu } u ^ { \nu }$ explicitly.

(b)Let δ indicate a variation or small change,and justify the formula

$$
\delta ( F _ { \alpha \beta } F ^ { \alpha \beta } ) = 2 F _ { \alpha \beta } \delta F ^ { \alpha \beta } .
$$

(c) Compute $( F _ { \alpha \beta } F ^ { \alpha \beta } ) _ { , \mu } = ?$

<table><tr><td colspan="2">Box 3.3 TECHNIQUES OF INDEX GYMNASTICS</td></tr><tr><td>Equation</td><td>Name and Discussion</td></tr><tr><td>Sβγ = S(wα,e,ey)</td><td>Computing components.</td></tr><tr><td>Saβ= S(wα,wβ,ey)</td><td>Computing other components.</td></tr><tr><td>S = Sβγe wβwY</td><td>Reconstructing the rank-() version of S.</td></tr><tr><td>S= SaβYeeeγ</td><td>Reconstructing the rank-() version of S. [Recall: one does not usually distinguish between the various versions; see equa- tion (3.15) and associated discussion.]</td></tr><tr><td>SaB =nBuSauy</td><td>Raising an index.</td></tr><tr><td>Saμy = nμBSaBy</td><td>Lowering an index.</td></tr><tr><td>M = Sa</td><td>Contraction of S to form a new tensor M.</td></tr><tr><td>Taβ = SaβM</td><td>Tensor product of S with M to form a new tensor T.</td></tr><tr><td>A²= AA</td><td>Squared length of vector A produced by forming tensor product A A and then contracting,which is the same as forming the</td></tr><tr><td>manBY = 8Y</td><td>correspondingl-formAandthenpiercing:A² = (A,A&gt;= AaA. The matrix formed from the metric&#x27;s “covariant components.” lmβll,is the inverse of that formed from its“contravariant components,” Iinβ. Equivalently, raising one index of the</td></tr><tr><td>SBy= N@BY</td><td>metric naβ produces the Kronecker delta. Gradient of N to form a new tensor S.</td></tr><tr><td>R = Nβ</td><td>Divergence of N to form a new tensor R.</td></tr><tr><td>Nβ,y=(nBμNau），= nβμNau</td><td>Taking gradients and raising or lowering indices are operations that commute.</td></tr><tr><td>NY= NaB.nμY</td><td>Contravariant index on a gradient is obtained by raising covari-</td></tr><tr><td>(RMβ)y=Ra,yM+RMβ,Y</td><td>ant index. Gradient of a tensor product; says V(R  M) =</td></tr><tr><td>Gβ=Faβ]三（Faβ-FBa）</td><td>Transpose(VR  M) + R ∀M. Antisymmetrizing a tensor F to produce a new tensor G.</td></tr><tr><td>Hβ=FaB）=（Faβ+Fβa)</td><td>Symmetrizing a tensor F to produce a new tensor H.</td></tr><tr><td>*Jp-= JreμaBY</td><td>Forming the rank-3 tensor that is dual to a vector (exercise</td></tr><tr><td>*Faβ=Fuμvaβ</td><td>3.14). Forming the antisymmetric rank-2 tensor that is dual toa given</td></tr><tr><td>*B=1B^uexμα</td><td>antisymmetric rank-2 tensor (exercise 3.14). Forming the l-form that is dual to an antisymmetric rank-3 tensor (exercise 3.14).</td></tr></table>

# Exercise 3.11. SYMMETRIES

Let $A _ { \mu \nu }$ be an antisymmetric tensor so that $A _ { \mu \nu } = - A _ { \nu \mu }$ and let $S ^ { \mu \nu }$ be a symmetric tensor so that $S ^ { \mu \nu } = S ^ { \nu \mu }$

(a) Justify the equations $A _ { \mu \nu } S ^ { \mu \nu } = 0$ in two ways: first, by writing out the sum explicitly (all sixteen terms) and showing how the terms in the sum cancel in pairs;second,by giving an argument to justify each equals sign in the following string:

$$
A _ { \mu \nu } S ^ { \mu \nu } = - A _ { \nu \mu } S ^ { \mu \nu } = - A _ { \nu \mu } S ^ { \nu \mu } = - A _ { \alpha \beta } S ^ { \alpha \beta } = - A _ { \mu \nu } S ^ { \mu \nu } = 0 .
$$

(b)Establish the following two identites foranyarbitrary tensor $V _ { \mu \nu }$

$$
V ^ { \mu \nu } A _ { \mu \nu } = \frac { 1 } { 2 } ( V ^ { \mu \nu } - V ^ { \nu \mu } ) A _ { \mu \nu } , \qquad V ^ { \mu \nu } S _ { \mu \nu } = \frac { 1 } { 2 } ( V ^ { \mu \nu } + V ^ { \nu \mu } ) S _ { \mu \nu } .
$$

# Exercise 3.12. SYMMETRIZATION AND ANTISYMMETRIZATION

To"symmetrize”a tensor,one averages it with all of its transposes.The components of the new,symmetrized tensor are distinguished by round brackets:

$$
\begin{array} { l } { { \displaystyle V _ { ( \mu ^ { p } ) } \equiv \frac { 1 } { 2 } ( V _ { \mu ^ { p } } + V _ { \nu _ { \mu } } ) } ; } \\ { ~ } \\ { { \displaystyle V _ { ( \mu \nu \lambda ) } \equiv \frac { 1 } { 3 ! } ( V _ { \mu \nu \lambda } + V _ { \nu \lambda \mu } + V _ { \lambda \mu \nu } + V _ { \nu _ { \mu \lambda } } + V _ { \mu \lambda \nu } + V _ { \lambda \nu \mu } ) } . } \end{array}
$$

One “antisymmetrizes” a tensor (square brackets) similarly:

$$
\begin{array} { l } { { \displaystyle V _ { [ \mu \nu ] } \equiv \frac { 1 } { 2 } ( V _ { \mu \nu } - V _ { \nu \mu } ) } ; } \\ { ~ } \\ { { \displaystyle V _ { [ \mu \nu \lambda ] } \equiv \frac { 1 } { 3 ! } ( V _ { \mu \nu \lambda } + V _ { \nu \lambda \mu } + V _ { \lambda \mu } , - V _ { \nu \mu \lambda } - V _ { \mu \lambda \nu } - V _ { \lambda \nu \mu } ) } . } \end{array}
$$

(a) Show that such symmetrized and antisymmetrized tensors are, indeed,symmetric and antisymmetric under interchange of the vectors inserted into their slots:

$$
\begin{array} { r l } & { V _ { ( \alpha \beta \gamma ) } u ^ { \alpha } v ^ { \beta } w ^ { \gamma } = + V _ { ( \alpha \beta \gamma ) } v ^ { \alpha } u ^ { \beta } w ^ { \gamma } = \cdot \cdot \cdot , } \\ & { V _ { [ \alpha \beta \gamma ] } u ^ { \alpha } v ^ { \beta } w ^ { \gamma } = - V _ { [ \alpha \beta \gamma ] } v ^ { \alpha } u ^ { \beta } w ^ { \gamma } = \cdot \cdot \cdot . } \end{array}
$$

(b) Show that a second-rank tensor can be reconstructed from its symmetric and antisymmetric parts,

$$
V _ { \mu \nu } = V _ { ( \mu \nu ) } + V _ { [ \mu \nu ] } ,
$$

but that a third-rank tensor cannot; $V _ { \{ \alpha \beta \gamma \} }$ and $V _ { [ \alpha \beta \gamma ] }$ contain together “less information” than $V _ { \alpha \beta \gamma }$ “Young diagrams"(see,e.g.,Messiah [196l],appendix D) describe other symmetries,more subtle than these two,which contain the missing information.

(c) Show that the electromagnetic field tensor satisfies

$$
F _ { ( \alpha \beta ) } = 0 , \qquad F _ { \alpha \beta } = F _ { [ \alpha \beta ] } .
$$

(d) Show that Maxwell's “magnetic” equations

$$
F _ { \alpha \beta , \gamma } + F _ { \beta \gamma , \alpha } + F _ { \gamma \alpha , \beta } = 0
$$

can be rewritten in the form

$$
F _ { [ \alpha \beta , \gamma ] } = 0 .
$$

# Exercise 3.13. LEVI-CIVITA TENSOR

The“Levi-Civita tensor” $\pmb { \varepsilon }$ in spacetime is a fourth-rank, completely antisymmetric tensor:

Choose an arbitrary but specific Lorentz frame, with ${ \pmb \theta } _ { 0 }$ pointing toward the future and with $\pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ a righthanded set of spatial basis vectors. The covariant components of $\pmb { \varepsilon }$ in this frame are

$$
\varepsilon _ { 0 1 2 3 } = \varepsilon ( e _ { 0 } , e _ { 1 } , e _ { 2 } , e _ { 3 } ) = + 1 .
$$

[Note: In an $_ { n }$ -dimensional space, $\pmb { \varepsilon }$ is the analogous completely antisymmetric rank- $_ n$ tensor. Its components are

$$
\varepsilon _ { 1 2 \ldots , n } = \varepsilon ( e _ { 1 } , e _ { 2 } , \ldots , e _ { n } ) = + 1 ,
$$

when computed on a“positively oriented,”orthonormal basis $\pmb { e } _ { 1 } , \ldots , \pmb { e } _ { n } . ]$

(a) Use the antisymmetry to show that

$$
\begin{array} { c } { \varepsilon _ { \alpha \beta \gamma \delta } = 0 \ \mathrm { u n l e s s } \ \alpha , \beta , \gamma , \delta \ \mathrm { a r e \ a l l \ d i f f e r e n t } , } \\ { { \mathrm { } } } \\ { { \mathrm { } : _ { \pi \ L { 0 } \pi _ { 1 } \pi _ { 2 } \pi _ { 3 } } = \left\{ \begin{array} { l l } { { + 1 \ \mathrm { f o r \ e v e n \ p e r m u t a t i o n s \ o f \ 0 , \ l , \ 2 , \ 3 , \ a n d } } } \\ { { - 1 \ \mathrm { f o r \ o d d \ p e r m u t a t i o n s } . } } \end{array} \right. } } \end{array}
$$

(b) Show that

$$
\varepsilon ^ { \pi _ { 0 } \pi _ { 1 } \pi _ { 2 } \pi _ { 3 } } = - \varepsilon _ { \pi _ { 0 } \pi _ { 1 } \pi _ { 2 } \pi _ { 3 } } .
$$

(c) By means of a Lorentz transformation show that $\varepsilon ^ { \overline { { \alpha } } \overline { { \beta } } \overline { { \gamma \delta } } }$ and $\varepsilon _ { \overline { { { \alpha } } } \overline { { { \beta } } } } \overline { { { \gamma } } } \overline { { { \delta } } }$ have these same values in any other Lorentz frame with $\pmb { e } _ { 0 }$ pointing toward the future and with $\pmb { e } _ { \bar { 1 } } , \ \pmb { e } _ { \bar { 2 } } , \ \pmb { e } _ { \bar { 3 } } \ \cdot$ a righthanded set. Hint: show that

$$
\varepsilon ^ { \alpha \beta \gamma \delta } A _ { \alpha } ^ { \overline { { { 0 } } } } A _ { \beta } ^ { \overline { { { 1 } } } } A _ { \gamma } ^ { \overline { { { 2 } } } } A _ { \delta } ^ { \overline { { { 3 } } } } = - { \operatorname * { d e t } } | A _ { \nu } ^ { \overline { { { \mu } } } } | ;
$$

from $A ^ { T } \eta A = \eta$ ，show that d $\mathsf { e t } | \bar { \Lambda ^ { \mu } } _ { \nu } | = \pm 1$ ； and verify that the determinant is $+ 1$ for transformations between frames with ${ \pmb { e } } _ { 0 }$ and ${ \pmb e } _ { \overline { { 0 } } }$ future-pointing, and with $\pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ and $e _ { \mathrm { { 1 } } } , e _ { \mathrm { { 2 } } } ,$ ${ \pmb e } _ { \overline { { 3 } } }$ righthanded.

(d） What are the components of $\pmb { \varepsilon }$ in a Lorentz frame with past-pointing ${ \pmb e } _ { \bar { 0 } } { \dagger }$ with lefthanded $\mathscr { e } _ { \bar { 1 } } , \mathscr { e } _ { \bar { 2 } } , \mathscr { e } _ { \bar { 3 } } ?$

(e） From the Levi-Civita tensor,one can construct several“permutation tensors.”In index notation:

$$
\begin{array} { c } { { \delta ^ { \alpha \beta \gamma } { } _ { \mu \nu \lambda } \equiv - \varepsilon ^ { \alpha \beta \gamma \rho } \varepsilon _ { \mu \nu \lambda \rho } ; } } \\ { { { } } } \\ { { \delta ^ { \alpha \beta } { } _ { \mu \nu } \equiv { \displaystyle \frac { 1 } { 2 } } \delta ^ { \alpha \beta \lambda } { } _ { \mu \nu \lambda } = - \frac { 1 } { 2 } \varepsilon ^ { \alpha \beta \lambda \rho } \varepsilon _ { \mu \nu \lambda \rho } ; } } \\ { { { } } } \\ { { \delta ^ { \alpha } { } _ { \mu } \equiv { \displaystyle \frac { 1 } { 3 } } \delta ^ { \alpha \beta } { } _ { \mu \beta } = { \displaystyle \frac { 1 } { 6 } } \delta ^ { \alpha \beta \lambda } { } _ { \mu \beta \lambda } = - \frac { 1 } { 6 } \varepsilon ^ { \alpha \beta \lambda \rho } \varepsilon _ { \mu \beta \lambda \rho } . } } \end{array}
$$

Show that:

$$
\delta ^ { \alpha \beta \gamma } { } _ { \mu \nu \lambda } = { \left\{ \begin{array} { l l } { + { \textrm { l i f } } \alpha \beta \gamma { \mathrm { ~ i s ~ a n ~ e v e n ~ p e r m u t a t i o n ~ o f ~ } } \mu \nu \lambda , } \\ { - { \textrm { l i f } } \alpha \beta \gamma { \mathrm { ~ i s ~ a n ~ o d d ~ p e r m u t a t i o n ~ o f ~ } } \mu \nu \lambda , } \\ { 0 { \mathrm { ~ o t h e r w i s e } } ; } \end{array} \right. }
$$

$$
\begin{array} { r l } & { \delta ^ { \alpha \beta } { } _ { \mu \nu } = \delta ^ { \alpha } { } _ { \mu } \delta ^ { \beta } { } _ { \nu } - \delta ^ { \alpha } { } _ { \nu } \delta ^ { \beta } { } _ { \mu } } \\ & { \qquad = \left\{ \begin{array} { l l } { \displaystyle + 1 \mathrm { ~ i f ~ } \alpha \beta \mathrm { ~ i s ~ a n ~ e v e n ~ p e r m u t a t i o n ~ o f ~ } \mu \nu , } \\ { \displaystyle - 1 \mathrm { ~ i f ~ } \alpha \beta \mathrm { ~ i s ~ a n ~ o d d ~ p e r m u t a t i o n ~ o f ~ } \mu \nu , } \\ { \qquad \displaystyle 0 \mathrm { ~ o t h e r w i s e } ; } \end{array} \right. } \\ & { \delta ^ { \alpha } { } _ { \mu } = \left\{ \begin{array} { l l } { \displaystyle + 1 \mathrm { ~ i f ~ } \alpha = \mu , } \\ { \displaystyle 0 \mathrm { ~ o t h e r w i s e } . } \end{array} \right. } \end{array}
$$

Exercise 3.14. DUALS

From any vector $\pmb { J }$ ,any second-rank antisymmetric tensor $\pmb { F } ( F _ { \alpha \beta } = F _ { [ \alpha \beta ] } )$ ,and any third-rank antisymmetric tensor $\pmb { \cal B } ( B _ { \alpha \beta \gamma } = B _ { [ \alpha \beta \gamma ] } )$ ,one can construct new tensors defined by

$$
{ } ^ { * } J _ { \alpha \beta \gamma } = J ^ { \mu } \varepsilon _ { \mu \alpha \beta \gamma } , \qquad { } ^ { * } F _ { \alpha \beta } = \frac 1 2 F ^ { \mu \nu } \varepsilon _ { \mu \nu \alpha \beta } , \qquad { } ^ { * } B _ { \alpha } = \frac 1 { 3 ! } B ^ { \lambda \mu \nu } \varepsilon _ { \lambda \mu \nu \alpha } .
$$

One calls $^ { * }$ the“dual”of ${ \pmb J } , \pmb { \imath F }$ the dual of $\pmb { F } ,$ and $\yen 8$ the dual of $\pmb { \ 8 }$ [A previous and entirely distinct use of the word “dual” $( \ S 2 . 7 )$ called a set of basis one-forms $\{ \pmb { \omega } ^ { \alpha } \}$ dual to a set of basis vectors $\{ \pmb { e } _ { \alpha } \}$ if $\langle { \pmb { \omega } } ^ { \alpha } , { \pmb { e } } _ { \beta } \rangle = \delta ^ { \alpha } { } _ { \beta }$ .Fortunately there are no grounds for confusion between the two types of duality. One relates sets of vectors to sets of l-forms. The other relates antisymmetric tensors of rank $\pmb { p }$ to antisymmetric tensors of rank $4 - p . ]$

(a) Show that

$$
\cdots J = J , \qquad \cdots F = - F , \qquad \cdots B = B .
$$

so (aside from sign） one can recover any completely antisymmetric tensor $\pmb { H }$ from its dual $^ { * } M$ by taking the dual once again, $^ { \ast \ast } M .$ This shows that $\pmb { H }$ and $^ { \ast } M$ contain precisely the same information.

(b) Make explicit this fact of same-information-content by writing out the components $^ \bullet A ^ { \alpha \beta \gamma }$ in terms of $A ^ { \alpha }$ ，also $^ { * } F ^ { \alpha \beta }$ in terms of $F ^ { \alpha \beta }$ also $" B ^ { \alpha }$ in terms of $B ^ { \alpha \beta \Upsilon }$

# Exercise 3.15. GEOMETRIC VERSIONS OF MAXWELL EQUATIONS

Show that, if $\pmb { F }$ is the electromagnetic field tensor, then $\pmb { \nabla } \pmb { \cdot } \pmb { \cdot } \pmb { F } = 0$ is a geometric frame-independent version of the Maxwell equations

$$
F _ { \alpha \beta , \gamma } + F _ { \beta \gamma , \alpha } + F _ { \gamma \alpha , \beta } = 0 .
$$

Similarly show that $\pmb { \nabla } \cdot \pmb { F } = 4 \pi \pmb { J }$ (divergence on second slot of $\pmb { F }$ ） is a geometric version of $F ^ { \alpha \beta } { } _ { , \beta } = 4 \pi J ^ { \alpha }$

# Exercise 3.16. CHARGE CONSERVATION

From Maxwel's equations $F ^ { \alpha \beta } { } _ { , \beta } = 4 \pi J ^ { \alpha }$ ，derivehe“eqatiofcargecoseatio”

$$
{ J ^ { \alpha } } _ { , \alpha } = 0 .
$$

Show that this equation does, indeed, correspond to conservation of charge. It will be studied further in Chapter 5.

# Exercise 3.17. VECTOR POTENTIAL

The vector potential $\pmb { A }$ of electromagnetic theory generates the electromagnetic field tensor via the geometric equation

$$
{ \pmb F } = - ( \mathrm { a n t i s y m m e t r i c ~ p a r t ~ o f ~ } { \pmb v } { \pmb A } ) ,
$$

$$
F _ { \mu p } = A _ { \nu , \mu } - A _ { \mu , \nu } .
$$

(a) Show that the electric and magnetic felds in a specific Lorentz frame are given by

$$
\pmb { { \cal B } } = \pmb { \nabla } \times \pmb { A } , \pmb { { \cal E } } = - \partial \pmb { A } / \partial t - \pmb { \nabla } \pmb { A } ^ { 0 } .
$$

(b) Show that $\pmb { \ F }$ will satisfy Maxwel's equations if and only if $\pmb { A }$ satisfies

$$
{ \cal A } ^ { \alpha , \mu } { } _ { , \mu } - { \cal A } ^ { \mu } { } _ { , \mu } { } ^ { , \alpha } = - 4 \pi J ^ { \alpha } { } .
$$

(c) Show that “gauge transformations"

$$
A _ { \mathrm { N E W } } = A _ { \mathrm { 0 L D } } + d \phi , \qquad \phi = \mathrm { a r b i t r a r y ~ f u n c t i o n } ,
$$

leave $\pmb { F }$ unaffected.

(d) Show that one can adjust the gauge so that

$$
\begin{array} { c } { { \pmb { \nabla } \cdot \pmb { A } = 0 ~ ( \mathrm { ^ { * } L o r e n t z ~ \underline { { { g } } } a u g e ^ { * } } ) , } } \\ { { \sqcup _ { \pmb { A } } = - 4 \pi \pmb { J } . } } \end{array}
$$

Here $\sqcap$ is the wave operator ("d'Alembertian"):

$$
\begin{array} { r } { \bigtriangledown \pmb { A } = A ^ { \alpha , \mu } , } \end{array}
$$

# Exercise 3.18. DIVERGENCE OF ELECTROMAGNETIC STRESS-ENERGY TENSOR

From an electromagnetic field tensor $\pmb { F } ,$ one constructs a second-rank,symmetric tensor $\pmb { \tau }$ ("stress-energy tensor,” to be studied in Chapter 5) as follows:

$$
T ^ { \mu \nu } = \frac { 1 } { 4 \pi } \Big ( F ^ { \mu \alpha } { F ^ { \nu } } _ { \alpha } - \frac { 1 } { 4 } \eta ^ { \mu \nu } F _ { \alpha \beta } F ^ { \alpha \beta } \Big ) .
$$

As an exercise in index gymnastics:

(a) Show that $\pmb { \nabla } \pmb { \cdot } \pmb { \tau }$ has components

$$
T ^ { \mu \nu } { } _ { , \nu } = \frac { 1 } { 4 \pi } \bigg [ F ^ { \mu \alpha } { } _ { , \nu } F _ { \alpha } ^ { \nu } + F ^ { \mu \alpha } F _ { \alpha , \nu } ^ { \nu } - \frac { 1 } { 2 } F _ { \alpha \beta } { } ^ { , \mu } F ^ { \alpha \beta } \bigg ] .
$$

(b)Manipulate this expression into the form

$$
T _ { \mu } ^ { \nu } { } _ { , \nu } ^ { \nu } = \frac 1 { 4 \pi } \biggl [ - F _ { \mu \alpha } F ^ { \alpha \nu } { } _ { , \nu } - \frac 1 2 F ^ { \alpha \beta } ( F _ { \alpha \beta , \mu } + F _ { \mu \alpha , \beta } + F _ { \beta \mu , \alpha } ) \biggr ] ;
$$

note that the first term of (3.62) arises directly from the second term of (3.61).

(c) Use Maxwell's equations to conclude that

$$
T ^ { \mu \nu } { } _ { , \nu } = - F ^ { \mu \alpha } J _ { \alpha } .
$$

CHAPTER 4

# ELECTROMAGNETISM AND DIFFERENTIAL FORMS

Theether trembledat hisagitations In a manner so familiar that I only need to say, In accordance with Clerk Maxwell's six equations It tickled peoples‘optics far away. You can feel the way it's done, You may trace them as they rundy by dy less dβ by dz is equal KdX/dt..

While the curl of (X,Y, Z) is the minus d/dt of the vector (a, b,c):

From The Revolution of the Corpuscle, written by A.A.Robb   
(to the tune of The Interfering Parrott)   
for a dinner of the research students of the Cavendish Laboratory in the days of the old mathematics.

This chapter is all Track 2. It is needed as preparation for \$\$14.5 and 14.6 (computation of curvature using differential forms) and for Chapter 15 (Bianchi identities and boundary of a boundary),but is not needed for the rest of the book.

# \$4.1. EXTERIOR CALCULUS

Stacks of surfaces, individually or intersecting to make “honeycombs,”"egg crates,” and other such structures ("differential formns"), give unique insight into the geometry of electromagnetism and gravitation.However, such insight comes at some cost in time.Therefore, most readers should skip this chapter and later material that depends on it during a first reading of this book.

Analytically speaking, differential forms are completely antisymmetric tensors; pictorially speaking, they are intersecting stacks of surfaces. The mathematical formalism for manipulating differential forms with ease,called “exterior calculus,” is summarized concisely in Box 4.l; its basic features are illustrated in the rest of this chapter by rewriting electromagnetic theory in its language. An effective way to tackle this chapter might be to(l) scan Box 4.l to get the flavor of the formalism; (2) read the rest of the chapter in detail; (3) restudy Box 4.l carefully; (4) get practice in manipulating the formalism by working the exercises.\*

# Box 4.1 DIFFERENTIAL FORMS AND EXTERIOR CALCULUS IN BRIEF

The fundamental definitions and formulas of exterior calculus are summarized here for ready reference. Each item consists of a general statement (at left of page) plus a leading application (at right of page). This formalism is applicable not only to spacetime, but also to more general geometrical systems (see heading of each section). No attempt is made here to demonstrate the internal consistency of the formalism, nor to derive it from any set of definitions and axioms. For a systematic treatment that does so, see, e.g., Spivak (l965),or Misner and Wheeler (1957).

# A. Algebra l (applicable to any vector space)

1. Basis 1-forms.

a. Coordinate basis $\pmb { \omega } ^ { j } = \pmb { d x } ^ { j }$ $( j$ tells which 1-form, not which component). b. General basis $\omega ^ { j } = L _ { \boldsymbol { k } ^ { \prime } } ^ { j } d \boldsymbol { x } ^ { \boldsymbol { k } ^ { \prime } }$ .

An application

Simple basis l-forms for analyzing Schwarzschild geometry around static spherically symmetric center of attraction:

$$
\begin{array} { r l } & { \pmb { \omega } ^ { 0 } = ( 1 - 2 m / r ) ^ { 1 / 2 } \pmb { d } t ; } \\ & { \pmb { \omega } ^ { 1 } = ( 1 - 2 m / r ) ^ { - 1 / 2 } \pmb { d } r ; } \\ & { \pmb { \omega } ^ { 2 } = r \pmb { d } \theta ; } \\ & { \pmb { \omega } ^ { 3 } = r \sin \theta \pmb { d } \phi . } \end{array}
$$

2.General p-form (or p-vector) is a completely antisymmetric tensor of rank $( \boldsymbol { \mathsf { \Sigma } } _ { p } ^ { 0 } )$ [or $\left( _ { 0 } ^ { p } \right) ]$ . It can be expanded in terms of wedge products (see $\ S 3 . 5$ and exercise 4.12):

$$
\begin{array} { c } { { \pmb { \alpha } = \displaystyle \frac { 1 } { p ! } \alpha _ { i _ { 1 } i _ { 2 } \ldots i _ { p } } \pmb { \omega } ^ { i _ { 1 } } \wedge \pmb { \omega } ^ { i _ { 2 } } \wedge \cdot \cdot \cdot \wedge \pmb { \omega } ^ { i _ { p } } } } \\ { { \equiv \alpha _ { | i _ { 1 } i _ { 2 } \ldots i _ { p } | } \pmb { \omega } ^ { i _ { 1 } } \wedge \pmb { \omega } ^ { i _ { 2 } } \wedge \cdot \cdot \cdot \wedge \pmb { \omega } ^ { i _ { p } } . } } \end{array}
$$

(Note: Vertical bars around the indices mean sum-

mation extends only over $i _ { 1 } < i _ { 2 } < \ldots < i _ { p } . )$

Two applications Energy-momentum l-form is of type $\pmb { \alpha } = \alpha _ { i } \pmb { \omega } ^ { i }$ or

$$
p = - E d t + p _ { x } d x + p _ { y } d y + p _ { z } d z .
$$

Faraday is a 2-form of type $\beta = \beta _ { \vert \mu \nu \vert } \omega ^ { \mu } \wedge \omega ^ { \nu }$ or in flat spacetime

$$
\begin{array} { l } { F = - E _ { z } d t \wedge d x - E _ { y } d t \wedge d y - E _ { z } d t \wedge d z } \\ { \qquad + B _ { z } d y \wedge d z + B _ { y } d z \wedge d x + B _ { z } d x \wedge d y } \end{array}
$$

3. Wedge product.

All familiar rules of addition and multiplication hold,such as

$$
\begin{array} { c } { { ( a \pmb { \alpha } + b \pmb { \beta } ) \wedge \gamma = a \pmb { \alpha } \wedge \gamma + b \pmb { \beta } \wedge \pmb { \gamma } , } } \\ { { ( \pmb { \alpha } \wedge \pmb { \beta } ) \wedge \pmb { \gamma } = \pmb { \alpha } \wedge ( \pmb { \beta } \wedge \pmb { \gamma } ) \equiv \pmb { \alpha } \wedge \pmb { \beta } \wedge \gamma , } } \end{array}
$$

except for a modified commutation law between a $p$ form $\pmb { \alpha }$ and a $q$ form $\pmb { \beta }$ ：

$$
\begin{array} { r } { \frac { \alpha } { p } \wedge \beta = ( - 1 ) ^ { p q } \beta \wedge \frac { \alpha } { p } . } \end{array}
$$

Applications to $^ { I }$ -forms ${ \pmb { a } } , { \pmb { \beta } }$ ：

$$
\begin{array} { c } { { \pmb { \alpha } \wedge \beta = - \pmb \beta \wedge \pmb \alpha , \qquad \pmb \alpha \wedge \pmb \alpha = 0 ; } } \\ { { \pmb \alpha \wedge \pmb \beta = ( \alpha _ { j } \pmb \omega ^ { j } ) \wedge ( \beta _ { k } \pmb \omega ^ { k } ) = \alpha _ { j } \beta _ { k } \pmb \omega ^ { j } \wedge \pmb \omega ^ { k } } } \\ { { = \displaystyle \frac { 1 } { 2 } ( \alpha _ { j } \beta _ { k } - \beta _ { j } \alpha _ { k } ) \pmb \omega ^ { j } \wedge \pmb \omega ^ { k } . } } \end{array}
$$

4. Contraction of p-form on p-vector.

$$
\begin{array} { r l } & { \quad ^ { \circ } p ^ { \prime } \circ ^ { \prime } } \\ & { = \alpha _ { | i _ { 1 } \dots i _ { p } | } A ^ { | j _ { 1 } \dots j _ { p } | } \langle { \underline { { \omega } } } ^ { i _ { 1 } } \wedge \cdot \cdot \cdot \wedge \omega ^ { i _ { p } } , \pmb { e } _ { j _ { 1 } } \wedge \cdot \cdot \cdot \wedge \pmb { e } _ { j _ { p } } \rangle } \\ & { \qquad [ \equiv \delta _ { j _ { 1 } \dots j _ { p } } ^ { i _ { 1 } \dots i _ { p } } \mathrm { ~ ( s e e ~ e x e r c i s e s ~ 3 . 1 3 ~ a n d ~ 4 . 1 2 ) ] ~ } } \\ & { = \alpha _ { | i _ { 1 } \dots i _ { p } | } A ^ { i _ { 1 } \dots i _ { p } } . } \end{array}
$$

Four applications

a. Contraction of a particle's energy-momentum 1-form ${ \pmb p } = p _ { \alpha } { \pmb \omega } ^ { \alpha }$ with 4-velocity $\pmb { \mu } = \pmb { u } ^ { \alpha } \pmb { \mathcal { e } } _ { \alpha }$ of observer (a 1-vector):

$$
- \langle p , u \rangle = - p _ { \alpha } u ^ { \alpha } = { \mathrm { e n e r g y ~ o f ~ p a r t i c l e } } .
$$

b.Contraction of Faraday 2-form F with bivector δP > △P [where δP = (dP/d>_)△λ1 and △P = $( d \mathcal { P } / d \lambda _ { 2 } ) \varDelta \lambda _ { 2 }$ are two infinitesimal vectors in a 2-surface $\mathcal { P } ( \lambda _ { 1 } , \lambda _ { 2 } )$ ,and the bivector represents the surface element they span] is the magnetic flux $\boldsymbol { \varPhi } = \langle \boldsymbol { F } , \delta \mathcal { P }$ $\wedge \ 4 \mathcal { P } \rangle$ through that surface element.

c. More generally, a $p$ -dimensional parallelepiped with vectors $a _ { 1 } , a _ { 2 } , \ldots , a _ { p }$ for legs has an oriented volume described by the “simple"p-vector a1 ^ a2 ^ . ap (oriented because interchange of two legs changes its sign). An egg-crate type of structure with walls made from the hyperplanes of $p$ different 1-forms $\pmb { \sigma } ^ { 1 }$ ，

$\pmb { \sigma } ^ { 2 } , \ldots , \pmb { \sigma } ^ { p }$ is described by the“simple" $p$ -form $\pmb { \sigma } ^ { 1 }$ $\wedge \sigma ^ { 2 } \wedge \ . . . \wedge \ \sigma ^ { p }$ The number of cells of $\pmb { \sigma } ^ { 1 } \wedge$ $\sigma ^ { 2 } \wedge \dots \wedge \sigma ^ { p }$ sliced through by the infinitesimal $p$ -volume $a _ { 1 } \wedge a _ { 2 } \wedge \dots \wedge a _ { p }$ is

$$
\langle \pmb { \sigma } ^ { 1 } \wedge \pmb { \sigma } ^ { 2 } \wedge \dots \wedge \pmb { \sigma } ^ { p } , \pmb { a } _ { 1 } \wedge \pmb { a } _ { 2 } \wedge \dots \wedge \pmb { a } _ { p } \rangle .
$$

d. The Jacobian determinant of a set of p functions $f ^ { k } ( x ^ { 1 } , \ldots , x ^ { n } )$ with respect to $p$ of their arguments is

$$
{ \begin{array} { r } { \left. d f ^ { 1 } \wedge d f ^ { 2 } \wedge \ \cdot \ \cdot \ \wedge \ d f ^ { p } , { \frac { \partial { \mathcal { S } } } { \partial x ^ { 1 } } } \wedge { \frac { \partial { \mathcal { S } } } { \partial x ^ { 2 } } } \wedge \ \cdot \ \cdot \ \wedge \ { \frac { \partial { \mathcal { P } } } { \partial x ^ { p } } } \right. } \\ { = \operatorname* { d e t } { \left\| \left( { \frac { \partial f ^ { k } } { \partial x ^ { j } } } \right) \right\| } \equiv { \frac { \partial ( f ^ { 1 } , f ^ { 2 } , \cdot \ \cdot \ , f ^ { p } ) } { \partial ( x ^ { 1 } , x ^ { 2 } , \cdot \ . \ . \ , x ^ { p } ) } } . } \end{array} }
$$

5. Simple forms.

a. A simple $p$ -form is one that can be written as a wedge product of $p$ 1-forms:

$$
\underset { p } { \pmb \sigma } = \underset { \ b { \alpha } } { \pmb \alpha } \wedge \underset { \ b { \beta } } { \pmb \beta } \wedge \underset { \ast \ b { \cdots } } { \cdot \cdot \cdot } \wedge \underset { \ b { \gamma } } { \pmb \gamma } .
$$

b. A simple $p$ -form $\pmb { \alpha } \wedge \pmb { \beta } \wedge \dots \wedge \pmb { \gamma }$ is represented by the intersecting families of surfaces of ${ \pmb { a } } , { \pmb { \beta } } , \dots , { \pmb { \gamma } }$ (egg-crate structure) plus a sense of circulation (orientation).

Applications:

a. In four dimensions (e.g.,spacetime) all O-forms, 1- forms,3-forms,and 4-forms are simple. A 2-form $\pmb { F }$ is generally a sum of two simple forms, e.g., $\pmb { F } =$ $- e d t \wedge d x + h d y \wedge d z$ it is simple if and only if $\pmb { F } \wedge \pmb { F } = 0$

b. A set of 1-forms ${ \pmb { a } } , { \pmb { \beta } } , \dots , { \pmb { \gamma } }$ is linearly dependent (one a linear combination of the others） if and only if

$$
\alpha \wedge \beta \wedge \dots \wedge \gamma = 0
$$

(egg crate collapsed).

# B. Exterior Derivative (applicable to any “differentiable manifold," with or without metric)

1. d produces a $( p + 1 )$ -form do from a $p$ -form $\pmb { \sigma }$

2. Effect of $\pmb { d }$ is defined by induction using the

Box 4.1 (continued)

(Chapter 2） definition of $\pmb { d f }$ and $f$ a function (0- form), plus

$$
\begin{array} { c } { { d ( \underline { { { \alpha } } } \wedge \underline { { { \beta } } } ) = d \alpha \wedge \beta + ( - 1 ) ^ { p } \alpha \wedge d \beta , } } \\ { { { } } } \\ { { d ^ { 2 } = d d = 0 . } } \end{array}
$$

Two applications

$$
d ( \alpha \wedge d \beta ) = d \alpha \wedge d \beta .
$$

For the $p$ -form $\pmb { \phi }$ ,with

$$
\phi = \phi _ { \mid i _ { 1 } . . . i _ { p } \mid } d x ^ { i _ { 1 } } \wedge . . . \wedge d x ^ { i _ { p } } ,
$$

one has (alternative and equivalent definition of $\pmb { d } \phi$ ）

$$
d \phi = d \phi _ { | i _ { 1 } . . . i _ { p } | } \wedge d x ^ { i _ { 1 } } \wedge \cdot \cdot \cdot \wedge d x ^ { i _ { p } } .
$$

# C. Integration (applicable to any “differentiable manifold," with or without metric)

# 1. Pictorial interpretation.

Text and pictures of Chapter 4 interpret $\scriptstyle \int \pmb { \alpha }$ (integral of specified l-form $\pmb { \alpha }$ along specified curve from specified starting point to specified end point) as “number of $\pmb { \alpha }$ -surfaces pierced on that route"; similarly, they interpret $\textstyle \int \phi$ (integral of specified 2-form $\pmb { \phi }$ over specified bit of surface on which there is an assigned sense of circulation or “orientation") as “number of cells of the honeycomb-like structure $\pmb { \phi }$ cut through by that surface”; similarly for the egg-crate-like structures that represent 3- forms; etc.

2. Computational rules for integration. To evaluate $\scriptstyle \int \pmb { \alpha }$ ,the integral of a $p$ -form

$$
\alpha = \alpha _ { | i _ { 1 } . . . i _ { p } | } ( x ^ { 1 } , . . . , x ^ { n } ) d x ^ { i _ { 1 } } \wedge . . . \wedge d x ^ { i _ { p } } ,
$$

over a $p$ -dimensional surface, proceed in two steps.

a. Substitute a parameterization of the surface,

$$
x ^ { k } ( \lambda ^ { 1 } , \ldots , \lambda ^ { p } )
$$

into $\pmb { \alpha }$ ,and collect terms in the form

$$
\alpha = a ( \lambda ^ { j } ) d \lambda ^ { 1 } \wedge . . . \wedge d \lambda ^ { p }
$$

(this is $\pmb { \alpha }$ viewed as a $\pmb { p }$ form in the $p$ -dimensional surface);

b. Integrate

$$
\int \alpha = \int a ( \lambda ^ { j } ) d \lambda ^ { 1 } d \lambda ^ { 2 } \dots d \lambda ^ { p }
$$

using elementary definition of integration.

Example: See equations (4.12) to (4.14).

3. The differential geometry of integration. Calculate $\scriptstyle \int \pmb { \alpha }$ for a $p$ -form $\pmb { \alpha }$ as follows.

a. Choose the $p$ -dimensional surface $\mathcal { S }$ over which to integrate.

b. Represent $s$ by a parametrization giving the generic point of the surface as a function of the parameters, $\mathcal { P } ( \lambda ^ { 1 } , \lambda ^ { 2 } , \dots \lambda ^ { p } )$ .This fixes the orientation. The same function with $\lambda ^ { 1 }  \lambda ^ { 2 }$ ， $\mathcal { P } ( \lambda ^ { 2 } , \lambda ^ { 1 } , \dots , \lambda ^ { p } )$ ,describes a different (i.e., oppositely oriented) surface, $- \mathcal { S } _ { }$

c. The infinitesimal parallelepiped

$$
\left( { \frac { \partial { \mathcal { P } } } { \partial \lambda ^ { 1 } } } A \lambda ^ { 1 } \right) \wedge \left( { \frac { \partial { \mathcal { P } } } { \partial \lambda ^ { 2 } } } A \lambda ^ { 2 } \right) \wedge \ \cdots \wedge \ \left( { \frac { \partial { \mathcal { P } } } { \partial \lambda ^ { p } } } A \lambda ^ { p } \right)
$$

is tangent to the surface. The number of cells of $\pmb { \alpha }$ it slices is

$$
\begin{array} { r } { \left. \alpha , \frac { \partial \mathcal { P } } { \partial \lambda ^ { 1 } } \wedge \ \cdot \ \cdot \ \wedge \ \frac { \partial \mathcal { P } } { \partial \lambda ^ { p } } \right. \ \varDelta \lambda ^ { 1 } \cdot \ . \ . \ \varDelta \lambda ^ { p } . } \end{array}
$$

This number changes sign if two of the vectors $\partial \mathcal { P } / \partial \lambda ^ { k }$ are interchanged, as for an oppositely oriented surface.

d. The above provides an interpretation motivating the definition

$$
\begin{array} { r } { \int \alpha \equiv \int \int \cdots \int \left. \alpha , \frac { \partial \mathcal { S } } { \partial \lambda ^ { 1 } } \wedge \frac { \partial \mathcal { S } } { \partial \lambda ^ { 2 } } \wedge \ \cdots \wedge \frac { \partial \mathcal { S } } { \partial \lambda ^ { p } } \right. } \\ { d \lambda ^ { 1 } d \lambda ^ { 2 } \ldots d \lambda ^ { p } . } \end{array}
$$

This definition is identified with the computational rule of the preceding section (C.2） in exercise 4.9.

Integrate a gradient df along a curve, $\mathcal { P } ( \lambda )$ from ${ \mathcal { P } } ( 0 )$ to ${ \mathcal { P } } ( 1 )$ ：

$$
\begin{array} { l } { { \displaystyle { \int } d f = \int _ { 0 } ^ { 1 } \langle d f , d \phi ^ { \rho } / d \lambda \rangle d \lambda = \int _ { \cdot } ^ { 1 } \left( d f / d \lambda \right) d \lambda } } \\ { { \displaystyle ~ = f [ \mathcal { O } ( 1 ) ] - f [ \mathcal { P } ( 0 ) ] . } } \end{array}
$$

e. Three different uses for symbol “d': First, lightface $d$ in explicit derivative expressions such as

# Box 4.1 (continued)

$d / d a$ ,or $d f / d a$ or $d \tilde { \mathscr { P } } / d a$ .neither numerator nor denominator alone has any meaning, but only the full string of symbols.Second, lightface $d$ inside an integral sign; e.g., Sfda. This is an instruction to perform integration,and has no meaning whatsoever without an integral sign; $^ { * 6 } \mathrm { f } \ldots d . \ldots ^ { 3 }$ ’ lives as an indivisible unit. Third, sans-serif $\pmb { d }$ e.g., $\pmb { d }$ alone, or $d f ,$ or da. This is an exterior derivative,which converts a $p$ -form into a $( p + 1 )$ -form. Sometimes lightface $^ { d }$ is used for the same purpose. Hence, $^ { d }$ alone, or $d f ,$ or $d x$ ,is always an exterior derivative unless coupled to an $\textstyle \int$ sign (second use),or coupled to a / sign (first use).

4. The generalized Stokes theorem (see Box 4.6).

a. Let $\partial \mathcal { V }$ be the closed $p$ -dimensional boundary of a $( p + 1 )$ -dimensional surface $\mathcal { V }$ Let $\pmb { \sigma }$ be a $p$ -form defined throughout $\mathcal { V }$

Then

$$
\boxed { \int _ { \mathcal { T } ^ { \prime } } d \sigma = \int _ { \partial \mathcal { V } } \sigma }
$$

[integral of $p$ -form $\pmb { \sigma }$ over boundary $\partial \mathcal { V }$ equals integral of $( p + 1 )$ -form dg over interior $\mathcal { V } ]$ b. For the sign to come out right, orientations of $\mathcal { V }$ and $\partial \mathcal { V }$ must agree in this sense: choose coordinates $y ^ { 0 } , y ^ { 1 } , \ldots , y ^ { p }$ on a portion of $\mathcal { V }$ ， with $y ^ { 0 }$ specialized so $y ^ { 0 } \leq 0$ in $\mathcal { V }$ and $y ^ { 0 } = 0$ at the boundary $\partial \mathcal { V }$ ； then the orientation

$$
\frac { \partial \mathcal { P } } { \partial y ^ { 0 } } \wedge \frac { \partial \mathcal { P } } { \partial y ^ { 1 } } \wedge ~ . ~ . ~ . ~ \wedge \frac { \partial \mathcal { P } } { \partial y ^ { p } }
$$

for $\mathcal { V }$ demands the orientation

$$
{ \frac { \partial { \mathcal { P } } } { \partial y ^ { 1 } } } \wedge \dots \wedge { \frac { \partial { \mathcal { P } } } { \partial y ^ { p } } }
$$

for $\partial \mathcal { V }$

c. Note: For a nonorientable surface,such as a Mobius strip, where a consistent and continuous choice of orientation is impossible, more intricate mathematics is required to give a definition of $" \partial ^ { , }$ for which the Stokes theorem holds.

Applications: Includes as special cases all integral theorems for surfaces of arbitrary dimension in spaces of arbitrary dimension, with or without metric, generalizing all versions of theorems of Stokes and Gauss. Examples:

a. $\mathcal { V }$ a curve, $\partial \mathcal { V }$ its endpoints, ${ \pmb \sigma } = f$ a 0-form (function):

$$
\int _ { \mathcal { V } } \ d f = \int _ { 0 } ^ { 1 } \left( d f / d \lambda \right) d \lambda = \int _ { \partial \mathcal { V } } f = f ( 1 ) - f ( 0 ) .
$$

b. $\mathcal { V }$ a 2-surface in 3-space, $\partial \mathcal { V }$ its closed-curve boundary, $\pmb { \nu }$ a l-form; translated into Euclidean vector notation, the two integrals are

$$
\int _ { \mathcal { V } } \ d \pmb { v } = \int _ { \mathcal { V } } \ ( \pmb { \nabla } \times \pmb { \nu } ) \cdot d \pmb { S } ; \int _ { \partial \mathcal { V } } \pmb { v } = \int _ { \partial \mathcal { V } } \pmb { \nu } \cdot d \pmb { l } .
$$

c. Other applications in $\ S \ S .$ ,20.2,20.3，20.5，and exercises 4.10,4.11, 5.2,and below.

D. Algebra I (applicable to any vector space with metric)

1. Norm of a p-form.

$$
\begin{array} { r } { | | \pmb { \alpha } | | ^ { 2 } \equiv \alpha _ { | i _ { 1 } . . . i _ { p } | } \alpha ^ { i _ { 1 } . . . i _ { p } } . } \end{array}
$$

Two applications: Norm of a 1-form equals its squared length, $| | { \pmb { \alpha } } | | ^ { 2 } = { \pmb { \alpha } } \cdot { \pmb { \alpha } }$ Norm of electromagnetic 2-form Or Faraday: $\| \pmb { F } | ^ { 2 } = B ^ { 2 } - E ^ { 2 }$

2. Dual of a p-form.

a. In an $\pmb { n }$ -dimensional space, the dual of a $p$ -form $\pmb { \alpha }$ is the $( n - p )$ -form $^ * { \pmb { \alpha } }$ ，with components

$$
( ^ { \ast } \alpha ) _ { k _ { 1 } \ldots k _ { n - p } } = \alpha ^  \{ i _ { 1 } \ldots i _ { p } \ : \epsilon _ { i _ { 1 } \ldots i _ { p } k _ { 1 } \ldots k _ { n - p } } .
$$

b. Properties of duals:

$$
{ \begin{array} { r l } & { * * \alpha = ( - 1 ) ^ { p - 1 } \alpha { \mathrm { ~ i n ~ } } \mathfrak { s p a c e t i m e } ; } \\ & { \alpha \wedge { ^ * \alpha } = | | \alpha | | ^ { 2 } \varepsilon { \mathrm { ~ i n ~ g e n e r a l } } . } \end{array} }
$$

c. Note: the definition of $\pmb { \varepsilon }$ (exercise 3.13) entails choosing an orientation of the space,i.e.,deciding which orthonormal bases (l） are“righthanded"and thus (2) have $\pmb { \varepsilon } ( \pmb { e } _ { 1 } , \ldots , \pmb { e } _ { n } ) = + 1$

Applications

a. For $f$ a 0-form, $\mathbf { \nabla } ^ { * } f = f \bar { \pmb \varepsilon }$ and $\begin{array} { r } { \mathcal { f } f d ( \mathrm { v o l u m e } ) = \mathcal { f } ^ { * } f . } \end{array}$ b. Dual of charge-current 1-form J is charge-current 3-form $^ { * } J$ The total charge $Q$ in a 3-dimensional hypersurface region $s$ is

$$
Q ( \mathcal { S } ) = \int _ { \mathcal { S } } \mathbf { \Psi } ^ { * } \mathbf { J } .
$$

Conservation of charge is stated locally by ${ \pmb d } ^ { * } { \pmb J } = 0$ Stokes' Theorem goes from this differential conservation law to the integral conservation law,

$$
0 = \int _ { \mathcal { V } } \mathbf { \nabla } d ^ { * } \mathbf { J } = \int _ { \partial \mathcal { T } } \mathbf { \nabla } ^ { * } \mathbf { J } .
$$

This law is of most interest when $\partial ^ { \aa } \mathcal { V } = \mathcal { S } _ { 2 } - \mathcal { S } _ { 1 }$ consists of the future $\mathcal { S } _ { 2 }$ and past $\mathcal { S } _ { 1 }$ boundaries of a spacetime region, in which case it states $Q ( \mathcal { S } _ { 2 } ) =$ $\boldsymbol { Q } ( \mathcal { S } _ { 1 } )$ ； see exercise 5.2.

c. Dual of electromagnetic field tensor $\pmb { F } =$ Faraday is ${ \pmb F } =$ Maxwell. From the ${ d ^ { * } } F = 4 \pi ^ { * } J$ Maxwell equation, find $\begin{array} { r } { 4 \pi Q = 4 \pi \int _ { \mathcal { S } } \ast \pmb { J } = \int _ { \mathcal { S } } \pmb { d } ^ { \ast } \pmb { F } = \int _ { \partial \mathcal { S } } \ast \pmb { F } . } \end{array}$

3.Simple forms revisited.

a. The dual of a simple form is simple.

b. Egg crate of $^ * { \pmb { \sigma } }$ is perpendicular to egg crate of $\pmb { \sigma } = \pmb { \alpha } \wedge \pmb { \beta } \wedge \dots \wedge \pmb { \mu }$ in this sense:

(l） pick any vector $\pmb { \nu }$ lying in intersection of surfaces of $\pmb { \sigma }$

$$
( \langle \alpha , V \rangle = \langle \beta , V \rangle = \dots = \langle \mu , V \rangle = 0 ) ;
$$

(2） pick any vector W lying in intersection ofsurfaces of ${ \ast } _ { \sigma }$ ；

(3）then $v$ and $\pmb { w }$ are necessarily perpendicular: $\pmb { V } \cdot \pmb { W } = 0$

Example: $\sigma = 3 \mathrm { ~ } d t$ is a simple l-form in spacetime.

a. ${ } ^ { * } \sigma = - 3 \ d x \ \wedge$ dy $\wedge$ dz is a simple 3-form.

b. General vector in surfaces of $\pmb { \sigma }$ is

$$
\pmb { \nu } = V ^ { x } \pmb { e } _ { x } + V ^ { y } \pmb { e } _ { y } + V ^ { z } \pmb { e } _ { z } .
$$

c. General vector in intersection of surfaces of ${ \ast } _ { \sigma }$ is

$$
\pmb { W } = \pmb { W } ^ { t } \pmb { e } _ { t } .
$$

# \$4.2. ELECTROMAGNETIC 2-FORM AND LORENTZ FORCE

The electromagnetic field tensor, Faraday $= F ,$ is an antisymmetric second-rank tensor (i.e.,2-form). Instead of expanding it in terms of the tensor products of basis 1-forms,

$$
{ \cal F } = { \cal F } _ { \alpha \beta } d x ^ { \alpha } \otimes d x ^ { \beta } ,
$$

the exterior calculus prefers to expand in terms of antisymmetrized tensor products ("exterior products,” exercise 4.1):

$$
{ \pmb F } = \frac { 1 } { 2 } F _ { \alpha \beta } { \pmb d } x ^ { \alpha } \wedge { \pmb d } x ^ { \beta } ,
$$

$$
d x ^ { \alpha } \wedge d x ^ { \beta } \equiv d x ^ { \alpha } \otimes d x ^ { \beta } - d x ^ { \beta } \otimes d x ^ { \alpha } .
$$

Electromagnetic 2-form expressed in terms of exterior products

Any 2-form (antisymmetric, second-rank tensor) can be so expanded. The symbol $^ { 6 6 } { \wedge } ^ { 5 9 }$ is variously called a“wedge,”a “hat,” or an “exterior product sign”； and $d x ^ { \alpha } \wedge d x ^ { \beta }$ are the“basis 2-forms”of a given Lorentz frame (see $\ S 3 . 5$ ,exercise 3.12, and Box 4.1).

There is no simpler way to illustrate this 2-form representation of the electromagnetic field than to consider a magnetic field in the $x$ -direction:

$$
\begin{array} { r } { F _ { y z } = - F _ { z y } = B _ { x } , } \\ { F = B _ { z } \pmb { d } \gamma \wedge \pmb { d } z . } \end{array}
$$

The 1-form ${ \pmb d \gamma } = \pmb { \mathrm { g r a d } } _ { \mathcal { Y } }$ is the set of surfaces (actually hypersurfaces) $y = 1 8$ (all $t , x , z ) , y = 1 9 ( { \mathrm { a l l } } t , x , z ) , y = 2 0 ( { \mathrm { a l l } } t , x , z ) ,$ , etc.; and surfaces uniformly interpolated between them. Similarly for the 1-form $\pmb { d z }$ .The intersection between these two sets of surfaces produces a honeycomb-like structure.That structure becomes a $^ { \mathfrak { s o } }$ -form” when it is supplemented by instructions (see arrows in Figure 4.l) that give a“sense of circulation” to each tube of the honeycomb (order of factors in the “wedge product” of equation 4.2;dy ^ $d z = - d z \wedge d y )$ .The 2-form $\pmb { F }$ in the example differs from this “basis 2-form”dy ^ $\pmb { d } z$ only in this respect, that where dy ^ dz had one tube, the field 2-form has $B _ { \varepsilon }$ tubes.

When one considers a tubular structure that twists and turns on its way through spacetime.one must have more components to describe it.The 2-form for the general electromagnetic field can be written as

$$
\begin{array} { l } { { F = E _ { x } d x \wedge d t + E _ { y } d y \wedge d t + E _ { z } d z \wedge d t + B _ { x } d y \wedge d z } } \\ { { \qquad + \ B _ { y } d z \wedge d x + B _ { z } d x \wedge d y } } \end{array}
$$

A 2-form as a honeycomb of tubes with a sense of circulation

(6 components,6 basis 2-forms).

A l-form is a machine to produce a number out of a vector (bongs of a bell as the vector pierces successive surfaces).A 2-form is a machine to produce a number out of an oriented surface (surface with a sense of circulation indicated on it: Figure 4.1, lower right). The meaning is as clear here as it is in elementary magnetism:

A 2-form as a machine to produce a number out of an oriented surface

![](images/503975ddcde280194f7bb6fbfaa0c926fec5ec3b1fdd447428fa87a16385b51f.jpg)  
Figure 4.1. Construction of the 2-form for the electromagnetic field $F = B _ { z } d y \wedge d z$ out of the l-forms dy and $\pmb { d z }$ by“wedge multiplication”(formation of honeycomb-like structure with sense of circulation indicated by arrows),A 2-form is a“machine to construct a number out of an oriented surface”(illustrated by sample surface enclosed by arrows at lower right;number of tubes intersected by this surface is

$$
\int _ { \mathrm { ( t h i s s u r f a c e ) } } { \overline { { F } } } = 1 8 ; \qquad \quad \cdots \quad -
$$

Faraday's concept of“magnetic flux").This idea of 2-form machinery can be connected to the“tensoras-machine”idea of Chapter 3 as follows.The shape of the oriented surface over which one integrates $\pmb { F }$ does not matter, for small surfaces.All that affects $\textstyle \int F$ is the area of the surface,and its orientation. Choose two vectors, $\pmb { u }$ and ${ \pmb v } _ { \pmb { \imath } }$ that lie in the surface. They form two legs of a parallelogram,whose orientation $\omega$ followed by $\pmb { \nu }$ and area are embodied in the exterior product u $\wedge \ v$ Adjust the lengths of $\pmb { u }$ and $\pmb { \nu }$ so their parallelogram, ${ \pmb u } \wedge { \pmb v } ,$ has the same area as the surface of integration. Then

F=SF=F(u, machinery idea [machinery idea of.this chapter Lof Chapter 3

Exercise:derive this result,for an infinitesimal surface u^ ${ \pmb v }$ and for general $\pmb { F } ,$ using the formalism of Box 4.1.

the number of Faraday tubes cut by that surface. The electromagnetic 2-form $\pmb { F }$ or Faraday described by such a“tubular structure”(suitably abstracted; Box 4.2) has a reality and a location in space that is independent of all coordinate systems and all artificial distinctions between “electric” and “magnetic” fields. Moreover, those tubes provide the most direct geometric representation that anyone has ever been able to give for the machinery by which the electromagnetic field acts on a charged particle. Take a particle of charge $^ e$ and 4-velocity

$$
\pmb { \mu } = \frac { d x ^ { \alpha } } { d \tau } \pmb { e } _ { \alpha } .
$$

Let this particle go through a region where the electromagnetic field is described by the 2-form

$$
F = B _ { x } d y \wedge d z
$$

of Figure 4.1. Then the force exerted on the particle (regarded as a l-form) is the contraction of this 2-form with the 4-velocity (and the charge);

Lorentz force as contraction of electromagnetic 2-form with particle's 4-velocity

$$
\pmb { \dot { p } } = d \pmb { p } / d \tau = e \pmb { F } ( \pmb { u } ) \equiv e \langle \pmb { F } , \pmb { u } \rangle ,
$$

as one sees by direct evaluation, letting the two factors in the 2-form act in turn on the tangent vector ${ \pmb u }$ ：

$$
\begin{array} { r l } & { \pmb { \dot { p } } = e B _ { x } \langle \pmb { d } y \wedge \pmb { d } z , \pmb { u } \rangle } \\ & { \quad = e B _ { x } \{ \pmb { d } y \langle \pmb { d } z , \pmb { u } \rangle - \pmb { d } z \langle \pmb { d } y , \pmb { u } \rangle \} } \\ & { \quad = e B _ { x } \{ \pmb { d } y \langle \pmb { d } z , \pmb { u } ^ { z } \pmb { e } _ { z } \rangle - \pmb { d } z \langle \pmb { d } y , \pmb { u } ^ { y } \pmb { e } _ { y } \rangle \} } \end{array}
$$

or

$$
{ \dot { p } } _ { \alpha } d x ^ { \alpha } = e B _ { x } u ^ { z } d y - e B _ { x } u ^ { y } d z .
$$

Comparing coeffcients of the separate basis l-forms on the two sides of this equa-tion, one sees reproduced allthe detail of the Lorentz force exerted by the magnetic field $B _ { x }$

$$
\begin{array} { l } { \displaystyle { \dot { p } _ { y } = \frac { d p _ { y } } { d \tau } = e B _ { x } \frac { d z } { d \tau } , } } \\ { \displaystyle { \dot { p } _ { z } = \frac { d p _ { z } } { d \tau } = - e B _ { x } \frac { d y } { d \tau } . } } \end{array}
$$

By simple extension of this line of reasoning to the general electromagnetic field, one concludes thatthe time-rate ofchange ofmomentum(1-form)is equal to the charge multiplied by the contraction of the Faraday with the 4-velocity.Figure 4.2 illustrates pictorially how the 2-form, $\pmb { F } ,$ serves as a machine to produce the l-form, $\pmb { \dot { p } }$ ,out of the tangent vector, eu.

# BoX 4.2 ABSTRACTING A 2-FORM FROM THE CONCEPT OF ‘HONEYCOMB-LIKE STRUCTURE." IN 3-SPACE AND IN SPACETIME

Open up a cardboard carton containing a dozen bottles,and observe the honeycomb structure of intersecting north-south and east-west cardboard separators between the bottles. That honeycomb structure of “tubes”("channels for bottles"） is a fairly apt illustration of a 2-form in the context of everyday 3-space.It yields a number (number of tubes cut) for each choice of smooth element of 2-surface slicing through the three-dimensional structure. However, the intersecting cardboard separators are rather too specific. All that a true 2-form can ever give is the number of tubes sliced through, not the “shape”of the tubes. Slew the carton around on the floor by $4 5 ^ { \circ }$ . Then half the separators run NW-SE and the other half run NE-SW,but through a given bit of 2-surface fixed in 3-space the count of tubes is unchanged. Therefore,one should be careful to make the concept of tubes in the mind's eye abstract enough that one envisages direction of tubes (vertical in the example) and density of tubes,but not any specific location or orientation for the tube walls.Thus all the following representations give one and the same 2-form, $\pmb { \sigma }$ ：

$$
\begin{array} { l } { { \pmb \sigma = B \pmb d x \wedge \pmb d y ; } } \\ { { \pmb \sigma = B ( 2 \pmb d x ) \wedge \left( \frac { 1 } { 2 } \pmb d y \right) } } \end{array}
$$

(NS cardboards spaced twice as close as before;   
EW cardboards spaced twice as wide as before);

$$
\sigma = B \ : d \left( { \frac { x - y } { \sqrt { 2 } } } \right) \wedge d \left( { \frac { x + y } { \sqrt { 2 } } } \right)
$$

(cardboards rotated through $4 5 ^ { \circ }$ ）；

$$
\pmb { \sigma } = B \frac { \alpha \pmb { d } x + \beta \pmb { d } y } { ( \alpha \delta - \beta \gamma ) ^ { 1 / 2 } } \wedge \frac { \gamma \pmb { d } x + \delta \pmb { d } y } { ( \alpha \delta - \beta \gamma ) ^ { 1 / 2 } }
$$

(both orientation and spacing of“cardboards” changing from point to point,with all four

functions, $\alpha , \beta , \gamma ,$ ,and δ,depending on position).

What has physical reality,and constitutes the real geometric object, is not any one of the l-forms just encountered individually, but only the 2-form $\pmb { \sigma }$ itself.This circumstance helps to explain why in the physical literature one sometimes refers to “tubes of force”and sometimes to “lines of force." The two terms for the same structure have this in common, that each yields a number when sliced by a bit of surface. The line-of-force picture has the advantage of not imposing on the mind any specific structure of “sheets of cardboard"; that is, any specifc decomposition of the 2-form into the product of l-forms. However, that very feature is also a disadvantage, for in a calculation one often finds it useful'to have a well-defined representation of the2-form as the wedge product of l-forms. Moreover, the tube picture,abstract though it must be if it is to be truthful, also has this advantage, that the orientation of the elementary tubes (sense of circulation as indicated by arrows in Figures 4.l and 4.5, for example) lends itself to ready visualization.Let the “walls” of the tubes therefore remain in all pictures drawn in this book as a reminder that 2-forms can be built out of 1-forms;but let it be understood here and hereafter how manyfold are the options for the individual l-forms!

Turn now from three dimensions to four, and find that the concept of “honeycomb-like structure” must be made still more abstract. In three dimensions the arbitrariness of the decomposition of the 2-form into l-forms showed in the slant and packing of the “cardboards,”but had no effect on the verticality,of the “channels for the bottles” ("direction of Faraday lines of force or tubes of force"); not so in four dimensions,or at least not in the generic case in four dimensions.

In special cases, the story is almost as simple in four dimensions as in three. An example of a special case is once again the 2-form ${ \pmb \sigma } = B { \pmb d } { \pmb x }$ ^ dy,with all the options for decomposition into l-forms that have already been mentioned, but with every option giving the same “direction” for the tubes.If the word “direction” now rises in status from “tube walls unpierced by motion in the direction of increasing $z ^ { \dag }$ to “tube walls unpierced either by motion in the direction of increasing $z$ ，or by motion in the direction of increasing t,or by any linear combination of such motions,” that is a natural enough consequence of adding the new dimension.Moreover, the same simplicity prevails for an electromagnetic plane wave.For example,let the wave be advancing in the $z$ -direction,and let the electric polarization point in the $x$ -direction; then for a monochromatic wave,one has

$$
E _ { x } = B _ { y } = E _ { 0 } \cos \omega ( z \mathrm { ~ . ~ . ~ } t ) = - F _ { 0 1 } = F _ { 3 1 } ,
$$

and all components distinct from these equal zero. Faraday is

$$
\begin{array} { r l r } {  { \pmb { F } = F _ { 0 1 } \pmb { d t } \wedge \pmb { d x } + F _ { 3 1 } \pmb { d z } \wedge \pmb { d x } } } \\ & { } & { = E _ { 0 } \cos \omega ( z - t ) \pmb { d ( z - t ) } \wedge \pmb { d x } , } \end{array}
$$

which is again representable as a single wedge product of two l-forms.

Not so in general! The general 2-form in four dimensions consists of six distinct wedge products,

$$
\begin{array} { r } { \pmb { F } = F _ { 0 1 } \pmb { d t } \wedge \pmb { d x } + F _ { 0 2 } \pmb { d t } \wedge \pmb { d y } + \cdot \cdot \cdot } \\ { + F _ { 2 3 } \pmb { d y } \wedge \pmb { d z } . } \end{array}
$$

It is too much to hope that this expression will reduce in the generic case to a single wedge product of two l-forms ("simple"2-form). It is not even

true that it will. It is only remarkable that it can be reduced from six exterior products to two (details in exercise 4.1); thus,

$$
{ \pmb F } = { \pmb \eta } ^ { 1 } \wedge { \pmb \xi } ^ { 1 } + { \pmb \eta } ^ { 2 } \wedge { \pmb \xi } ^ { 2 } .
$$

Each product $\pmb { \eta } ^ { i } \wedge \pmb { \xi } ^ { i }$ individually can be visualized as a honeycomb-like structure like those depicted in Figures 4.1, 4.2,4.4,and 4.5. Each such structure individually can be pictured as built out of intersecting sheets (l-forms), but with such details as the tilt and packing of these l-forms abstracted away. Each such structure individually gives a number when sliced by an element of surface. What counts for the 2-form $\pmb { F } ,$ however, is neither the number of tubes of ${ \pmb { \eta } } ^ { 1 } \wedge { \pmb \xi } ^ { 1 }$ cut by the surface, nor the number of tubes of $\pmb { \eta } ^ { 2 } \wedge \bar { \xi } ^ { 2 }$ cut by the surface, but only the sum of the two. This sum is what is referred to in the text as the “number of tubes of $\pmb { F } ^ { \ast }$ cut by the surface. The contribution of either wedge product individually is not well-defined, for a simple reason: the decomposition of a six-wedge-product object into two wedge products, miraculous though it seems, is actually far from unique (details in exercise 4.2).

In keeping with the need to have two products of l-forms to represent the general 2-form note that the vanishing of $\pmb { d } \pmb { F }$ ("no magnetic charges") does not automatically imply that $d ( \pmb { \eta } ^ { 1 } \wedge \pmb { \xi } ^ { 1 } )$ or $d ( \pmb { \eta } ^ { 2 } \land \pmb { \xi } ^ { 2 } )$ separately vanish. Note also that any spacelike slice through the general 2-form $\pmb { F }$ (reduction from four dimensions to three) can always be represented in terms of a honeycomb-like structure ("simple”2-form in three dimensions; Faraday's picture of magnetic tubes of force).

Despite the abstraction that has gone on in seeing in all generality what a 2-form is, there is no bar to continuing to use the term“honeycomb-like structure”in a broadened sense to describe this object; and that is the practice here and hereafter.

![](images/3f55682e01f2c80c4af3487f0b3b0f30fd8c7440d81e8a10c56f4427003e857b.jpg)  
Figure 4.2. The Faraday or 2-form $\pmb { F }$ of the electromagnetic fleld is a machine to produce a l-form (the time-rate of change of momentum $\pmb { \dot { \rho } }$ of a charged particle) out of a tangent vector (product of charge $^ e$ of the particle and its 4-velocity u). In spacetime the general 2-form is the “superposition” (see Box 4.2) of two structures like that ilustrated at the topof this diagram,the tubes of the first being tilted and packed as indicated,the tubes of the second being tilted in another direction and having a different packing density.

# $\ S 4 . 3$ .FORMS ILLUMINATE ELECTROMAGNETISM,AND ELECTROMAGNETISM ILLUMINATES FORMS

All electromagnetism allows itself to be summarized in the language of 2-forms, honeycomb-like“structures”(again in the abstract sense of “structure”of Box 4.2) of tubes filling all spacetime,as well when spacetime is curved as when it is flat. In brief, there are two such structures,one Faraday $= { \pmb { F } } ,$ the other Maxwell $= ^ { * } { \pmb { F } } ,$ each dual ("perpendicular,”the only place where metric need enter the discussion) to the other,each satisfying an elementary equation:

$$
\pmb { d } \pmb { F } = 0
$$

("no tubes of Faraday ever end") and

$$
{ d ^ { * } F } = 4 \pi ^ { * } J
$$

("the number of tubes of Maxwell that end in an elementary volume is equal to the amount of electric charge in that volume"). To see in more detail how this machinery shows up in action,look in turn at: (l) the definition of a 2-form; (2) the appearance of a given electromagnetic field as Faraday and as Maxwell; (3) the Maxwell structure for a point-charge at rest; (4) the same for a point-charge in motion; (5)the nature of the field of a charge that moves uniformly except during a brief instant of acceleration; (6) the Faraday structure for the field of an oscillating dipole; (7) the concept of exterior derivative; (8) Maxwel's equations in the language of forms; and (9) the solution of Maxwell's equations in flat spacetime, using a 1-form $\pmb { A }$ from which the Liénard-Wiechert 2-form $\pmb { F }$ can be calculated via ${ \pmb F } = \pmb { d A }$

Preview of key points in electromagnetism

A 2-form,as illustrated in Figure 4.l, is a machine to construct a number (net number of tubes cut") out of any “oriented 2-surface”(2-surface with “sense of circulation” marked on it):

A 2-form as machine for number of tubes cut

$$
\left( \begin{array} { l } { \mathrm { n u m b e r } } \\ { \mathrm { o f ~ t u b e s } } \\ { \mathrm { c u t } } \end{array} \right) = \int _ { \mathrm { s u r f a c e } } \pmb { F } .
$$

For example,let the 2-form be the one ilustrated in Figure 4.1

$$
{ \pmb F } = B _ { x } \pmb d y \wedge \pmb d z ,
$$

Number of tubes cut calculated in one example

and let the surface of integration be the portion of the surface of the 2-sphere $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = a ^ { 2 }$ ， $t =$ constant, bounded between $\theta = 7 0 ^ { \circ }$ and $\theta = 1 1 0 ^ { \circ }$ and between $\varphi = 0 ^ { \circ }$ and $\varphi = 9 0 ^ { \circ }$ ("Atlantic region of the tropics"). Write

$$
\begin{array} { c } { y = a \sin \theta \sin \varphi , } \\ { z = a \cos \theta , } \\ { { \pmb { d \gamma } = a ( \cos \theta \sin \varphi d \theta + \sin \theta \cos \varphi d \varphi ) , } } \\ { { \pmb { d z } = - a \sin \theta d \pmb { d \theta } , } } \\ { { \pmb { d \gamma } \wedge { \pmb { d z } = a ^ { 2 } \sin ^ { 2 } \theta \cos \varphi d \theta \wedge d \varphi . } } } \end{array}
$$

![](images/26161009f3d9fbf0fafb06034d764bf49997adce8992a61501eb9c1b46d114f2.jpg)  
Figure 4.3. Spacelike slices through Faraday,the electromagnetic 2-form,a geometric object, a honeycombof tubes that pervades allspacetime ("honeycomb”in the abstract sense spelled out more precisely in $\mathtt { B o x } 4 . 2$ ). The surfaces inthe drawingdo not look likea2-form (honeycomb),because the second familyof surfaces making up the honeycomb extends in the spatial direction that is suppressd from the drawing. Diagram

A shows one spacelike slice through the 2-form (time increases upwards in the diagram).In diagram B,a projection of the 2-form on this spacelike hypersurface gives the Faraday tubes of magnetic force inthis three-dimensional geometry (if the suppressed dimension were restored,the tubes would be tubes, not channels between lines). Diagram C shows another spacelike slice (hypersurface of simultaneity for an observer in a different Lorentz frame). Diagram D shows the very different pattern of magnetic tubes in this reference system. The demand that magnetic tubes of force shall not end $( \nabla \cdot \pmb { \cal B } = 0 )$ ,repeated over and over for every spacelike slice through Faraday,gives everywhere the result $\hat { \boldsymbol { \mathrm { o } } } \pmb { { \cal B } } / \hat { \eta } t = - \bar { \boldsymbol { \nabla } } \times \pmb { { \cal E } }$ Thus (magnetostatics) $^ +$ (covariance) (magnetodynamics). Similarly--see Chapters 17 and 21- (geometrostatics) $^ +$ (covariance) $\twoheadrightarrow$ (geometrodynamics).

The structure $d \theta \wedge d \theta$ looks like a “collapsed egg-crate”(Figure l.4, upper right) and has zero content, a fact formally evident from the vanishing of $\alpha \wedge \beta =$ $- \beta \wedge \alpha$ when $\pmb { \alpha }$ and $\pmb { \beta }$ are identical. The result of the integration,assuming constant $B _ { x } ,$ is

$$
\int _ { _ \mathrm { \small s u r f a c e } } { \pmb { F } } = a ^ { 2 } B _ { x } \int _ { _ { 7 0 ^ { \circ } } } ^ { 1 1 0 ^ { \circ } } \sin ^ { 2 } \theta d \theta \int _ { _ { 0 ^ { \circ } } } ^ { 9 0 ^ { \circ } } \cos \varphi d \varphi
$$

It is not so easy to visualize a pure electric field by means of its 2-form $\pmb { F }$ (Figure 4.4,left) as it is to visualize a pure magnetic field by means of its 2-form $\pmb { F }$ (Figures 4.1,4.2, 4.3). Is there not some way to treat the two fields on more nearly the same footing? Yes,construct the 2-form $\ast _ { F }$ (Figure 4.4,right) that is dual ("perpendicular"; Box 4.3；exercise 3.14) to $\pmb { F } .$

![](images/574b356ca8f0536af433616f9dee9809e23ec68bc758f809d33b27245afcca99.jpg)  
Figure 4.4. The Faraday structure

$$
{ \cal F } = \frac { 1 } { 2 } F _ { \mu \nu } \ d x ^ { \mu } \wedge \ d x ^ { \nu } = \frac { 1 } { 2 } F _ { 0 1 } d t \wedge \ d x + \frac { 1 } { 2 } F _ { 1 0 } d x \wedge \ d t = E _ { x } d x \wedge \ d t
$$

associated with an electric field in the $_ { x }$ -direction,and the dual("perpendicular") Maxwel honeycomblike 2-form

$$
\mathbf { \ { * } } F = { \frac { 1 } { 2 } } * F _ { \mu \nu } d x ^ { \mu } \wedge d x ^ { \nu } = { ^ { \circ } F } _ { 2 3 } d x ^ { 2 } \wedge d x ^ { 3 } = F ^ { 0 1 } d x ^ { 2 } \wedge d x ^ { 3 } = F _ { 1 0 } d x ^ { 2 } \wedge d x ^ { 3 } = E _ { x } d y \wedge d z .
$$

Represent in geometric form the field of a point-charge of strength $e$ at rest at the origin. Operate in flat space with spherical polar coordinates:

$$
\begin{array} { c } { { d s ^ { 2 } = . - d \tau ^ { 2 } = g _ { \mu \nu } d x ^ { \mu } d x ^ { \nu } } } \\ { { = - d t ^ { 2 } + d r ^ { 2 } + r ^ { 2 } d \theta ^ { 2 } + r ^ { 2 } \sin ^ { 2 } \theta d \varphi ^ { 2 } . } } \end{array}
$$

The electric field in the $r .$ direction being $E _ { r } = e / r ^ { 2 }$ ,it follows that the 2-form $\pmb { F }$ Or Faraday is

$$
F = \frac { 1 } { 2 } F _ { \mu \nu } d x ^ { \mu } \wedge d x ^ { \nu } = - E _ { r } d t \wedge d r = - \frac { e } { r ^ { 2 } } d t \wedge d r .
$$

Its dual, according to the prescription in exercise 3.14, is Maxwell:

Pattern of tubes in dual structure Mexwell for point-charge at rest

$$
M a x w e I I = { ^ { * } F } = e \sin \theta d \theta \wedge d \varphi ,
$$

as illustrated in Figure 4.5.

Take a tour in the positive sense around a region of the surface of the sphere illustrated in Figure 4.5. The number of tubes of $\ast _ { F }$ encompassed in the route will be precisely

$$
{ \binom { \mathrm { n u m b e r } } { \mathrm { o f ~ t u b e s } } } = e { \binom { \mathrm { s o l i d } } { \mathrm { a n g l e } } } .
$$

The whole number of tubes of $\ast _ { F }$ emergent over the entire sphere will be $ 4 \pi e .$ in conformity with Faraday's picture of tubes of force.

# Box 4.3 DUALITY OF 2-FORMS IN SPACETIME

Given a general 2-form (containing six exterior or wedge products)

$$
\pmb { F } = E _ { x } \pmb { d } x \wedge \pmb { d } t + E _ { y } \pmb { d } y \wedge \pmb { d } t + \cdot \cdot \cdot + B _ { z } \pmb { d } x \wedge \pmb { d } y ,
$$

one gets to its dual ("perpendicular") by the prescription

$$
{ } ^ { * } F = - B _ { x } d x \wedge d t - \cdot \cdot \cdot + E _ { y } d z \wedge d x + E _ { z } d x \wedge d y .
$$

# Duality Rotations

Note that the dual of the dual is the negative of the original 2-form; thus

$$
{ } ^ { * * } F = - E _ { x } d x \wedge d t - \cdot \cdot \cdot - B _ { z } d x \wedge d y = - F .
$$

In this sense \* has the same property as the imaginary number $i ; \ * *  = i i = - 1$ Thus one can write

$$
e ^ { * \alpha } = \cos \alpha + { } ^ { * } \sin \alpha .
$$

This operation, applied to $\pmb { F } ,$ carries attention from the generic 2-form in its simplest representation (see exercise 4.1)

$$
\pmb { F } = E _ { x } \pmb { d } x \wedge \pmb { d } t + B _ { x } \pmb { d } y \wedge \pmb { d } z
$$

to another“duality rotated electromagnetic feld"

$$
e ^ { * \alpha } F = ( E _ { x } \cos \alpha - B _ { x } \sin \alpha ) d x \wedge d t + ( B _ { x } \cos \alpha + E _ { x } \sin \alpha ) d y \wedge d z .
$$

If the original field satisfied Maxwel's empty-space field equations,so does the new field.With suitable choice of the “complexion” $\pmb { \alpha }$ , one can annul one of the two wedge products at any chosen point in spacetime and have for the other

$$
( B _ { x } { } ^ { 2 } + E _ { x } { } ^ { 2 } ) ^ { 1 / 2 } d y \wedge d z .
$$

Field of a point-charge in motion

How can one determine the structure of tubes associated with a charged particle moving at a uniform velocity? First express $\yen 5$ in rectangular coordinates moving with the particle (barred coordinates in this comoving “rocket” frame of reference; unbarred coordinates will be used later for a laboratory frame of reference). The relevant steps can be listed:

$$
{ } ^ { * } F = e \sin \bar { \theta } d \bar { \theta } \wedge d \overline { { \varphi } } = - e ( d \cos \bar { \theta } ) \wedge d \overline { { \varphi } } ;
$$

![](images/6ded1404acf9edcfdd001d4faace4d03e76b5ca5a9e4ab16185c4cbb942f844c.jpg)  
Figure 4.5. The field of $2 \cdot \mathrm { f o r m s } M a x w e I I = { } ^ { \ast } F = e \sin \theta d \theta \wedge d \phi$ that describes the electromagnetic field of a charge $_ e$ at rest at the origin.This picture is actually the intersection of $\yen 5$ with a 3-surface of constant time t; i.e.,the time direction is suppressed from the picture.

$$
\overline { { \varphi } } = \arctan \frac { \overline { { y } } } { \overline { { x } } } ; \qquad { \pmb d } \overline { { \varphi } } = \frac { \overline { { x } } \pmb { d } \overline { { y } } - \overline { { y } } \pmb { d } \overline { { x } } } { \overline { { x } } ^ { 2 } + \overline { { y } } ^ { 2 } } ;
$$

$$
\cos \theta = \frac { \overline { { z } } } { \overline { { r } } } ; \qquad - d ( \cos \theta ) = \frac { - d \overline { { z } } } { \overline { { r } } } + \frac { \overline { { z } } } { \overline { { r } } ^ { 3 } } ( \overline { { x } } d \overline { { x } } + \overline { { y } } d \overline { { y } } + \overline { { z } } d \overline { { z } } ) ;
$$

(d） combine to find

$$
{ } ^ { * } F = ( e / \overline { { r } } { } ^ { 3 } ) ( \overline { { x } } d / \overline { { y } } \wedge d / \overline { { z } } + \overline { { y } } d / \overline { { z } } \wedge d / \overline { { x } } + \overline { { z } } d / \overline { { x } } \wedge d / \overline { { y } } )
$$

(electromagnetic field of point charge in a comoving Cartesian system; spherically symmetric). Now transform to laboratory coordinates:

$$
\frac { 1 } { \sqrt { 1 - \beta ^ { 2 } } } = \cosh \alpha , ~ \frac { \beta } { \sqrt { 1 - \beta ^ { 2 } } } = \sinh \alpha
$$

$$
\left\{ \begin{array} { l } { { \overline { { t } } = t \cosh \alpha - x \sinh \alpha , } } \\ { { \overline { { x } } = - t \sinh \alpha + x \cosh \alpha , } } \\ { { \overline { { y } } = y \qquad \overline { { z } } = z ; } } \end{array} \right.
$$

$$
\overline { { { r } } } = [ ( x \cosh \alpha - t \sinh \alpha ) ^ { 2 } + y ^ { 2 } + z ^ { 2 } ] ^ { 1 / 2 } ;
$$

$$
\begin{array} { c } { { ^ { * } F = ( e / \bar { r } ^ { 3 } ) [ ( x \cosh \alpha - t \sinh \alpha ) \ / d \gamma \wedge d z + \gamma \ d z \wedge } } \\ { { ( \cosh \alpha \ d x - \sinh \alpha \ d t ) + z ( \cosh \alpha \ d x - \sinh \alpha \ d t ) \wedge \ d y ] ; } } \end{array}
$$

(d) compare with the general dual 2-form,

$$
\begin{array} { r l } & { ^ { * } F = E _ { z } { \bf { \em d } } \mathrm { \large / } { \mathrm {  ~ \wedge ~ } } { \bf { \it d } } z + E _ { y } { \bf { \em d } } z \mathrm {  ~ \wedge ~ } { \bf { \it d } } x + E _ { z } { \bf { \em d } } x \mathrm {  ~ \wedge ~ } { \bf { \it d } } y } \\ & { \qquad + B _ { x } { \bf { \em d } } t \mathrm {  ~ \wedge ~ } { \bf { \it d } } x + B _ { y } { \bf { \em d } } t \mathrm {  ~ \wedge ~ } { \bf { \it d } } y + B _ { z } { \bf { \em d } } t \mathrm {  ~ \wedge ~ } { \bf { \it d } } z ; } \end{array}
$$

and get the desired individual field components

$$
\begin{array} { r l r l } & {  E _ { x } = ( e / \overline { r } ^ { 3 } ) ( x \cosh \alpha - t \sinh \alpha ) , \quad } & { B _ { x } = 0 , } \\ & {  E _ { y } = ( e / \overline { r } ^ { 3 } ) ) ^ { \prime } \cosh \alpha , \quad } & { B _ { y } = - ( e / \overline { r } ^ { 3 } ) z \sinh \alpha ,  } \\ & {  \vphantom { ( e / \overline { r } ^ { 3 } ) }  E _ { z } = ( e / \overline { r } ^ { 3 } ) z \cosh \alpha ,  } & & { B _ { z } = ( e / \overline { r } ^ { 3 } ) y \sinh \alpha . } \end{array}
$$

One can verify that the invariants

$$
\begin{array} { l } { { B ^ { 2 } - E ^ { 2 } = \displaystyle \frac { 1 } { 2 } F _ { \alpha \beta } F ^ { \alpha \beta } , } } \\ { { { } } } \\ { { E \cdot B = \displaystyle \frac { 1 } { 4 } F _ { \alpha \beta } { } ^ { * } F ^ { \alpha \beta } } } \end{array}
$$

have the same value in the laboratory frame as in the rocket frame,as required. Note that the honeycomb structure of the differential form is not changed when one goes from the rocket frame to the laboratory frame. What changes is only the mathematical formula that describes it.

# \$4.4.RADIATION FIELDS

The Maxwel structure of tubes associated with a charge in uniform motion is more remarkable than it may seem at first sight, and not only because of the Lorentz contraction of the tubes in the direction of motion. The tubes arbitrarily far away move on in military step with the charge on which they center, despite the fact that there is no time for information“emitted” from the charge“right now” to get to the faraway tube “right now.” The structure of the faraway tubes “right now” must therefore derive from the charge at an earlier moment on its uniform-motion, straight-line trajectory. This circumstance shows up nowhere more clearly than in what happens to the field in consequence of a sudden change, in a short time $\pmb { A } \tau$ from one uniform velocity to another uniform velocity (Figure 4.6). The tubes have the standard patterns for the two states of motion, one pattern within a sphere of radius $r ,$ ，the other outside that sphere,where $r$ is equal to the lapse of time ("cm of light-travel time") since the acceleration took place. The necessity for the two patterns to fit together in the intervening zone, of thickness $\varDelta r = \varDelta \tau$ ,forces the field there to be multiplied up by a“stretching factor,” proportional to $r .$ This factor is responsible for the well-known fact that radiative forces fall off inversely only as the first power of the distance (Figure 4.6).

When the charge continuously changes its state of motion, the structure of the electromagnetic field, though based on the same simple principles as those illustrated in Figure 4.6, nevertheless looks more complex. The following is the Faraday 2-form for the field of an electric dipole of magnitude $p _ { 1 }$ oscillating up and down paralel to the $z$ -axis:

![](images/b0fc137f55ea69873815b93d4b12a50bf008d0117e9b0dae94307807a703e1f8.jpg)  
Figure 4.6. Mechanism of radiation. J. J. Thomson's way to understand why the strength of an electromagnetic wave falls only as the inverse first power of distance $r$ and why the amplitude of the wave varies (for low velocities） as $\sin \theta$ (maximum in the plane perpendicular to the line of acceleration). The charge was moving to the left at uniform velocity.Far away from it,the lines of force continue to move as if this uniform velocity were going to continue forever (Coulomb field of point-charge in slow motion).However, closer up the field is that of a point-change moving to the right with uniform velocity $\scriptstyle 1 / r ^ { 2 }$ dependence of strength upon distance). The change from the one field patern to another is confined to a shell of thickness $\pmb { \mathscr { s } } _ { \tau }$ Iocated at a distance $r$ from the point of acceleration (amplification of field by “stretching factor" $r \sin \theta \ \varDelta \beta / \varDelta \tau$ ；see text). We thank C.Teitelboim for the construction of this diagram.

$$
\begin{array} { r l } & { \underbrace { [ 2 \cos \theta \left( \frac { 1 } { r ^ { 3 } } - \frac { i \omega } { r ^ { 2 } } \right) } _ { \mathrm { g i v e s ~ } E _ { r } } d r \wedge d t + \underbrace { \sin \theta \left( \frac { 1 } { r ^ { 3 } } - \frac { i \omega } { r ^ { 2 } } - \frac { \omega ^ { 2 } } { r } \right) } _ { \mathrm { g i v e s ~ } E _ { \theta } } r d \theta \wedge d t } \\ & { \underbrace { + \sin \theta \left( \frac { - i \omega } { r ^ { 2 } } - \frac { \omega ^ { 2 } } { r } \right) } _ { \mathrm { g i v e s ~ } B _ { \phi } } d r \wedge r d \theta ] \} } \end{array}
$$

and the dual 2-form Maxwell $= ^ { \ast } F$ is

$$
{ } ^ { * } F = - B _ { x } d x \wedge d t - \cdot \cdot \cdot + E _ { x } d y \wedge d z + \cdot \cdot \cdot = \mathrm { r e a l } _ { \mathrm { ~ \tiny ~ h ~ } }
$$

$$
[ \sin \theta \left( { \frac { - i \omega } { r ^ { 2 } } } - { \frac { \omega ^ { 2 } } { r } } \right) \mathbf { \mathscr { d } } t \wedge r \sin \theta \ \mathbf { \mathscr { d } } \phi
$$

$$
\begin{array} { r l } & { \underbrace { + \ 2 \cos \theta \left( \frac { 1 } { r ^ { 3 } } - \frac { i \omega } { r ^ { 2 } } \right) r \ d \theta \wedge r \sin \theta \ d \phi } _ { \mathrm { g i v e s ~ } E _ { r } } } \\ & { + \ \sin \theta \left( \frac { 1 } { r ^ { 3 } } - \frac { i \omega } { r ^ { 2 } } - \frac { \omega ^ { 2 } } { r } \right) r \sin \theta \ d \phi \wedge \ d r ] \} . } \end{array}
$$

# $\ S 4 . 5$ . MAXWELL'S EQUATIONS

The general 2-form $\pmb { F }$ is written as a superposition of wedge products with a factor $^ { \frac { 1 } { 2 } , }$

$$
F = \frac { 1 } { 2 } F _ { \mu \nu } d x ^ { \mu } \wedge d x ^ { \nu } ,
$$

because the typical term appears twice, once as $F _ { x y } \ d x . \wedge d y$ and the second time as $F _ { y x } \pmb { d y } \wedge \pmb { d x }$ with $F _ { y x } = - F _ { x y }$ and dy $\bigwedge d x = - d x \wedge d y .$

If differentiation ("taking the gradient”; the operator $\pmb { d }$ ） produced out of a scalar a l-form,it is also true that differentiation (again the operator $\pmb { d } ,$ but now generally known under Cartan's name of “exterior differentiation"） produces a 2-form out of the general 1-form; and applied to a 2-form produces a 3-form; and applied to a 3-form produces a 4-form,the form of the highest order that spacetime will accommodate. Write the general $f$ form as

$$
\phi = \frac { 1 } { f ! } \phi _ { \alpha _ { 1 } \alpha _ { 2 } \ldots \alpha _ { f } } d x ^ { \alpha _ { 1 } } \wedge d x ^ { \alpha _ { 2 } } \wedge \cdot \cdot \cdot \wedge d x ^ { \alpha _ { f } }
$$

where the coefficient $\phi _ { \alpha _ { 1 } \alpha _ { 2 } \dots \alpha _ { f } }$ ,like the wedge product that follows it,isantisymmetric under interchange of any two indices.Then the exterior derivative of $\pmb { \phi }$ is

$$
d \phi \equiv \frac { 1 } { f ! } \frac { \partial \phi _ { \alpha _ { 1 } \alpha _ { 2 } \ldots \alpha _ { f } } } { \partial x ^ { \alpha _ { 0 } } } d x ^ { \alpha _ { 0 } } \wedge d x ^ { \alpha _ { 1 } } \wedge d x ^ { \alpha _ { 2 } } \wedge \cdots \wedge d x ^ { \alpha _ { f } } .
$$

Take the exterior derivative of Faraday according to this rule and find that it vanishes, not only for the special.case of the dipole oscillator,but also for a general electromagnetic field. Thus, in the coordinates appropriate for a local Lorentz frame, one has

$$
\begin{array} { l } { d F = d ( E _ { x } d x \wedge d t + \cdot \cdot \cdot + B _ { x } d y \wedge d z + \cdot \cdot \cdot ) } \\ { \ } \\ { = \left( { \frac { \partial E _ { x } } { \partial t } } d t + { \frac { \partial E _ { x } } { \partial x } } d x + { \frac { \partial E _ { x } } { \partial y } } d y + { \frac { \partial E _ { x } } { \partial z } } d z \right) \wedge d x \wedge d t } \\ { \ } \\ { \qquad + \cdot \cdot \cdot ( 5 \ \mathrm { m o r e \ s u c h \ s e t s \ o f \ 4 \ t e r m s \ e a c h } ) \cdot \cdot \cdot . . } \end{array}
$$

Note that such a term as dy $\wedge$ dy $\wedge \ d z$ is automatically zero("collapse of egg-crate cell when stamped $\left. \mathsf { o n } ^ { \mathsf { \pmb { \mathsf { \imath } } } } \right.$ ). Collect the terms that do not vanish and find

$$
\begin{array} { c } { { d F = \left( \displaystyle \frac { \partial B _ { x } } { \partial x } + \displaystyle \frac { \partial B _ { y } } { \partial y } + \displaystyle \frac { \partial B _ { z } } { \partial z } \right) d x \wedge d y \wedge d z } } \\ { { \ } } \\ { { + \left( \displaystyle \frac { \partial B _ { x } } { \partial t } + \displaystyle \frac { \partial E _ { z } } { \partial y } - \displaystyle \frac { \partial E _ { y } } { \partial z } \right) d t \wedge d y \wedge d z } } \\ { { \ } } \\ { { + \left( \displaystyle \frac { \partial B _ { y } } { \partial t } + \displaystyle \frac { \partial E _ { z } } { \partial z } - \displaystyle \frac { \partial E _ { z } } { \partial x } \right) d t \wedge d z \wedge d x } } \\ { { \ } } \\ { { + \left( \displaystyle \frac { \partial B _ { z } } { \partial t } + \displaystyle \frac { \partial E _ { y } } { \partial x } - \displaystyle \frac { \partial E _ { z } } { \partial y } \right) d t \wedge d x \wedge d y . } } \end{array}
$$

Each term in this expression is familiar from Maxwell's equations

$$
\mathrm { d i v } \pmb { B } = \nabla \cdot \pmb { B } = 0
$$

and

$$
\operatorname { c u r l } E = \nabla \times E = - \dot { B } .
$$

Each vanishes, and with their vanishing Faraday itself is seen to have zero exterior derivative:

$$
\begin{array} { r } { { \pmb d } { \pmb F } = 0 . } \end{array}
$$

In other words,“Faraday is a closed 2-form”;“the tubes of $\pmb { F }$ nowhere come to an end.”

A similar calculation gives for the exterior derivative of the dual 2-form Maxwell the result

$$
\begin{array} { r l } & { d ^ { * } F = d ( - B _ { x } d x \wedge d t - \cdots + E _ { x } d y \wedge d z + \cdots ) } \\ & { \qquad = \left( \frac { \partial E _ { x } } { \partial x } + \frac { \partial E _ { y } } { \partial y } + \frac { \partial E _ { z } } { \partial z } \right) d x \wedge d y \wedge d z } \\ & { \qquad + \left( \frac { \partial E _ { x } } { \partial t } - \frac { \partial B _ { z } } { \partial y } + \frac { \partial B _ { y } } { \partial z } \right) d t \wedge d y \wedge d z } \\ & { \qquad + \ \cdots } \end{array}
$$

$$
\begin{array} { r l } & { = 4 \pi ( \rho \ d x \wedge d y \wedge d z } \\ & { \quad - J _ { x } \ d t \wedge d y \wedge d z } \\ & { \quad - J _ { y } \ d t \wedge d z \wedge d x } \\ & { \quad - J _ { z } \ d t \wedge d x \wedge d y ) = 4 \pi ^ { \ast } J ; } \end{array}
$$

$$
d ^ { * } F = 4 \pi ^ { * } J .
$$

Faraday structure: tubes nowhere end

Maxwell structure: density of tube endings given by charge-current 3-form