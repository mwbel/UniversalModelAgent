discontinuous function of time (i.e., the fuel must be burned instantaneously). We will consider three possible cases:

1. If Φ is always positive, all of the propellant must be burned instantaneously at the beginning, and the optimum program for V is the heavy discontinuous curve of Fig. 8.4-2. For $V ( t )$ to be optimum, $\delta U$ must be negative for any variation of $V$ from the optimum. For instance, any variation $\delta V$ from the optimum curve of Fig. 8.4-2, such as the dotted curve,must be negative, which means that $\delta U$ would be negative. A positive variation $\delta V$ is not possible from the optimum curve shown, since $V _ { k }$ is the maximum available rocket thrust velocity fixed by the specific impulse and the mass ratio. These arguments, therefore, establish the optimum program for the propellant utilization corresponding to positive $\Phi$ to be that of instantaneous burning at $t = 0$

![](images/ff3efa72d01c0d356074866650e79a52f5f4cb27e0e75541703cef11aad377b0.jpg)  
Fig. 8.4-2. Instantaneous burning at $t = 0$

![](images/3c64d647a7b7993cd2be7ed175c192db37ef029c8ab50ca79aa9888b6c5478ca.jpg)  
Fig. 8.4-3. Instantaneous burning at $t = T ,$

2. If $\Phi$ is negative, the optimum curve for $V ( t )$ must be as shown in Fig. 8.4-3,which implies instantaneous burning at t = T. Any variation δV from this curve would be positive, which would result in a negative $\delta U$ cr a smaller value of $\upsilon$

3. If $\Phi$ changes sign from plus to minus, the optimum curve for $V$ must appear as in Fig. 8.4 4,and part of the fuel must be burned instantaneously at $t = 0$ ,and the remainder at $t = T$ ， Again,any varied curve which has zero or positive slope is allowable,and if a positive $\delta U$ cannot be produced, the discontinuous curve of Fig. 8.4-4 must stand as the optimum curve.

![](images/3c99568b0f0b600da7bb304289a5de5853bfc01a41a618755997b4c2674ba973.jpg)  
Fig. 8.4-4. Instantaneous burning at $t = 0$ and $t = T ,$

# PROBLEMS

1. For a specified program of fuel utilization, $F / m$ is a known function of time which allows no variation in the quantity $F / m$ . Assume now that both the initial velocity $v _ { 0 }$ and its inclination $\theta _ { 0 }$ to be specified,and show that the optimum program for the thrust attitude $\phi ( t )$ is

$$
\tan \phi = \tan \phi _ { 0 } - C _ { 2 } t
$$

2. Show that,if a body is projected upwards with an initial velocity at an angle $\theta _ { 0 }$ , the tangent to the flight path will be

$$
\tan \theta = \left( 1 - { \frac { t } { T } } \right) \tan \theta _ { 0 }
$$

where $T =$ time for maximum height.

3. For the case $\phi _ { 0 } = \theta _ { 0 } ,$ show that $\Phi$ in Eq.8.4-7 is always positive,and that for optimum utilization of the propellant all of the fuel must be burned instantaneously at the beginning.

4. Assuming that $v _ { 0 }$ is zero,and all of the fuel is burned at the initial instant, determine the time $T$ at which maximum horizontal velocity is attained at height $Y _ { c }$

5.Determine the time required to deliver a satelite to a height $Y = 3 0 0$ miles witha horizontal velocity of $V = 2 2 , 0 0 0$ ft/sec.

6.In Prob.4,showthattheinitial thrust attitudeshould besin $\phi _ { 0 } = ( 1 / V _ { \mathit { k } } ) \ \times$ ${ \sqrt { 2 g Y } } ,$ and that $\nu _ { k }$ mustbegreaterthanthevelocitynecessaryforproecting a body vertically upwards to a height $\boldsymbol { \underline { \boldsymbol { \gamma } } } .$

7. In Prob.5, determine the initial angle $\phi _ { 0 }$ and the total rocket velocity $V _ { k }$ ：

8. For the case where the variation of Φ is from positive to negative, discuss how you would find V or the portion of the fuel to be burned at the initial instant.   
9. Determine the optimum fuel utilization program to achieve maximum height for a rocket shot vertically.   
10. Determine the optimum fuel utilization program for maximum height of a two-stage rocket of equal stages.   
11. Discusstheproblem of obtaining the greatest altitude for a specified horizontal velocity.   
12. Discuss the problem of minimum propellant consumption for a specified horizontal velocity and altitude.

# 8.5 Gravity Turn1

In the previous section it was shown that the optimum thrust attitude for placing a satellite into orbit is given by the equation,

$$
\tan \phi = \left( 1 - { \frac { t } { T } } \right) \tan \theta _ { 0 }
$$

Likewise, the optimum thrust atitude for maximum range (balistic missile) can be shown to be $\phi =$ constant. These conditions may be satisfactory for a rocket traveling in vacuum but, owing to the large angle of attack $( \phi - \theta )$ which results from such trajectories, they are not feasible through the atmosphere. Thus for flight through the atmosphere， a trajectory known as gravity turn is generally used. In a gravity turn the thrust vector is kept parallel to the velocity vector at all times, starting with some nonvertical initial velocity $v _ { 0 }$ .Thus the gravity turn is also one of zero angle of attack or zero lift.

It is convenient here to measure the angle made by the velocity vector from the vertical, as shown in Fig. 8.5-1. Again assuming zero aerodynamic drag and constant gravity field, we write equations for the forces in the tangential and normal directions to the trajectory.

$$
{ \begin{array} { l } { { \frac { 1 } { g } } { \frac { d v } { d t } } = { \frac { F } { m g } } - \cos \psi } \\ { { \frac { v } { g } } { \frac { d \psi } { d t } } = \sin \psi } \end{array} }
$$

These equations are nonlinear and no analytical solution is known when $F / m g$ varies with time. A reasonable assumption for $F / m g$ is $F =$ constant, and $m = m _ { 0 } - m ^ { \prime } t .$

When $F / m g$ is a constant, these nonlinear equations can be solved analytically. For F/mg to be constant, the thrust F must decrease with time to conform to the decreasing mass. If $F / m g$ is a varying function of time, we can assume $F / m g$ to be constant over short intervals of time, and we can carry out a step-by-step numerical integration, using the analytical solution over each interval. It is evident, then, that the analytical solution for constant $F / m g$ is of practical interest, and we consider its development as follows:

![](images/8abc6878757198db6767e934fe428a95470a88c7ad914641b1da5123ec7d5aaf.jpg)  
Fig. 8.5-l. Gravity turn trajectory.

Let $F / m g = n$ over a short increment of the flight path. We introduce

$$
z = \tan { \frac { 1 } { 2 } } \psi = { \sqrt { \frac { 1 - \cos \psi } { 1 + \cos \psi } } } = { \frac { \sin \psi } { 1 + \cos \psi } }
$$

Then

$$
z ^ { 2 } = { \frac { 1 - \cos \psi } { 1 + \cos \psi } }
$$

and

Differentiating Eq. 8.5-3,

Therefore,

$$
{ \frac { 1 - z ^ { 2 } } { 1 + z ^ { 2 } } } = \cos \psi
$$

$$
{ \frac { d z } { d t } } = { \frac { 1 } { 2 \cos ^ { 2 } \left( \psi / 2 \right) } } { \frac { d \psi } { d t } }
$$

$$
\frac { d \psi } { d t } = ( 1 + \cos \psi ) \frac { d z } { d t }
$$

By substitution into Eqs. 8.5-1 and 8.5-2, they become,

$$
\begin{array} { l } { { \displaystyle { \frac { 1 } { g } \frac { d v } { d t } = n - \frac { 1 - z ^ { 2 } } { 1 + z ^ { 2 } } } } } \\ { { \displaystyle { \frac { v } { g } \frac { d z } { d t } = z } } } \end{array}
$$

Eliminating $d t$ between the above equations,

$$
\frac { d v } { v } = n \frac { d z } { z } - \frac { 1 - z ^ { 2 } } { 1 + z ^ { 2 } } \frac { d z } { z }
$$

Integrating, we have (see Peirce\* nos. 53 and 55),

$$
\ln v = \ln z ^ { n } + \ln { \frac { 1 + z ^ { 2 } } { z } } + \ln C ^ { \prime }
$$

or

$$
v = C z ^ { n - 1 } ( 1 + z ^ { 2 } )
$$

The constant $C$ can be evaluated from initial conditions to be,

$$
C = \frac { v _ { 0 } } { z _ { 0 } ^ { n - 1 } ( 1 + { z _ { 0 } } ^ { 2 } ) }
$$

Substituting Eq. 8.5-7 into 8.5-5 and integrating,

$$
\begin{array} { l } { { \displaystyle t = \frac { C } { g } \int _ { z _ { 0 } } ^ { z } z ^ { n - 2 } ( 1 + z ^ { 2 } ) d z } } \\ { { \displaystyle \quad = \frac { C } { g } z ^ { n - 1 } \left( \frac { 1 } { n - 1 } + \frac { z ^ { 2 } } { n + 1 } \right) \bigg \vert _ { z _ { 0 } } ^ { z } } } \end{array}
$$

Equation 8.5-9 gives $t$ as a function of $z = \tan { \frac { 1 } { 2 \psi } }$ for any initial condition $C$ .Thus, conversely, $\psi$ is known in terms of $t$ and $C$ Equation 8.5-7 gives $v$ as a function of $z$ and $C$ ,so that $\boldsymbol { v }$ is also known in terms of $t$ and $C$ Thus Eqs. 8.5-7, 8.5-8, and 8.5-9 represent the solution for the gravity turn trajectory when the thrust-to-weight ratio $F / m g$ is a constant $n$

To apply these equations for a varying $F / m g$ ,we start with the initial conditions expressed by Eqs. 8.5-3 and 8.5-8, and $F / m g = n$ at $t = 0$ Choosing a value of $\psi$ slightly greater than $\psi _ { 0 }$ ,determine $\boldsymbol { v }$ from Eq. 8.5-7 and $\Delta t$ from Eq. 8.5-9. The increment in the displacement is, then,

$$
\begin{array} { r } { \Delta x = \frac { 1 } { 2 } ( v _ { 0 } \sin \psi _ { 0 } + v \sin \psi ) \Delta t } \\ { \Delta y = \frac { 1 } { 2 } ( v _ { 0 } \cos \psi _ { 0 } + v \cos \psi ) \Delta t } \end{array}
$$

The procedure can now be repeated with the values at the new point as initial condition.

# PROBLEMS

1. By reversing the force $F _ { s }$ show that the motion of a body hurled into a resisting medium can be solved by the techniques of this section.   
2.If $F / m g$ is constant throughout flight, what is the effect of changing the initial angle $\psi _ { 0 }$ on; (a) the final velocity; $( b )$ the time of flight.   
3. For constant value of $F / m g$ , the velocity and its inclination $\psi$ were observed at a given time. If the initial angle is doubled, how would the above quantities differ at the same time.

4. From Eqs. 8.5-1 and 8.5--2 derive the ballistic equation of a rocket

$$
{ \frac { 1 } { v } } { \frac { d v } { d \psi } } = \left( { \frac { F - D } { m g } } \right) { \frac { 1 } { \sin \psi } } - { \frac { 1 } { \tan \psi } }
$$

where $D$ is the aerodynamic drag.

Hint: The normal and tangential accelerations can be written as

$$
{ \begin{array} { r c l } { } & { } & { { v { \dot { \psi } } } = v ^ { 2 } / R } \\ { } & { } & { { \dot { v } } = { \cfrac { d v } { d \psi } } \cfrac { d \psi } { d s } \cfrac { d s } { d t } = \operatorname * { \frac { v } { R } } \cfrac { d v } { d \psi } } \end{array} }
$$

where $R$ is the radius of curvature of the trajectory, and $d s = R d \psi$

# REFERENCES

1. Culer, G. J. and B. D. Fried,“Universal Gravity Turn Trajectories,” J. Appl. Physics,28,No. 6 (June 1957), 672-676   
2.Hall, H. H.,and E. D. Zambeli,“On the Optimization of Multistage Rockets," Jet Propulsion,28 (July 1958),463-465.   
3. Okhotsimskii, D.E.,and T. M. Eneev,“Some Variation Problems Connected with theLaunching of Artificial Satelites of the Earth,”J.British InterplanetarySoc., 16 (5), (Jan.-Feb. 1958), 263-294.   
4.Bellman, R. and Dreyfus, S.,"An Application of Dynamic Programming of the DetermnationofOptimal Satelite Trajectories J.British InterplanetarySociety Vol. 16 No. 3-4 (1959), p. 78-83.   
5. Leitmann,G."Optimization Techniques with Appications to AerospaceSytem" Academic Press, New York,1962.

# Generalized Theories of Mechanics

# CHAPTER 9

# 9.l Introduction

Experience indicates that our learning process consists of first assimilating simple bits of information and,second,ofcomprehending the relationships between the various bits of information. As a result there begins to emerge an over-all pattern of behavior predictable from a theory. Simple theories are necessary for the beginner, in spite of the fact that they are limited in scope and incapable of extension beyond the bounds for which they are intended.

Beyond this stage must be a more general theory which encompasses and unites all special theories into a harmonious understanding. Such a generalized theory of mechanics was developed by Hamilton and Lagrange. It encompasses all of classical mechanics, and an understanding of this important work is an essential part of advanced dynamics.

Preliminary to the discusson of the generalized theories,it is necessary to have clearly in mind the basic concepts of coordinates and their classification.

# 9.2 System with Constraints

The degrees of freedom of a body correspond to the minimum number of independent coordinates required to define its position. For a particle free to move in space, three coordinates are necessary to define its position. They may be rectangular coordinates x, y, z, spherical coordinates r, 0, $\phi$ ， or some other system of coordinates, but three are necessary， and each coordinate may be varied independently. We say then that the free particle has three degrees of freedom.

If, next, the particle is constrained to move on a specified surface, only two coordinates are necessary to define its position, and we say that it has two degrees of freedom. For instance, the Iatitude and longitude completely define a position of a particle on the earth's surface. If the particle is further constrained to move along a specified line on the surface, one coordinate-such as the distance along this line-will define its position, and such a particle will have one degree of freedom. Here we have placed two constraints on the particle, one to restrict it to a surface, and another to confine the motion along some line on the surface. In each case the three degrees of freedom of a free particle have been reduced by the number of constraints imposed on the particle.

The constraints of a system can be expressed analytically in terms of its geometry. For example, a particle a distance I from the fixed end of a string is constrained to move on a spherical surface, the equation of which is,

$$
x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = l ^ { 2 }
$$

In the generalcase,theequation ofconstraintrestrictingaparticle to any surface is,

$$
f ( x , y , z ) = 0
$$

When the particle is constrained to move along a curve in space, the curve can be considered to be the intersection of two surfaces, so that the two constraint equations to be satisfied are,

$$
\begin{array} { r } { f _ { 1 } ( x , y , z ) = 0 } \\ { f _ { 2 } ( x , y , z ) = 0 } \end{array}
$$

An elementary example of two constraints is illustrated by the simple pendulum whose circular path in the vertical plane is the intersection of a sphere and a vertical plane through its center. The constraint equation, $x ^ { 2 } + y ^ { 2 } = l ^ { 2 } ,$ is actually the result of two equations,

Sphere

Plane

$$
\begin{array} { r } { x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = l ^ { 2 } } \\ { z = 0 } \end{array}
$$

with the coordinates oriented as shown in Fig. 9.2-1.

Sometimes a constraint equation willalso depend on time. For instance, if the support point of the simple pendulum is given a motion xo(t), the constraint equation would have to be writen as

$$
[ x - x _ { 0 } ( t ) ] ^ { 2 } + y ^ { 2 } = l ^ { 2 }
$$

It is evident,then,that for a time-dependent constraint, the equation may be written in the form,

$$
C ( x , y , z , t ) = 0
$$

Constraints may also be imposed between particles； e.g., two particles whose distance between them is always constant. The first particle has three degrees of freedom. The second particle has two degrees of freedom. Thus we have $3 + 2 = 5$ degrees of freedom for the two particles bound to each other a given distance apart. Actually two free particles would have six degrees of freedom; however a constraint has been introduced, specifying the distance between them, so that the degrees of freedom have been reduced by one.

![](images/079ad85b82e726fb90ccf3924dfd6c5dab814ece8a91db81437579ea260b5600.jpg)  
Fig. 9.2-I. Intersection of the $x , y$ plane and a sphere of radius / defines the path of the simple pendulum mass.

The position of a rigid body is known if we know the position of three noncollinear points on it. The three points, if free， would have nine degrees of freedom, but since there are three rigid constraints between them,a rigid body has six degrees of freedom. Another way of arriving at the same result is to choose the first point arbitrarily,in which case it will have three degrees of freedom. The second point must move in a sphere about the first, so it has two degrees of freedom. The third point must now move in a circular line about l and 2 as axis,which adds another degree of freedom, making a total of six degrees of freedom.

The general rule for $N$ particles can be stated as follows. If $N$ particles have $c$ constraints restricting their freedom, the number of degrees of freedom $n$ will be,

$$
n = 3 N - c
$$

# 9.3 Generalized Coordinates

A simple pendulum is defined as a point mass on the end of a weightless, inextensible string, which is made to move in a vertical plane, as shown in Fig. 9.3-1. The point mass must move on a circular line in the plane, and

![](images/a5cbd5d4646dbae66ba8afbe2ba061d75e2b4da0df7021fe8645d40158202de8.jpg)  
Fig. 9.3-l. Simple pendulum.

has one degree offreedom. The position of the mass may be specified by rectangular coordinates $x , y$ ， which are not independent but subject to the constraint equation,

$$
x ^ { 2 } + y ^ { 2 } = l ^ { 2 }
$$

It is simpler, however, to specify its position by the angle 0, which is independent and free of any constraint equation. Such independent coordinates are called generalized coordinates， and the number of such coordinates corresponds to the degrees of freedom of the system.

Consider next the double pendulum of Fig. 9.3-2, which is a system of two degrees of freedom. If the position of each mass is to be defined in terms of rectangular coordinates,four coordinates, $x _ { 1 } , y _ { 1 } , x _ { 2 } , y _ { 2 } ,$ would be necessary. There are however, two constraint equations between the coordinates,

$$
\begin{array} { r } { x _ { 1 } { } ^ { 2 } + y _ { 1 } { } ^ { 2 } = l _ { 1 } { } ^ { 2 } } \\ { ( x _ { 2 } - x _ { 1 } ) { } ^ { 2 } + ( y _ { 2 } - y _ { 1 } ) { } ^ { 2 } = l _ { 2 } { } ^ { 2 } } \end{array}
$$

and the number of coordinates minus the number of constraints again agree with the degrees of freedom of the system. Any two of the four rectangular coordinates can be considered independent, but the remaining two must be related by the above constraint equations.

The double pendulum can also be defined by two angles, 01 and 02. Each θ can be varied independently and, therefore, no constraints exist between them. 01 and 0 are thus generalized coordinates for the double pendulum.

For a system of $n$ degrees offreedom, there are $n$ generalized coordinates, $q _ { 1 } , q _ { 2 } , q _ { 3 } , \ q _ { 4 } , . . . , q _ { n } .$ They are independent coordinates free from any constraints. They are not necessarily lengths or angles, but can be any independent set of quantities which describe completely the motion of the system.

![](images/931de8ee1dbd1adf72da4bb525ae701bfe7bffe8e9e5dd6809e7fa57173cfbd5.jpg)  
Fig. 9.3-2. Double pendulum.

It is always possible to relate the rectangular coordinates as some function of the generalized coordinates. For instance, in the case of the double pendulum, the rectangular coordinates expressed in terms of the generalized coordinates $q _ { 1 } = \theta _ { 1 }$ and $q _ { 2 } = \theta _ { 2 }$ are

$$
\begin{array} { l } { x _ { 1 } = l _ { 1 } \sin \theta _ { 1 } } \\ { y _ { 1 } = l _ { 1 } \cos \theta _ { 1 } } \\ { x _ { 2 } = l _ { 1 } \sin \theta _ { 1 } + l _ { 2 } \sin \theta _ { 2 } } \\ { y _ { 2 } = l _ { 1 } \cos \theta _ { 1 } + l _ { 2 } \cos \theta _ { 2 } } \end{array}
$$

In the more general case, the relationships between the various position coordinates x, y,z and the generalized coordinates can be expressed by the functional equation,

$$
x _ { i } = f _ { i } ( q _ { 1 } , q _ { 2 } , q _ { 3 } , . . . , q _ { n } , t )
$$

where $n$ is the number of degrees of freedom of the system.

# 9.4 Holonomic and Nonholonomic System

When the constraints are expressible as functions of the coordinates or coordinates and time, the system is said to be holonomic. Sometimes the constraints are expressed in terms of the velocities； however, if such expressions are integrable, we obtain the constraint equations as function of the coordinates or coordinates and time, so again we have a holonomic system.

![](images/90623b34dd3f3173ba1952fd029a85e81b0ee46a263ac612cec810625f24533a.jpg)  
Fig. 9.4-l. Example of holomonic system.

As an example, consider a wheel roling without slipping along a specified straightline,asshownin Fig.9.4-1.The velocityof thecenter is $\dot { x } = r \dot { \phi }$ ,which can be integrated to $x = r \phi + c$ The system is hence holonomic.

![](images/c43057cd0ab4c41814b956231637ddc6a64c05fa0e493076fa6cba3f437f1e66.jpg)  
Fig.9.4-2. Example of nonholonomic system.

If the same wheel rols without slipping on a plane, and is allowed to pivot about a vertical axis through thepoint ofcontact,as shown inFig. 9.4-2, the relationship between the velocities willbe found to be nonintegrable,and hence the system must be clasified as nonholonomic. We have,forinstance,the equations for the velocity normal and paralel to the path as,

$$
\begin{array} { l } { { \dot { x } \sin \theta - \dot { y } \cos \theta = 0 } } \\ { { \dot { x } \cos \theta + \dot { y } \sin \theta = r \dot { \phi } } } \end{array}
$$

and it is not possible to integrate these expressions to obtain relationships between the coordinates. It is possible, for instance, to roll the wheel to another point withadifferentvalue of $_ x$ ,but withtheothercoordiates $y$ $\theta$ ,and $\phi$ unchanged. It is evident, then, that $x$ cannot be functionally related to the remaining coordinates. Each of the other coordinates can be singled outin the same manner,so that there can be no unique relationship existing between them. We have only a relationship between the infinitesimals which can be writen as

$$
\begin{array} { r } { \sin \theta d x - \cos \theta d y = 0 } \\ { \cos \theta d x + \sin \theta d y - r d \phi = 0 } \end{array}
$$

In a holonomic system, the constraint equations are in the form,

$$
C ( r _ { 1 } , r _ { 2 } , r _ { 3 } , \ldots , t ) = 0
$$

Moreover,the diferential of the constraint equation is exact and expressible as,

$$
d C = { \frac { \partial C } { \partial r _ { 1 } } } d r _ { 1 } + { \frac { \partial C } { \partial r _ { 2 } } } d r _ { 2 } + \cdots { \frac { \partial C } { \partial t } } d t = 0
$$

It is also possible in the holonomic system to reduce the number of the dependent variables $r _ { i }$ by the number of constraint equations tothenumber of the degrees of freedom of the system. These are then expressible in terms of the $n$ generalized coordinates, equal to the number of degrees of freedom of the system,and independent of each other. Thus, provided we are able to find the $n$ generalized coordinates of the system, the problem reduces to that of solving $n$ independent equations in $q _ { i } ,$ without concern of the constraints of the system.

In the nonholonomic system, the constraints are not expressible in terms of the coordinates or coordinates and time, as in Eq. 9.4-1. The constraint equations are available only as relationships between the infinitesimals,

$$
a _ { 1 } d r _ { 1 } + a _ { 2 } d r _ { 2 } + \cdots + a _ { m } d t = 0
$$

which are nonintegrable. Thus, if we transform the dependent variables $r _ { i }$ into the equation

$$
r _ { i } = r _ { i } ( q _ { 1 } , q _ { 2 } , \ldots , t )
$$

we would find that not all the $q$ are independent. Special procedures to be used under these conditions are discussed in Sec. 9.9.

# 9.5 Principle of Virtual Work

A virtual displacement δx, δ0, δq, etc., is an infinitesimal change in the coordinate, which may be conceived in any manner irrespective of the time t. It may or may not coincide with the actual displacement,dx,d0,dq.

In the case of constrained motion, the virtual displacement must be compatible with the constraints. For instance,if a particle is constrained to move on a surface, the virtual displacement must be confined to the surface. If the constraint equation for this case is

$$
f ( x , y , z , t ) = 0
$$

the virtual displacement must satisfy the equation,

$$
\frac { \partial f } { \partial x } \delta x + \frac { \partial f } { \partial y } \delta y + \frac { \partial f } { \partial z } \delta z = 0
$$

For a nonholonomic constraint, the restriction is

$$
a _ { 1 } \delta x + a _ { 2 } \delta y + a _ { 3 } \delta z = 0
$$

Since virtual displacements are made irrespective of time, the above expression must be independent of time t.

Consider a particle acted upon by several forces. If the particle is in equilibrium, the resultant R of the forces must vanish,and the work done by the forces in a virtual displacement $\delta \mathbf { r }$ is zero.

$$
\mathbf { R } \cdot \delta \mathbf { r } = 0
$$

If the particle is constrained, the force R may be separated into an applied force F and a constraint force f. For equilibrium,

$$
\mathbf { R } = \mathbf { F } + \mathbf { f } = 0
$$

and the applied force is balanced by the constraint force. The virtual work is then,

$$
\mathbf { F } \cdot \delta \mathbf { r } + \mathbf { f } \cdot \delta \mathbf { r } = 0
$$

But now the virtual displacement $\delta \mathbf { r }$ must be consistent with the constraint, which requires that f $\mathbf { \nabla } \cdot \delta \mathbf { r } = 0$ . For instance,a particle made to move along a smooth wire would have a constraint force of the wire acting normal to the wire and hence to the virtual displacement. Thus the constraint force cannot contribute to the work,and we are left with the result,

$$
\mathbf { F } \cdot \delta \mathbf { r } = 0
$$

which states that, if the particle is in equilibrium, the work done by the applied forces due to a virtual displacement is zero.

For a system of particles in equilibrium,the sum of the forces acting on each particle must vanish. The virtual work of the system is the sum of the virtual work done on each particle, which must also be zero.

$$
\sum _ { i } { \bf R } _ { i } \cdot \delta { \bf r } _ { i } = 0
$$

The force $\mathbf { R } _ { i }$ can again be separated into the applied force $\mathbf { F } _ { i }$ and the force of constraint $\mathbf { f } _ { i } ,$ and since∑f·r =O,weobainthevirtual work forthe system of particles to be,

$$
\sum _ { i } \mathbf { F } _ { i } \cdot \delta \mathbf { r } _ { i } = 0
$$

where $\mathbf { F } _ { i }$ and $\delta \bar { \mathbf { r } } _ { i }$ are the applied force and the virtual displacement associated with particle i. Thus the principle of virtual work as presented by Jean Bernouli (1717) can be stated as follows: If a system of forces are in equilibrium, the work done by the applied forces in a virtual displacement compatible with the constraints is zero.

For a rigid body or a system of interconnected rigid bodies, internal forces, which always appear in equal and opposite pairs, must do no work. Thus,with the principle of virtual work, we can ignore allinternal forces and reaction forces of constraints, and equate the virtual work of the applied forces to zero.

# 9.6 D'Alembert's Principle

The principle of virtual work, established for the case of static equilibrium, can be extended to dynamics by a reasoning advanced by D'Alembert (1743). We will let p be the momentum of a particle in the system, and separate the forces acting on it into an applied force F and a constraint force f. The equation of motion of the particle can then be written as

$$
\mathbf { F } + \mathbf { f } - { \dot { \mathbf { p } } } = 0
$$

which states that the forces are in equilibrium with the kinetic reaction $- \dot { \mathfrak { p } }$ The quantity $- { \dot { \mathbf { p } } }$ is sometimes referred to as the “reverse effective force” because the force effective in producing the motion is equal to $\dot { \mathbf { p } } .$ ,and,if such a force is applied in the reverse sense, the motion could be nullified to produce a state of static equilibrium. As before, the virtual work of the constraint force is zero since f and $\delta \mathbf { r }$ are mutually perpendicular. The virtual work of the forces acting on the particle is, then,

$$
( \mathbf { F } - { \dot { \mathbf { p } } } ) \cdot \delta \mathbf { r } = 0
$$

and for the system of $N$ particles, we sum to obtain the result

$$
\sum _ { i = 1 } ^ { N } ( \mathbf { F } - \dot { \mathbf { p } } ) _ { i } \cdot \delta \mathbf { r } _ { i } = 0
$$

# PROBLEMS

1.A constraint is scleronomic if time-independent,and it is rheonomic if timedependent. If a particle of mass $m$ is free to slide on a smooth hoop of radius r, which is rotated with constant speed $\Omega$ about a verticle diameter,discuss the degrees of freedom and the type of constraint, holonomic, nonholonomic, scleronomic, or rheonomic.

2. The vertical diameter of a wheel rolling on a rough horizontal floor is rotated at a constant rate to form a circular path for the contact point. Is the con-straint holonomic or nonholonomic?

3. A sphere of radius $^ a$ , rolling on a rough, horizontal plane is a nonholonomic system. Attach body axes $x$ ， $y$ ， $z$ to the center of the sphere, defining their position by the Euler angles $\theta$ ， $\psi$ ， $\varphi$ . Show that the angular velocity of the sphere with respect to fixed axes $X , ~ Y$ ， $Z$ is $\boldsymbol { \omega } = \omega _ { X } \mathbf { I } + \omega _ { Y } \mathbf { J } + \omega _ { z } \bar { \mathbf { K } }$ where,

$$
\begin{array} { l } { { \omega _ { X } = \dot { \theta } \cos \psi + \dot { \varphi } \sin \theta \sin \psi } } \\ { { \omega _ { Y } = \dot { \theta } \sin \psi - \dot { \varphi } \sin \theta \cos \psi } } \\ { { \omega _ { Z } = \dot { \psi } + \dot { \varphi } \cos \theta } } \end{array}
$$

Show also that the constraint equation for no slipping is

$$
{ \bf V } _ { 0 } + \boldsymbol { \omega } \times { \bf r } = 0
$$

where $\mathbf { V } _ { 0 }$ is the velocity of the center of the sphere, and $\mathbf { r } = - a \mathbf { K }$

4. In Prob. 3, determine the variation of the constraint equation along the $X$ and $Y$ axes.

5. Virtual work for a system of $N$ particles can be expressed by the equation $\sum _ { i = 1 } ^ { N } ( \mathbf { F } _ { i } - m _ { i } { \ddot { \mathbf { r } } } _ { i } ) \cdot \delta \mathbf { r } _ { i } = 0$ Discuss the interpretation of this equation for a system of free particles versus a system of constrained particles.

# 9.7 Hamilton’s Principle

The principle of virtual work together with D'Alembert's principle was viewed by W. R.Hamilton (1805-1865) as a basis for his variational approach, leading to one of the most general statements of mechanics known as the Hamilton's Principle. It reduces the formulation of problems in dynamics to that of the variation of a scalar integral, irrespective of coordinates and for conservative and nonconservative systems.

We start with $N$ discrete mass particles, coupled by either holonomic or nonholonomic forces of constraints,and write the virtual work equation,

$$
\sum _ { i = 1 } ^ { N } ( m _ { i } { \ddot { \mathbf { r } } } _ { i } - \mathbf { F } _ { i } ) \cdot \delta \mathbf { r } _ { i } = 0
$$

We recognize inthis equationthat $\sum _ { i = 1 } ^ { N } \boldsymbol { F } _ { i } \cdot \delta \mathbf { r } _ { i }$ is the work done by the external forces in a virtual displacement, which could include nonconservative forces.

$$
\sum _ { i = 1 } ^ { N } \mathbf { F } _ { i } \cdot \delta \mathbf { r } _ { i } = \delta W
$$

Relating totefirst term ofEq.9.7-1,the followingdifferentialrlationships exist:

$$
\begin{array} { l } { { \displaystyle { \frac { d } { d t } } \left( { \dot { \bar { \mathbf { r } } } } _ { i } \cdot \delta \mathbf { r } _ { i } \right) = { \dot { \bar { \mathbf { r } } } } _ { i } \cdot { \frac { d } { d t } } \delta \mathbf { r } _ { i } + { \ddot { \bar { \mathbf { r } } } } _ { i } \cdot \delta \mathbf { r } _ { i } } } \\ { ~ = { \dot { \bar { \mathbf { r } } } } _ { i } \cdot \delta { \dot { \bar { \mathbf { r } } } } _ { i } + { \ddot { \bar { \mathbf { r } } } } _ { i } \cdot \delta \mathbf { r } _ { i } } \\ { ~ = \delta ( \frac { 1 } { 2 } { \dot { \bar { \mathbf { r } } } } _ { i } ^ { 2 } ) + { \ddot { \bar { \mathbf { r } } } } _ { i } \cdot \delta \mathbf { r } _ { i } } \end{array}
$$

The first term of Eq.9.7-1 can then be written as

$$
\begin{array} { c } { \displaystyle \sum _ { i = 1 } ^ { N } m _ { i } \ddot { \bf r } _ { i } \cdot \delta { \bf r } _ { i } = \displaystyle \sum _ { i = 1 } ^ { N } \frac { d } { d t } \left( m _ { i } \dot { \bf r } _ { i } \cdot \delta { \bf r } _ { i } \right) - \sum _ { i = 1 } ^ { N } \delta \left( \frac { 1 } { 2 } m _ { i } \dot { r } _ { i } ^ { ~ 2 } \right) } \\ { = \displaystyle \sum _ { i = 1 } ^ { N } \frac { d } { d t } \left( m _ { i } \dot { \bf r } _ { i } \cdot \delta { \bf r } _ { i } \right) - \delta T } \end{array}
$$

and Eq. 9.7-1 becomes

$$
\sum _ { i = 1 } ^ { N } { \frac { d } { d t } } \left( m _ { i } { \dot { \mathbf { r } } } _ { i } \cdot \delta \mathbf { r } _ { i } \right) = \delta T + \delta W
$$

Consider times $t = 0$ and $t = t _ { 1 }$ at which $\delta \mathbf { r } _ { i } = 0$ , and integrate Eq. 9.7-5:

$$
\int _ { 0 } ^ { t _ { 1 } } \sum _ { i = 1 } ^ { N } { \frac { d } { d t } } \left( m _ { i } { \dot { \mathbf { r } } } _ { i } \cdot \delta \mathbf { r } _ { i } \right) d t = \int _ { 0 } ^ { t _ { 1 } } ( \delta T + \delta W ) d t
$$

The left side of this equation is equal to the integrand evaluated at the upper and lower limits:

$$
\sum _ { i = 1 } ^ { N } m _ { i } \dot { \mathbf { r } } _ { i } \cdot \delta \mathbf { r } _ { i } \bigg | _ { 0 } ^ { \ell _ { 1 } } { = } \int _ { 0 } ^ { \ell _ { 1 } } ( \delta T + \delta W ) d t
$$

But since $\delta \bar { \mathbf { r } } _ { i }$ equals zero at $t = 0$ and $t _ { 1 }$ ,the left side of Eq. 9.7-7 is zero, and we arrive at the final result

$$
\int _ { 0 } ^ { t _ { 1 } } ( \delta T + \delta W ) d t = \delta \int _ { 0 } ^ { t _ { 1 } } T d t + \int _ { 0 } ^ { t _ { 1 } } \delta W d t = 0
$$

We will review now the variational principle leading to Eq. 9.7-8. The motion of the system defined by the time variation of the Nr, is defined as the dynamical path. At any time t between t = O and t1, the N-valued r; are given a virtual displacement Sr, thereby varying the dynamical path under the restriction $\delta t = 0$ . In the varied configuration, $T$ and $W$ undergo variations δT and δW due to the variation in the coordinates and their velocities. Of all the possible variations, the dynamical path corresponds to the one which leads to a stationary value of the integral in Eq. 9.7-8 which is Hamilton's principle.

When the system is conservative the work can be expressed in terms of the potential energy in which case Eq. 9.7-8 reduces to

$$
\delta \int _ { 0 } ^ { t _ { 1 } } ( T + W ) d t = 0
$$

Hamilton's principle states that, if the configuration of the system at two instants $t = 0$ and $t _ { 1 }$ is known, the motion of the system is given by the stationarity of the scalar integral. Hamilton's principle does not provide the solution to the dynamical problem, but formulates the equations of motion in a general manner irrespective of the coordinate system. It embodies both the Lagrange equation and the theorem of conservation of energy.

# 9.8 Lagrange's Equation (Holonomic System)

For a holonomic system, the dependent-variables $\mathbf { r } _ { i }$ can be expressed entirely in terms of the $n$ -generalized coordinates $q _ { k }$ and time t, corresponding to the $n$ degrees of freedom.

$$
\mathbf { r } _ { i } = \mathbf { r } _ { i } ( q _ { 1 } , q _ { 2 } , \ldots , q _ { n } , t )
$$

The $q _ { k }$ in the above equation are independent and no constraint equation exists between them.

Differentiating Eq. 9.8-1, the velocity can be written as

$$
{ \dot { \mathbf { r } } } _ { i } = { \frac { \partial \mathbf { r } _ { i } } { \partial q _ { 1 } } } { \dot { q } } _ { 1 } + { \frac { \partial \mathbf { r } _ { i } } { \partial q _ { 2 } } } { \dot { q } } _ { 2 } + \cdots + { \frac { \partial \mathbf { r } _ { i } } { \partial q _ { n } } } { \dot { q } } _ { n } + { \frac { \partial \mathbf { r } _ { i } } { \partial t } }
$$

By squaring and summing over allthe particles of the system, the kinetic energy becomes

$$
{ \boldsymbol { T } } = { \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { N } m _ { i } { \dot { \bar { \mathbf { r } } } } _ { \mathrm { { \ell } } ^ { 2 } } = { \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { N } m _ { i } \left[ \sum _ { k } ^ { n } \sum _ { l } ^ { n } { \frac { \partial \mathbf { r } _ { i } } { \partial q _ { k } } } { \frac { \partial \mathbf { r } _ { i } } { \partial q _ { l } } } { \dot { q } } _ { k } { \dot { q } } _ { l } + 2 { \frac { \partial \mathbf { r } _ { i } } { \partial t } } \sum _ { k } ^ { n } { \frac { \partial \mathbf { r } _ { i } } { \partial q _ { k } } } { \dot { q } } _ { k } + \left( { \frac { \partial \mathbf { r } _ { i } } { \partial t } } \right) ^ { 2 } \right]
$$

It is evident then that $T$ is a function of $q _ { k }$ ， $\dot { q } _ { k }$ ,and $t$ , and we may write

$$
T = T ( q _ { 1 } , q _ { 2 } , \ldots , { \dot { q } } _ { 1 } , { \dot { q } } _ { 2 } , \ldots , t )
$$

We will now consider the variation δTin Hamilton's equation, holding $t$ fixed

and

$$
\delta T = \sum _ { i = 1 } ^ { n } { \frac { \partial T } { \partial q _ { i } } } \delta q _ { i } + \sum _ { i = 1 } ^ { n } { \frac { \partial T } { \partial { \dot { q } } _ { i } } } \delta { \dot { q } } _ { i }
$$

$$
\int _ { 0 } ^ { t _ { 1 } } \delta T d t = \sum _ { i = 1 } ^ { n } \int _ { 0 } ^ { t _ { 1 } } { \frac { \partial T } { \partial q _ { i } } } \delta q _ { i } d t + \sum _ { i = 1 } ^ { n } \int _ { 0 } ^ { t _ { 1 } } { \frac { \partial T } { \partial { \dot { q } } _ { i } } } \delta { \dot { q } } _ { i } d t
$$

Writing the last integral in the form,

$$
\int _ { 0 } ^ { t _ { 1 } } { \frac { \partial T } { \partial { \dot { q } } _ { i } } } \delta { \dot { q } } _ { i } d t = \int _ { 0 } ^ { t _ { 1 } } { \frac { \partial T } { \partial { \dot { q } } _ { i } } } { \frac { d } { d t } } \delta q _ { i } d t
$$

we integrate by parts, letting

$$
u = { \frac { \partial T } { \partial { \dot { q } } _ { i } } } \qquad d v = { \frac { d } { d t } } \delta q _ { i } d t
$$

Then

$$
d u = { \frac { d } { d t } } { \frac { \partial T } { \partial { \dot { q } } _ { i } } } d t \qquad v = \delta q _ { i }
$$

and the integral becomes

$$
\int _ { 0 } ^ { t _ { 1 } } \frac { \partial T } { \partial { \dot { q } } _ { i } } \frac { d } { d t } \delta q _ { i } d t = \frac { \partial T } { \partial { \dot { q } } _ { i } } \delta q _ { i } \bigg | _ { 0 } ^ { t _ { 1 } } - \int _ { 0 } ^ { t _ { 1 } } \delta q _ { i } \frac { d } { d t } \frac { \partial T } { \partial { \dot { q } } _ { i } } d t
$$

Since $\delta q _ { i } = 0$ at $t = 0$ and $\tau _ { 1 }$ , the first term on the right is zero and Eq. 9.8-6 becomes,

$$
\delta \int _ { 0 } ^ { t _ { 1 } } T d t = - \sum _ { i = 1 } ^ { n } \int _ { 0 } ^ { t _ { 1 } } \left( { \frac { d } { d t } } { \frac { \partial T } { \partial { \dot { q } } _ { i } } } - { \frac { \partial T } { \partial q _ { i } } } \right) \delta q _ { \ i } d t
$$

Consider next the variation $\delta W$ due to the $^ m$ forces acting on the system

$$
\delta W = \sum _ { j = 1 } ^ { m } \mathbf { F } _ { j } \cdot \delta \mathbf { r } _ { j }
$$

The virtual displacement $\partial r _ { j }$ is

$$
\delta \mathbf { r } _ { j } = { \frac { \partial \mathbf { r } _ { j } } { \partial q _ { 1 } } } \delta q _ { 1 } + { \frac { \partial \mathbf { r } _ { j } } { \partial q _ { 2 } } } \delta q _ { 2 } + \cdots + { \frac { \partial \mathbf { r } _ { j } } { \partial q _ { n } } } \delta q _ { n }
$$

so that $\delta W$ becomes

$$
\delta W = \sum _ { j = 1 } ^ { m } \left( \mathbf { F } _ { j } \cdot { \frac { \partial \mathbf { r } _ { j } } { \partial q _ { 1 } } } \delta q _ { 1 } + \mathbf { F } _ { j } \cdot { \frac { \partial \mathbf { r } _ { j } } { \partial q _ { 2 } } } \delta q _ { 2 } + \cdots \cdot \mathbf { F } _ { j } \cdot { \frac { \partial \mathbf { r } _ { j } } { \partial q _ { \eta } } } \delta q _ { n } \right)
$$

We can now define the generalized force $Q _ { i }$ associated with $q _ { i }$ to be

$$
Q _ { i } = \sum _ { j = 1 } ^ { m } \mathbf { F } _ { j } \cdot { \frac { \partial \mathbf { r } _ { j } } { \partial q _ { i } } }
$$

which enables Eq. 9.8-10 to be written as

$$
\delta W = Q _ { 1 } \delta q _ { 1 } + Q _ { 2 } \delta q _ { 2 } + \cdots Q _ { n } \delta q _ { n } = \sum _ { i = 1 } ^ { n } Q _ { i } \delta q _ { i }
$$

We now substitute Eqs. 9.8-7 and 9.8-12 into Hamilton's equation,

$$
\delta \int _ { 0 } ^ { \ell _ { 1 } } ( T + W ) d t = - \sum _ { i = 1 } ^ { n } \int _ { 0 } ^ { t _ { 1 } } \left( { \frac { d } { d t } } { \frac { \partial T } { \partial { \dot { q } } _ { i } } } - { \frac { \partial T } { \partial q _ { i } } } - \ Q _ { i } \right) \delta q _ { i } d t = 0
$$

and since all the $\delta \boldsymbol { q } _ { i }$ are independent and arbitrary, we can let all the $\partial { q _ { i } }$ equal zero except for $\delta q _ { k }$ which will be specified as not equal to zero. Then in order to satisfy the above equation,the coeffcient of $\delta q _ { k }$ must be zero, and we arrive at Lagrange's equation for the holonomic system.

$$
\frac { d } { d t } \frac { \partial T } { \partial { \dot { q } } _ { k } } - \frac { \partial T } { \partial q _ { k } } = Q _ { k }
$$

So far we have not stated whether the forces $\mathbf { F } _ { j }$ are conservative or nonconservative.Foraconservativesystem,the work isexpresiblein terms of the potential energy $U$

and

$$
W = - U ( q _ { i } )
$$

$$
\delta W = - \sum _ { \partial q _ { i } } \delta q _ { i }
$$

It is evident then that Lagrange's equation for the conservative system is

$$
\frac { d } { d t } \frac { \partial T } { \partial \dot { q } _ { k } } - \frac { \partial T } { \partial q _ { k } } + \frac { \partial U } { \partial q _ { k } } = 0
$$

It is now convenient to define the Lagrangian as

$$
L = T - U
$$

and since $\partial U / \partial { \dot { q } } _ { k } = 0$ ,Eq.9.8-17caneiensoftheLaian as

$$
{ \frac { d } { d t } } { \frac { \partial L } { \partial { \dot { q } } _ { k } } } - { \frac { \partial L } { \partial q _ { k } } } = 0
$$

When both conservative and nonconservative forces act on a system, we can separate the virtual work into terms likeEqs.9.8-12and 9.8-16,and write Lagrange's equation as

$$
{ \frac { d } { d t } } { \frac { \partial L } { \partial { \dot { q } } _ { k } } } - { \frac { \partial L } { \partial q _ { k } } } = Q _ { k }
$$

# Example 9.8-1

The pendulum analogy is used in the simplified analysis of many dynamical problems, including the sloshing of liquid fuel in missiles. As an application of Lagrange's equation, we willconsider here the spherical pendulum ofFig.9.8-1.

![](images/120915d89dd96a5bd5438ba92a0ecc7a06db6ea2a2edbe0fce1a076a0b8fa3a5.jpg)  
Fig. 9.8-l. Spherical pendulum.

The position of the mass, at a distance $l$ from the center,can be specified by the generalized coordinates $\theta$ and $\boldsymbol { \varphi }$ ， which can be varied independently.

The kinetic and potential energies are,

$$
\begin{array} { l } { { T = \frac { 1 } { 2 } m [ ( l \dot { \theta } ) ^ { 2 } + ( l \dot { \varphi } \sin \theta ) ^ { 2 } ] } } \\ { { \ } } \\ { { U = m g l ( 1 - \cos \theta ) } } \end{array}
$$

and the Lagrangian becomes,

$$
L = \frac { \ d } { \ d t } m [ ( l \dot { \theta } ) ^ { 2 } + ( l \dot { \varphi } \sin \theta ) ^ { 2 } ] - m g l ( 1 - \cos \theta )
$$

Substituting into Lagrange's equation, the equations of motion are,

$$
m l ^ { 2 } \Big ( \ddot { \theta } - \dot { \varphi } { } ^ { 2 } \sin \theta \cos \theta + \frac { g } { l } \sin \theta \Big ) = 0
$$

$$
m l ^ { 2 } ( \ddot { \varphi } \sin ^ { 2 } \theta + 2 \dot { \varphi } \dot { \theta } \sin \theta \cos \theta ) = 0
$$

The solution of these equations can be obtained in the following manner. Equation e can be writen as

$$
{ \frac { d } { d t } } \dot { \varphi } \sin ^ { 2 } \theta = 0
$$

$$
\dot { \varphi } \sin ^ { 2 } \theta = C _ { 1 }
$$

If we examine the Lagrangian,we would note that $L$ is independent of $\varphi _ { i }$ so that

$$
{ \frac { \partial { L } } { \partial { \varphi } } } = 0
$$

We should then expect Lagrange's equation for the coordinate to reduce to

$$
\frac { d } { d t } \frac { \partial L } { \partial \dot { \varphi } } = 0
$$

and

$$
{ \frac { \partial L } { \partial { \dot { \varphi } } } } = { \mathrm { c o n s t a n t } }
$$

Equation $f$ then is the direct consequence of $\partial { \cal L } / \partial \varphi = 0$

We can now make a general statement as follows: If the Lagrangian is not a function of the generalized coordinate $q _ { k }$ ，then $\partial L / \partial q _ { k } = 0$ , and Lagrange's equation for $q _ { k }$ becomes

$$
\frac { d } { d t } \frac { \partial L } { \partial \dot { q } _ { k } } = 0
$$

Its integral is then immediately available as

$$
\begin{array} { c } { { ( g ) } } \\ { { } } \\ { { \ } } \\ { { ( h ) } } \end{array}
$$

$$
{ \frac { \partial L } { \partial { \dot { q } } _ { k } } } = { \mathrm { c o n s t a n t } } = p _ { k }
$$

where $p _ { k }$ is the generalized momentum for coordinate $q _ { k }$ . Such coordinates are called cyclic coordinates.

Returning to the solution of the two equations of motion, we substitute $\dot { \varphi }$ from Eq $f$ into Eq.d,

$$
\ddot { \theta } - { C _ { 1 } } ^ { 2 } { \frac { \cos \theta } { \sin ^ { 3 } \theta } } + { \frac { \sigma } { l } } \sin \theta = 0
$$

We solve this equation in the usual way by multiplying by $2 \dot { \theta }$ and integrating.

$$
2 \dot { \theta } \ddot { \theta } = 2 \dot { \theta } { C _ { 1 } } ^ { 2 } \frac { \cos \theta } { \sin ^ { 3 } \theta } - \frac { 2 g } { l } \dot { \theta } \sin \theta
$$

$$
\int d ( \dot { \theta } ^ { 2 } ) = 2 { C _ { 1 } } ^ { 2 } \int \frac { \cos \theta d \theta } { \sin ^ { 3 } \theta } - \frac { 2 g } { l } \int \sin \theta d \theta
$$

The solution for $\boldsymbol { \dot { \theta } }$ is then,

$$
\dot { \theta } ^ { 2 } = - \frac { { C _ { 1 } } ^ { 2 } } { \sin ^ { 2 } \theta } + \frac { 2 g } { l } \cos \theta + C _ { 2 }
$$

We have so far identified the constant C1 as the generalized momentum Po. Wewillshownowthattheconstant $C _ { 2 }$ isassocaedwiththetotaleergy $E$ of conservative system, which is

$$
E = T + U = 2 T - L
$$

We have from. Eqs. a, $^ b$ ,and c,

$$
m l ^ { 2 } { \Biggl [ } \dot { \theta } ^ { 2 } + \dot { \varphi } ^ { 2 } \sin ^ { 2 } \theta - { \frac { 1 } { 2 } } \dot { \theta } ^ { 2 } - { \frac { 1 } { 2 } } \dot { \varphi } ^ { 2 } \sin ^ { 2 } \theta + { \frac { g } { l } } ( 1 - \cos \theta ) { \Biggr ] } = E
$$

Eliminating $\dot { \varphi }$ from Eq $f ,$ we arrive at the result

$$
{ \dot { \theta } } ^ { 2 } = - \frac { p _ { \varphi } ^ { ~ 2 } } { \sin ^ { 2 } \theta } + \frac { 2 g } { l } \cos \theta + 2 \left( \frac { E } { m l ^ { 2 } } - \frac { g } { l } \right)
$$

By comparison with Eq.j, we find that

$$
C _ { 2 } = 2 \left( \frac { E } { m l ^ { 2 } } - \frac { g } { l } \right)
$$

# Example 9.8-2

A spinning satellite with moments of inertia $A$ ， $A$ ， $C$ with $C < A$ has whip antennas which are free to vibrate in the $z$ direction,as shownin Fig.9.8-2. Set up the vibration equation,using generalized coordinates associated with the normal modes of the antenna beam, and outline a procedure to establish the attitude drift of the spin axis.

![](images/73e25e30c5b1c2f92ad1e9ece95a2c388ae26409e91b621c54920d958d08c0f4.jpg)  
Fig. 9.8-2. Energy dissipation by whip antennas of a satellite.

We will assume the beam to have structural damping,which can be accounted for by a complex stiffness $E I ( 1 + i \alpha )$ ,where $_ { \alpha }$ is the structural damping factor. Letting $m$ be the mass per unit length of the antenna,and $w$ the elastic deflection in the $\boldsymbol { \mathscr { z } }$ direction, the differential equation of motion is

$$
E I ( 1 + i \alpha ) { \frac { \partial ^ { 4 } w } { \partial x ^ { 4 } } } + m { \frac { \partial ^ { 2 } w } { \partial t ^ { 2 } } } = m a _ { z }
$$

The acceleration $a _ { z }$ is that of a point along the undeformed antenna, which from Eq.7.6 14ais

$$
a _ { z } = 2 { \frac { C } { A } } ( x _ { 0 } + x ) { \omega _ { 0 } } ^ { 2 } \sin \theta \cos \theta \sin \dot { \varphi } t
$$

We will express the deflection in terms of generalized coordinates $q _ { n } ( t )$ and the normal modes $\varphi _ { n } ( x )$ of the antenna;

$$
w ( x , t ) = \sum _ { n = 1 } ^ { \infty } q _ { n } ( t ) \varphi _ { n } ( x )
$$

The normal modes are vibration shapes associated with the undamped harmonic oscillations at the natural frequencies $\Omega _ { n }$ , which obey the equation

$$
E I { \frac { d ^ { 4 } \varphi _ { n } } { d x ^ { 4 } } } - m \Omega _ { n } { } ^ { 2 } \varphi _ { n } = 0
$$

We now substitute Eq. $c$ into $^ a$ and replace $E I ( d ^ { 4 } \phi _ { n } / d x ^ { 4 } )$ by $m \Omega _ { n } { } ^ { z } \varphi _ { n }$ of Eq. $d$ to ob

$$
\sum _ { n = 1 } ^ { \infty } m \varphi _ { n } \ddot { q } _ { n } + \sum _ { n = 1 } ^ { \infty } m \Omega _ { n } { } ^ { 2 } ( 1 + i \alpha ) \varphi _ { n } q _ { n } = m a _ { z }
$$

Multiplying Eq. $e$ by $\varphi _ { k } d x$ and integrating over $x = 0$ to $l$ , and noting the orthogonality relationship of the normal modes,

$$
\int _ { 0 } ^ { l } \varphi _ { n } \varphi _ { k } m ~ d x = { \left\{ \begin{array} { l l } { 0 } & { { \mathrm { f o r ~ } } n \neq k } \\ { M } & { { \mathrm { f o r ~ } } n = k } \end{array} \right. }
$$

The result is

$$
\begin{array} { c } { { \displaystyle { \ddot { q } } _ { k } + ( 1 + i \alpha ) { \Omega _ { n } } ^ { 2 } q _ { k } = \frac { 1 } { M } \int _ { 0 } ^ { l } m a _ { z } \varphi _ { k } d x } } \\ { { = F \sin { \dot { \varphi } } t } } \end{array}
$$

where

$$
F = \frac { 2 } { M } \bigg ( \frac { C } { A } \bigg ) \omega _ { 0 } { } ^ { 2 } \sin { \theta } \cos { \theta } \int _ { 0 } ^ { l } ( x _ { 0 } + x ) \varphi _ { k } m \ d x
$$

The steady-state oscillation of the antenna is then established as

$$
q _ { k } = \frac { F \sin { ( \phi t + \epsilon _ { k } ) } } { \Omega _ { k } { ^ 2 } \sqrt { [ 1 - ( \dot { \phi } / \Omega _ { k } ) ^ { 2 } ] ^ { 2 } + \alpha ^ { 2 } } }
$$

To determine the energy disipated per cycle, westart with the strain energy

$$
\begin{array} { l }  \displaystyle { \mathcal { I } = \frac { 1 } { 2 } E I \int _ { 0 } ^ { \tau } ( \frac { d ^ { 2 } w } { d x ^ { \hat { \alpha } } } ) ^ { 2 } d x = \frac { E I } { 2 } ( q _ { 1 } ^ { 2 } \int _ { 0 } ^ { \tau } \varphi _ { 1 } ^ { \prime \prime 2 } d x + q _ { 2 } ^ { 2 } \int _ { 0 } ^ { l } \varphi _ { 2 } ^ { \prime \prime 2 } d x + 2 q _ { 1 } q _ { 2 } \int _ { 0 } ^ { l } \varphi _ { 1 } ^ { \prime \prime } { \varphi _ { 2 } } ^ { \prime } d x + \cdot \cdot \cdot } \end{array}
$$

Using only the first mode and noting that (see Sec. 7.6)

$$
\frac { \dot { \varphi } } { \Omega _ { 1 } } = \bigg ( 1 - \frac { C } { A } \bigg ) \frac { \omega _ { 0 } } { \Omega _ { 1 } } \cos \theta = R _ { 1 } \cos \theta
$$

the equation for the energy dissipated per cycle is

$$
\frac { \bar { z } I } { \bar { z } ^ { 2 } } \bigg ( 1 - \frac { C } { \cal A } \bigg ) \bigg ( \frac { C } { \cal A } \bigg ) ^ { 2 } \bigg ( \frac { \omega _ { 0 } } { \Omega _ { 1 } } \bigg ) ^ { 5 } \frac { \sin ^ { 2 } \theta \cos ^ { 3 } \theta } { ( 1 - { R _ { 1 } } ^ { 2 } \cos ^ { 2 } \theta ) ^ { 2 } + \alpha ^ { 2 } } \bigg ( \int _ { 0 } ^ { \bar { \iota } } ( x _ { 0 } + x ) \varphi _ { 1 } m d x \bigg ) ^ { 2 } \int _ { 0 } ^ { \bar { \iota } } \varphi ^ { \prime \prime } d x
$$

Equating this to Tof Eq.7.6-6,the rate of drift of the atitude angle can be expressed as

$$
\dot { \theta } = \frac { K \sin \theta \cos ^ { 2 } \theta } { ( 1 - \mathcal { R } _ { 1 } ^ { ~ 2 } \cos ^ { 2 } \theta ) ^ { 2 } + \alpha ^ { 2 } }
$$

where the many constants of the problem have been lumped into $\kappa$

![](images/a9d18907ae26d932d35c14ad08f585a713de087a4b653a6829ebc6d5991ce30c.jpg)  
Fig. 9.8-3. Resonance in attitude drift rate due to whip antennas.

This result should be compared to that of Example 7.6-1. Since $\theta$ generally starts from some small angle $\dot { \theta } _ { 0 }$ and increases for $C / A < 1$ , there is a possibility of resonance if $R _ { 1 }$ is greater than unity. The peak values, however,are expressible as

$$
\dot { \theta } = \frac { K } { \alpha ^ { 2 } } \sin \theta \cos ^ { 2 } \theta
$$

which is similar in form to Eq.fof Ex. 7.6-1,although the $K$ are different. A plot of the drift rate is shown in Fig. 9.8-3.

# 9.9 Nonholonomic Systems

The development of the previous section for the holonomic system, Eqs. 9.8-1 to 9.8-13, apply equally well to nonholonomic systems. The difference here is that for the nonholonomic system the $q _ { i }$ of Eq. 9.8-1 are not all independent. However, the requiremcnt for the independence of the $q _ { i }$ for the holonomic system was not imposed in the development of the previous section until the step between Eqs. 9.8-13 and 9.8-14 was required.

For the nonholonomic system, the $q _ { i }$ are restricted by the constraint equations of the form

$$
\begin{array} { l } { { a _ { 1 1 } d q _ { 1 } + a _ { 2 1 } d q _ { 2 } + \cdots a _ { n 1 } d q _ { n } + a _ { 0 1 } d t = 0 } } \\ { { \mathrm { ~ } } } \\ { { \cdot } } \\ { { \cdot } } \\ { { a _ { 1 m } d q _ { 1 } + a _ { 2 m } d q _ { 2 } + \cdots a _ { n m } d q _ { n } + a _ { 0 m } d t = 0 } } \end{array}
$$

which are nonintegrable. Holonomic constraints may also be present, but we willassume that they have been used to reduce the $q _ { i }$ to independent quantities, of which there will be $n - m$ ,where $m$ is the number of nonholonomic constraints.

We will assume for convenience that there are just two $m = 2$ ）nonholonomic constraints and write their variation,

$$
\begin{array} { r l } & { a _ { 1 1 } \delta q _ { 1 } + a _ { 2 1 } \delta q _ { 2 } + \cdots a _ { n 1 } \delta q _ { n } = 0 } \\ & { a _ { 1 2 } \delta q _ { 1 } + a _ { 2 2 } \delta q _ { 2 } + \cdots a _ { n 2 } \delta q _ { n } = 0 } \end{array}
$$

Since the variation is one of configuration, holding time constant, t does not enter into Eq. 9.9-2. Two of the $q _ { i }$ are now related by Eq. 9.9-2, leaving $n - 2$ of the $q _ { i }$ as independent quantities.

We will now multiply each of Eq. 9.9-2 by an undetermined multiplier λ and integrate between $t = 0$ and $t _ { 1 }$ as follows :

$$
\begin{array} { c } { { \displaystyle \sum _ { i = 1 } ^ { n } \int _ { 0 } ^ { t _ { 1 } } \lambda _ { 1 } a _ { i 1 } \delta q _ { i } d t = 0 } } \\ { { \displaystyle \sum _ { i = 1 } ^ { n } \int _ { 0 } ^ { t _ { 1 } } \lambda _ { 2 } a _ { i 2 } \delta q _ { i } d t = 0 } } \end{array}
$$

(Notethatthe λcouldbeafunctionoftimeas wellasconstants.) Including these terms in Eq. 9.8-13, we can write,

$$
\begin{array} { r } { \delta \int _ { 0 } ^ { t _ { 1 } } ( T + W ) d t = - \displaystyle \sum _ { i = 1 } ^ { n } \int _ { 0 } ^ { t _ { 1 } } \left( \frac { d } { d t } \frac { \partial T } { \partial { \dot { q } } _ { i } } - \frac { \partial T } { \partial q _ { i } } - Q _ { i } - \lambda _ { 1 } a _ { i 1 } - \lambda _ { 2 } a _ { i 2 } \right) \delta q _ { i } d t } \\ { = 0 \qquad ( 9 . 9 - } \end{array}
$$

Since $n - 2$ of the $\delta \boldsymbol { q } _ { i }$ are independent, we willseparate the aboveintegrals to

$$
\begin{array} { l } { { \displaystyle \sum _ { i = 1 } ^ { n - 2 } \int _ { 0 } ^ { t _ { 1 } } \left( \frac { d } { d t } \frac { \partial T } { \partial { \dot { q } } _ { i } } - \frac { \partial T } { \partial q _ { i } } - Q _ { i } - \lambda _ { 1 } a _ { i 1 } - \lambda _ { 2 } a _ { i 2 } \right) \delta q _ { i } d t } } \\ { { \displaystyle \qquad + \sum _ { n = 1 } ^ { n } \int _ { 0 } ^ { t _ { 1 } } \left( \frac { d } { d t } \frac { \partial T } { \partial { \dot { q } } _ { i } } - \frac { \partial T } { \partial q _ { i } } - Q _ { i } - \lambda _ { 1 } a _ { i 1 } - \lambda _ { 2 } a _ { i 2 } \right) \delta q _ { i } d t = 0 } } \end{array}
$$

where the two dqi of the last integral are fixed by the constraint equations and,therefore,arenotarbitrary.Wecan however,maketheintegrandofthe last integral zero by a proper choice of 𝜆1 and λz. Each of the integrand of the first integral can be shown to be zero by assuming one of the arbitrary Sq. to be nonzero and the remaining Sq to be al zero, repeating this procedure for each of the (n - 2) Sqi. We then arrive at n equations of the form,

$$
\frac { d } { d t } \frac { \partial T } { \partial \dot { q } _ { k } } - \frac { \partial T } { \partial q _ { k } } = Q _ { k } + \lambda _ { 1 } a _ { k 1 } + \lambda _ { 2 } a _ { k 2 }
$$

Since we have two additional unknowns 21 and 2 besides the n q, we needtwootherequations,whicharefurnishedbytheconstraintequations, Eq.9.9-1, writen in the form,

$$
\begin{array} { r } { a _ { 1 1 } \dot { q } _ { 1 } + a _ { 2 1 } \dot { q } _ { 2 } + \cdots a _ { n 1 } \dot { q } _ { n } + a _ { 0 1 } = 0 } \\ { a _ { 1 2 } \dot { q } _ { 1 } + a _ { 2 2 } \dot { q } _ { 2 } + \cdots a _ { n 2 } \dot { q } _ { n } + a _ { 0 2 } = 0 } \end{array}
$$

These $n + 2$ equations are then suffcient for the solution of the problem

In the development of this section, we have illustrated the method of Lagrange's undetermined multipliers, 2, which is not restricted to the nonholonomic system, and can be applied equally well to holonomic systems. Occasionally it is not convenient to reduce the variables of the holonomic system to independent quantities by the use of the constraint equations,in which case the Lagrange multiplier method can be used. In such a case, the Lagrange multiplier method will also provide a solution for the constraint forces, which are sometimes required.

# Example 9.9-l

A thin disk of radius $r$ rolls down an inclined plane of small angle $\propto$ with the horizontal. If the plane of the disk is always normal to the inclined plane, and capable of rotation about the normal, determine the $x , y$ motion of the disk.

Referring to Fig. 9.9-1, the coordinates of the problem are $\boldsymbol { \psi }$ ， $_ x$ and $\phi$ 、The equations for the kinetic and potential energies are,

$$
\begin{array} { l } { { T = \frac { 1 } { 2 } m [ ( r \phi ) ^ { 2 } + \frac { 1 } { 4 } ( r \psi ) ^ { 2 } + \frac { 1 } { 2 } ( r \phi ) ^ { 2 } ] } } \\ { { { } } } \\ { { U = - m g x \sin \alpha } } \end{array}
$$

and the constraint equation is

$$
r d \phi - \frac { d x } { \cos \psi } = 0
$$

The Lagrange equations are then,

$$
\begin{array} { r } { \displaystyle \frac { d } { d t } \bigg [ m \frac { r ^ { 2 } } { 4 } \dot { \psi } \bigg ] = 0 } \\ { - m g \sin \alpha + \frac { \lambda } { \cos \psi } = 0 } \\ { \displaystyle \frac { d } { d t } [ m ( \frac { 3 } { 2 } r ^ { 2 } ) \phi ] - r \lambda = 0 } \end{array}
$$

From $( d )$ ， $\dot { \psi }$ is a constant $n$ , and its integral is $\psi = \psi _ { 0 } + n t$ . Substituting for $\psi$ in $( e )$ ,the equation for $\lambda$ becomes

$$
\lambda = m g \sin \propto \cos \left( \psi _ { 0 } + n t \right)
$$

With $\lambda$ substituted into $( f ) ,$ its integral is

$$
\frac { 3 } { 2 } m r ^ { 2 } ( \not { \phi } - \not { \phi } _ { 0 } ) - \overleftarrow { m } { g } r \sin \alpha \Bigg [ \frac { 1 } { n } \sin \left( \psi _ { 0 } + n t \right) - \frac { 1 } { n } \sin \psi _ { 0 } \Bigg ] = 0
$$

![](images/4214669c1004554b019caeddc2768f9eb7c6839e268eef4540125101d7b11ecf.jpg)  
Fig. 9.9-l. Coordinates $y , x$ and $\phi$ are related by nonholonomic constraint.

The $x$ and $y$ displacements can be found from the integrals of

$$
\begin{array} { r } { d x = r \phi \cos \psi \ d t } \\ { d y = r \phi \sin \psi \ d t } \end{array}
$$

# 9.10 Lagrange's Equation for Impulsive Forces

During impact of one body on another,a very large force acts for a very short time. Such forces are said to be impulsive. As the time of contact diminishes to zero, the force tends to infinity； however, like the delta function, the time integral of the impulsive force is finite.

When an impulsive force acts on a body， the velocity of the body undergoes an instantaneous change over an infinitesimal change in displacement.Thusgeneralizedecities ${ \dot { q } } _ { i }$ will change instantaneously whereas generalized coordinates $q _ { i }$ will not. The system is nonconservative since energy is generally dissipated during impact.

In applying Lagrange's equation to impulsive force systems,weapproach it by a limiting process. Starting with the equation,

$$
\frac { d } { d t } \frac { \partial T } { \partial { \dot { q } } _ { i } } - \frac { \partial T } { \partial q _ { i } } = Q _ { i }
$$

we multiply by $d t$ and integrate over the impact time.

$$
\int _ { 0 } ^ { \epsilon } d \frac { \partial T } { \partial \dot { q } _ { i } } - \int _ { 0 } ^ { \epsilon } \frac { \partial T } { \partial q _ { i } } d t = \int _ { 0 } ^ { \epsilon } Q _ { i } d t
$$

The second integral contain terms assciated with the generalized coordinate $q _ { i }$ which do not change during the impact. Thus, in the limiting case when $\epsilon  0$ ,the second integral vanishes,and we obtain the relationship,

$$
\Delta \frac { \partial T } { \partial \dot { q } _ { i } } = \operatorname * { l i m } _ { \epsilon  0 } \int _ { 0 } ^ { \epsilon } Q _ { i } d t = \hat { Q } _ { i }
$$

This equation states that the change in the generalized momentum is equal to the generalized impulse.

# Example 9.10-1

Four equal bars, each of mass $m$ and length $2 a .$ ,lie on a smooth,horizontal floor,hinged together in the form of a rhombus, as shown in the sketch. If an

![](images/b035636f47bfc3eaf6ed2ea1adf2b9bb1c40d01b10f1060a33bc67f3d94b664a.jpg)  
Fig. 9.lo-l. Impulsively loaded structure.

impulsive force $\hat { F }$ Ib-sec. is applied at $A$ in the direction $C A$ ,determine the initial angular velocity of the bars.

Place coordinates $x , y$ with origin $o$ at the center of mass.

The $_ x$ and $y$ coordinates of the center $G$ of the bar are,

$$
x _ { G } = a \sin \theta \qquad y _ { G } = a \cos \theta
$$

and the velocity of the center of mass of the bars becomes

$$
{ \bf v } _ { G } = ( a \dot { \theta } \cos \theta ) { \bf i } + ( \dot { y } _ { 0 } \pm a \dot { \theta } \sin \theta ) { \bf j }
$$

where the minus sign applies to $A B$ and $A D$ and the plus sign to $C B$ and $C D$

The kinetic energy of the bars is

$$
\begin{array} { c } { { T = \displaystyle \frac { 1 } { 2 } 4 m \ v _ { G } { } ^ { 2 } + \frac { 1 } { 2 } \bigg ( 4 m \frac { a ^ { 2 } } { 3 } \bigg ) \dot { \theta } ^ { 2 } } } \\ { { = 2 m ( \dot { y _ { 0 } } ^ { 2 } + \frac { 4 } { 3 } a ^ { 2 } \dot { \theta } ^ { 2 } ) } } \end{array}
$$

and the change in the generalized momentum becomes

$$
\Delta \ \frac { \partial T } { \partial \dot { \theta } } = \textstyle \frac { 1 6 } { 3 } m a ^ { 2 } \dot { \theta }
$$

The generalized force $\hat { \boldsymbol { Q } }$ is found from the virtual work of the impulse. Due to virtual displacements $\delta y _ { 0 }$ and $\delta \theta$ , the point $A$ undergoes a displacement

$$
\delta ( y _ { 0 } + 2 a \cos \theta ) = \delta y _ { 0 } - 2 a \sin \theta \delta \theta
$$

and the virtual work of $\hat { F }$ is

$$
\delta W = \hat { F } ( \delta y _ { 0 } - 2 a \sin \theta \delta \theta )
$$

The generalized force due to $\delta \theta$ is then

$$
\hat { Q } _ { \theta } = - \hat { F } 2 a \sin \theta
$$

and, by substituting into Eq. 8.14-3, we obtain

and

$$
\begin{array} { c } { { \frac { 1 8 } { 3 } m a ^ { 2 } \dot { \theta } = - \hat { F } 2 a \sin \theta } } \\ { { { } } } \\ { { \dot { \theta } = - \displaystyle \frac { 3 \hat { F } \sin \theta } { 8 m a } } } \end{array}
$$

# PROBLEMS

1. A particle moving in space is defined by the spherical coordinates $r , \theta$ and $\varphi$ Determine the generalized forces associated with the spherical coordinates, andestablishthecomponentforcesintheadialmeridianandlaitude directions.

![](images/06e6f69c5d44f14e24ceb5b1b00adaab4c9a9a0302879f57662d54d5ea67bff3.jpg)  
Prob.1

2.A satellite moves in a plane orbit under the influence of an inverse square attraction. Derive the orbit equation from Lagrange’s formulation. Is there a cycliccodnatefortetemdfotdoit?

![](images/2aae9853b8f84de9b648a1960db7c2bc4cdec1dd1ab25a133ce28a68bffade9a.jpg)  
Prob. 2

3. A spherical pendulum of length $l$ is set up on the earth's surfaceat latitude λ, with the $z$ axis in theverticaldirection and $x$ axis pointing north. Show that the Lagrangian is

$$
{ \cal L } = \frac { m } { 2 } \biggl [ { \dot { x } } ^ { 2 } + { \dot { y } } ^ { 2 } + 2 ( x { \dot { y } } - { \dot { x } } y ) \Omega \sin { \lambda } - \frac { g } { l } ( x ^ { 2 } + y ^ { 2 } ) - 2 { \dot { y } } R \Omega \cos { \lambda } + 2 l { \dot { y } } \Omega \cos { \lambda } \biggr ] .
$$

where $\Omega$ is the rotation speed of the earth and $R =$ radius of earth.

4. Determine the Lagrangian for the symmetric top spinning about a fixed pivot on the floor. Establish the cyclic (ignorable) coordinates and write directly the resulting integrals.

5. For a system of $N$ particles, the kinetic energy can be written in the form

$$
T = \frac { 1 } { 2 } \sum _ { k = 1 } ^ { n } \sum _ { l = 1 } ^ { n } A _ { k l } \dot { q } _ { k } \dot { q } _ { l } + \sum _ { k = 1 } ^ { n } B _ { k } \dot { q } _ { k } + C
$$

where

$$
A _ { k l } = \sum _ { i = 1 } ^ { N } m _ { i } \frac { \partial r _ { i } } { \partial q _ { k } } \frac { \partial r _ { i } } { \partial q _ { l } } { } _ { } { } _ { } B _ { k } = \sum _ { i = 1 } ^ { N } m _ { i } \frac { \partial r _ { i } } { \partial t } \frac { \partial r _ { i } } { \partial q _ { k } } { } _ { } C = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { N } m _ { i } \left( \frac { \partial r _ { i } } { \partial t } \right) ^ { 2 }
$$

Prove that for a scleronomic conservative system,

$$
2 T = \sum _ { k = 1 } ^ { n } { \dot { q } } _ { k } { \frac { \partial L } { \partial { \dot { q } } _ { k } } }
$$

6. For a conservative system of $N$ particles, prove that the conservation of energy holds only if the time $\bar { \tau }$ does not appear explicitly in the Lagrangian, in which case,

$$
\frac { d E } { d t } = \frac { d } { d t } \bigg ( \sum _ { k = 1 } ^ { n } \dot { q } _ { k } \frac { \partial L } { \partial \dot { q } _ { k } } - L \bigg ) = 0
$$

7. Using the Lagrangian approach, deduce Eulers dynamical equations for an arbitrary rigid body subjected to moments about the body axes.

Hint: $\dot { T } = \Sigma _ { 2 } ( A \omega _ { x } { } ^ { 2 } + B \omega _ { y } { } ^ { 2 } + C \omega _ { z } { } ^ { 2 } )$ . Express the angular velocites in terms of Eulers angles. The generalized force can be determined by giving each of the Euler angles virtual displacement with the other two equal to zero.

8.A mass is suspended from a weightless spring of stiffness $k$ lb/in. Write Lagrange's equations and discuss the motion for small oscillations in the vertical plane.

![](images/4f16cfaee26326d317d4e9a9bfc5a2ee5be4eafd7fefd870a7cdbb4879e259bf.jpg)  
Prob.8

9. Using Lagrange's method, set up the equations for the motion of a bar suspended by a string and oscillating in a plane.

![](images/cec6f12ef6bc3816b60939236f1a805f0f8d0c3635c1f4024350e5f8a6a5bfb5.jpg)  
Prob.9

10. A uniform bar of mass m and length /is suspended from one end by a spring of stiffness $k$ Ib/in. The barcanswingfreelyonly inone vertical plane and the spring $_ x$ is constrained to move only in the vertical direction. Set up the Lagrange equations of motion.

![](images/48c37d044bb4fa596508a74fe351f20a843a0b7be7ae3490b970ce4bac852c11.jpg)  
Prob.10

11. A centrifugal pendulum of mass m and length r is attached to a flywheel of moment of inertia I. Show that the kinetic energy of the system is,

where

$$
\begin{array} { c } { { T = m r ^ { 2 } \displaystyle \biggl [ \frac { 1 } { 2 } \dot { \varphi } ^ { 2 } + \left( { \cal A } + \frac { { \cal R } } { r } \cos \varphi \right) \dot { \theta } ^ { 2 } + \left( 1 + \frac { { \cal R } } { r } \cos \varphi \right) \dot { \theta } \dot { \varphi } \biggr ] } } \\ { { { \cal A } = \displaystyle \frac { 1 } { 2 } \biggl ( \frac { { \cal I } } { m r ^ { 2 } } + \frac { { \cal R } ^ { 2 } } { r ^ { 2 } } + 1 \biggr ) } } \end{array}
$$

![](images/91ae33c54d5c9425d4b66be35dcca4fef5b1352b143fea7bd1da787ba614be6f.jpg)  
Prob. Il

12. A particle of mass $m$ slides without friction on a hoop of radius $r ,$ which is rotated with constant speed $\Omega$ about a vertical diameter. A single coordinate $\theta$ is sufficient to describe the position of $m$ ； however, we have a moving constraint. Compare the total energy of the system with that determined from $T + U = \dot { \theta } \dot { ( } \partial L / \partial \dot { \theta } ) - L$ and discuss this discrepancy.

![](images/73d97121790705434e477ec6ca7dbb72bd797d68e1b654af75ac6ba00f417b4a.jpg)  
Prob.12

13. A uniform bar of length 2l and mass $m$ is dropped from a height $h$ onto a horizontal floor. The bar descends without rotation and at an angle $\theta _ { 0 }$ with the floor. If the coefficient of restitution between the floor and bar is $e _ { i }$ determine the velocity of the center of the bar and its angular velocity immediately after impact.

![](images/fa638227e4cbd53589d6c180cc1b3dfab7509337550f328c85696e392dc742a4.jpg)  
Prob.13

14.In Prob. 13, determine the time elapsed after the first impact when the opposite side of the bar strikes the floor. What is the angleθwhen it strikes?   
15. A simplified two-dimensional version of a space craft in landing is shown in the sketch,where the two legs are restrained from rotation by a torsional spring of stiffness $K$ Ib-in./rad. If the legs strike the smooth inelastic plane with velocity $v$ ,determine the rotational velocity $\dot { \theta }$ immediately after impact. Assume $\dot { \theta } = 0$ before impact and the torsional spring to be exerting a moment $C _ { 0 }$ , holding the legs against the stop.

![](images/dc047232f51b139316b29ad8ec73b1525970c5dfbd1a880ba7ce1bf33591de97.jpg)  
Prob.15

16. For the system shown, show that, if one incorrectly takes $y$ and θ as independent generalized coordinates $q _ { 1 }$ and $q _ { 2 }$ ,then the resulting two Lagrange equations are also incorrect. Demonstrate the use of the Lagrangian multiplier by establishing the correct equation, using $y$ and θ,and a constraint equation.

![](images/abbec58f08a5596156a8c9fe2a611fab45d83a6e6a62d4897dc0c5f275e55c8f.jpg)  
Prob.16

17. Two uniform bars of mass m and length l are hinged as shown,and lie on a smooth horizontal plane. If an impulsive force strikes the bar normally at oneend,determine theangularvelocities ofthe twobars and the velocityof the hinge.

![](images/b879beba839903e44668cf1f751f43109137cfea2389ce64eedd5e1e7d7cf6f8.jpg)  
Prob.17

18. Four hinged bars, each of length l and mass $m$ ,fall in translation and strike a horizontal inelastic ground. Taking $y$ and $\theta$ as generalized coordinates,find the motion immediately after impact.

![](images/4a9dca68a6b9dac8622ac47fe8cdf66cb01ceadf4aa5388f7baca436496495c7.jpg)  
Prob.18

19. A rigid pendulum of length land mass $m$ can swing around the horizontal axis AA which is mounted in a frame that can rotate freely around the vertical axis $B B$ The moment of inertia of the frame and horizontal axle about the vertical axis is $I ,$ At the instant $t = 0$ , the pendulum in the vertical position is given an initial velocity $v _ { 0 }$ ,and the frame is given an initial angular velocity $\omega _ { 0 }$ .(a) Set up the equations of motion, noting that the momentum and energy are conserved; ${ \bar { ( b ) } }$ simplify the results of $\bar { ( a ) }$ by assuming small angles, sin $\bar { \theta _ { \mathbf { \lambda } } } = \theta$ ,and cos $\theta = 1 - \textstyle \frac { 1 } { 2 } \theta ^ { 2 }$ ； (c) discuss the motion of the simplified system for ${ \omega _ { 0 } } ^ { 2 } < g / l$ and ${ \omega _ { 0 } } ^ { 2 } > g / l .$

![](images/b6017e59da16dfc98d85425363296552550abb2be3596b29cedb44287b602635.jpg)  
Prob.19

20. A spherical pendulum of length $\mathbf { \xi } _ { l }$ and mass $m$ is suspended from end 0 of a horizontal arm of length $e$ that rotates with constant angular velocity $\omega$ about a fixed vertical axis $\breve { C }$ as shown in the sketch.Assuming small oscillatory amplitudes and a damping equal to $\zeta \times$ critical damping in a plane pendulum oscillation, show that the equations of motion of the pendulum bob are

![](images/4e1ced2ce933433be7cf19c8d09f3412fb9c481b64ad13c576c2894a4afc7c25.jpg)  
Prob. 20

$$
\begin{array} { l } { { \ddot { x } + 2 \zeta p \dot { x } + ( p ^ { 2 } - \omega ^ { 2 } ) x - 2 \omega \dot { y } = e \omega ^ { 2 } } } \\ { { \ddot { y } + 2 \zeta p \dot { y } + ( p ^ { 2 } - \omega ^ { 2 } ) y + 2 \omega \dot { x } = 0 } } \end{array}
$$

where $p ^ { 2 } = g / l$

21. In Prob. 20, let $z = x - x _ { 0 } + i y$ and $x _ { 0 } = e \omega ^ { 2 } / ( p ^ { 2 } - \omega ^ { 2 } )$ ,where $x _ { 0 }$ denotes the position of static equilibrium (not necessarily stable), and show that the two equations can be reduced to a single homogeneous equation in $\boldsymbol { \mathscr { z } }$ with a general solution

$$
z = A e \left( - \xi - i \right) ( p + \omega ) t + B e ^ { \left( - \zeta + i \right) \left( p - \omega \right) t } \quad \xi < < 1
$$

where terms of order $\zeta ^ { 2 }$ have been neglected. Discuss the criteria for stability of small oscillations.

22. A one-wheel trailer shown in the sketch is towed with velocity $v$ .If the trailer hitch has a lateral stiffness $k$ , and the radius of gyration of the trailer about the center of mass $G$ is $\rho$ , write the two equations of motion and the constraint equation for no lateral sliding of the trailer wheel. Determine the stability of the trailer for small $\theta$ (i.e.,roots of the characteristic equation must not have positive real parts).

23. Carry out the solution for $_ x$ and $y$ in Example 9.9-1. Show that, if the initial conditions are zero, the curve traced out will be a cycloid.

24. The spin axis of a space station with $C = k A$ (for a thin disk $k = 2$ is initially pointing to the north star. It is desired to change the direction of the spin axis by $\theta ^ { \circ }$ in a specified direction without inducinga precession about thenew direction. This can be done by two properly timed impulsive blasts from a single rocket engine on the rim and pointing parallel to the spin axis. If the initial angular momentum of the station is $h = C \omega _ { 0 }$ ,determine the timingof thefirst and secondblastsinrelationtothedesired directionchange and their magnitude.

![](images/9400540dbb21e75506e6d2dc37351e49e7bbd832d22e17a947542dfd5f6bcec6.jpg)  
Prob.22

![](images/d63d2bf93f4525c39e156bae3e7e47864036d62b2e78df2a11b6065642fd5460.jpg)  
Prob.24

# 9.ll Lagrange's Equations for Rotating Coordinates

In the dynamic analysis of flexible missiles,it is convenient to use a set of coordinates moving with the missile. The missile can be considered a system of particles whose position relative to the moving axes can be defined by generalized coordinates $q _ { i } ,$

In setting up the equations of motion, it is often simpler to start from the kinetic and potential energies of the system, using Lagrange's equation. For rotating coordinates, these equations differ from the usual Lagrange equations for fixed coordinates; however, since their rigorous derivation is lengthy,\* we will only present the equations and justify each term.

The position of the origin relative to the system of particles and the orientation of the axes are arbitrary choices which will influence the final form of the equations of motion. We will place the moving axes as shown in Fig. 9.11-1, with the origin at the center of mass and the $x$ axis coinciding with the missile longitudinal axis in the undeformed state. Aside from the coordinates $q _ { i }$ for the relative motion, the coordinate axes in plane motion will have three degrees of freedom, $x _ { 0 }$ ， $y _ { 0 }$ ,and $\theta$ ,which can be varied independently. The Lagrange equations can then be written as,

$$
\frac { d } { d t } \frac { \partial T } { \partial \dot { x } _ { 0 } } - \dot { \theta } \frac { \partial T } { \partial \dot { y } _ { 0 } } = \sum F _ { x }
$$

$$
\frac { d } { d t } \frac { \partial T } { \partial \dot { y } _ { 0 } } + \dot { \theta } \frac { \partial T } { \partial \dot { x } _ { 0 } } = \sum F _ { v }
$$

$$
\frac { d } { d t } \frac { \partial T } { \partial \dot { \theta } } + \dot { x } _ { 0 } \frac { \partial T } { \partial \dot { y } _ { 0 } } - \dot { y } _ { 0 } \frac { \partial T } { \partial \dot { x } _ { 0 } } = \Sigma M _ { 0 }
$$

The equation for $q _ { i }$ remain unaltered in form.

In accounting for the terms in these equations, we recognize $\partial T / \partial { \dot { x } } _ { 0 }$ and $\partial T / \partial { \dot { y } } _ { 0 }$ as the generalized momenta,and $\partial T / \partial \dot { \theta }$ as the generalized angular momentum. We will then represent the linear momentum by

$$
\mathbf { p } = { \frac { \partial T } { \partial { \dot { x } } _ { 0 } } } \mathbf { i } + { \frac { \partial T } { \partial { \dot { y } } _ { 0 } } } \mathbf { j }
$$

As the force equation is the rate of change of the linear momentum,

$$
\mathbf { F } = \left[ { \frac { d \mathbf { p } } { d t } } \right] + { \boldsymbol { \omega } } \times \mathbf { p }
$$

the terms of Eq. 9.11-1 and 9.11-2 are immediately accounted for.

\*Thomson, W.T.“Lagrange'sEquations forMoving Coordinates," SpaceTechnologyLaboratoriesReportNo.EM9-15TR5900068,LosAngeles(July1959).

The terms of Eq. 9.11-3 can be identified from Eq. 7.11-3, which can be written as

$$
\begin{array} { r } { \mathbf { M } _ { 0 } = \dot { \mathbf { h } } _ { 0 } + \dot { \mathbf { R } } _ { 0 } \times \sum m _ { i } \dot { \mathbf { r } } _ { i } } \end{array}
$$

The term ∂T/d0 is the angular momentum ho,and the remaining two terms are equal to $\begin{array} { r } { \dot { \bf R } _ { 0 } \times \sum m _ { i } \dot { \bf r } _ { i } , } \end{array}$ where $\dot { \bf R } _ { 0 } = \dot { x } _ { 0 } { \bf i } + \dot { y } _ { 0 } { \bf j } .$

![](images/58bdc2b52597186badb9f17fc3158ab36d96bb8b6e503ac53c8abdb8bcb68304.jpg)  
Fig. 9.ll-l. Rotating coordinate system.

# 9.12 Missile Dynamic Analysis

Misiles are, in general, flexible structures, weight being of primary concern. Vibrational problems are thus likely to plague their performance, and it is in general necessary to make a dynamical analysis of a vehicle in flight. Such an analysis consists of formulating the equations of motion in all their details to account for the interaction of the bending of the flexible missile with the rigid body motion, the reaction of the swiveling engine, the sloshing of the propellant, the excitation of the aerodynamic forces and gusts, and the coupling of the servosystem controlling the stability of its attitude. The equations of motion must then be linearized and programmed for machine computation, i.e., the missile is theoretically flown on the high-speed computer.

It is evident that a detailed formulation of all the factors pertinent to the dynamical analysis is beyond the scope of this text. It is possible, however, to discuss a greatly simplified problem which will serve to illustrate the dynamical techniques employed in the general analysis.

We will consider here the problem of a flexible missile of constant mass, where the propellant is treated as a solid to avoid the complications of sloshing. The engine will be considered to be gimballed, and the motion will be restrictedtotheverticalplaneofthetrajectorysshownin Fig. 9.12-1. The coupling of the servosystem, actuating the gimballed engine attitude, will also be neglected.

![](images/34523132466db80346e49fd5904b466870ec8041c60ff1ccc1c274943d52d440.jpg)  
Fig. 9.12-l. Geometry of flexible missile and coordinates.

# Coordinate system

The choice of the coordinate system is an important one which depends on the vibrational data available. The missile can be treated as a free-free beam,and its normal modes, computed with engine locked on, will be assumed to be available from a previous analysis. Such modes are orthogonal and possess the property of zero linear and angular momenta about the missile vibrational axis (axis coinciding with the undeformed missile with engine locked on,from which vibrational displacements are measured) passing through its center of mass. In actual analysis, the shear deformation and rotatory inertia terms are accounted for in the normal mode analysis； however,for simplicity of discussion we will omit these terms.

The $x$ ， $y$ coordinate axes willbe chosen with the origin at the center of mass, the $x$ axis coinciding with the missle vibrational axis. It is evident, then, that the misile longitudinal axis will undergo an additional displacement due to the rotation of the engine. The nature of this additional displacement is readily understood by considering a rigid missile whose engine section is given a rotational velocity $\delta$ by an internal hinge moment, as shown in Fig. 9.12-2. If $m$ and $m _ { e }$ are the total mass and the engine mass respectively, the maintenance of zero linear momentum (since there is no external force) can be expressed by the equation,

![](images/0563dd72e02b1b5de3b7c9ec6086c3cac1a63dc03226d2278fbfb24fc6f3a0c0.jpg)  
Fig. 9.I2-2. Conservation of linear and angular momenta.

$$
\int _ { - l _ { 1 } } ^ { l _ { 2 } } \dot { y } \ d m - \dot { \delta } \int _ { o } ^ { b } z \ d m = 0
$$

Letting c be a point on the missile longitudinal axis coinciding with the center of mass of the missile in the undeformed state, and $e$ be the center

of mass of the engine, or section aft of the hinge, the above equation becomes,

$$
{ \dot { y } } _ { c } = { \frac { m _ { e } z _ { e } } { m } } { \dot { \delta } }
$$

It is evident then that point $c$ is displaced laterally by the amount

$$
y _ { c } = \frac { m _ { e } z _ { e } } { m } \delta = C _ { 1 } \delta
$$

The small displacement of $c$ in the $x$ direction due to $\delta$ is of second order and will be neglected.

In addition to the lateral displacement $y _ { c }$ , there will be rotations of the sections forward and aft of the hinge to maintain zero angular momentum about the mass center of the missile. Letting the angular velocity of the missile forward of the hinge be $\dot { \theta } _ { f }$ ， $I _ { 0 }$ the mass moments of inertia of the entire missile about the center of mass, and $I _ { h }$ the mass moment of inertia of the engine about the hinge, the angular momentum equation is

$$
\int _ { - l _ { 1 } } ^ { l _ { 2 } } \dot { y } x d m - \dot { \delta } \int _ { o } ^ { b } z x d m = 0
$$

Since $\dot { y } = \dot { y } _ { c } - x \dot { \theta } _ { f }$ and $x = - ( l _ { h } + z )$ and $\int _ { - l _ { 1 } } ^ { l _ { 2 } } x \ d m = 0$ ，the equation reduces to

$$
I _ { 0 } \dot { \theta } _ { f } = ( I _ { h } + m _ { e } l _ { h } z _ { e } ) \dot { \delta }
$$

from which

$$
\theta _ { f } = \frac { I _ { h } + m _ { e } l _ { h } z _ { e } } { I _ { 0 } } \delta = C _ { 2 } \delta
$$

These displacements can be considered to be the rigid missile displacements due to hinge rotation $\delta$ , which must be added to the vibrational displacements to obtain the total displacement of the flexible missile center line. They are, therefore, equivalent to translating and rotating the missile vibrational axis by $y _ { c }$ and $\theta _ { f } ,$ andthe total lateral displacement y of the flexible center line from the moving coordinate axis $_ x$ is, at point $_ { x }$

$$
y = ( C _ { 1 } - C _ { 2 } x ) \delta + \textstyle \sum _ { i } q _ { i } ( t ) \phi _ { i } ( x )
$$

where the vibrational displacement is represented by the sum of the normal modes $\phi _ { i } ( x )$ multiplied by the generalized coordinate $q _ { i } ( t )$ associated with the mode.

With the displacement relative to the coordinate system established, we next examine the motion of the coordinate axes themselves. The $_ x$ axis, which coincides with the missile vibrational axis or the missile longitudinal axis with δ = O, makes an angle θ with the vertical, as shown in Fig. 9.12-1. The rate of rotation of the coordinate axes is then $\omega = { \dot { \theta } }$

The origin of the coordinate axes, coinciding with the center of mass at all times, has a velocity vo tangent to the trajectory. The angle α between $\mathbf { v } _ { 0 }$ and the $_ x$ axis is the angle of attack of the missile's longitudinal axis (the local angle of attack will differ from α by dy/dx). Due to the changing direction of the trajectory tangent, the acceleration of the origin will be $\dot { v } _ { 0 }$ parallel to $\mathbf { v } _ { 0 }$ and $v _ { 0 } \dot { \beta }$ perpendicular to $\mathbf { v } _ { 0 }$ where $\beta$ is the angle made by $\mathbf { v } _ { 0 }$ and the vertical.

# Equations of motion

With the coordinate system defined in the foregoing, the equations of motion can be formulated by determining the kinetic and potential energies of the missile to be substituted into Lagrange's equation,taking note of the fact that the coordinates are rotating (see Sec. 9.11).

The velocity of a point ${ \bf r } = x { \bf i } + y ,$ j in the rotating coordinate system is

$$
\mathbf { v } = \mathbf { v } _ { 0 } + [ \mathbf { v } ] + { \boldsymbol { \omega } } \times \mathbf { r }
$$

For any point $x , y$ forward of the hinge $h _ { i }$ the $_ x$ and $y$ components are

$$
\begin{array} { l } { { v _ { x } = \dot { x } _ { 0 } - y \dot { \theta } } } \\ { { v _ { y } = \dot { y } _ { 0 } + \dot { y } + x \dot { \theta } } } \end{array}
$$

(The relative velocity $\dot { x }$ of a point on the missile is of second order compared to $\dot { y }$ and is, therefore, neglected.) The velocity of a point aft of the hinge can be found from the above equations by replacing y by $y - z \delta$ ·

In writing the kinetic energy equation of the missile with the swiveling engine, we need the squares of the velocity as follows:

Forward of the hinge

$$
v ^ { 2 } = ( { \dot { x } } _ { 0 } - y { \dot { \theta } } ) ^ { 2 } + ( { \dot { y } } _ { 0 } + { \dot { y } } + x { \dot { \theta } } ) ^ { 2 }
$$

Aft of the hinge

$$
\begin{array} { c } { { v ^ { 2 } = [ ( \dot { x } _ { 0 } - y \dot { \theta } ) + z \dot { \theta } \delta ] ^ { 2 } + [ ( \dot { y } _ { 0 } + \dot { y } + x \dot { \theta } ) - z \dot { \delta } ] ^ { 2 } } } \\ { { = ( \dot { x } _ { 0 } - y \dot { \theta } ) ^ { 2 } + ( \dot { y } _ { 0 } + \dot { y } + x \dot { \theta } ) ^ { 2 } } } \\ { { + ~ 2 ( \dot { x } _ { 0 } - y \dot { \theta } ) z \dot { \theta } \delta + ( z \dot { \theta } \delta ) ^ { 2 } - 2 ( \dot { y } _ { 0 } + \dot { y } + x \dot { \theta } ) z \delta + ( z \dot { \delta } ) ^ { 2 } } } \end{array}
$$

Thus part of $v ^ { 2 }$ aft of the hinge has the same form as that forward of the hinge, which enables Ttobe writen in the form T=T+T,where the quantity $\delta$ appears only in $T _ { \delta }$

$$
\begin{array} { l } { { \displaystyle T _ { 0 } = \frac { 1 } { 2 } \int _ { - l _ { 1 } } ^ { l _ { 2 } } [ ( \dot { x } _ { 0 } - y \dot { \theta } ) ^ { 2 } + ( \dot { y } _ { 0 } + \dot { y } + x \dot { \theta } ) ^ { 2 } ] m ( x ) d x \ ~ ( 9 . 1 2 - 1 0 ) , } } \\ { { \displaystyle T _ { \delta } = \frac { 1 } { 2 } \int _ { o } ^ { b } [ 2 ( \dot { x } _ { 0 } - y \dot { \theta } ) z \dot { \theta } \delta + z ^ { 2 } \delta ^ { 2 } \dot { \theta } ^ { 2 } - 2 ( \dot { y } _ { 0 } + \dot { y } + x \dot { \theta } ) z \dot { \delta } + z ^ { 2 } \dot { \delta } ^ { 2 } ] m ( z ) d z } } \end{array}
$$

In these equations the generalized coordinates are $x _ { 0 }$ ， $y _ { 0 }$ ，0， $\delta$ ,and $q _ { i } ,$ and it must be remembered that $y$ is related to $\delta$ and $q _ { i }$ through Eq. 9.12-6.

The equations of motion relating to the generalized coordinates $x _ { 0 }$ ， $y _ { 0 }$ ， and $\theta$ can be determined from Lagrange's equations, Eqs. 9.11-1, 9.11-2, and 9.11-3, however, since the linear and angular momenta relative to the coordinate system are zero, the sums of the external forces and moments must equal the rate of change of the linear and angular momenta of the rigid missile, which are related to the linear and angular accelerations of the $x , \ y$ coordinate system with origin at the center of mass. These equations can therefore be written as

$$
\begin{array} { c } { { m a _ { 0 x } = - m g \cos \theta + F _ { e } + D ^ { * } } } \\ { { \ } } \\ { { m a _ { 0 y } = m g \sin \theta + F _ { e } ( \delta + y _ { h } ^ { \prime } ) - L ^ { * } } } \\ { { \ } } \\ { { I \ddot { \theta } = - F _ { e } ( \delta + y _ { h } ^ { \prime } ) l _ { h } - F _ { e } y _ { h } + { M _ { 0 } } ^ { * } } } \end{array}
$$

where $F _ { e }$ is the engine thrust, $D ^ { * } , L ^ { * }$ ,and $M _ { 0 } { ^ * }$ are the drag and lift com-ponents of the aerodynamic force and its moment about 0, $\boldsymbol { y _ { h } } ^ { \prime } = ( d \boldsymbol { y } / d \boldsymbol { x } ) _ { h }$ and $a _ { 0 x }$ and $a _ { 0 y }$ represent the acceleration of the center of mass O, which is

$$
\begin{array} { r l } & { a _ { 0 x } = \ddot { x } _ { 0 } - \dot { y } _ { 0 } \dot { \theta } = \dot { v } _ { 0 } \cos \propto - v _ { 0 } \dot { \beta } \sin \alpha } \\ & { a _ { 0 y } = \ddot { y } _ { 0 } + \dot { x } _ { 0 } \dot { \theta } = \dot { v } _ { 0 } \sin \alpha + v _ { 0 } \dot { \beta } \cos \alpha } \end{array}
$$

To demonstrate that these equations can also be determined from Lagrange's equations for rotating coordinates, the first of the above equation,for the sum of the forces in the $x$ direction, willbederived rom Eq.9.11-1.Dierentiating the inetic energy, we have,

$$
\begin{array} { l } { \displaystyle \frac { \partial T } { \partial \dot { x } _ { 0 } } = \int _ { - l _ { 1 } } ^ { l _ { 2 } } ( \dot { x } _ { 0 } - y \dot { \theta } ) m ( x ) d x + \dot { \theta } \delta \int _ { o } ^ { b } z m ( z ) d z } \\ { \displaystyle \frac { \partial T } { \partial \dot { y } _ { 0 } } = \int _ { - l _ { 1 } } ^ { l _ { 2 } } ( \dot { y } _ { 0 } + \dot { y } + x \dot { \theta } ) m ( x ) d x - \dot { \delta } \int _ { o } ^ { b } z m ( z ) d z } \end{array}
$$

Substituting into equation

$$
\frac { d } { d t } \frac { \partial T } { \partial \dot { x } _ { 0 } } - \dot { \theta } \frac { \partial T } { \partial \dot { y } _ { 0 } } = \sum F _ { x }
$$

we obtain

$$
\begin{array} { c } { { { \displaystyle { \int _ { - l _ { 1 } } ^ { l _ { 2 } } } [ ( \ddot { x } _ { 0 } - y \ddot { \theta } - \dot { y } \dot { \theta } ) - \dot { \theta } ( \dot { y } _ { 0 } + \dot { y } + x \dot { \theta } ) ] m ( x ) ~ d x } } } \\ { { + ~ ( 2 \dot { \theta } \dot { \delta } + \ddot { \theta } \delta ) { \displaystyle { \int _ { o } ^ { b } } z m ( z ) ~ d z } = \sum { F _ { x } } } } \end{array}
$$

This equation can be rearranged as follows:

$$
\begin{array} { l } { { m ( \ddot { x } _ { 0 } - \dot { \theta } \dot { y } _ { 0 } ) - 2 \dot { \theta } \biggl [ \int _ { - l _ { 1 } } ^ { l _ { 2 } } \dot { y } m ( x ) d x - \dot { \delta } \int _ { o } ^ { b } z m ( z ) d z \biggr ] } } \\ { { - \ddot { \theta } \biggl [ \int _ { - l _ { 1 } } ^ { l _ { 2 } } y m ( x ) d x - \delta \int _ { o } ^ { b } z m ( z ) d z \biggr ] } } \\ { { - \dot { \theta } ^ { 2 } \int _ { - l _ { 1 } } ^ { l _ { 2 } } x m ( x ) d x = \sum F _ { x } } } \end{array}
$$

Since the second and third terms on the left side of this equation are the linear momentum relative to the coordinates, or the condition for the $_ x$ axis passing through the center of mass (see Eq. 9.12-4), they are zero. The term $\dot { \theta } ^ { 2 }$ is also a negligibly small term. We have, therefore, demonstrated the use of the Lagrange's equation for rotating coordinates.

For the beam equation relating to the generalized coordinate $q _ { i }$ and the engine rotation equation relating to $\delta$ ， the usual form of Lagrange's equation applies. We need, however, the equation for the potential or strain energy due to bending, which is,

$$
U = { \frac { 1 } { 2 } } \int _ { - l _ { 1 } } ^ { l _ { 2 } } E I _ { A } \left( { \frac { \partial ^ { 2 } y } { \partial x ^ { 2 } } } \right) ^ { 2 } d x
$$

From Eq. 9.12-6 the curvature is

$$
\frac { \partial ^ { 2 } y } { \partial x ^ { 2 } } = \sum _ { i } q _ { i } { \varphi _ { i } } ^ { \prime }
$$

where the primes stand for differentiation with respect to $_ { x }$ Substituting into $U$ and making use of the orthogonality relation,

$$
\int _ { - l _ { 1 } } ^ { l _ { 2 } } E I _ { A } { \varphi _ { i } } ^ { \prime \prime } { \varphi _ { j } } ^ { \prime \prime } d x = \left\{ { 0 \qquad } \right. \qquad { \mathrm { f o r ~ } } j \neq i
$$

The equation for the strain energy becomes,

$$
U = \frac { 1 } { 2 } m \sum _ { i } \omega _ { i } { ^ 2 q _ { i } } ^ { 2 }
$$

The various partial derivatives needed for Lagrange's equation are:

$$
\begin{array} { l } { \displaystyle \frac { \partial T } { \partial \dot { q } _ { i } } = \int _ { - l _ { 1 } } ^ { l _ { 2 } } ( \dot { y } _ { 0 } + \dot { y } + x \dot { \theta } ) \frac { \partial \dot { y } } { \partial \dot { q } _ { i } } m ( x ) d x - \dot { \delta } \int _ { 0 } ^ { b } \frac { \partial \dot { y } } { \partial \dot { q } _ { i } } z m ( z ) d z } \\ { \displaystyle \frac { \partial T } { \partial q _ { i } } = - \dot { \theta } \int _ { - l _ { 1 } } ^ { l _ { 2 } } ( \dot { x } _ { 0 } - y \dot { \theta } ) \frac { \partial y } { \partial q _ { i } } m ( x ) d x - \dot { \theta } ^ { 2 } \delta \int _ { 0 } ^ { b } \frac { \partial y } { \partial q _ { i } } z m ( z ) d z } \\ { \displaystyle \frac { \partial U } { \partial q _ { i } } = m \omega _ { i } ^ { 2 } q _ { i } } \end{array}
$$

We note here that $\dot { \theta } ^ { 2 }$ is a very small quantity, and terms multiplied by it can be neglected. Substituting for y from Eq. 9.12-6, taking into account the orthogonality condition, and noting that the linear and angular momenta of the vibration modes are zero,

$$
\int _ { - l _ { 1 } } ^ { l _ { 2 } } \varphi _ { i } \ : m ( x ) \ : d x = \int _ { - l _ { 1 } } ^ { l _ { 2 } } x \varphi _ { i } \ : m ( x ) \ : d x = 0
$$

we arrive at the result,

$$
\begin{array} { l } { { m ( \ddot { q } _ { i } + \omega _ { i } { } ^ { 2 } q _ { i } ) - \displaystyle \ddot { \delta } \int _ { 0 } ^ { b } \varphi _ { i } z d m } } \\ { { \mathrm { ~ } = - \displaystyle \int _ { - l _ { 1 } } ^ { l _ { 2 } } L ^ { * } \varphi _ { i } d x + F _ { e } ( \delta + y _ { h } ^ { \prime } ) \varphi _ { i } ( - l _ { h } ) } } \end{array}
$$

where the right side of the equation is established from the generalized force

$$
Q _ { q i } = \int \bar { F } \frac { \delta y } { \delta q _ { i } } d x = \int \bar { F } \frac { \partial y } { \partial q _ { i } } d x
$$

In a similar manner, the engine rotation equation is determined from

$$
\frac { d } { d t } \frac { \partial T } { \partial \dot { \delta } } - \frac { \partial T } { \partial \delta } + \frac { \partial U } { \partial \delta } = Q _ { \delta }
$$

which gives

$$
\begin{array} { r l } & { [ I _ { h } - C _ { 1 } m _ { e } z _ { e } - C _ { 2 } ( I _ { h } + m _ { e } l _ { h } z _ { e } ) ] \ddot { \delta } } \\ & { \qquad + m _ { e } z _ { e } ( \ddot { x } _ { 0 } - \dot { \theta } \dot { y } _ { 0 } + g \cos \theta ) ( \delta + y _ { h } { ' } ) + ( I _ { h } + m _ { e } l _ { h } z _ { e } ) \ddot { \theta } } \\ & { \qquad - m _ { e } z _ { e } ( \ddot { y } _ { 0 } + \dot { \theta } \dot { x } _ { 0 } ) - \sum _ { i } \ddot { q } _ { i } \biggl [ \int _ { 0 } ^ { \delta } \varphi _ { i } z m ( z ) \dot { d z } \biggr ] } \\ & { \qquad = M _ { A } ( \delta _ { A } - \delta ) - M _ { D } \dot { \delta } - M _ { \delta } \delta } \end{array}
$$

where the generalized force $Q _ { \delta } = M _ { \scriptscriptstyle \perp } ( \delta _ { \scriptscriptstyle \perp } - \delta ) - M _ { D } \delta - M _ { \delta } \delta$ is associated with $M _ { \delta } ,$ the spring moment per unit angle of the hinge when locked, $M _ { D }$ with the damping moment of the hinge, $M _ { _ { d } }$ with the engine actuator moment, and $\delta _ { _ { \mathcal { A } } }$ with the engine actuator position called by the autopilot. The autopilot actuating the engine attitude $\delta$ operates from signals generated by the rate gyros in the missile in such a way that the missile motion at the position of the rate gyro, which depends on all of the generalized coordinates, is coupled to the previous equation through the engine attitude $\delta$

# PROBLEMS

1. Assume that the mass of a portion of the missile is represented by a Iumped mass $m _ { j }$ mounted on a spring of stiffness $k$ against lateral motion $\zeta _ { j }$ from the center line at $x _ { j }$ Derive the equationfor the additional kinetic energy of the missile due to $\zeta _ { j }$

2. Derive Eq. 9.12-13 by the use of Lagrange's equation,

$$
\frac { d } { d t } \frac { \partial T } { \partial \dot { y } _ { 0 } } + \dot { \theta } \frac { \partial T } { \partial \dot { x } _ { 0 } } = \sum F _ { y }
$$

3. Derive Eq. 9.12-14 by the use of Lagrange's equation,

$$
\frac { d } { d t } \frac { \partial T } { \partial \dot { \theta } } + \dot { x } _ { 0 } \frac { \partial T } { \partial \dot { y } _ { 0 } } - \dot { y } _ { 0 } \frac { \partial T } { \partial \dot { x } _ { 0 } } = \sum M _ { 0 }
$$

4. Prove Eqs. 9.12-24 and 9.12-25.

5. Derive Eq. 9.12-30 for the engine rotation.

6. An elastic uniform bar of mass $m$ and length $l$ is supported from its upper end by a smooth pin. A constant force $P$ is suddenly applied normal to the bar at its mid-length. Using generalized coordinates $q _ { i } ,$ and three arbitrary modes,

$$
\varphi _ { 1 } = \frac { x } { l } \qquad \varphi _ { 2 } = \sin \frac { \pi x } { l } \qquad \varphi _ { 3 } = \sin \frac { 2 \pi x } { l }
$$

determine the equation of motion, the natural frequencies,and the mode shapes.

7. It is proposed to determine the natural frequencies of the two span beams of unequal length by assuming the deflection to be expressible by the equation,

$$
\begin{array} { r } { y = \sum _ { i } q _ { i } \varphi _ { i } ( x ) } \end{array}
$$

where

$$
\varphi _ { \ i } ( x ) = { \sqrt { 2 } } \sin { \frac { i \pi x } { l } }
$$

$$
\omega _ { i } = ( i \pi ) ^ { 2 } \sqrt { \frac { E I } { m l ^ { 4 } } }
$$

![](images/c917348300c1a6e849aa2b86faa4191147346a819e48859582588aa24fa70667.jpg)  
Prob.7

Show that the constraint equation $\sum _ { i } q _ { i } \varphi _ { i } ( c ) = 0$ , must be imposed and that the equation for the natural frequencies is,

$$
\frac { { \varphi _ { 1 } } ^ { 2 } ( c ) } { \omega _ { 1 } ^ { 2 } - \omega ^ { 2 } } + \frac { { \varphi _ { 2 } } ^ { 2 } ( c ) } { 1 6 \omega _ { 1 } ^ { 2 } - \omega ^ { 2 } } + \frac { { \varphi _ { 3 } } ^ { 2 } ( c ) } { 8 1 \omega _ { 1 } ^ { 2 } - \omega ^ { 2 } } = 0
$$

# General References

1. Davis,L.,D.Follin,and L.Blitzer,Exterior Ballstics of Rockets,D.VanNsta, Princeton, N. J. (1958).   
2. Deimel,R.F.,Mechanics of the Gyroscope,The Macmillan Book Co., New York (1929). Reprinted by Dover Publications.   
3. Ehricke,H. A.,Space Flight, Vol.1,D. Van Nostrand,New York (1960).   
4.GoldsteinH.，Classical echanics,Addison-Wesley Publishing Co.，eading Mass. (1951).   
5. Gray,A.,ATreatise on Gyrostaticsand Rotational Motion,TheacmillnBookCo., New York (1918). Reprinted by Dover Publications.   
6.Lanczos,C.,The Variational Principle of Mechanics, The University of oronto Press, Toronto (1949).   
7. McCuskeyS.W.,ntroduction to Adanced Dynamics,Addison-Wesley Publiing Co., Reading, Mass. (1958).   
8. Moulton,F.R.,Introduction to Celestial Mechanics,2nd.ed.,he MacmillnBook Co., New York (1914).   
9. Osgood, W. F., Mechanics, The Macmillan Book Co., New York (1948).   
10.Roser,J.B.,R.R.Newton,and G.L.Gross,athematical Theory ofRocket Flight, McGraw-Hill Book Co.,New York (1947).   
11. Routh,E.J.，Advanced Dynamics of a System of Rigid Bodies, 6th ed.,The Macmillan Book Co., London (1905). Reprinted by Dover Publications.   
12. Scarborough,J.B.,The Gyroscope,Interscience Publishers,New York (1958).   
13. Seifert, H. S.,et al., Space Technology， John Wiley and Sons, New York (1959).   
14. Smart, E.H.,Advanced Dynamics,The Macmillan Book Co., New York (1951).   
15.Sommerfeld,A.,Mechanics,Academic Press, New York (1952).   
16.Synge,J.L.,andB.A.Griffith,Principles ofMechanics,3rd ed.,McGraw-HillBook Co., New York (1959).   
17. Timoshenko, S.,and D. H. Young, Adoanced Dynamics, McGraw-Hill Book Co., New York (1948).   
18. Webster, A. G.， The Dynamics of Particles, 2nd ed. B. G. Teubner, Leipzig, (1912). Reprinted by Dover Publications.

# Matrices

# APPENDIX A

A system of linear equations

$$
\begin{array} { r l } & { y _ { 1 } = a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + a _ { 1 3 } x _ { 3 } } \\ & { y _ { 2 } = a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + a _ { 2 3 } x _ { 3 } } \\ & { y _ { 3 } = a _ { 3 1 } x _ { 1 } + a _ { 3 2 } x _ { 2 } + a _ { 3 3 } x _ { 3 } } \end{array}
$$

can be arranged into the matrix notation

$$
{ \left[ \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \end{array} \right] } = { \left[ \begin{array} { l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] }
$$

where the rule for the matrix multiplication is evident from the original equations. For Eq. A-2 to equal Eq. A-1, the terms of each row must be multiplied by the terms of the column $x _ { 1 }$ $x _ { 2 }$ $x _ { 3 }$ . We can then view the matrix equation, Eq. A-2,as a convenient notation which may be further abbreviated to

$$
\{ y \} = [ a ] \{ x \}
$$

We will next consider another set of linear equations like that of Eq. A-1, relating $_ x$ to $z ,$ and write its matrix form as

$$
\{ x \} = [ b ] \{ z \}
$$

where $[ b ]$ is a square matrix like that of Eq. A-2. If we wish to relate $y$ to $z$ ， Eq. A-4 can be substituted into Eq. A-3 as follows:

$$
\begin{array} { c } { { \{ y \} = [ a ] [ b ] \{ z \} } } \\ { { = [ c ] \{ z \} } } \end{array}
$$

The elements of $[ c ]$ can then be shown to be available from the equation

$$
c _ { i j } = \sum _ { k } a _ { i k } b _ { k j }
$$

i.e., the third element of the second row is

$$
c _ { 2 3 } = a _ { 2 1 } b _ { 1 3 } + a _ { 2 2 } b _ { 2 3 } + a _ { 2 3 } b _ { 3 3 }
$$

There are many theorems relating to the manipulation of matrix equations; however for the purposes of linear transformation of coordinates, as treated in this text, the simple algebraic concepts discussed above are suffcient.

# REFERENCES

1. Frazer,R.A.W.J.Duncanand A.R.Collar,Elementary atricesCamridge University Press, New York (1938).   
2.Pipes,L.A.Appliedthematicsfor ngineersndicists2nded,caw Hill Book Co., New York (1958), Chap. 4.

# APPENDIX B

We occasionally encounter a quantity which has nine components in a three-dimensional space. In elasticity we encounter nine components of stress at a point, whereas in dynamics we find nine components of inertia.

For our purposes we can define a dyadic as a nine-component quantity which can be formed by multiplying two vectors, ignoring the dot- or cross-product rule. Thus the product of two vectors a and b is,

$$
\begin{array} { r l } & { \mathbf { a b } = \mathbf { i } \mathrm { i } a _ { x } b _ { x } + \mathbf { i j } a _ { x } b _ { y } + \mathbf { i k } a _ { x } b _ { z } } \\ & { \qquad + \mathbf { j i } a _ { y } b _ { x } + \mathbf { j j } a _ { y } b _ { y } + \mathbf { j k } a _ { y } b _ { z } } \\ & { \qquad + \mathbf { k i } a _ { z } b _ { x } + \mathbf { k j } a _ { z } b _ { y } + \mathbf { k k } a _ { z } b _ { z } } \end{array}
$$

Although the above dyadic was formed by the multiplication of the two vectors a and b, the elements of the dyadic (called dyads) need not be related to the two vectors. Furthermore, it is convenient to arrange such terms in matrix form, so that a dyadic is in general expressible as,

$$
\mathscr { C } = \left[ \begin{array} { l l l } { \mathbf { i } \mathbf { i } c _ { x x } } & { \mathbf { i j } c _ { x y } } & { \mathbf { i k } c _ { x z } } \\ { \mathbf { j i } c _ { y x } } & { \mathbf { j j } c _ { y y } } & { \mathbf { j k } c _ { y z } } \\ { \mathbf { k i } c _ { z x } } & { \mathbf { k j } c _ { z y } } & { \mathbf { k k } c _ { z z } } \end{array} \right]
$$

As an example of a dyadic not related to any vector, we have the inertia dyadic,

$$
\mathcal { S } = \left[ \begin{array} { r r r } { \mathbf { i } \dot { U } _ { x x } } & { - \mathbf { i j } I _ { x y } } & { - \mathbf { i k } I _ { x z } } \\ { - \mathbf { j i } I _ { y x } } & { \mathbf { j j } I _ { y y } } & { - \mathbf { j k } I _ { y z } } \\ { - \mathbf { k i } I _ { z x } } & { - \mathbf { k j } I _ { z y } } & { \mathbf { k k } I _ { z z } } \end{array} \right]
$$

To illustrate the general rule for the dot or cross product of a dyadic with a vector, we assume that the dyadic is formed by the product of two vectors as

$$
\mathcal { C } = { \mathfrak { a } } \mathbf { b }
$$

Its dot and cross product with a vector r is then dependent on the order of the product, and its interpretation is made clear by the following examples :

$$
{ \begin{array} { r l } & { \mathcal { C } \cdot \mathbf { r } = ( \mathbf { a } \mathbf { b } ) \cdot \mathbf { r } = \mathbf { a } ( \mathbf { b } \cdot \mathbf { r } ) = \mathbf { a } { \mathrm { ~ v e c t o r ~ i n ~ t h e ~ d i r e c t i o n ~ o ~ } } } \\ & { \mathbf { r } \cdot \mathcal { C } = \mathbf { r } \cdot ( \mathbf { a } \mathbf { b } ) = ( \mathbf { r } \cdot \mathbf { a } ) \mathbf { b } = \mathbf { a } { \mathrm { ~ v e c t o r ~ i n ~ t h e ~ d i r e c t i o n ~ o ~ } } } \\ & { \mathcal { C } \times \mathbf { r } = ( \mathbf { a } \mathbf { b } ) \times \mathbf { r } = \mathbf { a } ( \mathbf { b } \times \mathbf { r } ) = \mathbf { a n o t h e r ~ d y a d i c } } \\ & { \mathbf { r } \times \mathbf { \mathcal { C } } = \mathbf { r } \times ( \mathbf { a } \mathbf { b } ) = ( \mathbf { r } \times \mathbf { a } ) \mathbf { b } = \mathbf { a n o t h e r ~ d y a d i c } } \end{array} }
$$

If we form the dot product of the inertia dyadic with the angular velocity vector $\mathbf { \omega } \omega = \omega _ { x } \mathbf { i } + \omega _ { y } \mathbf { j } + \omega _ { z } \mathbf { k } ,$ ， the result will be the angular momentum vector.

$$
\begin{array} { r l } & { \mathbf { h } = \mathcal { I } \cdot \mathbf { \boldsymbol { \omega } } = \mathbf { i } ( I _ { x x } \omega _ { x } - I _ { x y } \omega _ { y } - I _ { x z } \omega _ { z } ) } \\ & { \qquad + \mathbf { j } ( - I _ { x y } \omega _ { x } + I _ { y y } \omega _ { y } - I _ { y z } \omega _ { z } ) } \\ & { \qquad + \mathbf { k } ( - I _ { x z } \omega _ { x } - I _ { y z } \omega _ { y } + I _ { z z } \omega _ { z } ) } \end{array}
$$

Here we encounter dot products such as,

$$
{ \begin{array} { r l } & { { \mathbf { j i } } \cdot { \mathbf { i } } = { \mathbf { j } } ( { \mathbf { i } } \cdot { \mathbf { i } } ) = { \mathbf { j } } } \\ & { { \mathbf { j i } } \cdot { \mathbf { j } } = { \mathbf { j } } ( { \mathbf { i } } \cdot { \mathbf { j } } ) = 0 , { \mathrm { e t c } } . } \end{array} }
$$

which are evident from the general rule,and recognize that the subscripts of the inertia are interchangeable, i.e., $I _ { x y } = I _ { y x }$ . If,furthermore, we dot the angular velocity vector into the angular momentum vector, the result is a scalar, which in this case is twice the kinetic energy.

$$
2 T = \omega \cdot \mathcal { F } \cdot \omega
$$

In summary, the dyadic is a special form of a tensor; however, our simple definition of the dyadic and its product with a vector requires no new rules of vector algebra, which appears to be adequate for the dynamical problems encountered in this text.For further reading on the subject,see reference.

# REFERENCE

1. Weatherburn,C.E.,Advanced Vector Analysis,G.Bell & Sons,Ltd.,London (1947), Chapter 5, and p. 207.

# The Variational Calculus

# APPENDIX C

Many problems in Dynamics are formulated in terms of maxima and minima of quantities expressed by an integral. In this section we will briefly discuss the essentials of the variational calculus which are encountered for such problems.

Consider the integral,

$$
I = \int _ { a } ^ { b } f \left( t , z , { \frac { d z } { d t } } \right) d t
$$

taken along a curve $z = \psi ( t )$ . The quantity $z$ can stand for any number of variables, such as position $_ { x }$ ， $y$ , and the thrust attitude $\phi$ of the missile problem. The value of the integral $\varLambda$ will depend on the curve $z = \psi ( t )$ which we wish to find for the condition of maxima or minima of the integral C-1.

Assuming that $z = \psi ( t )$ along curve $a b$ of Fig. C-1 to be the optimum curve, we draw curve 1 along $a b _ { 1 }$ as the varied curve. The quantity $z$ along the varied curve is represented by

$$
z _ { 1 } = z + \delta z
$$

where $\delta z$ is the variation of $z$ . The variation $\delta z$ differs from $d z$ in that $d z$ is the increment along the curve $z$ due to an increment $d t$ ,whereas $\delta z$ is the difference in the $_ { z }$ between the two curves for any given time t. We can also define the difference in the slopes of the $z$ curves at any time $t$ to be

$$
\delta z ^ { \prime } = { z _ { 1 } } ^ { \prime } - z ^ { \prime }
$$

If $\delta z$ is assumed to be a continuous function of time,we can differentiate Eq. C-2 and obtain

$$
\frac { d } { d t } \delta z = { z _ { 1 } } ^ { \prime } - z ^ { \prime }
$$

Comparing Eqs. C-3 and C-4, we find that

$$
\frac { d } { d t } \delta z = \delta \frac { d z } { d t }
$$

![](images/5c095d01bd39950f0abf9053b67302b9696f5bb35c26e10be0b41e886ed3a8de.jpg)  
Fig. C-l. Curve (1) is the varied curve of $a b$

which indicates that the orders of operation of $\delta$ and $d / d t$ are interchangeable. Likewise, it can be shown that the interchangeability rule applies to integrals.

$$
\delta \int z \ d t = \int \delta z \ d t
$$

With this understanding of $\delta$ , we now express $f$ along the varied curve by expanding it about the original curve. By Taylor series we can write,

$$
f ( t , z + \delta z , z ^ { \prime } + \delta z ^ { \prime } ) = f ( t , z , z ^ { \prime } ) + \frac { \partial f } { \partial z } \delta z + \frac { \partial f } { \partial z ^ { \prime } } \delta z ^ { \prime } + \cdot \cdot \cdot
$$

Considering only the first order variation, the variation of the integral $I$ is

$$
\delta I = \int _ { a } ^ { b } \left( { \frac { \partial f } { \partial z } } \delta z + { \frac { \partial f } { \partial z ^ { \prime } } } \delta z ^ { \prime } \right) d t
$$

The second term in this variation can be integrated by parts so that the final expression for $\delta I$ becomes

$$
\delta I = \frac { \partial f } { \partial z ^ { \prime } } \delta z \bigg \vert _ { a } ^ { b } + \int _ { a } ^ { b } \bigg ( \frac { \partial f } { \partial z } - \frac { d \partial f } { d t \partial z ^ { \prime } } \bigg ) \delta z d t
$$

For the curve z = γ(t) to be the optimum curve resulting in a maximum or minimum of $I ,$ the variation $\delta I$ must equal zero.

Most texts treat the case where the variation $\delta z$ is zero at the end points $a$ and $b$ (i.e., $b _ { 1 }$ coincides with $^ b$ ). In such cases the first term of Eq. C-9 vanishes, and we are left only with the integral. Since δz in the integral is arbitrary and not zero over the interval $\boldsymbol { u }$ t0 $^ { b }$ ,for the integrand to be zero, $\delta I = 0$ ,and we obtain Euler's equation

$$
\frac { d } { d t } \frac { \partial f } { \partial z ^ { \prime } } - \frac { \partial f } { \partial z } = 0
$$

The satisfaction of Euler's equation insures that the integral Iis amaximum or minimum. For the more general case where $\delta z$ is not zero at the end points, we must retain the first term and consider the entire expression $\delta I = 0 ,$ ,of Eq. C-9.

# Variation with Constraints

We often encounter problems of optimization where the integral $I$ must be maximized or minimized under conditions of constraints,

$$
\begin{array} { l } { { g \left( t , z , { \frac { d z } { d t } } \right) = 0 } } \\ { { \displaystyle h \left( t , z , { \frac { d z } { d t } } \right) = 0 } } \end{array}
$$

The procedure to be followed is then to multiply the constraint equations by arbitrary functions $\lambda$ , and maximize or minimize the equation

$$
I = \int _ { a } ^ { b } [ f ( t , z , z ^ { \prime } ) + \lambda _ { 1 } g ( t , z , z ^ { \prime } ) + \lambda _ { 2 } h ( t , z , z ^ { \prime } ) + \cdot \cdot \cdot ] d t
$$

which insures the satisfaction of the conditions of constraints in the process of optimization. The quantities λ are also functions of the variables of the problem and, since they are multiplied by zeros, the expression for I is unaltered. Equation C-9 is again applicable where $f$ now stands for the entire integrand of Eq. C-12.

Acceleration, components, 15,16 definition, 14 of general motion, 22   
Accelerometer, 186   
Altitude of, launching, 64 rocket burnout, 244 vertical coasting, 244   
Angular, momentum (moment of momentum), 49 momentum ellipsoid, 123 velocity referred to inertial coordinates,198 velocity vector, 8   
Angle of attack of missile, 227   
Anomaly, 60   
Antenna,energy dissipationof, 277   
Apogee, 59   
Apse line, 78   
Astronomical unit, 68   
Attitude control by flywheel, 236   
Attitudedrift,12,279   
Ballistic, equation for missile, 260 flight time, 93 range chart, 92 trajectory, 91   
Beam vibration of missile, 294   
Bernoulli, Jean,269   
Block diagram of, single axis platform, 183 three axis platform, 184   
Body fixed axes, 33 angular velocity of, 113   
Burnout velocity of rockets, 243   
Center of mass, earth-moon system, 55   
Central force field, 52   
Charts for orbit computation,72,74,75   
Chemical propellants, 243   
Circular orbit interception and rendezvous,83   
Circular orbit speed, 64   
Coasting height of rockets, 244   
Coin spinning, 153   
Complex angle of attack, 198   
Complex angular velocity, 116, 197   
Computer for inertial guidance, 187   
Cone, body, 115, 118 space, 115, 118   
Conic section, 59   
Conservation of energy, 48   
Conservation of momentum, 52   
Constraint, 261 equations for, 267 forces, 268 variational method with, 311   
Coordinate systems,4,29 cyclic, 276 transformation of, 29   
Coriolis acceleration,16,20,22   
Coupling in three axis platform, 183   
Cross product, 6   
Crushable material, 46   
Cubic equation for symmetric gyro, 136

D'Alembert,69   
Damped oscillation of gyrocompass,174   
Degrees of freedom, 262   
Derivative of a vector, 10   
Despinning of satellites,208   
Direct precession, 117   
Direction cosine,5,42,43   
Directrix,59   
Disk rolling on inclined plane, 281   
Displacement of a rigid body,101   
Drift of body attitude, 212   
Drop test, 46   
Dyadics of inertia,104,307,111,237,238

Earth,oblateness of, 94,98 precession of, 146   
Eccentric anomaly, 60   
Eccentricity,orbital,8,59   
Ecliptic plane, 68   
Efficiency of rockets, 246   
Ellipse,59 orbit transfer time, 74   
Ellipsoid of inertia,07,122   
Elliptic integrals,127   
Energy,47 conservation of, 48 dissipation effect on attitude, 208 dissipationbyhyteresis,215,277 kinetic, 47 orbital, 58 potential, 47   
Equations of, Euler, 111, 113, 311 Hamilton, 272 Lagrange, 272, 282,292   
Equatorial bulge,98   
Equivalent mass of two body problem, 55   
Escape velocity, 64   
Euler's, angles, 33 differential equation, 311 moment equation, 111   
Euler's, moment equation about principal axes, 113   
Exhaust velocity, 242   
Flexible missile,294   
Flight trajectory optimization,248   
Focus,59   
Forces, central, 52 conservative, 47 of constraint, 268   
Fuel, rocket,4   
General motion of rigid body 149,194   
Generalized coordinates, 264   
Generalized force,274   
Generalized impulse, 283   
Generalized momentum, 292   
Geometry of conic sections, 59   
Gimbal,axis of gyro17 mass effect, 163 walk, 169   
Gravitational constant for sun, 68   
Gravitational law, 2   
Gravitational torque, 147   
Gravity,torque of bodies,208 torque due to oblateness, 147 turn trajectory, 257   
Guidance, inertial,8   
Gyroscope, cubic equation for, 136 gimbals with mass,163 precession and nutation, 136,138   
Gyropendulum, 177   
Gyropickoffs, 179

Hamilton, 270,272   
Heading angle, 61   
Heliocentric orbit, 68   
Herpolhode curve, cone,32,118   
Hohmann transfer orbit, 66   
Holonomic system,266   
Hydrogen fuel, 242   
Hyperbola,60   
Hyperbolic transfer time, 75   
Hysteresis energy dissipation, 215

Impact, central,45   
Impulse, 45 specific of fuel, 242   
Impulsive, equation of Lagrange, 282 moment on gyro, 161   
Inertia, dyadic,04 ellipsoid, 107,122 moment of, 106 product of, 106   
Inertial, coordintes,3 guidance, 181 navigation, 186   
Initial conditions for satellite injection, 61   
Injection velocity,61   
Instantaneous burning of fuel. 255   
Instantaneous center, 32   
Instruments, gyroscopic,178,180   
Integrating gyro, 180   
Interception of satellite,circular orbit, 83 elliptic orbit, 85 noncoplanar orbit, 86   
Invariable plane, line, 122   
Invariance, of kinetic energy, 121 of moment of momentum, 121

Jet damping of rocket, 222

Kepler's equation, 76 law,53   
Kinetic energy， in generalized coordinates, 172 of rigid bodies, 105 of two body system,54   
Lagrange, 272 equations, 274, 275 equations for impulsive force, 282 equations for rotating coordinates, 292 multiplier, 250   
Lagrangian, 274   
Launching parameters, 61, 64   
Line integral, 47   
Linear equation with variable coefficients,228

Mass,definition of,2 Mass ratio of rocket, 243 Matrices,31, 305 Missile dynamics, 293 Moment, 49 of inertia, 103 of momentum, 49, 103

Moment, of a vector, 8   
Moments for steady precession of gyro, 140   
Momentum, conservation of, 52 linear,44,45 sphere,126 theorems,49   
Motion,about body axes,113 about a fixed point, 102 due to central forces,52 under zero moment, 113   
Navigation, inertial, 186   
Navigation errors, 188   
Near symmetric body, 201 inertia relationship, 203 motion referred to inertial coordinates, 205   
Newton’s law of gravitation, 2   
Newton's laws of motion, 2   
Node line, 35   
Noncoplanar orbit interception, 86   
Nonholonomic system,266,279   
Nonlinear equation techniques, 166   
Normal modes, 278   
Nutation of earth, 146   
Oblateness of earth,94, 98   
Optimization of, multistage payload, 246 thrust attitude, 249   
Orbit, change due to impulse, 66 computation charts, 72 eccentricity, 58 equation, 58 parameters, 62, 72 transfer time, 74, 75   
Ore crusher, 145   
Oscillation of, navigation errors, 188 symmetric gyro, 137   
Parabola, 60   
Particle, 1   
Particle dynamics, 44   
Payload, 246   
Pendulum, centrifugal, 287 double, 265 Schuler, 190 spherical, 275,290 tuned, 238   
Performance, of rockets, 240 multistage optimization, 246 powered trajectory, 249   
Perigee,59   
Period of elliptic orbit, 65   
Perturbation,of orbit parameters, 79 technique for nonlinear systems, 166   
Pickoff, gyro, 179   
Plane motion, 14   
Planets,staces fromn69 orbits of, 56   
Poinsot's geometric solution, 121   
Poinsot's ellipsoid   
Polar coordinates, 14   
Polhode curves,cones,,125   
Position error of platform, 189   
Potential, 48   
Potential energy,48,58,105   
Powered flight trajectory249   
Precession, 117 of earth, 146   
Principal axes, 107   
Propellant, mass,246 specific impulse, 242 sloshing, 293 types,242 utilization, 252   
Radial components of velocity，acceleration,14,15   
Radiue of curvature, 16   
Range,ballistic,92   
Rate gyro, 178   
Ratio,mass,243 thrust, 242   
Regression of node line, 99   
Relative motion,18 to rotating earth, 27   
Rendezvous of satellites, 83   
Resolution of platform torque, 185   
Resonance of spinning antenna,279   
Restitutionfie,45   
Retrograde precession,17   
Rheonomic,270   
Right-handed coordinate system, 4   
Rigid body, kinetic energyof,105   
Rocket, efficiency46 multistage, 242 theory, 240   
Rotated coordinates,33 moments and products of inertia about, 105   
Rotating curve, 18   
Rotation referred to inertial coordinates, 198   
Satellite, interception, 83 launching conditions, 61 orbits, 56 rendezvous, 83   
Scalar dot product, 6   
Scalar quantity, 3   
Schuler pendulum,190   
Scleronomic,270   
Semimajor, minor axes of ellipse, 59   
Simple pendulum, 264   
Single axis platform,181   
Single stage rocket,240   
Sleeping top,141   
Small oscillations of gyos,155   
Solar system, 68, 69   
Solid fuel, 242   
Solution by Laplace transform, 159   
Space, equations of motion,22 vehicle motion, 194   
Specific impulse of fuels, 242, 243   
Spin requirement for gyro139   
Spinning disk, 152   
Spinning rocket, 223   
Stable platform,180   
Stabilityrgyideraio of orbits, 81 of rotation about principal axes, 130   
Staging of rockets,246   
Steady precession of gyros,138   
Structural damping, 215   
Structural factor for rockets, 247   
Thrust,attitude of, 249 misalignment, 195 ratio of rockets, 242 of rockets,241, 221   
Time of ballistic flight,93   
Time of orbit travel,73   
Trajectorygavity25 optimum, 248   
Transfer, functions for platforms,182 matrix, 31   
Transfer orbit, coaxial ellipse, 70 Hohmann, 66 hyperbolic, 72 noncoplanar, 87 time,73   
Transformation of, coordinates, 29,34 moments and products of inertia, 105 velocity, 31, 37   
Transverse components,velocity d c celeration, 14,15   
Tumbling,rate of, 218   
Tuned absorber, 238   
Two body problem, 54

Undetermined multipliers, 280   
Unit vector,5

Variable mass body,220,230   
Variational method,25o,309,11   
Vector properties, addition, 5 bound, 4 components, 6   
Vector properties, cross products，6 derivative of,10,11 dot product, 6 free,4 moment of, 8 multiple product of, 8 quantity, 4 rectangular components, 7 resolution, 5   
Vehicle motioneffectongrocomss, 175   
Velocity,definition,13,14   
Velocity impulse for Hohmann transfer,67   
Vibration of missiles, 294   
Virtual work, 268

Weight,2 Work,47 virtual, 268

Zero lift trajectory, 257

# ACATALOG OF SELECTED DOVER BOOKS IN SCIENCE AND MATHEMATICS

QUALITATIVE THEORY OFDIFFERENTIAL EQUATIONS,V.V.Nemytskii and V.V. Stepanov. Classic graduate-level text by two prominent Soviet mathematicians covers classical differential equations as well as topological dynamic and ergodic theory. Bibliographies. 523pp. $5 \% \times 8 \%$ 65954-2 Pa. \$10.95

MATRICES AND LINEAR ALGEBRA,Hans Schneider and George Phillip Barker.Basic textbook covers theory of matrices and its applications to systems of linear equations and related topics such as determinants, eigenvalues and differential equations. Numerous exercises. 432pp. $5 \% \times 8 \%$ 66014-1 Pa. \$9.95

QUANTUM THEORY, David Bohm. This advanced undergraduate-level text presents the quantum theory in terms of qualitative and imaginative concepts, followed by specific applications worked out in mathematical detail. Preface. Index. $6 5 5 \mathrm { p p }$ · $5 \% \times 8 \%$ 65969-0 Pa. \$13.95

ATOMIC PHYSICS (8th edition), Max Born. Nobel laureate's lucid treatment of kinetic theoryof gases,lementary prticles,uclearatom,wave-corpuscles,toic structureandspectrallines,muchore.Over40appendices,iblography.49p. $5 \% \times 8 \%$ 65984-4 Pa. \$11.95

ELECTRONIC STRUCTURE AND THE PROPERTIES OF SOLIDS: The Physics of the Chemical Bond, Walter A. Harrison. Innovative text offers basic understanding of the electronic structure of covalent and ionic solids, simple metals,transition metals and their compounds.Problems.1980 edition.582pp. $6 \% \times 9 \%$ 66021-4 Pa. \$14.95

BOUNDARY VALUE PROBLEMS OF HEAT CONDUCTION， M. Necati Ozisik.Systematic,comprehensive treatment of modernmathematical methodsof solving problems in heat conduction and diffusion. Numerous examples and problems.Selected references.Appendices.505pp. $5 \% \times 8 \%$ 65990-9 Pa. \$11.95

A SHORT HISTORY OF CHEMISTRY (3rd edition), J.R. Partington. Classic expositioneosiginsistryyrlcalmtr ofatmosphretoryofencyawdtructureofomicoryuce $4 2 8 \mathrm { p p }$ $5 \% \times 8 \%$ (Availablein U.S.only) 65977-1 Pa.\$10.95

A HISTORY OF ARONOMY,A. Pannekoek.Wellbalanced, carefully easonedstudyeschocsoleicryokose Newton,Edgton'skarsuche.atedeees. $5 \% \times 8 \%$ 65994-1 Pa. \$11.95

PRINCIPLES OF METEOROLOGICAL ANALYSIS, Walter J. Saucier. Highly respectedtlyladiceic csa more).Forintermedatemeteorologytuets. $4 5 4 \mathrm { p p }$ $6 \% \times 9 \%$ 65979-8Pa.\$12.95

# CATALOG OF DOVER BOOKS

RELATIVITY, THERMODYNAMICS AND COSMOLOGY, Richard C. Tolman.Landmark study extends thermodynamics to special,general relativity;lso olicationsof relativistic mechanics,thermodynamics tocosmological models. $5 0 \mathrm { I p p }$ $5 \% \times 8 \%$ 65383-8 Pa. \$12.95

APPLIED ANALYSIS,Cornelius Lanczos. Classic work onanalysis and design of finite processes for approximating solution of analytical problems. Algebraic uations,matrices,rmonicalysisuadraturemthods,uchmore.59p. $5 \% \times 8 \%$ 65656-X Pa. \$12.95

SPECIAL RELATIVITY FOR PHYSICISTS, G.Stephenson and C.W. Kilmister. Concise elegant account for nonspecialists. Lorentz transformation,optical and dynamicalapplicaons,more.Bibliography.8pp. $5 \% \times 8 \%$ T65519-9Pa.\$4.95

INTRODUCTION TOANALYSIS, Maxwell Rosenlicht. Unusually clear,accessible coverageofstheoryeal nmbersstemmetricsacesoio functions,iemannitegration,multipleitegals,more.Wideangeofpoems. Undergraduate level. Bibliography. 254pp. $5 \% \times 8 \%$ 65038-3 Pa.\$7.95

INTRODUCTION TO QUANTUM MECHANICS With Applications to Chemistry,LinusPauling&E.Bright Wilson,Jr.Classicundergraduate textbyNobel Prize winner applies quantum mechanics to chemical and physical problems. Numerous tables and figures enhance the text. Chapter bibliographies. Appendices. Index. 468pp. $5 \% \times 8 \%$ 64871-0 Pa. \$11.95

ASYMPTOTIC EXPANSIONS OFINTEGRALS, Norman Bleistein& Richard A. Handelsman. Best introduction to important field with applications in a variety of scientific disciplines.New preface.Problems.Diagrams.Tables.Bibliography. Index. 448pp. $5 \% \times 8 \%$ 65082-0 Pa.\$11.95

MATHEMATICS APPLIED TO CONTINUUM MECHANICS,Lee A. Segel. Analyzes models of fluid flow and solid deformation.For upper-level math,science and engineering students. $6 0 8 \mathrm { p p }$ $5 \% \times 8 \%$ 65369-2 Pa. \$13.95

ELEMENTS OF REAL ANALYSIS, David A. Sprecher. Classic text covers fundamental concepts,real number system,point sets,functions of a real variable, Fourier series,much more.Over 500 exercises.352pp. $5 \% \times 8 \%$ 65385-4 Pa. \$9.95

PHYSICAL PRINCIPLESOF THE QUANTUM THEORY,Werner Heisenberg. Nobel Laureate discusses quantum theorv,uncertainty,wave mechanics,work of Dirac,roiger,nint $1 8 4 \mathrm { p p }$ $5 \% \times 8 \%$ 60113-7 Pa. \$4.95

INTRODUCTORY REAL ANALYSIS, A.N. Koimogorov, S.V. Fomin. Translated by Richard A. Silverman.Self-contained,evenly paced introduction to real and functional analysis.Some 350 problems. 403pp.5%×8%.61226-0 Pa. \$9.95

PROBLEMSAND SOLUTIONSINQUANTUMCHEMISTRY AND PHYSICS, Charles S. Johnson,Jr.and Lee G.Pedersen. Unusually varied problems,detailed solutions in coverage of quantum mechanics, wave mechanics,angular momentum，molecular spectroscopy， scattering theory， more. 280 problems plus 139 supplementary exercises. $4 3 0 \mathrm { p p }$ $6 \% \times 9 \%$ 65236-X Pa. \$11.95

# CATALOG OF DOVER BOOKS

ORDINARY DIFFERENTIAL EQUATIONS, Morris Tenenbaum and Harry Pollard.Exhaustive survey of ordinarydifferential equations for undergraduates in mathematics,engineering， science. Thorough analysis of theorems.Diagrams. Bibliography. Index.818pp. $5 \% \times 8 \%$ 64940-7 Pa. \$16.95

STATISTICAL MECHANICS:Principles and Applications, Terrell L. Hill. Standard text covers fundamentals of statistical mechanics, applications to fluctuationteory,mperfect gases,distriution unctions,more. p. $5 \% \times 8 \%$ 65390-0 Pa. \$9.95

ORDINARY DIFFERENTIAL EQUATIONS AND STABILITY THEORY:An Introduction， David A. Sanchez. Brief, modern treatment. Linear equation, stability theoryforautonomous and nonautonomous systems,etc.l64pp. $5 \% \times 8 \%$ 63828-6 Pa.\$5.95

THIRTY YEARS THAT SHOOK PHYSICS: The Story of Quantum Theory, GeorgeGamow.Lucid,accessible introduction toinfluential theory of energyand matter.Careful explanations of Dirac'sant-particles,Bohr's model of theatom, much more. l2 plates. Numerous drawings. $2 4 0 \mathrm { p p }$ $5 \% \times 8 \%$ 24895-X Pa. \$5.95

THEORY OF MATRICES, Sam Perlis. Ot tstanding text covering rank, nonsingularity and inverses in connection with the development of canonical matrices under the relation of equivalence,and without the interventionof determinants. Includes exercises. 237pp. $5 \% \times 8 \%$ 66810-X Pa. \$7.95

GREAT EXPERIMENTS IN PHYSICS: Firsthand Accounts from Galileo to Einstein,edited by MorrisH.Shamos. 25 crucial discoveries:Newton's laws of motion,dick'sdftheronetoectoice Original accounts clearly annotated.370pp. $5 \% \times 8 \%$ 25346-5 Pa.\$9.95

INTRODUCTION TO PARTIAL DIFFERENTIAL EQUATIONS WITH AP PLICATIONS,E.C. Zachmanoglouand Dale W.Thoe.Essentials ofpartial differential equations applied to common problemsinengineering and the physical sciences.Problems and answers.416pp. $5 \% \times 8 \%$ 65251-3 Pa. \$10.95

BURNHAM'S CELESTIAL HANDBOOK,Robert Burnham, Jr. Thorough guide to the stars beyond our solar system. Exhaustive treatment. Alphabetical by constellation: Andromeda to Cetus in Vol. 1; Chamaeleon to Orion in Vol. 2;and Pavo to VulpeculainVol.3.Hundredsofillustrations.IndexinVol.3.20p $6 \% \times 9 \%$ ， 23567-X,23568-8, 23673-0 Pa., Three-vol. set \$41.85

ASYMPTOTIC EXPANSIONS FOR ORDINARY DIFFERENTIAL EQUA TIONS,Wolfgang Wasow.Outstanding text coversasymptoticpower series， Jordan'scanonicalform,tuningpointproblemsingularperturbations,much more.Problems. ${ } ^ { 8 8 4 } \mathrm { p p }$ $5 \% \times 8 \%$ 65456-7 Pa. \$9.95

AMATEUR ASTRONOMER'S HANDBOOK, J.B. Sidgwick. Timeless, comprehensivecoveageofeleoesrrorsesesoutingsecos micrometersoose9as $5 \% \times 8 \%$ (USO) 24034-7 Pa. \$9.95

# CATALOG OF DOVER BOOKS

SPECIAL FUNCTIONS, N.N. Lebedev. Translated by Richard Silverman. FamousRussian work treating more important special functions,with applications to specific problems of physics and engineering.38 figures. 308pp. 5% × 8/. 60624-4 Pa. \$7.95

OBSERVATIONAL ASTRONOMY FOR AMATEURS, J.B. SidgWick. Mine of usefuldatoeifonetsrosoae oets $3 8 4 \mathrm { p p }$ $5 \% \times 8 \%$ (Available inU.S, only) 24033-9 Pa. \$8.95

INTEGRAL EQUATONS,F.G.Tricomi. Authoritative, well-written treatment of extremely useful mathematical tool with wideapplications.Voltera Equations, Fredholm Equations,muchmore.Advanced undergraduateto graduate level. Exercises.Bibliography.238pp. $5 \% \times 8 \%$ 64828-1 Pa. \$6.95

CELESTIAL OBJECTS FOR COMMON TELESCOPES, T.W. Webb. Inestimableaid forlocating and identifying nearly40o0celestial objects.77illustrations. 645pp. $5 \% \times 8 \%$ 20917-2,2-0a.wvol.set\$12.00

MODERN NONLINEAR EQUATIONS, Thomas L. Saaty. Emphasizes practical solution of problems; covers seven types of equations."...awelcomecontribution to the existing literature...."-Math Reviews.490pp. $5 \% \times 8 \%$ 64232-1 Pa.\$9.95

FUNDAMENTALS OF ASTRODYNAMICS, Roger Bate et al. Modern approach developed by U.S. Air Force Academy. Designed asa first course. Problems, exercises. Numerous illustrations. 455pp. $5 \% \times 8 \%$ 60061-0 Pa. \$8.95

INTRODUCTION TO LINEAR ALGEBRA AND DIFFERENTIAL EQUA-TIONS, John W. Dettman. Excellent text covers complex numbers,determinants, orthonormal bases, Laplace transforms,much more. Exercises with solutions. Undergraduate level. 416pp. $5 \% \times 8 \%$ 65191-6 Pa. \$9.95

INCOMPRESSIBLE AERODYNAMICS,edited by Bryan Thwaites. Covers theoretical and experimental treatment of the uniform flow of air and viscous fluids past two-dimensionalaerofoilsandthree-dimensionalwings;manyothertopis.54pp. $5 \% \times 8 \%$ 65465-6Pa. \$16.95

INTRODUCTION TO DIFFERENCE EQUATIONS,Samuel Goldberg. Exceptionally clear exposition of important discipline with applications to sociology, psychology，economics. Many illustrative examples; over 250 problems. 260pp. $5 \% \times 8 \%$ 65084-7 Pa. \$7.95

LAMINAR BOUNDARY LAYERS,edited byL. Rosenhead. Engineering classic covers steady boundary layers in two-and three-dimensional flow,unsteady boundary layers, stability,observational techniques,much more. 708pp. 5% ×8%. 65646-2 Pa. \$15.95

LECTURESON CLASSICAL DIFFERENTIAL GEOMETRY,SeCOnd Ediuon, Dirk J. Struik. Excellent brief introduction covers curves, theory of surfaces, fundamentalequations,geometryonasurface,conformal mapping,othropics. Problems. 240pp. $5 \% \times 8 \%$ 65609-8 Pa. \$6.95

# CATALOG OF DOVER BOOKS

GEOMETRY OF COMPLEX NUMBERS,Hans Schwerdtfeger. Illuminating, widely praised book on analytic geometry of circles,the Moebius transformation, and two-dimensional non-Euclidean geometries.200pp. $5 \% \times 8 \%$ 63830-8 Pa. \$6.95

MECHANICS, J.P.Den Hartog. A classic introductory text or refresher. Hundreds of applications and design problems illuminate fundamentals of trusses, loaded beamsand cables,etc.334 answered problems.462pp. $5 \% \times 8 \%$ 60754-2 Pa. \$8.95

TOPOLOGY, John G. Hocking and Gail S. Young. Superb one-year course in classical topology. Topological spaces and functions, point-set topology，much more.Examplesand problems.Bibliography. Index. $3 8 4 \mathrm { p p }$ $5 \% \times 8 \%$

STRENGTH OF MATERIALS, J.P. Den Hartog. Full, clear treatment of basic material (tension, torsion,bending,etc.) plus advanced material on engineering methods,applications. 350 answered problems. $3 2 3 \mathrm { p p }$ $5 \% \times 8 \%$ 60755-0 Pa. \$7.50

ELEMENTARY CONCEPTS OF TOPOLOGY， Paul Alexandroff. Elegant, intuitive approach to topology from set-theoretic topology to Beti groups; how concepts of topology are useful in math and physics. 25 figures. 57pp. $5 \% \times 8 \%$ 60747-X Pa. \$2.95

ADVANCED STRENGTH OF MATERIALS, J.P. Den Hartog. Superbly written advanced text covers torsion,rotating disks,membrane stresses in shells,much more.Many problems and answers.388pp. $5 \% \times 8 \%$ 65407-9Pa.\$9.95

COMPUTABILITY AND UNSOLVABILITY, Martin Davis. Classic graduatelevel introduction to theory of computability，usually referred to as theory of recurrent functions. New preface and appendix. 288pp. $5 \% \times 8 \%$ 61471-9 Pa. \$6.95

GENERAL CHEMISTRY,Linus Pauling. Revised 3rd editionof clasic first-year text by Nobel laureate. Atomic and molecular structure, quantum mechanics, statistical mechanics,thermodynamics corelated with descriptive chemistry. Problems. 992pp. $5 \times \times 8 \%$ 65622-5 Pa.\$19.95

ANINTRODUCTION TO MATRICES,SETSAND GROUPS FOR SCIENCE TUDENT,G.eeson.oisedable tetiroucessetod most impotntlytrices tdegteetsficsst engineering. Problems.164pp. $5 \% \times 8 \%$ 65077-4 Pa.\$6.95

THE HISTORICAL BACKGROUND OF CHEMISTRY, Henry M. Leicester Evolutionof ideasnotindividualbiography.oncentratesonformulationofa coherent set of chemical laws. 260pp. $5 \% \times 8 \%$ 61053-5Pa. \$6.95

THE PHILOSOPHY OF MATHEMATICS: An Introductory Essay, Stephan Korner.SurveystheviewsofatoistotleLbiz &ntonceingi tions and theoriesofappliedandpuremathematics.Introduction.Twoappen dices.Index.198pp. $5 \% \times 8 \%$ 25048-2 Pa.\$6.95

THE DEVELOPMENT OF MODERN CHEMISTRY, Aaron J. Ihde. Authoritative history of chemistry from ancient Greek theory to 20th-century innovation. Coversmajor chemists and their discoveries.209 illustrations.14 tables.Bibliographies. Indices. Appendices.851pp. $5 \% \times 8 \%$ 64235-6 Pa. \$17.95