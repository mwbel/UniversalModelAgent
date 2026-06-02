higher approximations.In l846 de Pontécoulant and Lubbock published their complete results by taking time as the independent variable. Hansen's theory (Sections 10.7-1O.9), the Fundamenta Nova Investigationis Orbitae Verae Quam Luna Perlustrat, was published in l838,Darlegung der theoretischen Berechnung der in der Mondtafeln angewandten Storungen with numerical results in 1862 and 1864, Uber die Darstellung der graden Aufsteigung und Ableitung des Mondes in Funktion der Lange in der Bahn und der Knotenlinge in 1874,and the Tables de la Lune in 1857. Poisson's memoir on the variation of constants appeared in 1835.Adams pointed out in l853 that Laplace's theoretical value of the secular acceleration was in error by about one-half. Then Delaunay's theory came out in 1867 (Section 9.2).Airy's numerical theory in l886 for numerically verifying Delaunay’s theory was a failure. Weiler in l872， Neisson-Nevill in 1877,and Oppolzer in 1887 published their own general methods (Section 10.13).Gyldén in 1886,Brendel in 1925,and some others published their own theories (Sections 10.18,10.19,10.22).

It was Hill (1878,l886) who initiated the idea of a periodic orbit for an intermediary orbit for the motion of the moon.Hill, by taking Euler's idea of expanding in powers of the eccentricity and inclination, computed with high accuracy the inequalities that are independent of the eccentricity and inclination.Adams independently proposed a similar idea for the motion of the lunar node. The theory of Hill and Adams was completed by Brown.Cowell compared Brown's theory with observations in 1903-l905.This was the opening of the present era in determining the motion of the perigee and node with the desired accuracy by using the infinite determinant named after Hill and an infinite number of linear equations (Brown,1895,1896,1908a,1915；Darwin,1916; Plummer, 1918; Moritz,1918, 1921).

Let $X , Y$ be the rectangular coordinates of the moon rotating about the $z$ -axis with constant angular velocity $\scriptstyle { \pmb { n } } ^ { \prime }$ around the earth's center. Then the equations of motion of the moon with the coordinates $X , Y , Z$ are

$$
\begin{array} { l } { { \displaystyle { \frac { d ^ { 2 } X } { d t ^ { 2 } } } - 2 n ^ { \prime } \frac { d Y } { d t } = \frac { \partial F } { \partial X } } , } \\ { { \displaystyle { \frac { d ^ { 2 } Y } { d t ^ { 2 } } } + 2 n ^ { \prime } \frac { d X } { d t } = \frac { \partial F } { \partial Y } } , } \end{array}
$$

$$
\frac { d ^ { 2 } Z } { d t ^ { 2 } } = \frac { \partial F } { \partial Z } ,
$$

$$
F = { \textstyle \frac { 1 } { 2 } } n ^ { \prime 2 } ( X ^ { 2 } + Y ^ { 2 } ) + F ^ { \prime } ,
$$

where $F ^ { \prime }$ is the force function of the perturbation, $\scriptstyle { \pmb { n } } ^ { \prime }$ is the mean motion of the sun around the earth,and the $X .$ -axis is directed to the mean position of the sun.Write

$$
u = X + { \sqrt { - 1 } } Y , \qquad s = X - { \sqrt { - 1 } } Y ;
$$

then the equations of motion are transformed to

$$
\begin{array} { c } { { \displaystyle \frac { d ^ { 2 } u } { d t ^ { 2 } } + 2 n { ' } \sqrt { - 1 } \frac { d u } { d t } = 2 \frac { \partial F } { \partial s } , } } \\ { { \displaystyle \frac { d ^ { 2 } s } { d t ^ { 2 } } - 2 n { ' } \sqrt { - 1 } \frac { d s } { d t } = 2 \frac { \partial F } { \partial u } , } } \\ { { \displaystyle X ^ { 2 } + Y ^ { 2 } = u s , \qquad r ^ { 2 } = X ^ { 2 } + Y ^ { 2 } + Z ^ { 2 } = u s + Z ^ { 2 } . } } \end{array}
$$

Take instead of $\pmb { t }$ the independent variable $\pmb { \zeta } _ { i }$ defined by

$$
\zeta = \exp { \{ \sqrt { - 1 } ( n - n ^ { \prime } ) ( t - t _ { 0 } ) \} } ,
$$

where $\pmb { n }$ and $t _ { 0 }$ are as yet undetermined constants. Write

$$
\nu = n - n ^ { \prime } , ~ D = \zeta \frac { d } { d \zeta } , ~ \mathbf { m } = \frac { n ^ { \prime } } { n - n ^ { \prime } } = \frac { n ^ { \prime } } { \nu } ;
$$

then we have

$$
\frac { d } { d t } = \nu \sqrt { - 1 } \zeta \frac { d } { d \zeta } = \nu \sqrt { - 1 } D , \frac { d ^ { 2 } } { d t ^ { 2 } } = - \nu ^ { 2 } D ^ { 2 } .
$$

The equations of motion are now

$$
\begin{array} { r } { D ^ { 2 } u + 2 \mathbf { m } D u = - \frac { 2 } { \nu ^ { 2 } } \frac { \partial F } { \partial s } , } \\ { D ^ { 2 } s - 2 \mathbf { m } D s = - \frac { 2 } { \nu ^ { 2 } } \frac { \partial F } { \partial u } , } \end{array}
$$

where

$$
F ^ { \prime } = \frac { m _ { E } + m _ { M } } { r } + \frac { m ^ { \prime } } { \Delta } - m ^ { \prime } \frac { x x ^ { \prime } + y y ^ { \prime } + z z ^ { \prime } } { r ^ { \prime 3 } } ,
$$

the units being chosen so that the gravitational constant is equal to unity; $m _ { E } , m _ { M }$ and $\mathbf { \Omega } _ { m ^ { \prime } }$ being the mass of the earth, moon, and sun, respectively. Let $\pmb { x } , \pmb { y } , \pmb { z } , \pmb { r }$ be the coordinates of the moon referred to the space-fixed frame with the earth as origin,and $\pmb { x } ^ { \prime } , \pmb { y } ^ { \prime } , \pmb { z } ^ { \prime } , \pmb { r } ^ { \prime }$ be the coordinates of the sun referred to the same frame. Let $s$ be the cosine of the angle between the radius vectors from the earth to the moon and to the sun; then,

$$
\begin{array} { c } { { x x ^ { \prime } + y y ^ { \prime } + z z ^ { \prime } = r r ^ { \prime } S , } } \\ { { \Delta ^ { 2 } = r ^ { 2 } + r ^ { \prime 2 } - 2 r r ^ { \prime } S , ~ \mu = m _ { M } + m _ { E } . } } \end{array}
$$

Dropping the unnecessary term $m ^ { \prime } / r ,$ we write the force function $\scriptstyle { F ^ { \prime } }$ as

$$
{ \begin{array} { r l } & { F ^ { \prime } = { \frac { \mu } { r } } + { \frac { m ^ { \prime } } { r ^ { \prime } } } \left[ { \frac { r ^ { 2 } } { r ^ { \prime 2 } } } \left( { \frac { 3 } { 2 } } S ^ { 2 } - { \frac { 1 } { 2 } } \right) + { \frac { r ^ { 3 } } { r ^ { \prime 3 } } } \left( { \frac { 5 } { 2 } } S ^ { 3 } - { \frac { 3 } { 2 } } S \right) + \cdots \right] } \\ & { ~ = { \frac { \mu } { r } } + { \frac { m ^ { \prime } } { r ^ { \prime 3 } } } \left( { \frac { 3 } { 2 } } r ^ { 2 } S ^ { 2 } - { \frac { 1 } { 2 } } r ^ { 2 } \right) + { \frac { m ^ { \prime } } { r ^ { \prime 3 } } } { \frac { 1 } { r ^ { \prime } } } \left( { \frac { 5 } { 2 } } r ^ { 3 } S ^ { 3 } - { \frac { 3 } { 2 } } r S r ^ { 2 } \right) + \cdots . } \end{array} }
$$

Put $m ^ { \prime } + \mu \approx m ^ { \prime } = n ^ { \prime 2 } a ^ { \prime 3 }$ ， $\kappa = \mu / \nu ^ { 2 }$ ; then,

$$
\frac { 2 } { \nu ^ { 2 } } F = \frac { 2 \kappa } { r } + \frac { 3 } { 4 } \mathbf { m } ^ { 2 } ( u + s ) ^ { 2 } - \mathbf { m } ^ { 2 } z ^ { 2 } + \Omega ,
$$

$$
\begin{array} { r } { \Omega = { 3 } { \bf m } ^ { 2 } \Big [ \frac { a ^ { \prime 3 } } { r ^ { \prime 3 } } r ^ { 2 } S ^ { 2 } - \frac { 1 } { 4 } ( u + s ) ^ { 2 } \Big ] - { \bf m } ^ { 2 } ( u s + z ^ { 2 } ) \Big [ \frac { a ^ { \prime 3 } } { r ^ { \prime 3 } } - 1 \Big ] \qquad } \\ { + \frac { { \bf m } ^ { 2 } } { a ^ { \prime } } \frac { a ^ { \prime 4 } } { r ^ { \prime 4 } } \left[ 5 r ^ { 3 } S ^ { 3 } - 3 r S ( u s + z ^ { 2 } ) \right] + \cdot \cdot \cdot } \end{array}
$$

$$
\mathbf { \Omega } = \Omega _ { 2 } + \Omega _ { 3 } + \cdots ,
$$

where $\Omega _ { p }$ is homogeneous of degree $\pmb { \mathscr { p } }$ with respect to $u , s ,$ and $_ z$ ,and of degree $2 - \pmb { \mathscr { p } }$ with respect to $\pmb { a } ^ { \prime }$ Then Hil's fundamental equations of motion take the form

$$
\begin{array} { r } { D ^ { 2 } u + 2 \mathbf { m } D u + \displaystyle \frac { 3 } { 2 } \mathbf { m } ^ { 2 } ( u + s ) - \frac { \kappa u } { r ^ { 3 } } = - \frac { \partial \Omega } { \partial s } \mathrm { , } } \\ { D ^ { 2 } s - 2 \mathbf { m } D s + \displaystyle \frac { 3 } { 2 } \mathbf { m } ^ { 2 } ( u + s ) - \frac { \kappa s } { r ^ { 3 } } = - \frac { \partial \Omega } { \partial u } \mathrm { , } } \\ { D ^ { 2 } z - \mathbf { m } ^ { 2 } z - \frac { \kappa z } { r ^ { 3 } } = - \frac { 1 } { 2 } \frac { \partial \Omega } { \partial z } \mathrm { . } } \end{array}
$$

Multiply the first equation of (3) by $\pmb { \mathscr { s } }$ and the second equation by $- \pmb { u } ,$ and add. Multiply the first equation of (3) by ${ \mathfrak { s } } .$ ，the second equation by $u _ { \mathrm { { ; } } }$ ,and the equation (4)by $2 z .$ ,and add. Then we obtain

$$
D ( u D s - s D u - 2 { \bf m } u s ) + \frac { 3 } { 2 } { \bf m } ^ { 2 } ( u ^ { 2 } - s ^ { 2 } ) = s \frac { \partial \Omega } { \partial s } - u \frac { \partial \Omega } { \partial u } ,
$$

$$
\begin{array} { c } { { s D ^ { 2 } u + u D ^ { 2 } s + 2 z D ^ { 2 } z - 2 { \bf m } ( u D s - s D u ) } } \\ { { { } } } \\ { { { } + \displaystyle { \frac { 3 } { 2 } { \bf m } ^ { 2 } ( u + s ) ^ { 2 } - 2 { \bf m } ^ { 2 } z ^ { 2 } - \frac { 2 \kappa } { r } } } } \\ { { { } } } \\ { { { } = \displaystyle { - \left( s \frac { \partial \Omega } { \partial s } + u \frac { \partial \Omega } { \partial u } + z \frac { \partial \Omega } { \partial z } \right) = - \sum _ { p = 2 } ^ { \infty } p \Omega _ { p } } } } \end{array}
$$

Multiply the two equations of (3) by $_ { D u }$ and $D s _ { ; }$ ，respectively, and multiply (5） by $2 D z ,$ and add the resulting three equations; then

$$
\begin{array} { c } { { { \cal D } u { \bf \cdot } { \cal D } s + ( { \cal D } z ) ^ { 2 } + \displaystyle \frac { 3 } { 4 } { \bf m } ^ { 2 } ( u + s ) ^ { 2 } - { \bf m } ^ { 2 } z ^ { 2 } + \displaystyle \frac { 2 \kappa } { r } \biggr ] } } \\ { { { \mathrm { } } } } \\ { { { \mathrm { } } = - \displaystyle \left[ \frac { \partial \Omega } { \partial s } { \cal D } s + \frac { \partial \Omega } { \partial u } { \cal D } u + \frac { \partial \Omega } { \partial z } { \cal D } z \right] } } \end{array}
$$

Since $\Omega$ is a function of $u , s , z ,$ and $\boldsymbol { \zeta }$ we have

$$
D \Omega = \frac { \partial \Omega } { \partial u } D u + \frac { \partial \Omega } { \partial s } D s + \frac { \partial \Omega } { \partial z } D z + \frac { \partial \Omega } { \partial \zeta } D \zeta ,
$$

where

$$
\frac { \partial \Omega } { \partial \zeta } D \zeta = \zeta \frac { \partial \Omega } { \partial \zeta } = D _ { t } \Omega = D ( D ^ { - 1 } D _ { t } \Omega ) ,
$$

$D _ { t }$ denoting the operation operating only on that part of $\Omega$ which contains $t$ or $\zeta$ explicitly.After substituting this in the above relation we integrate the result; then,

$$
) u \cdot D s + ( D z ) ^ { 2 } + { \frac { 3 } { 4 } } { \bf m } ^ { 2 } ( u + s ) ^ { 2 } - { \bf m } ^ { 2 } z ^ { 2 } + { \frac { 2 \kappa } { r } } = C - \Omega + D ^ { - 1 } ( D _ { 0 }
$$

where $c$ is an integration constant. Add this equation to (6); then

$$
\begin{array} { r l r } {  { \boldsymbol { \mathrm { \Lambda } } ^ { 2 } ( \boldsymbol { u } \boldsymbol { s } + \boldsymbol { z } ^ { 2 } ) - D \boldsymbol { u } \cdot D \boldsymbol { s } - ( D \boldsymbol { z } ) ^ { 2 } - 2 \mathbf { m } ( \boldsymbol { u } D \boldsymbol { s } - \boldsymbol { s } D \boldsymbol { u } ) } } \\ & { } & { + \mathrm { \Lambda } _ { 4 } ^ { 9 } \mathbf { m } ^ { 2 } ( \boldsymbol { u } + \boldsymbol { s } ) ^ { 2 } - 3 \mathbf { m } ^ { 2 } \boldsymbol { z } ^ { 2 } } \\ & { } & \\ & { } & { = C - \displaystyle \sum _ { p = 2 } ^ { \infty } ( \boldsymbol { \dot { p } } + 1 ) \Omega _ { p } + D ^ { - 1 } ( D _ { t } \Omega ) . } \end{array}
$$

Now, (4),(5),and (7) constitute the required equations.

# II.2INTERMEDIARY ORBIT

We neglect the solar eccentricity $\scriptstyle { e ^ { \prime } }$ ， the solar parallax $1 / a ^ { \prime }$ and the latitude $_ z$ in (4), (5), (7); then,

$$
r ^ { \prime } = a ^ { \prime } , \qquad r S = X ,
$$

and hence

$$
\Omega = 0 .
$$

The equations (5) and (7) are now

$$
\begin{array} { r } { D ^ { 2 } ( u s ) - D u { \cdot } D s - 2 \mathbf { m } ( u D s - s D u ) + \frac { 9 } { 4 } \mathbf { m } ^ { 2 } ( u + s ) ^ { 2 } = C , } \\ { D ( u D s - s D u - 2 \mathbf { m } u s ) + \frac { 3 } { 2 } \mathbf { m } ^ { 2 } ( u ^ { 2 } - s ^ { 2 } ) = 0 . } \end{array}
$$

These equations (8) contain the ratio m and the moon's orbital eccentricity. We consider such a particular solution of these two equations (8) that corresponds to $\epsilon = 0$ ，and call it Hill's intermediary orbit or $H i l l ^ { 3 } s$ variational curve. It is obtained by neglecting $e ^ { \prime }$ $, \ a / a ^ { \prime } , \ e ,$ and $\gamma _ { : }$ ，where $\gamma$ denotes the inclination of the moon's orbit. Since the two equations are of the second order, the solution should have four arbitrary constants. One of these is the constant $C .$ As we have taken $e = 0$ ，one of the four arbitrary constants drops,and another corresponding to the longitude of the perigee drops at the same time.Thus two arbitrary constants drop. If we take $\mathbf { m }$ instead of $C _ { z }$ ，we have two arbitrary constants m and a, of which the latter corresponds to the semimajor axis of the moon's orbit in the intermediary orbit.Thus Hill's intermediary orbit is a modified Keplerian circular orbit, so to speak, in the rotating coordinate system.The period for describing a complete revolution of the intermediary orbit is $2 \pi / ( n - n ^ { \prime } )$ ,about $1 4 \frac { 3 } { 4 }$ days.Hence the coordinates of the moon can be expanded in Fourier series with multiples of the argument $( n - n ^ { \prime } ) t$ ； that is， the intermediary orbit is a particular solution which can be expanded in Fourier series of $( n - n ^ { \prime } ) t$

Suppose that the orbit is symmetrical with regard to both the $X .$ -axis and the $\pmb { Y } .$ -axis,and is closed, that is,periodic.Then the solution will be of the form

$$
X = \sum _ { i = 0 } ^ { \infty } A _ { 2 i + 1 } \cos { ( 2 i + 1 ) } \xi , \qquad Y = \sum _ { i = 0 } ^ { \infty } A _ { 2 i + 1 } ^ { \prime } \sin { ( 2 i + 1 ) } \xi ,
$$

$$
\xi = ( n - n ^ { \prime } ) ( t - t _ { 0 } ) .
$$

We see that $\boldsymbol { Y } = 0$ and $d X / d t = 0$ for $t = t _ { 0 }$ . The orbit starts at $t = t _ { 0 }$ at a point on the $X$ -axis perpendicularly to the $X$ -axis and cuts the

$X .$ -axis on the opposite side of the origin also perpendicularly. This last point of intersection is called the syzygy.

From (9) we have

$$
\begin{array} { l l } { { u = { \bf a } \cdot \displaystyle \sum _ { i = - \infty } ^ { \infty } a _ { 2 i } \zeta ^ { 2 i + 1 } , } } & { { ~ A _ { 2 i + 1 } = { \bf a } ( a _ { 2 i } + a _ { - 2 i - 2 } ) , } } \\ { { \mathrm { } } } & { { } } \\ { { s = { \bf a } \cdot \displaystyle \sum _ { i = - \infty } ^ { \infty } a _ { - 2 i - 2 } \zeta ^ { 2 i + 1 } , } } & { { ~ A _ { 2 i + 1 } ^ { \prime } = { \bf a } ( a _ { 2 i } - a _ { - 2 i - 2 } ) . } } \end{array}
$$

Substituting these in (8) and equating the coefficients of $\zeta ^ { 2 j }$ ，we obtain

$$
\begin{array} { r l } & { \displaystyle \sum _ { i = 1 } ^ { \infty } \bigg [ 4 j ^ { 2 } - 1 - 2 \mathbf { m } + \frac { 1 } { 2 } \mathbf { m } ^ { 2 } + 4 i ^ { 2 } - 4 i j \bigg ] a _ { 2 } a _ { 2 i - 2 j } } \\ & { \qquad \quad + \left[ \frac { 9 } { 4 } \mathbf { m } ^ { 2 } + \frac { 3 } { 4 } \frac { \mathbf { m } ^ { 2 } } { j } \left( 2 \mathbf { m } + 1 \right) \right] \cdot \sum _ { i } a _ { 2 i } a _ { 2 j - 2 i - 2 } } \\ & { \quad \quad \quad \quad \quad + \left[ \frac { 9 } { 4 } \mathbf { m } ^ { 2 } - \frac { 3 } { 4 } \frac { \mathbf { m } ^ { 2 } } { j } \left( 2 \mathbf { m } + 1 \right) \right] \cdot \sum _ { i } a _ { 2 i } a _ { - 2 i - 2 j - 2 } = 0 , } \\ & { \displaystyle \sum _ { i } \left( 1 - j + \mathbf { m } + 2 i \right) a _ { 2 i } a _ { 2 i - 2 j } } \\ & { \quad \quad \quad \quad \quad - \frac { 3 } { 8 } \frac { \mathbf { m } ^ { 2 } } { j } \sum _ { i } \left( a _ { 2 i } a _ { 2 i - 2 i - 2 } - a _ { 2 i } a _ { - 2 j - 2 i - 2 } \right) } \end{array}
$$

In particular we have for $j = 0$ ，

$$
\frac { C } { { \bf a } ^ { 2 } } = 4 \cdot \sum _ { i } \Big [ ( 2 i + 1 + 2 { \bf m } ) ^ { 2 } + \frac { 1 } { 2 } { \bf m } ^ { 2 } \Big ] a _ { 2 i } ^ { 2 } + \frac { 9 } { 2 } { \bf m } ^ { 2 } \cdot \sum _ { i } a _ { 2 i } a _ { - 2 i - 2 } .
$$

We may put $a _ { 0 } = 1$ ，since a has been introduced.

We can suppose that $\pmb { a } _ { 2 i }$ is of the order $\mathbf { m } ^ { \left. 2 i \right. }$ . In fact, if we put $j = 1$ in (10), we obtain under this supposition

$$
\begin{array} { r l } & { \mathrm { ~ 3 - ~ 2 m ~ + \cdot \cdot ~ } ) ( a _ { 0 } a _ { 2 } + a _ { 0 } a _ { - 2 } ) \ + \ ( 1 1 \ - \ 2 m + \cdot \cdot \cdot ) ( a _ { 2 } a _ { 4 } + a _ { - 2 } a _ { - 4 } } \\ & { \mathrm { ~ \qquad ~ + ~ \cdot ~ } \cdot \cdot + \ ( 3 \mathbf m ^ { 2 } \ + \cdot \cdot \cdot ) ) ( a _ { 0 } ^ { 2 } \ + \ 2 a _ { 2 } a _ { - 2 } \ + \cdot \cdot \cdot ) } \\ & { \mathrm { ~ \qquad ~ + ~ \ } ( \frac { 3 } { 2 } \mathbf m ^ { 2 } \ - \cdot \cdot \cdot ) ( a _ { - 2 } ^ { 2 } \ + \ 2 a _ { 0 } a _ { - 4 } \ + \cdot \cdot \cdot ) \ = } \\ & { \mathrm { ~ \ ~ } \cdot \cdot + ( 4 \ + \mathbf m ) a _ { 2 } a _ { 4 } + ( 2 \ + \ \mathbf m ) a _ { 0 } a _ { 2 } + \ \mathbf m a _ { 0 } a _ { - 2 } } \\ & { \mathrm { ~ \ ~ \ } + \ ( - 2 \ + \cdot \cdot \cdot ) a _ { - 2 } a _ { - 4 } + \cdot \cdot \cdot } \\ & { \mathrm { ~ \ ~ \ } - \frac { 3 } { 8 } \mathbf m ^ { 2 } ( a _ { 0 } ^ { 2 } \ + \ 2 a _ { 2 } a _ { - 2 } \ + \cdot \cdot \cdot - \ a _ { - 2 } ^ { 2 } \ + \cdot \cdot \cdot ) \ = } \end{array}
$$

Suppose that $\pmb { a _ { 4 } }$ and $a _ { - 4 }$ are small in comparison with $\pmb { a _ { 2 } }$ and $\pmb { a } _ { - 2 }$ ; then we see from these equations that ${ a } _ { 2 }$ and $\pmb { a } _ { - 2 }$ are of the order $\mathbf { m ^ { 2 } }$ in comparison with $a _ { 0 } = 1$ ， because the determinant formed of the coefficients of $a _ { 0 } a _ { 2 }$ and $a _ { 0 } a _ { - 2 }$ in these two equations is not zero. By putting $j = 2$ in (10) we can see, similarly, that $a _ { 4 }$ and $\pmb { a } _ { - 4 }$ are of the order $\mathbf { m } ^ { 4 }$ ， and so on. Thus, we see that $a _ { 2 i }$ and $a _ { - 2 i }$ are of the order $\mathbf { m } ^ { | 2 i | }$ .

From this circumstance the coefficients $a _ { 2 i }$ and $\pmb { a } _ { - 2 i }$ can be calculated from (lO) and (ll). Suppose that the coefficients $a _ { 2 i }$ and $a _ { - 2 i }$ for $i = 1 , 2 , . . . , j - 1$ are known. We require a calculation of $\boldsymbol { a } _ { 2 \mathcal { I } }$ and $a - 2 j$ as far as the order $\mathbf { m } ^ { 1 2 j | }$ . The equations (lO) give two simultaneous linear equations for determining $\boldsymbol { a } _ { 0 } \boldsymbol { a } _ { 2 j }$ and $a _ { 0 } a _ { - 2 j }$ .We transform the equations so that the coefficients of $\boldsymbol { a } _ { 0 } \boldsymbol { a } _ { 2 j }$ and $a _ { 0 } a _ { - 2 j }$ are zero in the equations giving $a _ { 2 j }$ and $a _ { \scriptscriptstyle - 2 j }$ ，respectively. Such terms containing $a _ { 0 } a _ { 2 j }$ and $a _ { 0 } a _ { - 2 j }$ are obtained by putting $i = j$ and $i = 0$ ,respectively,in (lO).These terms are

$$
\begin{array} { r } { ( 4 j ^ { 2 } - 1 - 2 \mathbf { m } + \frac { 1 } { 2 } \mathbf { m } ^ { 2 } ) ( a _ { 0 } a _ { 2 j } + a _ { 0 } a _ { - 2 j } ) , } \\ { ( 1 + j + \mathbf { m } ) a _ { 0 } a _ { 2 j } + ( 1 - j + \mathbf { m } ) a _ { 0 } a _ { - 2 j } . } \end{array}
$$

Multiply these expressions by $j - 1 - \mathbf { m }$ and $4 j ^ { 2 } \mathrm { ~ - ~ } 1 \mathrm { ~ - ~ } 2 \mathbf { m } + \frac { 1 } { 2 } \mathbf { m } ^ { 2 } ;$ respectively,and add. Then the coefficient of $a _ { 0 } a _ { - 2 j }$ is zero. But the coefficient of $- a _ { 0 } a _ { 2 j }$ is $- 2 j ( 4 j ^ { 2 } - 1 - 2 \mathbf { m } + \textstyle { \frac { 1 } { 2 } } \mathbf { m } ^ { 2 } )$ ,which is not zero and has not the factor $\mathbf { m }$ ， because the smallest value is obtained for $j = \pm 1$ ，and $8 j ^ { 2 } - 2$ can never vanish.Dividing by this expansion the coefficient of $a _ { 0 } a _ { 2 j }$ becomes $- 1$ .Thus the result is, in Hill's notation (Hill,1878; see also Poincaré, 1909; Brown,1896):

$$
\sum _ { i } \{ [ 2 j , 2 i ] a _ { 2 i } a _ { 2 i - 2 j } + [ 2 j , ] a _ { 2 i } a _ { 2 j - 2 i - 2 } + ( 2 j , ) a _ { 2 i } a _ { - 2 j - 2 i - 2 } \} = 0 ,
$$

where

$$
{ \begin{array} { r l } & { [ 2 j , 2 i ] = - { \frac { i } { j } } { \frac { 8 j ^ { 2 } - 2 - 4 { \bf m } + { \bf m } ^ { 2 } + 4 ( i - j ) ( j - 1 - { \bf m } ) } { 8 j ^ { 2 } - 2 - 4 { \bf m } + { \bf m } ^ { 2 } } } , } \\ & { \qquad [ 2 j , ] = - { \frac { 3 } { 1 6 } } { \frac { { \bf m } ^ { 2 } } { j ^ { 2 } } } { \frac { 4 j ^ { 2 } - 8 j - 2 - 4 ( j + 2 ) { \bf m } - 9 { \bf m } ^ { 2 } } { 8 j ^ { 2 } - 2 - 4 { \bf m } + { \bf m } ^ { 2 } } } , } \\ & { \qquad ( 2 j , ) = - { \frac { 3 } { 1 6 } } { \frac { { \bf m } ^ { 2 } } { j ^ { 2 } } } { \frac { 2 0 j ^ { 2 } - 1 6 j + 2 - 4 ( 5 j - 2 ) { \bf m } + 9 { \bf m } ^ { 2 } } { 8 j ^ { 2 } - 2 - 4 { \bf m } + { \bf m } ^ { 2 } } } . } \end{array} }
$$

Obviously the coefficients of $a _ { 0 } a _ { - 2 j }$ and $a _ { 0 } a _ { 2 j }$ are $[ 2 j , 0 ] = 0$ and $[ 2 j , 2 j ] = - 1$ , respectively. The equations (l2) can be used for determining $a _ { - 2 j }$ . In fact, we put $- j$ in place of $j$ since $j$ can either be positive or negative. The coefficient of $a _ { 0 } a _ { 2 j }$ is then $[ - 2 j , 0 ] = 0$ ，and the coefficient of $a _ { 0 } a _ { - 2 j }$ is $[ - 2 j , - 2 j ] = - 1$ .Thus the equations (l2） can be solved by means of successive approximation. As far as $\mathbf { m } ^ { 7 }$ , we obtain

$$
\begin{array} { c c c c } { { a _ { 2 } = [ 2 , ] , \qquad a _ { - 2 } = ( - 2 , ) } } & { { \mathrm { t o } } } & { { { \bf m } ^ { 5 } ; } } \\ { { a _ { 4 } = [ 4 , 2 ] [ 2 , ] ( - 2 , ) + 2 [ 4 , ] [ 2 , ] , } } & { { } } & { { } } \\ { { a _ { - 4 } = [ - 4 , - 2 ] ( - 2 , ) [ 2 , ] + 2 ( - 4 , ) [ 2 , ] } } & { { \mathrm { t o } } } & { { { \bf m } ^ { 7 } . } } \end{array}
$$

The result is

$$
\begin{array} { c } { { a _ { 2 } = \displaystyle \frac { 3 } { 1 6 } \frac { 6 + 1 2 \mathbf { m } + 9 \mathbf { m } ^ { 2 } } { 6 - 4 \mathbf { m } + \mathbf { m } ^ { 2 } } \mathbf { m } ^ { 2 } , } } \\ { { \displaystyle a _ { - 2 } = - \frac { 3 } { 1 6 } \frac { 3 8 + 2 8 \mathbf { m } + 9 \mathbf { m } ^ { 2 } } { 6 - 4 \mathbf { m } + \mathbf { m } ^ { 2 } } \mathbf { m } ^ { 2 } . } } \end{array}
$$

Further coeffcients are expanded in the form of partial fractions, so that

$$
\begin{array} { c } { \displaystyle { a _ { 2 i } = M _ { 0 } + \frac { M _ { 1 } } { 6 - 4 { \bf m } + { \bf m } ^ { 2 } } + \frac { M _ { 2 } } { [ 6 - 4 { \bf m } + { \bf m } ^ { 2 } ] ^ { 2 } } + \cdots } } \\ { \displaystyle { + \frac { N _ { 1 } } { 3 0 - 4 { \bf m } + { \bf m } ^ { 2 } } + \frac { N _ { 2 } } { [ 3 0 - 4 { \bf m } + { \bf m } ^ { 2 } ] ^ { 2 } } + \cdots , } } \end{array}
$$

where $M _ { 1 } , M _ { 2 } , . . . , N _ { 1 } , N _ { 2 } , . . .$ are polynomials of the form

$$
A \mathbf { m } ^ { k } + B \mathbf { m } ^ { k + 1 }
$$

with constant coefficients $\pmb { A }$ and $B$ .Thus we obtain

$$
\begin{array} { l } { { \displaystyle { z + a _ { - } = - 3 \frac { 2 + \mathbf { m } } { 6 - 4 \mathbf { m } + \mathbf { m } ^ { 2 } } \mathbf { m } ^ { 2 } } , } } \\ { { \displaystyle { z - a _ { - } = = 3 \left[ \frac { 9 } { 8 } - \frac { 4 - 7 \mathbf { m } } { 6 - 4 \mathbf { m } + \mathbf { m } ^ { 2 } } \right] \mathbf { m } ^ { 2 } } , } } \\ { { \displaystyle { a + a _ { - } = - \frac { 3 } { 1 6 } \left[ \frac { 2 4 3 } { 1 6 } + \frac { 3 2 3 } { 6 - 4 \mathbf { m } + \mathbf { m } ^ { 2 } } - 9 6 \frac { 2 3 - 1 1 \mathbf { m } } { 6 - 4 \mathbf { m } + \mathbf { m } ^ { 2 } } \right] } , } } \\ { { \displaystyle { - \frac { 2 1 5 - 5 3 \mathbf { m } } { 3 0 - 4 \mathbf { m } + \mathbf { m } ^ { 2 } } \mathbf { M } } } } \\ { { \displaystyle { a - a _ { - } = \frac { 3 } { 3 2 } \left[ \frac { 2 4 3 } { 8 } + \frac { 1 7 5 + 5 6 3 \mathbf { m } } { 6 - 4 \mathbf { m } + \mathbf { m } ^ { 2 } } - 4 8 \frac { 8 9 - 3 2 \mathbf { m } } { 6 - 4 \mathbf { m } + \mathbf { m } ^ { 2 } } \right] } } } \\ { { \displaystyle { + - \frac { 3 } { 1 0 0 - 4 \mathbf { m } + \mathbf { m } ^ { 2 } } \mathbf { M } } } } \\ { { \displaystyle { + \frac { 5 } { 8 } \frac { 3 6 1 - 1 0 \mathbf { m } } { 4 0 - 4 \mathbf { m } + \mathbf { m } ^ { 2 } } \mathbf { M } ^ { 2 } } , } } \end{array}
$$

Hill(1878) made an artifice for more rapid formal convergence by expanding the series in powers of

$$
{ \overline { { \mathbf { m } } } } = { \frac { \mathbf { m } } { 1 + \alpha \mathbf { m } } }
$$

in place of $\mathbf { m }$ , with a constant $\pmb { \alpha }$ so chosen that the series formally converges most rapidly. The value $\alpha = - 1 / 3$ can make the series for $M / [ 6 - 4 \mathbf { m } + \mathbf { m } ^ { 2 } ] ^ { \kappa }$ in powers of m most rapidly formally convergent. The divisor is then $6 + { \frac { 1 } { 3 } } { \overline { { \mathbf { m } } } }$ .The series is convergent for $\overline { { \mathbf { m } } } < 3$ Thus

$$
\begin{array} { r l } & { a _ { 2 } + a _ { - 2 } = - [ \overline { { \mathbf { m } } } ^ { 2 } + \frac { 1 } { 2 } \overline { { \mathbf { m } } } ^ { 3 } - \frac { 2 } { 9 } \overline { { \mathbf { m } } } ^ { 4 } - \cdot \cdot \cdot ] } \\ & { \qquad = \mathbf { m } ^ { 2 } + \frac { 1 9 } { 6 } \mathbf { m } ^ { 3 } + \frac { 1 3 1 } { 1 8 } \mathbf { m } ^ { 4 } + \cdot \cdot \cdot , } \\ & { a _ { 2 } - a _ { - 2 } = \frac { 1 1 } { 8 } \overline { { \mathbf { m } } } ^ { 2 } + \frac { 5 } { 4 } \overline { { \mathbf { m } } } ^ { 3 } + \frac { 5 } { 7 2 } \overline { { \mathbf { m } } } ^ { 4 } + \cdot \cdot \cdot = \frac { 1 1 } { 8 } \mathbf { m } ^ { 2 } + \frac { 5 9 } { 1 2 } \mathbf { m } ^ { 3 } + \cdot \cdot \cdot } \\ & { \qquad \cdot \cdot \cdot . . } \end{array}
$$

The constant a is determined in the following manner. Put $\Omega = 0$ in (3); then we have

$$
\frac { \kappa u } { ( s u ) ^ { 3 / 2 } } = \biggl ( { \cal D } ^ { 2 } + 2 { \bf m } { \cal D } + \frac { 3 } { 2 } { \bf m } ^ { 2 } \biggr ) u + \frac { 3 } { 2 } { \bf m } ^ { 2 } s ,
$$

where we substitute the expansions for $\pmb { u }$ and $\pmb { \mathscr { s } }$ ：

$$
u = s = \mathbf { a } \cdot \sum _ { i } a _ { 2 i } , \qquad D u = \mathbf { a } \cdot \sum _ { i } ( 2 i + 1 ) a _ { 2 i } , \qquad \cdot \cdot \cdot ,
$$

and put $\zeta = 1$ . Since this relation should hold for any value of $\boldsymbol { \zeta } ,$ we obtain

$$
\frac { \kappa } { { \bf a } ^ { 3 } \left( \sum _ { i } a _ { 2 i } \right) ^ { 2 } } = \sum _ { i } \left[ ( 2 i + 1 + { \bf m } ) ^ { 2 } + 2 { \bf m } ^ { 2 } \right] a _ { 2 i } .
$$

But, since

$$
\kappa = { \frac { \mu } { ( n - n ^ { \prime } ) ^ { 2 } } } = { \frac { \mu ( 1 + { \bf m } ) ^ { 2 } } { n ^ { 2 } } } ,
$$

we find a from the formula

$$
\begin{array} { l } { { { \displaystyle = \left( \frac { \mu } { n ^ { 2 } } \right) ^ { 1 / 3 } ( 1 + { \bf m } ) ^ { 2 / 3 } } \ ~ } } \\ { { { \displaystyle ~ \qquad \times \left\{ \sum _ { i } [ ( 2 i + 1 + { \bf m } ) ^ { 2 } + 2 { \bf m } ^ { 2 } ] a _ { 2 i } \right\} ^ { - 1 / 3 } \cdot \left[ \sum _ { i } a _ { 2 i } \right] ^ { - } } } } \end{array}
$$

if $\pmb { a _ { 2 i } }$ are known. In the ordinary Keplerian motion, $\scriptstyle \mu / n ^ { 2 }$ is the cube of the semimajor axis $\pmb { a }$ .The difference of ${ \mathbf a } / a$ from 1 is expanded in powers of $\mathbf { m }$ ,and vanishes for $\mathbf { m } = 0$

The constant $c$ is determined from (11), that is, from

$$
C = { \bf { a } } ^ { 2 } [ 1 + 4 { \bf { m } } + { \textstyle \frac { 9 } { 2 } } { \bf { m } } ^ { 2 } + ( 9 + 1 2 { \bf { m } } + { \textstyle \frac { 9 } { 2 } } { \bf { m } } ^ { 2 } ) a _ { 2 } ^ { 2 } + \cdot \cdot \cdot ] .
$$

The result can be expressed in terms of the rectangular and polar coordinates with the longitude $L$ and $\xi = ( n - n ^ { \prime } ) t + \epsilon - \epsilon ^ { \prime }$ in the form

$$
\begin{array} { r l } & { ( L - n t - \epsilon ) = r \cos { ( L - n ^ { \prime } t - \epsilon ^ { \prime } - \xi ) } = \frac { 1 } { 2 } ( u \zeta ^ { - 1 } + s \zeta ) , } \\ & { ( L - n t - \epsilon ) = r \sin { ( L - n ^ { \prime } t - \epsilon ^ { \prime } - \xi ) } = - \frac { 1 } { 2 } ( u \zeta ^ { - 1 } - s \zeta ) \sqrt { - 1 } } \end{array}
$$

or

$$
\begin{array} { l } { r \cos { ( L - n t - \epsilon ) } } \\ { = { \bf a } { [ 1 + ( a _ { 2 } + a _ { - 2 } ) \cos { 2 \xi } + ( a _ { 4 } + a _ { - 4 } ) \cos { 4 \xi } + \cdot \cdot \cdot ] } , } \\ { r \sin { ( L - n t - \epsilon ) } } \\ { = { \bf a } { [ ( a _ { 2 } - a _ { - 2 } ) \sin { 2 \xi } + ( a _ { 4 } - a _ { - 4 } ) \sin { 4 \xi } + \cdot \cdot \cdot ] } ; } \end{array}
$$

or, by inserting Hil's (1878) numerical values

n = 17 325 594"060 85, n' = 1 295 977"415 16,   
$\mathbf { m } = 0 . 0 8 0 8 4 8 9 3 3 8 0 ,$ a = 0.999 093 141 $9 6 2 ( \mu / n ^ { 2 } ) ^ { 1 / 3 } ;$ ， $\boldsymbol { r }$ cos $( L - n t - \epsilon ) = { \bf a } ( 1 - 0 . 0 0 7 1 8 0 0 3 9 4 5 5 \cos 2 \xi$ - 0.000 006 042 459 cos $4 \xi$ - 0.000 000 032 576 cos $6 \xi$ + 0.000 000 000 180 cos 8), r sin $( L - n t - \epsilon ) = \mathbf { a } ( 0 . 0 1 0 2 1 1 4 5 4 3 9 6 \sin 2 \xi$ + 0.000 005 714 879 sin $4 \xi$ + 0.000 000 027 499 sin $6 \xi$ + 0.000 000 000 157 sin $8 \xi$ ).

The so-called variation in the moon's inequalities (Section 9.2） is included in this intermediary orbit.

Poincaré (l909） showed by mathematical induction that the coefficients of all terms of the expansions for $\pmb { u }$ and $\pmb { \mathscr { s } }$ are real. Suppose that the solution of (8) for $\pmb { u }$ and $\pmb { \mathscr { s } }$ are of the form $\mathbf { m } ^ { 2 \alpha + 2 \beta } u _ { \alpha } s _ { \beta } ,$ and that

$$
\begin{array} { c } { { \displaystyle \frac { u } { \bar { \zeta } } = u _ { 0 } + { \bf m } ^ { 2 } u _ { 1 } + \cdot \cdot \cdot + { \bf m } ^ { 2 q } u _ { q } + \cdot \cdot \cdot , } } \\ { { \mathrm { } } } \\ { { \displaystyle \frac { \cal S } { \zeta ^ { - 1 } } = s _ { 0 } + { \bf m } ^ { 2 } s _ { 1 } + \cdot \cdot \cdot + { \bf m } ^ { 2 q } s _ { q } + \cdot \cdot \cdot , } } \\ { { \mathrm { } } } \\ { { { \cal C } = C _ { 0 } + { \bf m } ^ { 2 } C _ { 1 } + \cdot \cdot \cdot + { \bf m } ^ { 2 q } C _ { q } + \cdot \cdot \cdot . . } } \end{array}
$$

We determine the coefficients ${ \pmb u } _ { \pmb { \alpha } }$ and $s _ { \beta }$ by successive approximation. We see then that $u _ { \alpha } , s _ { \alpha }$ are homogeneous polynomials of degree $\pmb { \alpha }$ with respect to $\zeta ^ { 2 }$ and $\zeta ^ { - 2 }$ . If we expand the coefficients of $\zeta ^ { 2 k }$ or $\zeta ^ { - 2 k }$ in powers ofm, then the expansion contains only such terms as those with $2 k$ ， $2 k + 4$ ， $2 k + 8 , \ldots$ as the exponents of $\mathbf { m }$ ,that is, in powers not of $\mathbf { m } ^ { 2 }$ but of $\mathbf { m ^ { 4 } }$ .This explains the rapidity of the convergence of Hill's series.

Wintner (1925,1938,1947) proved the convergence of the series,and hence the existence of the periodic solution of Hil's intermediary orbit, by the method of nonlinear infinite analysis,as will be described in Sections 11.4 and 20.9.

# 11.3VARIATIONAL CURVE

Hill (1878,1886) took as his intermediary orbit for the motion of the moon the particular solution (Section l1.2) of the equations (3) for which $\Omega = 0$ and called it the variational curve. Put $\Omega = 0$ in (3); then,

$$
\begin{array} { r } { \frac { d ^ { 2 } u } { d t ^ { 2 } } - 2 n ^ { \prime } \frac { d u } { d t } + \frac { \mu } { ( u s ) ^ { 3 / 2 } } u - \frac { 3 } { 2 } n ^ { \prime 2 } ( u + s ) = 0 , } \\ { \frac { d ^ { 2 } s } { d t ^ { 2 } } + 2 n ^ { \prime } \frac { d s } { d t } + \frac { \mu } { ( u s ) ^ { 3 / 2 } } s - \frac { 3 } { 2 } n ^ { \prime 2 } ( u + s ) = 0 , } \end{array}
$$

with the Jacobi integral

$$
{ \frac { 1 } { 2 } } { \frac { d u } { d t } } { \frac { d s } { d t } } = { \frac { \mu } { \sqrt { u s } } } + { \frac { 3 } { 8 } } n ^ { \prime 2 } ( u + s ) ^ { 2 } - C .
$$

In rectangular coordinates these equations are (Section 9.13)

$$
\begin{array} { r } { \frac { d ^ { 2 } X } { d t ^ { 2 } } - 2 n ^ { \prime } \frac { d Y } { d t } + \Big ( \frac { \mu } { r ^ { 3 } } - 3 n ^ { \prime 2 } \Big ) X = 0 , } \\ { \frac { d ^ { 2 } Y } { d t ^ { 2 } } + 2 n ^ { \prime } \frac { d X } { d t } + \frac { \mu } { r ^ { 3 } } Y = 0 , } \end{array}
$$

with the Jacobi integral

$$
{ \frac { 1 } { 2 } } \left[ \left( { \frac { d X } { d t } } \right) ^ { 2 } + \thinspace \left( { \frac { d Y } { d t } } \right) ^ { 2 } \right] = { \frac { \mu } { r } } + { \frac { 3 } { 2 } } n ^ { \prime 2 } X ^ { 2 } - C \geq 0 .
$$

Consider the zero-velocity curve

$$
\frac { \mu } { ( X ^ { 2 } + Y ^ { 2 } ) ^ { 3 / 2 } } + \frac { 3 } { 2 } n ^ { \prime 2 } X ^ { 2 } - C = 0 .
$$

This intersects the $\pmb { Y } .$ -axis at $Y _ { 0 } = \mu / C$ and cuts the $X .$ -axis at points whose coordinates are the roots of

$$
X ^ { 3 } - { \frac { 2 C } { 3 n ^ { \prime 2 } } } X + { \frac { 2 \mu } { 3 n ^ { \prime 2 } } } = 0 .
$$

If $( 2 C ) ^ { 3 / 2 } > 9 \mu n ^ { \prime }$ ,then two real roots of this equation are between O and $+ \sqrt { 2 C / ( 3 n ^ { \prime 2 } ) }$ .If $( 2 C ) ^ { 3 / 2 } = 9 \mu n ^ { \prime }$ ， then these two roots are equal. If $( 2 C ) ^ { 3 / 2 } < 9 \mu n ^ { \prime }$ ,then there is no real root. Two straight lines

$$
X = ~ \pm { \sqrt { 2 C / ( 3 n ^ { \prime 2 } ) } }
$$

are the asymptotes (Figure 10 of Chapter 9, page 349). At either of the double points

$$
X = { \frac { \sqrt { 2 C } } { 3 n ^ { \prime } } } = { \frac { \sqrt [ 3 ] { 9 \mu n ^ { \prime } } } { 3 n ^ { \prime } } } ,
$$

the force and the velocity both become zero.For the moon,the asymptote cuts the $X$ -axis at $\sqrt { 2 C / ( 3 n ^ { \prime 2 } ) } = 5 0 0 . 4 9 9 2$ in the units of the earth's mean equatorial radius and the earth's mass. At $\sqrt [ 3 ] { \mu / ( 3 n ^ { \prime 2 } ) } = 2 3 5 . 5 9 7 1$ the moon is stationary with respect to the sun. The points of intersection of the zero-velocity curve with the $X .$ -axis are $[ 2 \sqrt { 2 C } / ( 3 n ^ { \prime } ) ]$ sin $\{ \theta / 3 \}$ and $[ 2 \sqrt { 2 C } / ( 3 n ^ { \prime } ) ]$ sin $\{ 6 0 ^ { \circ } \mathrm { ~ - ~ } ( \theta / 3 ) \}$ , where sin $\theta = 9 \mu n ^ { \prime } / ( 2 C )$ or

$$
\theta = 3 2 ^ { \circ } 4 9 ^ { \prime } 6 ! 6 3 ,
$$

that is, numerically 109.6772 and 435.5623.In the case of the moon, in which n = 0.229 970 85,n’ = 0.017 202 124, $\mu = 1 1 6 0 9 . 0 1 4 ,$

$$
C = 1 1 1 . 1 8 8 8 3 ,
$$

the zero-velocity curve consists of an oval around the earth and two asymptotic branches, as in Figure $1 0 a$ of Chapter 9 (page 349). The oval cuts the $\mathbf { \nabla } _ { Y \cdot }$ -axis at $Y _ { 0 } = \pm 1 0 4 . 4 0 8$ and the $X .$ -axis at $X _ { 1 } = - 1 0 9 . 6 5 5$ and $X _ { 2 } =  { \mathrm { ~ + ~ } } 1 0 9 . 6 9 4$

Since

$$
\frac { \mu } { ( X ^ { 2 } + Y ^ { 2 } ) ^ { 1 / 2 } } + \frac { 3 } { 2 } n ^ { \prime 2 } X ^ { 2 } - C > 0
$$

inside the oval and in the outside regions of the asymptotic branches, extending to infinity toward the $\pm X \cdot$ -axis,the real motion should be inside the oval or in the outside regions of the asymptotic branches.The moon is now inside the oval.Hence,as far as the present approximation of neglecting the perturbations is concerned, the moon will remain inside the oval also in the future.

The behavior of the zero-velocity curve as a criterion of stability was discussed by Bohlin (1887, 1888)and extended to a more general class of dynamical problems.

Hill (l887) further discussed different systems of variables that might be employed in solving a system somewhat more general than the restricted three-body problem,namely, that of a particle of mass zero attracted by two bodies which move in Keplerian ellipses around their common center of gravity. He then turned to the motion of Hyperion disturbed by Titan by using elliptic coordinates.The idea was further developed by Bohlin (1887,1888),Kobb (1901),Darwin (1897),and Plummer (1902,1903,1904,1918).Similar considerations have been applied for studying the stability ofa circular orbit under a central force by Lehmann-Filhés (1898) and Frank (l908),and for asteroidal, cometary,and satellite problems by Kobb (1908),Darwin (1897),Plummer (1902,1903,1904,1918),Callandreau (1892),Heinrich (1913,1916, 1918)，Wilkens (1924),Wintner (1930,l936) and Hagihara (1927, 1952) (Sections 10.34,10.35).

The fraction $1 / \mathbf { m }$ represents the number of lunations in one period of the revolution of the sun around the earth, that is, the number of lunar months in one year.For $1 / \mathbf { m } < 1 / 3$ ，the analytical method will be of success in deriving the motion of the moon, but it fails for $1 / \mathbf { m } > 1 / 3 _ { ! }$ so that a method of mechanical quadrature should be adopted.The point where the variational curve, starting at a point on the $X .$ -axis perpendicularly to the $X .$ -axis, cuts the $X$ -axis again on the other side of the earth is the syzygy. The point where the curve cuts the $\pmb { Y } .$ -axis is called the quadrature.

![](images/94807fa47e770544b9b4df56e8f5b688af9d6ed53999f5b8520252d5c36275fd.jpg)  
FIGURE I (Matukuma, 1933-1957).

There is an orbit with cusps (Figure l).Hillthought that there would be no periodic solution beyond this point.It corresponds to 2.8 lunations,and the period of revolution of such a moon around the earth is 204.896 days. This is called the maximum lunation. The moon is stationary at either of the cusps. Adams (1877), Poincaré (1892), Hough (1901), Moritz (l9l8),and Wintner (l928) pointed out that it can be continued analytically beyond this point, so that the name of the maximum lunation loses its sense.Matukuma (1930,1932,1933,1957) computed numerically the periodic orbits beyond this maximum lunation as an analytical continuation of Hil's variational curves (Figure 2). Wintner (l930, 1930a, 1931；Section 20.l4) and Martin (193l, 193la) extended the research and discussed the result of Stromgren (l938； Section 17.5） in his numerical computation of periodic solutions of the restricted three-body problem.Hopf (l929） proved the existence of such a kind of periodic solution of Hill on the basis of Poincaré's theory of periodic solutions (Section l8.13).Hénon (1969,1970) recently studied thc trajectories beyond Hill's maximum lunation numerically and found five families of simple periodic symmetric orbits (see Section 17.6).

The moon of the maximum lunation is of the class of satellites with the minimum radius vector in syzygies and the maximum in quadratures; according to Hill (1878),“that which,having the longest lunation, is still able to appear at all angles with the sun and then undergo all possible phases. Whether this class of satellites is properly to be prolonged beyond

![](images/6745909a54d0cbcb2574931686900d30800ddfe20c2ebf01f801367eb43238c7.jpg)

FIGURE 2 (Matukuma, 1933-1957).

this moon, can only be decided by further employment of mechanical quadratures.But it is at least certain that the orbits,if they exist, do not intersect the line of quadratures and that the moon describing them would make oscillations to and fro, never departing as much as $9 0 °$ from the point of conjunction or of opposition”[Hill,Collected Math. Works,I (1905), 334]. But this is wrong, as predicted by Poincaré. The question is whether the periodic solution exists beyond the orbit of the moon of the maximum lunation. Poincaré's (l892) argument is as follows.

Let $X _ { 0 } , X _ { 0 } ^ { \prime }$ ， $Y _ { 0 } ,$ and ${ { { Y } } _ { 0 } ^ { \prime } }$ be the initial values of $X , d X / d t = X ^ { \prime } , Y ,$ and $d Y / d t = Y ^ { \prime }$ ，respectively. In the case of the moon of the maximum lunation, we have $X _ { 0 } = X _ { 0 } ^ { \prime } = Y _ { 0 } ^ { \prime } = 0$ and $\begin{array} { r } { Y _ { 0 } = Y _ { 0 } ^ { ( 0 ) } } \end{array}$ . In a time $_ { T }$ which is one-fourth of the period this moon will be in symmetric conjunction and $Y = 0$ ， $X ^ { \prime } = 0$ .Consider another particular solution with the initial condition 0, $X _ { 0 } ^ { \prime }$ ， $Y _ { \scriptscriptstyle 0 } , 0$ ,the position at the initial epoch being in symmetric quadrature. After $T + \tau _ { : }$ ，the coordinates will be

$$
Y = f _ { 1 } ( T + \tau , X _ { 0 } ^ { \prime } , Y _ { 0 } ) , ~ X ^ { \prime } = f _ { 2 } ( T + \tau , X _ { 0 } ^ { \prime } , Y _ { 0 } ) .
$$

The functions $f _ { 1 }$ and $f _ { 2 }$ can be expanded in powers of $\boldsymbol { \tau } , \ \boldsymbol { X } _ { 0 } ^ { \prime }$ and $\begin{array} { r } { Y _ { 0 } = Y _ { 0 } ^ { ( 0 ) } } \end{array}$ ,and vanish for $\tau = X _ { 0 } ^ { \prime } = 0 $ $\begin{array} { r } { Y _ { 0 } = Y _ { 0 } ^ { ( 0 ) } } \end{array}$ $\operatorname { I f } f _ { 1 } = f _ { 2 } = 0$ then we have symmetric conjunction at the end of $T + \tau$ and the solution will be periodic with period $4 T + 4 \tau$ From $f _ { 1 } = f _ { 2 } = 0$ we can derive $_ { T }$ and $Y _ { 0 }$ in terms of $X _ { 0 } ^ { \prime }$ ; and $\boldsymbol { \tau }$ and $Y _ { 0 }$ are developable in powers of $X _ { 0 }$ The exception may occur if the Jacobian of $f _ { 1 }$ and $f _ { 2 }$ with respect to $\pmb { \tau }$ and $\scriptstyle { Y _ { 0 } }$ vanishes for $\tau = X _ { 0 } ^ { \prime } = 0 _ { : }$ ， $\begin{array} { r } { Y _ { 0 } = Y _ { 0 } ^ { ( 0 ) } } \end{array}$ . This question will be decided by the numerical computation of Hillif it is further continued. Hill computed the functions $f _ { 1 } ( T , 0 , Y _ { 0 } )$ and $f _ { 2 } ( T , 0 , Y _ { 0 } )$ for different values of $_ { T }$ and $Y _ { 0 }$ ,and then determined by interpolation the values of $_ { T }$ and $\scriptstyle { Y _ { 0 } }$ for which the two functions vanish. If the Jacobian vanishes at this value, then the interpolation would be impossible by ordinary methods.Hence, the orbit of the moon can be continued analytically beyond the moon of the maximum lunation.

Then what will be the form of the orbit? The values of $X$ and $\pmb { Y }$ depend on $t$ and $X _ { 0 } ^ { \prime }$ ，since the initial value $Y _ { 0 }$ is given in terms of $X _ { 0 } ^ { \prime }$ by $f _ { 1 } = f _ { 2 } = 0$ If $X _ { 0 } ^ { \prime }$ and $t$ are sufficiently small, then $X$ and $Y$ can be expanded in powers of these two variables.By symmetry, $X$ contains only odd powers of $t _ { : }$ and $Y$ contains only even powers of $t .$ Hence,

$$
X = X _ { 0 } ^ { \prime } t + { \frac { X _ { 0 } ^ { \prime \prime } } { 6 } } t ^ { 3 } + \cdot \cdot \cdot ,
$$

$X _ { 0 } ^ { ( n ) }$ being the initial values of the nth derivative of $X .$ If $X _ { 0 } ^ { \prime }$ and $t$ are sufficiently small, then $X$ can be approximated by the first two terms.

$X _ { 0 } ^ { \prime \prime \prime }$ is developable in increasing powers of $X _ { 0 } ^ { \prime }$ .But, since $X _ { 0 } ^ { \prime }$ is small, $X _ { 0 } ^ { \prime \prime \prime }$ is reduced to the value that it takes for $X _ { 0 } ^ { \prime } = 0$ .For $X _ { 0 } ^ { \prime } = 0$ we have

$$
X _ { 0 } ^ { \prime \prime } = - \frac { 2 \mu n } { ( Y _ { 0 } ^ { ( 0 ) } ) ^ { 2 } } \cdot
$$

Hence,

$$
X = X _ { 0 } ^ { \prime } t - \frac { \mu n } { 3 ( Y _ { 0 } ^ { ( 0 ) } ) ^ { 2 } } t ^ { 3 } .
$$

For the moon for which the lunation is shorter than the maximum lunation, $X _ { 0 } ^ { \prime }$ is negative,and the two terms of the right-hand side are of the same sign, and $X$ cannot vanish for very small values of $t$ if it does not vanish for $t = 0$ 、For the moon of which the lunation is longer than the maximum lunation, $X _ { 0 } ^ { \prime }$ is positive,and $X$ vanishes for $t = 0$ and $t = \pm Y _ { 0 } ^ { ( 0 ) } \sqrt { 3 X _ { 0 } ^ { \prime } / ( \mu n ) }$ . Hence there are three values of $t$ for which $X$ vanishes, that is, three quadratures at very nearby epochs. Thus Hill's conjecture that such a moon can never be in quadrature is erroneous. There are three quadratures between two consecutive syzygies (Figure 2).

# II.4CONVERGENCE FOR A VARIATIONAL CURVE

The convergence limit of Hil's series (9) was discussed at first by Liapounov (l896) by a majorant method. The equations (3) are written with a small parameter $\lambda = \mathbf { m } ^ { 2 }$ in the form

$$
\begin{array} { r l r } & { } & { \displaystyle \frac { d ^ { 2 } u } { d \tau ^ { 2 } } + 2 \mathbf { m } \sqrt { - 1 } \frac { d u } { d \tau } - \frac { 3 } { 2 } \mathbf { m } ^ { 2 } u + \frac { \kappa u } { ( u s ) ^ { 3 / 2 } } = \frac { 3 } { 2 } \lambda s , } \\ & { } & { \displaystyle \frac { d ^ { 2 } s } { d \tau _ { \cdot } ^ { 2 } } - 2 \mathbf { m } \sqrt { - 1 } \frac { d s } { d \tau } - \frac { 3 } { 2 } \mathbf { m } ^ { 2 } s + \frac { \kappa s } { ( u s ) ^ { 3 / 2 } } = \frac { 3 } { 2 } \lambda u , } \\ & { } & { \displaystyle \tau = ( n - n ^ { \prime } ) ( t - t _ { 0 } ) . } \end{array}
$$

For $\lambda = 0$ the solution is

$$
u = a \exp { \{ \sqrt { - 1 } \tau \} } , \quad \quad s = a \exp { \{ - \sqrt { - 1 } \tau \} } ,
$$

where

$$
{ \frac { \kappa } { a ^ { 3 } } } = l = 1 + 2 { \bf m } + { \frac { 3 } { 2 } } { \bf m } ^ { 2 } .
$$

We define $\pmb { \mathscr { p } }$ and $q$ by

$$
u = a ( 1 - \rlap / ) \exp \{ \sqrt { - 1 } \tau \} , \ ~ s = a ( 1 - \rlap / ) \exp \{ - \sqrt { - 1 } \tau \} ;
$$

then,

$$
\begin{array} { r l r } {  { \frac { d ^ { 2 } p } { d \tau ^ { 2 } } + 2 ( 1 + \mathbf { m } ) \sqrt { - 1 } \frac { d p } { d \tau } - \frac { 3 } { 2 } l ( \boldsymbol { \phi } + q ) } } \\ & { } & { = \frac { 3 } { 2 } \lambda ( q - 1 ) \exp \{ - 2 \sqrt { - 1 } \tau \} + l R _ { p } , } \\ & { } & { \frac { d ^ { 2 } q } { d \tau ^ { 2 } } - 2 ( 1 + \mathbf { m } ) \sqrt { - 1 } \frac { d q } { d \tau } - \frac { 3 } { 2 } l ( \boldsymbol { \phi } + q ) } \\ & { } & { = \frac { 3 } { 2 } \lambda ( \boldsymbol { \phi } - 1 ) \exp \{ 2 \sqrt { - 1 } \tau \} + l R _ { q } , } \end{array}
$$

where $R _ { p } , R _ { q }$ denote terms of positive powers of $\not p , q$ with positive coefficients which are convergent for $| { \boldsymbol { p } } | < 1 , | { \boldsymbol { q } } | < 1$ and satisfy

$$
\begin{array} { r } { ( 1 - \phi ) ^ { - 1 / 2 } ( 1 - q ) ^ { - 3 / 2 } = 1 + \frac { 1 } { 2 } \phi + \frac { 3 } { 2 } q + R _ { p } , } \\ { ( 1 - \phi ) ^ { - 3 / 2 } ( 1 - q ) ^ { - 1 / 2 } = 1 + \frac { 3 } { 2 } \phi + \frac { 1 } { 2 } q + R _ { q } . } \end{array}
$$

Liapounov expanded $\not p , q$ in the form

$$
\dot { p } = / p _ { 1 } \lambda + / p _ { 2 } \lambda ^ { 2 } + \cdot \cdot \cdot , \qquad q = q _ { 1 } \lambda + q _ { 2 } \lambda ^ { 2 } + \cdot \cdot \cdot ,
$$

with the initial condition ${ \pmb { \mathscr { p } } } = { \pmb q }$ and $\ b { \mathscr { p } } _ { j } = \ b { q } _ { j }$ for $\tau = 0$ ,that is, $\boldsymbol { Y } = \mathbf { 0 }$ for $t = t _ { 0 } ,$ and wrote

$$
R _ { p } = P _ { 2 } \lambda ^ { 2 } + P _ { 3 } \lambda ^ { 3 } + \cdot \cdot \cdot , ~ R _ { q } = Q _ { 2 } \lambda ^ { 2 } + Q _ { 3 } \lambda ^ { 3 } + \cdot \cdot \cdot ,
$$

where $\bar { P } _ { j } , Q _ { j }$ are polynomials in $\pmb { \mathscr { p } _ { 1 } } , q _ { 1 } , . . . , p _ { j - 1 } , q _ { j - 1 }$ with positive coefficients.We obtain

$$
\begin{array} { r l r } { \frac { d ^ { 2 } \hat { \rho } _ { 1 } } { d \tau ^ { 2 } } + 2 ( 1 + \mathbf { m } ) \sqrt { - 1 } \frac { d \hat { \rho } _ { 1 } } { d \tau } - \frac { 3 } { 2 } l ( \hat { \rho } _ { 1 } + q _ { 1 } ) } & { ~ } & \\ & { } & { = - \frac { 3 } { 2 } \exp { \{ - 2 \sqrt { - 1 } \tau \} } , } \\ & { } & { \frac { d ^ { 2 } { q } _ { 1 } } { d \tau ^ { 2 } } - 2 ( 1 + \mathbf { m } ) \sqrt { - 1 } \frac { d q _ { 1 } } { d \tau } - \frac { 3 } { 2 } l ( \hat { \rho } _ { 1 } + q _ { 1 } ) } \\ & { } & \\ & { } & { = - \frac { 3 } { 2 } \exp { \{ 2 \sqrt { - 1 } \tau \} } , } \end{array}
$$

$$
\begin{array} { r l r } {  { \frac { d ^ { 2 } \hat { p } _ { j } } { d \tau ^ { 2 } } + 2 ( 1 + \mathbf { m } ) \sqrt { - 1 } \frac { d \hat { p } _ { j } } { d \tau } - \frac { 3 } { 2 } l ( \boldsymbol { \phi } _ { j } + \boldsymbol { \phi } _ { j } ) } } \\ & { } & \\ & { } & { = \frac { 3 } { 2 } q _ { j - 1 } \exp \{ - 2 \sqrt { - 1 } \tau \} + l P _ { j } , } \\ & { } & \\ & { } & { \frac { d ^ { 2 } q _ { j } } { d \tau ^ { 2 } } - 2 ( 1 + \mathbf { m } ) \sqrt { - 1 } \frac { d q _ { j } } { d \tau } - \frac { 3 } { 2 } l ( \boldsymbol { \phi } _ { j } + q _ { j } ) } \\ & { } & { = \frac { 3 } { 2 } \hat { p } _ { j - 1 } \exp \{ 2 \sqrt { - 1 } \tau \} + l Q _ { j } } \\ & { } & { ( j = 2 , 3 , \ldots ) . } \end{array}
$$

Let

$$
\begin{array} { l } { { \displaystyle { \dot { p } } _ { j } = \sum _ { i = 0 } ^ { j } a _ { j , j - 2 i } \exp \left\{ 2 ( j - 2 i ) \sqrt { - 1 } \tau \right\} } , } \\ { { \displaystyle { \dot { q } } _ { j } = \sum _ { i = 0 } ^ { j } a _ { j , j - 2 i } \exp \left\{ - 2 ( j - 2 i ) \sqrt { - 1 } \tau \right\} } , } \end{array}
$$

with constant $a _ { j , i }$ .Then the solution of the first set of equations (l3a) is

$$
\begin{array} { l c r } { { \pmb { \mathscr { p } } _ { 1 } = a _ { 1 , 1 } \exp \left\{ 2 \sqrt { - 1 } \tau \right\} + a _ { 1 , - 1 } \exp \left\{ - 2 \sqrt { - 1 } \tau \right\} , } } \\ { { \pmb { \mathscr { q } } _ { 1 } = a _ { 1 , 1 } \exp \left\{ - 2 \sqrt { - 1 } \tau \right\} + a _ { 1 , - 1 } \exp \left\{ 2 \sqrt { - 1 } \tau \right\} , } } \end{array}
$$

$$
a _ { 1 , 1 } = \mathrm { ~ - } \frac { 9 } { 1 6 } \frac { 2 \mathrm { ~ + ~ } 4 \mathbf { m } } { 6 \mathrm { ~ - ~ } 4 \mathbf { m } \mathrm { ~ + ~ } \mathbf { m } ^ { 2 } } , \qquad a _ { 1 , - 1 } = \frac { 3 } { 1 6 } \frac { 3 8 \mathrm { ~ + ~ } 2 8 \mathbf { m } \mathrm { ~ + ~ } 9 \mathbf { m } ^ { 2 } } { 6 \mathrm { ~ - ~ } 4 \mathbf { m } \mathrm { ~ + ~ } \mathbf { m } ^ { 2 } } .
$$

Also, let

$$
q _ { r - 1 } \exp \left\{ - 2 \sqrt { - 1 } \tau \right\} + l P _ { r } = \sum _ { i = 0 } ^ { r } A _ { r , r - 2 i } \exp \left\{ 2 ( r - 2 i ) \sqrt { - 1 } \tau \right\} ,
$$

$$
\phi _ { r - 1 } \exp \left\{ 2 \sqrt { - 1 } \tau \right\} + l Q _ { \tau } = \sum _ { i = 0 } ^ { r } A _ { r , r - 2 i } \exp \left\{ - 2 ( r - 2 i ) \sqrt { - 1 } \tau \right\}  _ { , . . }
$$

where $A _ { \tau , \sigma }$ are polynomials with positive coefficients

$$
a _ { 1 , \pm 1 } , a _ { 2 , \pm 1 } , a _ { 2 , 0 } , a _ { 2 , \pm 2 } , . . . , a _ { r - 1 , \pm ( r - 1 ) } .
$$

Then we obtain

$$
\begin{array} { r l r } & { a _ { r , \sigma } = \frac { \frac { 3 } { 2 } [ A _ { r , - \sigma } - { \bf \sigma } [ 4 \sigma ^ { 2 } - 4 ( 1 + { \bf m } ) \sigma + \frac { 3 } { 2 } l ] A _ { r , \sigma }  } {  2 \sigma ^ { 2 } [ 2 ( 4 \sigma ^ { 2 } - 1 ) - 4 { \bf m } + { \bf m } ^ { 2 } ]  } } & {  ( \sigma \neq 0 ) ,  } \\ & {  a _ { r , 0 } = - \frac { 1 } { 3 l } A _ { r , 0 } . } \end{array}
$$

Liapounov referred to the auxiliary lemma:

Lemma: If $a , \ b , \ c$ are positive numbers such that $a c - b ^ { 2 } > 0$ and $M > 0$ is not larger than the smaller root of

$$
{ \frac { x ^ { 2 } } { a } } - 2 { \frac { x } { b } } + { \frac { 1 } { c } } = 0 ,
$$

then the lower bound of the modulus of the function

$$
f ( x ) = a - 2 b x + c x ^ { 2 }
$$

for $\pmb { x } _ { \mathrm { i } }$ such that $| { \pmb x } | \le M ,$ is $f ( M ) = a - 2 b M + c M ^ { 2 }$ If

$$
M \leq \frac { 2 \sqrt { 4 \sigma ^ { 2 } - 1 } } { \sqrt { 4 \sigma ^ { 2 } - 1 } + \sqrt { 4 \sigma ^ { 2 } - 3 } } ,
$$

then, for $| { \mathbf { m } } | \leq M ,$ we have

$$
| 2 ( 4 \sigma ^ { 2 } - 1 ) - 4 { \bf m } + { \bf m } ^ { 2 } | \geq 2 ( 4 \sigma ^ { 2 } - 1 ) - 4 M + M ^ { 2 } .
$$

We assume $M \leq 1$ . Then, for $| { \bf m } | \le M \le 1$ , we can write

$$
| 2 ( 4 \sigma ^ { 2 } - 1 ) - 4 { \bf m } + { \bf m } ^ { 2 } | \geq 6 - 4 M + M ^ { 2 } .
$$

From the lemma, we have for the denominator in the equation for ${ \pmb a } _ { \tau , 0 }$

$$
| l | \geq 1 - 2 M + \frac { 3 } { 2 } M ^ { 2 } \qquad ( | \mathbf { m } | \leq M ) ,
$$

and

$$
M \equiv 1 - \frac { 1 } { \sqrt { 3 } } = 0 . 4 2 \dots
$$

Liapounov wrote

$$
\begin{array} { r } { | a _ { r , \sigma } | \leq \frac { 3 2 L | A _ { r , - \sigma } | + ( 8 + 4 M + \frac { 3 } { 2 } L ) | A _ { r , \sigma } | } { 2 ( 6 - 4 M + M ^ { 2 } ) } , } \\ { \alpha _ { r , \sigma } = \frac { \frac { 3 } { 2 } L A _ { r , - \sigma } + ( 8 + 4 M + \frac { 3 } { 2 } L ) A _ { r , \sigma } } { 2 ( 6 - 4 M + M ^ { 2 } ) } , } \end{array}
$$

where

$$
L = 1 + 2 M + \frac { 3 } { 2 } M ^ { 2 } , M \equiv 1 - \frac { 1 } { \sqrt { 3 } } ,
$$

$$
\begin{array} { r } { \alpha _ { 1 , 1 } = | a _ { 1 , 1 } | , \qquad \alpha _ { 1 , - 1 } = | a _ { 1 , - 1 } | , \qquad A _ { 1 , - 1 } = \frac { 3 } { 2 } , \qquad A _ { 1 , 1 } = 0 . } \end{array}
$$

Since we have

$$
\sum _ { i = 0 } ^ { j } \alpha _ { j , j - 2 i } = \frac { 8 + 4 M + 3 L } { 2 ( 6 - 4 M + M ^ { 2 } ) } \sum _ { i = 0 } ^ { j } A _ { j , j - 2 i } \qquad ( j = 1 , 2 , 3 , \ldots ) ,
$$

we can take

$$
z = \sum _ { j = 1 } ^ { \infty } \left( \sum _ { i = 0 } ^ { j } \alpha _ { j , j - 2 i } \right) \lambda ^ { j }
$$

as the majorant series for the solution

$$
\sum _ { i = 0 } ^ { j } a _ { j , j - 2 i } \exp \left\{ \pm 2 ( j - 2 i ) \sqrt { - 1 } \tau \right\}
$$

of the differential equations (13b)for $\phi _ { j } , q _ { j }$

Put

$$
\sum _ { i = 0 } ^ { j } A _ { j , j - 2 i } = \frac { 3 } { 2 } \sum _ { i = 0 } ^ { j - 1 } \alpha _ { j - 1 , j - 1 - 2 i } + L P _ { j } \qquad ( j = 2 , 3 , . . . ) .
$$

Summing from $j = 1$ to $j = \infty$ , we obtain

$$
z = \frac { 8 + 4 M + 3 L } { 2 ( 6 - 4 M + M ^ { 2 } ) } \left[ \frac { 3 } { 2 } ( 1 + z ) \lambda + L R _ { p } \right] .
$$

Expressing $R _ { p }$ according to the definition, we have

$$
z = \frac { 8 + 4 M + 3 L } { 2 ( 6 - 4 M + M ^ { 2 } ) } \Bigg \{ \frac { 3 } { 2 } ( 1 + z ) \lambda + L \bigg [ \frac { 1 } { ( 1 - z ) ^ { 2 } } - 1 - 2 z \bigg ] \Bigg \} ,
$$

or

$$
z = \epsilon ( 1 + z ) + h \frac { ( 3 - 2 z ) z ^ { 2 } } { ( 1 - z ) ^ { 2 } } ,
$$

where

$$
\epsilon = \frac { 3 ( 2 2 + 2 0 M + 9 M ^ { 2 } ) } { 8 ( 6 - 4 M + M ^ { 2 } ) } \lambda , \quad \quad h = \frac { 2 2 + 2 0 M + 9 M ^ { 2 } } { 4 ( 6 - 4 M + M ^ { 2 } ) } L .
$$

Liapounov considered,instead,

$$
z = \epsilon ( 1 + z ) + \frac { 9 h z ^ { 2 } } { 3 - 4 z }
$$

and obtained as the solution

$$
z = \frac { 3 + \epsilon - \sqrt { 9 - 6 ( 7 + 1 8 h ) \epsilon + 4 9 \epsilon ^ { 2 } } } { 2 ( 4 + 9 h - 4 \epsilon ) } .
$$

If as the condition for the resolvability of the expression under the radical we have

$$
\epsilon \leq \frac { 3 } { 7 + 1 8 h + \sqrt { ( 7 + 1 8 h ) ^ { 2 } - 4 9 } } ,
$$

or

$$
\epsilon \leq \frac { 3 } { 2 ( 7 + 1 8 h ) } , \mathrm { o r } \epsilon \leq \frac { 1 } { 6 ( 1 + 2 h ) } ,
$$

then Liapounov's majorant method can be applied and the series is absolutely and uniformly convergent. This is an inequality for $\lambda$ and $M$ ， if $| { \mathbf { m } } | \leq M .$ Supposing that $\lambda = M ^ { 2 }$ ,we obtain

$$
M \leq 1 / 7 .
$$

Hence, putting $\lambda = \mathbf { m } ^ { 2 }$ ， we find the lower bound

$$
| { \bf m } | \leq 1 / 7 \equiv 0 . 1 4 3 .
$$

Merman (1952) derived a sharper estimate.

From the above relations between $\alpha _ { r , \sigma }$ and $A _ { r , \sigma }$ we see, by putting $r = N + 1$ ，that

$$
\alpha _ { r , \sigma } = | a _ { r , \sigma } | \qquad ( r = 1 , 2 , . . . , N ; | \sigma | \le r ) .
$$

But we have

$$
: = \sum _ { j = 1 } ^ { N } \left( \sum _ { i = 0 } ^ { j } \left. a _ { j , j - 2 i } \right. \right) \lambda ^ { j } + \frac { 8 + 4 M + 3 L } { 2 ( 6 - 4 M + M ^ { 2 } ) } \sum _ { j = N + 1 } ^ { \overset { \circ } { \sum } } \left( \sum _ { i = 0 } ^ { j } A _ { j , j - 2 i } \right) \lambda ^ { j }
$$

The expression in the second sum

$$
\begin{array} { c } { { \displaystyle \frac { 8 + 4 M + 3 L } { ( 6 - 4 M + M ^ { 2 } ) } \left\{ \frac { 3 } { 2 } ( 1 + z ) \lambda + L \biggl [ \frac { 1 } { ( 1 - z ) ^ { 2 } } - 1 - 2 z \biggr ] \right\} } } \\ { { { } } } \\ { { = \epsilon ( 1 + z ) + h \frac { ( 3 - 2 z ) } { ( 1 - z } } } \end{array}
$$

expanded in powers of $\lambda$ , begins with $\lambda ^ { N + 1 }$ . In general let the expression be written

$$
\epsilon + L _ { 2 } \lambda ^ { 2 } + L _ { 3 } \lambda ^ { 3 } + \cdot \cdot \cdot + L _ { N } \lambda ^ { N } + \cdot \cdot \cdot .
$$

The terms up to the Nth power of $\lambda$ are obtained by substituting for $_ z$ the first sum of the expression (l3c).Put

$$
\epsilon ^ { \prime } = \sum _ { j = 1 } ^ { N } \left( \sum _ { i = 0 } ^ { j } | a _ { j , j - 2 i } | \right) \lambda ^ { j } - \sum _ { j = 2 } ^ { N } L _ { j } \lambda ^ { j } ;
$$

then we obtain

$$
z = \epsilon ^ { \prime } + \epsilon z + h { \frac { ( 3 - 2 z ) z ^ { 2 } } { ( 1 - z ) ^ { 2 } } } \cdotp
$$

Writing

$$
\delta = \frac { \epsilon ^ { \prime } } { 1 - \epsilon } , \qquad g = \frac { h } { 1 - \epsilon } ,
$$

we have

$$
z = \delta + g { \frac { ( 3 - 2 z ) z ^ { 2 } } { ( 1 - z ) ^ { 2 } } } \cdotp
$$

As $\pmb { N }$ increases, the residual for this expression tends to the residual for the above series of $\pmb { \mathscr { p } }$ ， $q$ in powers of $\lambda$ ,provided that the same number of terms is taken.

Consider the expansion

$$
\delta = z + a _ { 2 } z ^ { 2 } + a _ { 3 } z ^ { 3 } + \cdot \cdot \cdot ,
$$

or by inverting

$$
z = \delta + b _ { 2 } \delta ^ { 2 } + b _ { 3 } \delta ^ { 3 } + \cdot \cdot \cdot .
$$

Let

$$
\delta = \gamma + \delta ^ { \prime } ( c ) ( z - c ) + \textstyle { \frac { 1 } { 2 } } \delta ^ { \prime \prime } ( c ) ( z - c ) ^ { 2 } + \cdot \cdot \cdot \qquad ( \gamma = \delta ( c ) ) ,
$$

or by inverting

$$
z = c + { \frac { 1 } { \delta ^ { \prime } ( c ) } } ( \delta - \gamma ) + \cdot \cdot \cdot \quad \quad ( \delta ^ { \prime } ( c ) \neq 0 ) .
$$

This is possible only if $\delta ^ { \prime } ( c ) \neq 0$ .The value of $\pmb { c }$ nearest to zero is the branch point of $\delta ( z )$ nearest to O.Hence the radius of convergence of $\delta ( z )$ at $z = 0$ is equal to such a value $| c |$ . Such values of $\pmb { c }$ and $\gamma$ can be

found from (14) and $d \delta ( z ) / d z = 0 \nonumber$ where $\ S ( z )$ is given by (14).Differentiating the above relation (l4) and putting $\delta ^ { \prime } ( z ) = 0$ at $z = c ,$ we obtain

$$
1 = \frac { 2 } { 1 - c } \left[ 3 g c + g \frac { ( 3 - 2 c ) c ^ { 2 } } { ( 1 - c ) ^ { 2 } } \right] .
$$

We can write $c - \gamma$ for the expression in the square bracket. Thus the equations for determining $\pmb { c }$ and $\gamma$ are

$$
c = \frac { 1 + \gamma } { 3 ( 1 + 2 g ) } , \qquad 2 g c = \frac { ( 1 - c ) ^ { 3 } } { 3 - 3 c + c ^ { 2 } } ,
$$

which give the branch point $\delta = \gamma$ for $| c | < 1$ .The second equation of (15) gives

$$
c = 1 - \sqrt [ 3 ] { \frac { 2 g } { 1 + 2 g } } .
$$

This is because we put $\lambda = M ^ { 2 }$ in the foregoing discussion. Hence $\epsilon$ and $h$ ，and accordingly $g$ and $2 g / ( 1 + 2 g )$ , are real and positive for $\epsilon < 1$ The three roots are given by

$$
c _ { k } = 1 - \sqrt [ 3 ] { \frac { 2 g } { 1 + 2 g } } \left( \cos \frac { 2 k \pi } { 3 } + \sqrt { - 1 } \sin \frac { 2 k \pi } { 3 } \right) ( k = 0 , 1 , 2 ) ,
$$

that is,

$$
\left| { \bf \tau } \right| = 1 - \sqrt [ 3 ] { \frac { 2 g } { 1 + 2 g } } , \qquad \left| { \epsilon _ { 1 , 2 } } \right| = \sqrt { 1 + \sqrt [ 3 ] { \frac { 2 g } { 1 + 2 g } } + \sqrt [ 3 ] { \left( \frac { 2 g } { 1 + 2 g } \right) ^ { 2 } } } .
$$

We see that the two complex roots are outside the circle $| z | = 1$ ,and the only real root is inside the circle.Hence it is sufficient to derive the only real solution of the cubic equation.In practice we must determine $M > 0$ such that the two equations (15） for $\pmb { c }$ and $\boldsymbol { g }$ are satisfied for $\epsilon < 1$ . Then Hil's series is convergent absolutely and uniformly for $| { \mathbf { m } } | \leq M$

Since computation shows that the circle of convergence is not essen-tially enlarged by large values of $N .$ ，we have only to consider $N = 2$

For $\mathbf { m } = M$ we have

$$
\left| a _ { 1 , 1 } \right| + \left| a _ { 1 , - 1 } \right| = \frac { 3 } { 8 } \frac { 2 2 + 2 0 M + 9 M ^ { 2 } } { 6 - 4 M + M ^ { 2 } } .
$$

From the definition of $\epsilon$ we have

$$
\epsilon = ( | a _ { 1 , 1 } | + | a _ { 1 , - 1 } | ) \lambda \qquad ( \mathbf { m } = M ) .
$$

Then

$$
\begin{array} { c } { { \epsilon ^ { \prime } = \epsilon + \cdot \cdot \cdot , \qquad \delta = \epsilon ^ { \prime } + \cdot \cdot \cdot = \epsilon + \cdot \cdot \cdot , } } \\ { { z = \delta + \cdot \cdot \cdot = \epsilon + \cdot \cdot \cdot , } } \end{array}
$$

where terms containing $\lambda ^ { 2 } , \lambda ^ { 3 } .$ ... are omitted. But we also have

$$
g = h + \cdot \cdot \cdot , \qquad \frac { 3 - 2 z } { ( 1 - z ) ^ { 2 } } = 3 + \cdot \cdot \cdot ,
$$

where terms containing $\lambda$ are omitted. If we omit terms with $\lambda ^ { 3 }$ ,then we obtain

$$
\epsilon z + h { \frac { ( 3 - 2 z ) z ^ { 2 } } { ( 1 - z ) ^ { 2 } } } = ( 1 + 3 h ) \epsilon ^ { 2 } + \cdot \cdot \cdot ,
$$

or

$$
L _ { 2 } \lambda ^ { 2 } = ( 1 + 3 h ) \epsilon ^ { 2 } .
$$

Putting $N = 2$ in the series (13d),we find

$$
\begin{array} { l } { { \epsilon ^ { \prime } = \epsilon + \epsilon _ { 1 } - L _ { 2 } \lambda ^ { 2 } = \epsilon + \epsilon _ { 1 } - ( 1 + 3 h ) \epsilon ^ { 2 } , } } \\ { { \epsilon _ { 1 } = ( | a _ { 2 , - 2 } | + | a _ { 2 , 0 } | + | a _ { 2 , 2 } | ) \lambda ^ { 2 } , } } \end{array}
$$

where

$$
\begin{array} { r c l } { { } } & { { } } & { { a _ { 2 , 2 } = \displaystyle \frac { \frac { 3 } { 2 } L A _ { 2 , - 2 } - [ 1 6 - 8 ( 1 + M ) + \frac { 3 } { 2 } L ] A _ { 2 , 2 } } { 8 ( 3 0 - 4 M + M ^ { 2 } ) } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { a _ { 2 , 0 } = \displaystyle - \frac { 1 } { 3 L } A _ { 2 , 0 } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { z _ { 2 , - 2 } = \displaystyle \frac { \frac { 3 } { 2 } L A _ { 2 , 2 } - [ 1 6 + 8 ( 1 + M ) + \frac { 3 } { 2 } L ] A _ { 2 , - 2 } } { 8 ( 3 0 - 4 M + M ^ { 2 } ) } , } } \end{array}
$$

and

$$
\begin{array} { r l } & { \quad A _ { 2 , 2 } = \frac { 3 } { 8 } L ( a _ { 1 , 1 } ^ { 2 } + 2 a _ { 1 , 1 } a _ { 1 , - 1 } + 5 a _ { 1 , - 1 } ^ { 2 } ) , } \\ & { \quad A _ { 2 , 0 } = \frac { 3 } { 2 } a _ { 1 , - 1 } + \frac { 3 } { 4 } L ( 6 a _ { 1 , 1 } a _ { 1 , - 1 } + a _ { 1 , 1 } ^ { 2 } + a _ { 1 , - 1 } ^ { 2 } ) , } \\ & { \quad A _ { 2 , - 2 } = \frac { 3 } { 2 } a _ { 1 , 1 } + \frac { 3 } { 8 } L ( a _ { 1 , - 1 } ^ { 2 } + 2 a _ { 1 , 1 } a _ { 1 , - 1 } + 5 a _ { 1 , 1 } ^ { 2 } ) , } \end{array}
$$

which are expressed in terms of $a _ { 1 , 1 }$ and $a _ { 1 , - 1 }$

By numerical calculation Merman found that the value of $M$ satisfying the two equations (15) for $\pmb { c }$ and $g$ lies between $M = 0 . 1 8 0$ and $M = 0 . 1 8 1$ and that the value of $_ z$ calculated by

$$
z = { \frac { 1 + 2 \delta } { 3 ( 1 + 2 g ) } }
$$

satisfies

$$
2 g z < \frac { ( 1 - z ) ^ { 3 } } { 3 - 3 z + z ^ { 2 } } \qquad \mathrm { f o r } \qquad M = 0 . 1 8 0
$$

and

$$
2 g z > \frac { ( 1 - z ) ^ { 3 } } { 3 - 3 z + z ^ { 2 } } \qquad \mathrm { f o r } \qquad M = 0 . 1 8 1 .
$$

Riabov (1962） derived a sharper bound $| { \bf m } | < 1 / \sqrt { 1 5 } = 0 . 2 5 8 . . .$ by Liapounov's method of majorant series. This is much sharper than Wintner's limit 1/l2,and even sharper than Petrovskaya's limit 0.21, which will be immediately shown by means of Wintner's method of infinite nonlinear analysis. Riabov started with the same equations as Liapounov and Merman did for the variables $\pmb { \mathscr { p } }$ and $q$ . Riabov wrote the equations (l3) in the form

$$
L ( \xi , \eta ) = \phi _ { 1 } ( \tau ) , ~ N ( \xi , \eta ) = \phi _ { 2 } ( \tau ) ,
$$

$$
\begin{array} { l } { { \displaystyle \phi _ { 1 } ( \tau ) = \sum _ { k = 0 } ^ { j } { [ A _ { k } \exp { \{ 2 k \sqrt { - 1 } ~ \tau \} } + A _ { - k } \exp { \{ - 2 k \sqrt { - 1 } ~ \tau \} } ] } } , }  \\ { { \displaystyle \phi _ { 2 } ( \tau ) = \phi _ { 1 } ( - \tau ) } , } \end{array}
$$

where $L , N$ are differential operators,and $\xi , \eta$ stand for $\ p , q$ Let the solution of (13e) be

$$
\begin{array} { l } { { \displaystyle \xi ( \tau ) = \sum _ { k = 0 } ^ { j } [ M _ { k } \exp \left\{ 2 k \sqrt { - 1 } \tau \right\} + M _ { - k } \exp \left\{ - 2 k \sqrt { - 1 } \tau \right\} ] , } } \\ { { \displaystyle \eta ( \tau ) = \xi ( - \tau ) , } } \end{array}
$$

where $M _ { 0 } = - A _ { 0 } / ( 3 l )$ and

$$
\begin{array} { c } { { \displaystyle { \alpha _ { k } { \cal A } _ { k } + \delta _ { k } { \cal A } _ { - k } , ~ { \cal M } _ { - k } = \delta _ { k } { \cal A } _ { k } + \gamma _ { k } { \cal A } _ { - k } + ~ ( k \ne 0 ) } } } \\ { { { } } } \\  { { \displaystyle { \alpha _ { k } = \frac { 1 } { \Delta _ { k } } \left[ - 4 k ^ { 2 } + 4 ( 1 + { \bf m } ) k - \frac { 3 } { 2 } l \right] , ~ \delta _ { k } = \frac { 3 } { 2 \Delta _ { k } } l , } } } \\ { { { } } } \\ { { \gamma _ { k } = \frac { 1 } { \Delta _ { k } } \left[ - 4 k ^ { 2 } - 4 ( 1 + { \bf m } ) k - \frac { 3 } { 2 } l \right] , } } \\ { { { } } } \\ { { \Delta _ { k } = 4 k ^ { 2 } \Big [ 4 k ^ { 2 } - 1 - 2 { \bf m } + \frac { 1 } { 2 } { \bf m } ^ { 2 } \Big ] . } } \end{array}
$$

We expand $\pmb { \mathscr { p } } , \pmb { q }$ of (13) in powers of $\lambda$ ,as in Liapounov's work:

$$
\dot { p } = \ p _ { 1 } \lambda + \ p _ { 2 } \lambda ^ { 2 } + \cdot \cdot \cdot , \qquad q = q _ { 1 } \lambda + q _ { 2 } \lambda ^ { 2 } + \cdot \cdot \cdot ;
$$

then, in the first approximation, we obtain

$$
\begin{array} { r l } & { L ( \boldsymbol { \gamma } , \boldsymbol { q } ) = \ - \frac { 3 } { 2 } \exp { \{ - 2 \sqrt { - 1 } \ \tau \} } , \qquad N ( \boldsymbol { \gamma } , \boldsymbol { q } ) = \frac { 3 } { 2 } \exp { \{ 2 \sqrt { - 1 } \ \tau \} } , } \\ & { \dot { p } _ { 1 } = a _ { 1 } \exp { \{ 2 \sqrt { - 1 } \ \tau \} } + a _ { - 1 } \exp { \{ - 2 \sqrt { - 1 } \ \tau \} } , } \\ & { q _ { 1 } = a _ { - 1 } \exp { \{ 2 \sqrt { - 1 } \ \tau \} } + a _ { 1 } \exp { \{ - 2 \sqrt { - 1 } \ \tau \} } , } \end{array}
$$

$$
a _ { 1 } = \mathrm { ~ - { \frac { 9 } { 1 6 } } ~ } { \frac { 2 \mathrm { ~ + ~ } 4 \mathrm { m } \mathrm { ~ + ~ } 3 \mathrm { m } ^ { 2 } } { 6 \mathrm { ~ - ~ } 4 \mathrm { m } \mathrm { ~ + ~ } \mathrm { m } ^ { 2 } } } , \qquad a _ { \mathrm { - 1 } } = { \frac { 3 } { 1 6 } } { \frac { 3 8 \mathrm { ~ + ~ } 2 8 \mathrm { m } \mathrm { ~ + ~ } 9 \mathrm { m } ^ { 2 } } { 6 \mathrm { ~ - ~ } 4 \mathrm { m } \mathrm { ~ + ~ } \mathrm { m } ^ { 2 } } } ,
$$

as in Merman's work.Riabov took

$$
\begin{array} { c } { { ^ { \prime } \dot { p } , q ) = \frac { 3 } { 2 } \lambda ( q - 1 ) \exp \{ - 2 \sqrt { - 1 } \tau \} + l ( R _ { p } ^ { ( 2 ) } + R _ { p } ^ { ( 3 ) } + R _ { p } ^ { ( 4 ) } + \bar { R } _ { p } ) , } } \\ { { ^ { \prime } \dot { p } , q ) = \frac { 3 } { 2 } \lambda ( \dot { p } - 1 ) \exp \{ 2 \sqrt { - 1 } \tau \} + l ( R _ { q } ^ { ( 2 ) } + R _ { q } ^ { ( 3 ) } + R _ { q } ^ { ( 4 ) } + \bar { R } _ { q } ) , } } \end{array}
$$

where $R _ { \mathcal { p } } ^ { ( j ) }$ are of the jth degree in ${ \pmb { \mathscr { p } } } , { \pmb q } ,$ and $\bar { \boldsymbol { R } } _ { p }$ are terms of degree higher than the fourth in ${ p , q , }$ and $R _ { q } ^ { ( j ) }$ and ${ \overrightarrow { R } } _ { q }$ are the same expressions with $\pmb { \mathscr { p } }$ and $\pmb q$ exchanged, that is, $R _ { p } ( p , q ) = R _ { q } ( q , p )$ ·

Higher approximations are obtained from

$$
\begin{array} { r } { L ( \boldsymbol { p } _ { \sigma } , \boldsymbol { q } _ { \sigma } ) = f _ { \sigma } ( \boldsymbol { p } _ { 1 } , \ldots , \boldsymbol { p } _ { \sigma - 1 } , \boldsymbol { q } _ { 1 } , \ldots , \boldsymbol { q } _ { \sigma - 1 } , \tau ) , } \\ { N ( \boldsymbol { p } _ { \sigma } , \boldsymbol { q } _ { \sigma } ) = \phi _ { \sigma } ( \boldsymbol { p } _ { 1 } , \ldots , \boldsymbol { p } _ { \sigma - 1 } , \boldsymbol { q } _ { 1 } , \ldots , \boldsymbol { q } _ { \sigma - 1 } , \tau ) , } \end{array}
$$

where

$$
\begin{array} { l } { { f _ { \sigma } = \frac { 3 } { 2 } g _ { \sigma - 1 } \exp \left\{ - 2 \sqrt { - 1 } \tau \right\} + l P _ { \sigma } , } } \\ { { \phi _ { \sigma } = \frac { 1 } { 2 } \hbar _ { \sigma - 1 } \exp \left\{ 2 \sqrt { - 1 } \tau \right\} + l Q _ { \sigma } . } } \end{array}
$$

Let

$$
f ( \tau ) = \sum _ { j = - k } ^ { k } B _ { j } \exp \{ j \sqrt { - 1 } \tau \} , \qquad | f | _ { * } = \sum _ { j = - k } ^ { k } | B _ { j } | ;
$$

then, sup $| f ( \tau ) | \leq | f | _ { * }$ . Hence,

$$
\begin{array} { l } { \displaystyle \lvert \eta \rvert _ { * } = \displaystyle \lvert \xi \rvert _ { * } \leq \displaystyle \sum _ { k = 0 } ^ { j } \left( \lvert M _ { k } \rvert + \lvert M _ { - k } \rvert \right) } \\ { \displaystyle \qquad \leq \rho ^ { ( j ) } \displaystyle \sum _ { k = 0 } ^ { j } \left( \lvert A _ { k } \rvert + \lvert A _ { - k } \rvert \right) = \rho ^ { ( j ) } \lvert \phi _ { 1 } \rvert _ { * } , } \end{array}
$$

where

$$
\begin{array} { r l r } & { } & { \rho ^ { ( j ) } = \operatorname* { m a x } \Big ( \lvert \alpha _ { k } \rvert + \lvert \delta _ { k } \rvert , \lvert \delta _ { k } \rvert + \lvert \gamma _ { k } \rvert , \frac { 1 } { 3 ( 1 - 2 \mathbf { m } + \frac { 3 } { 2 } \mathbf { m } ^ { 2 } ) } \Big ) } \\ & { } & { ( k = 0 , 1 , . . . , j ) , } \end{array}
$$

or

$$
\rho ^ { ( j ) } \triangleq \rho = | \delta _ { 1 } | + | \gamma _ { 1 } | = \frac { 8 + 4 \mathbf { m } + 3 l } { 4 ( 3 - 2 \mathbf { m } + \frac { 1 } { 2 } \mathbf { m } ^ { 2 } ) } .
$$

Thus

$$
\begin{array} { r l } & { | \hat { p } _ { \sigma } ( \tau ) | _ { * } \leq \rho [ \frac { 3 } { 2 } | q _ { \sigma - 1 } | _ { * } + l | P _ { \sigma } | _ { * } ] , } \\ & { | q _ { \sigma } ( \tau ) | _ { * } \leq \rho [ \frac { 3 } { 2 } | \hat { p } _ { \sigma - 1 } | _ { * } + l | Q _ { \sigma } | _ { * } ] , \qquad | \hat { p } _ { \sigma } | _ { * } = | q _ { \sigma } | _ { * } . } \end{array}
$$

We represent these equations by a single equation

$$
u = \lambda \beta _ { 1 } + \rho [ { \textstyle { \frac { 3 } { 2 } } } \lambda u + l U ( u ) ] ,
$$

where

$$
\beta _ { 1 } = | \beta _ { 1 } | _ { * } = | q _ { 1 } | _ { * } = | a _ { 1 } | + | a _ { - 1 } | = \frac { 3 } { 8 } \frac { 2 2 + 2 0 { \bf m } + 9 { \bf m } ^ { 2 } } { 6 - 4 { \bf m } + { \bf m } ^ { 2 } } ,
$$

$$
U ( u ) = ( 1 - u ) ^ { - 2 } - 1 - 2 u = 3 u ^ { 2 } + 4 u ^ { 3 } + 5 u ^ { 4 } + \cdot \cdot \cdot . .
$$

The solution of (16):

$$
u = \beta _ { 1 } \lambda + u _ { 2 } \lambda ^ { 2 } + u _ { 3 } \lambda ^ { 3 } + \cdot \cdot \cdot
$$

is majorized by

$$
\sum _ { \sigma = 1 } ^ { \infty } | / p _ { \sigma } | _ { * } \lambda ^ { \sigma } , \qquad \sum _ { \sigma = 1 } ^ { \infty } | q _ { \sigma } | _ { * } \lambda ^ { \sigma } .
$$

If $| { \ p } _ { 2 } | _ { * } = | q _ { 2 } | _ { * } = { \beta } _ { 2 } ,$ ,then (16) becomes

$$
u = \lambda \beta _ { 1 } + \lambda ^ { 2 } \beta _ { 2 } - \lambda ^ { 2 } u _ { 2 } + \rho [ \textstyle { \frac { 3 } { 2 } } \lambda u + l U ( u ) ] ,
$$

where

$$
\begin{array} { r } { u _ { 2 } = ( \frac { 3 } { 2 } \beta _ { 1 } + 3 l \beta _ { 1 } ^ { 2 } ) . } \end{array}
$$

Riabov considered up to the fourth degree terms with $\lambda ^ { 4 }$ ,and solved (16) up to the terms in $u ^ { 4 }$ with the form

$$
u = \alpha ^ { ( N ) } + \rho \cdot \sum _ { \rho + j = 1 } ^ { 4 } a _ { \sigma , j } ^ { ( N ) } u ^ { \sigma + j } + \rho l \overline { { U ^ { ( N ) } } } ( u ) ,
$$

where

$$
\begin{array} { r } { \overline { { U } } ( u ) = \bar { R } _ { p } ( \lambda | \phi _ { 1 } | _ { * } + u , \lambda | q _ { 1 } | _ { * } + u ) \quad } \\ { = 6 ( \lambda | \phi _ { 1 } | _ { * } + u ) ^ { 5 } + 7 ( \lambda | \phi _ { 1 } | _ { * } + u ) ^ { 6 } + \cdot \cdot \cdot . . } \end{array}
$$

Then by means of the majorant series Riabov estimated the bound $| { \bf m } | < \bar { 1 } / \sqrt { 1 5 } = 0 . 2 5 8 . .$ ：

Petrovskaya (l962) constructed a periodic solution of the first sort of Poincaré (Section 18.13) in the form of series in m for the satellite threebody problem and obtained the limit of convergence of the series in powers of $\mathbf { m }$ and in the mass ratio $\mu$ by Liapounov's method of majorization.

With $\mathbf { m } = n _ { 0 } / n , n = n _ { 1 } - n _ { 0 }$ the usual equations of motion in the rotating frame $( x , y )$ for an infinitesimal mass under the action of finite bodies with masses $m _ { 0 }$ and $m _ { 1 }$ in a circular motion of radius $a _ { 0 }$ with mean motion $n _ { 0 } = \sqrt { k ^ { 2 } ( m _ { 0 } + m _ { 1 } ) / a _ { 0 } ^ { 3 } }$ are written

$$
\begin{array} { r l } & { \frac { d ^ { 2 } u } { d \tau ^ { 2 } } + 2 \mathbf { m } \sqrt { - 1 } \frac { d u } { d \tau } - \mathbf { m } ^ { 2 } u + \frac { k ^ { 2 } m _ { 0 } } { \pi ^ { 2 } } u r _ { 1 } ^ { - 3 } } \\ & { \qquad \quad + \frac { k ^ { 2 } m _ { 1 } } { n ^ { 2 } } ( u - a _ { 0 } ) r _ { 2 } ^ { - 3 } + \frac { k ^ { 2 } m _ { 1 } } { a _ { 0 } ^ { 2 } n ^ { 2 } } = 0 , } \\ & { \frac { d ^ { 2 } v } { d \tau ^ { 2 } } - 2 \mathbf { m } \sqrt { - 1 } \frac { d v } { d \tau } - \mathbf { m } ^ { 2 } v + \frac { k ^ { 2 } m _ { 0 } } { n ^ { 2 } } v r _ { 1 } ^ { - 3 } } \\ & { \qquad \quad + \frac { k ^ { 2 } m _ { 1 } } { n ^ { 2 } } ( v - a _ { 0 } ) r _ { 2 } ^ { - 3 } + \frac { k ^ { 2 } m _ { 1 } } { a _ { 0 } ^ { 2 } n _ { 2 } } = 0 , } \end{array}
$$

where $u = x + { \sqrt { - 1 } } y , v = x - { \sqrt { - 1 } } y , r _ { 1 } ^ { 2 } = u v , r _ { 2 } ^ { 2 } = ( u - a _ { 0 } ) ( v -$ ao), $\tau = n ( t - t _ { 0 } )$ Putμ= m/m,k²mo/(n²a³)=1+2m +m² =l, $\pmb { u } = \pmb { a } ( 1 - \pmb { p } )$ exp{√-1 τ}, $v = a ( 1 - q ) \exp \left\{ - \sqrt { - 1 } \tau \right\}$ ； then the equations for $\ p , q$ are derived in the form (l3) of Liapounov's theory. Put $\alpha = \mathbf { m } ^ { 1 / 3 }$ ， $\lambda = \alpha ^ { 2 } = \mathbf { m } ^ { 2 / 3 }$ ,and

$$
l = 1 + 2 \alpha ^ { 3 } + { \frac { 3 } { 2 } } \alpha ^ { 6 } , \beta = \sqrt [ 3 ] { \frac { \mu } { 1 + \mu } } \left( 1 + 2 \alpha ^ { 3 } + { \frac { 3 } { 2 } } \alpha ^ { 6 } \right) ^ { - 1 / 3 } \alpha ^ { 2 } .
$$

To such equations Petrovskaya applied Poincaré's theory (Section 18.7) for the existence of periodic solutions.

The solution $\pmb { \mathscr { p } } ^ { ( 1 ) } , \pmb { q } ^ { ( 1 ) }$ for $\mu = 0$ is expanded in powers of $\lambda$ and $\pmb { \alpha }$ ：

$$
{ \hat { p } } ^ { ( 1 ) } = \sum _ { k = 1 } ^ { \infty } \rlap { / } p _ { k } ^ { ( 1 ) } \lambda ^ { k } \alpha ^ { k } , \qquad q ^ { ( 1 ) } = \sum _ { k = 1 } ^ { \infty } q _ { k } ^ { ( 1 ) } \lambda ^ { k } \alpha ^ { k } ,
$$

where

$$
\begin{array} { r } { \dot { p } _ { 1 } ^ { ( 1 ) } = a _ { 1 , 1 } \exp \left\{ 2 \sqrt { - 1 } \tau \right\} + a _ { 1 , - 1 } \exp \big \{ - 2 \sqrt { - 1 } \tau \big \} , } \\ { q _ { 1 } ^ { ( 1 ) } = a _ { 1 , 1 } \exp \big \{ - 2 \sqrt { - 1 } \tau \big \} + a _ { 1 , - 1 } \exp \big \{ 2 \sqrt { - 1 } \tau \big \} , } \end{array}
$$

and

$$
\begin{array} { l } { { q _ { k } ^ { ( 1 ) } = \displaystyle \sum _ { \sigma = 0 } a _ { k , k - 2 \sigma } \exp \left\{ - 2 ( k - 2 \sigma ) \sqrt { - 1 } ~ \tau \right\} ~ ( k = 1 , 2 , \dots , } } \\ { { } } \\ { { a _ { 1 , 1 } = - \displaystyle \frac { 9 } { 1 6 } \displaystyle \frac { 2 + 4 \alpha ^ { 3 } + 3 \alpha ^ { 6 } } { 6 - 4 \alpha ^ { 3 } + \alpha ^ { 6 } } , ~ a _ { 1 , - 1 } = \displaystyle \frac { 3 } { 1 6 } \displaystyle \frac { 3 8 + 2 8 \alpha ^ { 3 } + 9 \alpha ^ { 6 } } { 6 - 4 \alpha ^ { 3 } + \alpha ^ { 6 } } , } } \\ { { a _ { k , s } = \displaystyle \frac { \frac { 3 } { 2 } [ \mathscr { A } _ { k , - s } - [ 4 s ^ { 2 } - 4 ( 1 + \alpha ^ { 3 } ) s + \frac { 3 } { 2 } l ] \mathscr { A } _ { k , s } } { 2 s ^ { 2 } [ 2 ( 4 s ^ { 2 } - 1 ) - 4 \alpha ^ { 3 } + \alpha ^ { 6 } ] } , } } \\ { { } } \\ { { a _ { k , 0 } = - \displaystyle \frac { 1 } { 3 l } \mathscr { A } _ { k , 0 } ~ ( k = 2 , 3 , \dots ; s = \pm 1 , \pm 2 , \dots ) , } } \end{array}
$$

where $\mathcal { A } _ { k , s }$ is the coefficient of $\lambda ^ { k } \alpha ^ { k }$ exp $\{ \sqrt { - 1 } \ s \tau \}$ in the expansion of the right-hand members of (l3a),after substituting the above solution for $\pmb { \mathscr { p } } ^ { ( 1 ) } , \pmb { q } ^ { ( 1 ) }$ , in powers of $\lambda , \alpha$ with $\alpha = \mathbf { m } ^ { 1 / 3 }$ . Similarly the coefficients of $\mu ^ { 2 } , \mu ^ { 3 } , \ldots$ can be obtained. The coefficients $a _ { k , s } , \mathcal { A } _ { k , s }$ are further expanded in powers of $\beta$ ，so that the solution is of the form

$$
{ \dot { p } } ^ { ( 3 ) } = \sum _ { k = 1 } ^ { \infty } { \dot { p } } _ { k } ^ { ( 3 ) } \lambda ^ { k } , \qquad q ^ { ( 3 ) } = \sum _ { k = 1 } ^ { \infty } q _ { k } ^ { ( 3 ) } \lambda ^ { k } ,
$$

$$
{ p } _ { 1 } ^ { \left( 3 \right) } = \sum _ { r = 0 } ^ { \infty } { { \beta } ^ { r } } { \left( { \sum _ { s = - \tau - 3 } ^ { { r } + 1 } { { a } _ { 1 , \tau , s } } } \exp { \{ { \sqrt { - 1 } } \ s \tau \} } \right) } ,
$$

$$
q _ { 1 } ^ { ( 3 ) } = \sum _ { r = 0 } ^ { \infty } \beta ^ { r } \biggl ( \sum _ { s = - r - 1 } ^ { r + 3 } a _ { 1 , r , - s } \exp { \{ \sqrt { - 1 } s \tau \} } \biggr ) ,
$$

for example.

Petrovskaya referred to Liapounov's lemma and estimated the magnitude of the various coefficients. She obtained the bounds:

$$
\begin{array} { r l r } & { } & { | a _ { k , r , s } | \leq \mathbf { a } _ { k , r , s } = \frac { 3 \left( 1 + 2 \alpha _ { 0 } ^ { 3 } + \frac { 3 } { 2 } \alpha _ { 0 } ^ { 6 } \right) \left| \mathcal { A } _ { k , r , - s } \right| + ( 9 + 1 0 \alpha _ { 0 } ^ { 3 } + \frac { 9 } { 2 } \alpha _ { 0 } ^ { 6 } ) \left| \mathcal { A } _ { k , r , - s } \right| } { 4 - \alpha _ { 0 } ^ { 3 } } } \\ & { } & \\ & { } & { | a _ { k , s } | \leq \mathbf { a } _ { k , s } = \frac { 3 \left( 1 + 2 \alpha _ { 0 } ^ { 3 } + \frac { 3 } { 2 } \alpha _ { 0 } ^ { 6 } \right) \left| \mathcal { A } _ { k , - s } \right| + ( 1 9 + 1 4 \alpha _ { 0 } ^ { 3 } + \frac { 9 } { 2 } \alpha _ { 0 } ^ { 6 } ) \left| \mathcal { A } _ { k , - s } \right| } { 4 ( 6 - 4 \alpha _ { 0 } ^ { 3 } + \alpha _ { 0 } ^ { 6 } ) } } \end{array}
$$

with

$$
| \alpha ^ { 3 } | \le \alpha _ { 0 } ^ { 3 } \le 0 . 4 2 , \qquad \beta _ { 0 } = \sqrt [ 3 ] { \frac { \mu } { 1 + \mu } } \alpha _ { 0 } ^ { 2 } \biggl ( 1 - 2 \alpha _ { 0 } ^ { 3 } + \frac { 3 } { 2 } \alpha _ { 0 } ^ { 6 } \biggr ) ^ { - 1 / 3 } ,
$$

where $\mathcal { A } _ { k , r , s }$ is the coefficient of $\lambda ^ { k } \alpha ^ { k } \beta ^ { \tau } \exp \left\{ \sqrt { - 1 } \ s \tau \right\}$ in the expansion of the right-hand members of (13b) for $j = 3 ;$ ,after substituting the above solution for $\pmb { \phi } ^ { ( 3 ) } , \pmb { q } ^ { ( 3 ) } ;$ in powers of $\lambda , \alpha , \beta$

Petrovskaya considered the majorant series

$$
\begin{array} { r l } & { \displaystyle \sum _ { k = 1 } ^ { \infty } \left\{ \sum _ { r = 0 } ^ { \infty } \sum _ { s = - s _ { r _ { 1 } } } ^ { s _ { r _ { 2 } } } \mathbf { a } _ { k , r , s } \beta _ { 0 } ^ { r } \Big ( 1 - \frac { \alpha } { \alpha _ { 0 } } \Big ) ^ { - 1 } \right\} \lambda ^ { k } , } \\ & { \displaystyle \sum _ { k = 1 } ^ { \infty } \sum _ { s = - k } ^ { + k } \mathbf { a } _ { k , s } \lambda ^ { k } \alpha _ { 0 } ^ { k } \Big ( 1 - \frac { \alpha } { \alpha _ { 0 } } \Big ) ^ { - 1 } . } \end{array}
$$

She derived the bounds:

$$
0 \ \leq \ | { \bf m } | < M _ { 0 } = \mathrm { m i n } \ ( \lambda _ { 0 } ^ { 3 / 2 } , \alpha _ { 0 } ^ { 3 } ) , 0 \ \leq \mu = \mu _ { 0 } ,
$$

or

$$
0 \leq | { \bf m } | \leq 0 . 0 0 8 , 0 \leq \mu \leq 0 . 0 0 1 .
$$

The satellites of Mars, Uranus, Neptune, the satellites I, II, III, IV, V of Jupiter,and all satelites of Saturn satisfy the conditions.

Wintner (1925） proved the convergence of Hill's series for his variational curve,and the continuation of the cuspidal orbit for the maximum lunation (l928).The method of proof is based on the infinite nonlinear analysis, which will be discussed in Sections 20.9-20.13.Holder (1929) extended the theory to include the existence proof of periodic solutions on the basis of Lichtenstein's theory of nonlinear integrodifferential equations (Sections 20.4-20.6).

Consider a differential equation

$$
\frac { d w } { d z } = f ( z , w ) , ~ w ( 0 ) = 0 ,
$$

for which $f ( z , w )$ is developable in an integral power series

$$
f ( z , w ) = \sum _ { m = 0 } ^ { \infty } \sum _ { n = 0 } ^ { \infty } c _ { m n } z ^ { m } w ^ { n } ,
$$

such that

$$
| f ( z , w ) | < M
$$

in the interval $| z | < a$ $| w | < b$ .Then it has been proved by Lindelof (1899)and Wintner (1925a,1925b,1925c,1926,1956,1956a,1956b; cf. 1925d) that the radius of convergence of the series

$$
w ( z ) = \sum _ { n = 1 } ^ { \infty } a _ { n } w ^ { n }
$$

is not smaller than min $( a , b / M )$ . Wintner (1956) further proved that this series is the best majorant.

Putting

$$
u = \sum _ { i = - \infty } ^ { \infty } a _ { 2 i } \zeta ^ { 2 i + 1 } , \qquad s = \sum _ { i = - \infty } ^ { \infty } a _ { - 2 i - 2 } \zeta ^ { 2 i + 1 } 
$$

in Hill's equations (8) for the variational curve, we obtain after Hill

$$
\begin{array} { r } { \displaystyle \sum _ { i = - \infty } ^ { \infty } \bigg \{ ( 2 i + 1 ) ^ { 2 } + 4 ( 2 i + 1 ) \mathbf { m } + \frac { 9 } { 2 } \mathbf { m } ^ { 2 } \bigg \} a _ { 2 i } ^ { 2 } \qquad } \\ { \displaystyle + \frac { 9 } { 2 } \mathbf { m } ^ { 2 } \cdot \sum _ { i = - \infty } ^ { \infty } a _ { 2 i } a _ { - 2 i - 2 } = \frac { C } { 4 \mathbf { a } ^ { 2 } } , } \end{array}
$$

$$
( j = \pm 1 , \pm 2 , \ldots ) .
$$

Here $\pmb { a } _ { 2 j }$ are determined from the second equation and $a _ { 0 }$ from the first. Since $[ 2 j , 2 j ] = - 1$ and $[ 2 j , 0 ] = 0$ by definition,we obtain

$$
\begin{array} { c } { { \displaystyle { \partial a _ { 2 j } = \sum _ { i = - \infty } ^ { \infty } [ 2 j , 2 i ] a _ { 2 i } a _ { 2 i - 2 j } + [ 2 j , ] \sum _ { i = - \infty } ^ { \infty } a _ { 2 i } a _ { - 2 i + 2 j - 2 } } } } \\ { { + ~ ( 2 j , ) \sum _ { i = - \infty } ^ { \infty } a _ { 2 i } a _ { - 2 i - 2 j - 2 } \qquad ( j = \pm 1 , \pm 2 , . } } \end{array}
$$

where $\Sigma ^ { \prime }$ means to exclude $i = j , i = 0$ Substitute

$$
a _ { 0 } = b _ { 0 } , \qquad a _ { 2 i } = { \bf m } { \frac { b _ { i } } { i ^ { 4 } } } a _ { 0 } \qquad ( i \ne 0 ) ;
$$

then the second equation (16a) is transformed to (in Wintner's notation in his theory of infinite nonlinear analysis,which will be treated in Sections 20.9-20.15):

$$
{ \begin{array} { r l } { \mathbf { \Phi } } & { = \mathbf { m } f _ { j } ( \mathbf { m } ; b _ { 1 } , b _ { - 1 } , b _ { 2 } , b _ { - 2 } , . . . ) \qquad ( j = \pm 1 , \pm 2 , . . . ) , } \\ { \mathbf { \Phi } } & { = \{ g _ { 1 j } + g _ { 2 j } + \mathbf { m } g _ { 3 j } + \mathbf { m } g _ { 4 j } + \mathbf { m } ^ { 2 } g _ { 5 j } } \\ & { \qquad + g _ { 6 j } + g _ { 7 j } + \mathbf { m } g _ { 8 j } + \mathbf { m } g _ { 9 j } + \mathbf { m } ^ { 2 } g _ { 1 0 , j } + \mathbf { m } ^ { 2 } g _ { 1 1 , j } \} } \\ & { \qquad \quad \qquad \quad \qquad \qquad \qquad \div \left[ 1 - { \frac { 4 \mathbf { m } - \mathbf { m } } { 8 j ^ { 2 } - 2 } } \right. } \end{array} }
$$

where

$$
\begin{array} { l } { { g _ { 1 j } = - { \displaystyle \frac { 2 ( j - 1 ) } { 4 j ^ { 2 } - 1 } } \cdot { \displaystyle \sum _ { i = - \infty } ^ { \infty } } , { \displaystyle \frac { 1 } { ( i - j ) ^ { 2 } } } { \displaystyle \frac { j ^ { 2 } } { i ^ { 2 } ( i - j ) ^ { 2 } } } b _ { i } b _ { i - j } , } } \\ { { \mathrm { } } } \\ { { g _ { 2 j } = - { \displaystyle \frac { 2 j ^ { 2 } + 2 j - 1 } { 4 j ^ { 2 } - 1 } } \cdot { \displaystyle \sum _ { i = - \infty } ^ { \infty } } { \displaystyle \frac { 1 } { i - j } } { \displaystyle \frac { j ^ { 3 } } { i ^ { 3 } ( i - j ) ^ { 3 } } } b _ { i } b _ { i - j } , } } \\ { { \cdot \cdot \cdot , } } \\ { { g _ { 6 j } = - { \displaystyle \frac { 3 } { 1 6 } } { \displaystyle \frac { 2 j ^ { 2 } - 4 j - 1 } { j ^ { 2 } ( 4 j ^ { 2 } - 1 ) } } \cdot { \displaystyle \sum _ { i = - \infty } ^ { \infty } } j ^ { 4 } { \displaystyle \frac { a _ { 2 i } a _ { - 2 i + 2 j + 2 } } { a _ { 2 i } + a _ { 0 } } } , } } \end{array}
$$

or, in general,

$$
g _ { l j } = g _ { l j } ( b _ { 1 } , b _ { - 1 } , b _ { 2 } , b _ { - 2 } , \ldots ) \qquad ( 1 \leq l \leq 1 1 , j \neq 0 ) .
$$

The functions $g _ { l j }$ are quadratic in an infinite number of variables $b _ { 1 } , b _ { - 1 } , b _ { 2 } , \dotsc$ Denote the majorant 一 that is, the series obtained by writing the absolute values for all coefficients in the series - of $g _ { l j }$ by $\overline { { g _ { l j } } }$ ; then the sequences

$$
\{ \overline { { g _ { 1 j } } } ( 1 , 1 , 1 , . . . ) \} , \{ \overline { { g _ { 2 j } } } ( 1 , 1 , 1 , . . . ) \} , . . . , \{ \overline { { g _ { 1 1 , j } } } ( 1 , 1 , 1 , . . . ) \} 
$$

are bounded. In fact,

$$
\left\{ { \frac { 2 j ^ { 2 } } { 4 j ^ { 2 } - 1 } } \right\} \quad { \mathrm { a n d } } \quad \left\{ \sum _ { i = - \infty } ^ { \infty } { ' } { \frac { 1 } { ( i - j ) ^ { 2 } } } { \frac { j ^ { 2 } } { i ^ { 2 } ( i - j ) ^ { 2 } } } \right\}
$$

are both bounded, the latter because

$$
\left\{ \sum _ { i = - \infty } ^ { \infty } ^ { \prime } \frac { 1 } { ( i - j ) ^ { 2 } } \frac { j ^ { 2 } } { i ^ { 2 } ( i - j ) ^ { 2 } } \right\} < j ^ { 2 } \sum _ { i = - \infty } ^ { \infty } ^ { \prime } \frac { 1 } { i ^ { 2 } ( i - j ) ^ { 2 } } < j ^ { 2 } . O \left( \frac { 1 } { j ^ { 2 } } \right) .
$$

Furthermore,

$$
| 4 \mathbf { m } - \mathbf { m } ^ { 2 } | \leq 4 | \mathbf { m } | + | \mathbf { m } ^ { 2 } | < 6 ,
$$

if there exists a δ such that $| { \bf m } | \leq 1 + \delta .$ Hence

$$
\left[ 1 - \frac { 4 \mathbf { m } - \mathbf { m } ^ { 2 } } { 8 j ^ { 2 } - 2 } \right] ^ { - 1 }
$$

is regular and uniformly bounded. Let the common upper bound be $G$ Expand this fraction in the form

$$
\sum _ { p = 0 } ^ { \infty } c _ { v j } { \bf m } ^ { v } \qquad ( j = \pm 1 , \pm 2 , . . . ) ;
$$

then we have by Cauchy's theorem,

$$
| c _ { v j } | \leq \frac { G } { ( 1 - \delta ) ^ { \upsilon } }
$$

and

$$
\sum _ { \nu = 0 } ^ { \infty } | c _ { \nu j } | \leq G \cdot \sum _ { \nu = 0 } ^ { \infty } \frac { 1 } { ( 1 - \delta ) ^ { \nu } } \cdot
$$

Substitute this in $f _ { j }$ ; then $f _ { j }$ can be formall arranged in an ascending power series of an infinite number of variables $\mathbf { m }$ ， $b _ { 1 } , b _ { - 1 } , b _ { 2 } , . . . \mathrm { L e t } \overline { { f _ { j } } }$ be the best majorant of $f _ { j }$ ; then we see that $\{ \overline { { f } } _ { \mathfrak { s } } ( 1 ; 1 , 1 , \ldots ) \}$ is bounded. Denote the upper bound of this sequence by $\kappa$ ; then

$$
\mathbf { m } < \operatorname* { m i n } { ( 1 , K ^ { - 1 } ) } ,
$$

and $b _ { j }$ is defined as a regular function of $\mathbf { m }$ ，such that $| b _ { j } ( \mathbf { m } ) | \leq 1$ Hence the coefficients $b _ { j } .$ ，and accordingly $\pmb { a _ { 2 j } }$ ，determine the set of periodic solutions $\pmb { u }$ and ${ \pmb S } .$ Thus

$$
f _ { j } = f _ { j } ( x ; y _ { 1 } , y _ { 2 } , . . . )
$$

is a power series of an infinite number of variables. Let $\overline { { \mathcal { f } _ { j } } }$ be its majorant and assume that there exist $a > 0 , b > 0 , M > 0 _ { : }$ ，such that

$$
\overline { { { f } } } _ { j } ( a ; b , b , \ldots ) \ : \equiv \ : M \qquad ( j = 1 , 2 , \ldots ) \ : ;
$$

that is, the series for $f _ { j }$ is convergent at all points such that

$$
| x | \leq a , \qquad | y _ { 1 } | \leq b , \qquad | y _ { 2 } | \leq b ,
$$

Then the equation

$$
y _ { j } = x { \overline { { f } } } _ { j }
$$

can be solved at all points $| x | \le \alpha , \alpha = \operatorname* { m i n } \left( a , b / M \right) ( a > 0 , b > 0 ,$ $M > 0$ ),in the form of a continuous power series

$$
y _ { j } = y _ { j } ( x ) \qquad ( j = 1 , 2 , . . . ) ,
$$

with

$$
\vert \bar { y } _ { j } \vert \ \triangleq b , \qquad y _ { j } ( 0 ) = 0 .
$$

Wintner (l929) obtained a further estimate for the convergence. Put

$$
F _ { j } = f _ { j } \phi _ { j } = \Phi _ { j } + \Psi _ { j } + \Lambda _ { j } ,
$$

where

$$
\begin{array} { l } { { \displaystyle { \phi _ { j } = 1 - \frac { 4 { \bf m } - { \bf m } ^ { 2 } } { 2 ( 4 j ^ { 2 } - 1 ) } } , ~ a _ { 2 j } = { \bf m } a _ { 0 } \frac { b _ { j } } { j ^ { 2 } } , } } \\ { { \displaystyle { \omega _ { j } = \sum _ { \stackrel { i = - \infty } { i \ne j } } ^ { \infty } [ 2 j , 2 i ] \cdot \frac { 1 } { i ^ { 2 } ( j - i ) ^ { 2 } } b _ { i } b _ { i - j } } , } } \end{array}
$$

$$
\begin{array} { r } { \psi _ { j } = [ 2 j , ] \frac { j ^ { 2 } } { 1 0 ^ { 2 } } \cdot \displaystyle \sum _ { i = - \infty } ^ { \infty } \frac { a _ { 2 i } a _ { - 2 i + 2 j - 2 } } { a _ { 0 } ^ { 2 } } , } \\ { \lambda _ { j } = ( 2 j , ) \frac { j ^ { 2 } } { 1 0 ^ { 2 } } \cdot \displaystyle \sum _ { i = - \infty } ^ { \infty } \frac { a _ { 2 i } a _ { - 2 i - 2 j - 2 } } { a _ { 0 } ^ { 2 } } , } \end{array}
$$

$$
\Phi _ { j } = \phi _ { j } \omega _ { j } , \qquad \Psi _ { j } = \omega _ { j } \psi _ { j } , \qquad \Lambda _ { j } = \omega _ { j } \lambda _ { j } .
$$

From the inequalities

$$
\sum _ { \mathfrak { z } = \infty } ^ { \infty } \prime \frac { 1 } { ( i - j ) ^ { 2 } } < \frac { 1 0 } { 3 } , \qquad \sum _ { \mathfrak { i } = - \infty } ^ { \infty } \frac { j ^ { 2 } } { i ^ { 2 } ( j - i ) ^ { 2 } } < 1 7 , \qquad \overline { { \omega _ { j } ^ { - 1 } } } \Big ( \frac { 1 } { 1 2 } \Big ) \leq \frac { 1 6 } { 1 5 } ,
$$

where $\overline { { { \omega _ { j } ^ { - 1 } } ( \mathbf { m } ) } }$ is the best majorant of the Maclaurin series for $1 / \omega _ { j } ( \mathbf { m } )$ ， Wintner proved at first that the best majorant of $\Phi _ { j } ( \mathbf { m } ; b _ { 1 } , b _ { - 1 } , b _ { 2 } , . . . )$ for $\mathbf { m } = 1 / 1 2 , b _ { 1 } = b _ { - 1 } = b _ { 2 } = b _ { - 2 } = \cdot \cdot \cdot = 1 / 3$ is

$$
\begin{array} { r } { \Phi _ { j } ( \frac { 1 } { 1 2 } ; \frac { 1 } { 3 } , \frac { 1 } { 3 } , \dots ) < 2 + \frac { 1 } { 5 } . } \end{array}
$$

By writing

$$
\begin{array} { r } { \tiny : - \frac { 3 { \bf m } ^ { 2 } } { 1 6 } \frac { 4 j ^ { 2 } - 8 j - 2 - 4 ( j + 2 ) { \bf m } - 9 { \bf m } ^ { 2 } } { 2 ( 4 j ^ { 2 } - 1 ) } \qquad } \\ { \times \displaystyle \sum _ { i = 0 , j = 1 } ^ { \infty } \frac { b _ { i } b _ { - i + j - 1 } } { i ^ { 2 } ( - i + j - 1 ) ^ { 2 } } , } \end{array}
$$

he proved that

$$
\mathsf { F } _ { j } - \Psi _ { j } ^ { * } = - \frac { 3 \mathbf { m } ^ { 2 } } { 1 6 } \frac { 4 j ^ { 2 } - 8 j - 2 - 4 ( j + 2 ) \mathbf { m } - 9 \mathbf { m } ^ { 2 } } { 2 ( 4 j ^ { 2 } - 1 ) } \frac { a _ { 2 j - 2 } } { a _ { 0 } } \frac { 2 } { \mathbf { m } ^ { 2 } } .
$$

From the inequalities

$$
\left| \frac { 4 j ^ { 2 } - 8 j - 2 } { 2 ( 4 j ^ { 2 } - 1 ) } \right| \leq \frac { 5 } { 3 } , \qquad \left| \frac { - 4 ( j + 2 ) { \bf m } } { 2 ( 4 j ^ { 2 } - 1 ) } \right| \leq \frac { 1 } { 6 } , \qquad \left| \frac { - 9 { \bf m } ^ { 2 } } { 2 ( 4 j ^ { 2 } - 1 ) } \right| \leq \frac { 3 } { 9 }
$$

and

$$
\sum _ { i = - \infty } ^ { \infty } \stackrel { \prime \prime } { = } \frac { \left| b _ { i } b _ { - i + j - 1 } \right| } { i ^ { 2 } ( - i + j - 1 ) ^ { 2 } } < \frac { 1 } { 2 } ,
$$

he derived

$$
\overline { { \Psi _ { j } ^ { * } } } ( \textstyle { \frac { 1 } { 1 2 } } ; \frac { 1 } { 3 } , \frac { 1 } { 3 } , \ldots ) < \frac { 1 } { 6 0 0 } .
$$

Thus the best majorant of $\Psi _ { j } - \Psi _ { j } ^ { * }$ for $j \neq 1$ $1 , | { \bf m } | < \frac { 1 } { 1 2 } , | b _ { j - 1 } | \le 1 / 3$ has been seen to be smaller than $1 / 3 2$ ,because of the relations

$$
\frac { a _ { 2 j - 2 } } { a _ { 0 } } = { \bf { m } } \frac { { b _ { j - 1 } } } { { ( j - 1 ) ^ { 2 } } } , \qquad \frac { 1 } { { ( j - 1 ) ^ { 2 } } } \equiv 1 .
$$

Hence, we find that

$$
\overline { { \Psi _ { j } } } ( \textstyle { \frac { 1 } { 1 2 } } ; \frac { 1 } { 3 } , \frac { 1 } { 3 } , \frac { 1 } { 3 } , \dots ) < \frac { 1 } { 1 0 } .
$$

For $j = 1$ ,we have

$$
\begin{array} { r } { | \Psi _ { 1 } - \Psi _ { 1 } ^ { * } | < \frac { 3 } { 4 } - \frac { 1 } { 6 0 0 } , \qquad \overline { { \Psi } } _ { 1 } ( \frac { 1 } { 1 2 } ; \frac { 1 } { 3 } , \frac { 1 } { 3 } , . . . ) < \frac { 3 } { 4 } . } \end{array}
$$

Next, write

$$
\begin{array} { r } { - \frac { 3 \mathbf { m } ^ { 2 } } { 1 6 } . \frac { 2 0 j ^ { 2 } - 1 6 j + 2 \mathbf { \delta } - 4 ( 5 j - 2 ) \mathbf { m } + 9 \mathbf { m } ^ { 2 } } { 2 ( 4 j ^ { 2 } - 1 ) } \qquad } \\ { \times \displaystyle { \sum _ { i = - \infty \atop i \ne 0 , - \infty } ^ { \infty } } \frac { b _ { i } b _ { - i - j - 1 } } { i ^ { 2 } ( - i - j - 1 ) ^ { 2 } } \vdots } \end{array}
$$

then,

$$
\Lambda _ { j } ^ { * } = - \frac { 3 { \bf m } ^ { 2 } } { 1 6 } \frac { 2 0 j ^ { 2 } - 1 6 j + 2 - 4 ( 5 j - 2 ) { \bf m } + 9 { \bf m } ^ { 2 } } { 2 ( 4 j ^ { 2 } - 1 ) } \frac { a _ { - 2 j - 2 } } { a _ { 0 } } \frac { 2 } { { \bf m } ^ { 2 } } .
$$

From the inequalities

$$
\left| \frac { 2 0 j ^ { 2 } - 1 6 j + 2 } { 2 ( 4 j ^ { 2 } - 1 ) } \right| \le 6 + \frac { 6 } { 1 8 } , \qquad \left| \frac { - 4 ( 2 j - 2 ) } { 2 ( 4 j ^ { 2 } - 1 ) } \right| \le \frac { 7 } { 1 8 } ,
$$

$$
\left| \frac { 9 } { 2 ( 4 j ^ { 2 } - 1 ) } \right| \leq \frac { 1 } { 1 8 } ,
$$

we obtain

$$
\begin{array} { r l } {  { \overline { { \Lambda _ { j } ^ { * } } } ( \frac { 1 } { 1 2 } ; \frac { 1 } { 3 } , \frac { 1 } { 3 } , \frac { 1 } { 3 } , \ldots ) } \quad } & { } \\ & { \leq \frac { 3 } { 1 6 } \frac { 1 } { 1 4 4 } ( 6 + \frac { 6 } { 1 8 } + \frac { 7 } { 1 8 } + \frac { 1 } { 1 8 } ) \cdot \sum _ { i \neq 0 , - \infty \atop i \neq 0 , - j - 1 } ^ { \infty } \frac { 1 / 9 } { i ^ { 2 } ( - i - j  } } \\ & { <  \frac { 3 } { 1 6 } \frac { 1 } { 1 4 4 } \frac { 7 } { 9 } \sum _ { i = 1 } ^ { \infty } \frac { 2 } { i ^ { 2 } } < \frac { 1 } { 1 0 0 } . } \end{array}
$$

For $j \neq 1$ ，we see by the definition of $b _ { j }$ that the best majorant of $\Lambda _ { j } \ : - \ : \Lambda _ { j } ^ { * }$ for all $j \neq - 1$ is

$$
\begin{array} { r } { | \Lambda _ { j } - \Lambda _ { j } ^ { * } | < \frac { 3 } { 1 6 } ( 6 + \frac { 7 } { 1 8 } + \frac { 1 } { 1 8 } ) \frac { 1 } { 1 2 } \frac { 1 } { 3 } 2 < \frac { 1 } { 1 2 } } \end{array}
$$

for $| { \bf m } | < 1 / 1 2 , | b _ { - j - 1 } | \le 1 / 3 . \mathrm { F o r } j = - 1$ we have

$$
\begin{array} { r } { | \Lambda _ { - 1 } - \Lambda _ { - 1 } ^ { * } | < \frac { 3 } { 1 6 } ( 6 + \frac { 7 } { 1 8 } + \frac { 1 } { 1 8 } ) 2 = \frac { 9 } { 4 } + \frac { 1 } { 6 } . } \end{array}
$$

Thus,

$$
\overline { { { \Lambda _ { 1 } } } } ( { \scriptstyle { \frac { 1 } { 1 2 } } } ; { \frac { 1 } { 3 } } , { \frac { 1 } { 3 } } , \cdot \cdot \cdot ) < 2 + { \scriptstyle { \frac { 1 } { 4 } } } + { \frac { 1 } { 6 } } + { \scriptstyle { \frac { 1 } { 1 0 0 } } } ,
$$

and

$$
F _ { j } ( \textstyle { \frac { 1 } { 1 2 } } ; \frac { 1 } { 3 } , \frac { 1 } { 3 } , \ldots ) < \frac { 1 } { 1 2 } + \frac { 1 } { 1 0 0 } ( j \neq - 1 ) .
$$

Accordingly,

$$
\begin{array} { r l } { \overline { { F _ { 1 } } } ( \frac { 1 } { 1 2 } ; \frac { 1 } { 3 } , \frac { 1 } { 3 } , \ldots ) < ( 2 + \frac { 1 } { 5 } ) + \frac { 3 } { 4 } + ( \frac { 1 } { 1 2 } + \frac { 1 } { 1 0 0 } ) , } & { } \\ { \overline { { F _ { - 1 } } } ( \frac { 1 } { 1 2 } ; \frac { 1 } { 3 } , \frac { 1 } { 3 } , \ldots ) < \frac { 1 } { 2 } + \frac { 1 } { 1 0 } + ( \frac { 9 } { 4 } + \frac { 1 } { 6 } + \frac { 1 } { 1 0 0 } ) , } & { } \\ { \overline { { F _ { j } } } ( \frac { 1 } { 1 2 } ; \frac { 1 } { 3 } , \frac { 1 } { 3 } , \ldots ) < ( 2 + \frac { 1 } { 5 } ) + \frac { 1 } { 1 0 } + ( \frac { 1 } { 1 2 } + \frac { 1 } { 1 0 0 } ) } & { ( | j | > 1 ) . } \end{array}
$$

Hence,

$$
\overline { { { F _ { j } } } } ( { \scriptstyle { \frac { 1 } { 1 2 } } } ; { \frac { 1 } { 3 } } , { \frac { 1 } { 3 } } , \ldots ) < 3 + { \scriptstyle { \frac { 3 } { 4 } } } = { \scriptstyle { \frac { 1 5 } { 4 } } } \qquad ( j = \pm 1 , \pm 2 , \ldots ) ,
$$

and

$$
\overline { { { f } } } _ { j } ( \frac { 1 } { 1 2 } ; \frac { 1 } { 3 } , \frac { 1 } { 3 } , \ldots ) < 4 \qquad ( j = \pm 1 , \pm 2 , \ldots ) .
$$

Thus Wintner obtained the result that, if we consider a sequence of power series $\{ f _ { j } ( \xi ; \eta _ { 1 } , \eta _ { - 1 } , . . . ) \} , j = \pm 1 , \pm 2 , . . . ,$ such that

$$
\overline { { f } } _ { j } ( A ; B , B , \ldots ) \ : \cong \ : M
$$

with $A > 0 , B > 0 , M > 0$ ,then the system of infinitely many implicit equations

$$
\eta _ { j } = \xi f _ { j } \qquad ( j = \pm 1 , \pm 2 , . . . ) ,
$$

admits the solution $\eta _ { j } = \eta _ { j } ( \xi )$ ，which is holomorphic at $\xi = 0$ ina sufficiently small circle $| \xi | < \alpha$ with

$$
\alpha = \operatorname* { m i n } { ( A , B / M ) } ,
$$

and which is such that $| \eta _ { j } ( \xi ) | < B$ for $| \xi | < \alpha$ Put $A = 1 / 1 2 , B = 1 / 3$ ； then

$$
\overline { { f _ { j } } } ( \textstyle { \frac { 1 } { 1 2 } } ; \frac { 1 } { 3 } , \frac { 1 } { 3 } , \ldots ) < 4 ,
$$

and $M = 4 , B / M = 1 / 1 2$ ; that is, $\alpha = 1 / 1 2$ . Hence the equations

$$
b _ { j } = { \bf m } f _ { j } ( { \bf m } ; b _ { 1 } , b _ { - 1 } , b _ { 2 } , b _ { - 2 } , \ldots ) \qquad ( j = \pm 1 , \pm 2 , \ldots )
$$

admit the solution $b _ { j } = b _ { j } ( \mathbf { m } ) < 1 / 3$ ，which is holomorphic for $\mathbf { m } = 0$ and for $| { \bf m } | < 1 / 1 2 .$ According to Poincaré (1905; Section 11.2), $b _ { j } ( \mathbf { m } )$ is of the order $\mathbf { m } ^ { | j | }$ .Hence we have, by Schwarzschild's lemma, that

$$
| b _ { j } ( \mathbf { m } ) | < \frac { | \mathbf { m } | ^ { | j | } } { 1 2 ^ { | j | } }
$$

for $\mathbf { m } < 1 / 1 2 .$ Consequently

$$
\sum _ { j = 1 } ^ { \infty } \{ | a _ { 2 j } ( \mathbf { m } ) | + | a _ { - 2 j } ( \mathbf { m } ) | \}
$$

is convergent for $| { \bf m } | < 1 / 1 2$ . This is Wintner's radius of convergence of Hill's series.

On this ground Wintner (l928） again discussed the possibility of continuing Hill's periodic orbit beyond the maximum lunation.As has just been proved, there exists a constant $\Omega$ such that

$$
\overline { { { g _ { l j } } } } ( 1 , 1 , 1 , \ldots ) < \Omega .
$$

Since $g _ { l j }$ contain only terms of degree lower than or equal to 2 either with respect to m or with respect to $b _ { j } ,$ there exist two positive numbers $A > 0$ and $B > 0$ ,by the condition for homogeneity,such that

$$
\overline { { { g _ { l j } } } } ( A ; B , B , \ldots ) < ( 1 + A + A ^ { 2 } ) ( 1 + B + B ^ { 2 } ) \Omega .
$$

By putting

$$
\phi _ { j } = \phi _ { j } ( \mathbf { m } ) = 1 + \frac { \psi ( \mathbf { m } ) } { 8 j ^ { 2 } - 2 } , \psi ( \mathbf { m } ) = \mathbf { m ^ { 2 } } - 4 \mathbf { m } ,
$$

Wintner proved that $| \psi ( \mathbf { m } ) | < 1 1 / 2$ for $1 \leq m \leq 5$ ，Hence， from $8 j ^ { 2 } - 2 \geq 6 .$ ，we obtain

$$
\begin{array} { r } { | \phi _ { j } ( \mathbf { m } ) | > \frac { 1 } { 1 2 } . } \end{array}
$$

Since ${ F } _ { j } = { f } _ { j } \phi _ { j }$ is the sum of the polynomials $g _ { l j s }$ we have

$$
{ \bf 4 } ; B , B , \ldots \rangle < \Lambda ( A , B ) \nonumber
$$

This upper bound of $F _ { j } { \mathrm { : } }$ ,together with the lower bound 1/12 of $| \phi _ { j } ( \mathbf { m } ) |$ ， proves the existence of the series $f _ { j }$

Choose $\hat { \mathbf { m } } \gtrapprox 0$ such that $0 < \hat { \mathbf { m } } < M _ { \ast }$ and consider m in the circle $| \mathbf { m } - \hat { \mathbf { m } } | \leqq A ^ { ( 0 ) }$ where $\pmb { A } ^ { ( 0 ) }$ is so small that $| \phi _ { j } ( \mathbf { m } ) | < 1 / 1 2$ holds also for $A = 2 A ^ { ( 0 ) }$ . Expanding $\phi _ { j } ( \mathbf { m } )$ about the value $\hat { \mathbf { m } }$ , we obtain

$$
\overline { { \mathbf { n } ) } } = \frac { 1 } { \phi _ { j } ( \hat { \mathbf { m } } + \mathbf { m } - \hat { \mathbf { m } } ) } = \hat { h } _ { j } ( \mathbf { m } - \hat { \mathbf { m } } ) = \sum _ { n = 0 } ^ { \infty } c _ { n } ^ { ( j ) } ( \hat { \mathbf { m } } ) \cdot ( \mathbf { m } - \hat { \mathbf { m } } ) ^ { \mathrm { { T } } }
$$

where $\hat { h } _ { j } ( \mu )$ is regular and smaller than l2 in absolute value for $| \mu | \leqq$ ${ \bf 2 } A ^ { ( 0 ) }$ . Hence, from Cauchy's theorem,

$$
\vert c _ { n } ^ { ( j ) } \vert < { \frac { 1 2 } { ( 2 A ^ { ( 0 ) } ) ^ { n } } } \cdotp
$$

Thus,

$$
\hat { h } _ { j } ( A ^ { ( 0 ) } ) = \sum _ { n = 0 } ^ { \infty } | c _ { n } ^ { ( j ) } | ( A ^ { ( 0 ) } ) ^ { n } < 1 2 \cdot \sum _ { n = 0 } ^ { \infty } \frac { 1 } { 2 ^ { n } } = 2 4 , ~ 0 \le \hat { \bf m } \le M .
$$

The polynomial $F _ { j } ( { \bf m } ; b _ { 1 } , b _ { - 1 } , b _ { 2 } , b _ { - 2 } , . . . )$ is bounded. Therefore, if we take

$$
\begin{array} { c } { { \vert \widehat { b } _ { j } \vert \le B ( > 0 ) ( j = \pm 1 , \pm 2 , \ldots ) , } } \\ { { { \widehat { F } } _ { j } ( \mathbf { m } - \hat { \mathbf { m } } ; b _ { 1 } - \widehat { b } _ { 1 } , b _ { - 1 } - \widehat { b } _ { - 1 } , \ldots ) = F _ { j } ( \mathbf { m } ; b _ { 1 } , b _ { - 1 } , \ldots ) , } } \end{array}
$$

then we obtain

$$
\tilde { F } _ { j } ( A ^ { \scriptscriptstyle ( 0 ) } ; 2 B , 2 B , \ldots ) \le \Lambda ( A ^ { \scriptscriptstyle ( 0 ) } + M ; 3 B ) ,
$$

because

$$
| b _ { j } - \hat { b } _ { j } | \leq 2 B , \qquad | b _ { j } - \hat { b } _ { j } | + | \hat { b } _ { j } | \leq 3 B .
$$

Hence,

$$
\begin{array} { r l } { \mathbf { n } - \hat { \mathbf { m } } ; b _ { 1 } - \hat { b _ { 1 } } , b _ { - 1 } - \hat { b } _ { - 1 } , . . . ) } & { } \\ & { \qquad = f _ { j } ( \mathbf { m } - \hat { \mathbf { m } } + \hat { \mathbf { m } } ; b _ { 1 } - \hat { b _ { 1 } } + \hat { b _ { 1 } } , . . . ) } \\ & { \qquad = f _ { j } ( \mathbf { m } ; b _ { 1 } , . . . ) = \frac { F _ { j } ( \mathbf { m } ; b _ { 1 } , . . . ) } { \phi _ { j } ( \mathbf { m } ) } } \\ & { \qquad = \hat { h } _ { j } ( \mathbf { m } - \hat { \mathbf { m } } ) \cdot \hat { F } _ { j } ( \mathbf { m } - \hat { \mathbf { m } } ; b _ { 1 } - \hat { b } _ { 1 } , . . . ) } \end{array}
$$

Since $\hat { \bar { h } } _ { j } \big ( A ^ { ( 0 ) } \big ) \ \leq \ 2 4 _ { : }$ we see that

$$
\hat { f } _ { j } ( \Lambda ^ { \scriptscriptstyle ( 0 ) } ; 2 B , 2 B , \ldots ) < 2 4 \Lambda ( \Lambda ^ { \scriptscriptstyle ( 0 ) } + M ; 3 B ) .
$$

Thus Wintner has proved the possibility of analytic continuation of $1 / \phi _ { j } ( \mathbf { m } )$

Now choose $\pmb { B }$ so that $B = B ( \eta ) > 0$ for $\eta > 0$ .The quantity $\eta$ is determined in the following manner. If we take the Jacobi constant $c$ smaller than a constant $\boldsymbol { J }$ in the solution ${ \boldsymbol x } ( t ) , { \boldsymbol y } ( t )$ of Hill's differential equations in the interval $0 < L < | x ( t ) | ^ { 2 } + | y ( t ) | ^ { 2 } < \Gamma < + \infty$ $( - \infty < t < + \infty )$ ，then there exist， according to Weierstrass， two functions $\vartheta = \vartheta ( L , \Gamma , J )$ and $H ( L , \Gamma , J )$ depending only on $L , \Gamma , J$ such that the solutions in Fourier series for ${ \boldsymbol x } ( t ) , { \boldsymbol y } ( t )$ are holomorphic in $| \Re ( t \sqrt { - 1 } ) | \ \leq \vartheta$ and are smaller than $\pmb { H }$ in absolute value.Then the expansions are valid for $0 < \eta \le \mathbf { m } < M ,$ and the Laurent series

$$
\sum _ { i = - \infty } ^ { \infty } a _ { 2 i } ( \mathbf { m } ) \zeta ^ { 2 i + 1 }
$$

is holomorphic for

$$
1 - \frac { \vartheta ( \eta ) } { 2 } \leq | \zeta | , \qquad 1 > \frac { \vartheta ( \eta ) } { 2 } > 0 ,
$$

and is smaller in absolute value than $2 H ( \eta )$ . By Cauchy’s theorem, we have

$$
| a _ { 2 j } ( { \bf m } ) | < H ( \eta ) \left[ 1 + { \frac { \vartheta ( \eta ) } { 2 } } \right] ^ { - 2 j - 1 } .
$$

Hence

$$
\left| b _ { j } ( \mathbf { m } ) \right| = \left| \frac { j ^ { 4 } a _ { 2 j } ( \mathbf { m } ) } { \mathbf { m } a _ { 0 } ( \mathbf { m } ) } \right| < \frac { j ^ { 4 } H ( \eta ) \left( 1 \mathbf { \Lambda } + \frac { \vartheta ( \eta ) } { 2 } \right) ^ { - 2 j - 1 } } { \eta Z ( \eta ) } ,
$$

where we can show that $a _ { 0 } ( { \bf m } ) > Z ( \eta ) > 0$ Thus,

$$
| b _ { j } ( \mathbf { m } ) | < B ( \eta ) .
$$

Now suppose that $b _ { j } ( \mathbf { m } )$ is holomorphic for $| { \bf m } | \le \eta ^ { ( 0 ) }$ . Then Wintner showed by his infinite nonlinear analysis (see Chapter 2O) that

$$
b _ { j } ( \mathbf { m } ) - b _ { j } ( \eta ^ { ( 0 ) } )
$$

is holomorphic for $\big | { \bf m } - \eta ^ { ( 0 ) } \big | \le \rho ^ { ( 0 ) } ,$ ，and its deviation is smaller than $\pmb { { \cal B } } ^ { ( 0 ) }$ .The two series

$$
\sum _ { j = - \infty } ^ { \infty } \frac { a _ { 2 j } } { a _ { 0 } } = \sum _ { j = - \infty } ^ { \infty } \cdot \frac { { \bf m } b _ { j } ( { \bf m } ) } { j ^ { 4 } } ,
$$

$$
\begin{array} { l } { { \displaystyle \sum _ { j = - \infty } ^ { \infty } \left[ ( 2 j + 1 + \mathbf { m } ) ^ { 2 } + 2 \mathbf { m } ^ { 2 } \right] \frac { a _ { 2 j } } { a _ { 0 } } } \ ~ } \\ { { \displaystyle = \sum _ { j = - \infty } ^ { \infty } \mathbf { m } \frac { ( 2 j + 1 + \mathbf { m } ) ^ { 2 } + 2 \mathbf { m } ^ { 2 } } { j ^ { 4 } } b _ { j } ( \mathbf { m } ) } } \end{array}
$$

are holomorphic for $0 < \mathbf { m } < \eta ^ { ( 0 ) } + \rho ^ { ( 0 ) }$ . Suppose that the expansions are valid even for $0 < \mathbf { m } \le \mathfrak { g } ^ { ( 0 ) } + \mathfrak { p } ^ { ( 0 ) }$ .Then,they are valid similarly for $\eta ^ { ( 0 ) } + 2 \rho ^ { ( 0 ) }$ ， $\eta ^ { ( 0 ) } + 3 \rho ^ { ( 0 ) } ;$ ,... This shows the possibility of analytical continuation.

In general, consider with Wintner (1925b) the power series

$$
f _ { j } = f _ { j } ( x ; y _ { 1 } , y _ { 2 } , . . . ) \qquad ( j = 1 , 2 , . . . ) ,
$$

with an infinite number of variables, and let $\overline { { f _ { i } } }$ be the majorant of $f _ { i }$ Suppose that there exist positive numbers $a , b , M$ such that

$$
\overline { { { f } } } _ { j } ( a ; b , b , \ldots ) \leq M .
$$

Then there exist power series $y _ { i } = y _ { i } ( x )$ , which are absolutely convergent in a circle of radius min $( a , b / M )$ drawn around the point $x = 0$ and remain always smaller than the bound $b$ .These power series satisfy

$$
\frac { d y _ { i } } { d x } = f _ { i } , \qquad y _ { i } ( 0 ) = 0 \qquad ( i = 1 , 2 , \ldots ) ,
$$

and,if an aggregate of terms of degree lower than $\pmb { n }$ in $\phi ( { \pmb x } )$ is denoted by $[ \phi ( { \pmb x } ) ] _ { n } ,$ such that $S _ { n } ^ { ( i ) } = [ y _ { i } ] _ { n } ,$ then

$$
\begin{array} { l } { { S _ { n + 1 } ^ { ( i ) } ( x ) = \displaystyle \int _ { 0 } ^ { x } [ f _ { i } ( x ; S _ { n } ^ { ( 1 ) } ( x ) , S _ { n } ^ { ( 2 ) } ( x ) , \ldots ) ] _ { n } d x , } } \\ { { \quad S _ { 1 } ^ { ( i ) } ( x ) = \displaystyle \int _ { 0 } ^ { x } f _ { i } ( 0 ; 0 , 0 , \ldots ) d x = x f _ { i } ( 0 ; 0 , 0 , \ldots ) . } } \end{array}
$$