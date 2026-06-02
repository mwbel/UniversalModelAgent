# Chapter 9

# The n-Body Problem

# 9.1The Center of Mass and the Invariable Plane

In this chapter we shall examine formally the equations of the $\pmb { \mathscr { T } }$ -bodyproblem and their known solutions,and put them into a form that is readily useful inwork on perturbations.

Let a system of $\mathfrak { r }$ bodies consist of point masses $\mathbf { \nabla } ^ { \eta } \mathbf { \vec { 2 } } _ { i }$ at $\pmb { \hat { z } _ { i } }$ ，where $\begin{array} { l l } { \dot { \mathfrak { L } } } & { = } \end{array}$ ...,n,and the $\pmb { \tilde { \mathfrak { L } } } _ { \pmb { \dot { z } } }$ are expressed with respect to an inertial frame of refrence. Let

$$
r _ { i j } = | \mathfrak { r } _ { j } - \mathfrak { r } _ { i } | , \ ( \mathfrak { r } _ { i j } = \mathfrak { r } _ { j i } ) ,
$$

then the equation of motion of $\mathcal { W } _ { \widehat { \pmb { \imath } } } \big ( \widetilde { \pmb { \imath } } _ { \widehat { \pmb { \imath } } } \big )$ is

$$
\mathfrak { m } _ { i } \ddot { \mathfrak { r } } _ { i } = - \dot { \kappa } ^ { 2 } m _ { i } \sum _ { j = 1 } ^ { n } \mathfrak { m } _ { j } \frac { \mathfrak { r } _ { i } - \mathfrak { r } _ { j } } { \mathfrak { r } _ { i j } ^ { 3 } } .
$$

Here the summation excludes $\dot { \mathfrak { z } } = \dot { \mathfrak { z } }$ and this case will automatically be excluded from future summations in this chapter where it would result in the vanishing of adenominator. For a complete solution of the $\mathfrak { V }$ -bodyproblem, $6 \pi$ constants of integration are needed; actually only ten are known.

Ifall the equations of the form (9.1.1) are added,all the terms on therightand side cancel out,and we have

$$
\sum _ { i = 1 } ^ { n } \pi _ { i } { \ddot { \bar { \bf z } } } _ { i } = \bar { \bf 0 } .
$$

This can be integrated at once to give

$$
\sum _ { i = 1 } ^ { n } \pi _ { i } \mathbf { r } _ { i } = \mathbf { a } t + \mathbf { b } ,
$$

vhere a and b are constant vectors. This means that the center of mass of the ystem moves, with respect to the (inertial) system of reference, in a straight

line with constant speed. We can therefore set the origin at the center of mass, when

$$
\sum _ { i = 1 } ^ { n } m _ { i } \mathbf { r } _ { i } = \emptyset
$$

and the equations (9.1.1) remain valid.

Multiply (9.1.1） vectorially by $\pmb { \hat { z } } _ { i } \times$ ，and add the resulting $\pmb { \pi }$ equations. Again,all the terms on the right-hand side cancel out,and we have

$$
\sum _ { i = 1 } ^ { n } m _ { i } \mathbf { r } _ { i } \times \ddot { \mathbf { r } } _ { i } = 0 ,
$$

or

$$
\sum _ { i = 1 } ^ { n } m _ { i } \mathbf { r } _ { i } \times \dot { \mathbf { r } } _ { i } = \mathbf { \hat { s } } ,
$$

where h is a constant vector. This is the integral of “areas."

The plane through the center of mass,perpendicular to h, is called the invariable plane of the system.We must be careful when applying thisrigorously toa physical system. The angular momentum integral is the result of the absence of external forces acting on the system,and it expresses the fact that the total angular momentum of the system is constant; this is made up of the angular momentum arising from orbital revolutions and from axial rotations. If all the bodies are unconnected,rigid, spherical bodies,whose concentric layers are homogeneous, then the axial rotations will remain constant,and so will the orbital angular momentum; in this case the system will have an invariable plane perpendicular to the orbital angular momentum vector. But if these conditions donot hold,then precessional movements and the effects of tidal friction result inan interchange between the orbital and rotational parts of the total angular momentum,and the invariable plane as defined by h,in (9.1.3) will not be constant.But the conditions very nearly hold fora planetary system,and we are justified in practice in speaking of the invariable plane of the solar system: it has elements $\Omega = I \theta 7 ^ { \circ }$ and $i = 1 ^ { \circ } 3 5 ^ { \prime }$ ,approximately.

# 9.2The Energy Integral and the Force Function

Define $\bar { v }$ ,the force function of the system,by

$$
\bar { U } = k ^ { 2 } \sum _ { i < j } ^ { n } \sum _ { j = 1 } ^ { n } \frac { \mathscr { N } _ { i } \mathscr { R } _ { j } } { \mathscr { r } _ { i j } } .
$$

Then

$$
\begin{array} { r } { \frac { \partial { \cal U } } { \partial x _ { i } } = k ^ { 2 } m _ { i } \frac { \partial } { \partial x _ { i } } \left\{ \displaystyle \sum _ { j = 1 } ^ { n } \frac { m _ { j } } { r _ { i j } } \right\} } \\ { = - k ^ { 2 } m _ { i } \displaystyle \sum _ { j = 1 } ^ { n } m _ { j } \frac { x _ { i } - x _ { j } } { r _ { i j } ^ { 3 } } . } \end{array}
$$

herefore equation (9.1.1) can be written

$$
\begin{array} { r } { \mathfrak { m } _ { i } \tilde { \mathfrak { r } } _ { i } = \nabla _ { i } \mathcal { U } , } \end{array}
$$

$$
\nabla _ { i } \equiv \mathbf { i } \frac { \partial } { \partial x _ { i } } + \hat { \mathbf { j } } \frac { \partial } { \partial y _ { i } } + \hat { \mathbf { k } } \frac { \partial } { \partial z _ { i } } .
$$

Suppose the system to be assembled from a state of infinite diffusion. Start th ${ \mathfrak { F } } { \mathfrak { R } } 1$ at $\pmb { \mathfrak { x } } _ { 1 }$ In moving $\scriptstyle { \widetilde { \pmb { i } } \pmb { \lambda } \pmb { \lambda } }$ from infinity to $\pmb { \Sigma } _ { 2 }$ anamount of work

$$
- k ^ { 2 } { \frac { \Re \Im \Im \Re _ { \mathbf { \Im } } } { \Im \Im \Im } }
$$

is performed. If $\yen 3$ is now moved to $\mathtt { r } _ { 3 }$ ,the additional work

$$
- \hat { \kappa } ^ { 2 } \frac { \hbar \varepsilon _ { 1 } \hbar \varepsilon _ { 3 } } { \hat { \tau } _ { 1 3 } } - \hat { \kappa } ^ { 2 } \frac { m _ { 2 } \hbar \varepsilon _ { 3 } } { \hat { \tau } _ { 2 3 } }
$$

performed.As more particles are assembled, the function $- \theta$ is steadily built p,so that $- \xi$ is the total potential energy of the system.

Now multiply (9.2.2) scalarly by $\dot { \Sigma } _ { i } \cdot$ ,and add all the $\ngeq$ equations; we have

$$
\begin{array} { c } { \displaystyle \sum _ { i = 1 } ^ { n } m _ { i } \dot { \bf r } _ { i } \cdot \ddot { \bf r } _ { i } = \displaystyle \sum _ { i = 1 } ^ { n } \dot { \bf r } _ { i } \cdot \nabla _ { i } U } \\ { = \displaystyle \frac { d U } { d t } . } \end{array}
$$

Integrating this, we find

$$
{ \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { n } m _ { i } { \dot { \bar { \bf r } } } _ { i } ^ { 2 } = U + \mathrm { c o a s t a n t } ,
$$

which is the energy integral. Let $\mathfrak { T }$ be the kinetic energy of the system; then

$$
T = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { n } \ m _ { i } \dot { \bar { \Sigma } } _ { i } ^ { 2 } ,
$$

and the energy integral can be written

$$
{ \mathcal { T } } = { \mathcal { V } } \div C .
$$

This completes the known integrals of the problem, $\mathbb { C }$ being the tenth constant of integration. These integrals are merely the consequence of the absence of external forces acting on the system.

# 9.3The Virial Theorem

Consider the function

$$
\displaystyle { \boldsymbol { \mathit { I } } } = \sum _ { i = 1 } ^ { n } m _ { i } { \bar { \bar { \mathbf { x } } } } _ { i } ^ { 2 } .
$$

Differentiating it twice with respect to the time, we find

$$
\begin{array} { l } { \displaystyle \frac { 1 } { 2 } \ddot { \tilde { I } } = \sum _ { i = 1 } ^ { n } m _ { i } \dot { \bf r } _ { i } ^ { 2 } + \sum _ { i = 1 } ^ { n } m _ { i } { \bf r } _ { i } \cdot \ddot { \bf r } _ { i } } \\ { = 2 \mathcal { T } + \sum _ { i = 1 } ^ { n } { \bf r } _ { i } \cdot \nabla _ { i } \mathcal { V } . } \end{array}
$$

Now $\sigma$ is $\tt _ { a }$ homogeneous function of all the coordinates of order $^ { - 1 }$ ,so that, by Euler's theorem,

$$
\begin{array} { l } { { \displaystyle \sum _ { i = 1 } ^ { n } } \displaystyle \mathbf { r } _ { i } \cdot \nabla _ { i } U = \displaystyle \sum _ { i = 1 } ^ { n } \left\{ x _ { i } \frac { \partial U } { \partial x _ { i } } + y _ { i } \frac { \partial U } { \partial y _ { i } } + z _ { i } \frac { \partial U } { \partial z _ { i } } \right\} } \\ { = - U . } \end{array}
$$

Therefore

$$
\ddot { \bar { \xi } } = \dot { \varepsilon } \bar { \mathcal { Z } } - 2 \bar { \mathcal { U } } .
$$

Using the energy integral, (9.2.4), this can be put into the alternative forms:

$$
\ddot { I } = 2 \bar { U } \div 4 \bar { C } = 2 \mathcal { Z } \div 2 C .
$$

(9.3.1)and (9.3.2) are forms of the virial theorem.

In(9.3.2） $\pmb { \mathcal { Z } }$ and $\mathcal { T }$ are positive. If $C$ is such as to make $2 3 7 \div \mathtt { d } C$ or $2 2 ^ { \prime } + 2 C$ positive, then I is positive, and I increases without limit. A fallacy (repeated in the first edition of this book,and first pointed out to me by H. Pollard)is to conclude that at least one of the r; must increase without limit, which is equivalent to saying that at least one of the bodies escapes from'the system. As an illustration,if r1= tcost and r2 = tsint,thenr²+r²=t²,which tends to infinity as t tends to infinity. But you cannot say that “at least one of the r1 must increase without limit.” In fact, only for the case n = 3 has it been proved that when $\ddot { \bar { z } }$ is positive, at least one body escapes.

For the system to hold together,or to be stable,it is certainly necessary that C be negative, and it must be such as to make I negative or zero; this is, however,by no means a sufficient condition.

# 9.4Transfer of the Origin:the Perturbing Forces

Suppose,as is the case with the Sun in the solar system, that one mass, $\gamma _ { \widehat { \varepsilon } , \widehat { \varepsilon } }$ ， say,is dominant. Let us transfer the origin to mn,and let the position vector

of m;with respect to $\gamma _ { 2 \lambda _ { 3 \lambda } }$ be $\boldsymbol { \mathfrak { T } } _ { i } ^ { \prime }$ Then

$$
\boldsymbol { \mathfrak { r } } _ { i } = \boldsymbol { \mathfrak { r } } _ { i } ^ { \prime } + \boldsymbol { \mathfrak { r } } _ { \mathfrak { r } } .
$$

i are not affected, and we have $\partial / \partial x _ { i } ^ { \prime } = \partial / \partial x _ { i }$ ,etc.

$$
\begin{array} { l } { { \displaystyle { \bar { U } } = k ^ { 2 } m _ { n } \sum _ { j = 1 } ^ { n - \frac { 1 } { 2 } } \frac { m _ { j } } { r _ { n j } } + k ^ { 2 } \sum _ { i < j } ^ { n - \frac { 1 } { 2 } } \sum _ { j = 1 } ^ { n - 1 } \frac { m _ { i } m _ { j } } { \bar { r } _ { i j } } } } \\ { { \displaystyle ~ = k ^ { 2 } m _ { n } \sum _ { j = 1 } ^ { n - 1 } \frac { m _ { j } } { r _ { n j } } + U ^ { \prime } . } } \end{array}
$$

$$
\nabla _ { i } U = \nabla _ { i } U ^ { \prime } - k ^ { 2 } m _ { n } m _ { i } \frac { { \bf r } _ { i } ^ { \prime } } { { \bf r } _ { i n } ^ { 3 } } . \quad ( i \neq j )
$$

lso,from the equation of motion of $\mho$ ,we have

$$
\begin{array} { l } { { \displaystyle { \ddot { \mathtt { r } } } _ { n } = - \ k ^ { 2 } \sum _ { j = 1 } ^ { n - 1 } m _ { j } \frac { \mathtt { r } _ { n } - \mathtt { r } _ { j } } { \tau _ { n j } ^ { 3 } } } } \\ { { \displaystyle ~ = k ^ { 2 } \sum _ { j = 1 } ^ { n - 1 } m _ { j } \frac { \mathtt { r } _ { j } ^ { j } } { \tau _ { n j } ^ { 3 } } . } } \end{array}
$$

The equation of motion of $\mathfrak { W } _ { \mathfrak { k } } ^ { \bullet }$ is

$$
\tilde { \mathbf { r } } _ { i } ^ { \prime } \div \tilde { \mathbf { r } } _ { \mathfrak { n } } = \frac { 1 } { \mathfrak { n } \mathfrak { r } _ { i } } \nabla _ { i } \bar { \mathcal { V } }
$$

$$
\ddot { \tau } _ { i } ^ { \prime } + k ^ { 2 } \sum _ { j = 1 } ^ { n - 1 } \tau _ { j } \frac { r _ { i } ^ { \prime } } { \tau _ { n j } ^ { 3 } } = \frac { 1 } { m _ { i } } \left( \nabla _ { i } \bar { U } ^ { \prime } - k ^ { 2 } m _ { n } m _ { i } \frac { \tau _ { i } ^ { \prime } } { r _ { i n } ^ { 3 } } \right) .
$$

lake out the ith term in the summation on the left-hand side; we have

$$
\ddot { \bar { x } } _ { i } ^ { \prime } + \bar { k } ^ { 2 } m _ { i } \frac { \bar { x } _ { i } ^ { \prime } } { r _ { i n } ^ { 3 } } + \bar { k } ^ { 2 } \sum _ { \substack { j \neq i } } ^ { n - 1 } m _ { j } \frac { \bar { x } _ { i } ^ { \prime } } { r _ { n j } ^ { 3 } } = \frac { 1 } { m _ { i } } \left( \nabla _ { i } \bar { U } ^ { \prime } - \bar { k } ^ { 2 } m _ { n } m _ { i } \frac { \bar { \mathbf { r } } _ { i } ^ { \prime } } { r _ { i n } ^ { 3 } } \right)
$$

or, dropping the primes, since the transfer to the new origin is complete, and we can do so without ambiguity,

$$
\ddot { \bar { x } } _ { i } + \dot { k } ^ { 2 } \big ( m _ { n } + m _ { i } \big ) \frac { \bar { x } _ { i } } { r _ { i n } ^ { 3 } } = \frac { 1 } { m _ { i } } \nabla _ { i } \bar { U } ^ { \prime } - k ^ { 2 } \sum _ { \stackrel { j = 1 } { j \neq i } } ^ { n - 1 } m _ { j } \frac { \bar { x } _ { j } } { r _ { j n } ^ { 3 } } .
$$

Now let

$$
R _ { i j } = \operatorname { \mathbb { k } } ^ { 2 } \left( { \frac { 1 } { r _ { i j } } } - { \frac { \operatorname { \mathbb { r } } _ { i } \cdot \operatorname { \mathbb { r } } _ { j } } { r _ { j n } ^ { 3 } } } \right) .
$$

Then

$$
m _ { j } \nabla _ { i } R _ { i j } = k ^ { 2 } \nabla _ { i } \left( \frac { m _ { j } } { r _ { i j } } \right) - k ^ { 2 } m _ { j } \frac { \mathbf { r } _ { j } } { r _ { j n } ^ { 3 } } ,
$$

and

$$
\begin{array} { l } { { \displaystyle \sum _ { j = 1 } ^ { n - 1 } m _ { j } \nabla _ { i } R _ { i j } = \frac { k ^ { 2 } } { m _ { i } } \sum _ { j = 1 } ^ { n - 1 } \nabla _ { i } \left( \frac { m _ { i } m _ { j } } { r _ { i j } } \right) - k ^ { 2 } \sum _ { j = 1 } ^ { n - 1 } m _ { j } \frac { { \bf r } _ { j } } { r _ { j n } ^ { 3 } } \quad ( j \neq i ) } } \\ { { = \displaystyle \frac { 1 } { m _ { i } } \nabla _ { i } U ^ { \prime } - k ^ { 2 } \sum _ { j = 1 } ^ { n - 1 } m _ { j } \frac { { \bf r } _ { j } } { r _ { j n } ^ { 3 } } . } } \end{array}
$$

Combining this result with (9.4.1),we have

$$
\ddot { \bar { x } } _ { i } + \dot { \bar { \kappa } } ^ { 2 } \big ( m _ { n } + m _ { i } \big ) \frac { \bar { x } _ { i } } { r _ { i n } ^ { 3 } } = \sum _ { j = 1 } ^ { n - 1 } m _ { j } \nabla _ { i } R _ { i j } .
$$

The equations (9.4.3) are fundamental. If the $\Re _ { i j }$ are zero, we are left with the equations of motion of the two-body problem, so it is the ${ \mathcal R } _ { i j }$ which cause the departures,or perturbations,from Keplerian motion. They are called the perturbative functions.

(9.4.3) can be written:

$$
\vec { \tau } _ { i } + \vec { k } ^ { 2 } ( m _ { n } + m _ { i } ) \frac { \boldsymbol { \mathrm { r } } _ { i } } { r _ { i n } ^ { 3 } } = k ^ { 2 } \sum _ { j = 1 \atop j \neq i } ^ { n - 1 } m _ { j } \left( \frac { \boldsymbol { \mathrm { r } } _ { j } - \boldsymbol { \mathrm { r } } _ { i } } { r _ { i j } ^ { 3 } } - \frac { \boldsymbol { \mathrm { r } } _ { j } } { r _ { j n } ^ { 3 } } \right) .
$$

The first terms on the right-hand side are the direct attractions on $\mathfrak { T } _ { 2 } ^ { 2 } .$ due to the perturbing bodies. The second terms are indirect, and it is tempting when working with the equations of motion to forget about these; it is a temptation that should be resisted unless the terms can definitely be shown to be negligible.

# 9.5Application to the Solar System

Consider the equations of motion of a body of negligible mass,a comet, say, in the solar system. If the origin is taken at the center of the Sun and $\pmb { \Sigma }$ is the position vector of the comet,we have

$$
\ddot { \bar { \mathbf { r } } } + \hat { M } k ^ { 2 } \frac { \mathbf { r } } { r ^ { 3 } } = \sum _ { i = 1 } ^ { 9 } m _ { i } \hat { k } ^ { 2 } \left( \frac { \mathbf { r } _ { i } - \mathbf { r } } { \vert \mathbf { r } _ { i } - \mathbf { r } \vert ^ { 3 } } - \frac { \bar { \mathbf { r } } _ { i } } { r _ { i } ^ { 3 } } \right) ,
$$

where M is the mass of the Sun, and the summation is taken over the nine maior planets, in order of increasing mean distance from the Sun.

Unless the comet moves close to another planet, the most important contribution to the right-hand side of(9.5.1） will come from Jupiter, $\mathcal { Y } \mathcal { Y } _ { 5 }$ and the effects.of the other planetsmay be relatively small. It follows that in practice （9.5.1) may be simplified; but any simplification must be theoretically justified.

Unless the comet passes close to Pluto,we can omit $i = 9$ since both the direct and indirect terms are very small But this is not the case for Mercury because, although the direct terms may become negligible,the indirect terms will be much greater,and they are not diminished as $\pmb { \mathcal { T } }$ increases.

The indirect term due to Mercury is

$$
- m _ { \frac { 1 } { 2 } } \bar { \kappa } ^ { 2 } \frac { \bar { \kappa } _ { 1 } } { \bar { \kappa } _ { 1 } ^ { * 3 } } ,
$$

which is equal to

$$
{ \frac { \mathfrak { M } _ { \bar { 4 } } } { \bar { M } + m _ { 1 } } } \ddot { \bar { \mathfrak { r } } } _ { 1 } = \ddot { \bar { \mathfrak { r } } } _ { \bar { 4 } } ,
$$

where $\overline { { \mathfrak { X } } } _ { \mathfrak { F } }$ is the center of mass of the Sun and Mercury. Hence (9.5.1) can be written

$$
\frac { d ^ { 2 } } { d t ^ { 2 } } \{ \boldsymbol { \mathbf { r } } - \overline { { \boldsymbol { \mathbf { r } } } } _ { \mathrm { 1 } } \} + M \bar { \kappa } ^ { 2 } \frac { \boldsymbol { \mathbf { r } } } { r ^ { 3 } } = \sum _ { i = 1 } ^ { 8 } m _ { i } k ^ { 2 } \frac { \boldsymbol { \mathbf { r } } _ { i } - \boldsymbol { \mathbf { r } } } { | \boldsymbol { \mathbf { r } } _ { i } - \boldsymbol { \mathbf { r } } | ^ { 3 } } - \sum _ { i = 2 } ^ { 8 } m _ { i } \bar { k } ^ { 2 } \frac { \boldsymbol { \mathbf { r } } _ { i } } { r _ { i } ^ { 3 } } .
$$

Therefore the neglect of an indirect term amounts, partially, to a change in the reference system; as far as the accelerated quantities are concerned, the origin has been moved to the center of mass of the Sun and the neglected planet.

I practical work on cometary perturbations it may be convenient to neglect the four inner (terrestrial) planets, since their direct perturbations are small; their indirect perturbations are absorbed by a change of origin to the center of mass,or barycenter, of the Sun and the four inner planets. If this point is at F4，then

$$
\frac { d ^ { 2 } } { d t ^ { 2 } } ( \mathbf { r } - \tilde { \mathbf { r } } _ { 4 } ) + M k ^ { 2 } \frac { \mathbf { r } } { r ^ { 3 } } = \sum _ { i = 1 } ^ { 8 } m _ { i } k ^ { 2 } \frac { \mathbf { r } _ { i } - \mathbf { r } } { | \mathbf { r } _ { i } - \mathbf { r } | ^ { 3 } } - \sum _ { i = 5 } ^ { 8 } m _ { i } k ^ { 2 } \frac { \mathbf { r } _ { i } } { r _ { i } ^ { 3 } } .
$$

istabulated in Planetary Coordinates (Ref. 48); it is referred $\$ 0$ as $\pmb { \tau _ { b } }$ ,and the reference system thus introduced, as $S _ { 4 }$

If the comet is far enough from the four inner planets for $\gamma \gg \gamma _ { i , i } =$ 1,2,3.4, then

$$
{ \frac { \mathtt { r } _ { i } - \mathtt { r } } { \mathtt { r } _ { i } - \mathtt { r } \mathtt { j } ^ { 3 } } } \sim - { \frac { \mathtt { r } } { \mathtt { r } ^ { 3 } } } .
$$

sor4 is always small,less than $5 \times \ I \{ 0 ^ { - 6 } \ A \} \subseteq$ so that for large $\gamma$ we can take

$$
\begin{array} { r } { \mathbf { \tilde { \mathbf { \rho } } } \mathbf { \tilde { \mathbf { \rho } } } \mathbf { - } \mathbf { \tilde { \mathbf { \rho } } } \mathbf { \overline { { \tilde { \mathbf { \varepsilon } } } } } \mathbf { \frac { \partial } { \partial \mathbf { z } } } = \mathbf { \tilde { \mathbf { \varepsilon } } } ^ { \prime } . } \end{array}
$$

and

$$
\frac { \texttt { r } } { \gamma ^ { 3 } } \sim \frac { \texttt { r } ^ { \prime } } { \gamma ^ { \prime } 3 } .
$$

Let

$$
M _ { 4 } = M + \sum _ { i = 1 } ^ { 4 } m _ { i } ;
$$

then (9.5.1） can be written:

$$
\frac { d ^ { 2 } { \bf r } ^ { \prime } } { d t ^ { 2 } } + k ^ { 2 } M _ { 4 } \frac { { \bf r } ^ { \prime } } { r ^ { \prime 3 } } = \sum _ { i = 5 } ^ { 8 } m _ { i } k ^ { 2 } \left( \frac { { \bf r } _ { i } ^ { \prime } - { \bf r } ^ { \prime } } { \vert { \bf r } _ { i } ^ { \prime } - { \bf r } ^ { \prime } \vert ^ { 3 } } - \frac { { \bf r } _ { i } } { r _ { i } ^ { 3 } } \right) .
$$

The device of adding the masses of the inner planets to that of the Sun is often called “throwing the planets into the $\mathtt { S u n } ^ { \mathfrak { N } }$ . It should be accompanied by a suitable change of origin.

# 9.6Problems

1.Show that the angular momentum of the $\pmb { \mathscr { T } } _ { \pmb { \mathscr { L } } } ^ { * }$ -body system about a line through any origin (of an inertial system）which makes an angle $\boldsymbol { \vartheta }$ with the normal to the invariable plane is $\hbar ^ { 2 } \cos \theta$ ,where $\mathbf { \lambda } _ { \mathbf { k } } ^ { 2 } ( \mathbf { \lambda } _ { \mathbf { k } } ^ { \prime }$ is the constant in the integral of areas with respect to that origin.

2.Find the relation between $\Bbbk$ and $h ^ { \prime }$ where they are the constants of areas with respect to the center of mass of the system,and any other origin of an inertial system.

3.Show that the planes through a fixed point $o$ which contain the tangents to the paths of two of the $\pmb { \mathcal { T } } _ { 2 }$ -bodies intersect the invariable plane in one line.

4.Find the invariable plane of the Earth,Moon,and Sun.Discuss the effects of precession and tidal friction on this plane.

5.Find the invariable plane of the system consisting of the Sun,Jupiter, and Saturn.To what extent does this account for the elements quoted in Section 9.1?

6.Show that

$$
\underbrace { \frac { 1 } { n } } _ { i = 1 } \frac { \dot { d } ^ { 2 } } { d t ^ { 2 } } \left( \sum _ { i \le j } ^ { n } \sum _ { j = 1 } ^ { n } m _ { i } m _ { j } r _ { i j } ^ { 2 } \right) = 4 C + 2  { U } .
$$

7. In a system of $\mathfrak { X }$ bodies, the force acting on $\mathcal { W } _ { \ell } \dot { \mathbf { \xi } } _ { 3 }$ is $\mathbf { \overline { { \underline { { F } } } } _ { \lambda } } _ { i }$ Show that

$$
{ \scriptstyle { \frac { 1 } { 2 } } } { \ddot { \vec { \mathcal { Z } } } } = 2 { \mathcal { T } } + \sum _ { i = 1 } ^ { n } { \mathop { \pi } } _ { i } \equiv { \vec { \mathcal { Z } } } _ { i } \equiv { \vec { \mathcal { Z } } } _ { i } \ { \mathrm { ~ - ~ } } { \vec { \mathcal { Z } } } _ { i } .
$$

8.Write down the equations of motion for the $\mathfrak { z }$ -bodyproblem when the law offorce varies inversely with the kth power of the distance. Find the force   
function and the integrals corresponding to those found in this chapter.

9.From the results of problem 8,find the value of k for which the equations ofmotion are independent.Solve the problem for this case,showing that the orbits with respect to the center of mass are ellipses,with this point as center. Show that the orbit of any body with respect to any other body is also a central ellipse,and that the same is true for the motion of any body with respect to the center of mass of any subgroup of the system. Show that all the periods are equal.

0.A comet is 15 AU from the Sun.Find numerically the possible magnitudes of the approximations introduced by $\{ \mathsf { a } \}$ neglecting Pluto; $( 3 )$ entirely neglecting the four inner planets; $\{ \mathfrak { c } \}$ adding the masses of the four inner planets to that of the Sun,without compensating for the indirect terms; (d) using the formula (9.5.4).

11.Starting with $\pmb { \mathcal { X } }$ bodies $\boldsymbol { \mathcal { W } } _ { \dot { \boldsymbol { z } } }$ at ${ \mathfrak { r } } _ { i } \{ { \mathfrak { x } } _ { i } , { \mathfrak { y } } _ { i } , z _ { i } \}$ ,where the origin is at the center of mass, construct the fictitious system of masses $\mu _ { i }$ at $\rho _ { i } \{ \xi _ { i } , \eta _ { i } , \zeta _ { i } \}$ ,where

$$
\mu _ { i } = m _ { 1 } \div m _ { 2 } + \cdots + m _ { i } ,
$$

and $\pmb { \mathscr { p } } _ { i }$ is the position vector of $\eta _ { i } ,$ with respect to the center of mass of the masses ${ \mathfrak { R } } _ { 1 } , { \mathfrak { R } } _ { 2 } , \dotsc , { \mathfrak { R } } _ { i - 1 }$ . There is no ${ \pmb \beta } _ { 1 }$ Show that if $T$ is the kinetic energy of the system,

$$
2 \mathcal { T } = \sum _ { i = 2 } ^ { n } m _ { i } \frac { \mu _ { i } - 1 } { \mu _ { i } } \big ( \dot { \xi } _ { i } ^ { 2 } + \dot { \eta } _ { i } ^ { 2 } + \dot { \zeta } _ { i } ^ { 2 } \big ) .
$$

Show that the integral of areas becomes

$$
\sum _ { i = 2 } ^ { n } { \boldsymbol { \pi } } _ { i } { \frac { \mu _ { i - 1 } } { \mu _ { i } } } { \boldsymbol { \rho } } _ { i } \times { \dot { \boldsymbol { \rho } } } _ { i } = { \hat { \mathbf { n } } } ,
$$

where h is the angular momentum of the actual system about the center of mass.

Show that the $\mathfrak { N }$ -body problem is thus reduced to a problem of $\{ \mathfrak { z } - \mathtt { i } \}$ fictitious bodies,and that the total order of the differential equations of motion is reduced by six.

2.Consider the three-body problem in terms of the fictitious bodies of problem 11. Write down the angular momentum integral, and hence prove a theorem due to Jacobi that the lines of nodes, with respect to the invariable plane, of the instantaneous orbits of two fictitious planets coincide.

l3. Prove that Jacobi's theorem of the nodes applies roughly to any two real planets and the Sun,where the invariable plane is that of these three bodies only.
