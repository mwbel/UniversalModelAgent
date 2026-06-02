# 4.4 Moment of Momentum

The moment about an arbitrary point $O$ of the momentum $\mathbf { p } = m \dot { \mathbf { R } }$ of a particle is

$$
\mathbf { h } _ { 0 } = \mathtt { r } \times m \dot { \mathbf { R } }
$$

where R is the absolute velocity of $m$ and $\mathbf { r }$ is drawn from $O$ as shown in Fig. 4.4-1. Differentiating this equation, we obtain

$$
\dot { \mathbf { b } } _ { 0 } = \mathbf { r } \times m \ddot { \mathbf { R } } + \dot { \mathbf { r } } \times m \dot { \mathbf { R } }
$$

![](images/67a57eb88800453cf6b11919549d2a9fff6b47b53137559b7dbcc97f1d93ac75.jpg)  
Fig. 4.4-l. Moment about $o$ of momentum mR is $\mathbf { r } \times m \mathbf { \check { R } }$ ：

Substituting $\dot { \mathbf { R } } = \dot { \mathbf { R } } _ { 0 } + \dot { \mathbf { r } }$ and noting that r $\bf { x } \in \partial \bar { \bf { r } } = 0$ ,this equation becomes

$$
\dot { \mathbf { h } } _ { 0 } = \mathbf { r } \times m \ddot { \mathbf { R } } - \dot { \mathbf { R } } _ { 0 } \times m \dot { \mathbf { r } }
$$

To establish the relationship between $\dot { \mathbf { h } } _ { 0 }$ and the moment $\mathbf { M } _ { 0 }$ of the forces $\mathbf { F } = m \tilde { \mathbf { R } }$ acting on $^ m$ , we have

$$
\begin{array} { c } { { { \bf M } _ { 0 } = { \bf r } \times m \ddot { \bf R } = { \bf r } \times m ( \ddot { \bf R } _ { 0 } + \ddot { \bf r } ) } } \\ { { { \bf \theta } } } \\ { { { \bf \theta } = \frac { d } { d t } ( { \bf r } \times m \dot { \bf r } ) - \ddot { \bf R } _ { 0 } \times m { \bf r } } } \end{array}
$$

Substituting $\mathbf { M } _ { 0 } = \mathbf { r } \times m \ddot { \mathbf { R } }$ into Eq. 4.4-3, we can also write

$$
M _ { 0 } = \dot { \bf h } _ { 0 } + \dot { \bf R } _ { 0 } \times m \dot { \bf r }
$$

Several interesting conclusions can be drawn from Eqs. 4.4-4 and 4.4-5 as follows:

a. If point $o$ is fixed in space, then $\dot { \bf R } _ { 0 } = \ddot { \bf R } _ { 0 } = 0$ and $\dot { \mathbf { r } } = \dot { \mathbf { R } }$ ，which results in the simplified equation

$$
\mathbf { M } _ { 0 } = \dot { \mathbf { h } } _ { 0 }
$$

b. If point $o$ is moving with constant velocity, $\ddot { \mathbf { R } } _ { 0 } = 0$ ,and

$$
\mathbf { M } _ { 0 } = { \frac { d } { d t } } \left( \mathbf { r } \times m { \dot { \mathbf { r } } } \right)
$$

which states that the moment is equal to the rate of change of the apparent moment of momentum expressed in terms of the relative velocity i.

c. If either $\ddot { \mathbf { R } } _ { 0 }$ and r or $\dot { \bf R } _ { 0 }$ and i are parallel, again the simplified equations are valid. d. If the system consists of more than one mass, then the second term of Eq. 4.4-4 becomes $- \ddot { \mathbf { R } } _ { 0 } \times \sum m \mathbf { r }$ which is zero $\left( \sum m \mathbf { r } = 0 \right)$ ）when the point $O$ coincides with the center of mass. The moment equation is then the same as in case $( b )$

# Example 4.4-l

A dumbbell idealized by two masses on a stiff, weightless rod of length $l$ is dropped without rotation, and the left mass strikes a ledge with velocity $v$ Assuming the coefficient of restitution to be $e$ ,determine the angular rotation of the dumbbell immediately after impact.

![](images/619be298907f9ce65645e55cc6798ca7cbf195a108f60a54eb8405f1a4ff6e33.jpg)  
Ex. 4.4-1

The sketch shows the dumbbellimmediately after impact. The velocity of the center of massimmediately after impact is $e v - \frac { l } { 2 } \dot { \theta }$ , and the change in the linear momentum is,

$$
\int f d t = 2 m \bigg ( e v - \frac { l } { 2 } \dot { \theta } \bigg ) - ( - 2 m v )
$$

The change in the moment of momentum about the center of mass is equal to the moment about the center of mass of the impulse,

$$
{ \frac { l } { 2 } } \int f d t = 2 m { \bigg ( } { \frac { l } { 2 } } { \bigg ) } ^ { 2 } { \dot { \theta } }
$$

Eliminating the impulse integral,the angular velocity immediately after impact is,

$$
\theta = \frac { v } { l } \left( 1 + e \right)
$$

# PROBLEMS

1. Aumingthatmeteosatractedbytheearthstartatinfinitywithospeed determine thespeed withhichtheywillstriketheearthegectigrction (radius of earth $= 3 9 6 0$ miles).

2. Theacceleraiofprticeacteduoyte a unit vector along r, is $( r ) { \frac { \mathbf { r } } { r } }$ ,where- is

$$
m { \ddot { \mathbf { r } } } = - f ( r ) { \frac { \mathbf { r } } { r } }
$$

Show by the vector method that equal areas are swept out by r per unit of time. Hint:

$$
{ \boldsymbol { \mathsf { r } } } \ \times { \frac { d ^ { 2 } { \boldsymbol { \mathbf { r } } } } { d t ^ { 2 } } } = { \frac { d } { d t } } { \bigg ( } { \boldsymbol { \mathbf { r } } } \ \times { \frac { d { \boldsymbol { \mathbf { r } } } } { d t } } { \bigg ) } \ = 0
$$

3. A force fieldin a plane is defined by the equation $\mathbf { F } = - \frac { K } { r } \mathbf { 1 } _ { \theta }$ where $r$ and $\theta$ are polar coordinates. Show that the above force does not have a potential when the path encloses the origin. Alternatively,describe a closed path exclusive of the origin and show that a potential exists.

4. Show that the moment of momentum about an arbitrary point 0 for a system of particles is equal to

$$
{ \bf h } _ { 0 } = \sum _ { i } { \bf r } _ { i } \times m _ { i } { \bf \dot { r } } _ { i } - { \bf \dot { R } } _ { 0 } \times \sum _ { i } m _ { i } { \bf r } _ { i }
$$

where the notation is that of Fig. 4.4-1.

5. If a tempered-steel ball, weighing 0.01 1b will support a dead weight of 800 1b without being crushed, what is the greatest speed with which it can be pro-jected without rupture, perpendicularly against a plane for which $e = 0 . 7 5$ ， assuming that the actual pressure is never greater than twice the average pressure, and the impact lasts 0.005 sec.

6. In Ex.4.4-1 the dumbbell in the horizontal position just prior to impact has an angular velocity of O.2 rad/sec counterclockwise. Determine the angular velocity immediately after impact.

7. In Ex. 4.4-1 determine the velocity of each mass before and after impact and prove that the change in the moment of momentum about the mass center is $\dot { 2 } m ( l / 2 ) ^ { 2 } \dot { \theta }$

8. During impact (see Fig. 4.2-1) the relative velocity of the two masses becomes equal to zero at the instant of maximum compression. Leting the common velocity of the masses at this instant be $\mathbf { V } _ { 0 }$ , it is possible to write for $m _ { 1 }$ the equations

$$
\begin{array} { l } { { \displaystyle \left( \int _ { \bf f \ / } d t \right) _ { \mathrm { c o m p r . } } = m _ { 1 } { \bf ( V _ { 1 \rho } - V _ { 0 } ) } } } \\ { { \displaystyle \left( \int _ { \bf f \ / } d t \right) _ { \mathrm { r e l a x . } } = m _ { 1 } { \bf ( V _ { 0 \rho } - V _ { 1 } ) } } } \end{array}
$$

and likewise a similar set for $m _ { 2 }$ .Derive Eq.4.2-2. Hint: When two fractions are equal, the two numerators and the two denominators may be added without altering their ratio.

# 4.5 Motion Under a Central Force

A force which is always directed towards a fixed point is called a central force. Choosing the origin $o$ of polar coordinates as the fixed point, the moment of the central force about O must be zero.

$$
\mathbf { M } = \mathbf { r } \times \mathbf { F } = { \dot { \mathbf { h } } } = 0
$$

![](images/e4343ca5614044793260e1e7663aa9777a5c43c67e71ffd7a5aca7dc2f33745b.jpg)  
Fig. 4.5-l. Radial and transverse components of orbit velocity.

The moment of momentum about $O$ must therefore be constant.

$$
\mathbf { h } = \mathbf { r } \times m \mathbf { v } = { \mathrm { c o n s t a n t } }
$$

As shown in Fig. 4.5-1, the magnitude of the cross product

$$
| \mathbf { r } \times \mathbf { v } | = { \frac { | \mathbf { r } \times d \mathbf { r } | } { d t } }
$$

is equal to twice the area swept out by the radial line per unit time. It is equal to the moment of momentum per unit mass, and we will designate it by the letter $h$

$$
h = | { \mathbf { r } } \times { \mathbf { v } } | = r ^ { 2 } \dot { \theta } \qquad .
$$

We will now examine the motion under a central force $F ( r )$ which is some arbitrary function of $r$ for a unit mass. The acceleration in the radial and transverse directions are

$$
\ddot { r } - r \dot { \theta } ^ { 2 } = F ( r )
$$

$$
r { \ddot { \theta } } + 2 { \dot { r } } { \dot { \theta } } = { \frac { 1 } { r } } { \frac { d } { d t } } r ^ { 2 } { \dot { \theta } } = 0
$$

From the second equation we obtain the integral corresponding to Eq. 4.5-3

$$
r ^ { 2 } { \dot { \theta } } = h = { \mathrm { c o n s t a n t } }
$$

Substituting θ = h/r2 into the first equation,it can be written as

$$
\displaystyle \ddot { r } - \frac { h ^ { 2 } } { r ^ { 3 } } = F ( r )
$$

or,since

$$
\ddot { r } = \dot { r } \frac { d \dot { r } } { d r }
$$

$$
\dot { r } \frac { d \dot { r } } { d r } = \frac { h ^ { 2 } } { r ^ { 3 } } + F ( r )
$$

Integrating,

$$
\dot { r } ^ { 2 } = - \frac { h ^ { 2 } } { r ^ { 2 } } + 2 \int F ( r ) d r + C
$$

To eliminate the time, we note that ${ \dot { r } } = ( d r / d \theta ) { \dot { \theta } } = ( d r / d \theta ) ( h / r ^ { 2 } )$ Thus Eq. 4.5-8 can be writen as

$$
\left( { \frac { d r } { d \theta } } \right) ^ { 2 } = - r ^ { 2 } + 2 { \frac { r ^ { 4 } } { h ^ { 2 } } } \int F ( r ) d r + C { \frac { r ^ { 4 } } { h ^ { 2 } } }
$$

When $F ( r )$ is specified,the orbit equation is obtained by the integration of the above equation.

Another equation of interest is the speed equation which can be determined from its two components as

$$
v ^ { 2 } = { \dot { r } } ^ { 2 } + ( r { \dot { \theta } } ) ^ { 2 } = 2 \int F ( r ) d r + C
$$

Since the direction of h as well as the magnitude must be a constant, the orbit plane, perpendicular to h, must also remain fixed. Thus, the motion under a central force requires a constant area rate and a fixed orientation of the orbit plane. The motion of planets, as stated by Kepler's second law, closely conforms to the above requirements.

# PROBLEMS

1. Determine the equation for the central attractive force $f ( r )$ for which all circular orbits have the same areal rate λ.   
2. Show that a particle in a central repulsive force field varying inversely as the square of the distance from the focus will move along a branch of a hyperbola.   
3.If a particle describes a circle with the center of force on the circumference, determine the law of force.

# 4.6 The Two-Body Problem

Consider two bodies assumed as particles and moving under the influence of a mutual attractive force. Letting $\mathbf { r } _ { 1 }$ $\mathbf { r } _ { 2 }$ ,and $\boldsymbol { \mathsf { r } } _ { c }$ be the displacement vectors of each mass and their center of mass,as shown in Fig. 4.6-1, the vector $\mathbf { r } = \mathbf { r } _ { 1 } - \mathbf { r } _ { 2 }$ will define their separation distance. The distance of each mass from their center of mass is $[ m _ { 2 } / ( m _ { 1 } + m _ { 2 } ) ] \mathbf { r }$ and $[ m _ { 1 } / ( m _ { 1 } + m _ { 2 } ) ] \mathbf { r }$ so that $\mathbf { r } _ { 1 }$ and $\mathbf { r } _ { 2 }$ can be expressed in terms of $\mathbf { r } _ { c }$ and r as

![](images/27b73c9f0b42b21d5b7fd70a82f388db3863a86f6a791a35d780f523ebb3f137.jpg)  
Fig. 4.6-l. Displacement vectors of two masses and their center of mass $c$

$$
\begin{array} { l } { \displaystyle \mathbf { r } _ { 1 } = \mathbf { r } _ { \circ } + \frac { m _ { 2 } } { m _ { 1 } + m _ { 2 } } \mathbf { r } } \\ { \displaystyle \mathbf { r } _ { 2 } = \mathbf { r } _ { \circ } - \frac { m _ { 1 } } { m _ { 1 } + m _ { 2 } } \mathbf { r } } \end{array}
$$

We now let $\mathbb { F } _ { 1 }$ and $\mathbf { F } _ { 2 }$ be forces acting on $m _ { 1 }$ and $m _ { 2 }$ respectively, and write Newton's equations,

$$
\begin{array} { l } { \mathbf { F } _ { 1 } = m _ { 1 } \ddot { \mathbf { r } } _ { 1 } = m _ { 1 } \ddot { \mathbf { r } } _ { \mathrm { c } } + \frac { m _ { 1 } m _ { 2 } } { m _ { 1 } + m _ { 2 } } \ddot { \mathbf { r } } } \\ { \qquad \mathrm { F } _ { 2 } = m _ { 2 } \ddot { \mathbf { r } } _ { 2 } = m _ { 2 } \ddot { \mathbf { r } } _ { \mathrm { c } } - \frac { m _ { 1 } m _ { 2 } } { m _ { 1 } + m _ { 2 } } \ddot { \mathbf { r } } } \end{array}
$$

In addition we can write the equation for the kinetic energy.

$$
\begin{array} { c } { { T = \displaystyle \frac { m _ { 1 } { \dot { r } } _ { 1 } ^ { ~ 2 } } { 2 } + \frac { m _ { 2 } { \dot { r } _ { 2 } } ^ { ~ 2 } } { 2 } } } \\ { { { } } } \\ { { { } = \displaystyle \frac { ( m _ { 1 } + m _ { 2 } ) } { 2 } { \dot { r } _ { c } } ^ { ~ 2 } + \frac { 1 } { 2 } \Big ( \frac { m _ { 1 } m _ { 2 } } { m _ { 1 } + m _ { 2 } } \Big ) { \dot { r } } ^ { 2 } } } \end{array}
$$

If we specify that the system is isolated from external forces, then the resultant force F = F1 + F = O, which requires that the acceleration r。 of its center of mass must be zero. The force equations then reduce to

$$
\mathbf { F _ { 1 } } = - \mathbf { F _ { 2 } } = \left( { \frac { m _ { 1 } m _ { 2 } } { m _ { 1 } + m _ { 2 } } } \right) \ddot { \mathbf { r } }
$$

Eqs. 4.6-3 and 4.6-4 indicate that the two-body problem can be reduced to that of a single body with an equivalent mass $( m _ { 1 } m _ { 2 } ) / ( m _ { 1 } + m _ { 2 } )$ at a distance r from the center of mass which is either stationary or in uniform motion along a straight line. It should be noted that the requirement $\mathbf { F } _ { 1 } = - \mathbf { F } _ { 2 }$ does not restrict the forces to be collinear, so that the force system may be a couple as well as a collinear mutual attraction.

If one of the masses is very large compared to the other, the equivalent mass $( m _ { 1 } m _ { 2 } ) / ( m _ { 1 } + m _ { 2 } )$ reduces to that of the smaller mass moving relative to the center of the larger mass. This is essentially the condition encountered when a satellite is placed into an orbit around the earth. It is,however, of interest to recognize that we have a two-body problem which can be analyzed exactly in terms of an equivalent one-body problem.

# Example 4.6-l

Assume that the ratio of the mass of the moon to that of the moon plus earth is known as

![](images/6d8f6a559d3f4952017305a456f14dbf8e1111366404fdb891d2083bb0197a50.jpg)  
Fig. 4.6-2. Earth-moon system and their center of mass.

By observation relative to the fixed stars, the angular velocity ω of the line joining the centers of the earth and moon can be measured as ω = 2.66 × 10-6 rad/sec. Show that the distance between the two bodies is

$$
D ^ { 3 } = \frac { g R ^ { 2 } } { \omega ^ { 2 } ( 1 ~ - ~ \mu ) }
$$

Referring to Fig. 4.6-2, the center of mass is given by the equation

$$
m _ { 1 } x = ( D - x ) m _ { 2 } \qquad x = D \mu
$$

Equating the force in Eq. 4.6-4 to Newton's gravitational force, we obtain

$$
\begin{array} { c } { { \displaystyle \frac { G m _ { 1 } m _ { 2 } } { D ^ { 2 } } = \frac { K m _ { 2 } } { D ^ { 2 } } = \frac { m _ { 1 } m _ { 2 } } { m _ { 1 } + m _ { 2 } } D \omega ^ { 2 } } } \\ { { { } } } \\ { { D ^ { 3 } = \displaystyle \frac { K ( m _ { 1 } + m _ { 2 } ) } { m _ { 1 } \omega ^ { 2 } } } } \end{array}
$$

Substituting $1 - \mu = m _ { 1 } / ( m _ { 1 } + m _ { 2 } ) ,$ and $K = g R ^ { 2 }$

$$
D ^ { 3 } = \frac { g R ^ { 2 } } { \omega ^ { 2 } ( 1 - \mu ) }
$$

# PROBLEMS

1. If the mass of the moon is $\scriptstyle { \frac { \mathbf { 1 } } { 8 \mathbf { 1 } } }$ times that of the earth and its period is 27.32 days, determine the distance in miles between their centers, using $R = 3 9 6 0$ miles for earth.   
2. Determine the distance from the earth's center to the center of mass of the earth-moon system.   
3. Determine the distance from the center of earth to the neutral point where the attractions of the earth and moon balance each other.   
4. Derive the equation,

$$
\frac { G m _ { 2 } } { r ^ { 8 } } = \frac { m _ { 2 } } { m _ { 1 } + m _ { 2 } } \bigg ( \frac { 2 \pi } { \tau } \bigg ) ^ { 2 }
$$

for the earth-moon system, where $m _ { 2 }$ and $m _ { 1 }$ are the mass of the moon and earth respectively, $r$ the distance between their centers, and $\tau$ the period of rotation of the moon about the earth.

# 4.7 Orbits of Planets and Satellites

In the two-body problem where one of the masses is very large compared to the other,the motion of the smaler mass takes place about the larger mass whose gravitational attraction is an inverse-square central force. For anartificialsatellitemovingaround theearth as its focalcenterthe gravitational attraction is

$$
F = - { \frac { G M m } { r ^ { 2 } } }
$$

where M and m are the masses of the earth and satellite, G is a constant, and $r$ is the distance of $m$ from thecenterof the earth. Equation4.7-1also applies to the earth-sun and the moon-earth system. The constant $_ { G M }$ can be evaluated from a simple experiment of a falling body at the earth's surface. If the measured acceleration of the faling body at r = R is g, then $F / m = - g = - G M / R ^ { 2 }$ We will now replace the constant $G M =$ $g R ^ { 2 }$ by the leter $K$ The constant $K$ can also becalculated from measured observations of earthbound satellite orbits.

Assuming the satelite to be successfully launched,its motion is governed by the following equations of force;

Radial force

$$
{ \ddot { r } } - r { \dot { \theta } } ^ { 2 } = - { \frac { K } { r ^ { 2 } } }
$$

Transverse force

$$
r \ddot { \theta } + 2 \dot { r } \dot { \theta } = \frac { 1 } { r } \frac { d } { d t } r ^ { 2 } \dot { \theta } = 0
$$

The second equation leads to the statement of conservation of moment of momentum per unit mass $r ^ { 2 } \theta = h ,$

Since our interest is centered about the shape of the orbit, it is advisable to eliminate the independent variable $t$ in terms of $\theta$ as follows,

$$
{ \dot { r } } = { \frac { d r } { d \theta } } { \dot { \theta } } = { \frac { h } { r ^ { 2 } } } { \frac { d r } { d \theta } } = - h { \frac { d } { d \theta } } { \frac { 1 } { r } }
$$

Thus by letting $1 / r = u ,$ the following terms are converted to the new variables,

$$
\begin{array} { l } { { \dot { r } = - h { \frac { d u } { d \theta } } } } \\ { { \ddot { r } = - h { \frac { d ^ { 2 } u } { d \theta ^ { 2 } } } \dot { \theta } = - h ^ { 2 } u ^ { 2 } { \frac { d ^ { 2 } u } { d \theta ^ { 2 } } } } } \end{array}
$$

Substituting these quantities into the radial force equation,the diferential equation for the orbit becomes

$$
{ \frac { d ^ { 2 } u } { d \theta ^ { 2 } } } + u = { \frac { K } { h ^ { 2 } } }
$$

Equation 4.7-4, being a second-order diferential equation,requires two arbitrary constants in the general solution. The generai solution for this differential equation is,

$$
u = \frac { K } { h ^ { 2 } } + C \cos { ( \theta - \theta _ { 0 } ) }
$$

where $K / h ^ { 2 }$ is the particular integral. The constant $\theta _ { 0 }$ can be made equal to zero by measuring $\theta$ from perigee (a point of minimum distance from the origin of $r$ ).

The evaluation of the constant $C$ can be made from the energy equation. For a body at heights beyond the influence of the atmosphere, the system is conservative and the total energy $E = T + U$ of any orbit is a constant. In this equation it is convenient to consider the energies as those associated with a unit mass.

For the determination of the potential energy per unit mass, we choose the point at infinity for reference,and from Eq. 4.7-1 we obtain,

$$
U ( r ) = - K \int _ { r } ^ { \infty } { \frac { d r } { r ^ { 2 } } } = - { \frac { K } { r } }
$$

Adding this to the kinetic energy per unit mass, the total energy becomes

$$
E = { \frac { v ^ { 2 } } { 2 } } - { \frac { K } { r } }
$$

In terms of $u$ and $\theta$ ，

$$
\begin{array} { l } { { v ^ { 2 } = { \dot { r } } ^ { 2 } + ( r { \dot { \theta } } ) ^ { 2 } = h ^ { 2 } \Bigl [ \Bigl ( \frac { d u } { d \theta } \Bigr ) ^ { 2 } + u ^ { 2 } \Bigr ] } } \\ { { \qquad = h ^ { 2 } \Bigl [ C ^ { 2 } \sin ^ { 2 } { \theta } + \Bigl ( \frac { K } { h ^ { 2 } } + C \cos { \theta } \Bigr ) ^ { 2 } \Bigr ] } } \end{array}
$$

so that substituting Eqs. 4.7-8 and 4.7-5 into Eq. 4.7-7 results in

$$
C ^ { 2 } = { \left( \frac { K } { h ^ { 2 } } \right) } ^ { 2 } { \left( 1 + \frac { 2 E h ^ { 2 } } { K ^ { 2 } } \right) }
$$

The equation for $\boldsymbol { u }$ can now be written as,

$$
u = \frac { K } { h ^ { 2 } } ( 1 + e \cos \theta )
$$

where

$$
e = \sqrt { 1 + \frac { 2 E h ^ { 2 } } { K ^ { 2 } } }
$$

Equations 4.7-10 and 4.7-11 apply to the general case for the motion under the inverse-square central force,and the type of orbit is established by the numerical value of $e$ as follows:

Hyperbola ife>1   
Parabola ife=1   
Ellipse if $0 < e < 1$ (perigee corresponding to $\theta = 0$ Circle if $e = 0$   
Subcircular ellipse if $- 1 < e < 0$ (apogee--point of maximum distance from theorigin ofr corresponding to $\theta = 0$

# 4.8 Geometry of Conic Sections

Motion under centralforce results in an orbit which is one of the conic sections. The conic is the locus of a point whose distance from a fixed point $F$ and a fixed line $D D ^ { \prime }$ have a constant ratio $e$ The fixed point $F$ is called the focus, the fixed line $D D ^ { \prime }$ the directrix,and the ratio $e$ the eccentricity.

Letting $m$ be the distance from the focus to the directrix $D D ^ { \prime }$ , the polar equation for the conic is

or

$$
\begin{array} { l } { r = e ( m - r \cos \theta ) } \\ { \displaystyle r = \frac { e m } { 1 + e \cos \theta } } \end{array}
$$

By letting $\theta = 0 ^ { \circ }$ ， $9 0 ^ { \circ }$ ， $1 8 0 ^ { \circ }$ ,and tan-1 $( b / a )$ ,important distances are found.   
These are shown in Figs. 4.8-1, 4.8-2, and 4.8-3.

![](images/1c361639859508c503b0af98935515c7e25a58a599823cd67c356d432b914582.jpg)  
Fig. 4.8-l. Geometry of thc ellipse.

![](images/ef412f70dee1a351cf548655c7a8688326daf416bc4bd8c687be3127b127a12b.jpg)

![](images/a0f111bd4a9a54facd0487bc5effdbde20aedc97b272366c8736c3f3f2001309.jpg)  
Fig. 4.8-2. Geometry of the hyperbola.   
Fig. 4.8-3. Geometry of the parabola.

# PROBLEMS

1. If $x$ and $\mathcal { Y }$ are rectangular coordinates of a point on the ellipse as shown in Fig. 4.8-1, show that $x = a$ cos $\psi$ and $y = b$ sin $\psi$ ,where the angle $\psi$ is called theeccentric anomaly. Hint: Useequation ofellipse in rectangular coordinates to relate $y$ in terms of $_ x$

2. Show that cos $\psi = ( a - r ) / a e$ Hint: From Fig. 4.8-1, $r$ cos $\theta = - ( a e \mathrm { ~ - ~ }$ a cos $\psi$ ).Combine with $r = [ a ( 1 - e ^ { 2 } ) ] / ( 1 + e \cos \theta )$ to eliminate cos 0.

3. Prove the relationship

$$
\tan { \frac { \psi } { 2 } } = { \sqrt { \frac { 1 - e } { 1 + e } } } \tan { \frac { \theta } { 2 } }
$$

# 4.9 Orbit Established from Initial Conditions

The initial conditions at rocket burnout are:

$$
\begin{array} { c } { { r = r _ { 0 } } } \\ { { { \begin{array} { l } { { } } \\ { { v = v _ { 0 } } } \end{array} } } } \\ { { \beta = \beta _ { 0 } } } \end{array}
$$

where $\beta$ is the heading angle, measured outward from the normal to $r _ { : }$ as shown in Fig. 4.9-1. From this information we would like to determine

![](images/b299af944357278ff9ff0db1e67d39b9f9026a644d1fb0b76db3772b6d7c936c.jpg)  
Fig. 4.9-l. Initial conditions at injection into orbit.

the value of the eccentricity $e$ ， which establishes the type of orbit, and $\theta _ { 0 }$ ， the angle between perigee and $r _ { 0 }$

We will let $r _ { p }$ be the perigee distance at $\theta = 0$ (when $e$ is negative, $\theta = 0$ corresponds to apogee with distance $r _ { a }$ ） in which case we have from Eq. 4.7-10

$$
\frac { h ^ { 2 } } { K } = r _ { p } ( 1 + e )
$$

Equation 4.7-10 can then be written as

$$
u = \frac { 1 + e \cos { \theta } } { r _ { p } ( 1 + e ) }
$$

The components of the initial velocity are,

$$
v _ { 0 } \cos \beta _ { 0 } = r _ { 0 } \dot { \theta } _ { 0 } = \frac { h } { r _ { 0 } }
$$

$$
v _ { 0 } \sin \beta _ { 0 } = { \dot { r } } _ { 0 } = - h \bigg ( { \frac { d u } { d \theta } } \bigg ) _ { \theta = \theta _ { 0 } } = { \frac { K e } { r _ { 0 } v _ { 0 } } } { \frac { \sin \theta _ { 0 } } { \cos \beta _ { 0 } } }
$$

Since from Eq. 4.7-10 we can write

$$
\frac { 1 } { r _ { 0 } } = \frac { K } { h ^ { 2 } } ( 1 + e \cos \theta _ { 0 } )
$$

substitution for $h ^ { 2 }$ from Eq. 4.9-3 results in the equation

$$
\frac { r _ { 0 } { v _ { 0 } } ^ { 2 } } { K } \cos ^ { 2 } \beta _ { 0 } = 1 + e \cos \theta _ { 0 }
$$

![](images/ecf2cb6095861890104974f81d449d484d90426f325201a07e168f96d26a9fee.jpg)  
Fig. 4.9-2. Orbit eccentricity established from initial values of $\beta$ and $r v ^ { 2 } / K .$

Solving for $e$ sin $\theta _ { 0 }$ and $e$ cos $\theta _ { 0 }$ in Eqs. 4.9-4 and 4.9-6 and dividing, the angular position from perigee is found

$$
\tan \theta _ { 0 } = \frac { ( r _ { 0 } { v _ { 0 } } ^ { 2 } / K ) \sin \beta _ { 0 } \cos \beta _ { 0 } } { ( r _ { 0 } { v _ { 0 } } ^ { 2 } / K ) \cos ^ { 2 } \beta _ { 0 } - 1 }
$$

By adding the squares of $e$ sin $\theta _ { 0 }$ and $e$ cos $\theta _ { 0 }$ ， $e ^ { 2 }$ is obtained

$$
e ^ { 2 } = { \Big ( } { \frac { r _ { 0 } { v _ { 0 } } ^ { 2 } } { K } } - 1 { \Big ) } ^ { 2 } \mathrm { c o s } ^ { 2 } \beta _ { 0 } + \mathrm { s i n } ^ { 2 } \beta _ { 0 }
$$

Equations 4.9-7 and 4.9-8 completely establish the orbit for any initial

conditions $r _ { 0 } { v ^ { \prime } } _ { 0 } { } ^ { 2 } / K$ and $\beta _ { 0 }$ arranged in nondimensional form. In addition, the total orbit energy established from Eq.4.7-7 at burnout is

$$
\frac { E r _ { 0 } } { K } = \frac { 1 } { 2 } \frac { { r _ { 0 } } { { l _ { 0 } } ^ { 2 } } } { K } - 1
$$

A plot of Eq. 4.9-8 showing $e$ as a function of $r _ { 0 } { v _ { 0 } } ^ { 2 } / K$ with $\beta _ { 0 }$ as parameter is presented in Fig. 4.9-2. It is evident that,if $\beta _ { 0 } \neq 0$ ， $e$ can never become zero, so that a circular orbit is not possible. Equation 4.9-7 indicates that, when $( r _ { 0 } { { \dot { c } } _ { 0 } } ^ { 2 } / K )$ cos2 $\beta _ { 0 } = 1$ ， $\theta _ { 0 } = 9 0 ^ { \circ }$ .For $( r _ { 0 } v _ { 0 } { } ^ { 2 } / K ) \cos ^ { 2 } \beta _ { 0 } < 1$ and $\beta _ { 0 } > 0$ ， $\theta _ { 0 }$ is in the second quadrant.

# PROBLEMS

1. Explorer No.7launched in October 1959 resulted in thefollowing observations. Apogee distance above earth surface $= 6 6 4$ miles, Perigee distance above earth surface $= 3 4 6$ miles, Orbit period $= 1 0 1 . 2$ min.

Using mean radius of earth to be 3960 miles, calculate $K$ for earth.

2. For Prob. 1, determine the eccentricity and the perigee and apogee speed

3.Determine the circular orbit radius for which a satellite will remain stationary with respect to earth.

4. Explorer No. 6 launched in August 1959 is reported to have perigee and apogee heights above the earth's surface of 157 miles and 26,400 miles. Calculate the orbit period, its eccentricity, and the maximum speed.

5. If the initial conditions for a satellite at rocket burnout are $\beta _ { 0 }$ $r _ { 0 } / R$ and $r _ { 0 } { v _ { 0 } } ^ { 2 } / K$ ， show that the perigee and apogee distances from the center of the earth are given by the equation

$$
\frac { r _ { p , \alpha } } { r _ { 0 } } = \frac { 1 } { 2 \mathrm { ~ - ~ } ( { r _ { 0 } { v _ { 0 } } ^ { 2 } } / { K } ) } \bigg [ 1 \pm \sqrt { 1 \mathrm { ~ - ~ } \left( \frac { { r _ { 0 } { v _ { 0 } } ^ { 2 } } } { K } \right) \left( 2 \mathrm { ~ - ~ } \frac { { r _ { 0 } { v _ { 0 } } ^ { 2 } } } { K } \right) \cos ^ { 2 } \beta _ { 0 } } \bigg ]
$$

where $-$ corresponds to perigee and $^ +$ to apogee. Plot $r _ { y } / r _ { 0 }$ and $r _ { a } / r _ { 0 }$ versus rv²/K> 1 for β = 1° and 5°

6. Assess the effect of the heading angle error $\beta _ { 0 }$ on the perigee height when the velocity at rocket burnout is equal to the circular orbit value.

7. Plot $\theta _ { 0 }$ versus $r _ { 0 } { \iota _ { 0 } ^ { \ast } } ^ { 2 } / K ,$ with $\beta _ { 0 }$ as parameter. Use a range of $0 < r _ { 0 } { v _ { 0 } } ^ { 2 } / K < 2$ and $\beta _ { 0 } = \%$ ， $1 ^ { \circ }$ ， $5 ^ { \circ }$ ， $1 0 ^ { \circ }$ $3 0 ^ { \circ }$

# 4.10 Satellite Launched with $\mathsf { \beta } _ { 0 } = 0$

The special case of a satellite launched with $\beta _ { 0 } = 0$ is instructive because of its simplicity of interpretation. From Eq. 4.9-7 it is evident that $\theta _ { 0 } = 0$ , so that the launch point corresponds with perigee. Equation 4.9-8 now becomes

$$
e = \frac { r _ { 0 } { v _ { 0 } } ^ { 2 } } { K } - 1
$$

which is represented by the straight line for βo = 0 in Fig.4.9-2. Equation 4.10-1 indicates that a circular orbit ( $e = 0 .$ ） is obtained only when rov2/K = 1 and βo = O. If vo or ro is increased so that 1 < rov²/K< 2, the orbit will be an ellipse. For values of rvo2/K >2, the orbit will become a hyperbola and the satelite will escape from the earth. Thus $r _ { 0 } v _ { 0 } { } ^ { 2 } / K = 2$ corresponds to the velocity of escape at height $\begin{array} { r } { r _ { 0 } = R + z } \end{array}$

$$
v _ { e } = { \sqrt { \frac { 2 K } { r _ { 0 } } } } = R { \sqrt { \frac { 2 g } { R + z } } }
$$

Considering the geometry of the eliptic orbit, the semimajor and semiminor axes are:

$$
\begin{array} { l } { \displaystyle \frac { a } { r _ { 0 } } = \frac { 1 } { 1 - e } } \\ { \displaystyle \frac { b } { r _ { 0 } } = \sqrt { \frac { 1 + e } { 1 - e } } } \end{array}
$$

The apogee distance is:

$$
\frac { r _ { a } } { r _ { 0 } } = \frac { 1 + e } { 1 - e }
$$

and in terms of the altitude $z$ above the earth's surface, the apogee and perigee altitudes are :

$$
\begin{array} { l } { \displaystyle \frac { z _ { \alpha } } { R } = \frac { r _ { 0 } } { R } \frac { 1 + e } { 1 - e } - 1 } \\ { \displaystyle \frac { z _ { p } } { R } = \frac { r _ { 0 } } { R } - 1 } \end{array}
$$

Numerical values for smalle are given in the following table to show the nearlycircularshapeofsuchelipticorbitsinspiteofthelargedifence in the apogee and perigee heights.

Table 4.l0-l. Calculations for Launching Altitude $r _ { 0 } / R = 1 . 1 0$   

<table><tr><td>e</td><td>1+e 1-e</td><td>za &amp;p</td><td>a 6</td><td>/Elliptic speed) Circular speed)</td></tr><tr><td>0.00</td><td>1.00</td><td>1.00</td><td>1.000</td><td>1.00</td></tr><tr><td>0.05</td><td>1.105</td><td>2.15</td><td>1.00125</td><td>1.025</td></tr><tr><td>0.10</td><td>1.22</td><td>3.40</td><td>1.0050</td><td>1.050</td></tr><tr><td>0.20</td><td>1.50</td><td>6.50</td><td>1.020</td><td>1.096</td></tr></table>

For an eccentricity of 0.20, the apogee height is 6.50 times the perigee height when the launch height is ro = 1.10R, or approximately 400 miles above the earth's surface.

We can next examine the case $r _ { 0 } v _ { 0 } { } ^ { 2 } / K < 1$ .Equation 4.7-10 with negative e shows that we have an ellipse with the starting point corresponding to apogee and perigee is at $\theta = 1 8 0 ^ { \circ }$ The speed is then not sufficient to balance the attractive force of the earth,and the satelite distance $r$ will diminish from its initial value $r _ { 0 }$ With negative $e$ ，the center of the ellipse falls between the origin and the launching point. It is evident from the previous set of numbers that the satellite will fall into a region where atmospheric drag becomes important, even for small negative $e$ Figure 4.10-1 shows one such orbit along with orbits for positive $e$

![](images/854f298bf0159f88c11e0ef0bfcf36b4db11bfe51bf54a2a371efee5679f94ed.jpg)  
Fig. 4.1o-l. Satellites launched with $\beta _ { 0 } = 0$ ·

The period of closed orbits, ellipses, or circles can be found by dividing the enclosed area by the areal rate $h / 2$ . The area of the ellipse is πab. The semiminor axis, from Fig. 4.8-1, is $b = a \sqrt { 1 } - e ^ { 2 }$ ,and $h$ from Eq. 4.9-5 at $\theta = 0$ is $h = \sqrt { K r _ { p } ( 1 + e ) } = \sqrt { K a ( 1 - e ^ { 2 } ) }$ . Thus the equation for the period becomes

$$
\tau = \frac { 2 \pi a b } { h } = \frac { 2 \pi } { \sqrt { K } } a ^ { 3 / 2 }
$$

# PROBLEMS

1. A satellite is launched parallel to the earth's surface at $r / R = 1 . 1 0$ with $r v ^ { 2 } / K =$ 1.20. Determine the apogee distance and the ratio of the apogee to perigee heights above the earth's surface.

2.A satellite is launched parallel to the earth's surface with a velocity of 18,000 mph at a height of 40o miles. Calculate the apogee height above the earth's surface and the period.

3. Plot the escape velocity from the earth as a function of the altitude.

4. Determine and plot the orbit energy level $E r _ { 0 } / K$ of circular orbits as a function of the altitude z.

5. For Prob. 4, plot the period versus $z$

6. For bodies launched with $\beta _ { 0 } = 0$ at height $r _ { 0 } / R$ ,determine the equation for the apogee distance $r _ { a }$ as function of the velocity parameter $r v ^ { 2 } / K$ at perigee.

# 4.l1 Cotangential Transfer between Coplanar Circular Orbits

Transfer between coplanar circular orbits can be effected by an ellptic orbit with perigee and apogee distances equal to the radii of the respective circles,as shown in Fig. 4.11-1. The cotangential ellipse is known as the

![](images/e2f9b0b7fb0664458ea5742fbe01fee93c17ce32a0b91646d192c4b8886beff0.jpg)  
Fig. 4.Il-l. Hohmann transfer orbit.

Hohmann transfer orbit, and it can be shown to be a minimum energy orbit for transfer between the coplanar circular orbits.

Assuming transfer to take place from 1 to 2, we can obtain the raio $r _ { a } / r _ { p }$ from Eq. 4.7-10. Letting $\theta = 1 8 0 ^ { \circ }$ ， $u = 1 / r _ { a }$ so that

$$
\frac { r _ { a } } { r _ { p } } = \frac { 1 + e } { 1 - e }
$$

From Eq. 4.10-1, $e$ can be eliminated in terms of $r _ { p } v _ { p } { } ^ { 2 } / K$ as

$$
e = \frac { { r _ { v } } { v _ { p } } ^ { 2 } } { K } - 1
$$

Substituting Eq. 4.11-1 into 4.11-2, we obtain

$$
\frac { r _ { p } { v _ { p } } ^ { 2 } } { K } = \frac { 2 ( r _ { a } / r _ { p } ) } { 1 + ( r _ { a } / r _ { p } ) }
$$

which is plotted in Fig. 4.11-2.

In interpreting these results, we can assume the space vehicle to be initially orbiting around the inner circle of radius rp. This requires $r _ { p } v _ { p } { } ^ { 2 } / K$ to be equal to 1.0. To escape from the inner circular orbit and

![](images/fb7249b42bb2e349516e67076be119a890358f966c1c689fa1439cf06759cf0a.jpg)  
Fig. 4.11-2. ${ r _ { p } } { v _ { p } } ^ { 2 } / K$ necessary for Hohmann transfer between orbits $r _ { a } / r _ { p }$

travel along the elliptic transfer orbit of ratio $r _ { a } / { r _ { p } } , r _ { p } { v _ { p } } ^ { 2 } / K$ must be increased to a value given by Eq. 4.11-3. This may be accomplished by firing a rocket in the tangential direction, the required increase in velocity being

$$
\Delta v _ { p } = \sqrt { \frac { K } { r _ { p } } } \Big [ \sqrt { \frac { 2 ( r _ { a } / r _ { p } ) } { 1 + ( r _ { a } / r _ { p } ) } } - 1 \Big ]
$$

On reaching point 2, the apogee velocity， which can be found by equating the angular momentum at 1 and 2,i.e., $r _ { p } v _ { p } = r _ { a } v _ { a }$ becomes

$$
\frac { r _ { a } { v _ { a } } ^ { 2 } } { K } = \frac { r _ { p } } { r _ { a } } \frac { { r _ { p } } { v _ { p } } ^ { 2 } } { K } = \frac { 2 } { 1 + { r _ { a } } / { r _ { p } } }
$$

Since the circular orbit velocity for radius $r _ { a }$ is $r _ { a } { v _ { a } } ^ { 2 } / K = 1$ ,and the apogee velocity as given by Eq. 4.11-5 is less than 1,another thrust in the forward direction is necessary. The increment in velocity required at point 2 to go into the circular orbit is then

$$
\Delta v _ { a } = \sqrt { \frac { K } { r _ { u } } } \left( 1 - \sqrt { \frac { 2 } { 1 + ( r _ { a } / r _ { v } ) } } \right)
$$

Thus the total impulse which must be applied in the direction of motion is determined by $\Delta v _ { p } + \Delta v _ { a }$ ， and the fuel energy corresponding to it is proportional to $( \Delta v _ { p } + \Delta v _ { a } ) ^ { 2 }$

It is of interest to compare the total velocity increment to transfer from orbit 1 to orbit 2 with that of the velocity increment for escape from orbit 1. The parabolic orbit velocity of escape from radius $r _ { p }$ is found from $r _ { p } v _ { p } { } ^ { 2 } / K = 2$ to be

$$
v _ { p e } = 1 . 4 1 4 \sqrt { \frac { K } { r _ { p } } }
$$

which requires a velocity increment of

$$
\Delta v _ { p } = 0 . 4 1 4 \sqrt { \frac { K } { r _ { p } } }
$$

acquired under a single impulsive thrust.

The total velocity increment for the Hohmann transfer orbit obtained by adding Eqs. 4.11-4 and 4.11-6 is

$$
\Delta v _ { p } = \sqrt { \frac { K } { r _ { p } } } \bigg [ \sqrt { \frac { 2 ( r _ { a } / r _ { p } ) } { 1 + ( r _ { a } / r _ { p } ) } } \bigg ( 1 - \frac { r _ { p } } { r _ { a } } \bigg ) + \sqrt { \frac { r _ { p } } { r _ { a } } } - 1 \bigg ]
$$

Equating Eqs. 4.11-8 and 4.11-9 we find $r _ { \alpha } / r _ { p } = 3 . 4$ .Thus transfer between circular orbits of $r _ { a } / r _ { p } > 3 . 4$ will require rocket energy in excess of the orbit escape energy.

# Heliocentric orbits

In considering planetary orbits, the large mass of the sun $( 9 9 . 2 \%$ of the total mass of the solar system) enables one to ignore all other forces. Although planetary orbits are ellipses with their orbit planes inclined slightly from the ecliptic (earth's orbit plane), great simplification results from assuming the orbit to be circular and coplanar.

Assuming coplanar circular orbits, the equations for the Hohmann transfer orbit are applicable with the numerical values of $K$ corresponding to the sun. $K$ for the sun can be found from measured data pertaining to any planet. Assuming a circular orbit of radius $r$ for the earth, we have

$$
{ \frac { r v ^ { 2 } } { K } } = 1
$$

where $r = 4 9 0 . 5 \times 1 0 ^ { 9 } \mathrm { f t } = 9 3 \times 1 0 ^ { 6 }$ miles

$K = G M _ { s }$ for the sun   
$v = 2 \pi r / \tau =$ velocity of earth   
T = 365.25 × 86,400 sec $=$ period of the earth around the sun

Substituting these figures intoEq. 4.11-10, $K$ for the heliocentric system is found to be $4 . 6 8 \times 1 0 ^ { 2 1 } \mathrm { f t ^ { 3 } / s e c ^ { 2 } }$

Another convenient set of units for planetary and interplanetary orbits is one referenced to the earth's orbit, with $r = 1$ astronomical unit and

T =1 year. Substituting unity for these quantities in the period equation T =2πV(/K),the helocentricconstant Kbecomes equal to atr nomical units cubed per year squared.

# PROBLEMS

1. Discuss how a space vehicle traveling around a circular orbit of radius can transfer to a coplanar circular orbit of radius $r _ { 1 }$ where $r _ { 1 } < r _ { 2 }$ $r _ { 2 }$

2. Show that, if $r _ { 1 } / r _ { 2 } < 0 . 5 0$ ,the velocity increment necessary for the transfer to the inner orbit will exceed that of escape from the outer orbit.

3. Determine the time of flight for the Hohmann transfer orbit.

4. Determine the equation for the velocity $v / v _ { c }$ versus distance $r / r _ { p }$ for the Hohmann transfer orbit,wheredepartureisfromtheinnerorbitofradius and circular orbit speed $v _ { c }$ $r _ { p }$

5. A rocket traveling in a circular orbit $r _ { 1 } v _ { 1 } { } ^ { 2 } / K = 1$ is given an impulsive thrust normal to the orbit so that the resultant velocity vector makes an angle $\beta _ { 0 }$ outward from the trangent to the departing circular orbit. Determine the neworbit,specifngtheprigeandapogeedistancesandtheececity Determine $\theta _ { 0 }$ to perigee.

6. For the maneuver of Prob. 5, determine the areal rate and show that the area enclosed from the point of maneuver to apogee is given by the equation

$$
A = \frac { { r _ { p } } ^ { 2 } } { 2 ( 1 - e ) } \sqrt { \frac { 1 + e } { 1 - e } } \bigg ( e \sqrt { 1 - e ^ { 2 } } + \sin ^ { - 1 } e + \frac { \pi } { 2 } \bigg )
$$

7. A rocket traveling at $1 8 { , } 3 0 0 \ \mathrm { m p h }$ at perigee, fires a retrorocket at perigee height of 300 miles. What velocity change is necessary to reach minimum altitude of 100 miles during the frst circuit ?

8. The following table gives the distances of some of the planets from the sun.

<table><tr><td>Planet</td><td>Mean Distance from Sun</td></tr><tr><td>Mercury</td><td>0.39</td></tr><tr><td>Venus</td><td>0.72</td></tr><tr><td>Earth</td><td>1.0 = 93 × 10 miles</td></tr><tr><td>Mars</td><td>1.52</td></tr><tr><td>Jupiter</td><td>5.2</td></tr></table>

Assuming the two orbits to be in the same plane, determine the Hohmann transfer orbit from earth to Mars and compute the time required for transit. Determine the position of Mars in its orbit relative to earth for interception to take place.

9. For the transfer orbit of Prob.1, determine the velocity increments necessary on departure and on arrival.

10. Determine the spherical region around earth where the earth's gravitational attraction dominates over that of the sun.

11. Determine the equation for the escape velocity from the solar system. What is its value at the earth's orbit.

# 4.12 Transfer Between Coplanar Coaxial Elliptic Orbits

Figure 4.12-1 shows two coaxial elliptic orbits in the same plane. To transfer from the inner orbit 1 to the outer orbit 2, it can be shown that for minimum expenditure of energy, the thrust should be impulsive at perigee of the inner orbit and apogee of the outer orbit.

We will assume that the orbit parameters e and $a$ of the two orbits are given. The perigee and apogee distances are then known from the relationships $r _ { p } = a ( 1 - e )$ and $r _ { a } = a ( 1 + e ) ,$

![](images/8d7ee5b9904941bb54e19b6821322e2a8a071b10df3420e7533be746b63caddd.jpg)  
Fig. 4.l2-l. Transfer between coplanar,coaxial, elliptic orbits.

Before impulse, the velocity at $p _ { 1 }$ can be obtained from Eq. 4.9-6 by letting $\beta = 0$ and $\theta = 0$ ，

$$
v _ { p 1 } = \sqrt { \frac { K } { r _ { p 1 } } \left( 1 + e _ { 1 } \right) }
$$

For the transfer orbit,the necessary velocity at perigee can be found from Eq. 4.11-3 to be

$$
v _ { p t } = \sqrt { \frac { K } { r _ { p 1 } } [ \frac { 2 ( r _ { a 2 } / r _ { p 1 } ) } { 1 + ( r _ { a 2 } / r _ { p 1 } ) } ] }
$$

The increment in velocity required at perigee of the inner orbit is then

$$
\Delta { v _ { p 1 } } = \sqrt { \frac { K } { r _ { p 1 } } } \bigg [ \sqrt { \frac { 2 ( r _ { \alpha 2 } / r _ { p 1 } ) } { 1 + ( r _ { a 2 } / r _ { p 1 } ) } } - \sqrt { 1 + e _ { 1 } } \bigg ]
$$

After departure, the vehicle proceeds along the transfer orbit until it reaches apogee. The velocity as it approaches apogee is

$$
v _ { a t } = { \frac { r _ { p 1 } } { r _ { a 2 } } } v _ { p t } = { \sqrt { \frac { K } { r _ { a 2 } } { \frac { 2 } { 1 + ( r _ { a 2 } / r _ { p 1 } ) } } } }
$$

The apogee velocity for orbit 2 can be found from Eq. 4.9-6, letting $\beta = 0$ and $\theta = 1 8 0 ^ { \circ }$ ，

$$
v _ { \alpha 2 } = \sqrt { \frac { K } { r _ { a 2 } } \left( 1 - e _ { 2 } \right) }
$$

The increment in velocity necessary to transfer from orbit (t) to orbit (2) at apogee is then

$$
\Delta v _ { a 2 } = \sqrt { \frac { K } { r _ { a 2 } } } \overline { { { \lfloor \sqrt { 1 - e _ { 2 } } - \sqrt { \frac { 2 } { 1 + ( r _ { a 2 } / r _ { p 1 } ) } } } \rfloor } }
$$

and the total increment in velocity in the tangential direction is

$$
\Delta v _ { p 1 } + \Delta v _ { a 2 }
$$

# 4.13 Orbital Change Due to Impulsive Thrust

In this section we will consider the general problem of changing an existing orbit to another of a given specification. Such changes may range from small corrections to an existing orbit, to large changes in the orbit for maneuvers. It will be assumed that the change will take place under impulsive thrust; e.g., a change in the direction and magnitude of the velocity vector takes place under negligible change in the displacement vector. This idealization is generally acceptable when the distance traveled during thrust is negligible in comparison to the radius vector.

In general, our concern is with elliptic and hyperbolic orbits, the circle and the parabola being special limiting cases. The relationship between the velocity $v$ ， the angular position $\theta$ ， the heading angle $\beta$ ,and the eccentricity $e$ , shown in Fig. 4.13-1, is already available from Eqs. 4.9-7 and 4.9-8, which are rewritten as follows:

$$
\tan \theta = \frac { ( r v ^ { 2 } / K ) \sin \beta \cos \beta } { ( r v ^ { 2 } / K ) \cos ^ { 2 } \beta - 1 }
$$

$$
e ^ { 2 } = \left[ \frac { r v ^ { 2 } } { K } - 1 \right] ^ { 2 } \cos ^ { 2 } \beta + \sin ^ { 2 } \beta
$$

By holding $\theta$ constant and varying $\beta$ ， $r { \tau } ^ { 2 } / K$ can be computed from Eq. 4.13-1 rearranged as follows:

$$
{ \frac { r v ^ { 2 } } { K } } = { \frac { 1 } { \cos ^ { 2 } \beta - ( \sin \beta \cos \beta ) / ( \tan \theta ) } }
$$

By holding e constant and varying β, the curve for rv2/K versus β can be computed from Eq. 4.13-2 rearranged as Eq. 4.13-4:

$$
\frac { r v ^ { 2 } } { K } = 1 \pm \sqrt { 1 - \left( \frac { 1 - e ^ { 2 } } { \cos ^ { 2 } \beta } \right) }
$$

These results for the ellipse and the hyperbola are plotted as shown in Figs. 4.13-2 and 4.13-3.

![](images/b3b335802b4eafff27ef66947a62a917a1787bd0208f82a009aec63a319ab113.jpg)  
Fig. 4.l3-l. Displacement, velocity and heading angle $\beta$ at any position 0.

In adition to these two equations we have the energy relationship of Eq. 4.7-7,

$$
\frac { E r } { K } = \frac { 1 } { 2 } \frac { r v ^ { 2 } } { K } - 1
$$

Since $E$ is constant for a given orbit, we can evaluate it at perigee. Leting $\theta = \beta = 0$ in Eqs. 4.13-1 and 4.13-2,

$$
e = \frac { { r _ { p } } { v _ { p } } ^ { 2 } } { K } - 1
$$

which substituted into Eq. 4.13-5 with $r = r _ { p }$ results in

$$
\frac { 2 E } { K } = - \frac { 1 - e } { r _ { p } }
$$

Since $r _ { p } = a ( 1 - e )$ for the ellipse and $r _ { p } = a ( e \mathrm { ~ - ~ } 1 )$ for the hyperbola (see Sec. 4.8), the energy $E$ can be expressed in terms of $a$ as follows.

$$
{ \frac { 2 E } { K } } = { \left\{ \begin{array} { l l } { - { \frac { 1 } { a } } } & { \quad { \mathrm { f o r ~ e l l i p t i c ~ o r b i t } } } \\ { \quad } \\ { + { \frac { 1 } { a } } } & { \quad { \mathrm { f o r ~ h y p e r b o l i c ~ o r b i t } } } \end{array} \right. }
$$

![](images/e58650c4b16713de9c452444a6fb3162f44050a04875b38b85ef7b5ddd335d75.jpg)  
Fig. 4.l3-2. Relation between $\beta$ and $r v ^ { 2 } / K$ with $e$ and $\theta$ as parameters for elliptic orbits.

![](images/e00907b6906d68d6384fc5e024f523eecc92759ecbfc3d64433e2a34a67369ae.jpg)  
Fig. 4.13-3. Relation between $\beta$ and $r v ^ { * } / K$ with $e$ and $\theta$ as parameters for hyperbolic orbits.

![](images/9575206f0f08e0ef47588d847713060d65fb27b31dbf264d1c383698e90308ba.jpg)

Substituting these values into Eq. 4.13-5, the energy equation can be written as

$$
\begin{array} { l l } { { \displaystyle { \frac { a } { r } } = \displaystyle { \frac { 1 } { 2 - ( r v ^ { 2 } / K ) } } } } & { { \mathrm { f o r ~ e l l i p t i c ~ o r b i t } } } \\ { { \displaystyle { \frac { a } { r } } = \displaystyle { \frac { 1 } { ( r v ^ { 2 } / K ) - 2 } } } } & { { \mathrm { f o r ~ h y p e r b o l i c ~ o r b i t } } } \end{array}
$$

Finally, we need an equation from which the time elapsed during travel along an orbit can becomputed. For this we examine the equation for the moment of momentum,

$$
r ^ { 2 } \dot { \theta } = h = \sqrt { K r _ { p } ( { 1 + e } ) }
$$

and rearrange it as follows:

$$
\frac { d \theta } { ( 1 + e \cos \theta ) ^ { 2 } } = \frac { \sqrt { K r _ { p } ( 1 + e ) } } { { r _ { p } } ^ { 2 } ( 1 + e ) ^ { 2 } } d t
$$

For $e < 1$ ,thentegraloftheleftideisseePeirehortableofIntgals no. 308 and no. 300),

$$
{ \begin{array} { r l } & { { \int _ { 0 } ^ { \theta } } { \frac { d \theta } { ( 1 + e \cos \theta ) ^ { 2 } } } = { \frac { 1 } { 1 - e ^ { 2 } } } { \Bigl ( } { \frac { - e \sin \theta } { 1 + e \cos \theta } } + { \int _ { 0 } ^ { \theta } } { \frac { d \theta } { 1 + e \cos \theta } } { \Bigr ) } } \\ & { \qquad = { \frac { 1 } { 1 - e ^ { 2 } } } { \biggl [ } { \frac { - e \sin \theta } { 1 + e \cos \theta } } + { \frac { 2 } { \sqrt { 1 - e ^ { 2 } } } } \tan ^ { - 1 } \left( { \frac { \sqrt { 1 - e ^ { 2 } } } { 1 + e } } \tan { \frac { \gamma _ { 2 } } { \log } } \theta \right) { \biggr ] } } \end{array} }
$$

For $e > 1$ ，

$$
\begin{array} { c }  { { \displaystyle { \int _ { 0 } ^ { \theta } \frac { d \theta } { ( 1 + e \cos \theta ) ^ { 2 } } = \frac { 1 } { e ^ { 2 } - 1 } \biggl [ \frac { e \sin \theta } { ( 1 + e \cos \theta ) } } } } \\ { { { - \displaystyle { \frac { 1 } { \sqrt { e ^ { 2 } - 1 } } \ln \left( \frac { \sqrt { e + 1 } + \sqrt { e - 1 } \tan \frac { 1 } { 2 } \theta } { \sqrt { e + 1 } - \sqrt { e - 1 } \tan \frac { 1 } { 2 } \theta } \right) } \biggr ] } } } \end{array}
$$

Replacing $r _ { p }$ in terms of $\boldsymbol { a }$ and $e$ as before, the equation for the time becor

For elliptic orbits $e < 1$ ）

$$
t _ { e } = \frac { a ^ { 3 / 2 } } { \sqrt { K } } \biggl [ 2 \tan ^ { - 1 } \left( \sqrt { \frac { 1 - e } { 1 + e } } \tan { \frac { 1 } { 2 } } \theta \right) - \frac { e \sqrt { 1 - e ^ { 2 } } \sin \theta } { 1 + e \cos \theta } \biggr ]
$$

For hyperbolic orbits( $e > 1$ ）

$$
t _ { h } = \frac { a ^ { 3 } 2 } { \sqrt { K } } \left[ \frac { e \sqrt { e ^ { 2 } - 1 } \sin \theta } { 1 + e \cos \theta } - \ln \left( \frac { \sqrt { e + 1 } + \sqrt { e - 1 } \tan \frac { 1 } { 2 } \theta } { \sqrt { e + 1 } - \sqrt { e - 1 } \tan \frac { 1 } { 2 } \theta } \right) \right]
$$

1 Third revised edition,Ginn & Co.1929.

![](images/f743c437131b5f1cdb5a18a4900cb802dfa0e1e5fd9ca3efe58f3e9c39d5003f.jpg)  
Fig.4.13-4. Dimensionless time for elliptic orbits.

These equations in nondimensional form, $\tau _ { e } = ( t _ { e } \sqrt { K } ) / ( 2 \pi a ^ { 3 } \acute { \acute { z } } )$ and $\tau _ { h } =$ $( t _ { h } \sqrt { K } ) / a ^ { 3 } 2$ ， have been computed and plotted by Augenstein1 and are reproduced here as Figs. 4.13-4 and 4.13-5.

A somewhat simpler expression for the time along the elliptic orbit is available in terms of the eccentric anomaly $\psi$ . For its derivation we need the following relationships:

![](images/f000f13468444cfdaf7edff9cb83704462d6eb7c59c6685f7faf83b22d2cd4f8.jpg)  
Fig. 4.l3-5. Dimensionless time for hyperbolic orbits.

From the equation of the ellipse

we obtain

$$
{ \frac { 1 } { r } } = { \frac { K } { h ^ { 2 } } } ( 1 + e \cos \theta ) = { \frac { 1 + e \cos \theta } { a ( 1 - e ^ { 2 } ) } }
$$

$$
h ^ { 2 } = K a ( 1 - e ^ { 2 } )
$$

From Eq. 4.7-11 for the eccentricity, we have,

$$
2 E = - ( 1 - e ^ { 2 } ) \frac { K ^ { 2 } } { h ^ { 2 } }
$$

From the invariance of the moment of momentum,

$$
r ^ { 2 } { \dot { \theta } } ^ { 2 } = { \frac { h ^ { 2 } } { r ^ { 2 } } }
$$

From the equation cos $\psi = ( a - r ) / a e$ (see Prob. 2, p. 60),

$$
\begin{array} { c c } { { ( a - r ) ^ { 2 } = a ^ { 2 } e ^ { 2 } ( 1 - \sin ^ { 2 } \psi ) } } & { { \mathrm { b y ~ s q u a r i n g } \strut } } \\ { { \strut } } & { { \strut } } \\ { { \dot { r } = a e \dot { \psi } \sin \psi } } & { { \mathrm { b y ~ d i f f e r e n t i a t i n g } \strut } } \end{array}
$$

We now write the total energy equation, Eq. 4.7-7, noting that $v ^ { 2 } = { \dot { r } } ^ { 2 } + ( r \dot { \theta } ) ^ { 2 }$ ,as follows:

$$
\dot { r } ^ { 2 } + ( r \dot { \theta } ) ^ { 2 } - \frac { 2 K } { r } = 2 E
$$

Using Eqs. 4.13-14, 4.13-15, and 4.13-16, this equation becomes

$$
\frac { r ^ { 2 } \dot { r } ^ { 2 } } { K / a } = a ^ { 2 } e ^ { 2 } - ( a - r ) ^ { 2 }
$$

Substituting Eqs. 4.13-17 and 4.13-18 into Eq. 4.13-19b, we obtain

$$
r \dot { \psi } = \sqrt { \frac { K } { a } }
$$

Replacing $r$ from the equation cos $\psi = ( a - r ) / a e$ , and rearranging,

$$
{ \sqrt { \frac { K } { a } } } d t = a { \sqrt { \frac { K } { a ^ { 3 } } } } d t = a ( 1 - e \cos \psi ) d \psi
$$

which integrates to

$$
{ \sqrt { \frac { K } { a ^ { 3 } } } } t = \psi - e \sin \psi + C
$$

The constant of integration $C$ is zero if time is measured from perigee. Equation 4.13-21isthe well-knownKeplerequationforplanetary motion.

# Example 4.13-1

A satellite is launched with the following initial conditions:

$$
\frac { r _ { 0 } { v _ { 0 } } ^ { 2 } } { K } = 1 . 4 0 \qquad \beta _ { 0 } = 2 0 ^ { \circ } \qquad \frac { r _ { 0 } } { R } = 2 . 0
$$

Determine the orbit parameters $e$ and $a / R$ ,and establish the initial position with respect to perigee.

From Eqs. 4.13-2 and 4.13-1

$$
\begin{array} { l c l } { { e = \sqrt { ( 0 . 4 ) ^ { 2 } ( 0 . 9 3 9 ) ^ { 2 } + ( 0 . 3 4 2 ) ^ { 2 } } = 0 . 5 0 8 } } \\ { { } } \\ { { \theta = \tan ^ { - 1 } { \frac { ( 1 . 4 ) ( 0 . 9 3 9 ) ( 0 . 3 4 2 ) } { ( 1 . 4 ) ( 0 . 9 3 9 ) ^ { 2 } - 1 } } = 6 2 ^ { \circ } 2 3 ^ { \prime } } } \end{array}
$$

These values agree with those of the graph of Fig. 4.13-2. From Eq. 4.13-9

$$
\begin{array} { l } { \displaystyle \frac { a } { { r _ { 0 } } } = \frac { 1 } { 2 \mathrm { ~ - ~ } 1 . 4 } = 1 . 6 7 = \frac { a } { R } \frac { R } { { r _ { 0 } } } } \\ { \displaystyle \frac { a } { R } = ( 1 . 6 7 ) ( 2 . 0 ) = 3 . 3 4 } \end{array}
$$

# Example 4.13-2

The satellite orbit of Example 4.13-1 was characterized by $e \ = 0 . 5 0 8$ and $a / R = 3 . 3 4$ ，and its launch point was $r _ { 0 } / R = 2 . 0$ ， $\theta = 6 2 ^ { \circ } 2 3 ^ { \prime }$ If the satellite continues along this orbit to $\theta \ : = \ : 1 5 0 ^ { \circ }$ ,at which time the orbit is to be increased to a value $a / R = 3 . 6 0$ without rotating the apse line, determine the required increment in the velocity and its direction.

We first determine the value of $r v ^ { z } / K$ and $\beta$ before impulse for $\theta \ : = 1 5 0 ^ { \circ }$ and $e \ = 0 . 5 0 8$ . Using subscripts 1 and 2 for before and after impulse, we find from Fig. 4.13-2

$$
{ \frac { r _ { 1 } v _ { 1 } { } ^ { 2 } } { K } } = 0 . 6 8 \qquad v _ { 1 } = 0 . 8 2 3 { \sqrt { \frac { K } { r _ { 1 } } } } \qquad \beta _ { 1 } = 2 4 ^ { \circ }
$$

From Eq. 4.13-9 we have

$$
{ \frac { a } { r _ { 1 } } } = { \frac { 1 } { 2 \ - 0 . 6 8 } } = 0 . 7 5 7 = { \frac { a } { R } } { \frac { R } { r _ { 1 } } } = 3 . 3 4 { \frac { R } { r _ { 1 } } }
$$

Therefore

$$
{ \frac { r _ { 1 } } { R } } = { \frac { 3 . 3 4 } { 0 . 7 5 7 } } = 4 . 4 1
$$

To maintain no rotation of the apse line, the new values of $r _ { 2 } v _ { 2 } { } ^ { 2 } / K$ and $\beta _ { 2 }$ after impulse must lie along the $\theta = 1 5 0 ^ { \circ }$ line in Fig. 4.13-2. (Note that $r _ { 2 } = r _ { 1 }$ for the instantaneous impulse.） The value of $a / R$ after impulse is specified as 3.60, so from Eq. 4.13-9 we have

Therefore

$$
\begin{array} { l } { \displaystyle \frac { a _ { 2 } } { r _ { 1 } } = \frac { a _ { 2 } } { R } \frac { R } { r _ { 1 } } = \frac { 3 . 6 0 } { 4 . 4 1 } = \frac { 1 } { 2 \mathrm { ~ - ~ } ( { r _ { 1 } } { v _ { 2 } } ^ { 2 } / K ) } } \\ { \displaystyle \frac { r _ { 1 } { v _ { 2 } } ^ { 2 } } { K } = 0 . 7 8 0 \mathrm { ~ \quad ~ } v _ { 2 } = 0 . 8 8 2 \sqrt { \frac { K } { r _ { 1 } } } } \end{array}
$$

The new eccentricity and heading angle corresponding to r1v2/K = 0.78 and $\theta = 1 5 0 ^ { \circ }$ is, from Fig. 4.13-2,

$$
e _ { 2 } = 0 . 3 0 \qquad \beta _ { 2 } = 1 1 ^ { \circ }
$$

(Note e2 = 0.77 and β2 = 49° is also a solution but one which requires a larger velocity increment.) Figure 4.13-6 shows a rough sketch of the two orbits.

![](images/85420ba30b057c9b9b0439e8619e5feb86193f18d84a4bd770374a834a29334c.jpg)  
Fig. 4.13-6. Impulsive orbit change without changing apse line.

From the vector diagram of the velocities, the tangential and normal components of the required velocity increments are

$$
\begin{array} { l } { \displaystyle \Delta v _ { t } = ( 0 . 8 8 2 \cos 1 3 ^ { \circ } - 0 . 8 2 3 ) \sqrt { \frac { K } { r _ { 1 } } } = 0 . 0 3 6 \sqrt { \frac { K } { r _ { 1 } } } } \\ { \displaystyle \Delta v _ { n } = ( 0 . 8 8 2 \sin 1 3 ^ { \circ } ) \sqrt { \frac { K } { r _ { 1 } } } = 0 . 1 9 8 \sqrt { \frac { K } { r _ { 1 } } } } \end{array}
$$

and the total velocity increment is

$$
\Delta v = \sqrt { 0 . 0 3 6 ^ { 2 } + 0 . 1 9 8 ^ { 2 } } \sqrt { \frac { K } { r _ { 1 } } } = 0 . 2 0 2 \sqrt { \frac { K } { r _ { 1 } } }
$$

or 0.202 times the circular velocity at a radial distance $r _ { 1 }$

# PROBLEMS

1. If in Example 4.13-2 the impulse of △v = 0.202√K/r1 is applied in the tangential directiondetermine the new orbit parameters $e$ and $a / R$ and the rotation of the apse line.

2. In Example 4.13-2 determine the time required for the satelite to reach $\theta \ : = \ :$ $1 5 0 ^ { \circ }$ from the initial position of $\theta = 6 2 ^ { \circ } 2 3 ^ { \prime }$   
3. In Prob.2 determine the eccentric anomaly $\psi$ corresponding to the two angles and check the time from Kepler's equation.   
4. A satellite is launched at a height of 400 miles with $r v ^ { 2 } / K = 1 . 5 0$ and $\beta _ { 0 } = 1 0 ^ { \gamma }$ Determine the eccentricity e, the orbit parameter a/R,and the position 00.   
5. If in Prob.4 the satellte is given an increment in velocity of $\Delta v = 2 0 0 0$ ft/sec at apogee, determine the new orbit, $e$ ， $a / R ,$ and $\theta$   
6. A satellite is placed into an orbit of $\textit { e } = 0 . 6 0$ at perigee of height $r / R = 1 . 2$ with $v ^ { 2 } = 1 . 6 \bar { v } _ { c } ^ { 2 }$ where $v _ { c }$ is thecircular velocityatthis height. Determine $a / R$ of the orbit and $r / R$ at $\theta = 1 0 0 ^ { \circ }$   
7. If the satellite of Prob. 6 is to reduce the size of the orbit to $a / R = 2 . 2 3$ with-out rotating the line of apse, by an increment of velocity at the position $\theta =$ $1 0 0 ^ { \circ }$ ，determine the new eccentricity and the components of the velocity increment along the tangent and normal to it.

# 4.14 Perturbation of Orbital Parameters

The motion of a space vehicle moving along a specified orbit is completely defined by the following three equations :

$$
\tan \theta = \frac { ( r v ^ { 2 } / K ) \sin \beta \cos \beta } { ( r v ^ { 2 } / K ) \cos ^ { 2 } \beta - 1 }
$$

$$
e ^ { 2 } = { \left( \frac { r v ^ { 2 } } { K } - 1 \right) } ^ { 2 } \mathrm { c o s } ^ { 2 } \beta + \mathrm { s i n } ^ { 2 } \beta
$$

$$
{ \begin{array} { r l } { { \frac { a } { r } } = { \frac { \pm 1 } { 2 - { \frac { r v ^ { 2 } } { K } } } } } & { { } \quad \left\{ + = { \mathrm { e l l i p s e } } \right. } \end{array} }
$$

If at a specified position in the orbit a small impulsive thrust is imparted, in what way willthe orbit parameters be affected? To answer this question we can examine each of the above equations separately.

Equation 4.14-1 indicates that the angular position of the apse line is a function of $r v ^ { 2 } / K$ and $\beta$ ,so that

$$
\theta = f \left( { \frac { r v ^ { 2 } } { K } } , \beta \right)
$$

Differentiating,

$$
d \theta = \frac { \partial f } { \partial \frac { r v ^ { 2 } } { K } } d \frac { r v ^ { 2 } } { K } + \frac { \partial f } { \partial \beta } d \beta
$$

The first term of this equation represents a variation of θ due to a variation in the velocity (i.e., r is not changed during impulsive thrust), holding β constant. This is equivalent to moving the point in Fig. 4.13-2 along the horizontal line. Figure 4.13-2 shows that, if $r v ^ { 2 } / K$ is increased along a horizontal line, then $\theta$ decreases,and vice versa. With larger velocities, the semimajor axis $^ { a }$ will also increase according to Eq. 4.14-3. Figure 4.14-1 illustrates how these orbits change with increasing velocity in the tangential direction. Al orbits will be tangent to the velocity line.

![](images/f59e18007fb33961596b974d6a9f079de65ad49012fb37a4c50c023c522212dc.jpg)  
Fig. 4.l4-l. Orbit variation by tangential thrust.

To evaluate quantitatively the rotation of the apse line due to an incrementin thetangentialvelocity,wecan derentiateEq.414-1,olding $\beta$ constant.

$$
d \theta = \frac { - \sin \beta \cos \beta \cos ^ { 2 } \theta d ( r v ^ { 2 } / K ) } { [ ( r v ^ { 2 } / K ) \cos ^ { 2 } \beta - 1 ] ^ { 2 } }
$$

To reduce this equation further, we first replace the denominator from Eq. 4.14-1

$$
d \theta = \frac { - \sin ^ { 2 } \theta d ( r v ^ { 2 } / K ) } { ( r v ^ { 2 } / K ) ^ { 2 } \sin \beta \cos \beta }
$$

then eliminate sin $\beta$ cos $\beta = ( K / r v ^ { 2 } ) e$ sin $\theta$ (see Eq. 4.9-4) to obtain

$$
d \theta = { \frac { - \sin \theta } { e } } { \frac { d ( r v ^ { 2 } / K ) } { r v ^ { 2 } / K } } = - { \frac { 2 \sin \theta } { e } } { \frac { d v } { v } }
$$

If $v$ is eliminated by Eq. 4.14-3, Eq. 4.14-6 can also be writen as

$$
d \theta = { \frac { - 2 \sin \theta } { e } } { \sqrt { { \frac { r } { K [ 2 - ( r / a ) ] } } } } d v
$$

If next the perturbation of the apse line is desired due to a small change in β, while holding the magnitude of the velocity constant, the change in $\theta$ canbe found from Fig.4.13-2 bymoving thepoint along thevertical line. Such a change corresponds to the second term of Eq. 4.14-4,and the required increment in the velocity vector is $d v = v \ d \beta$

The perturbation in the eccentricity $e$ due to a small increment in the tangential velocity is again available from Fig. 4.13-2 by moving the point along the horizontal(β = constant) line. It can be determined analytically by differentiating Eq. 4.14-2, holding $\beta$ constant. The result is

$$
d e = { \frac { 2 } { e } } \left( 1 - e ^ { 2 } \right) \left( { \frac { a } { r } } - 1 \right) { \frac { d v } { v } }
$$

When the thrust is continuous over a finite length of time, it can be visualized as a series of small impulses, and the orbit change can be obtained by a succession of small changes.

# PROBLEMS

1. Holding $\beta$ constant, integrate the second form of Eq. 4.14-5 and compare the rotation of the apse line in Prob. 4.13-1 with this equation.

2. Show that Eq. 4.14-8 can be expressed in the form $\frac { d e } { e } = 2 \left( \frac { e + \cos \theta } { e } \right) \frac { d v } { v }$ which indicates that $\frac { d e } { e } = 0$ for cos $\theta \ = \ - e$ Verify points on Fig.4.132 for which this is true.

3. According to Fig. 4.13-2, for $\theta$ greater than a certain value there is a value of ${ r v ^ { 2 } } / { K } ,$ $e$ ,and $\beta$ at which d0/de and dv/de are zero. Determine the locus of $r v ^ { 2 } / K ,$ $e$ and $\beta$ for such values.

# 4.15 Stability of Small Oscillations about a Circular Orbit

In a central force system, the circular orbit is always possible at a proper speed when the centrifugal force is balanced by the attractive force.

$$
- r _ { 0 } \dot { \theta } ^ { 2 } = F ( r _ { 0 } )
$$

To determine the stability of such an orbit to a small radial disturbance $r _ { 1 }$ ， we start with the general equation for the radial force

$$
\ddot { r } - r \dot { \theta } ^ { 2 } = F ( r )
$$

and eliminate $\dot { \theta }$ from the condition that the moment of momentum $r ^ { 2 } \dot { \theta } = h$ must be a constant.

$$
\tilde { r } - \frac { h ^ { 2 } } { r ^ { 3 } } = F ( r )
$$

We now let $r = r _ { 0 } + r _ { 1 } = r _ { 0 } [ 1 + ( r _ { 1 } / r _ { 0 } ) ] ,$ so that $\vec { r } = \vec { r } _ { 1 }$ and

$$
{ \frac { h ^ { 2 } } { r ^ { 3 } } } = { \frac { h ^ { 2 } } { { r _ { 0 } } ^ { 3 } } } \Big ( 1 + { \frac { r _ { 1 } } { r _ { 0 } } } \Big ) ^ { - 3 } = { \frac { h ^ { 2 } } { { r _ { 0 } } ^ { 3 } } } \Big ( 1 - { \frac { 3 r _ { 1 } } { r _ { 0 } } } + { \frac { 6 { r _ { 1 } } ^ { 2 } } { { r _ { 0 } } ^ { 2 } } } \cdot \cdot \cdot \Big )
$$

Also expand $F ( r )$ about $r _ { 0 }$ by the Taylor series

$$
{ \cal F } ( r ) = { \cal F } ( r _ { 0 } ) + r _ { 1 } { \cal F } ^ { \prime } ( r _ { 0 } ) + { \textstyle { \frac { 1 } { 2 } } } r _ { 1 } { } ^ { 2 } { \cal F } ^ { \prime \prime } ( r _ { 0 } ) + \cdot \cdot \cdot
$$

Substituting these expansions, ignoring higher-order terms, and noting that $- h ^ { 2 } / r _ { 0 } ^ { \ 3 } = F ( r _ { 0 } )$ ， we arrive at the differential equation for small oscillations about $r _ { 0 }$

$$
\bar { r } _ { 1 } - \biggl [ \frac { 3 } { r _ { 0 } } F ( r _ { 0 } ) + F ^ { \prime } ( r _ { 0 } ) \biggr ] r _ { 1 } = 0
$$

This is a well known second order differential equation for harmonic $- \left[ { \frac { 3 } { r _ { 0 } } } F ( r _ { 0 } ) + F ^ { \prime } ( r _ { 0 } ) \right]$   
stable oscillations we must have

$$
\frac { 3 } { r _ { 0 } } F ( r _ { 0 } ) + F ^ { \prime } ( r _ { 0 } ) < 0
$$

If $\frac { 3 } { r _ { 0 } } F ( r _ { 0 } ) + F ^ { \prime } ( r _ { 0 } ) \dot { > } 0$ , then the solution is an exponentially increasing function of time and the system is unstable.

# Example 4.15-1

Determine the differential equation for small oscillations about a circular orbit when the attractive force is $- K / r ^ { 2 }$ 。

We have $F ( r ) = - K / r ^ { 2 }$ ，Differentiating,

$$
F ^ { \prime } ( r ) = { \frac { 2 K } { r ^ { 3 } } }
$$

The differential equation of small oscillations is then

$$
\ddot { r } _ { 1 } + \frac { K } { { r _ { 0 } } ^ { 3 } } r _ { 1 } = 0
$$

and the solution for an initial disturbance of $r _ { 1 } ( 0 )$ with ${ \dot { r } } _ { 1 } ( 0 ) = 0$ is

$$
r _ { 1 } ( t ) = r _ { 1 } ( 0 ) \cos \sqrt { \frac { K } { { r _ { 0 } } ^ { 3 } } } t
$$

# PROBLEMS

1. For a central force -K/rn,show that a stable circular orbit is possble only for $n < 3$ 。

2. A body is moving ina circular orbit of radius under a central force $- K / r ^ { 2 }$ If the body is given a disturbance $r _ { 1 } ( 0 )$ ,show that the angular speed becomes

$$
{ \dot { \theta } } = { \frac { h } { { r _ { 0 } } ^ { 2 } } } { \left[ { 1 - { \frac { 2 r _ { 1 } ( 0 ) } { r _ { 0 } } } \cos { \sqrt { \frac { K } { { r _ { 0 } } ^ { 3 } } } } t } \right] }
$$

# 4.16 Interception and Rendezvous

Problem 1. (Circular orbits)

We will consider first the problem of two vehicles moving in the same circular orbit r/R,one leading the other by a specified angle Φ12 as shown inFig.4.16-1.We willlet1and2bethepursuerand thepursued

![](images/924cdabe32c9755e06b7bba494fbcf1e4139d708fed311bc0121bd84fb29c628.jpg)  
Fig. 4.16-l. Intercepting and rendezvous on circular orbit.

respectively. Since the orbit is circular, $r { v _ { 1 } } ^ { 2 } / K = 1 , ~ \beta = 0$ for both vehicles, and $\phi _ { 1 2 }$ remains unchanged until altered by thrust.

We wish now for 1 to overtake 2 at some position 3,indicated by angle $\phi _ { 2 3 }$ ， and to rendezvous with it along the circular orbit. What impulsive velocity increments are necessary at 1 and 3?

The problem is solved in the following manner. First the time required for 2 to travel to 3 is determined as

$$
t _ { 2 3 } = \frac { 2 \pi r ^ { 3 / 2 } } { \sqrt { K } } \frac { \phi _ { 2 3 } } { 3 6 0 ^ { \circ } }
$$

Vehicle 1 must travel to 3 on a new orbit which will require the same time. Due to equal radial distances Ol and O3, the perigee for the new orbit must bisect the angle $\phi _ { 1 2 } + \phi _ { 2 3 }$ .Thus $\theta$ measured from perigee to 3 is $\mathcal { Y } _ { 2 } ( \phi _ { 1 2 } + \phi _ { 2 3 } ) ;$ as shown in Fig. 4.16-1.

We must now choose a value of $e$ for the new orbit and, together with 0, determine $n = a / R$ for the time equation. If $e > 1$ , we use the hyperbolic formula.

$$
n = \frac { a } { R } = \left( \frac { r } { R } \right) \left( \frac { a } { r } \right) = \frac { r } { R } \Bigl ( \frac { 1 + e \cos \theta } { e ^ { 2 } - 1 } \Bigr )
$$

From Fig. 4.13-5 we find $\tau _ { h } = t _ { h } ( \sqrt { K / a ^ { 3 } } )$ and compute the time for vehicle 1 to travel from $\theta = 0$ to point 3.

$$
t _ { h } = \tau _ { h } \sqrt { \frac { a ^ { 3 } } { K } } = \tau _ { h } \sqrt { \eta ^ { 3 } } \sqrt { \frac { R ^ { 3 } } { K } } = 8 0 6 \tau _ { h } \sqrt { n ^ { 3 } }
$$

If this value disagrees with $\frac { 1 } { 2 } t _ { 2 3 }$ ,a new $e$ is chosen and the procedure is repeated until agreement is found.

With $e$ and $\theta$ known, $r v ^ { 2 } / K$ and $\beta$ are found from Fig. 4.13--3. Since $\beta$ is zero for the circular orbit, the new $\beta$ is the angle between the two velocity vectors at 3,and the increment in velocity is determined from the vector triangle as

$$
\Delta v = \sqrt { ( v _ { 3 } \cos \beta - v _ { 1 } ) ^ { 2 } + ( v _ { 3 } \sin \beta ) ^ { 2 } }
$$

where $v _ { 1 } = \sqrt { K / r }$ is the circular velocity. Due to symmetry the same $\Delta \boldsymbol { v }$ is applied at 1 to initiate the maneuver,and at 3 to rendezvous, as shown in Fig. 4.16-1.

# Example 4.16-l

Given two vehicles on the same circular orbit of $r / R = 3 . 0$ 、with vehicle 1 lagging vehicle 2 by $8 0 ^ { \circ }$ It is desired for 1 to intercept and rendezvous with 2 at a position 3 which is $4 0 ^ { \circ }$ ahead of 2. Determine the transfer orbit and the required increments of velocity.

We have $\phi _ { 1 2 } = 8 0 ^ { \circ }$ ,and $\dot { \phi _ { 2 3 } } = 4 0 ^ { \circ }$ ， so that perigee for the transfer orbit is $\theta = 6 0 ^ { \circ }$ ,bisecting angle 103. The timefor2 to travel to 3 is

$$
\begin{array} { c } { { t _ { 2 3 } = { \displaystyle \frac { 4 0 ( 2 \pi ) } { 3 6 0 } } \sqrt { \frac { R ^ { 3 } } { K } } ( 3 ) ^ { 3 } \nonumber \strut } } \\ { { = ( 0 . 6 9 8 ) ( 8 0 6 ) ( 5 . 2 0 ) = 2 9 3 0 ~ \mathrm { s e c } } } \end{array}
$$

and the half time is 1465 sec.

As an initial guess, we choose $e \ = 2 . 0$ ,and from Eq. 4.16-2 we find $a / R$ ·

$$
n = \frac { a } { R } = 3 . 0 \left( \frac { 1 + 2 \cos 6 0 ^ { \circ } } { 4 - 1 } \right) = 2 . 0
$$

From Fig.4.13-5, $\tau _ { h } = 0 . 8 0$ for $\theta \ : = \ : 6 0 ^ { \circ }$ and $e = 2 . 0$ The half time of flight from 1 to 3 is then

$$
t _ { h } = 0 . 8 0 ( 2 . 0 ) ^ { 3 } 2 ( 8 0 6 ) = 1 8 2 5 \mathrm { s e c } .
$$

$$
{ } ^ { \mathrm { { * } } } \sqrt { \frac { R ^ { 3 } } { K } } = \sqrt { \frac { [ ( 3 9 6 0 ) 5 2 8 0 ] ^ { 3 } } { ( 1 . 4 0 7 ) 1 0 ^ { 1 6 } } } = 8 0 6 ~ \mathrm { { s e c } }
$$

Sincethisislargerthan1465,theorbit is tooslowand weseek afaster oneby choosing a larger A few trials result in

$$
\begin{array} { l c r } { { e = 3 . 0 \qquad \displaystyle \frac { \alpha } { R } = 0 . 9 3 8 \qquad \displaystyle \frac { r v ^ { 2 } } { K } = 5 . 2 } } \\ { { \tau _ { h } = 2 . 0 \qquad t _ { h } = 1 4 6 5 \mathrm { s e c . } \qquad \displaystyle \beta = 4 6 ^ { \circ } } } \end{array}
$$

![](images/06f3b10b0d9d2c0dba18190436d83da7e9e0c242c7f0d41a823d8f8341f5e04a.jpg)  
Fig. 4.16-2. Vehicle (1) intercepting vehicle (2) at (3).

The circular and hyperbolic velocities at 3 are,

$$
v _ { 1 } = { \sqrt { \frac { K } { r } } } = { \sqrt { \frac { K } { 3 R } } } = { \frac { 1 } { 1 . 7 3 } } { \sqrt { \frac { K } { R } } } = { \frac { 2 5 , 9 3 0 } { 1 . 7 3 } } = 1 5 , 0 0 0 \mathrm { ~ f t / s e c ^ { * } }
$$

$$
v _ { 3 } = { \sqrt { \frac { 5 . 2 } { 3 } \frac { K } { R } } } = 3 4 { , } 1 0 0 \mathrm { f t / s e c }
$$

and the required incremental velocity is

$$
\Delta v = 1 0 ^ { 3 } { \sqrt { ( 2 3 . 7 - 1 5 ) ^ { 2 } + ( 2 4 . 5 8 ) ^ { 2 } } } = 2 6 , 0 0 0 { \mathrm { ~ f t } } / { \mathrm { s e c } }
$$

The geometry of the maneuver is shown in Fig. 4.16-2.

Problem 2. (Elliptic orbits)

If the orbit on which thetwo vehicles are travelingisanellipse,the problem becomes somewhat more complicated because the perigee for the transfer

$$
{ } ^ { \ast } \sqrt { \frac { K } { R } } = { \sqrt { \frac { ( 1 . 4 0 7 ) 1 0 ^ { 1 6 } } { ( 3 9 6 0 ) 5 2 8 0 } } } = 2 5 { , } 9 3 0 \ \mathrm { f t / s e c } .
$$

orbit cannot be found by inspection as in the circular-orbit case. Using the same notation as in Prob. 1, the time required for 2 to reach 3 in Fig. 4.16-3 is shown by the shaded areas subtended by the angle 203. A maneuver at 1 must put vehicle 1 on a new orbit, and its subtended angle 103 must result in the same time. Although angle $\mathbf { i } 0 3 = \phi$ is known, the perigee angle $\theta _ { 1 }$ is not known except in the special case $r _ { 1 } = r _ { 3 }$

![](images/174bbeac9dcb8f0bd17a3d2a1924ca51ebf39e560e69cc35ef20ccc0f68be470.jpg)  
Fig. 4.l6-3. Vehicle (1) intercepting vehicle (2) at (3) on elliptic orbit.

The solution is possible by trial as follows. For the new orbit we have

$$
\frac { r _ { 3 } } { r _ { 1 } } = \frac { 1 + e ^ { \prime } \cos \theta _ { 1 } } { 1 + e ^ { \prime } \cos ( \theta _ { 1 } + \phi ) }
$$

Choosing a value of $\theta _ { 1 }$ ,the eccentricity $e ^ { \prime }$ can be found. $n = \frac { a } { R }$ can be found from $\pm \left( \frac { r _ { 1 } } { R } \right) \left( \frac { 1 + e ^ { \prime } \cos \theta _ { 1 } } { e ^ { \prime 2 } - 1 } \right)$ where $^ +$ isused for $e ^ { \prime } > 1$ aRd $-$ for $e ^ { \prime } < 1$ . The angles $\theta _ { 1 }$ $\theta _ { 1 } + \phi$ ,and $e ^ { \prime }$ will establish $\tau _ { 1 }$ and $\tau _ { 3 }$ in Fig. 4.13-4 or 4.13-5. With the value of $a / R = n$ ,the elapsed time is found as in Prob. 1.

When agreement is established between the two elapsed times,the values of $e ^ { \prime }$ and $\theta _ { 1 }$ for the transfer orbit will result in $r { \tau } ^ { 2 } / K$ and $\beta ^ { \prime }$ , which can be found from Fig. 4.13-2 or 4.13-3. The remainder of the solution is then straightforward.

# Problem 3. (Noncoplanar interception)

Vehicle 2 at t = O is at latitude O and longitude O, traveling in a circular polar orbit of $r / R = 2 . 5$ and headed toward the north. Vehicle l at $t = 0$ is at latitude O and longitude $9 0 ^ { \circ }$ west,and traveling eastward in an equatorial elliptic orbit of $e = 0 . 5 0$ as shown in Fig.4.16-4. The above position of vehicle 1 corresponds to perigee for which $r / R = 1 . 5$ Determine the impulsive velocity increment at 1 to intercept vehicle 2 at 3 when its latitude is $3 0 ^ { \circ } \bf N$

The procedure for the solution of this problem is very much similar to that of Prob.2. The transfer orbit 1, 3 is inclined 30°to the equatorial plane, $r _ { 1 } / R = 1 . 5$ ,and $r _ { 3 } / R = 2 . 5$ ,the angle between $r _ { 1 }$ and $r _ { 3 }$ being $9 0 ^ { \circ }$ Perigee for the transfer orbit is again unknown and its position from r1 is $\theta _ { 1 }$

The elapsed time from 1 to 3 must equal that from 2 to 3, which is

$$
t _ { 2 3 } = { \frac { 3 0 ( 2 \pi ) } { 3 6 0 } } { \frac { ( 2 . 5 R ) ^ { 3 / 2 } } { \sqrt { K } } } = { \frac { \pi } { 6 } } ( 2 . 5 ) ^ { 3 / 2 } ( 8 0 6 ) = 1 6 7 0 ~ { \mathrm { s e c } }
$$

![](images/76dc16d3f12bdfa1a412cf33717f66f556903f7836f966e970b8b19af0a6fa57.jpg)  
Fig. 4.I6-4. Interception for noncoplanar orbits.

From the general equation of the orbit, we have for the two points on the transfer orbit,

$$
{ \frac { r _ { 3 } } { r _ { 1 } } } = { \frac { 2 . 5 } { 1 . 5 } } = 1 . 6 6 6 = { \frac { 1 + e ^ { \prime } \cos \theta _ { 1 } } { 1 + e ^ { \prime } \cos ( \theta _ { 1 } + 9 0 ^ { \circ } ) } }
$$

or

$$
0 . 6 6 6 = e ^ { \prime } ( \cos \theta _ { 1 } + 1 . 6 6 6 \sin \theta _ { 1 } )
$$

Choosing a value of01, the eccentricity of the transfer orbit e' can be found from the above equation. With these two values of $\ell ^ { \prime }$ and $\theta _ { 1 }$ ，we can compute $n$ from

$$
n = \frac { a } { R } = \pm \frac { r _ { 1 } } { R } \bigg ( \frac { 1 + e ^ { \prime } \cos \theta _ { 1 } } { e ^ { \prime 2 } - 1 } \bigg )
$$

where $^ +$ is used for $e ^ { \prime } > 1$ and $-$ for $e ^ { \prime } < 1 ,$

The nondimensional time $\tau _ { h }$ is next found from Fig. 4.13-5 and, with $a / R$ known, the elapsed time is computed and compared to the required time.

As a first choice of $\theta _ { 1 }$ try $3 4 0 ^ { \circ }$ . Equation 4.16-6 gives $e ^ { \prime } = 1 { , } 8 0 3$ and Eq. 4.16-7 gives $n = \frac { a } { R } = 1 . 7 9 5$ From Fig. 4.13-5, $\tau _ { h } = 0 . 1 5$ for $\theta _ { 1 } = 3 4 0 ^ { \circ }$ (same as for $+ 2 0 ^ { \circ }$ and $\tau _ { h } = 0 . 8 0$ for $\theta _ { 3 } = 7 0 ^ { \circ }$ , making a total for the elapsed time of $\tau _ { h } = 0 . 9 5$ . The actual elapsed time is then

$$
t _ { h } = \tau _ { h } \sqrt { \frac { a ^ { 3 } } { K } } = 0 . 9 5 ( 1 . 7 9 5 ) ^ { 3 / 2 } ( 8 0 6 ) = 1 8 4 5 \ \mathrm { s e c }
$$

Since this time is larger than 1670 sec, the orbit is too slow. A few trials result in the following:

$$
\begin{array} { c c l } { { } } & { { \theta _ { 1 } = 3 3 8 ^ { \circ } } } & { { e ^ { \prime } = 2 . 2 0 } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle \frac { a } { R } = 1 . 1 9 } } & { { \tau _ { \theta _ { 1 } } = 0 . 2 9 , } } & { { \tau _ { \theta _ { 3 } } = 1 . 3 1 , } } & { { \tau _ { h } = 1 . 6 0 } } \\ { { } } & { { } } & { { \displaystyle t _ { h } = 1 . 6 0 ( 1 . 1 9 ) ^ { 3 } \tilde { \varepsilon } ( 8 0 6 ) = 1 6 7 5 \mathrm { s e c } } } \\ { { } } & { { \displaystyle \left( \frac { r v ^ { 2 } } { K } \right) _ { 1 } = 3 . 2 6 , } } & { { v _ { 1 } = 1 . 8 \sqrt { \displaystyle \frac { K } { r _ { 1 } } } = 1 . 8 \sqrt { \displaystyle \frac { K } { 1 . 5 R } } = 1 . 4 7 \sqrt { \displaystyle \frac { K } { R } } } } \\ { { } } & { { } } & { { \beta _ { 1 } = - 1 5 ^ { \circ } } } \end{array}
$$

To find the velocity increment,let $x , y , z$ be radial, transverse, and normal to the equatorial plane at point 1. Then the components of $v _ { 1 }$ are (see Fig. 4.16-5):

$$
\begin{array} { c } { { v _ { 1 z } = - v _ { 1 } \sin 1 5 ^ { \circ } = - 0 . 3 8 1 \sqrt { \frac { K } { R } } } } \\ { { { } } } \\ { { v _ { 1 \nu } = v _ { 1 } \cos 1 5 ^ { \circ } \cos 3 0 ^ { \circ } = 1 . 2 3 \sqrt { \frac { K } { R } } } } \\ { { { } } } \\ { { v _ { 1 \tau } = v _ { 1 } \cos 1 5 ^ { \circ } \sin 3 0 ^ { \circ } = 0 . 7 1 1 \sqrt { \frac { K } { R } } } } \end{array}
$$

![](images/6e340d66fd0bceb13c4edbf274bd4e3353ab279270b6fd02b227a22233de2069.jpg)  
Fig416-5ittdat() of Fig. 4.16-4.

Theoriginal velocity isentirely in the $y$ direction,and since theinitial orbit was anelipse with e=05,rv/K=(1+e)=1.5ad = $\sqrt { 1 . 5 K / r _ { p } } = \sqrt { K / R }$

The $_ x$ , y, z components of the velocity increment at 1 are then,

$$
\begin{array} { l } { \displaystyle \Delta v _ { x } = - 0 . 3 8 1 \sqrt { \frac { K } { R } } } \\ { \displaystyle \Delta v _ { y } = 0 . 2 3 \sqrt { \frac { K } { R } } } \\ { \displaystyle \Delta v _ { z } = 0 . 7 1 1 \sqrt { \frac { K } { R } } } \end{array}
$$

# PROBLEMS

1. Two satellites 1 and 2 are in the same circular orbit of $r / R = a / R = 2$ in the same plane, but 2 is leading 1 by the angle $\phi _ { 1 2 } = 3 0 ^ { \circ }$ What velocity incre-ments are necessary to intercept and rendezvous when 2 has traveled through $4 5 ^ { \circ } .$

2. Repeat Prob. 1 when 2 has traveled $9 0 ^ { \circ }$

3. Two satellites 1 and 2 are in the same circular orbit of $a / R = n _ { 0 }$ in the same plane, but 2 is leading 1 by the angle $\phi _ { 1 2 }$ If 1 fires a retrorocket in the tangential direction, show that, in order for the two satellites to intercept after

![](images/c6d21276bac5538c3671fa310be728d65ed2ff92a205a1c954230eb50c1b22e6.jpg)  
Prob.3

1 has completed onerevolution ofits subcircular orbit,thenccessaryincrement in the velocity is

$$
\Delta v = v _ { c } \bigg \{ 1 - \sqrt { 2 - \frac { 1 } { [ 1 - ( \phi _ { 1 2 } / 3 6 0 ) ] ^ { 2 } \mathscr { s } } } \bigg \}
$$

where $v _ { e }$ is the circular orbit velocity.

4. If in Prob. 3 the rocket is fired towards the rear so as to increase the velocity, determine the△v necessary to intercept vehicle2 on the Nth visit to 1. Hint: The time for the Nth visit of vehicle 2 at point 1 is

![](images/5c11bf344a744af370c791a82fcbdbf46697d40d0707ab5dccb40e726af689a9.jpg)  
Prob.4

5. Two satelites 1 and 2 are traveling in the same elliptic orbit in the same plane. The orbit is characterized by $e \stackrel { { } = } { = } 0 . 6 0$ and $a / R \stackrel { \cdot } { = } 3 . 0$ When 1 is at $1 5 0 ^ { \circ }$ 2 is at $1 7 0 ^ { \circ }$ If interception and rendezvous are desired when 2 reaches $\theta \ : = \ : 2 1 0 ^ { \circ }$ ,determine the transfer orbit and the increments in velocity.

![](images/9d9b241cdbb1397f40d8f406f511d8d4f332a103a7a4722c5ebe42928db4f52a.jpg)  
Prob.5

6.Satellte2is leading satellie1 by an angle $\phi _ { 1 2 }$ in an elliptic orbit (see Fig. 4.16-3). To overtake 2 in a decreasingly short time,the eccentricity of the transfer orbit must increase to a large value. Show that in the limit as $e  \infty$ ,the perigee of the transfer orbit can be determined from the equation

$$
\cos \theta _ { 1 } - \frac { r _ { 2 } } { r _ { 1 } } \cos ( \theta _ { 1 } + \phi _ { 1 2 } ) = 0
$$

For fast transfer orbits, the actual $\theta _ { 1 }$ will be close to the above value.

7.Satellte2is traveingeast inanequatorialciruarbitof $a / R = 2$ being at positionloiee $t = 0$ .Satellite1at $t = 0$ is at latitude

$9 0 ^ { \circ }$ andtravelinginaneliptical orbit intheplane,longiude Owith $a / R = 2$ ande=0.30.If it isdesired for1 tointercept2at longitude330°,determine the transfer orbit and the components of the velocity increment. The position of 1 at $t = 0$ corresponds to perigee for the elliptic orbit.

# 4.17 Long-Range Ballistic Trajectories

Since the shortest distance between two points on the surface of a sphere is along a great circle, ballistic trajectories are also considered in the great circle plane. Figure 4.17-1 shows the pertinent geometry of a ballistic trajectory which is an ellipse with the center of the earth as focus. Perigee is then inside the earth while the point of maximum height coincides with apogee.

![](images/650638b3efa9ebb4fa7c9530bec9117a74dd2bbca39ca1440bacf1f24b382998.jpg)  
Fig. 4.l7-l. Geometry of a ballistic trajectory.

Of interest here is the determination of the range $R \phi$ ,the height $H .$ and the time $t _ { b }$ as function of the initial conditions which are $r _ { 0 } = R$ $v _ { 0 }$ and βo. We have at our disposal Eqs. 4.9-7 and 4.9-8 as developed in the initial-value problem of Sec. 4.9. The eccentricity is determined from the equation

$$
e ^ { 2 } = { \bigg ( } { \frac { R { v _ { 0 } } ^ { 2 } } { K } } - 1 { \bigg ) } ^ { 2 } \mathrm { c o s } ^ { 2 } \beta _ { 0 } + \sin ^ { 2 } \beta _ { 0 }
$$

![](images/2680421e6f0b7e1aab67058677d3acbab648e35464bf72cece7b8c1deae50a51.jpg)  
Fig. 4.17-2. Plot of Eq. 4.17-2 for the ballistic trajectory.( $\langle \phi$ versus $\beta _ { 0 }$ with $R v ^ { 2 } / K$ a parameter

Since $\phi / 2 = 1 8 0 ^ { \circ } - \theta _ { 0 }$ ，tan $\theta _ { 0 } = -$ tan $\phi / 2 )$ ， and Eq. 4.9-7 can be written as

$$
\tan { \frac { \phi } { 2 } } = { \frac { - ( R { v _ { 0 } } ^ { 2 } / K ) \sin \beta _ { 0 } \cos \beta _ { 0 } } { ( R { v _ { 0 } } ^ { 2 } / K ) \cos ^ { 2 } \beta _ { 0 } - 1 } }
$$

Figure 4.17-2 is a plot of $\phi$ versus $\beta _ { 0 }$ with $R { v _ { 0 } } ^ { 2 } / K$ as parameter. The height $H$ can be determined from its geometry.

$$
\begin{array} { l } { { r _ { a } = a ( 1 + e ) = H + R } } \\ { {  } } \\ { { { \frac { H } { R } } = { \frac { a } { R } } \left( 1 + e \right) - 1 } } \end{array}
$$

From the equation of the ellipse, we have for $\theta _ { 0 } = 1 8 0 ^ { \circ } - \phi / 2$ ， $r _ { 0 } = R$ ·

$$
\frac { a } { R } = \frac { \left( 1 - e \cos \frac { \phi } { 2 } \right) } { ( 1 - e ) ( 1 + e ) }
$$

which, substituted into Eq. 4.17-3, results in

$$
{ \frac { H } { R } } = { \frac { e } { 1 - e } } { \Big ( } 1 - \cos { \frac { \phi } { 2 } } { \Big ) }
$$

The time of flight is determined by subtracting the time required to go from perigee to $\theta = \theta _ { 0 }$ from half the orbit period and doubling this figure, which from Eq. 4.13-12 is

$$
\begin{array} { l } { { t _ { b } = 2 \bigg ( \frac { \pi a ^ { 3 / 2 } } { \sqrt { K } } - t _ { e } \bigg ) } } \\ { { = \frac { 2 a ^ { 3 / 2 } } { \sqrt { K } } \bigg \{ \pi - \bigg [ 2 \tan ^ { - 1 } \bigg ( \sqrt { \frac { 1 - e } { 1 + e } } \tan { \frac { 1 } { 2 } \theta _ { 0 } } \bigg ) - \frac { e \sqrt { 1 - e ^ { 2 } } \sin \theta _ { 0 } } { 1 + e \cos \theta _ { 0 } } \bigg ] \bigg \} } } \end{array}
$$

# PROBLEMS

1. For $R { v _ { 0 } } ^ { 2 } / K > 1$ ， show that the launching point corresponds to perigee if $\beta _ { 0 } = 0$

2. For a given initial velocity $R { v _ { 0 } } ^ { 2 } / K < 1$ , determine the angle $\beta _ { 0 }$ for maximum range.

3. Relate the maximum range to the optimum heading angle $\beta _ { 0 }$ and specified velocity $R { v _ { 0 } } ^ { 2 } / K .$

4.For a given range show that the minimum required velocity is related to $\beta _ { 0 }$ by the equation $( R v ^ { 2 } / K ) _ { \operatorname* { m i n } } = \frac { 2 \cos 2 \beta _ { 0 } } { 1 + \cos 2 \beta _ { 0 } }$

5. For a range of 50oo miles, determine the optimum angle $\beta _ { 0 }$ the height $H _ { i }$ and the velocity $R { v _ { 0 } } ^ { 2 } / K$

6. For Prob.5, determine the time of flight.

7. Discuss the effect of the earth's rotation on the motion of the ballistic missile.

![](images/9246eab44f95298a34f72558b7b9d42078cf9babfc77729416343eb5331dfdb5.jpg)  
Prob.6

# 4.18 Effect of the Earth's Oblateness

Due to the rotation of the earth from west to east, there is a speed advantage in launching a satellite in a direction with an easterly component. Such an orbit will precess in a westerly direction due to the earth's equatorial bulge, and thus a closed orbit is really not possible. The revolving satellite is like a gyroscope and, as shown in Fig. 4.18-1, its angular momentum vector $\mathbf { h } _ { s }$ perpendicular to its orbit plane and directed towards the northern hemisphere, must slowly revolve about the north polar axis due to the moment exerted by the excess mass over the sphere near the equator. The rate of precession will depend on the orbit angle with respect to the equator and, to a somewhat smaller extent, on the altitude.

The moment due to the equatorial bulge responsible for the precession of the satellite orbit can be determined as follows:

Referring to Fig. 4.18-2 the satellite $m _ { s }$ is attracted towards the mass element $d m$ of the earth according to the equation,

$$
d \mathbf { F } = - { \frac { K m _ { s } d m } { m r ^ { 3 } } } \mathbf { r }
$$

where $K = G m$ and $m$ is the mass of the earth.

![](images/70700e63406a534712fa288ee2bed36aa36e3b3863f2ccc10d837bf95810e680.jpg)  
Fig. 4.l8-l. Precession of orbit plane due to earth's oblateness.

![](images/ede286adca4851702aa0999d65c0c0847acae5420ddb199c672adadadebf1892.jpg)  
Fig. 4.18-2. Satellite $m _ { \mathfrak { g } }$ attracted by element $d m$ of earth.

Resolving r into components,

$$
\begin{array} { l } { { \mathbf { r } = { \mathbf { a } } - { \boldsymbol \rho } } } \\ { = ( a \cos \varphi ) { \mathbf { i } } + ( a \sin \varphi \cos \theta ) { \mathbf { j } } - ( a \sin \varphi \sin \theta ) { \mathbf { k } } - ( x { \mathbf { i } } + y { \mathbf { j } } + z { \mathbf { k } } ) } \end{array}
$$

where $\theta$ is the angle between the orbit plane and the equatorial plane and

$x , y , z$ are the components of $\mathsf { P }$ . The moment becomes,

$$
d \mathbf { M } = \rho \times d \mathbf { F }
$$

$$
\begin{array} { c } { { \displaystyle = \frac { - K m _ { s } d m } { m r ^ { 3 } } \left| \begin{array} { c c } { { \bf i } } & { { \bf j } } \\ { { x } } & { { y } } \\ { { ( a \cos \varphi - x ) } } & { { ( a \sin \varphi \cos \theta - y ) } } \end{array} \right. ( - a \sin \varphi \sin \theta - z } } \\ { { \displaystyle = \frac { K m _ { s } a d m } { m r ^ { 3 } } \left[ ( y \sin \varphi \sin \theta + z \sin \varphi \cos \theta ) \mathbf i - ( x \sin \varphi \sin \theta + z \cos \varphi ) \right. } } \\ { { \displaystyle \qquad \left. - ( x \sin \varphi \cos \theta - y \cos \varphi ) \mathbf k \right] ( 4 . 1 8 - \cos \varphi \cos \varphi ) } } \end{array}
$$

The quantity $1 / r ^ { 3 }$ can be obtained by the following steps:

$$
{ \begin{array} { r l } & { r ^ { 2 } = ( { \mathrm { a } } - { \mathrm {  ~ \ p } } ) \cdot ( { \mathrm { a } } - { \mathrm {  ~ \ p } } ) = a ^ { 2 } + { \mathrm {  ~ \rho } } ^ { 2 } - 2 { \mathsf { \pm } } \cdot { \mathrm {  ~ a ~ } } } \\ & { \quad = a ^ { 2 } + { \mathrm {  ~ \rho } } ^ { 2 } - 2 a \left( x \cos { \varphi } + y \sin { \varphi } \cos { \theta } - z \sin { \varphi } \sin { \theta } \right) } \\ & { { \frac { 1 } { r ^ { 3 } } } = { \frac { 1 } { a ^ { 3 } } } { \Bigl [ } 1 + \left( { \frac { \rho } { a } } \right) ^ { 2 } - { \frac { 2 } { a } } ( x \cos { \varphi } + y \sin { \varphi } \cos { \theta } - z \sin { \varphi } \sin { \theta } ) { \Bigr ] } ^ { - { \frac { 3 4 } { 9 2 } } } } \end{array} }
$$

and its substitution into the moment equation leads to a complicated expression for integration. The expression however can be simplified if $a$ is much larger than $\rho ( x , y , z )$ , in which case we neglect the term $( \rho / a ) ^ { 2 }$ in $1 / r ^ { 3 }$ ,expand the remaining terms by the binomial theorem,and retain only the first terms. We then obtain,

$$
{ \frac { 1 } { r ^ { 3 } } } \cong { \frac { 1 } { a ^ { 3 } } } \left[ 1 + { \frac { 3 } { a } } ( x \cos \varphi + y \sin \varphi \cos \theta - z \sin \varphi \sin \theta ) \right]
$$

and its substitution into the moment equationresults in $M _ { x }$ ， $M _ { y }$ and $M _ { z }$ The $_ x$ component of the moment is,

$$
\begin{array} { c } { { M _ { x } = \displaystyle \frac { K m _ { s } } { m a ^ { 2 } } \bigg [ \int ( y ~ \sin { \varphi } \sin { \theta } + z \sin { \varphi } \cos { \theta } ) ~ d m } } \\ { { \displaystyle + \frac { 3 } { a } \int ( y \sin { \varphi } \sin { \theta } + z \sin { \varphi } \cos { \theta } ) } } \\ { { \displaystyle \times ( x \cos { \varphi } + y \sin { \varphi } \cos { \theta } - z \sin { \varphi } \sin { \theta } ) ] m \bigg ] } } \end{array}
$$

where $\theta$ and $\varphi$ are held constant during integration. It is evident that the firstintegraliszeroduetosymmetryof theoblatespheroidAsoalss

products of the form xy,xz,yz willintegrate to zero due to symmetry. We are then left with the integral,

$$
\begin{array} { l } { { \displaystyle M _ { x } = \frac { 3 K m _ { s } } { m a ^ { 3 } } \sin ^ { 2 } \varphi \sin \theta \cos \theta \displaystyle \int ( y ^ { 2 } - z ^ { 2 } ) d m } } \\ { { \displaystyle \quad = \frac { 3 K m _ { s } } { m a ^ { 3 } } \sin ^ { 2 } \varphi \sin \theta \cos \theta \displaystyle \left[ \displaystyle \int ( x ^ { 2 } + y ^ { 2 } ) d m - \displaystyle \int ( x ^ { 2 } + z ^ { 2 } ) d m \right] } } \\ { { \displaystyle \quad = \frac { 3 K m _ { s } } { m a ^ { 3 } } ( C - A ) \sin ^ { 2 } \varphi \sin \theta \cos \theta } } \end{array}
$$

where $C$ and $A$ are the moments of inertia of the earth about the polar and equatorial axes respectively.

![](images/eb657356d8c93831f579bc4f590d38cc3d61a71812e824e1d576b15f3d567a5b.jpg)  
Fig. 4.18-3. Precession of vector $\mathbf { h } _ { s }$ due to moments $M _ { x }$ and $M _ { y }$

Similarly, the moment about the $y$ axis is,

$$
M _ { y } = { \frac { - 3 K m _ { s } } { m a ^ { 3 } } } ( C - A ) \sin \theta \sin \varphi \cos \varphi
$$

and the moment about the $z$ axis is zero.

$$
M _ { z } = 0
$$

These equations indicate that the moment $M _ { y }$ is negative for $0 \le \varphi \le \pi / 2$ , and positive for $\pi / 2 \leq \varphi \leq \pi ,$ the cycle repeating itself over $\pi$ to $2 \pi$ .Thus the net moment $M _ { y }$ over a complete cycle is zero. The moment $M _ { x }$ ,however, is always positive and varying as $\sin ^ { 2 } \varphi$

Figure 4.18-3 shows the orbit plane, the satellite $m _ { g } ,$ ,and the moments $M _ { x }$ and $M _ { y }$ exerted by the earth on the satelite. To determine the precession of the satellite orbit plane, we note that the angular momentum of the satellite has the value $h _ { s } = m _ { s } a ^ { 2 } \dot { \varphi }$ , which is normal to the orbit plane. The action of the moment $M _ { y }$ on $\mathbf { h } _ { s }$ is oscillatory and zero over a complete cycle,but Mx requires the rate of change of h, over the cycle to be cumulative in the $_ x$ direction.

Measuring the regression of the node line $\psi$ in the equatorial plane, the rate of precession $\dot { \psi }$ is directed along the $- z$ axis with components $\dot { \psi }$ sin $\theta$ in the plane of the orbit, and $\dot { \psi }$ cos $\theta$ normal to it. The component $\dot { \psi }$ sin $\theta$ rotates the vector $\mathbf { h } _ { s }$ to give

$$
\begin{array} { r } { \begin{array} { c } { h _ { s } \dot { \psi } \sin \theta = M _ { x } } \\ { m _ { s } a ^ { 2 } \dot { \varphi } \dot { \psi } \sin \theta = \cfrac { 3 K m _ { s } } { m a ^ { 3 } } ( C - A ) \sin \theta \cos \theta \sin ^ { 2 } \varphi } \end{array} } \end{array}
$$

from which the rate of precession of the orbit plane becomes,

$$
{ \dot { \psi } } = { \frac { 3 K } { \dot { \varphi } m a ^ { 5 } } } \left( C - A \right) \cos { \theta } \ { \sin } ^ { 2 } { \varphi }
$$

Since the moment of inertia of a sphere of radius $R$ is ${ \textstyle \frac { 2 } { 5 } } n \boldsymbol { R } ^ { 2 }$ ,we can introduce $C = { } _ { 5 } ^ { 2 } m { } R ^ { 2 }$ ,where $R$ is the mean radius of earth, and rewrite $\dot { \psi }$ as

$$
{ \dot { \psi } } = { \frac { 6 } { 5 a ^ { 3 } } } { \frac { K } { \dot { \varphi } } } { \binom { R } { a } } ^ { 2 } \left( { \frac { C - A } { C } } \right) \cos \theta \ \sin ^ { 2 } \varphi
$$

Assuming a circular orbit, the angular rate around the orbit, is a constant, $\dot { \varphi } = 2 \pi / \tau$ where $\tau$ is the orbit period equal to

$$
\tau = \frac { 2 \pi a ^ { 3 } \mathit { i } } { \sqrt { K } }
$$

Thus $\varphi$ can be replaced by $( 2 \pi / \tau ) t$ , and the precession angle measured in the equatorial plane per revolution of the satellite becomes,

$$
{ \begin{array} { l } { \displaystyle \psi = { \frac { 6 K } { 5 a ^ { 3 } } } { \left( { \frac { C - A } { C } } \right) } \left( { \frac { R } { a } } \right) ^ { 2 } { \frac { \tau } { 2 \pi } } \cos \theta { \int _ { 0 } ^ { \tau } \sin ^ { 2 } { \frac { 2 \pi } { \tau } } t } d t } \\ { \displaystyle \quad = { \frac { 6 K } { 5 } } { \left( { \frac { C - A } { C } } \right) } \left( { \frac { R } { a } } \right) ^ { 2 } { \frac { \tau ^ { 2 } } { 4 \pi a ^ { 3 } } } \cos \theta } \\ { \displaystyle \quad = { \frac { 6 \pi } { 5 } } { \left( { \frac { C - A } { C } } \right) } \left( { \frac { R } { a } } \right) ^ { 2 } \cos \theta } \end{array} }
$$

The quantity $( C - A ) / C$ for earth is 0.0032, so that the node line of the orbit regresses westward by the amount

$$
\psi = 0 . 0 1 2 1 \left( { \frac { R } { a } } \right) ^ { 2 } \cos \theta
$$

for each revolution of the satelite around the earth.

We can compare this equation with the equation given by Blitzer,2 which is

$$
\psi = 2 \pi J \bigg ( { \frac { R } { r } } \bigg ) _ { \mathrm { } \mathrm { c o s } ~ i } ^ { 2 }
$$

Translated into our notation with $J = 1 . 6 3 7 \times 1 0 ^ { - 3 }$ (see ref. 5) Blitzer's equation is

$$
\psi = 0 . 0 1 0 2 2 { \left( { \frac { R } { a } } \right) } ^ { 2 } \cos \theta
$$

which indicates fair agreement for our approximate equation, Eq. 4.18-13.

The reverse problem to the above is the precession of the earth's polar axis due to the moment exerted by the satelite on the earth. When the satellite is a sizeable mass, such as the moon,its influence is a measurable quantity. The problem of the precession of the earth's polar axis due to the sun and the moon is taken up in Chap. 5, Sec. 15.

# PROBLEMS

1. Examination of Eq. 4.18-7 indicates that no restriction as to the density variation of earth was imposed； however in letting ${ \bf \Pi } _ { 5 } ^ { 2 } m R ^ { 2 } = C$ just before Eq. 4.18-11,uniform density is implied. Indicate what would be changed in Eq. 4.18-12 if the density of the earth varied with the distance from its center.   
2. If the term $( \rho / a ) ^ { 2 }$ in Eq. 4.18-4 is retained to the first term of the binomial expansion, determine the correction to Eq. 4.18-5.   
3. For a satellite launched southeasterly in a circular orbit at an angle of $3 5 ^ { \circ }$ with the equator and at an altitude of 400 miles, determine the regression of the node per revolution taking into account the rotation of the earth during the period.   
4. Show that the attraction of a thin spherical shell of constant density is equal to that of a particle of the same mass concentrated at its center.   
5. Assuming that $( C - A ) / C = N$ differs from zero due to a narrow band around the equator of a perfect sphere, show that the mass of this narrow band must equal,

$$
m = { \frac { 4 N } { 5 \mathrm { ~ - ~ } 6 N } } m _ { 0 }
$$

where $m _ { 0 }$ is the total mass of the sphere plus the narrow band.

# REFERENCES

1. Augenstein, B. W.,"Dynamics Problems Associated with Satelite Orbit Control," Trans.ASME, SeriesB (Nov. 1959),281-288. 2. Blitzer,L., M. Weisfield,and D. Wheelon,"Perturbationofa Satelite Orbit Due to the Earth's Oblateness” J. Appl. Physics 27,No.10(Oct.1956),1141-1149.

3. Ehricke,KrafftA.,"Interplanetary Operations,"Space Technology,John Wileynd Sons, New York (1959), Chapter 8.   
4. Ehricke,Kraft A.,pace light,Vol.1,.vanostrand,Princeton,NJ. (960).   
5.King-Hele, D.G.,and D. M. C. Walker,“Methods for Predicting the Orbits of NearEarth-aeiesJshelearyc.,7No1(Jane9), 2-14.   
6. Moulton,F.R.,Celestial Mechanics,Macmillan Co.,New York (1914).   
7.RamseyA.mcsartImdgeUversityresNework(96) Chapter 1.

# CHAPTER 5

# 5.l Displacement of a Rigid Body

A rigid body can be viewed as a system of particles where the relative distances between particles are fixed. The position ofa rigid body is defined by any three points on it, not in the same straight line.

![](images/f79c1c9cf02de9c8dd6297f991fca4f63dce3b6ae9d0df7fdfcd6f0d3b4bd707.jpg)  
Fig. 5.l-l. Displacement of a rigid body.

The motion of a rigid body can be described by a translation of some reference point O, plus a rotation about some axis through O. Consider three arbitrary noncolinear points 1, 2, 3,in the initial and final positions $1 ^ { \prime }$ ， $2 ^ { \prime }$ ， $3 ^ { \prime }$ , as shown in Fig. 5.1-1. The first point 1 can be brought to $1 ^ { \prime }$ by a translation so that the new position is $1 ^ { \prime } , 2 ^ { \prime \prime } , 3 ^ { \prime \prime }$ . Next, rotate about an axis through $1 ^ { \prime }$ which is perpendicular to the plane $1 ^ { \prime }$ ， $2 ^ { \prime \prime }$ ， $2 ^ { \prime }$ ,bringing $2 ^ { \prime \prime }$ to coincide with $2 ^ { \prime }$ . Finally,rotate about anaxis through $1 ^ { \prime }$ and $2 ^ { \prime }$ ,tobring $3 ^ { \prime \prime \prime }$ to $3 ^ { \prime }$

We will now show Euler's proof that the two individual rotations can be replaced by a single rotation. Draw a unit sphere about point $1 ^ { \prime }$ and where the two rotation axes pierce it, connect the points by a great circle as shown in Fig. 5.1-2. Measure off $\mathcal { Y } _ { 2 } \boldsymbol { \theta } _ { 1 }$ on each side of the great circle at axis 1,drawing two other great circles,and do likewise with angle $\theta _ { 2 }$ at axis 2. Now a rotation of $\theta _ { 1 }$ about axis 1 will bring point $a$ to $b$ ,and a rotation $\theta _ { 2 }$ about axis 2 will bring $b$ back to $a$ .Thus $1 ^ { \prime } a$ is an undisturbed line during rotation $\theta _ { 1 }$ and $\theta _ { 2 }$ ,and therefore it must be the resultant axis of rotation. Note that $1 ^ { \prime } a$ is not in the plane containing the axes of rotation $\theta _ { 1 }$ and $\theta _ { 2 }$ , which again points out the fact that finite rotations do not possess the properties of vectors.

![](images/ae77387e45a2928da4600b2beec121d400c7ee139135a42b215cebae61c3ab24.jpg)  
Fig. 5.l-2. Resultant rotation axis by Euler's proof.

# 5.2 Moment of Momentum of a Rigid Body (About a Fixed Point or the Moving Center of Mass)

Let body axes $x$ ， $y , z$ be attached tothebody with the origin $O$ at any point. The velocity of any point $i$ on the body is then,

$$
\mathbf { v } _ { i } = \mathbf { v } _ { 0 } + { \boldsymbol { \omega } } \times \mathbf { r } _ { i }
$$

where ω is the angular velocity of the body.

The moment of momentum about the origin $O$ of the $_ x$ ， $y$ ， $_ { z }$ ,system is,

$$
\begin{array} { l } { { \displaystyle { \tt h } _ { 0 } = \sum _ { i } { \tt r } _ { i } \times m _ { i } ( { \tt v } _ { 0 } + \omega \times { \tt r } _ { i } ) } } \\ { { \displaystyle \quad = \sum _ { i } { \tt r } _ { i } \times ( \omega \times { \bf r } _ { i } ) m _ { i } - { \tt v } _ { 0 } \times \sum _ { i } m _ { i } { \tt r } _ { i } } } \end{array}
$$

If the reference point $O$ is stationary, $\mathbf { v } _ { 0 } = 0$ ,whereas if $O$ coincides with the center of mass, $\begin{array} { r } { \sum _ { i } m _ { i } \mathbf { r } _ { i } = 0 } \end{array}$ Thus,if $O$ is fixed,oeteoss, the angular momentum is given by the first term of the above equation, which can be expressed by the following integral,

$$
\mathbf { h } _ { 0 } = \int \mathbf { r } \times \left( { \boldsymbol { \omega } } \times \mathbf { r } \right) d m
$$

To evaluate this integral, we note that the first cross product $\omega \times \textbf { r }$ is

$$
\begin{array} { r } { \mathfrak { \omega } \times \mathfrak { r } = \left| \begin{array} { l l l } { \mathbf { i } } & { \mathbf { j } } & { \mathbf { k } } \\ { \omega _ { x } } & { \omega _ { y } } & { \omega _ { z } } \\ { x } & { y } & { z } \end{array} \right| = ( \omega _ { y } z - \omega _ { z } y ) \mathbf { i } + ( \omega _ { z } x - \omega _ { x } z ) \mathbf { j } } \end{array}
$$

Multiplying by dm, we have the $_ { x }$ ， y, z, components of the momentum of dm, as shown in Fig. 5.2-1.

The cross product r X (ω X r) dm is,

$$
\begin{array} { r } { \mathrm {  ~ { \widetilde { \ x } ~ } } ( \omega \times \mathrm {  ~ r ~ } ) d m = \left| \begin{array} { c c c } { \mathrm {  ~ i ~ } } & { \mathrm { \bf j ~ } } & { \mathrm { \bf k } } \\ { x } & { y } & { z } \\ { ( \omega _ { y } z - \omega _ { z } y ) } & { ( \omega _ { z } x - \omega _ { x } z ) } & { ( \omega _ { x } y - \omega _ { y } x ) } \end{array} \right| d m } \\ { = \mathrm { i } [ \omega _ { x } ( y ^ { 2 } + z ^ { 2 } ) - \omega _ { y } ( x y ) - \omega _ { z } ( x z ) ] d m } \\ { + \mathrm { j } [ - \omega _ { x } ( x y ) + \omega _ { y } ( x ^ { 2 } + z ^ { 2 } ) - \omega _ { z } ( y z ) ] d m } \\ { + \mathrm { \bf ~ k } [ - \omega _ { x } ( x z ) - \omega _ { y } ( y z ) + \omega _ { z } ( x ^ { 2 } + y ^ { 2 } ) ] d m } & { ( \mathcal { S } . 2 } \end{array}
$$

which represent the moment about the $_ { x }$ ， y, z, axes of the momentum vectors shown in Fig. 5.2-1. Integrating over the body, we arrive at the x, y, z, components of the moment of momentum of the body.

$$
\mathbf { h } _ { 0 } = h _ { x } \mathbf { i } + h _ { y } \mathbf { j } + h _ { z } \mathbf { k }
$$

We now define the moment of inertia of the body about the $_ { x }$ y,z,axes S

$$
I _ { x } = \int ( y ^ { 2 } + z ^ { 2 } ) d m \quad I _ { y } = \int ( x ^ { 2 } + z ^ { 2 } ) d m \quad I _ { z } = \int ( x ^ { 2 } + y ^ { 2 } ) d m
$$

and the products of inertia as,

$$
I _ { x y } = \int x y d m \quad I _ { x z } = \int x z d m \quad I _ { y z } = \int y z d m
$$

in which case the moment of momentum components along the x, y, z, axes become,

$$
\begin{array} { r l } & { h _ { x } = I _ { x } \omega _ { x } - I _ { x y } \omega _ { y } - I _ { x z } \omega _ { z } } \\ & { h _ { y } = - I _ { x y } \omega _ { x } + I _ { y } \omega _ { y } - I _ { y z } \omega _ { z } } \\ & { h _ { z } = - I _ { x z } \omega _ { x } - I _ { y z } \omega _ { y } + I _ { z } \omega _ { z } } \end{array}
$$

![](images/b77adea2fc333b56a0cd2bf0e367e8af521c64fc3197664d0acbb03565f923b5.jpg)  
Fig. 5.2-l. Components of momentum (w X r) dm.

The moments and products of inertia can beconcisely presented by an inertia dyadic as follows:\*

$$
\mathcal { I } = \left| \begin{array} { r r r } { \mathbf { i } \mathbf { i } I _ { x } } & { - \mathbf { i j } I _ { x y } } & { - \mathbf { i k } I _ { x z } } \\ { - \mathbf { j i } I _ { x y } } & { \mathbf { j j } I _ { y } } & { - \mathbf { j k } I _ { y z } } \\ { - \mathbf { k i } I _ { x z } } & { - \mathbf { k j } I _ { y z } } & { \mathbf { k k } I _ { z } } \end{array} \right|
$$

If we form the dot product of the inertia dyadic with the angular velocity vector

$$
\mathbf { \omega } \omega = \omega _ { x } \mathbf { i } + \omega _ { y } \mathbf { j } + \omega _ { z } \mathbf { k }
$$

we would obtain the moment of momentum

$$
\mathbf { h } = \mathcal { F } \cdot \mathbf { \omega } \mathbf { \omega }
$$

The orderofthe dot product must bepreserved with thefollowing interpretation,

\* See Appendix B.

$$
{ \begin{array} { r c l } { \mathbf { i j } \cdot \mathbf { i } = \mathbf { i } ( \mathbf { j } \cdot \mathbf { i } ) = 0 } \\ { \mathbf { j i } \cdot \mathbf { i } = \mathbf { j } ( \mathbf { i } \cdot \mathbf { i } ) = \mathbf { j } } \end{array} }
$$

# 5.3 Kinetic Energy of a Rigid Body

Consider a rigid body moving through space, and attach to it a set of bodyaxesx,y,z,withitsoiginconciding withitscenterofasen any point r will have a velocity equal to,

$$
\mathbf { v } = \mathbf { v } _ { 0 } + \mathbf { \omega } \times \mathbf { r }
$$

The square of the velocity is obtained by the dot product of its vector,

$$
v ^ { 2 } = \mathbf { v } \cdot \mathbf { v } = v _ { 0 } ^ { ~ 2 } + ( \boldsymbol { \omega } \times \mathbf { r } ) \cdot ( \boldsymbol { \omega } \times \mathbf { r } ) + 2 \mathbf { v } _ { 0 } \cdot ( \boldsymbol { \omega } \times \mathbf { r } )
$$

Thus, the kinetic energy of the body is given as,

$$
\begin{array} { r } { r = \frac { 1 } { 2 } \int v ^ { 2 } d m = \frac { 1 } { 2 }  m v _ { 0 } { } ^ { 2 } + \frac { 1 } { 2 } \int ( \omega \times \mathbf { r } ) \cdot ( \omega \times \mathbf { r } ) d m + \mathbf { v } _ { 0 } \cdot \omega \times \int \mathbf { r } d m  } \\ {  \qquad = \frac { 1 } { 2 }  m v _ { 0 } { } ^ { 2 } + \frac { 1 } { 2 } \int ( \omega \times \mathbf { r } ) \cdot ( \omega \times \mathbf { r } ) d m  \qquad ( 5 . 3 - 2 ) \cdot \mathbf { r } e l l \cdot \mathbf { r }  } \end{array}
$$

where Sr $d m = 0$ for the origin of the body axes coinciding with thecenter of mass. We have thus found that the kinetic energy of translation is determined as if the entire mass is concentrated at the center of mass as a particle, and the second term is the kinetic energy of rotation about an axis ω through the center of mass.

Focusing our attention to the kinetic energy of rotation, we examine the quantity $( \omega \times \bf { \delta r } ) \cdot ( \omega \times \bf { \delta r } )$ . Resolving ω X r into components along the body axes, the dot product is given by the square of the i, j, k components.

$$
\begin{array} { r l } & { ( \omega \times \mathrm {  ~ r ~ } ) \cdot ( \omega \times \mathrm {  ~ r ~ } ) = ( \omega _ { y } z - \omega _ { z } y ) ^ { 2 } + ( \omega _ { z } x - \omega _ { x } z ) ^ { 2 } + ( \omega _ { x } y - \omega _ { y } x ) ^ { 2 } } \\ & { \qquad = \omega _ { \mathrm { { z } } } { } ^ { 2 } ( y ^ { 2 } + z ^ { 2 } ) + \omega _ { y } { } ^ { 2 } ( x ^ { 2 } + z ^ { 2 } ) + \omega _ { z } { } ^ { 2 } ( x ^ { 2 } + y ^ { 2 } ) } \\ & { \qquad - 2 \omega _ { x } \omega _ { z } x z - 2 \omega _ { y } \omega _ { z } y z - 2 \omega _ { x } \omega _ { y } x y } \end{array}
$$

Thus

$$
\begin{array} { r l } & { 2 T _ { \mathrm { r o t . } } = \omega _ { x } ^ { 2 } I _ { x } + \omega _ { y } ^ { 2 } I _ { y } + \omega _ { z } ^ { 2 } I _ { z } - 2 \omega _ { x } \omega _ { z } I _ { x z } - 2 \omega _ { y } \omega _ { z } I _ { y z } } \\ & { \qquad - \ 2 \omega _ { x } \omega _ { y } I _ { x y } } \end{array}
$$

# 5.4 Moment of Inertia about a Rotated Axis

If $I _ { \xi \xi }$ is the moment of inertia of a body about any axis $\xi$ , with angular velocity ω,we can write

$$
2 T _ { \mathrm { r o t . } } = I _ { \xi \xi } \omega ^ { 2 }
$$

Substituting Eq. 5.3-3 into the above equation, we have

$$
\begin{array} { r l } & { I _ { \xi \xi } = \left( \frac { \omega _ { x } } { \omega } \right) ^ { 2 } I _ { x } + \left( \frac { \omega _ { y } } { \omega } \right) ^ { 2 } I _ { y } + \left( \frac { \omega _ { z } } { \omega } \right) ^ { 2 } I _ { z } } \\ & { \phantom { I I } - 2 \left( \frac { \omega _ { x } } { \omega } \right) \left( \frac { \omega _ { z } } { \omega } \right) I _ { x z } - 2 \Big ( \frac { \omega _ { y } } { \omega } \Big ) \left( \frac { \omega _ { z } } { \omega } \right) I _ { y z } - 2 \Big ( \frac { \omega _ { x } } { \omega } \Big ) \left( \frac { \omega _ { y } } { \omega } \right) I _ { x y } } \end{array}
$$

By letting $l _ { \xi x }$ ， $l _ { \xi y }$ ， $l _ { \xi { z } }$ be direction cosines of the vector w or axis $\xi$ with respect to the $_ { x }$ ， $y$ ， $z$ axes, the above equation can be written as

$$
I _ { \xi \xi } = { l _ { \xi x } } ^ { 2 } I _ { x } , + { l _ { \xi y } } ^ { 2 } I _ { y } + { l _ { \xi z } } ^ { 2 } I _ { z } - 2 l _ { \xi x } l _ { \xi z } I _ { x z } - 2 l _ { \xi y } l _ { \xi z } I _ { y z } - 2 l _ { \xi x } l _ { \xi y } I _ { x y }
$$

Equation 5.4-3 can be concisely written in terms of a double summation as follows

$$
I _ { \xi \xi } = \sum _ { \alpha } \sum _ { \beta } l _ { \xi \alpha } l _ { \xi \beta } I _ { \alpha \beta }
$$

where $\propto$ and $\beta$ take on the letters $x$ ， $y , z$ with $I _ { x x }$ interpreted as $I _ { x x } = I _ { x } , I _ { y y } ,$ etc.,and $I _ { \alpha \beta }$ as $- I _ { x y } , - I _ { y z } , - I _ { x z }$ In fact Eq.5.4-4can bechanged slightly to apply to products of inertia as well by the equation

$$
- I _ { \xi \eta } = \sum _ { \alpha } \sum _ { \beta } l _ { \xi \alpha } l _ { \eta \beta } I _ { \alpha \beta }
$$

![](images/5c473864b97f713125536f9f71eca72a72c136d4ba57760bcd747658205f24a4.jpg)  
Fig. 5.4-l. Components of r in two coordinate systems.

The direction cosines l5x to be used in Eq. 5.4-4 or 5.4-5 can be formed most conveniently from the transformation matrix between the two coordinate systems. If the two coordinate systems are x, y, z and x', y', z' with unit vectors i, j, k and i’, j', k',a point in space can be expressed in terms of either coordinate system as

$$
\mathbf { r } = x \mathbf { i } + y \mathbf { j } + z \mathbf { k } = x ^ { \prime } \mathbf { i } ^ { \prime } + y ^ { \prime } \mathbf { j } ^ { \prime } + z ^ { \prime } \mathbf { k } ^ { \prime }
$$

as shown in Fig. 5.4-1.

Scalar multiplication of Eq. 5.4-6 by i, j, and k results in

$$
\begin{array} { r l } & { x = ( \mathbf { i } ^ { \prime } \cdot \mathbf { i } ) x ^ { \prime } + ( \mathbf { j } ^ { \prime } \cdot \mathbf { i } ) y ^ { \prime } + ( \mathbf { k } ^ { \prime } \cdot \mathbf { i } ) z ^ { \prime } } \\ & { y = ( \mathbf { i } ^ { \prime } \cdot \mathbf { j } ) x ^ { \prime } + ( \mathbf { j } ^ { \prime } \cdot \mathbf { j } ) y ^ { \prime } + ( \mathbf { k } ^ { \prime } \cdot \mathbf { j } ) z ^ { \prime } } \\ & { z = ( \mathbf { i } ^ { \prime } \cdot \mathbf { k } ) x ^ { \prime } + ( \mathbf { j } ^ { \prime } \cdot \mathbf { k } ) y ^ { \prime } + ( \mathbf { k } ^ { \prime } \cdot \mathbf { k } ) z ^ { \prime } } \end{array}
$$

which, in matrix notation, is

$$
{ \left[ \begin{array} { l } { x } \\ { y } \\ { y } \\ { z } \end{array} \right] } = { \left[ \begin{array} { l l l } { l _ { x x ^ { \prime } } } & { l _ { x y ^ { \prime } } } & { l _ { x z ^ { \prime } } } \\ { l _ { y x ^ { \prime } } } & { l _ { y y ^ { \prime } } } & { l _ { y z ^ { \prime } } } \\ { l _ { z x ^ { \prime } } } & { l _ { z y ^ { \prime } } } & { l _ { z z ^ { \prime } } } \end{array} \right] } { \left[ \begin{array} { l } { x ^ { \prime } } \\ { y ^ { \prime } } \\ { z ^ { \prime } } \end{array} \right] }
$$

Thus when the transfer matrix between the two coordinates is known, the elements of the matrix are the direction cosines.

We note further that the equation for the kineticenergy can beexpressed by the dot product of the angular velocity and the moment of momentum,

$$
2 T = \mathbf { \boldsymbol { \omega } } \cdot \mathbf { \boldsymbol { h } } _ { 0 }
$$

Since $\mathbf { h } _ { 0 }$ can be expressed in terms of the momental dyadic (see Eq.5.2-9), the above equation becomes

$$
2 T = \infty \cdot \mathcal { I } \cdot \omega
$$

Again letting ${ \mathcal { I } } = \mathbf { A B }$ , the above double dot product is interpreted as

$$
( { \bf \omega } \circ \cdot { \bf A } ) ( { \bf B } \cdot { \bf \omega } \omega )
$$

which is a product of two scalars and, therefore, a pure number.

# 5.5 Principal Axes

We define the principal axes of the body, 1, 2, 3, as those about which the products of inertia vanish, and let $A$ ， $B$ $C$ ,be the moment of inertia about the 1, 2, 3 axes respectively. The moment of inertia about the instantaneous axes of rotation $\xi ,$ in terms of $A$ ， $B$ ， $C$ then becomes,

$$
{ I _ { \xi } = A { l _ { \xi 1 } } ^ { 2 } + B { l _ { \xi 2 } } ^ { 2 } + C { l _ { \xi 3 } } ^ { 2 } }
$$

where lg1,ls2, l are the direction cosines of the vector $\boldsymbol { \omega }$ ,oraxis $\xi$ and the principal axes 1, 2,3. Since the axes 1,2, 3 are fixed in the body, $A$ ， $B$ ， $C$ are constants. However,as the instantaneous axis $\xi$ is moved, $l _ { \xi 1 }$ ， $l _ { \xi 2 }$ ， $l _ { \xi 3 }$ change, and so will the value of $\mathbf { \Omega } _ { \mathcal { L } }$ about the $\xi$ axis.

If we let $\rho = 1 / \sqrt { I _ { \xi } } ,$ and lay off $\boldsymbol { \rho }$ and $\xi$ ,and do this for every orientation of the instantaneous axis $\xi$ ， we would obtain an ellipsoid of inertia.

Dividing the above equation by $I _ { \xi }$ and noting that $l _ { \xi 1 } / \sqrt { I _ { \xi } } = l _ { \xi 1 } \rho = x$ l2p=y,lp =z are theprincipal coordinates of theequation for the ellipsoid of inertia,Eq.5.5-1 becomes

$$
A x ^ { 2 } + B y ^ { 2 } + C z ^ { 2 } = 1
$$

# PROBLEMS

1. For the slender uniform bar of length / and mass $m$ oriented in the position shown, determine the moment and product of inertia about each of the axes.

![](images/bcfbd68fd8489a963a973d28f65b35301fb09f4ca1a8ab919913d0119e1ac74b.jpg)  
Prob.1

2. If the barof Prob.1isrotated about the $z$ axis with angular velocity $\omega$ ， determine the angular momentum about the three axes.

3. While getting into position for takeoff, a small aeroplane with two bladed propellers turns about its vertical axis as shown.Determine the x,y， z components of the angular momentum of the left propeller. Assume the propeller to be a uniform slender rod of length l.

![](images/b827d08b72e53be6f88ddddcb5a20ecbfb0d275d5600c3cd79ca0646747088b0.jpg)  
Prob. 3

4. Find the moments of inertia of six 10-1b weights arranged symmetrically on the x, y, z axes as follows: $x = \pm 5 , y = \pm 2 , z = \pm \bar { 6 }$ 5.Find the moment of inertia of the configuration of Prob.4 about an axis through the origin and the point (1,2, 2).

6. A thin disk of radius R is mounted on a shaft which deviates by an angle α from the normal. Choose orthogonal axes through the shaft and disk and determine the moment and product of inertia about each axis.   
7. Determine the moment of inertia about the $\xi$ ， $\eta$ ， $\zeta$ axes for a cube of sides $c$ ， if $\zeta$ is placed along the diagonal and the $\xi$ $\eta$ axes normal to $\zeta$ are rotated into a position such that $I _ { \xi } = I _ { \eta }$ What will be the direction cosines of $\xi$ and $\eta$ so placed ?   
8. Determine the length of a uniform cylinder of radius R such that its principal moments of inertia are equal.   
9. If $A$ ， $_ B$ $C$ are principal moments of inertia of a given body, show that $A + B$ is larger than $C$   
10. A space vehicle makes a landing on a hillside with velocities $v _ { z }$ and $v _ { x }$ just before impact as shown. If a leg strikes a boulder and the vehicle pivots about this point, show that the angular velocities immediately after impact are

$$
\begin{array} { l } { { \dot { \theta } _ { x } = - \frac { m \bar { y } } { { I _ { x } } } v _ { z } } } \\ { { \dot { \theta } _ { y } = \frac { m \bar { y } { I _ { y z } } - m \bar { z } { I _ { z } } } { { I _ { y } I _ { z } } - { I _ { y z } } ^ { 2 } } v _ { x } } } \\ { { \dot { \theta } _ { z } = \frac { m \bar { y } } { { I _ { z } } } v _ { x } + \frac { { I _ { y z } } } { { I _ { z } } } \frac { m \bar { y } { I _ { y z } } - m \bar { z } { I _ { z } } } { { I _ { y } I _ { z } } - { I _ { y z } } ^ { 2 } } v _ { x } } } \end{array}
$$

where the $_ x$ y， $z$ coordinates are oriented with $z$ vertical, $x$ parallel to the horizontal velocity $v _ { x } ,$ and $y$ horizontal.

![](images/99bc44e8e0ffa2f5523bfc8c95406cee5617ff37f49de427687ef8f20c64aa48.jpg)  
Prob.10

11. Assume that the moments and products of inertia about the x, y, z axes are known. Determine the equation for the inoment of inertia about the 5,n,5axes by noting that p²=p²-2 =p² -(p·i）,=i +/j +zk, and $\begin{array} { r } { I _ { \xi \xi } = \mathrm { ~ f ~ } \rho _ { \xi } ^ { 2 } \ d m , } \end{array}$ etc.

![](images/a7affed094ca790ba54ff2b1e0db19f1412703235af813c4939d6ac497d6d3f2.jpg)  
Prob. Il

12. In the same manner as in Prob. 11, determine the equation for the product of inertia $I _ { \xi \eta } , I _ { \xi \zeta } ,$ and $I _ { \eta \zeta }$ 。

13. An airplane of mass $M$ and moments of inertia $A$ ， $B$ ， $C$ about principal axes drops at a uniform rate of $V$ ft/sec,and at the same time spins at the rate of $\mathrm { i 0 ~ \ r p m }$ about an axis which makes equal angles with the three principal axes.Determine its total kinetic energy.

14. Show that the moment of inertia of three equal masses $1 2 0 ^ { \circ }$ apart as shown in the sketch is equal to $\% m l ^ { 2 }$ about any axis in its plane.

![](images/ec4305885404b96a2017f679a50e9d6d7fb2b7eb03a3ea23f6deea648cc90a60.jpg)  
Prob.14

15.With the $_ { x }$ ， $y$ , z axes passing through the center of massof a body shown in the sketch, prove that the moment of inertia about any axis n through the origin is

$$
\begin{array} { c } { { I _ { n } = \displaystyle \sum _ { i } m _ { i } [ x _ { i } { } ^ { 2 } ( 1 - n _ { x } ^ { 2 } ) + y _ { i } { } ^ { 2 } ( 1 - n _ { y } ^ { 2 } ) + z _ { i } { } ^ { 2 } ( 1 - n _ { z } ^ { 2 } ) } } \\ { { \nonumber } } \\ { { - \ 2 ( x _ { i } y _ { i } n _ { x } n _ { y } + x _ { i } z _ { i } n _ { x } n _ { z } + y _ { i } z _ { i } n _ { y } n _ { z } ) ] } } \end{array}
$$

where ${ \bf { n } } = n _ { x } { \bf { i } } + n _ { y } { \bf { j } } + n _ { z } { \bf { k } }$ is a unit vector along the axis $\mathbf { n }$ Hint: Start

$$
I _ { n } = \sum _ { i } m _ { i } ( \mathbf { r } _ { i } \times \mathbf { n } ) \cdot ( \mathbf { r } _ { i } \times \mathbf { n } ) = \sum _ { i } m _ { i } [ r _ { i } ^ { 2 } - ( \mathbf { r } _ { i } \cdot \mathbf { n } ) ^ { 2 } ]
$$

![](images/04f312fdde6b6343fa628a38fffaa4f6e17bcf30b21d2660aed2140384f7a2f0.jpg)  
Prob.15

16. Starting with $I _ { n ^ { \prime } } = \sum _ { i } m _ { i } [ ( \mathbf { r } _ { 0 } + \mathbf { r } _ { i } ) \times \mathbf { n } ] \cdot [ ( \mathbf { r } _ { 0 } + \mathbf { r } _ { i } ) \times \mathbf { n } ]$ derive the equation for the moment of inertia about an axis $n ^ { \prime }$ parallel to $n$ ， and displaced by the vector $\mathbf { r } _ { 0 }$

17. By actually multiplying, using the rule ij $\mathbf { \nabla } \cdot \mathbf { i } = 0$ ij $\begin{array} { r } { { \bf \nabla } \cdot \bf j = i , } \end{array}$ etc., show that $\boldsymbol { \mathsf { h } } = \mathcal { I } \cdot \boldsymbol { \mathsf { \omega } }$

18. Show that

$$
\dot { \boldsymbol { \mathcal { I } } } = [ \dot { \boldsymbol { \mathcal { I } } } ] + \omega \times \boldsymbol { \mathcal { I } } + \left| \begin{array} { c c } { \mathbf { i } \omega \times \mathbf { i } I _ { x } } & { - \mathbf { i } \omega \times \mathbf { j } I _ { x y } - \mathbf { i } \omega \times \mathbf { k } I _ { x y } } \\ { - \mathbf { j } \omega \times \mathbf { i } I _ { x y } } & { \mathbf { j } \omega \times \mathbf { j } I _ { y } } & { - \mathbf { j } \omega \times \mathbf { k } I _ { y z } } \end{array} \right|
$$

where

$$
[ \dot { \mathcal { I } } ] = \left| \begin{array} { c c c } { \mathfrak { i } \dot { \mathfrak { i } } I _ { x } } & { - \mathfrak { i } \dot { \mathfrak { j } } I _ { x y } } & { - \mathfrak { i } \mathbf { k } I _ { x z } } \\ { - \mathfrak { j } \mathfrak { i } I _ { x y } } & { \mathfrak { j } \dot { \mathfrak { j } } I _ { y } } & { - \mathfrak { j } \mathbf { k } \dot { I } _ { y z } } \\ { - \mathbf { k } \mathfrak { i } \dot { I } _ { x z } } & { - \mathbf { k } \mathfrak { j } I _ { y z } } & { \mathbf { k } \mathbf { k } \dot { I } _ { z } } \end{array} \right|
$$

19.Determine the total time derivative

$$
\frac { d \mathbf { h } } { d t } = \boldsymbol { \mathcal { S } } \cdot \dot { \boldsymbol { \omega } } + \dot { \boldsymbol { \mathcal { S } } } \cdot \boldsymbol { \omega }
$$

with respect to inertial coordinates,and show that it is equal to

$$
\frac { d \mathbf { h } } { d t } = \mathcal { I } \cdot \dot { \boldsymbol { \omega } } + [ \dot { \mathcal { I } } ] \cdot \boldsymbol { \omega } + \boldsymbol { \omega } \times \mathbf { h }
$$

# 5.6 Euler's Moment Equation

We have shown previously that the moment about the mass center is equal to the time derivative of the moment of momentum about this point. With $\mathbf h _ { c } = h _ { x } \mathbf i + h _ { y } \mathbf j + h _ { z } \mathbf k$ ，we can differentiate, noting that i, j,k rotate with the body.

$$
\begin{array} { r l } & { \mathbf { M } _ { c } = [ \dot { \mathbf { h } } _ { c } ] + \boldsymbol { \omega } \times \mathbf { h } _ { c } } \\ & { \qquad = ( \dot { h } _ { c a } \dot { \mathbf { i } } + h _ { v } \mathbf { j } + h _ { z } \mathbf { k } ) + \boldsymbol { \omega } \times \mathbf { h } _ { c } } \end{array}
$$

The cross product ω X h can easily be visualized as the rotation of the vectors hi, hj, hk,due to ωx, W, ω,as shown in Fig. 5.6-1. Thus,by adding vectors along the x,y,z directions,the above equation becomes,

$$
\begin{array} { c } { { { \bf M } _ { o } = M _ { x } { \bf i } + M _ { v } { \bf j } + M _ { z } { \bf k } } } \\ { { { \mathrm { } } } } \\ { { = ( h _ { x } + \omega _ { y } h _ { z } - \omega _ { z } h _ { y } ) { \bf i } + ( h _ { y } + \omega _ { z } h _ { x } - \omega _ { x } h _ { z } ) { \bf j } + ( h _ { z } + \omega _ { x } h _ { y } - \omega _ { y } { \bf k } ) } } \end{array}
$$

![](images/f58faf695f9226c62f6b5d843b1c88d8393dea8a7a76228116a61eacff9f28a9.jpg)  
Fig. 5.6-l. Components of moment of momentum and their rate of change.

The component equations,known as Euler's moment equations,are

$$
\begin{array} { r } { M _ { x } = h _ { x } + \omega _ { y } h _ { z } - \omega _ { z } h _ { y } } \\ { M _ { y } = h _ { y } + \omega _ { z } h _ { x } - \omega _ { x } h _ { z } } \\ { M _ { z } = h _ { z } + \omega _ { x } h _ { y } - \omega _ { y } h _ { x } } \end{array}
$$

where the $_ x$ y, $z$ axes with the origin coinciding with the center of mass rotate with angular velocity $\boldsymbol { \omega }$

Equation $5 . 6 \AA - 1$ or 5.6-3 for the moment is applicable to any coordinate system with a fixed origin or a moving origin coinciding with the center of mass. The angular velocity $\boldsymbol { \omega }$ is that of the coordinate stemand the axes are fixed in the body, the moments and products of inertia are constant.

For a body of revolution with moments of inertia $A$ ， $A$ ， $C$ about principal axes, $A$ about any transverse axis is the same, and so we might choose a set of transverse axes rotating at a speed different from that of the body without introducing a variable moment of inertia with time. We can for instance use the node axis system 5, n, &,in which case the moments are,

$$
\begin{array} { r } { M _ { \xi } = h _ { \xi } + h _ { \zeta } \omega _ { \eta } - h _ { \eta } \omega _ { \xi } } \\ { M _ { \eta } = h _ { \eta } + h _ { \xi } \omega _ { \zeta } - h _ { \zeta } \omega _ { \xi } } \\ { M _ { \zeta } = h _ { \zeta } + h _ { \eta } \omega _ { \xi } - h _ { \xi } \omega _ { \eta } } \end{array}
$$

These equations are known as Euler's modified equations.

# 5.7 Euler’s Equation for Principal Axes

With the origin of the body axes coinciding with the center of mass, we can orient the $_ x$ ， $y$ ， $z$ axes to coincide with the principal axes 1,2,3 of the body to eliminate the products of inertia terms in the moment of momentum expressions. We then have,

$$
h _ { 1 } = A \omega _ { 1 } \qquad h _ { 2 } = B \omega _ { 2 } \qquad h _ { 3 } = C \omega _ { 3 }
$$

where $A , B , C ,$ , are principal moments of inertia which are constant since 1,2, 3 are fixed in the body. The moment equations are then,

$$
\begin{array} { r } { M _ { 1 } = A \dot { \omega } _ { 1 } + \omega _ { 2 } \omega _ { 3 } ( C - B ) } \\ { M _ { 2 } = B \dot { \omega } _ { 2 } + \omega _ { 1 } \omega _ { 3 } ( A - C ) } \\ { M _ { 3 } = C \dot { \omega } _ { 3 } + \omega _ { 1 } \omega _ { 2 } ( B - A ) } \end{array}
$$

which are called the Euler's equations for principal axes. The general solution of these equations is diffcult, and in the sections to follow we will consider some special cases which enable an analytical solution.

# 5.8 Body with $A \ = \ B$ and Zero External Moment (Body Coordinates)

We will consider here a cylindrical disk with axis 3 normal to the circular face, as shown in Fig. 5.8-1.

The moment of inertia about the three body axes are,

Euler's equation then becomes,

$$
\begin{array} { r } { A \dot { \omega } _ { 1 } + ( C - A ) \omega _ { 2 } \omega _ { 3 } = 0 } \\ { A \dot { \omega } _ { 2 } - ( C - A ) \omega _ { 1 } \omega _ { 3 } = 0 } \\ { C \dot { \omega } _ { 3 } = 0 } \end{array}
$$

From the third of these equations, we conclude that $\omega _ { 3 }$ must be a constant.

$$
\omega _ { 3 } = n
$$

Making the substitution,

$$
n \left( { \frac { C - A } { A } } \right) = \lambda
$$

![](images/8216a55ac69ab918bd7be64b132f812971a67df27095a994133a0b5420d98d79.jpg)  
Fig. 5.8-l. Body of revolution with principal axes 1, 2, 3.

the first two equations can be written as,

$$
\begin{array} { r l r } { \dot { \omega } _ { 1 } + \lambda \omega _ { 2 } = 0 } & { { } } & { } \\ { \dot { \omega } _ { 2 } - \lambda \omega _ { 1 } = 0 } \end{array}
$$

Multiplying the first equation by $\omega _ { 1 }$ and the second by ${ \boldsymbol { \omega } } _ { 2 }$ ,and adding, we obtain the equation,

or

$$
\begin{array} { r l } { { \omega _ { 1 } \dot { \omega } _ { 1 } + \omega _ { 2 } \dot { \omega } _ { 2 } = 0 } } & { { } } \\ { { } } & { { } } \\ { { \omega _ { 1 } { } ^ { 2 } + \omega _ { 2 } { } ^ { 2 } = { \omega _ { 1 2 } } ^ { 2 } = \mathrm { c o n s t a n t } } } \end{array}
$$

Thus the magnitude of the resultant angular velocity vector w is a constant.

$$
\omega = \sqrt { { \omega _ { 1 } } ^ { 2 } + { \omega _ { 2 } } ^ { 2 } + { \omega _ { 3 } } ^ { 2 } } = \sqrt { { \omega _ { 1 2 } } ^ { 2 } + n ^ { 2 } } = \mathrm { c o n s t a n t }
$$

Since there is no moment acting on the body, we have,

$$
\mathbf { M } = \dot { \mathbf { h } } = 0
$$

which requires that the angular momentum vector h be a constant, fixed in