# Chapter 6

# The Two-Body Problem

# 6.1The Motion of the Center of Mass

The case of a central orbit described under an attraction μ/r² has already been considered.In this chapter we shall investigate the motion of two bodies that are subject only to their mutual attraction. It is assumed that the bodies arespherically symmetrical and that Newton's law holds; then the bodies can be considered to be point masses. The methods used will be general, but most of the applications and much of the language will apply specifically to a planet traveling around the Sun.

Let the bodies have masses m1 and mz and, with respect to an inertial reference system, position vectors r1 and r2 at some instant.Also let

$$
{ \mathfrak { r } } = { \mathfrak { r } } _ { 1 } - { \mathfrak { r } } _ { 2 } .
$$

Instead of the Newtonian gravitational constant G, we shall substitute k²,for reasons which will become apparent soon. Then the equations of motion are

$$
m _ { 1 } \ddot { \mathtt { r } } _ { 1 } = - \mathtt { k } ^ { 2 } m _ { 1 } \mathtt { m } 2 \frac { \mathtt { m } _ { 1 } - \mathtt { r } _ { 2 } } { r ^ { 3 } }
$$

and

$$
m _ { 2 } \mathbf { \ddot { r } } _ { 2 } = - k ^ { 2 } \pi _ { 1 } \pi _ { 2 } \frac { \mathbf { r } _ { 2 } - \mathbf { \dot { r } _ { 1 } } } { r ^ { 3 } } .
$$

These are equivalent to six second-order differential equations, requiring twelve arbitrary constants for their complete solution.Adding (6.1.1） and (6.1.2),we get

$$
\Re _ { 1 } \tilde { \bar { \bf r } } _ { 1 } + \eta _ { 2 } \ddot { \bar { \bf r } } _ { 2 } = 0
$$

which can be integrated at once to give

$$
m _ { \bar { 1 } } { \bf r } _ { 1 } + m _ { 2 } { \bf r } _ { 2 } = { \bf a } t + { \bf b } ,
$$

where a and b are constant vectors, supplying six constants of integration and leaving six more to be found.Let

$$
m _ { 3 } + 3 n _ { 2 } = M
$$

and

$$
M { \bf { \overline { { r } } } } = m _ { 1 } { \bf { r } } _ { 1 } + m _ { 2 } { \bf { r } } _ { 2 } ,
$$

so that F is the center of mass of the two bodies. Then (6.1.3) shows that the center of mass moves in a straight line with constant speed.

In considering planetary motion,we are concerned with the orbit of one body about another without regard to their motion through space, so (6.1.3) does not provide any useful information. (It should be noted that the constants a and b can be changed at will by changing the inertial system of reference.) But the interpretation is important.One application is to the theory of double stars.Suppose that the observed paths of the components of a visual binary on the celestial sphere are the full lines in Figure 6.1. The center of mass must divide corresponding positions in a constant ratio,and since it moves in a straight line with constant speed,its path can be drawn and the ratio of the masses can be determined. In some cases only one star is observed, moving in a twisted path,and the existence of a companion body is inferred from this. Thecompanion of Sirius was first discovered in this way by Bessel,and ina few recent cases bodies of planetary dimensions have been suspected as invisible companions to optically single stars, through similar reasoning.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/0da08fd7e958122447f3f26de3c9269f223a4b262dcb7aa7620328b268f70cef.jpg)  
Figure 6.1 The orbits of Sirius A and B

# Problems

1.Find approximately the distance of the center of mass of the Sun and Jupiter from the center of the Sun,and the speed of the Sun's center in its orbit about this center of mass. (Ignore the effects of the other planets.)   
2.Answer problem 1, substituting the Earth and the Moon for the Sun and Jupiter.   
3.Two unequal bodies describe circular orbits around each other while their center of mass moves through space with speed v,with respect to some fixed reference system. Sketch the orbits in space with values of u giving paths with and without loops,and mark in relative positions at particular times.Find the relation between the orbit and v such that the space orbit has cusps.

# 6.2The Relative Motion

Take a new origin at the center of mass so that

$$
{ \mathfrak { s r } } _ { 2 } { \mathfrak { s r } } _ { 1 } \div { \mathfrak { n } } _ { 2 } { \mathfrak { r } } _ { 2 } = 0 .
$$

(6.1.1) can be written:

$$
\begin{array} { l } { { \vec { \bf r } _ { 1 } = - k ^ { 2 } \frac { m _ { 2 } { \bf r } _ { 1 } - m _ { 2 } { \bf r } _ { 2 } } { { \vec { r } } ^ { 3 } } } } \\ { ~ = - k ^ { 2 } \frac { m _ { 2 } { \bf r } _ { 1 } + m _ { 1 } { \bf r } _ { 1 } } { r ^ { 3 } } } \\ { ~ = - k ^ { 2 } M \frac { { \bf r } _ { 1 } } { r ^ { 3 } } . } \end{array}
$$

Similarly, (6.1.2) can be written:

$$
\vec { \mathtt { r } } _ { 2 } = - \mathtt { k } ^ { 2 } \vec { \mathtt { d } } \mathtt { f } \frac { \mathtt { r } _ { 2 } } { r ^ { 3 } } .
$$

Subtract (6.2.2) from (6.2.1),and put $\bar { \kappa } ^ { 2 } \bar { \mathcal { M } } = \mu$ Then

$$
\begin{array} { r } { \tilde { \mathfrak { r } } = - \mu \frac { \mathfrak { r } } { \mathfrak { r } ^ { 3 } } . } \end{array}
$$

This is equivalent to three second-order differential equations requiring six constants of integration for their complete solution； finding and interpreting these constants constitutes the kernel of the two-body problem.

$\mathfrak { r } \times \{ 6 . 2 . 3 \}$ gives

$$
\begin{array} { r } { \mathbf { \vec { \varepsilon } } \times \vec { \mathbf { \varepsilon } } \mathbf { \vec { \mathnormal { \mathbf { \mathnormal { \varepsilon } } } } } = \boldsymbol { \mathfrak { \boldsymbol { ⨏ } } } , } \end{array}
$$

or, integrating,

$$
\qquad \tt { r } \times \dot { \tt z } = \dot { \tt z } ,
$$

where h is a constant vector supplying three constants of integration. (6.2.4) shows that the angular momentum of the system is constant,and that the motion takes place in the plane

$$
\underline { { \hat { \mathbf { x } } } } \cdot \dot { \mathbf { a } } = \hat { \boldsymbol { \mathfrak { V } } } ,
$$

provided that $y _ { 2 } = 0$

Now take $\texttt { l x } \{ 6 . 2 . 3 \}$ ,using (6.2.4) on the right-hand side. We obtain

$$
{ \begin{array} { r l } & { \mathbf { h } \times { \ddot { \mathbf { r } } } = - { \frac { \mu } { r ^ { 3 } } } \mathbf { h } \times \mathbf { r } } \\ & { \qquad = - { \frac { \mu } { r ^ { 3 } } } ( \mathbf { r } \times { \dot { \mathbf { r } } } ) \times \mathbf { r } } \\ & { \qquad = - { \frac { \mu } { r ^ { 3 } } } \lbrace r ^ { 2 } { \dot { \bar { \mathbf { r } } } } - ( \mathbf { r } \cdot { \dot { \bar { \mathbf { r } } } } ) \mathbf { r } \rbrace } \\ & { \qquad = - { \frac { \mu } { r ^ { 3 } } } \lbrace r ^ { 2 } { \dot { \bar { \mathbf { r } } } } - ( r { \dot { \bar { \mathbf { r } } } } ) \mathbf { r } \rbrace } \end{array} }
$$

$$
{ \begin{array} { r l } & { = - \mu \left\{ { \frac { \vec { \mathbf { r } } } { r } } - { \frac { \mathbf { r } { \hat { \mathbf { r } } } } { r ^ { 2 } } } \right\} } \\ & { = - \mu { \frac { d } { d t } } \left( { \frac { \mathbf { r } } { r } } \right) } \\ & { = - \mu { \frac { d { \hat { \mathbf { r } } } } { d { \hat { \mathbf { r } } } } } . } \end{array} }
$$

Note that we have shown that

$$
\frac { d \hat { \mathbf { r } } } { d \hat { \mathbf { t } } } = \frac { \hat { \mathbf { \xi } } _ { 1 } } { r ^ { 3 } } \hat { \mathbf { \xi } } _ { 1 } \times \hat { \mathbf { \xi } } _ { 1 } ,
$$

so if h= O, then r is constant,and the motion is in a straight line through the origin. Integrating,we obtain

$$
\hat { \mathbf { n } } \times \dot { \mathbf { r } } = - \mu \hat { \mathbf { r } } - \mathbf { \mathbf { p } } .
$$

P is a constant vector and seems at first sight to supply the remaining three constants of integration.But its components are not independent, for h·(6.2.5) gives

$$
\begin{array} { r } { \mathbf { \nabla } \mathbf { P } \cdot \bar { \mathbf { a } } = \boldsymbol { \widehat { 0 } } , } \end{array}
$$

since i·h = 0. So P supplies only two arbitrary constants, leaving one more to be found.

Takingr·（6.2.5)we obtain

$$
\mathbf { r } \cdot ( \mathbf { h } \times \dot { \mathbf { r } } ) = - \mu \dot { \boldsymbol { r } } - \mathbf { P } \cdot \mathbf { r }
$$

$$
- \mathtt { h } \cdot ( \mathtt { r } \times \dot { \mathtt { x } } ) = - \mu \mathtt { r } - \mathtt { p } \cdot \mathtt { r }
$$

or

$$
\hbar ^ { 2 } = \mu \tau + \frac { \pi } { 2 } \cdot \tau
$$

or

$$
\frac { \hbar ^ { 2 } / \mu } { \tau } = \hat { \hat { \hat { \tau } } } + \frac { \mathbb { P } } { \mu } \cdot \hat { \hat { \hat { \tau } } } .
$$

Letf make an angle $\Im$ with $\mathfrak { P }$ ; then (6.2.7) is equivalent to

$$
\frac { \hbar ^ { 2 } / \mu } { \hbar ^ { 2 } } = \mathbb { i } + \frac { P } { \mu } \cos \mathfrak { v } .
$$

This is the standard equation of a conic with the origin at one focus and with

$$
\frac { \bar { \mathcal { P } } } { \mu } = \mathcal { e }
$$

and

$$
\frac { \hbar ^ { 2 } } { \mu } = p = \alpha \{ 1 - e ^ { 2 } \} .
$$

For a hyperbola the condition that r is nonnegative shows that v varies between ±cos-1(-1/e),so that only one branch can be described, the relevant branch being concave toward the origin.P isa vector along the major axis of the orbit pointing toward the position of closest approach between the two bodies;in the case of a planet going around the Sun, it points toward perihelion. The angle u is known as the true anomaly;it ismeasured in the direction in which the orbit is described, starting from perihelion. The symbol “u” almost always replaces the conventional “0” of polar coordinates in this context.

In some problems in astronomy it is necessary to consider motion under a repulsive force varying with the inverse square of the distance. For example the particles in a comet's tail may sufer this repulsion from the Sun, owing to radiation pressure,which easily outweighs the gravitational attraction of the Sun.In this case the formal theory is the same, but the sign of k²,or p, is changed, and the equation of the orbit is

$$
\begin{array} { r } { \frac { \mathfrak { P } } { \mathfrak { r } } = - \mathbb { 1 } + \mathcal { e } \cos \mathfrak { v } . } \end{array}
$$

Sincer is positive,e is greater than one,and the orbit is a branch of hyperbola. Also,v varies between ±cos-1(1/e),so that the branch described is convex toward the focus occupied by the Sun.

# Problems

1. Using great care, derive equations of motion for the two bodies, A and B, in the following forms:A with respect to Bas origin,B with respect to A,and each with respect to their center of mass. Show that the resulting orbits are all conics with the same eccentricity but different major axes,and find the relations between the major axes. Compare the angular momenta of A about B,B about A,and each with respect to their center of mass.   
2.A star A is initially at rest with respect to an inertial system of reference. Another star B is projected from infinity with a velocity that would carry it a distance c from A if there were no mutual attraction. Investigate the motion of the center of mass in the subsequent motion.If the relative orbit has eccentricity e,find the angle through which Bis deflected, having passed A and receded to infinity,and the velocity which A has then acquired.

# 6.3The Orbit in Time

The final constant of integration is found by integrating the equation that expresses the constancy of the modulus of the angular momentum. This can be written

$$
\tau ^ { 2 } \frac { d v } { d t } = h = \sqrt { \mathscr { P } \mathscr { k } } .
$$

The equation of the orbit can be written:

$$
r = { \frac { p } { 1 + e \cos v } }
$$

so that,eliminating $\Im ^ { * }$ ，we get

$$
\begin{array} { r } { \frac { \mathrm { \normalfont ~ d } v } { ( 1 \div \mathrm { \normalfont ~ e ~ c o s ~ v } ) ^ { 2 } } = \sqrt { \frac { \mu } { p ^ { 3 } } } \mathrm { \normalfont ~ d } t . } \end{array}
$$

This can be integrated for alle without much trouble, but except for e = 0 or 1.an extra substitution is needed to put the result in a useful form.

e= O gives a circular orbit described with constant speed. There is no difficulty in the formal theory here,and results can always be found by putting e= 0 in the corresponding formulas for elliptic motion, so that a separate discussion is not necessary.

For the parabolic orbit,e= 1. If q is the perihelion distance for an elliptic orbit,q=a(1-e)and p= q(1+e).Hence,for the parabolic orbit,p=2q and the equation can be written:

$$
\displaystyle r = { \mathfrak { q } } \sec ^ { 2 } { \frac { v } { 2 } } .
$$

Since the results will be applied to the motion of comets,M can be taken as the mass of the Sun,which will be considered as unit mass. Then we can put $\mu = k ^ { 2 }$ (6.3.3) can now be written as

$$
\sec ^ { 4 } { \frac { v } { 2 } } d v = { \frac { k { \sqrt { 2 } } } { q ^ { 3 / 2 } } } d t .
$$

Writing the left-hand side as

$$
\sec ^ { 2 } { \frac { v } { 2 } } \left( 1 + \tan ^ { 2 } { \frac { v } { 2 } } \right)
$$

we find that the equation can be integrated at once to give

$$
\frac { \ddagger } { 3 } \tan ^ { 3 } \frac { v } { 2 } + \tan \frac { v } { 2 } = \frac { k } { \sqrt { 2 q ^ { 3 } } } ( t - T ) .
$$

$T$ is the final constant of integration,giving the time when $v = \emptyset$ or when the comet passes through perihelion.

Consider the solution of (6.3.5) for $\mathfrak { V }$ when $\ddagger$ is given. Let

$$
\mathcal { F } ( v ) \equiv \frac { 1 } { 3 } \tan ^ { 3 } \frac { v } { 2 } + \tan \frac { v } { 2 } - \frac { k } { \sqrt { 2 q ^ { 3 } } } ( t - \mathcal { T } ) .
$$

Then varying only $\mathfrak { V }$

$$
\frac { d \mathcal { F } } { d v } \equiv \frac { 1 } { 2 } \sec ^ { 4 } \frac { v } { 2 }
$$

which is positive for all v. (6.3.5),being a cubic equation for tan(u/2）,must have at least one root; since F(u) is monotonic, increasing with v,there is only one root for any given value of t.

Now consider the elliptic orbit. Squaring equation (6.2.4) we get

$$
\begin{array} { r } { \hbar ^ { 2 } = \dot { \bar { \bf x } } ^ { 2 } \bar { \bf x } ^ { 2 } - \left( \bar { \bf x } \cdot \dot { \bar { \bf x } } \right) ^ { 2 } } \\ { = \dot { \bar { \bf x } } ^ { 2 } \bar { \bf x } ^ { 2 } - \left( \bar { \bf x } \dot { \bar { \bf x } } \right) ^ { 2 } . } \end{array}
$$

Substituting for h andr² (from the energy integral） for the elliptic orbit, we fnd

$$
\mu \left( { \frac { 2 } { r } } - { \frac { 1 } { a } } \right) r ^ { 2 } - r ^ { 2 } { \dot { r } } ^ { 2 } = \mu a ( 1 - e ^ { 2 } ) .
$$

Define $\Xi$ by

$$
r = a \{ 1 - e \cos { \mathcal { E } } \} .
$$

Eis called the eccentric anomaly. As v varies from O to 360°,E also varies from $\mathfrak { G }$ to $3 6 0 ^ { \circ }$ Differentiating （6.3.8) we get

$$
\dot { \vec { \tau } } = \alpha e \dot { \vec { \Xi } } \sin { \vec { \Xi } } \cdot
$$

Substituting into (6.3.7) and rearranging,we obtain, eventually,

$$
\frac { a ^ { 3 } } { \mu } \dot { \mathcal { E } } ^ { 2 } ( 1 - e \cos \mathcal { E } ) ^ { 2 } = 1 .
$$

Now the orbit is described so that $d E / d t$ is positive, so that

$$
\acute { d t } = \sqrt { \frac { a ^ { 3 } } { \mu } } ( 1 - e \cos E ) \acute { d \mathcal { E } } .
$$

Integrating over a complete revolution, we get for the period

$$
P = 2 \pi \sqrt { \frac { a ^ { 3 } } { \mu } } ,
$$

the result obtained in Chapter 4. The mean motion, $\scriptstyle \gamma _ { t }$ ,is given by

$$
\begin{array} { c } { { n = { \frac { 2 \pi } { P } } } } \\ { { = { \sqrt { \frac { \mu } { a ^ { 3 } } } } . } } \end{array}
$$

$\mathfrak { X }$ is measured in radians per unit time. If $\mathcal { P }$ is expressed in mean solar days, n is called the mean daily motion. (6.3.9) can now be written:

$$
\pi d t = \left( { \tt i } - e \cos { \mathscr { E } } \right) d { \mathscr { E } }
$$

which can be integrated immediately to give

$$
\Omega ( \vec { t } - \vec { \mathcal { L } } ) = \Xi - e \sin \vec { \Xi } .
$$

T, the time of perihelion passage, is the final constant of integration for the elliptic orbit. (6.3.12)is Kepler's equation; it is often written in the form:

$$
M = E - e \sin \vec { E } ,
$$

where $\pmb { \lambda }$ is the mean anomaly, defined by

$$
M = n \{ t - T \} .
$$

A similar equation can be found for hyperbolic motion.In this case we make the substitutions

$$
\tau = a \{ 1 - e \cosh \frac { \ddagger } { \varepsilon } \}
$$

and

$$
\nu = \sqrt { - \frac { \ddot { \mu } } { a ^ { 3 } } }
$$

and we find

$$
\nu \left( t - T \right) = e \sin { \hat { F } } - \vec { F } .
$$

There is a simple but important derivation of Kepler's equation which explains the geometrical significance of $E$ The ellipse can be derived from the orthogonal projection of a circle called the eccentric circle. In the notation of Figure 6.2, the ellipse can be regarded as the locus of points $\mathcal { P }$ such that $P D / Q D$ is constant,the value of the constant being the ratio of the minor to major axes of the ellipse.Here $Q$ is any point on the eccentric circle,and $Q D$ is perpendicular to the diameter $A C B ,$ which is also the major axis of the ellipse, center $C$

Let $\pmb { \mathcal { F } }$ be the relevant focus; then $\xi P = \uparrow$ and $\angle A F P = 1 3$ Let $\angle Q C A = E$ ： then

$$
\begin{array} { r l } & { r ^ { 2 } = P D ^ { 2 } + D F ^ { 2 } } \\ & { \quad = \left( \frac { b } { a } Q D \right) ^ { 2 } + ( C F - C D ) ^ { 2 } } \\ & { \quad = \left( \frac { b } { a } \triangleleft \sin { E } \right) ^ { 2 } + ( a e - a \cos { E } ) ^ { 2 } } \\ & { \quad = a ^ { 2 } ( 1 - e ^ { 2 } ) \sin ^ { 2 } { E } + a ^ { 2 } ( e - \cos { E } ) ^ { 2 } \quad \mathrm { ~ [ s i n c e ~ } b ^ { 2 } = a ^ { 2 } ( 1 - e ^ { 2 } ) ] } \\ & { \quad = a ^ { 2 } ( 1 - e \cos { E } ) ^ { 2 } , } \end{array}
$$

showing that $E$ is defined as before.

The coordinates of $\mathcal { P }$ with respect to axes along the major and minor axes of the ellipse (the origin being at the center of the ellipse) are

$$
\left. \begin{array} { l } { { \ x { x } = \alpha \cos { E } , } } \\ { { y = b \sin { E } = a \sqrt { 1 - e ^ { 2 } } \sin { E } . } } \\ { { \ x { \pmod { E } } } } \end{array} \right\}
$$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/a98e7474d85165dd882fc2a5c69f67c56a7fcda32dd3191290fdd6d08b51ca93.jpg)  
Figure 6.2

As the elliptic orbit is described by $\mathbf { \Sigma } _ { p }$ we have, by the law of areas,

$$
{ \begin{array} { r } { { \frac { \tilde { M } } { 2 \pi } } = { \frac { \mathrm { a r e a ~ o f ~ s e c t o r ~ } A F P } { \mathrm { a r e a ~ o f ~ e l l i p s e } } } } \\ { = { \frac { \mathrm { a r e a ~ o f ~ s e c t o r ~ } A F Q } { \mathrm { a r e a ~ o f ~ c i r c l e } } } } \end{array} }
$$

$$
\begin{array} { r l } & { \operatorname { A r e a s } A F Q = A C Q - F C Q } \\ & { \qquad = \frac { 1 } { 2 } a ^ { 2 } \mathcal { E } - \frac { 1 } { 2 } a e ( a \sin \mathcal { E } ) , } \end{array}
$$

so we have

$$
\begin{array} { r } { \frac { \vec { M } } { 2 \pi } = \frac { a ^ { 2 } ( \vec { E } - e \sin \vec { E } ) } { 2 \pi a ^ { 2 } } } \end{array}
$$

or

$$
\mathbb { M } = \mathbb { E } - e \sin \bar { E } .
$$

Methods for the solution of Kepler's equation will be described later.

The equation of the elliptic orbit can be written:

Hence

$$
r = { \frac { a ( 1 - e ^ { 2 } ) } { 1 + e \cos v } } .
$$

$$
1 - e \cos \mathcal { E } = \frac { 1 - e ^ { 2 } } { \frac { 1 + e \cos \mathfrak { v } } { 1 + e \cos \mathfrak { v } } }
$$

S0

$$
\cos v = { \frac { \cos { \mathcal { E } } - e } { { \frac { 1 } { 2 } } - e \cos { \mathcal { E } } } } ,
$$

and

$$
\sin v = { \frac { \sqrt { 1 - e ^ { 2 } } \sin { \mathcal { E } } } { 1 - e \cos { \mathcal { E } } } } .
$$

Now

$$
\begin{array} { c } { \tan ^ { 2 } \displaystyle \frac { v } { 2 } = \displaystyle \frac { 1 - \cos v } { 1 + \cos v } } \\ { = \displaystyle \frac { ( 1 + e ) ( 1 - \cos E ) } { ( 1 - e ) ( 1 + \cos E ) } } \\ { = \displaystyle \frac { 1 + e } { 1 - e } \tan ^ { 2 } \displaystyle \frac { E } { 2 } . } \end{array}
$$

So

心

$$
\tan { \frac { v } { 2 } } = { \sqrt { \frac { 1 + e } { 1 - e } } } \tan { \frac { \mathcal { E } } { 2 } } .
$$

Some other formulas will now be derived for later use. Combining the differential form (6.3.12)with (6.3.8),we have

$$
\frac { d \mathcal { E } } { d t } = \frac { n a } { r } .
$$

We already know that

$$
\tau ^ { 2 } \frac { { \dot { d } } v } { { \dot { d } } \dot { \xi } } = h .
$$

Differentiating the equation of the orbit (6.2.8) with respect to the time and simplifying,we find

$$
\frac { d \mathfrak { s } } { d \mathfrak { t } } = \frac { e \mathfrak { L } } { h } \sin \mathfrak { s } .
$$

Similarly, from the derivative of (6.3.8),we find

$$
r ^ { \frac { d \vec { x } } { d \vec { x } } } = e \hbar a ^ { 2 } \sin \vec { E } .
$$

Never forget that $\mathbf { y } \cdot \mathbf { v } = \mathbf { y } \cdot \dot { \mathbf { r } } = r \dot { \mathbf { y } } ^ { * }$

It is often convenient to work in a reference system with the origin at the attracting focus, the X-axis pointing toward pericenter and the Y-axis in the direction for which the true anomaly is $9 0 ^ { \circ }$ ；then the Z-axis is parallel to the angular momentum. This will be referred to below as the “orbital reference system.”Using (6.3.16),we have

$$
\begin{array} { l } { X = \bar { r } \cos v = a ( \cos E - e ) , } \\ { \dot { Y } = \bar { r } \sin v = a \sqrt { 1 - e ^ { 2 } } \sin E . } \end{array} \bigg ]
$$

Differentiating these with respect to the time, we can then derive the expressions for the components of velocity:

$$
\begin{array} { l } { { \displaystyle { \dot { X } } = - \frac { n a ^ { 2 } } { r } \sin { E } , } } \\ { { \displaystyle { \dot { Y } } = \frac { n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } { r } \cos { E } . } } \end{array}
$$

Toillustrate the interpretation of the three anomalies,consider the Moon's libration in longitude. The period of rotation of the Moon on its axis is the same as the period of its revolution around the Earth (one sidereal month).If the Moonrevolved around the Earth in a circular orbit,then one half of its surface would be constantly pointing toward the Earth,and we would see no part of the other half. Now the Moon moves in an elliptic orbit with the Earth, $E$ as a focus. Let the Moon have center O,and let P be that point on the surface of the Moon such that O,P,and E are collinear at perigee,with P visible from the Earth.At any time OPwill make an angle with the major axis of the ellipse that is equal to the mean anomaly M of the Moon in its orbit,while the angle between OE and the major axis is the true anomaly v. Assuming for the moment that the axis of rotation of the Moon is perpendicular to the plane of the orbit,an observer on the Earth will see Pas being displaced from the center ofthe Moon's disk bya longitude $\{ \mathcal { M } - v \}$ ,orhe will see this extra longitude at the Moon's limb compared with what was observed at perigee. This is known as the libration in longitude of the Moon. To investigate its fullest extent,we find the maximum value of $\{ \mathbb { M } - \mathfrak { v } \}$ ；this occurs when

$$
\frac { \dot { a } ( \tilde { M } - v ) } { \dot { a } t } = 0 ,
$$

$$
\frac { d v } { d t } = n .
$$

From the angular momentum equation,the value of $\Im ^ { * }$ at this point is found from

$$
\gamma ^ { 2 } = { \frac { \vec { n } } { n } } ,
$$

and,substituting for $⨏ _ { \ b { \mathscr { k } } }$ and $\mathfrak { r }$ ,we find

$$
\mathfrak { r } = \mathfrak { a } ( 1 - { e } ^ { 2 } ) ^ { 1 / 4 } .
$$

The appropriate value of $\mathfrak { V }$ can then be found from the equation of the orbit. To find $\vec { \pmb { \mathscr { H } } }$ it is necessary first to find $\mathbf { \widehat { E } }$ from (6.3.8)，say,and then to solve Kepler's equation for $\vec { i } \vec { i }$ ，

(For the Moon, three other typesof libration must be considered.The axis of rotation is not perpendicular to the plane of its orbit, so an observer in the northern hemisphere of the Earth will sometimes see “over” the Moon's north pole, and sometimes “under” its south pole; this is libration in latitude. While looking at the Moon,an observer will be moving in space owing to the Earth's rotation; this will cause him to see a slightly different “half” at diferent times; this is diurnal libration. Also, because of its nonspherical shape, the Moon oscillates slightly；this effect,which is very small, leads to physical libration. The other three types of libration are classed as optical librations.)

# Problems

1. A planet travels around the Sun in an elliptic orbit and rotates on an axis perpendicular to the plane of its orbit with a period equal to the period of the orbit. Find the maximum libration in longitude and where in the orbit this is achieved.Show that if $e ^ { 2 }$ isneglected in the final answer,the maximum libration expressed in radians is 2e,and that the time interval between perihelion and the following position of maximum libration is

$$
\frac { 1 } { 4 } - \frac { 5 e } { 8 \pi }
$$

times the period.

2.Show that if the square of the eccentricity of the Moon's orbit is neglected, then the Moon will always turn the same face toward the empty focus.

3.If  is the angle between the direction of a planet's motion and the direction perpendicular to the radius vector,show that

$$
\tan \psi = \frac { e \sin \mathcal { E } } { \sqrt { 1 - e ^ { 2 } } } .
$$

4.Aplanet travels around the Sun in an ellipse of eccentricity e.Find the proportion of the time spent near the Sun between the ends of the minor axis to the total period.

5.Find the time during which a parabolic comet is inside the ends of the latusrectum of its path,in terms of $q$ ,itsperihelion distance. If $q = \hat { \infty } \times \hat { \pm } \hat { \mathfrak { V } } ^ { 7 }$ miles,show that the time is about 114 days.

6.The perihelion distance of a parabolic comet,measured in astronomical units,is'g (less than one).Assuming that the Earth's orbit is circular and that the comet moves in the ecliptic,show that if $\ddagger$ (measured in sidereal years) is the interval duringwhich the comet iswithin the Earth's orbit, then

$$
\dot { \iota } = \frac { \mathbb { i } } { 3 \pi } ( 1 + 2 q ) \sqrt { 2 - 2 q } .
$$

7.A planet describing a circular orbit receives a small impulse in the direction of its motion.At any future time it is at P,whereas if it had not received the impulse,it would have been $P ^ { j }$ .Show that although the

path of P is never far from the original circle, the length of PP' does not remain small. Discuss the case where the small impulse is radial.

8.Show that

$$
\begin{array} { r } { \sin \displaystyle \frac { 1 } { 2 } ( v - E ) = \sqrt { \frac { r } { p } } \sin \displaystyle \frac { 1 } { 2 } \phi \sin v , } \\ { \sin \displaystyle \frac { 1 } { 2 } ( v + E ) = \sqrt { \frac { r } { p } } \cos \displaystyle \frac { 1 } { 2 } \phi \sin v , } \end{array}
$$

where $e = s i \gamma _ { } \phi$ How would these formulas be useful in finding $E$ when $\mathfrak { v }$ and $\pmb { \mathcal { T } }$ are given and $\mathcal { C }$ is small?

9. Find the average value of $\mathfrak { F }$ in an elliptic orbit, taking the true anomaly as the independent variable. (You can avoid the integration of

$$
\int \frac { d v } { 1 + e \cos v }
$$

by changing the variable to $E$ ）

10.Find the average values of the following quantities in an elliptic orbit, taking the time as the independent variable:

$( \mathrm { a } ) \ r ; \quad ( \mathrm { b } ) \ d r / d t ; \quad ( \mathrm { c } ) \ 1 / r ; \quad ( \mathrm { d } ) \ d v / d t ;$ (e) the potential energy；(f） the kinetic energy;

For the last, consider only half the orbit from perihelion to aphelion.

11.Derive the following average values for the elliptic orbit,taking the time as the independent variable:

$$
{ \begin{array} { r l } & { \cdot \left( { \frac { a } { r } } \right) ^ { 3 } = ( 1 - e ^ { 2 } ) ^ { - 3 / 2 } ; } \\ & { \cdot \left( { \frac { a } { r } } \right) ^ { 4 } \cos v = e ( 1 - e ^ { 2 } ) ^ { - 5 / 2 } ; } \\ & { \cdot \left( { \frac { a } { r } } \right) ^ { 3 } = \left( 1 + { \frac { 1 } { 2 } } e ^ { 2 } \right) ( 1 - e ^ { 2 } ) ^ { - 5 / 2 } ; } \\ & { \cdot \left( { \frac { a } { r } } \right) ^ { 5 } = \left( 1 + { \frac { 3 } { 2 } } e ^ { 2 } \right) ( 1 - e ^ { 2 } ) ^ { - 7 / 2 } ; } \\ & { \cdot \left( { \frac { a } { r } } \right) ^ { 5 } \cos 2 v = { \frac { 3 } { 4 } } e ^ { 2 } ( 1 ^ { - } e ^ { 2 } ) ^ { - 7 / 2 } . } \end{array} }
$$

12.Show that the amount of heat received from the Sun by the planets,per unit area,in unit time,is on the average proportional to the reciprocals of the products of the major and minor axes of the orbits.

13.Find formulas for v in terms of F for the hyperbolic orbit. Find, for the hyperbolic orbit, those mean values mentioned above which are finite.

14.An ICBM is fired at an elevation of 45° with initial speed 5km/sec from a point on a flat Earth (constant g). Find the range and the time of flight.Now,taking into account the shape of the Earth and its rotation, let the ICBM be launched with the same elevation and speed, due east from latitude 45o.Find the range and time offlight.

What effect would air resistance have on your results?

(Use the energy and angular momentum to find a and e for the orbit.)

15.A rocket is Iaunched from latitude 45N over the north pole. If it strikes the point of launching twelve sidereal hours later, find the initial conditions of launching.

# 6.4Some Properties of the Motion

Taking $h \times ( 6 . 2 . 5 )$ we obtain

$$
\hbar ^ { 2 } \dot { \mathfrak { r } } = \mu \dot { \mathfrak { s } } + \hat { \mathfrak { r } } + \hat { \mathfrak { n } } \times \mathfrak { P } .
$$

(6.4.1) shows that the velocity at any point is the sum of two vectors of constant modulus.One,of length μ/h,is perpendicular to f,and the other,of length $e ( \mu / \hbar )$ ,isperpendicular to the major axis of the orbit.It follows that the hodograph of the motion is a circle of radius $\mu / h$ with center $\hat { \mathbf { a } } _ { s }$ distance $e \{ \mu / \hbar \}$ from the origin.The hodograph for elliptic motion is sketched in Figure $6 . 3 a ,$ with the corresponding position in the orbit shown in Figure $6 . 3 \bar { \mathfrak { z } }$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/c786fdf13d7be59b7d2143ad54ac4e5b1d0e08ed1b826391cf02cd57901f373a.jpg)  
Figure 6.3

f $Q$ is any point on the circle, $0 \textcircled { < } 2$ represents the velocity in the orbit at one extremity of the focal chord that is at right angles to $\sum \limits _ { \alpha }$ OPgives the velocity at perihelion.

where $C = - \{ \mu / 2 a \}$ The speed in $^ \mathrm { a }$ circular orbit of radius $\mathcal { T }$ is given by

Figures 6.4 and 6.5 are the hodographs of parabolic and hyperbolic motion. For the hyperbolic case, let $O A$ and $O B$ be tangents to the circle. Then the angles COA and COB are each equal to sin-1(1/e) and the angles PCA and $P C B$ are each equal to $\cos ^ { - 1 } \{ - 1 / e \}$ ; so only points on the arc $A P B$ are permissible. $O A$ and $o B$ are parallel to the asymptotes.The remaining arc would correspond to points on the branch of the hyperbola that is convex toward the center of force;it gives the hodograph for motion under an inverse square law of repulsion.

From Chapter 4 the energy integral is

$$
\begin{array} { r } { \bar { \mathbb { V } } ^ { 2 } = \hat { 2 } \frac { \mathcal { U } } { \mathfrak { F } } \pm \hat { 2 } C , } \end{array}
$$

$$
\begin{array} { r } { \mathbb { V } _ { c } ^ { 2 } = \frac { \mathcal { L } } { \mathfrak { r } } ; } \end{array}
$$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/8b7a5d79f0f71a26fe47c53cd672c203ca35197b2bd6c6499cf0a79d28aa0870.jpg)  
Figure 6.4 (left) and 6.5 (right）

and in a parabolic orbit by

$$
\begin{array} { r } { V _ { \mathfrak { p } } ^ { 2 } = 2 \frac { \mu } { \mathfrak { r } ^ { \ast } } . } \end{array}
$$

Suppose m1 to be projected from & point distant r from m2 with speed V relative to m2. There are three possibilities:

$$
V ^ { 2 } < , = , \mathrm { o r } > 2 \frac { \mu } { r } ,
$$

giving elliptic,parabolic, or hyperbolic orbits. The parabolic speed is the velocity of escape. It should be remembered that the major axis,and therefore the period of the resulting orbit,depends only on r and V and not on the direction of projection. Also,a particle with speed Vp will be moving ina parabolic orbit regardless of the direction of its motion. When $\pmb { \mathcal { T } } _ { \pmb { \mathcal { L } } \pmb { \mathcal { L } } } ^ { \pmb { \mathcal { L } } }$ is distant $\pmb { \mathscr { T } } _ { \vec { \updownarrow } }$ from $3 3 2 2$ ，the relative speed will be given by

$$
V _ { 1 } ^ { 2 } = V ^ { 2 } + 2 \mu \left( { \frac { 1 } { r _ { 1 } } } - { \frac { 1 } { r } } \right) .
$$

Consider (6.3.10). Rearranging $\ddag \ddag$ ,we find

$$
\frac { P ^ { 2 } } { \alpha ^ { 3 } } ( m _ { 1 } + \mathfrak { n } _ { 2 } ) = \frac { 4 \pi ^ { 2 } } { k ^ { 2 } } .
$$

This is the amended form of Kepler's third law. For any planet in the solar system $( m _ { 1 } + m _ { 2 } )$ is very nearly equal to the mass of the Sun, so that $\rho ^ { 2 } / a ^ { 3 }$ is effectively constant. The right-hand side of (6.4.2) is $\texttt { a }$ constant, the value of which depends on the units chosen.Provided consistent units are used, the quantity on the left-hand side will be the same for any pair of bodies.

The law provides a useful method for finding the masses of celestial bodies. For instance, if $P$ and $\pmb { \mathcal { L } }$ are known for a double star,then the sum of the masses of the components can be found.In some cases this can be combined with the observations described in Section 6.1, giving the ratio of the masses, and then the individual masses can be found. Alternatively, if the sum of the masses is assumed (twice the mass of the Sun may bea good value),or inferred from spectroscopic observation,and the orbit of one star about the other can be observed, then α can be calculated in terms of some definite unit of length. But the angle that a subtends at the distance of the Sun from the double star is observed; hence the distance of the system can be calculated in terms of the astronomical orbit: this is known as the dynamical parallax of the binary system.

Suppose a planet of mass $\mathfrak { P e }$ has a satellite whose mass is very small compared with ${ \mathfrak { M } } _ { \mathfrak { P } }$ and which has an orbit about the planet with semimajor axis $\mathcal { Q } _ { \mathfrak { I } }$ and period $P _ { 3 }$ If the corresponding values for the orbit of the planet around the Sun are $a _ { 2 }$ and $P _ { 2 }$ , and the mass of the Sun, $\pmb { \mathcal { M } }$ , is much greater than $\Im { \mathfrak { s a } } _ { \mathfrak { P } }$ then we can apply (6.4.2) to the satellite going around the planet and then to the planet going around the Sun, when we find:

$$
\frac { P _ { 1 } ^ { 2 } } { a _ { \pm } ^ { 3 } } \mathfrak { m } _ { \mathcal { P } } = \frac { \bar { P } _ { 2 } ^ { 2 } } { a _ { \pm } ^ { 3 } } \bar { M } .
$$

So.the mass of the planet can be measured in units of the mass of the Sun. If is measured in sidereal years, $\pmb { \alpha }$ inastronomical units, and masses in terms of the Sun's mass,then each side of (6.4.3) must be equal to one.

# Problems

1.Given that the eccentricity of the Earth's orbit is O.01673 and the astronomical unit is $1 . 4 9 5 \times 1 0 ^ { 8 } ~ \mathrm { k m } .$ find the perihelion and aphelion distances and the length of the semiminor axis of the orbit. Find also the speeds of the Earth at perihelion,aphelion, the ends of the minor axis,and the ends of the latus rectum.

2.Assuming that the Earth's orbit is circular and that meteors approach the Sun in elliptic and parabolic orbits,between what limits of relative speed will they hit the Earth's atmosphere,if the Earth's attraction is neglected? What effects on these limits will result if the eccentricity of the Earth's orbit is taken into account？

3.Two planets of equal mass moving in opposite directions collide and coalesce at a distance d from the Sun. At the time of their collision one planet is at perihelion and the other at aphelion,and both orbits have the same eccentricity e. Find the major axis of the orbit of the joint mass.

4.A comet moving in a parabolic orbit with perihelion distance $q$ collides, when distant r from the Sun,and combines with a body of equal mass that is at rest before the colision. Find the major axis and eccentricity of the orbit of the combined mass.

5. At a certain point in an elliptic orbit under the force $\mu / r ^ { 2 }$ the value of $\beta$ is changed by a small amount. If the eccentricities of the former and new orbits are the same, show that the point is at an extremity of the minor axis.

6.The Newtonian gravitation constant $G$ is found from terrestrial experiments to be $\phantom { + } 6 . 6 7 \updownarrow \times 1 0 ^ { - 8 }$ cgs units. Using data for the Earth's orbit, find the mass of the Sun.

If $g = 9 8 \hat { \mathfrak { z } }$ cgs units,and the radius of the Earth is 6380 km,find the mass of the Earth.

7.Assuming that the Moon's orbit about the Earth is circular,with radius 60 times the radius of the Earth and with period 27d 8h,show that this information together with values for $\mathfrak { g }$ and the Earth's radius given above furnishes one check for Newton's law of gravitation.

8.Show that the greatest value of dr/dt in an eliptic orbit occurs at the ends of the latus rectum,and find this value for a planet whose orbit has semimajor axis α and eccentricity e. What is the value for the Earth's orbit？

9.An artificial satelite is launched vertically upward with initial speed v. When the vertical speed becomes zero, the satelite is given a transverse speed u. Find the resulting orbit in terms of u and v.

10. If an artificial satellite starts off in an elliptic orbit such that atmospheric drag occurs only at perigee, describe qualitatively how the orbit will change，showing that it will eventually become circular. What is the radius of the circle?

Once the orbit has become circular, suppose that during one revolution it loses a small amount of energy, owing to atmospheric friction, but that the orbit remains circular,but with different radius.How will the energy lost be distributed between the kinetic and potential energies of the satellite?

11. When a periodic comet is at its greatest distance from the Sun,its speed receives a small increment $\delta v$ Show that the comet's least distance from the Sun will be increased by the quantity

$$
4 \delta v _ { \uparrow } \sqrt { \frac { a ^ { 3 } } { \mu } } \sqrt { \frac { 1 - e } { \frac { 1 + e } { \frac { 1 } { \mu } } } } .
$$

12.A particle is to be projected with given speed from a given point under a central Newtonian force,so that the line of apsides shall make a given angle $\boldsymbol { \theta }$ with the initial radiusvector.Show that there are two directions of projection making angles with this radius vector,whose sum is

$$
\left( \theta + { \frac { \pi } { 2 } } \right) \quad \Phi \pm \quad \left( \theta + 3 { \frac { \pi } { 2 } } \right) .
$$

13.If $P O P ^ { \prime }$ is a focal chord of an elliptic path described around the Sun, show that the time from $\mathcal { P }$ to $P ^ { \prime }$ through perihelion is equal to the time of falling toward the Sun from a distance $2 a$ to a distance $a \{ 1 \div \cos \alpha \}$ where $\alpha = 2 \pi - \left( E - E ^ { \prime \prime } \right)$ and $\Xi$ and $E ^ { t }$ are the eccentric anomalies at $\mathcal { P }$ and $P ^ { j }$

14.Two stars of masses $\Im \Im _ { \perp }$ and $\yen 12$ move under their mutual gravitation. Show that,if when $\mathcal { W } _ { 1 }$ is at rest,the velocity of ${ \tt R e } _ { 2 }$ isat right angles to the line joining the two masses and equal to

$$
\sqrt { \frac { G ( m _ { 1 } + m _ { 2 } ) } { d } }
$$

where $d$ is the distance of the two bodies,then the path of $\mathscr { T } \mathscr { V } _ { \Sigma }$ in space isa succession of cycloids,the body coming to rest at $\gtrdot$ cusp at equal intervals of time.

15.If particles are projected from a given point in the solar system with a given speed but in different directions,find the loci of the following points in their orbits: (a) the other focus; (b) perihelion; (c) aphelion; (d） the center of the ellipse; (e) the ends of the minor axis. (It is assumed that the speed of projection is less than the velocity of escape from the solar system.)

16.If the particles are now projected from a given point in the same direction but with different speeds, find the loci of the same points considered in problem 15.

17.Show that in eliptic motion under Newton's law,the projections on the external bisector of two radii, of the velocities corresponding to these radii, are equal. Show also that the sum of the projections on the inner bisector is equal to the projection of a line constant in magnitude and direction.

18.Show that if a particle describes an ellipse under a force to a focus, the speed at the mean distance from the center of force is a mean proportional between the speeds at the ends of any diameter.

19.The components of masses $\mathfrak { W } _ { \mathfrak { I } }$ and $\eta _ { 2 }$ forming a double star,describe ellptic orbits around each other in period $\mathcal { P }$ their greatest and least distances apart being $\mathcal { D } _ { \mathfrak { I } }$ and $\pmb { \mathscr { D } _ { 2 } }$ .Show that the rotational momentum of the orbital motion of the system is

$$
\frac { \pi } { \mathcal { P } } \cdot \frac { m _ { 1 } m _ { 2 } } { m _ { 1 } + m _ { 2 } } \sqrt { D _ { 1 } D _ { 2 } } ( \mathcal { D } _ { 1 } \div D _ { 2 } ) .
$$

20.Two stars of masses $\pmb { \mathcal { M } }$ and $\scriptstyle { \widehat { \mathfrak { s a } } }$ are initially at a great distance apart. M is at rest and $\mathcal { W } _ { \ell }$ has a velocity in $\pmb { \ V }$ in $\gtrdot$ direction that passes $1 1 1$ ata perpendicular distance $\boldsymbol { \mathfrak { T } }$ Show that after the encounter, when $_ { 3 2 }$ has again receded to a great distance, $\pmb { \hat { \hat { \mathbf { f } } } } \pmb { \hat { \mathbf { f } } }$ will have acquired the velocity

$$
2 V G m \{ G ^ { 2 } ( M + m ) ^ { 2 } + \sigma ^ { 2 } \gamma ^ { 4 } \} ^ { - 1 / 2 } ,
$$

and find its direction.

21.Two stars of masses $\mathbb { M }$ and m are a great distance apart and move toward oneanother with relative velocity $\mathbb { V }$ ， $\pmb { \sigma }$ being the perpendicular distance between the directions of their velocities,which are parallel. Show that the least distance between them during the subsequent motion is given by

$$
\frac { 1 } { d } = \frac { G ( M + m ) } { \sigma ^ { 2 } V ^ { 2 } } \left\{ 1 + \left[ 1 + \frac { \sigma ^ { 2 } V ^ { 4 } } { G ^ { 2 } ( M + m ) ^ { 2 } } \right] ^ { 1 / 2 } \right\} .
$$

22.For the two stars of problem 21, let $\phi$ be the angle through which the relative velocity is turned by the complete encounter; show that

$$
\tan { \frac { 1 } { 2 } } \phi = \frac { G ( M + m ) } { \sigma ^ { \frac { 1 } { 2 } } } \cdot
$$


<!-- chunk 0003: pages 81-120 -->
Show further that if the two stars have equal masses and one is initially at rest, the final speeds are

$$
V \cos { \frac { 1 } { 2 } } \phi \quad { \mathrm { a a d } } \quad V \sin { \frac { 1 } { 2 } } \phi .
$$

23.A comet of negligible mass is traveling initially ina parabolic orbit around the Sun.The orbit is disturbed bya close approach to Jupiter.Assume that during this approach,Jupiter is moving ina straight line and that the comet is subject only to Jupiter's gravitational attraction；also assume that the comet approaches Jupiter in either of the two directions tangential to Jupiter's orbital motion around the Sun.Investigate the conditions under which the velocity of the comet with respect to the Sun will be increased or decreased by the encounter.

24.A foreign body of negligible mass,travelingat velocity $\pmb { \ V }$ relative to the Sun's motion,penetrates into the solar system and approaches to a distance $D$ from the Sun before receding again.Show that when it has left the system, its direction of relative motion is deflected through an angle $\psi$ given by

$$
\csc \frac { \psi } { 2 } = \pm + \frac { { \mathcal { D } } V ^ { 2 } } { { \mathcal { D } } _ { 0 } { \mathcal { Y } } _ { 0 } ^ { 2 } } ,
$$

where $\gamma _ { 0 }$ is the orbital velocity of a planet revolving in a circular orbit at distance $D _ { 0 }$ .Calculate the deflection roughly when $\mathbb { V }$ is $2 8 \mathrm { k m } / \mathrm { s e c }$ ,and $\pmb { D }$ is 0.7 of an astronomical unit, the distance of Venus from the Sun.

25.A particle is projected a great distance from a star of mass $\tilde { \hat { \beta } } \tilde { \hat { \beta } }$ and radius ${ \mathfrak { r } } _ { 0 }$ with velocity $V$ ,such that,neglecting the attraction of the star,it would approach the star at a minimum distance $\sigma$ Write down the equations of energy and angular momentum, and find $\sigma$ such that the particle will just graze the star.

A star of radius $\mathfrak { r } _ { \mathfrak { Q } }$ moves through a cloud of particles,of density $\boldsymbol { \beta }$ particles per unit volume, with velocity $\pmb { \ V }$ relative to the cloud. Assuming that the particles have no relative velocities (or that the cloud has zero temperature), particles within a tunnel of radius $\boldsymbol { \mathscr { \sigma } }$ will be accreted by the star.Show that the rate of accretion is

$$
{ \dot { A } } = \pi { \dot { \gamma } } _ { 0 } ^ { 2 } \rho _ { 0 } \left( V \div { \frac { 2 { \dot { \mathcal { M } } } G } { r _ { 0 } V } } \right) 
$$

By considering probable figures for the Sun,show that the frst term in the parentheses can usually be neglected. (This is Eddington's formula for accretion.)

26.In another theory of accretion (due to Lyttelton) it is assumed that all particles collide on an axis through the center of the star, parallel to its

direction of motion,and that the collisions are nonelastic, completely annuling the components of velocity perpendicular to this axis, but leaving the components along the axis unchanged.

Show that the component of velocity along this axis is V,and find the condition for a particle, after its collision, to fallinto the star. Hence show thatall particleswithin a tunnel of radius

$$
\sigma = { \frac { 2 M G } { \ Y ^ { 2 } } }
$$

will be swept up,so that the rate of accretion is

$$
A = \frac { 4 \pi M ^ { 2 } G ^ { 2 } \rho _ { 0 } } { V ^ { 3 } } .
$$

27. Find the mass of Jupiter compared with that of the Sun from the following data:

Period of Ganymede (a satellite) = 7.155 days.

Mean distance of Ganymede from Jupiter $= 0 . 0 0 7 1 5 6$ astronomical units.

28.The sidereal period of Jupiter is11.86 years;find the value of $\pmb { \mathcal { Q } }$ Abody of negligible mass moves around the Sun with the same value of a; what is its period? If this body originally drifted away from Jupiter, how long would it be before it approached Jupiter again？ (Assume both orbits are circular,and neglect the attraction of Jupiter.）

29.Procyon isa visual binary with period 40.33 years. The orbit of Procyon B about Procyon A has a value of α which subtends 4".26 on the celestial sphere,while that of A about the center of mass of the system has $a =$ 1".02.Find the ratio of their masses.

If,from the distance of the system, the radius of the Earth's orbit around the Sun subtends an angle $\Updownarrow ^ { \prime \prime } . 2 8 \Updownarrow$ find the distance of the system,the separate masses of the components (compared with the mass of the Sun), and the physical dimensions of the orbit.

30.A binary system consists of two starswith masses $\frac { \pi } { i ^ { 3 } } = \frac { g } { 1 }$ and $\mathbb { M } _ { 2 }$ . The second of these is too faint to be observed, but its presence is inferred from the irregular proper motion of the first. If the first $\{ \mathbb { A } _ { \mathtt { L } } \}$ is found to move around the center of mass of the system in an ellpse subtending $a _ { I } ^ { \prime \prime }$ show that

$$
\frac { \tilde { \mathcal { M } } _ { 2 } ^ { 3 } } { ( \tilde { \mathcal { M } } _ { 1 } \div \tilde { \mathcal { M } } _ { 2 } ) ^ { 2 } } = \frac { a _ { 1 } ^ { \prime \prime } { } ^ { 3 } } { p ^ { \prime \prime } { } ^ { 3 } P ^ { 2 } }
$$

where $\mathcal { P }$ is the period and $\mathcal { P } ^ { \prime \prime }$ the parallax of the system.

31.In the case of a spectroscopic binary, usually the spectrum of only one star is observed. The radial velocity,V,of that star is recorded and plotted as a function of the time t. Show that the constant radial velocity, Ve, of the center of mass of the system can be found from the condition that the areas of the velocity curve above and below the line V= Vc must be equal.

# 6.5The Choice of Units

The values of the various constants used depend on the choice of units. If these are chosen as the astronomical unit (with a modification given below), the mass of the Sun,and the mean solar day,then the resulting value of $\mathbf { \mathcal { \bar { \kappa } } }$ is the Gaussian gravitational constant. When it was first calculated the following data were used:

1 sidereal $\mathrm { y e a r } = 3 6 5 . 2 5 6 3 8 3 5$ mean solar days;

The combined mass of the Earth and Moon,

$$
m _ { e \pm m } = { \frac { 1 } { 3 5 4 7 1 0 } } { \mathrm { ~ s o l a r ~ m a s s e s . } }
$$

Then

$$
\begin{array} { c } { \bar { k } = \frac { 2 \pi } { { P \sqrt { 1 + { m _ { e } } _ { + } } } \pi } } \\ { = 0 . 0 1 7 2 0 2 0 9 8 9 5 . } \end{array}
$$

These data have been revised,and the first figure is known to be steadily changing. The best figures available at the present time give

$$
\mathrm { 1 ~ s i d e r e a l ~ y e a r = 3 6 5 . 2 5 6 3 6 5 5 6 + 0 . 0 0 0 0 0 0 1 1 } \mathcal { T }
$$

where $T$ is measured in centuries from 1900,and

$$
m _ { e + m } = { \frac { 1 } { 3 2 8 9 1 2 } } \ \mathrm { s o l a r \ m a s s e s } .
$$

The value of $k ,$ as first defined, will be sensitive to revisions of the data and to long-term changes. It would be extremely inconvenient to alter its value; so, with the revised data, the unit of length is adjusted so that k retains its original value.

Often,and especially within a program, it is convenient to choose the unit of time so that the gravitational constant is equal to one. For instance, if we choose the mass of the Sun and the astronomical unit as units of mass and length,and take $\ k = \frac { \pi } { 2 }$ ,then in terms of the resulting unit of time the period of the Earth is $2 \pi$ . Such a set of units, often referred to as canonical units, can be advantageous, because, for motion in the solar system, the components of position and velocity will roughly have the same order of magnitude,and this will be, roughly,one. A change of units can always be accomplished with the input and output phases of $^ \mathrm { a }$ program.

Beware of using $G$ in your calculations. For instance, for motion around the Sun,we might take $G = 6 . 6 7 0 \times \mathrm { i } 0 ^ { - 8 }$ and $\tilde { \mathcal { M } } _ { \mathrm { S u m } } = 2 . 0 0 \times \mathrm { i } 0 ^ { 3 3 }$ cgs units, but these values are so poorly determined that the calculation would be of little use.

# Problems

1.Find $\pmb { k }$ when the units of length,mass,and time are as follows: $( a )$ the astronomical unit, the mass of the Sun,the sidereal year; (b) the mean distance of the Moon from the Earth,the mass of the Earth,the sidereal month. If in each case the unit of time is altered so that $k = 1$ ,find that new unit of time.   
2.The components of position and velocity of a comet are (8.134,-10.385,   
1.746)inunits of $\Im \Im ^ { 7 }$ km,and(18.43,15.97,-4.62) km/sec.Express these in terms of astronomical units and mean solar days. Also express them in such units that make $\acute { \kappa } = \acute { \bar { \kappa } }$ when the units of length and mass are the astronomical unit and the mass of the Sun.   
3.Find the maximum value of dr/dt in the Earth's orbit around the Sun in kilometers per second and astronomical units per mean solar day.

4.Show that for a parabolic comet

$$
V = { \frac { 2 6 . 1 7 5 } { \sqrt { r _ { \mathrm { A U } } } } } \ { \mathrm { m p s } }
$$

and find the corresponding result in kilometers per second and astronomical units per mean solar day.

5.A parabolic comet moving in the ecliptic has $q = 0 . 2 8 7 4 5$ AU.Calculate how long (in mean solar days) it lies in its orbit within that of (a) the Earth,(b) Mars, (c） Jupiter,and (d) Pluto,assuming that all these planets move in the ecliptic in circular orbits of radius $a$   
6.For the comet of problem 5, find the speed at perihelion,and the number of daysafter perihelion passage when its speed is 90,80,and 50 per cent of this value. Also find the time when itsspeed is 30 km/sec. Calculate the true anomalies for these positions.   
7.Find the orbital speed of Mercury at perihelion,aphelion,the ends of the minor axis, and the ends of the latus rectum. Give your answers in astronomical units per day.   
8.The mean daily motions of the minor planets Ceres and Medusa are, respectively, 711".2424 and 1105".8897. Find their mean distances from the Sun in astronomical units.

9.Find the period and orbital speed of asatellite that just grazes the Earth's equator. Find the mean distance and orbital speed for a satelite with period 24 sidereal hours.If the unit of length is the Earth's equatorial radius, the unit of mass is the mass of the Earth,and the unit of time is chosen to make k = 1,find the unit of time and express the above results in these units.

10.In order to find k, it is necessary to know the mass of the Earth + Moon. Tofind this,we proceed as follows: let a1 be the semimajor axis of the Moon's orbit about the Earth,and $P _ { \ I }$ its sidereal period.Show that

$$
\frac { a _ { 1 } ^ { 3 } } { P _ { 1 } ^ { 2 } } = \frac { k ^ { 2 } \pi } { 4 \pi ^ { 2 } } ,
$$

where $\mathbf { \nabla } \mathbf { \mathcal { W } }$ is the mass of the Earth $\scriptstyle + \ \Re \cos \Re$ Expressing $\mathcal { Q } _ { \downarrow }$ in astronomical units and $P _ { I }$ in sidereal years,show that

$$
{ \frac { \frac { 1 } { 4 } } { \mathfrak { m } } } \div \mathbb { 1 } = { \frac { P _ { 1 } ^ { 2 } } { a _ { 1 } ^ { 3 } } } ,
$$

and that since $\mathcal { W }$ is in units of the solar mass, we can neglect the number 1 on the left. Hence show that

$$
\frac { \mathtt { i } } { m } = \left( \frac { \\\\sin \pi _ { m } } { \sin \pi _ { s } } \right) ^ { 3 } P _ { \mathtt { i } } ^ { 2 } ,
$$

where $\pi _ { m }$ and $\pi _ { s }$ are the parallaxes of the Moon and Sun (i.e., the angles subtended by the Earth's equatorial radiusat the mean distances of these objects).The principal error in this method comes from the smallness of $\boldsymbol { \mathcal { \pi } } _ { \mathcal { s } }$ ，

11.Using the result above and taking $1 / \eta = 3 2 9 3 9 0$ (Newcomb'svalue) and $\pi _ { s } = 8 ^ { \prime \prime } . 7 9$ as initial values,show that the variation in $I / \gamma _ { 3 }$ caused by varying $\pi _ { s }$ is given by

$$
\delta \left( \frac { 1 } { m } \right) = - 1 1 2 4 4 0 \delta \pi _ { s } ,
$$

where $\delta \pi _ { s }$ is measured in seconds of arc. Thus show that evaluating $I \int \gamma \alpha$ is equivalent to measuring the solar parallax, or, conversely, that the measurement of the solar parallax yieldsa value for $1 / \pi$

12. Using Gauss’ value of $I \int \limits _ { 0 } ^ { + \infty } m$ ，show that

$$
\delta \tilde { \varepsilon } = [ 6 . 7 3 4 8 0 - 2 0 ] \delta \left( \frac { \mathrm { ~ i ~ } } { m } \right)
$$

(where the square brackets mean that the number enclosed is the logarithm of the number required),and thus obtain

$$
\delta \tilde { \kappa } = - 0 . 0 0 0 0 0 0 0 1 7 2 \delta \pi _ { s }
$$

as an approximate expression for changing $\Bbbk$ if it were not agreed to keep this quantity constant.

13.Consider the question of finding the value to ascribe to α for the Earth, as a result of better values of $\mathfrak { T } \mathfrak { T }$ and $\mathcal { P }$ than those used by Gauss, while retaining his value of $\Bbbk$ Let $\eta a _ { 1 }$ and $\mathcal { P } _ { 1 }$ be new values for the mass and period in question,and show that

$$
a = \left( \frac { \mathbb { i } + m _ { \mathbb { i } } } { \mathbb { i } + m } \right) ^ { 1 / 3 } \left( \frac { P _ { 1 } } { P } \right) ^ { 2 / 3 } ,
$$

and thus to terms of the first order

$$
a = 1 \div \frac { 1 } { 3 } \left( m _ { \mathrm { f } } - m + 2 \frac { P _ { \mathrm { l } } - P } { P } \right) .
$$

Take Newcomb's values

$$
\frac { 1 } { m _ { 1 } } = 3 2 9 3 9 0 , \quad P _ { 1 } = 3 6 5 . 2 5 6 3 6 0 4 2
$$

and show that they give $\mathrm { \Omega _ { \mathfrak { L } } = 1 . 0 0 0 0 0 0 0 3 0 }$

# 6.6The Solution of Kepler's Equation

Kepler's equation,and the hunt for its solution in numerical or analytical form have left a legacy rich in mathematical invention. Early in the century, Moulton (Ref. 11) wrote:

“A very large number of analytical and graphical solutions have been discovered,nearly every prominent mathematician from Newton until the middle of the last century having given the subject more or less attention. A bibliography containing the references to 123 papers on Kepler's equation is given in the Bulletin Astronomique, January 1900,and even this list is incomplete."

Invention did not cease in 1900,and the subject of the solution of Kepler's equation would make a good thesis. Even explicit analytical solutions are now known in the form of definite integrals,but they are not competitive among the numerical methods of solution.

All practical methods of solution involve successive approximations. In fact Kepler's equation provides a good example when learning different methods for solving nonlinear equations. In this section we shall use the equation to illustrate some methods to be used later for other problems. First, it is necessary to establish that Kepler's equation always has one and only one solution.

Consider

$$
\begin{array} { r } { \mathcal { F } ( \widehat { \mathcal { E } } ) \equiv \mathcal { E } - e \sin \widehat { \mathcal { Z } } - \mathcal { M } . } \end{array}
$$

Suppose that $\pi \pi < M < ( n \div 1 ) \pi .$ where $\mathfrak { R }$ is an integer. Then

$$
\begin{array} { r } { \bar { \bar { f } } \left( n \pi \right) = n \pi - \bar { M } < 0 , } \end{array}
$$

and

$$
{ \vec { F } } [ ( n + 1 ) \pi ] = ( n + 1 ) \pi - M > 0 .
$$

$S 0 ,$ there is at least one root in the range $\pi \pi < \mathcal { E } < ( \pi + 1 ) \pi$ Now

$$
\frac { d \mathcal { F } ( E ) } { d E } \equiv 1 - e \cos \mathcal { E }
$$

which is strictly positive. Then $F ( { \overrightarrow { E } } )$ is an increasing function, and has at most one root.

The methods to be discussed are general; so, notationally we shall conside

$$
f ( x ) = x - e \sin x - M = 0 , 0 \leq e < 1 .
$$

Let us call the actual solution $z = a$ , and the sequence of approximations, $\ S _ { \mathcal { Z } _ { \Re } \mathfrak { Z } }$ $\mathfrak { R } = \mathbb { 0 } , \mathbb { 1 } , \mathbb { 2 } , \dots$ Let the error of the approximation ${ \boldsymbol { \mathfrak { L } } } _ { \mathfrak { R } }$ be $\epsilon _ { \mathfrak { R } }$ ,so that

$$
x _ { \mathfrak { T } } \div \epsilon _ { \mathfrak { r } } = a .
$$

Then we can generate the Taylor series expansion

$$
\begin{array} { l } { { 0 = f ( a ) = f ( x _ { n } + \varepsilon _ { n } ) } } \\ { { \ = f ( x _ { n } ) + \epsilon _ { n } f ^ { \prime } ( x _ { n } ) + \frac { 1 } { 2 } \epsilon _ { n } ^ { 2 } f ^ { \prime \prime } ( x _ { n } ) + \frac { 1 } { 6 } \epsilon _ { n } ^ { 3 } f ^ { \prime \prime \prime } ( x _ { n } ) + \cdot \cdot \cdot } } \end{array}
$$

Let us define $\delta _ { \pi }$ by

$$
0 = f ( x _ { n } ) + \delta _ { n } f ^ { \prime } ( x _ { n } ) ,
$$

which is approximating $\epsilon _ { \pi }$ if $\epsilon _ { \mathfrak { r } } ^ { 2 }$ in (6.6.3) can be neglected. Starting with an initial guess $\pmb { \mathcal { Z } } \hat { \mathbf { \mu } }$ (the provenance of which will be discussed shortly),let the sequence $\{ x _ { \pi } \}$ be generated by

$$
x _ { n + 1 } = x _ { n } + \delta _ { n } = x _ { n } - { \frac { f ( x _ { n } ) } { f ^ { \prime } ( x _ { n } ) } } , n = 0 , 1 , 2 , \ldots
$$

This sequence gives the solution by Newton's method. Notice that the approximation to find $x _ { \pi + \frac { \pi } { 2 } }$ neglects the square of the error of ${ \mathfrak { X } } _ { \mathfrak { Z } }$ This is a quality of quadratic convergence which appears clearly in the following example:

$$
\begin{array} { r l r } & { } & { \mathrm { F o r ~ } M = 1 , e = . 8 , x _ { 0 } = 1 . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 , } \\ & { } & { x _ { 1 } = \frac { 2 . 1 8 5 6 7 5 2 4 1 } { 2 . 8 2 5 6 7 5 3 4 0 } \frac { 2 4 1 } { 3 9 5 6 8 5 } , } \\ & { } & { x _ { 2 } = \frac { 1 . 8 2 1 } { 2 . 8 2 1 } 5 2 5 3 4 0 2 4 1 4 4 5 , } \\ & { } & { x _ { 3 } = \frac { 1 . 7 8 2 6 9 3 1 7 0 1 0 9 2 2 1 } { 3 . 8 4 1 } , } \\ & { } & { x _ { 4 } = \frac { 1 . 7 8 2 1 9 1 4 1 3 2 4 1 8 5 1 } { 3 . 8 5 6 } , } \\ & { } & { x _ { 5 } = \frac { 1 . 7 8 2 1 9 1 3 2 8 9 3 7 9 0 3 } { 1 . 7 8 2 1 9 1 3 2 8 9 3 7 9 0 1 } . } \end{array}
$$

“Good” parts have been underlined. Roughly speaking， once convergence is well established in Newton's method, the number of correct figures is doubled for successive iterates. More precisely, we can say that the order of convergence is $\pmb { k }$ if

$$
\operatorname* { l i m } _ { \pi \to \infty } \frac { \epsilon _ { n + 1 } } { \epsilon _ { n } ^ { k } } \mathrm { e x i s t s , a n d i s \ n o t \ z e r o . }
$$

$\ l \overrightarrow { \mathfrak { F } } \ l 0 \tau \ k = \breve { \bar { z } }$ the convergence is linear, for $\xi = 2$ , the convergence is quadratic, and so on. We are going to derive and use a method having quartic convergence, with $k = 4$

First,retain just one further term in (6.6.3) in the approximation of $\delta _ { \pi }$ Then

$$
0 = f ( x _ { n } ) \div \delta _ { n } f ^ { \prime } ( x _ { n } ) + { \textstyle \frac { 1 } { 2 } } \delta _ { n } ^ { 2 } f ^ { \prime \prime } ( x _ { n } ) ,
$$

which will be abbreviated as

$$
\begin{array} { r } { \mathbb { G } = f _ { n } + \delta _ { n } \hat { j } _ { n } ^ { \prime } + \frac { 1 } { 2 } \delta _ { n } ^ { 2 } \hat { j } _ { n } ^ { \prime \prime } . } \end{array}
$$

This can be written in the form

$$
\delta _ { n } = - \frac { f _ { n } } { f _ { n } ^ { \prime } + \frac { 1 } { 2 } \delta _ { n } f _ { n } ^ { \prime \prime } } ,
$$

and this can be solved for δn with an accuracy consistent with the approximation already made by:

$$
\delta _ { n \downarrow } = - \frac { f _ { n } } { f _ { n } ^ { \prime } } , \quad \delta _ { n 2 } = - \frac { f _ { n } } { \bar { f } _ { n } ^ { \prime } + \frac { 1 } { 2 } \delta _ { n 1 } \bar { f } _ { n } ^ { \prime \prime } } , \quad x _ { n \div 1 } = x _ { n } + \delta _ { n 2 } .
$$

The sequence formed in this way would have cubic convergence; it is essentially Halley's method. Notice that in going from a program using Newton's method to one using Halley's,only one additional instruction is needed.

Finally,use a further term in (6.6.3) to approximate en by δn,and write

$$
\delta _ { n } = - \frac { f _ { n } } { f _ { n } ^ { \prime } + \frac { 1 } { 2 } \delta _ { n } f _ { n } ^ { \prime \prime } + \frac { 1 } { 6 } \delta _ { n } ^ { 2 } f _ { n } ^ { \prime \prime \prime } } .
$$

This can be adequately solved for Sn by:

followed by

$$
\begin{array} { r l } & { \delta _ { n 1 } = - \frac { f _ { n } } { f _ { n } ^ { \prime } } , } \\ & { \delta _ { n 2 } = - \frac { f _ { n } } { f _ { n } ^ { \prime } + \frac { 1 } { 2 } \delta _ { n 1 } f _ { n } ^ { \prime \prime } } , } \\ & { \delta _ { n 3 } = - \frac { f _ { n } } { f _ { n } ^ { \prime } + \frac { 1 } { 2 } \delta _ { n 2 } f _ { n } ^ { \prime \prime } + \frac { 1 } { 6 } \delta _ { n 2 } ^ { 2 } f _ { n } ^ { \prime \prime \prime } } } \\ & { } \\ & { x _ { n + 1 } = x _ { n } + \delta _ { n 3 } , } \end{array}
$$

which leads to a sequence {xn} having (in theory) quartic convergence. Calculations using this method are shown below.

$$
\begin{array} { r l r } & { } & { \mathrm { F o r ~ } M = 1 , e = 1 , \mathrm { ~ } z _ { 0 } = 1 . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 , } \\ & { } & { x _ { 1 } = \underline { { 1 . 8 0 4 } } 2 3 8 6 9 6 4 3 7 6 6 3 , } \\ & { } & { x _ { 2 } = \underline { { 1 . 7 } } 8 2 \underline { { 1 } } 9 1 3 3 2 9 5 9 5 7 5 , } \\ & { } & { x _ { 3 } = 1 . 7 8 2 \underline { { 1 } } 9 1 3 2 8 9 3 7 9 0 \underline { { 1 } } . } \end{array}
$$

The calculations for implementing the equations (6.6.7) are given by the instructions 210-360 in the following program. But before we are ready for that，we must devise tactics for making the initial guess, $\mathtt { z 0 }$ For a start, consider only values ofM for which 0≤M≤π.The value ofxo used above was xo= M. Consider the M -e plane. The guess xo = M is only correct for the loci $e = 0$ or $\tilde { \beta } \tilde { \mathcal { Z } } = \hat { \mathbb { Z } }$ $\pi$ Now consider

$$
x _ { 0 } = { \mathcal { M } } + k e , \ 0 \leq k \leq 1 .
$$

This is correct if $e = 0$ orif $k = \sin ( \mathcal { M } + \mathcal { k } e )$ The latter is true along the two sloping lines: $M = - k e \pm \sin ^ { - 1 } k$ These lines appear in Figure 6.6 for the case $k = . 8 5$

Using (6.6.8） with $\acute { \kappa } = . 8 5$ ,the tables listed above are modified to give

$$
x _ { 1 } = 1 . 7 8 5 9 9 3 0 8 7 8 3 5 9 6 7 ,
$$

$$
\mathrm { { z } _ { 2 } = \mathrm { { \underline { { { i } } } . 7 8 2 1 0 6 1 5 4 1 8 7 8 2 0 } } } ,
$$

$$
x _ { 3 } = { \underline { { 1 } } } . 7 8 2 \ { \underline { { 1 } } } . 9 1 \ { \underline { { 3 2 8 } } } . 9 4 5 \ 6 9 8 ,
$$

$$
x _ { 4 } = { \underline { { 1 . 7 8 2 } } } { \underline { { 1 9 1 } } } { \underline { { 3 2 8 } } } { \underline { { 9 3 7 } } } { \underline { { 9 0 } } } { \underline { { 1 } } } .
$$

Accelerated Convergence

$$
\begin{array} { r } { \mathbb { F } \mathrm { o r } \ M = 1 , \ e = . 8 , x _ { 0 } = \underline { { 1 } } . 6 8 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 , } \\ { x _ { 1 } = \underline { { 1 . 7 8 2 \ 1 9 3 } } 6 3 0 \underline { { 1 0 0 1 } } \underline { { 1 } } \mathbb { 7 } , } \\ { x _ { 2 } = \underline { { 1 . 7 8 2 \ 1 9 1 } } 3 2 8 9 3 7 9 0 1 . } \end{array}
$$

Next, suppose that $\pi \leq \mathbb { M } \leq 2 \pi$ Since sin $\pmb { \mathcal { A } }$ is negative, the modification to (6.6.8) is $x _ { 0 } = M - k e$ So,overall, for $0 \leq M \leq 2 \pi$ ，we can take ${ \mathfrak { X } } _ { \widehat { \mathfrak { Q } } } =$ $M + S G N ( \sin M ) k e .$ To consider any $\underline { { \tilde { \lambda } } } \underline { { \tilde { \mathcal { A } } } }$ ,bear in mind that for practical purposes, $E$ is only required $m \operatorname { o d } ( 2 \pi )$ So to find $\boldsymbol { \mathfrak { X } } _ { \mathfrak { Q } }$ ,calculate the following:

$$
\begin{array} { r }  \tilde { M } ^ { * } = \tilde { M } - \left[ \frac { M } { 2 \pi } \right] ( 2 \pi ) , \quad ( \mathrm { s o ~ t h a t ~ 0 \leq \tilde { M } ^ { * } < 2 \pi \} , } \\ { \sigma = S G N ( \mathrm { s i n ~ } \tilde { M } ^ { * } ) , } \\ { x _ { 0 } = \tilde { M } ^ { * } + \sigma \dot { \pi } e . \qquad } \end{array}
$$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0081-0120/ocr/images/cd17fb35a231e2f75691dce2714a120adaec9c6e60b973721f83c28c99e50cb8.jpg)  
Figure 6.6 The fgures give the number of iterations (counting the initial guess as one)before $\bar { \hat { j } } ( \hat { x _ { j } } ) \hat { \rvert } < \bar { \pmb { \mathrm { v } } } ^ { - 1 2 }$ The initial guess was ${ \mathfrak { x } } _ { 0 } = \mathbb { M } + . 8 5 e$

A discussion of other initial guesses can be found in a paper by Danby and Burkardt (Ref. 32). I hope that you will experiment with some of your own. A program listing is given below.

First,some comments are in order about the programs listed in this text. The listings are based on programs run on an IBM PC that generated the umbers appearing in the text. The version of BASIC is BASICA/D. (BASICA alone will generate functions only in single precision.) If a program is to be copied as it stands,then all instructions corresponding toa given line number should be entered without hitting the RETURN (or ENTER) key.The format below isfor clarity;it is not the same as a printout of the program. The main reason forlisting programs is to show how the mathematics can be transformed into program. Most readers will not use BASIC. If you do use BASIC, then, having followed the listed program, change it in order to suit your own style of programing.

REH NEVTON'S HETHOD VITH ACCELERATION APPLIED TOREH KEPLER'S EQUATION.CLSDEFDBL A-K,P-Z:DEFINT NINPUT ENTER A VALUE FOR THE ECCENTRICITY ；E:PRINTINPUT ENTER A VALUE FOR THE HEAN ANONALY ；H:PRINTPI=3.141592653589793#K=.85REK THIS CONTROLS THE INITIAL GUESS.SEE （6.6.8）DEL=1E-14110REH BOUND ON THE PERNISSIBLE ERROR FOR THE ANSVER.120HS=H-INT（H/（2\*PI））\*(2\*PI）SIGHA =SGN(SIN(HS)）140X=HS+SIGHA\*K\*EREM INITIAL GUESS.SEE (6.6.9).NC=0REN NC WILL COUNT THE NUKBER OF ITERATIONS.180PRINTXREH NOV WE HAVE THE HAIN ITERATION USING （6.6.7).200 ES= E\*SI(x)

210 F_=x-_ES-HS   
220IF ABS（F)<DEL THEN 410   
230 REK CONVERGENCE.   
240 EC=E\*COS（X）   
250 FP =1-EC   
260 FPP=ES   
270 FPPP = EC   
280 DX=-F/FP   
290 REM IFVE SKIPPED TO 36O VE VOULD BE APPLYING   
300 REM NEWTON'S HETHOD WITH QUADRATIC CONVERGENCE.   
310 DX=-F/(FP+DX\*FPP/2\*）   
320 REM IF WE SKIPPED TO 36O VE VOULD BE APPLYING   
330 REH HALLEY'S HETHOD VITH CUBIC CONVERGENCE.   
340 DX=-F/（FP+DX\*FPP/2#+DX\*DX\*FPPP/6#）   
350 REM THIS LEADS THEORETICALLY TO QUARTIC CONVERGENCE.   
360X=X+DX   
370 NC= NC÷1   
380 PRINT X,DX   
390 IF NC> 10 THEN420   
400 GOT0 200   
410 END   
420 PRINT "NO CONVERGENCE."   
430 END

Some points about this need discussion. The parameter DEL controls the accuracy of the solution. This should not be as small as the round-off error of the calculation,or the iteration may never stop in spite of the fact that all possible accuracy has been found. In case the test for ending the iteration fails, there should be a maximum number of steps allowed, after which some message should be relayed.Various tactics exist for ending an iteration. In the listing, lf(x)lis compared with DEL. (NEVER forget that the absolute value must be used).Alternatively,the correction $\vert \overrightarrow { i } - \overrightarrow { k } \vert$ might be compared.If the solution of $f ( x ) = 0$ may be at least an order of magnitude greater than one, then the relative size of the correction, |DX/f(x)| might be used. Keep an open mind, and make lots of experiments.A lot can be learned by using a hand calculator; here pressing a key can initiate the next operation, and the logical decisions are made by the operator.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0081-0120/ocr/images/6f39e7dc326bcb5634dde520768049aabc1c55c374207a76c84f913d775124e7.jpg)  
Figure 6.7 An iteration, using the secant method.

In Figure 6.6 the M-e plane has been divided into regions according to the number of iterations needed to secure |f(x)|<10-12.A count of “one" indicates that the initial guess was sufficiently accurate.

When solving f(x)= O it may happen that f'(x） is inconvenient or impossible to find. From many methods available, we shall consider two. In the secant method two approximations, Xn-1 and xn, are used to find the next, n+1:Geometrically，xn+1 is the point where the chord through the points (n-1,f(xn-1)) and (xn, f(xn)) cuts the x-axis,as illustrated in Figure 6.7. Analytically,

$$
x _ { n + 1 } = { \frac { x _ { n - 1 } f ( x _ { n } ) - x _ { n } f ( x _ { n - 1 } ) } { f ( x _ { n } ) - f ( x _ { n - 1 } ) } } .
$$

Two initial values are needed. One way to look for these is to have a search, increasing x by equal increments and calculating f(x） each time; when the product of two successive values of fis negative,a solution has been bracketed, and the iteration starts with the bracketing values of x. This is the method usedin the program listed below.

REH THE SECANT METHOD APPLIED TO KEPLER'S EQUATION. CLS   
DEFDBL A-H,O-Z:DEFINT N   
INPUT ENTER A VALUE FOR THE ECCENTRICITY ；E:PRINT INPUT ENTERA VALUE FOR THE MEAN ANOHALY :PRINT INPUT ENTER A VALUE FOR THE START OF THE SEARCH ；X PRINT   
INPUTENTER THE INCREHENTFOR THE SEARCH ；DX ：PRINT DEFFN F(X)= X-E \*SIN(X)-H   
REN VE ARE SOLVING $I ^ { \prime } ( \vec { \lambda } ) = 0$ ·   
TOL = 1E-14   
NS=0   
REM NS COUNTS THE NUMBER OF STEPS IN THE INITIAL SEARCH. FO=FN F(XO）:PRINT XO,FO   
REMLINES 18O-24O FORM THE SEARCH LOOP.IFA   
REN SOLUTION HAS NOT BEEN BRACKETED AFTER   
REH TEN STEPS，THE LOOP IS ABANDONED.   
X1=XO+DX   
1F   
REN THEN A SOLUTION HAS BEEN BRACKETED.   
= NS÷1   
NS>10 THEN_350   
=X1 :FO=F1:GOTO180   
NC=0   
RENTHIS NC COUNTS THE NUHBER OF SECANT ITERATIONS. REN 29O-34O FORM THE ITERATION LOOP USING THE   
  
C=NC+1:IF NC>10 THEN380   
X0 = X1 : FO = F1 : X1 = X : F1 = F   
GOTO 290   
PRINT SEARCH FAILED.FOR ANOTHER TRY ENTER 1   
PRINT TOQUIT,ENTER2   
INPUTN:ONNGOTO_6O,390   
30 PRINT "ITERATION FAILED"

A specimen run of this program produced the following results:

$$
\displaystyle \mathbb { F } _ { 0 \Sigma } M = 1 , e = . 8 .
$$

f（x)=x-esinx-MSearch  
0.0 -1.0000000000000000  
0.5 -0.8835404515266419  
1.0 -0.673176765 4418945  
1.5 -0.297995 9845542908  
2.0 +0.272 562 0567798615

# Iteration

1.761144320968186 -0.0244064424186945  
1.780 774744371344 -1.653586 514294148D-03  
1.782 201404 986 862 +1.176744626718573D-05  
1.782191324155 680 -5.584960938165295D-09  
1.782191328937 885 -1.892 930256985 892D-14  
1.782191328937 901 -5.551115123125783D-17

Convergence, when it is established, is better than linear but not as good as quadratic.

The next method to consider,known as Steffensen's method,has quadratic convergence. Suppose that the equation ${ \mathfrak { f } } \{ { \mathfrak { x } } \} = \ \mathfrak { 0 }$ isrearranged into the form

$$
{ \mathfrak { x } } = g \{ { \mathfrak { x } } \} .
$$

This can be done in any number of ways. For Kepler's equation we can write, for instance,

$$
x = g ( x ) = e \sin x + M .
$$

Then,with some initial $\mathtt { \mathtt { X 0 } }$ ,the sequence $\{ x _ { n } \} , n = 0 , 1 , 2 , \ldots$ is generated using

$$
x _ { n } = g ( x _ { n - 1 } ) , \quad n = 1 , 2 , \ldots
$$

As before,if ${ \mathfrak { X } } = { \mathfrak { a } }$ is the correct solution, and if $x _ { \mathfrak { T } } \div \varepsilon _ { \mathfrak { T } } = \mathfrak { a }$ then,by the mean value theorem,

$$
\begin{array} { r l } { a - \epsilon _ { n } = g ( a - \epsilon _ { n - 1 } ) } & { } \\ { = g ( a ) - \epsilon _ { n - 1 } g ^ { \prime } ( \xi _ { n - 1 } ) , } & { } \end{array}
$$

where $\xi _ { n - 1 }$ lies between $\pmb { \mathcal { Q } }$ and $\mathcal { Z } _ { \mathfrak { A } - \mathfrak { I } }$ . Then since $\alpha = g \{ \alpha \}$ ：

$$
\epsilon _ { n } = \epsilon _ { n - 1 } g ^ { \prime } ( \xi _ { n - 1 } ) .
$$

If $| \boldsymbol { \mathcal { G } } ^ { \prime } ( \boldsymbol { \mathfrak { x } } ) | < \mathrm { ~ \mathfrak { z } ~ }$ for the values of $\pmb { x }$ appearing in. the sequence, then the error $\epsilon _ { \mathfrak { T } }$ will tend to zero as $\Im \hat { \textbf { \textit { a } } }$ tends to infinity， and the sequence will converge to $\pmb { \mathcal { Q } }$ But the convergence will be,in general, linear,with the ratio between two

successive errors approaching $\clubsuit$ constant (equal to $g ^ { i } \{ a \} \}$ This property can, however,be harnessed,as follows.

Assume that $\epsilon _ { n + 2 } / \epsilon _ { n + 1 } \simeq \tilde { \mathcal { L } }$ and $\epsilon _ { n + 1 } / \epsilon _ { n } \simeq \mathbb { I }$ or, equivalently,

$$
\frac { a - x _ { n + 2 } } { a - x _ { n + 1 } } \simeq \frac { a - x _ { n + 1 } } { a - x _ { n } } \simeq \bar { L } .
$$

L is unknown, but can be ignored. If the“\~” symbol is replaced by “=",and a is replaced by an+2, then we have

$$
\frac { a _ { n + 2 } - x _ { n + 2 } } { a _ { n + 2 } - x _ { n + 1 } } = \frac { a _ { n + 2 } - x _ { n + 1 } } { a _ { n + 2 } - x _ { n } } .
$$

This can be solved for ${ \mathcal { a } } _ { \mathfrak { n } + 2 }$ So corresponding to the converging sequence $\{ x _ { \pi } \}$ ， there is another sequence, {an},and it can be shown that this converges to a faster than the frst sequence. This illustrates Aitken's“delta process". It will be applied to the solution of ${ \mathfrak { x } } = g _ { \mathfrak { x } } ^ { \prime } { \mathfrak { x } } )$ as follows.

Start with $^ { \oslash }$ guess, $\mathfrak { L } _ { \widehat { \sf U } }$ Then let

$$
\begin{array} { r } { x _ { 1 } ^ { * } = x _ { 0 } , \quad x _ { 2 } ^ { * } = g ( x _ { 1 } ^ { * } ) , \quad x _ { 3 } ^ { * } = g ( x _ { 2 } ^ { * } ) . } \end{array}
$$

Define $\pmb { \mathcal { Z } } _ { \vec { \lambda } }$ by

$$
{ \frac { x _ { 1 } - x _ { 3 } ^ { * } } { x _ { 1 } - x _ { 2 } ^ { * } } } = { \frac { x _ { 1 } - x _ { 2 } ^ { * } } { x _ { 1 } - x _ { 1 } ^ { * } } } .
$$

Then $\pmb { \mathcal { Z } } _ { \mathbb { I } }$ can be written as

$$
x _ { \mathrm { i } } = x _ { 0 } - \frac { ( x _ { \mathrm { i } } ^ { * } - x _ { 2 } ^ { * } ) ^ { 2 } } { ( x _ { \mathrm { i } } ^ { * } - 2 x _ { 2 } ^ { * } \div x _ { 3 } ^ { * } ) } .
$$

This shows the progress from xo to x1； further iterations are similar. The process is illustrated in the following program, applied to Kepler's equation in the form (6.6.12).Before calculating (6.6.17)it is advisable to make sure that the denominator is not too small; this will explain lines 130-160 in the listing below.Note that this is not intended as a general program for solving Kepler's equation but as an illustration of the use of Steffensen's method.

Notice that $| g ^ { \prime } ( x ) | = | e \cos x | \le e$ ,so that for elliptic motion the sequence generated by (6.6.i3) does converge linearly. But the algebra involved in deriving(6.6.15)does not require $\pmb { \mathcal { L } }$ to be less than one,and Steffensen's method can beapplied even if the sequence corresponding to (6.6.13) diverges linearly. For that reason, the program includes the hyperbolic version of Kepler's equation. Actually,the sequence (6.6.13) diverges worse than linearly,but Steffensen's method can still work;live dangerously,and try it!

80 90 PRINT IF   
REM THIS AVOIDS DIVISION BY ZERO IN（6.6.17）.REM IF THE DENOHINATOR IS CLOSE TO ZEROREN THE HETHOD IS ASSUNED TO HAVE CONVERGED.REN NOW APPLY （6.6.17).  
=（x2-x1）\*（x2-X1）/（x1-x2-x2+X3）  
END =LOG（2#\*H/E÷1.8#）:PRINT X1  
=E\*（EXP（X2）-EXP（-X2））/2#- = E\*（EXP（X1）-EXP（-X1））/2#-ABS（X1- X2-X2 + X3)<1E-14 THEN290=（x2-x1）\*（x2-X1）/(x1-x2-X2÷X3）=Xi-DX:PRINT X1,DXABS(DX）> 1E-14 THEN 230END

Finally,we shall describe an important application of the method of Laguerre,as modifed by B.A. Conway. This method was derived originally for finding roots of polynomials,and it does this with considerable success. It has local cubic convergence (for a simple root),and for real roots it usually generates a monatonic convergent sequence. So it is less sensitive to the quality of the initial guess than is Newton's method.We start the discussion with a somewhat pragmatic derivation of the method's basic formula.1

Let $P _ { n } \{ x \}$ be a polynomial in $\pmb { x }$ of degree $\mathfrak { P }$ ,having simple roots $\mathfrak { p } _ { 1 } , \mathfrak { p } _ { 2 } , \dots , \mathfrak { p } _ { \pi }$ Then

$$
P _ { n } ( x ) = a ( x - r _ { 1 } ) ( x - r _ { 2 } ) \cdot \cdot \cdot ( x - r _ { n } ) .
$$

Differentiating logarithmically, we find

$$
{ \frac { P _ { n } ^ { t } } { P _ { n } } } = { \frac { 1 } { x - r _ { 1 } } } + { \frac { 1 } { x - r _ { 2 } } } + \cdots + { \frac { 1 } { x - r _ { n } } } = A .
$$

Differentiating again,

$$
{ \frac { P _ { n } ^ { \prime \prime } } { P _ { n } } } - { \frac { P _ { n } ^ { \prime 2 } } { P _ { n } ^ { 2 } } } = - { \frac { 1 } { ( x - r _ { 1 } ) ^ { 2 } } } - { \frac { 1 } { ( x - r _ { 2 } ) ^ { 2 } } } - \cdots - { \frac { 1 } { ( x - r _ { n } ) ^ { 2 } } } = B .
$$

Suppose now that we want to approximate $\mathfrak { F } _ { \mathfrak { Z } }$ .For $\hat { \mathbf { \Omega } }$ given value of $\mathscr { x }$ ,assumed to be“close”to $\gamma _ { 1 }$ ,let

$$
p = x - r _ { 1 } , \quad \mathrm { a n d } \quad q _ { k } = x - r _ { k } , \quad k = 2 , 3 , \ldots , n ,
$$

and make the approximation

$$
q \simeq q _ { k } , \mathrm { ~ } _ { k } ^ { * } = 2 , 3 , \ldots , n .
$$

Then

$$
A \simeq \frac { 1 } { p } + \frac { \pi - 1 } { q } , ~ \mathrm { a n d } ~ B \simeq - \frac { 1 } { p ^ { 2 } } - \frac { \pi - 1 } { q ^ { 2 } } .
$$

Eliminating $\mathfrak { q }$ and solving for $\mathfrak { P }$ we find

$$
x - r _ { 1 } = p \simeq \frac { n } { A \pm \sqrt { ( n - 1 ) ( - n B - A ^ { 2 } ) } } .
$$

The sign must be chosen to maximize the absolute value of the denominator. If the value ofx “approximates”r1, then the subtraction of the right-hand side of(6.6.23）from $\pmb { \mathscr { X } }$ will providea better approximation.

Proceeding to Conway's application,we replace $\mathcal { P } _ { \mathcal R } \{ \boldsymbol { x } \}$ by $f ( x )$ so we are solving the equation $f ( x ) = 0$ Let

$$
A = \frac { f ^ { \prime } } { f } , \mathrm { \quad } \hat { \mathrm { a n d \quad } } B = \frac { f ^ { \prime \prime } } { f } - \frac { f ^ { \prime } 2 } { f ^ { 2 } } .
$$

Let n be a parameter to be chosen by whoever is using the method. Then if x is an approximation to a root,we continue to use the right-hand side of (6.6.23) to give an improvement to the approximation. More specifically, substituting (6.6.24) into the right-hand side of (6.6.23),we can define the iteration:

$$
x _ { i + 1 } = x _ { i } - \frac { n f _ { i } } { f _ { i } ^ { \prime } \pm \sqrt { ( n - \frac { 1 } { 4 } ) ^ { 2 } f _ { i } ^ { \prime 2 } - n ( n - \frac { 1 } { 4 } ) f _ { i } f _ { i } ^ { \prime \prime } } } .
$$

Here fi= f（xi），f= f'(xi）,and f=f"(xi）.The sign in the denominator will be the same as the sign of $\hat { f } _ { \downarrow } ^ { f }$

To demonstrate the quality of the local convergence of the sequence generated by(6.6.25),assume that f≠0,so that the denominator in (6.6.25） can be developed in powers of $f _ { \vdots }$ .Then,if $\pi > 1$ ，

$$
\begin{array} { r l r } {  { x _ { i + 1 } = x _ { i } - n f _ { i } \bigg / ( f _ { i } ^ { \prime } + ( n - 1 ) f _ { i } ^ { \prime } [ 1 - \frac { n } { n - 1 } \frac { f _ { i } f _ { i } ^ { \prime \prime } } { f _ { i } ^ { \prime 2 } } ] ^ { 1 / 2 } ) } } \\ & { } & { = x _ { i } - n f _ { i } \bigg / ( f _ { i } ^ { \prime } + ( n - 1 ) f _ { i } ^ { \prime } [ 1 - \frac { 1 } { 2 } \frac { n } { n - 1 } \frac { f _ { i } f _ { i } ^ { \prime \prime } } { f _ { i } ^ { \prime 2 } }   } \\ & { } & {   - \frac { 1 } { 8 } ( \frac { n } { n - 1 } ) ^ { 2 } ( \frac { f _ { i } f _ { i } ^ { \prime \prime } } { f _ { i } ^ { \prime 2 } } ) ^ { 2 } - \cdots ] \bigg ) } \\ & { } & { = x _ { i } - f _ { i } \bigg / ( f _ { i } ^ { \prime } - \frac { 1 } { 2 } \frac { f _ { i } f _ { i } ^ { \prime \prime } } { f _ { i } ^ { \prime } } - \frac { 1 } { 8 } \frac { n } { n - 1 } \frac { f _ { i } ^ { 2 } f _ { i } ^ { \prime \prime } } { f _ { i } ^ { \prime 8 } } - \cdots ) . } \end{array}
$$

Truncating the denominator after the second term,we see that the approximation is equivalent to Halley's method,with local cubic convergence,and that, provided $\Re > 1$ thisproperty is independent of the value of $\pmb { \mathcal { T } } _ { \pmb { \mathcal { L } } }$ ，

In its application,the method seems to be rather insensitive to the value of n that is used. Conway opts for n= 5.Note that if the expansion (6.6.3) were truncated after the quadratic term, and the resulting quadratic equation solved foren, then the resulting algorithm will be equivalent to (6.6.25) with n= 2.

Another form can be derived by dividing the numerator and denominator in （6.6.25)by n,and then letting n tend to infinity. Then

$$
x _ { i + 1 } = x _ { i } - { \frac { f _ { i } } { \operatorname { S G N } \left( f _ { i } ^ { \prime } \right) \left( f _ { i } ^ { \prime 2 } - f _ { i } f _ { i } ^ { \prime \prime } \right) { 1 } / { 2 } } } .
$$

If n is changed from step to step, then the method can be modifed to give local quartic convergence. Consider the sequence in (6.6.7). If this is combined explicitly into one formula,then

$$
x _ { i + 1 } = x _ { i } - f _ { i } \Bigg / \left( f _ { i } ^ { \prime } - \frac { 1 } { 2 } f _ { i } ^ { \prime \prime } \left( \frac { f _ { i } } { f _ { i } ^ { \prime } - \frac { 1 } { 2 } \frac { f _ { i } f _ { i } ^ { \prime \prime } } { f _ { i } ^ { \prime } } } \right) + \frac { 1 } { 6 } f _ { i } ^ { \prime \prime } \left( \frac { f _ { i } } { f _ { i } ^ { \prime } - \frac { 1 } { 2 } \frac { f _ { i } f _ { i } ^ { \prime \prime } } { f _ { i } ^ { \prime } } } \right) ^ { 2 } \right) .
$$

If the denominator is developed in powers of $f _ { i }$ ,we find

$$
x _ { i + 1 } = x _ { i } - f _ { i } \Bigg / \left( f _ { i } ^ { \prime } - \frac { 1 } { 2 } \left( \frac { f _ { i } f _ { i } ^ { \prime \prime } } { f _ { i } ^ { \prime } } \right) - \left( \frac { f _ { i } ^ { 2 } } { f _ { i } ^ { \prime 3 } } \right) \left( \frac { 1 } { 4 } f _ { i } ^ { t t 2 } - \frac { 1 } { 6 } f _ { i } ^ { t t } f _ { i } ^ { \prime } \right) \cdots \right) .
$$

Comparing this with (6.6.26),we see that we can achieve local quartic convergence if

$$
{ \frac { 1 } { 8 } } { \frac { 1 } { n - 1 } } { \bar { f } } _ { i } ^ { \prime \prime } = { \frac { 1 } { 4 } } { \bar { f } } _ { i } ^ { \prime \prime } 2 - { \frac { 1 } { 6 } } { \bar { f } } _ { i } ^ { \prime \prime \prime } { \bar { f } } _ { i } ^ { i } .
$$

Then

$$
\pi = { \frac { 6 - 4 X } { 3 - 4 X } } , \quad { \mathrm { w h e r e } } \quad X = { \frac { { \hat { j } } _ { i } ^ { \prime } { \hat { j } } _ { i } ^ { \prime \prime \prime } } { { \hat { j } } _ { i } ^ { \prime } } } .
$$

There is no guarantee that $\mathfrak { P }$ found in this way,will be less than one;consequently, the sign to be used in (6.6.25) should be the same as the sign of $( \pi - I ) f _ { i } ^ { \prime }$

But the greatest advantage of this method lies in its non-local qualities. You can apply it to the solution of Kepler's equation with initial guesses so stupid that Newton's method (accelerated or not) will fail; but in my experience this algorithm of Laguerre-Conway will converge in every case. But one important precaution must be taken. In (6.6.25) the ABSOLUTE VALUE of the contents of the radical must be calculated.Close to a solution,this will be positive anyway，but with a wild initial guess,it may be negative.For elliptic motion, with initial guesses made as described earlier,Iprefer to use Newton's method accelerated to give local quartic convergence,since it is quicker,and involves less computation (for instance, no square root need be taken).However,as we shall see,when using universal variables for hyperbolic motion, Newton's method can often fail,whereas the method of Laguerre-Conway does not.

This method will be used in the program listing in section 6.10.

# Problems

1. Figures like 6.6 are useful when comparing different methods of iteration or different initial guesses. See if you can confirm the details of that .

figure,and then derive similar figures when (a) Newton's method and (b) Halley's method isused.

2.If the instruction

$$
\delta _ { n 4 } = - \frac { f _ { n } } { \bar { f } _ { n } ^ { \prime } + \frac { 1 } { 2 } \delta _ { n 3 } \bar { f } _ { n } ^ { \prime \prime } + \frac { 1 } { 6 } \delta _ { n 3 } ^ { 2 } \bar { f } _ { n } ^ { \prime \prime \prime } + \frac { 1 } { 2 4 } \delta _ { n 3 } ^ { 3 } \bar { f } _ { n } ^ { \prime \prime \prime } }
$$

is added to (6.6.7) then we have a method with,in theory, quintic convergence. Test this and see if any advantage appears over the method with quartic convergence.

3.Compare the use of different values of $\Bbbk$ in (6.6.8).

4.Find the locus of exact solutions in the M - e plane if xo = M 十 (e/0.55)²(1.1-e). Find a diagram corresponding to Figure 6.6 for this initial guess.

5.Repeat exercise 4 for xo= M+(1.2/π)eM(π-M).These initial guesses are taken from Reference 32. Consult this,and see if you can find better initial guesses.

6.Investigate carefully different tactics for ending an iteration.

7.For the hyperbolic form of Kepler's equation we have

$$
\begin{array} { r } { f ( x ) = e \sin \frac { 1 } { 1 1 } ( x ) - x - M = 0 . } \end{array}
$$

Show that,neglecting $\exp \{ - { \mathfrak { x } } \mathfrak { x } \}$ in the expression for $\sin ^ { 3 } \pi \Im \{ x \}$ ,the approximation xg= In(2M/e) results. Writea program for solving this form of Kepler's equation using this initial guess. Better results can be obtained by taking

$$
x _ { 0 } = \ln \left( \frac { 2 M } { e } + k \right) , k > 0 .
$$

k = 1.8 gives good results. Experiment with this and other values. A discussion of this appears in Reference 32.

8.Experiment with the method of Laguerre-Conway. Remember to use the absolute value of the expression under the radical in (6.6.25) or (6.6.27). Generate figures like Figure 6.6,and experiment with different values of n. Try cases with stupid initial guesses, such as xo = M when M is close to zero and e is close to 1,and see if you can get the method to faill Compare the accelerated version of Newton's method having quartic convergence with the combination of (6.6.25) and (6.6.29).

9.Using (6.6.7),and with a suffciently good initial guess,using two iterations through (6.6.7)may be adequate; so it may be more efficient to run a program that uses precisely two iterations and dispenses with the test “IF ABs(F)<DEL ...".From Figure 6.6 it is clear that the initial guess xo= M\*+0.85oe will be adequate unless M\* is close to O or 2π, so for these cases different initial guesses must be devised. Consider M\*<0.1.

Show that if e is small, xo = M\* is adequate, while for e close to 1, xo \~ (6M\*)1/3. A formula that interpolates between these extremes is

$$
x _ { 0 } = M ^ { * } \div \left[ \left( 6 M ^ { * } \right) ^ { \frac { 1 } { 4 } / 3 } - M ^ { * } \right] e ^ { 2 } .
$$

Experiment with this and others, and find a similar formula for the cases $\mathbb { M } ^ { * } > 2 \pi - 0 . 1$ ：

# 6.7The f and g Functions

Let ro = r(to) and Vo = v(to) be the position and velocity vectors at time to of a body in Keplerian motion subject to the differential equation (6.2.3). We shall assume that these vectors are not parallel; consequently, the angular momentum of the orbit is not zero,and the orbit lies in a plane. Then if r(t)is the position vector at any time t, there exist unique scalars f and g such that

$$
\begin{array} { r } { \mathbf { \tilde { r } } ( \tilde { \mathbf { \Gamma } } ) = \tilde { f } \mathbf { r } _ { \mathbb { 0 } } \div g \mathbf { v } _ { \mathbb { 0 } } . } \end{array}
$$

f and g will depend on the times to and t, so (6.7.1) can be written more explicitlv as

$$
\begin{array} { r } { \bar { \mathbf { r } } ( t ) = \bar { f } ( t , t _ { 0 } ) \mathbf { r } ( t _ { 0 } ) + g ( t , t _ { 0 } ) \mathbf { v } ( t _ { 0 } ) . } \end{array}
$$

These scalar functions are independent of the reference system used to resolve the vectors. In particular, (6.7.2) is valid in the orbital reference system,where the components in the plane of the orbit are

$$
\begin{array} { r } { X ( t ) = f X ( t _ { 0 } ) + g \dot { X } ( t _ { 0 } ) , } \\ { Y ( t ) = f Y ( t _ { 0 } ) + g \dot { Y } ( t _ { 0 } ) . } \end{array}
$$

These can be solved for $f$ and $g$ when

$$
\begin{array} { l } { f = \displaystyle \frac { 1 } { D } [ X ( t ) \dot { Y } ( t _ { 0 } ) - Y ( t ) \dot { X } ( t _ { 0 } ) ] , } \\ { g = \displaystyle \frac { 1 } { D } [ Y ( t ) X ( t _ { 0 } ) - X ( t ) Y ( t _ { 0 } ) ] , } \\ { D = X ( t _ { 0 } ) \dot { Y } ( t _ { 0 } ) - Y ( t _ { 0 } ) \dot { X } ( t _ { 0 } ) = h . } \end{array}
$$

X(t),Y(t),X(to）,Y(to）, X(to）,Y(to) can be expressed in terms of the eccentric anomalies $\Xi$ and $\mathcal { E } _ { \mathfrak { d } }$ using (6.3.22) and (6.3.23).Substituting and simplifying, we find

$$
\begin{array} { l } { f = \displaystyle \frac { a } { r _ { 0 } } [ \cos ( E - E _ { 0 } ) - 1 ] + 1 , } \\ { g = \displaystyle \frac { 1 } { n } [ \sin ( E - E _ { 0 } ) - e \sin E + e \sin E _ { 0 } ] } \\ { = \displaystyle \frac { 1 } { n } - t _ { 0 } + \displaystyle \frac { 1 } { n } [ \sin ( E - E _ { 0 } ) - ( E - E _ { 0 } ) ] . } \end{array}
$$

To justify the second expression for g， consider Kepler's equation for the two

$$
\left. \begin{array} { c } { { \pi ( \frac { t } { t } - \widetilde { L } ) = \widetilde { L } - e \sin \widetilde { \cal E } , } } \\ { { \pi ( \dot { \bar { z } } _ { 0 } - T ) = \widetilde { \cal E } _ { 0 } - e \sin \widetilde { \cal E } _ { 0 } , } } \end{array} \right]
$$

and subtract the second from the first. Given formulas for f and g, (6.7.1) can be considered as the solution to the differential equation (6.2.3) with ro and vo as arbitrary constants: this is an important and useful expression. The velocity at time $\acute { \pmb { \updownarrow } }$ is found from

$$
\mathbf { v } ( t ) = \frac { \partial f ( t , t _ { 0 } ) } { \partial t } \mathbf { r } ( t _ { 0 } ) + \frac { \partial g ( t , t _ { 0 } ) } { \partial t } \mathbf { v } ( t _ { 0 } ) .
$$

Writing the partial derivatives of f and g as f, g, this can be written as

$$
\mathbf { v } \{ \pmb { \mathscr { t } } \} = \dot { \pmb { \mathscr { f } } } \{ \pmb { \mathscr { r } } _ { 0 } \pm \dot { \pmb { \mathscr { g } } } \mathbf { v } _ { 0 } .
$$

From(6.7.5）and (6.3.20）,we find

$$
\begin{array} { l } { { \dot { \vec { f } } = - \displaystyle \frac { a } { r } \frac { a } { r _ { 0 } } n \sin ( \vec { E } - \vec { E } _ { 0 } ) , } } \\ { { \dot { \vec { g } } = \displaystyle \frac { a } { r } [ \cos ( E - \vec { E } _ { 0 } ) - \vec { \bf i } ] + \vec { \bf i } . } } \end{array} \biggr ] 
$$

The f and g functions and their derivatives can also be expressed in terms of the true anomalies. Details are left as an exercise; the results are

$$
\begin{array} { r l } & { f = \frac { T } { p } [ \cos ( v - v _ { 0 } ) - 1 ] + 1 , } \\ & { g = \frac { T r _ { 0 } } { \sqrt { \mu p } } \sin ( v - v _ { 0 } ) , } \\ & { \dot { f } = - \sqrt { \frac { \mu } { p ^ { 3 } } } [ \sin ( v - v _ { 0 } ) + e \sin v - e \sin v _ { 0 } ] , } \\ & { \dot { g } = \frac { T _ { 0 } } { p } [ \cos ( v - v _ { 0 } ) - 1 ] + 1 . } \end{array}
$$

The f and g functions only came into prominence in the 1950's and the widespread use of high-speed computation. Up till then, they were “f and g series, expanded in powers of the time difference (t -to). We have the Taylor series

$$
\begin{array} { r } { \mathtt { r } ( \mathtt { t } ) = \mathtt { r } _ { 0 } + ( \mathtt { t } - \mathtt { t } _ { 0 } ) \dot { \mathtt { r } } _ { 0 } + \frac { 1 } { 2 } ( \mathtt { t } - \mathtt { t } _ { 0 } ) ^ { 2 } \ddot { \mathtt { r } } _ { 0 } + \frac { 1 } { 6 } ( \mathtt { t } - \mathtt { t } _ { 0 } ) ^ { 3 } \ddot { \mathtt { r } } _ { 0 } + \cdot \cdot \cdot } \end{array}
$$

$$
\begin{array} { r } { \ddot { \mathfrak { r } } _ { 0 } = - \frac { \mu \mathfrak { r } _ { 0 } } { \mathfrak { r } _ { 0 } ^ { 3 } } = - \sigma \mathfrak { r } _ { 0 } , } \end{array}
$$

$$
\begin{array} { r } { \ddot { \mathtt { r } } _ { 0 } = - \frac { \mu \mathtt { V } _ { 0 } } { r _ { 0 } ^ { 3 } } \div \frac { 3 \mu \mathtt { F } _ { 0 } \dot { r } _ { 0 } } { r _ { 0 } ^ { 4 } } = - \sigma \mathtt { v } _ { 0 . } \overset { , } { + } 3 \sigma \tau \mathtt { r } _ { 0 } , } \end{array}
$$

where

$$
\begin{array} { r } { \sigma = \frac { \mu } { r _ { 0 } ^ { 3 } } \mathrm { a n d } \tau = \frac { \dot { \bar { r } } _ { 0 } } { r _ { 0 } } = \frac { \mathbf { r } _ { 0 } \cdot \mathbf { v } _ { 0 } } { r _ { 0 } ^ { 2 } } . } \end{array}
$$

Substituting into (6.7.10),and rearranging, we find

$$
\begin{array} { r } { \mathbf { r } ( t ) = \left( \mathbb { i } - \frac { 1 } { 2 } \sigma ( t - \dot { \tau } _ { 0 } ) ^ { 2 } + \frac { 1 } { 2 } \sigma \tau ( \dot { \tau } - \dot { \tau } _ { 0 } ) ^ { 3 } + \cdots \right) \mathbf { r } _ { 0 } } \\ { + \left( ( \dot { \tau } - \dot { \tau } _ { 0 } ) - \frac { 1 } { 6 } \sigma ( \dot { \tau } - \dot { \tau } _ { 0 } ) ^ { 3 } + \cdots \right) \mathbf { v } _ { 0 } . } \end{array}
$$

Comparing this with (6.7.1),we can write

$$
\left. \begin{array} { l } { { f = 1 - { \frac { 1 } { 2 } } \sigma ( t - t _ { 0 } ) ^ { 2 } + { \frac { 1 } { 2 } } \sigma \tau ( t - t _ { 0 } ) ^ { 3 } + \cdots , } } \\ { { g = ( t - t _ { 0 } ) - { \frac { 1 } { 6 } } \sigma ( t - t _ { 0 } ) ^ { 3 } + \cdots . } } \end{array} \right]
$$

These are the $f$ and $g$ series.If $\mathtt { r _ { 0 } }$ is known,but not $\mathfrak { v } _ { 0 }$ ,then the leading terms in the series are useful, as we shall see when we consider the determination of orbits. But as soon as $\mathbf { v _ { 0 } }$ is known,then the $\pmb { \hat { \hat { \jmath } } }$ and $g$ functions are accessible, and should be used.

# Problems

1.Find expressions for the $\hat { \pmb { \xi } }$ and $g$ functions and their derivatives in the cases of hyperbolic and parabolic motion.

2.Show that

$$
f = \sqrt { \frac { \mu } { p } } \tan \frac { \frac { 1 } { 2 } } { 2 } ( v - v _ { 0 } ) \left[ \frac { 1 - \cos ( v - v _ { 0 } ) } { p } - \frac { 1 } { r } - \frac { 1 } { r _ { 0 } } \right] .
$$

3. Find the value of $f _ { \dot { \mathcal { G } } } - f _ { \mathcal { G } }$

4. Show that $\ddot { f } = - \mu f / \nu ^ { 3 } , \ddot { g } = - \mu g / \gamma ^ { 3 }$

5.Show that $\xi = - \frac { \partial { g } } { \partial { \ddag } _ { 0 } }$ and $\frac { \partial f } { \partial t _ { 0 } } = \mu g / \tau _ { 0 } ^ { 3 }$

6. Define the matrix $\mathbb { H } ( t , \ t _ { 0 } )$ by

$$
\begin{array} { r } { \bar { H } ( t , t _ { 0 } ) = \left[ \begin{array} { c c } { \bar { f } ( t , { t _ { 0 } } ) } & { g ( t , { t _ { 0 } } ) } \\ { \frac { \partial } { \partial t } \bar { f } ( t , { t _ { 0 } } ) } & { \frac { \partial } { \partial t } g ( t , { t _ { 0 } } ) } \end{array} \right] . } \end{array}
$$

Show that $H ( t _ { 2 } , t _ { 1 } ) \dot { \mathcal { H } } ( t _ { 1 } , t _ { 0 } ) = H ( t _ { 2 } , t _ { 0 } )$ and that $\check { \vec { z } } \vec { z } ^ { - 1 } \{ \vec { \tau } , \vec { \tau } _ { 0 } \} = \check { \vec { z } } \vec { z } \langle \vec { \tau } _ { 0 } , \vec { \tau } \rangle$ Show also that $\breve { H }$ is symplectic,i.e.,that $\tilde { \mathcal { H } } ^ { \mathcal { T } } \tilde { \mathcal { J } } \tilde { \mathcal { Z } } = \tilde { \mathcal { J } }$ ，where $\tilde { \pmb { j } }$ is the matrix

$$
{ \bf \underline { { \hat { \Pi } } } } ^ { \mathrm { ~ \tiny ~ { ~ \hat { ~ } { ~ \delta ~ } ~ } ~ } } \big [ \begin{array} { c } { { { \bf \underline { { \hat { \Pi } } } } { \bf \underline { { \hat { \Pi } } } } } } \\ { { - { \bf \bar { \Pi } } { \bf \underline { { \hat { \Pi } } } } } } \end{array} \big ] .
$$

# 6.8The Initial Value Problem I

The problem to be addressed is:“Given initial conditions rg = r(to） and Vo=v(to) for a time to,and given a second time t,find r(t) and v(t)”.In this section we shall consider only initial conditions that lead to an elliptic orbit.

From the initial conditions we can calculate ro = |rol,u,and the scalar product

$$
{ \mathfrak { U } } = { \mathfrak { r } } _ { \mathfrak { V } } \circ { \mathfrak { V } } _ { \Omega } .
$$

From the energy integral, we can solve for $\mathfrak { a }$

$$
a = \left( \frac { 2 } { \tau _ { 0 } } - \frac { v _ { 0 } ^ { 2 } } { \mu } \right) ^ { - 1 } .
$$

If ais negative, then stop immediately. Otherwise, find the mean motion n from

$$
\mathfrak { R } = \sqrt { \frac { \mu } { { a } ^ { 3 } } } .
$$

Next,from (6.3.8)and (6.3.21） we have

$$
r _ { 0 } = a ( 1 - e \cos E _ { 0 } ) \mathrm { a n d } u = r _ { 0 } \dot { r } _ { 0 } = e n a ^ { 2 } \sin E _ { 0 } .
$$

and

$$
\begin{array} { l } { { E C = e \cos \displaystyle E _ { 0 } = 1 - r _ { 0 } / a , \displaystyle \Bigg ] } } \\ { { } } \\ { { E S = e \sin \displaystyle E _ { 0 } = u / n a ^ { 2 } . \quad } } \end{array}
$$

Note that e can be found from these; it will be needed when making an initial xuess for the solution of Kepler's equation.

Writing down Kepler's equation for the times $t _ { \Updownarrow }$ and $\ddagger$ and subtracting one from the other,see (6.7.6),we find

$$
\begin{array} { r } { n \Delta \dot { t } = \Delta \dot { E } - e \sin \dot { E } + e \sin \dot { E } 0 , } \end{array}
$$

where

$$
\Delta t = t - { i _ { 0 } } , \quad \mathrm { a n d } \quad \Delta E = E - E _ { 0 } .
$$

Then $\mathcal { E } = \Delta \mathcal { E } + \mathcal { E } _ { 0 }$ so (6.8.5) can be rewritten as

$$
n \Delta t = \Delta \dot { E } - e \cos \dot { E } _ { 0 } \sin \Delta \dot { E } + e \sin \dot { E } _ { 0 } ( \mathbb { 1 } - \cos \Delta E ) .
$$

This is the new form for Kepler's equation. Notice that for a circular orbit the difference $\Delta \Xi$ canalways be found in spite of the fact that individual anomalies are not defined. The solution of (6.8.7) for the unknown x = △E,so that

$$
\begin{array} { r } { f ( x ) = x - E C \sin x + E S ( 1 - \cos x ) - n \Delta t = 0 , } \end{array}
$$

is as straightforward as for the basic form of Kepler's equation. But the initial guess Tn requires more care. Since

$$
\begin{array} { r } { z = \Delta \mathcal { E } = \Xi - \Xi _ { 0 } , } \end{array}
$$

then

$$
\begin{array} { r l } & { x _ { 0 } = ( \dot { M } + \sigma \dot { k } e ) - ( \dot { M } _ { 0 } + e \sin \dot { E } _ { 0 } ) } \\ & { \quad = \mathfrak { R } \dot { \Delta t } + \sigma \dot { k } e - e \sin \dot { E } _ { 0 } . } \end{array}
$$

To identify g we need to know the sign of sin M. Now

$$
\begin{array} { r l } & { \vec { M } = n ( t - T ) } \\ & { \quad = n ( t - t _ { 0 } ) + n ( t _ { 0 } - T ) } \\ & { \quad = n \Delta t + ( E _ { 0 } - e \sin E _ { 0 } ) . } \end{array}
$$

We want to avoid explicitly finding $E _ { \mathbb { 3 } }$ But we can write

$$
\begin{array} { r l } & { \sin M = \sin  { { \cal E } } _ { 0 } \cos ( n \Delta t - e \sin  { { \cal E } } _ { 0 } ) + \cos  { { \cal E } } _ { 0 } \sin ( n \Delta t - e \sin  { { \cal E } } _ { 0 } ) } \\ & { \phantom { \sin  { { \cal E } } _ { 0 } } = \frac { 1 } { e } [ { \cal E } S \cos ( n \Delta t - { \cal E } S ) + { \cal E } C \sin ( n \Delta t - { \cal E } S ) ] . } \end{array}
$$

So the sign of sin M is the same as the sign of the quantity in the brackets on the right of (6.8.10). If e is smaller than some quantity,such as 0.1, it is quicker to let $x _ { 0 } = n \Delta t$

Once $x = \Delta \xi$ has been found,the $f$ and $\mathscr { G }$ functions and their derivatives can be found from

$$
\begin{array} { r l } & { f = \cfrac { a } { r _ { 0 } } { \left( \cos { \Delta E } - 1 \right) } + 1 , } \\ & { g = \Delta t + \cfrac { 1 } { n } { \left( \sin { \Delta E } - \Delta E \right) } , } \\ & { \dot { f } = - \cfrac { a } { r } \cfrac { a } { r _ { 0 } } n \sin { \Delta E } , } \\ & { \dot { g } = \cfrac { a } { r } { \left( \cos { \Delta E } - 1 \right) } + 1 . } \end{array}
$$

To find $j$ and ${ \dot { g } } , \ r = r ( { \dot { \bar { \tau } } } )$ is needed. This might be found from

$$
\begin{array} { r l } & { \frac { \vec { t } ^ { * } } { \alpha } = \mathbb { i } - e \cos { \cal E } } \\ & { \quad = \mathbb { i } - e \cos ( \Delta { \cal E } + { \cal E } _ { 0 } ) } \\ & { \quad = \mathbb { 1 } - E C \cos \Delta { \cal E } + E S \sin \Delta { \cal E } . } \end{array}
$$

But Kepler's equation in the form (6.8.8) has been solved,and $f ^ { i } ( x )$ is equal to r/a.So this quantity,as well as C = cosx and S = sinx,can be taken from the subroutine for solving Kepler's equation and used in the construction of(6.8.11）.Finally, $\mathfrak { X } _ { \mathrm { ~ \left\{ ~ \mathfrak { t } ~ \right\} ~ } } ^ { \prime }$ and $\forall \{ t \}$ are found from

$$
\mathbf { r } ( t ) = f \dot { \mathbf { r } } _ { 0 } + g \mathbf { v } _ { 0 } , ~ \mathbf { v } ( t ) = \dot { f } \mathbf { r } _ { 0 } + \dot { g } \mathbf { v } _ { 0 } .
$$

A program listing follows. A good way to debug your program is to run it once and then transform the output,r(t),v(t),into initial conditions,reverse the sign of △t,and run the program again. Lines 410-430 do this.

10 REN THE INITIAL VALUE PROBLEN FOR ELLIPTIC MOTION.   
20DEFDBL A-,O-Z:DEFINT   
30 CLS   
40INPUT ENTER U；HU:PRINT   
50INPUTENTER THEINIIAL TIE,TOTOPINT   
6PRINT ENTER COHPONENTS OF THE INITIAL POSITION,   
X0，YO，Z0   
70 INPUT XOYOZOPRINT   
8 PRINT ENTER CONPONENTS OF THE INITIAL VELOCITY,   
XvO,YVO,zvO   
90INPUT XVO,YVO,ZVO：PRINT   
100INPUT ENTER THE FINAL TIHE,T ；T :PRINT   
110PI=3.141592653589793#   
120NB=0   
130 REH FOR THE DEBUGGING RUN,WITH INITIAL AND FINAL   
140 REK CONDITIONS REVERSED, $\sin = 1$   
150RO=SQR（XO\*XO+YO\*YO+ZO\*ZO）   
160VOS=XVO\*XVO+YVO\*YVO+ZVO\*VO   
170U=XO\*XVO+YO\*YVO÷ZO\*ZVO:REN（6.8.1）   
180A=1#/（2#/RO-VOS/MU):REN（6.8.2）   
190IFA<O THEN 47O:REN HYPERBOLIC HOTION.   
200EN=SQR(HU/(A\*\*A)）   
210EC=1-R0/A   
220ES=U/(EN\*A\*）:REM（6.8.4）   
230E=SQR（EC\*EC+ES\*ES）   
240DT=T-TO   
250 PRINT AE   
260 GOSUB 6OO :REN SOLVE KEPLER'S EQUATION   
270F=（A/RO）\*（C-1#）+1   
280G=DT÷(S-X）/EN、   
290FDOT=-（A/（RO\*FP)）\*EN\*S   
300GDOT=（C-1#）/FP+1#:RE（6.8.11）   
310X=XO\*F+XVO\*G   
320Y=YO\*F+YVO\*G   
330Z=ZO\*F+ZVO\*G:REN_(6.7.1）   
340XV=XO\*FDOT+XVO\*GDOT   
350YV=YO\*FDOT+YVO\*GDDT   
360ZV=ZO\*FDOT÷ZVO\*GDOT:REH（6.7.7）   
370 PRINT PINAL COHPONENTS OF POSITION ARE "；X ,Y,Z   
380PRINT   
390 PRINT FINAL COMPONENTS OF VELOCITY ARE  ；XV ,YV ,ZV   
400IFNB $\lneq$ 1THEN_460   
410 x0=x:Y0=Y:Z0=Z   
420xvo=xv:Yvo=Yv:zvO=ZV   
430TT=TO:TO=T:T=TT:NB=1: PRINT:GOTO 150   
440 REH SVITCHING TIHES AND COORDINATES IS   
450 REN INCLUDED FOR DEBUGGING.   
460END   
470 PRINT "HYPERBOLIC ORBIT.TRY AGAIN!   
480 END   
600 REN SOLUTION OF KEPLER'S EQUATION IN THE FORH（6.8.8   
610 REH USING ACCELERATED NEWTONS HETHOD,（6.6.7）.   
620DT=DT-INT（EN\*DT/（2#\*PI））\*(2\*PI）/EN   
630Y=EN\*DT-ES   
640 SIGHA=SGN（ES\*COS(Y)+EC\*SIN(Y)）   
650X=Y+SIGHA\*.85#\*E-ES   
660 REK CALCULATION OF INITIAL GUESS.   
670 NC=0   
680 DEL =1E-14   
690S=sIN（x）:C=COS(x）   
700F= X-EC\*S+ES\*(1-C)- EN\*DT   
710FP=1#-EC\*CES\*S   
720FPP=EC\*S+ES\*C   
730FPPP =EC\*C-ES\*S :RE DERIVATIVES OFF   
740 DX=-/FP   
0==/+DP/）DXDX\*FPP/6）   
770 X=X + DX:REN QUARTIC CONVERGENCE.   
8   
800 G0T0 690   
810 RETURN   
820 PRINT "THE SOLUTION OF KEPLER'S EQUATION FAILED."   
830 RETURN

Example:

$$
\begin{array} { r l } & { \mu = 1 , t _ { 0 } = 0 , t = 1 . \ \mathbf { r } _ { 0 } = ( 1 , \ 1 , \ - . 1 ) , \ v _ { 0 } = ( - . 1 , \ 1 , \ 2 ) . } \\ & { \mathbf { r } = ( . 4 6 6 0 8 0 7 8 4 6 5 3 9 2 3 4 , \ . 9 0 0 6 1 1 \ 2 3 4 9 0 7 7 2 3 6 , \ . 1 1 4 0 4 5 9 8 0 6 6 7 3 2 3 } \\ & { \mathbf { v } = ( - . 8 7 6 5 9 4 4 3 6 8 5 2 5 0 8 4 , \ . 4 7 3 1 5 6 6 0 4 9 7 9 4 7 8 6 , \ . 1 9 3 1 5 9 4 9 2 4 4 3 9 6 } \end{array}
$$

# 6.9Universal Variables

Recoiling in horror when $\mathfrak { a }$ is negative (as in the preceding section) should not happen. Equally,writing special routines for every possible type of orbit is not necessary. What we shall do in this section is to look for and find a single set of formulas which will solve the equation

$$
\displaystyle \ddot { \bar { \Sigma } } \div \frac { \mu \mathfrak { X } } { \mathfrak { X } ^ { 3 } } = \mathfrak { 0 }
$$

for any set of initial conditions.Obviously Kepler's equation in the form

$$
\dot { \kappa } \alpha ^ { - 3 / 2 } ( \dot { \iota } - \mathcal { T } ) = \mathcal { E } - e \sin \mathcal { E }
$$

would not qualify,since it is meaningless for negative $\pmb { \mathcal { E } }$ One way to hunt for universal formulas is to play with formulas such as (6.9.2) as follows:

$$
\begin{array} { r l } & { k ( t - T ) = a ^ { 3 / 2 } \left[ E - e \left( E - \frac { E ^ { 3 } } { 3 ! } + \frac { E ^ { 5 } } { 5 ! } - \frac { E ^ { 7 } } { 7 ! } + \cdots \right) \right] } \\ & { \quad \quad \quad = a ^ { 3 / 2 } \left[ ( 1 - e ) E + e \left( \frac { E ^ { 3 } } { 3 ! } - \frac { E ^ { 5 } } { 5 ! } + \frac { E ^ { 7 } } { 7 ! } - \cdots \right) \right] } \\ & { \quad \quad = q ( \sqrt { a } E ) + e \left[ \frac { ( \sqrt { a } E ) ^ { 3 } } { 3 ! } - \frac { 1 } { a } \frac { ( \sqrt { a } E ) ^ { 5 } } { 5 ! } + \frac { 1 } { a ^ { 2 } } \frac { ( \sqrt { a } E ) ^ { 7 } } { 7 ! } - \cdots \right] . } \end{array}
$$

Here $q = a \{ 1 - e \}$ Let $\sqrt { a } E = x$ ；then Kepler's equation takes the form

$$
k ( t - T ) = q x + e \left( { \frac { x ^ { 3 } } { 3 ! } } - { \frac { \mathbb { i } } { \alpha } } { \frac { x ^ { 5 } } { 5 ! } } + { \frac { 1 } { \alpha ^ { 2 } } } { \frac { x ^ { 7 } } { 7 ! } } - \cdots \right) .
$$

This formula is valid for all values of $\pmb { \mathcal { Q } }$ and $\pmb { \mathcal { e } }$ in particular,it is good for parabolic orbits where $z / \alpha = 0$ The series converges absolutely for all ${ \mathcal { X } } .$ whether $\pmb { \mathcal { Q } }$ is positive or negative, and the equation can be solved for $\pmb { \mathcal { Z } }$ using methods already discussed.To see how thisvalue of $\pmb { \mathcal { X } }$ could beused for further calculation,consider

$$
\begin{array} { l } { X = a ( \cos { \mathcal { E } } - e ) } \\ { = a \left( 1 - { \frac { 1 } { a } } { \frac { x ^ { 2 } } { 2 ! } } + { \frac { 1 } { a ^ { 2 } } } { \frac { x ^ { 4 } } { 4 ! } } - \cdots e \right) , } \end{array}
$$

and

$$
\begin{array} { l } { \displaystyle { Y = \alpha \sqrt { 1 - e ^ { 2 } } \sin {  { \cal E } } } } \\ { \displaystyle { \phantom { \frac { 1 } { 1 } } = \sqrt { a ( 1 - e ^ { 2 } ) } \left( x - \frac { 1 } { a } \frac { x ^ { 3 } } { 3 ! } + \frac { 1 } { a ^ { 2 } } \frac { x ^ { 5 } } { 5 ! } - \cdots \right) . } } \end{array}
$$

These are “universal formulas” and x is an example of a “universal variable." Other formulas can be manipulated in thie same way.

Obviously,we need to use a systematic approach. In doing so,we shall find new functions and new.formulas; we shall also have to learn how to compute the functions. Your patience is required in following the derivations: you will berewarded.Let us define a new independent variable, s,using the differential relation

$$
\ddot { a } \dot { \varepsilon } = \gamma \dot { a } \dot { s } .
$$

It is obvious that s will be proportional to the eccentric anomaly. (6.9.3) can include a constant factor for greater generality, this can always be inserted later; the derivations will look simpler with (6.9.3） as it is.We shall work with times tg and t,and will assume that s= O at the time to. Then we can write

$$
\displaystyle { \varepsilon - t _ { 0 } = \int _ { 0 } ^ { s } \gamma ( \overline { { s } } ) d \overline { { s } } } ,
$$

$$
\int _ { t _ { 0 } } ^ { t } d \overline { { t } } j _ { \uparrow } r ( \overline { { t } } ) = s .
$$

First we shall derive differential equations in terms of this new variable. Let a.prime stand for differentiation with respect to s. Then, by the chain rule,

and

$$
\begin{array} { l } { { \displaystyle { \frac { d } { d \dot { \varepsilon } } = \frac { d s } { d t } \frac { d } { d s } = \frac { \ddot { 1 } } { \gamma } \frac { d } { d s } } } } \\ { { \displaystyle { \frac { d ^ { 2 } } { d \dot { \varepsilon } ^ { 2 } } = \frac { 1 } { r } \frac { d } { d s } \left( \frac { 1 } { r } \frac { d } { d s } \right) = \frac { 1 } { r ^ { 2 } } \frac { d ^ { 2 } } { d s ^ { 2 } } - \frac { 1 } { r ^ { 3 } } r ^ { \prime } \frac { d } { d s } . } } } \end{array}
$$

Alternatively,

and

$$
\begin{array} { l } { { \displaystyle { \frac { d } { d s } } = r { \frac { d } { d t } } } } \\ { { } } \\ { { { \displaystyle { \frac { d ^ { 2 } } { d s ^ { 2 } } } = r ^ { 2 } { \frac { d ^ { 2 } } { d t ^ { 2 } } } + r { \dot { r } } { \frac { d } { d t } } } . } } \end{array}
$$

Then (6.9.1) can be written as

$$
{ \underline { { \mathfrak { r } } } } ^ { 3 / } - { \frac { { \mathfrak { r } } ^ { 7 } } { \mathfrak { r } } } ^ { 7 } + \mu { \frac { \mathfrak { r } } { \mathfrak { r } } } = \mathbb { 0 } .
$$

Now from (6.2.5),

$$
{ \begin{array} { r l } & { \mathbf { P } = { \dot { \mathbf { r } } } \times \mathbf { h } - \mu { \dot { \mathbf { r } } } } \\ & { \quad = { \dot { \mathbf { r } } } \times ( \mathbf { r } \times { \dot { \mathbf { r } } } ) - { \frac { \mu \mathbf { r } } { r } } } \\ & { \quad = ( { \dot { \mathbf { r } } } ) ^ { 2 } \mathbf { r } - ( r { \dot { r } } ) { \dot { \mathbf { r } } } - { \frac { \mu \mathbf { r } } { r } } } \\ & { \quad = \mu ( { \frac { 2 } { r } } - { \frac { 1 } { a } } ) \mathbf { r } - ( r r ^ { \prime } ) { \frac { \mathbf { r } ^ { \prime } } { r ^ { 2 } } } - { \frac { \mu \mathbf { r } } { r } } } \\ & { \quad = { \frac { \mu \mathbf { r } } { r } } - { \frac { r ^ { \prime } \mathbf { r } ^ { \prime } } { r } } - \left( { \frac { \mu } { a } } \right) \mathbf { r } } \\ & { \quad = - \mathbf { r } ^ { \prime \prime } - \alpha \mathbf { r } , } \end{array} }
$$

from (6.9.8). Here we have set

$$
\alpha = \frac { \mu } { z } = \frac { 2 \mu } { \tau } - \mathtt { i } ^ { 2 } .
$$

Finally,

$$
{ \bf r } ^ { \prime \prime } + \alpha \mathfrak { x } = - \frac { \mathfrak { P } } { \mathfrak { s } } .
$$

The problem has been reduced to one having no singularity,and the new differential equation is the harmonic oscillator.Mathematically, the problem is said to have been “regularized.” It will be convenient to differentiate (6.9.10） once more and write it as

$$
{ \boldsymbol { \mathfrak { x } } } ^ { f \prime \prime } + { \boldsymbol { \alpha } } { \boldsymbol { \mathfrak { x } } } ^ { \prime } = { \boldsymbol { \mathfrak { Q } } } .
$$

Next, consider $\vec { r } ^ { \prime } = r \bar { r } = \vec { \bf { r } } \cdot \dot { \bf { \bar { r } } }$ Then

$$
\begin{array} { r } { r ^ { \prime \prime } = r ( \dot { \bar { r } } \cdot \dot { \bar { r } } + \mathbf { r } \cdot \ddot { \bar { \varepsilon } } ) = \tau \left( \frac { \dot { \mathcal { Z } } \mu } { \bar { r } } - \frac { \dot { \mu } } { \bar { \alpha } } - \frac { \dot { \mu } } { \bar { r } } \right) = \mu - \alpha \bar { r } , } \end{array}
$$

so that

$$
r ^ { \prime \prime } + \alpha \tau = \mu , \quad \mathrm { a r s d } \quad r ^ { \prime \prime \prime } + \alpha r ^ { \prime } = 0 .
$$

Since $\ z = f \mathbf { r } _ { \mathbf { \Phi } } \mathbf { \Phi } _ { \mathbf { \Phi } } + g \mathbf { v } _ { \mathbf { \Phi } }$ , we find from (6.9.11)

$$
( f ^ { \prime \prime \prime } \div \alpha f ^ { \prime } ) \boldsymbol { \tau } _ { 0 } + ( g ^ { \prime \prime \prime } \div \alpha g ^ { \prime } ) \boldsymbol { \tau } _ { 0 } = 0 .
$$

$\yen 0$ and $\yen 0$ are arbitrary,so that

$$
f ^ { \prime \prime \prime } + \alpha f ^ { \prime } = 0 \mathrm { \Large ~ \ a n d ~ } g ^ { \prime \prime \prime } \div \alpha g ^ { \prime } = 0 .
$$

These are the new differential equations that we need.Next, we must turn our attention to the solution of the harmonic oscillator, but without considering any special cases.For a start, note that the solution of

$$
w ^ { \prime \prime } \ne \alpha w = 0
$$

can be written in series as

$$
w = w _ { 0 } \left( 1 - \alpha { \frac { s ^ { 2 } } { 2 ! } } + \alpha ^ { 2 } { \frac { s ^ { 4 } } { 4 ! } } - \cdots \right) + w _ { 1 } \left( s - \alpha { \frac { s ^ { 3 } } { 3 ! } } + \alpha ^ { 2 } { \frac { s ^ { 5 } } { 5 ! } } - \cdots \right) ,
$$

and that these series converge for all s regardless of α. To discuss the solution systematically we now introduce the“Stumpff functions”:

$$
c _ { k } ( x ) = { \frac { 1 } { k ! } } - { \frac { x } { ( k + 2 ) ! } } + { \frac { x ^ { 2 } } { ( k + 4 ) ! } } - \cdots , k = 0 , 1 , 2 , \ldots
$$

These series all converge absolutely for all $\pmb { \mathcal { Z } }$ Note that:

$$
\begin{array} { l } { \displaystyle \mathrm { F o r ~ } x > 0 \mathrm { , t h e n ~ } c _ { 0 } ( x ) = \cos \sqrt { x } \mathrm { , ~ } \quad c _ { 1 } ( x ) = \frac { \sin \sqrt { x } } { \sqrt { x } } \mathrm { , ~ } } \\ { \displaystyle } \\ { \displaystyle \mathrm { f o r ~ } x < 0 \mathrm { , t h e n ~ } c _ { 0 } ( x ) = \cosh \sqrt { - x } \mathrm { , ~ } c _ { 1 } ( x ) = \frac { \sinh \sqrt { - x } } { \sqrt { - x } } \mathrm { . ~ } } \end{array}
$$

and

The functions satisfy the recursion relations

$$
x c _ { k + 2 } ( x ) = \frac { \frac { 1 } { 4 } } { k ! } - c _ { k } ( x ) , k = 0 , 1 , 2 , \ldots .
$$

Before applying these functions we must acquire the ability to compute them. For our purposes we shall need co,C1, C2 and cg. It is most efficient to compute c2 and c3 by series and then use the recursion formula to find ci and co.(Make sure that you understand why this is so.） It is inefficient to use the series except for small values of the argument; but if the input argument is too large, it can be reduced by using “half-angle” formulas, found as follows.

Since $\cos ( 2 y ) = 2 \cos ^ { 2 } y - \frac { 1 } { 2 }$ ,then,from (6.9.15）,

$$
c _ { 0 } ( 4 y ^ { 2 } ) = 2 [ c _ { 0 } ( y ^ { 2 } ) ] ^ { 2 } - 1 ,
$$

$$
c _ { 0 } ( 4 x ) = 2 [ c _ { 0 } ( x ) ] ^ { 2 } - 1 ,
$$

a formula that continues to be valid if $\pmb { \mathcal { X } }$ is negative. Also $\sin 2 y = 2 \sin y \cos y .$ 50 ${ \frac { \sin 2 y } { 2 y } } = { \frac { \sin y } { y } } \cos y$ and then

$$
c _ { \mathbb { i } } ( 4 y ^ { 2 } ) = c _ { \mathbb { 0 } } ( y ^ { 2 } ) c _ { \mathbb { i } } ( y ^ { 2 } )
$$

$$
c _ { 1 } ( 4 x ) = c _ { 0 } ( x ) c _ { \check { \bot } } ( x ) .
$$

$$
c _ { 2 } ( { \scriptstyle \frac { 4 } { 2 } } x ) = { \scriptstyle \frac { 1 } { 2 } } [ c _ { 1 } ( x ) ] ^ { 2 } , \quad .
$$

and

$$
\begin{array} { r } { c _ { 3 } ( 4 x ) = \frac { 1 } { 4 } c _ { 2 } ( x ) \div \frac { 1 } { 4 } c _ { 0 } ( x ) c _ { 3 } ( x ) , } \end{array}
$$

Suppose that the series for c2 and cgs are only to be used for values of x where $| x | < X M$ The flowchart 6.1 shows a possible scheme for reducing $\mathscr { x }$ and then restoring the original value, while computing the $\mathcal { C } _ { \bar { 2 } }$

The series might be found using a loop that would include a test to terminate it when the necessary accuracy was achieved. Or XM can be chosen once and for all, and the consequent number of terms found in order to guarantee double precision accuracy.For instance,if XM= 0.1,then

$$
\begin{array} { r l } & { c _ { 2 } ( \boldsymbol { x } ) \simeq \displaystyle \frac { 1 } { 2 ! } - \frac { 1 } { 4 ! } \boldsymbol { x } + \frac { 1 } { 6 ! } \boldsymbol { x } ^ { 2 } - \frac { 1 } { 8 ! } \boldsymbol { x } ^ { 3 } + \frac { 1 } { 1 0 ! } \boldsymbol { x } ^ { 4 } - \frac { 1 } { 1 2 ! } \boldsymbol { x } ^ { 5 } + \frac { 1 } { 1 4 ! } \boldsymbol { x } ^ { 6 } } \\ & { \qquad = \displaystyle \frac { 1 } { 2 } \left( 1 - \frac { x } { 3 * 4 } \left( 1 - \frac { x } { 5 * 6 } \left( 1 - \frac { x } { 7 * 8 } \right. \right. \right. } \\ & { \qquad \left. \left. \left. \left( 1 - \frac { x } { 9 * 1 0 } \left( 1 - \frac { x } { 1 1 * 1 2 } \left( 1 - \frac { x } { 1 3 * 1 4 } \right) \right) \right) \right) \right) \right) } \\ & { \qquad = ( 1 - x ( 1 - x ( 1 - x ( 1 - x ( 1 - x ( 1 - x / 1 8 2 ) / 1 3 2 ) / 9 0 ) / 5 6 ) / 3 0 ) / 1 2 ) / 2 . } \end{array}
$$

Similarly,

$$
c _ { 8 } ( x ) \simeq \left( 1 - x \big ( 1 - x \big ( 1 - x \big ( 1 - x \big ( 1 - x \big ( 1 - x / 2 1 0 \big ) / 1 5 6 \big ) / 1 1 0 \big ) / 7 2 \big ) / 4 2 \big ) / 2 0 \right) / 6 .
$$

There follows a listing for a subroutine for calculating the Stumpff functions (lines 3000 to 3180) and also a program for testing the calculations using (6.9.15). However you set up your program, debug it very carefully. Your subroutine will gain you independence from some conventional functions and give you considerable versatility.

the derivation of which is left to the reader.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0081-0120/ocr/images/c4cbb49c89438fc7722debcdea18af915e6a8f768e29e6b088ea728eb39a280d.jpg)

REM THIS PROGRAN TESTS THE CALCULATION OF THE STUMPFF REM FUNCTIONS USING SERIES AND RECURSION,AGAINST REH TRIGONOHETRIC OR HYPERBOLIC FUNCTIONS,（6.9.15）. CLS   
DEFDBL A-H,O-Z :DEFINT   
INPUT ENTER A VALUE FOR THE ARGUMENT X"；X   
GOSUB 3000   
80 IFX<O#THEN100   
90P=SQR（X):Q=COS(P):R=SIN（P）/P:GOTO 120   
100P=SQR（-x)Q=（EXP（P）+EXP（-P）/2#   
$=$ Ci ； CHECK=   
C2 ；   
3000=0   
3010 XM=.1\*   
3020IF ABSX)<XH THEN 3060   
3030=N+1   
3040X=X/4#   
3050GOT03020   
3060C2=（1-X\*（1-X\*（1-X\*（1-X\*(1-X\*   
（1-x/182\*)/132#)/90#)/56#)/30）/12#)/2#   
3070C3=（1-X\*（1#-X\*（1-X\*（1-X\*（1-X\*   
（1#-X/210#)/156#)/110#)/72\*)/42#)/20#)/6   
3080 C1= 1#-X\*C3   
3090 C0=1-X\*C2   
3100IFN=O THEN3180   
3110 $z = z - 1$   
心

# Flowchart 6.1

3120C3=（C2+CO\*C3）/4#  
3130C2=C1\*C1/2#  
3140C1=C0\*Ci  
3150 C0=28\*C0\*C0-1#  
3160X=X\*48  
3170 G0TO 3100  
3180 RETURN

At last we are ready to apply these functions. Let

$$
{ \mathfrak { x } } = \alpha s ^ { 2 } .
$$

Verify that

and

$$
\begin{array} { l } { { \displaystyle \frac { d } { d s } [ c _ { 0 } ( \alpha s ^ { 2 } ) ] = - \alpha s c _ { 1 } ( \alpha s ^ { 2 } ) , \ } } \\ { { \displaystyle } } \\ { { \displaystyle \frac { d } { d s } [ s ^ { k + 1 } c _ { k + 1 } ( \alpha s ^ { 2 } ) ] = s ^ { k } c _ { k } ( \alpha s ^ { 2 } ) , \ { \displaystyle \varepsilon } = 0 , 1 , 2 , \ldots ] } } \end{array}
$$

Then verify that each of

$$
1 , s c _ { 1 } ( \alpha s ^ { 2 } ) , s ^ { 2 } c _ { 2 } ( \alpha s ^ { 2 } )
$$

is a solution of $v ^ { \prime \prime \prime } \partial ^ { \prime } \tau ^ { \prime } = 0$ and that the three functions are linearly independent.Then the general solution of that equation is

$$
r ( s ) = r _ { 0 } + r _ { 0 } ^ { \prime } s c _ { \tt I } ( \alpha s ^ { 2 } ) + r _ { 0 } ^ { \prime \prime } s ^ { 2 } c _ { 2 } ( \alpha s ^ { 2 } ) ,
$$

where $r _ { G } , r _ { \gimel } ^ { \beta }$ and $r _ { 0 } ^ { \prime \prime }$ are constants. To identify them, we have

$$
\left. \begin{array} { l } { r ( \dot { \varepsilon } _ { 0 } ) = r _ { 0 } , } \\ { r ^ { i } ( \dot { \varepsilon } _ { 0 } ) = r _ { 0 } ^ { i } = r _ { 0 } \dot { r } _ { 0 } , \mathrm { b y } ( 6 . 9 . 7 ) , } \\ { r ^ { i \prime } ( \dot { \varepsilon } _ { 0 } ) = \tau _ { 0 } ^ { i \prime } = \mu - \alpha \dot { r } _ { 0 } , \mathrm { b y } ( 6 . 9 . \dot { 1 } 2 ) . } \end{array} \right]
$$

Then

$$
\begin{array} { l } { r = r _ { 0 } + r _ { 0 } \dot { r } _ { 0 } s c _ { \frac { 1 } { 2 } } ( \alpha s ^ { 2 } ) + ( \mu - \alpha r _ { 0 } ) s ^ { 2 } c _ { 2 } ( \alpha s ^ { 2 } ) } \\ { = r _ { 0 } \left[ 1 - ( \alpha s ^ { 2 } ) c _ { 2 } ( \alpha s ^ { 2 } ) \right] + r _ { 0 } \dot { r } _ { 0 } s c _ { 1 } ( \alpha s ^ { 2 } ) + \mu s ^ { 2 } c _ { 2 } ( \alpha s ^ { 2 } ) } \\ { = r _ { 0 } c _ { 0 } ( \alpha s ^ { 2 } ) + r _ { 0 } \dot { r } _ { 0 } s c _ { 1 } ( \alpha s ^ { 2 } ) + \mu s ^ { 2 } c _ { 2 } ( \alpha s ^ { 2 } ) , } \end{array}
$$

since

$$
\mathbb { i } - x c _ { 2 } ( x ) = c _ { 0 } ( x ) .
$$

Next, from (6.9.4),

$$
\begin{array} { l } { \displaystyle { \dot { t } - t _ { 0 } = \int _ { 0 } ^ { s } r ( \bar { s } ) d \overline { { s } } \quad \mathrm { ~ } } } \\ { \displaystyle { \quad = r _ { 0 } s c _ { 1 } \big ( \alpha s ^ { 2 } \big ) + r _ { 0 } \dot { \bar { r } } _ { 0 } s ^ { 2 } c _ { 2 } \big ( \alpha s ^ { 2 } \big ) + \mu s ^ { 3 } c _ { 3 } \big ( \alpha s ^ { 2 } \big ) } . } \end{array}
$$

This, so easily derived, is the new form of Kepler's equation. We shall consider the matter of its solution shortly.

The $\hat { \pmb f }$ and $g$ functions satisfy (6.9.13). Also,

$$
{ \ddot { f } } + \left( { \frac { \mu } { r ^ { 3 } } } \right) f = 0 { \mathrm { a a d ~ } } { \ddot { g } } + \left( { \frac { \mu } { r ^ { 3 } } } \right) g = 0 .
$$

So

$$
\begin{array} { l } { { f _ { 0 } = 1 , \dot { f } _ { 0 } = 0 , \ddot { f } _ { 0 } = - \frac { \mu } { r _ { 0 } ^ { 3 } } , } } \\ { { g _ { 0 } = 0 , \dot { g } _ { 0 } = 1 , \ddot { g } _ { 0 } = 0 . } } \end{array}
$$

Therefore,

$$
\begin{array} { r l } & { f _ { 0 } ^ { \prime } = r _ { 0 } \dot { f } _ { 0 } = 0 , ~ \quad \dot { f } _ { 0 } ^ { \prime \prime } = r _ { 0 } ^ { 2 } \ddot { f } _ { 0 } + r _ { 0 } \dot { r } _ { 0 } \dot { f } _ { 0 } = - \frac { \mu } { r _ { 0 } } , } \\ & { g _ { 0 } ^ { \prime } = r _ { 0 } \dot { g } _ { 0 } = r _ { 0 } , ~ \quad g _ { 0 } ^ { \prime \prime } = r _ { 0 } ^ { 2 } \ddot { g } _ { 0 } + r _ { 0 } \dot { r } _ { 0 } \dot { g } _ { 0 } = r _ { 0 } \dot { r } _ { 0 } . } \end{array}
$$

Following the same method used for $\mathfrak { F }$ in (6.9.24),the $f$ and $g$ functions and their derivatives can be constructed as:

$$
\begin{array} { r l } & { f = 1 - \left( \frac { \mu } { r _ { 0 } } \right) s ^ { 2 } c _ { 2 } ( \alpha s ^ { 2 } ) , } \\ & { g = r _ { 0 } s c _ { 1 } ( \alpha s ^ { 2 } ) + r _ { 0 } \dot { r } _ { 0 } s ^ { 2 } c _ { 2 } ( \alpha s ^ { 2 } ) } \\ & { \phantom { \frac { f ^ { 2 } } { f ^ { 2 } } } = t - \bar { t } _ { 0 } - \mu s ^ { 3 } c _ { 3 } ( \alpha s ^ { 2 } ) , } \\ & { \phantom { \frac { f ^ { 2 } } { f ^ { 2 } } } \dot { f } = - \left( \frac { \mu } { r r _ { 0 } } \right) s c _ { 1 } ( \alpha s ^ { 2 } ) , } \\ & { \dot { g } = 1 - \left( \frac { \mu } { r } \right) s ^ { 2 } c _ { 2 } ( \alpha s ^ { 2 } ) . } \end{array}
$$

We now have all the formulas needed to find a solution of the initial value problem, but must still discuss the solution of Kepler's equation,(6.9.26). If we write it as

$$
f ( s ) = r _ { 0 } s c _ { 1 } ( \alpha s ^ { 2 } ) + r _ { 0 } \dot { r } _ { 0 } s ^ { 2 } c _ { 2 } ( \alpha s ^ { 2 } ) + \mu s ^ { 3 } c _ { 3 } ( \alpha s ^ { 2 } ) - \Delta t = 0 ,
$$

then the derivatives required for the solution are

$$
\begin{array} { r l } & { f ^ { \prime } ( s ) = r _ { 0 } c _ { 0 } ( \alpha s ^ { 2 } ) + r _ { 0 } \dot { r } _ { 0 } s c _ { 1 } ( \alpha s ^ { 2 } ) + \mu s ^ { 2 } c _ { 2 } ( \alpha s ^ { 2 } ) } \\ & { \qquad = r , } \\ & { f ^ { \prime \prime } ( s ) = - r _ { 0 } \alpha s c _ { 1 } ( \alpha s ^ { 2 } ) + r _ { 0 } \dot { r } _ { 0 } c _ { 0 } ( \alpha s ^ { 2 } ) + \mu s c _ { 1 } ( \alpha s ^ { 2 } ) } \\ & { \qquad = ( - r _ { 0 } \alpha + \mu ) s c _ { 1 } ( \alpha s ^ { 2 } ) + r _ { 0 } \dot { r } _ { 0 } c _ { 0 } ( \alpha s ^ { 2 } ) , } \\ & { f ^ { \prime \prime \prime } ( s ) = ( - r _ { 0 } \alpha + \mu ) c _ { 0 } ( \alpha s ^ { 2 } ) - r _ { 0 } \dot { r } _ { 0 } \alpha s c _ { 1 } ( \alpha s ^ { 2 } ) . } \end{array}
$$

If the arc of the orbit spanned by the two times is small, then a satisfactory initial guess (corresponding to ${ \mathfrak { x } } _ { \mathfrak { d } } = { \mathfrak { M } }$ ，way back） is

$$
s _ { \mathbb { 0 } } = \frac { \Delta \hat { \mathfrak { z } } } { \mathfrak { z } _ { \mathbb { 0 } } } .
$$

A better approximation when $\Delta \vec { \updownarrow }$ is small can be derived by writing (6.9.28) as

$$
\gamma _ { 0 } s + \frac { 1 } { 2 } \dot { \tau } _ { 0 } \dot { \vec { s } _ { 0 } } s ^ { 2 } - \Delta t \simeq 0 .
$$

Let

$$
\begin{array} { r } { \mathbf { \sigma } _ { s } = \frac { \Delta t } { \tau _ { 0 } } + \alpha \left( \frac { \Delta t } { \tau _ { 0 } } \right) ^ { 2 } + \mathrm { ~ . ~ . ~ . ~ } } \end{array}
$$

Substituting, and developing in powers of $\Delta \vec { \tau }$ we find $a = - { \frac { 1 } { 2 } } \dot { \bar { \mathfrak { r } } } _ { \mathfrak { Q } }$ In the same way, $\pmb { \delta }$ can be developed further as

$$
s = \frac { \Delta t } { r _ { 0 } } - \frac { 1 } { 2 } \dot { \bar { r } } _ { 0 } \left( \frac { \Delta t } { r _ { 0 } } \right) ^ { 2 } + \left( \frac { 1 } { 2 } \dot { \bar { r } } _ { 0 } ^ { 2 } - \frac { 1 } { 6 } \frac { \mu - \alpha r _ { 0 } } { r _ { 0 } } \right) \left( \frac { \Delta t } { r _ { 0 } } \right) ^ { 3 } + \cdot \cdot \cdot
$$

Otherwise there is no known satisfactory “universal” initial guess. If $\alpha > 0$ ,the orbit is elliptic,and the initial guess (6.8.9) can be used, bearingin mind that for elliptic motion,

$$
s = { \frac { \Delta E } { \sqrt { \alpha } } } , \quad \alpha > 0 .
$$

Kepler's equation for hyperbolic motion can be written as

$$
f ( F ) = e \sinh F - F - M , \quad \mathrm { w h e r e } \quad M = \sqrt { \frac { - \mu } { a ^ { 3 } } } ( t - T ) .
$$

It has been found by experiment (see exercise 7, section 6.6 and Reference 32) that a good initial guess is

$$
\mathrm { f o r ~ } \lambda M > 0 , F _ { 0 } = \ln \left[ \frac { 2 M } { e } + k \right] , k \geq 0 ,
$$

where $k = 1 . 8$ gives good results. A form of Kepler's equation relating any two times in $\hat { \bf \Phi }$ hyperbolic orbit can be derived as was (6.8.8). Let

$$
\Delta t = t - \dot { \tau } _ { 0 } , \Delta F = F - F _ { 0 } , \Delta \dot { M } = \sqrt { \frac { - \mu } { a ^ { 3 } } } \Delta t ,
$$

and

$$
\begin{array} { r } { \dot { C } H = e \cosh ( F _ { 0 } ) = 1 - \frac { r _ { 0 } } { a } , \ S H = e \sinh ( F _ { 0 } ) = \frac { r _ { 0 } \dot { r } _ { 0 } } { \sqrt { - \mu a } } . } \end{array}
$$

Then Kepler's equation becomes

$$
f ( \Delta F ) = C H \sin ( \Delta F ) + S H \cosh ( \Delta F ) - \Delta F - S H - \Delta M = 0 .
$$

If △M is positive and not too small, then $\exp \{ - \Delta F \}$ can be neglected, in a first approximation. So if the hyperbolic functions of (6.9.32) are expressed in exponential form, then

$$
\Delta M = \frac { S H + C H } { 2 } \mathrm { e x p } ( \Delta F ) + \frac { S H - C H } { 2 } \mathrm { e x p } ( - \Delta F ) - S H - \Delta F ,
$$

so that, approximately,

$$
\Delta M \simeq \frac { S E + C E } { 2 } \mathrm { e x p } ( \Delta F ) ,
$$

suggesting a first guess

$$
( \Delta F ) _ { 0 } = \mathrm { l n } \left( \frac { 2 \Delta M } { S H + C H } \right) = \mathrm { l n } \left( \frac { 2 \Delta M } { e } \right) - F _ { 0 } , ~ \Delta M > 0 .
$$

A similar development for $\Delta \mathbb { M } < \mathbb { Q }$ results in

$$
( \Delta F ) _ { 0 } = - \ln \left( \frac { 2 \Delta M } { S H - C H } \right) = - \ln \left( - \frac { 2 \Delta M } { e } \right) - F _ { 0 } , \Delta M < 0 .
$$

Earlier experience with Kepler's equation for hyperbolic orbits suggests the forms

$$
\begin{array} { r l } & { ( \Delta F ) _ { 0 } = \ln \left( \frac { 2 \Delta M + k e } { C H + S H } \right) , \Delta M > 0 , } \\ & { ( \Delta F ) _ { 0 } = - \ln \left( \frac { - 2 \Delta M + k e } { C H - S H } \right) , \Delta M < 0 , } \end{array}
$$

where $\Bbbk$ is $\hat { \mathbf { \Omega } }$ positive constant. $\chi = 1 . 8$ is effective. Finally,

$$
s = \frac { \Delta F } { \sqrt { - \alpha } } , \quad \alpha < 0 .
$$

# Exercise

If the orbit is nearly parabolic, $\alpha$ is small, and the adaptations just described may not work.One approach in this case is to note that fora parabolic orbit (6.9.27) reduces to

$$
f _ { \hat { 1 } } ( s ) = \frac { \mu } { 6 } s ^ { 3 } + \frac { \hat { \bar { 1 } } } { 2 } ( r _ { 0 } \dot { r } _ { 0 } ) s ^ { 2 } + r _ { 0 } s - \Delta t = 0 .
$$

This cubic may be solved to give an initial guess. A more general cubic may be derived by keeping all cubic terms in $\pmb { s }$ ,when we have

$$
\begin{array} { r } { f _ { 2 } ( s ) = \frac { 1 } { 6 } ( \mu - \alpha \vec { r } _ { 0 } ) s ^ { 3 } + \frac { 1 } { 2 } ( r _ { 0 } \dot { r } _ { 0 } ) s ^ { 2 } + r _ { 0 } s - \Delta t = 0 . } \end{array}
$$

This gives guesses that are correct for both circular and parabolic orbits.

To solve the cubic, write it as

$$
\begin{array} { r } { s ^ { 3 } \div a _ { 2 } s ^ { 2 } \div a _ { 1 } s \div a _ { 0 } = 0 . } \end{array}
$$

Let

$$
\begin{array} { r } { q = \frac { 1 } { 3 } a _ { \perp } - \frac { 1 } { 9 } a _ { 2 } ^ { 2 } , \quad r = \frac { 1 } { 6 } ( a _ { \perp } a _ { 2 } - 3 a _ { 0 } ) - \frac { 1 } { 2 7 } a _ { 2 } ^ { 3 } . } \end{array}
$$

f $q ^ { 3 } \ + r ^ { 2 } > 0$ ,there is just one real root which is found as follows:

$$
\begin{array} { r l } & { \mathrm { ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \textmu ~ \ m ~ } } \\ & { \mathrm { ~ a n d ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \textmu ~ \ m ~ } } \\ & { \mathrm { ~ T h e r ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \tt ~ \textmu ~ \tt ~ \tt ~ \tt ~ \textmu ~ \tt ~ \textmu ~ \tt ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ } } \\ & { \mathrm { ~ a n d ~ \tt ~ \tt ~ \tt \ u ~ \ * ~ \ * ~ \ u ~ \tt ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ } } \\ &  \mathrm  ~ T h e r ~ \ u ~ \tt ~ \ * ~ \tt \ u ~ \ * ~ \ u ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmu ~ \textmd ~ \ u ~ \textmd ~ \ u ~ \textmd ~ \ u ~ \textmd ~ \ u ~ \textmu ~ \textmu ~ \textmd ~ \textmd \ \end{array}
$$

Instances when there are three real roots are troublesome and should be avoided.

Write a program that uses either of the cubics for an initial guess and test it. Investigate conditions that would lead to three real roots. Compare the use of the cubic with the use of a search procedure like the one preceding the secant method in section 6.6. More details can be found in Reference 32. See if you can generate ideas of your own for initial guesses when universal variables are used.

# 6.10The Initial Value Problem I

The following program implements the equations and ideas of the preceding section. As with the program from Section 6.8,lines 360-380 contain instructions that reverse the initial and final conditions so that the program can be rerun as a check. The subroutine, lines 3000 and 3180, for calculating the Stumpff functions, has already been printed, and is omitted from this listing to save space. In the solution to Kepler's equation I have included the method ofLaguerre-Conway as a back-up,in the event that the accelerated Newton's method fails.When the latter succeeds (in all elliptic cases,and, in my experience,in most hyperbolic cases) I prefer it for its speed; but I have yet to know the Laguerre-Conway method to fail under any circumstances. An important difference between the use of universal and conventional variables is that the numbers appearing in the former case are often considerably larger. (Time differences, for instance, as opposed to the mean anomaly.) So care must be taken that the small number used in line 2470 is not too small. The accuracy obtainable is relative to the magnitude of the numbers used in the calculation.

REM INITIAL VALUE PROBLEM USING UNIVERSAL VARIABLES. REM THE SUBROUTINE STARTING AT LINE 3OOO FOR THE REN CALCULATION OF THE STUMPFF FUNCTIONS IS OMITTED. CLS DEFDBL A-H,O-Z :DEFINT N 60 INPUT ENTER UUPRINT 70 INPUT ENTER THE INITIAL TIME,TO _：TO :PRINT 80PRINT ENTER COMPONENTS OF THE INITIAL POSITION,XO,YO,ZO 90INPUT XOYO,ZO:PRINT 100PRINT "ENTER COHPONENTS OF THE INITIAL VELOCITY, xvO,Yvo,zvo" 110 INPUT XVO,YVO,ZVO-：PRINT 120 INPUT ENTER THE FINAL TIME,T ；T :PRINT 130 PI = 3.141592653589793# 140 NB=0 150 REH FOR THE DEBUGGING RUN,WITH INITIAL AND FINAL 160 REM TIMES REVERSED,NB = 1. 170 RO=SQR(XO\*XO+YO\*YO+ZO\*Z0） 180 V0S XVO\*XVO + YVO\*YVO + ZVO\*ZVO

190U=XO\*XVO+YO\*YVO+ZO\*ZVO  
200 ALPH=2\*HU/RO-VOS  
210DT=T-TO  
220GOSUB 2OOO:REM SOLVE KEPLER'S EQUATION.  
230F=1-（U/R0）\*C2  
240G=DT-U\*C3  
250FDOT=-（HU/（FP\*RO））\*C1  
260 GDOT=18-（U/FP）\*C2  
270X=XO\*F+XVO\*G  
280Y=Y0\*F+YVO\*G  
290Z=Z0\*F+2V0\*G  
300XV=XO\*FDOT+XVO\*GDOT  
310YV=YO\*FDOT+YVO\*GDOT  
PR  
350IFNB=1 THEN400  
360Xo=X:Y0=Y:Z0=Z  
370xvO=xv:YvO=YV:zvO=ZV  
380TT=TO:TO=T:T=TT:NB=1:GOTO170  
390 REM INITIAL AND FINAL CONDITIONS ARE REVERSED  
400END  
2000 REN SUBROUTINE FOR SOLVING KEPLER'S EQUATION USING  
2010 REN UNIVERSAL VARIABLES.  
2020 NC=0  
2030IFABS（DT/RO)>.2#THEN GOTO_2070  
2040S=DT/R0-（DT\*DT\*U）/（2\*RO\*RO\*RO）  
2050 REH FOR A HORE ACCURATE VALUE,SEE THE TEXT.  
2060G0T02320  
2070IF ALPHA<=O THEN2220  
2080 REN FIND INITIAL GUESS FOR ELLIPTIC HOTION  
2090=HU/ALPHA  
2100 EN=SQR(HU/（A\*A\*A））  
2110EC=1-RO/A  
2120ES=U/(EN\*A\*A)  
2130E=SQR（EC\*EC+ES\*ES）  
2140DT=DT-INT（EN\*DT/（2#\*PI)）\*（2#\*PI）/EN  
2150Y=EN\*DT-ES  
2160 SIGHA=SGN(ES\*COS(Y) + EC\*SIN(Y))  
2170X=Y+SIGMA\*.85\*E  
2180S=X/SQR(ALPHA)  
2190GOTO2320  
2200 REH FIND INITIAL GUESS FOR HYPERBOLIC HOTION.  
2210 REM SEE (6.9.34).  
2220A=HU/ALPHA  
2230 EN=SQR（-HU/（A\*A\*A)）  
2240CH=1-R0/  
2250SH=U/SQR（-A\*HU）  
2260E=SQR（CH\*CH-SH\*SH）  
2270D=EN\*DT  
2280IFDTHE2310  
2290S=LOG（(2\*DH+1.8\*E）/(CH+SH））/SQR(-ALPHA）  
2300GOTO2320  
2310S=-LOG（（-28DH+1.8\*\*E)/(CH-SH))/SQR（-ALPHA)  
2320 ST=s  
2330 REM STORE INITIAL GUESS FOR POSSIBLE USE LATER IN  
2340 REN LAGUERRE'S HETHOD,IN CASE NEWTON'S METHOD PAILS.  
2350X=S\*S\*ALPHA  
2360GOSUB3000  
2370 C1= C1\*S:C2= C2\*S\*S:C3= C3\*S\*S\*S  
2380F=RO\*C1+U\*C2+HU\*C3-DT  
2390FP $=$ RO\*CO+U\*C1÷U\*C2  
2400FPP $=$ （-RO\*ALPHA+U）\*C1+U\*CO  
2410FPPP $\equiv$ （-RO\*ALPHA+HU)\*CO-U\*ALPHA\*C1  
2420DS=-F/FP  
2430DS=-F/（FP $\nrightarrow$ DS\*FPP/2#)  
2440DS=-P/FP+DS\*FPP/2+DS\*DS\*FPPP/6#)  
2450S=S+DS  
2460 REN QUARTIC CONVERGENCE  
2470IF ABS（DS)<1E-12 THEN RETURN  
2480 REN NEVTON'S HETHOD SUCCEEDED  
2490NC=NC+1:IFC<6THEN2350  
2500 REN IF NC =6, THEN NEVTON'S METHOD HAS FAILED  
2510S=ST:LN=5:NC=0  
2520 REH START LAGUERRE'S HETHOD  
2530X= S\*S\*ALPHA  
2540GOSUB 3000  
2550 C1=C1\*S:C2=C2\*S\*S:C3_=C3\*S\*S\*S  
2560 F=RO\*C1+U\*C2HU\*C3-DT  
2570 FP=RO\*CO÷U\*C1+U\*C2  
2580 FPP=（-RO\*ALPHA÷NU）\*C1+U\*CO  
2590 DS=-LN\*F/（FP+SGN（FP）\*SQR  
（ABS((LN-1）\*（LN-1）\*FP\*FP-（LN-1)\*LN\*F\*FPP）)）  
2600S=S+DS  
2610 IF ABS（DS)< 1E-12 THEN RETURN  
2620NC=NC+1:IFNC<20THEN2530  
2630 PRINT "THE SOLUTION OF KEPLER'S EQUATION FAILED."  
2640 RETURN

Example:

$$
\begin{array} { r l } & { \mu = 1 , \ t _ { 0 } = 0 , \ t = 1 . \ \mathrm { r } _ { 6 } = ( 1 , \ 1 , - . 1 ) , \ \mathrm { v } _ { 0 } = ( - . 1 , \ 2 , \ - . 2 ) . } \\ & { \mathbf { r } = ( . 6 1 1 \ 2 3 8 \ 4 3 9 \ 2 3 1 \ 5 1 3 6 , \ 1 . 9 2 8 7 3 9 7 1 3 5 4 5 7 4 , \ - . 2 5 6 \ 2 4 7 \ 8 9 0 0 0 3 1 2 3 4 ) } \\ & { \mathbf { v } = ( - . 5 1 4 \ 7 7 7 0 9 8 3 8 8 2 7 0 9 , \ 1 . 6 6 4 \ 0 4 6 \ 1 4 2 1 1 3 5 3 6 , \ - . 1 2 7 7 5 6 1 2 5 4 3 9 7 7 8 } \end{array}
$$

# 6.11 The Two-Point Boundary Value Problem I-Application of Lambert's Theorem

The problem to be discussed in this and the following two sections is that offinding the Keplerian orbit passing through two given positions, with a given time taken for the transfer. This is of traditional importance in the determination of orbits,with the field dominated by the majesty of Gauss.Today, the problem must be routinely solved under many circumstances,such as maneuversleading to rendezvous between two spacecraft,and orbits of missiles.Today there are many good methods of solution,and a detailed discussion would fill a book.The first two methods to be considered are elegant to use, but will require some mathematical derivation. We shall also meet another “universal" formulation, due to Gauss.

Analytically, we are given ${ \mathfrak { r } } _ { 1 } = \{ x _ { 1 } , y _ { 1 } , z _ { 1 } \}$ and ${ \mathfrak { r } } _ { 2 } = \{ { \mathfrak { x } } _ { 2 } , { \mathfrak { y } } _ { 2 } , z _ { 2 } \}$ and $\Delta \vec { \mathfrak { z } } ,$ the time interval between them; this will be assumed to be positive.The problem will be considered solved if the velocity $\pmb { \mathbb { V } } _ { \ P }$ has been found.All practical methods of solution involve iteration. Also a solution is not unique;the operator may choose the sense in which the orbit is described,and,for elliptic motion, there may be the option of several revolutions being made before the end of the time interval is reached. In the following discussion we assume that less than a complete revolution is involved;generalization will be left to an exercise.The initial discussion will be for elliptic motion, but will soon be made general.

Let the two points in the orbit be called $\mathcal { P } _ { 1 }$ and $P _ { 2 }$ ,and the corresponding eccentric anomalies $\Xi _ { \mathfrak { Z } _ { \mathfrak { Z } } }$ and $E _ { 2 }$ Then $\mathcal { E } _ { 2 } > \mathcal { E } _ { 1 }$ ,and, since we are considering less than a complete revolution, $\mathcal { E } _ { 2 } - \mathcal { E } _ { 1 } ^ { \ast } < 2 \pi$ We can assume without loss of generality that $0 \leq E _ { 1 } < 2 \pi$ Now introduce the following intermediate quantities:

$$
\begin{array} { c c } { { 2 G = E _ { 2 } + E _ { 1 } , } } & { { \mathrm { s o ~ } \mathbb { 0 } < G < 2 \pi , } } \\ { { 2 g = E _ { 2 } - E _ { 1 } = \Delta E , \mathrm { s o } } } & { { \mathbb { 0 } < g < \pi . } } \end{array}
$$

jis defined by

$$
e \cos G = \cos j , \quad { \mathrm { w i t e r e ~ } } 0 < j < { \pi } .
$$

Also let

$$
\left. \begin{array} { l l } { { \epsilon = j \div g , } } & { { \mathrm { ~ s o ~ } \quad 0 < \frac { 1 } { 2 } \varepsilon < \pi , } } \\ { { \delta = j - g , } } & { { \mathrm { ~ s o ~ } - \frac { 1 } { 2 } \pi < \frac { 1 } { 2 } \delta < \frac { 1 } { 2 } \pi . } } \end{array} \right]
$$

Then

$$
\begin{array} { r } { r _ { 1 } = a ( \mathrm { i } - e \cos  { E _ { \mathrm { 1 } } } ) \quad \mathrm { a n d } \quad r _ { 2 } = a ( \mathrm { i } - e \cos  { E _ { \mathrm { 2 } } } ) , } \end{array}
$$

and

$$
\begin{array} { r l } & { \mathrel { \phantom { = } } \pi _ { \perp } \stackrel { + } { _ { \perp } } r _ { 2 } = a \tilde { \mathopen { : } } 2 - e \bigl ( \cos \tilde { E } _ { \perp } + \cos \tilde { E } _ { 2 } \bigr ) \bigr ] } \\ & { \qquad = 2 a \bigl ( \tilde { \mathrm { 1 } } - e \cos G \cos g \bigr ) } \\ & { \qquad = 2 a \bigl ( \tilde { \mathrm { 1 } } - \cos j \cos g \bigr ) . } \end{array}
$$

Let the chord $\mathcal { P } _ { \mathtt { I } } \mathcal { P } _ { 2 }$ have length $\mathfrak { C } ;$ this is known,since

$$
c ^ { 2 } = ( \mathbf { r } _ { 1 } - \mathbf { r } _ { 2 } ) ^ { 2 } = ( x _ { 1 } - x _ { 2 } ) ^ { 2 } + ( y _ { 1 } - y _ { 2 } ) ^ { 2 } + ( z _ { 1 } - z _ { 2 } ) ^ { 2 } .
$$

But also,using (6.3.16),we can write

$$
\begin{array} { r l } & { c ^ { 2 } = a ^ { 2 } ( \cos  { E _ { 2 } } - \cos  { E _ { 1 } } ) ^ { 2 } + a ^ { 2 } ( 1 - e ^ { 2 } ) ( \sin  { E _ { 2 } } - \sin  { E _ { 1 } } ) ^ { 2 } } \\ & { \phantom { c c } = 4 a ^ { 2 } \sin ^ { 2 } G \sin ^ { 2 } g + 4 a ^ { 2 } ( 1 - e ^ { 2 } ) \cos ^ { 2 } G \sin ^ { 2 } g } \\ & { \phantom { c c } = 4 a ^ { 2 } \sin ^ { 2 } g ( 1 - \cos ^ { 2 } j ) . } \end{array}
$$

So

$$
c = 2 a \sin g \sin j .
$$

Combining (6.11.4) and (6.11.6), we find

$$
r _ { 1 } + r _ { 2 } + c = 2 a [ 1 - \cos ( g + j ) ] = 4 a \sin ^ { 2 } { \frac { 1 } { 2 } } \varepsilon ,
$$

and

$$
r _ { 1 } + r _ { 2 } - c = 2 a \{ 1 - \cos ( g - j ) \} = 4 a \sin ^ { 2 } \frac { 1 } { 2 } \delta .
$$

Finally, from Kepler's equation,

$$
\begin{array} { r l } & { n { \Delta \hat { t } } = { \dot { \cal E } } _ { 2 } - { \dot { \cal E } } _ { 1 } - e ( \sin { \cal E } _ { 2 } - \sin { \cal E } _ { 1 } ) } \\ & { \quad \quad = ( \epsilon - \delta ) - ( \sin \epsilon - \sin \delta ) } \\ & { \quad \quad = ( \epsilon - \sin \epsilon ) - ( \delta - \sin \delta ) . } \end{array}
$$

Equations (6.11.7) to (6.11.9) constitute Lamberts theorem for eliptic motion.

$\lessdot$ and $\delta$ are not uniquely determined by these formulas,and they must next be discussed.First,note that if the orbital arc is sufficiently small, then $\varepsilon$ and $\delta$ should be taken as the smallest positive values satisfying (6.11.7) and (6.11.8). Now from the inequalities (6.11.3),we always have

$$
\begin{array} { r } { \mathrm { s i } \ I _ { 2 } \frac { 1 } { 2 } \boldsymbol { \epsilon } > \mathbb { G } , \quad \mathrm { a r a d } \quad \cos \frac { 1 } { 2 } \boldsymbol { \delta } > \mathbb { 0 } . } \end{array}
$$

The signs of cos eand of sin δ have stillto be determined. To do this, consider the critical situations in which these quantities are zero.

When sinδ=0, then δ=Oand r1+r2-c= 0, which can only happen when the chord PP2 passes through the attracting focus. So we have the rule:

$$
\left. { \begin{array} { l } { { \mathrm { I f ~ t h e ~ o r b i t a l ~ s e g m e n t ~ d o e s ~ n o t ~ i n c l u d e ~ t h e } } } \\ { { \mathrm { a t t r a c t i n g ~ f o c u s , ~ t h e n } } \sin { \frac { 1 } { 2 } } \delta > 0 . } \\ { } \\ { { \mathrm { I f ~ t h e ~ o r b i t a l ~ s e g m e n t ~ i n c l u d e s ~ t h e } } } \\ { { \mathrm { a t t r a c t i n g ~ f o c u s ~ t h e n } , \sin { \frac { 1 } { 2 } } \delta < 0 . } } \end{array} } \right\}
$$

Figure 6.8 ilustrates the first case. The attracting focus is S and the empty focus is $S ^ { \prime }$ ； the orbital segment is shaded. Notice that from the programing point of view,it is the decision of the operator whether to have one case or the other.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0081-0120/ocr/images/7d833ee9dc3bc9d1dbd8a15ba057806f9d3b01c21c4f6e5bdd257edef55de74e.jpg)  
Figure 6.8

When cos $\frac { 1 } { 2 } \varepsilon = 0$ then $\begin{array} { r } { \frac { 1 } { 2 } \epsilon = \frac { 1 } { 2 } \pi . } \end{array}$ and $r _ { 1 } + r _ { 2 } + c = 4 a$ Now $S \mathcal { P } _ { \mathtt { i } } + S ^ { i } \mathcal { P } _ { \mathtt { i } } =$ ${ \cal S } { \cal P } _ { 2 } + { \cal S } ^ { \prime } { \cal P } _ { 2 } = 2 a$ ， so in this case the chord $\mathbb { P } _ { 1 } \mathbb { P } _ { 2 }$ passes through the empty focus, $S ^ { j }$ Consequently:

$$
\begin{array} { l } { { \mathrm { I f ~ t h e ~ o r b i t a l ~ s e g m e n t ~ i n c i u d e ~ t h e } } } \\ { { \cdot \ \mathrm { e m p t y ~ f o c u s , ~ t h e n } \cos { \frac { 1 } { 2 } } \epsilon > 0 . } } \\ { { \ } } \\ { { \mathrm { I f ~ t h e ~ o r b i t a l ~ s e g m e n t ~ i n c i u d e s ~ t h e } } } \\ { { \mathrm { e m p t y ~ f o c u s ~ t h e n } , \ \mathrm { c o s } { \frac { 1 } { 2 } } \epsilon < 0 . } } \end{array}
$$

The test in this instance requires some calculation. Let the subscript c be

applied to the critical case when cos $\begin{array} { r } { \frac { 1 } { 2 } \epsilon = 0 } \end{array}$ So

$$
\left. \begin{array} { c } { { \begin{array} { r l } { { a _ { c } = \frac { r _ { 1 } + r _ { 2 } + c } { 4 } , } } & { { } } \\ { { } } & { { } } \\ { { s i n ^ { 2 } \frac { 1 } { 2 } \delta _ { c } = \frac { r _ { 1 } + r _ { 2 } - c } { r _ { 1 } + r _ { 2 } + c } , } } \\ { { } } & { { } } \\ { { n _ { c } ( \Delta t ) _ { c } = \pi - \delta _ { c } + \sin \delta _ { c } . } } \\ { { } } & { { } } \\ { { \mathrm { T h e n ~ c o s ~ } \frac { 1 } { 2 } \epsilon > , - \Theta \mathrm { ~ a c c o r d i n g ~ a s ~ t o } } } \\ { { } } & { { } } \\ { { \mathrm { w h e t h e r } \Delta t < \omega , > \left( \Delta t \right) _ { c } . } } \end{array} } } \end{array} \right\}
$$

Next define

$$
X = S G N ( \cos { \frac { 1 } { 2 } } \epsilon ) , ~ Y = S G N ( \sin { \frac { 1 } { 2 } } \delta ) .
$$

Then if $\boldsymbol { \epsilon } ^ { * }$ and $\delta ^ { * }$ are the smallest positive numbers satisfying (6.11.7) and (6.11.8),we have

$$
\epsilon = Y \epsilon ^ { * } \quad \widehat { \sf a n d } \quad \delta = \pi ( 1 - X ) + X \delta ^ { * } .
$$

(6.11.9) becomes

$$
\mathfrak { n } \Delta t = \mathfrak { n } ( 1 - X ) + X ( \mathfrak { e } ^ { * } - \sin \mathfrak { e } ^ { * } ) - Y ( \delta ^ { * } - \sin \delta ^ { * } ) .
$$

For a short enough time of transfer, $\Delta t$ the orbit will be hyperbolic.To test for this we must find the time of transfer, $\{ \Delta \dot { \mathfrak { L } } \} _ { \mathfrak { P } }$ ,for a parabolic arc. This is accomplished by considering the formulas for eliptic motion and letting $a \to \infty$ When $\pmb { \mathscr { Q } }$ is large, $\lessdot$ and $\delta$ are small, so,

$$
a \epsilon ^ { 2 } \simeq r _ { 1 } + r _ { 2 } + \epsilon ~ \mathrm { a n d } ~ a \delta ^ { 2 } \simeq r _ { 1 } + r _ { 2 } - \epsilon .
$$

Replacing $\mathfrak { a }$ by $\sqrt { \mu } a ^ { - 3 / 2 }$ , (6.11.16) is approximated by

$$
\sqrt { \mu } \Delta t \simeq \textstyle { \frac { 1 } { 6 } } a ^ { 3 / 2 } ( \epsilon ^ { * 3 } - \delta ^ { * 3 } ) ,
$$

where, obviously, we must take $X = 1$ . Then in the limit for parabolic motion, with $\sqrt { \mu } = \Bbbk$ ，

$$
6 k ( \Delta i ) _ { p } = ( r _ { 1 } + r _ { 2 } + c ) ^ { 3 / 2 } + Y ( r _ { 1 } + r _ { 2 } - c ) ^ { 3 / 2 } .
$$

This is Euler's theorem.

For practical purposes, the three equations that make up Lambert's theorem are best combined into one. Let

$$
\lambda _ { 1 } ^ { 2 } = r _ { 1 } + r _ { 2 } + c , \quad \lambda _ { 2 } ^ { 2 } = r _ { 1 } + r _ { 2 } - c ,
$$

where $\lambda _ { 1 }$ and $\lambda _ { 2 }$ are both positive. After substitution for $\approx$ ,(6.11.16) can be written as

$$
\begin{array} { l } { { 6 [ \bar { \kappa } \Delta { t } - a ^ { 3 / 2 } ( 1 - X ) \pi ] = 6 \alpha ^ { 3 / 2 } [ X ( \epsilon ^ { * } - \sin \epsilon ^ { * } ) - Y ( \delta ^ { * } - \sin \delta ^ { * } ) ] } } \\ { { = \frac { 3 } { 4 } X \frac { \epsilon ^ { * } - \sin \epsilon ^ { * } } { \sin ^ { 3 } \frac { 1 } { 2 } \epsilon ^ { * } } \left( 4 a \sin ^ { 2 } \frac { 1 } { 2 } \epsilon ^ { * } \right) ^ { 3 / 2 } - \frac { 3 } { 4 } Y \frac { \delta ^ { * } - \sin \delta ^ { * } } { \sin ^ { 3 } \frac { 1 } { 2 } \delta ^ { * } } \left( 4 a \sin ^ { 2 } \frac { 1 } { 2 } \delta ^ { * } \right) ^ { 3 / 2 } } } \\ { { = X Q ( \epsilon ^ { * } ) \lambda _ { 1 } ^ { 3 } - Y Q ( \delta _ { : } ^ { * } ) \lambda _ { 2 } ^ { 3 } , \qquad \quad \dots \quad \dots \quad \dots \quad \dots . } } \end{array}
$$

where the function $Q$ is defined by

$$
Q ( \theta ) = \frac { 3 } { 4 } \frac { \theta - \sin \theta } { \sin ^ { 3 } \frac { 1 } { 2 } \theta } .
$$

This function was the subject of some brilliant manipulation by Gauss. Here we summarize some of the results. Let

$$
x = \sin ^ { 2 } { \frac { 1 } { 2 } } \theta . \cdotp .
$$

Then with $a$ considered as a function of $\pmb { \mathcal { X } }$ ,we find from elementary calculus,

$$
{ \frac { 2 } { 3 } } x { \frac { d Q } { d x } } \div Q = ( 1 - x ) ^ { - 1 / 2 } .
$$

The appropriate solution is

$$
Q = \frac { 3 } { 2 } x ^ { - 3 / 2 } \int _ { 0 } ^ { x } \sqrt { \frac { t } { 1 - t } } d t .
$$

This will be expressed in three ways. If the integrand is expanded in powers of $\sharp ,$ and the resulting series integrated term by term,we find

$$
Q = F \left\{ { \textstyle \frac { 1 } { 2 } } , { \textstyle \frac { 3 } { 2 } } , { \textstyle \frac { 5 } { 2 } } ; x \right\} ,
$$

where the hypergeometric series is defined by

$$
F ( a , b , c ; x ) = 1 + { \frac { a \cdot b } { c } } x + { \frac { a ( a + 1 ) b ( b + 1 ) } { c ( c + 1 ) ( 1 ) ! } } x ^ { 2 } + \cdot \cdot \cdot
$$

Also,if $0 < x \leq 1$ ,then

$$
Q = { \frac { 3 } { 2 } } x ^ { - 3 / 2 } \left[ - ( x - x ^ { 2 } ) ^ { 1 / 2 } + { \frac { 1 } { 2 } } \sin ^ { - 1 } ( 2 x - 1 ) + { \frac { \pi } { 4 } } \right] ,
$$

and if $x < 0$ ,then

$$
Q = \frac { 3 } { 4 } ( - x ) ^ { - 3 / 2 } \left[ 2 ( x ^ { 2 } - x ) ^ { 1 / 2 } - \ln \left\{ 1 - 2 x + 2 ( x ^ { 2 } - x ) ^ { 1 / 2 } \right\} \right] .
$$

The series is not efficient for $| { \boldsymbol { { \boldsymbol { x } } } } |$ greater than about .1,and the analytical expressions are not efficient for $\vartriangle$ close to zero. In letting $\pmb { x }$ be negative,we are allowing for hyperbolic motion,and (6.11.19) has,magically， become universal.

Gauss expressed $Q$ as a function of

$$
\begin{array} { r } { x ^ { * } = \sin ^ { 2 } \frac { 1 } { 4 } \theta = \frac { 1 } { 2 } ( 1 - \sqrt { 1 - x } ) . } \end{array}
$$

The new series can be found by using the identity

$$
F ( a , b , a + 5 + { \textstyle \frac 1 2 } ; x ) = F ( 2 a , 2 b , a + \bar { b } ; + { \textstyle \frac 1 2 } ; { \textstyle \frac 1 2 } - { \textstyle \frac 1 2 } { \textstyle \sqrt { 1 - x } } ) .
$$

(See References 23 and 24 which contain a treasury of information such as this.） Then

$$
\begin{array}{c} \begin{array} { l } { \dot { { \mathbf { \Xi } } } } \\ { { { \mathbf { \Xi } } } } \\ { { { \mathbf { \Xi } } } } \end{array} \Vdash ( 1 , ~ 2 , ~ \frac { 5 } { 2 } ; ~ x ^ { * } )  \\ { { \mathbf { \Xi } } } \\ { { { \mathbf { \Xi } } } = 1 + \frac { 6 } { 5 } x ^ { * } + \frac { 6 \cdot 8 } { 5 \cdot 7 } x ^ { * 2 } + \frac { 6 \cdot 8 \cdot 1 0 } { 5 \cdot 7 \cdot 9 } x ^ { * 3 } + \cdot \cdot \cdot \cdot }  \end{array}
$$

Gauss first showed that $a$ satisfied the differential equation

$$
4 x ^ { * } ( 1 - x ^ { * } ) \frac { d Q } { d x ^ { * } } + 6 ( 1 - 2 x ^ { * } ) Q = 6 .
$$

and solved it in powers of $\boldsymbol { \mathfrak { X } } ^ { * }$ ,using the method of undetermined coefficients, to derive (6.11.29). The equation can also be solved analytically to give:

f $0 < x ^ { * } \leq \frac { 1 } { 2 }$ ,then

$$
Q = { \frac { 3 } { 1 6 } } { \frac { [ 2 ( 2 x ^ { * } - 1 ) ( x ^ { * } - x ^ { * 2 } ) ^ { \frac { 1 } { 4 } / 2 } + \sin ^ { - 1 } ( 2 x ^ { * } - 1 ) + { \frac { \pi } { 2 } } ] } { ( x ^ { * } - x ^ { * 2 } ) ^ { 3 / 2 } } } .
$$

If ${ x ^ { \ast } } < \emptyset$ then

$$
Q = \frac { 3 } { 1 6 } \frac { [ 2 ( 1 - 2 x ^ { * } ) ( x ^ { * 2 } - x ^ { * } ) ^ { 1 / 2 } - \ln \{ 1 - 2 x ^ { * } + 2 ( x ^ { * 2 } - x ^ { * } ) ^ { 1 / 2 } \} ] } { ( x ^ { * 2 } - x ^ { * } ) ^ { 3 / 2 } } .
$$

The following program was uscd to verify these formulas, showing that the series or the analytical expressions gave the same results,whether $\mathcal { X }$ or $z ^ { \ast }$ was used,and the program was used to decide on a cut-off point for the use of the serics. You should write a similar program and gain some facility with the calculation of $Q$ Gauss derived other expressions for the computation of $a$ some of which involved continucd fractions. (Note that the use of continued fractions in modern computation is increasing.) It would be worth while to read his book (Reference 23) and experiment with some of his formulas. In the work that follows we shall use the formulas that involve ${ \boldsymbol { \mathfrak { X } } } ^ { * }$ ，since they will also be useful in the following section. The series will be used for $\left. \mathfrak { Z } \right. < . \exists$ ,or $\left| x ^ { * } \right| < . 0 2 5$ ,and the formulas otherwise. You should experiment to see for what value of ${ \boldsymbol { \mathcal { Z } } } ^ { * }$ it is equally efficient, in terms of time, to calculate the series or the formulas on your computer.

（-SQR(X-X\*X)÷ATN(Y/SQR(1\*-Y\*Y)）/2\*+PI/4\*)   
160 170 PRINT:PRINT THE ANALYTICAL FORHULA GIVES  ； F REH（6.11.26)   
180GOTO230   
190Y=SQR（X\*X- X）   
200F=75\*(2\*\*Y-L0G（1\*-2\*\*X÷2#\*Y））\*（（-X）-1.5\*）   
210 REH（6.11.27）   
220 PRINT:PRINT THE ANALYTICAL FORMULA GIVES；F   
230XS=（i-SqR（1-X））/2\*   
240 A=1#:B=3#:X=XS   
250 GOSUB 500   
270 260 PRINT:PRINT "THE SUM OF THE _SERIES USING X\* IS PRINT :PRINT "THE NUHBER OF TERNS NEEDED WAS ; $\vdots ^ { \textbf { S } } _ { \widetilde { \mathtt { A } } } \mathbf { _ { \mathtt { A } } } _ { 2 }$   
280 IF XS < O THEN 340   
290Y=2#\*XS-1   
300F=（3#/16\*）\*（ATN（Y/SQR(1-Y\*Y））   
+2#\*Y\*SQR（XS-XS\*XS)÷PI/2\*)/（(XS-XS\*XS)1.5）   
310 REM（6.11.31）   
320 PRINT :PRINT "THE ANALYTICAL FORMULA GIVES " ；F   
330END   
340 Y#= SQR(XS\*XS-XS)   
350F=(3#/16\*）\*(2#\*（1-2#\*XS）\*Y   
LOG（1-2#\*XS+2\*Y））/（Y\*Y\*Y）   
360 REN(6.11.32）.   
370 PRINT :PRINT THE ANALYTICAL FORMULA GIVES " ；F   
380 END   
500 REN COMPUTES THE HYPERGEONETRIC SERIES $E \{ \hat { \mathbf { a } } , \hat { \mathbf { a } } , \hat { \mathbf { c } } ; \mathbf { Z } \}$   
510F=X\*A\*B/C   
520S=1#+F   
530FOR=1TO 200   
540 D=N   
550 F=F\*X\*(A ÷DN）\*(B+DN）/((C+DN）\*（DH÷1））   
560 S_=S+F   
570 IF ABS(F)< 1E-15 THEN 600   
580 NEXT N   
590 PRINT NO CONVERGENCE；DX =；F   
600 RETURN

# Examples

Wit $\mathtt { \ h \ m } = . 5 , Q = 1 . 2 1 0 8 4 1 8 6 0 0 5 9 1 3 2 .$ with the number of terms required in the series being 43 and 20.With $x = - . 5 , Q = . 8 8 0 5 4 5 0 3 5 8 1 6 6 3 0 6 ,$ with 43 and 18 terms needed.

We are now, at last, ready to construct a program. The unknown quantity to be approximated in the iteration will be

$$
z = { \frac { 1 } { a } } .
$$

The equation for $z$ is, from (6.11.19),

$$
f ( z ) = \frac { 1 } { k } [ \frac { 1 } { 6 } ( X Q _ { 1 } \lambda _ { 1 } ^ { 3 } - Y Q _ { 2 } \lambda _ { 2 } ^ { 3 } ) + ( 1 - X ) \pi z ^ { - 3 / 2 } ]  \Delta t = 0 ,
$$

where for $Q _ { i }$ the argument $x _ { i } = z \lambda _ { i } ^ { 2 } / 4$ is the input argument.

For a solution using Newton's method,

$$
f ^ { \prime } ( z ) = { \frac { 1 } { 4 k z } } \left( X \lambda _ { 1 } ^ { 3 } \Biggl \{ \left( \frac { 1 } { 4 } - { \frac { \lambda _ { 1 } ^ { 2 } z } { 4 } } \right) ^ { - 1 / 2 } - Q _ { 1 } \Biggl \} \right)
$$

$$
\begin{array} { l } { { - \mathbb { Y } \lambda _ { 2 } ^ { 3 } \left\{ \left( 1 - \frac { \lambda _ { 2 } ^ { 2 } z } { 4 } \right) ^ { - 1 / 2 } - Q _ { 2 } \right\} \Bigg ) } } \\ { { - ( 1 - X ) \frac { 3 \pi } { 2 k } z ^ { - 5 / 2 } . } } \end{array}
$$

On the following page a flowchart for the calculation is given. I hope that you will see that, once you are satisfied with the validity of the mathematics, the implementation of the method is quite simple. It should be noted that the calculation of $\{ \Delta \vec { \mathfrak { \tau } } \} _ { c }$ from (6.11.13) has been arranged to make use of the function $Q$

The initial guesses for the iteration are $z _ { o } = \pm 2 / \lambda _ { 1 } ^ { 2 }$ ,depending on the type of orbit. These are generally satisfactory although not ideal. A search procedure could be substituted,as discussed in a later exercise.

Finally，we need to find the velocity at the starting time $\ddagger _ { \ I }$ For this we shall derive expressions for the $\pmb { \hat { \jmath } }$ and $g$ functions,where

so that

$$
\left. \begin{array} { l } { \displaystyle \pmb { \tau } _ { 2 } = f \mathbf { r } _ { 1 } + g \mathbf { v } _ { 1 } } \\ { \displaystyle } \\ { \displaystyle \mathbf { v } _ { 1 } = \frac { 1 } { g } ( \mathbf { r } _ { 2 } - f \mathbf { r } _ { 1 } ) . } \end{array} \right]
$$

Notice that this fails if $g = \emptyset$ which happens when the chord $P _ { 1 } P _ { 2 }$ contains the attracting focus. There are extra complications here since the plane of the orbit is not determined. Discussion of this case is left as an exercise.

Define

$$
\alpha = \sqrt { a } \sin \textstyle { \frac { 1 } { 2 } } \varepsilon ^ { * } , \beta = \sqrt { a } \sin \textstyle { \frac { 1 } { 2 } } \delta ^ { * } , \gamma = \sqrt { a } \sin g .
$$

Then it is straightforward to show that

$$
\begin{array} { c } { f = \displaystyle \frac { a } { r _ { 1 } } ( \cos \Delta \mathcal { E } - 1 ) + \frac { 1 } { 4 } } \\ { = 1 - \displaystyle \frac { 2 \gamma ^ { 2 } } { r _ { 1 } } , } \end{array}
$$

and

$$
\begin{array} { l } { { g = \displaystyle \frac { a ^ { 3 / 2 } } { k } ( \sin \Delta E - e \sin E _ { 2 } + e \sin E _ { 1 } ) } } \\ { { = \displaystyle \frac { 4 } { k } \overline { { { Y } } } \alpha \beta \gamma . } } \end{array}
$$

Further,from (6.11.7) and (6.11.8), we have

$$
\begin{array} { r l } & { \alpha = \frac { \frac { 1 } { 2 } } { 2 } \lambda _ { 1 } , \quad \beta = \frac { 1 } { 2 } \lambda _ { 2 } , } \\ & { \gamma = \sqrt { a } ( \sin \frac { 1 } { 2 } \epsilon \cos \frac { 1 } { 2 } \delta - \cos \frac { 1 } { 2 } \epsilon \sin \frac { 1 } { 2 } \delta ) } \\ & { \quad = \alpha \sqrt { 1 - \frac { \lambda _ { 2 } ^ { 2 } } { 4 a } } - X Y \beta \sqrt { 1 - \frac { \lambda _ { 1 } ^ { 2 } } { 4 a } } . } \end{array}
$$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0081-0120/ocr/images/15ba270a9b0c103526169c5312973e0739f5acf6e41cb3b899f29b89438a9911.jpg)

These complete the formulas necessary to solve the problem with the exception of the case mentioned above where $\lambda _ { 2 } = \mathfrak { G }$ A program listing follows. When debugging your program you should use the output of a program for solving the initial value problem.For instance, using the example from section $6 . 1 0 .$ we would have

$$
\begin{array} { r l } & { \mathbf { r } _ { 1 } = ( 1 , . 1 , - . 1 ) } \\ & { \mathbf { r } _ { 2 } = ( . 6 1 1 2 3 8 4 3 9 2 3 1 5 1 3 6 , 1 . 9 2 8 7 3 9 7 1 3 5 4 5 7 4 , - . 2 5 6 2 4 7 8 9 0 0 0 3 1 2 3 4 ) } \\ & { \Delta t = 1 . } \end{array}
$$

The output should be

$$
{ \tt v } _ { 1 } = \{ - . \tt i , 2 , - . 2 \} .
$$

This example was successfully run. The iterates for $z$ as printed out were:

REN THE TVO-POINT BOUNDARY VALUE PROBLEM.   
REN APPLICATION OF LAMBERT'S THEOREM.   
CLS   
DEFDBL A-H,O-Z :DEFINT N   
PRINT ENTER COORDINATES OF THE INITIAL POSITION ; INPUT X1,Y1Z1:PRINT   
PRINT ENTER COORDINATES OF THE FINAL POSITION";   
INPUT X2,Y2,Z2:PRINT   
INPUT ENTER THE TIHE INTERVAL ；DT : PRINT   
100 INPUT ENTER THE VALUE OF HU；HU：PRINT   
110 PRINT ENTER +1 IF THE ORBITAL ARC DOES NOT INCLUDE 120PRITTE ATTRACTING FOCUS,OTHERISE,ETER-1；YY 130GK SQR（U）   
140 PI=3.141592653589793#   
150 R1=SQR（X1\*Xi+Y1\*Yi+Z1\*Z1）   
1602=SQR（X2\*X2+Y2\*Y2+Z2\*Z2）   
170C=SQB（（xi-x2）\*（x1-X2）+（Y1-Y2）\*（Y1- Y2）   
↑ （zi-z2)\*(Zi-Z2)）   
180L1=SQR（R1+2+）   
190L2=SQR（R1+R2-C）   
200 L12 = L1\*L1   
210 L13 =L12\*L1   
220 L22 = L2\*L2   
2 L23 L22\*L2   
DTP （L13-YY\*L23)/(6\*\*GK）   
REH (6.11.17）.   
12   
290 GOSUB4500   
300 DTC=(LI3\*PI-YY\*L23\*Q）/8#   
3.10 IF DTC >DT THEN340   
320 XX=1:NX=1:GOT0360   
330Z--2#/L12PRINTZ   
340 XX=1:X=1   
350 REK LINES 36O-47O CONTAIN THE ITERATION FOR Z.   
360 X=25\*Z\*L12:G0SUB 4500 $2 2 = 4$   
370 X=25\*Z\*L22G0SUB 450002=Q   
380DEL $=$ （XX\*Q1\*L13-YY\*Q2\*L23）/（6#\*GK)-DT

390IF NX=1 THEN410  
400DEL=DEL+2\*PI/（GK\*（Z1.5））  
410DER=（XX\*Li3\*（1/SQR（i-L12\*Z/4）-Q1）  
YY\*L23\*（1#/SQR（1-L22\*Z/4#）-Q2））  
420 DER=DER/（48\*GK\*Z):IF NX=1 THEN 440  
430 DER=DER-3\*PI/（GK\*Z2.5#)）：REH（6.11.34）.  
440DZ=-DEL/DER  
450 Z=Z÷DZ:IF ABS(DZ)<1E-15 THEN 480   
460 PRINTZ  
470GOTQ360  
480 PRINT Z  
490 GAH=（L1/2#)\*SQR(1、-L22\*2/4\*）  
-XX\*YY\*（L2/2)\*SQR（1\*-L12\*Z/4）  
500REM（6.11.39）  
510F= 1#-2\*GAN\*GAM/R1  
520 G= YY\*L1\*L2\*GAH/GK  
530 REM(6.11.37)AND （6.11.38）.  
540 XV1=（X2-F\*X1）/G  
550 YV1 （Y2-F\*Y1）/G  
560 ZVi=(22-F\*ZiS/G:REH （6.11.35）.  
570 PRINT XV1,YV1,ZV1  
580 END  
4500 XS=.5\*（1-SQR（1-X））  
4510IF ABS(X) > .1 THEN 4600  
4520FAC = 1.2#\*XS  
4530Q=1+FAC  
4540FRN=1TO10  
4550 DN= N  
4560 FAC=FAC\*XS\*（3#+DN）/（2.5\*+DN）  
4570 Q=Q+FAC  
4580 NEXTN:REH（6.11.29）.  
4590 RETURN  
4600IFXS<OTHEN4660  
4610Y=2#\*XS-1  
4620Q=（3#/16#）\*（ATN（Y/SQR（1-Y\*Y)）  
2\*\*Y\*SQR（XS-XS\*XS)+PI/2#）  
4630Q=Q/（(xs-xS\*xs)1.5）  
4640 RE(6.11.31）.  
4650 RETURN  
4660Y=SQR(XS\*XS- XS)  
4670=（3#/16\*）\*（2\*\*（1#-2\*\*XS）\*Y  
-LOG（1-2\*XS+2\*Y）)/（Y\*Y\*Y）  
4680 REN(6.11.32）.  
4690 RETURN

# Problems

1. We consider the case where the attracting focus lies on the chord $\mathcal { P } _ { 1 } \mathcal { P } _ { 2 }$ Show that it is still possible to find $\textit { a }$ Now show that for this case,

$$
p = { \frac { 2 r _ { 1 } r _ { 2 } } { r _ { 1 } + r _ { 2 } } } ~ \mathrm { a r d } ~ e \cos v _ { 1 } = { \frac { r _ { 2 } - r _ { 1 } } { r _ { 1 } + r _ { 2 } } } .
$$

With $a ^ { - } \sin a \sin a = 0$ the speeds at $\ddagger _ { 1 }$ and $\scriptstyle { \frac { \prime } { \imath } } _ { 2 }$ can be found. Since ${ \mathfrak { P } } = { \mathfrak { k } } ^ { 2 } / \mu$ theangle between the radiusvector and the velocity vector at time $\boldsymbol { \ddag _ { \perp } }$ can then be found. Then show that whether the radial distance is increasing or decreasing at $t _ { \ I }$ depends on the value of $X$ Finally,show in detail that if the operator chooses the orbital plane, then the problem can be solved.

2.If the transfer orbit is elliptic, show that the smallest possible value for $\pmb { a }$ is $( { \gamma } _ { 1 } \div { \gamma } _ { 2 } \div { \dot { c } } ) / 4$ Instead of using as initial guess for $\boldsymbol { z } _ { \mathfrak { G } }$ the quantity $2 / ( \uparrow ^ { * } \uparrow \uparrow ^ { \cdot } \uparrow ^ { * } 2 \uparrow ^ { \cdot } c )$ ,write a program in which a search is used instead of this guess,starting with z = 4/(r1+r2 +c),and diminishing it. If the orbit is hyperbolic,the search could start with $z _ { \cdot } = 0 ,$ with,again，gradual reduction.

3.If the transfer orbit is elliptic, there may be the possibility that more than one revolution can be involved. Show that if $\mathcal { m }$ revolutions are involved, then the left-hand side of (6.11.19) must be replaced by

$$
6 [ \xi \Delta t - a ^ { 3 / 2 } ( 2 m + 1 - X ) \pi \} .
$$

Generalize your program to allow for this: How will it break down if m complete revolutions are not possible?

# 6.12 The Two-Point Boundary Value Problem I-Gauss'Method

Thismethod is lengthy to derive but,when it isapplicable,probably the most efficient for computation. It uses the quantity y, defined to be the ratio of the area of the sector (i.e., the area swept out by the radiusvector during the time interval) to the area of the triangle(i.e.,the area $P _ { \mathbb { I } } S _ { \mathbb { \perp } } P _ { 2 , }$ Inapplication it is usual to assume that $\boldsymbol { s }$ is not included in the sector.

We start by considering the case of elliptic motion,again with the promise of universal formulas to come. Since $r = \hbar / a b$ twice the area of the sector is, by (6.11.9),

$$
\hbar \Delta t = a b [ ( \epsilon - \sin \epsilon ) - ( \delta - \sin \delta ) ] .
$$

If (Xi,Yi,O) and(X2,Y2,O) are the coordinates of Pi and P in the orbital reference system, then twice the area of the triangle is

$$
\begin{array} { l } { 2 \Delta = X _ { 1 } Y _ { 2 } - X _ { 2 } Y _ { 1 } } \\ { = a \bar { b } [ \sin  { E _ { 2 } } ( \cos  { E _ { 1 } } - e ) - \sin  { E _ { 1 } } ( \cos  { E _ { 2 } } - e ) ] } \\ { = a \bar { b } \left[ \sin (  { E _ { 2 } } -  { E _ { 1 } } ) - 2 e \cos \frac {  { E _ { 2 } } +  { E _ { 1 } } } { 2 } \sin \frac {  { E _ { 2 } } -  { E _ { 1 } } } { 2 } \right] } \\ { = a \bar { b } [ \sin 2 g - 2 \cos j \sin g ] } \\ { = a \bar { b } [ \sin ( \epsilon - \delta ) - ( \sin \epsilon - \sin \delta ) ] . } \end{array}
$$

Hence

$$
\begin{array} { l } { { \displaystyle { y = \frac { \hbar \varepsilon } { 2 \Delta } } } } \\ { { \displaystyle ~ = \frac { \varepsilon - \delta - ( \sin \varepsilon - \sin \delta ) } { \sin \left( \varepsilon - \delta \right) - ( \sin \varepsilon - \sin \delta ) } . } } \end{array}
$$

(6.12.1） contains $\mathfrak { a }$ implicitly, and this quantity is to be eliminated. Let

$$
v _ { 2 } - v _ { 1 } = 2 \acute { f } ,
$$

where ${ \bar { \pmb { \tau } } } _ { 1 }$ and ${ \mathfrak { V } } _ { 2 }$ are the true anomalies corresponding to $P _ { 3 }$ and $P _ { 2 }$ .Then

$$
c ^ { 2 } = \tau _ { \downarrow } ^ { 2 } + \tau _ { 2 } ^ { 2 } - 2 \tau _ { 1 } \tau _ { 2 } \cos 2 f .
$$

Now from (6.11.7) and (6.11.8),

$$
\begin{array} { c } { { 4 a ^ { 2 } \left[ 1 - \cos ( j + g ) \right] \left[ 1 - \cos ( j - g ) \right] = \left( r _ { 1 } + r _ { 2 } + c \right) \left( r _ { 1 } + r _ { 2 } - c \right) } } \\ { { = \left( r _ { 1 } + r _ { 2 } \right) ^ { 2 } - r _ { 1 } ^ { 2 } - r _ { 2 } ^ { 2 } + 2 r _ { 1 } r _ { 2 } \cos 2 \dot { f } , } } \\ { { = 4 r _ { 1 } r _ { 2 } \cos ^ { 2 } \dot { f } . } } \end{array}
$$

After some manipulation the left-hand side can be shown to be equal to

$$
4 a ^ { 2 } ( \cos g - \cos j ) ^ { 2 } ,
$$

so we have

$$
2 a ( \cos g - \cos j ) = 2 \cos f { \sqrt { r _ { 1 } r _ { 2 } } } .
$$

Multiplying through by $\cos g$ and using (6.11.4),we find

$$
r _ { \bar { 1 } } + r _ { 2 } - 2 \cos f \cos g \sqrt { r _ { 1 } r _ { 2 } } = 2 a \sin ^ { 2 } g .
$$

From (6.12.1),

$$
\begin{array} { c } { { y = \frac { \pi \xi } { \sin 2 g - 2 \sin g \cos j } } } \\ { { = \frac { a n t } { 2 \sin g \cos f \sqrt { \tau _ { 1 } \tau _ { 2 } } } . } } \end{array}
$$

Square (6.12.4), eliminate $\Re ^ { 2 }$ using $\mathfrak { r } ^ { 2 } \mathfrak { a } ^ { 3 } = \mathfrak { \mu } .$ and then substitute for $\boldsymbol { \mathfrak { Z } }$ from (6.12.2)； we get

$$
y ^ { 2 } ( r _ { 1 } + r _ { 2 } - 2 \cos f \cos g { \sqrt { r _ { 1 } r _ { 2 } } } ) = { \frac { 2 \mu t ^ { 2 } } { 4 \cos ^ { 2 } f r _ { 1 } r _ { 2 } } } .
$$

Also from (6.12.1),

$$
\begin{array} { r l } & { y - 1 = \frac { \epsilon - \delta - \sin ( \epsilon - \delta ) } { \sin ( \epsilon - \delta ) - ( \sin \epsilon - \sin \delta ) } } \\ & { \qquad = \frac { 2 g - \sin 2 g } { 2 \sin g \left( \cos g - \cos j \right) } } \\ & { \qquad = \frac { a ( 2 g - \sin 2 g ) } { 2 \sin g \cos f \sqrt { r _ { 1 } r _ { 2 } } } . } \end{array}
$$

Eliminating $\alpha$ between (6.12.4) and (6.12.6),we fnd

$$
y ^ { 2 } ( y - 1 ) = \frac { \mu t ^ { 2 } } { ( 2 \cos f \sqrt { r _ { 1 } r _ { 2 } } ) ^ { 3 } } \frac { 2 g - \sin 2 g } { \sin ^ { 3 } g } .
$$

In the notation of Gauss write

$$
1 + 2 \ell = \frac { r _ { \pm } + r _ { 2 } } { 2 \cos \ell \sqrt { r _ { \pm } r _ { 2 } } }
$$

and

$$
m ^ { 2 } = \frac { \mu t ^ { 2 } } { ( 2 \cos { f } \sqrt { \tau _ { 1 } \tau _ { 2 } } ) ^ { 3 } } .
$$

Then (6.12.5) and (6.12.7) become

$$
{ y ^ { 2 } = \frac { \pi ^ { 2 } } { \mathrm { \ddag ~ { \frac { \mathrm { 1 } } { \mathrm { 1 } } } ~ \sin ^ { 2 } ~ { g / 2 } ~ } } }
$$

and

$$
y ^ { 3 } - y ^ { 2 } = \pi z ^ { 2 } { \frac { 2 g - \sin 2 g } { \sin ^ { 3 } g } } .
$$

$\mathcal { Y }$ is the quantity to be determined from these two equations.

For the computation,define

$$
K = { \sqrt { 2 ( r _ { 1 } r _ { 2 } + r _ { 1 } \cdot r _ { 2 } ) } } = 2 { \sqrt { r _ { 1 } r _ { 2 } } } \cos f .
$$

Then

$$
m ^ { 2 } = \frac { ( k \Delta t ) ^ { 2 } } { K ^ { 3 } } ,
$$

and

$$
\ell = \frac { { { \sf r } _ { 1 } } + { { \sf r } _ { 2 } } - K } { 2 K } .
$$

Further,define

$$
{ \mathfrak { x } } ^ { * } = \sin ^ { 2 } { \frac { \mathfrak { z } } { 2 } } { \mathfrak { g } } .
$$

Then

$$
( 2 g - \sin 2 g ) / \sin ^ { 3 } \frac { 1 } { 2 } g = \frac { 4 } { 3 } Q ( x ^ { * } ) ,
$$

where $Q$ is the function discussed in the preceding section. The two equations to be solved can now be written as

$$
\left. \begin{array} { c } { { \varepsilon ^ { * } = \displaystyle \frac { m ^ { 2 } } { y ^ { 2 } } - \ell , } } \\ { { y = 1 + \left( m ^ { 2 } / y ^ { 2 } \right) \frac { 4 } { 3 } Q ( x ^ { * } ) . } } \end{array} \right]
$$

Note that these formulas are valid if the transfer orbit is hyperbolic.

A possible method for solving these equations,and one that is used in the program that follows,is Steffensen's method. One step can be summarized as follows:

$$
\left. \begin{array} { c } { { \displaystyle x _ { i } ^ { * } = \frac { \vec { m } ^ { 2 } } { y _ { i } ^ { 2 } } - \ell , } } \\ { { \displaystyle y _ { i + 1 } = 1 + \left( \frac { m ^ { 2 } } { y _ { i } ^ { 2 } } \right) \frac { 4 } { 3 } \mathcal { Q } ( x _ { i } ^ { * } ) , } } \end{array} \right| i = 1 , 2 .
$$

The new estimate of $\mathcal { Y }$ is

$$
y = y _ { 1 } - \frac { ( y _ { 2 } - y _ { 1 } ) ^ { 2 } } { y _ { 1 } - 2 y _ { 2 } \div y _ { 3 } } .
$$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0081-0120/ocr/images/83052ea7b2803a497cb2fe2ca9aaae5941ab0321df533f3dd0a171a92d98ecc3.jpg)

A good starting guess for y is yo = 1.

Once $y$ is known, then it is necessary to find the $f$ and $\mathfrak { g }$ functions. Since

$$
{ \displaystyle { \bf r } _ { 2 } = f { \bf r } _ { 1 } + g { \bf v } _ { 1 } } ,
$$

then

$$
\mathbf { r } _ { \mathrm { 1 } } \times \mathbf { r } _ { \mathrm { 2 } } = g \mathbf { \hat { a } } .
$$

Now the area of the sector is $\frac { 1 } { 2 } \hbar \Delta \tt t$ and that of the triangle is $\frac { 1 } { 2 } | \tt E _ { I } \times \tt E _ { 2 } |$ Therefore $y = \Delta t / g$ or

$$
g = { \frac { \Delta \mathit { t } } { \mathit { y } } } .
$$

Also

$$
\begin{array} { l } { f = \displaystyle 1 - \frac { a } { r _ { 1 } } ( 1 - \cos \Delta E ) } \\ { = \displaystyle 1 - \frac { 2 } { r _ { 1 } } a \sin ^ { 2 } g . } \end{array}
$$

But from (6.12.4),

$$
\alpha \sin ^ { 2 } g = \frac { ( k \Delta t ) ^ { 2 } } { K ^ { 2 } y ^ { 2 } } .
$$

So

$$
f = 1 - 2 \frac { ( k \Delta t ) ^ { 2 } } { K ^ { 2 } y ^ { 2 } \tau _ { \mathrm { \vec { r } } _ { \mathrm { \vec { \perp } } } } } .
$$

This completes the formulas needed to solve the problem.

A listing of a program for accomplishing this solution follows.

REN THE TWO-POINT BOUNDARY VALUE PROBLEN.   
REM APPLICATION OF THE HETHOD OF GAUSS.   
CLS   
DEFDBL A-H ,O-Z :DEFINT N   
PRINT 'ENTER COORDINATES OF THE INITIAL POSITION "   
INPUT X1,Y1,Z1 :PRINT   
PRINT ENTER'COORDINATES OF THE FINAL POSITION   
80INPUT X2,Y2,Z2:PRINT   
90 INPUT ENTER THE TIHE INTERVAL ；DT:PRINT   
100 INPUT "ENTER THE VALUE OF HU ；NU ：PRINT   
110 GK=SQR(HU）   
120 PI=3.141592653589793#   
130 R1 =SQR(X1\*X1 +Yi\*Y1 + Z1\*Z1）   
140R2= SQR（X2\*X2+Y2\*Y2+Z2\*22）   
150 KAY= SQR（28\*（R1\*R2 +X1\*X2 +Y1\*Y2 +Z1\*Z2)）   
160 REH(6.12.10）.   
170GOSUB 4OOO :REN FIND THE SECTOR-TRIANGLE RATIO.   
180F= 1-2\*（GK\*DT）\*（GK\*DT）/（KAY\*KAY\*YG1\*YG1\*R1）   
190G=DT/YG1:REH(6.12.16)AND （6.12.17）   
200 xv1 =（X2-F\*X1）/G   
210 Y1 = （Y2-F\*Y1）/G   
220 zv1 = （Z2-F\*Z1）/G   
230 PRINT XVi,YV1,ZV1   
240 END   
4000 REN SUBROUTINE FOR FINDING GAUSS’ SECTOR-TRIANGLE RATIO. 4010 HS= （GK\*DT）\*（GK\*DT）/（KAY\*KAY\*KAY）   
4020 EL=（R1+B2-KAY）/(28\*KAY):REN（6.12.11)AND（6.12.12）. 4030 YG1 = 1 :REH INITIAL GUESS.   
4040 XS =MS/（YG1\*YG1)-EL   
4050GOSUB 4500   
4060YG2=1÷（4#\*HS\*Q)/(3#\*YG1\*YG1):REM（6.12.14）.   
4070 XS=NS/(YG2\*YG2)-EL   
4080GOSUB 4500   
4090 YG3= 1+（4#\*NS\*Q)/（3\*YG2\*YG2）   
4100DEN=(YG1-YG2-YG2+YG3)   
4110IF ABS（DEN)<1E-15 THEN 4170   
4120DY=(YG2-YG1）\*（YG2-YG1）/DEN   
4130YG1= YG1- DY REN APPLICATION OF STEFFENSEN'S METHOD.   
4150 PRINT YG1   
4160IF ABS(DY)>1E-15 THEN 4040   
4170 RETURN   
4500IF ABS(XS)>.1THEN 4590   
4510 FAC= i.2\*XS   
4520Q=1÷FAC   
4530FORN=1T010 DN=N FAC=FAC\*XS\*（3÷DN）/(2.5+DN） Q=Q+FAC   
4570NEXTN:REH（6.11.29）.   
4580 RETURN   
4590IFXS<O#THEN4650   
4600Y=2#\*XS-1   
4610Q=（3#/16#)\*（ATN（Y#/SQR(1-Y\*Y）） 2#\*Y\*SQR(XS-XS\*XS)+PI/2)   
4620Q=Q/（（xs-xS\*Xs）1.5#） REH(6.11.31）.   
4640 RETURN   
4650Y=SQR(XS\*XS-XS）   
4660Q=（3/16#）\*（2\*（1-2\*XS）\*Y -LOG（1-2\*XS+2\*Y）)/（Y\*Y\*Y） REH（6.11.32）.   
4680 RETURN

# 6.13The Two-Point Boundary Value Problem III-The Method of Herrick and Liu

This is an attractive method that requires only the formulas for the $f$ and $g$ functions. The unknown quantity to be found by iteration is $\mathfrak { P }$ the parameter of the conic, and the method is sometimes referred to as the $z _ { p }$ iterationmethod." It fails (as do others)if the chord $P _ { \mathbb { I } } P _ { 2 }$ passes through the attracting focus （for $\mathfrak { P }$ is determined, but the orbit is not),but is otherwise valid for any type of orbit. The operator of the program will need to decide whether or not the orbital segment does not include $\{ \pmb { Y } = 1 \} ,$ ordoes include $( Y = - I )$ the attracting focus.If the orbit is elliptic,we shall assume that the transfer is accomplished in less than one complete revolution.

If $\mathfrak { v } _ { 1 }$ and ${ \mathfrak { V } } _ { 2 }$ are the respective true anomalies at the points $P _ { \mathrm { I } }$ and $P _ { 2 }$ ,then

$$
\begin{array} { l } { C = \cos ( v _ { 2 } - v _ { 1 } ) = \frac { \mathtt { F } _ { 1 } \cdot \mathtt { F } _ { 2 } } { r _ { 1 } r _ { 2 } } \bigg ] } \\ { \quad } \\ { \quad \mathrm { s i n } ( v _ { 2 } - v _ { 1 } ) = Y \sqrt { 1 - C ^ { 2 } } . } \end{array}
$$

Now from (6.7.9),

$$
\left. \begin{array} { l } { f = \displaystyle \frac { r _ { 2 } } { p } [ \cos ( v _ { 2 } - v _ { 1 } ) - 1 ] + 1 , } \\ { g = \displaystyle \frac { r _ { 1 } r _ { 2 } } { \sqrt { \mu p } } \sin ( v _ { 2 } - \dot { v } _ { 1 } ) , } \\ { \mathrm { v _ { 1 } } = \displaystyle \frac { r _ { 2 } - f \mathrm { { r } } _ { 1 } } { g } , } \end{array} \right. .
$$

where we assume that g≠0.

If p is estimated, V1 can be calculated,and the vectors r1 and v1 used to find the resulting position vector,r\*,at the end of the time interval △t. Then we can find the cosine of the angle between r1 and r\*

$$
\begin{array} { r } { C ^ { * } = \frac { \overrightarrow { \bf \nabla } _ { 1 } \cdot \overrightarrow { \bf \nabla } _ { 3 } \cdot } { \overrightarrow { \bf \nabla } _ { 3 } \cdot \overrightarrow { \bf \nabla } _ { 1 } \cdot \overrightarrow { \bf \nabla } _ { 3 } } . } \end{array}
$$

This must be compared with C from (6.13.1),and then p must be changed in order to drive the difference

$$
D ( \mathfrak { p } ) = C - C ^ { \ast }
$$

to zero. Once this has been done,the problem is solved, because the velocity $\yen 1$ is known.

As stated, this procedure can, however,lead to a false solution. When r\* is found from r1and vi,a “g” function is calculated; fora valid solution, this should have the same sign as Y.If this is not the case, the solution will be false.and a new search will be needed.

In the program that follows, the secant method is used for the iteration. First,there is a search for an interval in which D(p) changes sign.For the search, the program requires a starting value for p and an increment.p is stepped up by this increment until either D(p) changes sign,or there is no change after a specified number of trials. In the former case the secant method takes command; in the latter case the program stops,and different input values for p and its increment are needed. The program uses much of that from section 6.10.

REM TWO-POINT BOUNDARY VALUE PROBLEN.   
REN THE "P-ITERATION' METHOD.   
REM   
REH THE SUBROUTINE STARTING AT LINE 2OOO FOR SOLVING REH KEPLER'S EQUATION IN UNIVERSAL VARIABLES HAS BEEN REH OHITTED FROK THIS LISTING.SEE SECTION 6.10. REH   
REH TO CONFORN WITH THE NOTATION FOR UNIVERSAL   
REH VARIABLES,THE SUBSCRIPTS ARE O AND 1,NOT,AS 100 REM IN.THE TEXT,1 AND 2.   
110 REH   
120 CLS   
130DEFDBL A-H,O-Z:DEFINT   
140 PRINT ENTER COORDINATES OF THE INITIAL POSITION "   
150 INPUT XO,YO,ZO:PRINT   
160 PRINT ENTER COORDINATES OF THE FINAL POSITION "   
170 INPUT X1,Y1,Z1: PRINT   
180 INPUT ENTER THE TIKE INTERVAL :DT :PRINT   
190 INPUT ENTER THE VALUE DF HU；HU :PRINT   
200 PRINT "ENTER +1# IF THE ORBITAL ARC DOES NOT INCLUDE THE" 210 INPUT "ATTRACTING FOCUS；OTHERVISE,ENTER-1\*；YY 220 PRINT :PRINT ENTER A TRIAL VALUE FOR P AND AN   
230 PRINT "INTERVAL, DP TO BE USED IN THE INITIAL SEARCH " 240 INPUT P,DP ：

250RO=SQR（XO\*XOYO\*YO+Z0\*Z0）   
260 R1 = SQR(X1\*X1 + Y1\*Y1 + Z1\*Z1)   
270 CDF=（XO\*X1+YO\*Y1+ZO\*Z1）/（RO\*R1）   
280SDF=YY\*SQR（1\*-CDF\*CDF):REH（6.13.1）   
290 NSEC=0   
300 REM NSEC =O DURING THE PRELIMINARY SEARCH,AND 1 WHEN   
310 REH THE SECANT HETHOD IS IN PROGRESS.   
320 REH   
330 NTEST=1   
340 REN NTEST COUNTS THE NUNBER OF INCREMENTS IN THE   
350 REM INITIAL SEARCH.IF A SOLUTION IS NOT BRACKETED   
360 REN AFTER TEN INCREMENTS，THE OPERATOR HAS THE CHOICE   
370 REN OFENDING THE PROGRAN OR CHOOSING DIFFERENT P,DP.   
380 REM   
390 P2=P   
400F=R1\*（CDF-18）/P2+1#   
410 G=RO\*R1\*SDF/SQR（NU\*P2）   
420 xvo =（xi-F\*XO）/G   
430 YVO=（Yi-F\*YO）/G   
440 ZVO=（Zi-F\*ZO）/G:REN（6.13.2）   
450 VOS= XVO\*XVO+YVO\*YVO+ZVO\*ZVO   
460U=XO\*XVO+YO\*YVO+ ZO\*ZV0   
470 ALPHA = 2#\*HU/RO - VOS   
475 SDT=DT   
480GOSUB 2OOO :REN SOLVE KEPLER'S EQUATION   
485 DT = SDT   
490 F=1-（NU/RO）\*C2   
500G=DT-U\*C3   
510FDOT=-（HU/（FP\*RO)）\*C1   
520GDOT=1\*-（HU/FP）\*C2   
530X=XO\*F÷XVO\*G   
540Y=Y0\*F+YVO\*G   
550Z=Z0\*F÷ZV0\*G   
560 CAF=(XO\*X÷YO\*Y+ZO\*Z)/(RO\*SQR(X\*X÷Y\*Y+ Z\*Z)）   
570DEL2=CDF-CAF   
580PRINT P2,DEL2   
590 IF NSEC=1 THEN65O :REH（6.13.3)AND （6.13.4).   
600IF NTEST=1 THEN620   
610IF DEL1\*DEL2<O\* THEN640   
620 NTEST=NTEST+1 :IFNTEST>1O THEN 720   
630 DEL1 $=$ DEL2:P1=P2:P2=P1÷DP:GOTO400   
640 NSEC =1   
650DP= - DEL2\*(P2- P1)/(DEL2- DEL1)   
660 REK APPLICATION OF THE SECANT METHOD.   
670IF ABS(DP)<1E-14 THEN690   
680P1=P2:P2=P2+DP:DEL1 $=$ DEL2:GOT0400   
690IF G\*YY<O THEN GOTO 710   
700PRINT XVO,YVO,ZVO:END   
710 PRINT "FALSE SOLUTION."   
720 INPUT "ENTER 1 FOR ANOTHER TRY,2 TO QUIT；NN   
730ONNNG0TO 220,740   
720 END

With INPUT the same as that for the numerical example mentioned in section 6.11,the following iterations resulted:

p D（p)   
Search:1.0 -.397080 507304 5806   
1.5 -.290 793803873 9674   
2.0 -.2060136544382135   
2.5 -.139 279049 922 9185   
3.0 -.086129099 4391113   
3.5 -.043 0281042262790   
4.0 -.007428418756 8987   
4.5 +.0224750449176905   
Iteration:4.124206661103461   
4.116104006191029   
4.116 600642 601455   
4.116 600 000 054286   
4.116 599999999 998

# 6.14Some Expansions in Elliptic Motion

Although the formulas for elliptic motion make it possible to calculate the position of a planet in its orbit at any time,it would be useful to have this position given directly by one formula. Unfortunately Kepler's equation proves a stumbling block to this,but if it can be solved asa series,then we can find series expansions for r and v,in particular, in terms of M and e. The development of these series for their useful application (particularly to perturbation theory) demands the use of Bessel functions,and is considered outside the scope of this text.The reader should consult the texts by Smart or Plummer (Refs. 29,26) for full accounts. Here we shall be content to fnd the first few terms in three expansions.

Consider Kepler's equation

$$
M = E - e \sin \angle 2 .
$$

If e = O, then E= M,and if e is very small,M will be a reasonable first approximation to $E$ If we write Kepler's equation in the form

$$
\begin{array} { r } { \Xi ^ { \prime } = \mathbb { M } \div e \sin \mathcal { E } , } \end{array}
$$

then, given some value $\Xi _ { i }$ ,which is approximate, a better one is

$$
\begin{array} { r } { \vec { E } _ { i + \mathtt { i } } = \vec { M } \div e \sin \vec { E } _ { i } . } \end{array}
$$

So,starting off with $E _ { \ I } = M$ we have

$$
E _ { 2 } = M + e \sin M ,
$$

and

$$
\begin{array} { r l } & { E _ { 3 } = M + \epsilon \sin ( M + e \sin M ) } \\ & { \quad = M + e [ \sin \ M \cos ( e \sin M ) + \cos \ M \sin ( e \sin M ) ] . } \end{array}
$$

$E _ { 3 }$ is only an approximate value, correct to the order $e ^ { 2 }$ ： $\boldsymbol { \mathfrak { s o } } _ { \mathfrak { z } }$ consistent with this approximation,

$$
\begin{array} { r } { E _ { 3 } = \mathcal { M } + e \sin \mathcal { M } + e ^ { 2 } \sin \mathcal { M } \cos \mathcal { M } . } \end{array}
$$

f $e ^ { 3 }$ is negligible, this solution will be good enough; if $\Re \Re \dag$ we can find the term in $e ^ { 3 }$ by writing down $E _ { 4 }$ and neglecting $e ^ { 4 }$ We find

$$
\begin{array} { r } { \ E _ { 4 } = M + e \sin M + \frac { 1 } { 2 } e ^ { 2 } \sin 2 M + \frac { 1 } { 8 } e ^ { 3 } ( 3 \sin 3 M - \sin M ) . } \end{array}
$$

This process can be continued indefinitely,although the later terms obviously become unwieldy.

The following method for finding $\mathcal { T }$ in terms of $\mathcal { E }$ and $\tilde { \beta } \tilde { \mathcal { Z } }$ is due to MacMillan, as given by Moulton (Ref.11). From Kepler's equation

$$
e \frac { \partial \vec { \mathbf { z } } } { \partial e } = \frac { e \cdot \mathrm { s i n } \vec { \mathbf { z } } } { 1 - e \cos \vec { \mathbf { z } } } ,
$$

and

$$
d \vec { \mathcal { M } } = ( \mathbb { i } - e \cos \vec { \mathcal { E } } ) d \vec { \mathcal { E } } ,
$$

so that

$$
e \frac { \partial E } { \partial e } d \vec { M } = \stackrel { , } { e } \mathrm { s i } \hbar \overline { { E } } d \vec { E } .
$$

This can be integrated to give

$$
e \int _ { 0 } ^ { M } \frac { \partial E } { \partial e } d M = - e \cos { E } + \mathrm { c o u s t a n t } .
$$

Substituting the series for $\mathcal { E }$ in terms of $e$ and $\tilde { \mathcal { M } }$ ,we find

$$
- e \cos { E } = \cos { \sin } + e \int _ { 0 } ^ { { \sin } } ( \sin { M } + e \sin 2 M + \cdots ) d M
$$

or, since $r / a = 1 - e \cos \mathcal { E }$

$$
\frac { \tilde { r } } { a } = \mathbf { i } + c - e \cos M - \frac { \mathbf { i } } { 2 } e ^ { 2 } \cos 2 M + \cdot \cdot \cdot
$$

where $^ c$ is a constant still to be found. Assuming that the series is uniformly convergent (which is the case for moderate e), we can integrate both sides of the equation with respect to $\Im \hat { \mathcal { M } }$ between the limits $\tilde { \beta } \tilde { \mathcal { Z } } = 0$ to $M = 2 \pi$ ,integrating the series term by term. Hence

$$
\int _ { 0 } ^ { 2 \pi } { \frac { r } { a } } d M = 2 \pi ( 1 + c ) - e \int _ { 0 } ^ { 2 \pi } \cos M d \bar { M } - \cdot \cdot \cdot
$$

The trigonometric terms all vanish when integrated between these limits. To evaluate the left-hand side,wenote that $\pi f a$ and $d M$ can easily be put in terms $\mathcal { E }$ and $\vec { a } \vec { E }$ and we find

$$
2 \pi \{ 1 \div { \textstyle \frac { 1 } { 2 } } e ^ { 2 } \} = 2 \pi ( 1 \div c ) ,
$$

so that $\textstyle c = { \frac { \mathtt { i } } { 2 } } e ^ { 2 }$ Then

$$
\frac { r } { a } = 1 - e \cos M - \frac { 1 } { 2 } e ^ { 2 } ( \cos 2 M - 1 ) - \frac { 1 } { 8 } e ^ { 3 } ( \cos 3 M - 3 \cos M ) - \cdot \cdot \cdot
$$

To find the series for $\mathfrak { v }$ ,differentiate equation (6.3.17), and eliminate sin $\mathfrak { V }$ using(6.3.18）； then

$$
d v = \frac { \sqrt { \frac { 1 } { 2 } - e ^ { 2 } } } { ( 1 - e \cos \mathcal { E } ) ^ { 2 } } d \vec { M } ,
$$

and by Kepler's equation this reduces to

$$
\acute { a } v = \sqrt { 1 - e ^ { 2 } } \left( \frac { d E } { d M } \right) ^ { 2 } d \acute { z } M .
$$

The procedure is to use the series for E in terms of M to find dE/dM, square it,multiply it into V1-e² as a power seriesine,and then integrate. The final result is

$$
\begin{array} { r } { v = M + 2 e \sin M + \frac { 5 } { 4 } e ^ { 2 } \sin 2 M + \frac { 1 } { 1 2 } e ^ { 3 } ( 1 3 \sin 3 M - 3 \sin M ) + \cdot \cdot \cdot } \end{array}
$$

It is obvious in this case we have no trouble over the constant of integration. This expansion [or, more specifically, the expansion of $\{ v - M \} ]$ is called the equation of the center.

The reader will find additional expansions in Appendix D.

# Problems

1. Show that if fourth and higher powers of e are neglected, then

$$
\ E = M + { \frac { e \sin M } { 1 - e \cos M } } - { \frac { 1 } { 2 } } \left( { \frac { e \sin M } { 1 - e \cos M } } \right) ^ { 3 }
$$

is a solution of Kepler's equation.

2. Show that the equation of the center, $\{ v - \mathbb { M } \}$ ,is given in terms of the true anomaly $\mathfrak { V }$ by the expression

$$
\sum _ { p = 1 } ^ { \infty } ( - 1 ) ^ { p - 1 } { \frac { 2 \lambda ^ { p } \{ ( p + 1 ) - ( p - { \frac { 1 } { 4 } } ) \lambda ^ { 2 } \} } { p ( 1 + \lambda ^ { 2 } ) } } \sin p v ,
$$

where

$$
\lambda = { \frac { e } { 1 \div { \sqrt { 1 - e ^ { 2 } } } } } ,
$$

with $e$ being the eccentricity of the orbit. Show that the maximum value of the equation of the center occurs approximately when

$$
v = { \frac { \pi } { 2 } } \div \sin ^ { - 1 } \left\{ { \frac { 3 e } { 4 } } \right\} ,
$$

e being small.

3. Show that if the eccentricity $\pmb { \mathcal { e } }$ is small and $e ^ { 3 }$ is neglected,

$$
r = a ( \mathrm { i } - e \cos n \mathrm { i } + e ^ { 2 } \sin ^ { 2 } n \mathrm { i } )
$$

and

$$
\begin{array} { r } { \omega = \pi ( \mathbb { i } \div \frac { \mathbb { i } } { 2 } e ^ { 2 } \cos 2 \pi \mathbb { i } ) , } \end{array}
$$

where $\gamma$ is the radius vector, $\pmb { \hat { \tau } }$ the time measured from the nearer apsis, $2 \pi / \pi$ the period, $\alpha$ the semimajor axis, and $\omega$ the angular velocity about the empty focus.

Hence show that the Moon always very nearly turns the same face to that focus of its orbit in which·the Earth is not situated.

4. If the origin is at the center of force and the $\pmb { \mathcal { X } }$ -axis points toward pericenter,show that the coordinates in an elliptic orbit are $( x , y )$ where

$$
{ \frac { x } { a } } = \cos M + { \frac { 1 } { 2 } } e ( \cos 2 M - 3 ) + { \frac { 1 } { 8 } } e ^ { 2 } ( 3 \cos 3 M - 3 \cos M ) + \cdot \cdot \cdot
$$

and

$$
\frac { y } { a } = \sin M + \frac { 1 } { 2 } e \sin 2 M + \frac { 1 } { 2 4 } e ^ { 2 } ( 9 \sin 3 M - 1 5 \sin M ) + \cdot \cdot \cdot
$$

5. Derive two extra terms for each of the three series developed in this section.

# 6.15The Orbit in Space

The six constants of integration found in Sections 6.2 and 6.3 complete the formal solution to the problem,but they are not ina form that is immediately iseful to the astronomer. Any set of six independent constants will suffice, but those usually used will now be described: they are known as the elements of the orbit.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0081-0120/ocr/images/0381b0ad823ccd5c4101bf3029e929726ac6229b59e3feb9a1eb94616269cfc1.jpg)  
Figure 6.9

In Figure 6.9 the Sun is at $o$ ： $\boldsymbol { \wp } _ { \mathcal { Z } }$ points toward the vernal equinox and $\scriptscriptstyle \mathcal { O } z$ toward the north pole of the ecliptic. Let the plane of the orbit cut the celestial sphere in the great circle HPA, where H is the point where the body in its orbit rises north of the ecliptic, called the ascending node. The point at which the body crosses the ecliptic, moving south,is the descending node. The angle xOH is the longitude of the ascending node; it is written &. This angle is measured eastward around the ecliptic. The angle between the plane of the orbit and the ecliptic (or the angle between h and z) is called the inclination; it is written i.ialways lies between O and 180o.For O°≤i<90°the orbit is direct; for 90°<i<180° the orbit is retrograde.If OP is the direction of perihelion, the angle HOP is caled the argument of perihelion; it is written w. The quantity $\tilde { \omega }$ ,defined by

$$
\tilde { \omega } = \Omega \div \omega
$$

is the longitude of perihelion; it is measured first in the ecliptic to the ascending node,and then in the plane of the orbit to the direction of perihelion.The remaining three elements of the elliptic orbit are a,e,and T.For a parabolic orbit only five elementsare needed; ${ \pmb q } .$ theperiheliondistance,replaces $\pmb { \mathscr { Q } }$ ande.

is an element that can be used instead of $\omega$ There are other alternatives to the elements defined above. For instance it may be convenient to replace $\mathfrak { T }$ by

$$
\chi = - \pi \mathcal { T } .
$$

The true longitude of $\hat { \mathbf { a } }$ planet is the angle measured from the vernal equinox, first along the ecliptic to the ascending node,and then in the direction of the orbit to the planet.Denoting this by $\pmb { \cal \hat { L } }$ we have

$$
\mathcal { L } = \tilde { \omega } + v = \Omega + \omega + v = \Omega + \mathcal { U } ,
$$

where $\mathcal { U }$ is the angle HOA, $A$ being the position of the planet on the celestial sphere; $\mathfrak { U }$ iscalled the argument of the latitude of the planet. The mean longitude lof the planet is defined by

$$
\tilde { \iota } = \tilde { \omega } + n ( t - T ) = \tilde { \omega } + \tilde { M } .
$$

When $t = 0$ we have an epoch (which can, of course, be any convenient date); the value of $\pmb  \}$ when $\xi = 0$ is

$$
\epsilon = \tilde { \omega } - \eta \tilde { \mathcal { Z } } = \tilde { \omega } \div \chi ,
$$

which is the mean longitude at the epoch.

The angles $\beta$ and $i$ depend on the direction of h. Let $\hat { \bf \Phi } _ { \hat { \bf a } }$ have components $( \hat { h } _ { x } , \hat { h } _ { y } , \hat { h } _ { z } )$ Then

$$
\hat { \boldsymbol { h } } _ { z } = \hat { \boldsymbol { \mathrm { z } } } \cdot \hat { \boldsymbol { z } } = \cos \hat { \boldsymbol { \mathrm { z } } } .
$$

Let the unit vector along $O H$ be；this has components $( \cos \alpha , \sin \alpha , 0 )$ But $\hat { \tilde { z } } \times \hat { \tilde { \textbf { \textit { k } } } } = \hat { \textmd { n } } \hat { \textmd { s i n } } \hat { \tilde { z } }$ ,s0

$$
( - \hat { h } _ { y } , \hat { h } _ { z } , 0 ) = \hat { \mathbf { s } } \hat { \mathbf { s } } \hat { \mathbf { a } } i ( \cos \Omega , \sin \Omega , 0 ) ,
$$

and

$$
\begin{array} { c } { { \hat { h } _ { x } = \sin \Omega \sin i \quad \hat { 1 } } } \\ { { - \hat { h } _ { y } = \cos \Omega \sin i , } } \\ { { \hat { h } _ { z } = \cos i . } } \end{array}
$$

The angle $\omega$ can be found formally from the unit vector $\mathcal { P }$

We consider two programs. In the first,the INPUT will consist of a set of elements, and the OUTPUT will be the components of position and velocity at $\clubsuit$ given time t. The elements will be based on the ecliptic,and the coordinate axes for resolving the vectors will be equatorial. $\Sigma$ a vector has components $\{ X , Y , Z \}$ in the orbital reference system, and $\{ x , y , z \}$ in the equatorial system, then

$$
\left[ \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right] = P ( - \epsilon ) R ( - \Omega ) P ( - i ) R ( - \omega ) \left[ \begin{array} { l } { X } \\ { Y } \\ { Z } \end{array} \right] .
$$

(See Appendix $\mathfrak { B }$ for the definition of the rotation matrices.） I suggest the following sequence of calculations:

$\curvearrowleft$ Find the components of position and velocity at the time of perihelion in the orbital reference system.   
Rotate these to the equatorial system.   
Use the $f$ and $g$ functions to calculate components at the given time t.

If the elements contain, not the time of pericenter, but the mean anomaly at the epoch $t _ { \mathbb { G } }$ ,then the first step should be to find the components of position and velocity at $\ddagger _ { 0 }$ in the orbital reference system.

A partial listing showing the rotations and a possible subroutine for the :otations follows.

REH THIS PROGRAN HAS AS INPUT A SET OF KEPLERIAN RENELEHENTS,a,，i（INC)，TP(TIMEOF PERICENTER), REM Iittle Omega (AP),AND BIG DHEGA (LAN)； REN ALSO,A TIME T AT VHICH COMPONENTS OF POSITION REH AND VELOCITY ARE REQUIRED. THE ELEHENTS ARE REHREFERRED TO THE ECLIPTIC.VECTORS WILL BE REN RESOLVED IN THE EQUATORIAL REFERENCE SYSTEK. REM   
DEFDBL A-,O-Z :DEFINT   
100 CLS   
110 PI= 3.141592653589793   
120 GOSUB 5OOO :REM ENTER DATA.   
130 GDSUB 5500   
140 REM THIS VILL GIVE THE CONPONENTS OF POSITION   
150 REN AND VELOCITY AT THE TIME OF PERICENTER,TP.   
160 TO = TP   
170 REH YOU HUST INSERT HERE THE PROGRAN FROH SECTION 6.10   
180 REH THAT VILL FIND COHPONENTS OF POSITION AND   
190 REN VELOCITY AT TINE T. YOU VILL START FRON   
2000   
5006 PRINT   
5010 PRINT   
5020 INPUT "ENTER THE INCLINATION，IN DEGREES " ；INC   
5030PRINT   
5040 INC= INC\*PI/180   
5050 INPUT ENTER THE LONGITUDE OF THE ASCENDING NODE "；LAN   
5060 PRINT ,-

5070LAN= LAN\*PI/180  
5080 INPUT "ENTER THE ARGUNENT OF PERICENTER " ； AP  
5090 PRINT  
5100 AP= AP\*PI/180  
5110 INPUT "ENTER THE TIHE OF PERICENTER " ；TP  
5120 PRINT  
5130 PRINT ENTER THE TIHE AT VHICH THE COKPONENTS OP  
5140 INPUT POSITION AND VELOCITY ARE REQUIRED "；T  
5150 PRINT  
5160 DBL=.4090928 :REN OBLIQUITY OF THE ECLIPTIC  
5170 RETURN  
5500XC=A\*（1#-E）:YC=O:ZC=0  
5510 REM COORDINATES OF PERICENTER IN THE ORBITAL  
5520 REM REFERENCE SYSTEN.  
5530 TH=-AP:NR=3:GOSUB5710  
5540 TH =- INC : NR $= \sharp$ ：GOSUB 5710  
5550 TH=-LAN :NR $= 3$ ：GOSUB 5710  
5560TH=-OBL:NR $\equiv \textbf { \ 4 }$ :GOSUB_5710  
5570 REH THE POSITION VECTOR IS NOV RESOLVED IN  
5580 REN THE EQUATORIAL REFERENCE SYSTEM.  
5590 X0=XC:Y0 5600 $\begin{array} { r c l } { \texttt { X U } = } & { \texttt { A C } : \texttt { Y U } = } & { \texttt { Y U } : \texttt { L U } = \texttt { L U } = \texttt { L U } } \\ { \texttt { X C } = } & { \texttt { O E } : \texttt { Y C } = } & { \texttt { S Q R } \big ( \texttt { R U * ( I * ~ E ) / ( A * ( I * ~ - ~ E ) ) } \big ) \texttt { : Z C } = \texttt { O 2 } } \end{array}$ $z 0 = z c$   
5610 REH COMPONENTS OF THE VELOCITY AT PERICENTER  
5620 REN IN THE ORBITAL REFERENCE SYSTEN.  
5630 TH=-AP:NR $= 3$ ：GOSUB 5710  
5640T $=$ -INC :NR $\textbf { = 1 }$ :GOSUB 5710  
5650TE - LAN:NR $\ r = \ r _ { 3 }$ :GOSUB 5710  
5660 T $\risingdotseq$ -OBL:NR $\equiv \ 1$ ：GOSUB_5710  
5670 REH THE VELOCITY VECTOR IS NOV RESOLVED IN  
5680 REN THE EQUATORIAL REFERENCE SYSTEN.  
5690 $X V \cdot \theta = I C = \frac { 1 } { 2 } \times \frac { 1 } { 4 } = \frac { 1 } { 2 } \times \frac { 1 } { 4 } = \frac { 1 } { 2 } \times \frac { 1 } { 4 } = \frac { 1 } { 2 } \times \frac { 1 } { 4 }$   
5700 RETURN  
5710 REN THIS SUBROUTINE ROTATES COORDINATES THROUGH  
5720 REM THE ANGLE TH；NR IS 1,2,3 FOR ROTATIONS  
5730 REHAROUND THE X,Y,AND 2 AXES,RESPECTIVELY.  
5740.0NNRG0T05750,5790,5830  
5750YCT=YC\*COS（TH)+ZC\*SIN（TH）  
5760 ZC=-YC\*SIN（TH)+ZC\*COS(TH）  
5770 YC=YCT  
5780 RETURN  
5790 XCT = XC\*COS(TH)- ZC\*SIN（TH)  
5800 ZC=XC\*SIN（TH） $\pmb { \phi }$ ZC\*COS（TH）  
5810 XC = XCT  
5820 RETURN  
5830 XCT= XC\*COS(TH)+ YC\*SIN（TH）  
5840YC=-XC\*SIN（TH）+YC\*COS（TH）  
5850 XC= XCT  
5860 RETURN

In the second program (which should be debugged alongside the frst） the INPUT will consist of components of position and velocity at some time $\pmb { \xi }$ and the OUTPUT will be a set of elements. A completely general program would allow for the cases $i = 0$ (when $\Omega$ is undefined)and $e = \mathfrak { F }$ (when $\omega$ isundefined). Ileave such refinements to you; but we will consider the possibilities of parabolic orhyperbolic orbits.

A drawback with BASIC and some other languages is that, of the inverse trigonometric functions,only tan-1 is available,with OUTPUT in the interval $( - 9 0 ^ { 0 } , 9 0 ^ { 0 } )$ In FORTRAN there is the function DATAN2 $\left\{ \mathbb { Z } , \ Y \right\}$ ，where $\pmb { \chi }$ and $\gamma$ are numbers proportional to the cosine and sine of the angle (i.e., $\chi =$ $\gamma \cos \theta , Y = r \sin \theta ; \ r > 0 )$ and the value of the function is the angle with tangent $\gamma / X$ in the interval $\{ 0 ^ { \circ } , 3 6 0 ^ { \circ } \}$ If you are not using FORTRAN, I suggest that you write a subroutine to do the same job.

The formulas to be used here (and the algorithm that follows is not the only one possible)are: ：

$$
( \hbar _ { z } , \hbar _ { y } , \hbar _ { z } ) = \hbar = \tau \times \mathbf { v } .
$$

$$
( e _ { x } , e _ { y } , e _ { z } ) = \mathbf { e } = { \frac { \mathbf { \hat { s } } } { \mu } } = { \frac { \mathbf { v } \times \mathbf { h } } { \mu } } - { \hat { \mathbf { r } } } .
$$

Now let n point toward the ascending node, so that $\hat { \mathbf { z } } = \{ \cos \boldsymbol { \mathfrak { T } } , \sin \boldsymbol { \mathfrak { T } } , 0 \}$ .Then, since $\boldsymbol { \cdot } \ e = e \cos \omega$

$$
\cos \omega = e _ { x } \cos \Omega + e _ { y } \sin \Omega .
$$

Also

$$
\hat { \mathfrak { a } } \times \mathbf { e } = ( e \sin \omega ) \hat { \mathbf { b } }
$$

and

$$
\hat { \mathbf { n } } \times \mathbf { e } = ( e _ { z } \sin \Omega , - e _ { z } \cos \Omega , e _ { y } \cos \Omega - e _ { x } \sin \Omega ) .
$$

Equating the $\acute { \mathbf { \varepsilon } }$ 0r $y -$ components, and using (6.15.1), we find

$$
\varepsilon \sin \omega = { \frac { e _ { z } } { \sin i } } .
$$

Remember that this choice of elements is invalid,anyway, if sin $i = 0 .$ ）

At the start of the calculation the components of $\pmb { \Sigma }$ and $\blacktriangledown$ may have to be changed, using the rotation $P \{ \epsilon \}$ ,from equatorial to ecliptic coordinates. A sequence of calculation is as follows:

1.Find $\hbar _ { z } , \hbar _ { y } , \hbar _ { z }$ from (6.15.3）.   
2.From (6.15.1）， cos $\mathfrak { g } _ { \mathfrak { c } }$ is proportional to $- h _ { y }$ ,and sin $\Omega$ is proportional to $\tilde { h } _ { x }$ So find $\mathfrak { a }$   
3.From (6.15.1), cosi is proportional to $h _ { z }$ and $\sin i$ is proportional to $( \hat { \mu } _ { z } ^ { 2 } + \hat { \mu } _ { y } ^ { 2 } ) ^ { 1 / 2 }$ So find $\dot { z }$   
4.Find ecos $\omega$ and $\boldsymbol { \varepsilon }$ sin $\omega$ from (6.15.4), (6.15.5) and (6.15.6),and then find $\omega$ ：

5.Find $e$ from $e = ( e _ { x } ^ { 2 } + e _ { y } ^ { 2 } + e _ { z } ^ { 2 } ) ^ { \frac { 1 } { 2 } / 2 }$

6. Find a from

$$
a ^ { - \frac { 1 } { 4 } } = \frac { 2 } { r } - \frac { v ^ { 2 } } { \mu } .
$$

7.If $\mathfrak { a } ^ { - \mathfrak { I } }$ is positive, find $\pmb { \mathcal { E } }$ from

$$
\cos { \mathcal { E } } = 1 - { \frac { \hbar } { a } } , \quad e \sin { \mathcal { E } } = { \frac { { \bf r } \cdot { \bf v } } { \sqrt { a \mu } } } ,
$$

and then $\mathcal { T }$ from

$$
\mathcal { T } = \dot { \varepsilon } - \left( \dot { \bar { \varepsilon } } - e \sin \bar { \varepsilon } \right) \sqrt { \frac { a ^ { 3 } } { \mu } } .
$$

(One can, of course, add or subtract from this an integral multiple of the period.）

8. If a-1 is negative, the equations to use are

$$
\begin{array} { l } { Z = \displaystyle \cosh \bigl ( F \bigr ) = \frac { 1 } { e } \biggl ( 1 - \frac { r } { a } \biggr ) , } \\ { F = \ln \Big [ Z + \sqrt { Z ^ { 2 } - 1 } \Big ] \cdot S G N ( \mathbf { r } \cdot \mathbf { v } ) , } \\ { T = t - \bigl ( e \sinh F - F \bigr ) \sqrt { \frac { - a ^ { 3 } } { \mu } } . } \end{array}
$$

9.Ifa-1=0,and the orbit is parabolic; then

$$
\begin{array} { l } { { q = \displaystyle \frac { h ^ { 2 } } { 2 \mu } , ~ \tau = \tan \left( \frac { v } { 2 } \right) = \left( \displaystyle \frac { r } { q } - 1 \right) ^ { 1 / 2 } * S G N ( \mathbf { r } \cdot \mathbf { v } ) , } } \\ { { \mathrm { } } } \\ { { T = t - \displaystyle \left( \frac { 1 } { 3 } \tau ^ { 3 } + \tau \right) \sqrt { \frac { 2 q ^ { 3 } } { \mu } } . } } \end{array}
$$

and

These two programs should be debugged together, with the output of one being the input of the other. Make up your own orbits,and in each case make a sketch showing the orbit projected into the ecliptic, indicating the parts north or south of the ecliptic. Include the orbit of the Earth,and mark in the position of the Earth at the time of perihelion,so that you get some ideas about visibility. Also experiment with orbits of artificial satellites of the Earth.

Orbital elements of some comets and asteroids are listed in Appendices G and H.

# 6.16 The Geocentric Coordinates

We have seen how to find the heliocentric coordinates of a comet resolved in the equatorial reference system. Let the vector from the Earth to the Sun be

$$
{ \mathfrak { R } } = \{ X , Y , Z \} ,
$$

resolved in the same system. These coordinates are tabulated in almanacs for equatorial systems of specific epochs. Then the geocentric vector from the Earth to the comet is

$$
p = r + \pi .
$$

If p = (ε,n,S),resolved in the same system, and if the right ascension and declination (in radians)are $\alpha$ and $\delta$ then

$$
\rho = ( \xi , \eta , \zeta ) = \rho ( \cos \alpha \cos \delta , \sin \alpha \cos \delta , \sin \delta ) .
$$

Q and 8 are easily found,and can then be transposed, if wanted, to appropriate units. In this way,the observed values at any given time t can be computed. A table of such values for regular intervals of the time is called an ephemeris.

X,Y and Z are tabulated,and to find their values for a given time, interpolation will be needed. This is discussed in Section 10.2. If you are making up your own orbits, then it is suffcient to use a reasonable approximation based oshort formulas. The following set of formulas is taken from the Almanac for Computers,1986 Ref. 37. Iam grateful to Dr. L.E.Doggett for bringing it to my attention,and to Dr. P.K. Seidelmann for his permission to use it.

First,we introduce the Julian Date,JD,for specifying the time. This is the time measured from Greenwich Mean Noon on January 1st, 4713 B.C.Julian Datesare tabulated in almanacs; but the following beautiful formula enables the Julian Date to be found from the Gregorian Calendar Date fordates A.D.1900, February 28th,through A.D.2099.Let $\mathbf { Y }$ be the year, so $1 9 0 0 \leq Y \leq 2 9 9 9$ ；let Mbe the month,so $1 \leq M \leq 1 2$ ;let $\mathfrak { D }$ be the day, so $1 \leq D \leq 3 1$ ; let UT be the universal time in hours. Then

$$
\begin{array} { r l r } & { \mathrm { J D } = 3 6 7 * Y - \mathrm { I N T } ( 7 * ( Y + \mathrm { I N T } ( ( M + 9 ) / 1 2 ) ) / 4 ) + \mathrm { I N T } ( 2 7 5 * M / 9 ) } & \\ & { \quad \quad \quad + D + 1 7 2 1 0 1 3 . 5 + \mathrm { U T } / 2 4 . } &  \quad \quad \quad ( 6 . 1 6 \end{array}
$$

Here $\mathrm { I N T } _ { \cdots } ^ { \prime } ( \ldots )$ is the greatest integer function. This formula can be made more general to cover a wider range of dates.

Now let

$$
\mathcal { T } = ( \mathrm { J D } - 2 4 5 1 5 4 5 . 0 ) / 3 6 5 2 5 ,
$$

which is the time in centuries measured from AD 20o0. Next let

$$
M = 3 5 7 ^ { \circ } . 5 2 8 + 3 5 9 9 9 ^ { \circ } . 0 5 0 * T .
$$

Then the true longitude of the Sun is

$$
\begin{array} { r } { \bar { L } = 2 8 \bar { 0 } ^ { \circ } . 4 6 0 + 3 6 0 0 0 ^ { \circ } . 7 7 2 * T + ( 1 ^ { \circ } . 9 1 5 - 0 ^ { \circ } . 0 0 4 8 * T ) * S I N ( M ) } \\ { + 0 ^ { \circ } . 0 2 0 * S I N ( 2 * M ) , \qquad ( 6 } \end{array}
$$

ere appropriate conversion to radians must be made.

The radial distance may be adequately found from

$$
\mathrm { R } = 1 . 0 0 0 1 4 - 0 . 0 1 6 7 5 * \mathrm { C O S } ( \mathrm { M } ) - 0 . 0 0 0 1 4 * \mathrm { C O S } ( 2 * \mathrm { M } ) .
$$

b convert to equatorial coordinates, use

$$
\epsilon = 2 3 ^ { \circ } . 4 3 9 - 0 ^ { \circ } . 0 1 3 * T .
$$

Dver the period considered, the error in $\sum$ does not exceed about one minute farc.

# 17The Effects of Planetary Aberration and Parallax

Let us suppose that the computed right ascension and declination have been corrected for the effects of precession and annual and diurnal aberration.

Neglecting refraction effects in the Earth's atmosphere, there willstill be two factors leading to a diference between the observed and computed values. Since light moves with a finite speed, the position observed corresponds to some time before the instant of observation. This effect is called planetary aberration (it should not be confused with other types of aberration). If t is the time of observation, the observed position will correspond to a time

$$
t - { \frac { \rho } { c } }
$$

where $c$ is the speed of light.

Also the geocentric coordinates of the Sun are measured from the center of the Earth; in order to compute the angles measured by an actual observer, we should use the coordinates of the Sun measured from that observer. So we need the geocentric coordinates of the observer; they will depend on his (or her)position and on the time.Let the geocentric distance of the observer be P1,measured in units of the Earth's equatorial radius,and let the geocentric latitude be $\phi$ Let the local sidereal time (converted to radians) be $\mathfrak { s }$ These forma triplet of spherical polar coordinates,so that the coordinates of the observer are

$$
\begin{array} { r l } & { \Delta X = ( 4 . 2 6 3 5 6 \times 1 0 ^ { - 5 } ) \rho _ { 1 } \cos \phi \cos \theta , } \\ & { \Delta Y = ( 4 . 2 6 3 5 6 \times 1 0 ^ { - 5 } ) \rho _ { 1 } \cos \phi \sin \theta , } \\ & { \Delta Z = ( 4 . 2 6 3 5 6 \times 1 0 ^ { - 5 } ) \rho _ { 1 } \sin \phi . } \end{array}
$$

Then the modified solar coordinates,which should be used in the calculation ofright ascension and declination,are

$$
X _ { 1 } = X - \Delta X , \quad Y _ { 1 } = Y - \Delta Y , \quad Z _ { 1 } = Z - \Delta Z .
$$

The local sidereal time can be found by subtracting the longitude of the observer from the Greenwich sidereal time, the latter is tabulated in almanacs.A formula for Greenwich mean sidereal time is (Ref.37.）

$$
\begin{array} { r } { \mathrm { G M } _ { \mathrm { { \tiny 4 } S T } } ^ { \mathrm { { \tiny 4 } S T } } = 6 ^ { \mathrm { h } } . 6 9 7 3 7 4 5 6 + 2 4 0 0 ^ { \mathrm { i } } . 0 5 1 3 3 6 * \mathrm { T 0 } + 0 ^ { \mathrm { h } } . 0 0 0 0 2 5 8 6 2 2 * \mathrm { T 0 } ^ { 2 } } \\ { + 1 . 0 0 2 7 3 7 9 0 9 * \mathrm { U T } . \qquad ( 6 . } \end{array}
$$

where UT is the universal time of the observation, and

$$
\mathrm { T 0 } = ( \mathrm { 3 D 0 - 2 ~ 4 5 1 ~ 5 4 5 . 0 } ) / 3 6 ~ 5 2 5
$$

and JD0 is the Julian Date at $0 ^ { 3 ^ { 5 } }$ UT for the day of the observation.

Note that fora change of $\ B$ daysand $\mathbb { E }$ hours of mean solar time, the mean sidereal time changes by

$$
2 4 ^ { \mathrm { h } } . 0 6 5 7 0 9 8 2 3 5 * D + 1 . 0 0 2 7 3 7 9 0 9 * H .
$$

# 6.18 Projects

We now have powerful means to investigate and solve a wide variety of problems where Keplerian motion is a good approximation to actuality. In many cases, proper generalization can be made later using mumerical integration and some perturbation analysis. One intention of these projects is to breathe some life into the formulas and programs. The projects are intended to provide ideas,and many have been left deliberately vague, in order to encourage your initiative and imagination. Some projects assume graphics capability, and most are enhanced by the use of graphics: use it when possible; it is a superb learning tool, removing misconceptions,and generating new ideas. Where possible, I recommend that you try to turn a project into a “computer game.” Constantly, try to think of more questions for the computer to answer.

1.With INPUT $\pmb { \mathscr { z } }$ eand $\omega$ plot ellipses, parabolas and appropriate branches of hyperbolas; in particular, get used to the efects of changing e. In the case of hyperbolas, it may help the picture if asymptotes are included, say,as dotted lines.   
2.Let an attracting mass remain at the center of the screen,and consider motion relative to it. The INPUT would consist of initial conditions for the second body.Experiment with these, plotting the orbits.   
3. With the same model, let a “target” be fixed on the right of the screen; theinterceptor will start somewhere on the left,with initial velocity horizontal. Have a competition for the closest interception.   
4. With the same model, have the target moving around the central mass in an ellipse; this makes the timing of the launching of the interceptor important.   
5.With the same model, look at orbits having the same initial position and speed,but with varying initial directions for the velocity.   
6.This is like the preceding model, but now,keep the direction of the initial velocity fixed,and vary the initial speed. (Note: with polar coordinates $\mathfrak { T }$ and $\mathfrak { g }$ the equation of the orbit is $p / \tau = 1 \div e \cos ( v _ { 0 } + \theta )$ where $v _ { 0 }$ is the initial true anomaly. You do not need actually to find $\Im _ { \Im }$ ,but only the values of $e @ \mathfrak { C O S } \mathfrak { U } _ { \mathbb { Z } }$ and esin $\mathfrak { T } _ { \mathbb { Q } }$ ）   
7. Project 5 can be made more interesting if several particles are “fired" simultaneously from the same position,with the same speed, but in different directions. Plot positions after equal intervals of time. Erase the old positions before plotting new ones.   
8.Follow the simultaneous motions of several particles that start at the left ofthe screen at the same time, moving horizontally with the same initial speed.Again,plot positions after equal intervals of time. Notice the way in which the particles are “focused” and then dispersed. As an extra dimension for this project you might give the central body an actual size,   
and stop the orbits of the particles that are accreted

9. Follow the breaking up of a comet. The initial orbit would have position and velocity ro and vo just before to.For the project, the initial conditions at to would be ro and Vo +Svi,for the ith particle,where the velocity increments would be small.

10.Follow the motion of a visual binary system. First, keep the center of mass fixed,and then let the center of mass move across the screen,deriving figures like Figure 6.1. Allow for the fact that the plane of the orbit is unlikely to be perpendicular to the line of sight.

11.Now let the binary bea spectroscopic binary,which is studied through the Doppler shifts resulting from the velocity components in the line of sight; usually, the spectrum of one star only is observed.The radial velocity is plotted as a function of time. Plot some of these curves, varying the eccentricities and orientations of the orbits. Let $\gamma _ { G }$ be theradial velocity of the center of mass of the system.If the velocity curve is a plot of V, the radial velocity, against t, then it is the case that the area above the line $V = V _ { G }$ is equal to that below the line, $\mathbb { V } = \mathbb { V } _ { G }$ ,when just one revolution is considered. Can you justify this? Look up spectroscopic binaries in an astronomy textbook.

12.Set up graphics programs to illustrate the situations of problems 20-24 in section 6.4.

13.A satellite is moving in an orbit around the Earth.Choose elements forthe orbit,and then plot sub-orbital points (i.e.,points at which the satellite is at the zenith）,taking into account the rotation of the Earth.

14.A satellite is moving in an orbit around the Earth,and an observer is ata definite point on the Earth (which can be assumed to be spherical). It is required to find times at which the satellite rises and sets. Neglect atmospheric refraction.(With the origin at the center of the Earth,let vectors to the satellite and observer berand $\mathbf { z } ,$ respectively. You are looking for times at which $( \mathbb { R } - { \mathfrak { r } } )$ is perpendicular to R.Finding the times will require iteration.）

15. Ignoring refraction in the Earth's atmosphere,write a program for finding whether a satellite of the Earth isin direct sunlight,or shadow.Assume the Sun to be a point source of light. (Derive a formula for the distance from the center of the Earth to the line joining the satellite and the Sun; for critical cases,you are looking for times at which this distance is equal to the radius of the Earth.）

16.In a very oversimplified model of an ICBM trajectory a missile leaves a point on the Earth's surface with a given velocity and moves subject onlv to the gravitational field of a spherical Earth until it lands.Let the radius of the Earth be $\mathcal { R }$ and the initial speed be $\bar { \bar { \psi } }$ ；the angle of launch is to be varied.Let this angle be $\dot { \phi }$ ,theangle between the initial velocityand the local horizon.Let the center of the Earth be $o$ thepoint of launch be $P$ and the empty focus $O _ { \frac { 1 } { 2 } }$ First,show,using properties of the ellipse, that the angle $O P O _ { \textrm { i } } = 2 \phi$ For all $\phi \ a$ is the $\mathtt { S a m a n e } _ { \mathtt { Y } }$ and $P \mathcal { O } _ { 1 } = 2 a - \mathcal { R }$ a constant,so $O _ { I }$ lies on $\mathrm { ^ a }$ circle with center $P$ The range is greatest when the angle $P O Q _ { 3 }$ is greatest,or the angle $P 0 _ { \mathrm { i } } O = \pi / 2$ In this instance, show that $\csc ( \angle P O O _ { 1 } ) = ( 2 \mu / R V ^ { 2 } ) - 1$ ， Let the complete angle swept through by the radius vector from launch to landing be $\mathfrak { P }$ $\angle P O O _ { 1 } = \ I _ { 2 } / 2$ Construct a table showing for different 亚，the corresponding $\pmb { \updownarrow }$ and the time of fight.

17.Now investigate the consequences of small errors at launch of the ICBM. Start with an orbit of greater range. One at a time,add small errors of, say, $0 . 1 \%$ in the initial speed, $\pmb { \bar { \gamma } }$ and the launch angle, $\phi$ In each case, find the distance of the point of impact from the intended target. Assuming that the effects of the small initial errors are linear, derive tolerances for errorsat launch,so that errors at landing are within prescribed bounds.

18.Next,identify geographically the launching point and the target,and introduce the rotation of the Earth. Find a suitable trajectory for the ICBM.and look for a minimum launching speed.Repeat the error analysis.

19.Next,we consider some rendezvous problems. Note that the ICBM trajectories can be said to fall into this category. First, consider a “hostile" rendezvous,in which an ICBM with known orbit is to be destroyed.The interceptor is to be fired from a point on the surface of the Earth that can beclose to the target,or distant fromit.Byall means,choose actual geographical locations. Assume that there is a maximum initial speed for launching the interceptor.Find possible orbits for interception.

20.Now consider a “friendly” rendezvous with a satellite;here, assume that “friendly” means that at rendezvous (a) the velocities are parallel or (b) therelative speed isa minimum.

21.Suppose that we want to transfer from a circular orbit of radius $a _ { 1 }$ toa larger circular orbit of radius $a _ { 2 }$ ，these orbits being coplanar.The best known intermediate orbit is an ellipse having pericenter distance $a _ { 1 }$ and apocenter distance $\mathfrak { a } _ { 2 }$ ; this gives the “Hohmann transfer.” Assuming the velocity changes to be instantaneous, the increments at the ends of the transfer orbit are easily found and discussed analytically. It has been argued that if the ratio $a _ { 2 } / a _ { 1 }$ is large, greater than 10,say, then it is more effcient to use two transfer ellipses; the frst has pericenter distance $a _ { \ I }$ and apocenter distance $Q$ and the second has apocenter distance $Q$ and pericenter distance ${ a } _ { 2 }$ Consider this analytically or numerically.

22. Suppose that the circular orbits ofthe preceding project are in different planes, the angle between them being small. Use a Hohmann transfer orbit asa first approximation,and look for transfer ellipses having minimum total velocity changes at the ends. Is there a most efficient place for the transfer orbit to start or finish?

23.Using right ascension and declination as coordinates, plot apparent paths of comets as observed from the Earth. Include the option of adding the orbit of the Sun. This project is greatly enhanced if some of the brighter stars are included in the display. Use data from Appendix G.

24. Project cometary orbits into the ecliptic, and include, optionaly， orbits of the major planets.

25. Generalize ephemeris calculations to include range and range-rate. Include satellite-to-satellite observations.

26. We are not yet prepared to deal with the dynamics when more than two bodies are involved. But in many cases some idea of the motion can be generated by “patching together” parts of Keplerian orbits. Suppose that we have the Sun, with mass M,and a planet, with massm,moving around the Sun in a circular orbit of radius r1.Then (and this is discussed in section 11.18) the planet can be considered as surrounded by an “activity sphere”of radius $r _ { 1 } ( \pi / \tilde { \mathcal { M } } ) ^ { 2 / 5 }$ . Now introduce a third body, a comet, say, with negligible mass. Assume that outside the activity sphere, this mass moves in a Keplerian orbit around the Sun,but inside the activity sphere it moves in a Keplerian orbit around the planet.Writea program for calculating orbits in this model. Iteration will be needed to find when the comet enters the activity sphere. For a start,anyway, restrict calculations to two dimensions. Look for cases where an encounter with the planet results in a significant change in the orbital energy of the comet. Interpreting the planet as Jupiter, look for situations in which a parabolic comet is “captured” by Jupiter (turned into a periodic comet with aphelion distance close to the radius of Jupiter's orbit) or expelled from the solar system. Also investigate how a spacecraft launched from the Earth, with aphelion distance r1, can receive a boost in energy in order to reach, say,Saturn.

27.It has been suggested that the “star of Bethlehem” was Halley's comet, and that the Birth took place during the summer at about the time of the comet's appearance. Using the following elements (Ref. 71),discuss the hypothesis on the basis of geometrical reasoning. T= -11, Oct. 10.849, q = 0.58720,e = 0.96737,w = 92°.544,Ω = 35°.191,i = 163°.584. (Note: $T$ is given according to the Julian calendar.)
