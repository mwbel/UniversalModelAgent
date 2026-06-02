# Chapter 11. Contact Algorithms for Contact Dynamical Systems

An odd-dimensional manifold cannot admit a symplectic structure. The analogue of symplectic structure for odd-dimensional manifolds is a little less symmetric, but is also a very interesting structure – the contact structure. In this chapter, we apply the ideas of preserving Lie group and Lie algebra structure of dynamical systems in constructing symplectic algorithms for Hamiltonian systems to the study of numerical algorithms for contact dynamical systems and present so-called contact algorithms, i.e., algorithms preserving contact structure, for solving numerically contact systems.

# 11.1 Contact Structure

The source of contact structures are manifolds of contact element of configuration spaces. It is also of basic importance in physical and engineering sciences. Contact geometry has – as does symplectic geometry – broad applications in physics, e.g. geometrical optics, classical mechanics, thermodynamics, geometric quantization, and applied mathematics such as control theory.

# 11.1.1 Basic Concepts of Contact Geometry

Contact geometry $\mathbf { \left[ A r n 8 9 , A r n 8 8 \right]} $ is the study of a geometric structure on smooth manifolds given by a hyperplane distribution in the tangent bundle and specified by a one-form, both of which satisfy a “maximum non-degeneracy” condition called “complete nonintegrability”.

The integration of first-order partial differential equations is reduced to the integration of a system of ordinary differential equations, the so-called characteristic equations. The basic of this reduction is a simple geometric analysis of the formulation of curves. Let $M$ be a smooth manifold and let $V$ be a direction field on $M$ .

Definition 1.1. $N \subset M$ is called an integral surface of $V$ if the tangent plane of $N$ contains the direction of $V$ at every point (Fig. 1.1).

Let $\varGamma$ be a $k$ -dimensional submanifold in an $n$ -dimensional manifold $M$ (Fig. 1.2), $\varGamma$ is called a hypersurface if $k = n - 1$ .

The Cauchy problem for the direction field $v$ with initial manifold $\varGamma$ is the problem of finding a $( k + 1 )$ -dimensional integral submanifold of $v$ containing the initial submanifold $\varGamma$ .

![](../chunks/Symplectic Geometric Algorithms for Hamiltonian Systems, Kang Feng_Mengzhao Qin_part_0008_pages_0491-0560/auto/images/8f31855523d579ac163c9f8c35685dc43f186abfb276853d05f9456d86bd6325.jpg)  
Fig. 1.1. Meaning of definition

![](../chunks/Symplectic Geometric Algorithms for Hamiltonian Systems, Kang Feng_Mengzhao Qin_part_0008_pages_0491-0560/auto/images/edec02e4f19c9d194910bef438270694a057432d6e3786f4e04bca10ded95131.jpg)

![](../chunks/Symplectic Geometric Algorithms for Hamiltonian Systems, Kang Feng_Mengzhao Qin_part_0008_pages_0491-0560/auto/images/e2d8ded28dfefe774219e91b3417026860e9986418771b0adda7d33f03c436ce.jpg)  
Fig. 1.2. Integral surface with initial manifold of $\varGamma$

Every point in $n$ -dimensional space existence an $( n - 1 )$ -dimensional hyperplane, $\operatorname { c o d i m } = 1$ field of hyperplane, this means field of tangent hyperplane can be locally described by 1-form, and

$$
\begin{array} { c } { { \displaystyle \alpha = \sum _ { i = 1 } ^ { n } \alpha _ { i } \mathbf { d } x _ { i } , \mathrm { a n d } } } \\ { { \displaystyle \sum _ { i = 1 } ^ { n } \alpha _ { i } ^ { 2 } ( x ) \neq 0 , \quad \forall x \in \mathbf { R } ^ { n } . } } \end{array}
$$

Hyperplane in Fig. 1.3 is null space of 1-form $\alpha$ . Relation between hyperplane and its 1-form is not 1- to $^ { - 1 }$ correspondence. They may be different up to multiplication by a non zero constant. This multiplicator is dependent of point.

We consider what a filed of hyperplane looks like in general in a neighborhood of a point in an $n$ -dimensional manifold. For example, let $n = 2$ . Then the manifold is a surface and field of hyperplane is a field of straight line. Such a field in a neighborhood of a point is always constructed very simply, namely, as a field of tangent to a family of parallel lines in a plane. More precisely, one of the basic results of the local theory of ODEs is that it is possible to change any smooth field of tangent lines on a manifold into a field of tangents to family of straight lines in Euclidean space by using a diffeomorphism in a sufficiently small neighborhood of any point of the manifold.

![](../chunks/Symplectic Geometric Algorithms for Hamiltonian Systems, Kang Feng_Mengzhao Qin_part_0008_pages_0491-0560/auto/images/f784e8ac6b6cb0d09205e610cfd6d23629ce7914b40b9a0093d881c5edaeaf82.jpg)  
Fig. 1.3. Hyperplane

If $n > 2$ , then a hyperplane is not a line. For example, if $n = 3$ , most field of 2-dimensional tangent planes in ordinary 3-dimensional space cannot be diffeomorphically mapped onto a field of parallel planes. The reason is that there exists fields of tangent planes for which it is impossible to find integral surfaces, i.e., surface which have the prescribed tangent plane at each point.

A 1-form in 3-dimensional can be written in following standard form

$$
\alpha = x \mathbf { d } y + \mathbf { d } z .
$$

Every tangent hyperplane in point $x$ , which is denoted by $\Pi _ { x }$ , have:

$$
\left[ \eta _ { x } , \eta _ { y } , \eta _ { z } \right] \left[ \begin{array} { c } { { 0 } } \\ { { x } } \\ { { 1 } } \end{array} \right] = 0 ,
$$

and $[ 0 , x , 1 ]$ not all equal to zero, it is defined as a 2-dimensional field of hyperplane.

When $x = 0$ ,

$$
{ \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { 1 } \end{array} \right] } ^ { \mathrm { T } } { \left[ \begin{array} { l } { \eta _ { x } } \\ { \eta _ { y } } \\ { 0 } \end{array} \right] } = 0 .
$$

Each point with a hyperplane intersecting wall defines a direction field, see Fig. 1.4 and 1.5.

Next, we prove that in $\mathbf { R } ^ { 3 }$ space, there does not exist an integral surface which can be given by the 1-form $\alpha = x \mathbf { d } y + \mathbf { d } z$ , where $x , y$ is horizontal coordinate, $z$ is vertical coordinate, see Fig. 1.6.

Consider a pair of vectors emanating from the origin (0,0,0) and lying in the horizontal plane of our coordinate systems; another integral curve from (0,0,0) to (0,1,0), and then from (0,1,0) to (1,1,0), and another integral curve from (0,0,0) to (1,0,0), and then from (1,0,0) to $( 1 , 1 , - 1 )$ . As a result, these two curves cannot close up. The difference in the heights of these points is 1, this difference can be considered as a measure of the nonintegrability of the field.

We have four direction fields from the origin point 0 to walls of east, south, west, and north, respectively, describing by Fig. 1.5.

![](../chunks/Symplectic Geometric Algorithms for Hamiltonian Systems, Kang Feng_Mengzhao Qin_part_0008_pages_0491-0560/auto/images/02c4e835b0ed8d7e0408f9277b5d7e29499771841594a5f8b9fe52912f57ada5.jpg)  
Fig. 1.4. Defines the field of $2 n$ -dimensional plane $\alpha = 0$ in $\mathbf { R } ^ { 2 n + 1 }$

![](../chunks/Symplectic Geometric Algorithms for Hamiltonian Systems, Kang Feng_Mengzhao Qin_part_0008_pages_0491-0560/auto/images/eb1f1f308ef40d897bb38dec4fee247d10b33367c102ff5f9651469334a769f2.jpg)  
Fig. 1.5. Direction fields in each wall

# 11.1.2 Contact Structure

A contact element to an $n$ -dimensional smooth manifold at some point is an $( n - 1 )$ - dimensional plane tangent to the manifold at that point, i.e., an $( n - 1 )$ -dimensional subspace of the $n$ -dimensional tangent space at that point. At the $n$ -dimensional space for each point there is a $n - 1$ dimensional hyperplane, dimensions of this hyperplane field is $n - 1$ . We note first that a field of hyperplanes can be given locally by a differential 1-form: a plane in the tangent space gives a 1-form up to multiplication by a non zero constant. We choose this constant so that the value of the form on vertical basic vector is equal to 1. The Hyperplanes of the field are null space of the 1-form[Arn89,Arn88] .

Definition 1.2. A field of hyperplanes is said to be nondegenerate at a point if the rank of the 2-form $\mathrm { d } \alpha | _ { \omega = 0 }$ in the plane of the field passing through this point is equal to the dimension of the plane.

Definition 1.3. A differential 1-form $\alpha$ which is nowhere equal to the zero form on a manifold $M$ is called a contact form if the exterior derivative $\mathrm { d } \alpha$ of $\alpha$ defines a nondegenerate exterior 2-form in every plane $\alpha = 0$ .

![](../chunks/Symplectic Geometric Algorithms for Hamiltonian Systems, Kang Feng_Mengzhao Qin_part_0008_pages_0491-0560/auto/images/8035f0b8e4a31a2787b109921188b5181cd52a7bdb046bd939eb5b252ac46474.jpg)  
Fig. 1.6. Integral curves constructed for a non-integrable field of planes

Example 1.4. Consider the space $\mathbf { R } ^ { 2 n + 1 }$ with the contact structure by the 1-form $\alpha = \mathbf { d } u + p \mathbf { d } q$ . Where $q = ( q _ { 1 } , \cdots , q _ { n } ) , u , p = ( p _ { 1 } , \cdots , p _ { n } )$ , $\alpha$ is not equal to zero form at any point in $\mathbf { R } ^ { 2 n + 1 }$ , and consequently defines the field of $2 n$ -dimensional planes α = 0 in R2n+1.

Example 1.5. The form constructed in Example 1.4 is a contact form, the exterior derivatives of the form $\alpha$ is equal to

$$
\mathbf { d } \alpha | _ { \alpha = 0 } = \mathbf { d } q _ { 1 } \wedge \mathbf { d } p _ { 1 } + \cdot \cdot \cdot + \mathbf { d } q _ { n } \wedge \mathbf { d } p _ { n } .
$$

In the plane $\alpha = 0$ , $\left( q _ { 1 } , \cdot \cdot \cdot , q _ { n } ; p _ { 1 } , \cdot \cdot \cdot , p _ { n } \right)$ may serve as coordinate.

The matrix of the form $\omega = \mathrm { d } \alpha | _ { \alpha = 0 }$ has the form $\left[ \begin{array} { l l } { O } & { - I } \\ { I } & { O } \end{array} \right]$ , where $I$ is the identity matrix of order $n$ . The determinant of this matrix is equal to 1. Consequently, the 2-form $\omega$ is nondegenerate. In other words, the rank of this form is $2 n$ , so our field is nondegenerate at the origin and thus also in a neighborhood of the origin (in fact, this field of planes is nondegenerate at all points of the space).

Definition 1.6. A contact structure on the manifold $M$ is a field of tangent plane which are given locally as the set of zeros of a contact 1-form. The hyperplanes of the field are called contact hyperplanes. We can denote by $\Pi _ { x }$ the contact hyperplane at the point $x$ . Putting briefly, a contact structure on a manifold is a nondegenerate field of tangent hyperplane.

Definition 1.7. A field of planes is called nondegenerated on a manifold if it is nondegenerate at every point of the manifold.

It should be noted that on the even-dimensional manifold there cannot be a nondegenerate field of hyperplanes, on such a manifold a hyperplane is odd-dimensional, and the rank of every skew-symmetric bilinear form on an odd-dimensional space is less than the dimension of the space. Nondegenerate field of hyperplane do exist on odd-dimensional manifold.

Definition 1.8. A hyperplane (dimension $n - 1 \mathrm { \Delta }$ ) tangent to a manifold at some point is called a contact element, and this point is called the point of contact.

The set of all contact element of an $n$ -dimensional manifold has the structure of a smooth manifold of dimension $2 n - 1$ . The manifold of all contact elements of an $n$ -dimensional manifold is a fiber bundle whose base is our manifold and whose fiber is $( n - 1 )$ -dimensional projective space.

Theorem 1.9. The bundle of contact element is the projectivization of the cotangent bundle: it can be obtained from the cotangent bundle by changing every cotangent $n$ -dimensional vector space into on $( n - 1 )$ -dimensional projective space (a point of which is a line passing through the origin in the cotangent space).

Proof. A contact element is given by a 1-form on the tangent space, for which this element is not zero, and it is determined up to multiplication by a non zero number. But a form on the tangent space is a vector of the cotangent space. Therefore, a non zero vector of the cotangent space, determined up to a multiplication by a non zero number, is a non zero vector of the cotangent space, determined up to a multiplication by a non zero number, i.e., a point of the projectivized cotangent space. -

In this chapter, we simply consider the Euclidean space $\mathbf { R } ^ { 2 n + 1 }$ of $2 n { + 1 }$ dimensions as our basic manifold with the contact structure given by the normal form

$$
\alpha = \sum _ { i = 1 } ^ { n } x _ { i } \mathbf { d } y _ { i } + \mathbf { d } z = x \mathbf { d } y + \mathbf { d } z = ( 0 , x ^ { \mathrm { T } } , 1 ) \left[ \begin{array} { l } { \mathbf { d } x } \\ { \mathbf { d } y } \\ { \mathbf { d } z } \end{array} \right] ,
$$

here we have used 3-symbol notation to denote the coordinates and vectors on $\mathbf { R } ^ { 2 n + 1 }$

$$
x = ( x _ { 1 } , \cdots , x _ { n } ) ^ { \mathrm { T } } , \quad y = ( y _ { 1 } , \cdots , y _ { n } ) ^ { \mathrm { T } } , \quad z = ( z ) .
$$

A contact dynamical system on $\mathbf { R } ^ { 2 n + 1 }$ is governed by a contact vector field $f =$ $( a ^ { \mathrm { T } } , b ^ { \mathrm { T } } , c ) : \dot { \mathbf { R } ^ { 2 n + 1 } } \xrightarrow { } \dot { \mathbf { R } ^ { 2 n + 1 } }$ through equations

$$
\dot { x } = a ( x , y , z ) , \quad \dot { y } = b ( x , y , z ) , \quad \dot { z } = c ( x , y , z ) , \quad \cdot = : \frac { \mathrm { d } } { \mathrm { d } t } ,
$$

where the contactivity condition of the vector field $f$ is

$$
L _ { f } \alpha = \lambda _ { f } \alpha ,
$$

with some function $\begin{array} { r } { { \lambda } _ { f } : \begin{array} { r } { { \mathbf { R } } ^ { 2 n + 1 } \to { \mathbf { R } } } \end{array} } \end{array}$ , called the multiplier of $f$ . In (1.4), $L _ { f } \alpha$ denotes the Lie derivation of $\alpha$ with respect to $f$ and is usually calculated by the formula (see Chapter 1 of book)[Arn88]

$$
L _ { f } \alpha = i _ { f } { \bf d } \alpha + { \bf d } i _ { f } \alpha .
$$

It is easy to show from (1.4) and (1.5) that to any contact vector field $f$ on $\mathbf { R } ^ { 2 n + 1 }$ , there corresponds a function $K ( x , y , z )$ , called contact Hamiltonian, such that

$$
a = - K _ { y } + K _ { z } x , \quad b = K _ { x } , \quad c = K - x ^ { \operatorname { T } } K _ { x } = : K _ { e } .
$$

In fact, (1.6) represents the general form of a contact vector field. Its multiplier, denoted as $\lambda _ { f }$ from now, is equal to $K _ { z }$ .

Definition 1.10. A contact transformation $g$ is a diffeomorphism on $\mathbf { R } ^ { 2 n + 1 }$

$$
g : \quad { \left( \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right) } \quad \longrightarrow \quad { \left( \begin{array} { l } { { \widehat { x } } ( x , y , z ) } \\ { { \widehat { y } } ( x , y , z ) } \\ { { \widehat { z } } ( x , y , z ) } \end{array} \right) }
$$

conformally preserving the contact structure, i.e., $g ^ { * } \alpha = \mu _ { g } \alpha$ , that means

$$
\sum _ { i = 1 } ^ { n } { \widehat { x } } _ { i } \mathbf { d } { \widehat { y } } _ { i } + \mathbf { d } { \widehat { z } } = \mu _ { g } \left( \sum _ { i = 1 } ^ { n } x _ { i } \mathbf { d } y _ { i } + \mathbf { d } z \right) ,
$$

for some everywhere non-vanishing function $\mu _ { g } : \mathbf { R } ^ { 2 n + 1 } \to \mathbf { R }$ , called the multiplier of $g$ .

The explicit expression of (1.7) is

$$
( 0 , { \widehat x } ^ { \mathrm { T } } , 1 ) \left[ \begin{array} { l l l } { { \widehat x } _ { x } } & { { \widehat x } _ { y } } & { { \widehat x } _ { z } } \\ { { \widehat y } _ { x } } & { { \widehat y } _ { y } } & { { \widehat y } _ { z } } \\ { { \widehat z } _ { x } } & { { \widehat z } _ { y } } & { { \widehat z } _ { z } } \end{array} \right] = \mu _ { g } ( 0 , x ^ { \mathrm { T } } , 1 ) .
$$

A fundamental fact is that the phase flow $g _ { K } ^ { t }$ of a contact dynamical system associated with a contact Hamiltonian $K : \mathbf { R } ^ { 2 n + 1 } \stackrel { - } {  } \mathbf { R }$ is a one parameter (local) group of contact transformations on $\mathbf { R } ^ { 2 n + 1 }$ , i.e., $g _ { K } ^ { t }$ satisfies

$$
\begin{array} { r l } & { g _ { K } ^ { 0 } = \mathrm { i d e n t i t y ~ m a p ~ o n ~ } { \bf R } ^ { 2 n + 1 } ; } \\ & { g _ { K } ^ { t + s } = g _ { K } ^ { t } \circ g _ { K } ^ { s } , \quad \forall t , s \in { \bf R } ; } \\ & { ( g _ { K } ^ { t } ) ^ { * } \alpha = \mu _ { g _ { K } ^ { t } } \alpha , } \end{array}
$$

for some everywhere non-vanishing function $\mu _ { g _ { K } ^ { t } } : \mathbf { R } ^ { 2 n + 1 } \to \mathbf { R }$ . Moreover, we have the following relation between $\mu _ { G _ { k } ^ { * } }$ K and the Hamiltonian $K$ :

$$
\mu _ { g _ { K } ^ { t } } = \exp \int _ { 0 } ^ { t } ( K _ { z } \circ g _ { K } ^ { s } ) \mathrm { d } s .
$$

For general contact systems, condition (1.10) is stringent for algorithmic approximations to phase flows because only the phase flows themselves satisfy it. We will construct algorithms for contact systems such that the corresponding algorithmic approximations to the phase flows satisfy the condition (1.10), of course, probably, with different, but everywhere non-vanishing, multipliers from $\mu _ { g _ { K } ^ { t } }$ . We call such algorithms as contact ones.

# 11.2 Contactization and Symplectization

There is a well known correspondence between contact geometry on $\mathbf { R } ^ { 2 n + 1 }$ and conic (or homogeneous) symplectic geometry on $\mathbf { R } ^ { 2 n + 2 }$ . To establish this correspondence, we introduce two spaces $\mathbf { R } _ { + } ^ { 2 n + 2 }$ and ${ \bf R } _ { + } \times { \bf R } ^ { 2 n + 1 }$ .

a. We use the 4-symbol notation for the coordinates on $\mathbf { R } ^ { 2 n + 2 }$

$$
\left[ \begin{array} { c } { p _ { 0 } } \\ { p _ { 1 } } \\ { q _ { 0 } } \\ { q _ { 1 } } \end{array} \right] , \quad p _ { 0 } = ( p _ { 0 } ) , \quad q _ { 0 } = ( q _ { 0 } ) , \quad p _ { 1 } = \left[ \begin{array} { c } { p _ { 1 1 } } \\ { \vdots } \\ { p _ { 1 n } } \end{array} \right] , \quad q _ { 1 } = \left[ \begin{array} { c } { q _ { 1 1 } } \\ { \vdots } \\ { q _ { 1 n } } \end{array} \right] .
$$

Consider

$$
{ \bf R } _ { + } ^ { 2 n + 2 } = \left\{ ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) \in { \bf R } ^ { 2 n + 2 } \ | \ p _ { 0 } > 0 \right\}
$$

as a conic symplectic space with the standard symplectic form

$$
\omega = \mathrm { d } p _ { 0 } \wedge \mathrm { d } q _ { 0 } + \mathrm { d } p _ { 1 } \wedge \mathrm { d } q _ { 1 } .
$$

Definition 2.1. Function $\phi : \mathbf { R } _ { + } ^ { 2 n + 2 } \to \mathbf { R }$ is called a conic function if it satisfies

$$
\phi ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } \phi \Bigl ( 1 , \frac { p _ { 1 } } { p _ { 0 } } , q _ { 0 } , q _ { 1 } \Bigr ) , \quad \forall p _ { 0 } > 0 .
$$

So, a conic function on $\mathbf { R } ^ { 2 n + 2 }$ depends essentially only $2 n + 1$ variables.

${ \cal F } : { \bf R } _ { + } ^ { 2 n + 2 }  { \bf R } _ { + } ^ { 2 n + 2 }$

$$
F \circ T _ { \lambda } = T _ { \lambda } \circ F , \quad \forall \lambda > 0 ,
$$

where $T _ { \lambda }$ is the linear transformation on $\mathbf { R } ^ { 2 n + 2 }$

$$
T _ { \lambda } \left[ \begin{array} { c } { { p } } \\ { { q } } \end{array} \right] = \left[ \begin{array} { c } { { \lambda p } } \\ { { q } } \end{array} \right] , \quad p = \left[ \begin{array} { c } { { p _ { 0 } } } \\ { { p _ { 1 } } } \end{array} \right] , \quad q = \left[ \begin{array} { c } { { q _ { 0 } } } \\ { { q _ { 1 } } } \end{array} \right] .
$$

The conic condition (2.5) for the mapping $F : ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } )  ( P _ { 0 } , P _ { 1 } , Q _ { 0 } , Q _ { 1 } )$ can be expressed as follows:

$$
\begin{array} { r l } & { P _ { 0 } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } P _ { 0 } \Big ( 1 , \frac { p _ { 1 } } { p _ { 0 } } , q _ { 0 } , q _ { 1 } \Big ) > 0 , } \\ & { P _ { 1 } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } P _ { 1 } \Big ( 1 , \frac { p _ { 1 } } { p _ { 0 } } , q _ { 0 } , q _ { 1 } \Big ) , } \\ & { Q _ { 0 } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = Q _ { 0 } \Big ( 1 , \frac { p _ { 1 } } { p _ { 0 } } , q _ { 0 } , q _ { 1 } \Big ) , } \\ & { Q _ { 1 } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = Q _ { 1 } \Big ( 1 , \frac { p _ { 1 } } { p _ { 0 } } , q _ { 0 } , q _ { 1 } \Big ) , } \end{array} \qquad \forall \ : p _ { 0 } > 0 .
$$

So, a conic map is essentially depending only on $2 n + 2$ functions in $2 n + 1$ variables.

It should be noted that, in some cases, we also consider conic functions and conic maps defined on the whole Eucildean space. The following lemma gives a criterion of a conic symplectic map.

Lemma 2.3. $F : ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } )  ( P _ { 0 } , P _ { 1 } , Q _ { 0 } , Q _ { 1 } )$ is a conic symplectic map if and only if $( 0 , 0 , P _ { 0 } ^ { \mathrm { T } } , P _ { 1 } ^ { \mathrm { T } } ) F _ { * } - ( 0 , 0 , p _ { 0 } ^ { T } , p _ { 1 } ^ { \mathrm { T } } ) = 0$ , where $F _ { * }$ is the Jacobi matrix of $F$ at the point $\left( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } \right)$ .

Proof. For $F : ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } )  ( P _ { 0 } , P _ { 1 } , Q _ { 0 } , Q _ { 1 } )$ , the condition

$$
( 0 , 0 , P _ { 0 } ^ { \mathrm { T } } , P _ { 1 } ^ { \mathrm { T } } ) F _ { * } - ( 0 , 0 , p _ { 0 } ^ { \mathrm { T } } , p _ { 1 } ^ { \mathrm { T } } ) = 0 ,
$$

is equivalent to the condition

$$
P _ { 0 } \mathbf { d } Q _ { 0 } + P _ { 1 } \mathbf { d } Q _ { 1 } = p _ { 0 } \mathbf { d } q _ { 0 } + p _ { 1 } \mathbf { d } q _ { 1 } , \quad \mathrm { o r } \quad P \mathbf { d } Q = p \mathbf { d } q ,
$$

where $P = ( P _ { 0 } , P _ { 1 } ) , Q = ( Q _ { 0 } , Q _ { 1 } ) , p = ( p _ { 0 } , p _ { 1 } ) , q = ( q _ { 0 } , q _ { 1 } ) .$ Hence in matrix form, it can be written as

$$
\begin{array} { r } { Q _ { p } ^ { \mathrm { T } } \cdot P = 0 , \quad Q _ { q } ^ { \mathrm { T } } \cdot P = p . } \end{array}
$$

Notice that a function $f ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } )$ is homogeneous of degree $k$ , i.e.,

$$
f ( \lambda x _ { 1 } , \lambda x _ { 2 } , \cdots , \lambda x _ { n } ) = \lambda ^ { k } f ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } ) ,
$$

if and only if

$$
\sum x _ { i } f _ { x _ { i } } ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } ) = k f ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } ) .
$$

Therefore, the condition (2.7) is equivalent to

$$
P _ { p } ( p , q ) \cdot p = P ( p , q ) , \quad Q _ { p } ( p , q ) = 0 .
$$

If $F$ is conic symplectic, then

$$
\begin{array} { r } { Q _ { p } ^ { \mathrm { { T } } } P _ { p } - P _ { p } ^ { \mathrm { { T } } } Q _ { p } = O , \quad Q _ { q } ^ { \mathrm { { T } } } P _ { q } - P _ { q } ^ { \mathrm { { T } } } Q _ { q } = O , \quad Q _ { q } ^ { \mathrm { { T } } } P _ { p } - P _ { q } ^ { \mathrm { { T } } } Q _ { p } = I . } \end{array}
$$

Combining with (2.11), we get

$$
p = Q _ { q } ^ { \mathrm { T } } P _ { p } p - P _ { q } ^ { \mathrm { T } } Q _ { p } p = Q _ { q } ^ { \mathrm { T } } P , O = Q _ { p } ^ { \mathrm { T } } P _ { p } p - P _ { p } ^ { \mathrm { T } } Q _ { p } p = Q _ { p } ^ { \mathrm { T } } P .
$$

This proves the “only if” part.

Conversely, if $F$ satisfies the condition (2.8), then it satisfies (2.9), which means that it is symplectic. We know that if a matrix is symplectic, then its transpose is also symplectic. Therefore,

$$
P _ { q } P _ { p } ^ { \mathrm { T } } - P _ { p } P _ { q } ^ { \mathrm { T } } = O , \quad Q _ { q } Q _ { p } ^ { T } - Q _ { p } Q _ { q } ^ { \mathrm { T } } = O , \quad P _ { p } Q _ { q } ^ { \mathrm { T } } - P _ { q } Q _ { p } ^ { \mathrm { T } } = I .
$$

Combining with (2.10), we get

$$
\begin{array} { r } { P = P _ { p } Q _ { q } ^ { \mathrm { T } } P - P _ { q } Q _ { p } ^ { \mathrm { T } } P = P _ { p } p , } \\ { 0 = Q _ { q } Q _ { p } ^ { \mathrm { T } } P - Q _ { p } Q _ { q } ^ { \mathrm { T } } P = Q _ { q } p . } \end{array}
$$

This means that $F$ is conic. This finishes the proof.

b. Consider ${ \bf R } _ { + } \times { \bf R } ^ { 2 n + 1 }$ as the product of the positive real space $\mathbf { R } _ { + }$ and the contact space $\mathbf { R } ^ { 2 n + 1 }$ . We use $( w , x , y , z )$ to denote the coordinates of ${ \bf R } _ { + } \times { \bf R } ^ { 2 n + 1 }$ with $w > 0$ and with $x , y , z$ as before.

Definition 2.4. A map ${ \cal G } \colon { \mathbf { R } } _ { + } \times { \mathbf { R } } ^ { 2 n + 1 }  { \mathbf { R } } _ { + } \times { \mathbf { R } } ^ { 2 n + 1 }$ is called a positive product map if it is composed by a map $g : \mathbf { R } ^ { 2 n + 1 } \to \mathbf { R } ^ { 2 n + 1 }$ and a positive function $\gamma :$ ${ \bf R } ^ { 2 n + 1 }  { \bf R } _ { + }$ in the form

$$
\left[ \begin{array} { c } { { w } } \\ { { x } } \\ { { y } } \\ { { z } } \end{array} \right] \longrightarrow \left[ \begin{array} { c } { { W } } \\ { { X } } \\ { { Y } } \\ { { Z } } \end{array} \right] , \quad W = w \gamma ( x , y , z ) , \quad ( X , Y , Z ) = g ( x , y , z ) .
$$

We denote $\gamma \otimes g$ the positive product map composed of map $g$ and function $\gamma$ .

c. Define mapping $S : \mathbf { R } _ { + } \times \mathbf { R } ^ { 2 n + 1 } \to \mathbf { R } _ { + } ^ { 2 n + 2 }$

$$
\left[ \begin{array} { l } { w } \\ { x } \\ { y } \\ { z } \end{array} \right] \longrightarrow \left[ \begin{array} { l } { p _ { 0 } = w } \\ { p _ { 1 } = w x } \\ { q _ { 0 } = z } \\ { q _ { 1 } = y } \end{array} \right] .
$$

Then the inverse $S ^ { - 1 } : { \bf R } _ { + } ^ { 2 n + 2 }  { \bf R } _ { + } \times { \bf R } ^ { 2 n + 1 }$ is given by

$$
\left[ \begin{array} { c } { { p _ { 0 } } } \\ { { p _ { 1 } } } \\ { { q _ { 0 } } } \\ { { q _ { 1 } } } \end{array} \right] \longrightarrow \left[ \begin{array} { c } { { w = p _ { 0 } } } \\ { { x = \frac { p _ { 1 } } { p _ { 0 } } } } \\ { { y = q _ { 1 } } } \\ { { z = q _ { 0 } } } \end{array} \right] , \quad p _ { 0 } \neq 0 .
$$

Lemma 2.5. [Fen93b,Fen95] Given a transformation $F : ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) \to ( P _ { 0 } , P _ { 1 } , Q _ { 0 }$ , $Q _ { 1 } )$ on $\mathbf { R } _ { + } ^ { 2 n + 2 }$ and let $G = S ^ { - 1 } \circ F \circ S$ . Then we have:

$1 ^ { \circ }$ $F$ is a conic map on $\mathbf { R } _ { + } ^ { 2 n + 2 }$ if and only if $G$ is a positive product map on ${ \bf R } _ { + } \times { \bf R } ^ { 2 n + 1 }$ ; in this case, if we write $G = \gamma \otimes g$ , then

$$
\gamma ( x , y , z ) = P _ { 0 } ( 1 , x , z , y ) ,
$$

and $g : ( x , y , z ) \to ( X , Y , Z )$ is given by

$$
X = \frac { P _ { 1 } ( 1 , x , z , y ) } { P _ { 0 } ( 1 , x , z , y ) } , \quad Y = Q _ { 1 } ( 1 , x , z , y ) , \quad Z = Q _ { 0 } ( 1 , x , z , y ) .
$$

$2 ^ { \circ }$ $F$ is a conic symplectic map if and only if $G$ is a positive product map, say $\gamma \otimes g$ , on ${ \bf R } _ { + } \times { \bf R } ^ { 2 n + 1 }$ with $g$ also a contact map on $\mathbf { R } ^ { 2 n + 1 }$ . Moreover, in this case, the multiplier of the contact map $g$ is just equal to $\gamma ^ { - 1 } = P _ { 0 } ^ { - 1 } ( 1 , x , z , y )$ .

Proof. The conclusion $1 ^ { \circ }$ is easily proved by some simple calculations. Below we devote to the proof of $2 ^ { \circ }$ . Let $F$ send $( p _ { 0 } , \dot { p _ { 1 } } , q _ { 0 } , q _ { 1 } ) \stackrel { . } {  } ( P _ { 0 } , P _ { 1 } , Q _ { 0 } , Q _ { 1 } )$ , $G$ send $( w , x , y , z ) \to ^ { \bullet } ( W , X , Y , Z )$ . Then by using the conclusion $1 ^ { \circ }$ , we have

$$
\begin{array} { r } { P _ { 0 } \circ S = w P _ { 0 } ( 1 , x , z , y ) = w \gamma , P _ { 1 } \circ S = w P _ { 1 } ( 1 , x , z , y ) = w \gamma X ( x , y , z ) , } \end{array}
$$

$$
S _ { * } = \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { x } & { w I _ { n } } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { I _ { n } } & { 0 } \end{array} \right] , \quad G _ { * } = \frac { \partial \left( W , X , Y , Z \right) } { \partial \left( w , x , y , z \right) } = \left[ \begin{array} { l l l l } { \gamma } & { w \gamma _ { x } } & { w \gamma _ { y } } & { w \gamma _ { z } } \\ { 0 } & { } & { } & { } \\ { 0 } & { } & { g _ { * } } & { } \\ { 0 } & { } & { } & { } \end{array} \right] ,
$$

$$
S _ { * } \circ G = \left[ \begin{array} { c c c c } { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { X } } & { { W I _ { n } } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } \\ { { 0 } } & { { 0 } } & { { I _ { n } } } & { { 0 } } \end{array} \right] ,
$$

and compute

$$
\begin{array} { r l } & { \big ( ( ( 0 , 0 , P _ { 0 } ^ { \mathrm { T } } , P _ { 1 } ^ { \mathrm { T } } ) F _ { * } - ( 0 , 0 , p _ { 0 } ^ { \mathrm { T } } , p _ { 1 } ^ { \mathrm { T } } ) ) \circ S \big ) S _ { * } } \\ & { = \big ( ( 0 , 0 , P _ { 0 } ^ { \mathrm { T } } , P _ { 1 } ^ { \mathrm { T } } ) \circ S \big ) \big ( F _ { * } \circ S \big ) S _ { * } - \big ( ( 0 , 0 , p _ { 0 } ^ { \mathrm { T } } , p _ { 1 } ^ { \mathrm { T } } ) \circ S \big ) S _ { * } } \\ & { = ( 0 , 0 , w \gamma , w \gamma X ^ { \mathrm { T } } ) \big ( F _ { * } \circ S \big ) S _ { * } - ( 0 , 0 , w , w x ^ { \mathrm { T } } ) S _ { * } } \\ & { = ( 0 , 0 , w \gamma , w \gamma X ^ { \mathrm { T } } ) \big ( S _ { * } \circ G \big ) G _ { * } - ( 0 , 0 , w , w x ^ { \mathrm { T } } ) S _ { * } } \\ & { = w \gamma \big ( 0 , ( 0 , X ^ { \mathrm { T } } , 1 ) g _ { * } \big ) - w \gamma \big ( 0 , \gamma ^ { - 1 } ( 0 , x ^ { \mathrm { T } } , 1 ) \big ) . } \end{array}
$$

Noting that $S$ is a diffeomorphism, $S _ { * }$ is non-singular, $w > 0 , \gamma > 0$ , we obtain

$$
( 0 , 0 , P _ { 0 } ^ { \mathrm { T } } , P _ { 1 } ^ { \mathrm { T } } ) F _ { * } - ( 0 , 0 , p _ { 0 } ^ { \mathrm { T } } , p _ { 1 } ^ { \mathrm { T } } ) \equiv 0 \Longleftrightarrow ( 0 , X ^ { \mathrm { T } } , 1 ) g _ { * } - \gamma ^ { - 1 } ( 0 , x ^ { \mathrm { T } } , 1 ) \equiv 0 ,
$$

which proves the conclusion $2 ^ { \circ }$

Lemma 2.5 establishes correspondences between conic symplectic space and contact space and between conic symplectic maps and contact maps. We call the transform from $F$ to $G = S ^ { - 1 } \circ F \circ S = \gamma \otimes g$ contactization of conic symplectic maps, the call the transform transform from $G = \gamma \otimes g$ $S : \mathbf { R } _ { + } \times \mathbf { R } ^ { 2 n + 1 } \to \mathbf { R } _ { + } ^ { 2 n + 1 }$ to $F = S \circ G S ^ { - 1 }$ symplectization of contact space, and symplectization of contact maps and the transform $C = S ^ { - 1 } : { \bf R } _ { + } ^ { 2 n + 2 }  { \bf R } _ { + } \times { \bf R } ^ { 2 n + 1 }$ contactization of conic symplectic space.

# 11.3 Contact Generating Functions for Contact Maps

With the preliminaries of the last section, it is natural to derive contact generating function theory for contact maps from the well known symplectic analog[Fen93b,Fen95,Shu93] .

The following two lemmas can be proved easily[Fen95] .

Lemma 3.1. Hamiltonian $\phi : \mathbf { R } ^ { 2 n + 2 } \to \mathbf { R }$ is a conic function if only if the associated Hamiltonian vector field $a _ { \phi } = J \nabla \phi$ is conic, i.e., $a ( T _ { \lambda } z ) = T _ { \lambda } a ( z ) , \quad \lambda \ne 0 , \ z \in$ $\mathbf { R } ^ { 2 n + 2 }$ , where $J = \left[ { \begin{array} { c c } { O } & { - I _ { n + 1 } } \\ { I _ { n + 1 } } & { O } \end{array} } \right] .$ .

Lemma 3.2. Linear map ${ \left[ \begin{array} { l } { p } \\ { q } \end{array} \right] } \to C { \left[ \begin{array} { l } { p } \\ { q } \end{array} \right] }$ is a conic transformation on $\mathbf { R } ^ { 2 n + 2 }$ , i.e., $C \circ T _ { \lambda } \ : = \ : T _ { \lambda } \circ C .$ , if and only if the matrix $C$ has the diagonal form $C =$ $\left[ \begin{array} { c c } { { C _ { 0 } } } & { { O } } \\ { { O } } & { { C _ { 1 } } } \end{array} \right] w i t h \left( n + 1 \right) \times \left( n + 1 \right)$ matrix $C _ { 0 }$ and $C _ { 1 }$ .

Noting that the matrix in $g l ( 2 n + 2 )$

$$
C = \frac 1 2 ( I + J B ) , \quad B = B ^ { \mathrm { T } } \in S m ( 2 n + 2 ) ,
$$

establishes a 1-1 correspondence between near-zero Hamiltonian vector fields $z $ $\boldsymbol { a } ( \boldsymbol { z } ) \equiv J \nabla \phi ( \boldsymbol { z } )$ and near-identity symplectic maps $z \to g ( z )$ via generating relation

$$
g ( z ) - z = J \nabla \phi ( C g ( z ) + ( I - C ) z ) ,
$$

and combining Lemma 3.1 and Lemma 3.2, we find that matrix

$$
\begin{array} { r } { C = \left[ \begin{array} { c c } { C _ { 0 } } & { O } \\ { O } & { I - C _ { 0 } ^ { \mathrm { T } } } \end{array} \right] , \quad C _ { 0 } \in g l ( n + 1 ) , } \end{array}
$$

establishes a 1-1 correspondence between near-zero conic Hamiltonian vector fields $z  a ( z ) = J \nabla \phi ( z )$ and near-identity conic symplectic maps $z \to g ( z )$ via generating relation (3.3).

Write $\begin{array} { r } { C _ { 0 } = \left[ \begin{array} { l l } { \alpha } & { \beta ^ { \mathrm { T } } } \\ { \gamma } & { \delta } \end{array} \right] } \end{array}$ with $\alpha \in \textbf { R }$ , $\beta , \gamma \in \mathbf { \Gamma } ^ { \mathbf { R } ^ { n } }$ and $\delta \in g l ( n )$ . Then the generating relation (3.2) with generating matrix $C$ given by (3.3) can be expressed as

$$
\left\{ \begin{array} { l l } { \widehat { p } _ { 0 } - p _ { 0 } = - \phi _ { q _ { 0 } } ( \overline { { p } } , \overline { { q } } ) , } \\ { \widehat { p } _ { 1 } - p _ { 1 } = - \phi _ { q _ { 1 } } ( \overline { { p } } , \overline { { q } } ) , } \\ { \widehat { q } _ { 0 } - q _ { 0 } = \phi _ { q _ { 0 } } ( \overline { { p } } , \overline { { q } } ) , } \\ { \widehat { q } _ { 1 } - q _ { 1 } = \phi _ { q _ { 1 } } ( \overline { { p } } , \overline { { q } } ) , } \end{array} \right.
$$

where ${ \overline { { p } } } = { \left[ \begin{array} { l } { { \overline { { p } } } _ { 0 } } \\ { { \overline { { p } } } _ { 1 } } \end{array} \right] }$ and ${ \overline { { q } } } = { \left[ \begin{array} { l } { { \overline { { q } } } _ { 0 } } \\ { { \overline { { q } } } _ { 1 } } \end{array} \right] }$ are given by

$$
\left\{ \begin{array} { l l } { \overline { { p } } _ { 0 } = \alpha \widehat { p } _ { 0 } + ( 1 - \alpha ) p _ { 0 } + \beta ^ { \mathrm { T } } ( \widehat { p } _ { 1 } - p _ { 1 } ) , } \\ { \overline { { p } } _ { 1 } = \delta \widehat { p } _ { 1 } + ( I - \delta ) p _ { 1 } + \gamma ( \widehat { p } _ { 0 } - p _ { 0 } ) , } \\ { \overline { { q } } _ { 0 } = ( 1 - \alpha ) \widehat { q } _ { 0 } + \alpha q _ { 0 } - \gamma ^ { \mathrm { T } } ( \widehat { q } _ { 1 } - q _ { 1 } ) , } \\ { \overline { { q } } _ { 1 } = ( I - \delta ^ { \mathrm { T } } ) \widehat { q } _ { 1 } + \delta ^ { \mathrm { T } } q _ { 1 } - \beta ( \widehat { q } _ { 0 } - q _ { 0 } ) . } \end{array} \right.
$$

Every conic function $\phi$ can be contactized as an arbitrary function $\psi ( x , y , z )$ as follows

$$
\psi ( x , y , z ) = \phi ( 1 , x , z , y ) ,
$$

i.e.,

$$
\phi ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } \phi ( 1 , p _ { 1 } / p _ { 0 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } \psi ( p _ { 1 } / p _ { 0 } , q _ { 1 } , q _ { 0 } ) , \quad p _ { 0 } \neq 0 ,
$$

and we have the partial derivative relation:

$$
\left\{ \begin{array} { l l } { \phi _ { q _ { 0 } } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } \psi _ { z } ( x , y , z ) , } \\ { \phi _ { q _ { 1 } } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } \psi _ { y } ( x , y , z ) , } \\ { \phi _ { p _ { 0 } } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = \psi ( x , y , z ) - x ^ { \mathrm { T } } \psi _ { x } ( x , y , z ) = \psi _ { e } ( x , y , z ) , } \\ { \phi _ { p _ { 1 } } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = \psi _ { x } ( x , y , z ) , } \end{array} \right.
$$

where $\begin{array} { r } { x \ = \ \frac { p _ { 1 } } { p _ { 0 } } } \end{array}$ $y \ = \ q _ { 1 }$ , $z ~ = ~ q _ { 0 }$ on the right hand side. So, under contactizing transforms

$$
\begin{array} { r } { S : \left[ \begin{array} { c c c c c c c c c c } { w } \\ { x } \\ { x } \\ { y } \\ { z } \\ { z } \end{array} \right] \longrightarrow \left[ \begin{array} { c c c c c c c c c } { p _ { 0 } } \\ { p _ { 1 } } \\ { p _ { 1 } } \\ { q _ { 0 } } \\ { q _ { 1 } } \end{array} \right] = \left[ \begin{array} { c c c c c c c c c } { w } \\ { w x } \\ { w x } \\ { z } \\ { z } \\ { y } \end{array} \right] , \left[ \begin{array} { c c c c c c c c } { \hat { w } } \\ { \hat { x } } \\ { \hat { x } } \\ { \hat { y } } \\ { \hat { z } } \end{array} \right] \longrightarrow \left[ \begin{array} { c c c c c c c c } { \hat { p } _ { 0 } } \\ { \hat { p } _ { 1 } } \\ { \hat { p } _ { 1 } } \\ { \hat { q } _ { 0 } } \\ { \hat { q } _ { 1 } } \end{array} \right] = \left[ \begin{array} { c c c c c c c c c } { \hat { w } } \\ { \hat { w } } \\ { \hat { w } \hat { x } } \\ { \hat { x } } \\ { \hat { z } } \\ { \hat { y } } \end{array} \right] , } \\ { \left[ \begin{array} { c c c c c c c c c } { \overline { { w } } } \\ { \overline { { x } } } \\ { \overline { { y } } } \\ { \overline { { z } } } \end{array} \right] \longrightarrow \left[ \begin{array} { c c c c c c c c c } { \overline { { p } } _ { 0 } } \\ { \overline { { p } } _ { 1 } } \\ { \overline { { q } } _ { 0 } } \\ { \overline { { q } } _ { 1 } } \end{array} \right] = \left[ \begin{array} { c c c c c c c c c } { \overline { { w } } } \\ { \overline { { w } } } \\ { \overline { { z } } } \\ { \overline { { y } } } \\ { \overline { { y } } } \end{array} \right] , } \end{array}
$$

the generating relation (3.4) turns into

$$
\left\{ \begin{array} { l l } { \widehat { w } - w = - \overline { { w } } \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \\ { \widehat { w } \widehat { x } - w x = - \overline { { w } } \psi _ { y } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \\ { \widehat { z } - z = \psi _ { e } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \\ { \widehat { y } - y = \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \end{array} \right.
$$

and Equation (3.5) turns into

$$
\left\{ \begin{array} { l l } { \overline { { w } } = \alpha \widehat { w } + ( 1 - \alpha ) w + \beta ^ { \mathrm { T } } ( \widehat { w } \widehat { x } - w x ) , } \\ { \overline { { w } } \overline { { x } } = \delta \widehat { w } \widehat { x } + ( I - \delta ) w x + \gamma ( \widehat { w } - w ) , } \\ { \overline { { z } } = ( 1 - \alpha ) \widehat { z } + \alpha z - \gamma ^ { \mathrm { T } } ( \widehat { y } - y ) , } \\ { \overline { { y } } = ( I - \delta ^ { \mathrm { T } } ) \widehat { y } + \delta ^ { \mathrm { T } } y - \beta ( \widehat { z } - z ) . } \end{array} \right.
$$

Since the $p _ { 0 }$ -axis is distinguished for the contactization in which we should always take $p _ { 0 } \neq 0$ , it is natural to require $\beta = 0$ in (3.5). Let $\widehat { \mu } = \frac { w } { \widehat { w } } = \frac { p _ { 0 } } { \widehat { p } _ { 0 } }$ and $\overline { { \mu } } = \frac { w } { \overline { { w } } } = \frac { \tilde { p _ { 0 } } } { \overline { { p } } _ { 0 } }$ , we obtain from Equations (3.9) and (3.10)

$$
\widehat { \mu } = \frac { 1 + \alpha \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) } { 1 - ( 1 - \alpha ) \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) } , \quad \overline { { \mu } } = 1 + \alpha \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) ,
$$

and the induced contact transformation on the contact $( x , y , z )$ space $\mathbf { R } ^ { 2 n + 1 }$ is

$$
\left\{ \begin{array} { l l } { \widehat { x } - x = - \psi _ { y } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) + \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) \big ( ( 1 - \alpha ) \widehat { x } + \alpha x \big ) , } \\ { } \\ { \widehat { y } - y = \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \\ { } \\ { \widehat { z } - z = \psi _ { e } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \end{array} \right.
$$

with the bar variables on the right hand side given by $\overline { { x } } , \overline { { y } } , \overline { { z } }$

$$
\left\{ \begin{array} { l } { \overline { { x } } = d _ { 1 } \widehat { x } + d _ { 2 } x + d _ { 0 } , } \\ { \overline { { y } } = ( I - \delta ^ { \mathrm { T } } ) \widehat { y } + \delta ^ { \mathrm { T } } y , } \\ { \overline { { z } } = ( 1 - \alpha ) \widehat { z } + \alpha z - \gamma ^ { \mathrm { T } } ( \widehat { y } - y ) , } \end{array} \right.
$$

where

$$
\left\{ \begin{array} { l l } { d _ { 1 } = \big ( I - ( 1 - \alpha ) \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) \big ) \delta , } \\ { d _ { 2 } = \Big ( I + \alpha \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) \big ) ( I - \delta ) , } \\ { d _ { 0 } = - \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) \gamma . } \end{array} \right.
$$

Summarizing the above discussions, we have:

Theorem 3.3. Relations (3.12) – (3.14) give a contact map $( x , y , z ) \to ( { \widehat { x } } , { \widehat { y } } , { \widehat { z } } )$ via contact generating function $\psi ( x , y , z )$ under the type $C _ { 0 } = \left[ \begin{array} { l l } { \alpha } & { O } \\ { \gamma } & { \delta } \end{array} \right]$   . Vice versa.

However, the difficulty in the algorithmic implementation lies in the fact that, unlike $\bar { y }$ and $\overline { z }$ , which are linear combinations of ${ \widehat { y } } , y$ and ${ \widehat { z } } , z$ with constant matrix coefficients, since $\overline { { x } } = d _ { 1 } \widehat { x } + d _ { 2 } x + d _ { 0 }$ and $d _ { 1 } , d _ { 2 }$  are matrices with coefficients depending on $\bar { \psi } _ { z } = \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } )$ which in turn depends on $( { \overline { { x } } } , { \overline { { y } } } , { \overline { { z } } } )$ the combination of $\textstyle { \overline { { x } } }$ from $\widehat { x }$ and $x$ is not explicitly given, the entire equations for solving $\widehat { x } , \widehat { y } , \widehat { z }$ in terms of $x , y , z$ are highly implicit. The exceptional cases are the following:

(E1) $\alpha = 0 , \ \delta = O _ { n } , \ \gamma = O ($ ,

$$
\begin{array} { c } { \widehat { \mu } = 1 - \psi _ { z } ( x , \widehat { y } , \widehat { z } ) , \quad \overline { { \mu } } = 1 , } \\ { \left\{ \begin{array} { l l } { \widehat { x } - x = - \psi _ { y } ( x , \widehat { y } , \widehat { z } ) + \widehat { x } \psi _ { z } ( x , \widehat { y } , \widehat { z } ) , } \\ { \widehat { y } - y = \psi _ { x } ( x , \widehat { y } , \widehat { z } ) , } \\ { \widehat { z } - z = \psi _ { e } ( x , \widehat { y } , \widehat { z } ) = \psi ( x , \widehat { y } , \widehat { z } ) - x ^ { \mathrm { T } } \psi _ { x } ( x , \widehat { y } , \widehat { z } ) . } \end{array} \right. } \end{array}
$$

(E2) α = 1, δ = In, γ = O,

$$
\begin{array} { c } { \widehat { \mu } = \overline { { \mu } } = 1 + \psi _ { z } ( \widehat { x } , y , z ) , } \\ { \left\{ \widehat { x } - x = - \psi _ { y } ( \widehat { x } , y , z ) + x \psi _ { z } ( \widehat { x } , y , z ) , \right. } \\ { \left. \widehat { y } - y = \psi _ { x } ( \widehat { x } , y , z ) , \right. } \\ { \left. \widehat { z } - z = \psi _ { e } ( \widehat { x } , y , z ) = \psi ( \widehat { x } , y , z ) - x ^ { \mathrm { T } } \psi _ { x } ( \widehat { x } , y , z ) . \right. } \end{array}
$$

$\alpha = \frac { 1 } { 2 } , \thinspace \thinspace \thinspace \delta = \frac { 1 } { 2 } I _ { n } , \thinspace \thinspace \gamma = O ,$

$$
\begin{array} { c } { { \displaystyle \widehat { \mu } = \frac { 1 + \frac { 1 } { 2 } \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) } { 1 - \frac { 1 } { 2 } \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) } , \quad \overline { { \mu } } = 1 + \frac { 1 } { 2 } \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } } \\ { { \displaystyle } } \\ { { \left\{ \begin{array} { l } { { \hat { x } - x = - \psi _ { y } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) + \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) \frac { \hat { x } + x } { 2 } , } } \\ { { \hat { y } - y = \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } } \\ { { \hat { z } - z = \psi _ { e } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) = \psi ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) - \overline { { x } } ^ { \mathrm { T } } \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } } \end{array} \right. } } \end{array}
$$

with

$$
\overline { { x } } = \frac { \widehat { x } + x } { 2 } - \frac { 1 } { 4 } \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) ( \widehat { x } - x ) , \overline { { y } } = \frac { \widehat { y } + y } { 2 } , \overline { { z } } = \frac { \widehat { z } + z } { 2 } .
$$

For $\psi _ { z } = \lambda =$ constant, the case (E3) reduces to

$$
\begin{array} { l } { \displaystyle { \widehat { \mu } = \frac { 1 + \frac { 1 } { 2 } \lambda } { 1 - \frac { 1 } { 2 } \lambda } , \quad \overline { { \mu } } = 1 + \frac { 1 } { 2 } \lambda , } } \\ { \displaystyle { \left\{ \begin{array} { l l } { \displaystyle { \widehat { x } - x = - \psi _ { y } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) + \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) \frac { \widehat { x } + x } { 2 } , } } \\ { \displaystyle { \widehat { y } - y = \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } } \\ { \displaystyle { \widehat { z } - z = \psi _ { e } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) = \psi ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) - \overline { { x } } ^ { \mathrm { T } } \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } } \end{array} \right. } } \end{array}
$$

with

$$
\overline { { x } } = \frac { \widehat { x } + x } { 2 } - \frac { 1 } { 4 } \lambda ( \widehat { x } - x ) , \quad \overline { { y } } = \frac { \widehat { y } + y } { 2 } , \quad \overline { { z } } = \frac { \widehat { z } + z } { 2 } .
$$

Note that the symplectic map induced by generating function $\phi$ from the relation (3.2) can be represented as the composition of the maps, non-symplectic generally, $z  { \overline { { z } } }$ and $\overline { { z } }  \widehat { z }$

$$
\begin{array} { l } { { \overline { { z } } = z + C J \nabla \phi ( \overline { { z } } ) , } } \\ { { \overline { { z } } = z + ( I - C ) J \nabla \phi ( \overline { { z } } ) . } } \end{array}
$$

Theorem 3.4. Contact map $( x , y , z ) \to ( { \widehat { x } } , { \widehat { y } } , { \widehat { z } } )$ induced by contact generating function $\psi$   from the relations (3.12)–(3.14) can be represented as the composition of the maps $( x , y , z ) \to ( { \overline { { x } } } , { \overline { { y } } } , { \overline { { z } } } )$ and $( \overline { { x } } , \overline { { y } } , \overline { { z } } )  ( \widehat { x } , \widehat { y } , \widehat { z } )$ which are not contact generally and given, respectively, as follows

$$
\left\{ \begin{array} { l l } { \overline { { x } } - x = - \delta \psi _ { y } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) + \alpha \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) x - \gamma \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \\ { \overline { { y } } - y = ( I - \delta ^ { \mathrm { T } } ) \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \\ { \overline { { z } } - z = ( 1 - \alpha ) \psi _ { e } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) - \gamma ^ { \mathrm { T } } \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) } \end{array} \right.
$$

and

$$
\left\{ \begin{array} { l l } { \widehat { x } - \overline { { x } } = - ( I - \delta ) \psi _ { y } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) + ( 1 - \alpha ) \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) \widehat { x } + \gamma \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \\ { \widehat { y } - \overline { { y } } = \delta ^ { \mathrm { T } } \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \\ { \widehat { z } - \overline { { z } } = \alpha \psi _ { e } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) + \gamma ^ { \mathrm { T } } \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) . } \end{array} \right.
$$

(3.25) and (3.26) are the 2-stage form of the generating relation (3.12) of the contact map induced by generating function $\psi$ under the type $C _ { 0 } = { \left[ \begin{array} { l l } { \alpha } & { O } \\ { \gamma } & { \delta } \end{array} \right] }$ . Corresponding to the exceptional cases (E1), (E2) and (E3), the above 2-stage representation has simpler forms, we no longer use them here.

# 11.4 Contact Algorithms for Contact Systems

Consider contact system (1.3) with the vector field $a$ defined by contact Hamiltonian $K$ according to Equation (1.6). Take $\psi ( x , y , z ) = s K ( x , y , z )$ in $( 3 . 1 2 ) - ( 3 . 1 4 )$ as the generating function, we then obtain contact difference schemes with 1st order of accuracy of the contact system (1.3) associated with all possible types $C _ { 0 } = { \left[ \begin{array} { l l } { \alpha } & { O } \\ { \gamma } & { \delta } \end{array} \right] }$ The simplest and important cases are (write $\overline { { K } } _ { x } = K _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } )$ , etc.) as follows[Fen95] .

# 11.4.1 $\overline { { Q } }$ Contact Algorithm

$\overline { { Q } }$ . Contact analog of symplectic method $( p , Q ) ^ { 1 } \ ( \alpha = 0 , \delta = 0 _ { n } , \gamma = 0 )$ .

2-stage form :

1-stage form : $\begin{array} { l } { \widehat { x } = x + s \big ( - K _ { y } ( x , \widehat { y } , \widehat { z } ) + \widehat { x } K _ { z } ( x , \widehat { y } , \widehat { z } ) \big ) , } \\ { \widehat { y } = y + s K _ { x } ( x , \widehat { y } , \widehat { z } ) , } \\ { \widehat { z } = z + s K _ { e } ( x , \widehat { y } , \widehat { z } ) ; } \\ { \overline { { x } } = x , \quad \overline { { y } } = y + s \overline { { K } } _ { x } , \quad \overline { { z } } = z + s \overline { { K } } _ { e } , } \\ { \widehat { x } = \overline { { x } } + s ( - \overline { { K } } _ { y } + \widehat { x } \overline { { K } } _ { x } ) , \quad \widehat { y } = \overline { { y } } , \quad \widehat { z } = \overline { { z } } . } \end{array}$

# 11.4.2 $\overline { { P } }$ Contact Algorithm

$\overline { { P } }$ . Contact analog of symplectic method $( P , q ) ( \alpha = 1 , \delta = I _ { n } , \gamma = O )$ .

1-stage form: $\begin{array} { r l } & { \hat { x } = x + s \big ( - K _ { y } ( \hat { x } , y , z ) + x K _ { z } ( \hat { x } , y , z ) \big ) , } \\ & { \hat { y } = y + s K _ { x } ( \hat { x } , y , z ) , } \\ & { \hat { z } = z + s K _ { e } ( \hat { x } , y , z ) ; } \\ & { \overline { { x } } = x + s ( - \overline { { K } } _ { y } + x \overline { { K } } _ { z } ) , \quad \overline { { y } } = y , \quad \overline { { z } } = z , } \\ & { \hat { x } = \overline { { x } } , \quad \hat { y } = \overline { { y } } + s \overline { { K } } _ { x } , \quad \hat { z } = \overline { { z } } + s \overline { { K } } _ { e } . } \end{array}$   
2-stage form:

# 11.4.3 $\overline { { C } }$ Contact Algorithm

case $\overline { { C } }$ . Contact version of Poincare generating function method similarly to symplectic ´ $\left( \alpha = \frac { 1 } { 2 } , \delta = \frac { 1 } { 2 } I _ { n } , \gamma = O \right)$ .

2-stage form:

$$
\begin{array} { r l } & { \overline { { x } } = x + \frac { s } { 2 } ( - \overline { { K } } _ { y } + x \overline { { K } } _ { z } ) , \quad \overline { { y } } = y + \frac { s } { 2 } \overline { { K } } _ { z } , \quad \overline { { z } } = z + \frac { s } { 2 } \overline { { K } } _ { e } , } \\ & { \widehat { x } = \overline { { x } } + \frac { s } { 2 } ( - \overline { { K } } _ { y } + \widehat x \overline { { K } } _ { x } ) = \left( \overline { { x } } - \frac { s } { 2 } \overline { { K } } _ { y } \right) \left( 1 - \frac { s } { 2 } \overline { { K } } _ { z } \right) ^ { - 1 } , } \\ & { \widehat { y } = \overline { { y } } + \frac { s } { 2 } \overline { { K } } _ { x } = 2 \overline { { y } } - y , \quad \widehat { z } = \overline { { z } } + \frac { s } { 2 } \overline { { K } } _ { e } = 2 \overline { { z } } - z . } \end{array}
$$

One might suggest, for example, the following scheme for (1.3):

$$
\widehat { x } = x + s a ( \widehat { x } , y , z ) , ~ \widehat { y } = y + s b ( \widehat { x } , y , z ) , ~ \widehat { z } = z + s c ( \widehat { x } , y , z ) .
$$

It differs from (4.2) only in one term for $\widehat { x }$ , i.e., $\widehat { x } K ( \widehat { x } , y , z )$ instead of $x K ( \widehat { x } , y , z )$    This minute, but delicate, difference makes (4.2) contact and the other non-contact!

It should be noted that the $\overline { { Q } }$ and $\overline { { P } }$ methods are of order one of accuracy and the $\overline { { C } }$ method is of order two. The proof is similar to that for symplectic case. In principle, one can construct the contact difference schemes of arbitrarily high order of accuracy for contact systems, as was done for Hamiltonian systems, by suitably composing the $\overline { { Q } } , \overline { { P } }$ or $\overline { { C } }$ method and the respective reversible counterpart[QZ92] . Another general method for the construction of contact difference schemes is based on the generating functions for phase flows of contact systems which will be developed in the next section.

# 11.5 Hamilton–Jacobi Equations for Contact Systems

We recall that a near identity contact map $g \ : \ ( x , y , z ) \ \to \ ( { \widehat { x } } , { \widehat { y } } , { \widehat { z } } )$ can be generated from the so-called generating function $\psi ( x , y , z )$   , associated with a matrix $C _ { 0 } = { \left[ \begin{array} { l l } { \alpha } & { O } \\ { \gamma } & { \delta } \end{array} \right] }$ , by the relations (3.12) – (3.14). Accordingly, to the phase flow $e _ { K } ^ { t }$ of a contact system with contact Hamiltonian $K$ , there corresponds a time-dependent generating function $\psi ^ { t } ( x , y , z )$ such that the map $e _ { K } ^ { t } : ( x , y , z ) \to ( \widehat { x } , \widehat { y } , \widehat { z } )$ is generated from $\psi ^ { t }$ by the relations $( 3 . 1 2 ) - ( 3 . 1 4 )$ , in which $\psi$  is replaced by $\psi ^ { t }$ and $C _ { 0 }$ is given in advance as above. The function $\psi ^ { t }$ should be determined by $K$ and $C _ { 0 }$ . Below we derive the relevant relations between them.

Let $H ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } K \big ( \frac { p _ { 1 } } { p _ { 0 } } , q _ { 1 } , q _ { 0 } \big )$ , $p _ { 0 } \neq 0$ . With this conic Hamiltonian and with normal Darboux matrices $C = \left[ \begin{array} { c c } { C _ { 0 } } & { O } \\ { O } & { I - C _ { 0 } } \end{array} \right]$ , where ${ \cal C } _ { 0 } = \left[ \begin{array} { c c } { { \alpha } } & { { { \cal O } } } \\ { { \gamma } } & { { \delta } } \end{array} \right] ,$

$$
\frac { \partial } { \partial t } \phi ^ { t } ( u ) = H \big ( u + ( I - C ) J \nabla \phi ^ { t } ( u ) \big ) , \quad \mathrm { w i t h } \quad u = ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) ^ { \mathrm { T } } ,
$$

satisfied by the generating function $\phi ^ { t } ( u )$ of the phase flow $g _ { H } ^ { t }$ of the Hamiltonian system associated with the Hamiltonian $H$ while the phase flow $g _ { H } ^ { t }$ is generated from $\phi ^ { t }$ by the relation

$$
g _ { H } ^ { t } ( u ) - u = J \phi ^ { t } \bigl ( C g _ { H } ^ { t } ( u ) + ( I - C ) u \bigr ) .
$$

On the other hand, according to the discussion in Section 11.3, we have

$$
\phi ^ { t } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } \psi ^ { t } ( x , y , z ) , \quad \mathrm { w i t h } \quad x = \frac { p _ { 1 } } { p _ { 0 } } , \quad y = q _ { 1 } , \quad z = q _ { 0 } .
$$

So, by simple calculations, we have

$$
\begin{array} { r } { u + ( I - C ) J \nabla \phi ^ { t } ( u ) = \left[ \begin{array} { c } { p _ { 0 } - ( 1 - \alpha ) \phi _ { q _ { 0 } } } \\ { p _ { 1 } + \gamma \phi _ { q _ { 0 } } - ( I - \delta ) \phi _ { q _ { 1 } } } \\ { q _ { 0 } + \alpha \phi _ { p _ { 0 } } + \gamma ^ { \operatorname { T } } \phi _ { p _ { 1 } } } \\ { q _ { 1 } + \delta ^ { \operatorname { T } } \phi _ { p _ { 1 } } } \end{array} \right] = \left[ \begin{array} { c } { p _ { 0 } ( 1 - ( 1 - \alpha ) \psi _ { z } ) } \\ { p _ { 0 } ( x + \gamma \psi _ { z } - ( I - \delta ) \psi _ { y } ) } \\ { z + \alpha \psi _ { e } + \gamma ^ { \operatorname { T } } \psi _ { x } } \\ { y + \delta ^ { \operatorname { T } } \psi _ { x } } \end{array} \right] } \end{array}
$$

and

$$
\begin{array} { r l } & { H ( u + ( I - C ) J \nabla \phi ^ { t } ( u ) ) } \\ & { = p _ { 0 } \big ( 1 - ( 1 - \alpha ) \psi _ { z } \big ) K \left( \frac { x - ( I - \delta ) \psi _ { y } + \gamma \psi _ { z } } { 1 - ( 1 - \alpha ) \psi _ { z } } , y + \delta ^ { \mathrm { T } } \psi _ { x } , z + \alpha \psi _ { e } + \gamma ^ { \mathrm { T } } \psi _ { x } \right) . } \end{array}
$$

Therefore, from Equation (5.1), $\psi ^ { t } ( x , y , z )$ satisfies

$$
\frac { \partial } { \partial t } \psi ^ { t } = \left( 1 - ( 1 - \alpha ) \psi _ { z } \right) K \left( \frac { x - ( I - \delta ) \psi _ { y } + \gamma \psi _ { z } } { 1 - ( 1 - \alpha ) \psi _ { z } } , y + \delta ^ { \mathrm { T } } \psi _ { x } , z + \alpha \psi _ { e } + \gamma ^ { \mathrm { T } } \psi _ { x } \right) .
$$

Now we claim1. From (5.2), it follows that $\widehat { u } = g _ { H } ^ { t } ( \bar { u } )$ . The claim is then proved, since ${ \cal H } ( g _ { H } ^ { t } ( \bar { u } ) ) = { \cal H } ( \bar { u } )$ , for all $u$ . The following equality is valid

$$
H { \big ( } u + ( I - C ) J \nabla \phi ^ { t } ( u ) { \big ) } = H { \big ( } u - C J \nabla \phi ^ { t } ( u ) { \big ) } .
$$

So, replacing $C$ by $C - I$ in above discussions or, equivalently, replacing $\alpha$ and $\delta$ by $\alpha - 1$ and $\delta - 1$ with $\gamma$ unchanging in (5.3), we can derive equation satisfied by the $\psi ^ { t }$

$$
\frac { \partial } { \partial t } \psi ^ { t } = ( 1 + \alpha \psi _ { z } ) K \left( \frac { x + \delta \psi _ { y } + \gamma \psi _ { z } } { 1 + \alpha \psi _ { z } } , y + ( \delta ^ { \mathrm { T } } - I ) \psi _ { x } , z + ( \alpha - 1 ) \psi _ { e } + \gamma ^ { \mathrm { T } } \psi _ { x } \right) .
$$

(5.3) and (5.5) define the same function $\psi ^ { t }$ . When $t = 0 , e _ { K } ^ { t } = I$ , so we should impose the initial condition

$$
\psi ^ { 0 } ( x , y , z ) = 0 ,
$$

for solving the first order partial differential equation (5.3) or (5.5). We call both equations the Hamilton–Jacobi equations of the contact system associated with the contact Hamiltonian $K$ and the matrix $C _ { 0 } = { \left[ \begin{array} { l l } { \alpha } & { O } \\ { \gamma } & { \delta } \end{array} \right] }$

Specifically, we have Hamilton–Jacobi equations for particular cases:

(E1) $\alpha = 0 , \delta = O , \gamma = O$

$$
\frac { \partial } { \partial t } \psi ^ { t } = ( 1 - \psi _ { z } ^ { t } ) K \left( \frac { x - \psi _ { y } ^ { t } } { 1 - \psi _ { z } ^ { t } } , y , z \right) = K ( x , y - \psi _ { x } ^ { t } , z - \psi _ { e } ^ { t } ) .
$$

(E2) $\alpha = 1 , \delta = I _ { n } , \gamma = O .$

$$
\frac { \partial } { \partial { t } } \psi ^ { t } = K ( x , y + \psi _ { x } ^ { t } , z + \psi _ { e } ^ { t } ) = ( 1 + \psi _ { z } ^ { t } ) K \left( \frac { x + \psi _ { y } ^ { t } } { 1 + \psi _ { z } ^ { t } } , y , z \right) .
$$

(E3) α = 12 , δ = 12 In, γ = O.

$$
\begin{array} { r c l } { { \displaystyle { \frac { \partial } { \partial t } } \psi ^ { t } ~ = ~ \left( 1 - \frac { 1 } { 2 } \psi _ { z } ^ { t } \right) K \left( \frac { x - \displaystyle { \frac { 1 } { 2 } } \psi _ { y } ^ { t } } { 1 - \displaystyle { \frac { 1 } { 2 } } \psi _ { z } ^ { t } } , y + \displaystyle { \frac { 1 } { 2 } } \psi _ { x } ^ { t } , z + \displaystyle { \frac { 1 } { 2 } } \psi _ { e } ^ { t } \right) } } \\ { { ~ } } & { { ~ } } & { { ~ } } \\ { { ~ = ~ \left( 1 + \displaystyle { \frac { 1 } { 2 } } \psi _ { z } ^ { t } \right) K \left( \frac { x + \displaystyle { \frac { 1 } { 2 } } \psi _ { y } ^ { t } } { 1 + \displaystyle { \frac { 1 } { 2 } } \psi _ { z } ^ { t } } , y - \displaystyle { \frac { 1 } { 2 } } \psi _ { x } ^ { t } , z - \displaystyle { \frac { 1 } { 2 } } \psi _ { e } ^ { t } \right) . } } \end{array}
$$

Remark 5.1. On the construction of high order contact difference schemes.

If $K$ is analytic, then one can solve $\psi ^ { t } ( x , y , z )$ from the above Hamilton–Jacobi equations in the forms of power series in time $t$ . Its coefficients are recursively determined by the $K$ and the related matrix $C _ { 0 }$ . The power series are simply given from the corresponding conic Hamiltonian generating functions $\phi ^ { t } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } )$ by $\psi ^ { t } ( x , y , z ) = \psi ^ { t } ( 1 , x , z , y )$ , since the power series expressions of $\phi ^ { t }$ with respect to $t$ from the conic Hamiltonian $H ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } K \Big ( \frac { p _ { 1 } } { p _ { 0 } } , q _ { 1 } , q _ { 0 } \Big )$ have been well given $\mathrm { i n } ^ { [ \mathrm { F W 9 4 } ] }$ . Taking a finite truncation of the power series up to order $m$ , an arbitrary integer, with respect to the time $t$ and replacing by the truncation the generating function $\psi$ in (3.12)–(3.14), then one obtains a contact difference scheme of order $m$ for the contact system defined by the contact Hamiltonian $K$ . The proofs of these assertions are similar to those in the Hamiltonian system case, hence are omitted here.

# Bibliography

[Arn78] V. I. Arnold: Ordinary Differential Equations. The MIT Press, New York, (1978).   
[Arn88] V. I. Arnold: Geometrical Methods In The Theory of Ordinary Differential Equations. Springer-Verlag, Berlin, (1988).   
[Arn89] V. I. Arnold: Mathematical Methods of Classical Mechanics. Springer-Verlag, GTM 60, Berlin Heidelberg, Second edition, (1989).   
[Etn03] J. Etnyre: Introductory lectures on contact geometry. In Proc. Sympos. Pure Math, volume 71, page 81C107. SG/0111118, (2003).   
[Fen93b] K. Feng: Symplectic, contact and volume preserving algorithms. In Z.C. Shi and T. Ushijima, editors, Proc.1st China-Japan conf. on computation of differential equationsand dynamical systems, pages 1–28. World Scientific, Singapore, (1993).   
[Fen95] K. Feng: Collected works of Feng Kang. volume I,II. National Defence Industry Press, Beijing, (1995).   
[FW94] K. Feng and D.L. Wang: Dynamical systems and geometric construction of algorithms. In Z. C. Shi and C. C. Yang, editors, Computational Mathematics in China, Contemporary Mathematics of AMS, Vol 163, pages 1–32. AMS, (1994).   
[Gei03] H. Geiges: Contact geometry. Math.SG/0307242, (2003).   
[MNSS91] R. Mrugała, J.D. Nulton, J.C. Schon, and P. Salamon: Contact structure in thermodynamic theory. Reports on Mathematical Physics, 29:109C121, (1991).   
[QZ92] M. Z. Qin and W. J. Zhu: Construction of higher order symplectic schemes by composition. Computing, 47:309–321, (1992).   
[Shu93] H.B. Shu: A new approach to generating functions for contact systems. Computers Math. Applic., 25:101–106, (1993).
