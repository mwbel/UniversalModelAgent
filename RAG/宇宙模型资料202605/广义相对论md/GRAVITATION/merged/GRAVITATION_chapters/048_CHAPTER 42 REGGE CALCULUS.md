# CHAPTER 42 REGGE CALCULUS

# \$42.1. WHY THE REGGE CALCULUS?

This chapter is entirely Track 2. As preparation for it, Chapter 21 (variational principle and initial-value formalism) is needed. It is not needed as preparation for any later chapter, though it will be helpful in Chapter 43 (dynamics of geometry).

Gravitation theory is entering an era when situations of greater and greater com-plexity must be analyzed. Before about l965 the problems of central interest could mostly be handled by idealizations of special symmetry or special simplicity or both. The Schwarzschild geometry and its generalizations, the Friedmann cosmology and its generalizations, the joining together of the Schwarzschild geometry and the Friedmann geometry to describe the collapse of a bounded collection of matter, the vibrations of relativistic stars, weak gravitational waves propagating in an otherwise flat space: all these problems and others were solved by elementary means.

The need for Regge calculus as a computational tool

But today one is pressed to understand situations devoid of symmetry and not amenable to perturbation theory: How do two black holes alter in shape, and how much gravitational radiation do they emit when they collide and coalesce? What are the structures and properties of the singularities at the endpoint of gravitational collapse，predicted by the·theorems of Penrose, Hawking,and Geroch? Can a Universe that begins completely chaotic smooth itself out quickly by processes such as inhomogeneous mixmaster oscillations?

To solve such problems, one needs new kinds of mathematical tools-and in response to this need, new tools are being developed. The “global methods” of Chapter 34 provide one set of tools. The Regge Calculus provides another [Regge (1961); see also pp. 467-500 of Wheeler (1964a)].

# $\ S 4 2 . 2$ . REGGE CALCULUS IN BRIEF

Approximation of smooth geometries by skeleton structures

Consider the geodesic dome that covers a great auditorium, made of a multitude of flat triangles joined edge to edge and vertex to vertex. Similarly envisage spacetime,in the Regge calculus,as made of flat-space “simplexes” (four-dimensional item in this progression: two dimensions, triangle; three dimensions, tetrahedron; four dimensions, simplex) joined face to face, edge to edge, and vertex to vertex. To specify the lengths of the edges is to give the engineer all he needs in order to know the shape of the roof, and the scientist all he needs in order to know the geometry of the spacetime under consideration. A smooth auditorium roof can be approximated arbitrarily closely by a geodesic dome constructed of suffciently small triangles. A smooth spacetime manifold can be approximated arbitrarily closely by a locked-together assembly of sufficiently small simplexes.Thus the Regge calculus, reaching beyond ordinary algebraic expressons for the metric, provides a way to analyze physical situations deprived, as so many situations are, of spherical symmetry, and systems even altogether lacking in symmetry.

If the designer can give the roof any shape he pleases, he has more freedom than the analyst who is charting out the geometry of spacetime. Given the geometry of spacetime up to some spacelike slice that, for want of a better name, one may call “now,”one has no freedom at allin the geometry from that instant on. Einstein's geometrodynamic law is fully deterministic. Translated into the language of the Regge calculus, it provides a means to calculate the edge lengths of new simplexes from the dimensions of the simplexes that have gone before. Though the geometry is deterministically specified, how it will be approximated is not. The original spacelike hypersurface ("now") is approximated as a collection of tetrahedrons joined together face to face; but how many tetrahedrons there will be and where their vertices will be placed is the option of the analyst. He can endow the skeleton more densely with bones in a region of high curvature than in a region of low curvature to get the most “accuracy profit” from a specified number of points. Some of this freedom of choice for the lengths of the bones remains as one applies the geometrodynamic law in the form given by Regge (l96l) to calculate the future from the past. This freedom would be disastrous to any computer program that one tried to write, unless the programmer removed all indefiniteness by adding supplementary conditions of his own choice, either tailored to give good “accuracy profit,” or otherwise fixed.

Having determined the lengths of all the bones in the portion of skeletonized spacetime of interest, one can examine any chosen local cluster of bones in and by themselves.In this way one can find out all there is to be learned about the geometry in that region. Of course, the accuracy of one's findings will depend on the fineness with which the skeletonization has been carried out. But in principle that is no limit to the fineness or therefore to the accuracy,so long as one is working in the context of classical physics. Thus one ends up with a catalog of allthe bones, showing the lengths of each. Then one can examine the geometry of whatever spacelike surface one pleases,and look into many other questions besides. For this purpose one has only to pick out the relevant bones and see how they fit together.

# \$42.3. SIMPLEXES AND DEFICIT ANGLES

Role of Einstein field equation in fixing the skeleton structure

Figure 42.l recalls how a smoothly curved surface can be approximated by flat triangles. All the curvature is concentrated at the vertices. No curvature resides at

![](images/7470b8df0df099e5279e42cff460d85586647f4ed1fb31ff0eda65f2c5e2b51f.jpg)  
Figure 42.1. A2-geometry with continuously varying curvaturecan be approximated arbitrarilyclosely by apolyhedron built of triangles,provided only that the number of triangles is made suffciently great and the size of each suffciently small.The geometry in each triangle is Euclidean.The curvature of the surface shows up in the amount of deficit angle at each vertex (portion ABCD of polyhedron laid out above on a flat surface).

Deficit angle as a skeletonized measure of curvature:

(1）in two dimensions

the edge between one triangle and the next, despite one's first impression.A vector carried by parallel transport from $\pmb { A }$ through $\pmb { B }$ and $C$ to $D$ ,and then carried back by another route through $C$ and $\pmb { B }$ to $\pmb { A }$ returns to its starting point unchanged in direction,as one sees most easily by laying out this complex of triangles on a flat surface. Only if the route is allowed to encircle the vertex common to $A , B , C ,$ and $D$ does the vector experience a net rotation. The magnitude of the rotation is equal to the indicated deficit angle, δ,at the vertex. The sum of the deficit angles over all the vertices has the same value, ${ 4 \pi }$ ,as does the half-integral of the continuously distributed scalar curvature ${ \bf \Omega } ^ { ( 2 ) } R = 2 / a ^ { 2 }$ for a sphere of radius $a ^ { \dagger }$ ）taken over the entirety of the original smooth figure,

$$
\sum _ { \mathrm { { s k e l e t o n } } \atop \mathrm { { g e o m e t r y } } } \delta _ { i } = \frac { 1 } { 2 } \int _ { \stackrel { \mathrm { a c t u a l s m o o t h } } { \mathrm { g e o m e t r y } } } { } ^ { ( 2 ) } R d ( \mathrm { s u r f a c e } ) = 4 \pi .
$$

(2) in n (or four) dimensions

Generalizing from the example of a 2-geometry， Regge calculus approximates a smoothly curved $\pmb { n }$ -dimensional Riemannian manifold as a collection of $\pmb { n }$ -dimensional blocks, each free of any curvature at all, joiied by $( n - 2 )$ -dimensional regions in which all the curvature is concentrated (Box 42.1). For the four-dimensional spacetime of general relativity, the “hinge”at which the curvature is concentrated has the shape of a triangle, as indicated schematically in the bottom row of Figure 42.2.In the example illustrated there, ten tetrahedrons have that triangle in common. Between one of these tetrahedrons and the next fits a four-dimensional simplex. Every feature of this simplex is determined by the lengths of its ten edges. One of the features is the angle $\pmb { \alpha }$ between one of the indicated tetrahedrons or“faces” of the simplex and the next. Thus $\pmb { \alpha }$ represents the angle subtended by this simplex

# Box 42.1 THE HINGES WHERE THE $\cdot$ CURVATURE IS CONCENTRATED INTHE"ANGLE OF RATTLE" BETWEEN BUILDING BLOCKS IN A SKELETON MANIFOLD

<table><tr><td>Dimensionality of manifold</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Elementary flat-space</td><td></td><td></td><td></td></tr><tr><td>building block:</td><td>triangle</td><td>tetrahedron</td><td>simplex</td></tr><tr><td>Edge lengths to define it:</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Hinge where cycle of such blocks meet with a deficit</td><td></td><td></td><td></td></tr><tr><td>angle or “angle of rattle”S:</td><td>vertex</td><td>edge</td><td>triangle</td></tr><tr><td>Dimensionality of hinge:</td><td>0</td><td>1</td><td>2</td></tr><tr><td>“Content&quot; of such a hinge:</td><td>1</td><td>length I</td><td>area A</td></tr><tr><td>Contribution from all hinges within a given small region</td><td></td><td></td><td></td></tr><tr><td>to curvature of manifold:</td><td>8 region</td><td>region</td><td>MA region</td></tr><tr><td>Continuum limit of this quantity</td><td></td><td></td><td></td></tr><tr><td>expressed as an integral over the same small region:</td><td></td><td></td><td></td></tr><tr><td></td><td>R(g）/2 d8x</td><td>R(g）1/2 d8x</td><td>SR(-g）12 d4x</td></tr></table>

at the hinge. Summing the angles $\pmb { \alpha }$ for all the simplexes that meet on the given hinge $\mathcal { P Q R }$ , and subtracting from $2 \pi$ ,one gets the deficit angle associated with that hinge.And by then summing the deficit angles in a given small $\pmb { n }$ -volume with appropriate weighting $\left( \operatorname { \mathbf { B } o x } 4 2 . 1 \right)$ , one obtains a number equal to the volume integral of the scalar curvature of the original smooth $\pmb { n }$ geometry. See Box 42.2.

# $\$ 42.4$ ： SKELETON FORM OF FIELD EQUATIONS

Rather than translate Einstein's field equations directly into the language of the skeleton calculus, Regge turns to a standard variational principle from which Ein-stein's law lets itself be derived. It says (see $\ S 8 2 1 . 2$ and 43.3) adjust the 4-geometry throughout an extended region of spacetime, subject to certain specified conditions on the boundary, so that the dimensionless integral (action in units of $\hbar !$ ），

Einstein-Hilbert variational principle reduced to skeleton form

$$
I = ( c ^ { 3 } / 1 6 \pi \hbar G ) \int R ( - g ) ^ { 1 / 2 } d ^ { 4 } x ,
$$

is an extremum.This statement applies when space is free of mater and electromag-

![](images/dd0b4fb5b2d5b43cdef376fe1dd9ae756ce6daf0be683c5045d992e30c090ae4.jpg)  
Figure 42.2. Cycle of building blocks associated with a single hinge.Top row,two dimensions:left,schematic association of vertices $\mathcal { S } , \mathcal { F } , \mathcal { \ P } , \mathcal { F } , \mathcal { Z }$ with “hinge”at the vertex $\mathcal { P }$ ； right, same,but with elementary triangles indicated in full Middlerow,three dimensions: left,schematic;right,perspective representation of the six tetrahedrons that meet on the“hinge” $\vartheta _ { \bullet } ^ { \bullet }$ Bottom row,four dimensions; shown only schematically.The five vertices $\vartheta \vartheta \vartheta \vartheta \vartheta ( \vartheta { \cdot } \vec { \bf { z } } )$ belong to one simplex,a four-dimensional region throughout the interior of which space is flat.The five vertices $\mathcal { S } \tilde { \mathcal { Q } } \tilde { \mathcal { Q } } \tilde { \mathcal { Q } } \tilde { \mathcal { Q } } \tilde { \mathcal { Q } }$ belong to the next simplex; and so on around the cycle of simplexes.The two simplexes just named interface at the tetrahedron $\mathcal { S } \mathcal { Q } \mathcal { Q } \mathcal { Q } \mathcal { Q } \mathcal { Q } \mathcal { ) }$ ,insidewhich the geometry is also flat. Between that tetrahedron and the next, $\mathcal { P Q H } \mathcal { E }$ ,there is a certain hyperdihedral angle $\pmb { \alpha }$ subtended at the“hinge” $s \mathcal { P } \overset { \mathcal { Q } } { \underset { \mathcal { N } } { \sim } } \mathfrak { H }$ .The value of this angle is completely fixed by the ten edge lengths of the intervening simplex $\mathcal { P Q } \mathcal { Q } \mathcal { R } \mathcal { Q } \mathcal { E }$ .This dihedral angle,plus the corresponding dihedral angles subtended at the hinge $\mathcal { S } \vec { \mathcal { Z } } \vec { \mathcal { T } }$ by the other simplexes of the cycle,do not in general add up to $2 \pi$ The deficit,the “angle of ratte” or deficit angle δ,gives the amount of curvature concentrated at the hinge $\vartheta { \mathfrak { L } } { \mathfrak { H } }$ .There is no actual ratte or looseness of fit,unless one tries to imbed the cycle into an over-all flat four-dimensional space (analog of “stamping on” the collection of triangles,and seeing them open out by the amount of the deficit angle,as indicated in inset in Figure 42.1).

netic fields; a simplification that willbe made in the subsequent discussion to keep it from becoming too extended. When in addition al lengths are expressed in units of the Planck length

$$
L ^ { * } = ( \hbar G / c ^ { 3 } ) ^ { 1 / 2 } = 1 . 6 \times 1 0 ^ { - 3 3 } \mathrm { c m } ,
$$

and the curvature integral is approximated by its expresson in terms of deficit angles, Regge shows that the statement $\delta I = 0$ (condition for an extremum!) becomes

$$
( 1 / 8 \pi ) \ : \delta \sum _ { \mathrm { { \scriptsize ~ h i n g e s } ~ } } ^ { \cal H } A _ { h } \ : \delta _ { h } = 0 .
$$

# Box 42.2 FLOW DIAGRAMS FOR REGGE CALCULUS

A skeleton 4-geometry is completely determined by al its edge lengths. From the edge lengths one gets the integrated curvature by pursuing, for each hinge in the 4-geometry, the following flow diagram:

hinge cycle of blocks swinging on this hinge one of these blocks ?   
the two tetrahedral “faces” that set this block off from   
the blocks before and after it in the cycle of blocks angle $\pmb { \alpha }$ between these two faces fixed by the block's $n ( n - 1 ) / 2$ edge lengths Y deficit angle at the given hinge is 8 =27- bcks onthat hinge + contribution to integrated curvature $( \mathbf { B } \circ \mathbf { x } \ 4 2 . 1 )$ is 8 times area of hinge

One finds it natural to apply this analysis in either of two ways.First, one can probe a given 4-geometry (given set of edge lengths!) in the sense

![](images/364feda0124665e5cae8604401d178d7ae3cfff54a0bf1fda49681b27737b22e.jpg)

Second-and this is the rationale of Regge calculus-one can use the skeleton calculus to deduce a previously unknown 4-geometry from Einstein's geometrodynamic law, proceeding in the direction

![](images/8b452671c9e54e5246a71302c831ee573b50d796f4a78602a06ef730b778b1db.jpg)  
Box 42.2 (continued)

In the changes contemplated in this variational principle, certain edge lengths are thought of as being fixed. They have to do with the conditions specified at the boundaries of the region of spacetime under study. It is not necessary here to enter into the precise formulation of these boundary conditions, fortunately, since some questions of principle still remain to be clarified about the precise formulation of boundary conditions in general relativity (see $\ S 2 1 . 1 2 )$ .Rather,what is important is the effect of changes in the lengths of the edges of the blocks in the interior of the region being analyzed, as they augment or decrease the deficit angles at the various hinges. In his basic paper on the subject, Regge (l961) notes that the typical deficit angle $\delta _ { h }$ depends in a complicated trigonometric way on the values of numerous edge lengths $\ell _ { p } .$ However, he proves (Appendix of his paper) that “quite remarkably, we can carry out the variation as if the $\delta _ { h }$ were constants,” thus reducing the variational principle to the form

$$
( 1 / 8 \pi ) \sum _ { \stackrel { \mathrm { h i n g e s } } { h = 1 } } ^ { H } \delta _ { h } \delta A _ { h } = 0 .
$$

Here the change in area of the $\pmb { h }$ -th triangle-shaped hinge,according to elementary trigonometry, is

$$
\delta A _ { h } = \frac { 1 } { 2 } \sum _ { p } \updownarrow _ { p } \delta \ell _ { p } \cot { \mu _ { p h } } .
$$

In this equation $\theta _ { p h }$ is the angle opposite to the $\boldsymbol { p }$ -th edge in the triangle. Consequently, Einstein's equations in empty space reduce in skeleton geometry to the form

$$
\begin{array} { r l } { \sum } & { { } \delta _ { h } \mathrm { c o t a n } \theta _ { p h } = 0 , ( p = 1 , 2 , \ldots ) , } \end{array}
$$

Einstein field equation reduced to skeleton form

one equation for each edge length in the interior of the region of spacetime being analyzed.

# £42.5. THE CHOICE OF LATTICE STRUCTURE

Two questions arise in the actual application of Regge calculus, and it is not clear that either has yet received the resolution which is most convenient for practical applications of this skeleton analysis: What kind of lattce to use? How best to capitalize on the freedom that exists in the choice of edge lengths? The first question is discussed in this section, the second in the next section.

（1）avoiding floppiness

It might seem most natural to use a latice made of small nearly rectangular blocks, the departure of each from rectangularity being conditioned by the amount and directionality of the local curvature. However,such building blocks are“floppy." One could give them rigidity by specifying certain angles as well as the edge lengths. But then one would lose the cleanness of Regge's prescription: give edge lengths, and give only edge lengths,and give each edge length freely and independently, in order to define a geometry. In addition one would have to rederive.the Regge equations, including new.equations for the determination of the new angles. Therefore one discards the quasirectangle in favor of the simplex with its $5 \cdot 4 / 2 = 1 0$ edge lengths. This decided, one also concludes that even in flat spacetime the simplexes cannot all have identical edge lengths. Two-dimensional flat space can be filled with identical equilateral triangles,but already at three dimensions it ceases to be possible to fill out the manifold with identical equilateral tetrahedrons. One knows that a given carbon atom in diamond is joined to its nearest neighbors with tetrahedral bonds,but a litle reflection shows that the cell assignable to the given atom is far from having the shape of an equilateral tetrahedron.

The choice of lattice structure:

(2) necessity for unequal edge lengths

Synthesis would appear to be a natural way to put together the building blocks: first make one-dimensional structures; assemble these into two-dimensional structures; these, into three-dimensional ones; and these, into the final four-dimensional structure. The one-dimensional structure is made of points, l,2,3,...,alternating with line segments, 12,23,34,.... To start building a two-dimensional structure, pick up a second one-dimensional structure.It might seem natural to label its points $1 ^ { \prime } , 2 ^ { \prime } , 3 ^ { \prime } , \ldots$ ,etc.However, that labeling would imply a cross-connection between l and 1', between 2 and 2', etc., after the fashion of a ladder. Then the elementary cells would be quasirectangles. They would have the “floppiness” that is to be excluded. Therefore relabel the points of the second one-dimensional structure as $1 { _ { 2 } ^ { 1 \prime } } , 2 { _ { 2 } ^ { 1 \prime } } , 3 { _ { 2 } ^ { 1 \prime } }$ ,etc.The implication is that one cross-connects $2 _ { 2 } ^ { 1 \prime }$ with points 2 and 3 of the original one-dimensional structure, etc. One ends up with something like the

(3) construction of twodimensional structures

girder structure of a bridge,fully rigid in the context of two dimensions, as desired. The same construction, extended, fills out the plane with triangles. One now has a simple, standard two-dimensional structure. One might mistakenly conclude that one is_ready to go ahead to build up a three-dimensional structure: the mistake lies in the tacit assumption that the flat-space topology is necessarily correct.

Let it be the problem, for example,to determine the development in time of a 3-geometry that has the topology of a 3-sphere. This 3-sphere is perhaps strongly deformed from ideality by long-wavelength gravitational waves. A right arrangement of the points is the immediate desideratum. Therefore put aside for the present any consideration of the deformation of the geometry by the waves (alteration of edge lengths from ideality). Ask how to divide a perfect 3-sphere into two-dimensional sheets. Here each sheet is understood to be separated from the next by a certain distance.At this point two alternative approaches suggest themselves that one can call for brevity “blocks”and “spheres.”

(4)3-D structures built from 2-D structures by "method of blocks"

(1) Blocks.Note that a 3-sphere lets itself be decomposed into 5 identical, tetrahedron-like solid blocks (5 vertices; 5 ways to leave out any one of these vertices!) Fix on one of these“tetrahedrons.’ Select one vertex as summit and the face through the other three vertices as base.Give that base the two-dimensional lattice structure already described. Introduce a multitude of additional sheets piled above it as evenly spaced layers reaching to the summit. Each layer has fewer points than the layer before. The decomposition of the 3-geometry inside one “tetrahedron” is thereby accomplished. However, an unresolved question remains; not merely how to join on this layered structure in a regular way to the corresponding structure in the adjacent “tetrahedrons"; but even whether such a regular joinup is at all possible. The same question can be asked about the other two ways to break up the 3-sphere into identical “tetrahedrons” [Coxeter (1948)，esp. Pp.292-293:16 tetrahedrons defined by a total of 8 vertices or 600 tetrahedrons defined by a total of l20 vertices]. One can eliminate the question of joinup of structure in a simple way, but at the price of putting a ceiling on the accuracy attainable: take the stated number of vertices (5 or 8 or 120) as the total number of points that will be employed in the skeletonization of the 3-geometry (no further subdivision required or admitted). Considering the boundedness of the memory capacity of any computer, it is hardly ridiculous to contemplate a limitation to l20 tracer points in exploratory calculations!

(5)3-D structures from 2-D by“method of spheres"

(2) Spheres.An alternative approach to the“atomization” of the 3-sphere begins by introducing on the 3-sphere a North Pole and a South Pole and the hyperspherical angle $x$ $( x = 0$ at the first pole, $x = \pi$ at the second, $x = \pi / 2$ at the equator; see Box 27.2). Let each two-dimensional layer lie on a surface of constant $\dot { x } \dot { ( x ) }$ equal to some integer times some interval $\pmb { 4 } \chi )$ . The structure of this 2-sphere is already to be regarded as skeletonized into elementary triangles ("fully complete Buckminster Fuller geodesic dome"). Therefore the number of “faces” or triangles $F ,$ the number of edge lengths $E _ { \mathrm { { \scriptscriptstyle * } } }$ ,and the number of vertices $V$ must be connected by the relation of Euler:

$$
F - E + V = { \binom { \mathrm { a ~ t o p o l o g y - d e p e n d e n t } } { \mathrm { n u m b e r ~ o r ~ } ^ { \ast \ast } \mathrm { E u l e r ~ c h a r a c t e r } ^ { \prime \ast } } } ) = { \binom { 2 { \mathrm { ~ f o r ~ } } 2 \cdot { \mathrm { s p h e r e } } , } { \mathrm { 0 ~ f o r ~ } } }
$$

It follows from this relation that it is impossible for each vertex to sit at the center of a hexagon (each vertex the point of convergence of 6 triangles). This being the case,one is not astonished that a close inspection of the pattern of a geodesic dome shows several vertices where only 5 triangles meet. It is enough to have 12 such 5-triangle vertices among what are otherwise all 6-triangle vertices in order to meet the requirements of the Euler relation:

$$
{ \begin{array} { r l r } { { 2 } = F - E + V = n / 6 } & { } & { { \mathrm { E u l e r ~ c h a r a c t e r i s t i c } } } \\ { n = 1 2 } \end{array} }
$$

Among all figures with triangular faces, the icosahedron is the one with the smallest number of faces that meets this condition (5-triangle vertices exclusively!)

If each 2-surface has the patern of vertices of a geodesic dome, how is one dome to be joined to the next to make a rigid skeleton 3-geometry? Were the domes imbedded in a fat 3-geometry, rigidity would be no issue. Each dome would already be rigid in and by itself. However, the 3-geometry is not given to be flat. Only by a completely deterministic skeletonization of the space between the two 2-spheres will they be given rigidity in the context of curved space geometry.(1) Not by running a single connector from each vertex in one surface to the corresponding vertex in the next ("floppy structure"!) (2) Not by displacing one surface so each of its vertices comes above, or nearly above, the center of a triangle in the surface “below.” First, the numbers of vertices and triangles ordinarily will not agree. Second, even when they do, it will not give the structure the necessry rigidity to connect the vertex of the surface above to the three vertices of the triangle below. The space between will contain some tetrahedrons, but it will not be throughout decomposed into tetrahedrons. (3)A natural and workable approach to the skeletonization of the 3-geometry is to run a connector from each vertex in the one surface to the corresponding vertex in the next, but to flesh out this connection with additional structure that will give rigidity to the 3-geometry: intervening vertices and connectors as illustrated in Box 42.3.

(6)4-D structures built from 3-D structures

In working up from the skeletonization of a 3-geometry to the skeletonization of a 4-geometry,it is natural to proceed similarly. (l) Use identical patterns of points in the two 3-geometries. (2) Tie corresponding points together by single connectors. (3)Halfway,or approximately half way between the two 3-geometries insert a whole additional pattern of vertices. Each of these supplementary vertices is “dual” to and lies nearly“below” the center of a tetrahedron in the 3-geometry immediately above. (4) Connect each supplementary vertex to the vertices of the tetrahedron immediately above,to the vertices of the tetrahedron immediately below,and to those other supplementary vertices that are its immediate neighbors. (5)In this way get the edge lengths needed to divide the 4-geometry into simplexes,each of rigidly defined dimensions.

# Box 42.3 SYNTHESIS OF HIGHER-DIMENSIONAL SKELETON GEOMETRIES OUT OF LOWER-DIMENSIONAL SKELETON GEOMETRIES

![](images/5a03e26d4597c37018a19ad60d35e948b4918f4ef8d89b230442e4c25f77bf4a.jpg)

(1) One-dimensional structure as alternation of points and line segments. (2） Two-dimensional structure (a)"floppy"(unacceptable)and (b) rigidified (angles of triangles fully determined by edge lengths). When this structure is extended, as at right,the “normal" vertex has six triangles hinging on it.However, at least twelve 5-triangle vertices of the type indicated at $\boldsymbol { \mathcal { q } }$ are to be interpolated if the 2-geometry is to be able to close up into a 2-sphere. (3) Skeleton 3-geometry obtained by filling in between the skeleton 2-geometry... $\square 9 \cdots 5 9 9 0 \ldots 5 9 \ldots$ and the similar structure $\yen 123,456,7$ as follows. (a) Insert direct connectors such as ${ \mathcal { P } } { \mathcal { P } } ^ { \prime }$ between corresponding points in the two 2-geometries. (b) Insert an intermediate layer of “supplementary vertices” such as Sgqv@%.... Each of these supplementary vertices lies roughly halfway between the center of the triangle“above” it and the center of the corresponding triangle “below" it. (c)

Connect each such “supplementary vertex”with its immediate neighbors above,below,and in the same plane.(d) Give all edge lengths. (e) Then the skeleton 3-geometry between the two 2-geometries is rigidly specified. It is made up of five types of tetrahedrons, as follows. (1） “Rightthrough blocks,” such as ${ \mathcal { P P } } { \mathcal { S } } { \mathcal { T } }$ (six of these hinge on ${ \mathcal { P } } { \mathcal { P } } ^ { \prime }$ when $\mathcal { P }$ is a normal vertex; five, when it is a 5-fold vertex,such as indicated by $\boldsymbol { \mathcal { Q } }$ at the upper right).(2)“Lower-facing blocks,"such as dBPg.(3)“Lower-packing blocks,” such as $\mathcal { Q } \mathcal { P } \mathcal { S } \mathcal { T }$ (4,5) Corresponding“upper-facing blocks” and “upper-packing blocks” (not shown). The number of blocks of each kind is appropriately listed here for the two extreme cases of a 2-geometry that consists (a) of a normal hexagonal lattice extending indefinitely in a plane and (b) of a lattice consisting of the minimum number of 5-fold vertices ("type $\boldsymbol { \mathcal { Q } }$ vertices") that will permit closeup into a 2-sphere.

<table><tr><td>2-geometry of upper (orlower face</td><td>Hexagonal pattern of triangles</td><td>Icosahedron madeoftriangles</td></tr><tr><td>Its topology Vertices on upper face Nature of these vertices Edge lengths on upper face</td><td>Infinite 2-plane V 6-fold 3V</td><td>2-sphere 12 5-fold V=30</td></tr><tr><td>Triangles on upper face Number of&quot;supplementary vertices&quot;</td><td>2V 2V</td><td>20 20</td></tr><tr><td>Outer facing blocks Outer packing blocks</td><td>2V</td><td>20</td></tr><tr><td>Right through blocks</td><td>3V 6V</td><td>30</td></tr><tr><td>Inner packing blocks Inner facing blocks</td><td>3V 2V</td><td>60 30</td></tr></table>

# $\$ 42.6$ ．THE CHOICE OF EDGE LENGTHS

The choice of edge lengths:

So much for the lattce structure of the 4-geometry; now for the other issue, the freedom that exists in the choice of edge lengths. Why not make the simplest choice and let all edges be light rays? Because the 4-geometry would not then be fully determined. The geometry $g _ { \alpha \beta } ( x ^ { \mu } )$ differs from the geometry $\lambda ( x ^ { \mu } ) \ g _ { \alpha \beta } ( x ^ { \mu } )$ even though the same points that are connected by light rays in the one geometry are also connected by light rays-in the other geometry.

If none of the edges is null, it is nevertheless natural to take some of the edge lengths to be spacelike and some to be timelike. In consequence the area $\pmb { A }$ of the triangle in some cases willbe real, in other cases imaginary. In 3-space the parallelogram (double triangle) spanned by two vectors $\pmb { B }$ and $^ { c }$ is described by a vector

(1） choose some timelike, others spacelike

$$
2 A = B \times C
$$

perpendicular to the two vectors. One obtains the magnitude of $\pmb { A }$ from the formula

$$
4 A ^ { 2 } = B ^ { 2 } C ^ { 2 } - ( B \cdot C ) ^ { 2 } .
$$

In 4-space, let $\pmb { B }$ and $\pmb { c }$ be two edges of the triangle. Then,as in three dimensions, 2A is dual to the bivector built from $\pmb { B }$ and $\pmb { c }$ In other words,if $\pmb { B }$ goes in the $t$ direction and $\pmb { c }$ in the $z$ direction, then $\pmb { A }$ is a bivector lying in the $( x , y )$ plane. Consequently its magnitude $\pmb { A }$ is to be thought of as a real quantity. Therefore the appropriate formula for the area $\pmb { A }$ is (Tullio Regge)

$$
4 A ^ { 2 } = ( B \cdot C ) ^ { 2 } - B ^ { 2 } C ^ { 2 } .
$$

The quantity $\pmb { A }$ is real when the deficit angle $\pmb { \delta }$ is real. Thus the geometrically important product $\boldsymbol { A } \boldsymbol { \delta }$ is also real.

When the hinge lies in the $( x , y )$ plane,on the other hand,the quantity $\pmb { A }$ is purely imaginary. In that instance a test vector taken around the cycle of simplexes that swing on this hinge has undergone change only in its $z$ and $t$ components; that is, it has experienced a Lorentz boost; that is,the deficit angle δ is also purely imaginary. So again the product $\boldsymbol { A } \boldsymbol { \delta }$ is a purely real quantity.

(2)choose timelike lengths comparable to spacelike lengths

Turn now from character of edge lengths to magnitude of edge lengths. lt is desirable that the elementary building blocks sample the curvatures of space in different directions on a roughly equal basis. In other words, it is desirable not to have long needle-shaped building blocks nor pancake-shaped tetrahedrons and simplexes.This natural requirement means that the step forward in time should be comparable to the steps “sidewise” in space. The very fact that one should have to state such a requirement brings out one circumstance that should have been obvious before: the “hinge equations”

$$
\sum _ { \mathrm { ~ \scriptsize ~  ~ } } \delta _ { h } \cot \theta _ { p h } = 0 ( p = 1 , 2 , \ldots ) ,
$$

(3) why some lengths must be chosen arbitrarily

though they are as numerous as the edges,cannot be regarded as adequate to determine al edge lengths. There are necessarily relations between these equations that keep them from being independent. The equations cannot determine all the details of the necessarily largely arbitrary skeletonization process. They cannot do so any more than the field equations of general relativity can determine the coordinate system. With a given pattern of vertices (four-dimensional generalization of drawings in Box 42.3),one still has (a) the option how close together one will take successive layers of the structure and (b) how one will distribute a given number of points in space on a given layer to achieve the maximum payoff in accuracy (greater density of points in regions of greater curvature). To prepare a practical computer program founded on Regge calculus, one has to supply the machine not only with the hinge equations and initial conditions,but also with definite algorithms to remove all the arbitrariness that resides in options (a) and (b).

Deficit angles in terms of edge lengths

Formulas from solid geometry and four-dimensional geometry, out of which to determine the necessary hyperdihedral angles $\pmb { \alpha }$ and the deficit angles δ in terms of edge lengths and nothing but edge lengths, are summarized by Wheeler (1964a, pp. 469,470,and 490)and by C. Y.Wong(1971). Regge (1961) also gives a formula for the Riemann curvature tensor itself in terms of deficit angles and number of edges running in a given direction [see also Wheeler (1964a, p. 471)].

# \$42.7. PAST APPLICATIONS OF REGGE CALCULUS

Past applications of Regge calculus

Wong (l971) has applied Regge calculus to a problem where no time development shows itself, where the geometry can therefore be treated as static,and where in addition it is spherically symmetric.He determined the Schwarzschild and Reissner-Nordstrom geometries by the method of skeletonization. Consider successive spheres surrounding the center of attraction.Wong approximates each as an icosahedron. The condition

$$
^ { ( 3 ) } R = 1 6 \pi \left( \stackrel { \mathrm { e n e r g y ~ d e n s i t y } } { \mathrm { o n ~ t h e ~ } } 3 { \cdot } \mathrm { s p a c e } \right)
$$

$( \ S 2 1 . 5 )$ gives a recursion relation that determines the dimension of each icosahedron in terms of the two preceding icosahedra. Errors in the skeleton representation of the exact geometry range from roughly l0 percent to less than 1 percent, depending on the method of analysis, the quantity under analysis,and the fineness of the subdivision.

Partial skeletonization

Skeletonization of geometry is to be distinguished from mere rewriting of partial differential equations as difference equations. One has by now three illustrations that one can capitalize on skeletonization without fragmenting spacetime allthe way to the level of individual simplexes. The first illustration is the first part of Wong's work, where the time dimension never explicitly makes an appearance, so that the building blocks are three-dimensional only. The second is an alternative treatment, also given by Wong, that goes beyond the symmetry in $t$ to take account of the symmetry in $\pmb \theta$ and $\phi$ .It divides space into spherical shells, in each of which the geometry is “pseudo-flat" in much the same sense that the geometry of a paper cone is flat. The third is the numerical solution for the gravitational collapse of a spherical star by May and White (l966), in which there is symmetry in $\pmb \theta$ and $\phi$ ,but not in $r$ or $t$ .This zoning takes place exclusively in the r,t-plane. Each zone is a spherical shell. The difference as compared to Regge calculus (flat geometry within each building block) is the adjustable “conicity” given to each shell. The examples show that the decision about skeletonizing the geometry in a calculation is ordinarily not "whether" but “how much.”

# $\$ 42.8$ . THE FUTURE OF REGGE CALCULUS

Hopes for the future

In summary, Regge's skeleton calculus puts within the reach of computation problems that in practical terms are beyond the power of normal analytical methods. It affords any desired level of accuracy by suffciently fine subdivision of the spacetime region under consideration.By way of its numbered building blocks, it also offers a practical way to display the results of such calculations. Finally, one can hope that Regge's truly geometric way of formulating general relativity wil someday make the content of the Einstein field equations (Cartan's “moment of rotation”; see Chapter 15） stand out sharp and clear, and unveil the geometric significance of the so-called "geometrodynamic field momentum"(analysis ofthe boundary-value problem asociated with the_yariational problem of general relativity in Regge calculus; see g2r.12).
