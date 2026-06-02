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
