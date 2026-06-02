# CHAPTER II.

# RECTILINEAR MOTION.

28.A great part of the work in Celestial Mechanics consists of the solution of differential equations which,in most problems, are very complicated on account of the number of dependent variables involved. The ordinary Calculus is devoted, in a large part, to the treatment of equations in which there is but one independent variable and one dependent variable;and the step to simultaneous equations in several variables,requiring interpretation in connection with physical problems and mechanical principles，is one which is usually made not without some difficulty. The present chapter will be devoted to the formulation and to the solution of certain classes of problems in which the mathematical processes are closely related to those which are expounded in the mathematical text-books. It will form the bridge leading from the methods which are familiar in works on Calculus and elementary Differential Equations to those which are characteristic of mechanical and astronomical problems.

The examples chosen to illustrate the principles are taken largely from astronomical problems. They are of sufficient interest to justify their insertion，even though they were not needed as a preparation for the more complicated discussions which willfollow. They embrace the theory of falling bodies,the velocity of escape,parabolic motion，and the meteoric and contraction theories of the sun's heat.

# THE MOTION OF FALLING PARTICLES.

29.The Differential Equation of Motion. Suppose the mass of the particle is m and let s represent the line in which it falls. Take the origin $o$ at the surface of the earth and let the positive end of the line be directed upward. By the second law of motion the rate of change of momentum,or the product of the mass and the acceleration,is proportional to the force. Let $k ^ { 2 }$ represent the factor of proportionality, the numerical value of which will depend upon the units employed. Then,if $f$ represents the force, the differential equation of motion is

$$
m { \frac { d ^ { 2 } s } { d t ^ { 2 } } } = - \ k ^ { 2 } f .
$$

This is also the differential equation of motion for any case in which the resultant of all the forces is constantly in the same straight line and in which the body is not initially projected from that line. A more general treatment will therefore be given than would be required if $f$ were simply the force arising from the earth's attraction for the particle $\textmu m$

The force $f$ will depend in general upon various things, such as the position of $\textit { \textbf { m } }$ ，the time $t$ ，and the velocity $v$ This may be indicated by writing equation (1) in the form

$$
m \ : \frac { d ^ { 2 } s } { d t ^ { 2 } } = \ : - \ : k ^ { 2 } f ( s , t , v ) ,
$$

in which $f \left( s , t , v \right)$ simply means that the force may depend upon the quantities contained in the parenthesis. In order to solve this equation two integrations must be performed,and the character of the integrals will depend upon the manner in which $f$ depends upon s, $t$ ,and $v$ It is necessary to discuss the different cases separately.

30.Case of Constant Force. This simplest case is nearly realized when particles fall through small distances near the earth's surface under the influence of gravity. If the second is taken as the unit of time and the foot as the unit of length then $k ^ { 2 } f = m g ,$ where $g$ is the acceleration of gravity at the surface of the earth. Its numerical value,which varies somewhat with the latitude, is a little greater than 32. Then equation (1) becomes

$$
\frac { d ^ { 2 } s } { d t ^ { 2 } } = - \ g .
$$

This equation gives after one integration

$$
\frac { d s } { d t } = - \ g t + c _ { 1 } ,
$$

where $c _ { 1 }$ is the constant of integration. Let the velocity of the particle at the time $t = 0$ be $\ v { v } = \ v { v } _ { 0 }$ ，Then the last equation becomes at $t = 0$

$$
\begin{array} { r } { \boldsymbol { v } _ { 0 } = c _ { 1 } ; } \end{array}
$$

whence

$$
\frac { d s } { d t } = - \ g t + v _ { 0 } .
$$

The integral of this equation is

$$
\begin{array} { r } { s = - \frac { g t ^ { 2 } } { 2 } + v _ { 0 } t + c _ { 2 } . } \end{array}
$$

Suppose the particle is started at the distance $\bullet \bullet$ from the origin at the time $\pmb { t = 0 }$ ; then this equation gives

whence

$$
~ s _ { 0 } = ~ c _ { 2 } ;
$$

$$
\vartheta = - \frac { g t ^ { 2 } } { 2 } + \upsilon _ { 0 } t + \vartheta _ { 0 } .
$$

When the initial conditions are given this equation determines the position of the particle at any time;or,it determines the time at which the body has any position by the solution of the quadratic equation in $\pmb { t }$

If the acceleration were any other positive or negative constant than - mg,the equation for the space described would differ from (4) only in the coefficient of $t ^ { \mathfrak { z } }$

It is also possible to obtain an important relation between the speed and the position of the particle. Multiply both members of equation (3) by $\mathbf { 2 } { \frac { d s } { d t } }$ Then, since the derivative of $\left( \frac { d s } { d t } \right) ^ { 2 }$ is ${ \bf 2 } { \frac { d s } { d t } } \ { \frac { d ^ { 2 } s } { d t ^ { 2 } } }$ , the integral of the equation is

$$
\left( \frac { d s } { d t } \right) ^ { 2 } = - 2 g s + c _ { 8 } .
$$

It follows from the initial conditions that

$$
c _ { 8 } = v _ { 0 } { } ^ { 2 } + 2 g s _ { 0 } ;
$$

whence

$$
\left( { \frac { d s } { d t } } \right) ^ { 2 } - \left( { \frac { d s } { d t } } \right) _ { 0 } ^ { 2 } = - 2 g ( s - s _ { 0 } ) .
$$

31.Attractive Force Varying Directly as the Distance. Another simple case is that in which the force varies directly as the distance from the origin. Suppose it is always attractive toward the origin. This has been found by experiment to be very nearly the law of tension of an elastic string within certain limits of stretching. Then the velocity will decrease when the particle is on the positive side of the origin；therefore for these positions of the particle the acceleration must be taken with the negative sign,and the differential equation for positive values of $\pmb { \ s }$ is

$$
m { \frac { d ^ { 2 } s } { d t ^ { 2 } } } = - \ k ^ { 2 } s .
$$

For positions of the particle in the negative direction from the origin the velocity increases with the time,and therefore the acceleration is positive. The right member of equation (6) must be taken with such a sign that it will be positive. Since & is negative in the region under consideration the negative sign must be prefixed, and the equation remains as before. Equation (6) is, therefore,the general differential equation of motion for a body subject to an attractive force varying directly as.the distance.

Multiply both membersof equation (6) by $\mathbf { 2 } ~ \frac { d s } { d t }$ and integrate; the result is

$$
m \left( { \frac { d s } { d t } } \right) ^ { 2 } = - k ^ { 2 } s ^ { 2 } + c _ { 1 } .
$$

1f $\begin{array} { r } { \pmb { \mathscr { s } } = \pmb { \mathscr { s } } _ { 0 } } \end{array}$ and $\frac { d \ s } { d t } = 0 .$ at the time $\pmb { t = 0 }$ ， then this equation becomes

$$
\left( { \frac { d s } { d t } } \right) ^ { 2 } = { \frac { k ^ { 2 } } { m } } \left( s _ { 0 } { } ^ { 2 } - s ^ { 2 } \right) ,
$$

which may be written, as is customary in separating the variables,

$$
{ \frac { d s } { \sqrt { s _ { 0 } ^ { 2 } - s ^ { 2 } } } } = \pm { \frac { k d t } { \sqrt { m } } } .
$$

The integral of this equation is

$$
\sin ^ { - 1 } { \frac { s } { s _ { 0 } } } = \pm { \frac { k t } { \sqrt { m } } } + c _ { 2 } .
$$

Itisd $c _ { 2 } = \frac { \pi } { 2 }$ ； whence

$$
\sin ^ { - 1 } { \frac { s } { s _ { 0 } } } = \pm { \frac { k t } { \sqrt { m } } } + { \frac { \pi } { 2 } } .
$$

On taking the sine of both members,this equation becomes

$$
s = s _ { 0 } \sin \left( \pm \frac { k t } { \sqrt { m } } + \frac { \pi } { 2 } \right) = s _ { 0 } \cos \left( \frac { k t } { \sqrt { m } } \right) .
$$

From this equation it is seen that the motion is oscillatory and symmetrical with respect to the origin, with a period of $\frac { 2 \pi \sqrt { m } } { \gamma }$ .

For this reason it is called the equation for harmonic motiou. Obviously $\frac { d s } { d t }$ vanishes at some time during the motion forall initial conditions,and there was no real restriction of the generality of the problem in supposing that it was zero at $t = 0$

Equation (6) is in form the differential equation for many physical problems.When the initial conditions are assigned, it defines the motion of the simple pendulum, the oscillations of the tuning fork and most musical instruments, the vibrations of a radiating body,the small variations in the position of the earth's axis,etc. For this reason the method of finding its solution and the determination of the constants of integration should be thoroughly mastered.

# IⅢI. PROBLEMS.

1.A particle is started with an initial velocity of 2O meters per sec.and is subject to an acceleration of 2O meters per sec. What will be its velocity at the end of 4 secs.,and how far will it have moved?

$$
\begin{array} { r } { 1 n s . \quad \left\{ \begin{array} { l l } { v = 1 0 0 \mathrm { ~ m e t e r s ~ p e r ~ s e c . ~ } } \\ { s = 2 4 0 \mathrm { ~ m e t e r s . ~ } } \end{array} \right. } \end{array}
$$

2.A particle starting with an initial velocity of 10 meters per sec.and moving with a constant acceleration describes 2O5O meters in 5 secs. What is the acceleration?

3.A particle is moving with an acceleration of 5 meters per sec. Through what space must it move in order that its velocity shall be increased from 10 meters per sec.to 20 meters per sec.?

# Ans. 30 meters.

4.A particle starting with a positive initial velocity of 10 meters per sec. and moving under a positive acceleration of 2O meters per sec.described a space of 420 meters. What time was required?

5.Show that,if a particle starting from rest moves subject to an attractive force varying directly as the initial distance, the time of falling from any point to the origin is independent of the distance of the particle.

6.Suppose a particle moves subject to an attractive force varying directly as the distance,and that the acceleration at a distance of 1 meter is 1 meter a sec.If the particle starts from rest how long will it take it to fall from a distance of 20 meters to 10 meters?

7.Suppose a particle moves subject to a force which is repulsive from the origin and which varies directly as the distance；show that if ${ \pmb v } = { \bf 0 }$ and $\begin{array} { r } { \pmb { \mathscr { s } } \ : = \ : \pmb { \mathscr { s } } _ { 0 } } \end{array}$ when $t = 0$ ，then

$$
\log \bigg ( \frac { s + \sqrt { s ^ { 2 } - s _ { 0 } ^ { 2 } } } { s _ { 0 } } \bigg ) = \frac { k } { \sqrt { m } } t ;
$$

whene, leting ${ \frac { k } { \sqrt { m } } } = K ,$

$$
s = { \frac { s _ { 0 } } { 2 } } ( e ^ { \kappa t } + e ^ { - \kappa t } ) = s _ { 0 } \cosh K t .
$$

Observe that equation (7) may be written in the similar form

$$
\begin{array} { l } { \displaystyle { \ s = \frac { s _ { 0 } } { 2 } ( e ^ { \sqrt { - 1 } E t } + e ^ { - \sqrt { - 1 } E t } ) = s _ { 0 } \cos K t . } } \end{array}
$$

8.The surface gravity of the sun is 28 times that of the earth.If a solar prominence 1Oo,Ooo miles high was produced by an explosion,what must have been the velocity of the material when it left the surface of the sun?

32.Solution of Linear Equations by Exponentials. The differential equation (6) and the corresponding one for a repulsive force are linear in s with constant coefficients. There is a general theory which shows that all linear equations having constant coefficients can be solved in terms of exponentials;or,in certain special cases,in terms of exponentials multiplied by powers of the independent variable $t .$ ，This method has not only the advantage of generality,but is also very simple,and it will be illustrated by solving (5).  Consider the two forms

$$
\left\{ \begin{array} { l } { { \displaystyle \frac { d ^ { 2 } s } { d t ^ { 2 } } + k ^ { 2 } s = 0 , } } \\ { { } } \\ { { \displaystyle \frac { d ^ { 2 } s } { d t ^ { 2 } } - k ^ { 2 } s = 0 . } } \end{array} \right.
$$

Assume $\begin{array} { r } { \pmb { \mathscr { s } } = \pmb { \mathcal { e } } ^ { \lambda \pmb { \mathscr { t } } } } \end{array}$ and substitute in the diferential equations; whence

$$
\left\{ \begin{array} { l l } { { \lambda ^ { 2 } e ^ { \lambda t } + k ^ { 2 } e ^ { \lambda t } = 0 , } } \\ { { \lambda ^ { 2 } e ^ { \lambda t } - k ^ { 2 } e ^ { \lambda t } = 0 . } } \end{array} \right.
$$

Since these equations must be satisfed by all values of $\pmb { t }$ in order that $e ^ { \lambda t }$ shall be a solution,it follows that

$$
\left\{ \begin{array} { l l } { { \lambda ^ { 2 } + k ^ { 2 } = 0 , } } \\ { { \lambda ^ { 2 } - k ^ { 2 } = 0 . } } \end{array} \right.
$$

Let the roots of the first equation be $\lambda _ { 1 }$ and $\pmb { \lambda _ { 2 } }$ ； then the first equation of (8) is verified by both of the particular solutions $e ^ { \lambda _ { 1 } t }$ and $e ^ { \lambda _ { 2 } t }$ . The general solution is the sum of these two particular solutions,each multiplied by an arbitrary constant. Precisely similar results hold for the second equation of (8). On putting in the value of the roots, the respective general solutions are

$$
\left\{ \begin{array} { l l } { \mathfrak { s } = c _ { 1 } e ^ { \sqrt { - 1 } k t } + c _ { 2 } e ^ { - \sqrt { - 1 } k t } , } \\ { \mathfrak { s } = c _ { 1 } { } ^ { \prime } e ^ { k t } + c _ { 2 } { } ^ { \prime } e ^ { - k t } , } \end{array} \right.
$$

where $\pmb { c _ { 1 } } , \pmb { c _ { 2 } } , \pmb { c _ { 1 } } ^ { \prime }$ ,and ${ c _ { 2 } } ^ { \prime }$ are the constants of integration.

Suppose $\begin{array} { r } { \pmb { \mathscr { s } } = \pmb { \mathscr { s } } _ { \pmb { 0 } } , } \end{array}$ and $\frac { d s } { d t } = s _ { 0 } \prime$ when $\pmb { t = 0 }$ ； therefore

$$
\left\{ \begin{array} { l l } { { \mathfrak { s } } _ { 0 } = { \mathfrak { c } } _ { 1 } + { \mathfrak { c } } _ { 2 } , } \\ { { \mathfrak { s } } _ { 0 } = { \mathfrak { c } } _ { 1 } ^ { \prime } + { \mathfrak { c } } _ { 2 } ^ { \prime } . } \end{array} \right.
$$

The derivatives of (10) are

$$
\left\{ \begin{array} { l } { { \displaystyle { \frac { d s } { d t } } = c _ { 1 } \sqrt { - 1 } k e ^ { \sqrt { - 1 } k t } - c _ { 2 } \sqrt { - 1 } k e ^ { - \sqrt { - 1 } k t } } , } \\ { { } } \\ { { \displaystyle { \frac { d s } { d t } } = c _ { 1 } { ' } k e ^ { k t } - c _ { 2 } { ' } k e ^ { - k t } . } } \end{array} \right.
$$

On substuting $t = 0$ and $\frac { d s } { d t } = s _ { 0 } ^ { \prime }$ i folws that

Therefore

$$
\left\{ \begin{array} { l l } { { c _ { 1 } \sqrt { - 1 } k - c _ { 2 } \sqrt { - 1 } k = s _ { 0 } ^ { \prime } , } } \\ { { c _ { 1 } ^ { \prime } k - c _ { 2 } ^ { \prime } k = s _ { 0 } ^ { \prime } . } } \end{array} \right.
$$

$$
\left\{ \begin{array} { l } { \displaystyle c _ { 1 } = \frac { 1 } { 2 } \left( s _ { 0 } + \frac { s _ { 0 } ^ { \prime } } { k \sqrt { - 1 } } \right) , } \\ { \displaystyle c _ { 2 } = \frac { 1 } { 2 } \left( s _ { 0 } - \frac { s _ { 0 } ^ { \prime } } { k \sqrt { - 1 } } \right) , } \\ { \displaystyle c _ { 1 } ^ { \prime } = \frac { 1 } { 2 } \left( s _ { 0 } + \frac { s _ { 0 } ^ { \prime } } { k } \right) , } \\ { \displaystyle c _ { 2 } ^ { \prime } = \frac { 1 } { 2 } \left( s _ { 0 } - \frac { s _ { 0 } ^ { \prime } } { k } \right) . } \end{array} \right.
$$

Then the general solutions become

$$
\left\{ \begin{array} { l } { { \displaystyle \delta = \frac { s _ { 0 } } { 2 } ( e ^ { \iota \overline { { { - 1 } } } \iota t } + e ^ { - \iota \overline { { { - 1 } } } \iota t } ) + \frac { s _ { 0 } ^ { \prime } } { 2 k \sqrt { - 1 } } ( e ^ { \iota \overline { { { - 1 } } } \iota t } - e ^ { - \iota \sqrt { - 1 } k t } ) , } } \\ { { \displaystyle \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } } \\ { { \displaystyle \vartheta = \frac { s _ { 0 } } { 2 } ( e ^ { k t } + e ^ { - k t } ) + \frac { s _ { 0 } ^ { \prime } } { 2 k } ( e ^ { k t } - e ^ { - k t } ) . } } \end{array} \right.
$$

Or these expressions can be written in the form

$$
\left\{ \begin{array} { l l } { { \displaystyle s = s _ { 0 } \cos k t + \frac { s _ { 0 } ^ { \prime } } { k } \sin k t } , } \\ { { \displaystyle } s = s _ { 0 } \cosh k t + \frac { s _ { 0 } ^ { \prime } } { k } \sinh k t . } \end{array} \right.
$$

This method of treatment shows the close relation between the two problems much more clearly than the other methods of obtaining the solutions.

33. Attractive Force Varying Inversely as the Square of the Distance. For positions in the positive direction from the origin the velocity decreases algebraically as the time increases whether the motion is toward or from the origin；therefore in this region the acceleration is negative. Similarly，on the negative side of the origin the acceleration is positive.Since $\frac { k ^ { 2 } } { s ^ { 2 } }$ is always positive the right member has different signs in the two cases. For simplicity suppose the mass of the attracted particle is unity. Then the differential equation of motion for all positions of the particle in the positive direction from the origin is

$$
\frac { d ^ { 2 } s } { d t ^ { 2 } } = - \frac { k ^ { 2 } } { s ^ { 2 } } .
$$

On multiligotmmrsftsquationby $2 \frac { d s } { d t }$ and inte grating,it is found that

$$
\left( { \frac { d s } { d t } } \right) ^ { 2 } = { \frac { 2 k ^ { 2 } } { s } } + c _ { 1 } .
$$

Suppose $\mathit { \Delta } \ v { v } = \mathit { \Delta } \ v { v } _ { 0 }$ and $\textstyle s = s _ { 0 }$ when $t = 0$ ； then

$$
c _ { 1 } = v _ { 0 } { } ^ { 2 } - \frac { 2 k ^ { 2 } } { s _ { 0 } } .
$$

On substituting this expression for $\pmb { c _ { 1 } }$ in (13),it is found that

$$
\frac { d s } { d t } = \pm \ \sqrt { \frac { 2 \kappa ^ { 2 } } { s } + { v _ { 0 } } ^ { 2 } - \frac { 2 k ^ { 2 } } { s _ { 0 } } } .
$$

If $v _ { 0 } ^ { 2 } - \frac { 2 k ^ { 2 } } { s _ { 0 } } < 0$ there will be some finite distance $\pmb { \mathscr { s } } _ { 1 }$ at which $\frac { d s } { d t }$ will vanish; if the direction of motion of the particle is such that it reaches that point it will turn there and move in the opposite direction.If $v _ { 0 } ^ { 2 } - \frac { 2 k ^ { 2 } } { s _ { 0 } } = 0 , \frac { d s } { d t }$ will vanish at $s = \infty$ ; and if the particle moves out from the origin toward infinity its distance will become indefinitely great as the velocity approaches zero. If $v _ { 0 } ^ { 2 } - \frac { 2 k ^ { 2 } } { s _ { 0 } } > 0 , \frac { d s } { d t }$ never vanishes,andif thepartile movesout from the origin toward infinity its distance will become indefinitely great and its velocity will not approach zero.

Suppose $v _ { 0 } { } ^ { 2 } \stackrel { } { - } \frac { 2 k ^ { 2 } } { s _ { 0 } } < 0$ and that $\frac { d s } { d t } = 0$ when ${ \mathfrak { s } } = { \mathfrak { s } } _ { 1 }$ Then equation (13) gives

$$
\frac { d s } { d t } = \pm \sqrt { \frac { 2 } { s _ { 1 } } } k \sqrt { \frac { s _ { 1 } - s } { s } } .
$$

The positive or negative sign is to be taken according as the particle is receding from, or approaching toward, the origin.

This equation can be written in the form

$$
{ \frac { s d s } { { \sqrt { s _ { 1 } s - s ^ { 2 } } } } } = \pm { \sqrt { \frac { 2 } { s _ { 1 } } } } k d t ,
$$

and the integral is therefore

$$
- \sqrt { s _ { 1 } s - s ^ { 2 } } + \frac { s _ { 1 } } { 2 } \mathrm { s i n } ^ { - 1 } \biggl ( \frac { 2 s - s _ { 1 } } { s _ { 1 } } \biggr ) = \pm \sqrt { \frac { 2 } { s _ { 1 } } } k t + c _ { 2 } .
$$

Since $\textstyle { \pmb { \mathscr { s } } } = { \pmb { \mathscr { s } } } _ { 0 }$ when $\scriptstyle t = 0$ ,it follows that

$$
c _ { 2 } = - ~ \sqrt { s _ { 1 } s _ { 0 } - s _ { 0 } { } ^ { 2 } } + \frac { s _ { 1 } } { 2 } \mathrm { s i n } ^ { - 1 } \bigg ( \frac { 2 s _ { 0 } - s _ { 1 } } { s _ { 1 } } \bigg ) ;
$$

whence

$$
\begin{array} { r l r } {  { \frac { \vartheta _ { 1 } } { 2 } \bigg [ \sin ^ { - 1 } \bigg ( \frac { 2 \vartheta - \vartheta _ { 1 } } { \vartheta _ { 1 } } \bigg ) - \sin ^ { - 1 } \bigg ( \frac { 2 \vartheta _ { 0 } - \vartheta _ { 1 } } { \vartheta _ { 1 } } \bigg ) \bigg ] } } \\ & { } & { + \sqrt { s _ { 1 } \vartheta _ { 0 } - \vartheta _ { 0 } ^ { 2 } } - \sqrt { s _ { 1 } \vartheta - \vartheta ^ { 2 } } = \pm \sqrt { \frac { 2 } { s _ { 1 } } } k t . } \end{array}
$$

This equation determines the time at which the particle has any position at the right of the origin whose distance from it is less than ${ \pmb s } _ { 1 }$ .For values of s greater than ${ \pmb s } _ { 1 }$ ,and for all negative values of s,the second term becomes imaginary. That means that the equation does not hold for these values of the variables; this was indeed certain because the differential equations (13)and (14) were valid only for

$$
0 < s \leq \vartheta _ { \pm } \mathfrak { s } _ { 1 } .
$$

Suppose the particle is approaching the origin; then the negative sign must be used in the right member of (15). The time at which the particle was at rest is obtained by putting $\begin{array} { r } { \pmb { \mathscr { s } } = \pmb { \mathscr { s } } _ { 1 } } \end{array}$ in (15), and is

$$
T _ { 1 } = \mathrm { ~ - ~ } \frac { 1 } { k } \sqrt { \frac { { \mathfrak { s } } _ { 1 } } { 2 } \sqrt { { \mathfrak { s } } _ { 1 } { \mathfrak { s } } _ { 0 } - { \mathfrak { s } } _ { 0 } { } ^ { 2 } } } - \frac { 1 } { k } \left( \frac { { \mathfrak { s } } _ { 1 } } { 2 } \right) ^ { \frac { 3 } { 4 } } \bigg [ + \frac { \pi } { 2 } - \mathrm { ~ } \mathrm { { s i n } } ^ { - 1 } \left( \frac { 2 { \mathfrak { s } } _ { 0 } - { \mathfrak { s } } _ { 1 } } { { \mathfrak { s } } _ { 1 } } \right) \bigg ] .
$$

The time required for the particle to fall from $\scriptstyle { \pmb { \mathscr { s } } } _ { 0 }$ to the origin is obtained by putting $s = 0$ in (15),and is

$$
T _ { 2 } = \mathrm { } - \frac { 1 } { k } \sqrt { \frac { s _ { 1 } } { 2 } } \sqrt { s _ { 1 } s _ { 0 } - s _ { 0 } } ^ { 2 } - \frac { 1 } { k } \left( \frac { s _ { 1 } } { 2 } \right) ^ { \frac { 3 } { 2 } } \biggl [ - \frac { \pi } { 2 } - \sin ^ { - 1 } \biggl ( \frac { 2 s _ { 0 } - s _ { 1 } } { s _ { 1 } } \biggr ) \biggr ] .
$$

The time required for the particle to fall from rest at $s = s _ { 1 }$ to the origin is

$$
T = T _ { 2 } - T _ { 1 } = { \frac { \pi } { k } } \bigg ( { \frac { s _ { 1 } } { 2 } } \bigg ) ^ { \frac { 3 } { 2 } } .
$$

34.The Height of Projection. When the constant $\pmb { c _ { 1 } }$ has been determined by the initial conditions,equation (13) becomes

$$
\left( { \frac { d s } { d t } } \right) ^ { 2 } - { v _ { 0 } } ^ { 2 } = { v ^ { 2 } } - { v _ { 0 } } ^ { 2 } = 2 k ^ { 2 } \left( { \frac { 1 } { s } } - { \frac { 1 } { s _ { 0 } } } \right) .
$$

It follows from this equation that the speed depends only on the distance of the particle from the center of force and not on the direction of its motion. The greatest distance to which the particle recedes from the origin,or the height of projection from the origin, is obtained by putting $v = 0$ ,which gives

$$
\frac { 1 } { s _ { 1 } } = \frac { 1 } { s _ { 0 } } - \frac { { v _ { 0 } } ^ { 2 } } { 2 k ^ { 2 } } .
$$

But if the height of projection is measured from the point of projection $\begin{array} { r } { \pmb { \mathscr { s } } _ { 0 } ; \qquad } \end{array}$ ， as would be natural in considering the projection of a body away from the surface of the earth, the formula becomes

$$
s _ { 2 } = s _ { 1 } - s _ { 0 } = \frac { { v _ { 0 } } ^ { 2 } { s _ { 0 } } ^ { 2 } } { 2 k ^ { 2 } - { v _ { 0 } } ^ { 2 } { s _ { 0 } } } .
$$

35.The Velocity from Infinity. When the particle starts from $\scriptstyle { \mathfrak { s o } }$ with zero velocity,equation (13) becomes

$$
\left( { \frac { d s } { d t } } \right) ^ { 2 } = 2 k ^ { 2 } \left( { \frac { 1 } { s } } - { \frac { 1 } { s _ { 0 } } } \right) .
$$

If the particle fals from an infinite distance, ${ \pmb s } _ { \pmb 0 }$ is infinite and the equation reduces to

$$
\left( \frac { d s } { \bar { d } t } \right) ^ { 2 } = \frac { 2 k ^ { 2 } } { s } .
$$

From the investigations of Art.34 it follows that,if the particle is projected from any point $\pmb { \mathscr { s } }$ in the positive direction with the velocity defined by (18),it will recede to infinity.The law of attraction in deriving (18) is Newton's law of gravitation; therefore this equation can be used for the computation of the velocity which a particle starting from infinity would acquire in falling to the surfaces of the various planets,satellites,and the sun. Then,if the particle were projected from the surfaces of the various members of the solar system with these respective velocities,it would recede to an infinite distance if it were not acted on by other forces. But if its velocity were only enough to take it away from a satellite or a planet,it would still be subject to the attraction of the remaining members of the solar system, chief of which is of course the sun,and it would not in general recede to infinity and be entirely lost to the system.

36.Application to the Escape of Atmospheres. The kinetic theory of gases is that the volumes and pressures of gases are maintained by the mutual impacts of the individual molecules, which are,on the average,in a state of very rapid motion. The rarity of the earth's atmosphere and the fact that the pressure is about ffteen pounds to the square inch,serve to give some idea of the high speed with which the molecules move and of the great frequency of their impacts. The different molecules do not all move with the same speed in any given gas under fixed conditions; but the number of those which have a rate of motion different from the mean of the squares becomes less very rapidly as the differences increase. Theoretically,in all gases the range of the values of the velocities is from zero to infinity，although the extreme cases occur at infinitely rare intervals compared to the others. Under constant pressure the velocities are directly proportional to the square root of the absolute temperature,and inversely proportional to the square root of the molecular weight.

Since in all gases all velocities exist, some of the molecules of the gaseous envelopes of the heavenly bodies must be moving with velocities greater than the velocity from infinity,as defined in Art.35. If the molecules are near the upper limits of the atmosphere,and start away from the body to which they belong, they may miss collisions with other molecules and escape never to return\*. Since the kinetic theory of gases is supported by very strong observational evidence,and since if it is true it is probable that some molecules move with velocities greater than the velocity from infinity, it is probable that the atmospheres of all celestial bodies are being depleted by this process;but in most cases it is an excessively slow one,and is compensated,to some extent at least,by the accretion of meteoric matter and atmospheric molecules from other bodies. In the upper regions of the gaseous envelopes, from which alone the molecules escape, the temperatures are low,at least for planetary bodies like the earth,and high velocities are of rare occurrence. If the mean square velocity were as great as,or exceeded, the velocity from infinity the depletion would be a relatively rapid process. In any case the elements and compounds with low molecular weights would be lost most rapidly,and thus certain ones might freely escape and others be largely retained.

The manner in which the velocity from infinity with respect to the surface of an attracting sphere varies with its mass and radius will now be investigated. The mass of a body is proportional to the product of its density and cube of its radius. Then $k ^ { 2 }$ ，which is the attraction at unit distance,varies directly as the mass,and therefore directly as the product of the density and the cube of the radius. Hence it follows from (18) that the velocity from infinity at the surface of a body varies as the product of its radius and the square root of its density. The densities and the radii of the members of the solar system are usually expressed in terms of the density and the radius of the earth; hence the velocity from infinity can be easily computed for each of them after it has been determined for the earth.

Let $\pmb { R }$ represent the radius of the earth, and $\pmb { \theta }$ the acceleration of gravitation at its surface. Then it follows that

$$
{ \pmb g } = \frac { k ^ { 2 } } { R ^ { 2 } } .
$$

On substituting the value of $\pmb { k ^ { 2 } }$ determined from this equation into (18),the expression for the square of the velocity becomes

$$
\left( { \frac { d s } { d t } } \right) ^ { 2 } = { \frac { 2 g R ^ { 2 } } { s } } .
$$

Let $V = { \frac { d s } { d t } }$ when $\bullet = R$ ; whence

$$
V ^ { 2 } = 2 g R .
$$

Let a second be taken as the unit of time, and a meter as the unit of length．Then $R = 6 { , } 3 7 1 { , } 0 0 0$ and $g = 9 . 8 0 9 4 ^ { * }$ .On substituting in the last equation and carrying out the computation, it is found that $V = 1 1 , 1 8 0$ meters,or about 6.95 miles,per sec. On taking the values of the relative densities and radii of the planets as given in Chapter XI of Moulton's Introduction to Astronomy,the following results are found:

<table><tr><td>Body</td><td colspan="6">Velocity of Escape</td></tr><tr><td>Earth</td><td>11,180 meters,or</td><td></td><td></td><td>6.95 miles,per sec.</td><td></td><td></td></tr><tr><td>Moon</td><td>2,396</td><td>“</td><td>“</td><td>1.49 “</td><td>“</td><td>“</td></tr><tr><td>Sun</td><td>618,200</td><td>“</td><td>“ 384.30</td><td>“</td><td>“</td><td>“</td></tr><tr><td>Mercury</td><td>3,196</td><td>“</td><td>“</td><td>1.99 “</td><td>“</td><td>“</td></tr><tr><td>Venus</td><td>10,475</td><td>“</td><td>“</td><td>6.51 “</td><td>“</td><td>“</td></tr><tr><td>Mars</td><td>5,180</td><td>“</td><td>“</td><td>3.2: “</td><td>“</td><td>“</td></tr><tr><td>Jupiter</td><td>61,120</td><td>“</td><td>“</td><td>38.04</td><td>“ “</td><td>“</td></tr><tr><td>Saturn</td><td>37,850</td><td>“</td><td>“</td><td>23.53 “</td><td>“</td><td>“</td></tr><tr><td>Uranus</td><td>23,160</td><td>“</td><td>“</td><td>14.40</td><td>“ “</td><td>“</td></tr><tr><td>Neptune</td><td>20,830</td><td>“</td><td>“</td><td>12.95 “</td><td>“</td><td>“</td></tr></table>

The velocity from infinity decreases as the distance from the center of a planet increases,and the necessary velocity of projection in order that a molecule may escape decreases correspondingly;and the centrifugal acceleration of the planet's rotation adds to the velocities of certain molecules.

The question arises whether，under the conditions prevailing at the surfaces of the various bodies enumerated, the average molecular velocities of the atmospheric elements do not equal or surpass the corresponding velocity from infinity.

It is possible to find experimentally the pressure exerted by a gas having a given density and temperature upon a unit surface, from which the mean square velocity can be computed. It is shown in the kinetic theory of gases that the square root of the mean square velocity of hydrogen molecules at the temperature $\mathbf { 0 } ^ { \circ }$ Centigrade under atmospheric pressure is about 1,7O0 meters per second. Under the same conditions the velocities of oxygen and nitrogen molecules are about one-fourth as great.

The surface temperatures of the inferior planets are certainly much greater than zero degrees Centigrade in the parts where they receive the rays of the sun most directly,even if all the heat which may ever have been received from their interiors is neglected. It seems probable from the geological evidences of igneous action upon the earth that in the remote past they were at a much higher temperature,and the superior planets have not yet cooled down to the solid state. There is evidence that the most refractory substances have been in a molten state at some time,which implies that they have had a temperature of 30o0 or 40oo degrees Centigrade. Therefore the square root of the mean square velocity may have been much greater than the approximate mile a second for hydrogen given above,and it probably continued much greater for a long period of time. On comparing these results with the table of velocities from infinity,it is seen that the moon and inferior planets,according to this theory,could not possibly have retained free hydrogen and other elements of very small molecular weights,such as helium,in their envelopes；in the case of the moon，Mercury，and Mars, the escape of heavier molecules as nitrogen and oxygen must have been frequent. This is especially probable if the heated atmospheres extended out to great distances. The superior planets,and especially the sun,could have retained all of the familiar terrestrial elements,and from this theory it should be expected that these bodies would be surrounded with extensive gaseous envelopes.

The observed facts are that the moon has no appreciable atmosphere whatever; Mercury an extremely rare one, if any at all; Mars,one much less dense than that of the earth; Venus, one perhaps somewhat more dense than that of the earth；on the other hand the superior planets are surrounded by extensive gaseous envelopes.

37. The Force Proportional to the Velocity. When a particle moves in a resisting medium the forces to which it is subject depend upon its velocity. Experiments have shown that in the earth's atmosphere when the velocity is.less than 3 meters per second the resistance varies nearly as the first power of the velocity; for velocities from 3 to 300 meters pər second it varies nearly as the second power of the velocity；and for velocities about 400 meters per second, nearly as the third power of the velocity.

$( a )$ Consider first the case where the resistance varies as the first power of the velocity，and suppose the motion is on the earth's surface in a horizontal direction with no force acting except that arising from the resistance. Then the differential equation of motion is

$$
\frac { d ^ { 2 } s } { d t ^ { 2 } } + k ^ { 2 } \frac { d s } { d t } = 0 ,
$$

where $k ^ { 2 }$ is a positive constant which depends upon the units employed,the nature of the body,and the character of the resisting medium. Equation (2O) is linear in the dependent variable s,and the general method of solving linear equations can be applied.

Assume the particular solution

$$
s = e ^ { \lambda t } .
$$

Substitute in (20) and divide by $e ^ { \lambda t }$ ； then

$$
\lambda ^ { 2 } + k ^ { 2 } \lambda = 0 .
$$

The roots of this equation are

$$
\left\{ \begin{array} { l l } { \lambda _ { 1 } = 0 , } \\ { \lambda _ { 2 } = - k ^ { 2 } , } \end{array} \right.
$$

:and the general solution is

$$
\left\{ \begin{array} { l l } { s = c _ { 1 } + c _ { 2 } e ^ { - k ^ { 2 } t } , } \\ { \qquad } \\ { \displaystyle \frac { d s } { d t } = - c _ { 2 } k ^ { 2 } e ^ { - k ^ { 2 } t } . } \end{array} \right.
$$

:Suppose $\frac { d \ s } { d t } = \ v _ { v _ { 0 } }$ and $\begin{array} { r } { \pmb { \mathscr { s } } = \pmb { \mathscr { s } } _ { 0 } } \end{array}$ when $\pmb { t = 0 }$ .Then the constants $\pmb { c _ { 1 } }$ and $\pmb { c _ { 2 } }$ can be determined in terms of ${ \mathfrak { v } } _ { 0 }$ and ${ \pmb s } _ { \bf 0 } ,$ and the solution becomes

$$
\begin{array} { r } { s = s _ { 0 } + \frac { \mathcal { V } _ { 0 } } { \mathcal { k } ^ { 2 } } - \frac { \mathcal { V } _ { 0 } } { \mathcal { k } ^ { 2 } } e ^ { - \mathcal { k } ^ { 2 } t } . } \end{array}
$$

$( b )$ Consider the case where the resistance varies as the first power of the velocity and suppose the motion is in the vertical line. Take the positive end of the axis upward. When the motion is upward the velocity is positive and the resistance diminishes the velocity. Therefore when the motion is upward the resistance produces a negative acceleration,and the differential equation of motion is

$$
\frac { d ^ { 2 } s } { d t ^ { 2 } } + k ^ { 2 } \frac { d s } { d t } = - \ g .
$$

When the motion is downward the resistance algebraically increases the velocity; therefore in this case the resistance produces a positive acceleration. But since the velocity is opposite in sign in the two cases,equation (23) holds whether the particle is ascending or descending.

Equation (23) is linear,but not homogeneous,and it can easily be solved by the method known as the Variation of Parameters.

This method is so important in astronomical problems that it will be introduced in the present simple connection,though it is not at all necessary in order to obtain the solution of (23). In order to apply the method consider first the equation

$$
\frac { d ^ { 2 } s } { d t ^ { 2 } } + k ^ { 2 } \frac { d s } { d t } = 0 ,
$$

which is obtained from (23） simply by omitting the term which does not involve s. The general solution of this equation is the first of (21). The method of the variation of parameters,or constants,consists in so determining $\pmb { c _ { 1 } }$ and $\mathbf { c _ { 2 } }$ as functions of $\scriptstyle t$ that the differential equation shall be satisfied when the right member is included. This imposes only one condition upon the two quantities $c _ { 1 }$ and $\pmb { c _ { 2 } } _ { 3 } .$ ，and another can therefore be added.

If the coefficients $c _ { 1 }$ and $c _ { 2 }$ are regarded as functions of $t ,$ it is found on differentiating the first of (21) that

$$
\frac { d s } { d t } = \triangledown - k ^ { 2 } c _ { 2 } e ^ { - k ^ { 2 } t } + \frac { d c _ { 1 } } { d t } + e ^ { - k ^ { 2 } t } \frac { d c _ { 2 } } { d t } .
$$

As the supplementary condition on $c _ { 1 }$ and $\pmb { c _ { 2 } }$ these quantities will be made subject to the relation

$$
\frac { d c _ { 1 } } { d t } + e ^ { - k ^ { 2 } t } \frac { d c _ { 2 } } { d t } = 0 ,
$$

which simplifes theexpressionfor $\frac { d s } { d t }$ Then it is found that

$$
\frac { d ^ { 2 } s } { d t ^ { 2 } } = k ^ { 4 } c _ { 2 } e ^ { - k ^ { 2 } t } - k ^ { 2 } e ^ { - k ^ { 2 } t } \frac { d c _ { 2 } } { d t }
$$

and equation (23) gives

$$
k ^ { 2 } \frac { d c _ { 1 } } { d t } = - \ g .
$$

It follows from this equation and (25) that

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d c _ { 1 } } { d t } = \mathrm { ~ - ~ } \frac { g } { k ^ { 2 } } , \quad \quad \displaystyle \frac { d c _ { 2 } } { d t } = \frac { g } { k ^ { 2 } } e ^ { k ^ { 2 } t } , } \\ { \displaystyle c _ { 1 } = \mathrm { ~ - ~ } \frac { g } { k ^ { 2 } } t + c _ { 1 } ^ { \prime } , \quad c _ { 2 } = \displaystyle \frac { g } { k ^ { 4 } } e ^ { k ^ { 2 } t } + c _ { 2 } ^ { \prime } , } \end{array} \right.
$$

where ${ \pmb { c } } _ { 1 } ^ { \prime }$ and ${ c _ { 2 } } ^ { \prime }$ are new constants of integration. When these values of $\pmb { c _ { 1 } }$ and $\mathbf { c _ { 2 } }$ are substituted in (21),it is found that

$$
\vartheta = c _ { 1 } { } ^ { \prime } + c _ { 2 } { } ^ { \prime } e ^ { - k ^ { 2 } t } - \frac { g } { k ^ { 2 } } t + \frac { g } { k ^ { 4 } } .
$$

Since ${ \pmb { c _ { 1 } } } ^ { \prime }$ is arbitrary it can of course be supposed to include the constant $\frac { g } { k ^ { 4 } }$ ·

The expression (29) is the general solution of (23) because it contains two arbitrary constants, ${ \pmb { c _ { 1 } } } ^ { \prime }$ and ${ c _ { 2 } } ^ { \prime }$ ,and when substituted in (23） satisfies it identically in $t$ 、It will be observed that the part of the solution depending on $\pmb { c _ { 1 } } ^ { \prime }$ and ${ c _ { 2 } } ^ { \prime }$ has the same form as the solution of (2O)． It is clear that the general solution could have been found by the same method if the right member of (23) had been a known function of $t ,$ instead of the constant $- \textit { \textbf { g } }$

The velocity of the particle is found from (29) to be given by the equation

$$
\frac { d s } { d t } = - \left. k ^ { 2 } c _ { 2 } \right. e ^ { - k ^ { 2 } t } - \frac { g } { k ^ { 2 } } .
$$

Suppose s = So, $s = s _ { 0 } , \frac { d s } { d t } = v _ { 0 }$ at $t = 0$ On puting these Values in equations (29) and (30),it is found that

$$
\left\{ \begin{array} { l l } { \displaystyle s _ { 0 } = c _ { 1 } ^ { \prime } + c _ { 2 } ^ { \prime } + \frac { g } { \displaystyle { k ^ { 4 } } } , } \\ { \displaystyle v _ { 0 } = - k ^ { 2 } c _ { 2 } ^ { \prime } - \frac { g } { \displaystyle { k ^ { 2 } } } ; } \end{array} \right.
$$

whence

$$
\left\{ \begin{array} { l } { { c _ { 1 } } ^ { \prime } = { s _ { 0 } } + { \frac { v _ { 0 } } { k ^ { 2 } } } , } \\ { { } } \\ { { c _ { 2 } } ^ { \prime } = { - \displaystyle { \frac { v _ { 0 } } { k ^ { 2 } } - \frac { g } { k ^ { 4 } } } } . } \end{array} \right.
$$

Consequently，when the constants are determined by the initial conditions,the general solution (29) becomes

$$
\left\{ \begin{array} { l l } { { s = s _ { 0 } + \frac { v _ { 0 } } { k ^ { 2 } } + \frac { g } { k ^ { 4 } } - \frac { g } { k ^ { 2 } } t - \left( \frac { v _ { 0 } } { k ^ { 2 } } + \frac { g } { k ^ { 4 } } \right) e ^ { - k ^ { 2 } t } , } } \\ { { \nonumber } } \\ { { \displaystyle \frac { d s } { d t } = - \frac { g } { k ^ { 2 } } + \left( v _ { 0 } + \frac { g } { k ^ { 2 } } \right) e ^ { - k ^ { 2 } t } . } } \end{array} \right.
$$

The particlereachesitshighestpointwhen $\frac { d s } { d t }$ is zero.Let $\pmb { T }$ represent the time it reaches this point and $ \boldsymbol { S } -  \boldsymbol { s } _ { 0 }$ the height of this point;then it is found from equations (31) that

$$
\left\{ \begin{array} { c } { { e ^ { k ^ { 2 } \tau } = 1 + \frac { k ^ { 2 } v _ { 0 } } { g } , } } \\ { { S - s _ { 0 } = \frac { v _ { 0 } } { k ^ { 2 } } - \frac { g } { k ^ { 4 } } \log \Big ( 1 + \frac { k ^ { 2 } v _ { 0 } } { g } \Big ) . } } \end{array} \right.
$$

38.The Force Proportional to the Square of the Velocity. At the velocity of a strong wind,or of a body falling any considerable distance,or of a ball thrown, the resistance varies very nearly as the square of the velocity. An investigation will now be made of the character of the motion of a particle when projected upward against gravity，and subject to a resistance from the atmosphere varying as the square of the velocity. For simplicity in writing, the acceleration due to resistance at unit velocity will be taken as $k ^ { 2 } g$ .Then the differential equation of motion for a unit particle is

$$
\frac { d ^ { 2 } s } { d t ^ { 2 } } = - \ g - k ^ { 2 } g \left( \frac { d s } { d t } \right) ^ { 2 } .
$$

This equation may be written in the form

$$
{ \frac { { \frac { d } { d t } } \left( k { \frac { d s } { d t } } \right) } { 1 + k ^ { 2 } \left( { \frac { d s } { d t } } \right) ^ { 2 } } } = - k g ,
$$

of which the integral is

$$
\tan ^ { - 1 } \left( k { \frac { d s } { d t } } \right) = - \ k g t + c _ { 1 } .
$$

If $\frac { d s } { d t } = \upsilon _ { 0 }$ and $s _ { 0 } = 0$ when $t = 0$ ,then

$$
c _ { 1 } = \tan ^ { - 1 } { \left( k v _ { 0 } \right) } .
$$

On substituting in (33) and taking the tangent of both members, it is found that

$$
\frac { d s } { d t } = \frac { 1 } { k } \frac { v _ { 0 } k \mathrm { ~ - ~ } \mathrm { t a n ~ } ( k g t ) } { 1 \mathrm { ~ + ~ } v _ { 0 } k \mathrm { ~ t a n ~ } ( k g t ) } .
$$

This equation expresses the velocity in terms of the time. On multiplying both numerator and denominator of the right member of (34) by cos $( k g t )$ ,the numerator becomes the derivative of the denominator with respect to the time. Then integratig，the final solution becomes

$$
\begin{array} { c c c } { \displaystyle { s = \frac { 1 } { k ^ { 2 } g } \log \left[ v _ { 0 } k \sin \left( k g t \right) + \cos \left( k g t \right) \right] + c _ { 2 } . } } \end{array}
$$

It follows from the initial conditions that $c _ { 2 } = 0$ This equation expresses the distance passed over in terms of the time.

The equations can be so treated that the velocity will be expressed in terms of the distance. Equation (32) can be written


<!-- chunk 0002: pages 71-140 -->
$$
\frac { \frac { d } { d t } \left\{ k ^ { 2 } \left( \frac { d s } { d t } \right) ^ { 2 } \right\} } { 1 + k ^ { 2 } \left( \frac { d s } { d t } \right) ^ { 2 } } = - 2 g k ^ { 2 } \frac { d s } { d t } ,
$$

of which the integral is

$$
\log \Big \{ 1 + k ^ { 2 } \Big ( \frac { d s } { d t } \Big ) ^ { 2 } \Big \} = - 2 g k ^ { 2 } s + c _ { 1 } ^ { \prime } .
$$

From the initial conditions it follows that

Therefore

$$
{ c _ { 1 } } ^ { \prime } = \log { ( 1 + k ^ { 2 } v _ { 0 } { } ^ { 2 } ) } .
$$

$$
\left( \frac { d s } { d t } \right) ^ { 2 } = \frac { 1 } { k ^ { 2 } } ( 1 + k ^ { 2 } { v _ { 0 } } ^ { 2 } ) e ^ { - 2 g k ^ { 2 } s } - \frac { 1 } { k ^ { 2 } } .
$$

The maximum height, which is reached when the velocity becomes zero,is found from (36) to be

$$
S = \frac { 1 } { 2 g k ^ { 2 } } \log { ( 1 + k ^ { 2 } v _ { 0 } { } ^ { 2 } ) } .
$$

The time of reaching the highest point, which is found by putting $\frac { d s } { d t }$ equal to zero in (34), is given by

$$
T = \frac 1 { k g } \tan ^ { - 1 } { \left( v _ { 0 } k \right) } .
$$

When the particle falls the resistance acts in the opposite direction and the sign of the last term in (32) is changed.This may be accomplished by writing $\pmb { k } \pmb { \sqrt { - 1 } }$ instead of $k$ ,and if this change is made throughout the solution the results will be valid. Of course the results should be written in the exponential form, instead of the trigonometric as they were in (34) and (35),in order to avoid the appearance of imaginary expressions. If the initial velocity is zero, $v _ { 0 } = 0$ and the equations corresponding to (34), (35),and (36) are repectively

$$
\left\{ \begin{array} { c } { \displaystyle \frac { d s } { d t } = - \frac { 1 } { k } \frac { e ^ { k \sigma t } - e ^ { - k \sigma t } } { e ^ { k \sigma t } + e ^ { - k \sigma t } } , } \\ { \displaystyle e ^ { - \sigma k ^ { 2 } s } = \frac { e ^ { k \sigma t } + e ^ { - k \sigma t } } { 2 } , } \\ { \displaystyle \left( \frac { d s } { d t } \right) ^ { 2 } = \frac { 1 } { k ^ { 2 } } ( 1 - e ^ { 2 g k ^ { 2 } s } ) , } \end{array} \right.
$$

1. Show that

# IV. PROBLEMS.

$$
\frac { d ^ { 2 } s } { d t ^ { 2 } } = - k ^ { 2 } \frac { s } { \sqrt { s ^ { 6 } } } ,
$$

where the positive square root of $\vartheta ^ { \pmb { \theta } }$ is always taken,holds for the problem of Art.33 whichever side of the origin the particle may be. Integrate this equation.

2. Let $\ s = \ s ^ { \prime } - { \frac { g } { k ^ { 2 } } } t$ in equation (23)；integrate directly and show that the result is the same as that found by the variation of parameters.

3.Find equations (37) by direct integration of the differential equations.

4.Suppose a particle starts from rest and moves subject to a repulsive force varying inversely as the square of the distance; find the velocity and time elapsed in terms of the space described.

$$
\begin{array}{c} \begin{array} { r } { A n s . } \end{array} \left\{ \begin{array} { c } { v ^ { 2 } = 2 k ^ { 2 } \left( \frac { 1 } { \vartheta _ { 0 } } - \displaystyle \frac { 1 } { \vartheta } \right) , } \\ { k \sqrt { \frac { 2 } { s _ { 0 } } } t = \sqrt { s ^ { 2 } - s _ { 0 } s } + \displaystyle \frac { s _ { 0 } } { 2 } \log \left( \frac { \sqrt { s ^ { 2 } - s _ { 0 } s } + s - \displaystyle \frac { s _ { 0 } } { 2 } } { \displaystyle \frac { s _ { 0 } } { 2 } } \right) . } \end{array} \right.  \end{array}
$$

5.What is the velocity from infinity with respect to the sun at the earth's distance from the sun?

Ans． 42,220 meters, or 26.2 miles,per sec.

6.Suppose & particle moves subject to an attractive force varying directly as the distance, and to a resistance which is proportional to the speed; solve the differential equation by the gene al method for linear equations.

Ans.Let $k ^ { 2 }$ be the factor of proportionality for the velocity and $l ^ { 2 }$ for the distance. Then the solutions are

where

$$
\begin{array} { r } { s = c _ { 1 } e ^ { \lambda _ { 1 } t } + c _ { 2 } e ^ { \lambda _ { 2 } t } , } \end{array}
$$

$$
\left\{ { \begin{array} { l } { \lambda _ { 1 } = \frac { { - k ^ { 2 } + \sqrt { { k ^ { 4 } } - 4 { l ^ { 2 } } } } } { 2 } , } \\ { \lambda _ { 2 } = \frac { { - k ^ { 2 } - \sqrt { { k ^ { 4 } } - 4 { l ^ { 2 } } } } } { 2 } . } \end{array} } \right.
$$

Discuss more in detail the form of the solution and its physical meaning when $( a ) \ k ^ { 4 } - 4 l ^ { 2 } < 0 _ { ; }$ (6） $~ ) ~ k ^ { 4 } - 4 l ^ { 2 } = 0 ~$ （c） $k ^ { 4 } - 4 l ^ { 2 } > 0$

7. Suppose that in addition to the forces of problem 6 there is a force $\mu e ^ { \nu t }$ ； derive the solution by the method of the variation of parameters and discuss the motion of the particle.

8.Develop the method of the variation of parameters for a linear differential equation of the third order.

9.If $k ^ { 2 } = 0$ equation (23） becomes that which defines the motion of a freely falling body.Show that the limit of the solution (32) as $k ^ { 2 }$ approaches zero is

$$
\begin{array} { r } { s = s _ { 0 } + v _ { 0 } t - \frac { 1 } { 2 } g t ^ { 2 } . } \end{array}
$$

39.Parabolic Motion. There is a class of problems involving for their solution mathematical processes which are similar to those employed thus far in this chapter,although the motion is notina straight line. On account of the similarity in the analysis a short discussion of these problems will be inserted here.

Suppose the particle is subject to a constant acceleration downward; the problem is to find the character of the curve described when the particle is projected in any manner. The orbit will be in a plane which will be taken as the $\pmb { x y }$ -plane.Let the $\boldsymbol { y } \cdot \mathrm { \partial }$ -axis be vertical with the positive end directed upward. Then the differential equations of motion are

$$
\left\{ \begin{array} { l l } { \displaystyle { \frac { d ^ { 2 } x } { d t ^ { 2 } } = 0 , } } \\ { \displaystyle { \frac { d ^ { 2 } y } { d t ^ { 2 } } = - \mathrm { \nabla } g . } } \end{array} \right.
$$

Since these equations are independent of each other, they can be integrated separately, and give

$$
\left\{ \begin{array} { l l } { { x = a _ { 1 } t + a _ { 2 } , } } \\ { { } } \\ { { y = - \displaystyle \frac { g t ^ { 2 } } { 2 } + b _ { 1 } t + b _ { 2 } . } } \end{array} \right.
$$

Suppose ${ \boldsymbol { x } } = y = 0 , \ { \frac { d x } { d t } } = v _ { 0 } \cos \alpha , \ { \frac { d y } { d t } } = v _ { 0 } \sin \alpha$ when $t = 0$ ， where $\pmb { \alpha }$ is the angle between the line of initial projection and the plane of the horizon,and $v _ { 0 }$ is the speed of the projection. Then

![](images/c90b4f6a62dc78fae96bd34de24bc8d3f34b9b3db896887d7e02410c799a546e.jpg)  
Fig. 6.

the constants of integration are found to be

$$
\begin{array} { r l r } { a _ { 1 } = v _ { 0 } \cos \alpha , } & { { } } & { a _ { 2 } = 0 , } \\ { { \vphantom { \biggl | } } b _ { 1 } = v _ { 0 } \sin \alpha , } & { { } } & { b _ { 2 } = 0 ; } \end{array}
$$

and therefore

$$
\left\{ \begin{array} { l l } { x = v _ { 0 } \cos \alpha \cdot t , } \\ { \qquad } \\ { y = - { \frac { g t ^ { 2 } } { 2 } } + v _ { 0 } \sin \alpha \cdot t . } \end{array} \right.
$$

The equation of the curve described,which is found by eliminating $\pmb { t }$ between these two equations,is

$$
y = x \tan \alpha - { \frac { g \sec ^ { 2 } \alpha } { 2 { v _ { 0 } } ^ { 2 } } } x ^ { 2 } .
$$

This is the equation of a parabola whose axis is vertical with its vertex upward. It can be written in the form

$$
\begin{array} { r } { \left( x - \frac { { v _ { 0 } } ^ { 2 } } { g } \sin \alpha \cos \alpha \right) ^ { 2 } = - \frac { 2 { v _ { 0 } } ^ { 2 } } { g \sec ^ { 2 } \alpha } \left( y - \frac { { v _ { 0 } } ^ { 2 } \sin ^ { 2 } \alpha } { 2 g } \right) . } \end{array}
$$

The equation of a parabola with its vertex at the origin has the form

$$
x ^ { 2 } = - 2 p y ,
$$

where ${ \boldsymbol { 2 p } }$ is the parameter. On comparing this equation with the equation of the curve described by the particle,the coordinates of the vertex,or highest point,are seen to be

$$
\left\{ \begin{array} { l l } { \bar { x } = \displaystyle \frac { { v _ { 0 } } ^ { 2 } } { g } \sin \alpha \cos \alpha , } \\ { \quad } \\ { \bar { y } = \displaystyle \frac { { v _ { 0 } } ^ { 2 } } { 2 g } \sin ^ { 2 } \alpha . } \end{array} \right.
$$

The distance of the directrix from the vertex is one-fourth of the parameter;therefore the equation of the directrix is

$$
y = { \bar { y } } + { \frac { p } { 2 } } = { \frac { v _ { 0 } { } ^ { 2 } \sin ^ { 2 } \alpha } { 2 g } } + { \frac { v _ { 0 } { } ^ { 2 } \cos ^ { 2 } \alpha } { 2 g } } = { \frac { v _ { 0 } { } ^ { 2 } } { 2 g } } .
$$

The square of the velocity is found to be

$$
v ^ { 2 } = \left( { \frac { d x } { d t } } \right) ^ { 2 } + \left( { \frac { d y } { d t } } \right) ^ { 2 } = v _ { 0 } { } ^ { 2 } - 2 g y .
$$

To find the place where the particle will strike the horizontal plane put $y = 0$ in (40). The solutions for $_ { \pmb { x } }$ are $x = 0$ and

$$
\pmb { x } = \frac { 2 { v _ { 0 } } ^ { 2 } } { g } \sin \alpha \cos \alpha = \frac { { v _ { 0 } } ^ { 2 } } { g } \sin 2 \alpha .
$$

From this it follows that the range is greatest for a given initial velocity if $\alpha = 4 5 ^ { \circ }$ 。From (39) the horizontal velocity is seen to

be $v _ { 0 } \ \mathrm { c o s } \ \alpha$ ; hence the time of flight is $\frac { 2 v _ { 0 } } { g } \sin \alpha$ Therefore,if the other initial conditions are kept fixed，the whole time of flight varies directly as the sine of the angle of elevation.

The angle of elevation to attain a given range is found by solving

$$
x = a = { \frac { v _ { 0 } ^ { 2 } } { g } } \sin 2 \alpha
$$

for $_ \alpha$ If $a > \frac { v _ { 0 } { } ^ { 2 } } { g }$ there is no solution. If $a < \frac { \upsilon _ { 0 } { } ^ { 2 } } { g }$ there are two solutions differing from the value for maximum range $( \alpha = 4 5 ^ { \circ } )$ by equal amounts.

If the variation in gravity at different heights above the earth's surface, the curvature of the earth,and the resistance of the air are neglected, the investigation above applies to projectiles near the earth's surface. For bodies of great density the results given by this theory are tolerably accurate for short ranges. When the acceleration is taken toward the center of the earth,and gravity is supposed to vary inversely as the square of the distance,the path described by the particle is an ellipse with the center of the earth as one of the foci. This will be proved in the next chapter.

# V. PROBLEMS.

1.Prove that,if the accelerations parallel to the $\pmb { x }$ and $_ y$ -axes are any constant quantities,the path described by the particle is a parabola for general initial conditions. 2.Find the direction of the major axis,obtained in problem 1,in terms of the constant components of acceleration. 3.Under the assumptions of Art.39 find the range on a line making an angle $\pmb { \beta }$ with the $_ { \pmb { x } }$ -axis. 4.Show that the direction of projection for the greatest range on a given line passing through the point of projection is in a line bisecting the angle between the given line and the $\boldsymbol { y }$ -axis. 5.Show that the locus of the highest points of the parabolas as $\pmb { \alpha }$ takes allvaues is anllipe wosemjoraiis $\frac { v _ { 0 } { } ^ { 2 } } { g }$ and minor axis, $\frac { { \upsilon _ { 0 } } ^ { 2 } } { 2 g }$ - 6.Prove that the velocity at any point equals that which the particle would have at the point if it fell from the directrix of the parabola.

# THE HEAT OF THE SUN.

40. Work and Energy. When a force moves a particle against any resistance it is said to do work. The amount of the work is proportional to the product of the resistance and the distance through which the particle is moved. In the case of a free particle the resistance comes entirely from the inertia of the mass; if there is friction this is also resistance.

Energy is the power of doing work. If a given amount of work is done upon a particle free to move,the particle acquires a motion that will enable it to do exactly the same amount of work. The energy of motion is calied kinetic energy. If the particle is retarded by friction part of the original work expended will be used in overcoming the friction,and the particle will be capable of doing only as much work as has been done in giving it motion. Until about 1850 it was generally supposed that work done in overcoming friction is partly,or perhaps entirely,lost.In other words,it was believed that the total amount of energy in an isolated system might continually decrease. It was observed，however，that friction generates heat， sound, light,and electricity，depending upon the circumstances,and that these manifestations of energy are of the same nature as the original, but in a different form. It was then proved that these modified forms of energy are in every case quantitatively equivalent to the waste of that originally considered. The brilliant experiments of Joule and others,made in the middle of the nineteenth century，have established with great certainty the fact that the total amount of energy remains the same whatever changes it may undergo. This principle, known as the conservation of energy， when stated as holding throughout the universe, is one of the most far-reaching generalizations that has been made in the natural sciences in a hundred years.\*

41.Computation of Work. The amount of work done by a Newtonian force in moving a free particle any distance will now be computed. Let m equal the mass of the particle moved,and $k ^ { 2 }$ a constant depending upon the mass of the attracting body and the units employed. Then

$$
m { \frac { d ^ { 2 } s } { d t ^ { 2 } } } = - { \frac { k ^ { 2 } m } { s ^ { 2 } } } .
$$

\*Herbert Spencer regards the principle as being axiomatic,and states his views in regard to it in his First Principles,part 1.,chap. VI.

The right member is the force to which the particle is subject. By Newton's third law it is numerically equal to the reaction, or the resistance due to inertia. Then the work done in moving the particle through the element of distance $d s$ is

$$
m \frac { d ^ { 2 } s } { d t ^ { 2 } } d s = - \frac { k ^ { 2 } m } { s ^ { 2 } } d s = d W .
$$

The work done in moving the particle through the interval from ${ \pmb s } _ { 0 }$ to ${ \pmb s } _ { 1 }$ is found by taking the definite integral of this expression between the limits ${ \pmb s } _ { \bf 0 }$ and $\pmb { s _ { 1 } }$ ，On performing the integrations and substituting the limits,it is found that

$$
\frac { m } { 2 } \left( \frac { d s _ { 1 } } { d t } \right) ^ { 2 } - \frac { m } { 2 } \left( \frac { d s _ { 0 } } { d t } \right) ^ { 2 } = k ^ { 2 } m \left( \frac { 1 } { s _ { 1 } } - \frac { 1 } { s _ { 0 } } \right) .
$$

Suppose the initial velocity is zero; then the kinetic energy equals the work $\pmb { W }$ done upon the particle,and

$$
W = { \frac { m } { 2 } } \left( { \frac { d s _ { 1 } } { d t } } \right) ^ { 2 } = k ^ { 2 } m \left( { \frac { 1 } { s _ { 1 } } } - { \frac { 1 } { s _ { 0 } } } \right) .
$$

By hypothesis, the particle has no kinetic energy on the start, and therefore the power of doing work equals the product of one half the mass and the square of the velocity.  If the particle falls from infinity, $\pmb { \mathscr { s } } _ { 0 }$ is infinite, and the formula for the kinetic energy becomes

$$
{ \frac { m } { 2 } } \left( { \frac { d s _ { 1 } } { d t } } \right) ^ { 2 } = { \frac { k ^ { 2 } m } { s _ { 1 } } } .
$$

If the particle is stopped by striking a body when it reaches the point ${ \mathfrak { s } } _ { 1 }$ ，its kinetic energy is changed into some other form of energy such as heat. It has been found by experiment that a body weighing one kilogram falling 425 meters\* in the vicinity of the earth's surface,under the influence of the earth's attraction, generates enough heat to raise the temperature of one kilogram of water one degree Centigrade. This quantity of heat is called the calory.t The amount of heat generated is proportional to the product of the square of the velocity and the mass of the moving particle.Then，letting $\boldsymbol { \mathbf { \mathit { Q } } }$ represent the number of calories,it follows that

$$
Q = C m v ^ { 2 } .
$$

\* Joule found 423.5；Rowland 427.8. For results of experiments and references see Preston's Theory of Heat,p.594.

+ One-thousandth of this unit,defined in using the gram instead of the kilo gram,is also calleda calory.

Let m be expressed in kilograms and $v$ in meters per second. In order to determine the constant $c$ ,take $Q$ and m each equal to unity;then the velocity is that acquired by the body fallng through 425 meters.It was shown in Art.30 that,if the body falls from rest,

$$
\left\{ \begin{array} { l l } { s = - { \frac { 1 } { 2 } } g t ^ { 2 } , } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \end{array} \right.
$$

On eliminating $t$ between these equations,it is found that

$$
v ^ { 2 } = 2 g s .
$$

In the units employed $g = 9 . 8 0 9 4$ ，and since $s = 4 2 5$ and $v ^ { 2 } = 8 3 3 8$ ,it follows from (44) that

$$
C = { \frac { 1 } { 8 3 3 8 } } .
$$

Then the general formula (44) becomes

$$
Q = { \frac { m v ^ { 2 } } { 8 3 3 8 } } ,
$$

where $Q$ is expressed in calories if the kilogram,meter,and second are taken as the units of mass,distance,and time.

42. The Temperature of Meteors. The increase of temperature of a body，when the proper units are employed,is equal to the number of calories of heat acquired divided by the product of the mass and the specific heat of the substance. Suppose a meteor whose specifc heat is unity (in fact it would probably be much less than unity) should strike the earth with any given velocity;it is required to compute its increase of temperature if it took up all the heat generated. The specific heat has been taken so that the increase of temperature is numerically equal to the number of calories generated per unit mass. Meteors usually strike the earth with a velocity of about 25 miles,or 40,233 meters,per second. On substituting 40,233 for $v$ and unity for m in (45),it is found that $T = Q = 1 9 4 , 1 3 4$ ， the number of calories generated per unit mass,or the number of degrees through which the temperature of the meteor would be raised. As a matter of fact a large part of the heat would be imparted to the atmosphere； but the quantity of heat generated is so enormous that it could not be expected that any but the largest meteors would last long enough to reach the earth's surface.

A meteor falling into the sun from an infinite distance would strike its surface,as has been seen in Art.36,with a velocity of about 384 miles per second. The heat generated would be therefore $( \frac { 3 8 4 } { 2 5 } ) ^ { 2 }$ ,or 236, times as great as that produced in striking the earth. Thus it follows that a kilogram would generate, in faling into the sun,45,815,624 calories.

43.The Meteoric Theory of the Sun's Heat. When it is remembered what an enormous number of meteors (estimated by H.A.Newton\* as being as many as 8,0o0,00o daily） strike the earth,it is easily conceivable that enough strike the sun to maintain its temperature. Indeed, this has been advanced as a theory to account for the replenishment of the vast amount of heat which the sun radiates. There can be no question of its qualitative correctness,and it only remains to examine it quantitatively.

Let it be assumed that the sun radiates heat equally in every direction,and that meteors fall upon it in equal numbers from every direction. Under this assumption,the amount of heat radiated by any portion of the surface will equal that generated by the impact of meteors upon that portion. The amount of heat received by the earth will be to the whole amount radiated from the sun as the surface which the earth subtends as seen from the sun is to the surface of the whole sphere whose radius is the distance from the earth to the sun. The portion of the sun's surface which is within the cone whose base is the earth and vertex the center of the sun,is to the whole surface of the sun as the surface subtended by the earth is to the surface of the whole sphere whose radius is the distance to the sun. Therefore,the earth receives as much heat as is radiated by,and consequently generated upon,the surface cut out by this cone. But the earth would intercept precisely as many meteors as would fall upon this small area,and would, therefore,receive heat from the impact of a certain number of meteors upon itself,and as much heat from the sun as would be generated by the impact of an equal number upon the sun.

The heat derived by the earth from the two sources would be as the squares of the velocities with which the meteors strike the earth and sun. It was seen in Art. 42 that this number is $\frac { 1 } { 2 } \frac { 1 } { 3 6 }$ Therefore,if this meteoric hypothesis of the maintenance of the sun's heat is correct, the earth should receive $\frac { 1 } { 2 \Im \Im }$ as much heat from the impact of meteors as from the sun. This is certainly millions of times more heat than the earth receives from meteors, and consequently the theory that the sun's heat is maintained by the impact of meteors is not tenable.

44.Helmholtz's Contraction Theory. The amount of work done upon a particle is proportional to the product of the resistance overcome by the distance moved. There is nothing whatever said about how long the motion shall take,and if the work is converted into heat the total amount is the same whether the particle falls the entire distance at once,or covers the same distance by a succession of any number of shorter falls. When a body contracts it is equivalent to a succession of very short movements of all its particles in straight lines toward the center,and it is evident that, knowing the law of density, the amount of heat which will be generated can be computed.

In 1854 Helmholtz applied this idea to the computation of the heat of the sun in an attempt to explain its source of supply. He made the supposition that the sun contracts in such a manner that it always remains homogeneous. While this assumption is certainly incorrect,nevertheless the results obtained are of great value and give a good idea of what doubtless actually takes place under contraction. The mathematical part of the theory is given in the Philosophical Magazine for 1856,p. 516.

Consider a homogeneous gaseous sphere whose radius is $R _ { 0 }$ and density $\pmb { \sigma }$ Let $M _ { 0 }$ represent its mass. Let dM represent an element of mass taken anywhere in the interior or at the surface of the sphere.Let $\boldsymbol { R }$ be the distance of dM from the center of the sphere,and let $M$ represent the mass of the sphere whose radius is $\boldsymbol { R }$ ：The element of mass in polar coordinates is (Art.21)

$$
d M = \sigma R ^ { 2 } \cos \phi d \phi d \theta d R .
$$

The element is subject to the attraction of the whole sphere within it. As will be shown in Chapter IV, the attraction of the spherical shell outside of it balances in opposite directions so that it need not be considered in discussing the forces acting upon $d M$ Every element in the infinitesimal shell whose radius is $\scriptstyle { R }$ is attracted toward the center by a force equal to that acting on $d M$ ； therefore the whole shell can be treated at once.Let $d M _ { s }$ represent the mass of the elementary shell whose radius is $\boldsymbol { R }$ It is found by integrating (46) with respect to $\theta$ and $\phi$ Thus

$$
d M _ { \ast } = \sigma R ^ { 2 } d R \int _ { 0 } ^ { 2 \pi } \left\{ \int _ { - \frac { \pi } { 2 } } ^ { \frac { \pi } { 2 } } \cos \phi d \phi \right\} d \theta = 4 \pi \sigma R ^ { 2 } d R .
$$

The force to which $d M _ { s }$ is subject is kM dM..The element of work done in moving $d M _ { s }$ through the element of distance $\scriptstyle { d R }$ is

$$
d W _ { s } = { } - d M _ { s } \frac { k ^ { 2 } M } { R ^ { 2 } } d R .
$$

The work done in moving the shell from the distance $c R$ to $\scriptstyle { R }$ is the integral of this expression between the limits $\mathit { C R }$ and $\pmb { R }$ or

$$
W _ { s } = \mathrm { ~ - ~ } d M _ { s } k ^ { 2 } M { \int } _ { c R } ^ { R } \frac { d R } { R ^ { 2 } } = \frac { d M _ { s } k ^ { 2 } M } { R } \biggl ( \frac { C - 1 } { C } \biggr ) .
$$

But $\begin{array} { r } { M = { \frac { 4 } { 3 } } \pi \sigma R ^ { 3 } } \end{array}$ ； hence,substituting the value of $d M _ { s }$ from (47) and representing the work done on the elementary shell by $\pmb { W _ { s } } = d \pmb { W }$ ,it follows that

$$
d W = { \frac { 1 6 } { 3 } } \pi ^ { 2 } \sigma ^ { 2 } k ^ { 2 } \left( { \frac { C - 1 } { C } } \right) R ^ { 4 } d R .
$$

The integral of this expression from 0 to $R _ { 0 }$ gives the total amount of work done in the contraction of the homogeneous sphere from radius $\mathit { C R } _ { 0 }$ to $\scriptstyle { R _ { 0 } }$ That is,

$$
W = { \frac { 1 6 } { 3 } } \pi ^ { 2 } \sigma ^ { 2 } k ^ { 2 } \left( { \frac { C - 1 } { C } } \right) \int _ { 0 } ^ { \mathcal { R } _ { 0 } } R ^ { 4 } d R = { \frac { 1 6 } { 1 5 } } \pi ^ { 2 } \sigma ^ { 2 } k ^ { 2 } \left( { \frac { C - 1 } { C } } \right) R _ { 0 } \mathfrak { s } ,
$$

which may be written

$$
W = \frac { 3 } { 6 } k ^ { 2 } \left( \frac { C - 1 } { C } \right) \frac { M _ { 0 } ^ { 2 } } { R _ { 0 } } .
$$

If $c$ equals infinity, then

$$
\begin{array} { r } { W = \frac { 8 } { 6 } k ^ { 2 } \frac { \overline { { M _ { 0 } } } ^ { 2 } } { R _ { 0 } } . } \end{array}
$$

If the second is taken as the unit of time,the kilogram as the unit of mass,and the meter as the unit of distance,and if $k ^ { 2 }$ is computed from the value of $\pmb { g }$ for the earth,then,after dividing $\pmb { W }$ by $\frac { 8 3 3 8 } { 2 }$ ,the result will be numerically equal to the amount of heat in calories that will be generated if the work is all transformed into this kind of energy. The temperature to which the body will be raised,which is this quantity divided by the product of the mass and the specific heat,is

$$
T = \frac { Q } { \eta M _ { 0 } } = \frac { 2 W } { 8 3 3 8 \eta M _ { 0 } } ,
$$

where $\pmb { \eta }$ is the specific heat of the substance. Or, substituting (48) in (50),it is found that

$$
T = \frac { 3 k ^ { 2 } } { 5 \eta } \cdot \frac { C - 1 } { C } \cdot \frac { M _ { 0 } } { R _ { 0 } } \cdot \frac { 2 } { 8 3 3 8 } .
$$

By definition, $k ^ { 2 }$ is the attraction of the unit of mass at unit distance； therefore,if $\mathbf { \nabla } m _ { \mathbf { \nabla } }$ is the mass of the earth and $\pmb { r }$ its radius, it follows that

$$
g = { \frac { k ^ { 2 } m } { r ^ { 2 } } } .
$$

On solving for $k ^ { 2 }$ and substituting in (51),the expression for $\pmb { T }$ becomes

$$
T = \frac { 3 ( C - 1 ) } { 5 \eta C } \cdot \frac { r ^ { 2 } } { R _ { 0 } } \cdot \frac { M _ { 0 } } { m } \cdot \frac { 2 g } { 8 3 3 8 } .
$$

If the body contracted from infinity $\mathbf { \nabla } \cdot \mathbf { C } = \mathbf { \nabla } \infty$ ),the amount of heat generated would be sufficient to raise its temperature $\pmb { T }$ degrees Centigrade,where $\pmb { T }$ is given by the equation

$$
T = \frac { 3 } { 5 } \cdot \frac { 1 } { \eta } \cdot \frac { r ^ { 2 } } { R _ { 0 } } \cdot \frac { M _ { 0 } } { m } \cdot \frac { 2 g } { 8 3 3 8 } .
$$

Suppose the specific heat is taken as unity,which is that of water.\* The value of $\pmb { \mathscr { g } }$ is 9.8094 and

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { r ^ { 2 } } { R _ { 0 } } = 1 1 6 , 3 5 6 , } \\ { \displaystyle M _ { 0 } } \\ { \displaystyle \frac { M _ { 0 } } { m } = 3 3 2 , 0 0 0 . } \end{array} \right.
$$

On substituting these numbers in (53) and reducing,it is found that

Therefore, the sun contracting from infinity in such a way as to always remain homogeneous would generate enough heat to raise the temperature of an equal mass of water more than fifty-four millions of degrees Centigrade.

If it is supposed that the sun has contracted only from Neptune's orbit equation (52) can be used,which will give a value of $\pmb { T }$ about $\frac { 1 } { 6 \textcircled { 6 } 0 0 }$ less.In any case it is not intended to imply that it did ever contract from such great dimensions in the particular manner assumed；the results given are nevertheless significant and throw much light on the question of evolution of the solar system from a vastly extended nebula. If the contraction of the

\* No other ordinary terrestrial substance hag a specific heat so great ag unity except hydrogen gas, whose specific heat is 3.409. But the lighter gases of the solar &tmosphere may also have high values.

sun were the only source of its energy, this discussion would give & rather definite idea as to the upper limit of the age of the earth. But the limit is so small that it is not compatible with the conclusions reached by several lines of reasoning from geological evidence,and it is utterly at variance with the age of certain uranium ores computed from the percentage of lead which they contain. The recent discovery of enormous sub-atomic energies which become manifest in the disintegration of radium and several other substances prove the existence of sources of energy not heretofore considered,and suggest that the sun's heat may be supplied partly,if not largely,from these sources.It is certainly unsafe at present to put any limits on the age of the sun.

The experiments of Abbott have shown that, under the assumption that the sun radiates heat equally in every direction，the amount of heat emitted yearly would raise the temperature of a mass of water equal to that of the sun 1.44 degrees Centigrade. In order to find how great a shrinkage in the present radius would be required to generate enough heat to maintain the present radiation10,000 years,substitute 14,400 for $\boldsymbol { T }$ in (52) and solve for $C$ On carrying out the computation,it is found that

$$
C = 1 . 0 0 0 5 2 8 .
$$

Therefore, the sun would generate enough heat in shrinking about one four-thousandth of its present diameter to maintain its present radiation 10,000 years.

The sun's mean apparent diameter is $1 9 2 4 ^ { \prime \prime }$ ， so a contraction of its diameter of .0oo528 would make an apparent change of only $1 . { } ^ { \prime \prime } 0 _ { : }$ ，a quantity far too smallto be observed on such an object by the methods now in use. On reducing the shrinkage to other units,it is found that a contraction of the sun's radius of 36.8 meters annually would account for all the heat that is being radiated at present.

# VI. PROBLEMS.

1.According to the recent work of Abbott,of the Smithsonian Institution, a square meter exposed perpendicularly to the sun's rays at the earth's distance would receive 19.5 calories per minute. The average amount received per square meter on the earth's surface is to this quantity as the area of a circle is to the surface of a sphere of the same radius,or 1 to 4.The earth's surface receives,therefore,on the &verage 5 calories per square meter per minute. How many kilograms of meteoric matter would have to strike the earth with a velocity of 25 miles (40,233 meters) per sec.to generate $\texttt { T } _ { 3 } ^ { 1 } \texttt { F }$ this amount of heat?

2.How many pounds would have to fall per day on every square mile on the average? Tons on the whole earth?

$$
\left\{ \begin{array} { l l } { 9 1 7 \ { \mathrm { p o u n d s } } . } \\ { 9 0 , 3 0 0 , 0 0 0 \ { \mathrm { t o n s } } . } \end{array} \right.
$$

3.Find the amount of work done in the contraction of any fraction of the radius of a sphere when the law of density is $\sigma = \frac { l } { R ^ { 2 } }$ ·

Ans $W = 1 6 \pi ^ { 2 } k ^ { 2 } l ^ { 2 } \left( \frac { \textit { C } - 1 } { \textit { C } } \right) \cdot R = k ^ { 2 } \left( \frac { \textit { C } - 1 } { \textit { C } } \right) \cdot \frac { M _ { 0 } ^ { 2 } } { R _ { 0 } } ,$ R，orof the work done when the sphere is homogeneous.

4.Laplace assumed that the resistance of a fluid against compression is directly proportional to its density,and on the basis of this assumption he found that the law of density of a spherical body would be

$$
\sigma = \frac { G \sin { \left( \mu \frac { R } { a } \right) } } { \frac { R } { a } } ,
$$

where $\pmb { G }$ and $\pmb { \mu }$ are constants depending on the material of which the body is composed,and where $^ { a }$ is the radius of the sphere.This law of density is in harmony，when applied to the earth,with a number of phenomena,such as the precession of the equinoxes. Find the amount of heat generated by contraction from infinite dimensions to radius $\scriptstyle { \mathcal { R } } _ { 0 }$ of a body having the Laplacian law of density.

5.Find how much the heat generated by the contraction of the earth from the density of meteorites,3.5,to the present density of 5.6 would raise the temperature of the whole earth,assuming that the specific heat is 0.2.

Ans. $\pmb { T } = 6 5 2 0 . 5$ degrees Centigrade.

# HISTORICAL SKETCH AND BIBLIOGRAPHY.

The laws of falling bodies under constant acceleration were investigated by Galileo and Stevinus,and for many cases of variable acceleration by Newton. Such problems are comparatively simple when treated by the analytical processes which have come into use since the time of Newton. Parabolic motion was discussed by Galileo and Newton.

The kinetic theory of gases seems to have been first suggested by J.Bernouilli about the middle of the 18th century,but it was first developed mathematically by Clausius. Maxw.ll, Boltzmann,and O.E.Meyer have made important contributions to the subject,and more recently Burbury，Jeans, and Hilbert. Some of the principal books on the subject are:Risteen's Molecules and the Molecular Theory (descriptive work)；L.Boltzmann's Gastheorie;H.W.Watson's Kinetic Theory of Gases;O.E.Meyer's Die Kinetische Theorie der Gase;S.H.Burbury's Kinetic Theory of Gases;J.H.Jean's Xinetic Theory of Gases.

The meteoric theory of the sun's heat was first suggested by R. Mayer. The contraction theory was first announced in a public lecture by Helmholtz at Konigsberg Feb.7,1854,and was published later in Phil.Mag.1856. An important paper by J.Homer Lane appeared in the Am.Jour.of Sci. July,187o.The amount of heat generated depends upon the law of density of the gaseous sphere.Investigations covering this point are 16 papers by Ritter in Wiedemann's Annalen,vol.v.,1878,to vol.xx.,1883;by G.W.Hill, Annals of Math.,vol.Iv.,1888;and by G.H.Darwin,Phil.Trans.,1888.The original papers must be read for an exposition of the subject of the heat of the sun.Sub-atomic energies are discussed in E.Rutherford's Radioactive Substances and their Radiations.

For evidences of the great age of the earth consult Chamberlin and Salis bury's Geology,vol.I1.,and vol.I1., p.413 et seq.； for a general discussion of the age of the earth see Arthur Holmes'The Age of the Earth.
