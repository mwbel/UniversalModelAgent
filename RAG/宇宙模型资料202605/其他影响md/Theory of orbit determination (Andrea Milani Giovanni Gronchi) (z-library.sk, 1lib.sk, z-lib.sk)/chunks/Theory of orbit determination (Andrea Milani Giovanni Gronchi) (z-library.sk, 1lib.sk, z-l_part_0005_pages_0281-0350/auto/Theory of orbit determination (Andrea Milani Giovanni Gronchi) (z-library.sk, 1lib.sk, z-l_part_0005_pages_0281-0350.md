$$
\begin{array} { l } { \ell = 1 \implies f ( \mu ) = a _ { 1 } \mu = a _ { 1 } \sin \theta } \\ { \ell = 2 \implies f ( \mu ) = - 3 a _ { 0 } \mu ^ { 2 } + a _ { 0 } = a _ { 0 } \left( 1 - 3 \sin ^ { 2 } \theta \right) . } \end{array}
$$

By selecting for each integer $\ell$ a suitable constant factor we define a set of solutions of (13.7), the Legendre polynomials with argument $\sin \theta$ :

$$
P _ { \ell } ( \sin \theta ) = \sum _ { j = 0 } ^ { L } \ T _ { \ell j } \ ( \sin \theta ) ^ { \ell - 2 j } ,
$$

where $L$ is the integer part of $\ell / 2$ and $\mathit { \Delta } T _ { \ell j }$ is a coefficient solution of an equation equivalent to (13.9) going backward, that is the value of the coefficient $T _ { \ell 0 }$ of the highest degree in $\sin \theta$ is assigned first (Kaula 1966, Chapter 1)

$$
T _ { \ell j } = - { \frac { ( \ell - 2 j + 1 ) ( \ell - 2 j + 2 ) } { 2 j ( 2 \ell - 2 j + 1 ) } } T _ { \ell j - 1 } , T _ { \ell 0 } = { \frac { ( 2 \ell ) ! } { ( \ell ! ) ^ { 2 } 2 ^ { \ell } } } .
$$

The reason for this choice of $T _ { \ell 0 }$ will be explained later, by eq. (13.17). By combining the solution for $F ( \theta )$ with the solutions for $R ( r )$ we obtain two linearly independent solutions of the Laplace equation for each integer $\ell \geq 0$

$$
P _ { \ell } ( \sin \theta ) \frac { 1 } { r ^ { \ell + 1 } } , P _ { \ell } ( \sin \theta ) r ^ { \ell } ,
$$

where those with $r ^ { \ell }$ are smooth at the origin and unlimited for $r  + \infty$ , describing the gravity field inside a cavity surrounded by a mass distribution; they are internal harmonics. Those with $1 / r ^ { \ell + 1 }$ are of interest for satellite orbits: they are singular for $r = 0$ , and for $r  + \infty$ they tend to 0, the external harmonics. In this book we shall consider only the external zonal spherical harmonic of degree $\ell$ . The Legendre polynomials have exactly $\ell$ real roots in the interval $- 1 < \sin \theta < 1$ (Hobson 1931, pp. 18– 19), that is the zonal spherical harmonics have as many zeros along each meridian as the degree $\ell$ . This can give an intuitive understanding of the shape corresponding to each harmonic; e.g., $\ell = 2$ corresponds to an oblate (or prolate) shape, with flattening along the $x _ { 3 }$ axis, $\ell = 3$ to a pear shape giving different mass to the two hemispheres separated by the $x _ { 3 } = 0$ plane.

# Tesseral spherical harmonics

To remove the assumption of axial symmetry, we look for solutions of the Laplace equation depending upon all the polar coordinates, by using again the separation of variables, that is assuming $U = \Phi ( r , \theta , \lambda ) =$

$R ( r ) F ( \theta ) G ( \lambda )$ . By eq. (13.5)

$$
r ^ { 2 } \Delta \Phi = F G { \frac { d } { d r } } \left[ r ^ { 2 } { \frac { d R } { d r } } \right] + R \Delta _ { S } ( F G ) = 0
$$

and dividing by $U = R F G$ we get an equation equivalent to Laplace:

$$
{ \frac { r ^ { 2 } } { R F G } } \Delta \Phi = { \frac { 1 } { R } } { \frac { d } { d r } } \left[ r ^ { 2 } { \frac { d R } { d r } } \right] + { \frac { \Delta _ { S } ( F G ) } { F G } } = 0 .
$$

The two terms in the equation being a function of $r$ and a function of $( \theta , \lambda )$ , they have to be constant, thus defining an ordinary differential equation for $R ( r )$ , the same as the zonal case, and the partial differential equation

$$
\Delta _ { S } ( F G ) = - \ell ( \ell + 1 ) F G ,
$$

that is, $F ( \theta ) G ( \lambda )$ has to be an eigenfunction of the Laplace–Beltrami operator. The same argument can be applied to the two terms of

$$
{ \frac { \cos ^ { 2 } \theta } { F G } } \ \Delta _ { S } ( F G ) = { \frac { \cos \theta } { F } } \ { \frac { d } { d \theta } } \left[ \cos \theta \ { \frac { d F } { d \theta } } \right] + { \frac { 1 } { G } } \ { \frac { d ^ { 2 } G } { d \lambda ^ { 2 } } } = - \ell ( \ell + 1 ) \ \cos ^ { 2 } \theta .
$$

By selecting a negative constant for the term containing $\lambda$

$$
\frac { 1 } { G } \frac { d ^ { 2 } G } { d \lambda ^ { 2 } } = - m ^ { 2 } ,
$$

the equation for $G ( \lambda )$ and its solutions are

$$
\frac { d ^ { 2 } G } { d \lambda ^ { 2 } } + m ^ { 2 } G = 0 \Longleftrightarrow G ( \lambda ) = C _ { \ell m } \cos ( m \lambda ) + S _ { \ell m } \sin ( m \lambda ) ,
$$

pure trigonometric functions.7 Thus the equation for $F ( \theta )$ i s

$$
{ \frac { 1 } { F \cos \theta } } { \frac { d } { d \theta } } \left[ \cos \theta { \frac { d F } { d \theta } } \right] - { \frac { m ^ { 2 } } { \cos ^ { 2 } \theta } } = - \ell ( \ell + 1 ) .
$$

For $m = 0$ we obtain again eq. (13.7), that is the zonal harmonics. With the same arguments used in the previous section we can select for $R ( r )$ only the solution $1 / r ^ { \ell + 1 }$ , to get the external harmonics. The equation for $F ( \theta )$ is simplified by the change of variables $\mu = \sin \theta$ : if we set

$$
F ( \theta ) = ( \cos \theta ) ^ { m } f ( \sin \theta ) ,
$$

the function $f ( \mu )$ is a solution of the linear second-order differential equation

$$
\left( 1 - \mu ^ { 2 } \right) \frac { d ^ { 2 } f } { d \mu ^ { 2 } } - 2 ( m + 1 ) \mu \frac { d f } { d \mu } + ( \ell - m ) ( \ell + m + 1 ) f = 0 .
$$

By using the series expansion (13.8) we obtain again a second-order recursion formula

$$
a _ { k + 2 } = \frac { k ( k + 2 m + 1 ) - ( \ell - m ) ( \ell + m + 1 ) } { ( k + 2 ) ( k + 1 ) } a _ { k } .
$$

Again, as in the case of eq. (13.9), we can obtain solutions with a finite number of terms, a product of a polynomial in $\sin \theta$ of degree $k _ { m a x } = \ell - m$ with a power of $\cos \theta$ can be obtained; the polynomial has only even powers if $\ell - m$ is even, odd powers if $\ell - m$ is odd. Thus a solution of the differential equation for $F ( \theta )$ is the Legendre associated function of harmonic degree $\ell$ and harmonic order $m$

$$
P _ { \ell m } ( \sin \theta ) = ( 1 - \sin ^ { 2 } \theta ) ^ { m / 2 } \sum _ { j = 0 } ^ { L } T _ { \ell m j } ( \sin \theta ) ^ { \ell - m - 2 j } ,
$$

where $L$ is the integer part of $( \ell - m ) / 2$ , and the coefficients of the monomials in $\sin \theta$ are

$$
T _ { \ell m j } = - { \frac { ( \ell - m - 2 j + 1 ) ( \ell - m - 2 j + 2 ) } { 2 j ( 2 \ell - 2 j + 1 ) } } T _ { \ell m j - 1 } ,
$$

$$
T _ { \ell m 0 } = ( 2 \ell ) ! / \ell ! ( \ell - m ) ! 2 ^ { \ell } .
$$

By combining together the three functions $R ( r ) , F ( \theta )$ , and $G ( \lambda )$ , we find two spherical harmonic functions of degree $\ell$ and order $m$

$$
{ \frac { P _ { \ell m } ( \sin \theta ) } { r ^ { \ell + 1 } } } \cos ( m \lambda ) , { \frac { P _ { \ell m } ( \sin \theta ) } { r ^ { \ell + 1 } } } \sin ( m \lambda ) .
$$

For $m = 0$ we obtain only one solution, which is a zonal spherical harmonic. For $m > 0$ we obtain tesseral spherical harmonic functions. Some qualitative properties of the spherical harmonics: the harmonic of degree $\ell$ and order $m$ has $\ell - m$ zeros along each meridian and $2 m$ zeros along each parallel (and zeros at the two poles for $m > 0$ ). For $\ell - m = 0$ we have sectorial spherical harmonic functions, independent of the latitude.

# Expansion in spherical harmonics

The Laplace equation is linear, thus linear combinations of spherical harmonics are still solutions:

$$
\begin{array} { r c l } { { } } & { { = \displaystyle \frac { G M } { r } } } & { { + } } & { { \displaystyle \frac { G M } { r } \sum _ { \ell = 1 } ^ { + \infty } P _ { \ell } ( \sin \theta ) \ \frac { R _ { \oplus } ^ { \ell } } { r ^ { \ell } } C _ { \ell 0 } } } \\ { { } } & { { } } & { { + } } & { { \displaystyle \frac { G M } { r } \sum _ { \ell = 1 } ^ { + \infty } \sum _ { m = 1 } ^ { \ell } P _ { \ell m } ( \sin \theta ) \ \frac { R _ { \oplus } ^ { \ell } } { r ^ { \ell } } \ [ C _ { \ell m } \cos ( m \lambda ) + S _ { \ell m } \sin ( m \lambda ) ] . } } \end{array}
$$

where the length $R _ { \oplus }$ , to be interpreted as the equatorial radius of the Earth (or of the relevant planet), has been added to have adimensional coefficients $C _ { \ell m }$ , with $0 \leq m \leq \ell$ , and $S _ { \ell m }$ with $0 < m \le \ell$ . $M$ is the total mass of the planet as defined by eq. (13.1). By using the conventions $P _ { \ell 0 } = P _ { \ell } , P _ { 0 } = 1$ we can use the more compact formula

$$
U = { \frac { G M } { r } } \left\{ \sum _ { \ell = 0 } ^ { + \infty } \sum _ { m = 0 } ^ { \ell } P _ { \ell m } ( \sin \theta ) \ { \frac { R _ { \oplus } ^ { \ell } } { r ^ { \ell } } } \left[ C _ { \ell m } \cos ( m \lambda ) + S _ { \ell m } \sin ( m \lambda ) \right] \right\} .
$$

Another useful representation is by means of the set of harmonic functions on the sphere $r = R _ { \oplus }$ , which can be considered as functions of $( \theta , \lambda )$ only:

Y $\mathsf { \Pi } _ { \ell m i } ^ { \prime } = P _ { \ell m } ( \sin \theta ) \operatorname { t r i g } ( m \lambda , i ) , \operatorname { t r i g } ( m \lambda , 1 ) = \cos ( m \lambda ) , \operatorname { t r i g } ( m \lambda , 0 ) = \sin ( m \lambda )$ mλ); then the expansion (13.15) becomes

$$
U = \sum _ { \ell = 0 } ^ { + \infty } { \frac { G M R _ { \oplus } ^ { \ell } } { r ^ { \ell + 1 } } } \sum _ { m = 0 } ^ { \ell } \left[ C _ { \ell m } Y _ { \ell m 1 } + S _ { \ell m } Y _ { \ell m 0 } \right] .
$$

What we need is a relationship between the expansions in series of harmonic functions, such as the one above, and the properties of the extended mass generating the gravity field, that is of the mass density function $\rho$ . For this we need to restart from eq. (13.3) and to expand the kernel used to generate the potential $U$ from the density $\rho$ :

$$
{ \frac { 1 } { | \mathbf { x } - \mathbf { p } | } } = { \frac { 1 } { | \mathbf { x } | } } \left[ 1 - 2 { \frac { | \mathbf { p } | } { | \mathbf { x } | } } \cos \psi + { \frac { | \mathbf { p } | ^ { 2 } } { | \mathbf { x } | ^ { 2 } } } \right] ^ { - 1 / 2 }
$$

where $\psi$ is the angle between $\mathbf { x }$ and $\mathbf { p }$ , that is $\cos \psi = { \bf x } \cdot { \bf p } / | { \bf x } | | { \bf p } |$ . This inverse distance can be expanded as

$$
{ \frac { 1 } { \left| \mathbf { x } - \mathbf { p } \right| } } = \sum _ { \ell = 0 } ^ { + \infty } { \frac { | \mathbf { p } | ^ { \ell } } { | \mathbf { x } | ^ { \ell + 1 } } } P _ { \ell } ( \cos \psi )
$$

where $P _ { \ell }$ are Legendre polynomials because $1 / | \mathbf { x } - \mathbf { p } |$ is harmonic for $\mathbf { x } \neq \mathbf { p }$ . However, the Legendre polynomials contain an arbitrary factor, thus we need to check that those appearing in eq. (13.18) have the coefficient we have selected in eq. (13.11). To confirm this we have to compute the coefficient of highest degree in $\cos \psi$ among the terms with factor $| \mathbf { p } | / | \mathbf { x } |$ in the expansion (13.17) and confirm it coincides with $T _ { \ell 0 }$ :

$$
\left( { - 1 / 2 } \right) ( - 2 ) ^ { \ell } = { \frac { ( - 1 ) ^ { \ell } } { \ell ! } } \prod _ { k = 1 } ^ { \ell } ( 2 k - 1 ) = { \frac { ( 2 \ell ) ! } { ( \ell ! ) ^ { 2 } 2 ^ { \ell } } } = T _ { \ell 0 } .
$$

By substituting the expansion in Legendre polynomials into eq. (13.3) we get

$$
U ( \mathbf { x } ) = \int _ { W } \ { \frac { G \rho ( \mathbf { p } ) } { | \mathbf { x } - \mathbf { p } | } } \ d \mathbf { p } = \sum _ { \ell = 0 } ^ { + \infty } \ { \frac { G } { | \mathbf { x } | ^ { \ell + 1 } } } \ \int _ { W } \ \rho ( \mathbf { p } ) \ | \mathbf { p } | ^ { \ell } \ P _ { \ell } ( \cos \psi ) \ d \mathbf { p }
$$

and comparing with (13.15), the part of $U$ with factor $G / r ^ { \ell + 1 }$ , where $r = | { \bf x } |$ is

$$
\int _ { W } \rho ( { \bf p } ) | { \bf p } | ^ { \ell } P _ { \ell } ( \cos \psi ) d { \bf p } = M \sum _ { m = 0 } ^ { \ell } R _ { \oplus } ^ { \ell } \left[ C _ { \ell m } Y _ { \ell m 1 } + S _ { \ell m } Y _ { \ell m 0 } \right] .
$$

# Total mass and center of mass

As an example, let $\ell = 0$ ; $P _ { \ell } = 1$ and the equation above reduces to

$$
C _ { 0 0 } = { \frac { 1 } { M } } \ \int _ { W } \ \rho ( { \bf p } ) \ d { \bf p } = 1 .
$$

Let $\ell = 1$ ; the spherical harmonics are

$$
{ \bf \dot { \tau } } _ { 1 0 1 } = P _ { 1 0 } = x _ { 3 } / r , Y _ { 1 1 1 } = P _ { 1 1 } \cos \lambda = x _ { 1 } / r , Y _ { 1 1 0 } = P _ { 1 1 } \sin \lambda = x _ { 1 }
$$

and eq. (13.20) multiplied by $r = | \mathbf { x } |$ becomes

$$
{ \frac { 1 } { M } } \mathbf { x } \cdot \int _ { W } \rho ( \mathbf { p } ) \mathbf { p } d \mathbf { p } = R _ { \oplus } \left[ C _ { 1 1 } x _ { 1 } + S _ { 1 1 } x _ { 2 } + C _ { 1 0 } x _ { 3 } \right] ,
$$

the harmonic coefficients for $\ell = 1$ are related to the center of mass

$$
\mathbf { c } ^ { M } = ( 1 / M ) \int _ { W } \rho ( \mathbf { p } ) \mathbf { p } d \mathbf { p } ;
$$

in fact

$$
C _ { 1 1 } = \mathrm { c } _ { 1 } ^ { M } / R _ { \oplus } , S _ { 1 1 } = \mathrm { c } _ { 2 } ^ { M } / R _ { \oplus } , C _ { 1 0 } = \mathrm { c } _ { 3 } ^ { M } / R _ { \oplus } .
$$

As a consequence, if the origin of the coordinate system coincides with the planet center of mass, the coefficients of degree 1 are zero and the expansion of $U$ after the point mass term begins with degree 2:

$$
\frac { G M } { r } \left\{ 1 + \sum _ { \ell = 2 } ^ { + \infty } \sum _ { m = 0 } ^ { \ell } P _ { \ell m } ( \sin \theta ) \left( \frac { R _ { \oplus } } { r } \right) ^ { \ell } \left[ C _ { \ell m } \cos ( m \lambda ) + S _ { \ell m } \sin ( m \lambda ) \right] \right\} _ { r }
$$

that is, the point mass approximation is accurate to ${ \mathcal { O } } ( R _ { \oplus } ^ { 2 } / r ^ { 2 } )$ .

# Moments of inertia

Let $\ell = 2$ ; the Legendre functions are

$$
P _ { 2 0 } = { \frac { 3 } { 2 } } \sin ^ { 2 } \theta - { \frac { 1 } { 2 } } , P _ { 2 1 } = 3 \sin \theta \cos \theta , P _ { 2 2 } = 3 \cos ^ { 2 } \theta
$$

and the spherical harmonics are

$$
\begin{array} { l l } { { } } & { { \mathrm { \zeta _ { 2 0 1 } } = P _ { 2 0 } = ( 3 x _ { 3 } ^ { 2 } - r ^ { 2 } ) / 2 r ^ { 2 } , } } \\ { { } } & { { \mathrm { \zeta _ { 2 1 1 } } = P _ { 2 1 } \cos \lambda = 3 x _ { 3 } x _ { 1 } / r ^ { 2 } , } } \\ { { } } & { { \mathrm { \zeta _ { 2 2 1 } } = P _ { 2 2 } \cos ( 2 \lambda ) = 3 ( x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } ) / r ^ { 2 } , } } \end{array} ~ Y _ { 2 1 0 } = P _ { 2 1 } \sin \lambda = 3 x _ { 3 } x _ { 2 } / r ^ { 2 }
$$

and eq. (13.20) for $\ell = 2$ multiplied by $r ^ { 2 } / ( M R _ { \oplus } ^ { 2 } )$ becomes

$$
\begin{array} { l } { { \displaystyle { \frac { r ^ { 2 } } { M R _ { \oplus } ^ { 2 } } } \int _ { W } \rho ( { \bf p } ) | { \bf p } | ^ { 2 } \frac { 3 \cos ^ { 2 } \psi - 1 } { 2 } d { \bf p } } } \\ { { \displaystyle ~ = \frac { C _ { 2 0 } } { 2 } ( 2 x _ { 3 } ^ { 2 } - x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } ) + 3 C _ { 2 1 } x _ { 3 } x _ { 1 } + 3 S _ { 2 1 } x _ { 3 } x _ { 2 } } } \\ { { \displaystyle ~ + 3 C _ { 2 2 } ( x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } ) + 6 S _ { 2 2 } x _ { 1 } x _ { 2 } . } } \end{array}
$$

The geophysical significance of the degree $\ell = 2$ coefficients can be understood by expressing them in terms of the integrals

$$
A _ { i j } = { \frac { 1 } { M \ R _ { \oplus } ^ { 2 } } } \ \int _ { W } \ \rho ( { \bf p } ) \ p _ { i } p _ { j } \ d { \bf p } \qquad i , j = 1 , 2 , 3 .
$$

Taking into account that

$$
| { \bf x } | ^ { 2 } | { \bf p } | ^ { 2 } P _ { 2 } ( \cos \psi ) = \frac { 1 } { 2 } \left[ 3 ( { \bf x } \cdot { \bf p } ) ^ { 2 } - | { \bf x } | ^ { 2 } | { \bf p } | ^ { 2 } \right]
$$

and expanding as functions of the coordinates $( x _ { 1 } , x _ { 2 } , x _ { 3 } )$ and $\left( p _ { 1 } , p _ { 2 } , p _ { 3 } \right)$ we obtain the relationship between the integrals $A _ { i j }$ and the coefficients of harmonic degree $\ell = 2$

$$
\begin{array} { r l } & { \mathrm { \Lambda } _ { 1 } ^ { 2 } ( 2 A _ { 1 1 } - A _ { 2 2 } - A _ { 3 3 } ) + x _ { 2 } ^ { 2 } ( 2 A _ { 2 2 } - A _ { 1 1 } - A _ { 3 3 } ) + x _ { 3 } ^ { 2 } ( 2 A _ { 3 3 } - A _ { 1 1 } - A _ { 2 2 }  } \\ & {  \qquad + 6 ( x _ { 1 } x _ { 2 } A _ { 1 2 } + x _ { 2 } x _ { 3 } A _ { 2 3 } + x _ { 1 } x _ { 3 } A _ { 1 3 } )  } \\ & {  \qquad = C _ { 2 0 } ( 2 x _ { 3 } ^ { 2 } - x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } ) + 6 C _ { 2 1 } x _ { 3 } x _ { 1 } + 6 S _ { 2 1 } x _ { 3 } x _ { 2 } + 6 C _ { 2 2 } ( x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } )  } \\ & {  \qquad + 1 2 S _ { 2 2 } x _ { 1 } x _ { 2 } . } \end{array}
$$

The coefficients of polynomial degree 2 in the $x _ { j }$ variables provide a system of six equations, which is linear in the six integrals $A _ { i j }$ and in the five geopotential coefficients, and can be solved for the latter

$$
\begin{array} { r c l } { { \displaystyle C _ { 2 0 } } } & { { = } } & { { \displaystyle { A _ { 3 3 } - \frac { A _ { 1 1 } + A _ { 2 2 } } { 2 } } , ~ C _ { 2 2 } = \frac { 1 } { 4 } ( A _ { 1 1 } - A _ { 2 2 } ) , } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle C _ { 2 1 } } } & { { = } } & { { \displaystyle { A _ { 1 3 } } , ~ S _ { 2 1 } = A _ { 2 3 } , ~ S _ { 2 2 } = \frac { 1 } { 2 } A _ { 1 2 } . } } \end{array}
$$

If the origin of the coordinates, corresponding to $r ~ = ~ 0$ , is the center

of mass, then the integrals $A _ { i j }$ can be combined to provide the inertia quadratic form of the planet, represented by a symmetric positive definite $3 \times 3$ matrix with diagonal coefficients

$$
I _ { j j } = M R _ { \oplus } ^ { 2 } \left( A _ { i i } + A _ { k k } \right) \mathrm { w i t h } i \neq j \neq k \neq i
$$

and off-diagonal

$$
{ \cal I } _ { i j } = - M R _ { \oplus } ^ { 2 } A _ { i j } \mathrm { w i t h } i \ne j .
$$

Then the degree 2 harmonic coefficients of the gravity field of the planet can be computed in terms of the inertia matrix

$$
\begin{array} { r c l } { { C _ { 2 0 } } } & { { = } } & { { \displaystyle \frac { 1 } { M R _ { \oplus } ^ { 2 } } \left[ \frac { I _ { 1 1 } + I _ { 2 2 } } { 2 } - I _ { 3 3 } \right] , C _ { 2 2 } = \frac { 1 } { 4 M R _ { \oplus } ^ { 2 } } ( I _ { 2 2 } - I _ { 1 1 } ) , } } \\ { { C _ { 2 1 } } } & { { = } } & { { \displaystyle \frac { - 1 } { M R _ { \oplus } ^ { 2 } } I _ { 1 3 } , S _ { 2 1 } = \frac { - 1 } { M R _ { \oplus } ^ { 2 } } I _ { 2 3 } , S _ { 2 2 } = \frac { - 1 } { 2 M R _ { \oplus } ^ { 2 } } I _ { 1 2 } . ( } } \end{array}
$$

It is possible to select a reference system diagonalizing the inertia quadratic form, that is such that $I _ { i j } = 0$ for $i \neq j$ ; then $C _ { 2 1 } , S _ { 2 1 } , S _ { 2 2 }$ would be zero. The problem is that such a reference system is not known a priori: only information on the rotational state of the planet can be used to determine it. To solve for all the $I _ { j j }$ from the harmonic coefficients is not possible: some scale factor, e.g., the concentration coefficient $I _ { m a x } / M R _ { \oplus } ^ { 2 }$ where $I _ { m a x }$ is the largest eigenvalue of the inertia matrix, needs to be constrained by the rotation state information. This is another case of the following general property: the internal mass distribution cannot be determined by knowing only the gravity field outside of the body (see Section 13.1 and Chapter 17).

# Recursion formulae

In the computation of the spherical harmonic functions at a given point with polar coordinates $( r , \theta , \lambda )$ it is not convenient to compute the coefficients $T _ { \ell m j }$ from eq. (13.14), but rather the values of the Legendre polynomials and the associate functions could be computed by a recursion formula. There are many possible such formulae, we give here just one example: for the zonal harmonics (Hobson 1931, pp. 32–33)

$$
\ell P _ { \ell } ( \mu ) = ( 2 \ell - 1 ) \mu P _ { \ell - 1 } ( \mu ) - ( \ell - 1 ) P _ { \ell - 2 } ( \mu )
$$

and for the tesseral harmonics (Hobson 1931, pp. 107–108)

$$
( \ell - m ) ~ P _ { \ell m } ( \mu ) - ( 2 \ell - 1 ) \mu P _ { \ell - 1 m } ( \mu ) + ( \ell + m - 1 ) P _ { \ell - 2 m } ( \mu ) = 0 .
$$

Given the initial values

$$
P _ { 0 0 } ( \mu ) = 1 , ~ P _ { 1 0 } ( \mu ) = \mu , ~ P _ { 1 1 } ( \mu ) = \sqrt { 1 - \mu ^ { 2 } }
$$

it is possible to compute all the Legendre polynomials and associate functions, up to a maximum degree $\ell _ { m a x }$ , at some value of $\mu = \sin \theta$ by two-index recursion. The trigonometric functions $\sin ( m \lambda ) , \cos ( m \lambda )$ can also be computed recursively for a fixed $\lambda$ by the trigonometric addition formulae. In this way it is possible to set up a very efficient algorithm to compute all the spherical harmonic functions up to $\ell = \ell _ { m a x }$ at a given point.

To compute the partial derivatives of the potential, the gravity field components in the equation of motion and the second derivatives in the variational equation, it is efficient to use formulae expressing the derivatives of the spherical harmonics by means of combinations of Legendre polynomials, Legendre associated functions and trigonometric functions of $\lambda$ . The derivatives with respect to $r$ and $\lambda$ are elementary; for those with respect to $\theta$ it is convenient to use the relationships between the Legendre polynomials and their derivatives (Hobson 1931, p. 32)

$$
( \mu ^ { 2 } - 1 ) \frac { d P _ { \ell } ( \mu ) } { d \mu } = \ell \left[ \mu P _ { \ell } ( \mu ) - P _ { \ell - 1 } ( \mu ) \right]
$$

and for the associated Legendre functions (Wagner and Velez 1972, chapters 5–6)

$$
{ \frac { d P _ { \ell m } ( \sin \theta ) } { d \theta } } = P _ { \ell ( m + 1 ) } ( \sin \theta ) - m { \mathrm { ~ t a n } } \theta P _ { \ell m } ( \sin \theta )
$$

where the first $\mathrm { { t e r m } = 0 }$ for $m = \ell$ (we define $P _ { \ell m } = 0$ for $m > \ell$ ).

# 13.3 The Hilbert space of the harmonic functions

What is the rigorous meaning of the infinite summation in eq. (13.15)? Are the harmonic coefficients $C _ { \ell m } , S _ { \ell m }$ uniquely defined for a given harmonic function $U ( \mathbf { x } )$ ? To solve these problems we need some additional properties of the spherical harmonics, and this requires some functional analysis.8

# Orthogonality

The spherical harmonics on the sphere $Y _ { \ell m i }$ have the property, which has been used in the procedure of separation of variables, of being eigenfunctions of the Laplace–Beltrami operator: $\Delta _ { S } Y _ { \ell m i } = - \ell ( \ell + 1 )$ $Y _ { \ell m i }$ . This implies

that the functions $Y _ { \ell m i }$ are orthogonal with respect to the scalar product defined by the surface integral over $S ( 1 )$

$$
\langle Y _ { \ell m i } , Y _ { \ell ^ { \prime } m ^ { \prime } i ^ { \prime } } \rangle = \int _ { S ( 1 ) } Y _ { \ell m i } Y _ { \ell ^ { \prime } m ^ { \prime } i ^ { \prime } } d S = 0
$$

unless $\ell = \ell ^ { \prime } , m = m ^ { \prime } , i = i ^ { \prime }$ . Indeed

$$
- \ell ( \ell + 1 ) \left. Y _ { \ell m i } , Y _ { \ell ^ { \prime } m ^ { \prime } i ^ { \prime } } \right. = \left. \Delta _ { S } Y _ { \ell m i } , Y _ { \ell ^ { \prime } m ^ { \prime } i ^ { \prime } } \right. = \int _ { S ( 1 ) } \Delta _ { S } Y _ { \ell m i } , Y _ { \ell ^ { \prime } m ^ { \prime } i ^ { \prime } } d
$$

where the surface element in spherical polar coordinates is $d S = \cos \theta d \theta d \lambda$

$$
\begin{array} { l } { { \displaystyle \int _ { S ( 1 ) } \Delta _ { S } Y _ { \ell m i } , Y _ { \ell ^ { \prime } m ^ { \prime } i ^ { \prime } } d S } } \\ { { \displaystyle ~ = \int _ { 0 } ^ { 2 \pi } d \lambda \int _ { - \pi / 2 } ^ { \pi / 2 } \left[ Y _ { m ^ { \prime } \ell ^ { \prime } i ^ { \prime } } \Delta _ { S } Y _ { \ell m i } \right] \cos \theta d \theta } } \\ { { \displaystyle ~ = I _ { \theta } \int _ { 0 } ^ { 2 \pi } t r ( m ^ { \prime } \lambda , i ^ { \prime } ) t r ( m \lambda , i ) d \lambda = \pi \delta _ { m m ^ { \prime } } \delta _ { i i ^ { \prime } } I _ { \theta } } } \end{array}
$$

where $\delta _ { j k } = 0$ for $j \neq k$ , $\delta _ { j j } = 1$ and the integral $I _ { \theta }$ over the variable $\theta$ can be computed by parts:

$$
\begin{array} { r c l } { { I _ { \theta } } } & { { = } } & { { \displaystyle \int _ { - \pi / 2 } ^ { \pi / 2 } \left[ - \cos \theta \frac { \partial P _ { \ell m } } { \partial \theta } \frac { \partial P _ { \ell ^ { \prime } m ^ { \prime } } } { \partial \theta } - \frac { m ^ { 2 } } { \cos \theta } P _ { \ell m } P _ { \ell ^ { \prime } m ^ { \prime } } \right] d \theta . } } \end{array}
$$

The last step in (13.28) is due to the usual orthogonality of the sine and cosine functions over the interval $[ 0 , 2 \pi ]$ .

Given that $m = m ^ { \prime }$ , otherwise the other factor is zero, the integral $I _ { \theta }$ is symmetric with respect to the exchange of $( \ell ^ { \prime } , m ^ { \prime } , i ^ { \prime } )$ with $( \ell , m , i )$ , that is of the two spherical harmonics.9 Then

$$
\begin{array} { r l } & { - \ell ( \ell + 1 ) \left. Y _ { \ell m i } , Y _ { \ell ^ { \prime } m ^ { \prime } i ^ { \prime } } \right. } \\ & { = \left. \Delta _ { S } Y _ { \ell m i } , Y _ { \ell ^ { \prime } m ^ { \prime } i ^ { \prime } } \right. = \left. Y _ { \ell m i } , \Delta _ { S } Y _ { \ell ^ { \prime } m ^ { \prime } i ^ { \prime } } \right. = - \ell ^ { \prime } ( \ell ^ { \prime } + 1 ) \left. Y _ { \ell m i } , Y _ { \ell ^ { \prime } m ^ { \prime } i ^ { \prime } } \right. } \end{array}
$$

implying the scalar product is zero whenever $( \ell , m , i ) \neq ( \ell ^ { \prime } , m ^ { \prime } , i ^ { \prime } )$ . Thus the spherical harmonic functions $\{ Y _ { \ell m i } \}$ are an orthogonal set and the coefficients $C _ { \ell m }$ for $i = 1$ , $S _ { \ell m }$ for $i = 0$ define the corresponding components.

# Normalization

The spherical harmonics $\{ Y _ { \ell m i } \}$ are not an orthonormal set, that is the squared $L ^ { 2 }$ norm on $S ( 1 )$ is10

$$
\langle Y _ { \ell m i } , Y _ { \ell m i } \rangle = \int _ { 0 } ^ { 2 \pi } [ \mathrm { t r i g } ( m \lambda , i ) ] ^ { 2 } d \lambda \int _ { - \pi / 2 } ^ { \pi / 2 } \cos \theta \left[ P _ { \ell m } ( \sin \theta ) \right] ^ { 2 } d \theta
$$

$$
\begin{array} { r l l } { { \mathrm { ( f o r ~ } m = 0 , i = 1 \mathrm { ) } } } & { { { } = } } & { { 2 \pi \displaystyle \int _ { - 1 } ^ { 1 } ~ [ P _ { \ell } ( \mu ) ] ^ { 2 } ~ d \mu = \frac { 4 \pi } { 2 \ell + 1 } , \nonumber } } \\ { { \mathrm { ( f o r ~ } m > 0 \mathrm { ) } } } & { { { } = } } & { { \pi \displaystyle \int _ { - 1 } ^ { 1 } ~ [ P _ { \ell m } ( \mu ) ] ^ { 2 } ~ d \mu = \frac { 2 \pi } { 2 \ell + 1 } \displaystyle \frac { ( \ell + m ) ! } { ( \ell - m ) ! } . } } \end{array}
$$

Thus we can define the normalized harmonics and the normalized associate Legendre functions with unit quadratic mean on the sphere

$$
\begin{array} { l l l } { { \overline { { { Y } } } _ { \ell m i } } } & { { = } } & { { \overline { { { P } } } _ { \ell m } ( \sin \theta ) \mathrm { t r i g } ( m \lambda , i ) } } \\ { { } } & { { = } } & { { \sqrt { ( 2 \ell + 1 ) ( 2 - \delta _ { 0 m } ) { \frac { ( \ell - m ) ! } { ( \ell + m ) ! } } } Y _ { \ell m i } = H _ { \ell m } Y _ { \ell m i } } } \\ { { } } & { { } } & { { } } \end{array}
$$

( $\delta _ { 0 m } = 1$ for $m = 0$ , $\delta _ { 0 m } = 0$ otherwise). If we use $\{ Y _ { \ell m i } \}$ as an orthonormal function set on $S ( 1 )$ the expansion of the gravitational potential is

$$
= \frac { G M } { r } \left\{ \sum _ { \ell = 0 } ^ { + \infty } \sum _ { m = 0 } ^ { \ell } \overline { { { P } } } _ { \ell m } ( \sin \theta ) \left( \frac { R _ { \oplus } } { r } \right) ^ { \ell } \left[ \overline { { { C } } } _ { \ell m } \cos ( m \lambda ) + \overline { { { S } } } _ { \ell m } \sin ( m \lambda ) \right] \right\}
$$

$\overline { { C } } _ { \ell m } , \overline { { S } } _ { \ell m }$ are normalized harmonic coefficients of degree $\ell$ and order $m$ :

$$
\overline { { C } } _ { \ell m } = \frac { C _ { \ell m } } { H _ { \ell m } } , \quad \overline { { S } } _ { \ell m } = \frac { S _ { \ell m } } { H _ { \ell m } } .
$$

The degree $\ell \ = \ 1$ terms do not appear if the reference system has the center of mass as origin. For a given harmonic function $U = \Phi ( r , \theta , \lambda )$ , the normalized coefficients $\overline { { C } } _ { \ell m } , \overline { { S } } _ { \ell m }$ are uniquely defined by the harmonic function $U$ , e.g., through the scalar products

$$
\begin{array} { r c l } { { \displaystyle \langle \overline { { { Y } } } _ { \ell m 1 } ( \theta , \lambda ) , \Phi ( R _ { \oplus } , \theta , \lambda ) \rangle } } & { { = } } & { { \displaystyle 4 \pi \frac { G M } { R _ { \oplus } } \ \overline { { { C } } } _ { \ell m } } } \\ { { \displaystyle \langle \overline { { { Y } } } _ { \ell m 0 } ( \theta , \lambda ) , \Phi ( R _ { \oplus } , \theta , \lambda ) \rangle } } & { { = } } & { { \displaystyle 4 \pi \frac { G M } { R _ { \oplus } } \ \overline { { { S } } } _ { \ell m } } } \\ { { \displaystyle \langle \overline { { { Y } } } _ { \ell 0 1 } ( \theta ) , \Phi ( R _ { \oplus } , \theta , \lambda ) \rangle } } & { { = } } & { { \displaystyle 4 \pi \frac { G M } { R _ { \oplus } } \ \overline { { { C } } } _ { \ell 0 } . } } \end{array}
$$

For the computation of the normalized spherical harmonics $\overline { { Y } } _ { \ell m i }$ there are recursion formulae replacing those of the previous section. The reason for using them is that for $\ell$ large and $m$ also large the $L ^ { 2 }$ norm of the unnormalized harmonic $Y _ { \ell m i }$ grows to enormous values, producing computer overflows in the recursion formulae.11 Balmino et al. (1990) give an algorithm in Cartesian coordinates (thus free from the singularities at the poles) and using normalized harmonic functions and coefficients.

# Convergence

Is the expansion (13.15) convergent? The series expansion (13.18) is uniformly convergent on each sphere $| { \bf x } | = r$ for every $r > | \mathbf { p } |$ ; this follows from the properties of the Taylor series of the function $( 1 + z ) ^ { - 1 / 2 }$ (holomorphic for $| z | < 1$ ). The formula (13.18) is a power series in $1 / | \mathbf { x } |$ , the integral is a continuous operator, thus it is convergent for $| { \bf x } | > R$ provided the support $W$ of the mass density $\rho$ is contained in the open ball $| \mathbf { x } | < R$ .

A more subtle issue is what can be assumed about the convergence on the sphere $| \mathbf { x } | = R _ { \oplus }$ if the support $W$ touches it. If $\rho ( \mathbf { x } )$ is continuous, it is zero on the boundary of $W$ , thus the potential is harmonic on $| { \bf x } | \geq R _ { \oplus }$ . However, a solid planet could be modeled with a mass density jumping discontinuously to zero at the surface. The empirical Kaula rule was introduced to somewhat model this behavior (Kaula 1966, Chap. 5):

$$
\mathrm { R M S } ( \overline { { C } } _ { \ell m } ) = \mathrm { R M S } ( \overline { { S } } _ { \ell m } ) = K / \ell ^ { 2 }
$$

where the coefficients of degree $\ell$ are taken to be random variables with standard deviation proportional to a constant $K \simeq 1 0 ^ { - 5 }$ for the Earth, with other values for the other terrestrial planets (e.g., $K \simeq 1 0 ^ { - 4 }$ for the Moon). In this way the series of spherical harmonics is convergent on the sphere $| \mathbf { x } | = R _ { \oplus }$ in the $L ^ { 2 }$ norm, although only slowly, like the series $\sum ~ 1 / \ell ^ { 3 }$ .

# Completeness

The set of functions $\{ \overline { { Y } } _ { \ell m i } ( \theta , \lambda ) \}$ is a complete orthonormal sequence if it is a basis for the functional space of the harmonic functions on the sphere (Hobson 1931, p. 40–41). This requires that a function $g$ orthogonal to every element of the sequence is identically zero on the sphere:

$$
g , \overline { { Y } } _ { \ell m i } \rangle = \int _ { S } \ g ( \theta , \lambda ) \ \overline { { Y } } _ { \ell m i } ( \theta , \lambda ) \ d S = 0 \Longrightarrow g ( \theta , \lambda ) = 0 \ \mathrm { f o r ~ a l l } ~ \theta , \lambda .
$$

For a proof see (Hobson 1931, pp. 146–147) and (Albertella 1993, pp. 89– 91).

The question arises of what is the place in this context of the solutions of the Legendre equation (13.7), and of the similar equation (13.12), obtained by allowing the power series expansion (13.8) to be infinite. It can be shown (Hobson 1931, p. 12 and Chapter V) that these infinite series of powers of $\mu = \sin \theta$ are not convergent for $\mu$ in the closed $^ { 1 2 }$ interval $[ - 1 , 1 ]$ , thus their sums are not harmonic functions on any complete sphere $S ( r )$ .

A consequence of the convergence of the expansion and of the completeness of the basis $\{ \overline { { Y } } _ { \ell m i } \}$ is the solution of the exterior Dirichlet problem with a spherical boundary: given assigned values on the sphere $r = R$ , that is $\Phi ( R , \theta , \lambda ) = f ( \theta , \lambda )$ , where $f$ is continuous on the sphere, the function $\Phi$ , harmonic outside of the sphere, exists and is uniquely determined. The expansion of $\Phi$ in normalized spherical harmonics is uniquely determined by the integrals on the sphere $\langle \overline { { Y } } _ { \ell m k } ( \theta , \lambda ) , f ( \theta , \lambda ) \rangle$ , and then the sum of the series expansion such as eq. (13.29) is harmonic outside the sphere. It is unique because the difference of two such functions would have zero harmonic coefficients.

# 13.4 The gravity field along the orbit

We have expressed the gravity field as an expansion in spherical harmonics, functions of the satellite position $\mathbf { x }$ . We would like to find an expression for the gravitational potential, and derived quantities such as the gravity field and the gravity gradient experienced by the satellite as a function of time, assuming the satellite follows an unperturbed two-body orbit. To this purpose we shall consider the gravitational potential $U$ decomposed in harmonics

$$
U = \frac { G M } { r } + \sum _ { \ell = 2 } ^ { + \infty } \sum _ { m = 0 } ^ { \ell } U _ { \ell m } ,
$$

where $U _ { \ell m }$ is the component of degree $\ell$ and order $m$ .

# Equatorial orbit

We give an example to show that the potential can be expanded as a function of the orbital elements. Let us assume the satellite orbit is equatorial. The orbital elements are only $( a , e , \varpi , l _ { 0 } )$ , with $\varpi$ the angle between the inertial $x _ { 1 }$ axis and the direction of the pericenter, $l _ { 0 }$ the mean anomaly $l$ at epoch $t _ { 0 }$ . Moreover, let us assume the planet is rotating around the axis $x _ { 3 }$ with constant angular velocity $\Omega _ { \oplus }$ , with phase zero at $t = t _ { 0 }$ , thus the rotation phase is $\phi = \Omega _ { \oplus }$ $( t - t _ { 0 } )$ . Then

$$
\begin{array} { l c l } { { l } } & { { = } } & { { n \left( t - t _ { 0 } \right) + l _ { 0 } , \quad n = \sqrt { \displaystyle \frac { G M } { a ^ { 3 } } } } } \\ { { \lambda } } & { { = } } & { { v ( l ) + \varpi - \phi , \quad r = r ( l ) } } \end{array}
$$

where the functions $v ( l )$ (true anomaly) and $r ( l )$ have to be computed by solving the Kepler equation. Since $I = 0$ the latitude $\theta = 0$ and the harmonic of the potential $U _ { \ell m }$ of degree $\ell$ and order $m$ along the satellite orbit is

$$
U _ { \ell m } = \frac { G M \ R _ { \oplus } ^ { \ell } } { r ^ { \ell + 1 } } \ P _ { \ell m } ( 0 ) \ [ C _ { \ell m } \cos ( \psi _ { m } ) + S _ { \ell m } \sin ( \psi _ { m } ) ]
$$

where $\psi _ { m } = m ( v + \varpi - \phi )$ . If the orbit is also circular, then $v = l$ , $r = a$ , $\psi _ { m } = m [ \varpi + ( n - \Omega _ { \oplus } ) ( t - t _ { 0 } ) + l _ { 0 } ]$ , and the only frequency in the signal as a function of time is $m \left( n - \Omega _ { \oplus } \right)$ .

From this simple example we can already draw an interesting conclusion: for an equatorial circular orbit all the cosine harmonics with the same order $m$ have the same dependence upon time, the same result holds for the sine terms. Moreover, the $C _ { \ell m }$ and the $S _ { \ell m }$ terms have the same spectrum of frequencies.

The observations do not directly measure the potential, $^ { 1 3 }$ but many observables are obtained by either partial derivatives or time integrals from $U$ , e.g., the gravity gradient can be measured by a gradiometer, and these observables can also be represented as a sum of spherical harmonics.

If the orbit were to remain circular and planar, the simple model above would imply that there is an exact rank deficiency such that only $2 ( \ell _ { m a x } - 1 )$ harmonic coefficients could be determined among those of degree $2 \leq \ell \leq$ $\ell _ { m a x }$ . For example, the sectorial spherical harmonic coefficients $C _ { \ell \ell } , S _ { \ell \ell }$ could be solved, while all the others should be left among the consider parameters.

The orbit can remain neither circular nor planar because of the perturbations by the gravitational potential. However, the effects of the orbit perturbations on the perturbing potential are of second order in the small parameters $C _ { \ell m } , S _ { \ell m }$ and the above computations are correct to first order. Thus this model problem shows two important features of satellite geodesy: first, each spherical harmonic generates a signal in the observations with a characteristic frequency spectrum; second, there are spherical harmonics with different $\ell$ and $m$ giving highly correlated signals, resulting in either exact or at least approximate rank deficiency.

# Kaula expansion

For a general expansion of the gravitational potential as a Fourier series containing the orbital elements, we need to consider that in a reference system with the orbit plane as reference plane the expression of $U _ { \ell m }$ is given by eq. (13.31). Thus we only need to perform a rotation of coordinates, from a reference system defined by the planet’s equatorial plane and by some body-fixed direction in it to a reference system adapted to the Keplerian orbit (defined by the osculating orbital elements). The rotation from the $( x , y , z )$ equatorial reference system to the $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ reference system with $x ^ { \prime }$ axis along the direction of the pericenter and $z ^ { \prime }$ axis along the angular momentum direction $\hat { \mathbf { c } }$ is almost the same as used in Section 6.5, with the difference that the first rotation around the $z$ axis is by an angle $\alpha = \Omega - \phi$

$$
\left[ \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right] = R _ { \omega \hat { \mathbf { c } } } \ R _ { I \hat { \mathbf { N } } } \ R _ { \alpha \hat { \mathbf { z } } } \ \left[ \begin{array} { l } { x ^ { \prime } } \\ { y ^ { \prime } } \\ { z ^ { \prime } } \end{array} \right] = R ( \alpha , I , \omega ) \ \left[ \begin{array} { l } { x ^ { \prime } } \\ { y ^ { \prime } } \\ { z ^ { \prime } } \end{array} \right]
$$

where $\hat { N }$ is the current ascending node direction in the rotating equatorial plane; the angles $( \alpha , I , \omega )$ play the role of Euler angles.14 Thus the composite rotation $R ( \Omega , I , \omega )$ , when applied to the scalar field $U _ { \ell m }$ , transforms it into another function $U _ { \ell m } ^ { \prime }$ corresponding by value, that is $U _ { \ell m } ( x , y , z ) = U _ { \ell m } ^ { \prime } ( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ , which is equally harmonic because the Laplace operator is rotation invariant. The rotation leaves the radius $r$ invariant, thus it also preserves the decomposition of the harmonic function $U$ into homogeneous components of homogeneity degree $- \ell - 1$ , that is of harmonic degree $\ell$ . Thus the transformed $U _ { \ell m } ^ { \prime }$ can be expanded in spherical harmonics by using only spherical harmonics of degree $\ell$ and any order $k = 0 , \ldots , \ell$ . We use the expansion in the form of eq (13.16)

$$
U _ { \ell m } ^ { \prime } = \frac { G M R _ { \oplus } ^ { \ell } } { r ^ { \ell + 1 } } \sum _ { k = 0 } ^ { \ell } \left[ C _ { \ell k } ^ { \prime } Y _ { \ell k 1 } ( \theta ^ { \prime } , \lambda ^ { \prime } ) + S _ { \ell k } ^ { \prime } Y _ { \ell k 0 } ( \theta ^ { \prime } , \lambda ^ { \prime } ) \right]
$$

where the new coefficients $C _ { \ell k } ^ { \prime } , S _ { \ell k } ^ { \prime }$ are linear combinations of the old ones. In the simple case $I = 0 , \omega = 0$ we have $\theta = \theta ^ { \prime }$ and $\lambda = \lambda ^ { \prime } + \alpha$ , thus the new coefficients are obtained by

$$
\left[ \begin{array} { c c } { C _ { \ell m } ^ { \prime } } \\ { S _ { \ell m } ^ { \prime } } \end{array} \right] = \left[ \begin{array} { c c } { \cos ( m \alpha ) } & { - \sin ( m \alpha ) } \\ { \sin ( m \alpha ) } & { \cos ( m \alpha ) } \end{array} \right] \left[ \begin{array} { c c } { C _ { \ell m } } \\ { S _ { \ell m } } \end{array} \right]
$$

with $C _ { \ell k } ^ { \prime } = S _ { \ell k } ^ { \prime } = 0$ for $k \neq m$ . This results in an equation like (13.31).

The intermediate rotation around the ascending node axis has a more complicated effect, mixing the spherical harmonics with the same order and different degrees, thus it is expressed by a full $( 2 \ell + 1 ) \times ( 2 \ell + 1 )$ matrix with coefficients function of $I$ . There is a large literature on the computation of this matrix of conversion coefficients, with methods based either on spherical trigonometry (Kaula 1966, Chap. 3) or on the theory of group representations (Wigner 1959); they can be found in textbooks on quantum mechanics such as (Edmonds 1957) as well as in papers about geophysics (Sneeuw 1991, Jeffreys 1965). In the end, the component $U _ { \ell m } ^ { \prime }$ of the potential can be expanded with coefficients the inclination functions $F _ { \ell m p } ( I )$

$$
U _ { \ell m } = \frac { G M R _ { \oplus } ^ { \ell } } { r ^ { \ell + 1 } } \sum _ { p = 0 } ^ { \ell } F _ { \ell m p } ( I ) \left[ C _ { \ell m } \cos ( \psi _ { \ell m p } ) + S _ { \ell m } \cos ( \psi _ { \ell m p } ) \right]
$$

where the argument of the trigonometric function is

$$
\psi _ { \ell m p } = ( \ell - 2 p ) ( \omega + v ) + m ( \Omega - \phi ) - \frac { \pi } { 2 } [ ( \ell - m ) \bmod 2 ] ,
$$

the last term indicating that $C _ { \ell m } , S _ { \ell m }$ are replaced by $- S _ { \ell m } , C _ { \ell , m }$ when $\ell - m$ is odd. The inclination functions can be expressed as a trigonometric polynomial in $\sin I$ and $\cos I$ (Kaula 1966, eq. (3.62), p. 34)

$$
\begin{array} { r c l } { { { \cal F } _ { \ell m p } ( I ) } } & { { = } } & { { \displaystyle \sum _ { t = 0 } ^ { m i n ( p , k ) } \frac { ( 2 \ell - 2 t ) ! } { t ! ( \ell - t ) ! ( \ell - m - 2 t ) ! 2 ^ { 2 \ell - 2 t } } \sin ^ { \ell - m - 2 t } I } } \\ { { } } & { { } } & { { \displaystyle \times \sum _ { s = 0 } ^ { m } \binom { m } { s } \cos ^ { s } I \sum _ { c } { \binom { \ell - m - 2 t + s } { c } \binom { m - s } { p - t - c } ( - 1 ) ^ { c } } \cos ^ { s } I , } } \end{array}
$$

where $k$ is the integer part of $( \ell - m ) / 2$ and $c$ is summed over values making the binomial coefficients non-zero, that is with the lower index non-negative and not larger than the upper one. The inclination functions $F _ { \ell m p } ( I )$ with the indexes up to four are given by Kaula (1966, Table 1, pag. 34–35)15.

The formula above, called the Kaula expansion, can be practically used, with some caution in the computation of the binomial coefficients, even for comparatively large $\ell , m$ . However, for near polar orbits, it is more convenient to use a formula based upon modified Jacobi polynomials introduced by Kinoshita et al. (1974); it contains only powers of $\cos I$ and therefore can be truncated for an approximate expansion near $I = 9 0 ^ { \circ }$ . This formula has been converted to Kaula notation by Milani and Kneˇzevi´c (1995). For $k = \ell - 2 p > 0$ the terms up to order 2 in $\cos I$ are

$$
F _ { \ell m p } ( I ) = \sum _ { r = m a x ( 0 , k - m ) } ^ { m i n ( \ell - m , \ell + k ) } ( - 1 ) ^ { t } \frac { ( 2 \ell - 2 p - 1 ) ! ! ( \ell + m ) ! ( \ell - k ) ! } { 2 ^ { \ell + p } p ! ( m - k + r ) ! ( \ell + k - r ) ! r ! ( \ell - m - k + r ) ! } ,
$$

$$
\times \bigg \{ 1 + ( \ell - m - 2 r + k ) \cos I + \bigg [ k ( \ell - m - 2 r ) - r ( \ell - m - r )
$$

$$
+ \left. \frac { k ^ { 2 } - m + r ( r - 1 ) + ( \ell - m - r ) ( \ell - m - r - 1 ) } { 2 } \right] \cos ^ { 2 } I \Biggr \}
$$

where $t$ is the integer part of $( \ell - m + 1 + 2 r ) / 2$ . For $\ell - 2 p < 0$ we set $k = 2 p - \ell$ and use

$$
\begin{array} { r l r } { , ( I ) } & { = } & { \displaystyle \sum _ { r = m a x ( 0 , k - m ) } ^ { m i n ( l - m , l + k ) } ( - 1 ) ^ { t } \frac { ( 2 l - 2 p - 1 ) ! ! ( l + m ) ! ( l + k ) ! } { 2 ^ { l + p } p ! ( m - k + r ) ! ( l + k - r ) ! r ! ( l - m - r } } \\ & { } & { \times \bigg \{ 1 - ( l - m - 2 r + k ) \cos I + \Big [ k ( l - m - 2 r ) - r ( l - m - 1 ) \Big ] } \\ & { } & { + \ \frac { k ^ { 2 } - m + r ( r - 1 ) + ( l - m - r ) ( l - m - r - 1 ) } { 2 } \bigg ] \cos ^ { 2 } I \bigg \} } \end{array}
$$

where $t$ is the integer part of $( 3 l - 3 m + 1 + 2 r ) / 2$ .

When the expansions of the two-body problem are substituted in these expressions (in particular the expansion in powers of the eccentricity $e$ ), the dependence upon $e$ is contained in eccentricity functions $G _ { \ell p q } ( e )$ and new arguments appear:

$$
\ell m = \frac { G M R _ { \oplus } ^ { \ell } } { a ^ { \ell + 1 } } \sum _ { p = 0 } ^ { \ell } F _ { \ell m p } ( I ) \sum _ { q = - \infty } ^ { + \infty } G _ { \ell p q } ( e ) \left[ C _ { \ell m } \cos ( \psi _ { \ell m p q } ) + S _ { \ell m } \cos ( \psi _ { \ell m p q } ) \right] ,
$$

where the argument of the trigonometric function

$$
\psi _ { \ell m p q } = ( \ell - 2 p ) \omega + ( \ell - 2 p + q ) l + m ( \Omega - \phi ) - \frac { \pi } { 2 } m o d ( \ell - m , 2 )
$$

contains the mean anomaly $l$ rather than the true anomaly. The eccentricity functions $G _ { \ell p q } ( e )$ are analytic in $e$ and the lowest order term contains $e ^ { q }$ . Their explicit computation is not simple; for the lowest order terms in the eccentricity functions with pq up to 442 see (Kaula 1966, Table 2, p. 38).

# 13.5 Frequency analysis, ground track, and resonance

The most immediate consequence of the Kaula expansions for the geopotential perturbing function of the previous section is the possibility of listing all the frequencies which will appear in the first-order perturbations. By taking the time derivative of eq. (13.36)

$$
\frac { d \psi _ { \ell m p q } } { d t } = ( \ell - 2 p + q ) n - m \dot { \phi } + \left[ \left( \ell - 2 p \right) \dot { \omega } + m \dot { \Omega } \right] = \nu _ { l m p q }
$$

where the dot stands for time derivative, and $n$ is the mean motion. In a two-body approximation this is just a combination with integer coefficients of two constant frequencies, $n$ and $\Omega _ { \oplus }$ . In a better approximation, the slow frequencies of precession of the elements $\omega , \Omega$ , resulting from the zonal harmonics, also appear in the term between square brackets, thus in the frequency spectrum. The Kaula expansion allows us to compute this effect by averaging over the mean anomaly, that is by selecting the secular terms not containing it, with $\ell - 2 p + q = 0$ . For the simple case $e = 0$ , or anyway to order zero in $e$ : if $\ell = 2 p$ , that is for even order zonal harmonics,

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } U _ { \ell 0 } d l = \frac { G M R _ { \oplus } ^ { \ell } } { a ^ { \ell + 1 } } F _ { \ell 0 p } ( I ) C _ { \ell 0 } .
$$

The secular perturbation, that is the one generated by the secular terms, can be computed by the Lagrange perturbative equations, providing the perturbations in the elements to first-order in the small parameters, such as $C _ { \ell 0 }$ . For the longitude of the node the Lagrange equation is

$$
\frac { d \Omega } { d t } = \frac { 1 } { n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } \sin I } \frac { \partial R } { \partial I } ,
$$

where $R$ is the perturbing function, i.e., the potential $U$ without the monopole term. The secular perturbations on $\Omega$ result into a uniform precession with frequency

$$
\overline { { { \frac { d \Omega } { d t } } } } = G M \ R _ { \oplus } ^ { \ell } n a ^ { 3 } \ \sin I \sum _ { p = 0 } ^ { + \infty } \ \frac { R _ { \oplus } ^ { \ell } } { a ^ { \ell } } \ F _ { 2 p \ 0 p } ^ { \prime } ( I ) \ C _ { 2 p 0 } \ \left[ 1 + \mathcal { O } ( e ^ { 2 } ) \right] .
$$

If we use this secular value as $\dot { \Omega }$ in eq. (13.37) with $q = 0$ (for very low eccentricity), and also approximate $\dot { \omega }$ with a constant value (by a similar computation of the secular perturbation), for $q = 0$ the frequencies in the potential as a function of time, along the unperturbed two-body orbit, are

$$
\nu _ { \ell m p 0 } = ( \ell - 2 p ) ( n + \dot { \omega } ) + m ( \dot { \Omega } - \dot { \Omega } _ { \oplus } ) ,
$$

all integer combinations of two basic frequencies, although these are somewhat different from the two-body ones. The Lagrange equations contain only partials of the perturbing potential, thus the first-order perturbations can be obtained by the term-wise integration of a two-frequency Fourier series.

# Resonance

Let us suppose the orbit of the satellite is exactly resonant with the rotation of the Earth, that is there are two integers $j , k$ such that

$$
{ \frac { n + \dot { \omega } } { j } } = { \frac { \dot { \Omega } _ { \oplus } - \dot { \Omega } } { k } } = \nu .
$$

![](images/4bf3231b5b0c45cf42d6562086c21fa26e15d4c50dda61053eb63eac0ec63d57.jpg)  
Fig. 13.1. The ground track of a circular orbit with $I = 6 0 ^ { \circ }$ and in a resonance $j / k = 1 4 / 1$

In the two-body approximation, the period of the satellite would be exactly $k / j$ sidereal days. Neglecting the $q \neq 0$ terms, the frequencies in the time series are multiples of the basic frequency $\nu$

$$
\nu _ { \ell m p 0 } = \left[ \left( \ell - 2 p \right) j - m k \right] \nu .
$$

Thus the signal from all harmonics is periodic of period $2 \pi / \nu$ and can be described as a Fourier series with arguments a multiple of $\nu t$ . In a reference frame rotating with the Earth, the orbit is periodic and the ground track, the vertical projection of the orbit on a sphere of radius $R _ { \oplus }$ , returns on the same curve with a repeat cycle of $j$ days (Figure 13.1).

The geometric properties of the periodic orbits are reflected in the analytical form of the first-order perturbations: if in eq. (13.40) the integer inside the square brackets is zero, there is a zero frequency in the perturbative equations and thus enhanced perturbations on some of the elements. For example, for the geosynchronous satellites $j = k = 1$ , at order $\ell = 2$ there are zero frequencies for $p = 0 , m = 2$ with coefficients containing $C _ { 2 2 }$ , $S _ { 2 2 }$ and for $p = 1 , m = 0$ with $C _ { 2 0 }$ . In such cases the first-order solution obtained by simple quadrature is not a good approximation, and a different method needs to be used to identify the first approximation to be used, in the form of a pendulum-like equation (Kaula 1966, Section 3.6).

# NON-GRAVITATIONAL PERTURBATIONS

The non-gravitational perturbations arise because outer space is not empty. First, planetary atmospheres extend to large altitudes, where they can be thin enough to allow for a satellite orbit but still generate a significant aerodynamic drag, given the high relative velocity of the spacecraft. As will be discussed in Chapter 16, there is interest in satellites orbiting as low as possible to determine high-order harmonics of the planetary gravity field. This may require propulsion to compensate for orbital decay and/or the use of on-board accelerometers to measure the amount of drag; that is, non-gravitational perturbations are critical in the design phase of the mission.

Second, outer space is pervaded by electromagnetic radiation: the light arriving directly from the Sun, reflected by the Earth, and by the other planets. The photons exchange momentum with spacecraft when they are absorbed and reflected; spacecraft themselves emit infrared radiation and electromagnetic waves carrying away some momentum. The resulting accelerations are small, but at the level of accuracy of current tracking systems they are not negligible, hence the need to model and/or measure them. Even small natural bodies, such as asteroids with diameters in the km range, have orbits affected by non-gravitational perturbations in a measurable way.

This chapter cannot be a full revision of the textbook by Milani et al. (1987), which should take into account all the new results accumulated in more than 20 years since its publication. It is just an update on the issues raised by non-gravitational perturbations in the orbit determination problem, taking into account state-of-the-art instrumentation. The conclusions, which will result from the orders of magnitudes and from an understanding of the complexity of the problem, will be the following: to model the nongravitational perturbations is possible but they are anyway the main limitation to the accuracy of the orbit determination. For spacecraft, to measure non-gravitational accelerations directly with on-board instrumentation (see Section 16.1) allows for a much higher performance. The orbits of especially well observed asteroids, including some targets of space missions, may require special effort in non-gravitational force modeling.

# 14.1 Direct radiation pressure

Outer space is everywhere full of radiation, from different sources. We shall consider for now radiation, mostly visible light, coming from a single source, the Sun; we approximate the illumination from the Sun as if it were a point source. The photons of light carry energy and linear momentum: if the energy flux is measured by the intensity $\Phi _ { \odot }$ , the flux of momentum per unit cross-sectional area is $\Phi _ { \odot } / c$ , with $c$ the speed of light. The total transfer of linear momentum upon impact of the photons from the Sun on the spacecraft surface generates the direct radiation pressure.

# Interaction of radiation with the surface

To model what happens to the momentum carried by the radiation impacting the skin of the spacecraft, we can use a combination of three standard physical models: absorption, in which the photons are gobbled up by the spacecraft (acting as a black body), reflection, in which the photons bounce on a smooth surface following the laws of mirror reflection, and diffusion in which the photons are re-emitted with intensity following Lambert’s law, that is proportionally to the cosine of the angle $\theta$ from the normal to the surface. The mix of these three phenomena is controlled by three positive constants $\alpha , \rho , \delta$ (Milani et al. 1987, Chapter 4), with

$$
\alpha + \rho + \delta = 1
$$

expressing the fraction of the incident light that behaves according to the absorption, reflection, and diffusion law, respectively.

Under these hypotheses, the force applied by radiation pressure on an outer surface element $d S$ of the spacecraft is directed in part along the normal $\hat { \bf n }$ to the surface, in part along the direction to the Sun $\hat { \bf s }$ . The crosssectional area of the surface element with respect to the radiation flux is $\cos { \beta d S }$ where $\cos { \beta } = \hat { \bf s } \cdot \hat { \bf n }$ . For the surface to be illuminated, $\cos \beta > 0$ is necessary; the same condition is also sufficient if the shape is convex, otherwise there could be mutual shadowing between different parts.

The momentum of the absorbed photons is transferred to the spacecraft, thus the force acting on a surface element due to the absorption is

$$
d \mathbf { F } _ { \alpha } = - \ { \frac { \Phi _ { \odot } } { c } } \alpha \cos \beta \hat { \mathbf { s } } d S .
$$

The reflected photons transfer to the spacecraft the momentum they had upon arrival and the recoil momentum: the sum is directed along $\hat { \bf n }$

$$
d \mathbf { F } _ { \rho } = - \ \frac { \Phi _ { \odot } } { c } \ 2 \rho \cos ^ { 2 } \beta \hat { \mathbf { n } } d S .
$$

The photons of the fraction diffused are first absorbed, giving a force in the $- \hat { \mathbf { s } }$ direction equal to that of the absorption. Then they are re-emitted in different directions: for symmetry reasons, the resultant force is directed opposite to the surface normal $\hat { \bf n }$ , and its intensity contains the integrals

$$
{ \frac { \int _ { 0 } ^ { 2 \pi } d \lambda \int _ { 0 } ^ { \pi / 2 } \cos ^ { 2 } \theta \sin \theta d \theta } { \int _ { 0 } ^ { 2 \pi } d \lambda \int _ { 0 } ^ { \pi / 2 } \cos \theta \sin \theta d \theta } } = { \frac { 2 } { 3 } } ,
$$

thus the total force is

$$
d \mathbf { F } _ { \delta } = - \ \frac { \Phi _ { \odot } } { c } \ \delta \ \cos \beta \left[ \hat { \mathbf { s } } + \frac { 2 } { 3 } \hat { \mathbf { n } } \right] \ d S .
$$

The effect on the spacecraft orbit is due to the resultant of the forces on all the surface elements: if $S _ { I }$ is the portion of the outer surface illuminated by the Sun,

$$
\mathbf { F } = - \ { \frac { \Phi _ { \odot } } { c } } \ \int _ { S _ { I } } \ \left[ \left( 1 - \rho \right) \cos \beta { \hat { \mathbf { s } } } + \left( { \frac { 2 } { 3 } } \delta + 2 \rho \cos \beta \right) \cos \beta { \hat { \mathbf { n } } } \right] \ d S ,
$$

where we have used (14.1), is the radiation pressure force acting on the spacecraft. Note that, unless the shape has some special symmetry, it is by no means guaranteed that the resultant force is applied at the center of mass of the spacecraft, thus radiation pressure will also affect the spacecraft rotation state, also called the attitude.

For some simple shapes the integral (14.2) can be computed analytically, e.g., for a sphere with constant $\alpha , \rho , \delta$ the radiation pressure force is

$$
\mathbf { F } = - \ { \frac { \Phi _ { \odot } \mathcal { A } } { c } } { \hat { \mathbf { s } } }
$$

where the effective cross-section $\mathcal { A }$ is (Milani et al. 1987, p. 74–75)

$$
{ \mathcal { A } } = \left( \alpha + \rho + \frac { 1 3 } { 9 } \delta \right) \pi R ^ { 2 } = \left( 1 + \frac { 4 } { 9 } \delta \right) \pi R ^ { 2 } ,
$$

that is the geometric cross-sectional area times a coefficient depending upon $\delta$ . For this the name “reflectivity coefficient” and the symbol $C _ { R }$ are used, but this is not logical, taking into account that this coefficient is always $> 1$ .

The same formula (14.3) applies for a flat panel oriented orthogonally to $\hat { \bf s }$ , such as an optimally oriented solar array. For example, for $A = 1 6 ~ \mathrm { m ^ { 2 } }$ of solar panels, with large $\alpha \ge 0 . 8$ (thus $1 + 4 / 9 \delta \simeq 1$ and $A \simeq A$ ) and a total mass of the spacecraft $M = 5 0 0 ~ \mathrm { k g }$ , the area-to-mass ratio is $A / M = 0 . 3 2$ , the radiation pressure acceleration at 1 AU from the Sun, where $\Phi _ { \odot } \simeq 1 . 3 8$ $\mathrm { k W / m ^ { 2 } }$ , is directed along $- \hat { \mathbf { s } }$ with an intensity $\simeq 1 . 5 \times 1 0 ^ { - 5 } ~ \mathrm { c m / s ^ { 2 } }$ . For a spacecraft with a comparatively simple shape, say a box shaped bus with $\simeq 4 ~ \mathrm { m ^ { 2 } }$ faces, the radiation pressure acceleration has a variable component smaller in size by a factor of 3 or 4, depending upon the bus attitude and surface properties.

For a realistic spacecraft model the radiation pressure force is a complicated function of the illumination direction ˆs and of the spacecraft attitude. To compute it explicitly we need to know the exact shape, the attitude (including the state of the moving parts), and the three optical coefficients $\alpha , \rho , \delta$ for each portion of the surface. For a spacecraft with a complex shape this can be difficult, unless special care is taken in the design phase in using a simple shape, surfaces with well known properties, and a simple operation mode. An additional difficulty is due to the fact that the optical coefficients $\alpha , \rho , \delta$ change with time, as an effect of degradation of the spacecraft surface layers, damaged by charged particles from the Sun, and the magnetosphere of the relevant planet. Within a few years a white paint becomes brown and a mirror surface becomes irregular at a scale comparable to the wavelength of visible light; thus $\delta$ and $\rho$ decrease, $\alpha$ increases.

For a natural body such as an asteroid, the a priori knowledge of both the optical properties and the shape of the surface is very poor (also the mass is poorly known). On the other hand, given the known shape of some real asteroids, to approximate their surface with a sphere in most cases is not a good approximation. However, if the purpose is not real-time orbit determination, but rather processing in batch at or near the end of an asteroid orbiter mission, the data from the entire mission can be used to build a direct radiation pressure model for the asteroid which could have a relative accuracy comparable to that of a spacecraft.

# Secular perturbations

The relevance of radiation pressure as a source of perturbations on the orbit of both spacecraft and asteroid depends upon the way it accumulates with

time. We shall use a model problem to develop the tools to discuss the orbital effects of small perturbations, such as the non-gravitational ones.

The model is just a two-body problem, with a satellite of mass $M$ at $\vec { x }$ perturbed by a small force $\epsilon \mathbf { F } ( t )$ , where $\epsilon$ is a small parameter and $r = | \mathbf { x } |$ is the distance from the central body of mass $M _ { \oplus }$ :

$$
\frac { d ^ { 2 } { \bf x } } { d t ^ { 2 } } = - \frac { G M _ { \oplus } } { r ^ { 3 } } { \bf x } + \epsilon { \bf F } / M .
$$

In a mobile reference system defined by the orbit plane, orthogonal to the angular momentum vector $\mathbf { c } = \mathbf { x } \times d \mathbf { x } / d t$ , we have

$$
{ \hat { \mathbf { r } } } = { \frac { \mathbf { x } } { r } } , \quad { \hat { \mathbf { w } } } = { \frac { \mathbf { c } } { | \mathbf { c } | } } , \quad { \hat { \mathbf { t } } } = { \hat { \mathbf { w } } } \times { \hat { \mathbf { r } } }
$$

and the components of the non-gravitational acceleration are

$$
R = \epsilon { \bf F } \cdot \hat { \bf r } / M , T = \epsilon { \bf F } \cdot \hat { \bf t } / M , W = \epsilon { \bf F } \cdot \hat { \bf w } / M
$$

for the radial, transversal, and out of plane component, respectively. The total energy (per unit mass) $E$ of the two-body approximation has a time derivative equal to the power of the perturbing force

$$
\frac { d E } { d t } = \frac { \epsilon { \bf F } } { M } \cdot \frac { d { \bf x } } { d t } = R v _ { R } + T v _ { T } .
$$

By the two-body formulae (similar to those of Section 4.2) the velocity components $v _ { R }$ and $v _ { T }$ (along the $\hat { \mathbf { r } }$ and $\hat { \mathbf { t } }$ directions, respectively) are

$$
{ v _ { T } } = \frac { d \mathbf { x } } { d t } \cdot \hat { \mathbf { r } } = \frac { | \mathbf { c } | } { r } = \frac { G M _ { \oplus } } { | \mathbf { c } | } \left( 1 + e \cos v \right) , ~ { v _ { R } } = \frac { d \mathbf { x } } { d t } \cdot \hat { \mathbf { t } } = \frac { G M _ { \oplus } } { | \mathbf { c } | } ~ e \sin v
$$

with $| \mathbf { c } |$ the scalar angular momentum. This allows us to conclude how the orbital energy changes:

$$
{ \frac { d E } { d t } } = { \frac { G M _ { \oplus } } { | \mathbf { c } | } } \ [ T + e ( R \sin v + T \cos v ) ]
$$

and, by the relationship between energy and semimajor axis,

$$
{ \frac { d E } { d t } } = { \frac { G M _ { \oplus } } { 2 a ^ { 2 } } } { \frac { d a } { d t } } \Longrightarrow { \frac { d a } { d t } } = { \frac { 2 } { n \sqrt { 1 - e ^ { 2 } } } } \left[ T + e \left( R \sin v + T \cos v \right) \right] .
$$

The main term for a low eccentricity orbit is

$$
\frac { d a } { d t } = \frac { 2 } { n } T + \mathcal { O } ( e ) \Longrightarrow \frac { d n } { d t } = - \frac { 3 } { a } T + \mathcal { O } ( e ) .
$$

The main conceptual step in a perturbative approach is just to expand the solution to the complete equation of motion in a Taylor series with respect to the small parameter $\epsilon$ . For example, $a ( t ) = a _ { 0 } ( t ) + \epsilon a _ { 1 } ( t ) + \epsilon ^ { 2 } a _ { 2 } ( t ) + \cdot \cdot \cdot$ and the same expansion applies to the other five orbital elements. Then equations such as (14.4) can also be expanded in powers of $\epsilon$ and, by equating the terms of the same order in $\epsilon$ on both sides, we get $a _ { 0 }$ constant and $\epsilon d a _ { 1 } / d t = 2 T ^ { ( 0 ) } / n _ { 0 } + { \mathcal O } ( e )$ , where $T ^ { ( 0 ) }$ is $T$ evaluated on the unperturbed orbit. That is, eq. (14.4) can be reinterpreted as a first perturbative order equation, providing the $\mathcal { O } ( \epsilon )$ terms in the solution for $a ( t )$ , when the righthand side is computed at the unperturbed orbit.

The corresponding along-track effect can be computed by using a set of orbital elements non-singular for $e = 0$ (Milani et al. 1987, Section 3.3), e.g., $\lambda = \omega + \ell$ for $e > 0$ , where $\ell$ is the mean anomaly, while for $e = 0$ the element $\lambda$ is just the angle on the circular orbit with origin at the ascending node.1 Then the equations for the perturbed motion are

$$
\frac { d \lambda } { d t } = n + \mathcal { O } ( \epsilon ) , ~ a ~ \frac { d ^ { 2 } \lambda } { d t ^ { 2 } } = - 3 ~ T + \mathcal { O } ( e ) + \mathcal { P } \mathcal { O } ( \epsilon ) + \mathcal { O } ( \epsilon ^ { 2 } )
$$

where $\mathcal { P }$ contains terms arising from the integration of $d \lambda / d t - n$ . The non-trivial part of the above computation is to show that $_ { \mathcal { P } }$ contains only periodic terms with zero average. This implies that the effect of the $R$ and $W$ components does not accumulate quadratically with time in the along-track direction, at least not to order 1 in $\epsilon$ . A similar argument shows that there is no orbital effect accumulating quadratically with time in the other directions $\hat { \mathbf { r } } , \hat { \mathbf { w } }$ . Thus for a nearly circular orbit the acceleration along-track is, to a good approximation, $^ { - 3 }$ times the perturbative transversal acceleration. If the transversal component $T$ , as a function of time, can be decomposed into an average, or secular, part $T$ and a short periodic part averaging out over one two-body orbital period $P = 2 \pi / n$ , starting from $t = t _ { 0 }$ ,

$$
T ( t ) = \overline { { T } } + T _ { s p } ( t ) , \quad \overline { { T } } = \frac { 1 } { P } \int _ { t _ { 0 } } ^ { t _ { 0 } + P } T ( t ) d t
$$

then the perturbation in the semimajor axis also decomposes into a secular perturbation, with linear growth in $t$ , a short periodic perturbation averaging out over one period, and terms of higher order in $\epsilon$

$$
a ( t ) = a _ { 0 } + \frac { 2 \overline { { T } } } { n _ { 0 } } t + \frac { 2 } { n _ { 0 } } \int _ { 0 } ^ { t } T _ { s p } ( s ) d s + \mathcal { O } ( e ) + \mathcal { O } ( \epsilon ^ { 2 } )
$$

where $a _ { 0 } = a ( 0 )$ and $n _ { 0 } = n ( a _ { 0 } )$ . The accumulated along-track effect is obtained by combining eqs. (14.5) and (14.6)

$$
a ( t ) \left( \lambda ( t ) - \lambda _ { 0 } + n _ { 0 } t \right) = - \frac { 3 \overline { { T } } } { 2 } t ^ { 2 } + \mathcal { P } _ { 1 } \mathcal { O } ( \epsilon ) + \mathcal { O } ( e ) + \mathcal { O } ( \epsilon ^ { 2 } ) ,
$$

1 The variable defined in this way can be shown to be differentiable even for $e = 0$ where $\mathcal { P } _ { 1 }$ , arising from the integral of $\mathcal { P }$ and the double integral of $T _ { s p } / \epsilon$ , contains only periodic terms. In conclusion, for an orbit which is initially nearly circular, the only source of along-track effects quadratic in time is the averaged transversal acceleration $\overline { T }$ , with the same coefficient $^ { - 3 }$ as the instantaneous transversal acceleration (14.5).

The above result has deep implications on the relevance of nongravitational perturbations. For many sources of non-gravitational perturbations it is indeed the case that $\overline { T }$ is zero; e.g., if the orbit is circular and $\mathbf { F }$ is constant in time, $T ( \lambda )$ , when the unperturbed $\lambda = n _ { 0 } t + \lambda _ { 0 }$ is substituted, is a trigonometric function of time, averaging to zero.

We have outlined the argument to order zero in eccentricity, but in fact similar results can be proven to an arbitrary order. For example, let us assume that the vector $\mathbf { F }$ is constant in time, or even dependent upon the position s of the Sun, which in turn changes with time with frequencies much slower than $n$ , assuming that the satellite-to-Sun vector can be approximated by the Earth-to-Sun vector. Then, as shown by Anselmo et al. (1983a) and Milani et al. (1987, Section 4.2), there is no secular perturbation in the semimajor axis, to first order in the $\epsilon$ and to all orders in $e$ .

The same result applies also to many gravitational perturbations. For example, the gravitational perturbations from the Sun and from the other planets $2$ have a zero $\overline { T }$ , thus there is no secular perturbation in the semimajor axis to order one in the small parameters (which are those described in Section 4.5). This is a straightforward generalization of a classical result, going back to Lagrange. A simple comparison of the perturbative accelerations due to different causes (see Section 15.3) can be useful to discard from the dynamical model some exceedingly small effects. However, to decide which are the main effects we need to compute the secular along-track acceleration $\overline { T }$ .

The above discussion assumes that the radiation pressure has a constant direction and intensity, or at least varying with a period much longer than the orbital period, e.g., a period of one year for an Earth satellite. If the area-to-mass ratio and the optical properties are not changing with time, this is enough to avoid quadratic accumulations with time of the perturbation on the orbit. On the contrary, if the radiation pressure acceleration undergoes changes with frequency equal to the orbital period, this does result in quadratic effects. Two examples of this are as follows: an Earth satellite with a constant attitude and an Earth pointing antenna may experience secular perturbations in the semimajor axis due to the antenna, not to the body (Anselmo et al. 1983a); an asteroid orbiting the Sun with a rotation axis not orthogonal to the orbit plane experiences a secular perturbation in the semimajor axis if the two hemispheres “north” and “south” have either a different shape or different optical properties (Vokrouhlick´y and Milani 2000).

The orbital elements $e , \omega$ can experience secular perturbations due to radiation pressure (Milani et al. 1987, Section 4.3): they appear as long periodic perturbations, with periods $\geq 1$ year for an Earth satellite. For the elements $I , \Omega$ , if the radiation pressure $\mathbf { F }$ is constant the first-order secular effects are zero for $e = 0$ . Anyway the perturbations on the elements $e , \omega , I , \Omega$ result in changes in the spacecraft position with the orbital period. In conclusion, if $\overline { { T } } = 0$ , the effects on the spacecraft position do not accumulate quadratically with time, thus they are in general a minor problem for the accurate orbit determination used both in satellite geodesy and in the control of active spacecraft. However, for large $A / M$ space debris a long-term growth of eccentricity and inclination takes place: $e , I$ can reach high values and this is a major problem, because it may result in a large relative velocity with respect to active satellites in the same region, especially in the geosynchronous belt (Valk et al. 2007).

# 14.2 Thermal emission

A passive celestial body exposed to solar radiation $\Phi _ { \odot } A$ , where $A$ is the cross-sectional area, transforms the absorbed fraction $\alpha \Phi _ { \odot } A$ into heat and reaches some thermal state. The surface temperature is not uniform and changes with time as a result of both the rotation and the orbital motion. Thus the entire surface re-emits thermal radiation anisotropically, carrying away some net linear momentum. This phenomenon of thermal emission results in a perturbative acceleration, affecting the orbit.

For each surface element $d S$ the energy output due to thermal radiation is $\epsilon \sigma T ^ { 4 } d S$ , where $\boldsymbol { \tau }$ is the surface temperature, $\sigma = 5 . 6 7 \times 1 0 ^ { - 5 } \ \mathrm { e r g / c m ^ { 2 } s K }$ is the Stephan–Boltzmann constant, and $\epsilon$ is the emissivity coefficient ( $\epsilon = 1$ for a black body). The thermal radiation is diffused according to Lambert’s law, thus the flow of linear momentum results in a force

$$
d \mathbf { F } _ { \epsilon } = - \ \frac { 2 \epsilon \sigma T ^ { 4 } } { 3 c } \hat { \mathbf { n } } d S .
$$

To model the surface temperature distribution and to compute the integral of $d \mathbf { F } _ { \epsilon }$ is not simple: a full analytical solution exists only under very simple conditions. We shall briefly outline one such analytical solution, under the hypothesis that the surface is spherical, with radius $R$ , and that the body rotates uniformly around a constant axis, which we use as the $\hat { \mathbf { z } }$ axis of the reference frame; let $( r , \theta , \lambda )$ be polar coordinates in that frame. We further assume that the vector to the Sun $\mathbf { s }$ is constant (an approximation applicable over a time span short with respect to the period of the heliocentric motion) and that the surface temperature differences are small with respect to the average temperature, allowing us to linearize the heat equation (Milani et al. 1987, Section 5.2).

The heat equation for a stationary state reduces to the Laplace equation $\Delta T = 0$ . Thus, assuming that the rotation is fast enough to average out the temperature as a function of $\lambda$ , the temperature $\boldsymbol { \tau }$ of the body should reach an equilibrium state expressed by zonal spherical harmonics

$$
T ( r , \theta ) = \mathcal { T } _ { 0 } + \sum _ { i = 1 } ^ { + \infty } \mathcal { T } _ { i } \left( \frac { r } { R } \right) ^ { i } P _ { i } ( \sin \theta ) ,
$$

with $T _ { 0 }$ the average surface temperature, $\tau _ { i }$ constants, and $P _ { i }$ the Legendre polynomials of (13.10). As a boundary condition, we have the balance between the outward heat flow caused by thermal conduction $- \chi \partial T / \partial r$ (where $\chi$ is the thermal conductivity of the body, assumed to be constant) and the net emission at the surface (the difference between the external irradiation from the Sun and the emission)

$$
\epsilon \sigma T ^ { 4 } - \alpha \overline { { \hat { \mathbf { n } } \cdot \hat { \mathbf { s } } } } \Phi _ { \odot } = - \chi \frac { \partial T } { \partial r }
$$

where the over-line indicates the average over $\lambda$

$$
{ \overline { { { \hat { \mathbf { n } } } \cdot { \hat { \mathbf { s } } } } } } = { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } g ( { \hat { \mathbf { n } } } \cdot { \hat { \mathbf { s } } } ) d \lambda = s ( \theta )
$$

with the function $g$ equal to its argument if it is positive, zero otherwise (thus restricting the integral to the illuminated hemisphere). The function $s ( \theta )$ can be computed analytically: if the latitude and longitude of the Sun are $( \xi , \pi / 2 )$ we get three formulae for the three latitude zones, the midnight Sun, the dark noon, and the sunrise–sunset zones, respectively

$$
s ( \theta ) = \left\{ \begin{array} { l l } { \sin \xi \sin \theta } & { \mathrm { f o r ~ } \frac { \pi } { 2 } - \xi \le \theta } \\ { 0 } & { \mathrm { f o r } \theta \le \xi - \frac { \pi } { 2 } } \\ { \frac { 1 } { 2 \pi } \left[ 2 \cos \xi \cos \theta \cos \lambda _ { 1 } + \left( \sin \xi \sin \theta \right) \left( \pi - 2 \lambda _ { 1 } \right) \right] } \\ { \quad \mathrm { f o r ~ } \xi - \frac { \pi } { 2 } \le \theta \le \frac { \pi } { 2 } - \xi } \end{array} \right.
$$

where $\lambda _ { 1 }$ solves the terminator plane equation $\hat { \mathbf { n } } \cdot \hat { \mathbf { s } } = 0$ , that is $\cos \lambda _ { 1 } =$

$\tan \theta \tan \xi$ . With $s ( \theta )$ expanded in Legendre polynomials

$$
s ( \theta ) = s _ { 0 } + \sum _ { i = 1 } ^ { + \infty } s _ { i } P _ { i } ( \sin \theta )
$$

equation (14.9), linearizing in the temperature harmonic coefficients $\tau _ { i }$ (assumed $\ll ~ T _ { 0 }$ ), gives a separate equation for each zonal harmonic coefficient

$$
\epsilon \sigma T _ { 0 } ^ { 4 } = \alpha s _ { 0 } \Phi _ { \odot } , ~ T _ { i } = \frac { \alpha s _ { i } \Phi _ { \odot } } { 4 \epsilon \sigma T _ { 0 } ^ { 3 } + i \chi / R } ,
$$

with the solutions of lowest degree: $s _ { 0 } = 1 / 4$ and $s _ { 1 } = \sin \xi / 2$ . By substituting in eq. (14.8) and integrating over the sphere, we get the net thermal emission force directed along the $\hat { \mathbf { z } }$ axis

$$
\begin{array} { r c l } { { { \bf F } _ { \epsilon } } } & { { = } } & { { \displaystyle - \hat { \bf z } \frac { 2 \epsilon \sigma } { 3 c } \int _ { S } \sin \theta [ { \cal T } _ { 0 } ^ { 4 } + 4 { \cal T } _ { 0 } ^ { 3 } { \cal T } _ { 1 } P _ { 1 } ( \sin \theta ) ] d S } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \displaystyle - \hat { \bf z } \frac { 4 \pi \epsilon \sigma R ^ { 2 } } { 3 c } \int _ { - \pi / 2 } ^ { + \pi / 2 } \sin \theta \cos \theta ( T _ { 0 } ^ { 4 } + 4 T _ { 0 } ^ { 3 } { \cal T } _ { 1 } \sin \theta ) d \theta } } \end{array}
$$

where terms of higher degree have been neglected.3 The average temperature gives an isotropic emission, and the degree 1 harmonic gives a net force

$$
\mathbf { F } _ { \epsilon } = - \hat { \mathbf { z } } \frac { 4 \pi \alpha \Phi _ { \odot } R ^ { 2 } \sin \xi } { 9 c \beta }
$$

where the reduction factor $\beta = 1 + \chi T _ { 0 } / \alpha R \Phi _ { \odot }$ plays an important role. With $A = \pi R ^ { 2 }$ the cross-section, the acceleration is

$$
\frac { { \bf F } _ { \epsilon } } { M } = - \hat { \bf z } \frac { A \Phi _ { \odot } } { M c } \frac { 4 \alpha \sin \xi } { 9 \beta } .
$$

If we assume $\epsilon = \alpha$ , and the distance from the Sun 1 AU, the average temperature is $T _ { 0 } \simeq 2 8 0 \ : \mathrm { K }$ . The assumption $\tau _ { i } \ll \tau _ { 0 }$ used in the linearization of the equations implies $\beta \gg 1$ , i.e., high conductivity. As an example we use the LAGEOS class satellites (see Section 15.2), whose body is an aluminum sphere with a radius of 30 cm and a mass of 400 kg. Then

$$
\frac { \mathbf { F } _ { \epsilon } } { M } = - \hat { \mathbf { z } } \frac { 5 . 8 \times 1 0 ^ { - 8 } } { \beta } \sin \xi \cos / \mathrm { s } ^ { 2 } .
$$

If it is modeled as a homogeneous body, given the conductivity of aluminum $\chi = 2 . 1 \times 1 0 ^ { 7 }$ erg $\mathrm { c m ^ { - 1 } \ s ^ { - 1 } K ^ { - 1 } }$ , we have $\beta = 4 7 1$ . If a modification of the above computation is used to take into account an insulating core of radius 25 cm and an outer aluminum shell, $\beta = 1 5 5$ . In any case the thermal emission is one of the main sources of uncertainty in the dynamical model for spacecraft of the LAGEOS class (see Section 15.3).

For more complex shaped spacecraft, the explicit computation of a surface temperature model is a challenge, and the spherical approximation is too poor. The above computation can be used to give an order of magnitude, provided some estimate for the surface temperature excursion $\Delta T$ is available (to be used in place of the $\mathcal { T } _ { 1 }$ ).

Similar computations can be done for natural bodies, such as asteroids. The conductivity is expected to be much lower, and anyway it is essentially unknown: a reasonable guess would be for a range between 10 and 1000 erg/cm s K, depending upon the texture of the surface (e.g., regolith is a very good insulation, solid rock is more conductive). Moreover, neither the shape is close to spherical nor the conductivity is expected to be constant, given the very uneven distribution of regolith found in the few asteroids for which we have very close images (Eros, Itokawa). Thus to build a realistic thermal model of an asteroid is a challenge, and the thermal emission effects on the orbit cannot be accurately predicted.

# The Yarkovsky effect

The same argument used in Section 14.1 applies to thermal emission: what matters is the fraction of the perturbing acceleration contributing to the secular change in the semimajor axis. For example, if the attitude in an inertial reference system and the thermal state were constant, at least on average, the acceleration induced by thermal emission would be a constant vector and its contribution to $\overline { T }$ would be zero. This is the case for an axially symmetric body rapidly spinning around a fixed axis $\hat { \mathbf { z } }$ orthogonal to the plane of a circular heliocentric orbit. The same applies to a planetocentric orbit, even an eccentric one, if we can assume that the surface temperature is not significantly affected by the thermal emission from the planet and there are no eclipses (Anselmo et al. 1983a). However, unlike direct radiation pressure, thermal emission can have secular effects in the semimajor axis for a heliocentric orbit, even for a spherical shape; this is called the Yarkovsky effect. A similar effect occurs for geocentric orbits, due to the uneven heating resulting from radiation emitted by both the Sun and the Earth.

It is important to realize that there is no Yarkovsky force, but just thermal emission forces, which under suitable circumstances have a comparatively small, but significant, mean transversal component $\overline { T }$ . We shall discuss here the heliocentric case, in which there are two contributions to the Yarkovsky effect: the seasonal and the diurnal one.

# Seasonal Yarkovsky effect

If a body with a fixed rotation axis were in a constant thermal state as it orbits around the Sun, then the thermal emission force of eq. (14.11) would be of constant size and direction, thus $\overline { { T } } = 0$ . This condition can be violated for two reasons.4 The first is when the obliquity $\epsilon$ , that is the angle between the spin axis and the orbital angular momentum, is not 0. Then the latitude $\xi$ of the Sun in the body equatorial frame is not constant, and eq. (14.11) gives a thermal emission force changing with time, essentially with the frequency of the mean motion $n$ . The second reason is that the illumination $\Phi _ { \odot }$ is a function of the distance from the Sun, thus it changes for an eccentric orbit, mostly with the frequency $n$ .

In both cases, the thermal emission force has an intensity which changes with a period equal to the orbital period (in a two-body approximation), and the same resonance effect mentioned for radiation pressure on asymmetric bodies can apply. This is called a seasonal effect because it depends on the fact that the heliocentric body has temperature variations depending upon the equatorial obliquity and upon the orbital eccentricity, similarly to the major planets. An explicit computation of the size of this effect is not simple, even for a spherical body (Vokrouhlick´y et al. 2000), and becomes very complicated for complex shaped bodies. Qualitatively, the secular drift is always towards the lower semimajor axis and its magnitude can be up to 15 m/y for asteroids with diameter in the 300–500 m range.

# Diurnal Yarkovsky effect

The Yarkovsky diurnal effect arises because thermal inertia of the illuminated body results in a temperature maximum lagging some time after the maximum of illumination. This effect depends upon the conductivity $\chi$ , by no means linearly: for $\chi \to 0$ the thermal time lag goes to zero; for $\chi  + \infty$ the surface temperature excursion goes to zero; for some intermediate value of $\chi$ there is a maximum effect, see (Vokrouhlick´y et al. 2000, Figure 1). Interestingly, in the realistic range of values of $\chi$ for a small asteroid, in many cases the dependence upon $\chi$ is not very strong, the effect changing by less than a factor of 2. Thus this effect is always of the same order of magnitude, once the mass is known; of course it depends upon the obliquity $\epsilon$ , with the semimajor axis secularly increasing for prograde rotation ( $\epsilon < 9 0 ^ { \circ }$ ) and decreasing for retrograde ( $\epsilon > 9 0 ^ { \circ }$ ). The magnitude of this effect can be larger than that of the seasonal effect, up to several tens of $\mathrm { m } / \mathrm { y }$ .

# When is the Yarkovsky effect relevant?

The Yarkovsky effect is very important as a source of secular perturbations to model the dynamical evolution of asteroids, e.g., it is relevant for the transport of meteorites and asteroids to the near-Earth region: $\mathrm { 1 5 ~ m / y }$ $\simeq 1 0 ^ { - 4 }$ AU/My accumulates to a large change over the age of the asteroids. From the point of view of orbit determination, there are only a few and so far exceptional cases where effects of this class are relevant to fit an orbit of an asteroid. This is because the secular perturbations are typically a few percent of the instantaneous thermal emission accelerations. Thus for an orbit determination with a data span shorter that an orbital period they are very small, and anyway less relevant than the short period perturbations due to both direct radiation pressure and thermal emission.

The exceptional cases are asteroids with a very long observed arc; very accurate observations may also be needed. As an example, the first asteroid for which the Yarkovsky effect has been measured by orbit determination is (6489) Golevka, which has been observed by radar during three separate close approaches to the Earth; the second case was (152563) 1992 BF, an asteroid with an exceptionally long arc due to attribution of precovery observations (Chesley et al. 2003, Chesley et al. 2008). With the accumulation of more data and also with the expected improvements in astrometric accuracies, such cases will become much more frequent.

# 14.3 Indirect radiation pressure

The case of a satellite orbiting around a planet (and the Moon) is more complicated because the planet is an additional source of radiation, ultimately coming from the Sun but either reflected, or diffused, or absorbed and reemitted as infrared. Moreover, the planet casts a shadow which cuts off direct radiation pressure from the Sun and also results in thermal transient states of the spacecraft. This is a very complicated subject and our intent is not to explain in detail how to model the corresponding non-gravitational perturbation on the orbit, but just to list the different physical effects and give an idea of their relative importance for an accurate orbit determination.

# Reflected radiation pressure

A planet illuminated by the Sun also shows a linear combination of absorption, reflection, and diffusion, with optical coefficients (14.1) which may change significantly with the position on the surface. For example, on the Earth the planetary albedo $1 - \alpha _ { \oplus }$ can be $\sim 0 . 8$ for glaciers, fresh snow and clouds, $\sim 0 . 2$ for the ocean and intermediate for a continental area with clear sky, depending also on the vegetation cover. The ratio $\rho / \delta$ depends also upon the texture of the surface, with a smooth lake mirror reflecting more than a rough sea; there are phenomena intermediate between mirror reflection and diffusion, resulting in a concentration of reflected light near the perfect reflection direction, like in the sword of the Sun which can be observed at sunset from the seashore and from an airplane over the sea.

# Visible light

To accurately model the radiation pressure on a spacecraft from the visible light reflected/diffused by a planet we would need a map of the optical coefficients $\alpha , \rho , \delta$ values on the entire surface, in the case with an atmosphere with variable weather (as on the Earth and on Mars) including a full weather map giving at least the average cloud cover with good spatial and time resolution. Then the effect could be computed for each surface element, and some numerical approximation of a surface integral over the portion of surface visible from the spacecraft should be used. In practice, this has never been done, and although it may become technologically feasible in the future we have to question whether this would be useful.

To compute the orders of magnitude of the relevant effects, let us select the case of the geodetic satellite LAGEOS. Radiation reflected/diffused from the Earth has an instantaneous value of the order of $3 \times 1 0 ^ { - 8 } \ \mathrm { c m / s ^ { 2 } }$ (see Table 15.1 for comparison with other perturbations). The orbit of LAGEOS was found to be affected by a mystery drag, that is an unexpected secular decrease of the semimajor axis, corresponding to an average transversal deceleration $\overline { { T } } \approx - 3 \times 1 0 ^ { - 1 0 } ~ \mathrm { c m / s ^ { 2 } }$ ; superimposed on this secular effect, there were long periodic terms corresponding to values of $\overline { T }$ of the order of $1 0 ^ { - 1 0 } ~ \mathrm { c m / s ^ { 2 } }$ and with periods up to three years. The secular term cannot be explained by radiation pressure (possibly by the Yarkovsky effect and/or drag), but the long period ones could be: this implies that a “brute force” model of the radiation pressure of the Earth would need to have a relative accuracy $< ~ 0 . 0 0 3$ to roughly account for the long periodic terms of the mystery drag.

Anselmo et al. (1983b) have shown that the radiation from the Earth could well account for the long periodic perturbations to the semimajor axis of LAGEOS by a semiquantitative argument, in which what matters is the angle between the orbital plane of LAGEOS and the terminator plane through the Earth’s center of mass and orthogonal to the Sun’s direction. Neglecting topography, the intersection of the terminator plane with the Earth’s surface is the line along which either sunrise or sunset takes place.

When the satellite orbit is crossing the terminator plane, e.g., with a ground track crossing from day to night, the radiation pressure from the illuminated portion of the Earth is pushing from behind the spacecraft and increasing the semimajor axis. After the true anomaly of the satellite has increased by $\simeq \pi$ , there is another terminator plane crossing, this time with the ground track crossing from night to day, thus a push from the front and a decrease of the semimajor axis. If these two spikes of $T$ were exactly equal and opposite, there would be no contribution to $\overline { T }$ . However, one of the two terminator crossings is in the Northern hemisphere, the other in the Southern one with a much larger proportion of low albedo ocean area; if one of the two is with the ground track on a region experiencing summer, the other is in winter, with increased cloud cover. Thus there is unbalance and a long periodic perturbation, having as the main angular arguments the Sun mean longitude $\lambda _ { \odot }$ and LAGEOS longitude of the node $\Omega$ , thus the main effects have periods between 156 and 1050 days, in qualitative agreement with the frequency spectrum of the mystery drag.

# Infrared radiation

The thermal emission from the planet is regulated by the same heat equation (14.9), thus a solution for the thermal emission can be computed in the spherical surface approximation. However, unlike the asteroid case of Section 14.2, it is not possible to average over a revolution of the planet, because this period can be longer than the orbital period of the spacecraft; also the lag in the temperature maximum after the time of maximum illumination can be comparable to the satellite orbital period.

The average temperature $\mathcal { T } _ { 0 }$ results in isotropic emission which has the same effect of a change in the mass of the planet. The main contribution to the infrared radiation pressure perturbations arise from the first harmonic $\mathcal { T } _ { 1 }$ ; note that $\mathcal { T } _ { 1 } \ll \mathcal { T }$ is a reasonable approximation for a planet such as the Earth, but fails for the Moon and even more for Mercury. For an accurate model, the absorption $\alpha$ cannot be assumed to be constant; even on dark bodies like the Moon and Mercury there are comparatively bright surface features. Again the total effect of infrared radiation pressure needs to be computed as an integral over the portion of surface visible from the spacecraft.

The conclusion is that infrared radiation pressure can be modeled somewhat more easily than visible radiation pressure from the planet, because the surface behavior is less sharply variable, but still this can be a suitable model to simulate the effect, not an accurate model.

# Eclipses

A planet, or anyway a large body, prevents sunlight from reaching a shadow cone: when the spacecraft is in the full shadow, it experiences an eclipse of the Sun, during which there is no direct radiation pressure from sunlight (Milani et al. 1987, Section 5.4). This effect is important because the average transversal component $\overline { T }$ of the direct radiation pressure force is not zero when the orbit plane is such that eclipses occur and the orbital eccentricity is not zero. It is possible to compute semianalytically the effect on the semimajor axis (Aksnes 1976).

The full shadow is surrounded by a region of penumbra; e.g., the diameter of the Sun is $2 ^ { \circ }$ as seen from Mercury, and a Mercury orbiter with an orbital period of a few hours experiences penumbra for a few tens of seconds just before and after the full shadow.

For orbits undergoing eclipses, the assumption of Section 1.1 that the right-hand side of the equations of motion is differentiable may fail. In practice, the direct radiation pressure acceleration may go from its full value to zero (and vice versa) in a very short time span, that of the penumbra phase. Since this time span for abrupt change can be shorter than, or comparable to, the step size of the numerical integrator used to propagate the orbit, numerical instabilities may occur. Indeed, they have been detected in numerical experiments with space debris.

For large $A / M$ , of the kind which can occur in small space debris, the overall effect of eclipses, combined with other perturbations, can accumulate to very large values; the consequence is a very significant increase of the risk of impact on active satellites by high relative velocity debris (Valk and Lemaitre 2007).

# 14.4 Drag

Drag is caused by the direct interaction of the spacecraft with matter, assumed to be neutral (molecules). It is a resistive force, opposite in direction to the spacecraft velocity with respect to the average atmosphere

$$
\mathbf { F } _ { v } = - { \frac { 1 } { 2 } } C _ { D } A \rho \left| \mathbf { v } \right| \mathbf { v }
$$

with $\rho$ the density of the atmosphere, $A$ the cross-sectional area orthogonal to $\mathbf { v }$ , the velocity relative to the atmosphere, and $C _ { D }$ the adimensional drag coefficient (or aerodynamic coefficient), which is in general of the order of unity (Milani et al. 1987, Chapter 6).

It is already clear from eq. (14.12) that very accurate modeling of drag is not possible. The main unknown parameter is the density $\rho$ , changing both in space and in time. The dependence upon the distance from the geocenter $r$ can be described with moderate accuracy by an exponential model:

$$
\rho ( r ) = \rho _ { 0 } \exp \left( \frac { r _ { 0 } - r } { \mathcal { H } } \right) ,
$$

where $\rho _ { 0 } = r ( r _ { 0 } )$ and $\mathcal { H }$ is the scale height over which the density decreases by $1 / \exp ( 1 )$ . This equation gives the solution for an isothermal column of gas in equilibrium with its own weight (Boltzmann law), and is a valid approximation when the temperature undergoes little change with height, as it happens in some high atmospheric layers (above 250 km). In practice, the scale height changes with height, and $\rho _ { 0 }$ can experience variations by an order of magnitude or more as a result of solar and geomagnetic activity, on top of the changes driven by the solar illumination.

The computation of $C _ { D }$ is very complicated; when electromagnetic effects come into play, as a result of the charged particles in the ionosphere, the negative charging of the spacecraft surface may result in a coefficient $C _ { D }$ larger by one order of magnitude than the values typical of the neutral atmosphere (Milani et al. 1987, Section 6.3).

The atmosphere rotates with the Earth, more or less rigidly, thus the velocity $\mathbf { v }$ does not coincide with the inertial velocity but is closer to the velocity in a body fixed reference frame. Even the assumption, contained in eq. (14.12), that the drag force is along the direction $\hat { \mathbf { v } }$ is a simplification, because for some spacecraft shapes there could be a significant lift effect, e.g., for large panels oriented at an $\mathrm { a n g l e } \ne \frac { \pi } { 2 }$ with respect to $\hat { \bf v }$ .

In conclusion, although drag forces have been the first non-gravitational ones to be included in models of satellite orbits (King-Hele 1964), in state-ofthe-art satellite geodesy it is necessary to assume they are either measured by some on-board instrumentation (accelerometer), or compensated (drag free probe), or removed from the problem by using satellite navigation systems; see Chapter 16. They have to be taken into account when solving for the rapid orbital decay of low satellites and space debris, and in the planning of satellite geodesy missions whose lifetime is limited by orbital decay.

# 14.5 Active spacecraft effects

In an active spacecraft the energy from the Sun absorbed by the outer surface is processed in several ways before being re-emitted in different forms. Moreover, the internal temperature distribution is actively controlled by heaters, coolers, radiators, and by the dissipation of heat resulting from energy consumption. The thermal conditions (both the stationary states and the transients between them) are typically predicted with finite element algorithms, measured by on-board thermometers, and controlled by heat pipes and feedback loops activating heaters and variable surface radiators. All the clever methods used by aerospace engineers to maintain the onboard devices within their operational temperature range result in a more and more difficult task to model the thermal emission acceleration.

In practice, a model of the external surface temperatures with the required accuracy is never available.5 This is even more the case when the external conditions are extreme, e.g., in the cold of the outer Solar System exploration probes and in the heat of the interior planet orbiters (see Chapter 17).

# Radio wave beams

An active spacecraft needs to transmit to a ground station, by generating a directional radio wave beam; another possibility is a radio wave beam for radar, thus pointed to the planetary surface. Thus a fraction of the power $\alpha \Phi _ { \odot } A$ absorbed through the surface is converted into electrical power, a fraction of which is used to generate radio waves. Both conversions having an efficiency less than unity, the power actually emitted as radio waves is a small fraction of the absorbed power, a few per cent. Nevertheless, the emitted beam has a direction different from the Sun and may contribute significantly to the secular along-track effect $T$ (Milani et al. 1987, Section 5.3).

# Possible solutions

If the accuracy of the orbit determination requires to take into account thermal emission and other subtle effects depending upon the spacecraft structure and activity, there are only two solutions. Either the non-gravitational perturbations are not modeled, but measured by accelerometers (see Chapter 16), or they are described by a set of empirical parameters to be solved with the orbit. The accelerometers are more suitable for the large and rapidly variable non-gravitational perturbations of the Mercury orbiters (see Chapter 17). In the cold and slowly variable conditions of the outer Solar System cruise phases, few parameters can describe the non-gravitational perturbations over a long arc. Two examples of the latter approach follow.

In (Bertotti et al. 2003a) the interplanetary orbit of the Cassini mission had to be modeled very accurately during a time span of a few weeks, during a superior conjunction, to determine the post-Newtonian parameter $\gamma$ (see

Sections 6.6 and 17.5). The spacecraft was in a stationary state during the interplanetary cruise, with constant attitude and thermal state. Thus the non-gravitational acceleration (including both direct radiation pressure and thermal emission) over the observation arc time span used in the experiment could be modeled by a constant vector. The experiment was very successful (with an estimated $\mathrm { R M S } ( \gamma ) \simeq 2 \times 1 0 ^ { - 5 }$ ) because of the extremely accurate tracking and of the simple operations mode of the spacecraft.

In (Olsen 2007) the orbit of the Pioneer spacecraft, while navigating beyond Saturn in an orbit escaping from the Solar System, has been solved assuming a constant perturbing acceleration directed towards the Sun. The interpretation of this “Pioneer anomaly” has been the subject of some controversy, but Olsen convincingly argues that a minor anisotropy ( $\simeq 0 . 0 3$ of the isotropic term) in the thermal emission from the radioisotope power generator can account for the estimated $8 \times 1 0 ^ { - 8 } ~ \mathrm { c m / s ^ { 2 } }$ acceleration. The time span of the data is not enough to discriminate between a constant acceleration and one decaying exponentially with the radioactive material (with a known half life of 87 years), but some indications of decay have been found.

The only way to prove that the effect is indeed due to non-gravitational perturbations, rather than to “anomalous gravity” of whatever origin, is to test the orbits of celestial objects with very different area-to-mass ratio and orbiting in the same region. Wallin et al. (2007) solved for the orbits of the best observed trans-neptunian objects adding a parameter to model the “Pioneer anomaly”: if it were due to gravitational perturbations, by the equivalence principle it should also affect bodies of diameter $> 1 0 0 \mathrm { k m }$ . They found a value for the unexplained radial acceleration an order of magnitude smaller than the Pioneer value, consistent with zero at the 1 RMS level, and inconsistent with the Pioneer value at the 5 RMS level. Thus the “Pioneer anomaly” is non-gravitational, and it should be due to thermal emission.

# Maneuvers and leakages

It must not be forgotten that accurate orbit determination cannot be done on a spacecraft performing maneuvers, not only orbit control maneuvers, but also attitude control ones. Even when the attitude controlling torques are applied by using two thrusters acting in parallel and opposite directions, the amount of impulse from them cannot be balanced with very good accuracy; for the order of magnitude of this effect, see (Milani et al. 1987, Section 7.2). There are only two methods to control the degradation of orbit determination due to maneuvers, and they have to be chosen before, at the mission planning stage.

One method is to estimate, during the mission analysis study, how often the maneuvers have to be performed, and how much they affect the orbit. This is comparatively easy for the orbit maneuvers (Milani et al. 1987, Section 7.1), but it is not trivial for the attitude maneuvers. A space mission with a requirement for a very accurate orbit determination needs to use methods different from thruster activation to control attitude, such as reaction wheels, and the time span after which thruster activation is required for the unloading of the reaction wheels needs to be carefully predicted.

The second method is to agree, in the mission design phase, on a constraint on the time interval between maneuvers, and then use a multi-arc approach (see Chapter 15), with the arcs beginning and ending at the maneuver times. Still there is a requirement that the times are known.

Another similar problem is due to gas leaks from the thrusters. Even when the valves controlling the activation of the propulsion system are nominally shut, small leaks are difficult to avoid. The problem is that such leaks might be so small that the spacecraft designers do not worry about them, and still the impact on the orbit determination accuracy is significant. For example, a gas leak of hydrazine by an amount of 100 g per year might not be a problem from the point of view of fuel consumption, nevertheless with the gas at a temperature of $2 0 0 \mathrm { K }$ on a spacecraft with mass $M = 5 0 0 ~ \mathrm { k g }$ i t would result in an acceleration of $4 \times 1 0 ^ { - 7 } ~ \mathrm { c m / s ^ { 2 } }$ .

# 14.6 Case study: asteroid orbiter

The main conclusion which should be drawn from the discussion of the intricacies of non-gravitational perturbations modeling is a simple advice: do not do it. If possible, a mission requiring very accurate orbit determination should be designed in such a way that its performance does not depend upon the accuracy, reliability, and stability with time of the non-gravitational perturbation model. However, there is a class of space missions for which this advice cannot be followed: the asteroid orbiters, whose purpose includes an extremely accurate orbit determination of the asteroid.

To understand why there could be the need to do this, please refer to Chapter 12. The basic idea is that we may need to deflect the orbit of an asteroid, which is predicted to impact our planet at some time in the foreseeable future, a few tens of years from now. Alternatively, we may wish to demonstrate that the technology to take such a defensive action is available, to be used if and when it may become necessary; this was the main goal of the space mission study Don Quixote, first performed on behalf of the European Space Agency (ESA) in 2002, and later updated both by internal ESA and industrial studies.6

Don Quixote was intended as a two-spacecraft mission, with one component, Sancho, orbiting around the target asteroid with the necessary complement of instruments to allow for an extremely accurate orbit determination, of both the spacecraft asteroid-centric orbit and the asteroid heliocentric orbit. The second component, Hidalgo, would arrive later and impact the asteroid at the largest possible relative velocity, thus transferring a significant amount of linear momentum and changing the heliocentric orbit by an amount which could be measured by Sancho. The purpose was to test this simple kinetic method of deflection and learn how effective is the transfer of linear momentum.7

# Photo-gravitational symmetry

The Don Quixote method of deflection is attractive because it appears to be simple, not requiring new technologies (unlike other methods which have been proposed). However, there is a technology which needs to be demonstrated: non-gravitational perturbation modeling and/or determination. To understand this, we need to appreciate the orders of magnitude. Let us assume the target asteroid has a roughly spherical shape, with diameter $2 R = 3 0 0 ~ \mathrm { m }$ and density $\mathrm { 1 . 3 ~ g / c m ^ { 3 } }$ , thus a mass $m \simeq 1 8 \times 1 0 ^ { 6 }$ tons. If Sancho has a roughly circular orbit at a distance $r = 1 0 R$ , the acceleration due to gravity from the asteroid is $g \simeq 5 . 4 \times 1 0 ^ { - 5 } \ \mathrm { c m / s ^ { 2 } }$ , while the direct radiation pressure from the Sun is $f \simeq 1 . 8 \times 1 0 ^ { - 5 } \ \mathrm { c m / s ^ { 2 } }$ (we are assuming $A = 2 0 ~ \mathrm { m ^ { 2 } }$ and $M = 5 0 0 ~ \mathrm { k g }$ ), thus the perturbation approach used in Section 14.1 is a rough approximation. To use an analytical formula as a tool to find the appropriate orders of magnitude, we need to find an exact solution to the photo-gravitational problem as a function of both $f$ and $g$ ; we are neglecting the differential attraction from the Sun.

We assume that the spacecraft motion takes place in a plane orthogonal to the direction $\hat { \mathbf { s } }$ to the Sun, that is parallel to the asteroid terminator plane. Let us assume only three accelerations are acting on the spacecraft in a rotating reference system: the gravitational monopole attraction $\mathbf { g }$ , the radiation pressure acceleration f, and the centrifugal acceleration $\omega ^ { 2 } \mathbf { r }$ , where $\omega$ is the angular rate around an axis parallel to $\hat { \bf s }$ passing from the asteroid center of mass, and $\mathbf { r }$ is the vector orthogonal to this axis pointing to the position of the spacecraft. Let $\mathbf { h }$ be the vector parallel to $\hat { \bf s }$ between the asteroid center of mass and the plane in which the spacecraft asteroidcentric orbit lies. We look for a relative equilibrium solution, stationary in the frame rotating with angular velocity $- \boldsymbol { \omega } \hat { \mathbf { s } }$ , such that ${ \boldsymbol { \omega } } ^ { 2 } \mathbf { \Delta r } + \mathbf { g } + \mathbf { f } = \mathbf { 0 }$ . The components of the gravitational acceleration $\mathbf { g }$ along $\mathbf { r }$ and along $\mathbf { h }$ have to be balanced by centrifugal and radiation pressure accelerations (see Figure 14.1)

![](images/e94db5b37ac21d22fab9cb8f94903e3f7b55693e8d7895354e4b39b28ede94aa.jpg)  
Fig. 14.1. For an asteroid with $3 0 0 \mathrm { ~ m ~ }$ diameter, the simple two-body model of the photogravitational symmetry results in a very large displacement of the orbit plane with respect to the asteroid center of mass. The orbit plane does not even touch the asteroid!

$$
= - { \frac { G m } { \left( r ^ { 2 } + h ^ { 2 } \right) ^ { 3 / 2 } } } \left( \mathbf { r } + \mathbf { h } \right) , \ - \omega ^ { 2 } \mathbf { r } = - { \frac { G m } { \left( r ^ { 2 } + h ^ { 2 } \right) ^ { 3 / 2 } } } \mathbf { r } , \ \mathbf { f } = { \frac { G m } { \left( r ^ { 2 } + h ^ { 2 } \right) ^ { 3 / 2 } } } \mathbf { h }
$$

These equations have an exact solution for every $h$ provided $f , m$ change as

$$
f ( h ) = \omega ^ { 2 } ~ h ; ~ m ( h ) = m ( 0 ) ~ \big ( 1 + h ^ { 2 } / r ^ { 2 } \big ) ^ { - 3 / 2 } ,
$$

where $m ( 0 )$ is the mass corresponding to $h = f = 0$ .

In this simplified model, the circular solution of relative photogravitational equilibrium is valid for every value of $r$ . In reality this solution does not exist for $r$ smaller than the asteroid radius $R$ because of the shadow, and becomes a poor approximation when $r$ becomes comparable to the radius of the asteroid sphere of influence; then the differential gravitational attraction from the Sun becomes important.8 For intermediate values of $r$ , e.g., in the range 3 $R \leq r \leq 2 0 ~ R$ , it is a useful first approximation.

The geometry of the orbit and its velocity are unchanged, since $r$ and $\omega ^ { 2 } = G m ( 0 ) / r ^ { 3 }$ are independent of $h$ . Thus the value of $h$ is not observable by measuring the range and range-rate from Earth; the asteroid center of mass position (CoM), which is not observable directly, is shifted by $- \mathbf { h }$ . The implication is that, in this approximation, if the list of parameters to be solved includes the asteroid CoM position, the quantity $f$ , and the asteroid mass $m$ , then the normal matrix is degenerate. These parameters cannot be solved at once, whatever the set of range and range-rate observations, and this is independent of the measurement accuracy. This exact symmetry is called the photo-gravitational symmetry. The only solution is to assign a priori constraints to $f$ or $h$ : either $f$ is determined from a radiation pressure model, or $h$ is measured by some local observation of the asteroid, e.g., from images of the asteroid taken from the spacecraft.

The implications for Don Quixote are apparent from a simple order of magnitude computation. For the nominal asteroid and spacecraft discussed before, $h = f / \omega ^ { 2 } \simeq 5 0 0 ~ \mathrm { m }$ . A relative error of 0.1 in the model for radiation pressure on the spacecraft would imply an error in estimating the position of the asteroid CoM of $\simeq 5 0 ~ \mathrm { m }$ . Estimation of the position of the CoM of the asteroid from the images should give a smaller error, taking into account that such a small asteroid is expected to have a rather uniform density. Still an error of the order of $R / 1 0 \simeq 1 5 ~ \mathrm { m }$ would be unavoidable. What matters is that such an error would be much larger than the error in determining the position of Sancho with state-of-the-art tracking from the Earth, which could have submeter accuracy in range.

The above discussion is strongly simplified with respect to a realistic case, in which the shape of the asteroid is irregular, thus its gravity field contains significant low degree spherical harmonics, and the asteroid is in a heliocentric elliptic orbit, thus $f$ is not constant. In reality the task of finding, from images of the asteroid, where the CoM is, would be far from trivial, but would need to be included in a complex orbit determination problem, in which the orbit of the asteroid, the orbit of Sancho, the rotation state of the asteroid, and some harmonics of its gravity field would appear as fit parameters. Nevertheless, the order of magnitude estimate is applicable, and there is indeed a limit at a few tens of meters in the possibility of determining accurately the asteroid-centric orbit, thus also the asteroid orbit from tracking of the Sancho orbiter.

# Deflection by impact and its measure

Let us suppose the impactor Hidalgo has a mass of $4 0 0 ~ \mathrm { k g }$ and a relative velocity (with respect to the target asteroid) of 10 km/s. Then, even assuming that the linear momentum is transfered to the asteroid without gain due to ejecta, the asteroid changes its velocity by $0 . 0 2 ~ \mathrm { c m / s }$ . For an asteroid with semimajor axis $a = 0 . 9$ AU this implies a change in $a$ , depending upon the angle $\theta$ between the direction of the velocity change and the heliocentric velocity, of $\simeq 1 . 8 \ \cos \theta \ \mathrm { k m } .$ . This results in a change in the mean motion, accumulating an along-track drift of $- 5 6$ cos θ m/day. Thus the inaccuracy in the determination of the asteroid position, due to radiation pressure on Sancho, does not prevent a measurement with good relative accuracy, say 0.01 or better, of the deflection by continuing the tracking for weeks after the Hidalgo impact.

However, there is another element in the problem, namely nongravitational perturbations on the orbit of the asteroid. The assumed asteroid has an area-to-mass ratio $A / M \simeq 4 \times 1 0 ^ { - 5 }$ , thus $\beta \simeq 2 . 7 \times 1 0 ^ { - 9 }$ (see Section 4.6) and radiation pressure acceleration $\simeq 6 \times 1 0 ^ { - 1 0 } \ \mathrm { c m \ s ^ { - 2 } }$ . As a result, its semimajor axis changes by $\simeq 4$ $\cos \theta ^ { \prime }$ m/day, where $\theta ^ { \prime }$ is the angle between the direction $\hat { \bf s }$ and the heliocentric velocity. Thermal emission is somewhat smaller, but more difficult to be modeled. Thus the main term of the error budget of the deflection measurement is neither the range measurement error nor the error in modeling/measuring the radiation pressure on Sancho, but the error in modeling the non-gravitational perturbations on the orbit of the asteroid. For the best performance of a Don Quixote class mission, to model accurately direct radiation pressure and thermal emission effects on the asteroid is a requirement.

The above is not necessarily an argument against the Don Quixote style deflection experiments. As shown by Chesley (2006), in the real case of the asteroid (99942) Apophis which could impact the Earth in 2036 (see Section 12.6), it might be possible neither to exclude, nor to predict with certainty that impact unless a much better model of the Yarkovsky effect is available for that asteroid. As pointed out above, there is no way to measure the Yarkovsky effect in a short time span; what is required is to follow an asteroid with a very accurate tracking, allowing us to fit the non-gravitational acceleration, represented as a time series (possibly as polynomial interpolations), for an entire orbital period of the asteroid, to directly determine the average along-track acceleration. This could be done with a Sancho-class spacecraft orbiting around Apophis for an orbital period of the asteroid. The conclusion of this phase of the mission could allow us to predict without uncertainty either the occurrence or the impossibility of an impact, allowing for a Hidalgo spacecraft to perform the deflection if necessary.

# 15

# MULTI-ARC STRATEGY

One of the main assumptions used in Chapter 1 is that the dynamical model is deterministic. This assumption can be too optimistic for celestial bodies small enough to be significantly affected by complex non-gravitational interactions. Both drag and radiation pressure can be so poorly known that the errors in the dynamical model can affect the predictions by amounts exceeding, by orders of magnitude, the measurement accuracy.

When this is the case, there are three possible ways out, including the multi-arc strategy presented in this chapter. The others are the use of on-board accelerometers, see Chapters 16, 17, and the empirical parameterization of the unknown effects, see Section 14.5.

The multi-arc approach gives up the attempt to model the orbit of the spacecraft, over the entire time span of the observations, in a deterministic way with a single set of initial conditions. The time span of the observations is decomposed into shorter intervals and the set of observations belonging to each interval is called an observed arc, or just an arc. Each arc has its own set of initial conditions, as if there were a new spacecraft for each one of them. This results in over-parameterization, with the additional initial conditions absorbing the dynamical model uncertainties. Other parameters, e.g., in the dynamic model, can also be local to a single arc.

# 15.1 Local–global decomposition

The mathematics of the multi-arc method is a generalization of that of the marginal uncertainties discussed in Section 5.4. We use the notation $[ \mathbf { a } ; \mathbf { b } ]$ to indicate the stacking of the two column vectors $\mathbf { a }$ and $\mathbf { b }$ to form a longer vector. The vector of all fit parameters $\mathbf { x } = [ \mathbf { g } ; \mathbf { h } ]$ is split into a vector $\mathbf { g }$ of global fit parameters and a vector $\mathbf { h }$ of local fit parameters. The observations and the corresponding residuals are partitioned into $n$ arcs by some criterion, usually by time, in such a way that ${ \pmb \xi } = | { \pmb \xi } _ { 1 } ; { \pmb \xi } _ { 2 } ; \ldots ; { \pmb \xi } _ { n } |$ . The vector $\mathbf { h }$ is also split into vectors $\mathbf { h } _ { j }$ , one for each arc. Each subvector $\mathbf { h } _ { j }$ is associated to the arc with the same index, in such a way that the residuals from one arc do not depend upon the local parameters of another arc

$$
B _ { \mathbf { g } } ^ { ( j ) } = \frac { \partial \pmb { \xi } _ { j } } { \partial \mathbf { g } } , B _ { \mathbf { h } _ { i } } ^ { ( j ) } = \frac { \partial \pmb { \xi } _ { j } } { \partial \mathbf { h } _ { i } } \ = \mathbf { 0 } \ \mathrm { ~ f o r ~ } i \neq j .
$$

As a result the contributions of each arc to the overall normal equation are

$$
C _ { \mathbf { h } _ { i } \mathbf { h } _ { j } } = ( B _ { \mathbf { h } _ { i } } ^ { ( i ) } ) ^ { T } B _ { \mathbf { h } _ { j } } ^ { ( j ) } = C _ { \mathbf { h } _ { j } \mathbf { h } _ { i } } ^ { T } \ = \mathbf { 0 } \mathrm { f o r } \ i \neq j
$$

$$
C _ { \mathbf { g h } _ { i } } = ( B _ { \mathbf { g } } ^ { ( i ) } ) ^ { T } B _ { \mathbf { h } _ { i } } ^ { ( i ) } = C _ { \mathbf { h } _ { i } \mathbf { g } } ^ { T } , \quad C _ { \mathbf { g } \mathbf { g } } = \sum _ { i = 1 } ^ { n } ( B _ { \mathbf { g } } ^ { ( i ) } ) ^ { T } B _ { \mathbf { g } } ^ { ( i ) } = C _ { \mathbf { g } \mathbf { g } } ^ { T }
$$

giving to the normal matrix $C$ an arrow-like structure (here we show the simplest case with two arcs only):

$$
C = \left( \begin{array} { c c } { C _ { \bf g g } } & { C _ { \bf g h } } \\ { C _ { \bf h g } } & { C _ { \bf h h } } \end{array} \right) = \left( \begin{array} { c c c } { C _ { \bf g g } } & { C _ { \bf g h _ { 1 } } } & { C _ { \bf g h _ { 2 } } } \\ { C _ { \bf h _ { 1 } g } } & { C _ { \bf h _ { 1 } h _ { 1 } } } & { \bf 0 } \\ { C _ { \bf h _ { 2 } g } } & { \bf 0 } & { C _ { \bf h _ { 2 } h _ { 2 } } } \end{array} \right) .
$$

The contributions to the right-hand side $D$ of the normal equation are

$$
D = [ D _ { \mathbf { g } } ; D _ { \mathbf { h } } ] = [ D _ { \mathbf { g } } ; D _ { \mathbf { h } _ { 1 } } ; D _ { \mathbf { h } _ { 2 } } ; \ldots ; D _ { \mathbf { h } _ { n } } ] ,
$$

with

$$
D _ { \mathbf { g } } = - \sum _ { i = 1 } ^ { n } ( B _ { \mathbf { g } } ^ { ( i ) } ) ^ { T } \pmb { \xi } _ { i } , ~ D _ { \mathbf { h } _ { i } } = - ( B _ { \mathbf { h } _ { i } } ^ { ( i ) } ) ^ { T } \pmb { \xi } _ { i } .
$$

Then the normal equation can be written as a system of two vector equations:

$$
\left\{ \begin{array} { l l } { C _ { \mathbf { g g } } \Delta \mathbf { g } + C _ { \mathbf { g h } } \Delta \mathbf { h } = D _ { \mathbf { g } } } \\ { C _ { \mathbf { h g } } \Delta \mathbf { g } + C _ { \mathbf { h h } } \Delta \mathbf { h } = D _ { \mathbf { h } } } \end{array} \right.
$$

which can be solved as discussed in Section 5.4, by first solving for $\Delta \mathbf { h }$ in the second equation; the matrix $C _ { \mathbf { h } \mathbf { h } }$ is block diagonal, thus it is possible to invert each diagonal block $C _ { \mathbf { h } _ { j } \mathbf { h } _ { j } }$ separately

$$
\Delta \mathbf { h } _ { j } = C _ { \mathbf { h } _ { j } \mathbf { h } _ { j } } ^ { - 1 } \left[ D _ { \mathbf { h } _ { j } } - C _ { \mathbf { h } _ { j } \mathbf { g } } \Delta \mathbf { g } \right] ,
$$

implying that the corrections to the local parameters $\mathbf { h } _ { j }$ are not the same as would be obtained by ignoring the interaction with the global parameters, expressed by the submatrix $C _ { \mathbf { h } _ { j } \mathbf { g } }$ . These expressions for $\Delta \mathbf { h } _ { j }$ can be

substituted into the first equation

$$
\left[ C _ { \mathbf { g } \mathbf { g } } - \sum _ { j = 1 } ^ { n } C _ { \mathbf { g h } _ { j } } C _ { \mathbf { h } _ { j } \mathbf { h } _ { j } } ^ { - 1 } C _ { \mathbf { h } _ { j } \mathbf { g } } \right] \Delta \mathbf { g } = C ^ { \mathbf { g g } } \Delta \mathbf { g } = D _ { \mathbf { g } } - \sum _ { j = 1 } ^ { n } C _ { \mathbf { g h } _ { j } } C _ { \mathbf { h } _ { j } \mathbf { h } _ { j } } ^ { - 1 } D _ { \mathbf { h } }
$$

giving the solution for the global parameters

$$
\Delta { \bf g } = \Gamma _ { { \bf g } { \bf g } } [ D _ { \bf g } - \sum _ { j = 1 } ^ { n } C _ { { \bf g } { \bf h } _ { j } } C _ { { \bf h } _ { j } { \bf h } _ { j } } ^ { - 1 } D _ { { \bf h } _ { j } } ] , ~ \Gamma _ { { \bf g } { \bf g } } = [ C ^ { { \bf g } { \bf g } } ] ^ { - 1 } .
$$

The corrections $\Delta \mathbf { g }$ and the covariance $\Gamma _ { \mathbf { g } \mathbf { g } }$ are in general not the same as in a separate global-only correction (that is, $C ^ { \bf { g } \bf { g } } \neq C _ { \bf { g } \bf { g } }$ and $\Gamma _ { \mathbf { g g } } \neq C _ { \mathbf { g g } } ^ { - 1 }$ ).

The corrections to the local parameters are found by substituting $\Delta \mathbf { g }$ from (15.4) into (15.2):

$$
\Delta { \bf h } _ { j } = C _ { { \bf h } _ { j } { \bf h } _ { j } } ^ { - 1 } \left[ D _ { { \bf h } _ { j } } - C _ { { \bf h } _ { j } \mathrm { g } } \Gamma _ { \mathrm { g g } } D _ { \bf g } + C _ { { \bf h } _ { j } \mathrm { g } } \Gamma _ { \mathrm { g g } } \sum _ { k = 1 } ^ { n } C _ { \bf g h _ { \boldsymbol { k } } } C _ { { \bf h } _ { k } { \bf h } _ { k } } ^ { - 1 } D _ { { \bf h } _ { k } } \right] .
$$

Their covariance can be deduced by comparing with the formula giving the correction by means of the full covariance matrix

$$
\Delta { \bf h } _ { j } = \Gamma _ { { \bf h } _ { j } { \bf h } _ { j } } D _ { { \bf h } _ { j } } + \Gamma _ { { \bf h } _ { j } { \bf g } } D _ { { \bf g } } + \sum _ { k \neq j } \Gamma _ { { \bf h } _ { j } { \bf h } _ { k } } D _ { { \bf h } _ { k } } ,
$$

thus the covariance matrix of the local parameters $\mathbf { h } _ { j }$ is

$$
\Gamma _ { \mathbf { h } _ { j } \mathbf { h } _ { j } } = C _ { \mathbf { h } _ { j } \mathbf { h } _ { j } } ^ { - 1 } + C _ { \mathbf { h } _ { j } \mathbf { h } _ { j } } ^ { - 1 } C _ { \mathbf { h } _ { j } \mathbf { g } } \Gamma _ { \mathbf { g } \mathbf { g } } C _ { \mathbf { g } \mathbf { h } _ { j } } C _ { \mathbf { h } _ { j } \mathbf { h } _ { j } } ^ { - 1 }
$$

and the marginal uncertainty for $\mathbf { h } _ { j }$ is larger than in a separate local solution. There are correlations between the local and the global parameters:

$$
\Gamma _ { \mathbf { h } _ { j } \mathbf { g } } = - C _ { \mathbf { h } _ { j } \mathbf { h } _ { j } } ^ { - 1 } C _ { \mathbf { h } _ { j } \mathbf { g } } \Gamma _ { \mathbf { g } \mathbf { g } } .
$$

One advantage of the multi-arc decomposition is that the normal matrix has large portions of zeros, thus it is not necessary to store the full matrix in memory. However, the covariance matrix is in fact full, that is

$$
\Gamma _ { \mathbf { h } _ { j } \mathbf { h } _ { k } } = C _ { \mathbf { h } _ { j } \mathbf { h } _ { j } } ^ { - 1 } C _ { \mathbf { h } _ { j } \mathbf { g } } \Gamma _ { \mathbf { g } \mathbf { g } } C _ { \mathbf { g } \mathbf { h } _ { k } } C _ { \mathbf { h } _ { k } \mathbf { h } _ { k } } ^ { - 1 }
$$

for all $j \neq k$ , is in general not zero (unless either $C _ { \mathbf { h } _ { j } \mathbf { g } }$ or $C _ { \mathbf { g h } _ { k } }$ is zero). In practice it may not be necessary to compute the correlations between the local parameters of different arcs, and anyway the full covariance matrix does not need to be stored.1

# Selection of the arc decomposition

Although the formalism of the previous section could be applied to an arbitrary decomposition of the observations into arcs, it is most useful when the decomposition is suggested by the distribution of the observations in time.

A satellite of the Earth is observable by each ground station only when it is above the local horizon (actually with an elevation $> 1 5 \mathrm { - 2 0 ^ { \circ } }$ above the horizon, to avoid an increased error in the tropospheric correction). The time span over which this happens is called a pass. For an interplanetary probe, the rotation of the Earth controls the pass duration (see Section 17.2). If only a few stations can be used, the observational data are naturally concentrated in the time spans of the passes, with significant gaps in between.

Let us assume that the time span of a pass is of order $d t$ , while the time span between two passes is on average $\Delta t$ . If the uncertainty in the dynamic model is $\Delta \mathbf { F }$ and $T$ is its along-track component (see Section 14.1), we use either eq. (14.5) or (14.7), depending upon the relationship between $d t$ , $\Delta t$ , and the orbital period $P$ . Anyway the spacecraft position uncertainty is $\simeq 3 / 2 \left( d t / 2 \right) ^ { 2 } T$ over one pass (assuming initial conditions at the center of the arc) and accumulates to $\simeq 3 / 2 \left( \Delta t \right) ^ { 2 } T$ during the gap between observations. If $\Delta t \gg d t$ it may well be the case that the orbit can be modeled in a deterministic way during one pass, but not over an arc encompassing two or more passes. In this case the multi-arc approach can be effective.

# 15.2 Case study: satellite laser ranging

An important example of orbit determination where the local–global decomposition provides an effective strategy is satellite laser ranging (SLR). There are satellites, such as those of the LAGEOS class, including LA-GEOS I (launched 1976) and LAGEOS II (1992), on high orbits well above the neutral atmosphere. These are passive spacecraft (without power) and covered with corner cubes to reflect back the laser pulses from the ground stations (see Figure 15.1).

The observations consist of ranges between some ground station, equipped with laser and timing equipment, and the satellite. The range is measured by the two-way light travel time divided by twice the speed of light $c$ . It is corrected for the average distance between the reflecting corner cubes and the center of mass of the satellite, for the change in speed of light in the troposphere and for the finite time spans between transmission of the pulse, reflection, and reception at the ground station. The last correction is simpler than the one used for interplanetary tracking, see Section 17.2, because of the much shorter light times, allowing us to use just low-order corrections.

![](images/1c07fbce0a0d5e07f341c974445c37283cfbdce353568d6bfdf01ff39ccb7be7.jpg)  
Fig. 15.1. The LAser GEOdynamics Satellite LAGEOS II, launched by a NASA/ASI collaboration from the Space Shuttle in 1992. It has 426 retroreflectors, each 3.8 cm in diameter.

A satellite on a high orbit, like the LAGEOS ones, has two to six passes per day on each station.2 Modern SLR ground stations can generate thousands of pulses per pass (at a frequency $\simeq 1 0$ Hz or more), out of which a good fraction can result in a range measurement. The accuracy in range has been at the few cm level since the 1980s. The total data set collected over one year contains of the order of $m \simeq 1 0 ^ { 5 }$ or more observations per station, with few tens of worldwide operational stations. Thus the accumulated data set is huge, and the ranges have a relative accuracy of the order of 1 part in $1 0 ^ { 9 }$ .

With such a dataset it is possible to solve for a large set of parameters, including dynamical parameters (to be selected taking into account the orders of magnitude discussed in the next section), the initial conditions, and kinematical parameters. The latter include at least the station coordinates, but also their time derivatives, the Earth rotation parameters, and more. It is possible to solve for all the parameters at once, but such a fit would be subject to rank deficiency and to the effects of systematic errors.

# 15.3 Perturbation model

The LAGEOS class satellites were designed with a very low area-to-mass ratio $A / M = 0 . 0 0 7 \ \mathrm { c m ^ { 2 } g ^ { - 1 } }$ and launched in a very high orbit ( $\simeq$ 6000 km above the Earth’s surface), thus at the time of the launch of LAGEOS I it was believed that the non-gravitational perturbations would be a minor issue in the orbit determination. However, thanks to the extreme accuracy of the laser tracking, it was soon discovered that the first LAGEOS was experiencing a mystery drag, that is an empirical acceleration solved to allow a good fit to the data, with an average transversal component $\overline { { T } } \simeq - 3 \times 1 0 ^ { - 1 0 }  { ~ \mathrm { c m / s ^ { 2 } } }$ . The cause of this deceleration is now interpreted as a combination of the Yarkovsky effect, charged particle drag, Earth’s reflected radiation pressure, and eclipse effects (Bertotti and Iess 1991).

A useful exercise is to list the perturbations acting on the spacecraft orbit, in order of decreasing acceleration. For the LAGEOS class satellites, Table 15.1 lists the main perturbations down to $\simeq 1 \times 1 0 ^ { - 1 0 } ~ \mathrm { c m / s ^ { 2 } }$ , from (Milani et al. 1987, Section 2.2) and (Bertotti et al. 2003b, Section 18.3). The non-gravitational perturbations contain the small quantity $A \Phi _ { \odot } / ( M c ) = F _ { P R }$ , those due to the shape of the Earth contain the coefficients $\overline { { J } } _ { \ell m } = \sqrt { \overline { { C } } } _ { \ell m } ^ { 2 } + \overline { { S } } _ { \ell m } ^ { 2 }$ . The tidal terms contain the mass of the Moon $M _ { \mathbb { Q } }$ , the Sun $M _ { \odot }$ , and the planets, the dynamic Love coefficient $k _ { 2 }$ , and the -distances. Radiation pressure and drag have specific coefficients $C _ { R }$ and $C _ { D }$ .

Table 15.1. Accelerations in $\mathrm { c m / s ^ { 2 } }$ acting on a LAGEOS class spacecraft.   

<table><tr><td>Cause</td><td>Formula</td><td></td><td>Parameter Uncertainty Value</td><td></td></tr><tr><td>Earth monopole</td><td>GM@/r² = F0</td><td>GM</td><td>2.10-9</td><td>2.8.10²</td></tr><tr><td>Earth oblateness</td><td>3F0J20R/r²</td><td>J20</td><td>7.10-8</td><td>1.0·10-1</td></tr><tr><td>Earth triaxiality</td><td>3FJ22R/r²</td><td>J22</td><td>2.10-5</td><td>6.0·10-4</td></tr><tr><td>Moon tide</td><td>2GMqr/r</td><td>GM</td><td>1:10-7</td><td>2.1· 10-4</td></tr><tr><td>Sun tide</td><td>2GMor/r</td><td>GMo</td><td>4·10-10</td><td>9.6 :10-5</td></tr><tr><td>Harmonic (6,6)</td><td>F0 7J66R/6</td><td>J66</td><td>5.10-4</td><td>8.8.10-6</td></tr><tr><td>Solid tide</td><td>3k2GMR/(r r4）</td><td>k2</td><td>2.10-3</td><td>3.7 ·10-6</td></tr><tr><td>Radiation pressure</td><td>CRFPR</td><td>CR</td><td>2.10-2</td><td>3.2 ·10-7</td></tr><tr><td>RelativisticEarth</td><td>F GM/(c² r)</td><td>GM</td><td>2.10-9</td><td>9.5 :10-8</td></tr><tr><td>Earth albedo</td><td>CR FpR (1-)R/r²</td><td>a，CR</td><td>0.2</td><td>3.4· 10-8</td></tr><tr><td>Venus tide</td><td>2FGMqr/r</td><td>GMq</td><td>3.10-7</td><td>1.3 ·10-8</td></tr><tr><td>Indirect oblation</td><td>3J20GMR/</td><td>GMq</td><td>1·10-7</td><td>1.4 · 10-9</td></tr><tr><td>Thermal emission</td><td>4/9FPRα△T/T</td><td>α,△T</td><td>0.5</td><td>4·10-10</td></tr><tr><td>Atmospheric drag</td><td>CD Apu²/(2M)</td><td>CD,p</td><td>1</td><td>1.10-10</td></tr></table>

The list is long and contains exotic effects, like the main relativistic correction due to the mass of the Earth, and indirect oblation, the perturbation of the vector from the Earth–Moon center of mass to the center of the Earth, with respect to its two-body value, due to the oblateness of the Earth affecting the orbit of the Moon. However, what really matters is not the size of the accelerations (last column in the table), but the product of the acceleration size and its relative uncertainty (the column before the last). In this way we find that there are no significant uncertainties3 down to a level of the order of $\Delta F \le 1 0 ^ { - 8 } ~ \mathrm { c m / s ^ { 2 } }$ . Below that level there is an accumulation of uncertain accelerations around a level of order $1 0 ^ { - 9 } \ \mathrm { c m / s ^ { 2 } }$ .

The analysis should focus on the perturbing accelerations with secular effects on the semimajor axis. The acceleration of the mystery drag appears as comparatively small fractions of thermal emission and Earth-reflected radiation pressure, and also as significant asymmetries of the thermal emission. An even smaller fraction of radiation pressure from the Sun may have effects along-track quadratic in time, but this requires either subtle properties of the eclipses or asymmetries in the optical properties of the two hemispheres of LAGEOS. A full discussion of the solution to the mystery drag problem is beyond the scope of this book: we shall just assume that there is a “modeling barrier” for the values of $\overline { T }$ of the order of $\Delta \overline { { T } } \simeq 1 0 ^ { - 1 0 } ~ \mathrm { c m / s ^ { 2 } }$ .

Thus, over the time span of a pass ( $d t \simeq 2 \times 1 0 ^ { 3 }$ s) the errors in orbit propagations are $\leq 3 / 2 \ : \left( d t / 2 \right) ^ { 2 } \Delta F \simeq 0 . 0 1 5 \ : \mathrm { c m }$ , while over the average interval between passes, say $\Delta t \simeq 2 \times 1 0 ^ { 5 }$ s, the propagation error can be estimated by $3 / 2 ~ \Delta t ^ { 2 } ~ \Delta { \overline { { T } } } \simeq 6$ cm. In practice, the propagation error is negligible with respect to the measurement error over one pass, and is always significant over the time span between two passes, not to speak of the effect over a longer arc. This suggests that the orbit of LAGEOS is a very suitable case for a multi-arc orbit determination.

# 15.4 Local geodesy

The simplest application of the multi-arc method to LAGEOS is obtained by assuming that the goal is to solve for the station positions (and possibly motions due, e.g., to continental drift). If the arcs are shorter than the orbital period $( \simeq 3 + 1 / 2$ hours) and the measurement accuracy is of the order of 1 cm, there is no need to solve for any dynamical parameter.

Thus the only global parameters $\mathbf { g }$ are kinematical, namely the coordinates of the vector positions ${ \bf s } _ { i } , i = 1 , y$ , of the $y$ stations contributing ranges to the satellite. These coordinates are in a body-fixed frame, rotating with the Earth in a rigid body approximation.4 This is appropriate for an orbit determination using only data from a limited time span, such as one year or less. For a solution based on data from a longer time span, the station velocities ${ \bf v } _ { i }$ need to be added to the global parameters, accounting for both local motions and continental drift effects.

The only local parameters $\mathbf { h } _ { j }$ , with $j = 1 , n$ , to be solved for each of the $n$ arcs, are the initial conditions vectors $\mathbf { z } _ { j }$ , of dimension 6, containing some set of orbital elements; we shall assume Cartesian coordinates are used, that is $\mathbf { h } _ { j } = [ \mathbf { p } _ { j } ( t _ { j } ) ; \dot { \mathbf { p } } _ { j } ( t _ { j } ) ]$ consists of three position and three velocity coordinates at some epoch $t _ { j }$ (chosen at the center of the time span of the $j$ -th arc).

# Selection of the passes and data preparation

To reduce the observed arcs to a short time span, we need to use a local network of SLR stations. Milani et al. (1995) present an experiment based on the European SLR stations ranging to LAGEOS I. The European stations are so close that an arc containing all the passes included in the same orbit lasts only about half an hour. When the arc contains only $1 - 2$ passes, the information is not enough to solve for the initial conditions; the matrix $C _ { \mathbf { h } _ { j } \mathbf { h } _ { j } }$ is not invertible, or is very badly conditioned.

Thus we select as arcs only the intervals spanning passes over three European stations in the same orbit, but there are still enough data: $\simeq 1 0 0 0$ arcs with 4.3 million ranges from seven European stations to LAGEOS I in 1985–1991. In these arcs with $\geq 3$ passes the network of ground stations behaves like a rigid body, providing a reference system for the orbit.

When the observations are closely spaced in time, the outliers can be identified by fitting all the data to smooth functions of time, such as polynomials with a degree selected to capture the useful information. The outliers can be identified by the size of the residuals, without the need for corrections (see Figure 5.4). After a number of outlier removals, the value of the kurtosis can be used as control; outlier removal should stop when the kurtosis is $\leq 3$ . A reliable procedure for a large data set can be found in (Milani et al. 1995, Section 4); the fraction of outliers was $2 . 4 \%$ .

After achieving a satisfactory polynomial fit, it is expedient to compress the data by generating normal points. They are predictions based on the polynomial model, at times selected to represent the useful information. For example, if the raw data points are uniformly spaced at equal intervals of time of size $\Delta t$ , the normal points can be computed by a new sampling at intervals $k \Delta t$ , with the $k$ such that $\nu = 2 \pi / k \Delta t$ is less than the highest frequency contained in the signal generated by the parameters being solved. If the sampling of the raw data is non-uniform, the distribution of the times of the normal points needs to account for the data gaps. Thus the observations were compressed in $\simeq 4 6 0 0 0$ normal points, which have to be used as observables, but they are correlated, that is they have a full covariance matrix. Following Section 5.3, the normal matrix of the normal points has to be computed as the inverse of the covariance and to be used as weight matrix $W$ . It is often necessary to add a component to account for the errors which are systematic, or at least with much lower frequencies.

# 15.5 Symmetries and rank deficiencies

A difficulty in this approach is rank deficiency. We shall use the method of Chapter 6: we find an exact symmetry in an approximate problem, then we show that an approximate symmetry remains in the full problem. We will also use a different approach looking directly for approximate symmetries.

To find an exact symmetry, we use as approximate equation of motion the geocentric two-body dynamics for LAGEOS; it has the group of symmetry $S O ( 3 )$ of the rotations around the Earth’s center of mass. That is, for each initial conditions $\mathbf { h } _ { j } = [ \mathbf { p } _ { j } ( t _ { j } ) ; \dot { \mathbf { p } } _ { j } ( t _ { j } ) ]$ and each matrix $R \in S O ( 3 )$ the solution $[ \mathbf { p } _ { j } ^ { \prime } ( t ) ; \dot { \mathbf { p } } _ { j } ^ { \prime } ( t ) ]$ with initial conditions $\mathbf { h } _ { j } ^ { \prime } = [ R \mathbf { p } _ { j } ( t _ { j } ) ; R { \dot { \mathbf { p } } } _ { j } ( t _ { j } ) ]$ can be obtained by rotating the original solution, that is considering $[ { \bf p } _ { j } ^ { \prime } ( t ) ; \dot { \bf p } _ { j } ^ { \prime } ( t ) ] =$ $[ R \mathbf { p } _ { j } ( t ) ; R \dot { \mathbf { p } } _ { j } ( t ) ]$ . However, when the observation equation is included, the $S O ( 3 )$ symmetry is broken. The observables are the distances $r _ { i }$ between the satellite and the $i$ -th station on the rotating Earth; if $S ( t )$ is the rotation matrix between the reference system body fixed with the Earth and the inertial system in which the orbit of the satellite is computed, then $r _ { i } ( t ) =$ $| \mathbf { p } _ { j } ( t ) - S ( t ) \mathbf { s } _ { i } |$ . If all the stations are also rotated by $R$ , that is $\mathbf { s } _ { i } ^ { \prime } = R \mathbf { s } _ { i }$ , then the distance

$$
r _ { i } ( t ) = | { \bf p } _ { j } ( t ) - S ( t ) { \bf s } _ { i } | = | R { \bf p } _ { j } ( t ) - S ( t ) R { \bf s } _ { i } |
$$

is exactly invariant if and only if $S ( t ) R = R S ( t )$ .

Let us assume that the rotation of the Earth is uniform and with a fixed axis: $S ( t ) = R _ { \Omega _ { \oplus } t }$ , where the angular velocity $\Omega _ { \oplus }$ is a constant angular velocity. Then $R$ commutes with $S ( t )$ , for every $t$ , if and only if $R$ is a rotation around the same axis $\hat { \Omega } _ { \oplus }$ . Note that this exact symmetry applies also to an Earth with non-spherical shape, provided it is axially symmetric (zonal harmonics only) with respect to the rotation axis. By inspecting Table 15.1 we find that this symmetry is very accurate even in a realistic case, the largest perturbation (due to the Earth’s equatorial ellipticity) having a relative size of a few parts in $1 0 ^ { - 6 }$ of the monopole. Moreover, by rotating the orbit by an angle $\epsilon$ in longitude $\lambda  \lambda + \epsilon$ ) the $C _ { 2 2 } , S _ { 2 2 }$ perturbations change only by a fraction $2 \epsilon$ , thus the orbit difference with respect to the exact symmetry is much smaller than 1 cm, even for rotation angles affecting the station positions by a length $\epsilon R _ { \oplus }$ of hundreds of meters.5

We conclude that at least one constraint needs to be applied to avoid an approximate rank deficiency: it can be obtained by fixing the longitude of one station, or better the longitude of the barycenter of the local network. In fact, numerical experiments on short-arc orbit determination with distances only (Milani and Melchioni 1989) show that there is an approximate rank deficiency of order four, that is three more than what is explained by the symmetry discussed above.

There is no way to find other exact symmetries, in particular to recover the $S O ( 3 )$ symmetry group, unless we assume not only a spherical Earth but also that the Earth-fixed network of stations is non-rotating ( $S ( t )$ i s constant in time). However, this is by no means an approximation, since the distances have relative changes of order unity with respect to the realistic case. Nevertheless the rotation of the Earth, although it affects the observables $r _ { i } ( t )$ , has a reduced effect over one arc which is short enough. This occurs because the time span over which the orbit has to be propagated within a single arc ( $d t / 2 \simeq 1 0 0 0 ~ \mathrm { s }$ ) is short with respect to one day, that is the Earth rotation angle over the time $d t / 2$ is just $\eta = 0 . 0 7 3$ radians.

We look at the orbit determination problem in a body-fixed reference system,6 in which the ground stations are not moving (besides the tidal and continental drift effects). Then the equation of motion contains the apparent Coriolis and centrifugal accelerations (see Section 16.1):

$$
\mathbf { F } _ { a p p } ( \mathbf { p } _ { j } ( t ) , \dot { \mathbf { p } } _ { j } ( t ) ) = - 2 \boldsymbol { \Omega } _ { \oplus } ( t ) \times \dot { \mathbf { p } } _ { j } ( t ) - \boldsymbol { \Omega } _ { \oplus } ( t ) \times [ \boldsymbol { \Omega } _ { \oplus } ( t ) \times \mathbf { p } _ { j } ( t ) ] .
$$

Let $R$ be a small rotation, that is $R = I + Z + \cdots$ , where $Z$ is the infinitesimal rotation by small angles $\mathcal { O } ( \epsilon )$ , represented by an antisymmetric matrix ( $Z ^ { T } = - Z$ ), and the dots stand for $\mathcal { O } ( \epsilon ^ { 2 } )$ terms. In the spherical Earth approximation, the equation of motion changes only by

$$
\begin{array} { r l } & { \mathbf { F } _ { a p p } ( R \mathbf { p } _ { j } ( t ) , R \dot { \mathbf { p } } _ { j } ( t ) ) - \mathbf { F } _ { a p p } ( \mathbf { p } _ { j } ( t ) , \dot { \mathbf { p } } _ { j } ( t ) ) } \\ & { \quad = - 2 \pmb { \Omega } _ { \oplus } ( t ) \times Z \dot { \mathbf { p } } _ { j } ( t ) - \pmb { \Omega } _ { \oplus } ( t ) \times [ \pmb { \Omega } _ { \oplus } ( t ) \times Z \mathbf { p } _ { j } ( t ) ] + \mathcal { O } ( \epsilon ^ { 2 } ) . } \end{array}
$$

The main centrifugal term can have a significant along-track component. It can be estimated in size as $\leq \Omega _ { \oplus } ^ { 2 } p _ { j } \epsilon$ , thus its orbital effect over $d t / 2$ i s estimated by $\leq 3 / 2 a \eta ^ { 2 } \epsilon$ , where $a$ is the semimajor axis of LAGEOS, to be compared with station displacements $\epsilon R _ { \oplus }$ . With $a \simeq 2 R _ { \oplus }$ we find that the ratio (orbit change)/(stations displacement) is estimated as $\leq 3 \eta ^ { 2 } \simeq 0 . 0 1 5$ . For example, for $\epsilon \simeq 1 0 ^ { - 7 }$ the stations are displaced by 60 cm and still the rotated orbit is distorted by no more than 1 cm.

The Coriolis term for a circular orbit has zero along-track component, thus it affects much less the orbit of LAGEOS; it can be estimated as $\leq$ $2 \Omega _ { \oplus } \dot { p } _ { j } \epsilon$ , and the orbital effect over $d t / 2$ cannot exceed $3 e \eta n d t / 2 \epsilon a$ , with $e , n$ the eccentricity and mean motion of LAGEOS, which is even smaller than for the centrifugal term. Another acceleration breaking the symmetry for rotations displacing the pole is due to the Earth’s oblateness. It changes by a relative amount $\leq 2 \epsilon$ , thus for $\epsilon = 1 0 ^ { - 7 }$ the acceleration difference is $\simeq 2 \times 1 0 ^ { - 8 } ~ \mathrm { c m / s ^ { 2 } }$ , again not important over 1000 s. Thus we have identified approximate symmetries, although the corresponding exact symmetries (for $\eta = 0$ ) are not an approximation of a realistic problem.

The last approximate symmetry is well known to specialists of geodesy (both satellite and ground based): the geodetic network formed by the SLR stations can experience a lift, i.e., a translation away from the center of the Earth, by an amount $d$ , provided the initial positions $\mathbf { p } _ { j } ( t _ { 0 } )$ of the satellite are also translated in the same direction (for all $j$ ). Then the change in the two-body acceleration on the satellite is $\simeq 2 \left( G M _ { \oplus } / a ^ { 2 } \right) \left( d / a \right)$ . For example, for a $1 \textrm { m }$ lift, $d / a \simeq 1 0 ^ { - 7 }$ implies $| \Delta F _ { 0 } | \simeq 4 \times 1 0 ^ { - 5 } \ \mathrm { c m / s ^ { 2 } }$ . Taking into account that the monopole gives a small contribution to the along-track perturbation $T$ , the change in the orbit over 1000 s is much less than 1 cm.

# Constraints and rigidity of the network

The four constraints required to avoid approximate rank deficiencies could be described as fixing to their initial value the three coordinates of the barycenter of the stations network, and inhibiting the rotations around the geocenter–barycenter axis.7 They can be obtained with the a priori observation formalism of Section 6.1. Let ${ \bf s } _ { i } ^ { ( 0 ) } , i = 1 , y$ , be the initial values of the station coordinates; the barycenter coordinates are observed with uncertainty $\sigma$

$$
\sum _ { i = 1 } ^ { y } \frac { { \bf s } _ { i } - { \bf s } _ { i } ^ { ( 0 ) } } { y } = N ( { \bf 0 } , \sigma ^ { 2 } I ) ,
$$

that is, the probability density of the deviations from this a priori constraint is a Gaussian distribution with zero mean and covariance matrix $\sigma ^ { 2 } I$ ( $I$ is

a $3 \times 3$ identity matrix). The corresponding normal equation (6.3)

$$
\sum _ { i = 1 } ^ { y } \frac { \mathbf { s } _ { i } } { y \sigma ^ { 2 } } = \sum _ { i = 1 } ^ { y } \frac { \mathbf { s } _ { i } ^ { ( 0 ) } } { y \sigma ^ { 2 } }
$$

is added to the normal equation from the real observations. To inhibit rotations around the barycenter ${ \bf b } = \sum { \bf s } _ { i } ^ { ( 0 ) } / y$ we use an a priori constraint

$$
{ \frac { 1 } { K } } \sum _ { i = 1 } ^ { y } \mathbf { b } \times ( \mathbf { s } _ { i } ^ { ( 0 ) } - \mathbf { b } ) \cdot ( \mathbf { s } _ { i } - \mathbf { b } ) = 0
$$

with ${ \mathrm { R M S } } = \sigma$ and $\begin{array} { r } { K = \sum _ { i = 1 } ^ { y } | \mathbf { b } \times ( \mathbf { s } _ { i } ^ { ( 0 ) } - \mathbf { b } ) | } \end{array}$ ; the normal equation is

$$
{ \frac { 1 } { K } } \sum _ { i = 1 } ^ { y } \mathbf { b } \times ( \mathbf { s } _ { i } ^ { ( 0 ) } - \mathbf { b } ) \cdot \mathbf { s } _ { i } = { \frac { 1 } { K } } \sum _ { i = 1 } ^ { y } \mathbf { b } \times ( \mathbf { s } _ { i } ^ { ( 0 ) } - \mathbf { b } ) \cdot \mathbf { b } .
$$

To impose a tight constraint, a small value of $\sigma$ is used, e.g., $\sigma = 0 . 1$ for coordinates expressed in cm, thus the constraints have to be satisfied at the mm level. To assess the relevance of the approximate rank deficiency, the constraint is weakened to the meter level, with $\sigma = 1 0 0$ .

# Stability test

In (Milani et al. 1995) the stability of the solution is tested by splitting the data set (ranges from seven stations during one year) into two halves, formed by the odd and even arcs, numbered in order of time. With $\sigma = 0 . 1$ , the RMS of the differences between the station coordinates in the two “half” solutions is 1.63 cm. The component of rigid motion contained in the differences has $\mathrm { R M S } = 0 . 3 9 ~ \mathrm { c m }$ ; this is due to the two remaining degrees of freedom in the group of rigid motions, the tilt along axes passing from the barycenter $\mathbf { b }$ . The instabilities which are deformations of the network have $\mathrm { R M S } = 1 . 5 8$ cm, thus the constraints are effective. If the constraints are relaxed with $\sigma = 1 0 0$ , the RMS of the coordinate differences grows to 72.5 cm.

The accuracy of such a local geodetic network, obtained many years ago, was such that in a solution with seven years of data (1985–1991) the same “two halves” stability test gave a RMS of the station position differences of 0.58 cm, with only 0.19 of RMS tilt. The differences in the stations’ velocities had RMS = 0.32 cm/year, of which only 0.06 of tilt. In a solution including station velocities as global parameters, the number of constraints has to be increased to eight, inhibiting a translation velocity of the barycenter and a uniform rotation around the geocenter–barycenter axis.

# 16 SATELLITE GRAVIMETRY

In this chapter we deal with the problem of solving for the gravity field of a planet without degradation of the results due to non-gravitational perturbations. This problem is severe for low orbits around a planet with an atmosphere, like the Earth, because atmospheric drag sharply increases when the orbit altitude decreases. Even around planets without atmosphere, like Mercury, low orbits are much more affected by reflected and infrared radiation pressure from the planet’s surface (see Section 17.3). Thus we need to estimate how low the spacecraft needs to orbit, to be sensitive to the portion of the gravity field we wish to measure. Let us suppose the spacecraft is in a nearly circular orbit at an altitude $h$ above the surface of a planet with equatorial radius $R$ . The potential due to a spherical harmonic of degree $\ell$ and order $m$ is

$$
{ \frac { G M } { r } } \ \left( { \frac { R } { r } } \right) ^ { \ell } \ { \overline { { Y } } } _ { \ell m i }
$$

times the coefficient $\overline { { C } } _ { \ell m }$ for $i = 1$ , $S _ { \ell m }$ for $i = 0$ (see Chapter 13). Since $r = R + h$ , if we assume that $h$ coincides with the spatial scale of the harmonic, that is half of the smallest spatial wavelength, from the Kaula expansion (13.32) we have $h = \pi R / \ell$ and

$$
\left( { \frac { R } { r } } \right) ^ { \ell } = \left( 1 + { \frac { h } { R } } \right) ^ { \ell } = \left( 1 + { \frac { \pi } { \ell } } \right) ^ { - \ell } , \operatorname* { l i m } _ { \ell \to + \infty } \left( 1 + { \frac { \pi } { \ell } } \right) ^ { - \ell } = { \frac { 1 } { \exp ( \pi ) } } \simeq { \frac { 1 } { 2 3 . 1 } }
$$

that is, for $h$ equal to the spatial scale, the ratio of the monopole potential to the harmonics with high degree $\ell$ is essentially independent of $\ell$ and is close to the irrational number $\exp ( \pi )$ . For higher orbits, say $h = k \pi R / \ell$ , the ratio becomes $\exp ( \pi ) ^ { k }$ and the gravity signal sharply decreases as $k$ grows.

If we assume the gravity field is measured from the potential, good sensitivity can be obtained by keeping the altitude of the order of the spatial scale. One way to increase sensitivity is to measure derivatives of the potential: for the second radial derivative the sensitivity is increased by a factor $( \ell + 1 ) ( \ell + 2 ) / 2$ ; however, for $\ell = 1 0 0$ this only corresponds to $k \simeq 2 . 7$ .

In conclusion, if a gravimetry mission targets a short spatial scale, just a few times the scale height of the atmosphere, drag is a critical problem. For example, for the Earth $\ell \simeq 2 0 0$ (scale $\simeq 1 0 0$ km) can be reached only with equipment to neutralize the effect of drag. Such equipment is described, from the point of view of its impact on the orbit determination, in the next section.

# 16.1 On-board instrumentation

We list the instruments which could be used to neutralize the effect of nongravitational perturbations, with their advantages and problems.

# Navigation systems

On the surface of the Earth, navigation instruments provide accurate positioning, in the reference system defined by a satellite constellation, such as GPS, GLONASS, Galileo. The versions used on satellites in low Earth orbit provide information equivalent to a position every few seconds.

The position of the low satellite is not measured instantaneously: the phases received from the navigation satellites can be fitted to a reduced dynamics orbit, the solution of a simplified equation of motion, containing as free parameters initial conditions and some empirical acceleration, to absorb both the non-gravitational effects and the inaccuracies in the gravity field model. That is, spacecraft positioning is an orbit determination problem with an overwhelming amount of data, such that very short arcs (a few minutes) can be used and still tightly constrain the orbit. In practice, with state-of-the-art space-borne GPS navigators,1 we can assume that the orbit of a low satellite is known to a few centimeters at all times.

There are different ways to include the navigation data in the orbit determination. One way is a brute force method: a least squares fit with all the observables from navigation and the other instruments, and the equation of motion containing all the parameters (geopotential coefficients, initial conditions, and more). This can be used, but the same accuracy may be achieved by using methods with lower computational complexity, see Section 16.3.

More efficient is a kinematic method, in which the orbit determination is split into two steps. In the first step, the precision orbit determination (POD), the time series of spacecraft positions is determined by using the navigation data only. Since the non-gravitational perturbations are absorbed by the empirical accelerations, in the POD there is no need to use the data from on-board accelerometers. In the second step the other parameters are determined by using as observables the spacecraft positions and/or the measurements of the other instruments.2 The uncertainty of the positions from the POD has to be taken into account, but this is not the main source of error. Anyway, it is possible to iterate, by using the improved gravity field and the calibrated accelerometer data (see below) from the second step for the POD, replacing the empirical accelerations.

# Accelerometers

An accelerometer measures the relative acceleration of a sensitive element with respect to the instrument rigid frame. The sensitive element position needs to be controlled by a feedback loop, in such a way that it does not undergo any large-scale motion with respect to the frame; the amount of these corrections, actuated by electrostatic forces, is the actual measurement.

Two technologies are currently used for accelerometers. In the electrostatic accelerometer the sensitive element is a conductive mass levitating inside a cavity of capacitors. One sensitive element is enough to measure a vector acceleration. The main limitation is that the levitation is hard to be maintained with the same equipment on the ground and in space, thus testing on the ground is limited and expensive space-borne tests are needed.3

The alternative is a spring accelerometer, in which the sensitive element is free to move only along an axis, with a spring as restoring force and electrostatic forces as controls. Three separate units, with orthogonal axes, measure an acceleration vector, but this complexity is somewhat compensated by the ease of testing on the ground: each unit can be tested in a micro-gravity environment by orienting it normal to the local gravity field.

In fact, there are two main limitations to the use of accelerometers in a very accurate orbit determination. First, an accelerometer anyway provides only a relative measurement; the electrical quantities corresponding to a zero acceleration are simply not known, and ground tests would provide values different from those applicable in space.4 Thus accelerometers measure only changes, over limited time spans, of the accelerations. Second, there is no way to build an accelerometer which does not act also as a thermometer, that is the reading is a function of both acceleration and temperature.

In conclusion, spring accelerometers are robust and reliable, but they do not reach the same accuracy as the electrostatic ones because they are generally more temperature sensitive. Thus at present the electrostatic accelerometers are used for the top accuracy satellite gravimetry missions around the Earth, while the spring ones are used for the gravimetry of other planets.

# Apparent accelerations

The purpose of orbit determination for satellite gravimetry is not to determine the position of any specific point on the spacecraft, but to locate some point for which we can write an equation of motion, containing the dynamic parameters: the equation for the spacecraft center of mass (CoM) $\mathbf { x }$ is

$$
\ddot { \mathbf { x } } = \nabla U ( \mathbf { x } ) + \mathbf { a } _ { n g } ,
$$

where $U$ is the gravitational potential and $\mathbf { a } _ { n g }$ the non-gravitational acceleration. The non-gravitational forces act on the external surface of the spacecraft, and assuming the accelerometer frame is attached to a rigid spacecraft structure including the surface, the accelerometer cage is accelerated by $\mathbf { a } _ { n g }$ , the sensitive element does not feel this acceleration, and the instrument measures the apparent acceleration −ang.

However, the accelerometer cannot be placed exactly at $\mathbf { x }$ , but at some position displaced by the vector $\mathbf { Y }$ from the CoM in a spacecraft fixed reference system; let $\mathbf { y } = R \mathbf { Y }$ be the same displacement in the inertial system, with $R$ a time-dependent rotation. The accelerometer velocity in an inertial frame is

$$
{ \dot { \mathbf { y } } } = { \dot { R } } R ^ { T } \mathbf { y } + R { \dot { \mathbf { Y } } } = { \boldsymbol { \omega } } \times \mathbf { y } + R { \dot { \mathbf { Y } } }
$$

with $\omega$ the angular velocity (Arnold 1976). The inertial acceleration is

$$
\ddot { \mathbf { y } } = [ \boldsymbol { \omega } \times ( \boldsymbol { \omega } \times \mathbf { y } ) + \dot { \boldsymbol { \omega } } \times \mathbf { y } ] + 2 \boldsymbol { \omega } \times R \dot { \mathbf { Y } } + R \ddot { \mathbf { Y } } = \mathbf { a } _ { r o t } + \mathbf { a } _ { \mathbf { Y } }
$$

where the part inside square brackets is the rotation acceleration $\mathbf { a } _ { r o t }$ of the accelerometer, and aY is the acceleration due to a possible drift of the CoM in the spacecraft frame, due to either movable parts or fuel consumption. Both are applied by solid state forces on the accelerometer cage.

Moreover, the accelerometer sensitive element is accelerated by the gravity field $\nabla U ( { \bf x } + { \bf y } )$ , while the cage is accelerated by the gravity field at the CoM: thus the accelerometer also measures a gravity gradient acceleration. This acceleration can be computed, neglecting $\mathcal { O } ( | \mathbf { y } | ^ { 2 } )$ terms, from the matrix of second derivatives of the gravitational potential $U$ :

$$
{ \bf a } _ { g g } ( { \bf y } ) = \frac { \partial ^ { 2 } U } { \partial { \bf x } ^ { 2 } } ( { \bf x } ) { \bf y } .
$$

Thus there are differential accelerations, functions of $\mathbf { y }$ , while $\mathbf { a } _ { n g }$ does not depend upon $\mathbf { y }$ , and the accelerometer measures the combination

$$
\mathbf { a } _ { a c c } ( \mathbf { y } ) = - \mathbf { a } _ { n g } - \mathbf { a } _ { r o t } ( \mathbf { y } ) - \mathbf { a } _ { \mathbf { Y } } + \mathbf { a } _ { g g } ( \mathbf { y } )
$$

where the minus sign applies to accelerations acting on the cage, plus when acting on the sensing element directly. The equation of motion of the CoM using the accelerometer is obtained by substituting (16.3) into (16.1):

$$
\ddot { \mathbf { x } } = \nabla U ( \mathbf { x } ) - \mathbf { a } _ { a c c } - \mathbf { a } _ { r o t } ( \mathbf { y } ) - \mathbf { a } _ { \mathbf { Y } } + \mathbf { a } _ { g g } ( \mathbf { y } ) .
$$

It is possible to compute the equation of motion for the accelerometer $\mathbf x + \mathbf y$ by adding eq. (16.4) to (16.2), with cancellation of $\mathbf { a } _ { r o t } , \mathbf { a } _ { \mathbf { Y } }$

$$
\ddot { \mathbf { x } } + \ddot { \mathbf { y } } = \nabla U ( \mathbf { x } ) - \mathbf { a } _ { a c c } + \nabla \left( \nabla U \right) ( \mathbf { x } ) \mathbf { y } = \nabla U ( \mathbf { x } + \mathbf { y } ) - \mathbf { a } _ { a c c }
$$

with the surprising result that, when using the data from the accelerometer as a term in the equation of motion, the equations of motion for the accelerometer are simpler than those for the CoM.5

The above presentation is somewhat simplified: care needs to be taken of three points. First, the tracking instruments are neither in $\mathbf { x }$ nor in $\mathbf { x } + \mathbf { y }$ , but have some other reference point (e.g., the antenna phase center) displaced by a vector $\mathbf { Z }$ in spacecraft axes from the CoM. If the tracking data are spacecraft positions, they refer to ${ \bf x } + { \bf z }$ (where ${ \bf z } = R { \bf Z }$ ) and have to be corrected by subtracting $\mathbf z - \mathbf y$ ; on the other hand, $\mathbf { Z } - \mathbf { Y }$ is better known than $\mathbf { Z }$ , since the position of the CoM inside the spacecraft structure may depend upon the poorly known content of fuel in the tanks. If the tracking data are range and/or range-rate, corrections containing $\mathbf z - \mathbf y$ and ${ \dot { \mathbf { z } } } - { \dot { \mathbf { y } } }$ , respectively, have to be applied, and the requirements on the knowledge of $\mathbf { Z } - \mathbf { Y }$ and $\dot { \mathbf { Z } } - \dot { \mathbf { Y } }$ are severe for state-of-the-art tracking systems (see Chapter 17).

Second, for an electrostatic accelerometer there is really a single sensitive reference point, the CoM of the levitating mass. For a spring accelerometer, there are three separate sensitive points $\mathbf { Y } _ { i }$ , $i = 1 , 2 , 3$ , with mutual distances of several cm which cannot be ignored. The solution is to select a conventional reference point $\mathbf { Y }$ in the accelerometer structure, then correct the readings of the three channels for the displacements $R \left( \mathbf { Y } _ { i } - \mathbf { Y } \right)$ , with $\mathbf { Y } _ { i } - \mathbf { Y }$ well known (and presumably constant).

Third, this discussion assumes that the rotation state, not just $R$ but also $\omega$ and $\dot { \omega }$ , are well known. In reality there will be a contribution from the knowledge of these quantities in the error budget. Experience shows that the corresponding requirements on the attitude control subsystem need to be clearly specified at an early stage in the design of the space mission.

# Calibration

The relationship between the measured electrical quantity $q$ and the actual acceleration $a _ { a c c }$ for each accelerometer sensitive element is of the form

$$
a _ { a c c } = a q + b T + c + \cdot \cdot \cdot
$$

where $a$ is the scale calibration, $T$ the local temperature, $b$ the thermal sensitivity, $c$ the absolute calibration, and the dots stand for the nonlinear effects, typically negligible provided the accelerometer dynamic range is not exceeded. The above formula is for an instrument with a single sensitive axis; for a three-axis accelerometer there are three such formulae.6

The scale calibration can be measured by a known acceleration: internal calibration with an ad hoc electrostatic force and external calibration with, e.g., the planet monopole gravity gradient, or the apparent force from spacecraft rotation. The thermal sensitivity can be measured on the ground.

The most critical calibration is the absolute one, for which a dedicated calibration device and/or procedure would be very difficult. Thus one key issue of this chapter will be the a posteriori calibration, that is the determination of the values of $c$ as part of the orbit determination problem. The only information we have on $c$ is that it changes slowly with time, but how slowly we do not know yet: every ground based laboratory is affected by too much acceleration noise, thus tests in space are the only possibility.7 We conclude that $c$ needs to be determined as three constants for each observed arc, possibly even as coefficients of interpolation models for each arc, depending upon the arc time span, see Section 17.6 and 16.3, respectively.

# Drag free missions

A drag free spacecraft uses an accelerometer coupled to the orbit control subsystem with a feedback loop, such that the measured accelerations $\mathbf { a } _ { a c c }$ are controlled to zero by thrusting. Ideally, the sensitive element of an electrostatic accelerometer should follow a purely gravitational orbit. The discussions above, on the measurements not being at the CoM and about calibration, make clear that this ideal condition can be realized only roughly. In particular it is difficult to obtain the absolute calibration in real time.

Nevertheless, an approximate drag free system may be necessary. A high spatial resolution gravimetry mission around the Earth needs to orbit where drag is significant, and two problems arise. The first is the mission duration, which could be cut short by orbital decay unless the drag is compensated by thrust: a solution is to have an orbit which is drag free, but only on average, e.g., impulsive thrust used when necessary.

The second problem is the accelerometer saturation: to ensure linearity of the calibration (16.6), the acceleration measured needs to be controlled, and this is a requirement applicable at all time, implying a drag free system with continuous thrust. The measured $\mathbf { a } _ { a c c }$ does not need to be controlled to the accelerometer sensitivity, but below the saturation level, at least $1 0 ^ { 3 }$ times larger. For a low satellite experiencing significant drag, an effective strategy is to have continuous thrust along a single direction, opposite to the velocity, controlling the low-frequency portion of the deceleration. Lift and radiation pressure accelerations (acting in different directions) do not need to be controlled, and the motion of the accelerometer reference point follows eq. (16.5), with $\mathbf { a } _ { a c c }$ including the apparent force due to thrust.

# Gradiometers

A very powerful instrument for gravimetry missions is a gradiometer, directly measuring some second derivatives of the potential. It contains a number of accelerometers, electrically coupled in such a way that the differences of the accelerations are directly measured. A gradiometer is particularly effective when coupled to a navigation system; then the orbit can be considered known, and the differences in acceleration are linearly related to the gravity gradient matrix $\partial ^ { 2 } U / \partial \mathbf { x } ^ { 2 }$ , e.g.,

$$
\frac { d ^ { 2 } U } { d r ^ { 2 } } = \frac { \frac { \partial U } { \partial r } ( \mathbf { x } + d / 2 \mathbf { r } ) - \frac { \partial U } { \partial r } ( \mathbf { x } - d / 2 \mathbf { r } ) } { d } + \mathcal { O } ( d / r ) ,
$$

where the $\mathcal { O } ( d / r )$ term is typically below the instrument sensitivity.

The calibration of gradiometers is not very different from that of accelerometers, with one equation (16.6) for each differential measurement, where the temperature $T$ is replaced by the difference in temperature between the two units. Thus the temperature needs to be controlled only in a relative sense: if all the accelerometers are contained in a well-insulated container, the thermal correction can be much smaller. The gradiometers are used to increase sensitivity to short spatial scales; the time-scale over which the signal changes can be short, e.g., for $\ell \simeq 2 0 0$ the shortest period is $< 3 0$ s, but the longest period from the $\ell - 2 p = 2$ term is $> 2 7 0 0$ s, see (13.38). Thus the critical issue is the a posteriori calibration, discussed in Section 16.3.

# Apparent accelerations

The question is how many accelerometers, and how many independent measurements of components of $\partial ^ { 2 } U / \partial \mathbf { x } ^ { 2 }$ , are to be used. The apparent acceleration $\mathbf { a } _ { r o t }$ is linear in the positions ${ \bf y } _ { i }$ of the accelerometers, and so is $\mathbf { a } _ { g g }$ . Thus no matter where the CoM is, the differential apparent accelerations can be computed by using the relative positions ${ \bf y } _ { i } - { \bf y } _ { j }$ . If the gravimeter can be considered as a rigid body, there is no Coriolis term. The centrifugal apparent acceleration can be obtained from a potential $W$ :

$$
- { \boldsymbol { \omega } } \times [ { \boldsymbol { \omega } } \times ( \mathbf { y } _ { i } - \mathbf { y } _ { j } ) ] = \nabla \left[ { \frac { 1 } { 2 } } ~ | { \boldsymbol { \omega } } | ^ { 2 } ~ | \Pi ( \mathbf { y } _ { i } - \mathbf { y } _ { j } ) | ^ { 2 } \right] = \nabla W
$$

where $\Pi$ is the projection on the plane orthogonal to the angular velocity $\omega$ . Then the matrix of second derivatives measured by the gradiometer is in fact $\partial ^ { 2 } ( U + W ) / \partial { \bf x } ^ { 2 }$ . $U$ satisfies the Laplace equation, thus

$$
\Delta ( U + W ) = \Delta W = 2 | \omega | ^ { 2 } .
$$

If the knowledge of the rotation state (from the attitude control subsystem) is good enough, each differential measurement can be corrected for the centrifugal term.8 However, the gradiometer could be better in measuring rotation than the attitude control; then the accuracy would be limited by the errors in the centrifugal term. A solution is to measure all three diagonal components of $\partial ^ { 2 } ( U + W ) / \partial { \bf x } ^ { 2 }$ and compute $| \omega | ^ { 2 }$ from the formula above: this requires two accelerometers along each of the three orthogonal axes, and leaves only two diagonal components independently measured.

# 16.2 Accelerometer missions

An accelerometer mission for gravimetry could have just two instruments: an accelerometer and a navigation system. The orbit determination can be decomposed into two steps. The first is the POD, using the phases from the navigation satellites and solving for the satellite positions (with empirical accelerations absorbing the dynamic model errors).

There are several ways to define the second step. We shall use as an example the method used in a simulation of one such mission, the Italian Space Agency project SAGE (Albertella and Migliaccio 1998). In this approach, the second step uses as observables the three coordinates of the satellite, and has to solve for a large set of parameters, including the harmonic coefficients and the initial conditions for each arc. The latter are also determined by the navigation, but with an accuracy insufficient to solve for the gravity field.

A simple formula to estimate the maximum arc time span uses the assumption that the accelerometer measurements only contain noise, with known constant spectral density $\Delta A$ . If $x _ { T }$ is the coordinate of the satellite position $\mathbf { x }$ in the transverse direction at the extremes of an arc time span $P$

$$
\mathrm { R M S } ( x _ { T } ) = 2 \Delta A \ ( P / 2 ) ^ { 3 / 2 } .
$$

For example, if $\Delta A \ = \ 3 \times 1 0 ^ { - 6 } \ \mathrm { c m } \ \mathrm { s } ^ { - 2 } \ \mathrm { H z } ^ { 1 / 2 }$ and the positions from navigation have an $\mathrm { R M S } > 1$ cm, the random error due to accelerometer noise is less, even for arcs covering an orbital period (5560 s for $h = 4 0 0 { \mathrm { k m } }$ ). This is an optimistic estimate of the orbit errors due to the accelerometer (calibration errors have a larger effect), giving just an upper bound for the arc time span. Still, this estimate has severe implications; e.g., for a six months simulation, with arcs of $1 / 2$ orbital period, there are $\simeq 5 5 0 0$ arcs, thus $\simeq 3 3 0 0 0$ initial conditions. If the target is to solve for the 8281 coefficients up to degree and order 90, the dimension of the normal/covariance matrix is $\simeq 4 1 3 0 0$ . This strongly suggests the decomposition of the normal equation.

# Local–global decomposition

The local–global decomposition of Section 15.1 can be used as a solution to the problem of a too large normal matrix. If we can neglect the a priori correlation between initial conditions of different arcs, this method allows us to invert $\simeq 5 5 0 0$ matrices $C _ { \mathbf { h } _ { i } \mathbf { h } _ { j } }$ which are just $6 \times 6$ matrices if the local parameters are just the initial conditions, somewhat larger, e.g., $9 \times 9$ , if accelerometer calibration parameters are also estimated for each arc. Then the solution for the harmonic coefficients $\mathbf { g }$ are obtained by inverting a matrix $\mathrm { 8 2 8 1 \times 8 2 8 1 }$ , by using eq. (15.4). Also the equations for $\mathbf { g }$ can be decomposed by resonant decomposition, see Section 13.5.

![](images/efeefd4c6917c1f561a5cd85e1bd26592b8ebf6cdaa45e32ebc66444af76da6d.jpg)  
Fig. 16.1. A simulation of the SAGE gravimetry mission. The smooth curves plotted as RMS values ( $\log _ { 1 0 }$ scale) for each harmonic degree $\ell$ , from top to bottom on the left, are: the expected values of the coefficients according to the Kaula rule; the formal RMS of the results taking into account local–global correlations; the same RMS neglecting them. The jagged curve is the actual error with local–global correlations, the dotted one the actual error neglecting them.

The SAGE simulations provided a numerical experiment on the quantitative aspects of the local–global decomposition. The covariance matrix of the global parameters $\Gamma _ { \mathbf { g } \mathbf { g } }$ is not the inverse of the normal matrix $C _ { \mathbf { g } \mathbf { g } }$ , but of another matrix $C ^ { \mathrm { { g g } } }$ defined by eq. (15.3), which is obtained by subtracting from $C _ { \mathbf { g } \mathbf { g } }$ a matrix with non-negative eigenvalues. This implies that $C ^ { \mathrm { { g g } } } < C _ { \mathrm { { g g } } }$ , by which we mean that for each vector $\Delta \mathbf { g }$

$$
\Delta \mathbf { g } \cdot C ^ { \mathbf { g g } } \Delta \mathbf { g } \leq \Delta \mathbf { g } \cdot C _ { \mathbf { g g } } \Delta \mathbf { g } .
$$

Now $\Delta \mathbf { g } \cdot C ^ { \mathbf { g } \mathbf { g } } \Delta \mathbf { g } = \sigma ^ { 2 }$ is a confidence ellipsoid for the global parameters $\mathbf { g }$ , and the above inequality implies that the confidence ellipsoids with matrix $C _ { \mathbf { g } \mathbf { g } }$ would be smaller (for the same $o$ ). Ignoring the local–global correlations, and replacing the marginal covariance matrix of $\mathbf { g }$ (for whatever local parameters $\mathbf { h }$ ) with the conditional covariance matrix of $\mathbf { g }$ (for $\mathbf { h }$ kept fixed) gives an optimistic assessment of the accuracy of the results (see Section 5.4).

Figure 16.1 shows the results of a simulation, for a six-month mission, with and without the local–global terms $C _ { \mathbf { h } _ { j } \mathbf { g } }$ . The difference between the two cases is dramatic: neglecting the local–global terms gives an illusory accuracy estimate, by more than two orders of magnitude in the RMS values. In this example, using the conditional covariance of $\mathbf { g }$ would give the impression that the coefficients up to degree and order 90 can be estimated with a S/N ratio $> 1 0$ , while in fact $\mathrm { S } / \mathrm { N } > 1$ is possible only up to degree $\simeq 6 0$ . Moreover, the actual error (difference between the ground truth value used in the simulation and the obtained solution) is larger.

The SAGE simulations were simplified (the initial conditions were the only local parameters), but the conclusions on the need of a full solution for all parameters still stand. With more local parameters (for accelerometer calibration) the local–global terms would have an even bigger impact.

# 16.3 Gradiometer missions

A gradiometer mission could have just two instruments, a navigation system and a gradiometer, but the latter is large and complex; as shown in Section 16.1, six accelerometers are required. Since at present electrostatic three-axis accelerometers are used (ESA 1999), there are 18 accelerometer channels, and the measurement procedure has a complexity which we are not going to discuss. To allow for a self-contained discussion of the gravity field solution with a gradiometer we use two simplifying assumptions. First, the spacecraft position is determined by the navigation, in a POD independent from the accelerometer data. Second, we assume that the differential measurements from the accelerometer channels are summarized in independent measurements of two out of three diagonal terms of $\partial ^ { 2 } U / \partial \mathbf { x } ^ { 2 }$ , the effect of apparent accelerations having been removed by pre-processing (the errors in this procedure contribute to the error model). The gradiometer calibrations are summarized as two slowly varying functions of time.

A basic choice is the organization of the gravimetry observations in one of three possible ways. In a spacewise method the data points are ordered by their position in space, in a reference frame rotating with the Earth; this is a sampling of gravity around a geocentric sphere (a thin shell if the orbit is almost circular). The advantage is that most of the gravitational signal to be determined is also organized spatially, although there are time-dependent signals due to tides and other deformations. In a timewise method the data points are considered as a discretized time series. This is a less natural way of looking at the static gravity: indeed, each spherical harmonic appears as a sum of signals with different frequencies, by eq. (13.36). The advantage of the timewise methods is in the treatment of the gradiometer calibrations. In a frequencywise method the time series of the gradiometer data are Fourier transformed into the frequency domain: the effect of each spherical harmonic is represented by a Fourier polynomial and the fit can be directly performed in the frequency space. If each harmonic is solved independently, the computational cost is low: this method is used in the mission design phase, to convert requirements in the error spectrum of the gradiometer into an error spectrum of the recovered gravity. However, the correlations between the harmonics have to be taken into account sooner or later, see Section 16.5.

These three approaches are equivalent for a perfect distribution of data. With a spatial distribution uniform on a sphere and a time distribution uniform over an unlimited time span there is a well conditioned one-to-one correspondence between spherical harmonics, a linear subspace of the signal as function of time, and its discrete spectra. However, such uniformities are impossible in real missions, and there are superpositions between the frequencies of the gravitational signal and the one of the calibrations.

We will thus follow the timewise approach for a second step of orbit determination, in which the positions are assumed as given, that is with a kinematic method. A significant advantage is that it is not necessary to consider the positions from the navigation as observables, and is not necessary to solve for the initial conditions, that is to recompute a more refined orbit (as in the accelerometer mission case). The gradiometer measures directly the gravity potential, through some of its second derivatives, without the intermediary of the orbit. The position time series is needed only to assign the measurement taken at some time to a specific point in space.

The accuracy requirements for this positioning can be assessed by estimating the third derivative of the potential; e.g., for the radial derivatives and the monopole term, with a radial displacement by $\Delta r \simeq - 1 0$ cm

$$
{ \mathrm { \Pi } _ { 3 } ^ { I _ { 0 } } } = - { \frac { 3 } { r } } { \frac { \partial ^ { 2 } U _ { 0 } } { \partial r ^ { 2 } } } \Longrightarrow \Delta { \frac { \partial ^ { 2 } U _ { 0 } } { \partial r ^ { 2 } } } \simeq { \frac { \partial ^ { 3 } U _ { 0 } } { \partial r ^ { 3 } } } \Delta r = - 3 { \frac { \Delta r } { r } } { \frac { \partial ^ { 2 } U _ { 0 } } { \partial r ^ { 2 } } } \simeq 5 \times 1 0 ^ { - 8 } { \frac { \partial ^ { 2 } U _ { 0 } } { \partial r ^ { 2 } } }
$$

for an orbit at altitude $h = 2 5 0 ~ \mathrm { k m }$ . With a monopole gradient $\simeq 7 \times 1 0 ^ { - 7 }$ $\mathrm { s } ^ { - 2 }$ , the change in the radial gradient is $\simeq 3 \times 1 0 ^ { - 1 4 } \ \mathrm { s ^ { - 2 } }$ , or $3 \times 1 0 ^ { - 5 }$ E (in E¨otv¨os unit: 1 $\mathrm { E = 1 0 ^ { - 9 } \ s ^ { - 2 } }$ ). This is well below the sensitivity of the current gradiometers, implying that, in the context of gradiometer missions, the positioning provided by state-of-the-art navigation systems is accurate enough to be used neglecting entirely its uncertainty.

# Gradiometer error models

To decide how to model the calibration functions, we need to follow three principles of good practice. First, calibration models should be based on some understanding of the measurement physics. Second, the error models used in the simulations must contain non-random terms, to describe the unavoidable systematics. Third, the solutions should try to compensate for the systematic errors, without using information on the specific functional expression of the systematics introduced in the simulation. We shall elaborate on these three principles, by using a case study, the European Space Agency mission GOCE, to be launched very soon,9 with the goal of determining the Earth’s gravity field up to very high harmonic degree (ESA 1999).

The performance of gradiometers (also of accelerometers and satellite-tosatellite tracking systems) is generally represented as a noise spectral density $S$ , a function of the frequency $f$ . The measurement band is a frequency interval $[ f _ { m } , f _ { s } ]$ in which the noise spectral density $S$ is minimum, e.g., for GOCE $f _ { s } = 1 / 1 0 \ : \mathrm { H z }$ and $f _ { m } = 1 / 2 0 0 \ : \mathrm { H z }$ , with a requirement $S \le 4 \times 1 0 ^ { - 3 } \mathrm { ~ E ~ }$ $\mathrm { H z ^ { - 1 / 2 } }$ in the measurement band. The noise increases for frequencies $> f _ { s }$ , that is for short integration time; typically, the observations are taken with sampling interval $d t$ of the order of $1 / f _ { s }$ . The Nyquist frequency $f _ { N } =$ $1 / ( 2 d t )$ needs to be $\leq f _ { s }$ to avoid aliasing from noise at higher frequencies. $S ( f )$ increases again for frequencies $< f _ { m }$ : a typical assumption is that the increase is like $1 / f$ . Thus the shape of $S ( f )$ is trapezoidal in a log-log plot.

However, this is a model for noise, and the most important error terms are not noise. For example, the thermal signals are low frequency (the accelerometers are thermally insulated) and have as forcing frequencies integer combinations of the orbit mean motion $n$ and of the Earth’s rotation frequency $\Omega _ { \oplus }$ . Unfortunately some of these appear also in the gravitational signal, see eq. (13.32). An active thermal control might change the dominating frequencies, but might also introduce some systematic signal with another frequency.

Another source of systematics is the attitude control system: errors in the estimation of $R , \omega , \dot { \omega }$ appear as spurious signals in the measured gravity gradient. Since the torques acting on the spacecraft attitude contain signals with frequencies $n$ and $\boldsymbol { n } _ { \oplus }$ , the rotation matrix $R$ contains the same frequencies, and some of these would alias with the gravity signal. The active attitude control might suppress some of these frequencies, and again introduce new ones, which should be included in the error model.

We use as example the simulation published by Milani et al. (2005d). The random error component was simulated as uncorrelated Gaussian noise with $\mathrm { R M S } = 0 . 0 0 4 \mathrm { E }$ (E¨otv¨os units, $1 0 ^ { - 9 } \mathrm { s ^ { - 2 } }$ ). This noise term was used to define the formal covariance, that is the gravity gradient residuals are weighted dividing by 0.004 E. The data simulation did include some systematic errors, represented by a finite number of harmonics, with an amplitude growing as $1 / f$ : a daily term (with amplitude of 1.73 E), “once per rev” and “twice per rev” terms (with amplitude of 0.1 and 0.055 E), supposedly accounting for thermal changes. A very long term drift (supposedly due to seasonal thermal effects) had a period of one year and an amplitude of 18.6 E, decreased, with respect to the $f ^ { - 1 }$ law, by a factor 0.03 (supposedly an a priori calibration by means of a temperature measurement accurate to $\simeq 2 \times 1 0 ^ { - 3 }$ kelvin). Moreover, a term with period 1000 s and amplitude of 0.02 E, five times the RMS of the noise component, was added to investigate the effects of systematic errors due to other causes, such as the attitude control.

# A posteriori gradiometer calibration

The simulation of Milani et al. (2005d) adopted a kinematic timewise method, that is only the gravity harmonic coefficients $\mathbf { g }$ (e.g., $2 0 1 ^ { 2 } - 4$ coefficients for $\ell _ { m a x } = 2 0 0 .$ ) and the gradiometer a posteriori calibration parameters $\mathbf { h }$ were fit to the gradiometer observations. The main issue is the dimension of $\mathbf { h }$ : e.g., if two calibration parameters had to be solved for each interval of $\simeq ~ 2 0 0$ s, then for a nominal eight month mission $\mathbf { h }$ is a vector with $\approx 2 \times 1 0 ^ { 5 }$ components. Note that, if the parameters $\mathbf { h }$ appear linearly in the calibrations as functions of time, the least squares problem is linear, although a very large one. To solve for $> 1 0 0 0 0 0$ parameters would be a problem, not only for the computational load, but also for the bad conditioning of the normal matrix.

The challenge was how to neutralize the systematics (by absorbing them in the calibrations) with acceptable computational load and numerical stability, and this without cheating; e.g., to solve for a finite number of sinusoids would mean using the information on the systematics introduced in the simulation. This would produce illusory results, not reproducible with real data, where the systematic errors cannot have such a simple spectrum.

The time-dependent absolute calibration of the gradiometer, for each component, can be represented as a linear combination of $N$ suitable base functions $c ( t ) = \textstyle \sum c _ { i } \ b _ { i } ( t )$ . This is applicable only to the time span $\Delta t$ of an arc, which cannot be too long, both to keep low the number $N$ of base functions solved at once (to avoid computational complexity and instability) and not to impose one specific functional representation of the absolute calibration. On the other hand, $\Delta t$ cannot be too short: the calibration to be removed has to be the low-frequency component, with frequencies below a calibration band upper limit $f _ { c }$ well separated from $f _ { m }$ . As an example, the tests of Milani et al. (2005d) have used a calibration band with frequencies below $f _ { c } = 1 / 2 0 0 0 ~ \mathrm { H z }$ . Thus $\Delta t$ , $N$ , and the base functions $b _ { i }$ have to be selected to model an arbitrary signal in the calibration band $f < f _ { c }$ ; spurious signals in the intermediate band with $f _ { c } < f < f _ { m }$ are not removed.

The base functions $b _ { i }$ must be such that the normal equation for the calibration parameters $\mathbf { h } _ { i }$ of each arc $i$ is well conditioned. After testing different choices, including Fourier expansions and Chebichev polynomials, Milani et al. (2005d, Section 2.3) concluded that a good choice was a base containing a constant, a linear function of time, sine and cosine terms with periods $\Delta t / k$ for $k = 1 , \ldots , K$ . To limit the removal of signal to the calibration band, $K \simeq \Delta t \cdot f _ { c }$ . For example, $\Delta t = 1 0 0 0 0$ s, $K = 5$ are acceptable choices. The total number of local parameters $\mathbf { h }$ for a simulation over eight months, with $N _ { a r c } = 2 0 0 0$ arcs, was $2 \left( 2 K + 2 \right) \times N _ { a r c } = 4 8 0 0 0$ .

# Local–global correlations

Given the number of parameters to be solved, e.g., 40 397 global and 48 000 local, some decomposition of the normal equation is necessary. The first one is the local–global decomposition of Section 15.1. The impact of the local– global correlations on the results and their estimated uncertainty, discussed in Section 16.2, also occurs in gradiometer missions. Only some of the global coefficients, with low degree and order $\ell$ , $m$ , are severely affected.

The uncertainty estimated without the local–global terms is significantly smaller than in the complete computation, especially for $\ell = 2 , 3 , 6 , 7 , 8$ ; the difference is not significant for $\ell \geq 2 5$ (Milani et al. 2005d, Figure 1). For the Fourier component with $k = 4$ (frequency $1 / 2 5 0 0 ~ \mathrm { H z } )$ and the $C _ { 2 0 }$ harmonic (main frequency $1 / 2 6 8 0 ~ \mathrm { H z } )$ , the local–global correlations (from $\Gamma _ { \ell g }$ ) are $\simeq 0 . 2$ (a significant effect does not require a very high correlation). The actual error is consistent with the higher formal uncertainty, not with the lower one.

The spherical harmonics with $\ell < 2 5$ generate gradiometer signals with frequencies outside the measurement band, thus GOCE should not be used to solve for them. The simplest solution is to include in $\mathbf { g }$ only the coefficients of degree $\ell \geq 2 5$ . In this way the formal RMS is somewhat underestimated, due to the correlations between the harmonics with $\ell \geq 2 5$ and those with $2 \leq \ell \leq 2 4$ ; this becomes negligible for $\ell > 7 5$ . A better solution is to use a collocation method, e.g., by adding a priori observations of the harmonics with $2 \leq l \leq 2 4$ weighted with the inverse of their covariance matrix, as resulting from previous gravimetry missions.