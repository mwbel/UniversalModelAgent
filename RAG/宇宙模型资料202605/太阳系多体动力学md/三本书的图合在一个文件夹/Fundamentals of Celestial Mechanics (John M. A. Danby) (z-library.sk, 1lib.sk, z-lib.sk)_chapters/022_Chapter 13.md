# Chapter 13

# The Earth and its Rotation

# 13.1 The Eulerian Motion of the Earth

The Earth is not a sphere, and in this chapter we shal consider some of the consequences of this. We shall assume that the Earth has symmetry about an axis and can be represented by $\clubsuit$ spheroid for which $a = b > c ;$ but the Earth is not homogeneous, and we must be wary of using the formulas for the field of a homogeneous spheroid. Let the moments of inertia of the Earth about the axes (the principal axes of inertia of the spheroid) be $A , B$ and $\pmb { C }$ Then $A = B < C$

First we shall consider the rotation of the Earth when no outside forces are acting on it. Then,in Euler's equations, (5.2.7), $\Sigma = \emptyset$ ,and

$$
\begin{array} { r l r } & { } & { \displaystyle { A \frac { \dot { d } \omega _ { 1 } } { d t } - ( A - C ) \omega _ { 2 } \omega _ { 3 } = 0 } , } \\ & { } & { \displaystyle { A \frac { \dot { d } \omega _ { 2 } } { d t } - ( C - A ) \omega _ { 3 } \omega _ { 1 } = 0 } , } \\ & { } & { \displaystyle { C \frac { \dot { d } \omega _ { 3 } } { d t } } \qquad = 0 . } \end{array}
$$

From (13.1.3) we have

$$
{ \boldsymbol { \omega } } _ { 3 } = \cos \tt { s } _ { \mathrm { ~ } } ^ { \ddag } { \boldsymbol { \mathrm { a } } } \ m { \ddag } ,
$$

so that the spin of the Earth about its axis of symmetry is constant. Let

$$
{ \mathfrak { r } } = { \frac { C - A } { A } } \omega _ { 3 } { \mathrm { ; } }
$$

then the first two equations become

and

$$
\begin{array} { l } { \displaystyle { \frac { d \omega _ { 1 } } { d t } + n \omega _ { 2 } = 0 } } \\ { \displaystyle { } } \\ { \displaystyle { \frac { d \omega _ { 2 } } { d t } - n \omega _ { 1 } = 0 . } } \end{array}
$$

$$
\frac { \bar { d } ^ { 2 } \omega _ { \bar { z } } } { \bar { d } \bar { z } ^ { 2 } } + n ^ { 2 } \omega _ { 1 } = 0 ,
$$

and similarly,

$$
\frac { d ^ { 2 } \omega _ { 2 } } { d t ^ { 2 } } + n ^ { 2 } \omega _ { 2 } = 0 .
$$

The general solution of equations (13.1.5) is, then,

$$
\begin{array} { l } { \omega _ { \bar { 4 } } = \alpha \cos ( n t + \beta ) , } \\ { \omega _ { \bar { 2 } } = \alpha \sin ( n \bar { t } + \beta ) . } \end{array}
$$

The period of these terms, measured in sidereal days,so that $\omega _ { 3 } = 2 \pi$ ,is

$$
{ \frac { 2 \pi } { \pi } } = { \frac { A } { C - A } } .
$$

From other sources the value of this is known to be about 303,so that the period is 303 sidereal days,or 302 mean solar days.This is called the Eulerian free period.

A consequence can be considered as follows. Let $\mathcal { P }$ bea point on the Earth, and with origin at the center of the Earth,and $\theta z$ pointing along the direction f $\omega _ { 3 }$ ,let $\mathcal { O } x$ meet the meridian through $P$ (See Figure 13.1.）The angular velocity of the Earthis

$$
\omega _ { 1 } \hat { \mathbf { x } } + \omega _ { 2 } \hat { \mathbf { y } } + \omega _ { 3 } \hat { \mathbf { z } } ,
$$

so that it has direction cosines proportional to $\omega _ { 1 } , \omega _ { 2 }$ ,and $\omega _ { 3 }$ Let the instantaneous axis of rotation cut the Earth near the north pole at $\pmb { \xi }$ ；then the equation of the line $0 I$ is

$$
\begin{array} { r } { \frac { x } { \omega _ { 1 } } = \frac { y } { \omega _ { 2 } } = \frac { z } { \omega _ { 3 } } , } \end{array}
$$

or

$$
{ \frac { x } { \alpha \cos ( n t + \beta ) } } = { \frac { y } { \alpha \sin ( n t + \beta ) } } = { \frac { z } { \omega _ { 3 } } } .
$$

Therefore the angle $\sqrt { 2 }$ is $a _ { j } = a _ { 3 }$ ,and the component of $\mathbb { N } _ { \xi } ^ { \xi }$ along $\Im \mathcal { P }$ is

$$
N Q = { \frac { \alpha } { \omega _ { 3 } } } \cos ( n \mathbf { \vec { \tau } } + \beta ) .
$$

Now the latitude of $P$ measured with respect to the axis of rotation, is nearly

$$
9 0 ^ { \circ } - P Q = 9 0 ^ { \circ } - P N + \frac { \alpha } { \omega _ { 3 } } \cos ( n \pm \beta ) .
$$

$$
V = - { \frac { G M } { 4 } } - { \frac { G ( A + B + C - 3 I ) } { 2 r ^ { 3 } } } .
$$

Diferentiating the first,and using the second to eliminate du2/dt, we find $\mathcal { P N }$ is constant, so that the Eulerian oscillation should give rise to a variation in the latitude of $\mathcal { P }$ with period approximately ten months.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0201-0240/ocr/images/4fa0784a3b0c20181ff7383c533b5522b6e9c783cab929f3452bb46fe1cc30d6.jpg)  
Figure 13.1

The latitude of a point can be found very accurately by astronomical observations,and it is known from these that it does,in fact,vary.But the empirical formula for the latitude demands two periodic terms (as opposed to one in (13.1.8))；one of these has amplitude $0 ^ { \prime \prime } . 0 9$ and period one year,and the other has amplitude $0 ^ { t / t } . 1 8$ and period 14 months.The first is probably due to periodic changes in the moments of inertia of the Earth resulting from seasonal changes in the weather. The second might be the modification of the Eulerian free oscillation produced by the nonrigidity of the Earth. For,suppose the Earth had no rigidity,or that it was composed of nonviscous fuid; the two equal axes must always be perpendicular to the instantaneous axis of rotation;hence there can be no free oscillation of this sort.Therefore,as the rigidity of the Earth diminished, the Eulerian free period would increase until it became infinite for the case of no rigidity. There are, however, other possible explanations for the second term,and it may be that the actual Eulerian free oscillation simply hasan amplitude too small to be detected.

# 13.2 The Couple Exerted on the Earth by a Distant Body

Consider MacCullagh's formula for the potential of a body at a distant point,(5.4.1）:

Let the origin be at the center of mass of the body,and let the axes be the principal axes of inertia. The force exerted on a distant unit mass at r is $- \sqrt { \sqrt [ 3 ] { 4 } }$ and from Newton's third law the distant mass exerts an equal and opposite force on the body. This results in a couple of moment $\pmb { \tau } \times \pmb { \nabla } \pmb { \nu }$ about the origin, exerted by the distant unit mass.

This couple is the result of the lack of spherical symmetry of the body, which expresses itself in the fact that $\pmb { \zeta }$ is not just a function of $\pmb { \mathscr { r } }$ but involves $\pmb { \mathcal { x } }$ $y$ and $z$ in addition. Therefore, in finding the couple, we can ignore all those parts of $\pmb { \gamma }$ that are simply functions of $\pmb { \mathcal { F } }$

Now

$$
\xi = { \frac { A x ^ { 2 } + B y ^ { 2 } + C z ^ { 2 } } { r ^ { 2 } } }
$$

and so provides the only part of $\pmb { \updownarrow }$ about which we need worry; call this

$$
\begin{array} { l } { \displaystyle { V _ { \mathrm { i } } = \frac { 3 G J } { 2 r ^ { 3 } } } } \\ { \displaystyle { \phantom { \frac { J } { J } } = \frac { 3 G } { 2 r ^ { 5 } } ( A x ^ { 2 } \div B y ^ { 2 } + C z ^ { 2 } ) } . } \end{array}
$$

The evaluation of $\mathfrak { x } \times \nabla \mathbb { V } = \mathfrak { x } \times \nabla \mathbb { V } _ { 1 }$ is straightforward; the couple is

$$
{ \bf { I } } = \frac { 3 G } { r ^ { 5 } } \left( { ( C - B ) y z , ~ ( A - C ) z x , ~ ( B - A ) x y } \right) ) .
$$

# 13.3 The Couples Exerted on the Earth by the Sun and Moon

With origin at the center of the Earth, take axes $\mathbb { E } x , \mathbb { E } y .$ and $\mathcal { E } z$ such that Er points toward the vernal equinox and $\Sigma z$ points toward the north celestial pole;also $E \lambda , \ E Y$ ，and $\pmb { { Z Z } }$ such that $\Sigma X$ points toward the vernal equinox and $\sum Z$ points toward the north pole of the ecliptic. (See Figure 13.2). The relations between coordinates are

$$
\begin{array} { l } { x = X , } \\ { y = Y \cos \epsilon - Z \sin \epsilon , , } \\ { z = Y \sin \epsilon + Z \cos \epsilon . . } \end{array}
$$

ere $\boldsymbol { \varepsilon }$ is the obliquity of the ecliptic, assumed to be constant.

f $\beta$ is the ascending node of the Moon's orbit, then

$$
X \Omega = - g \dddot { \iota } + \mathfrak { C } \mathfrak { O } \mathfrak { V } \mathfrak { L } \mathfrak { a } \mathfrak { H } ,
$$

where $g$ is the rate of regression of the node in the ecliptic (all periodic perturbations being neglected).

Let k be the inclination of the Moon's orbit to the ecliptic; since it is small, we shall neglect $\bar { \hbar } ^ { 2 }$ so that sin $k = \ k$ and $\cos \overrightarrow { \ast } = \overrightarrow { \ddag }$ To this order, we see that after a time $t , \ \beta _ { 4 }$ will regress through an angle $g \dot { \varepsilon }$ with respect to the Moon's orbit.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0201-0240/ocr/images/972f7c746338ed0102d8485366b9a2d971c3d9112cb3d0e75743ae6178af0f43.jpg)  
Figure 13.2

Let $\scriptstyle { \hat { \mathbf { r } } } 2$ and $\mathfrak { R } _ { 1 }$ be the mean motions of the Moon and Sun, respectively; then

$$
\begin{array} { c } { X S = n _ { \perp } t + \alpha , } \\ { X M _ { 1 } = X \Omega + \Omega M } \\ { = n t + \beta , } \\ { \Omega M = n t + g t + \gamma , } \end{array}
$$

where $_ \alpha$ ， $\beta$ and $\gamma$ are constants, and the meridian through $\mathcal { Z }$ and $\mathbb { M }$ meets the ecliptic at $i \hbar f _ { 1 }$ .Then

$$
\begin{array} { r } { \sin M \mathbb { M } _ { 1 } = \sin k \sin \Omega \mathbb { M } } \\ { = k \sin ( n t + g _ { \bar { \imath } } ^ { \sf t } \div \gamma ) . } \end{array}
$$

Let R and r be the distances (assumed constant) of the Sun and the Moon. Then we have the values of $\{ X , Y , Z \}$ for the Sun.

$$
\vec { \mathcal { R } } \left( \cos ( n _ { 1 } t + \alpha ) , \ \sin ( n _ { 1 } t + \alpha ) , \ 0 \right) ,
$$

and for the Moon,

$$
r \left( \cos ( n t + \beta ) , \ \sin ( n t + \beta ) , \ k \sin ( n t + g t + \gamma ) \right) .
$$

Then from (13.3.1) we find the values of $( x , y , z )$

$$
R ( \cos ( n _ { 1 } t + \alpha ) , \ \sin ( n _ { 1 } t + \alpha ) \cos \epsilon , \ \sin ( n _ { 1 } t + \alpha ) \sin \epsilon )
$$

for the Sun,and

$$
\begin{array} { r } { r ( \cos ( n t + \beta ) , \ \sin ( n t + \beta ) \cos \epsilon - \tilde { k } \sin ( n t + g t + \gamma ) \sin \epsilon , \quad } \\ { \sin ( n t + \beta ) \sin \epsilon + \tilde { k } \sin ( n t + g t + \gamma ) \cos \epsilon ) } \end{array}
$$

for the Moon.

Let the masses of the Sun and Moon be $\mathbb { M } _ { s }$ and $M _ { m }$ ,and let them exert couples $s ^ { \mathbb { T } }$ and $\yen 12$ on the Earth. From (13.2.1),using the property $A = B$ ,we find

$$
\left. \begin{array} { l } { \displaystyle _ { s } \Gamma _ { x } = \frac { 3 M _ { s } G } { R ^ { 3 } } ( C - A ) \sin ^ { 2 } ( n _ { 1 } t + \alpha ) \cos \epsilon \sin \epsilon , } \\ { \displaystyle _ { s } \Gamma _ { y } = \frac { 3 M _ { s } G } { R ^ { 3 } } ( A - C ) \sin ( n _ { 1 } t + \alpha ) \cos ( n _ { 1 } t + \alpha ) \sin \epsilon , } \\ { \displaystyle _ { s \Gamma _ { z } = 0 . } } \end{array} \right]
$$

These expressions are to be used in a moment to establish the existence of the precession of the Earth's axis of rotation; this takes 26,o00 years for a complete cycle, so that we are certainly justified in neglecting the annual variations in the expressions (13.3.4). If we take averages over one year,the $y .$ component vanishes,and we are left with

$$
s ^ { \overline { { \Gamma } } } \overline { { { x } } } = \frac { 3 M _ { s } G } { 4 R ^ { 3 } } ( C - A ) \sin 2 \epsilon .
$$

Similarly, we have for the couple exerted by the Moon,

$$
\begin{array} { l } { { { \displaystyle { \it \Pi } _ { m } \Gamma _ { x } = \frac { 3 M _ { m } G } { r ^ { 3 } } ( C - A ) \left\{ \sin ^ { 2 } ( n t + \beta ) \sin \epsilon \cos \epsilon \right. } \ } _ { } } \\ { { \left. \qquad + k \sin ( n t + \beta ) \sin ( n t + g t + \gamma ) \cos 2 \epsilon \right\} } , } \\ { { { \it \Pi } _ { m } \Gamma _ { y } = \frac { 3 M _ { m } G } { r ^ { 3 } } ( A - C ) \left\{ \cos ( n t + \beta ) \sin ( n t + \beta ) \sin \epsilon \right. } } \\ { { \left. \qquad + k \cos ( n t + \beta ) \sin ( n t + g t + \gamma ) \cos \epsilon \right\} , } } \\ { { { \it \Pi } _ { m } \Gamma _ { z } = 0 . } } \end{array}
$$

Consider the mean values taken over one sidereal month. We have

$$
\begin{array} { r l } & { \sin ( n t + g t + \gamma ) = \sin \left[ ( n t + \beta ) + ( g t - \beta + \gamma ) \right] } \\ & { \phantom { \sin \alpha \sin \beta \sin \gamma \sin \alpha \sin \beta \sin \gamma \sin \alpha \sin \beta \sin \gamma \sin \alpha \sin \beta \sin \gamma \sin \alpha \sin \beta \sin \gamma \sin \alpha \beta \sin \gamma \sin \alpha \beta \sin \gamma \sin \alpha \beta \sin \gamma } = \sin ( n t + \beta ) \cos ( g t - \beta + \gamma ) + \cos ( n t + \beta ) \sin ( g t - \beta + \gamma ) , } \end{array}
$$

so that the mean values are

$$
\begin{array} { l } { { _ { m } \widehat \Gamma _ { x } = \displaystyle \frac { 3 M _ { m } G } { r ^ { 3 } } ( C - A ) \left\{ \frac 1 4 \sin 2 \epsilon + \displaystyle \frac { k } { 2 } \cos ( g t - \beta + \gamma ) \cos 2 \epsilon \right\} , } } \\ { { _ { m } \widehat \Gamma _ { y } = \displaystyle \frac { 3 M _ { m } G } { r ^ { 3 } } ( A - C ) \displaystyle \frac { k } { 2 } \sin ( g t - \beta + \gamma ) \cos \epsilon . } } \end{array}
$$

Finally,if we average over the period of revolution of the nodes (still short compared with 26,000 years), the only nonzero term is

$$
{ } _ { m } \overline { { \widehat { \Gamma } } } _ { x } = \frac { 3 M _ { m } G } { 4 x ^ { 3 } } ( C - A ) \sin 2 \epsilon .
$$

Therefore the mean value of the total couple exerted by the Sun and Moon on the Earth, taken over a period of about nineteen years,acts along the $\boldsymbol { \mathfrak { x } }$ -axis and has magnitude

$$
\begin{array} { r } { \widetilde { \Gamma } = \displaystyle \frac { 3 G } { 4 } ( C - A ) \sin 2 \epsilon \left( \frac { M _ { m } } { r ^ { 3 } } + \frac { M _ { s } } { R ^ { 3 } } \right) . } \end{array}
$$

If we substitute numerical values for the masses and distances, we see that the Moon contributes about two-thirds of the total.

# 13.4 The Lunisolar Precession

In this section we shall consider analytically the consequences of the mean couple, (13.3.8), acting on the spinning Earth; this consequence is the lunisolar precession of the Earth's axis. But before doing this we shall consider a qualitative explanation for the precession.

From the reasoning in Section 12.3, we see that a close satellite of the Earth, moving in a circular orbit,would suffer a regresson of its line of nodes,due to the perturbations of the Moon and Sun. The inclination of its orbit to the ecliptic would suffer no secular perturbation. Suppose the satellite initially had an orbit in the plane of the Earth's equator; the plane of the orbit would not remain equatorial but would lag behind. But now suppose the satellite to be fastened to the Earth; it would try to force the plane of the Earth's equator to regress,following the plane of its orbit.

Now consider the Earth as being made up of a sphere, with radius equal to the polar radius of the Earth,and a ring of extra material that is most concentrated around the equator. Consider this ring as being composed of a system of satellites; the plane of the orbit of each one will try to regress, and, if it were not attached to the Earth,it would succeed.As it is,each satelite in the ring will try to communicate this regression to the plane of the Earth's equator. They are partially successful, and as a result the plane regresses, while making a constant angle with the ecliptic (barring periodic variation)； this is the phenomenon of precession.

If the satellites experienced no friction with the main body of the Earth, the precession of the bulge would be much faster than the actual precession. Also, if the Earth's crust foated on a liquid interior, the precession would still be too fast.Hence it is possible to conclude that the Earth's crust is rigidly attached to the interior.

Let us return to the consequence of the couple (13.3.8). We are to ignore fluctuations about the mean value; but these would be expected to cause periodic variations about the mean precessional motion with periods much less than

26,000 years. We shallalso ignore the phenomenon of variation of latitude, and assume that the axis of rotation of the Earth is rigidly fixed along the shortest nrincipal axis of inertia of a rigid Earth.

Let the spin of the Earth about its axis be n. Using the notation of Section 13.3,we see that the direction of the axis is ； also

$$
\hat { \mathbf { x } } = \frac { \hat { \mathbf { z } } \times \hat { \mathbf { z } } } { \sin \epsilon } .
$$

The total angular velocity of the Earth is composed of this spin and the motion of the axis itself;so it is

$$
n \hat { \mathbf { z } } \div \hat { \mathbf { z } } \times \frac { d \hat { \mathbf { z } } } { d \hat { t } } .
$$

Then the angular momentum of the Earth is

$$
C n \hat { \mathbf { z } } + A \hat { \mathbf { z } } \times \frac { d \hat { \mathbf { z } } } { d \hat { \mathbf { z } } }
$$

and its rate of change is

$$
\begin{array} { r } { C { \boldsymbol { n } } \frac { d \hat { \boldsymbol { z } } } { d t ^ { \frac { 1 } { 2 } } } + A \hat { \boldsymbol { z } } \times \frac { d ^ { 2 } \hat { \boldsymbol { z } } } { d t ^ { 2 } } , } \end{array}
$$

since $\pmb { \mathscr { n } }$ is constant. The equation for the rate of change of the angular momentum is, then,

$$
\begin{array} { r } { C n \frac { d \hat { \mathbf { z } } } { d t } \div A \hat { \mathbf { z } } \times \frac { d ^ { 2 } \hat { \mathbf { z } } } { d t ^ { 2 } } = \overline { { \Gamma } } \hat { \mathbf { x } } } \\ { = \overline { { \Gamma } } \frac { \hat { \mathbf { z } } \times \hat { \mathbf { z } } } { \sin \epsilon } . } \end{array}
$$

For the steady precession of $\hat { \mathbf { z } }$ around $\hat { \mathbb Z }$ with angular velocity $\omega \hat { \mathbb { Z } }$ we have

$$
\begin{array} { r } { \frac { \hat { d } \hat { \mathbf Z } } { \hat { d t } } = \omega \hat { \mathbf Z } \times \hat { \mathbf z } , } \end{array}
$$

and

$$
\begin{array} { r } { \frac { d ^ { 2 } \hat { \mathbf { z } } } { d t ^ { 2 } } = \omega ^ { 2 } \hat { \mathbf { Z } } \times ( \hat { \mathbf { Z } } \times \hat { \mathbf { z } } ) } \\ { = \omega ^ { 2 } ( \hat { \mathbf { Z } } \cos \varepsilon - \hat { \mathbf { z } } ) . } \end{array}
$$

Substituting these conditions into (13.4.1), we see that such motion is possible, provided $\omega$ satisfies the quadratic equation

$$
\begin{array} { r l r } {  { C n \omega - A \omega ^ { 2 } \cos \epsilon = - \frac { \overline { { \Gamma } } } { \sin \epsilon } } } \\ & { } & { = - \frac { 3 } { 2 } G ( \frac { M _ { m } } { \gamma ^ { 3 } } + \frac { M _ { s } } { R ^ { 3 } } ) ( C - A ) \cos \epsilon . } \end{array}
$$

The sum of the roots (which are real) is equal to $C _ { 2 } / ( A \cos \theta )$ If we take the sidereal day as the unit of time, this has the approximate value $2 \pi / \cos \theta .$ But the product of the roots is seen to be very small. Hence (13.4.2) has two real roots,of which one is of the order $2 \pi / \cos \theta$ and the other is very small; obviously we must look to the second of these for terms relevant to the actual precession. We can neglect the square of this small root, so that we find

$$
\omega = - \frac { 3 G } { 2 n } \frac { C - A } { C } \left( \frac { \tilde { M } _ { m } } { r ^ { 3 } } + \frac { \tilde { M } _ { s } } { R ^ { 3 } } \right) \cos \epsilon .
$$

Now let the unit of length be the astronomical unit, the unit of mass be the mass of the Sun,and the unit of time be the sidereal year. Then $G = 4 \pi ^ { 2 }$ and $\mathfrak { n } = 2 \pi \times 3 6 5 . 3$ Substituting these values and that of $\tt C O S E$ into (13.4.3) we find

$$
\omega = - 2 \pi { \frac { C - A } { C } } 1 . 1 9 \times \mathrm { i } 0 ^ { - 2 } .
$$

It is known that $\omega$ is negative ( $p _ { j }$ recedes around the ecliptic), and if we adopt the period 25,800 years for the precession,we find

$$
{ \frac { C - A } { C } } = { \frac { 1 } { 3 0 8 } } .
$$

A better value is $\ I _ { 2 } / 3 0 4$ so that agreement with even this rough theory is satisfactory. A more refined theory would enable $( C - A ) / C$ to be found from observation.

If the reader is not aware of the elementary theory of spinning tops, he should consult any elementary mechanics text. The account given here is based on the methods used in Milne's Vectorial Mechanics (Ref.8). We shall not investigate the stability of the precessional motion of the Earth's axis, but it can be shown to be stable by the use of elementary methods given in most texts.

# 13.5Nutation

Let us forget,for the moment,about the terms in the expressions for the couples exerted on the Earth by the Sun and Moon that produce the mean value , (13.3.8), used to establish the lunisolar precession; we are left with certain periodic terms.We have seen that,as far as the couple is concerned, the Moon is more potent than the Sun, so that the most important of the periodic terms will be those arising from the motion of the Moon's node, for these have the largest amplitude and the longest period. The annual fuctuations due to the Sun and the monthly fluctuations due to the Moon will be ignored. From (13.3.6) and (13.3.7) we find the following relevant terms:

$$
\Gamma _ { x } ^ { \prime } = \frac { 3 M _ { m } G } { 2 r ^ { 3 } } ( C - A ) k \cos 2 \epsilon \cos ( g t - \beta + \gamma \} ,
$$

and

$$
\tilde { \tau } _ { y } ^ { r } = - \frac { 3 M _ { m } G } { 2 \tilde { \tau } _ { x } ^ { 3 } \tilde { \tau } _ { y } ^ { 3 } } ( C - A ) k \cos \epsilon \sin ( g t - \beta + \gamma ) .
$$

Let

$$
p = { \frac { 3 M _ { m } G } { 2 r ^ { 3 } } } ( C - A ) k ;
$$

then, if the time is measured from a suitable epoch, we can put

$$
\left. \begin{array} { l } { { \Gamma _ { x } ^ { \prime } = p \cos 2 \varepsilon \cos g \dot { t } _ { \ast } } } \\ { { \Gamma _ { y } ^ { \prime } = - p \cos \epsilon \sin g \dot { t } _ { \ast } } } \end{array} \right]
$$

Consider the effects of this couple, isolated from the rest of the precessional motion； this is justified in $\mathbf { a }$ first approximation because all the effects are small. At some instant the component of the couple $\Gamma _ { x } ^ { \prime }$ will be trying to induce a precession of the Earth's axis with angular velocity $\omega _ { z } ^ { \prime }$ ,where

$$
C n \omega _ { x } ^ { \prime } = - \frac { \bar { \Gamma } _ { x } ^ { \prime } } { \sin \epsilon } .
$$

This will be true only instantaneously, but if we assume $\Sigma _ { z } ^ { \prime }$ to remain constant for a time $d t$ then the Earth's axis will precess through an angle

$$
w _ { x } ^ { \prime } d t ,
$$

and, according to the property of precession, this motion willbe at right angles to the direction of the couple that is causing it. Hence the Earth's axis will move along the $y .$ axis through an angle

$$
- \frac { \mathcal { P } } { C \mathcal { n } } \frac { \cos 2 \varepsilon } { \sin \varepsilon } \cos g \dot { \varepsilon } d \dot { \varepsilon } .
$$

So for general $\ddagger$ we see that $\Sigma _ { z } ^ { \prime }$ will result in simple harmonic motion along the $y$ -axis with period $2 \pi / g$ 0r 18.6 years. In exactly the same way, $\Sigma _ { y } ^ { f }$ causes simple harmonic motion along the $\pmb { \mathcal X } ^ { \bullet }$ axis, with the same period but different amplitude. Combining the two, we see that the Earth's axis describes an ellipse in space with period 18.6 years.

The elliptic motion is superimposed upon the steady precessional motion already found; the result is that the Earth's axis describes a wavy path through space, the extra waviness being called the nutation (for “nodding").

We must emphasize that the account given here of precession and nutation only scratches at the surface of the problem. The reader will find an adequate treatment in texts such as those of Plummer or Smart (Refs.26, 29),but that requires an analytical approach involving theory outside the scope of this text. However, we have tried to show how elementary methods can be used to account for the grosser aspects of the phenomena, and may provide a geometrical understanding that is not perhaps so easily grasped from the analytical methods.

The constants involved in the formulas for precession and nutation are found basically from observation.But observations must be referred to an inertial system of reference,and this is extremely difficult.to do. For example,positions of stars at different times might be used; but the stars have their own motions, and even if many stars were used so that their individual motions perhaps canceled out, there is still the possibility of some general drift that would not be affected. The motion of the Sun through space results in a general drift ofstars away from the direction of motion,and a determination of the solar motion based on the observed positions of stars at different times involves a redetermination of the constants of precession and nutation. One approach to the determination of an inertial reference system is to use dynamics of the asteroids. Another is to use the quasars as reference objects; these are very remote and present stellar images.

# 13.6Problems

1. Prove that the mutual potential energy of two distant bodies is approximately

$$
- \frac { G } { r } \left\{ M M ^ { \prime } + \frac { M ( A ^ { \prime } + B ^ { \prime } + C ^ { \prime } - 3 I ^ { \prime } ) } { 2 r ^ { 2 } } + \frac { M ^ { \prime } ( A + B + C - 3 I ) } { 2 r ^ { 2 } } \right\} ,
$$

where $\mathfrak { r }$ is the distance between their centers of mass, and $M$ and $\pmb { M } ^ { \prime }$ are their masses, etc.

2. The quadratic equation for the precessional motion has another solution; find it. Investigate the stability of the two solutions.

3. The boundary between the United States and Canada is, in part, defined by the 49th parallel of latitude. If this were measured with respect to the instantaneous north pole, find the extent (in meters) by which it would vary.

4. Investigate the precession of Jupiter, assuming it to be solid and homogeneous.

5. Investigate the precession of Saturn's rings.

6.An artificial satellite moves in a circular orbit,initially in the plane of the Earth's equator, just grazing the surface of the Earth. Assuming that the orbit is free from atmospheric friction, find the period and the time taken for a revolution around the ecliptic of the nodes of the orbit. (Consider the action of the Sun and Moon.)

7.Find the axes of the ellipse describing the nutation considered in Section 13.5.Sketch part of the path traced out on the celestial sphere by the Earth's axis as a result of precession and nutation； will this include loops?
