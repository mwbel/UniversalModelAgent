# Chapter 4

# Central Orbits

# 4.1 General Properties

A central orbit is an orbit described by a particle acted on by forces, the resultant of which always passes through a fixed point. In practice only a single force,the resultant, is considered. With this statement, we have a violation of Newton's third law.Still, the theory of central orbits isuseful and, as we shall see, can be applied to rigorous Newtonian mechanics.

Take the fixed point as the origin and let the force, per unit mass, be where $\pmb { f }$ is a scalar function that could depend not only on position but also on time, velocity, etc. $f$ is the law of attraction toward the origin.

The equation of motion is

$$
\ddot { \mathfrak { z } } = - \hat { \mathfrak { z } } \hat { \mathfrak { x } } .
$$

Multiplying by $\pmb { \Sigma } \times$ we get

$$
\qquad \ I ^ { \mathbf { s } } \times { \tilde { \bar { \mathbf { z } } } } = { \boldsymbol { \mathbb { 3 } } } ,
$$

which can be integrated at once to give

$$
\tt { r } \times \tt { \dot { \tt { F } } } = \tt { b }
$$

where h, the angular momentum per unit mass, is a constant vector. Hence Kepler's second law holds for all central orbits. (We have also seen that, should Kepler's second law be obeyed, the orbit is a central orbit.) Multiplying (4.1.2) by r., we get

$$
\begin{array} { r } { \underline { { \vec { \mathfrak { x } } } } \cdot \vec { \mathfrak { z } } = 0 , } \end{array}
$$

the equation of a plane through the origin. So, the motion takes place in this plane. Since central orbits are two-dimensional, the vector notation has no advantage and therefore will not be used.

Note that if ${ \bf \ S } \equiv \mathbb { 0 }$ , then the motion takes place in a line containing the origin. A linear orbit is possible only if it passes through the origin. Often $j$ has a singularity at the origin,so there is legitimate worry about the meaning of such an orbit. In practical cases the center of force is occupied by matter that prevents too close an approach; should the moving particle penetrate this matter, then the physical circumstances become obscure,but we should expect the law of force to change. A few orbits passing through the origin will be considered here from a mathematical angle;but such orbits are not realistic.

We shall assume that $f$ varies with position only, and we shall consider only conservative felds. This means that there must be a scalar function $\mathbb { V } ( \pmb { \tau } )$ such that the radial component of $\sqrt { y }$ is equal to $f ( T )$ ,and the transverse component is zero; i.e.,

$$
{ \frac { \partial V } { \partial r } } = f ( r ) \quad { \mathrm { a a d } } \quad { \frac { 1 } { r } } { \frac { \partial V } { \partial \theta } } = 0 .
$$

The latter condition means that $f$ is $^ \mathrm { a }$ function of $\tilde { \textbf { \textit { z } } }$ only and so can be written $f ( T )$ . In this case we find a $\pmb { \gamma }$ for any $f$ from

$$
V = \int \limits _ { 0 } ^ { \pi } f ( x ) d x .
$$

Hence the necessary and sufficient condition for the feld to be conservative is that $f$ should not vary with $\boldsymbol { \vartheta }$

The equation of motion is now

$$
\ddot { \bar { \mathbf { r } } } = - \hat { f } ( \gamma ) \hat { \bar { \mathbf { x } } } .
$$

The energy integral is

$$
\begin{array} { r } { { \frac { 1 } { 2 } } \dot { \bar { \Sigma } } ^ { 2 } + V ( \bar { r } ) = C . } \end{array}
$$

This and (4.1.2) are the fundamental equations for central orbits. If $\pmb { \ V }$ is chosen such that it tends to zero when r tends to infinity， C is definedas the energy of the orbit. From(4.1.6) C-V(r) must be nonnegative, so that the circles given by the solutions,if any，of

$$
C - V \{ \gamma \} = \emptyset
$$

represent in general important boundaries that cannot be crossed during the motion. In particular, if $C$ is negative, there must be an upper limit to the possible values of $\gamma$ ,so that the motion is bounded. If $C$ is positive and $\bar { a } \bar { \gamma } / \bar { a } \bar { \tau }$ (orf)always has the same sign, the velocity will tend to a finite limit when r tends to infinity; the particle will never return,and the motion is infinite.

Resolving (4.1.5) along the radial and transverse directions, we have

$$
j ^ { 2 } - r \dot { \theta } ^ { 2 } = - f ( r )
$$

and

$$
3 9 \div 2 \dot { 7 } \dot { 9 } = 0 .
$$

(4.1.8) can be integrated at once to give

$$
\gamma ^ { 2 } \dot { \theta } = \Bbbk , \qquad .
$$

which is equivalent to (4.1.2). The energy equation in polar coordinates is

$$
\frac { 1 } { 2 } ( \dot { r } ^ { 2 } + r ^ { 2 } \dot { \theta } ^ { 2 } ) + V ( r ) = C .
$$

The equations are not altered if $- \hat { \pmb { \tau } }$ replaces $\ddagger$ and $\hslash$ has its sign reversed; so the motion is reversible. This means that if $\blacktriangledown$ were to change its sign at some point,the path would be retraced.From (4.1.9) it is clear that $\dot { \theta }$ must have the same sign throughout the motion; it will usually be taken as positive. Also from (4.1.9) we see that if $C$ is positive, $\dot { \theta }$ tends to zero as $\Im ^ { \star }$ tends to infinity;then, since $\dot { \mathfrak { r } }$ tends to $\clubsuit$ finite limit, the motion must be asymptotic, such as hyperbolic motion. This willnot be the case if $C = 0$ (corresponding toa parabolic orbit for Newtonian motion), since $\dot { \gamma }$ tends to zero.

Eliminating $\dot { \theta }$ from (4.1.9) and (4.1.10), we get

$$
{ \frac { 1 } { 2 } } { \dot { \mathfrak { x } } } ^ { 2 } = C - V ( { \mathfrak { x } } ) - { \frac { { \mathfrak { h } } ^ { 2 } } { 2 { \mathfrak { x } } ^ { 2 } } } ,
$$

which relates $\pmb { \mathscr { T } }$ and $^ { \ddagger }$ .The condition that the right-hand side must be nonnegative provides more stringent limits for the motion than $C - \sqrt [ \gamma ] { r } ) = 0$ A point where $\dot { \mathfrak { r } } = \mathfrak { V }$ is called an apsis (plural apsides). Not allorbits have apsides; a spiral orbit may have none;a branch of $\hat { \pmb { \alpha } }$ hyperbola has one and an elliptic orbit has two. The existence of apsides depends on the equation

$$
0 = C - V ( r ) - \frac { h ^ { 2 } } { 2 r ^ { 2 } } .
$$

In particular, if $\mathfrak { T } ^ { \circ }$ lies between two single roots, $\mathfrak { T } _ { 1 }$ and $r _ { 2 }$ ,of this equation, then the motion must always take place within the ring bounded by the circles with radii $\pmb { \gamma _ { \updownarrow } }$ and ${ \mathfrak { T } } _ { 2 }$ An apsis at the shorter distance is called pericenter,and at the longer one, apocenter (with variations according to context, as explained in Section 1.3). The angle between two successive apsidal lines (which must be pericenter and apocenter) is called the apsidal angle. Since the orbits are reversible, they must be symmetrical about any apsis.

# 4.2 The Stability of Circular Orbits

The simplest central orbit is a circle with center at the origin; it can be described under any force of attraction $f ( q )$ . If the radius of the circle is $\pmb { a }$ we have $z = a$ and $\dot { r } = \ddot { r } = \beta$ so that

$$
a \dot { \theta } ^ { 2 } = \acute { f } \{ a \} ,
$$

$$
\bar { \iota } = [ \alpha ^ { 3 } f ( \alpha ) ] ^ { 1 / 2 } ,
$$

and

$$
{ \frac { 1 } { 2 } } a ^ { 2 } { \dot { \theta } } ^ { 2 } + V ( a ) = C .
$$

Now suppose that the particle receives a small impulse. The impulse can be resolved along and perpendicular to h. The impulse along h will slightly alter the value of h and the plane of the orbit $( \cos \hat { \mathbf { a } } )$ .The impulse along fwill leave h unchanged, while the transverse impulse will change $\Bbbk$ but not $\hat { \tilde { \mathbf { a } } }$ The resulting orbit will remain in one plane,which cannot be very different from the original plane; then, since the change in $\hat { \bf \textmu }$ is always small, there is no loss of generality, in considering the stability of the orbit,if we neglect it.Therefore we shall consider only the effects of the component of the impulse that is perpendicular to h.For the new orbit we can write

$$
r ^ { 2 } { \dot { \theta } } = \lbrace a ^ { 3 } f \lbrace a \rbrace + \delta \rbrace ^ { 1 / 2 } ,
$$

where $\delta$ giving the change in $\nmid$ , is small. Eliminating $j$ from (4.2.4) and (4.1.7), we get

$$
\ddot { \tau } - \frac { \frac { 1 } { 4 } } { \bar { \tau } ^ { 3 } } [ a ^ { 3 } f ( a ) + \delta ] = - f ( \bar { \tau } ) .
$$

Let us assume that the subsequent motion is very nearly circular,so that we can put

$$
\boldsymbol r = \boldsymbol a + \boldsymbol x ,
$$

where $\pmb { \mathscr { x } }$ remains small; then $f ( a + x )$ can be expanded in a Taylor series in. powers of $\pmb { \mathcal { X } }$ (4.2.5)becomes

$$
\ddot { x } - \frac { 1 } { a ^ { 3 } } \left( \mathbb { 1 } - 3 \frac { x } { a } \right) \mathbb { i } a ^ { 3 } f ( a ) + \delta \mathbb { i } = - f ( a ) - x f ^ { \prime } ( a ) + O ( x ^ { 2 } ) .
$$

Simplifying, and ignoring terms of order ${ \mathfrak { X } } ^ { 2 }$ ,we get

$$
\ddot { x } + x \left[ 3 \frac { f ( a ) } { a } + f ^ { \prime } ( a ) \right] - \frac { \delta } { a ^ { 3 } } = 0 .
$$

The constant term on the left-hand side can be absorbed by changing the dependent variable； this will leave an equation of the form

$$
\ddot { x } + \vec { k } x = 0 .
$$

If $k _ { z }$ is positive, the solution is the well-known one for simple harmonic motion. If $k$ is negative, the solution involves hyperbolic functions and $\mathscr { D }$ no longer remains small;in this case the orbit deviates entirely from $\textbf { z }$ circle and is said to be unstable.The condition for stability is, then,

$$
3 \frac { f ( a ) } { a } + f ^ { \prime } ( a ) > 0 .
$$

We notice that if equality occurs, the $\delta$ termin （4.2.6） is enough to tip the balance and insure instability. When the inequality is reversed, the orbit is unstable.

Let us consider orbits with constant energy C, but variable angular momentum $\pmb { \hat { n } }$ ,and assume that one such circular orbit is possible. From (4.1.11） we find

$$
\acute { \iota } _ { \acute { \iota } } { } ^ { 2 } = 2 \acute { \iota } ^ { 2 } C - 2 \acute { r } ^ { 2 } { \bar { \mathcal { V } } } \left( r \right) - r ^ { 2 } \dot { r } ^ { 2 } .
$$

So, for some C,if r and r are known,h can be found. As r and r vary,h wil vary.We shall now investigate when $\Bbbk$ hasamaximum.

Writing

$$
\hbar ^ { 2 } = g _ { \downarrow } ^ { f } \uparrow ^ { * } , \dot { \uparrow } )
$$

and using the notation

$$
g _ { r } = { \frac { \partial g } { \partial r } } , \quad g _ { r r } = { \frac { \partial ^ { 2 } g } { \partial r ^ { 2 } } } , \quad g _ { r { \dot { r } } } = { \frac { { \hat { \partial } } ^ { 2 } g } { \partial r { \hat { \partial } } { \dot { r } } } } , \quad { \mathrm { e t c . } }
$$

we have

$$
d ( h ^ { 2 } ) = g _ { \tau } d \vec { \tau } + g _ { \dot { \tau } } d \dot { \vec { \tau } }
$$

and

$$
d ^ { 2 } ( h ^ { 2 } ) = g _ { r r } ( d r ) ^ { 2 } + 2 g _ { r \dot { r } } d r d \dot { r } + g _ { \dot { r } \dot { r } } ( d \dot { r } ) ^ { 2 } .
$$

For $\hbar ^ { 2 }$ to have $\mathrm { ^ a }$ stationary value, $\mathcal { Q } _ { \downarrow } ^ { j } \langle \hat { \hbar } ^ { 2 } \rangle = 0$ s0,

$$
g _ { \mathrm { i r } } = \Updownarrow = g _ { \dot { r } } .
$$

For that value to be a maximum, $\vec { a } ^ { 2 } \{ \hbar ^ { 2 } \}$ must be negative for all dr and $d ^ { 2 }$ ,s0 that

$$
g _ { \tau r } g _ { \bar { r } \dot { \bar { r } } } - g _ { r \dot { \bar { r } } } ^ { 2 } > \ell .
$$

(We already know from (4.2.8) that $g _ { \dot { \tau } \dot { \bar { r } } } < 0 .$ )(4.2.9) gives

$$
r \left( 4 C - 4 V ( r ) - 2 r { \frac { d V ( r ) } { d r } } - 2 \dot { r } ^ { 2 } \right) = 0 = - 2 r ^ { 2 } \dot { r } .
$$

So. ${ \dot { \mathfrak { r } } } = 0$ and therefore the orbit must be a circle; the energy is $C$ and the circular velocity is given by the square root of $r ^ { 2 } \{ \vec { d } \} / \vec { d } \tau \}$ (4.2.10) gives

$$
- 2 r ^ { 2 } \left[ 4 C - 4 V - 8 r \frac { d V } { d r } - 2 r ^ { 2 } \frac { d ^ { 2 } V } { d r ^ { 2 } } \right] > 0
$$

or, simplifying by means of (4.2.11),

$$
- 2 { \pi } ^ { 2 } \left[ - 6 { \mathcal { F } } \frac { { \bar { d } } V } { d r } - 2 { r } ^ { 2 } \frac { { \bar { d } } ^ { 2 } V } { { \bar { d r } } ^ { 2 } } \right] > 0 .
$$

$\mathtt { B u t \ } d Y / d y = f ( r ) .$ and $\mathfrak { r } ^ { 2 }$ must be positive; so, we have

$$
3 f ( x ) + r f ^ { \prime } ( x ) > 0
$$

as the condition for $\Bbbk$ to havea maximum.Hence,if the circular orbit is stable, $\gtrapprox$ hasa maximum.Similarly,if the circular orbit isunstable, $\hslash$ hasa minimum value.

# 4.3Further Basic Formulas

Two other formulas are often used where only the form of the orbit (as opposed to its description in time) is important. We have

$$
\frac { d \bar { \varepsilon } } { d \vartheta } = \frac { \dot { \bar { \varepsilon } } } { \dot { \theta } } ,
$$

$\Im \emptyset ,$ using this to eliminate $\dot { \mathfrak { F } }$ and $\dot { \theta }$ from the equations of energy and angular momentum (4.1.10) and (4.1.9), we get

$$
\left( { \frac { d r } { d \theta } } \right) ^ { 2 } = { \frac { 2 r ^ { 4 } } { \hbar ^ { 2 } } } \left[ C - V ( r ) - { \frac { \hbar ^ { 2 } } { 2 r ^ { 2 } } } \right] .
$$

Another equation that does not involve the time can be found as follows: let $I f = u$ Then

$$
\begin{array} { l } { { \displaystyle { \frac { \dot { d } u } { d \theta } = - \frac { \frac { \dddot { \tau } } { r ^ { 2 } } } { { \dot { \tau } } ^ { 2 } } \cdot \frac { \dot { d } { r } } { \dot { d } \theta } } } } \\ { { \displaystyle ~ = - \frac { 1 } { r ^ { 2 } } \cdot \frac { d r } { d t } \cdot \frac { \dot { d } t } { d \theta } } } \\ { { \displaystyle ~ = - \frac { \dot { r } } { \dot { R } } . } } \end{array}
$$

Also

$$
\begin{array} { l } { { \displaystyle { \frac { d ^ { 2 } u } { d \theta ^ { 2 } } = - \frac { \dot { d } } { d \theta } \left( \frac { \dot { r } } { h } \right) } } } \\ { { \displaystyle ~ = - \frac { \dot { d } t } { d \theta } \cdot \frac { \dot { d } } { d t } \left( \frac { \dot { r } } { h } \right) } } \\ { { \displaystyle ~ = - \frac { \dot { 1 } } { \dot { h } ^ { 2 } u ^ { 2 } } \cdot \frac { \dot { d } ^ { 2 } \dot { r } } { d t ^ { 2 } } } . }  \end{array}
$$

Substituting into (4.1.7) and putting $\gamma \dot { \theta } ^ { 2 } = \lambda ^ { 2 } u ^ { 3 }$ ,we get

$$
{ \frac { \dot { d } ^ { 2 } u } { \dot { d } \theta ^ { 2 } } } + v = { \frac { 1 } { \hbar ^ { 2 } u ^ { 2 } } } \hat { f } \left( { \frac { 1 } { u } } \right) .
$$

In general (and as long as we have a conservative field), (4.3.2) is not so useful as (4.3.1), since the latter.is only a first-order differential equation. In fact (4.3.2) can be recovered (rather laboriously) by differentiating (4.3.1),and its only advantage occurs when $\int \limits _ { 0 } ^ { \infty } f ( \ 1 / z ) d z \rangle$ has such a form that the solution can be written down directly; this is the case when

$$
f \left( \frac { 1 } { u } \right) = a u ^ { 2 } + b u ^ { 3 } .
$$

Equations (4.1.7) and (4.1.8) require four arbitrary constants for their com-plete solution; so far we have discussed two, $h$ and $\pmb { C }$ Since $\pmb \theta$ does not occur explicitly in the equations of motion, but only $\dot { \theta }$ and ${ \ddot { \theta } } ,$ an arbitrary constant can be added to $\varnothing$ in the final answer. Once the equation of the orbit is known, as a function g(r,θ)= O,say, (4.1.9) can be used to find a first-order differential equation for r or θ in terms of t; the solution to this supplies the fourth arbitrary constant in the form ${ \boldsymbol { \mathfrak { r } } } = { \boldsymbol { \mathfrak { r } } } \{ { \boldsymbol { \sharp } } - { \boldsymbol { \mathfrak { t } } } _ { \mathfrak { Q } } \}$ ： $\boldsymbol { \vartheta } = \boldsymbol { \vartheta } \{ \boldsymbol { \mathfrak { t } } - \boldsymbol { \mathfrak { t } } _ { 0 } \}$ . Alternatively we can use the expression for the areal velocity,

$$
{ \frac { { \vec { a } } { \hat { A } } } { { \vec { d } } { \hat { t } } } } = { \frac { \vec { 1 } } { 2 } } \gamma ^ { 2 } { \dot { \vec { \theta } } } = { \frac { \vec { 1 } } { 2 } } { \dot { \hbar } } .
$$

Then

$$
A = { \frac { 1 } { 2 } } \hbar \dot { \tau } + \cos \Omega \dot { \mathrm { s } } \mathrm { a } \ m \dot { \bar { \mathrm { t } } } .
$$

This is useful when the area $\pmb { A }$ can be conveniently calculated asa function $o f$ ror $\mathfrak { g }$ In particular, if the area swept out between two points $\gamma _ { \tt 7 }$ and $\gamma _ { 2 }$ is known,then the time in the orbit between these points is

$$
\displaystyle \ddagger _ { 2 1 } = \frac { 2 } { h } A _ { 2 1 } .
$$

The uses of these equations will be illustrated by some examples in the following four sections.

# 4.4Newtonian Attraction

(It might be helpful,at this stage,to refer to Appendix A for a review of the basic properties of conics.)

If a massive body is at the origin,it will give rise toa field of force

$$
- \frac { \sharp } { \mathfrak { x } ^ { 2 } } \hat { \mathfrak { x } }
$$

according to Newton's law of gravitation. So

$$
\hat { f } = \frac { \mu } { \gamma ^ { 2 } } \quad \mathrm { a n d } \quad \mathrm { \nabla } V = - \frac { \mu } { \gamma } .
$$

Here we assume that the attracting body is at rest; a proper treatment, giving rise to the same equations, will be given in Chapter 6. (4.3.2) gives

$$
{ \frac { d ^ { 2 } u } { d \beta ^ { 2 } } } \div u = { \frac { \mu } { \hbar ^ { 2 } } }
$$

and the solution to this may be written down at once as

$$
\begin{array} { r } { u - \frac { \mu } { \hbar ^ { 2 } } = A \cos ( \theta - \theta _ { 0 } ) . } \end{array}
$$

This can be put into the form

$$
\begin{array} { r } { \frac { \mathcal { P } } { \gamma } = \mathbb { i } \div e \cos ( \theta - \theta _ { 0 } ) , } \end{array}
$$

where

$$
\displaystyle { { \mathfrak { p } } = { \frac { \hbar ^ { 2 } } { \mu } } }
$$

and $e$ and $\theta _ { 0 }$ are arbitrary constants. But (4.4.1) is the polar equation of a conic with $\hat { \mathbf { z } }$ focus at the origin, eccentricity $\mathcal { e }$ and semilatus rectum (or parameter) $p .$

We could now use (4.4.1) and (4.1.9) to find an equation for $\mathcal { T }$ 0i $\pmb \theta$ in terms of $\pmb { \xi }$ and the solution of this would provide another arbitrary constant which, together with $\hbar , e .$ and $\beta _ { 0 }$ ，completes the solution. This solution does not include $C$ ，and since the energy integral is often very convenient to work with, $C$ will now be found in terms of the other constants of integration.

The energy integral is

$$
{ \frac { v ^ { 2 } } { 2 } } - { \frac { \ddot { \mu } } { r } } = C .
$$

Now

$$
v ^ { 2 } = j ^ { 2 } + \ r ^ { 2 } \dot { \theta } ^ { 2 } .
$$

Differentiating（4.4.1） with respect to $\pmb { \dot { \tau } }$ ,we have

$$
- \frac { \mathcal { P } } { { \gamma ^ { 2 } } } \dot { \tau } = - e \sin ( \theta - \theta _ { 0 } ) \dot { \theta } ,
$$

s0

$$
{ \begin{array} { r l } & { { \dot { r } } = { \frac { e \hbar } { p } } \sin ( \theta - \theta _ { 0 } ) \quad ( { \mathrm { s i n c e ~ } } r ^ { 2 } { \dot { \theta } } = \hbar ) } \\ & { \quad = { \frac { e \hbar } { \hbar } } \sin ( \theta - \theta _ { 0 } ) . } \end{array} }
$$

Also

$$
\begin{array} { l } { { \displaystyle r \dot { \theta } = \frac { h } { r } } } \\ { { \displaystyle ~ = \frac { \mu } { h } [ 1 + e \cos ( \theta - \theta _ { 0 } ) ] } . } \end{array}
$$

So

$$
{ \begin{array} { r l } & { v ^ { 2 } = \left( { \frac { \mu } { h } } \right) ^ { 2 } [ ! \div 2 e \cos ( \theta - \theta _ { 0 } ) + e ^ { 2 } ] } \\ & { ~ = \mu \left[ { \frac { 2 } { r } } - { \frac { 1 - e ^ { 2 } } { \mathcal { P } } } \right] . } \end{array} }
$$

Hence

$$
C = - \mu { \frac { \mathbb { i } - e ^ { 2 } } { 2 g } } = - { \frac { \mu } { 2 a } } ,
$$

where $\mathfrak { Q }$ is negative for the hyperbola. For the parabola, $1 / a = \emptyset$ Hence the energy of the orbit depends only on the major axis. Now consider equation (4.3.3) and apply it to an elliptic orbit. Let us start to measure $A _ { 3 }$ the area swept out by the radius vector, when t= O,and continue until the particle has returned to its starting point in the ellipse; then $\hat { A }$ will be equal to the area of the ellipse, πab,and we find that the time taken over one complete revolution is

$$
\bar { P } = \frac { 2 } { \bar { h } } \pi \alpha \bar { \ b } .
$$

Since $\mathfrak { z } = \mathfrak { a } \sqrt { \mathbb { 1 } - \mathfrak { e } ^ { 2 } }$ ,and $\hbar ^ { 2 } / \mu = p = a ( \mathbb { i } - e ^ { 2 } )$ we have

$$
P = 2 \pi { \frac { \alpha ^ { 3 / 2 } } { \mu ^ { 1 / 2 } } } .
$$

$\mathcal { P }$ is the period of the eliptic orbit; this also depends only on the major axis of the ellipse.

The energy equation for an elliptic orbit is

$$
v ^ { 2 } = \mu \left\{ \frac { 2 } { \tau } - \frac { 1 } { \alpha } \right\}
$$

so that the energy of the orbit is equal to the energy of $\hat { \mathbf { \Omega } }$ particle at rest on the circumference of $\hat { \bf { \varepsilon } }$ circle with center the origin and radius $2 a$ Hence the speed at any point in the orbit is equal to the speed that would be acquired in falling fromrest on the circumference of the circle to that point.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0040/ocr/images/78d2228a0c4d84518702137fe560c8c975965dfaa36ba0b3725ec7134ea0c12c.jpg)  
Figure 4.1

If $^ \mathrm { a }$ particle is projected from $\hat { \pmb { \alpha } }$ point $R _ { i }$ distant $c$ from the center of force $o$ ， with speed ${ \mathfrak { V } } _ { 0 }$ ,then it will move in an ellipse, parabola, or hypcrbola according


<!-- chunk 0002: pages 41-80 -->
as $v _ { 0 } ^ { 2 }$ is less than, equal to, or greater than $2 \mu / c$ Let the first condition hold; then the major axis of the ellipse is given by

$$
v _ { 0 } ^ { 2 } = \mu \left( { \frac { 2 } { c } } - { \frac { 1 } { a } } \right) .
$$

Let $P$ be the other focus of the ellipse; this will vary, depending on the direction of projection. But since OR+RP= 2a,then RP= 2a-c, so that P must be on the circumference of a circle with center Rand radius (2a-c). If the orbit passes through a point S, then similar reasoning shows that P must lie on the circumference of a circle with center $S$ and radius $( 2 a - 0 S )$

Consider the problem of projecting the particle from $\mathcal { R }$ with initial speed ${ \mathfrak { V } } { \mathfrak { Q } }$ so that it later passes through $\boldsymbol { S }$ If the two circles intersect each other in two real points,there are two possible foci $P$ and two possible routes from $\scriptstyle { \frac { \overrightarrow { x } } { \overrightarrow { x } } }$ t0 $\mathcal { S }$ with initial speed $z _ { 0 }$ .If the circles do not intersect,then $s$ cannot be reached from $\mathcal { R }$ with this speed.The limit of accessibility occurs when the two circles touch,as shown in Figure 4.2;in this case there isa unique orbit from $\scriptstyle { \mathcal { R } }$ to $\boldsymbol { S }$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/ed81e9aa3f047fb0a559058d9760cc400dade33555ceaaedb600c486e836e0ac.jpg)  
Figure 4.2

Consider the locus of points $s$ which are just accessible from $\mathcal { R }$ In the notation of Figure 4.2 we have

$$
O S + S R = O S + S P + P R
$$

$$
{ \begin{array} { r l } & { = O S + S B + R A } \\ & { = O B + R A } \\ & { = O A + R A , } \end{array} }
$$

which is constant.So the locus of S is an ellipse,with foci O and R and major axis OA+RA, touching at A the circle with center O and radius OA. The tangent to this ellipse at S is the bisector of the angle BSR; since this must also be the tangent to the orbit from $\pmb { R }$ to $s$ (the bisector of the angle $B S P )$ ,the ellipses touch at $\boldsymbol { S }$ Therefore the locus of $s$ is the envelope of all the possible orbits from $\mathcal { R }$ This ellipse defines the region of accessibility from $\mathcal { R }$ corresponding to the initial speed of projection ${ \mathfrak { V } } _ { \mathfrak { V } }$ ·

# 4.5Einstein's Modification of the Equation of the Orbit

Asa consequence of the theory of relativity，Newton's law is modified so that the equation of the orbit becomes

$$
{ \frac { d ^ { 2 } u } { d \theta ^ { 2 } } } + u = { \frac { \mu } { \tilde { h } ^ { 2 } } } \div { \alpha 3 \epsilon } ^ { 2 }
$$

where

$$
\alpha = 3 \frac { \mu } { c ^ { 2 } } .
$$

c is the speed of light, so α is a small quantity,the square of which will be neglected. The ratio of ou² to μ/h² is equal to three times the square of the transverse velocity in units of $c$

Equation (4.5.1) is to be solved by approximations.A first approximation, found by neglecting $\pmb { \alpha }$ altogether,is

$$
\begin{array} { r } { u = \frac { \mu } { \hbar ^ { 2 } } [ 1 \div e \cos ( \theta - \theta _ { 0 } ) ] . } \end{array}
$$

To find a better approximation,we substitute this value of $\mathcal { U }$ into the right-hand side of (4.5.1); this gives

$$
\frac { d ^ { 2 } u } { d \theta ^ { 2 } } + u = \frac { \mu } { \hbar ^ { 2 } } + \alpha \frac { \mu ^ { 2 } } { \hbar ^ { 4 } } + 2 \alpha \frac { \mu ^ { 2 } } { \hbar ^ { 4 } } e \cos ( \theta - \theta _ { 0 } ) + \frac { 1 } { 2 } \alpha \frac { \mu ^ { 2 } } { \hbar ^ { 4 } } e ^ { 2 } [ 1 + \cos 2 ( \theta - \theta _ { 0 } ) ] .
$$

Now it is easily verified that a particular integral of

$$
\frac { d ^ { 2 } u } { d \theta ^ { 2 } } + u = \alpha \frac { \mu ^ { 2 } } { h ^ { 4 } } \left\{ 1 + 2 e \cos ( \theta - \theta _ { 0 } ) + \frac { 1 } { 2 } e ^ { 2 } [ 1 + \cos 2 ( \theta - \theta _ { 0 } ) ] \right\}
$$

is

$$
u = \alpha \frac { \mu ^ { 2 } } { \hbar ^ { 4 } } \left\{ \left( 1 + \frac { 1 } { 2 } e ^ { 2 } \right) + e \theta \sin ( \theta - \theta _ { 0 } ) - \frac { 1 } { 6 } e ^ { 2 } \cos 2 ( \theta - \theta _ { 0 } ) \right\} .
$$

The complete solution of (4.5.3) is, then,

$$
\begin{array} { c } { { \displaystyle { u - \frac { 1 } { p } [ 1 + e \cos ( \theta - \theta _ { 0 } ) ] = \frac { \alpha } { p ^ { 2 } } \left\{ \left( 1 + \frac { 1 } { 2 } e ^ { 2 } \right) + e \theta \sin ( \theta - \theta _ { 0 } ) \right. } } } \\  { \displaystyle { \left. - \frac { 1 } { 6 } e ^ { 2 } \cos 2 ( \theta - \theta _ { 0 } ) \right\} , } } \end{array}
$$

where ${ \mathfrak { P } } = \hbar ^ { 2 } / \mu$

Consider the modification to Keplerian motion described by(4.5.4)； this is due to the terms on the right-hand side. The first of these has the effect of slightly increasing $\mathfrak { U }$ bya constant quantity; this amount will be imperceptible. The third term is small and periodic and its effects will also be imperceptible. But the other term, while fuctuating, has a steadily increasing amplitude, so that after a long enough time it is sure to have a perceptible effect. Ignoring the other terms,we have, so far as observable effects are concerned,

$$
u = \frac { 1 } { p } [ 1 + e \cos ( \theta - \theta _ { 0 } ) ] + \frac { \alpha e } { p ^ { 2 } } \theta \sin ( \theta - \theta _ { 0 } ) .
$$

Let

$$
k \theta = { \frac { \alpha \hat { \theta } } { p } } ,
$$

then,neglecting $\alpha ^ { 2 }$ ,(4.5.5) can be written

$$
u = \frac { 1 } { p } [ 1 \div e \cos ( \theta - \theta _ { 0 } - \dot { \varepsilon } \theta ) ] .
$$

Now at any instant $( \theta _ { \exists } + \mu \theta )$ is the angular coordinate of perihelion, and from (4.5.6) we see that at any instant the planet may be considered to be moving in an ellipse. But the coordinate that defines the line of apsides is continually changing,so that the ellipse can be considered as rotating slowly in space. The rate of angular change of the line of apsides is

$$
\Delta { \omega } = \frac { 2 \pi \alpha } { p } \mathrm { p e r } \mathrm { p e r i o d } \bar { 4 } .
$$

Now,if we substitute the values for the orbit of Mercury,we find that the change, $\Delta _ { w }$ in a century is $4 3 ^ { \prime \prime }$ This may seem to be a very small quantity, but its effects can be observed, and until the advent of the theory of relativity this $4 3 ^ { n }$ remained as a serious discrepancy between observation and prediction based on Newton's law.

# 4.6 The Case $f ( r ) = r ^ { 2 } r ^ { 2 }$

Here it is simplest to resolve the equation of motion along the $\pmb { \mathcal { L } } -$ and $\mathfrak { Y }$ -axes to get

$$
\ddot { x } + n ^ { 2 } x = 0 \quad \mathrm { a . r i d } \quad \ddot { y } + \dot { n } ^ { 2 } y = 0 .
$$

The solution is

$$
x = A \cos ( n t + a ) , y = B \cos ( n t + b ) .
$$

This motion is always finite and must possess apsides. Let the axes be directed so that one apsis lies on the $\Im$ axis,and let $t = 0$ correspond to this apsis. Then at $\dot { \varepsilon } = 0$ ${ \mathfrak { Z } } = { \mathfrak { G } }$ and $\dot { y } = 0$ ,so that $\alpha = \pm \{ \pi / 2 \}$ and $\bar { b } = 0$ Hence the solution can be put in the form

$$
x = A \sin \pi t , y = B \cos \pi t ,
$$

so that the orbit is an ellipse with the origin at its center.

# 4.7The Case $f ( r ) = \mu / { r ^ { 3 } }$ -Cotes'Spirals

This case can be discussed rather simply for two reasons; (4.3.2) takes an elementary form,and $f$ is such that the equations of motion can be integrated easily. We have

$$
V \{ \mathfrak { r } \} = - \frac { \sharp } { 2 \mathfrak { r } ^ { 2 } } ,
$$

S0

$$
\begin{array} { r } { \ddot { \mathfrak { F } } ^ { * } - \tau \dot { \mathfrak { H } } ^ { 2 } = - \frac { \mu } { \mathfrak { p } ^ { 3 } } , } \end{array}
$$

$$
r ^ { 2 } { \dot { \theta } } = \hbar ,
$$

and

$$
\dot { \bar { r } } ^ { 2 } + r ^ { 2 } \dot { \theta } ^ { 2 } - \frac { \ddot { \mu } } { r ^ { 2 } } = 2 C .
$$

Multiplying (4.7.1) by $\mathfrak { r }$ and adding (4.7.3), we get

$$
7 ^ { \bullet } \ddot { \cdot } \stackrel { ! } { \cdot } \dot { \vec { \cdot } } ^ { 2 } = 2 C .
$$

This can be integrated at once to give

$$
r \dot { \vec { z } } = 2 C \dot { \vec { \tau } } + \dot { \vec { A } }
$$

and

$$
r ^ { 2 } = 2 C \ t { \tmspace 4 2 3 4 2 } + 2 A \ t + B ,
$$

where $A$ and $\mathcal { B }$ are arbitrary constants.

If (4.7.5） is valid for all $\pmb { \xi }$ then the right-hand side must be positive for al $\scriptstyle { \dot { \vec { \tau } } } ,$ or

$$
C > 0 \quad \mathrm { a } \Re { \mathrm { ~ \widehat { d } ~ { ~ \widehat { ~ 2 ~ B ~ C ~ - ~ A } ^ { 2 ~ } > 0 ~ } } } .
$$

In this case the motion will never terminate (we assume that it would terminate if the particle fell into the origin); $\Im ^ { * }$ has one minimum value, an apsis, and the orbit branches off asymptotically on either side.

If the conditions (4.7.6) do not hold, the motion must involve the particle's falling into (or starting from) the origin, so that the motion must begin or end. f $C$ is negative, the motion will begin and end, and the orbit will possess one

apsis. Otherwiser willvary monatonically between zero and infinity,and there will be no apsis; the motion is asymptotic unless C= 0.

The solution can be continued as follows: from (4.2.8) we have

$$
\begin{array} { r l } & { \hbar ^ { 2 } = 2 C r ^ { 2 } + \mu - ( r \dot { r } ) ^ { 2 } } \\ & { \quad = 2 C ( 2 C t ^ { 2 } + 2 A t + B ) + \mu - ( 2 C t + A ) ^ { 2 } } \\ & { \quad = \mu + 2 B C - A ^ { 2 } . } \end{array}
$$

Now

$$
\dot { \theta } = \frac { \hbar } { r ^ { 2 } }
$$

so

$$
\theta = ( \mu + 2 B C - A ^ { 2 } ) ^ { 1 / 2 } \int { \frac { d t } { 2 C t ^ { 2 } + 2 A t + B } } + D .
$$

The various cases depending on the signs of $C$ and $( 2 \mathcal { B } \mathcal { C } - A ^ { 2 } )$ are reflected in the behavior of the integral.A full discussion is left to the interested reader; there are six separate cases to be considered.These curves are known as Cotes' spirals.

The form of the orbit can also be investigated by using (4.3.2). We have

$$
{ \frac { \dot { a } ^ { 2 } u } { \dot { a } \theta ^ { 2 } } } \div u = { \frac { \ddot { \mu } } { \hbar ^ { 2 } } } u
$$

or

$$
\frac { \vec { d } ^ { 2 } \mathcal { U } } { \vec { d } \theta ^ { 2 } } \div \mathcal { U } \left( 1 - \frac { \mu } { \hbar ^ { 2 } } \right) = 0
$$

or, substituting for $\hbar ^ { 2 }$ ，

$$
\frac { d ^ { 2 } u } { d \theta ^ { 2 } } + \frac { u } { \hbar ^ { 2 } } ( 2 B C - A ^ { 2 } ) = 0 .
$$

Again,we are concerned with the sign of $( 2 \ B C - A ^ { 2 } )$ ·

An interesting situation occurs when a force $\Im f ^ { 3 }$ is superimposed onto another feld, $f ( x )$ The equations of motion for the feld $f ( \gamma )$ alone can be written

$$
{ \frac { \ddot { \mathtt { i } } } { 2 } } { \dot { r } } ^ { 2 } = { \frac { \dot { h } ^ { 2 } } { 2 r ^ { 4 } } } \left( { \frac { d r } { d \theta } } \right) ^ { 2 } = C - V ( r ) - { \frac { \dot { h } ^ { 2 } } { 2 r ^ { 2 } } } .
$$

With the added attraction $\pi / \gamma ^ { 3 }$ ,the equations of motion become

$$
{ \frac { 1 } { 2 } } { \dot { r } } ^ { 2 } = { \frac { \hbar _ { 1 } ^ { 2 } } { 2 r _ { \cdots } ^ { 4 } } } \left( { \frac { { \dot { d } } r } { { \dot { d } } \theta } } \right) ^ { 2 } = C _ { 1 } - V ( r ) - { \frac { \hbar _ { 1 } ^ { 2 } - v } { 2 r ^ { 2 } } } .
$$

$\beta _ { i j }$ and $C _ { 1 }$ are constants for the new motion; if they are chosen such that

$$
\hbar _ { \tt 3 } ^ { 2 } = \hbar ^ { 2 } \div v \quad \mathrm { a n d } \quad C _ { \tt \equiv } = C _ { \tt 3 }
$$

then the equations (4.7.8) become

$$
\frac { 1 } { 2 } \dot { r } ^ { 2 } = \frac { h ^ { 2 } } { 2 r ^ { 4 } } \left[ \frac { d r } { d ( k \theta ) } \right] ^ { 2 } = C - V ( r ) - \frac { h ^ { 2 } } { 2 r ^ { 2 } }
$$

where $\bar { \kappa } = \bar { \lambda } / \bar { \lambda } _ { 1 }$

Now suppose that the original equations have the solution

$$
r = r _ { 1 } ( t ) , \quad r = r _ { 2 } ( \theta ) .
$$

Then in the new motion,

$$
r = r _ { \hat { 1 } } ( { t - \hat { \varepsilon } _ { 0 } } ) , \quad r = r _ { 2 } [ \hat { \varepsilon } ( \theta - \theta _ { 0 } ) ] .
$$

So, the new orbit resembles the old except that thelatter is continuously rotating. Apsidal angles are increased by the factor $1 / \hbar$ This result was known to Newton.

# 4.8To Find the Law of Force,Given the Orbit

So far we have started with a law of force and have investigated possible orbits. The reverse problem of finding the law of force that may be responsible for a given orbit is also important.

Consider the case of a circular orbit of radius $\pmb { G }$ ,passing through the origin. If the direction $\theta = \emptyset$ passes through the center of the circle, the polar equation is

$$
r = 2 a \cos \theta .
$$

Then

$$
\begin{array} { c } { { u = \displaystyle \frac { 1 } { 2 a \cos \theta } , } } \\ { { 2 a \displaystyle \frac { d u } { d \theta } = \displaystyle \frac { \sin \theta } { \cos ^ { 2 } \theta } , } } \\ { { 2 a \displaystyle \frac { d ^ { 2 } u } { d \theta ^ { 2 } } = \displaystyle \frac { 1 + \sin ^ { 2 } \theta } { \cos ^ { 3 } \theta } , } } \end{array}
$$

and

$$
\frac { \vec { c } ^ { 2 } \varkappa } { \vec { d } \cdot \vec { 2 } ^ { 2 } } + \varkappa = \frac { \mathtt { i } } { \mathfrak { a } \cos ^ { 3 } \theta } .
$$

So, by (4.3.2), we have

$$
\xi ( r ) = \frac { \lambda ^ { 2 } } { \alpha r ^ { 2 } \cos ^ { 3 } \theta } .
$$

This field of force is not conservative, nor is it unique, for we can substitute from (4.8.1) to get laws of force such as

$$
\hat { \beta } ( \tau ) = \frac { \hbar ^ { 2 } } { 2 a ^ { 2 } \tau \cos ^ { 4 } \theta } ,
$$

or

$$
f ( r ) = { \frac { \hbar ^ { 2 } } { 4 a ^ { 3 } \cos ^ { 5 } \theta } } ,
$$

or infinitely many others. But if we want a conservative feld, we must use (4.8.1) to eliminate 0. In this case the solution is unique,and we have

$$
f ( r ) = { \frac { 8 a ^ { 2 } \hbar ^ { 2 } } { r ^ { 5 } } } .
$$

If we are interested only in conservative fields, it is usually simpler to use equation (4.3.1). This avoids the use of u and involves only one diferentiation. Here the equation of the orbit must be used to eliminate θ from dr/d0.For the case considered above we have

$$
\left( { \frac { d r } { d \theta } } \right) ^ { 2 } = 4 a ^ { 2 } \sin ^ { 2 } \theta = 4 a ^ { 2 } - r ^ { 2 } ,
$$

s0

$$
\begin{array} { c } { { V ( r ) = C - \frac { \hbar ^ { 2 } } { 2 \pi ^ { 2 } } - \frac { \hbar ^ { 2 } } { 2 r ^ { 4 } } ( 4 a ^ { 2 } - r ^ { 2 } ) } } \\ { { = C - \frac { 2 a ^ { 2 } \hbar ^ { 2 } } { r ^ { 4 } } , } } \end{array}
$$

leading immediately to (4.8.2).

Now consider the case of a circular orbit of radius $\pmb { a }$ where the center of force $o$ is inside the circle and at a distance $c$ from its center $C$ Let $\mathbfcal { P }$ bea point on the circumference of the circle, and let $\angle P O C = \theta$ (See Figure 4.3.） From the triangle $\ o P C$ we have

$$
a ^ { 2 } = c ^ { 2 } + r ^ { 2 } - 2 c \tau \cos \theta ,
$$

which is the polar equation of the circle. Differentiating this we have

$$
\begin{array} { r } { 0 = ( 2 r - 2 c \cos \theta ) d r + 2 c r \sin \theta d \theta , } \end{array}
$$

so that

$$
\begin{array} { l } { { \left( \frac { d r } { d \theta } \right) ^ { 2 } = \frac { 4 c ^ { 2 } r ^ { 2 } \sin ^ { 2 } \theta } { 4 ( r - c \cos \theta ) ^ { 2 } } } } \\ { { = \frac { r ^ { 2 } [ 4 c ^ { 2 } r ^ { 2 } - ( a ^ { 2 } - c ^ { 2 } - r ^ { 2 } ) ^ { 2 } ] } { ( a ^ { 2 } - c ^ { 2 } + r ^ { 2 } ) ^ { 2 } } . } } \end{array}
$$

But

$$
\left( { \frac { d \varepsilon } { d \theta } } \right) ^ { 2 } = { \frac { 2 r ^ { 4 } } { h ^ { 2 } } } ( C - V ( r ) ) - r ^ { 2 }
$$

S0

$$
\frac { 2 \pi ^ { 4 } } { h ^ { 2 } } ( C - V ( r ) ) = \frac { 4 a ^ { 2 } r ^ { 4 } } { ( a ^ { 2 } - c ^ { 2 } \div r ^ { 2 } ) ^ { 2 } }
$$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/6fcdcfbd3ecdac42ce43853f410f4ec011f67708c6fb18d43b2ad8a041cfa3bf.jpg)  
Figure 4.3

and

$$
C - V ( r ) = \frac { 2 a ^ { 2 } \hbar ^ { 2 } } { ( a ^ { 2 } - c ^ { 2 } + r ^ { 2 } ) ^ { 2 } } .
$$

Then

$$
\displaystyle { f ( r ) = \frac { 8 a ^ { 2 } \hbar ^ { 2 } r } { ( a ^ { 2 } - c ^ { 2 } \div r ^ { 2 } ) ^ { 3 } } . }
$$

This solution is unique,provided $c \neq 0$

It should be remembered that if we start off with the law of force (4.8.4), then there are infinitely many possible orbits, of which the circular orbit is only one.Also,if we wanted a law of force to account for any circular orbit with the center of force anywhere inside the circle, then (4.8.4) would be no good, since it specifies $a ^ { 2 } - c ^ { 2 }$

Consider the Keplerian orbit.From Kepler's first two laws it is established that the orbit of a planet is central and that its equation can be expressed as

$$
\frac { \pi } { r } = 1 + e \cos \theta .
$$

Here $\mathcal { P }$ and $\mathcal { E }$ are not specified; in fact we can give $e$ any positive value. From the equation of the orbit,

$$
\left( { \frac { d { \mathcal { F } } } { d \theta } } \right) ^ { 2 } = \left( { \frac { e } { p } } \varsigma ^ { 2 } \sin \theta \right) ^ { 2 }
$$

$$
= \frac { r ^ { 4 } } { p ^ { 2 } } \left[ e ^ { 2 } - \left( \frac { p } { r } - \mathbb { i } \right) ^ { 2 } \right] .
$$

So, from (4.3.1),

$$
{ \frac { h ^ { 2 } } { 2 p ^ { 2 } } } \left[ e ^ { 2 } - \left( { \frac { p } { r } } - 1 \right) ^ { 2 } \right] + { \frac { \lambda h ^ { 2 } } { 2 r ^ { 2 } } } = C - V ( r )
$$

Or

$$
{ \frac { \hbar ^ { 2 } } { p \tau } } + { \frac { \hbar ^ { 2 } ( e ^ { 2 } - 1 ) } { 2 p ^ { 2 } } } = C - V ( \tau ) .
$$

Then, with the proviso that V tends to zero as r tends to infinity, the constant terms go $\cot \frac { \frac { 1 } { 2 } } { 2 }$ and we have

$$
V ( r ) = - \frac { \hbar ^ { 2 } / \mathfrak { p } } { r } = - \frac { \mu } { r } .
$$

This is the inverse square law of attraction. It will account for any conic orbit as long as the origin is at one focus.

In writing down (4.1.1）we considered $- f \hat { \mathfrak { T } }$ to be the force per unit mass. Assuming the form f(r)= μ/r²,it follows that the force acting on a planet of mass m is -(μm/r²)r. Now, from Newton's third law,the planet must be exerting an equal and opposite force on the Sun;but this force should be predicted by the same inverse square law and must be of the form-(μ'M/r²)r, where $\overrightarrow { M }$ is the mass of the Sun.Hence both forces must be equal in magnitude to

$$
G \frac { \vec { M } \cdot \vec { m } } { r ^ { 2 } } .
$$

This embodies Newton's law of gravitation. $G$ is the Newtonian gravitational constant,and its value is found experimentally to be $6 . 6 7 0 \times 1 0 ^ { - 8 }$ c.g.s. units. The motion observed in the solar system confirms that $G$ is a constant which is independent of physical conditions such as temperature or chemical composition,and it is reasonable to expect that it is $\hat { \bf a }$ universal constant of nature.

Since M is much greater than m for any planet,the effects of the attraction of that planet on the Sun are small compared with the effects of the attraction of the Sun on the planet; so the situation in the solar system corresponds approximately to a model with a fixed center of attraction. The general problem, in which two masses move in one another's fields,is considered in Chapter 6.

# 4.9 The “Universality” of Newton's Law

Newton's law of gravitation is described as being “universal.” It is applied in many contexts,and it is important to see what justification there may be for applying it to situations outside the solar system. We have seen that Newton's law follows from Kepler's first two laws of planetary motion (the third cannot be invoked because it is not accurate), so if we can find two bodies traveling around each other in accord with Kepler's first two laws, we know that they are subject to Newton's law.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/b521529073e3c8e0a4dfec933fd77ee8459f87e60fbcdb1d83ebef6e2bfeeaa7.jpg)  
Figure 4.4

Fortunately there are many such systems, where two stars are observed to be moving around each other; these are called visual binaries (as opposed to other types of binary, which reveal their duplicity by showing two spectra, or one spectrum with regularly shifting lines,or by eclipsing each other).Where two such stars are observed, the motion of the fainter star,or companion, is plotted with respect to the brighter or primary star. These observed, or apparent, orbits are found to be ellipses,and the law of areas about the primary is obeyed; but the primaries are not at the foci of the ellipses. This is not necessarily a contradiction of Kepler's first law, since we are not observing the true orbit, but a projection of it. The true orbit, $\pmb { S }$ will lie in a plane that is unlikely to be at right angles to the line of sight. The apparent orbit $S ^ { \prime }$ is the projection f $\boldsymbol { s }$ onto the plane (sometimes called the plane of the sky) which is at right angles to the line of sight.

Now an ellipse will always project into another ellipse,and therefore since $S ^ { \prime }$ is observed to be an ellipse, $S$ is an ellipse also.The law of areas depends on ratios; but ratios are not altered by projection,and since the law of areas holds for the apparent orbit,it must also hold for the true orbit. Hence we can apply the theory of central orbits to the true orbit. We assume that the stars are spheres,so that their fields depend on the distance from their centers and not on orientation,and we assume conservative fields.

Now,with a suitable projection,a focus of $\boldsymbol { S }$ can be made to project into any desired point of $S ^ { \prime }$ (although the shape of $S ^ { \prime }$ will naturally be affected by the projection), so whatever the position of the primary in $S ^ { \beta }$ ,there is always a possible ellipse $\mathcal { S }$ with the primary at one focus. Thus it is possible, by geometrical reasoning, to argue that Kepler's first two laws could hold for the motion of double stars so that Newton's law would follow. But we want to show that Newton's law is the only plausible one,and to do this we must show that there is no reasonable law to account for elliptic motion unless the center of attraction is at one focus of the ellipse.

Consider an ellptic orbit described under the action of a force directed toward an arbitrary point inside the ellipse. If this point is taken as origin, the equation of the ellipse must be taken in its general form:

$$
g ( x , y ) \equiv a x ^ { 2 } + 2 n x y + b y ^ { 2 } + 2 m x + 2 i y + c = 0 .
$$

To find a law of force that is responsible for this orbit,we can change to polar coordinates and use (4.3.2).But it is more straightforward to derive an expression for the force in terms of cartesian coordinates.

The equations of motion are

$$
\ddot { x } = - f ( r ) { \frac { x } { r } } , \quad \ddot { y } = - f ( r ) { \frac { \ddot { y } } { r } } ,
$$

and the angular momentum integral can be written

$$
x { \dot { y } } - y { \dot { x } } = h .
$$

The equation of the orbit is $g \{ x , y \} = 0$ Differentiating this with respect to $\ddagger .$ we find

$$
\frac { \partial g } { \partial x } \cdot \frac { d x } { d t } + \frac { \partial g } { \partial y } \cdot \frac { d y } { d t } = 0 .
$$

which can be written

$$
g _ { x } { \dot { x } } + g _ { y } { \dot { y } } = 0 .
$$

Eliminating $\dot { y }$ by means of (4.9.3), we have

$$
{ \dot { z } } = - { \frac { { \hbar g _ { y } } } { x g _ { x } + y g _ { y } } } .
$$

Similarly,

$$
{ \dot { y } } = { \frac { h g _ { x } } { x g _ { x } + y g _ { y } } } .
$$

Differentiating again, we have

$$
\ddot { z } = \frac { \partial \dot { z } } { \partial x } \dot { z } + \frac { \partial \dot { x } } { \partial y } \dot { y } .
$$

Substituting for $\mathscr { Z }$ and performing the differentiations, we get, eventually,

$$
\ddot { x } = \frac { \bar { h } ^ { 2 } { \dot { x } } \left( - g _ { y } ^ { 2 } g _ { x x } + 2 g _ { x } g _ { y } g _ { x y } - g _ { x } ^ { 2 } g _ { y y } \right) } { ( x g _ { x } + y g _ { y } ) ^ { 3 } } .
$$

Then, from (4.9.2), we have

$$
f ( \tau ) = \hbar ^ { 2 } \tau ^ { \prime } \frac { ( g _ { y } ^ { 2 } g _ { x x } - 2 g _ { x } g _ { y } g _ { x y } + g _ { x } ^ { 2 } g _ { y y } ) } { ( x g _ { x } + y g _ { y } ) ^ { 3 } } .
$$

This law of force will account for any orbit, $g \{ { \mathfrak { x } } , { \mathfrak { y } } \} = 0$ Now substituting from (4.9.1), differentiating, and using (4.9.1) to eliminate quadratic terms, we get

$$
f ( r ) = h ^ { 2 } r \frac { ( a b c + 2 i m n - a ^ { 2 } - b m ^ { 2 } - c n ^ { 2 } ) } { ( m x + i y + c ) ^ { 3 } } .
$$

Now the line $\eta _ { 2 } x + \bar { \xi } y + c = 0$ is called the polar of the origin with respect to the conic,and the distance of the point $\{ x , y \}$ from the line is the positive value of

$$
\frac { m x + i y + c } { ( i ^ { 2 } + \mathfrak { m } ^ { 2 } ) ^ { 1 / 2 } } .
$$

Hence (4.9.5) can be expressed verbally in the following form, due to Hamilton:

For a particle at $\mathcal { P }$ to describe an elliptic orbit under the action of a central force directed toward the point $o$ ，the force acting on $\mathcal { P }$ varies directly as the radius from $o$ and inversely as the cube of the perpendicular distance from $\mathcal { P }$ to the polar of $o$ with respect to the ellipse.

This is not valid if $o$ is at the center of the ellipse, since then the polar of $o$ is at infinity. A proof of this theorem,using projective geometry, is given in Introduction to Dynamics by L.A. Pars, p.299 (Ref.6).

In general the law of force given by Hamilton's theorem is not conservative. If it is conservative, then for points $\{ \mathfrak { X } , \mathfrak { Y } \}$ on the ellipse, $( \eta x + l y + c )$ must bea function of $\pmb { \mathcal { J } } ^ { 2 }$ To investigate this condition, rotate the axes so that the polar of the origin is parallel to the $\mathscr { Y }$ axis, when ${ \vec { \mathbf { \ell } } } = \boldsymbol { \mathbb { 0 } }$ Then,for points on the ellipse, $\mathscr { Z }$ must be a function of $\uparrow ^ { \star }$ This can be written

$$
{ \mathfrak { X } } = { \mathfrak { q } } \{ { \mathfrak { r } } \}
$$

an expression that must be identical with the equation of the ellipse. It follows that (4.9.6) must be a quadratic in $\mathscr { X }$ and $\mathfrak { Y }$ ,and this means that the function $\mathcal { G }$ is confined to the following two forms: (1) $q ( q ) \equiv a + b q ^ { 2 }$ and (2) $g ( \gamma ) \equiv a + b \gamma ^ { 2 }$ [The form $q ( r ) \equiv a + b r + c r ^ { 2 }$ does not make (4.9.6) a quadratic in $\mathfrak { L }$ and $y =$

Form (1) gives a circular orbit with the center of force somewhere inside the circle. This is not acceptable for various reasons. The force exerted by the primary would at first increase and later decrease with increasing distance from the star,which seems unlikely. It is strange that only circular orbits occur. That there are other orbits close to the circular orbits can be seen as follows. Consider the apsidal equation, (4.1.12). For the circular orbit this has two positive roots, $r = \{ a \div c \}$ and $( a - c )$ Then, provided $^ c$ is not zero, small changes in the energy geometrical reasoning, to argue that Kepler's first two laws could hold for the motion of double stars so that Newton's Iaw would follow. But we want to show that Newton's law is the only plausible one,and to do this we must show that there is no reasonable law to account for eliptic motion unless the center of attraction is at one focus of the ellipse.

Consider an elliptic orbit described under the action of a force directed toward an arbitrary point inside the ellipse. If this point is taken as origin, the equation of the ellipse must be taken in its general form:

$$
g ( x , y ) \equiv a x ^ { 2 } + 2 a x y + b y ^ { 2 } + 2 m x + 2 l y + c = 0 .
$$

To find a law of force that is responsible for this orbit,we can change to polar coordinates and use (4.3.2). But it is more straightforward to derive an expression for the force in terms of cartesian coordinates.

The equations of motion are

$$
\ddot { z } = - f ( r ) { \frac { x } { r } } , \quad \ddot { y } = - f ( r ) { \frac { \ddot { y } } { r } } ,
$$

and the angular momentum integral can be written

$$
{ \mathfrak { Z } } { \dot { \mathfrak { Y } } } - { \mathfrak { Y } } { \dot { \mathfrak { X } } } = { \dot { \lambda } } .
$$

The equation of the orbit is $g \{ x , y \} = 0$ Differentiating this with respect to $\scriptstyle { \frac { \dag } { \hat { \varepsilon } } } ,$ we find

$$
\frac { \partial g } { \partial x } \cdot \frac { d x } { d t ^ { \frac { 3 } { 2 } } } \div \frac { \partial g } { \partial y } \cdot \frac { d y } { d t } = 0 .
$$

which can be written

$$
g _ { x } { \dot { x } } + g _ { y } { \dot { y } } = 0 .
$$

Eliminating $j$ by means of (4.9.3), we have

$$
{ \dot { x } } = - { \frac { { \hbar g _ { y } } } { { x g _ { x } + y g _ { y } } } } .
$$

Similarly,

$$
{ \dot { y } } = { \frac { \hbar g _ { x } } { x g _ { x } + y g _ { y } } } .
$$

Diferentiating again, we have

$$
\ddot { x } = \frac { \partial \dot { x } } { \partial x } \dot { x } + \frac { \partial \dot { x } } { \partial y } \dot { y } .
$$

Substituting for $\mathscr { x }$ and performing the differentiations, we get, eventually,

$$
\ddot { x } = \frac { \hbar ^ { 2 } x ( - \mathcal { G } _ { y } ^ { 2 } g _ { x x } + 2 \mathcal { G } _ { x } \mathcal { G } _ { y } \mathcal { G } _ { x y } - g _ { x } ^ { 2 } \mathcal { G } _ { y y } ) } { ( x \mathcal { G } _ { x } + y \mathcal { G } _ { y } ) ^ { 3 } } .
$$

Then, from (4.9.2), we have

$$
f ( \tau ) = \lambda ^ { 2 } \tau \frac { ( g _ { y } ^ { 2 } g _ { x x } - 2 g _ { x } g _ { y } g _ { x y } + g _ { x } ^ { 2 } g _ { y y } ) } { ( x g _ { x } + y g _ { y } ) ^ { 3 } } .
$$

This law of force will account for any orbit, $g \{ { \mathfrak { x } } , y \} = 0$ Now substituting from (4.9.1), differentiating, and using (4.9.1) to eliminate quadratic terms, we get

$$
f ( r ) = h ^ { 2 } r \frac { ( a b c + 2 i m n - a l ^ { 2 } - b m ^ { 2 } - c n ^ { 2 } ) } { ( m x + l y + c ) ^ { 3 } } .
$$

Now the line $\eta _ { 2 } x + l y + c = 0$ is called the polar of the origin with respect to the conic, and the distance of the point $\{ \ v { x } , \ v { y } \}$ from the line is the positive value of

$$
\frac { m x + l y + c } { ( l ^ { 2 } + m ^ { 2 } ) ^ { 1 / 2 } } .
$$

Hence (4.9.5) can be expressed verbally in the following form, due to Hamilton:

For a particle at $\mathcal { P }$ to describe an elliptic orbit under the action of a central force directed toward the point $o$ ，the force acting on $P$ varies directly as the radius from $\pmb { \mathcal { O } }$ and inversely as the cube of the perpendicular distance from $\mathcal { P }$ to the polar of $o$ with respect to the ellipse.

This is not valid if $o$ is at the center of the ellipse, since then the polar of $o$ is at infinity. A proof of this theorem,using projective geometry, is given in Introduction to Dynamics by L.A. Pars, p. 299 (Ref. 6).

In general the law of force given by Hamilton's theorem is not conservative. If it is conservative, then for points $\{ \mathfrak { L } , \mathfrak { Y } \}$ on the ellipse, $( m x + l y + c )$ must bea function of $\Im ^ { * }$ To investigate this condition, rotate the axes so that the polar of the origin is parallel to the $\mathscr { Y }$ -axis, when $\xi = 0$ Then, for points on the ellipse, $\pmb { \mathcal { Z } }$ must be a function of $\mathscr { T }$ This can be written

$$
x = g _ { \ell } ^ { \ell } ( \vec { \mathfrak { z } } )
$$

an expression that must be identical with the equation of the ellipse. It follows that (4.9.6) must be a quadratic in $\pmb { \mathcal { X } }$ and $\Im$ ,and this means that the function $\mathcal { G }$ is confined to the following two forms: (1) $q ( \gamma ) \equiv a + b \gamma ^ { 2 }$ ,and (2) $q ( 3 ) \equiv a + b _ { 2 }$ [The form $q ^ { \prime } ( r ) \equiv a + b r + c r ^ { 2 }$ does not make (4.9.6) a quadratic in $\mathscr { X }$ and $y . ]$

Form (1) gives a circular orbit with the center of force somewhere inside the circle. This is not acceptable for various reasons. The force exerted by the primary would at frst increase and later decrease with increasing distance from the star,which seems unlikely. It is strange that only circular orbits occur.That there are other orbits close to the circular orbits can be seen as follows. Consider the apsidal equation, (4.1.12). For the circular orbit this has two positive roots, $z ^ { * } = \{ a \pm c \}$ and $\{ a - c \}$ Then, provided $\pmb { c }$ is not zero, smallchanges in the energy and angular momentum will still leave the apsidal equation with two positive roots (which will differ only slightly from those of the circular orbit），and the motion will be confined to values of r lying between these roots; but it will no longer be circular, so that the observed orbit will no longer be elliptic. Hence this case can be disregarded. (In some cases spectroscopic observations yield the component of orbital velocity in the line of sight; this is of such a nature as to rule out these circular orbits.)

Form（2） gives the orbit

$$
r \cos \theta = a + b r
$$

since $x = r \cos \theta$ But this is the Keplerian orbit that we are trying to justify.

One other case must'be discussed. If the primary is at the center of the ellpse S, then we have the law of force f= n²r. But from the properties of projection the primary will still be at the center of the apparent ellipse, S', and this is not observed.

We have established that Newton's law is the only plausible law governing the Keplerian motion within the solar system,and where they are sufficiently observed,the motions of exterior systems.In addition this law has successfully predicted or accounted for nearly every other observed motion that involves deviations from Keplerian motion caused by perturbations. It has also led to anaccurate modification of Kepler's third law. The remainder of the text will be devoted to a discussion of some of its consequences.

# 4.10Worked Examples

The problems below are intended to help readers become thoroughly accustomed to working with central orbits. In many cases the solution is halfway achieved when the energy and angular momentum integrals have been written down,and the values of $\hslash$ and $C$ found from the initial conditions.Readers should have these equations at their fingertips; they will also need to be able to use all the properties of Keplerian motion discussed above.Facility with these formulas can only be achieved through practice. Some of the methods that are useful in solving these problems are illustrated in the examples worked below.

1.A particle moves in a circular orbit of radius a under an attraction toa point inside the circle. The greatest and least speeds of the particle in its orbit are ${ \mathfrak { V } } _ { \Sigma }$ and v2.(See Figure 4.5).Show that the period is

$$
{ \frac { \pi a ( v _ { \tt A } + \tau _ { 2 } ) } { v _ { 1 } v _ { 2 } } } .
$$

Since the angular momentum about the center of force is constant,the greatest and least speeds must be achieved at the ends of a diameter that passes through the center of force. Let the pericenter distance be x; then the angular momenta at the ends of this diameter are $\boldsymbol { \mathfrak { X } } \boldsymbol { \mathfrak { U } } _ { \perp }$ and $( 2 a - x ) v _ { 2 }$ But these are both equal to $h _ { i }$ s0

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/2e3f18a5350da9fecbfb3a4fd95c115c5c76e91e23959063f89d2c8def3554f7.jpg)  
Figure 4.5

$$
\hbar = x v _ { 1 } = ( 2 a - x ) v _ { 2 } .
$$

Eliminating $\mathscr { X }$ and solving for $h$ we find

$$
\hbar = 2 a \frac { v _ { 1 } v _ { 2 } } { v _ { 1 } + v _ { 2 } } .
$$

The areal velocity is $\frac { 3 } { 2 } h$ ,and the product of the areal velocity and the period is equal to the total area of the circle, $\pi a ^ { 2 }$ .Hence

$$
\bar { p } \cdot a \frac { v _ { \bar { 1 } } v _ { 2 } } { v _ { \bar { 1 } } + v _ { 2 } } = \pi a ^ { 2 }
$$

and the answer follows at once.

[N.B.A reader who set about this problem by finding the law of force and working from that would run into difficulties.]

2.A particle is projected with velocity $\sqrt { 2 \mu / 3 a ^ { 3 } }$ at right angles to the radius vector at a distance a from the center of an attracting force $\mu _ { i } / 3 ^ { 4 }$ per unit mass. Find the path of the particle and show that the time it takes to reach the center is

$$
\frac { 3 \pi } { 8 } \sqrt [ ] { \frac { 3 a ^ { 5 } } { 2 \mu } } .
$$

From the initial conditions the angular momentum is

$$
\hbar = a \sqrt { \frac { 2 \mu } { 3 a ^ { 3 } } } = \sqrt { \frac { 2 \mu } { 3 a } } .
$$

The potential function is $V = - \mu / 3 \gamma ^ { 3 }$ ,so the energy of the orbit is

$$
C = { \frac { 1 } { 2 } } \left( { \frac { 2 \mu } { 3 a ^ { 3 } } } \right) - { \frac { \mu } { 3 a ^ { 3 } } } = 0 .
$$

Then,from equation (4.3.1)，we have

$$
\left( { \frac { d r } { d \vartheta } } \right) ^ { 2 } = { \frac { 2 r ^ { 4 } } { \hbar ^ { 2 } } } \left( { \frac { \mu } { 3 r ^ { 3 } } } - { \frac { \hbar ^ { 2 } } { 2 r ^ { 2 } } } \right)
$$

and substituting for $h$ and simplifying, we get

$$
\begin{array} { l } { \displaystyle \left( \frac { d r } { d \theta } \right) ^ { 2 } = a r - r ^ { 2 } } \\ { = \frac { 1 } { 4 } [ a ^ { 2 } - ( 2 r - a ) ^ { 2 } ] . } \end{array}
$$

Then

$$
\frac { 2 \delta \varepsilon } { [ a ^ { 2 } - ( 2 r - a ) ^ { 2 } ] ^ { 1 / 2 } } = d \theta
$$

which can be integrated to give

$$
\cos ^ { - 1 } \left\{ { \frac { 2 \tau - a } { a } } \right\} = \theta - \theta _ { 0 }
$$

or

$$
2 \tau = a [ 1 \div \cos ( \theta - \theta _ { 0 } ) ] .
$$

Let us measure $\theta$ such that $\hbar = 0$ when $r = a$ then $\hat { \theta } _ { \Updownarrow } = \Updownarrow$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/a59d138374c8b36dc152a76956980eff1b204566f48974f2aa4f876b14ce8c4f.jpg)  
Figure 4.6

As $\theta$ goes from 0 to $\mathfrak { F }$ $\mathfrak { r }$ goes from $\pmb { \mathcal { Q } }$ to 0. The area swept out by the radius vector is

$$
\begin{array} { l } { { \displaystyle { \cal A } = \frac { 1 } { 2 } \int _ { 0 } ^ { \pi } r ^ { 2 } d \theta = \frac { a ^ { 2 } } { 8 } \int _ { 0 } ^ { \pi } ( 1 + \cos \theta ) ^ { 2 } d \theta } } \\ { { \displaystyle ~ = \frac { a ^ { 2 } } { 8 } \left[ \theta + 2 \sin \theta + \frac { 1 } { 2 } \theta + \frac { 1 } { 4 } \sin 2 \theta \right] _ { 0 } ^ { \pi } } } \\ { { \displaystyle ~ = \frac { 3 a ^ { 2 } \pi } { 1 6 } . } } \end{array}
$$

The time taken is this area divided by the areal velocity, or

$$
\frac { 2 A } { \hbar } = \frac { 3 \pi } { 8 } \sqrt { \frac { 3 a ^ { 5 } } { 2 \mu } } .
$$

3. A particle moving under the action of $\clubsuit$ central force of attraction $\mu _ { i } / 3 ^ { - 2 }$ isprojected from infinity with velocity $\pmb { \ V }$ so as to pass the center of force at a distance $^ { c }$ i the force did not erist. Show that the equation of the orbit is

$$
\textstyle { \frac { 1 } { r } } = { \frac { \mu } { V ^ { 2 } c ^ { 2 } } } + { \frac { 1 } { c } } \cos \theta { \sqrt { \frac { 1 } { \frac { 1 } { 2 } } + { \frac { \mu ^ { 2 } } { c ^ { 2 } V ^ { 4 } } } } }
$$

where $\mathfrak { g }$ is measured from an apsis.

From the properties of motion under the inverse square law of attraction, we know that the orbit is a conic, and since the particle has finite velocity at infinity, it is a hyperbola.Then if $\boldsymbol { \theta }$ is measured from the apsis, the polar equation of the orbit is

$$
\frac { \mathcal { P } } { \mathfrak { r } ^ { \mathrm { ~ ~ } } } = \mathbb { i } + \mathscr { e } \cos \theta ,
$$

where

$$
p = a \{ 1 - e ^ { 2 } \} = \frac { \hbar ^ { 2 } } { \mu } ,
$$

$\Bbbk$ being the angular momentum.

The energy equation is

$$
{ \bar { \mathcal { V } } } ^ { 2 } = \mu \left\{ { \frac { 2 } { r } } - { \frac { 1 } { a } } \right\} ,
$$

and from the initial conditions, this gives

$$
\begin{array} { r } { a = - \frac { \mathcal { Y } } { Y ^ { 2 } } . } \end{array}
$$

Also from the initial conditions,

$$
\hbar = c Y .
$$

Substituting for $\pmb { \mathcal { Q } }$ and $\hslash$ into (4.10.1) and solving for $e ^ { 2 }$ ,we find

$$
e ^ { 2 } = \mathbb { i } + \frac { c ^ { 2 } \mathbb { Y } ^ { 4 } } { \mu ^ { 2 } }
$$

so that the equation of the orbit becomes

$$
\frac { ( c ^ { 2 } V ^ { 2 } / \mu ) } { r } = 1 + \cos { \theta } \sqrt { \frac { 1 + } { \frac { c ^ { 2 } V ^ { 4 } } { \mu ^ { 2 } } } } ,
$$

from which the result follows at once.

4 $A$ particle is projected froma pointA at right angles to SA and isacted on by $\alpha$ force varying inversely as the square of the distance toward $S$ If the intensity of the force is unity at unit distance， $\pmb { S A }$ ，and the speed of projection is $\frac { \underline { { \hat { \mathbf { j } } } } } { 2 } .$ show that the eccentricity of the orbit is $\frac { 3 } { \frac { \xi } { \pm } }$ andfind the periodic time.

With the dimensions given in the question, the law of attraction is $\Im f \Im ^ { 2 }$ ， and the potential function is $- ( I / \gamma )$ .The energy of the orbit is

$$
C = { \frac { 1 } { 2 } } v ^ { 2 } - { \frac { 1 } { r } } = { \frac { 1 } { 8 } } - 1
$$

which is negative; hence the orbit is an ellipse. Using the energy integral in the form

$$
v ^ { 2 } = \frac { 2 } { r } - \frac { 1 } { a } ,
$$

we find $a = 4 / 7$

The angular momentum of the orbit is $\frac { \texttt { I } } { 2 }$ ,and since

$$
\begin{array} { r } { a _ { \mathrm { \ell } } ^ { \prime } ( 1 - e ^ { 2 } ) = \lambda ^ { 2 } , } \end{array}
$$

we have

$$
\begin{array} { r } { \frac { 4 } { 7 } ( 1 - e ^ { 2 } ) = \frac { 1 } { 4 } } \end{array}
$$

so that

$$
\begin{array} { r } { e = \frac { 3 } { 4 } . } \end{array}
$$

To find the period, we use the formula

$$
P = 2 \pi { \sqrt { \frac { a ^ { 3 } } { \mu } } } , \quad { \mathrm { w h e r e ~ } } \mu = 1
$$

so that $P = 1 6 \pi / 7 \sqrt { 7 }$ units of time.

# 4.11 Problems

1. Find the condition for the Iaw of force to result in finite motion for all values of $C$

2.A particle moves in a feld of force $\mu _ { i } / { \gamma } ^ { 2 }$ toward the origin. Show that its orbit isa conic.If the maximum and minimum speeds in an elliptical orbit are ${ \mathfrak { V } } _ { 1 }$ and $z _ { 2 }$ ，find the values of $a , e ,$ the period and the angular momentum,in terms of $\mathfrak { V } _ { \mathfrak { I } }$ ， ${ \mathfrak { V } } _ { 2 }$ and $\mu$

3.A particle moves in a field of force $\mu _ { i } / \gamma ^ { 2 }$ toward the origin. It is projected with velocity $\pmb { \ V }$ from $\mathbf { a }$ point at distance $\mathcal { R }$ at an angle $\beta$ to the radius vector. Show that in the subsequent motion

$$
\dot { \bar { r } } ^ { 2 } = V ^ { 2 } - \frac { 2 \mu } { R } + \frac { 2 \mu } { \bar { r } } - \frac { R ^ { 2 } V ^ { 2 } \sin ^ { 2 } \beta } { r ^ { 2 } } .
$$

Hence find conditions satisfied by ${ \mathfrak { R } } , \ { \mathfrak { V } } , \ { \mathfrak {beta } }$ so that $\gamma$ may $( a )$ increase steadily to infinity, (b) decrease toa minimum and then increase to infinity,(c) oscillate between two fixed values.

4.Show that in elliptic motion about $\hat { \mathbf { \Omega } }$ focus under attraction $\mu _ { i } / { \tau } ^ { 2 }$ ，the radial velocity is given by the equation

$$
r ^ { 2 } \dot { \vec { r } } ^ { 2 } = \frac { \mu } { a } \{ a ( 1 + e ) - r \} \{ \vec { r } - a ( 1 - e ) \} .
$$

5. Show that for a central orbit described under the Iaw of force $\mu / \gamma ^ { 2 }$ ,the apsidal distances are given by the roots of the quadratic

$$
2 C \tau ^ { 2 } \div 2 \mu \tau - \hbar ^ { 2 } = 0 .
$$

Hence, or otherwise, show that for an elliptic orbit $C = - \{ \mu / 2 a \}$ and $\hbar ^ { 2 } = \mu \mathfrak { p } .$ where $\mathcal { P }$ is the length of the semilatus rectum.

6.Find the condition for a circular orbit,described under the law of force $f ( r ) = \mu / r ^ { \ast }$ ,to be stable. Investigate the stability of circular motion under the following laws of force:

$$
\frac { \mu } { r ^ { 2 } } , ~ \frac { v } { r ^ { 3 } } , ~ \frac { \mu } { r ^ { 2 } } \div \frac { v } { r ^ { 3 } } , ~ \frac { \mu } { r ^ { 2 } } + \frac { v } { r ^ { 4 } } .
$$

7.A particle moves subject to a repulsive force $\mu f ^ { - 2 }$ away from the origin. Show that the orbit is the branch of $\clubsuit$ hyperbola that does not contain the origin,the origin being at $\hat { \pmb { \alpha } }$ focus.If the particle is projected with velocity $\sqrt { \mu / c }$ froma point distant $c$ from the origin,at right angles to theradius vector, find the eccentricity of the hyperbola.

8.A particle describes an ellipse under the action of a central force directed toward a focus.Find,in terms of the eccentricity of the ellipse,the ratio of the time spent near pericenter between the ends of the latus rectum to the total period of the orbit.

9.A particle acted on by a central force $\mu / \gamma ^ { 2 }$ is projected with velocity $\mathcal { U }$ at right angles to the radius vector at a distance $c$ from the center of force. Investigate the limits of $\mathfrak { Q }$ that yield the various types of conic orbit,and in the case of the eliptic orbit find the eccentricity and major axis,and also find the condition as to whether the projection point at the end of the major axis is at pericenter or apocenter.

10.A body is describing an ellipse of eccentricity eunder the action of a force tending toward a focus, and when it is at the near apsis the center of force is transferred to the other focus. Show that the eccentricity of the new orbit is

$$
{ \frac { e ( 3 \pm e ) } { 1 - e } } .
$$

11.If the apsidal distances are a and b, where a is greater than b, show that the velocity at the former is given by

$$
v _ { \alpha } ^ { 2 } = \frac { 2 b ^ { 2 } } { b ^ { 2 } - a ^ { 2 } } \int _ { a } ^ { b } \mathcal { F } \bar { d } \bar { \tau }
$$

and the velocity at any distance $\pmb { \mathcal { F } }$ is given by

$$
v ^ { 2 } = \frac { 2 a ^ { 2 } } { b ^ { 2 } - a ^ { 2 } } \int _ { a } ^ { r } F d r + \frac { 2 b ^ { 2 } } { b ^ { 2 } - a ^ { 2 } } \int _ { r } ^ { b } F d r ,
$$

where $\pmb { F }$ is the central force.

12. If(C) is a closed orbit described under the action of a central force, S the center of force, $o$ the center of gravity of the area enclosed by the curve $( C )$ and $G$ the center of gravity of the curve $\{ C \}$ ,on the supposition that the density at each point varies inverselyas the speed,show that the points S,O,and G are collinear and that 2SG= 3SO.Show also that the center of gravity of the curve $( C )$ ,assuming constant density,also lies on the line $S O G$

13.Find the condition for the stability of $\gtrdot$ circular orbit,described under the law of force $f ( x )$ toward the center of the circle,by considering the equation (4.1.11).

14.A particle moving ina circular orbit with speed ${ \mathfrak { V } } _ { C }$ under the action ofa force directed toward its center is given a small radial impulse resulting in an initial radial velocity $\delta { v } _ { c }$ If the resulting motion is stable,show that the mean of the apsidal distances is approximately $\mathfrak { L }$ ,the radius of the original circle. Solve the equations of motion for $\pmb { \tau }$ and $\boldsymbol { \theta }$ and show that the apsidal angle is $\pi / \frac { \pi } { 2 }$ where

$$
{ \mathfrak { z } } ^ { 2 } = 3 + { \frac { \alpha f ^ { \prime } ( \alpha ) } { f ( \alpha ) } } .
$$

15.Aparticledescribes $\mathtt { a }$ circle,of radius $\pmb { \mathcal { Q } }$ ,steadilyunder $\hat { \mathbf { \Omega } }$ centralattraction $\phi ( \gamma ) = \beta _ { 1 } \gamma _ { 3 } 3$ to the center of the circle,where $\phi ^ { \prime } ( a ) > \widehat { \mathfrak { V } }$ Show that the period ofa small oscillation about the steady motion is

$$
2 \pi \sqrt [ 4 ] { \frac { a ^ { 3 } } { \phi ^ { \prime } ( a ) } } .
$$

16.A body is describing an ellipse under the action of a force to a focus. When the body is at one extremity of the minor axis, the law of force is changed without instantaneous change of the magnitude of the force or of the velocity. If the force now varies as the distance, show that the periodic time is the same as before.

17.A particle, acted on by a central force of attraction toward a point $o$ varying as the distance, is projected froma point $P$ so as to pass through a point $Q$ such that $O P = O Q$ Show that the least possible speed of projection is

$$
O P { \sqrt { \mu \sin \angle P O Q } }
$$

where $\mu \mathcal { O P }$ is the force per unit mass,and find its direction.

18.Two particles are describing the same ellipse about a center of force in the center in opposite directions, the mass of one being double that of the other. If the particles meet and coalesce at the end of the minor axis, show that the new orbit trisects the major axis of the old.

19. If two particles $P , Q$ describe the same ellipse under the same central force to the center $C$ ,show that the area of the triangle $C P Q$ is invariable.

20. If a particle is describing an ellipse about a center of force in the center, show that the sum of the reciprocals of its angular velocities about the foci is constant.

21.A particle is moving in a circular orbit under the action of a central force $\mu / \tau ^ { 3 }$ when it receives a small tangential impulse. Trace the future orbit for the two cases of the impulse increasing and decreasing the speed.

22.A particle is subject to a central attraction $\mu / r ^ { 3 }$ per unit mass toward a fxed point $o$ It is projected from a point $\mathcal { P }$ ，with speed $\sqrt { \mu } / O P$ ,in $\hat { \mathbf { \Omega } }$ direction making an angle $\alpha$ with the radius vector $o p$ Show that the tangent to the path at every point makes a fixed angle with the radius vector.

23.Using the theorem on revolving orbits,and letting the initial force tend to zero, deduce some of the possible orbits under the law of force $\mu _ { 1 } / \gamma ^ { 3 }$ Why cannot all the possible orbits be found in this way?

24.When the law of force is $( \mu / r ^ { 2 } ) \div ( v / r ^ { 3 } )$ ，show that the orbit is a conic whose major axis is rotating around the focus, and find its mean angular velocity in terms of the period if the conic is an ellipse.

25.Discuss the possible orbits under an inverse cube law of attraction. Show that there are six possible cases,and describe each one, sketching specimen curves.

26.A particle moves under an attraction $\mu \beta ^ { \frac { 3 } { 2 } } \gamma ^ { 5 }$ per unit mass toward a fixed point $o$ It is projected from a point $A$ distant $\pmb { \alpha }$ from $\boldsymbol { \vartheta }$ with velocity $\mathfrak { v }$ at right angles to OA. Show that the differential equation of the orbit is

$$
\left( { \frac { d r } { d \theta } } \right) ^ { 2 } = { \frac { r ^ { 2 } - a ^ { 2 } } { a ^ { 2 } v ^ { 2 } } } \left[ \left( v ^ { 2 } - { \frac { \mu } { 2 a ^ { 4 } } } \right) r ^ { 2 } - { \frac { \mu } { 2 a ^ { 2 } } } \right] .
$$

Show that in the special case when $v ^ { 2 } = \mu / 2 a ^ { 4 }$ the orbit is the circle on $o A$ as diameter,and that the time from $A$ to $o$ is

$$
\pi \frac { a ^ { 3 } } { \sqrt { 8 \mu } } .
$$

27.By considering the energy equation, investigate some possible orbits when the law of force is $\mu / \gamma ^ { 5 }$

28.A particle moves under the central force $- \mu \{ \hat { r } ^ { 2 } / \hat { r } \} \hat { \bar { \Sigma } }$ Solve the motion for position and time.

29.Show that if the central force is $\mu ( r / x ^ { 3 } )$ , the orbit is a conic; and show further that if the particle is projected at right angles to the radius vector at $\{ a , 0 \}$ with speed given by $2 v ^ { 2 } a = \mu$ theorbit isa circle.

30.A particle of mass m is projected from an apsis with the velocity from infinity under the attraction of a force

$$
\frac { m } { r ^ { 3 } } \log \frac { r } { a }
$$

directed to a center at a distance $a _ { i , }$ find the equation of the orbit de scribed.

31.A particle is projected at a distance $\pmb { \mathcal { a } }$ from the center of force with velocity $2 ( \sqrt { 3 ! } / a )$ at an angle $\pi / \frac { A } { 2 }$ with the radius vector, the force being $\mu _ { i } ^ { j } ( 3 / \gamma ^ { 3 } ) \dot { + }$ $( a ^ { 2 } / \gamma ^ { 5 } ) ]$ per unit mass. Determine the orbit, and show that the time to the center of force is

$$
\frac { \alpha ^ { 2 } } { \sqrt { 2 \mu } } \left( 2 - \frac { \pi } { 2 } \right) .
$$

32.A particle under the action of a central force $\mu [ ( r \div a ) / r ^ { 3 } ]$ is projected froman apsis at distance $\alpha$ with $\hat { \bf \Phi }$ speed that is proportionate to that in a circle at the same distance as $\ I : \sqrt { 2 }$ Show that the equation of the orbit is $r ( 2 + \theta ^ { 2 } ) = 2 a$ and that the particle will arrive at the origin in time

$$
\pi _ { \left\{ \sqrt [ ] { \frac { \alpha ^ { 3 } } { 8 \mu } } \right. } 
$$

33.Find the conservative law of force to the origin when the path is the cardioid $r = a ( 1 - \cos \theta )$ ;and show that if $\Sigma =$ is the force at the apsis and $\mathfrak { V }$ the speed, then $3 v ^ { 2 } = 4 a E ^ { \ast }$

34.Find the conservative laws of force under which a particle can describe the orbits (a） $r = 1 / c \theta$ and (b) $\gamma = e ^ { \theta }$

35.Find the conservative law of force under which a particle can describe the orbit $\boldsymbol { z } ^ { 2 } = a ^ { 2 } \cos { 2 \theta }$

36.Show that in order that it may be possible for $\hat { \mathbf { \Omega } }$ particle to describe a circular orbit under the attraction of $\hat { \mathbf { \Omega } }$ center of force situated at a given point within the circle,the law of force must be of the form

$$
\mu { \frac { \gamma } { \{ \gamma ^ { 2 } + b ^ { 2 } \} ^ { 3 } } } .
$$

Show that the group of possible circles in $\mathrm { ^ a }$ field of this form consists of the orbits described when the particle is projected from any point distant $\mathfrak { z }$ from the center of force in any direction with the velocity from infinity, and that the periodsvary as the cubes of the radii of the circles.

37.Find expressions for the central force when the orbit is an ellipse with the origin lying at the ends of the major and minor axes,respectively. What do they reduce to when the orbit becomesa circle?

38.Show that the curves

$$
a x + b y + c = x f \left( { \frac { y } { x } } \right) ,
$$

where $a , \vec { b } ,$ and $\mathfrak { c }$ are arbitrary constants and $f$ is a given function, can be described under the same law of central force to the origin.

39.If a conic is described under the central force $\mu ( r / p ^ { 3 } )$ given by Hamilton's theorem,show that the periodic time is

$$
2 \pi \sqrt { \frac { p _ { 0 } ^ { 3 } } { \mu } } ,
$$

where ${ \mathfrak { P o } } _ { \widehat { \mathfrak { a } } }$ is the perpendicular from the center of the conic on the polar of the center of force.
