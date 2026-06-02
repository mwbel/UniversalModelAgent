hundreds of papers which have been written on the theory of the determination of orbits,very little that is really new or theoretically important has been added to the work of Laplace and Gauss unless more than three observations are used.

110.Preparation of the Observations. Whatever method it may be proposed to follow,the observations as obtained by the practical astronomer require certain slight corrections which should be made before the computation of the orbit is undertaken.

The attractions of the moon and the sun upon the equatorial bulge of the earth cause a small periodic oscillation and a slow secular change in the position of the plane of its equator. Since the equinoxes are the places where the equator and ecliptic intersect,the vernal equinox undergoes small periodic oscillations (the nutation） and slowly changes its position along the ecliptic (the precession). It is obviously necessary to have all the observations referred to the same coordinate system, and it is customary to use the mean equinox and position of the equator at the beginning of the year in which the observations are made.

The observed places are also affected by the aberration of light due to the revolution of the earth around the sun and to its rotation on its axis. Since the rotation is very slow compared to the revolution，the aberration due to the former is relatively small and generally may be neglected，especially if the observations arenot very precise.

Suppose $\pmb { \alpha _ { 0 } }$ and $\delta _ { 0 }$ are the observed right ascension and declination of the body at any time. Then the right ascension and declination referred to the mean equinox of the beginning of the year,and corrected for the annual aberration,are

$$
\left\{ \begin{array} { l l } { \alpha = \alpha _ { 0 } - 1 5 f - g \sin { ( G + \alpha _ { 0 } ) } \tan { \delta _ { 0 } } - h \sin { ( H + \alpha _ { 0 } ) } \sec { \delta _ { 0 } } , } \\ { \delta = \delta _ { 0 } - i \cos { \delta _ { 0 } } - g \cos { ( G + \alpha _ { 0 } ) } - h \cos { ( H + \alpha _ { 0 } ) } \sin { \delta _ { 0 } } , } \end{array} \right.
$$

where $f , g , h , G $ and $\pmb { H }$ are auxiliary quantities, called the Independent Star-Numbers,which are given in the American Ephemeris and Nautical Almanac for every day of the year. In practice these numbers are to be taken from the Ephemeris. They depend upon the motions of the earth,but their derivation belongs to the domain of Spherical and Practical Astronomy, and cannot be taken up here.\* The corrections to $\pmb { \alpha _ { 0 } }$ and $\delta _ { 0 }$ furnished by equations (4) are expressed in seconds of arc.

\* Chauvenet, Spherical and Practical Astronomy,vol.1., chap. x1.

The corrections for the diurnal aberration are

$$
\begin{array} { r } { \left\{ \begin{array} { l l l } { \Delta \alpha = - 0 ^ { \prime \prime } . 3 2 2 \cos \varphi \cos ( \theta - \alpha _ { 0 } ) \sec \delta _ { 0 } , } \\ { \Delta \delta = - 0 ^ { \prime \prime } . 3 2 2 \cos \varphi \sin ( \theta - \alpha _ { 0 } ) \sin \delta _ { 0 } , } \end{array} \right. } \end{array}
$$

where $\varphi$ is the latitude of the observer,and $\theta - \alpha _ { 0 }$ is the hour angle of the object at the time of the observation. The second of these corrections cannot exceed the small quantity $\mathbf { 0 ^ { \prime \prime } } . 3 2 2$ ， and the first is also small unless $\delta _ { 0 }$ is near $\pm \ 9 0 ^ { \circ }$

111. Outline of the Laplacian Method of Determining an Orbit. Before entering on the details which are necessary for the determination of the elements of an orbit by either of the two methods which are in common use,a brief exposition of the general lines of argument used in them will be given. From these outlines the plan of attack can be understood,and then the bearings of the detailed investigations will be fully appreciated.

In order to keep to the central thought suppose only three complete observations are available for the determination of the orbit. Let the dates of the observations be $t _ { 1 } , \ t _ { 2 } ,$ and $t _ { 3 }$ ，and hence at these times the right ascensions and declinations of the observed body as seen from the earth are known. For the sake of definiteness in the terminology let $\boldsymbol { c }$ represent the observed body revolving around the sun, $\boldsymbol { S }$ ,and observed from the earth $E ; \xi , \eta , \zeta$ the rectangular coordinates of $\boldsymbol { c }$ with respect to $E$ ； $x , y _ { \mathrm { ; } }$ ， $\pmb { z }$ the rectangular coordinates of $c$ with respect to $S ; X , Y , z$ the rectangular coordinates of $\boldsymbol { s }$ with respect to $E$ ； $\pmb { \rho }$ the distance from $\mathbfit { \Delta } E$ to $\pmb { C }$ ； $\pmb { r }$ the distance from $\pmb { S }$ to $\boldsymbol { c }$ ； $\scriptstyle { R }$ the distance from $\mathbfit { \Delta } E$ to $\pmb { S }$ Then

$$
\left\{ \begin{array} { l l } { \xi = \rho \cos \delta \cos \alpha = \rho \lambda , } \\ { \qquad = \rho \cos \delta \sin \alpha = \rho \mu , } \\ { \qquad \ m \leq \rho \sin \delta \quad \qquad = \rho \nu . } \end{array} \right.
$$

The quantities $\lambda , \mu ,$ and $\nu _ { . }$ ，which are the direction cosines of the line from $\pmb { { \cal E } }$ to $\boldsymbol { c }$ ， are known at $t _ { 1 } , \ t _ { 2 } ,$ and $t _ { 3 }$ .The distance $\pmb { \rho }$ is entirely unknown.

First Step. The first step is to determine the values of the first and second derivatives of $\lambda , \mu , \nu , X , Y$ ,and $z$ at some time near the dates of observation,say at $t _ { 2 }$ .It will be sufficient at present to show that it can be done with considerable approximation without discussing the best method of doing it. The value of the frst derivative of $\gimel$ during the interval $t _ { 1 }$ to $t _ { 2 }$ averages

$$
\lambda _ { 1 2 } ^ { \prime } = \frac { \lambda _ { 2 } - \lambda _ { 1 } } { t _ { 2 } - t _ { 1 } } ,
$$

and this is very nearly the value of $\lambda ^ { \prime }$ at the middle of the interval unless $\lambda ^ { \prime }$ happens to be changing very rapidly. The approximation is better the shorter the interval. In a similar manner ${ \lambda } _ { 2 3 } ^ { ' }$ is formed. When the interval $t _ { 2 } - t _ { 1 }$ equals the interval $t _ { 3 } \ : - \ : t _ { 2 }$ the value of $\lambda ^ { \prime }$ at $\mathbf { { f _ { 2 } } }$ is very nearly

$$
\begin{array} { r } { \lambda _ { 2 } ^ { \prime } = \frac { 1 } { 2 } [ \lambda _ { 1 2 } ^ { \prime } + \lambda _ { 2 3 } ^ { \prime } ] . } \end{array}
$$

If the intervals are not equal,adjustment for the disparity can of course be made.

In a similar manner it follows from the definition of a derivative that the second derivative of $\lambda$ at $t _ { 2 }$ ,in case the two intervals are equal, is approximately

$$
\lambda _ { 2 } ^ { \prime \prime } = \frac { \lambda _ { 2 3 } ^ { \prime } - \lambda _ { 1 2 } ^ { \prime } } { \frac { 1 } { 2 } ( t _ { 3 } - t _ { 1 } ) } .
$$

The first and second derivatives of $\pmb { \mu }$ and $\pmb { \nu }$ are given approximately by similar formulas,and it is to be understood that when the intervals are as short as they generally are in practice the approximations,especially as obtained by the more refined methods which will be considered in the detailed discussion,are very close. The American Ephemeris gives the values of $X , Y$ ,and $z$ for every day in the year,and from these data the values of their first and second derivatives can be found. As a matter of fact only the first derivatives of these coordinates will be required.

Second Step. The second step is to impose the condition that $c$ moves around $s$ in accordance with the law of gravitation. It will be assumed that $c$ is not sensibly disturbed by the attractions of other bodies. Hence its coordinates satisfy the differential equations

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } x } { d t ^ { 2 } } = - \frac { k ^ { 2 } x } { r ^ { 3 } } , } \\ { \displaystyle \frac { d ^ { 2 } y } { d t ^ { 2 } } = - \frac { k ^ { 2 } y } { r ^ { 3 } } , } \\ { \displaystyle \frac { d ^ { 2 } z } { d t ^ { 2 } } = - \frac { k ^ { 2 } z } { r ^ { 3 } } . } \end{array} \right.
$$

But it also follows from the relations of $C , { \cal E }$ and $\boldsymbol { s }$ that

$$
\left\{ \begin{array} { l l } { x = \rho \lambda - X , } \\ { y = \rho \mu - Y , } \\ { z = \rho \nu - Z . } \end{array} \right.
$$

On substituting these expressions for $x , y$ and $\pmb { \mathscr { z } }$ in equations (7), they become

$$
\left\{ \begin{array} { l l } { ( \rho \lambda ) ^ { \prime \prime } - X ^ { \prime \prime } = \frac { - k ^ { 2 } ( \rho \lambda - X ) } { r ^ { 3 } } , } \\ { \qquad } \\ { ( \rho \mu ) ^ { \prime \prime } - Y ^ { \prime \prime } = \frac { - k ^ { 2 } ( \rho \mu - Y ) } { r ^ { 3 } } , } \\ { \qquad } \\ { ( \rho \nu ) ^ { \prime \prime } - Z ^ { \prime \prime } = \frac { - k ^ { 2 } ( \rho \nu - Z ) } { r ^ { 3 } } . } \end{array} \right.
$$

But since $\mathbfit { \Delta } E$ also revolves around $\boldsymbol { \mathsf { \Pi } } _ { \boldsymbol { \mathsf { S } } } ^ { g }$ in accordance with the law of gravitation,it follows that

$$
\begin{array} { r l r } & { } & { X ^ { \prime \prime } = - \frac { k ^ { 2 } X } { R ^ { 3 } } , } \\ & { } & \\ & { } & { Y ^ { \prime \prime } = - \frac { k ^ { 2 } Y } { R ^ { 3 } } , } \\ & { } & \\ & { } & { Z ^ { \prime \prime } = - \frac { k ^ { 2 } Z } { R ^ { 3 } } . } \end{array}
$$

Therefore equations (9) become

$$
\left\{ \begin{array} { l } { { \displaystyle \lambda \rho ^ { \prime \prime } + 2 \lambda ^ { \prime } \rho ^ { \prime } + \left[ \lambda ^ { \prime \prime } + \frac { k ^ { 2 } \lambda } { r ^ { 3 } } \right] \rho = - k ^ { 2 } X \left[ \frac { 1 } { R ^ { 3 } } - \frac { 1 } { r ^ { 3 } } \right] } , } \\ { { \displaystyle \mu \rho ^ { \prime \prime } + 2 \mu ^ { \prime } \rho ^ { \prime } + \left[ \mu ^ { \prime \prime } + \frac { k ^ { 2 } \mu } { r ^ { 3 } } \right] \rho = - k ^ { 2 } Y \left[ \frac { 1 } { R ^ { 3 } } - \frac { 1 } { r ^ { 3 } } \right] } , } \\ { { \displaystyle \nu \rho ^ { \prime \prime } + 2 \nu ^ { \prime } \rho ^ { \prime } + \left[ \nu ^ { \prime \prime } + \frac { k ^ { 2 } \nu } { r ^ { 3 } } \right] \rho = - k ^ { 2 } Z \left[ \frac { 1 } { R ^ { 3 } } - \frac { 1 } { r ^ { 3 } } \right] } . } \end{array} \right.
$$

The unknown quantities in these equations are $\rho ^ { \prime \prime } , \ \rho ^ { \prime } , \ \rho ;$ and $r _ { : }$ the first three of which enter linearly.

Third Step. The third step is to determine the distance of $\boldsymbol { c }$ from $E$ and $\boldsymbol { s }$ by means of equations (1O) and a geometrical condition which the three bodies must satisfy. In order to solve equations (10) for $\pmb { \rho }$ ,let

$$
D = { \left| \begin{array} { l l l l } { \lambda , } & { \lambda ^ { \prime } , } & { \lambda ^ { \prime \prime } + { \frac { k ^ { 2 } \lambda } { T ^ { 3 } } } } \\ { } & { } & { } \\ { \mu , } & { \mu ^ { \prime } , } & { \mu ^ { \prime \prime } + { \frac { k ^ { 2 } \mu } { T ^ { 3 } } } } \\ { } & { } & { } \\ { \nu , } & { \nu ^ { \prime } , } & { \nu ^ { \prime \prime } + { \frac { k ^ { 2 } \nu } { T ^ { 3 } } } } \end{array} \right| } = { \left| \begin{array} { l l l } { \lambda , } & { \lambda ^ { \prime } , } & { \lambda ^ { \prime \prime } } \\ { \mu , } & { \mu ^ { \prime } , } & { \mu ^ { \prime \prime } } \\ { \nu , } & { \nu ^ { \prime } , } & { \nu ^ { \prime \prime } } \end{array} \right| } .
$$

The second form of the determinant $D$ is obtained by multiplying the frst column by ${ \frac { k ^ { 2 } } { r ^ { 3 } } } \mathrm { a n d }$ subtracting the product from the third column. The determinant which is obtained by replacing the elements of the third column of $D$ by the right member of (10) will also be needed．If the common factor $\left[ { \frac { 1 } { R ^ { 3 } } } - { \frac { 1 } { r ^ { 3 } } } \right]$ is omitted, this determinant is

$$
D _ { 1 } = { \bf - \nabla } k ^ { 2 } \left| \begin{array} { c c c } { { \lambda , } } & { { \lambda ^ { \prime } , } } & { { X } } \\ { { } } & { { } } & { { } } \\ { { \mu , } } & { { \mu ^ { \prime } , } } & { { Y } } \\ { { \nu , } } & { { \nu ^ { \prime } , } } & { { Z } } \end{array} \right| .
$$

The determinants $D$ and $D _ { 1 }$ involve only known quantities.

The solution of equations (10) for $\pmb { \rho }$ is

$$
\rho = \frac { D _ { 1 } } { D } \left[ \frac { 1 } { R ^ { 3 } } - \frac { 1 } { r ^ { 3 } } \right] .
$$

To this equation in the two unknown quantities $\pmb { \rho }$ and $\pmb { r }$ must be added the equation

$$
r ^ { 2 } = \rho ^ { 2 } + R ^ { 2 } - 2 \rho R \cos \psi ,
$$

which expresses the fact that the three bodies $c , s _ { \mathrm { { z } } }$ and $\pmb { \cal E }$ form a triangle. The angle $\psi$ is the angle at $\mathbfit { \Delta } E$ between $\scriptstyle { R }$ and $\pmb \rho _ { ; }$ and this equation also has only the unknowns $\pmb { \rho }$ and $r$ ，The problem of solving (13) and (14) for $\pmb { \rho }$ and $\pmb { r }$ is that which constitutes the third step. The solution of this problem gives the coordinates of $\boldsymbol { c }$ by means of equations (8) wnich involve only $\pmb { \rho }$ as an unknown.

Fourth Step. The fourth step is the determination of the components of velocity of $\boldsymbol { c }$ It follows from (8) that

$$
\left\{ \begin{array} { l l } { x ^ { \prime } = \rho ^ { \prime } \lambda + \rho \lambda ^ { \prime } - X ^ { \prime } , } \\ { y ^ { \prime } = \rho ^ { \prime } \mu + \rho \mu ^ { \prime } - Y ^ { \prime } , } \\ { z ^ { \prime } = \rho ^ { \prime } \nu + \rho \nu ^ { \prime } - Z ^ { \prime } . } \end{array} \right.
$$

The only unknown in the right members of these equations is $\pmb { \rho } ^ { \prime }$ which can be determined from (1O). The expression for it is

$$
\left\{ \begin{array} { l } { \displaystyle \rho ^ { \prime } = + \frac { D _ { 2 } } { 2 D } \left[ \frac { 1 } { R ^ { 3 } } - \frac { 1 } { r ^ { 3 } } \right] , } \\ { \displaystyle D _ { 2 } = - k ^ { 2 } \left| \begin{array} { l l l } { \displaystyle \lambda , } & { X , } & { \displaystyle \lambda ^ { \prime \prime } } \\ { \displaystyle p , } & { Y , } & { \displaystyle \mu ^ { \prime \prime } } \\ { \displaystyle p , } & { Z , } & { \displaystyle \nu ^ { \prime \prime } } \end{array} \right| . } \end{array} \right.
$$

Therefore $\acute { \boldsymbol { x } } ^ { \prime } , \boldsymbol { y } ^ { \prime }$ and $\pmb { z } ^ { \prime }$ become known.

Fifth Step. The fth and last step is to determine the elements of the orbit from the position and components of velocity of the body. This is the problem which was solved in chap. v.

112. Outline of the Gaussian Method of Determining an Orbit. First Step. The first step in the Gaussian method is to impose the condition that $c$ moves in a plane passing through $\boldsymbol { s }$ Since $\pmb { S }$ is the origin for the coordinates $x , y .$ and $\pmb { z }$ ,this condition is

$$
\left\{ \begin{array} { l l } { A x _ { 1 } + B y _ { 1 } + C z _ { 1 } = 0 , } \\ { A x _ { 2 } + B y _ { 2 } + C z _ { 2 } = 0 , } \\ { A x _ { 3 } + B y _ { 3 } + C z _ { 3 } = 0 , } \end{array} \right.
$$

where $A , B , C$ are constants which depend upon the position of the plane of motion. The result of eliminating the unknown constants $A , B$ and $c$ is the equation

$$
\left| { \begin{array} { l l l } { x _ { 1 } , } & { y _ { 1 } , } & { z _ { 1 } } \\ { x _ { 2 } , } & { y _ { 2 } , } & { z _ { 2 } } \\ { x _ { 3 } , } & { y _ { 3 } , } & { z _ { 3 } } \end{array} } \right| = 0 .
$$

The determinant (17) can be expanded with respect to the elements of the three columns giving the three equations

$$
\left\{ \begin{array} { l l } { ( y _ { 2 } z _ { 3 } - z _ { 2 } y _ { 3 } ) x _ { 1 } - ( y _ { 1 } z _ { 3 } - z _ { 1 } y _ { 3 } ) x _ { 2 } + ( y _ { 1 } z _ { 2 } - z _ { 1 } y _ { 2 } ) x _ { 3 } = 0 , } \\ { ( x _ { 2 } z _ { 3 } - z _ { 2 } x _ { 3 } ) y _ { 1 } - ( x _ { 1 } z _ { 3 } - z _ { 1 } x _ { 3 } ) y _ { 2 } + ( x _ { 1 } z _ { 2 } - z _ { 1 } x _ { 2 } ) y _ { 3 } = 0 , } \\ { ( x _ { 2 } y _ { 3 } - y _ { 2 } x _ { 3 } ) z _ { 1 } - ( x _ { 1 } y _ { 3 } - y _ { 1 } x _ { 3 } ) z _ { 2 } + ( x _ { 1 } y _ { 2 } - y _ { 1 } x _ { 2 } ) z _ { 3 } = 0 . } \end{array} \right.
$$

Evidently these three equations are but different forms of the same one;but when the nine parentheses are determined from additional principles and ${ \pmb x } _ { 1 } , \ { \pmb x } _ { 2 } ,$ .· are expressed in terms of the geocentric .coordinates by (8)，they become independent in the unknowns $\rho _ { 1 } , \rho _ { 2 } ,$ and $\pmb { \rho _ { 3 } }$ .The parentheses are the projections of twice the triangles formed by $\pmb { S }$ and the positions of $c$ taken in twos upon the three fundamental planes. Since in each equation the three areas are projected upon the same plane the triangles themselves can be used instead of their projections. If [1,2], [1,3],and [2,3] represent the triangles formed by $\pmb { S }$ and $c$ ai the .times $t _ { 1 } t _ { 2 } , \ t _ { 1 } t _ { 3 } ,$ and $t _ { 2 } t _ { 3 }$ respectively,equations (18) become

$$
\left\{ \begin{array} { l l } { \left[ 2 , 3 \right] x _ { 1 } - \left[ 1 , 3 \right] x _ { 2 } + \left[ 1 , 2 \right] x _ { 3 } = 0 , } \\ { \left[ 2 , 3 \right] y _ { 1 } - \left[ 1 , 3 \right] y _ { 2 } + \left[ 1 , 2 \right] y _ { 3 } = 0 , } \\ { \left[ 2 , 3 \right] z _ { 1 } - \left[ 1 , 3 \right] z _ { 2 } + \left[ 1 , 2 \right] z _ { 3 } = 0 . } \end{array} \right.
$$

Second Step. The second step consists in developing the ratios of the triangles as power series in the time-intervals. This is done by integrating equations (7） as power series in the timeintervals,and then substituting the results for $t = t _ { 1 } , t _ { 2 } , t _ { 3 }$ in the coeffcients of (18) or (19).Inasmuch as these series are based upon equations (7） the condition that $c$ shall move about $\boldsymbol { s }$ in accordance with the law of gravitation has been imposed. In order not to prolong the discussion at this point (for the details see Art.127) the results will be given at once. For the purpose of simplifying the writing, let

$$
\left\{ \begin{array} { l l } { k ( t _ { 2 } - t _ { 1 } ) = \theta _ { 3 } , } \\ { k ( t _ { 3 } - t _ { 2 } ) = \theta _ { 1 } , } \\ { k ( t _ { 3 } - t _ { 1 } ) = \theta _ { 2 } , } \\ { \theta _ { 2 } = \theta _ { 1 } + \theta _ { 3 } . } \end{array} \right.
$$

In this notation the ratios of the triangles [2,3]and [1,2] to [1,3] are found to be

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { [ 2 , 3 ] } { [ 1 , 3 ] } = \frac { \theta _ { 1 } } { \theta _ { 2 } } \left[ 1 + \frac { 1 } { 6 } \frac { \theta _ { 2 } ^ { 2 } - \theta _ { 1 } ^ { 2 } } { { r _ { 2 } } ^ { 3 } } + \cdots \right] , } \\ { \displaystyle \frac { [ 1 , 2 ] } { [ 1 , 3 ] } = \frac { \theta _ { 3 } } { \theta _ { 2 } } \left[ 1 + \frac { 1 } { 6 } \frac { \theta _ { 2 } ^ { 2 } - \theta _ { 3 } ^ { 2 } } { { r _ { 2 } } ^ { 3 } } + \cdots \right] . } \end{array} \right.
$$

Third Step. The third step consists in developing equations for the determination of $\rho _ { 1 } , \rho _ { 2 } ,$ and $\pmb { \rho _ { 3 } }$ The results of substituting equations (8)and (21) in (19) are

$$
\left\{ \begin{array} { l l } { \displaystyle \theta _ { s } \left[ 1 + \frac { 1 } { 6 } \frac { \theta _ { s } ^ { 2 } } { \tau _ { s } ^ { 3 } } - \frac { \theta _ { s } ^ { 2 } } { \tau _ { s } ^ { 3 } } + \dots \right] ( \lambda _ { 1 } p _ { 1 } - X _ { 1 } ) - \theta _ { 2 } ( \lambda _ { 2 } \rho _ { 2 } - X _ { 3 } ) } \\ { \displaystyle \qquad + \theta _ { s } \left[ 1 + \frac { 1 } { 6 } \frac { \theta _ { s } ^ { 2 } - \theta _ { s } ^ { 2 } } { \tau _ { s } ^ { 3 } } + \dots \right] ( \lambda _ { 1 } p _ { 2 } - X _ { 3 } ) = 0 , } \\ { \displaystyle \theta _ { 1 } \left[ 1 + \frac { 1 } { 6 } \frac { \theta _ { s } ^ { 2 } - \theta _ { s } ^ { 2 } } { \tau _ { s } ^ { 3 } } + \dots \right] ( \mu _ { 1 } p _ { 1 } - Y _ { 1 } ) - \theta _ { 2 } ( \mu _ { 2 } p _ { 2 } - Y _ { 2 } ) } \\ { \displaystyle \qquad + \theta _ { s } \left[ 1 + \frac { 1 } { 6 } \frac { \theta _ { s } ^ { 2 } - \theta _ { s } ^ { 2 } } { \tau _ { s } ^ { 2 } } + \dots \right] ( \mu _ { s } p _ { s } - Y _ { 3 } ) = 0 , } \\ { \displaystyle \theta _ { 1 } \left[ 1 + \frac { 1 } { 6 } \frac { \theta _ { s } ^ { 2 } - \theta _ { s } ^ { 2 } } { \tau _ { s } ^ { 2 } } + \dots \right] ( \nu _ { 3 } p _ { 1 } - Z _ { 1 } ) - \theta _ { 2 } ( \nu _ { 2 } \rho _ { 2 } - Z _ { 3 } ) } \\ { \displaystyle \qquad + \theta _ { s } \left[ 1 + \frac { 1 } { 6 } \frac { \theta _ { s } ^ { 2 } - \theta _ { s } ^ { 2 } } { \tau _ { s } ^ { 2 } } + \dots \right] ( \nu _ { 3 } \rho _ { 3 } - Z _ { 3 } ) = 0 , } \end{array} \right.
$$

These equations involve the unknowns $\rho _ { 1 } , \ \rho _ { 2 } , \ \rho _ { 3 } ,$ and $\mathbf { \boldsymbol { r } _ { 2 } } ,$ the first three of which enter linearly. Since $\mathbf { \boldsymbol { r } _ { 2 } }$ enters only as it is multiplied by the small quantities $\theta _ { 1 } { } ^ { 2 } , \ \theta _ { 2 } { } ^ { 2 }$ or $\theta _ { 3 } { } ^ { 2 }$ ,it might be supposed that in a first approximation these terms could be neglected, after which $\rho _ { 1 } , \rho _ { 2 } ,$ and $\rho _ { 3 }$ would be determined by linear equations. A detailed discussion of the determinants which are involved shows,however, that it is necessary to retain the terms in $\mathbf { \boldsymbol { r } _ { 2 } }$ even in the first approximation.

The solution of equations (22) for $\pmb { \rho _ { 2 } }$ has the form

$$
\Delta \rho _ { 2 } = P + \frac { Q } { r _ { 2 } { ^ 3 } } ,
$$

where $\Delta$ is the determinant of the coefficients of $\rho _ { 1 } , \rho _ { 2 }$ and $\pmb { \rho _ { 3 } }$ and $P$ and $Q$ are functions of the known quantities $\lambda _ { 1 } , \ \lambda _ { 2 } , \ \cdots ,$ $X _ { 1 } , ~ Y _ { 1 } ,$

Since $s , \mathbf {  { \mathit { E } } }$ and $c$ form a triangle at $t _ { 2 }$ the quantities $\pmb { \rho _ { 2 } }$ and $\mathbf { \boldsymbol { r } _ { 2 } }$ satisfy the equation

$$
{ r _ { 2 } } ^ { 2 } = \rho _ { 2 } { ^ 2 } + { R _ { 2 } } ^ { 2 } - 2 \rho _ { 2 } { R _ { 2 } } \cos \psi _ { 2 } .
$$

The solution of any two equations of (22) for $\pmb { \rho _ { 1 } }$ and $\pmb { \rho _ { 3 } }$ in terms of $\pmb { \rho _ { 2 } }$ and $\pmb { r _ { 2 } }$ has the form

$$
\left\{ \begin{array} { l l } { \displaystyle M \rho _ { 1 } = P _ { 1 } \rho _ { 2 } \left[ 1 - \frac 1 6 \frac { \theta _ { 2 } ^ { 2 } - \theta _ { 1 } ^ { 2 } } { \displaystyle r _ { 2 } ^ { 3 } } + \cdots \right] + Q _ { 1 } , } \\ { \displaystyle M \rho _ { 3 } = P _ { 3 } \rho _ { 2 } \left[ 1 - \frac 1 6 \frac { \theta _ { 2 } ^ { 2 } - \theta _ { 3 } ^ { 2 } } { \displaystyle r _ { 2 } ^ { 3 } } + \cdots \right] + Q _ { 3 } , } \end{array} \right.
$$

where $M , P _ { 1 } , P _ { 3 }$ are functions of known quantities, and $Q _ { 1 }$ and $Q _ { 3 }$ involve only $\boldsymbol { r _ { 2 } }$ as an unknown.

Fourth Step. The fourth step consists in determining $\pmb { \rho _ { 1 } }$ and $\pmb { \rho _ { 3 } }$ The quantities $\pmb { \rho _ { 2 } }$ and $\mathbf { \boldsymbol { r } _ { 2 } }$ are found first by solving (23) and (24), which is exactly the same as the third step of the Laplacian method,and then $\pmb { \rho _ { 1 } }$ and $\pmb { \rho _ { 3 } }$ are given by (25).

Frfth Step. The fifth step consists in determining the elements from the known positions of $c$ at the times $t _ { 1 }$ and $t _ { 3 }$ These two positions and that of $c$ define the plane of the orbit without further work. Gauss solved the problem of determining the remaining elements by developing two equations involving only two unknowns. One equation was derived from the ratio of the triangle formed by $\boldsymbol { s }$ and $\boldsymbol { c }$ at $t _ { 1 }$ and $t _ { 3 }$ to the area of the sector contained between $r _ { 1 } , r _ { 3 } $ ,and the arc of the orbit described in the interval $t _ { 1 } t _ { 3 }$ ，The other equation was derived from Kepler's equation at the epochs $\mathbf { { \boldsymbol { t } } _ { 1 } }$ and $t _ { 3 }$ The formulas are complex, but the method of solving the two equations is a rapid process of successive approximations. After the equations are solved the elements are uniquely determined without any trouble. Later methods have been devised which avoid many of the complexities of that due to Gauss.

I.THE LAPLACIAN METHOD OF DETERMINING ORBITS.

113.Determination of the First and Second Derivatives of the Angular Coördinates from Three Observations. It was found in the outline [Art.111] of this method of determining orbits that the first and second derivatives of the angular coordinates，or of the direction cosines $\lambda , \mu ,$ and $\pmb { \nu }$ will be required.

Let $k ( t - t _ { 0 } ) = \tau$ and then equations (7) become

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } x } { d \tau ^ { 2 } } = - \frac { x } { r ^ { 3 } } , } \\ { \displaystyle \frac { d ^ { 2 } y } { d \tau ^ { 2 } } = - \frac { y } { r ^ { 3 } } , } \\ { \displaystyle \frac { d ^ { 2 } z } { d \tau ^ { 2 } } = - \frac { z } { r ^ { 3 } } . } \end{array} \right.
$$

$x = x _ { 0 } , \ y = y _ { 0 } , \ z = z _ { 0 } , \ { \frac { d x } { d \tau } } = x _ { 0 } , \ { \frac { d y } { d \tau } } = y _ { 0 } , \ { \frac { d z } { d \tau } } = z _ { 0 } ,$ at $\tau = 0$ 。The solution of equations (26) can be expanded as power series in $\boldsymbol { \tau }$ which will converge if the value of $\pmb { \tau }$ is not too great.\* They will have the form

$$
\begin{array} { r l r } & { } & { [ x = x _ { 0 } + { x _ { 0 } } ^ { \prime } \tau + \frac { 1 } { 2 } ( \frac { d ^ { 2 } x } { d \tau ^ { 2 } } ) _ { 0 } \tau ^ { 2 } + \cdots + \frac { 1 } { n ! } ( \frac { d ^ { n } x } { d \tau ^ { n } } ) _ { 0 } \tau ^ { n } + \cdots , } \\ & { } & { \sqrt { y } = y _ { 0 } + { y _ { 0 } } ^ { \prime } \tau + \frac { 1 } { 2 } ( \frac { d ^ { 2 } y } { d \tau ^ { 2 } } ) _ { 0 } \tau ^ { 2 } + \cdots + \frac { 1 } { n ! } ( \frac { d ^ { n } y } { d \tau ^ { n } } ) _ { 0 } \tau ^ { n } + \cdots , } \\ & { } & { [ z = z _ { 0 } + z _ { 0 } ^ { \prime } \tau + \frac { 1 } { 2 } ( \frac { d ^ { 2 } z } { d \tau ^ { 2 } } ) _ { 0 } \tau ^ { 2 } + \cdots + \frac { 1 } { n ! } ( \frac { d ^ { n } z } { d \tau ^ { n } } ) _ { 0 } \tau ^ { n } + \cdots ,  } \end{array}
$$

where the subscript O on the parentheses indicates that the derivatives are taken for $\tau = 0$ .The second derivatives can be replaced by the right members of (26) for $\tau = 0$ ； the third derivatives can be replaced by the first derivatives of the right members of (26), and so on. All the derivatives in this way will be expressed in terms of $x _ { 0 } , y _ { 0 } , z _ { 0 } , x _ { 0 } ^ { \prime } , y _ { 0 } ^ { \prime }$ ,and ${ \boldsymbol { z } } _ { 0 } ^ { \prime }$

\* For the determination of the exact realm of convergence see a paper by F.R. Moulton in The Astronomical Journal,vol. 23 (1903).

It is important to know for how great intervals the series (27) are of practical value. The limits are smaller the smaller the perihelion distance and the greater the eccentricity，and moreover they depend upon the position of the body in its orbit at ${ \boldsymbol { \tau } } = 0 .$ Fora small planet whose mean distance is 2.65,which is about the average for these bodies,and the eccentricity of whose orbit does not exceed O.4,which is much greater than that of most of them,the series (27） always converge for an interval of less than 160 days. If the orbit is a parabola whose perihelion distance is unity the series (27） converge if the interval of time does not exceed 54 days. Of course, the series are not of practical value in their whole range of convergence. In practice in the case of small planets an interval of 90 days is nearly always small enough to secure rapid convergence of (27),and in the case of the orbits of comets 2O days is rarely too great an interval.

The coordinates of the earth also are expansible as series of the form of (27)，and the rapid convergence holds for very long intervals because of the small eccentricity of the earth's orbit. Hence it follows from equations (8） that $\rho , ~ \lambda , ~ \mu ,$ and ${ \pmb \nu }$ can be expanded as power series of the type of (27). The range of usefulness of these expansions is the same as that of the series for $x , y$ and $\pmb { z }$

It will be sufficient to consider the series for $\lambda$ because those in $\pmb { \mu }$ and $\pmb { \nu }$ are symmetrically similar. The series for $\lambda$ fora general value of $\tau$ and for $\tau _ { 1 } , \ \tau _ { 2 } ,$ and $\tau _ { 3 } ,$ which correspond to $t _ { 1 } , t _ { 2 } ,$ and $\pmb { t _ { 3 } }$ respectively，are

$$
\left\{ \begin{array} { l } { { \lambda = c _ { 0 } + c _ { 1 } \tau + c _ { 2 } \tau ^ { 2 } + \cdots , } } \\ { { } } \\ { { \lambda _ { 1 } = c _ { 0 } + c _ { 1 } \tau _ { 1 } + c _ { 2 } \tau _ { 1 } ^ { 2 } + \cdots , } } \\ { { } } \\ { { \lambda _ { 2 } = c _ { 0 } + c _ { 1 } \tau _ { 2 } + c _ { 2 } \tau _ { 2 } ^ { 2 } + \cdots , } } \\ { { } } \\ { { \lambda _ { 3 } = c _ { 0 } + c _ { 1 } \tau _ { 3 } + c _ { 2 } \tau _ { 3 } ^ { 2 } + \cdots , } } \end{array} \right.
$$

where $c _ { 0 } , c _ { 1 } , c _ { 2 } , \cdots$ are constants. If these equations are terminated after the terms of the second degree the coefficients ${ c _ { 0 } , \ c _ { 1 } , }$ and $\pmb { c _ { 2 } }$ are determined in terms of the observed quantities $\lambda _ { 1 } , \lambda _ { 2 } ,$ and $\lambda _ { 3 }$ ,and the time-intervals $\tau _ { 1 } , \tau _ { 2 } ,$ and $\pmb { \tau _ { 3 } }$ If more observations are available more coefficients can be determined； the number which can be determined equals the number of observations.

The simplest way of expressing $\lambda$ in terms of $\boldsymbol { \tau }$ with known coefficients is to set equal to zero the eliminant of $\mathbf { l } , \mathbf { \alpha } , { \pmb { c } } _ { 1 } ,$ and ${ \pmb { c _ { 2 } } }$ in (28),which is

$$
{ \left| \begin{array} { l l l l } { \lambda , } & { 1 , } & { \tau , } & { \tau ^ { 2 } } \\ { \lambda _ { 1 } , } & { 1 , } & { \tau _ { 1 } , } & { \tau _ { 1 } { } ^ { 2 } } \\ { \lambda _ { 2 } , } & { 1 , } & { \tau _ { 2 } , } & { \tau _ { 2 } { } ^ { 2 } } \\ { \lambda _ { 3 } , } & { 1 , } & { \tau _ { 3 } , } & { \tau _ { 3 } { } ^ { 2 } } \end{array} \right| } = 0 .
$$

The expansion of this determinant with respect to the elements of the first column is

$$
A _ { 0 } \lambda - A _ { 1 } \lambda _ { 1 } + A _ { 2 } \lambda _ { 2 } - A _ { 3 } \lambda _ { 3 } = 0 ,
$$

where

$$
A _ { 0 } = { \left| \begin{array} { l l l } { 1 , } & { \tau _ { 1 } , } & { { \tau _ { 1 } } ^ { 2 } } \\ { 1 , } & { \tau _ { 2 } , } & { { \tau _ { 2 } } ^ { 2 } } \\ { 1 , } & { \tau _ { 3 } , } & { { \tau _ { 3 } } ^ { 2 } } \end{array} \right| } = - ( \tau _ { 2 } - \tau _ { 1 } ) ( \tau _ { 3 } - \tau _ { 2 } ) ( \tau _ { 1 } - \tau _ { 3 } ) ,
$$

and where $A _ { 1 } , A _ { 2 }$ and $A _ { 3 }$ are obtained from $\scriptstyle A _ { 0 }$ by permuting $\tau$ with $\tau _ { 1 } , \tau _ { 2 } ,$ and $\pmb { \tau _ { 3 } }$ respectively. The determinant $\scriptstyle A _ { 0 }$ is distinct from zero if $\tau _ { 1 } , \ \tau _ { 2 } ,$ and $\pmb { \tau _ { 3 } }$ are distinct. Hence equation (30) becomes

$$
\begin{array} { c } { { \lambda = \displaystyle \frac { ( \tau - \tau _ { 2 } ) ( \tau - \tau _ { 3 } ) } { ( \tau _ { 1 } - \tau _ { 2 } ) ( \tau _ { 1 } - \tau _ { 3 } ) } \lambda _ { 1 } + \frac { ( \tau - \tau _ { 3 } ) ( \tau - \tau _ { 1 } ) } { ( \tau _ { 2 } - \tau _ { 3 } ) ( \tau _ { 2 } - \tau _ { 1 } ) } \lambda _ { 2 } } } \\ { { + \frac { ( \tau - \tau _ { \mathrm { i } } ) ( \tau - \tau _ { 2 } ) } { ( \tau _ { 3 } - \tau _ { 1 } ) ( \tau _ { 3 } - \tau _ { 2 } ) } \lambda _ { 3 } . } } \end{array}
$$

It follows from the form of (31） that this equation gives $\gimel$ exactly at $\tau _ { 1 } , \tau _ { 2 } ,$ and $\pmb { \tau _ { 3 } }$ ; for other small values of $\pmb { \tau }$ it gives $\lambda$ approximately. The exact value of $\lambda$ is given by an infinite series, the first equation of (28)，within the range of its convergence. Geometrically considered this series defines a curve,marked $\boldsymbol { C }$ in Fig.31. The second degree polynomial (31） defines another curve $C _ { 2 }$ .These two curves intersect at $\tau _ { 1 } , \ \tau _ { 2 } ,$ and $\pmb { \tau _ { 3 } } .$ ，but in general do not intersect elsewhere. For small values of $\tau$ the two curves nearly coincide,and the approximate value of $\lambda$ can be found from the polynomial near the origin.

![](images/0a0af994f079b8f42f930584e41ecacbaf96d7a09c6e8b951856b888d6fad27b.jpg)  
Fig. 31.

The first and second derivatives of $\lambda$ are found from (31) to be given approximately by

$$
\left\{ \begin{array} { l l } { { \displaystyle { \lambda ^ { \prime } = \frac { 2 \tau - ( \tau _ { 2 } + \tau _ { 3 } ) } { ( \tau _ { 1 } - \tau _ { 2 } ) ( \tau _ { 1 } - \tau _ { 3 } ) } \lambda _ { 1 } + \frac { 2 \tau - ( \tau _ { 3 } + \tau _ { 1 } ) } { ( \tau _ { 2 } - \tau _ { 3 } ) ( \tau _ { 2 } - \tau _ { 1 } ) } \lambda _ { 2 } } } } \\ { { \displaystyle ~ + \frac { 2 \tau - ( \tau _ { 1 } + \tau _ { 2 } ) } { ( \tau _ { 3 } - \tau _ { 1 } ) ( \tau _ { 3 } - \tau _ { 2 } ) } \lambda _ { 3 } , } } \\ { { \displaystyle { \lambda ^ { \prime \prime } = \frac { 2 } { ( \tau _ { 1 } - \tau _ { 2 } ) ( \tau _ { 1 } - \tau _ { 3 } ) } \lambda _ { 1 } + \frac { 2 } { ( \tau _ { 2 } - \tau _ { 3 } ) ( \tau _ { 2 } - \tau _ { 1 } ) } \lambda _ { 2 } } } } \\ { { \displaystyle ~ + \frac { 2 } { ( \tau _ { 3 } - \tau _ { 1 } ) ( \tau _ { 3 } - \tau _ { 2 } ) } \lambda _ { 3 } . } } \end{array} \right.
$$

There are similar expressions in $\mu$ and ${ \pmb \nu }$

114.Determination of the Derivatives from more than Three Observations. If the observations were perfectly exact and near together, the more there were available the more exactly could $\lambda$ be determined for small values of $\tau$ ，and the more of its derivatives could be determined. Suppose there are four observations. Then $\lambda$ is defined by a third degree polynomial analogous to (31）which reduces to $\lambda _ { 1 } , \lambda _ { 2 } , \lambda _ { 3 } ,$ and $\lambda _ { 4 }$ for $\tau = \tau _ { 1 } , \tau _ { 2 } , \tau _ { 3 } $ and $\pmb { \tau _ { 4 } }$ respectively. The explicit expression for $\lambda$ is

$$
\left\{ \begin{array} { r } { \lambda = + \frac { ( \tau - \tau _ { 2 } ) ( \tau - \tau _ { 3 } ) ( \tau - \tau _ { 4 } ) } { ( \tau _ { 1 } - \tau _ { 2 } ) ( \tau _ { 1 } - \tau _ { 3 } ) ( \tau _ { 1 } - \tau _ { 4 } ) } \lambda _ { 1 } } \\ { + \frac { ( \tau - \tau _ { 3 } ) ( \tau - \tau _ { 4 } ) ( \tau - \tau _ { 1 } ) } { ( \tau _ { 2 } - \tau _ { 3 } ) ( \tau _ { 2 } - \tau _ { 4 } ) ( \tau _ { 2 } - \tau _ { 1 } ) } \lambda _ { 2 } } \\ { + \frac { ( \tau - \tau _ { 4 } ) ( \tau - \tau _ { 1 } ) ( \tau - \tau _ { 2 } ) } { ( \tau _ { 3 } - \tau _ { 4 } ) ( \tau _ { 3 } - \tau _ { 1 } ) ( \tau _ { 3 } - \tau _ { 2 } ) } \lambda _ { 3 } } \\ { + \frac { ( \tau - \tau _ { 1 } ) ( \tau - \tau _ { 2 } ) ( \tau - \tau _ { 3 } ) } { ( \tau _ { 4 } - \tau _ { 1 } ) ( \tau _ { 4 } - \tau _ { 2 } ) ( \tau _ { 4 } - \tau _ { 3 } ) } \lambda _ { 4 } , } \end{array} \right.
$$

from which the first,second,and third,but not higher,derivatives can be found.

It is obvious from this how to proceed for any number of observations. The process is unique and does not become excessively laborious unless the number of observations is considerable. The number of derivatives which can be determined,at least approximately，is one less than the number of observations, but no derivative higher than the third will in any case be used.If the observations extend over a long period so that the convergence of (28) fails or becomes slow for the largest values of $\pmb { \tau } _ { : }$ ,it is necessary to omit some of them in the discussion. Usually,owing to the errors in the observations,four or five will give $\lambda$ and its first two derivatives as accurately as any greater number.

115.The Approximations in the Determination of the Values of $\lambda , ~ \mu , ~ \nu$ and their Derivatives. In the applications it is important to know the character of the approximations which are made，and whether all the quantities employed are determined with the same degree of accuracy. It is obvious no exact numerical answers can be given to these questions because the orbits under consideration are undetermined. But it has been insisted that the values of $\pmb { \tau }$ must not be too great in order that the series (28) shall converge rapidly. Consequently，the values of $\boldsymbol { \tau }$ at the times of the observations can be considered as small quantities, and the degree of the approximation can be described in terms of the lowest powers of the $\tau _ { i }$ which occur in the neglected terms. This gives a definite meaning to the order of approximation,and experience shows that it is a satisfactory measure of the accuracy of the results when the time-intervals are limited as described in Art. 113.

Suppose first that only three observations have been made. The approximations in the determination of $\pmb { \lambda }$ and its derivatives arise from the fact that the higher terms of (28) are neglected. The coefficients ${ \mathfrak { c } } _ { 0 } , { \mathfrak { c } } _ { 1 } $ and ${ \pmb { c _ { 2 } } }$ are determined by

$$
\left\{ \begin{array} { l l } { c _ { 0 } + c _ { 1 } \tau _ { 1 } + c _ { 2 } \tau _ { 1 } ^ { 2 } = \lambda _ { 1 } - c _ { 3 } \tau _ { 1 } ^ { 3 } - c _ { 4 } \tau _ { 1 } ^ { 4 } - \cdots , } \\ { c _ { 0 } + c _ { 1 } \tau _ { 2 } + c _ { 2 } \tau _ { 2 } ^ { 2 } = \lambda _ { 2 } - c _ { 3 } \tau _ { 2 } ^ { 3 } - c _ { 4 } \tau _ { 2 } ^ { 4 } - \cdots , } \\ { c _ { 0 } + c _ { 1 } \tau _ { 3 } + c _ { 2 } \tau _ { 3 } ^ { 2 } = \lambda _ { 3 } - c _ { 3 } \tau _ { 3 } ^ { 3 } - c _ { 4 } \tau _ { 3 } ^ { 4 } - \cdots . . . } \end{array} \right.
$$

The errors of lowest degree in the $\tau _ { i }$ come from neglecting the terms in the right members which are multiplied by the unknown constant $c _ { 3 }$ .Let the errors be denoted by $\Delta c _ { 0 } , \ \Delta c _ { 1 } ,$ and $\Delta c _ { 2 }$ Then

$$
{ \begin{array} { r l } & { { \mathrm { 1 , } } \quad \tau _ { 1 } , \quad { \tau _ { 1 } } ^ { 2 } } \\ & { { \mathrm { 1 , } } \quad \tau _ { 2 } , \quad { \tau _ { 2 } } ^ { 2 } | \Delta c _ { 0 } = - | c _ { 3 } \tau _ { 3 } ^ { 3 } + c _ { 4 } \tau _ { 4 } ^ { 4 } + \cdots , \quad \tau _ { 2 } , \quad \tau _ { 2 } ^ { 2 } | } \\ & { { \mathrm { 1 , } } \quad \tau _ { 3 } , \quad { \tau _ { 3 } } ^ { 3 } } \end{array} }
$$

and similar expressions for $\Delta \pmb { c } _ { 1 }$ and $\Delta c _ { 2 }$ These determinants are easily reduced by the elementary rules for simplifying determinants,and it is found that

$$
\left\{ \begin{array} { l l } { \Delta c _ { 0 } = - c _ { 3 } \tau _ { 1 } \tau _ { 2 } \tau _ { 3 } - c _ { 4 } \tau _ { 1 } \tau _ { 2 } \tau _ { 3 } ( \tau _ { 1 } + \tau _ { 2 } + \tau _ { 3 } ) + \cdots , } \\ { \Delta c _ { 1 } = + c _ { 3 } ( \tau _ { 1 } \tau _ { 2 } + \tau _ { 2 } \tau _ { 3 } + \tau _ { 3 } \tau _ { 1 } ) } \\ { \qquad \quad \qquad \quad + c _ { 4 } ( \tau _ { 1 } + \tau _ { 2 } ) ( \tau _ { 2 } + \tau _ { 3 } ) ( \tau _ { 3 } + \tau _ { 1 } ) + \cdots , } \\ { \Delta c _ { 2 } = - c _ { 3 } ( \tau _ { 1 } + \tau _ { 2 } + \tau _ { 3 } ) } \\ { \qquad \quad - c _ { 4 } ( \tau _ { 1 } ^ { 2 } + \tau _ { 2 } ^ { 2 } + \tau _ { 3 } ^ { 2 } + \tau _ { 1 } \tau _ { 2 } + \tau _ { 2 } \tau _ { 3 } + \tau _ { 3 } \tau _ { 1 } ) + \cdots . } \end{array} \right.
$$

It follows from these equations that ${ \mathfrak { c } } _ { 0 } , \ { \mathfrak { c } } _ { 1 } ,$ and $\pmb { c _ { 2 } }$ are determined up to the third,second,and first orders respectively.

Now consider the first equation cf (28). Since $\pmb { c _ { 1 } }$ is multiplied by $\pmb { \tau }$ and $c _ { 2 }$ by $\tau ^ { 2 }$ ,each of the first three terms in the series for $\lambda$ is determined up to the third order in the $\tau _ { i } .$ 、On taking the first and second derivatives, it is seen that $\lambda ^ { \prime }$ and $\lambda ^ { \prime \prime }$ are determined up to the second and first orders respectively. Consequently, $\lambda$ in general is determined by the first terms of (28) more accurately than its first derivative,and its frst derivative in general is determined more accurately than its second derivative. These facts must be remembered in the applications.

116.Choice of the Origin of Time. The origin of time has not been specified as yet except that it has been supposed that it is near the dates of the observations so that $\tau _ { 1 } , \ \tau _ { 2 } ,$ and $\boldsymbol { \tau _ { 3 } }$ will be small． Any epoch $\pmb { t _ { 0 } }$ which satisfies this condition can be used as an origin,and the problem at once arises of determining what one is most advantageous.

The choice of the origin of time which has been universally made is the date of the second observation. That is, $t _ { 0 } = t _ { 2 }$ and therefore $\pmb { \tau _ { 2 } } = \mathbf { 0 }$ The value of $\lambda$ is exactly known at $\tau = \tau _ { 2 } = 0$ and the derivative of $\lambda$ at $t = t _ { 2 }$ is

$$
\lambda _ { 2 } { ' } = c _ { 1 } + 2 c _ { 2 } \tau _ { 2 } + \cdot \cdot \cdot = c _ { 1 } ,
$$

which is subject to the error $\Delta { c } _ { 1 }$ ，which,by (35),is in this case $\pmb { c _ { 3 } } \pmb { \tau _ { 3 } } \pmb { \tau _ { 1 } }$ 。And similarly,the error in ${ \lambda _ { 2 } } ^ { \prime \prime }$ is $\Delta c _ { 2 } = - \ c _ { 3 } [ \tau _ { 1 } + \tau _ { 3 } ]$ The error in ${ \lambda } _ { 2 } ^ { \prime }$ is of the second order while that in ${ \lambda _ { 2 } } ^ { \prime \prime }$ is of the first order. In general,an error of the first order is more serious than one of the second order. But it should be noticed that when $t _ { 0 } = t _ { 2 }$ the quantities $\pmb { \tau _ { 1 } }$ and $\pmb { \tau _ { 3 } }$ are opposite in sign；and if the intervals between the successive observations are equal, $\tau _ { 1 } + \tau \bullet = 0$ and the error in ${ \lambda _ { 2 } } ^ { \prime \prime }$ is also of the second order. Consequently，when $t _ { 0 } = t _ { 2 }$ it is advantageous to have the successive observations separated by as nearly equal time-intervals as possible. But unfavorable weather and other circumstances generally cause the observations to be unequally spaced.

Suppose the epoch of the frst observation is taken as the origin of time. The quantity $\lambda _ { 1 }$ is exactly known. The error in ${ \lambda _ { 1 } } ^ { \prime }$ is $\Delta c _ { 1 } = c _ { 3 } \tau _ { 2 } \tau _ { 3 }$ ,which is of the second order as before,but is approximately twice as great numerically as that in ${ \lambda _ { 2 } } ^ { \prime }$ because $\tau _ { 3 }$ now represents $k$ times the whole interval between the frst and third observations. The error in ${ \lambda _ { 1 } } ^ { \prime \prime }$ is $\Delta c _ { 2 } = - c _ { 3 } ( \tau _ { 2 } + \tau _ { 3 } )$ which is much larger than before because $\pmb { \tau _ { 3 } }$ now depends on the whole interval covered by the observations,and because $\pmb { \tau _ { 2 } }$ and $\pmb { \tau _ { 3 } }$ in this case are both positive. It follows from this that it is not advantageous to use the time of the first observation as the origin of time;and for similar reasons the epoch of the third observation is to be rejected.

The question now arises what should be taken for the origin of time when the epoch of the second observation is not midway between those of the other two. Since in general the error in $\gimel$ is only of the third order and that in $\lambda ^ { \prime }$ is only of the second,while $\lambda ^ { \prime \prime }$ is subject to an error of the first order,it is clear that the origin of time should be so chosen,if possible,as to make the first order error in $\lambda ^ { \prime \prime }$ vanish. It follows from the second equation of (35) that this result will be secured if

$$
\left\{ \begin{array} { l } { \tau _ { 1 } + \tau _ { 2 } + \tau _ { 3 } = k ( t _ { 1 } - t _ { 0 } ) + k ( t _ { 2 } - t _ { 0 } ) + k ( t _ { 3 } - t _ { 0 } ) = 0 , } \\ { { \mathrm { w h e n c e ~ } } t _ { 0 } = { \frac { 1 } { 3 } } ( t _ { 1 } : t + t _ { 2 } + t _ { 3 } ) . } \end{array} \right.
$$

The best choice of the origin of time is therefore given by the second of (36),and this value of $\scriptstyle t _ { 0 }$ becomes the date of the second observation when the successive observations are equally distant from one another. With this choice of $t _ { 0 }$ the errors in $\lambda ^ { \prime }$ and $\lambda ^ { \prime \prime }$ are of the second order,while $\lambda$ is known up to the third order.

117. The Approximations when there are Four Observatins. When there are four observations the equations which correspond to the last three of (28) are

$$
{ \left\{ \begin{array} { l l } { c _ { 0 } + c _ { 1 } \tau _ { 1 } + c _ { 2 } { \tau _ { 1 } } ^ { 2 } + c _ { 3 } { \tau _ { 1 } } ^ { 3 } = \lambda _ { 1 } - c _ { 4 } { \tau _ { 1 } } ^ { 4 } + \cdots , } \\ { c _ { 0 } + c _ { 1 } \tau _ { 2 } + c _ { 2 } { \tau _ { 2 } } ^ { 2 } + c _ { 3 } { \tau _ { 2 } } ^ { 3 } = \lambda _ { 2 } - c _ { 4 } { \tau _ { 2 } } ^ { 4 } + \cdots , } \\ { c _ { 0 } + c _ { 1 } \tau _ { 3 } + c _ { 2 } { \tau _ { 3 } } ^ { 2 } + c _ { 3 } { \tau _ { 3 } } ^ { 3 } = \lambda _ { 3 } - c _ { 4 } { \tau _ { 3 } } ^ { 4 } + \cdots , } \\ { c _ { 0 } + c _ { 1 } \tau _ { 4 } + c _ { 2 } { \tau _ { 4 } } ^ { 2 } + c _ { 3 } { \tau _ { 4 } } ^ { 3 } = \lambda _ { 4 } - c _ { 3 } { \tau _ { 4 } } ^ { 4 } + \cdots . . . . } \end{array} \right. }
$$

The determinant of the coefficients of $c _ { 0 } , c _ { 1 } , c _ { 2 } ,$ and $c _ { 3 }$ is

$$
\delta = { \left| \begin{array} { l l l l } { 1 , } & { \tau _ { 1 } , } & { { \tau _ { 1 } } ^ { 2 } , } & { { \tau _ { 1 } } ^ { 3 } } \\ { 1 , } & { \tau _ { 2 } , } & { { \tau _ { 2 } } ^ { 2 } , } & { { \tau _ { 2 } } ^ { 3 } } \\ { 1 , } & { \tau _ { 3 } , } & { { \tau _ { 3 } } ^ { 2 } , } & { { \tau _ { 3 } } ^ { 3 } } \\ { 1 , } & { \tau _ { 4 } , } & { { \tau _ { 4 } } ^ { 2 } , } & { { \tau _ { 4 } } ^ { 3 } } \end{array} \right| } = ( \tau _ { 2 } - \tau _ { 1 } ) ( \tau _ { 3 } - \tau _ { 1 } ) ( \tau _ { 4 } - \tau _ { 1 } ) ( \tau _ { 3 } - \tau _ { 2 } )
$$

which is not zero since the dates of the observations are distinct.

The errors of lowest order in $c _ { 0 } , \ c _ { 1 } , \ c _ { 2 } , $ and $c _ { 3 }$ are determined from (37)；when only the first terms in the right members are known they contain ${ c _ { 4 } }$ as a factor. Let these errors be represented by $\Delta c _ { 0 } , \Delta c _ { 1 } , \Delta c _ { 2 }$ and $\Delta { \boldsymbol { c } } _ { 3 }$ ； their orders in the $\tau _ { j }$ are required. The expression for $\Delta \ . c _ { \theta }$ is

$$
\Delta c _ { 0 } = { \frac { - c _ { 4 } } { \delta } } { \left| \begin{array} { l l l l } { \tau _ { 1 } { } ^ { 4 } , } & { \tau _ { 1 } , } & { \tau _ { 1 } { } ^ { 2 } , } & { \tau _ { 1 } { } ^ { 3 } } \\ { \tau _ { 2 } { } ^ { 4 } , } & { \tau _ { 2 } , } & { \tau _ { 2 } { } ^ { 2 } , } & { \tau _ { 2 } { } ^ { 3 } } \\ { \tau _ { 3 } { } ^ { 4 } , } & { \tau _ { 3 } , } & { \tau _ { 3 } { } ^ { 2 } , } & { \tau _ { 3 } { } ^ { 3 } } \\ { \tau _ { 4 } { } ^ { 4 } , } & { \tau _ { 4 } , } & { \tau _ { 4 } { } ^ { 2 } , } & { \tau _ { 4 } { } ^ { 3 } } \end{array} \right| } .
$$

When the factors $\tau _ { 1 } , \ \tau _ { 2 } , \ \tau _ { 3 } ,$ and $\tau _ { 4 }$ are removed from this determinant it is identical with $\delta$ except the columns are permuted. Three permutations of columns bring it to the form of $\pmb { \delta }$ ；hence

$$
\Delta c _ { 0 } = + c _ { 4 } \tau _ { 1 } \tau _ { 2 } \tau _ { 3 } \tau _ { 4 } .
$$

The expression for $\Delta \pmb { c } _ { 1 }$ is

$$
\Delta c _ { 1 } = { \frac { - c _ { 4 } } { \delta } } \left| \begin{array} { l l l l } { { 1 , } } & { { { \tau _ { 1 } } ^ { 4 } , } } & { { { \tau _ { 1 } } ^ { 2 } , } } & { { { \tau _ { 1 } } ^ { 3 } } } \\ { { 1 , } } & { { { \tau _ { 2 } } ^ { 4 } , } } & { { { \tau _ { 2 } } ^ { 2 } , } } & { { { \tau _ { 2 } } ^ { 3 } } } \\ { { 1 , } } & { { { \tau _ { 3 } } ^ { 4 } , } } & { { { \tau _ { 3 } } ^ { 2 } , } } & { { { \tau _ { 3 } } ^ { 3 } } } \\ { { 1 , } } & { { { \tau _ { 4 } } ^ { 4 } , } } & { { { \tau _ { 4 } } ^ { 2 } , } } & { { { \tau _ { 4 } } ^ { 3 } } } \end{array} \right| .
$$

If $\pmb { \tau _ { 2 } }$ is put equal to $\tau _ { 1 }$ in this determinant it vanishes because then two lines become the same. Therefore it is divisible by $\tau _ { 2 } \mathrm { ~ - ~ } \tau _ { 1 } .$ Similarly,it is divisible by $\tau _ { 3 } \mathrm { ~ - ~ } \tau _ { 1 } ,$ $\tau _ { 4 } \mathrm { ~ - ~ } \tau _ { 1 } ,$ $\tau _ { 3 } \mathrm { ~ - ~ } \tau _ { 2 } ,$ ， $\tau _ { 4 } - \tau _ { 2 } ,$ and $\tau _ { 4 } \mathrm { ~ - ~ } \tau _ { 3 }$ ; that is,it is divisible byδ.All the elements of each column are of the same degree；and since every term of the ex" pansion of a determinant has a factor from each column, the terms of the expansion are all of the same degree. The degree of this determinant is nine, because this is the sum of the degrees of its columns. Hence $\Delta { { c } _ { 1 } }$ is of the third degree because $\pmb { \delta }$ is of the sixth degree. Moreover,it is symmetrical in $\tau _ { 1 } , \ \cdots , \ \tau _ { 4 }$ because both $\delta$ and the numerator determinant are symmetrical in these quantities. Each term of the expansion contains $\pmb { \tau _ { \pmb { \mathscr { s } } } }$ only to the first degree because $\tau _ { j }$ occurs in the numerator determinant to the fourth degree as the highest,and in δ to the third degree. The numerical coefficient of each term in the expansion is the same, because of the symmetry,and it can be determined by the consideration of a single term. It is found by considering the product of the main diagonal elements that it is $^ { + 1 }$ .Analogous discussions can be made for $\Delta c _ { 2 }$ and $\Delta c _ { 3 }$ ,and it is found in this way that

$$
\left\{ \begin{array} { l l } { \Delta c _ { 1 } = - c _ { 4 } [ \tau _ { 1 } \tau _ { 2 } \tau _ { 3 } + \tau _ { 2 } \tau _ { 3 } \tau _ { 4 } + \tau _ { 3 } \tau _ { 4 } \tau _ { 1 } + \tau _ { 4 } \tau _ { 1 } \tau _ { 2 } ] , } \\ { \Delta c _ { 2 } = + c _ { 4 } [ \tau _ { 1 } \tau _ { 2 } + \tau _ { 1 } \tau _ { 3 } + \tau _ { 1 } \tau _ { 4 } + \tau _ { 2 } \tau _ { 3 } + \tau _ { 2 } \tau _ { 4 } + \tau _ { 3 } \tau _ { 4 } ] , } \\ { \Delta c _ { 3 } = - c _ { 4 } [ \tau _ { 1 } + \tau _ { 2 } + \tau _ { 3 } + \tau _ { 4 } ] . } \end{array} \right.
$$

It follows from (38)and (39) that when there are four observations $\lambda , \lambda ^ { \prime } , \lambda ^ { \prime \prime }$ ，and $\lambda ^ { \prime \prime \prime }$ are determined up to small quantities of the fourth,third,second,and first order respectively. Ordinarily $\lambda ^ { \prime \prime \prime }$ is not needed, though it becomes useful when the solution is double,as it may be,in determining which of them belongs to the physical problem.In this latter case it is advantageous to make $\Delta \pmb { c } _ { 3 }$ vanish by determining $t _ { 0 }$ so that

$$
\left\{ \begin{array} { l l } { \tau _ { 1 } + \tau _ { 2 } + \tau _ { 3 } + \tau _ { 4 } = 0 , \quad \mathrm { w h e n c e } } \\ { t _ { 0 } = \frac { 1 } { 4 } ( t _ { 1 } + t _ { 2 } + t _ { 3 } + t _ { 4 } ) . } \end{array} \right.
$$

If the solution of the problem is made to depend only on $\lambda , \lambda ^ { \prime }$ ， and $\lambda ^ { \prime \prime }$ ，it is most advantageous to choose $t _ { 0 }$ so that $\Delta c _ { 2 }$ shall vanish, for then all the quantities are determined up to the third order. This condition becomes

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \tau _ { 1 } \tau _ { 2 } + \tau _ { 1 } \tau _ { 3 } + \tau _ { 1 } \tau _ { 4 } + \tau _ { 2 } \tau _ { 3 } + \tau _ { 2 } \tau _ { 4 } + \tau _ { 3 } \tau _ { 4 } = 0 , } & { \mathrm { w h e n c e } } \\ { 6 t _ { 0 } { } ^ { 2 } - 3 ( t _ { 1 } + t _ { 2 } + t _ { 3 } + t _ { 4 } ) t _ { 0 } + t _ { 1 } t _ { 2 } } & { } \\ { \qquad \quad \qquad \quad \qquad \qquad \quad \qquad \qquad \qquad \quad + t _ { 1 } t _ { 3 } + t _ { 1 } t _ { 4 } + t _ { 2 } t _ { 3 } + t _ { 2 } t _ { 4 } + t _ { 3 } t _ { 4 } = 0 . } \end{array} \right. } \end{array}
$$

The values of $t _ { 0 }$ determined by this quadratic equation are of no practical value unless they are real. The discriminant of the quadratic is

$$
\begin{array} { r l r } {  { 9 ( t _ { 1 } + t _ { 2 } + t _ { 3 } + t _ { 4 } ) ^ { 2 } - 2 4 ( t _ { 1 } t _ { 2 } + t _ { 1 } t _ { 3 } + t _ { 1 } t _ { 4 } + t _ { 2 } t _ { 3 } + t _ { 2 } t _ { 4 } + t _ { 3 } t _ { 4 } ) } } \\ & { } & { ~ \textmd { = } H = 3 ( t _ { 1 } - t _ { 2 } ) ^ { 2 } + 3 ( t _ { 1 } - t _ { 3 } ) ^ { 2 } + 3 ( t _ { 1 } - t _ { 4 } ) ^ { 2 } } \\ & { } & { ~ \textmd { \textmd { ering } } 3 ( t _ { 2 } - t _ { 3 } ) ^ { 2 } + 3 ( t _ { 2 } - t _ { 4 } ) ^ { 2 } + 3 ( t _ { 3 } - t _ { 4 } ) ^ { 2 } > 0 . } \end{array}
$$

Therefore the solutions are always real, and are explicitly

$$
t _ { a } = \frac { 3 ( t _ { 1 } + t _ { 2 } + t _ { 3 } + t _ { 4 } ) \pm \sqrt { H } } { 1 2 } .
$$

In order to get a concrete idea of the nature of the results suppose the intervals between the successive observations are equal to $\pmb { T }$ .Then (42） gives

$$
\begin{array} { r } { t _ { 0 } = \frac { 1 } { 4 } ( t _ { 1 } + t _ { 2 } + t _ { 3 } + t _ { 4 } ) \pm \frac { 1 } { 6 } \sqrt { 1 5 } T . } \end{array}
$$

The first term on'the right is the mean epoch of the observations, and the two values of $t _ { 0 }$ are at the distance $\scriptstyle { \frac { 1 } { 6 } } { \sqrt { 1 5 } } T$ either side of this time. Since the interval between the mean epoch and $t _ { + }$ or $t _ { 3 }$ is $\scriptstyle { \frac { \mathbf { 1 } } { \mathbf { 2 } } } T$ ,it follows that $t _ { 9 }$ is between $t _ { 1 }$ and $t _ { 2 }$ and distant $( { \textstyle { \frac { 1 } { 6 } } } \sqrt { 1 5 } - { \textstyle { \frac { 1 } { 2 } } } ) T = { \textstyle { \frac { 1 } { 6 } } } T$ approximately from $t _ { 2 }$ ,or symmetrically situated between $t _ { 3 }$ and $t _ { 4 }$ ，In practice it will be most convenient to choose $t _ { 0 } = t _ { 2 }$ or $t _ { 0 } = t _ { 3 }$ ，for then $\lambda$ is given exactly, the coefficients of (33) are as simple as possible,and (41) is nearly satisfied.

The discusson when there are five or more observations can be carried out in a similar manner. For each additional observation one additional coefficient in the series (28) can be determined, and those which were determined previously become known to one order higher in the $\tau _ { j } .$ ，In each case one additional order of accuracy in the determination of $\lambda ^ { \prime \prime }$ can be secured by properly selecting $t _ { 0 _ { } }$ ,but it is simplest to let $t _ { 0 }$ equal the date of the observation which is nearest the mean epoch of all of the observations.

118.The Fundamental Equations. The fundamental equations of the method of Laplace are (10), where $\lambda , \mu , \nu , \lambda ^ { \prime } , \mu ^ { \prime } , \nu ^ { \prime } , \lambda ^ { \prime \prime } , \mu ^ { \prime \prime } , \nu ^ { \prime \prime }$ are given by (31) and (32) and corresponding equations in $\pmb { \mu }$ and $\pmb { \nu }$ · The solution of equations (10) for $\rho , \rho ^ { \prime }$ ,and $\pmb { \rho } ^ { \prime \prime }$ is

$$
\left\{ \begin{array} { l } { \displaystyle \rho = \frac { D _ { 1 } } { D } \left[ \frac { 1 } { R ^ { 3 } } - \frac { 1 } { r ^ { 3 } } \right] , } \\ { \displaystyle \rho ^ { \prime } = \frac { D _ { 2 } } { 2 D } \left[ \frac { 1 } { R ^ { 3 } } - \frac { 1 } { r ^ { 3 } } \right] , } \\ { \displaystyle \rho ^ { \prime \prime } = \frac { 1 } { D } \left[ D _ { 3 } - \frac { D _ { 1 } } { r ^ { 3 } } \right] \left[ \frac { 1 } { R ^ { 3 } } - \frac { 1 } { r ^ { 3 } } \right] , } \end{array} \right.
$$

where

$$
\left\{ \begin{array} { c c } { { D = + \left| \begin{array} { c c c } { { \lambda , } } & { { \lambda ^ { \prime } , } } & { { \lambda ^ { \prime \prime } } } \\ { { \mu , } } & { { \mu ^ { \prime } , } } & { { \mu ^ { \prime \prime } } } \\ { { \nu , } } & { { \nu ^ { \prime } , } } & { { \nu ^ { \prime \prime } } } \end{array} \right| , } } & { { D _ { 1 } = - \left| \begin{array} { c c c } { { \lambda , } } & { { \lambda ^ { \prime } , } } & { { X } } \\ { { \mu , } } & { { \mu ^ { \prime } , } } & { { Y } } \\ { { \nu , } } & { { \nu ^ { \prime } , } } & { { Z } } \end{array} \right| , } } \\ { { D _ { 2 } = - \left| \begin{array} { c c c } { { \lambda , } } & { { X , } } & { { \lambda ^ { \prime \prime } } } \\ { { \mu , } } & { { Y , } } & { { \mu ^ { \prime \prime } } } \\ { { \nu , } } & { { Z , } } & { { \nu ^ { \prime \prime } } } \end{array} \right| , } } & { { D _ { 3 } = - \left| \begin{array} { c c c } { { X , } } & { { \lambda ^ { \prime } , } } & { { \lambda ^ { \prime \prime } } } \\ { { Y , } } & { { \mu ^ { \prime } , } } & { { \mu ^ { \prime \prime } } } \\ { { Z , } } & { { \nu ^ { \prime } , } } & { { \nu ^ { \prime \prime } } } \end{array} \right| . } } \end{array} \right.
$$

These determinants are subject to small errors because of the fact that the higher terms of equations (28) have been neglected. After $\pmb { \rho }$ and $\pmb { \rho } ^ { \prime }$ have been approximately determined corrections can be made for these omissons. The determinants are also subject to small errors because they have been developed under the tacit assumption that the observations were made from the position of the center of the earth instead of from one or more points on its surface. After the approximate distances have been determined the observations can be corrected for the effects of the observer's position on the surface of the earth.

119.The Equations for the Determination of $\pmb { r }$ and $\rho$ Consider the triangle formed by $s , \mathbf { \boldsymbol { E } }$ and $\boldsymbol { C }$ Let $\psi$ represent the angle at $\boldsymbol { \mathscr { E } }$ and $\varphi$ that at $c$ .Then it follows that

![](images/28fad1ff862120c93bea78c7c3806d51f39588412945ea3707d62082090953fe.jpg)  
Fig. 32.

$$
\left\{ \begin{array} { c } { { R \cos \psi = X \lambda + Y \mu + Z \nu , } } \\ { { \ } } \\ { { \rho = R \frac { \sin { ( \psi + \varphi ) } } { \sin { \varphi } } , } } \\ { { \ } } \\ { { r = R \frac { \sin { \psi } } { \sin { \varphi } } . } } \end{array} \right.
$$

When equations (46) are substituted in the first equation of (44) the result is

$$
\stackrel { \mathrm { R e ~ } \ast \mathrm { w o s e ~ } \ast \mathrm { \infty } } { \mathrm { R } } \mathrm { ~ s i n ~ } \psi \mathrm { ~ c o s ~ } \varphi + \bigg [ R \mathrm { \cos } \psi - \frac { D _ { 1 } } { D R ^ { 3 } } \bigg ] \mathrm { \sin ~ } \varphi = \frac { - D _ { 1 } } { D R ^ { 3 } \mathrm { \sin } ^ { 3 } \psi } \mathrm { \sin } ^ { 4 } \varphi .
$$

In order to simplify this expression let

$$
\left\{ \begin{array} { c } { N \sin m = R \sin \psi , } \\ { N \cos m = R \cos \psi - \displaystyle \frac { D _ { 1 } } { D R ^ { 3 } } , } \\ { M = \displaystyle \frac { - \ N D R ^ { 3 } \sin ^ { 3 } \psi } { D . } , } \end{array} \right.
$$

where the sign of $N$ will be so cnosen that $M$ shall be positive. With this determination of the sign of $N$ the first two equations of (47) uniquely determine $N$ and $\pmb { m }$ ,and the equation in $\varphi$ becomes simply

$$
\sin ^ { 4 } \varphi = M \sin ( \varphi + m ) .
$$

The quantities $M$ and $^ { m }$ are known and $M$ is positive.

Now consider the solution of (48) for $\varphi$ Since $\pmb \rho = { \bf 0 }$ ， $r = R$ is a solution of the problem,it follows from (48) that $\varphi = \pi - \psi$ is a solution of (48). This solution belongs to the position of the observer and is to be rejected. It follows from Fig.32 that the $\varphi$ belonging to the physical problem,which must exist if the computation is made from good observations,satisfies the inequality

$$
\varphi < \pi - \psi .
$$

The solutions of (48) are the intersections of the curves defined by the equations

$$
\left\{ \begin{array} { l l } { y _ { 1 } = \sin ^ { 4 } \varphi , } \\ { y _ { 2 } = M \sin { ( \varphi + m ) } . } \end{array} \right.
$$

For m negative and near zero and $M$ somewhat less than unity these curves have the relation shown in Fig. 33.

![](images/d1c50a37204bc475bcde0c639ad78f0602252b0602e928b703a30b0f53a74cf2.jpg)  
Fig. 33.

Consider frs the case where $\frac { D _ { 1 } } { D }$ is positive. Since both $\pmb { \rho }$ and $\pmb { r }$ must be positive,it follows from the first of (44) that in this case $r > R$ Since $\psi$ is less than $\mathbf { 1 8 0 ^ { \circ } }$ ,it follows from (47） that $N$ is negative,and that $\textbf { \textit { m } }$ is in the third or fourth quadrant.

In case $^ { m }$ is in the fourth quadrant the ascending branch of the curve $y _ { 2 }$ crosses the $\varphi \cdot$ -axis in the first quadrant,and, if $M < 1$ ， the relations of the curves are as indicated in Fig. 33. If $\pmb { m }$ is near $1 8 0 ^ { \circ }$ there are three solutions, $\varphi _ { 1 } , ~ \varphi _ { 2 } ,$ and $\varphi _ { 3 }$ ，one of which is $\pi - \psi$ and belongs to the positionof theobserver.If $\varphi _ { 3 } = \pi - \psi ,$ both $\varphi _ { 1 }$ and $\varphi _ { 2 }$ fulfill all the conditions of the problem and it can not be determined which belongs to the orbit of the observed body without additional information. However, it might happen that $\varphi _ { 1 }$ would give so great values of $\pmb { r }$ and $\pmb { \rho }$ that it would be known from practical observational considerations that the body would be invisible; it would be known in this case that $\varphi _ { 2 }$ ，which would give a smaller $r$ ,belongs to the physical problem.If $\varphi _ { 2 } = \pi - \psi _ { 3 }$ it follows from (49） that $\varphi _ { 1 }$ belongs to the problem. The case $\varphi _ { 1 } = \pi - \psi$ cannot occur for then the physical problem could have no solution.If,for a fixed $M$ ,the ascending branch of the curve $y _ { 2 }$ moves to the right the roots $\varphi _ { 1 }$ and $\varphi _ { 2 }$ approach coincidence;and as it moves farther to the right $\varphi _ { 3 }$ alone remains real. This case,which corresponds to $\mathscr { m }$ far from $1 8 0 ^ { \circ }$ in the fourth quadrant or in the third quadrant,cannot arise,for then the problem would have no solution.Therefore, if $\frac { D _ { 1 } } { D }$ is positive, then $r > R$ ,m is in the fourth quadrant,and there are one or two possible solutions of the physical problem according as $\varphi _ { 2 }$ or $\varphi _ { 3 }$ equals $\pi - \psi$

Now suppose $\frac { D _ { 1 } } { D }$ is negative. In this case $r < R$ and m is in the first or second quadrant.If m is in the first quadrant the descending branch of the curve $y _ { 2 }$ crosses the $\varphi$ -axis in the second quadrant,and for a small $\pmb { m }$ and $M < 1$ the relations are as shown in Fig 34. In this case the solution of the problem is unique or double according as $\varphi _ { 2 }$ or $\varphi _ { 3 }$ equals $\pi - \psi$ .If m is in the second quadrant the descending branch of thə curve $y _ { 2 }$ crosses the $\varphi$ -axis in the first quadrant, $\varphi _ { 2 }$ and $\varphi _ { 3 }$ are not real,and the problem has no solution. Therefore, if $\frac { D _ { 1 } } { D }$ is negative, then $r < R$ mis in the first quadrant,and there are one or two possible solutions of the physical problem according as $\varphi _ { 2 }$ or $\varphi _ { 3 }$ equals $\pi - \psi$

![](images/ce9de4373f2d8ea7a7a52dbc810037711100260724a444c82d281b790b9059fd.jpg)  
Fig. 34.

120.The Condition for a Unique Solution. The solution of the physical problem is unique whether $\frac { D _ { 1 } } { D }$ is positive or negative if $\varphi _ { 2 } = \pi - \psi _ { ; }$ ,and otherwise it is double.Suppose $\varphi = \pi - \psi + \epsilon ,$ where e is a small positive number. When $\frac { D _ { 1 } } { D }$ is positive, it is seen from Fig.33 that if $\varphi _ { 2 } = \pi - \psi$ the difference $y _ { 1 } - y _ { 2 }$ is positive for $\varphi = \varphi _ { 2 } + \epsilon$ and, when $\frac { D _ { 1 } } { D }$ is negative, it is seen from Fig.34 that $y _ { 1 } - y _ { 2 }$ is negative for $\varphi = \varphi _ { 2 } + \epsilon = \pi - \psi + \epsilon .$

It follows from (50） that $y _ { 1 }$ and $y _ { 2 }$ can be expanded as power series in e when $\varphi = \pi - \psi + \epsilon$ 、The first two terms of the difference are

$$
\begin{array} { c } { y _ { 1 } - y _ { 2 } = [ \sin ^ { 4 } ( \pi - \psi ) - M \sin ( \pi - \psi + m ) ] } \\ { + [ 4 \sin ^ { 3 } ( \pi - \psi ) \cos ( \pi - \psi ) } \\ { - M \cos { ( \pi - \psi + m ) } ] \epsilon + \cdots . } \end{array}
$$

The term independent of $\epsilon$ is zero because $\varphi = \pi - \psi$ is a solution of (48). A reduction of the coefficient of $\epsilon$ by equations (47) and (48) gives

$$
y _ { 1 } - y _ { 2 } = \frac { M R } { N } \left[ 1 + \frac { 3 D _ { 1 } } { D \bar { R } ^ { 4 } } \cos \psi \right] \epsilon + \cdot \cdot \cdot .
$$

Therefore the condition that the solution of the physical problem shall be unique is

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { 1 } { N } \left[ 1 + \frac { 3 D _ { 1 } } { D R ^ { 4 } } \cos \psi \right] > 0 \quad \mathrm { i f } \quad \displaystyle \frac { D _ { 1 } } { D } > 0 , } \\ { \displaystyle \frac { 1 } { N } \left[ 1 + \frac { 3 D _ { 1 } } { D R ^ { 4 } } \cos \psi \right] < 0 \quad \mathrm { i f } \quad \displaystyle \frac { D _ { 1 } } { D } < 0 . } \end{array} \right.
$$

This function is completely determined by the observations, and consequently it is known without solving (48) whether the solution of the problem is unique or double.

The limit of the inequalities (52) is

$$
1 + { \frac { 3 D _ { 1 } } { D R ^ { 4 } } } \cos \psi = 0 .
$$

On eliminating cos $\psi$ and $\frac { D _ { 1 } } { D }$ by the first equations of (44) and (46),it is found that

$$
\rho ^ { 2 } = r ^ { 2 } + \frac { 2 } { 3 } \frac { R ^ { 5 } } { r ^ { 3 } } - \frac { 5 } { 3 } R ^ { 2 } .
$$

The minimum value of the right member of this equation,considered as a function of $\pmb { r }$ ,is zero；therefore for each value of $\pmb { r }$ there is a unique positive value of $\pmb { \rho }$ ：All points defined by pairs of values of $\pmb { r }$ and $\pmb { \rho }$ which satisfy (54) are on the boundary of the regions where the inequalities (52) are satisfied. These boundary surfaces are evidently surfaces of revolution around the line joining the earth and the sun. The section of these surfaces by & plane through the line $\mathtt { S E }$ is shown in Fig.35.\*

![](images/1aac7521f4cc4927d25853f8f73f0ab1e3bacc268070863c03103cd35ab8a35b.jpg)  
Fig. 35.

The surfaces defined by (54) divide space into four parts, two of which in the diagram are shaded,and two of which are plain. The function (52) has the same sign throughout each of these regions and changes sign when the boundary surface is crossed at any ordinary point. This is a special case of a general proposition which will be proved.

Suppose $x _ { 0 } , y _ { 0 } , z _ { 0 }$ is an ordinary point on the surface defined by $F ( x , \ y , \ z ) = 0$ Consider the value of $\pmb { F }$ at $x _ { 0 } + \Delta x$ ， $y _ { 0 } + \Delta y ,$ $z _ { 0 } + \Delta z$ ,where $\Delta x , \Delta y$ ,and $\Delta \boldsymbol { z }$ are small. The value of the function at this point is

$$
\begin{array} { r } { F ( x _ { 0 } + \Delta x , y _ { 0 } + \Delta y , z _ { 0 } + \Delta z ) \quad \quad } \\ { \quad = F ( x _ { 0 } , y _ { 0 } , z _ { 0 } ) + \frac { \partial F } { \partial x } \Delta x + \frac { \partial F } { \partial y } \Delta y + \frac { \partial F } { \partial z } \Delta z + \cdots . } \end{array}
$$

The first term in the right member of this equation is zero because $x _ { 0 } , \ y _ { 0 } , z _ { 0 }$ is on the surface. Now suppose the point ${ \pmb x } _ { 0 } + \Delta { \pmb x } _ { : }$ ： is on the perpendicular to the surface at $x _ { 0 } , y _ { 0 } , z _ { 0 }$ .Then

$$
\Delta x = { \frac { p { \frac { \partial F } { \partial x } } } { \sqrt { \left( { \frac { \partial F } { \partial x } } \right) ^ { 2 } + \left( { \frac { \partial F } { \partial y } } \right) ^ { 2 } + \left( { \frac { \partial F } { \partial z } } \right) ^ { 2 } } } } ,
$$

$$
\Delta y = \frac { p \frac { \partial F } { \partial y } } { \sqrt { \left( \frac { \partial F } { \partial x } \right) ^ { 2 } + \left( \frac { \partial F } { \partial y } \right) ^ { 2 } + \left( \frac { \partial F } { \partial z } \right) ^ { 2 } } } ,
$$

$$
\Delta z = \frac { p \frac { \partial { \cal F } } { \partial { z } } } { \sqrt { \left( \frac { \partial { \cal F } } { \partial x } \right) ^ { 2 } + \left( \frac { \partial { \cal F } } { \partial y } \right) ^ { 2 } + \left( \frac { \partial { \cal F } } { \partial z } \right) ^ { 2 } } } ,
$$

where $p$ is the distance from ${ \boldsymbol { x } } _ { 0 } , { \boldsymbol { y } } _ { 0 } , { \boldsymbol { z } } _ { 0 }$ to $x _ { 0 } + \Delta x , y _ { 0 } + \Delta y , z _ { 0 } + \Delta z ,$ because the factors by which $p$ is multiplied are the direction cosines of the normai to the surface. On one side of the surface $p$ is positive,and on the other side it is negative. The expression for the value of the function $\pmb { F }$ at the point $x _ { 0 } + \Delta x _ { \mathrm { { i } } }$ ，.…· becomes

$$
{ \begin{array} { r l } & { \operatorname { \mathcal { F } } ( x _ { 0 } + \Delta x , y _ { 0 } + \Delta y , z _ { 0 } + \Delta z ) } \\ & { \qquad = p \left[ \left( { \frac { \partial F } { \partial x } } \right) ^ { 2 } + \left( { \frac { \partial F } { \partial y } } \right) ^ { 2 } + \left( { \frac { \partial F } { \partial z } } \right) ^ { 2 } \right] ^ { \frac { 1 } { 4 } } + p ^ { 2 } \left[ \right] + \cdots . } \end{array} }
$$

For $p$ very small the sign of the function is determined by the sign of the first term on the right whose coefficient is not zero. Since $x _ { 0 } , \ y _ { 0 } , \ z _ { 0 }$ is by hypothesis an ordinary point of the surface, not all of the first partial derivatives of $\pmb { F }$ are zero,and consequently the sign of the function changes with the change of sign of $p$ .That is, the function changes sign when the surface for which it is zero is crossed; and it does not change sign at any other finite point because the function is continuous.

In order to find in which of the four regions of Fig.35 the solution is unique,and in which it is double,consider a point on the line $_ { S E }$ to the left of $\pmb { \cal E }$ At such a point $r = \rho + R$ ， $\psi = \pi$ and it follows that

$$
1 + \frac { 3 D _ { 1 } } { D R ^ { 4 } } \cos \psi = 1 - \frac { 3 D _ { 1 } } { D R ^ { 4 } } = 1 - \frac { 3 ( \rho + R ) ^ { 3 } } { R [ \rho ^ { 2 } + 3 \rho R + 3 R ^ { 2 } ] } ,
$$

which is clearly negative for $\pmb { \rho }$ very large. Since in this case $r > R$ it follows that $\frac { D _ { 1 } } { D } > 0 .$ $N < 0$ and the first inequality of (52) is the one under consideration. Since the inequality is satisfied the solution of the problem is unique if the observed body is in the unshaded area to the left of $\mathbfit { \Delta } E$ .If the surface is crossed into the larger shaded area at a point for which $r > R$ the function changes sign while the sign of $N$ is unchanged. Then the first inequality of (52) is not satisfied and the solution of the physical problem is double. In this region the function (53) is positive and $N$ is negative. If the surface is crossed into the smaller unshaded area the function (53） becomes negative, $\boldsymbol { \mathbf { \mathit { N } } }$ becomes positive,and the second inequality of (52),which is now in question, is satisfied. Therefore the solution is unique in this unshaded area. It is shown similarly that it is double in the smaller shaded area.

121. Use of a Fourth Observation in Case of a Double Solution. Suppose $\varphi _ { 3 } = \pi - \psi$ so that there are two solutions of (48) which correspond to the conditions of the physical problem.One method of determining which solution actually belongs to the physical problem,in case there are four observations,is obviously to develop (48),using the fourth observation instead of one of the original three. In general, this will make the result unique.

A better method of resolving the ambiguous case can be developed from equations (44). Eliminate $\pmb { r }$ from the second and third equations of (44) by means of the first. The results are

$$
\left\{ \begin{array} { l l } { \rho ^ { \prime } = \displaystyle \frac { D _ { 2 } } { 2 D _ { 1 } } \rho = P \rho , \qquad P = \displaystyle \frac { D _ { 2 } } { 2 D _ { 1 } } , } \\ { \rho ^ { \prime \prime } = \displaystyle \frac { \rho } { D _ { 1 } } \left[ D _ { 3 } - \displaystyle \frac { D _ { 1 } } { R ^ { 3 } } + D _ { \rho } \right] . } \end{array} \right.
$$

The derivative of the first of these equations is

$$
\rho ^ { \prime \prime } = P ^ { \prime } \rho + P \rho ^ { \prime } = ( P ^ { \prime } + P ^ { 2 } ) \rho ,
$$

which equated to the right member of the second equation gives

$$
D _ { 3 } - \frac { D _ { 1 } } { R ^ { 3 } } + D \rho = D _ { 1 } ( P ^ { \prime } + P ^ { 2 } ) .
$$

Since this equation is linear $\rho$ is uniquely determined unless $D$ is zero. The determinant $D$ will be examined in Art.124. Equation (55) must be based upon not less than four observations,for $P ^ { \prime }$ involves $\lambda ^ { \prime \prime \prime } , \mu ^ { \prime \prime \prime }$ ，and $\nu ^ { \prime \prime \prime }$ which cannot be determined, even approximately,from three observations.

122.The Limits on m and $M$ .In an actual problem of the determination of an orbit the constants m and $M$ are subject to the condition that equation (48) shall have three real roots between 0 and $\pi$ .The limits imposed by this condition can be determined from the conditions that it shall have double roots； for,suppose $M$ is fixed and that m varies. In the first case, represented in Fig. 33.there are three real solutions of (48) until, the curve $_ { y _ { 2 } }$ moving to the right, $\varphi _ { 1 }$ and $\varphi _ { 2 }$ become equal;and in the second case,represented in Fig. 34,there are three real solutions of (48) until, the curve $y _ { 2 }$ moving to the left, $\varphi _ { 2 }$ and $\varphi _ { 3 }$ become equal. The two cases are not essentially different for $\varphi _ { 1 }$ in the first case corresponds exactly to $\varphi _ { 3 }$ in the second. Similarly,if m remains fixed and $M$ , starting from a smal value, increases there are three real solutions of (56) until either $\varphi _ { 2 }$ and $\varphi _ { 3 }$ or $\varphi _ { 1 }$ and $\varphi _ { 2 }$ ,in the first and second cases respectively，become equal. When the limits are passed for which two values of $\varphi$ which satisfy (48) are equal, there is only one real solution between O and $\pmb { \pi }$

The conditions that (48) shall have a double root are

$$
\begin{array} { r } { \sin ^ { 4 } \varphi = M \sin { ( \varphi + m ) } , } \\ { \left\{ \begin{array} { r } { \sin ^ { 4 } \varphi \cos \varphi = M \cos { ( \varphi + m ) } , } \\ { 4 \sin ^ { 3 } \varphi \cos \varphi = M \cos { ( \varphi + m ) } . } \end{array} \right. } \end{array}
$$

The solution of the quotient of these equations for tan $\pmb { \varphi }$ is

$$
\tan \varphi = \frac { - \textnormal { 3 } \pm \sqrt { 9 - 1 6 \tan ^ { 2 } m } } { 2 \tan m } .
$$

It follows at once that $\mathscr { m }$ is subject to the condition

$$
9 - 1 6 \tan ^ { 2 } m \geq 0
$$

in order that the double root shall be real． Hence

$$
3 2 3 ^ { \circ } 8 ^ { \prime } \equiv m \leq 3 6 0 ^ { \circ } , \qquad 0 \equiv m \leq 3 6 ^ { \circ } 5 2 ^ { \prime } ,
$$

the first range for $\textbf { \textit { m } }$ belonging to the first case, represented in Fig. 33,and the second to the second case, represented in Fig. 34.

For each $\textbf { \textit { m } }$ there are two values of $\varphi$ defined by (57） between O and $\pi$ 、In the first case,in which tan $\textbf { \textit { m } }$ is negative, tan $\varphi$ is positive whether the upper or the lower sign is used before the radical, and it is smallest when the upper sign is used.Therefore the value of $\varphi$ defined by (57) when the upper sign is used is that one for which $\varphi _ { 1 } = \varphi _ { 2 }$ in Fig.33,and the one determined when the lower sign is used is that one for which $\varphi _ { 2 } = \varphi _ { 3 }$ .When m has the limiting value for which the radical vanishes φ1 = φ2 = Φ3. The discussion is analogous in the second case in which tan m is positive.

The limiting values of $\varphi$ ,defined by (57),which correspond to the limiting values of $\textbf { \textit { m } }$ as given in (58), are respectively

$$
\varphi = 1 1 6 ^ { \circ } 3 4 ^ { \prime } , \qquad \varphi = 6 3 ^ { \circ } 2 6 ^ { \prime } ,
$$

and for both of these values of $\varphi$ the value of $M$ defined by (56) is $M = 1 . 4 3 1$ .This is the maximum $M$ for which (48) can have three real roots between O and $\pmb { \pi }$ 、In order that the three roots shall be real for this $M$ the value of m must be $3 6 ^ { \circ } ~ 5 2 ^ { \prime }$ or $\mathrm { { 3 2 3 ^ { \circ } 8 ^ { \prime } } }$ ， and the three roots are then equal.

Consider the first case and suppose m starts from $\mathbf { 3 2 3 ^ { \circ } 8 ^ { \prime } }$ and increases to $3 6 0 ^ { \circ }$ .The two values of $\varphi$ defined by (57） start from $6 3 ^ { \circ } \ 2 6 ^ { \prime }$ ．One goes to O and the other to $9 0 ^ { \circ } .$ The two corresponding values of $M$ start from 1.431，and one goes to 0 and the other to unity. For each value of $\textmu m$ between the limits (58)there are two limits between which $M$ must lie in order that (48)shall have three real solutions. In constructing a table of the solutions of (48) depending on the two independent parameters, $M$ and $m _ { \parallel }$ ，these limits should be observed in order to reduce the work as much as possible.

123.Differential Corrections. Suppose the approximate solution of (48) has been found from the graphs of $_ { y _ { 1 } }$ and $y _ { 2 }$ orby numerical trials,or from the tables of the roots of this equation. Let $\varphi _ { 0 }$ represent the approximate solution and $\varphi _ { 0 } + \Delta \varphi$ the exact solution.The problem is to find $\Delta \varphi$

Let

$$
\sin ^ { 4 } \varphi _ { 0 } - M \sin \left( \varphi _ { 0 } + m \right) = \eta ,
$$

where $\pmb { \eta }$ will be a small quantity if $\varphi _ { 0 }$ is an approximate solution of (48).If $\varphi _ { 0 } + \Delta \varphi$ is substituted in (48) in place of $\varphi _ { . }$ ,the resvilt expanded asa power series in $\Delta \varphi$ becomes

$$
- \mathrm { \Delta } \eta = [ 4 \sin ^ { 3 } \varphi _ { 0 } \cos \varphi _ { 0 } - M \cos ( \varphi _ { 0 } + m ) ] \Delta \varphi + [ \mathrm { \Delta } ] \left( \Delta \varphi \right) ^ { 2 } + \cdots .
$$

This power series can be inverted, giving $\Delta \varphi$ as a power series in $\pmb { \eta }$ The result is

$$
\Delta \varphi = \frac { - \eta } { 4 \sin ^ { 3 } \varphi _ { 0 } \cos \varphi _ { 0 } - M \cos \left( \varphi _ { 0 } + m \right) } + \left[ \right] \eta ^ { 2 } + \cdot \cdot \cdot .
$$

The only exception is when the coefficient of $\Delta \varphi$ in the power series in $\Delta \varphi$ is zero. This is the second of equations (56)，the conditions for a double root. In this case the expression for $\Delta \varphi$ proceeds in powers of $\pm \ \sqrt { \eta }$ .In practice difficulty arises if the coefficient of $\Delta \varphi$ is small without being zero,for then $\varphi _ { 0 }$ must be very close to the true value of $\varphi$ before the method of differential corrections can be applied.

The higher terms of (61) can be computed without any difficulty, but they rapidly become more complex. It is simpler in practice to neglect them and to repeat the process with successive improved values of $\varphi _ { 0 }$

It is possible to develop a more convenient method for computing the differential corrections by making use of the fact that the work is done with logarithms. After $_ m$ and $M$ have been computed from the observational data the approximate solution of (48) can be determined from the diagram. The curve $y _ { 1 }$ can be drawn accurately once for all. The better known sine curve, in this case flattened or stretched vertically by the factor $M$ ，can be drawn free hand with sufficient accuracy to enable one to get a very approximate estimate of the value of $\varphi$ Let it be $\varphi _ { 0 }$ The logarithms of the right and left members of (48) will be computed and they will of course be found to be unequal. Let

In the successive approximations only the first and third of these logarithms will be changed. The tables give the logarithms of the trigonometric functions. Let the tabular difference for the logarithm of sin $\varphi _ { 0 }$ and sin $( \varphi _ { 0 } + \delta \varphi )$ be $\epsilon _ { 1 ; }$ ，where $\delta \varphi$ is some convenient increment to $\varphi _ { 0 }$ ,and let $\epsilon _ { 2 }$ be the corresponding tabular difference for sin $( \varphi _ { 0 } + m )$ .These quantities are taken down from the margins of the tables when the logarithms of sin $\varphi _ { 0 }$ and sin $( \varphi _ { 0 } + m )$ are taken out. Then the correction $\Delta \varphi$ is given by the equation

$$
\Delta \varphi = { \frac { \delta \varphi \cdot \epsilon } { 4 \epsilon _ { 1 } - \epsilon _ { 2 } } } ,
$$

where the result is expressed in the units used for ${ \pmb { \delta } } \varphi$ This method is so convenient in practice that a very few minutes suffices in any case to find the solution of (48) with allthe accuracy which may be desired.In the first approximation，where the error is in general large,one degree could be taken for $\delta \varphi$ In the later approximations $1 0 ^ { \prime \prime }$ is a convenient increment because the tabular differences of the logarithms for differences of ${ \bf { 1 0 ^ { \prime \prime } } }$ are given on the margins of the tables.\*

124.Discussion of the Determinant $D$ 、The determinant $D$ ， equation (45),enters into the determination of the constants $M$ and $\mathscr { m }$ ,and the solution becomes indeterminate in form if it is zero. Consequently it is important to find under what circumstances it vanishes.

Suppose the determination of the orbit is being based on only three observations. Then the values of $\lambda , \lambda ^ { \prime }$ ,and $\lambda ^ { \prime \prime }$ , which occur in $D$ ，are given by (31) and (32). There are corresponding expressions for $\mu , ~ \mu ^ { \prime } , ~ \mu ^ { \prime \prime } ; ~ \nu , ~ \nu ^ { \prime } , ~ \nu ^ { \prime \prime }$ .After they are substituted in (45) the determinant $D$ can be factored into the product of two determinants. In order to simplify the notation let

$$
P _ { 1 } = \frac { \left( \tau - \tau _ { 2 } \right) \left( \tau - \tau _ { 3 } \right) } { \left( \tau _ { 1 } - \tau _ { 2 } \right) \left( \tau _ { 1 } - \tau _ { 3 } \right) } , \qquad P _ { 2 } = \frac { \left( \tau - \tau _ { 1 } \right) \left( \tau - \tau _ { 3 } \right) } { \left( \tau _ { 2 } - \tau _ { 1 } \right) \left( \tau _ { 2 } - \tau _ { 3 } \right) } ,
$$

$$
P _ { 3 } = \frac { \left( \tau - \tau _ { 1 } \right) \left( \tau - \tau _ { 2 } \right) } { \left( \tau _ { 3 } - \tau _ { 1 } \right) \left( \tau _ { 3 } - \tau _ { 2 } \right) } ,
$$

and denote the derivatives of these functions with respect to $\pmb { \tau }$ by accents.Then

$$
\left\{ \begin{array} { l l } { D = \Delta _ { 1 } \Delta _ { 2 } , } \\ & { \left| \begin{array} { l } { P _ { 1 } , } \\ { \Delta _ { 1 } = \left| \begin{array} { l l l } { P _ { 1 } , } & { P _ { 1 } ^ { \prime } , } & { P _ { 1 } ^ { \prime \prime } } \\ { P _ { 2 } , } & { P _ { 2 } ^ { \prime } , } & { P _ { 2 } ^ { \prime \prime } } \end{array} \right| , } \\ { P _ { 3 } , } & { P _ { 3 } ^ { \prime } , } & { P _ { 3 } ^ { \prime \prime } } \end{array} \right| } \\ { \Delta _ { 2 } = \left| \begin{array} { l l l } { \lambda _ { 1 } , } & { \lambda _ { 2 } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { \mu _ { 2 } , } & { \mu _ { 3 } } \\ { \nu _ { 1 } , } & { \nu _ { 2 } , } & { \nu _ { 3 } } \end{array} \right| . } \end{array} \right.
$$

Consequently $D$ can vanish only if $\Delta _ { 1 }$ or $\Delta _ { 2 }$ is zero.

\*The solution of (48) depends on the two parameters $M$ and $\scriptstyle m$ ； if there were but one the relations between it and $\varphi$ could easily be tabulated. In spite of the two parameters Leuschner has extended a table originally due to Oppolzer from which the solution can be read directly with considerable approximation. It is table xvI.in the third (Buchholz) edition of Klinkerfues’Theoretische Astronomie.

It will be shown frst that $\Delta _ { 1 }$ is a constant which is distinct from zero. Since it is formally of the third degree in $\boldsymbol { \tau }$ ，necessary and sufficient conditions that it shall be independent of $\pmb { \tau }$ are that ${ \Delta _ { 1 } } ^ { \prime } = 0$ for all values of $\pmb { \tau }$ .The derivative of a determinant is the sum of the determinants which are obtained by replacing successively the columns of the original determinant by their derivatives.Hence ${ \Delta _ { 1 } } ^ { \prime }$ is a sum of three determinants. Since the derivative of the first column is identical with the second column, the first of these determinants is zero for all values of $\pmb { \tau }$ Since the derivative of the second column is identical with the third, the second determinant is zero. The derivative of the third column is zero，and therefore the third determinant is zero. Hence ${ \Delta } _ { 1 } ^ { \prime }$ is identically zero and $\Delta _ { 1 }$ is a constant. Its value, which is easily found for $\tau = 0$ ,is

$$
\Delta _ { 1 } = \frac { 2 \left| \begin{array} { l l } { \tau _ { 2 } \tau _ { 3 } , } & { \tau _ { 2 } + \tau _ { 3 } , } \\ { \tau _ { 3 } \tau _ { 1 } , } & { \tau _ { 3 } + \tau _ { 1 } , } \\ { \tau _ { 1 } \tau _ { 2 } , } & { \tau _ { 1 } + \tau _ { 2 } , } \end{array} \right| } { ( \tau _ { 1 } - \tau _ { 2 } ) ^ { 2 } ( \tau _ { 2 } - \tau _ { 3 } ) ^ { 2 } ( \tau _ { 3 } - \tau _ { 1 } ) ^ { 2 } }
$$

This determinant is distinct from zero and independent of the choice of the epoch $t _ { 0 }$

In order to interpret $\Delta _ { 2 }$ multiply the first,second,and third columns by $\rho _ { 1 } , \rho _ { 2 }$ and $\pmb { \rho _ { 3 } }$ respectively. Then,in the notation of equations (6),the determinant $\Delta _ { 2 }$ becomes

$$
\rho _ { 1 } \rho _ { 2 } \rho _ { 3 } \Delta _ { 2 } = { \Bigg | } { \xi _ { 1 } , \xi _ { 2 } , \xi _ { 3 } { \Bigg | } } .
$$

The right member of this equation is numerically the expression for six times the volume of the tetrahedron formed by the earth and the three positions of $\boldsymbol { C }$ with respect to $E$ .The volume of this tetrahedron is zero only if the three positions of $\boldsymbol { C }$ lie in a plane passing through the fourth point $\mathcal { E }$ ：This，of course,is referring the position of $\boldsymbol { C }$ to $E$ as an origin. A simpler way of expressing the same result is,the determinant $\Delta _ { 2 }$ (and therefore $D$ ） is zero only if the three apparent positions of $\boldsymbol { C }$ as observed from $\mathbfcal { E }$ lie on an arc of $^ { a }$ great circle.

It follows from (44) that if $D$ is zero, $D _ { 1 }$ and $D _ { 2 }$ are also zero unless $\textstyle R = r$ ，In general，the expressions for $\pmb { \rho }$ and $\pmb { \rho } ^ { \prime }$ become indeterminate when $D$ is zero，and they are poorly determined when $\pmb { D }$ is small. One case in which $\Delta _ { 2 }$ and $_ D$ are always zero is that in which $c$ moves in the plane of the earth's orbit. But in this case there are only four elements to be determined,and since each observation gives a single coordinate (the longitude) four observations are required.

An expression for $\Delta _ { 2 }$ can be obtained by means of equations (6). After some simple reductions it is found that

$$
+ \sin { ( \alpha _ { 3 } - \alpha _ { 2 } ) } \tan { \delta _ { 1 } } + \sin { ( \alpha _ { 1 } - \alpha _ { 3 } ) } \tan { \delta _ { 2 } } ] .
$$

125.Reduction of the Determinants $D _ { 1 }$ and $D _ { 2 }$ The expressions for $D _ { 1 }$ and $D _ { 2 }$ ,equations (45),become as a consequence of equations (31) and (32) and corresponding expressions for $\mu , \mu ^ { \prime } , \nu ,$ and $\nu ^ { \prime }$

$$
\begin{array} { r l r } & { \cdots } & \\ & { D _ { 1 } = - \left| P _ { 1 } \mu _ { 1 } + P _ { 2 } \lambda _ { 2 } + P _ { 3 } \mu _ { 3 } , \ P _ { 1 } ^ { \prime } \lambda _ { 1 } + P _ { 2 } ^ { \prime } \lambda _ { 2 } + P _ { 3 } ^ { \prime } \lambda _ { 3 } , \ X \right| } \\ & { } & \\ & { D _ { 1 } = - \left| P _ { 1 } \mu _ { 1 } + P _ { 2 } \mu _ { 2 } + P _ { 3 } \mu _ { 3 } , \ P _ { 1 } ^ { \prime } \mu _ { 1 } + P _ { 2 } ^ { \prime } \mu _ { 2 } + P _ { 3 } ^ { \prime } \mu _ { 3 } , \ Y \right| , } \\ & { } & \\ & { \left| P _ { 1 } \nu _ { 1 } + P _ { 2 } \nu _ { 2 } + P _ { 3 } \nu _ { 3 } , \ P _ { 1 } ^ { \prime } \nu _ { 1 } + P _ { 2 } ^ { \prime } \nu _ { 2 } + P _ { 3 } ^ { \prime } \nu _ { 3 } , \ Z \right| } \\ & { } & \\ & { \qquad \quad \left| P _ { 1 } \lambda _ { 1 } + P _ { 2 } \lambda _ { 2 } + P _ { 3 } \lambda _ { 3 } , \ P _ { 1 } ^ { \prime \prime } \lambda _ { 1 } + P _ { 2 } ^ { \prime \prime } \lambda _ { 2 } + P _ { 3 } ^ { \prime \prime } \lambda _ { 3 } , \ X \right| } \\ & { } & \\ & { D _ { 2 } = + \left| P _ { 1 } \mu _ { 1 } + P _ { 2 } \mu _ { 2 } + P _ { 3 } \mu _ { 3 } , \ P _ { 1 } ^ { \prime \prime } \mu _ { 1 } + P _ { 2 } ^ { \prime \prime } \mu _ { 2 } + P _ { 3 } ^ { \prime \prime } \mu _ { 3 } , \ Y \right| . } \\ & { } & \\ & { \qquad \quad \left| P _ { 1 } \nu _ { 1 } + P _ { 2 } \nu _ { 2 } + P _ { 3 } \nu _ { 3 } , \ P _ { 1 } ^ { \prime \prime } \nu _ { 1 } + P _ { 2 } ^ { \prime \prime } \nu _ { 2 } + P _ { 3 } ^ { \prime \prime } \nu _ { 3 } , \ Z \right| } \end{array}
$$

If the first column of $D _ { 1 }$ is multiplied by $\frac { P _ { 3 } ^ { ' } } { P _ { 3 } }$ and subtracted from the second column,the result is

$$
\begin{array} { r } { | P _ { \lambda } , ( P _ { 1 } { ' } P _ { 3 } - P _ { 1 } P _ { 3 } { ' } ) \lambda _ { 1 } + ( P _ { 2 } { ' } P _ { 3 } - P _ { 2 } P _ { 3 } { ' } ) \lambda _ { 2 } , X | } \\ { - \displaystyle \frac { 1 } { P _ { 3 } } | P _ { \mu } , ( P _ { 1 } { ' } P _ { 3 } - P _ { 1 } P _ { 3 } { ' } ) \mu _ { 1 } + ( P _ { 2 } { ' } P _ { 3 } - P _ { 2 } P _ { 3 } { ' } ) \mu _ { 2 } , Y | , } \\ { P _ { \nu } , ( P _ { 1 } { ' } P _ { 3 } - P _ { 1 } P _ { 3 } { ' } ) \nu _ { 1 } + ( P _ { 2 } { ' } P _ { 3 } - P _ { 2 } P _ { 3 } { ' } ) \nu _ { 2 } , Z | } \end{array}
$$

where

$$
\left\{ \begin{array} { l l } { P _ { \lambda } = P _ { 1 } \lambda _ { 1 } + P _ { 2 } \lambda _ { 2 } + P _ { 3 } \lambda _ { 3 } , } \\ { P _ { \mu } = P _ { 1 } \mu _ { 1 } + P _ { 2 } \mu _ { 2 } + P _ { 3 } \mu _ { 3 } , } \\ { P _ { \nu } = P _ { 1 } \nu _ { 1 } + P _ { 2 } \nu _ { 2 } + P _ { 3 } \nu _ { 3 } . } \end{array} \right.
$$

This determinant is the sum of the two determinants

$$
\begin{array} { r l } { - \frac { 1 } { P _ { 3 } } \bigg | { P _ { 1 } } \lambda _ { 1 } + { P _ { 2 } } \lambda _ { 2 } , } & { ( P _ { 1 } { ' } P _ { 3 } - P _ { 1 } { P _ { 3 } } ^ { \prime } ) \lambda _ { 1 } + ( P _ { 2 } { ' } P _ { 3 } - P _ { 2 } { P _ { 3 } } ^ { \prime } ) \lambda _ { 2 } , \quad X } \\ { - \frac { 1 } { P _ { 3 } } \bigg | { P _ { 1 } } \mu _ { 1 } + { P _ { 2 } } \mu _ { 2 } , } & { ( { P _ { 1 } } { ' } P _ { 3 } - P _ { 1 } { P _ { 3 } } ^ { \prime } ) \mu _ { 1 } + ( P _ { 2 } { ' } P _ { 3 } - P _ { 2 } { P _ { 3 } } ^ { \prime } ) \mu _ { 2 } , \quad Y } \\ { { P _ { 1 } } \nu _ { 1 } + { P _ { 2 } } \nu _ { 2 } , } & { ( { P _ { 1 } } { ' } P _ { 3 } - P _ { 1 } P _ { 3 } ^ { \prime } ) \nu _ { 1 } + ( P _ { 2 } { P _ { 3 } } - P _ { 2 } P _ { 3 } ^ { \prime } ) \nu _ { 2 } , \quad Z \bigg | } \end{array}
$$

and

$$
 - | \begin{array} { c c c } { \lambda _ { 3 } , } & { ( P _ { 1 } { } ^ { \prime } P _ { 3 } - P _ { 1 } P _ { 3 } { } ^ { \prime } ) \lambda _ { 1 } + ( P _ { 2 } { } ^ { \prime } P _ { 3 } - P _ { 2 } P _ { 3 } { } ^ { \prime } ) \lambda _ { 2 } , } & { X } \\ { \mu _ { 3 } , } & { ( P _ { 1 } { } ^ { \prime } P _ { 3 } - P _ { 1 } P _ { 3 } { } ^ { \prime } ) \mu _ { 1 } + ( P _ { 2 } { } ^ { \prime } P _ { 3 } - P _ { 2 } P _ { 3 } { } ^ { \prime } ) \mu _ { 2 } , } & { Y } \\ { \nu _ { 3 } , } & { ( P _ { 1 } { } ^ { \prime } P _ { 3 } - P _ { 1 } P _ { 3 } { } ^ { \prime } ) \nu _ { 1 } + ( P _ { 2 } { } ^ { \prime } P _ { 3 } - P _ { 2 } P _ { 3 } { } ^ { \prime } ) \nu _ { 2 } , } & { Z } \end{array} | .
$$

The terms in $\lambda _ { 2 } , \mu _ { 2 } ,$ and ${ \pmb { \nu } } _ { 2 }$ can be eliminated in a similar manner from the second column of the first of these determinants. Then each of the determinants is the sum of two others,and the reduced expression for $D _ { 1 }$ becomes

$$
\begin{array} { r l } { D _ { 1 } = - ( P _ { 1 } P _ { 2 } ^ { \prime } - P _ { 1 } ^ { \prime } P _ { 2 } ) \left| \begin{array} { l l l } { \lambda _ { 1 } } & { \lambda _ { 2 } } & { X } \\ { \mu _ { 1 } } & { \mu _ { 2 } } & { Y } \\ { \nu _ { 1 } } & { \nu _ { 2 } } & { Z } \end{array} \right| } & { } \\ { \nu _ { 2 } } & { = ( P _ { 2 } P _ { 2 } ^ { \prime } - P _ { 2 } ^ { \prime } P _ { 3 } ) \left| \begin{array} { l l l } { \lambda _ { 2 } } & { \lambda _ { 3 } } & { X } \\ { \mu _ { 2 } } & { \mu _ { 3 } } & { Y } \\ { \nu _ { 2 } } & { \nu _ { 3 } } & { Z } \end{array} \right| } \\ { \nu _ { 3 } } & { = \left| \begin{array} { l l l } { \lambda _ { 3 } } & { \lambda _ { 1 } } & { X } \\ { \mu _ { 3 } } & { \mu _ { 1 } } & { Y } \\ { \nu _ { 2 } } & { \nu _ { 3 } } & { Z } \end{array} \right| . } \end{array}
$$

The coefficients of these determinants are needed for $\pmb { \tau } = \mathbf { 0 }$ It is found from (63) that

$$
{ \begin{array} { r l } & { P _ { 1 } P _ { 2 } ^ { \prime } - P _ { 1 } { ' } P _ { 2 } = { \frac { \textstyle + \tau _ { 3 } ^ { 2 } } { ( \tau _ { 2 } - \tau _ { 1 } ) ( \tau _ { 3 } - \tau _ { 2 } ) ( \tau _ { 3 } - \tau _ { 1 } ) } } , } \\ & { P _ { 2 } P _ { 3 } ^ { \prime } - P _ { 2 } { ' } P _ { 3 } = { \frac { \textstyle + \tau _ { 1 } ^ { 2 } } { ( \tau _ { 2 } - \tau _ { 1 } ) ( \tau _ { 3 } - \tau _ { 2 } ) ( \tau _ { 3 } - \tau _ { 1 } ) } } , } \\ & { P _ { 3 } P _ { 1 } ^ { \prime } - P _ { 3 } { ' } P _ { 1 } = { \frac { \textstyle + \tau _ { 2 } ^ { 2 } } { ( \tau _ { 2 } - \tau _ { 1 } ) ( \tau _ { 3 } - \tau _ { 2 } ) ( \tau _ { 3 } - \tau _ { 1 } ) } } . } \end{array} }
$$

Then the expression for $D _ { 1 }$ reduces to

$$
\{ \begin{array} { c c c c } { \displaystyle { | D _ { 1 } = - \frac { \tau _ { 3 } ^ { 2 } } { P } | _ { \displaystyle { \mu _ { 1 } , \quad \mu _ { 2 } , \quad \cal Z } } ^ { \displaystyle { | \lambda _ { 1 } , \quad \lambda _ { 2 } , \quad { \cal X } | } } - \frac { \tau _ { 1 } ^ { 2 } } { P } | _ { \displaystyle { \mu _ { 2 } , \quad \mu _ { 3 } , \quad { \cal Y } } } } } \\  \displaystyle  | \begin{array} { c c c c }  \displaystyle  | \begin{array} { c c c c }  \displaystyle { | \begin{array} { c c c c } { \displaystyle { | \begin{array} { c c c c } { \end{array} } | } & { \displaystyle { \lambda _ { 3 } , } } & { \displaystyle { \lambda _ { 1 } , } } & { \displaystyle { \cal X } } \\ { \displaystyle { | \begin{array} { c c c c } { \displaystyle { | \begin{array} { c c c c } \end{array} | } & { \displaystyle { \mu _ { 3 } , } } & { \displaystyle { \lambda _ { 3 } , } } & { \displaystyle { \cal Y } } \\ { \displaystyle { p } _ { 2 } , } & { \mu _ { 3 } , } & { \displaystyle { \cal Z } } \end{array} | } } } \\ { \displaystyle { | \begin{array} { c c c c } { \displaystyle { | \begin{array} { c c c c } { \displaystyle { | \begin{array} { c c c c } \end{array} | } & { \displaystyle { \lambda _ { 3 } , } } & { \displaystyle { \lambda _ { 1 } , } } & { \displaystyle { \cal X } } \\ { \displaystyle { P } | _ { \displaystyle { \mu _ { 3 } , } } } & { \displaystyle { \mu _ { 1 } , } } & { \displaystyle { \cal Y } } \end{array} | } } } \\ { \displaystyle { P = ( \tau _ { 2 } - \tau _ { 1 } ) ( \tau _ { 3 } - \tau _ { 2 } ) ( \tau _ { 3 } - \tau _ { 3 } ) ( \tau _ { 3 } - \tau _ { 7 } ) } } & { , } \end{array} | } } } \end{array}  } \end{array} \end{array} \end{array}
$$

In a similar manner the expression for $D _ { 2 }$ reduces to

$$
D _ { 2 } = \frac { 2 \tau _ { 3 } } { P } \left| \begin{array} { l l l } { \lambda _ { 1 } , } & { \lambda _ { 2 } , } & { X } \\ { \mu _ { 1 } , } & { \mu _ { 2 } , } & { Y } \\ { \nu _ { 1 } , } & { \nu _ { 2 } , } & { Z } \end{array} \right| + \frac { 2 \tau _ { 1 } } { P } \left| \begin{array} { l l l } { \lambda _ { 2 } , } & { \lambda _ { 3 } , } & { X } \\ { \mu _ { 2 } , } & { \mu _ { 3 } , } & { Y } \\ { \nu _ { 2 } , } & { \nu _ { 3 } , } & { Z } \end{array} \right|
$$

$$
+ \frac { 2 \tau _ { 2 } } { P } \Bigg | _ { \nu _ { 3 } , ~ \ \mu _ { 1 } , ~ \ Y } ^ { \lambda _ { 3 } , ~ \ \lambda _ { 1 } , ~ X } \Bigg | .
$$

Each of the determinants in the expressions for $D _ { 1 }$ and $D _ { 3 }$ can be developed in a form similar to (66).

126.Correction for the Time Aberration. Since the velocity of light is finite,the body $c$ at any instant is apparently where it was at some preceding instant. This introduces a slight error in the data which must be corrected, if accurate results are desired, after the approximate distances have been determined. Since the velocity of light is very great and the apparent motions of the heavenly bodies are in general slow,it will not be necessary to know the distance of $\boldsymbol { c }$ with a high degree of accuracy in order to correct for the finite velocity of light.

Let $E _ { 1 } , \ E _ { 2 } ,$ and $E _ { 3 }$ be the positions of the observer at $t _ { 1 } , \ t _ { 2 } ,$ and $t _ { 3 }$ respectively. Let the observed directions of $c$ at these epochs be $\mathcal { E } _ { 1 } C _ { 1 } , ~ \mathcal { E } _ { 2 } C _ { 2 } ,$ and ${ \bf { { E } } } _ { 3 } C _ { 3 }$ .In the time required for the light to go from $\boldsymbol { C }$ to $\mathbfit { \Delta } E$ the former will have moved forward in its orbit to the positions $p _ { 1 } , p _ { 2 } ,$ and $p _ { 3 }$ ，which are its true places at the epochs $t _ { 1 } , \ t _ { 2 } ,$ and $t _ { 3 }$ .If the distances are known the observed coordinates can easily be corrected for these slight motions；but this changes all the observed data of the problem and makes it necessary to recompute all the determinants.

![](images/5dc0c1aeb8613f6cb6d67b7cef4542d6ba3d2b12388aa177020e16141687a497.jpg)  
Fig. 36.

A second method,which is more convenient in practice, is to correct the times of the observations. The body $\boldsymbol { C }$ passed through the points $C _ { 1 } , C _ { 2 }$ and $\boldsymbol { C } _ { 3 }$ ，notat $t _ { 1 } , t _ { 2 } ,$ and $t _ { 3 ; \ l }$ ，but at these epochs diminished by the time required for light to move from $C _ { 1 } , \ C _ { 2 } ,$ and $C _ { 3 }$ to $E _ { 1 } , \ E _ { 2 } ,$ and $\mathbf { { \mathit { E } } _ { 3 } }$ respectively. In order to make these corrections to the epochs it is necessary to know $E _ { 1 } C _ { 1 } = \rho _ { 1 } ,$ $E _ { 2 } C _ { 2 } = \rho _ { 2 } ,$ ， $E _ { 3 } C _ { 3 } = \rho _ { 3 }$ It will be supposed that (48)， (46),and (44) have been solved and that $\pmb { \rho }$ and $\rho ^ { \prime }$ are known. Then the values of $\rho _ { 1 } , \rho _ { 2 } ,$ and $\pmb { \rho _ { 3 } }$ are given with sufficient approximations for present purposes by

$$
\left\{ \begin{array} { l l } { \rho _ { 1 } = \rho + \rho ^ { \prime } \tau _ { 1 } , } \\ { \rho _ { 2 } = \rho + \rho ^ { \prime } \tau _ { 2 } , } \\ { \rho _ { 3 } = \rho + \rho ^ { \prime } \tau _ { 3 } . } \end{array} \right.
$$

Let $V$ represent the velocity of light. Then the epochs at which $\pmb { C }$ was at ${ \cal C } _ { 1 } , { \cal C } _ { 2 } ,$ and $c _ { 3 }$ are

$$
\left\{ \begin{array} { l l } { \displaystyle \tau _ { 1 } - \Delta \tau _ { 1 } = \tau _ { 1 } - \frac { \rho _ { 1 } } { V } = \tau _ { 1 } - \frac { \left( \rho + \rho ^ { \prime } \tau _ { 1 } \right) } { V } , } \\ { \displaystyle \tau _ { 2 } - \Delta \tau _ { 2 } = \tau _ { 2 } - \frac { \rho _ { 2 } } { V } = \tau _ { 2 } - \frac { \left( \rho + \rho ^ { \prime } \tau _ { 2 } \right) } { V } , } \\ { \displaystyle \tau _ { 3 } - \Delta \tau _ { 3 } = \tau _ { 3 } - \frac { \rho _ { 3 } } { V } = \tau _ { 3 } - \frac { \left( \rho + \rho ^ { \prime } \tau _ { 3 } \right) } { V } . } \end{array} \right.
$$

Now consider the correction to $D , D _ { 1 } ,$ and $D _ { 2 }$ In $D$ only the factor $\Delta _ { 1 }$ is altered. But in the applications only the ratios of $D$ to $D _ { 1 }$ and $D _ { 2 }$ are used,and the latter contain $\Delta _ { 1 }$ as a factor. Therefore the only change required is to replace $\tau _ { 1 } , \ \tau _ { 2 } ,$ and $\pmb { \tau _ { 3 } }$ by $\tau _ { 1 } - \Delta \tau _ { 1 }$ ， $\tau _ { 2 } \mathrm { ~ - ~ } \Delta \tau _ { 2 } ,$ and $\tau _ { 3 } - \Delta \tau _ { 3 }$ respectively in the numerators of the coefficients of the determinants in (67) and (68).

127. Development of $x , y ;$ and $\pmb { z }$ in Series. In order to determine the corrections which should be added to $\lambda ^ { \prime }$ and $\lambda ^ { \prime \prime }$ so as to determine the elements of the orbit with greater accuracy, it is necessary to have $x , y$ ,and $\pmb { z }$ developed as power series in $\tau$ These quantities satisfy the differential equations

$$
{ \left\{ \begin{array} { l l } { { \displaystyle { \frac { d ^ { 2 } x } { d \tau ^ { 2 } } } = - { \frac { x } { r ^ { 3 } } } = - u x , } } & { \ \left( u = { \frac { 1 } { r ^ { 3 } } } \right) , } \\ { { \displaystyle { \frac { d ^ { 2 } y } { d \tau ^ { 2 } } } = - { \frac { y } { r ^ { 3 } } } = - u y } } & { \ } \\ { { \displaystyle { \frac { d ^ { 2 } z } { d \tau ^ { 2 } } } = - { \frac { z } { r ^ { 3 } } } = - u z . } } & { } \end{array} \right. }
$$

It is shown in the theory of differential equations that the solutions of differential equations of this type are expansible as power series of the form

$$
\left\{ \begin{array} { l l } { x = x _ { 0 } + x _ { 0 } { ' } \tau + \frac { 1 } { 2 } x _ { 0 } { ' } ^ { \prime } \tau ^ { 2 } + \frac { 1 } { 6 } x _ { 0 } { ' } ^ { \prime \prime } \tau ^ { 3 } + \frac { 1 } { 2 4 } x _ { 0 } \mathrm { { i } } ^ { \mathrm { { i v } } } \tau ^ { 4 } + \frac { 1 } { 1 2 0 } x _ { 0 } \mathrm { { ' } } ^ { \mathrm { } } \tau ^ { 5 } + \cdots , } \\ { y = y _ { 0 } + y _ { 0 } { ' } \tau + \frac { 1 } { 2 } y _ { 0 } { ' } ^ { \prime } \tau ^ { 2 } + \frac { 1 } { 6 } y _ { 0 } { ' } ^ { \prime \prime } \tau ^ { 3 } + \frac { 1 } { 2 4 } y _ { 0 } \mathrm { { i } } ^ { \mathrm { { i v } } } \tau ^ { 4 } + \frac { 1 } { 1 2 0 } y _ { 0 } \mathrm { { ' } } ^ { \mathrm { } } \tau ^ { 5 } + \cdots , } \\ { z = z _ { 0 } + z _ { 0 } { ' } \tau + \frac { 1 } { 2 } z _ { 0 } { ' } ^ { \prime \prime } \tau ^ { 2 } + \frac { 1 } { 6 } z _ { 0 } { ' } ^ { \prime \prime } \tau ^ { 3 } + \frac { 1 } { 2 4 } z _ { 0 } \mathrm { { i } } ^ { \mathrm { { i v } } } \tau ^ { 4 } + \frac { 1 } { 1 2 0 } z _ { 0 } \mathrm { { ' } } ^ { \mathrm { } } \tau ^ { \mathrm { } } + \cdots . } \end{array} \right.
$$

It is found from (71) and its successive derivatives that

$$
\left\{ \begin{array} { l l } { x _ { 0 } ^ { \prime \prime } = - u _ { 0 } x _ { 0 } , } \\ { x _ { 0 } ^ { \prime \prime \prime } = - u _ { 0 } { ' } x _ { 0 } - u _ { 0 } x _ { 0 } { ' } , } \\ { x _ { 0 } ^ { \mathrm { { i v } } } = ( - u _ { 0 } { ' } ^ { \prime } + u _ { 0 } { ^ { 2 } } ) x _ { 0 } - 2 u _ { 0 } { ' } x _ { 0 } { ' } , } \\ { x _ { 0 } ^ { \mathrm { { v } } } = ( - u _ { 0 } { ' } ^ { \prime \prime \prime } + 4 u _ { 0 } u _ { 0 } { ' } ) x _ { 0 } - ( 3 u _ { 0 } { ' } ^ { \prime } - u _ { 0 } { ^ { 2 } } ) x _ { 0 } { ' } . } \\ { . \quad . \quad . \quad . \quad . \quad . \quad . \quad . . \quad . . \quad . . \quad . . \quad . . \quad . . \quad . . \quad . . } \end{array} \right.
$$

The coefficients of the series for $_ y$ and $\pmb { z }$ differ only in that $y _ { 0 } , y _ { 0 } ^ { \mathrm { ~ \prime ~ } }$ and $\boldsymbol { z } _ { 0 } , \ \boldsymbol { z } _ { 0 } ^ { \prime }$ appear in place of ${ \boldsymbol { x } } _ { 0 } , { \boldsymbol { x } } _ { 0 } ^ { \prime }$ respectively. Therefore

$$
\begin{array} { r l } & { \left\{ \begin{array} { l l } { x = f x _ { 0 } + g x _ { 0 } ^ { \prime } , } \\ { y = f y _ { 0 } + g y _ { 0 } ^ { \prime } , } \\ { z = f z _ { 0 } + g z _ { 0 } ^ { \prime } , } \end{array} \right. } \\ & { \left\{ \begin{array} { l l } { f = 1 - \frac { 1 } { 2 } u _ { 0 } \tau ^ { 2 } - \frac { 1 } { 6 } u _ { 0 } ^ { \prime } \tau ^ { 3 } - \frac { 1 } { 2 ^ { 4 } } ( u _ { 0 } ^ { \prime \prime } - u _ { 0 } ^ { \circ } ) \tau ^ { 4 } } \\ { \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad - \frac { 1 } { 1 2 ^ { 2 0 } } ( u _ { 0 } ^ { \prime \prime \prime } - 4 u _ { 0 } u _ { 0 } ^ { \prime } ) \tau ^ { 5 } + \cdot \cdot \cdot , } \\ { g = \tau - \frac { 1 } { 6 } u _ { 0 } \tau ^ { 3 } - \frac { 1 } { 1 2 } u _ { 0 } ^ { \prime } \tau ^ { 4 } - \frac { 1 } { 1 2 ^ { 2 0 } } ( 3 u _ { 0 } ^ { \prime \prime } - u _ { 0 } ^ { \circ } ) \tau ^ { 5 } + \cdot \cdot \cdot . . } \end{array} \right. } \end{array}
$$

In order to have $f$ and $g$ in a form for practical use the derivatives of $\textbf { \em u }$ must be expressed in terms of $x _ { 0 } , y _ { 0 } , z _ { 0 } , x _ { 0 } ^ { \prime } , y _ { 0 } ^ { \prime }$ ,and ${ \tilde { \boldsymbol { z } } _ { 0 } } ^ { \prime }$ .Lagrange has done this very elegantly by introducing $\pmb { p }$ and $\pmb q$ by the equations

$$
\left\{ \begin{array} { l l } { { r ^ { 2 } p = \displaystyle \frac { 1 } { 2 } \frac { d r ^ { 2 } } { d \tau } = x x ^ { \prime } + y y ^ { \prime } + z z ^ { \prime } , } } \\ { { } } \\ { { r ^ { 2 } q = \displaystyle \frac { 1 } { 2 } \frac { d ^ { 2 } r ^ { 2 } } { d \tau ^ { 2 } } = x ^ { \prime 2 } + y ^ { \prime 2 } + z ^ { \prime 2 } - r ^ { 2 } u . } } \end{array} \right.
$$

Then it is found that

$$
{ \left\{ \begin{array} { l l } { { u ^ { \prime } = - { \displaystyle \frac { 3 } { r ^ { 4 } } } { \frac { d r } { d \tau } } = - { \displaystyle \frac { 3 } { r ^ { 4 } } } { \frac { 1 } { 2 r } } { \frac { d r ^ { 2 } } { d \tau } } = - 3 u p , } } \\ { { p ^ { \prime } = + { \displaystyle \frac { 1 } { 2 r ^ { 2 } } } { \frac { d ^ { 2 } r ^ { 2 } } { d \tau ^ { 2 } } } - { \displaystyle \frac { 1 } { r ^ { 3 } } } { \frac { d r ^ { 2 } } { d \tau } } { \frac { d r } { d \tau } } = q - 2 p ^ { 2 } , } } \\ { { q ^ { \prime } = - { \displaystyle \frac { 1 } { r ^ { 3 } } } { \frac { d ^ { 2 } r ^ { 2 } } { d \tau ^ { 2 } } } { \frac { d r } { d \tau } } + { \displaystyle \frac { 1 } { 2 r ^ { 2 } } } { \frac { d ^ { 3 } r ^ { 2 } } { d \tau ^ { 3 } } } = - u p - 2 p q . } } \end{array} \right. }
$$

By means of these equations and their successive derivatives the coefficients in the series for $f$ and $g$ can be expressed as polynomials in $u , p .$ and $q$ ，The expressions for $f$ and $g$ become

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { f = 1 - \frac 1 2 u _ { 0 } \tau ^ { 2 } + \frac 1 2 u _ { 0 } p _ { 0 } \tau ^ { 3 } + \frac { 1 } { 2 4 } ( 3 u _ { 0 } q _ { 0 } - 1 5 u _ { 0 } p _ { 0 } ^ { 2 } + u _ { 0 } ^ { 2 } ) \tau ^ { 4 } } \\ { \qquad \quad + \frac { 1 } { 8 } ( 7 u _ { 0 } p _ { 0 } ^ { 3 } - 3 u _ { 0 } p _ { 0 } q _ { 0 } - u _ { 0 } ^ { 2 } p _ { 0 } ) \tau ^ { 5 } + \cdots , } \\ { g = \tau - \frac 1 6 u _ { 0 } \tau ^ { 3 } + \frac { 1 } { 4 } u _ { 0 } p _ { 0 } \tau ^ { 4 } + \frac { 1 } { 1 2 5 } ( 9 u _ { 0 } q _ { 0 } - 4 5 u _ { 0 } p _ { 0 } ^ { 2 } } \\ { \qquad \quad \quad + u _ { 0 } ^ { 2 } ) \tau ^ { 5 } + \cdots . } \end{array} \right. } \end{array}
$$

The derivatives of $x , y$ and $\pmb { z }$ can be determined from equations (73) and (75). For example

$$
\left\{ \begin{array} { l l } { x ^ { \prime \prime \prime } = f ^ { \prime \prime \prime } x _ { 0 } + g ^ { \prime \prime \prime } x _ { 0 } { \mathrm { ' } } , } \\ { x ^ { \mathrm { i v } } = f ^ { \mathrm { i v } } x _ { 0 } + g ^ { \mathrm { i v } } x _ { 0 } { \mathrm { ' } } , } \\ { . \quad . \quad . \quad . \quad . \quad . \quad . . . . } \end{array} \right.
$$

128.Computation of the Higher Derivatives of $\lambda , ~ \mu , ~ \nu .$ The values of $\lambda , \lambda ^ { \prime }$ ，and $\lambda ^ { \prime \prime }$ determined by equations (31) and (32) are only approximate because $c _ { 3 } , \ c _ { 4 } ,$ ... were unknown. But after the higher derivatives become known these coefficients are obtainable,and the approximate values can be corrected.

The third derivatives of equations (8) are

$$
\left\{ \begin{array} { c } { \rho ^ { \prime \prime \prime } \lambda + 3 \rho ^ { \prime \prime } \lambda ^ { \prime } + 3 \rho ^ { \prime } \lambda ^ { \prime \prime } + \rho \lambda ^ { \prime \prime } = x ^ { \prime \prime \prime } + X ^ { \prime \prime \prime } , } \\ { \rho ^ { \prime \prime \prime } \mu + 3 \rho ^ { \prime \prime } \mu ^ { \prime } + 3 \rho ^ { \prime } \mu ^ { \prime \prime } + \rho \mu ^ { \prime \prime \prime } = y ^ { \prime \prime \prime } + Y ^ { \prime \prime \prime } , } \\ { \rho ^ { \prime \prime \prime } \nu + 3 \rho ^ { \prime \prime } \nu ^ { \prime } + 3 \rho ^ { \prime } \nu ^ { \prime \prime } + \rho \nu ^ { \prime \prime \prime } = z ^ { \prime \prime \prime } + Z ^ { \prime \prime \prime } . } \end{array} \right.
$$

The left members of these equations involve the four unknowns $\rho ^ { \prime \prime \prime } , \lambda ^ { \prime \prime \prime } , \mu ^ { \prime \prime \prime }$ and $\nu ^ { \prime \prime \prime }$ ，the first and second derivatives having been determined approximately by equations (31), (32),and (44); but the unknowns are not independent because $\lambda , \mu , \nu ,$ and their derivatives satisfy the relations

$$
{ \left\{ \begin{array} { l l } { { \lambda } ^ { 2 } + \mu ^ { 2 } + \nu ^ { 2 } = 1 , } \\ { \lambda { \lambda } ^ { \prime } + \mu \mu ^ { \prime } + \nu \nu ^ { \prime } = 0 , } \\ { \lambda { \lambda } ^ { \prime \prime } + \mu \mu ^ { \prime \prime } + \nu \nu ^ { \prime \prime } + \lambda ^ { \prime 2 } + \mu ^ { \prime 2 } + \nu ^ { \prime 2 } = 0 , } \\ { \lambda { \lambda } ^ { \prime \prime \prime } + \mu \mu ^ { \prime \prime \prime } + \nu \nu ^ { \prime \prime \prime } + 3 ( \lambda ^ { \prime } \lambda ^ { \prime \prime } + \mu ^ { \prime } \mu ^ { \prime \prime } + \nu ^ { \prime } \nu ^ { \prime \prime } ) = 0 } \end{array} \right. }
$$

Consequently if equations (77) are multiplied by $\lambda , \ \mu ,$ and ${ \pmb \nu }$ respectively and added, the result is

$$
\begin{array} { c } { { \rho ^ { \prime \prime \prime } = 3 \rho ^ { \prime } ( \lambda ^ { \prime 2 } + \mu ^ { \prime } ^ { 2 } + \nu ^ { \prime } ^ { 2 } ) + 3 \rho ( \lambda ^ { \prime } \lambda ^ { \prime \prime } + \mu ^ { \prime } \mu ^ { \prime \prime } + \nu ^ { \prime } \nu ^ { \prime \prime } ) } } \\ { { + ( x ^ { \prime \prime \prime } + X ^ { \prime \prime \prime } ) \lambda + ( y ^ { \prime \prime \prime } + Y ^ { \prime \prime \prime } ) \mu + ( z ^ { \prime \prime \prime } + Z ^ { \prime \prime \prime } ) \nu , } } \end{array}
$$

which uniquely defines $\pmb { \rho } ^ { \prime \prime \prime }$ Then $\lambda ^ { \prime \prime \prime } , ~ \mu ^ { \prime \prime \prime }$ and $\pmb { \nu } ^ { \prime \prime \prime }$ are determined by (77） because $\pmb { x } ^ { \prime \prime \prime } , \ y ^ { \prime \prime \prime } , \ z ^ { \prime \prime \prime }$ are given by (76) and $X ^ { \prime \prime \prime }$ ， $Y ^ { \prime \prime \prime }$ ,and $\mathbf { Z ^ { \prime \prime \prime } }$ can be found from the Ephemeris.

The quantities $\lambda ^ { \mathrm { i v } } , ~ \mu ^ { \mathrm { i v } }$ and $\pmb { \nu } ^ { \mathrm { i } \mathbf { v } }$ can be computed in a similar way by taking the derivatives of (77） and reducing by means of the relations among $\lambda$ ， $\pmb { \mu } _ { : }$ and $\pmb { \nu }$

129.Improvement of the Values of $x , \ y , \ z , \ x ^ { \prime } , \ y ^ { \prime } , \ z ^ { \prime } .$ Afte1 $D , D _ { 1 ; }$ and $D _ { 2 }$ have been found from (65)，(66)，(67)，and (68) equation (48) can be solved,and then $x , y , z$ and their first derivatives can be determined from (8) and their first derivatives. These results are only approximate because of the errors to which $\lambda , \mu , \nu , \lambda ^ { \prime } , \mu ^ { \prime }$ and $\nu ^ { \prime }$ are subject,and the problem is to coreet them after ${ \boldsymbol { \lambda } } ^ { \prime \prime \prime }$ ， $\pmb { \mu } ^ { \prime \prime \prime }$ ，.. ave been determined.

It follows from the first equation of (28) that

$$
\begin{array} { r } { c _ { 3 } ~ = ~ \frac { 1 } { 6 } \lambda ^ { \prime \prime \prime } , \qquad c _ { 4 } = \frac { 1 } { 2 4 } \lambda ^ { \mathrm { i v } } , \qquad \cdots \cdots . } \end{array}
$$

Then equations (35） give

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \Delta c _ { 0 } = - \frac { 1 } { 6 } \lambda ^ { \prime \prime \prime } \tau _ { 1 } \tau _ { 2 } \tau _ { 3 } - \frac { 1 } { 2 4 } \lambda ^ { \mathrm { i v } } \tau _ { 1 } \tau _ { 2 } \tau _ { 3 } ( \tau _ { 1 } + \tau _ { 2 } + \tau _ { 3 } ) + \cdots , } \\ { \Delta c _ { 1 } = + \frac { 1 } { 6 } \lambda ^ { \prime \prime \prime } ( \tau _ { 1 } \tau _ { 2 } + \tau _ { 2 } \tau _ { 3 } + \tau _ { 3 } \tau _ { 1 } ) } \\ { \qquad \quad \qquad \qquad \quad + \frac { 1 } { 2 4 } \lambda ^ { \mathrm { i v } } ( \tau _ { 1 } + \tau _ { 2 } ) ( \tau _ { 2 } + \tau _ { 3 } ) ( \tau _ { 3 } + \tau _ { 1 } ) + \cdots , } \\ { \Delta c _ { 2 } = - \frac { 1 } { 6 } \lambda ^ { \prime \prime \prime } ( \tau _ { 1 } + \tau _ { 2 } + \tau _ { 3 } ) } \\ { \qquad \quad \qquad - \frac { 1 } { 2 4 } \lambda ^ { \mathrm { i v } } ( \tau _ { 1 } ^ { 2 } + \tau _ { 2 } ^ { 2 } + \tau _ { 3 } ^ { 2 } + \tau _ { 1 } \tau _ { 2 } + \tau _ { 2 } \tau _ { 3 } + \tau _ { 3 } \tau _ { 1 } ) + \cdots , } \end{array} \right. } \end{array}
$$

and the expression for $\lambda$ becomes

$$
\begin{array} { r } { \lambda = c _ { 0 } + \Delta c _ { 0 } + ( c _ { 1 } + \Delta c _ { 1 } ) \tau + ( c _ { 2 } + \Delta c _ { 2 } ) \tau ^ { 2 } \qquad } \\ { + \frac 1 6 \lambda ^ { \prime \prime \prime } \tau ^ { 3 } + \frac 1 2 \lambda ^ { \mathrm { i v } } \tau ^ { 4 } + \cdot \cdot \cdot , } \end{array}
$$

where $\pmb { c _ { 0 } } , \ \pmb { c _ { 1 } } ,$ and $\pmb { c _ { 2 } }$ are the approximate values of the coefficients of the series which are obtained from (31） and (32) by puting $\pmb { \tau }$ equal to zero. There are corresponding equations for $\mu$ and $\pmb { \nu }$ With these more nearly correct values of $\lambda , \lambda ^ { \prime } , \lambda ^ { \prime \prime } , \cdots$ thedeterminants $D , D _ { 1 }$ ,and $D _ { 2 }$ are computed from (45), $\varphi$ is determined from (48), $\pmb { \rho }$ and $\pmb { \rho } ^ { \prime }$ from (44),and $x , y , z , x ^ { \prime } , y ^ { \prime } , z ^ { \prime }$ from (8) and their first derivatives.Then still higher derivatives of $\lambda$ ， $\mu , \nu$ can be computed and still more nearly exact values of $\lambda , \lambda ^ { \prime }$ and $\lambda ^ { \prime \prime }$ determined,or the elements can be determined from $x , y , z , x ^ { \prime } { \mathrm { , ~ } }$ $y ^ { \prime } , z ^ { \prime }$ by the methods of chap. v.

There are two principal objections to the method of Laplace. One is that it is necessary to recompute all determinants and auxiliaries at each stage of the approximation，each of which costs a very considerable amount of labor. The other is that the method depends upon the motion of the observer through the equations by means of which $X ^ { \prime \prime } , ~ Y ^ { \prime \prime }$ ，and $Z ^ { \prime \prime }$ were eliminated from (9). Obviously all that is really fundamental in the problem is that $c$ shall have been observed from definite known places and that it shall move about the sun in accordance with the law of gravitation.

130.The Modifications of Harzer and Leuschner. The method of Laplace for determining orbits has not been found very satisfactory in practice. The reason seems to be that the conditions that the first and third observations shall be exactly satisfied are not directly imposed as they are,for example,in the method of Gauss. To remedy this defect Harzer proposed\* the plan of so determining $x , y , z , x ^ { \prime } , y ^ { \prime } , z ^ { \prime }$ by differential corrections, after their approximate values have been found,that the three observations shall be exactly fulfilled. If more than three observations are under consideration, they cannot in general be exactly satisfied,and the adjustments are then made by the method of least squares.

It will be sufficient here to sketch the method of making the differential corrections. The right ascensions and declinations are expressed in terms of the coordinates and components of velocity at $\scriptstyle t _ { 0 }$ by

$$
\left\{ \begin{array} { l l } { \rho \lambda = f x _ { 0 } + g x _ { 0 } { } ^ { \prime } + X , } \\ { \rho \tilde { \mu } = f y _ { 0 } + g y _ { 0 } { } ^ { \prime } + Y , } \\ { \rho \tilde { \nu } = f z _ { 0 } + g z _ { 0 } { } ^ { \prime } + Z , } \end{array} \right.
$$

which are obtained by substituting equations (73) in equations (8). The right ascension and declination enter through $\lambda , \mu ,$ and ${ \pmb \nu }$ of equations (6). The result can be indicated

$$
\left\{ \begin{array} { l l } { \alpha = F ( x _ { 0 } , y _ { 0 } , z _ { 0 } , x _ { 0 } ^ { \prime } , y _ { 0 } ^ { \prime } , z _ { 0 } ^ { \prime } ) , } \\ { \delta = G ( x _ { 0 } , y _ { 0 } , z _ { 0 } , x _ { 0 } ^ { \prime } , y _ { 0 } ^ { \prime } , z _ { 0 } ^ { \prime } ) . } \end{array} \right.
$$

\* Astronomische Nachrichten, Nos.3371-2 (1896).

From these equations the variations in $\pmb { \alpha }$ and $\delta$ ，which are the known differences between the observations and the approximate theory,are expressed in terms of the variations in $\boldsymbol { x } _ { 0 } , \cdots , \boldsymbol { z } _ { 0 } ^ { \prime }$ ,which are required. The relations are

$$
\left\{ \begin{array} { l l } { \Delta \alpha = \displaystyle \frac { \partial F } { \partial x _ { 0 } } \Delta x _ { 0 } + \displaystyle \frac { \partial F } { \partial y _ { 0 } } \Delta y _ { 0 } + \displaystyle \frac { \partial F } { \partial z _ { 0 } } \Delta z _ { 0 } + \displaystyle \frac { \partial F } { \partial x _ { 0 ^ { \prime } } } \Delta x _ { 0 ^ { \prime } } + \displaystyle \frac { \partial F } { \partial y _ { 0 ^ { \prime } } } \Delta y _ { 0 ^ { \prime } } + \displaystyle \frac { \partial F } { \partial z _ { 0 ^ { \prime } } } \Delta z _ { 0 ^ { \prime } } } \\ { \Delta \hat { \theta } = \displaystyle \frac { \partial G } { \partial x _ { 0 } } \Delta x _ { 0 } + \displaystyle \frac { \partial G } { \partial y _ { 0 } } \Delta y _ { 0 } + \displaystyle \frac { \partial G } { \partial z _ { 0 } } \Delta z _ { 0 } + \displaystyle \frac { \partial G } { \partial x _ { 0 ^ { \prime } } } \Delta x _ { 0 ^ { \prime } } + \displaystyle \frac { \partial G } { \partial y _ { 0 ^ { \prime } } } \Delta y _ { 0 ^ { \prime } } + \displaystyle \frac { \partial G } { \partial z _ { 0 ^ { \prime } } } \Delta z _ { 0 ^ { \prime } } } \end{array} \right.
$$

In forming the partial derivatives it must be remembered that $\boldsymbol { x } _ { 0 } , \cdots , \boldsymbol { z } _ { 0 } ^ { \prime }$ enter through $f$ and $g$ as well as explicitly. When these equations are written for three dates they become equal to the number of arbitraries, viz., $\Delta x _ { 0 } , \cdots , \Delta z _ { 0 } ^ { \prime }$ ,and consequently determine them uniquely provided the determinant of their coefficients is distinct from zero. The circumstances under which it vanishes have not been investigated. If there are more than three observations the number of equations exceeds the number of arbitraries and the method of least squares is employed.

When the date of the second observation is taken as the origin of time and the number of observations is only three,the number of equations of condition reduces to four which in general can be satisfied by suitably determining $\Delta \rho _ { 0 } , \ \Delta x _ { 0 } ^ { \prime } , \ \Delta y _ { 0 } ^ { \prime }$ ，and $\Delta { { z } _ { 0 } } ^ { \prime }$ .This is the procedure adopted by Leuschner\* to abbreviate the method of Harzer.In its simplified form the method has been found very convenient in practice and has led to highly satisfactory results.

II.THE GAUSSIAN METHOD OF DETERMINING ORBITS.

131.The Equation for $\pmb { \rho _ { 2 } }$ ，Equations (19) are fundamental in the method of Gauss. If the geocentric coordinates are introduced by equations (8),equations (19) become

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { [ 2 , 3 ] \rho _ { 1 } \lambda _ { 1 } - [ 1 , 3 ] \rho _ { 2 } \lambda _ { 2 } + [ 1 , 2 ] \rho _ { 3 } \lambda _ { 3 } } \\ { \qquad \quad = [ 2 , 3 ] X _ { 1 } - [ 1 , 3 ] X _ { 2 } + [ 1 , 2 ] X _ { 3 } , } \\ { [ 2 , 3 ] \rho _ { 1 } \mu _ { 1 } - [ 1 , 3 ] \rho _ { 2 } \mu _ { 2 } + [ 1 , 2 ] \rho _ { 3 } \mu _ { 3 } } \\ { \qquad \quad = [ 2 , 3 ] Y _ { 1 } - [ 1 , 3 ] Y _ { 2 } + [ 1 , 2 ] Y _ { 3 } , } \\ { [ 2 , 3 ] \rho _ { 1 } \nu _ { 1 } - [ 1 , 3 ] \rho _ { 2 } \nu _ { 2 } + [ 1 , 2 ] \rho _ { 3 } \nu _ { 3 } } \\ { \qquad \quad = [ 2 , 3 ] Z _ { 1 } - [ 1 , 3 ] Z _ { 2 } + [ 1 , 2 ] Z _ { 3 } . } \end{array} \right. } \end{array}
$$

The left members of these equations are linear in the three unknowns $\pmb { \rho _ { 1 } } , \pmb { \rho _ { 2 } } ,$ and $\pmb { \rho _ { 3 } }$ ，Their solution for ${ \pmb \rho } _ { 2 }$ is

$$
\{ \begin{array} { l l l } { \displaystyle \rho _ { 2 } = \frac { D } { \Delta } , } & & \\ & & { | \lambda _ { 1 } , \quad \lambda _ { 2 } , \quad \lambda _ { 3 } | } \\ { \Delta = - [ 2 , 3 ] [ 1 , 3 ] [ 1 , 2 ] | | \begin{array} { l l l } { \lambda _ { 1 } , } & { \mu _ { 2 } , } & { \mu _ { 3 } } \\ { \mu _ { 1 } , } & { \mu _ { 2 } , } & { \mu _ { 3 } } \end{array} | = - [ 2 , 3 ] [ 1 , 3 ] [ 1 , 2 ] \Delta _ { 2 } , } \\ & & { | \begin{array} { l l l } { \lambda _ { 1 } , } & { \lbrack 2 , 3 ] X _ { 1 } - [ 1 , 3 ] X _ { 2 } + [ 1 , 2 ] X _ { 3 } , } & { \lambda _ { 3 } } \\ { D = [ 2 , 3 ] [ 1 , 2 ] | \begin{array} { l l l } { \lambda _ { 1 } , } & { [ 2 , 3 ] Y _ { 1 } - [ 1 , 3 ] Y _ { 2 } + [ 1 , 2 ] Y _ { 3 } , } & { \mu _ { 3 } } \\ { \mu _ { 1 } , } & { [ 2 , 3 ] Z _ { 1 } - [ 1 , 3 ] Z _ { 2 } + [ 1 , 2 ] Z _ { 3 } , } & { \nu _ { 3 } } \end{array} | } \end{array} | } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \end{array} 
$$

The determinant $_ D$ is the sum of three determimants

$$
\left\{ \begin{array} { l l l } { { D = [ 2 , 3 ] ^ { 2 } [ 1 , 2 ] D ^ { ( 1 ) } - [ 2 , 3 ] [ 1 , 3 ] [ 1 , 2 ] D ^ { ( 2 ) } + [ 2 , 3 ] [ 1 , 3 ] = 0 } } \\ { { } } \\ { { D ^ { ( 1 ) } = \left| \begin{array} { l l l } { { \lambda _ { 1 } } , } & { { X _ { 1 } , } } & { { \lambda _ { 3 } } } \\ { { \mu _ { 1 } , } } & { { Y _ { 1 } , } } & { { \mu _ { 3 } } } \\ { { \nu _ { 1 } , } } & { { Z _ { 1 } , } } & { { \nu _ { 3 } } } \end{array} \right| , } } & { { D ^ { ( 2 ) } = \left| \begin{array} { l l l } { { \lambda _ { 1 } , } } & { { X _ { 2 } , } } & { { \lambda _ { 3 } } } \\ { { \mu _ { 1 } , } } & { { Y _ { 2 } , } } & { { \mu _ { 3 } } } \\ { { \nu _ { 1 } , } } & { { Z _ { 2 } , } } & { { \nu _ { 3 } } } \end{array} \right| , } } \\ { { D ^ { ( 3 ) } = \left| \begin{array} { l l l } { { \lambda _ { 1 } , } } & { { X _ { 3 } , } } & { { \lambda _ { 3 } } } \\ { { \mu _ { 1 } , } } & { { Y _ { 3 } , } } & { { \mu _ { 3 } } } \\ { { \nu _ { 1 } , } } & { { Z _ { 3 } , } } & { { \nu _ { 3 } } } \end{array} \right| . } } \end{array} \right.
$$

Consequently the frst equation of (81) becomes

$$
\Delta _ { 2 \rho _ { 2 } } = - \frac { [ 2 , 3 ] } { [ 1 , 3 ] } D ^ { ( 1 ) } + D ^ { ( 2 ) } - \frac { [ 1 , 2 ] } { [ 1 , 3 ] } D ^ { ( 3 ) } .
$$

Suppose $t _ { 2 }$ is taken as the origin of time. Then it follows from equations (73) that

$$
\left\{ \begin{array} { l l } { x _ { 1 } = f _ { 1 } x _ { 2 } + g _ { 1 } x _ { 2 } { ' } , \qquad y _ { 1 } = f _ { 1 } y _ { 2 } + g _ { 1 } y _ { 2 } { ' } , \qquad z _ { 1 } = f _ { 1 } z _ { 2 } + g _ { 1 } z _ { 2 } { ' } , } \\ { x _ { 3 } = f _ { 3 } x _ { 2 } + g _ { 3 } x _ { 2 } { ' } , \qquad y _ { 3 } = f _ { 3 } y _ { 2 } + g _ { 3 } y _ { 2 } { ' } , \qquad z _ { 3 } = f _ { 3 } z _ { 2 } + g _ { 3 } z _ { 2 } { ' } . } \end{array} \right.
$$

The expressions for the ratios of triangles then become

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { [ 2 , 3 ] } { [ 1 , 3 ] } = \frac { x _ { 2 } y _ { 3 } - x _ { 3 } y _ { 2 } } { x _ { 1 } y _ { 3 } - x _ { 3 } y _ { 1 } } = \frac { + ~ g _ { 3 } } { f _ { 1 } g _ { 3 } - f _ { 3 } g _ { 1 } } , } \\ { \displaystyle \frac { [ 1 , 2 ] } { [ 1 , 3 ] } = \frac { x _ { 1 } y _ { 2 } - x _ { 2 } y _ { 1 } } { x _ { 1 } y _ { 3 } - x _ { 3 } y _ { 1 } } = \frac { - ~ g _ { 1 } } { f _ { 1 } g _ { 3 } - f _ { 3 } g _ { 1 } } . } \end{array} \right.
$$

The numerators and denominators of the expressions for the right members of these equations are found from (75) to be expansible as power series in $\tau _ { 1 }$ and $\pmb { \tau _ { 3 } }$ .But in order to simplify (83） it is convenient to let

$$
\left\{ \begin{array} { l l } { k ( t _ { 3 } - t _ { 1 } ) = \tau _ { 3 } - \tau _ { 1 } = 2 \tau , } \\ { \tau _ { 1 } = - \tau + \epsilon , \qquad \tau _ { 3 } = + \tau + \epsilon , } \end{array} \right.
$$

where e is in general small compared to $\boldsymbol { \tau }$ ,and will be supposed to be of the order of $\scriptstyle { \pmb { \tau } } ^ { 2 }$ ，Then the expressions for the ratios of the triangles become

$$
\left\{ \begin{array} { l } { { \displaystyle \frac { [ 2 , 3 ] } { [ 1 , 3 ] } = \frac { \textstyle + g _ { 3 } } { f _ { 1 } g _ { 3 } - f _ { 3 } g _ { 1 } } = \frac { 1 } { 2 } + \frac { \epsilon } { 2 \tau } + \frac { 1 } { 4 } u \tau ^ { 2 } P + \frac { \tau \epsilon } { 1 2 } u Q , } } \\ { { \displaystyle \frac { [ 1 , 2 ] } { [ 1 , 3 ] } = \frac { - g _ { 1 } } { f _ { 1 } g _ { 3 } - f _ { 3 } g _ { 1 } } = \frac { 1 } { 2 } - \frac { \epsilon } { 2 \tau } + \frac { 1 } { 4 } u \tau ^ { 2 } P - \frac { \tau \epsilon } { 1 2 } u Q , } } \\ { { \displaystyle P = 1 - \frac { \epsilon ^ { 2 } } { \tau ^ { 2 } } - 2 p \epsilon + \frac { 1 } { 1 2 } ( 7 u - 1 5 p ^ { 2 } + 3 q ) \tau ^ { 2 } + \cdots , } } \\ { { \displaystyle Q = 1 - \frac { \epsilon ^ { 2 } } { \tau ^ { 2 } } + \frac { 3 } { 2 } p \frac { \tau ^ { 2 } } { \epsilon } - 3 p \epsilon + \frac { 1 } { 6 0 } ( 3 7 u - 7 6 5 p ^ { 2 } + 1 5 3 q ) \tau ^ { 2 } } } \\ { { \displaystyle \qquad + \frac { 1 } { 4 } p ( 3 u + 1 4 p ^ { 2 } - 6 q ) \frac { \tau ^ { 4 } } { \epsilon } + \cdots , } } \end{array} \right.
$$

where all terms up to the sixth order have been written. The quantity $\textbf { \em u }$ is defined by $u = { \frac { 1 } { r _ { 2 } { } ^ { 3 } } }$ and $p$ and $\pmb q$ are defined in (74).

On making use of equations (86), equation (83) becomes

$$
\Delta _ { 2 } \rho _ { 2 } = K + \frac { \tau ^ { 2 } } { 4 r _ { 2 } ^ { 3 } } P K _ { 1 } + \frac { \tau \epsilon } { 1 2 r _ { 2 } ^ { 3 } } Q K _ { 2 } ,
$$

where

$$
\begin{array} { r } { { \boldsymbol { K } } = - \frac { 1 } { 2 } | \begin{array} { l l l } { \lambda _ { 1 } , } & { X _ { 1 } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { Y _ { 1 } , } & { \mu _ { 2 } } \\ { \nu _ { 1 } , } & { Z _ { 1 } , } & { \nu _ { 3 } } \end{array} | + | \begin{array} { l l l } { \lambda _ { 1 } , } & { X _ { 2 } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { Y _ { 2 } , } & { \mu _ { 3 } } \\ { \nu _ { 1 } , } & { Z _ { 2 } , } & { \nu _ { 3 } } \end{array} | - \frac { 1 } { 2 } | \begin{array} { l l l } { \lambda _ { 1 } , } & { X _ { 3 } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { Y _ { 3 } , } & { \mu _ { 3 } } \\ { \nu _ { 1 } , } & { Z _ { 3 } , } & { \nu _ { 3 } } \end{array} | , } \\ { { \boldsymbol { K } } _ { 1 } = - | \begin{array} { l l l } { \lambda _ { 1 } , } & { X _ { 1 } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { Y _ { 1 } , } & { \mu _ { 3 } } \\ { \nu _ { 1 } , } & { Z _ { 1 } , } & { \nu _ { 3 } } \end{array} | - | \begin{array} { l l l } { \lambda _ { 1 } , } & { X _ { 3 } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { Y _ { 3 } , } & { \mu _ { 3 } } \\ { \nu _ { 1 } , } & { Z _ { 3 } , } & { \nu _ { 3 } } \end{array} | , } \\  { \boldsymbol { K } } _ { 2 } = - | \begin{array} { l l l } { \lambda _ { 1 } , } & { X _ { 1 } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { Y _ { 1 } , } & { \mu _ { 2 } } \\ { \nu _ { 1 } , } & { Z _ { 1 } , } & { \nu _ { 3 } } \end{array} | + | \begin{array} { l l l } { \lambda _ { 1 } , } & { X _ { 2 } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { X _ { 3 } , } &   \end{array} \end{array}
$$

The right members of the expressions for $\textstyle K , K _ { 1 } ,$ and $\pmb { K _ { 2 } }$ add giving the simpler expressions

$$
\begin{array} { r } { \left\{ \begin{array} { l l l } { K = - \displaystyle \frac { 1 } { 2 } \left| \begin{array} { l l l } { \lambda _ { 1 } , } & { X _ { 1 } + X _ { 3 } - 2 X _ { 2 } , } & { \lambda _ { 3 } - \lambda _ { 1 } } \\ { \mu , } & { Y _ { 1 } + Y _ { 3 } - 2 Y _ { 2 } , } & { \mu _ { 3 } - \mu _ { 1 } } \\ { \nu _ { 1 } , } & { Z _ { 1 } + Z _ { 3 } - 2 Z _ { 2 } , } & { \nu _ { 3 } - \nu _ { 1 } } \end{array} \right| , } \\ { K _ { 1 } = - \displaystyle \left| \begin{array} { l l l } { \lambda _ { 1 } , } & { X _ { 1 } + X _ { 3 } , } & { \lambda _ { 3 } - \lambda _ { 1 } } \\ { \mu _ { 1 } , } & { Y _ { 1 } + Y _ { 3 } , } & { \mu _ { 3 } - \mu _ { 1 } } \\ { \nu _ { 1 } , } & { Z _ { 1 } + Z _ { 3 } , } & { \nu _ { 3 } - \nu _ { 1 } } \end{array} \right| , } \\ { K _ { 2 } = + \left| \begin{array} { l l l } { \lambda _ { 1 } , } & { X _ { 5 } - X _ { 1 } , } & { \lambda _ { 3 } - \lambda _ { 1 } } \\ { \mu _ { 1 } , } & { Y _ { 5 } - Y _ { 1 } , } & { \mu _ { 3 } - \mu _ { 1 } } \\ { \nu _ { 1 } , } & { Z _ { 5 } - Z _ { 1 } , } & { \nu _ { 3 } - \nu _ { 1 } } \end{array} \right| } \end{array} \right. } \end{array}
$$

Consider equation (87). The determinant $\Delta _ { 2 }$ by which the left member is multiplied is given in terms of the $\alpha _ { i }$ and $\delta _ { i }$ by (66), which appeared in the method of Laplace.It can also be written, by properly combining columns,in the form

$$
\Delta _ { 2 } = { \left| \begin{array} { l l l } { \lambda _ { 1 } , } & { \lambda _ { 2 } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { \mu _ { 2 } , } & { \mu _ { 3 } } \\ { \nu _ { 1 } , } & { \nu _ { 2 } , } & { \nu _ { 3 } } \end{array} \right| } = { \left| \begin{array} { l l l } { \lambda _ { 1 } , } & { \lambda _ { 1 } + \lambda _ { 3 } - 2 \lambda _ { 2 } , } & { \lambda _ { 3 } - \lambda _ { 1 } } \\ { \mu _ { 1 } , } & { \mu _ { 1 } + \mu _ { 3 } - 2 \mu _ { 2 } , } & { \mu _ { 3 } - \mu _ { 1 } } \\ { \nu _ { 1 } , } & { \nu _ { 1 } + \nu _ { 3 } - 2 \nu _ { 2 } , } & { \nu _ { 3 } - \nu _ { 1 } } \end{array} \right| } .
$$

If $\lambda _ { i } , ~ \mu _ { i } , ~ \nu _ { i }$ are replaced by the series (28)，taking $\tau _ { 2 } = 0$ ，the second column is of the second order and the third column is of the first order in the time-intervals. Therefore $\Delta _ { 2 }$ is of the third order.

Since the left member of (87) is of the third order the right member also must be of the third order. The second column of the expression for $\kappa$ ,the first equation of (88),is of the second order，and the third column is of the first order. Therefore $\kappa$ is of the third order. The determinant $K _ { 1 }$ is of the first order and $K _ { 2 }$ is of the second order. The former is multiplied by $\tau ^ { 2 }$ which is of the second order,and the latter by $\curvearrowleft$ ，which is of the third order. In a preliminary determination of an orbit the terms of higher order may be omitted,after which (87) becomes

$$
\Delta _ { 2 } \rho _ { 2 } = K + \frac { \tau ^ { 2 } K _ { 1 } } { 4 { r _ { 2 } } ^ { 3 } } .
$$

This equation is of the same form as the first of (44),and involves the two unknowns $\pmb { \rho _ { 2 } }$ and $\boldsymbol { r } _ { 2 }$ .They are expressible in terms of a single unknown $\varphi$ by means of equations (46) affected with the subscript 2. The resulting equation has exactly the same form as (48), and its solution gives approximate values of $\pmb { \rho _ { 2 } }$ and $\boldsymbol { r } _ { 2 }$

132. The Equations for $\pmb { \rho _ { 1 } }$ and $\pmb { \rho _ { 3 } }$ ，Equations (80) are linear in $\pmb { \rho _ { 1 } }$ and $\pmb { \rho _ { 3 } } .$ ，and these quantities can be determined from any two of the three equations. The two to be used in practice are those for which the determinant of the coefficients of $\pmb { \rho _ { 1 } }$ and $\pmb { \rho _ { 3 } }$ is the greatest,for they will best determine these quantities.

The solution of the first two equations of (80) for $\pmb { \rho _ { 1 } }$ and $\pmb { \rho _ { 2 } }$ if they are written frst in determinant form,and if they are then expanded as a sum of determinants, is

$$
\begin{array} { r } { \{ | \begin{array} { l l } { \lambda _ { 1 } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { \mu _ { 3 } } \end{array} | \rho _ { 1 } = | \begin{array} { l l } { X _ { 1 } , } & { \lambda _ { 3 } } \\ { Y _ { 1 } , } & { \mu _ { 3 } } \end{array} | - [ \begin{array} { l } { 1 , 3 } \\ { 2 , 3 } \end{array} ] | \begin{array} { l l } { X _ { 2 } , } & { \lambda _ { 3 } } \\ { Y _ { 2 } , } & { \mu _ { 3 } } \end{array} | } \\ & { \phantom { = } + [ \begin{array} { l l } { [ 1 , 2 ] } \end{array} ] | \begin{array} { l l } { X _ { 3 } , } & { \lambda _ { 3 } } \\ { Y _ { 3 } , } & { \mu _ { 3 } } \end{array} | + \rho _ { 2 } [ \begin{array} { l } { [ 1 , 3 ] } \\ { 2 , 3 } \end{array} ] | \begin{array} { l l } { \lambda _ { 2 } , } & { \lambda _ { 3 } } \\ { \mu _ { 2 } , } & { \mu _ { 3 } } \end{array} | , } \\ { | \begin{array} { l l } { \lambda _ { 1 } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { \mu _ { 3 } } \end{array} | \rho _ { 3 } = [ \begin{array} { l l } { [ 2 , 3 ] } \end{array} ] | \begin{array} { l l } { \lambda _ { 1 } , } & { X _ { 1 } } \\ { \mu _ { 1 } , } & { Y _ { 1 } } \end{array} | - [ \begin{array} { l } { 1 , 3 } \end{array} ] | \begin{array} { l l } { \lambda _ { 1 } , } & { X _ { 2 } } \\ { \mu _ { 1 } , } & { Y _ { 2 } } \end{array} | } \\ & { \phantom { = } + | \begin{array} { l l } { \lambda _ { 1 } , } & { X _ { 3 } } \\ { \mu _ { 1 } , } & { Y _ { 3 } } \end{array} | + \rho _ { 2 } [ \begin{array} { l l } { [ 1 , 3 ] } \end{array} ] | \begin{array} { l l } { \lambda _ { 1 } , } & { \lambda _ { 2 } } \\ { \mu _ { 1 } , } & { Y _ { 2 } } \end{array} | . } \end{array}
$$

The solution of the first and third equations of (80) differs from this only in that the $\mu _ { i }$ are replaced by the $\nu _ { i }$ ,and the $Y _ { i }$ by the $Z _ { i }$ ； and the solution of the second and third equations of (8O) can be obtained from (89) by changing the $\lambda _ { i } , \ \mu _ { i } , \ X _ { i } ,$ and $Y _ { i }$ to $\mu _ { i } , \nu _ { i } ,$ $\boldsymbol { Y } _ { i } ,$ and $\mathbf { { z } _ { i } }$ respectively.

After $\rho _ { 1 } , \ \rho _ { 2 } ,$ and $\pmb { \rho _ { 3 } }$ have been computed the correction of the time for the time-aberration can be computed. The method was explained in Art.126.

133.Improvement of the Solution. The results so far obtained are only approximate because only the first term of $P$ was retained while the term in $Q$ was entirely neglected. Having found an approximate solution it is easy to correct it. The values of $\rho _ { 1 } , \rho _ { 2 } ,$ and $\pmb { \rho _ { 8 } }$ are known,and the corresponding values of $r$ can be found at each of the three epochs from

$$
r ^ { 2 } = \rho ^ { 2 } + R ^ { 2 } - 2 \rho R \cos \psi ,
$$

which expresses the fact that $s , E$ and $\pmb { C }$ form triangles at the dates of the three observations. After $r _ { 1 } , \ r _ { 2 }$ and $\pmb { r _ { 3 } }$ have been found the first and second derivatives of $r$ at $t = t _ { 2 }$ can be found by the method of Art. 113. Then equations (74) define $p$ and $q$ after which more approximate values of $P$ and $Q$ can be determined.

134.The Method of Gauss for Computing the Ratios of the Triangles. Equation (83)，which is fundamental in determining $\pmb { \rho _ { 2 } }$ and $\mathbf { \hat { r } _ { 2 } } .$ ,involves two ratios of triangles. It follows from (86) that they can be written in the form

$$
\left\{ \begin{array} { l l } { \frac { [ 2 , 3 ] } { [ 1 , 3 ] } = \frac { 1 } { 2 } + \frac { \epsilon } { 2 \tau } + \frac { P _ { 1 } } { r _ { 2 } ^ { 3 } } , } \\ { \frac { [ 1 , 2 ] } { [ 1 , 3 ] } = \frac { 1 } { 2 } - \frac { \epsilon } { 2 \tau } + \frac { P _ { 2 } } { { r _ { 2 } } ^ { 3 } } . } \end{array} \right.
$$

Consequently，if the ratios of the triangles can be determined $P _ { 1 }$ and $P _ { 2 }$ can be found from these equations. One of the important features of the method of Gauss is a convenient means of determining the ratios of the triangles. In order to apply this method it is necessary to find the inclination and node of the orbit and the argument of the latitude at the dates of the observations.

Since the geocentric coordinates are all known after $\rho _ { 1 } , ~ \rho _ { 2 } , ~ \rho _ { 3 }$ have been determined, the heliocentric coordinates can be computed. Suppose ecliptic coordinates are used and that the longitudes and latitudes,as well as the distances，are known at $t _ { 1 } , t _ { 2 }$ and $t _ { 3 }$ ，The inclination is less or greater than $9 0 ^ { \circ }$ according as $l _ { 3 }$ is greater or less than $l _ { 1 }$ Then it follows from the spherical triangles $C _ { 1 } \Omega l _ { 1 }$ and $\mathrm { C } _ { 3 } \Omega l _ { 3 }$ that

![](images/f50f14cf8c0a7416965e9f7d66fa312c501d4f6741358b23b3af45a7ecda2abb.jpg)  
Fig. 37.

$$
\begin{array} { r } { \left\{ \tan i \sin ( l _ { 1 } - \theta ) = \tan b _ { 1 } , \right. } \\ { \left. \tan i \sin ( l _ { 3 } - \theta ) = \tan b _ { 3 } . \right. } \end{array}
$$

But $l _ { 3 } - \Omega = ( l _ { 3 } - l _ { 1 } ) + ( l _ { 1 } - \delta 3 )$ ； therefore these equationgbecome

$$
\left\{ \begin{array} { l l } { \tan i \sin ( { l _ { 1 } } - \delta ) = \tan b _ { 1 } , } \\ { \tan i \cos ( { l _ { 1 } } - \delta ) = { \displaystyle { \frac { \tan b _ { 3 } - \tan b _ { 1 } \cos ( { l _ { 3 } } - { l _ { 1 } } ) } { \sin ( { l _ { 3 } } - { l _ { 1 } } ) } } } , } \end{array} \right.
$$

which determine $\textit { i }$ and $\Omega$ uniquely since the quadrant of $\mathbf { \chi } _ { i }$ is al ready known from the sign of ${ \mathit { l } } _ { 3 } - { \mathit { l } } _ { 1 }$ ·

The longitude of $\boldsymbol { C }$ from the node is called the argument of the latitude.It follows from Fig.37 that

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \cos { ( l _ { i } - \Omega ) } \cos { b _ { i } } = \cos { u _ { i } } , \qquad ( j = 1 , \ 2 , \ 3 ) , } \\ { \sin { ( l _ { i } - \Omega ) } \cos { b _ { i } } = \sin { u _ { i } } \cos { i } , } \\ { \sin { b _ { i } } = \sin { u _ { i } } \sin { i } , } \end{array} \right. } \end{array}
$$

which uniquely define $u _ { 1 } , u _ { 2 } ,$ and $\boldsymbol { \mathscr { u } } _ { 3 }$

Let $\pmb { A }$ equal the area of the sector contained between the radii $\mathbf { \Delta } r _ { 1 }$ and $\pmb { r _ { 2 } }$ and the orbit. Then the ratio of the area of the sector to the area of the triangle contained between $\pmb { r _ { 1 } }$ and $\pmb { r _ { 2 } }$ is

$$
\eta = \frac { A } { \left[ r _ { 1 } , \ r _ { 2 } \right] } = \frac { k \sqrt { p } \ ( t _ { 2 } - t _ { 1 } ) } { r _ { 1 } r _ { 2 } \sin \left( u _ { 2 } - u _ { 1 } \right) } ,
$$

where $\pmb { p }$ now represents the parameter of the conic. Suppose the corresponding ratios for $t _ { 3 } - t _ { 1 }$ and $t _ { 3 } - t _ { 2 }$ have been found;then the ratios of the triangles are known. The method of Gauss depends upon the determination of these ratios. Each of these quantities is defined by two simultaneous equations in two unknown quantities.

135.The First Equation of Gauss. The polar equation of the conic gives

$$
\left\{ \begin{array} { l l } { \underline { { p } } _ { 1 } = 1 + e \cos v _ { 1 } , } \\ { r _ { 1 } } \\ { \underline { { p } } _ { 2 } = 1 + e \cos v _ { 2 } , } \end{array} \right.
$$

whence

$$
\begin{array} { c } { p \frac { r _ { 1 } + r _ { 2 } } { r _ { 1 } r _ { 2 } } = 2 + e ( \cos v _ { 1 } + \cos v _ { 2 } ) } \\ { = 2 + 2 e \cos \left( \frac { v _ { 2 } + v _ { 1 } } { 2 } \right) \cos \left( \frac { v _ { 2 } - v _ { 1 } } { 2 } \right) . } \end{array}
$$

Since $v _ { 2 } - v _ { 1 } = u _ { 2 } - u _ { 1 }$ is known, the only unknown in the right member of this equation is ecos (），which will o be eliminated. From the equations of Art. 98 it follows that

$$
\left\{ \begin{array} { l l } { \sqrt { r _ { 1 } } \cos \frac { v _ { 1 } } { 2 } = \sqrt { a ( 1 - e ) } \cos \frac { E _ { 1 } } { 2 } , } \\ { \sqrt { r _ { 1 } } \sin \frac { v _ { 1 } } { 2 } = \sqrt { a ( 1 + e ) } \sin \frac { E _ { 1 } } { 2 } , } \\ { \sqrt { r _ { 2 } } \cos \frac { v _ { 2 } } { 2 } = \sqrt { a ( 1 - e ) } \cos \frac { E _ { 2 } } { 2 } , } \\ { \sqrt { r _ { 2 } } \sin \frac { v _ { 2 } } { 2 } = \sqrt { a ( 1 + e ) } \sin \frac { E _ { 2 } } { 2 } . } \end{array} \right.
$$

From these equations it is found that

$$
\begin{array} { r } { \{ \sqrt { r _ { 1 } r _ { 2 } } \cos ( \frac { v _ { 2 } - v _ { 1 } } { 2 } ) = a \cos ( \frac { E _ { 2 } - E _ { 1 } } { 2 } ) - a e \cos ( \frac { E _ { 2 } + E _ { 1 } } { 2 } ) , \ } \\ { \sqrt { r _ { 1 } r _ { 2 } } \cos ( \frac { v _ { 2 } + v _ { 1 } } { 2 } ) = a \cos ( \frac { E _ { 2 } + E _ { 1 } } { 2 } ) - a e \cos ( \frac { E _ { 2 } - E _ { 1 } } { 2 } ) . \ } \end{array}
$$

On eliminating e cos $\left( \frac { E _ { 2 } + E _ { 1 } } { 2 } \right)$ and slig oeo $\left( { \frac { v _ { 2 } + v _ { 1 } } { 2 } } \right)$ it is found that

$$
e \cos \left( \frac { v _ { 2 } + v _ { 1 } } { 2 } \right) = \frac { \upsilon } { \sqrt { r _ { 1 } r _ { 2 } } } \cos \left( \frac { E _ { 2 } - E _ { 1 } } { 2 } \right) - \cos \left( \frac { v _ { 2 } - v _ { 1 } } { 2 } \right) .
$$

As a consequence of this equation (94) reduces to

$$
p = \frac { 2 r _ { 1 } r _ { 2 } \sin ^ { 2 } \left( \frac { \vartheta _ { 2 } - v _ { 1 } } { 2 } \right) } { r _ { 1 } + r _ { 2 } - 2 \sqrt { r _ { 1 } r _ { 2 } } \cos \left( \frac { \vartheta _ { 2 } - v _ { 1 } } { 2 } \right) \cos \left( \frac { E _ { 2 } - E _ { 1 } } { 2 } \right) } \cdot
$$

On eliminating $\pmb { p }$ from this equation and (93) the equation

$$
\eta ^ { 2 } = \frac { k ^ { 2 } ( t _ { 2 } - t _ { 1 } ) ^ { 2 } \sec ^ { 2 } \left( \displaystyle \frac { v _ { 2 } - v _ { 1 } } { 2 } \right) } { 2 r _ { 1 } r _ { 2 } \left\{ r _ { 1 } + r _ { 2 } - 2 \sqrt { r _ { 1 } r _ { 2 } } \cos \left( \displaystyle \frac { v _ { 2 } - v _ { 1 } } { 2 } \right) \cos \left( \displaystyle \frac { E _ { 2 } - E _ { 1 } } { 2 } \right) \right\} }
$$

is obtained.In order to simplify it let

$$
\left\{ \begin{array} { l l } { \displaystyle v _ { 2 } - v _ { 1 } = u _ { 2 } - u _ { 4 } = 2 f , } \\ { \displaystyle E _ { 2 } - E _ { 1 } \ ~ = 2 g , } \\ { \displaystyle m = \frac { \dot { k } ( t _ { 2 } - t _ { 1 } ) } { ( 2 \sqrt { \dot { \sqrt { \kappa _ { 1 } r _ { 2 } } } \cos f ) ^ { \sharp } } } , } \\ { \displaystyle l = \frac { r _ { 1 } \div { \ r _ { 2 } } } { 4 \sqrt { r _ { 1 } r _ { 2 } } \cos f } - \frac { 1 } { 2 } . } \end{array} \right.
$$

Then the expression for $\pmb { \eta } ^ { 2 }$ reduces to

$$
\eta ^ { 2 } = \frac { m ^ { 2 } } { l + \mathrm { s i n } ^ { 2 } \frac { g } { 2 } } ,
$$

in which $\eta$ and $g$ are the unknowns. This is the first equation in the method of Gauss.

136.The Second Equation of Gauss. An independent equation involving $\eta$ and $g$ will now be derived.It will be made to depend upon Kepler's equation，thus insuring its independence of (98) which was derived without reference to Kepler's equation The first equations are

$$
\left\{ \begin{array} { l l } { M _ { 1 } = \displaystyle \frac { k ( t _ { 1 } - T ) } { a ^ { \frac { 3 } { 2 } } } = E _ { 1 } - e \sin E _ { 1 } , } \\ { M _ { 2 } = \displaystyle \frac { k ( t _ { 2 } - T ) } { a ^ { \frac { 3 } { 2 } } } = E _ { 2 } - e \sin E _ { 2 } ; } \end{array} \right.
$$

whence

$$
\frac { k ( t _ { 2 } - t _ { 1 } ) } { a ^ { 3 } } = 2 g - 2 e \sin g \cos \left( \frac { E _ { 2 } + E _ { 1 } } { 2 } \right) .
$$

The quantities $\pmb { a }$ and e cos $\left( \frac { E _ { 2 } + E _ { 1 } } { 2 } \right) ;$ must be eliminated in order to reduce this equation to the required type. On making use of the first equation following (95),it is found that

$$
\frac { k ( t _ { 2 } - t _ { 1 } ) } { a ^ { \frac { 3 } { 4 } } } = 2 g - \sin 2 g + 2 \frac { \sqrt { r _ { 1 } r _ { 2 } } } { a } \sin g \cos f .
$$

It remains to eliminate $^ { a }$ By Art. 98

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { r _ { 1 } } { a } = 1 - e \cos E _ { 1 } , } \\ { \quad } \\ { \displaystyle \frac { r _ { 2 } } { a } = 1 - e \cos E _ { 2 } ; } \end{array} \right.
$$

whence

$$
\frac { r _ { 1 } + r _ { 2 } } { a } = 2 - 2 e \cos g \cos \left( \frac { E _ { 2 } + E _ { 1 } } { 2 } \right) .
$$

On eliminating $e \cos \left( { \frac { E _ { 2 } + E _ { 1 } } { 2 } } \right)$ by the frst equation following (95) this equation becomes

$$
{ \frac { 1 } { a } } = { \frac { 2 \sin ^ { 2 } g } { r _ { 1 } + r _ { 2 } - 2 { \sqrt { r _ { 1 } r _ { 2 } } } \cos g \cos f } } ,
$$

which becomes as a consequence of the expression for $\pmb { \eta ^ { 2 } }$

$$
\frac { 1 } { a } = \bigg ( \frac { 2 \eta \sin g \cos f } { k ( t _ { 2 } - t _ { 1 } ) } \bigg ) ^ { 2 } r _ { 1 } r _ { 2 } .
$$

On eliminating $^ { a }$ between (99) and (100),it is found that

$$
\frac { \eta ^ { 3 } } { m ^ { 2 } } - \frac { \eta ^ { 2 } } { m ^ { 2 } } = \frac { 2 g - \sin 2 g } { \sin ^ { 3 } g } ,
$$

which is the second equation in $\pmb { \eta }$ and $g$ .There are similar equations for the time-intervals $t _ { 3 } - t _ { 1 }$ and $t _ { 3 } - t _ { 2 }$

137.Solution of (98) and (1o1). It follows from the definition of $\pmb { \eta }$ that it is positive if the heliocentric motion in the orbit is less than $1 8 0 ^ { \circ }$ in the interval $t _ { 2 } - t _ { 1 }$ .It will be supposed in what follows that the observations are so close together that this condition is fulflled.

Let

$$
\left\{ \begin{array} { c } { { \sin ^ { 2 } \displaystyle \frac { g } { 2 } = x , } } \\ { { \displaystyle \frac { 2 g - \sin 2 g } { \sin ^ { 3 } g } = X . } } \end{array} \right.
$$

On eliminating $\pmb { \eta }$ from (98) and (101) and making use of (102), it is found that

$$
m = ( l + x ) ^ { \sharp } + X ( l + x ) ^ { \sharp } .
$$

The quantity $X$ must now be expressed in terms of $_ x$ ,after which (103)will involve this quantity alone as an unknown. This will be cione by first expressing $X$ in terms of $g$ ,and then $g$ in terms of $x$ The following are well-known expansions of the trigonometrical functions:

whence

$$
{ \left\{ \begin{array} { l l } { \sin 2 g = 2 g - { \frac { 4 } { 8 } } g ^ { 3 } + { \frac { 4 } { 1 5 } } g ^ { 5 } - { \frac { 8 } { 3 1 5 } } g ^ { 7 } + { \frac { 8 } { 5 6 7 0 } } g ^ { 9 } - \cdots { \cdot \cdot \cdot } _ { 9 } } \\ { \sin ^ { 3 } g = g ^ { 3 } - { \frac { 1 } { 2 } } g ^ { 5 } + { \frac { 1 3 } { 1 2 } } g ^ { 7 } - { \frac { 4 } { 3 0 } } { \frac { 1 } { 2 } } g ^ { 9 } + \cdots { \cdot \cdot \cdot } ; } \end{array} \right. }
$$

$$
\begin{array} { l } { { X = \frac { 4 } { 8 } - \frac { 4 } { 1 5 } g ^ { 2 } + \frac { 8 } { 3 1 5 } g ^ { 4 } - \frac { 8 } { 5 6 7 0 } g ^ { 6 } + \cdots } } \\ { { \overline { { { 1 - \frac { 1 } { 2 } g ^ { 2 } } + \frac { 1 3 } { 1 2 0 } g ^ { 4 } - \frac { 4 1 } { 3 0 2 4 } g ^ { 6 } + \cdots } } } } \\ { { = \frac { 4 } { 3 } ( 1 + \frac { 3 } { 1 0 } g ^ { 2 } + \frac { 1 7 } { 2 8 0 } g ^ { 4 } + \frac { 2 9 } { 2 8 0 0 } g ^ { 6 } + \cdots ) . } } \end{array}
$$

From the first of (102) it follows that

$$
\left\{ \begin{array} { l l } { g = 2 \sin ^ { - 1 } ( x ^ { \mathfrak { i } } ) = 2 x ^ { \mathfrak { i } } + \frac { 1 } { 3 } x ^ { \mathfrak { i } } + \frac { 3 } { 2 0 } x ^ { \mathfrak { s } } + \frac { 5 } { 5 6 } x ^ { \mathfrak { i } } + \cdots , } \\ { g ^ { 2 } = 4 x + \frac { 4 } { 3 } x ^ { 2 } + \frac { 3 2 } { 4 5 } x ^ { 3 } + \frac { 1 6 } { 3 6 } x ^ { 4 } + \cdots , } \\ { g ^ { 4 } = 1 6 x ^ { 2 } + \frac { 3 2 } { 8 } x ^ { 3 } + \frac { 1 1 2 } { 1 5 } x ^ { 4 } + \cdots , } \\ { g ^ { 6 } = 6 4 x ^ { 3 } + 6 4 x ^ { 4 } + \cdots . } \end{array} \right.
$$

Then (104) becomes

.or

$$
\begin{array} { c } { { X = \frac 4 3 [ 1 + \frac 6 5 x + \frac 6 5 \cdot \mathbb { X } ^ { 2 } + \frac 6 5 \cdot \mathbb { X } \cdot 1 0 } } \\ { { X = \frac 1 4 [ 1 + \frac 6 5 x + \frac 6 5 \cdot \mathbb { X } ^ { 2 } \times ^ { 2 } + \frac 6 5 \cdot \mathbb { X } \cdot 1 0 } } \\ { { = \frac 1 3 \cdot ( \frac 1 5 x + \frac 6 5 \cdot \mathbb { X } ^ { 2 } + \frac 6 5 \cdot \mathbb { X } ^ { 6 } + \cdots ) ^ { - 1 } } } \\ { { = \frac 1 3 \cdot \frac 9 4 - \frac 9 { 1 0 } [ x - \frac 2 { 3 5 } x ^ { 2 } - \frac { 5 2 } { 1 5 7 5 } x ^ { 3 } + \cdots ] } } \\ { { \vdots } } \\ { { \xi = \frac 2 { 3 5 } x ^ { 2 } + \frac { 5 2 } { 1 5 7 5 } x ^ { 3 } + \cdots . } } \end{array}
$$

Let

If $\scriptstyle { \frac { 1 } { 2 } } g$ is a small quantity of the frst order, $\pmb { x }$ is of the second order .and $\xi$ is of the fourth order.

From (98) it is found that

$$
x = { \frac { m ^ { 2 } } { \eta ^ { 2 } } } - l .
$$

Let

$$
h = \frac { m ^ { 2 } } { \frac { 5 } { 6 } + l + \xi } ;
$$

then (101) may be written

$$
\eta - 1 = \frac { m ^ { 2 } X } { \eta ^ { 2 } } = \frac { \frac { 1 0 } { 9 } h } { \eta ^ { 2 } - h } ,
$$

fromwhich it is found that

$$
n ^ { 3 } - \eta ^ { 2 } - h \eta - \frac { h } { 9 } = 0 .
$$

If $\xi$ were known $^ { h }$ wculd be determined by (107) and $\pmb { \eta }$ by (108), which has but one real positive root. In the first approximation .compute $h$ assuming that the small quantity $\xi$ is zero; then find the real positive root of (1o8)． Or,instead of computing the root, use may be made of the tables which have been constructed by Gauss, giving the real positive values of $\eta$ for values of $h$ ranging from O to O.6.\* The value of $_ x$ is then computed by (106) and the value of $\xi$ by (105). $\dagger$ With this value of $\xi , h$ ,and $\eta$ are recomputed, .and the process is repeated until the desired degree of precision is attained. Experience has shown that this method of computing the ratio of the sector to the triangle converges very rapidly,even when the time-interval is considerable.

The species of conic section is decided at this point, the orbit being an elipse, parabola,or hyperbola according as $_ x$ is positive, zero, or negative; for,x = sin² $x = \sin ^ { 2 } { \frac { g } { 2 } } = \sin ^ { 2 } { \frac { 1 } { 4 } } ( E _ { 2 } - E _ { 1 } )$ ,and $E _ { 2 }$ and ${ \bf { { E } } } _ { 1 }$ are real in ellipses, zero in parabolas,and imaginary in hyperbolas.

Gauss has introduced a transformation which facilitates the computation of $ { \boldsymbol { l } }$ which was defined in the last equation of (97).t Let

$$
\sqrt [ 4 ] { \frac { r _ { 2 } } { r _ { 1 } } } = \tan { ( 4 5 ^ { \circ } + \omega ^ { \prime } ) } , ~ 0 ^ { \circ } \leq \omega ^ { \prime } \leq 4 5 ^ { \circ } ;
$$

whence

$$
\frac { \overline { { r _ { 1 } } } + \displaystyle r _ { 2 } } { \sqrt { r _ { 1 } r _ { 2 } } } = \sqrt { \frac { \overline { { r _ { 2 } } } } { r _ { 1 } } } + \sqrt { \frac { \overline { { r _ { 1 } } } } { r _ { 2 } } } = \tan ^ { 2 } { \left( 4 5 ^ { \circ } + \omega ^ { \prime } \right) } + \cot ^ { 2 } { \left( 4 5 ^ { \circ } + \omega ^ { \prime } \right) } ,
$$

or

$$
\frac { r _ { 1 } + r _ { 2 } } { \sqrt { r _ { 1 } r _ { 2 } } } = 2 + 4 \tan ^ { 2 } 2 \omega ^ { \prime } .
$$

Then the last equation of (97) becomes

$$
l = \frac { \sin ^ { 2 } \frac { f } { 2 } + \tan ^ { 2 } 2 \omega ^ { \prime } } { \cos f } .
$$

138.Determination of the Elements $a , e ,$ and $\pmb { \omega }$ After $\pmb { \mathscr { g } }$ has been found by the method of Art.137 it is easy to obtain the elements $a , e _ { \mathrm { i } }$ and $\pmb { \omega }$ The major semi-axis $^ { a }$ is defined by the last equation on page 240,or by the preceding equation for the longer time-interval $t _ { 3 } - t _ { 1 } ,$

$$
a = { \frac { r _ { 1 } + r _ { 3 } - 2 \sqrt { r _ { 1 } r _ { 3 } } \cos g \cos f } { 2 \sin ^ { 2 } g } } .
$$

The parameter of the orbit $\pmb { p }$ is determined by equation (93). Since

$$
p = a ( 1 - e ^ { 2 } ) \quad { \mathrm { o r } } \quad p = a ( e ^ { 2 } - 1 )
$$

according as the orbit is an ellipse or hyperbola, $\pmb { e }$ is determined when $^ { a }$ and $p$ are known.

If the angle $\pmb { v }$ is computed from the perihelion point it is related to the heliocentric distances and $^ e$ and $\pmb { p }$ by the polar equation of the conic,

$^ \ddagger$ Theoria Motus,Art.86.

$$
r _ { i } = \frac { p } { 1 + e \cos v _ { i } } \qquad ( i = 1 , 2 , 3 ) .
$$

Either of these equations determines a value of $v$ since $\pmb { r }$ is known at $t _ { 1 } , t _ { 2 } ,$ and $t _ { 3 } ,$ and then $\pmb { \omega }$ is determined by

$$
\omega = u _ { i } - v _ { i } .
$$

139. Second Method of Determining $a , e ,$ and $\omega$ ：The method of Gauss depends upon the complicated formulas of Arts.135 and 136.If the higher terms of $P$ and $Q$ ,equations (86),give sufficiently accurate values of the ratios of the triangles, there is another method \* which is simpler and especially advantageous when the intervals between the observations are not very great. The data which wil be used in the solution are $r _ { 1 } , u _ { 1 } ; r _ { 2 } , u _ { 2 } ; r _ { 3 } , u _ { 3 } ,$ the heliocentric coordinates at $t _ { 1 } , t _ { 2 }$ and $t _ { 3 }$

The elements $i$ and $\Omega$ can be computed by equations (91), which are valid for any orbit. The difficulties all arise in finding $a , e , \omega$ .Let the parameter $p$ be adopted as an element in place of the major semi-axis $a$ .It is more convenient in that it does not become infinite when $e$ equals unity,and it is involved alone in the equation of areas,

$$
k { \sqrt { p } } d t = r ^ { 2 } d v = r ^ { 2 } d u .
$$

The integral of this equation is

$$
\stackrel { \cdot } { k } \sqrt { p } ( t _ { 3 } - t _ { 1 } ) = \int _ { u _ { 1 } } ^ { u _ { 3 } } r ^ { 2 } d u .
$$

If $r ^ { 2 }$ were expressed in terms of $_ { u }$ the integral in the right member could be found,when the value of $p$ would be given.It will be shown from the knowledge of the value of $r ^ { 2 }$ when $u = u _ { 1 } , u _ { 2 } , u _ { 3 } ,$ viz., $r ^ { 2 } = r _ { 1 } { } ^ { 2 } , r _ { 2 } { } ^ { 2 } , r _ { 3 } { } ^ { 2 }$ ，that $r ^ { 2 }$ can be expressed in terms of $_ { \pmb { u } }$ with sufficient accuracy to give a very close approximation to the value of $p$

For values of $_ { u }$ not too remote from $\boldsymbol { u } _ { 2 }$ the function $r ^ { 2 }$ can be expanded in a converging series of the form

$$
r ^ { 2 } = r _ { 2 } ^ { 2 } + c _ { 1 } ( u - u _ { 2 } ) + c _ { 2 } ( u - u _ { 2 } ) ^ { 2 } + c _ { 3 } ( u - u _ { 2 } ) ^ { 3 } + \cdots .
$$

In an unknown orbit the coefficients of the series (114) are unknown, but it will now be shown how a sufficient number to define $p$ with the desired degree of accuracy can be easily found. By hypothesis, the radii and arguments of latitude are known at the epochs $t _ { 1 } , t _ { 2 } ,$ and $t _ { 3 }$ ：Hence (114) becomes at $t _ { 1 }$ and $t _ { 3 }$

\*F.R.Moulton: The Astronomical Journal, vol. xxi., No.510 (1901).

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { r _ { 1 } { ^ 2 } = r _ { 2 } { ^ 2 } + c _ { 1 } ( u _ { 1 } - u _ { 2 } ) + c _ { 2 } ( u _ { 1 } - u _ { 2 } ) { ^ 2 } } \\ { \qquad \quad + c _ { 3 } ( u _ { 1 } - u _ { 2 } ) ^ { 3 } + c _ { 4 } ( u _ { 1 } - u _ { 2 } ) ^ { 4 } + \cdots , } \\ { r _ { 3 } { ^ 2 } = r _ { 2 } { ^ 2 } + c _ { 1 } ( u _ { 3 } - u _ { 2 } ) + c _ { 2 } ( u _ { 3 } - u _ { 2 } ) { ^ 2 } } \\ { \qquad \quad + c _ { 3 } ( u _ { 3 } - u _ { 2 } ) ^ { 3 } + c _ { 4 } ( u _ { 3 } - u _ { 2 } ) ^ { 4 } + \cdots . } \end{array} \right. } \end{array}
$$

For abbreviation let

$$
\left\{ \begin{array} { l l } { \sigma _ { 1 } = u _ { 3 } - u _ { 2 } , } \\ { \sigma _ { 2 } = u _ { 3 } - u _ { 1 } , } \\ { \sigma _ { 3 } = u _ { 2 } - u _ { 1 } , } \\ { \epsilon _ { 1 } = c _ { 3 } ( u _ { 1 } - u _ { 2 } ) ^ { 3 } + c _ { 4 } ( u _ { 1 } - u _ { 2 } ) ^ { 4 } + \cdots , } \\ { \epsilon _ { 3 } = c _ { 3 } ( u _ { 3 } - u _ { 2 } ) ^ { 3 } + c _ { 4 } ( u _ { 3 } - u _ { 2 } ) ^ { 4 } + \cdots . } \end{array} \right.
$$

Then equations (115) can be written

$$
\left\{ { \begin{array} { l l } { - c _ { 1 } \sigma _ { 3 } + c _ { 2 } { \sigma _ { 3 } } ^ { 2 } = { r _ { 1 } } ^ { 2 } - { r _ { 2 } } ^ { 2 } - \epsilon _ { 1 } , } \\ { + c _ { 1 } \sigma _ { 1 } + c _ { 2 } { \sigma _ { 1 } } ^ { 2 } = { r _ { 3 } } ^ { 2 } - { r _ { 2 } } ^ { 2 } - \epsilon _ { 3 } . } \end{array} } \right.
$$

On solving for $c _ { 1 }$ and $c _ { 2 }$ ,it is found that

$$
\left\{ \begin{array} { l l } { c _ { 1 } = \frac { - { \bf \Gamma } ( r _ { 1 } { } ^ { 2 } - { \bf \Gamma } \mathbf { - } \mathbf { \ } \mathbf { \epsilon } _ { 1 } ) \sigma _ { 1 } { } ^ { 2 } + { \bf \Gamma } ( r _ { 3 } { } ^ { 2 } - { \bf \Gamma } \mathbf { 6 } _ { 3 } ) \sigma _ { 3 } { } ^ { 2 } - { r _ { 2 } } ^ { 2 } ( \sigma _ { 3 } { } ^ { 2 } - \sigma _ { 1 } { } ^ { 2 } ) } { \sigma _ { 1 } \sigma _ { 2 } \sigma _ { 3 } } , } \\ { c _ { 2 } = \frac { ( r _ { 1 } { } ^ { 2 } - { \bf \Gamma } \mathbf { - } { \bf \epsilon } _ { 1 } ) \sigma _ { 1 } + ( r _ { 3 } { } ^ { 2 } - { \bf \Gamma } \mathbf { 6 } _ { 3 } ) \sigma _ { 3 } - { r _ { 2 } } ^ { 2 } \sigma _ { 2 } } { \sigma _ { 1 } \sigma _ { 2 } \sigma _ { 3 } } ; } \end{array} \right.
$$

and,on substituting the values of $\epsilon _ { 1 }$ and $\epsilon _ { 3 } .$

$$
\left\{ \begin{array} { l } { { c _ { 1 } = \frac { - { r _ { 1 } } ^ { 2 } \sigma _ { 1 } { } ^ { 2 } + { r _ { 3 } } ^ { 2 } { \sigma _ { 3 } } ^ { 2 } - { r _ { 2 } } ^ { 2 } ( \sigma _ { 3 } { } ^ { 2 } - { \sigma _ { 1 } } ^ { 2 } ) } { \sigma _ { 1 } \sigma _ { 2 } \sigma _ { 3 } } } } \\ { { \qquad \quad - { c _ { 3 } } \sigma _ { 1 } \sigma _ { 3 } - c _ { 4 } \sigma _ { 1 } \sigma _ { 3 } ( \sigma _ { 1 } - \sigma _ { 3 } ) - \cdots , } } \\ { { c _ { 2 } = \frac { { r _ { 1 } } ^ { 2 } \sigma _ { 1 } + { r _ { 3 } } ^ { 2 } \sigma _ { 3 } - { r _ { 2 } } ^ { 2 } \sigma _ { 2 } } { \sigma _ { 1 } \sigma _ { 2 } \sigma _ { 3 } } } } \\ { { \qquad \quad - { c _ { 3 } } ( \sigma _ { 1 } - \sigma _ { 3 } ) + c _ { 4 } ( 3 \sigma _ { 1 } \sigma _ { 3 } - \sigma _ { 2 } { } ^ { 2 } ) - \cdots . } } \end{array} \right.
$$

Having obtained these expressions for the coefficients of the second and third terms of (114),let this series be substituted for $r ^ { 2 }$ in (113) and the result integrated. On making use of (16),it is easily found that

$$
\begin{array} { l } { { \displaystyle \left. ~ k \sqrt { p } ( t _ { 3 } - t _ { 1 } ) = r _ { 2 } { } ^ { 2 } \sigma _ { 2 } + \frac { c _ { 1 } } { 2 } ( { \sigma _ { 1 } } ^ { 2 } - { \sigma _ { 3 } } ^ { 2 } ) + \frac { c _ { 2 } } { 3 } ( { \sigma _ { 1 } } ^ { 3 } + { \sigma _ { 3 } } ^ { 3 } ) \right. } } \\ { { \displaystyle \left. + \frac { c _ { 3 } } { 4 } ( { \sigma _ { 1 } } ^ { 4 } - { \sigma _ { 3 } } ^ { 4 } ) + \frac { c _ { 4 } } { 5 } ( { \sigma _ { 1 } } ^ { 5 } + { \sigma _ { 3 } } ^ { 5 } ) + \cdots . \right. } } \end{array}
$$

On substituting the values of $\pmb { c _ { 1 } }$ and $\mathbf { c _ { 2 } }$ given in (117),this equation becomes

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { k \sqrt { p } ( t _ { 3 } - \dot { t } _ { 1 } ) = \frac { { r _ { 2 } } ^ { 2 } \sigma _ { 2 } ^ { 3 } } { 6 \sigma _ { 1 } \sigma _ { 3 } } + \frac { { r _ { 1 } } ^ { 2 } \sigma _ { 2 } } { 6 \sigma _ { 3 } } ( 2 \sigma _ { 3 } - \sigma _ { 1 } ) } \\ { \qquad \quad + \frac { { r _ { 3 } } ^ { 2 } \sigma _ { 2 } } { 6 \sigma _ { 1 } } ( 2 \sigma _ { 1 } - \sigma _ { 3 } ) + \frac { { C _ { 3 } } \sigma _ { 2 } ^ { 3 } } { 1 2 } ( \sigma _ { 3 } - \sigma _ { 1 } ) } \\ { \qquad \quad - \frac { { C _ { 4 } } \sigma _ { 2 } ^ { 3 } } { 3 0 } \left\{ 4 ( \sigma _ { 3 } - \sigma _ { 1 } ) ^ { 2 } + \sigma _ { 1 } \sigma _ { 3 } \right\} - \cdots . } \end{array} \right. } \end{array}
$$

If the second observation divides the whole interval into two nearly equal parts，, as generally will be the case in practice, ${ \pmb \sigma } _ { \pmb { 1 } }$ and ${ \pmb \sigma } _ { 3 }$ will be nearly equal.Let

$$
\sigma _ { 1 } - \sigma _ { 3 } = \epsilon , \quad \mathrm { a n d } \quad \sigma _ { 1 } + \sigma _ { 3 } = \epsilon _ { 2 } ;
$$

whence

$$
\left\{ \begin{array} { l l } { \displaystyle \sigma _ { 1 } = \frac { \sigma _ { 2 } + \epsilon } { 2 } , } \\ { \displaystyle \sigma _ { 3 } = \frac { \sigma _ { 2 } - \epsilon } { 2 } , } \end{array} \right.
$$

where e is in general a very small quantity. On substituting these expressions in the last terms of (i18) this equation becomes

$$
\left\{ \begin{array} { l } { { k \sqrt { p } ( t _ { 3 } - t _ { 1 } ) = \displaystyle { \frac { { r _ { 2 } } ^ { 2 } { \sigma _ { 2 } } ^ { 3 } } { 6 \sigma _ { 1 } \sigma _ { 3 } } } + \frac { { r _ { 1 } } ^ { 2 } \sigma _ { 2 } } { 6 \sigma _ { 3 } } \left( 2 \sigma _ { 3 } - \sigma _ { 1 } \right) } } \\ { { \qquad + \displaystyle { \frac { { r _ { 3 } } ^ { 2 } \sigma _ { 2 } } { 6 \sigma _ { 1 } } } \left( 2 \sigma _ { 1 } - \sigma _ { 3 } \right) - \frac { c _ { 3 } \sigma _ { 2 } { } ^ { 3 } \epsilon } { 1 2 } } } \\ { { \qquad - \displaystyle { \frac { c _ { 4 } } { 1 2 0 } } { \sigma _ { 2 } } ^ { 3 } \left( { \sigma _ { 2 } } ^ { 2 } + 1 5 \epsilon ^ { 2 } \right) - \cdots . } } \end{array} \right.
$$

It is found in a similar way on integrating between the limits corresponding to $\mathbf { { f _ { 2 } } }$ and $\mathbf { { \boldsymbol { t } } _ { 1 } }$ that

$$
\left\{ \begin{array} { l l } { { k \sqrt { p } ( t _ { 2 } - t _ { 1 } ) = \displaystyle \frac { { r _ { 2 } } ^ { 2 } \sigma _ { 3 } ( 3 \sigma _ { 1 } + \sigma _ { 3 } ) } { 6 \sigma _ { 1 } } + \displaystyle \frac { { r _ { 1 } } ^ { 2 } \sigma _ { 3 } ( 3 \sigma _ { 1 } + 2 \sigma _ { 3 } ) } { 6 \sigma _ { 2 } } } } \\ { { \displaystyle \qquad - \frac { { r _ { 3 } } ^ { 2 } \sigma _ { 3 } { } ^ { 3 } } { 6 \sigma _ { 1 } \sigma _ { 2 } } + \frac { c _ { 3 } \sigma _ { 3 } { } ^ { 3 } } { 1 2 } ( 2 \sigma _ { 1 } + \sigma _ { 3 } ) } } \\ { { \displaystyle \qquad + \frac { c _ { 4 } } { 3 0 } \sigma _ { 3 } { } ^ { 3 } ( 5 \sigma _ { 1 } { } ^ { 2 } - 5 \sigma _ { 1 } \sigma _ { 3 } - 4 \sigma _ { 3 } { } ^ { 2 } ) + \cdots } . } \end{array} \right.
$$

For the intervals of time which are used in determining an orbit these series converge very rapidly,and an approximate value of $\pmb { p }$ ,which is generally as accurate as is desired,can be obtained by taking only the first three terms\*in the right member of (119). By considering equations (119） and (12O） simultaneously and neglecting terms in $c _ { 4 }$ and of higher order,it is possible to determine both $p$ and $c _ { 3 }$ .But not much increase in accuracy is obtained because the term in $c _ { 3 }$ in (119) is multiplied by the small quantity $\epsilon$ ，while that in $c _ { 4 }$ does not carry this factor. Suppose the value of $p$ has been computed; it will be shown how $\omega$ and $\pmb { \mathscr { q } }$ can be found.

The polar equation of the conic gives

$$
\left\{ \begin{array} { l l } { { e \cos { \left( u _ { 1 } - \omega \right) } = \displaystyle \frac { p - r _ { 1 } } { r _ { 1 } } } , } \\ { { \ } } \\ { { e \cos { \left( u _ { 3 } - \omega \right) } = \displaystyle \frac { p - r _ { 3 } } { r _ { 3 } } } . } \end{array} \right.
$$

Now $u _ { 3 } - \omega = ( u _ { 3 } - u _ { 1 } ) + ( u _ { 1 } - \omega )$ .On substituting this expression for $u _ { 3 } \mathrm { ~ - ~ } \omega$ in the second equation of (121),expanding, and reducing by the first,it is found that

$$
\left\{ \begin{array} { l l } { { e \sin \left( u _ { 1 } - \omega \right) = \displaystyle \frac { r _ { 3 } ( p - r _ { 1 } ) \cos \left( u _ { 3 } - u _ { 1 } \right) - r _ { 1 } ( p - r _ { 3 } ) } { r _ { 1 } r _ { 3 } \sin \left( u _ { 3 } - u _ { 1 } \right) } , } } \\ { { } } \\ { { e \cos \left( u _ { 1 } - \omega \right) = \displaystyle \frac { p - r _ { 1 } } { r _ { 1 } } . } } \end{array} \right.
$$

Since $e$ is positive these equations define $e$ and $\omega$ uniquely.When $p$ and $e$ are known, $a$ is defined by $p = a ( 1 - e ^ { 2 } )$ or $p = a ( e ^ { 2 } - 1 )$ according as the orbit is an ellipse or an hyperbola.

If the elements $a , e _ { \mathrm { i } }$ and $\omega$ have not been found with sufficient approximation it is now possible to correct them.It follows from (114) that

$$
c _ { 3 } = \frac { 1 } { 6 } \frac { \partial ^ { 3 } ( r ^ { 2 } ) } { \partial { u _ { 2 } } ^ { 3 } } , \qquad c _ { 4 } = \frac { 1 } { 2 4 } \frac { \partial ^ { 4 } ( r ^ { 2 } ) } { \partial { u _ { 2 } } ^ { 4 } } ,
$$

and since

$$
r ^ { 2 } = \frac { p ^ { 2 } } { [ 1 + e \cos { ( u - \omega ) } ] ^ { 2 } } ,
$$

it is found that

\*For conditions and rapidity of convergence see the original paper in the Astronomical Journal,No.5io.It is shown there that the elements of asteroid orbits will be given by the first three terms of (119) correct to the sixth decimal place if the whole interval covered by the observations is not more than 40 days,and in the case of comets'orbits,if the interval is not more than 10 days. When the two corrective terms defined by (123) are added the corresponding intervals are 1Oo days and 20 days.

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { c _ { 3 } } { p ^ { 2 } } = \frac { - \mathrm { ~ e ~ s i n ~ } ( u \mathrm { ~ - ~ } \omega ) } { 3 [ 1 + \mathrm { ~ e ~ c o s ~ } ( u \mathrm { ~ - ~ } \omega ) ] ^ { 3 } } + \frac { 3 e ^ { 2 } \sin { ( u \mathrm { ~ - ~ } \omega ) } \cos { ( u \mathrm { ~ - ~ } \omega ) } } { [ 1 + \mathrm { ~ e ~ c o s ~ } ( u \mathrm { ~ - ~ } \omega ) ] ^ { 4 } } } \\ { \displaystyle \qquad + \frac { 4 e ^ { 3 } \sin ^ { 3 } { ( u \mathrm { ~ - ~ } \omega ) } } { [ 1 + \mathrm { ~ e ~ c o s ~ } ( u \mathrm { ~ - ~ } \omega ) ] ^ { 5 } } , } \\ { \displaystyle \frac { c _ { 4 } } { p ^ { 2 } } = \frac { - e \mathrm { ~ c o s ~ } ( u \mathrm { ~ - ~ } \omega ) } { 1 2 [ 1 + \mathrm { ~ e ~ c o s ~ } ( u \mathrm { ~ - ~ } \omega ) ] ^ { 3 } } - \frac { e ^ { 2 } \sin ^ { 2 } { ( u \mathrm { ~ - ~ } \omega ) } } { [ 1 + \mathrm { ~ e ~ c o s ~ } ( u \mathrm { ~ - ~ } \omega ) ] ^ { 4 } } } \\ { \displaystyle \qquad + \frac { 3 e ^ { 2 } \cos ^ { 2 } { ( u \mathrm { ~ - ~ } \omega ) } } { 4 [ 1 + \mathrm { ~ e ~ c o s ~ } ( u \mathrm { ~ - ~ } \omega ) ] ^ { 4 } } + \frac { 6 e ^ { 2 } \sin ^ { 2 } { ( u \mathrm { ~ - ~ } \omega ) } \cos { ( u \mathrm { ~ - ~ } \omega ) } } { [ 1 + \mathrm { ~ e ~ c o s ~ } ( u \mathrm { ~ - ~ } \omega ) ] ^ { 5 } } } \\ { \displaystyle \qquad + \frac { 5 e ^ { 4 } \sin ^ { 4 } { ( u \mathrm { ~ - ~ } \omega ) } } { [ 1 + \mathrm { ~ e ~ c o s ~ } ( u \mathrm { ~ - ~ } \omega ) ] ^ { 5 } } . } \end{array} \right.
$$

With the values of $c _ { 3 }$ and $c _ { 4 }$ computed from these equations the higher terms of (119) can be added,thus determining a more accurate value of $p$ ，after which $e$ and $\omega$ can be recomputed by (122)． Besides being very brief this method has the advantage of being the same for all conics.

140.Computation of the Time of Perihelion Passage. The methods of computing the time of perihelion passage depend upon whether the body moves in a parabola,ellipse,or hyperbola, and are based on the formulas of chap.v.

Parabolic Case. Equation (32),of chap.v., is

$$
k ( t - T ) = \sqrt { 2 } q ^ { 3 } \left[ \tan { \frac { v } { 2 } } + { \frac { 1 } { 3 } } \tan ^ { 3 } { \frac { v } { 2 } } \right] ,
$$

where ${ 2 q } = p$ Since $u = v + \omega$ and $u _ { 1 } , \ u _ { 2 }$ and $\mathbf { \delta } \mathbf { \mathcal { U } } _ { 3 }$ are known, this equation determines $\boldsymbol { T }$

Elliptic Case. The first two equations of (49), chap. $\mathbf { v }$ ., give

$$
\left\{ \begin{array} { l l } { \sin { E } = \frac { \sqrt { 1 - e ^ { 2 } } \sin v } { 1 + e \cos v } , } \\ { \cos { E } = \frac { e + \cos v } { 1 + e \cos v } , } \end{array} \right.
$$

which uniquely define $\boldsymbol { E }$ Then Kepler's equation

$$
M = n ( t - T ) = E - e \sin E
$$

determines $\pmb { T }$ by using $v$ and the corresponding $\pmb { { \cal E } }$ at $t _ { 1 } , t _ { 2 } ,$ or $t _ { 3 } .$ Hyperbolic Case. The quantity $\pmb { F }$ is defined by

$$
\operatorname { t a n h } { \frac { F } { 2 } } = { \sqrt { \frac { e - 1 } { e + 1 } } } \tan { \frac { v } { 2 } } ,
$$

after which $\pmb { T }$ is given by

$$
\frac { k \sqrt { 1 + m } } { a ^ { \frac { 3 } { 2 } } } ( t - T ) = - F + e \sinh F .
$$

141.Direct Derivation of Equations Defining Orbits. The motion of an observed body must satisfy both geometrical and dynamical conditions. Altogether the simplest mode of procedure is to write out at once these conditions. They will involve directly or indirectly many of the equations of the methods of Laplace and Gauss,for these methods both rest in the end on the essentials of the problem.

Let the notation of Art.1l1 be adopted. Think of the sun as an origin. Then obviously the $_ { \pmb { x } }$ -coordinate of $c$ equals the $_ x$ -coordinate of the observer plus the $\pmb { x }$ -coordinate of $\boldsymbol { C }$ with respect to the observer. Similar equations are of course true in the two other coordinates. These relations are explicitly

$$
\left\{ \begin{array} { l l } { - \lambda _ { i } \rho _ { i } + x _ { i } = - X _ { i } , \qquad ( i = 1 , 2 , 3 ) , } \\ { - \mu _ { i } \rho _ { i } + y _ { i } = - Y _ { i } , } \\ { - \nu _ { i } \rho _ { i } + z _ { i } = - Z _ { i } . } \end{array} \right.
$$

These equations are subject to no errors of parallax because the coordinates of the observer have been used. Moreover， they contain all the geometrical relations which exist among the bodies $s , E _ { \mathrm { { \scriptscriptstyle i } } }$ and $\pmb { \mathcal { L } }$ at $t _ { 1 } , t _ { 2 } ,$ and $t _ { 3 }$

The next condition to be applied is that $c$ shall move about $\boldsymbol { s }$ according to the law of gravitation. This is equivalent to stating that its coordinates can be developed in series of the form of (73). On making use of this notation, equations (129) become

$$
\left\{ \begin{array} { l l } { - \lambda _ { 1 } \rho _ { 1 } + f _ { 1 } x _ { 0 } + g _ { 1 } x _ { 0 } \prime = - X _ { 1 } , } \\ { - \lambda _ { 2 } g _ { 2 } + f _ { 2 } x _ { 0 } + g _ { 3 } z _ { 0 } \prime = - X _ { 2 } , } \\ { - \lambda _ { 3 } g _ { 3 } + f _ { 3 } x _ { 0 } + g _ { 3 } x _ { 0 } \prime = - X _ { 3 } , } \\ { - \mu _ { 1 } g _ { 1 } + f _ { 1 } y _ { 0 } + g _ { 1 } y _ { 0 } \prime = - Y _ { 1 } , } \\ { - \mu _ { 2 } g _ { 2 } + f _ { 3 } g _ { 0 } + g _ { 2 } y _ { 0 } \prime = - Y _ { 2 } , } \\ { - \mu _ { 3 } g _ { 3 } + f _ { 3 } y _ { 0 } + g _ { 3 } g _ { 0 } \prime = - Y _ { 3 } ; } \\ { - \nu _ { 1 } \rho _ { 1 } + f _ { 1 } z _ { 0 } + g _ { 1 } z _ { 0 } \prime = - Z _ { 1 } , } \\ { - \nu _ { 2 } g _ { 2 } + f _ { 2 } z _ { 0 } + g _ { 2 } z _ { 0 } \prime = - Z _ { 2 } , } \\ { - \nu _ { 3 } g _ { 3 } + f _ { 3 } z _ { 0 } + g _ { 2 } z _ { 0 } \prime = - Z _ { 3 } . } \end{array} \right.
$$

If the date of the second observation is taken as the origin of time,as is convenient in practice, $f _ { 2 } = 1$ and $g _ { 2 } = 0$

Equations (130) contain fully the geometrical and dynamical conditions of the problem and are valid for all classes of conics. Since they are only the necessary conditions no artificial dificulties or exceptional cases have been introduced；and if in a special case they should fail no other mode of approach could succeed.

The right members of equations (130) are entirely known； the unknowns in the left members are $\rho _ { 1 } , \rho _ { 2 } , \rho _ { 3 } , x _ { 0 } , x _ { 0 } ^ { \prime } , y _ { 0 } , y _ { 0 } ^ { \prime } , z _ { 0 } ,$ and ${ { z } _ { 0 } } ^ { \prime }$ .That is,the number of unknowns exactly equals the number of equations. The quantities $\rho _ { 1 } , \rho _ { 2 } ,$ and $\pmb { \rho _ { 3 } }$ enter linearly,but $\boldsymbol { x } _ { 0 } , \ \cdots , \ \boldsymbol { z } _ { 0 } ^ { \prime }$ occur not only explicitly but also in the higher terms of the $f _ { i }$ and the $g _ { \hat { \imath } }$ ，The solution of (130) for $\rho _ { 1 } , \rho _ { 2 } ,$ and $\pmb { \rho _ { 3 } }$ is

$$
\left\{ \begin{array} { l l } { \Delta _ { 2 } \rho _ { 1 } = + A _ { 1 } - \displaystyle \frac { \left( f _ { 1 } g _ { 3 } - f _ { 3 } g _ { 1 } \right) } { g _ { 3 } } A _ { 2 } - \displaystyle \frac { g _ { 1 } } { g _ { 3 } } A _ { 3 } , } \\ { \Delta _ { 2 } \rho _ { 2 } = \displaystyle \frac { - \ g _ { 3 } } { f _ { 1 } g _ { 3 } - f _ { 3 } g _ { 1 } } B _ { 1 } + B _ { 2 } + \displaystyle \frac { g _ { 1 } } { f _ { 1 } g _ { 3 } - f _ { 3 } g _ { 1 } } B _ { 3 } , } \\ { \Delta _ { 2 } \rho _ { 3 } = \displaystyle \frac { - \ g _ { 3 } } { g _ { 1 } } C _ { 1 } + \displaystyle \frac { \left( f _ { 1 } g _ { 3 } - f _ { 3 } g _ { 1 } \right) } { g _ { 1 } } C _ { 2 } + C _ { 3 } , } \end{array} \right.
$$

where

$$
\left\{ \begin{array} { c c c } { \Delta _ { 2 } = \left| \begin{array} { c c c } { \lambda _ { 1 } , } & { \lambda _ { 2 } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { \mu _ { 2 } , } & { \mu _ { 3 } } \\ { \nu _ { 1 } , } & { \nu _ { 2 } , } & { \nu _ { 3 } } \end{array} \right| , } & { \quad \boldsymbol { A } _ { i } = \left| \begin{array} { c c c } { \boldsymbol { X } _ { i } , } & { \lambda _ { 2 } , } & { \lambda _ { 3 } } \\ { \boldsymbol { Y } _ { i } , } & { \mu _ { 2 } , } & { \mu _ { 3 } } \\ { \boldsymbol { Z } _ { i } , } & { \nu _ { 2 } , } & { \nu _ { 3 } } \end{array} \right| , } \\ { \boldsymbol { B } _ { i } = \left| \begin{array} { c c c } { \lambda _ { 1 } , } & { \boldsymbol { X } _ { i } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { \boldsymbol { Y } _ { i } , } & { \mu _ { 3 } } \\ { \nu _ { 1 } , } & { \boldsymbol { Z } _ { i } , } & { \nu _ { 3 } } \end{array} \right| , } & { \quad \boldsymbol { C } _ { i } = \left| \begin{array} { c c c } { \lambda _ { 1 } , } & { \lambda _ { 2 } , } & { \boldsymbol { X } _ { i } } \\ { \mu _ { 1 } , } & { \mu _ { 2 } , } & { \boldsymbol { Y } _ { i } } \\ { \nu _ { 1 } , } & { \nu _ { 2 } , } & { \boldsymbol { Z } _ { i } } \end{array} \right| . } \end{array} \right.
$$

In order to complete the discussion the coefficients of the determinants in the right members of these equations must be developed, as they were in (86);and since $\Delta _ { 2 }$ is of the third order,terms of the right member of the third order must be retained even in the first approximation. When applied to the second of (131),this leads to an equation of the form of the frst of (44). The details of this and the completion of the solution of equations (13o) will be called out in the questions which follow Art.142.

142.Formulas for Computing an Approximate Orbit. For convenience in use the formulas for the computation of an approxi-

mate orbit are collected here in the order in which they are used.   
The numbers attached are those occurring in the text.

Preparation of the data. The observed right ascensions and declinations, $\pmb { \alpha _ { 0 } }$ and $\delta _ { 0 }$ ，are corrected for precession，aberration, etc., by

$$
\left\{ \begin{array} { l } { \alpha = \alpha _ { 0 } - 1 5 f - g \sin { \left( G + \alpha _ { 0 } \right) } \tan { \delta _ { 0 } } - h \sin { \left( H + \alpha _ { 0 } \right) } \sec { \delta _ { 0 } } , } \\ { \delta = \delta _ { 0 } - i \cos { \delta _ { 0 } } - g \cos { \left( G + \alpha _ { 0 } \right) } - h \cos { \left( H + \alpha _ { 0 } \right) } \sin { \delta _ { 0 } } . } \end{array} \right.
$$

The direction cosines are given by

$$
\begin{array} { r l } & { \int ^ { \lambda _ { j } } = \cos \delta _ { j } \cos \alpha _ { j } , \qquad ( j = 1 , 2 , 3 ) , } \\ & { \left\{ \mu _ { j } = \cos \delta _ { j } \sin \alpha _ { j } , \right. } \\ & { \left. \nu _ { j } = \sin \delta _ { j } . \right. } \end{array}
$$

The Method of Laplace. Take $t _ { 0 } = t _ { 2 }$ unless the intervals between the successive observations are very unequal，when $\begin{array} { r } { t _ { 0 } = \frac { 1 } { 3 } ( t _ { 1 } + t _ { 2 } + t _ { 3 } ) } \end{array}$ .It will be supposed that $t _ { 0 } = t _ { 2 }$ Suppose $\boldsymbol { \cal X }$ $\pmb { Y }$ ，and $\mathbf { z }$ are tabulated in the Ephemeris for $t _ { a } , ~ t _ { b } , ~ t _ { c }$ where $t _ { b }$ is near $\scriptstyle t _ { 0 }$ ，Then compute $X , ~ Y ~ .$ and $\mathbf { z }$ at $t _ { 0 }$ from formulas of the type\*

$$
\begin{array} { c } { { X = \displaystyle \frac { ( t _ { 0 } - t _ { b } ) ( t _ { 0 } - t _ { c } ) } { ( t _ { a } - t _ { b } ) ( t _ { a } - t _ { c } ) } X _ { a } + \displaystyle \frac { ( t _ { 0 } - t _ { a } ) ( t _ { 0 } - t _ { c } ) } { ( t _ { b } - t _ { a } ) ( t _ { b } - t _ { c } ) } X _ { b } } } \\ { { + \displaystyle \frac { ( t _ { 0 } - t _ { a } ) ( t _ { 0 } - t _ { b } ) } { ( t _ { c } - t _ { a } ) ( t _ { c } - t _ { b } ) } X _ { c } . } } \end{array}
$$

$$
k ( t _ { j } - t _ { 2 } ) = \tau _ { j } , ~ ( j = 1 , 2 , 3 ; \tau _ { 2 } = 0 ) .
$$

$$
P = - \tau _ { 1 } \tau _ { 3 } ( \tau _ { 3 } - \tau _ { 1 } ) .
$$

$$
D = \frac { 2 } { P } \left| { \begin{array} { c c c } { \lambda _ { 1 } , } & { \lambda _ { 2 } . } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { \mu _ { 2 } , } & { \mu _ { 3 } } \\ { \nu _ { 1 } , } & { \nu _ { 2 } , } & { \nu _ { 3 } } \end{array} } \right| .
$$

$$
D _ { 1 } = \mathrm { - } \left. \frac { { \tau _ { 3 } } ^ { 2 } } { P } \right| \mu _ { 1 } , \mu _ { 2 } , \quad Y  \\  \nu _ { 1 } , \nu _ { 2 } , Z \left| \left. - \frac { { \tau _ { 1 } } ^ { 2 } } { P } \right| \mu _ { 2 } , \mu _ { 3 } , \zeta \right| .
$$

$$
D _ { 2 } = + \frac { 2 \tau _ { 3 } } { P } \left| \begin{array} { l l l } { \lambda _ { 1 } , } & { \lambda _ { 2 } , } & { X } \\ { \mu _ { 1 } , } & { \mu _ { 2 } , } & { Y } \\ { \nu _ { 1 } , } & { \nu _ { 2 } , } & { Z } \end{array} \right| + \frac { 2 \tau _ { 1 } } { P } \left| \begin{array} { l l l } { \lambda _ { 2 } , } & { \lambda _ { 3 } , } & { X } \\ { \mu _ { 2 } , } & { \mu _ { 3 } , } & { Y } \\ { \nu _ { 2 } , } & { \nu _ { 3 } , } & { Z } \end{array} \right| .
$$

\*These equations are very simple because $t _ { a } , ~ t _ { b } ,$ and $t _ { c }$ differ by intervals of one day,but there are other methods of interpolation which are even simpler.

$$
R \cos \psi = X \lambda + Y \mu + Z \nu , ( 0 < \psi \leq \pi ) .
$$

$$
\begin{array} { r } { \left\{ { \begin{array} { c } { N \sin m = R \sin \psi , } \\ { \rule { 0 ex } { 5 ex } } \\ { N \cos m = R \cos \psi - \displaystyle \frac { D _ { 1 } } { D R ^ { 3 } } , } \\ { M = - \displaystyle \frac { N D R ^ { 3 } } { D _ { 1 } } \sin ^ { 3 } \psi > 0 . } \end{array} } \right. } \end{array}
$$

$$
\sin ^ { 4 } \varphi = M \sin { ( \varphi + m ) } .
$$

$$
\pmb { r } = R \frac { \sin \psi } { \sin \varphi } , \qquad \rho = R \frac { \sin \left( \psi + \varphi \right) } { \sin \varphi } .
$$

$$
\rho ^ { \prime } = \frac { D _ { 2 } } { 2 D } \left[ \frac { 1 } { R ^ { 3 } } - \frac { 1 } { r ^ { 3 } } \right] .
$$

$$
\pmb { x } = \rho \lambda - \pmb { X } , \pmb { y } = \rho \mu - \pmb { Y } , \ z = \rho \nu - \pmb { Z }
$$

Compute $\lambda ^ { \prime } , \mu ^ { \prime } ,$ $\nu ^ { \prime }$ from equations of the type

$$
\begin{array} { c } { { \lambda ^ { \prime } = \displaystyle \frac { - { \bf \rho } ( \tau _ { 2 } + \tau _ { 3 } ) \lambda _ { 1 } } { ( \tau _ { 1 } - \tau _ { 2 } ) ( \tau _ { 1 } - \tau _ { 3 } ) } - \frac { ( \tau _ { 3 } + \tau _ { 1 } ) \lambda _ { 2 } } { ( \tau _ { 2 } - \tau _ { 3 } ) ( \tau _ { 2 } - \tau _ { 1 } ) } } } \\ { { - \frac { ( \tau _ { 1 } + \tau _ { 2 } ) \lambda _ { 3 } } { ( \tau _ { 3 } - \tau _ { 1 } ) ( \tau _ { 3 } - \tau _ { 2 } ) } . } } \end{array}
$$

Compute $X ^ { \prime } , Y ^ { \prime }$ and $Z ^ { \prime }$ from equations of the type

$$
\begin{array} { c } { { k X ^ { \prime } = { \displaystyle \frac { 2 t _ { 2 } - ( t _ { b } + t _ { c } ) } { ( t _ { a } - t _ { b } ) ( t _ { a } - t _ { c } ) } } X _ { a } + { \displaystyle \frac { 2 t _ { 2 } - ( t _ { c } + t _ { a } ) } { ( t _ { b } - t _ { a } ) ( t _ { b } - t _ { c } ) } } X _ { b } } } \\ { { + { \displaystyle \frac { 2 t _ { 2 } - ( t _ { a } + t _ { b } ) } { ( t _ { c } - t _ { a } ) ( t _ { c } - t _ { b } ) } } X _ { c } . } } \end{array}
$$

$$
\left\{ \begin{array} { l l } { x ^ { \prime } = \rho ^ { \prime } \lambda + \rho \lambda ^ { \prime } - X ^ { \prime } , } \\ { y ^ { \prime } = \rho ^ { \prime } \mu + \rho \mu ^ { \prime } - Y ^ { \prime } , } \\ { z ^ { \prime } = \rho ^ { \prime } \nu + \rho \nu ^ { \prime } - Z ^ { \prime } . } \end{array} \right.
$$

At this point the correction for the time aberration may be made by equations (70)，and the approximate values of $x , \ y , \ z ,$ $\boldsymbol { x } ^ { \prime } , \boldsymbol { y } ^ { \prime }$ and $z ^ { \prime }$ may be improved by the methods of Arts.128 and 129;or, the elements may be computed at once from the formulas given in chap.v. The formulas for the determination of the elements will be given and the rumbers of the equations refer to chap.v

The integrals of areas in the equator system are

$$
\left\{ \begin{array} { l l } { x y ^ { \prime } - y x ^ { \prime } = b _ { 1 } , } \\ { y z ^ { \prime } - z y ^ { \prime } = b _ { 2 } , } \\ { z x ^ { \prime } - x z ^ { \prime } = b _ { 3 } . } \end{array} \right.
$$

f $\epsilon$ represents the obliquity of the ecliptic, the corresponding constants in the ecliptic system are

$$
\left\{ \begin{array} { l l } { a _ { 1 } = b _ { 1 } \cos \epsilon - b _ { 3 } \sin \epsilon , } \\ { a _ { 2 } = b _ { 2 } , } \\ { a _ { 3 } = b _ { 1 } \sin \epsilon + b _ { 3 } \cos \epsilon , } \end{array} \right.
$$

and $\mathbf { \chi } _ { i } ^ { \phantom { \dagger } }$ and $\otimes$ are defined by (chap. v.)

$$
\left\{ \begin{array} { l l l l l l l l l } { a _ { 1 } = } & { \sqrt { { a _ { 1 } } ^ { 2 } + { a _ { 2 } } ^ { 2 } + { a _ { 3 } } ^ { 2 } } \cos i , } & & & { } \\ { a _ { 2 } = \pm } & { \sqrt { { a _ { 1 } } ^ { 2 } + { a _ { 2 } } ^ { 2 } + { a _ { 3 } } ^ { 2 } } \sin i \sin \Omega , } & & { } \\ { a _ { 3 } = \mp } & { \sqrt { { a _ { 1 } } ^ { 2 } + { a _ { 2 } } ^ { 2 } + { a _ { 3 } } ^ { 2 } } \sin i \cos \Omega . } & & { } \end{array} \right.
$$

The major axis and parameter are defined by

$$
x ^ { \prime } { } ^ { 2 } + y ^ { \prime } { } ^ { 2 } + z ^ { \prime } { } ^ { 2 } = k ^ { 2 } \left( { \frac { 2 } { r } } - { \frac { 1 } { a } } \right) ,
$$

$$
k ^ { 2 } p = k ^ { 2 } a ( 1 - e ^ { 2 } ) = a _ { 1 } { } ^ { 2 } + a _ { 2 } { } ^ { 2 } + a _ { 1 } { } ^ { 2 } .
$$

It follows from Fig.37,p.237, that

$$
\left\{ \begin{array} { l } { \sin i \sin u = \sin \displaystyle \dot { b } = \frac { z } { r } , } \\ { \cos i \sin u = \cos b \sin ( { l - \delta } ) = \frac { y } { r } \mathrm { c o s } \otimes - \frac { x } { r } \mathrm { s i n } \otimes , } \\ { \cos u = \cos b \cos ( { l - \delta } ) = \frac { y } { r } \mathrm { s i n } \otimes + \frac { x } { r } \mathrm { c o s } \otimes , } \end{array} \right.
$$

which define $\textbf { \em u }$ The angle $\pmb { \upsilon }$ is given by

$$
r = { \frac { p } { 1 + e \cos \vartheta } } .
$$

and

$$
\omega = u - v .
$$

If the orbit is a parabola, $\pmb { T }$ is defined by

$$
k ( t - T ) = { \textstyle { \frac { 1 } { 2 } } } p ^ { \frac { 3 } { 4 } } \left[ \tan { \frac { v } { 2 } } + { \frac { 1 } { 3 } } \tan ^ { 3 } { \frac { v } { 2 } } \right] .
$$

If the orbit is an ellipse, $E , n _ { \colon }$ and $\pmb { T }$ are defined by

$$
\tan { \frac { E } { 2 } } = { \sqrt { \frac { 1 - e } { 1 + e } } } \tan { \frac { v } { 2 } } ,
$$

$$
n = { \frac { k } { a ^ { \frac { 3 } { 2 } } } } ,
$$

$$
\boldsymbol { n } ( t - T ) = E - e \sin \theta .
$$

The corresponding equations for hyperbolic orbits are

$$
\begin{array} { c } { { a + r = a e \cosh F , } } \\ { { { } } } \\ { { n ( t - T ) = - F + e \sinh F . } } \end{array}
$$

The Method of Gauss. The observed data are corrected by (4) and the direction cosines are given by (6). The coordinates of the sun at $t _ { 1 } , t _ { 2 } ,$ and $\mathbf { { \boldsymbol { t } } _ { 3 } }$ can be computed from equations of the type

$$
\begin{array} { c } { { X _ { i } = \displaystyle \frac { ( t _ { i } - t _ { b } ) ( t _ { i } - t _ { c } ) } { ( t _ { a } - t _ { b } ) ( t _ { a } - t _ { c } ) } X _ { a } + \displaystyle \frac { ( t _ { i } - t _ { a } ) ( t _ { i } - t _ { c } ) } { ( t _ { b } - t _ { a } ) ( t _ { b } - t _ { c } ) } X _ { b } } } \\ { { + \displaystyle \frac { ( t _ { i } - t _ { a } ) ( t _ { i } - t _ { b } ) } { ( t _ { c } - t _ { a } ) ( t _ { c } - t _ { b } ) } X _ { c } } } \end{array}
$$

where $X _ { a } , X _ { b } , X _ { c }$ are taken from the Ephemeris and $\mathbf { \Delta } _ { t _ { b } }$ is the time nearest to $t _ { i }$ for which $\pmb { X }$ is given.Then

$$
\Delta _ { 2 } = { \left| \begin{array} { l l l } { \lambda _ { 1 } , } & { \lambda _ { 2 } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { \mu _ { 2 } , } & { \mu _ { 3 } } \\ { \nu _ { 1 } , } & { \nu _ { 2 } , } & { \nu _ { 3 } } \end{array} \right| } ,
$$

$$
\left\{ \begin{array} { r l } { \boldsymbol { K } \ = \ - \ \frac { 1 } { 2 } \left| \boldsymbol { \lambda } _ { 1 } , \quad \boldsymbol { X } _ { 1 } + \boldsymbol { X } _ { 3 } - 2 \boldsymbol { X } _ { 2 } , \quad \lambda _ { 3 } \right| , } & { } \\ { \boldsymbol { K } \ = \ - \ \frac { 1 } { 2 } \left| \boldsymbol { \mu } _ { 1 } , \quad \boldsymbol { Y } _ { 1 } + \ \boldsymbol { Y } _ { 3 } - 2 \boldsymbol { Y } _ { 2 } , \quad \mu _ { 3 } \right| , } & { } \\ { \boldsymbol { \nu } _ { 1 } , \quad \boldsymbol { Z } _ { 1 } + \ \boldsymbol { Z } _ { 3 } - 2 \boldsymbol { Z } _ { 2 } , \quad \boldsymbol { \nu } _ { 3 } \ } & { } \\ { } & { } \\ { \boldsymbol { K } _ { 1 } \ = \ - \ \ \left| \boldsymbol { \mu } _ { 1 } , \quad \boldsymbol { X } _ { 1 } + \boldsymbol { X } _ { 3 } , \quad \lambda _ { 3 } \right| } & { } \\ { \boldsymbol { K } _ { 1 } \ = \ - \ \left| \boldsymbol { \mu } _ { 1 } , \quad \boldsymbol { Y } _ { 1 } + \boldsymbol { Y } _ { 3 } , \quad \boldsymbol { \mu } _ { 3 } \right| . } & { } \\ { \boldsymbol { \nu } _ { 1 } , \quad \boldsymbol { Z } _ { 1 } + \ \boldsymbol { Z } _ { 3 } , \quad \boldsymbol { \nu } _ { 3 } } \end{array} \right.
$$

On neglecting the last term of (87),which is very small,and comparing the result with the first of (44),it is seen that the explicit formulas for determining $\pmb { r _ { 2 } }$ and $\pmb { \rho _ { 2 } }$ are

$$
R _ { 2 } \cos \psi _ { 2 } = X _ { 2 } \lambda _ { 2 } + Y _ { 2 } \mu _ { 2 } + Z _ { 2 } \nu _ { 2 } , ( 0 < \psi _ { 2 } \leq \pi ) ,
$$

$$
\left\{ \begin{array} { l } { { N \sin m = R _ { 2 } \sin \psi _ { 2 } , } } \\ { { \quad } } \\ { { N \cos m = R _ { 2 } \cos \psi _ { 2 } - \displaystyle \frac { K } { \Delta _ { 2 } } , } } \\ { { \quad \quad \quad \quad M = \displaystyle \frac { 4 \Delta _ { 2 } R ^ { 3 } \sin ^ { 3 } \psi } { K _ { 1 } } > 0 . } } \end{array} \right.
$$

$$
\sin ^ { 4 } \varphi = M \sin { ( \varphi + m ) } .
$$

$$
\left\{ \begin{array} { l l } { r _ { 2 } = \displaystyle \frac { R _ { 2 } \sin \psi _ { 2 } } { \sin \varphi } , } \\ { \rho _ { 2 } = R _ { 2 } \displaystyle \frac { \sin ( \psi _ { 2 } + \varphi ) } { \sin \varphi } . } \end{array} \right.
$$

Then $\pmb { \rho _ { 1 } }$ and $\pmb { \rho _ { 3 } }$ are given by

$$
\{ \begin{array} { l l } { \displaystyle | \begin{array} { l l } { \lambda _ { 1 } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { \mu _ { 3 } } \end{array} | \rho _ { 1 } = | \begin{array} { l l } { X _ { 1 } , } & { \lambda _ { 3 } } \\ { Y _ { 1 } , } & { \mu _ { 3 } } \end{array} | - \frac { [ 1 , 3 ] } { [ 2 , 3 ] } \bigg | \begin{array} { l l } { X _ { 2 } , } & { \lambda _ { 3 } } \\ { Y _ { 2 } , } & { \mu _ { 3 } } \end{array} | } \\ & { \qquad \quad + \frac { [ 1 , 2 ] } { [ 2 , 3 ] } \bigg | \begin{array} { l l } { X _ { 3 } , } & { \lambda _ { 3 } } \\ { Y _ { 3 } , } & { \mu _ { 3 } } \end{array} | + \rho _ { 2 } \frac { [ 1 , 3 ] } { [ 2 , 3 ] } \bigg | \begin{array} { l l } { \lambda _ { 2 } , } & { \lambda _ { 3 } } \\ { \mu _ { 2 } , } & { \mu _ { 3 } } \end{array} \bigg | \colon } \\ { \displaystyle | \begin{array} { l l } { \lambda _ { 1 } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { \mu _ { 3 } } \end{array} | \rho _ { 3 } = \frac { [ 2 , 3 ] } { [ 1 , 2 ] } \bigg | \begin{array} { l l } { \lambda _ { 1 } , } & { X _ { 1 } } \\ { \mu _ { 1 } , } & { Y _ { 1 } } \end{array} | - \frac { [ 1 , 3 ] } { [ 1 , 2 ] } \bigg | \begin{array} { l l } { \lambda _ { 1 } , } & { X _ { 2 } } \\ { \mu _ { 1 } , } & { Y _ { 2 } } \end{array} | } \\ & { \qquad \quad + \bigg | \begin{array} { l l } { \lambda _ { 1 } , } & { X _ { 3 } } \\ { \mu _ { 1 } , } & { Y _ { 3 } } \end{array} | + \rho _ { 2 } \frac { [ 1 , 3 ] } { [ 2 , 3 ] } \bigg | \begin{array} { l l } { \lambda _ { 1 } , } & { \lambda _ { 2 } } \\ { \mu _ { 3 } , } & { \mu _ { 2 } } \end{array} | , } \end{array} 
$$

(or by formulas obtained from these by cyclical permutation of the letters $\lambda , \mu , \nu$ and $X , ~ Y , ~ \mathbf { Z } )$ ，where

and

$$
2 \tau = \tau _ { 3 } - \tau _ { 1 } , ~ 2 \epsilon = \tau _ { 3 } + \tau _ { 1 } ,
$$

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { [ 1 , 3 ] } { [ 2 , 3 ] } = \frac { 1 } { \frac { 1 } { 2 } + \frac { \epsilon ^ { 2 } } { 2 \tau ^ { 2 } } + \frac { \epsilon ^ { 3 } } { 2 \tau ^ { 2 } } } , } \\ { \displaystyle \frac { [ 1 , 2 ] } { [ 2 , 3 ] } = 1 - \frac { \epsilon ^ { 2 } + \frac { \epsilon ^ { 2 } } { 2 \tau ^ { 2 } } } { 1 + \frac { \epsilon ^ { 2 } } { \tau ^ { 2 } } + \frac { \epsilon ^ { 3 } } { 2 \tau ^ { 2 } } } , } \\ { \displaystyle \frac { [ 1 , 3 ] } { [ 2 , 3 ] } = \frac { 1 + \frac { \epsilon ^ { 2 } } { 2 \tau ^ { 2 } } + \frac { \epsilon ^ { 3 } } { 2 \tau ^ { 2 } } } { 1 + \frac { \epsilon ^ { 2 } } { \tau ^ { 2 } } + \frac { \epsilon ^ { 3 } } { 2 \tau ^ { 2 } } } , } \\ { \displaystyle \frac { [ 2 , 3 ] } { [ 1 , 2 ] } = \frac { 1 + \frac { \epsilon ^ { 2 } } { \tau ^ { 2 } } + \frac { \epsilon ^ { 3 } } { 2 \tau ^ { 3 } } } { 1 - \frac { \epsilon ^ { 2 } } { \tau ^ { 2 } } + \frac { 2 \tau ^ { 3 } } { 2 \tau ^ { 3 } } } , } \\ { \displaystyle \frac { [ 1 , 3 ] } { [ 1 , 2 ] } = \frac { 1 } { \frac { 1 } { 2 } - \frac { \epsilon ^ { 2 } } { 2 \tau ^ { 2 } } + \frac { \epsilon ^ { 3 } } { 4 \tau ^ { 2 } } } . } \end{array} \right.
$$

$$
\left\{ \begin{array} { l l } { x _ { i } = \rho _ { i } \lambda _ { i } - X _ { i } , } & { ( j = 1 , 2 , 3 ) , } \\ { y _ { i } = \rho _ { i } \mu _ { i } - Y _ { i } , } & \\ { z _ { i } = \rho _ { j } \nu _ { j } - Z _ { i } . } & \end{array} \right.
$$

At this point the correction for the time aberration may be made; the first two derivatives of $r _ { 2 } ^ { 2 }$ may be computed from the values $r _ { 1 } { } ^ { 2 } , \ r _ { 2 } { } ^ { 2 }$ and $r _ { 3 } { } ^ { 2 }$ by applying the formulas (32) to this case; $p$ and $q$ may be computed from (74) and more approximate values of $P$ and $Q$ may be determined from (86)；and then the computation may be repeated beginning with equations (46); or,the method of Gauss of Art.134 may be used to improve the accuracy of the expressions for the ratios of the triangles;or, the elements may be computed without further approximation of the intermediate quantities. The formulas for the computation of the elements will be given. Let the rectangular coordinates in the ecliptic system be $\bar { x } _ { i } , \bar { y } _ { i } , \bar { z } _ { i } ,$ and the obliquity of the ecliptic $\epsilon _ { \bullet }$ which will not be confused with the é defined in (85). Then

$$
\left\{ \begin{array} { l l } { \bar { x } _ { j } = x _ { i } , ( j = 1 , 2 , 3 ) , } \\ { \bar { y } _ { j } = + y _ { i } \cos \epsilon + z _ { i } \sin \epsilon , } \\ { \bar { z } _ { j } = - y _ { j } \sin \epsilon + z _ { j } \cos \epsilon . } \end{array} \right.
$$

$$
\left\{ \begin{array} { l l } { A { \bar { x } } _ { 1 } + B { \bar { y } } _ { 1 } + C { \bar { z } } _ { 1 } = 0 , } \\ { A { \bar { x } } _ { 2 } + B { \bar { y } } _ { 2 } + C { \bar { z } } _ { 2 } = 0 , } \\ { A { \bar { x } } _ { 3 } + B { \bar { y } } _ { 3 } + C { \bar { z } } _ { 3 } = 0 , } \end{array} \right.
$$

from which

$$
\stackrel { \scriptscriptstyle \mathrm { L } } { A } : B : C = \left| \begin{array} { l l } { \bar { y } _ { 1 } , } & { \bar { z } _ { 1 } } \\ { \bar { y } _ { 2 } , } & { \bar { z } _ { 2 } } \end{array} \right| : \left| \begin{array} { l l } { \bar { z } _ { 1 } , } & { \bar { x } _ { 1 } } \\ { \bar { z } _ { 2 } , } & { \bar { x } _ { 2 } } \end{array} \right| : \left| \begin{array} { l l } { \bar { x } _ { 1 } , } & { \bar { y } _ { 1 } } \\ { \bar { x } _ { 2 } , } & { \bar { y } _ { 2 } } \end{array} \right| .
$$

Then，from equations corresponding to (11)，(14)，and (15) of chap. v.,

$$
\left\{ \begin{array} { c } { \cos i = \frac { A } { \sqrt { A ^ { 2 } + B ^ { 2 } + C ^ { 2 } } } , } \\ { { } } \\ { { \sin \ \otimes \sin i \ = \frac { \pm B } { \sqrt { A ^ { 2 } + B ^ { 2 } + C ^ { 2 } } } } , } \\ { { } } \\ { { \cos \ \otimes \sin i \ = \frac { \mp C } { \sqrt { A ^ { 2 } + B ^ { 2 } + C ^ { 2 } } } , } } \end{array} \right.
$$

which define $\ d \Omega$ and $\scriptstyle i .$

It follows from Fig.37 that the arguments of the latitude are defined by

$$
\left\{ \begin{array} { l l } { \sin i \sin u _ { i } = \displaystyle \frac { \bar { z } _ { j } } { r _ { i } } , \qquad ( j = 1 , \ 2 , \ 3 ) , } \\ { \cos i \sin u _ { i } = \displaystyle \frac { \bar { y } _ { j } } { r _ { i } } \cos \ \otimes - \displaystyle \frac { \bar { x } _ { j } } { r _ { i } } \sin \ \otimes , } \\ { \cos u _ { i } = \displaystyle \frac { \bar { y } _ { j } } { r _ { i } } \sin \ \otimes + \displaystyle \frac { \bar { x } _ { j } } { r _ { j } } \cos \ \otimes . } \end{array} \right.
$$

$$
\sigma _ { 1 } = u _ { 3 } - u _ { 2 } , \qquad \sigma _ { 2 } = u _ { 3 } - u _ { 1 } , \qquad \sigma _ { 3 } = u _ { 2 } - u _ { 1 } .
$$

$$
\begin{array} { r } { k \sqrt { p } ( t _ { 3 } - t _ { 1 } ) = \frac { { r _ { 2 } } ^ { 2 } { \sigma _ { 2 } } ^ { 3 } } { 6 \sigma _ { 1 } \sigma _ { 3 } } + \frac { { r _ { 1 } } ^ { 2 } \sigma _ { 2 } ( 2 \sigma _ { 3 } - \sigma _ { 1 } ) } { 6 \sigma _ { 3 } } + \frac { { r _ { 3 } } ^ { 2 } \sigma _ { 2 } ( 2 \sigma _ { 1 } - \sigma _ { 3 } ) } { 6 \sigma _ { 1 } } , } \end{array}
$$

defines $p$

$$
\left\{ \begin{array} { l l } { e \sin \left( u _ { 1 } - \omega \right) = \frac { r _ { 3 } ( p - r _ { 1 } ) \cos \sigma _ { 2 } - r _ { 1 } ( p - r _ { 3 } ) } { r _ { 1 } r _ { 3 } \sin \sigma _ { 2 } } , } \\ { e \cos \left( u _ { 1 } - \omega \right) = \frac { p - r _ { 1 } } { r _ { 1 } } } \end{array} \right.
$$

define e and $\omega$ Hence $^ { a }$ can be determined from $p$ and $e$

Since $v _ { j } = u _ { j } - \omega \ ( j = 1 , \ : 2 , \ : 3 )$ , the time of perihelion passage is determined precisely as in the method of Laplace by equations (of chap.v.） (32)，[(50),(30),(42)],[(73)，(74)] in the parabolic, elliptic,and hyperbolic cases respectively.

# XVII. PROBLEMS.

1.Take three observations of an asteroid not separated from one another by more than 15 days,or three of a comet not separated from one another by more than 6 days,and compute the elements of the orbit by both the method of Laplace and also that of Gauss.

2. Prove that the apparent motion of $c$ cannot be permanently along & great circle unless it moves in the plane of the ecliptic.

3.Apply formulas (31） and (32) ona definite closed function,as for example $x = \sin t$

4.By means of the equation

$$
r ^ { 2 } = R ^ { 2 } + \rho ^ { 2 } - 2 R r \cos \psi
$$

eliminate $\pmb { \rho }$ from the first equation of (44) and discuss the result by the methods of the Theory of Algebraic Equations,and show that the solutions agree qualitatively with those obtained in Art.119.

5.Discuss the determinants $_ { D }$ ， $D _ { 1 }$ ,and $D _ { 2 }$ when there are four observations.

6.Express $\Delta _ { 2 }$ when there are three observations in terms of the $\pmb { \alpha _ { i } }$ and the ${ \pmb \delta } _ { \pmb { i } }$ in sucha manner that the fact it is of the third order will be explicitly exhibited.

7.Develop the explicit formulas,using the $\lambda _ { i } , \mu _ { i } ,$ and ${ \pmb { \nu } } _ { \pmb { \imath } }$ and the determinant notation,for the differential corrections of the method of Harzer and Leuschner.

8.Give a geometrical interpretation of the vanishing of the coeffcients of ${ \pmb \rho } _ { 1 }$ and $\pmb { \rho _ { 3 } }$ in equations (89).

9.Suppose three positions of $c$ are known as in Art.139.Show $( a )$ that the three equations

$$
{ r } _ { i } = \frac { p } { 1 + e \cos \left( u _ { i } - \omega \right) } , \qquad ( i = 1 , 2 , 3 ) ,
$$

define $p , e _ { \mathrm { i } }$ ，and ω without using the intervals of time in which the arcs are described; $( b )$ write out the explicit formulas for computing $\textit { \textbf { p } } , \textit { \textbf { e } } ,$ and $\omega ;$ $( c )$ compare their length with that of (119) and (122);and $( d )$ show that $p$ is not well determined as it depends upon ratios of small quantities of the third order.

10. Suppose $f _ { 2 } = 1$ ， $g _ { 2 } = 0$ and regard (130)as linear equations in $\rho _ { 1 } , \rho _ { 2 } , \rho _ { 3 } ,$ $x _ { 0 } , x _ { 0 } ^ { \prime } , y _ { 0 } , y _ { 0 } ^ { \prime } , z _ { 0 } , z _ { 0 } ^ { \prime }$ .Show that the determinant of the coefficients is

$$
\Delta = - g _ { 1 } g _ { 3 } ( f _ { 1 } g _ { 3 } - f _ { 3 } g _ { 1 } ) \left| { \begin{array} { l l l } { \lambda _ { 1 } , } & { \lambda _ { 2 } , } & { \lambda _ { 3 } } \\ { \mu _ { 1 } , } & { \mu _ { 2 } , } & { \mu _ { 3 } } \\ { \nu _ { 1 } , } & { \nu _ { 2 } , } & { \nu _ { 3 } } \end{array} } \right| .
$$

11.Show that on using the expansions of equations (S6) the second equation of (131) becomes (87).

12.Having found $\pmb { \rho _ { 2 } }$ from the equation corresponding to (87),and ${ \pmb \rho } _ { 1 }$ and $\pmb { \rho _ { 3 } }$ from (131),show that $x _ { 0 } , x _ { 0 } ^ { \prime } , y _ { 0 } , y _ { 0 } ^ { \prime } , z _ { 0 } , z _ { 0 } ^ { \prime }$ can be determined from equations (130). (Then the elements can be determined as in the Laplacian Method.)

# HISTORICAL SKETCH AND BIBLIOGRAPHY.

The first method of finding the orbit of a body (comet moving in a parabola）from three observations was devised by Newton，and is given in the Principia,Book II1.,Prop.xLI. The solution depends upon a graphical construction,which,by successive approximations,leads to the elements.One of the earliest applications of the method was by Halley to the comet which has since borne his name. Newton seems to have had trouble with the problem of determining orbits,for he said,“This being a problem of very great difficulty,I tried many methodg of resolving it.”Newton's success in basing his discussion on the fundamental elements of the problem was fully explained by Laplace in his memoir on the subject.

The first complete solution which did not depend upon & graphical construction was given by Euler in 1744 in his Theoria Motuum Planetarum et Cometarum. Some important advances were made by Lambert in 1761. Up to this time the methods were for the most part based upon one or the other of two assumptions,which are only approximately true,viz.,that in the interval $t _ { 3 } - t _ { 1 }$ the observed body describes a straight line with uniform speed,or that the radius at the time of the second observation divides the chord joining the end positions into segments which are proportional to the intervals betw(en the observations.In attempting to improve on the second of these assumptions Lambert made the discovery of the relation among the radii,chord, time-interval,and major axis mentioned in Art.92.He later made the determination depend upon the curvature of the apparent orbit, which iscloselyrelated to thedeterminant $\Delta _ { 2 }$ ,andin this direction approached the best modern methods. He had an unusual grasp of the physics and geometry of the problem，and really anticipated many of the ideas which were carried out by his successors in better and more convenient ways.

Lagrange wrote three memoirs on the theory of orbits,two in 1778 and one in 1783．They are printed together in his collected works,vol.Iv.,pp.439- 532.As one would expect，with Lagrange came generality，precision，and mathematical elegance. He determined the geocentric distance of $c$ at the time of the second observation by an equation of the eighth degree,which is nothing else than (87) with $\boldsymbol { r _ { 2 } }$ eliminated by means of the equation which expresses the fact that S, $\pmb { \cal E }$ and $c$ forma triangle at $t _ { 2 }$ ，He developed the expressions for the heliocentric coordinates as power series in the time-intervals {eqs.(73)l,and laid the foundation for the development of expressions for intermediate elements in power series. These developments have been completed and put in form for numerical applications by Charlier,Meddelande frän Lunds Astronomiska Observatorium，No.46. The original work of Lagrange was not put in a form adapted to the needs of the computer,and has not been used in practice.

In 1780 Laplace published an entirely new method in Mémoires de l'Academie Royale des Sciences de Paris (Collected Works,vol.x.,pp.93-146).This method,the fundamental ideas of which have been given in this chapter,has been the basis fora great deal of later work. Among the developments in this line may be mentioned a memoir by Villarceau (Annales de t'Observatoire de Paris,vol.I.),the work of Harzer (Astronomische Nachrichten,vol. 141),and its simplification by Leuschner (Publications of the Lick Observatory,vol.vi1.,Part 1.).The approximations beyond the first are not conveniently carried out in the original method of Laplace,but the method of differential corrections devised by Harzer and simplified by Leuschner has proved very satisfactory in practice.

Olbers published his classical Abhandlung iber die leichteste und bequemste Methode,die Bahn eines Kometen zu berechnen,in 1797.This method has not been surpassed for computing parabolic orbits and is in very general use even at the present time.It is given in nearly every treatise on the theory of determining orbits.

The discovery of Ceres in 1801 and its loss after having been observed only a short time drew the attention of a brilliant young German mathematician, Gauss,to the problem of determining the elements of the orbit of a heavenly body from observations made from the earth. The problem was quickly solved,and an application of the method led to the recovery of Ceres. Gauss elaborated and perfected his work,and in 18o9 brought it out in his Theoria Motus Corporum Coelestium. This work, written by a man at once a master of mathematics and highly skilled as a computer,is so filled with valuable ideas and is so exhaustive that it remains a classic treatise on the subject to this day.The later treatises allare under the greatest obligations to the work of Gauss.

In the Memoirs of the National Academy of Science,vol.Iv.(1888),Gibbs published a method of considerable originality in which the first approximation to theratios of the triangles was obtained more exactly by including all thre geocentric distances as unknown from the beginning. The method is also distinguished by the fact that it was developed by the calculus of vector analysis.

The works to be consulted are:

The Theoria Motus of Gauss.

Watson's Theoretical Astronomy (now out of print).

Oppolzer's Bahnbestimmung,an exhaustive treatise.

Tisserand's Lecons sur la Determination des Orbites,written in the characteristically clear French style.

Bauschinger's Bahnbestimmung,a recent book of great excellence by one of the best authorities on the subject of the theory of orbits.

Klinkerfues’ Theoretische Astronomie (third edition by Buchholz),an excellent work and the most exhaustive one yet issued.

# CHAPTER VII.

# THE GENERAL INTEGRALS OF THE PROBLEM OF $\mathscr { n }$ BODIES.

143.The Differential Equations of Motion. Suppose the bodies are homogeneous in spherical layers; then they will attract each other as though their masses were at their centers. Let $m _ { 1 }$ ， $m _ { 2 } , \ldots , m _ { n }$ represent their masses. Let the coordinates of $m _ { \mathrm { i } }$ referred to a fixed system of axes be $x _ { i } , y _ { i } , z _ { i } ( i = 1 , \cdots , n )$ .Let ${ r } _ { i , j }$ represent the distance between the centers of $m _ { i }$ and $m _ { \hat { \imath } } .$ Let $k ^ { 2 }$ represent a constant depending upon the units employed. Then the components of force on $m _ { 1 }$ parallel to the $\pmb { x } \cdot$ -axis are

$$
- \frac { k ^ { 2 } m _ { 1 } m _ { 2 } } { r ^ { 2 } _ { 1 , ~ 2 } } \cdot \frac { ( x _ { 1 } - x _ { 2 } ) } { r _ { 1 , ~ 2 } } , \qquad \dots , \qquad - \frac { k ^ { 2 } m _ { 1 } m _ { n } } { r ^ { 2 } _ { 1 , ~ n } } \cdot \frac { ( x _ { 1 } - x _ { n } ) } { r _ { 1 , ~ n } } ,
$$

and the total force is their sum. Therefore

$$
m _ { 1 } \frac { d ^ { 2 } x _ { 1 } } { d t ^ { 2 } } = \mathrm { ~ - ~ } k ^ { 2 } m _ { 1 } \sum _ { j = 2 } ^ { n } m _ { j } \frac { \left( x _ { 1 } - x _ { j } \right) } { r ^ { 3 } { } _ { 1 , { \mathrm { ~ } j } } } ,
$$

and there are corresponding equations in $_ y$ and $\pmb { z }$ ·

There are similar equations for each body,and the whole system of equations is

$$
\left\{ \begin{array} { l l } { m _ { \ast } \displaystyle \frac { d ^ { 2 } x _ { \ast } } { d t ^ { 2 } } = \displaystyle - k ^ { 2 } m _ { \ast } \displaystyle \sum _ { j = 1 } ^ { n } m _ { i } \displaystyle \frac { ( x _ { \ast } - x _ { i } ) } { r ^ { 3 } \imath , i } , } \\ { m _ { \ast } \displaystyle \frac { d ^ { 2 } y _ { i } } { d t ^ { 2 } } = \displaystyle - \ k ^ { 2 } m _ { \ast } \displaystyle \sum _ { j = 1 } ^ { n } m _ { i } \displaystyle \frac { ( y _ { i } - y _ { i } ) } { r ^ { 3 } \imath , i } , } \\ { m _ { i } \displaystyle \frac { d ^ { 2 } z _ { i } } { d t ^ { 2 } } = \displaystyle - \ k ^ { 2 } m _ { \ast } \displaystyle \sum _ { j = 1 } ^ { n } m _ { i } \displaystyle \frac { ( z _ { i } - z _ { j } ) } { r ^ { 3 } \imath , i } ; \quad ( i = 1 , \cdots , n ; j \neq i ) . } \end{array} \right.
$$

Each of these equations involves all of the $_ { 3 n }$ variables $x _ { i } , \ y _ { i } ,$ and $z _ { i } ,$ and the system must, therefore,be solved simultaneously. There are ${ 3 n }$ equations each of the second order，so that the problem is of order $6 n$

Equations (1) can be put ina simple and elegant form by the introduction of the potential function,which in this problem will be denoted by $U$ instead of $V$ .The constant $k ^ { 2 }$ will be included in the potential. In chap.iv the potential, $V$ ，was defined by the integral $V = \int \frac { d m } { \rho }$ - In this case the system is composed of discrete masses, and the potential is

$$
U = \textstyle { \frac { 1 } { 2 } } k ^ { 2 } \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } { \frac { m _ { i } m _ { j } } { r _ { i , i } } } , \qquad ( i \neq j ) .
$$

The partial derivative of $\boldsymbol { U }$ with respect to $\pmb { x _ { i } }$ is

$$
\frac { \partial U } { \partial x _ { i } } = k ^ { 2 } m _ { i } \frac { \partial } { \partial x _ { i } } \sum _ { j = 1 } ^ { n } \frac { m _ { j } } { r _ { i , j } } = - k ^ { 2 } m _ { i } \sum _ { j = 1 } ^ { n } m _ { j } \frac { ( x _ { i } - x _ { i } ) } { r ^ { 3 } \llap / v _ { i , j } } , ~ ( i \pm j ) ,
$$

and there are similar equations in ${ { y } _ { i } }$ and ${ \pmb z _ { i } }$ .Therefore equations (1) can be written in the form

$$
\left\{ \begin{array} { l l } { m _ { i } \displaystyle \frac { d ^ { 2 } x _ { i } } { d t ^ { 2 } } = \displaystyle \frac { \partial U } { \partial x _ { i } } , } \\ { m _ { i } \displaystyle \frac { d ^ { 2 } y _ { i } } { d t ^ { 2 } } = \displaystyle \frac { \partial U } { \partial y _ { i } } , } \\ { m _ { i } \displaystyle \frac { d ^ { 2 } z _ { i } } { d t ^ { 2 } } = \displaystyle \frac { \partial U } { \partial z _ { i } } , \qquad ( i = 1 , ~ \cdots , ~ n ) . } \end{array} \right.
$$

144.The Six Integrals of the Motion of the Center of Mass. The function $\boldsymbol { \tau }$ is independent of the choice of the coordinate axes since it depends upon the mutual distances of the bodies alone.Therefore,if the origin is displaced parallel to the ${ \pmb x } \mathrm { \cdot }$ -axis in the negative direction through a distance $_ { \pmb { \alpha } }$ ，the $\pmb { x }$ -coordinate of every body will be increased by the quantity $\pmb { \alpha }$ ,but the potential function will not be changed. Let the fact that $U$ is a function of all the $\pmb { x }$ -coordinates be indicated by writing

$$
U = U ( x _ { 1 } , \ x _ { 2 } , \ \cdot \cdot \cdot , \ x _ { n } ) .
$$

After the origin is displaced the $\pmb { x }$ -coordinates become

$$
x _ { i } \prime = x _ { i } + \alpha , ( i = 1 , \ \cdots , \ n ) .
$$

The partial derivative of $U$ with respect to $_ { \pmb { \alpha } }$ is

$$
{ \frac { \partial U } { \partial \alpha } } = { \frac { \partial U } { \partial { x _ { 1 } } ^ { \prime } } } { \frac { \partial { x _ { 1 } } ^ { \prime } } { \partial \alpha } } + { \frac { \partial U } { \partial { x _ { 2 } } ^ { \prime } } } { \frac { \partial { x _ { 2 } } ^ { \prime } } { \partial \alpha } } + \cdots + { \frac { \partial U } { \partial { x _ { n } } ^ { \prime } } } { \frac { \partial { x _ { n } } ^ { \prime } } { \partial \alpha } } .
$$

But $\frac { \partial x _ { 2 } ^ { \prime } } { \partial \alpha } = 1$ ， $( i = 1 , \cdots , n )$ and $\frac { \partial U } { \partial \alpha } = 0$ because $U$ does not involve $_ { \pmb { \alpha } }$ explicitly. Therefore，on dropping the accents and

writing the corresponding equations in $y _ { i }$ and ${ \pmb z } _ { \pmb { i } }$ for displacements $\beta$ and $\gamma .$ ,it is found that

$$
\left\{ \begin{array} { l } { \displaystyle { \frac { \partial U } { \partial \alpha } } = \sum _ { i = 1 } ^ { n } { \frac { \partial U } { \partial x _ { i } } } = 0 , } \\ { \displaystyle { \frac { \partial U } { \partial \beta } } = \sum _ { i = 1 } ^ { n } { \frac { \partial U } { \partial y _ { i } } } = 0 , } \\ { \displaystyle { \frac { \partial U } { \partial \gamma } } = \sum _ { i = 1 } ^ { n } { \frac { \partial U } { \partial z _ { i } } } = 0 . } \end{array} \right.
$$

Therefore equations (3) give

$$
\left\{ \begin{array} { l l } { \displaystyle \sum _ { i = 1 } ^ { n } m _ { * } \frac { d ^ { 2 } x _ { i } } { d t ^ { 2 } } = 0 , } \\ { \displaystyle \sum _ { i = 1 } ^ { n } m _ { * } \frac { d ^ { 2 } y _ { i } } { d t ^ { 2 } } = 0 , } \\ { \displaystyle \sum _ { i = 1 } ^ { n } m _ { * } \frac { d ^ { 2 } z _ { i } } { d t ^ { 2 } } = 0 . } \end{array} \right.
$$

These equations are at once integrable,and the result of integration is

$$
\left\{ \begin{array} { l l } { \displaystyle { \sum _ { i = 1 } ^ { n } m _ { \mathrm { i } } \frac { d x _ { \mathrm { i } } } { d t } = \alpha _ { 1 } } , } \\ { \displaystyle { \sum _ { i = 1 } ^ { n } m _ { \mathrm { i } } \frac { d y _ { \mathrm { i } } } { d t } = \beta _ { 1 } } , } \\ { \displaystyle { \sum _ { i = 1 } ^ { n } m _ { \mathrm { i } } \frac { d z _ { \mathrm { i } } } { d t } = \gamma _ { 1 } } , } \end{array} \right.
$$

where $\alpha _ { 1 } , \beta _ { 1 } , \gamma _ { 1 }$ are the constants of integration. On integrating again,it follows that

$$
\left\{ \begin{array} { l l } { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } x _ { i } = \alpha _ { 1 } t + \alpha _ { 2 } , } \\ { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } y _ { i } = \beta _ { 1 } t + \beta _ { 2 } , } \\ { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } z _ { i } = \gamma _ { 1 } t + \gamma _ { 2 } . } \end{array} \right.
$$

Let $\sum _ { i = 1 } ^ { n } m _ { i } = M$ and $\bar { x } , ~ \bar { y }$ and $\vec { z }$ represent the coordinates of the center of mass of the $_ n$ bodies; then,by Art.19,