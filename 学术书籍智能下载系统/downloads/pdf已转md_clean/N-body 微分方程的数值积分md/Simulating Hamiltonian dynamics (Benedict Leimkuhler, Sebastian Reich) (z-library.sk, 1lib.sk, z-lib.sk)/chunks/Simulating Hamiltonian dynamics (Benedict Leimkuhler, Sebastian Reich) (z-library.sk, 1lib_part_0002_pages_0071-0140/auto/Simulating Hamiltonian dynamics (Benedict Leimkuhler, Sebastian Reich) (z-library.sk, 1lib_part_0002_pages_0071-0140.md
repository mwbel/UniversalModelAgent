One then requires a definition of the corresponding transformed conjugate momenta $\hat { p }$ such that the overall transformation $\pmb { \psi }$ from $( \pmb q , \pmb p )$ to $( \hat { \pmb q } , \hat { \pmb p } )$ is symplectic. Such a definition is provided by

$$
\hat { p } : = [ h _ { q } ( q ) ] ^ { - T } p .
$$

The overall coordinate transformation $\pmb { \psi }$ is hence given by

$$
\psi ( q , p ) = \left[ \begin{array} { c } { { h ( q ) } } \\ { { { [ } h _ { q } ( q ) { ] } ^ { - T } p } } \end{array} \right] .
$$

This type of symplectic transformation is sometimes called a canonical point transformation [73, 124].

The Jacobian of the map $\pmb { \psi }$ is

$$
\pmb { \psi } _ { z } ( z ) = \left[ \begin{array} { c c } { h _ { q } ( \pmb { q } ) } & { \mathbf { 0 } } \\ { G ( \pmb { q } , \pmb { p } ) } & { [ h _ { q } ( \pmb { q } ) ] ^ { - T } } \end{array} \right] ,
$$

where $G ( \pmb { q } , \pmb { p } )$ is the matrix of partial derivative of the vector $[ h _ { q } ( q ) ] ^ { - T } p$ with respect to $\pmb q$ . It can be verified by explicit computation that

$$
\pmb { \psi } _ { z } ( z ) ^ { T } \pmb { J } ^ { - 1 } \pmb { \psi } _ { z } ( z ) = \pmb { J } ^ { - 1 } ,
$$

where $\jmath$ is the canonical structure matrix. A different proof for the symplecticness of canonical point transformations will be given in Section 3.6.

For the coordinate transformation from polar to cartesian coordinates, we obtain the expression

$$
{ \left[ \begin{array} { l } { p _ { 1 } } \\ { p _ { 2 } } \end{array} \right] } = { \frac { 1 } { r } } \left[ r \sin \theta \quad \cos \theta \right] { \left[ \begin{array} { l } { p _ { r } } \\ { p _ { \theta } } \end{array} \right] } \left[ { \begin{array} { l } { p _ { r } } \\ { p _ { \theta } } \end{array} } \right]
$$

for the conjugate momenta $p _ { r } , ~ p _ { \theta }$ . This implies that the kinetic energy of a particle in $\mathbb { R } ^ { 2 }$ with mass $m$ transforms according to

$$
{ \frac { 1 } { 2 m } } \left( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } \right) = { \frac { 1 } { 2 m } } \left( p _ { r } ^ { 2 } + { \frac { 1 } { r ^ { 2 } } } p _ { \theta } ^ { 2 } \right) .
$$

The main result of this section is contained in the following:

Theorem 1 The flow map $\pmb { \phi } _ { \tau , H }$ of a Hamiltonian system (3.7) is symplectic. ✷

Proof. Recall that the Jacobian of the flow map

$$
\pmb { F } ( t ) = \frac { \partial } { \partial z } \pmb { \phi } _ { t , H } ( z )
$$

satisfies the variational equation (3.24) with initial condition $F ( 0 ) = I _ { 2 d }$ . To prove the proposition, we have to verify that

$$
F ( t ) ^ { T } J ^ { - 1 } F ( t ) = J ^ { - 1 } .
$$

Since $F ( 0 ) = I _ { 2 d }$ the statement is true for $t = 0$ . Hence we only have to show that

$$
\frac { d } { d t } K = 0 , \qquad K ( t ) : = F ( t ) ^ { T } J ^ { - 1 } F ( t ) .
$$

Indeed, we obtain

$$
\begin{array} { r l } & { \frac { d } { d t } K = F ^ { T } J ^ { - 1 } \dot { F } + \left[ \dot { F } \right] ^ { T } J ^ { - 1 } F } \\ & { ~ = F ^ { T } J ^ { - 1 } \left[ J H _ { z z } ( z ( t ) ) F \right] + \left[ F ^ { T } H _ { z z } ( z ( t ) ) J ^ { T } \right] J ^ { - 1 } F } \\ & { ~ = F ^ { T } H _ { z z } ( z ( t ) ) F - F ^ { T } H _ { z z } ( z ( t ) ) F } \\ & { ~ = \bf { 0 } . } \end{array}
$$

The symplecticness of the flow map implies the existence of certain global conservation laws or integral invariants related to the evolution of subsets of phase space. In particular, we will show in the following subsection that symplecticness implies preservation of area for one-degree-of-freedom systems ( $\left[ d = 1 \right.$ ). In higher dimensions this invariant is replaced by the preservation of volume $( d > 1 )$ ). Conservation of volume under the flow map of a canonical Hamiltonian system follows from Liouville’s Theorem [7] (see problem 7 in the Exercises), but it can also be considered as a consequence of the symplecticness of the flow map.6 In other words, the sets $\mathcal { U } _ { t }$ , $t > 0$ , defined by (3.21) might change their shapes significantly but they will always occupy the same volume in phase space as time $t$ increases. The existence of this integral invariant implies severe and important restrictions on the possible solution behavior of Hamiltonian dynamical systems. As we will see throughout this book, preservation of the symplectic structure under numerical discretization is often a very desirable property for long-term approximate integration of Hamiltonian systems.

# 3.5.1 One-degree-of-freedom systems

Let $\pmb { \psi } : \mathbb { R } ^ { 2 }  \mathbb { R } ^ { 2 }$ be a symplectic map in the plane. We write the Jacobian $\pmb { \psi } _ { z } ( z )$ as

$$
\pmb { \psi } _ { z } ( z ) = \left[ \begin{array} { c c } { { a } } & { { b } } \\ { { c } } & { { d } } \end{array} \right] .
$$

Using this in (3.25), we obtain the equivalent condition

$$
a d - b c = 1 .
$$

6Symplecticness also implies the existence of other integral invariants for $d > 1$ . Thus the concept of symplecticness is a stronger property than conservation of volume.

However, this is the same as saying

$$
\mathsf { d e t } [ \pmb { \psi } _ { z } ( z ) ] = 1 .
$$

Thus, for planar maps $\pmb { \psi }$ , the condition of symplecticness (3.25) is that the determinant of the Jacobian ${ \pmb { \psi } } _ { z } ( z )$ is everywhere equal to one.

What is the implication of this for the behavior of the map $\pmb { \psi } ?$ Let $\mathcal { R }$ be a bounded subset of phase space. The oriented area7 $\alpha ( \mathcal { R } )$ is defined by the integral

$$
\alpha ( \mathcal { R } ) = \int _ { \mathcal { R } } d q d p .
$$

Let $\hat { \mathcal { R } }$ denote the image of $\mathcal { R }$ under $\pmb { \psi }$ , i.e. ${ \hat { \mathcal { R } } } = \pmb { \psi } ( { \mathcal { R } } )$ . Then, following the standard rules for changing variables in an integral

$$
\begin{array} { l } { \displaystyle \alpha ( \hat { \mathcal { R } } ) = \int _ { \hat { \mathcal { R } } } d \hat { q } d \hat { p } } \\ { \displaystyle \quad = \int _ { \mathcal { R } } \operatorname* { d e t } [ \psi _ { z } ( z ) ] d q d p } \\ { \displaystyle \quad = \int _ { \mathcal { R } } d q d p } \\ { \displaystyle \quad = \alpha ( \mathcal { R } ) . } \end{array}
$$

Thus a symplectic map of the plane is area preserving.

The implications of symplecticness for the behavior of maps in higher dimensions are taken up in the following section.

# 3.5.2 The symplectic structure of phase space

We now turn to the general situation and discuss the symplectic structure associated to $2 d \cdot$ -dimensional phase space. The book of LANDAU AND LIFSHITZ [105] gives a clear explanation of the symplectic structure. A more advanced and mathematically precise treatment will be found in the book of ARNOLD [7].

Let us start with some notation from differential geometry. A two-form on $\mathbb { R } ^ { 2 d }$ is a skew-symmetric bilinear function $\Omega ( \pmb { \xi } , \pmb { \eta } )$ with arguments $\pmb { \xi }$ and $\pmb { \eta }$ in $\mathbb { R } ^ { 2 d }$ . Bilinearity means that the function is linear in each of its two arguments

![](images/a5babd35f0e1eac7c15b1ff88d3149414846eda36e4f31bbfd8adbd2a3951f86.jpg)  
Figure 3.4 The two-form $\Omega$ for $d = 1$ is the oriented area of the parallelogram described by a pair of vectors in $\mathbb { R } ^ { 2 }$ , i.e. it is the transverse coordinate of the cross product of the pair of vectors viewed as embedded in $\mathbb { R } ^ { 3 }$ .

separately, and skew-symmetry means

$$
\Omega ( \pmb { \xi } , \pmb { \eta } ) = - \Omega ( \pmb { \eta } , \pmb { \xi } ) ,
$$

for any $\xi , \eta$

The symplectic structure matrix

$$
J = \left[ \begin{array} { c c } { { { \bf 0 } } } & { { + I _ { d } } } \\ { { - I _ { d } } } & { { { \bf 0 } } } \end{array} \right] ,
$$

introduces the symplectic two-form $\Omega$ on the phase space $\mathbb { R } ^ { 2 d }$

$$
\Omega ( \pmb { \xi } , \pmb { \eta } ) : = \pmb { \xi } ^ { T } J ^ { - 1 } \pmb { \eta } , \qquad \pmb { \xi } , \pmb { \eta } \in \mathbb { R } ^ { 2 d } .
$$

Let us give a geometric interpretation of the two-form $\Omega$ . For $d = 1$ , $\Omega ( \pmb { \xi } , \pmb { \eta } )$ is the oriented area of the parallelogram spanned by the two vectors $\pmb { \xi }$ and $\pmb { \eta }$ in $\mathbb { R } ^ { 2 }$ . This is easily verified since, for $d = 1$

$$
\begin{array} { r } { \pmb { \xi } ^ { T } J ^ { - 1 } \pmb { \eta } = \xi _ { 2 } \eta _ { 1 } - \xi _ { 1 } \eta _ { 2 } , \qquad \pmb { \xi } = ( \xi _ { 1 } , \xi _ { 2 } ) ^ { T } , \pmb { \eta } = ( \eta _ { 1 } , \eta _ { 2 } ) ^ { T } \in \mathbb { R } ^ { 2 } . } \end{array}
$$

The orientation of area refers to the fact that $\Omega ( \pmb { \xi } , \pmb { \eta } )$ is either equal to the area spanned by $\pmb { \xi }$ and $\pmb { \eta }$ or is equal to the negative of this area. Viewing the two planar vectors as embedded in $\mathbb { R } ^ { 3 }$ , the two-form $\Omega$ is nothing but the $Z$ -coordinate of the cross product of the two vectors (Fig. 3.4).

For $d > 1$ , we project $\pmb { \xi } \in \mathbb { R } ^ { 2 d }$ and $\pmb { \eta } \in \mathbb { R } ^ { 2 d }$ down on to the $\left( q _ { i } , p _ { i } \right)$ -coordinate planes, $i = 1 , \ldots , d$ . Denote the corresponding vectors in $\mathbb { R } ^ { 2 }$ by $\pmb { \xi } ^ { ( i ) }$ , $\pmb { \eta } ^ { ( i ) }$ respectively, $i = 1 , \ldots , d$ . Then $\Omega ( \pmb { \xi } , \pmb { \eta } )$ is equivalent to the sum of the oriented areas of the parallelograms spanned by the pair of vectors $\pmb { \xi } ^ { ( i ) }$ and $\pmb { \eta } ^ { ( i ) }$ . To be precise, if we now denote by $\Omega _ { 0 }$ the standard two-form of a pair of vectors in the plane, define

$$
\Omega ( \pmb { \xi } , \pmb { \eta } ) = \sum _ { i = 1 } ^ { d } \Omega _ { 0 } ( \pmb { \xi } ^ { ( i ) } , \pmb { \eta } ^ { ( i ) } ) .
$$

In fact, this is synonymous with saying

$$
\Omega ( \pmb { \xi } , \pmb { \eta } ) = \pmb { \xi } ^ { T } \pmb { J } ^ { - 1 } \pmb { \eta } ,
$$

where $\jmath$ refers to the symplectic structure matrix in $\mathbb { R } ^ { 2 d }$ .

Next we consider the integral of $\Omega$ over a smooth two-dimensional surface $S \subset \mathbb { R } ^ { 2 d }$ of phase space. We can view such a two-surface as being described8 by a smooth mapping $\pmb { \sigma }$ from an open subset $\mathcal { R }$ of the $( u , v )$ -plane into phase space $\mathbb { R } ^ { 2 d }$ such that the partial derivatives $\pmb { \sigma } _ { u } ( u , v )$ and $\pmb { \sigma } _ { v } ( u , v )$ are linearly independent vectors for all $( u , v ) \in \mathcal { R }$ . We define the integral of the two-form $\Omega$ over the surface $s$ by

$$
\begin{array} { r } { \int _ { \mathcal { S } } \Omega : = \int _ { \mathcal { R } } \Omega ( \pmb { \sigma } _ { u } d u , \pmb { \sigma } _ { v } d v ) } \\ { = \int _ { \mathcal { R } } \pmb { \sigma } _ { u } ^ { T } J ^ { - 1 } \pmb { \sigma } _ { v } d u d v ; } \end{array}
$$

the last integral is to be understood as the usual integral of the function $f : =$ $\pmb { \sigma } _ { u } ^ { T } \pmb { J } ^ { - 1 } \pmb { \sigma } _ { v }$ over $\mathcal { R } \subset \mathbb { R } ^ { 2 }$ . To give a geometric interpretation to the integral, we separate the mapping $\pmb { \sigma }$ into $d$ components $\pmb { \sigma } _ { 1 } , \pmb { \sigma } _ { 2 } , \dots . . . , \pmb { \sigma } _ { d }$ , with $\pmb { \sigma } _ { i }$ taking values in the $\left( p _ { i } , q _ { i } \right)$ -coordinate plane. Denote the image of $\mathcal { R }$ under $\pmb { \sigma } _ { i }$ by $S _ { i } \subset \mathbb { R } ^ { 2 }$ . To interpret the integral of $\Omega$ over the surface $s$ , we first partition $\mathcal { R }$ into a mesh of small rectangles with dimensions $\Delta u \times \Delta v$ . Such a partition results in corresponding partitions of each of the map images (the coordinate plane projections of the surface) into small curved regions (see Fig. 3.5). For a fine enough partition, the “rectangle images” are approximated by parallelograms (see Fig. 3.6) spanned by the vectors

$$
\pmb { \xi } ^ { ( i ) } = \pmb { \sigma } _ { i , u } \Delta u \in \mathbb { R } ^ { 2 } , \qquad \pmb { \eta } ^ { ( i ) } = \pmb { \sigma } _ { i , v } \Delta v \in \mathbb { R } ^ { 2 } .
$$

The integral of the two-form $\Omega$ is now approximated by the sum of the oriented areas of these parallelograms. The integral of $\Omega$ over $s$ is then taken to be the limiting value of this sum as the diameter of the underlying mesh imposed on $\mathcal { R }$ tends uniformly to zero. In other words

$$
\int _ { S } \Omega = \sum _ { i } \alpha ( S _ { i } ) ,
$$

with $\alpha ( S _ { i } )$ being the oriented area of $S _ { i } \subset \mathbb { R } ^ { 2 }$ .

$^ 8 | { \mathfrak { n } }$ general, the surface must be divided into a collection of overlapping regions called charts, in each of which a local parameterization is defined [7].

![](images/fd1620f26a81700d6f6626e39cfc0447106c415d56152087ed77652a8ddf1600.jpg)  
Figure 3.5 A surface is defined by a parameterization: a collection of $d$ mappings from a parameter space in the uv -plane to the canonical $\left( q _ { i } , p _ { i } \right)$ - coordinate planes. A rectangular mesh in parameter space induces a curved mesh in the coordinate planes.

Now consider how the symplectic two-form $\Omega$ changes under a coordinate transformation $\pmb { \psi } : \mathbb { R } ^ { 2 d }  \mathbb { R } ^ { 2 d }$ . We define the transformed differential form ${ \pmb { \psi } } ^ { * } \Omega$ by

$$
\pmb { \psi } ^ { \ast } \Omega \left( \pmb { \xi } , \pmb { \eta } \right) : = \Omega \left( \pmb { \psi } _ { z } ( z ) \pmb { \xi } , \pmb { \psi } _ { z } ( z ) \pmb { \eta } \right) .
$$

In other words, ${ \pmb { \psi } } ^ { * } \Omega ( \pmb { \xi } , \pmb { \eta } )$ is equal to $\Omega ( \hat { \pmb { \xi } } , \hat { \pmb { \eta } } )$ where $\hat { \xi } , \hat { \eta }$ are the transports of the vectors $\pmb { \xi }$ and $\pmb { \eta }$ , respectively, under the linearization (Jacobian matrix) of $\pmb { \psi }$ . A transformation $\pmb { \psi }$ is called symplectic, if

$$
\psi ^ { * } \Omega = \Omega ,
$$

or, equivalently

$$
\pmb { \psi } _ { z } ( z ) ^ { T } \pmb { J } ^ { - 1 } \pmb { \psi } _ { z } ( z ) = \pmb { J } ^ { - 1 } ,
$$

![](images/a67e524649422a578f9a46db94bbfc4939956b870685d667b3619140f8ca40e5.jpg)  
Figure 3.6 For a small rectangular patch in parameter space, the image under the parameterization is a small region that is approximated by a parallelogram whose oriented area is computed in the usual way. The integral of the two-form over a two-surface is then obtained as the limit, for decreasing meshwidth in parameter space, of the sum of the induced two-forms.

which is the definition we gave before. In other words, symplectic maps leave the symplectic two-form $\Omega$ invariant. Thus, for $d = 1$ , a map $\pmb { \psi }$ is symplectic if the parallelogram spanned by $\pmb { \xi }$ and $\pmb { \eta }$ has the same area as the parallelogram spanned by the two vectors $\pmb { \psi } _ { z } ( z ) \pmb { \xi }$ and ${ \pmb { \psi } } _ { z } ( z ) { \pmb { \eta } }$ . This implies that, for $d = 1$ , a symplectic map conserves area.

More generally, this important integral invariance can be written as

$$
\begin{array} { l } { \displaystyle { \int _ { \mathcal { S } } \Omega : = \int _ { \mathcal { S } } \pmb { \psi } ^ { * } \Omega } } \\ { \displaystyle \qquad = \int _ { \mathcal { R } } \Omega ( \pmb { \psi } _ { z } \pmb { \sigma } _ { u } d u , \pmb { \psi } _ { z } \pmb { \sigma } _ { v } d v ) } \end{array}
$$

$$
\begin{array} { l } { \displaystyle = \int _ { \mathcal R } \Omega \left( \bar { \pmb { \sigma } } _ { u } d u , \bar { \pmb { \sigma } } _ { v } d v \right) } \\ { \displaystyle = \int _ { \bar { \mathcal S } } \Omega , } \end{array}
$$

where ${ \bar { \mathcal { S } } } : = \psi ( { \mathcal { S } } )$ and $\bar { \pmb { \sigma } } : = \pmb { \psi } \circ \pmb { \sigma } : \mathcal { R }  \bar { \mathcal { S } }$ is a parameterization of $\bar { S }$ . For $d > 1$ , this formula implies the conservation of a sum of oriented areas of projections of $s$ on to the $\left( q _ { i } , p _ { i } \right)$ -coordinate planes, i.e.

$$
\sum _ { i } \alpha ( S _ { i } ) = \sum _ { i } \alpha ( \bar { S } _ { i } ) .
$$

We refer to this quantity as the symplectic area.

We have already mentioned that the flows of Hamiltonian systems preserve volume in phase space. In fact, it can be shown that conservation of the symplectic two-form $\Omega$ alone implies that the sum over all distinct $k$ -tuples $1 \leq i _ { 1 } < i _ { 2 } <$ $\dots < i _ { k } \le d$ of oriented volumes of projections of a $2 k$ -dimensional submanifold on to the $\left( p _ { i _ { 1 } } , p _ { i _ { 2 } } , \ldots , p _ { i _ { k } } , q _ { i _ { 1 } } , q _ { i _ { 2 } } , \ldots , q _ { i _ { k } } \right)$ -coordinate system is also conserved under the map [7]; as a special case ( $k = d$ ), this implies the conservation of phase space volume.

We also mention that, although our geometric interpretation above relied on the fact that $\jmath$ was the canonical structure matrix, a corresponding geometric property would hold locally for any Hamiltonian system. This is a consequence of Darboux’s theorem [7, 8].

# 3.6 Differential forms and the wedge product

The definition (3.28) is not always the most convenient approach to check the symplecticness of a given map $\pmb { \psi }$ . This is true in particular if the map is given implicitly or the definition involves additional variables that could, in principle, be eliminated. In those cases, it is best to use implicit differentiation combined with a definition of symplecticness in terms of differential one- and two-forms. We develop the necessary mathematical material in this section.

Recall from calculus that if $f : \mathbb { R } ^ { m }  \mathbb { R }$ is a smooth function, then its directional derivative along a vector $\pmb { \xi } \in \mathbb { R } ^ { m }$ , denoted here by $d f ( \pmb { \xi } )$ , is given by

$$
d f ( \pmb { \xi } ) = \frac { \partial f } { \partial z _ { 1 } } \xi _ { 1 } + \frac { \partial f } { \partial z _ { 2 } } \xi _ { 2 } + \cdot \cdot \cdot + \frac { \partial f } { \partial z _ { m } } \xi _ { m } ,
$$

where the partial derivatives of $f$ are computed at a fixed location $z \in \mathbb { R } ^ { m }$ . It is clear from the definition that $d f ( \pmb { \xi } )$ is linear in $\pmb { \xi }$ . The linear functional $d f ( . )$ is called the differential of $f$ at $z$ and is an $\mathsf { e x }$ ample of a differential one-form.

A particularly simple class of differentials is provided by the coordinate functions $f ( z ) = z _ { i }$ and

$$
d z _ { i } ( \pmb { \xi } ) = \xi _ { i } ,
$$

$i = 1 , \dots , m$ . Indeed, the differentials $d z _ { i }$ can be used as a basis for representing any other differential df since

$$
d f ( { \pmb \xi } ) = \frac { \partial f } { \partial z _ { 1 } } d z _ { 1 } ( { \pmb \xi } ) + \frac { \partial f } { \partial z _ { 2 } } d z _ { 2 } ( { \pmb \xi } ) + \dots + \frac { \partial f } { \partial z _ { m } } d z _ { m } ( { \pmb \xi } ) ,
$$

and, consequently

$$
d f = { \frac { \partial f } { \partial z _ { 1 } } } d z _ { 1 } + { \frac { \partial f } { \partial z _ { 2 } } } d z _ { 2 } + \cdot \cdot \cdot + { \frac { \partial f } { \partial z _ { m } } } d z _ { m } .
$$

To summarize, the set of all differentials at a point $z \in \mathbb { R } ^ { m }$ forms a linear space with the differentials $d z _ { i }$ as a basis.

We now apply a coordinate transformation $\pmb { \psi } : \mathbb { R } ^ { m }  \mathbb { R } ^ { m }$ and define

$$
{ \hat { z } } = \psi ( z ) ,
$$

as well as the transformed function

$$
{ \hat { f } } ( z ) = f ( { \hat { z } } ) = f ( \pmb { \psi } ( z ) ) .
$$

Denoting the ith component of the transformation $\pmb { \psi }$ by $\Psi ^ { j }$ , i.e. $\hat { z } _ { i } = \Psi ^ { i } ( z )$ , the standard chain rule implies

$$
\begin{array} { r l } & { d \hat { t } = \displaystyle { \sum _ { j } \frac { \partial f } { \partial \hat { z } _ { j } } \frac { \partial \Psi ^ { j } } { \partial z _ { 1 } } d z _ { 1 } } + \sum _ { j } \frac { \partial f } { \partial \hat { z } _ { j } } \frac { \partial \Psi ^ { j } } { \partial z _ { 2 } } d z _ { 2 } + \cdots + \sum _ { j } \frac { \partial f } { \partial \hat { z } _ { j } } \frac { \partial \Psi ^ { j } } { \partial z _ { m } } d z _ { m } , } \\ & { \quad = \displaystyle { \frac { \partial f } { \partial \hat { z } _ { 1 } } \sum _ { i } \frac { \partial \Psi ^ { 1 } } { \partial z _ { i } } d z _ { i } } + \frac { \partial f } { \partial \hat { z } _ { 2 } } \sum _ { i } \frac { \partial \Psi ^ { 2 } } { \partial z _ { i } } d z _ { i } + \cdots + \frac { \partial f } { \partial \hat { z } _ { m } } \sum _ { i } \frac { \partial \Psi ^ { m } } { \partial z _ { i } } d z _ { i } } ,  \end{array}
$$

which we rewrite as

$$
d \hat { f } = \frac { \partial f } { \partial \hat { z } _ { 1 } } d \hat { z } _ { 1 } + \frac { \partial f } { \partial \hat { z } _ { 2 } } d \hat { z } _ { 2 } + \cdot \cdot \cdot + \frac { \partial f } { \partial \hat { z } _ { m } } d \hat { z } _ { m } ,
$$

in the new basis

$$
d \hat { Z } _ { j } = \sum _ { i } \frac { \partial \Psi ^ { j } } { \partial z _ { i } } d z _ { i } .
$$

To compactify the notation, we introduce the column vector of differential oneforms

$$
d z = ( d z _ { 1 } , d z _ { 2 } , \ldots , d z _ { m } ) ^ { T } ,
$$

with the property that $d z ( \pmb { \xi } ) = \pmb { \xi }$ and hence

$$
d f = f _ { z } \cdot d z .
$$

The transformation rule (3.29) becomes

$$
d \hat { z } = \pmb { \psi } _ { z } ( z ) d z ,
$$

and, consequently

$$
d \hat { z } ( \pmb { \xi } ) = \pmb { \psi } _ { z } ( z ) d z ( \pmb { \xi } ) = \pmb { \psi } _ { z } ( z ) \pmb { \xi } .
$$

Let us now come back to symplectic transformations and a splitting of variables $\pmb { \mathrm { \tau } } _ { Z } = ( \pmb { q } , \pmb { p } ) \in \mathbb { R } ^ { 2 d }$ with associated one-forms $d q _ { i }$ , $d p _ { j }$ , $i = 1 , \ldots , d$ . Given any two vectors $\pmb { \xi } , \pmb { \eta } \in \mathbb { R } ^ { 2 d }$ , the symplectic two-form $\Omega$ is defined by

$$
\Omega ( \pmb { \xi } , \pmb { \eta } ) = \pmb { \xi } ^ { T } J ^ { - 1 } \pmb { \eta } .
$$

Using the ordering of the two vectors $\pmb { \xi }$ and $\pmb { \eta }$ into a sequence of projections $\pmb { \xi } ^ { ( i ) } , \pmb { \eta } ^ { ( i ) } \in \mathbb { R } ^ { 2 }$ down on to the $\left( q _ { i } , p _ { i } \right)$ -coordinate planes, as introduced in the previous section, it is straightforward to verify that

$$
\Omega ( { \pmb \xi } , { \pmb \eta } ) = \sum _ { i } \Omega _ { 0 } ( { \pmb \xi } ^ { ( i ) } , { \pmb \eta } ^ { ( i ) } ) = \sum _ { i } \left[ d p _ { i } ( { \pmb \xi } ) d q _ { i } ( { \pmb \eta } ) - d q _ { i } ( { \pmb \xi } ) d p _ { i } ( { \pmb \eta } ) \right] ,
$$

where, by definition, $d q _ { i } ( \pmb { \xi } ) = \xi _ { 1 } ^ { ( i ) }$ , $d p _ { i } ( \pmb { \xi } ) = \xi _ { 2 } ^ { ( i ) }$ etc. This suggests to introduce the wedge product of two differentials $d f$ and $d g$ via

$$
( d f \wedge d g ) ( \pmb { \xi } , \pmb { \eta } ) : = d g ( \pmb { \xi } ) d f ( \pmb { \eta } ) - d f ( \pmb { \xi } ) d g ( \pmb { \eta } ) ,
$$

and, in particular, to write

$$
\Omega = \sum _ { i } d q _ { i } \wedge d p _ { i } .
$$

Using vector notation, we shorten this to

$$
\Omega = d \pmb { q } \wedge d \pmb { p } .
$$

Conservation of symplecticness, under a transformation

$$
\begin{array} { c } { { \hat { q } = { \pmb { \psi } } ^ { 1 } ( { \pmb q } , { \pmb p } ) , } } \\ { { \hat { p } = { \pmb { \psi } } ^ { 2 } ( { \pmb q } , { \pmb p } ) } } \end{array}
$$

reduces now to the statement that

$$
d \hat { \pmb q } \wedge d \hat { \pmb { p } } = d \pmb { q } \wedge d \pmb { p } ,
$$

where

$$
\begin{array} { r } { d \hat { \pmb q } = \pmb { \psi } _ { \pmb q } ^ { 1 } ( \pmb q , \pmb p ) d \pmb q + \pmb { \psi } _ { p } ^ { 1 } ( \pmb q , \pmb p ) d \pmb { p } , } \\ { d \hat { \pmb q } = \pmb { \psi } _ { \pmb q } ^ { 2 } ( \pmb q , \pmb p ) d \pmb q + \pmb { \psi } _ { p } ^ { 2 } ( \pmb q , \pmb p ) d \pmb { p } . } \end{array}
$$

We will prove this result below.

One can immediately verify several algebraic properties of the wedge product which prove useful in calculations:

PROPERTIES OF THE WEDGE PRODUCT

Let da, db, dc, be $k$ -vectors of differential one-forms on $\mathbb { R } ^ { m }$ , then the following properties hold.

1. Skew-symmetry

$$
d a \wedge d b = - d b \wedge d a .
$$

2. Bilinearity: for any $\alpha , \beta \in \mathbb { R }$

$$
d \pmb { a } \wedge ( \alpha d \pmb { b } + \beta d \pmb { c } ) = \alpha d \pmb { a } \wedge d \pmb { b } + \beta d \pmb { a } \wedge d \pmb { c } .
$$

3. Rule of matrix multiplication (as a consequence of Property 2 and the definition)

$$
d \pmb { a } \wedge ( \pmb { A } d \pmb { b } ) = ( \pmb { A } ^ { T } d \pmb { a } ) \wedge d \pmb { b } ,
$$

for any $k \times k$ matrix A. (See Problem 9 in the Exercises.)

Note that Properties 1 and 3 of the wedge product imply that, if $\pmb { A }$ is a symmetric matrix, then

$$
d { \pmb a } \wedge ( { \pmb A } d { \pmb a } ) = 0 .
$$

We now prove (3.30). We first verify that

$$
d pmb { q } \wedge d \pmb { p } = \frac { 1 } { 2 } ( J ^ { - 1 } d z ) \wedge d z .
$$

Indeed, we have

$$
\begin{array} { l } { { ( J ^ { - 1 } d z ) \wedge d z = \displaystyle \sum _ { i = 1 } ^ { d } [ d z _ { i } \wedge d z _ { d + i } - d z _ { d + i } \wedge d z _ { i } ] } } \\ { { { } } } \\ { { { } = \displaystyle \sum _ { i = 1 } ^ { d } [ d q _ { i } \wedge d p _ { i } - d p _ { i } \wedge d q _ { i } ] } } \\ { { { } } } \\ { { { } = 2 d q \wedge d p . } } \end{array}
$$

Hence (3.30) is equivalent to

$$
( J ^ { - 1 } d \hat { z } ) \wedge d \hat { z } = ( J ^ { - 1 } d z ) \wedge d z ,
$$

where

$$
d \hat { z } = \pmb { { \psi } } _ { z } ( z ) d z .
$$

Applying the rule of matrix multiplication, we obtain

$$
\begin{array} { r } { ( J ^ { - 1 } d \hat { z } ) \wedge d \hat { z } = \left( J ^ { - 1 } \pmb { \psi } _ { z } ( z ) d z \right) \wedge ( \pmb { \psi } _ { z } ( z ) d z ) , } \\ { = \left( \pmb { \psi } _ { z } ( z ) ^ { T } J ^ { - 1 } \pmb { \psi } _ { z } ( z ) d z \right) \wedge d z , } \end{array}
$$

and symplecticness of the map $\pmb { \psi }$ , i.e.

$$
\pmb { \psi } _ { z } ( z ) ^ { T } \pmb { J } ^ { - 1 } \pmb { \psi } _ { z } ( z ) = \pmb { J } ^ { - 1 }
$$

implies (3.31).

As indicated in the introduction, the wedge product notation can be combined with implicit differentiation which makes it a powerful tool to verify symplecticness of an implicitly given transformation $\pmb { \psi }$ . As an illustration, let us come back to the canonical point transformation

$$
\begin{array} { c } { \hat { \pmb q } = { \pmb h } ( { \pmb q } ) , } \\ { { \pmb h } _ { { \pmb q } } ( { \pmb q } ) ^ { T } \hat { \pmb p } = { \pmb p } , } \end{array}
$$

as already discussed in Example 6. Implicit differentiation yields

$$
\begin{array} { c } { d \hat { \pmb q } = { \pmb h } _ { \pmb q } ( { \pmb q } ) d { \pmb q } , } \\ { { \pmb h } _ { \pmb q } ( { \pmb q } ) ^ { T } d \hat { \pmb p } + \displaystyle \sum _ { i } \hat { p } _ { i } h _ { { \pmb q } { \pmb q } } ^ { i } d { \pmb q } = d { \pmb p } , } \end{array}
$$

where $h ^ { j } ( \pmb q )$ denotes the ith component of the transformation $\pmb { h } ( \pmb q )$ . Taking wedge products with $d \hat { p }$ and $d \pmb q$ , respectively, leads to

$$
d \hat { \pmb { q } } \wedge d \hat { \pmb { p } } = ( h _ { \pmb { q } } ( \pmb { q } ) d \pmb { q } ) \wedge d \hat { \pmb { p } } = d \pmb { q } \wedge \left( h _ { \pmb { q } } ( \pmb { q } ) ^ { T } d \hat { \pmb { p } } \right) ,
$$

and, since

$$
\sum _ { i } d { \pmb q } \wedge ( \hat { p } _ { i } h _ { { \pmb q } { \pmb q } } ^ { i } ( { \pmb q } ) d { \pmb q } ) = \sum _ { i } \hat { p } _ { i } \left[ d { \pmb q } \wedge ( h _ { { \pmb q } { \pmb q } } ^ { i } ( { \pmb q } ) d { \pmb q } ) \right] = 0 ,
$$

to

$$
d \pmb { q } \wedge d \pmb { p } = d \pmb { q } \wedge \left( h _ { q } ( \pmb { q } ) ^ { T } d \hat { \pmb { p } } + \sum _ { i } \hat { p } _ { i } h _ { q \pmb { q } } ^ { i } d \pmb { q } \right) = d \pmb { q } \wedge \left( h _ { q } ( \pmb { q } ) ^ { T } d \hat { \pmb { p } } \right) ,
$$

respectively. This implies

$$
d \hat { \pmb { q } } \wedge d \hat { \pmb { p } } = d \pmb { q } \wedge \Big ( \pmb { h } _ { \pmb { q } } ( \pmb { q } ) ^ { T } d \hat { \pmb { p } } \Big ) = d \pmb { q } \wedge d \pmb { p } ,
$$

as desired.

We will encounter more applications of this basic procedure in the following chapter.

# 3.7 Exercises

1. Lagrange’s equation.

a. Assume that equation (3.14) defines, for each fixed $\pmb q$ , a one-to-one map between the conjugate momenta $p$ and the velocities $\dot { \pmb q }$ . Let us write the inverse relation as $\dot { \pmb q } = \pmb v ( \pmb p , \pmb q )$ . Use this map in the Hamiltonian (3.16) to evaluate $\nabla _ { \boldsymbol { q } } H$ and $\nabla _ { p } H$ . The result shows that the Lagrange equation (3.13) is equivalent to a canonical Hamiltonian system (3.4)–(3.5).

b. Given the Lagrangian (3.17) verify the definition of the conjugate momenta (3.18) and find an explicit expression for the Hamiltonian $H$ in terms of $\pmb q$ and $\pmb { p }$ only. Show that

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } \pmb { q } = \frac { 1 } { m } \pmb { p } + \frac { 1 } { 2 m } \hat { b } \pmb { q } , } \\ { \displaystyle \frac { d } { d t } \pmb { p } = - \frac { \gamma } { \| \pmb { q } \| ^ { 3 } } \pmb { q } + \frac { 1 } { 2 m } \hat { b } \pmb { p } - \frac { 1 } { 4 m } \hat { b } ^ { T } \hat { b } \pmb { q } } \end{array}
$$

are the associated canonical equations of motion and that these equations are equivalent to (3.10).

2. Angular momentum.

a. Show that, angular momentum $m = q \times p$ is conserved for canonical equations with Hamiltonian

$$
H ( \pmb { q } , \pmb { p } ) = \frac { 1 } { 2 } \| \pmb { p } \| ^ { 2 } + \varphi ( \| \pmb { q } \| ) .
$$

If in addition $\varphi ( r ) = - 1 / r$ (Kepler problem), verify that the Runge–Lenz vector

$$
\pmb { e } = \pmb { p } \times \pmb { m } - \frac { \pmb { q } } { \Vert \pmb { q } \Vert }
$$

is also a first integral. You may use the vector identity

$$
\pmb { a } \times ( \pmb { b } \times \pmb { c } ) = \pmb { b } ( \pmb { a } \cdot \pmb { c } ) - \pmb { c } ( \pmb { a } \cdot \pmb { b } ) .
$$

b. Show that the canonical Equations (3.32)–(3.33) for a charged particle in a constant magnetic field $b$ possess the scalar quantity

$$
\mu = b \cdot ( q \times p )
$$

as a first integral. The preserved quantity is also called the magnetic momentum. In terms of the noncanonical Hamiltonian formulation (3.11)– (3.12), the magnetic momentum is given by

$$
\mu = b \cdot \left( q \times \left( p - \frac { 1 } { 2 } \pmb { b } \times \pmb { q } \right) \right) .
$$

3. Integrals of the N-body problem. Show that the total linear and angular momenta

$$
\pmb { p } _ { \mathrm { t o t } } = \sum _ { i = 1 } ^ { N } \pmb { p } _ { i } , \pmb { m } _ { \mathrm { t o t } } = \sum _ { i = 1 } ^ { N } \pmb { q } _ { i } \times \pmb { p } _ { i }
$$

are conserved quantities for an $N .$ -body system with distance-based pair potentials (the system does not need to be homogeneous).

4. Variational equations. Consider a planar central-force problem

$$
H = \frac 1 2 \| \pmb { p } \| ^ { 2 } + \varphi ( \| \pmb { q } \| ) , \qquad \pmb { q } , \pmb { p } \in \mathbb { R } ^ { 2 } .
$$

a. Find the variational equations for this problem.

b. Let $\pmb q ^ { * }$ be an equilibrium point $( \varphi ^ { \prime } ( \lVert \boldsymbol { q } ^ { * } \rVert ) = 0 )$ . Determine the eigenvalues and eigenvectors of the variational equations. [Hint: consider separately perturbations in (i) the radial $( q )$ direction and (ii) the tangential directions.] What does the eigenstructure suggest about the behavior of nearby solutions?

5. Canonical transformations. Consider the planar central-force problem of problem 4 and the canonical change to polar coordinates described in Example 6.

a. Show that the momentum corresponding to the angle variable, $p _ { \theta }$ , is just the third component $m _ { 3 } = q _ { 1 } p _ { 2 } - q _ { 2 } p _ { 1 }$ of the angular momentum vector $m$ , and, hence, is constant along any solution.

b. Using the result of part [a], show how to reduce the planar central-force problem to a one-degree-of-freedom problem. In particular, show that the Kepler problem can be reduced to a one-degree-of-freedom problem with potential energy function

$$
\varphi _ { \mathrm { r e d u c e d } } ( r ) = \frac { m _ { 3 } ^ { 2 } } { 2 r ^ { 2 } } - \frac { 1 } { r } .
$$

Graph this potential and discuss the behavior of solutions.

6. Canonical transformations. Show that the map $\pmb { \psi } _ { \epsilon }$ , defined by

$$
\begin{array} { l } { { Q = q + \varepsilon p , } } \\ { { P = p + \varepsilon F ( Q ) , } } \end{array}
$$

is symplectic for $\varepsilon > 0$ , provided the Jacobian matrix of the map $\pmb { F } : \mathbb { R } ^ { d }  \mathbb { R } ^ { d }$ at $Q$ is symmetric.

7. Volume preservation. The divergence of a vector field $\pmb { f } : \mathbb { R } ^ { k }  \mathbb { R } ^ { k }$ is defined by

$$
{ \mathrm { d i v } } \pmb { f } : = \sum _ { i = 1 } ^ { k } { \frac { \partial } { \partial z _ { i } } } t _ { i } .
$$

Liouville’s theorem [7] states that the phase flow of a divergence-free vector field preserves volume. Show that Hamiltonian vector fields are divergence free, i.e., $\mathrm { d i v } [ J \nabla _ { z } H ] \left( z \right) \equiv 0$ , which implies conservation of volume for Hamiltonian systems.

8. Volume preservation. The linear differential equation

$$
\frac { d } { d t } z = { \bf \cal A } z ,
$$

$z \in \mathbb { R } ^ { 4 }$ and

$$
\pmb { A } = \left[ \begin{array} { c c c c } { 3 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { - 1 } \end{array} \right] ,
$$

generates a flow map that is volume preserving. Show that the flow map does not preserve the symplectic two-form (3.27) ( $d = 2 .$ ) for any permutation of the variables.

9. Wedge product. Let da, db be two $k$ -vectors of differential one-forms on $\mathbb { R } ^ { m }$ . Verify the rule of matrix multiplication, i.e., show that

$$
d \pmb { a } \wedge ( \pmb { M } d \pmb { b } ) = ( \pmb { M } ^ { T } d \pmb { a } ) \wedge d \pmb { b } ,
$$

for any $k \times k$ matrix $M$ . Hint: Start from

$$
d \pmb { a } \wedge ( \pmb { M } d \pmb { b } ) = \sum _ { i } d a _ { i } \wedge \left( \sum _ { j } m _ { i j } d b _ { j } \right) .
$$

# 4

# Geometric integrators

In Chapter 2, we introduced the concept of a numerical integrator as a mapping which approximates the flow-map of a given system of differential equations. We have also seen a few instances of how such integrators behave, demonstrating concepts such as convergence and order of accuracy. We observed that the typical picture is a locally accurate approximation that gradually drifts further from the true trajectory (see Fig. 2.3, Fig. 2.5 and the left panel of Fig. 2.7); the rate of drift can be reduced by reducing the stepsize (and thereby also increasing the amount of computational work), but the qualitative picture does not change in any significant way.

What stands out as remarkable, therefore, is the behavior, illustrated in the right panel of Fig. 2.7, of the Euler-B method, which retains bounded trajectories when applied to the harmonic oscillator. In Chapter 2, we provided an explanation for this in the form of a linear stability analysis showing that certain methods, including St¨ormer–Verlet and Euler-B, have eigenvalues on the unit circle when applied to the harmonic oscillator (or any other oscillatory linear system), if the stepsize is below some threshold value. The Euler-B and St¨ormer–Verlet methods (among others) possess a strong asymptotic stability property for linear systems.

It is interesting to note that a related long-term stability property extends to nonlinear models. If we apply, for example, the St¨ormer–Verlet methods to the Lennard–Jones oscillator, we obtain the results illustrated in Fig. 4.1 (compare with Fig. 2.3 and Fig. 2.5). As in the case of the same method applied to the harmonic oscillator, the numerical method appears to be finding solution points on a periodic orbit not much different than the exact one. Note that it would be quite extraordinary to imagine that the actual period itself would be exactly resolved, so that we would expect the true and approximate solutions to drift slowly apart with time. On the other hand, the energy returns, in each period, to its initial value, and there is no noticeable steady accumulation of error in the energy. This is reflected in a qualitative agreement between the numerical and exact solutions. There is clearly some important feature of the St¨ormer–Verlet method, one that cannot be explained with the techniques (error analysis or linear stability analysis) mentioned in Chapter 2.

![](images/e949ed94f314ca5c1de512721d55917e8f5c7cc3bb72f9fe67fea88c5afbc822.jpg)  
Figure 4.1 Solution curves in the $q V \cdot$ -plane (left) and energy error (right) for the St¨ormer-Verlet method applied to the Lennard–Jones oscillator.

If these differences were observed solely in one-degree-of-freedom systems such as nonlinear oscillators, they would only be of academic interest, but this is not the case. The situation becomes still more dramatic when we look at a more complicated example. For example, we will consider in this section a simple molecular model consisting of a system of $N .$ -point masses interacting in pair potentials. We will see that the St¨ormer–Verlet method facilitates integration on very long time intervals, when applied to this complicated multidimensional nonlinear model problem.

In Chapter 3, we have seen some hints of a deeper theory when we discussed the structure of the flow map itself, focusing on those special properties of Hamiltonian systems

$$
\frac { d } { d t } z = J \nabla _ { z } H ( z ) ,
$$

such as the conservation of first integrals and the symplectic structure. We have seen that the symplectic property carries with it geometric implications regarding the way in which the flow map acts on sets of initial conditions. For example, the volume of a set of points in phase space is conserved by a Hamiltonian flow. The flows of conservative systems have a nonlinear structural stability property: solutions through points of a region of phase space cannot be squeezed together over time into a smaller region of phase space. Observations like this one led DE VOGELAERE in the 1950s [49] and later RUTH [166], CHANNEL [43] and FENG KANG [57] to wonder if the structural properties of the flow map of a Hamiltonian system, if imposed on the numerical integrator itself, might lead to improved behavior in simulations.

Recall that a map $\pmb { \psi }$ from $\mathbb { R } ^ { 2 d }$ to $\mathbb { R } ^ { 2 d }$ is said to be symplectic if

$$
\left[ \frac { \partial } { \partial z } \pmb { \psi } ( z ) \right] ^ { T } \pmb { J } ^ { - 1 } \left[ \frac { \partial } { \partial z } \pmb { \psi } ( z ) \right] = \pmb { J } ^ { - 1 } .
$$

Equivalently, if we write

$$
\left[ \begin{array} { l } { Q } \\ { P } \end{array} \right] = \boldsymbol { \psi } \left( \left[ \begin{array} { l } { q } \\ { p } \end{array} \right] \right) ,
$$

then the symplecticness of the map is summarized by the condition

$$
d \pmb { Q } \wedge d \pmb { P } = d \pmb { q } \wedge d \pmb { p } ,
$$

in terms of the wedge product of differential one-forms.

As in Chapter 2, we view a numerical method $\psi _ { \Delta t }$ as a mapping from one time level to another which, via iteration, generates discrete approximations $( \pmb q ^ { n } , \pmb { p } ^ { n } )$ . Any reasonable numerical integrator applied to (4.1) will preserve the symplecticness relation up to a certain error which is proportional to a power of the stepsize $\Delta t$ . We will term a numerical method a symplectic integrator if the symplecticness condition

$$
d \pmb { q } ^ { n + 1 } \wedge d \pmb { p } ^ { n + 1 } = d \pmb { q } ^ { n } \wedge d \pmb { p } ^ { n }
$$

is preserved exactly. The problem now is to derive such symplectic integrators and to enquire in detail about the benefits of using such methods for the simulation of nonlinear systems.

To illustrate, let us walk through the simple one-degree-of-freedom example of the nonlinear oscillator discretized using the Euler-B method

$$
\begin{array} { l } { { q ^ { n + 1 } = q ^ { n } + \Delta t p ^ { n + 1 } , } } \\ { { p ^ { n + 1 } = p ^ { n } - \Delta t \varphi ^ { \prime } ( q ^ { n } ) . } } \end{array}
$$

Taking differentials of both sides of equations (4.4)–(4.5), and using the bilinearity of the wedge product, we have

$$
\begin{array} { c } { { d q ^ { n + 1 } \wedge d p ^ { n + 1 } = d ( q ^ { n } + \Delta t p ^ { n + 1 } ) \wedge d p ^ { n + 1 } } } \\ { { = d q ^ { n } \wedge d p ^ { n + 1 } + \Delta t d p ^ { n + 1 } \wedge d p ^ { n + 1 } . } } \end{array}
$$

Now the wedge product of anything with itself is zero, so we have

$$
\begin{array} { r l } & { d q ^ { n + 1 } \wedge d p ^ { n + 1 } = d q ^ { n } \wedge d p ^ { n + 1 } } \\ & { \qquad = d q ^ { n } \wedge d \big ( p ^ { n } - \Delta t \varphi ^ { \prime } ( q ^ { n } ) \big ) } \\ & { \qquad = d q ^ { n } \wedge d p ^ { n } - \Delta t d q ^ { n } \wedge d \varphi ^ { \prime } ( q ^ { n } ) . } \end{array}
$$

Since $d \varphi ^ { \prime } ( q ^ { n } ) = \varphi ^ { \prime \prime } ( q ^ { n } ) d q ^ { n }$ , the right-hand side reduces to

$$
d q ^ { n } \wedge d p ^ { n } - \Delta t d q ^ { n } \wedge ( \varphi ^ { \prime \prime } ( q ^ { n } ) d q ^ { n } ) = d q ^ { n } \wedge d p ^ { n } ,
$$

and this implies that

$$
d q ^ { n + 1 } \wedge d p ^ { n + 1 } = d q ^ { n } \wedge d p ^ { n } ,
$$

hence $\psi _ { \Delta t }$ is a two-dimensional symplectic map, i.e. an area-preserving map of the plane. In this and later chapters, we will introduce more general classes of symplectic methods for arbitrary Hamiltonian functions and show how their symplecticness enhances their numerical performance.

There are many challenges that might cause this program to fail. First, it is not a priori clear that such symplectic integrators would, in typical cases, be more computable than the flow map itself. Fortunately, as we shall see in this and later chapters, for many types of Hamiltonian systems we can even develop explicit symplectic integrators whose per timestep cost is similar to that of the most popular non-symplectic methods. Another possible problem might arise from the following fact: the symplecticness condition is more general than the condition for having a Hamiltonian flow map. That is, there are symplectic maps that are not the flow map of any Hamiltonian system. Could it be that there are additional structures in a Hamiltonian flow that give rise to important aspects of some interesting physical phenomena or which contribute to the long-term stability of the dynamics? This topic will be visited in Chapter 5.

Before proceeding with the development of symplectic integrators it is natural to ask first if there are other – perhaps more elementary – properties of a Hamiltonian flow whose preservation would improve the outlook for simulation.

In particular, what of the energy integral? Isn’t it reasonable to demand that a numerical integrator for a conservative problem should retain the total energy as a first integral? In fact, it is possible to design such schemes. Unfortunately, these methods often exhibit disappointing numerical properties. They are generally implicit, requiring the solution of nonlinear equations at each timestep. Moreover in typical cases, they do not demonstrate the same level of agreement with the qualitative solution behavior that we observe using simpler and more easily implemented symplectic methods. Nonetheless there are often good reasons to maintain some integrals, such as angular momentum, during numerical simulation and we explain how this can be done.

Another geometric property of Hamiltonian systems arising in typical applications such as the N-body problem is the so-called time-reversal symmetry. We believe that this property can have very important ramifications for the behavior of integrators, in many cases comparable to the effects of preserving symplectic structure. The reversing symmetry is therefore also introduced and discussed in this chapter.

# 4.1 Symplectic maps and methods

The Euler-B method can be applied, in a modified form, to the general Hamiltonian $H ( \pmb { q } , \pmb { p } )$ with $d \geq 1$ degrees of freedom. The equations are

$$
\begin{array} { r } { \pmb { q } ^ { n + 1 } = \pmb { q } ^ { n } + \Delta t \nabla _ { p } H ( \pmb { q } ^ { n } , \pmb { p } ^ { n + 1 } ) , } \\ { \pmb { p } ^ { n + 1 } = \pmb { p } ^ { n } - \Delta t \nabla _ { \pmb { q } } H ( \pmb { q } ^ { n } , \pmb { p } ^ { n + 1 } ) . } \end{array}
$$

By arguments similar to those mentioned in Chapter 2, this method is easily seen to be first-order accurate. Observe that it is not possible, as it was for the nonlinear oscillator, to solve for the variables at one time level in terms of the previous one: the propagation requires in general the solution of a nonlinear system for $p ^ { n + 1 }$ . This method is implicit. For sufficiently small $\Delta t$ , the solution of this system is guaranteed by the implicit function theorem. Let us examine this argument briefly, since it is typical of arguments used to justify the application of implicit methods. Define a function $\boldsymbol { F }$ by

$$
\begin{array} { r } { \pmb { F } ( \pmb { p } ^ { n } , \pmb { q } ^ { n } , \Delta t , \pmb { u } ) = \pmb { u } - \pmb { p } ^ { n } - \Delta t \nabla _ { \pmb { q } } H ( \pmb { q } ^ { n } , \pmb { u } ) . } \end{array}
$$

We assume here that $H$ is twice differentiable, so that $\boldsymbol { F }$ is differentiable in $\pmb { u }$ . Observe that $\pmb { F } ( \pmb { p } ^ { n } , \pmb { q } ^ { n } , 0 , \pmb { p } ^ { n } ) = \pmb { 0 }$ , and that $\begin{array} { r } { \frac { \partial F } { \partial { u } } ( p ^ { n } , \pmb { q } ^ { n } , 0 , \pmb { p } ^ { n } ) = I _ { d } } \end{array}$ is nonsingular. It follows from the implicit function theorem (see BUCK [35]) that we can solve the equation

$$
\begin{array} { r } { F ( p ^ { n } , q ^ { n } , \Delta t , \boldsymbol { u } ) = 0 , } \end{array}
$$

for $\pmb { u }$ in terms of the other arguments of $\boldsymbol { F }$ whenever $\Delta t$ is sufficiently small. Observe that the need to solve these nonlinear equations places a local restriction on the size of the timestep which could, in the event of rapid solution variation, be quite stringent.

Once $p ^ { n + 1 }$ is known, calculation of $\pmb q ^ { n + 1 }$ from (4.6) is then completely explicit.

The corresponding Euler- $A$ method is given by

$$
\begin{array} { r } { \pmb { q } ^ { n + 1 } = \pmb { q } ^ { n } + \Delta t \nabla _ { p } H ( \pmb { q } ^ { n + 1 } , \pmb { p } ^ { n } ) , } \\ { \pmb { p } ^ { n + 1 } = \pmb { p } ^ { n } - \Delta t \nabla _ { \pmb { q } } H ( \pmb { q } ^ { n + 1 } , \pmb { p } ^ { n } ) . } \end{array}
$$

It can be shown that this method is also first-order accurate.

Euler-A and Euler-B methods are canonically symplectic. Let us show this for the Euler-B method using the wedge product notation. Taking differentials of the numerical method yields the implicit system of linear equations

$$
\begin{array} { r } { d pmb { q } ^ { n + 1 } = d \pmb { q } ^ { n } + \Delta t \left[ H _ { p q } d \pmb { q } ^ { n } + H _ { p p } d \pmb { p } ^ { n + 1 } \right] , } \\ { d \pmb { p } ^ { n + 1 } = d \pmb { p } ^ { n } - \Delta t \left[ H _ { q q } d \pmb { q } ^ { n } + H _ { q p } d \pmb { p } ^ { n + 1 } \right] , } \end{array}
$$

which can be thought of as the discrete variational equations associated with (4.6)–(4.7). For notational convenience, we have dropped the arguments in the second-order partial Jacobian matrices $H _ { q q }$ , $H _ { q p } = H _ { p q } ^ { T }$ , $H _ { p p }$ , i.e.

$$
H _ { q q } = \left( \frac { \partial ^ { 2 } { \cal H } } { \partial q _ { i } \partial q _ { j } } \right) , \quad H _ { q p } = \left( \frac { \partial ^ { 2 } { \cal H } } { \partial q _ { i } \partial p _ { j } } \right) , \quad H _ { p p } = \left( \frac { \partial ^ { 2 } { \cal H } } { \partial p _ { i } \partial p _ { j } } \right) .
$$

Observe that

$$
d \pmb { q } ^ { n } \wedge H _ { \pmb { q } \pmb { q } } d \pmb { q } ^ { n } = 0 ,
$$

and

$$
d { p } ^ { n + 1 } \wedge H _ { p p } d { p } ^ { n + 1 } = 0 ,
$$

because $H _ { q q }$ and $H _ { p p }$ are symmetric matrices. If we take the wedge product of (4.10) with $d p ^ { n + 1 }$ from the right, we find

$$
d \pmb { q } ^ { n + 1 } \wedge d \pmb { p } ^ { n + 1 } = d \pmb { q } ^ { n } \wedge d \pmb { p } ^ { n + 1 } + \Delta t H _ { p q } d \pmb { q } ^ { n } \wedge d \pmb { p } ^ { n + 1 } .
$$

Similarly

$$
\begin{array} { r } { d \pmb { q } ^ { n } \wedge d \pmb { p } ^ { n + 1 } = d \pmb { q } ^ { n } \wedge d \pmb { p } ^ { n } - \Delta t d \pmb { q } ^ { n } \wedge H _ { q p } d \pmb { p } ^ { n + 1 } , } \\ { = d \pmb { q } ^ { n } \wedge d \pmb { p } ^ { n } - \Delta t H _ { q p } ^ { T } d \pmb { q } ^ { n } \wedge d \pmb { p } ^ { n + 1 } , } \end{array}
$$

by taking the wedge product of (4.11) with $d \pmb q ^ { n }$ from the left. Upon plugging (4.13) into (4.12), we obtain the desired equality (4.3). A similar proof goes through for the Euler-A method (4.8)–(4.9). Therefore, the general forms of the Euler-A and Euler- $\cdot B$ methods are canonically symplectic. Euler-A and Euler-B are sometimes referred to collectively as the symplectic Euler methods.

We can also find second-order symplectic methods without much difficulty. The implicit midpoint method is defined as follows

$$
\begin{array} { r } { z ^ { n + 1 } = z ^ { n } + { \Delta t } J \nabla H ( z ^ { n + 1 / 2 } ) , \qquad z ^ { n + 1 / 2 } = ( z ^ { n + 1 } + z ^ { n } ) / 2 . } \end{array}
$$

This method is evidently implicit. For implementation purposes, it is useful to write it as a composition of two “half-steps”: an implicit Euler step

$$
z ^ { n + 1 / 2 } = z ^ { n } + \frac { 1 } { 2 } \Delta t J \nabla H ( z ^ { n + 1 / 2 } ) ,
$$

followed by an explicit Euler step

$$
z ^ { n + 1 } = z ^ { n + 1 / 2 } + \frac { 1 } { 2 } \Delta t J \nabla H ( z ^ { n + 1 / 2 } ) .
$$

For implicit midpoint, the equation for $d z ^ { n }$ is equivalent to

$$
d z ^ { n + 1 } = d z ^ { n } + \Delta t J H _ { z z } \frac { d z ^ { n } + d z ^ { n + 1 } } { 2 } .
$$

Taking the wedge product with $J ^ { - 1 } d z ^ { n }$ and $J ^ { - 1 } d z ^ { n + 1 }$ , respectively, from the left, we obtain

$$
\begin{array} { r l } & { J ^ { - 1 } d z ^ { n + 1 } \wedge d z ^ { n } = J ^ { - 1 } d z ^ { n } \wedge d z ^ { n } + \Delta t J ^ { - 1 } J H _ { z z } \frac { d z ^ { n } + d z ^ { n + 1 } } 2 \wedge d z ^ { n } } \\ & { \qquad = J ^ { - 1 } d z ^ { n } \wedge d z ^ { n } + \frac { \Delta t } 2 H _ { z z } d z ^ { n + 1 } \wedge d z ^ { n } , } \end{array}
$$

and

$$
\begin{array} { l } { { J ^ { - 1 } d z ^ { n + 1 } \wedge d z ^ { n + 1 } = J ^ { - 1 } d z ^ { n } \wedge d z ^ { n + 1 } + \Delta t J ^ { - 1 } J H _ { z z } \frac { d z ^ { n } + d z ^ { n + 1 } } 2 \wedge d z ^ { n + 1 } } } \\ { { \qquad = J ^ { - 1 } d z ^ { n + 1 } \wedge d z ^ { n } - \displaystyle \frac { \Delta t } 2 H _ { z z } d z ^ { n + 1 } \wedge d z ^ { n } . } } \end{array}
$$

Here we have made use of Property 3 of the wedge product as stated in Section 3.6 and, in particular, used that

$$
d z ^ { n } \wedge A d z ^ { n } = d z ^ { n + 1 } \wedge A d z ^ { n + 1 } = 0 ,
$$

for any symmetric matrix $\pmb { A } \in \mathbb { R } ^ { 2 d \times 2 d }$ . Summing up, we arrive at the equality

$$
J ^ { - 1 } d z ^ { n + 1 } \wedge d z ^ { n + 1 } = J ^ { - 1 } d z ^ { n } \wedge d z ^ { n } ,
$$

implying symplecticness of the scheme with respect to the structure matrix J. Observe that this argument required at no point that $\jmath$ be the canonical structure matrix, only that it be constant, skew-symmetric, and invertible, thus we have shown: the implicit midpoint method preserves any constant symplectic structure.

# 4.2 Construction of symplectic methods by Hamiltonian splitting

In the above discussion, we have shown that several integrators are symplectic when applied to integrate Hamiltonian systems. In this section, we show that there is a simple technique that can often be used to produce good symplectic methods.

Suppose that we can split the Hamiltonian $H$ into the sum of $k \ \geq \ 2$ Hamiltonians $H _ { j }$ , $i = 1 , \dots , k$ , i.e.

$$
H ( z ) = \sum _ { i = 1 } ^ { k } { H _ { i } ( z ) } ,
$$

with each Hamiltonian vector field

$$
\frac { d } { d t } z = J \nabla _ { z } H _ { i } ( z )
$$

explicitly solvable. A symplectic integrator is then derived as an appropriate composition of the corresponding flow maps. Since each flow map is obviously symplectic and any composition of symplectic maps yields a symplectic map, the resulting numerical method is symplectic. See problem 2 in the Exercises.

As a simple example, consider a nonlinear oscillator $\begin{array} { r } { H ( q , p ) = \frac 1 2 p ^ { 2 } + \varphi ( q ) } \end{array}$ . The energy can be decomposed into kinetic and potential terms

$$
H = H _ { 1 } + H _ { 2 } , H _ { 1 } = \frac { 1 } { 2 } p ^ { 2 } , H _ { 2 } = \varphi ( q ) .
$$

Now each term is exactly integrable. The equations of motion for $H _ { 1 }$ are

$$
\begin{array} { r } { \dot { q } = p , } \\ { \dot { p } = 0 , } \end{array}
$$

which has the flow map

$$
\begin{array} { r } { \pmb { \phi } _ { t , H _ { 1 } } \left( \left[ \begin{array} { c } { q } \\ { p } \end{array} \right] \right) = \left[ \begin{array} { c } { q + t p } \\ { p } \end{array} \right] . } \end{array}
$$

Similarly, $H _ { 2 }$ has flow map

$$
\pmb { \phi } _ { t , H _ { 2 } } \left( \left[ \begin{array} { c } { { q } } \\ { { p } } \end{array} \right] \right) = \left[ \begin{array} { c } { { q } } \\ { { p - t \varphi ^ { \prime } ( q ) } } \end{array} \right] .
$$

Each of these maps is symplectic (each is the flow map of a Hamiltonian system), hence the map defined by

$$
\pmb { \psi } _ { \Delta t } : = \pmb { \phi } _ { \Delta t , H _ { 1 } } \circ \pmb { \phi } _ { \Delta t , H _ { 2 } }
$$

is also symplectic.

We still need to show that such a composition method approximates the flow map with at least first order.

FIRST-ORDER SPLITTING

If $H = H _ { 1 } + H _ { 2 } + . . . + H _ { k }$ is any splitting into twice differentiable terms, then the composition method

$$
\pmb { \psi } _ { \Delta t } = \pmb { \phi } _ { \Delta t , H _ { 1 } } \circ \pmb { \phi } _ { \Delta t , H _ { 2 } } \circ \cdot \cdot \cdot \circ \pmb { \phi } _ { \Delta t , H _ { k } }
$$

is (at least) a first-order symplectic integrator.

Let us walk through a proof for the case $k = 2$ . In Chapter 5 a more detailed result will be given. We wish to compare the flow map $\pmb { \phi } _ { \Delta t , H }$ with $\psi _ { \Delta t }$ . It is enough to compare the images of an arbitrary point $z ^ { 0 }$ under the two maps. Using a Taylor series expansion in powers of $\Delta t$ and the definition of the flow map, it is easy to show that

$$
\begin{array} { r l } & { \pmb { \phi } _ { \Delta t , H } ( z ^ { 0 } ) = z ^ { 0 } + \Delta t \dot { z } ( 0 ) + \mathcal { O } ( \Delta t ^ { 2 } ) } \\ & { \qquad = z ^ { 0 } + \Delta t J \nabla H ( z ^ { 0 } ) + \mathcal { O } ( \Delta t ^ { 2 } ) . } \end{array}
$$

We can argue in a similar way that

$$
\phi _ { \Delta t , H _ { i } } ( z ^ { 0 } ) = z ^ { 0 } + \Delta t J \nabla H _ { i } ( z ^ { 0 } ) + \mathcal { O } ( \Delta t ^ { 2 } ) ,
$$

$j = 1 , 2$ . And then, performing similar expansions in $\Delta t$ , we arrive at

$$
\begin{array} { r l } & { \psi _ { \Delta t } ( z ^ { 0 } ) = \phi _ { \Delta t , H _ { 1 } } \left( \Phi _ { \Delta t , H _ { 2 } } ( z ^ { 0 } ) \right) } \\ & { \qquad = \phi _ { \Delta t , H _ { 2 } } ( z ^ { 0 } ) + \Delta t J \nabla H _ { 1 } \left( \phi _ { \Delta t , H _ { 2 } } ( z ^ { 0 } ) \right) + \mathcal { O } ( \Delta t ^ { 2 } ) } \\ & { \qquad = z ^ { 0 } + \Delta t J \nabla H _ { 2 } ( z ^ { 0 } ) + \Delta t J \nabla H _ { 1 } ( z ^ { 0 } ) + \mathcal { O } ( \Delta t ^ { 2 } ) } \\ & { \qquad = z ^ { 0 } + \Delta t J \nabla H ( z ^ { 0 } ) + \mathcal { O } ( \Delta t ^ { 2 } ) } \\ & { \qquad = \phi _ { \Delta t , H } ( z ^ { 0 } ) + \mathcal { O } ( \Delta t ^ { 2 } ) . } \end{array}
$$

This estimate of the local error, together with the evident smoothness of the flow map, proves that the composition method is at least first order.

The only apparent drawback of this approach is that it requires the splitting of the given Hamiltonian into explicitly solvable subproblems. This may not always be possible or desirable. In many cases, the system may admit a partitioning, but without the individual terms being exactly integrable. In these cases, one may be able to construct effective schemes by substituting another symplectic integrator for the $\mathsf { e x a c t }$ flow map at some stage. The splitting technique may in this way simplify the development of an effective method by breaking down a complicated problem into a series of lesser challenges.

A curious special case arises when $H _ { 1 }$ and $H _ { 2 }$ are first integrals of each other, i.e., $\{ H _ { 1 } , H _ { 2 } \}$ . Then the two flow maps commute (see problem 4 in the Exercises) and the composition method is exact

$$
\Phi _ { \Delta t , H _ { 1 } + H _ { 2 } } = \pmb { \phi } _ { \Delta t , H _ { 1 } } \circ \pmb { \phi } _ { \Delta t , H _ { 2 } } = \pmb { \phi } _ { \Delta t , H _ { 1 } } \circ \pmb { \phi } _ { \Delta t , H _ { 2 } } .
$$

# 4.2.1 Separable Hamiltonian systems

The splitting described earlier for the special case of the oscillator is applicable to any separable Hamiltonian of the form

$$
H ( \pmb { q } , \pmb { p } ) = T ( \pmb { p } ) + V ( \pmb { q } ) .
$$

As we have seen in earlier chapters, such systems are ubiquitous in chemical and physical modeling, being the standard form for $N .$ -body simulations with a flat (i.e. Euclidean) kinetic energy metric.

As before, the form of the energy function suggests a natural splitting into kinetic energy

$$
H _ { 1 } ( \pmb { p } ) = T ( \pmb { p } ) ,
$$

and potential energy

$$
H _ { 2 } ( \pmb q ) : = V ( \pmb q ) .
$$

The differential equations corresponding to $H _ { 2 }$ can be written

$$
\begin{array} { l } { { \displaystyle { \frac { d } { d t } } { \pmb q } = { \bf 0 } } , } \\ { { \displaystyle { \frac { d } { d t } } { \pmb p } = - \nabla _ { { \pmb q } } V ( { \pmb q } ) . } } \end{array}
$$

These equations are completely integrable, since $\pmb q$ is constant along solutions and $p$ therefore varies linearly with time. The flow map is

$$
\Phi _ { \tau , V } (  { \boldsymbol { q } } ,  { \boldsymbol { p } } ) = \left[ \begin{array} { c } {  { \boldsymbol { q } } } \\ {  { \boldsymbol { p } } - \tau \nabla _ { \ b { q } } V (  { \boldsymbol { q } } ) } \end{array} \right] .
$$

Similarly, we can derive the flow map for the kinetic term $\left( H _ { 1 } \right)$

$$
\pmb { \phi } _ { \tau , T } ( \pmb q , \pmb { p } ) = \left[ \pmb { q } + \tau \nabla _ { \pmb { p } } T ( \pmb { p } ) \right] .
$$

Now consider the composition of these two maps for $\tau = \Delta t$

$$
\pmb { \psi } _ { \Delta t } : = \pmb { \phi } _ { \Delta t , T } \circ \pmb { \phi } _ { \Delta t , V } .
$$

Applying this map to a point of phase space $( \pmb q ^ { n } , \pmb { p } ^ { n } )$ , we first compute a point $( { \bar { q } } , { \bar { p } } )$

$$
\begin{array} { l } { { \bar { \pmb q } = \pmb q ^ { n } , } } \\ { { \bar { \pmb p } = \pmb p ^ { n } - \Delta t \nabla _ { \pmb q } V ( \pmb q ^ { n } ) . } } \end{array}
$$

Next, apply $\pmb { \phi } _ { \Delta t , T }$ to this point, i.e.

$$
\begin{array} { r l } & { \pmb q ^ { n + 1 } = \pmb { \bar { q } } + \Delta t \nabla _ { p } T ( \pmb { \bar { p } } ) , } \\ & { \pmb { p } ^ { n + 1 } = \pmb { \bar { p } } . } \end{array}
$$

These equations can be simplified by the elimination of the intermediate values, to yield

$$
\begin{array} { l } { { { \pmb q } ^ { n + 1 } = { \pmb q } ^ { n } + \Delta t \nabla _ { p } T ( { \pmb p } ^ { n + 1 } ) , } } \\ { { { \pmb p } ^ { n + 1 } = { \pmb p } ^ { n } - \Delta t \nabla _ { { \pmb q } } V ( { \pmb q } ^ { n } ) . } } \end{array}
$$

This is evidently the Euler-B method introduced in the previous section specialized to the case of a mechanical Hamiltonian. While the Euler-B method is normally implicit, it becomes explicit when applied to this special class of Hamiltonians due to the separation of variable dependencies.

By reversing the order in which the two maps are applied, we obtain another composition method, $\pmb { \phi } _ { \Delta t , V } \circ \pmb { \phi } _ { \Delta t , T }$ , which reduces after a similar calculation to the Euler-A method.

An interesting point that should be mentioned is that not all symplectic maps are given by a splitting. For the general Hamiltonian, it is clear that the Euler-A and Euler-B methods are not obtained from any splitting. It is only for the special case of a separable Hamiltonian that these methods can be viewed in this special way.

# 4.2.2 A second-order splitting method

Higher-order splitting methods are also easily constructed. We will take up this theme in more detail in Chapter 6. For now, as an illustration, consider again the mechanical Hamiltonian and the splitting

$$
H = H _ { 1 } + H _ { 2 } + H _ { 3 } ,
$$

with

$$
H _ { 1 } = \frac { 1 } { 2 } V ( \pmb { q } ) , \qquad H _ { 2 } = T ( \pmb { p } ) , \qquad H _ { 3 } = \frac { 1 } { 2 } V ( \pmb { q } ) .
$$

The associated composition method is equivalent to

$$
\pmb { \psi } _ { \Delta t } = \pmb { \phi } _ { \Delta t / 2 , V } \circ \pmb { \phi } _ { \Delta t , T } \circ \pmb { \phi } _ { \Delta t / 2 , V } .
$$

After simplification, it becomes clear that this integrator is nothing other than the second-order St¨ormer–Verlet method (2.16)–(2.18) of Chapter 2 written in terms of the canonical coordinates

$$
\begin{array} { c } { { p ^ { n + 1 / 2 } = p ^ { n } - \displaystyle \frac { 1 } { 2 } \Delta t \nabla _ { q } V ( q ^ { n } ) , } } \\ { { q ^ { n + 1 } = q ^ { n } + \Delta t \nabla _ { p } T ( p ^ { n + 1 / 2 } ) , } } \\ { { p ^ { n + 1 } = p ^ { n + 1 / 2 } - \displaystyle \frac { 1 } { 2 } \Delta t \nabla _ { q } V ( q ^ { n + 1 } ) . } } \end{array}
$$

Since it is a splitting method we may infer: the St¨ormer–Verlet method (4.14)– (4.16) is canonically symplectic.

Just as the implicit midpoint method turned out to be the composition of implicit and explicit Euler steps, notice that the St¨ormer–Verlet method can be

expressed as a composition of half-steps using the Euler-A and Euler-B methods, i.e.

$$
\begin{array} { r } { \phi _ { \triangle t , \frac { 1 } { 2 } V } \circ \phi _ { \triangle t , T } \circ \phi _ { \triangle t , \frac { 1 } { 2 } V } = \phi _ { \triangle t , \frac { 1 } { 2 } V } \circ \phi _ { \triangle t , \frac { 1 } { 2 } T } \circ \phi _ { \triangle t , \frac { 1 } { 2 } T } \circ \phi _ { \triangle t , \frac { 1 } { 2 } T } \circ \phi _ { \triangle t , \frac { 1 } { 2 } V } } \\ { = \phi _ { \frac { 1 } { 2 } \triangle t , V } \circ \phi _ { \frac { 1 } { 2 } \triangle t , T } \circ \phi _ { \frac { 1 } { 2 } \triangle t , T } \circ \phi _ { \frac { 1 } { 2 } \triangle t , V } . } \end{array}
$$

# 4.3 Time-reversal symmetry and reversible discretizations

An important geometric property of Newton’s equations of motion is related to the invariance of a Hamiltonian $H = H ( \pmb { q } , \pmb { p } )$ under the reflection symmetry

$$
p \mapsto - p ,
$$

i.e. the Hamiltonian is an even function in the momentum $\pmb { p }$ . We consider the consequences of this property for the solution behavior of the corresponding Hamiltonian system

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } \pmb { q } = \nabla _ { p } H ( \pmb { q } , \pmb { p } ) , } \\ { \displaystyle \frac { d } { d t } \pmb { p } = - \nabla _ { \pmb { q } } H ( \pmb { q } , \pmb { p } ) . } \end{array}
$$

The key fact is this: if $( \pmb q ( t ) , \pmb p ( t ) )$ is a solution then also $( \pmb { \hat { q } } ( t ) , \pmb { \hat { p } } ( t ) ) : = ( \pmb { q } ( - t )$ , $- { \pmb p } ( - t ) )$ is.

To prove this observe that

$$
\frac { d } { d t } \hat { \pmb { q } } ( t ) = - \pmb { \dot { q } } ( - t ) = - \nabla _ { p } H ( \pmb { q } ( - t ) , \pmb { p } ( - t ) ) = \nabla _ { p } H ( \hat { \pmb { q } } ( t ) , \hat { \pmb { p } } ( t ) ) ,
$$

and

$$
\frac { d } { d t } \pmb { \hat { p } } ( t ) = \pmb { \dot { p } } ( - t ) = - \nabla _ { \ b { q } } H ( \pmb { q } ( - t ) , \pmb { p } ( - t ) ) = - \nabla _ { \ b { q } } H ( \pmb { \hat { q } } ( t ) , \pmb { \hat { p } } ( t ) ) .
$$

Here we used the general fact that if $h ( x , y )$ is an even function of $y$ , then $h _ { x }$ is also even in $y$ , and $h _ { y }$ is odd in $y$ , meaning that $h _ { x } ( x , - y ) = h _ { x } ( x , y )$ , and $h _ { y } ( x , - y ) = - h _ { y } ( x , y )$ .

The invariance of the Hamiltonian with respect to $p \mapsto - p$ evidently implies that for every solution of the Hamiltonian system, there is another solution which traverses the same positional curve but in the opposite direction, with a negated momentum.

Another way of saying this is that if we evolve the solution $\tau$ units in time forward from a given point $z ^ { 0 } = ( q ^ { 0 } , p ^ { 0 } )$ , then negate the momentum, evolve the solution $\tau$ units further, then negate the momentum again, we end up back at our starting point $z ^ { 0 }$ . A system that has this property is said to be time reversible.

![](images/7d408721a541001695a89e2174930ff9b819f779b3827438020977fb1802de4c.jpg)  
Figure 4.2 The time-reversal symmetry in a one-degree-of-freedom system. A point $z ^ { 0 }$ of the phase plane is mapped $\tau$ units forward along the trajectory, reflected about the line $p = 0$ , again evolved forward in time $\tau$ units, and, finally, reflected again about the $p$ -axis, arriving back at the initial point $z ^ { 0 }$ .

In the planar case (one-degree-of-freedom case), time reversibility implies that the phase portrait is symmetric with respect to the line $p = 0$ , with directionality of trajectories reversed about this axis (Fig. 4.2).

# 4.3.1 Time-reversible maps

Let us develop the concept of time-reversible systems in a somewhat more general setting. Upon introducing the matrix

$$
{ \pmb S } = \left[ \begin{array} { c c } { + { \pmb I } _ { d } } & { \ { \pmb 0 } } \\ { { \pmb 0 } } & { - { \pmb I } _ { d } } \end{array} \right] ,
$$

the time-reversal symmetry can be rewritten as

$$
H ( z ) = H ( \pmb { S } z ) , \qquad z = ( \pmb { q } , \pmb { p } ) ^ { T } .
$$

This property of a Hamiltonian $H$ implies an associated transformation property for the vector field

$$
\begin{array} { r l } { \nabla _ { z } H ( z ) = \nabla _ { z } H ( \pmb { S } z ) } \\ { = \pmb { S } ^ { T } \nabla _ { \hat { z } } H ( \pmb { S } z ) , } \end{array}
$$

$\hat { z } = S z$ , implying

$$
\begin{array} { r } { J \nabla _ { z } H ( z ) = J S ^ { T } \nabla _ { \hat { z } } H ( S z ) } \\ { = - S J \nabla _ { \hat { z } } H ( S z ) , } \end{array}
$$

or, with $\dot { z } = f ( z ) = J \nabla _ { z } H ( z )$ ,

$$
\pmb { f } ( z ) = - \pmb { S } \pmb { f } ( \pmb { S } z ) .
$$

We call a differential equation with this property time reversible with respect to the involution $s$ .1

Now solving ${ d z } / { d t } = - S f ( S z )$ is precisely equivalent to applying the combination of a coordinate transformation $z  S z$ with a time transformation $d t / d \tau = - 1$ to the differential equation $d z / d t = { \pmb f } ( z )$ . In other words, applying the symmetry and simultaneously negating time does not effect the system. The flow map therefore satisfies

$$
\pmb { \phi } _ { \tau , H } ( z ) = \pmb { S } \pmb { \phi } _ { - \tau , H } ( \pmb { S } z ) .
$$

Let $[ \pmb { \phi } _ { \tau , H } ] ^ { - 1 }$ denote the inverse of the mapping $\pmb { \phi } _ { \tau , H }$ . Then we know that $\pmb { \phi } _ { - \tau , H } = [ \pmb { \phi } _ { \tau , H } ] ^ { - 1 }$ for any flow map, we therefore obtain

$$
{ } \pmb { \phi } _ { \tau , H } ( z ) = \pmb { S } \left[ \pmb { \phi } _ { \tau , H } \right] ^ { - 1 } ( \pmb { S } z ) .
$$

We call any invertible mapping $\pmb { \psi }$ that satisfies

$$
\pmb { \psi } ( z ) = \pmb { S } \pmb { \psi } ^ { - 1 } ( \pmb { S } z )
$$

time reversible under the involution $s$ .

# 4.3.2 Linear-reversible maps

Now let us discuss the case where the underlying map is a linear function. We say that

$$
\pmb { \psi } ( z ) = P z
$$

is time reversible if the matrix $P$ satisfies the identity

$$
P = S P ^ { - 1 } S .
$$

Since $S = S ^ { - 1 }$ , the matrix $P ^ { - 1 }$ is a similarity transformation of $P$ ; i.e. $P$ and $P ^ { - 1 }$ have identical eigenvalues. Thus, as for symplectic matrices, real matrices satisfying time-reversal symmetry have an eigenvalue $\lambda$ if and only if also $1 / \lambda$ , $\bar { \lambda }$ , and $1 / \bar { \lambda }$ lie in the spectrum.

$^ 1 \mathsf { A }$ matrix $S \in \mathbb { R } ^ { d \times d }$ is called an involution if $S S = I _ { d }$

# 4.3.3 Time-reversible methods by symmetric composition

The method $\psi _ { \Delta { t } } ^ { * }$ defined by

$$
\pmb { { \psi } } _ { \Delta t } ^ { * } = \left[ \pmb { { \psi } } _ { - \Delta t } \right] ^ { - 1 }
$$

is called the adjoint method of $\psi _ { \Delta t }$ . In other words, given a method $\psi _ { \Delta t }$ its adjoint method $\psi _ { \Delta { t } } ^ { * }$ is (implicitly) defined by

$$
z ^ { n } = \pmb { \psi } _ { - \Delta t } ( z ^ { n + 1 } ) ,
$$

and

$$
\begin{array} { r } { \pmb { \psi } _ { \Delta t } ^ { * } ( z ^ { n } ) : = z ^ { n + 1 } . } \end{array}
$$

From this definition we readily obtain that the adjoint of the adjoint method is the original method, i.e. $\psi _ { \Delta { t } } = [ \psi _ { \Delta { t } } ^ { * } ] ^ { * }$ . It is also readily verified that the local error of $\psi _ { \Delta t }$ and its adjoint method are of the same order with respect to the stepsize $\Delta t$ . A method $\psi _ { \Delta t }$ is called symmetric if $\pmb { \psi } _ { \Delta t } = \pmb { \psi } _ { \Delta t } ^ { * }$ , i.e., ${ \pmb { \psi } } _ { - \Delta t } = { \pmb { \psi } } _ { \Delta t } ^ { - 1 }$

As an illustration, the explicit Euler method

$$
z ^ { n + 1 } = z ^ { n } + \Delta t J \nabla _ { z } H ( z ^ { n } ) ,
$$

is not symmetric. The inverse $[ { \pmb { \psi } } _ { \Delta t } ] ^ { - 1 }$ is obtained by exchanging $z ^ { n }$ and $z ^ { n + 1 }$ , i.e.

$$
z ^ { n } = z ^ { n + 1 } + \Delta t J \nabla _ { z } H ( z ^ { n + 1 } ) .
$$

Upon replacing $\Delta t$ by $- \Delta t$ and rearranging terms, we get the implicit Euler method

$$
z ^ { n + 1 } = z ^ { n } + \Delta t J \nabla _ { z } H ( z ^ { n + 1 } ) .
$$

Thus the implicit Euler method is the adjoint of the explicit Euler method and vice versa. The symplectic Euler-B method

$$
\begin{array} { r l } & { \pmb { q } ^ { n + 1 } = \pmb { q } ^ { n } + \Delta t \nabla _ { p } H ( \pmb { q } ^ { n } , \pmb { p } ^ { n + 1 } ) , } \\ & { \pmb { p } ^ { n + 1 } = \pmb { p } ^ { n } - \Delta t \nabla _ { \pmb { q } } H ( \pmb { q } ^ { n } , \pmb { p } ^ { n + 1 } ) } \end{array}
$$

is also not symmetric. Its adjoint is the symplectic Euler-A method

$$
\begin{array} { r } { \pmb { q } ^ { n + 1 } = \pmb { q } ^ { n } + \Delta t \nabla _ { p } H ( \pmb { q } ^ { n + 1 } , \pmb { p } ^ { n } ) , } \\ { \pmb { p } ^ { n + 1 } = \pmb { p } ^ { n } - \Delta t \nabla _ { \pmb { q } } H ( \pmb { q } ^ { n + 1 } , \pmb { p } ^ { n } ) . } \end{array}
$$

Knowing a numerical method $\psi _ { \Delta t }$ and its adjoint method, a symmetric method $\hat { \pmb { { \psi } } } _ { \Delta t }$ is immediately available through the following concatenation (composition) of the two methods

$$
\hat { \pmb { \psi } } _ { \Delta t } : = \pmb { \psi } _ { \Delta t / 2 } ^ { * } \circ \pmb { \psi } _ { \Delta t / 2 } .
$$

Let us verify this statement

$$
\begin{array} { r l } & { \hat { \psi } _ { - \Delta t } = { \pmb { \psi } } _ { - \Delta t / 2 } ^ { * } \circ { \pmb { \psi } } _ { - \Delta t / 2 } } \\ & { \qquad = \left[ { \pmb { \psi } } _ { \Delta t / 2 } \right] ^ { - 1 } \circ \left[ { \pmb { \psi } } _ { \Delta t / 2 } ^ { * } \right] ^ { - 1 } } \\ & { \qquad = \left[ { \pmb { \psi } } _ { \Delta t / 2 } ^ { * } \circ { \pmb { \psi } } _ { \Delta t / 2 } \right] ^ { - 1 } } \\ & { \qquad = \left[ \hat { \pmb { \psi } } _ { \Delta t } \right] ^ { - 1 } . } \end{array}
$$

Take the implicit Euler method as $\psi _ { \Delta t }$ . Then $\hat { \pmb { { \psi } } } _ { \Delta t }$ is the concatenation of the implicit with the $\mathsf { e x }$ plicit Euler method, i.e.

$$
\begin{array} { l } { { z ^ { n + 1 / 2 } = z ^ { n } + \displaystyle \frac { \Delta t } { 2 } J \nabla _ { z } H ( z ^ { n + 1 / 2 } ) , } } \\ { { z ^ { n + 1 } = z ^ { n + 1 / 2 } + \displaystyle \frac { \Delta t } { 2 } J \nabla _ { z } H ( z ^ { n + 1 / 2 } ) , } } \end{array}
$$

which, since

$$
z ^ { n + 1 / 2 } = \frac { z ^ { n } + z ^ { n + 1 } } { 2 } ,
$$

is equivalent to the implicit midpoint method. Choosing $\psi _ { \Delta t }$ to be the map corresponding to the explicit Euler method, we obtain the trapezoidal rule for $\hat { \pmb { { \psi } } } _ { \Delta t }$ .

Similarly, concatenation of half steps with the Euler-B method with the Euler-A method yields the series of steps

$$
\begin{array} { c } { { q ^ { n + 1 / 2 } = q ^ { n } + \displaystyle \frac { 1 } { 2 } \Delta t \nabla _ { p } H ( q ^ { n } , p ^ { n + 1 / 2 } ) , } } \\ { { \displaystyle p ^ { n + 1 / 2 } = p ^ { n } - \displaystyle \frac { 1 } { 2 } \Delta t \nabla _ { q } H ( q ^ { n } , p ^ { n + 1 / 2 } ) , \ ~ } } \\ { { \displaystyle q ^ { n + 1 } = q ^ { n + 1 / 2 } + \displaystyle \frac { 1 } { 2 } \Delta t \nabla _ { p } H ( q ^ { n + 1 } , p ^ { n + 1 / 2 } ) , \ ~ } } \\ { { \displaystyle p ^ { n + 1 } = p ^ { n } - \displaystyle \frac { 1 } { 2 } \Delta t \nabla _ { q } H ( q ^ { n + 1 } , p ^ { n + 1 / 2 } ) . \ ~ } } \end{array}
$$

After elimination of redundancy, we arrive at the generalized St¨ormer–Verlet/leapfrog method

$$
\begin{array} { c } { { \pmb q ^ { n + 1 } = \pmb q ^ { n } + \displaystyle \frac { 1 } { 2 } \Delta t ( \nabla _ { p } H ( \pmb q ^ { n } , \pmb p ^ { n + 1 / 2 } ) + \nabla _ { p } H ( \pmb q ^ { n + 1 } , \pmb p ^ { n + 1 / 2 } ) ) , } } \\ { { \pmb p ^ { n + 1 / 2 } = \pmb p ^ { n } - \displaystyle \frac { 1 } { 2 } \Delta t \nabla _ { q } H ( \pmb q ^ { n } , \pmb p ^ { n + 1 / 2 } ) , } } \\ { { \pmb p ^ { n + 1 } = \pmb p ^ { n } - \displaystyle \frac { 1 } { 2 } \Delta t \nabla _ { q } H ( \pmb q ^ { n + 1 } , \pmb p ^ { n + 1 / 2 } ) . } } \end{array}
$$

This is an implicit second-order symplectic method which specializes to the St¨ormer–Verlet method in the case of N-body systems.

It is worthwhile to note that, in both of the above examples, the concatenation of non-symmetric first-order methods yields a symmetric method of second order. More generally, one can prove the following:

Theorem 1 The order of a symmetric method is necessarily even.

Proof. Suppose by way of contradiction that the order of a given symmetric method is odd, so that the leading-order term in the local error expansion is even. We have

$$
\pmb { \psi } _ { \Delta t } ( z ) = \pmb { \phi } _ { \Delta t } ( z ) + \pmb { C } _ { 2 k } ( z ) \Delta t ^ { 2 k } + \pmb { \mathcal { O } } ( \Delta t ^ { 2 k + 1 } ) ,
$$

and

$$
\begin{array} { r } { \pmb { \psi } _ { - \Delta t } ( z ) = \pmb { \phi } _ { - \Delta t } ( z ) + \pmb { C } _ { 2 k } ( z ) \Delta t ^ { 2 k } + \pmb { \mathcal { O } } ( \Delta t ^ { 2 k + 1 } ) . } \end{array}
$$

Because of $\pmb { \psi } _ { \Delta t } ( z ) = z + \mathcal { O } ( \Delta t )$ and a similar property of $\pmb { \phi } _ { \Delta t }$ , the above two expansions immediately lead to

$$
\begin{array} { r } { \phi _ { - \Delta t } \circ \pmb { \psi } _ { \Delta t } \left( z \right) = z + \pmb { C } _ { 2 k } ( z ) \Delta t ^ { 2 k } + \pmb { \mathcal { O } } ( \Delta t ^ { 2 k + 1 } ) , } \end{array}
$$

and

$$
\begin{array} { r } { \pmb { \psi } _ { - \Delta t } \circ \pmb { \phi } _ { \Delta t } \left( z \right) = z + \pmb { C } _ { 2 k } ( z ) \Delta t ^ { 2 k } + \pmb { \mathcal { O } } ( \Delta t ^ { 2 k + 1 } ) . } \end{array}
$$

We can easily show the following: a smooth map $\boldsymbol { F }$ defined by

$$
\pmb { F } ( z ) = z + \epsilon \pmb { G } ( z )
$$

is invertible for sufficiently small $\epsilon$ , and

$$
F ^ { - 1 } ( z ) = z - \epsilon G ( z ) + O ( \epsilon ^ { 2 } ) .
$$

Applying this with $\pmb { F } = \pmb { \psi } _ { - \Delta t } \circ \pmb { \phi } _ { \Delta t }$ , $G ( z ) = C _ { 2 k } ( z )$ and $\epsilon = \Delta t ^ { 2 k }$ , we find

$$
\phi _ { \Delta t } ^ { - 1 } \circ \pmb { \psi } _ { - \Delta t } ^ { - 1 } \left( z \right) = z - C _ { 2 k } ( z ) \Delta t ^ { 2 k } + \mathcal { O } ( \Delta t ^ { 2 k + 1 } ) .
$$

On the other hand, since $\pmb { \phi } _ { \Delta t }$ is self-adjoint and we have assumed the same property for $\psi _ { \Delta t }$ , it follows that

$$
\begin{array} { r } { \phi _ { - \Delta t } \circ \pmb { \psi } _ { \Delta t } \left( z \right) = z - C _ { 2 k } ( z ) \Delta t ^ { 2 k } + \mathcal { O } ( \Delta t ^ { 2 k + 1 } ) . } \end{array}
$$

Comparing this formula with (4.19) we conclude that $C _ { 2 k } = \bf 0$ , contradicting our assumption that the leading term in the local error was of even order. ✷

Given a time-reversible Hamiltonian system or a general differential equation

$$
\frac { d } { d t } z = \pmb { f } ( z ) ,
$$

satisfying (4.17), then a numerical method is called time reversible if

$$
\pmb { \psi } _ { \Delta t } ( z ^ { n } ) = \pmb { S } \pmb { \psi } _ { \Delta t } ^ { - 1 } ( \pmb { S } z ^ { n } ) .
$$

This definition is in accordance with (4.18). Provided the numerical method is symmetric this definition is equivalent to

$$
\pmb { \psi } _ { \Delta t } ( z ^ { n } ) = \pmb { S } \pmb { \psi } _ { - \Delta t } ( \pmb { S } z ^ { n } ) .
$$

However this equality is satisfied by all numerical methods we have encountered so far when applied to a differential equation satisfying (4.17). Hence we can conclude that symmetric methods are time-reversible. See problem 11 in the Exercises.

# 4.4 First integrals

First integrals play an important role in Hamiltonian mechanics [149, 124]. We have already seen several instances of first integrals in Chapter 3 and noted that first integrals lead essentially to a reduction in the number of degrees of freedom. Can this property be reproduced by a numerical method? The answer is no in general if one looks at the class of symplectic integration methods. However, there are a number of important exceptions and we will discuss the most important ones in the following two subsections.

# 4.4.1 Preservation of first integrals by splitting methods

Splitting methods can sometimes be shown to exactly conserve certain first integrals. We begin by considering the important example of an $N .$ -body system with pairwise distance-dependent interactions

$$
H = \sum _ { i = 1 } ^ { N } \frac { \lVert \pmb { p } _ { i } \rVert ^ { 2 } } { 2 m _ { i } } + \sum _ { i = 1 } ^ { N - 1 } \sum _ { j = i + 1 } ^ { N } \varphi _ { i j } ( \lVert \pmb { q } _ { i } - \pmb { q } _ { j } \rVert ) .
$$

Such a system is in the form $H ( \pmb { q } , \pmb { p } ) = T ( \pmb { p } ) + V ( \pmb { q } )$ , hence the splitting technique discussed in Section 4.2.1 is directly applicable. In particular the St¨ormer–Verlet method provides an elementary time-reversible and symplectic discretization for this problem.

On the other hand, as shown in Chapter 3, (4.20) has other properties and it is interesting to ask if these are also conserved under discretization. Specifically, both the total linear momentum $\begin{array} { r } { p _ { \mathrm { t o t } } = \sum _ { j = 1 } ^ { N } p _ { j } } \end{array}$ and the total angular momentum $\begin{array} { r } { \pmb { m } _ { \mathrm { t o t } } = \sum _ { j = 1 } ^ { N } \pmb { q } _ { j } \times \pmb { p } _ { j } } \end{array}$ j=1  are conserved by the flow. Let $p _ { \mathrm { t o t } } ^ { n }$ and $m _ { \mathrm { t o t } } ^ { n }$ represent the discrete forms of the linear and angular momenta; it is desirable that these be preserved under iteration, i.e. that

$$
\pmb { p } _ { \mathrm { t o t } } ^ { n + 1 } = \pmb { p } _ { \mathrm { t o t } } ^ { n } , \quad \pmb { m } _ { \mathrm { t o t } } ^ { n + 1 } = \pmb { m } _ { \mathrm { t o t } } ^ { n } .
$$

To examine these directly, we can begin by writing out the discrete equations for each particle

$$
\begin{array} { c } { { q _ { j } ^ { n + 1 } = q _ { j } ^ { n } + \displaystyle \frac { 1 } { m _ { j } } p _ { j } ^ { n + 1 / 2 } , } } \\ { { p _ { j } ^ { n + 1 / 2 } = p _ { j } ^ { n } + \displaystyle \sum _ { i \neq j } \displaystyle \frac { \varphi _ { i j } ^ { \prime } ( r _ { i j } ^ { n } ) } { r _ { i j } ^ { n } } ( q _ { j } ^ { n } - q _ { i } ^ { n } ) , } } \\ { { p _ { j } ^ { n + 1 } = p _ { j } ^ { n + 1 / 2 } + \displaystyle \sum _ { i \neq j } \displaystyle \frac { \varphi _ { i j } ^ { \prime } ( r _ { i j } ^ { n + 1 } ) } { r _ { i j } ^ { n + 1 } } ( q _ { j } ^ { n + 1 } - q _ { i } ^ { n + 1 } ) . } } \end{array}
$$

Now the angular momentum can be computed directly as follows

$$
\begin{array} { l } { { \displaystyle m _ { \mathrm { t o t } } ^ { n + 1 } = \sum _ { j = 1 } ^ { N } q _ { j } ^ { n + 1 } \times p _ { j } ^ { n + 1 } } } \\ { { \displaystyle \quad \quad = \sum _ { j = 1 } ^ { N } q _ { j } ^ { n + 1 } \times ( p _ { j } ^ { n + 1 / 2 } + \sum _ { i \neq j } \frac { \varphi _ { i j } ^ { \prime } ( r _ { i j } ^ { n + 1 } ) } { r _ { i j } ^ { n + 1 } } ( q _ { j } ^ { n + 1 } - q _ { i } ^ { n + 1 } ) ) } } \\ { { \displaystyle \quad \quad = \sum _ { j = 1 } ^ { N } q _ { j } ^ { n + 1 } \times p _ { j } ^ { n + 1 / 2 } + \sum _ { j = 1 } ^ { N } q _ { j } ^ { n + 1 } \times \sum _ { i \neq j } \tau _ { i j } ( q _ { j } ^ { n + 1 } - q _ { i } ^ { n + 1 } ) ) , } } \end{array}
$$

where we have written

$$
\tau _ { i j } : = \frac { \varphi _ { i j } ^ { \prime } ( r _ { i j } ^ { n + 1 } ) } { r _ { i j } ^ { n + 1 } } .
$$

Continuing

$$
\begin{array} { l } { { \displaystyle m _ { t \ o t } ^ { n + 1 } = \sum _ { j = 1 } ^ { N } q _ { j } ^ { n + 1 } \times p _ { j } ^ { n + 1 / 2 } + \sum _ { j = 1 } ^ { N } \sum _ { i \ne j } q _ { j } ^ { n + 1 } \times \tau _ { i j } ( q _ { j } ^ { n + 1 } - q _ { i } ^ { n + 1 } ) } } \\ { { \displaystyle \qquad = \sum _ { j = 1 } ^ { N } q _ { j } ^ { n + 1 } \times p _ { j } ^ { n + 1 / 2 } + \sum _ { j = 1 } ^ { N } \sum _ { i \ne j } \tau _ { i j } ( q _ { j } ^ { n + 1 } \times q _ { j } ^ { n + 1 } - q _ { j } ^ { n + 1 } \times q _ { i } ^ { n + 1 } ) } } \\ { { \displaystyle \qquad = \sum _ { j = 1 } ^ { N } q _ { j } ^ { n + 1 } \times p _ { j } ^ { n + 1 / 2 } + \sum _ { j = 1 } ^ { N } \sum _ { i \ne j } \tau _ { i j } q _ { j } ^ { n + 1 } \times q _ { i } ^ { n + 1 } . } } \end{array}
$$

Note that the second term on the right-hand side can be broken down into a sum of pairs of terms $\left( i < j \right)$

$$
\tau _ { i j } q _ { j } ^ { n + 1 } \times q _ { i } ^ { n + 1 } + \tau _ { j i } \pmb { q } _ { i } ^ { n + 1 } \times \pmb { q } _ { j } ^ { n + 1 } .
$$

It is easy to see that $\tau _ { i j } ~ = ~ \tau _ { j i }$ , since these coefficients depend only on the distances between particles, thus, taking into account the antisymmetry of the cross product, we must have

$$
\tau _ { i j } { \pmb q } _ { j } ^ { n + 1 } \times { \pmb q } _ { i } ^ { n + 1 } + \tau _ { j i } { \pmb q } _ { i } ^ { n + 1 } \times { \pmb q } _ { j } ^ { n + 1 } = { \pmb 0 } ,
$$

and

$$
\pmb { m } _ { \mathrm { t o t } } ^ { n + 1 } = \sum _ { j = 1 } ^ { N } \pmb { q } _ { j } ^ { n + 1 } \times \pmb { p } _ { j } ^ { n + 1 / 2 } .
$$

Using (4.21) and simplifying, we find

$$
\begin{array} { l } { { \displaystyle m _ { \mathrm { t o t } } ^ { n + 1 } = \sum _ { j = 1 } ^ { N } ( { \bf q } _ { j } ^ { n } + \frac { 1 } { m _ { j } } p _ { j } ^ { n + 1 / 2 } ) \times p _ { j } ^ { n + 1 / 2 } } } \\ { { \displaystyle ~ = \sum _ { j = 1 } ^ { N } { \bf q } _ { j } ^ { n } \times p _ { j } ^ { n + 1 / 2 } } . } \end{array}
$$

Upon substituting (4.22) into (4.24), a line of argumentation analogous to that we have used above leads to

$$
\pmb { m } _ { \mathrm { t o t } } ^ { n + 1 } = \sum _ { j = 1 } ^ { N } \pmb { q } _ { j } ^ { n } \times \pmb { p } _ { j } ^ { n } = \pmb { m } _ { \mathrm { t o t } } ^ { n } .
$$

An even easier argument establishes the conservation of total linear momentum.

More generally, consider a splitting method with $H = H _ { 1 } + H _ { 2 } + . . . + H _ { k }$ , and suppose that a given first integral $F$ is also a first integral for each of the Hamiltonians $H _ { j }$ , i.e.

$$
\{ F , H _ { i } \} = 0 , \qquad i = 1 , \ldots , k .
$$

In this case, a numerical method constructed based on a concatenation of the flows of each of the Hamiltonians $H _ { j }$ will also automatically preserve $F$ . Thus we might as well have shown the conservation of angular momentum above by showing that the Poisson brackets of each component of $m _ { \mathrm { t o t } }$ with $\tau$ and with $V$ all vanish.

Example 1 Let us consider the Kepler problem in $\mathbb { R } ^ { 3 }$ with Hamiltonian

$$
H = { \frac { 1 } { 2 } } { \pmb { p } } \cdot { \pmb { p } } - { \frac { 1 } { \| { \pmb { q } } \| } } .
$$

A splitting method based on the splitting into kinetic and potential energy will certainly preserve linear and angular momentum. As a result the numerical solution will stay in a plane as determined by the initial data. However the numerically computed positions will not stay on a closed orbit. This is because the Runge–Lenz vector

$$
\pmb { e } = \pmb { p } \times \pmb { m } - \frac { \pmb { q } } { \Vert \pmb { q } \Vert }
$$

is a first integral of $H$ but not of $T$ and $V$ individually.

# 4.4.2 Implicit midpoint preserves quadratic first integrals

There are other instances of exact conservation of first integrals under symplectic discretization. For example, the implicit midpoint method exactly preserves any quadratic first integral of the form

$$
F = \frac { z ^ { T } A z } { 2 } + b ^ { T } z ,
$$

where $\pmb { A }$ is a symmetric matrix. Let us prove this for an arbitrary differential equation

$$
{ \frac { d } { d t } } z = { \pmb f } ( z )
$$

that satisfies

$$
\frac { d } { d t } F = ( \pmb { A } z + \pmb { b } ) ^ { T } \pmb { f } ( z ) = 0 .
$$

The implicit midpoint method yields

$$
z ^ { n + 1 } = z ^ { n } + \Delta t f ( z ^ { n + 1 / 2 } ) , \qquad z ^ { n + 1 / 2 } = \frac { z ^ { n + 1 } + z ^ { n } } 2 ,
$$

and we have to show that

$$
\frac { ( z ^ { n + 1 } ) ^ { T } A z ^ { n + 1 } } { 2 } + b ^ { T } z ^ { n + 1 } = \frac { ( z ^ { n } ) ^ { T } A z ^ { n } } { 2 } + b ^ { T } z ^ { n } .
$$

We multiply the first equation in (4.25) by $( { \pmb A } z ^ { n + 1 / 2 } + { \pmb b } ) ^ { T }$ from the left. We obtain

$$
\begin{array} { r l } & { \left( A z ^ { n + 1 / 2 } + b \right) ^ { T } z ^ { n + 1 } = \left( A z ^ { n + 1 / 2 } + b \right) ^ { T } z ^ { n } + \Delta t \left( A z ^ { n + 1 / 2 } + b \right) ^ { T } f \left( z ^ { n + 1 / 2 } \right) } \\ & { \qquad = \left( A z ^ { n + 1 / 2 } + b \right) ^ { T } z ^ { n } , } \end{array}
$$

and the desired result follows since

$$
{ \frac { 1 } { 2 } } \left( \pmb { A } z ^ { n } \right) ^ { T } z ^ { n + 1 } = { \frac { 1 } { 2 } } \left( \pmb { A } z ^ { n + 1 } \right) ^ { T } z ^ { n } .
$$

This implies, for example, that the implicit midpoint method exactly conserves linear and angular momentum and the total energy of a linear Hamiltonian system.

Similarly, one can show that the symplectic Euler methods and the generalized leapfrog method preserve any first integral of the form

$$
\boldsymbol { F } = \boldsymbol { q } ^ { T } \boldsymbol { A } \boldsymbol { p } + \boldsymbol { b } ^ { T } \boldsymbol { z } .
$$

(See problem 9 in the Exercises.)

# 4.5 Case studies

The splitting technique is a remarkably versatile tool for designing symplectic methods. It will be encountered frequently in the later chapters of this book. In the remainder of this chapter, we give several detailed examples of how splitting methods can be easily constructed for some special applications.

# 4.5.1 Application to $N .$ -body systems: a molecular dynamics model problem

We apply the St¨ormer–Verlet integrator to simulate a simplified molecular system consisting of $N$ equal mass particles interacting pairwise via a Lennard–Jones potential $\varphi _ { \mathsf { L J } } ( r ) = \epsilon \left[ ( \bar { r } / r ) ^ { 1 } 2 - 2 ( \bar { r } / r ) ^ { 6 } \right]$ . We chose $\epsilon = 0 . 4$ and $\bar { r } = 1$ . In this experiment we study the natural rearrangement of the particles over time.

In our numerical simulation we took $N = 4 0 0$ and placed all particles on to a regular cartesian lattice at the points $( i , j ) \in \mathbb { R } ^ { 2 }$ , $i , j = 0 , 1 , \ldots , 1 9 . \ { \mathsf { N e x t } }$ we perturbed each of the particles from the exact lattice positions by a small uniformly distributed random offset (magnitude no more than 0.01) so that the resulting particle positions were near – but not exactly at – the lattice sites. We then simulated the system using the St¨ormer–Verlet method. If the cartesian lattice were a stable equilibrium structure for the Lennard–Jones system, we would expect the particles to oscillate (chaotically) within small domains near the lattice sites, but the cartesian lattice is not stable: the system instead rearranges itself into a more favorable configuration which is near to a triangular lattice. This behavior is illustrated in Fig. 4.3, where snapshots of the dynamics of a system of 400 particles at various times are shown.

At this energy level, the particles are mostly held together by the attractive effect of the Lennard–Jones potential, although it is possible for particles to be ejected occasionally from the larger cluster. The triangular lattice is the local structure that minimizes the energy. The evolving cluster of particles tends to spend a substantially greater proportion of time in the vicinity of this type of lattice configuration. One typically observes that the evolution is not entirely uniform: particles arrange themselves into ordered regions (sometimes referred to as domains) surrounded by so-called lines of dislocation or grain boundaries. The shape of each domain and of the entire system is irregular and may continue to evolve with time, but the lattice structure will generally remain.

![](images/953ff4df0017b7e2cb8f32000f00ae067ddd5c4362821a4e5578ac62b9eb8390.jpg)  
Figure 4.3 Snapshots of the dynamics of a 400 atom planar Lennard–Jones system at various times between $t = 0$ and $t = 1 6 0$ .

The structure of the lattice can be characterized by means of a so-called order parameter. We define the order parameter as follows. For each particle, we first define the neighbor set $\mathcal { T } _ { j }$ by

$$
\mathcal { T } _ { i } = \{ j \neq i : \| \pmb { q } _ { j } - \pmb { q } _ { i } \| < \Delta \}
$$

typically fixing $\Delta$ at a small multiple of the displacement $\bar { r }$ used in the definition of the Lennard–Jones potential, say $\Delta = 1 . 3 \bar { r }$ . For each pair of particles in the neighbor set, with indices $j$ and $k$ , say, we define the angle $\theta _ { j i k }$ with vertex at $\pmb q _ { j }$ and sides defined by $\pmb { u } = \pmb { q } _ { j } - \pmb { q } _ { i }$ and $v = q _ { k } - q _ { i }$ . The so-called $C _ { m }$ , $m \geq 1$ , order parameter is defined in terms of these angles by

$$
\mu _ { m } = \sum _ { i = 1 } ^ { N } \sum _ { j , k \in \mathbb { Z } _ { i } } \cos ( m \theta _ { j i k } ) .
$$

The order parameter $\mu _ { 6 }$ is maximized when the atoms are at the vertices of a hexagonal lattice. If we graph these order parameters against time we see the curves shown in Fig. 4.4. Observe that, following a relaxation phase, there is transition in both order parameters, illustrating the transition from rectangular to hexagonal lattice configurations.

At these energies, the defects are generally not stable structures; instead they can be observed to evolve very slowly with time, eventually disappearing from the lattice. After 16000 steps we have arrived at very near a hexagonal lattice. The elimination of the final defects is typically associated to ejection of a particle, as we see in the final frame of Fig. 4.3. The $\mu _ { 6 }$ order parameter (Fig. 4.4) continues to rise until about $t = 2 0 0$ , where it stabilizes around $\mu _ { 6 } = 4 0 0 0$ .

![](images/703f077aaf512531c363b05d246186b85be827fad88c9b92a5dfbd29a65fa73d.jpg)  
Figure 4.4 Long-term evolution of parameters $\mu _ { 4 }$ and $\mu _ { 6 }$ for the 400-atom Lennard–Jones system.

It is now natural to ask what meaning can be assigned to the simulation results. We will take up this issue in greater detail in Chapter 5. For now, we employ a crude measure of the accuracy of the simulation, the energy, which we have plotted against time in Fig. 4.5 for a relatively long simulation of 100000 timesteps (i.e. to $t = 1 0 0 0$ ). Despite the presence of a large number of degrees of freedom and a complicated (chaotic) motion, the energy fluctuates within a narrow band around the true value.

![](images/1961e1dee30e776a0ad9e20f45017f346eea31947a5d08aea62254b837ca5e96.jpg)  
Figure 4.5 Energy vs. time for the 400-atom planar Lennard–Jones system solved on the time interval [0, 1000].

Whereas for the Lennard–Jones oscillator (Fig. 4.1) the behavior might be explained as a consequence of the numerical method inheriting periodic solutions (a desirable property, no doubt, but one that might be restricted to very lowdimensional systems), the results here seem to indicate a more generic stability property.

The challenges evident in this planar molecular model become much more acute when we turn to three-dimensional problems, where the local minima proliferate. For such applications, integrators exhibiting good long-term stability are very important indeed.

# 4.5.2 Particle in a magnetic field

We next present a method to simulate the motion of a particle moving in a magnetic field. This scheme demonstrates the versatility of the splitting formalism. As discussed in Chapter 3, a classical particle of mass $m$ moving in a potential field $V$ and subject to a constant magnetic field $\pmb { b } = ( b _ { 1 } , b _ { 2 } , b _ { 3 } ) ^ { T }$ can be modeled as a Hamiltonian system with

$$
H = \frac { 1 } { 2 m } \| \pmb { p } \| ^ { 2 } + V ( \pmb { q } ) ,
$$

and symplectic structure matrix

$$
\begin{array} { r } { J = \left[ \begin{array} { c c } { \mathbf { 0 } } & { + I } \\ { - I } & { \widehat { \boldsymbol { b } } } \end{array} \right] , \qquad \mathrm { w h e r e } \qquad \widehat { \boldsymbol { b } } = \left[ \begin{array} { c c c } { 0 } & { - b _ { 3 } } & { b _ { 2 } } \\ { b _ { 3 } } & { 0 } & { - b _ { 1 } } \\ { - b _ { 2 } } & { b _ { 1 } } & { 0 } \end{array} \right] . } \end{array}
$$

A splitting method can be based on the same splitting which gave the Euler-B method in the last section. The only difference lies in the modification of the structure matrix to incorporate the magnetic field.

Consider first the potential term $\begin{array} { r } { H _ { 2 } = V ( \pmb q ) } \end{array}$ . Upon writing out the differential equations $\dot { z } = J \nabla _ { z } H _ { 2 } ( z )$ in terms of $\pmb q$ and $p$ we find

$$
\begin{array} { l } { { \displaystyle { \frac { d } { d t } } { \pmb q } = { \bf 0 } } , } \\ { { \displaystyle { \frac { d } { d t } } { \pmb p } = - \nabla _ { { \pmb q } } V ( { \pmb q } ) , } } \end{array}
$$

which has the solution after one timestep $\bar { \pmb q } = { \pmb q } ^ { n }$ , $\bar { p } = p ^ { n } - \Delta t \nabla _ { q } V ( q ^ { n } )$ . On the other hand, the differential equations for the kinetic term $H _ { 1 } = \| \pmb { p } \| ^ { 2 } / 2 m$ are

$$
\begin{array} { l } { \displaystyle { \frac { d } { d t } \boldsymbol { q } = \boldsymbol { p } / m , } } \\ { \displaystyle { \frac { d } { d t } p = \frac { 1 } { m } \boldsymbol { b } \times \boldsymbol { p } = \frac { 1 } { m } \widehat { \boldsymbol { b } } p . } } \end{array}
$$

This is a linear system and hence is integrable. In fact, the second equation can be written

$$
\frac { d } { d t } p = \Omega { \pmb p } = \left[ \begin{array} { c c c } { 0 } & { - \omega _ { 3 } } & { \omega _ { 2 } } \\ { \omega _ { 3 } } & { 0 } & { - \omega _ { 1 } } \\ { - \omega _ { 2 } } & { \omega _ { 1 } } & { 0 } \end{array} \right] { \pmb p } ,
$$

$\pmb { \varOmega } : = \widehat { \pmb { b } } / m$ , which has solution $\pmb { p } ( t ) = \mathrm { e x p } \left( \Omega t \right) \pmb { p } ( 0 )$ . This exponential can be explicitly computed using “Rodrigues’ Formula”

$$
\exp \left( \Omega t \right) = I + \frac { \sin ( \omega t ) } { \omega } \Omega + 2 \left[ \frac { \sin ( \omega t / 2 ) } { \omega } \right] ^ { 2 } \Omega ^ { 2 } ,
$$

where $\omega = \sqrt { \omega _ { 1 } ^ { 2 } + \omega _ { 2 } ^ { 2 } + \omega _ { 3 } ^ { 2 } }$ . The solution for $\pmb q$ is then obtained by integration, i.e.

$$
\begin{array} { l } { { \displaystyle { \pmb q } ( t ) = { \pmb q } ( 0 ) + \frac { 1 } { m } \int _ { 0 } ^ { t } \exp ( \varOmega s ) { \pmb p } ( 0 ) d s } \ ~ } \\ { { \displaystyle ~ = { \pmb q } ( 0 ) + \frac { 1 } { m } \left[ t I + \frac { 1 - \cos ( \omega t ) } { \omega ^ { 2 } } \pmb \Omega - \frac { \sin ( \omega t ) - \omega t } { \omega ^ { 3 } } \Omega ^ { 2 } \right] { \pmb p } ( 0 ) } } \\ { { \displaystyle ~ = { \pmb q } ( 0 ) + \frac { 1 } { m } { \pmb F } ( t ) { \pmb p } ( 0 ) } , } \end{array}
$$

where the last equation is to be understood as the defining equation for the $3 \times 3$ matrix $\pmb { F } ( t )$ .

As in the canonical case, the symmetric “leapfrog splitting” method

$$
\pmb { \psi } _ { \Delta t } = \pmb { \phi } _ { \frac { 1 } { 2 } \Delta t , V } \circ \pmb { \phi } _ { \Delta t , T } \circ \pmb { \phi } _ { \frac { 1 } { 2 } \Delta t , V }
$$

again yields a second-order method. The idea of using a splitting in this way to propagate a particle in a magnetic field was suggested to one of us by J.C. SCOVEL, therefore we feel that it is appropriate to name the scheme accordingly.

$$
\begin{array} { c } { { \displaystyle p ^ { n + 1 / 2 } = p ^ { n } - \frac { \Delta t } { 2 } \nabla _ { q } V ( q ^ { n } ) , } } \\ { { \displaystyle q ^ { n + 1 } = q ^ { n } + \frac { 1 } { m } F ( \Delta t ) p ^ { n + 1 / 2 } , } } \\ { { \displaystyle p ^ { n + 1 } = \exp ( \Delta t \Omega ) p ^ { n + 1 / 2 } - \frac { \Delta t } { 2 } \nabla _ { q } V ( q ^ { n + 1 } ) . } } \end{array}
$$

# Numerical experiment

Let us compare with numerical experiments Scovel’s method and the symplectic implicit midpoint method, treating the case of a particle of mass $m = 1$ moving in a magnetic field $\pmb { b } = ( 0 , 0 , 1 ) ^ { T }$ under the influence of an attractive Coloumb potential $V = - 1 / | | \pmb q | |$ .

To evaluate the quality of a numerical solution to this problem, we look to the first integrals, namely the energy $H$ and the magnetic momentum

$$
\mu = b \cdot \left( q \times \left( p - \frac { 1 } { 2 } \pmb { b } \times \pmb { q } \right) \right) .
$$

(See the Exercises in Chapter 3.)

The initial conditions we used were $\pmb { q } = ( 1 , 1 , 1 ) ^ { T }$ and $\pmb { p } = ( 0 , 0 , 0 ) ^ { T }$ . In Fig. 4.6, we plot the relative error in energy and the projection of the solution trajectory on to the $\left( q _ { 1 } , q _ { 2 } \right)$ -plane for Scovel’s method and $\Delta t = 0 . 1$ .

![](images/0f232815ccac8ca7ca53333f3c5bc9630d7d26c22f7a9e3e1c48225459d58e49.jpg)  
Figure 4.6 Energy and projected trajectory using Scovel’s method, $\Delta t = 0 . 1$ .

While Scovel’s method is explicit, the implicit midpoint method requires the solution of a nonlinear system of equations at each timestep. For this purpose, we use the following procedure. The nonlinear equations defining the half-step in the implicit midpoint scheme are solved by a fixed-point iteration in $\left( \bar { \pmb q } _ { k } , \bar { \pmb p } _ { k } \right)$

$$
\begin{array} { l } { \displaystyle \bar { \pmb q } _ { k + 1 } = \pmb q ^ { n } + \frac { \Delta t } { 2 } \bar { \pmb p } _ { k } , } \\ { \displaystyle \bar { \pmb p } _ { k + 1 } = \pmb p ^ { n } + \frac { \Delta t } { 2 } \pmb b \times \bar { \pmb p } _ { k } - \frac { \Delta t } { 2 } \nabla _ { \pmb q } V ( \bar { \pmb q } _ { k } ) , } \end{array}
$$

for $k = 0 , 1 , 2 , \ldots .$ with $\bar { p } ^ { 0 } = p ^ { n }$ . The iteration is stopped once

$$
| | \bar { \pmb q } _ { k } - \bar { \pmb q } _ { k - 1 } | | _ { \infty } + | | \bar { \pmb p } _ { k } - \bar { \pmb p } _ { k - 1 } | | _ { \infty } \ \leq \ \epsilon ,
$$

![](images/4787764b3d529ef8c8024c3d875356eff7965094ff71ed18ed6beca68b5242ea.jpg)  
Figure 4.7 (Left) Maximum error in the energy versus stepsize for the implicit midpoint rule (solid) and Scovel’s method $( \times )$ . (Right) Precision versus work (number of force evaluations per unit time interval) diagram for the implicit midpoint method (solid) and Scovel’s method $( \times )$ .

with $\epsilon = 1 0 ^ { - 9 }$ . We then set

$$
{ \pmb q } ^ { n + 1 / 2 } = \bar { \pmb q } _ { k } , \qquad { \pmb p } ^ { n + 1 / 2 } = \bar { \pmb p } _ { k } ,
$$

and proceed with half a timestep of the explicit Euler method. This completes one timestep with the implicit midpoint method.

In Fig. 4.7(a), we plot the maximum relative error in energy, i.e.

$$
E _ { \mathrm { m a x } } = \operatorname* { m a x } _ { n = 1 , 2 , \ldots } { \frac { | H ( z ^ { 0 } ) - H ( z ^ { n } ) | } { | H ( z ^ { 0 } ) | } } ,
$$

as a function of the stepsize $\Delta t$ . We see that the implicit midpoint rule is slightly more accurate than Scovel’s method. In Fig. 4.7(b), we graph the numerical error against the number of force evaluations per unit time interval. Scovel’s method method is the clear winner. The efficiency differences between the explicit and implicit methods generally become more pronounced in systems with higher dimension, or with more costly force calculations. This rule of thumb might not apply in cases where highly accurate solutions are required and higher-order methods need to be used.

# 4.5.3 Weakly coupled systems

Suppose that our Hamiltonian $H$ can be written as a sum of $k$ decoupled terms $H _ { j }$ together with a coupling term $H _ { c }$ , i.e.

$$
H = H _ { 1 } + H _ { 2 } + \ldots + H _ { k } + H _ { c } ,
$$

and

$$
\{ H _ { i } , H _ { j } \} = 0 ,
$$

for all $i , j = 1 , \dots , k$ . The condition (4.33) implies that the flow map associated with the Hamiltonian

$$
\tilde { H } = H _ { 1 } + H _ { 2 } + \cdot \cdot \cdot + H _ { k }
$$

satisfies

$$
\pmb { \phi } _ { t , \tilde { H } } = \pmb { \phi } _ { t , H _ { 1 } } \circ \pmb { \phi } _ { t , H _ { 2 } } \circ \cdot \cdot \cdot \circ \pmb { \phi } _ { t , H _ { k } } .
$$

If, in addition, all the Hamiltonians $H _ { j }$ and $H _ { c }$ are explicitly integrable, then we can easily obtain a splitting method from the composition of the flow maps $\boldsymbol { \Phi } _ { t , \tilde { H } }$ and Φt,Hc .

As an illustration, consider the gravitational model for a pair of planets orbiting a star. In the star-centered frame, the Hamiltonian is

$$
H = \frac { 1 } { 2 m _ { 1 } } \lVert { \pmb p } _ { 1 } \rVert ^ { 2 } + \frac { 1 } { 2 m _ { 2 } } \lVert { \pmb p } _ { 2 } \rVert ^ { 2 } - \frac { G m _ { 1 } m _ { \odot } } { \lVert { \pmb q } _ { 1 } \rVert } - \frac { G m _ { 2 } m _ { \odot } } { \lVert { \pmb q } _ { 2 } \rVert } - \frac { G m _ { 1 } m _ { 2 } } { \lVert { \pmb q } _ { 1 } - { \pmb q } _ { 2 } \rVert } ,
$$

where $G$ is the universal gravitational constant, and $m _ { 1 } , ~ m _ { 2 }$ , and $m _ { \odot }$ represent the masses of the two planets and the star, respectively. We divide $H$ into three parts

$$
\begin{array} { l } { { \displaystyle H _ { 1 } = \frac { 1 } { 2 m _ { 1 } } \| { \pmb p } _ { 1 } \| ^ { 2 } - \frac { G m _ { 1 } m _ { \odot } } { \| { \pmb q } _ { 1 } \| } } , } \\ { { \displaystyle H _ { 2 } = \frac { 1 } { 2 m _ { 2 } } \| { \pmb p } _ { 2 } \| ^ { 2 } - \frac { G m _ { 2 } m _ { \odot } } { \| { \pmb q } _ { 2 } \| } } , } \end{array}
$$

and

$$
H _ { c } = - \frac { G m _ { 1 } m _ { 2 } } { \left\| \pmb q _ { 1 } - \pmb q _ { 2 } \right\| } .
$$

A second-order splitting method is then given by

$$
\begin{array} { r } { \pmb { \psi } _ { \Delta t } = \pmb { \phi } _ { \frac { 1 } { 2 } \Delta t , H _ { c } } \circ \pmb { \phi } _ { \Delta t , H _ { 1 } + H _ { 2 } } \circ \pmb { \phi } _ { \frac { 1 } { 2 } \Delta t , H _ { c } } . } \end{array}
$$

The Hamiltonians $H _ { 1 }$ and $H _ { 2 }$ describe completely decoupled Kepler problems, hence they can be solved in principle. The coupling term $H _ { c }$ depends only on position variables, so it, too, can be integrated exactly. A method of this type was used to advantage by WISDOM AND HOLMAN [203] in a celebrated study of the long-term dynamics of the Solar System.

There are some subtleties here: while Kepler problems are exactly solvable using the available integrals, not all methods are suitable for use in a timestepping setting, where many such computations may be needed. Another aspect that will govern the overall efficiency of the method is the extent to which the perturbation due to the coupling term $H _ { 1 2 }$ can be viewed as small compared with the Kepler terms. If the coupling is strong, we can expect large errors to crop up at each step of computation. More discussion of gravitational N-body problems will be found in Chapter 9.

# 4.5.4 Linear/nonlinear splitting

There are many phenomena which are described, in zeroth-order approximation, by a quadratic Hamiltonian. For example, we might have

$$
H = \frac { 1 } { 2 } { \pmb p } ^ { T } { \pmb M } ^ { - 1 } { \pmb p } + \frac { 1 } { 2 } { \pmb q } ^ { T } { \pmb K } { \pmb q } + \epsilon H _ { \sf N } ( { \pmb q } , { \pmb p } ) ,
$$

where  can be viewed as a small perturbation parameter. For these problems it is often useful to employ a splitting technique in which the quadratic part is evolved separately from $H _ { \mathsf { N } }$ .

In most cases, $H _ { \mathsf { N } }$ may be regarded as position dependent only and, hence, is integrable. If $H _ { \mathsf { N } }$ is not exactly integrable, an alternate symplectic method can often be used for its evolution. An example for linear/nonlinear splitting is given by the Fermi–Pasta–Ulam problem (see problem 5 in the Exercises) [60, 192]. Some discussion of linear/nonlinear splittings in the context of Hamiltonian partial differential equations may be found in [129].

# 4.6 Exercises

1. Canonical methods. Show that the Euler-A method is canonical.

2. Composition of symplectic maps. Show that the composition of two symplectic maps $\pmb { \psi } _ { 1 }$ , $\pmb { \psi } _ { 2 }$ yields a symplectic map.

3. Kepler problem. Discretize the planar Kepler problem with Hamiltonian

$$
H ( \pmb { q } , \pmb { p } ) = \frac { 1 } { 2 } \pmb { p } ^ { T } \pmb { p } - \frac { 1 } { | | \pmb { q } | | } ,
$$

and initial conditions $\pmb { q } = ( 1 , 0 ) ^ { T }$ and $\pmb { p } = ( 0 , 1 ) ^ { T }$ , by the explicit St¨ormer– Verlet method and the implicit midpoint rule. Use functional iteration to solve the nonlinear equations resulting from the implicit midpoint rule (see Section 4.5.2). Compare the two methods based on the conservation of energy versus stepsize and the number of force field evalations per timestep. Take the stepsize $\Delta t$ from the interval [0.01, 0.0001] and integrate over a time interval [0, 10].

4. Commuting flow maps. Show that if the Poisson bracket of two functions $F$ and $G$ , $\{ F , G \}$ , vanishes identically, then the corresponding flow maps $\pmb { \phi } _ { \tau , F }$ and $\phi _ { \tau , G }$ satisfy

$$
\phi \circ \pmb { \phi } _ { \tau , F } \circ \pmb { \phi } _ { \tau , G } - \phi \circ \pmb { \phi } _ { \tau , G } \circ \pmb { \phi } _ { \tau , F } = \mathscr { O } ( \tau ^ { 2 } ) ,
$$

for any smooth function $\phi : \mathbb { R } ^ { 2 d }  \mathbb { R }$ . (This result is a first step to show that the two flow maps commute if and only if $\{ F , G \} = 0$ ; see Chapter 5.) Hint: differentiate the given formula with respect to $\tau$ and make use of the Poisson bracket notation.

5. Fermi–Pasta–Ulam problem. The “Fermi–Pasta–Ulam problem” [60, 192] has Hamiltonian

$$
H = \frac { 1 } { 2 m } \sum _ { i = 1 } ^ { N - 1 } p _ { i } ^ { 2 } + \frac { \kappa } { 2 } \sum _ { i = 1 } ^ { N - 1 } r _ { i } ^ { 2 } + \frac { \lambda } { s } \sum _ { i = 1 } ^ { N - 1 } \epsilon r _ { i } ^ { s } , r _ { i } = q _ { i + 1 } - q _ { i } , q _ { 0 } = q _ { N } = 0 ,
$$

where $\kappa$ is the linear elastic constant (Hooke’s spring), $\lambda$ is a small parameter, and $s$ is a small positive integer (usually $s = 3$ or $s = 4$ ). Choosing $m = \kappa =$ 1, $N = 3 2$ , $s = 3$ , and $\lambda = 1 / 4$ ,

a. Implement the Euler-B method for this problem.

b. Design and implement a first-order “linear/nonlinear” splitting method for this problem.

c. Apply each of the two methods with the following initial condition

$$
q _ { i } = \left( \frac { 2 } { N } \right) ^ { 1 / 2 } \sin \frac { i \pi } { N } , \qquad p _ { i } = 0 ,
$$

$i = 1 , \ldots , N { - } 1$ , over a time interval of 200 periods of length $T = 2 \pi / \omega$ , $\omega = 2 \sin ( \pi / ( 2 N ) )$ [192]. Monitor the total energy $H$ and the harmonic energy

$$
E _ { \mathrm { { h a r m o n i c } } } = { \frac { 1 } { 2 m } } \sum _ { i = 1 } ^ { N - 1 } p _ { i } ^ { 2 } + { \frac { \kappa } { 2 } } \sum _ { i = 1 } ^ { N - 1 } r _ { i } ^ { 2 } .
$$

Compare the methods in terms of accuracy and efficiency. For further comparison, also implement the fourth-order explicit Runge–Kutta method of Section 2.4. Changing the value of $\lambda$ , what behavior in Eharmonic do you observe for larger and smaller values of $\lambda ?$

6. Discretized Schr¨odinger equation. Differential equations involving complex variables arise in quantum mechanics following discretization in the spatial variables. In a simplified case such systems would take the form of a linear system

$$
\dot { z } = - \mathrm { i } H z ,
$$

where the dimension of the complex vector $\boldsymbol { z } \in \mathbb { C } ^ { d }$ is typically very large, and $H$ is a real symmetric matrix. This can be viewed as a canonical Hamiltonian system over a symplectic structure on $\mathbb { C } ^ { d }$ . We introduce the complex-valued Hermitian inner product

$$
\langle \pmb { u } , \pmb { v } \rangle _ { \mathsf { C } } = \sum _ { i = 1 } ^ { d } \bar { u } _ { i } v _ { i } ,
$$

where $\bar { W }$ denotes the complex conjugate of a complex number $W \in \mathbb { C }$ . The symplectic two-form $\Omega$ is now defined in terms of the imaginary part of the Hermitian inner product [124]

$$
\Omega ( \pmb { \xi } , \pmb { \eta } ) = \mathsf { I m } \langle \pmb { \xi } , \pmb { \eta } \rangle _ { \mathsf { C } } , \qquad \pmb { \xi } , \pmb { \eta } \in \mathbb { C } ^ { d } .
$$

The real inner product needed to define the gradient is given by

$$
\langle \pmb { u } , \pmb { v } \rangle = \mathsf { R e } \langle \pmb { u } , \pmb { v } \rangle _ { \mathsf { C } } .
$$

a. Using the standard definition

$$
\langle \nabla _ { z } H ( z ) , u \rangle = \operatorname* { l i m } _ { \varepsilon \to 0 } { \frac { H ( z + \varepsilon u ) - H ( z ) } { \varepsilon } }
$$

of a gradient, show that

$$
\nabla _ { z } H ( z ) = H z ,
$$

for the quadratic Hamiltonian

$$
H ( z ) = { \frac { 1 } { 2 } } \langle z , H z \rangle .
$$

Also verify that the structure matrix associated with the symplectic twoform $\Omega$ is

$$
J = - \mathsf { i } I _ { d } ,
$$

i.e.

$$
\Omega ( \pmb { \xi } , \pmb { \eta } ) = \langle \pmb { \xi } , \pmb { J } ^ { - 1 } \pmb { \eta } \rangle .
$$

b. Show that the two-norm $\| z \| _ { 2 }$ is a conserved quantity of the differential equation (4.34). Discretize the Schr¨odinger equation (4.34) by the implicit midpoint method. Is the resulting discretization symplectic and will it preserve the two-norm $\Vert z \Vert _ { 2 } ?$ Note: recall that the two-norm of a vector $z = ( z _ { 1 } , z _ { 2 } , \ldots , z _ { d } ) ^ { T }$ in $\mathbb { C } ^ { d }$ is defined by

$$
\| z \| = \langle z , z \rangle ^ { 1 / 2 } = ( | z _ { 1 } | ^ { 2 } + | z _ { 2 } | ^ { 2 } + . . . + | z _ { d } | ^ { 2 } ) ^ { 1 / 2 } ,
$$

where $\left| Z _ { j } \right|$ represents the complex modulus of $Z _ { I }$ , i.e. the square root of the sum of squares of the real and imaginary parts.

c. By separating $z = x + \mathrm { i } y$ into its real and imaginary parts, show that (4.34) can be rewritten as a canonical and separable Hamiltonian system with $d$ degrees of freedom. If the St¨ormer–Verlet method is applied to this system, is the two-norm of the solution still conserved?

7. Time-dependent Hamiltonian systems. A time-dependent or non-autonomous Hamiltonian system in $R ^ { 2 d }$ has an energy function

$$
H = H ( \pmb { q } , \pmb { p } , t ) .
$$

The differential equations associated to such a system are taken to be

$$
\begin{array} { r } { \dot { \pmb q } = + \nabla _ { \pmb { p } } H ( \pmb q , \pmb { p } , t ) , } \\ { \dot { \pmb { p } } = - \nabla _ { \pmb { q } } H ( \pmb q , \pmb { p } , t ) . } \end{array}
$$

The key difference between an autonomous (time-independent) and nonautonomous system is that, in the latter case, the energy is no longer a conserved quantity of the motion. On the other hand, it is possible to construct an extended system for any non-autonomous system by identifying $t$ with an additional variable $Q$ , corresponding momentum $P$ , and Hamiltonian

$$
\tilde { H } = H ( \pmb { q } , \pmb { p } , Q ) + P .
$$

a. Write out the differential equations for the extended Hamiltonian $\tilde { H }$ . Show that if the extended system is solved with initial conditions $\pmb q ( t _ { 0 } ) =$ $\pmb q ^ { 0 }$ , $\pmb { p } ( t _ { 0 } ) = \pmb { p } ^ { 0 }$ , $Q ( t _ { 0 } ) = t _ { 0 }$ , $P ( t _ { 0 } ) = 0$ , then the solution obtained is the same as that of the original Hamiltonian $( H )$ for the initial conditions $\pmb q ( t _ { 0 } ) = \pmb q ^ { 0 }$ , $\pmb { p } ( t _ { 0 } ) = \pmb { p } ^ { 0 }$ . Thus a non-autonomous Hamiltonian system is equivalent to an autonomous system with an additional degree of freedom.

b. A symplectic integrator applied to the extended Hamiltonian system can typically be reduced to an integrator for the original system. By applying Euler-B to (4.35) and simplifying the resulting equations, show that, in terms of the original variables, the method is equivalent to

$$
\begin{array} { r } { \pmb q ^ { n + 1 } = \pmb q ^ { n } + \Delta t \nabla _ { p } H ( \pmb q ^ { n } , \pmb p ^ { n + 1 } , t _ { n } ) , } \\ { \pmb p ^ { n + 1 } = \pmb p ^ { n } - \Delta t \nabla _ { p } H ( \pmb q ^ { n } , \pmb p ^ { n + 1 } , t _ { n } ) . } \end{array}
$$

c. Find the appropriate generalization of the St¨ormer–Verlet method to non-autonomous Hamiltonian systems of the form $H ( \pmb { q } , \pmb { p } ) = T ( \pmb { p } ) +$ $V ( \pmb q , t )$ .

d. (Refers to problem $^ { 6 }$ .) In many applications arising in quantum mechanics, the matrix $H$ in (4.34) must be regarded as time dependent. Often, the system takes the form

$$
\pmb { H } = \pmb { H } _ { 0 } + \varepsilon \pmb { H } _ { 1 } ( t ) ,
$$

where $H _ { 0 }$ is independent of $t$ and easily diagonalized (i.e. has eigenvalues that can easily be computed), while $H _ { 1 } ( t )$ is very sparse (has many zero elements) or is possibly diagonal, and $\varepsilon > 0$ is a small coupling parameter. Based on this additive decomposition, and an extension of the Hamiltonian as outlined above, develop an appropriate symplectic splitting method for the non-autonomous, Hamiltonian system (4.34).

8. General reversing symmetry and magnetic fields. Recall that a general differential equation ${ d z } / { d t } = { { \pmb f } } ( z )$ is reversible with respect to an involution S if $- { \pmb f } ( z ) = { \pmb S } { \pmb f } ( { \pmb S } z )$ .

a. With this definition, show that the equations of motion for a particle in a constant magnetic field are not time reversible with respect to the involution $p  - p$ .

b. Consider an augmented system obtained by treating the constant vector $b$ as a variable of the system

$$
\begin{array} { l } { \displaystyle { \frac { d } { d t } q = p / m , } } \\ { \displaystyle { \frac { d } { d t } p = - \nabla _ { q } V ( q ) + \frac { 1 } { m } b \times p , } } \\ { \displaystyle { \frac { d } { d t } b = 0 . } } \end{array}
$$

Show that this system is time reversible with respect to the involution defined by $p  - p , \ b  - b$ .

c. Consider the implication of part (b) for the flow map of the system. What property should a method have to be considered time reversible for the magnetic field problem? In what sense is Scovel’s method a timereversible scheme?

9. Preservation of first integrals. Show for any of the two symplectic Euler methods that first integrals of the general form

$$
F = \pmb { q } ^ { T } \pmb { A } p
$$

are exactly preserved. What can you conclude for the generalized leapfrog method?

10. Canonical Hamiltonian with a magnetic field. The equations of motion for a particle in a constant magnetic field can be recast in an alternative, canonical Hamiltonian form. For a constant magnetic field $b$ , this was discussed in Chapter 3. Here we generalize the canonical approach to nonconstant magnetic fields $b ( q )$ , $\pmb q \in \mathbb { R } ^ { 3 }$ .

a. We assume that

$$
\sum _ { i = 1 } ^ { 3 } \frac { \partial } { \partial q _ { i } } b _ { i } ( \pmb q ) = 0 .
$$

Hence, one can introduce a (non-unique) vector potential $\pmb { A }$ such that $\nabla _ { q } \times \pmb { A } ( \pmb { q } ) = \pmb { b } ( \pmb { q } )$ . For a constant vector $b$ , what is $A ( q ) ?$

b. Write out the differential equations for the canonical Hamiltonian

$$
H _ { c } ( \pmb { p } , \pmb { q } ) = \frac { 1 } { 2 m } | | \pmb { p } + \pmb { A } ( \pmb { q } ) | | ^ { 2 } - \frac { \gamma } { | | \pmb { q } | | }
$$

and compare with (3.32)–(3.33) of Chapter 3.

c. Devise symplectic methods for the canonical equations of motion. Discuss their respective advantages and disadvantages.

11. Time-reversible methods. Show that the generalized St¨ormer–Verlet method and the implicit midpoint rule are both time reversible when applied to a time-reversible Hamiltonian system. Use the symmetry property of the two methods and show that

$$
\pmb { \psi } _ { \Delta t } ( z ^ { n } ) = \pmb { S } \pmb { \psi } _ { - \Delta t } ( \pmb { S } z ^ { n } ) .
$$

On the contrary, both symplectic Euler methods also satisfy the above identity but, since they are not symmetric, they are not time reversible. Verify this statement for the symplectic Euler-B method.

# 5

# The modified equations

We have seen in the previous chapter that integrators preserving symplectic structure and/or first integrals can often be constructed in a straightforward way. In this chapter, we consider the properties of those methods and the implications for long-term simulations.

The traditional approach of numerical analysis generally assumes that the purpose of simulation is the faithful reproduction of a particular solution or trajectory, but individual trajectories typically are not of primary interest in most modern, scientific research; 1 rather, the scientist typically treats the trajectory as a particular realization of a fundamentally stochastic evolution modelling in some way the myriad undetermined perturbations present in a “real-world” environment. It was the important discovery of LORENZ [119] that differential equations can exhibit a chaotic solution behavior that includes an essentially stochastic or “random” component. The scientist views the model being analyzed as representative of a class of nearby models based on parameters which are typically only empirically (and approximately) determined. Furthermore, exact initial conditions are also typically not available. Some classical examples of such a scenario are molecular dynamics and numerical weather prediction.

It is now apparent that most modern large-scale simulations are conducted with timesteps and time intervals such that the numerical solution cannot be thought of as close to any particular model solution. The purpose of wedding the development of integrators to the standard axiomatic principle of timestepping – that one is attempting to approximate a particular trajectory – is thus called into question. Although high accuracy often is not needed in nonlinear dynamics computations, we must recognize certain important constraints imposed by the laws of nature. For example, there is widespread agreement that a conservative system should be sampled on or near the surface of constant energy, although it should be evident by now that this alone is not enough of a restriction (any arbitrary sequence of random data points in the phase space could be easily projected to the energy surface, but would not be expected to provide a reasonable approximation of a trajectory). The presence of first integrals such as energy and weaker adiabatic invariants (which exhibit only a mild variation over long time intervals) can provide helpful criteria for assessing the validity of a simulation, even in a nonlinear setting.

In this chapter, we begin our investigation of the implications of geometric properties for the behavior of a numerical method. The cornerstone of this theory is the principle of backward error analysis. In the context of numerical linear algebra, backward error analysis was promulgated by WILKINSON [202] and others and has been used as a means of evaluating the propagation of rounding errors in various matrix algorithms. Let us illustrate with the problem of solving a system of $N$ linear equations in $N$ unknowns

$$
\pmb { A x } = \pmb { b } ,
$$

where the $N \times N$ nonsingular matrix $\pmb { A }$ and right-hand side vector $\pmb { b } \in \mathbb { R } ^ { N }$ are known, and a vector $\boldsymbol { x } \in \mathbb { R } ^ { N }$ is to be computed by the standard technique of Gaussian elimination, i.e. reduction of the matrix A to an upper triangle matrix via successive elementary row operations (replacing a row of the matrix by the sum of the row and a scalar multiple of another), and corresponding modification of the right-hand side. At each stage of the calculation in finite precision, rounding errors are introduced. These rounding errors are compounded by successive operations, and this may result in a serious growth in error. In a forward error analysis, the potential magnitude of this error growth is evaluated, resulting in a bound for the total error as a function of the dimension of the system and the magnitude of the rounding errors introduced at each step.

For Gaussian elimination, it has been found that an alternative backward error analysis is far more meaningful. The philosophy of backward error is based on recognition that the problem being solved is, itself, typically only an approximation to the actual problem of interest, since the elements of the matrix A and vector $^ { b }$ are, themselves, generally subject to small errors of measurement, prior computation, and/or finite representation. It can be shown that the solution obtained by a numerical finite-precision arithmetic implementation of Gaussian elimination is the exact solution of a nearby linear system, i.e. the approximate solution $\widehat { \boldsymbol { x } }$ obtained by the numerical scheme satisfies a perturbed linear system of the form

$$
( \pmb { A } + \Delta \pmb { A } ) \widehat { \pmb { x } } = \pmb { b } + \Delta \pmb { b } ,
$$

where the magnitudes of the matrix $\Delta A$ and vector $\Delta b$ can be bounded by the product of a constant, the growth factor, and the magnitude of the rounding errors.

It is this idea which we will now develop for the purposes of understanding geometric integrators. In this analogy, the linear system is replaced by a system of differential equations satisfying some geometric properties (for example, Hamiltonian, symplecticness, integral preserving). Truncation errors introduced by the integrator play the same role as rounding errors do in the linear algebra context. It is shown that, in a practical sense, the numerical solution obtained from an appropriate geometric integrator is the exact solution to a perturbed system of differential equations satisfying the same geometric property (or properties). The existence of such a backward error interpretation has direct implications for the qualitative behavior of the numerical solution and, ultimately, in the effectiveness of the method compared with others.

# 5.1 Forward v. backward error analysis

The discretization of a sufficiently smooth differential equation,

$$
\frac { d } { d t } z = \pmb { f } ( z ) ,
$$

by a one-step method

$$
z ^ { n + 1 } = \pmb { \psi } _ { \Delta t } ( z ^ { n } ) , \qquad t _ { n + 1 } = t _ { n } + \Delta t ,
$$

of order $p \geq 1$ implies that there exists a constant $M > 0$ such that

$$
\begin{array} { r } { | | \psi _ { \Delta t } ( z ) - \phi _ { \Delta t , t } ( z ) | | \leq M \Delta t ^ { p + 1 } , } \end{array}
$$

for all $z$ in an appropriate subset of phase space $\mathbb { R } ^ { k }$ and for all $\Delta t$ sufficiently small. Here $\pmb { \phi } _ { \Delta t , f }$ denotes the exact time- $\Delta t$ -flow of the vector field $\boldsymbol { f }$ . As already mentioned in Section 2.1.2, the difference between the exact solution $z ( t _ { n } )$ and the numerically computed approximation $z ^ { n }$ at $t ~ = ~ t _ { n }$ satisfies an upper bound

$$
| | z ( t _ { n } ) - z ^ { n } | | \leq K \left( e ^ { t _ { n } L } - 1 \right) \Delta t ^ { p } ,
$$

$L > 0$ the Lipschitz constant of $\boldsymbol { f }$ and $K > 0$ a constant independent of $t _ { n }$ and $\Delta t$ . It is obvious that this estimate becomes useless whenever $t _ { n } L \gg 1$ unless a very small timestep $\Delta t$ is taken. This requirement is certainly not satisfied in simulations of large nonlinear systems where low-order methods are typically used to integrate to very long times $t _ { n }$ .

Backward error (or modified equations) analysis in the context of (partial) differential equations can be traced back to the work of WARMING AND HYETT [199]. The idea is simple: we derive a modified differential equation (the modified differential equation depends on the stepsize $\Delta t$ )

$$
\frac { d } { d t } z = \tilde { { \pmb f } } ( z ; \Delta t ) ,
$$

and choose the modified vector field $\tilde { \pmb { f } } ( \Delta t ) : \mathbb { R } ^ { k }  \mathbb { R } ^ { k }$ such that the numerical method $\psi _ { \Delta t }$ is a more accurate solution to this modified problem.

Let us demonstrate the basic idea by going through a simple example. Assume we discretize the differential equation (5.2) by the explicit Euler method

$$
z ^ { n + 1 } = z ^ { n } + { \Delta t } f ( z ^ { n } ) .
$$

This approximation has to be compared with the flow map $\boldsymbol { \phi } _ { t , f }$ at $t = \Delta t$ . The first two terms in the Taylor series expansion of $\pmb { \phi } _ { t = \Delta t , f }$ are given by

$$
\begin{array} { r l r } {  { z ( t _ { n + 1 } ) = \pmb { \phi } _ { \Delta t , f } ( z ^ { n } ) } } \\ & { } & { = z ^ { n } + \Delta t \pmb { f } ( z ^ { n } ) + \frac { \Delta t ^ { 2 } } { 2 } \pmb { f } ^ { \prime } ( z ^ { n } ) \pmb { f } ( z ^ { n } ) + \mathcal { O } ( \Delta t ^ { 3 } ) , } \end{array}
$$

where $\pmb { f } ^ { \prime } ( z )$ denotes the Jacobian of $\boldsymbol { f }$ at $z$ . Taking the difference of $\psi _ { \Delta t } ( z ^ { n } )$ and $\pmb { \phi } _ { \Delta t , f } \left( z ^ { n } \right)$ , we obtain, as expected,

$$
\pmb { \phi } _ { \Delta t , t } ( z ^ { n } ) - \pmb { \psi } _ { \Delta t } ( z ^ { n } ) = \frac { \Delta t ^ { 2 } } { 2 } \pmb { f } ^ { \prime } ( z ^ { n } ) \pmb { f } ( z ^ { n } ) + \pmb { \mathcal { O } } ( \Delta t ^ { 3 } ) .
$$

Let us now consider the modified differential equation

$$
\frac { d } { d t } z = \tilde { { \bf f } } _ { 1 } ( z ; \Delta t ) : = { \bf f } ( z ) - \frac { \Delta t } { 2 } { \bf f } ^ { \prime } ( z ) { \bf f } ( z ) ,
$$

with associated flow map $\pmb { \phi } _ { t , \tilde { f } _ { 1 } }$ . At $t = \Delta t$ , we obtain (neglecting terms of order $\Delta t ^ { 3 }$ and higher)

$$
\begin{array} { l } { \phi _ { \Delta t , \tilde { f } _ { 1 } } ( z ^ { n } ) \approx \displaystyle \bigg [ z ^ { n } + t \tilde { f } _ { 1 } ( z ^ { n } ; \Delta t ) + \frac { t ^ { 2 } } { 2 } \tilde { f } _ { 1 } ^ { \prime } ( z ^ { n } ; \Delta t ) \tilde { f } _ { 1 } ( z ^ { n } ; \Delta t ) \bigg ] _ { t = \Delta t } } \\ { \approx z ^ { n } + \Delta t \displaystyle \left[ f ( z ^ { n } ) - \frac { \Delta t } { 2 } { \bf f } ^ { \prime } ( z ^ { n } ) { \bf f } ( z ^ { n } ) \right] + \frac { \Delta t ^ { 2 } } { 2 } { \bf f } ^ { \prime } ( z ^ { n } ) { \bf f } ( z ^ { n } ) . } \end{array}
$$

Thus

$$
\boldsymbol { \phi } _ { \Delta t , \tilde { t } _ { 1 } } ( \boldsymbol { z } ^ { n } ) = \boldsymbol { z } ^ { n } + \Delta t \boldsymbol { f } ( \boldsymbol { z } ^ { n } ) + \mathcal { O } ( \Delta t ^ { 3 } ) ,
$$

and comparison with (5.5) shows that the Euler method is a second-order discretization of the modified differential equation (5.6). This procedure can be continued. We make the ansatz

$$
\tilde { f } _ { i } ( z ; \Delta t ) = f ( z ) + \Delta t \delta f _ { 1 } ( z ) + \Delta t ^ { 2 } \delta f _ { 2 } ( z ) + . . . + \Delta t ^ { i } \delta f _ { i } ( z ) ,
$$

with $\delta { \pmb f } _ { 1 } ( z ) = - ( 1 / 2 ) { \pmb f } ^ { \prime } ( z ) { \pmb f } ( z )$ . As for the modification $\delta f _ { 1 }$ , the functions $\delta f _ { j }$ , $j = 2 , \dots , i$ , are obtained by computing the Taylor series expansion of the flow map $\boldsymbol { \phi } _ { t , \tilde { f } _ { i } }$ and choosing the modified differential equation2 such that

$$
\begin{array} { r } { \Phi _ { t = \Delta t , \tilde { t _ { i } } } ( z ^ { n } ) = z ^ { n } + \Delta t f ( z ^ { n } ) + \mathcal { O } ( \Delta t ^ { i + 2 } ) . } \end{array}
$$

Hence Euler’s method can be viewed as a discretization of order $p = i + 1$ for the modified differential equation (5.7). If we assume for the moment that we can increase the index $j$ to infinity and that the limit is well defined, then we may take $\tilde { \pmb { f } } ( \Delta t ) : = \tilde { \pmb { f } } _ { i = \infty } ( \Delta t )$ in (5.4) and the Euler method would be the exact solution to the modified differential equation (5.4) at $t = \Delta t$ , i.e.

$$
\pmb { \psi } _ { \Delta t } ( z ) = \pmb { \phi } _ { \Delta t , \tilde { t } } ( z ) .
$$

This equation is the equivalent to the backward error equation (5.1) for Gaussian elimination.

It is important to keep in mind that backward error analysis requires that the stepsize $\Delta t$ is kept constant. Otherwise different modified differential equations are obtained at each integration step and the numerical method cannot be considered as the “exact” solution of a single modified differential equation.

Let us return to general numerical one-step methods of order $p \geq 1$ . Ideally, we would like to find a modified differential equation (5.4) such that

(i) the modified vector field $\tilde { \pmb { f } } ( \Delta t )$ is close to the given vector field $\boldsymbol { f }$ , i.e.,

$$
\begin{array} { r } { | | \pmb { f } ( z ) - \tilde { \pmb { f } } ( z ; \Delta t ) | | = \mathcal { O } ( \Delta t ^ { p } ) , } \end{array}
$$

$p \geq 1$ the order of the numerical method $\psi _ { \Delta t }$ , and (ii) the numerical computed solutions can be considered as the exact solutions of the modified vector field $\tilde { \pmb { f } } ( \Delta t )$ , i.e., the equality (5.8) holds.3

Let us suppose for the moment that (i) and (ii) can indeed be achieved. We may compare the solution behavior of the modified equation (5.4) to the solutions of the given problem (5.2). In general, not much has been gained yet: the solutions of these two differential equations will, in general, still diverge exponentially fast as the time interval $t _ { n }$ is increased. Backward error analysis becomes useful as soon as one can show that the modified equation shares some qualitative features with the given problem. We will come back to this point in Section 5.1.2.

# 5.1.1 Linear systems

In this section, we focus on linear differential equations

$$
\frac { d } { d t } z = { \bf \cal A } z ,
$$

$z \in \mathbb { R } ^ { k }$ , $\pmb { A } \in \mathbb { R } ^ { k \times k }$ .

While linear differential equations are certainly too special to be of practical relevance, restriction to this class of problems allows us to satisfy condition (5.8) exactly and to present the basic ideas of backward error analysis in a simple context. We have already encountered the basic ingredients in Section 2.6 when we discussed numerical methods for the harmonic oscillator using eigenvalues. Nonlinear problems have to be treated with different techniques and we will come back to them in Section 5.2.

The general solution of a linear equation (5.9) can be obtained in the following manner. We make the ansatz

$$
\boldsymbol { z } ( t ) = \mathsf { R e } \{ \boldsymbol { v } \boldsymbol { \mathrm { e } } ^ { \lambda t } \} ,
$$

where $\pmb { v } \in \mathbb { C } ^ { k }$ is a complex-valued vector, $\lambda \in \mathbb { C }$ is a complex number, and $\mathsf { R e } \left( z \right)$ denotes the real part of a complex number $Z$ . Upon substituting this trial solution into the equation (5.9), we obtain the algebraic condition

$$
\mathsf { R e } \left\{ \left[ \pmb { A } - \lambda \pmb { I } _ { k } \right] \pmb { v } \mathrm { e } ^ { \lambda t } \right\} = \mathbf { 0 } .
$$

Since this equation has to hold for all $t$ , we have to have

$$
\left[ \pmb { A } - \lambda \pmb { I } _ { k } \right] \pmb { v } = \pmb { 0 } ,
$$

and, hence, $\lambda$ is an eigenvalue of $\pmb { A }$ and $\pmb { v }$ an associated eigenvector. Denote the set of eigenvalues of $\pmb { A }$ by $\lambda _ { j }$ , $i = 1 , \ldots , k$ , with associated eigenvectors $\pmb { v } _ { j }$ , then the general solution of (5.9) can be represented as4

$$
z ( t ) = \sum _ { i } { \mathsf { R e } } \left\{ c _ { i } { \pmb v } _ { i } \mathrm { e } ^ { \lambda _ { i } t } \right\} ,
$$

where $C _ { I }$ , $i = 1 , \dots , k$ , are complex numbers determined by the initial condition $z ( 0 ) = z _ { 0 }$ , i.e.,

$$
z _ { 0 } = \sum _ { i } { \mathsf { R e } } \{ c _ { i } \ : v _ { i } \} .
$$

4Here we have assumed, for simplicity, that all eigenvalues are distinct from each other and the eigenvectors form a complete basis in Rk .

Example 1Let us discuss the harmonic oscillator

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } q = \omega p , } \\ { \displaystyle \frac { d } { d t } p = - \omega q , } \end{array}
$$

with frequency $\omega > 0$ . The associated matrix

$$
\pmb { A } = \left[ \begin{array} { c c } { 0 } & { \omega } \\ { - \omega } & { 0 } \end{array} \right]
$$

has eigenvalues $\lambda _ { 1 / 2 } = \pm i \omega$ and (normalized) eigenvectors

$$
v _ { 1 } = { \frac { 1 } { \sqrt 2 } } \left[ { - i \atop 1 } \right] , \qquad v _ { 2 } = { \frac { 1 } { \sqrt 2 } } \left[ { 1 \atop - i } \right] .
$$

The general solution can be written as

$$
q ( t ) = c _ { 1 } \mathsf { R e } \{ - i \mathsf { e } ^ { i \omega t } \} + c _ { 2 } \mathsf { R e } \{ \mathsf { e } ^ { - i \omega t } \} = c _ { 1 } \mathsf { S i n } ( \omega t ) + c _ { 2 } \mathsf { C o s } ( \omega t ) ,
$$

and

$$
p ( t ) = c _ { 1 } \mathsf { R e } \left\{ \mathsf { e } ^ { i \omega t } \right\} + c _ { 2 } \mathsf { R e } \left\{ - i \mathsf { e } ^ { - i \omega t } \right\} = c _ { 1 } \mathsf { c o s } ( \omega t ) - c _ { 2 } \mathsf { s i n } ( \omega t ) ,
$$

where $c _ { 1 } = p ( 0 )$ and $c _ { 2 } = q ( 0 )$ .

Let us return to numerical approximations of (5.9). Any one-step method discussed in Chapters 2 and 4 will lead to a discretization of type (see Section 2.6)

$$
\begin{array} { r } { z ^ { n + 1 } = \pmb { \psi } _ { \Delta t } ( z ^ { n } ) , } \\ { = \widehat { R } ( \Delta t ) z ^ { n } . } \end{array}
$$

Here $\widehat { R } ( \Delta t )$ is a $k \times k$ matrix depending on the stepsize $\Delta t$ . To be able to relate the numerical solutions $z ^ { n }$ back to the analytic solution, we write

$$
z ^ { n } = \mathsf { R e } \{ \pmb { u } \mathrm { e } ^ { \tilde { \lambda } t _ { n } } \} , \qquad t _ { n } = { n } \cdot \Delta t ,
$$

and obtain the algebraic condition

$$
\left[ \widehat { R } ( \Delta t ) - \mu I _ { k } \right] \pmb { u } = \mathbf { 0 }
$$

for $\pmb { u }$ and

$$
\boldsymbol { \mu } = \mathrm { e } ^ { \tilde { \lambda } \Delta t } .
$$

Hence, for any fixed value of $\Delta t$ , we have to find all eigenvectors $\pmb { u } _ { j }$ and eigenvalues $\mu _ { i } , i = 1 , \ldots , k$ , of the matrix $\widehat { R } ( \Delta t )$ . Then the numerical approximation

$z ^ { n }$ is given by

$$
z ^ { n } = \sum _ { j } \mathsf { R e } \{ d _ { i } { \pmb u } _ { i } \mu _ { i } ^ { n } \} = \sum _ { j } \mathsf { R e } \{ d _ { i } { \pmb u } _ { i } \mathrm { e } ^ { \tilde { \lambda } _ { i } t _ { n } } \} ,
$$

with

$$
\tilde { \lambda } _ { i } = \frac { 1 } { \Delta t } \ln \mu _ { i } ,
$$

and the complex numbers $d _ { i }$ are determined by the initial $z ^ { 0 } = z ( 0 )$ .

Example 2The explicit Euler method,applied to (5.9), leads to

$$
\widehat { \pmb { R } } ( \Delta t ) = \pmb { I } _ { k } + \Delta t \pmb { A } .
$$

It is easy to verify that an eigenvector $\pmb { v }$ of the matrix $\pmb { A }$ is also an eigenvector of $\widehat { R } ( \Delta t )$ , i.e. $v = u$ . This observation leads immediately to

$$
\mu _ { i } = 1 + \Delta t \lambda _ { i } ,
$$

where $\lambda _ { j }$ is an eigenvalue of $\pmb { A }$ . More generally, any (non-partitioned) Runge–Kutta (RK) method (see Section 2.4) leads to a matrix $\widehat { R } ( \Delta t )$ which has a set of eigenvectors identical to that of $\pmb { A }$ . Hence $\mu$ is equal to a rational polynomial in $\lambda$ . For example, the implicit midpoint rule leads to

$$
\mu _ { i } = \frac { 1 + ( \Delta t / 2 ) \lambda _ { i } } { 1 - ( \Delta t / 2 ) \lambda _ { i } } .
$$

Let us apply these formulas to the harmonic oscillator (5.10)–(5.11). The explicit Euler method yields

$$
\mu _ { 1 / 2 } = 1 \pm i \omega \Delta t = r \mathrm { e } ^ { \pm i \tilde { \omega } \Delta t } ,
$$

where

$$
r = \sqrt { 1 + ( \omega \Delta t ) ^ { 2 } } , ~ \tilde { \omega } = \frac { \tan ^ { - 1 } ( \omega \Delta t ) } { \Delta t } .
$$

This expression has to be compared with $\mathrm { e } ^ { \pm i \omega \Delta t }$ . We see that the numerical solutions grow in magnitude since $r > 1$ and that there is a shift in phase since $\tilde { \omega } < \omega$ . On the other hand, the implicit midpoint rule leads to $r = 1$ and

$$
\tilde { \omega } = \frac { 2 } { \Delta t } \tan ^ { - 1 } \left( { \omega \Delta t } / { 2 } \right) .
$$

Hence, the numerical solutions have constant magnitude but there is still a shift in phase, i.e., $\tilde { \omega } < \omega$ . ✷

We now give (5.13) a time-continuous interpretation, i.e.,

$$
\boldsymbol { z } ( t ) = \sum _ { i } \mathsf { R e } \left\{ d _ { i } \boldsymbol { u } _ { i } \mathrm { e } ^ { \tilde { \lambda } _ { i } t } \right\} ,
$$

and develop the modified equation corresponding to the scheme (5.12). For a fixed value of $\Delta t$ , denote the matrix of eigenvectors $\pmb { u } _ { j }$ of $\widehat { R } ( \Delta t )$ by ${ \cal U } ( \Delta t )$ and the diagonal matrix of eigenvalues $\mu _ { j }$ by $M ( \Delta t )$ . Then, upon dropping the stepsize dependence of all matrices involved, the identity

$$
\widehat { \pmb { R } } = { \pmb { U } } { \pmb { M } } { \pmb { U } } ^ { - 1 }
$$

is obtained, which leads to the matrix

$$
{ \tilde { \pmb { A } } } : = { \pmb { U } } { \pmb { \Lambda } } { \pmb { U } } ^ { - 1 } ,
$$

where $\pmb { \Lambda }$ is a diagonal matrix with its diagonal entries equal to $\tilde { \lambda } _ { j }$ . Indeed, since

$$
\mathrm { e } ^ { t \tilde { A } } | _ { t = n \Delta t } = U \mathrm { e } ^ { n \Delta t \Lambda } U ^ { - 1 } = U \left[ \mathrm { e } ^ { \Delta t A } \right] ^ { n } U ^ { - 1 } = U \left[ M \right] ^ { n } U ^ { - 1 } = \left[ \widehat { R } \right] ^ { n } ,
$$

we can conclude that (5.12) can be viewed as the exact solution of the modified linear differential equation

$$
\frac { d } { d t } z = \tilde { \pmb { A } } ( \Delta t ) z
$$

sampled at time intervals $\Delta t$

Example 3 Let us apply a general Runge-Kutta method to the harmonic oscillator (5.10)–(5.11). We write

$$
\mu _ { 1 / 2 } = r \mathrm { e } ^ { \pm i \tilde { \omega } \Delta t } ,
$$

with both $\tilde { \omega }$ and $r$ depending on $\Delta t$ . Then the modified differential equation is of the form

$$
\frac { d } { d t } z = \tilde { \omega } ( \Delta t ) J z + \frac { \log r ( \Delta t ) } { \Delta t } z ,
$$

and, hence

$$
\tilde { \pmb { A } } ( \Delta t ) : = \tilde { \omega } ( \Delta t ) \pmb { J } + \frac { \log r ( \Delta t ) } { \Delta t } \pmb { I } _ { 2 } .
$$

The harmonic oscillator has energy

$$
H = { \frac { \omega } { 2 } } \left[ q ^ { 2 } + p ^ { 2 } \right] .
$$

If we evaluate the energy along solutions of the modified equations, then we obtain

$$
\frac { d } { d t } H = \frac { 2 \log r ( \Delta t ) } { \Delta t } H .
$$

Hence a RK method conserves energy if and only if $r ( \Delta t ) = 1$ . This is the case for all Gauss–Legendre $\mathsf { R K }$ methods, which also happen to be symplectic. In fact, a Gauss–Legendre RK method, applied to the harmonic oscillator (5.10)–(5.11), can be thought of as the exact solution to a modified harmonic oscillator (Hamiltonian system) with modified Hamiltonian

$$
\tilde { \cal H } = { \frac { \tilde { \omega } ( \Delta t ) } { 2 } } \left[ q ^ { 2 } + p ^ { 2 } \right] ,
$$

i.e. a harmonic oscillator with frequency $\tilde { \omega } ( \Delta t )$

This last example showed that the modified equation (5.15) may inherit the Hamiltonian structure of the given equations of motion provided a proper discretization is used. In particular, for the harmonic oscillator, the symplectic Gauss–Legendre RK methods conserve energy exactly and can be viewed as exact solutions to a “modified” harmonic oscillator. In the following section we will explore the relation of symplectic methods and conservation of energy in the context of general nonlinear Hamiltonian systems before presenting more detailed results in Section 5.2.

# 5.1.2 The nearby Hamiltonian

Let us suppose that (5.2) is a Hamiltonian differential equation, then it would be desirable that the modified vector field $\tilde { \pmb { f } } ( \Delta t )$ is also Hamiltonian with modified Hamiltonian function $\tilde { H } ( \Delta t )$ . As we will discuss in more detail in Section 5.2, symplectic integration methods indeed give rise to modified differential equations that are Hamiltonian. In particular:

(i) the modified Hamiltonian $\tilde { H } ( \Delta t )$ is close to the originally given Hamiltonian $H$ , i.e.

$$
\mid \tilde { H } ( z ; \Delta t ) - H ( z ) \mid = \mathcal { O } ( \Delta t ^ { p } ) ,
$$

$p \geq 1$ the order of the method, and

$$
\tilde { \pmb { f } } ( \boldsymbol { z } ; \Delta t ) = \pmb { J } \nabla _ { \boldsymbol { z } } \tilde { H } ( \boldsymbol { z } ; \Delta t ) .
$$

The connection between symplectic integration methods and Hamiltonian modified equations has, for example, been explored in the work of AUERBACH AND FRIEDMAN [12], FENG [59], SANZ-SERNA [171], and YOSHIDA [206]. A more systematic treatment has, for example, been given by HAIRER [77], REICH [153], BENETTIN AND GIORGILLI [16], TANG [191], and CALVO, MURUA, AND SANZ-SERNA [40].

Thus a symplectic integrator solves a slightly perturbed Hamiltonian problem “exactly.” If the qualitative solution behavior of the given problem is “stable” under small perturbations of the Hamiltonian, then, roughly speaking, a symplectic method will reproduce this qualitative solution behavior. Examples of such instances will be discussed in Section 5.2.3. On the other hand, non-symplectic methods, for which the modified vector field is not Hamiltonian, will change the qualitative solution behavior of a Hamiltonian problem in a significant way. In terms of the dynamics at equilibria for example, a non-Hamiltonian perturbation may change stable centers into sources or sinks.

Let us have a closer look at the explicit Euler method and the symplectic Euler-A method (4.8)–(4.9) from Section 4.1 when applied to Hamiltonian differential equations

$$
\begin{array} { l } { { \displaystyle { \frac { d } { d t } } { \pmb q } = { \pmb M } ^ { - 1 } { \pmb p } } , \ } \\ { { \displaystyle { \frac { d } { d t } } { \pmb p } = - \nabla _ { \pmb q } V ( { \pmb q } ) . } \ } \end{array}
$$

According to the general formula (5.6), the explicit Euler method gives rise to a modified system (5.7) with the first-order modification given by

$$
\begin{array} { l } { { \displaystyle \delta f _ { 1 } ( \boldsymbol { q } , \boldsymbol { p } ) = - \frac { 1 } { 2 } \left[ \begin{array} { c c } { { \bf 0 } } & { { \cal M } ^ { - 1 } } \\ { { - \cal V } _ { \boldsymbol { q } \boldsymbol { q } } ( \boldsymbol { q } ) } & { { \bf 0 } } \end{array} \right] \left[ \begin{array} { c } { { \cal M } ^ { - 1 } { \boldsymbol { p } } } \\ { { - \nabla _ { \boldsymbol { q } } \boldsymbol { V } } ( \boldsymbol { q } ) } \end{array} \right] , } } \\ { { \displaystyle ~ = \frac { 1 } { 2 } \left[ \begin{array} { c } { { \cal M } ^ { - 1 } \nabla _ { \boldsymbol { q } } \boldsymbol { V } ( \boldsymbol { q } ) } \\ { { \cal V } _ { \boldsymbol { q } \boldsymbol { q } } ( \boldsymbol { q } ) { \cal M } ^ { - 1 } \boldsymbol { p } } \end{array} \right] . } } \end{array}
$$

This vector field is not conservative. Next we consider the symplectic Euler-A method

$$
\begin{array} { l } { { { \pmb q } ^ { n + 1 } = { \pmb q } ^ { n } + \Delta t { \pmb M } ^ { - 1 } { \pmb p } ^ { n } , } } \\ { { { \pmb p } ^ { n + 1 } = { \pmb p } ^ { n } - \Delta t \nabla _ { \pmb q } V ( { \pmb q } ^ { n + 1 } ) . } } \end{array}
$$

Taylor expansion of the second equation yields

$$
\pmb { p } ^ { n + 1 } = \pmb { p } ^ { n } - \Delta t \nabla _ { q } V ( \pmb { q } ^ { n } ) - \Delta t ^ { 2 } V _ { q q } ( \pmb { q } ^ { n } ) \pmb { M } ^ { - 1 } \pmb { p } ^ { n } + \pmb { \mathcal { O } } ( \Delta t ^ { 3 } ) .
$$

If we compare this with the Taylor series expansion of the exact time- $\Delta t$ -flow map, then we obtain the first-order modification

$$
\delta f _ { 1 } ( \pmb { q } , \pmb { p } ) = \frac { 1 } { 2 } \left[ \begin{array} { c } { { { \cal M } ^ { - 1 } \nabla _ { \pmb { q } } { \cal V } ( \pmb { q } ) } } \\ { { - { \cal V } _ { \pmb { q } \pmb { q } } ( \pmb { q } ) { \cal M } ^ { - 1 } \pmb { p } } } \end{array} \right]
$$

in the expansion (5.7). This term is conservative and can be written as

$$
\delta f _ { 1 } ( q , p ) = \left[ { + \nabla _ { p } \delta H _ { 1 } ( q , p ) } \right] , \quad \mathrm { w i t h } \quad \delta H _ { 1 } : = \frac { 1 } { 2 } p ^ { T } M ^ { - 1 } \nabla _ { q } V ( q ) .
$$

Thus the symplectic Euler-A method is a second-order integrator for a modified Hamiltonian system with Hamiltonian

$$
\tilde { H } _ { 1 } ( \Delta t ) = \frac { \pmb { p } ^ { T } \pmb { M } ^ { - 1 } \pmb { p } } { 2 } + V ( \pmb { q } ) + \frac { \Delta t } { 2 } \pmb { p } ^ { T } \pmb { M } ^ { - 1 } \nabla _ { \pmb { q } } V ( \pmb { q } ) .
$$

Example 4Let us consider the reduced Kepler problem

$$
\frac { d } { d t } r = p _ { r } , \quad \frac { d } { d t } p _ { r } = \frac { I ^ { 2 } } { r ^ { 3 } } - \frac { m _ { 3 } } { r ^ { 2 } }
$$

with Hamiltonian

$$
H ( r , p _ { r } ) = { \frac { 1 } { 2 } } p _ { r } ^ { 2 } + { \frac { I ^ { 2 } } { 2 r ^ { 2 } } } - { \frac { m _ { 3 } } { r } } .
$$

Here $r > 0$ is the distance of the planet to the origin (“sun”) and $m _ { 3 }$ is the (constant) angular momentum of the planet. We discretize the equations of motion by the Euler-A method and obtain

$$
r ^ { n + 1 } = r ^ { n } + \Delta t p _ { r } ^ { n } , \quad p _ { r } ^ { n + 1 } = p _ { r } ^ { n } - \Delta t \left[ \frac { m _ { 3 } } { ( r ^ { n + 1 } ) ^ { 2 } } - \frac { I ^ { 2 } } { ( r ^ { n + 1 } ) ^ { 3 } } \right] .
$$

To first order in $\Delta t$ , the associated modified Hamiltonian is

$$
\tilde { H } _ { 1 } ( r , p _ { r } ; \Delta t ) = H ( r , p _ { r } ) + \frac { \Delta t } { 2 } \left[ \frac { m _ { 3 } } { r ^ { 2 } } - \frac { I ^ { 2 } } { r ^ { 3 } } \right] p _ { r } .
$$

![](images/d98d11b8b1399f45722831a299b6ee2830ac50b6a5568db29da86f4b4165d9d2.jpg)  
Figure 5.1 Maximum error in the energy with respect to the Hamiltonian $H$ (o) and the modified Hamiltonian $\tilde { H } _ { 1 } ( \Delta t ) \ ( \times )$ as a function of the stepsize $\Delta t$ .

In Fig. 5.1, we plot the error in energy along numerically computed trajectories w.r.t. the Hamiltonian $H$ and the modified Hamiltonian $\tilde { H } _ { 1 } ( \Delta t )$ . The initial conditions $( r , p _ { r } ) = ( 1 , 0 . 5 )$ were used while the stepsize was chosen from $\Delta t \in [ 0 . 0 1 ,$ 0.1]. It can be seen that the numerical solution converges with first order in $\Delta t$ to $H = c o n s t$ . and with second order to $\tilde { H } _ { 1 } ( \Delta t ) = c o n s t .$ ., as predicted. An important point is that both $H$ and $\tilde { H } _ { 1 } ( \Delta t )$ possess the same qualitative solution behavior, i.e. the solutions are periodic. Its shape and period are, of course, different for the exact solution and its numerical approximation. This can be seen from Fig. 5.2. Note that the modified

![](images/72298448d18446312d71f707235722d27e1b01b4a8497899dc9b28c0bf9f2396.jpg)  
Figure 5.2 The numerical solution for $\Delta t = 0 . 2 \ ( \times )$ as compared with the exact solution of the Kepler problem and the exact solution of the modified problem with Hamiltonian $\tilde { H } _ { 1 } ( \Delta t = 0 . 2 )$ .

Hamiltonian equations are

$$
\frac { d } { d t } r = p _ { r } + \frac { \Delta t } { 2 } \left[ \frac { m _ { 3 } } { r ^ { 2 } } - \frac { I ^ { 2 } } { r ^ { 3 } } \right] , \quad \frac { d } { d t } p _ { r } = \frac { c ^ { 2 } } { q ^ { 3 } } - \frac { m _ { 3 } } { r ^ { 2 } } + p _ { r } \frac { \Delta t } { 2 } \left[ \frac { 2 } { r ^ { 3 } } - \frac { 3 I ^ { 2 } } { r ^ { 4 } } \right] .
$$

# 5.2 The modified equations

In this section, we examine in more detail the development of the modified equations and discuss their geometric properties in the context of Hamiltonian dynamics and symplectic integration.

# 5.2.1 Asymptotic expansion of the modified equations

Let us return to the formal expansion (5.7) of the modified vector field $\tilde { \pmb { f } } _ { i } ( \Delta t )$ . The correcting vector fields $\delta f _ { j }$ , $j = 1 , \dots , i$ , are determined by Taylor series expansion of the flow map $\pmb { \phi } _ { t = \Delta t , \tilde { \pmb { f } } _ { i } }$ and the numerical method $\psi _ { \Delta t }$ in terms of $\Delta t$ and by matching the first $j + 1$ terms in the two expansions. Here we describe a somewhat more abstract recursive approach [158]. Let us assume that a modified vector field $\tilde { \pmb { f } } _ { i } ( \Delta t )$ has been found such that the numerical method $\psi _ { \Delta t }$ is an integrator of order $p = i + 1$ with respect to this modified differential equation, i.e., the flow map $\pmb { \phi } _ { t , \tilde { f } _ { i } } ( z )$ satisfies

$$
\pmb { \phi } _ { \Delta t , \tilde { t } _ { i } } ( z ) - \pmb { \psi } _ { \Delta t } ( z ) = \mathscr { O } ( \Delta t ^ { i + 2 } ) .
$$

Then we define

$$
\delta { \pmb f } _ { i + 1 } ( z ) = \operatorname* { l i m } _ { \tau  0 } \frac { \pmb { \psi } _ { \tau } - \pmb { \phi } _ { \tau , \tilde { \pmb f } _ { i } ( \tau ) } ( z ) } { \tau ^ { i + 2 } } ,
$$

and introduce a new modified vector field $\tilde { \pmb { f } } _ { i + 1 } ( \Delta t )$ by

$$
\tilde { \pmb { f } } _ { i + 1 } ( \Delta t ) : = \tilde { \pmb { f } } _ { i } ( \Delta t ) + \Delta t ^ { i + 1 } \pmb { \delta } \pmb { f } _ { i + 1 } .
$$

This numerical method $\psi _ { \Delta t }$ is now a method of order $p = i + 2$ with respect to the new modified vector field $\tilde { \pmb { f } } _ { i + 1 } ( \Delta t )$ as can be seen from

$$
\begin{array} { r l } & { \boldsymbol { \phi } _ { \Delta t , \tilde { t } _ { i + 1 } } ( z ) - \boldsymbol { \psi } _ { \Delta t } ( z ) = \boldsymbol { \phi } _ { \Delta t , \tilde { t } _ { i } } ( z ) + \Delta t ^ { i + 2 } \delta { { f } _ { i + 1 } } ( z ) + \mathcal { O } ( \Delta { { t } ^ { i + 3 } } ) - \boldsymbol { \psi } _ { \Delta t } ( z ) } \\ & { \qquad = \Delta t ^ { i + 2 } \delta { { f } _ { i + 1 } } ( z ) + \boldsymbol { \phi } _ { \Delta t , \tilde { t } _ { i } } ( z ) - \boldsymbol { \psi } _ { \Delta t } ( z ) + \mathcal { O } ( \Delta { { t } ^ { i + 3 } } ) } \\ & { \qquad = \mathcal { O } ( \Delta { { t } ^ { i + 3 } } ) . } \end{array}
$$

The recursion is started with $\tilde { \pmb { f } } _ { 0 } : = { \pmb f }$ . For a method of order $p \geq 2$ , the first $p - 1$ vector fields $\delta f _ { j }$ are identical zero.

Unfortunately, this series does not, in general, converge as $i  \infty$ , i.e., the recursion (5.18)–(5.19) yields only an asymptotic expansion. Estimates for the difference between the flow maps of the modified equations and the numerical method are available if the involved maps are real analytic and bounded on an open (complex) neighborhood of a compact subset ${ \mathcal { K } } \subset \mathbb { R } ^ { k }$ of phase space. In particular, BENETTIN AND GIORGILLI [16], HAIRER AND LUBICH [79], and REICH [158], using different techniques, derive an estimate of type

$$
| | \pmb { \psi } _ { \Delta t } ( z ) - \pmb { \phi } _ { \Delta t , \tilde { t } _ { i } } ( z ) | | \leq c _ { 1 } \Delta t ( c _ { 2 } ( i + 1 ) \Delta t ) ^ { i + 1 } ,
$$

for all $z \in \kappa$ , where $c _ { 1 } , c _ { 2 } > 0$ are appropriate constants independent of the iteration index $j$ and the stepsize $\Delta t$ . This formula indicates that the sequence of modified vector fields $\tilde { \pmb { f } } _ { i } ( \Delta t )$ converges before it starts to diverge for larger values

![](images/423dcec0e17e55e3ebc9a290255ef967ec4721d6e4a995ff1c17f81a9724e8e2.jpg)  
Figure 5.3 The function $f ( i ) = ( i \Delta t ) ^ { i }$ plotted for $\Delta t = 0 . 1$ $( + )$ , $\Delta t = 0 . 0 1$ (o), and $\Delta t = 0 . 0 0 1$ ( ) in the range $f ( j ) \leq 1$ .

of $j$ ( $\Delta t$ fixed). The point of divergence is shifted to larger and larger values of $j$ as $\Delta t \to 0$ . See Fig. 5.3 for an illustration.

Set $j _ { * }$ equal the integer part of

$$
s ( \Delta t ) : = \frac { 1 } { c _ { 2 } e \Delta t } - 1 .
$$

This choice implies

$$
\begin{array} { r } { c _ { 2 } \big ( i _ { * } + 1 \big ) \Delta t < c _ { 2 } \big ( s + 1 \big ) \Delta t = e ^ { - 1 } , } \end{array}
$$

$$
j _ { * } + 1 > s ,
$$

and, hence, makes the expression on the right-hand side of (5.20) exponentially small in the stepsize $\Delta t$ :

$$
\begin{array} { r l } & { \lvert | \pmb { \psi } _ { \Delta t } ( z ) - \pmb { \phi } _ { \Delta t , \tilde { t } _ { i _ { * } } } ( z ) \rvert | \leq c _ { 1 } \Delta t e ^ { - i _ { * } - 1 } } \\ & { \qquad \leq c _ { 1 } \Delta t e ^ { - s } } \\ & { \qquad \leq 3 c _ { 1 } \Delta t e ^ { - \gamma / \Delta t } , } \end{array}
$$

with $\gamma = 1 / { \left( c _ { 2 } e \right) }$ . The modified differential equation is now defined by

$$
\frac { d } { d t } z = \tilde { \pmb { f } } ( z ; \Delta t ) : = \tilde { \pmb { f } } _ { i _ { * } } ( z ; \Delta t ) .
$$

Following standard forward error analysis (see Sections 2.1.2 and 2.3), the difference of the exact solution $z ( t _ { n } )$ of the modified differential equation (5.22) and the numerical computed $z ^ { n }$ at $t = t _ { n }$ is bounded by

$$
| | z ( t _ { n } ) - z ^ { n } | | \leq K \left( e ^ { t _ { n } \bar { L } } - 1 \right) e ^ { - \gamma / \Delta t } ,
$$

$K > 0$ an appropriate constant and $\bar { L } > 0$ the Lipschitz constant of the numerical method as introduced in Section 2.3. In contrast to forward error analysis with respect to the given differential equation, this term remains (exponentially) small over periods of time

$$
t _ { n } \ll \frac { \gamma } { \Delta t \bar { L } }
$$

[79]. Often this time interval is still not long enough, and more sophisticated error concepts, such as shadowing [76, 173] have to be used in addition to backward error analysis.

# 5.2.2 Conservation of energy for symplectic methods

If a Hamiltonian differential equation

$$
\frac { d } { d t } z = J \nabla _ { z } H ( z )
$$

is discretized by a symplectic method, then the modified vector fields $\tilde { \pmb { f } } _ { i } ( \Delta t )$ are Hamiltonian,5 i.e., there exists a Hamiltonian $\tilde { H } _ { i } ( \Delta t )$ such that

$$
\frac { d } { d t } z = \tilde { f } _ { i } ( z ; \Delta t ) = J \nabla _ { z } \tilde { H } _ { i } ( z ; \Delta t ) .
$$

A proof of this result will be given in Section 5.3.

In case all the involved functions and maps are real analytic and bounded, the difference between the numerical method $\psi _ { \Delta t }$ and the flow map $\pmb { \phi } _ { \Delta t , \tilde { \pmb { f } } }$ of an optimally truncated modified equation (5.22) can be made exponentially small, i.e., an estimate (5.21) holds. Let us denote the corresponding Hamiltonian by $\tilde { H } ( \Delta t )$ . For a symplectic method of order $p \geq 1$ , we have

$$
H ( z ) - \tilde { H } ( z ; \Delta t ) = \mathcal { O } ( \Delta t ^ { p } ) .
$$

Let us now investigate the conservation of the modified Hamiltonian $\tilde { H } ( \Delta t )$ along numerically computed solutions. After $n$ steps, we obtain:

$$
\begin{array} { r l r } {  { | \tilde { H } ( z ^ { n } ; \Delta t ) - \tilde { H } ( z ^ { 0 } ; \Delta t ) | \leq \sum _ { i = 1 } ^ { n } | \tilde { H } ( z ^ { i } ; \Delta t ) - \tilde { H } ( z ^ { i - 1 } ; \Delta t ) | } } \\ & { } & { \leq \displaystyle \sum _ { i = 1 } ^ { n } | \tilde { H } ( \psi _ { \Delta t } ( z ^ { i - 1 } ) ; \Delta t ) - \tilde { H } ( \phi _ { \Delta t , \tilde { t } } ( z ^ { i - 1 } ) ; \Delta t ) | } \\ & { } & { \leq \displaystyle \sum _ { i = 1 } ^ { n } \lambda | | \psi _ { \Delta t } ( z ^ { i - 1 } ) - \phi _ { \Delta t , \tilde { t } } ( z ^ { i - 1 } ) | | } \\ & { } & { < 3 \lambda n \Delta t c _ { 1 } e ^ { - \gamma / \Delta t } , } \end{array}
$$

$\lambda > 0$ the Lipschitz constant of $\tilde { H } ( \Delta t )$ . Here we have used the estimate (5.21) and the fact that $\tilde { H } ( \Delta t )$ is a first integral of the modified vector field $\tilde { \pmb { f } } ( \Delta t )$ which implies that

$$
\begin{array} { r } { \tilde { H } ( z ^ { i - 1 } ; \Delta t ) = \tilde { H } ( \Phi _ { \Delta t , \tilde { t } } ( z ^ { i - 1 } ) ; \Delta t ) . } \end{array}
$$

Thus the drift in the energy $\tilde { H } ( \Delta t )$ remains exponentially small over exponentially long time intervals

$$
t _ { N } = n \cdot \Delta t \leq e ^ { \gamma / ( 2 \Delta t ) } .
$$

This estimate and (5.25) imply the conservation of the given Hamiltonian $H$ over an exponentially long period of time up to terms of order $\Delta t ^ { p }$ . This result was first mentioned by NEISHTADT [143]. Explicit proofs can be found in the papers by BENETTIN AND GIORGILLI [16], HAIRER AND LUBICH [79], and REICH [158]

Example 5 The following experiment to illustrate the superior conservation of energy by a symplectic method follows an idea first used by BENETTIN AND GIORGILLI [16]. Consider the following one degree-of-freedom system

$$
\dot { q } = p , \qquad \dot { p } = - V ^ { \prime } ( q ) , \qquad V ( q ) = e ^ { - q ^ { 2 } / 2 } .
$$

For $| q |$ sufficiently large, e.g., $| q | > 2 0$ , the force $F ( q ) = - V ^ { \prime } ( q )$ will be below machine precision in a standard double precision computation. Hence any numerical method will be essentially exact in that region of phase space and the modified equations can be identified with $\dot { q } = p , \ \dot { p } = 0$ . Let us now perform a sequence of experiments with initial values $q ( 0 ) \ = \ - 2 0$ , $p ( 0 ) = 1$ . We compute the solution up to the point where $| q ( t ) | > 2 0$ again. Now recall that we may assume that $\tilde { \cal H } = { \cal H } = p ^ { 2 } / 2$ for $| q | > 2 0$ . Hence we measure the change in energy from its initial to its final value, which gives us precisely the drift in energy due to the non-exact nature of backward error analysis. The numerically computed drift in the energy compared to the “fitted” exponential function $1 5 0 e ^ { - 1 1 . 8 / \Delta t }$ can be found in Fig. 5.4. ✷

![](images/a6ba777ac90b612a6a2b33f9b10e62a884fc217ab20207fa4458fdcb7686f32c.jpg)  
Figure 5.4 Demonstration of the exponential decay in the energy drift as $\Delta t \to 0$ for a simple one-dimensional collision problem.

The nearly exact conservation of a modified Hamiltonian $\tilde { H }$ has an interesting consequence in relation to exact conservation of energy. Following essentially the argument of GE AND MARSDEN [69], we assume that (5.23) does not possess any first integrals other than functions of the Hamiltonian $H$ . By backward error analysis, there is a modified Hamiltonian $\tilde { H } ( \Delta t )$ such that a symplectic method is the “exact” time- $\Delta t$ -flow map corresponding to (5.24). If one would insist that the symplectic method also exactly conserves the Hamiltonian $H$ , then one would obtain that the Poisson bracket of $H$ and $\tilde { H } ( \Delta t )$ is identically zero, i.e.

$$
\{ H , \tilde { H } ( \Delta t ) \} = 0 .
$$

This relation together with the assumption that $H$ has no first integral except functions of $H$ implies that the modified Hamiltonian has to be of the form

$$
\tilde { H } ( z ; \Delta t ) = \rho ( H ( z ) ; \Delta t ) ,
$$

where $\rho$ is some function of $H$ and possibly $\Delta t$ . However, this has the implication that, on level sets of constant energy $E = H$ , the modified vector field is equivalent to the given vector field up to a multiplication by the constant factor $\rho ^ { \prime } ( E ; \Delta t )$ . Hence,

$$
\pmb { \psi } _ { \Delta t } = \pmb { \phi } _ { \rho ^ { \prime } \Delta t , H } ,
$$

up to terms exponentially small in $\Delta t$ and our symplectic and energy conserving method would solve the given Hamiltonian problem “exactly” up to a rescaling

of time. This will be impossible, in general, and therefore exact conservation of energy and symplecticness are conflicting issues.

# 5.2.3 Applications

Let us now give a very brief outline of how backward error analysis and the existence of a modified Hamiltonian problem can guide us in understanding the numerical behavior of symplectic integration methods. We first consider the two extreme ends of possible solution behavior: (i) completely integrable and (ii) hyperbolic, i.e. fully chaotic. Finally, we briefly discuss the behavior of an adiabatic invariant under symplectic discretization.

# Integrable systems

Let us assume that our given Hamiltonian system (5.23) can be, at least formally, transformed to a new set of canonical variables $( \mathsf { I } , \phi )$ and that the transformed Hamiltonian takes the simple form $H _ { 0 } ( \mathbf { l } )$ . The associated equations of motion

$$
\frac { d } { d t } \mathbf { I } = \mathbf { 0 } , \qquad \frac { d } { d t } \pmb { \phi } = \nabla _ { | } H _ { 0 } ( \mathbf { I } )
$$

are then solvable and the given problem is called integrable. The variables $( \mathsf { I } , \phi )$ are called action-angle variables [7, 8].

A classical problem in mechanics is the behavior of integrable systems under small perturbations. One is typically led to consider Hamiltonian functions of the form

$$
H ( \mathbf { l } , \pmb { \phi } , \varepsilon ) = H _ { 0 } ( \mathbf { l } ) + \varepsilon H _ { 1 } ( \mathbf { l } , \pmb { \phi } , \varepsilon ) ,
$$

where $\varepsilon > 0$ is small parameter and $H _ { 1 }$ is $2 \pi$ -periodic with respect to all the components in the angle variable $\phi$ . Let us assume that $H _ { 0 }$ is convex in I and that both $H _ { 0 }$ and $H _ { 1 }$ are real-analytic functions. Then the NEKHOROSHEV theorem [144, 116] states that the action variable $\mathsf { I } ( t )$ drifts by no more than terms of order ${ \mathcal O } ( \varepsilon ^ { 1 / 2 n } )$ over an exponentially long time interval $| t | < e ^ { c / \varepsilon ^ { 1 / 2 n } }$ . Here $c > 0$ is some constant and $n$ is the number of degrees of freedom. See [116] for a precise statement of this result and its proof.

Let us now apply a symplectic integrator to an integrable Hamiltonian system of the form (5.23). Note that we do not make use of action-angle variables at this point. Under appropriate conditions, backward error analysis will lead to a modified Hamiltonian

$$
\tilde { H } ( z ) = H ( z ) + \Delta t ^ { p } \delta H ( z , \Delta t ) ,
$$