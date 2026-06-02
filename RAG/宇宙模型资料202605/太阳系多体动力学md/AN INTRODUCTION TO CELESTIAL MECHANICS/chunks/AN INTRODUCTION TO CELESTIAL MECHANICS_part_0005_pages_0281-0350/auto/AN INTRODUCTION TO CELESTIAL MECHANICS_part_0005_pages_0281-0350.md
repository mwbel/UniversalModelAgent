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

# CHAPTER VIII.

# THE PROBLEM OF THREE BODIES.

151.Problem Considered. There are a number of important results in the Problem of Three Bodies which have been established with mathematical rigor if the initial coordinates and the components of velocity fulfill certain special conditions. While these special cases have not been found in nature,there are nevertheless some applications of the results obtained，and the processes employed are mathematically elegant and lead to most interesting conclusions. This chapter will contain such of these results as fall within the scope of this work,reserving the theories of perturbations,by means of which the positions of the heavenly bodies are predicted, to subsequent chapters.

The first part of the chapter will be devoted to a discussion of some of the properties of motion of an infinitesimal body when it is attracted by two finite bodies which revolve in circles around their center of mass,and will include the proof of the existence of certain particular solutions in which the distances of the infinitesimal body from the finite bodies are constants. The second part of the chapter will be devoted to an exposition of a method of finding particular solutions of the motion of three finite bodies such that the ratios of their mutual distances are constants. These solutions include the former,but the discoverable properties of motion are so much fewer,and are obtained with so much more difficulty， that it is advisable to divide the discussion into two parts.

The particular solutions of the Problem of Three Bodies which will be discussed here were given for the first time by Lagrange in a prize memoir in 1772. The method adopted here is radically different from that employed by him,and lends itself much more readily to a generalization to the case where a larger number of bodies is involved. But,on the other hand, the reduction of the order of the problem by one unit,which was a very interesting feature of Lagrange's memoir,is not accomplished by this method. However,as it has not been possible to make any use of this reduction,it has not been of any practical importance.

Mathematically speaking,an infinitesimal body is one that is attracted by finite masses but does not attract them. Physically speaking,it is a body of such a small mass that it will disturb the motion of finite bodies less than an arbitrarily assigned amount, however small, during any arbitrarily assgned time, however long. To actually determine a small mass fulfilling these conditions it is only necessary to make it so small that its whole attraction, which is always greater than its disturbing force, on one of the large bodies,if placed at the minimum distance possible, would move the large body less than the assigned small distance in the assigned time.

MOTION OF THE INFINITESIMAL BODY.

152.The Differential Equations of Motion. Suppose the system consists of two finite bodies revolving in circles around their common center of mass,and of an infinitesimal body subject to their attraction. Let the unit of mass be so chosen that the sum of the masses of the finite bodies shall be unity; then they can be represented by $1 - \mu$ and $\pmb { \mu }$ ，where the notation is so chosen that $\mu \leq \frac { \mathtt { 1 } } { \mathtt { 2 } }$ .Let the unit of distance be so chosen that the constant distance between the finite bodies shall be unity. Let the unit of time be so chosen that $k ^ { 2 }$ shall equal unity. Let the origin of coordinates be taken at the center of mass of the finite bodies, and let the direction of the axes be so chosen that the $\xi \eta$ -plane is the plane of their motion.Let the coordinates of $1 - \mu , \mu _ { : }$ and the infinitesimal body be $\xi _ { 1 } , \eta _ { 1 } , 0 ; \xi _ { 2 } , \eta _ { 2 } , 0$ ; and $\xi , \eta , \xi$ respectively, and

$$
\begin{array} { c } { { r _ { 1 } = \sqrt { ( \xi - \xi _ { 1 } ) ^ { 2 } + ( \eta - \eta _ { 1 } ) ^ { 2 } + \zeta ^ { 2 } } , } } \\ { { r _ { 2 } = \sqrt { ( \xi - \xi _ { 2 } ) ^ { 2 } + ( \eta - \eta _ { 2 } ) ^ { 2 } + \zeta ^ { 2 } } . } } \end{array}
$$

Then the differential equations of motion for the infinitesimal body are

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } \xi } { d t ^ { 2 } } = - \left( 1 - \mu \right) \frac { \left( \xi - \xi _ { 1 } \right) } { { r _ { 1 } } ^ { 3 } } - \mu \frac { \left( \xi - \xi _ { 2 } \right) } { { r _ { 2 } } ^ { 3 } } , } \\ { \displaystyle \frac { d ^ { 2 } \eta } { d t ^ { 2 } } = - \left( 1 - \mu \right) \frac { \left( \eta - \eta _ { 1 } \right) } { { r _ { 1 } } ^ { 3 } } - \mu \frac { \left( \eta - \eta _ { 2 } \right) } { { r _ { 2 } } ^ { 3 } } , } \\ { \displaystyle \frac { d ^ { 2 } \xi } { d t ^ { 2 } } = - \left( 1 - \mu \right) \frac { \xi } { { r _ { 1 } } ^ { 3 } } - \mu \frac { \xi } { { r _ { 2 } } ^ { 3 } } . } \end{array} \right.
$$

As a consequence of the way the units have been chosen the mean angular motion of the finite bodies is

$$
n = k \frac { \sqrt { ( 1 - \mu ) + \mu } } { a ^ { 3 } } = 1 .
$$

Let the motion of the bodies be referred to a new system of axes having the same origin as the old, and rotating in the $\sum \eta -$ plane in the direction in which the finite bodies move with the uniform angular velocity unity. The coordinates in the new system are defined by the equations

$$
\left\{ \begin{array} { l l } { \xi = x \cos t - y \sin t , } \\ { \eta = x \sin t + y \cos t , } \\ { \zeta = z , } \end{array} \right.
$$

and similar equations for the letters with subscripts 1 and 2. On computing the second derivatives of (2) and substituting in (1), it is found that

$$
\begin{array} { r l } & { \left\{ \begin{array} { l l } { \left\{ \frac { d ^ { 2 } v } { d \theta ^ { 2 } } - 2 \frac { d y } { d \theta } - x \right\} \cos { t } - \left\{ \frac { d ^ { 2 } y } { d \theta ^ { 2 } } + 2 \frac { d z } { d t } - y \right\} \sin { t } } \\ { = - \left\{ \begin{array} { l l } { ( 1 - \mu ) \frac { ( x - x ) } { r ^ { 1 / 2 } } + \frac { y } { r ^ { 1 / 2 } } } \end{array} \right\} \cos { t } } \\ { \qquad + \left\{ ( 1 - \mu ) \frac { ( y - y ) } { r ^ { 1 / 3 } } + \frac { ( y - y ) } { r ^ { 1 / 3 } } \right\} \cos { t } } \end{array} \right. } \\ & { } \\ & { \left\{ \frac { d ^ { 2 } z } { d \theta ^ { 2 } } - 2 \frac { d y } { d t } - x \right\} \sin { t } + \left\{ \frac { d ^ { 3 } y } { d \theta ^ { 2 } } + 2 \frac { d z } { d t } - y \right\} \cos { t } } \\ { = - \left\{ ( 1 - \mu ) \frac { ( x - z ) } { r ^ { 1 / 3 } } + \mu \frac { ( x - x ) } { r ^ { 2 } } \right\} \sin { t } } \\ { \qquad - \left\{ ( 1 - \mu ) \frac { ( y - y ) } { r ^ { 1 / 3 } } + \mu \frac { ( y - y ) } { r ^ { 2 } } \right\} \cos { t } , } \end{array}
$$

Multiply the first two equations by cos $\mathbf { \Delta } _ { t }$ and sin $\pmb { \ell }$ respectively, then by - sin $\pmb { t }$ and cos $\mathbf { \Delta } _ { t }$ ,and add；the results are

$$
{ \left\{ \begin{array} { l l } { \displaystyle { \frac { d ^ { 2 } x } { d t ^ { 2 } } } - 2 { \frac { d y } { d t } } = x - ( 1 - \mu ) { \frac { ( x - x _ { 1 } ) } { { r _ { 1 } } ^ { 3 } } } - \mu { \frac { ( x - x _ { 2 } ) } { { r _ { 2 } } ^ { 3 } } } , } \\ { \displaystyle { \frac { d ^ { 2 } y } { d t ^ { 2 } } } + 2 { \frac { d x } { d t } } = y - ( 1 - \mu ) { \frac { ( y - y _ { 1 } ) } { { r _ { 1 } } ^ { 3 } } } - \mu { \frac { ( y - y _ { 2 } ) } { { r _ { 2 } } ^ { 3 } } } , } \\ { \displaystyle { \frac { d ^ { 2 } z } { d t ^ { 2 } } } \quad \quad \quad = } & { \displaystyle - ( 1 - \mu ) { \frac { z } { { r _ { 1 } } ^ { 3 } } } - \mu { \frac { z } { { r _ { 2 } } ^ { 3 } } } . } \end{array} \right. }
$$

The position of the axes can be so taken at the origin of time that the $_ x$ -axis will continually pass through the centers of the

finite bodies; then $y _ { 1 } = 0 , y _ { 2 } = 0$ ，and the equations become

$$
{ \left\{ \begin{array} { l l } { \displaystyle { \frac { d ^ { 2 } x } { d t ^ { 2 } } } - 2 { \frac { d y } { d t } } = x - ( 1 - \mu ) { \frac { ( x - x _ { 1 } ) } { { r _ { 1 } } ^ { 3 } } } - \mu { \frac { ( x - x _ { 2 } ) } { { r _ { 2 } } ^ { 3 } } } , } \\ { \displaystyle { \frac { d ^ { 2 } y } { d t ^ { 2 } } } + 2 { \frac { d x } { d t } } = y - ( 1 - \mu ) { \frac { y } { { r _ { 1 } } ^ { 3 } } } - \mu { \frac { y } { { r _ { 2 } } ^ { 3 } } } , } \\ { \displaystyle { \frac { d ^ { 2 } z } { d t ^ { 2 } } } \quad \quad \quad = \quad - ( 1 - \mu ) { \frac { z } { { r _ { 1 } } ^ { 3 } } } - \mu { \frac { z } { { r _ { 2 } } ^ { 3 } } } . } \end{array} \right. }
$$

These are the differential equations of motion of the infinitesimal body referred to axes rotating so that the finite bodies always lie on the $_ x$ -axis. They have the important property that they do not involve explicitly the independent variable $t$ because the coordinates of the finite bodies have become constants as a consequence of the particular manner in which the axes are rotated. On the other hand,in equations (1) the quantities $\xi _ { 1 } , \xi _ { 2 } , \eta _ { 1 } ,$ and $\eta _ { 2 }$ are functions of $t .$

The general problem of determining the motion of the infinitesimal body is of the sixth order;if it moves in the plane of motion of the finite bodies,the problem is of the fourth order.

153.Jacobi's Integral. Equations (4) admit an integral which was first given by Jacobi in Comptes Rendus de l'Académie des Sciences de Paris,vol.I1.,p.59,and which has been discussed by Hill in the first of his celebrated papers on the Lunar Theory, The American Journal of Mathematics,vol.1.,p.18,and again by Darwin in his memoir on Periodic Orbits in Acta Mathematica, vol. xx1., p.102.Let

$$
U = { \textstyle \frac { 1 } { 2 } } ( x ^ { 2 } + y ^ { 2 } ) + { \frac { ( 1 - \mu ) } { r _ { 1 } } } + { \frac { \mu } { r _ { 2 } } } ;
$$

then equations (4) can be written in the form

$$
\left\{ \begin{array} { l } { \displaystyle \frac { d ^ { 2 } x } { d t ^ { 2 } } - 2 \frac { d y } { d t } = \frac { \partial U } { \partial x } , } \\ { \displaystyle \frac { d ^ { 2 } y } { d t ^ { 2 } } + 2 \frac { d x } { d t } = \frac { \partial U } { \partial y } , } \\ { \displaystyle \frac { d ^ { 2 } z } { d t ^ { 2 } } \qquad = \frac { \partial U } { \partial z } . } \end{array} \right.
$$

If these equations are multiplied by $2 { \frac { d x } { d t } } , \ 2 { \frac { d y } { d t } }$ ，and $2 { \frac { d z } { d t } }$ respectively,and added, the resulting equation can be integrated,

since $U$ is a function of $x , y$ ,and $\pmb { \mathscr { z } }$ alone, and give

$$
\begin{array} { c } { \left( \frac { d x } { d t } \right) ^ { 2 } + \left( \frac { d y } { d t } \right) ^ { 2 } + \left( \frac { d z } { d t } \right) ^ { 2 } = V ^ { 2 } = 2 U - C } \\ { \equiv x ^ { 2 } + y ^ { 2 } + \frac { 2 ( 1 - \mu ) } { \lnot \mathrm { \Gamma } _ { 1 } } + \frac { 2 \mu } { r _ { 2 } } - C . } \end{array}
$$

Five integrals more are required in order completely to solve the problem.If the infinitesimal body moved in the $x y .$ -plane only three would remain to be found, the last two of which could be obtained by Jacobi's last multiplier,\* if the first one were found. Thus it appears that only one new integral is needed for the complete solution of this special problem in the plane.†But Bruns has proved in Acta Mathematica,vol. x1., that,when rectangular cordinates are used,no new algebraic integrals exist；and Poincaré has proved in Les Méthodes Nouvelles de la Mécanique Celeste, vol.I.,chap.v., that when the elements of the orbits are used as variables, there are no new uniform transcendental integrals, even when the mass of one of the finite bodies is very small compared to that of the other (see Art.147). These demonstrations are entirely outside the scope of this work and cannot be reproduced here.

154.The Surfaces of Zero Relative Velocity.t Equation （7) is a relation between the square of the velocity and the coordinates of the infinitesimal body referred to the rotating axes. Therefore, when the constant of integration $C$ has been determined numerically by the initial conditions,equation (7) determines the velocity with which the infinitesimal body will move,if at all,at all points of the rotating space；and conversely, for a given velocity,equation (7） gives the locus of those points of relative space where alone the infinitesimal body can be. In particular,if $V$ is put equal to zero in this equation it wil define the surfaces at which the velocity will be zero. On one side of these surfaces the velocity will be real and on the other side imaginary；or,in other words,it is

\* Developed in Vorlesungen iber Dynamik， supplementary volume to Jacobi's collected works.

$^ { \dagger }$ Hill put his special equations in such a form that they would be reduced to quadratures if a single variable were expressed in terms of the time,American Journal of Mathemalics,vol.1.,p.16.

$\ddagger$ First discussed by Hill in his Lunar Theory，The American Journal of Mathematics,vol.1.;and again,for motion in the xy-plane,by Darwin in his Periodic Orbits,in Acta Mathematica,vol.xx1.

possible for the body to move on one side,and impossible for it to move on the other. The general proposition that a function changes sign as the surface at which it is zero is crossed (at least at a regular point of the surface) was proved in Art.120. While it will not be possible to say in any except very particular cases what the orbit will be,yet this partition of relative space will show in what portions the infinitesimal body can move and in what portions it can not.

The equation of the surfaces of zero relative velocity is

$$
\left\{ \begin{array} { l l } { \displaystyle x ^ { 2 } + y ^ { 2 } + \frac { 2 ( 1 - \mu ) } { r _ { 1 } } + \frac { 2 \mu } { r _ { 2 } } = C , } \\ { \displaystyle r _ { 1 } = \sqrt { ( x - x _ { 1 } ) ^ { 2 } + y ^ { 2 } + z ^ { 2 } } , } \\ { \displaystyle r _ { 2 } = \sqrt { ( x - x _ { 2 } ) ^ { 2 } + y ^ { 2 } + z ^ { 2 } } . } \end{array} \right.
$$

Since only the squares of $\pmb { y }$ and $\pmb { z }$ occur the surfaces defined by (8) are symmetrical with respect to the xy and $\pmb { x } \pmb { z }$ -planes,and,when $\begin{array} { r } { \mu = \frac { 1 } { 2 } . } \end{array}$ ，with respect to the $_ { y z }$ -plane also. The surfaces for $\mu \neq \frac { 1 } { 2 }$ can be regarded as being deformations of those for $\begin{array} { r } { \mu = \frac { 1 } { 2 } } \end{array}$ It follows from the way in which $\pmb { \mathscr { z } }$ enters that a line parallel to the ${ \pmb z } .$ -axis pierces the surfaces in two (or no) real points. Moreover, the surfaces are contained within a cylinder whose axis is the ${ \pmb z }$ -axis and whose radius is $\sqrt { C }$ ，to which certain of the folds are asymptotic at $z ^ { 2 } = \infty$ ; for, as $z ^ { 2 }$ increases the equation approaches as a limit

$$
x ^ { 2 } + y ^ { 2 } = C .
$$

155. Approximate Forms of the Surfaces. From the properties of the surfaces given in the preceding article and from the shapes of the curves in which the surfaces intersect the reference planes, a general idea of their form can be obtained. The equation of the curves of intersection of the surfaces with the xy-plane is obtained byputting $\pmb { z }$ equal to zero in the frst of (8),and is

$$
x ^ { 2 } + y ^ { 2 } + { \frac { 2 ( 1 - \mu ) } { \sqrt { ( x - x _ { 1 } ) ^ { 2 } + y ^ { 2 } } } } + { \frac { 2 \mu } { \sqrt { ( x - x _ { 2 } ) ^ { 2 } + y ^ { 2 } } } } = C .
$$

For large values of $_ { \pmb { x } }$ and $y$ which satisfy this equation the third and fourth terms are relatively unimportant, and the equation may be written

$$
x ^ { 2 } + y ^ { 2 } = C - { \frac { 2 ( 1 - \mu ) } { \sqrt { ( x - x _ { 1 } ) ^ { 2 } + y ^ { 2 } } } } - { \frac { 2 \mu } { \sqrt { ( x - x _ { 2 } ) ^ { 2 } + y ^ { 2 } } } } = C - \epsilon ,
$$

where $\epsilon$ is a small quantity. This is the equation of a circle whose radius is $\sqrt { C - \epsilon } ,$ therefore,one branch of the curve in the xyplane is an approximately circular oval within the asymptotic cylinder. It is also to be noted that the larger $\boldsymbol { c }$ is,the larger are the values of $_ { \pmb { x } }$ and $y$ which satisfy the equation,the smaller is $\epsilon _ { i }$ the more nearly circular is the curve,and the more nearly does it approach its asymptotic cylinder.

![](images/b68a5ac6889ad5d5899171cce72c6c6accb1bbc1ce9eb0190b036de076dec960.jpg)  
Fig. 38.

For small values of $\pmb { x }$ and $_ y$ satisfying (9) the first and second terms are relatively unimportant，and the equation may be written

$$
{ \frac { 1 - \mu } { r _ { 1 } } } + { \frac { \mu } { r _ { 2 } } } = { \frac { C } { 2 } } - { \frac { x ^ { 2 } + y ^ { 2 } } { 2 } } = { \frac { C } { 2 } } - \epsilon .
$$

This is the equation of the equipotential curves\* for the two centers of force, $1 - \mu$ and $\pmb { \mu }$ For large values of $\boldsymbol { C }$ they consist of closed ovals around each of the bodies $1 - \mu$ and $\pmb { \mu }$ ; for smaller values of $\boldsymbol { c }$ these ovals unite between the bodies forming a dumbbell shaped figure in which the ends are of different size except when $\begin{array} { r } { \mu = \frac { 1 } { 2 } } \end{array}$ ； and for still smaller values of $\boldsymbol { c }$ the handle of the dumb-bell enlarges until the figure becomes an oval enclosing both of the bodies

From the foregoing considerations it follows that the approximate forms of the curves in which the surfaces intersect the xyplane are as given in Fig.38. The curves $C _ { 1 } , C _ { 2 } , C _ { 3 } , C _ { 4 } , C _ { 5 }$ are in the order of decreasing values of the constant $\boldsymbol { C }$ .They were not drawn from numerical calculations and are intended to show only qualitatively the character of the curves.

![](images/a2fe9d9f28842e4302f067983dca971916a5d50498aae668fa18e4c271d92719.jpg)  
Fig.39.

The equation of the curves of intersection of the surfaces and the $\pmb { x } \pmb { \mathcal { z } }$ -plane is obtained by putting $_ y$ equal to zero in equation (8),and is

$$
x ^ { 2 } + { \frac { 2 ( 1 - \mu ) } { \sqrt { ( x - x _ { 1 } ) ^ { 2 } + z ^ { 2 } } } } + { \frac { 2 \mu } { \sqrt { ( x - x _ { 2 } ) ^ { 2 } + z ^ { 2 } } } } = C .
$$

For large values of $x$ and $z$ satisfying this equation the second

and third terms are relatively unimportant, and it may be writen

$$
x ^ { 2 } = C - \epsilon ,
$$

which is the equation of a symmetrical pair of straight lines parallel to the ${ \pmb z } .$ -axis. The larger $C$ is, the larger is the value of $_ x$ which,for a given value of $\pmb { z }$ ,satisfies the equation,and, therefore, the smaller is ε.Hence,the larger $c$ the closer the lines are to the asymptotic cylinder.

![](images/5e1e3cf373dc65750a45beb47909326b15f9175a460acdfcd78ad89c6c16819a.jpg)  
Fig. 40.

For small values of $_ { \pmb { x } }$ and $\pmb { z }$ satisfying equation (10) the first term is relatively unimportant,and the equation may be written

$$
{ \frac { 1 - \mu } { r _ { 1 } } } + { \frac { \mu } { r _ { 2 } } } = { \frac { C } { 2 } } - \epsilon .
$$

This is again the equation of the equipotential curves and has the same properties as before. Hence, the forms of the curves in the $\pmb { x } \pmb { z }$ -plane are qualitatively like those given in Fig.39. Again, the curves $C _ { 1 } , \cdots , C _ { 5 }$ are in the order of decreasing values of the constant $\boldsymbol { C }$ ,and were not drawn from numerical calculations.

The equation of the curves of intersection of the surfaces and the yz-plane is obtained by putting $\pmb { x }$ equal to zero in equation (8),and is

$$
y ^ { 2 } + { \frac { 2 ( 1 - \mu ) } { \sqrt { { x _ { 1 } } ^ { 2 } + y ^ { 2 } + z ^ { 2 } } } } + { \frac { 2 \mu } { \sqrt { { x _ { 2 } } ^ { 2 } + y ^ { 2 } + z ^ { 2 } } } } = C .
$$

For large values of $\pmb { y }$ and $\pmb { \mathscr { z } }$ satisfying this equation the second and third terms are relatively unimportant,and it may be written

$$
y ^ { 2 } = C - \epsilon ,
$$

which is the equation of a pair of lines near the asymptotic cylider, approaching it as $c$ increases.

If $1 - \mu$ is much greater than $\pmb { \mu } _ { : }$ ，the numerical value of ${ \pmb x } _ { 2 }$ is much greater than that of $x _ { 1 }$ ； hence, for small values of $\pmb { y }$ and $\pmb { z }$ satisfying (11), this equation may be written

$$
\frac { 2 ( 1 - \mu ) } { r _ { 1 } } = C - \epsilon ,
$$

which is the equation of a circle which becomes larger as $c$ decreases. Hence,the forms of the curves in the yz-plane are qualitatively as given in Fig.40. Again,the curves $C _ { 1 } , \cdots , C _ { 5 }$ are in the order of decreasing values of the constant $\boldsymbol { C }$

From these three sections of the surfaces it is easy to infer their forms for the different values of $c$ .They may be roughly described as consisting of, for large values of $c$ ,a closed fold approximately spherical in form around each of the finite bodies,and of curtains hanging from the asymptotic cylinder symmetrically with respect to the xy-plane; for smaller values of $\boldsymbol { C }$ ，the folds expand and coalesce (Fig. 38,curve $C _ { 3 , }$ ；for still smaller values of $\boldsymbol { c }$ the united folds coalesce with the curtains,the first points of contact being in every case in the $\boldsymbol { x } \boldsymbol { y }$ -plane；and for suffciently small values of $\boldsymbol { c }$ the surfaces consist of two parts symmetrical with respect to the xy-plane but not intersecting it (Figs.39, curve ${ \cal C } _ { 5 } ,$ and 40,curve $C _ { 6 , }$ .

156. The Regions of Real and Imaginary Velocity. Having determined the forms of the surfaces,it remains to find in what regions of relative space the motion is real and in what it is imaginary. The equation for the square of the velocity is

$$
V ^ { 2 } = x ^ { 2 } + y ^ { 2 } + { \frac { 2 ( 1 - \mu ) } { r _ { 1 } } } + { \frac { 2 \mu } { r _ { 2 } } } - C .
$$

Suppose $\boldsymbol { c }$ is so large that the ovals and curtains are al separate.

The motion will be real in those portions of relative space for which the right member of this equation is positive. If it is positive in one point in a closed fold it will be positive in every other point within it,for the function changes sign only at a surface of zero relative velocity.

It is evident from the equation that $\pmb { x }$ and $_ y$ can be taken so large that the right member will be positive,however great $c$ may be;therefore, the motion is real outside of the curtains. It is also clear that a point can be chosen so near to either ${ \bf l } - \mu$ or $\pmb { \mu }$ ,that is,either $\pmb { r } _ { 1 }$ or $\pmb { r _ { 2 } }$ may be taken so small, that the right member will be positive,however great $c$ may be; therefore,the motion is real within the folds around the finite bodies.

If the value of $\boldsymbol { c }$ were so large that the folds around the finite bodies were closed,and if the infinitesimal body should be within one of these folds at the origin of time,it would always remain there since it could not cross a surface of zero velocity. If the earth's orbit is supposed to be circular and the mass of the moon infinitesimal,it is found that the constant $c$ ，determined by the motion of the moon,is so large that the fold around the earth is closed with the moon within it. Therefore the moon cannot recede indefinitely from the earth. It was in this manner，and with these approximations,that Hill proved that the moon's distance from the earth has a superior limit.\*

157.Method of Computing the Surfaces. Actual points on the surfaces can be found most readily by first determining the curves in the xy-plane,and then finding by methods of approximation the values of $z$ which satisfy (7). Besides, the curves in the $\boldsymbol { x y }$ -plane are of most interest because the first points of contact as the various folds coalesce occur in this plane,and,indeed,on the $\pmb { x }$ -axis,as can be seen from the symmetries of the surfaces.

The equation of the curves in the $\pmb { x y }$ -plane is

$$
x ^ { 2 } + y ^ { 2 } + { \frac { 2 ( 1 - \mu ) } { \sqrt { ( x - x _ { 1 } ) ^ { 2 } + y ^ { 2 } } } } + { \frac { 2 \mu } { \sqrt { ( x - x _ { 2 } ) ^ { 2 } + y ^ { 2 } } } } = C .
$$

If this equation is rationalized and cleared of fractions the result is a polynomial of the sixteenth degree in $_ x$ and $y$ .When the value of one of the variables is taken arbitrarily the corresponding values of the other can be found by solving this rationalized equation. This problem presents great practical difficulties because of the high degree of the equation，and these troubles are supplemented by the presence of foreign solutions which are introduced by the processes of rationalization.

The diffculty from foreign solutions can be avoided entirely, and the degree of the equation can be very much reduced by transforming to bi-polar coordinates. That is，points on the curves can be defined by giving their distances from two fixed points on the $_ x$ -axis. This method could not be applied if the curves were not symmetrical with respect to the axis on which the poles lie.Let the centers of the bodies $1 - \mu$ and $\pmb { \mu }$ be taken as the poles; the distances from these points are $\boldsymbol { r } _ { 1 }$ and $\boldsymbol { r _ { 2 } }$ respectively. To complete the transformation it is only necessary to express $x ^ { 2 } + y ^ { 2 }$ in terms of these quantities.

![](images/e6879a4d05c228e0a040f1a06b634d349d668d784b03ac6b8fa6dbd64ac3b816.jpg)  
Fig. 41.

Let $P$ be a point on one of the curves; then $O A = x , A P = y .$ and，since $O$ is the center of mass of $1 - \mu$ and $\pmb { \mu }$ $\widetilde { O \mu } = 1 - \mu ;$ and $\overline { { \mathcal { O } ( 1 - \mu ) } } = - \mu ,$ 、It follows that

$$
\left\{ \begin{array} { l l } { y ^ { 2 } = r _ { 1 } { } ^ { 2 } - ( x + \mu ) ^ { 2 } = r _ { 1 } { } ^ { 2 } - x ^ { 2 } - 2 \mu x - \mu ^ { 2 } , } \\ { y ^ { 2 } = r _ { 2 } { } ^ { 2 } - [ x - ( 1 - \mu ) ] ^ { 2 } = r _ { 2 } { } ^ { 2 } - x ^ { 2 } + 2 ( 1 - \mu ) x - ( 1 - \mu ) ^ { 2 } . } \end{array} \right.
$$

On eliminating the first power of $_ x$ from these equations and solving for $x ^ { 2 } + y ^ { 2 }$ ,it is found that

$$
x ^ { 2 } + y ^ { 2 } = ( 1 - \mu ) { r _ { 1 } } ^ { 2 } + \mu { r _ { 2 } } ^ { 2 } - \mu ( 1 - \mu ) .
$$

As a consequence of this equation, (9) becomes

$$
( 1 - \mu ) \left[ r _ { 1 } { } ^ { 2 } + { \frac { 2 } { r _ { 1 } } } \right] + \mu \left[ r _ { 2 } { } ^ { 2 } + { \frac { 2 } { r _ { 2 } } } \right] = C + \mu ( 1 - \mu ) = C ^ { \prime } .
$$

If an arbitrary value of $\pmb { r _ { 2 } }$ is assumed $\boldsymbol { r } _ { 1 }$ can be computed from this equation；the points of intersection of the circles around $1 - \mu$ and $\pmb { \mu }$ as centers,with the computed and assumed values respectively of $r _ { 1 }$ and $r _ { 2 }$ as radii,will be points on the curves. To follow out this plan,let equation (12)be written in the form

$$
\left\{ \begin{array} { l l } { r _ { 1 } { ^ 3 } + a r _ { 1 } + b = 0 , } \\ { a = - \displaystyle \frac { C ^ { \prime } } { 1 - \mu } + \frac { \mu } { 1 - \mu } \left[ r _ { 2 } { ^ 2 } + \displaystyle \frac { 2 } { r _ { 2 } } \right] , } \\ { b = 2 . } \end{array} \right.
$$

Since $b = 2$ is positive there is at least one real negative root of the first of (13) whatever value $a$ may have. But the only value of $r _ { 1 }$ which has a meaning in this problem is real and positive; hence the condition for real positive roots must be considered.

It follows from (12) that $C ^ { \prime }$ is always greater than $\mu \left[ r _ { 2 } { } ^ { 2 } + \frac { 2 } { r _ { 2 } } \right]$ for all real positive values of $r _ { 1 }$ and $r _ { 2 }$ ; therefore $^ { a }$ is always negative. It is shown in the Theory of Equations that a cubic equation of this form has three distinct real roots if $2 7 b ^ { 2 } + 4 a ^ { 3 } < 0$ ； or,since $b = 2$ ,if

$$
a + 3 < 0 .
$$

Suppose this inequality is satisfied. Then a convenient method of solving the cubic is

$$
\left\{ \begin{array} { l l } { \sin \theta = \displaystyle \frac { b } { 2 } \sqrt { \frac { 2 7 } { - a ^ { 3 } } } , \quad \theta \leq \displaystyle \frac { \pi } { 2 } , } \\ { r _ { 1 1 } = 2 \sqrt { \frac { - a } { 3 } } \sin \frac \theta 3 , } \\ { r _ { 1 2 } = 2 \sqrt { \frac { - a } { 3 } } \sin \left( 6 0 ^ { \circ } - \frac \theta 3 \right) , } \\ { r _ { 1 3 } = - 2 \sqrt { \frac { - a } { 3 } } \sin \left( 6 0 ^ { \circ } + \frac \theta 3 \right) , } \end{array} \right.
$$

where $r _ { 1 1 } , r _ { 1 2 } , r _ { 1 3 }$ are the three roots of the cubic.

The limit of the inequality (14) is $a + 3 = 0$ ; or, in terms of the original quantities,

$$
\left\{ \begin{array} { l l } { \displaystyle r _ { 2 } ^ { 2 } + a ^ { \prime } r _ { 2 } + b ^ { \prime } = 0 , } \\ { \displaystyle a ^ { \prime } = - \frac { C ^ { \prime } } { \mu } + \frac { 3 ( 1 - \mu ) } { \mu } , } \\ { \displaystyle b ^ { \prime } = 2 . } \end{array} \right.
$$

The solution of this equation gives the extreme values of $\pmb { r _ { 2 } }$ for which (13) has real roots. Therefore,in the actual computation equation (16) should be solved first for $\boldsymbol { r } _ { 2 1 }$ and $\boldsymbol { r } _ { 2 2 }$ .The values of

$\pmb { \ell _ { 2 } }$ to be substituted in (13) should be chosen at convenient intervals between these roots.

Equation (16) will not have real positive roots for all values of a', the condition for real positive roots being

$$
a ^ { \prime } + 3 \leq 0 ;
$$

the limiting value of which is,in the original quantities,

$$
- \frac { C ^ { \prime } } { \mu } + \frac { 3 ( 1 - \mu ) } { \mu } = - \ 3 ;
$$

whence

$$
C ^ { \prime } = 3 .
$$

Therefore $C ^ { \prime }$ must be equal to,or greater than,3 in order that thc curves shall have real points in the xy-plane. For $C ^ { \prime } = 3$ the curves are just vanishing from the plane,and it follows at once that equation (12) is then satisfied by $r _ { 1 } = 1$ ， $r _ { 2 } = 1$ ; that is,the surfaces vanish from the $\boldsymbol { x y }$ -plane at the points which form equilateral triangles with $1 - \mu$ and $\pmb { \mu }$

158.Double Points of the Surfaces and Particular Solutions of the Problem of Three Bodies. It follows from the general forms of the surfaces that the double points which appear as $c$ diminishes are all in the xy-plane. Therefore it is sufficient in this discussion to consider the equation of the curves in the xy-plane. There are three double points on the $_ { \pmb { x } }$ -axis which appear when the ovals around the finite bodies touch each other and when they touch the exterior curve enclosing them both. There are two more which appear,as the surfaces vanish from the xy-plane,at the two points making equilateral triangles with the finite bodies.

These double points are of interest as critical points of the curves,and it will now be shown that they are connected with important dynamical properties of the system. Let the.equation of the curves be written

$$
F ( x , y ) \equiv x ^ { 2 } + y ^ { 2 } + { \frac { 2 ( 1 - \mu ) } { r _ { 1 } } } + { \frac { 2 \mu } { r _ { 2 } } } - C = 0 .
$$

The conditions for double points are

$$
{ \left\{ \begin{array} { l l } { { \displaystyle { \frac { 1 } { 2 } } } { \frac { \partial F } { \partial x } } \equiv x - ( 1 - \mu ) { \frac { ( x - x _ { 1 } ) } { { r _ { 1 } } ^ { 3 } } } - \mu { \frac { ( x - x _ { 2 } ) } { { r _ { 2 } } ^ { 3 } } } = 0 , } \\ { { \displaystyle { \frac { 1 } { 2 } } { \frac { \partial F } { \partial y } } \equiv y - ( 1 - \mu ) { \frac { y } { { r _ { 1 } } ^ { 3 } } } - \mu { \frac { y } { { r _ { 2 } } ^ { 3 } } } = 0 . } } \end{array} \right. }
$$

The left members of these equations are the same as the right members of the equations (4)for $z = 0$ The expressions $\frac { 1 } { 2 } \frac { \partial F } { \partial x }$ and $\frac { 1 } { 2 } ~ \frac { \partial F } { \partial y }$ areoprtitl t alloriypntsofturvedice $\frac { d x } { d t }$ and $\frac { d y } { d t }$ are zero at the surfaces of zero velocity it follows from (4) that the directions of acceleration，or the lines of effective force，are orthogonal to the surfaces of zero relative velocity. Therefore,if the infinitesimal body is placed on a surface of zero relative velocity it will start in its motion in the direction of the normal. But at the double points the sense of the normal becomes ambiguous; hence,it might be surmised that if the infinitesimal body were placed at one of these points it would remain relatively at rest.

The conditions imposed by (17) and (18) are also the conditions that $\frac { d ^ { 2 } x } { d t ^ { 2 } }$ and d，orthecomponntsofaeleratin,inatios (4) shall vanish.Hence,if the infinitesimal body is placed at a double point with zero relative velocity,its ooordinates will identically fulfill the differential equations of motion and it will remain forever relatively at rest,unless disturbed by forces exterior to the system under consideration. These are particular solutions of the Problem of Three Bodies,and are special cases of the Lagrangian solutions.

Consider equations (18),the second of which is satisfied by $y = 0$ ：The double points on the $_ { x }$ -axis,and the straight line solutions of the problem are given by the conditions

$$
\left\{ \begin{array} { l l } { x - ( 1 - \mu ) { \frac { ( x - x _ { 1 } ) } { [ ( x - x _ { 1 } ) ^ { 2 } ] ^ { \sharp } } } - \mu { \frac { ( x - x _ { 2 } ) } { [ ( x - x _ { 2 } ) ^ { 2 } ] ^ { \sharp } } } = 0 , } \\ { y = 0 , } \\ { z = 0 . } \end{array} \right.
$$

The left member of the first equation considered as a function of $_ x$ is positive for $x = + \infty$ ; it is negative for ${ \mathfrak { x } } = { \mathfrak { x } } _ { 2 } + \epsilon _ { \mathfrak { z } }$ where e is a very small positive quantity; it is positive for $x = x _ { 2 } - \epsilon ;$ it is negative for ${ \pmb x } = { \pmb x } _ { 1 } + { \pmb \epsilon } _ { 3 }$ it is positive for ${ \pmb x } = { \pmb x } _ { 1 } - { \pmb \epsilon } _ { 2 }$ and it is negative for $x = - \infty$ . Since the function is finite and continuous except when $x = + \infty$ ，x2， ${ \pmb x } _ { 1 } .$ or $- \infty$ ，it follows that the function changes sign three times by passing through zero, $( a )$ once between $+ \infty$ and ${ \boldsymbol { \mathscr { x } } } _ { 2 }$ ， $( b )$ once between $\pmb { x _ { 2 } }$ and $\pmb { x } _ { 1 }$ and $( c )$ once between $\pmb { x _ { 1 } }$ and $- \infty$ ．Therefore, there are three positions on the line through $1 - \mu$ and $\pmb { \mu }$ at which the infinitesimal body will remain when given proper initial projection.

$( a )$ Let the distance from $\pmb { \mu }$ to the double point on the $x \cdot$ -axis between $+ \infty$ and $x _ { 2 }$ be represented by $\rho$ “Then $x - x _ { 2 } = \rho _ { ; }$ $x - x _ { 1 } = r _ { 1 } = 1 + \rho , x = 1 - \mu + \rho$ ；therefore the first equation of (19) becomes after clearing of fractions

$$
\rho ^ { 5 } + ( 3 - \mu ) \rho ^ { 4 } + ( 3 - 2 \mu ) \rho ^ { 3 } - \mu \rho ^ { 2 } - 2 \mu \rho - \mu = 0 .
$$

This quintic equation has one variation in the sign of its coefficients,and hence only one real positive root. The value of this root depends upon $\pmb { \mu }$ ，Consider the left member of the equation as a function of $\pmb { \rho }$ and $\mu$ For $\mu = 0$ the equation becomes

$$
\rho ^ { 3 } ( \rho ^ { 2 } + 3 \rho + 3 ) = 0 ,
$$

which has three roots $\rho = 0$ ，and two others,coming from the second factor，which are complex. It follows from the theory of the solution of algebraic equations that,for $\mu$ different from zero but sufficiently small, three roots of the equation are expressible as power series in $\mu ^ { \sharp }$ ，vanishing with this parameter.\* The one of these three roots obtained by taking the real value of $\mu ^ { \frac { 1 } { 8 } }$ is real; the other two are complex. Therefore, the real root has the form

$$
\rho = a _ { 1 } \mu ^ { \ddag } + a _ { 2 } \mu ^ { \ddag } + a _ { 3 } \mu ^ { \ddag } + \cdots .
$$

On substituting this expression for $\pmb { \rho }$ in (20) and equating to zero the coefficients of corresponding powers of $\mu ^ { \tt t }$ ,it is found that

$$
a _ { 1 } = { \frac { 3 ^ { \dagger } } { 3 } } , \qquad a _ { 2 } = { \frac { 3 ^ { \dagger } } { 9 } } , \qquad a _ { 3 } = - { \frac { 1 } { 2 7 } } , \qquad \cdots .
$$

Hence

$$
\{ r _ { 2 } = \rho = ( \frac { \mu } { 3 } ) ^ { \tt t } + \frac { 1 } { 3 } ( \frac { \mu } { 3 } ) ^ { \tt t } - \frac { 1 } { 9 } ( \frac { \mu } { 3 } ) ^ { \tt t } + \cdots ,
$$

The corresponding value of $C ^ { \prime }$ is found by substituting these values of $\boldsymbol { r } _ { 1 }$ and $\pmb { r _ { 2 } }$ in equation (12).

$( b )$ Let the distance from $\mu$ to the double point on the $_ x$ axis between $x _ { 2 }$ and $x _ { 1 }$ be represented by $\pmb { \rho }$ .Then in this case $x - x _ { 2 } = - \rho , \ x - x _ { 1 } = r _ { 1 } = 1 - \rho , \ x = ( 1 - \mu )$ $x = ( 1 - \mu ) - \rho$ ；therefore the first equation of (19) becomes

$$
\rho ^ { 5 } - ( 3 - \mu ) \rho ^ { 4 } + ( 3 - 2 \mu ) \rho ^ { 3 } - \mu \rho ^ { 2 } + 2 \mu \rho - \mu = 0 .
$$

\* See Harkness and Morley's Theory of Functions,chapter Iv.

On solving as in $( a )$ , the values of $\mathbf { \boldsymbol { r } _ { 2 } }$ and $r _ { 1 }$ are found to be

$$
\left\{ \begin{array} { l l } { { r _ { 2 } = \rho = \left( \frac { \mu } { 3 } \right) ^ { \frac { 1 } { 3 } } - \frac { 1 } { 3 } \left( \frac { \mu } { 3 } \right) ^ { \frac { 1 } { 3 } } - \frac { 1 } { 9 } \left( \frac { \mu } { 3 } \right) ^ { \frac { 3 } { 3 } } + \cdots , } } \\ { { \hfill } } \\ { { r _ { 1 } = 1 - \rho . } } \end{array} \right.
$$

The corresponding value of $C ^ { \prime }$ is found by substituting these values of $r _ { 1 }$ and $r _ { 2 }$ in equation (12).

(c）Let the distance from $1 - \mu$ to the double point on the $x \cdot$ -axis between $\pmb { x _ { 1 } }$ and $- \infty$ be represented by $1 - \rho$ .In this case $x - x _ { 2 } = - 2 + \rho ,$ $x - x _ { 1 } = - 1 + \rho _ { : }$ ， $x = - \ \mu - 1 + \rho ,$ and the first equation of (19) becomes

$$
\begin{array} { c } { { \rho ^ { 5 } - ( 7 + \mu ) \rho ^ { 4 } + ( 1 9 + 6 \mu ) \rho ^ { 3 } - ( 2 4 + 1 3 \mu ) \rho ^ { 2 } } } \\ { { { } } } \\ { { { } + ( 1 2 + 1 4 \mu ) \rho - 7 \mu = 0 . } } \end{array}
$$

When $\mu = 0$ this equation becomes

$$
\rho ^ { 5 } - 7 \rho ^ { 4 } + 1 9 \rho ^ { 3 } - 2 4 \rho ^ { 2 } + 1 2 \rho = 0 ,
$$

which has but one root $\rho = 0$ .Therefore $\rho$ can be expressed as a power series in $\pmb { \mu }$ which converges for sufficiently small values of this parameter,and vanishes with it. This root will have the form

$$
\rho = c _ { 1 } \mu + c _ { 2 } \mu ^ { 2 } + c _ { 3 } \mu ^ { 3 } + c _ { 4 } \mu ^ { 4 } + \cdots .
$$

On substituting this expression for $\rho$ in (23),and equating to zero the coefficients of the various powers of $\mu$ ,it is found that

$$
c _ { 1 } = { \frac { 7 } { 1 2 } } , \qquad c _ { 2 } = 0 , \qquad c _ { 3 } = { \frac { 2 3 \times 7 ^ { 2 } } { 1 2 ^ { 4 } } } ,
$$

Hence

$$
\left\{ \begin{array} { l l } { \rho = \displaystyle \frac { 7 } { 1 2 } \mu + \frac { 2 3 \times 7 ^ { 2 } } { 1 2 ^ { 4 } } \mu ^ { 3 } + \cdots , } \\ { r _ { 1 } = 1 - \rho , } \\ { r _ { 2 } = 1 + r _ { 1 } = 2 - \rho . } \end{array} \right.
$$

The corresponding value of $C ^ { \prime }$ is found by substituting these values of $r _ { 1 }$ and $\mathbf { \boldsymbol { r } _ { 2 } }$ in equation (12).

If the values of $r _ { 1 }$ and $r _ { 2 }$ given by the first three terms of the series (21)， (22)，and (24) are not suffciently accurate，more nearly correct values should be found by differential corrections.

In order to find the double points not on the $_ x$ -axis consider equations (18） again. They，or any two independent functions of them, define the double pcints.Since $y$ is distinct from zero in this case the second equation may be divided by it, giving

$$
\mathbf { 1 } - { \frac { 1 - \mu } { \left. r _ { 1 } \right. ^ { 3 } } } - { \frac { \mu } { \left. r _ { 2 } \right. ^ { 3 } } } = 0 .
$$

Multiply this equation by ${ \boldsymbol { x } } - { \boldsymbol { x } } _ { 2 }$ and ${ \boldsymbol { x } } - { \boldsymbol { x } } _ { 1 } ,$ and subtract the products separately from the first of (18). The results are

$$
\left\{ \begin{array} { r } { x _ { 2 } - \left( 1 - \mu \right) \displaystyle \frac { \left( x _ { 2 } - x _ { 1 } \right) } { { r _ { 1 } } ^ { 3 } } = 0 , } \\ { x _ { 1 } - \mu \displaystyle \frac { \left( x _ { 1 } - x _ { 2 } \right) } { { r _ { 2 } } ^ { 3 } } = 0 , } \\ { z = 0 . } \end{array} \right.
$$

But $x _ { 2 } = 1 - \mu , $ ${ \boldsymbol { \mathscr { x } } } _ { 1 } = { \boldsymbol { \mathscr { - } } } \ { \boldsymbol { \mu } } _ { : }$ and $x _ { 2 } - x _ { 1 } = 1$ ；therefore these equations reduce to

$$
\left\{ { \begin{array} { r } { 1 - { \frac { 1 } { { r _ { 1 } } ^ { 3 } } } = 0 , } \\ { - 1 + { \frac { 1 } { { r _ { 2 } } ^ { 3 } } } = 0 , } \\ { z = 0 . } \end{array} } \right.
$$

The only real solutions are $r _ { 1 } = 1 , r _ { 2 } = 1 _ { ; }$ ，and the points form equilateral triangles with the finite bodies whatever their relative masses may be. As was shown in the last of Art. 157, they occur at the places where the surfaces vanish from the xy-plane.

# XX. PROBLEMS.

1.The units defined in Art.152 are called canonical units；what would the canonical unit of time be in days for the earth and sun?

2.Show on á priori grounds that,when the motion of the system is referred to axes rotating as in Art.152,the differential equations should not involve the time explicitly.

3.Why cannot an integral corresponding to (7) be derived from equations (1）at once without any transformations? Prove that there is an integral of (1).

4.What are the surfaces of zero velocity for a body projected vertically upward against gravity? For a body moving subject to a central force varying inversely as the square of the distance?

5.Show by direct reductions from (13)and (14) that

$$
( r _ { 1 } - r _ { 1 1 } ) ( r _ { 1 } - r _ { 1 2 } ) ( r _ { 1 } - r _ { 1 3 } ) \equiv r _ { 1 } { } ^ { 3 } + a r _ { 1 } + b = 0 .
$$

6.Prove that the solution of (16) gives the extreme values of $\pmb { r _ { 2 } }$ for which (14) has real roots. Hint. Consider the graph of $y = r _ { 2 } { } ^ { 3 } + a ^ { \prime } r _ { 2 } + b ^ { \prime }$

7.Impose the conditions on (12) that $c ^ { \prime }$ shall be a minimum and show that it is satisfied only for $\pmb { r } _ { 1 } = 1$ ， $\mathbf { \hat { r } _ { 2 } } = 1$ ,and that the minimum value of $c ^ { \prime }$ is 3.

8.Why are not the lines of effective force orthogonal to all of the surfaces of constant velocity?

9.Prove that the double point between $\pmb { \mu }$ and $1 - \mu$ is nearer $\pmb { \mu }$ than ig the one between $\pmb { \mu }$ and $+ \infty$ .

10.Prove that,as $c ^ { \prime }$ diminishes, the first double point to appear is the one between $\pmb { \mu }$ and $1 - \pmb { \mu } ;$ ：the second,the one between $\pmb { \mu }$ and $+ \infty$ ；the third, the one between ${ \mathfrak { 1 } } - \mu$ and -o；and the last,those which make equilateral triangles with the finite bodies.

11. If $\mu = \textstyle \operatorname* { d e t } _ { \mathbf { i } \in \mathbf { \Gamma } } 1 - \mu = \operatorname* { d e t } _ { \mathbf { i } \in \mathbf { \Gamma } } \left( \begin{array} { l l } { \right. } & { } \\ { \left. \sum _ { i = 1 } ^ { \infty } \left( \mathbf { i } _ { i } \right) - \mathbf { i } _ { i } \right) = \operatorname* { d e t } _ { \mathbf { i } } \left( \mathbf { i } _ { i } \right) , } \end{array}$ find the values of $r _ { 1 } , r _ { 3 } ,$ and $c ^ { \prime }$ from (21), (22), (24),and (12).

$$
\left[ \begin{array} { l l l l } { ( 2 1 ) } & { r _ { 2 } = 0 . 3 4 0 , \quad } & { r _ { 1 } = 1 . 3 4 0 , \quad } & { C ^ { \prime } = 3 . 5 3 5 ; } \\ { ( 2 2 ) } & { r _ { 2 } = 0 . 2 7 6 , \quad } & { r _ { 1 } = 0 . 7 2 4 , \quad } & { C ^ { \prime } = 3 . 6 5 3 ; } \\ { ( 2 4 ) } & { r _ { 2 } = 1 . 9 4 7 , \quad } & { r _ { 1 } = 0 . 9 4 7 , \quad } & { C ^ { \prime } = 3 . 1 7 3 . } \end{array} \right.
$$

12.From the approximate values of the last example find by the method of differential corrections more accurate values.

$$
\begin{array} { r l r l r l } { { 1 1 ) } } & { \boldsymbol { r _ { 2 } } = 0 . 3 4 7 , } & & { \boldsymbol { r _ { 1 } } = 1 . 3 4 7 , } & & { \boldsymbol { C ^ { \prime } } = 3 . 5 3 4 ; } \\ { { } ! 2 ) } & { \boldsymbol { r _ { 2 } } = 0 . 2 8 2 , } & & { \boldsymbol { r _ { 1 } } = 0 . 7 1 8 , } & & { \boldsymbol { C ^ { \prime } } = 3 . 6 5 3 ; } \\ { { 3 ) } } & { \boldsymbol { r _ { 2 } } = 1 . 9 4 7 , } & & { \boldsymbol { r _ { 1 } } = 0 . 9 4 7 , } & & { \boldsymbol { C ^ { \prime } } = 3 . 1 7 3 . } \end{array}
$$

13.Considering the earth's orbit to bea circle, find the distance in mileg from the earth to the double point which is opposite to the sun.Would an infinitesimal body at this point be eclipsed?

Ans.930,240 miles.

159. Tisserand's Criterion for the Identity of Comets.\* Comets sometimes pass near the planets in their revolutions around the sun,and then the elements of their orbits are greatly changed. The planet Jupiter is especially potent in producing these perturbations because of its great mass and because at its distance the attraction of the sun is much less than it is at the distances of the earth-like planets. Since a comet has no characteristic features by which it may be recognized with certainty,its identity might be in question if it were not followed visually during the time of the perturbations.

One way of testing the identity of two comets appearing at different epochs is to take the orbit of the earlier and to compute the perturbations which it undergoes,and then to compare the derived elements with those determined from the later observations;or, the start may be made with the elements of the later comet,and by inverse processes the earlier elements may be com-puted and the comparison made. One or the other of these plans has been followed until recent years.

But the question arises if there is not some relation among the elements which remains unaltered by the perturbations. This is the question which Tisserand has answered in the affrmative in one of his characteristically elegant and important papers on Celestial Mechanics.

Let the eccentricity of Jupiter's orbit be supposed equal to zero, and the mass of the comet infinitesimal. While both of these assumptions are false they are very nearly fulfilled,and the error introduced will be inappreciable,especially as the comet will be near enough to Jupiter to sufer sensible disturbances only a very short time. Under these suppositions,and when the.units are properly chosen, the integral

$$
\left( { \frac { d x } { d t } } \right) ^ { 2 } + \left( { \frac { d y } { d t } } \right) ^ { 2 } + \left( { \frac { d z } { d t } } \right) ^ { 2 } = x ^ { 2 } + y ^ { 2 } + { \frac { 2 ( 1 - \mu ) } { r _ { 1 } } } + { \frac { 2 \mu } { r _ { 2 } } } - C
$$

holds true. This is an answer to the question； for，when the elements are known the velocity and coordinates can be computed at any time,and the motion referred to rotating axes by equations (2)． Hence,to test the identity of two comets,compute the function (7) for each orbit and see if the constant $\boldsymbol { C }$ is the same for both. If the two values of $\boldsymbol { C }$ are the same,the probability is very strong that only one comet has been observed; if they are different,the two comets are certainly distinct bodies.

The process just explained has the inconvenience of involving considerable computation. This can be largely avoided by expressing (7) in terms of the ordinary elements of the orbit. The first step is to express (7) in terms of coordinates measured from fixed axes. The equations of transformation are the inverse of equations (2),viz.,

$$
\left\{ \begin{array} { l l } { x = + \xi \cos t + \eta \sin t , } \\ { y = - \xi \sin t + \eta \cos t , } \\ { z = \xi . } \end{array} \right.
$$

From these equations it is found that

$$
x ^ { 2 } + y ^ { 2 } = \xi ^ { 2 } + \eta ^ { 2 } ,
$$

$$
\begin{array} { r } { \left( \frac { d x } { d t } \right) ^ { 2 } + \left( \frac { d y } { d t } \right) ^ { 2 } + \left( \frac { d z } { d t } \right) ^ { 2 } = \left( \frac { d \xi } { d t } \right) ^ { 2 } + \left( \frac { d \eta } { d t } \right) ^ { 2 } + \left( \frac { d \xi } { d t } \right) ^ { 2 } \qquad } \\ { + \xi ^ { 2 } + \eta ^ { 2 } - 2 \left( \xi \frac { d \eta } { d t } - \eta \frac { d \xi } { d t } \right) . \qquad } \end{array}
$$

Hence equation (7） becomes

$$
\begin{array} { c } { \displaystyle { \left( \frac { d \xi } { d t } \right) ^ { 2 } + \left( \frac { d \eta } { d t } \right) ^ { 2 } + \left( \frac { d \xi } { d t } \right) ^ { 2 } - 2 \left( \xi \frac { d \eta } { d t } - \eta \frac { d \xi } { d t } \right) } } \\ { \displaystyle { = \frac { 2 ( 1 - \mu ) } { r _ { 1 } } + \frac { 2 \mu } { r _ { 2 } } - C , } } \end{array}
$$

Let $\pmb { r }$ represent the distance of the comet from the origin,and $\textit { i }$ the angle between the plane of its instantaneous orbit and the $\xi \eta$ -plane. Then equations (24),Art.89,give

$$
\left\{ \begin{array} { l l } { \left( \frac { d \xi } { d t } \right) ^ { 2 } + \left( \frac { d \eta } { d t } \right) ^ { 2 } + \left( \frac { d \zeta } { d t } \right) ^ { 2 } = \frac { 2 } { r } - \frac { 1 } { a } , } \\ { \left( \xi \frac { d \eta } { d t } - \eta \frac { d \xi } { d t } \right) = \sqrt { a ( 1 - e ^ { 2 } ) } \cos i . } \end{array} \right.
$$

Hence equation (25) becomes

$$
\frac { 2 } { r } - \frac { 1 } { a } - 2 \sqrt { a ( 1 - e ^ { 2 } ) } \cos i = \frac { 2 ( 1 - \mu ) } { r _ { 1 } } + \frac { 2 \mu } { r _ { 2 } } - C .
$$

In the case of Jupiter and the sun $\mu$ is less than one-thousandth. Therefore the origin is very near the center of the sun,and $\pmb { r } _ { 1 }$ is sensibly equal to $\pmb { r }$ .In both instances the elements will be determined when the comet is far from both Jupiter and the sun so that $- \frac { 2 \mu } { r _ { 1 } } + \frac { 2 \mu } { r _ { 2 } }$ will be so small that it may be neglected without important error; then (26) reduces to the simple expression

$$
\begin{array} { r } { \frac { 1 } { a } + 2 \sqrt { a ( 1 - \overline { { e ^ { 2 } } } ) } \cos i = C . } \end{array}
$$

It will be noticed that the elements of this formula are the instantaneous elements for motion around a unit mass situated at the center of mass of the finite bodies. The actual elements used in Astronomy are the elements referred to the center of the sun，with the sun as the attracting mass. Nevertheless，on account of the small relative mass of Jupiter the two sets of elements are very nearly the same,and if the two orbits are of the same body,the equation

$$
\frac { 1 } { a _ { 1 } } + 2 \sqrt { a _ { 1 } ( 1 - e _ { 1 } { ^ { 2 } } ) } \cos i _ { 1 } = \frac { 1 } { a _ { 2 } } + 2 \sqrt { a _ { 2 } ( 1 - e _ { 2 } { ^ { 2 } } ) } \cos i _ { 2 }
$$

must be fulflled, where the elements are those in actual use by astronomers. Such is the criterion developed by Tisserand, and employed later by Schulhof and others.

160.Stability of Particular Solutions. Five particular solutions of the motion of the infinitesimal body have been found. If the infinitesimal body is displaced a very little from the exact points of the solutions and given a small velocity it will either oscillate around these respective points,at least for a considerable time, or it will rapidly depart from them. In the first case the particular solution from which the displacement is made is said to be stable; in the second case, it is said to be unstable.

The question of stability must be formulated mathematically. Consider the equations

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } x } { d t ^ { 2 } } - \displaystyle 2 \frac { d y } { d t } = f ( x , \ y ) , } \\ { \displaystyle \frac { d ^ { 2 } y } { d t ^ { 2 } } + \displaystyle 2 \frac { d x } { d t } = g ( x , \ y ) . } \end{array} \right.
$$

Suppose ${ \pmb x } = { \pmb x } _ { 0 } , { \pmb y } = { \pmb y } _ { 0 } ,$ where $\pmb { x _ { 0 } }$ and $y _ { 0 }$ are constants, is & particular solution of (28). That is,

$$
f ( x _ { 0 } , \ y _ { 0 } ) = 0 , \qquad g ( x _ { 0 } , \ y _ { 0 } ) = 0 .
$$

Give the body a small displacement and a small velocity so that its coordinates and components of velocity are

$$
\left\{ \begin{array} { l } { { x = x _ { 0 } + x ^ { \prime } , } } \\ { { y = y _ { 0 } + y ^ { \prime } , } } \\ { { \displaystyle \frac { d x } { d t } = \frac { d x ^ { \prime } } { d t } , } } \\ { { \displaystyle \frac { d y } { d t } = \frac { d y ^ { \prime } } { d t } , } } \end{array} \right.
$$

where $x ^ { \prime } , \ y ^ { \prime } , { \frac { d x ^ { \prime } } { d t } }$ J and $\frac { d y ^ { \prime } } { d t }$ are initilly veryall.Omaing these substitutions in (28),the differential equations become

$$
\left\{ \begin{array} { l l } { \displaystyle { \frac { d ^ { 2 } x ^ { \prime } } { d t ^ { 2 } } - 2 \frac { d y ^ { \prime } } { d t } = f ( x _ { 0 } + x ^ { \prime } , ~ y _ { 0 } + y ^ { \prime } ) , } } \\ { \displaystyle { \frac { d ^ { 2 } y ^ { \prime } } { d t ^ { 2 } } + 2 \frac { d x ^ { \prime } } { d t } = g ( x _ { 0 } + x ^ { \prime } , ~ y _ { 0 } + y ^ { \prime } ) . } } \end{array} \right.
$$

When the right members are developed by Taylor's formula, they take the form

$$
\left\{ \begin{array} { l l } { f ( x _ { 0 } + x ^ { \prime } , \ y _ { 0 } + y ^ { \prime } ) = f ( x _ { 0 } , \ y _ { 0 } ) + \displaystyle \frac { \partial f } { \partial x } x ^ { \prime } + \displaystyle \frac { \partial f } { \partial y } y ^ { \prime } + \cdots , } \\ { g ( x _ { 0 } + x ^ { \prime } , \ y _ { 0 } + y ^ { \prime } ) = g ( x _ { 0 } , \ y _ { 0 } ) + \displaystyle \frac { \partial g } { \partial x } x ^ { \prime } + \displaystyle \frac { \partial g } { \partial y } y ^ { \prime } + \cdots . } \end{array} \right.
$$

In the partial derivatives ${ \boldsymbol { \mathscr { x } } } = { \boldsymbol { \mathscr { x } } } _ { 0 }$ and $y = y _ { 0 }$ ，The first terms in the right members are respectively zero；hence equations (30) become

$$
\left\{ \begin{array} { l l } { \displaystyle { \frac { d ^ { 2 } x ^ { \prime } } { d t ^ { 2 } } - 2 \frac { d y ^ { \prime } } { d t } = \frac { \partial f } { \partial x ^ { \prime } } x ^ { \prime } + \frac { \partial f } { \partial y ^ { \prime } } y ^ { \prime } + \cdots , } } \\ { \displaystyle { \frac { d ^ { 2 } y ^ { \prime } } { d t ^ { 2 } } + 2 \frac { d x ^ { \prime } } { d t } = \frac { \partial g } { \partial x ^ { \prime } } x ^ { \prime } + \frac { \partial g } { \partial y ^ { \prime } } y ^ { \prime } + \cdots } } \end{array} \right.
$$

If $\scriptstyle { \pmb { x } } ^ { \prime }$ and $y ^ { \prime }$ are taken very small on the start the influence of the higher powers in the right members will be inappreciable,at least for a considerable time. If the parts which involve second and higher degree terms in $x ^ { \prime }$ and $y ^ { \prime }$ are neglected, the differential equations reduce to the linear system

$$
\left\{ \begin{array} { l l } { \displaystyle { \frac { d ^ { 2 } x ^ { \prime } } { d t ^ { 2 } } } - 2 { \frac { d y ^ { \prime } } { d t } } = { \frac { \partial f } { \partial x ^ { \prime } } } x ^ { \prime } + { \frac { \partial f } { \partial y ^ { \prime } } } y ^ { \prime } , } \\ { \displaystyle { \frac { d ^ { 2 } y ^ { \prime } } { d t ^ { 2 } } } + 2 { \frac { d x ^ { \prime } } { d t } } = { \frac { \partial g } { \partial x ^ { \prime } } } x ^ { \prime } + { \frac { \partial g } { \partial y ^ { \prime } } } y ^ { \prime } . } \end{array} \right.
$$

The solutions of a system of linear differential equations with constant coefficients can in general be expressed in terms of exponentials in the form

$$
\left\{ \begin{array} { l l } { x ^ { \prime } = \alpha _ { 1 } e ^ { \lambda _ { 1 } t } + \alpha _ { 2 } e ^ { \lambda _ { 2 } t } + \alpha _ { 3 } e ^ { \lambda _ { 3 } t } + \alpha _ { 4 } e ^ { \lambda _ { 4 } t } , } \\ { y ^ { \prime } = \beta _ { 1 } e ^ { \lambda _ { 1 } t } + \beta _ { 2 } e ^ { \lambda _ { 2 } t } + \beta _ { 3 } e ^ { \lambda _ { 3 } t } + \beta _ { 4 } e ^ { \lambda _ { 4 } t } , } \end{array} \right.
$$

where $\alpha _ { 1 } , \cdots , \alpha _ { 4 }$ are the constants of integration, and $\beta _ { 1 } , \cdots , \beta _ { 4 }$ are constants depending upon them and the constants involved in the differential equations.If $\lambda _ { 1 } , ~ \cdots , ~ \lambda _ { 4 }$ are pure imaginary numbers, then $\scriptstyle { \pmb x } ^ { \prime }$ and $y ^ { \prime }$ are expressible in periodic functions,and the solution from which the start was made is said to be stable; if any of $\lambda _ { 1 } , \cdots , \lambda _ { 4 }$ are real or complex numbers, then $\scriptstyle { \pmb x } ^ { \prime }$ and $y ^ { \prime }$ change indefinitely with $t _ { i }$ ，and the solution is said to be unstable.

There are exceptional cases where the solution contains constant terms instead of exponentials; they are of course stable if all the exponentials are purely imaginary. There are other exceptional cases in which the solution contains exponentials multiplied by some power of $t$ ；these solutions are usually regarded as unstable.

161.Application of the Criterion for Stability to the Straight Line Solutions. The definitions and general methods of the last article will now be applied to the special cases which have arisen in the discussion of the motion of the infinitesimal body. The original differential equations were (Art.152)

$$
\begin{array} { r l } & { \left\lceil \frac { d ^ { 2 } x } { d t ^ { 2 } } - 2 \frac { d y } { d t } = x - ( 1 - \mu ) \frac { ( x - x _ { 1 } ) } { { r _ { 1 } } ^ { 3 } } - \mu \frac { ( x - x _ { 2 } ) } { { r _ { 2 } } ^ { 3 } } \equiv f ( x , y , z ) , \right. } \\ & { \left. \frac { d ^ { 2 } y } { d t ^ { 2 } } + 2 \frac { d x } { d t } = y - ( 1 - \mu ) \frac { y } { { r _ { 1 } } ^ { \prime } } - \mu \frac { y } { { r _ { 2 } } ^ { 3 } } \equiv g ( x , y , z ) , \right. } \\ & { \left. \frac { d ^ { 2 } z } { d t ^ { 2 } } \right. \qquad \quad = \quad - \left( 1 - \mu \right) \frac { z } { { r _ { 1 } } ^ { 3 } } - \mu \frac { z } { { r _ { 2 } } ^ { 3 } } \equiv h ( x , y , z ) . } \end{array}
$$

The straight line solutions occur for

$$
x = x _ { 0 i } , \qquad y = 0 , \qquad z = 0 ,
$$

where $i = 1 , 2 , 3$ according as the point lies between $+ \infty$ and $\pmb { \mu }$ ， $\pmb { \mu }$ and ${ \bf 1 } - \mu _ { \mathrm { ~ } }$ or $1 - \mu$ and $- \infty$ , and where these values of $x , y ,$ and $\pmb { \mathscr { z } }$ satisfy equation (19). Make the substitution

$$
\left\{ \begin{array} { l l } { { \displaystyle x = x _ { 0 i } + x ^ { \prime } } , \quad } & { { \displaystyle y = y ^ { \prime } , \quad } \quad z = z ^ { \prime } , } \\ { { \displaystyle \frac { d x } { d t } = \frac { d x ^ { \prime } } { d t } , \quad } \quad } & { { \displaystyle \frac { d y } { d t } = \frac { d y ^ { \prime } } { d t } , \quad } \quad \frac { d z } { d t } = \frac { d z ^ { \prime } } { d t } . } \end{array} \right.
$$

Then it is found that

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial f } { \partial x ^ { \prime } } x ^ { \prime } + \frac { \partial f } { \partial y ^ { \prime } } y ^ { \prime } + \frac { \partial f } { \partial z ^ { \prime } } z ^ { \prime } = x ^ { \prime } + \frac { 2 ( 1 - \mu ) x ^ { \prime } } { [ ( x _ { 0 i } - x _ { 1 } ) ^ { 2 } ] ^ { \frac { 3 } { 2 } } } + \frac { 2 \mu x ^ { \prime } } { [ ( x _ { 0 i } - x _ { 2 } ) ^ { 2 } ] ^ { \frac { 3 } { 2 } } } , } \\ { \displaystyle \frac { \partial g } { \partial x ^ { \prime } } x ^ { \prime } + \frac { \partial g } { \partial y ^ { \prime } } y ^ { \prime } + \frac { \partial g } { \partial z ^ { \prime } } z ^ { \prime } = y ^ { \prime } - \frac { ( 1 - \mu ) y ^ { \prime } } { [ ( x _ { 0 i } - x _ { 1 } ) ^ { 2 } ] ^ { \frac { 3 } { 2 } } } - \frac { \mu y ^ { \prime } } { [ ( x _ { 0 i } - x _ { 2 } ) ^ { 2 } ] ^ { \frac { 3 } { 2 } } } , } \\ { \displaystyle \frac { \partial h } { \partial x ^ { \prime } } x ^ { \prime } + \frac { \partial h } { \partial y ^ { \prime } } y ^ { \prime } + \frac { \partial h } { \partial z ^ { \prime } } z ^ { \prime } \equiv \quad - \frac { ( 1 - \mu ) z ^ { \prime } } { [ ( x _ { 0 i } - x _ { 1 } ) ^ { 2 } ] ^ { \frac { 3 } { 2 } } } - \frac { \mu z ^ { \prime } } { [ ( x _ { 0 i } - x _ { 2 } ) ^ { 2 } ] ^ { \frac { 3 } { 2 } } } . } \end{array} \right.
$$

Let

$$
A _ { i } = \frac { 1 - \mu } { [ ( x _ { 0 i } - x _ { 1 } ) ^ { 2 } ] ^ { \frac { 3 } { 4 } } } + \frac { \mu } { [ ( x _ { 0 i } - x _ { 2 } ) ^ { 2 } ] ^ { \frac { 3 } { 4 } } } .
$$

Then the eguations correspending to (32) become in this case

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } x ^ { \prime } } { d t ^ { 2 } } - 2 \frac { d y ^ { \prime } } { d t } = ( 1 + 2 A _ { i } ) x ^ { \prime } , } \\ { \displaystyle \frac { d ^ { 2 } y ^ { \prime } } { d t ^ { 2 } } + 2 \frac { d x ^ { \prime } } { d t } = ( 1 - A _ { i } ) y ^ { \prime } , } \\ { \displaystyle \frac { d ^ { 2 } z ^ { \prime } } { d t ^ { 2 } } \qquad \quad = - A _ { i } z ^ { \prime } . } \end{array} \right.
$$

The last equation is independent of the first two and can be treated separately. The solution is (Art.32)

$$
z ^ { \prime } = c _ { 1 } e ^ { \sqrt { - 1 } \sqrt { A _ { i } } t } + c _ { 2 } e ^ { - \sqrt { - 1 } \sqrt { A _ { i } } t } .
$$

Therefore the motion parallel to the ${ \mathfrak { z } } .$ -axis,for small displacements, is periodic withtheperiod $\frac { 2 \pi } { \sqrt { A _ { i } } }$

Consider now the simultaneous equations

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } x ^ { \prime } } { d t ^ { 2 } } - 2 \frac { d y ^ { \prime } } { d t } = ( 1 + 2 A _ { \ast } ) x ^ { \prime } , } \\ { \displaystyle \frac { d ^ { 2 } y ^ { \prime } } { d t ^ { 2 } } + 2 \frac { d x ^ { \prime } } { d t } = ( 1 - A _ { \ast } ) y ^ { \prime } . } \end{array} \right.
$$

To find the solutions let

$$
\left\{ \begin{array} { l } { { x ^ { \prime } = K e ^ { \lambda t } , } } \\ { { y ^ { \prime } = L e ^ { \lambda t } , } } \end{array} \right.
$$

where $\kappa$ and $L$ are constants. On substituting these expressions in equations (37) and dividing out $e ^ { \lambda t }$ ,it is found that

$$
\left\{ \begin{array} { r } { [ \lambda ^ { 2 } - ( 1 + 2 A _ { i } ) ] K - 2 \lambda L = 0 , } \\ { 2 \lambda K + [ \lambda ^ { 2 } - ( 1 - A _ { i } ) ] L = 0 . } \end{array} \right.
$$

In order that equations (38) shall be particular solutions of (37) equations (39） must be fulfilled. They are verified by $K = 0$ ， $L = 0$ ； but in this case $x ^ { \prime } = 0$ ， $y ^ { \prime } = 0$ ，and the solutions reduce to the straight line solutions. Equations (39) can be satisfied by values of $\kappa$ and $L$ different from zero only if the determinant of the coefficients vanishes. This condition is

$$
\left| \begin{array} { l l } { { \lambda ^ { 2 } - ( 1 + 2 A _ { i } ) , } } & { { \qquad - 2 \lambda } } \\ { { \hphantom { 0 } + 2 \lambda } } & { { \hphantom { 0 } } } \\ { { \hphantom { 0 } + 2 \lambda } } & { { \hphantom { 0 } , \qquad \lambda ^ { 2 } - ( 1 - A _ { i } ) } } \end{array} \right| = 0 .
$$

This equation is the condition upon $\lambda$ that equations (38) may be a solution of (37). There are four roots of this biquadratic, each giving a particular solution,and the general solution is the sum of the four particular solutions multiplied by arbitrary constants; that is, if the four roots of (40) are $\lambda _ { 1 } , \lambda _ { 2 } , \lambda _ { 3 } , \lambda _ { 4 } ,$ the general solution is

$$
\left\{ \begin{array} { l l } { x ^ { \prime } = K _ { 1 } e ^ { \lambda _ { 1 } t } + K _ { 2 } e ^ { \lambda _ { 2 } t } + K _ { 3 } e ^ { \lambda _ { 3 } t } + K _ { 4 } e ^ { \lambda _ { 4 } t } , } \\ { y ^ { \prime } = L _ { 1 } e ^ { \lambda _ { 1 } t } + L _ { 2 } e ^ { \lambda _ { 2 } t } + L _ { 3 } e ^ { \lambda _ { 3 } t } + L _ { 4 } e ^ { \lambda _ { 4 } t } , } \end{array} \right.
$$

where the $\kappa _ { i }$ are the arbitrary constants of integration,and the $L _ { j }$ are defined in terms of them respectively by either of the equations (39).The $\lambda _ { \eta }$ depend of course upon the subscript $_ i$ on $\pmb { A }$ ,but the notation need not be burdened with this fact since the equations all have the same form whether $_ { i }$ is 1, 2, or 3.

It remains to determine the character of the roots of the biquadratic (40). It follows from (34) and (21)，(22),and (24) respectively that

$$
\left\{ \begin{array} { l l } { \displaystyle A _ { 1 } \equiv \frac { 1 - \mu } { ( 1 + r _ { 2 } ) ^ { 3 } } + \frac { \mu } { r _ { 2 } ^ { 3 } } = 4 - 2 \cdot 3 \left( \frac { \mu } { 3 } \right) ^ { \ast } + \cdot \cdot \cdot , } \\ { \displaystyle A _ { 2 } \equiv \frac { 1 - \mu } { ( 1 - r _ { 2 } ) ^ { 3 } } + \frac { \mu } { r _ { 2 } ^ { 3 } } = 4 + 2 \cdot 3 \left( \frac { \mu } { 3 } \right) ^ { \ast } + \cdot \cdot \cdot , } \\ { \displaystyle A _ { 3 } \equiv \frac { 1 - \mu } { ( 1 - \rho ) ^ { 3 } } + \frac { \mu } { ( 2 - \rho ) ^ { 3 } } = 1 + \frac { \tau } { 8 } \mu + \cdot \cdot \cdot . } \end{array} \right.
$$

It follows from (42) that, for small values of $\pmb { \mu } _ { : }$ ,the term of (40) which is independent of $\gimel$ satisfies the inequality

$$
{ \bf 1 } + A _ { i } - 2 A _ { i } { \bf 2 } < 0 , ( i = 1 , 2 , 3 ) ;
$$

and,indeed,this relation is true for values of $\pmb { \mu }$ up to the limit $\textstyle { \frac { 1 } { 2 } }$ ， as can be verified easily.\* Therefore the biquadratic has two real roots which are equal in numerical value and opposite in sign,and two conjugate pure imaginaries. It follows from the definitions given that the motion is unstable. If the infinitesimal body were displaced a very little from the points of solution it would in general depart to a comparatively great distance.

162.Particular Values of the Constants of Integration. The constants of integration will now be expressed in terms of the initial conditions,and it will be shown that the latter can be selected so that the motion will be periodic.

Suppose $\pmb { \lambda _ { 1 } }$ and $\pmb { \lambda _ { 2 } }$ are the real roots of equation (40)； then $\lambda _ { 1 } = - \lambda _ { 2 }$ The imaginary roots are

\*H.C. Plummer gave a general proof in Monthly Not.of Roy. Astr. Soc., vol. LXII. (1901).

$$
\left\{ \begin{array} { l l } { \lambda _ { 3 } = + \sqrt { - \mathrm { \Delta } 1 } \sigma , } \\ { \lambda _ { 4 } = - \sqrt { - \mathrm { \Delta } 1 } \sigma , } \end{array} \right.
$$

where $\pmb { \sigma }$ is a real number. The $\mathbf { { \cal L } } _ { j }$ are expressed in terms of the $\pmb { K _ { j } }$ by equations (39),and are

$$
L _ { j } = \frac { [ \lambda _ { j } ^ { 2 } - ( 1 + 2 A _ { i } ) ] } { 2 \lambda _ { j } } K _ { j } = c _ { j } K _ { j } , \binom { i = 1 , 2 , 3 ; } { j = 1 , 2 , 3 , 4 } .
$$

Since the $\pmb { \lambda _ { j } }$ are equal in numerical value but opposite in sign in pairs,and the last two are imaginary,it follows that

$$
\left\{ \begin{array} { l l } { c _ { 1 } = - c _ { 2 } , } \\ { c _ { 3 } = + { \sqrt { - \ 1 } } c , } \\ { c _ { 4 } = - { \sqrt { - \ 1 } } c , } \end{array} \right.
$$

where $\pmb { c }$ is a real constant depending on $\dot { \pmb { \mathscr { i } } }$

Let xo', yo', $x _ { 0 } ^ { \prime } , y _ { 0 } ^ { \prime } , \frac { d x _ { 0 } ^ { \prime } } { d t }$ ， and $\frac { d y _ { 0 } { ' } } { d t }$ be the initial coordinates and components of velocity; then equations (41) give at $\pmb { t = 0 }$

$$
\left\{ \begin{array} { l } { { { x _ { 0 } } ^ { \prime } = K _ { 1 } + K _ { 2 } + K _ { 3 } + K _ { 4 } , } } \\ { { \quad } } \\ { { { y _ { 0 } } ^ { \prime } = c _ { 1 } ( K _ { 1 } - K _ { 2 } ) + \sqrt { - 1 } c ( K _ { 3 } - K _ { 4 } ) , } } \\ { { \quad } } \\ { { \displaystyle { \frac { d x _ { 0 } ^ { \prime } } { d t } } ^ { \prime } = \lambda _ { 1 } ( K _ { 1 } - K _ { 2 } ) + \sqrt { - 1 } \sigma ( K _ { 3 } - K _ { 4 } ) , } } \\ { { \quad } } \\ { { \displaystyle { \frac { d y _ { 0 } ^ { \prime } } { d t } } ^ { \prime } = c _ { 1 } \lambda _ { 1 } ( K _ { 1 } + K _ { 2 } ) - c \sigma ( K _ { 3 } + K _ { 4 } ) . } } \end{array} \right.
$$

The values of the constants of integration are found in terms of the initial coordinates and components of velocity by solving these equations.

The values of $\mathbf { \nabla } x ^ { \prime }$ and $y ^ { \prime }$ increase in general without limit with the time,but if the initial conditions are such that $K _ { 1 } = K _ { 2 } = 0$ they become purely periodic. This case will now be considered. The initial coordinates, $x _ { 0 } ^ { \prime } , \ y _ { 0 } ^ { \prime }$ ，will determine $\pmb { K _ { 3 } }$ and $\kappa _ { 4 } ,$ by means of which $\frac { d x _ { 0 } } { d t } ^ { \prime }$ and $\frac { d y _ { 0 } { ' } } { d t }$ are defined. Thus

$$
\left\{ \begin{array} { l l } { { x _ { 0 } } ^ { \prime } = K _ { 3 } + K _ { 4 } , } \\ { { y _ { 0 } } ^ { \prime } = \sqrt { - \ 1 } c ( K _ { 3 } - K _ { 4 } ) ; } \end{array} \right.
$$

whence

$$
\begin{array} { r } { \{ K _ { 3 } = \displaystyle \frac { { x _ { 0 } } ^ { \prime } } { 2 } - \frac { \sqrt { - 1 } } { 2 c } y _ { 0 } \} , } \\ { \displaystyle K _ { 4 } = \displaystyle \frac { { x _ { 0 } } ^ { \prime } } { 2 } + \frac { \sqrt { - 1 } } { 2 c } y _ { 0 } \} . } \end{array}
$$

The equations (41) become

$$
\left\{ \begin{array} { l l } { { x ^ { \prime } = \displaystyle \frac { { x _ { 0 } } ^ { \prime } } { 2 } ( e ^ { \lambda \overline { { { - } } } \mathrm { i } \sigma t } + e ^ { - \lambda \overline { { { - } } } \sigma t } ) - \displaystyle \frac { \sqrt { { - } 1 } } { 2 c } y _ { 0 } ^ { \prime } ( e ^ { \lambda \overline { { { - } } } \mathrm { i } \sigma t } - e ^ { - \nu \overline { { { - } } } \mathrm { i } \sigma t } ) } } \\ { { \qquad = x _ { 0 } ^ { \prime } \cos \sigma t + \displaystyle \frac { y _ { 0 } ^ { \prime } } { c } \sin \sigma t , } } \\ { { y ^ { \prime } = \displaystyle \sqrt { { - } 1 } \displaystyle \frac { c } { 2 } { x _ { 0 } } ^ { \prime } ( e ^ { \lambda \overline { { { - } } } \mathrm { i } \sigma t } - e ^ { - \nu \overline { { { - } } } \mathrm { i } \sigma t } ) + \displaystyle \frac { y _ { 0 } ^ { \prime } } { 2 } ( e ^ { \lambda \overline { { { - } } } \mathrm { i } \sigma t } + e ^ { - \nu \overline { { { - } } } \mathrm { i } \sigma t } ) } } \\ { { \qquad = \displaystyle - c x _ { 0 } ^ { \prime } \sin \sigma t + y _ { 0 } ^ { \prime } \cos \sigma t . } } \end{array} \right.
$$

The equation of the orbit is found by eliminating $\scriptstyle t$ from these equations. Solve for cos $^ { \sigma t }$ and sin $^ { \sigma t }$ ; then square and add, and the result,after dividing out coimmon factors, is

$$
\frac { { x ^ { \prime } } ^ { 2 } } { \frac { c ^ { 2 } { x _ { 0 } ^ { \prime } } ^ { 2 } + { y _ { 0 } ^ { \prime } } ^ { 2 } } { c ^ { 2 } } } + \frac { { y ^ { \prime } } ^ { 2 } } { c ^ { 2 } { x _ { 0 } ^ { \prime } } ^ { 2 } + { y _ { 0 } ^ { \prime } } ^ { 2 } } = 1 .
$$

This is the equation of an ellipse with the major and minor axes lying along the coordinate axes,and with the center at the origin. Since $\lambda _ { 3 }$ is imaginary it follows from (43) and (44) that $c ^ { 2 } > 1$ ； therefore the major axis of the ellipse is parallel to the $_ y$ -axis. The eccentricity is given by

$$
e ^ { 2 } = { \frac { c ^ { 2 } - 1 } { c ^ { 2 } } } ,
$$

which, for large values of $^ { c }$ ,is very near unity. The orbits have the remarkable property that their eccentricity is independent of the initial small displacements,depending only upon the distribution of the mass between the finite bodies,and upon the one of the three straight line solutions from which they sprig.

It is obvious that this discussion is not completely rigorous because the terms of higher degree in the right members of the differential equations have been neglected. The linear terms alone do not give sufficient conditions for the existence of periodic orbits,and consequently when the discussion is thus restricted it answers only the question as to the stability of the solution. But in the present case periodic orbits actually exist about all three points for all $0 < \mu \leq \frac { 1 } { 2 }$ .Some special examples for $\mu = \scriptstyle { \frac { 1 } { \mathrm { { T I } } } }$ were found by Darwin in his memoir in Acta Mathematica,vol. 21. The complete analysis for these orbits,including the much more difficult case in which the finite bodies describe elliptical orbits, was given by the author in the Mathematische Annalen，vol. LxXII1. (1912),pp.441-479,and in the Publications of the Carnegie Institution of Washington, No. 161,Periodic Orbits,chapters v., vI., and vI1.

163.Application to the Gegenschein. If the constants $\textstyle \mathbf { K _ { 1 } }$ and $K _ { 2 }$ are zero the infinitesimal body will revolve in an ellipse around the point of equilibrium. If these constants are not zero but small in numerical value compared to $K _ { 3 }$ and $\kappa _ { 4 } ,$ the motion will be nearly in an ellipse for a considerable time,but will eventually depart very far from it. It would be possible to have any number of infinitesimal bodies revolving around the same point without disturbing one another.

Consider the motion of the earth around the sun. It is in a curve which is nearly a circle. One of the straight line solution points is exactly opposite to the sun,and if a meteor should pass near it with initial conditions approximately such as have becn defined in the last article it would make one or more circuits around this point before pursuing its path into other regions. If a very great number were swarming around this point at one time they would appear from the earth as a hazy patch of light with its center at the anti-sun，and elongated along the ecliptic. This is the appearance of the gegenschein which was discovered independently by Brorsen，Backhouse,and Barnard in 1855,1868,and 1875 respectively.

The crucial question seems to be whether or not there are enough meteors with the approximate initial conditions to explain the observed phenomena,but no certain answer can be given. However,it is certain that the meteors are exceedingly numerous,as many as 8,0oo,00o striking into the earth's atmosphere daily according to H.A. Newton；and it is only reasonable to suppose that they cause the zodiacal light which is very bright compared to the gegenschein. The suggestion that this may be the cause of the gegenschein was first made by Gylden in the closing paragraph of a memoir in the Bulletin Astronomique, vol. 1., entitled,Sur un Cas Particulier du Probleme des Trois Corps.\*

164.Application of the Criterion for Stability to the Equilateral Triangle Solutions. The particular solutions of the original diferential equations in this case are $r _ { 1 } = 1$ ， $r _ { 2 } = 1$ .The equations corresponding to (33) are

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial f } { \partial { \dot { x } } ^ { \prime } } { x ^ { \prime } } + \frac { \partial f } { \partial { y ^ { \prime } } } { y ^ { \prime } } + \frac { \partial f } { \partial { z ^ { \prime } } } { z ^ { \prime } } = \frac { 3 } { 4 } { x ^ { \prime } } + \frac { 3 \sqrt { 3 } } { 4 } ( 1 - 2 \mu ) { y ^ { \prime } } , } \\ { \displaystyle \frac { \partial g } { \partial { x ^ { \prime } } } { x ^ { \prime } } + \frac { \partial g } { \partial { y ^ { \prime } } } { y ^ { \prime } } + \frac { \partial g } { \partial { z ^ { \prime } } } { z ^ { \prime } } = \frac { 3 \sqrt { 3 } } { 4 } ( 1 - 2 \mu ) { x ^ { \prime } } + \frac { 9 } { 4 } { y ^ { \prime } } , } \\ { \displaystyle \frac { \partial h } { \partial { x ^ { \prime } } } { x ^ { \prime } } + \frac { \partial h } { \partial { y ^ { \prime } } } { y ^ { \prime } } + \frac { \partial h } { \partial { z ^ { \prime } } } { z ^ { \prime } } = - { z ^ { \prime } } ; } \end{array} \right.
$$

and the differential equations up to terms of the second degree are

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } x ^ { \prime } } { d t ^ { 2 } } - 2 \frac { d y ^ { \prime } } { d t } = \frac { 3 } { 4 } x ^ { \prime } + \frac { 3 \sqrt { 3 } } { 4 } ( 1 - 2 \mu ) y ^ { \prime } , } \\ { \displaystyle \frac { d ^ { 2 } y ^ { \prime } } { d t ^ { 2 } } + 2 \frac { d x ^ { \prime } } { d t } = \frac { 3 \sqrt { 3 } } { 4 } ( 1 - 2 \mu ) x ^ { \prime } + \frac { 9 } { 4 } y ^ { \prime } , } \\ { \displaystyle \frac { d ^ { 2 } z ^ { \prime } } { d t ^ { 2 } } \qquad = - z ^ { \prime } . } \end{array} \right.
$$

The last equation is independent of the first two,and its solution is

$$
{ \mathfrak { z } } ^ { \prime } = { \mathfrak { c } } _ { 1 } \sin t + { \mathfrak { c } } _ { 2 } \cos { \tau } .
$$

Therefore the motion parallel to the z-axis, for small displacements,is periodic with period $2 \pi$ ,the same as that of the revolution of the finite bodies.

To find the solutions of the first two equations let

$$
\left\{ \begin{array} { l l } { { \pmb x } ^ { \prime } = K e ^ { \lambda t } , } \\ { { \pmb y } ^ { \prime } = L e ^ { \lambda t } } \end{array} \right.
$$

On substituting these expressions in the first two equations of (47) and dividing out common factors,it is found that

$$
\left\{ \begin{array} { c } { { \displaystyle [ \lambda ^ { 2 } - \frac { 3 } { 4 } ] K - \left[ 2 \lambda + \frac { 3 } { 4 } \sqrt { 3 } \left( 1 - 2 \mu \right) \right] L = 0 , } } \\ { { \displaystyle \left[ 2 \lambda - \frac { 3 } { 4 } \sqrt { 3 } \left( 1 - 2 \mu \right) \right] K + [ \lambda ^ { 2 } - \frac { 9 } { 4 } ] L = 0 . } } \end{array} \right.
$$

In order that solutions may be obtained other than $\boldsymbol { x } ^ { \prime } = \boldsymbol { 0 } , \boldsymbol { y } ^ { \prime } = \boldsymbol { 0 }$ the determinant of these equations must vanish. That is.

$$
\begin{array} { r l } & { \left| \lambda ^ { 2 } - \frac { 3 } { 4 } , - 2 \lambda - \frac { 3 \sqrt { 3 } } { 4 } ( 1 - 2 \mu ) \right| = \lambda ^ { 4 } + \lambda ^ { 2 } + \frac { 2 7 } { 4 } \mu \left( 1 - \mu \right) = 0 . } \\ & { \left| 2 \lambda - \frac { 3 \sqrt { 3 } } { 4 } ( 1 - 2 \mu ) , \lambda ^ { 2 } - \frac { 9 } { 4 } \right| } \end{array}
$$

Let $\lambda _ { 1 } , ~ \lambda _ { 2 } , ~ \lambda _ { 3 } , ~ \lambda _ { 4 }$ be the roots of this biquadratic. Then the general solutions of (47） are

$$
\left\{ \begin{array} { l l } { x ^ { \prime } = K _ { 1 } e ^ { \lambda _ { 1 } t } + K _ { 2 } e ^ { \lambda _ { 2 } t } + K _ { 3 } e ^ { \lambda _ { 3 } t } + K _ { 4 } e ^ { \lambda _ { 4 } t } , } \\ { y ^ { \prime } = L _ { 1 } e ^ { \lambda _ { 1 } t } + L _ { 2 } e ^ { \lambda _ { 2 } t } + L _ { 3 } e ^ { \lambda _ { 3 } t } + L _ { 4 } e ^ { \lambda _ { 4 } t } , } \end{array} \right.
$$

where $K _ { 1 } , K _ { 2 } , K _ { 3 } , K _ { 4 }$ are the constants of integration, and $L _ { 1 } , L _ { 2 } ,$ $L _ { 3 } , L _ { 4 }$ are constants related to them by either of equations (49).

It is found from (50) that

$$
\left\{ \begin{array} { l l } { \medskip \lambda _ { 1 } = - \medskip \lambda _ { 2 } = \sqrt { \frac { - \ 1 + \sqrt { 1 - 2 7 \mu ( 1 - \mu ) } } { 2 } } , } \\ { \medskip \lambda _ { 3 } = - \ \lambda _ { 4 } = \sqrt { \frac { - \ 1 - \sqrt { 1 - 2 7 \mu ( 1 - \mu ) } } { 2 } } . } \end{array} \right.
$$

The number $\mu$ never exceeds $\begin{array} { r } { \frac { \dot { \mathbf { z } } } { 2 } , } \end{array}$ and if $1 - 2 7 \mu ( 1 - \mu ) \geq 0$ the roots are pure imaginaries in conjugate pairs; if this inequality is not fulfiled they are complex quantities. The inequality may be written

$$
1 - 2 7 \mu ( 1 - \mu ) = \epsilon ,
$$

where é is a positive quantity whose limit is zero. The solution of this equation is

$$
\mu = { \textstyle \frac { 1 } { 2 } } \pm \sqrt { \frac { 2 3 + 4 \epsilon } { 1 0 8 } } .
$$

Since $\pmb { \mu }$ represents the mass which is less than one-half the negative sign must be taken. At the limit $\epsilon = 0$ ， $\mu = . 0 3 8 5 \cdots$ .Therefore if $\mu < . 0 3 8 5 \cdots$ the roots of (50) are pure imaginaries and the equilateral triangle solutions are stable；if $\mu > . 0 3 8 5 \cdots$ the roots of (5O) are complex and the equilateral triangle solutions are unstable.

# XXI. PROBLEMS.

1.If a comet approaching the sun in a parabola should be disturbed by Jupiter so that its orbit remained a parabola while its perihelion distance was doubled,what would be the relation between the new inclination and the old?

Ans.

$$
\cos i _ { 2 } = - \frac { \sqrt { 2 } } { 2 } \cos i _ { 1 } .
$$

2.Prove that if a comet's orbit,whose inclination to Jupiter's orbit i zero,is changed by the perturbations of Jupiter from a parabola to an ellipse the parameter of the orbit is necessarily decreased.Investigate the changes in the parameters for changes in the major axes of the other species of conics.

3.Suppose a comet is moving in an ellipse in the plane of Jupiter's orbit, and that the perturbing action of Jupiter is inappreciable except for a short time when they are near each other. Prove that if the perturbation of Jupiter has increased the eccentricity，the period has been increased or decreased according as the product of the major semi-axis and the square root of the parameter in the original elipse is greater or less than unity when expressed in the canonical units.

4.A particle placed midway between two equal fixed masses is in equilibrium． Investigate the character of the equilibrium by the method of Art.161.

5.Suppose ${ \bf 1 } - \mu$ and $\pmb { \mu }$ are the sun and earth respectively; find the period of oscillation parallel to the ${ \pmb z }$ -axis for an infinitesimal body slightly displaced from the xy-plane near the straight line solution point opposite to the sun with respect to the earth as an origin.

Ans.183.304 mean solar days.

6.In the same case,find the period of oscillation in the xy-plane.

Ans. 139.6 mean solar days.

7.Prove that in general for small values of $\pmb { \mu }$ the periods of oscillation both parallel to the ${ \pmb z } .$ -axis and in the $x y .$ -plane,are longest for the point opposite to $\pmb { \mu }$ with respect to $1 - \mu$ as origin；next longest for the point opposite to $1 - \mu$ with respect to $\pmb { \mu }$ as origin；and shortest for the point between $1 - \mu$ and $\pmb { \mu }$

8.Find the eccentricity of the orbit in the xy-plane opposite to the sun in the case of the sun and earth.

9.The differential equations (35) admit the integral

$$
\begin{array} { r } { \left( \frac { d x ^ { \prime } } { d t } \right) ^ { 2 } + \left( \frac { d y ^ { \prime } } { d t } \right) ^ { 2 } + \left( \frac { d z ^ { \prime } } { d t } \right) ^ { 2 } = ( 1 + 2 A _ { i } ) x ^ { \prime 2 } + ( 1 - A _ { i } ) y ^ { \prime 2 } - A _ { i } z ^ { \prime 2 } + C ; } \end{array}
$$

discuss the meaning of this integral after the manner of articles 154-159.

10.What can be said regarding the independence of equations (39) after the condition has been imposed that the determinant shall vanish?

11.If the explanation of the gegenschein given in Art.163 is true what should be its maximum parallax in celestial latitude for an observer in latitude $4 5 ^ { \circ } \}$

Ans.Roughly $\mathbf { 1 5 ^ { \prime } }$ 。(Too small to be observed with certainty in such an indefinite object.)

12. Suppose $\begin{array} { r } { \pmb { \mu } = \frac { 1 } { 2 } } \end{array}$ and reduce the problem of finding the motion of the infinitesimal body through the origin along the $\pmb { z }$ -axis to elliptic integrals.

CASE OF THREE FINITE BODIES.

165.Conditions for Circular Orbits. The theorem of Lagrange that it is possible to start three finite bodies in such a manner that their orbits will be similar ellipses,all described in the same time,will be proved in this section.It will be established first for the special case in which the orbits are circles. It will be assumed that the three bodies are projected in the same plane. Take the origin at their center of mass and the $\xi \eta$ -plane as the plane of motion. Then the differential equations of motion are (Art.143)

$$
\begin{array} { r l r } {  { \{ \frac { d ^ { 2 } \xi _ { i } } { d t ^ { 2 } } = \frac { 1 } { m _ { i } } \frac { \partial U } { \partial \xi _ { i } } , \qquad ( i = 1 , \ 2 , \ 3 ) ,  } }  \\ & { } & \\ & { } & {  \frac { d ^ { 2 } \eta _ { i } } { d t ^ { 2 } } = \frac { 1 } { m _ { i } } \frac { \partial U } { \partial \eta _ { i } } ,  } \\ & { } & \\ & { } & {  U = \frac { k ^ { 2 } m _ { 1 } m _ { 2 } } { r _ { 1 , 2 } } + \frac { k ^ { 2 } m _ { 2 } m _ { 3 } } { r _ { 2 , 3 } } + \frac { k ^ { 2 } m _ { 3 } m _ { 1 } } { r _ { 3 , 1 } } .  } \end{array}
$$

The motion of the system is referred to axes rotating with the uniform angular velocity $_ n$ by the substitution

$$
\left\{ \begin{array} { l l } { \xi _ { \mathrm { i } } = x _ { \mathrm { i } } \cos \eta t - y _ { \mathrm { i } } \sin \eta t , \qquad } & { ( i = 1 , 2 , 3 ) , } \\ { \eta _ { i } = x _ { \mathrm { i } } \sin \eta t + y _ { \mathrm { i } } \cos n t . } & { } \end{array} \right.
$$

On making the substitution，and reducing as in Art.152,it is iound that

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } x _ { i } } { d t ^ { 2 } } - \displaystyle 2 n \frac { d y _ { i } } { d t } - n ^ { 2 } x _ { i } - \displaystyle \frac { 1 } { m _ { i } } \frac { \partial U } { \partial x _ { i } } = 0 , } \\ { \displaystyle \frac { d ^ { 2 } y _ { i } } { d t ^ { 2 } } + \displaystyle 2 n \frac { d x _ { i } } { d t } - n ^ { 2 } y _ { i } - \displaystyle \frac { 1 } { m _ { i } } \frac { \partial U } { \partial y _ { i } } = 0 . } \end{array} \right.
$$

If the bodies are moving in circles around the origin with the angular velocity $_ n$ ，their coordinates with respect to the rotating axes are constants. Since the first and second derivatives are then zero,equations (54) become

$$
\left\{ \begin{array} { l l } { - \ n ^ { 2 } x _ { 1 } + k ^ { 2 } m _ { 2 } \displaystyle \frac { ( x _ { 1 } - x _ { 2 } ) } { r ^ { 3 } \scriptscriptstyle 1 , \ 2 } + k ^ { 2 } m _ { 3 } \displaystyle \frac { ( x _ { 1 } - x _ { 3 } ) } { r ^ { 3 } \scriptscriptstyle 1 , \ 3 } = 0 , } \\ { - \ n ^ { 2 } x _ { 2 } + k ^ { 2 } m _ { 1 } \displaystyle \frac { ( x _ { 2 } - x _ { 1 } ) } { r ^ { 3 } \scriptscriptstyle 1 , \ 2 } + k ^ { 2 } m _ { 3 } \displaystyle \frac { ( x _ { 2 } - x _ { 3 } ) } { r ^ { 3 } \scriptscriptstyle 2 , \ 3 } = 0 , } \\ { - \ n ^ { 2 } x _ { 3 } + k ^ { 2 } m _ { 1 } \displaystyle \frac { ( x _ { 3 } - x _ { 1 } ) } { r ^ { 3 } \scriptscriptstyle 1 , \ 3 } + k ^ { 2 } m _ { 2 } \displaystyle \frac { ( x _ { 3 } - x _ { 2 } ) } { r ^ { 3 } \scriptscriptstyle 2 , \ 3 } = 0 , } \end{array} \right.
$$

$$
\left\{ { \begin{array} { l } { - \displaystyle n ^ { 2 } y _ { 1 } + k ^ { 2 } m _ { 2 } \frac { ( y _ { 1 } - y _ { 2 } ) } { r ^ { 3 } \scriptscriptstyle 1 , 2 } + k ^ { 2 } m _ { 3 } \frac { ( y _ { 1 } - y _ { 3 } ) } { r ^ { 3 } \scriptscriptstyle 1 , 3 } = 0 , } \\ { - \displaystyle n ^ { 2 } y _ { 2 } + k ^ { 2 } m _ { 1 } \frac { ( y _ { 2 } - y _ { 1 } ) } { r ^ { 3 } \scriptscriptstyle 1 , 2 } + k ^ { 2 } m _ { 3 } \frac { ( y _ { 2 } - y _ { 3 } ) } { r ^ { 3 } \scriptscriptstyle 2 , 3 } = 0 , } \\ { - \displaystyle n ^ { 2 } y _ { 3 } + k ^ { 2 } m _ { 1 } \frac { ( y _ { 3 } - y _ { 1 } ) } { r ^ { 3 } \scriptscriptstyle 1 , 3 } + k ^ { 2 } m _ { 2 } \frac { ( y _ { 3 } - y _ { 2 } ) } { { r ^ { 3 } \scriptscriptstyle 2 , 3 } } = 0 . } \end{array} } \right.
$$

And conversely,if the masses and initial projections are such that these six equations are fulfilled the bodies move in circles around the origin with the uniform angular velocity $\mathscr { n }$

Since the origin is at the center of mass the coordinates satisfy

$$
\left\{ \begin{array} { l l } { m _ { 1 } x _ { 1 } + m _ { 2 } x _ { 2 } + m _ { 3 } x _ { 3 } = 0 , } \\ { m _ { 1 } y _ { 1 } + m _ { 2 } y _ { 2 } + m _ { 3 } y _ { 3 } = 0 . } \end{array} \right.
$$

If the first equation of (55) is multiplied by $m _ { 1 }$ , the second by $^ { m _ { 2 } , }$ and the products added, the sum becomes，as a consequence of the first equation of (56),the third of (55)．In a similar manner the last equation of (55) can be derived from the others in $y$ and the last of (56). Therefore the third and sixth equations of (55) can be suppressed, and equations (56) used in place of them, giving a somewhat simpler system of equations.

The units of time, space,and mass are so far arbitrary. It is possible,without loss of generality,to select them so that $r _ { 1 , \mathrm { ~ 2 ~ } } = 1$ and $k ^ { 2 } = 1$ .Then necessary and sufficient conditions for the existence of solutions in which the orbits are circles are

$$
\begin{array} { r } { { \mathfrak { m } } _ { 1 } x _ { 1 } + { \mathfrak { m } } _ { 2 } x _ { 2 } + { \mathfrak { m } } _ { 3 } x _ { 3 } = 0 , } \\ { [ - \pi ^ { 2 } x _ { 1 } + { \mathfrak { m } } _ { 2 } ( x _ { 1 } - x _ { 2 } ) + { \mathfrak { m } } _ { 3 } \frac { ( x _ { 1 } - x _ { 3 } ) } { T _ { 1 , 3 } ^ { 2 } } = 0 ,  } \\ { -  \pi ^ { 2 } x _ { 2 } + { \mathfrak { m } } _ { 1 } ( x _ { 2 } - x _ { 1 } ) + { \mathfrak { m } } _ { 4 } \frac { ( x _ { 2 } - x _ { 3 } ) } { T _ { 3 , 3 } ^ { 2 } } = 0 ,  } \\ { { \mathfrak { m } } _ { 1 } y _ { 1 } + { \mathfrak { m } } _ { 2 } y _ { 2 } + { \mathfrak { m } } _ { 3 } y _ { 3 } = 0 , } \\ { -  \pi ^ { 2 } y _ { 1 } + { \mathfrak { m } } _ { 2 } ( y _ { 1 } - y _ { 2 } ) + { \mathfrak { m } } _ { 3 } \frac { ( y _ { 1 } - y _ { 3 } ) } { T _ { 1 , 3 } ^ { 3 } } = 0 , } \\ { - \pi ^ { 2 } y _ { 2 } + { \mathfrak { m } } _ { 1 } ( y _ { 2 } - y _ { 1 } ) + { \mathfrak { m } } _ { 3 } \frac { ( y _ { 2 } - y _ { 3 } ) } { T _ { 3 , 3 } ^ { 2 } } = 0 . } \end{array}
$$

166.Equilateral Triangle Solutions. There is a solution of the problem for every set of real values of the variables satisfying equations (57). It is easy to show that the equations are fulfilled

if the bodies lie at the vertices of an equilateral triangle.Then ${ r _ { 1 , ~ 2 } } = { r _ { 2 , ~ 3 } } = { r _ { 1 , ~ 3 } } = 1$ ，and equations (57) become

$$
\begin{array} { r } { m _ { 1 } x _ { 1 } + m _ { 2 } x _ { 2 } + m _ { 3 } x _ { 3 } = 0 , } \\ { \left[ ( m _ { 2 } + m _ { 3 } - n ^ { 2 } ) x _ { 1 } - m _ { 2 } x _ { 2 } - m _ { 3 } x _ { 3 } = 0 , \right. } \\ { ( m _ { 1 } + m _ { 3 } - n ^ { 2 } ) x _ { 2 } - m _ { 1 } x _ { 1 } - m _ { 3 } x _ { 3 } = 0 , } \\ { \left. m _ { 1 } y _ { 1 } + m _ { 2 } y _ { 2 } + m _ { 3 } y _ { 3 } = 0 , \right. } \\ { \left. ( m _ { 2 } + m _ { 3 } - n ^ { 2 } ) y _ { 1 } - m _ { 2 } y _ { 2 } - m _ { 3 } y _ { 3 } = 0 , \right. } \\ { \left. ( m _ { 1 } + m _ { 3 } - n ^ { 2 } ) y _ { 2 } - m _ { 1 } y _ { 1 } - m _ { 3 } y _ { 3 } = 0 . \right. } \end{array}
$$

These equations are linear and homogeneous in $x _ { 1 } , \ x _ { 2 } , \ \cdots , \ y _ { 3 } .$ In order that they may have a solution different from ${ \pmb x } _ { 1 } = { \pmb x } _ { 2 }$ $\mathbf { \partial } = \cdots = y _ { 3 } = 0$ ，which is incompatible with $r _ { 1 , 2 } = r _ { 2 , 3 } = r _ { 1 , 3 } = 1 { \mathrm { . } }$ ， the determinant of their coefficients must vanish. On letting $M = m _ { 1 } + m _ { 2 } + m _ { 3 } ;$ ,it is easily found that this condition is

$$
m _ { 3 } { } ^ { 2 } ( M - n ^ { 2 } ) ^ { 4 } = 0 ,
$$

from which $n ^ { 2 } = M$ .Then two of the $\pmb { x _ { i } }$ and two of the $y _ { i }$ are arbitrary,and hence the equations have a solution compatible with $r _ { i , j } = 1$ .Therefore,the equilateral triangular configuration with proper initial components of velocity is a particular solution of the Problem of Three Bodies; and,if the units are such that the mutual distances and $k ^ { 2 }$ are unity,the square of the angular velocity of revolution is equal to the sum of the masses of the three bodies.

167。Straight Line Solutions. The last three equations of (57) are fulfilled by $y _ { 1 } = y _ { 2 } = y _ { 3 } = 0$ ,that is,if the bodies are all on the $_ x$ -axis. Suppose they lie in the order $m _ { 1 } , m _ { 2 } ,$ $\mathbf { \nabla } m _ { 3 }$ from the negative end of the axis toward the positive. Then $x _ { 3 } > x _ { 2 } > x _ { 1 }$ and $r _ { 1 , 2 } = x _ { 2 } - x _ { 1 } = 1$ ,and the first three equations of (57) become

$$
\left\{ \begin{array} { r } { m _ { 1 } x _ { 1 } + m _ { 2 } ( 1 + x _ { 1 } ) + m _ { 3 } x _ { 3 } = 0 , } \\ { m _ { 2 } + \displaystyle \frac { m _ { 3 } } { ( x _ { 3 } - x _ { 1 } ) ^ { 2 } } + n ^ { 2 } x _ { 1 } = 0 , } \\ { - m _ { 1 } + \displaystyle \frac { m _ { 3 } } { ( x _ { 3 } - x _ { 1 } - 1 ) ^ { 2 } } + n ^ { 2 } ( 1 + x _ { 1 } ) = 0 . } \end{array} \right.
$$

On eliminating $x _ { 3 }$ and $n ^ { 2 }$ ,it is found that

$$
m _ { 2 } + ( m _ { 1 } + m _ { 2 } ) x _ { 1 } + \frac { m _ { 3 } { } ^ { 3 } ( 1 + x _ { 1 } ) } { ( M x _ { 1 } + m _ { 2 } ) ^ { 2 } } - \frac { m _ { 3 } { } ^ { 3 } x _ { 1 } } { ( M x _ { 1 } + m _ { 2 } + m _ { 3 } ) ^ { 2 } } = 0 .
$$

If this equation is cleared of fractions a quintic equation in $\pmb { x } _ { 1 }$ is obtained whose coefficients are all positive. Therefore there is no real positive root but there is at least one real negative root, and consequently at least one solution of the problem.

Instead of adopting $x _ { 1 }$ as the unknown, $x _ { 3 } \textrm { -- } x _ { 2 } ,$ ，which will be denoted by $A$ ，may be used. The distance $x _ { 1 }$ must be expressed in terms of this new variable. The relations among xi, x2, xs, and $\pmb { A }$ are

$$
\left\{ \begin{array} { r l } { m _ { 1 } x _ { 1 } + m _ { 2 } x _ { 2 } + m _ { 3 } x _ { 3 } = 0 , } & { } \\ { \qquad \quad x _ { 2 } - x _ { 1 } = 1 , } & { } \\ { \qquad \quad x _ { 3 } - x _ { 2 } = A ; } \end{array} \right.
$$

whence

$$
x _ { 1 } = - \frac { m _ { 2 } + m _ { 3 } + m _ { 3 } A } { M } .
$$

On substituting this expression for $\pmb { x _ { 1 } }$ in (59),clearing of fractions, and dividing out common factors, the condition for the collinear solutions becomes

$$
\begin{array} { c } { { ( m _ { 1 } + m _ { 2 } ) A ^ { 5 } + ( 3 m _ { 1 } + 2 m _ { 2 } ) A ^ { 4 } + ( 3 m _ { 1 } + m _ { 2 } ) A ^ { 3 } } } \\ { { - ( m _ { 2 } + 3 m _ { 3 } ) A ^ { 2 } - ( 2 m _ { 2 } + 3 m _ { 3 } ) A - ( m _ { 2 } + m _ { 3 } ) = 0 . } } \end{array}
$$

This is precisely Lagrange's quintic equation in $^ { A , * }$ and has but ·one real positive root since the coefficients change sign but once. The only $\pmb { A }$ valid in the problem for the chosen order of the masses is positive；hence the solution of (6O) is unique and defines the distribution of the bodies in the straight line solution of the Problem of Three Bodies. It is evident that two more distinct straight line solutions will be obtained by cyclically permuting the order of the three bodies.

168.Dynamical Properties of the Solutions. Since the bodies revolve in circles with uniform angular velocity around the center of mass, the law of areas holds for each body separately; therefore .the resultant of all the forces acting upon each body is constantly directed toward the center of mass (Art.48).

Let the distances of $m _ { 1 } , \ m _ { 2 } ,$ and $\mathbf { \Delta } m _ { 3 }$ from their center of mass be $a _ { 1 } , ~ a _ { 2 } ,$ and ${ \mathfrak { a } } _ { 3 }$ respectively. Then the centrifugal acceleration to which $m _ { i }$ is subject is $\alpha _ { i } = \frac { V _ { i } ^ { 2 } } { a _ { i } }$ where $V _ { i }$ is the linear velocity of $m _ { \mathrm { i } }$ ，But this may be written $\alpha _ { i } = n ^ { 2 } a _ { i }$ 、The centripetal force exactly balances the centrifugal； therefore the acceleration toward the center of mass is

$$
\alpha _ { i } = n ^ { 2 } a _ { i } ;
$$

that is,the accelerations of the various bodies toward their common center of mass are directly proportional to their respective distances from this point.

169.General Conic Section Solutions. The solutions of the problem of three bodies which have been discussed are char\~ acterized by the fact that their orbits are circles. It will be shown that corresponding to each of them there is a solution in which the orbits are conic sections of arbitrary eccentricity. These solutions are characterized by the fact that in them the ratios of the mutual distances of the bodies are constant, though the distances themselves are variable.

The differential equations of motion when the system is referred to fixed axes with the origin at the center of gravity of the system are

$$
\{ \begin{array} { l l } { \frac { d \hat { z } _ { 1 1 } ^ { \prime } } { d t ^ { 2 } } = - \frac { m _ { 0 } ( \hat { z } _ { 1 } ^ { \prime } - \hat { z } _ { 2 } ^ { \prime } ) } { r ^ { 3 } ! } - \frac { m _ { 0 } ( \hat { z } _ { 1 } ^ { \prime } - \hat { z } _ { 3 } ^ { \prime } ) } { r ^ { 3 } ! } , } \\ { \frac { d \hat { z } _ { 1 2 } ^ { \prime } } { d t ^ { 2 } } = - \frac { m _ { 0 } ( \hat { z } _ { 1 } ^ { \prime } - \hat { z } _ { 1 } ^ { \prime } ) } { r ^ { 3 } ! } - \frac { m _ { 0 } ( \hat { z } _ { 1 } ^ { \prime } - \hat { z } _ { 3 } ^ { \prime } ) } { r ^ { 3 } ! s } , } \\ { \frac { d \hat { z } _ { 8 } ^ { \prime } } { d t ^ { 2 } } = - \frac { m _ { 1 } ( \hat { z } _ { 2 } ^ { \prime } - \hat { z } _ { 1 } ^ { \prime } ) } { r ^ { 3 } ! } - \frac { m _ { 0 } ( \hat { z } _ { 2 } ^ { \prime } - \hat { z } _ { 3 } ^ { \prime } ) } { r ^ { 5 } ! s } , } \\ { \frac { d \hat { z } _ { 9 2 } ^ { \prime } } { d t ^ { 2 } } = - \frac { m _ { 1 } ( \hat { z } _ { 1 } ^ { \prime } - \hat { z } _ { 1 } ^ { \prime } ) } { r ^ { 3 } ! s } - \frac { m _ { 0 } ( \hat { z } _ { 2 } ^ { \prime } - \hat { z } _ { 3 } ^ { \prime } ) } { r ^ { 2 } ! s } , } \\ { \frac { d \hat { z } _ { 8 } ^ { \prime } } { d t ^ { 2 } } = - \frac { m _ { 1 } ( \hat { z } _ { 3 } ^ { \prime } - \hat { z } _ { 1 } ^ { \prime } ) } { r ^ { 3 } ! s ! } - \frac { m _ { 0 } ( \hat { z } _ { 6 } ^ { \prime } - \hat { z } _ { 5 } ^ { \prime } ) } { r ^ { 2 } ! s ! } , } \\  \frac { d \hat { z } _ { 1 3 } ^ { \prime } } { d t ^ { 2 } } = - \frac { m _ { 1 } ( \hat { z } _ { 1 } ^ { \prime } - \hat { z } _ { 1 } ^ { \prime } ) }  r ^  3 \end{array}
$$

Suppose the coordinates of $m _ { 1 } , ~ m _ { 2 }$ and $m _ { 3 }$ at $t = t _ { 0 }$ are respectively $( x _ { 1 } , y _ { 1 } )$ ， $( x _ { 2 } , y _ { 2 } )$ ,and $( x _ { 3 } , y _ { 3 } )$ ,and let the respective distances from the origin be $r _ { 1 } ^ { ( 0 ) } , \ r _ { 2 } ^ { ( 0 ) }$ and $r _ { 3 } ^ { ( 0 ) }$ Suppose the angles that $r _ { 1 } ^ { ( 0 ) } , r _ { 2 } ^ { ( 0 ) }$ and $r _ { 3 } ^ { ( 0 ) }$ make with the $\xi$ -axis are $\varphi _ { 1 } , ~ \varphi _ { 2 } ,$ and $\varphi _ { 3 }$ Then

$$
\left\{ \begin{array} { l l } { x _ { 1 } = r _ { 1 } { } ^ { ( 0 ) } \cos \varphi _ { 1 } , } & { x _ { 2 } = r _ { 2 } { } ^ { ( 0 ) } \cos \varphi _ { 2 } , \quad \quad x _ { 3 } = r _ { 3 } { } ^ { ( 0 ) } \cos \varphi _ { 3 } , } \\ { y _ { 1 } = r _ { 1 } { } ^ { ( 0 ) } \sin \varphi _ { 1 } , } & { y _ { 2 } = r _ { 2 } { } ^ { ( 0 ) } \sin \varphi _ { 2 } , \quad \quad y _ { 3 } = r _ { 3 } { } ^ { ( 0 ) } \sin \varphi _ { 3 } . } \end{array} \right.
$$

Now let the coordinates of the bodies at any time $t$ be $( \xi _ { 1 } , \eta _ { 1 } )$ ， $( \xi _ { 2 } , \eta _ { 2 } )$ ，and $( \xi _ { 3 } , \eta _ { 3 } )$ . Suppose the ratios of the mutual distances

are constants; then the mutual distances at $\pmb { t }$ are

$$
\rho r _ { 1 , 2 } , \quad \rho r _ { 2 , 3 } , \qquad \rho r _ { 1 , 3 } ,
$$

where $\pmb { \rho }$ is the factor of proportionality. Since the shape of the figure formed by the three bodies is unaltered, it follows that

$$
r _ { 1 } = r _ { 1 } { } ^ { ( 0 ) } \rho , \qquad r _ { 2 } = r _ { 2 } { } ^ { ( 0 ) } \rho , \qquad r _ { 3 } = r _ { 3 } { } ^ { ( 0 ) } \rho .
$$

![](images/0004ca56764349df0aa88ee8e9de191477ab17191bf36ac3c898df730ce2df31.jpg)  
Fig. 42.

Moreover, the radii $r _ { 1 } , r _ { 2 } ,$ and $\pmb { r _ { 3 } }$ will have turned through the same angle $\pmb \theta$ Hence

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \xi _ { 1 } = r _ { 1 } ^ { ( 0 ) } \rho \cos { ( \theta + \varphi _ { 1 } ) } = ( x _ { 1 } \cos { \theta } - y _ { 1 } \sin { \theta } ) \rho , } \\ { \eta _ { 1 } = r _ { 1 } ^ { ( 0 ) } \rho \sin { ( \theta + \varphi _ { 1 } ) } = ( x _ { 1 } \sin { \theta } + y _ { 1 } \cos { \theta } ) \rho , } \\ { \xi _ { 2 } = r _ { 2 } ^ { ( 0 ) } \rho \cos { ( \theta + \varphi _ { 2 } ) } = ( x _ { 2 } \cos { \theta } - y _ { 2 } \sin { \theta } ) \rho , } \\ { \eta _ { 2 } = r _ { 2 } ^ { ( 0 ) } \rho \sin { ( \theta + \varphi _ { 2 } ) } = ( x _ { 2 } \sin { \theta } + y _ { 2 } \cos { \theta } ) \rho , } \\ { \xi _ { 3 } = r _ { 3 } ^ { ( 0 ) } \rho \cos { ( \theta + \varphi _ { 3 } ) } = ( x _ { 3 } \cos { \theta } - y _ { 3 } \sin { \theta } ) \rho , } \\ { \eta _ { 3 } = r _ { 3 } ^ { ( 0 ) } \rho \sin { ( \theta + \varphi _ { 3 } ) } = ( x _ { 3 } \sin { \theta } + y _ { 3 } \cos { \theta } ) \rho . } \end{array} \right. } \end{array}
$$

If equations (61) are transformed by means of (64) they will involve only the two dependent variables $\pmb { \rho }$ and $\theta$ ，and they will be necessary conditions for the existence of solutions in which the ratios of the mutual distances are constants. It follows from the first two equations of (61) and (64) after multiplying the results of the transformation by cos $\theta$ and sin $\theta$ and adding,and then by -sin $\theta$ and cos $\theta$ and adding, that

$$
\left\{ \begin{array} { l } { \displaystyle x _ { 1 } \frac { d ^ { 2 } \rho } { d t ^ { 2 } } - 2 y _ { 1 } \frac { d \rho } { d t } \frac { d \theta } { d t } - x _ { 1 } \rho \left( \frac { d \theta } { d t } \right) ^ { 2 } - y _ { 1 } \rho \frac { d ^ { 2 } \theta } { d t ^ { 2 } } } \\ { = - \left\{ \frac { m _ { 2 } ( x _ { 1 } - x _ { 2 } ) } { r _ { 1 , 2 } ^ { 3 } } + \frac { m _ { 3 } ( x _ { 1 } - x _ { 3 } ) } { r _ { 1 , 3 } ^ { 3 } } \right\} \frac { 1 } { \rho ^ { 2 } } , } \\ { \displaystyle y _ { 1 } \frac { d ^ { 2 } \rho } { d t ^ { 2 } } + 2 x _ { 1 } \frac { d \rho } { d t } \frac { d \theta } { d t } - y _ { 1 } \rho \left( \frac { d \theta } { d t } \right) ^ { 2 } + x _ { 1 } \rho \frac { d ^ { 2 } \theta } { d t ^ { 2 } } } \\ { = - \left\{ \frac { m _ { 2 } ( y _ { 1 } - y _ { 2 } ) } { r _ { 1 , 2 } ^ { 3 } } + \frac { m _ { 3 } ( y _ { 1 } - y _ { 3 } ) } { r _ { 1 , 3 } ^ { 3 } } \right\} \frac { 1 } { \rho ^ { 2 } } . } \end{array} \right.
$$

Let

$$
\rho ^ { 2 } { \frac { d \theta } { d t } } = \psi .
$$

Then

$$
2 { \frac { d \rho } { d t } } { \frac { d \theta } { d t } } + \rho { \frac { d ^ { 2 } \theta } { d t ^ { 2 } } } = { \frac { 1 } { \rho } } { \frac { d \psi } { d t } } , \quad \quad \rho \left( { \frac { d \theta } { d t } } \right) ^ { 2 } = { \frac { \psi ^ { 2 } } { \rho ^ { 3 } } } ,
$$

and equations (65) become

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } \rho } { d t ^ { 2 } } - \frac { y _ { 1 } } { x _ { 1 } \rho } \frac { d \psi } { d t } - \frac { \psi ^ { 2 } } { \rho ^ { 3 } } = - \frac { 1 } { x _ { 1 } } \Big \{ \frac { m _ { 2 } ( x _ { 1 } - x _ { 2 } ) } { r ^ { 3 } \scriptscriptstyle { 1 , ~ 2 } } + \frac { m _ { 3 } ( x _ { 1 } - x _ { 3 } ) } { r ^ { 3 } \scriptscriptstyle { 1 , ~ 3 } } \Big \} \frac { 1 } { \rho ^ { 2 } } , } \\ { \displaystyle \frac { d ^ { 2 } \rho } { d t ^ { 2 } } + \frac { x _ { 1 } } { y _ { 1 } \rho } \frac { d \psi } { d t } - \frac { \psi ^ { 2 } } { \rho ^ { 3 } } = - \frac { 1 } { y _ { 1 } } \Big \{ \frac { m _ { 2 } ( y _ { 1 } - y _ { 2 } ) } { r ^ { 3 } \scriptscriptstyle { 1 , ~ 2 } } + \frac { m _ { 3 } ( y _ { 1 } - y _ { 3 } ) } { r ^ { 3 } \scriptscriptstyle { 1 , ~ 3 } } \Big \} \frac { 1 } { \rho ^ { 2 } } . } \end{array} \right.
$$

And the equations which are similarly derived from the last four equations of (61) and of (65) are

$$
\begin{array} { r } { \{ \frac { d ^ { 2 } \rho } { d t ^ { 2 } } - \frac { y _ { 2 } } { x _ { 2 } \rho } \frac { d \psi } { d t } - \frac { \psi ^ { 2 } } { \rho ^ { 3 } } = - \frac { 1 } { x _ { 2 } } \Bigl \{ \frac { m _ { 1 } ( x _ { 2 } - x _ { 1 } ) } { r ^ { 3 } _ { 1 } , ~ 2 } + \frac { m _ { 3 } ( x _ { 2 } - x _ { 3 } ) } { r ^ { 3 } _ { 2 } , ~ 3 } \Bigr \} \frac { 1 } { \rho ^ { 2 } } , } \\ { \frac { d ^ { 2 } \rho } { d t ^ { 2 } } + \frac { x _ { 2 } } { y _ { 2 } \rho } \frac { d \psi } { d t } - \frac { \psi ^ { 2 } } { \rho ^ { 3 } } = - \frac { 1 } { y _ { 2 } } \Bigl \{ \frac { m _ { 1 } ( y _ { 2 } - y _ { 1 } ) } { r ^ { 3 } _ { 1 } , ~ 2 } + \frac { m _ { 3 } ( y _ { 2 } - y _ { 3 } ) } { r ^ { 3 } _ { 2 } , ~ 3 } \Bigr \} \frac { 1 } { \rho ^ { 2 } } ; } \\ { \frac { d ^ { 2 } \rho } { d t ^ { 2 } } - \frac { y _ { 3 } } { x _ { 3 } \rho } \frac { d \psi } { d t } - \frac { \psi ^ { 2 } } { \rho ^ { 3 } } = - \frac { 1 } { x _ { 3 } } \Bigl \{ \frac { m _ { 1 } ( x _ { 3 } - x _ { 1 } ) } { r ^ { 3 } _ { 1 } , ~ 3 } + \frac { m _ { 2 } ( x _ { 3 } - x _ { 2 } ) } { r ^ { 3 } _ { 2 } , ~ 3 } \Bigr \} \frac { 1 } { \rho ^ { 2 } } , } \\ { \frac { d ^ { 2 } \rho } { d t ^ { 2 } } + \frac { x _ { 3 } } { y _ { 3 } \rho } \frac { d \psi } { d t } - \frac { \psi ^ { 2 } } { \rho ^ { 3 } } = - \frac { 1 } { y _ { 3 } } \Bigl \{ \frac { m _ { 1 } ( y _ { 3 } - y _ { 1 } ) } { r ^ { 3 } _ { 1 } , ~ 3 } + \frac { m _ { 2 } ( y _ { 3 } - y _ { 2 } ) } { r ^ { 3 } _ { 2 } , ~ 3 } \Bigr \} \frac { 1 } { \rho ^ { 2 } } . } \end{array}
$$

Equations (67) and (68) are necessary conditions for the existence of solutions in which the ratios of the distances of the bodies are constants. There are but two variables, $\rho$ and $\psi$ to be determined. The first gives the dimensions of the system by means of (63),and the second its orientation by means of (66)．In order that the solutions in question may exist these equations must be consistent. In pairs of two they define $\pmb { \rho }$ and $\psi$ when the initial conditions are specified. In order that for given initial conditions the $\pmb { \rho }$ and $\psi$ shall be identical as defined by each of the three pairs of differential equations,the coefficients of corresponding terms in $\pmb { \rho }$ and $\psi$ must be the same. This can be proved by considering the expansion of the solutions as power series in $t - t _ { 0 }$ by the method of Art.127.In order that the solutions shall be the same the coefficients of corresponding powers of $t \mathrm { ~ - ~ } t _ { 0 }$ must be identical; and in order that these conditions shall be satisfied the coefficients of corresponding terms in the differential equations must be identical. Therefore the conditions for the consistency of equations (67) and (68) are either

$$
\begin{array} { r } { \frac { \mathcal { Y } _ { 1 } } { x _ { 1 } } = \frac { \mathcal { Y } _ { 2 } } { x _ { 2 } } = \frac { \mathcal { Y } _ { 3 } } { x _ { 3 } } , } \end{array}
$$

or

$$
\stackrel { d \psi } { \bar { d t } } = 0 ,
$$

and the system of six equations

$$
\{ \begin{array} { l l } { \frac { m _ { 0 } ( x _ { 1 } , \ - x _ { 3 } ) } { r _ { 3 } ^ { 3 } , y } + \frac { m _ { 0 } ( x _ { 1 } , \ - x _ { 3 } ) } { r _ { 1 } ^ { 3 } , } } & { = } \\ { \frac { m _ { 1 } ( x _ { 2 } , \ - x _ { 1 } ) } { r _ { 3 } ^ { 3 } , y } + \frac { m _ { 0 } ( x _ { 2 } , \ - x _ { 3 } ) } { r _ { 2 } ^ { 3 } , y } } & { = } \\ { \frac { m _ { 1 } ( x _ { 3 } , \ - x _ { 1 } ) } { r _ { 3 } ^ { 3 } , y } + \frac { m _ { 0 } ( x _ { 3 } , \ - x _ { 3 } ) } { r _ { 2 } ^ { 3 } , z _ { 3 } } } & { = } \\ { \frac { m _ { 1 } ( x _ { 3 } , \ - x _ { 3 } ) } { r _ { 3 } ^ { 3 } , z _ { 3 } } + \frac { m _ { 0 } ( x _ { 3 } , \ - x _ { 3 } ) } { r _ { 2 } ^ { 3 } , z _ { 3 } } } & { = } \\ { \frac { m _ { 0 } ( y _ { 1 } , \ - y _ { 3 } ) } { r _ { 3 } ^ { 3 } , z } + \frac { m _ { 0 } ( y _ { 1 } , \ - y _ { 3 } ) } { r _ { 1 } ^ { 3 } , z } } & { = } \\ { \frac { m _ { 1 } ( y _ { 2 } , \ - y _ { 1 } ) } { r _ { 3 } ^ { 3 } , z } + \frac { m _ { 0 } ( y _ { 2 } , \ - y _ { 3 } ) } { r _ { 3 } ^ { 3 } , z } } & { = } \\ { \frac { m _ { 1 } ( y _ { 3 } , \ - y _ { 1 } ) } { r _ { 3 } ^ { 3 } , z } + \frac { m _ { 0 } ( y _ { 3 } , \ - y _ { 3 } ) } { r _ { 3 } ^ { 3 } , z } } & { = } \\ { \frac { m _ { 1 } ( y _ { 3 } , \ - y _ { 1 } ) } { r _ { 3 } ^ { 3 } , z } + \frac { m _ { 2 } ( y _ { 3 } , \ - y _ { 3 } ) } { r _ { 3 } ^ { 3 } , z } } & { = } \\  \frac { m _ { 1 } ( y _ { 1 } , \ - y _ { 1 } ) } { r _ { 3 } ^ { 3 } , z } + \frac  m _ { 2 } ( \end{array}
$$

where $n ^ { 2 }$ is the common constant value of the brackets in the right members of (67) and (68). And it follows from equations (71), as well as from the original definitions of the $\pmb { x _ { i } }$ and the $y _ { i } ,$ that the center of mass equations

$$
\left\{ \begin{array} { l l } { m _ { 1 } x _ { 1 } + m _ { 2 } x _ { 2 } + m _ { 3 } x _ { 3 } = 0 , } \\ { m _ { 1 } y _ { 1 } + m _ { 2 } y _ { 2 } + m _ { 3 } y _ { 3 } = 0 , } \end{array} \right.
$$

are fulfilled.

Equations (69) are satisfied only if the three bodies are in a straight line at $t = t _ { 0 }$ .Since，by hypothesis,the shape of the configuration is constant,they always remain in a straight line in this case. The position of the axes can be so chosen at $t = t _ { 0 }$ that $y _ { 1 } = y _ { 2 } = y _ { 3 } = 0$ and the conditions for the existence of the solutions reduce to the first three equations of (71). These equations are the same as (55)of Art.165,and it was shown in Art.167 that they have but three real solutions.

Suppose equations (69) are satisfied and that the bodies remain colinear; therefore the resultant of all the forces to which each one is subject is directed constantly toward the center of gravity of the system,and consequently the law of areas with respect to this point holds. Hence

$$
{ r _ { 1 } } ^ { 2 } { \frac { d \theta } { d t } } = c _ { 1 } , { \gamma _ { 2 } } ^ { 2 } { \frac { d \theta } { d t } } = c _ { 2 } , r _ { 3 } { } ^ { 2 } { \frac { d \theta } { d t } } = c _ { 3 } ,
$$

where $c _ { 1 } , ~ c _ { 2 } ,$ and $c _ { 3 }$ are constants. It follows from (63） that. $\rho ^ { 2 } \frac { d \theta } { d t } = \frac { c _ { 1 } } { ( { r _ { 1 } } ^ { ( 0 ) } ) ^ { 2 } }$ r）,and then from (66) that $\frac { d \psi } { d t } = 0$ Hence equations (66),(67),and (68) become in this case

$$
\left\{ \begin{array} { c } { { \displaystyle \frac { d ^ { 2 } \rho } { d t ^ { 2 } } - \frac { \psi ^ { 2 } } { \rho ^ { 3 } } = { } - n ^ { 2 } \frac { 1 } { \rho ^ { 2 } } , } } \\ { { { } ~ \psi = c _ { 0 } = \mathrm { c o n s t a n t } , } } \\ { { \displaystyle \frac { d \theta } { d t } = \frac { \psi } { \rho ^ { 2 } } = \frac { c _ { 0 } } { \rho ^ { 2 } } . } } \end{array} \right.
$$

These are the differential equations in polar coordinates for the Problem of Two Bodies.Except for differences of notation, they are the same as equations (65) of chap.v. Therefore $\pmb { \rho }$ and $\theta$ satisfy the conditions of conic section motion under the law of gravitation,and it follows from (63)and the definition of $\theta$ that the three bodies describe similar conic sections having an arbitrary eccentricity. These solutions include the straight line solutions in which the orbits are circles as a special case.

Suppose equations (69) are not satisfied；then the bodies are not collinear. But if the bodies are not collinear equation (70) must hold in order that equations (67) and (68) may be compatible.It follows from equations (66) and (63) that the law of areas with respect to the origin holds for each body separately. It was shown in Art. 166 that equations (71) are satisfied if the bodies are at the vertices of an equilateral triangle. It is easy to show that,unless they are collinear, there is no other solution. In the case of the equilateral triangle solution equations (67) and (68) also reduce to (72),and the orbits are similar conic sections of arbitrary eccentricity.

# XXII. PROBLEMS.

1.Take as an hypothesis that a solution exists in which the three bodieg are always collinear. Prove that the law of areas holds for each body separately with respect to the center of mass of the system,with respect to either of the other bodies,and with respect to the center of mass of any two of the bodies.

2.Write the conditions that the accelerations to which the bodies are subject shall be directed toward their common center of mass and proportional to their respective distances.

Ans. Equations (55).

3.The resultant of the forces acting on each body always passes through a fixed point. Prove that the equilateral triangle configuration is the only solution of equations (55) unless the bodies lie in a straight line.

4.Suppose $m _ { 1 } = m _ { 2 } = m _ { 3 } = 1 _ { ; }$ ，and that the bodies move according to the equilateral triangular solution．Find the radius of the circle in which a particle would revolve around one of them in the period in which they revolve around their center of mass.

Ans. $R = 3 ~ ^ { \sharp }$

5.Prove that the equilateral triangular circular solutions hold when the mutual attractions of the bodies vary as any power of the distance.

6. Find the number of collinear solutions when the force varies as any power of the distance.

7.Prove that when the force varies inversely as the fifth power one solution is that each of the bodies moves in a circle through their center of mass in such a way that the three bodies are always at the vertices of an equilateral triangle.

8.Prove that if the three bodies are placed at rest in any one of the configurations admitting circular solutions,they will fall to their center of mass in the same time in straight hnes.

9.Find the distribution of mass among the three bodies for which the time of falling to their center of mass will be the least;the greatest.

10.Prove that if any four masses are placed at the vertices of a regular tetrahedron,the resultant of all the forces acting on each body passes through the center of mass of the four,and that the magnitudes of the accelerations are proportional to the respective distances of the bodies from their center of mass.

11.Prove that there are no circular solutions in the Problem of Four Bodies in which the bodies do not all move in the same plane.

12.Investigate the stability of the triangle and straight line solutions of the Problem of Three Bodies when all of the masses are finite.

# HISTORICAL SKETCH AND BIBLIOGRAPHY.

The first particular solutions of the Problem of Three Bodies were found by Lagrange in his prize memoir,Essai sur le Probleme des Trois Corps,which was submitted to the Paris Academy in 1772 (Coll.Works,vol.v1.,p. 229, Tisserand's Méc.Cel.vol.1.,chap.vii1.)．The solutions which he found are precisely those given in the last part of this chapter.His method was to divide the problem into two parts; $( a )$ the determination of the mutual distances of the bodies, $( b )$ having solved $( a )$ ，the determination of the plane of the triangle in space and the orientation of the triangle in the plane. He proved that if the part $( a )$ were solved the part $( b )$ could also be solved. To solve $( a )$ it was necessary to derive three differential equations involving the three mutual distances alone as dependent variables. He found three equations,one of which was of the third order,and the remaining two of the second order each,making the whole problem of the seventh order.The reduction of the general problem of three bodies by the ten integrals leaves it of the eighth order;hence Lagrange's analysis reduced the problem by one unit. He found that he could integrate the differential equations completely by assuming that the ratios of the mutual distances were constants. The demonstration was repeated by Laplace in the Mécanique Céleste,vol.v.,p.31o. In l'Exposition du Systeme du Monde he remarked that if the moon had been given to the earth by Providence to illuminate the night,as some have maintained, the end sought has been only imperfectly attained; for,if the moon were properly started in opposition to the sun it would always remain there relatively,and the whole earth would have either the full moon or the sun always in view. The demonstration upon which he based his remark was made under the assumption that there was no disturbing force. If there were disturbing forces the configuration would not be preserved unless the solution were stable, which it is not,as was proved by Liouville, Journal de Mathematiques, vol. vI1., 1845.

A number of memoirs_have appeared following more or less closely along the lines marked out by Lagrange. Among them may be mentioned one by Radau in the Bulletin Astronomique,vol.I1.,p.113；by Lindstedt in the Annales del'Ecole Normale,3rd series,vol.1.,p.85;byAllegret in theJournal de Mathematiques,1875,p.277; by Bour in the Journal de l'Ecole Polytechnique, vol.xxxvi.；and by Mathieu in the Journal de Mathématiques,1876,p.345.

Jacobi,without a knowledge of the work of Lagrange,reduced the general Problem of Three Bodies to the seventh order in Crelle's Journal,1843,p. 115 (Coll.Works,vol.Iv.,p.478).It has never been reduced further.

Concerning the solutions of the problem of more than three bodies in which the ratios of the mutual distances are constants a number of papers have appeared,among which are one by Lehmann-Filhes in the Astronomische Nachrichten,vol.cxxvI1.,p.137,one by F.R.Moulton in The Transactions of the American Mathemalical Society,vol.1.,p.17,and one by W.R.Longley in Bulletin of the American Mathematical Society,vol. xIi.,p.324.

No new periodic solutions of the problem of three bodies were discovered after those of Lagrange until Hill developed his Lunar Theory,The American Journal of Mathematics,vol.1. (1878). These solutions of Hill are of immensely greater practical value than those of the Lagrangian type.It should be stated,however, that they are not strictly periodic solutions of any actual case,because a small part of the perturbing action of the sun was neglected.

![](images/ae397da57bb66322ef3c107729ba7dabb33295dc6a651352b5cd9f005722407f.jpg)

The next important advance was made by Poincaré in a memoir in the Bulletin Astronomique,vol.I.,in which he proved that when the masses of two of the bodies are small compared to that of the third,there is an infinite number of sets of initial conditions for which the motion is periodic. These ideas were elaborated and the results extended in a memoir crowned with the prize offered by the late King Oscar of Sweden. This memoir appeared in Acta Mathematica，vol.xiI1. The methods employed by Poincaré are incomparably more profound and powerful than any previously used in Celestial Mechanics,and mark an epoch in the development of the science. The work of Poincaré was recast and extended in many directions, and published in three volumes entitled,Les Méthodes Nouvelles de la Mécanique Celeste.It is written with admirable directness and clearness,and is given in suffcient detail to make so profound a work as easily read as possible.

An important memoir on Periodic Orbits by Sir George Darwin appeared in Acta Mathematica,vol.xxi.(1899).In this investigation it was assumed that one of the three masses is infinitesimal and that the finite masses,having the ratio of ten to one,revolve in circles.A large number of periodic orbits,belonging to a number of families,were discovered by numerical experiments. The question of their stability was answered by using essentially the method employed by Hill in his discussion of the motion of the lunar perigee.

A considerable number of investigations in the domain of periodic orbits, employing analytical processes based on the methods of Poincaré,have been published by F.R.Moultonand his former students Daniel Buchanan,Thomas Buck,F.L.Griffin,Wm.R. Longley,and W.D.MacMillan. These papers have appeared in the Transactions of the American Mathematical Society,the Proceedings of the London Mathematical Society, the Mathematische Annalen, and the Proceedings of the Fifth International Congress of Mathematicians. Besides containing the analysis for a great variety of periodic orbits,they show the existence of infinite sets of closed orbits of ejection which form the boundaries between different classes of periodic orbits. These investigationg are published under the title“Periodic Orbits ”as Publication 161 of the Carnegie Institution of Washington.

# CHAPTER IX.

# PERTURBATIONS-GEOMETRICAL CONSIDERATIONS.

170.Meaning of Perturbations. It was shown in chapter v. that if two spherical bodies move under the influence of their mutual attractions each describes a conic section with respect to their center of mass as a focus,and that the path of each body with respect to the other is a conic. The converse theorem is also true; that is, if the law of areas holds and if the orbit of one body is a conic with respect to the other as a focus, then if the force depends only on the distance it varies inversely as the square of the distance (see also Art.58). If there is a resisting medium, or if either of the bodies is oblate,or if there is a third body attracting the two under consideration,or if there is any force acting upon the bodies other than that of the mutual attractions of the two spheres,their orbits will cease to be exact conic sections. Suppose the coordinates and components of velocity are given at a definite instant $t _ { 0 }$ ;then,if the conditions of the two-body problem were precisely fulfilled，the orbits would be definite conics in which the bodies would move so as to fulfill the law of areas. The differences between the coordinates and the components of velocity in the actual orbits and those which the bodies would have had if the motion had been undisturbed are the perturbations. It is necessary to include the changes in the components of velocity as perturbations,for the paths described depend not only upon the relative positions of the bodies and the forces to which they are subject,but also upon the relative velocities with which they are moving.

Several methods of computing perturbations have been devised depending upon the somewhat diferent points of view which may be taken. Of these the two following are the ones most frequently used.

171.Variation of Coördinates. The simplest conception of perturbations is that the coordinates are directly perturbed.Fcr example,if a planet is subject to the attraction of another planet the coordinates and components of velocity of the former at any time $\pmb { t }$ differ by definite amounts from what they would have been if the sun had been the only source of attraction,and these differences are computed by appropriate devices. No attempt is made to get the equations of the curve described,and usually no general information as to what will happen in the course of a long time is secured. This method is applied only to comets and small planets.

172.Variation of the Elements. This method is variously called the Variation of the Elements, the Variation of Parameters, and the Variation of the Constants of Integration. According to this conception,a body subject to the law of gravitation is always moving in a conic section,but in one which changes at each instant. The variable conic is tangent to the actual orbit at every point of it；and further, if the body were moving undisturbed in any one of the tangent conics it would have the same velocity at the point of tangency which it has in the actual orbit at that point. This conic is said to osculate with the actual orbit at the point of contact. The perturbations are the differences between the elements of the orbit on the start,and those of the osculating conic at any time. An obvious advantage of this method is that the elements change very slowly，since in most of the cases which actually arise in the solar system the perturhing forces are small. But if the perturbations were very large,as they are in some of the multiple star systems,this method would lose its relative advantages.

![](images/f6d9d2272d3343ab52249857c436262e518180f5d21d376ad11681926ec085ca.jpg)  
Fig. 43.

The conception of perturbations as being variations of the elements arises quite naturally in considering the factors which determine the elements of an orbit. It was shown in chap.v. that the initial positions of the two bodies and the directions of projection determine the plane of the orbit; that the initial positions and the velocities of projection determine the length of the major axis;and that the initial conditions,including the direction of projection and the velocities,determine the eccentricity and the line of the apsides.

Suppose a body m is projected from $P _ { 0 }$ ,Fig.43,in the direction $Q _ { 0 }$ with the velocity $V _ { 0 }$ .Suppose there are no forces acting upon it except the attraction of $\boldsymbol { s }$ ; then,in accordance with the results of the two-body problem,it follows that it will move in a conic section $C _ { 0 }$ whose elements are uniquely determined. Suppose that when it arrives at $P _ { 1 }$ it becomes subject to an instantaneous impulse of intensity $f _ { 1 }$ in the direction $P _ { 1 } Q _ { 1 }$ ； this position and the new velocity and direction of motion determine a new conic $C _ { 1 }$ in which the body will move until it is again disturbed by some external force. Suppose it becomes subject to the impulse $f _ { 2 }$ in the direction $P _ { 2 } Q _ { 2 }$ when it arrives at $P _ { 2 }$ ; it will move in the new conic $C _ { 2 }$ ，This may be supposed to continue indefinitely. The body will be moving in conic sections which change from time to time when it is subject to the disturbing impulses. Suppose the instantaneous impulses become very small,and that the intervals of time between them become shorter and shorter. The general characteristics of the motion will remain the same. At the limit the impulses become a continually disturbing force,and the orbit a conic section which continually changes.

173.Derivation of the Elements from a Graphical Construction. It was shown in Art.89 that the major semi-axis is given by the very simple equation

$$
V ^ { 2 } = k ^ { 2 } ( S + m ) \left( \frac { 2 } { r } - \frac { 1 } { a } \right) ,
$$

where $V$ is the initial velocity, $k ^ { 2 }$ the Gaussian constant, $\beta + m$ the sum of the masses, $\boldsymbol { r }$ the initial distance of the bodies from each other,and $^ a$ the major semi-axis. Suppose the major semiaxis has been computed by (1); it will be shown how the remaining elements can be found by the aid of very simple geometrical constructions. The initial positions of $\boldsymbol { S }$ and $m$ ,and the direction of projection of $\pmb { m }$ ，determine the position of the plane of the orbit,and therefore $\boldsymbol { \Omega }$ and $_ { i }$

Suppose $\pmb { m }$ is at the point $P$ at the origin of time,and that it is projected in the direction $P Q$ with the velocity $V$ .The sun $\boldsymbol { s }$ is at one of the foci. It is known from the properties of conic sections that the lines from $P$ to the two foci make equal angles with the tangent $P Q$ 、Draw the line $_ { P R }$ making the same angle with the tangent that $_ { S P }$ makes. Let $\pmb { r _ { 1 } }$ represent the distance from $\pmb { S }$ to $P$ ，and $\pmb { r _ { 2 } }$ the distance from $\pmb { P }$ to the second focus. Therefore $r _ { 1 } + r _ { 2 } = 2 a$ ；or， $r _ { 2 } = 2 a - r _ { 1 } , $ which defines the position of $S _ { 1 }$ .Call the mid-point of $\mathbf { \boldsymbol { S } } \mathbf { \boldsymbol { S } } _ { 1 }$ ， $O$ ；then $e = { \frac { S O } { a } }$ Suppose $S \varOmega$ is the line of nodes； then the angle $\Omega \ : S A = \omega .$ and $\pi = \omega + \delta \delta$

![](images/acb439a8b9c25ec4a1d0def66e273719dbceca9e923d47ba62919537ea9e9d1d.jpg)  
Fig. 44.

The only element remaining to be found is the time of perihelion passage. The angle $A S P$ ，counted in the direction of motion, is $v$ .The eccentric anomaly is given by the equation (Art. 98)

$$
\tan { \frac { E } { 2 } } = { \sqrt { \frac { 1 - e } { 1 + e } } } \tan { \frac { v } { 2 } } .
$$

After $\pmb { \cal E }$ has been found the time of perihelion passage, $\pmb { T }$ ,is defined by the equation (Art.93)

$$
\begin{array} { r } { n ( t - T ) = E - e \sin E . } \end{array}
$$

174.Resolution of the Disturbing Force. Whatever may be the source of the disturbing force it is convenient,in order to find its effects upon the elements,to resolve it into three rectangular components. It is possible to do this in several ways,each having advantages for particular purposes. The one will be adopted here which on the whole leads most simply to the determination of the manner in which the elements vary when the body under consideration is subject to any disturbing force. It would be possible without much difficulty to derive from geometrical considerations the expressions for the rates of change of the elements for any disturbing forces,but the object of this chapter is to explain the nature and causes of perturbations of various sorts, and the attention will not be divided by unnecessary digressions on methods of computation. This part falls naturally to the methods of analysis,which willbe given in the next chapter.

The disturbing force will be resolved into three rectangular components: $( a )$ the orthogonal component,\* S，which is perpendicular to the plane of the orbit,and which is taken positive when directed toward the north pole of the ecliptic； $( b )$ the tangential component, $T$ ，which is in the line of the tangent,and which is taken positive when it acts in the direction of motion; and $( c )$ the normal component, $N$ ，which is perpendicular to the tangent,and which is taken positive when directed to the interior of the orbit.

The instantaneous effects of these components upon the various elements will be discussed separately；and, unless it is otherwise stated, it always must be understood that the results refer to the way in which the elements are changing at given instants,and not to the cumulative effects of the disturbing forces. Although the effects of the different components are considered separately,yet when two or more act simultaneously it is sometimes necessary to estimate somewhat carefully the magnitude of their separate perturbations,in order to determine the character of their joint effects.

I.EFFECTS OF THE COMPONENTS OF THE DISTURBING FORCE.

175.Disturbing Effects of the Orthogonal Component. In order $^ { \dag , _ { 0 } }$ fix the ideas and abbreviate the language it will be supposed that the disturbed body is the moon moving around the earth. The perturbations arising from the disturbing action of the sun are very great and present many features of exceptional interest. Besides， this is the case which Newton treated by methods essentially the same as those employed here.† The

\*A designation due to Sir John Herschel, Outlines of Astronomy, p.420.   
+ Principia, Book 1.,Section 11,and Book II1., Props xx.-xxxv.

character of the perturbations arising from positive components alone will be investigated；in every case negative components change the elements in the opposite way.

It is at once evident that the orthogonal component will not change $a , e , T ,$ and $\omega$ ,if $\omega$ is counted from a fixed line in the plane of the orbit.But the $\omega$ in ordinary use is counted from the ascending node of the orbit;hence if the negative of the rate of jncrease of $\ d \Omega$ be multiplied by cos $_ i$ the result will be the rate of increase of $\omega$ due to the change in the origin from which it is reckoned. Consequently it is sufficient to consider the changes in $\boldsymbol { \Omega }$ and $\textit { i }$ when discussing the perturbations due to the orthogonal component.

![](images/96ab875b6bd2aae2bd0b8a3e19f505d94479a3f2d1478ca145555e3ccc03fe3d.jpg)  
Fig. 45.

Let $A B$ be in the plane of the ecliptic, $P _ { 0 } Q _ { 0 }$ in the plane of the undisturbed orbit，and $\boldsymbol { \Omega } _ { 0 }$ and $\dot { \iota _ { 0 } }$ the corresponding node and inclination. Suppose there is an instantaneous impulse $P _ { 0 } S _ { 0 }$ when the moon is at $P _ { 0 }$ ； it will then move in the direction $P _ { 0 } P _ { 1 }$ ， and the new node and inclination will be $\boldsymbol { \partial } _ { 1 }$ and $i _ { 1 }$ ，It is evident at once that ${ \dot { \iota } } _ { 1 } > { \dot { \iota } } _ { 0 }$ and $\delta \boldsymbol { { \mathbf { \mathit { \delta } } } } _ { 1 } < \delta \boldsymbol { { \mathbf { \mathit { \delta } } } } _ { 0 }$ .Suppose a new instantaneous impulse $P _ { 1 } S _ { 1 }$ acts when the moon arrives at $P _ { 1 }$ .The new node and inclination are $\Omega _ { 2 }$ and $i _ { 2 } ,$ and it is evident that $i _ { 2 } < i _ { 1 }$ and $\delta \smash { \delta \mathbf { \ z } ^ { } } < \delta \mathbf { \ z } _ { 1 }$ If $P _ { 0 } \Omega _ { 1 } = \Omega _ { 1 } P _ { 1 ; }$ ， $P _ { 0 } S _ { 0 } = P _ { 1 } S _ { 1 }$ ，and the vclocity of the moon at $P _ { 0 }$ equals that at $P _ { 1 }$ ，then $i _ { 0 } = i _ { 2 }$ .The total result is a regression of the node and an unchanged inclination.

From the corresponding figure at the descending node it is seen that a negative $\boldsymbol { s }$ before node passage and a symmetrically opposite positive $\pmb { S }$ after node passage will produce the same results as those which were found at the ascending node. Therefore,a positive $\boldsymbol { s }$ causes the nodes to advance if the moon is in the first or second quadrant,and to regress if it is in the third or fourth quadrant；and a positive $\pmb { S }$ causes the inclination to increase if the moon is in the first or fourth quadrant,and to decrease if it is in the second or third quadrant.

The following quantitative results may be noted: The rate of change of both $\Omega$ and $\textit { i }$ is proportional to $\boldsymbol { \mathrm { \Sigma } } ^ { g }$ The rate of change of $\displaystyle { \boldsymbol { \partial } }$ is greater the smaller $_ i$ ; for $i = 0$ evidently $\boldsymbol { \Omega }$ is not defined, but in this case in such problems as the Lunar Theory $\boldsymbol { s }$ vanishes. Fora given $\textit { i }$ the rate of change of $\Omega$ is greater the nearer the point at which disturbance occurs is to midway between the two nodes. The rate at which $\romannumeral 1$ changes is greater the nearer the point at which the disturbance occurs is to a node.

176.Effects of the Tangential Component upon the Major Axis. Instead of deriving all the conclusions directly from geometrical constructions,it will be better to make use of some of the simple equations which have been found in chapter v. If it were desired the theorems contained in these equations could be derived from geometrical considerations,as was done by Newton in the Principia,but this would involve considerable labor and would add nothing to the understanding of the subject.

The major semi-axis is given in terms of the initial distance and the initial velocity by equation (1);viz.,

$$
V ^ { 2 } = k ^ { 2 } ( E + m ) \left( \frac { 2 } { r } - \frac { 1 } { a } \right) .
$$

In an elliptic orbit $^ { a }$ is positive; hence, since a positive $\pmb { T }$ increases $V ^ { 2 }$ and does not instantaneously change $r , \ a$ positive $\pmb { T }$ increases the major semi-axis when the moon is in any part of its orbit. It also follows from this equation that a given $\pmb { T }$ is most effective in changing $^ { a }$ when $V$ has its largest value,or when the moon is at the perigee,and that the rate of change is more rapid the larger $^ { a }$

Expressed in terms of partial derivatives, the dependence of $\pmb { a }$ upon $\pmb { T }$ is given by

$$
\frac { \partial a } { \partial T } = \frac { \partial a } { \partial V } \frac { \partial V } { \partial T } = \frac { 2 a ^ { 2 } V } { k ^ { 2 } ( E + m ) } \frac { \partial V } { \partial T } .
$$

177.Effects of the Tangential Component upon the Line of Apsides. The tangential component increases or decreases the speed,but does not instantaneously change the direction of motion.The focus $E$ is of course not changed, $\boldsymbol { r } _ { 1 }$ is unchanged, and,according to the results of the last article, $^ { a }$ is increased. Since $r _ { 2 } = 2 a - r _ { 1 }$ while the direction of $r _ { 2 }$ remains the same, it follows that the focus $E _ { 1 }$ is thrown forward to $E _ { 1 } ^ { \prime }$ ,Fig.46.The line of apsides is rotated forward from $A B$ to $A ^ { \prime } B ^ { \prime }$ .Hence it is easily seen that $^ { a }$ positive tangential component causes the line of apsides to rotate forward during the first half revolution,and back ward during the second half revolution.

The instantaneous.effects are the same for points which are symmetrical with respect to the major axis. When the moon is at $\kappa$ or $L$ the whole displacement of the second focus is perpendicular to the line of apsides,and at these points the rate of rotation of the apsides is a maximum for a given change in the major axis. But the major axis is changed most when the moon is at perigee; therefore the place at which the line of the.apsides rotates most rapidly is near $\kappa$ and $\boldsymbol { L }$ and between these points and the perigee. The rate of rotation of the line of apsides becomes zero when the moon is at perigee or apogee.It should be remembered that the whole problem is complicated by the fact that the magnitude of $\boldsymbol { \mathsf { T } }$ depends upon the distances of both moon and sun, and these distances continually vary.

![](images/09e99c097018462594876f65ffcbc3b0b46990b63c245e0925ccd6a30904f1e6.jpg)  
Fig. 46.

# 178. Effects of the Tangential Component upon the Eccentricity.

Theeentriciyisgivenbytheequation $\ e = { \frac { E E _ { 1 } } { 2 a } } .$ Fig.46.

When the moon is at the perigee $\mathit { \mathbf { E } } \mathit { \mathbf { E _ { 1 } } }$ and $2 a$ are increased by the same amount. Since $E E _ { 1 }$ is less than $2 a$ the eccentricity is increased at this point. When the moon is at apogee ${ \bf 2 } a$ is increased while $E E _ { 1 }$ is decreased equally,hence the eccentricity is decreased. Consequently there is some place between perigee and apogee where the eccentricity is not changed,and it is easy to show that this place is at the end of the minor axis. Let $\pmb { 2 \Delta \alpha }$ represent the instantaneous increase in ${ \bf 2 } a$ when the moon is at $c$ or $D$ ,Fig.47.Then $\mathbf { \boldsymbol { r } _ { 2 } }$ will be increased by the quantity $2 \Delta a$ ， and $\mathit { \mathbf { E E _ { 1 } } }$ by $\Delta E$ If $\pmb \theta$ is the angle $C E _ { 1 } E$ cos $\theta = \frac { E E _ { 1 } } { 2 a } = \frac { 2 a e } { 2 a } = e ,$ and, moreover, $\Delta E = 2 \Delta a$ cos $\theta = 2 e \Delta a$ .Therefore

$$
e ^ { \prime } = \frac { E E _ { 1 } + \Delta E } { 2 a + 2 \Delta a } = \frac { 2 a e + 2 e \Delta a } { 2 a + 2 \Delta a } = e ;
$$

or,the eccentricity is unchanged by the tangential component when the moon is at an end of the minor axis of its orbit.

The changes in the time of perihelion passage depend upon the changes in the period and the direction of the major axis,as well as on the direct perturbations of the longitude in the orbit. Since the period depends upon the major axis alone，whose changes have been discussed, the foundations for an investigation of the changes in the time of perihelion passage have been laid,except in so far as they are direct perturbations in longitude;but further inquiry into this subject will be omitted because geometrical methods are not well suited to such an investigation,and because the time of perihelion passage is an element of little interest in the present connection.

![](images/baac190c49cdeb2800b8a63053a7d5d8565773bc535e7a317fe3261f1c528365.jpg)  
Fig. 47.

179.Effects of the Normal Component upon the Major Axis. It follows from (1） that the major axis depends upon the speed at a given point and not upon the direction of motion. Since the normal component acts at right angles to the tangent,it does not instantaneously change the speed and, therefore, leaves the major axis unchanged.

180.Effects of the Normal Component upon the Line of Apsides. Consider the effect of an instantaneous normal component when the moon is at $P$ ,Fig.48.Let $_ { P T }$ represent the tangent to the orbit. The effect of the normal component will be to change it to $P T ^ { \prime }$ · Since the radii to the two foci make equal angles with the tangent the radius $\pmb { r _ { 2 } }$ will be changed to ${ r _ { 2 } } ^ { \prime }$ ； and, since the normal com-ponent does not affect the length of the major axis, $\pmb { r _ { 2 } }$ and ${ \boldsymbol { r } } _ { 2 } ^ { \prime }$ will be of equal length. Consequently,when the moon is in the region LAK α positive normal component will rotate the line of apsides forward, and when it is in the region KBL,backward. At the points $\kappa$ and $L$ the normal component does not change the direction of the line of apsides.

![](images/70ed9702fad20221e0acb2da732ae290b6b78f50c1eda411979555d2c41b4da4.jpg)  
Fig. 48.

In the applications to the perturbations of the moon it will be important to determine the relative effectiveness of a given normal force in changing the line of apsides when the moon is at the two positions $A$ and $B$ ：When the moon is at either of these two points the second focus $E _ { 1 }$ is displaced along the line $\kappa L$ The effectiveness of a force in changing the direction of motion of a body is inversely proportional to the speed with which it moves; but by the law of areas the velocities at $A$ and $B$ are inversely proportional to their distances from $\boldsymbol { \mathbf { \mathit { E } } }$ Let $E _ { A }$ and $E _ { B }$ represent the effectiveness of a given force in changing the direction of motion at $A$ and $B$ respectively,and let $V _ { A }$ and $V _ { B }$ represent the velocities at the same points. Then

$$
{ \cal E } _ { \cal A } : { \cal E } _ { \cal B } = { \cal V } _ { \cal B } : { \cal V } _ { \cal A } = a ( 1 - e ) : a ( 1 + e ) .
$$

The rotation of the line of apsides is directly proportional to the displacement of $E _ { 1 }$ along the line $K L$ .The displacements along $\kappa L$ are directly proportional to the products of the lengths of the radii from $A$ and $B$ to $E _ { 1 }$ and the angles through which they are rotated. But the angles are proportional to $E _ { A }$ and $E _ { B }$ ，and the lengths of the radii to $E _ { 1 }$ to $a ( 1 + e )$ and $a ( 1 - e )$ .Therefore,letting $R _ { A }$ and $R _ { B }$ represent the rotation of the line of apsides at the two points,it follows that

$$
R _ { A } : R _ { B } = a ( 1 + e ) E _ { A } : a ( 1 - e ) E _ { B } = 1 : 1 ;
$$

or,equal instantaneous normal forces produce equal, but oppositely directed, rotations of the line of apsides when the moon is at apogee and at perigee.

Suppose the forces act continuously over small arcs. Since the linear velocities are inversely as the radii， the effectiveness,in changing the direction of the line of apsides,of a constant force acting through a small arc at $A$ is to that of an equal force acting through an equal arc at $B$ as $a ( 1 - e )$ is to $a ( 1 + e )$ .In practice the disturbing iorces are not instantaneous but act continuously, thcir magnitudes depending upon the positions of the bodies; consequently，unless the normal component is smaller at apogee than at perigee the average rotation of the line of apsides due to a normal component always having the same sign is in the direction of the rotation when the moon is at apogee.

181. Effects of the Normal Component upon the Eccentricity. f $2 a$ represents the major axis, the eccentricity is given by

$$
e = { \frac { E E _ { 1 } } { 2 a } } .
$$

After the action of the normal component the eccentricity is

$$
e ^ { \prime } = { \frac { E E _ { 1 } ^ { \prime } } { 2 a } } ,
$$

the major axis being unchanged. It is easily seen from Fig.48 that $^ { a }$ positive normal force decreases the eccentricity during the first half revolution and increases it during the second half, $E E _ { 1 } { ' }$ being less than $E F _ { 1 }$ in the first case,and greater in the second. The instantaneous change in the eccentricity vanishes when the moon is at $A$ or $B$

It follows from Fig. 48 that a given change in the direction of $r _ { 2 }$ produces a greater change in the eccentricity when the moon is in the second or third quadrant than when the moon is in a corresponding part of the first or fcurth quadrant. Besides this, the moon moves slower the farther it is from the earth,and consequently a given normal component is more effective in changing the direction of motion,and therefore of $r _ { 2 } .$ ，when the moon is near apogee than when it is near perigee. Hence a given normal component causes greater changes in the eccentricity if the moon is near apogee than it does if the moon is near perigee.

182.Table of Results. The various results obtained will be of constant use in the applications which follow,and they will be most convenient when condensed into a table. The results are given for only positive values of the disturbing components； for negative components they are the opposite in every case.

![](images/c3e57e7dad84a542ea60b11e3e86fba5b9e306d77165666b7b43524dbeb994c0.jpg)  
Fig. 49.

The orthogonal component, $\pmb { S }$ ,is positive when directed toward the north pole of the ecliptic.

The tangential component, $\pmb { T } _ { : }$ ,is positive when directed in the direction of motion.

The normal component, $N$ ，is positive when directed to the interior of the ellipse.

<table><tr><td rowspan=1 colspan=1>Component...</td><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>N</td></tr><tr><td rowspan=1 colspan=1>Nodes......</td><td rowspan=1 colspan=1>Advance in firstand second quad-rants；regress,inthird and fourthquadrants.</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Inclination....</td><td rowspan=1 colspan=1>Increases in firstand fourth quad-rants；decreasesinsecondandthird quadrants.</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Major Axis...</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>Always increases</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Line of Apsides</td><td rowspan=1 colspan=1>No effect ifωiscounted from afixed point ratherthan from &amp;.</td><td rowspan=1 colspan=1>In interval ACB,forward;In interval BDA,backward</td><td rowspan=1 colspan=1>In interval LAK,forward;In intervai KBL,backward</td></tr><tr><td rowspan=1 colspan=1>Eccentricity...</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>In interval DAC,increases;In interval&#x27;CBD,decreases</td><td rowspan=1 colspan=1>In interval ACB,decreases;In interval BDA,increases</td></tr></table>

183.Disturbing Effects of a Resisting Medium. The simplest disturbance of eliptic motion is that arising from a resisting medium. The only disturbing force is a negative tangential component,which has the same magnitude for points symmetrically situated with respect to the major axis. Therefore,it is seen from the Table that:(1) $\Omega$ and $\textit { i }$ are unchanged； (2) $^ { a }$ is continually decreased；(3） the line of apsides undergoes periodic variations, rotating backward during the first half revolution, and rotating forward equally during the second half； (4) the eccentricity decreases while the body moves through the interval DAC,and increases during the remainder of the revolution. It takes the body longer to move through the arc CBD than through DAC;but,on the other hand,if the resistance depends on a high power of the velocity,as experiment shows it does for high velocities,the change is much greater at perigee than at apogee,and the whole effect in a revolution is a decrease in the eccentricity. The application of these results to a comet，planet，or satellite resisted by meteoric matter,or possibly the ether,is evident.

184.Perturbations Arising from Oblateness of the Central Body. Consider the case of a satellite revolving around an oblate planet in the plane of its equator. It was shown in equations (30),p.122,that the attraction under these circumstances is always greater than that of a concentric sphere of equal mass,but that the two attractions approach equality as the satellite recedes. The excess of the attraction of the spheroid over that of an equal sphere will be considered as being the disturbing force，which, it will be observed, acts in the line of the radius vector and is always directed toward the planet. Therefore the normal com-

![](images/ecbf4ad3bf5b2c3674245d0535667856c098b3a0e8850698475ae5641ed918c9.jpg)  
Fig. 50.