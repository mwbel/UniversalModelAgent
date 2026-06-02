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


<!-- chunk 0005: pages 281-350 -->
$$
\left\{ \begin{array} { l l } { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } x _ { i } = M \bar { x } , } \\ { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } y _ { i } = M \bar { y } , } \\ { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } z _ { i } = M \bar { z } . } \end{array} \right.
$$

Therefore,equations (5) become

$$
\left\{ \begin{array} { l l } { M \bar { x } = \alpha _ { 1 } t + \alpha _ { 2 } , } \\ { M \bar { y } = \beta _ { 1 } t + \beta _ { 2 } , } \\ { M \bar { z } = \gamma _ { 1 } t + \gamma _ { 2 } ; } \end{array} \right.
$$

that is,the coordinates of the center of mass vary directly as the time. From this it can be inferred that the center of mass moves with uniform speed in a straight line. Or otherwise,the velocity of the center of mass is

$$
\overline { { V } } = \sqrt { \left. \frac { d \bar { x } } { d t } \right. ^ { 2 } + \left( \frac { d \bar { y } } { d t } \right) ^ { 2 } + \left( \frac { d \bar { z } } { d t } \right) ^ { 2 } } = \frac { 1 } { M } \sqrt { \alpha _ { 1 } { } ^ { 2 } + \beta _ { 1 } { } ^ { 2 } + \gamma _ { 1 } { } ^ { 2 } } ,
$$

which is a constant；and on eliminating $t$ from equations (7),it is found that

$$
\frac { M \bar { x } - \alpha _ { 2 } } { \alpha _ { 1 } } = \frac { M \bar { y } - \beta _ { 2 } } { \beta _ { 1 } } = \frac { M \bar { z } - \gamma _ { 2 } } { \gamma _ { 1 } } ,
$$

which are the symmetrical equations of a straight line in space of three dimensions. Equations (8) and (9) give the theorem:

If n bodies are subject to no forces except their mutual attractions, their center of mass moves in $^ { a }$ straight line with uniform speed. The special case $\overline { { V } } = 0$ will arise if $\alpha _ { 1 } = \beta _ { 1 } = \gamma _ { 1 } = 0$ Since it is impossible to know any fixed point in space it is impossible to determine the six constants.

The origin might now be transferred to the center of mass of the system，as it was in the Problem of Two Bodies,or, to the center of one of the bodies,as it will be in Art.148,and the order of the problem reduced six units.

145.The Three Integrals of Areas. The potential function is not changed by a rotation of the axes. Suppose the system of coordinates is rotated around the $\pmb { \mathscr { z } } .$ -axis through the angle $- \phi _ { * }$ and call the new coordinates $x _ { i } ^ { \prime } , y _ { i } ^ { \prime }$ and $\tilde { z } _ { i } ^ { \prime }$ .They are related to the old by the equationg

$$
\left\{ \begin{array} { l l } { x _ { i } { ' } = x _ { i } \cos \phi - y _ { i } \sin \phi , } \\ { y _ { i } { ' } = x _ { i } \sin \phi + y _ { i } \cos \phi , } \\ { z _ { i } { ' } = z _ { i } , \qquad ( i = 1 , \cdot \cdot \cdot , n ) . } \end{array} \right.
$$

Since the function $U$ is not changed by the rotation it does not contain $\phi$ explicitly；therefore

$$
{ \frac { \partial U } { \partial \phi } } = \sum _ { i = 1 } ^ { n } { \frac { \partial U } { \partial { x _ { i } } ^ { \prime } } } { \frac { \partial { x _ { i } } ^ { \prime } } { \partial \phi } } + \sum _ { i = 1 } ^ { n } { \frac { \partial U } { \partial { y _ { i } } ^ { \prime } } } { \frac { \partial { y _ { i } } ^ { \prime } } { \partial \phi } } + \sum _ { i = 1 } ^ { n } { \frac { \partial U } { \partial { z _ { i } } ^ { \prime } } } { \frac { \partial { z _ { i } } ^ { \prime } } { \partial \phi } } = 0 .
$$

But from (10) it follows that

$$
{ \frac { \partial { x _ { i } } ^ { \prime } } { \partial \phi } } = \ - \ { y _ { i } } ^ { \prime } , \qquad { \frac { \partial { y _ { i } } ^ { \prime } } { \partial \phi } } = { x _ { i } } ^ { \prime } , \qquad { \frac { \partial { z _ { i } } ^ { \prime } } { \partial \phi } } = 0 , \qquad ( i = 1 , \ \cdots , \ n ) ;
$$

therefore (11） becomes

$$
\sum _ { i = 1 } ^ { n } \left[ { x _ { i } } ^ { \prime } { \frac { \partial U } { \partial y _ { i } ^ { \prime } } } - { y _ { i } } ^ { \prime } { \frac { \partial U } { \partial x _ { i } ^ { \prime } } } \right] = 0 .
$$

On dropping the accents,which are of no further use,it is found as a consequence of (3) that

$$
\left\{ \begin{array} { l l } { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } \left[ x _ { i } \frac { d ^ { 2 } y _ { i } } { d t ^ { 2 } } - y _ { i } \frac { d ^ { 2 } x _ { i } } { d t ^ { 2 } } \right] = 0 , } \\ { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } \left[ y _ { i } \frac { d ^ { 2 } z _ { i } } { d t ^ { 2 } } - z _ { i } \frac { d ^ { 2 } y _ { i } } { d t ^ { 2 } } \right] = 0 , } \\ { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } \left[ z _ { i } \frac { d ^ { 2 } x _ { i } } { d t ^ { 2 } } - x _ { i } \frac { d ^ { 2 } z _ { i } } { d t ^ { 2 } } \right] = 0 . } \end{array} \right.
$$

Each term of these sums can be integrated separately, giving

$$
\left\{ \begin{array} { l l } { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } \left[ x _ { i } \frac { d y _ { i } } { d t } - y _ { i } \frac { d x _ { i } } { d t } \right] = c _ { 1 } , } \\ { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } \left[ y _ { i } \frac { d z _ { i } } { d t } - z _ { i } \frac { d y _ { i } } { d t } \right] = c _ { 2 } , } \\ { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } \left[ z _ { i } \frac { d x _ { i } } { d t } - x _ { i } \frac { d z _ { i } } { d t } \right] = c _ { 3 } . } \end{array} \right.
$$

The parentheses are the projections of the areal velocities of the various bodies upon the three fundamental planes (Art.16). As it is impossible to determine any fixed point in space,so also it is impossible to determine any fixed direction in space；consequently it is impossible tc determine practically the constants $c _ { 1 } , \ c _ { 2 } , \ c _ { 3 }$ ，Yet,in this case it is customary to assume that the fixed stars,on the average, do not revolve in space, so that, by observing them, these constants can be determined. It is evident, however,that there is no more reason for assuming that the stars do not revolve than there is for assuming that they are not drifting through space,each being a pure assumption without any possibility of proof or disproof.But it is to be noted that,if these assumptions are granted, the constants $c _ { 1 } , \ c _ { 2 } ,$ and $c _ { 3 }$ can be determined easily with a high degree of precision,while in the present state of observational Astronomy the constants of equations (4) cannot be found with any considerable accuracy.

Let $A _ { i } , \ B _ { i }$ and $C _ { i }$ represent the projections of the areas de-scribed by the line from the origin to the body $m _ { i }$ upon the $x y , y z ,$ and ${ \pmb z x } .$ -planes respectively;then (12) can be written

$$
\left\{ \begin{array} { l } { { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } { \frac { d A _ { i } } { d t } } = c _ { 1 } } , } \\ { { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } { \frac { d B _ { i } } { d t } } = c _ { 2 } } , } \\ { { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } { \frac { d C _ { i } } { d t } } = c _ { 3 } } , } \end{array} \right.
$$

the integrals of which are

$$
\left\{ \begin{array} { l l } { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } A _ { i } = c _ { 1 } t + c _ { 1 } { ' } , } \\ { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } B _ { i } = c _ { 2 } t + c _ { 2 } { ' } , } \\ { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } C _ { i } = c _ { 3 } t + c _ { 3 } { ' } . } \end{array} \right.
$$

Hence the theorem:

The sums of the products of the masses and the projections of the areas described by the corresponding radii are proportional to the time; or, from (12),the sums of the products of the masses and the rates of the projections of the areas are constants.

It is possible,as was first shown by Laplace, to direct the axes so that two of the constants in equations (12) shall be zero,while the third becomes $\sqrt { { c _ { 1 } } ^ { 2 } + { c _ { 2 } } ^ { 2 } + { c _ { 3 } } ^ { 2 } }$ .This is the plane of maximum sum of the products of the masses and the rates of the projections of areas. Its relations to the original fixed axes are defined by the constants $c _ { 1 } , \ c _ { 2 } , \ c _ { 3 } ,$ ，and its position is,therefore, always the same. On this account it was called the invariable plane by Laplace. At present the invariable plane of the solar system is inclined to the ecliptic by about $2 ^ { \circ }$ ，and the longitude of its ascending node is about $2 8 6 ^ { \circ }$ .These fgures are subject to some uncertainty because of our imperfect knowledge regarding the masses of some of the planets. If the position of the plane were known with exactness it would possess some practical advantages over the ecliptic，which undergoes considerable variations,as a fundamental plane of reference. It has been of great value in certain theoretical investigations.\*

146.The Energy Integral.t On multiplying equations (3) by $\frac { d x _ { i } } { d t } , \frac { d y _ { i } } { d t } , \frac { d z _ { i } } { d t }$ respectively,adding,and summing with respect to $_ i$ ， it is found that

$$
\begin{array} { r l } & { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } \left\{ \frac { d ^ { 2 } x _ { i } } { d t ^ { 2 } } \frac { d x _ { i } } { d t } + \frac { d ^ { 2 } y _ { i } } { d t ^ { 2 } } \frac { d y _ { i } } { d t } + \frac { d ^ { 2 } z _ { i } } { d t ^ { 2 } } \frac { d z _ { i } } { d t } \right\} } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \left. \frac { \partial U } { \partial x _ { i } } \frac { d x _ { i } } { d t } + \frac { \partial U } { \partial y _ { i } } \frac { d y _ { i } } { d t } + \frac { \partial U } { \partial z _ { i } } \frac { d z _ { i } } { d t } \right\} . } \end{array}
$$

The potential $U$ is a function of the $3 n$ variables $x _ { i } , y _ { i } , z _ { i } ,$ alone; therefore the right member of (l4) is the total derivative of $U$ with respect to $\scriptstyle t .$ ，Upon integrating both members of this equation,it is found that

$$
{ \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { n } m _ { i } \left\{ \left( { \frac { d x _ { i } } { d t } } \right) ^ { 2 } + \left( { \frac { d y _ { i } } { d t } } \right) ^ { 2 } + \left( { \frac { d z _ { i } } { d t } } \right) ^ { 2 } \right\} = U + h .
$$

The left member of this equation is the kinetic energy of the whole system，and the right member is the potential function plus & constant.

Let the potential energy of one configuration of a system with respect to another configuration be defined as the amount of work required to change it from the one to the other. If two bodies attract each other according to the law of the inverse squares, the force existing between them is $\frac { k ^ { 2 } m _ { i } m _ { j } } { r ^ { 2 } { } _ { i , ~ j } }$ The amount of work done inhanging theirdistanceapartfrom $r _ { i , j } ^ { ( 0 ) }$ to $r _ { i , j }$ is

$$
W _ { i , j } = k ^ { 2 } m _ { i } m _ { j } { \int _ { r _ { i , j } ^ { ( 0 ) } } ^ { r _ { i } , j } } \frac { d r _ { i , j } } { r _ { i , j } ^ { 2 } } = k ^ { 2 } m _ { i } m _ { j } \left[ \frac { 1 } { r _ { i , j } ^ { ( 0 ) } } - \frac { 1 } { r _ { i , j } } \right] .
$$

\*See memoirs by Jacobi,Journal de Math.,vol.Ix.； Tisserand,Méc.Cel. vol.1., chap.xxv.; Poincaré,Les Méthodes Nouvelles de la Méc.Cel.,vol.I., p.39.

$^ { \dagger }$ This is very frequently called the Vis Viva integral.

If the bodies are at an infinite distance from one another at the start, then $r _ { \uparrow , \ast } ^ { ( 0 ) } = \infty$ ,and (16) becomes

hence

$$
\begin{array} { r l r } & { } & { - \ { \cal W } _ { i , i } = \frac { k ^ { 2 } m _ { i } m _ { j } } { r _ { i , \ j } } ; } \\ & { } & { } \\ & { } & { { \cal U } = - \displaystyle \frac { 1 } { 2 } \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } { \cal W } _ { i , i } . } \end{array}
$$

Therefore, $\boldsymbol { U }$ is the negative of the potential energy of the whole system with respect to the infinite separation of the bodies as the original configuration. Hence (15) gives the theorem:

In a system of $\scriptstyle n$ bodies subject to no forces except their mutual attractions the sum of the kinetic and potential energies is a constant.

147. The Question of New Integrals. Ten of the whole $6 n$ integrals which are required in order to solve the problem com-pletely have been found. These ten integrals are the only ones known,and the question arises whether any more of certain types exist.

In a profound memoir in the Acta Mathematica, vol. x1., Bruns has demonstrated that，when the rectangular coordinates are chosen as dependent variables, there are no new algebraic integrals. This does not,of course,exclude the possibility of algebraic integrals when other variables are used. Poincaré has demonstrated in his prize memoir in the Acta Mathematica, vol. xI1., and again with some additions in Les Methodes Nouvelles de la Mécanique Céleste,chap.V.,that the Problem of Three Bodies admits no new uniform transcendental integrals,even when the masses of two of the bodies are very small compared to that of the third. In this theorem the dependent variables are the elements of the orbits of the bodies，which continually change under their mutual attractions. It does not follow that integrals of the class considered by Poincaré do not exist when other dependent variables are employed. In fact, Levi-Civita has shown the existence of this class of integrals in a special problem，which comes under Poincaré's theorem，when suitable variables are used (Acta Mathematica， vol. xxx.). The practical importance of the theorems of Bruns and Poincaré have often been overrated by those who have forgotten the conditions under which they have been proved to hold true.

# XVIII. PROBLEMS.

1.Write equations (1） when the force varies inversely as the nth power of the distance.For what values of $_ { n }$ do the cquations all become independent? The Problem of $\pmb { n }$ Bodies can be completely solved for this law of force;show that the orbits with respect to the center of mass of the system are all ellipses with this point as center.Show that the orbit of any body with respect to any other is also a central ellipse,and that the same is true for the motion of any body with respect to the center of mass of any subgroup of the whole system. Show that the periods are all equal.

2.What will be the definition of the potential function when the force varies inversely as the nth power of the distance?

3. Derive the equations immediately preceding (4) directly from equations (1).

4.Prove that the theorem regarding the motion of the center of mass holds when the force varies as any power of the distance.

5.Derive the equations immediately preceding (12) directly from equations (1),and show that they hold when the force varies as any power of the distance.

6.Any plane through the origin can be changed into any other plane through the origin by a rotation around each of two of the coordinate axes. Transform equations (12) by successive rotations around two of the axes,and show that the angles of rotation can be so chosen that two of the constants, to which the functions of the new coordinates similar to (12) are equal,are zero,and that the third is $\sqrt { { c _ { 1 } } ^ { 2 } + { c _ { 2 } } ^ { 2 } + { c _ { 3 } } ^ { 2 } }$ ：(This is the method used by Laplace to prove the existence of the invariable plane.)

7.Why are equations (13） not to be regarded as integrals of the differential equations (1),thus making the whole number of integrals thirteen?

148. Transfer of the Origin to the Sun. Nothing is known of the absolute motions of the planets because the observations furnish information regarding only their relative positions,or their positions with respect to the sun.It is true that it is known that the solar system is moving toward the constellation Hercules, but it must be remembered that this motion is only with respect to certain of the stars. The problem for the student of Celestial Mechanics is to determine the relative positions of the members of the solar system；or,in particular,to determine the positions of the planets with respect to the sun. To do this it is advanta-geous to transfer the origin to the sun,and to employ the resulting differential equations.

Suppose $m _ { n }$ is the sun and take its center as the origin,and let the coordinates of the body $m _ { i }$ referred to the new system be $x _ { i } ^ { \prime } , \ y _ { i } ^ { \prime } , \ z _ { i } ^ { \prime }$ .Then the old coordinates are expressed in terms of the new by the equations

$$
x _ { i } = x _ { i } { ' } + x _ { n } , y _ { i } = y _ { i } { ' } + y _ { n } , z _ { i } = z _ { i } { ' } + z _ { n } , ( i = 1 , \cdots , n - 1 ) .
$$

Since the differences of the old variables are equal to the corresponding differences of the new,it follows that

$$
\frac { \partial U } { \partial x _ { i } } = \frac { \partial U } { \partial x _ { i } } , \qquad \frac { \partial U } { \partial y _ { i } } = \frac { \partial U } { \partial y _ { i } } , \qquad \frac { \partial U } { \partial z _ { i } } = \frac { \partial U } { \partial z _ { i } } , \qquad ( i = 1 , \ \cdots , \ n - 1 ) .
$$

As a consequence of these transformations equations (3) become

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } x _ { i } ^ { \prime } } { d t ^ { 2 } } + \frac { d ^ { 2 } x _ { n } } { d t ^ { 2 } } = \displaystyle \frac { 1 } { m _ { i } } \frac { \partial U } { \partial x _ { i } ^ { \prime } } , } \\ { \displaystyle \frac { d ^ { 2 } y _ { i } ^ { \prime } } { d t ^ { 2 } } + \frac { d ^ { 2 } y _ { n } } { d t ^ { 2 } } = \displaystyle \frac { 1 } { m _ { i } } \frac { \partial U } { \partial y _ { i } ^ { \prime } } , } \\ { \displaystyle \frac { d ^ { 2 } z _ { i } ^ { \prime } } { d t ^ { 2 } } + \frac { d ^ { 2 } z _ { n } } { d t ^ { 2 } } = \displaystyle \frac { 1 } { m _ { i } } \frac { \partial U } { d z _ { i } ^ { \prime } } , \qquad ( i = 1 , ~ \cdots , ~ n - 1 ) . } \end{array} \right.
$$

Since the origin is at $x _ { n } { ' } = y _ { n } { ' } = z _ { n } { ' } = 0$ ,the first equation of (1)gives,on putting ${ \textit { i } } = n$ ，

$$
\begin{array} { r l } & { \frac { d ^ { 2 } x _ { n } } { d t ^ { 2 } } = \frac { k ^ { 2 } m _ { 1 } { x _ { 1 } } ^ { \prime } } { r ^ { 3 } \scriptscriptstyle { 1 } , n } + \frac { k ^ { 2 } m _ { 2 } { x _ { 2 } } ^ { \prime } } { r ^ { 3 } \scriptscriptstyle { 2 } , n } + \cdot \cdot \cdot + \frac { k ^ { 2 } m _ { n - 1 } { x _ { \star - 1 } ^ { \prime } } } { r ^ { 3 } \scriptscriptstyle { n - 1 } , n } } \\ & { \phantom { \frac { d ^ { 2 } x _ { n } } { d t ^ { 2 } } } = k ^ { 2 } \sum _ { j = 1 } ^ { n - 1 } \frac { m _ { j } { x _ { j } } ^ { \prime } } { r ^ { 3 } j , n } . } \end{array}
$$

This equation,with the corresponding ones in $_ y$ and $\pmb { z }$ ，substituted in (17） completes the transformation to the new variables；but it will be advantageous to combine the terms in another manner so that those which come from the attraction of the sun shall be separate from the others. The differential equations will be written for the body $m _ { 1 } ,$ ,from which the others can be formed by permuting the subscripts.

The potential function can be broken up into the sum

or,

$$
\begin{array} { c } { { U = k ^ { 2 } m _ { n } \displaystyle \sum _ { i = 1 } ^ { n - 1 } \displaystyle \frac { m _ { i } } { r _ { i , n } } + \frac { \imath } { \bar { z } } k ^ { 2 } \displaystyle \sum _ { i = 1 } ^ { n - 1 } \displaystyle \sum _ { j = 1 } ^ { n - 1 } \displaystyle \frac { m _ { i } m _ { j } } { r _ { i , j } } , \quad ( i \ne j ) ; } } \\ { { U = k ^ { 2 } m _ { n } \displaystyle \sum _ { j = 1 } ^ { n - 1 } \displaystyle \frac { m _ { j } } { r _ { j , n } } + U ^ { \prime } . } } \end{array}
$$

On substituting equations (18) and (19) in equations (17),the latter become

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } { x _ { 1 } } ^ { \prime } } { d t ^ { 2 } } + k ^ { 2 } ( m _ { 1 } + m _ { n } ) \frac { { x _ { 1 } } ^ { \prime } } { r ^ { 3 } \scriptscriptstyle 1 , n } = \frac { 1 } { m _ { 1 } } \frac { \partial U ^ { \prime } } { \partial { x _ { 1 } } ^ { \prime } } - k ^ { 2 } \sum _ { j = 2 } ^ { n - 1 } \frac { m _ { j } { x _ { j } } ^ { \prime } } { r ^ { 3 } j , n } , } \\ { \displaystyle \frac { d ^ { 2 } { y _ { 1 } } ^ { \prime } } { d t ^ { 2 } } + k ^ { 2 } ( m _ { 1 } + m _ { n } ) \frac { { y _ { 1 } } ^ { \prime } } { r ^ { 3 } \scriptscriptstyle 1 , n } = \frac { 1 } { m _ { 1 } } \frac { \partial U ^ { \prime } } { \partial { y _ { 1 } } ^ { \prime } } - k ^ { 2 } \sum _ { j = 2 } ^ { n - 1 } \frac { m _ { j } { y _ { j } } ^ { \prime } } { r ^ { 3 } j , n } , } \\ { \displaystyle \frac { d ^ { 2 } { z _ { 1 } } ^ { \prime } } { d t ^ { 2 } } + k ^ { 2 } ( m _ { 1 } + m _ { n } ) \frac { { z _ { 1 } } ^ { \prime } } { r ^ { 3 } \scriptscriptstyle 1 , n } = \frac { 1 } { m _ { 1 } } \frac { \partial U ^ { \prime } } { \partial { z _ { 1 } } ^ { \prime } } - k ^ { 2 } \sum _ { j = 2 } ^ { n - 1 } \frac { m _ { j } { z _ { j } } ^ { \prime } } { r ^ { 3 } j , n } . } \end{array} \right.
$$

Let

$$
R _ { 1 , j } = \lambda ^ { 2 } \bigg \{ \frac { 1 } { r _ { 1 , j } } - \frac { x _ { 1 } ^ { \prime } x _ { j } ^ { \prime } + y _ { 1 } ^ { \prime } y _ { j } ^ { \prime } + z _ { 1 } ^ { \prime } z _ { j } ^ { \prime } } { r _ { j , n } ^ { 3 } } \bigg \} ;
$$

then,equations (2O) can be written in the form

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } x _ { 1 } { } ^ { \prime } } { d t ^ { 2 } } + k ^ { 2 } ( m _ { 1 } + m _ { n } ) \frac { x _ { 1 } { } ^ { \prime } } { r ^ { 3 } \scriptscriptstyle { } _ { 1 , n } } = \sum _ { j = 2 } ^ { n - 1 } m _ { j } \frac { \partial R _ { 1 , j } } { \partial x _ { 1 } { } ^ { \prime } } , } \\ { \displaystyle \frac { d ^ { 2 } y _ { 1 } { } ^ { \prime } } { d t ^ { 2 } } + k ^ { 2 } ( m _ { 1 } + m _ { n } ) \frac { y _ { 1 } { } ^ { \prime } } { r ^ { 3 } \scriptscriptstyle { } _ { 1 , n } } = \sum _ { j = 2 } ^ { n - 1 } m _ { j } \frac { \partial R _ { 1 , j } } { \partial y _ { 1 } { } ^ { \prime } } , } \\ { \displaystyle \frac { d ^ { 2 } z _ { 1 } { } ^ { \prime } } { d t ^ { 2 } } + k ^ { 2 } ( m _ { 1 } + m _ { n } ) \frac { z _ { 1 } { } ^ { \prime } } { r ^ { 3 } \scriptscriptstyle { } _ { 1 , n } } = \sum _ { j = 2 } ^ { n - 1 } m _ { j } \frac { \partial R _ { 1 , j } } { \partial z _ { 1 } { } ^ { \prime } } . } \end{array} \right.
$$

Let the accents,which have become useless, be dropped, and, in order to derive the general equations corresponding to (21), let

$$
R _ { i , j } = k ^ { 2 } \left\{ { \frac { 1 } { r _ { i , j } } } - { \frac { x _ { i } x _ { j } + y _ { i } y _ { j } + z _ { i } z _ { j } } { r _ { i , n } ^ { 3 } } } \right\} , \qquad ( i \neq j
$$

Then, the general equations for relative motion are

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } x _ { i } } { d t ^ { 2 } } + k ^ { 2 } ( m _ { i } + m _ { n } ) \frac { x _ { i } } { r ^ { 3 } i , n } = \sum _ { j = 1 } ^ { n - 1 } m _ { j } \frac { \partial R _ { i , j } } { \partial x _ { i } } , } \\ { \displaystyle \frac { d ^ { 2 } y _ { i } } { d t ^ { 2 } } + k ^ { 2 } ( m _ { i } + m _ { n } ) \frac { y _ { i } } { r ^ { 3 } i , n } = \sum _ { j = 1 } ^ { n - 1 } m _ { j } \frac { \partial R _ { i , j } } { \partial y _ { i } } , } \\ { \displaystyle \frac { d ^ { 2 } z _ { i } } { d t ^ { 2 } } + k ^ { 2 } ( m _ { i } + m _ { n } ) \frac { z _ { i } } { r ^ { 3 } i , n } = \sum _ { j = 1 } ^ { n - 1 } m _ { j } \frac { \partial R _ { i , j } } { \partial z _ { i } } , } \end{array} \right.
$$

in which $i = 1 , \cdots , n - 1$

149.Dynamical Meaning of the Equations. In order to understand easily the meaning of the equations,suppose that there are but three bodies, $m _ { 1 } , ~ m _ { 2 } ,$ and $m _ { n }$ Suppose $m _ { n }$ is the sun, let its mass equal unity,and let the distances from it to $m _ { 1 }$ and $\mathbf { \Delta } m _ { 2 }$ be $\pmb { r } _ { 1 }$ and $\boldsymbol { r } _ { 2 }$ respectively. Then equations (23) are,in full,

$$
\begin{array} { r }  \{ \begin{array} { l l } { \frac { d ^ { 2 } \widetilde { x } \gamma _ { 1 } } { d t } + k ^ { \nu } ( 1 + m _ { 1 } ) \frac { x _ { 1 } } { \gamma _ { 1 } ^ { 3 } } = k ^ { \nu } m _ { 2 } \frac { \widetilde { \vartheta } } { \widetilde { x } _ { 1 } } \{ \frac { 1 } { r _ { 1 , 2 } } - \frac { x _ { 1 } x _ { 2 } + y _ { 1 } y _ { 3 } + z _ { 1 } z _ { 2 } } { \gamma _ { 2 } ^ { 3 } } \} , } \\ { \frac { d ^ { 2 } \widetilde { y } \gamma _ { 1 } } { d t } + k ^ { \nu } ( 1 + m _ { 1 } ) \frac { y _ { 1 } } { \gamma _ { 1 } ^ { 3 } } = k ^ { \nu } m _ { 2 } \frac { \widetilde { \vartheta } } { \widetilde { x } _ { 1 } } \{ \frac { 1 } { r _ { 1 , 2 } } - \frac { x _ { 1 } x _ { 2 } + y _ { 1 } y _ { 3 } + z _ { 2 } + z _ { 1 } z _ { 3 } } { \gamma _ { 2 } ^ { 3 } } \} , } \\ { \frac { d ^ { 2 } z _ { 1 } } { d t ^ { 5 } } + k ^ { \nu } ( 1 + m _ { 1 } ) \frac { z _ { 1 } } { \gamma _ { 1 } ^ { 2 } } = k ^ { \nu } m _ { 3 } \frac { \widetilde { \vartheta } } { \widetilde { x } _ { 2 } } \{ \frac { 1 } { r _ { 1 , 3 } } - \frac { x _ { 1 } x _ { 2 } - y _ { 1 } y _ { 3 } + z _ { 1 } z _ { 3 } } { \gamma _ { 2 } ^ { 5 } } \} ; } \\ { \frac { d ^ { 2 } x _ { 2 } } { d t } + k ^ { \nu } ( 1 + m _ { 2 } ) \frac { x _ { 2 } } { \gamma _ { 3 } ^ { 2 } } = k ^ { \nu } m _ { 1 } \frac { \widetilde { \vartheta } } { d z _ { 1 } } \{ \frac { 1 } { r _ { 2 , 1 } } - \frac { x _ { 2 } x _ { 1 } + y _ { 2 } y _ { 1 } + z _ { 2 } z _ { 2 } } { \gamma _ { 1 } ^ { 3 } } \} , } \\  \frac { d ^ { 2 } x _ { 3 } } { d t } + k ^ { \nu } ( 1 + m _ { 3 } ) \frac { x _ { 2 } } { \gamma _ { 3 } ^ { 3 } } = k ^ { \nu } m _  \end{array} \end{array}
$$

If $m _ { 2 }$ were zero the frst three equations would be independent of the second three,and they would then be the equations for the relative motion of the body $m _ { 1 }$ with respect to $m _ { n } = 1$ ,and could be integrated. All the variations from the purely elliptical motion arise from the presence of the right members,which are, in the first three equations,the partial derivatives of $R _ { 1 , : }$ with respect to the variables $x _ { 1 } , y _ { 1 } ,$ and ${ \pmb z _ { 1 } }$ respectively. On this account $m _ { 2 } R _ { 1 , \ 2 }$ is called the perturbative function.

The partial derivatives of the first terms of the right members of the first three equations are respectively

$$
\begin{array} { r } { { } - \ k ^ { 2 } m _ { 2 } \frac { \left( x _ { 1 } - x _ { 2 } \right) } { r ^ { 3 } 1 , \ 2 } , \quad { } - \ k ^ { 2 } m _ { 2 } \frac { \left( y _ { 1 } - y _ { 2 } \right) } { r ^ { 3 } 1 , \ 2 } , \quad { } - \ k ^ { 2 } m _ { 2 } \frac { \left( z _ { 1 } - z _ { 2 } \right) } { r ^ { 3 } 1 , \ 2 } , } \end{array}
$$

which are the components of acceleration of $\pmb { m _ { 1 } }$ due to the attraction of $\mathbf { \Delta } m _ { 2 }$ ，The partial derivatives of the second terms are

$$
\qquad - \ k ^ { 2 } m _ { 2 } { \frac { x _ { 2 } } { { r _ { 2 } } ^ { 3 } } } , \quad - \ k ^ { 2 } m _ { 2 } { \frac { y _ { 2 } } { { r _ { 2 } } ^ { 3 } } } , \quad - \ k ^ { 2 } m _ { 2 } { \frac { z _ { 2 } } { { r _ { 2 } } ^ { 3 } } } , \qquad 
$$

which are the negatives of the components of the acceleration of the sun due to the attraction of $\mathbf { \Delta } m _ { 2 }$ .Therefore the right members of the first three equations of (24) are the differences of the components of acceleration of $m _ { 1 }$ and of the sun due to the attraction of $m _ { 2 }$ .Similarly,the right members of the last three equations are the differences of the components of the acceleration of $m _ { 2 }$ and of the sun due to the attraction of $m _ { 1 }$ .If two bodies are subject to equal parallel accelerations their relative positions will not be changed. The differences of their accelerations are due to the disturbing forces,and measure these disturbances. The right members of (24) are,therefore,exactly those parts of the accelerations due to the disturbing forces.

If there are $n - 2$ disturbing bodies the right members are the sums of terms depending upon the bodies $m _ { 2 } , \cdots , m _ { n - 1 }$ similar to the right members of (24)，which depend upon $m _ { 2 }$ alone；or,in other words,the whole resultants of the disturbing accelerations are equal to the sums of the parts arising from the action of the separate disturbing bodies.

150.The Order of the System of Equations. The order of the system of equations (23） is $6 n - 6$ ,instead of $_ { 6 n }$ as (1）was in the case of absolute motion. In the absolute motion ten integrals were found which reduced the problem to order $6 n - 1 0$ Six of these related to the motion of the center of mass,three to the areal velocities，and one to the energy of the system. In the present case but four integrals, the three integrals of areas and the energy integral, can be found,which leaves the problem of order $6 n - 1 0$ also.

The problem can be reduced to the order $6 n - 6$ by using the integrals for the center of mass directly. In particular,consider the differential equations for the bodies $m _ { 1 } , m _ { 2 } , \cdots , m _ { n - 1 }$ In the original equations they involve the coordinates of $m _ { n }$ ，but these quantities can be eliminated by means of equations (5).

If the origin is taken at the center of mass

$$
\sum _ { i = 1 } ^ { n } m _ { i } x _ { i } = 0 , \qquad \sum _ { i = 1 } ^ { n } m _ { i } y _ { i } = 0 , \qquad \sum _ { i = 1 } ^ { n } m _ { i } z _ { i } = 0 ,
$$

and the elimination becomes particularly simple. $_ { \mathrm { { O r } } }$ ,because of these linear homogeneous relations,the $\boldsymbol { n }$ variables of each set can be expressed linearly and homogeneously in terms of $n \sim 1$ new variables. Thus

$$
\begin{array} { r l } & { x _ { 1 } = a _ { 1 1 } \xi _ { 1 } + a _ { 1 2 } \xi _ { 2 } + \cdots + a _ { 1 , n - 1 } \xi _ { n - 1 } , } \\ & { x _ { 2 } = a _ { 2 1 } \xi _ { 1 } + a _ { 2 2 } \xi _ { 2 } + \cdots + a _ { 2 , n - 1 } \xi _ { n - 1 } , } \\ & { \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \cdot \quad \cdot \cdot \quad \cdot \cdot \quad \cdot \quad \cdot \quad \cdot } \\ & { x _ { n } = a _ { n 1 } \xi _ { 1 } + a _ { n 2 } \xi _ { 2 } + \cdots + a _ { n , n - 1 } \xi _ { n - 1 } , } \end{array} .
$$

and similar sets of equations for $y$ and $\pmb { \mathscr { z } } .$ The coefficients ${ a } _ { i j }$ are arbitrary constants except that they must be so chosen that every determinant of the matrix of the substitutions shall be distinct from zero; for,otherwise,a linear relation would exist among the $\xi _ { i }$ These constants can be so chosen that the transformed equations preserve a symmetrical form. This method was employed by Jacobi in an important memoir entitled,Sur l'élimination des nceuds dans le probleme des trois corps (Journal de Math. vol. Ix., 1844),and by Radau in a memoir entitled, Sur une transformation des équations différentielles de la Dynamique (Annales de l'Ecole Normale, 1st series, vol. v.).

# XIX. PROBLEMS.

1. Make the transformation ${ \pmb x } _ { i } = { \pmb x } _ { i } ^ { \prime } + { \pmb x } _ { n }$ in the integrals (12) and (15), and eliminate xn, yn, 2n, dtdt and $\frac { d z _ { n } } { d t }$ by means of equations (4)and (5). Prove that the resulting expressions are four integrals of equations (23).

2.Derive equations (23) directly by taking the origin at $m _ { n } ,$ without first making use of the fixed axes.

3.The equations (23) are not symmetrical, since each body requires & different perturbative function $\mathbf { \mathit { R } } _ { : , : }$ in the right members.Construct the corresponding system of differential equations where the motion of $\scriptstyle m _ { n - 1 }$ is referred to a rectangular system of axes with the origin at $m _ { n }$ ； the motion of $\scriptstyle m _ { n - 2 }$ to a parallel system of axes with origin at the center of mass of $\scriptstyle { \mathbf { \mathcal { m } } } _ { \mathbf { n } }$ and $_ { m _ { n - 1 } }$ ；the motion of $\scriptstyle m _ { n - 8 }$ to a parallel system of axes with the origin at the center of mass of $m _ { n } , m _ { n - 1 }$ and $m _ { n - 2 } ,$ and continue in this way. Show that the results are the symmetrical equations

$$
\begin{array} { r l r l } & { \frac { \mu _ { n } } { \mu _ { n - 1 } } m _ { n - 1 } \frac { d ^ { 2 } x _ { n - 1 } } { d t ^ { 2 } } = \frac { \partial U } { \partial x _ { n - 1 } } , } & & { \mu _ { n } = m _ { n } , \qquad \mu _ { n - 1 } = m _ { n - 1 } + m _ { n } , } \\ & { \frac { \mu _ { n - 1 } } { \mu _ { n - 2 } } m _ { n - 2 } \frac { d ^ { 2 } x _ { n - 2 } } { d t ^ { 2 } } = \frac { \partial U } { \partial x _ { n - 2 } } , } & & { \mu _ { n - 1 } = m _ { n - 2 } + m _ { n - 1 } + m _ { n } , } \\ & { \vdots } & \\ & { \frac { \mu _ { 2 } } { \mu _ { 1 } } m _ { 1 } \frac { d ^ { 2 } x _ { 1 } } { d t ^ { 2 } } = \frac { \partial U } { \partial x _ { 1 } } , } & & { \mu _ { 1 } = m _ { 1 } + m _ { 2 } + \cdots + m _ { n } , } \end{array}
$$

.and similar equations in $\pmb { y }$ and $\pmb { z }$ where

$$
\begin{array} { r l } & { U = k ^ { 2 } m _ { n } \Big ( \frac { m _ { n - 1 } } { r _ { n , n - 1 } } + \frac { m _ { n - 2 } } { r _ { n , n - 2 } } + \cdots + \frac { m _ { 1 } } { r _ { n , 1 } } \Big ) } \\ & { \quad + k ^ { 2 } m _ { n - 1 } \Big ( \frac { m _ { n - 2 } } { r _ { n - 1 , n - 2 } } + \frac { m _ { n - 3 } } { r _ { n - 1 , n - 3 } } + \cdots + \frac { m _ { 1 } } { r _ { n - 1 , 1 } } \Big ) } \\ & { \quad \vdots } \\ & { \quad + k ^ { 2 } m _ { 2 } \frac { m _ { 1 } } { r _ { 1 , 2 } } . } \end{array}
$$

(These equations are the same as found by Radau from a different standpoint in the memoir cited in Art.150. They have been employed by Tisserand in a very elegant demonstration of Poisson's theorem of the invariability of the major axes of the planets'orbits up to perturbations of the second order inclusive with respect to the masses.Poincaré has generally used this system in his researches in the Problem of Three Bodies.)

4.Derive the differential equations corresponding to (23） in polar coordinates.

$$
\begin{array} { r l } & { [ \cfrac { d ^ { 2 } r _ { i , n } } { d t ^ { 2 } } - r _ { i , n } \cos ^ { 2 } \phi _ { i } \Big ( \cfrac { d \theta _ { j } } { d t } \Big ) ^ { 2 } - r _ { i , n } ( \cfrac { d \phi _ { i } } { d t } ) ^ { 2 } = - \cfrac { k ^ { 2 } ( m _ { j } + m _ { n } ) } { \tau _ { i , n } ^ { 2 } } + \sum _ { \ell = 1 } ^ { n - 1 } m _ { i } \cfrac { \partial R _ { j , i } } { \partial r _ { i , n } } , } \\ & { \cfrac { d } { d t } \Big ( \tau ^ { 2 } { _ i , n } \cos ^ { 2 } \phi _ { i } \cfrac { d \theta _ { j } } { d t } \Big ) = \displaystyle \sum _ { i = 1 } ^ { n - 1 } m _ { i } \cfrac { \partial R _ { i , i } } { \partial \theta _ { j } } , } \\ & { \cfrac { d } { d t } ( \tau ^ { 2 } { _ i , n } \cfrac { d \phi _ { j } } { d t } ) + \tau ^ { 2 } { _ i , n } \sin \phi _ { i } \cos \phi _ { i } \Big ( \cfrac { d \theta _ { j } } { d t } \Big ) ^ { 2 } = \displaystyle \sum _ { i = 1 } ^ { n - 1 } m _ { i } \cfrac { \partial R _ { j , i } } { \partial \phi _ { j } } , } \\ & { \cfrac { ( j = 1 , \dots , n - 1 ) , \ ( i + j ) } { \partial \theta _ { j } } . } \end{array}
$$

# HISTORICAL SKETCH AND BIBLIOGRAPHY.

The investigations in the Problem of $_ { n }$ Bodies are of two classes； first, those which lead to general theorems holding in every system；and second, those which give good approximations for a certain length of time in particular systems,such as the solar system.Investigations of the second class are known as theories of perturbations,the discussion of which will be given in another chapter.

The first general theorems are regarding the motion of the center of mass, and were given by Newton in the Principia. The ten integrals and the theorems to which they lead were known by Euler. The next general result was the proof of the existence and the discussion of the properties of the invariable plane by Laplace in 1784.In the winter semester of 1842-43 Jacobi gave a course of lectures in the University of Konigsberg on Dynamics. In this course he gave the results of some very important investigations on the integration of the differential equations which arise in Mechanics. In all cases where the forces depend upon the coordinates alone,and where a potential function exists,conditions which are fulfilled in the Problem of $_ n$ Bodies,he proved that if all the integrals except two have been found the last two can always be found.He also showed,in extending some investigations of Sir William Rowan Hamilton,that the problem is reducible to that of solving a partial differential equation whose order is one-half as great as that of the original system.Jacobi's lectures are published in the supplementary volume to his collected works. They are of great importance in themselves,as well as being an absolutely necessary prerequisite to the reading of the epoch-making memoirs of Poincaré,and they should be accessible to every student of Celestial Mechanics.

It isa question of the highest interest whether the motions of the members of such a system as the sun and planets are purely periodic. Newcomb has shown in an important memoir published in the Smithsonian Contributions to Knowledge,December 1874,that the differential equations can be formally Batisfied by purely periodic series.He did not,however,prove the convergence of these series；and,indeed,Poincaré has shown in Les Méthodes Nouvelles, chaps.Ix.and xil.,that they are in general divergent.

As was stated in Art.147,Bruns has proved in the Acta Mathematica vol.xi.,that,using rectangular coordinates,there are no new algebraic integrals;and Poincaré,in the Acta Mathematica, vol. xi1.,that,using the elements as variables,there are no new uniform transcendental integrals,even when the masses of all the bodies except one are very small.

For further reading regarding the general differential equations in different sets of variables the student will do well to consult Tisserand's Mécanique Celeste, vol.1. chapters I1.,Iv., and v.
