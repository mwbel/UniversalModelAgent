# CHAPTER III.

CENTRAL FORCES.

45.Central Force. This chapter will be devoted to the discussion of the motion of a material particle when subject to an attractive or repelling force whose line of action always passes through a fixed point. This fixed point is called the center of force. It is not implied that the force emanates from the center or that there is but one force,but simply that the resultant of all the forces acting on the particle always passes through this point. The force may be directed toward the point or from it,or part of the time toward and part of the time from it. It may be zero at any time,but if the particle passes through a point where the force to which it is subject becomes infinite,a special investigation,which cannot be taken up here,is required to follow it farther. Since attractive forces are of most frequent occurrence in astronomical and physical problems, the formulas developed will be for this case; a change of sign of the coefficient of intensity of the force for unit distance will make the formulas valid for the case of repulsion.

The origin of coordinates will be taken at the center of force, and the line from the origin to the moving particle is called the radius vector. The path described by the particle is called the orbit. The orbits of this chapter are plane curves. The planes are defined by the position of the center of force and the line of initial projection. The xy-plane will be taken as the plane of the orbit.

46. The Law of Areas. The first problem will be to derive the general properties of motion which hold for all central forces. The first of these,which is of great importance,is the law of areas, and constitutes the first Proposition of Newton's Principia. It is, if a particle is subject to a central force, the areas which are swept over by the radius vector are proportional to the intervals of time in which they are described. The following is Newton's demonstration of it.

Let $o$ be the center of force,and let the particle be projected from $\pmb { A }$ in the direction of $\pmb { B }$ with the velocity $A B$ Then,by the first law of motion, it would pass to $C ^ { \prime }$ in the first two units of time if there were no external forces acting upon it. But suppose that when it arrives at $B$ an instantaneous force acts upon it in the direction of the origin with such intensity that it would move to $^ { b }$ in a unit of time if it had no previous motion. Then,by the second law of motion，it will move along the diagonal of the parallelogram $B b C C ^ { \prime }$ to $\boldsymbol { C }$ .If no other force were applied it would move with uniform velocity to $D ^ { \prime }$ in the next unit of time. But suppose that when it arrives at $c$ another instantaneous force acts upon it in the direction of the origin with such intensity that it would move to $c$ in a unit of time if it had no previous motion． Then,as before,it will move along the diagonal of the parallelogram and arrive at $D$ at the end of the unit of time. This process can be repeated indefinitely.

![](images/93782613a45933aae031377fc91d783e1edb34e81392835756c602de99d31ae2.jpg)  
Fig.7.

The following equalities among the areas of the triangles involved hold, since they have sequentially equal bases and altitudes:

$$
O A B = O B C ^ { \prime } = O B C = O C D ^ { \prime } = O C D = \mathrm { e t c . }
$$

Therefore，it follows that $O A B = O B C = O C D = O D E$ ，etc. That is, the areas of the triangles swept over in the succeeding units of time are equal; and, therefore, the sums of the areas of the triangles described in any intervals of time are proportional to the intervals.

The reasoning is true without any changes however small the intervals of time may be. Let the path be considered for some fixed finite period of time.Let the intervals into which it is divided be taken shorter and shorter; the impulses will become closer and closer together. Suppose the ratio of the magnitudes of the impulses to the values of the intervals between them remains finite;then the broken line will become more and more nearly a smooth curve. Suppose the intervals of time approach zero as a limit； the succession of impulses will approach a continuous force as a limit,and the broken line will approach a smooth curve as a limit. The areas swept over by the radius vector in any finite intervals of time are proportional to these intervals during the whole limiting process. Therefore,the proportionality of areas holds at the limit,and the theorem is true for a continuous central force.

It will be observed that it is not necessary that the central force shall vary continuously. It may be attractive and instantaneously change to repulsion,or become zero,and the law will still hold; but it is necessary to exclude the case where it becomes infinite unless a special investigation is made.

The linear velocity varies inversely as the perpendicular from the origin upon the tangent to the curve at the point of the moving particle;for,the area described in a unit of time is equal to the product of the velocity and the perpendicular upon the tangent. Since the area described in a unit of time is always the same,it follows that the linear velocity of the particle varies inversely as the perpendicular from the origin to the tangent of its orbit.

47. Analytical Demonstration of the Law of Areas. Although the language of Geometry was employed in the demonstration of Art.46,yet the essential elements of the methods of the Differential and Integral Calculus were used. Thus,in passing to the limit,the process was essentially that of expressing the problem in differential equations；and,in insisting upon comparing intervals of finite size when the units of measurement were indefinitely decreased, the process of integration was really employed. It will be found that in the treatment of all problems involving variable forces and motions the methods are in essence those of the Calculus,even though the demonstrations be couched in geometrical language. It is perhaps easier to follow the reasoning in geometrical form when one encounters it for the first time; but the processes are all special and involve fundamental difficulties which are often troublesome. On the other hand, the development of the Calculus is of the precise form to adapt it to the treatment of these problems,and after its principles have been once mastered, the application of it is characterized by comparative simplicity and great generality. A few problems will be treated by both methods to show their essential sameness,and to illustrate the advantages of analysis.

Let $f$ represent the acceleration to which the particle is subject. By hypothesis, the line of force always passes through a fixed point, which will be taken as the origin of coordinates.

Let $o$ be the center of force,and $\pmb { P }$ any position of the particle whose rectangular coordinates are $\pmb { x }$ and $\pmb { y }$ ，and whose polar coordinates are $\pmb { r }$ and $\pmb \theta$ ，Then the components of acceleration along the $\pmb { x }$ and $_ y$ -axes are respectively $\neq f$ cos $\pmb \theta$ and = f sin 0, and the differential equations of motion are

![](images/101d8fa1d601813199f3f83798b60acad92514b2070cc4ddb243bc52087e6b58.jpg)  
Fig. 8.

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } x } { d t ^ { 2 } } = \neq f \cos \theta = \mp f \frac x r , } \\ { \displaystyle \frac { d ^ { 2 } y } { d t ^ { 2 } } = \neq f \sin \theta = \mp f \frac y r . } \end{array} \right.
$$

The negative sign must be taken before the right members of these equations if the force is attractive,and the positive if it is repulsive.

Multiply the frst equation of (1） by $- \pmb { y }$ and the second one by $+ \textit { \textbf { x } }$ and add. The result is

$$
x { \frac { d ^ { 2 } y } { d t ^ { 2 } } } - y { \frac { d ^ { 2 } x } { d t ^ { 2 } } } = 0 .
$$

On integrating this expression by parts, it is found that

$$
x { \frac { d y } { d t } } - y { \frac { d x } { d t } } = h ,
$$

where $\pmb { h }$ is the constant of integration.

The integrals of differential equations generally lead to important theorems even though the whole problem has not been solved，and in what follows they will be discussed as they are obtained.

On referring to Art.16,it is seen that (2) may be written

$$
x { \frac { d y } { d t } } - y { \frac { d x } { d t } } = r ^ { 2 } { \frac { d \theta } { d t } } = 2 { \frac { d A } { d t } } = h ,
$$

where $\pmb { A }$ is the area swept over by the radius vector. The integral of this equation is

$$
\begin{array} { r } { A = \frac { 1 } { 2 } h t + c , } \end{array}
$$

which shows that the area is directly proportional to the time.   
This is the theorem which was to be proved.

48. Converse of the Theorem of Areas. By hypothesis

$$
A = c _ { 1 } t + c _ { 2 } .
$$

On taking the derivative with respect to $t _ { i }$ ,it is found that

$$
\frac { d A } { d t } = c _ { 1 } .
$$

This equation becomes in polar coordinates

$$
r ^ { 2 } { \frac { d \theta } { d t } } = 2 c _ { 1 } ,
$$

and in rectangular coordinates

$$
x { \frac { d y } { d t } } - y { \frac { d x } { d t } } = 2 c _ { 1 } .
$$

The derivative of this expression with respect to $\pmb { t }$ is

$$
x \frac { d ^ { 2 } y } { d t ^ { 2 } } - y \frac { d ^ { 2 } x } { d t ^ { 2 } } = 0 ;
$$

or

$$
{ \frac { d ^ { 2 } x } { d t ^ { 2 } } } : { \frac { d ^ { 2 } y } { d t ^ { 2 } } } = x : y .
$$

That is, the components of acceleration are proportional to the coordinates; therefore, if the law of areas is true with respect to a point,the resultant of the accelerations passes through that point.

Or,since $r ^ { 2 } { \frac { d \theta } { d t } } = 2 c _ { 1 }$ ,it follows that ${ \frac { d } { d t } } \left( r ^ { 2 } { \frac { d \theta } { d t } } \right) = 0 .$ Hence, by (19),Art.14, the acceleration perpendicular to the radius vector is zero;that is, the acceleration is in the line passing through the origin.

49.The Laws of Angular and Linear Velocity. From the expression for the law of areas in polar coordinates, it follows that

$$
{ \frac { d \theta } { d t } } = { \frac { h } { r ^ { 2 } } } ;
$$

therefore,the angular velocity is inersely proportional tothe square of the radius vector.

The linear velocity is

$$
\frac { d s } { d t } = \frac { d s } { d \theta } \frac { d \theta } { d t } = \frac { d s } { d \theta } \frac { h } { r ^ { 2 } } .
$$

Let $\pmb { p }$ represent the perpendicular from the origin upon the tangent; then it is known from Differential Calculus that

$$
\frac { d s } { d \theta } = \frac { r ^ { 2 } } { p } .
$$

Hence the expression for the linear velocity becomes

$$
{ \frac { d s } { d t } } = { \frac { h } { p } } ;
$$

therefore, the linear velocity is inversely proportional to the perpendicular from the origin upon the tangent.

SIMULTANEOUS DIFFERENTIAL EQUATIONS.

50.The Order of a System of Simultaneous Differential Equations. One integral,equation (2),of the differential equations (1)has been found which the motion of the particle must fulfill. The question is how many more integrals must be found in order to have the complete solution of the problem.

The number of integrals which must be found to completely solve a system of differential equations is called the order of the system. Thus, the equation

$$
{ \frac { d ^ { n } x } { d t ^ { n } } } = c
$$

is of the nth order,because it must be integrated $\pmb { n }$ times to be reduced to an integral form. Similarly,the general equation

$$
f _ { n } { \frac { d ^ { n } x } { d t ^ { n } } } + f _ { n - 1 } { \frac { d ^ { n - 1 } x } { d t ^ { n - 1 } } } + \cdots + f _ { 1 } { \frac { d x } { d t } } + f _ { 0 } = 0 ,
$$

where $f _ { n } , \cdots \cdots , f _ { 0 }$ are functions of $_ { \pmb { x } }$ and $t$ ，must be integrated $\pmb { n }$ times in order to express $_ x$ as a function of $t .$ ,and is of the nth order.

An equation of the nth order can be reduced to an equivalent system of $\pmb { n }$ simultaneous equations each of the frst order. Thus, to reduce (6) to a simultaneous system, let

$$
x _ { 1 } = { \frac { d x } { d t } } , \qquad x _ { 2 } = { \frac { d x _ { 1 } } { d t } } , \qquad \cdots \cdots \cdots , \qquad x _ { n - 1 } = { \frac { d x _ { n - 2 } } { d t } } ;
$$

whence

$$
\left\{ \begin{array} { l } { \displaystyle \frac { d x } { d t } = x _ { 1 } , } \\ { \displaystyle \frac { d x _ { 1 } } { d t } = x _ { 2 } , } \\ { \displaystyle \frac { d x _ { 2 } } { d t } = x _ { 3 } , } \\ { \displaystyle \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot } \\ { \displaystyle \frac { d x _ { n - 1 } } { d t } = - \frac { f _ { n - 1 } } { f _ { n } } x _ { n - 1 } - \dots - \frac { f _ { 1 } } { f _ { n } } x _ { 1 } - \frac { f _ { 0 } } { f _ { n } } . } \end{array} \right.
$$

Therefore, these $\mathscr { n }$ simultaneous equations,each of the first order, constitute a system of the nth order. An equation,or a system of equations,reduced to the form (7) is said to be reduced to the normal form,and the system is called a normal system.

Two simultaneous equations of order $_ m$ and $\pmb { n }$ can be reduced to a normal system of order $m + n$ .Consider the equations

$$
\left\{ \begin{array} { l l } { f _ { m } \displaystyle \frac { d ^ { m } x } { d t ^ { m } } + \cdots + f _ { 1 } \displaystyle \frac { d x } { d t } + f _ { 0 } = 0 , } \\ { ~ } \\ { \displaystyle \phi _ { n } \displaystyle \frac { d ^ { n } y } { d t ^ { n } } + \cdots + \phi _ { 1 } \displaystyle \frac { d y } { d t } + \phi _ { 0 } = 0 , } \end{array} \right.
$$

where the $f _ { i }$ and the $\phi _ { \mathbf { i } }$ are functions of $\textstyle { \pmb x } , \ { \pmb y } .$ and $\pmb { t } .$ By a substitution similar to that used in reducing (6),it follows that they are equivalent to the normal system

$$
\left\{ \begin{array} { l }  \displaystyle \begin{array} { c } { \frac { d x } { d t } = x _ { 1 } , } \\ { \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot } \\ { \frac { d x _ { m - 1 } } { d t } = - \frac { f _ { m - 1 } } { f _ { m } } x _ { m - 1 } - \cdot \cdot \cdot - \frac { f _ { 1 } } { f _ { m } } x _ { 1 } - \frac { f _ { 0 } } { f _ { m } } , } \end{array} \right. \end{array}
$$

which is of the order $m + n$ .Evidently a similar reduction is possible when each equation contains derivatives with respect to both of the variables, either separately or as products.

Conversely, $^ { a }$ normal system of order n can in general be transformed into a single equation of order n with one dependent varuible. To fix the ideas, consider the system of the second order

$$
\left\{ \begin{array} { l } { \displaystyle \frac { d x } { d t } = f \left( x , \ y , \ t \right) , } \\ { \displaystyle \frac { d y } { d t } = \phi ( x , \ y , \ t ) . } \end{array} \right.
$$

In addition to these two equations form the derivative of one of them,for example the first,with respect to $\scriptstyle t .$ The result is

$$
{ \frac { d ^ { 2 } x } { d t ^ { 2 } } } = { \frac { \partial f } { \partial x } } { \frac { d x } { d t } } + { \frac { \partial f } { \partial y } } { \frac { d y } { d t } } + { \frac { \partial f } { \partial t } } .
$$

If $\pmb { y }$ and $\frac { d y } { d t }$ areeliminatedbetween(10)and(11)theresult will be an equation of the form

$$
\frac { d ^ { 2 } x } { d t ^ { 2 } } + F \left( x , \frac { d x } { d t } \right) = 0 ,
$$

where $\pmb { F }$ is a function of both $\pmb { x }$ and $\frac { d x } { d t }$ · Of course, $\pmb { f }$ and $\phi$ of equations (1O) may have such properties that the elimination of $\pmb { y }$ and dis very difficult.

If the normal system were of the third order in the dependent variables $\qquad x , \ y _ { \mathrm { { i } } }$ and ${ \pmb z }$ ，the first and second derivatives of the first equation would be taken,and the first derivative of the second and third equations. These four new equations with the original three make seven from which y, z,d，dt， dt， and $\frac { d ^ { 2 } z } { d t ^ { 2 } }$ can in general be eliminated,giving an equation of the third order in $\pmb { x }$ alone. This process can be extended to a system of any order.

The differential equations (1) can be reduced by the substitutior $x ^ { \prime } = { \frac { d x } { d t } }$ d，y' $y ^ { \prime } = { \frac { d y } { d t } }$ to the normal system

$$
\left\{ \begin{array} { l l } { \displaystyle { \frac { d x } { d t } } = x ^ { \prime } , \quad } & { \displaystyle { \frac { d x ^ { \prime } } { d t } } = \mp f \displaystyle { \frac { x } { r } } , } \\ { \displaystyle { \frac { d y } { d t } } = y ^ { \prime } , \quad } & { \displaystyle { \frac { d y ^ { \prime } } { d t } } = \mp f \displaystyle { \frac { y } { r } } , } \end{array} \right.
$$

which is of the fourth order. Therefore four integrals must be found in order to have the complete solution of the problem. The components of velocity, $\pmb { x } ^ { \prime }$ and $y ^ { \prime }$ ，playroles similar to the coordinates in (12),and,for brevity，they will be spoken of frequently in the future as being coordinates.

51.Reduction of Order. When an integral of a system of differential equations has been found two methods can be followed in completing the solution. The remaining integrals can be found from the original differential equations as though none was already known; or,by means of the known integral, the order of the system of differential equations can be reduced by one. That the order of the system can be reduced by means of the known integrals will be shown in the general case. Consider the system of differential equations

$$
\left\{ \begin{array} { l } { \displaystyle \frac { d x _ { 1 } } { d t } = f _ { 1 } ( x _ { 1 } , \mathrm { ~ } \cdots , \mathrm { ~ } x _ { n } , t ) , } \\ { \displaystyle \frac { d x _ { 2 } } { d t } = f _ { 2 } ( x _ { 1 } , \mathrm { ~ } \cdots , \mathrm { ~ } x _ { n } , t ) , } \\ { \displaystyle ~ \cdot _ { \mathrm { ~ } } ~ \cdot _ { \mathrm { ~ } } ~ \cdot _ { \mathrm { ~ } } ~ \cdot _ { \mathrm { ~ } } ~ \cdot _ { \mathrm { ~ } } ~ \cdot _ { \mathrm { ~ } } ~ \cdot _ { \mathrm { ~ } } } \\ { \displaystyle \frac { d x _ { n } } { d t } = f _ { n } ( x _ { 1 } , \mathrm { ~ } \cdots , \mathrm { ~ } x _ { n } , t ) . } \end{array} \right.
$$

Suppose an integral

$$
F ( x _ { 1 } , \ x _ { 2 } , \ \cdots , \ x _ { n } , \ t ) = { \mathrm { c o n s t a n t } } = c ,
$$

has been found. Suppose this equation is solved for ${ \pmb x } _ { \pmb n }$ in terms of $x _ { 1 } , \cdots , x _ { n - 1 } , c ,$ and $t$ ，The result may be written

$$
x _ { n } = \psi ( x _ { 1 } , \ x _ { 2 } , \ \cdot \cdot \cdot , \ x _ { n - 1 } , \ c , \ t ) .
$$

Substitute this expression for $x _ { n }$ in the first $n - 1$ equations of (13); they become

$$
\left\{ \begin{array} { l } { \displaystyle \frac { d x _ { 1 } } { d t } = \phi _ { 1 } ( x _ { 1 } , \ \cdots , \ x _ { n - 1 } , \ c , \ t ) , } \\ { \displaystyle \frac { d x _ { 2 } } { d t } = \phi _ { 2 } ( x _ { 1 } , \ \cdots , \ x _ { n - 1 } , \ c , \ t ) , } \\ { ~ \cdot ~ \cdot ~ \cdot ~ \cdot ~ \cdot ~ \cdot ~ \cdot ~ \cdot ~ \cdot ~ \cdot ~ \cdot ~ \cdot } \\ { \displaystyle \frac { d x _ { n - 1 } } { d t } = \phi _ { n - 1 } ( x _ { 1 } , \cdots , x _ { n - 1 } , \ c , \ t ) . } \end{array} \right.
$$

This is a simultaneous system of order $n - 1$ ,and is independent of the variable $x _ { n }$

It is apparent from these theorems and remarks that the order of a simultaneous system of differential equations is equal to the sum of the orders of the individual equations; that the equations can be written in several ways,e. g., as one equation of the nth order,or $\mathscr { n }$ equations of the first order;and that the integrals may all be derived from the original system,or that the order may be reduced after each integral is found. In mechanical and physical problems the intuitions are important in suggesting methods of treatment,so it is generally advantageous to use such variables that their geometrical and physical meanings shall be easily perceived.For this reason,it is generally simpler not to reduce the order of the problem after each integral is found.

# VII. PROBLEMS.

1.Prove the converse of the law of areas by the geometrical method,and show that the steps agree with the analysis of Art.48. 2.Prove the law of angular velocity by the geometrical method. 3.Why cannot equations (1) be integrated separately? 4.Derive the law of areas directly from equation (2）without passing to polar coordinates. 5.Show in detail that a normal system of order four can be reduced to & single equation of order four,and the converse. 6.Reduce the system of equations (12) to one of the third order by means of the integral of areas.

52.The Vis Viva Integral. Suppose the acceleration is toward the origin;then the negative sign must be taken before the right members of equations (1). Multiply the frst of (1）by $\mathbf { 2 } ~ { \frac { d x } { d t } }$ ， the second by $2 { \frac { d y } { d t } }$ , and add. The result is

$$
\begin{array} { r } { 2 \frac { d ^ { 2 } x } { d t ^ { 2 } } \frac { d x } { d t } + 2 \frac { d ^ { 2 } y } { d t ^ { 2 } } \frac { d y } { d t } = - \frac { 2 f } { r } \Big ( x \frac { d x } { d t } + y \frac { d y } { d t } \Big ) . } \end{array}
$$

It follows from $r ^ { 2 } = x ^ { 2 } + y ^ { 2 }$ that

$$
\begin{array} { r } { \displaystyle { \boldsymbol { x } } \frac { d \boldsymbol { x } } { d t } + \boldsymbol { y } \frac { d \boldsymbol { y } } { d t } = \boldsymbol { r } \frac { d \boldsymbol { r } } { d t } ; } \end{array}
$$

therefore

$$
2 { \frac { d ^ { 2 } x } { d t ^ { 2 } } } { \frac { d x } { d t } } + 2 { \frac { d ^ { 2 } y } { d t ^ { 2 } } } { \frac { d y } { d t } } = - \ 2 f { \frac { d r } { d t } } .
$$

Suppose $f$ depends upon $\pmb { r }$ alone,as it does in most astronomical and physical problems. Then $f = \phi ( r )$ ，and

$$
\ 2 { \frac { d ^ { 2 } x } { d t ^ { 2 } } } { \frac { d x } { d t } } + \ 2 { \frac { d ^ { 2 } y } { d t ^ { 2 } } } { \frac { d y } { d t } } = \ - \ 2 \phi ( r ) { \frac { d r } { d t } } .
$$

The integral of this equation is

$$
\left( { \frac { d x } { d t } } \right) ^ { 2 } + \left( { \frac { d y } { d t } } \right) ^ { 2 } = v ^ { 2 } = \mathbf { \nabla } - 2 \int \phi ( r ) d r + c .
$$

When the form of the function $\phi ( r )$ is given the integral on the right can be found. Suppose the integral is $\Phi ( \pmb { r } )$ ； then

$$
v ^ { 2 } = - 2 \Phi ( r ) + c .
$$

If $\Phi ( r )$ is a single-valued function of $\boldsymbol { r }$ ,as it is in physical problems,it follows from (16) that,if the central force is a function of the distance alone,the speed is the same at all points equally distant from the origin. Its magnitude at any point depends upon the initial distance and speed,and not upon the path described. Since the force of gravitation varies inversely as the square of the distance between the attracting bodies,it follows that a body， for example a comet,has the same speed at a given distance from the sun whether it is approaching or receding.

ExAMPLES WHERE $f$ IS A FUNCTION OF THE COORDINATES ALONE.

53.Force Varying Directly as the Distance. In order to find integrals of equations (1） other than that of areas, the value of f in terms of the coordinates must be known. In the case in which the intensity of the force varies directly as the distance the integration becomes particularly simple. Let $k ^ { 2 }$ represent the acceleration at unit distance. Then $f = k ^ { 2 } r$ ,and,in case the force is attractive,equations（1） become

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } x } { d t ^ { 2 } } = - k ^ { 2 } x , } \\ { \displaystyle \frac { d ^ { 2 } y } { d t ^ { 2 } } = - k ^ { 2 } y . } \end{array} \right.
$$

An important property of these equations is that each is independent of the other，as the first one contains the dependent variable $_ x$ alone and the second one $y$ alone．It is observed,moreover,that they are linear and the solution can be found by the method given in Art.32. If x = x, $\mathbf { \nabla } x = x _ { 0 } , \ { \frac { d x } { d t } } = x _ { 0 } ^ { \prime }$ ， ${ y = y _ { 0 } , \frac { d y } { d t } = y _ { 0 } } ^ { \prime } $ at $\mathbf { \nabla } _ { t } = \mathbf { 0 }$ ,then the solutions expressed in the trigonometrical form are

$$
\left\{ \begin{array} { l } { { x = + x _ { 0 } \cos k t + \frac { x _ { 0 } ^ { \prime } } { k } \sin k t , } } \\ { { \frac { d x } { d t } = - k x _ { 0 } \sin k t + x _ { 0 } ^ { \prime } \cos k t , } } \\ { { y = + y _ { 0 } \cos k t + \frac { y _ { 0 } ^ { \prime } } { k } \sin k t , } } \\ { { \frac { d y } { d t } = - k y _ { 0 } \sin k t + y _ { 0 } ^ { \prime } \cos k t . } } \end{array} \right.
$$

The equation of the orbit is obtained by eliminating $\pmb { t }$ between the first and third equations of (18). On multiplying by the appro priate factors and adding,it is found that

$$
\left\{ \begin{array} { l l } { ( x _ { 0 } y _ { 0 } ^ { \prime } - y _ { 0 } x _ { 0 } ^ { \prime } ) \sin { k t } = k ( x _ { 0 } y - y _ { 0 } x ) , } \\ { ( x _ { 0 } y _ { 0 } ^ { \prime } - y _ { 0 } x _ { 0 } ^ { \prime } ) \cos { k t } = y _ { 0 } ^ { \prime } x - x _ { 0 } ^ { \prime } y . } \end{array} \right.
$$

The result of squaring and adding these equations is

$$
\begin{array} { r l r } & { } & { ( k ^ { 2 } y _ { 0 } { } ^ { 2 } + y { } _ { 0 } { } ^ { \prime 2 } ) x ^ { 2 } + ( k ^ { 2 } x _ { 0 } { } ^ { 2 } + x { } _ { 0 } { } ^ { \prime 2 } ) y ^ { 2 } - 2 ( k ^ { 2 } x _ { 0 } y _ { 0 } + x _ { 0 } { } ^ { \prime } y _ { 0 } { } ^ { \prime } ) x y } \\ & { } & { = ( x _ { 0 } y _ { 0 } { } ^ { \prime } - y _ { 0 } x _ { 0 } { } ^ { \prime } ) ^ { 2 } . } \end{array}
$$

This is the equation of an ellipse with the origin at the center unless ${ x _ { 0 } y _ { 0 } } ^ { \prime } - { y _ { 0 } x _ { 0 } } ^ { \prime } = 0 ,$ ,when the orbit degenerates to two straight lines which must be coincident；for, then

$$
\frac { x _ { 0 } } { x _ { 0 } ^ { ' } } = \frac { y _ { 0 } } { y _ { 0 } ^ { ' } } = \mathrm { c o n s t a n t } = c ;
$$

from which

$$
x _ { 0 } = c x _ { 0 } { ' } , \qquad y _ { 0 } = c y _ { 0 } { ' } .
$$

In this case equation (20) becomes

$$
( k ^ { 2 } c ^ { 2 } + 1 ) ( { y _ { 0 } } ^ { \prime } x - { x _ { 0 } } ^ { \prime } y ) ^ { 2 } = 0 ,
$$

and the motion is rectilinear and oscillatory. In every case both the coordinates ana the components of velocity are periodic with the period $\frac { 2 \pi } { k }$ , whatever theinitialconditionsmay be.

54.Differential Equation of the Orbit. The curve described by the moving particle, independently of the manner in which it may move along this curve, is of much interest. A general method offinding the orbit is to integrate the differential equations and then to eliminate the time. This is often a complicated process,and the question arises whether the time cannot be eliminated before the integration is performed,so that the integration will lead directly to the orbit.It will be shown that this is the case when the force does not depend upon the time.

The differential equations of motion are [Art. 47]

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } x } { d t ^ { 2 } } = - f \displaystyle \frac { x } { r } , } \\ { \displaystyle \frac { d ^ { 2 } y } { d t ^ { 2 } } = - f \displaystyle \frac { y } { r } . } \end{array} \right.
$$

Since $\pmb { f }$ does not involve the time $t$ enters only in the derivatives.

But a second differential quotient cannot be separated as though it were an ordinary fraction;therefore,the order of the derivatives must be reduced before the direct elimination of $\mathbf { \Delta } _ { t }$ can be made. In order to do this most conveniently polar coordinates will be employed. Equations (22) become in these variables

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d ^ { 2 } r } { d t ^ { 2 } } - r \left( \displaystyle \frac { d \theta } { d t } \right) ^ { 2 } = \ - \ f , } \\ { \displaystyle r \frac { d ^ { 2 } \theta } { d t ^ { 2 } } + 2 \frac { d r } { d t } \frac { d \theta } { d t } = 0 . } \end{array} \right.
$$

The integral of the second of these equations is

$$
r ^ { 2 } { \frac { d \theta } { d t } } = h .
$$

On eliminating $\frac { d \theta } { d t }$ fromthrtofeaofi the result is found to be

$$
{ \frac { d ^ { 2 } r } { d t ^ { 2 } } } = { \frac { h ^ { 2 } } { r ^ { 3 } } } - f .
$$

Now let $r = { \frac { 1 } { u } }$ ； therefore

$$
\left\{ \begin{array} { l }  { \displaystyle { \frac { d r } { d t } } = - { \frac { 1 } { u ^ { 2 } } } { \frac { d u } { d t } } = - { \frac { 1 } { u ^ { 2 } } } { \frac { d u } { d \theta } } { \frac { d \theta } { d t } } = - h { \frac { d u } { d \theta } } , } \\ { { \displaystyle { d ^ { 2 } } r } } \\  { \displaystyle { \overline { { d t ^ { 2 } } } } = - h { \frac { d } { d t } } \left( { \frac { d u } { d \theta } } \right) = - h { \frac { d ^ { 2 } u } { d \theta ^ { 2 } } } { \frac { d \theta } { d t } } = - h ^ { 2 } u ^ { 2 } { \frac { d ^ { 2 } u } { d \theta ^ { 2 } } } . } \end{array} \right.
$$

When this value of the second derivative of $\pmb { r }$ is equated to the one given in (24),it is found that

$$
f = h ^ { 2 } u ^ { 2 } \left( u + \frac { d ^ { 2 } u } { d \theta ^ { 2 } } \right) .
$$

This differential equation is of the second order,but one integrai has been used in determining it; therefore the problem of finding the path of the body is of the third order.The complete problem was of the fourth order; the fourth integral expresses the relation between the coordinates and the time,or defines the position of the particle in its orbit.

Since the integral of (25) expresses $\textbf { \em u }$ ,and therefore $\pmb { r } _ { : }$ , in terms of $\pmb \theta _ { . }$ ,the equation

$$
r ^ { 2 } { \frac { d \theta } { d t } } = h ,
$$

when integrated, gives the relation between $\pmb \theta$ and $\pmb { \imath } .$

7

Conversely,equation (25) can be used to find the law of central force which will cause a particle to describe a given curve. It is only necessary to write the equation of the curve in polar coordinates and to compute the right member of (25). This is generally a simpler process than the reverse one of finding the orbit when the law of force is given.

55.Newton's Law of Gravitation. In the early part of the seventeenth century Kepler announced three laws of planetary motion，which he had derived from a most laborious discussion of a long series of observations of the planets,especially of Mars. They are the following:

LAW I. The radius vector of each planet with respect to the sun as the origin sweeps over equal areas in equal times.

LAW II. The orbit of each planet is an ellipse with the sun at one of its foci.

LAW III. The squares of the periods of the planets are to each other as the cubes of the major semi-axes of their respective orbits.

It was on these laws that Newton based his demonstration that the planets move subject to forces directed toward the sun，and varying inversely as the squares of their distances from the sun. The Newtonian law will be derived here by employing the analytical method instead of the geometrical methods of the Principia.\*

From the converse of the theorem of areas and Kepler's first law, it follows that the planets move subject to central forces directed toward the sun. The curves described are given by the second law,and equation (25) can, therefore,be used to find the expression for the acceleration in terms of the coordinates. Let $^ { a }$ represent the major semi-axis of the ellipse,and $e$ its eccentricity；then its equation in polar coordinates with origin at a focus is

$$
r = { \frac { a ( 1 - e ^ { 2 } ) } { 1 + e \cos \theta } } .
$$

Therefore

$$
u + \frac { \stackrel { \triangledown } { \sim } u } { d \theta ^ { 2 } } = \frac { 1 } { a ( 1 - e ^ { 2 } ) } .
$$

On substituting this expression in (25),it is found that the equatio for the acceleration is

$$
f = { \frac { h ^ { 2 } } { a ( 1 - e ^ { 2 } ) } } \cdot { \frac { 1 } { r ^ { 2 } } } = { \frac { k ^ { 2 } } { r ^ { 2 } } } .
$$

\* Book .. Proposition X

Therefore, the acceleration to which any planet is subject varies inversely as the square of its distance from the sun.

If the distance $\pmb { r }$ is eliminated by the polar equation of the conic the expression for $f$ has the form

$$
f = k _ { 1 } { } ^ { 2 } ( 1 + e \cos \theta ) ^ { 2 } ,
$$

which depends only upon the direction of the attracted body and not upon its distance. Now for points on the ellipse the two expressions for $f$ give the same value,but elsewhere they give different values. It is clear that many other laws of force,all agreeing in giving the same numerical values of $f$ for points on the ellipse,can be obtained by making other uses of the equation of the conic to eliminate $r$ .For example,since it follows from the polar equation of the ellipse for points on its circumference that

$$
\frac { ( 1 + e \cos \theta ) r } { a ( 1 - e ^ { 2 } ) } = 1 ,
$$

one such law is

$$
f = \frac { k ^ { 2 } ( 1 + e \cos \theta ) ^ { 3 } r } { a ( 1 - e ^ { 2 } ) } ,
$$

and this value of $f ,$ ，which depends both upon the direction and distance of the attracted body,differs from both of the preceding for points not on the ellipse. All of these laws are equally consistent with the motion of the planet in question as expressed by Kepler's laws. But the laws of Kepler hold for each of the eight planets and the twenty-six known satelites of the solar system, besides for more than seven hundred small planets which have so far been discovered.It is natural to impose the condition,if possible,that the force shall vary according to the same law for each body. Since the eccentricities and longitudes of the perihelia of their orbits are all different, the law of force is the same for all these bodies only when it has the form

$$
f = { \frac { k ^ { 2 } } { r ^ { 2 } } } .
$$

Another reason for adopting this expression for $f$ is that in case of all the others the attraction would depend upon the direction of the attracted body,and this seems improbable. This conclusion is further supported by the fact that the forces to which comets are subject when they move through the entire system of planets vary according to this law. And finally,as will be shown in Art. 89,the accelerations to which the various planets are subject vary from one to another according to this law.

From the consideration of Kepler's laws, the gravity at the earth's surface,and the motion of the moon around the earth, Newton was led to the enunciation of the Law of Universal Gravitation, which is,every two particles of matter in the universe attract each other with a force which acts in the line joining them, and whose intensity varies as the product of their masses and inversely as the squares of their distance apart.

It will be observed that the law of gravitation involves considerably more than can be derived from Kepler's laws of planetary motion；and it was by a master stroke of genius that Newton grasped it in its immense generality,and stated it so exactly that it has stood without change for more than 2Oo years. When contemplated in its entirety it is one of the grandest conceptions in the physical sciences.

56. Examples of Finding the Law of Force. $( a )$ If a particle describes a circle passing through the origin，the law of force (depending on the distance alone) under which it moves is a very simple expression. Let $^ { a }$ represent the radius；then the polar equation of the circle is

$$
r = 2 a \cos \theta , ~ u = \frac { 1 } { 2 a \cos \theta } .
$$

Therefore

$$
\frac { d ^ { 2 } u } { d \theta ^ { 2 } } + u = 8 a ^ { 2 } u ^ { 3 } .
$$

On substituting this expression in (25),it is found that

$$
f = { \frac { 8 a ^ { 2 } h ^ { 2 } } { r ^ { 5 } } } = { \frac { k ^ { 2 } } { r ^ { 5 } } } .
$$

$( b )$ Suppose the particle describes an elipse with the origin at the center. The polar equation of an ellipse with the center as origin is

$$
r ^ { 2 } = { \frac { b ^ { 2 } } { 1 - e ^ { 2 } \cos ^ { 2 } \theta } } .
$$

From this it follows that

$$
\left\{ \begin{array} { c } { { b u = \sqrt { 1 - e ^ { 2 } \cos ^ { 2 } \theta } , } } \\ { { \begin{array} { r l } { { b \frac { d ^ { 2 } u } { d \theta ^ { 2 } } = \frac { e ^ { 2 } \cos ^ { 2 } \theta - e ^ { 2 } \sin ^ { 2 } \theta } { \sqrt { 1 - e ^ { 2 } \cos ^ { 2 } \theta } } - \frac { e ^ { 4 } \sin ^ { 2 } \theta \cos ^ { 2 } \theta } { ( 1 - e ^ { 2 } \cos ^ { 2 } \theta ) ^ { \frac { 3 } { 2 } } } , } } \\ { { u + \frac { d ^ { 2 } u } { d \theta ^ { 2 } } = \frac { 1 - e ^ { 2 } } { b ^ { 4 } } \cdot \frac { 1 } { \eta ^ { 3 } } . } } \end{array} } } \end{array} \right.
$$

On substituting in (25),the expression for $f$ is found to be

$$
f = { \frac { h ^ { 2 } ( 1 - e ^ { 2 } ) } { b ^ { 4 } } } \cdot r = k ^ { 2 } r .
$$

# THE UNIVERSALITY OF NEWTON'S LAW.

57.Double Star Orbits. The law of gravitation is proved from Kepler's laws and certain assumptions as to its uniqueness to hold in the solar system；the question whether it is actually universal naturally presents itself. The fixed stars are so remote that it is not possible to observe planets revolving around them, if indeed they have such attendants. The only observations thus far obtained which throw any light upon the subject are those of the motions of the double stars.

Double star astronomy started about 1780 with the search for close stars by Sir William Herschel for the purpose of determining parallax by the differential method. A few years were sufficient to show him,to his great surprise,that in some cases the two components of a pair were revolving around each other，and that, therefore, they were physically connected as well as being apparently in the same part of the sky. The discovery and measurement of these systems has been pursued with increasing interest and zeal by astronomers. Burnham's great catalogue of double stars contains about 13,Ooo of these objects. The relative motions are so slow in most cases that only a few have yet completed one revolution,or enough of one revolution so that the shapes of their orbits are known with certainty. There are now about thirty pairs whose observed angular motions have been sufficiently great to prove，within the errors of the observations,that they move in ellipses with respect to each other in such a manner that the law of areas is fulfilled．In no case is the primary at the focus, or at the center,of the relative elipse deseribed by the companion, but it occupies some other place within the ellipse,the position varying greatly in different systems.

From the observations and the converse of the law of areas it. follows that the resultant of the forces acting upon one star of & pair is always directed toward the other. The law of variation cf the intensity of the force depends upon the position in the ellipse which the center of force occupies. It must not be overlooked at this point that the orbits of the stars are not observed directly,but that it is their projections upon the planes tangent to the celestial sphere at their respective places which are seen. The effect of this sort of projection is to change the true ellipse into a different apparent eilipse whose major axis has a different. direction，and one that is differently situated with respect to the central star; indeed,it might happen that if one of the stars was really in the focus of the true ellipse described by the other,the projection would be such as to make it lie on the minor axis of the apparent ellipse.

Astronomers have assumed that the orbits are plane curves and that the apparent departure of the central star from the focus of the ellipse described by the companion is due to projection,and have then computed the angle of the line of nodes and the inclination. No inconsistencies are introduced in this way，but the possibility remains that the assumptions are not true. The question of what the law of force must be if it is not Newton's law of gravitation will now be investigated.

![](images/03f6caef16c11ff1b207e51a0b625112f51d87c4bf00aa76906a82a56f57c70c.jpg)  
Fig.9.

58.Law of Force in Binary Stars. If the force varied directly as the distance the primary star would be at the center of the ellipse described by the secondary (Art.53). No projection would change this relative position,and since such a condition has never been observed,it is inferred that the force does not vary directly as the distance.

The condition will now be imposed that the curve shall be a conic with general position for the origin,and the expression for the central force will be found. The equation of the general conic is

$$
a x ^ { 2 } + 2 b x y + c y ^ { 2 } + 2 d x + 2 f y = g .
$$

Ontransforingtolarcrdinatesadting $r = { \frac { 1 } { u } }$ ，this equation gives

$$
u = A \sin \theta + B \cos \theta \pm { \sqrt { C \sin 2 \theta + D \cos 2 \theta + H } } ,
$$

where

$$
\left\{ \begin{array} { r l } { \displaystyle { A = \frac { f } { g } , \quad \quad B = \frac { d } { g } , \quad } } & { \displaystyle { C = \frac { f d + b g } { g ^ { 2 } } , } } \\ { \displaystyle { D = \frac { d ^ { 2 } + a g - f ^ { 2 } - c g } { 2 g ^ { 2 } } , \quad } } & { \displaystyle { H = \frac { d ^ { 2 } + a g + f ^ { 2 } + c g } { 2 g ^ { 2 } } . } } \end{array} \right.
$$

On differentiating (27) twice,it is found that

$$
\begin{array} { l } { \frac { d ^ { 2 } u } { d \theta ^ { 2 } } = - \ A \sin \theta - B \cos \theta } \\ { \pm \frac { - C ^ { 2 } - D ^ { 2 } - ( C \sin 2 \theta + D \cos 2 \theta ) ^ { 2 } - 2 H ( C \sin 2 \theta + D \cos 2 \theta ) } { ( C \sin 2 \theta + D \cos 2 \theta + H ) ^ { \frac { 1 } { 2 } } } . } \end{array}
$$

On substituting (27) and (28) in (25),it follows that

$$
f = \pm \frac { h ^ { 2 } } { r ^ { 2 } } \frac { ( H ^ { 2 } - C ^ { 2 } - D ^ { 2 } ) } { ( C \sin 2 \theta + D \cos 2 \theta + H ) ^ { 4 } } .
$$

This becomes as a consequence of (27)

$$
f = \pm { \frac { h ^ { 2 } } { r ^ { 2 } } } { \frac { ( H ^ { 2 } - C ^ { 2 } - D ^ { 2 } ) } { \left( { \frac { 1 } { r } } - A \sin \theta - B \cos \theta \right) ^ { 3 } } } .
$$

There are also infinitely many other laws,all giving the same values of $f$ for points on the ellipse in question,which are obtained by multiplying these expressions by any functions of $\textbf { \em u }$ and $\pmb \theta$ which are unity on the ellipse in virtue of equation (27).

It does not seem reasonable to suppose that the attraction of two stars for each other depends upon their orientation in space. Equation (29） becomes independent of $\theta$ if $C = D = \mathbf { 0 }$ ,and (30), if $A = B = 0$ The first gives

$$
f = \pm { \frac { \mathrm { c o n s t a n t } } { r ^ { 2 } } } ,
$$

and the second,

$$
f = \pm { \mathrm { ~ c o n s t a n t } } \cdot r .
$$

The first is Newton's law,and the second is excluded by the fact that no primary star has been found in the center of the orbit described by the companion. It is clear that $\pmb \theta$ can be eliminated from (29) and (30) by means of (27) without imposing the conditions that $A = B = C = D = 0 ,$ 、But Griffin has shown\* that for all such laws,except the Newtonian，the force either vanishes when the distance between the bodies vanishes，or becomes imaginary for certain values of $\boldsymbol { r }$ .Clearly both of these laws are improbable from a physical point of view. Hence it is extremely probable that the law of gravitation holds throughout the stellar systems;and this conclusion is supported by the fact that the spectroscope shows the stars are composed of familiar terrestrial elements.

59.Geometrical Interpretation of the Second Law. The expression for the central force given in (30) may be put in a very simple and interesting form. Let $g ^ { 3 } h ^ { 2 } ( H ^ { 2 } - C ^ { 2 } - D ^ { 2 } ) = N$ and transform $\frac { 1 } { r } - A \sin \theta - B$ cos $\pmb \theta$ into rectangular coordinates and the original constants； then (30) becomes

$$
f = { \frac { \mp N r } { ( d x + f y - g ) ^ { 3 } } } .
$$

The equation of the polar of the point $( x ^ { \prime } , y ^ { \prime } )$ with respect to the general conic (26) ist

0 $\ x _ { 1 } x ^ { \prime } + b ( x _ { 1 } y ^ { \prime } + y _ { 1 } x ^ { \prime } ) + c y _ { 1 } y ^ { \prime } + d ( x _ { 1 } + x ^ { \prime } ) + f ( y _ { 1 } + y ^ { \prime } ) - g = 0 ,$ where $\pmb { x _ { 1 } }$ and ${ \pmb y } _ { 1 }$ are the running variables. When $( x ^ { \prime } , y ^ { \prime } )$ is the origin this equation becomes

$$
d x _ { 1 } + f y _ { 1 } - g = 0 ,
$$

and has the same form as the denominator of (31). The values of $\pmb { x }$ and $\pmb { y }$ in (31） are such that they satisfy the equation of the conic,while $\pmb { x _ { 1 } }$ and $_ { y _ { 1 } }$ of (32) satisfy the equation of the polar line. They are, therefore, in general numerically different from $\pmb { x }$ and $\pmb { y }$ · But the distance from any point $( x , y )$ of the conic to the polar line with respect to the origin is given by the equation

$$
p = \frac { d x + f y - g } { \sqrt { d ^ { 2 } + f ^ { 2 } } } ,
$$

where $\pmb { x }$ and $\pmb { y }$ are the coordinates of points on the conic. Let

$$
N ^ { \prime } = \frac { N } { ( d ^ { 2 } + f ^ { 2 } ) _ { \tt 5 } ^ { 3 } } ;
$$

then (31） becomes

\*American Journal of Mathematics,vol.31 (1909),pp.62-85.   
+ Salmon's Conic Sections,Art. 89.

$$
f = \ast { \frac { N ^ { \prime } r } { p ^ { 3 } } } .
$$

Therefore,if a particle moving subject to $^ { a }$ central force describes any conic,the intensity of the force varies directly as the distance of the particle_from the origin,and inversely as the cube of its distance from the polar of the origin with respect to the conic.

60.Examples of Conic Section Motion. $( a )$ When the orbit is a central conic with the origin at the center,the polar line recedes to infinity，and $\frac { N ^ { \prime } } { p ^ { 3 } }$ must be regarded as a constant. Then the force varies directly as the distance,as was shown in Art. 56 (b).

$( b )$ When the origin is at one of the foci of the conic the polar lineis thedretrx where $e$ is the eccentricity. Then (33) becomes

$$
f = \mp \frac { N ^ { \prime } e ^ { 3 } } { r ^ { 2 } } .
$$

This is Newton's law which was derived from the same conditions in Art. 55.

# VIII. PROBLEMS.

1. Findthevisva ntegral when $f = { \frac { c } { r ^ { 2 } } } , f = c r , f = { \frac { c } { r ^ { n } } } .$

2.Suppose that in Art.53 the particle is projected orthogonally from the $\pmb { \mathscr { x } }$ -axis;find the equations corresponding to (19) and (2O). Suppose still further that $\pmb { k } = \pmb { 1 }$ ， $\scriptstyle { \mathfrak { x } } _ { 0 } = 1$ ；find the initial velocity such that the eccentricity of the ellipse may be $1 / 2$ ·

$$
A n s . \quad { \left\{ \begin{array} { l l } { \upsilon _ { 0 } = { \frac { 1 } { 2 } } { \sqrt { 3 } } , } & { 0 \mathbf { r } } \\ { \upsilon _ { 0 } = { \frac { \pi } { 3 } } { \sqrt { 3 } } . } \end{array} \right. }
$$

3.Find the central force as a function of the distance under which a particle may describe the spiral $r = { \frac { 1 } { c \theta } }$ the spiral $\pmb { r } = \pmb { e } ^ { \pmb { \theta } }$ · ，

$$
A n s . f = \frac { h ^ { 2 } } { r ^ { 3 } } , f = \frac { 2 \lambda ^ { 2 } } { r ^ { 3 } } .
$$

4.Find the central force as a function of the distance under which 9 particle may describe the lemniscate $\pmb { r } ^ { 2 } = a ^ { 2 }$ cos 20.

$$
A n s . f = { \frac { 3 h ^ { 2 } a ^ { 4 } } { r ^ { 7 } } } .
$$

5. Find the central force as a function of the distance under which a particle may describe the cardioid $r = a ( 1 + \cos \theta )$ ·

$$
A n s . f = { \frac { 3 a h ^ { 2 } } { r ^ { 4 } } } .
$$

6. Suppose the particle describes an elipse with the origin in its interior, at a distance $\pmb { n }$ from the $\pmb { x }$ -axis and $\pmb { m }$ from the $\boldsymbol { y } \cdot \mathrm { \Sigma }$ axis. $( a )$ Show that two of the laws of force are

$$
\left\{ \begin{array} { l l } { { f = \displaystyle \frac { h ^ { 2 } } { r ^ { 2 } } \displaystyle \frac { ( a c ) ^ { \frac { 1 } { 2 } } } { [ 2 m n \sin \theta \cos \theta + ( a - c - n ^ { 2 } + m ^ { 2 } ) \cos ^ { 2 } \theta + c - m ^ { 2 } ] ^ { \frac { 3 } { 4 } } } , } }  \\ { { f = \displaystyle \frac { h ^ { 2 } a ^ { 2 } c ^ { 2 } r } { [ a c - a m ^ { 2 } - c n ^ { 2 } - c n y - a m x ] ^ { 3 } } , } } \end{array} \right.
$$

where $\pmb { a }$ and $\pmb { c }$ have the same meaning as in (26),and where the polar axis is parallel to the major axis of the ellipse. $( b )$ If the origin is between the center and the focus show that the force at unit distance isa maximum for ${ \pmb \theta } = { \bf 0 }$ and is & minimum for $\theta = \frac { \pi } { 2 }$ ; that if the origin is betwen a focus and the nearest apse the maximum is for θ = a and the minimum for $\pmb \theta = \mathbf 0$ ; and that if the origin is on the minor axis the maximum is for $\pmb \theta = \mathbf 0 ,$ and the minimum for $\theta = \frac { \pi } { 2 }$ ·

7. Interpret equation (29) geometrically.

$$
C \sin 2 \theta + D \cos 2 \theta + H = \frac { ( d x + f y ) ^ { 2 } + g ( a x ^ { 2 } + c y ^ { 2 } + 2 b x y ) } { g ^ { 2 } r ^ { 2 } } .
$$

The numerator of this expression set equal to zero is the equation'of the tangents (real or imaginary） from the origin to the conic. (Salmon's Conic Sections,Art. 92.)

8.Find expressions for the central force when the orbit is an ellipse with the origin at an end of the major and minor axes respectively. Show that they reduce to $\frac { k ^ { 2 } } { r ^ { 5 } }$ when the ellise becomes a circle.

$$
\begin{array} { r } { A n \mathrm { s . } \left\{ \begin{array} { l l } { f = \frac { h ^ { 2 } \sqrt { c } } { a r ^ { 2 } } \cdot \frac { 1 } { \cos ^ { 3 } \theta } , } \\ { f = \frac { h ^ { 2 } \sqrt { a } } { c r ^ { 2 } } \cdot \frac { 1 } { \sin ^ { 3 } \theta } . } \end{array} \right. } \end{array}
$$

DETERMINATION OF THE ORBIT FROM THE LAW OF FORCE.

61.Force Varying as the Distance. The problem of finding the orbit when the law of force is given is generally more difficult than the converse, since it involves the integration of (25). The method of integration varies with the different laws of force,and the character of the integrals depends upon the initial conditions. The process will be illustrated first in the case in which the force varies as the distance,a problem treated by another method in Art. 53.

If $f = k ^ { 2 } r$ ,equation (25) becomes

or

$$
\begin{array} { c } { { \frac { \displaystyle { k ^ { 2 } } } { \displaystyle { u } } = h ^ { 2 } u ^ { 2 } \left[ u + \frac { \displaystyle d ^ { 2 } u } { \displaystyle d \theta ^ { 2 } } \right] , } } \\ { { \frac { \displaystyle d ^ { 2 } u } { \displaystyle d \theta ^ { 2 } } = \frac { \displaystyle k ^ { 2 } } { \displaystyle h ^ { 2 } } \frac { \displaystyle 1 } { \displaystyle u ^ { 3 } } - u . } } \end{array}
$$

The first integral of this equation is

$$
\left( \frac { d u } { d \theta } \right) ^ { 2 } = \mathrm { ~ - ~ } \frac { k ^ { 2 } } { h ^ { 2 } } \frac { 1 } { u ^ { 2 } } - u ^ { 2 } + c _ { \mathrm { { i } } } ;
$$

whence

$$
d \theta = { \frac { \pm u d u } { \left[ { \frac { { c _ { 1 } } ^ { 2 } } { 4 } } - { \frac { k ^ { 2 } } { h ^ { 2 } } } - \left( { \frac { c _ { 1 } } { 2 } } - u ^ { 2 } \right) ^ { 2 } \right] ^ { \frac { 1 } { 4 } } } } .
$$

Let

$$
\frac { c _ { 1 } } { 2 } - u ^ { 2 } = z , ~ \frac { { c _ { 1 } } ^ { 2 } } { 4 } - \frac { k ^ { 2 } } { h ^ { 2 } } = A ^ { 2 } .
$$

The constant $A ^ { 2 }$ must be positive in order that $\frac { d u } { d \theta }$ may be real, as it is if the particle is started with real initial conditions.

If the upper sign is used, equation (34) becomes

$$
2 d \theta = \frac { - d z } { \sqrt { A ^ { 2 } - z ^ { 2 } } } .
$$

It is easily verified that the same equation (36) would be reached, when the initial conditions are substituted, if the lower sign were used.The integral of (35) is

$$
\cos ^ { - 1 } { \frac { z } { A } } = 2 ( \theta + c _ { 2 } ) ,
$$

or

$$
z = A \cos 2 ( \theta + c _ { 2 } ) .
$$

On going back to the variable $\pmb { r }$ ,this equation becomes

$$
r ^ { 2 } = \frac { 2 } { c _ { 1 } - 2 A \cos 2 ( \theta + c _ { 2 } ) } .
$$

This is the polar equation of an elipse with the origin at the center. Hence, a particle moving subject to an attractive force varying directly as the distance describes an elipse with the origin at the center. The only exceptions are when the particle passes through the origin，and when it describes a circle.In the first $h = 0$ and equation (25) ceases to be valid; in the second, $c _ { 1 }$ has such a ralue that it satisfies the equation

$$
\left( \frac { d u } { d \theta } \right) _ { 0 } ^ { 2 } = \mathrm { ~ - ~ } \frac { k ^ { 2 } } { \mathit { h } ^ { 2 } } \cdot \frac { 1 } { { u _ { 0 } } ^ { 2 } } - { u _ { 0 } } ^ { 2 } + c _ { 1 } = 0 ,
$$

and the equation of the orbit becomes $u = u _ { 0 }$ In this case equation (34) fails.

62. Force Varying Inversely as the Square of the Distance. Suppose a particle moves under the influence of a central attraction the intensity of which varies inversely as the square of the distance; it is required to determine its orbit when it is projected in any manner. Equation (25) is in this case

$$
{ \frac { d ^ { 2 } u } { d \theta ^ { 2 } } } = { \frac { k ^ { 2 } } { h ^ { 2 } } } - u .
$$

This equation can be written in the form

$$
{ \frac { d ^ { 2 } u } { d \theta ^ { 2 } } } + u = { \frac { k ^ { 2 } } { h ^ { 2 } } } .
$$

This is a linear non-homogeneous diferential equation and can be integrated by the method of variation of parameters,which was explained in Art.37.When its right member is neglected the general solution is

$$
u = c _ { 1 } \cos \theta + c _ { 2 } \sin \theta .
$$

It i ler that if $\frac { k ^ { 2 } } { h ^ { 2 } }$ is added to this value of $_ { \pmb { u } }$ the diferential equation will be identically satisfied. Consequently the general solution of (37),which is the same as that found by the variation of parameters,is

$$
u = { \frac { k ^ { 2 } } { h ^ { 2 } } } + c _ { 1 } \cos \theta + c _ { 2 } \sin \theta .
$$

On taking the reciprocal of this equation,it is found that

$$
r = \frac { 1 } { \frac { k ^ { 2 } } { \bar { h } ^ { 2 } } + c _ { 1 } \cos \theta + c _ { 2 } \sin \theta } .
$$

Now let ${ \mathfrak { c } } _ { 1 } = A { \mathrm { ~ c o s ~ } } \theta _ { 0 } , { \mathfrak { c } } _ { 2 } = A$ sin $\theta _ { 0 }$ ,where $\pmb { A }$ and $\theta _ { 0 }$ are constants. It is clear that $\pmb { A }$ can always be taken positive and equal to $\sqrt { { c _ { 1 } } ^ { 2 } + { c _ { 2 } } ^ { 2 } }$ and a real $\theta _ { 0 }$ can be determined so that these equations will be satisfied whatever real values $\mathbf { c _ { 1 } }$ and ${ \pmb { c } } _ { \mathbf { 2 } }$ may have. Then the equation for the orbit becomes

$$
\pmb { \gamma } = \frac { 1 } { \frac { k ^ { 2 } } { \hbar ^ { 2 } } + A \cos { ( \theta - \theta _ { 0 } ) } } .
$$

This is the polar equation of a conic with the origin at one of the foci.

From tliis investigation and that of Art.55 it follows that if the orbit is a conic section with the origin at one of the foci,and the force depends on the distance alone, then the body moves subject to a central force varying inversely as the square of the distance; and conversely,if the force varies inversely as the square of the distance,then the body will describe a conic section with the origin at one of the foci.

Let $\pmb { p }$ represent the parameter of the conic and e its eccentricity. Then，comparing (38) with the ordinary polar equation of the conic,r =1+e cos Φ' ,it is found that

$$
\left\{ \begin{array} { l l } { p = \displaystyle \frac { h ^ { 2 } } { k ^ { 2 } } , } \\ { e = \displaystyle \frac { h ^ { 2 } } { k ^ { 2 } } A , } \end{array} \right.
$$

and $\pmb { \theta } _ { 0 }$ is the angle between the polar axis and the end of the major axis directed to the farthest apse. The constants $h ^ { 2 }$ and $A$ are determined by the initial conditions,and they in turn define $\pmb { p }$ and $\pmb { e }$ by (39).If $e < 1$ ，the conic is an ellipse；if $e = 1$ ，the conic is a parabola;if $e > 1$ ,the conic is a hyperbola；and if $e = 0$ ， the conic is a circle.

# 63.Force Varying Inversely as the Fifth Power of the Distance.

In this case $f = { \frac { k ^ { 2 } } { r ^ { 5 } } }$ , and (25) becomes

$$
k ^ { 2 } u ^ { 5 } = h ^ { 2 } u ^ { 2 } \left( u + \frac { d ^ { 2 } u } { d \theta ^ { 2 } } \right) .
$$

On solving for $\frac { d ^ { 2 } u } { d \theta ^ { 2 } }$ and integrating,it isfoundthat

$$
\left( { \frac { d u } { d \theta } } \right) ^ { 2 } = { \frac { 1 } { 2 } } { \frac { k ^ { 2 } } { h ^ { 2 } } } u ^ { 4 } - u ^ { 2 } + c _ { 1 } .
$$

Therefore

$$
d \theta = { \frac { d u } { \sqrt { c _ { 1 } + { \frac { 1 } { 2 } } { \frac { k ^ { 2 } } { h ^ { 2 } } } u ^ { 4 } - u ^ { 2 } } } } .
$$

The right member of this equation cannot in general be integrated in terms of the elementary functions,but it can be transformed into an elliptic integral of the first kind. Then $_ { \boldsymbol { u } }$ and consequently $\pmb { r } _ { \bullet }$ is expressible in terms of $\theta$ by elliptic functions,and the orbits n general either wind into the origin or pass out to infinity, their particular character depending upon the initial conditions.

There are certain special cases which are integrable in terms of elementary functions.

$( a )$ If such a constant value of $\textbf { \em u }$ is taken that it fulfills (41) when its right member is set equal to zero, then $\pmb { r }$ is a constant and the orbit isa circle with the origin at the center. It is easily seen that a similar special case will occur for a central force varying as any power of the distance.

$( b )$ Another special case is that in which the initial conditions are such that $c _ { 1 } \neq 0$ and the right member of (41） isa perfect square. That is, $c _ { 1 } = \frac { h ^ { 2 } } { 2 k ^ { 2 } }$ Then equation (41） becomes

$$
\left( { \frac { d u } { d \theta } } \right) ^ { 2 } = \ \left( \frac { 1 } { \sqrt { 2 } } \frac { k } { h } u ^ { 2 } - \frac { 1 } { \sqrt { 2 } } h \right) ^ { 2 } = \frac { 1 } { 2 } \Big ( A ^ { 2 } u ^ { 2 } - \frac { 1 } { A ^ { 2 } } \Big ) ^ { 2 } .
$$

The integral of this equation is

$$
\log { \frac { 1 + A ^ { 2 } u } { 1 - A ^ { 2 } u } } = { \sqrt { 2 } } ( \pm \theta - c _ { 2 } ) ;
$$

whence

$$
r = - \ k ^ { 2 } [ \frac { 1 + e ^ { \mathsf { s i } \overline { { 2 } } ( \pm \theta - c _ { 2 } ) } } { [ 1 - e ^ { \mathsf { s i } \overline { { 2 } } ( \pm \theta - c _ { 0 } ) } ] } = + A ^ { 2 } \coth \frac { \sqrt { 2 } } { 2 } ( \pm \theta - c _ { 2 } ) ,
$$

where coth $\frac { \sqrt { 2 } } { 2 } ( \pm \theta - c _ { 2 } )$ is the hyperbolic cotangent of

$$
{ \scriptstyle { \frac { 1 } { 2 } } } { \sqrt { 2 } } ( \pm \theta - c _ { 2 } ) .
$$

$( c )$ If the initial conditions are such that $\pmb { c _ { 1 } = 0 }$ ,equation (41) gives

$$
\pm \ d \theta = { \frac { d u } { \displaystyle u { \sqrt { { \frac { 1 } { 2 } } { \frac { k ^ { 2 } } { h ^ { 2 } } } u ^ { 2 } - 1 } } } } ,
$$

the integral of which is

$$
\pm \theta = \cos ^ { - 1 } \left( \frac { \sqrt { 2 } h } { k u } \right) + c _ { 2 } .
$$

On taking the cosines of both members and solving for $\pmb { r }$ ,the polar equation of the orbit is found to be

$$
r = \frac { k } { \sqrt { 2 } h } \cos \left( c _ { 2 } \mp \theta \right) ,
$$

which is the equation of a circle with the origin on the circumference.

$( d )$ If none of these conditions is fulfilled the right member of (41) is a biquadratic,and equation (42) can be written in the form

$$
\pm \ d \theta = \frac { C d u } { \sqrt { \pm \ ( 1 \pm \alpha ^ { 2 } u ^ { 2 } ) ( 1 \pm \beta ^ { 2 } u ^ { 2 } ) } } ,
$$

where $C , \alpha ^ { 2 }$ and $\beta ^ { 2 }$ are constants which depend upon the coefficients of (41）in a simple manner. Equation (45) leads to an elliptic integral which expresses $\theta$ in terms of $\boldsymbol { \mathscr { u } }$ ，On taking the inverse functions and the reciprocals, $r$ is expressed as an elliptic function of $\pmb \theta$ ，The curves are spirals of which the circle through the origin, and the one around the origin as center,are limiting cases.

If the curve is a circle through the origin the force varies inversely as the fifth power of the distance (Art.56)；but if the force varies inversely as the fth power of the distance, the orbits which the particle will describe are curves of which the circle is a particular limiting case. On the other hand,if the orbit is a conic with the origin at the center or at one of the foci,the force varies directly as the distance,or inversely as the square of the distance;and conversely,if the force varies directly as the distance, or inversely as the square of the distance, the orbits are always conics with the origin at the center,or at one of the foci respectively $\left[ \mathrm { A r t s . ~ 5 3 , ~ 5 5 , ~ 5 6 ~ } \left( b \right) \right]$ .A complete investigation is necessary for every law to show this converse relationship.

# IX. PROBLEMS.

1.Discuss the motion of the particle by the general method for linear equations when the force varies inversely as the cube of the distance. Trace the curves in the various special cases.

2. Express $C , \alpha ^ { 2 } .$ and $\beta ^ { \mathfrak { g } }$ of equation (45) in terms of the initial conditions. For original projections at right angles to the radius vector investigate all the possible cases,reducing the integrals to the normal form, and expressing $\pmb { r }$ a elliptic functions of $\pmb \theta$ Draw the curves in each case.

3. Suppose the Iaw of force is that given in (29)； i.e.

$$
f = \frac { M } { r ^ { 2 } ( C \sin 2 \theta + D \cos 2 \theta + H ) ^ { \frac { 3 } { 4 } } } = \frac { M } { r ^ { 2 } [ \phi ( \theta ) ] ^ { \frac { 3 } { 2 } } } .
$$

Integrate the differential equation of the orbit,(25),by the method of variation of parameters,and show that the general solution has the form

$$
{ \frac { 1 } { r } } = c _ { 1 } \cos \theta + c _ { 2 } \sin \theta + { \sqrt { \phi ( \theta ) } } ,
$$

where $\pmb { c _ { 1 } }$ and $\pmb { c _ { \tilde { \mathbf { z } } } }$ are constants of integration. Show that the curve is a conic.

4. When the force is $f = \frac { \mu } { r ^ { 2 } } + \frac { \nu } { r ^ { 3 } }$ show that, if $\nu < h ^ { 2 }$ ， the general equaa tion of the orbit described has the form

$$
r = \frac { a } { 1 - e \cos ( k ^ { q } ) } ,
$$

where ${ \pmb a } , \ { \pmb e } ,$ and $k$ are the constants depending upon the initial conditions and $\pmb { \mu }$ and ${ \pmb \nu }$ ：Observe that this may be regarded as being a conic section whose major axis revolves around the focus with the mean angular velocity

$$
{ \boldsymbol { n } } = \left( 1 - k \right) { \frac { 2 \pi } { T } } ,
$$

where $\pmb { T }$ is the period of revolution.

5.In the case of a central force the motion along the radius vector is defined by the equation

$$
\begin{array} { r } { \frac { d ^ { 2 } r } { d t ^ { 2 } } = - f + \frac { h ^ { 2 } } { r ^ { 3 } } . } \end{array}
$$

Discuss the integration of this equation when

$$
f = { \frac { k ^ { 2 } } { r ^ { 5 } } } .
$$

6. Suppose the law of force is that given by (30); i. .,

$$
f = \frac { N } { r ^ { 2 } \left( \frac { 1 } { r } - A \sin \theta - B \cos \theta \right) ^ { 3 } } .
$$

ubstitute in (25) and derive the general equation of the orbit described.

Hint. Let ${ \pmb u } = { \pmb v } + { \pmb A }$ sin $\theta + B$ cos $\pmb \theta$ ；then (25) becomeg

$$
\frac { d ^ { 2 } v } { d \theta ^ { 2 } } + v = \frac { N h ^ { - 2 } } { v ^ { 3 } } .
$$

Ans. ${ \frac { 1 } { r } } = A \sin \theta + B \cos \theta + { \sqrt { c _ { 1 } \cos ^ { 2 } \theta + c _ { 2 } \sin 2 \theta + c _ { 3 } \sin ^ { 2 } \theta } } ,$ Thich is the equation of a conic section.

7. Suppose the law of force is

$$
\pmb { f } = \frac { c _ { 1 } + c _ { 2 } \cos 2 \theta } { r ^ { 2 } } ,
$$

Bhow that,for all initial projections,the orbit is an algebraic curve of the fourth degree unless $\mathbf { c } _ { 2 } = \mathbf { 0 }$ ，when it reduces toa conic.

# HISTORICAL SKETCH AND BIBLIOGRAPHY.

The subject of central forces was first discussed by Newton.In Sections I1.and I1.of the First Book of the Principia he gave a splendid geometrical treatment of the subject,and arrived at some very general theorems. These portions of the Principia especially deserve careful study.

All the simpler cases were worked out in the eighteenth century by analytical methods.A few examples are given in detail in Legendre's Traité des Fonctions Elliptiques.An exposition of principles and a list of examples are given in nearly every work on analytical mechanics;among the best ef these treatments are the Fifth Chapter in Tait and Steele's Dynamics of $^ { \pmb { a } }$ Particle,and the Tenth Chapter，vol.1.,of Appell's Mécanique Rationelle. Stader's memoir,vol.xLvi.,Journal fur Mathematik,treats the subject in great detail. The special problem where the force varies inversely as the ffth power of the distance has been given a complete and elegant treatment byMacMillan in The American Journal of Mathematics,vol.xxx,pp.282-306.

The problem of finding the general expression for the possible laws of force operating in the binary star systems was proposed by M.Bertrand in vol. LxxxIv.of the Comptes Rendus,and was immediately solved by MM.Darboux and Halphen,and published in the same volume. The treatment given above in the text is similar to that given by M.Darboux,which has also been reproduced in a note at the end of the Mécanique of M.Despeyrous. The method of M.Halphen is given in Tisserand's Mé:anique Celeste,vol.I.,p.36,and in Appell's Mécanique Rationelle,vol.1.,p.372. It seems to have been generally overlooked that Newton had reated the same problem in the Principia, Book 1., Scholium to Proposition XvI1．This was reproduced and shown to be equivalent to the work of MM.Darboux and Halphen by Professor Glaisher in the Monthly Notices f R.A.S., vol. xxxix.

M.Bertrand has shown (Comptes Rendus,vol.LxxvI1.) that the only laws of central force under the action of which a particle will describe a conic section for all initial conditions are $f = \pm { \frac { k ^ { 2 } } { r ^ { 2 } } }$ and $f = \pm k ^ { 2 } r$ M. Koenigs has proved (Bulletin de la Societé Mathématique,vol.xvI1.) that the only laws of central force depending upon the distance alone,for which the curves deseribed are algebraicforallinitial conditionsare $f = \pm { \frac { k ^ { 2 } } { r ^ { 2 } } }$ and $f = \pm k ^ { 2 } r$ Griffin has shown (American Journal of Mathematics,vol. xxxi.） that the only law,where the force is a function of the distance alone,where it does not vanish at the center of force,and where it is real throughout the plane,giving an elliptical orbit is the Newtonian law.
