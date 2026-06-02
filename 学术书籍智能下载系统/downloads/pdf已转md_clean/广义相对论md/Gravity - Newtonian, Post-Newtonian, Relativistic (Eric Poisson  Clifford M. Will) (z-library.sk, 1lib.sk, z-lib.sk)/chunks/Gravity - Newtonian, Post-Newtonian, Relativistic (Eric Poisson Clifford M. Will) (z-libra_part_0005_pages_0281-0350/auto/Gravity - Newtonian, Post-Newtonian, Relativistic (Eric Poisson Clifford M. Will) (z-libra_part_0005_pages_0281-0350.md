With this assignment the equation for $\Phi$ integrates to $\begin{array} { r } { \Phi = - \frac { 1 } { 2 } c ^ { 2 } \ln [ 1 - 2 G M / ( c ^ { 2 } r ) ] + } \end{array}$ $h ( t )$ , in which $h ( t )$ is an arbitrary function of integration. The boundary conditions of Eq. (5.157) require that $h ( t ) = 0$ , and we arrive at

$$
e ^ { - 2 \Phi / c ^ { 2 } } = 1 - { \frac { 2 G M } { c ^ { 2 } r } } .
$$

The resulting metric,

$$
d s ^ { 2 } = - \left( 1 - { \frac { R } { r } } \right) d ( c t ) ^ { 2 } + \left( 1 - { \frac { R } { r } } \right) ^ { - 1 } d r ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) ,
$$

with

$$
R : = { \frac { 2 G M } { c ^ { 2 } } } ,
$$

is Schwarzschild’s external metric, expressed in terms of the body’s Schwarzschild radius $R$ . So we discover, after a very short calculation, that a spherically-symmetric solution to Einstein’s equations in vacuum is necessarily static, and given by the Schwarzschild metric; this statement is known as Birkhoff’s theorem.

<table><tr><td>Box 5.8</td><td>Birkhoff&#x27;s theorem in Newtonian gravity</td></tr><tr><td></td><td>There is an analogous statement of Birkhoffs theorem in Newtonian theory.For spherical symmetryand in vacuum, Laplace&#x27;s equation for the Newtonian potential is 1d (x2aU(t,r)) = 0.</td></tr><tr><td></td><td>r2 dr dr This can be easily integrated to give U(t,r) = GM/r + h(t), where GM is an integration constant,</td></tr><tr><td></td><td> and h(t) an arbitrary function of time. But since all physical manifestations of the potential depend on</td></tr></table>

As we have emphasized elsewhere, coordinates are merely labels of spacetime events; they have no physical significance whatever, and any coordinate system can be used to describe the geometry of spacetime, with equivalent physical results. Nevertheless, the choice of coordinates can have a significant impact on the ease of calculations. We remarked earlier that the Coulomb gauge of linearized theory is useful for illuminating certain aspects of the theory, but not for calculations that go beyond linearized theory (as will be seen abundantly in later portions of this book); for this the Lorenz gauge is far more useful.

Here too, our choice of coordinates was arbitrary – in this instance they are known as the Schwarzschild coordinates. Their main advantage is that they provide the simplest route to a solution of Einstein’s equations and the simplest expression for the metric. One disadvantage is that a transformation from the polar coordinates $( r , \theta , \phi )$ to quasi-Cartesian coordinates $( x , y , z )$ produces a complicated metric with many off-diagonal terms.

Another disadvantage, which is shared by the isotropic and harmonic coordinates introduced below, is that the Schwarzschild coordinates are badly behaved at $r = R$ . This, in the pure vacuum case – vacuum everywhere – marks the boundary of the black hole, known as the event horizon. Because we are not concerned here with the black-hole aspects of the spacetime, and because this infamous coordinate difficulty is resolved in all textbooks on general relativity, we shall have very little to say on this issue.

To illustrate further the arbitrariness of coordinates, we express the Schwarzschild metric in a number of alternative coordinate systems, each with its own advantages and disadvantages.

# Isotropic coordinates

The transformation

$$
r = r _ { \mathrm { i s o } } \bigg ( 1 + \frac { R } { 4 r _ { \mathrm { i s o } } } \bigg ) ^ { 2 }
$$

brings the Schwarzschild metric to the new form

$$
d s ^ { 2 } = - \bigg ( \frac { 1 - R / 4 r _ { \mathrm { i s o } } } { 1 + R / 4 r _ { \mathrm { i s o } } } \bigg ) ^ { 2 } d ( c t ) ^ { 2 } + \bigg ( 1 + \frac { R } { 4 r _ { \mathrm { i s o } } } \bigg ) ^ { 4 } \bigg [ d r _ { \mathrm { i s o } } ^ { 2 } + r _ { \mathrm { i s o } } ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) \bigg ] ,
$$

in which the spatial metric is proportional to the flat-space expression $d r _ { \mathrm { i s o } } ^ { 2 } + r _ { \mathrm { i s o } } ^ { 2 } ( d \theta ^ { 2 } +$ $\sin ^ { 2 } \theta d \phi ^ { 2 } )$ . The coordinates $t , \theta$ , and $\phi$ are unchanged, and therefore they carry the same meaning as they do in Schwarzschild coordinates. The new radial coordinate $r _ { \mathrm { i s o } }$ , however, does not possess a recognizable geometrical meaning: it does not measure the proper circumference of great circles, and it does not measure proper radial distance. A curious property of the isotropic coordinates is that the metric keeps its form under the inversion $r _ { \mathrm { i s o } }  R ^ { 2 } / ( 4 r _ { \mathrm { i s o } } )$ ; this isometry is largely unphysical, but it has played a very useful role in the construction of initial-data sets for the numerical simulation of black-hole mergers.

The main advantage of this coordinate system is that the additional transformation $x = r _ { \mathrm { i s o } } \sin \theta \cos \phi$ , $y = r _ { \mathrm { i s o } } \sin \theta \sin \phi$ , $z = r _ { \mathrm { i s o } } \cos \theta$ produces a simple expression for the metric in Cartesian-like coordinates, with the components

$$
\begin{array} { l } { { g _ { 0 0 } = - \bigg ( \displaystyle \frac { 1 - R / 4 r _ { \mathrm { i s o } } } { 1 + R / 4 r _ { \mathrm { i s o } } } \bigg ) ^ { 2 } , } } \\ { { g _ { j k } = \delta _ { j k } \bigg ( 1 + \displaystyle \frac { R } { 4 r _ { \mathrm { i s o } } } \bigg ) ^ { 4 } . } } \end{array}
$$

When $r _ { \mathrm { i s o } }$ is large compared with the Schwarzschild radius $R$ , these expressions become

$$
\begin{array} { l } { { \displaystyle g _ { 0 0 } = - 1 + R / r _ { \mathrm { i s o } } - \frac { 1 } { 2 } ( R / r _ { \mathrm { i s o } } ) ^ { 2 } + \cdots ~ , } } \\ { { \displaystyle g _ { j k } = \delta _ { j k } \bigg ( 1 + R / r _ { \mathrm { i s o } } + \frac { 3 } { 8 } ( R / r _ { \mathrm { i s o } } ) ^ { 2 } + \cdots \bigg ) , } } \end{array}
$$

and they can be compared with the Newtonian metric of Eq. (5.154). In spherical symmetry, and in a vacuum exterior, the Newtonian potential is $U = G M / r _ { \mathrm { i s o } }$ , so that $2 U / c ^ { 2 } =$ $R / r _ { \mathrm { i s o } }$ . The Newtonian metric has $g _ { 0 0 } = - 1 + 2 U / c ^ { 2 } = - 1 + R / r _ { \mathrm { i s o } }$ and $g _ { j k } = \delta _ { j k } ( 1 +$ $2 U / c ^ { 2 } ) = \delta _ { j k } ( 1 + R / r _ { \mathrm { { i s o } } } )$ . We see that the Schwarzschild metric, when it is expressed in isotropic coordinates, differs from this by terms of order $( R / r _ { \mathrm { i s o } } ) ^ { 2 }$ and higher; these corrections cannot be obtained in the linearized approximation that led to the Newtonian metric. The fact that the Schwarzschild metric with $R = 2 G M / c ^ { 2 }$ reduces to the Newtonian metric when $r _ { \mathrm { i s o } }$ is large confirms the identification of $M$ with the body’s total mass.

Like the Schwarzschild coordinates, the isotropic coordinates become ill-behaved at the black-hole horizon, which is now situated at $\begin{array} { r } { r _ { \mathrm { i s o } } = \frac { 1 } { 4 } R } \end{array}$ .

# Harmonic coordinates

Another popular coordinate system for the Schwarzschild spacetime is obtained by the transformation

$$
\begin{array} { r } { r = r _ { \mathrm { h } } + \frac { 1 } { 2 } R . } \end{array}
$$

For reasons that will be identified below, the new system is called harmonic, and in it the metric takes the form

$$
d s ^ { 2 } = - \left( { \frac { 1 - R / 2 r _ { \mathrm { h } } } { 1 + R / 2 r _ { \mathrm { h } } } } \right) d ( c t ) ^ { 2 } + \left( { \frac { 1 + R / 2 r _ { \mathrm { h } } } { 1 - R / 2 r _ { \mathrm { h } } } } \right) d r _ { \mathrm { h } } ^ { 2 } + ( r _ { \mathrm { h } } + { \scriptstyle { \frac { 1 } { 2 } } } R ) ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) .
$$

As before we find that $t , \theta$ , and $\phi$ carry the same geometrical meaning, but that $r _ { \mathrm { h } }$ is linked neither to a proper circumference nor to a proper radial displacement. And the harmonic coordinates also are ill-behaved at the event horizon, which is now situated at $\begin{array} { r } { r _ { \mathrm { h } } = \frac { 1 } { 2 } R } \end{array}$ .

The additional transformation $x = r _ { \mathrm { h } } \sin \theta \cos \phi$ , $y = r _ { \mathrm { h } } \sin \theta \sin \phi$ , $z = r _ { \mathrm { h } } \cos \theta$ produces a complicated metric, but we find it worthwhile to display it here:

$$
\begin{array} { l } { { g _ { 0 0 } = - \displaystyle \frac { 1 - R / 2 r _ { \mathrm { h } } } { 1 + R / 2 r _ { \mathrm { h } } } , } } \\ { { g _ { j k } = \bigg ( \displaystyle \frac { 1 + R / 2 r _ { \mathrm { h } } } { 1 - R / 2 r _ { \mathrm { h } } } \bigg ) n _ { j } n _ { k } + \big ( 1 + R / 2 r _ { \mathrm { h } } \big ) ^ { 2 } \big ( \delta _ { j k } - n _ { j } n _ { k } \big ) , } } \end{array}
$$

where $n ^ { j } : = x ^ { j } / r _ { \mathrm { h } }$ is a radial unit vector, whose index is lowered with the Euclidean metric $\delta _ { j k }$ , so that $n _ { j } : = \delta _ { j k } n ^ { k }$ . We note that in this Euclidean sense, the two terms in the spatial metric are orthogonal to each other, because $( \delta _ { j k } - n _ { j } n _ { k } ) n ^ { k } = 0$ . This observation simplifies the computation of the inverse metric, which is given by

$$
\begin{array} { l } { { g ^ { 0 0 } = - \displaystyle \frac { 1 + R / 2 r _ { \mathrm { h } } } { 1 - R / 2 r _ { \mathrm { h } } } , } } \\ { { g ^ { j k } = \bigg ( \displaystyle \frac { 1 - R / 2 r _ { \mathrm { h } } } { 1 + R / 2 r _ { \mathrm { h } } } \bigg ) n ^ { j } n ^ { k } + \big ( 1 + R / 2 r _ { \mathrm { h } } \big ) ^ { - 2 } \big ( \delta ^ { j k } - n ^ { j } n ^ { k } \big ) . } } \end{array}
$$

For future reference we also record the expression

$$
\sqrt { - g } = \left( 1 + R / 2 r _ { \mathrm { h } } \right) ^ { 2 }
$$

for the metric determinant.

When $r _ { \mathrm { h } }$ is large compared with $R$ the metric becomes

$$
\begin{array} { l } { { g _ { 0 0 } = - 1 + R / r _ { \mathrm { h } } - \displaystyle \frac { 1 } { 2 } ( R / r _ { \mathrm { h } } ) ^ { 2 } + \cdots \cdot } } \\ { { \displaystyle g _ { j k } = \big ( 1 + R / r _ { \mathrm { h } } \big ) \delta _ { j k } + \frac { 1 } { 4 } ( R / r _ { \mathrm { h } } ) ^ { 2 } \big ( \delta _ { j k } + n _ { j } n _ { k } \big ) + \cdots } } \end{array}
$$

Here also we find that this agrees with the Newtonian metric of Eq. (5.154) to order $R / r _ { \mathrm { h } }$ with deviations occurring at order $( R / r _ { \mathrm { h } } ) ^ { 2 }$ and higher.

To explain the meaning of the phrase “harmonic coordinates” we examine the set of four scalar fields $\begin{array} { r } { X ^ { ( 0 ) } : = c t , X ^ { ( 1 ) } : = ( r - \frac { 1 } { 2 } R ) \sin \theta \cos \phi , X ^ { ( 2 ) } : = ( r - \frac { 1 } { 2 } R ) \sin \theta \sin \phi } \end{array}$ , and $X ^ { ( 3 ) } : = ( r - { \textstyle \frac { 1 } { 2 } } R ) \cos \theta$ in the Schwarzschild spacetime. We collectively denote the members of the set by $X ^ { ( \mu ) }$ , and observe that while we have defined the scalar fields in terms of the original Schwarzschild coordinates $( t , r , \theta , \phi )$ , we have the simpler expressions $X ^ { ( \mu ) } = x ^ { \mu }$ in the Cartesian version $( t , x , y , z )$ of the harmonic coordinates.

It is a matter of simple computation to show that each one of the four scalar fields satisfies the wave equation

$$
\begin{array} { r } { \boxed { \vphantom { \bigg | } } _ { g } X ^ { ( \mu ) } = 0 } \end{array}
$$

in Schwarzschild spacetime. Here $\begin{array} { r } { \Pi _ { g } : = g ^ { \alpha \beta } \nabla _ { \alpha } \nabla _ { \beta } } \end{array}$ is the curved-spacetime wave operator, and we note the important fact that Eq. (5.175) is covariant and can therefore be expressed in any coordinate system; the equation is easiest to verify if we adopt the Schwarzschild coordinates $( t , r , \theta , \phi )$ . The term “harmonic” refers to solutions to Eq. (5.175), which is a generalization from three-dimensional Euclidean space to four-dimensional curved spacetime of Laplace’s equation $\nabla ^ { 2 } X = 0$ ; it has been a long tradition that solutions to Laplace’s equation are called harmonic functions.

We can re-express Eq. (5.175) as $\nabla _ { \alpha } X ^ { ( \mu ) \alpha } = 0$ , where the vector fields $X ^ { ( \mu ) \alpha }$ are defined by $X _ { \alpha } ^ { ( \mu ) } = \nabla _ { \alpha } \bar { X ^ { ( \mu ) } }$ . With the divergence identity of Eq. (5.40), this is

$$
\frac { 1 } { \sqrt { - g } } \partial _ { \alpha } \Big ( \sqrt { - g } g ^ { \alpha \beta } \partial _ { \beta } X ^ { ( \mu ) } \Big ) = 0 ,
$$

and the wave equation continues to be covariant. We now, however, specialize the coordinate system to $( t , x , y , z )$ , the Cartesian version of our harmonic coordinates. We have already noted that $X ^ { ( \mu ) } = x ^ { \mu }$ in this coordinate system, and it follows that $\partial _ { \beta } X ^ { ( \mu ) } = \delta _ { \beta } ^ { \mu }$ . Making the substitution reveals that the harmonic condition becomes

$$
\partial _ { \beta } \big ( \sqrt { - g } g ^ { \alpha \beta } \big ) = 0
$$

when it is expressed in the harmonic coordinates $( t , x , y , z )$ . An alternative statement of this is

$$
g ^ { \mu \nu } \Gamma _ { \mu \nu } ^ { \alpha } = 0 .
$$

It can be verified that these equations are indeed satisfied by the Cartesian-like metric of Eqs. (5.171); the computation relies on the results displayed in Eqs. (5.172) and (5.173). But they are not satisfied by the metric of Eqs. (5.170) expressed in spherical polar coordinates. Despite our use of covariant language in our discussion of Eq. (5.175), we are making a very specific coordinate choice in Eqs. (5.177) and (5.178), which are clearly not covariant equations. Another way of looking at this is to recognize that Eqs. (5.175) are four constraints on the coordinates $x ^ { \mu } \equiv X ^ { ( \mu ) }$ .

Harmonic coordinates play a powerful role in our development of weak-field gravity in subsequent chapters, and our digression here serves mostly as a motivation for the coordinate conditions of Eq. (5.177). These, naturally enough, are known as the harmonic coordinate conditions.

# Painleve–Gullstrand coordinates ´

The problems of the preceding coordinate systems at the event horizon can be traced to the bad behavior of the time coordinate $t$ , which becomes frozen at the event horizon. As we shall see in a moment, the coordinate time required for an observer to cross the horizon is always infinite, in spite of the fact that the required proper time $\tau$ is perfectly finite. To explore the features of the Schwarzschild spacetime near the horizon, it is necessary to define a new time coordinate $T$ that is smoothly related to proper time as measured by an observer falling into the black hole.

A simple candidate for such a new time coordinate (though not the only one) is the one defined by

$$
d ( c T ) : = d ( c t ) + ( 1 - R / r ) ^ { - 1 } \sqrt { R / r } d r ;
$$

the motivation behind this choice will be revealed shortly. Integration yields

$$
c T = c t + 2 R \bigg ( \sqrt { r / R } + \frac { 1 } { 2 } \ln { \frac { \sqrt { r / R } - 1 } { \sqrt { r / R } + 1 } } \bigg ) ,
$$

and admitting for the moment that $T$ is well-behaved across $r = R$ , we see that $t$ must diverge logarithmically as the horizon is approached. It is this behavior that signals the pathology of the Schwarzschild time coordinate.

Making the substitution of Eq. (5.179) into Eq. (5.163) brings the metric to the new form

$$
d s ^ { 2 } = - d ( c T ) ^ { 2 } + \left[ d r + \sqrt { R / r } d ( c T ) \right] ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) ,
$$

and the coordinates $( T , r , \theta , \phi )$ are known as the Painleve–Gullstrand coordinates´ . The meaning of the time coordinate must still be elucidated, but the spatial coordinates $( r , \theta , \phi )$ are the same as in the original system of Schwarzschild coordinates. The new coordinates possess the intriguing property that the three-dimensional surfaces $T =$ constant are intrinsically flat. This statement follows by inserting $d T = 0$ into Eq. (5.181) and observing that the spacetime interval becomes $d s ^ { 2 } = d r ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } )$ ; this is the flat-space metric expressed in spherical polar coordinates.

To identify the meaning of the Painleve–Gullstrand time ´ $T$ we consider an observer – let’s call her Meirong – moving radially in the Schwarzschild spacetime with constant angular coordinates $( \theta , \phi )$ ; for such an observer the spacetime interval reduces to $d s ^ { 2 } = { }$ $- d ( c T ) ^ { 2 } + [ d r + \sqrt { R / r } d ( c T ) ] ^ { 2 }$ . If, in addition, Meirong moves on a world line described by the differential equation

$$
\frac { d r } { d T } = - c \sqrt { R / r } ,
$$

then the spacetime interval simplifies further to $d s ^ { 2 } = - d ( c T ) ^ { 2 }$ . This shows that $T$ i s proper time for our observer, and Eq. (5.182) informs us that Meirong falls radially toward the black hole, having started from rest at $r = \infty$ . Integration of Eq. (5.182) is immediate, and we find that

$$
T = T _ { 0 } - \frac { 2 R } { 3 c } ( r / R ) ^ { 3 / 2 } ,
$$

where the constant of integration $T _ { 0 }$ is the time at which Meirong reaches the black-hole singularity at $r = 0$ ; this expression confirms our expectation that $T ( r )$ is perfectly well

behaved at $r = R$ . Finally, it is not hard to show that Meirong’s world line, described by Eq. (5.183), is a timelike geodesic of the Schwarzschild spacetime; our observer is therefore falling freely toward the black hole.

# 5.6.3 Motion of a test mass

We examine the motion of a test mass in the equatorial plane $\begin{array} { r } { ( \theta = \frac { \pi } { 2 } ) } \end{array}$ ) of the Schwarzschild spacetime. The particle is moving freely on a timelike geodesic of the spacetime, and our restriction to equatorial motion does not represent a loss of generality: It can be shown that in a spherically-symmetric spacetime, geodesic motion always proceeds within a fixed spatial plane, and this plane can always be chosen to be equatorial. For concreteness we assume that the particle follows a bounded trajectory, and moves between an innermost radius $r _ { - }$ (the pericenter) and an outermost radius $r _ { + }$ (the apocenter); this does represent a loss of generality, because unbounded motion is also possible.

We begin with the form of the geodesic equation given by Eq. (5.53). This equation reveals that when the metric does not depend explicitly on one of its coordinates $x ^ { \mu }$ , the associated component $u _ { \mu }$ of the velocity vector is a constant of the motion. Here we have two conserved quantities, $u _ { 0 }$ and $u _ { \phi }$ , and we express them as

$$
u _ { 0 } = : - c \sqrt { 1 + 2 \varepsilon / c ^ { 2 } } , \qquad u _ { \phi } = : h ,
$$

thereby defining the constants $\varepsilon$ and $h$ . Raising the index on the velocity vector gives us two equations of motion,

$$
\dot { t } = \frac { \sqrt { 1 + 2 \varepsilon / c ^ { 2 } } } { 1 - R / r }
$$

and

$$
\dot { \phi } = \frac { h } { r ^ { 2 } } .
$$

We use an overdot to indicate differentiation with respect to proper time $\tau$ . Equation (5.186) informs us that $h$ has the interpretation of a conserved angular momentum per unit mass; $\varepsilon$ will presently be identified as a conserved orbital energy per unit mass.

The equation of motion for $r ( \tau )$ can be obtained from the normalization condition $g _ { \alpha \beta } u ^ { \alpha } u ^ { \beta } = - c ^ { 2 }$ for the velocity vector. A short calculation yields

$$
{ \frac { 1 } { 2 } } { \dot { r } } ^ { 2 } + \nu ( r ) = \varepsilon ,
$$

where

$$
\nu ( r ) = - { \frac { G M } { r } } + { \frac { h ^ { 2 } } { 2 r ^ { 2 } } } { \left( 1 - { \frac { R } { r } } \right) }
$$

is an effective potential for the radial component of the motion. Equation (5.187) takes the form of an energy equation, and it is this equation that reveals $\varepsilon$ as an orbital energy per unit mass. A graph of $\nu ( r )$ can be used to display the regions where motion is possible, given values for $h$ and $\varepsilon$ , and the energy diagram goes a long way toward a qualitative understanding of the possible motions (see Fig. 5.4). It is remarkable that Eqs. (5.186) and (5.187) are so very similar to the Newtonian equations of motion in a central potential $U =$ $G M / r$ . There are two major points of departure: the overdot in the differential equations refers to proper time $\tau$ instead of coordinate time $t$ , and the effective potential $\nu ( r )$ contains a relativistic correction $- R / r$ in the centrifugal term. These differences are negligible when $r \gg R$ , but they are very important when $r$ is comparable to $R$ ; in particular, it is noteworthy that the centrifugal barrier is no longer infinite in the relativistic description, but instead goes to zero as $r  R$ .

![](images/201f01b793778d1558d5e46b3d74f274ed6d39dda160dfe277fb3ec2cc5e61c9.jpg)  
Effective potential $\nu ( r )$ for radial motion in the Schwarzschild spacetime, in units of GM/ R. The angular-momentum parameter $h$ is chosen to be larger than ${ \sqrt { 6 G M R } } ,$ and set to such a value that a circular orbit occurs at $r = 6 R .$ The horizontal line is a curve of constant $\varepsilon$ , and in this case the motion takes place between two turning points at $r _ { - } = 3 . 8 R$ and $r _ { + } = 1 1 . 4 R .$ The inset displays an orbit with parameters $p = 5 . 7 R$ and $e = 0 . 5$ .

As stated previously, we examine the bound motion of a particle between the turning points $r _ { \pm }$ ; this situation requires that $h > { \sqrt { 6 G M R } }$ . It is useful to introduce the orbital elements $p$ and $e$ , which are defined by

$$
r _ { - } = : \frac { p } { 1 + e } , \qquad r _ { + } = : \frac { p } { 1 - e } .
$$

These are reminiscent of the definitions in Newtonian celestial mechanics; here $p$ is a relativistic semi-latus rectum, while $e$ is a relativistic eccentricity. The orbit is circular when $e = 0$ .

The orbital elements are related to the constants of the motion $h$ and $\varepsilon$ , and the relationship can be worked out by factorizing $\varepsilon - \nu ( r )$ as

$$
k \bigg ( \frac { 1 } { r } - \frac { 1 } { r _ { 0 } } \bigg ) \bigg ( \frac { 1 } { r } - \frac { 1 } { r _ { - } } \bigg ) \bigg ( \frac { 1 } { r } - \frac { 1 } { r _ { + } } \bigg ) ,
$$

where $k$ is a constant and $r _ { 0 }$ is a third root of the equation $\varepsilon - \nu ( r ) = 0$ . Comparing this form with Eq. (5.188) reveals the following relations: $\begin{array} { r } { k = \frac { 1 } { 2 } h ^ { 2 } R } \end{array}$ , $r _ { 0 } = R / ( 1 - 2 R / p )$ ,

and

$$
\begin{array} { l } { { \displaystyle h ^ { 2 } = \frac { G M p } { 1 - \frac { 1 } { 2 } ( 3 + e ^ { 2 } ) R / p } , } } \\ { { \displaystyle \varepsilon = - \frac { G M } { 2 p } ( 1 - e ^ { 2 } ) \frac { 1 - 2 R / p } { 1 - \frac { 1 } { 2 } ( 3 + e ^ { 2 } ) R / p } . } } \end{array}
$$

In the limit $R / p \to 0$ , that is, when $p$ is much larger than the Schwarzschild radius $R$ , Eqs. (5.190a) and (5.190b) reduce to the Newtonian expressions for the orbital angular momentum and energy, respectively. To ensure that $r _ { 0 } < r _ { - }$ we demand that $p > ( 3 + e ) R$ .

As the particle moves around the mass $M$ , its radial coordinate proceeds from $r =$ $r _ { - } = p / ( 1 + e )$ to $r = r _ { + } = p / ( 1 - e )$ and back again. This radial motion is conveniently described by the parametric equation

$$
r ( \chi ) = \frac { p } { 1 + e \cos \chi } ,
$$

where $\chi$ is an orbital parameter that runs from 0 to $2 \pi$ during a complete radial cycle. The particle is at pericenter $p / ( 1 + e )$ when $\chi = 0$ , at apocenter $p / ( 1 - e )$ when $\chi = \pi$ , and back at pericenter when $\chi = 2 \pi$ . Equation (5.191) is very similar to the description of elliptical motion in Newtonian gravity, $r = p / ( 1 + e \cos \phi )$ , but it actually serves as a definition for $\chi$ , which is not equal to the azimuthal angle $\phi$ .

When Eqs. (5.190a), (5.190b), and (5.191) are inserted into Eq. (5.188), we obtain

$$
\varepsilon - \nu ( r ) = \frac { G M } { 2 p } e ^ { 2 } \sin ^ { 2 } \chi \frac { 1 - ( 3 + e \cos \chi ) R / p } { 1 - \frac { 1 } { 2 } ( 3 + e ^ { 2 } ) R / p } ,
$$

and Eq. (5.187) can be turned into an equation of motion for $\chi$ . The end result is an expression for $\dot { \chi }$ , whose reciprocal is

$$
\frac { d \tau } { d \chi } = \sqrt { \frac { p ^ { 3 } } { G M } } ( 1 + e \cos \chi ) ^ { - 2 } \frac { [ 1 - \frac { 1 } { 2 } ( 3 + e ^ { 2 } ) R / p ] ^ { 1 / 2 } } { [ 1 - ( 3 + e \cos \chi ) R / p ] ^ { 1 / 2 } } .
$$

This equation can be integrated to get proper time $\tau$ as a function of the orbital parameter $\chi$ . The azimuthal angle is obtained by integrating $d \phi / d \chi = \dot { \phi } ( d \tau / d \chi )$ ; combining Eqs. (5.186), (5.190a), and (5.191) gives

$$
\frac { d \phi } { d \chi } = \frac { 1 } { \sqrt { 1 - ( 3 + e \cos \chi ) R / p } } .
$$

This equation shows that $\phi$ becomes equal to $\chi$ in the Newtonian limit $R / p \to 0$ . Finally, similar manipulations produce

$$
\frac { d t } { d \chi } = \sqrt { \frac { p ^ { 3 } } { G M } } ( 1 + e \cos \chi ) ^ { - 2 } \frac { [ 1 - ( 1 + e ) R / p ] ^ { 1 / 2 } [ 1 - ( 1 - e ) R / p ] ^ { 1 / 2 } } { [ 1 - ( 3 + e \cos \chi ) R / p ] ^ { 1 / 2 } [ 1 - ( 1 + e \cos \chi ) R / p ] } ,
$$

an equation that can be integrated to obtain $t ( \chi )$ .

Equations (5.193), (5.194), and (5.195), along with Eq. (5.191), form a complete set of orbital equations for the bounded motion of a test mass in the Schwarzschild spacetime.

Except for Eq. (5.194), which can be solved in terms of an elliptic function, the equations must be integrated numerically, and the formulation developed here is especially convenient for this purpose. The equations make the reduction to the Newtonian limit very easy to accomplish, and corrections of order $R / p , ( R / p ) ^ { 2 }$ , and so on can be systematically worked out.

The orbital equations become especially simple when $e = 0$ and the orbit is circular. Then $r ( \chi ) = p$ and we find that the equations integrate to

$$
\begin{array} { l } { \displaystyle \phi = \frac { 1 } { \sqrt { 1 - 3 R / p } } \chi , } \\ { \displaystyle t = \sqrt { \frac { p ^ { 3 } } { G M } } \frac { 1 } { \sqrt { 1 - 3 R / p } } \chi , } \\ { \displaystyle \tau = \sqrt { \frac { p ^ { 3 } } { G M } } \frac { \sqrt { 1 - 3 R / 2 p } } { \sqrt { 1 - 3 R / p } } \chi . } \end{array}
$$

These equations imply the simple relation $\phi = \Omega t$ , where $\Omega : = \sqrt { G M / p ^ { 3 } }$ is the orbital angular velocity as measured by an observer at rest at infinity; the proper angular velocity differs from this by a factor of $( 1 - 3 R / 2 p ) ^ { - 1 / 2 }$ . In this circular case $\chi$ loses its usefulness as an orbital parameter, and it is appropriate to replace it by $\phi$ .

Returning to the general case $e \neq 0$ , we observe that in the course of a complete radial cycle, the orbital parameter $\chi$ increases by $2 \pi$ , the azimuthal angle increases by $\Delta \phi$ , the time coordinate increases by the orbital period $P$ , and the particle’s proper time increases by the proper period $\mathcal { P }$ . These quantities are defined by

$$
\Delta \phi = \int _ { 0 } ^ { 2 \pi } \frac { d \phi } { d \chi } d \chi , \qquad P = \int _ { 0 } ^ { 2 \pi } \frac { d t } { d \chi } d \chi , \qquad \mathcal { P } = \int _ { 0 } ^ { 2 \pi } \frac { d \tau } { d \chi } d \chi .
$$

The integrals can be evaluated numerically for each pair of orbital elements $p$ and $e$ , and analytical expressions can be obtained when $R / p$ is small. We find

$$
\begin{array} { r l } & { \chi \phi = 2 \pi + 6 \pi \left( \frac { G M } { C ^ { 2 } p } \right) + \frac { 3 \pi } { 2 } ( 1 8 + e ^ { 2 } ) \left( \frac { G M } { c ^ { 2 } p } \right) ^ { 2 } + \cdots , } \\ & { \quad p = 2 \pi \sqrt { \frac { \alpha ^ { 3 } } { G M } } \Bigg [ 1 + 3 ( 1 - e ^ { 2 } ) \bigg ( \frac { G M } { c ^ { 2 } p } \bigg ) } \\ & { \qquad + \frac { 3 } { 2 } ( 1 - e ^ { 2 } ) \big ( 4 + 5 \sqrt { 1 - e ^ { 2 } } \big ) \bigg ( \frac { G M } { c ^ { 2 } p } \bigg ) ^ { 2 } + \cdots \Bigg ] , } \\ & { \quad p = 2 \pi \sqrt { \frac { \alpha ^ { 3 } } { G M } } \Bigg [ 1 + \frac { 3 } { 2 } ( 1 - e ^ { 2 } ) \bigg ( \frac { G M } { c ^ { 2 } p } \bigg ) } \\ & { \qquad + \frac { 3 } { 8 } ( 1 - e ^ { 2 } ) \big ( 1 7 - e ^ { 2 } + 4 \sqrt { 1 - e ^ { 2 } } \big ) \bigg ( \frac { G M } { c ^ { 2 } p } \bigg ) ^ { 2 } + \cdots \Bigg ] , } \end{array}
$$

where $a : = p / ( 1 - e ^ { 2 } )$ is the relativistic semi-major axis. To arrive at Eqs. (5.199) and (5.200) it is helpful to change the variable of integration from $\chi$ to $u$ , defined by

$$
\tan { \frac { \chi } { 2 } } = { \sqrt { \frac { 1 + e } { 1 - e } } } \tan { \frac { u } { 2 } } ;
$$

in Newtonian celestial mechanics $u$ is known as the eccentric anomaly, refer to Eq. (3.32), and its range during a complete radial cycle is also from $u = 0$ to $u = 2 \pi$ .

The fact that $\Delta \phi > 2 \pi$ implies that the orbit is not closed; for small values of $R / p$ the orbit is approximately elliptical, but its major axis rotates by an angle $\Delta \phi - 2 \pi$ in the course of each orbit. This is the pericenter advance of relativistic motion, an effect that was famously measured for Mercury and a number of binary pulsars. To first order in $R / p$ we have that the advance is equal to $6 \pi ( G M / c ^ { 2 } p )$ per orbit. For Mercury this amounts to a tiny, but measurable 42.98 seconds of arc per century (refer to Table 3.1). For binary pulsars the effect is measured in degrees per year.

It is important to note that Eqs. (5.198), (5.199), and (5.200) do not apply when $e = 0$ , because as we have seen, $\chi$ loses its meaning as orbital parameter in the circular case. The limit $e \to 0$ is therefore singular, and in this case we have the exact results

$$
\Delta \phi = 2 \pi , \qquad P = 2 \pi \sqrt { \frac { p ^ { 3 } } { G M } } , \qquad \mathcal { P } = 2 \pi \sqrt { \frac { p ^ { 3 } } { G M } } \sqrt { 1 - \frac { 3 R } { 2 p } } .
$$

Equations (5.198), (5.199), and (5.200) are instances of post-Newtonian expansions, in which a quantity of interest is expressed as an expansion in powers of a post-Newtonian parameter $\varepsilon \sim ( v / c ) ^ { 2 } \sim U / c ^ { 2 }$ ; here the adopted expansion parameter is $\varepsilon : = G M / ( c ^ { 2 } p )$ . The leading term in these equations is the Newtonian answer, and this is labeled a 0pn term. The term of order $\varepsilon$ is the first post-Newtonian correction, and it is labeled a 1pn term. And finally, the term of order $\varepsilon ^ { 2 }$ is a second post-Newtonian correction, or 2pn term. This kind of approximation to general relativity will be a central theme in the remainder of this book.

# 5.6.4 Motion of light

We next examine the motion of a photon in the equatorial plane of a Schwarzschild spacetime. The vector tangent to the photon’s world line is $p ^ { \alpha }$ , and this satisfies the geodesic equation (5.54). A consequence of this equation is that both $p _ { 0 }$ and $p _ { \phi }$ are constants of the motion, and by a constant rescaling of the parameter $\lambda$ on the world line, we can set $p _ { 0 } = - c$ and $p _ { \phi } = h$ . (This rescaling implies that $p ^ { \alpha }$ is not quite the photon’s momentum vector; the unit of momentum has been changed by a factor $p _ { 0 } ^ { \mathrm { r e s c a l e d } } / p _ { 0 } ^ { \mathrm { c o n v e n t i o n a l } } = c ^ { 2 } / ( \hbar \omega _ { \infty } )$ , where $\omega _ { \infty }$ is the photon’s frequency as measured by an observer at rest at infinity. In these units, the parameter $h$ represents the photon’s angular momentum multiplied by $c ^ { 2 }$ and divided by $\hbar \omega _ { \infty }$ .)

We have already obtained two equations of motion,

$$
i = { \frac { 1 } { 1 - R / r } }
$$

![](images/2f4a3d69328e61c02791f2f4851a41ce48ea06cb1ddc836663bd9ade2cfd5c79.jpg)

# Fig. 5.5

Effective potential $\mu ( r )$ for photon motion in the Schwarzschild spacetime, in units of $c ^ { 2 }$ . The angular-momentum parameter $h$ is chosen to be larger than $h _ { c }$ . The horizontal line marks the constant $c ^ { 2 }$ , and in this case the photon meets a turning point at $\begin{array} { r } { r = p > \frac { 3 } { 2 } R . } \end{array}$ The inset displays a photon orbit with $p = 2 . 5 R .$

and

$$
\dot { \phi } = \frac { h } { r ^ { 2 } } ,
$$

and the third follows as a consequence of the null condition $g _ { \alpha \beta } p ^ { \alpha } p ^ { \beta } = 0$ . We get

$$
\dot { r } ^ { 2 } + \mu ( r ) = c ^ { 2 } ,
$$

where

$$
\mu ( r ) = \frac { h ^ { 2 } } { r ^ { 2 } } \biggl ( 1 - \frac { R } { r } \biggr )
$$

is an effective potential for the radial component of the photon’s motion. In these equations an overdot indicates differentiation with respect to the (rescaled) world-line parameter $\lambda$ .

The effective potential of Eq. (5.206) contains only a centrifugal term – compare with Eq. (5.188) – and it represents a barrier. The potential is maximum at $\begin{array} { r } { r = \frac { 3 } { 2 } R = 3 G M / c ^ { 2 } } \end{array}$ , and a photon with $h = h _ { c } : = ( 3 \sqrt { 3 } / 2 ) R c$ can move on a circular orbit at this radius, although the orbit is unstable (see Fig. 5.5). A photon with $h < h _ { c }$ either moves in from $r = \infty$ , or moves out to $r = \infty$ , and this photon does not encounter a turning point of its radial motion. On the other hand, a photon with $h > h _ { c }$ encounters a turning point at a radius $r = p > { \frac { 3 } { 2 } } R$ . It moves in from $r = \infty$ , turns around at $r = p$ , and moves out to $r = \infty$ ; this type of behavior corresponds to the deflection of light by a massive body.

We consider this case in more detail, and examine the deflected motion of a photon with $h > h _ { c }$ . As we have seen, the motion has a radial turning point at $r = p$ , and Eqs. (5.205)

and (5.206) imply the relationship

$$
h ^ { 2 } = { \frac { p ^ { 2 } c ^ { 2 } } { 1 - R / p } }
$$

between the angular-momentum parameter $h$ and the orbital element $p$ . We describe the motion in terms of an orbital parameter $\eta$ , and write

$$
r ( \eta ) = \frac { p } { \sin \eta }
$$

to represent a photon that starts at $r = \infty$ (when $\eta = 0$ ), moves in to $r = p$ (when $\begin{array} { r } { \eta = \frac { \pi } { 2 } } \end{array}$ ), and returns to $r = \infty$ (when $\eta = \pi$ ). This representation is analogous to the one adopted in Eq. (5.191), and in flat spacetime the orbital parameter $\eta$ would be equal to the azimuthal angle $\phi$ ; in the Schwarzschild spacetime these quantities are distinct.

When Eqs. (5.207) and (5.208) are inserted into Eq. (5.206) we obtain

$$
c ^ { 2 } - \mu ( r ) = \frac { c ^ { 2 } \cos ^ { 2 } \eta } { 1 - R / p } \bigg ( 1 - \frac { 1 + \sin \eta + \sin ^ { 2 } \eta } { 1 + \sin \eta } \frac { R } { p } \bigg ) ,
$$

and Eq. (5.205) can be turned into an equation of motion for $\eta ( \lambda )$ . We get

$$
\dot { \eta } = \frac { c \sin ^ { 2 } \eta } { p \sqrt { 1 - R / p } } \bigg ( 1 - \frac { 1 + \sin \eta + \sin ^ { 2 } \eta } { 1 + \sin \eta } \frac { R } { p } \bigg ) ^ { 1 / 2 } .
$$

With this and Eq. (5.203) we obtain

$$
\frac { d t } { d \eta } = \frac { p \sqrt { 1 - R / p } } { c [ 1 - ( \sin \eta ) R / p ] \sin ^ { 2 } \eta } \bigg ( 1 - \frac { 1 + \sin \eta + \sin ^ { 2 } \eta } { 1 + \sin \eta } \frac { R } { p } \bigg ) ^ { - 1 / 2 } ,
$$

which allows computation of the time coordinate along the photon’s world line. Then Eq. (5.204) yields

$$
\frac { d \phi } { d \eta } = \biggl ( 1 - \frac { 1 + \sin \eta + \sin ^ { 2 } \eta } { 1 + \sin \eta } \frac { R } { p } \biggr ) ^ { - 1 / 2 } ,
$$

which determines $\phi$ . Equations (5.208), (5.211), and (5.212) form a complete set of orbital equations for the motion of a deflected photon. These equations must be integrated numerically, and the formulation provided here is convenient for this purpose.

In the course of a complete orbit (from $\eta = 0$ to $\eta = \pi$ ) the azimuthal angle increases by an amount $\Delta \phi$ given by the integral of Eq. (5.212). The integration cannot be accomplished analytically in general, but an expansion in powers of $R / p$ gives

$$
\Delta \phi = \pi + 4 \bigg ( \frac { G M } { c ^ { 2 } p } \bigg ) + \bigg ( \frac { 1 5 \pi } { 4 } - 4 \bigg ) \bigg ( \frac { G M } { c ^ { 2 } p } \bigg ) ^ { 2 } + \cdot \cdot \cdot .
$$

In flat spacetime the answer would be the obvious $\Delta \phi = \pi$ , and the difference between $\Delta \phi$ and $\pi$ is the photon’s deflection angle $\alpha$ . Equation (5.213) reveals that to leading order in a post-Newtonian expansion, $\alpha = 4 G M / ( c ^ { 2 } p )$ . This is the famous deflection of light, to

![](images/55a3238abfe013f6fc480c0c59d3831dec4b9a0669e6153461e745f9ec904d02.jpg)  
Deflection of a photon in Schwarzschild spacetime. The deflection angle $\alpha : = \Delta \phi - \pi$ is plotted as a function of the orbital parameter $p / R$ The higher curve is the exact result, computed by integrating Eq. (5.212) numerically. The lower curve is the approximate expression of Eq. (5.213). We observe that the curves coincide when $p / R \gg 1 .$ When $p / R = 3 / 2 , 5 0$ that $p = 3 G M / c ^ { 2 }$ , the exact deflection angle is infinite: this is the photon’s circular orbit.

which we will return in Chapter 10 in the context of post-Newtonian theory. The exact and approximate versions of the deflection angle are plotted in Fig. 5.6.

# 5.6.5 Spherical bodies in hydrostatic equilibrium

The previous subsections have dealt with the external Schwarzschild metric, which is a solution to the Einstein field equations in vacuum. We next turn to a description of the interior, assuming that the body is in hydrostatic equilibrium; this implies that the interior metric is time-independent. This discussion of stellar structure extends to general relativity the material that was developed in Sec. 2.2 in the context of Newton’s theory.

# Equations of stellar structure

We take the body to consist of a perfect fluid, and we adopt the form of Eq. (5.91) for its energy-momentum tensor:

$$
\begin{array} { r } { T _ { \beta } ^ { \alpha } = ( \mu + p ) u ^ { \alpha } u _ { \beta } / c ^ { 2 } + p \delta _ { \beta } ^ { \alpha } . } \end{array}
$$

Here $\mu$ is the fluid’s proper energy density, $p$ is the pressure, and $u ^ { \alpha }$ is the velocity field. The energy density is decomposed as $\mu = \rho c ^ { 2 } + \epsilon$ , in terms of a proper rest-mass density $\rho$ and a proper density $\epsilon$ of internal (thermodynamic) energy. The first law of thermodynamics implies that these variables are related by $\rho d \epsilon = ( \epsilon + p ) d \rho$ .

In a static situation the fluid’s velocity vector has $u ^ { 0 }$ as its only non-vanishing component, and this can be determined by the normalization condition $g _ { \alpha \beta } u ^ { \alpha } u ^ { \beta } = - c ^ { 2 }$ , in which we insert the metric of Eq. (5.156). We find that $u ^ { 0 } = c e ^ { \Phi / c ^ { 2 } }$ and $u _ { 0 } = - c e ^ { - \Phi / c ^ { 2 } }$ , and the relevant components of the energy-momentum tensor are $- T _ { 0 } ^ { 0 } / c ^ { 2 } = \mu / c ^ { 2 } = \rho + \epsilon / c ^ { 2 }$ , $- T _ { r } ^ { 0 } / c = 0$ , and $T _ { r } ^ { r } = p$ . Inserting these within the field equations of Eq. (5.160), we obtain

$$
\frac { d m } { d r } = 4 \pi r ^ { 2 } ( \rho + \epsilon / c ^ { 2 } ) ,
$$

and

$$
\frac { d \Phi } { d r } = - \frac { G } { r ^ { 2 } f } \big ( m + 4 \pi r ^ { 3 } p / c ^ { 2 } \big ) ,
$$

in which $f : = 1 - 2 G m / ( c ^ { 2 } r )$ . These equations can be compared with their Newtonian counterparts, Eqs. (2.13) and (2.14); recall that the potential $\Phi$ reduces to $U$ in the Newtonian limit.

The field equations must be supplemented with the equation of hydrostatic equilibrium. This is obtained by working out the radial component of the conservation equation $\nabla _ { \beta } T ^ { \alpha \beta } =$ 0. Part of the work was already carried out in Sec. 5.3.2, and a good starting point for this task is Eq. (5.97), the curved-spacetime formulation of Euler’s equation. An even better starting point is found in Box 5.5, which works out the condition of hydrostatic equilibrium for any static spacetime. Adapting this to the specific metric of Eq. (5.156), we find that the pressure of a spherical body in hydrostatic equilibrium is determined by

$$
{ \frac { d p } { d r } } = \big ( \rho + \epsilon / c ^ { 2 } + p / c ^ { 2 } \big ) { \frac { d \Phi } { d r } } .
$$

This equation can be compared with Eq. (2.13). Combining this with Eq. (5.216), we obtain

$$
\frac { d p } { d r } = - \frac { G } { r ^ { 2 } f } \big ( \rho + \epsilon / c ^ { 2 } + p / c ^ { 2 } \big ) \big ( m + 4 \pi r ^ { 3 } p / c ^ { 2 } \big ) ,
$$

an equation known as the Tolman–Oppenheimer–Volkoff $( T O V )$ equation, after Richard C. Tolman (1881–1948), J. Robert Oppenheimer (1904–1967), and George Volkoff (1914– 2000), who were among the first to study the structure of spherical bodies in general relativity.

The equations of relativistic stellar structure involve the fluid variables $\rho , \epsilon , p$ , and the metric variables $m$ and $\Phi$ . There is one more variable $( \epsilon )$ than in the Newtonian theory, and the equations must be supplemented by the first law $\rho d \epsilon = ( \epsilon + p ) d \rho$ and an equation of state $p = p ( \rho )$ . The equations are integrated outward from $r = 0$ with the boundary conditions $\rho ( 0 ) = \rho _ { c } , \epsilon ( 0 ) = \epsilon _ { c } , p ( 0 ) = p _ { c } , m ( 0 ) = 0$ , and $\Phi ( 0 ) = \Phi _ { c }$ . Integration proceeds until the pressure vanishes at the boundary $r = R _ { 0 }$ , and $M : = m ( r = R _ { 0 } )$ i s the body’s total mass. The constant $\Phi _ { c }$ can be adjusted so that $e ^ { - 2 \Phi / c ^ { 2 } }$ matches the value $1 - 2 G M / ( c ^ { 2 } R _ { 0 } )$ at the boundary, and this ensures that the interior metric joins smoothly with the Schwarzschild exterior metric at $r = R _ { 0 }$ .

# Incompressible fluid

The equations of relativistic stellar structure must typically be integrated numerically. There is, however, a simple situation that permits an analytical integration, the rather unphysical case of an incompressible fluid with $\rho = \rho _ { 0 } =$ constant and $\epsilon = 0$ . This situation was the one considered by Karl Schwarzschild in 1915, and the resulting solution is known as the interior Schwarzschild solution. The corresponding Newtonian situation was examined back in Sec. 2.2.2.

The mass function of an incompressible fluid is obtained directly from Eq. (5.215), and is given by

$$
m ( r ) = \frac { 4 \pi } { 3 } \rho _ { 0 } r ^ { 3 } = M ( r / R _ { 0 } ) ^ { 3 } ,
$$

in which $M$ is the total mass and $R _ { 0 }$ the stellar radius. With a little work it can then be shown that Eq. (5.218) integrates to

$$
p = \rho _ { 0 } c ^ { 2 } \frac { \sqrt { 1 - R r ^ { 2 } / R _ { 0 } ^ { 3 } } - \sqrt { 1 - R / R _ { 0 } } } { 3 \sqrt { 1 - R / R _ { 0 } } - \sqrt { 1 - R r ^ { 2 } / R _ { 0 } ^ { 3 } } } ,
$$

in which $R : = 2 G M / c ^ { 2 } < R _ { 0 }$ is the body’s Schwarzschild radius. The pressure properly vanishes at $r = R _ { 0 }$ , and at $r = 0$ it is given by

$$
p _ { c } = \rho _ { 0 } c ^ { 2 } \frac { 1 - \sqrt { 1 - R / R _ { 0 } } } { 3 \sqrt { 1 - R / R _ { 0 } } - 1 } .
$$

This equation reveals that for a fixed density, the central pressure increases as the ratio $R _ { 0 } / R$ decreases, that is, as the body becomes increasingly compact. This is the expected behavior: more pressure is required to support a more compact body against its own weight. But the central pressure becomes infinite when $R _ { 0 }$ reaches a critical value given by

$$
R _ { 0 , \mathrm { c r i t } } = { \frac { 9 } { 8 } } R = { \frac { 9 } { 4 } } { \frac { G M } { c ^ { 2 } } } ,
$$

or when the mass reaches a critical value given by

$$
M _ { \mathrm { c r i t } } = { \bigg ( } { \frac { 3 } { 4 \pi } } { \bigg ) } ^ { 1 / 2 } { \bigg ( } { \frac { 4 c ^ { 2 } } { 9 G } } { \bigg ) } ^ { 3 / 2 } \rho _ { 0 } ^ { - 1 / 2 } = 5 . 6 9 M _ { \odot } { \bigg ( } { \frac { 4 \times 1 0 ^ { 1 7 } { \mathrm { k g / m } } ^ { 3 } } { \rho _ { 0 } } } { \bigg ) } ^ { 1 / 2 } ;
$$

the fiducial value adopted for $\rho _ { 0 }$ is typical of densities found in neutron stars. We have found that the total mass of an incompressible body in general relativity cannot exceed $M _ { \mathrm { c r i t } }$ if the body is to remain in hydrostatic equilibrium. This limiting mass is a purely relativistic phenomenon; there is no such limit in Newtonian gravity.

# Relativistic polytropes

A maximum mass is a generic feature of relativistic stellar models, and the phenomenon is also witnessed in relativistic polytropes, the extension to general relativity of the Newtonian

polytropes examined in Sec. 2.2.3. We consider a fluid with an equation of state

$$
p = K \rho ^ { 1 + 1 / n } , \qquad \epsilon = n p ,
$$

directly imported from Sec. 2.2.3. As in the Newtonian discussion, we introduce the scales $\rho _ { c }$ (central density), $p _ { c } = K \rho _ { c } ^ { 1 + 1 / n }$ (central pressure), $m _ { 0 } = 4 \pi \rho _ { c } r _ { 0 } ^ { 3 }$ (mass scale), $r _ { 0 } ^ { 2 } =$ $( n + 1 ) p _ { c } / ( 4 \pi G \rho _ { c } ^ { 2 } )$ (squared length scale), and work with scale-free variables $\theta$ , $\mu$ , and $\xi$ , such that $\rho = \rho _ { c } \theta ^ { n }$ , $p = p _ { c } \theta ^ { n + 1 }$ , $m = m _ { 0 } \mu$ , and $r = r _ { 0 } \xi$ . We introduce also a relativistic parameter

$$
b : = \frac { p _ { c } } { \rho _ { c } c ^ { 2 } } = \frac { K \rho _ { c } ^ { 1 / n } } { c ^ { 2 } } ,
$$

which is a dimensionless measure of how relativistic the central conditions are; when $b \ll 1$ the body is non-relativistic, and it is highly relativistic when $b > 1$ .

It is a simple matter to convert Eqs. (5.215) and (5.218) to dimensionless forms involving the scale-free variables. We obtain

$$
\frac { d \mu } { d \xi } = \xi ^ { 2 } \theta ^ { n } ( 1 + n b \theta )
$$

and

$$
\frac { d \theta } { d \xi } = - \bigg ( \frac { \mu } { \xi ^ { 2 } } + b \xi \theta ^ { n + 1 } \bigg ) \frac { 1 + ( n + 1 ) b \theta } { 1 - 2 ( n + 1 ) b \mu / \xi } ,
$$

and these are relativistic versions of the Lane–Emden equations of Newtonian stellar structure; we see that they reduce to Eqs. (2.49) when $b  0$ . The equations are integrated outward from $\xi = 0$ with the boundary conditions $\theta ( 0 ) = 1$ and $\mu ( 0 ) = 0$ . Integration proceeds until $\theta = 0$ at $\xi = \xi _ { 1 }$ , which marks the body’s boundary, where both the pressure and density vanish. The body’s total mass is then $M = m _ { 0 } \mu _ { 1 }$ with $\mu _ { 1 } : = \mu ( \xi = \xi _ { 1 } )$ , while the body’s radius is $R _ { 0 } = r _ { 0 } \xi _ { 1 }$ .

For a selected equation of state, that is, for each choice of parameters $K$ and $n$ , integration of Eqs. (5.226) and (5.227) gives rise to a continuous sequence of stellar models parameterized by the central density $\rho _ { c }$ . Alternatively, because the central density is related to the relativistic parameter $b$ by Eq. (5.225), it is convenient to adopt $^ b$ as a parameter on the sequence. Because $m _ { 0 }$ and $r _ { 0 }$ depend on the central density (and therefore on $b$ ), it is necessary to rescale the mass and length units so as to eliminate this dependence before we produce plots of the mass $M$ and radius $R _ { 0 }$ as functions of $b$ on the sequence. We therefore set

$$
M = \bar { m } _ { 0 } b ^ { ( 3 - n ) / 2 } \mu _ { 1 } , \qquad R _ { 0 } = \bar { r } _ { 0 } b ^ { ( 1 - n ) / 2 } \xi _ { 1 } ,
$$

in which

$$
\bar { m } _ { 0 } : = m _ { 0 } b ^ { - ( 3 - n ) / 2 } = \frac { ( n + 1 ) ^ { 3 / 2 } K ^ { n / 2 } c ^ { 3 - n } } { ( 4 \pi ) ^ { 1 / 2 } G ^ { 3 / 2 } } ,
$$

$$
\bar { r } _ { 0 } : = r _ { 0 } b ^ { - ( 1 - n ) / 2 } = \frac { ( n + 1 ) ^ { 1 / 2 } K ^ { n / 2 } c ^ { 1 - n } } { ( 4 \pi ) ^ { 1 / 2 } G ^ { 1 / 2 } } ,
$$

# Fig. 5.7

![](images/3a27b6af3c47f775d810353382c36e82dd836a546d9c5bebe842417dcc147c09.jpg)  
Mass of a relativistic polytrope, in units of $\bar { m } _ { 0 }$ , as a function of the relativistic parameter $b$ , for selected values of the polytropic index n. Models with $b \ll 1$ are non-relativistic, while models with $b$ close to one are relativistic. In each case the mass reaches a maximum value at a critical value of b. A larger $\boldsymbol { \eta }$ means a stiffer equation of state, and a higher maximum mass.

are the rescaled mass and length units, respectively, which are independent of $^ b$ and therefore constant on the sequence. Plots of $M / { \bar { m } } _ { 0 }$ as a function of $b$ for selected values of the polytropic index $n$ are presented in Fig. 5.7.

<table><tr><td>Box 5.9</td><td>Neutron stars</td></tr><tr><td></td><td>Exceptforblack holes,neutronstarsare the mostdenseobjects intheuniverse,andtheirgravitationalfieldsare So strong thattheir description mustbe based upon general relativity.Atypical neutron star hasa mass around 1.4 M,a radius ofthe orderof 10km,a density comparable to 6.6 × 1017 kg/m³,and the strength of its gravitational field is measured by GM/(c² R) ~ O.21. Most neutron stars harbour intense magnetic fields, anging from 1O8 T to perhaps 1O11 T,and many are active pulsars, emiting sharp pulses of radio waves or X-rays at very regular time intervals. Neutron stars are formed in supernovae events, during which the outer layers of a normal star at the end stage ofits stellar evolution are ejected in a violent explosion,and the core undergoes gravitational collapse.The neutron-star state is one of the three posible forms of stellar death,along with the white-dwarf state for less massive stars (up to approximately 5 solar masss) and the black-hole state for more massive stars (from approximately 30 solar masses).</td></tr></table>

The internal composition of neutron stars is governed by the physics of nuclear matter at densities that far exceed those of ordinary nuclei. While this nuclear physics is fairly well understood at the relatively low densities found near the surface, it becomes less certain as the density increases toward the center. The outer layer of a neutron star is believed to be made of ordinary heavy nuclei, but this familiar form of matter gives way to a distribution of superfluid neutrons deeper inside the star. Deeper still the neutrons arrange themselves in lattice structures, and eventually the density becomes sufficiently large to accommodate exotic forms of matter such as pion, kaon, and hyperon condensates, and perhaps even strange quark matter.

The structure of a neutron star is determined by the equations of stellar structure reviewed in the text, and by the equation of state $p = p ( \rho )$ of nuclear matter, which depends on the details of the strong nuclear interactions at the high densities involved. Because the equation of state is highly uncertain beyond normal nuclear densities, the structure of neutron stars is still poorly understood. In practice various models of the relevant nuclear physics are encoded in model equations of state, and the equations of stellar structure are integrated for each equation of state, giving rise to a sequence of stellar models parameterized by the central density $\rho _ { c } ,$ each sequence features a maximum mass beyond which the models are dynamically unstable.

Models of neutron stars are constrained by measurements of their masses and radii. A measurement of the mass can be made when the neutron star is an active pulsar and a member of a binary system. In such cases it is found that most masses are clustered between $1 . 3 ~ M _ { \odot }$ and $1 . 6 M _ { \odot }$ , but a mass as high as $2 . 4 \pm 0 . 4 M _ { \odot }$ was deduced for the “black-widow pulsar,” a 1.6 ms pulsar in orbit around a low-mass star, which has transferred a large fraction of its original mass to the neutron star. Another large-mass neutron star is PSR J1614-2230, a 3.15 ms pulsar in orbit around a $0 . 5 M _ { \odot }$ white dwarf; its mass was measured in 2010 to be $1 . 9 7 \pm 0 . 0 4 M _ { \odot }$ by exploiting the Shapiro time delay, a relativistic effect to be introduced in Sec. 10.2.5. These measurements imply that the maximum mass of a neutron star must exceed 2 $M _ { \odot } ,$ and this observation rules out a number of model equations of state, including some associated with more exotic forms of matter.

The radius of a neutron star is much harder to estimate, but substantial progress has been achieved in the last few years by exploiting the measured light curves of X-ray bursters displaying photospheric radius expansion, and of transient low-mass $\tt X$ -ray binaries. These measurements permit the simultaneous estimation of both the mass and radius of a small sample of neutron stars (with fairly large uncertainties), and these estimates can be used to constrain the equation of state of nuclear matter. These studies reveal that a typical neutron star of $1 . 4 M _ { \odot }$ should have a radius between $1 1 \mathrm { k m }$ and $1 2 \mathrm { k m }$ , and confirm that the maximum mass should be larger than 2 $M _ { \odot }$ .

# 5.7 Bibliographical notes

Our survey of curved spacetime and general relativity is very incomplete, and the reader is invited to pursue an advanced education by consulting some of the excellent textbooks devoted to this subject. Among our favorites are the introductory texts by Schutz (2003 and 2009) and Hartle (2003), the venerable classics by Weinberg (1972) and Misner, Thorne, and Wheeler (1973), and the more modern treatments by Wald (1984) and Carroll (2003).

Our presentation of the linearized theory in Sec. 5.5 is modelled on Flanagan and Hughes (2005). Schwarzschild’s original paper can be found in an English translation at arXiv.org/abs/physics/9905030. (Warning: The translators of the paper claim incorrectly that it proves the “science fiction” of black holes; Schwarzschild’s solution uses slightly unusual coordinates, but it’s still the spacetime of a black hole.) The Painleve–´ Gullstrand coordinates to describe the Schwarzschild metric (Sec. 5.6.2) were discovered independently by Painleve (1921) and Gullstrand (1922); their properties are described in´ more depth in Martel and Poisson (2001). Relativistic polytropes (Sec. 5.6.5) were first investigated by Tooper (1965).

The physics of neutron stars, summarized so briefly in Box 5.9, is reviewed much more thoroughly in Shapiro and Teukolsky (1983), Glendenning (2000), and Friedman and Stergioulas (2013). A survey of equations of state for nuclear matter is provided by Lattimer and Prakash (2001 and 2007), and Steiner et al. (2010) describe the state-of-the-art in mass and radius determinations. The recent discovery of a two solar-mass pulsar is reported in Demorest et al. (2010).

# 5.8 Exercises

5.1 (a) Transform the metric of Minkowski spacetime from the usual $( c t , x , y , z )$ coordinates of an inertial frame, to new coordinates $( c t ^ { \prime } , x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ related by the coordinate transformation

$$
\begin{array} { r l } & { c t = \alpha ^ { - 1 } ( 1 + \alpha x ^ { \prime } ) \sinh ( \alpha c t ^ { \prime } ) , } \\ & { ~ x = \alpha ^ { - 1 } ( 1 + \alpha x ^ { \prime } ) \cosh ( \alpha c t ^ { \prime } ) , } \\ & { ~ y = y ^ { \prime } , } \\ & { z = z ^ { \prime } , } \end{array}
$$

where $\scriptstyle { \alpha : = g / c ^ { 2 } }$ , with $g$ a constant with the dimensions of an acceleration.

(b) For $\alpha c t ^ { \prime } \ll 1$ , show that the origin of the new frame $( x ^ { \prime } = 0$ ) is uniformly accelerated, in the Newtonian sense.   
(c) Show that a clock at rest at $x ^ { \prime } = h$ runs fast compared to a clock at rest at $x ^ { \prime } = 0$ by a factor $( 1 + g h / c ^ { 2 } )$ . How does this relate to the principle of equivalence?   
(d) For an observer at the spatial origin of the new frame, calculate the components of the spacetime velocity $\vec { u }$ and acceleration $\vec { a }$ vectors. Verify that ${ \vec { u } } \cdot { \vec { u } } = - c ^ { 2 }$ , ${ \vec { u } } \cdot { \vec { a } } = 0$ , and that ${ \vec { a } } \cdot { \vec { a } } = g ^ { 2 }$ .

This is the Rindler spacetime of a uniformly accelerated observer.

5.2 In electrodynamics, a charge that accelerates relative to an inertial frame radiates electromagnetic radiation. A charge that is at rest or in uniform motion in an inertial frame does not radiate. Consider the following situations: (a) a charge is at rest near the surface of the Earth; (b) a charge is in free fall near the surface of the Earth. Assume for simplicity that the Earth itself is at rest in an inertial frame. In which case does the charge radiate electromagnetic waves to infinity? Does this conflict with the Einstein equivalence principle? Why or why not?

5.3 Prove the following useful relations:

(a) $\nabla _ { \gamma } g _ { \alpha \beta } = 0$ ;   
(b) $g _ { \alpha \mu } \partial _ { \gamma } g ^ { \mu \beta } = - g ^ { \mu \beta } \partial _ { \gamma } g _ { \alpha \mu }$ ;   
(c) $\partial _ { \gamma } g ^ { \alpha \beta } = - \Gamma _ { \mu \gamma } ^ { \alpha } g ^ { \mu \beta } - \Gamma _ { \mu \gamma } ^ { \beta } g ^ { \mu \alpha }$ ;   
(d) $\Gamma _ { \alpha \gamma } ^ { \alpha } = \partial _ { \gamma } \ln ( \sqrt { - g } )$ , where $g = \operatorname* { d e t } ( g _ { \mu \nu } )$ ;   
(e) $\sqrt { - g } g ^ { \mu \nu } \Gamma _ { \mu \nu } ^ { \alpha } = - \partial _ { \beta } ( \sqrt { - g } g ^ { \alpha \beta } )$ .

5.4 Prove the following results:

(a) Divergence of a vector:

$$
\nabla _ { \alpha } { \cal A } ^ { \alpha } = { \frac { 1 } { \sqrt { - g } } } \partial _ { \alpha } \bigl ( \sqrt { - g } { \cal A } ^ { \alpha } \bigr ) ;
$$

(b) Divergence of a second-rank tensor:

$$
\begin{array} { l } { { \nabla _ { \beta } { \cal A } _ { \alpha } ^ { ~ \beta } = \displaystyle \frac { 1 } { \sqrt { - g } } \partial _ { \beta } \big ( \sqrt { - g } { \cal A } _ { \alpha } ^ { ~ \beta } \big ) - \Gamma _ { \alpha \mu } ^ { \gamma } { \cal A } _ { \gamma } ^ { ~ \mu } , } } \\ { { { } } } \\ { { \nabla _ { \beta } { \cal A } ^ { \alpha \beta } = \displaystyle \frac { 1 } { \sqrt { - g } } \partial _ { \beta } \big ( \sqrt { - g } { \cal A } ^ { \alpha \beta } \big ) + \Gamma _ { \mu \nu } ^ { \alpha } { \cal A } ^ { \mu \nu } ; } } \end{array}
$$

(c) D’Alembertian of a scalar field:

$$
\sqcup _ { g } \phi : = g ^ { \mu \nu } \nabla _ { \mu } \nabla _ { \nu } \phi = { \frac { 1 } { \sqrt { - g } } } \partial _ { \mu } { \bigl ( } { \sqrt { - g } } g ^ { \mu \nu } \partial _ { \nu } \phi { \bigr ) } .
$$

5.5 Show explicitly that if a vector $\vec { A }$ is parallel-transported along a world line, then ${ \vec { A } } \cdot { \vec { A } }$ is constant along the world line.

5.6 (a) By transforming from $x - y$ coordinates to $r { - } \phi$ coordinates, write down the metric of two-dimensional Euclidean space in polar coordinates, and calculate all the Christoffel symbols. (b) Write down the geodesic equation, $d ^ { 2 } x ^ { j } / d s ^ { 2 } + \Gamma _ { n k } ^ { j } ( d x ^ { k } / d s ) ( d x ^ { n } / d s ) = 0$ , for the two coordinates $x ^ { 1 } = r$ and $x ^ { 2 } = \phi$ , where $s$ is proper distance along the geodesic. (c) Solve the geodesic equations explicitly for $r ( s )$ and $\phi ( s )$ , and show that they are equivalent to the usual equations for straight-line motion, $x = A s + B , y$ $y =$ $C s + D$ , where $A , B , C$ , and $D$ are constants.

5.7 (a) Write down the metric of a two-dimensional sphere of unit radius, in standard $\theta { - } \phi$ coordinates. Calculate the Christoffel symbols, and find the geodesic equations for $\theta ( s )$ and $\phi ( s )$ . (b) Show that the curve $\phi =$ constant, $\theta = A s + B$ is a geodesic, and describe the curve in words. (c) Show that the curve $\theta =$ constant, $\phi = C s + D$ is a geodesic for only one specific value of $\theta$ . Find that value and describe the curve in words.

5.8 As we saw in the text, a timelike geodesic between events 1 and 2 in spacetime is a curve that maximizes the proper-time functional

$$
\tau = \frac { 1 } { c } \int _ { 1 } ^ { 2 } L ( r ^ { \alpha } , \dot { r } ^ { \alpha } ) d \lambda , \qquad L ( r ^ { \alpha } , \dot { r } ^ { \alpha } ) : = \sqrt { - g _ { \alpha \beta } \dot { r } ^ { \alpha } \dot { r } ^ { \beta } } ,
$$

where $r ^ { \alpha } ( \lambda )$ is an arbitrary world line that links events 1 and 2, $\lambda$ is an arbitrary parameter that ranges between $\lambda _ { 1 }$ and $\lambda _ { 2 }$ , and $\dot { r } ^ { \alpha } = d x ^ { \alpha } / d \lambda$ .

(a) Prove that the functional is invariant under a general reparameterization of the form $\lambda \to \lambda ^ { \prime } = f ( \lambda )$ , where $f$ is any monotonic function of its argument.   
(b) Prove that the geodesic is described by a generalized form of the geodesic equation, $\ddot { r } ^ { \alpha } + \Gamma _ { \beta \gamma } ^ { \alpha } \dot { r } ^ { \beta } \dot { r } ^ { \gamma } = \kappa \dot { r } ^ { \alpha }$ . Express $\kappa ( \lambda )$ in terms of $L$ .   
(c) Show that the geodesic equation assumes its usual form (with a zero right-hand side) when proper time $\tau$ is adopted as the parameter $\lambda$ . (This can be done only after the variation has been performed.)   
(d) Prove that the usual form of the geodesic equation is invariant under a reparameterization of the form $\tau \to \tau ^ { \prime } = a \tau + b$ , where $a$ and $b$ are constants; this defines the class of affine parameters.   
(e) Show that the usual form of the geodesic equation can be derived on the basis of the alternative Lagrangian $L ^ { \prime } ( r ^ { \alpha } , \dot { r } ^ { \alpha } ) = g _ { \alpha \beta } \dot { r } ^ { \alpha } \dot { r } ^ { \beta }$ , where $\dot { r } ^ { \alpha } = d x ^ { \alpha } / d \tau$ .

5.9 (a) Show that the condition $R _ { \alpha [ \beta \gamma \delta ] } = 0$ is equivalent to the cyclic condition of Eq. (5.59d). (b) By counting components, show that the antisymmetry conditions $R _ { \alpha \beta ( \gamma \delta ) } = 0$ and $R _ { ( \alpha \beta ) \gamma \delta } = 0$ , together with the cyclic condition $R _ { \alpha [ \beta \gamma \delta ] } = 0$ , are sufficient to leave 20 independent components of the Riemann tensor. (c) Show that the antisymmetry conditions together with the symmetry $R _ { \gamma \delta \alpha \beta } =$ $R _ { \alpha \beta \gamma \delta }$ are not sufficient, but must be supplemented by one additional constraint, given by $R _ { \alpha [ \beta \gamma \delta ] } = 0$ with all four indices distinct.

5.10 (a) Verify that

$$
R _ { \beta \gamma \delta } ^ { \alpha } = \partial _ { \gamma } \Gamma _ { \beta \delta } ^ { \alpha } - \partial _ { \delta } \Gamma _ { \beta \gamma } ^ { \alpha } + \Gamma _ { \mu \gamma } ^ { \alpha } \Gamma _ { \beta \delta } ^ { \mu } - \Gamma _ { \mu \delta } ^ { \alpha } \Gamma _ { \beta \gamma } ^ { \mu }
$$

by carrying out the explicit calculations of Eq. (5.57).

(b) Prove the Bianchi identity,

$$
\nabla _ { \alpha } R _ { \mu \nu \beta \gamma } + \nabla _ { \gamma } R _ { \mu \nu \alpha \beta } + \nabla _ { \beta } R _ { \mu \nu \gamma \alpha } = 0 .
$$

Hint: Because it is a tensorial equation, the identity can be verified in any coordinate system. Choose a local inertial frame, in which the Christoffel symbols vanish (but not their derivatives!).

(c) Verify the contracted Bianchi identity, $\nabla _ { \beta } G ^ { \alpha \beta } = 0$ .

5.11 Show that the metric

$$
d s ^ { 2 } = - d ( c t ) ^ { 2 } + ( c t / a ) ^ { 2 } \left[ \frac { d r ^ { 2 } } { 1 + r ^ { 2 } / a ^ { 2 } } + r ^ { 2 } \big ( d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } \big ) \right] ,
$$

where $a$ is a constant with units of distance, is that of flat spacetime: (a) by finding a coordinate transformation that brings the line element to the Minkowski form everywhere in spacetime; and (b) by calculating at least five non-trivial components of its Riemann tensor.

5.12 (a) Calculate the Riemann curvature tensor for the metric of a two-dimensional sphere of unit radius. (b) Repeat for an infinitely long, two-dimensional cylinder of unit radius. What do you make of your answer for the Riemann tensor?

5.13 (a) For a perfect fluid, show that the relativistic Euler equation can be written in the form

$$
( \mu + p ) \left( \frac { d u _ { \alpha } } { d \tau } - \frac { 1 } { 2 } u ^ { \beta } u ^ { \gamma } \partial _ { \alpha } g _ { \beta \gamma } \right) = - c ^ { 2 } \partial _ { \alpha } p - u _ { \alpha } \frac { d p } { d \tau } ,
$$

in which $\tau$ is proper time along the world line of a fluid element.

(b) If the fluid undergoes a stationary flow (pressure, density independent of $t$ ) in a stationary spacetime $( g _ { \mu \nu }$ independent of $t$ ), prove that $( \mu + p ) u _ { 0 } \mathcal { V } =$ constant along the flow lines. This is the relativistic version of Bernoulli’s equation.

5.14 Show that the mass density of a point particle can be written in the form

$$
\rho ( x ^ { \alpha } ) = \frac { m c } { u ^ { 0 } \sqrt { - g } } \delta _ { 3 } \bigl ( x - r ( t ) \bigr ) .
$$

5.15 By exploiting only spherical symmetry, we can always write the metric of a spherically-symmetric spacetime in the form

$$
d s ^ { 2 } = - e ^ { - 2 \Phi / c ^ { 2 } } d ( c t ) ^ { 2 } - 2 h d ( c t ) d r + e ^ { 2 \Lambda / c ^ { 2 } } d r ^ { 2 } + r ^ { 2 } \bigl ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } \bigr ) ,
$$

in which $\Phi , \Lambda$ , and $h$ are arbitrary functions of $t$ and $r$ . Show that it is always possible to find a transformation $t = F ( T , r )$ so that the metric in $( T , r , \theta , \phi )$ coordinates has no off-diagonal $d ( c t ) d r$ term.

5.16 (a) Show that the isotropic coordinates

$$
X ^ { ( \mu ) } : = \left\{ t , x _ { \mathrm { i s o } } = r _ { \mathrm { i s o } } \sin \theta \cos \phi , \ y _ { \mathrm { i s o } } = r _ { \mathrm { i s o } } \sin \theta \sin \phi , \ z _ { \mathrm { i s o } } = r _ { \mathrm { i s o } } \cos \theta \right\}
$$

do not satisfy the harmonic coordinate condition, Eq. (5.175).

(b) Show that the spherical polar harmonic coordinates $( t , r _ { \mathrm { h } } , \theta , \phi )$ do not satisfy the harmonic coordinate condition.

5.17 If $\dot { g } _ { \alpha \beta } : = \eta _ { \alpha \beta } + p _ { \alpha \beta }$ , show that to first order in $p _ { \alpha \beta }$ , the harmonic coordinate condition (5.177) is equivalent to the Lorenz-gauge condition of linearized theory, $\partial ^ { \beta } \bar { p } _ { \alpha \beta } = 0$ , where $\bar { p } _ { \alpha \beta }$ is the trace-reversed perturbation, and indices are raised and lowered using $\eta _ { \alpha \beta }$ .

5.18 In the course of your study of general relativity you come across a vacuum solution to the Einstein field equations given by

$$
\begin{array} { l } { { d s ^ { 2 } = - d ( c t ) ^ { 2 } + \left( \frac { 4 \alpha c t x ^ { j } } { r ( r ^ { 2 } - \alpha ^ { 2 } ) } \right) d ( c t ) d x ^ { j } } } \\ { { \ + \left[ \frac { ( r + \alpha ) ^ { 4 } } { r ^ { 4 } } \delta _ { j k } - \frac { 4 \alpha ^ { 2 } c ^ { 2 } t ^ { 2 } x ^ { j } x ^ { k } } { r ^ { 2 } ( r ^ { 2 } - \alpha ^ { 2 } ) ^ { 2 } } \right] d x ^ { j } d x ^ { k } , } } \end{array}
$$

in which $\alpha$ is a constant and $r ^ { 2 } : = \delta _ { j k } x ^ { j } x ^ { k }$ . You take it upon yourself to study the significance of this spacetime.

(a) Transform the metric from the Cartesian coordinates $x ^ { j }$ to the standard spherical polar coordinates $( r , \theta , \phi )$ , and show that the metric is, in fact, spherically symmetric. Hint: What are $\delta _ { j k } d x ^ { j } d x ^ { k }$ and $( x ^ { j } / r ) d x ^ { j }$ in spherical coordinates?   
(b) Calculate the acceleration of a body at rest at very large $r$ , and use your result to relate the parameter $\alpha$ to the total mass $M$ in the spacetime.   
(c) Find a coordinate transformation that puts the metric in a static form, and confirm your result in part (b) by reading off the mass directly from the metric.   
(d) Can you name this spacetime?

5.19 Calculate the potential $\Phi ( \boldsymbol { r } )$ for a spherical body of uniform density. Make sure to impose the proper boundary conditions at the boundary $r = R _ { 0 }$ .

5.20 Suppose that a free-falling observer moves radially inward in the Schwarzschild spacetime, having started from rest at infinity; denote the observer’s four-velocity $u ^ { \alpha }$ . Furthermore, suppose that a photon is also moving radially inward, and that it is just about to catch up with the observer; denote the photon’s four-momentum $p ^ { \alpha }$ and its energy-at-infinity $\hbar \omega _ { \infty }$ . On the basis of the general formula

$$
\hbar \omega = - g _ { \alpha \beta } p ^ { \alpha } u ^ { \beta } ,
$$

calculate the photon’s frequency $\omega$ as measured by the observer when the photon catches up with her. Express your result in terms $\omega _ { \infty }$ and $r _ { 0 }$ , the radius at which the photon and observer meet. Is this a redshift or a blueshift? Does the expression become singular at the event horizon? Should it?

In this chapter we embark on a general program to specialize the formulation of general relativity to a description of weak gravitational fields. We will go from the exact theory, which governs the behavior of arbitrarily strong fields, such as those of neutron stars and black holes, to a useful approximation that applies to weak fields, such as those of planets, main-sequence stars, and white dwarfs. This approximation will reproduce the predictions of Newtonian theory, but we will formulate a method that can be pushed systematically to higher and higher order to produce an increasingly accurate description of a weak gravitational field. We shall find that the method is so successful that it can actually handle fields that are not so weak. For example, it provides a perfectly adequate description of gravity at a safe distance from a neutron star, and it can be used as a foundation to study the motion of a binary black-hole system, provided that the mutual gravity between bodies is weak.

The foundation for these methods is “post-Minkowskian theory,” the topic of this chapter and the next. In post-Minkowskian theory the strength of the gravitational field is measured by the gravitational constant $G$ , and the Einstein field equations are formally expanded in powers of $G$ . At zeroth post-Minkowskian order there is no field, and one deals with Minkowski spacetime. At first post-Minkowskian order the gravitational field appears as a correction of order $G$ to the Minkowski metric, and the (linearized) field equations are integrated to obtain this correction. The correction is refined by terms of order $G ^ { 2 }$ in the second post-Minkowskian approximation, and the process is continued until the desired degree of accuracy is achieved.

The formulation of the Einstein field equations that is best suited to this post-Minkowskian expansion was put forward by Landau and Lifshitz, and this framework is introduced in Sec. 6.1. In Sec. 6.2 we refine the Landau–Lifshitz formulation by imposing the harmonic coordinate conditions, and we show that the exact field equations can be expressed as a set of ten wave equations in Minkowski spacetime, with complicated and highly non-linear source terms. We explain how the metric can be systematically expanded in powers of the gravitational constant $G$ and inserted within the wave equations; these are iterated a number of times, and each iteration increases the accuracy of the solution by one power of $G$ .

In Sec. 6.3 we develop mathematical techniques to integrate the wave equation in flat spacetime. We begin by introducing the retarded Green’s function for the wave equation, and we explain how the solution can be expressed as an integral over the past light cone of the spacetime point at which it is evaluated. Our methods involve a partition of threedimensional space into near-zone and wave-zone regions, and we describe how the lightcone integral, decomposed into near-zone and wave-zone contributions, can be evaluated.

In Chapter 7 we implement the techniques developed here and construct the second post-Minkowskian approximation to the metric of a weakly curved spacetime. The post-Minkowskian approximation does not rely on an assumption that the matter distribution moves slowly. While this may be the typical context – in a gravitationally bound system, weak gravitational fields induce slow motions – we shall nevertheless divorce the weakfield assumption from a logically distinct slow-motion assumption, which is not required for the developments of this chapter. We shall eventually return to slow motions, however, and formulate an approximation method that incorporates both weak-field and slow-motion aspects. This is the domain of post-Newtonian theory, an approximation to general relativity that combines an expansion in powers of $G$ (to measure the strength of the field) with an expansion in powers of $c ^ { - 2 }$ (to measure the velocity of the matter distribution). Post-Newtonian theory is informally introduced in Chapter 7, but it is developed more systematically in Chapters 8, 9, and 10. The other main applications of post-Minkowskian theory, gravitational waves and radiation reaction, are the subject of Chapters 11 and 12.

# 6.1 Landau–Lifshitz formulation of general relativity

# 6.1.1 New formulation of the field equations

The post-Minkowskian approach to integrate the Einstein field equations is based on the Landau and Lifshitz formulation of these equations. In this framework the main variables are not the components of the metric tensor $g _ { \alpha \beta }$ but those of the “gothic inverse metric”

$$
{ \mathfrak { g } } ^ { \alpha \beta } : = { \sqrt { - g } } g ^ { \alpha \beta } ,
$$

where $g ^ { \alpha \beta }$ is the inverse metric and $g$ the metric determinant. The factor of $\scriptstyle { \sqrt { - g } }$ implies that ${ \mathfrak { g } } ^ { \alpha \beta }$ is not a tensor; such objects, which differ from tensors by factors of the metric gdeterminant, are known as tensor densities. Knowledge of the gothic metric is sufficient to determine the metric itself: note first that $\operatorname* { d e t } [ { \mathfrak { g } } ^ { \alpha \beta } ] = g$ , so that $g$ can be directly obtained from the gothic metric; then Eq. (6.1) gives $g ^ { \alpha \beta }$ , which can be inverted to obtain $g _ { \alpha \beta }$ .

In the Landau–Lifshitz formulation, the left-hand side of the field equations is built from

$$
H ^ { \alpha \mu \beta \nu } : = \mathfrak { g } ^ { \alpha \beta } \mathfrak { g } ^ { \mu \nu } - \mathfrak { g } ^ { \alpha \nu } \mathfrak { g } ^ { \beta \mu } .
$$

This tensor density is readily seen to possess the same symmetries as the Riemann tensor,

$$
H ^ { \mu \alpha \beta \nu } = - H ^ { \alpha \mu \beta \nu } , \qquad H ^ { \alpha \mu \nu \beta } = - H ^ { \alpha \mu \beta \nu } , \qquad H ^ { \beta \nu \alpha \mu } = H ^ { \alpha \mu \beta \nu } .
$$

It also satisfies the remarkable identity

$$
\partial _ { \mu \nu } H ^ { \alpha \mu \beta \nu } = 2 ( - g ) G ^ { \alpha \beta } + \frac { 1 6 \pi G } { c ^ { 4 } } ( - g ) t _ { \mathrm { L L } } ^ { \alpha \beta } ,
$$

in which $G ^ { \alpha \beta }$ is the Einstein tensor, and

$$
\begin{array} { c } { { ( - g ) t _ { \mathrm { L L } } ^ { \alpha \beta } : = \displaystyle \frac { c ^ { 4 } } { 1 6 \pi G } \Bigg \{ \partial _ { \lambda } g ^ { \alpha \beta } \partial _ { \mu } g ^ { \lambda \mu } - \partial _ { \lambda } g ^ { \alpha \lambda } \partial _ { \mu } g ^ { \beta \mu } + \displaystyle \frac { 1 } { 2 } g ^ { \alpha \beta } g _ { \lambda \mu } \partial _ { \rho } g ^ { \lambda \nu } \partial _ { \nu } g ^ { \mu \rho } } } \\ { { - g ^ { \alpha \lambda } g _ { \mu \nu } \partial _ { \rho } g ^ { \beta \nu } \partial _ { \lambda } g ^ { \mu \rho } - g ^ { \beta \lambda } g _ { \mu \nu } \partial _ { \rho } \mathfrak { g } ^ { \alpha \nu } \partial _ { \lambda } \mathfrak { g } ^ { \mu \rho } + g _ { \lambda \mu } g ^ { \nu \rho } \partial _ { \nu } \mathfrak { g } ^ { \alpha \lambda } \partial _ { \rho } \mathfrak { g } ^ { \beta \mu } } } \\ { { + \displaystyle \frac { 1 } { 8 } \big ( 2 g ^ { \alpha \lambda } g ^ { \beta \mu } - g ^ { \alpha \beta } g ^ { \lambda \mu } \big ) \big ( 2 g _ { \nu \rho } g _ { \sigma \tau } - g _ { \rho \sigma } g _ { \nu \tau } \big ) \partial _ { \lambda } \mathfrak { g } ^ { \nu \tau } \partial _ { \mu } \mathfrak { g } ^ { \rho \sigma } \Bigg \} \quad ( 6 . } } \end{array}
$$

is the Landau–Lifshitz pseudotensor, so named because it does not transform as a tensor under a general coordinate transformation; the quantity $\partial _ { \mu \nu } H ^ { \alpha \mu \beta \nu }$ is also a pseudotensor, and $( - g ) G ^ { \alpha \beta }$ is a tensor density. Equation (6.4) is valid for any spacetime, whether or not its metric is a solution to the Einstein field equations.

The identity of Eq. (6.4) implies that the Einstein field equations, $G ^ { \alpha \beta } = ( 8 \pi G / c ^ { 4 } ) T ^ { \alpha \beta }$ , can be expressed in the alternative, non-tensorial form

$$
\partial _ { \mu \nu } H ^ { \alpha \mu \beta \nu } = \frac { 1 6 \pi G } { c ^ { 4 } } ( - g ) \bigl ( T ^ { \alpha \beta } + t _ { \mathrm { L L } } ^ { \alpha \beta } \bigr ) .
$$

As promised, the left-hand side involves $H ^ { \alpha \mu \beta \nu }$ , and the right-hand side is built from $T ^ { \alpha \beta }$ , the energy-momentum tensor of the matter distribution, and $t _ { \mathrm { L L } } ^ { \alpha \beta }$ . This form of the field equations provides the Landau–Lifshitz pseudotensor with a loose physical interpretation: it represents the distribution of gravitational-field energy in spacetime, which is added to the matter contribution on the right-hand side of the field equations.

By virtue of the antisymmetry of $H ^ { \alpha \mu \beta \nu }$ in the last pair of indices, we have that the equation

$$
\partial _ { \beta \mu \nu } H ^ { \alpha \mu \beta \nu } = 0
$$

holds as an identity. This, together with Eq. (6.6), implies that

$$
\partial _ { \beta } \Big [ ( - g ) \big ( T ^ { \alpha \beta } + t _ { \mathrm { L L } } ^ { \alpha \beta } \big ) \Big ] = 0 .
$$

These are conservation equations for the total energy-momentum pseudotensor, expressed in terms of a partial-derivative operator. These equations are equivalent to the usual expression of energy-momentum conservation, $\nabla _ { \beta } T ^ { \alpha \beta } = 0$ , which involves only the matter’s energymomentum tensor and a covariant-derivative operator.

As we have seen, Eqs. (6.6) and (6.8) suggest that $t _ { \mathrm { L L } } ^ { \alpha \beta }$ can be interpreted as an energymomentum (pseudo)tensor for the gravitational field, and this interpretation is supported by the fact that the Landau–Lifshitz pseudotensor is quadratic in $\partial _ { \mu } { \mathfrak { g } } ^ { \alpha \beta }$ , just as the energymomentum tensor of the electromagnetic field is quadratic in $\partial _ { \mu } A ^ { \alpha }$ . This interpretation, however, is not to be taken literally. It is, after all, based on a very specific reformulation of the Einstein field equations, and other reformulations would give rise to other candidates for the energy-momentum pseudotensor. And it is based on a non-tensorial quantity whose numerical value can change arbitrarily by performing a coordinate transformation; indeed, $t _ { \mathrm { L L } } ^ { \alpha \beta }$ can be made to vanish at any selected event in spacetime by adopting Riemann normal coordinates in the neighborhood of this event (refer to Sec. 5.2.5). The literature abounds with attempts to introduce the energy-momentum tensor for the gravitational field. Such an object does not exist; do not fall prey to false prophets.

<table><tr><td>Box 6.1</td><td>Two versions of energy-momentum conservation We state in the text that the two versions of energy-momentum conservation,VβTαβ = O and</td></tr><tr><td></td><td>δβ[(-g)(Tβ t)]=Oreeqivalent. Ifct,tereisamportatconceptualdiferecebeteen these statements.The first equation is a direct consequence of the local conservation of energy-momentum, as observed in a local inertial frame; as such it is valid whether or not Einstein&#x27;s equations are satisfied,or in- ded,whether or not general relativity is the correct theory of gravity.The fact that it is compatible with the Bianchi dentity, VβGαβ= O,isanadded featurespecific to Einstein&#x27;stheory.There are alternativetheories that lack this consistency,and yet Vβ Tαβ is still zero. By contrast, the second conservation equation folows only after using Einstein&#x27;s equations to derive Eq.(6.6).Furthermore,the tedious calculations required to establish that the two versions are equivalent involve inserting the feld equations (6.6)at various critical steps along the way. The botm line is that the conservation equation VβTαβ = O is fundamental; the equation δβ[(-g)(Tαβ + tL)] = O is a consequenceof Einstein&#x27;s equations.If Einstein&#x27;s equations are satisfied, then either equation may be adopted to express energy-momentum conservation,and the statements are equivalent in this sense.</td></tr></table>

Equations (6.1)–(6.8) form the core of the Landau–Lifshitz framework. It is out of the question to provide a derivation of these equations (the calculations are straightforward but extremely lengthy), but the following considerations, borrowed from Landau and Lifshitz in their influential book The Classical Theory of Fields, will provide at least a partial understanding of where they come from.

Let us write down the Einstein field equations, in their usual tensorial form

$$
G ^ { \alpha \beta } = { \frac { 8 \pi G } { c ^ { 4 } } } T ^ { \alpha \beta } ,
$$

at an event $P$ in spacetime, in a local coordinate system such that $\partial _ { \gamma } g _ { \alpha \beta } ( P ) \stackrel { * } { = } 0$ . (We do not demand that $g _ { \alpha \beta } \stackrel { * } { = } \eta _ { \alpha \beta }$ at $P$ ; the special equality sign $\stackrel { * } { = }$ means “equals in the selected coordinate system.”) In these coordinates the Riemann tensor at $P$ involves only the metric and its second derivatives, and a short computation reveals that the Einstein tensor is given by

$$
\begin{array} { c } { { G ^ { \alpha \beta } \overset { * } { = } \frac 1 2 \big ( g ^ { \alpha \lambda } g ^ { \beta \mu } g ^ { \nu \rho } + g ^ { \beta \lambda } g ^ { \alpha \mu } g ^ { \nu \rho } - g ^ { \alpha \lambda } g ^ { \beta \rho } g ^ { \mu \nu } - g ^ { \alpha \mu } g ^ { \beta \nu } g ^ { \lambda \rho } } } \\ { { { } } } \\ { { - g ^ { \alpha \beta } g ^ { \mu \lambda } g ^ { \nu \rho } + g ^ { \alpha \beta } g ^ { \mu \nu } g ^ { \lambda \rho } \big ) \partial _ { \mu \nu } g _ { \lambda \rho } . } } \end{array}
$$

If we now compute $\partial _ { \mu \nu } H ^ { \alpha \mu \beta \nu }$ , at the same point $P$ and in the same coordinate system, we find after straightforward manipulations that it is given by

$$
\begin{array} { c } { { \partial _ { \mu \nu } H ^ { \alpha \mu \beta \nu } \overset { * } { = } ( - g ) \big ( g ^ { \alpha \lambda } g ^ { \beta \mu } g ^ { \nu \rho } + g ^ { \beta \lambda } g ^ { \alpha \mu } g ^ { \nu \rho } - g ^ { \alpha \lambda } g ^ { \beta \rho } g ^ { \mu \nu } - g ^ { \alpha \mu } g ^ { \beta \nu } g ^ { \lambda \rho } } } \\ { { - g ^ { \alpha \beta } g ^ { \mu \lambda } g ^ { \nu \rho } + g ^ { \alpha \beta } g ^ { \mu \nu } g ^ { \lambda \rho } \big ) \partial _ { \mu \nu } g _ { \lambda \rho } . } } \end{array}
$$

To arrive at this result we had to differentiate $( - g )$ using the rule $\partial _ { \mu } ( - g ) = ( - g ) g ^ { \alpha \beta } \partial _ { \mu } g _ { \alpha \beta }$ , which leads to $\partial _ { \mu \nu } ( - g ) \stackrel { * } { = } ( - g ) g ^ { \alpha \beta } \partial _ { \mu \nu } g _ { \alpha \beta }$ . We also had to relate derivatives of the inverse metric to derivatives of the metric itself; here we have used the rule $\partial _ { \mu } g ^ { \alpha \beta } = - g ^ { \alpha \lambda } g ^ { \beta \rho } \partial _ { \mu } g _ { \lambda \rho }$ , which leads to $\partial _ { \mu \nu } g ^ { \alpha \beta } \stackrel { * } { = } - g ^ { \alpha \lambda } g ^ { \beta \rho } \partial _ { \mu \nu } g _ { \lambda \rho }$ .

Our results imply that

$$
\partial _ { \mu \nu } H ^ { \alpha \mu \beta \nu } \overset { * } { = } 2 ( - g ) G ^ { \alpha \beta } .
$$

This is the same as Eq. (6.4), because $( - g ) t _ { \mathrm { L L } } ^ { \alpha \beta } \overset { * } { = } 0$ at $P$ by virtue of the fact that each term in the Landau–Lifshitz pseudotensor is quadratic in $\partial _ { \mu } { \mathfrak { g } } ^ { \alpha \beta }$ , which vanishes at $P$ in the gselected coordinate system. It is therefore plausible that at any other event in spacetime, and in an arbitrary coordinate system, the identity (6.4) should hold, with a pseudotensor $( - g ) t _ { \mathrm { L L } } ^ { \alpha \beta }$ that restores all first-derivative terms that were made to vanish at $P$ in the special coordinate system. To show that this pseudotensor takes the specific form of Eq. (6.5) requires a long computation.

# 6.1.2 Coordinate freedom

The Landau–Lifshitz formulation of general relativity is an exact reformulation of the standard form of the theory. No approximations are involved, and no restrictions are placed on the choice of coordinates. It has to be acknowledged, however, that the usefulness of the formalism is largely limited to situations in which (i) the coordinates $x ^ { \alpha } = ( c t , x ^ { j } )$ are modest deformations of the Lorentzian coordinates of flat spacetime, and (ii) ${ \mathfrak { g } } ^ { \alpha \beta }$ deviates only moderately from the Minkowski metric $\eta ^ { \alpha \beta }$ g. For these situations, which form the context of this book, the formalism is an excellent starting point for a systematic approximation method.

In other contexts the Landau–Lifshitz formulation can be a terrible approach. Even a simple problem such as finding the static, spherically symmetric, vacuum solution to the Einstein field equations, the Schwarzschild metric, which took us about six lines of mathematics back in Sec. 5.6, turns out to be a horrible undertaking in the Landau–Lifshitz approach. The lesson is that while the Landau–Lifshitz formulation of the field equations is mathematically equivalent to the tensorial formulation, it is not equivalent when it comes to the ease of performing calculations. In the post-Minkowskian context it is the preferred formulation; in other contexts it decidedly is not.

Given the practical restriction on the coordinate system, it is useful to observe that the Landau–Lifshitz formulation is manifestly invariant under Lorentz transformations, which we express in the general form

$$
x ^ { \mu ^ { \prime } } = \Lambda _ { \alpha } ^ { \mu ^ { \prime } } x ^ { \alpha } ,
$$

in which the transformation matrix $\Lambda _ { \alpha } ^ { \mu ^ { \prime } }$ is constant and possesses a unit determinant. (In fact, the formalism is invariant under all transformations that are linear in the coordinates, so long as the transformation matrix possesses a unit determinant; this ensures that $g$ is not changed during the transformation. The transformation can also be generalized to include uniform translations, $x ^ { \mu }  x ^ { \mu } + c ^ { \mu }$ , where $c ^ { \mu }$ is a constant vector.) It is easy to show that ${ \mathfrak { g } } ^ { \alpha \beta }$ and its partial derivatives transform as tensors under this class of transformations, and from this observation it follows immediately that all equations of the formalism are invariant under the transformation of Eq. (6.13).

# 6.1.3 Integral conservation identities

Because they involve a partial-derivative operator, the differential identities of Eq. (6.8) can immediately be turned into integral identities. We consider a three-dimensional region $V$ , a fixed (time-independent) domain of the spatial coordinates $x ^ { j }$ , bounded by a twodimensional surface $S$ . We assume that $V$ contains at least some of the matter (so that $T ^ { \alpha \beta }$ is non-zero somewhere within $V$ ), but that $S$ does not intersect any of the matter (so that $T ^ { \alpha \beta } = 0$ everywhere on $S$ ).

# Total momentum and angular momentum: Volume integrals

We formally define a total momentum four-vector $P ^ { \alpha } [ V ]$ associated with the region $V$ by the three-dimensional integral

$$
P ^ { \alpha } [ V ] : = \frac { 1 } { c } \int _ { V } ( - g ) \big ( T ^ { \alpha 0 } + t _ { \mathrm { L L } } ^ { \alpha 0 } \big ) d ^ { 3 } x .
$$

This total momentum includes a contribution from the matter’s momentum density $c ^ { - 1 } T ^ { \alpha 0 }$ , and a contribution from the gravitational field represented by $c ^ { - 1 } t _ { \mathrm { L L } } ^ { \alpha 0 }$ ; the factor of $( - g )$ i s inserted so that we can take advantage of the conservation identities of Eq. (6.8). In flat spacetime and in Lorentzian coordinates, $P ^ { \alpha } [ V ]$ would have a firm interpretation as a total momentum vector associated with the energy-momentum tensor $T ^ { \alpha \beta }$ . In curved spacetime, and in a coordinate system that cannot be assumed to be Lorentzian, the quantity defined by Eq. (6.14) does not have any direct physical meaning. It is, nevertheless, a useful quantity to introduce, as we shall have occasion to recognize.

The momentum four-vector can be decomposed into a time component $P ^ { 0 } [ V ]$ and a spatial three-vector $P ^ { j } [ V ]$ . The time component can be used to define an energy $E [ V ] : =$ $c P ^ { 0 } [ V ]$ associated with the region $V$ . Alternatively, we can define a total mass

$$
M [ V ] : = \frac { 1 } { c ^ { 2 } } \int _ { V } ( - g ) \bigl ( T ^ { 0 0 } + t _ { \mathrm { L L } } ^ { 0 0 } \bigr ) d ^ { 3 } x .
$$

The three-momentum is given by

$$
P ^ { j } [ V ] : = \frac { 1 } { c } \int _ { V } ( - g ) \bigl ( T ^ { j 0 } + t _ { \mathrm { L L } } ^ { j 0 } \bigr ) d ^ { 3 } x .
$$

In a similar way we introduce a total angular-momentum tensor $J ^ { \alpha \beta } [ V ]$ associated with the region $V$ . This is defined by

$$
J ^ { \alpha \beta } [ V ] : = \frac { 1 } { c } \int _ { V } \Bigl [ x ^ { \alpha } ( - g ) \bigl ( T ^ { \beta 0 } + t _ { \mathrm { L L } } ^ { \beta 0 } \bigr ) - x ^ { \beta } ( - g ) \bigl ( T ^ { \alpha 0 } + t _ { \mathrm { L L } } ^ { \alpha 0 } \bigr ) \Bigr ] d ^ { 3 } x ,
$$

and we note that the tensor is antisymmetric in its indices. The interpretation of $J ^ { \alpha \beta } [ V ]$ i s easier to identify once it is decomposed into time and spatial components. The antisymmetry

of the tensor implies that $J ^ { 0 0 } [ V ] = 0$ . The time-space components can be expressed in the form

$$
c ^ { - 1 } J ^ { 0 j } [ V ] = P ^ { j } [ V ] t - M [ V ] R ^ { j } [ V ] ,
$$

where

$$
R ^ { j } [ V ] : = \frac { 1 } { M [ V ] c ^ { 2 } } \int _ { V } ( - g ) \bigl ( T ^ { 0 0 } + t _ { \mathrm { L L } } ^ { 0 0 } \bigr ) x ^ { j } d ^ { 3 } x
$$

represents the position of the center-of-mass of the region $V$ . Equation (6.18) reveals that when $c ^ { - 1 } J ^ { 0 j } [ V ]$ is a constant, it fixes the position of the center-of-mass at $t = 0$ ; when it is not a constant it measures the extent by which the center-of-mass fails to move with a total momentum $P ^ { j } [ V ]$ . The spatial components of the angular-momentum tensor are

$$
J ^ { j k } [ V ] = \frac { 1 } { c } \int _ { V } \Bigl [ x ^ { j } ( - g ) \bigl ( T ^ { k 0 } + t _ { \mathrm { L L } } ^ { k 0 } \bigr ) - x ^ { k } ( - g ) \bigl ( T ^ { j 0 } + t _ { \mathrm { L L } } ^ { j 0 } \bigr ) \Bigr ] d ^ { 3 } x ,
$$

and this is best recognized in its equivalent vectorial form

$$
J ^ { j } [ V ] : = \frac { 1 } { 2 } \epsilon _ { \phantom { } p q } ^ { j } J ^ { p q } [ V ] = \frac { 1 } { c } \int _ { V } \epsilon _ { \phantom { } p q } ^ { j } x ^ { p } \left( - g \right) \left( T ^ { q 0 } + t _ { \mathrm { L L } } ^ { q 0 } \right) d ^ { 3 } x ,
$$

where $\epsilon _ { j p q }$ is the completely antisymmetric permutation symbol. The integrand is the cross product between the position vector $x ^ { p }$ and the momentum density $c ^ { - 1 } ( - g ) ( T ^ { q 0 } + t _ { \mathrm { L L } } ^ { q 0 } )$ within $V$ , and it is natural to interpret the integral as the total angular momentum contained in this region.

# Total momentum and angular momentum: Surface integrals

The total momentum $P ^ { \alpha } [ V ]$ and angular momentum $J ^ { \alpha \beta } [ V ]$ were defined previously in terms of integrals over the three-dimensional region $V$ . It is possible to provide alternative definitions in terms of surface integrals over the two-dimensional surface $S$ that surrounds this region. This is advantageous when the volume integrals of Eq. (6.14) and (6.17) are ill-defined or difficult to compute.

Substituting Eq. (6.6) into Eq. (6.14) gives

$$
P ^ { \alpha } [ V ] = { \frac { c ^ { 3 } } { 1 6 \pi G } } \int _ { V } \partial _ { \mu \nu } H ^ { \alpha \mu 0 \nu } d ^ { 3 } x .
$$

Summation over $\nu$ must exclude $\nu = 0$ , because $H ^ { \alpha \mu 0 0 } = 0$ . We therefore have

$$
P ^ { \alpha } [ V ] = \frac { c ^ { 3 } } { 1 6 \pi G } \int _ { V } \partial _ { k } \bigl ( \partial _ { \mu } H ^ { \alpha \mu 0 k } \bigr ) d ^ { 3 } x ,
$$

and this can be written as a surface integral by invoking Gauss’s theorem. We have

$$
P ^ { \alpha } [ V ] : = { \frac { c ^ { 3 } } { 1 6 \pi G } } \oint _ { S } \partial _ { \mu } H ^ { \alpha \mu 0 k } d S _ { k } ,
$$

where $d S _ { k }$ is an outward-directed surface element on the two-dimensional surface $S$ . Equation (6.22) can be adopted as an alternative definition for the total momentum enclosed

by $S$ ; $H ^ { \alpha \mu 0 k }$ must then be constructed from a solution to Einstein’s equations for the given distribution of matter.

As before the momentum four-vector can be decomposed into time and spatial components. We have that the total mass $M [ V ]$ can be expressed as

$$
M [ V ] : = { \frac { c ^ { 2 } } { 1 6 \pi G } } \oint _ { S } \partial _ { j } H ^ { 0 j 0 k } d S _ { k } ,
$$

and the total three-momentum is

$$
P ^ { j } [ V ] : = \frac { c ^ { 3 } } { 1 6 \pi G } \oint _ { S } \partial _ { n } H ^ { j n 0 k } d S _ { k } - \frac { c ^ { 2 } } { 1 6 \pi G } \frac { d } { d t } \oint _ { S } H ^ { 0 j 0 k } d S _ { k } .
$$

With similar manipulations we arrive at a surface-integral definition for the total angular momentum. One of the two terms that occur within the volume integral when we substitute Eq. (6.6) into Eq. (6.17) is $x ^ { \alpha } \partial _ { k \mu } H ^ { \beta \mu 0 k }$ , which can be expressed as $\partial _ { k } ( x ^ { \alpha } \partial _ { \mu } H ^ { \beta \mu 0 k } ) +$ $\partial _ { \mu } H ^ { \mu \beta 0 \alpha }$ . The first term gives rise to a surface integral, and the second term can be expanded as $\partial _ { 0 } H ^ { 0 \beta 0 \alpha } + \partial _ { k } H ^ { k \beta 0 \alpha }$ ; in this, the first term can be ignored because it is symmetric in $\alpha$ and $\beta$ , and the second term gives rise to another surface integral. Collecting results, we arrive at

$$
J ^ { \alpha \beta } [ V ] : = \frac { c ^ { 3 } } { 1 6 \pi G } \oint _ { S } \left( x ^ { \alpha } \partial _ { \mu } H ^ { \beta \mu 0 k } - x ^ { \beta } \partial _ { \mu } H ^ { \alpha \mu 0 k } + H ^ { 0 \alpha k \beta } - H ^ { 0 \beta k \alpha } \right) d S _ { k } ,
$$

and this can be adopted as an alternative definition for the total angular momentum enclosed by $S$ .

The decomposition of $J ^ { \alpha \beta } [ V ]$ into time and spatial components first returns Eq. (6.18) together with the alternative expression

$$
M [ V ] R ^ { j } [ V ] : = \frac { c ^ { 2 } } { 1 6 \pi G } \oint _ { S } \left( x ^ { j } \partial _ { n } H ^ { 0 n 0 k } - H ^ { 0 j 0 k } \right) d S _ { k }
$$

for the position of the center-of-mass. It also returns

$$
\begin{array} { c } { { J ^ { j k } [ V ] : = \displaystyle \frac { c ^ { 3 } } { 1 6 \pi G } \oint _ { \cal S } \left( x ^ { j } \partial _ { m } H ^ { k m 0 n } - x ^ { k } \partial _ { m } H ^ { j m 0 n } + H ^ { 0 j n k } - H ^ { 0 k n j } \right) d S _ { n } } } \\ { { - \displaystyle \frac { c ^ { 2 } } { 1 6 \pi G } \frac { d } { d t } \oint _ { \cal S } \left( x ^ { j } H ^ { 0 k 0 n } - x ^ { k } H ^ { 0 j 0 n } \right) d S _ { n } } } \end{array}
$$

as an alternative definition for the angular-momentum tensor.

# Conservation statements

To obtain the conservation statements satisfied by $P ^ { \alpha } [ V ]$ and $J ^ { \alpha \beta } [ V ]$ , we differentiate their defining expressions (in terms of volume integrals) with respect to $x ^ { 0 }$ and use the local conservation identity of Eq. (6.8). Starting with Eq. (6.14), we get

$$
\begin{array} { r l r } {  { \frac { d } { d x ^ { 0 } } P ^ { \alpha } [ V ] = \frac { 1 } { c } \int _ { V } \partial _ { 0 } \Big [ ( - g ) \big ( T ^ { \alpha 0 } + t _ { \mathrm { L L } } ^ { \alpha 0 } \big ) \Big ] d ^ { 3 } x } } \\ & { } & { = - \frac { 1 } { c } \int _ { V } \partial _ { k } \Big [ ( - g ) \big ( T ^ { \alpha k } + t _ { \mathrm { L L } } ^ { \alpha k } \big ) \Big ] d ^ { 3 } x . } \end{array}
$$

Converting this to a surface integral, and recalling our previous assumption that $S$ does not intersect the matter distribution, so that $T ^ { \alpha \beta } = 0$ on $S$ , we arrive at

$$
\dot { P } ^ { \alpha } [ V ] = - \oint _ { S } ( - g ) t _ { \mathrm { L L } } ^ { \alpha k } d S _ { k } ,
$$

in which an overdot indicates differentiation with respect to $t : = x ^ { 0 } / c$ . The rate of change of $P ^ { \alpha } [ V ]$ is therefore expressed as a flux integral over $S$ , and the flux is measured by the Landau–Lifshitz pseudotensor (recall the definitions of fluxes provided back in Sec. 4.2). Equation (6.29) gives rise to the individual statements

$$
{ \dot { M } } [ V ] = - { \frac { 1 } { c } } \oint _ { S } ( - g ) t _ { \mathrm { L L } } ^ { 0 k } d S _ { k }
$$

and

$$
{ \dot { P } } ^ { j } [ V ] = - \oint _ { S } ( - g ) t _ { \mathrm { L L } } ^ { j k } d S _ { k }
$$

for the fluxes of mass and momentum three-vector across $S$ .

Proceeding along similar lines for the angular-momentum tensor, we arrive at

$$
{ \dot { J } } ^ { \alpha \beta } [ V ] = - \oint _ { S } \left[ x ^ { \alpha } ( - g ) t _ { \mathrm { { L L } } } ^ { \beta k } - x ^ { \beta } ( - g ) t _ { \mathrm { { L L } } } ^ { \alpha k } \right] d S _ { k } .
$$

The symmetry of $t _ { \mathrm { L L } } ^ { \alpha \beta }$ was essential in obtaining this result. When decomposed into time and spatial components, the statement becomes

$$
c ^ { - 1 } { \dot { J } } ^ { 0 j } [ V ] = { \dot { P } } ^ { j } [ V ] t + { \frac { 1 } { c } } \oint _ { S } x ^ { j } ( - g ) t _ { \mathrm { { L L } } } ^ { 0 k } d S _ { k }
$$

and

$$
{ \dot { J } } ^ { j k } [ V ] = - \oint _ { S } \left[ x ^ { j } ( - g ) t _ { \mathrm { L L } } ^ { k n } - x ^ { k } ( - g ) t _ { \mathrm { L L } } ^ { j n } \right] d S _ { n } .
$$

Equation (6.33), when combined with Eq. (6.18), implies that

$$
{ \frac { d } { d t } } { \big ( } M [ V ] R ^ { j } [ V ] { \big ) } = P ^ { j } [ V ] - { \frac { 1 } { c } } \oint _ { S } x ^ { j } ( - g ) t _ { \mathrm { { L L } } } ^ { 0 k } d S _ { k } .
$$

# 6.1.4 Total mass, momentum, and angular momentum

The limit in which $V$ is taken to include all of three-dimensional space is particularly interesting. In this limit $P ^ { \alpha } [ V ]$ is known to coincide with the Arnowitt–Deser–Misner four-momentum of an asymptotically-flat spacetime, and its physical interpretation as a measure of total momentum is robust. This statement is true whenever the coordinates $x ^ { \alpha }$ coincide with a Lorentzian system at infinity; the coordinates do not have to be Lorentzian (and indeed, they could not be) at finite spatial distances.

Recalling the definitions of Eqs. (6.15) and (6.23), we define the total mass of the spacetime as

$$
\begin{array} { c } { { M : = \displaystyle \frac { 1 } { c ^ { 2 } } \int _ { \mathrm { a l l s p a c e } } ( - g ) \big ( T ^ { 0 0 } + t _ { \mathrm { L L } } ^ { 0 0 } \big ) d ^ { 3 } x } } \\ { { : = \displaystyle \frac { c ^ { 2 } } { 1 6 \pi G } \oint _ { \infty } \partial _ { j } H ^ { 0 j 0 k } d S _ { k } . } } \end{array}
$$

Recalling the definitions of Eqs. (6.16) and (6.24), we define the total three-momentum of the spacetime as

$$
\begin{array} { r l } & { P ^ { j } : = \cfrac { 1 } { c } \int _ { \mathrm { a l l s p a c e } } ( - g ) \big ( T ^ { j 0 } + t _ { \mathrm { L L } } ^ { j 0 } \big ) d ^ { 3 } x } \\ & { \mathrel { \mathop : } = \cfrac { c ^ { 3 } } { 1 6 \pi G } \oint _ { \infty } \partial _ { n } H ^ { j n 0 k } d S _ { k } - \cfrac { c ^ { 2 } } { 1 6 \pi G } \cfrac { d } { d t } \oint _ { \infty } H ^ { 0 j 0 k } d S _ { k } . } \end{array}
$$

Recalling the definitions of Eqs. (6.20) and (6.27), we define the total angular-momentum three-tensor of the spacetime as

$$
\begin{array} { r l } {  { J ^ { j k } : = \frac { 1 } { c } \int _ { \mathrm { a l l s p a c e } } \biggl [ x ^ { j } ( - g ) \bigl ( T ^ { k 0 } + t _ { \mathrm { L L } } ^ { k 0 } \bigr ) - x ^ { k } ( - g ) \bigl ( T ^ { j 0 } + t _ { \mathrm { L L } } ^ { j 0 } \bigr ) \biggr ] d ^ { 3 } x } } \\ &  \mathrel { \phantom { = } } \\ & { \phantom { = } \operatorname* { \frac { c ^ { 3 } } { 3 } } \qquad \quad \int _ { \infty } ^ { 3 } \biggl \{ \int _ { \infty } ^ { j } \bigl ( x ^ { j } \partial _ { m } H ^ { k m 0 n } - x ^ { k } \partial _ { m } H ^ { j m 0 n } + H ^ { 0 j n k } - H ^ { 0 k n j } \bigr ) d S _ { n } } \\ & { \qquad \quad - \frac { c ^ { 2 } } { 1 6 \pi G } \frac { d } { d t } \oint _ { \infty } \bigl ( x ^ { j } H ^ { 0 k 0 n } - x ^ { k } H ^ { 0 j 0 n } \bigr ) d S _ { n } . } \end{array}
$$

And finally, recalling Eqs. (6.19) and (6.26), we define

$$
\begin{array} { l } { { \displaystyle R ^ { j } : = \frac { 1 } { M c ^ { 2 } } \int _ { \mathrm { a l l ~ s p a c e } } \bigl ( T ^ { 0 0 } + t _ { \mathrm { L L } } ^ { 0 0 } \bigr ) x ^ { j } d ^ { 3 } x } } \\ { { \displaystyle : = \frac { c ^ { 2 } } { 1 6 \pi G M } \oint _ { \infty } \left( x ^ { j } \partial _ { n } H ^ { 0 n 0 k } - H ^ { 0 j 0 k } \right) d S _ { k } } } \end{array}
$$

as the position of the center-of-mass for the entire spacetime. The mass, momentum, angular momentum, and center-of-mass position of a spacetime can be defined either in terms of volume integrals over all space, or in terms of surface integrals at infinity. The surface integrals are especially powerful because they allow us to determine these quantities directly from the asymptotic behavior of the metric at large distances; an intimate knowledge of the material source is not required. This is reminiscent of the situation in electrodynamics: the total electric charge can be determined by integrating the normal component of the electric field over a surface enclosing the charge, and nothing need be known of the detailed distribution of charge within the surface.

Equations (6.30), (6.31), and (6.34) imply that the total mass $M$ , total momentum $P ^ { j }$ , and total angular momentum $J ^ { j k }$ are constant in time whenever the surface integrals vanish in the limit $S \to \infty$ . Under these circumstances, we have the conservation statements

$$
M = { \mathrm { c o n s t a n t } } , \qquad P ^ { j } = { \mathrm { c o n s t a n t } } , \qquad J ^ { j k } = { \mathrm { c o n s t a n t } } .
$$

Furthermore, it can be shown that whenever the surface integrals vanish, the volume integrals of Eqs. (6.14) and (6.17) can be evaluated on any spacelike hypersurface and produce the same result. In particular, the momentum four-vector can be evaluated on a surface of simultaneity $t ^ { \prime } =$ constant that is obtained from the original surface $t =$ constant by a Lorentz transformation; this observation can be used to show that $P ^ { \alpha }$ transforms as a four-vector under the transformation of Eq. (6.13).

In a similar way, Eq. (6.35) implies that $M { \dot { R } } ^ { j } = P ^ { j }$ whenever its surface integral vanishes, and whenever $M$ itself is a constant. Assuming that $P$ also is constant, we have

$$
M { \pmb R } ( t ) = M { \pmb R } ( 0 ) + { \pmb P } t ,
$$

where $\pmb { R } ( 0 )$ is the position of the center-of-mass at $t = 0$ . This equation states that the center-of-mass moves uniformly with a velocity $P / M$ (recall that $M = P ^ { 0 } / c$ ) .

When Eq. (6.40) holds it is natural to adopt a reference frame in which $P$ vanishes. This can always be achieved by performing a Lorentz transformation described by Eq. (6.13) and directing the boost in the direction of the momentum; the boost parameter must be set equal to $v = | \pmb { P } | / M$ . Once this is accomplished, it is also natural to place the origin of the spatial coordinates at the center-of-mass $\pmb { R }$ . This can always be achieved by translating the coordinates according to $x \to x - c$ , with $c$ denoting a constant vector. It is easy to see that the translation changes the position of the center-of-mass according to $\pmb { R }  \pmb { R } - \pmb { c }$ , and choosing $c = R$ places the center-of-mass at the origin of the spatial coordinates.

These choices define the center-of-mass frame of the spacetime:

$$
\mathrm { c e n t e r - o f - m a s s ~ f r a m e : } \qquad { \cal P } ^ { j } = 0 , \qquad { \cal R } ^ { j } = 0 .
$$

As we have seen, this choice can be made whenever $P$ is a constant vector, and whenever $M { \dot { R } } = P$ . These conditions are fulfilled whenever the surface integrals of Eqs. (6.31) and (6.35) vanish when $S \to \infty$ . This always happens when the spacetime is stationary. In the context of a radiating spacetime, however, the surface integrals cannot be assumed to vanish; in fact, the mass, momentum, and angular momentum of the spacetime are typically seen to change with time because the radiation transports energy, momentum, and angular momentum away from the source. Fortunately this effect can often be neglected in the context of approximate calculations.

We conclude this discussion with an illustration: We use the surface integrals to calculate the mass, momentum, and angular momentum of the Schwarzschild spacetime, first encountered back in Sec. 5.6. Expressing the metric of Eq. (5.163) in Cartesian coordinates, we find that

$$
\begin{array} { l } { { g _ { 0 0 } = - \left( 1 - \displaystyle \frac { R } { r } \right) \ : , } } \\ { { g _ { j k } = \delta _ { j k } + \left( 1 - \displaystyle \frac { R } { r } \right) ^ { - 1 } \displaystyle \frac { R } { r } n _ { j } n _ { k } \ : , } } \end{array}
$$

where $R : = 2 G M / c ^ { 2 }$ and $n ^ { j } : = x ^ { j } / r$ . It is then simple to show that $g = - 1$ and

$$
\begin{array} { l } { { \displaystyle { \mathfrak { g } } ^ { 0 0 } = - \left( 1 - \frac { R } { r } \right) ^ { - 1 } , } } \\ { { \displaystyle { \mathfrak { g } } ^ { j k } = \delta ^ { j k } - \frac { R } { r } n ^ { j } n ^ { k } . } } \end{array}
$$

We next compute $H ^ { \alpha \mu 0 j }$ by substituting Eqs. (6.44) into Eq. (6.2), and insert the result within Eq. (6.22) to calculate $P ^ { \alpha } [ r ]$ , the momentum vector associated with a surface $S$ of constant $r$ . The computations involve the surface element $d S _ { j } = r ^ { 2 } n _ { j } d \Omega$ (where $d \Omega : = \sin \theta$ dθdφ is an element of solid angle), and they lead to $P ^ { j } [ r ] = 0$ and

$$
M [ r ] = M \frac { r } { r - 2 G M / c ^ { 2 } } .
$$

The spatial momentum vanishes (as expected, since the coordinates are centered on the black hole), and in the limit $r  \infty$ our previous result reduces to

$$
M [ \infty ] = M .
$$

The total energy is $c P ^ { 0 } [ \infty ] = M c ^ { 2 }$ , and $M$ is recognized as the total gravitational mass of the Schwarzschild spacetime. A similar calculation reveals that the center-of-mass is situated at $R ^ { j } = 0$ and that the angular momentum vanishes.

# 6.2 Relaxed Einstein equations

# 6.2.1 Harmonic coordinates and a wave equation

It is advantageous at this stage to impose the four conditions

$$
\partial _ { \beta } { \mathfrak { g } } ^ { \alpha \beta } = 0
$$

on the gothic inverse metric. These are known as the harmonic coordinate conditions, and they were first encountered back in Sec. 5.6 (see Eq. (5.177)) in the context of the Schwarzschild solution. It is also useful to introduce the potentials

$$
h ^ { \alpha \beta } : = \eta ^ { \alpha \beta } - \mathfrak { g } ^ { \alpha \beta } ,
$$

where $\eta ^ { \alpha \beta } : = \mathrm { d i a g } ( - 1 , 1 , 1 , 1 )$ is the Minkowski metric expressed in Lorentzian coordinates $( x ^ { 0 } : = c t , x ^ { j } )$ . In terms of these potentials the harmonic coordinate conditions read

$$
\partial _ { \beta } h ^ { \alpha \beta } = 0 ,
$$

and in this context they are usually referred to as the harmonic gauge conditions. We observe that the harmonic conditions are preserved under the Lorentz transformations of

Eq. (6.13), and that the potentials $h ^ { \alpha \beta }$ transform as a tensor under this restricted class of coordinate transformations.

<table><tr><td>Box 6.2</td><td>Existence of harmonic coordinates</td></tr><tr><td></td><td>It seems plausible that the four harmonic coordinate conditions of Eq. (6.47)can always be imposed, given thefourdegrees ofcoordinate freedom inherent to general relativity,butitis worthwhile toseethis explicitly. Given an initial coordinate system in which δβ gαβ / O, we make a coordinate transformation to x&#x27; = fμ(xα).Itis then straightforward to show that in the new coordinates</td></tr><tr><td></td><td>vgμ&#x27;v&#x27;=√-g&#x27;△gf²(xα），</td></tr><tr><td>gfl= O,ensures thatthe harmonic coordinate conditions will hold in the new coordinates.</td><td>where g := g/v VμV, is the curved spacetime d&#x27;Alembertian operator acting on each one of the four functions fμ,treated as a scalar function of xα.Choosing each function tobe harmonic,thatis,asolution to</td></tr></table>

The introduction of the potentials $h ^ { \alpha \beta }$ and the imposition of the harmonic gauge conditions simplify the appearance of the Einstein field equations. It is easy to verify that the left-hand side becomes

$$
\partial _ { \mu \nu } H ^ { \alpha \mu \beta \nu } = - \Omega h ^ { \alpha \beta } + h ^ { \mu \nu } \partial _ { \mu \nu } h ^ { \alpha \beta } - \partial _ { \mu } h ^ { \alpha \nu } \partial _ { \nu } h ^ { \beta \mu } ,
$$

where $\begin{array} { r } { \ d \Pi : = \eta ^ { \mu \nu } \partial _ { \mu \nu } } \end{array}$ is the flat-spacetime wave operator. The right-hand side of the field equations stays essentially unchanged, but the harmonic conditions do slightly simplify the form of the Landau–Lifshitz pseudotensor; as can be seen from Eq. (6.5), the first two terms of $( - g ) t _ { \mathrm { L L } } ^ { \alpha \beta }$ vanish in harmonic coordinates. Isolating the wave operator on the left-hand side, and putting everything else on the right-hand side, gives us the formal wave equation

$$
\boxed { 1 } h ^ { \alpha \beta } = - \frac { 1 6 \pi G } { c ^ { 4 } } \tau ^ { \alpha \beta }
$$

for the potentials $h ^ { \alpha \beta }$ , where

$$
\tau ^ { \alpha \beta } : = ( - g ) \big ( T ^ { \alpha \beta } [ \mathsf { m } , g ] + t _ { \mathrm { L L } } ^ { \alpha \beta } [ h ] + t _ { \mathrm { H } } ^ { \alpha \beta } [ h ] \big )
$$

is the effective energy-momentum pseudotensor for the wave equation. We have introduced

$$
( - g ) t _ { \mathrm { H } } ^ { \alpha \beta } : = \frac { c ^ { 4 } } { 1 6 \pi G } \Big ( \partial _ { \mu } h ^ { \alpha \nu } \partial _ { \nu } h ^ { \beta \mu } - h ^ { \mu \nu } \partial _ { \mu \nu } h ^ { \alpha \beta } \Big )
$$

as an additional (harmonic-gauge) contribution to the effective energy-momentum pseudotensor.

In our expression for $\tau ^ { \alpha \beta }$ we have indicated that the energy-momentum tensor $T ^ { \alpha \beta }$ is a functional of matter variables $\mathsf { m }$ , in addition to being a functional of the metric tensor $g _ { \alpha \beta }$ (which is obtained from the gravitational potentials). As an example, when the matter consists of a perfect fluid, $\mathsf { m }$ collectively denotes variables such as the mass density $\rho$ , pressure $p$ , and velocity field $u ^ { \alpha }$ . We have also indicated that the Landau–Lifshitz and harmonic pseudotensors are functionals of $h ^ { \alpha \beta }$ . As we shall see below, imposition of the gauge conditions (6.49) is equivalent to enforcing the conservation equations

$$
\partial _ { \beta } \tau ^ { \alpha \beta } = 0 ,
$$

which can be compared with Eq. (6.8). It is easy to verify that $( - g ) t _ { \mathrm { H } } ^ { \alpha \beta }$ is separately conserved, in that it satisfies $\partial _ { \beta } [ ( - g ) t _ { \mathrm { H } } ^ { \alpha \beta } ] = 0$ as an identity.

The wave equation of Eq. (6.51) is the main starting point of post-Minkowskian theory. It is worth emphasizing the fact that this equation, together with Eq. (6.49) or (6.54), is an exact formulation of the Einstein field equations; no approximations have been introduced at this stage.

For a metric $g _ { \alpha \beta }$ to satisfy the complete set of Einstein field equations, it is necessary for the potentials $h ^ { \alpha \beta }$ to satisfy both the wave equation and the gauge condition/conservation statement; it is the union of Eq. (6.51) and (6.49) or (6.54) that is equivalent to the original form of the Einstein field equations, $G ^ { \alpha \beta } = ( 8 \pi G / c ^ { 4 } ) T ^ { \alpha \beta }$ . The two sets of equations play different roles. The wave equation (6.51) determines the gravitational potentials $h ^ { \alpha \beta } [ \mathsf { m } ]$ (and therefore the metric) as functions of the harmonic coordinates $x ^ { \alpha }$ , in terms of the matter variables $\mathsf { m }$ ; these, however, remain undetermined until we also involve the conservation equation (6.54). It is this equation that determines the behavior of the matter variables in a curved spacetime whose metric is built from $h ^ { \alpha \beta } [ \mathsf { m } ]$ . Solving both sets of equations therefore determines both the metric and the matter variables. This reminds us of John Wheeler’s famous words: matter tells spacetime how to curve, and spacetime tells matter how to move; the decomposition of the field equations into a wave equation and a gauge condition/conservation statement provides a mathematical representation of this maxim.

We have just seen that when the complete set of Einstein field equations is integrated, one cannot solve for the metric independently of the matter variables, and one cannot solve for the matter variables independently of the metric. It is useful to observe, however, that when the equations are decomposed into the subsets [wave equation] and [gauge condition/ conservation statement], one is entirely free to solve the wave equation (6.51) without also enforcing the gauge condition of Eq. (6.49) or the conservation statement of Eq. (6.54). Solving the wave equation independently of the gauge condition/conservation statement amounts to integrating only a subset of the Einstein field equations, and the procedure returns ten gravitational potentials $h ^ { \alpha \beta } [ \mathsf { m } ]$ expressed as functionals of undetermined matter variables m. The metric obtained from these potentials is also a functional of m, and it is not yet a solution to the Einstein field equations; it becomes a solution only when the gauge condition/conservation statement is imposed as an additional condition on the matter variables. The wave equation (6.51), taken by itself independently of Eqs. (6.49) or (6.54), is known as the relaxed Einstein field equation.

<table><tr><td>Box 6.3</td><td>Wave equation in flat and curved spacetimes</td></tr><tr><td></td><td>Because it involves second derivatives of the potentials,the term hμv dμvh&amp;β on the right-hand side of the</td></tr><tr><td></td><td>field equations might have been more appropriately placed on theleft-hand side,andjoined together with the</td></tr><tr><td></td><td> wave-operator term.In fact, there is a way of combining allsecond-order derivatives into a curved-spacetime</td></tr><tr><td></td><td> wave operator. For this purpose we treat hαβ as a collection of ten scalar felds instead ofas a tensor field.</td></tr></table>

The scalar wave operator associated with the metric $g _ { \alpha \beta }$ (which is to be constructed from the potentials) is denoted $\boxed { \begin{array} { r l } \end{array} } _ { g } ,$ , and it has the following action on each of the ten potentials:

$$
\begin{array} { l } { { \displaystyle \bigtriangledown _ { g } h ^ { \alpha \beta } = \frac { 1 } { \sqrt { - g } } \partial _ { \mu } \big ( \sqrt { - g } g ^ { \mu \nu } \partial _ { \nu } h ^ { \alpha \beta } \big ) } } \\ { { \displaystyle \qquad = \frac { 1 } { \sqrt { - g } } \partial _ { \mu } \Big [ \big ( \eta ^ { \mu \nu } - h ^ { \mu \nu } \big ) \partial _ { \nu } h ^ { \alpha \beta } \Big ] } } \\ { { \displaystyle \qquad = \frac { 1 } { \sqrt { - g } } \Big [ \bigtriangledown h ^ { \alpha \beta } - h ^ { \mu \nu } \partial _ { \mu \nu } h ^ { \alpha \beta } \Big ] , } } \end{array}
$$

where we have used the harmonic gauge conditions in the last step. This expression does indeed involve all second-derivative terms that appear in Eq. (6.51). The field equations could then be formulated in terms of $\boxed { \begin{array} { r l } \end{array} } _ { g } ,$ , and this was, in fact, the approach adopted by Kovacs and Thorne in their series of papers on the generation of gravitational waves. This approach, while conceptually compelling, is not as immediately useful for post-Minkowskian theory as the approach adopted here, which is based on the Minkowski wave operator. It is indeed much simpler to solve the wave equation in flat spacetime than it is to solve it in a curved spacetime with a complicated (and as yet unknown) metric.

# 6.2.2 Formal solution to the wave equation

The wave equation of Eq. (6.51) admits the formal solution

$$
h ^ { \alpha \beta } ( x ) = \frac { 4 G } { c ^ { 4 } } \int G ( x , x ^ { \prime } ) \tau ^ { \alpha \beta } ( x ^ { \prime } ) d ^ { 4 } x ^ { \prime } ,
$$

where $\boldsymbol { x } = \left( c t , \boldsymbol { x } \right)$ is a field point and $x ^ { \prime } = ( c t ^ { \prime } , x ^ { \prime } )$ a source point. The two-point function $G ( x , x ^ { \prime } )$ is the retarded Green’s function of the Minkowski wave operator, which satisfies

$$
\begin{array} { r } { \boxed { \ d \Pi } G ( x , x ^ { \prime } ) = - 4 \pi \delta ( x - x ^ { \prime } ) , } \end{array}
$$

and which is known to be a function of $x - x ^ { \prime }$ only. (An explicit expression will be presented in Sec. 6.3.) This property is sufficient to prove that if the effective energy-momentum pseudotensor $\tau ^ { \alpha \beta }$ satisfies the conservation identities of Eq. (6.54), then the potentials $h ^ { \alpha \beta }$ will satisfy the harmonic gauge conditions of Eq. (6.49). The converse property, that $\partial _ { \beta } \tau ^ { \alpha \beta } = 0$ when $\partial _ { \beta } h ^ { \alpha \beta } = 0$ , follows immediately from the wave equation (6.51).

To prove that $\partial _ { \beta } h ^ { \alpha \beta } = 0$ when $\partial _ { \beta } \tau ^ { \alpha \beta } = 0$ , we begin by differentiating Eq. (6.56) with respect to $x ^ { \beta }$ :

$$
\partial _ { \beta } h ^ { \alpha \beta } = \frac { 4 G } { c ^ { 4 } } \int \partial _ { \beta } G ( x , x ^ { \prime } ) \tau ^ { \alpha \beta } ( x ^ { \prime } ) d ^ { 4 } x ^ { \prime } .
$$

Using the previously mentioned property that $G ( x , x ^ { \prime } )$ depends on $x - x ^ { \prime }$ only, we may write this as

$$
\partial _ { \beta } h ^ { \alpha \beta } = \frac { 4 G } { c ^ { 4 } } \int \left[ - \partial _ { \beta ^ { \prime } } G ( x , x ^ { \prime } ) \right] \tau ^ { \alpha \beta } ( x ^ { \prime } ) d ^ { 4 } x ^ { \prime } ,
$$

in which the Green’s function is now differentiated with respect to $x ^ { \prime \beta }$ . Integrating by parts, we arrive at

$$
\partial _ { \beta } h ^ { \alpha \beta } = \frac { 4 G } { c ^ { 4 } } \int G ( x , x ^ { \prime } ) \partial _ { \beta ^ { \prime } } \tau ^ { \alpha \beta } ( x ^ { \prime } ) d ^ { 4 } x ^ { \prime } .
$$

This equation reveals directly that $h ^ { \alpha \beta }$ satisfies the harmonic gauge conditions when $\tau ^ { \alpha \beta }$ is conserved.

# 6.2.3 Iteration of the relaxed field equations

The question that concerns us now is this: Given the complexity of Eqs. (6.51)–(6.54), how can we construct solutions for a particular choice of matter variables $\mathsf { m } ?$ Our answer will be: by successive approximations. We shall not attempt to find exact solutions to our equations; instead, we shall retreat to an approximate context in which our spacetime deviates only moderately from Minkowski spacetime. To construct the metric of this spacetime we consider a formal expansion of the form

$$
h ^ { \alpha \beta } = G k _ { 1 } ^ { \alpha \beta } + G ^ { 2 } k _ { 2 } ^ { \alpha \beta } + G ^ { 3 } k _ { 3 } ^ { \alpha \beta } + \cdot \cdot \cdot .
$$

for the gravitational potentials. Such an expansion in powers of $G$ is known as a post-Minkowskian expansion, and our hope is that the expansion – an asymptotic expansion that is not expected to converge – will give rise to an acceptable approximation to the true metric, at least in a useful portion of the spacetime. In the mathematical language of asymptotic expansions, our hope is that $g _ { \alpha \beta } ( x ) - g _ { \alpha \beta } ^ { n } ( x ) = O ( G ^ { n + 1 } )$ when $x$ is within a wide domain $\boldsymbol { \mathcal U }$ of the spacetime manifold; here $g _ { \alpha \beta } ^ { n }$ is the metric obtained from Eq. (6.61) after truncating the asymptotic series to order $G ^ { n }$ . Equation (6.61) gives rise to the successive approximations $h _ { 0 } ^ { \alpha \beta } = 0$ , $h _ { 1 } ^ { \alpha \beta } = G k _ { 1 } ^ { \alpha \beta }$ , $h _ { 2 } ^ { \alpha \beta } = G k _ { 1 } ^ { \alpha \beta } + G ^ { 2 } k _ { 2 } ^ { \alpha \beta }$ , and so on, for the gravitational potentials.

<table><tr><td>Box 6.4</td><td>The expansion parameter G</td></tr><tr><td></td><td>This development in powers of G is a formal device only. Because G has dimensions, its numerical value depends on the units in which it is evaluated,anditseems ridiculous to letit play the role ofa&quot;smal&quot; expan- sion parameter. For example, we were raised in geometrized units in which G = 1,and this does not look like asmal quantity. The actual expansion parameter in a typical situation involving a characteristic mass mc confinedtoaregionofcharacteristicsizerc is Gmc/(c2rc),whichissmallnsituationsinvolvingweak grav- itational fields. Because the proper specification of the expansion parameter requires additional information that is specific to each situation considered,it is economicalto stick with Gasaformal expansion parameter, and let each physical situation dictate the translation to a meaningful, dimensionlessparameter.The absence of aunique,dimensionless expansion parameter for the Einstein field equations is part of the reason why the expansions of post-Minkowskian and post-Newtonian theory are believed to be asymptotic sequences that may not converge.</td></tr></table>

In principle we might begin the process of solving the Einstein field equations by substituting Eq. (6.61) into Eq. (6.51) and plucking out terms that share the same power of $G$ . In practice, however, it is more convenient to proceed by iterations, as we now explain.

In the zeroth iteration of the relaxed field equations we set $h _ { 0 } ^ { \alpha \beta } = 0$ and immediately get $g _ { \alpha \beta } ^ { 0 } = \eta _ { \alpha \beta }$ , the metric of Minkowski spacetime. From this we construct $T ^ { \alpha \beta } [ \mathsf { m } , g ] =$ $T ^ { \alpha \beta } [ \mathsf { \ddot { m } } , \eta ] , t _ { \mathrm { L L } } ^ { \dot { \alpha } \beta } [ h ] = t _ { \mathrm { L L } } ^ { \alpha \beta } [ h _ { 0 } ] = 0$ , and $t _ { \mathrm { H } } ^ { \alpha \beta } [ h ] = t _ { \mathrm { H } } ^ { \alpha \beta } [ h _ { 0 } ] = 0$ . From all this we obtain $\tau _ { 0 } ^ { \alpha \beta } =$ $T ^ { \alpha \beta } [ \mathsf { m } , \eta ]$ ; this is the energy-momentum tensor of the matter variables $\mathsf { m }$ , and in the zeroth iteration these live in Minkowski spacetime.

In the first iteration of the relaxed field equations we solve the wave equation $\Pi h ^ { \alpha \beta } = - ( 1 6 \pi G / c ^ { 4 } ) \tau _ { 0 } ^ { \alpha \beta }$ for $h _ { 1 } ^ { \alpha \beta } = G k _ { 1 } ^ { \alpha \beta }$ . Because the source $\tau _ { 0 } ^ { \alpha \beta }$ is known from the zeroth iteration, the wave equation can be integrated without difficulty (at least in principle), and this returns the potentials $h _ { 1 } ^ { \alpha \beta }$ as functionals of the matter variables $\mathsf { m }$ , which have yet to be determined. From the potentials we form the metric $g _ { \alpha \beta } ^ { 1 }$ and construct $\tau _ { 1 } ^ { \alpha \beta }$ αβ , an improved version of the effective energy-momentum pseudotensor. This involves the material contribution $T ^ { \alpha \beta } [ \mathsf { m } , g _ { 1 } ]$ , as well as the field contributions $t _ { \mathrm { L L } } ^ { \alpha \beta } [ h _ { 1 } ]$ and $t _ { \mathrm { H } } ^ { \alpha \beta } [ h _ { 1 } ]$ .

In the second iteration of the relaxed field equations we solve the wave equation $\Pi h ^ { \alpha \beta } = - ( 1 6 \pi G / c ^ { 4 } ) \tau _ { 1 } ^ { \alpha \beta }$ for $h _ { 2 } ^ { \alpha \beta } = { \cal G } k _ { 1 } ^ { \alpha \beta } + { \cal G } ^ { 2 } k _ { 2 } ^ { \alpha \bar { \beta } }$ , an improved version of the gravita-1 2 1 tional potentials. Because the source τ αβ1 i s known from the first iteration, the wave equation can once more be integrated, and $h _ { 2 } ^ { \bar { \alpha } \beta }$ are again functionals of the undetermined matter variables m. From the new potentials we form the metric $g _ { \alpha \beta } ^ { 2 }$ and construct $\tau _ { 2 } ^ { \alpha \beta }$ , the latest version of the effective energy-momentum pseudotensor. The stage is ready for the next iteration.

After $n$ iterations we obtain the potentials $h _ { n } ^ { \alpha \beta } = G k _ { 1 } ^ { \alpha \beta } + G ^ { 2 } k _ { 2 } ^ { \alpha \beta } + \cdot \cdot \cdot + G ^ { n } k _ { n } ^ { \alpha \beta }$ , the nth post-Minkowskian approximation to the true potentials $h ^ { \alpha \beta }$ . These functions of the harmonic coordinates $x ^ { \alpha }$ are functionals of the matter variables $\mathsf { m }$ , which must now be determined. This is accomplished in the very last step of the procedure, the implementation of the gauge condition/conservation statement, which has not yet been invoked. We thus impose $\partial _ { \beta } h _ { n } ^ { \alpha \beta } = 0$ on our iterated solution to the relaxed field equations; this determines $\mathsf { m }$ and returns e conservati $g _ { \alpha \beta } ^ { n } ( x )$ as aation or field in spacetime. Equivalently, we may enforce, which (as we have seen) is formally equivalent to $\partial _ { \beta } \tau _ { n - 1 } ^ { \alpha \beta } = 0$ $\partial _ { \beta } h _ { n } ^ { \alpha \beta } = 0$ . It is important to observe that while the gauge condition involves , the conservation statement involves $\tau _ { n - 1 } ^ { \alpha \beta }$ ; these quantities are linked by the iteration procedure described previously.

Let us illustrate the foregoing discussion by choosing the matter content of the spacetime to consist of $N$ point masses labeled by an index $A = ( 1 , 2 , \ldots , N )$ . In this case the collective matter variables $\mathsf { m }$ denote the set of vectors $\pmb { r } _ { A } ( t )$ , which give the position of each body in the harmonic system of coordinates. After $n$ iterations of the relaxed field equations we obtain gravitational potentials of the form $h _ { n } ^ { \alpha \beta } ( x ^ { \alpha } ; r _ { A } )$ ; these are functions of the spacetime coordinates $x ^ { \alpha }$ and functionals of the trajectories $\pmb { r } _ { A } ( t )$ . At this stage of the procedure the trajectories are not determined; the functions $\pmb { r } _ { A } ( t )$ are completely arbitrary. In the final step we enforce the conservation equation $\partial _ { \beta } \tau _ { n - 1 } ^ { \alpha \beta } = 0$ , and this produces equations

of motion of the form

$$
\frac { d ^ { 2 } { \pmb r } _ { A } } { d t ^ { 2 } } = O ( G ) + O ( G ^ { 2 } ) + \cdots + O ( G ^ { n - 1 } ) .
$$

These are used to determine $\pmb { r } _ { A } ( t )$ , and the task is completed: we have the metric and the motion of the individual bodies. These considerations indicate that two iterations of the relaxed field equations are required to obtain the Newtonian equations of motion – the $O ( G )$ term on the right-hand side of Eq. (6.62).

It is important to understand that the iterations must be performed on the relaxed equations only, and not on the full set of Einstein field equations. In other words, one iterates the wave equation only, and leaves the gauge condition/conservation statement alone, until the final iteration is carried out; the gauge condition/conservation statement is enforced in the very last step of the procedure. It would indeed be misguided to enforce it at every iterative step. To see why, imagine that we choose to enforce $\partial _ { \beta } \tau ^ { \alpha \beta } = 0$ immediately at the zeroth iteration. Because τ α $\tau _ { 0 } ^ { \alpha \beta } = T ^ { \alpha \beta } [ \mathsf { m } , \eta ]$ , this is the conservation equation for matter fields in Minkowski spacetime, and it implies that the matter cannot be subjected to gravitational interactions. (In the illustrative case of point masses examined previously, the bodies would have to move on straight lines.) The next iteration would produce $h _ { 1 } ^ { \alpha \beta }$ as sourced by this matter field, and the next version of the conservation statement, $\partial _ { \beta } \tau _ { 1 } ^ { \alpha \beta } = 0$ , would imply that the matter is, after all, subjected to a gravitational interaction. (In our example, the point masses would now be allowed to move according to the Newtonian equations of motion, in a gravitational field determined as if the masses were moving on straight lines.) We have a contradiction, and this tension is best avoided by delaying the implementation of the gauge condition/conservation statement until the very last step of the iterative procedure.

As a small technical point, we might mention that the procedure does retain a limited amount of latitude. As dsolve the wave equation $\begin{array} { r } { \boxed { - 1 } h ^ { \alpha \beta } = - ( 1 6 \pi G / c ^ { 4 } ) \tau _ { n - 1 } ^ { \alpha \beta } } \end{array}$ matefor $h _ { n } ^ { \alpha \beta }$ p in the iterative procedur, given the known source $\tau _ { n - 1 } ^ { \alpha \beta }$ The l ep is to impose the a nal co $\partial _ { \beta } \tau _ { n - 1 } ^ { \alpha \beta } = 0$ . These steps can be switched: once τ αβn−1 $h _ { n - 1 } ^ { \alpha \beta }$ $( n - 1 ) \mathrm { t h }$ the conservation equation $\partial _ { \beta } \tau _ { n - 1 } ^ { \alpha \beta } = 0$ . The final step is then to obtain $h _ { n } ^ { \alpha \beta }$ by integrating the wave equation, and the gauge condition $\partial _ { \beta } h _ { n } ^ { \alpha \beta } = 0$ will automatically be satisfied by the solution.

We can be even more flexible. If we are interested only in the equations of motion that arise from the $( n - 1 ) \operatorname { t h }$ iteration, and not in the spacetime metric that is generated by that motion, then we do not actually have to complete the iterations to obtain $h _ { n } ^ { \alpha \beta }$ . The solutions $h _ { n - 1 } ^ { \alpha \beta }$ are sufficient to insert into the conservation equations $\partial _ { \beta } \tau _ { n - 1 } ^ { \alpha \beta } = 0$ , from which the motion of the system can be determined consistently to order $G ^ { n - 1 }$ .

The iterative, post-Minkowskian method described in this section is technically demanding to carry out, and in the next chapter we shall develop a number of helpful techniques that permit its successful implementation. Before we start, however, we must learn how to solve a wave equation in flat spacetime. This is the topic of the following section.

# 6.3 Integration of the wave equation

At first sight the wave equation (6.51) appears to be highly non-linear, with the potentials $h ^ { \alpha \beta }$ present on both sides of the equation. In Sec. 6.2.3 we outlined an iterative procedure that ensures that in the course of each iteration, the wave equation is actually linear in $h ^ { \alpha \beta }$ and involves a known source term $\tau ^ { \alpha \beta }$ . The task of solving the relaxed field equations therefore appears to be straightforward, and in this section we introduce a number of powerful techniques to integrate the wave equation.

For simplicity we shall eliminate all unnecessary tensorial indices on the wave equation, which we now write as

$$
\Pi \psi = - 4 \pi \mu .
$$

The scalar potential $\psi ( x )$ plays the role of $h ^ { \alpha \beta }$ , and the source function $\mu ( x )$ plays the role of $( 4 G / c ^ { 4 } ) \tau ^ { \alpha \beta }$ ; the remaining factor of $4 \pi$ is retained for later convenience. Here $\boldsymbol { x } = \left( c t , \boldsymbol { x } \right)$ labels a spacetime event, and we recall that

$$
\boldsymbol { \Pi } : = \eta ^ { \alpha \beta } \partial _ { \alpha \beta } = - \frac { 1 } { c ^ { 2 } } \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } + \nabla ^ { 2 }
$$

is the wave operator of Minkowski spacetime. The source function $\mu ( x )$ is assumed to be known, but unlike the typical situations encountered in electrodynamics, for example, it cannot be assumed to be confined to a bounded region of three-dimensional space; it is instead taken to be distributed over all space. The reason originates from the post-Minkowskian context: as we have seen, during each iteration of the relaxed field equations, $\tau ^ { \alpha \beta }$ is built in part from $T ^ { \alpha \beta }$ , which normally has compact support, and in part from $t _ { \mathrm { L L } } ^ { \alpha \beta }$ and $t _ { \mathrm { H } } ^ { \alpha \beta }$ , which do not because they are constructed from $h ^ { \alpha \beta }$ , which extends over all space. Our source term in Eq. (6.63) will therefore extend over all space, but $\mu$ is assumed to fall off sufficiently rapidly to ensure that $\psi$ decays at least as fast as $r ^ { - 1 }$ (where $r : = | { \boldsymbol { x } } | ,$ ). Occasionally we shall find it useful to decompose $\mu$ into a piece $\mu _ { \mathrm { c } }$ with compact support (analogous to $T ^ { \alpha \beta }$ ) and a piece $\mu _ { \mathrm { n c } }$ with non-compact support.

A summary of our main results in this section is contained in Box 6.7.

# 6.3.1 Retarded Green’s function

The central tool to integrate Eq. (6.63) is the retarded Green’s function $G ( x , x ^ { \prime } )$ , a solution to

$$
\Theta G ( x , x ^ { \prime } ) = - 4 \pi \delta ( x - x ^ { \prime } ) = - 4 \pi \delta ( c t - c t ^ { \prime } ) \delta ( x - x ^ { \prime } ) ,
$$

with the property that $G ( x , x ^ { \prime } )$ vanishes when $x$ is in the past of $x ^ { \prime }$ . As we show in Box 6.5, the Green’s function is given explicitly by

$$
G ( x , x ^ { \prime } ) = \frac { \delta ( c t - c t ^ { \prime } - | x - x ^ { \prime } | ) } { | x - x ^ { \prime } | } ,
$$

where

$$
| { \pmb x } - { \pmb x } ^ { \prime } | : = \sqrt { ( { \pmb x } - { \pmb x } ^ { \prime } ) ^ { 2 } + ( { \pmb y } - { \pmb y } ^ { \prime } ) ^ { 2 } + ( z - z ^ { \prime } ) ^ { 2 } }
$$

is the Euclidean distance between the field point $_ x$ and the source point $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ . Alternatively, the Green’s function can be expressed as

$$
G ( x , x ^ { \prime } ) = 2 \Theta ( c t - c t ^ { \prime } ) \delta \big [ ( c t - c t ^ { \prime } ) ^ { 2 } - | { \pmb x } - { \pmb x } ^ { \prime } | ^ { 2 } \big ] ,
$$

in terms of the flat spacetime interval $\Delta s ^ { 2 }$ between $x$ and $x ^ { \prime }$ ; here $\Theta ( c t - c t ^ { \prime } )$ is the Heaviside step function, which is equal to one when $c t > c t ^ { \prime }$ and zero when $c t < c t ^ { \prime }$ .

# Box 6.5

# Green’s function for the wave equation

To construct a solution to Eq. (6.65) we write the Green’s function as the Fourier transform

$$
G ( x , x ^ { \prime } ) = \frac { 1 } { 2 \pi } \int \tilde { G } ( k ; x , x ^ { \prime } ) e ^ { - i k ( c t - c t ^ { \prime } ) } d k ,
$$

and we represent the time delta function as

$$
\delta ( c t - c t ^ { \prime } ) = \frac { 1 } { 2 \pi } \int e ^ { - i k ( c t - c t ^ { \prime } ) } d k .
$$

Substituting these expressions into Green’s equation yields

$$
\bigl ( \nabla ^ { 2 } + k ^ { 2 } \bigr ) \tilde { G } ( k ; x , x ^ { \prime } ) = - 4 \pi \delta ( x - x ^ { \prime } ) .
$$

When $k = 0$ this equation reduces to Green’s equation for the Poisson equation, and from this comparison we learn that $\tilde { G } ( 0 ; x , x ^ { \prime } ) = | x - x ^ { \prime } | ^ { - 1 }$ .

We can anticipate that for $k \neq 0 , \tilde { G }$ will be of the form

$$
\tilde { G } ( k ; x , x ^ { \prime } ) = \frac { g ( k , | x - x ^ { \prime } | ) } { | x - x ^ { \prime } | } ,
$$

with $g$ representing a function that stays non-singular when the second argument, $R : = | { \pmb x } - { \pmb x } ^ { \prime } | ,$ approaches zero. That $\tilde { G }$ should depend on the spatial variables through $R$ only can be justified on the grounds that three-dimensional space is both homogeneous (so that $\tilde { G }$ can depend only on the vector $\pmb { R } : = \pmb { x } -$ $\mathbf { } _ { \mathbf { } ^ { x ^ { \prime } } }$ ) and isotropic (so that only the length of the vector matters, and not its direction). That $\tilde { G }$ should behave $\mathsf { a s l } / R$ when $R$ is small is justified by the following discussion.

We take Eq. (2) and integrate both sides over a sphere of small radius $\varepsilon$ centered at $\mathbf { \Delta } _ { x ^ { \prime } }$ . Since $\nabla ^ { 2 } { \tilde { G } } =$ $\boldsymbol { \nabla } \cdot \boldsymbol { \nabla } \tilde { G } _ { \iota }$ we can use Gauss’s theorem to get

$$
\oint _ { R = \varepsilon } { \nabla } \tilde { G } \cdot d S + k ^ { 2 } \int _ { R < \varepsilon } \tilde { G } d ^ { 3 } x = - 4 \pi ,
$$

where $d \pmb { S }$ is the surface element on the sphere. In this equation, the volume integral is of order $\boldsymbol { \tilde { G } } \varepsilon ^ { 3 }$ and it contributes nothing in the limit $\varepsilon \to 0$ , unless $\tilde { G }$ happens to be as singular as $1 / \varepsilon ^ { 3 }$ . The surface integral, on the other hand, is equal to

$$
4 \pi \varepsilon ^ { 2 } { \frac { d { \tilde { G } } } { d R } } { \bigg | } _ { R = \varepsilon } .
$$

If $\tilde { G }$ were to behave as $1 / \varepsilon ^ { 3 }$ , then $d \tilde { G } / d R$ would be of order $1 / \varepsilon ^ { 4 }$ , the surface integral would contribute a term of order $1 / \varepsilon ^ { 2 }$ , and the left-hand side could never give rise to the required $- 4 \pi$ . We conclude that $\tilde { G }$ cannot be so singular, and that the left-hand side is dominated by the surface integral. This implies that $\tilde { G }$ must be of order $1 / \varepsilon$ , as was anticipated in Eq. (3). Setting ${ \tilde { G } } = g / R$ returns $- 4 \pi g ( k , \varepsilon ) +$ $O ( \varepsilon )$ for the surface integral, and this gives us the condition $g ( k , 0 ) = 1$ . We also recall that $g ( 0 , R ) = 1$ .

We may now safely take $R \neq 0$ and substitute Eq. (3) into Eq. (2), taking its right-hand side to be zero. Since $\tilde { G }$ depends on $_ { x }$ only through $R$ , the Laplacian operator becomes

$$
\nabla ^ { 2 }  \frac { 1 } { R ^ { 2 } } \frac { d } { d R } R ^ { 2 } \frac { d } { d R } .
$$

Acting with this on ${ \tilde { G } } = g / R$ yields $g ^ { \prime \prime } / R$ and Eq. (2) becomes

$$
g ^ { \prime \prime } + k ^ { 2 } g = 0 ,
$$

with a prime indicating differentiation with respect to $R$ . With the boundary condition at $R = 0$ specified previously, two linearly independent solutions to this equation are

$$
g _ { \pm } ( k , R ) = e ^ { \pm i k R } .
$$

Substituting this into Eq. (3), and that into Eq. (1), we obtain

$$
G _ { \pm } ( x , x ^ { \prime } ) = \frac { 1 } { 2 \pi } \int \frac { e ^ { \pm i k R } } { R } e ^ { - i k ( c t - c t ^ { \prime } ) } d k = \frac { 1 } { 2 \pi R } \int e ^ { - i k ( c t - c t ^ { \prime } \mp R ) } d k ,
$$

$$
G _ { \pm } ( x , x ^ { \prime } ) = \frac { \delta \bigl ( c t - c t ^ { \prime } \mp | x - x ^ { \prime } | \bigr ) } { | x - x ^ { \prime } | } .
$$

The function $G _ { + } ( x , x ^ { \prime } )$ , which is non-zero when $c t - c t ^ { \prime } = + R _ { \ast }$ , is known as the retarded Green’s function; the function $G _ { - } ( x , x ^ { \prime } )$ , which is non-zero when $c t - c t ^ { \prime } = - R _ { \ast }$ is known as the advanced Green’s function.

The retarded Green’s function can be expressed in the alternative form

$$
G _ { + } ( x , x ^ { \prime } ) = 2 \Theta ( c t - c t ^ { \prime } ) \delta \bigl [ ( c t - c t ^ { \prime } ) ^ { 2 } - | { \pmb x } - { \pmb x } ^ { \prime } | ^ { 2 } \bigr ] .
$$

The new argument of the delta function factorizes as $( c t - c t ^ { \prime } - R ) ( c t - c t ^ { \prime } + R ) _ { }$ , and when $c ( t - t ^ { \prime } ) > 0$ only the first factor may go through zero; the second factor is then equal to $2 R$ , and the delta function is distributionally equal to $\delta ( c t - c t ^ { \prime } - R ) / ( 2 R )$ . At this stage the step function becomes redundant, because the delta function is active only when $c ( t - t ^ { \prime } ) > 0$ , and we have reproduced Eq. (4).

Similarly, the advanced Green’s function can be expressed as

$$
G _ { - } ( x , x ^ { \prime } ) = 2 \Theta ( c t ^ { \prime } - c t ) \delta \bigl [ ( c t - c t ^ { \prime } ) ^ { 2 } - | { \pmb x } - { \pmb x } ^ { \prime } | ^ { 2 } \bigr ] .
$$

In terms of the retarded Green’s function $G ( x , x ^ { \prime } )$ , the solution to Eq. (6.63) is

$$
\psi ( x ) = \int G ( x , x ^ { \prime } ) \mu ( x ^ { \prime } ) d ^ { 4 } x ^ { \prime } ,
$$

where $d ^ { 4 } x ^ { \prime } = d ( c t ^ { \prime } ) d ^ { 3 } x ^ { \prime }$ . After substitution of Eq. (6.66) and integration over $d ( c t ^ { \prime } )$ , this becomes

$$
\psi ( t , { \pmb x } ) = \int \frac { \mu ( t - | { \pmb x } - { \pmb x } ^ { \prime } | / c , { \pmb x } ^ { \prime } ) } { | { \pmb x } - { \pmb x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } .
$$

This is the retarded solution to the wave equation, and the domain of integration extends over $\mathcal { C } ( \boldsymbol { x } )$ , the past light cone of the field point $\boldsymbol { x } = \left( c t , \boldsymbol { x } \right)$ .

# 6.3.2 Near zone and wave zone: slow-motion condition

In the following subsection the domain $\mathcal { C } ( \boldsymbol { x } )$ will be partitioned into a near-zone domain $\mathcal { N }$ and a wave-zone domain $\mathcal { W }$ . Our task in this subsection is to introduce the important notions of near and wave zones in the general context of the wave equation (6.63).

To do so we introduce the following scaling quantities:

$$
\begin{array} { r l } & { t _ { c } : = \mathrm { c h a r a c t e r i s t i c ~ t i m e ~ s c a l e ~ o f ~ t h e ~ s o u r c e } , } \\ & { \omega _ { c } : = \displaystyle \frac { 2 \pi } { t _ { c } } = \mathrm { c h a r a c t e r i s t i c ~ f r e q u e n c y ~ o f ~ t h e ~ s o u r c e } , } \\ & { \lambda _ { c } : = \displaystyle \frac { 2 \pi c } { \omega _ { c } } = c t _ { c } = \mathrm { c h a r a c t e r i s t i c ~ w a v e l e n g t h ~ o f ~ t h e ~ r a d i a t i o n } . } \end{array}
$$

The characteristic time scale $t _ { c }$ is the time required for noticeable changes to occur within the source; it is defined such that $\partial _ { t } \mu$ is typically of order $\mu / t _ { c }$ over the support of the source function. The characteristic frequency $\omega _ { c }$ and wavelength $\lambda _ { c }$ are derived directly from $t _ { c }$ . If, for example, $\mu$ oscillates with a frequency $\omega$ , then $t _ { c } \sim 2 \pi / \omega$ , $\omega _ { c } \sim \omega$ , and $\lambda _ { c } \sim 2 \pi c / \omega$ .

The near zone and the wave zone are defined as

$$
\begin{array} { r l r } & { } & { \mathrm { n e a r \ z o n e } ; \quad r \ll \lambda _ { c } = \displaystyle \frac { 2 \pi c } { \omega _ { c } } = c t _ { c } , } \\ & { } & { \mathrm { w a v e \ z o n e } ; \quad r \gg \lambda _ { c } = \displaystyle \frac { 2 \pi c } { \omega _ { c } } = c t _ { c } . } \end{array}
$$

Thus, the near zone is the region of three-dimensional space in which $r : = | { \boldsymbol { x } } |$ is small compared with a characteristic wavelength $\lambda _ { c }$ , while the wave zone is the region in which $r$ is large compared with this length scale. As we can see from the example of $\mathrm { B o x } 6 . 6$ , the potential behaves very differently in the two zones: in the near zone the difference between $\tau : = t - r / c$ and $t$ is small (the field retardation is unimportant), and time derivatives are small compared with spatial derivatives; in the wave zone the difference between $\tau = t - r / c$ and $t$ is large, and time derivatives are comparable to spatial derivatives. These properties are shared by all generic solutions to the wave equation.

Another important feature of the near zone concerns the quantity $( r / c ) \partial _ { t } \mu$ . This is of order $( r / c ) ( \mu / t _ { c } )$ , or $( r / \lambda _ { c } ) \mu$ , which is much smaller than $\mu$ . In the near zone, therefore,

$$
\frac { r } { c } \frac { \partial \mu } { \partial t } = O \Big ( \frac { r } { \lambda _ { c } } \mu \Big ) \ll \mu .
$$

This states, simply, that the source retardation is unimportant within the near zone.

Thus far our considerations have been general, and our definitions of near and wave zones apply whether the source function $\mu$ is extended over all space or confined to a bounded region $V$ . In addition, our definitions apply independently of the existence of a slow-motion condition, to which we turn next.

When the source function $\mu$ has a piece $\mu _ { \mathrm { c } }$ with compact support, we can introduce the additional scaling quantities

$$
\begin{array} { r l } & { r _ { c } : = \mathrm { c h a r a c t e r i s t i c ~ l e n g t h ~ s c a l e ~ o f ~ t h e ~ c o m p a c t - s u p p o r t ~ s o u r c e } , } \\ & { v _ { c } : = \frac { r _ { c } } { t _ { c } } = \mathrm { c h a r a c t e r i s t i c ~ v e l o c i t y ~ w i t h i n ~ t h e ~ s o u r c e } . } \end{array}
$$

The characteristic radius $r _ { c }$ is defined such that $\mu _ { \mathrm { c } }$ vanishes outside a sphere of radius $r _ { c }$ ; this part of $\mu$ has support only within this sphere. The characteristic velocity $v _ { c }$ is defined in terms of the scales $r _ { c }$ and $t _ { c }$ ; it represents the speed with which changes in the source propagate across the region of space occupied by the source. In the case of a fluid, for example, $v _ { c }$ would be associated with the speed of sound within the fluid. In a binary-star system, $v _ { c }$ would be associated with the orbital velocities of the stars.

A slow-motion condition is in effect when the characteristic velocity $v _ { c }$ is small compared with the speed of light:

$$
v _ { c } \ll c \qquad \mathrm { ( s l o w \mathrm { - m o t i o n } \ c o n d i t i o n ) . }
$$

It then follows from Eq. (6.75) that

$$
r _ { c } \ll \lambda _ { c } ( \mathrm { s l o w \mathrm { - m o t i o n } c o n d i t i o n } ) ;
$$

this equation states that $\mu _ { \mathrm { c } }$ is necessarily situated deep within the near zone when a slowmotion condition is in effect.

<table><tr><td>Box 6.6</td><td colspan="3">Dipole solution to the wave equation</td></tr><tr><td colspan="3"></td></tr><tr><td rowspan="2"></td><td rowspan="2">ψ =(p ·n)</td><td>We examine the solutiontoaspecificversionofEq. (6.63),</td><td></td></tr><tr><td>[cosω(t -r/c)_ @ sinω(t -r/c)]. r² C r</td><td></td></tr><tr><td> potential of a dipole of constant direction p,oscillting in strength with a frequency f = ω/(2π); the</td><td colspan="3">which corresponds to μ = -p : Vδ(x) cos ωt.Here p is a constant vector,r := |x|,n := x/r is the unit radial vector,and ω is an angular frequency. Physically speaking, this solution represents the scalar</td></tr></table>

Our first observation is that $\psi$ behaves very differently depending on whether is small or large compared with λ. When $r \ll \lambda = 2 \pi c / \omega ,$ the trigonometric functions can be expanded in powers of $\omega r / c ,$ and

the result is

$$
\psi = ( { \pmb { p } } \cdot { \pmb { n } } ) \frac { \cos \omega t } { r ^ { 2 } } \bigg [ 1 + O \bigg ( \frac { \omega ^ { 2 } r ^ { 2 } } { c ^ { 2 } } \bigg ) \bigg ]
$$

with a correction term that is quadratic in $r / \lambda \ll 1$ . We observe also that in the near zone – the region $r \ll \lambda -$ the derivatives of $\psi$ are related by

$$
{ \frac { \partial _ { t } \psi } { c | \nabla \psi | } } = O \Big ( { \frac { \omega r } { c } } \Big ) \qquad \mathrm { ( n e a r z o n e ) . }
$$

In the near zone, therefore, a time derivative is smaller than a spatial derivative (multiplied by $c$ ) by a factor of order $r / \lambda \ll 1$ .

When, on the other hand, $r \gg \lambda = 2 \pi c / \omega ,$ it is no longer appropriate to expand the trigonometric functions, and the potential must be expressed as

$$
\psi = - ( { \pmb { p } } \cdot { \pmb { n } } ) \frac { \omega } { c } \frac { \sin \omega \tau } { r } \bigg [ 1 + O \bigg ( \frac { c } { \omega r } \bigg ) \bigg ]
$$

in terms of the retarded-time variable $\tau : = t - r / c ;$ ; here the difference between $\tau$ and $t$ is large, and the correction term is linear in $\lambda / r \ll 1$ . We observe also that in the wave zone – the region $r \gg \lambda$ – the derivatives of $\psi$ are related by

$$
{ \frac { \partial _ { t } \psi } { c | \nabla \psi | } } = O ( 1 ) \qquad { \mathrm { ( w a v e ~ z o n e ) . } }
$$

To obtain this result we have used the fact that the spatial dependence contained in $\pmb { n }$ and $r ^ { - 1 }$ produces a spatial derivative of fractional order $\lambda / r$ , while the spatial dependence contained in $\tau = t - r / c$ produces a spatial derivative of order unity. In the wave zone, therefore, a time derivative has the same order of magnitude as a spatial derivative (multiplied by $c$ ).

# 6.3.3 Integration domains

The integral of Eq. (6.70) extends over the past light cone $\mathcal { C } ( \boldsymbol { x } )$ of the field point $x$ . To evaluate the integral we partition $\mathcal { C } ( \boldsymbol { x } )$ into two pieces, the near-zone domain $\mathcal { N } ( x )$ and the wave-zone domain $\mathcal { W } ( x )$ . We place the boundary of the near and wave zones at an arbitrarily selected radius $\mathcal { R }$ , with $\mathcal { R }$ imagined to be of the same order of magnitude as $\lambda _ { c }$ , the characteristic wavelength of the radiation emitted by $\mu$ . The near zone is then imagined as a three-dimensional ball of radius $\mathcal { R }$ that traces out a world tube $\mathcal { D }$ in spacetime. We let $\mathcal { N } ( x )$ be the part of $\mathcal { C } ( \boldsymbol { x } )$ where $r ^ { \prime } : = | { \pmb x } ^ { \prime } | < \mathcal { R }$ , and we let $\mathcal { W } ( x )$ be the part of $\mathcal { C } ( \boldsymbol { x } )$ where $r ^ { \prime } > \mathcal { R }$ . The near-zone and wave-zone domains join together to form the complete light cone of the field point $x \colon { \mathcal { N } } ( x ) + { \mathcal { W } } ( x ) = { \mathcal { C } } ( x )$ . The domains are illustrated in Fig. 6.1.

We write Eq. (6.70) as

$$
\psi ( x ) = \psi _ { \mathcal { N } } ( x ) + \psi _ { \mathcal { W } } ( x ) ,
$$

![](images/e6ef80df788ade9ddd199080ae9441137e98397c1ff63bf91db921358328225e.jpg)

# Fig. 6.1

Integration domains for the retarded solution of the wave equation: $\mathcal { C } ( \boldsymbol { x } )$ is the past light cone of the field point x; $\mathcal { D }$   
is the world tube traced by a three-dimensional ball of radius ${ \mathcal { R } } ,$ which contains the near-zone region of spacetime;   
$\mathcal { N } ( \boldsymbol { x } )$ is the intersection of ${ \mathcal { C } } ( x )$ with the near zone; and ${ \mathcal W } ( x )$ is the remaining piece of the light cone.

where

$$
\psi _ { \mathcal { N } } ( x ) = \int _ { \mathcal { N } } G ( x , x ^ { \prime } ) \mu ( x ^ { \prime } ) d ^ { 4 } x ^ { \prime }
$$

is the near-zone portion of the light-cone integral, while

$$
\psi _ { \mathcal W } ( x ) = \int _ { \mathcal W } G ( x , x ^ { \prime } ) \mu ( x ^ { \prime } ) d ^ { 4 } x ^ { \prime }
$$

is the wave-zone portion. Methods to evaluate $\psi _ { \mathcal { N } }$ and $\psi _ { \mathcal { H } }$ will be developed in the following two subsections. It is an important fact that while $\psi _ { \mathcal { N } }$ and $\psi _ { \mathcal W }$ will individually depend on the cutoff parameter $\mathcal { R }$ , their sum $\psi = \psi _ { \mathcal { N } } + \psi _ { \mathcal { W } }$ will necessarily be independent of $\mathcal { R }$ . The $\mathcal { R }$ -dependence of $\psi _ { \mathcal { N } }$ and $\psi _ { \mathcal { H } }$ is therefore unimportant, and it can freely be ignored. This observation will serve as a helpful simplifying tool in many subsequent computations.

# 6.3.4 Integration over the near zone

In this subsection we develop methods to evaluate

$$
\psi _ { \mathcal { N } } ( x ) = \int _ { \mathcal { N } } \frac { \mu ( t - | x - x ^ { \prime } | / c , x ^ { \prime } ) } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } ,
$$

the near-zone contribution to the complete solution $\psi = \psi _ { \mathcal { N } } + \psi _ { \mathcal { W } }$ to the wave equation. We recall that the domain of integration $\mathcal { N }$ is the intersection between $\mathcal { C } ( \boldsymbol { x } )$ , the past light cone of the field point $x$ , and the near zone $r ^ { \prime } < \mathcal { R }$ .

# Wave-zone field point

We first evaluate Eq. (6.80) when $x$ is situated in the wave zone, that is, when $r > \mathcal { R }$ . For this purpose we introduce a modified integrand,

$$
\begin{array} { r l } {  { \frac { \mu ( t - | x - x ^ { \prime } | / c , x ^ { \prime } ) } { | x - x ^ { \prime } | } = \int \frac { \mu ( t - | x - x ^ { \prime } | / c , y ) } { | x - x ^ { \prime } | } \delta ( y - x ^ { \prime } ) d ^ { 3 } y } } \\ & { = : \int g ( x , x ^ { \prime } , y ) \delta ( y - x ^ { \prime } ) d ^ { 3 } y , } \end{array}
$$

in which we can treat $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ and $\boldsymbol { y }$ as independent variables. Knowing that $\mathbf { \Delta } _ { \mathbf { { x } ^ { \prime } } }$ lies within the near zone, we treat it as a small vector, and express $g$ as a Taylor expansion about $\mathbf { x } ^ { \prime } = \mathbf { 0 }$ Keeping just a few terms in this expansion, we have

$$
g ( x , x ^ { \prime } , y ) = g ( x , { \bf 0 } , y ) + \frac { \partial g } { \partial x ^ { \prime } { } ^ { j } } x ^ { \prime } { } ^ { j } + \frac { 1 } { 2 } \frac { \partial ^ { 2 } g } { \partial x ^ { \prime } { } ^ { j } x ^ { \prime } { } ^ { k } } x ^ { \prime } { } ^ { j } x ^ { \prime } { } ^ { k } + \cdot \cdot \cdot ,
$$

in which all derivatives are evaluated at $\mathbf { x } ^ { \prime } = \mathbf { 0 }$ . But $\partial g / \partial x ^ { \prime } { } ^ { j } = - \partial g / \partial x ^ { j }$ because $g$ depends on $\mathbf { \Delta } _ { \mathbf { { x } ^ { \prime } } }$ only through the combination $| x - x ^ { \prime } |$ , and our Taylor expansion can be expressed as

$$
g ( x , x ^ { \prime } , y ) = g ( x , { \bf 0 } , y ) - \frac { \partial g } { \partial x ^ { j } } x ^ { \prime j } + \frac { 1 } { 2 } \frac { \partial ^ { 2 } g } { \partial x ^ { j } x ^ { k } } x ^ { \prime j } x ^ { \prime k } + \cdot \cdot \cdot .
$$

The derivatives of $g$ are still evaluated at $\mathbf { x } ^ { \prime } = \mathbf { 0 }$ , but because the differentiation is now carried out with respect to $_ x$ , we can set $\mathbf { x } ^ { \prime } = \mathbf { 0 }$ in $g$ before taking the derivatives. Observing that $g$ then becomes a function of $| { \boldsymbol { x } } | = r$ only, we have

$$
g ( x , x ^ { \prime } , y ) = g ( r , 0 , y ) - { \frac { \partial g ( r , 0 , y ) } { \partial x ^ { j } } } x ^ { \prime j } + { \frac { 1 } { 2 } } { \frac { \partial ^ { 2 } g ( r , 0 , y ) } { \partial x ^ { j } x ^ { k } } } x ^ { \prime j } x ^ { \prime k } + \cdot \cdot \cdot .
$$

Keeping all terms of the Taylor expansion, this is

$$
g ( x , x ^ { \prime } , y ) = \sum _ { \ell = 0 } ^ { \infty } \frac { ( - 1 ) ^ { \ell } } { \ell ! } x ^ { \prime L } \partial _ { L } g ( r , 0 , y ) ,
$$

where $L : = j _ { 1 } j _ { 2 } \cdots j _ { \ell }$ is a multi-index of the sort introduced back in Sec. 1.5.3. More explicitly, we have established the identity

$$
\frac { \mu ( t - | x - x ^ { \prime } | / c , y ) } { | x - x ^ { \prime } | } = \sum _ { \ell = 0 } ^ { \infty } \frac { ( - 1 ) ^ { \ell } } { \ell ! } x ^ { \prime L } \partial _ { L } \frac { \mu ( t - r / c , y ) } { r } .
$$

The dependence of $\mu / r$ on the variables $x ^ { j }$ is contained entirely within $r$ .

Inserting this within Eq. (6.81) to restore $y = x ^ { \prime }$ , and substituting the result into Eq. (6.80), we arrive at

$$
\psi _ { \mathcal { N } } ( t , x ) = \sum _ { \ell = 0 } ^ { \infty } \frac { ( - 1 ) ^ { \ell } } { \ell ! } \partial _ { L } \bigg [ \frac { 1 } { r } \int _ { \mathcal { M } } \mu ( \tau , x ^ { \prime } ) x ^ { \prime L } d ^ { 3 } x ^ { \prime } \bigg ] ,
$$

where

$$
\tau : = t - r / c
$$

![](images/f81fcc4fd4dda525148061e089cbc21cc6dcff929c118d415c54ea912cadb2cd.jpg)  
Near-zone integration, wave-zone field point. The domain $\mathcal { M }$ is a surface of constant time bounded externally by the sphere $r ^ { \prime } = \mathcal { R }$ .

is a retarded-time variable. Note that the temporal dependence of the source function no longer involves $\mathbf { \Delta } _ { \mathbf { { x } ^ { \prime } } }$ , the variable of integration. The domain of integration has therefore become a surface of constant time (the constant being equal to $\tau$ ) bounded externally by the sphere $r ^ { \prime } = \mathcal { R }$ . This domain is denoted $\mathcal { M }$ in Eq. (6.87), and is illustrated in Fig. 6.2.

Equation (6.87) is valid everywhere within the wave zone. It simplifies when $r  \infty$ , that is, when $\psi _ { \mathcal { N } }$ is evaluated in the far-away wave zone. In this limit we retain only the dominant $r ^ { - 1 }$ term in $\psi _ { \mathcal { N } }$ , and we approximate Eq. (6.87) by

$$
\psi _ { \mathcal { N } } = \frac { 1 } { r } \sum _ { \ell = 0 } ^ { \infty } \frac { ( - 1 ) ^ { \ell } } { \ell ! } \int _ { \mathcal { M } } \partial _ { L } \mu ( \tau , \pmb { x } ^ { \prime } ) x ^ { \prime L } d ^ { 3 } x ^ { \prime } + O ( r ^ { - 2 } ) .
$$

The dependence of $\mu$ on $x ^ { j }$ is contained in $\tau$ , so that $\partial _ { j } \mu = - c ^ { - 1 } \mu ^ { ( 1 ) } \partial _ { j } r = - c ^ { - 1 } \mu ^ { ( 1 ) } n _ { j }$ , in which $\mu ^ { ( 1 ) }$ denotes the first derivative of $\mu$ with respect to $\tau$ . We used the fact that

$$
\partial _ { j } r = n _ { j } ,
$$

where $n ^ { j } = x ^ { j } / r$ is the unit radial vector. Invoking this result once more, we find that $\partial _ { j k } \mu = c ^ { - 2 } \mu ^ { ( 2 ) } n _ { j } n _ { k } + O ( r ^ { - 1 } )$ , and continuing along these lines reveals that in general, $\partial _ { L } \mu = ( - 1 ) ^ { \ell } c ^ { - \ell } \mu ^ { ( \ell ) } n _ { L } + O ( r ^ { - 1 } )$ . Inserting this into our previous expression for $\psi _ { \mathcal { N } }$ , we find that Eq. (6.87) becomes

$$
\psi _ { \mathcal { N } } ( t , { \pmb x } ) = \frac { 1 } { r } \sum _ { \ell = 0 } ^ { \infty } \frac { 1 } { \ell ! c ^ { \ell } } n _ { L } \bigg ( \frac { d } { d \tau } \bigg ) ^ { \ell } \int _ { \mathcal { M } } \mu ( \tau , { \pmb x } ^ { \prime } ) { \pmb x } ^ { \prime L } d ^ { 3 } { \pmb x } ^ { \prime } + O ( r ^ { - 2 } )
$$

![](images/ef7974385638b92b96b64a831fe5ec924784bab162af42d0750233eb04b7aa44.jpg)  
Fig. 6.3 Near-zone integration, near-zone field point.

in the far-away wave zone. This is a multipole expansion for the potential $\psi _ { \mathcal { N } }$ , in which each $\ell$ -pole moment $\int _ { \mathcal { M } } \mu x ^ { L } d ^ { 3 } x$ is differentiated $\ell$ times with respect to $\tau$ . Note that $n _ { L } x ^ { \prime L } = n _ { j _ { 1 } } n _ { j _ { 2 } } \cdot \cdot \cdot n _ { j _ { \ell } } x ^ { \prime j _ { 1 } } x ^ { \prime j _ { 2 } } \cdot \cdot \cdot x ^ { \prime j _ { \ell } } = ( { \pmb n } \cdot { \pmb x } ^ { \prime } ) ^ { \ell }$ .

# Near-zone field point

We next evaluate Eq. (6.80) when $x$ is situated in the near zone, that is, when $r = | { \boldsymbol { x } } | < \mathcal { R }$ . In this situation, both $_ { x }$ and $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ lie within the near zone, and $| x - x ^ { \prime } |$ can be treated as a small quantity. To evaluate the integral we simply Taylor-expand the time-dependence of the source function,

$$
\mu ( t - | \pmb { x } - \pmb { x } ^ { \prime } | / c ) = \mu ( t ) - \frac { 1 } { c } \frac { \partial \mu } { \partial t } | \pmb { x } - \pmb { x } ^ { \prime } | + \frac { 1 } { 2 c ^ { 2 } } \frac { \partial ^ { 2 } \mu } { \partial t ^ { 2 } } | \pmb { x } - \pmb { x } ^ { \prime } | ^ { 2 } + \cdots ,
$$

in which all derivatives are evaluated at time $t$ . Substituting this expansion into Eq. (6.80) produces

$$
\psi _ { \mathcal { N } } ( t , x ) = \sum _ { \ell = 0 } ^ { \infty } \frac { ( - 1 ) ^ { \ell } } { \ell ! c ^ { \ell } } \bigg ( \frac { \partial } { \partial t } \bigg ) ^ { \ell } \int _ { \mathcal { M } } \mu ( t , x ^ { \prime } ) | x - x ^ { \prime } | ^ { \ell - 1 } d ^ { 3 } x ^ { \prime } ,
$$

which is valid everywhere within the near zone. Note that once more the domain of integration is $\mathcal { M }$ , a surface of constant time bounded externally by the sphere $r ^ { \prime } = \mathcal { R }$ ; here, however, the integral is evaluated at time $t$ instead of at the retarded time $\tau$ . The geometry is illustrated in Fig. 6.3.

# 6.3.5 Integration over the wave zone

In this subsection we develop a method to evaluate

$$
\psi _ { \mathcal W } ( x ) = \int _ { \mathcal W } \frac { \mu ( t - | x - x ^ { \prime } | / c , x ^ { \prime } ) } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } ,
$$

the wave-zone portion of the complete solution $\psi = \psi _ { \mathcal { N } } + \psi _ { \mathcal { W } }$ to the wave equation. We recall that the domain of integration $\mathcal { W }$ is the intersection between $\mathcal { C } ( \boldsymbol { x } )$ , the past light cone of the field point $x$ , and the wave zone $r ^ { \prime } > \mathcal { R }$ .

Before we proceed with the work, we pause and ask whether $\psi _ { \mathcal { H } } ( x )$ could be dispensed with by taking the limit $\mathcal { R } \to \infty$ , thereby achieving $\psi _ { \mathcal { N } }  \psi$ and $\psi \mathcal { H } \to 0$ . The answer is no: we cannot take $\mathcal { R }$ beyond its original value of order $\lambda _ { c }$ , and we cannot dispense with $\psi _ { \mathcal W }$ . The reason can be gleaned from Figs. 6.2 and 6.3: The difference between the domain $\mathcal { M }$ and the light cone $\mathcal { C } ( \boldsymbol { x } )$ becomes increasingly large as $\mathcal { R }$ increases, and the Taylor expansion for $\mu ( t - | { \pmb x } - { \pmb x } ^ { \prime } | / c )$ becomes increasingly inaccurate; the resulting expression for $\psi _ { \mathcal { N } }$ would then become increasingly unreliable as $\mathcal { R }$ increases beyond $\lambda _ { c }$ . This lesson was hard learned. Early attempts to integrate the wave equation of post-Minkowskian theory were indeed based on the limit $\mathcal { R } \to \infty$ , with the expectation that $\psi _ { \mathcal { N } }$ would make a good approximation to $\psi$ . Such attempts led to a host of divergent integrals that had to be argued away or swept under the rug. While these methods could sometimes be teased to give correct physical results, their mathematical justification left a lot to be desired. The decomposition of $\psi$ into near-zone and wave-zone pieces nicely overcomes all these difficulties.

Our method to integrate over $\mathcal { W }$ must reflect the nature of the integrand there, and the fact that we are integrating over a null cone instead of a surface of constant time. For the slow-motion systems that we will generally encounter, the compact-support piece of $\mu$ lies deep within the near zone, and therefore vanishes on $\mathcal { W }$ . The extended piece survives, and it is built from potentials that are themselves solutions to the wave equation. This implies that for a given integration point $( c t ^ { \prime } , \mathbf { \boldsymbol { x } } ^ { \prime } )$ on $\mathcal { W }$ , $\mu _ { \mathrm { n c } }$ is predominantly a function of $t ^ { \prime } - r ^ { \prime } / c$ . Integration over the light cone is therefore facilitated by adopting retarded time as a variable of integration. The strategy is therefore this: Express the integral of Eq. (6.93) in terms of the spherical coordinates $( r ^ { \prime } , \theta ^ { \prime } , \phi ^ { \prime } )$ , and then switch variables from $r ^ { \prime }$ to $u ^ { \prime } : = c t ^ { \prime } - r ^ { \prime }$ in order to perform the integration.

The strategy lends itself to a nice geometrical representation (see Fig. 6.4). A surface $u ^ { \prime } =$ constant is a future-directed null cone $\mathcal { F }$ that emanates from $r ^ { \prime } = 0$ . It intersects $\mathcal { C } ( \boldsymbol { x } )$ on a two-dimensional surface $\mathcal { S } ( u ^ { \prime } )$ parameterized by the angular variables $\theta ^ { \prime }$ and $\phi ^ { \prime }$ . Integration on $\mathcal { C } ( \boldsymbol { x } )$ can therefore be achieved by integrating over $\mathcal { S } ( u ^ { \prime } )$ and adding the contributions from each relevant $\mathcal { F }$ . Integrating on $\mathcal { S } ( u ^ { \prime } )$ amounts to varying $\theta ^ { \prime }$ and $\phi ^ { \prime }$ over their allowed range, and the integration over $\mathcal { C } ( \boldsymbol { x } )$ is completed by varying $u ^ { \prime }$ , which ranges from $u ^ { \prime } = - \infty$ to $u ^ { \prime } = u : = c t - r$ ; the final value of $u ^ { \prime }$ corresponds to a future null cone that is tangent to $\mathcal { C } ( \boldsymbol { x } )$ , emanating from the spacetime event at which $r ^ { \prime } = 0$ crosses $\mathcal { C } ( \boldsymbol { x } )$ .

To make these ideas explicit, we first provide a mathematical expression for $\mathcal { S } ( u ^ { \prime } )$ . Because $c t ^ { \prime } = c t - | \pmb { x } - \pmb { x } ^ { \prime } |$ on $\mathcal { C } ( \boldsymbol { x } )$ and $c t ^ { \prime } = u ^ { \prime } + r ^ { \prime }$ on $\mathcal { F }$ , we find that it is described

![](images/85ffc38ec3b1ddd3a647d0723c54523321c57c9ca8a1b148340fcb397b34b4cb.jpg)

# Fig. 6.4

Geometrical representation of the wave-zone integrations. $\mathcal { C } ( \boldsymbol { x } )$ is the past light cone of the field point x. $\mathcal { F }$ is the future light cone $u ^ { \prime } = c t ^ { \prime } - r ^ { \prime } = c$ onstant with apex a $\mathbf { \nabla } \cdot r ^ { \prime } = 0 . \mathcal { S } ( u ^ { \prime } )$ is the two-dimensional surface of intersection between the past and future light cones.

$$
\boldsymbol { u } ^ { \prime } = c t - \boldsymbol { r } ^ { \prime } - | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | ,
$$

in which $u ^ { \prime }$ and $t$ are constant. The equation can be solved for $r ^ { \prime }$ expressed as a function of $\theta ^ { \prime }$ and $\phi ^ { \prime }$ :

$$
r ^ { \prime } ( u ^ { \prime } , \theta ^ { \prime } , \phi ^ { \prime } ) = { \frac { ( c t - u ^ { \prime } ) ^ { 2 } - r ^ { 2 } } { 2 ( c t - u ^ { \prime } - n ^ { \prime } \cdot x ) } } ,
$$

where ${ \pmb n } ^ { \prime } : = { \pmb x } ^ { \prime } / r ^ { \prime }$ . We next return to Eq. (6.93) and change variables from $r ^ { \prime }$ to $u ^ { \prime }$ , using

$$
{ \frac { \partial u ^ { \prime } } { \partial r ^ { \prime } } } = { \pmb { n } } ^ { \prime } \cdot \pmb { \nabla } ^ { \prime } u ^ { \prime } = { \frac { u ^ { \prime } - c t + { \pmb { n } } ^ { \prime } \cdot \pmb { x } } { | \pmb { x } - \pmb { x } ^ { \prime } | } } \cdotp
$$

This yields

$$
\psi _ { \mathcal { W } } = \int _ { - \infty } ^ { u } d u ^ { \prime } \oint _ { \mathcal { S } ( u ^ { \prime } ) } \frac { \mu ( ( u ^ { \prime } + r ^ { \prime } ) / c , \pmb { x } ^ { \prime } ) } { c t - u ^ { \prime } - \pmb { n } ^ { \prime } \cdot \pmb { x } } r ^ { \prime } ( u ^ { \prime } , \theta ^ { \prime } , \phi ^ { \prime } ) ^ { 2 } d \Omega ^ { \prime } ,
$$

our new starting expression to calculate the wave-zone contribution to the potential $\psi ( x )$

To proceed it will be necessary to restrict our attention to source functions of the form

$$
\mu ( x ^ { \prime } ) = \frac { 1 } { 4 \pi } \frac { f ( \tau ^ { \prime } ) } { r ^ { \prime n } } n ^ { \prime \langle L \rangle } ,
$$

where $f$ is an arbitrary function of $\tau ^ { \prime } = t ^ { \prime } - r ^ { \prime } / c$ , $n$ is an arbitrary integer, and $n ^ { \prime \langle L \rangle }$ is an STF product of $\ell$ radial vectors $n ^ { \prime j } = x ^ { \prime j } / r ^ { \prime }$ ; these angular tensors were introduced back in Sec. 1.5.3, and we recall that they are closely related to the spherical-harmonic functions $Y _ { l m } ( \theta ^ { \prime } , \phi ^ { \prime } )$ . Fortunately, the restriction imposed here is not too severe from a practical point of view: All source functions to be inserted in wave-zone integrals in this book will be superpositions of the irreducible forms displayed in Eq. (6.98).

Substituting Eq. (6.98) into Eq. (6.97), we obtain

$$
\psi _ { \mathcal W } = \frac { 1 } { 4 \pi } \int _ { - \infty } ^ { u } d u ^ { \prime } ~ f ( u ^ { \prime } / c ) \oint _ { \mathcal S ( u ^ { \prime } ) } \frac { n ^ { \prime \langle L \rangle } } { r ^ { \prime } ( u ^ { \prime } , \theta ^ { \prime } , \phi ^ { \prime } ) ^ { n - 2 } } \frac { d \Omega ^ { \prime } } { c t - u ^ { \prime } - n ^ { \prime } \cdot x } .
$$

The angular integration can be simplified by orienting the coordinate axes so that the selected field point $_ x$ is aligned with the $z$ -direction, so that $\mathbf { \nabla } n = e _ { z }$ ; this specific choice will be undone at the end of our computation. We make use of Eq. (1.164),

$$
n ^ { \prime \langle L \rangle } = N _ { \ell } \sum _ { m = - \ell } ^ { \ell } \mathcal { Y } _ { \ell m } ^ { \langle L \rangle } Y _ { \ell m } ( \theta ^ { \prime } , \phi ^ { \prime } ) ,
$$

where $N _ { \ell } : = { 4 \pi \ell ! } / { ( 2 \ell + 1 ) ! ! }$ , integrate over $d \phi ^ { \prime }$ , and observe that since the rest of the integrand is independent of $\phi ^ { \prime }$ , the only surviving term in the sum is $m = 0$ . Inserting now $Y _ { \ell 0 } = [ ( 2 \ell + 1 ) / 4 \pi ] ^ { 1 / 2 } P _ { \ell } ( \cos \theta ^ { \prime } )$ and $\mathcal { Y } _ { \ell 0 } ^ { \langle L \rangle } \stackrel { - } { = } [ 4 \pi / ( 2 \ell + 1 ) ] ^ { 1 / 2 } N _ { \ell } ^ { - 1 } e _ { z } ^ { \langle L \rangle }$ within the integral, we obtain

$$
\psi _ { \mathcal { W } } = \frac { 1 } { 2 } n ^ { \langle L \rangle } \int _ { - \infty } ^ { u } d u ^ { \prime } \ : f ( u ^ { \prime } / c ) \int _ { \mathcal { S } ( u ^ { \prime } ) } \frac { P _ { \ell } ( \xi ) } { r ^ { \prime } ( u ^ { \prime } , \xi ) ^ { n - 2 } ( c t - u ^ { \prime } - r \xi ) } d \xi ,
$$

in which $\xi : = \cos \theta ^ { \prime }$ and

$$
r ^ { \prime } ( u ^ { \prime } , \xi ) : = r ^ { \prime } ( u ^ { \prime } , \theta ^ { \prime } , 0 ) = \frac { ( c t - u ^ { \prime } ) ^ { 2 } - r ^ { 2 } } { 2 ( c t - u ^ { \prime } - r \xi ) } .
$$

Switching integration variables from $\xi$ back to $r ^ { \prime }$ , using the fact that $\partial \xi / \partial r ^ { \prime } = ( c t - u ^ { \prime } -$ $r \xi ) / r r ^ { \prime }$ , we recast $\psi _ { \mathcal W }$ in the elegant form

$$
\psi _ { \mathcal W } = \frac { n ^ { \langle L \rangle } } { 2 r } \int _ { - \infty } ^ { u } d u ^ { \prime } f ( u ^ { \prime } / c ) \int _ { \mathcal { S } ( u ^ { \prime } ) } \frac { P _ { \ell } ( \xi ) } { r ^ { \prime ( n - 1 ) } } d r ^ { \prime } ,
$$

in which $\xi$ is now the function of $\boldsymbol { r } ^ { \prime }$ determined by Eq. (6.102); an explicit expression will be provided below. We observe that the angular dependence of $\psi _ { \mathcal { H } }$ is contained in the factor $n ^ { \langle L \rangle }$ , with $\pmb { n }$ previously chosen to be aligned with the $z$ -direction. But since the remaining integral is now independent of all angles, the orientation of the coordinate axes has become irrelevant, and the special choice $\pmb { n } = \pmb { e } _ { z }$ immaterial; we may now take $\pmb { n }$ to point in the arbitrary direction specified by the polar angles $\theta$ and $\phi$ . The potential $\psi _ { \mathcal W }$ has thus become a function of $( t , r , \theta , \phi )$ , with the dependence on $t$ contained within $u = c t - r$ .

To complete the wave-zone integration we must now give an explicit description of the closed surface $\mathcal { S } ( u ^ { \prime } )$ , and specify the limits of the integral over $d \boldsymbol { r } ^ { \prime }$ so as to exclude the near zone from the domain of integration. The specific limits depend on whether the field point is in the near zone or in the wave zone.

![](images/3ed9821bab7b5008e2a84dbce68b01b9d90eec949160ac121dcabe9f8816acc7.jpg)  
Fig. 6.5

Integration over the domain ${ \mathcal W } ( x )$ , for a field point x in the wave zone, is carried out over each intersection surface $\mathcal { S } ( u ^ { \prime } )$ in a sequence of future null cones $u ^ { \prime } =$ constant. The left panel corresponds to $u ^ { \prime } < u - 2 \mathcal { R } _ { \mathrm { ~ } }$ ; the integration runs from $\xi = - 1 \left( { \mathfrak { p o i n t } } { \mathcal { A } } \right) { \mathfrak { t o } } \xi = 1 \left( { \mathfrak { p o i n t } } { \mathcal { B } } \right)$ . The center panel corresponds to $u ^ { \prime } > u - 2 \mathcal { R } ;$ the intersection $\mathcal { S } ( u ^ { \prime } )$ terminates at $\mathcal { A } ^ { \prime }$ , the boundary of the near zone $\mathcal { N }$ . The right panel corresponds to $u ^ { \prime } = u ;$ the cones are tangent, and $\mathcal { S } ( u ^ { \prime } )$ runs from the edge of the near zone to x.

# Wave-zone field point

To begin we assume that the field point $x$ is situated in the wave zone, so that $r > \mathcal { R }$ . We recall that $\mathcal { S } ( u ^ { \prime } )$ is the intersection between the past null cone $\mathcal { C } ( \boldsymbol { x } )$ and the future null cone $u ^ { \prime } =$ constant. From Fig. 6.5 we see that when $u ^ { \prime } < u - 2 \mathcal { R }$ , $\mathcal { S } ( u ^ { \prime } )$ does not encounter the boundary of the near zone, and in this case $\xi$ ranges from $\xi = - 1$ , at which $\begin{array} { r } { r ^ { \prime } = \frac { 1 } { 2 } ( c t - u ^ { \prime } - r ) = \frac { 1 } { 2 } ( u - u ^ { \prime } ) } \end{array}$ , to $\xi = 1$ , at which $r ^ { \prime } = { \textstyle { \frac { 1 } { 2 } } } ( c t - u ^ { \prime } + r ) = { \textstyle { \frac { 1 } { 2 } } } ( u - u ^ { \prime } ) + r$ ; these limits correspond to the events $\mathcal { A }$ and $\boldsymbol { B }$ in the left panel of Fig. 6.5. When $u - 2 \mathcal { R } \leq$ $u ^ { \prime } \leq u$ we see that $\mathcal { S } ( u ^ { \prime } )$ runs into the boundary of the near zone, and in this case the lower bound on $r ^ { \prime }$ must be $r ^ { \prime } = \mathcal { R }$ , with the corresponding value of $\xi > - 1$ obtained from Eq. (6.102); the upper bound on $r ^ { \prime }$ is still $\begin{array} { r } { \frac { 1 } { 2 } ( u - u ^ { \prime } ) + r } \end{array}$ , and these limits correspond to events $\mathcal { A } ^ { \prime }$ and $B ^ { \prime }$ in the center panel of Fig. 6.5. The integration terminates when $u ^ { \prime } = u$ , as depicted on the right panel.

Defining $\begin{array} { r } { s : = \frac { 1 } { 2 } ( u - u ^ { \prime } ) } \end{array}$ and the functions

$$
\begin{array} { l } { { \displaystyle { \cal A } ( s , r ) : = \int _ { \mathcal { R } } ^ { r + s } \frac { P _ { \ell } ( \xi ) } { r ^ { \prime ( n - 1 ) } } d r ^ { \prime } } , } \\ { { \displaystyle { \cal B } ( s , r ) : = \int _ { s } ^ { r + s } \frac { P _ { \ell } ( \xi ) } { r ^ { \prime ( n - 1 ) } } d r ^ { \prime } } , } \end{array}
$$

we obtain the final expression

$$
\psi _ { \mathcal { W } } ( t , r , \theta , \phi ) = \frac { n ^ { \langle L \rangle } } { r } \left\{ \int _ { 0 } ^ { \mathcal { R } } d s f ( \tau - 2 s / c ) A ( s , r ) + \int _ { \mathcal { R } } ^ { \infty } d s f ( \tau - 2 s / c ) B ( s , r ) \right\}
$$

for the wave-zone contribution to the potential $\psi ( x )$ , when $x$ is situated in the wave zone. The quantity $\xi$ that appears in $A$ and $B$ is determined by Eq. (6.102), in which we insert the definitions $u = c t - r$ and $\begin{array} { r } { s = \frac { 1 } { 2 } ( u - u ^ { \prime } ) } \end{array}$ ; this yields

$$
\xi = \frac { r + 2 s } { r } - \frac { 2 s ( r + s ) } { r r ^ { \prime } } ,
$$

with $\xi = 1$ when $r ^ { \prime } = r + s$ and $\xi = - 1$ when $r ^ { \prime } = s$ .

![](images/37aa4545c140257ed8443cb8289e85b85b5315651036ae5569c95ffe35238aa4.jpg)

# Fig. 6.6

Integration over the domain $\mathcal { W } ( \boldsymbol { x } )$ , for a field point x in the near zone. The left panel corresponds to $u ^ { \prime } < u - 2 \mathcal { R } ;$ the integration runs from $\xi = - 1 \left( { \mathfrak { p o i n t } } { \mathcal { A } } \right) { \mathfrak { t o } } \xi = 1 \left( { \mathfrak { p o i n t } } { \mathcal { B } } \right)$ . The center panel corresponds to $u ^ { \prime } > u - 2 \mathcal { R } ;$ the intersection $\mathcal { S } ( u ^ { \prime } )$ terminates at $\mathcal { A } ^ { \prime }$ , the boundary of the near zone $\mathcal { N }$ . The right panel corresponds to $\boldsymbol { u } ^ { \prime } = \boldsymbol { u } - 2 \mathcal { R } + 2 \boldsymbol { r } _ { i }$ ; the future cone intersects the past cone at $\xi = 1 ( \mathsf { p o i n t } B ^ { \prime \prime } )$ at the edge of the near zone.

# Near-zone field point

We next take the field point $x$ to be situated in the near zone, so that $r < \mathcal { R }$ . In this case we find again that when $u ^ { \prime } < u - 2 \mathcal { R }$ , $\mathcal { S } ( u ^ { \prime } )$ does not encounter the near zone and $\xi$ ranges from $^ { - 1 }$ to $+ 1$ (represented by the points $\mathcal { A }$ and $\boldsymbol { B }$ in the left panel of Fig. 6.6). When $u ^ { \prime } > u - 2 \mathcal { R }$ , the integration runs from point $\mathcal { A } ^ { \prime }$ in the center panel of Fig. 6.6, at which $r ^ { \prime } = \mathcal { R }$ , to point $B ^ { \prime }$ , at which $\xi = 1$ . But there is now a maximum value of $u ^ { \prime }$ at which the future null cone intersects $\mathcal { C } ( \boldsymbol { x } )$ at $\xi = 1$ (point $B ^ { \prime \prime }$ in the right panel), corresponding to $u ^ { \prime } = u - 2 \mathcal { R } + 2 r$ ; here the integration terminates. In this case, the minimum value of $\begin{array} { r } { s : = \frac { 1 } { 2 } ( u - u ^ { \prime } ) } \end{array}$ is $\mathcal { R } - r$ , and we obtain the expression

$$
\psi _ { \mathcal { W } } ( t , r , \theta , \phi ) = \frac { n ^ { \langle L \rangle } } { r } \left\{ \int _ { \mathcal { R } - r } ^ { \mathcal { R } } d s f ( \tau - 2 s / c ) A ( s , r ) + \int _ { \mathcal { R } } ^ { \infty } d s f ( \tau - 2 s / c ) B ( s , r ) \right\}
$$

for the wave-zone contribution to the potential $\psi ( x )$ , when $x$ is situated in the near zone. The functions $A ( s , r )$ and $B ( s , r )$ are again given by Eq. (6.104), and $\xi$ is still given by Eq. (6.106).

Equation (6.105) is a concrete expression for the $\psi _ { \mathcal { H } } ( x )$ of Eq. (6.93) when the field point $x$ is in the wave zone, and Eq. (6.107) is the corresponding expression when $x$ is in the near zone. In both cases the source function $\mu ( x ^ { \prime } )$ takes the form displayed in Eq. (6.98), with $f ( \tau ^ { \prime } )$ describing its temporal behavior, $r ^ { \prime - n }$ describing its radial profile, and $n ^ { \prime \langle L \rangle }$ describing its angular profile. Note that $\psi _ { \mathcal { H } } ( x )$ depends on the entire past history of the system, because $f$ must be evaluated at retarded times $\tau - 2 s / c$ all the way back to $- \infty$ . This is a direct consequence of the fact that the source $\mu$ is not bounded by the near zone, and is generated by retarded fields that are themselves solutions to the wave equation. In post-Minkowskian theory, this feature is a consequence of the non-linearity of the Einstein field equations, which imply that the gravitational field itself generates gravity. While it may seem like a daunting task to evaluate the integrals of Eqs. (6.105) and (6.107), we shall find that they can be evaluated relatively easily for many interesting situations, with physically reasonable assumptions about the past behavior to ensure convergence.

# Estimates

It is instructive to give crude estimates to the integrals of Eqs. (6.105) and (6.107). Suppose first that we wish to evaluate Eq. (6.105) in the far-away wave zone, and keep only its dominant $r ^ { - 1 }$ part. Taking $P _ { \ell } ( \xi )$ to be of order unity, we approximate the functions defined by Eqs. (6.104) as $\begin{array} { r } { A \sim \int _ { \mathcal { R } } ^ { \infty } p ^ { - ( n - 1 ) } d p \sim \mathcal { R } ^ { - ( n - 2 ) } } \end{array}$ and $\begin{array} { r } { B \sim \int _ { s } ^ { \infty } p ^ { - ( n - 1 ) } d p \sim s ^ { - ( n - 2 ) } } \end{array}$ ; we ignore all numerical factors and exclude the special case $n = 2$ . Inserting $A$ into the first integral of Eq. (6.105) yields $\begin{array} { r l r } { \mathcal { R } ^ { - ( n - 2 ) } \int _ { 0 } ^ { \mathcal { R } } f ( \tau - 2 s / c ) d s ~ } & { { } } & { } \end{array}$ . Taking $\mathcal { R }$ to be small, we Taylorexpand $f ( \tau - 2 s / c )$ about $s = 0$ and integrate term by term. A typical term in the expansion is

$$
\frac { \mathcal { R } ^ { q + 1 } } { c ^ { q } \mathcal { R } ^ { n - 2 } } f ^ { ( q ) } ( \tau ) ,
$$

where the superscript $( q )$ indicates the number of derivatives with respect to $\tau$ . As was motivated in the paragraph that follows Eq. (6.79), we are interested in the $\mathcal { R }$ -independent part of $\psi _ { \mathcal W }$ . In order to extract this from our previous expansion, we retain the term $q =$ $n - 3$ and discard all others. An estimate for the first integral is therefore $c ^ { - ( n - 3 ) } f ^ { ( n - 3 ) } ( \tau )$ . We next substitute $B$ into the second integral of Eq. (6.105) and obtain $\textstyle { \int _ { \mathcal { R } } ^ { \infty } s ^ { - ( n - 2 ) } f ( \tau - }$ $2 s / c ) d s$ . Assuming that $f$ and all its derivatives vanish in the infinite past, repeated integration by parts returns an expression of the form

$$
\frac { f ( \tau - 2 \mathcal { R } / c ) } { \mathcal { R } ^ { n - 3 } } + \frac { f ^ { ( 1 ) } ( \tau - 2 \mathcal { R } / c ) } { c \mathcal { R } ^ { n - 4 } } + \frac { f ^ { ( 2 ) } ( \tau - 2 \mathcal { R } / c ) } { c ^ { 2 } \mathcal { R } ^ { n - 5 } } + \cdot \cdot \cdot
$$

The $\mathcal { R }$ -independent part of this is easily seen to be of the form $c ^ { - ( n - 3 ) } f ^ { ( n - 3 ) } ( \tau )$ , as we had for the first integral. We conclude that a crude estimate for Eq. (6.105) is

$$
\psi _ { \mathcal { W } } \sim \frac { 1 } { c ^ { n - 3 } } \frac { n ^ { \langle L \rangle } } { r } f ^ { ( n - 3 ) } ( \tau ) \qquad \mathrm { ( f a r \mathrm { - } a w a y ~ w a v e ~ z o n e ) . }
$$

The estimate ignores numerical factors, $\mathcal { R }$ -dependent terms, and terms that decay faster than $r ^ { - 1 }$ .

This estimate leads us to expect that the contribution from the wave-zone integral will be a small correction at any given iteration order of post-Minkowskian theory. First, the source function $f$ is built from the pseudotensors $t _ { \mathrm { L L } } ^ { \alpha \beta }$ and $t _ { \mathrm { H } } ^ { \alpha \beta }$ , which are quadratic in $h ^ { \alpha \beta }$ and therefore much smaller than the potentials themselves. Second, depending on $n$ , the power with which the source falls off with $r ^ { - 1 }$ , there will be additional time derivatives acting on $f$ , generating additional powers of $v _ { c } / c$ . Accordingly, in many cases we will be able to ignore the contributions of the wave-zone integrals. But even when we are required to calculate those contributions, we will be able to do so using only the leading-order contributions to $f$ . We will see a specific example of such a calculation in Sec. 7.4.

Suppose next that we wish to evaluate Eq. (6.107) deep within the near zone, f $\operatorname { x } r \ll \mathcal { R }$ . Here the first integral of Eq. (6.107) is approximated as $\begin{array} { r } { \int _ { \mathcal { R } - r } ^ { \mathcal { R } } d s f ( \tau - 2 s / c ) A ( s , r ) \sim } \end{array}$ $r f ( \tau - 2 \mathcal { R } / c ) A ( \mathcal { R } , r )$ , with $\begin{array} { r } { A ( \mathcal { R } , r ) \sim \int _ { \mathcal { R } } ^ { r + \mathcal { R } } p ^ { - ( n - 1 ) } d p \sim r \mathcal { R } ^ { - ( n - 1 ) } } \end{array}$ . This produces the estimate

$$
\frac { r ^ { 2 } } { \mathcal { R } ^ { n - 1 } } f ( \tau - 2 \mathcal { R } / c )
$$

for the first integral, and the $\mathcal { R }$ -independent part of this is $c ^ { - ( n - 1 ) } r ^ { 2 } f ^ { ( n - 1 ) } ( \tau )$ . The second integral of Eq. (6.107) involves the domain of integration $\mathcal { R } < s < \infty$ . Because $s$ is large compared with $r$ , we have the estimate $\begin{array} { r } { B \sim \int _ { s } ^ { r + s } p ^ { - ( n - 1 ) } d p \sim r s ^ { - ( n - 1 ) } } \end{array}$ . Inserting this inside the integral gives $\begin{array} { r } { r \int _ { \mathcal R } ^ { \infty } s ^ { - ( n - 1 ) } f ( \tau - 2 s / c ) d s } \end{array}$ , and repeated integration by parts returns an expression of the form

$$
\frac { r f ( \tau - 2 \mathcal { R } / c ) } { \mathcal { R } ^ { n - 2 } } + \frac { r f ^ { ( 1 ) } ( \tau - 2 \mathcal { R } / c ) } { c \mathcal { R } ^ { n - 3 } } + \frac { r f ^ { ( 2 ) } ( \tau - 2 \mathcal { R } / c ) } { c ^ { 2 } \mathcal { R } ^ { n - 4 } } + \cdot \cdot \cdot .
$$

The $\mathcal { R }$ -independent part of this is of the form $c ^ { - ( n - 2 ) } r f ^ { ( n - 2 ) } ( \tau )$ . Collecting results, we conclude that a crude estimate for Eq. (6.107) is

$$
\psi _ { \mathcal { W } } \sim \frac { 1 } { c ^ { n - 2 } } n ^ { \langle L \rangle } \Big [ f ^ { ( n - 2 ) } ( \tau ) + c r f ^ { ( n - 1 ) } ( \tau ) \Big ] \qquad \mathrm { ( n e a r ~ z o n e ) . }
$$

The estimate ignores numerical factors and all $\mathcal { R }$ -dependent terms. In Sec. 7.3.4 we will learn that these contributions can be completely ignored for all our purposes in this book.

The case $n = 2$ , for which $\mu$ falls off as $r ^ { - 2 }$ , is special because the functions $A$ and $B$ are now logarithmic in $\mathcal { R }$ and $s$ , and thus cannot be handled by our simple power-counting methods. We shall see that such terms are important in post-Minkowskian theory, and generate what are known as gravitational-wave “tails.” We perform these computations, and describe these effects, in Chapter 11.

<table><tr><td>Box 6.7</td><td>Solution to the wave equation</td></tr><tr><td></td><td>The solution to the wave equation  = -4π μ can be decomposedas γ=γN+ψw， where // is the near-zone portion ofthe integral overthe past light-cone&amp;(x) ofthe field point x,while</td></tr><tr><td rowspan="4"></td><td>w is the wave-zone portion.The boundary between the near and wave zones is placed at r&#x27;= R =</td></tr><tr><td>O(λc), where λc is a characteristic wavelength of the radiation. When the field point x = (ct, x) is in the wave zone,</td></tr><tr><td>N(x)= e！</td></tr><tr><td>l=0 n() dsf(t - 2s/)(s,r). γw(x)= r JR</td></tr></table>

And when $x$ is in the near zone,

$$
\begin{array} { l l l } { \displaystyle \psi _ { \mathcal { N } } ( x ) = \sum _ { \ell = 0 } ^ { \infty } \frac { ( - 1 ) ^ { \ell } } { \ell ! c ^ { \ell } } \bigg ( \frac { \partial } { \partial t } \bigg ) ^ { \ell } \int _ { \mathcal { M } } \mu ( t , \pmb { x } ^ { \prime } ) | \pmb { x } - \pmb { x } ^ { \prime } | ^ { \ell - 1 } d ^ { 3 } \pmb { x } ^ { \prime } , } \\ { \displaystyle \psi _ { \mathcal { W } } ( x ) = \frac { n ^ { ( L ) } } { r } \bigg \{ \int _ { \mathcal { R } - r } ^ { \mathcal { R } } d s f ( \tau - 2 s / c ) A ( s , r ) + \int _ { \mathcal { R } } ^ { \infty } d s f ( \tau - 2 s / c ) B ( s , r ) \bigg \} . } \end{array}
$$

Here $\tau : = t - r / c$ is retarded time, $\mathcal { M }$ is a surface of constant time bounded externally by the sphere $r ^ { \prime } = \mathcal { R } ,$ and $L$ is a multi-index that contains a number $\ell$ of individual spatial indices. For $\psi _ { \mathcal { H } }$ we have assumed that the source function $\mu$ is of the specific form

$$
\mu ( x ) = \frac { 1 } { 4 \pi } \frac { f ( \tau ) } { r ^ { n } } n ^ { \langle L \rangle } ,
$$

in which ${ \pmb n } = { \pmb x } / r$ , and we have defined

$$
A ( s , r ) : = \int _ { \mathcal { R } } ^ { r + s } \frac { P _ { \ell } ( \xi ) } { r ^ { \prime ( n - 1 ) } } d r ^ { \prime } , \qquad B ( s , r ) : = \int _ { s } ^ { r + s } \frac { P _ { \ell } ( \xi ) } { r ^ { \prime ( n - 1 ) } } d r ^ { \prime } ,
$$

where $\xi = ( r + 2 s ) / r - 2 s ( r + s ) / ( r r ^ { \prime } ) .$

# 6.4 Bibliographical notes

The formulation of the Einstein field equations detailed in Sec. 6.1 was first proposed by Landau and Lifshitz in their classic textbook The Classical Theory of Fields, now available in a fourth English edition (2000). Rigorous definitions for the total mass, momentum, and angular momentum of an asymptotically-flat spacetime were provided in a sequence of papers by Arnowitt, Deser, and Misner; their work is based on Hamiltonian methods, and is conveniently summarized in their 1962 review article.

The relaxation of the Einstein field equations described in Sec. 6.2 has become a standard tool of the field. The idea originated in Havas and Goldberg (1962), and it is beautifully summarized in Ehlers et al. (1976); another useful reference is Walker and Will (1980). The curved-spacetime formulation of the relaxed field equations in Box 6.3 was first proposed by Thorne and Kovacs (1975).

The mathematical methods introduced in Sec. 6.3 to integrate the wave equation when the source is extended over all space were first devised by Wiseman and Will (1991). They form the core of the DIRE approach (Direct Integration of the Relaxed Einstein equations) to post-Minkowskian theory, initiated by Will and Wiseman (1996) and developed systematically by Pati and Will (2000 and 2001). An alternative approach, based on a formal multipolar expansion of the potential outside the source, was pursued by Blanchet, Damour, Iyer, and their collaborators; this work is nicely summarized in Blanchet’s Living Reviews article (2006).

# 6.5 Exercises

6.1 Show that $g _ { \alpha \beta } = \sqrt { - \mathfrak { g } } \mathfrak { g } _ { \alpha \beta }$ , where ${ \mathfrak { g } } _ { \alpha \beta }$ is the matrix inverse to ${ \mathfrak { g } } ^ { \alpha \beta }$ , and $\mathfrak { g } = \mathrm { d e t } [ \mathfrak { g } ^ { \alpha \beta } ] =$ $g$ . If we define ${ \mathfrak { g } } ^ { \alpha \beta } : = \eta ^ { \alpha \beta } - h ^ { \alpha \beta }$ g, and $h ^ { \alpha \beta }$ is of order $G$ g, show that

$$
\begin{array} { c } { { ( - g ) = 1 - h + \displaystyle { \frac { 1 } { 2 } } h ^ { 2 } - \displaystyle { \frac { 1 } { 2 } } h ^ { \mu \nu } h _ { \mu \nu } + { \cal O } ( G ^ { 3 } ) , } } \\ { { g _ { \alpha \beta } = \eta _ { \alpha \beta } + h _ { \alpha \beta } - \displaystyle { \frac { 1 } { 2 } } h \eta _ { \alpha \beta } + h _ { \alpha \mu } h _ { ~ \beta } ^ { \mu } - \displaystyle { \frac { 1 } { 2 } } h h _ { \alpha \beta } } } \\ { { + \left( \displaystyle { \frac { 1 } { 8 } } h ^ { 2 } - \displaystyle { \frac { 1 } { 4 } } h ^ { \mu \nu } h _ { \mu \nu } \right) \eta _ { \alpha \beta } + { \cal O } ( G ^ { 3 } ) , } } \end{array}
$$

where indices on $h ^ { \alpha \beta }$ are lowered and contracted with the Minkowski metric.

6.2 Show that under the coordinate transformation $x ^ { \prime \mu } = f ^ { \mu } ( x ^ { \alpha } )$ ,

$$
\begin{array} { r } { \mathfrak { g } ^ { \mu ^ { \prime } \nu ^ { \prime } } = J ^ { - 1 } \partial _ { \alpha } f ^ { \mu } \partial _ { \beta } f ^ { \nu } \mathfrak { g } ^ { \alpha \beta } , } \\ { \partial _ { \nu ^ { \prime } } \mathfrak { g } ^ { \mu ^ { \prime } \nu ^ { \prime } } = \sqrt { - g ^ { \prime } } \Pi _ { g } f ^ { \mu } ( x ^ { \alpha } ) , } \end{array}
$$

where $J : = \operatorname* { d e t } [ \partial f ^ { \mu } / \partial x ^ { \alpha } ]$ is the Jacobian of the transformation, and where for any scalar function $f , \sqcap _ { g } f = ( - g ) ^ { - 1 / 2 } \partial _ { \beta } ( \mathfrak { g } ^ { \alpha \beta } \partial _ { \alpha } f )$ .

6.3 Consider the Schwarzschild metric in harmonic coordinates, given by Eqs. (5.171). Show explicitly that

$$
\begin{array} { l } { { \displaystyle { \mathfrak { g } } ^ { 0 0 } = - \frac { ( 1 + R / 2 r ) ^ { 3 } } { 1 - R / 2 r } , } } \\ { { \displaystyle { \mathfrak { g } } ^ { j k } = \delta ^ { j k } - \left( \frac { R } { 2 r } \right) ^ { 2 } n ^ { j } n ^ { k } , } } \end{array}
$$

where $R : = 2 G M / c ^ { 2 }$ , and verify that the harmonic gauge condition $\partial _ { \beta } { \mathfrak { g } } ^ { \alpha \beta } = 0$ i s satisfied.

6.4 Consider the potentials $h ^ { \alpha \beta }$ for a stationary source $( \partial _ { 0 } h ^ { \alpha \beta } = 0 )$ ), in harmonic gauge. Show that the conserved quantities for the spacetime can be written in terms of the following surface integrals at infinity:

$$
\begin{array} { l } { { { \cal M } = - { \displaystyle \frac { c ^ { 2 } } { 1 6 \pi G } } \oint _ { \infty } r ^ { 2 } { \frac { \partial h ^ { 0 } } { \partial r } } d \Omega , } } \\ { { { \cal P } ^ { j } = - { \displaystyle \frac { c ^ { 3 } } { 1 6 \pi G } } \oint _ { \infty } r ^ { 2 } { \frac { \partial h ^ { 0 j } } { \partial r } } d \Omega , } } \\ { { { \cal J } ^ { j k } = - { \displaystyle \frac { c ^ { 3 } } { 1 6 \pi G } } \oint _ { \infty } r ^ { 2 } { \frac { \partial } { \partial r } } \left( x ^ { j } h ^ { 0 k } - x ^ { k } h ^ { 0 j } \right) d \Omega , } } \\ { { { \cal R } ^ { j } = - { \displaystyle \frac { c ^ { 2 } } { 1 6 \pi G M } } \oint _ { \infty } r ^ { 4 } { \frac { \partial } { \partial r } } \left( { \displaystyle \frac { x ^ { j } h ^ { 0 0 } } { r ^ { 2 } } } \right) d \Omega , } } \end{array}
$$

where $d \Omega = \sin \theta d \theta d \phi$ is the element of solid angle.

6.5 Consider the stationary metric given by

$$
\begin{array} { l } { { d s ^ { 2 } = - \left( 1 - \frac { R } { r } \right) d ( c t ) ^ { 2 } - \frac { 4 G S } { c ^ { 2 } r } \sin ^ { 2 } \theta d \phi d t } } \\ { { \qquad + \left( 1 + \frac { R } { r } \right) \left( d r ^ { 2 } + r ^ { 2 } d \theta ^ { 2 } + r ^ { 2 } \sin ^ { 2 } \theta d \phi ^ { 2 } \right) , } } \end{array}
$$

which is accurate to first order in $G$ in a post-Minkowskian expansion; here $R =$ $2 G M / c ^ { 2 }$ and $S$ is a constant.

(a) Working to first order in $G$ , find ${ \mathfrak { g } } ^ { \alpha \beta }$ and verify that it is in the harmonic gauge. g(b) Using the surface integral formulation, find the mass, momentum, and angular momentum for this spacetime.

6.6 Using surface integrals, find the center-of-mass position of a spacetime for which

$$
h ^ { 0 0 } = { \frac { 4 G M } { c ^ { 2 } | x - a | } } ,
$$

where $\pmb { a }$ is a constant vector.

6.7 Verify that the harmonic energy-momentum pseudotensor is conserved, so that $\partial _ { \beta } [ ( - g ) t _ { \mathrm { H } } ^ { \alpha \beta } ] = 0$ .

6.8 Using the techniques of Sec. 6.3, find the solution to the wave equation $\square \psi = - 4 \pi \mu$ when $\boldsymbol { \mu } = - \boldsymbol { p } \cdot \nabla \delta ( \mathbf { x } ) \cos \omega t$ , with $\pmb { p }$ a constant vector. First take $x$ to be in the wave zone, and find the solution there; then take $x$ to be in the near zone. For the wave-zone expression, show that the sum over $\ell$ truncates. For the near-zone expression, show that the sum does not truncate. Compare your results with those of Box 6.6. Can you reconcile your results with the exact solution?

6.9 Using the techniques of Sec. 6.3, find the solution to the wave equation $\square \psi = - 4 \pi \mu$ when $\mu$ is equal to $\mu _ { 0 } ( r / r _ { 0 } ) ^ { 4 }$ for $r \textless r _ { 0 }$ , and to $\mu _ { 0 } ( r _ { 0 } / r ) ^ { 4 }$ for $r > r _ { 0 }$ . You may take $r _ { 0 }$ to be smaller than $\mathcal { R }$ . You should find that

$$
\psi = 4 \pi \mu _ { 0 } r _ { 0 } ^ { 2 } { \left[ { \frac { 2 } { 3 } } - { \frac { 1 } { 4 2 } } { \left( { \frac { r } { r _ { 0 } } } \right) } ^ { 6 } \right] }
$$

for $r \textless r _ { 0 }$ , and

$$
\psi = 4 \pi \mu _ { 0 } \frac { r _ { 0 } ^ { 3 } } { r } \biggl ( \frac { 8 } { 7 } - \frac { r _ { 0 } } { 2 r } \biggr )
$$

when $r > r _ { 0 }$ . Observe that while $\psi _ { \mathcal { N } }$ and $\psi _ { \mathcal W }$ both depend on $\mathcal { R }$ , the final outcome for $\psi$ is independent of $\mathcal { R }$ .

The theory was formulated in Chapter 6, and now we must get our hands dirty with its implementation. In this chapter we construct the second post-Minkowskian approximation to the metric of a curved spacetime produced by a bounded distribution of matter. For concreteness we choose the matter to consist of a perfect fluid. Our treatment allows the fluid to be of one piece (in the case of a single body), or broken up into a number of disconnected components (in the case of an $N$ -body system).

Although the post-Minkowskian approximation does not require slow motion, we shall nevertheless assume that the fluid is subjected to a slow-motion condition of the sort described in Sec. 6.3.2: if $v _ { c }$ is a characteristic velocity within the fluid, we insist that $v _ { c } / c \ll 1$ . This amounts to incorporating a post-Newtonian expansion within the post-Minkowskian approximation. We do this for two reasons. First, our ultimate goal is to describe situations of astrophysical interest, and the virial theorem implies that $U \sim v ^ { 2 }$ for any gravitationally bound system; weak fields are naturally accompanied by slow motion. Second, any attempt to keep the velocities arbitrary in the post-Minkowskian expansion quickly leads to calculations that are unmanageable, and we prefer to avoid these complications here.

We begin in Sec. 7.1 by assembling the required tools and exploring the general structure of the gravitational potentials in the near and wave zones. In Sec. 7.2 we perform the first iteration of the relaxed field equations, and the outcome of this calculation is used as input in the second iteration, carried out in Sec. 7.3 for the near zone, and in Sec. 7.4 for the wave zone. Our main results are summarized in Boxes 7.5 and 7.7.

Before we proceed it is perhaps useful to recall the main results of the preceding chapter. We saw that in the Landau–Lifshitz formulation of general relativity, the Einstein field equations take the form of a wave equation for the gravitational potentials $h ^ { \alpha \beta } : = \eta ^ { \alpha \beta } - \sqrt { - g } g ^ { \alpha \beta }$ , together with the harmonic-gauge condition $\partial _ { \beta } h ^ { \alpha \beta } = 0$ ; this is formally equivalent to the conservation equation $\partial _ { \beta } \tau ^ { \alpha \beta } = 0$ for the effective energymomentum pseudotensor, which acts as the source term in the wave equation. Each post-Minkowskian iteration of the wave equation gives rise to a new expression for the source, which is inserted back into the wave equation for the next iteration. After each iteration $h ^ { \alpha \beta }$ is expressed as an integral of the source over the past light cone of the field point $( t , \boldsymbol { x } )$ . Because the support of $\tau ^ { \alpha \beta }$ is not limited to the matter distribution, the domain of integration covers the entire light cone, and it is decomposed into a near-zone domain $\mathcal { N }$ and a wave-zone domain $\mathcal { W }$ ; the gravitational potentials are expressed as $h ^ { \alpha \beta } = h _ { { \mathcal { N } } } ^ { \alpha \beta } + h _ { { \mathcal { W } } } ^ { \alpha \beta }$ . The boundary between the near and wave zones is placed at an arbitrary radius $r = \mathcal { R }$ , with $\mathcal { R }$ chosen to be of the same order of magnitude as a characteristic wavelength of the gravitational radiation; while $h _ { \mathcal { N } } ^ { \alpha \beta }$ and $h _ { \mathcal { W } } ^ { \alpha \beta }$ individually depend on $\mathcal { R }$ , their sum is guaranteed to be independent of the cutoff radius, and this dependence can therefore be ignored.

And now onward with an explicit implementation of these ideas.

# 7.1 Assembling the tools

We begin by gathering the various tools, formulae, and assumptions that are required in implementation of the post-Minkowskian expansion. Our discussion here will set the stage for the various applications to come, to post-Newtonian theory (Chapters 8 to 10), to gravitational waves (Chapter 11), and to gravitational radiation reaction (Chapter 12).

# 7.1.1 Fluid variables

A description of the laws of fluid mechanics in curved spacetime was presented in Sec. 5.3. There we saw that the matter variables $\mathsf { m }$ that are relevant to a perfect fluid are the proper mass density $\rho$ , the proper internal energy density $\epsilon$ , the pressure $p$ , and the velocity field $u ^ { \alpha }$ . The energy-momentum tensor of a perfect fluid is

$$
T ^ { \alpha \beta } = ( \rho + \epsilon / c ^ { 2 } + p / c ^ { 2 } ) u ^ { \alpha } u ^ { \beta } + p g ^ { \alpha \beta } .
$$

The fluid dynamics is subjected to two conservation statements, a conservation of restmass expressed by $\nabla _ { \alpha } ( \rho u ^ { \alpha } ) = 0$ , and a conservation of energy-momentum expressed by $\nabla _ { \beta } T ^ { \alpha \beta } = 0$ .

For our purposes it is convenient to employ a slightly different set of matter variables. Noting that the components of $u ^ { \alpha }$ are not all independent (because of the normalization condition $g _ { \alpha \beta } u ^ { \alpha } u ^ { \beta } = - c ^ { 2 } ,$ ), we express the four-velocity field as

$$
u ^ { \alpha } = \gamma ( c , \pmb { v } ) ,
$$

in terms of a three-velocity field $\pmb { v }$ and a factor $\gamma : = u ^ { 0 } / c$ that can be determined in terms of $\pmb { v }$ by the normalization condition. Making the substitution within the equation of mass conservation, we find that it can be expressed in the form

$$
\partial _ { t } \rho ^ { * } + \partial _ { j } ( \rho ^ { * } v ^ { j } ) = 0 ,
$$

in terms of a rescaled mass density defined by

$$
\rho ^ { * } : = \sqrt { - g } \gamma \rho = \sqrt { - g } \rho u ^ { 0 } / c .
$$

To arrive at Eq. (7.3) we made use of the divergence identity of Eq. (5.40). Finally, we shall use $\Pi : = \epsilon / \rho$ instead of $\epsilon$ ; this is the fluid’s internal energy per unit mass. Our final set of matter variables is therefore

$$
\mathfrak { m } : = \{ \rho ^ { * } , p , \Pi , \pmb { \upsilon } \} ,
$$

and all other fluid variables can be determined in terms of this set.

The continuity equation (7.3) plays an important role in the description of a perfect fluid. We observe that unlike $\nabla _ { \beta } T ^ { \alpha \beta } = 0$ , which constrains the dynamics of the fluid, the statement of mass conservation is entirely kinematical in nature. Equation (7.3) states that the rest-mass of a fluid element does not change as we follow its motion within the fluid; this is tantamount to defining what one means by the phrase “fluid element,” and the statement is indeed a piece of the kinematical description of the fluid. This is quite distinct, for example, from the statement of the first law of thermodynamics, $d \Pi - ( p / \rho ^ { 2 } ) d \rho = 0$ (refer to Sec. 1.4.2), which is dynamical in nature.

We assume that the fluid is subjected to a slow-motion condition. Recalling the scaling quantities introduced in Sec. 6.3.2, we have that $r _ { c }$ is the radius of a sphere that surrounds the matter distribution, $t _ { c }$ is a characteristic time scale associated with the fluid motions, $v _ { c } = r _ { c } / t _ { c }$ is a characteristic velocity within the fluid, $\lambda _ { c } = c t _ { c }$ is a characteristic wavelength of the gravitational radiation produced by the moving fluid, and $m _ { c }$ is the characteristic mass of the matter distribution. We demand that $v _ { c } / c \ll 1$ , which implies that the fluid is situated deep within the near zone: $r _ { c } \ll \lambda _ { c }$ .

The slow-motion condition gives rise to a hierarchy between the components of the energy-momentum tensor. From Eq. (7.1) we have the approximate relations $T ^ { 0 0 } \simeq \rho ^ { * } c ^ { 2 }$ , $T ^ { 0 j } \simeq \rho ^ { * } v ^ { j } c$ , and $T ^ { j k } \simeq \rho ^ { * } v ^ { j } v ^ { k } + p \delta ^ { j k }$ , and these imply

$$
T ^ { 0 j } / T ^ { 0 0 } \sim v _ { c } / c , \qquad T ^ { j k } / T ^ { 0 0 } \sim ( v _ { c } / c ) ^ { 2 } .
$$

A glance at Eq. (6.51) then reveals that this hierarchy is inherited by the gravitational potentials:

$$
h ^ { 0 j } / h ^ { 0 0 } \sim v _ { c } / c , \qquad h ^ { j k } / h ^ { 0 0 } \sim ( v _ { c } / c ) ^ { 2 } .
$$

It is useful to express these relations more directly as

$$
T ^ { 0 0 } = O ( c ^ { 2 } ) , \qquad T ^ { 0 j } = O ( c ) , \qquad T ^ { j k } = O ( 1 ) ,
$$

and (taking into account the factor $c ^ { - 4 }$ in the field equations)

$$
h ^ { 0 0 } = O ( c ^ { - 2 } ) , \qquad h ^ { 0 j } = O ( c ^ { - 3 } ) , \qquad h ^ { j k } = O ( c ^ { - 4 } ) ,
$$

thereby introducing $c ^ { - 2 }$ as a post-Newtonian expansion parameter. This notation serves as a powerful mnemonic to judge the importance of various terms in a post-Newtonian expansion. But it is a notational shortcut that must be used with care; it should be remembered, for example, that a relation such as $T ^ { j k } = O ( 1 )$ really stands for something more meaningful, such as $T ^ { j k } / T ^ { 0 0 } \sim ( v _ { c } / c ) ^ { 2 }$ .

# 7.1.2 General structure of the potentials: Near zone

Having introduced the matter variables, the slow-motion condition, and the post-Newtonian hierarchy, we turn next to an examination of the general structure of the gravitational potentials $h ^ { \alpha \beta }$ . These are determined by the relaxed field equations

$$
\Pi h ^ { \alpha \beta } = - \frac { 1 6 \pi G } { c ^ { 4 } } \tau ^ { \alpha \beta } ,
$$

in which

$$
\tau ^ { \alpha \beta } = ( - g ) \big ( T ^ { \alpha \beta } + t _ { \mathrm { L L } } ^ { \alpha \beta } + t _ { \mathrm { H } } ^ { \alpha \beta } \big )
$$

is the effective energy-momentum pseudotensor of Eq. (6.52). We decompose the potentials as $h ^ { \alpha \beta } = h _ { { \mathcal { N } } } ^ { \alpha \beta } + h _ { { \mathcal { W } } } ^ { \alpha \bar { \beta } }$ , and first examine them when the field point $_ { x }$ is in the near zone, where $r : = | { \mathbf { } } x | < \mathcal { R }$ .

Consulting Box 6.7, we see that $h _ { \mathcal { N } } ^ { \alpha \beta }$ can be expressed as the expansion

$$
h _ { \mathcal { N } } ^ { \alpha \beta } ( t , { \boldsymbol { x } } ) = \frac { 4 G } { c ^ { 4 } } \sum _ { \ell = 0 } ^ { \infty } \frac { ( - 1 ) ^ { \ell } } { \ell ! c ^ { \ell } } \bigg ( \frac { \partial } { \partial t } \bigg ) ^ { \ell } \int _ { \mathcal { M } } \tau ^ { \alpha \beta } ( t , { \boldsymbol { x } } ^ { \prime } ) | { \boldsymbol { x } } - { \boldsymbol { x } } ^ { \prime } | ^ { \ell - 1 } d ^ { 3 } { \boldsymbol { x } } ^ { \prime } ,
$$

in which $\mathcal { M }$ is a surface of constant time bounded externally by $r ^ { \prime } : = | { \pmb x } ^ { \prime } | = \mathcal { R }$ . The first few terms are

$$
h _ { \mathcal { N } } ^ { \alpha \beta } ( t , x ) = \frac { 4 G } { c ^ { 4 } } \Bigg [ \int _ { \mathcal { M } } \frac { \tau ^ { \alpha \beta } ( t , x ^ { \prime } ) } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } - \frac { 1 } { c } \frac { d } { d t } \int _ { \mathcal { M } } \tau ^ { \alpha \beta } ( t , x ^ { \prime } ) d ^ { 3 } x ^ { \prime } \Bigg . \Bigg .
$$

and we see that each successive term comes with an additional factor of $c ^ { - 1 }$ , signifying that it is smaller than the previous term by a factor of order $v _ { c } / c \ll 1$ . This is our first encounter with a post-Newtonian expansion in powers of $c ^ { - 2 }$ , with fractional orders assigned to odd powers of $c ^ { - 1 }$ .

The expansion of Eq. (7.13) is a direct consequence of the relaxed field equations. It simplifies when we take into account the conservation statement $\partial _ { \beta } \tau ^ { \alpha \beta } = 0$ for the energymomentum pseudotensor. When we examine the expansion for $h _ { \mathcal { N } } ^ { 0 0 }$ , for example, we note that the second term is given by $\textstyle - \int _ { \mathcal { M } } \partial _ { 0 } \tau ^ { 0 0 } d ^ { 3 } x ^ { \prime }$ . The conservation statement allows us to make the substitution $\partial _ { 0 } \tau ^ { 0 0 } = - \partial _ { j } \tau ^ { 0 j }$ inside the integral, which can then, by Gauss’s theorem, be converted to a surface integral over $\partial \mathcal { M }$ , the boundary of the region $\mathcal { M }$ ; this is the surface $r ^ { \prime } = \mathcal { R }$ . The surface integral would vanish if $\tau ^ { 0 j }$ were confined to the near zone, and in this case the expansion for $h _ { \mathcal { N } } ^ { 0 0 }$ would skip the term at order $c ^ { - 1 }$ . In general, however, $\tau ^ { 0 j }$ extends beyond the near zone, and the surface integral does not vanish. But since $\tau ^ { 0 j }$ is constructed from the potentials, the surface integral can be estimated and shown to be of a very high order in the post-Newtonian expansion, well beyond any order that we will encounter in this book. In practice, therefore, we can appeal to energy conservation and eliminate the second term in the expansion for $h _ { \mathcal { N } } ^ { 0 0 }$ .

In fact, the conservation equations $\partial _ { \beta } \tau ^ { \alpha \beta } = 0$ can be put to good use to simplify and organize many terms in the expansion of $h _ { \mathcal { N } } ^ { \alpha \beta }$ . Particularly useful are a number of identities that follow from the conservation equations, namely,

$$
\begin{array} { l } { { \tau ^ { 0 j } = \partial _ { 0 } \big ( \tau ^ { 0 0 } x ^ { j } \big ) + \partial _ { k } \big ( \tau ^ { 0 k } x ^ { j } \big ) , } } \\ { { \tau ^ { j k } = \displaystyle \frac { 1 } { 2 } \partial _ { 0 0 } \big ( \tau ^ { 0 0 } x ^ { j } x ^ { k } \big ) + \frac { 1 } { 2 } \partial _ { p } \big ( 2 \tau ^ { p ( j } x ^ { k ) } - \partial _ { q } \tau ^ { p q } x ^ { j } x ^ { k } \big ) , } } \end{array}
$$

$$
\begin{array} { l } { { \tau ^ { 0 j } x ^ { k } = \displaystyle \frac { 1 } { 2 } \partial _ { 0 } \big ( \tau ^ { 0 0 } x ^ { j } x ^ { k } \big ) + \tau ^ { 0 [ j } x ^ { k ] } + \displaystyle \frac { 1 } { 2 } \partial _ { p } \big ( \tau ^ { 0 p } x ^ { j } x ^ { k } \big ) \ : , } } \\ { { \tau ^ { j k } x ^ { n } = \displaystyle \frac { 1 } { 2 } \partial _ { 0 } \big ( 2 \tau ^ { 0 ( j } x ^ { k ) } x ^ { n } - \tau ^ { 0 n } x ^ { j } x ^ { k } \big ) \qquad } } \\ { { \qquad + \displaystyle \frac { 1 } { 2 } \partial _ { p } \big ( 2 \tau ^ { p ( j } x ^ { k ) } x ^ { n } - \tau ^ { n p } x ^ { j } x ^ { k } \big ) \ : , } } \end{array}
$$

in which round and square brackets surrounding indices denote symmetrized and antisymmetrized combinations, respectively. Exploiting these identities, we find after some manipulations that the various components of the gravitational potentials are now given by

$$
\begin{array} { r l } { \varepsilon ^ { \prime \prime } } & { [ \mathcal { L } _ { \varepsilon } , \mathcal { R } - \varepsilon ^ { \prime \prime } ] ^ { \ell } } \\ & { = \frac { 1 } { \mathcal { L } _ { \varepsilon } ^ { 2 } } \frac { \partial ^ { 2 } \mathcal { L } _ { \varepsilon } ( t ) } { \partial t } ( \frac { 1 } { 2 } \varepsilon \gamma ^ { 2 } \varepsilon \gamma ^ { 2 } \varepsilon \gamma ^ { 2 } \varepsilon \gamma ^ { 2 } \varepsilon \gamma ^ { 3 } - \gamma \varepsilon ^ { \prime \prime } \varepsilon \gamma ^ { 2 } \varepsilon \gamma ^ { 3 } \varepsilon \gamma ^ { 3 }  } \\ & { \qquad - \frac { 1 } { \mathcal { L } _ { \varepsilon } ^ { 2 } } \frac { \partial ^ { 2 } \mathcal { L } _ { \varepsilon } ( t ) } { \partial t } \frac { 1 } { \partial \mathcal { L } _ { \varepsilon } } \frac { \partial ^ { 2 } \mathcal { L } _ { \varepsilon } ( t ) } { \partial t } \gamma \varepsilon ^ { 2 \prime } \gamma \varepsilon ^ { 3 } \varepsilon \gamma ^ { 2 } \gamma \varepsilon \gamma ^ { 3 }  } \\ & { \qquad  \frac { 1 } { 2 } \varepsilon \gamma ^ { 2 } \varepsilon \gamma ^ { 2 } \varepsilon \gamma \varepsilon \gamma ^ { 3 }  } \\ & { \qquad - 2 \partial \varepsilon \gamma ^ { 2 } ) \varepsilon \gamma \varepsilon \gamma ^ { 3 } \varepsilon \gamma ^ { 4 } \gamma \varepsilon \gamma ^ { 2 } \varepsilon \gamma ^ { 3 } } \\ & { \leq \frac { \partial ^ { 2 } \mathcal { L } _ { \varepsilon } ( t ) } { \partial t } [ \int _ { \varepsilon } \varepsilon \gamma ^ { 2 } \varepsilon \gamma ^ { 3 } \varepsilon \gamma ^ { 4 } ] ^ { \ell } \gamma \varepsilon \gamma ^ { 2 } \varepsilon \gamma ^ { 2 } \gamma \varepsilon \gamma ^ { 2 } \gamma \varepsilon \gamma ^ { 3 } \varepsilon \gamma \varepsilon \gamma ^ { 3 } \varepsilon \gamma ^ { 2 } \gamma \varepsilon \gamma ^ { 3 } } \\ & { \qquad - \frac { 1 } { \mathcal { R } _ { \varepsilon } ^ { 2 } } \gamma \gamma ^ { 2 } \gamma \varepsilon \gamma \gamma ^ { 3 } \varepsilon \gamma \varepsilon \gamma ^ { 3 } \varepsilon \gamma \varepsilon \gamma ^ { 3 } \varepsilon \gamma \varepsilon \gamma ^ { 3 }  } \\ & { \qquad - \partial \varepsilon \gamma \varepsilon \gamma ^ { 3 } ] ^ { \ell } \gamma \varepsilon \gamma ^ { 3 } \varepsilon \gamma ^ { 3 } \varepsilon \gamma \varepsilon \gamma ^ { 3 } \varepsilon \gamma ^ { 3 } \varepsilon \gamma \varepsilon \gamma ^ { 3 } } \\ &  \leq \varepsilon \gamma ^ { 4 } \int \end{array}
$$

in which $\tau ^ { \alpha \beta }$ is expressed as a function of $t$ and $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ inside the integrals, a number within brackets placed above a symbol such as $\mathcal { T } ^ { j k }$ indicates the number of differentiations with respect to time, and $h ^ { \alpha \beta } [ \partial \mathcal { M } ]$ denotes the collected surface terms generated during our manipulations of the integrals (the details will not be displayed here). We have also introduced the following notation for the multipole moments of the source $\tau ^ { \alpha \beta }$ :

$$
\begin{array} { l } { { \displaystyle { \mathcal { Z } } ^ { L } ( t ) : = \int _ { \mathcal { M } } c ^ { - 2 } \tau ^ { 0 0 } ( t , x ) x ^ { L } d ^ { 3 } x \ : , } } \\ { { \displaystyle { \mathcal { J } } ^ { j L } ( t ) : = \epsilon ^ { j a b } \int _ { \mathcal { M } } c ^ { - 1 } \tau ^ { 0 b } ( t , x ) x ^ { a L } d ^ { 3 } x \ : , } } \\ { { \displaystyle { \mathcal { M } } ^ { j k L } : = \int _ { \mathcal { M } } \tau ^ { j k } ( t , x ) x ^ { L } d ^ { 3 } x \ : , } } \end{array}
$$

in which $L$ is a multi-index containing a number $\ell$ of individual indices, so that $A ^ { L } : =$ $A ^ { j _ { 1 } j _ { 2 } \dots j _ { \ell } }$ and $x ^ { L } : = x ^ { j _ { 1 } } x ^ { j _ { 2 } } \ldots x ^ { j _ { \ell } }$ .

There is a lot to take in with the expansions of Eq. (7.15), and we shall now take the time to describe the structure of $h _ { \mathcal { N } } ^ { 0 0 }$ in some detail. We begin with the first term on the right-hand side of Eq. (7.15a), and observe that it leads off at order $c ^ { - 2 }$ with a Newtonian-like potential associated with the mass density $c ^ { - 2 } \tau ^ { 0 0 } \sim \rho ^ { * }$ . Embedded within this term are corrections of order $( v _ { c } / c ) ^ { 2 }$ and higher that enter the detailed expression for $\tau ^ { 0 0 }$ , as well as corrections of order $G$ and higher that arise in previous iterations of the relaxed field equations. But the leading contribution gives rise to Newtonian gravity.

The integral that appears in the second term in $h _ { \mathcal { N } } ^ { 0 0 }$ is known as a superpotential, because the factor $\vert x - x ^ { \prime } \vert$ appears in the numerator instead of the denominator; as we shall see, a superpotential is a potential sourced by another potential. Because of the time derivatives, this term leads off at order $c ^ { - 2 }$ relative to the Newtonian term, or at overall order $c ^ { - 4 } \operatorname { i n } h _ { \mathcal { N } } ^ { 0 0 }$ ; it is a “first post-Newtonian correction,” or 1pn correction, to the gravitational potential. It also contains higher-order corrections coming from higher-order terms in $c ^ { - 2 } \tau ^ { 0 0 }$ , just as we saw previously for the leading-order Newtonian term. It is instructive to note that the superpotential itself is of order $m _ { c } r$ , but since each time derivative produces a factor of $t _ { c } ^ { - 1 } = v _ { c } / r _ { c }$ , its contribution to $h _ { \mathcal { N } } ^ { 0 0 }$ is a factor of order $( v _ { c } / c ) ^ { 2 }$ smaller than the Newtonian potential when $r$ is comparable to $r _ { c }$ .

The third term in $h _ { \mathcal { N } } ^ { 0 0 }$ involves three time derivatives of $\mathcal { T } ^ { k k } ( t )$ , the trace of the mass quadrupole moment. The factor of $c ^ { - 3 }$ in front indicates that this term is a factor of order $( v _ { c } / c ) ^ { 3 }$ smaller than the leading Newtonian term, and therefore represents a $1 . 5 \mathrm { { P N } }$ contribution to the gravitational potential. We will show below that since this term depends on $t$ only, it can always be absorbed into a redefinition of the time coordinate, and therefore be removed by a coordinate transformation. This observation suggests that the $1 . 5 \mathrm { P N }$ term does not play a physical role, and we shall have occasion to show that such is indeed the case. The expression for the $1 . 5 \mathrm { P N }$ term displayed in Eq. (7.15a) is derived in Box 7.1.

The integral that appears in the fourth term in $h _ { \mathcal { N } } ^ { 0 0 }$ is sometimes called a superduperpotential because of the presence of $| { \boldsymbol { x } } - { \boldsymbol { x } } ^ { \prime } | ^ { 3 }$ in the numerator; a superduperpotential is a potential sourced by a superpotential. Because of the time derivatives, this term leads off at order $c ^ { - 4 }$ relative to the Newtonian term, and therefore represents a 2pn correction to the gravitational potential.

We now examine the fifth set of terms. The first member of the set involves the mass quadrupole moment differentiated five times with respect to time, and it scales as

$$
\frac { r _ { c } ^ { 2 } } { c ^ { 5 } } \frac { 1 } { t _ { c } ^ { 5 } } m _ { c } r _ { c } ^ { 2 } = \left( v _ { c } / c \right) ^ { 5 } \frac { m _ { c } } { r _ { c } } ,
$$

which is a correction of order $( v _ { c } / c ) ^ { 5 }$ relative to the Newtonian term. The other members have the same scaling, and this group of terms give rise to a $2 . 5 \mathrm { { p N } }$ correction to the gravitational potential. Unlike the $1 . 5 \mathrm { P N }$ term, this group depends on the spatial coordinates in addition to time, and it cannot be removed by a coordinate transformation. It gives rise to real, physical effects on the system. The nature of these effects can be anticipated from the fact that the $2 . 5 \mathrm { { p N } }$ terms involve an odd number of time derivatives, and are therefore antisymmetric under a time reflection $t  - t$ ; this is in contrast with the 1pn and 2pn terms, which are symmetric under the time reflection. This property is associated with dissipative processes taking place within the system, representing a radiative loss of energy to gravitational waves. The $2 . 5 \mathrm { { p N } }$ contributions to the gravitational potentials are known as radiation-reaction potentials, and their effects will be explored in detail in Chapter 12.

Turning next to the other components of the gravitational potentials, we observe that they have a very similar structure. The component $\bar { h } _ { \mathcal { N } } ^ { 0 j }$ leads off at order $c ^ { - 3 }$ with a Newtonianlike potential sourced by the mass-current density $c ^ { - 1 } \tau ^ { 0 j } \sim \rho ^ { * } v ^ { j }$ . Comparing this with the leading term in $h _ { \mathcal { N } } ^ { 0 0 }$ , we see that it is smaller by a factor of order $v _ { c } / c$ , and it would be tempting to assign a $0 . 5 \mathrm { { P N } }$ label to this term. As we shall see below, however, all effects arising from $h _ { \mathcal { N } } ^ { 0 j }$ will be the result of a coupling with other quantities that also scale as $v _ { c } / c$ ; the result is a 1pn correction to the leading Newtonian effect. Keeping this context in mind, it is appropriate to reset the post-Newtonian counter and to declare that the leading term in $\boldsymbol { h } _ { \mathcal { N } } ^ { 0 j }$ makes a 1pn contribution to the gravitational potentials. The expansion of $h _ { \mathcal { N } } ^ { 0 j }$ continues with a superpotential term at order which is assigned a 2pn label, and this is followed by $2 . 5 \mathrm { { P N } }$ contributions. The absence of a term at order $c ^ { - 4 }$ is a consequence of momentum conservation; the manipulations that led to the disappearance of the $c ^ { - 3 }$ term in $h _ { \mathcal { N } } ^ { 0 0 }$ lead to the same conclusion here, and in both cases we see that these terms are absorbed in the surface integrals $h ^ { \alpha \beta } [ \partial \mathcal { M } ]$ .

And finally, the components $h _ { \mathcal { N } } ^ { j k }$ lead off at order $c ^ { - 4 }$ with a Newtonian-like potential sourced by $\tau ^ { j k } \sim \rho ^ { * } v ^ { j } v ^ { k }$ ; this is smaller than the leading term in $h _ { \mathcal { N } } ^ { 0 0 }$ by a factor of order $( v _ { c } / c ) ^ { 2 }$ and represents a 1pn contribution to the gravitational potentials. The next term, involving a single time derivative, does not vanish; use of Eqs. (7.14c) and (7.14d) converts it to three time derivatives of the mass quadrupole moment. This term represents a $1 . 5 \mathrm { { P N } }$ contribution, and it is followed by a superpotential term at $2 \mathrm { P N }$ order, and a set of $2 . 5 \mathrm { { p N } }$ contributions.

The potentials $h _ { \mathcal { N } } ^ { \alpha \beta }$ provide the near-zone portion of the light-cone integral giving $h ^ { \alpha \beta }$ in terms of $\tau ^ { \alpha \beta }$ N , and we have yet to examine the wave-zone portion $h _ { \mathcal { W } } ^ { \alpha \beta }$ . We recall from $\operatorname { B o x } 6 . 7$ that this can be expressed as

$$
\begin{array} { c l } { { { \displaystyle h _ { \scriptscriptstyle \mathcal { W } } ^ { \alpha \beta } ( t , { \bf x } ) = \frac { 4 G } { c ^ { 4 } } \frac { n ^ { \langle L \rangle } } { r } \bigg \{ \int _ { \mathcal { R } - r } ^ { \mathcal { R } } d s f ^ { \alpha \beta } ( \tau - 2 s / c ) { \cal A } ( s , r ) } } } \\ { { { \displaystyle ~ + \int _ { \mathcal { R } } ^ { \infty } d s f ^ { \alpha \beta } ( \tau - 2 s / c ) { \cal B } ( s , r ) \bigg \} } , } } \end{array}
$$

when $\tau ^ { \alpha \beta }$ can be put in the specific form

$$
\tau ^ { \alpha \beta } = \frac { 1 } { 4 \pi } \frac { f ^ { \alpha \beta } ( \tau ) } { r ^ { n } } n ^ { \langle L \rangle } .
$$

Here $\tau = t - r / c$ is retarded time, $n ^ { \langle L \rangle }$ is an angular STF tensor of the sort introduced back in Sec. 1.5.3, and the functions $A ( s , r )$ and $B ( s , r )$ are defined by Eq. (6.104). Although restrictive, the expression of Eq. (7.18) is nevertheless useful because the wave-zone sources $\tau ^ { \alpha \beta }$ encountered below will always be decomposed in the elementary forms displayed in Eq. (7.19); the complete $h _ { \mathcal { W } } ^ { \alpha \beta }$ can then be obtained by summing over these elementary contributions.

Little more can be said about the general structure of $h _ { \mathcal { W } } ^ { \alpha \beta }$ in the near zone. The sources $f ^ { \alpha \beta }$ vanish in the first iteration of the relaxed field equations, because we are instructed to set $h ^ { \alpha \beta } = 0$ in $\tau ^ { \alpha \beta }$ and the material source is confined to the near zone. In the second and higher iterations, $h ^ { \alpha \beta }$ is no longer zero, and $\tau ^ { \alpha \beta }$ now extends into the wave zone; in these cases we have no choice but to plow through the detailed calculations to see what contribution $h _ { \mathcal { W } } ^ { \alpha \beta }$ might make. We encounter some of these calculations later in this chapter, and then again in Chapter 11.

<table><tr><td>Box 7.1</td><td>Radiation-reaction terms in the potentials Toillustrate how the various radiation-reaction terms arise in the potentials, we examine the contribution</td></tr><tr><td></td><td>1 a τ00(t,x&#x27;)(r²-2x.x&#x27;+r&#x27;2)d³x&#x27; 6c3 at</td></tr><tr><td></td><td>gral, giving -}c-2r²ə² Sn doto d3x&#x27;= }c-2r²ə² Suəjτ0j d3x&#x27;,which becomes a sur- face term, reflecting the fact that energy is conserved apart from a tiny flux of gravitational radiation. In the second term, x canbe brought outside the integral, giving }c-2xjδ² Su doτ0x&#x27;j d³x&#x27; = 3c-²xiə² S.n toi d3x&#x27; plusasurface term. This yields-}c-ixidt Sn dktki d3x&#x27;,which gives another surface term.The elimination of this term reflects the conservation of momentum.The third term</td></tr></table>

The next term in $h _ { \mathcal { N } } ^ { 0 0 }$ involving an odd number of time derivatives is

$$
\begin{array} { c } { { \displaystyle - \frac { 1 } { 1 2 0 c ^ { 5 } } \bigg ( \frac \partial { \partial t } \bigg ) ^ { 5 } \int _ { \mathcal { M } } \tau ^ { 0 0 } ( t , x ^ { \prime } ) \Big [ \mathrm { \small ~ \displaystyle } r ^ { 4 } - 4 r ^ { 2 } x \cdot x ^ { \prime } + 4 ( x \cdot x ^ { \prime } ) ^ { 2 } + 2 r ^ { 2 } r ^ { \prime 2 } } } \\ { { - 4 r ^ { \prime 2 } x \cdot x ^ { \prime } + r ^ { \prime 4 } \Big ] d ^ { 3 } x ^ { \prime } . } } \end{array}
$$

The first two terms can be shown to become surface integrals by appealing to the conservation identities of Eqs. (7.14), and the remaining four terms are displayed in Eq. (7.15a). Similar manipulations, albeit becoming progressively more complicated, yield the corresponding terms displayed in Eqs. (7.15) for $h _ { \mathcal { N } } ^ { 0 j }$ and $h _ { \mathcal { N } } ^ { j k }$ .

# 7.1.3 Near-zone metric

We will need to construct the spacetime metric $g _ { \alpha \beta }$ from the gravitational potentials $h ^ { \alpha \beta }$ . The link is provided by the gothic inverse metric ${ \mathfrak { g } } ^ { \alpha \beta } = \eta ^ { \alpha \beta } - h ^ { \alpha \beta }$ , which is related to the inverse metric $g ^ { \alpha \beta }$ by ${ \mathfrak { g } } ^ { \alpha \beta } = { \sqrt { - g } } g ^ { \alpha \beta }$ g. The inverse relation is $g _ { \alpha \beta } = \sqrt { - \mathfrak { g } } \mathfrak { g } _ { \alpha \beta }$ , in which ${ \mathfrak { g } } _ { \alpha \beta }$ gis the matrix inverse to ${ \mathfrak { g } } ^ { \alpha \beta }$ , and $\mathfrak { g } : = \operatorname* { d e t } [ \mathfrak { g } ^ { \alpha \beta } ]$ . Given that $h ^ { \alpha \beta }$ g gis of order $G$ , we can g g g gsolve these equations and obtain the metric and its inverse as post-Minkowskian expansions in powers of $G$ , and express the results in terms of the potentials $h ^ { \alpha \beta }$ . We find

$$
\begin{array} { l } { { g _ { \alpha \beta } = \eta _ { \alpha \beta } + h _ { \alpha \beta } - \frac { 1 } { 2 } h \eta _ { \alpha \beta } + h _ { \alpha \beta } h _ { \beta } ^ { \mu } - \frac { 1 } { 2 } h h _ { \alpha \beta } } } \\ { { \ \qquad + \left( \frac { 1 } { 8 } h ^ { 2 } - \frac { 1 } { 4 } h ^ { \mu \nu } h _ { \mu \nu } \right) \eta _ { \alpha \beta } + { \cal O } ( G ^ { 3 } ) , } } \\ { { g ^ { \alpha \beta } = \eta ^ { \alpha \beta } - h ^ { \alpha \beta } + \frac { 1 } { 2 } h ^ { \mu \nu \alpha \beta } - \frac { 1 } { 2 } h h ^ { \alpha \beta } } } \\ { { \ \qquad + \left( \frac { 1 } { 8 } h ^ { 2 } + \frac { 1 } { 4 } h ^ { \mu \nu } h _ { \mu \nu } \right) \eta ^ { \alpha \beta } + { \cal O } ( G ^ { 3 } ) , } } \\ { { \ \displaystyle ( - g ) = 1 - h + \frac { 1 } { 2 } h ^ { 2 } - \frac { 1 } { 2 } h ^ { \mu \nu } h _ { \mu \nu } + { \cal O } ( G ^ { 3 } ) , } } \\ { { \ \displaystyle \sqrt { - g } = 1 - \frac { 1 } { 2 } h + \frac { 1 } { 8 } h ^ { 2 } - \frac { 1 } { 4 } h ^ { \mu \nu } h _ { \mu \nu } + { \cal O } ( G ^ { 3 } ) . } } \end{array}
$$

It is understood that here, indices on $h ^ { \alpha \beta }$ are lowered with the Minkowski metric, so that $h _ { \alpha \beta } : = \eta _ { \alpha \mu } \eta _ { \beta \nu } h ^ { \mu \nu }$ and $h : = \eta _ { \mu \nu } h ^ { \mu \nu }$ .

In practice, the construction of the metric from the potentials depends on the context, which dictates the degree of accuracy required of each metric component. Suppose that we are specifically interested in determining the geodesic motion of a slowly-moving particle in the near zone of a weakly-curved spacetime. As we saw back in Sec. 5.2.3, the motion is governed by a Lagrangian $L$ given by

$$
\begin{array} { l } { { { \cal { L } } = - m c \sqrt { - g _ { \alpha \beta } \displaystyle \frac { d r ^ { \alpha } } { d t } \displaystyle \frac { d r ^ { \beta } } { d t } } } } \\ { { { \mathrm { } = - m c ^ { 2 } \sqrt { - g _ { 0 0 } - 2 g _ { 0 j } v ^ { j } / c - g _ { j k } v ^ { j } v ^ { k } / c ^ { 2 } } , } } } \end{array}
$$

where $r ^ { \alpha } = ( c t , r )$ describes the particle’s position in spacetime, and $v ^ { j } = d r ^ { j } / d t$ is its three-dimensional velocity vector. Newtonian gravity is reproduced by inserting the approximations $g _ { 0 0 } = - 1 + 2 U / c ^ { 2 } + O ( c ^ { - 4 } ) , g _ { 0 j } = O ( c ^ { - 3 } )$ , and $g _ { j k } = \delta _ { j k } + O ( c ^ { - 2 } )$ within the Lagrangian, and expanding the square root to order $c ^ { - 2 }$ ; this yields

$$
{ \cal L } = - m c ^ { 2 } + \frac { 1 } { 2 } m v ^ { 2 } + m U + { \cal O } ( c ^ { - 2 } ) ,
$$

in which $U$ is the Newtonian potential. The first term is an irrelevant constant, and we indeed recognize ${ \frac { 1 } { 2 } } m v ^ { 2 } + m U$ as the Lagrangian of Newtonian gravity; the remaining terms of order $c ^ { - 2 }$ are 1pn corrections. This simple exercise teaches us that a contribution of order $c ^ { - 2 }$ to $g _ { 0 0 }$ is a Newtonian term, but that a term of order $c ^ { - 2 }$ in $g _ { j k }$ is actually a post-Newtonian correction.

If we now want the post-Newtonian corrections to the motion, we must evaluate the Lagrangian to order $c ^ { - 2 }$ , and this requires calculation of the metric to the following orders of approximation:

$$
\begin{array} { r c l } { { { \cal O } ( c ^ { - 4 } ) } } & { { \mathrm { f o r } } } & { { g _ { 0 0 } , } } \\ { { { \cal O } ( c ^ { - 3 } ) } } & { { \mathrm { f o r } } } & { { g _ { 0 j } , } } \\ { { { \cal O } ( c ^ { - 2 } ) } } & { { \mathrm { f o r } } } & { { g _ { j k } . } } \end{array}
$$