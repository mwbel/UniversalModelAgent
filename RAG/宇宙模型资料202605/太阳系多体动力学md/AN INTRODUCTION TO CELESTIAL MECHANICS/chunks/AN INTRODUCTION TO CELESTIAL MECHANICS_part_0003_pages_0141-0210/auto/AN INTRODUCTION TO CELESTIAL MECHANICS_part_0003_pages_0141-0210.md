It follows from the expression for $\pmb { B }$ that the differential elements corresponding to $\theta = \theta _ { 0 } , \phi = \phi _ { 0 }$ and to $\theta = \pi + \theta _ { 0 } , \phi = - \phi _ { 0 }$ are equal in numerical value but opposite in sign. Since all the elements entering in the integral can be paired in this way, it follows that $V _ { 1 } = 0 .$ ,after which (36) becomes

$$
\left\{ \begin{array} { r } { V = \frac { \sigma } { 2 } \int _ { - \frac { \pi } { 2 } } ^ { \frac { \pi } { 2 } } \int _ { 0 } ^ { 2 \pi } \left\{ \frac { \cos ^ { 2 } \phi \cos ^ { 2 } \theta } { a ^ { 2 } } \left( \frac { 2 x ^ { 2 } } { a ^ { 2 } } - C \right) + \frac { \cos ^ { 2 } \phi \sin ^ { 2 } \theta } { b ^ { 2 } } \right. } \\ { \left. \qquad \times \left( \frac { 2 y ^ { 2 } } { b ^ { 2 } } - C \right) + \frac { \sin ^ { 2 } \phi } { c ^ { 2 } } \left( \frac { 2 z ^ { 2 } } { c ^ { 2 } } - C \right) \right\} \frac { \cos \phi d \phi d \theta } { A ^ { 2 } } } \\ { + 2 \sigma \int _ { - \frac { \pi } { 2 } } ^ { \frac { \pi } { 2 } } \int _ { 0 } ^ { 2 \pi } \left\{ \frac { x y \cos ^ { 2 } \phi \sin \theta \cos \theta } { a ^ { 2 } b ^ { 2 } } + \frac { y z \sin \phi \cos \phi \sin \theta } { b ^ { 2 } c ^ { 2 } } \right. } \\ { \left. \qquad + \frac { z x \sin \phi \cos \phi \cos \theta } { c ^ { 2 } a ^ { 2 } } \right\} \frac { \cos \phi d \phi d \theta } { A ^ { 2 } } . } \end{array} \right.
$$

By comparing the elements properly paired,it is seen that the second integral is zero.

Let

$$
W = \frac { \sigma } { 2 } \int _ { - \frac { \pi } { 2 } } ^ { \frac { \pi } { 2 } } \int _ { 0 } ^ { 2 \pi } \frac { \cos \phi d \phi d \theta } { \frac { \cos ^ { 2 } \phi \cos ^ { 2 } \theta } { a ^ { 2 } } + \frac { \cos ^ { 2 } \phi \sin ^ { 2 } \theta } { b ^ { 2 } } + \frac { \sin ^ { 2 } \phi } { c ^ { 2 } } } ;
$$

then (37) can be written in the form

$$
V = - \ C W + { \frac { x ^ { 2 } } { a } } \ { \frac { \partial W } { \partial a } } + { \frac { y ^ { 2 } } { b } } \ { \frac { \partial W } { \partial b } } + { \frac { z ^ { 2 } } { c } } { \frac { \partial W } { \partial c } } .
$$

For a given ellipsoid $\boldsymbol { W }$ is a constant, and the equation of the level surfaces has the form

$$
C _ { 1 } x ^ { 2 } + C _ { 2 } y ^ { 2 } + C _ { 3 } z ^ { 2 } = { \mathrm { c o n s t a n t } } ,
$$

which is the equation of concentric similar ellipsoids, whose axes are proportional to $C _ { 1 } { } ^ { - 1 } , \ C _ { 2 } { } ^ { - 1 }$ ，and $C _ { 3 } {  }$

In order to reduce $W$ to an integrable form,let

$$
\left\{ \begin{array} { l l } { { M = \displaystyle { \frac { \cos ^ { 2 } \phi } { a ^ { 2 } } } + \displaystyle { \frac { \sin ^ { 2 } \phi } { c ^ { 2 } } } } , } \\ { { { } } } \\ { { N = \displaystyle { \frac { \cos ^ { 2 } \phi } { b ^ { 2 } } } + \displaystyle { \frac { \sin ^ { 2 } \phi } { c ^ { 2 } } } } ; } \end{array} \right.
$$

then (38) becomes

$$
\begin{array} { r l r } & { } & { W = \displaystyle \frac { \sigma } { 2 } \int _ { - \frac { \pi } { 2 } } ^ { \frac { \pi } { 2 } } \int _ { 0 } ^ { 2 \pi } \frac { \cos \phi d \phi d \theta } { M \cos ^ { 2 } \theta + N \sin ^ { 2 } \theta } } \\ & { } & \\ & { } & { = 4 \sigma \displaystyle \int _ { 0 } ^ { \frac { \pi } { 2 } } \int _ { 0 } ^ { \frac { \pi } { 2 } } \frac { \cos \phi d \phi d \theta } { M \cos ^ { 2 } \theta + N \sin ^ { 2 } \theta } . } \end{array}
$$

$\pmb { M }$ and $\pmb { N }$ are independent of $\theta$ ； hence,on integrating with respect to this variable,it is found that\*

$$
\begin{array} { l } { { W = 2 \pi \sigma \displaystyle \int _ { 0 } ^ { \frac { \pi } { 2 } } \frac { \cos { \phi } d \phi } { \sqrt { M N } } } } \\ { { = 2 \pi \sigma a b c ^ { 2 } \displaystyle \int _ { 0 } ^ { \frac { \pi } { 2 } } \frac { \cos { \phi } d \phi } { \sqrt { ( a ^ { 2 } \sin ^ { 2 } { \phi } + c ^ { 2 } \cos ^ { 2 } { \phi } ) ( b ^ { 2 } \sin ^ { 2 } { \phi } + c ^ { 2 } \cos ^ { 2 } { \phi } ) } } . } } \end{array}
$$

To return to the symmetry in $a , b$ and $\pmb { c }$ which existed in (38), Jacobi introduced the transformation

$$
\sin \phi = \frac { c } { \sqrt { c ^ { 2 } + s } } ;
$$

whence

$$
W = \pi \sigma a b c \int _ { 0 } ^ { \infty } \frac { d s } { \sqrt { ( a ^ { 2 } + s ) ( b ^ { 2 } + s ) ( c ^ { 2 } + s ) } } .
$$

On forming the derivatives with respect to $a , b$ ,and $\pmb { c }$ ,and substituting in (39),it follows that

$$
\begin{array} { c } { { V = \pi \sigma a b c \displaystyle \int _ { 0 } ^ { \infty } \left( 1 - \frac { x ^ { 2 } } { a ^ { 2 } + s } - \frac { y ^ { 2 } } { b ^ { 2 } + s } - \frac { z ^ { 2 } } { c ^ { 2 } + s } \right) } } \\ { { \times \displaystyle \frac { d s } { \sqrt { ( a ^ { 2 } + s ) ( b ^ { 2 } + s ) ( c ^ { 2 } + s ) } } . } } \end{array}
$$

The components of attraction are

$$
\begin{array} { l } { \displaystyle  X = k ^ { 2 } \frac { \partial V } { \partial x } = - \int _ { 0 } ^ { \infty } \frac { 2 \pi \sigma a b c x k ^ { 2 } d s } { ( a ^ { 2 } + s ) \sqrt { ( a ^ { 2 } + s ) ( b ^ { 2 } + s ) ( c ^ { 2 } + s ) } } ,  } \\ { \displaystyle  Y = k ^ { 2 } \frac { \partial V } { \partial y } = - \int _ { 0 } ^ { \infty } \frac { 2 \pi \sigma a b c y k ^ { 2 } d s } { ( b ^ { 2 } + s ) \sqrt { ( a ^ { 2 } + s ) ( b ^ { 2 } + s ) ( c ^ { 2 } + s ) } } ,  } \\ { \displaystyle  [ Z = k ^ { 2 } \frac { \partial V } { \partial z } = - \int _ { 0 } ^ { \infty } \frac { 2 \pi \sigma a b c z k ^ { 2 } d s } { ( c ^ { 2 } + s ) \sqrt { ( a ^ { 2 } + s ) ( b ^ { 2 } + s ) ( c ^ { 2 } + s ) } } .  } \end{array}
$$

Equation (41) is homogeneous of the second degree in $a , b ,$ \* Letting tan $\pmb \theta = \pmb z$ , the integral reduces to one of the standard formg.

and $\pmb { c }$ ； and therefore $\frac { \partial V } { \partial x } , \frac { \partial V } { \partial y } , \frac { \partial V } { \partial z }$ ，computed from (39)，are homogeneous of degree zero in the same quantities. It follows, therefore,that if $a , ~ b$ and $\pmb { c }$ are increased by any factor $\pmb { \nu }$ the components of attraction $X , ~ Y$ and $\mathbf { z }$ ，will not be changed；or, the elliptic homoeoid contained between the ellipsoidal surfaces whose axes are $a , \ b$ c and va, ${ \pmb \nu } { \pmb b }$ ，and vc attracts the interior particle $\pmb { P }$ equally in opposite directions. (Compare Art.67.)

The component of attraction, $\pmb { X }$ ，is independent of $y$ and $\pmb { z }$ and involves $\pmb { x }$ to the first degree；therefore the $_ x$ -component of attraction is proportional to the ${ \pmb x } ^ { \th }$ -coirdinate of the particle and is constant everywhere within the ellipsoid in the plane ${ \boldsymbol { \xi } } = { \boldsymbol { x } }$ .Similar results are true for the two other coordinates.

Suppose the notation has been chosen so that $a > b > c$ Then (41） can be put in the normal form for an eliptic integral of the frst kind by the substitution

$$
\sin \varphi = { \frac { c } { \sqrt { a ^ { 2 } - c ^ { 2 } } } } { \frac { u } { \sqrt { 1 - u ^ { 2 } } } } ,
$$

$$
\kappa ^ { 2 } = \frac { a ^ { 2 } - b ^ { 2 } } { a ^ { 2 } - c ^ { 2 } } < 1 ,
$$

which gives

$$
W = \frac { 2 \pi \sigma a b c } { \sqrt { a ^ { 2 } - c ^ { 2 } } } \int _ { 0 } ^ { \frac { \sqrt { a ^ { 2 } - c ^ { 2 } } } { a } } \frac { d u } { \sqrt { ( 1 - u ^ { 2 } ) ( 1 - \kappa ^ { 2 } u ^ { 2 } ) } } .
$$

This integral can be readily computed,when $\pmb { \kappa } ^ { 2 }$ is small, by expanding the integrand as a power series in $\kappa ^ { 2 }$ and integrating term by term.

# XII. PROBLEMS.

1. Discuss the level surfaces given by equation (29).

2.Set up the expressions for the components of attraction instead of that for the potential as in Art.79. Determine what parts of the integrals vanish, integrate with respect to $\pmb \theta$ ,and show that the results are

$$
\begin{array} { l } { \displaystyle \left[ X = - 4 \pi \sigma b c x k ^ { 2 } \int _ { 0 } ^ { \frac { \pi } { 2 } } \frac { \mathrm { s i n } ^ { 2 } \phi \cos \phi d \phi } { \sqrt { ( b ^ { 2 } \sin ^ { 2 } \phi + a ^ { 2 } \cos ^ { 2 } \phi ) ( c ^ { 2 } \sin ^ { 2 } \phi + a ^ { 2 } \cos ^ { 2 } \phi ) } } , \right. } \\ { \displaystyle \left. Y = - 4 \pi \sigma a y k ^ { 2 } \int _ { 0 } ^ { \frac { \pi } { 2 } } \frac { \sin ^ { 2 } \phi \cos \phi d \phi } { \sqrt { ( c ^ { 2 } \sin ^ { 2 } \phi + b ^ { 2 } \cos ^ { 2 } \phi ) ( a ^ { 2 } \sin ^ { 2 } \phi + b ^ { 2 } \cos ^ { 2 } \phi ) } } , \right. } \\ { \displaystyle \left. Z = - 4 \pi \sigma a b z k ^ { 2 } \int _ { 0 } ^ { \frac { \pi } { 2 } } \frac { \sin ^ { 2 } \phi \cos \phi d \phi } { \sqrt { ( a ^ { 2 } \sin ^ { 2 } \phi + c ^ { 2 } \cos ^ { 2 } \phi ) ( b ^ { 2 } \sin ^ { 2 } \phi + c ^ { 2 } \cos ^ { 2 } \phi ) } } . \right. } \end{array}
$$

Hint.Derive the results for $z$ ,and since it is immaterial in what order the axes are chosen,derive the others by a permutation of the letters $a , b , c .$

3. Transform the equations of problem 2 by

$$
\sin \phi = \frac { \alpha } { \sqrt { a ^ { 2 } + s } } , \qquad \sin \phi = \frac { b } { \sqrt { b ^ { 2 } + s } } , \qquad \sin \phi = \frac { c } { \sqrt { c ^ { 2 } + s } } ,
$$

respectively,and show that equations (43) result.

4. Show that the potential of an ellipsoid upon a particle at its center is

$$
V _ { 0 } = \pi \sigma a b c \int _ { 0 } ^ { \infty } \frac { d s } { \sqrt { ( a ^ { 2 } + s ) ( b ^ { 2 } + s ) ( c ^ { 2 } + s ) } } = W .
$$

5. From the value of $\scriptstyle { V _ { 0 } }$ and equations (43) derive the value of the potential (42).

6.Transform the equations of problem 2 so that they take the form

$$
\begin{array} { r } { \int \frac { u ^ { 2 } d u } { \sqrt { \left( 1 - u ^ { 2 } \right) \left( 1 - \kappa ^ { 2 } u ^ { 2 } \right) } } . } \end{array}
$$

7. Integrate equations (28) without expanding the expresion for $r ^ { \mathfrak { L } }$ as a power series in $e ^ { 2 }$

80. The Attraction of a Solid Homogeneous Ellipsoid upon an Exterior Particle. Ivory's Method. The integrals become so complicated in the case of an exterior particle that the components of attraction have not been found by direct integration except in series. They are computed indirectly by expressing them in terms of the components of attraction of a related elipsoid upon particles in its interior. This artifice constitutes Ivory's method.\*

![](images/01b4cece8b9eb8e0350149f8e8e3c11caf189ccc757e27bbbc488cc1f4e40ed3.jpg)  
Fig. 23.

Let it be required to find the attraction of the ellipsoid $\mathbfit { \Delta } E$ upon the exterior particle $P ^ { \prime }$ at the point $( x ^ { \prime } , \ y ^ { \prime } , \ z ^ { \prime } )$ .Let the semiaxes of $\pmb { \cal E }$ be $a , b _ { i }$ ，and c. Construct tbrough $P ^ { \prime }$ an ellipsoid ${ \pmb E ^ { \prime } }$ ， confocal with $\pmb { { \cal E } }$ ，with the semi-axes $a ^ { \prime } , b ^ { \prime } , c ^ { \prime }$ ，and suppose it has the same density as $\pmb { \cal E }$ .The axes of the two ellipsoids are related by the equations

$$
\left\{ \begin{array} { l l } { { a ^ { \prime } = \ \sqrt { { a ^ { 2 } } + \kappa } , } } \\ { { b ^ { \prime } = \ \sqrt { { b ^ { 2 } } + \kappa } , } } \\ { { c ^ { \prime } = \ \sqrt { { c ^ { 2 } } + \kappa } , } } \end{array} \right.
$$

where $\pmb { \kappa }$ is defined by the equation

$$
\frac { { x ^ { \prime } } ^ { 2 } } { a ^ { 2 } + \kappa } + \frac { { y ^ { \prime } } ^ { 2 } } { b ^ { 2 } + \kappa } + \frac { { z ^ { \prime } } ^ { 2 } } { c ^ { 2 } + \kappa } - 1 = 0 .
$$

The only value of $\pmb { \kappa }$ admissible in this problem is real and positive. Equation (46) is a cubic in $\pmb { \kappa }$ and has one positive and two negative roots; for, the left member considered as a function of $\pmb { \kappa }$ is negative when $\kappa = + \infty$ ；positive，when $\pmb { \kappa } = \pmb { 0 }$ (because $( x ^ { \prime } , \ y ^ { \prime } , \ z ^ { \prime } )$ is exterior to the ellipsoid $\pmb { \cal E }$ ）；positive，when $\kappa = - \ c ^ { 2 } + \epsilon$ (where e is a very small positive quantity)；negative,when $\kappa = - \ c ^ { 2 } - \epsilon ;$ positive，when $\kappa = - b ^ { 2 } + \epsilon$ negative，when $\kappa = - b ^ { 2 } - \epsilon ;$ positive,when $\kappa = - a ^ { 2 } + \epsilon$ ；negative，when $\kappa = - \ a ^ { 2 } - \epsilon ;$ and negative when $\kappa = - \infty$ . The graph of the function is given in Fig.24. When the positive root is taken, $a ^ { \prime } , \ b ^ { \prime }$ ，and ${ \pmb { c } } ^ { \prime }$ are determined uniquely.

![](images/2190eab558c87e836acd989ae37dea883cf4acb7fb17e8669dc523c3bf79dfad.jpg)  
Fig. 24.

A one-to-one correspondence between the points upon the twc ellipsoids will now be established by the equations (compare Art.77)

$$
\xi ^ { \prime } = \frac { a ^ { \prime } } { a } \xi , \eta ^ { \prime } = \frac { b ^ { \prime } } { b } \eta , \xi ^ { \prime } = \frac { c ^ { \prime } } { c } \xi .
$$

Let $\pmb { \cal P }$ be the point corresponding to $\scriptstyle { P ^ { \prime } }$ .It will be shown that the attraction of $\pmb { { \cal E } }$ upon $P ^ { \prime }$ is related in a very simple manner to that of $E ^ { \prime }$ upon $P$

Let $X , ~ Y$ ，and $z$ represent the components of attraction of ${ \pmb E } ^ { \prime }$ upon the interior particle $\pmb { P }$ at the point $( x , y , z )$ .They can be computed by the methods of Art.79,and will be supposed known. Let $X ^ { \prime } , Y ^ { \prime }$ and $\mathbf { Z ^ { \prime } }$ be the components of attraction of $\mathbf { \delta } _ { E }$ upon $P ^ { \prime }$ ， which are required. The expressions for the $\pmb { x }$ -components are

$$
\begin{array}{c} \begin{array} { r } { [ X = - k ^ { 2 } \sigma \overset { \displaystyle \int } \int \int \frac { x - \xi ^ { \prime } } { \rho ^ { \prime } } d \xi ^ { \prime } d \eta ^ { \prime } d \xi ^ { \prime } = k ^ { 2 } \sigma \overset { \displaystyle \int } \int \int \frac { \partial ( \frac { 1 } { \rho ^ { \prime } } ) } { \partial \xi ^ { \prime } } d \xi ^ { \prime } d \eta ^ { \prime } d \xi ^ { \prime } , } \\ { [ X ^ { \prime } = - k ^ { 2 } \sigma \overset { \displaystyle \int } \int \int \frac { x ^ { \prime } - \xi } { \rho ^ { 3 } } d \xi d \eta d \xi = k ^ { 2 } \sigma \overset { \displaystyle \int } \int \int \frac { \partial ( \frac { 1 } { \rho } ) } { \partial \xi } d \xi d \eta d \xi . } \end{array} ]  \end{array}
$$

On performing the integration with respect to $\pmb { \xi } ,$ it is found that

$$
\left\{ \begin{array} { l } { { \displaystyle { \cal X } = k ^ { 2 } \sigma \int \int \left( \frac { 1 } { \rho _ { 2 } ^ { \prime } } - \frac { 1 } { \rho _ { 1 } ^ { \prime } } \right) d \eta ^ { \prime } d \xi ^ { \prime } } , } \\ { { \displaystyle { \cal X } ^ { \prime } = k ^ { 2 } \sigma \int \int \left( \frac { 1 } { \rho _ { 2 } } - \frac { 1 } { \rho _ { 1 } } \right) d \eta d \xi } , } \end{array} \right.
$$

where ${ \pmb \rho } _ { \mathbf { 2 } }$ and $\pmb { \rho _ { 1 } }$ are the distances from $P ^ { \prime }$ to the ends of the elementary column obtained by integrating with respect to $\xi$ The solution is completed by integrating over the whole surface of $\pmb { \cal E }$ · The first equation of (49) is interpreted similarly.

Now $X ^ { \prime }$ will be related to $X$ in a simple manner by the aid of the following lemma:

If $\pmb { P }$ and $\pmb { A }$ are any two points on the surface of $\pmb { \cal E }$ ，and if $P ^ { \prime }$ and $A ^ { \prime }$ are the respective corresponding points on the surface of ${ \pmb E } ^ { \prime }$ ,then the distances $\overline { { P A ^ { \prime } } }$ and $\overline { { P ^ { \prime } A } }$ are equal.

Let $\overline { { P A ^ { \prime } } } = \rho ^ { \prime }$ and $\overline { { A P ^ { \prime } } } = { \rho }$ Then $\rho = \rho ^ { \prime }$ For，let the coordinates of $P$ and $\pmb { A }$ be respectively $\xi _ { 1 } , \eta _ { 1 } , \xi _ { 1 } \mathrm { a n d } \xi _ { 2 } , \eta _ { 2 } , \xi _ { 2 } ;$ and of $\scriptstyle { \pmb { P } } ^ { \prime }$ and $A ^ { \prime } , \xi _ { 1 } ^ { \prime } , \eta _ { 1 } ^ { \prime } , \zeta _ { 1 } ^ { \prime }$ and $\xi _ { 2 } ^ { \prime } , \eta _ { 2 } ^ { \prime } , \zeta _ { 2 } ^ { \prime }$ .Then

$$
\begin{array} { r } { \int \rho ^ { \prime 2 } = ( \xi _ { 1 } - \xi _ { 2 } ^ { \prime } ) ^ { 2 } + ( \eta _ { 1 } - \eta _ { 2 } ^ { \prime } ) ^ { 2 } + ( \xi _ { 1 } - \xi _ { 2 } ^ { \prime } ) ^ { 2 } , } \\ { \int \ d \rho ^ { 2 } = ( \xi _ { 2 } - \xi _ { 1 } ^ { \prime } ) ^ { 2 } + ( \eta _ { 2 } - \eta _ { 1 } ^ { \prime } ) ^ { 2 } + ( \xi _ { 2 } - \xi _ { 1 } ^ { \prime } ) ^ { 2 } . } \end{array}
$$

On making use of equations (45) and (47),it is found that

$$
\rho ^ { \prime 2 } - \rho ^ { 2 } = \kappa \left( { \frac { \xi _ { 2 } { } ^ { 2 } } { a ^ { 2 } } } + { \frac { \eta _ { 2 } { } ^ { 2 } } { b ^ { 2 } } } + { \frac { \zeta _ { 2 } { } ^ { 2 } } { c ^ { 2 } } } \right) - \kappa \left( { \frac { \xi _ { 1 } { } ^ { 2 } } { a ^ { 2 } } } + { \frac { \eta _ { 1 } { } ^ { 2 } } { b ^ { 2 } } } + { \frac { \zeta _ { 1 } { } ^ { 2 } } { c ^ { 2 } } } \right) .
$$

Since $\pmb { P }$ and $A$ are on the surface of the ellipsoid whose semi-axes are $a , b$ ,and $\pmb { c }$ ,each parenthesis equals unity. Therefore $\rho ^ { \prime 2 } - \rho ^ { 2 } = 0$ ， or $\rho = \rho ^ { \prime }$

Suppose the integrals (49) are computed so that the elements at corresponding points of the two surfaces are always taken simultaneously. Then $\rho _ { 1 } = { \rho _ { 1 } } ^ { \prime }$ and $\rho _ { 2 } = \rho _ { 2 } ^ { \prime }$ throughout the integration.

Moreerifl $d \eta = \frac { b } { b ^ { \prime } } d \eta ^ { \prime }$ and $d \xi = \frac { c } { c ^ { \prime } } d \xi ^ { \prime }$ Therefore

$$
\left\{ \begin{array} { l } { { X = k ^ { 2 } \sigma \displaystyle \int \int \left( \frac { 1 } { { \rho _ { 2 } } ^ { \prime } } - \frac { 1 } { { \rho _ { 1 } } ^ { \prime } } \right) d \eta ^ { \prime } d \xi ^ { \prime } , } } \\ { { X ^ { \prime } = k ^ { 2 } \sigma \displaystyle \frac { b c } { b ^ { \prime } c ^ { \prime } } \displaystyle \int \int \left( \frac { 1 } { { \rho _ { 2 } } ^ { \prime } } - \frac { 1 } { { \rho ^ { \prime } } } \right) d \eta ^ { \prime } d \xi ^ { \prime } = \displaystyle \frac { b c } { b ^ { \prime } c ^ { \prime } } X ; } } \end{array} \right.
$$

and similarly

$$
\left\{ \begin{array} { l } { { Y ^ { \prime } = \displaystyle \frac { c a } { c ^ { \prime } a ^ { \prime } } Y , } } \\ { { \ Z ^ { \prime } = \displaystyle \frac { a b } { a ^ { \prime } b ^ { \prime } } Z . } } \end{array} \right.
$$

The letters $a , b , c ,$ and s of equations (43) should be given accents to agree with the notations of this article;and,since $P$ and $P ^ { \prime }$ are coresponding points, $\quad x = { \frac { a } { a ^ { \prime } } } x ^ { \prime }$ ， $y = { \frac { b } { b ^ { \prime } } } y ^ { \prime }$ ， $z = { \frac { c } { c ^ { \prime } } } z ^ { \prime }$ After making these changes in equations (43) and substituting them in (50)and (51),it is found that

$$
\begin{array} { l } { { \displaystyle \left\{ X ^ { \prime } = - 2 \pi \sigma a b c k ^ { 2 } x ^ { \prime } \int _ { 0 } ^ { \infty } \frac { d s ^ { \prime } } { ( a ^ { \prime 2 } + s ^ { \prime } ) \sqrt { ( a ^ { \prime 2 } + s ^ { \prime } ) ( b ^ { \prime 2 } + s ^ { \prime } ) ( c ^ { \prime 2 } + s ^ { \prime } ) } } , \right. } } \\ { { \displaystyle \left\{ Y ^ { \prime } = - 2 \pi \sigma a b c k ^ { 2 } y ^ { \prime } \int _ { 0 } ^ { \infty } \frac { d s ^ { \prime } } { ( b ^ { \prime 2 } + s ^ { \prime } ) \sqrt { ( a ^ { \prime 2 } + s ^ { \prime } ) ( b ^ { \prime 2 } + s ^ { \prime } ) ( c ^ { \prime 2 } + s ^ { \prime } ) } } , \right. } } \\ { { \displaystyle \left. Z ^ { \prime } = - 2 \pi \sigma a b c k ^ { 2 } z ^ { \prime } \int _ { 0 } ^ { \infty } \frac { d s ^ { \prime } } { ( c ^ { \prime 2 } + s ^ { \prime } ) \sqrt { ( a ^ { \prime 2 } + s ^ { \prime } ) ( b ^ { \prime 2 } + s ^ { \prime } ) ( c ^ { \prime 2 } + s ^ { \prime } ) } } . \right. } } \end{array}
$$

It follows from equations (45) that

$$
a ^ { \prime } { } ^ { 2 } = a ^ { 2 } + \kappa , \qquad b ^ { \prime } { } ^ { 2 } = b ^ { 2 } + \kappa , \qquad c ^ { \prime } { } ^ { 2 } = c ^ { 2 } + \kappa ;
$$

hence,on letting $\begin{array} { r } { s = s ^ { \prime } + \kappa _ { \mathrm { : } } } \end{array}$ it follows that

$$
\begin{array} { r } { \left\{ \begin{array} { l } { X ^ { \prime } = - 2 \pi \sigma a b c k ^ { 2 } x ^ { \prime } \displaystyle \int _ { \kappa } ^ { \infty } \frac { d s } { ( a ^ { 2 } + s ) \sqrt { ( a ^ { 2 } + s ) ( b ^ { 2 } + s ) c ^ { 2 } + s ) } } , } \\ { \displaystyle Y ^ { \prime } = - 2 \pi \sigma a b c k ^ { 2 } y ^ { \prime } \displaystyle \int _ { \kappa } ^ { \infty } \frac { d s } { ( b ^ { 2 } + s ) \sqrt { ( a ^ { 2 } + s ) ( b ^ { 2 } + s ) ( c ^ { 2 } + s ) } } , } \\ { \displaystyle Z ^ { \prime } = - 2 \pi \sigma a b c k ^ { 2 } z ^ { \prime } \displaystyle \int _ { \kappa } ^ { \infty } \frac { d s } { ( c ^ { 2 } + s ) \sqrt { ( a ^ { 2 } + s ) ( b ^ { 2 } + s ) ( c ^ { 2 } + s ) } } . } \end{array} \right. } \end{array}
$$

It follows from equations (40) and (41） that the components of attraction for interior particles are homogeneous of degree zero in $a , \ b$ and $c$ ，and that they are proportional to the respective coordinates of the attracted particle. Let $X$ ，asabove,represent the attraction of the ellipsoid $E ^ { \prime }$ ，whose semi-axes are $a ^ { \prime } , \ b ^ { \prime } , \ c ^ { \prime } ,$ upon the interior particle at $( x , y , z )$ ; let $X ^ { \prime \prime }$ represent the attraction of $E ^ { \prime }$ upon an interior particle at $( x ^ { \prime \prime } , y ^ { \prime \prime } , z ^ { \prime \prime } )$ ，which will be supposed to be related to $( x , y , z )$ by equations of the same form as (47). Then it follows that

$$
{ \frac { X ^ { \prime \prime } } { X } } = { \frac { x ^ { \prime \prime } } { x } } , \qquad { \frac { Y ^ { \prime \prime } } { Y } } = { \frac { y ^ { \prime \prime } } { y } } , \qquad { \frac { Z ^ { \prime \prime } } { Z } } = { \frac { z ^ { \prime \prime } } { z } } .
$$

Let the point $( x ^ { \prime \prime } , ~ y ^ { \prime \prime } , ~ z ^ { \prime \prime } )$ ， always corresponding to $( x , y , z )$ ， approach the surface of ${ \pmb E } ^ { \prime }$ as a limit. Then at the limit

$$
{ \frac { X ^ { \prime \prime } } { X } } = { \frac { a ^ { \prime } } { a } } , \quad { \frac { Y ^ { \prime \prime } } { Y } } = { \frac { b ^ { \prime } } { b } } , \quad { \frac { Z ^ { \prime \prime } } { Z } } = { \frac { c ^ { \prime } } { c } } .
$$

On combining these equations with (50) and (51),it is found that

$$
{ \frac { X ^ { \prime \prime } } { X ^ { \prime } } } = { \frac { Y ^ { \prime \prime } } { Y ^ { \prime } } } = { \frac { Z ^ { \prime \prime } } { Z ^ { \prime } } } = { \frac { a ^ { \prime } b ^ { \prime } c ^ { \prime } } { a b c } } = { \frac { M ^ { \prime } } { M } } .
$$

That is,the attraction of $^ { a }$ solid ellipsoid upon an exterior particle is to the attraction of $^ { a }$ confocal ellipsoid passing through the particle, as the mass of the frst ellipsoid is to that of the second ellipsoid.

Consider another ellipsoid confocal with the one passing through the particle and interior to it；by the same reasoning the ratios of the components of attraction of these two ellipsoids are as their masses. Let $X ^ { \prime \prime \prime }$ ， $Y ^ { \prime \prime \prime }$ ， ${ \pmb Z } ^ { \prime \prime \prime }$ be the components of attraction of the new ellipsoid whose semi-axes are $a ^ { \prime \prime \prime } , b ^ { \prime \prime \prime } , c ^ { \prime \prime \prime }$ Then

$$
{ \frac { X ^ { \prime \prime } } { X ^ { \prime \prime \prime } } } = { \frac { Y ^ { \prime \prime } } { Y ^ { \prime \prime \prime } } } = { \frac { Z ^ { \prime \prime } } { Z ^ { \prime \prime \prime } } } = { \frac { a ^ { \prime } b ^ { \prime } c ^ { \prime } } { a ^ { \prime \prime \prime } b ^ { \prime \prime \prime } c ^ { \prime \prime \prime } } } = { \frac { M ^ { \prime } } { M ^ { ' \prime \prime } } } .
$$

On combining this proportion with (53),it is found that

$$
\frac { X ^ { \prime } } { X ^ { \prime \prime \prime } } = \frac { Y ^ { \prime } } { Y ^ { \prime \prime \prime } } = \frac { Z ^ { \prime } } { Z ^ { \prime \prime \prime } } = \frac { M } { M ^ { \prime \prime \prime } } .
$$

Therefore,two confocal ellipsoids attract particles which are exterior to both of them in the same direction and with forces which are proportional to their masses. This theorem was found by Maclaurin and Lagrange for ellipsoids of revolution,and was extended by Laplace to the general case where the three axes are unequal. It is established most easily, however,by Ivory's method as above, and it is frequently called Ivory's theorem.

The right members of equations (52) can be transformed to forms which are more convenient for computation by putting,in the first, $\frac { a } { { \sqrt { a ^ { 2 } + s } } } = u$ ; in the second, $\frac { b } { \sqrt { b ^ { 2 } + s } } = u$ and in the third, $\frac { c } { \sqrt { b ^ { 2 } + s } } = u$ .The results of the substitutions are

$$
\scriptstyle \left\{ \begin{array} { l l } { { X ^ { \prime } = - 4 \pi \sigma b c k ^ { 2 } x ^ { \prime } \displaystyle \int _ { 0 } ^ { \frac { \alpha } { \sqrt { a ^ { 2 } + \kappa } } } \frac { u ^ { 2 } d u } { \sqrt { [ a ^ { 2 } - ( a ^ { 2 } - b ^ { 2 } ) u ^ { 2 } ] [ a ^ { 2 } - ( a ^ { 2 } - c ^ { 2 } ) u ^ { 2 } ] } } , } } \\ { { Y ^ { \prime } = - 4 \pi \sigma c a k ^ { 2 } y ^ { \prime } \displaystyle \int _ { 0 } ^ { \frac { b } { \sqrt { b ^ { 2 } + \kappa } } } \frac { u ^ { 2 } d u } { \sqrt { [ b ^ { 2 } - ( b ^ { 2 } - c ^ { 2 } ) u ^ { 2 } ] [ b ^ { 2 } - ( b ^ { 2 } - a ^ { 2 } ) u ^ { 2 } ] } } , } } \\ { { Z ^ { \prime } = - 4 \pi \sigma a b k ^ { 2 } z ^ { \prime } \displaystyle \int _ { 0 } ^ { \frac { c } { \sqrt { c ^ { 2 } + \kappa } } } \frac { u ^ { 2 } d u } { \sqrt { [ c ^ { 2 } - ( c ^ { 2 } - a ^ { 2 } ) u ^ { 2 } ] [ c ^ { 2 } - ( c ^ { 2 } - b ^ { 2 } ) u ^ { 2 } ] } } . } } \end{array} \right.
$$

When the attracted particle is in the interior of the ellipsoid the forms of the integrals are the same except that the upper limits are unity.

81.The Attraction of Spheroids. The components of attraction will be obtained from (54)，which hold for exterior particles. Suppose the attracting body is an oblate spheroid in which $\scriptstyle a = b > c$ and let $\pmb { e }$ represent the eccentricity of a meridian section. Then

$$
c ^ { 2 } = a ^ { 2 } ( 1 - e ^ { 2 } ) ,
$$

and equations (54) become

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { X ^ { \prime } } { x ^ { \prime } } = \displaystyle \frac { Y ^ { \prime } } { y ^ { \prime } } = - \ 4 \pi \sigma k ^ { 2 } \sqrt { 1 - \ e ^ { 2 } } \displaystyle \int _ { 0 } ^ { \frac { a } { \sqrt { a ^ { 2 } + \kappa } } } \displaystyle \frac { u ^ { 2 } d u } { \sqrt { 1 - \ e ^ { 2 } u ^ { 2 } } } , } \\ { \displaystyle \frac { Z ^ { \prime } } { z ^ { \prime } } = \ - \ 4 \pi \sigma k ^ { 2 } \displaystyle \int _ { 0 } ^ { \frac { c } { \sqrt { c ^ { 2 } + \kappa } } } \displaystyle \frac { u ^ { 2 } d u } { 1 - e ^ { 2 } + e ^ { 2 } u ^ { 2 } } . } \end{array} \right.
$$

The integrals of these equations are

$$
\left\{ \begin{array} { l } { \displaystyle \frac { X ^ { \prime } } { x ^ { \prime } } = \frac { Y ^ { \prime } } { y ^ { \prime } } = - 2 \pi \sigma k ^ { 2 } \frac { \sqrt { 1 - e ^ { 2 } } } { e ^ { 3 } } \left[ \frac { - a e } { \sqrt { a ^ { 2 } + \kappa } } \sqrt { 1 - \frac { a ^ { 2 } e ^ { 2 } } { a ^ { 2 } + \kappa } } \right. } \\ { \displaystyle \qquad + \left. \sin ^ { - 1 } \left( \frac { a e } { \sqrt { a ^ { 2 } + \kappa } } \right) \right] , } \\ { \displaystyle \frac { Z ^ { \prime } } { z ^ { \prime } } = - 4 \pi \sigma \frac { k ^ { 2 } } { e ^ { 3 } } \left[ \frac { c e } { \sqrt { c ^ { 2 } + \kappa } } - \sqrt { 1 - e ^ { 2 } } \right. } \\ { \displaystyle \qquad \left. \times \tan ^ { - 1 } \left( \frac { c e } { \sqrt { ( 1 - e ^ { 2 } ) ( c ^ { 2 } + \kappa ) } } \right) \right] . } \end{array} \right.
$$

The components of attraction for interior particles are obtained from equations (56) by putting $\kappa = 0$

Now suppose the attracting body is a prolate spheroid and that $a = b < c$ Then $a ^ { 2 } = b ^ { 2 } = c ^ { 2 } ( 1 - \epsilon ^ { 2 } )$ ，and equations (54) become

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { X ^ { \prime } } { x ^ { \prime } } = \displaystyle \frac { Y ^ { \prime } } { y ^ { \prime } } = - \ 4 \pi \sigma k ^ { 2 } \int _ { 0 } ^ { \frac { \alpha } { \sqrt { \smash { \frac { a ^ { 2 } + \kappa } { \varepsilon ^ { 2 } + \kappa } } } } } \displaystyle \frac { u ^ { 2 } d u } { \sqrt { \smash { \frac { a ^ { 2 } + d u } { \varepsilon ^ { 2 } + \varepsilon ^ { 2 } u ^ { 2 } } } } } , } \\ { \displaystyle \frac { Z ^ { \prime } } { z ^ { \prime } } = \mathrm { ~ - ~ } 4 \pi \sigma k ^ { 2 } ( 1 - \epsilon ^ { 2 } ) \int _ { 0 } ^ { \frac { \sigma } { \sqrt { \smash { \frac { a ^ { 2 } + \kappa } { \varepsilon ^ { 2 } + \kappa } } } } } \displaystyle \frac { u ^ { 2 } d u } { 1 - \mathrm { ~ } \epsilon ^ { 2 } u ^ { 2 } } . } \end{array} \right.
$$

The integrals of these equations are

$$
\left\{ \begin{array} { l } { \displaystyle \frac { X ^ { \prime } } { x ^ { \prime } } = \frac { Y ^ { \prime } } { y ^ { \prime } } = - \frac { 2 \pi \alpha k ^ { 2 } } { \epsilon ^ { 3 } } \biggl [ \frac { a \epsilon } { \sqrt { a ^ { 2 } + \kappa } } \sqrt { 1 - \epsilon ^ { 2 } + \frac { a ^ { 2 } e ^ { - } } { a ^ { 2 } + \kappa } } } \\ { \displaystyle ~ - ~ ( 1 - \epsilon ^ { 2 } ) \log \biggr ( \frac { a \epsilon } { \sqrt { ( 1 - \epsilon ^ { 2 } ) ( a ^ { 2 } + \kappa ) } } } \\ { \displaystyle ~ + \sqrt { 1 + \frac { a ^ { 2 } e ^ { 2 } } { ( 1 - \epsilon ^ { 2 } ) ( a ^ { 2 } + \kappa ) } } \biggr ) , } \\ { \displaystyle \frac { Z ^ { \prime } } { z ^ { \prime } } = - 2 \pi \alpha k ^ { 2 } \frac { ( 1 - \epsilon ^ { 2 } ) } { \epsilon ^ { 3 } } \biggl ( \frac { - 2 \alpha \epsilon } { \sqrt { \epsilon ^ { 2 } + \kappa } } + \log \frac { 1 + \frac { c \epsilon } { \sqrt { c ^ { 2 } + \kappa } } } { 1 - \frac { c \epsilon } { \sqrt { c ^ { 2 } + \kappa } } } \biggr ) . } \end{array} \right.
$$

When the particle is interior to the spheroid the equations for the components of attraction are the same except that $\kappa = 0$

82.The Attraction at the Surfaces of Spheroids. The components of attraction for an interior particle,which are obtained in the case of an oblate spheroid from (56) by putting $\kappa = 0$ ， are,omitting the accents,

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { X } { x } = \displaystyle \frac { Y } { y } = - \ 2 \pi \sigma k ^ { 2 } \frac { \sqrt { 1 - e ^ { 2 } } } { e ^ { 3 } } [ - e \ \sqrt { 1 - e ^ { 2 } } + \sin ^ { - 1 } e ] , } \\ { \displaystyle \frac { Z } { z } = - \ 4 \pi \sigma \frac { k ^ { 2 } } { e ^ { 3 } } \Big [ e - \sqrt { 1 - e ^ { 2 } } \tan ^ { - 1 } \Big ( \frac { e } { \sqrt { 1 - e ^ { 2 } } } \Big ) \Big ] . } \end{array} \right.
$$

The limits of these expressions as the attracted particle approaches the surface of the spheroid are the components of attraction for a particle at the surface. As the attracted particle passes outward through the surface, $\kappa _ { s }$ in equations (56),starts with the value zero and increases continuously in such a manner that it always fulfills equation (46). Therefore equations (59)，having no discontinuity as the attracted particle reaches the surface,hold when $\textstyle x , y , z$ fulfill the equation of the ellipsoid.

When $e$ is small,as in the case of the planets,equations (59) are convenient when expanded as power series in e. On substituting the expansions

$$
\left\{ \begin{array} { r } { \sqrt { 1 - e ^ { 2 } } = 1 - \displaystyle \frac { e ^ { 2 } } { 2 } - \frac { e ^ { 4 } } { 8 } - \cdots , } \\ { \sin ^ { - 1 } e = e + \displaystyle \frac { e ^ { 3 } } { 6 } + \frac { 3 e ^ { 5 } } { 4 0 } + \cdots , } \\ { \sqrt { 1 - e ^ { 2 } } \tan ^ { - 1 } \Big ( \displaystyle \frac { e } { \sqrt { 1 - e ^ { 2 } } } \Big ) = e - \displaystyle \frac { e ^ { 3 } } { 3 } - \displaystyle \frac { 2 e ^ { 5 } } { 1 5 } + \cdots , } \end{array} \right.
$$

in equations (59),it is found that

$$
\left\{ \begin{array} { l l } { \displaystyle { \frac { X } { x } = \frac { Y } { y } = - \frac { 4 } { 3 } \pi \sigma k ^ { 2 } ( 1 - \frac { 1 } { 5 } e ^ { 2 } + \cdots ) , } } \\ { \displaystyle { \frac { Z } { z } = - \frac { 4 } { 3 } \pi \sigma k ^ { 2 } ( 1 + \frac { 2 } { 5 } e ^ { 2 } + \cdots ) . } } \end{array} \right.
$$

The mass of the spheroid is

$$
\begin{array} { r } { M = { \frac { 4 } { 5 } } \pi \sigma a ^ { 2 } c = { \frac { 4 } { 3 } } \pi \sigma a ^ { 3 } { \sqrt { 1 - e ^ { 2 } } } . } \end{array}
$$

The radius of a sphere having equal mas is defined by the equation

whence

$$
\begin{array} { c } { { M = { \frac { 4 } { 8 } } \pi \sigma R ^ { 3 } = { \frac { 4 } { 8 } } \pi \sigma a ^ { 3 } \sqrt { 1 - e ^ { 2 } } ; } } \\ { { { } } } \\ { { R = a ( 1 - e ^ { 2 } ) ^ { \sharp } . } } \end{array}
$$

The attraction of this sphere for a particle upon its surface is given by the equation

$$
{ \cal F } = - \frac { k ^ { 2 } M } { R ^ { 2 } } = - { \textstyle \frac { 4 } { 8 } } \pi \sigma k ^ { 2 } a ( 1 - e ^ { 2 } ) ^ { \tt b } .
$$

When the attracted particle is at the equator of the spheroid ${ \sqrt { x ^ { 2 } + y ^ { 2 } } } = a$ ； hence the ratio of the attraction of the spheroid for a particle at its equator to that of an equal sphere for a particle upon its surface is

$$
{ \frac { \sqrt { X ^ { 2 } + Y ^ { 2 } } } { F } } = { \frac { ( 1 - { \frac { 1 } { 5 } } e ^ { 2 } \cdot \cdot \cdot \cdot ) } { ( 1 - e ^ { 2 } ) ^ { \frac { 1 } { 6 } } } } = 1 - { \frac { e ^ { 2 } } { 3 0 } } + \cdot \cdot \cdot \cdot .
$$

This is less than unity when $e$ is small; therefore the attraction of the spheroid for a particle on its surface at its equator is less than that of a sphere having equal mass and volume for a particle on its surface.

When the attracted particle is at the pole of the spheroid $z = c = a { \sqrt { 1 - e ^ { 2 } } }$ ; hence in this case

$$
{ \frac { Z } { F } } = { \sqrt { 1 - e ^ { 2 } } } { \frac { ( 1 + { \frac { 2 } { 5 } } e ^ { 2 } \cdot \cdot \cdot ) } { ( 1 - e ^ { 2 } ) ^ { \frac { 1 } { 6 } } } } = 1 + { \frac { e ^ { 2 } } { 1 5 } } + \cdot \cdot \cdot .
$$

This is greater than unity when $e$ is small; therefore the attraction of the spheroid for a particle on its surface at its pole is greater than that of a sphere having equal mass and volume for a particle on its surface.

There is some place between the equator and pole at which the attractions are just equal. The latitude of this place will now be found. The coordinates of the particle must fulfill the equation of the spheroid； therefore

$$
f ( x , y , z ) \equiv \frac { x ^ { 2 } + y ^ { 2 } } { a ^ { 2 } } + \frac { z ^ { 2 } } { c ^ { 2 } } - 1 = 0 .
$$

The direction cosines of the normal to the surface at the point $( x , y , z )$ are

$$
\begin{array} { r l } & { \frac { \frac { \partial f } { \partial x } } { \sqrt { \left( \frac { \partial f } { \partial x } \right) ^ { 2 } + \left( \frac { \partial f } { \partial y } \right) ^ { 2 } + \left( \frac { \partial f } { \partial z } \right) ^ { 2 } } } , \qquad \frac { \frac { \partial f } { \partial y } } { \sqrt { \left( \frac { \partial f } { \partial x } \right) ^ { 2 } + \left( \frac { \partial f } { \partial y } \right) ^ { 2 } + \left( \frac { \partial f } { \partial z } \right) ^ { 2 } } } , } \\ & { \quad \quad \quad \quad \frac { \frac { \partial f } { \partial z } } { \sqrt { \left( \frac { \partial f } { \partial x } \right) ^ { 2 } + \left( \frac { \partial f } { \partial y } \right) ^ { 2 } + \left( \frac { \partial f } { \partial z } \right) ^ { 2 } } } . } \end{array}
$$

The last is the cosine of the angle between the normal at the point $( x , \ y , \ z )$ and the ${ \pmb z }$ -axis.and is. therefore, the sine of the

geographical latitude, which willbe represented by $\phi$ Hence, it follows from (62) that

$$
\begin{array} { c } { \sin \phi = \displaystyle \frac { \frac { \partial f } { \partial z } } { \sqrt { \left( \frac { \partial f } { \partial x } \right) ^ { 2 } + \left( \frac { \partial f } { \partial y } \right) ^ { 2 } + \left( \frac { \partial f } { \partial z } \right) ^ { 2 } } } } \\ { = \displaystyle \frac { z } { \sqrt { \left( x ^ { 2 } + y ^ { 2 } \right) \left( 1 - e ^ { 2 } \right) ^ { 2 } + z ^ { 2 } } } . } \end{array}
$$

From (62) and (63) it is found that

$$
\left\{ \begin{array} { l } { { \displaystyle x ^ { 2 } + y ^ { 2 } = \frac { a ^ { 2 } \cos ^ { 2 } \phi } { 1 - e ^ { 2 } \sin ^ { 2 } \phi } = a ^ { 2 } \cos ^ { 2 } \phi \{ 1 + e ^ { 2 } \sin ^ { 2 } \phi + \cdots \} , } } \\ { { \qquad z ^ { 2 } = \frac { a ^ { 2 } ( 1 - e ^ { 2 } ) ^ { 2 } \sin ^ { 2 } \phi } { 1 - e ^ { 2 } \sin ^ { 2 } \phi } } } \\ { { \qquad = a ^ { 2 } \sin ^ { 2 } \phi \{ 1 - e ^ { 2 } ( 1 + \cos ^ { 2 } \phi ) + \cdots \} . } } \end{array} \right.
$$

Let $\pmb { G }$ represent the whole attraction of the spheroid; then it is found from (60) and (64) that

$$
\begin{array} { l } { G = - \sqrt { \overline { { X ^ { 2 } + Y ^ { 2 } + Z ^ { 2 } } } } } \\ { = - \frac { 4 } { 8 } \pi \sigma k ^ { 2 } \sqrt { ( 1 - \frac { 1 } { 8 } e ^ { 2 } \cdot \cdot \cdot ) ^ { 2 } ( x ^ { 2 } + y ^ { 2 } ) + ( 1 + \frac { 4 } { 8 } e ^ { 2 } \cdot \cdot \cdot ) ^ { 2 } z ^ { 2 } } } \\ { = - \frac { 4 } { 8 } \pi \sigma k ^ { 2 } a \left\{ 1 - \frac { e ^ { 2 } } { 1 0 } ( 1 + \cos ^ { 2 } \phi ) + \cdot \cdot \cdot \right\} . } \end{array}
$$

The ratio of this expression to that for the attraction of a sphere of equal mass and volume, given by (61), is

$$
{ \frac { G } { F } } = { \frac { 1 - { \frac { e ^ { 2 } } { 1 0 } } ( 1 + \cos ^ { 2 } \phi ) \cdots } { ( 1 - e ^ { 2 } ) ^ { \tt t } } } = 1 - { \frac { e ^ { 2 } ( 1 - 3 \sin ^ { 2 } \phi ) } { 3 0 } } \cdots . \cdot .
$$

This becomes equal to unity up to terms of the fourth order in $\pmb { e }$ when $3 \sin ^ { 2 } \phi = 1 _ { \mathrm { { i } } }$ ,from which it is found that

$$
\phi = 3 5 ^ { \circ } 1 5 ^ { \prime } 5 2 ^ { \prime \prime } .
$$

Let $\pmb { r }$ represent the radius of the spheroid; then

$$
r ^ { 2 } = { \frac { a ^ { 2 } ( 1 - e ^ { 2 } ) } { 1 - e ^ { 2 } \cos ^ { 2 } \psi } } ,
$$

where $\psi$ is the angle between the radius and the plane of the equator. Since this angle differs from $\phi$ only by terms of the second and higher orders in $\pmb { \ell } _ { : }$ ,it follows that,with the degree of approximation employed,

$$
\ r ^ { 2 } = { \frac { a ^ { 2 } ( 1 - e ^ { 2 } ) } { 1 - e ^ { 2 } \cos ^ { 2 } \phi } } = a ^ { 2 } ( 1 - e ^ { 2 } ) ( 1 + e ^ { 2 } \cos ^ { 2 } \phi + \cdots ) .
$$

When $\phi = 3 5 ^ { \circ } 1 5 ^ { \prime } 5 2 ^ { \prime \prime }$ ，

$$
r ^ { 2 } = a ^ { 2 } \left( 1 - \frac { e ^ { 2 } } { 3 } + \cdot \cdot \cdot \right) .
$$

The radius of a sphere of equal volume has been found to be given by the equation

$$
R ^ { 2 } = a ^ { 2 } ( 1 - e ^ { 2 } ) ^ { \frac { 1 } { 3 } } = a ^ { 2 } \left( 1 - { \frac { e ^ { 2 } } { 3 } } + \cdot \cdot \cdot \right) ,
$$

which is seen to be equal to the radius of the spheroid up to terms of the second order inclusive in the eccentricity. Therefore,in the case of an oblate spheroid of small ecentricity,the intensity of the attraction is sensibly the same for a particle on its surface in latitude $\mathbf { 3 5 ^ { \circ } 1 5 ^ { \prime } 5 2 ^ { \prime \prime } }$ as that of a sphere having equal mass and volume for a particle on its surface；or, because of the equality of $\pmb { R }$ and $\pmb { r }$ ，a spheroid of small eccentricity attracts a particle on its surface in latitude $\mathbf { 3 5 ^ { \circ } 1 5 ^ { \prime } 5 2 ^ { \prime \prime } }$ with sensibly the same force it would exert if its mass were all at its center.

# XIII. PROBLEMS.

1. Show that Ivory's method can be applied when the attraction varieg as any power of the distance. 2.Show why Ivory's method cannot be used to find the potential of a solid ellipsoid upon an exterior particle when it is known for an interior particle. 3.Find the potential of a thin ellipsoidal shell contained between two similar ellipsoids upon an interior particle.Hint.It has been proved (Art.79) that the resultant attraction is zero at all interior points; therefore the potential is constant and it is sufficient to find it for the center.Let the semi-axes of the two surfaces be $a , b$ c and $( 1 + \mu ) a$ ， $( 1 + \mu ) b$ ， $( 1 + \mu ) c$ ；then the distance between the two surfaces measured along the radius from the eenter will be $\pmb { \mu \rho }$ .Therefore

$$
\begin{array} { l } { { \displaystyle { V = \sigma \mu \int _ { - \frac { \pi } { 2 } } ^ { \frac { \pi } { 2 } } \int _ { 0 } ^ { 2 \pi } { \frac { \rho ^ { 3 } \cos \phi d \phi d \theta } { \rho } } } } } \\ { { \displaystyle { \quad = \sigma \mu \int _ { - \frac { \pi } { 2 } } ^ { \frac { \pi } { 2 } } \int _ { 0 } ^ { 2 \pi } { \frac { \cos \phi d \phi d \theta } { \frac { \cos ^ { 2 } \phi } { a ^ { 2 } } + \frac { \cos ^ { 2 } \phi \sin ^ { 2 } \theta } { b ^ { 2 } } + \frac { \sin ^ { 2 } \phi } { c ^ { 2 } } } { b ^ { 2 } } } } } } \\ { { \displaystyle { \quad = 2 \pi \sigma \mu a b c \int _ { 0 } ^ { \infty } { \frac { d s } { \sqrt { ( a ^ { 2 } + s ) ( b ^ { 2 } + s ) ( c ^ { 2 } + s ) } } } . } } } \end{array}
$$

4.Show that in the case of two thin confocal shels similar elements of mass at points which correspond according to the definition (47) are proportional to the products of the three axes of the respective elipsoids.Then show,using problem 3 and Ivory's method,that the potential of an ellipsoidal shell upon an exterior particle is

$$
\begin{array} { c } { { V ^ { \prime } = 2 \pi \sigma \mu a b c \displaystyle \int _ { 0 } ^ { \infty } \displaystyle \frac { d s ^ { \prime } } { \sqrt { ( { a ^ { \prime } } ^ { 2 } + s ^ { \prime } ) ( { b ^ { \prime } } ^ { 2 } + s ^ { \prime } ) ( { c ^ { \prime } } ^ { 2 } + s ^ { \prime } ) } } } } \\ { { = 2 \pi \sigma \mu a b c \displaystyle \int _ { \kappa } ^ { \infty } \displaystyle \frac { d s } { \sqrt { ( a ^ { 2 } + s ) ( b ^ { 2 } + s ) ( c ^ { 2 } + s ) } } . } } \end{array}
$$

5.Prove that the level surfaces of thin homogeneous elipsoids are confocal elipsoids. What are the lines of force which are orthogonal to these surfaces?

6.Discuss the form of level surfaces when they are entirely exterior to homogeneous solid ellipsoids.

# HISTORICAL SKETCH AND BIBLIOGRAPHY.

The attractions of bodies were first investigated by Newton. His results are given in the Principia,Book 1., Secs. XI1.and xI1.，and are derived by synthetic processes similar to those used in the first part of this chapter. The problem of the attraction of ellipsoids has been the subject of many memoirs,and the case in which they are homogeneous was completely solved early in the nineteenth century. Among the important papers are those by Stirling,1735，Phil. Trans.；by Euler，1738, Petersburg;by Lagrange, 1773 and i775,Coll.Works,vol.I1.,p.619；by Laplace,1782,Méc. Cel., vol.I1.；by Ivory，1809-1828,Phil.Trans.；by Legendre，18l1，Mém.de l'Inst.de France,vol.x1.; by Gauss,Coll.Works,vol. v.;by Rodriguez,1816, Corres.sur l'Ecole Poly.,vol. I1.;by Poisson，1829,Conn.des Temps；by Green，1835，Math．Papers，yol.vi11.；Chasles，1837-1846，Jour.l'Ecole Poly.and Mém.des Savants Etrangers,vol.Ix.；MacCullagh，1847,Dublin Proc.,vol.I1.；Lejeune-Dirichlet,Journal de Liouville,vol.Iv.,and Crelle, vol. xxxII.

The earlier papers were devoted for the most part to the attractions of homogeneous ellipsoids of revolution upon particles in particular positions, as on the axis. Lagrange gave the general solution for the attractions of general homogeneous elipsoids upon interior particles. This was extended byIvory and Maclaurin (with Laplace's generalizations) to exterior particles. Ivory's theorem has been extended in a most interesting manner by Darboux in Note xvi. to the second volume of the Mécanique of Despeyrous. Chasles gave a synthetic proof of the theorems regarding the attractions of homogeneous ellipsoids in Mémoires des Savants Etrangers,vol.Ix.,and Lejeune-Dirichlet embraced in a most elegant manner in one discussion the case of both interior and exterior points by using a discontinuous factor (Liouville's Journal,vol. iv.).

Laplace proved that the potential for an exterior particle fulflls the partial differential equation

$$
\frac { \partial ^ { 2 } V } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } V } { \partial y ^ { 2 } } + \frac { \partial ^ { 2 } V } { \partial z ^ { 2 } } = 0 ,
$$

and determined $V$ bythe condition that it must bea function satisfying this equation.This is a process of great generality，and is relatively simple except in the trivial cases.This has been made the starting-point of most of the investigations of the latter part of the last century,especially where the attracting bodies are not homogeneous.In a paper on Electricity and Magnetism,in 1828,Green introduced the term potential function for V,and discussed many of its mathematical properties.Green's memoir remained nearly unknown until about 1846.and in the meantime many of his theorems had been rediscovered by Chasles,Gauss,Sturm,and Thomson.One of Green's theorems has found an extremely useful application，when the independent variables are two in number,in the Theory of Functions.

Poisson showed that the potential function for an interior particle fulfills the partial differential equation

$$
\begin{array} { r } { \frac { \partial ^ { 2 } V } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } V } { \partial y ^ { 2 } } + \frac { \partial ^ { 2 } V } { \partial z ^ { 2 } } = - \ 4 \pi \sigma . } \end{array}
$$

Among the books treating the subject of attractions and potential may be mentioned Thomson and Tait's Natural Philosophy，part I.，Neumann's Potential,Poincaré's Potential,Routh'sAnalytical Statics,vol.I1.,and Tisserand's Mécanique Celeste,vol. I1．The last-mentioned develops most fully the astronomical applications and should be used in further reading.

The attractions of spheroids and ellipsoids has been fundamental in the discussions of possible figures of equilibrium of rotating fluids. The reason is,of course,that the conditions for equilibrium involve the components of attraction. Maclaurin proved in 1742 that for slow rotation an oblate spheroid, whose eccentricity is a function of the rate of rotation and the density of the fluid,is a figure of equilibrium.There are,indeed,two such figures； for slow rotation one is nearly spherical and the other is very much flattened.For faster rotation the figures are more nearly of the same shape； for a certain greater rate of rotation they are identical;and for still faster rotation no spheroid is a figure of equilibrium．In 1834 Jacobi proved that when the rate of rotation is not too great there is an ellipsoid of three unequal axes which is & figure of equilibrium,which for a certain rate of rotation coincides with the more nearly spherical of the Maclaurin spheroids.For this work Tisserand's Mecanique Celeste,vol. I1.,should be consulted.In a very important memoir (Acta Mathematic, vol. vi.) Poincaré proved that there are infinitely many other figures of equilibrium which,for certain values of the rate of rotation, coincide with the corresponding Jacobian elipsoid,as it,for a certain rate of rotation,coincides with the Maclaurin spheroid. The least elongated of these figures is larger at one end than it is at the other,and was called the apioid,that is, the pear-shaped figure.Later computations by Sir George Darwin (Philosophical Transactions,vol.198) have shown it is so elongated that it might well be called a cucumber-shaped figure.

# CHAPTER V.

# THE PROBLEM OF TWO BODIES.

83.Equations of Motion. It will be assumed in this chapter that the two bodies are spheres and homogeneous in concentric layers.Then,in accordance with the results obtained in Art.69, they will attract each other with a force which is proportional to the product of their masses and which varies inversely as the square of the distance between their centers.

Let $\pmb { m _ { 1 } }$ and $\mathbf { \Delta } m _ { 2 }$ represent the masses of the two bodies,and ${ m _ { 1 } + m _ { 2 } = M }$ Choose an arbitrary system of rectangular axes in space and let the coordinates of $\pmb { m _ { 1 } }$ and $\mathbf { \Delta } m _ { 2 }$ referred to it be respectively $( \xi _ { 1 } , \eta _ { 1 } , \zeta _ { 1 } )$ and $( \xi _ { 2 } , \eta _ { 2 } , \zeta _ { 2 } )$ .Let the distance between $m _ { 1 }$ and $\mathbf { \Delta } m _ { 2 }$ be denoted by $\pmb { r }$ ; then it follows from the laws of motion and the law of gravitation that the differential equations which the coordinates of the bodies satisfy are

$$
\left\{ \begin{array} { l l } { m _ { 1 } \frac { \partial \hat { \lambda } _ { 1 } } { \partial t ^ { 2 } } = - k ^ { 2 } m _ { 1 } m _ { 2 } \frac { ( \hat { \lambda } _ { 1 } - \hat { \lambda } _ { 2 } ) } { r ^ { 3 } } , } \\ { m _ { 1 } \frac { \partial \hat { \lambda } _ { 1 } } { \partial t ^ { 2 } } = - k ^ { 2 } m _ { 1 } m _ { 2 } \frac { ( \hat { \lambda } _ { 1 } - \hat { \eta } _ { 1 } ) } { r ^ { 3 } } , } \\ { m _ { 1 } \frac { \partial \hat { \lambda } _ { 1 } } { \partial t ^ { 2 } } = - k ^ { 2 } m _ { 1 } m _ { 2 } \frac { ( \hat { \lambda } _ { 1 } - \hat { \lambda } _ { 2 } ) } { r ^ { 5 } } , } \\ { m _ { 2 } \frac { \partial \hat { \lambda } _ { 2 } } { \partial t ^ { 2 } } = - k ^ { 2 } m _ { 1 } m _ { 1 } \frac { ( \hat { \lambda } _ { 2 } - \hat { \lambda } _ { 1 } ) } { r ^ { 3 } } , } \\ { m _ { 2 } \frac { \partial \hat { \lambda } _ { 2 } } { \partial t ^ { 2 } } = - k ^ { 2 } m _ { 2 } m _ { 1 } \frac { ( \hat { \lambda } _ { 2 } - \hat { \eta } _ { 1 } ) } { r ^ { 3 } } , } \\ { m _ { 2 } \frac { \partial \hat { \lambda } _ { 2 } } { \partial t ^ { 2 } } = - k ^ { 2 } m _ { 2 } m _ { 1 } \frac { ( \hat { \lambda } _ { 2 } - \hat { \eta } _ { 1 } ) } { r ^ { 3 } } , } \\ { m _ { 2 } \frac { \partial \hat { \lambda } _ { 2 } } { \partial t ^ { 2 } } = - k ^ { 2 } m _ { 2 } m _ { 1 } \frac { ( \hat { \lambda } _ { 2 } - \hat { \lambda } _ { 1 } ) } { r ^ { 3 } } . } \end{array} \right.
$$

In order to solve these six simultaneous equations of the second order twelve integrals must be found. They will introduce twelve arbitrary constants of integration which can be determined in any particular case by the three initial coordinntes and the three components of the initial velocity of each of the bodies.

84.The Motion of the Center of Mass. On adding the first and fourth, the second and fifth,and the third and sixth equations of the system (1),it is found that

$$
\left\{ \begin{array} { l l } { m _ { 1 } \displaystyle \frac { d ^ { 2 } \xi _ { 1 } } { d t ^ { 2 } } + m _ { 2 } \displaystyle \frac { d ^ { 2 } \xi _ { 2 } } { d t ^ { 2 } } = 0 , } \\ { m _ { 1 } \displaystyle \frac { d ^ { 2 } \eta _ { 1 } } { d t ^ { 2 } } + m _ { 2 } \displaystyle \frac { d ^ { 2 } \eta _ { 2 } } { d t ^ { 2 } } = 0 , } \\ { m _ { 1 } \displaystyle \frac { d ^ { 2 } \xi _ { 1 } } { d t ^ { 2 } } + m _ { 2 } \displaystyle \frac { d ^ { 2 } \zeta _ { 2 } } { d t ^ { 2 } } = 0 . } \end{array} \right.
$$

These equations are immediately integrable,and give

$$
\begin{array} { l } { \displaystyle \left\{ m _ { 1 } \frac { d \xi _ { 1 } } { d t } + m _ { 2 } \frac { d \xi _ { 2 } } { d t } = \alpha _ { 1 } , \right. } \\ { \displaystyle \left\{ m _ { 1 } \frac { d \eta _ { 1 } } { d t } + m _ { 2 } \frac { d \eta _ { 2 } } { d t } = \beta _ { 1 } , \right. } \\ { \displaystyle \left. m _ { 1 } \frac { d \xi _ { 1 } } { d t } + m _ { 2 } \frac { d \xi _ { 2 } } { d t } = \gamma _ { 1 } . \right. } \end{array}
$$

On integrating again they become

$$
\left\{ { \begin{array} { l } { m _ { 1 } \xi _ { 1 } + m _ { 2 } \xi _ { 2 } = \alpha _ { 1 } t + \alpha _ { 2 } , } \\ { m _ { 1 } \eta _ { 1 } + m _ { 2 } \eta _ { 2 } = \beta _ { 1 } t + \beta _ { 2 } , } \\ { m _ { 1 } \xi _ { 1 } + m _ { 2 } \xi _ { 2 } = \gamma _ { 1 } t + \gamma _ { 2 } . } \end{array} } \right.
$$

Thus, six of the twelve integrals are found, the arbitrary constants of integration being $\alpha _ { 1 } , \alpha _ { 2 } , \beta _ { 1 } , \beta _ { 2 } , \gamma _ { 1 } , \gamma _ { 2 } .$

Let $\overline { { \xi } } , \ \overline { { \eta } } ,$ and $\overline { { \xi } }$ be the coordinates of the center of mass of the system; then it follows from Art.19 and equations (3) that

$$
\left\{ \begin{array} { l l } { M \overline { { \xi } } = m _ { 1 } \xi _ { 1 } + m _ { 2 } \xi _ { 2 } = \alpha _ { 1 } t + \alpha _ { 2 } , } \\ { M \overline { { \eta } } = m _ { 1 } \eta _ { 1 } + m _ { 2 } \eta _ { 2 } = \beta _ { 1 } t + \beta _ { 2 } , } \\ { M \overline { { \xi } } = m _ { 1 } \xi _ { 1 } + m _ { 2 } \xi _ { 2 } = \gamma _ { 1 } t + \gamma _ { 2 } . } \end{array} \right.
$$

From these equations it follows that the coordinates increase directly as the time,and, therefore, that the center of mass moves with uniform velocity. Or, taking their derivatives, squaring, and adding,it is found that

$$
M ^ { 2 } \Big \{ \bigg ( \frac { d \overline { { \xi } } } { d t } \bigg ) ^ { 2 } + \bigg ( \frac { d \overline { { \eta } } } { d t } \bigg ) ^ { 2 } + \bigg ( \frac { d \overline { { \xi } } } { d t } \bigg ) ^ { 2 } \Big \} = \alpha _ { 1 } { } ^ { 2 } + \beta _ { 1 } { } ^ { 2 } + \gamma _ { 1 } { } ^ { 2 } ;
$$

whence

$$
\overline { { { V } } } = \frac { \sqrt { { \alpha _ { 1 } } ^ { 2 } + \beta _ { 1 } ^ { 2 } + { \gamma _ { 1 } } ^ { 2 } } } { M } ,
$$

where $\overline { { V } }$ represents the speed with which the center of mass moves. The speed is therefore constant.

On eliminating $\scriptstyle t$ from (4),it is found that

$$
\frac { \overline { { M \bar { \xi } } } - \alpha _ { 2 } } { \alpha _ { 1 } } = \frac { \overline { { M \eta } } - \beta _ { 2 } } { \beta _ { 1 } } = \frac { \overline { { M \bar { \xi } } } - \gamma _ { 2 } } { \gamma _ { 1 } } .
$$

The coordinates of the center of mass fulfll these relations which are the symmetrical equations of a straight line in space; therefore, the center of mass moves in $^ { a }$ straight line with constant speed.

85.The Equations for Relative Motion. Take a new system of axes parallel to the old,but with the origin at the center of mass of the two bodies. Let the coordinates of $m _ { 1 }$ and $\mathbf { \Delta } m _ { 2 }$ referred to this new system be $x _ { 1 } , \ y _ { 1 } , \ z _ { 1 }$ and $x _ { 2 } , \ y _ { 2 } , \ z _ { 2 }$ respectively.They are related to the old coordinates by the equations

$$
\left\{ \begin{array} { l l } { x _ { 1 } = \xi _ { 1 } - \overline { { \xi } } , } & { x _ { 2 } = \xi _ { 2 } - \overline { { \xi } } , } \\ { y _ { 1 } = \eta _ { 1 } - \overline { { \eta } } , } & { y _ { 2 } = \eta _ { 2 } - \overline { { \eta } } , } \\ { z _ { 1 } = \xi _ { 1 } - \overline { { \xi } } ; } & { z _ { 2 } = \xi _ { 2 } - \overline { { \xi } } . } \end{array} \right.
$$

On substituting in (1), the differential equations of motion in the new variables are found to be

$$
\left\{ \begin{array} { l l } { m _ { 1 } \frac { \partial \overline { { x } } _ { 2 } } { \partial t ^ { 2 } } = - k ^ { 2 } m _ { 1 } m _ { 2 } \frac { \left( \overline { { x } } _ { 1 } - \overline { { x } } _ { 2 } \right) } { r ^ { 3 } } , } \\ { m _ { 1 } \frac { \partial \overline { { y } } _ { 1 } } { \partial t ^ { 2 } } = - k ^ { 2 } m _ { 1 } m _ { 2 } \frac { \left( \overline { { y } } _ { 1 } - \overline { { y } } _ { 2 } \right) } { r ^ { 3 } } , } \\ { m _ { 1 } \frac { \partial \overline { { z } } _ { 1 } } { \partial t ^ { 3 } } = - k ^ { 2 } m _ { 1 } m _ { 2 } \frac { \left( \overline { { x } } _ { 1 } - \overline { { z } } _ { 2 } \right) } { r ^ { 3 } } , } \\ { m _ { 2 } \frac { \partial \overline { { x } } _ { 2 } } { \partial t ^ { 3 } } = - k ^ { 2 } m _ { 2 } m _ { 1 } \frac { \left( \overline { { x } } _ { 2 } - \overline { { x } } _ { 1 } \right) } { r ^ { 3 } } , } \\ { m _ { 2 } \frac { \partial \overline { { y } } _ { 2 } } { \partial t ^ { 2 } } = - k ^ { 2 } m _ { 2 } m _ { 1 } \frac { \left( \overline { { y } } _ { 2 } - \overline { { y } } _ { 1 } \right) } { r ^ { 3 } } , } \\ { m _ { 2 } \frac { \partial \overline { { z } } _ { 2 } } { \partial t ^ { 2 } } = - k ^ { 2 } m _ { 2 } m _ { 1 } \frac { \left( \overline { { z } } _ { 2 } - \overline { { y } } _ { 2 } \right) } { r ^ { 3 } } , } \end{array} \right.
$$

which are of the same form as the equations for absolute motion.

The coordinates of the center of mass are given by equations (4); therefore if $x _ { 1 } , \ y _ { 1 } ,$ ······, ${ \pmb z } _ { 2 }$ were known，and if the constants $\alpha _ { 1 } , ~ \alpha _ { 2 } , ~ \beta _ { 1 } , ~ \beta _ { 2 } , ~ \gamma _ { 1 } ,$ and $\gamma _ { 2 }$ were known,the absolute positions in space could be found. But, since there is no way of determining these constants,the problem of relative motion，as expressed in (6),is all that can be solved.

Since the new origin is at the center of mass,the coordinates are related by the equations

$$
\left\{ { \begin{array} { l } { m _ { 1 } x _ { 1 } + m _ { 2 } x _ { 2 } = 0 , } \\ { m _ { 1 } y _ { 1 } + m _ { 2 } y _ { 2 } = 0 , } \\ { m _ { 1 } z _ { 1 } + m _ { 2 } z _ { 2 } = 0 . } \end{array} } \right.
$$

Therefore,when the coordinates of one body with respect to the center of mass of the two are known the coordinates of the second body &re given by equations (7).

Equations (7） can be used to eliminate $x _ { 2 } , \ y _ { 2 } ,$ and ${ \boldsymbol { z } } _ { 2 }$ from the first three equations of (6),and $x _ { 1 } , \ y _ { 1 } ,$ and ${ \pmb z _ { 1 } }$ from the last three. The results of the elimination are

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \frac { d ^ { 2 } x _ { 1 } } { d \theta ^ { 2 } } = - k ^ { 2 } M \frac { x _ { 1 } } { r ^ { 3 } } , } \\ { \frac { d ^ { 3 } y _ { 1 } } { d \theta ^ { 2 } } = - k ^ { 2 } M \frac { y _ { 1 } } { r ^ { 3 } } , } \\ { \frac { d ^ { 2 } z _ { 1 } } { d \theta ^ { 3 } } = - k ^ { 2 } M \frac { z _ { 1 } } { r ^ { 3 } } , } \\ { \frac { d ^ { 2 } x _ { 2 } } { d \theta ^ { 2 } } = - k ^ { 2 } M \frac { x _ { 2 } } { r ^ { 3 } } , } \\ { \frac { d ^ { 2 } x _ { 3 } } { d \theta ^ { 2 } } = - k ^ { 2 } M \frac { x _ { 3 } } { r ^ { 3 } } , } \\ { \frac { d ^ { 2 } y _ { 2 } } { d \theta ^ { 2 } } = - k ^ { 2 } M \frac { y _ { 2 } } { r ^ { 3 } } , } \\ { \frac { d ^ { 2 } z _ { 2 } } { d \theta ^ { 2 } } = - k ^ { 2 } M \frac { z _ { 3 } } { r ^ { 3 } } . } \end{array} \right. } \end{array}
$$

In the first three equations the $r$ which appears in the right member must be expressed in terms of $x _ { 1 } , \ y _ { 1 }$ ，and ${ \pmb z _ { 1 } }$ ；and in the second three it must be expressed in terms of $x _ { 2 } , y _ { 2 } ,$ and ${ \pmb z } _ { 2 }$ It follows from equations(7） that

$$
{ \frac { M } { m _ { 2 } } } \ { \sqrt { x _ { 1 } { } ^ { 2 } + y _ { 1 } { } ^ { 2 } + z _ { 1 } { } ^ { 2 } } } = { \frac { M } { m _ { 2 } } } r _ { 1 } = { \frac { M } { m _ { 1 } } } r _ { 2 } = r .
$$

The equations in $x _ { 1 } , y _ { 1 } , z _ { 1 }$ are now independent of those in $x _ { 2 } , y _ { 2 } , z _ { 2 } ,$ and conversely. But what is really desired in practice is the

motion of one body with respect to the other. Let $\pmb { x } , \ \hat { \pmb { y } } _ { 1 }$ and a represent the coordinates of $\mathbf { \Delta } m _ { 2 }$ with respect to ${ \mathbf { } } m _ { 1 }$ then

$$
x = x _ { 2 } - x _ { 1 } , y = y _ { 2 } - y _ { 1 } , z = z _ { 2 } - z _ { 1 } .
$$

Hence if the frst,second,and third equations of (8) are subtracted from the fourth,fth,and sixth equations respectively,the results are, as a consequence of these relations,

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } x } { d t ^ { 2 } } = - k ^ { 2 } M \displaystyle \frac { x } { r ^ { 3 } } . } \\ { \displaystyle \frac { d ^ { 2 } y } { d t ^ { 2 } } = - k ^ { 2 } M \displaystyle \frac { y } { r ^ { 3 } } , } \\ { \displaystyle \frac { d ^ { 2 } z } { d t ^ { 2 } } = - k ^ { 2 } M \displaystyle \frac { z } { r ^ { 3 } } . } \end{array} \right.
$$

The problem is now of the sixth order,having been reduced from the twelfth by means of the six integrals (2) and (3). The six new constants of integration which will be introduced in integrating equations (9) will be determined by the three initial coordinates,and the three projections of the initial velocity of ${ \pmb m } _ { \bf 1 }$ with respect to $\mathbf { \Delta } m _ { 2 }$

86.The Integrals of Areas. Multiply the first equation of (9) by $- \ y ,$ and the second by $+ x ,$ ,and add； the result is

$$
\left\{ \begin{array} { l l } { { x \displaystyle { \frac { d ^ { 2 } y } { d t ^ { 2 } } } - y \displaystyle { \frac { d ^ { 2 } x } { d t ^ { 2 } } } = 0 \mathrm { , ~ a n d } } } \\ { { y \displaystyle { \frac { d ^ { 2 } z } { d t ^ { 2 } } } - z \displaystyle { \frac { d ^ { 2 } y } { d t ^ { 2 } } } = 0 } , } \\ { { z \displaystyle { \frac { d ^ { 2 } x } { d t ^ { 2 } } } - x \displaystyle { \frac { d ^ { 2 } z } { d t ^ { 2 } } } = 0 } . } \end{array} \right.
$$

The integrals of these equations are

$$
\left\{ \begin{array} { l l } { { \displaystyle x { \frac { d y } { d t } } - y { \frac { d x } { d t } } = a _ { 1 } , } } \\ { { \displaystyle y { \frac { d z } { d t } } - z { \frac { d y } { d t } } = a _ { 2 } , } } \\ { { \displaystyle z { \frac { d x } { d t } } - x { \frac { d z } { d t } } = a _ { 3 } . } } \end{array} \right.
$$

It follows from Art.16 that $a _ { 1 } , ~ a _ { 2 } , ~ a _ { 3 }$ are the projections of twice the areal velocity upon the $x y , y z$ and ${ \pmb z x }$ -planes respectively.

Upon multiplying equations (10) by $z , x ,$ and $\boldsymbol { y }$ respectively， and adding,it is found that

$$
a _ { 1 } z + a _ { 2 } x + a _ { 3 } y = 0 .
$$

This is the equation of a plane passing through the origin,and it follows from its derivation that the coordinates of $\pmb { m } _ { 1 }$ always fulfill it; therefore,the motion of one body with respect to the otheris in a plane which passes through the center of the other.

The constants $a _ { 1 } , \ a _ { 2 } ,$ and $a _ { 3 }$ determine the position of the plane of the orbit with respect to the axes of reference. In polar coordinates equation (11） becomes

$$
a _ { 1 } \sin \varphi + a _ { 2 } \cos \varphi \cos \theta + a _ { 3 } \cos \varphi \sin \theta = 0 .
$$

The $\pmb { x y }$ -plane and the plane of the orbit intersect in a line $\pmb { L }$ (Fig.25).Suppose $o L$ is that half line which passes through the point at which the body $\displaystyle m _ { 1 }$ goes from the negative to the positive side of the xy-plane. Let $\boldsymbol { \Omega }$ represent the angle between the positive end of the $\pmb { x }$ -axis and the line $O L$ counted in the positive direction from $o { \mathfrak { x } }$ This angle may have any value from $0 ^ { \circ }$ to $3 6 0 ^ { \circ }$ Let $\textit { i }$ represent the inclination between the two planes counted in the direction of positive rotation around $O L$ The angle $\mathbf { \chi } _ { i } ^ { \phantom { \dagger } }$ may have any value from $0 ^ { \circ }$ to $1 8 0 ^ { \circ }$ It is less or greater than $9 0 ^ { \circ }$ according as ${ a } _ { 1 }$ is positive or negative. Then, when $\varphi = 0$ the value of $\theta$ is $6 8$ or $\delta \stackrel { } { + } \pi$ When $\theta = \delta \delta + { \textstyle { \frac { 1 } { 2 } } } \pi$ the value of $\pmb { \varphi }$ is $_ { i }$ or $\pi - i$ according as $_ i$ is less than or greater than $9 0 ^ { \circ }$ .In these cases equation (12) becomes respectively

![](images/836e99c333f075556f5a1923c84182ae1036e6e92c417a77e08e85b14118b4bd.jpg)  
Fig. 25.

$$
\left\{ \begin{array} { l l } { a _ { 2 } \cos { \Omega } + a _ { 3 } \sin { \Omega } = 0 , } \\ { a _ { 1 } \sin { i } = a _ { 2 } \cos { i } \sin { \Omega } \triangleq a _ { 3 } \cos { i } \cos { \Omega } = 0 , } \end{array} \right.
$$

where the signs of the second equation are the upper if $\mathbf { \chi } _ { i } ^ { \bullet }$ is less than $9 0 ^ { \circ }$ ,and the lower if it is greater than $9 0 ^ { \circ }$ ·

Since the projections of the areal velocity upon the three fundamental planes are constants (viz., $\scriptstyle { \frac { 1 } { 2 } } a _ { 1 } , { \frac { 1 } { 2 } } a _ { 2 } ,$ and $\scriptstyle { \frac { 1 } { 2 } } a _ { 3 } ,$ ,the areal velocity in the plane of the orbit is also constant. Let this constant be represented by $\scriptstyle { \frac { 1 } { 2 } } c _ { 1 }$ ；then

$$
c _ { 1 } = \sqrt { { a _ { 1 } } ^ { 2 } + { a _ { 2 } } ^ { 2 } + { a _ { 3 } } ^ { 2 } } ,
$$

where the positive value of the square root is taken. On solving (13)and (14) for ${ a } _ { 1 } , { a } _ { 2 }$ and $a _ { 3 } ,$ it is found that

$$
\left\{ \begin{array} { l l } { a _ { 1 } = + c _ { 1 } \cos i , } \\ { a _ { 2 } = \pm c _ { 1 } \sin i \sin \delta \sin , } \\ { a _ { 3 } = \mp c _ { 1 } \sin i \cos \delta \partial , } \end{array} \right.
$$

where the upper or lower signs are to be taken in the last two equations according as $\Dot { \iota }$ is less than or greater than $9 0 ^ { \circ }$ ; that is, according as ${ \pmb a } _ { \bf 1 }$ is positive or negative. With this understanding equations (15） uniquely determine $_ { i }$ and $\displaystyle { \delta \boldsymbol { \mathbf { \rho } } }$ ，which uniquely determine the position of the plane of the orbit.

87.Problem in the Plane. Since the orbit lies in a known plane, the coordinate axes may be chosen so that the $_ { \pmb { x } }$ and $y .$ -axes liə in this plane. If the coordinates are represented by $_ { x }$ and $\pmb { y }$ as before, the differential equations of motion are

$$
\left\{ \begin{array} { l } { { \displaystyle \frac { d ^ { 2 } x } { d t ^ { 2 } } = - k ^ { 2 } M \displaystyle \frac { x } { r ^ { 3 } } , } } \\ { { \displaystyle \frac { d ^ { 2 } y } { d t ^ { 2 } } = - k ^ { 2 } M \displaystyle \frac { y } { r ^ { 3 } } . } } \end{array} \right.
$$

The problem is now of the fourth order instead of the sixth as it was in (9),having been reduced by means of the integrals (10). It will be observed that,since the position of the plane is defined by the two elements $\boldsymbol { \Omega }$ and $i _ { \cdot }$ ，orby the ratios of $a _ { 1 } , \ a _ { 2 } ,$ and $a _ { 3 }$ in (11)，only two of the arbitrary constants were involved in the reduction. This probiem might be solved by deriving the differential equation of the orbit as in Art.54 and integrating as in Art.62, the last integral being derived from the integral of areas; but,it is preferable to obtain the results directly by the method which is usually employed in Celestial Mechanics.

Equations (16) give

$$
x \ : \frac { d ^ { 2 } y } { d t ^ { 2 } } - y \frac { d ^ { 2 } x } { d t ^ { 2 } } = 0 .
$$

The integral of this equation is

$$
x \ : \frac { d y } { d t } - y \frac { d x } { d t } = c _ { 1 } ,
$$

which becomes in polar coordinates

$$
r ^ { 2 } { \frac { d \theta } { d t } } = c _ { 1 } .
$$

Let $\pmb { A }$ represent the area swept over by the radius vector $\pmb { r }$ ; then

$$
\textbf { 2 } \frac { d A } { d t } = r ^ { 2 } \frac { d \theta } { d t } = c _ { 1 } ;
$$

whence

$$
2 A = c _ { 1 } t + c _ { 2 } ,
$$

from which it follows that the areas swept over by the radius vector are proportional to the times in which they are described.

On multiplying (16) by $2 \ { \frac { d x } { d t } } \operatorname { a n d } \ 2 \ { \frac { d y } { d t } }$ respectively, and ading, the result is

$$
\begin{array} { r } { 2 \frac { d ^ { 2 } x } { d t ^ { 2 } } \frac { d x } { d t } + 2 \frac { d ^ { 2 } y } { d t ^ { 2 } } \frac { d y } { d t } = - 2 \frac { k ^ { 2 } M } { r ^ { 3 } } \left( x \frac { d x } { d t } + y \frac { d y } { d t } \right) = - \frac { 2 k ^ { 2 } M } { r ^ { 2 } } \frac { d r } { d t } . } \end{array}
$$

The integral of this equation is

$$
\left( { \frac { d x } { d t } } \right) ^ { 2 } + \left( { \frac { d y } { d t } } \right) ^ { 2 } = { \frac { 2 k ^ { 2 } M } { r } } + c _ { 3 } .
$$

This equation, which involves only the square _of the velocity and the distance, is known as the vis viva integral (Art. 52). On transforming the left member to polar coordinates,this equation becomes

$$
\left( { \frac { d r } { d t } } \right) ^ { 2 } + r ^ { 2 } \left( { \frac { d \theta } { d t } } \right) ^ { 2 } = { \frac { 2 k ^ { 2 } M } { r } } + c _ { 4 } .
$$

But

$$
{ \frac { d r } { d t } } = { \frac { d r } { d \theta } } { \frac { d \theta } { d t } } ;
$$

therefore

$$
\left( { \frac { d \theta } { d t } } \right) ^ { 2 } \left\{ \left( { \frac { d r } { d \theta } } \right) ^ { 2 } + r ^ { 2 } \right\} = { \frac { 2 k ^ { 2 } M } { r } } + c _ { 3 } .
$$

On eliminating $\frac { d \theta } { d t }$ by meansof (17),this equatiogive

$$
d \theta = { \frac { c _ { 1 } d r } { r { \sqrt { - { \ c _ { 1 } } ^ { 2 } + 2 k ^ { 2 } M r + { \ c _ { 3 } } r ^ { 2 } } } } } ,
$$

which may be written in the form

$$
d \theta = \frac { - d \left( \frac { c _ { 1 } } { r } \right) } { \sqrt { c _ { 3 } + \frac { k ^ { 4 } M ^ { 2 } } { { c _ { 1 } } ^ { 2 } } - \left( \frac { k ^ { 2 } M } { c _ { 1 } } - \frac { c _ { 1 } } { r } \right) ^ { 2 } } } .
$$

Let $B ^ { 2 }$ and $\textbf { \em u }$ be defined by

$$
\begin{array} { l } { { \{ c _ { 3 } + \frac { k ^ { 4 } M ^ { 2 } } { { c _ { 1 } } ^ { 2 } } = B ^ { 2 } ,  } } \\ { { \{  \frac { k ^ { 2 } M } { c _ { 1 } } - \frac { c _ { 1 } } { r } = - \mathrm { \Delta } u ,  } } \end{array}
$$

in which $B ^ { 2 }$ must be positive for a real orbit; then (20) becomes

$$
d \theta = \frac { - d u } { \sqrt { B ^ { 2 } - { \overline { { u ^ { 2 } } } } } } .
$$

The integral of this equation is

$$
\theta = \cos ^ { - 1 } { \frac { u } { B } } + c _ { 4 } .
$$

On changing from $u , B _ { \mathrm { : } }$ and $\pmb { c _ { 4 } }$ to $\pmb { r }$ and the original constants,it is found that

$$
r = \frac { c _ { 1 } } { \frac { \vec { k } ^ { 2 } M } { c _ { 1 } } - \sqrt { c _ { 3 } + \frac { \vec { k } ^ { 4 } M ^ { 2 } } { { c _ { 1 } } ^ { 2 } } \cos { \mathrm { ~ } } ( \theta - c _ { 4 } ) } } ,
$$

which is the polar equation of a conic section with the origin at one of its foci.

88.The Elements in Terms of the Constants of Integration. The node and inclination are expressed in terms of the constants of integration by (15).

The ordinary equation of a conic section with the origin at the right-hand focus is

$$
r = \frac { p } { 1 + e \cos ( \theta - \omega ) } ,
$$

where $p$ is the semi-parameter,and $\omega$ is the angle between the polar axis and the major axis of the conic. On comparing this equation with (21),it is found that

$$
\left\{ \begin{array} { l } { { p = \frac { c _ { 1 } ^ { 2 } } { k ^ { 2 } M } , } } \\ { { \epsilon ^ { 2 } = 1 + \frac { c _ { 1 } ^ { 2 } c _ { 3 } } { k ^ { 4 } M ^ { 2 } } , } } \\ { { \omega = c _ { 4 } - \pi ; } } \\ { { c _ { 1 } = k \sqrt { M p } , } } \\ { { { } } } \\ { { c _ { 3 } = - \frac { k ^ { 2 } ( 1 - e ^ { 2 } ) } { p } M . } } \end{array} \right.
$$

When $e ^ { 2 } < 1$ ，the orbit is an ellipse and $p = a ( 1 - e ^ { 2 } )$ ，where $^ { a }$ is the major semi-axis;when $e ^ { 2 } = 1$ ,the orbit isa parabola and ${ \mathfrak { p } } = 2 q ;$ ，where $q$ is the distance from the origin to the vertex of the parabola；and when $e ^ { 2 } > 1$ ，the orbit is an hyperbola and $p = a ( e ^ { 2 } - 1 )$

Let $\scriptstyle A _ { 0 }$ represent the area described at the time the body passes perihelion;\* then the time of perihelion passage is found from equation (18) to be

$$
\pmb { T } = \frac { 2 A _ { 0 } - c _ { 2 } } { c _ { 1 } } .
$$

This completes the determination of the elements in terms of the constants of integration. They are defined in terms of the initial coordinates and components of velocity by the equations where they first occur,viz.,(10),(17),(18),(19),and (21).

89.Properties of the Motion. Suppose the orbit is an ellpse. Then，when the values of the constants of integration given in (22) are substituted in (17) and (i9),these equations become

$$
\left\{ \begin{array} { c } { { r ^ { 2 } \displaystyle \frac { d \theta } { d t } = k ~ \sqrt { M a ( 1 - e ^ { 2 } ) } , } } \\ { { \left( \displaystyle \frac { d x } { d t } \right) ^ { 2 } + \left( \displaystyle \frac { d y } { d t } \right) ^ { 2 } = V ^ { 2 } = k ^ { 2 } M \left( \displaystyle \frac { 2 } { r } - \displaystyle \frac { 1 } { a } \right) , } } \end{array} \right.
$$

where $V$ is the speed in the orbit at the distance $\pmb { r }$ from the origin. When the orbit isa circle, $r = a$ and

\* Unless $\mathbf { \Delta } m _ { 2 }$ is specified to be some body other than the sun the nearest apse will be called the perihelion point.

$$
V _ { c } ^ { 2 } = \frac { k ^ { 2 } M } { r } .
$$

When the orbit is a parabola, $a = \infty$ and

$$
{ V _ { p } } ^ { 2 } = { \frac { 2 k ^ { 2 } M } { r } } .
$$

Therefore,at a given distance from the origin the ratio of the speed ina parabolic orbit to that in a circular orbit is

$$
V _ { p } : V _ { c } = { \sqrt { 2 } } : 1 .
$$

Thus,in the motion of comets around the sun they cross the planets'orbits with velocities about 1.414 times those with which the respective planets move.

The speed that a body will acquire in falling from the distance s to the distance $\pmb { r }$ toward the cen.ter of force $k ^ { 2 } M$ is given by (see Art. 35)

$$
V ^ { 2 } = 2 k ^ { 2 } M \left( \frac { 1 } { r } - \frac { 1 } { s } \right) .
$$

If s is determined by the condition that this shall equal the speed in the orbit,it is found,after equating the right member of this

![](images/e9a99169f679a0f5eedae773d601d1cd87fa679e9284a82e0b21ab08fe13eb0c.jpg)  
Fig. 26.

expression to the right member of the second of (24),that $\ldots \ldots$ and

$$
V ^ { 2 } = 2 k ^ { 2 } M \left( \frac { 1 } { r } - \frac { 1 } { 2 a } \right) .
$$

Therefore, the speed of $^ { \pmb { a } }$ body moving in an ellipse is at every point equal to that which it would acquire in falling from the circumference of $a$ circle,with center at the origin and radius equal to the major axis of the conic, to the ellipse.

The speed at $P$ in the ellipse is equal to that which would be acquired in falling from $P ^ { \prime }$ to $P$ ·

Equation (26) gives an interesting conclusion about the possible motion of $m _ { 1 }$ on the basis of this equation alone,and without making any use of the detailed properties of motion in a conic section. Since the left member is necessarily positive (or zero) $\boldsymbol { r }$ can take only such values that the right member shall be positive (or zero). Consequently $r \leq 2 a$ in all the motion whatever it may be. This result is trivial in this simple case in which all the circumstances of motion are fully known,but the corresponding discussion in the Problem of Three Bodies (Chap. VI.） gives valuable information which has not been otherwise obtained.

Consider the second equation of (24) and suppose the body $m _ { 1 }$ is projected from a point which is distant $r$ from the body m2. It follows at once that the major axis of the conic depends upon the initial distance from the origin and the initial speed, but not upon the direction of projection.If $V ^ { 2 } < \frac { 2 k ^ { 2 } M } { r } = U ^ { 2 } ,$ ：U²,which is the velocity the body $m _ { 1 }$ would acquire in falling from infinity, $^ { a }$ is positive and the orbit is an ellipse；if $V ^ { 2 } = U ^ { 2 } ,$ $^ { a }$ is infinite and the orbit is a parabola; if $V ^ { 2 } > U ^ { 2 } , \epsilon$ $^ { a }$ is negative and the orbit is an hyperbola.

Let $t _ { 1 }$ and $t _ { 2 }$ be two epochs, and $A _ { 1 }$ and $A _ { 2 }$ the corresponding values of the area described by the radius vector. Then equation (18) gives

$$
2 ( A _ { 2 } - A _ { 1 } ) = ( t _ { 2 } - t _ { 1 } ) c _ { 1 } .
$$

Suppose $t _ { 2 } - t _ { 1 } = P$ ，the period of revolution；then $2 ( A _ { 2 } - A _ { 1 } )$ equals twice the area of the ellipse，which equals $2 \pi a b$ The expression for the period, found by substituting the value of $\pmb { c _ { 1 } }$ given in (22) and solving, is

$$
P = { \frac { 2 \pi a ^ { \frac { 3 } { 2 } } } { k { \sqrt { M } } } } \cdot
$$

From this equation it follows that the period is independent of every element except the major axis; or,because of (26),the period depends only upon the initial distance from the origin and the initial speed，and not upon the direction of projection. The major semi-axis will be called the mean distance, although it must be understood that it is not the average distance when the time is used as the independent variable. (See Probs.4 and 5,p. 154.) The three orbits drawn in Fig. 27 have the same length of major axis and are consequently described in the same time. The speed of projection from $A$ is the same in each case, the differences in the shapes and positions resulting from the different directions of projection.

![](images/e404667d23d6178d3bb4b52f1545279c8ee451c0e550540474d6738486920709.jpg)  
Fig. 27.

If the two systems $m _ { 1 } , m _ { 2 } ,$ and $m _ { 2 } , m _ { 3 }$ are considered,and the ratio of their periods is taken,it is found that

$$
{ \frac { P ^ { 2 } { } _ { 1 , ~ 2 } } { P ^ { 2 } { } _ { 3 , ~ 2 } } } = { \frac { a ^ { 3 } { } _ { 1 , ~ 2 } } { a ^ { 3 } { } _ { 3 , ~ 2 } } } \cdot { \frac { M _ { 3 , ~ 2 } } { M _ { 1 , ~ 2 } } } .
$$

If the two systems are composed of the sun and two planets respectively，then $M _ { 1 , \textbf { 2 } }$ and $M _ { 3 , \textbf { 2 } }$ are very nearly equal because the masses of the planets are exceedingly small compared to that of the sun. Therefore,this equation becomes very nearly

$$
{ \frac { P ^ { 2 } { } _ { 1 , ~ 2 } } { P ^ { 2 } { } _ { 3 , ~ 2 } } } = { \frac { a ^ { 3 } { } _ { 1 , ~ 2 } } { a ^ { 3 } { } _ { 2 , ~ 2 } } } ;
$$

or,the squares of the periodic times of the planets are proportional to the cubes of their mean distances. This is Kepler's third law.

It is to be observed that,in taking the ratios of the periods,it was assumed that $k ^ { \th }$ has the same value for the different planets; that is,that the sun's acceleration of the two planets would be the same at unit distance. On the other hand,it follows from the last equation,which Kepler established directly by observations, that $\pmb { k }$ has the same value for the various planets. This means that the force of gravitation between the sun and the several planets is proportional to their respective masses,as measured by their inertias. This result is not self-evident for the force of gravitation conceivably might depend upon the chemical constitution or physical condition of a body, just as chemical affinity, magnetism and all other known forces depend upon one or both of these things.In fact，it is remarkable that gravitation is proportional to inertia and independent of everything else.

90.Selection of Units and the Determination of the Constant $\pmb { k }$ 、 When the units of time,mass,and distance are chosen $k$ can be determined from (27). It is evident that they can all be taken arbitrarily,but it will be convenient to employ those units in which astronomical problems are most frequently treated. The mean solar day will be taken as the unit of time;the mass of the sun will be taken as the unit of mass;and the major semi-axis of the earth's orbit will be taken as the unit of distance. When these units are employed the $k$ determined by themis called the Gaussian constant,having been defined in this way by Gauss in the Theoria Motus, Art.1.

Let $\mathbf { \Delta } m _ { 2 }$ represent the mass of the sun and $\mathbf { \Delta } m _ { 1 }$ that of the earth and moon together;then it has been found from observation that in these units

$$
\left\{ { \begin{array} { l } { m _ { 1 } = { \frac { m _ { 2 } } { 3 5 4 7 1 0 } } = { \frac { 1 } { 3 5 4 7 1 0 } } , } \\ { P = 3 6 5 . 2 5 6 3 8 3 5 . } \end{array} } \right.
$$

On substituting these numbers in (27),it is found that

$$
\left\{ \begin{array} { c } { { k = \displaystyle \frac { 2 \pi } { P \sqrt { 1 + m _ { 1 } } } = 0 . 0 1 7 2 0 2 0 9 8 9 5 , } } \\ { { } } \\ { { \log k = 8 . 2 3 5 5 8 1 4 4 1 4 - 1 0 . } } \end{array} \right.
$$

Since $\pmb { m _ { 1 } }$ is very small $k = { \frac { 2 \pi } { P } }$ nearly,and is, therefore, nearly the mean daily motion of the earth in its orbit,or about $\frac { 1 } { 6 0 }$ The mean daily motion of a planet whose masis $m _ { i }$ is $\frac { 2 \pi } { P _ { i } }$ ， and is usually designated by $\textstyle \pmb { n } _ { \pmb { \mathscr { i } } }$ ，This is found from (27) to be

$$
n _ { i } = \frac { k \sqrt { 1 + m _ { i } } } { a _ { i } \mathbf { \hat { s } } } .
$$

The period of the earth's revolution around the sun and its mean distance were not known with perfect exactness at the time of Gauss,nor are they yet,and it is clear that the value of $k$ varies with the different determinations of these quantities. If astronomers held strictly to the definitions of the units given above it would be necessary to recompute those tables which depend upon $k$ every time an improvement in the values of the constants is made. These inconveniences are avoided by keeping the numerical value of $k$ that which Gauss determined，and choosing the unit of distance so that (27) will always be fulfilled.

If the mean distance between two bodies is taken as the unit of distance and the sum of their masses as the unit of mass,and if the unit of time is taken so that $k$ equals unity,then the units form what is called a canonical system. Since $M = 1$ and $k ^ { 2 } = 1$ in this system，and from (30) $n = 1$ ，the equations become somewhat simplified and are advantageous in purely theoretical investigations.

# XIV. PROBLEMS.

1.Find the differential equations for the problem of the relative motion of two bodies in polar coordinates.

Ans.

$$
{ \frac { d ^ { 2 } r } { d t ^ { 2 } } } = r \left( { \frac { d \theta } { d t } } \right) ^ { 2 } - { \frac { k ^ { 2 } M } { r ^ { 2 } } } , { \frac { d } { d t } } \left( r ^ { 2 } { \frac { d \theta } { d t } } \right) = 0 .
$$

2.Integrate the equations of problem 1 and interpret the constants of integration.

3.The earth moves in its orbit,which may be assumed to be circular,with a speed of 18.5 miles per second.Suppose the meteors approach the sun in parabolas;between what limits will be their relative speed when they strike into the earth's atmosphere?

Ans.7.66 to 44.66 miles per second.(The Nov.14 meteors meet the earth and have a relative speed near the upper limit;the Nov.27 meteors overtake the earth and have a relative speed near the lower limit.)

4.Find the average length of the radius vector of an ellipse in terms of aand e,taking the time as the independent variable.

Ans.

$$
\operatorname { A v e r a g e } r = { \frac { \int r d t } { \int d t } } = a \left( 1 + { \frac { e ^ { 2 } } { 2 } } \right) .
$$

5.Find the average length of the radius vector of an elipse, taking the angle as the independent variable.

Ans.

$$
\operatorname { A v e r a g e } r = { \frac { \int r d \theta } { \int d \theta } } = { \frac { 2 \pi a { \sqrt { 1 - e ^ { 2 } } } } { 2 \pi } } = b .
$$

6.Prove that the amount of heat received from the sun by the planets per unit area is on the average proportional to the reciprocals of the products of the major and minor axes of their orbits.For a fixed major axis how does the total amount of heat received in a revolution depend upon the eccentricity of the orbit?

7.If particles are projected from a given point with a given velocity but in different directions,find the locus of $( a )$ perihelion points; $( b )$ aphelion points; $( c )$ centers of ellipses; $( d )$ ends of minor axes.

8.If particles are projected from a given point in a given direction but with different spceds, find the loci of the same points as in problem 7,and express the coordinates of these points in terms of the initial values of the coordinates and the components of velocity.

9.Suppose a comet moving in a parabolic orbit with perihelion distance $\pmb q$ collides with and combines with an equal mass which is at rest before the collision.Find the eccentricity and the perihelion distance of the orbit of the combined mass.

10.Suppose the mass of Jupiter is 1/1047 when expressed in terms of the mass of the sun,and that its mean distance from the sun is 483,3o0,0o0 miles. (the mean distance from the earth to the sun is 92,9oo,00O miles).Find Jupiter's period of revolution around the sun,and the size of the orbit which the sun describes with respect to the center of gravity of itself and Jupiter.

91.Position in Parabolic Orbits. Having found the curves in which the bodies move,it remains to find their positions in their orbits at any given epoch. The case of the parabolic orbit being the simplest will be considered frst,and it will be supposed,to fix the ideas,that the motion is that of a comet with respect to the sun. Since the masses of the comets are negligible, $M = 1$ and equation (17) becomes

$$
r ^ { 2 } { \frac { d \theta } { d t } } = k { \sqrt { p } } = k { \sqrt { 2 q } } .
$$

When the polar angle in the orbit is counted from the vertex of the parabola it is denoted by $v$ ，and is called the true anomaly. Then

$$
\left\{ \begin{array} { l } { \displaystyle \frac { d \theta } { d t } = \frac { d v } { d t } , } \\ { \displaystyle r = \frac { p } { 1 + \cos v } = q \sec ^ { 2 } \frac { v } { 2 } . } \end{array} \right.
$$

Hence,equation (31） gives

$$
{ \frac { \sqrt { 2 } k } { q ^ { \frac { 3 } { 2 } } } } d t = \sec ^ { 4 } { \frac { v } { 2 } } d v = \left( \sec ^ { 2 } { \frac { v } { 2 } } + \sec ^ { 2 } { \frac { v } { 2 } } \tan ^ { 2 } { \frac { v } { 2 } } \right) d v .
$$

The integral of this expression is

$$
\tan { \frac { v } { 2 } } + \frac { 1 } { 3 } \tan ^ { 3 } \frac { v } { 2 } = \frac { k ( t - T ) } { \sqrt { 2 } q ^ { 3 } } ,
$$

where $\pmb { T }$ is the time of perihelion passage. This is a cubic equation in $\tan { \frac { \upsilon } { 2 } }$ . On taking the right member to the left side it is seen that for $t - T > 0 _ { : }$ ,the function is negative when $v = 0$ ,and that it increases continually with $v$ until it equals infinity for $v = 1 8 0 ^ { \circ }$ Therefore,there is but one real solution of (32) for tan $\frac { v } { 2 }$ ，and it is positive.For $t - T < 0$ it is seen in a similar manner that there is one real negative solution.

Equation (32) may be written

$$
2 5 \tan ^ { 3 } { \frac { v } { 2 } } + 7 5 \tan { \frac { v } { 2 } } = { \frac { 7 5 k } { \sqrt { 2 } } } { \frac { ( t - T ) } { q ^ { \frac { 3 } { 4 } } } } = K { \frac { ( t - T ) } { q ^ { \frac { 3 } { 4 } } } } .
$$

Tables have been constructed giving the value of the right member of this equation for different values of $v$ .From these tables $v$ can be found by interpolation when $t - T$ is given；or，conversely, $t - T$ can be found when $v$ is given. These tables are known as Barker's,and are VI.in Watson's Theoretical Astronomy,and IV. in Oppolzer's Bahnbestimmung.\*

In order to find the direct solution of the cubic equation let

$$
\tan { \frac { v } { 2 } } = 2 \cot 2 w = \cot w - \tan w ;
$$

whence

$$
\tan ^ { 3 } { \frac { v } { 2 } } = - 3 \tan { \frac { v } { 2 } } + \cot ^ { 3 } w - \tan ^ { 3 } w .
$$

This substitution reduces (32) to

$$
\cot ^ { 3 } w - \tan ^ { 3 } w = { \frac { 3 k ( t - T ) } { { \sqrt { 2 } } q ^ { 3 } } } .
$$

Let

$$
\cot w = { \sqrt [ { \sqrt [ { 3 } ] { \cot { \frac { 3 } { 2 } } } } } ;
$$

whence

$$
\cot s = { \frac { 3 k ( t - T ) } { 2 ^ { \sharp } q ^ { \sharp } } } .
$$

Therefore the formulas for thecomputation of $\tan { \frac { v } { 2 } }$ are, in the

\*In Oppolzer's Bahnbestimmung the factor 75 is not introduced.

order of their application,

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \cot s = \frac { 3 k ( t - T ) } { ( 2 q ) ^ { \frac { s } { 2 } } } , } \\ { \cot w = \sqrt [ 3 ] { \cot \frac { s } { 2 } } , } \\ { \tan \frac { v } { 2 } = 2 \cot 2 w . } \end{array} \right. } \end{array}
$$

After $\pmb { v }$ has been found $\pmb { r }$ is determined by the polar equation of the parabola,r = 1+ cos v $r = { \frac { p } { 1 + \cos \upsilon } } = q \sec ^ { 2 } { \frac { \upsilon } { 2 } } .$

92.Equation involving Two Radii and their Chord. Euler's Equation. Consider the positions of the comet at the instants $t _ { 1 }$ and $t _ { 2 }$ .Let the corresponding radii be $\pmb { r _ { 1 } }$ and $\pmb { r _ { 2 } } , $ ，and the chord joining their extremities s. Let the corresponding true anomalies be $v _ { 1 }$ and ${ \boldsymbol { v } } _ { 2 }$ ：Then it follows that

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { k ( t _ { 1 } - T ) } { \sqrt { 2 } q ^ { \frac { 3 } { 2 } } } = \tan \frac { v _ { 1 } } { 2 } + \frac { 1 } { 3 } \tan ^ { 3 } \frac { v _ { 1 } } { 2 } , } \\ { \displaystyle \frac { k ( t _ { 2 } - T ) } { \sqrt { 2 } q ^ { \frac { 3 } { 2 } } } = \tan \frac { v _ { 2 } } { 2 } + \frac { 1 } { 3 } \tan ^ { 3 } \frac { v _ { 2 } } { 2 } . } \end{array} \right.
$$

The difference of these equations is

$$
\begin{array} { r l r } {  { \frac { \iota _ { 2 } ^ { * } - { \iota _ { 1 } } } { \sqrt { 2 } q ^ { \frac { 3 } { 2 } } } = \tan { \frac { v _ { 2 } } { 2 } } - \tan { \frac { v _ { 1 } } { 2 } } + \frac { 1 } { 3 } ( \tan ^ { 3 } \frac { v _ { 2 } } { 2 } - \tan ^ { 3 } \frac { v _ { 1 } } { 2 } ) ; } } \\ & { } & \\ & { \frac { 3 k ( t _ { 2 } - t _ { 1 } ) } { \sqrt { 2 } q ^ { \frac { 3 } { 2 } } } = ( \tan \frac { v _ { 2 } } { 2 } - \tan \frac { v _ { 1 } } { 2 } ) [ 3 ( 1 + \tan \frac { v _ { 1 } } { 2 } \tan \frac { v _ { 2 } } { 2 } )  } \\ & { } & \\ & { } & {  + ( \tan \frac { v _ { 2 } } { 2 } - \tan \frac { v _ { 1 } } { 2 } ) ^ { 2 } ] . } \end{array}
$$

The equation for the chord is

$$
\begin{array} { l } { { \displaystyle \vartheta ^ { 2 } = r _ { 1 } { } ^ { 2 } + r _ { 2 } { } ^ { 2 } - 2 r _ { 1 } r _ { 2 } \cos \left( v _ { 2 } - v _ { 1 } \right) } } \\ { { \displaystyle \qquad = ( r _ { 1 } + r _ { 2 } ) ^ { 2 } - 4 r _ { 1 } r _ { 2 } \cos ^ { 2 } \left( \displaystyle \frac { v _ { 2 } - v _ { 1 } } { 2 } \right) . } } \end{array}
$$

From this equation it is found that

$$
2 \sqrt { r _ { 1 } r _ { 2 } } \cos \left( \frac { v _ { 2 } - v _ { 1 } } { 2 } \right) = \pm \ \sqrt { ( r _ { 1 } + r _ { 2 } + s ) ( r _ { 1 } + r _ { 2 } - s ) } .
$$

The $+$ sign is to be taken before the radical if $v _ { 2 } - v _ { 1 } < \pi _ { \mathrm { i } }$ and the-sign if $v _ { 2 } \mathrm { ~ - ~ } v _ { 1 } > \pi$

It follows from the polar equation of the parabola that

$$
r _ { 1 } = q \sec ^ { 2 } { \frac { v _ { 1 } } { 2 } } , \qquad r _ { 2 } = q \sec ^ { 2 } { \frac { v _ { 2 } } { 2 } } .
$$

These expressions for $\pmb { r _ { 1 } }$ and $\pmb { r _ { 2 } } .$ ,substituted in (35), give

$$
1 + \tan { \frac { v _ { 1 } } { 2 } } \tan { \frac { v _ { 2 } } { 2 } } = \pm \frac { \sqrt { ( r _ { 1 } + r _ { 2 } + s ) ( r _ { 1 } + r _ { 2 } - s ) } } { 2 q } .
$$

It also follows from the expressions for $\pmb { r _ { 1 } }$ and $\pmb { r _ { 2 } }$ that

$$
r _ { 1 } + r _ { 2 } = q \left( 2 + \tan ^ { 2 } \frac { v _ { 1 } } { 2 } + \tan ^ { 2 } \frac { v _ { 2 } } { 2 } \right) .
$$

The last two equations give

$$
\begin{array} { l } { \displaystyle \frac { ( r _ { 1 } + r _ { 2 } + s ) + ( r _ { 1 } + r _ { 2 } - s ) \mp 2 \sqrt { ( r _ { 1 } + r _ { 2 } + s ) ( r _ { 1 } + r _ { 2 } - s ) } } { 2 q } } \\ { \displaystyle \qquad = \left( \tan \frac { v _ { 2 } } { 2 } - \tan \frac { v _ { 1 } } { 2 } \right) ^ { 2 } ; } \end{array}
$$

whence

$$
{ \frac { { \sqrt { r _ { 1 } + r _ { 2 } + s } } \ = \ { \sqrt { \frac { r _ { 1 } + r _ { 2 } - s } { \sqrt { 2 q } } } } } { \sqrt { 2 q } } } { \frac { r _ { 1 } + { \sqrt { 2 \ r _ { 2 } - s } } } { \sqrt { 2 } } } = \tan { \frac { v _ { 2 } } { 2 } } - \tan { \frac { v _ { 1 } } { 2 } } .
$$

Equation (34) becomes, as a consequence of (36) and (37),

$$
6 k ( t _ { 2 } - t _ { 1 } ) = ( r _ { 1 } + r _ { 2 } + s ) ^ { \tt S } = ( r _ { 1 } + r _ { 2 } - s ) ^ { \tt S } .
$$

This equation is remarkable in that it does not involve $\pmb q$ It was discovered by Euler and bears his name. It is of the first importance in some methods of determining the elements of a parabolic orbit from geocentric observations.

There is a corresponding equation,due to Lambert,for elliptic orbits. The right member is developed as a power series in ${ \bf 1 } / a _ { \mathrm { . } }$ ， the first term constituting the right member of Euler's equation.

93.Position in Elliptic Orbits. The integral of areas and the vis viva integral are respectively

$$
\left\{ \begin{array} { r } { r ^ { 2 } \displaystyle \frac { d v } { d t } = k \sqrt { ( 1 + m ) a ( 1 - e ^ { 2 } ) } , } \\ { \left( \displaystyle \frac { d r } { d t } \right) ^ { 2 } + r ^ { 2 } \left( \displaystyle \frac { d v } { d t } \right) ^ { 2 } = k ^ { 2 } ( 1 + m ) \left( \displaystyle \frac { 2 } { r } - \displaystyle \frac { 1 } { a } \right) . } \end{array} \right.
$$

The result of eliminating $\frac { d v } { d t }$ from thesecond of theseequations

by means of the first is

$$
\left( { \frac { d r } { d t } } \right) ^ { 2 } + { \frac { k ^ { 2 } ( 1 + m ) a ( 1 - e ^ { 2 } ) } { r ^ { 2 } } } = k ^ { 2 } ( 1 + m ) \left( { \frac { 2 } { r } } - { \frac { 1 } { a } } \right) .
$$

Let $^ { n }$ represent the mean angular motion of the body in its orbit; then

$$
n = \frac { 2 \pi } { P } = \frac { k \sqrt { 1 + m } } { a ^ { 3 } } .
$$

On introducing $\pmb { n }$ in (39)and solving,it is found that

$$
n d t = \frac { r } { a } \frac { d r } { \sqrt { a ^ { 2 } e ^ { 2 } - ( a - r ) ^ { 2 } } } .
$$

In order to normalize the integral which appears in the right member of (40),let the auxiliary $E$ be introduced by the equation

$$
\left. \begin{array} { c } { { a - r = a e \cos { \cal E } , \mathrm { w h e n c e } } } \\ { { r = a ( 1 - e \cos { \cal E } ) . } } \end{array} \right.
$$

This angle $\pmb { { \cal E } }$ is called the eccentric anomaly. Then (40) becomes

$$
\begin{array} { r } { n d t = ( 1 - e \cos E ) d E , } \end{array}
$$

the integral of which is

$$
n \left( t - T \right) = E - e \sin { E } .
$$

The quantity $n ( t - T )$ is the angle which would have been described by the radius vector if it had moved uniformly with the average rate. It is usually denoted by $M$ and is called the mean anomaly. Therefore

$$
\boldsymbol { n } ( t - T ) = \boldsymbol { M } = \boldsymbol { E } - \boldsymbol { e } \sin \boldsymbol { E } .
$$

The $M$ can at once be found when $( t - T )$ is given,after which equation (42) must be solved for $E$ Then $\pmb { r }$ and $v$ can be found from (41） and the polar equation of the elipse. Equation (42), known as Kepler's equation, is transcendental in $\pmb { \cal E }$ ,and the solution for this quantity cannot be expressed in a finite number of terms. Since it is very desirable to have the solution as short as possible astronomers have devoted much attention to this equation，and several hundred methods of solving it have been discovered.

94.Geometrical Derivation of Kepler's Equation. Construct the ellipse in which the body moves,and also its auxiliary circle AQB. The angle AFP equals the true anomaly, v； the angle $\pmb { A } C Q$ will be defined as the eccentric anomaly, $E$ ,and it will be shown that the relation between $M$ and $\pmb { \cal E }$ is given by Kepler's equation.

![](images/82ace5671414723330c1f864b4a107a5f9de1fcc880eb20b753d30ca32507f92.jpg)  
Fig. 28.

From the law of areas and the properties of the auxiliary circle, it follows that

$$
{ \frac { M } { 2 \pi } } = { \frac { \mathrm { a r e a ~ } A F P } { \mathrm { a r e a ~ e l l i p s e } } } = { \frac { \mathrm { a r e a ~ } A F Q } { \mathrm { a r e a ~ c i r c l e } } } .
$$

$$
A F Q = \operatorname { a r e a } A C Q - \operatorname { a r e a } F C Q = { \frac { a ^ { 2 } E } { 2 } } - { \frac { a } { 2 } } a e \sin { E } .
$$

Therefore

$$
{ \frac { M } { 2 \pi } } = { \frac { a ^ { 2 } } { 2 } } { \frac { ( E - e \sin E ) } { \pi a ^ { 2 } } } ,
$$

$$
\left\{ F P = r = \frac { a ( 1 - e ^ { 2 } ) } { 1 + e \cos v } = \sqrt { P D ^ { 2 } + \overrightarrow { F D } ^ { 2 } } = a ( 1 - e \cos E ) , \right.
$$

which is the definition of the eccentric anomaly given in (41).

95.Solution of Kepler's Equation. It will be shown first that Kepler's equation always has one,and only one,real solution for every value of $M$ and for every $e$ such that $0 \not \Xi e < 1$ .Write the equation in the form

$$
\phi ( E ) \equiv E - e \sin E - M = 0 .
$$

Suppose $M$ has some given value between $\varkappa \pi$ and $( n + 1 ) \pi ,$ where $_ { \pmb { n } }$ is any integer; then there is but one real value of $\pmb { \cal E }$ satisfying this equation,and it lies between $\varkappa \pi$ and $( n + 1 ) \pi$ For, the function $\phi ( E )$ when ${ \mathcal { E } } = n \pi$ is

$$
\phi ( n \pi ) = n \pi - M < 0 .
$$

And ${ \phi } ( E )$ when $E = ( n + 1 ) \pi$ is

$$
\phi [ ( n + 1 ) \pi ] = ( n + 1 ) \pi - M > 0 .
$$

Consequently there is an odd number of real solutions for $\pmb { \cal E }$ which lie between $n \pi$ and $( n + 1 ) \pi$ .But the derivative

$$
\phi ^ { \prime } ( E ) \equiv 1 - e \cos E
$$

is always positive；therefore $\phi ( E )$ increases continually with $\pmb { \cal E }$ and takes the value zero but once.

A convenient method of practically solving the equation is by means of an expansion due to Lagrange. Suppose $\pmb { \mathscr { z } }$ is defined as a function of $\boldsymbol { w }$ by the equation

$$
{ z } = w + \alpha \phi ( z ) ,
$$

where $_ { \alpha }$ is a parameter. Lagrange has shown that any function of $\pmb { \mathscr { z } }$ can be expressed in a power series in $_ { \alpha }$ ，which converges for suffciently small values of $\pmb { \alpha }$ ，of the form\*

$$
\left\{ \begin{array} { l l } { { \displaystyle F ( z ) = F ( w ) + \frac { \alpha } { 1 } \cdot \phi ( w ) F ^ { \prime } ( w ) + \frac { \alpha ^ { 2 } } { 1 \cdot 2 } \frac { \partial } { \partial w } [ \{ \phi ( w ) \} ^ { 2 } F ^ { \prime } ( w ) ] } } \\ { { \displaystyle \qquad + \ \cdots + \frac { \alpha ^ { n + 1 } } { ( n + 1 ) ! } \frac { \partial ^ { n } } { \partial w ^ { n } } [ \{ \phi ( w ) \} ^ { n + 1 } F ^ { \prime } ( w ) ] + \cdots . } } \end{array} \right.
$$

This expansion can be applied to the solution of Kepler's equation by writing it

$$
E = M + e \sin E ,
$$

which is of the same form as (43). The expansion of $\pmb { \cal E }$ as a series in $e$ can be taken from (44) by putting $\begin{array} { r } { \pmb { F } ( z ) = \pmb { E } } \end{array}$ ， $\phi ( z ) = \sin { \cal E }$ ， $w = M$ and $\alpha = e$ ，The result is

$$
{ \cal E } = M + \frac { e } { 1 } \sin M + \frac { e ^ { 2 } } { 1 \cdot 2 } \sin 2 M + \cdots .
$$

All the terms on the right except the first are expressed in radians and must be reduced to degrees by multiplying each of them by the number of degrees in a radian. The higher terms are considerably more complicated than those written,and the work of computing them increases very rapidly. In the planetary and satellite orbits the eccentricity is very small,and the series (45) converges with great rapidity,the first three terms giving quite an accurate value of $E$

96.Differential Corrections. A method will now be explained in one of its simplest applications,which is of great importance in many astronomical problems. Suppose an approximate value of $\boldsymbol { E }$ is determined by the frst three terms of (45).Call it $E _ { 0 }$ ； it is required to find the correct value of $\pmb { { \cal E } }$

Kepler's equation gives

$$
M _ { 0 } = E _ { 0 } - e \sin E _ { 0 } .
$$

For a particular value of $M$ ,viz., $M _ { 0 } ,$ the corresponding value of $\pmb { { \cal E } }$ ,viz., $\mathcal { E } _ { 0 } ,$ is known.It is required to find the value of $\pmb { { \cal E } }$ corresponding to $M$ ，which differs only a little from $M _ { 0 }$ The angle $M$ is a function of $\pmb { { \cal E } }$ and may be written

$$
M = M _ { 0 } + \Delta M _ { 0 } = f ( E _ { 0 } + \Delta E _ { 0 } ) .
$$

On expanding the right member by Taylor's formula, this equation becomes

$$
M = M _ { 0 } + \Delta M _ { 0 } = f ( E _ { 0 } ) + f ^ { \prime } ( E _ { 0 } ) \Delta E _ { 0 } + \cdots .
$$

By the definitions of the quantities, $M _ { 0 } = f ( { \cal E } _ { 0 } )$ ； therefore this equation becomes

$$
M - M _ { 0 } = f ^ { \prime } ( E _ { 0 } ) \Delta E _ { 0 } + \cdots = ( 1 - e \cos E _ { 0 } ) \Delta E _ { 0 } + \cdots .
$$

Since $\Delta \mathbf { { E } } _ { 0 }$ is very small the squares and higher powers may be neglected,\* and then equation (46) gives for the correction to be applied to $\scriptstyle { { \mathbf { } } _ { 0 } }$

$$
\Delta E _ { 0 } = \frac { M - M _ { 0 } } { 1 - e \cos E _ { 0 } } .
$$

With the more nearly correct value of $E , E _ { 1 } = E _ { 0 } + \Delta E _ { 0 }$ and $M _ { 1 }$ can be computed from Kepler's equation,and a second correction will be

$$
\Delta E _ { 1 } = \frac { M - M _ { 1 } } { 1 - e \cos E _ { 1 } } .
$$

This process can be repeated until the value of $\pmb { \cal E }$ is found as near as may be desired $^ \dagger$ In the planetary orbits two applications of

\*If the higher terms in $\Delta \mathbf { { E } } _ { 0 }$ were not neglected $\Delta \mathbf { { \mathcal { E } } } _ { 0 }$ could be expressed as & power series in $M - M _ { 0 } ,$ of which the first term would be the right member of (47).

$^ \dagger$ For the proof of the convergence of a similar,but somewhat more laborious, process see Appell's Mécanique vol.1.,p.391.

the formulas will nearly always give results which are sufficiently accurate,and usually one correction will suffice.

97.Graphical Solution of Kepler's Equation. When the eccentricity is more than O.2 the method of solving Kepler's equation given above is laborious because the first approximation will be very inexact. These high eccentricities occur in binary star and comet orbits,and are sometimes even so great as 0.9. In the case of binary star orbits it is usually sufficient to have a solution to within a tenth of one degree.In this work a rapid graphical method is of great practical value.

![](images/fba8d72ef60a53b63d02638d0979d1745061b5560bc1a077b03d6e1e577fade4.jpg)  
Fig. 29.

Consider Kepler's equation

$$
E - e \sin E - M = 0 ,
$$

where $M$ is given and $\pmb { { \cal E } }$ is required. Take a rectangular system of axes and construct the sine curve and the straight line whose equations are

$$
\left\{ \begin{array} { l l } { \displaystyle { y = \sin E , } } \\ { \displaystyle { y = \frac { 1 } { e } ( E - M ) . } } \end{array} \right.
$$

The abscissa of their point of intersection is the value of $\pmb { \cal E }$ satisfying the equation;\* for, eliminating $_ y$ ,Kepler's equation results. The first curve is the familiar sine curve which can be constructed once for all; the second is a straight line making with the $\pmb { { \cal E } }$ -axis an angle whose tangent is $1 / e$ .Instead of drawing the straight line a straight-edge can be laid down making the proper slope with the axis. To facilitate the determination of its position construct a line with the degrees marked on it at an altitude of $^ { 1 0 0 ; ^ { * } }$ then place the bottom of the straight-edge at $M$ and the top at $M + 1 0 0 e _ { \scriptscriptstyle \mathrm { \perp } }$ ,and it follows that it will have the proper slope. If $M$ is so near $1 8 0 ^ { \circ }$ that the straight-edge runs off from the diagram, the top can be placed at $M + 5 0 e$ on the 50-line.As $M$ becomes very near $1 8 0 ^ { \circ }$ the mean and eccentric anomalies become very nearly equal, exactly coinciding at $M = 1 8 0 ^ { \circ }$ ·

98.Recapitulation of Formulas. The equations for the computation of the polar coordinates，when the time is given，will now be given in the order in which they are used.

whence

$$
\left\{ \begin{array} { l l } { \displaystyle n = \frac { k \sqrt { 1 + m } } { a ^ { 3 } } , } \\ { \displaystyle M = n ( t - T ) , } \\ { \displaystyle E _ { 0 } = M + \epsilon \sin { M } + \frac { e ^ { 2 } } { 2 } \sin { 2 M } , } \\ { \displaystyle M _ { 0 } = E _ { 0 } - \epsilon \sin { E _ { 0 } } , } \\ { \displaystyle \Delta E _ { 0 } = \frac { M - M _ { 0 } } { 1 - \epsilon \cos { E _ { 0 } } } , } \\ { \displaystyle E _ { 1 } = E _ { 0 } + \Delta E _ { 0 } , } \\ { \displaystyle r = a ( 1 - \epsilon \cos { E } ) = \frac { a ( 1 - e ) } { 1 + \epsilon \cos { \nu } } ; } \end{array} \right.
$$

$$
\left\{ \begin{array} { c } { \cos v = \displaystyle \frac { \cos E - e } { 1 - e \cos E } \displaystyle , } \\ { \sin v = \displaystyle \frac { \sqrt { 1 - e ^ { 2 } } \sin E } { 1 - e \cos E } \displaystyle , } \\ { 1 + \cos v = \displaystyle \frac { ( 1 - e ) ( 1 + \cos E ) } { 1 - e \cos E } \displaystyle , } \\ { 1 - \cos v = \displaystyle \frac { ( 1 + e ) ( 1 - \cos E ) } { 1 - e \cos E } \displaystyle , } \end{array} \right.
$$

\* This device is due to C.A. Young.

The square root of the quotient of the last two equations gives a very convenient formula for the computation of $v$ ,viz.,

$$
{ \sqrt { \frac { 1 - \cos v } { 1 + \cos v } } } = \tan { \frac { v } { 2 } } = { \sqrt { \frac { 1 + e } { 1 - e } } } \tan { \frac { E } { 2 } } .
$$

The last equation of (48) and equation (50) give the polar coordinates when $E$ is known.

99.The Development of $\boldsymbol { E }$ in Series. The equations which have been given are sufficient to enable one to compute the polar, and consequently the rectangular，coordinates at any epoch; yet,in some kinds of investigations,as in the theory of perturbations,it is necessary to have the developments of not only $\boldsymbol { \mathbf { \mathit { E } } }$ ,but also the polar coordinates,carried so far that the functions are represented by the series with the desired degree of accuracy.

The application of Lagrange's method of Art. 95 to Kepler's equation gives $\mathbfit { \Delta } E$ asa power series in e whose coefficients are functions of $M$ .This method has been used to get the first terms of the series and it can be continued as far as may be desired. It is very elegant in practice and is subject only to the difficulty of proving its legitimacy. But a direct treatment of Kepler's equation based on more elementary considerations is not difficult. The solution of

$$
M = E - e \sin E
$$

for $\boldsymbol { E }$ is $j \pi$ when $M = j \pi$ ,where $j = 0 , 1 , 2 , \cdots ,$ whatever value e may have. Moreover,it has been shown that when $e$ is less than unity the solution is unique for all values of $M$ .When $e = 0$ the solution is $E = M$ for all values of $M$ If $_ { u }$ is defined by the equation

$$
E - M = u
$$

Kepler's equation becomes

$$
\begin{array} { r } { u = e \sin { ( M + u ) } , } \end{array}
$$

which defines $\boldsymbol { u }$ in terms of $M$ and $e$ .Forevery value of $M$ different from $j \pi _ { ; }$ ,for which the solution is already known, the right member of

$$
e = \frac { u } { \sin \left( M + u \right) }
$$

can be expanded as a converging power series in $\boldsymbol { \mathscr { u } }$ .When this series is inverted $_ { \mathscr { u } }$ will be given as a power series in $e$ whose

coefficients are functions of $M$ Since $\textbf { \em u }$ vanishes with $e _ { : }$ it will have the form

$$
u = u _ { 1 } e + u _ { 2 } e ^ { 2 } + u _ { 3 } e ^ { 3 } + \cdots .
$$

Instead of forming the series in $\textbf { \em u }$ and then inverting, it is simpler to substitute (52) in (51) and to determine ui, uz, · by the condition that the result shall be an identity in e. The result of the substitution is

$$
\left\{ \begin{array} { l l } { u _ { 1 } e + u _ { 2 } e ^ { 2 } + u _ { 3 } e ^ { 3 } + \dotsb = e \sin M \cos u + e \cos M \sin u } \\ { \qquad = e \sin M \left[ 1 - \frac { \left( u _ { 1 } e + u _ { 2 } e ^ { 2 } \dotsb \right) ^ { 2 } } { 2 \mathrm { ~ l ~ } } + \frac { \left( u _ { 1 } e + \dotsb \right) ^ { 4 } } { 4 \mathrm { ~ l ~ } } - \dotsb \right] } \\ { \qquad + e \cos M \left[ \left( u _ { 1 } e + u _ { 2 } e ^ { 2 } + \dotsb \right) - \frac { \left( u _ { 1 } e \cdot \dotsb \right) ^ { 3 } } { 3 \mathrm { ~ l ~ } } + \dotsb \right] . } \end{array} \right.
$$

On equating coefficients of corresponding powers of $\pmb { e _ { \mathrm { i } } }$ it is found that

$$
\left\{ \begin{array} { l } { \displaystyle u _ { 1 } = \sin M , } \\ { \displaystyle u _ { 2 } = u _ { 1 } \cos M = \frac 1 2 \sin 2 M , } \\ { \displaystyle u _ { 3 } = - \frac 1 2 u _ { 1 } ^ { 2 } \sin M + u _ { 2 } \cos M = \frac 3 8 \sin 3 M - \frac 1 8 \sin M , } \\ { . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . } \end{array} \right.
$$

Some general properties of the solutions easily follow from these equations.It follows from (51） that if for any $M = M _ { 0 }$ the solution for $^ { \ast }$ ，which is known to exist uniquely, is $u = u _ { 0 } ,$ then the solution for $M = M _ { 0 } + 2 j \pi$ ( $\dot { \boldsymbol { j } }$ any integer) is also $u = u _ { 0 } .$ Therefore $^ { \ast }$ is a periodic function of $M$ with the period $\mathbf { 2 \pi }$ Since this is true for all values of $e$ ,each $u _ { j }$ is separately periodic with the period $2 \pi$ If any $M _ { 0 }$ and $\scriptstyle { \boldsymbol { u } } _ { 0 }$ satisfy (51),then $- \ M _ { 0 }$ and - $\scriptstyle { \boldsymbol { u } } _ { 0 }$ also satisfy (51)； therefore $\textbf { \em u }$ is an odd function of $\pmb { M }$ and the $\boldsymbol { u } _ { j }$ are sines of multiples of $M$ If the sign of $e$ is changed and $\pmb { \pi }$ is added to $M$ in (51),the equation is unchanged；therefore the $u _ { j }$ with odd subscripts involve only sines of odd multiples of $M$ ， and those with even subscripts only sines of even multiples of $M$

It will be shown that the highest multiple of $M$ appearing in $\ b { u } _ { j }$ is $j M$ .The general term of (53) is

$u _ { j } = \sin M P _ { i } ( u _ { 1 } , u _ { 2 } , \cdots , u _ { j - 1 } ) + \cos M Q _ { j } ( u _ { 1 } , u _ { 2 } , \cdots , u _ { j - 1 } ) ,$ where $P _ { j }$ and $Q _ { j }$ are polynomials in $u _ { 1 } , \ u _ { 2 } , \ \cdots , \ u _ { j - 1 }$ These quantities must enter in such powers that they are multiplied by $e ^ { j - 1 }$ .Suppose the general terms of the polynomials $P _ { j }$ and $Q _ { j }$ are,except for numerical coefficients which do not enter into the present argument, respectively

$$
p _ { j } = u _ { 1 } ^ { j _ { 1 } } \cdot u _ { 2 } ^ { j _ { 2 } } \cdot \cdot \cdot \ u _ { j - 1 } ^ { j _ { j - 1 } } , \qquad q _ { j } = u _ { 1 } ^ { k _ { 1 } } \cdot u _ { 2 } ^ { k _ { 2 } } \cdot \cdot \cdot \ u _ { j - 1 } ^ { k _ { j - 1 } } .
$$

The exponents of $u _ { 1 } , \ \cdots , \ u _ { j - 1 }$ are subject to the condition that $\pmb { p } _ { j }$ and ${ { q } _ { j } }$ shall be multiplied by $e ^ { i - 1 }$ .The term $u _ { m }$ carries with it the factor $e ^ { m }$ ,and therefore $\boldsymbol { u } _ { m } ^ { n }$ carries the factor mn. Hence the exponents of $u _ { 1 } , \cdots , u _ { i - 1 }$ in $p _ { i }$ and $q _ { j }$ must satisfy

$$
\begin{array} { r } { \left\{ \begin{array} { l } { j _ { 1 } + 2 j _ { 2 } + \cdots + ( j - 1 ) j _ { i - 1 } = j - 1 , } \\ { k _ { 1 } + 2 k _ { 2 } + \cdots + ( j - 1 ) k _ { i - 1 } = j - 1 . } \end{array} \right. } \end{array}
$$

Now suppose that the highest multiples of $M$ in $u _ { m }$ is $\pmb { m M }$ for $m = 1 , \cdots , j - 1$ .It follows from the properties of powers of the sines that the highest multiple in $\boldsymbol { u } _ { m } ^ { n }$ is mnM. Since the highest multiple of the product of two or more sines is the sum of their highest multiples,the highest multiples in $p _ { j }$ and $q _ { i }$ are respectively

$$
j _ { 1 } + 2 j _ { 2 } + \cdots + ( j - 1 ) j _ { i - 1 } , ~ k _ { 1 } + 2 k _ { 2 } + \cdots + ( j - 1 ) k _ { i - 1 } ,
$$

which are $j - 1$ by (54)． But it follows from (53) that $p _ { j }$ is multiplied by sin $M$ and $q _ { i }$ by cos $M$ ； therefore the highest multiple appearing in $\mathbf { \delta } \mathbf { \mathcal { u } } _ { j }$ is $j M$ .That is, $u _ { j }$ has the form

$$
\left\{ \begin{array} { c } { { u _ { 2 k } = + a _ { 2 } ^ { ( 2 k ) } \sin 2 M + \cdots + a _ { 2 k } ^ { ( 2 k ) } \sin 2 k M , } } \\ { { { } } } \\ { { u _ { 2 k + 1 } = a _ { 1 } ^ { ( 2 k + 1 ) } \sin M + \cdots + a _ { 2 k + 1 } ^ { ( 2 k + 1 ) } \sin { ( 2 k + 1 ) } M , } } \end{array} \right.
$$

according as $j$ is even or odd.

It is easy to develop a check on the acceuracy of the computations. Since $E = M + u$ ,it follows that

$$
\frac { \partial E } { \partial M } = 1 + \frac { \partial u } { \partial M } = 1 + \frac { \partial u _ { 1 } } { \partial M } e + \frac { \partial u _ { 2 } } { \partial M } e ^ { 2 } + \cdots + \frac { \partial u _ { i } } { \partial M } e ^ { i } + \cdots .
$$

But it follows from Kepler's equation that

$$
\frac { \partial E } { \partial M } = \frac { 1 } { 1 - e \cos E } .
$$

Suppose $M = 0$ ; therefore $\mathcal { E } = 0$ and for this value of $\pmb { M }$

$$
{ \frac { \partial E } { \partial { \overline { { M } } } } } = { \frac { 1 } { 1 - e } } = 1 + e + e ^ { 2 } + \cdots + e ^ { i } + \cdots .
$$

Therefore,since the coefficient of $e ^ { i }$ in this series is unity,for $M = 0$

$$
\left\{ \begin{array} { c } { \frac { \partial u _ { 2 k } } { \partial M } = 2 a _ { 2 } ^ { ( 2 k ) } + 4 a _ { 4 } ^ { ( 2 k ) } + \cdots + 2 k a _ { 2 k } ^ { ( 2 k ) } = 1 , } \\ { { } } \\ { \frac { \partial u _ { 2 k + 1 } } { \partial M } = a _ { 1 } ^ { ( 2 k + 1 ) } + \cdots + ( 2 k + 1 ) a _ { 2 k + 1 } ^ { ( 2 k + 1 ) } = 1 . } \end{array} \right.
$$

These equations constitute a valuable check on all the computations.

It is found from (56) that

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial ^ { 2 } E } { \partial M ^ { 2 } } = \frac { - \ e \sin E } { ( 1 - e \cos E ) ^ { 2 } } \displaystyle \frac { \partial E } { \partial M } = \frac { - \ e \sin E } { ( 1 - e \cos E ) ^ { 3 } } , } \\ { \displaystyle \frac { \partial ^ { 3 } E } { \partial M ^ { 3 } } = \frac { - \ e \cos E } { ( 1 - e \cos E ) ^ { 4 } } + \frac { 3 e ^ { 2 } \sin ^ { 2 } E } { ( 1 - e \cos E ) ^ { 5 } } . } \end{array} \right.
$$

For $M = 0$ ,the first of these equations is identically zero,but the second one becomes

$$
\begin{array} { r l } & { \frac { \partial ^ { 3 } E } { \partial M ^ { 3 } } = \frac { - \ e } { ( 1 - e ) ^ { 4 } } = \ - \ \displaystyle \left[ e + 4 e ^ { 2 } + \frac { 4 \cdot 5 } { 1 \cdot 2 } e ^ { 3 } + \cdots \qquad \right. } \\ & { \qquad \left. + \frac { 4 \cdot 5 \ \cdots \ ( n + 2 ) } { 1 \cdot 2 \ \cdots \ ( n - 1 ) } e ^ { n } + \cdots \right] , } \end{array}
$$

Then the conditions similar to (57) are

$$
\left\{ \begin{array} { l l } { \displaystyle { - \frac { \partial ^ { 3 } u _ { 2 k } } { \partial M ^ { 3 } } = 2 ^ { 3 } a _ { 2 } ^ { ( 2 k ) } + 4 ^ { 3 } a _ { 4 } ^ { ( 2 k ) } + \dots + ( 2 k ) ^ { 3 } a _ { 2 k } ^ { ( 2 k ) } } } \\ { \displaystyle { \qquad = \frac { 4 \cdot 5 \cdot \cdot ( 2 k + 2 ) } { 1 \cdot 2 \cdot \cdot \cdot ( 2 k - 1 ) } , } } \\ { \displaystyle { - \frac { \partial ^ { 3 } u _ { 2 k + 1 } } { \partial M ^ { 3 } } = 1 ^ { 3 } a _ { 1 } ^ { ( 2 k + 1 ) } + 3 ^ { 3 } a _ { 3 } ^ { ( 2 k + 1 ) } + \dots } } \\ { \displaystyle { \qquad + ( 2 k + 1 ) ^ { 3 } a _ { 2 k + 1 } ^ { ( 2 k + 1 ) } = \frac { 4 \cdot 5 \cdot \cdot \cdot ( 2 k + 3 ) } { 1 \cdot 2 \cdot \cdot \cdot \cdot 2 k } . } } \end{array} \right.
$$

These equations constitute a check which is independent of that given in (57). In a similar way check formulas can be found froma consideration of all odd derivatives of $E$ with respect to $M .$

Equations (57),(58)，and similar ones for higher derivatives of $\mathbfcal { E }$ ，are linear in the coefficients $a _ { j } ^ { ( k ) }$ ,which it is desired to find; consequently,when the number of equations equals the number of unknowns,the latter are uniquely determined,at least if the determinant of the coefficients is not zero. It can be shown that the determinant is not zero.

For the purposes of illustration suppose $\qquad k = 0$ 、Then the second equation of (57） gives $a _ { \mathfrak { r } } ^ { : 1 ) } = \bar { \mathbf { 1 } }$ whence $u _ { 1 } = \sin M$ agreeing with the result in (53). Suppose $k = 1$ ； then the first equation of (57） gives $2 a _ { 2 } ^ { ( 2 ) } = 1$ ，whence $u _ { 2 } = { \frac { 1 } { 2 } }$ sin $2 M$ As an illustration involving both (57） and (58)，suppose $k = 1$ and consider the second equations of (57) and (58). They become in this case

$$
\left\{ \begin{array} { l l } { { a _ { 1 } ^ { ( 3 ) } + ~ 3 a _ { 3 } ^ { ( 3 ) } = 1 , } } \\ { { } } \\ { { a _ { 1 } ^ { ( 3 ) } + 2 7 a _ { 3 } ^ { ( 3 ) } = { \displaystyle \frac { 4 \cdot 5 } { 1 \cdot 2 } } ; } } \end{array} \right.
$$

whence $\begin{array} { r } { a _ { 1 } ^ { ( 3 ) } = - \frac { 1 } { 8 } . } \end{array}$ ， $\begin{array} { r } { a _ { 3 } ^ { ( 3 ) } = + \frac { 3 } { 8 } } \end{array}$ ， agreeing with the results given in (53).

When the expansion is carried out by the method of Lagrange, or by that which has just been explained,the value of $\mathbfit { \Delta } E$ to terms of the sixth order in $e$ is found to be

$$
\left\{ \begin{array} { l l } { { { \cal { E } } = M + e \sin M + \frac { v ^ { 2 } } { 2 } \sin 2 M } } \\ { { \mathrm { } } } \\ { { \mathrm { } + \frac { e ^ { 3 } } { 3 ! 2 ^ { 3 } } \left( 3 ^ { 2 } \sin 3 M - 3 \sin M \right) } } \\ { { \mathrm { } + \frac { e ^ { 4 } } { 4 ! 2 ^ { 3 } } \left( 4 ^ { 3 } \sin 4 M - 4 \cdot 2 ^ { 2 } \sin 2 M \right) } } \\ { { \mathrm { } + \frac { e ^ { 8 } } { 5 ! 2 ^ { 4 } } \left( 5 ^ { 4 } \sin 5 M - 5 \cdot 3 ^ { 4 } \sin 3 M + 1 0 \sin M \right) } } \\ { { \mathrm { } + \frac { e ^ { 6 } } { 6 ! 2 ^ { 3 } } \left( 6 ^ { 8 } \sin 6 M - 6 \cdot 4 ^ { 5 } \sin 4 M + 1 5 \cdot 2 ^ { 8 } \sin 2 M \right) } } \\ { { \mathrm { } + \mathrm { } \mathrm { } \cdot \mathrm { } \mathrm { } \cdot \mathrm { } \mathrm { ~ . ~ . ~ . ~ } \mathrm { ~ . ~ . ~ } \mathrm { ~ . ~ } \mathrm { ~ . ~ } \mathrm { ~ } \cdot \mathrm { ~ } \mathrm { ~ } \mathrm { ~ ~ . ~ . ~ } \mathrm { ~ } \cdot \mathrm { ~ } \mathrm { ~ ~ . ~ } \mathrm { ~ } \cdot \mathrm { ~ } \mathrm { ~ ~ . ~ } \mathrm { ~ } \cdot \mathrm { ~ } \mathrm { ~ } \cdot \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \cdot \mathrm { ~ } \mathrm { ~ } \mathrm { ~ . ~ } \mathrm { ~ } \cdot \mathrm { ~ } \mathrm { ~ } \mathrm { ~ . ~ } \mathrm { ~ } \mathrm { ~ . ~ } } } \end{array} \right.
$$

100.The Development of $r$ and $v$ in Series. The value of $\boldsymbol { r }$ in terms of $e$ and $M$ can be obtained by the method of Lagrange by letting $F ( z ) = \cos { E }$ and making use of the last equation of (48). This method has the disadvantage of being rather laborious.

It follows from Kepler's equation that \*

$$
\left\{ \begin{array} { l l } { \displaystyle e \frac { \partial E } { \partial e } = \frac { e \sin E } { 1 - e \cos E } , } \\ { \displaystyle d M = ( 1 - e \cos E ) d E . } \end{array} \right.
$$

Therefore

$$
e \frac { \partial E } { \partial e } d M = e \sin E d E .
$$

\* The method employed in this Art.is due to MaMillan.

The integral of this equation gives

$$
e \int _ { 0 } ^ { \mathcal { M } } \frac { \partial E } { \partial e } d M = - \ e \cos E + c ,
$$

which expresses -ecos $E$ in terms of $M$ very simply by substituting in the left member the explicit value of $E$ given in (59). For example,the first terms are

$$
\begin{array} { c } { { - \displaystyle e \cos E = - c + e \int _ { 0 } ^ { \mathcal M } \left[ \sin M + e \sin 2 M \right. } } \\ { { \left. + \frac 3 8 e ^ { 2 } ( 3 \sin 3 M - \sin M ) + \cdots \right] d M } } \\ { { \left. = - c - e \cos M - \frac 1 2 e ^ { 2 } \cos 2 M - \frac 3 8 e ^ { 3 } ( \cos 3 M - \cos M ) \cdots \right. } } \end{array}
$$

The last equation of (48) and (60) give for $\pmb { r }$ the series

$$
\frac { r } { a } = 1 - e \cos E = 1 - c - e \cos M - \frac { 1 } { 2 } e ^ { 2 } \cos 2 M \cdots .
$$

It remains to determine the constant c. Since $\pmb { r }$ is measured from the focus of the ellipse,it follows that $r = a ( 1 - e )$ at $M = 0$ ； whence

$$
1 - e = 1 - c - e - { \frac { 1 } { 2 } } e ^ { 2 } + \cdots + b _ { i } e ^ { i } + \cdots ,
$$

where $b _ { j }$ is the coefficient of $e ^ { i }$ in the series for $- ~ e$ cos $\pmb { \cal E }$ at $M = 0$ · The two sides of this equation must be the same for all values of $e$ for which (61） converges；therefore $c$ must have the form

$$
\begin{array} { r } { c = c _ { 2 } e ^ { 2 } + c _ { 3 } e ^ { 3 } + \cdots , } \end{array}
$$

where $c _ { 2 } , \ c _ { 3 } , \ \cdots$ are determined so that the right member will contain no terms in $e ^ { 2 } , e ^ { 3 } , \cdots ;$ that is, $- \ : c _ { j } + b _ { j } = 0 , j = 2 , 3 , \cdots .$ Since-ecos $\pmb { \cal E }$ ,as defined by (6O),is the integral of a sine series it contains no constant terms；therefore the $b _ { j }$ are the sums of the coefficients of the cosine terms. Now consider

$$
\int _ { 0 } ^ { 2 \pi } { \frac { r } { a } } d M = \int _ { 0 } ^ { 2 \pi } \left[ 1 - c - e \cos M - { \frac { e ^ { 2 } } { 2 } } \cos 2 M + \cdot \cdot \cdot \right] d M .
$$

It was shown in Problem 4,p.154,that the value of this integral is $2 \pi ( 1 + { \textstyle { \frac { 1 } { 2 } } } e ^ { 2 } )$ .Therefore the coefficients of $e ^ { 3 } , e ^ { 4 } .$ · contain no constant terms and the exact value of $c$ is $\begin{array} { r l } { - } & { { } \frac { 1 } { 2 } e ^ { 2 } \cdot } \end{array}$

The series for ${ \frac { r } { a } } \operatorname { u p }$ to the sixth power of $e$ is

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { r } { a } = 1 - e \cos M - \frac { e ^ { 2 } } { 2 } \left( \cos 2 M - 1 \right) } \\ { \displaystyle \qquad - \frac { e ^ { 3 } } { 2 1 2 ^ { 2 } } \left( 3 \cos 3 M - 3 \cos { \mathcal { M } } \right) } \\ { \displaystyle \qquad - \frac { e ^ { 4 } } { 3 1 2 ^ { 3 } } \left( 4 ^ { 2 } \cos 4 M - 4 . 2 ^ { 2 } \cos 2 M \right) } \\ { \displaystyle \qquad - \frac { e ^ { 8 } } { 4 1 2 ^ { 4 } } \left( 5 ^ { 3 } \cos 5 M - 5 \cdot 3 ^ {  s } \cos 3 M + 1 0 \cos { \mathcal { M } } \right) } \\ { \displaystyle \qquad - \frac { e ^ { 6 } } { 5 1 2 ^ { 2 } } \left( 6 ^ { 4 } \cos 6 M - 6 \cdot 4 ^ { s } \cos 4 M + 1 5 \cdot 2 ^ { s } \cos 2 M \right) } \\ { \displaystyle \qquad - \ . \qquad . \qquad . \qquad . \qquad . \qquad . \qquad . \qquad . \qquad . \qquad . \qquad . \qquad . } \end{array} \right.
$$

The computation of the series for $v$ will now be considered.It follows from the first two equations of (49) that

$$
d v = \frac { \sqrt { 1 - e ^ { 2 } } } { ( 1 - e \cos E ) ^ { 2 } } d M ,
$$

which becomes as a consequence of Kepler's equation

$$
d v = \sqrt { 1 - e ^ { 2 } } \biggl ( \frac { d E } { d M } \biggr ) ^ { 2 } d M .
$$

The quantity $\frac { d { \cal E } } { d M }$ isfoudatoe9) and integrated gives， after $\textstyle { \sqrt { 1 - e ^ { 2 } } }$ has been expanded as a power series in $e ^ { 2 }$ ，

$$
\left\{ \begin{array} { l } { { \displaystyle v = \mathcal { M } + 2 e \sin { \mathcal { M } } + \frac { \varepsilon } { 4 } e ^ { 2 } \sin { 2 \mathcal { M } } } } \\ { { { } } } \\ { { { } + \frac { \varepsilon ^ { 2 } } { 1 2 } ( 1 3 \sin { 3 \mathcal { M } } - 3 \sin { \mathcal { M } } ) } } \\ { { { } } } \\ { { { } + \frac { \varepsilon ^ { 4 } } { 9 6 } ( 1 0 3 \sin { 4 \mathcal { M } } - 4 4 \sin { 2 \mathcal { M } } ) } } \\ { { { } } } \\ { { { } + \frac { e ^ { 6 } } { 9 6 0 } ( 1 0 9 7 \sin { 5 \mathcal { M } } - 6 4 5 \sin { 3 \mathcal { M } } + 5 0 \sin { \mathcal { M } } ) } } \\ { { { } { } + \frac { e ^ { 6 } } { 9 6 0 } ( 1 2 2 3 \sin { 6 \mathcal { M } } - 9 0 2 \sin { 4 \mathcal { M } } + 8 5 \sin { 2 \mathcal { M } } ) } } \\ { { { } + { } \ . { } \ . \ . \ . \ \ . \ . \ \ . \ \ . \ \ . \ \ . \ \ . \ \ . \ \ \ . \ \ . \ \ . \ \ . \ \ . \ \ . \ \ . \ \ . \ \ . } } \end{array} \right.
$$

When $^ e$ is small,as in the planetary orbits, these series are very rapidly convergent; if e exceeds 0.6627 ... they diverge， as

Laplace first showed, for some values of $M$ . This value of $e$ is exceeded in the solar system only in the case of some of the comets' orbits,but developments of this sort are not employed in computing the perturbations of the comets.

101.Direct Computation of the Polar Coordinates.\* It has been observed that there is considerable labor involved in finding the coordinates at any time in the case of elliptic motion. The question arises whether it may not be due partly to the fact that the final result is obtained by determining $\mathbfit { \Delta } E$ as an intermediary function from Kepler's equation. The question also arises whether the coordinates cannot conveniently be found directly from the differential equations. It will be shown that the answer to the latter question is in the affirmative.

Equations (16) become in polar coordinates

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } r } { d t ^ { 2 } } - r \left( \displaystyle \frac { d v } { d t } \right) ^ { 2 } + \displaystyle \frac { k ^ { 2 } ( 1 + m ) } { r ^ { 2 } } = 0 , } \\ { \displaystyle \frac { d } { d t } \left( r ^ { 2 } \displaystyle \frac { d v } { d t } \right) = 0 . } \end{array} \right.
$$

On integrating the second of these equations and eliminating $\frac { d v } { d t }$ frothefrstsfall

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } r } { d t ^ { 2 } } - \frac { h ^ { 2 } } { r ^ { 3 } } + \frac { k ^ { 2 } ( 1 + m ) } { r ^ { 2 } } = 0 , } \\ { \displaystyle r ^ { 2 } \frac { d v } { d t } = h = k \sqrt { ( 1 + m ) a ( 1 - e ^ { 2 } ) } . } \end{array} \right.
$$

After eliminating $k ^ { 2 } ( 1 + m )$ by the frst equation of (48) and changing from the independent variable $t$ to $M$ by means of the second equation of (48), these equations become

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } r } { d M ^ { 2 } } - \frac { a ^ { 4 } ( 1 - e ^ { 2 } ) } { r ^ { 3 } } + \frac { a ^ { 3 } } { r ^ { 2 } } = 0 , } \\ { \displaystyle \frac { d v } { d M } = \frac { a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } { r ^ { 2 } } . } \end{array} \right.
$$

The first equation of (65) is independent of the second and can be integrated separately.It is satisfied by $\pmb { r } = \pmb { a }$ and $e = 0$ ,in which case the orbit is a circleIn order to get the elliptic orbit let

\*This method was first published by the author in the Astronomical Journal,vol.25 (1907).

$$
r = a ( 1 - \rho e ) ,
$$

where ape is the deviation from a circle. When the planet is at perihelion, $r = a ( 1 - e )$ .Therefore $\rho = 1$ for $M = 0$ 、When the planet is at aphelion, $r = a ( 1 + \mathcal { e } )$ .Therefore $\rho = - 1$ for $M = \pi _ { : }$ and $\pmb { \rho }$ varis between $^ { - 1 }$ and $+ \textbf { 1 }$ Sinee $\frac { d r } { d M }$ is zero for $M$ equal to 0 and $\pi$ ,it follows that $\frac { d \rho } { d M }$ is zero for $M$ equal to O and $\pi$

When (66) is substituted in (65),these equations become

$$
\left\{ \begin{array} { l l } { \displaystyle { \frac { d ^ { 2 } \rho } { d M ^ { 2 } } } + \frac { \rho - e } { ( 1 - \rho e ) ^ { 3 } } = 0 , } \\ { \displaystyle { \frac { d v } { d M } } - \frac { \sqrt { 1 - e ^ { 2 } } } { ( 1 - \rho e ) ^ { 2 } } = 0 . } \end{array} \right.
$$

Since e is less than unity and $\pmb { \rho }$ varies from - 1 to $^ { + 1 }$ ，the second terms of these equations can be expanded as converging power series in $e$ ，giving

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } \rho } { d M ^ { 2 } } + \rho = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { \infty } { ( i + 1 ) [ i - ( i + 2 ) \rho ^ { 2 } ] \rho ^ { i - 1 } e ^ { i } } , } \\ { \displaystyle \frac { d v } { d M } = \sqrt { 1 - e ^ { 2 } } \sum _ { i = 0 } ^ { \infty } { ( i + 1 ) \rho ^ { i } e ^ { i } } . } \end{array} \right.
$$

It has been shown that $\boldsymbol { r }$ ,and hence $\pmb { \rho }$ ,is expansible as a power series in $e$ This fact also follows from the form of the first equation of (67） and the general principles of Differential Equations. Hence $\pmb { \rho }$ can be written in the form

$$
\rho = \rho _ { 0 } + \rho _ { 1 } e + \rho _ { 2 } e ^ { 2 } + \cdots ,
$$

where $\rho _ { 0 } , \ \rho _ { 1 } , \ \rho _ { 2 } , \ \cdot$ ·are functions of $M$ which remain to be determined. Since $\pmb { \rho }$ is periodic with the period $2 \pi$ for all $e$ less than unity,each $\rho _ { j }$ separately is a sum of trigonometric terms. Since the motion is symmetrical with respect to the major axis of the orbit,and since $M = 0$ when the planet is at its perihelion, $\rho$ is an even function of $M$ .This is true for all values of $e$ for which the series converges,and therefore each $\pmb { \rho } _ { j }$ is a sum of cosine terms.

A change in the sign of $e$ is equivalent to changing the origin to the other focus of the ellipse. Hence if the sign of $e$ is changed and $\pmb { \pi }$ is added to $M$ the value of $\pmb { r }$ is unchanged; from (66) it follows that the sign of $\pmb { \rho }$ is changed. Since this is true for all values of $\pmb { e }$ for which the series converges

$$
\rho _ { i } ( { \cal M } ) e ^ { i } = - \rho _ { i } ( { \cal M } + \pi ) ( - e ) ^ { i } .
$$

Therefore if $j$ is even $\pmb { \rho } _ { \pmb { j } }$ is a sum of cosines of odd multiples of $\pmb { M }$ ， and if $j$ is odd $\pmb { \rho _ { j } }$ is a sum of cosines of even multiples of $M$ It is seen on referring to equations (68)and (66) that this is the same property as that which was established Art.100.

It can easily be proved from the properties of the $\pmb { \rho } _ { \pmb { j } }$ and the second equation of (67) that $v$ is expressible as a series of the form

$$
\upsilon = \upsilon _ { 0 } + v _ { 1 } e + v _ { 2 } e ^ { 2 } + \cdots ,
$$

and that each $v _ { i } \left( j > 1 \right)$ is a sum of sines of integral multiples of $M$ A more detailed discussion shows that if $j$ is even $v _ { i }$ is a sum of sines of even multiples of $M$ ,and if $j$ is odd $v _ { j }$ is a sum of sines of odd multiples of $M$ ：

The solution can be directly constructed without any difficulty. The result of substituting (68) in the first of (67) is

$$
\begin{array} { c } { { \displaystyle \left[ \frac { d ^ { 2 } \rho _ { 0 } } { d M ^ { 2 } } + \frac { d ^ { 2 } \rho _ { 1 } } { d M ^ { 2 } } e + \frac { d ^ { 2 } \rho _ { 2 } } { d M ^ { 2 } } e ^ { 2 } + \cdots \right] + [ \rho _ { 0 } + \rho _ { 1 } e + \rho _ { 2 } e ^ { 2 } + \cdots ] } } \\ { { = [ 1 - 3 \rho _ { 0 } ^ { 2 } ] e + [ 3 \rho _ { 0 } - 6 \rho _ { 0 } \rho _ { 1 } - 6 \rho _ { 0 } ^ { 3 } ] e ^ { 2 } + \cdots . } } \end{array}
$$

On equating coefficients of corresponding powers of $\pmb { e }$ in the left and right members of this equation,it is found that

$$
\left\{ \begin{array} { l l } { ( a ) } & { \frac { d ^ { 2 } \rho _ { 0 } } { d M ^ { 2 } } + \rho _ { 0 } = 0 , } \\ { ~ } \\ { ( b ) } & { \frac { d ^ { 2 } \rho _ { 1 } } { d M ^ { 2 } } + \rho _ { 1 } = 1 - 3 \rho _ { 0 } \mathrm { ^ 2 } , } \\ { ~ } \\ { ( c ) } & { \frac { d ^ { 2 } \rho _ { 2 } } { d M ^ { 2 } } + \rho _ { 2 } = 3 \rho _ { 0 } ( 1 - 2 \rho _ { 1 } - 2 \rho _ { 0 } \mathrm { ^ 2 } ) , } \\ { ~ } \\ { ~ } \end{array} \right.
$$

Equations (7O) can be integrated in the order in which they are written. Two constants of integration arise at _each step and they are to be determined so that $\rho = 1$ and $\frac { d \rho } { d M } = 0$ for $M = 0$ whatever may be the value of $\pmb { e } ,$ It follows from (68) that these conditions are

$$
\left\{ \begin{array} { l l } { \rho ( 0 ) = \rho _ { 0 } ( 0 ) + \rho _ { 1 } ( 0 ) e + \rho _ { 2 } ( 0 ) e ^ { 2 } + \cdots = 1 , } \\ { \displaystyle \frac { d \rho } { d M } = \frac { d \rho _ { 0 } } { d M } + \frac { d \rho _ { 1 } } { d M } e + \frac { d \rho _ { 2 } } { d M } e ^ { 2 } + \cdots = 0 , } \end{array} \right.
$$

where $M$ is given the value O after the derivatives of the second equation have been formed. Since these equations hold for all values of $e$ ,it follows that

$$
\left\{ \begin{array} { c c c c } { { \rho _ { 0 } ( 0 ) = 1 , } } & { { \quad \rho _ { 1 } ( 0 ) = 0 , \quad } } & { { \rho _ { 2 } ( 0 ) = 0 , } } & { { \quad \cdots , } } \\ { { \displaystyle \frac { d \rho _ { 0 } } { d M } = 0 , \quad } } & { { \displaystyle \frac { d \rho _ { 1 } } { d M } = 0 , \quad } } & { { \displaystyle \frac { d \rho _ { 2 } } { d M } = 0 , \quad } } & { { \cdots . } } \end{array} \right.
$$

The general solution of equation $( a )$ of (70) is (Art.32)

$$
\rho _ { 0 } = a _ { 0 } \cos M + b _ { 0 } \sin M ,
$$

where $a _ { 0 }$ and $b _ { 0 }$ are the constants of integration. It follows from (71) that $a _ { 0 } = 1 , b _ { 0 } = 0$ ,and therefore that

$$
\rho _ { 0 } = \cos M .
$$

The fact that $b _ { 0 }$ is zero also follows from the general property that the $\pmb { \rho } _ { j }$ involve only cosines.

On substituting the value of $\pmb { \rho _ { 0 } }$ in the right member of $( b )$ of (70), this equation becomes

$$
\frac { d ^ { 2 } \rho _ { 1 } } { d M ^ { 2 } } + \rho _ { 1 } = - \ \frac { 1 } { 2 } - \frac { 3 } { 2 } \cos 2 M .
$$

This equation can be solved by the method of the variation of parameters (Art.37). But since the part of the solution which comes from the right member will contain terms of the same form as the right member,it is simpler to substitute the expression

$$
\rho _ { 1 } = a _ { 1 } \cos M + b _ { 1 } \sin M + c _ { 1 } + d _ { 1 } \cos 2 M
$$

in the differential equation and to determine $c _ { 1 }$ and $d _ { 1 }$ so that it will be satisfied. This leads to the solution

$$
\rho _ { 1 } = a _ { 1 } \cos M + b _ { 1 } \sin M - \textstyle { \frac { 1 } { 2 } } + \textstyle { \frac { 1 } { 2 } } \cos 2 M ,
$$

which is the general solution since it satisfies the differential equation and has the two arbitrary constants ${ a } _ { 1 }$ and $b _ { 1 }$ On determining ${ { a } _ { 1 } }$ and $b _ { 1 }$ by (71), the expression for $\pmb { \rho _ { 1 } }$ becomes

$$
\rho _ { 1 } = - \textstyle { \frac { 1 } { 2 } } + \frac { 1 } { 2 } \cos 2 M .
$$

With the values of po and p1 which have been found equation (c) of (70) becomes

$$
\frac { d ^ { 2 } \rho _ { 2 } } { d M ^ { 2 } } + \rho _ { 2 } = - 3 \cos 3 M ,
$$

of which the general solution is

$$
\rho _ { 2 } = a _ { 2 } \cos M + b _ { 2 } \sin M + { \textstyle \frac { 3 } { 8 } } \cos 3 M .
$$

If az and bz are determined by (71),the final expression for p2 becomes

$$
\rho _ { 2 } = { \textstyle \frac { 3 } { 8 } } ( - \cos { \cal M } + \cos { 3 { \cal M } } ) .
$$

This process of integration can be continued as far as may be desired. It follows from the results which have been found that

$$
\begin{array} { r l } & { \frac { r } { a } = 1 - \rho e = 1 - ( \rho _ { 0 } + \rho _ { 1 } e + \rho _ { 2 } e ^ { 2 } + \cdots ) e } \\ & { \quad = 1 - e \cos M - \frac { 1 } { 2 } e ^ { 2 } ( \cos 2 M - 1 ) - \frac { 3 } { 8 } e ^ { 3 } ( \cos 3 M - \cos M ) \cdots } \end{array}
$$

which agrees with those given in (62).

When the values for $\rho _ { 0 } , \ \rho _ { 1 } ,$ .\*. are substituted in the second equation of (67),the result is

$$
\frac { d v } { d M } = 1 + 2 e \cos M + \textstyle { \frac { \delta } { 2 } } e ^ { 2 } \cos 2 M + \cdots ,
$$

and the integral of this equation is

$$
\begin{array} { r } { v = c + M + 2 e \sin M + \frac { 5 } { 4 } e ^ { 2 } \sin 2 M + \cdots . } \end{array}
$$

Sipce $\pmb { v } = \mathbf { 0 }$ when $M = 0$ ，the arbitrary constant $\pmb { c }$ is zero,and the result agrees with that given in (64).

The method which has just been developed is,for this special problem，perhaps not superior to that depending upon the solution of Kepler's equation. But if the conditions of the problem are: modified a little,for example by adding the terms which would come from the oblateness of a planet when the body moves in the plane of its equator [equations (30),Chapter IV], Kepler's equation no longer holds and the method depending on it fails, while the one under consideration here can be applied without any modification except in the numerical values of the coeffcients which depend upon the terms added to the differential equations. But additional terms in the differential equations change the period of the motion,if indeed it remains periodic,and in order to exhibit the periodicity explicitly some modifications of the methods of determining the constants of integration are in general necessary. This method of integrating in series is typical of those which are employed in the theories of perturbations and the more difficult parts of Celestial Mechanics,and for this reason it should be thoroughly mastered.

102.Position in Hyperbolic Orbits. There are close analogies between this problem and that of finding the position of a body in an elliptic orbit. But it follows from the polar equation of +he hyperbola,

$$
r = \frac { a ( \epsilon ^ { 2 } - 1 ) } { 1 + \epsilon \cos v } ,
$$

where $^ { a }$ is its major semi-axis and e its eccentricity, that in this c8 $\begin{array} { r } { \mathrm { \ s e \ } v \mathrm { \ c a n \ v a r y \ o n l y \ f r o m } - \pi + \cos ^ { - 1 } \left( \frac { 1 } { \epsilon } \right) \mathrm { \ t o } + \pi - \cos ^ { - 1 } \left( \frac { 1 } { \epsilon } \right) . } \end{array}$

The integrals of areas and vis viva are respectively in the case of hyperbolic orbits

$$
\left\{ \begin{array} { r } { r ^ { 2 } \displaystyle \frac { d v } { d t } = k \sqrt { ( 1 + m ) a ( \epsilon ^ { 2 } - 1 ) } , } \\ { \left( \displaystyle \frac { d r } { d t } \right) ^ { 2 } + r ^ { 2 } \left( \displaystyle \frac { d v } { d t } \right) ^ { 2 } = k ^ { 2 } ( 1 + m ) \left( \displaystyle \frac { 2 } { r } + \displaystyle \frac { 1 } { a } \right) , } \end{array} \right.
$$

On eliminating $v$ from the second of these equations by means of the first and solving,it is found that

where

$$
\begin{array} { c l c r } { { a \nu d t = \displaystyle \frac { r d r } { \sqrt { ( a + r ) ^ { 2 } - a ^ { 2 } \epsilon ^ { 2 } } } , } } \\ { { \nu = \displaystyle \frac { k \ \sqrt { 1 + m } } { a ^ { 3 } } . } } \end{array}
$$

This equation can be integrated at once in terms of hyperbolic functions,but it is preferable to introduce first an auxiliary quantity $\pmb { F }$ corresponding to the eccentric anomaly in eliptic orbits.Let

$$
a + r = \frac { a \epsilon } 2 ( e ^ { r } + e ^ { - r } ) = a \epsilon \cosh F ;
$$

then

$$
\begin{array} { l } { \displaystyle { \nu d t = \left\{ - 1 + \frac { \epsilon } { 2 } \left( e ^ { F } + e ^ { - F } \right) \right\} d F = [ - 1 + \epsilon \cosh F ] d F . } } \end{array}
$$

The integral of this equation is

$$
M = \nu ( t - T ) = - \ F + \frac { \epsilon } { 2 } ( e ^ { r } - e ^ { - F } ) = - \ F + \epsilon \sinh F ,
$$

which gives $\pmb { t }$ when $\pmb { F }$ is known. The inverse problem of finding $\pmb { F }$ when $\nu ( t - T )$ is given is one of more difficulty. The most expeditious method would be,in general, to find an approximate value of $\pmb { F }$ by some graphical process,and then a more exact value by differential corrections. The value of $\pmb { F }$ satisfying (74) is the abscissa of the point of intersection of the line

$$
y = \frac { 1 } { \epsilon } \left( F + M \right) ,
$$

and the hyperbolic sine curve

$$
y = \frac { e ^ { F } - e ^ { - F } } { 2 } = \sinh F .
$$

The differential corrections could be computed in a manner analogous to that developed in the case of the ellptic orbits.

From (73) and the polar equation of the hyperbola, it follows that

$$
r = \frac { a ( \epsilon ^ { 2 } - 1 ) } { 1 + \epsilon \cos v } = a [ - 1 + \epsilon \cosh F ]
$$

and from this equation,

$$
\tan { \frac { v } { 2 } } = \sqrt { \frac { \epsilon + 1 } { \epsilon - 1 } } \frac { \sqrt { - 1 + \frac { 1 } { 2 } ( e ^ { F } + e ^ { - F } ) } } { \sqrt { + 1 + \frac { 1 } { 2 } ( e ^ { F } + e ^ { - F } ) } } = \sqrt { \frac { \epsilon + 1 } { \epsilon - 1 } } \mathrm { t a n h } { \frac { F } { 2 } } ,
$$

which is a convenient formula for computing $\pmb { v }$ when $\pmb { F }$ has been found.

103.Position in Elliptic and Hyperbolic Orbits when e is Nearly Equal to Unity. The analytical solutions heretofore given have depended upon expansions in powers of $e$ If $e$ is large,as in the case of some of the periodic comets’orbits,the convergence ceases or is so slow that the methods become impracticable. The graphical process, however,avoids this difficulty.

In order to obtain a workable analytical solution, the developments for elliptical orbits will be made in powers of $\frac { 1 - e } { 1 + e }$ The start is made from the equation of areas and the polar equation of the orbit which will be assumed to be an ellipse.

Let

$$
\left\{ \begin{array} { l l } { { w = \tan { \frac { v } { 2 } } , } } \\ { { \phantom { - } \lambda = { \frac { 1 - e } { 1 + e } } ; } } \end{array} \right.
$$

then the equation of areas becomes

$$
\frac { \mathfrak { X } \sqrt { \mathrm { \Large ~ i ~ } + \mathrm { \Large ~ e } } } { 2 ( 1 - \mathrm { \Large ~ e } ) ^ { \sharp } } d t = \frac { ( \mathrm { \small ~ i ~ } + w ^ { \mathfrak { s } } ) } { ( 1 + \lambda w ^ { 2 } ) ^ { 2 } } \dot { d } w .
$$

When $\pmb { \lambda }$ is very small the right member of this equation can be developed into a rapidly converging series in $\lambda$ for all values of $\pmb { v }$ not too near $1 8 0 ^ { \circ }$ .Since the periodic comets are always invisible when near aphelion, there will seldom be occasion to consider the solution in this region. On expanding the right member and integrating,the result is found to be

$$
\begin{array} { c } { { \displaystyle \frac { n ( 1 + e ) ^ { \sharp } } { 2 ( 1 - e ) ^ { \sharp } } ( t - T ) = w + \frac { w ^ { 3 } } { 3 } - 2 \lambda \left( \frac { w ^ { 3 } } { 3 } + \frac { w ^ { 5 } } { 5 } \right) } } \\ { { + \ : 3 \lambda ^ { 2 } \left( \frac { w ^ { 5 } } { 5 } + \frac { w ^ { 7 } } { 7 } \right) - 4 \lambda ^ { 3 } \left( \frac { w ^ { 7 } } { 7 } + \frac { w ^ { 9 } } { 9 } \right) + \cdots . } } \end{array}
$$

When the orbit is a parabola $e = 1$ and $\lambda = 0$ ，and this equation reduces to (32)，which is a cubic in $_ w$ .Since the perihelion distance in an ellipse is $q = a ( 1 - e )$ and $n = { \frac { k } { a ^ { \frac { 3 } { 2 } } } }$ ，it follows that

$$
\frac { n \sqrt { 1 + e } } { 2 ( 1 - e ) ^ { \sharp } } = \frac { k } { 2 q ^ { \sharp } } .
$$

It is desired to find the value of $\boldsymbol { w }$ for any value of $\scriptstyle t .$ If the eccentricity should become equal to unity,the left member keeping the same value,equation (75) would have the form

$$
\frac { k ( 1 + e ) ^ { \ddagger } } { 2 q ^ { \ddagger } } ( t - T ) = W + \frac { \ d H } { \ d s } W ^ { \downdownarrows } ,
$$

where $\boldsymbol { \varpi }$ would be the tangent of half the true anomaly in the resulting parabolic orbit. From this equation $\pmb { W }$ can be determined by means of Barker's tables,or from equations (33). Suppose $W$ has been found; then $\boldsymbol { w }$ can be expressed as a series in $\lambda$ of which the coefficients are functions of $\boldsymbol { \ W }$ For,assume the development

$$
w = a _ { 0 } + a _ { 1 } \lambda + a _ { 2 } \lambda ^ { 2 } + a _ { 3 } \lambda ^ { 3 } + \cdots ;
$$

substitute it in the right member of (75),which is equal to the right member of (76). The result of the substitution is

$$
\begin{array} { c } { { W + \displaystyle \frac { W ^ { 3 } } { 3 } = a _ { 0 } + \displaystyle \frac { a _ { 0 } ^ { 3 } } { 3 } + \bigl [ a _ { 1 } + a _ { 0 } { } ^ { 2 } a _ { 1 } - \frac { 2 } { 8 } a _ { 0 } { } ^ { 3 } - \frac { 2 } { 5 } a _ { 0 } { } ^ { 5 } \bigr ] \lambda } } \\ { { \mathrm { } } } \\ { { \mathrm { } + \bigl [ a _ { 2 } + a _ { 0 } { } ^ { 2 } a _ { 2 } + a _ { 0 } a _ { 1 } { } ^ { 2 } - 2 a _ { 0 } { } ^ { 2 } a _ { 1 } - 2 a _ { 0 } { } ^ { 4 } a _ { 1 } + \frac { 3 } { 8 } a _ { 0 } { } ^ { 5 } + \frac { 3 } { 7 } a _ { 0 } { } ^ { 7 } \bigr ] \lambda ^ { 2 } } } \\ { { \mathrm { } + \bigl [ a _ { 3 } + a _ { 0 } { } ^ { 2 } a _ { 3 } + \frac { a _ { 1 } { } ^ { 3 } } { 3 } - 2 a _ { 0 } { } ^ { 2 } a _ { 2 } - 2 a _ { 0 } { } ^ { 4 } a _ { 2 } - 2 a _ { 0 } a _ { 1 } { } ^ { 2 } } } \\ { { \mathrm { } , \mathrm { ~ \ ~ \ } , \mathrm { ~ \ ~ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } { ~ \ } \mathrm { ~ \ } { ~ \ } \mathrm { ~ \ } { ~ \ } \mathrm { ~ \ } { ~ \ } \mathrm { ~ \ } { ~ \ } \mathrm { ~ \ } { ~ \ } \mathrm { ~ \ } { ~ \ } } } \end{array}
$$

Since this equation is an identity in $\lambda$ ，the coefficients of corresponding powers of $\lambda$ are equal. Hence

$$
\left\{ \begin{array} { l } { \displaystyle a _ { 0 } + \frac { a _ { 0 } ^ { a ^ { 3 } } } { 3 } = W + \frac { W ^ { 3 } } { 3 } , } \\ { \displaystyle a _ { 1 } ( 1 + a _ { 0 } ^ { \sigma } ) = \frac { 2 } { 8 } a _ { 0 } ^ { a ^ { 3 } } + \frac { 2 } { 9 } a _ { 0 } ^ { 5 } , } \\ { \displaystyle a _ { 2 } ( 1 + a _ { 0 } ^ { \sigma } ) = - \ a _ { 0 } a _ { 1 } ^ { 2 } + 2 a _ { 0 } ^ { \sigma } a _ { 1 } + 2 a _ { 0 } ^ { 4 } a _ { 1 } - \frac { 3 } { 8 } a _ { 0 } ^ { 5 } - \frac { 3 } { 7 } a _ { 0 } ^ { 7 } , } \\ { \displaystyle a _ { 3 } ( 1 + a _ { 0 } ^ { z } ) = - \frac { a _ { 1 } ^ { 3 } } { 3 } + 2 a _ { 0 } ^ { \sigma } a _ { 2 } + 2 a _ { 0 } ^ { 4 } a _ { 2 } + 2 a _ { 0 } a _ { 1 } ^ { 2 } + 4 a _ { 0 } ^ { 3 } a _ { 1 } ^ { 2 } } \\ { \displaystyle \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad - 3 a _ { 0 } ^ { 4 } a _ { 1 } - 3 a _ { 0 } ^ { 6 } a _ { 1 } + \frac { 4 } { 7 } a _ { 0 } ^ { 7 } + } \\ { . } \end{array} \right.
$$

There are three solutions for ${ \bf { \mathit { a } } _ { 0 } } ,$ only one of which is real. On taking the real root of the first equation,it is found that

$$
\begin{array} { r l } & { \left| { a _ { 1 } } = \frac { { \frac { { 2 } } { 8 } } { { W ^ { 3 } } } + { \frac { { 2 } } { 8 } } { { W ^ { 5 } } } } { { 1 + { W ^ { 2 } } } } , \right. } \\ & { \left| { a _ { 2 } } = \frac { { { \frac { { 1 1 } } { 1 5 } } { { W ^ { 5 } } } + \frac { { 4 3 0 } } { 3 1 5 } { { W ^ { 7 } } } + \frac { { 8 3 } } { 8 5 } { { W ^ { 9 } } } + \frac { { 3 7 } } { 1 7 5 } { { W ^ { 1 1 } } } } } { { { ( 1 + { W ^ { 2 } } ) ^ { 3 } } } } , \right. } \\ &  \left. { a _ { 3 } } = \frac { { \frac { { 2 9 2 } } { 1 6 } { W ^ { 7 } } + \frac { { 7 9 2 8 } } { 2 8 3 5 } { { W ^ { 9 } } + \frac { { 1 0 3 2 8 } } { 2 8 3 5 } { W ^ { 1 1 } } + \frac { { 4 3 2 } } { 1 7 5 } { { W ^ { 1 3 } } } + \frac { { 6 6 9 2 } } { 7 8 7 5 } { W ^ { 1 5 } } + \frac { 1 8 4 } { 1 5 7 5 } { { W ^ { 1 1 } } } } } { { ( 1 + { W ^ { 2 } } ) ^ { 5 } } } , \right. } \end{array}
$$

When the values of these coefficients are substituted in (77） the tangent of one-half the true anomaly is determined. The first term gives that which would come from a parabolic orbit,the remaining terms vanishing for $e = 1$ .In the series (64) the first term in the right member would be the true anomaly if the orbit were a circle,the higher terms being the corrections to circular motion.In the series (77) the first term in the right member would give the tangent of one-half the true anomaly if the orbit were a parabola,the higher terms being the corrections to parabolic motion.

These equations apply equally to hyperbolic orbits in which the eccentricity is near unity if $1 - e$ and $1 + e$ are changed to $\epsilon - 1$ and $\epsilon + 1$ throughout, where $\bullet$ is the eccentricity of the hyperbola.

# XV. PROBLEMS.

1. Show how the cubic equation (32） can be solved approximately for tan $\frac { v } { 2 }$ withgreatrapiitybytheaidofagraphicalcostrution.

2.Develop the equations for differential corrections to the approximate values found by the graphical method.Apply to a particular problem and verify the result.

3.If $e = 0 . 2$ and $M = 2 1 4 ^ { \circ }$ ,find $E _ { 0 } , M _ { 0 } , E _ { 1 } , M _ { 1 } , E _ { 2 } ,$ and $M _ { 2 }$

Ans. $E _ { 0 } = 2 0 8 ^ { \circ } 3 9 ^ { \prime } 1 6 ^ { \prime \prime } . 6 , \quad M _ { 0 } = 2 1 4 ^ { \circ } 8 ^ { \prime } 5 8 ^ { \prime \prime } . 6 ; \quad E _ { 1 } = 2 0 8 ^ { \circ } 3 1 ^ { \prime } 3 8 ^ { \prime \prime } . 4 ,$ $M _ { 1 } = 2 1 3 ^ { \circ } ~ 5 9 ^ { \prime } ~ 5 9 ^ { \prime \prime } . 8 ; \quad E _ { 2 } = 2 0 8 ^ { \circ } ~ 3 1 ^ { \prime } ~ 3 8 ^ { \prime \prime } . 6 , \quad M _ { 2 } = 2 1 4 ^ { \circ } ~ 0 0 ^ { \prime } ~ 0 0 ^ { \prime \prime } .$

4.Show from the curves employed in solving Kepler's equation that the solution is unique for all values of $e < 1$ and $M$

5.In (50) the quadrant is not determined by the equation； show that corresponding values of $\scriptstyle { \frac { 1 } { 2 } } v$ and $\scriptstyle { \frac { 1 } { 2 } } E$ always lie in the same quadrant.

6.Express the rectangular coordinates $x = r$ cos v, $\boldsymbol { y } = \boldsymbol { r }$ sin $v$ in terms of the eccentric anomaly，and then,by means of the Lagrange expansion formula,in terms of $M$

$$
\left\{ \begin{array} { l } { { \displaystyle \frac { x } { a } = \cos { \cal M } + \frac { e } { 2 } ( \cos { 2 \cal M } - 3 ) + \frac { e ^ { 2 } } { 2 ! 2 ^ { 2 } } ( 3 \cos { 3 \cal M } - 3 \cos { \cal M } ) } } \\ { { \qquad \quad + \frac { e ^ { 3 } } { 3 ! 2 ^ { 3 } } ( 4 ^ { 2 } \cos { 4 \cal M } - 4 \cdot 2 ^ { 2 } \cos { 2 \cal M } ) + \cdots } } \\ { { \displaystyle \frac { y } { a } = \sin { \cal M } + \frac { e } { 2 } \sin { 2 \cal M } + \frac { e ^ { 2 } } { 3 ! 2 ^ { 2 } } ( 3 ^ { 2 } \sin { 3 \cal M } - 1 5 \sin { \cal M } ) } } \\ { { \qquad \quad + \frac { e ^ { 3 } } { 4 ! 2 ^ { 3 } } ( 4 ^ { 3 } \sin { 4 \cal M } - 1 0 \cdot 2 ^ { 3 } \sin { 2 \cal M } ) + \cdots . } } \end{array} \right.
$$

7. Show that the properties of $E$ asa power serieg in $e$ ，which were established in Art.99,follow from the Lagrange expansion.

8.Derive the firet three terms of the series for $\pmb { r }$ by the Lagrange formula.

9.Give a geometrical interpretation of $\pmb { F }$ (Art.102） corresponding to that of $\pmb { \cal E }$ in an elliptic orbit.

10.Express $v$ as a power series in e by a method analogous to that used in Ait. 103.

11.Show that the branch of the hyperbola which is convex to the sun is described by the body in purely imaginary time.

12.Add to the right members of equations (16)the terms $- { \frac { 3 } { 1 0 } } ( 1 + m ) b ^ { 2 } { e _ { 1 } } ^ { 2 } { \frac { x } { r ^ { 5 } } }$ and $- { \frac { 3 } { 1 0 } } ( 1 + m ) b ^ { 2 } { e _ { 1 } } ^ { 2 } { \frac { y } { r ^ { 5 } } }$ ，whichcomrbateesf tetralbod [equations (30), Chap.Iv.],where $\scriptstyle { e _ { 1 } }$ is the əccentricity of a meridian section. and integrate by the method of Art.101.

104.The Heliocentric Position in the Ecliptic System. Methods have been given for finding the positions in the orbits in the various cases which arise. The formulas will now be derived for determining the position referred to different systems of axes, The origin will first be kept fixed at the body with respect to which the motion of the second is given. Since most of the applications are in the solar system where the origin is at the center of the sun, the coordinates will be called heliocentric.

Positions of bodies in the solar system are usually referred to one of two systems of coordinates， the ecliptic system，or the equatorial system. The fundamental plane in the ecliptic system is the plane of the earth's orbit; in the equatorial system it is the plane of the earth's equator. The zero point of the fundamental circles in both systems is the vernal equinox,or the point at which the ecliptic cuts the equator from south to north,and is denoted by $\looparrowleft$ .The polar coordinates in the ecliptic system are called longitude and latitude;and in the equatorial,right ascension and declination. When the origin is at the sun Roman letters are used to represent the coordinates,and when at the earth,Greek. Thus

Origin at sun. Origin at earth.

$$
\begin{array} { r l } { \mathrm { t u d e } } & { { } \begin{array} { l l l l l l l } { \mathrm { t u d e } } & { { } } & { l } & { { } } & { \quad \lambda } & { { } { \mathrm { m e a s u r e d ~ e a s t w a r d . } } } \end{array} } \\ { \mathrm { a d e } } & { { } \begin{array} { l l l l l l } { \mathrm { ~ } } & { b } & { { } } & { } & { \beta } & { { } + \mathrm { ~ i f ~ n o r t h } ; \mathrm { ~ } - \mathrm { ~ i f ~ s o u t h . } } & { } \\ { \mathrm { a s c e n s i o n } } & { { } } & { a } & { { } } & { \alpha } & { { } { \mathrm { m e a s u r e d ~ e a s t w a r d . } } } \end{array} } \\ { \mathrm { a a t i o n } } & { { } \begin{array} { l l l l l l } { \mathrm { ~ } } & { d } & { { } } & { } & { \delta } & { { } + \mathrm { ~ i f ~ n o r t h } ; \mathrm { ~ - ~ i f ~ s o u t h . } } & { } \\ { \mathrm { r e } } & { { } } & { r } & { { } } & { \rho } & { { } } \end{array} } \end{array}
$$

In practice $^ { a }$ and $\scriptstyle { d }$ are very seldom used. Absolute positions of fundamental stars are given in the equatorial system，and the observed positions of comets are determined by comparison with them. In some theories relating to planets and comets,especially in considering the mutual perturbation of planets and their perturbations of comets,it is more convenient to use the ecliptic system; hence it is necessary to be able to transform the equations from one system to the other.

The ascending node is the projection on the ecliptic, from the sun,of the place at which the body crosses the plane of the ecliptic from south to north.It is measired from a fixed point in the ecliptic,the vernal equinox,and is denoted by $\boldsymbol { \Omega }$ . The projection of the point where the body crosses the plane of the ecliptic from north to south is called the dzscending node, and is denoted by .

The inclination is the angle between the plane of the orbit and the plane of the ecliptic,and is denoted by $\therefore$ 、It has been the custom of some writers to take the inclination always less than $9 0 ^ { \circ }$ ，and to define the direction of motion as direct or retrograde, according as it is the same as that of the earth or the opposite. Another method that has been used is to consider all motion direct and the inclination as varying from $0 ^ { \circ }$ to $1 8 0 ^ { \circ }$ .The latter method avoids the use of double signs in the formulas and is adopted here. [See Art.86.] The node and inclination define the position of the plane of the orbit in spacu.

The distance from the ascending node to the perihelion point counted in the direction of the motion of the body in its orbit is $\pmb { \omega }$ ， and defines the orientation of the orbit in its plane. The longitude of the perihelion is denoted by $\pmb { \pi }$ ，and is given by the equation

$$
\pi = \Omega + \omega .
$$

This element is not a longitude in the ordinary sense because it is counted in two different planes.

The problem of relative motion of two bodies was of the sixth order (Art.85),and in the integration six arbitrary constants were introduced. There are six elements,therefore，which are independent functions of these constants. They are

${ \pmb a } =$ major semi-axis,which defines the size of the orbit and the period of revolution.   
${ \pmb e } =$ the eccentricity,which defines the shape of the orbit.   
$\begin{array} { r l } { \small } & { { } \partial _ { \mathbf { \alpha } } = } \end{array}$ longitude of ascending node,and   
${ \dot { \mathfrak { i } } } =$ inclination to plane of the ecliptic,which together define the position of the plane of the orbit.   
$\omega =$ longitude of the perihelion point measured froim the node, or $\pi =$ longitude of the perihelion,either defining the orientation of the orbit in its plane.   
$\pmb { T } =$ time of perihelion passage,defining，with the other elements,the position of the body in its orbit at any time.

The polar coordinates have been computed； hence the rectangular coordinates with the positive end of the $_ x$ -axis directed to the periheiion point and the $_ y$ -axis in the plane of the orbit are given by the equations

$$
\left\{ { \begin{array} { l } { x _ { 0 } = r \cos \upsilon , } \\ { y _ { 0 } = r \sin \upsilon , } \\ { z _ { 0 } = 0 . } \end{array} } \right.
$$

If the $\pmb { x }$ -axis is rotated backward to the line of nodes,the coordiates in the new system are

$$
\left\{ \begin{array} { l l } { x = r \cos { ( v + \omega ) } = r \cos { ( v + \pi - \Omega ) } , } \\ { y = r \sin { ( v + \omega ) } = r \sin { ( v + \pi - \Omega ) } , } \\ { z = 0 . } \end{array} \right.
$$

The longitude of the body in its orbit counted from the ascending node is called the argument of the latitude and is denoted by ${ \pmb u } .$ It is given by the equation

$$
u = v + \omega ;
$$

hence u is known when $v$ has been found.

![](images/3e0f91c19190917ff0f2817a1641ebe73dc14628b3e90de031315849b03ed7a2.jpg)  
Fig.30.

Let $\boldsymbol { \vartheta }$ represent the sun and Sxy the plane of the ecliptic; ${ \pmb S } \Omega { \pmb A }$ ， the plane of the orbit; $\Omega$ ， the ascending node; $\pi$ ，the perihelion point; $\pmb { A }$ ，the projection of the position of the body；and angle $\Pi { \cal S } A = v$ Then $\Omega { \cal A } = \omega + v = u .$

Let the position of the body now be referred to a rectangular system of axes with the origin at the sun, the $_ { \pmb { x } }$ -axis in the line of the nodes, and the $_ y$ -axis in the plane of the ecliptic. Then equations (79) become

$$
\begin{array} { r l } & { \left\{ \begin{array} { l l } { x ^ { \prime } = r \cos { ( v + \omega ) } = r \cos { u } , } \\ { y ^ { \prime } = r \sin { ( v + \omega ) } \cos { i } = r \sin { u } \cos { i } , } \\ { z ^ { \prime } = r \sin { ( v + \omega ) } \sin { i } = r \sin { u } \sin { i } . } \end{array} \right. } \end{array}
$$

But,in terms of the heliocentric latitude and longitude,

$$
\left\{ \begin{array} { l l } { x ^ { \prime } = r \cos b \cos ( l - \delta ) , } \\ { y ^ { \prime } = r \cos b \sin ( l - \delta ) , } \\ { z ^ { \prime } = r \sin b . } \end{array} \right.
$$

Therefore,comparing (80) and (81),it is found that

whence

$$
\left\{ \begin{array} { l l } { \cos b \cos ( { l - \delta } ) = \cos u , } \\ { \cos b \sin ( { l - \delta } ) = \sin u \cos i , } \\ { \sin b } & { = \sin u \sin i ; } \end{array} \right.
$$

$$
\left\{ \begin{array} { l l } { \tan { ( \mathit { l } - \delta ) } = \tan { u } \cos { i } , } \\ { \tan { b } } & { = \tan { i } \sin { ( \mathit { l } - \delta ) } . } \end{array} \right.
$$

Since cos $\pmb { b }$ is always positive,equations (82) and (83) determine the heliocentric longitude and latitude, $\boldsymbol { l }$ and $\boldsymbol { b }$ ，uniquely when $\delta \boldsymbol { \delta } , i ,$ and $\textbf { \em u }$ are known.

105.Transfer of the Origin to the Earth. Let E,H,Z be the geocentric coordinates of the center of the sun referred to a system of axes with the $\pmb { x }$ -axis directed to the vernal equinox,and the $y .$ -axis in the plane of the ecliptic.Let P, $\Lambda$ ,and $\mathbf { B } ^ { * }$ represent the geocentric distance,longitude,and latitude of the sun respectively. These quantities are given in the Nautical Almanac for every day in the year. The rectangular coordinates are expressed in terms of them by

$$
\left\{ \begin{array} { l l } { \Xi = \mathrm { { P } } \cos \mathrm { { B } } \cos \mathrm { { A } } , } \\ { \mathrm { { H } } = \mathrm { { P } } \cos \mathrm { { B } } \sin \mathrm { { A } } , } \\ { \mathrm { { Z } } = \mathrm { { P } } \sin \mathrm { { B } } . } \end{array} \right.
$$

The angle B is generally less than a second of arc,and unless great &ccuracy is required these equations may be replaced by

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \Xi = \mathrm { \bf ~ P } \cos \mathrm { \bf ~ A } , } \\ { \mathrm { \bf ~ H } = \mathrm { \bf ~ P } \sin \mathrm { \bf ~ A } , } \\ { \mathrm { \bf ~ Z } = 0 . } \end{array} \right. } \end{array}
$$

Let $\xi ^ { \prime \prime } , \ \eta ^ { \prime \prime }$ and $\zeta ^ { \prime \prime }$ be the geocentric,and $x ^ { \prime \prime } , \ y ^ { \prime \prime }$ ，and $z ^ { \prime \prime }$ the heliocentric,coordinates of the body with the $\pmb { x }$ -axis directed toward the vernal equinox and the $_ y$ -axis in the plane of the ecliptic.Therefore

$$
{ \bf \mathrm { \bf ~ ^ { * } ~ P } } , { \bf \Phi } , { \bf B } = \mathrm { c a p i t a l } \rho , \lambda , \beta .
$$

$$
\left\{ \begin{array} { l l } { \xi ^ { \prime \prime } = x ^ { \prime \prime } + \Xi , } \\ { \eta ^ { \prime \prime } = y ^ { \prime \prime } + \mathrm { H } , } \\ { \xi ^ { \prime \prime } = z ^ { \prime \prime } + \mathrm { z } . } \end{array} \right.
$$

In polar coordinates these equations are

$$
\left\{ \begin{array} { l l } { \rho \cos \beta \cos \lambda = r \cos b \cos l + \mathrm { P } \cos \mathrm { B } \cos \Lambda , } \\ { \rho \cos \beta \sin \lambda = r \cos b \sin l + \mathrm { P } \cos \mathrm { B } \sin \Lambda , } \\ { \rho \sin \beta \qquad = r \sin b \qquad + \mathrm { P } \sin \mathrm { B } . } \end{array} \right.
$$

From these equations $\lambda$ and $\beta$ can be found; but this system may be transformed into one which is more convenient by multiplying the first equation by cos $\boldsymbol { \Lambda }$ ,the second by sin $\pmb { \Lambda }$ ，and adding the products；and then multiplying the first by - sin $\Delta$ and the second by cos $\boldsymbol { \Lambda }$ ,and adding the products. The results are

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \rho \cos \beta \cos \left( \mathrm { \tt A } - \mathrm { \tt A } \right) = r \cos b \cos \left( l - \mathrm { \tt A } \right) + \mathrm { P } \cos \mathrm { \tt B } , } \\ { \rho \cos \beta \sin \left( \mathrm { \tt A } - \mathrm { \tt A } \right) = r \cos b \sin \left( l - \mathrm { \tt A } \right) , } \\ { \rho \sin \beta \ ~ } & { \quad \mathrm + \mathrm { P } \sin \mathrm { \tt B } . } \end{array} \right. } \end{array}
$$

These equations give the geocentric distance， longitude，and latitude, $\rho , \lambda ,$ and $\beta$ ·

106.Transformation to Geocentric Equatorial Coordinates. Let $\epsilon$ represent the inclination of the plane of the ecliptic to the plane of the equator.Let $\xi ^ { \prime \prime } , \eta ^ { \prime \prime }$ ，and $\xi ^ { \prime \prime }$ be the geocentric coordinates of the body referred to the ecliptic system with the $\pmb { x }$ -axis directed toward the vernal equinox. Then, the equatorial system can be obtained by rotating the ecliptic system around the $\pmb { x }$ -axis in the negative direction through the angle $\epsilon _ { \mathfrak { g } }$ the relations between the coordinates in the two systems being

$$
\left\{ \begin{array} { l } { { \xi ^ { \prime \prime \prime } = \xi ^ { \prime \prime } , } } \\ { { \eta ^ { \prime \prime \prime } = \eta ^ { \prime \prime } \cos \epsilon - \xi ^ { \prime \prime } \sin \epsilon , } } \\ { { \xi ^ { \prime \prime \prime } = \eta ^ { \prime \prime } \sin \epsilon + \xi ^ { \prime \prime } \cos \epsilon ; } } \end{array} \right.
$$

or,in polar coordinates,

$$
\left\{ \begin{array} { l l } { \cos \delta \cos \alpha = \cos \beta \cos \lambda , } \\ { \cos \delta \sin \alpha = \cos \beta \sin \lambda \cos \epsilon - \sin \beta \sin \epsilon , } \\ { \sin \delta } \end{array} \right.
$$

In order to solve these equations conveniently for $\pmb { \delta }$ and $\pmb { \alpha }$ the auxiliaries $\pmb { n }$ and $\pmb { N }$ will be introduced by the equations

$$
\left\{ \begin{array} { l l } { n \sin N = \sin \beta , } \\ { n \cos N = \cos \beta \sin \lambda , } \end{array} \right.
$$

in which $\pmb { n }$ is a positive quantity. Then equations (86) become

whence

$$
\left\{ \begin{array} { l } { { \cos \delta \cos \alpha = \cos \beta \cos \lambda , } } \\ { { \cos \delta \sin \alpha = n \cos ( N + \epsilon ) , } } \\ { { \sin \delta } } \end{array} \right.
$$

$$
\left\{ \begin{array} { l l } { \displaystyle n \sin N = \sin \beta , } \\ { \displaystyle n \cos N = \cos \beta \sin \lambda , } \\ { \displaystyle \tan \alpha = \frac { \cos \left( N + \epsilon \right) \tan \lambda } { \cos N } , } \\ { \displaystyle \tan \delta = \tan \left( N + \epsilon \right) \sin \alpha . } \end{array} \right.
$$

These equations,together with the first of (86),which is used in determining the quadrant in which $_ \alpha$ lies,give $_ { \pmb { \alpha } }$ and $\pmb { \delta }$ without ambiguity when $\lambda$ and $\beta$ are known.

If $_ \alpha$ and $\pmb { \delta }$ are given and $\lambda$ and $\beta$ are required,the equations from which they can be computed are found by interchanging $\pmb { \alpha }$ and $\pmb { \delta }$ with $\lambda$ and $\beta$ ,and changing $\epsilon$ to - ein (88). They are\*

$$
\left\{ \begin{array} { l } { { m \sin M = \sin \delta , } } \\ { { m \cos M = \cos \delta \sin \alpha , } } \\ { { \phantom { m } \tan \lambda = { \frac { \cos \left( M - \epsilon \right) \tan \alpha } { \cos M } } , } } \\ { { \phantom { m } \tan \beta = \tan \left( M - \epsilon \right) \sin \lambda . } } \end{array} \right.
$$

107.Direct Computation of the Geocentric Equatorial Coordinates. The geocentric equatorial coordinates, $_ \alpha$ and $\delta$ ，can be found directly from the elements, $_ i$ and $\boldsymbol { \Omega }$ ，and the argument of the latitude $\textbf { \em u }$ ，without frst finding the ecliptic coordinates, $\pmb { \lambda }$ and $\beta$

Ina system of axes with the $\pmb { x }$ -axis directed to the node and the $\pmb { y }$ -axis in the plane of the ecliptic,the equations for the heliocentric coordinates are

$$
\left\{ \begin{array} { l l } { x ^ { \prime } = r \cos u , } \\ { y ^ { \prime } = r \sin u \cos i , } \\ { z ^ { \prime } = r \sin u \sin i . } \end{array} \right.
$$

$* _ { m }$ and $\pmb { M }$ are new auxiliaries,not being related to any of the quantitieg which these letters previously have represented.

If the system is rotated around the ${ \pmb z }$ -axis until the $\pmb { x } \cdot$ -axis is directed toward the vernal equinox, the coordinates are

$$
\left\{ \begin{array} { l l } { { x ^ { \prime \prime } = x ^ { \prime } \cos \ \Omega - y ^ { \prime } \sin \ \Omega , } } \\ { { y ^ { \prime \prime } = x ^ { \prime } \sin \ \Omega + y ^ { \prime } \cos \ \Omega , } } \\ { { z ^ { \prime \prime } = z ^ { \prime } ; } } \end{array} \right.
$$

or,

$$
\begin{array} { r l } & { \left\{ { x ^ { \prime \prime } = r ( \cos u \cos \theta - \sin u \cos i \sin \theta ) , } \right. } \\ & { \left\{ { y ^ { \prime \prime } = r ( \cos u \sin \theta + \sin u \cos i \cos \theta ) , } \right. } \\ & { \left. { z ^ { \prime \prime } = r \sin u \sin i . } \right. } \end{array}
$$

lf the system is rotated now around the $\pmb { x }$ -axis through the angle $- \ \epsilon ,$ the coordinates become

$$
\left\{ \begin{array} { l l } { { x ^ { \prime \prime \prime } = x ^ { \prime \prime } , } } \\ { { y ^ { \prime \prime \prime } = y ^ { \prime \prime } \cos \epsilon - z ^ { \prime \prime } \sin \epsilon , } } \\ { { z ^ { \prime \prime \prime } = y ^ { \prime \prime } \sin \epsilon + z ^ { \prime \prime } \cos \epsilon ; } } \end{array} \right.
$$

or, in polar coordinates,

$$
\begin{array} { r l } & { \int _ { } ^ { x ^ { \prime \prime \prime } } = r \{ \cos u \cos \vartheta - \sin u \cos i \sin \vartheta \} , } \\ & { \left\{ y ^ { \prime \prime \prime } = r \{ \left( \cos u \sin \vartheta + \sin u \cos i \cos \vartheta \right) \cos \epsilon \right. } \\ & { \qquad - \sin u \sin i \sin \epsilon \} , } \\ & { \left\{ z ^ { \prime \prime \prime } = r \{ \left( \cos u \sin \vartheta + \sin u \cos i \cos \vartheta \right) \sin \epsilon \right. } \\ & { \qquad + \left. \sin u \sin i \cos \epsilon \right\} . } \end{array}
$$

In order to facilitate the computation Gauss introduced the new auxiliaries $A , a , B , b , C$ and $c$ by the equations

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \sin a \sin A = \cos \Omega , } \\ { \sin a \cos A = - \sin \Omega \cos i , } \\ { \sin b \sin B = \sin \Omega \cos e , } \\ { \sin b \cos B = \cos \Omega \cos i \cos e - \sin i \sin \epsilon , } \\ { \sin c \sin C = \sin \Omega \sin \epsilon , } \\ { \sin c \cos C = \cos \Omega \cos i \sin \epsilon + \sin i \cos \epsilon . } \end{array} \right. \quad \mathrm { s i n ~ } a > 0 , } \end{array}
$$

These constants depend upon the elements alone,so they need be computed but once for a given orbit. They are of particular advantage when the coordinates are to be computed for a large number of epochs,as in constructing an ephemeris. When these constants are substituted in (91),these equations for the heliocentric coordinates take the simple form

$$
\left\{ { \begin{array} { l } { x ^ { \prime \prime \prime } = r \sin a \sin { ( A + \ u ) } , } \\ { y ^ { \prime \prime \prime } = r \sin b \sin { ( B + u ) } , } \\ { z ^ { \prime \prime \prime } = r \sin c \sin { ( C + u ) } . } \end{array} } \right.
$$

from which $x ^ { \prime \prime \prime } , y ^ { \prime \prime \prime }$ ,and $z ^ { \prime \prime \prime }$ can be found.

Then finally, the geocentric equatorial coordinates are defined by

$$
\left\{ \begin{array} { l l } { \rho \cos { \delta } \cos \alpha = x ^ { \prime \prime \prime } + X ^ { \prime } , } \\ { \rho \cos { \delta } \sin \alpha = y ^ { \prime \prime \prime } + Y ^ { \prime } , } \\ { \rho \sin { \delta } } & { = z ^ { \prime \prime \prime } + Z ^ { \prime } , } \end{array} \right.
$$

where $X ^ { \prime } , Y ^ { \prime }$ ,and $\mathbf { \delta } Z ^ { \prime }$ are the rectangular geocentric coordinates of the sun referred to the equatorial system. They are given in the Nautical Almanac for every day in the year,and,therefore, these equations define $\rho , \alpha ,$ and $\delta$

This completes the theory of the determination of the heliocentric and geocentric coordinates of a body, moving in any orbit, when either the ecliptic or the equatorial system is used.

# XVI. PROBLEMS.

1. Interpret the angle $\pmb { N }$ ,equation (87)，geometrically and show that $\pmb { n }$ is simply a factor of proportionality.

2. Suppose the ascending node is taken always as that one which is les than $1 8 0 ^ { \circ }$ ，and that the inclination varies from $- 9 0 ^ { \circ }$ to $+ ~ 9 0 ^ { \circ }$ ； discuss the changes which will be made in the equations (78),·.,(93),and in particular, write the definitions of the Gaussian constants $^ { a }$ ,A，·.··, $c$ for this method of defining the elements.

3.Interpret the Gaussian constan:, defined by (92)， geometrically.

# HISTORICAL SKETCH AND BIBLIOGRAPHY.

The Problem of Two Bodies for spheres of finite size wag first solved by Newton about 1685,and is given in the Principia,Book 1., Section 11．The demonstration is geometrical. The methods of the Calculus were cultivated with ardor in continental Europe at the beginning of the 18th century,but Newton's system of Mechanics did not find immediate acceptance;indeed, the French clung to the vortex theory of Descartes (1596-165O) until Voltaire,after his visit to London 1727，vigorously supported the Newtonian theory，1728-1738. This，with the fact that the English continued to employ the geometrical methods of the Principia,delayed the analytical solution of the problem．It was probably accomplished by Daniel Bernouilli in the memoir for which he received the prize from the French Academy in 1734,and it was certainly solved in detail by Euler in 1744 in his Theoria motuum planetarum et cometarum. Since that time the modifications have been chiefly in the choice of variables in which the problem has been expresed.

The solution of Kepler's equation naturally was first made by Kepier himself. The next was by Newton in the Principia. From a graphical construction involving the cycloid he was able to find very easily the approximate solution for the eccentric anomaly.A very large number of analytical and graphical solutions have been discovered, nearly every prominent mathematician from Newton until the middle of the last century having given the subject more or less attention．A bibliography containing references to 123 papers on Kepler's equation is given in the Bulletin Astronomique,Jan.1900, and even this extended list is incomplete.

The transformations of coordinates involve merely the solutions of spherical triangles,the treatment ofwhich ina perfectly general form the mathematical world owes to Gauss (1777-1855),and which was introduced into American Trigonometries by Chauvenet.

The Problem of Two Bodies is treated in every work on Analytical Mechanics. The reader will do well to consult further Tisserand's Méc. Cel., vol. 1., chapters VI. and vII.

# CHAPTER VI.

# THE DETERMINATION OF ORBITS.

108.General Consideration. In discussing the problem of two bodies [Arts.86--88] it was shown how the constants of integration which arise when the differential equations are solved can be determined in terms of the original values of the coordinates and of the components of velocity；and then it was shown how the elements of the conic section orbit can be determined in terms of these constants. Consequently,it is natural to seek to determine the position and components of the observed body at some epoch. The difficulty arises from the fact that the observations, which are made from the moving earth,give only the direction of the object as seen by the observer,and furnish no direct information respecting its distance. An observation of apparent position simply determines the fact that the body is somewhere on one half of a defined line passing through the observer. The position of the body in space is therefore not given，and,of course，its components of velocity are not determined. It becomes necessary on this account to secure additional observations at other times. In the interval of time before the second observation is made the earth will have moved and the observed body will have gone to another place in its orbit. The second observation simply determines another line on which the body is located at another date. It is clear that the problem of finding the position of the body and the elements of its orbit from such data presents some difficulties.

The first question to settle is naturally the number of observations which are necessary in order that it shall be possible to determine the elements of the orbit. Since an orbit is defined by six elements,it follows that six independent quantities must be given by the observations in order that the elements may be determined. A single complete observation gives two quantities, the angular coordinates of the body. Therefore three complete observations are just sufficient,so far as these considerations are concerned, to define its orbit. It is at least certain that no smaller number will suffice. If the observed body is a comet whose orbit is a parabola, the eccentricity is unity and only five elements are to be found. In this case two complete observations and one observation giving one of the two angular coordinates are enough.

109.Intermediate Elements. The apparent positions of the observed body are usually obtained by measuring its angular distances and directions from neighboring fixed stars. Since the stars are catalogued in right ascension and declination the results come out in these coordinates,but they can,of course, be changed to the ecliptic system,or any other,if it is desired.

Suppose the observations are made at the times $t _ { 1 } , \ t _ { 2 } ,$ and $\pmb { t _ { 3 } }$ ， and let the corresponding coordinates be denoted by their usual symbols having the subscripts 1,2,and 3 respectively. The right ascensions and declinations are functions of the elements of the orbit and the dates of observation. These relations may be represented by

$$
\begin{array} { r } { \left\{ \alpha _ { 1 } = \varphi ( \otimes , ~ i , ~ \omega , ~ a , ~ e , ~ T ; ~ t _ { 1 } ) , \right. } \\ { \alpha _ { 2 } = \varphi ( \otimes , ~ i , ~ \omega , ~ a , ~ e , ~ T ; ~ t _ { 2 } ) , } \\ { \alpha _ { 3 } = \varphi ( \otimes , ~ i , ~ \omega , ~ a , ~ e , ~ T ; ~ t _ { 3 } ) , } \\ { \delta _ { 1 } = \psi ( \otimes , ~ i , ~ \omega , ~ a , ~ e , ~ T ; ~ t _ { 1 } ) , } \\ { \delta _ { 2 } = \psi ( \otimes , ~ i , ~ \omega , ~ a , ~ e , ~ T ; ~ t _ { 2 } ) , } \\ { \delta _ { 3 } = \psi ( \otimes , ~ i , ~ \omega , ~ a , ~ e , ~ T ; ~ t _ { 3 } ) . } \end{array}
$$

The problem consists in solving these six equations for the six unknown elements. The functions $\varphi$ and $\psi$ are highly transcendental and involve the elements in a very complicated fashion. In the case of an ellipse the position in the orbit is found by passing through Kepler's equation,in the hyperbola the process is similar, and in the parabola a cubic equation must be solved;and in all three cases the coordinates with respect to the earth are obtained by a number of trigonometrical transformations. Hence it is clear that there is no direct solution of equations (1) by ordinary processes.

Although the ultimate object is to determine the elements of the orbit,the problem of finding other quantities which define the elements may be treated first. These quantities may be considered as being intermediate elements. It has been remarked that if the coordinates and the components of velocity are known at any epoch,the elements can be found. Suppose it is desired to find the polar coordinates and their derivatives,which deter.

mine uniquely the rectangular coordinates and their derivatives, at the time of the second observation $t _ { 2 }$ ，The equations corresponding to (1） become for this problem

$$
\left\{ \begin{array} { l } { \alpha _ { 1 } = f \left( \alpha _ { 2 } , \ \hat { \sigma } _ { 2 } , \ \rho _ { 2 } , \ \alpha _ { 2 } ^ { \prime } , \ \hat { \sigma } _ { 2 } ^ { \prime } , \ \rho _ { 2 } ^ { \prime } ; \ t _ { 1 } , \ t _ { 2 } \right) , } \\ { \alpha _ { 2 } = \alpha _ { 2 } , } \\ { \alpha _ { 3 } = f \left( \alpha _ { 2 } , \ \hat { \sigma } _ { 2 } , \ \rho _ { 2 } , \ \alpha _ { 2 } ^ { \prime } , \ \hat { \sigma } _ { 2 } ^ { \prime } , \ \rho _ { 2 } ^ { \prime } ; \ t _ { 2 } , \ t _ { 3 } \right) , } \\ { \hat { \sigma } _ { 1 } = g ( \alpha _ { 2 } , \ \hat { \sigma } _ { 2 } , \ \rho _ { 2 } , \ \alpha _ { 2 } ^ { \prime } , \ \hat { \sigma } _ { 2 } ^ { \prime } , \ \rho _ { 2 } ^ { \prime } ; \ t _ { 1 } , \ t _ { 2 } ) , } \\ { \hat { \sigma } _ { 2 } = \hat { \sigma } _ { 2 } , } \\ { \delta _ { 3 } = g ( \alpha _ { 2 } , \ \hat { \sigma } _ { 2 } , \ \rho _ { 2 } , \ \alpha _ { 2 } ^ { \prime } , \ \hat { \sigma } _ { 2 } ^ { \prime } , \ \rho _ { 2 } ^ { \prime } ; \ t _ { 2 } , \ t _ { 3 } ) , } \end{array} \right.
$$

where

$$
{ \alpha _ { 2 } } ^ { \prime } = \frac { d \alpha } { d t } , \qquad \hat { \alpha } _ { 2 } ^ { \prime } = \frac { d \delta } { d t } , \qquad { \rho _ { 2 } } ^ { \prime } = \frac { d \rho } { d t } \quad \mathrm { a t } \quad t = t _ { 2 } .
$$

Since $\pmb { \alpha _ { 2 } }$ and $\pmb { \delta _ { 2 } }$ are observed quantities only the first,third,fourth, and sixth equations are to be solved for the four unknowns $\rho _ { 2 } , \alpha _ { 2 } ^ { \prime }$ ， ${ \pmb \delta _ { 2 } } ^ { \prime }$ ，and ${ \pmb \rho } _ { 2 } ^ { \prime }$ .The problem is therefore reduced to the solution of four simultaneous equations,and they are moreover much simpler than (1). These equations can be put in a manageable form,and this is,in fact,one of the methods of treating the problem.It was first developed and applied to the actual determination of orbits by Laplace in 1780,and it has been somewhat extended and modified as to details by many later writers.

As another set of intermediate elements the three coordinates at two epochs may be taken. Suppose the times $t _ { 1 }$ and $t _ { 3 }$ are chosen for this purpose. Then the fundamental equations corresponding to (1) can be written in the form

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \alpha _ { 1 } = \alpha _ { 1 } , } \\ { \alpha _ { 2 } = F ( \alpha _ { 1 } , ~ \delta _ { 1 } , ~ \rho _ { 1 } , ~ \alpha _ { 3 } , ~ \delta _ { 3 } , ~ \rho _ { 3 } ; ~ t _ { 1 } , ~ t _ { 2 } , ~ t _ { 3 } ) , } \\ { \alpha _ { 3 } = \alpha _ { 3 } , } \\ { \delta _ { 1 } = \delta _ { 1 } , } \\ { \delta _ { 2 } = G ( \alpha _ { 1 } , ~ \delta _ { 1 } , ~ \rho _ { 1 } , ~ \alpha _ { 3 } , ~ \delta _ { 3 } , ~ \rho _ { 3 } ; ~ t _ { 1 } , ~ t _ { 2 } , ~ t _ { 3 } ) , } \\ { \delta _ { 3 } = \delta _ { 3 } . } \end{array} \right. } \end{array}
$$

In this case the equations are reduced to two in the two unknowns $\pmb { \rho _ { 1 } }$ and $\pmb { \rho _ { 3 } }$ ，and they also can be solved. This is the line of attack on the problem laid out by Lagrange in 1778,taken up independently and carried out differently by Gauss in 1801,and followed more or less closely by many later writers. In spite of the