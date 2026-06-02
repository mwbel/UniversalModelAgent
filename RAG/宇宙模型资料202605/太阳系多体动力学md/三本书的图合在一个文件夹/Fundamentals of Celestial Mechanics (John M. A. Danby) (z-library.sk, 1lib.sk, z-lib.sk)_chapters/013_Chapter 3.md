# Chapter 3

# Introduction To Vectorial Mechanics

# 3.1Forces as Vectors

Mechanics deals with the effects of forces, and the first step in this chapter is to establish that forces are vectors.Certainly forces have magnitudes and directions, so we have to show that they can be added or resolved according to thevector law.It can be shown experimentally that a force $P$ can be resolved ina direction makingθ with its line of action,and that the resultant is Pcos0; so,forces can be resolved and therefore added as vectors. Alternatively we can accept the properties of the triangle of forces to be experimentally proved.That is、if three forces acting through a point are in equilibrium, then it is possible to construct a triangle with sides parallel to the lines of action of the forces and with lengths proportional to their magnitudes.This is precisely equivalent to thevector law of addition.

Forces are localized vectors,and they must always be treated as such. Expressions such as “resolving a force” or “the moment ofa force” follow from theirvector definitions.

# 3.2Basic Definitions

The mass of a body is a measure of the amount of material in the body. A unit of mass can be defined in terms of a definite volume of some standard substance; for instance, the gram is the mass of a cubic centimeter of water. At some point on the Earth's surface the force exerted on a body of mass m is mg,where $g$ is constant for that place,due mostly to the Earth's gravity. mgis the weight of the body.On the Moon the body would weigh less,but its mass would remain the same;hence mass, and not weight, is the fundamental quantity. Two masses can be compared at some place by comparing their weights,so there is no difficulty in allotting a measure to any particular mass. Mass is, of course,a scalar quantity. In the work immediately following, it wil be convenient to assume that bodies are point masses;a point mass has its entire mass concentrated at a geometrical point.

The product mv of the mass and velocity of a body is the linear momentum of that body. This is a vector. (A discussion of the system of reference with respect to which v is measured is given in the following section.)

Let a mass m be at r with respect to some origin O. Then the product r X mv is the angular momentum about O of the mass. (This is sometimes called “moment of momentum."） Angular momentum is a vector of which the modulus is seen (from Section 2.5)to be 2m times the areal velocity with respect to O.Angular momentum will usually be used in preference to areal velocity.

The kinetic energy of m is $\scriptstyle { \frac { 1 } { 2 } } \gamma \gamma ^ { 2 }$ ,a scalar.

If a constant force P acts on a particle that suffers a displacement r, then the work done by the force is P·r, a scalar. If P is not constant, the work done in moving from A to B is compounded from the infinitesimal displacements dr along the curve AB,so that the total is

$$
\bar { \mathcal { W } } _ { A \bar { B } } = \int _ { A } ^ { B } \mathbf { P } \cdot d \mathbf { r }
$$

integrated along the curve.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0040/ocr/images/c72311a43745ce5a2ff0974ca42629d970d80425257f88d983849a7f86724598.jpg)  
Figure 3.1

Power is the rate of doing work.The work done by $\pmb { \Sigma }$ in $\mathfrak { a }$ displacement dr is $P \cdot d x$ which can be written as $\mathbb { P } \cdot ( d \mathbb { r } / d t ) d t$ so that the rate of doing work is $\mathbb { P } \cdot \mathbb { v }$ ascalar.

These quantities can be measured in units of length,mass,and time. These units will often be taken in this text as the centimeter, the gram,and the second, oras $^ { 6 6 } \mathfrak { C }$ g.s.”units.The unit of force is the dyne; it produces unit acceleration in unit mass.The unit of work is the erg,measured by one dyne moving its point of application through one centimeter; and so on. There is no ambiguity in denoting all these by “c.g.s. units."

It is always important to bear in mind the dimensions of these quantities. If L,M,and T stand for length,mass, and time, then speed has the dimensions $\pmb { \bar { z } } / \pmb { \bar { z } }$ kinetic energy has the dimensions $\sqrt { 2 } \pmb { \mathscr { L } } ^ { 2 } / \pmb { \mathscr { L } } ^ { 2 }$ ,and so on. It is a useful check to make sure that all the terms in any equation have the same dimensions. For instance, it is all right to equate kinetic energy and work,but not work and power.

The force exerted by a body or system of bodies at some point is taken to mean the force that the system would exert on a particle of unit mass placed at that point.This is strictly “force per unit mass,”and the dimensions must be altered accordingly. The phrase “per unit mass” ought, then, to be included also wherever quantities such as energy or momentum occur, but in practice there need be no ambiguity ifit is not always used.

Let $\mathbf { P }$ be such a force, varying with $\pmb { \tau }$ ；then it constitutes a field of force. An important type of field of force is one where $\mathbb { P } ( \mathbf { r } )$ is the gradient of a scalar function of r. This is expressed conventionally as

$$
\pmb { \mathrm { p } } = - \nabla \pmb { \mathrm { V } }
$$

where $V _ { \{ \pmb { z } \} }$ is the potential of the field. It should be noted that we get the same feld of force if an arbitrary constant is added to $\pmb { \zeta }$ .If such a potential function exists, then the field is said to be conseruative. In such $\hat { \pmb { c } }$ case it is often easier to work with $\pmb { \bar { \gamma } }$ ,a scalar, than with $\pmb { \mathcal P }$ For a conservative field (3.2.1） becomes

$$
\begin{array} { l } { \displaystyle { \mathcal { W } _ { A B } = - \int _ { A } ^ { B } \nabla V \cdot d { \mathbf { r } } } } \\ { \displaystyle \quad = - \int _ { A } ^ { B } \nabla V \cdot \hat { \pmb { \tau } } d s } \\ { \displaystyle \quad = - \int _ { A } ^ { B } \frac { d V } { d s } d s \quad [ \mathrm { b y ~ ( 2 . 8 . 1 ) } ] } \\ { \displaystyle = V ( A ) - V ( B ) . } \end{array}
$$

So, the work done in going from $A$ to $\mathcal { B }$ depends only on the positions of the ends of the path and not on the shape of the path itself. This is one of the most important properties of $\mathtt { a }$ conservative field,and it is possible to define it by this property.

Considera mass m on the Earth at A. If it is lifted toa point $\mathcal { B }$ the work performed by the gravitational attraction of the Earth is negative, and equal t $\pmb { \mathscr { m } } ^ { \sharp } \pmb { \mathscr { s } } _ { A B }$ But whoever lifts it works against the gravitational attraction of the Earth, and performs positive work of amount $- m \sqrt [ 3 ] { 3 } = 0$ Now, if the mass descends to $\pmb { A }$ ,energy equal to this amount of work is released and is available to be turned into any form of energy such as kinetic energy, heat, etc. Hence the mass has energy by virtue of its position, and this is known as potential energy. It should not be confused with “potential", since it has different dimensions.

Usually it is possible to choose the arbitrary constant in the potential such that $\pmb { \bar { \nu } }$ tends to zero at great distances. In this case the potential at $A$ is equal to the work done by the attracting system in moving a unit mass from $A$ to infinity. The dimensions of potential are therefore work per unit mass.

In many texts the potential is defined as the negative value of that given by (3.2:2)；usually when it is defined in this way it is called the force function. In practice it is easy to get the signs confused, and, regardless of the definition, when the potential finds its way into an actual equation,it is wise to check that its sign makes sense. For Newtonian attraction, V is negative and the force function is positive. An example of positive V is the potential of the field due to the repulsive force experienced by particles in the tail of a comet as a result nf the radiation pressure from the Sun.

The potential function must be single-valued. For example,if V=-ku,in two-dimensional polar coordinates, then for any point V has an infinite number ofvalues. The gradient of V gives a force that is k/r in the transverse direction, but if a point moves around the origin in a closed curve, the work done in one revolution is 2πk,and not zero. If frictional forces, such as air resistance, are present, then the feld will not be conservative. However,in nearly all the work in this text we shall be concerned with conservative fields.

The surfaces V = constant are called level surfaces. No work is done in a displacement over a level surface. From Section 2.8 we see that the line of action of the force through any point is perpendicular to the level surface through that point.

# 3.3Newton's Laws of Motion

The bridge between the kinematics of a particle and the forces acting on it is provided by Newton's three laws of motion. These are:

1.Every particle continues in a state of rest or uniform motion in a straight line unless it is compelled by some external force to change that state.   
2.The rate of change of the linear momentum of a particle is proportional to the force applied to the particle and takes place in the same direction as that force.   
3.The mutual actions of any two bodies are always equal and oppositely directed.

These laws can be introduced as fundamental laws,without proof,and followed up mathematically. To ignore possible laboratory verifications makes mechanics appear somewhat abstract; but all we shall say here is that the laws can be reasonably verifed.A full discussion is given in most standard texts on mechanics.

Newton's first law demands some sort of reference system with respect to which the “uniform velocity” can be measured. If we have one such reference system, then any other that is not accelerated with respect to the first system will do equally well for the application of Newton's laws. Hence we have the usual stipulation that the axes must be “nonaccelerated.” The trouble arises when we look for the first suitable reference system,and this involves discussion that is out of place in an elementary text. Here we shall adopt a common way out,working backwards and defining such a system as one with respect to which the first law holds. Axes rotating with the Earth are not suitable in principle (before Newton's laws can be applied.to motion with respect to these, the Coriolis forces have to be imposed),although they are adequate for many laboratory experiments. Similarly, it may not be reasonable to assume that a suitable set of axes can be moving through space with the solar system,since such a set is undoubtedly accelerated with respect to the galaxy; but the effects of this are negligible and produce no practical difficulties.

Newton's first law clears the decks in showing whethera force is in action ornot.If there is no net force acting on a body, its equation of motion must be in the form

$$
{ \bf r } = { \bf r } _ { \vartheta } + { \bf v } t ,
$$

and,conversely, if this is its equation of motion, then there is no net force acting onthe body.For example,from Kepler's frst law we can say that there must be some force acting on the planets.It is Newton's second law that enables us to investigate the force quantitatively.

The second law can be used as a proof that forces are vectors. But this makes the definition of a force unnecessarily abstract. If the mass of the body remains constant, the second law can be put in the familiar form:

$$
{ \vec { \mathbf { z } } } = { \mathfrak { m } } { \ddot { \mathbf { z } } } .
$$

Masses will be constant in the work in this text,but (3.3.1） would not be applicable, say, to the motion of a meteor burning up in the atmosphere. Some of the consequences of this will be considered in the following section.

Newton's third law must always be borne in mind where forces are concerned. For instance,the Earth exerts a gravitational pull on the Moon; so, the Moon must exert a precisely equal and opposite pull on the Earth. It is only because the Earth is some eighty times more massive than the Moon that the kinematical effects on the Earth are less noticeable.

# 3.4 The Laws of Energy and Momentum

Consider Newton's second law in the form:

$$
\begin{array} { r } { \mathfrak { P } = \frac { d \left( \mathfrak { N } \mathfrak { v } \mathfrak { v } \right) } { d \mathfrak { i } } . } \end{array}
$$

This is equivalent to

$$
\mathfrak { P } a \mathfrak { t } = a \mathfrak { f } ( \mathfrak { N } , \mathfrak { v } )
$$

so that

$$
\int \mathbb { P } \bar { d } \dot { \varepsilon } = \eta \bar { \varepsilon } + \eta \bar { \varepsilon } \mathrm { a r s t a r i } \dot { \bar { \varepsilon } } .
$$

This is the equation of linear momentum. In particular, if no net force is acting onaparticle,then its linear momentum is constant.

Now consider $\Im \Re \{ 3 . 4 . \Im \}$ We have

$$
{ \begin{array} { r } { { \boldsymbol { \mathbf { r } } } \times { \dot { \boldsymbol { \mathbf { P } } } } = { \boldsymbol { \mathbf { r } } } \times { \frac { d { \left( m \mathbf { v } \right) } } { d t } } } \\ { = { \frac { d \left( { \boldsymbol { \mathbf { r } } } \times m \mathbf { v } \right) } { d t } } } \end{array} }
$$

since (dr/dt) ×v = v × v = 0. This means that the moment of the forces acting on a particle is equal to the rate of change of the angular momentum of the particle. In particular,if the moment is zero (when the line of action of the resultant of the forces passes through the origin), then the angular momentum is constant. Conversely, if the angular momentum is constant (so that the motion takes place ina plane and the law of areas is obeyed), then the resultant force passes through the origin. We have seen that some force must be acting on the planets to account for their curved paths; now we see that the force must be directed toward the Sun.

The work done in moving $\mathbf { P }$ through dr is

$$
{ \begin{array} { r l } & { \mathbf { P } \cdot d \mathbf { r } = { \frac { d ( m \mathbf { v } ) } { d t } } \cdot d \mathbf { r } } \\ & { \qquad = { \frac { d ( m \mathbf { v } ) } { d t } } \cdot { \frac { d \mathbf { r } } { d t } } d t } \\ & { \qquad = \mathbf { v } \cdot { \frac { d ( m \mathbf { v } ) } { d t } } d t . } \end{array} }
$$

If $\pmb { \mathcal { W } }$ is a constant, this can be integrated to give

$$
W _ { A B } = \int _ { A } ^ { B } \mathbb { P } \cdot d \mathbf { { r } } = { \textstyle { \frac { 1 } { 2 } } } \mathtt { m } v _ { B } ^ { 2 } - { \textstyle { \frac { 1 } { 2 } } } \mathtt { m } v _ { A } ^ { 2 } .
$$

By (3.2.3) this can be written as

$$
\begin{array} { r } { V ( A ) - V ( B ) = \frac { 1 } { 2 } v _ { B } ^ { 2 } - \frac { 1 } { 2 } v _ { A } ^ { 2 } } \end{array}
$$

since $\gamma$ is derived from a function of force per unit mass. So the changes in kinetic and potential energy are equal. The energy integral (3.4.5),can always be written down at once in any problem where $\pmb { \ V }$ exists,without recourse to the equation of motion. /

Any of these three equations may be more useful in a problem than the equation of motion (3.3.1),and it is always as well to consider their merits before embarking on the solution to a problem. This applies in particular to the energy integral.

Consider motion with respect to axes that are rotating with constant angular velocity $\omega$ about the $\boldsymbol { z }$ -axis.Ifa mass m is acted on bya force $\mathcal { P }$ itsmotion with respect to the rotating axes will be given by

$$
{ \boldsymbol { \mathbb { P } } } = m [ { \ddot { \bar { x } } } + 2 \omega { \hat { \mathbf { z } } } \times { \dot { \bar { { \mathbf { z } } } } } \cdot { \boldsymbol { \mathbb { z } } } \cdot { \boldsymbol { \mathbb { z } } } ^ { 2 } { \hat { \mathbf { z } } } \times ( { \hat { \mathbf { z } } } \times { \bar { { \mathbf { r } } } } ) ]
$$

where equation (2.7.2) has been applied twice. Let $\mathfrak { r }$ have components $\mathbf { z }$ along $\boldsymbol { \mathcal { O } } \boldsymbol { z }$ and $\pmb { \rho }$ at right angles to $\boldsymbol { \vartheta } \boldsymbol { z }$ ；then

$$
{ \mathfrak { r } } = z { \hat { \mathfrak { z } } } + { \mathfrak { p } }
$$

and

$$
\mathbf { P } = m [ \tilde { \mathbf { r } } + 2 \omega \hat { \mathbf { z } } \times \dot { \mathbf { r } } - \omega ^ { 2 } \rho ] .
$$

Multiply scalarly by $\dot { \pmb { \tau } }$ then, since $\boldsymbol { \rho } \cdot \dot { \boldsymbol { \tau } } = \boldsymbol { \rho } \cdot \dot { \boldsymbol { \rho } }$ ，

$$
\mathbb { P } \cdot \dot { \mathbb { r } } = m \big [ \ddot { \mathbb { r } } \cdot \dot { \mathbb { r } } - \omega ^ { 2 } \rho \cdot \dot { \rho } \big ] .
$$

f $\pmb { \mathcal P }$ arises from a potential $\pmb { \gamma }$ ,described with respect to the rotating axes, then we get the modified energy integral

$$
\begin{array} { r } { \bar { \gamma } - \frac { 1 } { 2 } \omega ^ { 2 } \rho ^ { 2 } \div \frac { 1 } { 2 } \bar { \dot { \Sigma } } ^ { 2 } = \mathrm { c o n s t a n t } , } \end{array}
$$

which is the same as the usual energy integral for the motion of a particle in a field of potential

$$
\begin{array} { r } { \Psi - \frac { 1 } { 2 } \omega ^ { 2 } \rho ^ { 2 } . } \end{array}
$$

This is the modified potential. The term $- \textstyle { \frac { 1 } { 2 } } \omega ^ { 2 } \rho ^ { 2 }$ is the rotational potential.

Some uses of the equations of motion will now be demonstrated by considering their application to five simple problems.

# 3.5Simple Harmonic Motion

A particle moves in a straight line under the action of a force that varies directly with the distance from some fixed point. If this point is taken as the origin and $\mathscr { Z }$ is the distance measured from it, the force per unit mass can be written as $- \hbar ^ { 2 } z$ ,and the equation of motion is

$$
\ddot { z } = - \mathbb { k } ^ { 2 } x .
$$

The field is conservative, with potential $\scriptstyle { \frac { 3 } { 2 } } \displaystyle { \overrightarrow { k } } ^ { 2 } \displaystyle { \overrightarrow { x } } ^ { 2 }$ , so that the energy integral is

$$
{ \textstyle \frac { 1 } { 2 } } \dot { x } ^ { 2 } + { \textstyle \frac { 1 } { 2 } } \dot { \kappa } ^ { 2 } x ^ { 2 } = \mathtt { c o a s t a n t } ,
$$

where the constant must be positive, so that it can be put equal to $\scriptstyle { \frac { 1 } { 2 } } k ^ { 2 } a ^ { 2 }$ Writing (3.5.2) in the form:

$$
\frac { d x } { ( x ^ { 2 } - x ^ { 2 } ) ^ { 1 / 2 } } = k d t
$$

we find the solution for the motion to be

$$
{ \mathfrak { x } } = a \cos \{ { \mathfrak { k } } { \mathfrak { k } } \div { \mathfrak { b } } \} ,
$$

where $\pmb { \alpha }$ and $b$ are arbitrary constants.

Aninspection of the energy integral yields several properties of the motion. It is symmetrical about the origin; it is determined by the speed at the origin; and it represents finite oscillations whatever the initial speed may be.

# 3.6Motion in a Uniform Field Subject to Resistance Proportional to the Velocity

Near the Earth's surface there is a uniform feld of force,-gz, where z is the unit vector pointing vertically upward. Between certain limits of speed the air resistance is proportional to the velocity. The equation of motion is then

$$
m \ddot { \bar { \bf z } } = - m g \hat { \bar { \bf z } } - m \bar { k } { \bf v } .
$$

The forces are not conservative,so we cannot use the energy integral in the form of (3.4.5). The motion obviously takes place in a vertical plane (for there is no force to cause any deviation from such a plane) and there is no advantage in using vectors. Let position in the plane of motion be specified (x,z),where the x-axis is horizontal; then the resolution of (3.6.1) gives

$$
\ddot { z } = - \dot { k } \dot { x } ,
$$

and

$$
\ddot { z } = - g - \hbar \dot { z } .
$$

(3.6.2) can be put into the form:

$$
\frac { \dot { a } } { d \dot { \bar { \varepsilon } } } \{ \dot { x } e ^ { \dot { \bar { \kappa } } \dot { t } } \} = 0 ,
$$

$$
{ \dot { z } } = A e ^ { - k \ t }
$$

and

$$
x = - \frac { A } { \vec { \kappa } } e ^ { - \vec { \kappa } \vec { \tau } } + B ,
$$

where $A$ and $B$ are arbitrary constants. Therefore the speed along the $\pmb { \mathcal { X } }$ -axis, which is the horizontal speed, tends to zero,and x, the horizontal range, tends to a finite limit as $\ddagger$ tends to infinity.

A similar solution of (3.6.3) yields

$$
\frac { d } { d t } \{ \dot { z } e ^ { \dot { \kappa } t } \} = - g e ^ { \dot { \kappa } t } ,
$$

S0

$$
\dot { \boldsymbol { z } } = - \frac { \boldsymbol { g } } { \boldsymbol { \xi } } + \boldsymbol { C } \boldsymbol { e } ^ { - \boldsymbol { \kappa } t }
$$

and

$$
z = - \frac { g } { k } t - \frac { C } { k } e ^ { - i k t } + i D .
$$

If the particle is initially rising, $\dot { z }$ is positive; it will vanish when

$$
e ^ { - \bar { \kappa } \tau } = \frac { g } { C \bar { \kappa } } ,
$$

or when

$$
z = - \frac { g } { k ^ { 2 } } \log { \left( \frac { k C } { g } \right) } - \frac { g } { k ^ { 2 } } + D .
$$

The particle will then start to descend and will have $\hat { \bf \Phi }$ limiting speed $- \{ g / k \}$ · The energy at any point is given by

$$
\begin{array} { r } { \frac { 1 } { 2 } \{ \dot { x } ^ { 2 } \div \dot { z } ^ { 2 } \} + g z , } \end{array}
$$

and an evaluation of this willshow how much energy is lost at any stage, owing to the air resistance.

# 3.7 Linear Motion in an Inverse Square Field

The approximation to a uniform field is valid only near the Earth's surface. Farther away we must usea force

$$
- \frac { \hat { k } ^ { 2 } } { g ^ { 2 } } \hat { \mathbf { z } }
$$

per unit mass,where $\nsim$ is the distance from the Earth's center. General motion in this field will be considered later;for the moment we shall only discuss motion in the $z$ -direction. Since the motion is linear, it is pointless to use vectors.

The field is conservative with potential $- ( k ^ { 2 } / r )$ The energy integral is therefore

$$
\dot { z } ^ { 2 } = \frac { 2 k ^ { 2 } } { z } - \frac { 2 k ^ { 2 } } { z _ { 0 } } \div v _ { 0 } ^ { 2 }
$$

where $\mathtt { \mathtt { \mathtt { A } } } _ { \mathtt { 0 } }$ and ${ \mathfrak { C } } 0$ are the position and speed when $t = 0$ Important information can be found merely by applying the condition that the right-hand side of (3.7.1) must not be negative. There are three cases to be considered. We suppose that ${ \mathfrak { r } } _ { \mathfrak { d } } > { \mathfrak { 0 } }$

1.If $v _ { 0 } ^ { 2 } < 2 \lambda ^ { 2 } / z _ { 0 }$ ，there will be some finite distance, $z _ { 1 }$ ，at which $\dot { z }$ will vanish;at this distance the particle will turn and start to descend.   
2.If $v _ { 0 } ^ { 2 } > 2 k ^ { 2 } / z _ { 0 }$ ， $\dot { z }$ will never vanish but will tend to some finite value as $z$ tends to infinity; the particle will always continue to move away and will never return.   
3.If $v _ { \Updownarrow } ^ { 2 } = 2 \bar { \kappa } ^ { 2 } / z _ { 0 }$ ，then $\dot { z } \  \ \emptyset$ as $z  \infty$ This critical value of $v _ { 0 }$ is known as the velocity of escape (we should in this text write “speed of escape,”but this use of the word “velocity”is too well established). It is of fundamental importance in many problems; one of the most topical is that of achieving the speed necessary for $\gtrdot$ rocket to escape completely from the Earth.

To calculate the velocity of escape from $\curvearrowleft$ the value of $k ^ { 2 }$ must be known. This is the product of the mass of the attracting body and the constant of gravitation. However, we can find the velocity of escape from the surface of the Earth from a knowledge of the Earth's radius (taken to be 6360 km) and the value of $g$ at the surface of the Earth, for the latter is $\mathtt { k } ^ { 2 }$ divided by the square of.the Earth'sradius.Taking ${ g = 9 8 1 }$ c.g.s.units, the velocity of escape is

$$
( 2 \times 9 8 1 \times 6 3 6 0 \times 1 0 ^ { 5 } ) ^ { 1 / 2 } = \mathrm { { 1 1 . 2 } \times \mathrm { { 1 0 } ^ { 5 } ~ c m / s e c } } .
$$

From a point above the surface of the Earth, the velocity of escape would, of course,be less.

The velocity of escape is often referred to as the velocity from infinity, since it is the speed which a particle, starting from rest at infinity,would acquire on reaching $z _ { 0 }$

The full solution to the problem can be found by integrating (3.7.1). Cases $1 , 2$ and3 must be treated separately. Here we shall consider only the first. Let $\dot { z } = 0$ when $z = z _ { 1 }$ ；then (3.7.1) can be written as ·.

$$
\begin{array} { c } { { \displaystyle \frac { d z } { d t } = \pm \left\{ 2 k ^ { 2 } \left( \frac { 1 } { z } - \frac { 1 } { z _ { 1 } } \right) \right\} ^ { 1 / 2 } } } \\ { { = \pm \left( \frac { 2 k ^ { 2 } } { z _ { 1 } } \right) ^ { 1 / 2 } \left( \frac { z _ { 1 } - z } { z } \right) ^ { 1 / 2 } . } } \end{array}
$$

$\mathtt { T a e } + \alpha \mathrm { r } - \mathrm { s i g n }$ is to be taken when the particle is receding from or approaching the origin.Writing the equation as

$$
\frac { z d z } { ( z z _ { 1 } - z ^ { 2 } ) ^ { 1 / 2 } } = \pm k \left( \frac { 2 } { z _ { 1 } } \right) ^ { 1 / 2 } d \pm
$$

we have, on integration,

$$
- ( z z _ { 1 } - z ^ { 2 } ) ^ { 1 / 2 } + \frac { z _ { 1 } } { 2 } \sin ^ { - 1 } \left( \frac { 2 z - z _ { 1 } } { z _ { 1 } } \right) = \pm k \pm \frac { \left( 2 \right) } { z _ { 1 } } ^ { 1 / 2 } + \mathrm { \ c o n s t a n t . }
$$

Applying the condition $z = z _ { 0 }$ when $\sharp = \emptyset$ we have

$$
\begin{array} { r l r } {  { \frac { z _ { 1 } } { 2 } \{ \sin ^ { - 1 } ( \frac { 2 z - z _ { 1 } } { z _ { 1 } } ) - \sin ^ { - 1 } ( \frac { 2 z _ { 0 } - z _ { 1 } } { z _ { 1 } } ) \} + ( z _ { 1 } z _ { 0 } - z _ { 0 } ^ { 2 } ) ^ { 1 / 2 } } } \\ & { } & \\ & { } & { \quad \quad - ( z _ { 1 } z - z ^ { 2 } ) ^ { 1 / 2 } = \pm k \bar { t } ( \frac { 2 } { z _ { 1 } } ) ^ { 1 / 2 } . } \end{array}
$$

# 3.8Foucault's Pendulum

In 1851 the French scientist Foucault devised an experiment,which could be performed under laboratory conditions, to demonstrate the Earth's rotation. A simple pendulum was suspended from the dome of the Pantheon in Paris and it was shown that the plane in which it swung was slowly rotating. This phenomenon is really due to the Earth's (and the observer's) rotating under the pendulum.

Let the point of suspension of the pendulum be $o$ ,and let the bob be at $\mathcal { P }$ Let $\mathbb { P } \mathbb { P } = \mathbb { r } ,$ where $\mathfrak { F }$ is constant. Now let $\hat { \mathbf { k } }$ point along CO,where $\boldsymbol { C }$ is the center of the Earth. Let us assume that $\gamma$ is very small compared with the radius of the Earth, $\curvearrowleft$ ; then the forces acting on the bob, of mass m, are the tension in the string, acting along $\tt P G$ , and gravity $\sin \theta$ acting along $- \hat { \mathbf { k } }$ These can be written

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0040/ocr/images/1e95f8d9c36dc8d1ebdfd60efe61b36563fbd14ac4e503090b5e67556034ae0b.jpg)  
Figure 3.2

The equation of motion with respect to nonrotating axes fixed in space is found by equating $m \{ d ^ { 2 } \pmb { \mathrm { r } } / d ^ { 2 } \pmb { \mathrm { t } } ^ { 2 } \}$ with the above forces. But to write down the equation of motion observed with respect to axes moving with $o$ , we must apply the Coriolis forces derived in (2.7.5). In this example $\omega ^ { 2 }$ is so small compared with that it may be ignored. If $d / d / t$ now applies to the motion observed from $o$ ： we have

$$
\frac { d ^ { 2 } \pmb { \mathrm { r } } } { d t ^ { 2 } } + 2 \omega \hat { \bf z } \times \frac { d \pmb { \mathrm { r } } } { d t } = - g \hat { \bf k } - \frac { \pmb { \mathrm { r } } } { m } \hat { \bf \xi } .
$$

The normal equation of motion for the simple pendulum is found by putting $\omega = 0$ To solve (3.8.1）,eliminate $\mathfrak { T }$ by multiplying through vectorially by $\tilde { \Xi } \times$

We get

$$
\hat { \boldsymbol { \mathfrak { x } } } \times { \frac { d ^ { 2 } \boldsymbol { \mathfrak { x } } } { d t ^ { 2 } } } + 2 \omega \hat { \boldsymbol { \mathfrak { x } } } \times \left( \hat { \boldsymbol { \mathfrak { z } } } \times { \frac { d \boldsymbol { \mathfrak { x } } } { d t } } \right) = - g \hat { \boldsymbol { \mathfrak { x } } } \times \hat { \boldsymbol { \mathbf { k } } } .
$$

Since dr/dt = O,r·(dr/dt) = 0,and the second term on the left-hand side red1ices to

$$
- 2 \omega \hat { \mathbf { x } } \cdot \hat { \mathbf { z } } \frac { d \mathbf { r } } { d \hat { t } } = - 2 \omega \sin \lambda \frac { d \mathbf { r } } { d \hat { t } } ;
$$

where $\lambda$ is the latitude of $o$ The amplitude of the swing is assumed to be small. So we have

$$
\hat { \bf x } \times \frac { \dot { a } _ { \bf x } ^ { 2 } } { \dot { a } \dot { \bf z } ^ { 2 } } - 2 \omega \sin \lambda \frac { \dot { d } { \bf x } } { \dot { d t } } = - g \hat { \bf x } \times \hat { \bf k } .
$$

From the known properties of the motion we are looking for a solution that includes a uniform rotation about $\hat { \bf k }$ Consider axes rotating with angular velocity w'k,and let δ/dt represent the rate of change with respect to these axes. $w ^ { f }$ is constant, and is so small that $\omega ^ { i 2 }$ and $\omega { \omega } ^ { \beta }$ can be neglected (the justification for this will appear shortly). (3.8.2) becomes

$$
{ \hat { \mathbf { r } } } \times \left( { \frac { \partial ^ { 2 } \mathbf { r } } { \partial t ^ { 2 } } } + 2 \omega ^ { i } { \hat { \mathbf { k } } } \times { \frac { \partial \mathbf { r } } { \partial t } } \right) - 2 \omega \sin \lambda { \frac { \partial \mathbf { r } } { \partial t } } = - g { \hat { \mathbf { r } } } \times { \hat { \mathbf { k } } } .
$$

Rearranging this we get

$$
\hat { \bf r } \times \frac { \partial ^ { 2 } \hat { \bf x } } { \partial t ^ { 2 } } - 2 ( \hat { \bf r } \cdot \hat { \bf k } \omega ^ { \prime } + \omega \sin \lambda ) \frac { \partial \hat { \bf x } } { \partial t } = - g \hat { \bf r } \times \hat { \bf k } .
$$

During the motion we assume that the pendulum is never far from the vertical so that $\hat { \mathbf { x } } \cdot \hat { \mathbf { k } } \simeq 1$ Then, if

$$
v ^ { \prime } = - v \sin \lambda ,
$$

the equation reduces to that of a simple pendulum. Hence the motion observed from $o$ is that of a simple pendulum rotating with angular velocity $- \hat { \tilde { \mathbf { k } } } \omega \sin \lambda$ ，

# 3.9 The Equation of Motion of a Rocket, Subject Only to Its Own Propulsion

We include this section to illustrate the careful treatment required for problems that involve changing mass.A rocket traveling in vacuo is accelerated by the high-velocity expulsion of & small part of its mass. With respect to axes fixed in space, we have the situations before and after the expulsion that are shown in Figure 3.3.

The relative speed at which the expelled matter leaves the rocket is $\xi + \mathbb { Y }$ and for a time $\vec { \mathcal { Q } } \vec { \mathcal { L } }$ a thrust $a ^ { 3 } \ + \pmb { \mathscr { V } } _ { i }$ is exerted on the rocket so that the force propelling it forward is

$$
( \bar { U } + \bar { \mathcal { V } } ) \frac { \bar { d } \bar { M } } { \bar { d } \bar { t } } .
$$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0040/ocr/images/5d0465dfdb6ae28f62c26677c7fcbc529f9903ac1a6bd4a15dfbc0d44e0be9c5.jpg)  
Figure 3.3

Since linear momentum is conserved, we have

$$
M U = ( M - d M ) ( U + d U ) - V d M
$$

or

$$
M d U - U d M - V d M = 0 .
$$

Rearranging and dividing by $\vec { \mathcal { \pm } } _ { t } ^ { \ \dagger } ,$ we find

$$
M \frac { d \bar { U } } { d t } = ( U \div \bar { \mathcal { V } } ) \frac { d \bar { M } } { d \sharp } .
$$

# 3.10Problems

1. Under what conditions will both the linear and angular momenta of a moving particle be constant?

2. Show that the following fields of force are conservative, and find the potential functions:

$$
\mathbf { P } = \mathbf { g } { \mathrm { ~ ( a ~ c o n s t a n t ) } } ; \quad \mathbf { P } = c \mathbf { r } ; \quad \mathbf { P } = - \mu { \frac { \mathbf { r } } { \tau ^ { 2 } } } ; \quad \mathbf { P } = - \mu { \frac { \mathbf { r } } { r ^ { n } } } .
$$

3.A particle is whirled around at the end of a light, inextensible string of length $\alpha$ ，with constant speed $\mathfrak { C }$ If the particle has mass $\because a$ ,find the tension in the string and the angular momentum about the point of rotation. If the string breaks,describe the path of the particle (neglecting gravity) and show that the angular and linear momenta are conserved.

4. Show that when $\mathbf { \vec { a } } = \mathbf { g }$ , the motion of a particle takes place in a plane, and that the path isa parabola.

5.A mass m is suspended from a point $\beta$ bya light inextensible string of length $\hat { \pmb { \mathscr { T } } }$ The string makes a constant angle with the vertical. By taking moments about $\pmb { \mathcal { O } }$ and using the equation for the angular momentum, show that m moves around the vertical with constant angular velocity; find this velocity.

6.Show that the equation x+k²x = O describes the projection of uniform circular motion on the x-axis, and find the angular velocity of this motion. Hence deduce the general solution to the equation.

7. By trying a solution of the form x = emt, solve the equation x-k²x = 0, and show that the same method can be used to solve +k²x=0.

8.A particle describing simple harmonic motion coalesces with a similar particle at rest at the origin. Describe the subsequent motion.

9. Show that if a particle starting from rest moves subject to an attractive force varying directly as the initial distance of the particle from the origin, then the time of traveling from any point to the origin is independent of the initial distance.

10.Discuss linear motion in a constant field of force with air resistance proportional to the square of the velocity. Investigate the limiting velocities, if any.

11.A particle,subject to a constant feld of force g, falls from a height $\acute { h }$ ， encounteringair resistance proportional to its velocity. Find an expression for the kinetic energy at any point of its descent. How much energy is lost to the frictional force during the total fall?

12.A particle moving initially in simple harmonic motion becomes subject to air resistance varying with its speed. Investigate the subsequent motion.

13.Write down the equations of motion fora freely falling body in a constant field as observed from a point on the surface of the rotating Earth. Investigate any deviations of its path from the vertical;do these depend on the latitude?

14.For the examples given in the text, find out whether the motion is reversible (i.e.,whether the path would be retraced if the velocity were to be suddenly reversed).Discuss the reasons in the cases where the motion is not reversible.

For the remaining problems an inverse square field is assumed.

15.A particle is projected vertically upward from a height $\sin \beta$ with speed ${ \mathfrak { V } } _ { \widehat { \sf U } }$ (less than the velocity of escape).What is the maximum height attained? How longwill it take to reach this height?

16. Show that the time taken for a particle to fall from rest at the height $\$ 1$ to the origin is

$$
\frac { \pi } { k } \left( \frac { s _ { 1 } } { 2 } \right) ^ { 3 / 2 } .
$$

17.Solve the problem of linear motion in an inverse square field when the initial speed is equal to the velocity of escape.

18.Solve the problem of linear motion in an inverse square field when the initial speed is greater than the velocity of escape.

19.Compare the velocity of escape from the surface of the Earth with that froma point 5Oo km above the surface.What initial speed must a particle be given when launched from the Earth's surface so that it will just reach the Moon (380.000 km away)？ If the actual speed is 0.1 percent less than this,how close will the particle get to the Moon？ (Neglect the Moon's gravitational pull.）

20.A minor planet has radius $2 5 \pi 3 2$ , and average density 3.0. What is the velocity of escape from its surface? If a particle on the Earth's surface were given this (vertical) velocity, how far would it rise? Discuss the possibility of a man jumping off the minor planet and escaping from it altogether.

21.A meteor,mass one gram, falls from rest at infinity and burns up in the Earth's atmosphere (neglect the height above the surface of the Earth). Given that a body weighing one kilogram, falling $4 . 2 5 \times 1 0 ^ { 4 }$ cm near the surface of the Earth, generates one calorie, find the number of calories generated by the meteor, assuming that all its energy is turned into heat (but neglecting the energy from any chemical changes).

22.Find the surface gravity (in terms of $\pmb { \mathscr { G } }$ for the Earth) and the velocity of escape for each of the following objects (masses and radii are given in terms of the terrestrial values).

The Sun, $M = 3 3 3 { , } 0 0 0$ ： $\mathcal { R } = \mathfrak { I } \varnothing 9$ The Moon, $M = 0 . 0 1 2 3$ ， $R = 0 . 2 7 2$ Venus, $\tilde { \mathcal { M } } = 0 . 8 \tilde { \lambda } 7$ ： ${ \mathcal { R } } = \emptyset . 9 7$ Jupiter, $M = 3 \Im 8$ ， $\Re = \mathbb { i } 1 . 2$ Uranus, $M = 1 4 . 6$ ： $\Re = 3 . 9$

Mercury, $M = 0 . 0 5 6$ $R = 0 . 3 9$ Mars, $M = 0 . 1 0 8$ ： $R = 0 . 5 3$ Saturn, $M = 9 5 . 2$ $R = 9 . 5$ Neptune, $M = 1 7 . 3$ $R = 4 . 2$

23.In a gas containing molecules of mass $\mathbb { M }$ grams, at a temperature $2 0 \pi$ the“most probable speed” of a molecule is $\mathfrak { v }$ ,where

$$
\widetilde { \lambda } \widetilde { \lambda } v ^ { 2 } = 2 \widetilde { \varepsilon } T .
$$

$\gnapprox$ is Boltzmann's constant and has the value $1 . 3 8 \times 1 0 ^ { - 1 6 }$ Jeans has shown that if this speed is greater than about one-fifth of the velocity of escape of a planet, then the gas will almost entirely have escaped from the planet after a few million years. Bearing in mind that the solar system has existed for several billion years and that at some time the planets may have been much hotter than they are now, investigate the likelihood that each planet and the Moon has retained its initial supply of hydrogen $\mathit { \check { M } } = \mathit { \check { \Pi } } _ { \mathit { \check { \Pi } } } . 6 7 \times \mathit { \check { \Pi } } _ { \mathit { \check { \Pi } } } - 2 4 \mathit { \check { \Pi } } _ { \mathit { \check { \Pi } } }$ ，nitrogen $\mathit { \check { A } } \mathit { \check { A } } = 2 8 \times \mathit { \check { 1 } . 6 6 } \times \mathit { 1 0 ^ { - 2 4 } } ,$ ，and argon $\mathcal { Z } =$ $3 9 . 9 \times \mathrm { \bar { 1 } . 6 6 \times 1 0 ^ { - 2 4 } } ,$
