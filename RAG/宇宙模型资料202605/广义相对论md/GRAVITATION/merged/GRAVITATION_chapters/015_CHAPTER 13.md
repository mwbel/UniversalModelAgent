# CHAPTER 13

# RIEMANNIAN GEOMETRY: METRIC AS FOUNDATION OF ALL

Philosophy is written in this great book (by which 丨 mean the universe) which stands always open to our view,but it cannot be understood unless one first learns how to comprehend the language and interpret the symbols in which it is written,and its symbols are triangles,circlas,and other geometric figures, without which it is not humanly possible to comprehend even one word of it;without these one wanders in a dark labyrinth.

GALILEO GALILEI (1623)

This chapter is entirely Track 2.   
Chapters $\bullet - 1 1$ are necessary   
preparation for it. It will be   
needed as preparation for (1） the second half of Chapter 14 (calculation of curvature), and (2) the details,but not the message,of Chapter 15 (Bianchi identities).

$\$ 123.6$ (proper reference frame) will be useful throughout the applications of gravitation theory (Chapters 18-40).

Constraints imposed on spacetime by special relativity

# $\$ 13.1$ . NEW FEATURES IMPOSED ON GEOMETRY BY LOCAL VALIDITY OF SPECIAL RELATIVITY

Freely falling particles (geodesics) define and probe the structure of spacetime. This spacetime is curved. Gravitation is a manifestation of its curvature.So far,so good, in terms of Newton's theory of gravity as translated into geometric language by Cartan.What is absolutely unacceptable, however,is the further consequence of the Cartan-Newton viewpoint (Chapter l2): stratification of spacetime into slidable slices,with no meaning for the spacetime separation between an event in one slice and an event in another.

Of all the foundations of physics, none is more firmly established than special relativity;and of all the lessons of special relativity none stand out with greater force than these.(l） Spacetime,far from being stratified,is homogeneous and isotropic throughout any region small enough ("local region"） that gravitational tide-producing effects ("spacetime curvatures") are negligible. (2) No local experiment whatsoever can distinguish one local inertial frame from another. (3) The speed of light is the same in every local inertial frame. (4) It is not possible to give frame-independent meaning to the separation in time ("no Newtonian stratification").(S） Between every event and every nearby event there exists a frame-independent, coordinate-independent spacetime interval("Riemannian geometry"). (6) Spacetime is always and everywhere locally Lorentz in character("local Lorentz character of this Riemannian geometry").

What mathematics gives all these physical properties? A metric: a metric that is locally Lorentz ( $\mathfrak { S 8 } 1 3 . 2$ and l3.6).All else then follows. In particular, the metric destroys the stratified structure of Newtonian spacetime, as well as its gravitational potential and universal time coordinate. But not destroyed are the deepest features of Newtonian gravity: (l） the equivalence principle (as embodied in geodesic description of free-fall motion, $\ S \ S 1 3 . 3$ and 13.4); and (2） spacetime curvature (as measured by tidal effects. $\ S 1 3 . 5 )$

The skyscraper of vectors, forms, tensors (Chapter 9), geodesics, parallel transport, covariant derivative (Chapter lO), and curvature (Chapter Il） has rested on crumbling foundations-Newtonian physics and a geodesic law based on Newtonian physics.But with metric now on the scene,the whole skyscraper can be transferred to new foundations without a crack appearing. Only one change is necessary: the geodesic law must be selected in a new,relativistic way; a way based on metric $( \ S \ S 1 3 . 3$ and l3.4). Resting on metric foundations, spacetime curvature acquires additional and stronger properties (the skyscraper is redecorated and extended), which are studied in $\ S 1 3 . 5$ and in Chapters l4 and I5,and which lead almost inexorably to Einstein's field equation.

Metric: the instrument which imposes the constraints

# $\$ 12$ .METRIC

A spacetime metric: a curved spacetime metric; a locally Lorentz, curved spacetime metric. This is the foundation of spacetime geometry in the real, physical world. Therefore take a moment to recall what “metric” is in three contrasting languages.

In the language of elementary geometry.“metric” is a table giving the interval between every event and every other event $\mathbf { ( B o x ~ l 3 . l }$ and Figure l3.1). In the language of coordinates,“metric” is a set of ten functions of position, $g _ { \mu \nu } ( x ^ { \alpha } )$ ,such that the expression

$$
\varDelta s ^ { 2 } = - \varDelta \tau ^ { 2 } = g _ { \mu \nu } ( x ^ { \alpha } ) \varDelta x ^ { \mu } \varDelta x ^ { \nu }
$$

# Metric described in three languages

gives the interval between any event $x ^ { \alpha }$ and any nearby event $x ^ { \alpha } + 4 x ^ { \alpha }$ In the language of abstract differential geometry， metric is a bilinear machine, $\pmb { \sigma } \equiv ( \dots \dots \dots )$ .te produce a number ["scalar product ${ \pmb g } ( { \pmb u } , { \pmb v } ) \equiv ( { \pmb u } \cdot { \pmb v } ) ^ { * } ]$ out of two tangent vectors. $\pmb { u }$ and ${ \pmb v } .$

The link between the abstract. machine viewpoint and the concrete coordinate viewpoint is readily exhibited. Let the tangent vector

$$
\pmb { \xi } \equiv \pmb { \varDelta } \mathrm { r } ^ { \alpha } \pmb { e } _ { \alpha } = \pmb { \varDelta } \mathrm { r } ^ { \alpha } ( \hat { \partial } / \hat { c } \pmb { x } ^ { \alpha } )
$$

represent the displacement between two neighboring events. The abstract viewpoint gives

$$
\mathbf { 1 } \mathfrak { s } ^ { : } \equiv \boldsymbol { \xi } \cdot \boldsymbol { \xi } \equiv g ( \mathbf { 1 } \mathfrak { x } ^ { \mu } \pmb { e } _ { \mu } . \mathbf { \mathcal { A } } \mathfrak { x } ^ { : \prime } \pmb { e } _ { \nu } ) = \mathbf { 4 } \mathfrak { x } ^ { \mu } \mathbf { 3 } \mathfrak { x } ^ { \nu } \pmb { g } ( \pmb { e } _ { \mu } . \pmb { e } _ { \nu } )
$$

(tontinued on page 310)

# Box 13.1 METRIC DISTILLED FROM DISTANCES

# Raw Data on Distances

Let the shape of the earth be described as in Figure l3.l,by giving distances between some of the principal identifiable points: buoys. ships, icebergs,lighthouses, peaks, and flags: points to a total of $n = 2 \times 1 0 ^ { 7 }$ . The total number of distances to be given is $n ( n - 1 ) / 2 = 2 \times 1 0 ^ { 1 4 }$ .With 2Oo distances per page of printout, this means

<table><tr><td>First point</td><td>Second point</td><td>Distance (Nautical miles)</td><td>First point</td><td>Seco pr</td></tr><tr><td>9,316,434</td><td>14,117,103</td><td>1410.316</td><td>9,316.434</td><td></td></tr><tr><td>9.316,434</td><td>14.117,104</td><td>1812.717</td><td>9,316,434</td><td></td></tr><tr><td>9,316,434</td><td>14,117,105</td><td>1629.291</td><td>9.3</td><td></td></tr><tr><td>921/4</td><td>14 </td><td></td><td></td><td></td></tr></table>

$1 0 ^ { 1 2 }$ pages weighing $6 \ { \tt g }$ each, or $6 \times 1 0 ^ { 6 }$ metric tons of data. With 6 tons per truck this means $1 0 ^ { 6 }$ truckloads of data; or with one truck passing by every 5 seconds, $5 \times 1 0 ^ { 6 }$ seconds or 2 months of night and day traffc to get in the data.

![](images/0bb12ea6a8b469300578dd8841d409944557902a55b9f23f1cc5c3d9a06ffd19.jpg)

# First Distillation: Distances to Nearby Points Only

Get distances between faraway points by adding distances covered on the elementary short legs of the trip.Boil down the table of distances to give only the distance between each point and the hundred nearest points. Now have $1 0 0 ~ n = 2 \times 1 0 ^ { 9 }$ distances, or $2 \times 1 0 ^ { 9 } / 2 0 0 = 1 0 ^ { 7 }$ pages of data, or 60 tons of records, or l0 truckloads..

# Second Distillation: Distances Between Nearby Points in Terms of Metric

Idealize the surface of the earth as smooth. Then in any sufficiently limited region the geometry is Euclidean. This circumstance has a happy consequence. It is.enough to know a few distances between the nearby points to be able to determine all the

distances between the nearby points.Locate point 2 so that (lO2) is a right triangle; thus, $( 1 2 ) ^ { 2 } = ( 1 0 ) ^ { 2 } + ( 2 0 ) ^ { 2 }$ Consider a point 3 close to 0. Define

$$
x ( 3 ) = ( 1 3 ) - ( 1 0 )
$$

and

$$
y ( 3 ) = ( 2 3 ) - ( 2 0 ) .
$$

Then the distance (O3) does not have to be supplied independently; it can be calculated from the formula\*

$$
( 0 3 ) ^ { 2 } = [ x ( 3 ) ] ^ { 2 } + [ y ( 3 ) ] ^ { 2 } .
$$

Similarly for a point 4 and its distance (O4) from the local origin O. Similarly for the distance $( m n )$ between any two points $m$ and $n$ that are close to 0:

$$
( m n ) ^ { 2 } = [ x ( m ) - x ( n ) ] ^ { 2 } + [ y ( m ) - y ( n ) ] ^ { 2 } .
$$

Thus it is only needful to have the distance $( 1 m )$ (from point l） and $( 2 m )$ (from point 2) for each point m close to 0 $( m = 3 , 4 , \dots , N + 2 )$ to be able to work out

$$
\left( \begin{array} { l } { \mathrm { v o f u m e ~ o f } } \\ { n \mathrm { - d i m e n s i o n a l } } \\ { \mathrm { s i m p l e x } } \\ { \mathrm { s p a n n e d ~ b y } } \\ { ( n + 1 ) \mathrm { p o i n t s } } \end{array} \right) = \left( \frac { ( - 1 ) ^ { n + 1 } } { 2 ^ { n } } \right) ^ { 1 / 2 } \frac { 1 } { n ! } \left| \begin{array} { l l l l l l } { 0 } & { 1 } & { 1 } & { 1 } & { \ldots } & { 1 } \\ { 1 } & { 0 } & { ( 0 1 ) ^ { 2 } } & { ( 0 2 ) ^ { 2 } } & { \ldots } & { ( 0 n ) ^ { 2 } } \\ { 1 } & { ( 1 0 ) ^ { 2 } } & { 0 } & { ( 1 2 ) ^ { 2 } } & { \ldots } & { ( 1 n ) ^ { 2 } } \\ { \ldots } & { \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot } \\ { 1 } & { ( n 0 ) ^ { 2 } } & { ( n 1 ) ^ { 2 } } & { ( n 2 ) ^ { 2 } } & { \ldots } & { 0 } \end{array} \right|
$$

$$
\begin{array} { c } { { \mathrm { a r e a } = \big \{ s \big [ s - ( 0 1 ) \big ] \big [ s - ( 0 2 ) \big ] \big [ s - ( 1 2 ) \big ] \big \} ^ { 1 / 2 } . } } \\ { { 2 s = ( 0 1 ) + ( 0 2 ) + ( 1 2 ) . } } \end{array}
$$

for the area of a triangle. Conversely. if the four points are to remain in two-dimensional Euchdean space.the tetrahedron must collapse to zero volume. This requirement supplies one condition on the one distance (O3).It simplifies the discussion of this condition to take (O3)smalland(IO2)to be a right triangle. as above. However. the general principle i、 independent of such approximations.and follows directly from the extended Hero-Tartaglia formula. It is enough in a locally Euclidean or Lorentz space of $n$ dimensions to have laid down $( n + 1 )$ fiducial points $0 , 1 . 2 . \dots n$ and to know the distance of every other point $j , k , \dots$ from these fiducial points. in order to be able to calculate the distance of these pointsj. k...from one another(distances between nearby points in terms of coordinates": metric as distilation of distance data).

its distance from every point $_ n$ close to 0. The prescription to determine the $N ( N - 1 ) / 2$ distances between these $N$ nearby points can be reexpressed to advantage in these words: (l) each point has two coordinates, $x$ and $y \cdot$ and (2) the distance is given in terms of these coordinates by the standard Euclidean metric; thus

$$
( \varDelta s ) ^ { 2 } = ( \varDelta x ) ^ { 2 } + ( \varDelta y ) ^ { 2 } .
$$

Having gone this far on the basis of“distance geometry” (for more on which,see Robb i9i4 and l936),one can generalize from a smallregion (Euclidean) to a large region (not Euclidean). Introduce any arbitrary smooth pair of everywhere-independent curvilinear coordinates $x ^ { k }$ ,and express distance, not only in the immediate neighborhood of the point O, but also in the immediate neighborhood of every point of the surface (except places where one has to go to another coordinate patch;at least two patches needed for 2-sphere) in terms of the formula

$$
d s ^ { 2 } = g _ { j k } d x ^ { j } d x ^ { k } .
$$

Thus out of the table of distances between nearby points one has distilled now five numbers per point (two coordinates, $x ^ { 1 } , x ^ { 2 }$ , and three metric coefficients, $g _ { 1 1 } , g _ { 1 2 } =$ $g _ { 2 1 }$ and $g _ { 2 2 } )$ ，down bya factor of $1 0 0 / 5 = 2 0 $ from what one had before (now 3 tons of data,or half a truckload).

# Third Distillation: Metric Coefficients Expressed as Analytical Functions of Coordinates

Instead of giving the three metric coefficients at each of the $2 \times 1 0 ^ { 7 }$ points of the surface,give them as functions of the two coordinates $x ^ { 1 } , x ^ { 2 }$ ,in terms of a power series or an expansion in spherical harmonics or otherwise with some modest number, say l00,of adjustable coefficients. Then the information about the geometry itself (as distinct from the coordinates of the $2 \times 1 0 ^ { 7 }$ points located on that geometry) is caught up in these three hundred coefficients, a single page of printout. Goodbye to any truck!In brief,metric provides a shorthand way of giving the distance between every point and every other point-but its role,its justification and its meaning lies in these distances and only in these many distances.

![](images/775ed2c40f3f70628979759e07c9c6ed380163a084588ec8794bf1a65227c8c6.jpg)  
Figure 13.1. 1 Distances determine geometry.Upper left: Sufciently great tidal forces,applied to theearth with tailored timing,have deformed it to the shape of a tear drop.Lower left: This tear drop is approximated by apolyhedron built out of triangles (skeleton geometry").The approximation can be madearbitrarily goodby making the number of triangles sufciently great and the size of each sufficiently small. Upper right:The geometry in each triangle is Euclidean: giving the three edge lengths fixes all the features of the figure,including the indicated angle.Lower right: The triangles that belong to a given vertex, laid out on a fat surface,fail to meet.The deficit angle measures the amount of curvature concentrated at that vertex on the tear-drop earth. The sum of these deficit angles for all vertices of the tear drop equals $4 \pi$ .This“Gauss-Bonnet theorem”is valid for any figure with the topology of the 2-sphere； for the simplest figure of all,a tetrahedron,four vertices with a deficit angle at each of $\mathfrak { l } 8 0 ^ { \circ }$ are needed-3 triangles $\times 6 0 ^ { \circ }$ per triangle available $= 1 8 0 ^ { \circ }$ deficit.In brief.the shape of the tear drop,in the given skeleton-geometry approximation,is determined by its 50 visible edge lengths plus.say,32 more edge lengths hidden behind the figure,oratotal of82 edge lengths,and by nothing more("distances determine geometry")."Metric" tells the distance between every point and every nearby point. If volcanic action raises Rejkjavik,the distances between that Icelandic capital and nearby points increase accordingly: distances again reveal shape.Conversely,that there is not a great bump on the earth in the vicinity of Iceland,and that the earth does not now have a tear-drop shape,can be unambiguously established byanalyzing the pattern of distances from point to point in a sufficiently well-distributed network of points,with no call for any observations other than measurements of distance.

for the interval between those events: comparison with the coordinate viewpoint [equation (13.1)] reveals

Covariant components of metric

$$
g _ { \mu \nu } = g ( e _ { \mu } , e _ { \nu } ) = e _ { \mu } \cdot e _ { \nu }
$$

"Line element"' compared with “metric as bilinear machine"

(standard equation for calculating components of a tensor).

Just as modern differential geometry replaces the old style“differential” df by the “differential form”df(Box 2.3,page 63), so it also replaces the old-style “line element"

$$
d s ^ { 2 } = g _ { \mu \nu } d x ^ { \mu } d x ^ { \nu } = ( { \mathrm { " i n t e r v a l ~ b e t w e e n ~ } } x ^ { \alpha } { \mathrm { ~ a n d ~ } } x ^ { \alpha } + d x ^ { \alpha } { \mathrm { " ) } }
$$

by the bilinear machine ("metric tensor")

$$
g \equiv d s ^ { 2 } \equiv g _ { \mu \nu } d x ^ { \mu } \otimes d x ^ { \nu } .
$$

Metric produces a correspondence between 1-forms and tangent vectors

The output ${ \pmb g } ( { \pmb \xi } , { \pmb \xi } )$ of this machine,for given displacement-vector input, is identical to the old-style interval. Hence, $d s ^ { 2 } = g _ { \mu \nu } \ : d x ^ { \mu } \otimes d x ^ { \nu }$ represents the interval of an unspecified displacement; and the act of inserting $\pmb { \xi }$ into the slots of $\pmb { d } \pmb { s } ^ { 2 }$ is the act of making explicit the interval $g ( \xi , \xi ) = g _ { \mu \nu } \ : \varDelta x ^ { \mu } \ : \varDelta x ^ { \nu }$ of an explicit displacement.

In curved spacetime with metric, just as in flat spacetime with metric $( \ S 2 . 5 )$ ,a particular 1-form $\widetilde { \pmb { u } }$ corresponds to any given tangent vector $\pmb { u }$

("representation of the same physical quantity in the two alternative versions of vector and 1-form”;"corresponding representations”as $( _ { 0 } ^ { 1 } )$ -tensor and as $\ l ^ { ( 0 ) }$ -tensor). Example: the 1-form $\widetilde { \pmb { u } }$ corresponding to a basis vector $\pmb { \mu } = \pmb { e } _ { \alpha }$ has components

$$
\begin{array} { r l } & { \boldsymbol { u } _ { \beta } = \langle \widetilde { \pmb { u } } , \pmb { e } _ { \beta } \rangle \equiv g ( \pmb { u } , \pmb { e } _ { \beta } ) = \pmb { g } ( \pmb { e } _ { \alpha } , \pmb { e } _ { \beta } ) = \pmb { g } _ { \alpha \beta } ; } \\ & { \left[ \mathrm { s t a n d a r d ~ w a y ~ } \right] \overset { \mathrm { \scriptsize ~ \textstyle ~ \displaystyle ~ \displaystyle ~ } } { \longrightarrow } \left[ \begin{array} { l } { \qquad \qquad \mathrm { \textstyle ~ \displaystyle ~ \sum ~ } _ { [ \mathrm { \scriptsize ~ e q u a t i o n ~ ( 1 \cdot ~ c ) } ] } } \\ { \qquad \mathrm { \textstyle ~ \displaystyle ~ [ b y ~ } \pmb { u } = \pmb { e } _ { \alpha } ] } \end{array} \right. } \\ & { \qquad \mathrm { \quad ~ \displaystyle ~ } [ \mathrm { d e f i n i t i o n ~ } ( 1 3 . 5 ) ] . } \end{array}
$$

thus

Also as in flat spacetime $( \ S 3 . 2 )$ ,a tensor can accept either a vector or a 1-form into any given slot

$$
\pmb { S } ( \widetilde { \pmb { u } } , \pmb { \sigma } , \pmb { v } ) \equiv \pmb { S } ( \pmb { u } , \pmb { \sigma } , \pmb { v } ) .
$$

Lowering indices

Equivalently,in component language, the indices of a tensor can be lowered with the covariant components of the metric

$$
\begin{array} { r } { S _ { \alpha } { } ^ { \beta } { } _ { \gamma } = S ( \pmb { e } _ { \alpha } , \omega ^ { \beta } , \pmb { e } _ { \gamma } ) = S ( \tilde { \pmb { e } } _ { \alpha } , \omega ^ { \beta } , \pmb { e } _ { \gamma } ) = S ( g _ { \alpha \mu } \omega ^ { \mu } , \omega ^ { \beta } , \pmb { e } _ { \gamma } ) = g _ { \alpha \mu } S ^ { \mu \beta } { } _ { \gamma } , } \\ { \dot { \mathrm { ~ \ ` ~ } } [ \operatorname* { d e f i n i t i o n ~ o f ~ } S _ { \alpha } { } ^ { \beta } { } _ { \gamma } ] } \end{array}
$$

The basis vectors $\{ \pmb { \mathscr { e } } _ { \alpha } \}$ can be chosen arbitrarily at each event. Therefore the corresponding components $g _ { \alpha \beta }$ of the metric are quite arbitrary (though symmetric: $g _ { \alpha \beta } = g _ { \beta \alpha } )$ . But the mixed components $g ^ { \alpha } { } _ { \beta }$ are not arbitrary. In particular,equations (13.5) and (13.7) imply

$$
\pmb { g } ( \widetilde { \pmb { u } } , \pmb { v } ) \equiv \pmb { g } ( \pmb { u } , \pmb { v } ) \equiv \langle \widetilde { \pmb { u } } , \pmb { v } \rangle .
$$

Therefore one concludes that the metric tensor in mixed representation is identical with the unit matrix:

Mixed and contravariant components of metric

$$
g ^ { \alpha } { } _ { \beta } \equiv g ( \omega ^ { \alpha } , \pmb { e } _ { \beta } ) \equiv \langle \pmb { \omega } ^ { \alpha } , \pmb { e } _ { \beta } \rangle = \delta ^ { \alpha } { } _ { \beta } .
$$

This feature of the metric in turn fixes the contravariant components of the metric:

$$
\begin{array} { r } { g ^ { \alpha \mu } g _ { \mu \beta } = g ^ { \alpha } { } _ { \beta } = \delta ^ { \alpha } { } _ { \beta } ; } \\ { \mathrm { L } _ { [ \mathrm { ' l o w e r i n g } ] } } \end{array}
$$

i.e.,

$$
| | g ^ { \alpha \beta } | | \ \mathrm { i s \ t h e \ m a t r i x \ i n v e r s e \ o f \ } | | g _ { \alpha \beta } | | .
$$

This reciprocity enables one to undo the lowering of tensor indices (i.e.,raise indices) Raising indices with $g ^ { \alpha \beta }$ ：

$$
S ^ { \mu \beta } { } _ { \gamma } = \delta ^ { \mu } { } _ { \alpha } S ^ { \alpha \beta } { } _ { \gamma } = g ^ { \mu \nu } g _ { \nu \alpha } S ^ { \alpha \beta } { } _ { \gamma } = g ^ { \mu \nu } S _ { \nu } { } ^ { \beta } { } _ { \gamma } .
$$

The last two paragraphs may be summarized in brief:

（2） $\begin{array} { l } { { g _ { _ { \beta } } ^ { \alpha } = \delta ^ { \alpha } { } _ { \beta } ; } } \\ { { | | g ^ { \alpha \beta } | | = | | g _ { \alpha \beta } | | ^ { - 1 } ; } } \end{array}$ (3) tensor indices are lowered with $g _ { \alpha \beta }$ ； (4） tensor indices are raised with $g ^ { \alpha \beta }$

In this formalism of metric and index shufling,a big question demands attention: how can one tell whether the metric is locally Lorentz rather than locally Euclidean or locally something else? Of course, one criterion (necessary； not sufficient!） is dimensionality-a locally Lorentz spacetime must have four dimensions. (Recall the method of $\ S 1 . 2$ to determine dimensionality.） Confine attention, then, to fourdimensional manifolds. What else must one demand? One must demand that at every event $\mathcal { P }$ there exist an orthonormal frame (orthonormal set of basis vectors $\{ \pmb { \mathscr { e } } _ { \hat { \alpha } } \} )$ in which the components of the metric have their flat-spacetime form

$$
g _ { \hat { \alpha } \hat { \beta } } \equiv e _ { \hat { \alpha } } \cdot e _ { \hat { \beta } } = \eta _ { \alpha \beta } \equiv \mathrm { d i a g o n a l } ~ ( - 1 , 1 , 1 , 1 ) .
$$

To test for this is straightforward (exercise 13.1). (l） Search for a timelike vector $\pmb { u } \left( \pmb { u } \cdot \pmb { u } < 0 \right)$ . If none exist, spacetime is not locally Lorentz. If one is found, then (2） examine all non-zero vectors $\pmb { v }$ perpendicular to ${ \pmb u } .$ If they are all spacelike $( { \pmb v } \cdot { \pmb v } > 0 )$ , then spacetime is locally Lorentz. Otherwise it is not.

Metric must be locally Lorentz

# Exercise 13.1. TEST WHETHER SPACETIME IS LOCAL LORENTZ

Prove that the above two-step procedure for testing whether spacetime is locally Lorentz is valid: i.e.. prove that if the procedure says“yes." then there exists an orthonormal basis with $g _ { \hat { \alpha } \hat { \beta } } = \eta _ { \alpha \beta }$ at the event in question; if it says “no.” then no such basis exists.

# Exercise 13.2. PRACTICE WITH METRIC

A four-dimensional manifold with coordinates $v , r , \theta , \phi$ has line element (old-style notation)

$$
d s ^ { 2 } = { } - ( 1 - 2 M / r ) d { v ^ { 2 } } + 2 d { v } d r + r ^ { 2 } ( d \theta ^ { 2 } + \mathrm { s i n ^ { 2 } } \theta d \phi ^ { 2 } ) ,
$$

corresponding to metric (new-style notation)

$$
d \pmb { \mathscr { s } } ^ { 2 } = - ( 1 - 2 M / r ) d \nu \otimes d v + d v \otimes d r + d r \otimes d v + r ^ { 2 } ( d \theta \otimes d \theta + \sin ^ { 2 } \theta d \phi \otimes d \phi ) ,
$$

where $M$ is a constant.

(a)Find the“covariant"components $g _ { \alpha \beta }$ and“contravariant"components $g ^ { \alpha \beta }$ of the metric in this coordinate system. [Answer: $g _ { v v } \dot { = } - ( 1 - 2 M / r )$ ， $g _ { v r } = g _ { r v } = 1$ ， $g _ { \theta \theta } = r ^ { 2 }$ ， $g _ { \phi \phi } = r ^ { 2 }$ $\sin ^ { 2 } \theta$ ； all other $g _ { \alpha \beta }$ vanish; $g ^ { v r } = g ^ { r v } = 1$ ， $g ^ { r r } = ( 1 - 2 M / r )$ ， $g ^ { \theta \theta } = r ^ { - 2 }$ ， $g ^ { \phi \phi } = r ^ { - 2 } \sin ^ { - 2 } \theta ,$ all other $g ^ { \alpha \beta }$ vanish.J

(b) Define a scalar field $t$ by

$$
t \equiv v - r - 2 M \ln [ ( r / 2 M ) - 1 ] .
$$

What are the covariant and contravariant components ( $\operatorname { \Pi } _ { \langle u _ { \alpha } \rangle }$ and $u ^ { \alpha }$ ）of the 1-form $\widetilde { \pmb { v } } \equiv { \pmb { d } } t ^ { \mathcal { T } } ;$ What is the squared length $\pmb { \upsilon } ^ { 2 } \equiv \pmb { \upsilon } \cdot \pmb { u }$ ,of the corresponding vector? Show that $\pmb { u }$ is timelike in the region $r > 2 M ,$ [Answer: $u _ { v } = 1$ ， $u _ { r } = - 1 / ( 1 \AA ^ { - 2 } M / r )$ ， $u _ { \theta } = u _ { \phi } = 0$ ； $u ^ { v } = - 1 / ( 1 -$ $2 M / r )$ ， $u ^ { r } = 0$ ， $u ^ { \theta } = u ^ { \phi } = 0$ ； $\begin{array} { r } { \pmb { \upsilon } ^ { 2 } = - 1 / ( 1 - 2 M / r ) . } \end{array}$ ]

(c) Find the most general non-zero vector orthogonal to $\bar { \pmb { \upsilon } }$ in the region $r > 2 M ,$ and show that it is spacelike. Thereby conclude that spacetime is locally Lorentz in the region $r > 2 M ,$ [Answer: Since $w \cdot u = w _ { \alpha } u ^ { \alpha } = - w _ { v } / ( 1 - 2 M / r )$ ， $w _ { v }$ must vanish, but $w _ { r } , ~ \boldsymbol { w } _ { \theta } , ~ \boldsymbol { w } _ { \phi }$ are arbitrary,and $w ^ { 2 } = ( 1 - 2 M / r ) w _ { r } ^ { ~ 2 } + r ^ { - 2 } w _ { \theta } ^ { ~ 2 } + r ^ { - 2 } \sin ^ { - 2 } \theta w _ { \phi } ^ { ~ 2 } > 0 . ]$

(d) Let $t , r , \theta , \phi$ be new coordinates for spacetime.Find the line element in this coordinate system.[Answer:This is the“Schwarzschild”line element

$$
d s ^ { 2 } = { } - \left( 1 - { \frac { 2 M } { r } } \right) d t ^ { 2 } + { \frac { d r ^ { 2 } } { 1 - 2 M / r } } + r ^ { 2 } d \theta ^ { 2 } + r ^ { 2 } \sin ^ { 2 } \theta d \phi ^ { 2 } .
$$

(e）Find an orthonormal basis,for which $g _ { \hat { \alpha } \hat { \beta } } = \eta _ { \alpha \beta }$ in the region $r > 2 M$ [Answer:$\bullet _ { \widehat { 0 } } \equiv ( 1 - 2 M / r ) ^ { - 1 / 2 } \partial / \partial t$ ， $\begin{array} { r } { \pmb { e } _ { \hat { r } } \equiv ( 1 - 2 M / r ) ^ { 1 / 2 } \partial / \hat { \sigma } r } \end{array}$ ， $\pmb { e } _ { \hat { \theta } } \equiv r ^ { - 1 } \partial / \partial \theta$ ， $\pmb { e } _ { \hat { \phi } } = ( r \sin \theta ) ^ { - 1 } \hat { c } / \partial \phi . ]$

# $\$ 123.3$ .CONCORD BETWEEN GEODESICS OF CURVED SPACETIME GEOMETRY AND STRAIGHT LINES OF LOCAL LORENTZ GEOMETRY

More could be said about the mathematical machinery and physical implications of "metric,” but an issue of greater urgency presses for attention. What has metric (or spacetime interval) to do with geodesic (or world line of test particle)? Answer:

Two mathematical objects ("straight line in a local Lorentz frame” and“geodesic of the over-all global curved spacetime geometry") equal to the same physical object ("world line of test particle") must be equal to each other ("condition of consistency"). As a first method to spell out this consistency requirement, examine the two mathematical representations of the world line of a test particle in the neighborhood of a given event $\mathcal { P } _ { 0 }$ . The local-Lorentz representation says:

“Pick a local Lorentz frame at $\mathcal { P } _ { 0 }$ [As spelled out in exercise 13.3,such a local Lorentz frame is the closest thing there is to a global Lorentz frame at $\mathcal { P } _ { 0 }$ ；i.e., it is a coordinate system in which

$$
\begin{array} { r l } & { \mathrm {  { \mathcal E } } _ { \alpha \beta } (  { \mathcal P } _ { 0 } ) = \eta _ { \alpha \beta } \mathrm {  { \left( \mathrm { \mathrm { H a t } } \mathrm { - } s p a c e t i m e \mathrm { \ m e t r i c } \right) } } , } \\ & { \mathrm {  { \mathcal E } } _ { \alpha \beta , \gamma } (  { \mathcal P } _ { 0 } ) = 0 , } \end{array}
$$

$g _ { \alpha \beta , \gamma \delta } ( \mathcal { P } _ { 0 } ) \neq 0$ except in special cases, such as flat space.]

The world line in that frame has zero acceleration,

Local-Lorentz description of straight lines

$$
d ^ { 2 } x ^ { \alpha } / d \tau ^ { 2 } = 0 \mathrm { ~ a t ~ } \hat { \mathcal { P } } _ { 0 } \mathrm { ~ ( ^ { * } s t r a i g h t \mathrm { - } l i n e ~ e q u a t i o n " ) , }
$$

where $\tau$ is proper time as measured by the particle's clock.”

The geodesic representation says

“In the local Lorentz frame, as in any coordinate frame, the world line satisfies the geodesic equation

Geodesic description of straight lines

$$
d ^ { 2 } x ^ { \alpha } / d \tau ^ { 2 } + { \cal { T } } ^ { \alpha } { } _ { \beta \gamma } ( d x ^ { \beta } / d \tau ) ( d x ^ { \gamma } / d \tau ) = 0
$$

$\tau$ is an affine parameter because it is time as measured by the test particle's clock)." Consistency of the two representations for any and every choice of test particle (any and every choice of $d x ^ { \alpha } / d \tau$ at ${ \mathcal { P } } _ { 0 }$ ）demands

Condition of consistency: y = 0 in local Lorentz frame

i.e., it demands that every,local Lorentz frame is a local inertial frame. (On local inertial frames see $\ S 1 1 . 6 . )$ In such a frame,allocal effects of "gravitation” disappear. That is the physical shorthand for (13.18).

One does not have to speak in the language of a specific coordinate system when one demands identity between the geodesic (derived from the $\Gamma ^ { \alpha } { } _ { \beta \gamma } )$ and the straight line of the local Lorentz geometry $( g _ { \mu \nu } )$ . The local Lorentz specialization of coordinates may be the most immediate way to see the physics ("no local effects of gravitation"), but it is not the right way to formulate the basic mathematical requirement in its full generality and power. The right way is to demand

$$
\begin{array} { r } { \pmb { \nabla } \pmb { g } = 0 ( ^ { \mathfrak { c } \mathfrak { c } } \mathrm { c o m p a t i b i l i t y ~ o f ~ } \pmb { g } \mathrm { ~ a n d ~ } \pmb { \nabla } ^ { \prime \prime } ) . } \end{array}
$$

Stated in the language of an arbitrary coordinate system, this requirement reads

Consistency reformulated: $\pmb { \bigtriangledown } \pmb { \mathfrak { g } } = 0$

$$
g _ { \alpha \beta ; \gamma } \equiv \frac { \partial g _ { \alpha \beta } } { \partial x ^ { \gamma } } - { \Gamma ^ { \mu } } _ { \alpha \gamma } g _ { \mu \beta } - { \Gamma ^ { \mu } } _ { \beta \gamma } g _ { \alpha \mu } = 0 .
$$

That this covariant requirement is fulfilled in every coordinate system follows from its validity in one coordinate system: a local Lorentz frame. (The first term in this equation,and the last two terms,are separately required to vanish in the local Lorentz frame at point $\mathcal { P } _ { 0 }$ -and required to vanish by the physics.) From $\pmb { \nabla } _ { \pmb { g } } = 0$ ， One can derive both the abstract chain rule

$$
\nabla _ { u } \left( v \cdot w \right) = ( \nabla _ { u } v ) \cdot w + v \cdot ( \nabla _ { u } w )
$$

(Exercise 13.4） and the following equations for the connection coefficients in any frame in terms of (l) the metric coefficients, $g _ { \alpha \beta } = \pmb { e } _ { \alpha } \cdot \pmb { e } _ { \beta }$ ,and (2） the covariant commutation coefficients

$$
c _ { \alpha \beta \gamma } \equiv c _ { \alpha \beta } ^ { \mu } g _ { \mu \gamma } \equiv \langle \pmb { \omega } ^ { \mu } , [ \pmb { e } _ { \alpha } , \pmb { e } _ { \beta } ] \rangle g _ { \mu \gamma }
$$

of that frame:

$$
\begin{array} { c } { { T ^ { \alpha } { } _ { \beta \gamma } = g ^ { \alpha \mu } { \cal T } _ { \mu \beta \gamma } \qquad \mathrm { ( d e f n i t i o n ~ o f } ~ { \cal T } _ { \mu \beta \gamma } \mathrm { ) , } } } \\ { { { } } } \\ { { { \cal T } _ { \mu \beta \gamma } = \displaystyle { \frac { 1 } { 2 } \left( g _ { \mu \beta , \gamma } + c _ { \mu \beta \gamma } + g _ { \mu \gamma , \beta } + c _ { \mu \gamma \beta } - g _ { \beta \gamma , \mu } - c _ { \beta \gamma \mu } \right) } } } \\ { { { } } } \\ { { { } = \displaystyle { \frac { 1 } { 2 } \left( g _ { \mu \beta , \gamma } + g _ { \mu \gamma , \beta } - g _ { \beta \gamma , \mu } \right) } ~ \mathrm { i n ~ a n y ~ c o o r d i n a t e ~ f r a n } } } \end{array}
$$

(See Exercise 13.4).

Equations (13.23) are the connection coefficients required to make the geodesics of curved spacetime coincide with the straight lines of the local Lorentz geometry. And they are fixed uniquely; no other choice of connection coefficients will do the job!

Summary: in curved spacetime with a local Lorentz metric,the following seemingly different statements are actually equivalent: (l） the geodesics of curved spacetime coincide with the straight lines of the local Lorentz geometry; (2) every local Lorentz frame [coordinates with $g _ { \alpha \beta } ( \mathcal { P } _ { 0 } ) = \eta _ { \alpha \beta } .$ $g _ { \alpha \beta , \gamma } ( \mathcal { P } _ { 0 } ) = 0 ]$ is a local inertial frame $\lbrack { T ^ { \alpha } { } _ { \beta \gamma } } ( \mathcal { P } _ { 0 } ) = 0 ] ,$ ：(3）the metric and covariant derivative satisfy the compatibility condition $\pmb { \nabla } _ { \pmb { g } } = 0$ ; (4) the covariant derivative obeys the chain rule (13.2O); (S) the connection coefficients are determined by the metric in the manner of equations (13.23).A sixth equivalent statement, derived in the next section, says (6) the geodesics of curved spacetime coincide with world lines of extremal proper time.

# EXERCISES

# Exercise 13.3. MATHEMATICAL REPRESENTATION OF LOCAL LORENTZ FRAME

By definition,a local Lorentz frame at a given event $\mathcal { P } _ { 0 }$ is the closest thing there to a global Lorentz frame. Thus, it should be a coordinate system with $g _ { \mu \nu } ( \mathcal { P } _ { 0 } ) = \eta _ { \mu \nu } ,$ and with as many derivatives of $g _ { \mu \nu }$ as possible vanishing at $\scriptstyle { \mathcal { P } } _ { 0 }$ Prove that there exist coordinates in which $g _ { \mu \nu } ( \mathcal { P } _ { 0 } ) = \eta _ { \mu \nu }$ and $g _ { \mu \nu , \rho } ( \mathcal { P } _ { 0 } ) = 0$ ,but that $g _ { \mu \nu , \rho \sigma } ( \mathcal { P } _ { 0 } )$ cannot vanish in general. Hence, such coordinates are the mathematical representation of a local Lorentz frame.[Hint: Let $\{ x ^ { \alpha ^ { \prime } } ( { \mathcal { P } } ) \}$ be an arbitrary but specific coordinate system,and $\{ x ^ { \mu } ( { \mathcal { P } } ) \}$ be a local Lorentz frame,both with origins at $\mathscr { P } _ { 0 }$ . Expand the coordinate transformation between the two in powers of $x ^ { \mu }$

$$
x ^ { \alpha ^ { \prime } } = { M ^ { \alpha } } _ { \mu } x ^ { \mu } + \frac { 1 } { 2 } { N ^ { \alpha } } _ { \mu \nu } x ^ { \mu } x ^ { \nu } + \frac { 1 } { 6 } { P ^ { \alpha } } _ { \mu \nu \rho } x ^ { \mu } x ^ { \nu } x ^ { \rho } + \ldots ;
$$

and use the transformation matrix $L ^ { \alpha ^ { \prime } } { } _ { \mu } \equiv \hat { \sigma } x ^ { \alpha ^ { \prime } } / \hat { \sigma } x ^ { \mu }$ to get $g _ { \mu \nu } ( \mathcal { P } _ { 0 } )$ ， $g _ { \mu \nu , \rho } ( \mathcal { P } _ { 0 } )$ ,and $g _ { \mu \nu , \rho \sigma } ( \mathcal { P } _ { 0 } )$ in terms of $g _ { \alpha ^ { \prime } \beta ^ { \prime } }$ anditid $M ^ { \alpha } { } _ { \mu } , N ^ { \alpha } { } _ { \mu \nu } , P ^ { \alpha } { } _ { \mu \nu \rho } .$ Show that whatever $g _ { \alpha ^ { \prime } \beta ^ { \prime } }$ may be (so long as it is nonsingular, so exists!),one can choose the 16 constants $M ^ { \alpha } { } _ { \mu }$ to make $g _ { \mu \nu } = \eta _ { \mu \nu }$ (ten conditions)； one can choose the $4 \times 1 0 = 4 0$ constants $N ^ { \gamma } { } _ { \mu \nu }$ to make the $1 0 \times 4 = 4 0 \ : g _ { \mu \nu , \rho } ( \mathcal { P } _ { 0 } )$ vanish; but one cannot in general choose the $4 \times 2 0 =$ $8 0 ~ P ^ { \alpha } { } _ { \mu \nu \rho }$ to make the $1 0 \times 1 0 = 1 0 0 g _ { \mu \nu , \rho \sigma }$ vanish.]

# Exercise 13.4. CONSEQUENCES OF COMPATIBILITY BETWEEN $\pmb { \mathscr { g } }$ AND $\blacktriangledown$

(a) From the condition of compatibility $\pmb { \bigtriangledown } \pmb { \mathfrak { g } } = 0$ ,derive the chain rule (13.20). (b) From the condition of compatibility $\pmb { \bigtriangledown } \pmb { \mathfrak { g } } = 0$ and definitions (13.21) and (13.22), derive equation (13.23) for the connection coefficients. [Answer: See exercise 8.15,p. 216.]

# $\$ 123.4$ .GEODESICS AS WORLD LINES OF EXTREMAL PROPER TIME

In a local Lorentz frame, it is easy to distinguish a world line that is straight from one that is not. Position the Lorentz frame and so orient it that the starting point of the world line, $\boldsymbol { \mathcal { Q } }$ ,lies at the origin and the end point, $\it { \Omega } ^ { \it { \Delta } }$ ,lies at $x = 0 , y = 0$ ， $z = 0 , t = T .$ As an example of a nonstraight world line, consider passage at uniform velocity from $\boldsymbol { \mathcal { Q } }$ to point $\mathcal { P }$ .with coordinates $( \textstyle { \frac { 1 } { 2 } } T ; 0 , 0 , { \frac { 1 } { 2 } } R )$ and from there again with uniform velocity to point $\mathcal { B }$ The lapse of proper time from start to finish ("length of world line") is

![](images/449a44e24742d5cfad4a7304b1572d0fea19013b690a1d67d934399d9d58494c.jpg)

$$
\tau = ( T ^ { 2 } - R ^ { 2 } ) ^ { 1 / 2 } .
$$

Thus the lapse of proper time is diminished from its straight-line value,and diminished moreover for any choice of $R$ whatsoever, except for the zero or straight-line value $R = 0$ .As for this simple nonstraight curve, so also for any other nonstraight curve: the lapse of proper time between $\boldsymbol { \mathcal { Q } }$ and $\mathcal { B }$ is less than the straight-line lapse (Exercise 6.3). Thus, in flat spacetime,extremal length of world line is an indicator of straightness.

Any local region of the curved spacetime of the real, physical world is Lorentz in character. In this local Lorentz geometry, it is easy to set up Lorentz coordinates and carry out the extremal-length analysis just sketched to distinguish between a straight line and a nonstraight line:

$$
\begin{array} { l } { { \displaystyle \tau = \int _ { d } ^ { \varphi } d \tau = \int _ { d } ^ { \varphi \rangle } ( - \eta _ { \mu \nu } d x ^ { \mu } d x ^ { \nu } ) ^ { 1 / 2 } } } \\ { { \displaystyle \quad = \left( \begin{array} { l } { { \mathrm { a ~ m a x i m u m ~ f o r ~ s t r a i g h t ~ l i n e } } } \\ { { \mathrm { a s ~ c o m p a r e d ~ t o ~ a n y ~ v a r i a n t ~ o f } } } \\ { { \mathrm { t h e ~ s t r a i g h t ~ l i n e } } } \end{array} \right) . } } \end{array}
$$

In flat spacetime,straight lines have extremal length

Extremal length in curved spacetime

Such a test for straightness can be carried out separately in each local Lorentz region along the world line, or, with greater efficiency, it can be carried out over many local Lorentz regions simultaneously, i.e.,over a region with endpoints $\boldsymbol { \mathcal { q } }$ and $\mathfrak { B }$ so widely separated that no single Lorentz frame can possibly contain them both. To carry out the analysis, one must abandon local Lorentz coordinates. Therefore introduce a general curvilinear coordinate system and find

$$
{ \begin{array} { r l } & { \tau = \int _ { \mathcal { a } } ^ { \varphi ^ { 3 } } d \tau = \int _ { \mathcal { a } } ^ { \varphi ^ { 3 } } ( - g _ { \mu \nu } d x ^ { \mu } d x ^ { \nu } ) ^ { 1 / 2 } } \\ & { \qquad = { \Biggl ( } { \mathrm { i s ~ s t r a i g h t ~ i n ~ e a c h ~ l o c a l ~ L o r e n t l d ~ l i n e ~ t h a t } } } \\ & { \qquad = { \Biggl ( } { \mathrm { i s ~ s t r a i g h t ~ i n ~ e a c h ~ l o c a l ~ L o r e n t z ~ f r a m e } } } \\ & { \qquad { \mathrm { a l o n g ~ i t s ~ p a t h , ~ a s ~ c o m p a r e d ~ t o ~ a n y ~ } } ^ { * } { \mathrm { n e a r b y } } ^ { \prime } { \mathrm { , } } { \Biggr ) } . } \end{array} }
$$

In the real world,the path of extremal $\tau$ , being straight in every local Lorentz frame, must be a geodesic of spacetime.

Notice that the word “maximum” in equation (l3.24) has been replaced by "extremum” in the statement (13.25). When $\boldsymbol { \mathcal { Q } }$ and $\boldsymbol { \mathcal { B } }$ are widely separated, they may be connected by several different geodesics with differing lapses of proper time (Figure 13.2). Each timelike geodesic extremizes $\tau$ with respect to nearby deformations of itself, but the extremum need not be a maximum. When several distinct geodesics connect two events, the typical one is not a local maximum ("mountain peak") but a saddle point ("mountain pass") in such a diagram as Figure 13.2 0r 13.3.

Concord between locally straight lines (lines of extremal $\tau$ )and geodesics of curved spacetime demands that timelike geodesics have extremal proper length. If so, then any curve $x ^ { \mu } ( \lambda )$ between $\boldsymbol { \mathcal { Q } }$ (where $\lambda = 0$ and $\mathcal { B }$ (where $\lambda = 1$ ）that extremizes $\tau$ should satisfy the geodesic equation. To test for an extremal by comparing times, pick a curve suspected to be a geodesic,and deform it slightly but arbitrarily:

Along either curve the lapse of proper time is

$$
\tau = \int _ { d } ^ { \varepsilon \beta } d \tau = \int _ { 0 } ^ { 1 } \left( - g _ { \mu \nu } { \frac { d x ^ { \mu } } { d \lambda } } { \frac { d x ^ { \nu } } { d \lambda } } \right) ^ { 1 / 2 } d \lambda .
$$

At fixed $\lambda$ the metric coefficient $g _ { \mu \nu } [ x ^ { \alpha } ( \lambda ) ]$ differs from one curve to the other by

$$
\delta g _ { \mu \nu } \equiv g _ { \mu \nu } [ a ^ { \alpha } ( \lambda ) + \delta a ^ { \alpha } ( \lambda ) ] - g _ { \mu \nu } [ a ^ { \alpha } ( \lambda ) ] = { \frac { \partial g _ { \mu \nu } } { \partial x ^ { \sigma } } } \delta a ^ { \sigma } ( \lambda ) ;
$$

and the components $d x ^ { \prime } / d \lambda$ of the tangent vector differ by

$$
\delta \left( \frac { d x ^ { \nu } } { d \lambda } \right) \equiv \frac { d ( a ^ { \nu } + \delta a ^ { \nu } ) } { d \lambda } - \frac { d a ^ { \nu } } { d \lambda } = \frac { d } { d \lambda } ( \delta a ^ { \nu } ) .
$$

These changes in $g _ { \mu \nu }$ and $d x ^ { \nu } / d \lambda ,$ at fixed $\lambda$ , produce corresponding changes in the lapse of proper time in equation (13.27):

$$
\delta \tau = \int _ { 0 } ^ { 1 } \biggl \{ \frac { - g _ { \mu \nu } ( d a ^ { \mu } / d \lambda ) d ( \delta a ^ { \nu } ) / d \lambda - \frac { 1 } { 2 } ( g _ { \mu \nu , \sigma } \delta a ^ { \sigma } ) ( d a ^ { \mu } / d \lambda ) ( d a ^ { \nu } / d \lambda ) } { [ - g _ { \gamma \delta } ( d a ^ { \gamma } / d \lambda ) ( d a ^ { \delta } / d \lambda ) ] ^ { 1 / 2 } } \biggr \} d \lambda . \biggr .
$$

Integrate the first term by parts. Strike out the end-point terms, because both paths must pass through $\boldsymbol { \mathcal { Q } }$ and $\mathcal { B }$ $\delta a ^ { \mu } = 0$ at $\lambda = 0$ and $\lambda = 1$ ). Thus find

$$
\delta \tau = \int _ { \lambda = 0 } ^ { \lambda = 1 } f _ { \sigma } ( \lambda ) \ : \delta a ^ { \sigma } \left[ - g _ { \gamma \delta } \frac { d a ^ { \gamma } } { d \lambda } \frac { d a ^ { \delta } } { d \lambda } \right] ^ { 1 / 2 } d \lambda .
$$

Here the $f _ { \sigma }$ ("forceterms") in the integrand are abbreviations for the four expressions

$$
f _ { \sigma } ( \lambda ) = \frac { 1 } { \left[ - g _ { \gamma \delta } \frac { d a ^ { \gamma } } { d \lambda } \frac { d a ^ { \delta } } { d \lambda } \right] ^ { 1 / 2 } } \frac { d } { d \lambda } \frac { g _ { \sigma \nu } \frac { d a ^ { \nu } } { d \lambda } } { \left[ - g _ { \gamma \delta } \frac { d a ^ { \gamma } } { d \lambda } \frac { d a ^ { \delta } } { d \lambda } \right] ^ { 1 / 2 } } - \frac { \frac { 1 } { 2 } \frac { \partial g _ { \mu \nu } } { \partial x ^ { \sigma } } \frac { d a ^ { \mu } } { d \lambda } \frac { d a ^ { \nu } } { d \lambda } } { \left[ - g _ { \gamma \delta } \frac { d a ^ { \gamma } } { d \lambda } \frac { d a ^ { \delta } } { d \lambda } \right] } .
$$

An extremum is achieved,and the first-order change $\delta \tau$ vanishes for every first-order deformation $\delta a ^ { \sigma } ( \lambda )$ from an optimal path $x ^ { \sigma } = a ^ { \sigma } ( \lambda )$ , when the four quantities $f _ { \sigma }$ that multiply the $\delta a ^ { \sigma }$ all vanish. Thus one arrives at the four conditions

$$
f _ { \sigma } ( \lambda ) = 0
$$

for the determination of an extremal world line. (An alternative viewpoint on the extremization is spelled out in Figure 13.3.)

Suffcent these four equations are, but independent they are not, by reason of a “bead argument" (automatic vanishing of $\delta \tau$ for any set of changes that merely slide points, like beads, along an existing world line). The operation of mere “sliding of beads” implies the trivial change

$$
\delta a ^ { \sigma } ( \lambda ) = h ( \lambda ) \frac { d a ^ { \sigma } } { d \lambda } ,
$$

where $h ( \lambda )$ is an arbitrary function of position along the world line ("more sliding here than there"). Already knowing that this operation cannot change $\boldsymbol { \tau }$ oneis guaranteed that the integrand in (l3.30) must vanish when one inserts (13.33) for $\delta a ^ { \sigma }$ ； and must vanish, moreover, whatever choice is made for the arbitrary “magnitude of slide” factor $h ( \lambda )$ .This requirement implies and demands that the scalar product $f _ { \sigma } d a ^ { \sigma } / d \lambda$ must automatically vanish;or, otherwise stated,

$$
f _ { \sigma } \frac { d a ^ { \sigma } } { d \tau } = 0 .
$$

The argument applies,and this equation holds, whether one is or is not dealing with an optimal world line. An equation of this type, valid whether or not the world line is an allowable track for a free test particle (track of extremal lapse of proper

time),is known as an identity.Equation (13.34),an important identity in the realm of spacetime geodesics,is an appropriate forerunner for the Bianchi identities of Chapter 15: the most important identities in the realm of spacetime curvature.

The freedom that exists to “slide $\lambda$ -values along the world line”can be exploited to replace the arbitrary parameter $\lambda$ by the physically more interesting parameter of proper time itself,

$$
d \tau = \Big [ - g _ { \gamma \delta } { \frac { d a ^ { \gamma } } { d \lambda } } { \frac { d a ^ { \delta } } { d \lambda } } \Big ] ^ { 1 / 2 } d \lambda .
$$

.'yu.c   
Star oscillating back and forth through the plane of a disc galaxy,as an example of a situation where two events $\boldsymbol { \mathcal { Q } }$ and $\boldsymbol { \vartheta }$ can be connected by more than one geodesic. Upper left: The galaxy seen edge-on. showing (dashed line)the path of the star in question. referred to a local frame partaking of and comoving with the general revolution of the nearby“disc stars.” Upper right: The efective potential sensed by the star,according to Newtonian gravitation theory,is like that experienced bya ballwhich rolls down one inclined plane and up another("free fall toward galactic plane”with acceleration $g = \frac { 1 } { 2 }$ in the units used here).The three central frames: Possible and impossble world lines for the star connecting two given events $\boldsymbol { \mathcal { a } }$ (plane of galaxy at $t = 0$ and $\ddot { \ast } \beta$ (plane of galaxy at $t = 2$ ).Right:Throw starup from the galactic plane with enough velocity so that it just gets back to the plane at $t = 2$ Left: Throw it up with half the velocityand it will come back in half the time (very contrary to behavior of a simple harmonic oscillation,but in accord with galaxy's v-shaped potential)，thus being able to make two excursions in the allotted time between $\boldsymbol { \mathcal { a } }$ and :B.Center:A conceivable world line (conceivable with rocket propulsion!) but not a geodesic. Bottom: Comparison of these and any other paths that allow themselves to be approximated in the form

$$
z = a _ { 1 } \sin { ( \pi t / 2 ) } + a _ { 2 } \sin { ( 2 \pi t / 2 ) } .
$$

Here the two adjustable parameters, ${ \pmb a } _ { 1 }$ and $\pmb { a } _ { 2 }$ ，provide the coordinates in a two-dimensional “function space"(approximation to the infinite-dimensional function space required to depict allconceivable world lines connecting $\boldsymbol { \mathcal { a } }$ and $\boldsymbol { \mathfrak { B } }$ ; note comparison in right center frame between one-term Fourier approximation and exact,parabolic law of free fal; similarly in left center frame,where the two curves agree too closely to be shown separate on the diagram). Details: In the Context of general relativity,take an arbitrary world line that connects $\mathcal { Q }$ and $\mathcal { B }$ ,evaluate lapse of proper time,repeat for other world lines,and say that a given world line represents a posible motion ("geodesic") when for it the proper time is an extremum with respect to allnearby world lines.In the Newtonian approximation,the difference between the lapse of proper time and the lapse $( t _ { \mathcal { B } } - t _ { \ell } )$ of coordinate time is all that comes to attention, in the form of the “action integral"(on a “per-unit-mass basis")

$$
\begin{array} { l } { I = \int _ { d } ^ { \circ \beta } [ ( \mathrm { { k i n e t i c } } ) - ( \mathrm { { p o t e n t i a l } } ) ] d t } \\ { = \int [ \frac { 1 } { 2 } ( \frac { d z } { d t } ) ^ { 2 } -  | z | ] d t } \end{array}
$$

(maximum, or other extremum,in the proper time implies minimum,or corresponding other extremum, in the action $\pmb { I }$ ).The integration gives

$$
I = ( \pi ^ { 2 } a _ { 1 } ^ { 2 } / 8 ) - ( 4 | a _ { 1 } | / \pi ) + ( \pi ^ { 2 } a _ { 2 } ^ { 2 } / 2 )
$$

for $\vert a _ { 2 } \vert < \frac { 1 } { 2 } \vert a _ { 1 } \vert$ (one-excursion motions),and for $\vert a _ { 2 } \vert > \frac { 1 } { 2 } \left\{ a _ { 1 } \vert a _ { 2 } \vert \right.$ (two-excursion motions),

$$
I = ( \pi ^ { 2 } a _ { 1 } ^ { 2 } / 8 ) + ( \pi ^ { 2 } a _ { 2 } ^ { 2 } / 2 ) - ( 4 | a _ { 2 } | / \pi ) - ( a _ { 1 } ^ { 2 } / \pi | a _ { 2 } | ) .
$$

The one-excursion motion minimizes the action (maximizes the lapse of proper time). The two-excursion motion extremizes the action but does not minimize it ("saddle point”;“mountain pass”in the topography). Choquard (1955） gives other examples of problems of mechanics where there is more than one extremum.Morse (l934) and Morse and Cairns (i969) give a theorem connecting the number of saddles of various types with the numbers of maxima and minima ("critical-point theorem of the calculus of variations in the large").

![](images/50e40ff7d0429e80e0b2a6bb8ad266c7a47fbd6cb7e0a8761fcce4544221a4cc.jpg)

![](images/88ee75b80872a65b2e521e48121b9301daecf9cc91782e79910bdd5fae26c5d0.jpg)

![](images/d94fd8270489ff9aabc8853a64475d3c7913651d23e104bc2aaf92fbc90a6361.jpg)  
Figure 13.3. Extremizing lapse of proper time by suitable choice of world line.Left: Spacetime；and world line $F$ that extremizes the lapse of proper time $\boldsymbol { \tau }$ from $\boldsymbol { \mathcal { Q } }$ to $\boldsymbol { \mathcal { B } }$ compared to other world lines.The specific world lines depicted in the diagram happen to be distinguished from fiducial world line $G$ by two“Fourier amplitudes" $a _ { 1 }$ and ${ a } _ { 2 }$

$$
\delta a ^ { \mu } ( \lambda ) = a _ { 1 } \sin ( \pi \lambda ) + a _ { 2 } \sin ( 2 \pi \lambda ) , \ldots \ .
$$

where the arbitrary scaling of $\lambda$ ,and its zero,are so adjusted that $\lambda ( { \mathcal { Q } } ) = 0 , \lambda ( { \mathcal { B } } ) = 1 .$

Right:“Path space.”The coordinates in this space are the Fourier amplitudes $\pmb { a } _ { 1 }$ and $\alpha _ { 2 }$ .Only these two amplitudes (two dimensions") are shown out of what in principle are infinitely many amplitudes ("infinite-dimensional path space") required to represent the general timelike world line connecting $\boldsymbol { \mathscr { q } }$ and B.Any given contour curve runs through allthose points (in path space)for which the corresponding world lines (in spacetime) rack up the indicated lapse of proper time $\pmb { \tau }$ Foregoing description is classical: according to quantum mechanics,all the timelike world lines connecting $\boldsymbol { \mathcal { Q } }$ and $\mathcal { B }$ occur with the same probability amplitude(principle of democracy of histories") with theonly diference from one to another being the phase of this complex probability amplitude exp $( - i m \tau / \hbar )$ $m =$ mass of particle, $\hbar =$ quan tum of angular momentum). In ihe sum over these probability amplitudes, however,destructive interference wipes out the contributions from all those histories which differ too much from the optimal or classical history ("Fresnel wave zone";“Feynman's principle of sum over histories”;see Feynman and Hibbs, 1965).Capitalizing on this wave-mechanical background to show how the machinery of the physical world works,Box 25.3 spells out the Hamilton-Jacobi method ("short-wavelength limit of quantum mechanics"） for determining geodesics,a method considerably more convenient for most applications than the usuai “second-order differential equations for geodesics” (equation l0.27).

Focus on a specific world line, $x ^ { \mu } = a ^ { \mu } ( \lambda )$ ，with all deformations of it gone from view; one may replace $a ^ { \mu } ( \lambda )$ by $x ^ { \mu } ( \lambda )$ everywhere. Then the differential equations (13.32) for an extremal world line reduce to

$$
g _ { \sigma \nu } { \frac { d ^ { 2 } x ^ { \nu } } { d \tau ^ { 2 } } } + { \frac { 1 } { 2 } } \biggl ( { \frac { \partial g _ { \sigma \nu } } { \partial x ^ { \mu } } } + { \frac { \partial g _ { \sigma \mu } } { \partial x ^ { \nu } } } - { \frac { \partial g _ { \mu \nu } } { \partial x ^ { \sigma } } } \biggr ) { \frac { d x ^ { \mu } } { d \tau } } { \frac { d x ^ { \nu } } { d \tau } } = 0 .
$$

As an aside, note that the identity (l3.34) now follows by one differentiation (with respect to $\pmb { \tau }$ ）of the equation

$$
g _ { \sigma \nu } { \frac { d x ^ { \sigma } } { d \tau } } { \frac { d x ^ { \nu } } { d \tau } } + 1 = 0 .
$$

Thus the identity is to be interpreted as saying that 4-velocity and 4-acceleration are orthogonal for any world line, extremal or not. Now return to (l3.36), raise an index with $g ^ { \beta \sigma }$ ,and thereby bring the equation for a straight line of local Lorentz geometry into the form

$$
\frac { d ^ { 2 } x ^ { \beta } } { d \tau ^ { 2 } } + g ^ { \beta \sigma } \frac { 1 } { 2 } \bigg ( \frac { \partial g _ { \sigma \nu } } { \partial x ^ { \mu } } + \frac { \partial g _ { \sigma \mu } } { \partial x ^ { \nu } } - \frac { \partial g _ { \mu \nu } } { \partial x ^ { \sigma } } \bigg ) \frac { d x ^ { \mu } } { d \tau } \frac { d x ^ { \nu } } { d \tau } = 0 .
$$

Compare with the standard form of the equation for a geodesic in “premetric geometry,”

$$
\frac { d ^ { 2 } x ^ { \beta } } { d \lambda ^ { 2 } } + { \cal { T } } ^ { \beta } { } _ { \mu \nu } \frac { d x ^ { \mu } } { d \lambda } \frac { d x ^ { \nu } } { d \lambda } = 0 .
$$

Conclude that the geodesics of the premetric geometry will agree with the straight lines of the local Lorentz geometry if and only if two conditions are satisfied: (l) the 40 connection coefficients $T ^ { \beta } { } _ { \mu \nu }$ that define geodesics, covariant derivatives, and parallel transport must be given in terms of the 10 metric coefficients $g _ { \mu \nu }$ ("Einstein gravitation potentials") by the equations (13.22) and (13.23) previously derived; and (2) the geodesic parameter $\lambda$ must agree with the proper time $\pmb { \tau }$ up to an arbitrary normalization of zero point and an arbitrary but constant scale factor； thus

$$
\lambda = a \tau + b .
$$

(Nothing in the formalism has any resemblance whatsoever to the universal time t of Newton“flowing everywhere uniformly";rather, there is a separate proper time $\pmb { \tau }$ for each geodesic). See Box 13.3 for another variational principle, which gives in one step both the extremal world line and the right parametrization on that line.

With this step,one has completed the transfer of the ideas of curved-space geometry from a foundation based on geodesics to a foundation based on metric. The resulting geometry always and everywhere anchors itself to the principle of"local Lorentz character,”as the geometry of Newton-Cartan never did and never could.

# Exercise 13.5. ONCE TIMELIKE，ALWAYS TIMELIKE

# EXERCISES

Show that a geodesic of spacetime which is timelike at one event is everywhere timelike. Similarly,show that a geodesic initially spacelike is everywhere spacelike,and a geodesic initially null is everywhere null.[Hint:This is the easiest exercise in the book!]

(coniinued on page 324)

# Box 13.2 "GEODESIC" VERSUS "EXTREMAL WORLD LINE"

Once the connection coefficients $T ^ { \alpha } { } _ { \mu \nu }$ have been expressed in terms of Einstein's gravitational potentials $g _ { \mu \nu }$ by the equations (l3.22) and (13.23), as they are now and hereafter will be in this book ("Riemannian or metric geometry"), it is permissible and appropriate to subsume under the one word“geodesic” two previously distinct ideas:(l) a parametrized world line that satisfies the geodesic equation

$$
\frac { d ^ { 2 } x ^ { \alpha } } { d \lambda ^ { 2 } } + { \cal { T } } ^ { \alpha } { } _ { \mu \nu } \frac { d x ^ { \mu } } { d \lambda } \frac { d x ^ { \nu } } { d \lambda } = 0 ;
$$

and (2)a world line that extremizes the proper time (or, if spacelike,a curve that extremizes the proper distance) between two events $\boldsymbol { \mathcal { Q } }$ and $\mathcal { B }$ .The one possible source of confusion is this, that (l)

presupposes a properly parametrized curve (as was essential, for example, in the Schild's ladder con-struction employed for parallel transport in Chapter 10),whereas (2) cares only about the course of the world line through spacetime, being indifferent to what parametrization is used or whether any parametrization at all is introduced. This is not to deny the possibility of “marking in afterward’ along the extremal curve the most natural and easily evaluated of all parameters, the proper time itself, whereupon the extremal curve of (2) satisfies the geodesic equation of (l).Ambiguity is avoided by insisting on proper parametrization: henceforth the word “curve” means a parametrized curve, the word“geodesic” means a properly parametrized geodesic.

# Box 13.3 "DYNAMIC" VARIATIONAL PRINCIPLE FOR GEODESICS

If the principle of extremal length

$$
\tau = \int _ { d } ^ { \infty } { \biggl [ } - g _ { \mu \nu } { \frac { d x ^ { \mu } } { d \lambda } } { \frac { d x ^ { \nu } } { d \lambda } } { \biggr ] } ^ { 1 / 2 } d \lambda = \mathrm { e x t r e m u m }
$$

is indifferent to choice of parametrization $[ ^ { 6 6 } d \lambda ^ { 3 }$ canceling out in (l)] and if the geodesic equation finds the proper parametrization a matter of concern, it is appropriate to search for another extremal principle that yields in one package both the right curve and the right parameter. By analogy with elementary mechanics, one expects that an equation of motion [the geodesic equation

$$
d ^ { 2 } x ^ { \mu } / d \lambda ^ { 2 } + { \Gamma ^ { \mu } } _ { \alpha \beta } ( d x ^ { \alpha } / d \lambda ) ( d x ^ { \beta } / d \lambda ) = 0 ]
$$

whose leading term has the form $\mathbf { \cdots } \mathbf { \mathit { \hat { x } } } ^ { \mathbf { \prime } \mathbf { \prime } }$ can be derived from a Lagrangian with leading term $\mathbf { \phi } ^ { 6 6 1 } \dot { x } ^ { 2 } \mathbf { \bar { \phi } } ^ { , 9 }$ ("kinetic energy"；“dynamic” term). The simplest coordinate invariant generalization of ${ \scriptstyle { \frac { 1 } { 2 } } } { \dot { x } } ^ { 2 }$ is

$$
\frac { 1 } { 2 } g _ { \mu \nu } ( d x ^ { \mu } / d \lambda ) ( d x ^ { \nu } / d \lambda ) .
$$

Thus one is led to try, in place of the“geometric” principle of extremal length, a new“dynamic” extremal principle:

$$
{ \begin{array} { r l } & { I = { \cfrac { 1 } { 2 } } \int _ { a } ^ { \mathfrak { B } } g _ { \mu \nu } { \frac { d x ^ { \mu } } { d \lambda } } { \frac { d x ^ { \nu } } { d \lambda } } d \lambda } \\ & { \quad = \int _ { a } ^ { \mathfrak { B } } L \left( x ^ { \sigma } , { \cfrac { d x ^ { \sigma } } { d \lambda } } \right) d \lambda = { \mathrm { e x t r e m u m } } } \end{array} }
$$

(replacement of square root in previous variational principle by first power). The condition for an extremum, here as before [equations (13.30)to (13.32)] is annulment of the so-called Euler-Lagrange “functional derivative”

$$
\begin{array} { r l } & { 0 = \frac { \delta I } { \delta x ^ { \sigma } } \equiv \left( \begin{array} { l } { \mathrm { c o e f f i c i e n t ~ o f ~ } \delta x ^ { \sigma } \mathrm { ~ i n } } \\ { \mathrm { t h e ~ i n t e g r a n d ~ o f ~ } \delta I } \end{array} \right) } \\ & { \quad = \frac { \partial L } { \partial x ^ { \sigma } } - \frac { d } { d \lambda } \frac { \partial L } { \partial \left( \frac { d x ^ { \sigma } } { d \lambda } \right) } ; } \end{array}
$$

or, written out in full detail,

$$
g _ { \sigma \nu } \frac { d ^ { 2 } x ^ { \nu } } { d \Lambda ^ { 2 } } + \frac { 1 } { 2 } \left( \frac { \partial g _ { \sigma \nu } } { \partial x ^ { \mu } } + \frac { \partial g _ { \sigma \mu } } { \partial x ^ { \nu } } - \frac { \partial g _ { \mu \nu } } { \partial x ^ { \sigma } } \right) \frac { d x ^ { \mu } } { d \Lambda } \frac { d x ^ { \nu } } { d \Lambda } = 0 ;
$$

or, after multiplication by the reciprocal metric,

$$
\frac { d ^ { 2 } x ^ { \alpha } } { d \lambda ^ { 2 } } + g ^ { \alpha \sigma } \frac { 1 } { 2 } \bigg ( \frac { \partial g _ { \sigma \nu } } { \partial x ^ { \mu } } + \frac { \partial g _ { \sigma \mu } } { \partial x ^ { \nu } } - \frac { \partial g _ { \mu \nu } } { \partial x ^ { \sigma } } \bigg ) \frac { d x ^ { \mu } } { d \lambda } \frac { d x ^ { \nu } } { d \lambda } = 0 ;
$$

which translates into the geodesic equation

$$
{ \frac { d ^ { 2 } x ^ { \alpha } } { d \lambda ^ { 2 } } } + { \Gamma ^ { \alpha } } _ { \mu \nu } { \frac { d x ^ { \mu } } { d \lambda } } { \frac { d x ^ { \nu } } { d \lambda } } = 0 .
$$

Thus,the new “dynamic” expression (2) is indeed extremal for geodesic curvesand, by contrast with proper length, (l), it is extremal when and only when the geodesic is affnely parametrized.[Its “Euler-Lagrange equations”(6)remain satisfied only under parameter changes $\lambda _ { \mathrm { n e w } } = a \lambda _ { \mathrm { o l d } } + b$ ，which keep the parameter affine; by contrast, the Euler-Lagrange equations (l3.31) and (13.32) for the “principle of extremal length”(l) remain satisfied for any change of parameter whatsoever.]


<!-- chunk 0006: pages 351-420 -->
# Exercise 13.6. SPACELIKE GEODESICS HAVE EXTREMAL LENGTH

Show that any spacelike curve linking two events $\pmb { \mathcal { Q } }$ and $\mathcal { B }$ is a geodesic if and only if it extremizes the proper length

$$
s = \int _ { d } ^ { \cdot \beta } ( g _ { \mu \nu } d x ^ { \mu } d x ^ { \nu } ) ^ { 1 / 2 } . . .
$$

[Hint: This is almost as easy as exercise 13.5 if one has already proved the analogous theorem for timelike geodesics.]

# ExerciSe 13.7. METRIC TENSOR MEASURED BY LIGHT SIGNALS AND FREE PARTICLES [Kuchar]

(a) Instead of parametrizing a timelike geodesic by the proper time $\pmb { \tau }$ ,parametrize it by an arbitrary parameter $\mu$ ，

$$
{ \pmb \tau } = { \pmb F } ( { \pmb \mu } ) .
$$

Write the geodesic equation in the $\pmb { \mu }$ parametrization.

(b) Use now the coordinate time $t$ as a parameter. Throw out a cloud of free particles with different “velocities” $v ^ { \mathrm { i } } = d x ^ { \mathrm { i } } / d t$ and observe their“accelerations” $a ^ { \mathrm { i } } = \bar { d } ^ { 2 } x ^ { \mathrm { i } } / d t ^ { 2 }$ Discuss what combinations of the components of the affine connection $T ^ { \iota } { } _ { \kappa \lambda }$ one can measure in this way. (Assume that no standard clocks measuring $\tau$ are available!)

(c) Show that one can measure the conformal metric $\widetilde { g } _ { \mu \epsilon }$ ,i.e., the ratios of the components of the metric tensor $g _ { \kappa }$ to a given component (say, $g _ { 0 0 } \mathrm { , }$

$$
\qquad \overline { { { g } } } _ { \iota \kappa } = { \cal A } g _ { \iota \kappa } , \qquad { \cal A } \equiv ( - g _ { 0 0 } ) ^ { - 1 } ,
$$

using only the light signals moving along the null geodesics $g _ { u \kappa } d x ^ { \iota } d x ^ { \kappa } = 0$

(d) Combine now the results of (b) and (c). Assume that $T ^ { \iota } { } _ { \kappa \lambda }$ is generated by the metric tensor by (13.22),(13.23),in the coordinate frame $x ^ { t }$ . Show that one can determine $\pmb { A }$ everywhere, if one prescribes it at one event (equivalent to fixing.the unit of time).

# S13.5. METRIC-INDUCED PROPERTIES OF RIEMANN

Symmetries of Riemann in absence of metric

In Newtonian spacetime,in the real, physical spacetime of Einstein-indeed,in any manifold with covariant derivative-the Riemann curvature tensor has these symmetries (exercise 11.6):

$$
\begin{array} { r l } { R ^ { \alpha } { } _ { \beta \gamma \delta } \equiv R ^ { \alpha } { } _ { \beta [ \gamma \delta ] } \quad } & { \mathrm { ( a n t i s y m m e t r y ~ o n ~ l a s t ~ t w o ~ i n d i c e s ) } } \\ { R ^ { \alpha } { } _ { [ \beta \gamma \delta ] } \equiv 0 \quad } & { \mathrm { ( v a n i s h i n g ~ o f ~ c o m p l e t e l y ~ a n t i s y m m e t r i c ~ p a r t ) . } } \end{array}
$$

In addition, it satisfies a diferential identity (exercise 11.10):

$$
{ R ^ { \alpha } } _ { \beta [ \gamma \delta ; \epsilon ] } \equiv 0 \qquad \mathrm { ( " B i a n c h i ~ i d e n t i t y " ) }
$$

New symmetries imposed by metric

(see Chapter 15 for geometric significance).

When metric is brought onto the scene, whether in Einstein spacetime or elsewhere, it impresses on Riemann the additional symmetry (exercise 13.8)

$$
R _ { \alpha \beta \gamma \delta } \equiv R _ { [ \alpha \beta ] \gamma \delta } { \mathrm { ~ ( a n t i s y m m e t r y ~ o n ~ f i r s t ~ t i w o ~ i n d i c e s ) } } .
$$

This,together with (13.40) and (13.41), forms a complete set of symmetries for Riemann; other symmetries that follow from these (exercise 13.10) are

$$
R _ { \alpha \beta \gamma \delta } = R _ { \gamma \delta \alpha \beta } ~ ( \mathrm { s y m m e t r y ~ u n d e r ~ p a i r ~ e x c h a n g e } ) ,
$$

and

$$
R _ { [ \alpha \beta \gamma \delta ] } = 0 \qquad \mathrm { ( v a n i s h i n g ~ o f ~ c o m p l e t e l y ~ a n t i s y m m e t r i c ~ p a r t ) . }
$$

These symmetries reduce the number of independent components of Riemann from $4 \times 4 \times 4 \times 4 = 2 5 6$ to 20 (exercise 13.9).

With metric present, one can construct a variety of new curvature tensors from Riemann. Some that will play important roles later are as follows.

(1） The double dual of Riemann, ${ \pmb {6 } } \equiv { ^ \star }$ Riemann\* (analog of Maxwell三 \*Faraday),which has components

$$
{ { \cal { G } } ^ { \alpha \beta } } _ { \gamma \delta } \equiv \frac { 1 } { 2 } \epsilon ^ { \alpha \beta \mu \nu } R _ { \mu \nu } ^ { \rho \sigma } \frac { 1 } { 2 } \epsilon _ { \rho \sigma \gamma \delta } = - \frac { 1 } { 4 } \delta _ { \rho \sigma \gamma \delta } ^ { \alpha \beta \mu \nu } R _ { \mu \nu } ^ { \rho \sigma }
$$

(exercise 13.11).

(2) The Einstein curvature tensor, which is symmetric (exercise 13.11)

Einstein tensor

$$
{ G ^ { \beta } } _ { \delta } \equiv { G ^ { \mu \beta } } _ { \mu \delta } ; G _ { \beta \delta } = G _ { \delta \beta } .
$$

(3) The Ricci curvature tensor,which is symmetric,and the curvature scalar

Ricci tensor

$$
R ^ { \beta } { } _ { \delta } \equiv R ^ { \mu \beta } { } _ { \mu \delta } , \qquad R _ { \beta \delta } = R _ { \delta \beta } ; \qquad R \equiv R ^ { \beta } { } _ { \beta } ;
$$

Curvature scalar

which are related to the Einstein tensor by (exercise 13.12)

$$
{ R ^ { \beta } } _ { \delta } = { G ^ { \beta } } _ { \delta } + { \frac { 1 } { 2 } } R { \delta ^ { \beta } } _ { \delta } .
$$

(4） The Weyl conformal tensor (exercise 13.13)

Weyl conformal tensor

$$
C ^ { \alpha \beta } { } _ { \gamma \delta } = R ^ { \alpha \beta } { } _ { \gamma \delta } - 2 \delta ^ { [ \alpha } { } _ { [ \gamma } R ^ { \beta ] } { } _ { \delta ] } + \frac { 1 } { 3 } \delta ^ { [ \alpha } { } _ { [ \gamma } \delta ^ { \beta ] } { } _ { \delta ] } R .
$$

The Bianchi identity (l3.42） takes a particularly simple form when rewritten in terms of the double dual $\pmb { \ 6 }$ ：

Bianchi identities

$$
{ { \cal { G } } _ { \alpha \beta } } _ { ; \delta } ^ { \delta } \equiv 0 \qquad ( \mathrm { { } ^ { * * } B i a n c h i \ i d e n t i t y ^ { * * } ) }
$$

(exercise l3.11); and it has the obvious consequence

$$
{ G _ { \alpha } } ^ { \beta } { } _ { ; \beta } \equiv 0 ( \mathrm { \small { ~ \left( ' { c o n t r a c t e d } ~ B i a n c h i ~ i d e n t i t y ^ { * } \right) } } .
$$
