# 3.6 Quaternions

Quaternions were invented by Hamilton (1866) in the mid nineteenth century. They can be considered to be four-vectors that can be used in place of a normal $3 \times 3$ matrix, so they have some computational efficiency advantage and are commonly used in space attitude and video game applications. They are based on Euler’s theorem that any arbitrary rotation can be described as a rotation about a single axis, which is the eigenvector of the transformation, and has the same components in the rotated and unrotated systems.

# 3.6.1 Properties of quaternions

A quaternion can be thought of as the combination of a scalar, $s$ , and a three-vector, v, and can be written $( s , \mathbf { v } )$ . The vector represents the axis direction multiplied by the sine of half of the rotation angle, and the scalar is the cosine of half of the rotation angle (Section 3.6.2).

Quaternions are also an extension of complex numbers into the three-dimensional realm. In this case, the scalar is the real quantity, and the vector components are three imaginary quantities. This permits the definition of operations like addition, subtraction, multiplication, inverse, normalization, etc., as straightforward extensions of the same operations on complex numbers. The quaternions can be expressed in ordinary vector notation. So there is an entire mathematical formalism for quaternions, and for rotational dynamics cast in quaternions. Two successive rotations are represented by the multiplication of two quaternions. The advantage of using quaternions over rotation matrices is that only four quantities are required, not nine. Quaternion representation of rigid-body rotations leads to kinematical expressions involving the Euler symmetric parameters.

The most important properties of quaternions are summarized here. Let the four parameters $( q _ { 1 } , q _ { 2 } , q _ { 3 } , q _ { 4 } )$ form the components of the quaternion $\bar { q }$ as follows:

$$
\bar { q } \equiv q _ { 4 } + \mathrm { i } q _ { 1 } + \mathrm { j } q _ { 2 } + \mathrm { k } q _ { 3 } ,
$$

where i, $\mathrm { j } , \mathrm { k }$ are the hyperimaginary numbers satisfying the conditions

$$
\begin{array} { r l } & { \mathrm { i } ^ { 2 } = \mathrm { j } ^ { 2 } = \mathrm { k } ^ { 2 } = - 1 , } \\ & { \mathrm { i } \mathrm { j } = - \mathrm { j } \mathrm { i } = \mathrm { k } , } \\ & { \mathrm { j } \mathrm { k } = - \mathrm { k } \mathrm { j } = \mathrm { i } , } \\ & { \mathrm { k i } = - \mathrm { i } \mathrm { k } = \mathrm { j } . } \end{array}
$$

The conjugate, or inverse, of $\bar { q }$ is defined as

$$
\bar { q } ^ { \star } \equiv q _ { 4 } - \mathrm { i } q _ { 1 } - \mathrm { j } q _ { 2 } - \mathrm { k } q _ { 3 } .
$$

The quantity $q _ { 4 }$ is the real, or scalar, part of the quaternion, and $\mathrm { i } q _ { 1 } + \mathrm { j } q _ { 2 } + \mathrm { k } q _ { 3 }$ is the imaginary, or vector, part.

A vector in three-dimensional space, U, having the components $( U _ { 1 } , U _ { 2 } , U _ { 3 } )$ is expressed in quaternion notation, with a scalar part equal to zero, as

$$
{ \bf { U } } = \mathrm { i } U _ { 1 } + \mathrm { j } U _ { 2 } + \mathrm { k } U _ { 3 } .
$$

If the vector $\mathbf { q }$ corresponds to the vector part of $\bar { q }$ $( { \bf q } = \mathrm { i } q _ { 1 } + \mathrm { j } q _ { 2 } + \mathrm { k } q _ { 3 } )$ , then an alternate representation of $\bar { q }$ is

$$
\bar { q } = ( q _ { 4 } , \mathbf { q } ) .
$$

Quaternion multiplication is performed in the same manner as the multiplication of complex numbers, or algebraic polynomials, except that the order of the operations must be taken into account, because they are not commutative. For example, the product of two quaternions is

$$
\bar { q } ^ { \prime \prime } = \bar { q } \bar { q } ^ { \prime } = ( q _ { 4 } + \mathrm { i } q _ { 1 } + \mathrm { j } q _ { 2 } + \mathrm { k } q _ { 3 } ) ( q _ { 4 } ^ { \prime } + \mathrm { i } q _ { 1 } ^ { \prime } + \mathrm { j } q _ { 2 } ^ { \prime } + \mathrm { k } q _ { 3 } ^ { \prime } ) .
$$

Using Equation (3.31), this reduces to

$$
\begin{array} { r l } & { \bar { q } ^ { \prime \prime } = \bar { q } \bar { q } ^ { \prime } = ( - q _ { 1 } q _ { 1 } ^ { \prime } - q _ { 2 } q _ { 2 } ^ { \prime } - q _ { 3 } q _ { 3 } ^ { \prime } + q _ { 4 } q _ { 4 } ^ { \prime } ) } \\ & { \qquad = + \mathrm { i } ( + q _ { 1 } q _ { 4 } ^ { \prime } + q _ { 2 } q _ { 3 } ^ { \prime } - q _ { 3 } q _ { 2 } ^ { \prime } + q _ { 4 } q _ { 1 } ^ { \prime } ) } \\ & { \qquad = + \mathrm { j } ( - q _ { 1 } q _ { 3 } ^ { \prime } + q _ { 2 } q _ { 4 } ^ { \prime } + q _ { 3 } q _ { 1 } ^ { \prime } + q _ { 4 } q _ { 2 } ^ { \prime } ) } \\ & { \qquad = + \mathrm { k } ( q _ { 1 } q _ { 2 } ^ { \prime } - q _ { 2 } q _ { 1 } ^ { \prime } + q _ { 3 } q _ { 4 } ^ { \prime } + q _ { 4 } q _ { 3 } ^ { \prime } ) . } \end{array}
$$

If $\bar { q } = ( q _ { 4 } , \mathbf { q } )$ , then (3.36) can alternatively be expressed as

$$
\bar { q } ^ { \prime \prime } = \bar { q } \bar { q } ^ { \prime } = ( q _ { 4 } q _ { 4 } ^ { \prime } - { \bf q } \cdot { \bf q } ^ { \prime } + q _ { 4 } { \bf q } ^ { \prime } + q _ { 4 } ^ { \prime } { \bf q } + { \bf q } \times { \bf q } ^ { \prime } ) .
$$

The length, or norm, of $\bar { q }$ is defined as

$$
| \bar { q } | \equiv \sqrt { \bar { q } ^ { \star } \bar { q } } = \sqrt { \bar { q } \bar { q } ^ { \star } } = \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } + q _ { 3 } ^ { 2 } + q _ { 4 } ^ { 2 } } .
$$

# 3.6.2 Euler symmetric parameters

The Euler symmetric parameters $( q _ { 1 } , q _ { 2 } , q _ { 3 } , q _ { 4 } )$ , used to represent finite rotations, are defined by the following equations

$$
\begin{array} { l } { q _ { 1 } \equiv e _ { 1 } \sin \phi / 2 , } \\ { q _ { 2 } \equiv e _ { 2 } \sin \phi / 2 , } \\ { q _ { 3 } \equiv e _ { 3 } \sin \phi / 2 , } \\ { q _ { 4 } \equiv \cos \phi / 2 . } \end{array}
$$

Then,

$$
q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } + q _ { 3 } ^ { 2 } + q _ { 4 } ^ { 2 } = 1 .
$$

The transformation matrix, $\mathcal { A }$ , in terms of the Euler symmetric parameters, is

$$
\mathcal { A } = \left( \begin{array} { c c c } { q _ { 1 } ^ { 2 } - q _ { 2 } ^ { 2 } - q _ { 3 } ^ { 2 } + q _ { 4 } ^ { 2 } } & { 2 ( q _ { 1 } q _ { 2 } + q _ { 3 } q _ { 4 } ) } & { 2 ( q _ { 1 } q _ { 3 } - q _ { 2 } q _ { 4 } ) } \\ { 2 ( q _ { 1 } q _ { 2 } - q _ { 3 } q _ { 4 } ) } & { - q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } - q _ { 3 } ^ { 2 } + q _ { 4 } ^ { 2 } } & { 2 ( q _ { 2 } q _ { 3 } + q _ { 1 } q _ { 4 } ) } \\ { 2 ( q _ { 1 } q _ { 3 } + q _ { 2 } q _ { 4 } ) } & { 2 ( q _ { 2 } q _ { 3 } - q _ { 1 } q _ { 4 } ) } & { - q _ { 1 } ^ { 2 } - q _ { 2 } ^ { 2 } + q _ { 3 } ^ { 2 } + q _ { 4 } ^ { 2 } } \end{array} \right) .
$$

The inverse transformation matrix may be obtained by replacing $q _ { 1 } , q _ { 2 }$ and $q _ { 3 }$ by $- q _ { 1 } , - q _ { 2 }$ and $- q _ { 3 }$ , respectively, in (3.41) and leaving $q _ { 4 }$ unaltered.

The Euler symmetric parameters may be regarded as components of a quaternion $\bar { q }$ defined by

$$
\bar { q } \equiv q _ { 4 } + \mathrm { i } q _ { 1 } + \mathrm { j } q _ { 2 } + \mathrm { k } q _ { 3 }
$$

where i, j, k are hyperimaginary numbers as specified in (3.32).

# 3.6.3 Quaternion rotation

If a set of four Euler symmetric parameters, corresponding to the rigid-body rotation defined by the transformation matrix, $\mathcal { A }$ , are the components of the quaternion $\bar { q }$ , then $\bar { q }$ is the representation of the rigid-body rotation. If $\bar { q } ^ { \prime }$ corresponds to the rotation matrix, $\mathcal { A } ^ { \prime }$ , then the rotation described by the product $A ^ { \prime } \times A$ is equivalent to the rotation described by $\bar { q } \bar { q } ^ { \prime }$ . Note the inverse order of quaternion multiplication as compared with matrix multiplication.

The transformation of a vector, $\mathbf { U }$ , corresponding to multiplication by matrix $\mathcal { A }$

$$
\mathbf { U } ^ { \prime } = \mathcal { A } \times \mathbf { U }
$$

is effected in quaternion algebra by the operation

$$
{ \bf U } ^ { \prime } = \bar { q } ^ { \star } { \bf U } \bar { q } .
$$

For computation purposes, it is convenient to express quaternion multiplication in matrix form. Let the components of $\bar { q }$ form a four-vector as follows,

$$
\bar { q } = \left( \begin{array} { c } { { q _ { 1 } } } \\ { { q _ { 2 } } } \\ { { q _ { 3 } } } \\ { { q _ { 4 } } } \end{array} \right) .
$$

This procedure is analogous to expressing the complex number $c = a + \mathrm { i } b$ in the

form of the two-vector

$$
\mathbf { c } = { \binom { a } { b } } .
$$

In matrix form, (3.36) then becomes

$$
\left( \begin{array} { c } { { q _ { 1 } ^ { \prime \prime } } } \\ { { q _ { 2 } ^ { \prime \prime } } } \\ { { q _ { 3 } ^ { \prime \prime } } } \\ { { q _ { 4 } ^ { \prime \prime } } } \end{array} \right) = \left( \begin{array} { c c c c } { { q _ { 4 } ^ { \prime } } } & { { q _ { 3 } ^ { \prime } } } & { { - q _ { 2 } ^ { \prime } } } & { { q _ { 1 } ^ { \prime } } } \\ { { - q _ { 3 } ^ { \prime } } } & { { q _ { 4 } ^ { \prime } } } & { { q _ { 1 } ^ { \prime } } } & { { q _ { 2 } ^ { \prime } } } \\ { { q _ { 2 } ^ { \prime } } } & { { - q _ { 1 } ^ { \prime } } } & { { q _ { 4 } ^ { \prime } } } & { { q _ { 3 } ^ { \prime } } } \\ { { - q _ { 1 } ^ { \prime } } } & { { - q _ { 2 } ^ { \prime } } } & { { - q _ { 3 } ^ { \prime } } } & { { q _ { 4 } ^ { \prime } } } \end{array} \right) \times \left( \begin{array} { c } { { q _ { 1 } } } \\ { { q _ { 2 } } } \\ { { q _ { 3 } } } \\ { { q _ { 4 } } } \end{array} \right) .
$$

Given the quaternion components corresponding to two successive rotations, (3.44) gives the quaternion components corresponding to the total rotation.

In the same manner as elementary rotation matrices, there are elementary quaternions. The quaternion for rotation about the $x$ -axis through an angle $\theta$ is

$$
q _ { x } = \cos \theta / 2 + \mathbf { i } ~ \sin \theta / 2 ,
$$

and similarly about the $y$ -axis and $z$ -axis through angles $\omega$ and $\phi$ respectively, the quaternions are

$$
q _ { y } = \cos { \omega } / 2 + \mathbf { j } ~ \sin { \omega } / 2 ,
$$

and

$$
q _ { z } = \cos \phi / 2 + { \bf k } \ \sin \phi / 2 .
$$

# 3.7 Spherical trigonometry

Take the surface of a sphere with unit radius. All lines of interest are parts of great circles. There is only one great circle through two points, that are not on opposite ends of a diameter. A spherical triangle $A B C$ is defined by three points on the surface of the sphere, the sides being parts of great circles. $o$ is the center of the sphere, $( O A , O C ) = b$ , $( O B , O C ) = a$ , and $( O A , O B ) = c$ (see Fig. 3.4). The angles between the planes are $A = ( O A C , O A B )$ , $B = ( O B A , O B C )$ , $C =$ $( O C B , O C A )$ . Let i, j and k be non-mutually perpendicular unit vectors along $o A$ , $O B$ and $O C$ . Then $\mathbf { i } \times \mathbf { j }$ is a vector with magnitude $\sin c$ perpendicular to $A O B$ and $\mathbf { i } \times \mathbf { k }$ is a vector with magnitude $\sin b$ perpendicular to $A O C$ . Then

$$
( \mathbf { i } \times \mathbf { j } ) \cdot ( \mathbf { i } \times \mathbf { k } ) = \sin b \sin c \cos A .
$$

Using the triple scalar product (3.5) and then the triple vector product (3.6),

$$
\begin{array} { r l } & { ( \mathbf { i } \times \mathbf { j } ) \cdot ( \mathbf { i } \times \mathbf { k } ) = \mathbf { i } \cdot [ \mathbf { j } \times ( \mathbf { i } \times \mathbf { k } ) ] } \\ & { \quad = \mathbf { i } \cdot [ \mathbf { i } \cdot ( \mathbf { j } \cdot \mathbf { k } ) - \mathbf { k } \cdot ( \mathbf { i } \cdot \mathbf { j } ) ] = ( \mathbf { j } \cdot \mathbf { k } ) - ( \mathbf { i } \cdot \mathbf { k } ) \cdot ( \mathbf { i } \cdot \mathbf { j } ) , } \end{array}
$$

![](images/7e6028bb47dc2fe3cb75ab7595681d5dcad8efc6f8d2ade323e41a7a745ef816.jpg)  
Fig. 3.4. Angles in a spherical triangle.

and, replacing the unit vector products by their values as functions of angles,

$$
\sin b \sin c \cos A = \cos a - \cos b \cos c .
$$

Hence,

$$
\cos a = \cos b \cos c + \sin b \sin c \cos A ,
$$

and two other relations obtained by permutation of the letters that are known as the cosine law of spherical trigonometry.

By the definition of the vector product, the quantities in parentheses give vectors perpendicular to the planes and their cross product is the sine of the angle $A$ . The denominator eliminates the magnitude from the numerator. Thus,

$$
\sin A = | ( \mathbf { i } \times \mathbf { j } ) \times ( \mathbf { i } \times \mathbf { k } ) | / | \mathbf { i } \times \mathbf { j } | | \mathbf { i } \times \mathbf { k } | .
$$

Applying the formula for the triple vector product on $\mathbf { i } \times \mathbf { j }$ , i and $\mathbf { k }$ , one gets

$$
\sin A = | ( \mathbf { i } \times \mathbf { j } ) \cdot \mathbf { k } - ( \mathbf { i } \times \mathbf { j } ) \cdot \mathbf { j } | / \sin b \sin c .
$$

The second product is null, because $\mathbf { j }$ is perpendicular to $\mathbf { i } \times \mathbf { j } .$ so that

$$
\sin A = [ { \bf i } , { \bf j } , { \bf k } ] / \sin b \sin c ,
$$

and, finally, dividing both sides by $\sin a$ ,

$$
{ \frac { \sin A } { \sin a } } = [ \mathbf { i } , \mathbf { j } , \mathbf { k } ] / { \sin a } \sin b \sin c .
$$

The same approach can be used for sin $B$ and sin $C$ , so the result is the sine law of spherical trigonometry:

$$
{ \frac { \sin A } { \sin a } } = { \frac { \sin B } { \sin b } } = { \frac { \sin C } { \sin c } } .
$$

Two other important relations are obtained as follows. Eliminate cos $b$ in (3.45) using the similar expression of $\cos b$ , and one gets

$$
\cos a = \cos ^ { 2 } c \cos a + \cos c \sin c \sin a \cos B + \sin b \sin c \cos A ,
$$

and dividing all by $\sin b$ , one gets

$$
\sin b \cos A = \cos a \sin c - \cos c \sin a \cos B ,
$$

and, by permutation, five other equalities.

Now, let us divide (3.47) by either $\sin b \sin A$ or $\sin a \sin B$ , which are equal following (3.46) and, rearranging it, one finally gets

$$
\cos c \cos B = \sin c \cot a - \sin B \cot A ,
$$

and, by permutation, five other relations.

# 3.8 Coordinate systems

Astronomy has used and continues to use a number of different coordinate systems, reference frames, origins and transformations depending on the observations, purposes and accuracies required. The dynamical reference system at an epoch, based on the moving equinox and mean equator for a fixed time, has been the primary reference frame of the past. A new, fixed fundamental reference frame based on very distant radio sources is being introduced with sub-milliarcsecond accuracy. This change is from a dynamical system, based on the orbital motions of the planets, to a kinematic system, based on the rotations and motions of the Earth. While this reference frame is fixed at an epoch, the motions of the Earth, a common observing platform, will still be involved. Thus, the transformations between coordinate systems must be considered as necessary. The relationships or transformations may be given in spherical trigonometry expressions, or matrices and vectors. Also, there are necessary transformations for the appropriate relativistic time scales for the different reference frames (see Section 5.5).

The standard coordinate frame is defined as a right-handed system usually denoted in terms of $x$ , $y$ , z. Any positions can be designated in terms of this coordinate system. The origin and two of the axes are arbitrary. Thus, a plane, defined by two axes, and an origin, a fiducial direction defining one axis in the plane, are sufficient to define a coordinate system.

Combinations of rotations can be accomplished by matrix multiplications. Care must be exercised concerning the signs, or directions, of the rotations. Let us take, as an example, the transformation using Eulerian angles (see Fig. 3.5).

![](images/a0516feb208b7186531ce95d55c3d71b3d0ffb72a137b33b115aa5b80b46451d.jpg)  
Fig. 3.5. Successive rotations of axes about $O x$ , $O y _ { 1 }$ and $O z _ { 2 }$ .

We start from a coordinate system $( x , y , z )$ and transform it by three successive rotations:

(i) a rotation about the $O x$ axis through an angle $\theta$ transforms the coordinates $x$ , y, z of a point $P$ into $x _ { 1 } = x$ , $y _ { 1 } , z _ { 1 }$ ;   
(ii) a rotation about the new $O y _ { 1 }$ axis through an angle $\omega$ transforms the coordinates $x _ { 1 } , y _ { 1 } , z _ { 1 }$ of the point $P$ into $x _ { 2 }$ , $y _ { 2 } = y _ { 1 } , z _ { 2 }$ ;   
(iii) a rotation about the new $O z _ { 2 }$ axis through an angle $\phi$ transforms the coordinates $x _ { 2 } , y _ { 2 } , z _ { 2 }$ of the point $P$ into $x ^ { \prime }$ $' , y ^ { \prime } , z ^ { \prime } = z _ { 2 }$ .

Following Section 3.4.1, the result of these three rotations can be obtained by applying successively three matrix multiplications. If the horizontal vector representation is chosen then,

$$
\begin{array} { c c c c } { { ( x ^ { \prime } } } & { { y ^ { \prime } } } & { { z ^ { \prime } ) = ( x } } & { { y } } & { { z ) \times \left( \begin{array} { c c c } { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { \cos \theta } } & { { - \sin \theta } } \\ { { 0 } } & { { \sin \theta } } & { { \cos \theta } } \end{array} \right) } } \\ { { } } & { { } } & { { \times \left( \begin{array} { c c c } { { \cos \omega } } & { { 0 } } & { { \sin \omega } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { - \sin \omega } } & { { 0 } } & { { \cos \omega } } \end{array} \right) \times \left( \begin{array} { c c c } { { \cos \phi } } & { { - \sin \phi } } & { { 0 } } \\ { { \sin \phi } } & { { \cos \phi } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right) . } } \end{array}
$$

The multiplications must be performed from left to right.

If the vertical vector representation is chosen, then, using the notations defined in Section 3.4.1,

$$
\begin{array} { r } { \left( \begin{array} { l } { x ^ { \prime } } \\ { y ^ { \prime } } \\ { z ^ { \prime } } \end{array} \right) = \mathcal { R } _ { 3 } ( \phi ) \times \mathcal { R } _ { 2 } ( \omega ) \times \mathcal { R } _ { 1 } ( \theta ) \times \left( \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right) , } \end{array}
$$

or

$$
\begin{array} { r l r } & { } & { \left( \begin{array} { c } { x ^ { \prime } } \\ { y ^ { \prime } } \\ { z ^ { \prime } } \end{array} \right) = \left( \begin{array} { c c c c } { \cos \phi } & { \sin \phi } & { 0 } \\ { - \sin \phi } & { \cos \phi } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) \times \left( \begin{array} { c c c c } { \cos \omega } & { 0 } & { - \sin \omega } \\ { 0 } & { 1 } & { 0 } \\ { \sin \omega } & { 0 } & { \cos \omega } \end{array} \right) } \\ & { } & { \times \left( \begin{array} { c c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { \cos \theta } & { \sin \theta } \\ { 0 } & { - \sin \theta } & { \cos \theta } \end{array} \right) \times \left( \begin{array} { c } { x } \\ { y } \\ { z } \end{array} \right) = { \mathcal D } \times \left( \begin{array} { c } { x } \\ { y } \\ { z } \end{array} \right) . } \end{array}
$$

In this case, the multiplications must be performed from right to left.

The direction cosine elements of the rotation matrx $\mathcal { D }$ would then be as follows.

$$
{ \begin{array} { r l } & { a _ { 1 } ^ { 1 } = \cos \phi \cos \theta - \sin \phi \sin \theta \cos \omega } \\ & { a _ { 2 } ^ { 1 } = - \cos \phi \sin \theta - \sin \phi \cos \theta \cos \omega } \\ & { a _ { 3 } ^ { 1 } = \sin \phi \sin \omega } \\ & { a _ { 1 } ^ { 2 } = \sin \phi \cos \theta + \cos \phi \sin \theta \cos \omega } \\ & { a _ { 2 } ^ { 2 } = - \sin \phi \sin \theta + \cos \phi \cos \theta \cos \omega } \\ & { a _ { 3 } ^ { 2 } = - \cos \phi \sin \omega } \\ & { a _ { 1 } ^ { 3 } = \sin \theta \sin \omega } \\ & { a _ { 2 } ^ { 2 } = \cos \theta \sin \omega } \\ & { a _ { 3 } ^ { 3 } = \cos \omega . } \end{array} }
$$

# 3.9 Differential coordinates

In many applications, one is confronted with the problem of determining the coordinates of an object $B$ with respect to another object $A$ whose position in a global coordinate system is known $( \alpha = \alpha _ { 0 } , \delta _ { 0 } $ ). Hence the coordinates of $B$ are $\alpha _ { 0 } + \Delta \alpha$ and $\delta = \delta _ { 0 } + \Delta \delta$ . Actually, in many applications, in particular in double-star astrometry, it is customary to use spherical polar coordinates $\rho$ and $\theta$ as shown in Fig. 3.6. Here, $\rho = { \mathrm { A r c } } A B$ and $\theta$ is the position angle reckoned eastward from the direction of the North pole $P$ .

![](images/58d0867d1b956e2353b15147554e2f6de52bfe06b123d5fcd66b0c4165c6fa24.jpg)  
Fig. 3.6. Differential and standard coordinates.

# 3.9.1 Standard coordinates

In most of the cases, the observation is performed at the focal plane of a telescope, which is a geometric transform of the projection of the field onto the plane tangent to the celestial sphere at A. This transformation is called gnomonic transformation. It transforms the differential coordinates $r$ , $\theta$ into rectangular coordinates, also called “standard coordinates” $A x$ , Ay in the tangent plane $\Pi$ . Ay is directed towards the North pole, tangent to the local celestial meridian, and $A x$ is perpendicular and directed eastward, parallel to the celestial equator. Note that the orientation of the standard coordinates, as seen from the outside of the celestial sphere, is opposite to the orientation of the spherical polar coordinates. The relations are

$$
\begin{array} { r } { x = \tan r \sin \theta , } \\ { y = \tan r \cos \theta . } \end{array}
$$

The relation between $( r , \theta )$ and $( \Delta \alpha , \Delta \delta )$ is obtained using formulae (3.45) and (3.46) in the spherical triangle $P A B$ for $r$ ,

$$
\begin{array} { l } { \cos r = \sin \delta _ { 0 } \sin ( \delta _ { 0 } + \Delta \delta ) + \cos \delta _ { 0 } \cos ( \delta _ { 0 } + \Delta \delta ) \cos \Delta \alpha , } \\ { \sin r \sin \theta = \cos ( \delta _ { 0 } + \Delta \delta ) \sin \Delta \alpha . } \end{array}
$$

Dividing (3.51) by (3.50), one obtains $x$ . Applying now formula (3.47), one gets, $\sin r \cos \theta = \sin ( \delta _ { 0 } + \Delta \delta ) \cos \Delta \alpha ,$

![](images/df59962d59f647df26cb209c8920f8b5e01026b03592c930f43f664f0246a317.jpg)  
Fig. 3.7. Geometry in the $\mathbf { r } _ { 1 } { - } \mathbf { r } _ { 2 }$ plane.

which, divided by (3.50), gives $y$ . Finally, replacing $\delta + \Delta \delta$ by $\delta$ , one finally obtains,

$$
\begin{array} { c } { { x = \frac { \cos \delta \sin \Delta \alpha } { \sin \delta _ { 0 } \sin \delta + \cos \delta _ { 0 } \cos \delta \cos \Delta \alpha } , } } \\ { { y = \frac { \cos \delta _ { 0 } \sin \delta - \sin \delta _ { 0 } \cos \delta \cos \Delta \alpha } { \sin \delta _ { 0 } \sin \delta + \cos \delta _ { 0 } \cos \delta \cos \Delta \alpha } . } } \end{array}
$$

# 3.9.2 Displacement of a body

A problem encountered in many instances is the determination of the position of a body after it has moved by an angle $\theta$ . Let $\mathbf { r } _ { 1 }$ be the unit vector of the initial position and $\mathbf { r } _ { 2 }$ of the new direction. The transformation from $\mathbf { r } _ { 1 }$ to $\mathbf { r } _ { 2 }$ is a rotation by the angle $\theta$ about the normal unit vector, $\mathbf { N }$ , to the $\mathbf { r } _ { 1 } { - } \mathbf { r } _ { 2 }$ plane (see Fig. 3.7):

$$
\mathbf { N } = \mathbf { r } _ { 1 } \times \mathbf { r } _ { 2 } .
$$

In this plane let us consider a system of rectangular coordinates defined by $\mathbf { r } _ { 1 }$ and W directly perpendicular

$$
\mathbf { W } = \mathbf { N } \times \mathbf { r } _ { 1 } .
$$

The projection of $\mathbf { r } _ { 2 }$ on $\mathbf { W }$ is $\sin \theta$ and as a result

$$
\begin{array} { r } { { \bf r } _ { 2 } = { \bf r } _ { 1 } \cos \theta + ( { \bf N } \times { \bf r } _ { 1 } ) \sin \theta . } \end{array}
$$

# 3.9.3 Space standard coordinates

It is useful, for instance, in determining the space velocity of a star, to compute the rectangular equatorial coordinates $( x , y , z )$ of a vector $\mathbf { V }$ , whose coordinates in the standard system are $( p , q , r )$ with $r \neq 0$ (Fig. 3.8). Two rotations are necessary to

![](images/c1f7f7b377d976b966666b6ea4a2f262af2d4f6b58b30d9a89536c3a661de0d3.jpg)  
Fig. 3.8. Space standard coordinates.

transform space standard coordinates into the equatorial system:

(i) a rotation by an angle $( \delta - \pi / 2 )$ about the $S p$ axis, to align $S r$ with $O z$ , (ii) then a rotation of an angle $( - \alpha - \pi / 2 )$ about $S r$ (now $O z$ ) to align $S p$ and $S q$ with $O x$ and $O y$ .

One gets,

$$
\begin{array} { r l r } & { } & { \left( \begin{array} { c } { x } \\ { y } \\ { z } \end{array} \right) = \left( \begin{array} { c c c } { - \sin \alpha } & { - \cos \alpha } & { 0 } \\ { \cos \alpha } & { - \sin \alpha } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) \times \left( \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { \sin \delta } & { - \cos \delta } \\ { 0 } & { \cos \delta } & { \sin \delta } \end{array} \right) \times \left( \begin{array} { c } { p } \\ { q } \\ { r } \end{array} \right) } \\ & { } & { = \mathcal { R } \times \left( \begin{array} { c } { p } \\ { q } \\ { r } \end{array} \right) } \end{array}
$$

with

$$
\mathcal { R } = \left( \begin{array} { c c c } { - \sin \alpha } & { - \sin \delta \cos \alpha } & { \cos \delta \cos \alpha } \\ { \cos \alpha } & { - \sin \delta \sin \alpha } & { \cos \delta \sin \alpha } \\ { 0 } & { \cos \delta } & { \sin \delta } \end{array} \right) .
$$

# 3.10 Reference coordinates

There are a number of natural reference frames to use in astronomy. Origins for the reference frames can include the barycenter of the Solar System, the geocenter, and the observer. Similarly, the equator, ecliptic, and horizon are natural reference planes. Thus, reference frames are developed based on these natural origins and planes, but there is the complication that everything is in motion. Also, there are necessary transformations for the appropriate relativistic time scales for the different reference frames.

# 3.10.1 Equatorial celestial coordinates

Using a fixed reference frame of some epoch, the barycenter as the origin, and the equator as a reference plane, from a fiducial point in the equatorial plane, a right-handed coordinate frame is specified. In this reference frame, right ascensions can be measured in the equatorial plane, usually in time measurement from $_ { \mathrm { ~ 0 ~ h ~ } }$ to $^ { 2 4 \mathrm { h } }$ , but also from $0 ^ { \circ }$ to $3 6 0 ^ { \circ }$ . Declination is measured perpendicular to the equatorial plane, positive to the North from $0 ^ { \circ }$ to $9 0 ^ { \circ }$ . For a complete specification, the distance is needed along with the motions of the object in all three directions. Such a fixed barycentric reference is natural for a reference frame based on extragalactic sources, which is now called the International Celestial Reference Frame (ICRF), (see Section 7.2). Celestial reference frames can also be geocentric, with the origin at the geocenter, or topocentric, with the origin at the observer.

# 3.10.2 Terrestrial geocentric and geodetic coordinates

Geocentric terrestrial coordinates are Earth fixed and rotating with the Earth. The prime reference plane of such geocentric coordinates is the plane of the equator. The fiducial point is defined by the arbitrary prime meridian called the International Meridian, close to the Greenwich Meridian (see Fig. 3.9). This frame defines a system of rectangular coordinates $( x , y , z )$ or of spherical coordinates (longitude, $\lambda ^ { \prime }$ , latitude, $\phi ^ { \prime }$ , and radial distance, $\rho ^ { \prime }$ ). Longitude is measured positively to the East from the International Meridian and usually designated to $\pm 1 8 0 ^ { \circ }$ . Latitude is measured from the equator to $\pm 9 0 ^ { \circ }$ , positive to the North. As in the case of the sky, there is also an International Terrestrial Reference Frame (ITRF) described in Section 9.3.

The Earth is not a rigid body, nor is it a sphere. Owing to the shape of the Earth there is a need for geodetic coordinates (longitude, latitude, and height) that refer to an adopted spheroid, which best represents the shape of the Earth, and whose equatorial radius and flattening are specified. Geodetic longitude $( \lambda )$ is the same as the geocentric longitude. Geodetic latitude $( \phi )$ is equal to the inclination to the equatorial plane of the normal to the spheroid (see Fig. 3.9). Geodetic height $( h )$ is the distance above the spheroid measured along the normal to the spheroid (see also Section 9.4). One must note that this normal does not coincide with the vertical, pointing towards the zenith, and is perpendicular to the local equipotential surface. The corresponding latitude $( \phi _ { 0 } )$ and longitude $\left( \lambda _ { 0 } \right)$ are therefore different. The angle between the two directions is the deflection of the vertical (see Section 9.7.2).

![](images/d91e0d5019895ed3f224ee384fc52837d897e018630c81055cf228b60702f467.jpg)  
Fig. 3.9. Geocentric and geodetic coordinates. The direction of the zenith is different from the radius and the normal to the spheroid.

# 3.10.3 Topocentric coordinates

Topocentric coordinates are celestial cooordinates, which can be defined in terms of the local zenith and the resulting horizon plane, or in terms of the Earth’s axis of rotation and the plane of the celestial equator. The local meridian, which contains the directions of the local zenith and the axis of rotation North–South, is common to both frames as shown also on Fig. 3.10.

With respect to the horizon and the local zenith, the altitude $( a )$ is measured positively from the horizon toward the zenith, while, alternatively, the zenith distance $( z )$ is measured from the zenith toward the horizon $( z = 9 0 ^ { \circ } - a )$ . Azimuth $( A )$ is measured from $0 ^ { \circ }$ to $3 6 0 ^ { \circ }$ from North in the direction of East. However, sometimes it is measured from the South, so it is best to specify the convention being used (see Fig. 3.11). In the topocentric equatorial frame, the angular coordinates are known as local hour angle (LHA) and declination (δ). LHA is measured from $0 ^ { \circ }$ to $3 6 0 ^ { \circ }$ , or from $_ { 0 \mathrm { ~ h ~ } }$ to $2 4 ~ \mathrm { h }$ , from South in the direction of West, along the equator. The

![](images/41d2c6d6d06d03869c405aec6334ca608b841a41676556ce4b9673a52040eace.jpg)  
Fig. 3.10. Topocentric coordinates.

![](images/a598eca7ce52899c468d4a25e48bc3fe7b0e021e85f5d332c6312ebb0f1eccdf.jpg)  
Fig. 3.11. The observer $o$ and an arbitrary point $P$ shown with respect to the equatorial and hour circles, with the reference directions of zenith and North celestial pole.

LHA of a celestial object increases by about $1 5 ^ { \circ }$ , or $1 \mathrm { { h } }$ , for every hour of sidereal time. Declination is measured from the equator to the celestial pole, positive toward the North.

# 3.11 Time

For each origin there is an appropriate coordinate time (see Chapter 5). The time scale on the geoid based on atomic time standards and the international System of Units (Syst\`eme international d’unit´es, SI) unit of time (second) is the International Atomic Time (TAI). This is the measurable time scale and the basis for all other time scales, including the Coordinated Universal Time (UTC), and standard times used around the world.

The idealized time on the geoid is Terrestrial Time (TT), which is a continuation of an earlier time scale (Ephemeris Time), and is currently defined by its origin in 1977 with respect to TAI (International Atomic Time) and the SI second. Realizations of TT are designated as $\mathrm { T T } ( \mathbf { x } )$ . For instance,

$$
\mathrm { T T } ( \mathrm { T A I } ) = \mathrm { T A I } + 3 2 . 1 8 4 \mathrm { s } .
$$

By a transformation, Geocentric Coordinate Time (TCG), the time scale appropriate for geocentric coordinates, can be determined from TT (Section 5.5.1). Another transformation from TCG will give Barycentric Coordinate Time (TCB), the coordinate time appropriate for barycentric coordinates centered at the barycenter of the Solar System (Section 5.5.2). TT, TCG, and TCB are defined to satisfy the relativistic transformations between the different origins, such that units of measurements are consistent between the different coordinate systems.

There were previously defined time scales, Terrestrial Dynamical Time (TDT), which is equivalent to Terrestrial Time (TT) and Barycentric Dynamical Time (TDB), which was a time scale for the barycenter of the Solar System, such that there were only periodic differences between TDT and TDB. Unfortunately, this led to ambiguities in the determination of TDB, and differences in the values of units, depending on the time scale being used. The time scales will be further studied in Sections 5.5.1, 5.5.2, and 10.4.4.

# 3.12 Extragalactic reference frame

The extragalactic, or fundamental, reference frame provides a reference frame to which all observations can be referred. Owing to the number, wavelengths, and magnitudes of the reference sources, direct observation on the extragalactic reference frame is not always possible. Thus, observations must be made in the coordinate system available and then transformed into the extragalactic reference frame (see Section 7.2). The extragalactic reference frame defines a fixed reference frame, while most other coordinate systems are subject to motions, or rotations, so the epoch of the coordinate system must be considered. Also the motion of the observer’s platform must be included. An observer on the surface of the Earth is subject to the kinematics of the Earth with respect to the celestial reference frame, referred to as precession and nutation, and the dynamics of the Earth itself, called polar motion and Earth rotation (see Section 10.3). There are also effects due to parallax (Section 6.2) and to aberration (Section 6.3).

Distinction must also be made between small- and large-angle observations. Small-angle observations can be made with respect to the reference stars whose positions are on the extragalactic reference frame. These observations are differential and require only differential corrections (see Section 3.9). Large-angle observations must be transformed from the coordinate system of the instrument and date to the extragalactic reference frame.

In the past, the vernal equinox, one of the intersections of the ecliptic with the celestial equator was used as the origin for measuring right ascensions $( \alpha )$ along the equator. The equinox has been replaced by an origin, defined to have no rotation with respect to the extragalactic reference sources (Section 8.4). Thus, in the ICRF, right ascensions are now measured from this fixed origin along a fixed conventional equator to the hour circle.

One should mention that a reference frame can also be defined in terms of our galaxy by the plane of the Milky Way, called the galactic plane (see Section 7.7). Thus, galactic latitude is measured from the plane in the North and South directions and galactic longitude is measured in the galactic plane with a specified origin. The details concerning all the reference systems will be given in Chapters 7, 8, 9 and 10.

# 4

Treatment of astronomical data

As a rule, an astrometric observation does not directly provide the quantity sought, but rather some function of it and of a number of other parameters. The procedure that is used to obtain it is called reduction of observations. Generally, one needs to use several observations taken at different times and conditions, and treat them together. Astrometric data reduction includes taking into account a variety of effects that are described in the following chapters. But it also consists of a mathematical treatment of the data, for which one generally assumes some statistical properties. Among other things, one must be aware of the fact that a numerical result has no physical significance, and is not useful, unless there is an indication of how good the numbers are. The results must be supplemented by another number, called uncertainty, which provides an interval (sometimes called error bars) within which there is a stated probability that it includes the true value. Sometimes, when several quantities are computed simultaneously, and are mutually dependent or correlated, other numbers called correlation coefficients must be determined.

This chapter presents succinctly the most commonly used statistical tools to perform the data reduction. There are many textbooks in statistics or data treatment to which one should refer in order to go deeper in the understanding of the procedures or get more information. Let us mention, for instance, Jaech (1985), Liebelt (1967) and Silvey (1991). For more mathematical approaches, see Mendenhall et al. (1986) or Stark and Woods (1986).

# 4.1 Introduction to data reduction

Let us first give an example to illustrate how data reduction occurs in a classical problem of astrometry.

# 4.1.1 Example

Suppose that a minor planet is photographed, or observed with a CCD, together with $N$ stars, whose positions on the sky, $\mathbf { A } _ { i }$ , are known. We then wish to determine the equatorial coordinates, $\alpha$ and $\delta$ , that we denote by the vector A. The positions are determined on the plane of the plate, or of the CCD, and one obtains the coordinates $\mathbf { X } ( x , y )$ of the image of the planet and ${ \bf X } _ { i } ( x _ { i } , y _ { i } )$ of the $N$ stars.

The reduction of the plate consists of determining the relation

$$
\mathbf { F } ( \mathbf { X } , \mathbf { A } ) = 0
$$

that links the measured quantities to the unknowns. This function is not arbitrary, but its form can be deduced from the physics of the transformation between points on the celestial sphere and points on the photographic plate, namely the path of the light rays through space and the atmosphere, then through the telescope. This includes the effect of the differential atmospheric refraction, then the geometric transformation from a sphere onto a plane (gnomonic projection, see Section 3.9.1), the irregularities of the plate or of the CCD, and the aberrations of the optics. The refraction depends upon zenith distance, color of the object, temperature, pressure and the water content of the atmosphere (see Section 6.1). The gnomonic projection is a well-defined transformation, which is a function of $\mathbf { X }$ and A, as well as of the focal length of the telescope. The optical aberrations produce an additional modification of the formulae for gnomonic projection that are usually represented by a power series of $x$ and $y$ .

One may compute the leading part of F from the refraction formulae and observed values of temperature, pressure and hygrometry, and the gnomonic transformation from a nominal value of the focal length and the position of the optical axis of the telescope. The remaining effects are small, so that, together with the optical aberrations, they can be represented by power series of $x$ and $y$ . In addition, one must take into account measurement uncertainties $\varepsilon _ { j }$ on $\mathrm { X }$ and A. So the relation will become

$$
\mathbf { F } ( \mathbf { X } , \mathbf { A } , p _ { 1 } , \ldots p _ { j } , \ldots p _ { k } , \varepsilon _ { \mathbf { X } } , \ldots \varepsilon _ { \mathbf { A } } ) = 0 ,
$$

where the parameters $p _ { j }$ are the unknown coefficients of the development in power series.

# 4.1.2 Principle of data reduction

Prior to obtaining (4.1), we have actually performed two preliminary steps of the reduction, that are present in all problems. The first step has three parts.

(i) Modeling. This consists of writing the theoretical equations that link the observed and the unknown quantities.

(ii) Linearization. The model is applied to the observed quantities so that only a small part is not taken into account. This small part is assumed to be in general increments to roughly known quantities or neglected small effects. It depends upon $k$ parameters $p _ { j }$ that appear in the equations as first degree quantities, so that $\mathbf { F }$ is a linear equation in $p _ { j }$ .

(iii) Solving the linearized equations. To determine these parameters, one uses the $N$ measurements of reference stars, each giving rise to equations of condition:

$$
\mathbf { F } _ { n } \left( \mathbf { X } _ { i } , \mathbf { A } _ { i } , p _ { 1 } , \ldots p _ { j } , \ldots p _ { k } , \varepsilon ( \mathbf { X } _ { i } ) , \ldots \varepsilon ( \mathbf { A } _ { i } ) \right) = 0 ,
$$

with $1 < n < N$

The next step is to solve these $N$ vectorial Equations (4.2) with $k$ linear unknowns. This is usually, but not necessarily, done by a least-squares adjustment, which provides the values of the parameters, their uncertainties, and correlations that depend on the uncertainties with which the measurements are performed.

Finally, when these parameters $p _ { i }$ are determined, one again writes Equation (4.1), A being unknown and $\mathbf { X }$ being known. Now, $A$ , the minor planet position, can be determined.

In the following sections, we shall describe the theoretical background and practical procedures of the steps of the reduction process.

Note. It may be that the modeled equations do not represent the reality well enough to justify linearization. One must then solve a set of nonlinear equations. There is no general method to do so, and one must search, case by case, for the best way to reach an adequate solution (see Section 4.4.7).

# 4.1.3 Basic concept of uncertainties

No observation is exact, there is always an error. The error is the difference between the value measured and the true value. Since the latter is not known, it is impossible to determine it. For this reason it is preferable to speak of uncertainties. Indeed, if one could evaluate part of the error, one would add this evaluation to the value measured and improve it. Therefore this procedure would be part of the evaluation of the unknown value. At some time, however, when all possible components of errors are analyzed and their effects added, the result is still not the true value, and there remains an unknown difference, or error. However, its order of magnitude may be evaluated with some associated probability. The result is the uncertainty, which characterizes the dispersion of values that can be assigned to a measured quantity. It is a number attached to a numerical result, which depends upon the probability of the true value being within some domain around the value determined. This probability quantifies the level of confidence. One may distinguish two types of error.

(i) Random errors. These presumably arise from unpredictable, or stochastic, variations of a parameter influencing the measurement of a quantity. This is the case, for example, for the rapid atmospheric fluctuations giving rise to an agitation of the images and scintillation. The origin of these effects is the presence in the atmosphere of small $( 5 - 2 0 \mathrm { c m } )$ ) moving turbulent cells, each acting like a small lens modifying the mean direction of the rays, while focusing or de-focusing them. Another example is the residual of an ensemble of settings on the same star image by a measuring machine, or the centering error of an image spread over several CCD pixels. These errors are treated by various statistical methods, some of which are presented in Sections 4.2 and 4.4. Their evaluation provides the precision of the measurement.

(ii) Systematic errors. These correspond to effects which, if they were known, would provide a correction to the result. They may arise from an insufficient accuracy of the model, from the omission of a significant parameter in the reduction, or from some unknown instrumental bias. There are a few hints to estimate the order of magnitude of systematic errors (Section 4.3), but it is not an easy task, and it also involves a deep understanding of the problem and accumulated practice. The evaluated systematic errors provide the accuracy of the measurement.

The combination of estimated random and systematic errors is the uncertainty. Let $\hat { x }$ be the estimated value of a parameter $x$ , and $\sigma _ { x }$ be a quantity such that the true value $x _ { 0 }$ has a probability of 0.683 of being within the interval

$$
\hat { x } - \sigma _ { x } < x _ { 0 } < \hat { x } + \sigma _ { x } .
$$

Then, we can write

$$
x _ { 0 } = \hat { x } \pm \sigma _ { x } .
$$

The quantity $\sigma _ { x }$ is called the standard uncertainty or deviation. Often it is also referred to as the root mean square uncertainty (r.m.s.). Its definition will be given in the next section.

# 4.2 Random errors

Generally, the best available estimate of the expected value of $x$ that varies randomly, and for which $n$ independent values, $x _ { k }$ , have been obtained, is the arithmetic mean or average, $\mu$ ,

$$
x = \mu = { \frac { 1 } { n } } \sum _ { k = 1 } ^ { n } x _ { k } .
$$

The residual of each measurement is

$$
r _ { k } = x _ { k } - \mu .
$$

One introduces the variance of the measurements

$$
\sigma ^ { 2 } ( x _ { k } ) = { \frac { 1 } { n - 1 } } \sum _ { k = 1 } ^ { n } r _ { k } ^ { 2 } ,
$$

and the standard deviation, $\sigma ( x _ { k } )$ , is the square root of the variance.

# 4.2.1 Combination of random quantities

Generally, the quantity, $z$ , to be determined depends upon $N$ different random parameters, $x _ { i }$ . Let us assume that there exists a model that links these different quantities, and that one has

$$
z = f ( x _ { 1 } , x _ { 2 } , \dots x _ { N } ) .
$$

Let us assume that each of the parameters, $x _ { i }$ , is random with an expected value $\mu _ { i }$ and a standard deviation $\sigma _ { i }$ . Then, for small deviations of these quantities from their expected values, the first-order Taylor expansion yields

$$
z - \mu _ { z } = \sum _ { i = 1 } ^ { N } \frac { \partial f } { \partial x _ { i } } ( x _ { i } - \mu _ { i } ) .
$$

Hence, the expected value of $z$ is

$$
\mu _ { z } = f ( \mu _ { 1 } , \mu _ { 2 } , \ldots \mu _ { N } ) ,
$$

and

$$
\begin{array} { c } { ( z - \mu _ { z } ) ^ { 2 } = \displaystyle \sum _ { i = 1 } ^ { N } \left( \frac { \partial f } { \partial x _ { i } } \right) ^ { 2 } ( x _ { i } - \mu _ { i } ) ^ { 2 } } \\ { + 2 \displaystyle \sum _ { i = 1 } ^ { N } \displaystyle \sum _ { j = i + 1 } ^ { N } \left( \frac { \partial f } { \partial x _ { i } } \right) \left( \frac { \partial f } { \partial x _ { j } } \right) ( x _ { i } - \mu _ { i } ) ( x _ { j } - \mu _ { j } ) . } \end{array}
$$

The expected value of $( z - \mu _ { z } ) ^ { 2 }$ is the variance $\sigma _ { z } ^ { 2 }$ of $z$ , and similarly, for each of the parameters, the expected values of $( x _ { i } - \mu _ { i } ) ^ { 2 }$ are $\sigma _ { i } ^ { 2 }$ .

Now, in the second part of (4.7), the expected value of $( x _ { i } - \mu _ { i } ) ( x _ { j } - \mu _ { j } )$ is written as $\sigma _ { i } \sigma _ { j } \rho _ { i j }$ , where $\rho _ { i j }$ is, by definition, the correlation coefficient of $x _ { i }$ and $x _ { j }$ . The product, $\sigma _ { i j } = \sigma _ { i } \sigma _ { j } \rho _ { i j }$ , is called the covariance of $x _ { i }$ and $x _ { j }$ . If $x _ { i }$ and $x _ { j }$ are independent variables, meaning that their variations do not depend one on the other nor on a common cause, then the correlation coefficient is null. With these

notations, (4.7) becomes

$$
\sigma _ { z } ^ { 2 } = \sum _ { i = 1 } ^ { N } \left( \frac { \partial f } { \partial x _ { i } } \right) ^ { 2 } \sigma _ { x _ { i } } ^ { 2 } + 2 \sum _ { i = 1 } ^ { N } \sum _ { j = i + 1 } ^ { N } \frac { \partial f } { \partial x _ { i } } \frac { \partial f } { \partial x _ { j } } \sigma _ { i } \sigma _ { j } \rho _ { i j } .
$$

Finally, one introduces the variance–covariance matrix, the symmetric matrix $| \sigma _ { i j } |$ , whose elements are $\sigma _ { i i } = \sigma _ { i } ^ { 2 }$ in row $i$ , column $i$ and $\sigma _ { i j }$ both in row $i$ , column $j$ and row $j$ , column $i$ .

Example. Coordinates $\alpha$ and $\delta$ of a star in a fixed reference system change with time proportional to its proper motion $\mu _ { \alpha }$ and $\mu _ { \delta }$ . Let $\alpha _ { 0 }$ and $\delta _ { 0 }$ be its position at some time origin; its values at time $t$ are

$$
\begin{array} { c } { { \alpha = \alpha _ { 0 } + t \mu _ { \alpha } , } } \\ { { { } } } \\ { { \delta = \delta _ { 0 } + t \mu _ { \delta } , } } \end{array}
$$

provided that $t$ is not too large, and the star is not close to the poles. Following the notation of the Hipparcos Catalogue, let us set

$$
\begin{array} { r } { \alpha ^ { * } = \alpha \cos \delta _ { 0 } , } \\ { \mu _ { \alpha } ^ { * } = \mu _ { \alpha } \cos \delta _ { 0 } . } \end{array}
$$

In these notations, Equations (4.9) become :

$$
\begin{array} { c } { { \alpha ^ { * } = \alpha _ { 0 } ^ { * } + t \mu _ { \alpha } ^ { * } , } } \\ { { \delta = \delta _ { 0 } + t \mu _ { \delta } . } } \end{array}
$$

Since the determination of proper motions is based upon observed values of the position, $\mu _ { \alpha } ^ { * }$ and $\alpha ^ { * }$ on one side, $\mu _ { \delta }$ and $\delta$ on the other side are correlated. The corresponding correlation coefficients are given in the catalogue. Applying (4.8), one gets

$$
\begin{array} { r l } & { \sigma _ { \alpha ^ { * } } ^ { 2 } ( t ) = \sigma _ { \alpha ^ { * } } ^ { 2 } ( 0 ) + 2 t \rho _ { \alpha ^ { * } \mu \alpha ^ { * } } ( 0 ) \sigma _ { \mu \alpha ^ { * } } ( 0 ) \sigma _ { \alpha ^ { * } } ( 0 ) + t ^ { 2 } \sigma _ { \mu \alpha ^ { * } } ^ { 2 } ( 0 ) , } \\ & { \sigma _ { \delta } ^ { 2 } ( t ) = \sigma _ { \delta } ^ { 2 } ( 0 ) + 2 t \rho _ { \delta \mu \delta } ( 0 ) \sigma _ { \delta } ( 0 ) \sigma _ { \mu \delta } ( 0 ) + t ^ { 2 } \sigma _ { \mu \alpha } ^ { 2 } ( 0 ) . } \end{array}
$$

The degradation of the standard errors of positions depends on the correlation coefficients, as well as on individual variances.

# 4.2.2 Generalization to functions of $N$ variables

Let us generalize Equation (4.5), assuming a transformation of an $N$ -vector $\mathbf { X }$ into an $N$ -vector $\mathbf { z }$ , and let us call, respectively, $\Delta \mathbf { x }$ and $\Delta \mathbf { z }$ the differences from their expected values. The equivalent to (4.5) now is

$$
\Delta \mathbf { z } = \mathcal { I } _ { f } \left( \mathbf { x } \right) \Delta \mathbf { x } ,
$$

where $\mathcal { I } _ { f }$ is the $N \times N$ Jacobian of the transformation,

$$
\mathcal { I } _ { f } = \left( \frac { \partial f _ { j } } { \partial x _ { i } } \right) _ { 1 \leq i , j \leq N } ,
$$

as evaluated at the expected values. Let $\mathcal { C }$ be the variance–covariance matrix of $\Delta \mathbf { x }$ . It can be computed as

$$
\mathcal { C } = \Delta \mathbf { x } \times \Delta \mathbf { x } ^ { \top } ,
$$

where $\Delta \mathbf { x }$ is a column vector and $\Delta \mathbf { x } ^ { \top }$ is the corresponding transposed (row) vector. Then, the theory of transformation of functions provides the new variance– covariance matrix

$$
\mathcal { S } = \mathcal { I } _ { f } \times \mathcal { C } \times \mathcal { T } _ { f } ^ { \prime } ,
$$

where $\mathcal { T } _ { f } ^ { \prime }$ is the transposed matrix of $\mathcal { I } _ { f }$ . This result is to be applied in particular to coordinate transformations for which the number of dimensions is not modified by the transformation.

# 4.2.3 Linear combination of random quantities

Let us consider a function $z$ that has the following form

$$
z = \sum _ { i = 1 } ^ { N } A _ { i } x _ { i } ,
$$

where $A _ { i }$ are constants. In this case, the variance of $z$ is

$$
\sigma _ { z } ^ { 2 } = \sum _ { i = 1 } ^ { N } A _ { i } ^ { 2 } \sigma _ { i } ^ { 2 } + 2 \sum _ { i = 1 } ^ { N } \sum _ { j = i + 1 } ^ { N } A _ { i } A _ { j } \sigma _ { i j } .
$$

A particular case is when all the parameters $x _ { i }$ are independent. Then, the variance of $z$ is:

$$
\sigma _ { z } ^ { 2 } = \sum _ { i = 1 } ^ { N } { A _ { i } } ^ { 2 } { \sigma _ { i } } ^ { 2 } .
$$

The variance of $z$ is the same linear combination of variances as z.

Example. Let us compute the variance of the uncertainty in measuring a plate. Let us assume that it is because of the random atmospheric error, whose variance is $\sigma _ { \mathrm { A } } ^ { 2 }$ , the random error of the measuring machine, whose variance is $\sigma _ { \mathrm { M } } ^ { 2 }$ , and the random error due to the sensitivity distribution in the plate, whose variance is $\sigma _ { \mathrm { S } } ^ { 2 }$ . Clearly these three phenomena are independent and have no influence on one another. Then,

the variance of the measurement is

$$
\sigma _ { z } ^ { 2 } = \sigma _ { \mathrm { A } } ^ { 2 } + \sigma _ { \mathrm { M } } ^ { 2 } + \sigma _ { \mathrm { S } } ^ { 2 } ,
$$

provided that the three quantities are expressed in the same units. The standard uncertainty of $z$ is therefore:

$$
\sigma _ { z } = \sqrt { \sigma _ { \mathrm { A } } ^ { 2 } + \sigma _ { \mathrm { M } } ^ { 2 } + \sigma _ { \mathrm { S } } ^ { 2 } } .
$$

This formulation is very commonly used to evaluate the standard uncertainties of measurements.

# 4.2.4 Normal probability density function

One may extend the notion of successive values of a random parameter to a continuous function, that takes for each possible value of the random parameter – called hereafter the random variable – the associated probability. Such a function is called the probability density function (pdf). Among the many possible pdfs, one has a particular status. It results from the central limit theorem, which states that the sum of a large number of mutually independent random variables tends to a probability density function called the Gaussian, or normal, density function given by

$$
f ( x ) = \frac { 1 } { \sqrt { 2 \pi \sigma } } \exp \left[ \frac { - ( x - \mu ) ^ { 2 } } { 2 \sigma ^ { 2 } } \right] ,
$$

where $\mu$ is the mean of the probability distribution, and $\sigma$ is the standard deviation. It is represented in Fig. 4.1. Table 4.1 gives the level of confidence, $C$ , for different intervals around the mean, that is the probability for a value to be within the interval

$$
\mu - k _ { p } \sigma < x < \mu + k _ { p } \sigma ,
$$

where $k _ { p }$ is called the coverage factor. It is given by

![](images/8a1be11fca4d33058b090b344b505aa29182789b4ebf5dc8b6eace949f224e4b.jpg)  
Fig. 4.1. The normal probability density function.

Table 4.1. Levels of confidence for different intervals of $x$ symmetric with respect to the mean   

<table><tr><td>Coverage factor k p</td><td>Level of confidence C</td></tr><tr><td>1σ</td><td>68.27%</td></tr><tr><td>1.645σ</td><td>90.00%</td></tr><tr><td>2σ</td><td>95.45%</td></tr><tr><td>2.5g</td><td>98.70%</td></tr><tr><td>3g</td><td>99.73%</td></tr></table>

An important property of this pdf is that any random variable, formed by taking a linear combination of independent normally distributed random variables, is itself also normally distributed. This normal pdf is commonly assumed to represent the probability density function of random quantities contributing to measurements. It is indeed a fact that uncertainties of many physical measurements are well represented by the normal law. This justifies the importance of this pdf in astrometry.

# 4.2.5 Other probability density functions

The Gaussian pdf can be generalized to as many independent random variables as needed. For instance, let $X _ { 1 }$ and $X _ { 2 }$ be two random variables, and $x _ { 1 }$ and $x _ { 2 }$ the measurements with mean values $\mu _ { 1 }$ and $\mu _ { 2 }$ , and the corresponding variances $\sigma _ { 1 } ^ { 2 }$ and $\sigma _ { 2 } ^ { 2 }$ . To be general, one should also allow for a correlation coefficient $\rho$ . Then the bivariant pdf is

$$
\begin{array} { c } { { f ( x _ { 1 } , x _ { 2 } ) = \displaystyle \frac { 1 } { \pi \sigma _ { 1 } \sigma _ { 2 } \sqrt { 1 - \rho ^ { 2 } } } \exp \left[ - \frac { 1 } { 2 ( 1 - \rho ^ { 2 } ) } \right. } } \\ { { \displaystyle \left. \times \left( \frac { ( x _ { 1 } - \mu _ { 1 } ) ^ { 2 } } { \sigma _ { 1 } ^ { 2 } } + \frac { 2 \rho ( x _ { 1 } - \mu _ { 1 } ) ( x _ { 2 } - \mu _ { 2 } ) } { \sigma _ { 1 } \sigma _ { 2 } } + \frac { ( x _ { 2 } - \mu _ { 2 } ) ^ { 2 } } { \sigma _ { 2 } ^ { 2 } } \right) \right] . } } \end{array}
$$

If $X _ { 1 }$ and $X _ { 2 }$ are independent, then $\rho = 0$ .

This can be extended to $N$ random variables $X _ { 1 } , \dots X _ { N } ( x _ { 1 } \dots x _ { N } )$ in which we introduce all the quantities of the variance–covariance matrix $| \sigma _ { i j } |$ defined in Section 4.2.1:

$$
f ( x _ { 1 } , x _ { 2 } \dots x _ { N } ) = \left( { \frac { 1 } { 2 \pi } } \right) ^ { 0 . 5 N } { \sqrt { | \sigma _ { i j } | } } \exp \left[ - { \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { N } \sum _ { j = 1 } ^ { N } \sigma _ { i j } ( x _ { i } - \mu _ { i } ) ( x _ { j } - \mu _ { j } ) \right] ,
$$

where $ { \mu } _ { 1 } , \dots  { \mu } _ { N }$ are the expected values of $x _ { 1 } , \ldots . x _ { N }$

There are many other probability density functions that may be useful in some particular situations. Let us present the three most frequently used.

(i) Chi-square pdf. This is closely related to the Gaussian distribution. It describes the statistics of a sample of $N$ observations of a quantity that obeys a Gaussian pdf with a variance $\sigma ^ { 2 }$ . One is led to compute the average

$$
\bar { x } = \sum _ { i = 1 } ^ { N } \frac { x _ { i } } { N } ,
$$

and the sample variance

$$
s ^ { 2 } = \frac { 1 } { N - 1 } \left( \sum _ { i = 1 } ^ { N } { x _ { i } } ^ { 2 } - N \bar { x } ^ { 2 } \right) .
$$

One then considers the random variable

$$
y = \frac { \nu s ^ { 2 } } { \sigma ^ { 2 } } ,
$$

where $\nu = N - 1$ is the degree of freedom. This random variable has a pdf called the chi-square pdf, $\chi _ { \nu } ^ { 2 } ( y )$ , which has the following form,

$$
\chi _ { \nu } ^ { 2 } ( y ) = K y ^ { ( \nu - 2 ) / 2 } \exp ( y / 2 ) ,
$$

where the constant $K$ is chosen in such a way that the integral from $- \infty$ to $+ \infty$ of $\chi ^ { 2 } ( \nu )$ is equal to 1. One has

$$
K = \frac { 1 } { 2 ^ { \nu / 2 } \varGamma ( \nu / 2 ) } ,
$$

in which $\varGamma$ is the gamma function:

$$
\varGamma ( x ) = \int _ { 0 } ^ { \infty } \exp ( - t ) t ^ { x - 1 } \mathrm { d } t .
$$

The chi-square pdf is usually tabulated as a function of the degree of freedom, and is used to find the probability that $s ^ { 2 }$ exceeds some given number, showing how well the sample is representative of the distribution. Figure 4.2 gives graphs of some chi-square pdfs.

(ii) Gamma-type pdfs. These constitute a large family of probability density functions,

$$
G ( y , a , b ) = \frac { 1 } { b { \cal { I } } ( a ) } y ^ { a - 1 } \exp ( - y / b )
$$

with $a , b$ and $y$ positive. The chi-square pdf is a particular case of gamma pdfs. Another particular case is the exponential pdf

$$
E ( y , b ) = \frac { 1 } { b } \exp ( - y / b ) ,
$$

corresponding to $a = 1$ .

![](images/38f7f21e6b67fdd73b006d27f3075961e09c25f42bb61daad187b322f5517d22.jpg)  
Fig. 4.2. Examples of chi-square pdfs for various values of the degrees of freedom $\nu$ .

(iii) Uniform pdf. This is a useful probability density function for evaluating the effect of rounding errors, which may, in some cases, be non-negligible in an error budget. The pdf is constant in a finite interval of the variable

$$
\begin{array} { l } { \displaystyle f ( y ) = \frac { 1 } { b - a } , \quad \mathrm { w i t h } \quad a \le y \le b , } \\ { \displaystyle f ( y ) = 0 , \mathrm { e l s e w h e r e } . } \end{array}
$$

The corresponding variance is

$$
\sigma ^ { 2 } = \frac { ( b - a ) ^ { 2 } } { 1 2 } .
$$

# 4.3 Systematic errors

In contrast to random errors, there is no rigorous definition of systematic errors. They are the types of error that cannot be characterized by an uncertainty computed by using the methods described in the preceding section. The uncertainty of a given source of errors can in some cases be treated by random methods (e.g. described by a normal pdf), and in some cases it has to be considered as giving rise to an offset depending upon the level of accuracy required.

A simple way to distinguish the two types of error is to see what happens if the variance is multiplied by some number larger than one and all the parameters increased accordingly. If the random error treatment is justified, the mean value should not change, and only its standard deviation changes. If the mean value is modified, then one says that parameters produce a bias. In this case, one should model the effect involved, and consider the parameters that describe this effect as part of the unknowns, either directly in the equations, or by adding further conditions from parallel measurements, or theoretical considerations. However, in all cases, there exist some remaining unidentified biases, and there is no way to recognize their existence, so that in practice, one is led to treat the left over errors as an uncertainty.

The vocabulary to be used in stating the uncertainty of a measurement depends upon the type of errors that are present in the process. If all the parameters introduced in the model are random, then the standard uncertainty represents what is called precision. If there are, in addition, biases, one should evaluate them, and add them to the precision and obtain what is called the accuracy of the determination. In other terms, one may say that the precision describes the random distribution of variations in the measurements, whereas the accuracy is an estimation of the difference between the measurement and the true value, which is inaccessible. For this reason, it is preferable to use the word uncertainty, which represents a combination of both types of errors.

The significant quantity is accuracy, but it cannot be treated rigorously as a random quantity when using the result of the measurement to obtain some other quantity. Some effects of the bias can be computed by using the model, while the effect of the precision may be extended by using formula (4.7). It can also be evaluated from comparisons between observations performed independently, and under different conditions. The uncertainty of the result will be the quadratic sum of the precision and of the assumed effects of the biases.

The only possible way to reduce biases is to introduce their effects in the model, and consider the parameters governing them as unknown parameters, whose variances will be determined together with the variances of other unknowns.

# 4.4 Method of least squares

The method that we are going to present is not the only possible method capable of estimating the unknown parameters of a measurement model. It has, however, many important positive properties which justify its very wide use, provided that some conditions are satisfied; in particular, that the model can be linearized with respect to the unknown parameters (next section).

Let $\mathbf { X } ( x _ { 1 } , x _ { 2 } \ldots x _ { n } )$ be the vector of unknowns, A the vector of measurements $( a _ { 1 } , a _ { 2 } \ldots a _ { m } )$ , and $\mathbf { P } ( p _ { 1 } , p _ { 2 } \ldots p _ { q } )$ the vector of the parameters entering the model which relates $\mathbf { A }$ to $\mathbf { X }$ . One has

$$
\mathbf { A } + \mathbf { E } = \mathbf { F } \left( \mathbf { X } , \mathbf { P } \right) ,
$$

with $n + q$ unknowns and $\mathbf { E } ( \varepsilon _ { 1 } , \varepsilon _ { 2 } \dots \varepsilon _ { m } )$ is an unknown error vector of the measurements A.

# 4.4.1 Linearization of the equations

The method of least squares is designed to find the most probable estimation, $\hat { a } _ { i }$ , of the components $a _ { i }$ of A. The assumptions are:

- the pdf of all the unknowns is the normal probability density function;   
- the unknowns are sufficiently small, so that one may neglect their squares.

The first assumption is met if all the parameters, which may cause a bias, are taken into account by (4.13), so that their uncertainties may be considered as random. The second assumption implies that, unless the unknowns are indeed small, one knows an approximate value $\mathbf { X } _ { 0 } ( x _ { 1 } ^ { 0 } , x _ { 2 } ^ { 0 } \dots x _ { n } ^ { 0 } )$ and ${ \bf P } _ { 0 } ( p _ { 1 } ^ { 0 } , p _ { 2 } ^ { 0 } \ldots p _ { q } ^ { 0 } )$ , so that one can develop (4.13) as follows,

$$
\begin{array} { l } { { \displaystyle { \bf A } = { \bf F } ( { \bf X } _ { 0 } , { \bf P } _ { 0 } ) + \sum _ { i = 1 } ^ { n } \left( \frac { \partial { \bf F } ( { \bf X } _ { 0 } , { \bf P } _ { 0 } ) } { \partial x _ { i } } \right) \hat { \bf \delta } x _ { i } } \ ~ } \\ { { \displaystyle ~ + \sum _ { j = 1 } ^ { q } \left( \frac { \partial { \bf F } ( { \bf X } _ { 0 } , { \bf P } _ { 0 } ) } { \partial p _ { j } } \right) \hat { \bf \delta } p _ { j } - { \bf E } } , } \end{array}
$$

where $\delta x _ { i }$ and $\delta p _ { j }$ are the new unknowns and, following our assumption, the second order of the development is negligible, and can be added to $\mathbf { E }$ without changing its randomness. This equation does not formally distinguish the actual unknowns and the parameters. So we shall not individualize the second part further, and shall include in $\mathbf { X }$ all unknowns, whether they are of astronomical interest or are additional parameters. Writing (4.14) for each component of A, one gets a set of $m$ equations

$$
a _ { j } - F _ { j } ( x _ { 1 } , \dots x _ { k } ) = \sum _ { i = 1 } ^ { k } \bigg ( \frac { \partial F _ { j } ( x _ { 1 } , \dots x _ { k } ) } { \partial x _ { i } } \bigg ) \delta x _ { i } - \varepsilon _ { j } ,
$$

where $1 \leq j \leq m$ and $k = n + q$ is the number of unknown quantities, while $\varepsilon _ { j }$ describes the statistical properties of the uncertainties of $a _ { j }$ . This set of linear equations in $\delta x _ { i }$ cannot be solved if $k < j$ . Therefore, it is necessary to increase the number of equations by performing a series of observations obeying the same model. In the example of a plate reduction given in Section 4.1, one measures a sufficient number of reference stars, each providing two equations. The beauty of the method of least squares is that it allows any number $m$ of Equations (4.15), provided that $m$ is strictly larger than the number $k$ of unknowns. A general experience is that it is desirable that $m$ be of the order of two or three times $k$ . The quantity $m - k = \nu$ is the degree of freedom as introduced in Section 4.2.5.

The ensemble of Equations (4.15) is called the equations of condition, or design equations, the coefficients of the second member forming the design matrix $\mathcal { D }$ .

Equations (4.15) can then be written as

$$
\begin{array} { r } { { \bf C } = \mathcal { D } { \bf Y } + { \bf E } , } \end{array}
$$

where $\mathbf { Y }$ is the vector of the new unknowns $( \delta x _ { 1 } \dots \delta x _ { k } )$ , and $\mathbf { C }$ is the vector of the left-hand members of (4.15)

$$
\mathbf { C } = ( a _ { j } - F _ { j } ( x _ { 1 } \ldots x _ { k } ) ) , \quad j = 1 , m .
$$

# 4.4.2 Principle of the method of least squares

If the conditions stated in the beginning of Section 4.4.1 are met, the expected value of $\mathbf { E }$ is zero, and its variance is

$$
\frac { 1 } { m - 1 } \sum _ { j = 1 } ^ { m } \varepsilon _ { j } ^ { 2 } .
$$

In reality, of course, this is not the case. The objective of the method of least squares is to determine the vector $\mathbf { Y }$ that minimizes the sum of the squares of the components of $\mathbf { E }$ ,

$$
\sum _ { j = 1 } ^ { m } \boldsymbol { \varepsilon } _ { j } ^ { 2 } = \mathbf { E } ^ { \top } \cdot \mathbf { E } = \left( \mathbf { C } - \mathcal { D } Y \right) ^ { \top } \cdot ( \mathbf { C } - \mathcal { D } \mathbf { Y } ) ,
$$

where the superscript $\top$ denotes that the vector, or the matrix, is transposed. The quantity in (4.17) is minimum, if its derivative with respect to $\mathbf { Y }$ is zero. The righthand member of (4.17) can also be written as

$$
\mathbf { C } ^ { \top } \cdot \mathbf { C } - \left( \mathcal { D } \mathbf { Y } \right) ^ { \top } \cdot \mathbf { C } - \mathbf { C } \cdot \mathcal { D } \mathbf { Y } + \left( \mathcal { D } \mathbf { Y } \right) ^ { \top } \cdot \mathcal { D } \mathbf { Y } .
$$

Its derivative with respect to $\mathbf { Y }$ is

$$
- \mathscr { D } \mathbf { C } + \mathscr { D } ^ { \top } \mathscr { D } \mathbf { X } + ( \mathscr { D } \mathbf { Y } ) ^ { \top } \mathscr { D } - \mathbf { C } ^ { \top } \mathscr { D } = 0 ,
$$

which is equivalent to

$$
\begin{array} { r } { \mathcal { D } ^ { \top } \mathcal { D } \mathbf { Y } = \mathcal { D } ^ { \top } \mathbf { C } . } \end{array}
$$

The product of the transposed design matrix by itself is a square matrix of dimension $k$ . One can, hence, solve (4.18), and obtain the solution

$$
\begin{array} { r } { \hat { \mathbf Y } = ( \mathcal { D } ^ { \top } \mathcal { D } ) ^ { - 1 } \mathcal { D } ^ { \top } \mathbf C , } \end{array}
$$

which is the estimate of $\mathbf { Y }$ by the least-squares procedure.

# 4.4.3 Weighted least-squares solution

An important result concerning this solution is the Gauss–Markov theorem, which states that the least-squares estimate, $\hat { \mathbf Y }$ , given by (4.19) is a better estimation than a solution given by any other possible linear estimator, provided that all the components of $\mathbf { E }$ have the same variance and are uncorrelated. Now, to estimate the variance of $\varepsilon _ { j }$ , which is the variance of an observation, is not a straightforward task, and it often presents a non-negligible qualitative aspect. We shall assume that this is done.

The absence of correlation normally implies that the unknowns are well chosen, in the sense that they correspond to the minimum needed to describe the model. For example, a rotation around a given point in a plane should be represented by a single angle $\theta$ , and not by $\sin \theta$ and cos $\theta$ .

A simple way to equalize the variances in Equation (4.13) is to multiply each equation by the inverse of $\varepsilon _ { j }$ . Let $\mathcal { G }$ be a square matrix of order $m$ , whose elements are all zeroes except for the main diagonal components, which are $g _ { j } = \varepsilon _ { j } ^ { - 1 } .$ . This operation is performed on (4.16) by multiplying both sides of the equation by $\mathcal { G }$

$$
\mathcal { G } D \mathbf { Y } + \mathcal { G } \mathbf { E } = \mathcal { G } \mathbf { C } ,
$$

so that the right-hand member of (4.17) becomes

$$
{ ( { \mathcal { G } } \mathbf { C } - { \mathcal { G } } D \mathbf { Y } ) } ^ { \top } ( { \mathcal { G } } \mathbf { C } - { \mathcal { G } } D \mathbf { Y } ) .
$$

Let $\mathcal { W }$ be the square matrix of order $k$

$$
\mathcal { W } = \mathcal { G } ^ { \top } \mathcal { G } .
$$

After some calculations, (4.19) becomes

$$
\begin{array} { r } { \hat { \mathbf { Y } } = ( \mathcal { D } ^ { \top } \mathcal { W } \mathcal { D } ) ^ { - 1 } \mathcal { D } ^ { \top } \mathcal { W } \mathbf { C } . } \end{array}
$$

The matrix $\mathcal { W }$ is the weight matrix. All its terms are zeroes except on the main diagonal where they are $w _ { j j } = \varepsilon _ { j } ^ { - 2 }$ .

The weight matrix may be generalized in the case when there are correlations between the unknowns. Then, the non-diagonal terms are not all null. We shall not deal with this case.

The procedure described by Equation (4.20) is the weighted least-squares procedure to which the Gauss–Markov theorem applies.

Remark. The definition of $\mathcal { G }$ , as adopted here, implies that the variances and, hence, the standard deviations are unity. One could use $g _ { i i } = s \varepsilon _ { j } ^ { - 1 }$ , where $s$ is any appropriate value of the common standard deviation.

It is possible to verify whether the assumption concerning the variances are significant by computing the variance of the residuals, by applying (4.17) to the estimated unknowns, and extending (4.4) to $m - k$ degrees of freedom. One gets

$$
s _ { 0 } ^ { 2 } = \frac { 1 } { m - k } ( \mathbf { C } - \mathcal { D } \hat { \mathbf { Y } } ) ^ { \top } \mathcal { W } ( \mathbf { C } - \mathcal { D } \mathbf { Y } ) .
$$

Or, if we call $\mathbf { R } ( r _ { i } )$ the vector of residuals,

$$
\begin{array} { l } { \displaystyle { { \bf R } = { \bf C } - \mathcal { D } \hat { \bf Y } } , } \\ { \displaystyle { s _ { 0 } ^ { 2 } = \frac { 1 } { m - k } { \bf R } ^ { \top } \mathcal { W } { \bf R } } . } \end{array}
$$

One can show that $s _ { 0 } ^ { 2 }$ is an unbiased estimate of the unit weight variance.

# 4.4.4 Variance–covariance matrix of the estimation

An important result is that the variance-covariance matrix for the estimation $\hat { \mathbf Y }$ is

$$
\begin{array} { r } { \mathcal { V } = ( \mathcal { D } ^ { \top } \mathcal { W } \mathcal { D } ) ^ { - 1 } . } \end{array}
$$

The proof involves complicated algebra, and we shall not give it. Let us note that (4.20) can also be written as

$$
\begin{array} { r } { \hat { \mathbf Y } = \mathcal { V } D ^ { \top } \mathcal { W } \mathbf C . } \end{array}
$$

The diagonal terms of the matrix $\nu$ , $v _ { i i }$ are the formal variances of $\hat { y } _ { i }$ . They are computed as though the model described by (4.15) is exact. They are actually underestimations of the true values, and in order to get more realistic estimations, one should multiply them by the unit-weight variance, $s _ { 0 } ^ { 2 }$ . So, finally, the best estimate of the standard deviation of $\hat { y } _ { i }$ is

$$
\hat { \sigma _ { i } } = s _ { 0 } \sqrt { v _ { i i } } .
$$

The best estimates of correlation coefficients are not affected by $s _ { 0 }$ , and one has

$$
\hat { \rho } _ { i j } = \frac { \hat { \sigma } _ { i j } } { \hat { \sigma } _ { i } \hat { \sigma } _ { j } } = \frac { v _ { i j } } { \sqrt { v _ { i i } } \sqrt { v _ { j j } } } .
$$

# 4.4.5 Chi-square test

An important problem is to check whether the model used is indeed representative of the reality as described by the observations (C). Many tests exist that help in answering this question. Let us describe the simplest one, which is particularly well fit to a least-square solution: the chi-square test.

Let us introduce the random variable $u$

$$
u \ = \sum _ { i = 1 } ^ { n } \left( { \frac { r _ { i } } { s _ { 0 } } } \right) ^ { 2 } ,
$$

and apply the probability distribution of $u$ , as given in Section 4.2.5,

$$
\chi ^ { 2 } ( \nu , u ) = \left( 2 ^ { \nu / 2 } { \cal T } \left( \frac { \nu } { 2 } \right) \right) ^ { - 1 } u ^ { ( \nu - 2 ) / 2 } \exp { ( - u / 2 ) } ,
$$

Table 4.2. Limiting values $\chi _ { 0 } ^ { 2 }$ of $\chi ^ { 2 }$ for given probability $p$   

<table><tr><td>V</td><td>p = 0.1</td><td>p = 0.05</td><td>p = 0.01</td><td>p = 0.001</td></tr><tr><td>5</td><td>9.2</td><td>11.2</td><td>15.1</td><td>20.5</td></tr><tr><td>10</td><td>16.0</td><td>18.3</td><td>23.2</td><td>29.6</td></tr><tr><td>20</td><td>28.4</td><td>31.4</td><td>37.6</td><td>45.3</td></tr><tr><td>30</td><td>40.3</td><td>43.8</td><td>56.9</td><td>59.7</td></tr><tr><td>40</td><td>51.8</td><td>55.8</td><td>63.7</td><td>73.4</td></tr><tr><td>60</td><td>74.4</td><td>79.1</td><td>88.4</td><td>99.6</td></tr><tr><td>80</td><td>96.6</td><td>101.9</td><td>112.3</td><td>124.8</td></tr><tr><td>100</td><td>118.5</td><td>124.3</td><td>135.8</td><td>149.5</td></tr></table>

where $\nu$ is the degree of freedom. When $\nu$ increases, the chi-square pdf tends towards a normal distribution, whose mean and variance are $\nu$ and $2 \nu$ , respectively. These functions, or their integrals, giving the probability of having $u < u _ { 0 }$ are found in most books on probability, or current statistical software. One can associate the level of confidence, $c$ , given by

$$
c = \int _ { \chi _ { 0 } ^ { 2 } } ^ { \infty } \chi ^ { 2 } \mathrm { d } \chi ^ { 2 } ,
$$

which is the probability for $\chi ^ { 2 }$ to exceed the observed value of $\chi _ { 0 } ^ { 2 }$ . Table 4.2 gives, for a few values of the degree of freedom $\nu$ , the probability $p$ of getting values of $\chi ^ { 2 }$ larger than $\chi _ { 0 } ^ { 2 }$ .

# 4.4.6 Goodness of fit

The computation of $\chi ^ { 2 }$ , corresponding to the residuals of a least-squares solution, and the determination of the probability that it exceeds the computed value, gives an indication of the quality of the fit as regards the adopted model. If the value obtained is such that the probability of exceeding it is small, this is a clear indication that some systematic effects remain in the residuals, and that there is a good probability that the observations do not fit the model. If the values obtained are larger than those given in, or interpolated from, Table 4.2, one must very seriously consider the adequacy of the model.

However, it might be that only a very small number of large residuals increases $\chi ^ { 2 }$ . If this is the case, it is possible that the corresponding observations were spoiled by some spurious event. For instance, in the case of the reduction of a photographic plate, it could be that a reference position of a star was incorrectly copied, or even that a star was mistaken for another. These cases should first be investigated by considering the distribution of residuals, which should obey the normal law. If there is a small number of large residuals, one should re-do the least-square solution omitting these outliers. If this is sufficient to significantly increase the probability of getting the new $\chi ^ { 2 }$ , the new solution is acceptable. But, if that is not the case, and the $\chi ^ { 2 }$ is still too high, then the linearized model used to describe the observations is not adequate, and there remains at least one cause for systematic errors.

A drawback of the chi-square test is that the values used to compare $\chi ^ { 2 }$ with $\chi _ { 0 } ^ { 2 }$ are dependent upon the degree of freedom. If $\nu$ is large enough ( $\lfloor \nu > 2 0$ or 30), there exists another test which has the advantage of being independent of $\nu$ . It is derived from what is called the $F 2$ statistics, which is a transformation of $\chi ^ { 2 }$ statistics of the least-square fit,

$$
F 2 = \left( \frac { 9 \nu } { 2 } \right) ^ { 1 / 2 } \left( \left( \frac { \chi ^ { 2 } } { \nu } \right) ^ { 1 / 3 } + \frac { 2 } { 9 \nu } - 1 \right) .
$$

If $\chi ^ { 2 }$ follows the chi-square distribution with a degree of freedom equal to $\nu$ , then $F 2$ is approximately normal with a mean value of zero and a unit standard deviation. The value of $F 2$ is the goodness of fit. A value larger than 3 is a clear indication of a modeling error (probability smaller than 0.0027), especially after removing outliers.

# 4.4.7 Problems in linearization

There exist cases for which no linearization is possible. This happens when no evident approximate solution exists and, in particular, when there exists a choice among several sets of parameters that could fit the observations and still differ by quantities of order zero. Such a case occurred, for instance, in the reduction of double-star data from the Hipparcos mission. Because of the periodicity of $s = 1 { ' } 2 0 8$ in the grid, the projected separation, $\rho$ , of a double star would give the same modulation if it were $\rho \pm k s$ , $k$ being an integer (see Fig. 2.7). If there is no a priori knowledge of the actual separation, for instance from ground-based observations, $k$ is an additional unknown quantity. However, since the observations were made at different angles relative to the two stars, $k$ is not always the same, so it cannot enter explicitly in the equations of condition. The solution was to consider in the space of the unknowns $X = \rho \sin \theta$ , and $Y = \rho \cos \theta$ , where $\theta$ is the angle of position) the sum of the square of the residuals as a function

$$
F ( X , Y , k )
$$

and to search for the deepest among the minimums of $F$ , which are distributed in a regular, two-dimensional grid. Then, starting from such a minimum, one may linearize the equations. In other cases, different methods have to be found by deep analysis of the problem, and no general rule can be suggested.

Now, if one is rather close to the solution, but still too far for a linearization to be justified, there exist, in mathematical software packages, nonlinear leastsquare programs that may be applied. However, caution should be taken that the convergence of the iterations is correct by monitoring the evolution of the sum of the squares of the residuals. Actually, it is good practice to apply an iterative procedure for the normal least-squares. One adds the solution S obtained in a first approximation to $\mathbf { X }$ , and iterate the procedure, thus controlling the behavior of the residuals. In all the cases, it is advisable to check the results with the chi-square test and compute the goodness of fit.

# 4.5 Additional aspects

The Gaussian distribution is not the only distribution useful in astronomy. In this section, we shall present the Poisson distribution, which has specific applications when observations have discrete values, for instance when they are photon counts. Another often-encountered problem concerns sparse data, which requires a treatment that is different from the ones presented above. Finally, statistical treatment is not limited to stationary cases; one often needs to evaluate the stability in time of some parameter. We shall consider these three special problems in this section.

# 4.5.1 Poisson distribution

A Poisson distribution is one of discrete probability expressed as

$$
P ( r ) = \frac { \mu ^ { r } \exp ( - \mu ) } { r ! } ,
$$

where $r$ is an integer and $\mu$ is a positive number. There is a recurrence relation between successive probabilities,

$$
P ( r + 1 ) = \frac { \mu P ( r ) } { r + 1 } .
$$

This probability distribution corresponds to a random physical mechanism, called a Poisson process. It occurs, for example, when an event happens in the mean $\mu$ times in some interval of time $\Delta t$ . The probability of having $r$ such events during a given interval $\Delta t$ is $P ( r )$ .

The variance of a Poisson distribution can be obtained, after some algebra, and is,

$$
\sigma ^ { 2 } = \sum _ { r = 0 } ^ { \infty } ( r - \mu ) ^ { 2 } P ( r ) = \mu .
$$

![](images/e439c5059d349951370088957114bcd9163f0ad0c6ea38bdb3726b106c867a76.jpg)  
Fig. 4.3. Probabilities $p ( n )$ of Poisson distributions for different $\mu$ .

Figure 4.3 gives the shape of Poisson distribution for different values for $\mu$ . The probability of observing at least $N$ events is:

$$
P ( r \geq N ) = \sum _ { r = N } ^ { \infty } \frac { \mu ^ { r } \exp ( - \mu ) } { r ! } .
$$

# 4.5.2 Robust estimations

A major problem in estimation is what to do with outliers. Suppressing one or two observations modifies not only the variance – a result that is generally sought – but also the estimation itself. An estimation is robust if the removal of outliers has the least possible effect on the value found.

For instance, a least-square fit of points on a straight line (Fig. 4.4) may be biased by the presence of several outliers. In this particular case, the removal of outliers, as described in the preceding section, might affect good points rather than points actually widely distributed in the plane, because, as shown in Fig. 4.4, some correct points may be more distant from a wrong solution than false ones. Here a graphic representation of the situation allows one to recognize the real situation, and to find the best procedure to obtain the correct solution.

As an example, the median of a distribution is a robust estimation of the central value. For $N$ values, $x _ { i } , i = \Delta \dots N$ , sorted into ascending order, the median is

![](images/79031210ef2a625f83272e671b13dc475ae5a766672d59b11115b40c81aa3454.jpg)  
Fig. 4.4. Faulty linear least-square fit to a straight line sensitive to outliers.

![](images/7875e7700286d5918791b516821c542017731e4c9231a08b9a29bf05b21a1a0b.jpg)  
Fig. 4.5. Example of Allan variance for a cesium frequency standard and a hydrogen maser.

defined by

$$
\begin{array} { l } { { \displaystyle x _ { m } = x _ { N - 1 } / 2 \quad \mathrm { f o r } N \mathrm { o d d } , } } \\ { { \displaystyle x _ { m } = \frac { 1 } { 2 } ( x _ { N / 2 } + x _ { N / 2 - 1 } ) \quad \mathrm { f o r } N \mathrm { e v e n } . } } \end{array}
$$

If the distribution has a strong central clustering, the suppression of $x _ { 1 }$ or $x _ { N }$ does not modify the estimation of the median by more than the mean distance between clustered values, while the mean is modified by $x _ { 1 } / N$ or $x _ { N } / N$ .

# 4.5.3 Allan variance

Let us consider a parameter that may not be stable in time; one wishes to quantify its stability, and see how much it changes with time. This can be the case of the frequency of an atomic clock, the rate of rotation of a pulsar, or the period of a variable star.

Let $T$ be the repetition rate of measurements, $x _ { k }$ , such that their times are $t _ { k } =$ $t _ { 0 } + k T$ . Let us consider three successive samples, $x _ { k } , x _ { k + 1 }$ , and $x _ { k + 2 }$ , and consider the deviation of the central sample from the mean of the adjacent ones:

$$
y _ { k } = x _ { k + 1 } - ( x _ { k + 2 } + x _ { k } ) / 2 .
$$

The Allan variance for a period $\tau = m T$ is proportional to the average of the square of the deviation for this period. An estimation is

$$
\sigma _ { a } = \frac { K } { 2 ( m - 1 ) } \sum _ { k = 1 } ^ { m - 1 } y _ { k } ^ { 2 } ,
$$

where $K$ is a constant that depends on the characteristics of the parameter, in particular its power spectrum. Computing the Allan variance for increasing values of $\tau$ , one can evaluate, for instance, for how long a clock is stable, and at what point various perturbations become predominant. Figure 4.5 shows, as an example, the Allan variances of a laboratory cesium standard and a hydrogen maser. The latter is very stable, but only for one day, then instabilities appear. This is particularly useful in VLBI. On the contrary, the stability of cesium standards remains comparable over several years, a fundamental quality for an accurate clock.

# 5 Principles of relativity

For many years, the theory of relativity was ignored for astrometry because the effects were much smaller than the accuracies being achieved. For the motions of bodies of the Solar System, Newtonian theory was adequate, provided that some relativistic corrections were introduced. Actually, there was a long period of questioning whether the theory of relativity was correct or not, and thus relativistic corrections were introduced in a manner to determine whether observational data could then be better represented.

However, over the past 30 years, there has been a very significant improvement in the accuracies of observations, all confirming the conclusions of general relativity. So its introduction became not only acceptable, but necessary. In 1976, the International Astronomical Union introduced relativistic concepts of time and the transformations between various time scales and reference systems. In 1991, it extended them to reference frames and to astrometric quantities. Now, with plans for microarcsecond astrometry and with time standards approaching accuraries of one part in $1 0 ^ { - 1 6 }$ , and better in the future, it is necessary to base all astrometry, reference systems, ephemerides, and observational reduction procedures on consistent relativistic grounds. This means that relativity must be accepted in its entirety, and that concepts, as well as practical problems, must be approached from a relativistic point of view. In 2000, the IAU enforced this approach further by extending the 1991 models for future requirements in such a way that they become valid to accuracies several orders better than those currently achieved in 2000.

The aim of this chapter is to provide the physical background, the definitions, and the basic expressions of the Theory of General Relativity that are useful for astrometric applications in regions of weak gravitational fields, such as the one that characterizes the Solar System. Whenever it is necessary, they will be applied in the next chapters of the book. For more details on the concepts developed in this chapter, see Mould (1994), Fock (1976), Ohanian (1980), or Rindler (1977).

# 5.1 Relativity principles

The general concept of relativity is as old as the advent of mechanics. It was based on what was called, and still is in a more particular sense, an inertial frame. A reference frame is called inertial if a free particle, that is not subject to any external force, moves without acceleration with respect to it. In the case of Newtonian mechanics, such free particles move with constant speed along straight lines. The Galilean principle of relativity states that if a reference frame is inertial, all reference frames that move with a constant linear speed with respect to it are also inertial. This Newtonian mechanical relativity principle was generalized by Einstein, who stated that all inertial frames are totally equivalent for the performance of all physical experiments. In Einstein’s Theory of Relativity, the inertial frame is generalized by the notion of a free falling isolated local frame, in an electrically and magnetically shielded environment, sufficiently small that inhomogeneities in the external fields can be ignored throughout the volume, and in which self-gravitating effects are negligible. Under these conditions, any local non-gravitational test experiment performed in a free falling frame is independent of where and when in the Universe it is performed and of the velocity of the frame.

Two theories of relativity, respectively called special and general, are modifications of the classical physical laws in order to enter into the framework of this principle. To take just one example, the invariance of the speed of light, whatever the speed of the observer, was demonstrated for the first time in 1887 by Michelson and Morley with an interferometer that could rotate. They attempted to show that there was a difference in the speed of light as measured in the direction of the Earth orbital motion, compared with the speed at right angles. The result was negative and led to the principle of relativity, as far as the independence on the velocity of the frame is concerned. This will be developed in the following sections.

# 5.2 Special relativity

Special relativity, proposed by Einstein in 1906, was the outcome of an effort to build a coherent theory that would explain, without introducing an hypothetical ether, several effects that were found to contradict the Newtonian principles upon which physics – and especially mechanics – were based until that time.

# 5.2.1 The Newtonian mechanical concepts

Newtonian mechanics postulates the existence of an absolute, Euclidean space and an independent, absolute time. The points in space are referred to three coordinates in some system of rectangular axes. The Galilean relativity concept applies, which is that all systems of coordinates are equivalent (or interchangeable) provided they move with respect to one another with a constant velocity; the laws of mechanics are everywhere the same. Let us consider a fixed, reference coordinate system $S$ (ox yz and a time scale $t$ ) and a second system $S ^ { \prime }$ $( o ^ { \prime } x ^ { \prime } y ^ { \prime } z ^ { \prime }$ and a time scale $t ^ { \prime }$ ), which moves with respect to $S$ with a velocity $\mathbf { V }$ and is identical to $S$ at time $t = 0$ . Assuming that $\mathbf { V }$ is along the $o x$ axis with a speed equal to $v$ , the relations between the coordinates are

$$
\begin{array} { l } { x = x ^ { \prime } + v t , } \\ { y = y ^ { \prime } , } \\ { z = z ^ { \prime } , } \\ { t = t ^ { \prime } . } \end{array}
$$

The last equation expresses the fact that the time is absolute, that is, the same in all equivalent reference frames.

Let $P$ be a point at $x _ { 0 }$ $) , y _ { 0 } , z _ { 0 }$ at time $t = 0$ , which moves in $S ^ { \prime }$ along the $o ^ { \prime } x ^ { \prime }$ axis with a velocity $v ^ { \prime }$ .

$$
\begin{array} { l } { { x ^ { \prime } = x _ { 0 } + v ^ { \prime } t , } } \\ { { y ^ { \prime } = y _ { 0 } , } } \\ { { z ^ { \prime } = z _ { 0 } , } } \\ { { t ^ { \prime } = t . } } \end{array}
$$

The position of $P$ in system $S$ is therefore

$$
\begin{array} { l } { { { x = x _ { 0 } + ( v + v ^ { \prime } ) t , } } } \\ { { { y = y _ { 0 } , } } } \\ { { { z = z _ { 0 } . } } } \end{array}
$$

So, we have the following result: the velocity with respect to the fixed system is equal to the sum of the velocity $v$ of the moving system and the velocity $v ^ { \prime }$ with respect to the moving system

$$
\boldsymbol { V } = \boldsymbol { v } + \boldsymbol { v } ^ { \prime } .
$$

This can of course be generalized to the three coordinates.

# 5.2.2 Invariance of the speed of light

As already mentioned, the law of addition of velocities was tested by Michelson and Morley in 1887, assuming that $P$ is moving at the speed of light, $c$ . At that time, it was believed that the light was a property of ether, and an experiment was devised to determine the speed of the Earth’s orbital velocity with respect to the ether, measuring it in the direction of the Earth’s motion, or opposite to it, or perpendicular to it. In all the cases, the speed was found to be the same. Equation (5.4) does not match this experimental result if $v = c$ . One has

![](images/a12a8331190b9b9d50075f10a6410d4f4c1a3a5b167d515378d81e049da70b72.jpg)  
Fig. 5.1. A light pulse bouncing between the mirrors $A$ and $B$ as seen by an observer moving with a velocity $v$ .

$$
c = c \pm v .
$$

The interpretations of this result are that there is no ether and that no velocity larger than the speed of light, $c$ , can exist. The light is seen travelling with the speed $c$ by any observer, whether the source, or the observer, moves or not. This has many consequences. Let us describe one of them.

Consider a pair of parallel mirrors, $A B$ , separated by a rod of length, $L$ , and a light pulse bouncing from one to the other. This constitutes a periodic system, a clock, with a period $P = 2 t = 2 L / c$ , which can be measured by an observer fixed with respect to this experimental equipment (system $S$ ).

A second observer in a system, $S ^ { \prime }$ , moves with a speed $v$ perpendicular to the rod (Fig. 5.1). After time $t$ , the rod will appear to him at the location $A ^ { \prime } B ^ { \prime }$ . For him, the light pulse will have followed the segment $A B ^ { \prime }$ , but at the same speed $c$ during the same time $t$ . Let us apply the theorem of Pythagorus to the triangle $A A ^ { \prime } B ^ { \prime }$ . One gets:

$$
A B ^ { \prime 2 } = c ^ { 2 } t ^ { 2 } = v ^ { 2 } t ^ { 2 } + L ^ { 2 } .
$$

A similar conclusion will be obtained for the time when the light pulse bounces back to $A$ seen as at $A ^ { \prime \prime }$ by the moving observer. Solving for $t$ , one obtains

$$
t = { \frac { L } { c { \sqrt { \frac { 1 - v ^ { 2 } } { c ^ { 2 } } } } } } .
$$

The apparent period is $P ^ { \prime } = P \gamma$ , with $\gamma = ( 1 - v ^ { 2 } / c ^ { 2 } ) ^ { - 1 / 2 }$ . The moving clock ticks slower by the amount $1 / \gamma$ . The general result, a consequence of the constancy of the speed of light, is that a time interval measured in a moving frame is longer than the same one measured in a frame fixed with respect to the events. This property is known as the time dilatation. One may similarly describe another fundamental result, which is the contraction of moving objects. A rod in motion relative to an observer will have its length contracted along the direction of the motion as compared with an identical rod at rest. If $L$ is the length at rest, the apparent length is $L ^ { \prime } = L / \gamma$ when moving at velocity $v$ along $L$ .

For more details on these properties, together with some others, see Mould (1994).

# 5.2.3 The Lorentz transformation

The preceding properties were formalized by Lorentz, who proposed the following transformation between coordinates $x$ , $y$ , z, (r), and time $t$ in a given reference frame $S$ , and $x ^ { \prime }$ , $y ^ { \prime }$ , z  , $( \mathbf { r } ^ { \prime } )$ , and $t ^ { \prime }$ in another frame $S ^ { \prime }$ moving with a constant speed $\mathbf { V }$ with respect to $S$ .

The generalized vectorial form of Lorentz transformation (Fock, 1976) is

$$
\begin{array} { l } { { \bf { r } } ^ { \prime } = { \bf { r } } - \gamma { \bf { V } } t + ( \gamma - { \bf { \nabla } } I ) { \bf { V } } \left( { \bf { V } } \cdot { \bf { r } } \right) / V ^ { 2 } } \\ { t ^ { \prime } = \gamma [ t - ( { \bf { V } } \cdot { \bf { r } } ) / c ^ { 2 } ] , } \end{array}
$$

where $\gamma$ is the quantity already mentioned, $\gamma = ( 1 - V ^ { 2 } / c ^ { 2 } ) ^ { - 1 / 2 }$ . The inverse formulae are

$$
\begin{array} { r l } & { \mathbf { r } = \mathbf { r } ^ { \prime } + \gamma \mathbf { V } t ^ { \prime } + ( \gamma - 1 ) \mathbf { V } ( \mathbf { V } \cdot \mathbf { r } ^ { \prime } ) / V ^ { 2 } } \\ & { t = \gamma [ t ^ { \prime } + ( \mathbf { V } \cdot \mathbf { r } ^ { \prime } ) / c ^ { 2 } ] . } \end{array}
$$

Let us now assume that the velocity $\mathbf { V }$ is along the $x$ -axis, ${ \bf V } = ( v _ { x } , 0 , 0 )$ . The $y$ and $z$ components reduce to an identity. The $x$ component becomes:

$$
x ^ { \prime } = x - \gamma v _ { x } t + ( \gamma - 1 ) \left( { \frac { v _ { x } } { v _ { x } } } \right) ^ { 2 } x .
$$

The terms independent of $\gamma$ vanish and Equations (5.5) become:

$$
\begin{array} { l } { x ^ { \prime } = \gamma ( x - v _ { x } t ) , } \\ { y ^ { \prime } = y , } \\ { z ^ { \prime } = z , } \\ { t ^ { \prime } = \gamma ( t - v _ { x } x / c ^ { 2 } ) . } \end{array}
$$

The inverse formulae are similar except that the sign of $v _ { x }$ changes, since it represents the velocity of $S$ with respect to $S ^ { \prime }$ .

These simplified formulae are in the form in which the Lorentz transformation is usually presented in reference books. But in astrometry, the situation is generally such that one wishes to choose axes that are not constrained by the relative motion of reference planes.

Let us now derive the Lorentzian equivalent to the Newtonian law of addition of velocities. Let $\mathbf { V }$ be the constant velocity of a reference system $S ^ { \prime }$ with respect to the system S. In S, a point $\mathbf { r }$ has a velocity $\mathbf { U } = \mathrm { d } \mathbf { r } / \mathrm { d } t$ , and in $S ^ { \prime }$ , its coordinates are $\mathbf { r } ^ { \prime }$ , $t ^ { \prime }$ and the velocity is $\mathbf { U } ^ { \prime } = \mathrm { d } \mathbf { r } ^ { \prime } / \mathrm { d } t ^ { \prime }$ .

Let us differentiate (5.6) with respect to $t$

$$
\begin{array} { l } { { \displaystyle { \frac { \mathrm { d } \mathbf { r } } { \mathrm { d } t } } = { \frac { \mathrm { d } \mathbf { r } ^ { \prime } } { \mathrm { d } t ^ { \prime } } } { \frac { \mathrm { d } t ^ { \prime } } { \mathrm { d } t } } + \gamma \mathbf { V } { \frac { \mathrm { d } t ^ { \prime } } { \mathrm { d } t } } + \left( \gamma - 1 \right) \left( \mathbf { V } \cdot { \frac { \mathrm { d } \mathbf { r } ^ { \prime } } { \mathrm { d } t ^ { \prime } } } { \frac { \mathrm { d } t ^ { \prime } } { \mathrm { d } t } } \right) \mathbf { V } / { V ^ { 2 } } } } \\ { { \displaystyle \mathrm { d } t = \gamma \left[ \mathrm { d } t ^ { \prime } + \left( \mathbf { V } \cdot { \frac { \mathrm { d } \mathbf { r } ^ { \prime } } { \mathrm { d } t ^ { \prime } } } \mathrm { d } t ^ { \prime } \right) / c ^ { 2 } \right] . } } \end{array}
$$

Or, with the new notation,

$$
\frac { \mathrm { d } t ^ { \prime } } { \mathrm { d } t } = \frac { 1 } { \gamma ( 1 + \mathbf { V } \cdot \mathbf { U } ^ { \prime } / c ^ { 2 } ) } ,
$$

from which one derives,

$$
\mathbf { U } = \frac { \mathbf { U } ^ { \prime } + \gamma \mathbf { V } + \left( \gamma - 1 \right) ( \mathbf { V } \cdot \mathbf { U } ^ { \prime } ) \mathbf { V } / V ^ { 2 } } { \gamma ( \mathbf { 1 } + \mathbf { V } \cdot \mathbf { U } ^ { \prime } / c ^ { 2 } ) } .
$$

The inverse formula is

$$
\mathbf { U } ^ { \prime } = \frac { \mathbf { U } - \gamma \mathbf { V } + ( \gamma - \mathbf { 1 } ) ( \mathbf { V } \cdot \mathbf { U } ) \mathbf { V } / \mathbf { V } ^ { 2 } } { \gamma ( \mathbf { 1 } - \mathbf { V } \cdot \mathbf { U } / c ^ { 2 } ) } .
$$

If (5.8) is applied to the simplified case with ${ \bf V } = ( v _ { x } , 0 , 0 )$ , one gets

$$
u _ { x } = \frac { u _ { x } ^ { \prime } + \gamma v _ { x } + ( \gamma - 1 ) ( v _ { x } u _ { x } ^ { \prime } ) v _ { x } / { v _ { x } } ^ { 2 } } { \gamma ( 1 + v _ { x } u _ { x } ^ { \prime } / c ^ { 2 } ) } ,
$$

the term $u _ { x } ^ { \prime }$ cancels out and $\gamma$ is a factor of both terms of the quotient, so that one gets

$$
u _ { x } = { \frac { v _ { x } + u _ { x } ^ { \prime } } { 1 + v _ { x } u _ { x } ^ { \prime } / c ^ { 2 } } } ,
$$

which is the formula that is usually given in reference books together with

$$
\frac { \mathrm { d } t } { \mathrm { d } t ^ { \prime } } = \gamma ( 1 + v _ { x } u _ { x } ^ { \prime } / c ^ { 2 } ) .
$$

# 5.2.4 The metric of special relativity

Let us consider a light pulse emitted by $o$ at time $t = 0$ . At time $t$ , in the system $S$ , it reaches a point $P$ of coordinates $x , y , z$ , and one has

$$
c ^ { 2 } t ^ { 2 } = x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ,
$$

or

$$
x ^ { 2 } + y ^ { 2 } + z ^ { 2 } - c ^ { 2 } t ^ { 2 } = 0 .
$$

In the system $S ^ { \prime }$ the coordinates of $P$ are $x ^ { \prime }$ , $y ^ { \prime } , z ^ { \prime }$ , but because of the invariance of the speed of light, which is also $c$ in the system $S ^ { \prime }$ , one has similarly

$$
x ^ { \prime 2 } + y ^ { \prime 2 } + z ^ { \prime 2 } - c ^ { 2 } t ^ { \prime 2 } = 0 .
$$

The quantity (5.10) is an invariant interval. Written in a differential form, considering an infinitesimal distance $O P$ , one has

$$
\mathrm { d } x ^ { \prime 2 } + \mathrm { d } y ^ { \prime 2 } + \mathrm { d } z ^ { \prime 2 } - c ^ { 2 } \mathrm { d } t ^ { \prime 2 } = 0 .
$$

Now, let us generalize this by considering an event characterized by its three coordinates $x , y , z$ and the time $t$ in the system $S$ . Let us compute the quantity $x ^ { \prime 2 } + y ^ { \prime 2 } + z ^ { \prime 2 } - c ^ { 2 } t ^ { \prime 2 }$ by applying the simplified Lorentz transformation (5.8). Let us consider the inverse equations:

$$
\begin{array} { l } { x = \gamma ( x ^ { \prime } + v t ) } \\ { y = y ^ { \prime } } \\ { z = z ^ { \prime } } \\ { t = \gamma ( t ^ { \prime } + v x ^ { \prime } / c ^ { 2 } ) } \end{array}
$$

and compute

$$
x ^ { 2 } + y ^ { 2 } + z ^ { 2 } - c ^ { 2 } t ^ { 2 } = \gamma ( x ^ { \prime } + v t ^ { \prime } ) ^ { 2 } + y ^ { \prime 2 } + z ^ { \prime 2 } - c ^ { 2 } \gamma ^ { 2 } ( t ^ { \prime } + v x ^ { \prime } / c ^ { 2 } ) ^ { 2 } .
$$

The terms multiplying $\gamma$ are

$$
\begin{array} { r l } & { G = x ^ { \prime 2 } + 2 v x ^ { \prime } t ^ { \prime } + v ^ { 2 } t ^ { \prime 2 } - c ^ { 2 } t ^ { \prime 2 } - 2 v x ^ { \prime } t ^ { \prime } - v ^ { 2 } x ^ { \prime 2 } / c ^ { 2 } , } \\ & { G = x ^ { \prime 2 } ( 1 - v ^ { 2 } / c ^ { 2 } ) - c ^ { 2 } t ^ { \prime 2 } ( 1 - v ^ { 2 } / c ^ { 2 } ) = ( x ^ { \prime 2 } - c ^ { 2 } t ^ { \prime 2 } ) / \gamma . } \end{array}
$$

Therefore, one finally gets:

$$
x ^ { 2 } + y ^ { 2 } + z ^ { 2 } - c ^ { 2 } t ^ { \prime 2 } = x ^ { \prime 2 } + y ^ { \prime 2 } + z ^ { \prime 2 } - c ^ { 2 } t ^ { \prime 2 } = s ^ { 2 } .
$$

The quantity is an invariant for all transformations between reference systems in uniform motion, one with respect to others. This quantity, $s ^ { 2 }$ , is a generalized

distance that is also called the invariant interval or metric of special relativity. It is usually presented for an infinitesimal displacement and written

$$
\mathrm { d } s ^ { 2 } = \mathrm { d } x ^ { 2 } + \mathrm { d } y ^ { 2 } + \mathrm { d } z ^ { 2 } - c ^ { 2 } \mathrm { d } t ^ { 2 } .
$$

By analogy with the space coordinates $x , y , z$ , and because $c t$ has the dimension of a length, $t$ is called coordinate time. It results that in special relativity (and actually also in general relativity), an event is specified by four coordinates: three space coordinates and the time coordinate.

All the properties already described, and those that will be presented in the next subsections, are a consequence of the metric (5.12). This fully describes the properties of space-time, invariant from the coordinate system that could be chosen, provided that it is inertial, meaning that it is not accelerated in any fashion.

# 5.2.5 Coordinate time and proper time

Let us consider two events that occur after a time dt at the same point of the reference frame, so that $\mathrm { d } x = \mathrm { d } y = \mathrm { d } z = 0 .$ . Then the metric reduces to

$$
\mathrm { d } s ^ { 2 } = - c ^ { 2 } \mathrm { d } t ^ { 2 } .
$$

The time $t$ is linked to the object. This new time is called proper time $\tau$ and is the one that rules all the local physics of the point considered. The metric (5.12) can therefore be written in the general case as

$$
\mathrm { d } s ^ { 2 } = - c ^ { 2 } \mathrm { d } \tau ^ { 2 } = \mathrm { d } x ^ { 2 } + \mathrm { d } y ^ { 2 } + \mathrm { d } z ^ { 2 } - c ^ { 2 } \mathrm { d } t ^ { 2 } .
$$

In an integrated form, this relation means that for any interval $s ^ { 2 }$ between two events, the quantity

$$
\scriptstyle { \sqrt { - s ^ { 2 } } } / { c }
$$

equals the reading of a clock that travels at a constant speed between the two events.

In order to obtain the relation between the proper and the coordinate times, let us consider the components of the velocities as measured with respect to the coordinate time $t$ . Changing the signs, one gets

$$
\begin{array} { c } { { c ^ { 2 } \left( \displaystyle \frac { \mathrm { d } \tau } { \mathrm { d } t } \right) ^ { 2 } = c ^ { 2 } - \left[ \left( \displaystyle \frac { \mathrm { d } x } { \mathrm { d } t } \right) ^ { 2 } + \left( \displaystyle \frac { \mathrm { d } y } { \mathrm { d } t } \right) ^ { 2 } + \left( \displaystyle \frac { \mathrm { d } z } { \mathrm { d } t } \right) ^ { 2 } \right] , } } \\ { { \displaystyle \displaystyle \frac { \mathrm { d } \tau } { \mathrm { d } t } = \sqrt { 1 - \frac { v ^ { 2 } } { c ^ { 2 } } } = 1 / \gamma . } } \end{array}
$$

This is exactly the expression obtained in presenting the time dilatation in Section 5.2.3. Coming back to it, one sees that the moving observer measures the period of the clock in coordinate time, while the experimenter, fixed with respect to it, measures it in proper time.

![](images/20f7d0c06db1165d2ee5638b2b8bd9a6f04f5ccbab72e971d55e14bd286066ef.jpg)  
Fig. 5.2. Minkowsky’s $x { - } t$ diagram. Events in the lower part of the cone have been seen by $o$ in the past. Those in the upper part will be seen sometime in the future. Outside the cone, are events inaccessible to the observer until some time when the light issued will reach the world line of the observer.

For an observer at rest within his or her reference frame – for instance at the origin – the coordinate time and the proper time are identical, but this is not the case as soon as he or she observes a moving object and assigns time to events on this object. This can be visualized in Minkowsky’s diagram (Fig. 5.2). A line on the diagram represents the path of an object and is called a world line. The world lines of light reaching $o$ are straight lines defined by $x = c t$ . One can see, using Equation (5.13), that $\tau = 0$ along the line for a photon; the proper time between emission and reception does not change. The vertical line corresponds to a fixed point in space and one has $t = \tau$ . Inside the cone, one has $\left| x \right| < \left| c t \right|$ . In the lower part (past), events occur before the origin event. Outside the cone no causal connection with the origin event is possible, because the velocity of any information linking the two events would be larger than the speed of light.

If we consider the path $O P O ^ { \prime }$ of a traveler, $A$ , leaving $o$ for $P$ , and then coming back to the origin $O ^ { \prime }$ after some time $t _ { 0 }$ . Since during all the path, the proper time of $A$ is always smaller than $t$ , the proper life time of $A$ between the event $o$ and $O ^ { \prime }$ is smaller than for an observer who remained fixed. This is the famous paradox of Langevin’s twins. However, since accelerations must exist to reverse the path, the problem is not as simple, and one has to introduce the acceleration expressions in general relativity in order to describe completely the behavior of the traveling twin, so that one cannot consider that there is a strict symmetry between the twins. We shall not dwell more on this paradox (see for instance Mould, 1994), but we have taken this opportunity to illustrate the basics of mechanics in special relativity.

# 5.2.6 Mass and acceleration

We have already seen that the expression of velocity is not the same if reckoned in the local environment with proper time, or in a general reference frame with coordinate time. In any reference frame, the components of the velocity are:

$$
\left( { \frac { \mathrm { d } x } { \mathrm { d } t } } , { \frac { \mathrm { d } y } { \mathrm { d } t } } , { \frac { \mathrm { d } z } { \mathrm { d } t } } \right) = \gamma ( v _ { x } , v _ { y } , v _ { z } ) = \gamma \mathbf { v } ,
$$

where $v _ { x } , v _ { y }$ and $v _ { z }$ are the components of the velocity $\mathbf { V }$ . In local coordinates, with $t = \tau$ (proper time), we have

$$
v = \sqrt { v _ { x } ^ { 2 } + v _ { y } ^ { 2 } + v _ { z } ^ { 2 } }
$$

and

$$
\gamma = 1 .
$$

Now, if we consider the Newtonian law of conservation of linear momentum in this inertial frame, we can still write it in the local frame using proper time

$$
\mathbf { p } = m \mathbf { v } ,
$$

where $m$ is the inertial mass.

But if we transcribe it in the general coordinate system, using coordinate time t instead of $\boldsymbol { \tau } , \mathbf p$ and $\mathbf { V }$ become $\mathbf { P }$ and $\mathbf { V }$ , and, we have

$$
\mathbf { P } = m \mathbf { V } .
$$

In this case the modulus can be written as a function of proper quantities

$$
P ^ { 2 } = m ^ { 2 } v ^ { 2 } \left( { \frac { \mathrm { d } \tau } { \mathrm { d } t } } \right) ^ { 2 } = m ^ { 2 } v ^ { 2 } \left( 1 - { \frac { v ^ { 2 } } { c ^ { 2 } } } \right) .
$$

The law of conservation of momentum implies here that $m$ is not constant and is velocity dependent. If $m _ { 0 }$ is the mass at rest (that is $v = 0$ in a local frame), one has

$$
m = m _ { 0 } \gamma = m _ { 0 } \left( 1 - \frac { v ^ { 2 } } { c ^ { 2 } } \right) ^ { - 1 / 2 } .
$$

This result implies that the mass increases toward infinity when the velocity approaches $c$ , a direct consequence of the limitation of velocities by the speed of light. It expresses the impossibility to accelerate a particle to this limiting velocity.

Let us note, at this point, that the acceleration A of a particle in general has to be computed taking into account that $\gamma$ depends upon the velocity $v$ . The derivative of (5.14) is hence,

$$
\mathbf { A } = { \frac { \mathrm { d } \mathbf { V } } { \mathrm { d } \tau } } = \gamma { \frac { \mathrm { d } \mathbf { V } } { \mathrm { d } t } } = \gamma { \frac { \mathrm { d } } { \mathrm { d } t } } \left( \gamma \mathbf { v } \right) = \gamma \left( { \frac { \mathrm { d } \gamma } { \mathrm { d } t } } \mathbf { v } + \gamma { \frac { \mathrm { d } \mathbf { v } } { \mathrm { d } t } } \right)
$$

and, if a is the acceleration with respect to the coordinate time, that is $\mathbf { a } = \mathrm { d } \mathbf { V } / \mathrm { d } t$ , one gets

$$
\mathbf { A } = \gamma { \frac { \mathrm { d } \gamma } { \mathrm { d } t } } \mathbf { v } + \gamma ^ { 2 } \mathbf { a } .
$$

# 5.3 General relativity

General relativity is an extension of the theory of special relativity in the sense that it keeps its results locally, but supplements them with a theory of gravity to which it gives a geometrical form. Let us remember that classical Newtonian celestial mechanics implicitly postulates that the gravitational attraction is a force that propagates at an infinite speed, a concept that contradicts the basic assumption of special relativity, in which no information can be transferred with a velocity higher than the speed of light. General relativity postulates that the presence of masses curves the Euclidian four-dimensional space-time of special relativity, and that the motions are guided by the deformed shape of the space-time, which is described by a metric analogous to, but more complex than, the special relativity metric. Finally, this geometrization of the gravitational field is a formulation of a more general basic principle of general relativity, the equivalence principle.

# 5.3.1 The equivalence principles

In classical mechanics, there are two distinct properties of matter that are involved in mechanics: the gravitational mass, $m$ , which links the gravitational force, F, to the acceleration, a, by $\mathbf { F } = m \mathbf { a }$ , and the inertial mass, $m ^ { \prime }$ , which is a factor that links any inertial type of force, like the centrifugal force, to the acceleration, by $\mathbf { F } = m ^ { \prime } \mathbf { a } .$ . It has been recognized since Galileo that to the accuracy of observations, one has $m ^ { \prime } = m$ , and classical mechanics uses this weak equivalence principle. In the generalization of this weak equivalence principle, Einstein postulated the generalized relativity principle as already described in Section 5.1, and, in particular, that a freely falling laboratory, even near a strongly gravitating mass, is strictly equivalent to a laboratory in free motion on an artificial satellite, or a space-probe outside the Solar System. This is just a particular situation; the equivalence principle states more generally that there is no experiment that would allow one to distinguish whether a room is in a uniformly accelerating elevator, or if it is a fixed room in a gravitational field having a uniform strength over the dimensions of the room.

The consequence is that there is no preferred standard of rest. All are equivalent, and in each of them all non-gravitational laws of nature take the same form as in special relativity. This means that locally, in this standard of rest, there exists a metric that has the form and the properties of the special relativity metric (5.12) describing a flat four-dimensional space-time. The extension to full space-time is not possible by straight translation, because of the presence of gravitating masses. General relativity states that there exists an extended metric, which depends on the distribution and motion of masses in the Universe; and that at each point, there exists a flat special relativity space-time, tangent to the general relativity space-time in the sense that the four coordinates and their derivatives on the two space-times can be set to correspond. In this general relativity space-time, a test particle moves on a geodesic of this generalized metric. In particular, light bends in a gravitational field, because the geodesic is no longer a straight line. It also implies that light traveling down a gravitational field suffers a blueshift, which corresponds to a gravitational time dilatation and adds to the time dilatation due to velocity as described in Section 5.2.5.

The dependence of the metric of general relativity on the distribution and motion of masses is realized essentially through the gravitational potential $U$ and, with a much smaller intensity, through the Lense–Thirring acceleration, W, due to the gravito-magnetic field of a rotating body. Then,

$$
\mathrm { d } s ^ { 2 } = f ( x , y , z , t , U , { \mathbf W } ) .
$$

This will be presented in the following section.

# 5.3.2 The potentials in general relativity

In Newtonian mechanics, the masses produce at a point, $P$ , of coordinates $x$ , $y , z$ , a potential $U ( x , y , z )$ , such that the components of forces along the $P x , P y$ and $P z$ axes are respectively

$$
\frac { \partial U } { \partial x } , \frac { \partial U } { \partial y } , \frac { \partial U } { \partial z } ,
$$

or, in other terms, that the force f at a point $P$ is related to $U$ by

$$
\mathbf { f } = \nabla U .
$$

We have adopted here the sign convention that is in common use in celestial mechanics.

Let $Q _ { i } ( m _ { i } )$ be the $N$ masses acting on the point $P ( X , Y , Z )$ . The expression of the Newtonian potential at $P$ is

$$
U \left( P \right) = G \sum _ { i = 1 } ^ { N } \frac { m _ { i } } { \vert P Q _ { i } \vert } ,
$$

where $G$ is the universal constant of gravitation. For a finite gravitating body, one has to integrate with respect to infinitesimal volumes with density $\rho$ over the volume $V$ of the body

$$
U ( P ) = G \int \int \int _ { ( V ) } \frac { \rho ( x , y , z ) } { \sqrt { ( X - x ) ^ { 2 } + ( Y - y ) ^ { 2 } + ( Z - z ) ^ { 2 } } } \mathrm { d } x \mathrm { d } y \mathrm { d } z .
$$

If $P$ is outside a sphere including the volume $V$ , this expression can be expanded in spherical harmonics. If the origin of axes is taken at the center of mass $o$ of the body, and $r , \phi$ (latitude), and $\lambda$ (longitude) are the spherical coordinates of $P$ , one has

$$
U = \frac { G M } { r } \left[ 1 + \sum _ { n = 2 } ^ { \infty } \frac { J _ { n } a _ { \mathrm { e } } ^ { n } } { r ^ { n } } P _ { n } \left( \sin \phi \right) + \sum _ { n = 2 } ^ { \infty } \sum _ { k = 1 } ^ { \infty } \frac { J _ { n k } a _ { \mathrm { e } } ^ { n } } { r ^ { n } } P _ { n k } \left( \sin \phi \right) \cos k \left( \lambda - \lambda _ { n k } \right) \right] ,
$$

where $M$ is the mass of the body, and $a _ { \mathrm { e } }$ is a scaling factor. In the case of the Earth, $a _ { \mathrm { e } }$ is the equatorial radius of the Earth, $M$ is the mass of the Earth, $r , \phi , \lambda$ are the spherical equatorial coordinates of $P$ $, J _ { n } , J _ { n k }$ are dimensionless coefficients, respectively called zonal and tesseral harmonics, $\lambda _ { n k }$ are the phases of the tesseral harmonics, $P _ { n }$ are Legendre polynomials of degree $n$ , and $P _ { n k }$ are associated Legendre polynomials of degree $n$ and order $k$ .

In the case of general relativity, an additional term of second order in $c ^ { - 2 }$ must be added (Soffel, 2000):

$$
\Delta U = \frac { 1 } { 2 c ^ { 2 } } G \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } \int \int \int _ { ( V ) } \rho ( x , y , z ) \sqrt { ( X - x ) ^ { 2 } + ( Y - y ) ^ { 2 } + ( Z - z ) ^ { 2 } } \mathrm { d } x \mathrm { d } y \mathrm { d } z ,
$$

where $\rho ( x , y , z )$ is the gravitational mass density. Actually, this expression can also be developed in spherical harmonics, so that both terms can be added and an expansion identical to (5.19) can be used in a coordinate system with its origin at $o$ . The coefficients have slightly different values, but the form remains the same.

In addition, if the body is rotating around an axis crossing the origin $o$ , in analogy to the situation in electro-magnetism (see Section 3.5.2), matter currents produce gravito-magnetic fields that lead to a magnetic type gravitational vector potential (see Soffel, 1989, or Brumberg, 1991a), whose value, outside the body is given by

$$
\mathbf { W } = G \int \int \int \int _ { ( V ) } \frac { \rho ^ { \prime } ( x , y , z ) \mathbf { V } ( x , y , z ) } { ( X - x ) ^ { 2 } + ( Y - y ) ^ { 2 } + ( Z - z ) ^ { 2 } } \mathrm { d } x \mathrm { d } y \mathrm { d } z ,
$$

where $\rho ^ { \prime } ( x , y , z )$ is the mass-flux density and $\mathbf { V } ( x , y , z )$ is the velocity of a point of the body. In what follows, we shall call $w _ { i }$ with $i = 1 , 2 , 3$ the projections of $\mathbf { W }$ on the three axes.

Let us now turn to the potential at the surface of the Earth. Contrary to the situation outside the Earth, in which we can use a non-rotating system of coordinates, on the Earth, one must take into account the additional acceleration due to the rotation of the Earth. One uses a local reference that is linked to the site, and hence is rotating with respect to the outside world.

Following the principle of equivalence, the gravitational acceleration and the rotational inertial acceleration combine into a single one, which depends on a potential that is the sum of the gravitational potential of the Earth, $U _ { \mathrm { G } }$ , and the rotational potential, $U _ { \mathrm { R } }$ . The latter is equal to

$$
U _ { \mathrm { R } } = \frac { 1 } { 2 } \omega ^ { 2 } ( x ^ { 2 } + y ^ { 2 } ) ,
$$

where $\omega$ is the angular velocity of the Earth, and $x$ and $y$ are the coordinates of the point $P$ in a plane perpendicular to the axis of rotation. The equipotential surfaces are defined by $U _ { \mathrm { { G } } } + U _ { \mathrm { { R } } } = K .$ . The gravity vector at some point $P$ is perpendicular to the surface passing by $P$ . For a certain value of $K$ , the equipotential surface matches the mean sea level. It is called the geoid. It plays an important role in the realization of the Earth time scales, as well as in geodesy (see Section 9.5.2).

# 5.3.3 The metric in general relativity

The most general form of a four-dimensional metric is

$$
\mathrm { d } s ^ { 2 } = \sum _ { i = 0 } ^ { 3 } \sum _ { j = 0 } ^ { 3 } g _ { i j } \mathrm { d } x _ { i } \mathrm { d } x _ { j } ,
$$

with $g _ { i j } = g _ { j i }$ (the index 0 corresponds to the time-like coordinate). In the development of the theory, this is often represented by a four-dimensional symmetric tensor $\mathcal { T } = \| g _ { i j } \|$ . In the case of general relativity, if the potential vanishes, the $\mathrm { d } s ^ { 2 }$ reduces, in any space-time point, to a tangental special relativity metric,

$$
\mathrm { d } s ^ { 2 } = - c ^ { 2 } \mathrm { d } x _ { 0 } ^ { 2 } + \mathrm { d } x _ { 1 } ^ { 2 } + \mathrm { d } x _ { 2 } ^ { 2 } + \mathrm { d } x _ { 3 } ^ { 2 } .
$$

This form with one negative sign is a characterization of pseudo-Euclidean geometry. The geometry of general relativity is therefore pseudo-Euclidean, but, in this presentation, we shall not need to use specific results of this geometry. Furthermore, the vanishing terms have to be small and the small parameter happens to be proportional to $1 / c ^ { 2 }$ . The coefficients, $g _ { i j }$ , can be expanded as a function of small parameters. As recommended by the International Astronomical Union (IAU) in 2000, the only terms that are, or could be, significant in astrometry at the microarcsecond accuracy, or in time transfer at a $1 0 ^ { - 1 7 } \mathrm { s }$ precision, in a weak field like the case of the Solar System, are the following:

$$
\begin{array} { l } { { g _ { 0 0 } = - 1 + \displaystyle \frac { 2 U } { c ^ { 2 } } - \displaystyle \frac { 2 U ^ { 2 } } { c ^ { 4 } } , } } \\ { { \displaystyle g _ { i i } = 1 + \displaystyle \frac { 2 } { c ^ { 2 } } U , } } \\ { { \displaystyle g _ { 0 i } = - \displaystyle \frac { 4 } { c ^ { 3 } } w _ { i } . } } \end{array}
$$

All other terms, in particular the cross space terms $g _ { i j }$ , are null. In tensor notation, this gives:

$$
\left( { \begin{array} { c c c c } { - 1 + \frac { 2 U } { c ^ { 2 } } - \frac { 2 U ^ { 2 } } { c ^ { 4 } } } & { - \frac { 4 } { c ^ { 3 } } w _ { 1 } } & { - \frac { 4 } { c ^ { 3 } } w _ { 2 } } & { - \frac { 4 } { c ^ { 3 } } w _ { 3 } } \\ { - \frac { 4 } { c ^ { 3 } } w _ { 1 } } & { 1 + \frac { 2 } { c ^ { 2 } } U } & { 0 } & { 0 } \\ { - \frac { 4 } { c ^ { 3 } } w _ { 2 } } & { 0 } & { 1 + \frac { 2 } { c ^ { 2 } } U } & { 0 } \\ { - \frac { 4 } { c ^ { 3 } } w _ { 3 } } & { 0 } & { 0 } & { 1 + \frac { 2 } { c ^ { 2 } } U } \end{array} } \right) .
$$

It is usually assumed that $U$ vanishes at infinity. As in special relativity, one distinguishes the proper time, $\tau$ , and the coordinate time, $t$ . The metric can be written as, in the usual notation:

$$
\begin{array} { l } { { \displaystyle \mathrm { d } s ^ { 2 } = - c ^ { 2 } \mathrm { d } \tau ^ { 2 } = \left( - 1 + \frac { 2 U } { c ^ { 2 } } - \frac { 2 U ^ { 2 } } { c ^ { 4 } } \right) c ^ { 2 } \mathrm { d } t ^ { 2 } } } \\ { { \displaystyle ~ + \left( 1 + \frac { 2 U } { c ^ { 2 } } \right) ( \mathrm { d } x ^ { 2 } + \mathrm { d } y ^ { 2 } + \mathrm { d } z ^ { 2 } ) } } \\ { { \displaystyle ~ - \frac { 4 } { c ^ { 3 } } ( w _ { 1 } \mathrm { d } x + w _ { 2 } \mathrm { d } y + w _ { 3 } \mathrm { d } z ) \mathrm { d } t . } } \end{array}
$$

The relation between $\tau$ and $t$ is an extension of the relation (5.13). Neglecting terms of order 3 and more in $1 / c$ , one gets

$$
{ \frac { \mathrm { d } \tau } { \mathrm { d } t } } = { \sqrt { 1 - { \frac { 2 U } { c ^ { 2 } } } - { \frac { v ^ { 2 } } { c ^ { 2 } } } } } .
$$

The presence of the potential describes quantitatively the gravitational time dilatation mentioned in Section 5.3.1.

The motion of a point mass – or of a photon – is fully described by the metric which depends on time, since masses are moving and consequently the potentials vary with time. It is a geodesic of the space-time manifold. If $( x _ { 0 } , x _ { 1 } , x _ { 2 } , x _ { 3 } )$ are the coordinates of a free-falling particle, its motion – that is the variation of its coordinates with time – can be expressed in terms of some parameter $p$ by solving the four geodesic differential equations

$$
\frac { \mathrm { d } } { \mathrm { d } p } \left( \sum _ { i = 0 } ^ { 3 } g _ { k i } \frac { \mathrm { d } x _ { i } } { \mathrm { d } p } \right) - \frac { 1 } { 2 } \sum _ { i = 0 } ^ { 3 } \sum _ { j = 0 } ^ { 3 } \frac { \partial g _ { i j } } { \partial x _ { k } } \frac { \mathrm { d } x _ { i } } { \mathrm { d } p } \frac { \mathrm { d } x _ { j } } { \mathrm { d } p } = 0 ,
$$

where the coefficients $g _ { i j }$ are given as functions of $U ( x _ { 0 } , x _ { 1 } , x _ { 2 } , x _ { 3 } )$ by the expressions (5.22).

Remark. In almost all the practical cases of astrometry, in particular in the Solar System, it is sufficient to keep only the terms in $1 / c ^ { 2 }$ in (5.22), or use any other simplified expression like the Schwarzschild space-time (see Section 5.3.5). Even in a number of instances, as will be indicated in the following chapters, the Newtonian or the special relativity models may be quite sufficient to describe the observations, but this is no longer true when observed objects are out of the Solar System (e.g. VLBI observations, see Kopeikin and Sch¨affer, 1999). A more sophisticated approach to relativistic astrometry is necessary in many other cases listed by Kopeikin and Gwinn (2000). Finally, when the objects are surrounded by a very strong gravitational field, one cannot limit the relativistic equations to the truncated expressions given above. This is, for instance, the case of gravitational waves, pulsar, quasar, or black hole theories. We shall not consider these cases, except millisecond pulsar timing observations, which are presented in a simplified form in Section 14.7.

# 5.3.4 Transformation between reference frames

In practice, two different space-time coordinate systems are currently used:

(i) a Geocentric Celestial Reference System (GCRS), whose origin is at the center of mass of the Earth, realized by a terrestrial reference frame, bounded somewhat outside the orbit of the Moon, and   
(ii) a Barycentric Celestial Reference System (BCRS), whose origin is the barycenter of the Solar System, realized by a barycentric reference frame and extending to the whole Solar System.

In many problems, it is necessary to use successively, or simultaneously, these two (and possibly others like topocentric or satellite) reference frames. The transformation from one to another is not trivial as in the case of Newtonian mechanics. In the most general case, the metric of one of the space-time systems $( x _ { 0 } , x _ { 1 } , x _ { 2 } , x _ { 3 } )$ is:

$$
\mathrm { d } s ^ { 2 } = \sum _ { \alpha = 0 } ^ { 3 } \sum _ { \beta = 0 } ^ { 3 } g _ { \alpha \beta } \mathrm { d } x _ { \alpha } \mathrm { d } x _ { \beta } \quad ( \mathrm { w i t h \ } g _ { \alpha \beta } = g _ { \beta \alpha } )
$$

and the metric of the second $( x _ { 0 } ^ { \prime } , x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } , x _ { 3 } ^ { \prime } )$ is

$$
\mathrm { d } s ^ { \prime 2 } = \sum _ { i = 0 } ^ { 3 } \sum _ { j = 0 } ^ { 3 } g _ { i j } ^ { \prime } \mathrm { d } x _ { i } ^ { \prime } \mathrm { d } x _ { j } ^ { \prime } \quad ( \mathrm { w i t h \ } g _ { i j } ^ { \prime } = g _ { j i } ^ { \prime } ) ,
$$

where the quantities $g$ and $g ^ { \prime }$ are respectively functions of the corresponding coordinates. They are related by the fundamental tensor relation describing the change of reference

$$
g _ { \alpha \beta } \left( x _ { 0 } , x _ { 1 } , x _ { 2 } , x _ { 3 } \right) = \sum _ { i = 0 } ^ { 3 } \sum _ { j = 0 } ^ { 3 } g _ { i j } ^ { \prime } ( x _ { 0 } ^ { \prime } , x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } , x _ { 3 } ^ { \prime } ) \frac { \partial x _ { i } ^ { \prime } } { \partial x _ { \alpha } } \frac { \partial x _ { j } ^ { \prime } } { \partial x _ { \beta } } .
$$

Solving these ten differential equations permits one to express the new coordinates with respect to the old ones, or vice versa. The full general solution is very complex and can be found in Brumberg and Kopeikin (1990). Even if we apply this transformation for reduced metrics (5.22), the calculation is lengthy and will not be presented here. The results for the transformation between GCRS and BCRS are given in Recommendation B1-3 of the General Assembly of the IAU in 2000 (Andersen, 2001) for the metric defined in (5.24). This is the geodesic precession and nutation (Section 7.5).

# 5.3.5 The Schwarzschild approximation

An often-used simplified form of the metric (5.22), reduced to its second term, is the Schwarzschild space-time, which is spherically symmetric around a single particle of mass $M$ , so that the potential reduces to $U = G M / r$ . It is convenient to use the transformation defining polar coordinates (radius vector $r$ , latitude $\phi$ , and longitude $\lambda$ ), and the transformed metric is

$$
\mathrm { d } s ^ { 2 } = - c ^ { 2 } \mathrm { d } \tau ^ { 2 } = \left( { \frac { \mathrm { d } r ^ { 2 } } { 1 - { \frac { 2 G M } { r c ^ { 2 } } } } } + r ^ { 2 } \mathrm { d } \phi ^ { 2 } + r ^ { 2 } \cos ^ { 2 } \phi \mathrm { d } \lambda ^ { 2 } \right) - \left( 1 - { \frac { 2 G M } { r c ^ { 2 } } } \right) c ^ { 2 } \mathrm { d } t ^ { 2 } .
$$

It can be extended to the fourth order in $1 / c$ , assuming that the bodies are not rotating, that is setting $\mathbf { W } = 0$ . It is sufficient to replace in (5.28) the term in $c ^ { 2 } \mathrm { d } t ^ { 2 }$ by

$$
\left( 1 - \frac { 2 G M } { r c ^ { 2 } } + \frac { 2 G ^ { 2 } M ^ { 2 } } { r ^ { 2 } c ^ { 4 } } \right) c ^ { 2 } \mathrm { d } t ^ { 2 } .
$$

These expressions can conveniently be used whenever one may neglect all the masses except the central non-rotating mass.

# 5.3.6 The parametrized post-Newtonian formulation

Another simplified and useful tool for the evaluation of astrometric consequences of general relativity is the parametrized, post-Newtonian (PPN) formalism introduced in its earlier form by Eddington (1922), but essentially developed by Nordtvedt (1970) and used by Will (1981). It has been widely used in describing various relativistic effects, and in comparing them with observations. It is actually a generalization of the expressions (5.28) and (5.29) with the same assumptions.

The idea is to consider the most general form (5.21) of the metric, accepting that the main terms are those given to the second order in $1 / c$ . This takes into account a large set of possible metrics of alternative theories of gravity that include, for special values of the parameters, the Einsteinian Theory of General Relativity. Will has introduced ten parameters related to the ten terms of the general metric (5.21), with particular physical meanings that can, in principle, be determined from observations. However, in practice, most of them are not, at present, accessible to observation, so we shall keep only the two that are generally used: $\gamma$ , which describes the space curvature, and $\beta$ , which gives the amount of nonlinearity of the gravitational field. The corresponding metric is given by

$$
\begin{array} { l } { { g _ { 0 0 } = - 1 + \displaystyle \frac { 2 U } { c ^ { 2 } } - \beta \displaystyle \frac { U ^ { 2 } } { c ^ { 4 } } } } \\ { { g _ { i i } = 1 + 2 \gamma \displaystyle \frac { U } { c ^ { 2 } } } } \\ { { g _ { 0 i } = - \displaystyle \frac { 2 ( 1 + \gamma ) } { c ^ { 3 } } w _ { i } . } } \end{array}
$$

Comparing this with (5.22), one sees that in general relativity, $\beta = \gamma = 1 .$ . Most of the tests of general relativity use this representation and, up to now, the two parameters were found to be equal to 1 with uncertainties of the order of $1 0 ^ { - 3 }$ to $1 0 ^ { - 4 }$ .

# 5.3.7 Harmonic coordinates

In the most general approach in general relativity, the motion and the distribution of masses are mutually dependent. This is expressed by field equations which permit the determination of the ten elements, $g _ { i j }$ , of the metric (5.21), usually expressed as a four-dimensional tensor. There are ten covariant field equations, but they admit four arbitrary functions and hence satisfy four identities, which can be used to simplify the equations by a convenient choice of coordinate systems. In practice, the specific choice that is used to simplify the field equations, and consequently the solution, corresponds to what are called harmonics coordinates (Fock, 1976, and Brumberg, 1991a). In 2000, the IAU recommended that they should systematically be used, at least when terms of order larger than $1 / c ^ { 2 }$ are to be kept.

Let $g$ be the determinant of the $\| g _ { i j } \|$ tensor. The four $j = 0$ to 4) conditions that set the four identities and define the harmonic coordinates are (Brumberg, 1991a)

$$
\frac { \partial \left( \sum _ { i = 0 } ^ { 3 } g _ { i j } \sqrt { - g } \right) } { \partial x _ { j } } = 0 .
$$

In the case of the tensor of the general metric (5.23), and neglecting the terms of higher order than $1 / c ^ { 4 }$ , the effect of $\mathbf { W }$ disappears, and one is left with

$$
g = - 1 - 4 \frac { U } { c ^ { 2 } } - \frac { 2 U ^ { 2 } } { c ^ { 4 } } ,
$$

and

$$
\sqrt { - g } = 1 + \frac { 2 U } { c ^ { 2 } } - \frac { U ^ { 2 } } { c ^ { 4 } } .
$$

Applying the definition (5.31), one finally gets the harmonic conditions up to order $1 / c ^ { 4 }$ :

- for the time-like argument

$$
\frac { \partial } { \partial x _ { 0 } } \left( - 1 + \frac { 3 U ^ { 2 } } { c ^ { 4 } } - \frac { 4 } { c ^ { 3 } } ( w _ { 1 } + w _ { 2 } + w _ { 3 } ) \right) = 0 ,
$$

- and for the three space-like arguments

$$
\frac { \partial } { \partial x _ { j } } \left( 1 + \frac { 4 U } { c ^ { 2 } } + \frac { 3 U ^ { 2 } } { c ^ { 4 } } - 4 \frac { w _ { j } } { c ^ { 3 } } \right) = 0 .
$$

However, in this book, which is not devoted to relativistic celestial mechanics, we shall not use the harmonic conditions. To get more acquainted with their use, refer to Fock (1976) and Brumberg (1991a).

# 5.4 Space-time coordinate systems

Locally, a space-time coordinate system is defined by the flat, special relativity space-time tangent to the general relativity space, as is postulated by the equivalence principle (Section 5.3.1). In a small environment, like a laboratory or an astronomical instrument, one can use it in conjunction with the laws of physics of special relativity. To what extent this is adequate depends on the accuracy with which one needs to represent the physical phenomena. This is discussed in detail by Guinot (1997). For instance, if one wishes to synchronize two clocks to $1 0 ^ { - 1 7 } \mathrm { s }$ , they should remain at a distance less than $1 \textrm { m }$ . The problem is how to extend a local reference system to the astronomical universe.

# 5.4.1 Practical reference frames

Our knowledge of positions in space is dependent on the light received from the celestial objects. What is measured, in the local tangent, flat frame, is the direction from which the light reaches the instrument. Between the source and the observer, the light travels in a space where the gravitational potentials do not vanish. It follows a geodesic as does any test particle, but at speed c. So, one is led to determine the geodesic line by solving Equations (5.26) using the reduced form of the metric (5.22) or, if necessary, the full metric (5.24).

Let us, however, remark that, in reality, the Universe is not empty and has a certain mass distribution and a certain density. In constructing a cosmic reference frame, or discussing any cosmological observation, one should take into account the mean density of the Universe (Kopeikin, 2001). In modeling pulsar observations, the gravity field surrounding the object is a major parameter to be taken into account.

But in constructing an astrometric reference frame for observations from the Solar System, it is not necessary to know the shape of the light path, provided that it does not change in an observable manner during the few decades of validity of a reference frame. So, in practice, except within the Solar System itself, one ignores the effects of the outside gravitational fields. It is conventionally assumed that the reference system is such that directions correspond to the directions from which the light arrives, when it reaches the outskirts of the Solar System. In other terms, they correspond to what they would be, if all the masses outside the Solar System vanished.

The background of this procedure is that we model the environment by an asymptotically flat, or Minkowskian, space-time. The details can be found in Soffel (1989). The procedure is based on the notion of Weyl parallelism in such a space. Provided that the axes are defined far away from the Sun, the space-time is practically flat, and can, therefore, be used as if it was Euclidean. So, what is left is to determine the path of a light beam through the Solar System. At this level, we shall ignore the various effects that bend the light in the vicinity of the observer (refraction), or produce an apparent deviation (aberration). At this point, we shall assume that the local frame is free falling, which means that we are neglecting the effects of Earth rotation and gravity. All these additional effects have to be taken into account and will be described in Chapter 6.

# 5.4.2 Light paths

Light crosses the Solar System on a geodesic line defined by the distribution of potentials due to the Sun and the planets. One should, therefore, know the positions of the bodies of the Solar System and their motions during the travel of the light beam.

As a first approximation, sufficient in practice, let us limit ourselves by considering independently the principal effect due to the solar potential, and then add to it the effects due to individual planets which are smaller by at least a factor of $1 0 ^ { - 3 }$ , the maximum in terms of solar mass (Jupiter). In the latter case, it is sufficient to assume that they are fixed at the position they have at the moment of closest approach of the light beam. We shall describe the path of a light beam in the potential of a point-like mass $P$ , which is, again, a sufficiently good approximation of the potential of the Sun and the planets.

Let us use the extended Schwarzschild metric, (5.28) and (5.29), but simplifying the notation by setting $m = G M / c ^ { 2 }$ . The four non-zero metric coefficients are:

$$
\begin{array} { l } { \displaystyle g _ { 0 0 } = - 1 + \frac { 2 m } { r } - \frac { 2 m ^ { 2 } } { r ^ { 2 } } } \\ { \displaystyle g _ { 1 1 } = \frac { 1 } { c ^ { 2 } ( 1 - 2 m / r ) } , } \\ { \displaystyle g _ { 2 2 } = \frac { r ^ { 2 } } { c ^ { 2 } } , } \\ { \displaystyle g _ { 3 3 } = \frac { r ^ { 2 } \cos ^ { 2 } \phi } { c ^ { 2 } } . } \end{array}
$$

The path of the light is described by the coordinate time $t$ , the three spherical coordinates, $r , \phi$ and $\lambda$ , and the solution of Equations (5.26).

Since all the $g _ { i j }$ with $i$ not equal to $j$ are zero, Equations (5.26) reduce to

$$
\frac { \mathrm { d } } { \mathrm { d } p } \left( g _ { k k } \frac { \mathrm { d } x _ { k } } { \mathrm { ~ d } p } \right) - \frac { 1 } { 2 } \sum _ { i = 0 } ^ { 3 } \frac { \partial g _ { i i } } { \partial x _ { k } } \left( \frac { \partial x _ { i } } { \partial p } \right) ^ { 2 } = 0 ,
$$

with $k = 0$ to 3.

Now, the potential has a spherical symmetry, so that the plane comprising $P$ and the initial velocity vector of the light is a plane of symmetry of the problem, so that the path is in this plane. Let us chose it as the equatorial plane of the system of coordinates, and we have

$$
\phi \equiv 0
$$

and, of course,

$$
\frac { \mathrm { d } x _ { 2 } } { \mathrm { d } t } = \frac { \mathrm { d } \phi } { \mathrm { d } t } = 0 .
$$

If we turn now to other equations, we note that $\lambda = x _ { 3 }$ is absent from all four coefficients. Hence, the second term of (5.32) disappears, and one has, with cos $\phi = 1$ ,

$$
{ \frac { \mathrm { d } } { \mathrm { d } p } } \left( { \frac { r ^ { 2 } } { c ^ { 2 } } } { \frac { \mathrm { d } { \lambda } } { \mathrm { d } p } } \right) = 0 ,
$$

or

$$
r ^ { 2 } { \frac { \mathrm { d } \lambda } { \mathrm { d } p } } = h .
$$

Similarly, the time $x _ { 0 } = t$ does not appear in (5.32) and the equation for $x _ { 0 }$ becomes

$$
\frac { \mathrm { d } } { \mathrm { d } p } \left( \left( - 1 + \frac { 2 m } { r } - \frac { 2 m ^ { 2 } } { r ^ { 2 } } \right) \frac { \mathrm { d } t } { \mathrm { d } p } \right) = 0 ,
$$

or

$$
\left( 1 - { \frac { 2 m } { r } } + { \frac { 2 m ^ { 2 } } { r ^ { 2 } } } \right) { \frac { \mathrm { d } t } { \mathrm { d } p } } = k .
$$

Let us remark, that at this level, we have not yet assumed anything about $\mathrm { d } s ^ { 2 }$ . This means that all this is valid for the one body problem in general relativity. The results obtained mean that:

(1) the motion is plane,   
(2) the constant $h$ is the generalization of the law of conservation of the angular momentum,   
(3) the constant $k$ is the generalization of the law of conservation of energy.

At this point, let us return to the $\mathrm { d } s ^ { 2 }$ which is a constant on a geodesic and, in the case of the light, $\mathrm { d } s ^ { 2 } = 0$ . Substituting the equation $\theta = 0$ into the metric (5.29), one gets

$$
c ^ { 2 } \left( { \frac { \mathrm { d } s } { \mathrm { d } p } } \right) ^ { 2 } = 0 = { \frac { 1 } { 1 - { \frac { 2 m } { r } } } } \left( { \frac { \mathrm { d } r } { \mathrm { d } p } } \right) ^ { 2 } + r ^ { 2 } \left( { \frac { \mathrm { d } \lambda } { \mathrm { d } p } } \right) ^ { 2 } - \left( 1 - { \frac { 2 m } { r } } + { \frac { 2 m ^ { 2 } } { r ^ { 2 } } } \right) c ^ { 2 } \left( { \frac { \mathrm { d } t } { \mathrm { d } p } } \right) ^ { 2 } ,
$$

or, introducing the integrals (5.33) and (5.34), and leaving only the first- and the second-order terms in $m$ ,

$$
\left( { \frac { \mathrm { d } r } { \mathrm { d } p } } \right) ^ { 2 } = \left( 1 - { \frac { 2 m ^ { 2 } } { r ^ { 2 } } } \right) c ^ { 2 } k ^ { 2 } - \left( 1 - { \frac { 2 m } { r } } \right) { \frac { h ^ { 2 } } { r ^ { 2 } } } \quad { \mathrm { a n d } } \quad { \frac { \mathrm { d } \lambda } { \mathrm { d } p } } = { \frac { h } { r ^ { 2 } } } .
$$

These equations give the parametrized path of the light in its plane of propagation. They can be integrated from any departure position and the path followed is a function of the parameter $p$ , which, in a first approximation, neglecting $m$ and setting $k = 1$ , is the coordinate time. In any case, at least in the Solar System, where $m$ is very small, it is a valid approximation.

In summary, these equations allow the computation of the path of light throughout the Solar System, assuming that the bodies are symmetric, non-rotating, and nonmoving with respect to the observer, and that the planetary effects are additive.

The application of these equations to the apparent shift of the direction from which the light reaches the observer is given in Chapter 6. They are to be applied in order to determine the coordinate axes and the directions of extra-solar objects.

# 5.5 Time scales

Coordinate time is one of the coordinates of general relativity, so there is a specific time scale with each coordinate frame.

# 5.5.1 Terrestrial time scales

Since we are on the Earth, terrestrial reference frames and time scales have a particular importance, and the compatibility with general relativity concepts is imperative. Having defined a Geocentric Celestial Reference Frame (GCRS) on the basis of the preceding section, let us find the corresponding time coordinate scale.

The origin of the GCRS is the center of mass of the Earth, $E$ , at which point the potential $U$ is set to zero. The corresponding time scale is called Geocentric Coordinate Time (TCG, Temps-coordonn´ee g´eocentrique). The problem is to build a practical time scale on the surface of the Earth that coincides with TCG.

If we come back to Equation (5.25), we can determine the coordinate time, $t$ , at any place in which the potential is $U$ , and the rotational potential is

$$
U _ { \mathrm { R } } = { \frac { 1 } { 2 } } \omega ^ { 2 } ( x ^ { 2 } + y ^ { 2 } ) = v ^ { 2 } / 2 .
$$

It results that, neglecting the terms in $c ^ { - 4 }$

$$
\frac { \mathrm { d } t } { \mathrm { d } \tau } = 1 - \frac { U _ { \mathrm { G } } } { c ^ { 2 } } ,
$$

where $U _ { \mathrm { G } }$ is the potential at the geoid (see Section 9.5.2),

$$
\begin{array} { r } { U _ { \mathrm { G } } = U + U _ { \mathrm { R } } . } \end{array}
$$

This coordinate time is called Terrestrial Time (TT) and differs from TCG uniquely by a constant rate. The unit of time of TT is the second of the International System of Units (SI) as realized on the geoid and defined as follows:

The second is the duration of 9 192 631 770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the caesium 133 atom.

This definition refers to the atom in its ground state, undisturbed, and at a temperature of $0 \mathrm { K }$ .

Atomic cesium clocks realize the SI second as a proper time which, at the geoid, is equal to the coordinate time TT. The ratio defined by the equation (5.36) provides the relationship between TT and TCG:

$$
\mathrm { T C G } - \mathrm { T T } = L _ { \mathrm { G } } \times ( J D - 2 4 4 3 1 4 4 . 5 ) \times 8 6 4 0 0 \mathrm { s } ,
$$

with $L _ { \mathrm { G } } = U _ { \mathrm { G } } / c ^ { 2 } = 6 . 9 6 9 2 9 0 1 3 4 \times 1 0 ^ { - 1 0 }$ , and $J D$ is the Julian day. The bracket vanishes on January 1, 1977, 0h.TT. The uncertainty of this expression is $1 0 ^ { - 1 7 }$ . It was decided at the General Assembly of the IAU in 2000, that this value of $L _ { \mathrm { G } }$ will become a defining constant of TT. This overcomes the difficulties due to the temporal changes of the geoid and the intricacy of its definition.

The practical construction of TT is obtained by comparing the readings of many atomic clocks. Because they are at different altitudes, the local potentials are different, and the rates of their coordinate times are different. It is, therefore, necessary to reduce them to the geoid. If $h _ { 1 }$ and $h _ { 2 }$ are the heights of the clocks, and $g$ is the mean gravity at $( h _ { 1 } + h _ { 2 } ) / 2$ , then the difference of rates is obtained by applying Equation (5.25). To a sufficient accuracy, this gives

$$
\Delta \left( { \frac { \mathrm { d } \tau } { \mathrm { d } t } } \right) = { \frac { g ( h _ { 1 } - h _ { 2 } ) } { c ^ { 2 } } } .
$$

The time scale that is derived by the BIPM (Bureau International des Poids et Mesures) is actually the TAI (temps atomique international). One representation of T T is

$$
\mathrm { T T } ( \mathrm { T A I } ) = \mathrm { T A I } + 3 2 . 1 8 4 \mathrm { s } .
$$

# 5.5.2 Barycentric time

In addition to the geocentric reference system, the other important reference system used in astronomy is centered at the barycenter of the Solar System. This point, $\mathbf { X } _ { \mathrm { B } }$ , is defined by the condition that the following integral over a volume $V ( \mathbf { x } )$ including all the masses of the Solar System is null,

$$
\int _ { V } \left[ \rho ( { \bf x } ) + \frac { 1 } { c ^ { 2 } } \left( \frac { 1 } { 2 } \rho ( { \bf x } ) v ( { \bf x } ) ^ { 2 } \right) \right] ( { \bf x } - { \bf x } _ { \mathrm { B } } ) \mathrm { d } V = 0 .
$$

This point is such that its motion in the Galaxy is linear, if one neglects the gravitational potential of the Galaxy. One of the major problems of astrometry is to refer the observations to a Barycentric Celestial Reference Frame. This is treated in the following chapters. Such a reference frame has a coordinate time called TCB (temps-coordonn´ee barycentrique $=$ Barycentric Coordinate Time). The difficulty in computing TCB for any point of the Solar System is that the potentials vary with time because of the motion of planets.

Let us call $t ( \mathrm { T C B } )$ and $\mathbf { X }$ the barycentric coordinates of an event in barycentric reference coordinates. The potential is described by the summation of particular potentials produced by $N$ significant Solar System bodies with masses $M _ { i }$ and positions $\mathbf { X } _ { i }$ that we describe as point-like masses

$$
U _ { 0 } = G \sum _ { i = 1 } ^ { N } M _ { i } / \left| \mathbf { x } - \mathbf { x _ { i } } \right| .
$$

Let us consider an event at the center of mass of the Earth. Then, one can obtain the difference between TCB and TCG. In this case, $U _ { 0 }$ should not contain the Earth potential, and let us denote it as $U _ { 0 } ^ { \mathrm { e x t } }$ . Let $\mathbf { v } _ { \mathrm { e } }$ be the coordinate velocity of the Earth’s center of mass and $\mathbf { X } _ { \mathrm { e } }$ its coordinates; the relation between TCB and TCG can be obtained by computing

$$
\mathrm { T C B - T C G } = \frac { 1 } { c ^ { 2 } } \left[ \int _ { 0 } ^ { t } \left( U _ { 0 } ^ { \mathrm { e x t } } + \frac { 1 } { 2 } v _ { \mathrm { e } } ^ { 2 } \right) \mathrm { d } t + \mathbf { v _ { e } } \cdot ( \mathbf { x } - \mathbf { x _ { e } } ) \right] + \mathrm { O } ( c ^ { - 4 } ) .
$$

Additional terms in $c ^ { - 4 }$ can be found in recommendation B1-4 of the IAU (Andersen, 2001). This expression has a linear term which represents the difference of their mean rates:

$$
( \mathrm { T C B } - \mathrm { T C G } ) _ { \mathrm { s e c u l a r } } = L _ { \mathrm { C } } ( J D - 2 4 4 3 1 4 4 . 5 ) \times 8 6 4 0 0 \mathrm { s } ,
$$

where the best value at present of $L _ { \mathrm { C } }$ is

$$
L _ { \mathrm { C } } = 1 . 4 8 0 8 2 6 8 6 7 4 1 \times 1 0 ^ { - 8 } ,
$$

with an uncertainty of $1 0 ^ { - 1 7 }$ . In addition, the expression (5.38) has a nonlinear variation described by a number of periodic terms depending on the various periods present in the motions of planets. They are discussed in Fukushima (1995), who finds that there are 515 terms that are greater in amplitude than 0.1 ns. The most important terms in TCB–TCG are, in seconds,

$$
0 . 0 0 1 6 5 8 \sin g + 0 . 0 0 0 0 1 4 \sin 2 g ,
$$

where $g = 3 5 7 { ' } . 5 3 + 0 { ' } 9 8 5 0 0 3 ( J D - 2 4 5 1 5 4 5 . 0 )$ essentially represents the mean anomaly of the Earth’s orbit.

# 5.6 Astrometric effects

Whenever the accuracy of observations is such that a relativistic metric produces a non-negligible effect, one may compute the difference between what is obtained, assuming classical Newtonian Euclidean space and absolute time, and the solution by using the relativistic metric. Erroneously this is called a relativistic astrometric effect, because the complete effect results from the Theory of General Relativity. So, it is preferable to describe, as in the following sections, those phenomena observed by astrometric means, making use directly of the Theory of General (or sometimes Special) Relativity.

# 5.6.1 Relativistic reduction of astrometric measurements

In general, astrometric observations are related to some local frame of reference (telescope, artificial satellite, ranging system). But in order to compare measurements performed at different times and/or different locations, it is necessary to refer them to some conventional point, for instance the barycenter of the Solar System, or the center of mass of the Earth. In classical reduction procedures, one proceeds by taking into account the position and the velocity of the observer and the timing in some absolute time-scale. Examples of effects to be taken into account are aberration, parallactic displacements, precession and nutation, polar motion, refraction, corrections to reduce to some definite reference frame, etc. These will be described in the following chapters. But in the case of relativity, these reductions must take into account the potential in the field, and its dependence on time.

In special or general relativity, the transformation from local time and positions into some unique system of space-time coordinates implies working in a given metric, involving not only positions and velocities, but the Lorentz transformation in special relativity, and the effects of potentials in general relativity. A discussion of the problems in the most general context can be found in Brumberg (1991a). We shall apply them in the particular cases in the following chapters.

# 5.6.2 Main relativistic effects

Let us list the cases when it is essential to use a relativistic approach, and give a hint as to the treatment of the most important such phenomena, in particular those that have been – and still are – the classical tests of general relativity. There are three classical, relativistic effects that were originally used to verify the Einstein theory. Others have been added since.

(i) The advance of perihelia of planets. The part of the motion of perihelia that could not be explained by the classical Newtonian celestial mechanics amounts to $4 2 . 7$ per century for Mercury and is fully explained by the theory of general relativity. The rotation is

$$
\frac { 6 \pi m } { a ( 1 - e ^ { 2 } ) }
$$

per revolution for a planet of semi-major axis $a$ , eccentricity $e$ , and $m = G M / c ^ { 2 }$ , where $M$ is the mass of the central body. (ii) The bending of light. The principle is given in Section 5.4.2 and the evaluation of the effect is presented in Section 6.4.5. For a ray grazing the Sun, the effect is 1.75. At $9 0 ^ { \circ }$ from the Sun, the effect is 4.0717 mas (see Section 6.4.3). It is the cause of the gravitational lensing by stars or quasars. (iii) Gravitational time dilatation. This effect is described in Section 5.3.3 by Equation (5.24) and is now very well determined with accurate atomic clocks on board satellites. (iv) Geodesic precession and nutation. This effect represents the rotation of a reference coordinate system in presence of forces. This is the case of the geocentric axes with respect to the barycentric ones, even if they are both defined by the apparent directions of the same fixed extragalactic objects (see Section 7.5). (v) Light time delays. The travel time for light as measured by radar ranging depends on the potential in the path. This will be presented in Section 6.5. This is equivalent to the dependence of length with respect to the potential. (vi) Gravitational red shift. The difference in gravitational potential between the place of emission and the observer has an effect that cannot be distinguished from the Doppler shift due to radial velocity. It has, however, to be taken into account and will be touched upon in Section 11.3.2. (vii) Gravitational wave emissions. In analyzing the motion of a binary pulsar, Taylor and Weisberg (1989) have shown that there was an energy loss, interpreted in the framework of general relativity, as an emission of gravitational waves. However, until now, no direct detection of such waves has been achieved. (viii) Pulsar timing. This problem is touched upon in Section 14.7.

Some other astrometric phenomena are not relativistic effects (aberration, parallax), but are modified by the Theory of General Relativity, and are observationally mixed with them. So, one has to keep them in mind, especially at the level of microarcsecond accuracies. For this reason, in the chapters that follow, and generally speaking in modern astrometry, one has to think in terms of general relativity, and return to more classical approaches, only if it is clear that this is consistent with the accuracy of the observations.

# 6

Apparent displacements of celestial objects

The apparent direction in the sky at which a celestial object appears is not the actual direction from which the light was emitted. What is observed is the tangent direction of the light when it reaches the observer. For reasons that will be discussed in this chapter, the light path is not rectilinear and several corrections describing the effects of bending, or shifts in direction, are to be applied to the direction from which the light is observed to determine the actual direction of the emission. We shall not deal here with the various transformations undergone by the light within the observing instrument; they are particular to each case. Some examples are given in Chapter 14. We shall consider only the direction from which the light came when it entered into the instrument. One has to consider the atmospheric refraction, the shift in direction due to the combination of the speed of light with the motion of the observer, called aberration, and the bending of light in the presence of gravitational fields. The latter has been already presented in Section 5.4.2, but will be revisited in Section 6.4. Similarly, the geodesic precession and nutation are to be considered when relating the positions from a moving reference frame of fixed orientation to a fixed reference frame of the same orientation (see Section 7.5). In addition, one often wants to get the direction of the source as seen from a point other than the observatory, for example the center of the Earth or the barycenter of the Solar System. These are the parallactic corrections. Sometimes, particularly for objects in the Solar System, one wishes to know the position of an object at the time of the observation, or the exact time at which the observed light was emitted. This is called the light-time correction. All these effects are discussed in this chapter.

# 6.1 Atmospheric refraction

When light crosses a surface which separates two gas layers with refractive indices $n$ and $n + \mathrm { d } n$ , it is deviated – refracted – in a manner described by Snell’s law. Let $\xi$ be the angle of incidence (angle of the ray with the normal of the separation surface)

in the medium characterized by the refractive index $n$ . The angle of refraction in the medium of refractive index $n + \mathrm { d } n$ is $\xi + \mathrm { d } \xi$ and obeys the relation

$$
( n + \mathrm { d } n ) \sin ( \xi + \mathrm { d } \xi ) = n \sin \xi .
$$

The total bending of the light is the quantity

$$
R = z - z _ { 0 } ,
$$

where $z _ { 0 }$ is the observed zenith distance of the object, and $z$ is the zenith distance it would have had without the atmosphere and is referred to the vertical direction (zenith) $o a$ of the observer,

$$
z = z _ { 0 } + R .
$$

In theory, the determination of $R$ should imply the knowledge of $n$ at all points of the atmosphere crossed by the ray, and the angle of the local normals to iso-index layers with the vertical $V$ at the origin. It would be obtained by integrating (6.1) from the ground with a measured refractive index $n _ { 0 }$ to space – at a height of the order of $5 0 ~ \mathrm { k m }$ – from which one may consider that the vacuum is sufficient to assume $n = 1$ . The theory was made by Garfinkel (1944) and applied using lidar measurements at various altitudes. For practical applications in astrometry, no lidar observations are available, and one is led to represent the atmosphere by a model that allows computation of $R$ as a function only of conditions (temperature, pressure, etc.) at the observatory.

# 6.1.1 Planar stratified layers

The simplest model is to consider that the atmosphere is described by plane horizontal layers. In this case, the normals to the layers are all parallel to the vertical, so that $\xi$ can be replaced by $z$ , and formula (6.1) simply reduces to consider that the quantity $n \sin z$ is an invariant, so that at the two limits of the integration, one has

$$
n _ { 0 } \sin z _ { 0 } = \sin z .
$$

Replacing z by its expression (6.2) and neglecting $R ^ { 2 }$ , one gets the first-order refraction formula,

$$
R = ( n _ { 0 } - 1 ) \tan z _ { 0 } .
$$

This is a very poor representation of the actual refraction, except very close to the zenith.

![](images/9e961933f4e3c0e9cf65c8d4402688f3458894f945a4ff77c0fe5983b8d4cb9a.jpg)  
Fig. 6.1. Refraction through a spherical atmospheric layer.

# 6.1.2 Spherical atmosphere model

The next step is to assume that the atmosphere is radially symmetric around the local vertical. The iso-refractive index curves are spheres centered at the center of the Earth, $o$ . Let $r _ { 0 }$ be the radius vector at the observer, $\varOmega$ , and $z _ { 0 }$ the apparent zenith distance of the ray, with respect to the vertical $V ( O \varOmega )$ . Let us consider a small layer with a width $\mathrm { d } \boldsymbol { r }$ and a refractive index $n$ . Let $N M$ (Fig. 6.1) be the linear path of the light within this layer. At $N$ , one may apply Snell’s law to the light coming from the outer medium with the refractive index equal to $n - \mathrm { d } n$ . Calling $\psi$ and $\xi + \mathrm { d } \xi$ , respectively, the refractive and incidence angles in $N$ , one has

$$
n \sin \psi = ( n - \mathrm { d } n ) \sin ( \xi + \mathrm { d } \xi ) .
$$

Let $\theta$ be the angle between the verticals at $\varOmega$ and $M , \mathrm { d } \theta$ its increment from $M$ to $N$ , and $r$ the radius vector at $M$ . The sine relation in $O M N$ gives

$$
r \sin \xi = ( r + \mathrm { d } r ) \sin \psi .
$$

Multiplying both equations, member by member, one gets, after simplification by sin $\psi$ :

$$
n r \sin \xi = ( r + \mathrm { d } r ) ( n - \mathrm { d } n ) \sin ( \xi + \mathrm { d } \xi ) .
$$

This relation proves that the quantity $n r \sin \xi$ is an invariant, so that

$$
n r \sin \psi = n _ { 0 } r _ { 0 } \sin z _ { 0 } .
$$

Now, since $z = \theta + \psi$ in the triangle $K O M$ , and since in $M H N$ , tan $\psi = r \mathrm { d } \theta / \mathrm { d } r$ , one gets

$$
\mathrm { d } z = \mathrm { d } \psi + { \frac { \tan \psi } { r } } \mathrm { d } r .
$$