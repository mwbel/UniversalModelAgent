Chapter ll faces up to the central issue: geodesic deviation ("rate of change of separation vector between two geodesics"),and its use in defining the curvature of spacetime.

Spacetime curvature

But to define curvature is not enough. The man who would understand gravity deeply must also see curvature at work, producing relative accelerations of particles in_ Newtonian spacetime (Chapter l2); he must learn how,in Einstein spacetime, distances (metric) determine completely the curvature and the law of parallel trans-port (Chapter l3); he must be the master of powerful tools for computing curvature (Chapter l4); and he must grasp the geometric significance of the algebraic and differential symmetries of curvature (Chapter 15).

# This chapter:a Track-1 overview of differential geometry

Unfortunately, such deep understanding requires time-far more time than one can afford in a ten-week or fteen-week course,far more than a lone reader may wish to spend on first passage through the book. For the man who must rush on rapidly,this chapter contains a “Track-1” overview of the essential mathematical tools $( \ S \ S 8 . 4 \ – 8 . 7 )$ . From it one can gain an adequate,but not deep,understanding of spacetime curvature, of tidal gravitational forces,and of the mathematics of curved spacetime.This overview is also intended for the Track-2 reader; it will give him a taste of what is to come.The ambitious reader may also wish to consult other introductions to differential geometry (see Box 8.1).

# Box 8.1 BOOKS ON DIFFERENTIAL GEOMETRY

There are several mathematics texts that may be consulted for a more detailed and extensive discussion of modern differential geometry along the line taken here. Bishop and Goldberg (l968) is the no.l reference.Hicks (l965) could be chosen as a current standard graduate-level text, with O'Neill (1966） at the undergraduate level introducing many of the same topics without presuming that the reader finds easy and obvious the current style in which pure mathematicians think and write.Auslander and MacKenzie (l963）at a somewhat more advanced level also allow for the reader to whom differential equations are more familiar than homomorphisms.Willmore (l959) is easy to read but presents no challenge,and leads to little progress in adapting to the style of current mathematics.Trautman (l965) and Misner (1964a, 1969a) are introductions somewhat similar to ours, except for deemphasis of pictures; like ours, they are aimed at the student of relativity. Flanders (1963） is easy and useful as an introduction to exterior differential forms;it also gives examples of their application to a wide variety of topics in physics and engineering.

# $\$ 8.2$ .TRACK 1 VERSUS TRACK 2: DIFFERENCE IN OUTLOOK AND POWER

Nothing is more wonderful about the relation between Einstein's theory of gravity and Newton's theory than this,as discovered by Elie Cartan (l923,1924): that both theories lend themselves to description in terms of curvature; that in both this curvature is governed by the density of mass-energy; and that this curvature allows itself to be defined and measured without any use of or reference to any concept of metric. The difference between the two theories shows itself up in this: Einstein's theory in the end (or in the beginning,depending upon how one presents it!) does define an interval between every event and every nearby event; Newton's theory not only does not, but even says that any attempt to talk of spacetime intervals violates Newton's laws. This being the case, Track 2 will forego for a time (Chapters 9-12) any use of a spacetime metric ("Einstein interval"). It will extract everything possible from a metric-free description of spacetime curvature (all of Newton's theory; important parts of Einstein's theory).

Geodesic deviation is a measurer and definer of curvature,but the onlooker is forbidden to reduce a vector description of separation to a numerical measure of distance (no metric at this stage of the analysis): what an impossible situation! Nevertheless,that is exactly the situation with which Chapters 9-12 will concern themselves: how to do geometry without a metric. Speaking physically, one will overlook at this stage the fact that the geometry of the physical world is always and everywhere locally Lorentz, and endowed with a light cone, but one will exploit to the fullest the Galileo-Einstein principle of equivalence: in any given locality one can find a frame of reference in which every neutral test particle, whatever its velocity, is free of acceleration. The tracks of these neutral test particles define the geodesics of the geometry. These geodesics provide tools with which one can do much: define parallel transport (Chapter lO),define covariant derivative (Chapter 10),quantify geodesic deviation (Chapter ll), define spacetime curvature (Chapter 11),and explore Newtonian gravity (Chapter l2). Only after this full exploitation of metric-free geodesics will Track 2 admit the Einstein metric back into the scene (Chapters 13-15).

But to forego use of the metric is a luxury which Track 1 can ill afford; too little time would be left for relativistic stars, cosmology, black holes, gravitational waves, experimental tests,and the dynamics of geometry. Therefore,the Track-1l overview in this chapter keeps the Einstein metric throughout. But in doing so,it pays a heavy price: (l) no possibility of seeing curvature at work in Newtonian spacetime (Chapter 12); (2) no possibility of comparing and contrasting the geometric structures of Newtonian spacetime (Chapter l2) and Einstein spacetime (Chapter l3),and hence no possibility of grasping fully the Newtonian-based motivation for the Einstein field equations (Chapter 17); (3) no possibility of understanding fully the mathematical interrelationships of “geodesic,”“parallel transport,” "covariant derivative,”“curvature,”and “metric”(Chapters 9,10,11,13); (4) no possibility of introducing the mathematical subjects “differential topology"(geometry without metric or covariant

Preview of Track-2 differential geometry

What the Track-1 reader will miss

derivative, Chapter 9) and “affne geometry”(geometry with covariant derivative but no metric, Chapters l0 and 11),subjects which find major application in modern analytical mechanics [see, e.g., Arnold and Avez (l968)； also exercise 4.ll of this book],in Lie group theory with its deep implications for elementary particle physics [see,e.g., Hermann (1966); also exercises 9.12, 9.13,10.16,and 11.12 of this book], in the theory and solution of partial differential equations [see,e.g., Sternberg(l969)], and,of course, in gravitation theory.

# $\$ 8.3$ . THREE ASPECTS OF GEOMETRY: PICTORIAL，ABSTRACT，COMPONENT

Gain the power in $\ S 8 . 4$ and Chapter 9 to discuss tangent vectors,l-forms, tensors in curved spacetime; gain the power in $\ S 8 . 5$ and Chapter l0 to parallel-transport vectors,to differentiate them,to discuss geodesics; use this power in $\ S 8 . 7$ and Chapter 1l to discuss geodesic deviation, to define curvature; .... But full power this will be only if it can be exercised in three ways:in pictures,in abstract notation,and in component notation (Box 8.3). Elie Cartan $( \mathbf { B o x 8 . 2 } ) ,$ gave new insight into both

![](images/5590f1d72c1e39219c35c50382256f6dabe7fe26dca7ec31952a9a2842c7064d.jpg)  
Box 8.2 ELIE CARTAN,1869-1951

Elie Cartan is a most remarkable figure in recent mathematical history. One learns from his obituary [Chern and Chevalley (l952)] that he was born a blacksmith's son in southern France,and proved the value of government scholarship aid by rising through the system to a professorship at the Sorbonne in l912 when he was 43. At the age of 32 he invented the exterior derivative [Cartan (1901), which he used then mostly in differential equations and the theory of Lie groups,where he had already made significant contributions. He was about fifty when he began applying it to geometry, and sixty before Riemannian geometry specifically was the object of this research,including his text [Cartan (l928)], which is still reprinted and worth studying. Although universally recognized,his work did not find responsive readers until he neared retiremcnt around 1940,when the “Bourbaki” generation of French mathematicians began to provide a conceptual framework for (among other things) Cartan's insights and methods.This made Cartan communicable and teachable as his own writings never were,so that by the time of his death at 82 in 1951 his infuence was obviously dominating the revolutions then in full swing in all the fields (Lie groups, differential equations, and differential geometry) in which he had primarily worked.

The modern,abstract,coordinate-free approach to geometry,which is used extensively in this book, is due largely to Elie Cartan.He also discovered the geometric approach to Newtonian gravity that is developed and exploited in Chapter 12.

# Box 8.3 THREE LEVELS OF DIFFERENTIAL GEOMETRY

(l） Purely pictorial treatment of geometry: tangent vector is conceived in terms of the separation of two points in the limit in which the points are indefinitely close; vectors are added and subtracted locally as in flat space; vectors at distinct points are compared by parallel transport from one point to another; this_parallel transport is accomplished by_a “Schild's ladder construction”of geodesics (Box 10.2); diagrams,yes;algebra, no; it is tied conceptually as closely as possible to the world of test particles and measurements.   
(2) Abstract differential geometry: treats a tangent vector as existing in its own right,without necessity to give its breakdown into components, $\pmb { A } = A ^ { 0 } \pmb { e } _ { 0 } + A ^ { 1 } \pmb { e } _ { 1 } + A ^ { 2 } \pmb { e } _ { 2 } + A ^ { 3 } \pmb { e } _ { 3 } ,$

just as one is accustomed nowadays in electromagnetism to treat the electric vector $\pmb { { \cal E } } ,$ ， without having to write out its components; uses a similar approach to differentiation (compare gradient operator $\mathbf { v }$ of elementary vector analysis,as distinguished from coordinate-dependent pieces of such an operator, such as $\partial / \partial x , \partial / \partial y$ ，etc.)； is the quickest, simplest mathematical scheme One knows to derive general results in differential geometry. (3) Differential geometry as expressed in the language of components: is indispensible in programming large parts of general relativity for a computer; is convenient or necessary or both when one is dealing even at the level of elementary algebra with the most simple applications of relativity, from the expansion of the Friedmann universe to the curvature around a static center of attraction.

Newtonian gravity (Chapter l2) and the central geometric simplicity of Einstein's field equations (Chapter l5), because he had full command of all three methods of doing differential geometry. Today, no one has full power to communicate with others about the subject who cannot express himself in all three languages. Hence the interplay between the three forms of expression in what follows.

It is not new to go back and forth between the three languages,as witnesses the textbook treatment of the velocity and acceleration of a planet in Kepler motion around the sun. The velocity is written

Planetary orbit as example of three viewpoints

$$
\mathbf { \nu } = v ^ { \hat { r } } e _ { \hat { r } } + v ^ { \hat { \phi } } e _ { \hat { \phi } } .
$$

(The hats $\dots$ on $\boldsymbol { e } _ { \hat { \boldsymbol { r } } }$ and $\pmb { e } _ { \hat { \phi } }$ signify that these are unit vectors.）The acceleration is

$$
a = \frac { d \mathfrak { v } } { d t } = \frac { d \mathfrak { v } ^ { \hat { r } } } { d t } \mathfrak { e } _ { \hat { r } } + \frac { d \mathfrak { v } ^ { \hat { \phi } } } { d t } \mathfrak { e } _ { \hat { \phi } } + \mathfrak { v } ^ { \hat { r } } \frac { d \mathfrak { e } _ { \hat { r } } } { d t } + \mathfrak { v } ^ { \hat { \phi } } \frac { d \mathfrak { e } _ { \hat { \phi } } } { d t } .
$$

![](images/568de275318e2c00970bf21b67b4aa8467ab69a36f0143b9d4c2e39ba67c2728.jpg)  
Figure 8.1. A Keplerian orbit in the sun’s gravitational feld,as treated using the standard Euclidean-space version of Newtonian gravity.The basis vectors themselves change from point to point along the orbit [equations (8.3).This fgure illustrates the pictorialaspectof differential geometry.Later(exercise8.5)it wililustrate the concepts of“covariant derivative”and “connection coefficients.”

The unit vectors are turning (Figure 8.1) with the angular velocity $\omega = d \phi / d t$ ; so

$$
\begin{array} { l } { \displaystyle \frac { d e _ { \hat { r } } } { d t } = \omega e _ { \hat { \phi } } = \frac { d \hat { \phi } } { d t } e _ { \hat { \phi } } , } \\ { \displaystyle \frac { d e _ { \hat { \phi } } } { d t } = - \omega e _ { \hat { r } } = - \frac { d \phi } { d t } e _ { \hat { r } } . } \end{array}
$$

Thus the components of the acceleration have the values

$$
a ^ { \hat { r } } = { \frac { d v ^ { \hat { r } } } { d t } } - v ^ { \hat { \phi } } { \frac { d \phi } { d t } } = { \frac { d ^ { 2 } r } { d t ^ { 2 } } } - r \left( { \frac { d \phi } { d t } } \right) ^ { 2 }
$$

and

$$
a ^ { \hat { \phi } } = { \frac { d v ^ { \hat { \phi } } } { d t } } + v ^ { \hat { r } } { \frac { d \phi } { d t } } = { \frac { d } { d t } } \left( r { \frac { d \phi } { d t } } \right) + { \frac { d r } { d t } } { \frac { d \phi } { d t } } .
$$

Here is the acceleration in the language of components; $\pmb { a }$ was the acceleration in abstract language; and Figure 8.l shows the acceleration as an arrow. Each of these three languages will receive its natural generalization in the coming sections and chapters from two-dimensional flat space (with curvilinear coordinates） to four-dimensional curved spacetime, and from spacetime to more general manifolds (see $\ S 9 . 7$ on manifolds).

Turn now to the Track-1 overview of diferential geometry.

# $\$ 8.4$ . TENSOR ALGEBRA IN CURVED SPACETIME

Tensor algebra:

To see spacetime curvature at work,examine tidal gravitational forces (geodesic deviation); and to probe these forces, make measurements in a finite-sized laboratory. Squeeze the laboratory to infinitesimal size; alleffects of spacetime curvature become infinitesimal; the physicist cannot tell whether he is in fat spacetime or curved spacetime.Neither can the mathematician,in the limit as his domain of attention squeezes down to a single event, $\mathcal { P } _ { o }$

(1）occurs in infinitesimal neighborhood of an event

At the event $\mathcal { P } _ { o }$ (in the infinitesimal laboratory) both physicist and mathematician can talk of vectors, of 1-forms, of tensors; and no amount of spacetime curvature can force the discussion to change from its flat-space form.A particle at $\mathcal { P } _ { o }$ has a 4-momentum $\pmb { p }$ ,with squared length

(2) is same in curved spacetime as in flat

$$
p ^ { 2 } = p \cdot p = g ( p , p ) = - m ^ { 2 } .
$$

The squared length,as always, is calculated by inserting $\pmb { p }$ into both slots of a linear machine, the metric $\pmb { \mathscr { g } }$ at $\mathcal { P } _ { o }$ . The particle also has a 4-acceleration $\pmb { a }$ at $\mathcal { P } _ { o }$ ； and, if the particle is charged and freely moving, then $\pmb { a }$ is produced by the electromagnetic feld tensor $\pmb { F }$ ：

$$
m \pmb { a } = e \pmb { F } ( . \dots , \pmb { u } ) .
$$

In no way can curvature affect such local, coordinate-free, geometric relations.And in no way can it prevent one from introducing a local Lorentz frame at $\mathcal { P } _ { o } ,$ and from performing standard, flat-space index manipulations in it:

$$
p = p ^ { \alpha } e _ { \alpha } , \quad p ^ { 2 } = p ^ { \alpha } p _ { . } ^ { \beta } \eta _ { \alpha \beta } = p ^ { \alpha } p _ { \alpha } , \quad \quad m a ^ { \alpha } = e F ^ { \alpha \beta } u _ { \beta } .
$$

But local Lorentz frames are not enough for the man who would calculate in curved spacetime. Non-Lorentz frames (nonorthonormal basis vectors $\{ \pmb { e } _ { \alpha } \} )$ often simplify calculations.Fortunately,no effort at all is required to master the rules of "index mechanics”in an arbitrary basis at a fixed event $\mathcal { P } _ { o }$ . The rules are identical to those in flat spacetime, except that (l) the covariant Lorentz components $\eta _ { \alpha \beta }$ of the metric are replaced by

(3)rules for component manipulation change slightly when using nonorthonormai basis

$$
\begin{array} { r } { g _ { \alpha \beta } \equiv \pmb { e } _ { \alpha } \cdot \pmb { e } _ { \beta } \equiv \pmb { g } ( \pmb { e } _ { \alpha } , \pmb { e } _ { \beta } ) ; } \end{array}
$$

Components of metric

(2) the contravariant components $\eta ^ { \alpha \beta }$ are replaced by $g ^ { \alpha \beta }$ ， where

$$
| | g ^ { \alpha \beta } | | \equiv | | g _ { \alpha \beta } | | ^ { - 1 } ( \mathrm { m a t r i x \ i n v e r s e } ) ;
$$

i.e.,

$$
g _ { \alpha \beta } g ^ { \beta \gamma } = \delta _ { \alpha } \gamma ;
$$

(3)the Lorentz transformation matrix $| | A ^ { \alpha ^ { \prime } } { } _ { \beta } | |$ and its inverse $1 1 A ^ { \beta } { } _ { \alpha ^ { \prime } } | |$ are replaced by an arbitrary but nonsingular transformation matrix $| | L ^ { \alpha ^ { \prime } } { } _ { \beta } | |$ and its inverse $1 1 L ^ { \beta } { _ { \alpha } } ! !$ ：

$$
\begin{array} { r } { \pmb { \mathscr { e } } _ { \beta } = \pmb { \mathscr { e } } _ { \alpha ^ { \prime } } L ^ { \alpha ^ { \prime } } { } _ { \beta } , \qquad p ^ { \beta } = L ^ { \beta } { } _ { \alpha } p ^ { \alpha ^ { \prime } } , } \\ { | ! L ^ { \beta } { } _ { \alpha ^ { \prime } } | | = | ! L ^ { \alpha ^ { \prime } } { } _ { \beta } | | ^ { - 1 } ; } \end{array}
$$

(4) in the special case of “coordinate bases,” ${ \pmb e } _ { \alpha } = \partial \mathcal { P } / \partial x ^ { \alpha }$ ， $\begin{array} { r } { \pmb { e } _ { \beta ^ { \prime } } = \partial \mathcal { P } / \partial \boldsymbol { x } ^ { \beta ^ { \prime } } , } \end{array}$

$$
L ^ { \alpha ^ { \prime } } { } _ { \beta } = \partial x ^ { \alpha ^ { \prime } } / \partial x ^ { \beta } , \qquad L ^ { \beta } { } _ { \alpha ^ { \prime } } = \partial x ^ { \beta } / \partial x ^ { \alpha ^ { \prime } } ;
$$

and (5) the Levi-Civita tensor $\pmb { \varepsilon }$ ,like the metric tensor, has components that depend--- on how nonorthonormal the basis vectors are (see exercise 8.3): if ${ \pmb \theta } _ { 0 }$ points toward the future and $\pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ are righthanded, then

$$
\begin{array} { l } { { \varepsilon _ { \alpha \beta \gamma \delta } = ( - g ) ^ { 1 / 2 } [ \alpha \beta \gamma \delta ] , } } \\ { { \varepsilon ^ { \alpha \beta \gamma \delta } = g ^ { - 1 } \varepsilon _ { \alpha \beta \gamma \delta } = - ( - g ) ^ { - 1 / 2 } [ \alpha \beta \gamma \delta ] , } } \end{array}
$$

where $[ \alpha \beta \gamma \delta ]$ is the completely antisymmetric symbol

$$
[ \alpha \beta \gamma \delta ] \equiv \left\{ { \begin{array} { l } { + 1 { \mathrm { ~ i f ~ } } \alpha \beta \gamma \delta { \mathrm { ~ i s ~ a n ~ e v e n ~ p e r m u t a t i o n ~ o f ~ } } 0 1 2 3 , } \\ { - 1 { \mathrm { ~ i f ~ } } \alpha \beta \gamma \delta { \mathrm { ~ i s ~ a n ~ o d d ~ p e r m u t a t i o n ~ o f ~ } } 0 1 2 3 , } \\ { 0 { \mathrm { ~ i f ~ } } \alpha \beta \gamma \delta { \mathrm { ~ a r e ~ n o t ~ a l l ~ d i f f e r e n t } } , } \end{array} } \right.
$$

and where $g$ is the determinant of the matrix $1 | g _ { \alpha \beta } | |$

$$
g \equiv { \sf d e t l l } g _ { \alpha \beta } | | = { \sf d e t l } | \pmb { e } _ { \alpha } \cdot \pmb { e } _ { \beta } | | .
$$

Read Box 8.4 for full discussion and proofs; work exercise 8.1 below for fuller understanding and mastery.

Several dangers are glossed over in this discussion.In flat spacetime one often does not bother to say where a vector,l-form, or tensor is located. One freely moves geometric objects from event to event without even thinking. Ofcourse,the unwritten rule of transport is: hold all lengths and directions fixed while moving;i.e.,hold all Lorentz-frame components fixed; i.e.，“parallel-transport” the object. But in

# Box 8.4 TENSOR ALGEBRA AT A FIXED EVENT IN AN ARB/TRARY BASIS

A.Bases

Tangent-vector basis: Pick $\pmb { e } _ { 0 } , \pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ at $\scriptstyle { \mathcal { P } } _ { 0 }$ arbitrarily-but insist they belinearly independent.

“Dual basis” for l-forms: The basis $\{ \pmb { e } _ { \alpha } \}$ determines a l-form basis $\{ { \pmb { \omega } } ^ { \alpha } \}$ (its “dual basis") by

$$
\langle { \pmb w } ^ { \alpha } , { \pmb e } _ { \beta } \rangle = \delta ^ { \alpha } { } _ { \beta }
$$

[see equation (2.19)].

Geometric interpretation (Figure 9.2): ${ \pmb e } _ { 2 } , { \pmb e } _ { 3 } , { \pmb e } _ { 0 }$ lie parallel to surfaces of $\pmb { \omega } ^ { 1 }$ ； $\pmb { \varrho } _ { 1 }$ pierces precisely one surface of $\pmb { \omega } ^ { 1 }$

Function interpretation: $\langle { \pmb { \omega } } ^ { \alpha } , { \pmb { \sigma } } _ { \beta } \rangle = \delta ^ { \alpha } { } _ { \beta }$ determines the value of $\pmb { \omega } ^ { \pmb { \alpha } }$ on any vector $\pmb { \mu } = \pmb { u } ^ { \beta } \pmb { \mathcal { e } } _ { \beta }$ (number of “bongs of bel" as $\pmb { u }$ pierces $\pmb { \omega } ^ { \alpha }$ ：

$$
\langle { \pmb w } ^ { \alpha } , { \pmb u } \rangle = \langle { \pmb w } ^ { \alpha } , u ^ { \beta } { \pmb e } _ { \beta } \rangle = u ^ { \beta } \langle { \pmb w } ^ { \alpha } , { \pmb e } _ { \beta } \rangle = u ^ { \beta } \delta _ { \beta } ^ { \alpha } = u ^ { \alpha } .
$$

Special case: coordinate bases. Choose an arbitrary coordinate system $\{ x ^ { \alpha } ( { \mathcal { P } } ) \}$ At $\mathcal { P } _ { 0 }$ choose ${ \pmb { e } } _ { \alpha } = \partial \pmb { \mathcal { P } } / \partial x ^ { \alpha }$ as basis vectors.Then the dual basis is $\pmb { \omega } ^ { \alpha } = \pmb { d x } ^ { \alpha }$ Proof: the general coordinate-free relation $\langle \pmb { d } f , \pmb { v } \rangle = \hat { \partial } _ { \pmb { v } } f$ [equation (2.17)], with $f = x ^ { \alpha }$ and $\pmb { v } = \partial \pmb { \mathcal { P } } / \partial x ^ { \beta }$ ，reads

$$
\begin{array} { r } { \langle \pmb { d } x ^ { \alpha } , \partial \pmb { \mathcal { P } } / \partial x ^ { \beta } \rangle = ( \partial / \partial x ^ { \beta } ) x ^ { \alpha } = \delta _ { \beta } ^ { \alpha } . } \end{array}
$$

# B. Algebra of Tangent Vectors and 1-Forms

The Lorentz-frame discussion of equations (2.19) to(2.22) is completely unchanged when one switches to an arbitrary basis. Its conclusions:

expansion, $\pmb { u } = \pmb { e } _ { \alpha } \pmb { u } ^ { \alpha }$ ， $\sigma = \sigma _ { \alpha } \omega ^ { \alpha }$ ； calculation of components, uα = <ωα,u>, O& = (σ,eα>; value of form on vector, $\langle \pmb { \sigma } , \pmb { u } \rangle = \sigma _ { \alpha } u ^ { \alpha }$

Application to gradients of functions:

expansion, ${ \pmb d } f = f _ { , \alpha } { \pmb \omega } ^ { \alpha }$ [defines $f _ { , \alpha } ]$ ；   
calculation of components, $f _ { , \alpha } = \langle d f , e _ { \alpha } \rangle = \partial _ { \pmb { \theta } _ { \alpha } } f$ [see equation (2.17)].

Raising and lowering of indices is accomplished with gaβ and gαβ equations (8.5） and (8.6)). Proof:

$\widetilde { \pmb { u } }$ ，the l-form corresponding to $\pmb { u }$ , is defined by $\langle \widetilde { \pmb { u } } , \pmb { v } \rangle = \pmb { u } \cdot \pmb { v }$ for all $\mathbf { \Delta } v ;$   
thus, $u _ { \alpha } \equiv \langle \tilde { \pmb { u } } , \pmb { e } _ { \alpha } \rangle = \pmb { u } \cdot \pmb { e } _ { \alpha } = u ^ { \beta } \pmb { e } _ { \beta } \cdot \pmb { e } _ { \alpha } = u ^ { \beta } g _ { \beta \alpha } .$ ：   
inverting this equation yields $u ^ { \beta } = g ^ { \beta \alpha } u _ { \alpha }$

# C. Change of Basis

The discussion of Lorentz transformations in equations (2.39) to (2.43) is applicable to general changes of basis if one replaces $| | A ^ { \alpha ^ { \prime } } { } _ { \beta } | |$ by an arbitrary but nonsingular matrix $1 | L ^ { \alpha ^ { \prime } } { } _ { \beta } | |$ [equations (8.7), (8.8)]. Conclusions:

$$
\begin{array} { r l r l } & { \pmb { e } _ { \alpha ^ { \prime } } = \pmb { e } _ { \beta } L ^ { \beta } _ { \alpha ^ { \prime } } , } & & { \pmb { e } _ { \beta } = \pmb { e } _ { \alpha ^ { \prime } } L ^ { \alpha ^ { \prime } } { } _ { \beta } ; } \\ & { \pmb { \omega } ^ { \alpha ^ { \prime } } = L ^ { \alpha ^ { \prime } } { } _ { \beta } \pmb { \omega } ^ { \beta } , } & & { \pmb { \omega } ^ { \beta } = L ^ { \beta } _ { \alpha ^ { \prime } } \pmb { \omega } ^ { \alpha ^ { \prime } } ; } \\ & { \pmb { v } ^ { \alpha ^ { \prime } } = L ^ { \alpha ^ { \prime } } { } _ { \beta } \pmb { v } ^ { \beta } , } & & { \pmb { v } ^ { \beta } = L ^ { \beta } _ { \alpha ^ { \prime } } \pmb { v } ^ { \alpha ^ { \prime } } ; } \\ & { \sigma _ { \alpha ^ { \prime } } = \sigma _ { \beta } L ^ { \beta } _ { \alpha ^ { \prime } } , } & & { \sigma _ { \beta } = \sigma _ { \alpha ^ { \prime } } L ^ { \alpha ^ { \prime } } { } _ { \beta } . } \end{array}
$$

When both bases are coordinate bases, then $L ^ { \beta } { } _ { \alpha ^ { \prime } } = \partial x ^ { \beta } / \partial x ^ { \alpha ^ { \prime } } , L ^ { \alpha ^ { \prime } } { } _ { \beta } = \partial x ^ { \alpha ^ { \prime } } / \partial x ^ { \beta }$ Proof:

$$
{ \pmb e } _ { \alpha ^ { \prime } } = { \frac { \hat { \alpha } } { \hat { \alpha } x ^ { \alpha ^ { \prime } } } } = { \frac { \hat { \alpha } x ^ { \beta } } { \hat { \alpha } x ^ { \alpha ^ { \prime } } } } { \frac { \hat { \alpha } } { \hat { \alpha } x ^ { \beta } } } = { \frac { \hat { \alpha } x ^ { \beta } } { \hat { \alpha } x ^ { \alpha ^ { \prime } } } } { \pmb e } _ { \beta } ; \qquad \mathrm { s i m i l a r l y } ~ { \pmb e } _ { \beta } = { \frac { \hat { \alpha } x ^ { \alpha ^ { \prime } } } { \hat { \alpha } x ^ { \beta } } } { \pmb e } _ { \alpha ^ { \prime } } .
$$

# D． Algebra of Tensors

The discussions of tensor algebra given in $\ S 3 . 2$ [equations (3.8) to (3.22)] and in $\ S 3 . 5$ (excluding gradient and divergence) are unchanged, except that

$$
\eta _ { \alpha \beta } \longrightarrow g _ { \alpha \beta } \qquad \eta ^ { \alpha \beta } \longrightarrow g ^ { \alpha \beta } , \qquad A _ { \beta } ^ { \alpha ^ { \prime } } \longrightarrow L _ { \beta } ^ { \alpha ^ { \prime } } , \qquad A _ { \alpha ^ { \prime } } ^ { \beta } \longrightarrow L _ { \alpha ^ { \prime } } ^ { \beta } ;
$$

and the components of the Levi-Civita tensor are changed from (3.50) to (8.10) [see exercise 8.3[.

Chief conclusions :

expansion, $\pmb { S } = S ^ { \alpha } { } _ { \beta \gamma } \pmb { \theta } _ { \alpha } \otimes \pmb { \omega } ^ { \beta } \otimes \pmb { \omega } ^ { \gamma } ;$   
components, $S ^ { \alpha } { } _ { \beta \gamma } = \pmb { S } ( \pmb { \omega } ^ { \alpha } , \pmb { e } _ { \beta } , \pmb { e } _ { \gamma } ) ;$   
raising and lowering indices, $S _ { \mu \beta } { } ^ { \nu } = g _ { \mu \alpha } g ^ { \nu \gamma } S ^ { \alpha } { } _ { \beta \gamma } ;$   
change of basis, $S ^ { \lambda ^ { \prime } } { } _ { \mu ^ { \prime } \nu ^ { \prime } } = L ^ { \lambda ^ { \prime } } { } _ { \alpha } L ^ { \dot { \beta } } { } _ { \mu ^ { \prime } } L ^ { \gamma } { } _ { \nu ^ { \prime } } S ^ { \alpha } { } _ { \beta \gamma }$ ；   
machine operation, $\pmb { S } ( \pmb { \sigma } , \pmb { u } , \pmb { v } ) = { S ^ { \alpha } } _ { \beta \gamma } \sigma _ { \alpha } u ^ { \beta } v ^ { \gamma }$ ；   
tensor product, ${ \pmb { \tau } } = { \pmb { \mu } } \otimes { \pmb { v } } \Longleftrightarrow { \pmb { T } } ^ { \alpha \beta } = { \pmb { u } } ^ { \alpha } { \pmb { v } } ^ { \beta }$ ；   
contraction, ${ \bf \ddot { \theta } } ^ { \bullet } { \bf \bar { M } } =$ contraction of $\pmb R$ on slots 1 and $3 ^ { \mathfrak { w } } \Longleftrightarrow M _ { \mu \nu } = R ^ { \alpha } { } _ { \mu \alpha \nu }$ wedge product, $\alpha \wedge \beta$ has components $\alpha ^ { \mu } \beta ^ { \nu } - \beta ^ { \mu } \alpha ^ { \nu }$ ；   
Dual, ${ } ^ { * } J _ { \alpha \beta \gamma } = J ^ { \mu } \varepsilon _ { \mu \alpha \beta \gamma } , { } ^ { * } F _ { \alpha \beta } = { \scriptstyle { \frac { 1 } { 2 } } } F ^ { \mu \nu } \varepsilon _ { \mu \nu \alpha \beta } , { } ^ { * } B _ { \alpha } = { \scriptstyle { \frac { 1 } { 6 } } } B ^ { \lambda \mu \nu } \varepsilon _ { \lambda \mu \nu \alpha } .$

# E. Commutators (exercise 8.2; \$9.6; Box 9.2)

f ${ \pmb u }$ and $\pmb { \nu }$ are tangent vector felds,one takes the view that $\pmb { u } = \hat { d } _ { \pmb { u } }$ and $\pmb { v } = \hat { d } _ { \pmb { v } }$ and one defines

$$
\mathbf { \Delta } [ u , v ] \equiv [ \hat { \sigma } _ { u } , \hat { \sigma } _ { v } ] \equiv \hat { \sigma } _ { u } \hat { \sigma } _ { v } - \hat { \sigma } _ { v } \hat { \sigma } _ { u } .
$$

This commutator is itself a tangent vector field.

Components in a coordinate basis:

$$
\begin{array} { r } { [ { \pmb u } , { \pmb v } ] = ( u ^ { \beta } v ^ { \alpha } , _ { \beta } - v ^ { \beta } u ^ { \alpha } , _ { \beta } ) ( \partial / \partial x ^ { \alpha } ) . \qquad } \\ { \qquad \quad \pmb { \mathrm { t } } = { \pmb e } _ { \alpha } ] } \end{array}
$$

Commutation coefficients of a basis:

$$
[ { \pmb e } _ { \alpha } , { \pmb e } _ { \beta } ] \equiv c _ { \alpha \beta } { } ^ { \gamma } { \pmb e } _ { \gamma } , \qquad c _ { \alpha \beta \mu } \equiv c _ { \alpha \beta } { } ^ { \gamma } g _ { \gamma \mu } .
$$

Coordinate basis ("holonomic") ${ c _ { \alpha \beta } } ^ { \gamma } = 0$

Noncoordinate basis ("anholonomic") some ${ c _ { \alpha \beta } } ^ { \gamma } \neq 0$ (see exercise 9.9).

curved spacetime there is no global Lorentz coordinate system in which to hold components fixed; and objects initially parallel, after “parallel transport” along different curves cease to be parallel("geodesic deviation”; Earth's meridians,parallel at equator, cross at north and south poles). Thus,in curved spacetime one must not blithely move a geometric object from point to point, without carefully specifying how it is to be moved and by what route. Each local geometric object has its own official place of residence (event $\mathcal { P } _ { o } )$ ; it can interact with other objects residing there (tensor algebra); but it cannot interact with any object at another event $\mathcal { L }$ until it has been carefully transported from $\mathcal { P } _ { o }$ to $\mathfrak { L }$

Vectors and tensors must not be moved blithely from point to point

This line of reasoning, pursued further,leads one to speak of the“tangent space” at each event, in which that event's vectors (arrows)and 1-forms (families of surfaces) lie,and in which its tensors (linear machines） operate. One even draws heuristic pictures of the tangent space,as in Figure 9.1 (p. 231).

Tangent space defined

Another danger in curved spacetime is the temptation to regard vectors as arrows linking two events ("point for head and point for tail")-i.e.,to regard the tangent space of Figure 9.l as lying in spacetime itself.This practice can be useful for heuristic purposes, but it is incompatible with complete mathematical precision. (How is the tangent space to be molded into a warped surface?) Four definitions of a vector were given in Figure 2.l (page 49): three definitions relying on “point for head and point for tail"； one, $" d \varphi / d \lambda "$ ，purely local. Only the local definition is wholly viable in curved spacetime, and even it can be improved upon, in the eyes of mathematicians,as follows.

Definitions of vector in curved spacetime:

(1)as $d \mathcal { P } / d \lambda$

There is a one-to-one correspondence (complete “isomorphism") between vectors ${ \pmb u }$ and directional derivative operators $\partial _ { \pmb { u } }$ . The concept of vector is a bit fuzzy, but “directional derivative” is perfectly well-defined.To get rid of all fuzziness, exploit the isomorphism to the full: define the tangent vector $\pmb { u }$ to be equal to the corresponding directional derivative

$$
\pmb { u } \equiv \partial _ { \pmb { u } } .
$$

(2) as directional derivative

(This practice, unfamiliar as it may be to a physicist at first, has mathematical power; so this book will use it frequently. For a fuller discussion, see $\ S 9 . 2 . )$

# Exercise 8.1. PRACTICE WITH TENSOR ALGEBRA

Let $t , x , y , z$ be Lorentz coordinates in flat spacetime, and let

$$
r = ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 } , \qquad \theta = \cos ^ { - 1 } ( z / r ) , \qquad \phi = \tan ^ { - 1 } ( y / x )
$$

be the corresponding spherical coordinates. Then

$$
{ \pmb e } _ { 0 } = \hat { \sigma } \mathcal { S } / \hat { \sigma } t , \qquad { \pmb e } _ { r } = \hat { \sigma } \mathcal { S } ^ { \beta } / \hat { \sigma } r , \qquad { \pmb e } _ { \theta } = \hat { \sigma } \mathcal { S } / \hat { \sigma } \theta , \qquad { \pmb e } _ { \phi } = \hat { \sigma } \mathcal { P } / \hat { \sigma } \phi
$$

is a coordinate basis,and

$$
{ \pmb { e } } _ { \hat { \imath } } = \frac { \partial \mathcal { P } } { \partial t } , \qquad { \pmb { e } } _ { \hat { \imath } } = \frac { \partial \mathcal { P } } { \partial r } , \qquad { \pmb { e } } _ { \hat { \imath } } = \frac { 1 } { r } \frac { \hat { c } \mathcal { P } } { \hat { c } \theta } , \qquad { \pmb { e } } _ { \hat { \imath } } = \frac { 1 } { r \sin \theta } \frac { \hat { \partial } \mathcal { P } } { \hat { c } \phi }
$$

is a noncoordinate basis.

(a) Draw a picture of $\mathbf { \mathcal { e } } _ { \theta } , \mathbf { \mathcal { e } } _ { \phi } , \mathbf { \mathcal { e } } _ { \hat { \theta } }$ ,and $\pmb { e } _ { \hat { \phi } }$ at several different points on a sphere of constant t,r. [Answer for $\pmb { \theta } , \pmb { \theta } _ { \phi }$ should resemble Figure 9.1.]

(b) What are the l-form bases $\scriptstyle \left\{ \pmb { \omega } ^ { \alpha } \right\}$ and $\{ \pmb { \omega } ^ { \hat { \alpha } } \}$ dual to these tangent-vector bases? [Answer: $\omega ^ { 0 } = \mathbf { \nabla } \mathbf { \mathbf { \mathbf { \mathit { d } } } } t$ $\pmb { \omega } ^ { \tau } = \pmb { d r }$ $\omega ^ { \theta } = d \theta$ $\omega ^ { \phi } = d \phi$ ； $\pmb { \omega } ^ { \hat { 0 } } = \pmb { d } t$ $\pmb { \omega } ^ { \dagger } = \pmb { d r }$ $\omega ^ { \bar { \dot { \theta } } } = r d \theta$ ， $\begin{array} { r } { { \pmb { \omega } } ^ { \hat { \diamond } } = r \sin \theta \mathbf { d } \phi . } \end{array}$ 1

(c) What is the transformation matrix linking the original Lorentz frame to the spherical. coordinate frame $\{ \pmb { e _ { a } } \} \ ?$ [Answer: nonzero components are

$$
\begin{array} { r l r l } & { L ^ { t } _ { 0 } = 1 , \quad } & { L ^ { z } _ { r } = \frac { \hat { c } \hat { z } } { \hat { \sigma } r } = \cos \theta . } & & { L ^ { z } _ { \theta } = \frac { \hat { \sigma } z } { \hat { \sigma } \theta } = - r \sin \theta , } \\ & { L ^ { z } _ { r } = \sin \theta \cos \phi , \quad } & { L ^ { x } _ { \theta } = r \cos \theta \cos \phi , \quad } & { L ^ { x } _ { \phi } = - r \sin \theta \sin \phi , } \\ & { L ^ { \nu } _ { r } = \sin \theta \sin \phi , \quad } & { L ^ { \nu } _ { \theta } = r \cos \theta \sin \phi , \quad } & { L ^ { \nu } _ { \phi } = r \sin \theta \cos \phi . ] } \end{array}
$$

(d) Use this transformation matrix to calculate the metric components $g _ { \alpha \beta }$ in the spherical coordinate basis. and invert the resulting matrix to get $g ^ { \alpha \beta }$ .[Answer:

$$
\begin{array} { r l r l r l r l r l } & { } & { g _ { 0 0 } = - 1 , \quad } & { g _ { r r } = 1 , } & & { g _ { \theta \theta } = r ^ { 2 } , \quad } & { g _ { \phi \phi } = r ^ { 2 } \sin ^ { 2 } \theta , } & & { \mathrm { a l l ~ o t h e r ~ } g _ { \alpha \beta } = 0 . } \\ & { } & { g ^ { 0 0 } = - 1 , } & & { g ^ { r r } = 1 , } & & { g ^ { \theta \theta } = r ^ { - 2 } , } & & { g ^ { \phi \phi } = r ^ { - 2 } \sin ^ { - 2 } \theta , } & & { \mathrm { a l l ~ o t h e r ~ } g ^ { \alpha \beta } = 0 . } \end{array}
$$

(e) Showthat the noncoordinate basis $\left\{ \pmb { e } _ { \dot { \alpha } } \right\}$ is orthonoraleveryhere;ie,tat $g _ { \hat { \alpha } \hat { \beta } } =$ $\eta _ { \alpha \beta }$ ；i.e. that

$$
g = - { \omega } ^ { \hat { 0 } } \otimes { \omega } ^ { \hat { 0 } } + { \omega } ^ { \hat { \tau } } \otimes { \omega } ^ { \hat { \tau } } + { \omega } ^ { \hat { \theta } } \otimes { \omega } ^ { \hat { \theta } } + { \omega } ^ { \hat { \phi } } \otimes { \omega } ^ { \hat { \phi } } .
$$

(f） Write the gradient of a function $f$ in terms of the spherical coordinate and noncoordinate bases. [Answer:

$$
{ \begin{array} { r l } & { d f = { \frac { \partial f } { \partial t } } d t + { \frac { \partial f } { \partial r } } d r + { \frac { \partial f } { \partial \theta } } d \theta + { \frac { \partial f } { \partial \phi } } d \phi } \\ & { \qquad = { \frac { \partial f } { \partial t } } { \boldsymbol { \omega } } ^ { \hat { 0 } } + { \frac { \partial f } { \partial r } } { \boldsymbol { \omega } } ^ { \hat { r } } + { \frac { 1 } { r } } { \frac { \partial f } { \partial \theta } } { \boldsymbol { \omega } } ^ { \hat { \theta } } + { \frac { 1 } { r \sin \theta } } { \frac { \partial f } { \partial \phi } } { \boldsymbol { \omega } } ^ { \hat { \phi } } . } \end{array} }
$$

(g)What are the components of the Levi-Civita tensor in the spherical coordinate and noncoordinate bases? [Answer for coordinate basis:

$$
\begin{array} { l } { { \varepsilon _ { 0 r \theta \phi } = - \varepsilon _ { r 0 \theta \phi } = + \varepsilon _ { r \theta 0 \phi } = \cdot \cdot \cdot = r ^ { 2 } \sin \theta , } } \\ { { \varepsilon ^ { 0 r \theta \phi } = - \varepsilon ^ { r 0 \theta \phi } = + \varepsilon ^ { r \theta \phi 0 } = \cdot \cdot \cdot = - r ^ { - 2 } \sin ^ { - 1 } \theta . } } \end{array}
$$

# Exercise 8.2. COMMUTATORS

Take the mathematician's viewpoint that tangent vectors and directional derivatives are the same thing, $\pmb { u } = \hat { d } _ { \pmb { u } }$ .Let ${ \pmb u }$ and $\pmb { \nu }$ be two vector fields,and define their commutator in the manner familiar from quantum mechanics

$$
[ { \pmb u } , { \pmb v } ] \equiv [ \hat { \sigma } _ { { \pmb w } } , \hat { \sigma } _ { { \pmb v } } ] \equiv \hat { \sigma } _ { { \pmb u } } \hat { \sigma } _ { { \pmb v } } - \hat { \sigma } _ { { \pmb v } } \hat { \sigma } _ { { \pmb u } }
$$

(a) Derive the following expression for $[ { \pmb u } , { \pmb v } ] ,$ ,valid in any coordinate basis,

$$
[ { \pmb u } , { \pmb v } ] = ( { \pmb u } ^ { \beta } { \pmb v } ^ { \alpha } , \beta - v ^ { \beta } { \pmb u } ^ { \alpha } , \beta ) { \pmb e } _ { \alpha } .
$$

Thus, despite the fact that it looks like a second-order differential operator, $[ { \pmb u } , { \pmb v } ]$ is actually of first order-i.e., it is a tangent vector.

(b) For any basis $\{ \pmb { \mathscr { e } } _ { \pmb { \alpha } } \}$ ,one defines the“commutation coefficients” ${ c _ { \beta } } { _ { \gamma } } ^ { \alpha }$ and ${ c _ { \beta \gamma \alpha } }$ by

$$
[ e _ { \beta } , e _ { \gamma } ] \equiv c _ { \beta \gamma } { } ^ { \alpha } e _ { \alpha } ; c _ { \beta \gamma \alpha } \equiv g _ { \alpha \mu } c _ { \beta \gamma } { } ^ { \mu } .
$$

Show that ${ c _ { \beta \gamma } } ^ { \alpha } = { c _ { \beta \gamma \alpha } } = 0$ for any coordinate basis.

(c） Calculate $c _ { \hat { \beta } \hat { \gamma } } { } ^ { \hat { \alpha } }$ for the spherical noncoordinate basis of exercise 8.1.[Answer: All vanish except

$$
\begin{array} { r l } & { c _ { \hat { r } \hat { \theta } } ^ { \enspace \enspace \hat { \theta } } = - c _ { \hat { \theta } \hat { r } } ^ { \enspace \enspace \hat { \theta } } = - 1 / r , } \\ & { c _ { \hat { r } \hat { \phi } } ^ { \enspace \enspace \hat { \phi } } = - c _ { \hat { \phi } \hat { r } } ^ { \enspace \enspace \hat { \phi } } = - 1 / r , } \\ & { c _ { \hat { \theta } \hat { \phi } } ^ { \enspace \enspace \hat { \phi } } = - c _ { \hat { \phi } \hat { \theta } } ^ { \enspace \enspace \hat { \phi } } = - \cot \theta / r . ] } \end{array}
$$

# Exercise 8.3. COMPONENTS OF LEVI-CIVITA TENSOR IN NONORTHONORMAL FRAME

(a) Show that expressions (8.10) are the components of $\pmb \varepsilon$ in an arbitrary basis, with ${ \pmb \theta } _ { 0 }$ pointing toward the future and $\pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ right-handed.[Hints: (l） Review the discussion of $\pmb \varepsilon$ in Lorentz frames, given in exercise 3.13. (2) Calculate $\pmb { \varepsilon } _ { \alpha \beta \gamma \delta }$ and $\varepsilon ^ { \alpha \beta \gamma \delta }$ by transforming from a local Lorentz frame $\left\{ \pmb { e } _ { \hat { \mu } } \right\}$ ,e.g.,

$$
\varepsilon _ { \alpha \beta \gamma \delta } = L _ { \alpha } ^ { \hat { \mu } } L _ { \beta } ^ { \hat { \nu } } L _ { \gamma } ^ { \hat { \lambda } } L _ { \delta } ^ { \hat { \rho } } \varepsilon _ { \hat { \mu } \hat { \nu } \hat { \lambda } \hat { \rho } } .
$$

(3) Show that these expressions reduce to

$$
\varepsilon _ { \alpha \beta \gamma \delta } = \mathsf { d e t l } | L ^ { \hat { \mu } } { } _ { \nu } | | \varepsilon _ { \alpha \beta \hat { \gamma } \hat { \delta } } , \qquad \varepsilon ^ { \alpha \beta \gamma \delta } = \mathsf { d e t l } | L ^ { \nu } { } _ { \hat { \mu } } | | \varepsilon ^ { \hat { \alpha } \hat { \beta } \hat { \gamma } \hat { \delta } } .
$$

(4) Show, from the transformation law for the metric components, that

$$
( \mathop { \bf d e t } | | L ^ { \nu } { } _ { \hat { \mu } } | | ) ^ { 2 } \mathop { \bf d e t } | | g _ { \alpha \beta } | | = - 1 .
$$

(5)Combine these results to obtain expressions (8.10).]

(b) Show that the components of the permutation tensors [defined by equations (3.50h)- (3.50j)] have the same values [equations (3.50k)- $( 3 . 5 0 \mathbf { m } ) ]$ in arbitrary frames as in Lorentz frames.

Additional exercises on tensor algebra: exercises 9.3 and 9.4 (page 234).

# \$8.5. PARALLEL TRANSPORT, COVARIANT DERIVATIVE, CONNECTION COEFFICIENTS，GEODESICS

The vehicle that carries one from classical mechanics to quantum mechanics is the correspondence principle. Similarly, the vehicle between flat spacetime and curved spacetime is the equivalence principle: “The laws of physics are the same in any local Lorentz frame of curved spacetime as in a global Lorentz frame of flat spacetime.”But to apply the equivalence principle,one must first have a mathematical representation of a local Lorentz frame. The obvious choice is this: $\pmb { A }$ local Lorentz frame at a given event ${ \mathcal { P } } _ { o }$ is the closest thing there is to a global Lorentz frame at that event; i.e., it is a coordinate system in which

Equivalence principle as vehicle between flat spacetime and curved

Local Lorentz frame: mathematical representation

$$
g _ { \mu \nu } ( \mathcal { P } _ { o } ) = \eta _ { \mu \nu } ,
$$

and in which $g _ { \mu \nu }$ holds as tightlyas possible to $\eta _ { \mu \nu }$ in the neighborhood of ${ \mathcal { P } } _ { o }$ ：

$$
g _ { \mu \nu , \alpha } ( \mathcal { P } _ { o } ) = 0 .
$$

More tightly than this it cannot hold in general $[ g _ { \mu \nu , \alpha \beta } ( \mathcal { P } _ { o } )$ cannot be set to zero]; spacetime curvature forces it to change. [Combine $\ S 1 1 . 5$ with equations (8.24) and (8.44).]

An observer in a local Lorentz frame in curved spacetime can compare vectors and tensors at neighboring events, just as he would in fat spacetime. But to make the comparison, he must parallel-transport them to a common event. For him the act of parallel transport is simple:he keeps all Lorentz-frame components fixed, just as if he were in flat spacetime. But for a man without a local Lorentz frameperhaps with no coordinate system or basis vectors at all-parallel transport is less trivial.He must either ask his Lorentz-based friend the result,or he must use a more sophisticated technique.One technique he can use-a“Schild's ladder”construction that requires no coordinates or basis vectors whatsoever-is described in $\ S 1 0 . 2$ and Box l0.2. But the Track-l reader need not master Schild's ladder. He can always ask a local Lorentz observer what the result of any given parallel transport is,.or he can use general formulas worked out below.

Comparison by paralel transport is the foundation on which rests the gradient of a tensor field, VT. No mention of parallel transport was made in $\ S 3 . 5$ ，where the gradient was first defined, but parallel transport occurred implicitly: one defined $\yen 7$ in such a way that its components were $T ^ { \alpha } { } _ { \beta , \gamma } = \partial T ^ { \alpha } { } _ { \beta } / \partial x ^ { \gamma }$ [for $\pmb { \tau }$ a $\mathbf { \Sigma } ( _ { 1 } ^ { 1 } )$ tensor]; i.e., one asked $\yen 7$ to measure how much the Lorentz-frame components of $\pmb { \tau }$ change from point to point. But“no change in Lorentz components”would have meant “parallel transport,” so one was implicitly asking for the change in $\pmb { \tau }$ relative to what $\pmb { \tau }$ would have been after pure parallel transport.

To codify in abstract notation this concept pf differentiation,proceed as follows. First define the “covariant derivative” $\yen 1$ of $\pmb { \tau }$ along a curve $\mathcal { P } ( \lambda )$ , whose tangent vector is $\pmb { \mu } = d \mathcal { P } / d \lambda$ ：

$$
( \nabla _ { u } T ) _ { \mathrm { a t } \mathcal { P } ( 0 ) } = \operatorname* { l i m } _ { \varepsilon \to 0 } \left\{ \frac { T [ \mathcal { P } ( \varepsilon ) ] _ { \mathrm { p a r a l l e l - t r a n s p o r t e d t o } \mathcal { P } ( 0 ) } - T [ \mathcal { P } ( 0 ) ] } { \varepsilon } \right\} .
$$

Gradient defined

(See Figure 8.2 for the special case where $\pmb { \tau }$ is a vector field ${ \pmb v } .$ ）Then define $\yen 7$ to be the linear machine,that gives $\yen 1$ when $\pmb { u }$ is inserted into its last slot:

$$
\pmb { \nabla } \pmb { \tau } ( . \dots , . \dots , \pmb { u } ) \equiv \pmb { \nabla } _ { \pmb { u } } \pmb { \tau } .
$$

The result is the same animal ("gradient") as was defined in $\ S 3 . 5$ (for proof see exercise 8.8). But this alternative definition makes clear the relationship to parallel transport, including the fact that

In a local Lorentz frame,the components of $\yen 7$ are directional derivatives of the components of T: $T ^ { \beta } { } _ { \alpha , \gamma } ,$ Not so in a general basis. If $\{ \pmb { e } _ { \beta } ( \mathcal { P } ) \}$ is a basis that varies arbitrarily but smoothly from point to point, and $\{ \pmb { \omega } ^ { \pmb { \alpha } } ( \mathcal { P } ) \}$ is its dual basis, then $\pmb { \nabla } \pmb { T } = \pmb { \nabla } ( T ^ { \beta } { } _ { \alpha } \pmb { e } _ { \beta } \otimes \pmb { \omega } ^ { \alpha } )$ will contain contributions from $\bigtriangledown e _ { \beta }$ and $\yen 40$ , as well as from $\nabla { T ^ { \beta } } _ { \alpha } \equiv { \bf { d } } T ^ { \beta } { } _ { \alpha } = T ^ { \beta } { } _ { \alpha , \gamma } \pmb { \omega } ^ { \gamma } { } $

To quantify the contributions from $\triangledown _ { \pmb { \theta } _ { \beta } }$ and $\yen 40$ ,i.e.,to quantify the twisting, turning,expansion,and contraction of the basis vectors and 1-forms,one defines "connection coefficients":

![](images/949aa0130233846b2081f9a8add92c5ebf85326e2a3800c460dc7f48d6e15430.jpg)  
Figure 8.2. Definition of the covariant derivative $\cdots$ of a vector field ${ \pmb v }$ along a curve ${ \mathcal { P } } ( \lambda )$ ， with tangent vector $\pmb { \upsilon } \equiv d \vartheta / d \lambda$ ：（l） choose a point ${ \mathcal { P } } ( 0 )$ on the curve,at which to evaluate $\yen 1$ (2)Choose a nearby point $\mathcal { P } ( \varepsilon )$ on the curve.(3） Parallel-transport ${ \pmb v } [ \mathcal { P } ( \varepsilon ) ]$ along the curve back to ${ \mathcal { P } } ( 0 )$ ，getting the vector ${ \pmb v } _ { \mathrm { i i } } [ \pmb { \mathcal { P } } ( \pmb { \varepsilon } ) ] .$ (4）Take the difference $\delta \pmb { v } \equiv \pmb { v } _ { \nparallel } [ \mathcal { P } ( \varepsilon ) ] - \pmb { v } [ \mathcal { P } ( 0 ) ] .$ (5）Then $\yen 1$ is defined by

$$
\begin{array} { r } { \pmb { \nabla _ { \pmb { u } } } \pmb { v } \equiv \mathrm { \small ~ L i m ~ } \frac { \delta \pmb { v } } { \varepsilon } = \mathrm { \small ~ L i m ~ } \bigg \{ \frac { \pmb { v } _ { \mathrm { i i } } [ \pmb { \mathcal { S } } ( \varepsilon ) ] - \pmb { v } [ \pmb { \mathcal { S } } ( 0 ) ] } { \varepsilon } \bigg \} . } \end{array}
$$

$$
\begin{array} { r l } & { \Gamma ^ { \alpha } { } _ { \beta \gamma } \equiv \langle \boldsymbol { \omega } ^ { \alpha } , \boldsymbol { \nabla } _ { \gamma } \pmb { e } _ { \beta } \rangle \qquad \left[ \begin{array} { l } { \mathrm { N o t e ~ r e v e r s a l ~ o f ~ } \beta \mathrm { ~ a n d ~ } \gamma \mathrm { ~ t o ~ m a k e ~ t h e } } \\ { \mathrm { d i f f e r e n t i a t i n g ~ i n d e x ~ c o m e ~ l a s t ~ o n ~ } T } \end{array} \right] } \\ &  \qquad \quad \begin{array} { r l } & { \qquad \quad \begin{array} { r l } & { } \\ & { \qquad \mathrm { ~ \left[ i m e ^ \alpha \mathbf { v } _ { \it \alpha \gamma } \right] ~ } } \end{array} } \\ & { \qquad = \left( \begin{array} { l } { \alpha \mathrm { ~ c o m p o n e n t ~ o f ~ c h a n g e ~ i n ~ } \pmb { e } _ { \beta } , \mathrm { ~ r e l a t i v e } } \\ { \mathrm { t o ~ p a r a l l e l ~ t r a n s p o r t , ~ a l o n g ~ } \pmb { e } _ { \gamma } } \end{array} \right) , } \end{array} \end{array}
$$

and one proves (exercise 8.l2) that

$$
\langle \pmb { \nabla } _ { \gamma } \pmb { \omega } ^ { \alpha } , \pmb { e } _ { \beta } \rangle = - { \Gamma ^ { \alpha } } _ { \beta \gamma } .
$$

In terms of these coefficients and

$$
{ T ^ { \beta } } _ { \alpha , \gamma } \equiv \nabla _ { \gamma } { T ^ { \beta } } _ { \alpha } \equiv \partial _ { \pmb { \theta } _ { \gamma } } { T ^ { \beta } } _ { \alpha } \equiv \partial _ { \gamma } { T ^ { \beta } } _ { \alpha } ,
$$

thecomponentsofthegradienteoted $T ^ { \beta } { } _ { \alpha ; \gamma } ,$

Components of gradient in arbitrary frame

$$
T ^ { \beta } { } _ { \alpha ; \gamma } = T ^ { \beta } { } _ { \alpha , \gamma } + T ^ { \beta } { } _ { \mu \gamma } T ^ { \mu } { } _ { \alpha } - T ^ { \mu } { } _ { \alpha \gamma } T ^ { \beta } { } _ { \mu }
$$

(see exercise 8.13). If the basis at the event where $\yen 7$ is calculated were a local Lorentz frame,the components of Twould just be T.Because it is not,one must correct this “Lorentz-frame”value for the twisting,turning,expansion, and contraction of the basis vectors and l-forms. The $^ { \mathfrak { s } } T T ^ { \mathfrak { s } }$ terms in equation (8.21) are the necessary corrections-one for each index of $\pmb { \tau } .$ The pattern of these correction terms is easy to remember: (l) $" + "$ sign if index being corrected is up, $^ { 6 6 } - { } ^ { 5 9 }$ sign if it is down; (2) differentiation index ( $\langle \gamma$ in above case) always at end of $\boldsymbol { r }$ ； (3) index being corrected ( $\beta$ in first term, $\pmb { \alpha }$ in second） shifts from $T$ onto $\boldsymbol { r }$ and gets replaced on $T$ by a dummy summation index $( \mu )$

Knowing the components (8.21) of the gradient, one can calculate the components of the covariant derivative $\yen 1$ by a simple contraction into $u ^ { \gamma }$ [see equation (8.17):

$$
\begin{array} { r } { \pmb { \nabla } _ { \pmb { u } } \pmb { T } = ( T ^ { \beta } { } _ { \alpha ; \gamma } u ^ { \gamma } ) \pmb { e } _ { \beta } \otimes \pmb { \omega } ^ { \alpha } . } \end{array}
$$

Components of covariant derivative

When $\pmb { u }$ is the tangent vector to a curve $\mathcal { P } ( \lambda ) , \pmb { \upsilon } = d \mathcal { P } / d \lambda$ ,one uses the notation $D T ^ { \beta } { } _ { \alpha } / d \lambda$ for the components of $\yen 1$

$$
\begin{array} { r l } & { \frac { D T ^ { \beta } _ { \alpha } } { d \lambda } \equiv T ^ { \beta } _ { \alpha ; \gamma } u ^ { \gamma } \overset { \_ } { = } T ^ { \beta } _ { \alpha ; \gamma } \frac { d x ^ { \gamma } } { d \lambda } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad  \end{array}
$$

The“”in $T ^ { \beta } { } _ { \alpha ; \gamma }$ reminds one to correct $T ^ { \beta } { } _ { \alpha , \gamma }$ with $^ { 6 6 } T T ^ { \prime \prime }$ terms; similarly, the “D” in $D T ^ { \beta } { } _ { \alpha } / d \lambda$ reminds one to correct $d T ^ { \beta } { } _ { \alpha } / d \lambda$ with $^ { 6 6 } T ^ { 7 }$ terms.

Calculation of connection coefficients from metric and commutators

This is all well and good, but how does one find out the connection coefficients $\Gamma ^ { \alpha } { } _ { \beta \gamma }$ foragivenbasisThe answer isderivedinexercise8.15.Itsays: (1)taketh metric coeficients in the given basis; (2)calculate their directional derivatives along the basis directions

$$
\begin{array} { l l } { { g _ { \beta \gamma , \mu } \equiv \partial _ { \mu } g _ { \beta \gamma } \ } } & { { = \partial g _ { \beta \gamma } / \partial x ^ { \mu } ; } } \\ { { \uparrow \ } } & { { \uparrow \ \mathrm { [ i f ~ a ~ c o o r d } } } \end{array}
$$

(3) calculate the commutation coefficients of the basis [equations (8.14) in general; $c _ { \mu \beta \gamma } = 0$ in special case of coordinate basis]; (4) calculate the “covariant connection coefficients"

$$
\begin{array} { c } { { { \cal T } _ { \mu \beta \gamma } = \displaystyle \frac { 1 } { 2 } ( g _ { \mu \beta , \gamma } + g _ { \mu \gamma , \beta } - g _ { \beta \gamma , \mu } + \underbrace { c _ { \mu \beta \gamma } + c _ { \mu \gamma \beta } - c _ { \beta \gamma \mu } } _ { \displaystyle \mathrm { \large \large \displaystyle \frac { 1 } { 2 } } } ; } } \\ { { \mathrm { \smallskip \displaystyle \ z e o r d i n a t e \ b a s i s } } } \end{array}
$$

(5）raise an index to get the connection coefficients:

$$
\begin{array} { r } { T ^ { \alpha } { } _ { \beta \gamma } = g ^ { \alpha \mu } { \cal T } _ { \mu \beta \gamma } . } \end{array}
$$

[Note on terminology: a coordinate basis always has $c _ { \alpha \beta \gamma } = 0$ , and is sometimes called holonomic; a noncoordinate basis always has some of its $c _ { \alpha \beta \gamma }$ nonzero, and is sometimes called anholonomic. In the holonomic case, the connection coefficients are sometimes called Christoffel symbols.]

The component notation, with its semicolons, commas, $D$ 's, connection coefficients, etc. looks rather formidable at first. But it bears great computational power,one discovers as one proceeds deep into gravitation theory; and its rules of manipulation are simple enough to be learned easily. By contrast, the abstract notation $( \boldsymbol { \nabla } \pmb { \tau } , \pmb { \nabla } _ { \pmb { u } } \pmb { T } ,$ etc.)is poorly suited to complex calculations; but it possesses great conceptual power.

This contrast shows clearly in the way the two notations handle the concept of geodesic.A geodesic of spacetime is a curve that is straight and uniformly parametrized,as measured in each local Lorentz frame along its way. If the geodesic is timelike,then it is a possible world line for a freely falling particle,and its uniformly ticking parameter $\lambda$ (called“affine parameter") is a multiple of the particle's proper time, $\lambda = a \tau + b$ .(Principle of equivalence: test particles move on straight lines in local Lorentz frames,and each particle's clock ticks at a uniform rate as measured by any Lorentz observer.） This definition of geodesic is readily translated into abstract, coordinate-free language: a geodesic is a curve $\mathcal { P } ( \lambda )$ that parallel-transports its tangent vector $\pmb { \upsilon } = d \mathcal { P } / d \lambda$ along itself--

Geodesic and affine parameter defined

$$
\pmb { \nabla } _ { \pmb { u } } \pmb { u } = 0 .
$$

(See Figure 10.1.) What could be simpler conceptually? But to compute the geodesic, given an initial event $\scriptstyle { \mathcal { P } } _ { o }$ and initial tangent vector $\pmb { u } ( \pmb { \mathcal { P } } _ { 0 } )$ there,one must use the component formalism. Introduce a coordinate system $x ^ { \alpha } ( { \mathcal { P } } )$ , in which $u ^ { \alpha } = d x ^ { \alpha } / d \lambda$ ， and write the component version of equation (8.25) as

$$
0 = { \frac { D ( d x ^ { \alpha } / d \lambda ) } { d \lambda } } = { \frac { d ( d x ^ { \alpha } / d \lambda ) } { d \lambda } } + \left( { T ^ { \alpha } } _ { \mu \gamma } { \frac { d x ^ { \mu } } { d \lambda } } \right) { \frac { d x ^ { \gamma } } { d \lambda } }
$$

[see equation (8.23), with one less index on $T ]$ ;i.e.,

$$
{ \frac { d ^ { 2 } x ^ { \alpha } } { d \lambda ^ { 2 } } } + { \Gamma ^ { \alpha } } _ { \mu \gamma } { \frac { d x ^ { \mu } } { d \lambda } } { \frac { d x ^ { \gamma } } { d \lambda } } = 0 .
$$

Geodesic equation

This geodesic equation can be solved (in principle) for the coordinates of the geodesic, $x ^ { \alpha } ( \lambda )$ ，when initial data $[ x ^ { \alpha }$ and $d x ^ { \alpha } / d \lambda$ at $\lambda = \lambda _ { 0 } ]$ have been specified.

The geodesics of the Earth's surface (great circles) are a foil against which one can visualize connection coefficients; see Figure 8.3.

The material of this section is presented more deeply and from a different view-point in Chapters l0 and 13. The Track-2 reader who plans to study those chapters is advised to ignore the following exercises. The Track-l reader who intends to skip Chapters 9-15 will gain necessary experience with the component formalism by working exercises 8.4-8.7. Less important to him, but valuable nonetheless,are exercises 8.8-8.15,which develop the formalism of covariant derivatives and connection coefficients in a systematic manner. The most important results of these exercises will be summarized in Box 8.6 (pages 223 and 224).

# ExerCiSe 8.4. PRACTICE IN WRITING COMPONENTS OF GRADIENT

Rewrite the following quantities in terms of ordinary derivatives $( f _ { . \gamma } \equiv \partial _ { e } f \equiv { \mathbf { v } } _ { \gamma } f )$ and $" T 7 "$ correction terms: (a) $T _ { \ ; \check { \check { Y } } }$ where $T$ is a function. (b) $T ^ { \alpha } { } _ { ; Y }$ where $\pmb { \tau }$ is a vector. (c) $T _ { \alpha ; \gamma }$ where $\pmb { \tau }$ is a 1-frm. (d) $T ^ { \alpha } { _ { \beta 8 } } ^ { \varepsilon } { _ { ; \gamma } } { \cdot }$ [Answer:

(a) $T _ { ; \gamma } = T _ { , \gamma } . \qquad ( { \mathsf { b } } ) \ T ^ { \alpha } { } _ { ; \gamma } = T ^ { \alpha } { } _ { , \gamma } + \Gamma ^ { \alpha } { } _ { \mu \gamma } T ^ { \mu } .$ (c） Ta;γ= Ta,y- Γ²aγTu.(d) $T ^ { \alpha } { } _ { \beta 8 } { } ^ { \varepsilon } { } _ { ; 7 } = T ^ { \alpha } { } _ { \beta 8 } { } ^ { \varepsilon } { } _ { ; 7 } + T ^ { \alpha } { } _ { \mu \gamma } T ^ { \mu } { } _ { \beta 8 } { } ^ { \varepsilon } - T ^ { \mu } { } _ { \beta \gamma } T ^ { \alpha } { } _ { \mu 8 } { } ^ { \varepsilon } - T ^ { \mu } { } _ { \delta \gamma } T ^ { \alpha } { } _ { \beta \mu } { } ^ { \varepsilon } + T ^ { \varepsilon } { } _ { \mu \gamma } T ^ { \alpha } { } _ { \beta 8 } { } ^ { \mu } { } .$

# EXERCISES

![](images/c4e807d7faad5206609287168bc7e886ddd3e2eae692ddd2275f4ebf9b39e611.jpg)  
Figure 8.3. The why of connection coeffcients,schematically portrayed. The aviator pursuing his great circle route from Peking to Vancouver finds himself early going north,butlater going south,although heis navigating the straightest route that is at all open to him (geodesic). The apparent change in direction indicates a turning,not in his route,but in the system of coordinates with respect to which his route is described. The vector $\pmb { v }$ of his velocity (a vector defined not on spacetime butrather on the Earth's two-dimensional surface),carried forward by parallel transport from an earlier moment to a later moment,finds itself in agreement with the velocity that he is then pursuing; or,in the abstract language of coordinate-free differential geometry,the covariant derivative $\yen 1$ vanishes along the route ("equation of a geodesic"). Though $\pmb { \nu }$ is in this sense constant,the individual pieces of which the navigator considers this vector to be built, $\pmb { \nu } = v ^ { \theta } \pmb { e } _ { \theta } + v ^ { \phi } \pmb { e } _ { \phi } ,$ are not constant.

In the language of components,the quantities $v ^ { \pmb { \theta } }$ and $v ^ { \phi }$ are changing along the route at a rate that annuls the covariant derivative of ${ \pmb v }$ thus

$$
\pmb { \nabla } _ { \pmb { v } } \pmb { v } = \pmb { a } = a ^ { \phi } \pmb { e } _ { \phi } + a ^ { \theta } \pmb { e } _ { \theta } = 0 ,
$$

or

$$
\begin{array} { c } { { 0 = a ^ { \theta } = \displaystyle \frac { d v ^ { \theta } } { d t } + \Gamma ^ { \theta } { } _ { m n } v ^ { m } v ^ { n } \mathrm { , } } } \\ { { 0 = a ^ { \phi } = \displaystyle \frac { d v ^ { \phi } } { d t } + \Gamma ^ { \phi } { } _ { m n } v ^ { m } v ^ { n } \mathrm { . } } } \end{array}
$$

In this sense the connection coefficients $T _ { ~ m n } ^ { j }$ serve as“turning coeficients” to tell how fast to“turn” the components of a vector in order to keep that vector constant (against the turning infuence of the base vectors).

Alternatively,the navigator can use an “automatic pilot system” which parallel-transports its own base vectors along the plane's route:

$$
\begin{array} { r } { \pmb { \nabla } _ { \pmb { v } } \pmb { e } _ { \theta ^ { \prime } } = \pmb { \nabla } _ { \pmb { v } } \pmb { e } _ { \phi ^ { \prime } } = 0 ; } \end{array}
$$

solid vectors at $\pmb { \mathcal { a } }$ become dotted vectors at $\clubsuit$ .Then the components of $\pmb { \nu }$ must be kept fixed to achieve a great-circle route,

$$
\frac { d v ^ { \theta ^ { \prime } } } { d t } = \frac { d v ^ { \phi ^ { \prime } } } { d t } = 0 ;
$$

and the turning coeficients are used to describe the turning of the lines of latitude and longitude relative to this parallel-transported basis:

$$
\begin{array} { r } { \pmb { \nabla } _ { \pmb { v } } \pmb { e } _ { \theta } = \pmb { e } _ { m } \varGamma ^ { m } { } _ { \theta n } \upsilon ^ { n } , } \\ { \pmb { \nabla } _ { \pmb { v } } \pmb { e } _ { \phi } = \pmb { e } _ { m } \varGamma ^ { m } { } _ { \phi n } \upsilon ^ { n } . } \end{array}
$$

Thesame turning coefficients enter into both viewpoints.The only difference is in how these coeffcients are used.

# Exercise 8.5. A SHEET OF PAPER IN POLAR COORDINATES

The two-dimensional metric for a flat sheet of paper in polar coordinates $( r , \theta )$ is $d s ^ { 2 } = d r ^ { 2 }$ $+ \ r ^ { 2 } d \phi ^ { 2 }$ -or,in modern notation, $g = d r \otimes d r + r ^ { 2 } d \phi \otimes d \phi$

(a)Calculate the connection coeffcients using equations (8.24).[Answer: $\begin{array} { r } { \hat { I } _ { \phi \phi } ^ { r } = - r ; } \end{array}$ $\begin{array} { r } { T _ { \tau \phi } ^ { \phi } = \bar { T } _ { \phi r } ^ { \phi } = 1 / r ; } \end{array}$ all othersvanish.]

(b) Write down the geodesic equation in $( r , \phi )$ .coordinates. [Answer: $d ^ { 2 } r / d \lambda ^ { 2 } -$ $r ( d \phi / d \lambda ) ^ { 2 } = 0$ ； $d ^ { 2 } \phi / d \lambda ^ { 2 } + ( 2 / r ) ( d r / d \lambda ) ( d \phi / d \lambda ) = 0 . ]$

(c） Solve this geodesic equation for $r ( \lambda )$ and $\phi ( \lambda )$ ,and show that the solution is a uniformly parametrized straight line $( x \equiv r \cos \phi = a \lambda + b$ for some $a$ and $b ; y \equiv r \sin \phi = j \lambda + k$ for some $j$ and $k$

(d) Verify that the noncoordinate basis $\pmb { e } _ { \hat { r } } \equiv \pmb { e } _ { r } = \partial \pmb { \mathcal { P } } / \partial r$ $\begin{array} { r } { \pmb { \mathscr { e } } _ { \hat { \phi } } \equiv r ^ { - 1 } \pmb { \mathscr { e } } _ { \phi } \quad r ^ { - 1 } \partial \pmb { \mathscr { P } } / \partial \phi , } \end{array}$ $\pmb { \omega } ^ { r } = \pmb { d r } , \pmb { \bar { \omega } } ^ { \hat { \phi } } = r \pmb { d \phi }$ is orthonormal,and that $\langle { \pmb { \omega } } ^ { \alpha } , { \pmb { \sigma } } _ { \beta } \rangle = \delta ^ { \hat { \alpha } } { } _ { \beta }$ .Then calculate the connection coefficients of this basis from a knowledge [part (a)] of the connection of the coordinate basis. [Answer:

$$
\begin{array} { r l } & { \Gamma ^ { \hat { \phi } } { } _ { \hat { \phi } \hat { \mathbf { r } } } = \langle \boldsymbol { \omega } ^ { \hat { \phi } } , \boldsymbol { \Psi } _ { \hat { r } } \pmb { e } _ { \hat { \phi } } \rangle = \langle r d \phi , \boldsymbol { \Psi } _ { r } ( r ^ { - 1 } \pmb { e } _ { \phi } ) } \\ & { \quad \quad \quad = r \langle d \phi , ( \pmb { \Psi } _ { r } r ^ { - 1 } ) \pmb { e } _ { \phi } + r ^ { - 1 } ( \pmb { \Psi } _ { r } \pmb { e } _ { \phi } ) \rangle = r \langle d \phi , - r ^ { - 2 } \pmb { e } _ { \phi } \rangle + \langle d \phi , \pmb { \Psi } _ { r } \pmb { e } _ { \phi } \rangle } \\ & { \quad \quad \quad = \begin{array} { r } { - r ^ { - 1 } + \displaystyle \int ^ { \phi } { } _ { \phi r } = - r ^ { - 1 } + r ^ { - 1 } = 0 ; } \end{array} } \end{array}
$$

similarly, $\Gamma _ { . } ^ { \hat { \phi } } { } _ { \hat { \tau } \hat { \phi } } = + 1 / r , \Gamma _ { . } ^ { \hat { \tau } } { } _ { \hat { \phi } \hat { \phi } } = - 1 / r ;$ all others vanish.]

(e) Consider the Keplerian orbit of Figure 8.l and $\ S 8 . 3$ as a nongeodesic curve in the sun's two-dimensional,Euclidean, equatorial plane.In place of the old notation $d \nu / d t , d e _ { \hat { r } } / d t$ ， etc.,use the new notation $\pmb { \nabla } _ { \pmb { v } } \pmb { v } , \pmb { \nabla } _ { \pmb { v } } \pmb { e } _ { \hat { \tau } }$ ,etc.Then $\pmb { v } = d \mathcal { P } / d t$ is the tangent to the orbit,and $\ b { a } = \ b { \nabla } _ { \ b { v } } \ b { v }$ is the acceleration. Derive equations (8.4) for $a ^ { \dagger }$ and $a ^ { \hat { \phi } }$ using component manipulations and connection coefficients in the orthonormal basis.

# Exercise 8.6. SPHERICAL COORDINATES IN FLAT SPACETIME

The spherical noncoordinate basis $\left\{ \pmb { e } _ { \hat { \alpha } } \right\}$ of Exercise 8.1 was orthonormal, $g _ { \hat { \alpha } \hat { \beta } } = \eta _ { \hat { \alpha } \hat { \beta } }$ ，bu1 had nonvanishing commutation coefficients [part (c) of Exercise 8.2].

(a) Calculate the connection coefficients for this basis,using equations (8.24). [Answer:

$$
\begin{array} { r l } & { \Gamma ^ { \hat { \theta } } { } _ { \hat { r } \hat { \theta } } = \Gamma ^ { \hat { \phi } } { } _ { \hat { r } \hat { \phi } } = - \Gamma ^ { \hat { r } } { } _ { \hat { \theta } \hat { \theta } } = - \Gamma ^ { \hat { r } } { } _ { \hat { \phi } \hat { \phi } } = 1 / r ; } \\ & { \Gamma ^ { \hat { \phi } } { } _ { \hat { \theta } \hat { \phi } } = - \Gamma ^ { \hat { \theta } } { } _ { \hat { \phi } \hat { \phi } } = \cot \theta / r ; } \end{array}
$$

all others vanish.]

(b) Write down expressions for $\pmb { \nabla } _ { \hat { \pmb { \alpha } } } \pmb { e } _ { \hat { \pmb { \beta } } }$ in terms of $\pmb { e } _ { \hat { \gamma } } ,$ and verify the correctness of these expressions by drawing sketches of the basis vectors on a sphere of constant $t$ and $r .$ [Answer:

$$
\begin{array} { l l } { { \pmb { \nabla } _ { \hat { \theta } } \pmb { e } _ { \hat { r } } = r ^ { - 1 } \pmb { e } _ { \hat { \theta } } , } } & { { \pmb { \nabla } _ { \hat { \theta } } \pmb { e } _ { \hat { \theta } } = - r ^ { - 1 } \pmb { e } _ { \hat { r } } , \pmb { \nabla } _ { \hat { \phi } } \pmb { e } _ { \hat { r } } = r ^ { - 1 } \pmb { e } _ { \hat { \phi } } , } } \\ { { \pmb { \nabla } _ { \hat { \phi } } \pmb { e } _ { \hat { \theta } } = ( \cot \theta / r ) \pmb { e } _ { \hat { \phi } } , } } & { { \pmb { \nabla } _ { \hat { \phi } } \pmb { e } _ { \hat { \phi } } = - r ^ { - 1 } \pmb { e } _ { \hat { r } } - ( \cot \theta / r ) \pmb { e } _ { \hat { \theta } } . } } \end{array}
$$

All others vanish.]

(c) Calculate the divergence of a vector, $\pmb { \nabla } \cdot \pmb { A } = A ^ { \hat { \alpha } } { } _ { ; \hat { \pmb { \alpha } } } .$ in this basis.[Answer:

$$
\begin{array} { r l } & { \pmb { \nabla } \cdot \pmb { A } = A ^ { \hat { t } } , \hat { \pmb { \imath } } + r ^ { - 2 } ( r ^ { 2 } A ^ { \hat { \pmb { r } } } ) , \hat { \pmb { \imath } } + ( \sin \theta ) ^ { - 1 } ( \sin \theta A ^ { \hat { \theta } } ) , \hat { \pmb { \theta } } + A ^ { \hat { \phi } } , \hat { \pmb { \phi } } } \\ & { \quad \quad = \frac { \partial A ^ { \hat { t } } } { \partial t } + \frac { 1 } { r ^ { 2 } } \frac { \partial ( r ^ { 2 } A ^ { \hat { \tau } } ) } { \partial r } + \frac { 1 } { r \sin \theta } \frac { \partial ( \sin \theta A ^ { \hat { \theta } } ) } { \partial \theta } + \frac { 1 } { r \sin \theta } \frac { \hat { c } A ^ { \hat { \phi } } } { \hat { c } \phi } . } \end{array}
$$

This answer should be familiar from flat-space vector analysis.]

# Exercise 8.7. SYMMETRIES OF CONNECTION COEFFICIENTS

Fromequation (8.24b),thesymmetryof temetrcandtheantisymetry $( c _ { \beta \gamma \mu } = - c _ { \gamma \beta \mu } )$

of the commutation_coeffcients. show that: $T _ { \alpha 1 \beta \gamma 1 } = 0$ (last two indices are symmetric) in a coordinate basis: $I _ { ( \hat { \alpha } \hat { \beta } ) \hat { \gamma } } = 0$ (first two indices are antisymmetric) in a globally orthonormal basis,gaβ = naβ

# SYSTEMATIC DERIVATION OF RESULTS IN S8.5

# ExerciSe 8.8. NEW DEFINITION OF VT COMPARED WITH OLD DEFINITION

The new definition of $\yen 7$ is given by equations (8.16) and (8.17). Use the fact that parallel transport keeps local-Lorentz components fixed to derive,from (8.16),the Lorentz-frame equation $\pmb { \nabla _ { \pmb { u } } } \pmb { \bar { T } } = T ^ { \beta } { } _ { \alpha , \gamma } u ^ { \gamma } \pmb { e } _ { \beta } \otimes \pmb { \omega } ^ { \alpha }$ :From this and equation (8.17), infer that the Lorentzframe components of $\yen 7$ are $T ^ { \beta } { } _ { \alpha , \gamma }$ --which accords with the old definition of $\forall \pmb { \tau } .$

# Exercise 8.9. CHAIN RULE FOR $\pmb { \nabla _ { \pmb { u } } } \pmb { \tau }$

(a)Use calculations in'a local Lorentz frame to show that $\because \check { \pmb { \triangledown } } _ { \pmb { \Uparrow } } ^ { \pmb { \Uparrow } }$ obeys the standard chain rule for derivatives:

$$
\nabla _ { u } ( f A \otimes B ) = ( \nabla _ { u } f ) A \otimes B + f ( \nabla _ { u } A ) \otimes B + f A \otimes ( \nabla _ { u } B ) .
$$

Here $\pmb { A }$ and $\pmb { B }$ are arbitrary vectors,1-forms,or tensors;and $f$ is an arbitrary function.[Hint: assume for concreteness that $\pmb { A }$ is a (） tensor and $\pmb { B }$ is a vector. Then this equation reads, in Lorentz-frame component notation,

$$
( f A ^ { \alpha } { } _ { \beta } B ^ { \gamma } ) _ { , \delta } u ^ { \delta } = ( f _ { , \delta } u ^ { \delta } ) A ^ { \alpha } { } _ { \beta } B ^ { \gamma } + f ( A ^ { \alpha } { } _ { \beta , \delta } u ^ { \delta } ) B ^ { \gamma } + f A ^ { \alpha } { } _ { \beta } ( B ^ { \gamma } { } _ { , \delta } u ^ { \delta } ) .
$$

(b) Rewrite equation (8.27) in component notation in an arbitrary basis. [Answer: same as (8.27'), except “,” is replaced everywhere by ";". But note that $f _ { \bar { s } } \bar { u } ^ { \bar { s } } = f _ { , \bar { s } } u ^ { \bar { s } }$ , because the function $f$ "has no components to correct".]

# Exercise 8.10. COVARIANT DERIVATIVE COMMUTES WITH CONTRACTION

(a) Let $\pmb { S }$ be a $\left( { } _ { 2 } ^ { 1 } \right)$ tensor, Using components in a local Lorentz frame show that

$\pmb { \nabla } _ { \pmb { u } }$ (contraction on slots l and 2 of $\pmb { S } ) =$ (contraction on slots l and 2 of $\yen 5$

[Hint: in a local Lorentz frame this equation makes the trivial statement

$$
\biggl ( \sum _ { \alpha } S _ { \alpha \beta } ^ { \alpha } \biggr ) _ { , \gamma } u ^ { \gamma } = \sum _ { \alpha } ( S _ { \alpha \beta , \gamma } ^ { \alpha } u ^ { \gamma } ) . ]
$$

Exercise 8.11. ALGEBRAIC PROPERTIES OF $\blacktriangledown$

Use calculations in a local Lorentz frame to show that

$$
\pmb { \nabla } _ { a \pmb { u } + b \pmb { v } } \pmb { S } = a \pmb { \nabla } _ { \pmb { u } } \pmb { S } + b \pmb { \nabla } _ { \pmb { v } } \pmb { S }
$$

for all tangent vectors ${ \pmb u } , { \pmb v }$ and numbers $a , b$ ; also that

$$
\pmb { \nabla _ { \pmb { u } } } ( \pmb { S } + \pmb { M } ) = \pmb { \nabla _ { \pmb { u } } } \pmb { S } + \pmb { \nabla _ { \pmb { u } } } \pmb { M }
$$

for any two tensor fields $\pmb { s }$ and $\pmb { M }$ of the same rank;also that

![](images/667e2aea5a26c6d23f1f6eabfc377ddb022b39e6851de4a83a8448e33a187f40.jpg)

for any two vector fields $\pmb { u }$ and ${ \pmb w } .$

# Exercise 8.12. CONNECTION COEFFICIENTS FOR 1-FORM BASIS

Show that the same connection coefficients $\Gamma ^ { \alpha } { } _ { \beta \ Y }$ that describe the changes in $\{ \pmb { e } _ { \beta } \}$ from point to point [definition (8.19a)] also describe the changes in $\{ \pmb { \omega } ^ { \alpha } \}$ , except for a change in sign [equation (8.19b)]. {Answer: (1) $\langle { \pmb { \omega } } ^ { \alpha } , { \pmb e } _ { \beta } \rangle = \delta ^ { \alpha } { } _ { \beta }$ is a constant function (O or l, depending on whether $\alpha = \beta \mathrm { \hbar }$ .(2)Thus, $\pmb { \nabla } _ { \gamma } \langle \pmb { \omega } ^ { \alpha } , \pmb { e } _ { \beta } \rangle = \partial _ { \pmb { e } _ { \gamma } } \langle \pmb { \omega } ^ { \alpha } , \pmb { e } _ { \beta } \rangle = 0 .$ (3)But $\langle \pmb { \omega } ^ { \alpha } , \pmb { e } _ { \beta } \rangle$ is the contraction of $\pmb { \omega } ^ { \alpha } \otimes \pmb { e } _ { \beta } ,$ so equation (8.28) implies $0 = \check { \Psi } _ { \boldsymbol { \ Y } }$ (contraction of $\pmb { \omega } ^ { \alpha } \otimes \pmb { \mathscr { e } } _ { \beta } )$ $=$ contraction of $[ \pmb { \nabla } _ { \gamma } ( \pmb { \omega } ^ { \alpha } \otimes \pmb { e } _ { \beta } ) ]$ (4)Apply the chain rule (8.27) to conclude ${ \boldsymbol { 0 } } =$ contraction of $[ ( \nabla _ { \gamma } \omega ^ { \alpha } ) \otimes \pmb { e } _ { \beta } + \pmb { \omega } ^ { \alpha } \otimes ( \dot { \nabla } _ { \gamma } \pmb { e } _ { \beta } ) ] = \langle \pmb { \nabla } _ { \gamma } \pmb { \omega } ^ { \alpha } , \pmb { e } _ { \beta } \rangle + \langle \pmb { \omega } ^ { \alpha } , \pmb { \nabla } _ { \gamma } \pmb { e } _ { \beta } \rangle$ (5）Finally，use definition (8.l9a) to arrive at the desired result,(8.19b).)

# Exercise 8.13.‘ $. r { \boldsymbol { \tau } } ^ { \prime \prime }$ CORRECTION TERMS FOR $\pmb { T } ^ { \beta } { } _ { \alpha : \gamma }$

Derive equation (8.21) for $T ^ { \beta } { } _ { \alpha ; \gamma }$ in an arbitrary basis by first calculating the components of $\yen 1$ for arbitrary $\pmb { u }$ ,and by then using equation (8.17) to infer the components of $\yen 1$ [Answer: (l) Use the chain rule (8.27) to get

$$
\begin{array} { r l } & { \pmb { \nabla _ { u } T } = \pmb { \nabla _ { u } } ( T ^ { \beta } \pmb { \alpha _ { \beta } } \otimes \pmb { \omega ^ { \alpha } } ) } \\ & { \quad \quad = ( \pmb { \nabla _ { u } T ^ { \beta } } \pmb { \alpha _ { \beta } } \otimes \pmb { \omega ^ { \alpha } } + T ^ { \beta } \llcorner ( \pmb { \nabla _ { u } } \pmb { e _ { \beta } } ) \otimes \pmb { \omega ^ { \alpha } } + T ^ { \beta } \llcorner \pmb { e _ { \beta } } \otimes ( \pmb { \nabla _ { u } } \pmb { \omega ^ { \alpha } } ) . } \end{array}
$$

(2） Write $\pmb { u }$ in terms of its components, $\pmb { \mu } = \pmb { u } ^ { \gamma } \pmb { e } _ { \gamma }$ ；use linearity of $\pmb { \sigma } _ { \pmb { u } }$ in ${ \pmb u }$ from equation (8.29), to get $\begin{array} { r } { \pmb { \nabla _ { u } } = u ^ { \gamma } \pmb { \nabla _ { \gamma } } } \end{array}$ and use this in $\yen 1$

$$
\pmb { \nabla _ { u } T } = u ^ { \gamma } \{ T _ { \alpha , \gamma } ^ { \beta } \pmb { e _ { \beta } } \otimes \pmb { \omega ^ { \alpha } } + T _ { \alpha } ^ { \beta } ( \pmb { \nabla _ { \gamma } } \pmb { e _ { \beta } } ) \otimes \pmb { \omega ^ { \alpha } } + T _ { \alpha } ^ { \beta } \pmb { e _ { \beta } } \otimes ( \pmb { \nabla _ { \gamma } } \pmb { \omega ^ { \alpha } } ) \} .
$$

(3）Use equations $_ { ( 8 . 1 9 a , \mathbf { b } ) }$ ,rewritten as

$$
\begin{array} { r } { \pmb { \nabla } _ { \gamma } \pmb { e } _ { \beta } = { \Gamma ^ { \mu } } _ { \beta \gamma } \pmb { \theta } _ { \mu } , \qquad \pmb { \nabla } _ { \gamma } \pmb { \omega } ^ { \alpha } = - { \Gamma ^ { \alpha } } _ { \mu \gamma } \pmb { \omega } ^ { \mu } , } \end{array}
$$

to put $\yen 1$ in the form

$$
\pmb { \nabla _ { \pmb { \mu } } } \pmb { T } = u ^ { \gamma } \{ T ^ { \beta } { } _ { \alpha , \gamma } \pmb { e } _ { \beta } \otimes \pmb { \omega } ^ { \alpha } + T ^ { \mu } { } _ { \beta \gamma } T ^ { \beta } { } _ { \alpha } \pmb { e } _ { \mu } \otimes \pmb { \omega } ^ { \alpha } - T ^ { \alpha } { } _ { \mu \gamma } T ^ { \beta } { } _ { \alpha } \pmb { e } _ { \beta } \otimes \pmb { \omega } ^ { \mu } \} .
$$

(4)Rename dummy indices so that the basis tensor ${ \pmb e } _ { \beta } \otimes { \pmb \omega } ^ { \alpha }$ can be factored out:

$$
\pmb { \nabla _ { u } } \pmb { T } = u ^ { \gamma } \{ T ^ { \beta } { } _ { \alpha , \gamma } + \bar { T ^ { \beta } } { } _ { \mu \gamma } T ^ { \mu } { } _ { \alpha } - \bar { T ^ { \mu } } { } _ { \alpha \gamma } T ^ { \beta } { } _ { \mu } \} \pmb { e } _ { \beta } \otimes \pmb { \omega } ^ { \alpha } .
$$

(5）By comparison with

$$
\begin{array} { r } { \pmb { \nabla } _ { \pmb { u } } \pmb { T } = \pmb { \nabla } \pmb { T } ( \dots , \dots , \dots , \pmb { u } ) = ( T ^ { \beta } { } _ { \alpha ; \gamma } u ^ { \gamma } ) \pmb { e } _ { \beta } \otimes \pmb { \omega } ^ { \alpha } , } \end{array}
$$

read of the value of $T ^ { \beta } { } _ { \alpha ; \gamma \cdot 1 }$

# Exercise 8.14. METRIC IS COVARIANTLY CONSTANT

Show on physical grounds (using properties of local Lorentz frames) that

$$
{ \pmb { \bigtriangledown } } \pmb { \bigtriangledown } = 0
$$

or,equivalently, that $\pmb { \bigtriangledown _ { u } } \pmb { g } = 0$ for any vector $\pmb { u }$ .Then deduce as a mathematical consequence the obviously desirable product rule

$$
\nabla _ { \boldsymbol { u } } ( A \cdot B ) = ( \nabla _ { \boldsymbol { u } } A ) \cdot B + A \cdot ( \nabla _ { \boldsymbol { u } } B ) .
$$

[Answer:(l) As discussed following equation (8.18), the components of $\yen 9$ in a local Lorentz frame are $g _ { \mu \nu , \alpha }$ Just use $\pmb { \mathscr { g } }$ for $\pmb { \tau }$ in that discusion. But these components allvanish by equation (8.15b). Therefore equation (8.33) holds in this frame,and-as a tensor equation-in all frames.(2） The product rule is also a tensor equation, true immediately via components in a local Lorentz frame.(3) Prove the product rule also the hard way,to see where equation (8.33) enters.Use the chain rule of exercise 8.9 to write

$$
\begin{array} { c } { { \pmb { \nabla _ { u } } ( g \otimes A \otimes B ) = ( \pmb { \nabla _ { u } } g ) \otimes A \otimes B + g \otimes ( \pmb { \nabla _ { u } } A ) \otimes B } } \\ { { + \pmb { g } \otimes A \otimes ( \pmb { \nabla _ { u } } B ) . } } \end{array}
$$

Use equation (8.33） to drop one term,then contract, forming

$$
\pmb { A } \cdot \pmb { B } = \mathrm { c o n t r a c t i o n } \left( \pmb { g } \otimes \pmb { A } \otimes \pmb { B } \right)
$$

and the other inner products. Exercise 8.1O is used to justify commuting the contraction with $\pmb { \sigma } _ { \pmb { u } }$ on the lefthand side.l

# Exercise 8.15. CONNECTION COEFFICIENTS IN TERMS OF METRIC

Use the fact that the metric is covariantly constant [equation (8.33)] to derive equation (8.24b) for the connection coeffcients. Treat equation (8.24c) as a definition of $\Gamma _ { \mu \beta \gamma }$ in terms of $\boldsymbol { T } ^ { \alpha } { } _ { \beta \boldsymbol { Y } } .$ [Answer: (l) Calculate the components of $\yen 9$ in an arbitrary frame:

$$
\begin{array} { r } { g _ { \alpha \beta ; \gamma } = 0 = g _ { \alpha \beta , \gamma } - { \Gamma ^ { \mu } } _ { \alpha \gamma } g _ { \mu \beta } - { \Gamma ^ { \mu } } _ { \beta \gamma } g _ { \mu \dot { \alpha } } } \\ { \equiv g _ { \alpha \beta , \gamma } - { \Gamma } _ { \beta \alpha \gamma } - { \Gamma } _ { \alpha \beta \gamma } ; \qquad } \end{array}
$$

thereby conclude that $g _ { \alpha \beta , \gamma } = 2 { \Gamma } _ { ( \alpha \beta ) \gamma } .$ (Round brackets denote symmetric part.) (2) Construct the metric terms in theclaimed answer for Pμpy:

$$
\begin{array} { r l } & { \frac { 1 } { 2 } ( g _ { \mu \beta , \gamma } + g _ { \mu \gamma , \beta } - g _ { \beta \gamma , \mu } ) = { \cal T } _ { ( \mu \beta ) \gamma } + { \cal T } _ { ( \mu \gamma ) \beta } - { \cal T } _ { ( \beta \gamma ) \mu } } \\ & { \phantom { \frac { 1 } { 2 } ( g _ { \mu \beta , \gamma } + g _ { \mu \gamma , \beta } - { \cal T } _ { \beta \mu } ) } } \\ & { \phantom { \frac { 1 } { 2 } ( g _ { \mu \beta , \gamma } + g _ { \mu \gamma , \beta } + { \cal T } _ { \mu \beta \gamma } + { \cal T } _ { \mu \gamma \beta } + { \cal T } _ { \gamma \mu \beta } - { \cal T } _ { \beta \gamma \mu } - { \cal T } _ { \gamma \beta \mu } ) } } \\ & { \phantom { \frac { 1 } { 2 } ( g _ { \mu \beta \gamma } + g _ { \mu \beta \gamma } + { \cal T } _ { \mu \beta \gamma } + { \cal T } _ { \beta [ \mu \gamma ] } + { \cal T } _ { \gamma [ \mu \beta ] } ) } } \end{array}
$$

(3）Infer fromequation (8.3l), with ${ \pmb u }$ and $\pmb { \nu }$ chosen as two basis vectors $\mathbf { \Omega } ( \pmb { u } = \pmb { e } _ { \mu } , \pmb { w } = \pmb { e } _ { \nu } ,$ 9 that

$$
c _ { \mu \nu } ^ { \rho } \pmb { e } _ { \rho } \equiv [ \pmb { e } _ { \mu } , \pmb { e } _ { \nu } ] = \pmb { \nabla } _ { \mu } \pmb { e } _ { \nu } - \pmb { \nabla } _ { \nu } \pmb { e } _ { \mu } = ( { T ^ { \rho } } _ { \nu \mu } - { T ^ { \rho } } _ { \mu \nu } ) \pmb { e } _ { \rho } = 2 { T ^ { \rho } } _ { [ \nu \mu ] } \pmb { e } _ { \rho } ;
$$

i.e.,

$$
{ \cal { T } ^ { \rho } } _ { [ \mu \nu ] } = - \mathrm { \frac { ~ 1 } { 2 ~ } } c _ { \mu \nu } { } ^ { \rho } ; \qquad \varGamma _ { \rho [ \mu \nu ] } = - \mathrm { \frac { ~ 1 } { 2 ~ } } c _ { \mu \nu \rho } .
$$

(4)This,combined with step (2) yields the desired formula for $\hat { I _ { \mu \beta \gamma ^ { \cdot } } } ]$

# $\$ 8.6$ :LOCAL LORENTZ FRAMES: MATHEMATICAL DISCUSSION

An observer falling freely in curved spacetime makes measurements in his local Lorentz frame.What he discovers has been discussed extensively in Parts Iand I of this book.Try now to derive his basic discoveries from the formalism of the last section.

Pick an event $\mathcal { P } _ { o }$ on the observer's world line.His local Lorentz frame there is a coordinate system $x ^ { \alpha } ( { \mathcal { P } } )$ in which

Local Lorentz frame:

$$
g _ { \alpha \beta } \equiv \pmb { e } _ { \alpha } \cdot \pmb { e } _ { \beta } \equiv \frac { \partial \mathcal { P } } { \partial x ^ { \alpha } } \cdot \frac { \partial \mathcal { P } } { \partial x ^ { \beta } } = \eta _ { \alpha \beta } \ \mathrm { a t } \ \mathcal { P } _ { o }
$$

(Lorentz metric at $\mathcal { P } _ { \pmb { \mathscr { o } } } )$ ,and in which

$$
\partial g _ { \alpha \beta } / \partial x ^ { \mu } = 0 \mathrm { ~ a t ~ } \mathcal { P } _ { o }
$$

(metric as Lorentz as possible near $\mathcal { P } _ { \pmb { \mathscr { o } } }$ ). [See equation (8.15).] In addition,by virtue of equations (8.24),

$$
{ \varGamma ^ { \alpha } } _ { \beta \gamma } = 0 \mathrm { ~ a t ~ } \mathcal { P } _ { o }
$$

(no “correction terms”in covariant derivatives). Of course, the observer must be at rest in his local Lorentz frame; i.e.,his world line must be

$$
x ^ { j } = x ^ { j } ( \mathcal { P } _ { o } ) = \mathrm { c o n s t a n t } ; \qquad x ^ { 0 } \mathrm { v a r y i n g } .
$$

Query:Equations (8.35) to (8.37) guarantee that the observer is at rest in a local Lorentz frame.Do they imply that he is freely falling?(They should!） Answer: Calculate the observer's 4-acceleration $\pmb { a } = d \pmb { u } / d \tau$ (notation of chapter $6 ) = \nabla _ { \mathbf { u } } \mathbf { u }$ (notation of this chapter). His 4-velocity, calculated from equation (8.37) is

Origin falls freely along a geodesic

$$
\begin{array} { r } { \pmb { \mu } = ( d x ^ { \alpha } / d \tau ) \pmb { e } _ { \alpha } = ( d x ^ { 0 } / d \tau ) \pmb { e } _ { 0 } = \pmb { e } _ { 0 } ; } \\ { \left[ \begin{array} { c } { \mathrm { b e c a u s e } \pmb { u } \mathrm { \ a n d \ } \pmb { e } _ { 0 } \mathrm { \ b o t h } } \\ { \mathrm { h a v e \ u n i t \ l e n g t h } } \end{array} \right] ^ { \dag } } \end{array}
$$

so his 4-acceleration is

$$
\begin{array} { r } { \pmb { a } = \pmb { \nabla } _ { \pmb { u } } \pmb { u } = \pmb { \nabla } _ { 0 } \pmb { e } _ { 0 } = { \Gamma } ^ { \alpha } _ { 0 0 } \pmb { e } _ { \alpha } } \\ { = 0 \mathrm { ~ a t ~ } \mathcal { P } _ { \hat { 0 } } . } \end{array}
$$

Thus, he is indeed freely falling $( \pmb { \mathscr { a } } = 0 )$ ; and he moves along a geodesice $( \nabla _ { \mathbf { \pmb { u } } } \pmb { \mu } = 0 )$ 1

Query: Do freely falling particles move along straight lines $( d ^ { 2 } x ^ { \alpha } / d \tau ^ { 2 } = 0 )$ inthe observer's local Lorentz frame at $\mathcal { P } _ { \pmb { \mathscr { o } } } \mathscr { ? }$ (They should!) Answer: A freely falling particle experiences zero 4-acceleration

Freely falling particles move on straight lines

$$
\begin{array} { r } { \pmb { a } _ { \mathrm { p a r t i c l e } } = \pmb { \nabla } _ { \pmb { u } _ { \mathrm { p a r t i c l e } } } \pmb { u } _ { \mathrm { p a r t i c l e } } = 0 ; } \end{array}
$$

i.e., it parallel-transports its 4-velocity; i.e., it moves along a geodesic of spacetime

with affine parameter equal to its proper time. The geodesic equation for its world line,in local Lorentz coordinates, says

$$
{ \begin{array} { r l } { { \frac { d ^ { 2 } x ^ { \alpha } } { d \tau ^ { 2 } } } = - { r ^ { \alpha } } _ { \mu \nu } { \frac { d x ^ { \mu } } { d \tau } } { \frac { d x ^ { \nu } } { d \tau } } } \\ { \ } & { \ } \\ & { \qquad = 0 \ \mathrm { a t } \ { \mathcal { P } } _ { o } . } \end{array} }
$$

The particle's world line is, indeed, straight at $\mathcal { P } _ { o }$

Query:Does the freely falling observer Fermi-Walker-transport his spatial basis vectors $\bullet _ { j } .$ ：i.e.,can he attach them to gyroscopes that he carries? (He should be able to!) Answer: Fermi-Walker transport (Box 6.2) would say

$$
\begin{array} { r l r } { \frac { d \pmb { e } _ { j } } { d \tau } } & { { } \equiv } & { \pmb { \nabla } _ { \pmb { u } } \pmb { e } _ { j } = \pmb { u } ( \pmb { a } \cdot \pmb { e } _ { j } ) - \pmb { a } ( \pmb { u } \cdot \pmb { e } _ { j } ) . } \end{array}
$$

But $\pmb { u } = \pmb { e } _ { 0 } , \pmb { e } _ { 0 } \cdot \pmb { e } _ { j } = 0$ ,and ${ \pmb a } = 0$ for the observer; so Fermi-Walker transport in this case reduces to parallel transport along ${ \pmb { \theta } } _ { \mathbf { 0 } }$ : thus $\pmb { \bigtriangledown } _ { 0 } \pmb { \varrho } _ { j } = 0$ .This is,indeed, how $\pmb { e } _ { j }$ is transported through $\mathcal { P } _ { o }$ ,because

$$
\begin{array} { r } { \pmb { \nabla } _ { 0 } \pmb { e } _ { j } = { \cal T } ^ { \alpha } { } _ { j 0 } \pmb { e } _ { \alpha } = 0 \mathrm { a t } \mathcal { P } _ { o } . } \end{array}
$$

# \$8.7. GEODESIC DEVIATION AND THE RIEMANN CURVATURE TENSOR

“Gravitation is a manifestation of spacetime curvature, and that curvature shows up in the deviation of one geodesic from a nearby geodesic (relative acceleration of test particles).”To make this statement precise, first quantify the “deviation”or “relative acceleration” of neighboring geodesics.

Focus attention on a family of geodesics ${ \mathcal { P } } ( \lambda , n )$ ； see Figure 8.4. The smoothly varying parameter $\pmb { n }$ ("selector parameter") distinguishes one geodesic from the next. For fixed $_ n$ ， $\mathcal { P } ( \lambda , n )$ is a geodesic with affine parameter $\lambda$ and with tangent vector

$$
\pmb { \mu } = \hat { \sigma } \mathcal { P } / \hat { \partial } \lambda ;
$$

thus $\pmb { \bigtriangledown _ { \pmb { u } } } \pmb { u } = 0$ (geodesic equation). The vector

$$
\pmb { n } \equiv \partial \mathcal { P } / \partial n
$$

measures the separation between points with the same value of $\lambda$ on neighboring geodesics.

An observer falling freely along the“fiducial geodesic” $n = 0$ watches a test particle fall along the“test geodesic"” $n = 1$ . The velocity of the test particle relative to him he quantifies by $\yen 1$ ，This relative velocity, like the separation vector ${ \pmb n } ,$ ， is an arbitrary “initial condition.”Not arbitrary,however,is the “relative acceleration,” $\yen 1$ of the test particle relative to the observer (see Boxes I1.2 and 11.3). It would be zero in flat spacetime. In curved spacetime,it is given by

![](images/eec624dcfe9caf76ee09de7f33491625cecde122804216239382d9ad4064c903.jpg)  
Figure 8.4. A family of geodesics ${ \mathcal { P } } ( \lambda , n )$ 、The selector parameter $n$ tells“which”geodesic;the affine parameter $\lambda$ tells“where”on a given geodesic. The separation vector $\pmb { \eta } \equiv \hat { \sigma } ^ { \mathrm { s p } } / \partial n$ at a point $\mathcal { P } ( \lambda , 0 )$ along the fiducial geodesic, $n = 0$ ,reaches (approximately） to the point $^ { g p } ( \lambda , 1 )$ with the same value of $\lambda$ on the test geodesic, $n = 1$ 、

$$
\begin{array} { r } { \forall _ { u } \forall _ { u } n + R i e m a n n \left( . . . , u , n , u \right) = 0 , } \end{array}
$$

Riemann curvature tensor defined by relative acceleration of geodesics

or, in component notation,

$$
\frac { D ^ { 2 } n ^ { \alpha } } { d \lambda ^ { 2 } } + R ^ { \alpha } { } _ { \beta \gamma \delta } u ^ { \beta } n ^ { \gamma } u ^ { \delta } = 0 .
$$

This equation serves as a definition of the“Riemann curvature tensor;"and it can also be used to derive the following expressions for the components of Riemann ina coordinate basis:

Components of Riemann

$$
\begin{array} { r l } & { R ^ { \alpha } { } _ { \beta \gamma \delta } = \langle d x ^ { \alpha } , [ \Psi _ { \gamma } , \Psi _ { \delta } ] \pmb { e } _ { \beta } \rangle } \\ & { \quad \quad \quad = \frac { \partial { \cal T } ^ { \alpha } { } _ { \beta \delta } } { \partial x ^ { \gamma } } - \frac { \partial { \cal T } ^ { \alpha } { } _ { \beta \gamma } } { \partial x ^ { \delta } } + { \cal T } ^ { \alpha } { } _ { \mu \gamma } { \cal T } ^ { \mu } { } _ { \beta \delta } - { \cal T } ^ { \alpha } { } _ { \mu \delta } { \cal T } ^ { \mu } { } _ { \beta \gamma } . } \end{array}
$$

(For proof,read Box I1.4, Box l1.5.and exercise 11.3,in that order.) For a glimpse of the man who first analyzed the curvature of spaces with three and more dimensions, see Box 8.5.

Spacetime curvature causes not only geodesic deviation, but also route dependence in parallel transport (parallel transport around a closed curve changes a vector or tensor-Box l1.7)； it causes covariant derivatives to fail to commute equation (8.44)}; and it prevents the existence of a global Lorentz coordinate system (S11.5).

At first sight one might think Riemann has $4 \times 4 \times 4 \times 4 = 2 5 6$ independent components. But closer examination $( \ S 1 3 . 5 )$ reveals a variety of symmetries

$$
R _ { \alpha \beta \gamma \delta } = R _ { [ \alpha \beta ] [ \gamma \delta ] } = R _ { [ \gamma \delta ] [ \alpha \beta ] } , \qquad R _ { [ \alpha \beta \gamma \delta ] } = 0 , \qquad R _ { \alpha [ \beta \gamma \delta ] } = 0
$$

# Box 8.5 GEORG FRIEDRICH BERNHARD RIEMANN

September 17, 1826, Breselenz, Hanover-July 20, 1866, Selasca, Lake Maggiore

![](images/7d49a684eea05616c150f4d548a5b252b192295a8d0ce4b1f1e863bf77e6cc76.jpg)

With his famous doctoral thesis of l85l,“Foundations for a general theory of functions of a single complex variable,”Riemann founded one branch of modern mathematics (the theory of Riemann surfaces)；and with his famous lecture of three years later founded another (Riemannian geometry).These and other writings will be found in his collected works,edited by H. Weber (1953).

"The properties which distinguish space from other conceivable triply-extended magnitudes are only to be deduced from experience.... At every point the three-directional measure of curvature can have an arbitrary value if only the effective curvature of every measurable region of space does not differ noticeably from zero.”[G. F. B. Riemann,“On the hypotheses that lie at the foundations of geometry,”Habilitationsvorlesung of June 10,1854,on entry into the philosophical faculty of the University of Gotingen.]

Dying of tuberculosis twelve years later, occu-(antisymmetry on first two indices; antisymmetry on last two; -symmetry under exchange of first pair with last pair; vanishing of completely antisymmetric parts). These reduce Riemann (in four dimensions) from 256 to 20 independent components.

Besides these algebraic symmetries, Riemann possesses differential symmetries called “Bianchi identities,”

$$
R ^ { \alpha } { } _ { \beta [ \lambda \mu ; \nu ] } = 0 ,
$$

which have deep geometric significance (Chapter 15).

From Riemann one can form several other curvature tensors by contraction. The easiest to form are the “Ricci curvature tensor,”

pied with an attempt at a unified explanation of gravity and electromagnetism, Riemann communicated to Betti his system of characterization of multiply-connected topologies (which opened the door to the view of electric charge as “lines of force trapped in the topology of space"),making use of numbers that today are named after Betti but that are identified with a symbol, $R _ { n }$ ,that honors Riemann.

“A more detailed scrutiny of a surface might disclose that what we had considered an elementary piece in reality has tiny handles attached to it which change the connectivity character of the piece,and that a microscope of ever greater magnification would reveal ever new topological complications of this type,ad infinitum.The Riemann point of view allows, also for real space,topological conditions entirely different from those realized by Euclidean space.Ibelieve that only on the basis of the freer and more general conception of geometry which had been brought out by the development of mathematics during the last century,and with an open mind for the imaginative possibilities which it has revealed,can a philosophically fruitful attack upon the space problem be undertaken." H. Weyl (1949, p. 91).

“But...physicists were still far removed from such a way of thinking; space was still, for them, a rigid, homogeneous something,susceptible of no change or conditions. Only the genius of Riemann, solitary and uncomprehended,had already won its way by the middle of the last century to a new conception of space,in which space was deprived of its rigidity,and in which its power to take part in physical events was recognized as possible.” A.Einstein (1934,p. 68).

Riemann formulated the first known model for superspace (for which see Chapter 43),a superspace built,however, not of the totality of all 3- geometries with positive definite Riemannian metric (the dynamic arena of Einstein's general relativity), but-of all conformally equivalent closed Riemannian 2-geometries of the same topology, a type of superspace known today as Teichmüller space,for more on Riemann's contributions to which and the subsequent development of which, see the chapters by L. Bers and J. A. Wheeler in Gilbert and Newton (1970).

Ricci curvature tensor

$$
R _ { \mu \nu } \equiv R _ { ~ \mu \alpha \nu } ^ { \alpha } \stackrel { _ = } { _ \mathrm { \tiny ~ \left\{ ~ \right\} ~ } } r _ { ~ \mu \nu , \alpha } ^ { \alpha } - { \cal T } _ { ~ \mu \alpha , \cdot } ^ { \alpha } + { \cal T } _ { ~ \beta \alpha } ^ { \alpha } { \cal T } _ { ~ \mu \cdot } ^ { \beta } - { \cal T } _ { ~ \beta \nu } ^ { \alpha } { \cal T } _ { ~ \mu \alpha } ^ { \beta } ,
$$

and the“scalar curvature,"

Scalar curvature

$$
R \equiv R ^ { \mu } { } _ { \mu } .
$$

But of much greater geometric significance is the“Einstein curvature tensor”

Einstein curvature tensor

$$
{ G ^ { \mu } } _ { \nu } \equiv \frac { 1 } { 2 } \varepsilon ^ { \mu \alpha \beta \gamma } R _ { \beta \gamma } ^ { \rho \sigma } \frac { 1 } { 2 } \varepsilon _ { \nu \alpha \rho \sigma } = R ^ { \mu } _ { \nu } - \frac { 1 } { 2 } \delta ^ { \mu } _ { \nu } R .
$$

Of all second-rank curvature tensors one can form by contracting Riemann, only Einstein $= \pmb { G }$ retains part of the Bianchi identities (8.46): it satisfies

Contracted Bianchi identities

$$
{ \cal G } _ { ; \nu } ^ { \mu \nu } = 0 .
$$

For the beautiful geometric meaning of these “contracted Bianchi identities”("the boundary of a boundary is zero"), see Chapter 15.

Box 8.6 summarizes the above equations describing curvature,as well as the fundamental equations for covariant derivatives.

[The following exercises from Track 2 are appropriate for the Track-l reader who wishes to solidfy his understanding of curvature: 11.6,11.9,11.10,13.7-11,and 14.3.]

# Exercise 8.16. SOME USEFUL FORMULAS IN COORDINATE FRAMES

In any coordinate frame,define $g$ to be the determinant of the matrix $g _ { \alpha \beta }$ [equation 8.11] Derive the following relations,valid in any coordinate frame.

(a) Contraction of connection coefficients:

$$
{ \Gamma ^ { \alpha } } _ { \beta \alpha } = ( \ln \sqrt { - \cdot } g ) _ { , \beta } .
$$

[Hint: Use the results of exercise 5.5.]

(b） Components of Ricci tensor:

$$
R _ { \alpha \beta } = \frac { 1 } { \sqrt { - g } } ( \sqrt { - g } { \cal { \Gamma } } ^ { \mu } { } _ { \alpha \beta } ) _ { , \mu } - ( \ln \sqrt { - g } ) _ { , \alpha \beta } - { \cal { \Gamma } } ^ { \mu } { } _ { \nu \alpha } { \cal { T } } ^ { \nu } { } _ { \beta \mu } .
$$

(c) Divergence of a vector $A ^ { \alpha }$ or antisymmetric tensor $F ^ { \alpha \beta }$ ：

$$
{ A ^ { \alpha } } _ { ; \alpha } = { \frac { 1 } { \sqrt { - g } } } ( { \sqrt { - g } } A ^ { \alpha } ) _ { , \alpha } , { F ^ { \alpha \beta } } _ { ; \beta } = { \frac { 1 } { \sqrt { - g } } } ( { \sqrt { - g } } F ^ { \alpha \beta } ) _ { , \beta } .
$$

(d) Integral of a scalar field $\Psi$ Over the proper volume of a 4-dimensional region $\mathcal { V }$ ：

$$
\int _ { \mathcal { V } } \Psi d ( { \mathrm { p r o p e r ~ v o l u m e } } ) = \int _ { \mathcal { V } } \Psi { \sqrt { - g } } d t d x d y d z .
$$

[Hint: In a localLorentz frame, $d ( \mathrm { p r o p e r v o l u m e } ) = d t d \hat { x } d \hat { y } d \hat { z } ,$ Usea Jacobian to transform this volume element to the given coordinate frame,and prove from the transformation law

$$
g _ { \alpha \beta } = \frac { \partial x ^ { \hat { \mu } } } { \partial x ^ { \alpha } } \frac { \partial x ^ { \hat { \nu } } } { \partial x ^ { \beta } } \eta _ { \mu \nu }
$$

that the Jacobian is equal to ${ \sqrt { - g } } . ]$

Box 8.6 COVARIANT DERIVATIVE AND CURVATURE: FUNDAMENTAL EQUATIONS   

<table><tr><td>Entity</td><td>Abstract notation</td><td>Component notation</td></tr><tr><td>Covariant Derivative</td><td>Vut = vT(....... u)</td><td>Ta;yuY = DTB/dX (u=dp/d) dT +(TB,T-r'aT）uu d</td></tr><tr><td>algebraic properties (Exercise 8.11)</td><td>uf=auf= &lt;df,u) Vau+bvT =aT+ bT (S+M)=S+M</td><td>faua=fua TB(auY+bu）=TY +bTUY (s+M=S+M</td></tr><tr><td>chain rule</td><td>uw ~ ∀wu = [u,w] for u, w both vector fields (AB)=(A)B+A(B) fA)=(uSA+A</td><td>rP{μp]=- p[equation (8.34)] （AB)u²=AB;Buu+ABY:uu</td></tr><tr><td>Vu and contraction commute</td><td>(contraction of S) =(contraction of S)</td><td>（fAaB）uu=fABu+fAaB;uu (∑soay)u=∑(Sayixu) T ;μ α</td></tr><tr><td>*metric covariantly constant</td><td>Vug = 0</td><td>gaβ;yuY =0</td></tr><tr><td>Gradient</td><td>4T</td><td>TPa;y=TBay+reyTa- rαyTB</td></tr><tr><td>Connection Coefficients</td><td>raBy=&lt;w,eB） =-&lt;,ua,e&gt;</td><td>raBy=garμBy* FBy= 2(gupy+8uy.B-8u</td></tr><tr><td></td><td></td><td>+ Cμβγ +CμγB -CBγμ）* Cβyu= 8u = gμa&lt;wα,[eβ,eγl&gt;*</td></tr><tr><td>Local Lorentz frame at 90 Parallel trans- port</td><td>Vs = 0</td><td>Coordinate system with gμ(9）=nμ raBy(9）=0 SaB;uY =0</td></tr><tr><td>Entity</td><td colspan="2">Abstract notation Component noiation</td></tr><tr><td>Geodesic Equation</td><td>4uu = 0 Riemann (σ.C.A.B)三(σ.(A.B)C)</td><td>d²x/dx²+ r. (dxu/d)(dx/d)=0 in a coordinate basis</td></tr><tr><td>Riemann Curvature Tensor</td><td>(A.B)三[A:B-A.B) (not track-one formulas: see Chapter I1)</td><td>arags arBy RBy6 = 2xY ax + roμyrB-raur"BY in coordinate frame</td></tr><tr><td>Ricci Curvature Tensor</td><td>Ricci = contraction on slots land3ofRiemann</td><td>[see equation (l1.13) for formula in non- coordinate frame] Rμ=Rαμav=Ta-raa+raβrβup -rr in coordinate frame</td></tr><tr><td>*Curvature Scalar</td><td>R=(contraction of Ricci)</td><td>R= R</td></tr><tr><td>*Einstein Curvature Tensor</td><td>G = Ricci - gR</td><td>Gaβ= RaB-8aR Useful formulas for computing Gα&amp; (derived in §14.2): Go=-(R1212 + R223+ R3131）,</td></tr><tr><td></td><td></td><td>G1=-(RO²02 + R03+ R²323),</td></tr><tr><td>*Symmetries of Curvature Tensors</td><td></td><td>G1= R1020 + R1323, etc. Raβγ&amp;=R[aβ}ys]=R[γs]laβ},R[aβγs1=O,Ra[βγs=0 Rβ=R(aβ).Gaβ= G(aB)</td></tr><tr><td>Bianchi Identities</td><td></td><td>Rβ{x:x = 0</td></tr><tr><td>*Contracted Bianchi Identities</td><td></td><td>Ga=0</td></tr><tr><td>Geodesic Deviation</td><td>un+ Riemann(...,u.n,u) = 0</td><td>D²na +RaBy8uβnYu=0 d</td></tr><tr><td>Parallel Transport around closed</td><td>δA + Riemann (...A.u,v) = 0 if u,v are edges of curve</td><td>SAα+RαBy8AβuYu=0</td></tr></table>

\*If metric is absent,these starred formulas cannot be formulated.Allother formulas are valid in absence of metric.
